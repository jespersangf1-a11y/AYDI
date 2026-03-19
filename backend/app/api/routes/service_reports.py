# backend/app/api/routes/service_reports.py
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.models import ServiceReport
from app.schemas.service import ServiceReportCreate, ServiceReportResponse, ServiceReportUpdate

router = APIRouter(tags=["service-reports"])


@router.get("/service-reports", response_model=list[ServiceReportResponse])
async def list_service_reports(
    category: str | None = None,
    severity: str | None = None,
    boat_class: str | None = None,
    report_type: str | None = None,
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
    result = await db.execute(query)
    return result.scalars().all()


@router.post("/service-reports", response_model=ServiceReportResponse, status_code=201)
async def create_service_report(
    data: ServiceReportCreate,
    db: AsyncSession = Depends(get_db),
):
    report = ServiceReport(**data.model_dump())
    db.add(report)
    await db.commit()
    await db.refresh(report)
    return report


@router.get("/service-reports/{report_id}", response_model=ServiceReportResponse)
async def get_service_report(
    report_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(ServiceReport).where(ServiceReport.id == report_id))
    report = result.scalar_one_or_none()
    if not report:
        raise HTTPException(status_code=404, detail="Servicebericht nicht gefunden")
    return report


@router.patch("/service-reports/{report_id}", response_model=ServiceReportResponse)
async def update_service_report(
    report_id: UUID,
    data: ServiceReportUpdate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(ServiceReport).where(ServiceReport.id == report_id))
    report = result.scalar_one_or_none()
    if not report:
        raise HTTPException(status_code=404, detail="Servicebericht nicht gefunden")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(report, field, value)

    await db.commit()
    await db.refresh(report)
    return report


@router.delete("/service-reports/{report_id}", status_code=204)
async def delete_service_report(
    report_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(ServiceReport).where(ServiceReport.id == report_id))
    report = result.scalar_one_or_none()
    if not report:
        raise HTTPException(status_code=404, detail="Servicebericht nicht gefunden")
    await db.delete(report)
    await db.commit()
