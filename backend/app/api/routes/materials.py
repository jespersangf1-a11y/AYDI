# backend/app/api/routes/materials.py
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.models import Layout, Material, ZoneMaterial
from app.schemas.materials import (
    MaterialCreate,
    MaterialResponse,
    MaterialUpdate,
    ZoneMaterialCreate,
    ZoneMaterialResponse,
)

router = APIRouter(tags=["materials"])


# --- Global material database ---


@router.get("/materials", response_model=list[MaterialResponse])
async def list_materials(
    category: str | None = None,
    subcategory: str | None = None,
    db: AsyncSession = Depends(get_db),
):
    query = select(Material).order_by(Material.name)
    if category:
        query = query.where(Material.category == category)
    if subcategory:
        query = query.where(Material.subcategory == subcategory)
    result = await db.execute(query)
    return result.scalars().all()


@router.post("/materials", response_model=MaterialResponse, status_code=201)
async def create_material(
    data: MaterialCreate,
    db: AsyncSession = Depends(get_db),
):
    material = Material(**data.model_dump())
    db.add(material)
    await db.commit()
    await db.refresh(material)
    return material


@router.get("/materials/{material_id}", response_model=MaterialResponse)
async def get_material(
    material_id: UUID,
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
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Material).where(Material.id == material_id))
    material = result.scalar_one_or_none()
    if not material:
        raise HTTPException(status_code=404, detail="Material nicht gefunden")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(material, field, value)

    await db.commit()
    await db.refresh(material)
    return material


@router.delete("/materials/{material_id}", status_code=204)
async def delete_material(
    material_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Material).where(Material.id == material_id))
    material = result.scalar_one_or_none()
    if not material:
        raise HTTPException(status_code=404, detail="Material nicht gefunden")
    await db.delete(material)
    await db.commit()


# --- Zone material assignments (per layout) ---


@router.get(
    "/projects/{project_id}/layouts/{layout_id}/materials",
    response_model=list[ZoneMaterialResponse],
)
async def list_zone_materials(
    project_id: UUID,
    layout_id: UUID,
    db: AsyncSession = Depends(get_db),
):
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
    db: AsyncSession = Depends(get_db),
):
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
    return zone_mat


@router.delete(
    "/projects/{project_id}/layouts/{layout_id}/materials/{zone_material_id}",
    status_code=204,
)
async def delete_zone_material(
    project_id: UUID,
    layout_id: UUID,
    zone_material_id: UUID,
    db: AsyncSession = Depends(get_db),
):
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
