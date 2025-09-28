from typing import List, Optional, Dict, Any
from models.portfolio import *
from datetime import datetime, timezone
import logging

logger = logging.getLogger(__name__)

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
    async def get_portfolio(self, portfolio_id: str = "default") -> Optional[PortfolioResponse]:
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
        
        return PortfolioResponse(
            portfolio = Portfolio.model_validate(portfolio_doc),    
            skills = [SkillCategory.model_validate(doc) for doc in skills],
            experiences = [Experience.model_validate(doc) for doc in experiences],
            projects = [Project.model_validate(doc) for doc in projects],   
            achievements = [Achievement.model_validate(doc) for doc in achievements],
            publications = [Publication.model_validate(doc) for doc in publications]
        )

    async def create_or_update_portfolio(self, portfolio_data: Portfolio) -> Portfolio:
        """Create or update portfolio"""
        now = datetime.now(timezone.utc)
        portfolio_dict = portfolio_data.model_dump(exclude = {"createdAt", "updatedAt"})
        portfolio_dict["updatedAt"] = now
        
        await self.portfolios.replace_one(
            {"userId": portfolio_data.userId},
            {
                "$set": {**portfolio_dict, "updatedAt": now},
                "$setOnInsert": {"createdAt": now}
            },
            upsert = True
        )
        return Portfolio(**portfolio_dict, createdAt = portfolio_data.createdAt or now, updatedAt = now)

    async def update_personal_info(self, updates: PersonalInfoUpdate, portfolio_id: str = "default") -> bool:
        """Update personal information"""
        update_dict = updates.model_dump(exclude_unset = True)
        if not update_dict:
            return False
        
        update_dict.pop("updatedAt", None)  # Prevent manual update of updatedAt
        
        result = await self.portfolios.update_one(
            {"userId": portfolio_id},
            {
                "$set": {
                    **{f"personal.{k}": v for k, v in update_dict.items()}, 
                    "updatedAt": datetime.now(timezone.utc)
                }
            }
        )
        return result.matched_count > 0

    async def update_about_section(self, updates: AboutSectionUpdate, portfolio_id: str = "default") -> bool:
        """Update about section"""
        update_dict = updates.model_dump(exclude_unset = True)
        if not update_dict:
            return False
            
        update_dict.pop("updatedAt", None) # Prevent manual update of updatedAt
            
        result = await self.portfolios.update_one(
            {"userId": portfolio_id},
            {
                "$set": {
                    **{f"about.{k}": v for k, v in update_dict.items()},
                    "updatedAt": datetime.now(timezone.utc)
                }
            }
        )
        return result.matched_count > 0

    # Skills methods
    async def get_skills(self, portfolio_id: str = "default") -> List[SkillCategory]:
        """Get all skill categories"""
        docs = await self.skills.find({"portfolioId": portfolio_id}, {"_id": 0}).sort("order", 1).to_list(None)
        return [SkillCategory.model_validate(doc) for doc in docs]

    async def create_skill(self, skill_data: SkillCategoryCreate, portfolio_id: str = "default") -> SkillCategory:
        """Create new skill category"""
        now = datetime.now(timezone.utc)
        skill = SkillCategory(**skill_data.model_dump(), portfolioId = portfolio_id, createdAt = now, updatedAt = now)
        await self.skills.insert_one(skill.model_dump())
        return skill

    async def update_skill(self, skill_id: str, updates: SkillCategoryUpdate) -> bool:
        """Update skill category"""
        update_dict = updates.model_dump(exclude_unset = True)
        if not update_dict:
            return False
            
        update_dict["updatedAt"] = datetime.now(timezone.utc)
        result = await self.skills.update_one({"id": skill_id}, {"$set": update_dict})
        return result.matched_count > 0

    async def delete_skill(self, skill_id: str) -> bool:
        """Delete skill category"""
        result = await self.skills.delete_one({"id": skill_id})
        return result.deleted_count > 0

    # Experience methods
    async def get_experiences(self, portfolio_id: str = "default") -> List[Experience]:
        """Get all experiences"""
        docs = await self.experiences.find({"portfolioId": portfolio_id}, {"_id": 0}).sort("order", 1).to_list(None)
        return [Experience.model_validate(doc) for doc in docs]

    async def create_experience(self, exp_data: ExperienceCreate, portfolio_id: str = "default") -> Experience:
        """Create new experience"""
        now = datetime.now(timezone.utc)
        experience = Experience(**exp_data.model_dump(), portfolioId = portfolio_id, createdAt = now, updatedAt = now)
        await self.experiences.insert_one(experience.model_dump())
        return experience

    async def update_experience(self, exp_id: str, updates: ExperienceUpdate) -> bool:
        """Update experience"""
        update_dict = updates.model_dump(exclude_unset = True)
        if not update_dict:
            return False
            
        update_dict["updatedAt"] = datetime.now(timezone.utc)
        result = await self.experiences.update_one({"id": exp_id}, {"$set": update_dict})
        return result.matched_count > 0

    async def delete_experience(self, exp_id: str) -> bool:
        """Delete experience"""
        result = await self.experiences.delete_one({"id": exp_id})
        return result.deleted_count > 0

    # Projects methods
    async def get_projects(self, portfolio_id: str = "default") -> List[Project]:
        """Get all projects"""
        docs = await self.projects.find({"portfolioId": portfolio_id}, {"_id": 0}).sort("order", 1).to_list(None)
        return [Project.model_validate(doc) for doc in docs]

    async def create_project(self, project_data: ProjectCreate, portfolio_id: str = "default") -> Project:
        """Create new project"""
        now = datetime.now(timezone.utc)
        project = Project(**project_data.model_dump(), portfolioId = portfolio_id, createdAt = now, updatedAt = now)
        await self.projects.insert_one(project.model_dump())
        return project

    async def update_project(self, project_id: str, updates: ProjectUpdate) -> bool:
        """Update project"""
        update_dict = updates.model_dump(exclude_unset = True)
        if not update_dict:
            return False
            
        update_dict["updatedAt"] = datetime.now(timezone.utc)
        result = await self.projects.update_one({"id": project_id}, {"$set": update_dict})
        return result.matched_count > 0

    async def delete_project(self, project_id: str) -> bool:
        """Delete project"""
        result = await self.projects.delete_one({"id": project_id})
        return result.deleted_count > 0

    # Achievements methods  
    async def get_achievements(self, portfolio_id: str = "default") -> List[Achievement]:
        """Get all achievements"""
        docs = await self.achievements.find({"portfolioId": portfolio_id}, {"_id": 0}).sort("order", 1).to_list(None)
        return [Achievement.model_validate(doc) for doc in docs]

    async def create_achievement(self, achievement_data: AchievementCreate, portfolio_id: str = "default") -> Achievement:
        """Create new achievement"""
        now = datetime.now(timezone.utc)
        achievement = Achievement(**achievement_data.model_dump(), portfolioId = portfolio_id, createdAt = now, updatedAt = now)
        await self.achievements.insert_one(achievement.model_dump())
        return achievement

    async def update_achievement(self, achievement_id: str, updates: AchievementUpdate) -> bool:
        """Update achievement"""
        update_dict = updates.model_dump(exclude_unset = True)
        if not update_dict:
            return False
            
        update_dict["updatedAt"] = datetime.now(timezone.utc)
        result = await self.achievements.update_one({"id": achievement_id}, {"$set": update_dict})
        return result.matched_count > 0

    async def delete_achievement(self, achievement_id: str) -> bool:
        """Delete achievement"""
        result = await self.achievements.delete_one({"id": achievement_id})
        return result.deleted_count > 0

    # Publications methods
    async def get_publications(self, portfolio_id: str = "default") -> List[Publication]:
        """Get all publications"""
        docs = await self.publications.find({"portfolioId": portfolio_id}, {"_id": 0}).sort("order", 1).to_list(None)
        return [Publication.model_validate(doc) for doc in docs]

    async def create_publication(self, pub_data: PublicationCreate, portfolio_id: str = "default") -> Publication:
        """Create new publication"""
        now = datetime.now(timezone.utc)
        publication = Publication(**pub_data.model_dump(), portfolioId = portfolio_id, createdAt = now, updatedAt = now)
        await self.publications.insert_one(publication.model_dump())
        return publication

    async def update_publication(self, pub_id: str, updates: PublicationUpdate) -> bool:
        """Update publication"""
        update_dict = updates.model_dump(exclude_unset = True)
        if not update_dict:
            return False
            
        update_dict["updatedAt"] = datetime.now(timezone.utc)
        result = await self.publications.update_one({"id": pub_id}, {"$set": update_dict})
        return result.matched_count > 0

    async def delete_publication(self, pub_id: str) -> bool:
        """Delete publication"""
        result = await self.publications.delete_one({"id": pub_id})
        return result.deleted_count > 0

    # Migration and export methods
    async def migrate_mock_data(self, mock_data: Dict[str, Any]) -> bool:
        """Migrate data from mock.js format to database"""
        try:
            now = datetime.now(timezone.utc)

            # Portfolio
            portfolio = Portfolio(
                personal = PersonalInfo(**mock_data["personal"]),
                about = AboutSection(**mock_data["about"]),
            )
            await self.portfolios.update_one(
                {"userId": "default"},
                {
                    "$set": {**portfolio.model_dump(exclude = {"createdAt", "updatedAt"}), "updatedAt": now},
                    "$setOnInsert": {"createdAt": now},
                },
                upsert = True,
            )

            # Skills
            for i, skill_cat in enumerate(mock_data["skills"]["categories"]):
                skill = SkillCategory(
                    title = skill_cat["title"],
                    items = skill_cat["items"],
                    order = i,
                )
                await self.skills.update_one(
                    {"portfolioId": "default", "title": skill.title},
                    {
                        "$set": {**skill.model_dump(exclude = {"createdAt", "updatedAt"}), "updatedAt": now},
                        "$setOnInsert": {"createdAt": now},
                    },
                    upsert = True,
                )

            # Experiences
            for i, exp in enumerate(mock_data["experience"]):
                experience = Experience(
                    title = exp["title"],
                    company = exp["company"],
                    location = exp["location"],
                    duration = exp["duration"],
                    description = exp["description"],
                    current = exp.get("current", False),
                    order = i,
                )
                await self.experiences.update_one(
                    {"portfolioId": "default", "title": experience.title, "company": experience.company},
                    {
                        "$set": {**experience.model_dump(exclude = {"createdAt", "updatedAt"}), "updatedAt": now},
                        "$setOnInsert": {"createdAt": now},
                    },
                    upsert = True,
                )

            # Projects
            for i, proj in enumerate(mock_data["projects"]):
                project = Project(
                    title = proj["title"],
                    description = proj["description"],
                    technologies = proj["technologies"],
                    github = proj.get("github", "#"),
                    demo = proj.get("demo", "#"),
                    featured = proj.get("featured", False),
                    placeholder = proj.get("placeholder", False),
                    order = i,
                )
                await self.projects.update_one(
                    {"portfolioId": "default", "title": project.title},
                    {
                        "$set": {**project.model_dump(exclude = {"createdAt", "updatedAt"}), "updatedAt": now},
                        "$setOnInsert": {"createdAt": now},
                    },
                    upsert = True,
                )

            # Achievements
            for i, ach in enumerate(mock_data["achievements"]):
                achievement = Achievement(
                    title = ach["title"],
                    description = ach["description"],
                    order = i,
                )
                await self.achievements.update_one(
                    {"portfolioId": "default", "title": achievement.title},
                    {
                        "$set": {**achievement.model_dump(exclude = {"createdAt", "updatedAt"}), "updatedAt": now},
                        "$setOnInsert": {"createdAt": now},
                    },
                    upsert = True,
                )

            # Publications
            for i, pub in enumerate(mock_data["publications"]):
                publication = Publication(
                    title = pub["title"],
                    authors = pub["authors"],
                    publication = pub["publication"],
                    year = pub["year"],
                    doi = pub.get("doi"),
                    order = i,
                )
                await self.publications.update_one(
                    {"portfolioId": "default", "title": publication.title},
                    {
                        "$set": {**publication.model_dump(exclude = {"createdAt", "updatedAt"}), "updatedAt": now},
                        "$setOnInsert": {"createdAt": now},
                    },
                    upsert = True,
                )

            return True
        
        except Exception as e:
            logger.exception(f"Migration error: {e}")
            return False    
        
    async def export_data(self, portfolio_id: str = "default") -> Optional[PortfolioResponse]:
        """Export all portfolio data"""
        return await self.get_portfolio(portfolio_id)