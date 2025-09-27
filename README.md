# Abhranil Das - Personal Portfolio

A full-stack personal portfolio web application showcasing projects, skills, achievements, and publications.  

Built with a modern React frontend and a FastAPI backend powered by MongoDB Atlas.  

---

## 📸 Demo

- **Live Frontend**: [Vercel Deployment](https://personal-portfolio-gray-ten-12.vercel.app/)  
- **Live Backend**: [Render Deployment](https://personalportfolio-915l.onrender.com/docs)  

---

## 🚀 Features

- 🎨 **Modern UI** – Responsive, animated React + Tailwind design  
- ⚡ **FastAPI Backend** – High-performance Python backend with RESTful API  
- 📦 **MongoDB Atlas** – Cloud database for portfolio content  
- 🔄 **Data Migration** – Simple script (`migrate_data.py`) to seed/update portfolio info  
- ☁️ **CI/CD Deployment** – Frontend (Vercel) & Backend (Render) auto-deploy on push  
- 🔐 **CORS + Configurable Env Vars** – Secure integration between services  

---

## 🛠 Tech Stack

- **Frontend**: React 18, Tailwind CSS, Lucide Icons  
- **Backend**: FastAPI, Motor (async MongoDB driver), Pydantic  
- **Database**: MongoDB Atlas  
- **Deployment**: Vercel (frontend) & Render (backend)  
- **Config**: dotenv for environment variables  

---

## 📂 Repository Structure

```text
PersonalPortfolio/
├── backend/       # FastAPI backend (API, MongoDB integration, migration script)
├── frontend/      # React frontend (UI, API service, portfolio pages)
├── tests/         # Unit tests (frontend, backend)
└── README.md      # Root documentation (this file)
├── LICENSE        # License information
```

Each subproject has its own detailed README:

- [📘 Backend Docs](backend/README.md)

- [🎨 Frontend Docs](frontend/README.md)

## ⚡ Quick Start

1. **Clone the repository**

```bash
git clone https://github.com/Abhranil2021/PersonalPortfolio.git
cd PersonalPortfolio
```

2. **Set up Backend ([Instructions](backend/README.md))**

- Create `.env` with MongoDB connection info
- Copy `mock.example.js` → `mock.js` and add personal info
- Run `python migrate_data.py` to seed the database
- Start FastAPI with `uvicorn`

3. **Set up Frontend ([Instructions](frontend/README.md))**

- Install `npm` dependencies
- Create `.env` with backend base URL (e.g. http://localhost:8000)
- Start React dev server with `npm start`

## ☁️ Deployment

- Frontend → Deploy `frontend/` on Vercel
- Backend → Deploy `backend/` on Render
- Database → MongoDB Atlas cluster

Both are connected with CI/CD: push to GitHub → auto-build & redeploy.

## 🤝 Contributing

Contributions are welcome!

- Fork the repository
- Create a feature branch
- Make your changes
- Submit a pull request

## 📜 License

© 2025 Abhranil Das. All rights reserved.
