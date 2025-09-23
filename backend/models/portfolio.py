from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, timezone
import uuid

class PersonalInfo(BaseModel):
    name: str
    tagline: str
    email: str
    github: str
    linkedin: str
    kaggle: str

class Education(BaseModel):
    institution: str
    degree: str
    duration: str

class AboutSection(BaseModel):
    title: str = "About Me"
    description: str
    education: Education

class Portfolio(BaseModel):
    id: str = Field(default_factory = lambda: str(uuid.uuid4()))
    userId: str = "default"
    personal: PersonalInfo
    about: AboutSection
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class SkillCategory(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    portfolioId: str = "default"
    title: str
    items: List[str]
    order: int = 0
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Experience(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    portfolioId: str = "default"
    title: str
    company: str
    location: str
    duration: str
    description: str
    current: bool = False
    order: int = 0
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Project(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    portfolioId: str = "default"  
    title: str
    description: str
    technologies: List[str]
    github: str = "#"
    demo: str = "#"
    featured: bool = False
    placeholder: bool = False
    order: int = 0
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Achievement(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    portfolioId: str = "default"
    title: str
    description: str
    order: int = 0
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

class Publication(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    portfolioId: str = "default"
    title: str
    authors: str
    publication: str
    year: str
    doi: Optional[str] = None
    order: int = 0
    createdAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updatedAt: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

# Request models for API endpoints
class PersonalInfoUpdate(BaseModel):
    name: Optional[str] = None
    tagline: Optional[str] = None
    email: Optional[str] = None
    github: Optional[str] = None
    linkedin: Optional[str] = None
    kaggle: Optional[str] = None

class AboutSectionUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    education: Optional[Education] = None

class SkillCategoryCreate(BaseModel):
    title: str
    items: List[str]
    order: int = 0

class SkillCategoryUpdate(BaseModel):
    title: Optional[str] = None
    items: Optional[List[str]] = None
    order: Optional[int] = None

class ExperienceCreate(BaseModel):
    title: str
    company: str
    location: str
    duration: str
    description: str
    current: bool = False
    order: int = 0

class ExperienceUpdate(BaseModel):
    title: Optional[str] = None
    company: Optional[str] = None
    location: Optional[str] = None
    duration: Optional[str] = None
    description: Optional[str] = None
    current: Optional[bool] = None
    order: Optional[int] = None

class ProjectCreate(BaseModel):
    title: str
    description: str
    technologies: List[str]
    github: str = "#"
    demo: str = "#"
    featured: bool = False
    placeholder: bool = False
    order: int = 0

class ProjectUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    technologies: Optional[List[str]] = None
    github: Optional[str] = None
    demo: Optional[str] = None
    featured: Optional[bool] = None
    placeholder: Optional[bool] = None
    order: Optional[int] = None

class AchievementCreate(BaseModel):
    title: str
    description: str
    order: int = 0

class AchievementUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    order: Optional[int] = None

class PublicationCreate(BaseModel):
    title: str
    authors: str
    publication: str
    year: str
    doi: Optional[str] = None
    order: int = 0

class PublicationUpdate(BaseModel):
    title: Optional[str] = None
    authors: Optional[str] = None
    publication: Optional[str] = None
    year: Optional[str] = None
    doi: Optional[str] = None
    order: Optional[int] = None

# Response models
class PortfolioResponse(BaseModel):
    portfolio: Portfolio
    skills: List[SkillCategory]
    experiences: List[Experience]
    projects: List[Project]
    achievements: List[Achievement]
    publications: List[Publication]