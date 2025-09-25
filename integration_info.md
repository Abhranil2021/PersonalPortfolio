# Portfolio Backend Integration Information

## Overview
This document outlines the API contracts, data models, and integration strategy for converting the portfolio from mock data to a dynamic backend system.

## Current Mock Data Structure (mock.js)
- Personal information (name, tagline, contact links)
- About section (description, education)
- Skills (5 categories with technology lists)
- Experience (3 positions including current role)
- Projects (3 real + 2 placeholders)
- Achievements (3 items)
- Publications (2 research papers)

## Database Models

### 1. Portfolio Model
```javascript
{
  _id: ObjectId,
  userId: String, // For future multi-user support
  personal: {
    name: String,
    tagline: String,
    email: String,
    github: String,
    linkedin: String,
    kaggle: String
  },
  about: {
    title: String,
    description: String,
    education: {
      institution: String,
      degree: String,
      duration: String
    }
  },
  createdAt: Date,
  updatedAt: Date
}
```

### 2. Skill Categories Model
```javascript
{
  _id: ObjectId,
  portfolioId: ObjectId,
  title: String,
  items: [String],
  order: Number,
  createdAt: Date,
  updatedAt: Date
}
```

### 3. Experience Model
```javascript
{
  _id: ObjectId,
  portfolioId: ObjectId,
  title: String,
  company: String,
  location: String,
  duration: String,
  description: String,
  current: Boolean,
  order: Number,
  createdAt: Date,
  updatedAt: Date
}
```

### 4. Projects Model
```javascript
{
  _id: ObjectId,
  portfolioId: ObjectId,
  title: String,
  description: String,
  technologies: [String],
  github: String,
  demo: String,
  featured: Boolean,
  placeholder: Boolean,
  order: Number,
  createdAt: Date,
  updatedAt: Date
}
```

### 5. Achievements Model
```javascript
{
  _id: ObjectId,
  portfolioId: ObjectId,
  title: String,
  description: String,
  order: Number,
  createdAt: Date,
  updatedAt: Date
}
```

### 6. Publications Model
```javascript
{
  _id: ObjectId,
  portfolioId: ObjectId,
  title: String,
  authors: String,
  publication: String,
  year: String,
  doi: String,
  order: Number,
  createdAt: Date,
  updatedAt: Date
}
```

## API Endpoints

### Portfolio Management
- `GET /api/portfolio` - Get complete portfolio data
- `PUT /api/portfolio/personal` - Update personal information
- `PUT /api/portfolio/about` - Update about section

### Skills Management
- `GET /api/skills` - Get all skill categories
- `POST /api/skills` - Create new skill category
- `PUT /api/skills/:id` - Update skill category
- `DELETE /api/skills/:id` - Delete skill category

### Experience Management
- `GET /api/experience` - Get all experience entries
- `POST /api/experience` - Create new experience
- `PUT /api/experience/:id` - Update experience
- `DELETE /api/experience/:id` - Delete experience

### Projects Management
- `GET /api/projects` - Get all projects
- `POST /api/projects` - Create new project
- `PUT /api/projects/:id` - Update project
- `DELETE /api/projects/:id` - Delete project

### Achievements Management
- `GET /api/achievements` - Get all achievements
- `POST /api/achievements` - Create new achievement
- `PUT /api/achievements/:id` - Update achievement
- `DELETE /api/achievements/:id` - Delete achievement

### Publications Management
- `GET /api/publications` - Get all publications
- `POST /api/publications` - Create new publication
- `PUT /api/publications/:id` - Update publication
- `DELETE /api/publications/:id` - Delete publication

### Data Migration
- `POST /api/migrate` - Migrate mock.js data to database
- `GET /api/export` - Export database data to JSON format

## Frontend Integration Strategy

### Data Loading
1. Replace mock.js imports with API calls
2. Use React hooks (useState, useEffect) for data management
3. Implement loading states and error handling
4. Maintain same component structure and props

### API Integration Points
- `Portfolio.jsx` component will fetch data on mount
- Individual sections will use the fetched data
- Keep existing component structure intact
- Add loading spinners for better UX

### Error Handling
- Fallback to cached data if API fails
- Display user-friendly error messages
- Implement retry mechanisms for failed requests

## Data Migration Plan
1. Create seed script to populate database with mock.js data
2. Add migration endpoint to transfer data
3. Validate data integrity after migration
4. Switch frontend to use API endpoints
5. Keep mock.js as backup reference

## Backup & Export Strategy
- Regular database backups
- Export functionality to JSON format
- Ability to restore from backup
- Version control for content changes

## Future Enhancements
- Admin dashboard for content management
- Image upload for projects/profile
- Content versioning and history
- SEO optimization with dynamic meta tags
- Analytics integration