// API Configuration
export const API_CONFIG = {
  BASE_URL: process.env.REACT_APP_API_URL || 'http://localhost:8000/api',
  TIMEOUT: 10000, // 10 seconds
  RETRY_ATTEMPTS: 3,
  RETRY_DELAY: 1000, // 1 second
};

// Application Constants
export const APP_CONFIG = {
  TITLE: process.env.REACT_APP_TITLE || 'Portfolio App',
  DESCRIPTION: 'AI/ML Specialist with expertise in machine learning, computer vision, and data science.',
  KEYWORDS: ['AI', 'Machine Learning', 'Data Science', 'Computer Vision', 'NLP', 'Python'],
  AUTHOR: 'Abhranil Das',
};

// Navigation Sections
export const NAVIGATION_SECTIONS = [
  { id: 'hero', label: 'Home' },
  { id: 'about', label: 'About' },
  { id: 'skills', label: 'Skills' },
  { id: 'experience', label: 'Experience' },
  { id: 'projects', label: 'Projects' },
  { id: 'publications', label: 'Publications' },
  { id: 'contact', label: 'Contact' }
];

// Skill Icons Mapping
export const SKILL_ICONS = {
  "Programming": "Code",
  "ML Frameworks": "Brain",
  "AI Specializations": "Brain",
  "Data Processing & Analytics": "Database",
  "Databases and Data Analytics": "Database",
  "LLM & GenAI Tools": "Brain",
  "Cloud/MLOps/Other Tools": "Cloud",
  "MLOps/Cloud Tools": "Cloud"
};

// Animation Delays
export const ANIMATION_DELAYS = {
  SECTION_FADE: 100,
  CARD_STAGGER: 150,
  TEXT_TYPING: 50,
};

// Breakpoints (matching Tailwind)
export const BREAKPOINTS = {
  SM: '640px',
  MD: '768px',
  LG: '1024px',
  XL: '1280px',
  '2XL': '1536px',
};

// Error Messages
export const ERROR_MESSAGES = {
  NETWORK_ERROR: 'Failed to connect to the server. Please check your internet connection.',
  API_ERROR: 'Failed to load portfolio data. Please try again later.',
  TIMEOUT_ERROR: 'Request timed out. Please try again.',
  UNKNOWN_ERROR: 'An unexpected error occurred. Please try again.',
};

// Loading Messages
export const LOADING_MESSAGES = [
  'Loading portfolio...',
  'Fetching latest data...',
  'Almost ready...',
];


// Theme Colors
export const THEME_COLORS = {
  PRIMARY: '#3b82f6',
  SECONDARY: '#8b5cf6',
  ACCENT: '#06b6d4',
  SUCCESS: '#10b981',
  WARNING: '#f59e0b',
  ERROR: '#ef4444',
  DARK: '#111827',
  LIGHT: '#f9fafb',
};

// Local Storage Keys
export const STORAGE_KEYS = {
  THEME: 'portfolio_theme',
  LAST_VISIT: 'portfolio_last_visit',
  USER_PREFERENCES: 'portfolio_preferences',
};

// Feature Flags
export const FEATURES = {
  DARK_MODE_TOGGLE: false,
  ANALYTICS: process.env.NODE_ENV === 'production',
  SERVICE_WORKER: process.env.NODE_ENV === 'production',
  ERROR_REPORTING: process.env.NODE_ENV === 'production',
};

// Performance Monitoring
export const PERFORMANCE = {
  ENABLE_MONITORING: process.env.NODE_ENV === 'production',
  SAMPLE_RATE: 0.1,
};

// Cache Configuration
export const CACHE_CONFIG = {
  PORTFOLIO_TTL: 5 * 60 * 1000, // 5 minutes
  IMAGES_TTL: 24 * 60 * 60 * 1000, // 24 hours
};