# backend/app/api/routes/costs.py
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.permissions import get_current_user
from app.db.database import get_db
from app.models.models import CostItem, Layout, User
from app.schemas.costs import CostItemCreate, CostItemResponse, CostItemUpdate

router = APIRouter(prefix="/projects/{project_id}", tags=["costs"])


async def _verify_layout(
    project_id: UUID,
    layout_id: UUID,
    db: AsyncSession,
) -> None:
    """Verify the layout exists and belongs to the given project."""
    result = await db.execute(
        select(Layout).where(Layout.id == layout_id, Layout.project_id == project_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")


@router.get(
    "/layouts/{layout_id}/costs",
    response_model=list[CostItemResponse],
)
async def list_cost_items(
    project_id: UUID,
    layout_id: UUID,
    category: str | None = None,
    db: AsyncSession = Depends(get_db),
):
    """List all cost items for a layout, with optional category filter."""
    await _verify_layout(project_id, layout_id, db)

    query = select(CostItem).where(CostItem.layout_id == layout_id).order_by(
        CostItem.category, CostItem.created_at
    )
    if category:
        query = query.where(CostItem.category == category)

    result = await db.execute(query)
    return result.scalars().all()


@router.post(
    "/layouts/{layout_id}/costs",
    response_model=CostItemResponse,
    status_code=201,
)
async def create_cost_item(
    project_id: UUID,
    layout_id: UUID,
    data: CostItemCreate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Create a new cost item for a layout."""
    await _verify_layout(project_id, layout_id, db)

    cost_item = CostItem(layout_id=layout_id, **data.model_dump())
    db.add(cost_item)
    await db.commit()
    await db.refresh(cost_item)
    return cost_item


@router.get(
    "/layouts/{layout_id}/costs/summary",
)
async def get_cost_summary(
    project_id: UUID,
    layout_id: UUID,
    db: AsyncSession = Depends(get_db),
) -> dict:
    """Return aggregated cost breakdown by category and zone for a layout."""
    await _verify_layout(project_id, layout_id, db)

    result = await db.execute(
        select(CostItem).where(CostItem.layout_id == layout_id)
    )
    items = result.scalars().all()

    total_cost: float = 0.0
    breakdown_by_category: dict[str, float] = {}
    breakdown_by_zone: dict[str, float] = {}

    for item in items:
        total_cost += item.total_cost_eur

        breakdown_by_category[item.category] = (
            breakdown_by_category.get(item.category, 0.0) + item.total_cost_eur
        )

        if item.zone_name:
            breakdown_by_zone[item.zone_name] = (
                breakdown_by_zone.get(item.zone_name, 0.0) + item.total_cost_eur
            )

    return {
        "total_cost": round(total_cost, 2),
        "breakdown_by_category": {k: round(v, 2) for k, v in breakdown_by_category.items()},
        "breakdown_by_zone": {k: round(v, 2) for k, v in breakdown_by_zone.items()},
        "item_count": len(items),
    }


@router.get(
    "/layouts/{layout_id}/costs/{cost_item_id}",
    response_model=CostItemResponse,
)
async def get_cost_item(
    project_id: UUID,
    layout_id: UUID,
    cost_item_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    """Get a single cost item by ID."""
    await _verify_layout(project_id, layout_id, db)

    result = await db.execute(
        select(CostItem).where(
            CostItem.id == cost_item_id,
            CostItem.layout_id == layout_id,
        )
    )
    cost_item = result.scalar_one_or_none()
    if not cost_item:
        raise HTTPException(status_code=404, detail="Kostenposition nicht gefunden")
    return cost_item


@router.patch(
    "/layouts/{layout_id}/costs/{cost_item_id}",
    response_model=CostItemResponse,
)
async def update_cost_item(
    project_id: UUID,
    layout_id: UUID,
    cost_item_id: UUID,
    data: CostItemUpdate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Partially update a cost item."""
    await _verify_layout(project_id, layout_id, db)

    result = await db.execute(
        select(CostItem).where(
            CostItem.id == cost_item_id,
            CostItem.layout_id == layout_id,
        )
    )
    cost_item = result.scalar_one_or_none()
    if not cost_item:
        raise HTTPException(status_code=404, detail="Kostenposition nicht gefunden")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(cost_item, field, value)

    await db.commit()
    await db.refresh(cost_item)
    return cost_item


@router.delete(
    "/layouts/{layout_id}/costs/{cost_item_id}",
    status_code=204,
)
async def delete_cost_item(
    project_id: UUID,
    layout_id: UUID,
    cost_item_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Delete a cost item."""
    await _verify_layout(project_id, layout_id, db)

    result = await db.execute(
        select(CostItem).where(
            CostItem.id == cost_item_id,
            CostItem.layout_id == layout_id,
        )
    )
    cost_item = result.scalar_one_or_none()
    if not cost_item:
        raise HTTPException(status_code=404, detail="Kostenposition nicht gefunden")

    await db.delete(cost_item)
    await db.commit()
