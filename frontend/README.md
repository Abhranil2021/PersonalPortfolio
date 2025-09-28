# Abhranil Das - Portfolio Frontend

A modern, responsive portfolio website built with React showcasing AI/ML expertise, projects, and achievements.  

---

## 📸 Demo

- **Live Site**: [personal-portfolio-vercel](https://personal-portfolio-gray-ten-12.vercel.app/)

---

## 🚀 Features

- 🎨 Modern, clean design with smooth animations  
- 📱 Fully responsive across devices  
- ⚡ Optimized for fast performance  
- 🔄 Real-time data fetching from FastAPI backend  
- 🎯 SEO-friendly with meta tags  
- ♿ Accessible design following WCAG guidelines  
- 🌐 Cross-browser compatibility  

---

## 🛠 Tech Stack

- **Frontend**: React, Tailwind CSS, Lucide Icons  
- **Backend Integration**: FastAPI (custom API service with error handling)  
- **State Management**: React Hooks  
- **Build Tool**: Create React App  
- **Styling**: Tailwind CSS with custom animations  

---

## ⚡ Quick Start

1. **Clone the repository**  
```bash
git clone https://github.com/Abhranil2021/PersonalPortfolio.git  
cd frontend  
```

2. **Install dependencies**  
```bash
npm install  
```

3. **Set up environment variables**  
```bash
cp .env.example .env  
# Edit `.env` with your backend base URL (e.g., http://localhost:8000)  
```

4. **Start development server**  
```bash
npm start  
```

5. **Open in browser**  
Navigate to http://localhost:3000  

---

## 🔗 Backend Integration

- Backend: [FastAPI Service](../backend/README.md)  
- Default backend URL: http://localhost:8000  

The frontend expects these API endpoints (all prefixed with `/api`):  

- `GET /api/portfolio` → Complete portfolio data  
- `PUT /api/portfolio/personal` → Update personal info  
- `PUT /api/portfolio/about` → Update about section  

⚠️ Note: In production, only `GET /api/portfolio` is publicly accessible.  
The `PUT` endpoints are for local/admin use only and should be protected or excluded from deployment.  

---

## 📂 Project Structure

```text
frontend/  
├── public/           # Static files and HTML template  
├── src/  
│   ├── components/   # React components  
│   ├── hooks/        # Custom React hooks  
│   ├── services/     # API service layer  
│   ├── styles/       # Global styles  
│   └── utils/        # Constants and utilities  
├── package.json      # Dependencies and scripts  
├── .env              # Environment variables  
├── .env.example      # Example env file  
└── README.md         # Instructions for Frontend Setup  
```

---

## ⚙️ Environment Variables

| Variable            | Description              | Default                  |
|---------------------|--------------------------|--------------------------|
| REACT_APP_API_URL   | Backend base URL         | http://localhost:8000    |
| REACT_APP_TITLE     | Application title        | Portfolio App            |
| REACT_APP_AUTHOR    | Application author       | Portfolio Author         |

---

## ☁️ Deployment

1. **Build the project**  
```bash
npm run build  
```

2. **Deploy the `build` folder** to your hosting service of choice:  
   - Vercel (recommended)  
   - Netlify  
   - AWS S3 + CloudFront  
   - GitHub Pages  

On Vercel, deployments are automatic from the main branch if connected to GitHub.
Preview deployments are also generated for pull requests and feature branches.

---

## 🌍 Browser Support

- Chrome 90+  
- Firefox 88+  
- Safari 14+  
- Edge 90+  

---

## 📊 Performance

| Metric                  | Mobile  | Desktop |
|-------------------------|---------|---------|
| Real Experience Score   | 100     | 99      |
| First Contentful Paint  | 0.77s   | 1.29s   |
| Largest Contentful Paint| 1.44s   | 2.19s   |
| Time to First Byte      | 0.19s   | 0.22s   |
| Cumulative Layout Shift | 0.0     | 0.0     |

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
