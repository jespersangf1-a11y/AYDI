# backend/app/api/routes/structural_items.py
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.models import Layout, StructuralItem
from app.schemas.structural import (
    StructuralItemCreate,
    StructuralItemResponse,
    StructuralItemUpdate,
)

router = APIRouter(prefix="/projects/{project_id}", tags=["structural"])


@router.get(
    "/layouts/{layout_id}/structural",
    response_model=list[StructuralItemResponse],
)
async def list_structural_items(
    project_id: UUID,
    layout_id: UUID,
    item_type: str | None = None,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Layout).where(Layout.id == layout_id, Layout.project_id == project_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")

    query = select(StructuralItem).where(StructuralItem.layout_id == layout_id)
    if item_type:
        query = query.where(StructuralItem.item_type == item_type)
    result = await db.execute(query)
    return result.scalars().all()


@router.post(
    "/layouts/{layout_id}/structural",
    response_model=StructuralItemResponse,
    status_code=201,
)
async def create_structural_item(
    project_id: UUID,
    layout_id: UUID,
    data: StructuralItemCreate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Layout).where(Layout.id == layout_id, Layout.project_id == project_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")

    item = StructuralItem(**data.model_dump(), layout_id=layout_id)
    db.add(item)
    await db.commit()
    await db.refresh(item)
    return item


@router.get(
    "/layouts/{layout_id}/structural/{item_id}",
    response_model=StructuralItemResponse,
)
async def get_structural_item(
    project_id: UUID,
    layout_id: UUID,
    item_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Layout).where(Layout.id == layout_id, Layout.project_id == project_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")

    result = await db.execute(
        select(StructuralItem).where(
            StructuralItem.id == item_id,
            StructuralItem.layout_id == layout_id,
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Strukturelement nicht gefunden")
    return item


@router.patch(
    "/layouts/{layout_id}/structural/{item_id}",
    response_model=StructuralItemResponse,
)
async def update_structural_item(
    project_id: UUID,
    layout_id: UUID,
    item_id: UUID,
    data: StructuralItemUpdate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Layout).where(Layout.id == layout_id, Layout.project_id == project_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")

    result = await db.execute(
        select(StructuralItem).where(
            StructuralItem.id == item_id,
            StructuralItem.layout_id == layout_id,
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Strukturelement nicht gefunden")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(item, field, value)

    await db.commit()
    await db.refresh(item)
    return item


@router.delete(
    "/layouts/{layout_id}/structural/{item_id}",
    status_code=204,
)
async def delete_structural_item(
    project_id: UUID,
    layout_id: UUID,
    item_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Layout).where(Layout.id == layout_id, Layout.project_id == project_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")

    result = await db.execute(
        select(StructuralItem).where(
            StructuralItem.id == item_id,
            StructuralItem.layout_id == layout_id,
        )
    )
    item = result.scalar_one_or_none()
    if not item:
        raise HTTPException(status_code=404, detail="Strukturelement nicht gefunden")
    await db.delete(item)
    await db.commit()
