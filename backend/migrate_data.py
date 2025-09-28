#!/usr/bin/env python3
"""
Data migration script to populate database with mock.js data
"""
import asyncio
import sys
import os
from pathlib import Path
import json5    # to read mock.js file
from typing import Dict, Any
import logging

# Add backend directory to path
sys.path.append(str(Path(__file__).parent))

from services.portfolio_service import PortfolioService
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables
ROOT_DIR = Path(__file__).parent
load_dotenv(ROOT_DIR / '.env')

# Create logs directory
LOG_DIR = Path(__file__).parent / 'data' / 'logs'
LOG_DIR.mkdir(exist_ok = True)

# Configure logging
logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers = [logging.StreamHandler(), logging.FileHandler(LOG_DIR / 'server.log', encoding = 'utf-8')]
)
logger = logging.getLogger(__name__)

# Path to mock.js file
MOCK_DATA_PATH = os.environ.get('MOCK_DATA_PATH', Path(__file__).parent / 'data' / 'mock.js')

# function to load mock data from mock.js file
def load_mock_data() -> Dict[str, Any]:
    """
    Loads and parses portfolio data from the mock.js file.
    """
    # Check if file exists
    if not MOCK_DATA_PATH.exists():
        logger.error(f"Mock data file not found at: {MOCK_DATA_PATH}")
        raise FileNotFoundError(f"Mock data file not found at: {MOCK_DATA_PATH}")
    
    # Read the file content
    with open(MOCK_DATA_PATH, 'r', encoding = 'utf-8') as f:
        js_content = f.read()

    # Clean the content by removing the JS export statement and trailing semicolon
    js_object_string = js_content.replace('export const mockData = ', '').strip()
    if js_object_string.endswith(';'):
        js_object_string = js_object_string[:-1]
    
    # Parse the cleaned string using json5
    return json5.loads(js_object_string)

async def main():
    """Run data migration"""
    try:
        # load mock data from mock.js file
        MOCK_DATA = load_mock_data()
        if not MOCK_DATA:   
            logger.error("❌ Migration failed: Mock data is empty. Please check your mock.js file.")
            return
        
        # Connect to database
        mongo_uri = os.environ['MONGO_URI']
        client = AsyncIOMotorClient(mongo_uri)
        db = client[os.environ['DB_NAME']]
        
        # Create service
        service = PortfolioService(db)
        
        logger.info("Starting data migration...")
        
        # Migrate data
        success = await service.migrate_mock_data(MOCK_DATA)
        
        if success:
            logger.info("✅ Data migration completed successfully!")
            
            # Verify migration
            portfolio_data = await service.get_portfolio()
            
            # Convert to dict for easy access
            portfolio_dict = portfolio_data.model_dump()
            
            if portfolio_data:
                logger.info(f"✅ Verification passed:")
                logger.info(f"   - Portfolio: {portfolio_dict['portfolio']['personal']['name']}")
                logger.info(f"   - Skills: {len(portfolio_dict['skills'])} categories")
                logger.info(f"   - Experience: {len(portfolio_dict['experiences'])} entries")
                logger.info(f"   - Projects: {len(portfolio_dict['projects'])} projects")
                logger.info(f"   - Achievements: {len(portfolio_dict['achievements'])} achievements")
                logger.info(f"   - Publications: {len(portfolio_dict['publications'])} publications")
            else:
                logger.error("❌ Verification failed - no data found")
        else:
            logger.error("❌ Data migration failed!")
            
        # Close connection
        client.close()
        
    except Exception as e:
        logger.exception(f"❌ Migration error: {e}")

if __name__ == "__main__":
    asyncio.run(main())