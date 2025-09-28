from fastapi import APIRouter, HTTPException, Depends, Request
from typing import Dict, Any
from models.portfolio import *
from services.portfolio_service import PortfolioService
from motor.core import AgnosticDatabase

# Create router
router = APIRouter(prefix = "/api", tags = ["portfolio"])

# Dependency to get database
def get_database(request: Request) -> AgnosticDatabase:
    return request.app.database

# Dependency to get portfolio service
def get_portfolio_service(db: AgnosticDatabase = Depends(get_database)):
    return PortfolioService(db)

# Portfolio endpoints
@router.get("/portfolio")
async def get_portfolio(service: PortfolioService = Depends(get_portfolio_service)):
    """Get complete portfolio data"""
    try:
        portfolio_data = await service.get_portfolio()
        if not portfolio_data:
            raise HTTPException(status_code = 404, detail = "Portfolio not found")
        return portfolio_data
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.put("/portfolio/personal", response_model = Dict[str, str])
async def update_personal_info(
    updates: PersonalInfoUpdate,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Update personal information"""
    try:
        success = await service.update_personal_info(updates)
        if not success:
            raise HTTPException(status_code = 400, detail = "No updates provided or portfolio not found")
        return {"message": "Personal information updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.put("/portfolio/about", response_model = Dict[str, str])
async def update_about_section(
    updates: AboutSectionUpdate,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Update about section"""
    try:
        success = await service.update_about_section(updates)
        if not success:
            raise HTTPException(status_code = 400, detail = "No updates provided or portfolio not found")
        return {"message": "About section updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

# Skills endpoints
@router.get("/skills")
async def get_skills(service: PortfolioService = Depends(get_portfolio_service)):
    """Get all skill categories"""
    try:
        skills = await service.get_skills()
        return skills
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.post("/skills", response_model = SkillCategory)
async def create_skill(
    skill_data: SkillCategoryCreate,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Create new skill category"""
    try:
        skill = await service.create_skill(skill_data)
        return skill
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.put("/skills/{skill_id}", response_model = Dict[str, str])
async def update_skill(
    skill_id: str,
    updates: SkillCategoryUpdate,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Update skill category"""
    try:
        success = await service.update_skill(skill_id, updates)
        if not success:
            raise HTTPException(status_code = 404, detail = "Skill category not found or no updates provided")
        return {"message": "Skill category updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.delete("/skills/{skill_id}", response_model = Dict[str, str])
async def delete_skill(
    skill_id: str,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Delete skill category"""
    try:
        success = await service.delete_skill(skill_id)
        if not success:
            raise HTTPException(status_code = 404, detail = "Skill category not found")
        return {"message": "Skill category deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

# Experience endpoints
@router.get("/experience")
async def get_experiences(service: PortfolioService = Depends(get_portfolio_service)):
    """Get all experiences"""
    try:
        experiences = await service.get_experiences()
        return experiences
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.post("/experience", response_model = Experience)
async def create_experience(
    exp_data: ExperienceCreate,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Create new experience"""
    try:
        experience = await service.create_experience(exp_data)
        return experience
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.put("/experience/{exp_id}", response_model = Dict[str, str])
async def update_experience(
    exp_id: str,
    updates: ExperienceUpdate,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Update experience"""
    try:
        success = await service.update_experience(exp_id, updates)
        if not success:
            raise HTTPException(status_code = 404, detail = "Experience not found or no updates provided")
        return {"message": "Experience updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.delete("/experience/{exp_id}", response_model = Dict[str, str])
async def delete_experience(
    exp_id: str,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Delete experience"""
    try:
        success = await service.delete_experience(exp_id)
        if not success:
            raise HTTPException(status_code = 404, detail = "Experience not found")
        return {"message": "Experience deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

# Projects endpoints
@router.get("/projects")
async def get_projects(service: PortfolioService = Depends(get_portfolio_service)):
    """Get all projects"""
    try:
        projects = await service.get_projects()
        return projects
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.post("/projects", response_model = Project)
async def create_project(
    project_data: ProjectCreate,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Create new project"""
    try:
        project = await service.create_project(project_data)
        return project
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.put("/projects/{project_id}", response_model = Dict[str, str])
async def update_project(
    project_id: str,
    updates: ProjectUpdate,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Update project"""
    try:
        success = await service.update_project(project_id, updates)
        if not success:
            raise HTTPException(status_code = 404, detail = "Project not found or no updates provided")
        return {"message": "Project updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.delete("/projects/{project_id}", response_model = Dict[str, str])
async def delete_project(
    project_id: str,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Delete project"""
    try:
        success = await service.delete_project(project_id)
        if not success:
            raise HTTPException(status_code = 404, detail = "Project not found")
        return {"message": "Project deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

# Achievements endpoints
@router.get("/achievements")
async def get_achievements(service: PortfolioService = Depends(get_portfolio_service)):
    """Get all achievements"""
    try:
        achievements = await service.get_achievements()
        return achievements
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.post("/achievements", response_model = Achievement)
async def create_achievement(
    achievement_data: AchievementCreate,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Create new achievement"""
    try:
        achievement = await service.create_achievement(achievement_data)
        return achievement
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.put("/achievements/{achievement_id}", response_model = Dict[str, str])
async def update_achievement(
    achievement_id: str,
    updates: AchievementUpdate,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Update achievement"""
    try:
        success = await service.update_achievement(achievement_id, updates)
        if not success:
            raise HTTPException(status_code = 404, detail = "Achievement not found or no updates provided")
        return {"message": "Achievement updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.delete("/achievements/{achievement_id}", response_model = Dict[str, str])
async def delete_achievement(
    achievement_id: str,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Delete achievement"""
    try:
        success = await service.delete_achievement(achievement_id)
        if not success:
            raise HTTPException(status_code = 404, detail = "Achievement not found")
        return {"message": "Achievement deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

# Publications endpoints
@router.get("/publications")
async def get_publications(service: PortfolioService = Depends(get_portfolio_service)):
    """Get all publications"""
    try:
        publications = await service.get_publications()
        return publications
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.post("/publications", response_model = Publication)
async def create_publication(
    pub_data: PublicationCreate,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Create new publication"""
    try:
        publication = await service.create_publication(pub_data)
        return publication
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.put("/publications/{pub_id}", response_model = Dict[str, str])
async def update_publication(
    pub_id: str,
    updates: PublicationUpdate,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Update publication"""
    try:
        success = await service.update_publication(pub_id, updates)
        if not success:
            raise HTTPException(status_code = 404, detail = "Publication not found or no updates provided")
        return {"message": "Publication updated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.delete("/publications/{pub_id}", response_model = Dict[str, str])
async def delete_publication(
    pub_id: str,
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Delete publication"""
    try:
        success = await service.delete_publication(pub_id)
        if not success:
            raise HTTPException(status_code = 404, detail = "Publication not found")
        return {"message": "Publication deleted successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

# Migration and export endpoints
@router.post("/migrate", response_model = Dict[str, str])
async def migrate_mock_data( 
    mock_data: Dict[str, Any],
    service: PortfolioService = Depends(get_portfolio_service)
):
    """Migrate mock.js data to database"""
    try:
        success = await service.migrate_mock_data(mock_data)
        if not success:
            raise HTTPException(status_code = 422, detail = "Migration failed")
        return {"message": "Data migrated successfully"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))

@router.get("/export")
async def export_data(service: PortfolioService = Depends(get_portfolio_service)):
    """Export all portfolio data"""
    try:
        data = await service.export_data()
        if not data:
            raise HTTPException(status_code = 404, detail = "No data found")
        return data
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code = 500, detail = str(e))