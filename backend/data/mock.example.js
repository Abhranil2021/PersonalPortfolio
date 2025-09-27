/**
 * NOTE:
 * This is a placeholder dataset for demonstration purposes.
 * 
 * To personalize this project:
 *  
 * 1. Copy this file and rename it to `mock.js` inside the same folder (`backend/data`), or create a new file named `mock.js` and copy the contents of this file there.
 * 2. Replace the placeholder values with your real personal information.
 * 3. DO NOT commit `mock.js` if your repository is public, as it may contain sensitive data. Place it in `.gitignore` to avoid accidental commits.
 * 4. Run the migration script manually to seed your MongoDB database:
 * 
 *    python migrate_data.py
 * 
 * The backend will then use the data from your database, not from this file.
 */

export const mockData = {
  personal: {
    name: "John Doe",
    tagline: "AI/ML Specialist • Data Scientist • Machine Learning Engineer",
    email: "johndoe@example.com",
    github: "https://github.com/johndoe",
    linkedin: "https://www.linkedin.com/in/johndoe/",
    kaggle: "https://www.kaggle.com/johndoe"
  },
  
  about: {
    title: "About Me",
    description: "Passionate about artificial intelligence, data science, and solving real-world problems with machine learning.",
    education: {
      institution: "Tech University",
      degree: "Bachelor of Technology in Computer Science",
      duration: "2018 - 2022"
    }
  },

  skills: {
    categories: [
      { title: "Programming", items: ["Python"] },
      { title: "ML Frameworks", items: ["NumPy", "Scikit-learn", "TensorFlow", "PyTorch"] },
      { title: "AI Specializations", items: ["Deep Learning", "Computer Vision", "NLP"] },
      { title: "Databases", items: ["Pandas", "MongoDB", "MySQL"] },
      { title: "LLM & GenAI Tools", items: ["Transformers", "OpenAI", "Langchain"] },
      { title: "Cloud/MLOps/Other Tools", items: ["FastAPI", "Docker", "Kubernetes"] }
    ]
  },

  experience: [
    {
      id: 1,
      title: "Data Scientist",
      company: "TechCorp",
      location: "Remote",
      duration: "Jul 2024 - Present",
      description: "• Building predictive analytics models\n• Deploying ML models into production\n• Collaborating with cross-functional teams",
      current: true
    },
    {
      id: 2,
      title: "Machine Learning Intern",
      company: "Innovate Labs",
      location: "New York, USA",
      duration: "May 2023 - Jul 2023",
      description: "• Developed data profiling tools\n• Built interactive dashboards\n• Conducted exploratory data analysis",
      current: false
    }
  ],

  projects: [
    {
      id: 1,
      title: "Smart Health Monitoring System",
      description: "An IoT + ML powered system that tracks patient vitals and predicts potential health risks.",
      technologies: ["Python", "TensorFlow", "IoT", "FastAPI"],
      github: "https://github.com/johndoe/health-monitor",
      demo: "#",
      featured: true
    },
    {
      id: 2, 
      title: "Movie Recommendation Engine",
      description: "Personalized recommendation system using collaborative filtering and NLP-based content analysis.",
      technologies: ["Scikit-learn", "Pandas", "NLP"],
      github: "https://github.com/johndoe/movie-recommender",
      demo: "#",
      featured: true
    },
    {
      id: 3, 
      title: "E-commerce Analytics Dashboard",
      description: "Interactive dashboard providing sales insights and customer behavior analysis.",
      technologies: ["React", "FastAPI", "MongoDB", "Plotly"],
      github: "https://github.com/johndoe/ecommerce-dashboard",
      demo: "#",
      featured: false
    },
  ],

  achievements: [
    { title: "Hackathon Finalist", description: "Reached finals in a national hackathon." },
    { title: "Dean’s List", description: "Recognized for academic excellence." }
  ],

  publications: [
    {
      title: "Deep Learning for Image Classification",
      authors: "John Doe, Jane Smith",
      publication: "International Conference on AI",
      year: "2023"
    }
  ]
};
