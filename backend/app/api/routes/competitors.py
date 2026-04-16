# backend/app/api/routes/competitors.py
import logging
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import func, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.permissions import get_current_user
from app.db.database import get_db
from app.models.models import BrandReferenceModel, CompetitorModel, User
from app.schemas.competitors import (
    BrandReferenceCreate,
    BrandReferenceResponse,
    CompetitorCreate,
    CompetitorResponse,
    CompetitorUpdate,
)

logger = logging.getLogger(__name__)

router = APIRouter(tags=["competitors"])


# --- Competitor models ---


@router.get("/competitors", response_model=list[CompetitorResponse])
async def list_competitors(
    boat_class: str | None = None,
    brand: str | None = None,
    limit: int = Query(100, ge=1, le=500),
    offset: int = Query(0, ge=0),
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    query = select(CompetitorModel).order_by(CompetitorModel.brand, CompetitorModel.model_name)
    if boat_class:
        query = query.where(CompetitorModel.boat_class == boat_class)
    if brand:
        query = query.where(CompetitorModel.brand == brand)
    query = query.limit(limit).offset(offset)
    result = await db.execute(query)
    return result.scalars().all()


@router.post("/competitors", response_model=CompetitorResponse, status_code=201)
async def create_competitor(
    data: CompetitorCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    competitor = CompetitorModel(**data.model_dump())
    db.add(competitor)
    await db.commit()
    await db.refresh(competitor)
    logger.info("User %s created competitor %s", _user.id, competitor.id)
    return competitor


@router.get("/competitors/segment/{boat_class}")
async def get_segment_statistics(
    boat_class: str,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(CompetitorModel).where(CompetitorModel.boat_class == boat_class)
    )
    competitors = result.scalars().all()

    count = len(competitors)

    # Average length
    lengths = [c.length_m for c in competitors if c.length_m is not None]
    avg_length_m = round(sum(lengths) / len(lengths), 2) if lengths else None

    # Average price from price_range_eur min/max avg
    prices: list[float] = []
    for c in competitors:
        if c.price_range_eur:
            min_p = c.price_range_eur.get("min")
            max_p = c.price_range_eur.get("max")
            if min_p is not None and max_p is not None:
                prices.append((min_p + max_p) / 2)
            elif min_p is not None:
                prices.append(min_p)
            elif max_p is not None:
                prices.append(max_p)
    avg_price = round(sum(prices) / len(prices), 2) if prices else None

    # Unique brands
    brands = sorted({c.brand for c in competitors})

    return {
        "boat_class": boat_class,
        "count": count,
        "avg_length_m": avg_length_m,
        "avg_price": avg_price,
        "brands": brands,
    }


@router.get("/competitors/{competitor_id}", response_model=CompetitorResponse)
async def get_competitor(
    competitor_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(CompetitorModel).where(CompetitorModel.id == competitor_id)
    )
    competitor = result.scalar_one_or_none()
    if not competitor:
        raise HTTPException(status_code=404, detail="Wettbewerbermodell nicht gefunden")
    return competitor


@router.patch("/competitors/{competitor_id}", response_model=CompetitorResponse)
async def update_competitor(
    competitor_id: UUID,
    data: CompetitorUpdate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(CompetitorModel).where(CompetitorModel.id == competitor_id)
    )
    competitor = result.scalar_one_or_none()
    if not competitor:
        raise HTTPException(status_code=404, detail="Wettbewerbermodell nicht gefunden")

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(competitor, field, value)

    await db.commit()
    await db.refresh(competitor)
    logger.info("User %s updated competitor %s (fields: %s)", _user.id, competitor_id, list(update_data.keys()))
    return competitor


@router.delete("/competitors/{competitor_id}", status_code=204)
async def delete_competitor(
    competitor_id: UUID,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(CompetitorModel).where(CompetitorModel.id == competitor_id)
    )
    competitor = result.scalar_one_or_none()
    if not competitor:
        raise HTTPException(status_code=404, detail="Wettbewerbermodell nicht gefunden")
    await db.delete(competitor)
    await db.commit()
    logger.info("User %s deleted competitor %s", _user.id, competitor_id)


# --- Brand reference models ---


@router.get("/brand-references", response_model=list[BrandReferenceResponse])
async def list_brand_references(
    boat_class: str | None = None,
    shipyard_id: str | None = None,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    query = select(BrandReferenceModel).order_by(
        BrandReferenceModel.model_name
    )
    if boat_class:
        query = query.where(BrandReferenceModel.boat_class == boat_class)
    if shipyard_id:
        query = query.where(BrandReferenceModel.shipyard_id == shipyard_id)
    result = await db.execute(query)
    return result.scalars().all()


@router.post("/brand-references", response_model=BrandReferenceResponse, status_code=201)
async def create_brand_reference(
    data: BrandReferenceCreate,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    ref = BrandReferenceModel(**data.model_dump())
    db.add(ref)
    await db.commit()
    await db.refresh(ref)
    logger.info("User %s created brand reference %s", _user.id, ref.id)
    return ref


@router.get("/brand-references/{ref_id}", response_model=BrandReferenceResponse)
async def get_brand_reference(
    ref_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(BrandReferenceModel).where(BrandReferenceModel.id == ref_id)
    )
    ref = result.scalar_one_or_none()
    if not ref:
        raise HTTPException(status_code=404, detail="Referenzmodell nicht gefunden")
    return ref


@router.delete("/brand-references/{ref_id}", status_code=204)
async def delete_brand_reference(
    ref_id: UUID,
    db: AsyncSession = Depends(get_db),
    _user: User = Depends(get_current_user),
):
    result = await db.execute(
        select(BrandReferenceModel).where(BrandReferenceModel.id == ref_id)
    )
    ref = result.scalar_one_or_none()
    if not ref:
        raise HTTPException(status_code=404, detail="Referenzmodell nicht gefunden")
    await db.delete(ref)
    await db.commit()
    logger.info("User %s deleted brand reference %s", _user.id, ref_id)
