from fastapi import FastAPI, APIRouter, Depends
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware
from motor.motor_asyncio import AsyncIOMotorClient
from motor.core import AgnosticDatabase
import os
import logging
from pathlib import Path
from pydantic import BaseModel, Field
from typing import List, AsyncGenerator
import uuid
from datetime import datetime, timezone
from contextlib import asynccontextmanager

# Import routes
from routes.portfolio_routes import router as portfolio_router

ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Configure logging
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# New Lifespan Manager for app startup and shutdown
@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup: Connect to the database
    mongo_url = os.environ['MONGO_URL']
    app.mongodb_client = AsyncIOMotorClient(mongo_url)
    app.database = app.mongodb_client[os.environ['DB_NAME']]
    logging.info("Attempting to establish MongoDB connection...")
    try:
        await app.database.command("ping")
        logging.info("MongoDB connection established.") 
    except Exception as e:
        logging.info(f"Failed to connect to MongoDB: {e}")
    
    yield
    
    # Shutdown: Close the database connection
    logging.info("Application shutdown...")
    app.mongodb_client.close()
    logging.info("MongoDB connection closed.")

# Create the main app without a prefix
app = FastAPI(title = "Portfolio API", version = "1.0.0", lifespan = lifespan)

# Create a router with the /api prefix
api_router = APIRouter(prefix = "/api")

# Dependency to get the database connection
def get_database(request) -> AgnosticDatabase:
    return request.app.database

# check for Pydantic BaseModel
class StatusCheck(BaseModel):
    id: str = Field(default_factory = lambda: str(uuid.uuid4()))
    client_name: str
    timestamp: datetime = Field(default_factory = datetime.now(timezone.utc))

class StatusCheckCreate(BaseModel):
    client_name: str

# Legacy routes (keep existing functionality)
@api_router.get("/")
async def root():
    return {"message": "Portfolio API is running"}

@api_router.post("/status", response_model = StatusCheck)
async def create_status_check(input: StatusCheckCreate, db: AgnosticDatabase = Depends(get_database)):
    status_dict = input.model_dump()
    status_obj = StatusCheck(**status_dict)
    _ = await db.status_checks.insert_one(status_obj.model_dump())
    return status_obj

@api_router.get("/status", response_model = List[StatusCheck])
async def get_status_checks(db: AgnosticDatabase = Depends(get_database)):
    status_checks = await db.status_checks.find().to_list(1000)
    return [StatusCheck(**status_check) for status_check in status_checks]

# Include all routers
app.include_router(api_router)
app.include_router(portfolio_router)

app.add_middleware(
    CORSMiddleware,
    allow_credentials = True,
    allow_origins = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8001)