from typing import List, Optional, Dict, Any
from models.portfolio import *
from datetime import datetime, timezone

class PortfolioService:
    def __init__(self, db):
        self.db = db
        self.portfolios = db.portfolios
        self.skills = db.skills
        self.experiences = db.experiences
        self.projects = db.projects
        self.achievements = db.achievements
        self.publications = db.publications

    # Portfolio methods
    async def get_portfolio(self, portfolio_id: str = "default") -> Optional[Dict]:
        """Get complete portfolio data"""
        portfolio_doc = await self.portfolios.find_one({"userId": portfolio_id}, {"_id": 0})
        
        if not portfolio_doc:
            return None
            
        # Get all related data (exclude _id field)
        skills = await self.skills.find({"portfolioId": portfolio_id}, {"_id": 0}).sort("order", 1).to_list(None)
        experiences = await self.experiences.find({"portfolioId": portfolio_id}, {"_id": 0}).sort("order", 1).to_list(None)
        projects = await self.projects.find({"portfolioId": portfolio_id}, {"_id": 0}).sort("order", 1).to_list(None)
        achievements = await self.achievements.find({"portfolioId": portfolio_id}, {"_id": 0}).sort("order", 1).to_list(None)
        publications = await self.publications.find({"portfolioId": portfolio_id}, {"_id": 0}).sort("order", 1).to_list(None)

        return {
            "portfolio": portfolio_doc,
            "skills": skills,
            "experiences": experiences,
            "projects": projects,
            "achievements": achievements,
            "publications": publications
        }

    async def create_or_update_portfolio(self, portfolio_data: Portfolio) -> Portfolio:
        """Create or update portfolio"""
        portfolio_dict = portfolio_data.model_dump()
        portfolio_dict["updatedAt"] = datetime.now(timezone.utc)
        
        await self.portfolios.replace_one(
            {"userId": portfolio_data.userId},
            portfolio_dict,
            upsert = True
        )
        return portfolio_data

    async def update_personal_info(self, updates: PersonalInfoUpdate, portfolio_id: str = "default") -> bool:
        """Update personal information"""
        update_dict = {k: v for k, v in updates.model_dump().items() if v is not None}
        if not update_dict:
            return False
            
        result = await self.portfolios.update_one(
            {"userId": portfolio_id},
            {"$set": {f"personal.{k}": v for k, v in update_dict.items()}}
        )
        return result.modified_count > 0

    async def update_about_section(self, updates: AboutSectionUpdate, portfolio_id: str = "default") -> bool:
        """Update about section"""
        update_dict = {k: v for k, v in updates.model_dump().items() if v is not None}
        if not update_dict:
            return False
            
        result = await self.portfolios.update_one(
            {"userId": portfolio_id},
            {"$set": {f"about.{k}": v for k, v in update_dict.items()}}
        )
        return result.modified_count > 0

    # Skills methods
    async def get_skills(self, portfolio_id: str = "default") -> List[Dict]:
        """Get all skill categories"""
        return await self.skills.find({"portfolioId": portfolio_id}, {"_id": 0}).sort("order", 1).to_list(None)

    async def create_skill(self, skill_data: SkillCategoryCreate, portfolio_id: str = "default") -> SkillCategory:
        """Create new skill category"""
        skill = SkillCategory(**skill_data.model_dump(), portfolioId = portfolio_id)
        await self.skills.insert_one(skill.model_dump())
        return skill

    async def update_skill(self, skill_id: str, updates: SkillCategoryUpdate) -> bool:
        """Update skill category"""
        update_dict = {k: v for k, v in updates.model_dump().items() if v is not None}
        if not update_dict:
            return False
            
        update_dict["updatedAt"] = datetime.now(timezone.utc)
        result = await self.skills.update_one({"id": skill_id}, {"$set": update_dict})
        return result.modified_count > 0

    async def delete_skill(self, skill_id: str) -> bool:
        """Delete skill category"""
        result = await self.skills.delete_one({"id": skill_id})
        return result.deleted_count > 0

    # Experience methods
    async def get_experiences(self, portfolio_id: str = "default") -> List[Dict]:
        """Get all experiences"""
        return await self.experiences.find({"portfolioId": portfolio_id}, {"_id": 0}).sort("order", 1).to_list(None)

    async def create_experience(self, exp_data: ExperienceCreate, portfolio_id: str = "default") -> Experience:
        """Create new experience"""
        experience = Experience(**exp_data.model_dump(), portfolioId = portfolio_id)
        await self.experiences.insert_one(experience.model_dump())
        return experience

    async def update_experience(self, exp_id: str, updates: ExperienceUpdate) -> bool:
        """Update experience"""
        update_dict = {k: v for k, v in updates.model_dump().items() if v is not None}
        if not update_dict:
            return False
            
        update_dict["updatedAt"] = datetime.now(timezone.utc)
        result = await self.experiences.update_one({"id": exp_id}, {"$set": update_dict})
        return result.modified_count > 0

    async def delete_experience(self, exp_id: str) -> bool:
        """Delete experience"""
        result = await self.experiences.delete_one({"id": exp_id})
        return result.deleted_count > 0

    # Projects methods
    async def get_projects(self, portfolio_id: str = "default") -> List[Dict]:
        """Get all projects"""
        return await self.projects.find({"portfolioId": portfolio_id}, {"_id": 0}).sort("order", 1).to_list(None)

    async def create_project(self, project_data: ProjectCreate, portfolio_id: str = "default") -> Project:
        """Create new project"""
        project = Project(**project_data.model_dump(), portfolioId = portfolio_id)
        await self.projects.insert_one(project.model_dump())
        return project

    async def update_project(self, project_id: str, updates: ProjectUpdate) -> bool:
        """Update project"""
        update_dict = {k: v for k, v in updates.model_dump().items() if v is not None}
        if not update_dict:
            return False
            
        update_dict["updatedAt"] = datetime.now(timezone.utc)
        result = await self.projects.update_one({"id": project_id}, {"$set": update_dict})
        return result.modified_count > 0

    async def delete_project(self, project_id: str) -> bool:
        """Delete project"""
        result = await self.projects.delete_one({"id": project_id})
        return result.deleted_count > 0

    # Achievements methods  
    async def get_achievements(self, portfolio_id: str = "default") -> List[Dict]:
        """Get all achievements"""
        return await self.achievements.find({"portfolioId": portfolio_id}, {"_id": 0}).sort("order", 1).to_list(None)

    async def create_achievement(self, achievement_data: AchievementCreate, portfolio_id: str = "default") -> Achievement:
        """Create new achievement"""
        achievement = Achievement(**achievement_data.model_dump(), portfolioId = portfolio_id)
        await self.achievements.insert_one(achievement.model_dump())
        return achievement

    async def update_achievement(self, achievement_id: str, updates: AchievementUpdate) -> bool:
        """Update achievement"""
        update_dict = {k: v for k, v in updates.model_dump().items() if v is not None}
        if not update_dict:
            return False
            
        update_dict["updatedAt"] = datetime.now(timezone.utc)
        result = await self.achievements.update_one({"id": achievement_id}, {"$set": update_dict})
        return result.modified_count > 0

    async def delete_achievement(self, achievement_id: str) -> bool:
        """Delete achievement"""
        result = await self.achievements.delete_one({"id": achievement_id})
        return result.deleted_count > 0

    # Publications methods
    async def get_publications(self, portfolio_id: str = "default") -> List[Dict]:
        """Get all publications"""
        return await self.publications.find({"portfolioId": portfolio_id}, {"_id": 0}).sort("order", 1).to_list(None)

    async def create_publication(self, pub_data: PublicationCreate, portfolio_id: str = "default") -> Publication:
        """Create new publication"""
        publication = Publication(**pub_data.model_dump(), portfolioId = portfolio_id)
        await self.publications.insert_one(publication.model_dump())
        return publication

    async def update_publication(self, pub_id: str, updates: PublicationUpdate) -> bool:
        """Update publication"""
        update_dict = {k: v for k, v in updates.model_dump().items() if v is not None}
        if not update_dict:
            return False
            
        update_dict["updatedAt"] = datetime.now(timezone.utc)
        result = await self.publications.update_one({"id": pub_id}, {"$set": update_dict})
        return result.modified_count > 0

    async def delete_publication(self, pub_id: str) -> bool:
        """Delete publication"""
        result = await self.publications.delete_one({"id": pub_id})
        return result.deleted_count > 0

    # Migration and export methods
    async def migrate_mock_data(self, mock_data: Dict[str, Any]) -> bool:
        """Migrate data from mock.js format to database"""
        try:
            # Create portfolio
            portfolio = Portfolio(
                personal = PersonalInfo(**mock_data["personal"]),
                about = AboutSection(**mock_data["about"])
            )
            await self.create_or_update_portfolio(portfolio)

            # Create skills
            for i, skill_cat in enumerate(mock_data["skills"]["categories"]):
                skill = SkillCategory(
                    title = skill_cat["title"],
                    items = skill_cat["items"],
                    order = i
                )
                await self.skills.replace_one(
                    {"portfolioId": "default", "title": skill.title},
                    skill.model_dump(),
                    upsert = True
                )

            # Create experiences
            for i, exp in enumerate(mock_data["experience"]):
                experience = Experience(
                    title = exp["title"],
                    company = exp["company"],
                    location = exp["location"],
                    duration = exp["duration"],
                    description = exp["description"],
                    current = exp.get("current", False),
                    order = i
                )
                await self.experiences.replace_one(
                    {"portfolioId": "default", "title": experience.title, "company": experience.company},
                    experience.model_dump(),
                    upsert = True
                )

            # Create projects
            for i, proj in enumerate(mock_data["projects"]):
                project = Project(
                    title = proj["title"],
                    description = proj["description"],
                    technologies = proj["technologies"],
                    github = proj.get("github", "#"),
                    demo = proj.get("demo", "#"),
                    featured = proj.get("featured", False),
                    placeholder = proj.get("placeholder", False),
                    order = i
                )
                await self.projects.replace_one(
                    {"portfolioId": "default", "title": project.title},
                    project.model_dump(),
                    upsert = True
                )

            # Create achievements
            for i, ach in enumerate(mock_data["achievements"]):
                achievement = Achievement(
                    title = ach["title"],
                    description = ach["description"],
                    order = i
                )
                await self.achievements.replace_one(
                    {"portfolioId": "default", "title": achievement.title},
                    achievement.model_dump(),
                    upsert = True
                )

            # Create publications
            for i, pub in enumerate(mock_data["publications"]):
                publication = Publication(
                    title = pub["title"],
                    authors = pub["authors"],
                    publication = pub["publication"],
                    year = pub["year"],
                    doi = pub.get("doi"),
                    order = i
                )
                await self.publications.replace_one(
                    {"portfolioId": "default", "title": publication.title},
                    publication.model_dump(),
                    upsert = True
                )

            return True
        except Exception as e:
            print(f"Migration error: {e}")
            return False

    async def export_data(self, portfolio_id: str = "default") -> Optional[Dict]:
        """Export all portfolio data"""
        return await self.get_portfolio(portfolio_id)