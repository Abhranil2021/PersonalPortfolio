import React, { useState, useEffect } from 'react';
import { Menu, X, Github, Linkedin, Mail, ExternalLink,  Code, Brain, Database, Cloud, Loader2 } from 'lucide-react';
import { API_CONFIG } from '../utils/constants';

// API Configuration
const API_BASE_URL = API_CONFIG.BASE_URL;

// API Service
class PortfolioAPI {
  static async fetchPortfolio() {
    try {
      const response = await fetch(`${API_BASE_URL}/api/portfolio`);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.error('Error fetching portfolio:', error);
      throw error;
    }
  }

  static async updatePersonalInfo(updates) {
    try {
      const response = await fetch(`${API_BASE_URL}/api/portfolio/personal`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updates),
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.error('Error updating personal info:', error);
      throw error;
    }
  }

  static async updateAboutSection(updates) {
    try {
      const response = await fetch(`${API_BASE_URL}/api/portfolio/about`, {
        method: 'PUT',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updates),
      });
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      return await response.json();
    } catch (error) {
      console.error('Error updating about section:', error);
      throw error;
    }
  }
}

const Portfolio = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [scrollY, setScrollY] = useState(0);
  const [activeSection, setActiveSection] = useState('hero');
  const [portfolioData, setPortfolioData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const handleScroll = () => setScrollY(window.scrollY);
    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  useEffect(() => {
    const handleScroll = () => {
      const sections = ['hero', 'about', 'skills', 'experience', 'projects', 'achievements', 'publications', 'contact'];
      const scrollPosition = window.scrollY + 100;

      for (const section of sections) {
        const element = document.getElementById(section);
        if (element) {
          const { offsetTop, offsetHeight } = element;
          if (scrollPosition >= offsetTop && scrollPosition < offsetTop + offsetHeight) {
            setActiveSection(section);
            break;
          }
        }
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // Fetch portfolio data on component mount
  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const data = await PortfolioAPI.fetchPortfolio();
        setPortfolioData(data);
        setError(null);
      } catch (err) {
        setError('Failed to load portfolio data. Please try again later.');
        console.error('Portfolio fetch error:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  const scrollToSection = (sectionId) => {
    document.getElementById(sectionId)?.scrollIntoView({ behavior: 'smooth' });
    setIsMenuOpen(false);
  };

  // Loading state
  if (loading) {
    return (
      <div className="min-h-screen bg-gray-900 text-white flex items-center justify-center">
        <div className="text-center">
          <Loader2 className="animate-spin w-12 h-12 mx-auto mb-4 text-blue-400" />
          <p className="text-gray-400 font-light">Loading portfolio...</p>
        </div>
      </div>
    );
  }

  // Error state
  if (error || !portfolioData) {
    return (
      <div className="min-h-screen bg-gray-900 text-white flex items-center justify-center">
        <div className="text-center max-w-md mx-auto px-4">
          <div className="bg-red-900/20 border border-red-500/30 rounded-lg p-6">
            <p className="text-red-400 mb-4">{error || 'Failed to load portfolio data'}</p>
            <button 
              onClick={() => window.location.reload()} 
              className="bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 text-sm font-light transition-colors"
            >
              Retry
            </button>
          </div>
        </div>
      </div>
    );
  }

  const { portfolio, skills, experiences, projects, achievements, publications } = portfolioData;

  const skillIcons = {
    "Programming": Code,
    "ML Frameworks": Brain,
    "AI Specializations": Brain,
    "Data Processing & Analytics": Database,
    "Databases and Data Analytics": Database,
    "LLM & GenAI Tools": Brain,
    "Cloud/MLOps/Other Tools": Cloud,
    "MLOps/Cloud Tools": Cloud
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white">
      {/* Navigation */}
      <nav className={`fixed top-0 w-full z-50 transition-all duration-300 ${
        scrollY > 50 ? 'bg-gray-900/95 backdrop-blur-sm border-b border-gray-800' : 'bg-transparent'
      }`}>
        <div className="max-w-7xl mx-auto px-6">
          <div className="flex justify-between items-center py-4">
            {/* Desktop Menu */}
            <div className="hidden md:flex space-x-8">
              {[
                { id: 'hero', label: 'Home' },
                { id: 'about', label: 'About' },
                { id: 'skills', label: 'Skills' },
                { id: 'experience', label: 'Experience' },
                { id: 'projects', label: 'Projects' },
                { id: 'publications', label: 'Publications' },
                { id: 'contact', label: 'Contact' }
              ].map((item) => (
                <button
                  key={item.id}
                  onClick={() => scrollToSection(item.id)}
                  className={`text-sm font-light hover:text-blue-400 transition-colors ${
                    activeSection === item.id ? 'text-blue-400' : 'text-gray-300'
                  }`}
                >
                  {item.label}
                </button>
              ))}
            </div>

            {/* Social Links */}
            <div className="hidden md:flex space-x-4">
              <a href={portfolio.personal.github} className="text-gray-400 hover:text-white transition-colors">
                <Github size={18} />
              </a>
              <a href={portfolio.personal.linkedin} className="text-gray-400 hover:text-white transition-colors">
                <Linkedin size={18} />
              </a>
              <a href={portfolio.personal.kaggle} className="text-gray-400 hover:text-white transition-colors">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor">
                  <path d="M18.825 23.859c-.022.092-.117.141-.281.141h-3.139c-.187 0-.351-.082-.492-.248l-5.178-6.589-1.448 1.374v5.111c0 .235-.117.352-.351.352H5.505c-.236 0-.354-.117-.354-.352V.353c0-.233.118-.353.354-.353h2.431c.234 0 .351.12.351.353v14.343l6.203-6.272c.165-.165.33-.246.495-.246h3.239c.144 0 .236.06.283.18.035.099.023.198-.036.297l-5.61 6.062 6.302 8.407c.059.094.071.181.036.297z"/>
                </svg>
              </a>
            </div>

            {/* Mobile Menu Button */}
            <button
              onClick={() => setIsMenuOpen(!isMenuOpen)}
              className="md:hidden text-gray-300"
            >
              {isMenuOpen ? <X size={24} /> : <Menu size={24} />}
            </button>
          </div>
        </div>

        {/* Mobile Menu */}
        {isMenuOpen && (
          <div className="md:hidden bg-gray-900/95 backdrop-blur-sm border-t border-gray-800">
            <div className="px-6 py-4 space-y-3">
              {[
                { id: 'hero', label: 'Home' },
                { id: 'about', label: 'About' },
                { id: 'skills', label: 'Skills' },
                { id: 'experience', label: 'Experience' },
                { id: 'projects', label: 'Projects' },
                { id: 'publications', label: 'Publications' },
                { id: 'contact', label: 'Contact' }
              ].map((item) => (
                <button
                  key={item.id}
                  onClick={() => scrollToSection(item.id)}
                  className="block text-left text-gray-300 hover:text-blue-400 transition-colors text-sm"
                >
                  {item.label}
                </button>
              ))}
            </div>
          </div>
        )}
      </nav>

      {/* Hero Section */}
      <section id="hero" className="min-h-screen flex items-center justify-center relative">
        <div className="text-center max-w-4xl mx-auto px-6">
          <div className="w-16 h-16 rounded-full bg-blue-600 mx-auto mb-8 flex items-center justify-center">
            <span className="text-white text-xl font-light">AD</span>
          </div>
          <h1 className="text-4xl md:text-6xl font-light mb-6 text-white tracking-wider">
            {portfolio.personal.name}
          </h1>
          <p className="text-lg text-gray-400 mb-12 max-w-2xl mx-auto font-light">
            {portfolio.personal.tagline}
          </p>
          <button 
            onClick={() => scrollToSection('projects')}
            className="bg-blue-600 hover:bg-blue-700 text-white px-8 py-3 text-sm font-light tracking-wide transition-colors"
          >
            View Work
          </button>
          <button 
            onClick={() => scrollToSection('contact')}
            className="border border-blue-600 hover:bg-blue-600 text-blue-400 hover:text-white px-8 py-3 text-sm font-light tracking-wide transition-colors"
          >
            Get In Touch
          </button>
        </div>
      </section>

      {/* About Section */}
      <section id="about" className="py-20 bg-gray-800">
        <div className="max-w-6xl mx-auto px-6">
          <h2 className="text-3xl font-light text-center mb-16 text-white">
            {portfolio.about.title}
          </h2>
          <div className="grid lg:grid-cols-3 gap-12">
            <div className="lg:col-span-2">
              <p className="text-gray-300 leading-relaxed mb-8 font-light">
                {portfolio.about.description}
              </p>
              <div>
                <h3 className="text-xl font-light mb-4 text-white">Education</h3>
                <div className="bg-gray-900 p-6">
                  <p className="font-light text-white mb-2">{portfolio.about.education.institution}</p>
                  <p className="text-gray-400 text-sm mb-1">{portfolio.about.education.degree}</p>
                  <p className="text-gray-500 text-sm">{portfolio.about.education.duration}</p>
                </div>
              </div>
            </div>
            <div>
              <h3 className="text-xl font-light mb-6 text-white">Key Achievements</h3>
              <div className="space-y-4">
                {achievements.map((achievement, index) => (
                  <div key={achievement.id || index} className="bg-gray-900 p-4">
                    <h4 className="text-blue-400 text-sm font-light mb-2">{achievement.title}</h4>
                    <p className="text-gray-400 text-xs leading-relaxed">{achievement.description}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Technical Skills */}
      <section id="skills" className="py-20">
        <div className="max-w-6xl mx-auto px-6">
          <h2 className="text-3xl font-light text-center mb-16 text-white">
            Technical Skills
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {skills.map((category, index) => {
              const IconComponent = skillIcons[category.title] || Code;
              return (
                <div key={category.id || index} className="bg-gray-800 p-6">
                  <div className="flex items-center mb-4">
                    <IconComponent size={20} className="text-blue-400 mr-3" />
                    <h3 className="text-lg font-light text-blue-400">{category.title}</h3>
                  </div>
                  <div className="flex flex-wrap gap-2">
                    {category.items.map((skill, skillIndex) => (
                      <span key={skillIndex} className="inline-block bg-gray-900 text-gray-300 px-3 py-1 text-xs font-light">
                        {skill}
                      </span>
                    ))}
                  </div>
                </div>
              );
            })}
          </div>
        </div>
      </section>

      {/* Experience */}
      <section id="experience" className="py-20 bg-gray-800">
        <div className="max-w-6xl mx-auto px-6">
          <h2 className="text-3xl font-light text-center mb-16 text-white">
            Experience
          </h2>
          <div className="space-y-8">
            {experiences.map((exp, index) => (
              <div key={exp.id || index} className="bg-gray-900 p-6">
                <div className="flex flex-col md:flex-row md:justify-between md:items-start mb-4">
                  <div className="flex-1">
                    <div className="flex items-center gap-3 mb-2">
                      <h3 className="text-xl font-light text-white">{exp.title}</h3>
                      {exp.current && (
                        <span className="bg-blue-600 text-white px-3 py-1 text-xs font-light">
                          Current
                        </span>
                      )}
                    </div>
                    <p className="text-blue-400 font-light mb-1">{exp.company}</p>
                    <p className="text-gray-500 text-sm">{exp.location}</p>
                  </div>
                  <div className="text-gray-500 text-sm mt-2 md:mt-0 md:text-right">
                    {exp.duration}
                  </div>
                </div>
                <div className="text-gray-300 font-light leading-relaxed">
                  {exp.description.split('\n').map((line, lineIndex) => (
                    <p key={lineIndex} className="mb-1 text-sm">{line}</p>
                  ))}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Projects */}
      <section id="projects" className="py-20">
        <div className="max-w-6xl mx-auto px-6">
          <h2 className="text-3xl font-light text-center mb-16 text-white">
            Projects
          </h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {projects.map((project, index) => (
              <div key={project.id || index} className="bg-gray-800 p-6">
                <div className="flex justify-between items-start mb-4">
                  <h3 className="text-lg font-light text-white">{project.title}</h3>
                  {project.featured && (
                    <span className="bg-blue-600 text-white px-2 py-1 text-xs font-light">Featured</span>
                  )}
                  {project.placeholder && (
                    <span className="bg-gray-600 text-white px-2 py-1 text-xs font-light">Placeholder</span>
                  )}
                </div>
                <div className="text-gray-300 font-light text-sm leading-relaxed mb-4">
                  {project.description.split('\n').map((line, lineIndex) => (
                    <p key={lineIndex} className="mb-1">{line}</p>
                  ))}
                </div>
                <div className="flex flex-wrap gap-1 mb-4">
                  {project.technologies.map((tech, techIndex) => (
                    <span key={techIndex} className="bg-gray-900 text-gray-400 px-2 py-1 text-xs font-light">
                      {tech}
                    </span>
                  ))}
                </div>
                <div className="flex space-x-4">
                  <a href={project.github} className="text-gray-400 hover:text-white transition-colors">
                    <Github size={16} />
                  </a>
                  <a href={project.demo} className="text-gray-400 hover:text-white transition-colors">
                    <ExternalLink size={16} />
                  </a>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Achievements Section
      <section id="achievements" className="py-20 bg-gray-800">
        <div className="max-w-6xl mx-auto px-6">
          <h2 className="text-3xl font-light text-center mb-16 text-white">
            Achievements
          </h2>
          <div className="grid md:grid-cols-3 gap-8">
            {achievements.map((achievement, index) => (
              <div key={achievement.id || index} className="bg-gray-900 p-6 text-center hover:bg-gray-800 transition-colors">
                <Award size={32} className="text-yellow-400 mx-auto mb-4" />
                <h3 className="text-lg font-light mb-3 text-yellow-400">{achievement.title}</h3>
                <p className="text-gray-300 text-sm font-light">{achievement.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section> */}

      {/* Publications */}
      <section id="publications" className="py-20">
        <div className="max-w-6xl mx-auto px-6">
          <h2 className="text-3xl font-light text-center mb-16 text-white">
            Publications
          </h2>
          <div className="space-y-6">
            {publications.map((publication, index) => (
              <div key={publication.id || index} className="bg-gray-800 p-6">
                <h3 className="text-lg font-light text-blue-400 mb-3">{publication.title}</h3>
                <p className="text-gray-300 text-sm font-light mb-2">{publication.authors}</p>
                <p className="text-gray-400 text-sm font-light mb-2">{publication.publication}</p>
                <div className="flex items-center space-x-4 text-xs text-gray-500">
                  <span>Year: {publication.year}</span>
                  {publication.doi && <span>DOI: {publication.doi}</span>}
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Contact */}
      <section id="contact" className="py-20 bg-gray-800">
        <div className="max-w-4xl mx-auto px-6 text-center">
          <h2 className="text-3xl font-light mb-8 text-white">
            Get In Touch
          </h2>
          <p className="text-gray-400 mb-12 font-light leading-relaxed">
            Interested in collaborating on some project or just want to have a quick chat? I'd love to hear from you.
          </p>
          <div className="flex justify-center space-x-6">
            <a 
              href={`mailto:${portfolio.personal.email}`}
              className="flex items-center space-x-2 bg-gray-900 hover:bg-gray-700 px-6 py-3 transition-colors"
            >
              <Mail size={16} />
              <span className="text-sm font-light">Email</span>
            </a>
            <a 
              href={portfolio.personal.github}
              className="flex items-center space-x-2 bg-gray-900 hover:bg-gray-700 px-6 py-3 transition-colors"
            >
              <Github size={16} />
              <span className="text-sm font-light">GitHub</span>
            </a>
            <a 
              href={portfolio.personal.linkedin}
              className="flex items-center space-x-2 bg-gray-900 hover:bg-gray-700 px-6 py-3 transition-colors"
            >
              <Linkedin size={16} />
              <span className="text-sm font-light">LinkedIn</span>
            </a>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-8 bg-gray-900 text-center border-t border-gray-800">
        <p className="text-gray-500 text-sm font-light">
          © 2025 {portfolio.personal.name.split(' ')[0]} {portfolio.personal.name.split(' ')[1] || ''}. All rights reserved.
        </p>
      </footer>
    </div>
  );
};

export default Portfolio;