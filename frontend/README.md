# Abhranil Das - Portfolio Frontend

A modern, responsive portfolio website built with React showcasing AI/ML expertise, projects, and achievements.

## Features

- 🎨 Modern, clean design with smooth animations
- 📱 Fully responsive across all devices  
- ⚡ Fast loading with optimized performance
- 🔄 Real-time data fetching from FastAPI backend
- 🎯 SEO optimized with meta tags
- ♿ Accessible design following WCAG guidelines
- 🌐 Cross-browser compatibility

## Tech Stack

- **Frontend**: React 18, Tailwind CSS, Lucide Icons
- **Backend Integration**: Custom API service with error handling
- **State Management**: React Hooks with custom portfolio hook
- **Build Tool**: Create React App
- **Styling**: Tailwind CSS with custom animations

## Quick Start

1. **Clone the repository**
```bash
   git clone <repository-url>
   cd frontend
```

2. **Install dependencies**
```bash
   npm install
```

3. **Set up environment**

```bash   
   cp .env.example .env
   # Edit .env with your API URL
```

4. **Start development server**

```bash   
   npm start
```

5. **Open in browser**

Navigate to http://localhost:3000

## Backend Integration

Ensure your FastAPI backend is running on `http://localhost:8000` or update the `REACT_APP_API_URL` in your `.env` file.

The frontend expects these API endpoints:

- `GET /api/portfolio` - Complete portfolio data
- `PUT /api/portfolio/personal` - Update personal info
- `PUT /api/portfolio/about` - Update about section

## Project Structure

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
└── .env             # Environment variables
```

## Available Scripts

- `npm start` - Start development server
- `npm build` - Build for production
- `npm test` - Run tests
- `npm run lint` - Run ESLint
- `npm run format` - Format code with Prettier

## Deployment

1. **Build the project**

```bash   
   npm run build
```

2. **Deploy the `build` folder to your preferred hosting service:**
    - Netlify
    - Vercel
    - AWS S3 + CloudFront
    - GitHub Pages

## Environment Variables

| Variable          | Description          | Default                  |
|-------------------|----------------------|--------------------------|
| `REACT_APP_BACKEND_URL` | Backend API URL       | `http://localhost:8000/api` |
| `REACT_APP_TITLE`   | Application title     | Portfolio title          |
| `REACT_APP_DEBUG`   | Enable debug mode     | `false`                  |

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Performance

- Lighthouse Score: 95+ (Performance, Accessibility, Best Practices, SEO)
- First Contentful Paint: <1.5s
- Largest Contentful Paint: <2.5s

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and linting
5. Submit a pull request

## License

© 2025 Abhranil Das. All rights reserved.