# Abhranil Das - Portfolio Backend

A FastAPI-based backend service powering the portfolio frontend.  
Provides RESTful API endpoints for portfolio data, including personal info, skills, projects, achievements, and publications.  

---

## 🚀 Features

- ⚡ High-performance backend with **FastAPI**  
- 📦 MongoDB integration using **Motor** (async driver)  
- 🔄 Manual data migration with `mock.js` (upsert support)  
- 🔐 CORS middleware for secure frontend-backend communication  
- 📊 Built-in health/status checks  
- 🧩 Modular structure with routes, models, and services  

---

## 🛠 Tech Stack

- **Framework**: FastAPI  
- **Database**: MongoDB (Atlas)  
- **ODM/Driver**: Motor (async MongoDB driver)  
- **Config**: Pydantic + dotenv  
- **Deployment**: Render  

---

## ⚡ Quick Start

1. **Clone the repository**  
```bash
git clone https://github.com/Abhranil2021/PersonalPortfolio.git  
cd backend  
```

2. **Create virtual environment**  
```bash
python -m venv .venv  
source .venv/bin/activate   # On Windows: .venv\Scripts\activate  
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt  
```

4. **Set up environment variables**  
```bash
cp .env.example .env  
# Edit .env with your MongoDB URI and database names  
```

5. **Prepare your mock data**  
```bash
cp data/mock.example.js data/mock.js  
# Replace placeholder values with your personal information  
```

6. **Seed the database (required once before first run)**  
```bash
python migrate_data.py  
```

7. **Start the backend**  
```bash
uvicorn server:app --reload --host 0.0.0.0 --port 8000  
```

---

## 🔗 API Endpoints

**Base URL**:  
- Local: http://localhost:8000  
- Production: https://your-backend.onrender.com  

**Available endpoints (all prefixed with `/api`):**  

- `GET /api/` → Root check  
- `POST /api/status` → Insert a status check  
- `GET /api/status` → Get all status checks  
- `GET /api/portfolio` → Get complete portfolio data  
- `PUT /api/portfolio/personal` → Update personal info  
- `PUT /api/portfolio/about` → Update about section  

👉 Note: Provide only the **base URL** (e.g., `http://localhost:8000`) in your frontend `.env`, not the `/api` prefix.

⚠️ Note: In production, only GET /api/portfolio is publicly accessible.  
The PUT endpoints are for local/admin use only and should be protected or excluded from deployment.

---

## 📖 API Documentation

FastAPI provides interactive API documentation at:

- Swagger UI: `/docs`  
- ReDoc: `/redoc`  

Example:  
https://your-backend.onrender.com/docs 

---

## 📂 Project Structure

```text
backend/  
├── data/                  # Mock seed data (mock.js required)  
│   ├── mock.example.js     # Example data (safe to commit)  
│   └── mock.js             # Personal data (to be created, not committed)  
├── models/                 # Pydantic models  
│   └── portfolio.py  
├── routes/                 # API routes  
│   └── portfolio_routes.py  
├── services/               # Business logic & DB services  
│   └── portfolio_service.py  
├── .env                    # Environment variables  
├── .env.example            # Example env file  
├── migrate_data.py         # Data migration script  
├── requirements.txt        # Dependencies  
└── server.py               # FastAPI app entrypoint  
```

---

## ⚙️ Environment Variables

| Variable         | Description                 | Example |
|------------------|-----------------------------|---------|
| MONGO_URI        | MongoDB connection string   | mongodb+srv://... |
| DB_NAME          | Main portfolio DB name      | personal_info_collection |
| STATUS_DB_NAME   | Status checks DB name       | status_checks |
| CORS_ORIGINS     | Allowed frontend origins    | http://localhost:3000, https://personal-portfolio.vercel.app |

---

## 🔄 Data Migration (Required Before First Run)

This backend depends on seeded portfolio data.  
Before starting the server, you must run the migration script once to insert data into MongoDB:

    python migrate_data.py  

- Reads from `backend/data/mock.js`  
- Inserts or updates your personal portfolio information into MongoDB  
- Should be run **manually** before starting the backend for the first time  
- Not tied to backend startup (to avoid overwriting data on every deploy)  

After the migration, simply start the backend:

```bash
    uvicorn server:app --host 0.0.0.0 --port 8000  
```

---
---

## ☁️ Deployment (Render)

1. **Build Command**  
```bash
pip install -r backend/requirements.txt  
```

2. **Start Command**  
```bash
uvicorn server:app --host 0.0.0.0 --port $PORT  
```

3. **Environment Variables** (set in Render dashboard)  
   - MONGO_URI  
   - DB_NAME  
   - STATUS_DB_NAME  
   - CORS_ORIGINS  

---

## 🤝 Contributing

1. Fork the repository  
2. Create a feature branch  
3. Make your changes  
4. Run tests and linting  
5. Submit a pull request  

---

## 📜 License

© 2025 Abhranil Das. All rights reserved.

