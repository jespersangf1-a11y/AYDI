# backend/app/api/routes/materials.py
import logging
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.permissions import get_current_user
from app.db.database import get_db
from app.models.models import Layout, Material, Project, User, ZoneMaterial
from app.schemas.materials import (
    MaterialCreate,
    MaterialResponse,
    MaterialUpdate,
    ZoneMaterialCreate,
    ZoneMaterialResponse,
)

logger = logging.getLogger(__name__)

router = APIRouter(tags=["materials"])


async def _verify_project_ownership(
    project_id: UUID,
    user: User,
    db: AsyncSession,
) -> None:
    """Verify the project exists and belongs to the given user."""
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.user_id == user.id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Projekt nicht gefunden")


# --- Global material database ---


@router.get("/materials", response_model=list[MaterialResponse])
async def list_materials(
    category: str | None = None,
    subcategory: str | None = None,
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    query = select(Material).order_by(Material.name)
    if category:
        query = query.where(Material.category == category)
    if subcategory:
        query = query.where(Material.subcategory == subcategory)
    query = query.limit(limit).offset(offset)
    result = await db.execute(query)
    return result.scalars().all()


@router.post("/materials", response_model=MaterialResponse, status_code=201)
async def create_material(
    data: MaterialCreate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    material = Material(**data.model_dump())
    db.add(material)
    await db.commit()
    await db.refresh(material)
    logger.info("User %s created material %s", _user.id, material.id)
    return material


@router.get("/materials/{material_id}", response_model=MaterialResponse)
async def get_material(
    material_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Material).where(Material.id == material_id))
    material = result.scalar_one_or_none()
    if not material:
        raise HTTPException(status_code=404, detail="Material nicht gefunden")
    return material


@router.patch("/materials/{material_id}", response_model=MaterialResponse)
async def update_material(
    material_id: UUID,
    data: MaterialUpdate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Material).where(Material.id == material_id))
    material = result.scalar_one_or_none()
    if not material:
        raise HTTPException(status_code=404, detail="Material nicht gefunden")

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(material, field, value)

    await db.commit()
    await db.refresh(material)
    logger.info("User %s updated material %s (fields: %s)", _user.id, material_id, list(update_data.keys()))
    return material


@router.delete("/materials/{material_id}", status_code=204)
async def delete_material(
    material_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Material).where(Material.id == material_id))
    material = result.scalar_one_or_none()
    if not material:
        raise HTTPException(status_code=404, detail="Material nicht gefunden")
    await db.delete(material)
    await db.commit()
    logger.info("User %s deleted material %s", _user.id, material_id)


# --- Zone material assignments (per layout) ---


@router.get(
    "/projects/{project_id}/layouts/{layout_id}/materials",
    response_model=list[ZoneMaterialResponse],
)
async def list_zone_materials(
    project_id: UUID,
    layout_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await _verify_project_ownership(project_id, _user, db)
    result = await db.execute(
        select(Layout).where(Layout.id == layout_id, Layout.project_id == project_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")

    result = await db.execute(
        select(ZoneMaterial).where(ZoneMaterial.layout_id == layout_id)
    )
    return result.scalars().all()


@router.post(
    "/projects/{project_id}/layouts/{layout_id}/materials",
    response_model=ZoneMaterialResponse,
    status_code=201,
)
async def assign_zone_material(
    project_id: UUID,
    layout_id: UUID,
    data: ZoneMaterialCreate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await _verify_project_ownership(project_id, _user, db)
    result = await db.execute(
        select(Layout).where(Layout.id == layout_id, Layout.project_id == project_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")

    # Verify material exists
    result = await db.execute(
        select(Material).where(Material.id == data.material_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Material nicht gefunden")

    zone_mat = ZoneMaterial(
        layout_id=layout_id,
        zone_name=data.zone_name,
        surface_type=data.surface_type,
        material_id=data.material_id,
        area_sqm=data.area_sqm,
        notes=data.notes,
    )
    db.add(zone_mat)
    await db.commit()
    await db.refresh(zone_mat)
    logger.info("User %s assigned material to zone %s (zone_material_id: %s)", _user.id, data.zone_name, zone_mat.id)
    return zone_mat


@router.delete(
    "/projects/{project_id}/layouts/{layout_id}/materials/{zone_material_id}",
    status_code=204,
)
async def delete_zone_material(
    project_id: UUID,
    layout_id: UUID,
    zone_material_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await _verify_project_ownership(project_id, _user, db)
    result = await db.execute(
        select(Layout).where(Layout.id == layout_id, Layout.project_id == project_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")

    result = await db.execute(
        select(ZoneMaterial).where(
            ZoneMaterial.id == zone_material_id,
            ZoneMaterial.layout_id == layout_id,
        )
    )
    zone_mat = result.scalar_one_or_none()
    if not zone_mat:
        raise HTTPException(status_code=404, detail="Materialzuweisung nicht gefunden")
    await db.delete(zone_mat)
    await db.commit()
    logger.info("User %s deleted zone material assignment %s", _user.id, zone_material_id)
