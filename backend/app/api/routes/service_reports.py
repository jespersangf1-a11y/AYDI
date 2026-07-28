# backend/app/api/routes/service_reports.py
import logging
from uuid import UUID

from fastapi import APIRouter, Depends, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.ownership import (
    ensure_readable,
    ensure_writable,
    owner_id_for,
    visible_to,
)
from app.core.permissions import get_current_user
from app.db.database import get_db
from app.models.models import ServiceReport, User
from app.schemas.service import ServiceReportCreate, ServiceReportResponse, ServiceReportUpdate

logger = logging.getLogger(__name__)

router = APIRouter(tags=["service-reports"])


@router.get("/service-reports", response_model=list[ServiceReportResponse])
async def list_service_reports(
    category: str | None = None,
    severity: str | None = None,
    boat_class: str | None = None,
    report_type: str | None = None,
    limit: int = Query(50, ge=1, le=200),
    offset: int = Query(0, ge=0),
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    query = select(ServiceReport).order_by(ServiceReport.created_at.desc())
    if category:
        query = query.where(ServiceReport.category == category)
    if severity:
        query = query.where(ServiceReport.severity == severity)
    if boat_class:
        query = query.where(ServiceReport.boat_class == boat_class)
    if report_type:
        query = query.where(ServiceReport.report_type == report_type)
    # Der mitgelieferte Berichtsbestand plus die eigenen Berichte. Ein
    # Servicebericht einer fremden Werft ist damit nicht mehr abrufbar.
    query = visible_to(query, ServiceReport, user)
    query = query.limit(limit).offset(offset)
    result = await db.execute(query)
    return result.scalars().all()


@router.post("/service-reports", response_model=ServiceReportResponse, status_code=201)
async def create_service_report(
    data: ServiceReportCreate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    report = ServiceReport(**data.model_dump(), owner_id=owner_id_for(user))
    db.add(report)
    await db.commit()
    await db.refresh(report)
    logger.info("User %s created service report %s", user.id, report.id)
    return report


@router.get("/service-reports/{report_id}", response_model=ServiceReportResponse)
async def get_service_report(
    report_id: UUID,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(ServiceReport).where(ServiceReport.id == report_id))
    return ensure_readable(result.scalar_one_or_none(), user, name="Servicebericht")


@router.patch("/service-reports/{report_id}", response_model=ServiceReportResponse)
async def update_service_report(
    report_id: UUID,
    data: ServiceReportUpdate,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(ServiceReport).where(ServiceReport.id == report_id))
    report = ensure_writable(result.scalar_one_or_none(), user, name="Servicebericht")

    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(report, field, value)

    await db.commit()
    await db.refresh(report)
    logger.info("User %s updated service report %s (fields: %s)", user.id, report_id, list(update_data.keys()))
    return report


@router.delete("/service-reports/{report_id}", status_code=204)
async def delete_service_report(
    report_id: UUID,
    user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(ServiceReport).where(ServiceReport.id == report_id))
    report = ensure_writable(result.scalar_one_or_none(), user, name="Servicebericht")
    await db.delete(report)
    await db.commit()
    logger.info("User %s deleted service report %s", user.id, report_id)
