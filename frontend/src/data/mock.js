export const mockData = {
  personal: {
    name: "ABHRANIL DAS",
    tagline: "AI/ML Specialist • Data Scientist • Machine Learning Engineer",
    email: "das.abhranil.2020@gmail.com",
    github: "https://github.com/Abhranil2021",
    linkedin: "https://www.linkedin.com/in/abhranildas2/",
    kaggle: "https://www.kaggle.com/abhranil123"
  },
  
  about: {
    title: "About Me",
    description: "AI/ML specialist with a strong foundation in data science and machine learning engineering. Graduated from IIT Guwahati with expertise in building end-to-end ML solutions, from data profiling tools to advanced neural networks. Passionate about leveraging AI to solve real-world problems through innovative approaches in computer vision, NLP, and predictive analytics.",
    education: {
      institution: "Indian Institute of Technology, Guwahati",
      degree: "Bachelor of Technology, Electronics and Electrical Engineering",
      duration: "2020 - 2024"
    }
  },

  skills: {
    categories: [
      {
        title: "Programming",
        items: ["Python", "C/C++", "SQL"]
      },
      {
        title: "ML Frameworks",
        items: ["NumPy", "Scikit-learn", "Statsmodels", "TensorFlow", "PyTorch", "HuggingFace"]
      },
      {
        title: "AI Specializations",
        items: ["Deep Learning", "Computer Vision", "Natural Language Processing", "Large Language Models", "Generative AI", "AI Agents"]
      },
      {
        title: "Databases and Data Analytics",
        items: ["Pandas", "Polars", "PySpark", "Matplotlib", "Seaborn", "Plotly", "MySQL", "MongoDB", "Databricks SQL"]
      },
      {
        title: "LLM & GenAI Tools",
        items: ["Transformers", "OpenAI", "FAISS", "ChromaDB", "Langchain", "NLTK", "SpaCy"]
      },
      {
        title: "Cloud/MLOps/Other Tools",
        items: ["FastAPI", "Docker", "Kubernetes", "MLFlow", "Databricks workspace"]
      }
    ]
  },

  experience: [
    {
      id: 1,
      title: "Data Scientist - Predictive Analytics",
      company: "Adani AI Labs",
      location: "Kolkata, India",
      duration: "Jul 2025 - Present",
      description: "• Placeholder text - Current role focusing on predictive analytics and AI solutions\n• More details to be added\n• Working on advanced ML models for business optimization",
      current: true
    },
    {
      id: 2,
      title: "Data Scientist Intern",
      company: "TVS Motor Company Ltd",
      location: "Bengaluru, India",
      duration: "May 2023 - Jul 2023",
      description: "• Designed a dataset-agnostic Data Profiling Tool that generates comprehensive data profiles for any dataset\n• Performed data cleaning and EDA on datasets with 50,000+ entries and 20+ features, achieving 90%+ scores across various metrics\n• Built interactive dashboard using Streamlit with 4.36 minutes average profiling time",
      current: false
    },
    {
      id: 3,
      title: "Machine Learning Engineer Intern",
      company: "Saptang Labs Pvt Ltd",
      location: "Chennai, India", 
      duration: "May 2022 - Jul 2022",
      description: "• Worked on Named Entity Recognition and Entity Linking for 50,000+ news articles\n• Fine-tuned DistilBERT model achieving 4.5 seconds average inference time\n• Created knowledge graphs using SpaCy for efficient information retrieval and semantic analysis",
      current: false
    }
  ],

  projects: [
    {
      id: 1,
      title: "Anomaly Detection in Surveillance Footages",
      description: "• End-to-end CNN + LSTM neural network for detecting anomalies in surveillance footage using TensorFlow\n• Achieved 94% accuracy with 10.2s inference time on Hockey Fight Detection Dataset\n• Deployed using Gradio for interactive demonstration",
      technologies: ["TensorFlow", "VGG16", "LSTM", "Gradio", "Computer Vision"],
      github: "#",
      demo: "#",
      featured: true
    },
    {
      id: 2, 
      title: "CaptionCraft: Image Captioning with Transformers",
      description: "• Image captioning application using Vision Transformer (ViT) and GPT2 decoder\n• Fine-tuned on Flickr 8K Dataset achieving ROUGE-L score of 0.28\n• Built with PyTorch and HuggingFace for comprehensive and contextually-rich captions",
      technologies: ["PyTorch", "HuggingFace", "ViT", "GPT2", "Transformers"],
      github: "#",
      demo: "#",
      featured: true
    },
    {
      id: 3,
      title: "LLM Prompt Recovery",
      description: "• Pipeline to recover prompts from AI-generated text using Gemma 2-2B-Instruct model\n• Fine-tuned with PEFT (QLoRA) achieving ROUGE-L score of 0.32 and SCS of 0.59\n• Developed advanced techniques for reverse-engineering AI text generation processes",
      technologies: ["Gemma", "PEFT", "QLoRA", "LLMs", "Fine-tuning"],
      github: "#", 
      demo: "#",
      featured: true
    },
    {
      id: 4,
      title: "Advanced Neural Architecture Search",
      description: "• Placeholder project - Automated neural architecture search system for optimizing deep learning models\n• Designed for cross-domain optimization across different datasets\n• Implements advanced AutoML techniques for model efficiency",
      technologies: ["AutoML", "Neural Search", "PyTorch", "Optimization"],
      github: "#",
      demo: "#",
      featured: false,
      placeholder: true
    },
    {
      id: 5,
      title: "Real-time ML Model Deployment Platform", 
      description: "• Placeholder project - Scalable platform for deploying and monitoring machine learning models in production\n• Real-time inference capabilities with monitoring dashboards\n• Built for enterprise-scale ML operations and model lifecycle management",
      technologies: ["MLOps", "Docker", "Kubernetes", "FastAPI", "Monitoring"],
      github: "#",
      demo: "#", 
      featured: false,
      placeholder: true
    }
  ],

  achievements: [
    {
      title: "Kaggle Notebooks Expert",
      description: "Best-ever rank of 3053 among more than 60k users on the platform"
    },
    {
      title: "JEE Advanced 2020",
      description: "Secured AIR 1871 among 1,50,000 candidates"
    },
    {
      title: "KVPY SX 2019", 
      description: "Obtained KVPY fellowship by securing an AIR of 303"
    }
  ],

  publications: [
    {
      title: "Smart Cabin for Office using Embedded Systems and Sensors",
      authors: "Anirban Dasgupta, Abhranil Das, Parishmita Deka, Soham Das",
      publication: "Smart Embedded Systems - Advances and Applications, CRC Press",
      year: "2023",
      doi: "9781032628059"
    },
    {
      title: "Few-Shot Glaucoma Classification from Fundus Images Using Meta-Learning Models",
      authors: "Anirban Dasgupta, Anwesha Sengupta and Abhranil Das", 
      publication: "7th International Conference on Signal Processing, Computing and Control (ISPCC 2k25), IEEE",
      year: "2025"
    }
  ]
};