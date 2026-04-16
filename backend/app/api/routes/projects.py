import logging
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.permissions import get_current_user
from app.db.database import get_db
from app.models.models import Project, User
from app.schemas.schemas import ProjectCreate, ProjectResponse, ProjectStatus, ProjectUpdate

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/projects", tags=["projects"])


async def _get_user_project(project_id: UUID, user: User, db: AsyncSession) -> Project:
    """Fetch a project ensuring it belongs to the authenticated user."""
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.user_id == user.id)
    )
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="Projekt nicht gefunden")
    return project


@router.get("", response_model=list[ProjectResponse])
async def list_projects(
    status: ProjectStatus | None = None,
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    query = select(Project).where(Project.user_id == _user.id)
    if status:
        query = query.where(Project.status == status.value)
    query = query.order_by(Project.created_at.desc()).limit(limit).offset(offset)
    result = await db.execute(query)
    return result.scalars().all()


@router.post("", response_model=ProjectResponse, status_code=201)
async def create_project(
    data: ProjectCreate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    project = Project(**data.model_dump(), user_id=_user.id)
    db.add(project)
    await db.commit()
    await db.refresh(project)
    logger.info("User %s created project %s (%s)", _user.id, project.id, data.name)
    return project


@router.get("/{project_id}", response_model=ProjectResponse)
async def get_project(
    project_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    return await _get_user_project(project_id, _user, db)


@router.patch("/{project_id}", response_model=ProjectResponse)
async def update_project(
    project_id: UUID,
    data: ProjectUpdate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    project = await _get_user_project(project_id, _user, db)

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        if isinstance(value, ProjectStatus):
            value = value.value
        setattr(project, field, value)

    await db.commit()
    await db.refresh(project)
    logger.info("User %s updated project %s (fields: %s)", _user.id, project_id, list(update_data.keys()))
    return project


@router.delete("/{project_id}", status_code=204)
async def delete_project(
    project_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    project = await _get_user_project(project_id, _user, db)
    await db.delete(project)
    await db.commit()
    logger.info("User %s deleted project %s", _user.id, project_id)
