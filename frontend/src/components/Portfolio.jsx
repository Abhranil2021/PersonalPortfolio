import React, { useState, useEffect } from 'react';
import { mockData } from '../data/mock';
import { Button } from './ui/button';
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from './ui/card';
import { Badge } from './ui/badge';
import { Separator } from './ui/separator';
import { 
  Github, 
  Linkedin, 
  Mail, 
  ExternalLink, 
  Code2, 
  Brain, 
  Database, 
  Award,
  Calendar,
  MapPin,
  BookOpen
} from 'lucide-react';

const Portfolio = () => {
  const [activeSection, setActiveSection] = useState('hero');

  useEffect(() => {
    const handleScroll = () => {
      const sections = ['hero', 'about', 'skills', 'experience', 'projects', 'contact'];
      const currentSection = sections.find(section => {
        const element = document.getElementById(section);
        if (element) {
          const rect = element.getBoundingClientRect();
          return rect.top <= 100 && rect.bottom >= 100;
        }
        return false;
      });
      if (currentSection) {
        setActiveSection(currentSection);
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  const scrollToSection = (sectionId) => {
    const element = document.getElementById(sectionId);
    if (element) {
      element.scrollIntoView({ behavior: 'smooth' });
    }
  };

  return (
    <div className="min-h-screen bg-slate-950 text-white">
      {/* Navigation */}
      <nav className="fixed top-0 left-0 right-0 z-50 bg-slate-950/80 backdrop-blur-sm border-b border-slate-800">
        <div className="max-w-6xl mx-auto px-6 py-4">
          <div className="flex justify-between items-center">
            <div className="text-xl font-light tracking-tight text-blue-400">AD</div>
            <div className="hidden md:flex space-x-8">
              {['About', 'Skills', 'Experience', 'Projects', 'Contact'].map((item) => (
                <button
                  key={item}
                  onClick={() => scrollToSection(item.toLowerCase())}
                  className={`text-sm font-normal transition-all duration-300 hover:-translate-y-0.5 ${
                    activeSection === item.toLowerCase() ? 'text-white' : 'text-slate-400'
                  }`}
                >
                  {item}
                </button>
              ))}
            </div>
            <div className="flex space-x-4">
              <a href={mockData.personal.github} target="_blank" rel="noopener noreferrer">
                <Button variant="ghost" size="sm" className="hover:scale-105 transition-transform text-slate-300 hover:text-white">
                  <Github className="h-4 w-4" />
                </Button>
              </a>
              <a href={mockData.personal.linkedin} target="_blank" rel="noopener noreferrer">
                <Button variant="ghost" size="sm" className="hover:scale-105 transition-transform text-slate-300 hover:text-white">
                  <Linkedin className="h-4 w-4" />
                </Button>
              </a>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section id="hero" className="min-h-screen flex items-center justify-center px-6 py-24">
        <div className="max-w-4xl mx-auto text-center">
          <div className="mb-8">
            <div className="w-16 h-16 mx-auto mb-8 border border-slate-700 rounded-full flex items-center justify-center bg-slate-900">
              <Brain className="h-8 w-8 text-blue-400" />
            </div>
          </div>
          <h1 className="text-6xl md:text-8xl lg:text-9xl font-light tracking-tight mb-6 leading-none">
            {mockData.personal.name}
          </h1>
          <p className="text-lg md:text-xl text-slate-300 font-light tracking-wide mb-12 max-w-2xl mx-auto">
            {mockData.personal.tagline}
          </p>
          <Button 
            onClick={() => scrollToSection('contact')}
            className="bg-blue-600 text-white hover:bg-blue-700 transition-all duration-300 hover:scale-105"
          >
            Get In Touch
          </Button>
        </div>
      </section>

      {/* About Section */}
      <section id="about" className="py-24 px-6 bg-slate-900">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-light tracking-tight mb-16 text-center">About Me</h2>
          <div className="grid md:grid-cols-2 gap-12">
            <div>
              <p className="text-lg text-slate-300 leading-relaxed mb-8">
                {mockData.about.description}
              </p>
              <div className="space-y-4">
                <h3 className="text-xl font-normal">Education</h3>
                <div className="bg-slate-800 p-6 rounded-lg border border-slate-700">
                  <h4 className="font-medium">{mockData.about.education.institution}</h4>
                  <p className="text-slate-400">{mockData.about.education.degree}</p>
                  <p className="text-sm text-slate-500 flex items-center mt-2">
                    <Calendar className="h-4 w-4 mr-2" />
                    {mockData.about.education.duration}
                  </p>
                </div>
              </div>
            </div>
            <div>
              <h3 className="text-xl font-normal mb-6">Key Achievements</h3>
              <div className="space-y-4">
                {mockData.achievements.map((achievement, index) => (
                  <div key={index} className="bg-slate-800 p-6 rounded-lg border border-slate-700">
                    <div className="flex items-center mb-2">
                      <Award className="h-5 w-5 mr-2 text-blue-400" />
                      <h4 className="font-medium">{achievement.title}</h4>
                    </div>
                    <p className="text-slate-400 text-sm">{achievement.description}</p>
                  </div>
                ))}
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Skills Section */}
      <section id="skills" className="py-24 px-6">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-light tracking-tight mb-16 text-center">Technical Skills</h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {mockData.skills.categories.map((category, index) => (
              <Card key={index} className="border-slate-700 bg-slate-900 hover:shadow-lg hover:shadow-blue-500/10 transition-all duration-300 hover:-translate-y-1">
                <CardHeader>
                  <CardTitle className="text-lg font-normal flex items-center text-white">
                    {category.title === 'Programming' && <Code2 className="h-5 w-5 mr-2 text-blue-400" />}
                    {category.title === 'ML Frameworks' && <Brain className="h-5 w-5 mr-2 text-blue-400" />}
                    {category.title === 'AI Specializations' && <Brain className="h-5 w-5 mr-2 text-blue-400" />}
                    {category.title === 'Data & Analytics' && <Database className="h-5 w-5 mr-2 text-blue-400" />}
                    {category.title === 'LLM & GenAI Tools' && <Brain className="h-5 w-5 mr-2 text-blue-400" />}
                    {category.title}
                  </CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="flex flex-wrap gap-2">
                    {category.items.map((skill, skillIndex) => (
                      <Badge key={skillIndex} variant="secondary" className="text-xs bg-slate-800 text-slate-300 border-slate-600">
                        {skill}
                      </Badge>
                    ))}
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Experience Section */}
      <section id="experience" className="py-24 px-6 bg-gray-50">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-light tracking-tight mb-16 text-center">Experience</h2>
          <div className="space-y-8">
            {mockData.experience.map((job, index) => (
              <Card key={job.id} className={`border-gray-100 hover:shadow-lg transition-all duration-300 ${
                job.current ? 'ring-2 ring-gray-200' : ''
              }`}>
                <CardHeader>
                  <div className="flex justify-between items-start">
                    <div>
                      <CardTitle className="text-xl font-normal">{job.title}</CardTitle>
                      <CardDescription className="text-lg mt-1">{job.company}</CardDescription>
                      <div className="flex items-center text-sm text-gray-500 mt-2">
                        <MapPin className="h-4 w-4 mr-1" />
                        {job.location}
                        <Separator orientation="vertical" className="mx-3 h-4" />
                        <Calendar className="h-4 w-4 mr-1" />
                        {job.duration}
                      </div>
                    </div>
                    {job.current && (
                      <Badge variant="secondary" className="bg-black text-white">
                        Current
                      </Badge>
                    )}
                  </div>
                </CardHeader>
                <CardContent>
                  <p className="text-gray-700 leading-relaxed">{job.description}</p>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Projects Section */}
      <section id="projects" className="py-24 px-6">
        <div className="max-w-6xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-light tracking-tight mb-16 text-center">Projects</h2>
          <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">
            {mockData.projects.map((project) => (
              <Card key={project.id} className={`border-gray-100 hover:shadow-lg transition-all duration-300 hover:-translate-y-2 ${
                project.placeholder ? 'opacity-70 border-dashed' : ''
              }`}>
                <CardHeader>
                  <div className="flex justify-between items-start">
                    <CardTitle className="text-lg font-normal leading-tight">
                      {project.title}
                      {project.placeholder && <span className="text-xs text-gray-500 ml-2">(Placeholder)</span>}
                    </CardTitle>
                    {project.featured && (
                      <Badge variant="secondary" className="text-xs">
                        Featured
                      </Badge>
                    )}
                  </div>
                </CardHeader>
                <CardContent>
                  <p className="text-gray-600 text-sm mb-4 leading-relaxed">{project.description}</p>
                  <div className="flex flex-wrap gap-1 mb-4">
                    {project.technologies.map((tech, techIndex) => (
                      <Badge key={techIndex} variant="outline" className="text-xs">
                        {tech}
                      </Badge>
                    ))}
                  </div>
                  <div className="flex space-x-2">
                    <Button variant="ghost" size="sm" className="hover:scale-105 transition-transform">
                      <Github className="h-4 w-4 mr-1" />
                      Code
                    </Button>
                    <Button variant="ghost" size="sm" className="hover:scale-105 transition-transform">
                      <ExternalLink className="h-4 w-4 mr-1" />
                      Demo
                    </Button>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Publications Section */}
      <section className="py-24 px-6 bg-gray-50">
        <div className="max-w-4xl mx-auto">
          <h2 className="text-4xl md:text-5xl font-light tracking-tight mb-16 text-center">Publications</h2>
          <div className="space-y-6">
            {mockData.publications.map((pub, index) => (
              <Card key={index} className="border-gray-100">
                <CardContent className="pt-6">
                  <div className="flex items-start mb-2">
                    <BookOpen className="h-5 w-5 mr-2 text-gray-600 mt-0.5" />
                    <div>
                      <h3 className="font-medium text-lg mb-1">{pub.title}</h3>
                      <p className="text-gray-600 text-sm mb-2">{pub.authors}</p>
                      <p className="text-gray-500 text-sm">{pub.publication} ({pub.year})</p>
                      {pub.doi && <p className="text-xs text-gray-400 mt-1">DOI: {pub.doi}</p>}
                    </div>
                  </div>
                </CardContent>
              </Card>
            ))}
          </div>
        </div>
      </section>

      {/* Contact Section */}
      <section id="contact" className="py-24 px-6">
        <div className="max-w-2xl mx-auto text-center">
          <h2 className="text-4xl md:text-5xl font-light tracking-tight mb-16">Get In Touch</h2>
          <p className="text-lg text-gray-600 mb-12 leading-relaxed">
            Interested in collaboration or have a project in mind? I'd love to hear from you.
          </p>
          <div className="flex justify-center space-x-6 mb-12">
            <a href={`mailto:${mockData.personal.email}`}>
              <Button variant="outline" className="hover:scale-105 transition-transform">
                <Mail className="h-4 w-4 mr-2" />
                Email
              </Button>
            </a>
            <a href={mockData.personal.github} target="_blank" rel="noopener noreferrer">
              <Button variant="outline" className="hover:scale-105 transition-transform">
                <Github className="h-4 w-4 mr-2" />
                GitHub
              </Button>
            </a>
            <a href={mockData.personal.linkedin} target="_blank" rel="noopener noreferrer">
              <Button variant="outline" className="hover:scale-105 transition-transform">
                <Linkedin className="h-4 w-4 mr-2" />
                LinkedIn
              </Button>
            </a>
            <a href={mockData.personal.kaggle} target="_blank" rel="noopener noreferrer">
              <Button variant="outline" className="hover:scale-105 transition-transform">
                <ExternalLink className="h-4 w-4 mr-2" />
                Kaggle
              </Button>
            </a>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 px-6 border-t border-gray-100 bg-gray-50">
        <div className="max-w-4xl mx-auto text-center">
          <p className="text-gray-500 text-sm">
            © 2025 Abhranil Das. Built with React and modern web technologies.
          </p>
        </div>
      </footer>
    </div>
  );
};

export default Portfolio;