"""Community Intelligence API endpoints."""
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.models import CommunityReport, CommunityPattern
from app.schemas.schemas import (
    AggregationResultResponse,
    CommunityReportCreate,
    CommunityReportResponse,
    CommunityPatternResponse,
)
from app.services.community.aggregator import aggregate_reports_to_patterns
from app.services.community.engine import find_relevant_patterns

router = APIRouter(prefix="/community", tags=["community"])


# === Reports ===

@router.post("/reports", response_model=CommunityReportResponse, status_code=201)
async def create_report(
    report: CommunityReportCreate,
    db: AsyncSession = Depends(get_db),
):
    """Create a community report."""
    db_report = CommunityReport(
        source_forum=report.source_forum,
        source_url=report.source_url,
        source_date=report.source_date,
        boat_manufacturer=report.boat_manufacturer,
        boat_model=report.boat_model,
        boat_year=report.boat_year,
        hull_material=report.hull_material,
        hull_construction=report.hull_construction,
        propulsion=report.propulsion,
        issues=[issue.model_dump() for issue in report.issues],
        positives=[pos.model_dump() for pos in report.positives],
        reliability=report.reliability,
        raw_text=report.raw_text,
    )
    db.add(db_report)
    await db.commit()
    await db.refresh(db_report)
    return db_report


@router.get("/reports", response_model=list[CommunityReportResponse])
async def list_reports(
    manufacturer: str | None = None,
    model: str | None = None,
    hull_material: str | None = None,
    limit: int = Query(default=50, le=200),
    offset: int = Query(default=0, ge=0),
    db: AsyncSession = Depends(get_db),
):
    """List community reports with optional filters."""
    query = select(CommunityReport)
    if manufacturer:
        query = query.where(CommunityReport.boat_manufacturer == manufacturer)
    if model:
        query = query.where(CommunityReport.boat_model == model)
    if hull_material:
        query = query.where(CommunityReport.hull_material == hull_material)
    query = query.order_by(CommunityReport.created_at.desc())
    query = query.offset(offset).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


@router.get("/reports/{report_id}", response_model=CommunityReportResponse)
async def get_report(report_id: int, db: AsyncSession = Depends(get_db)):
    """Get a single community report."""
    result = await db.execute(
        select(CommunityReport).where(CommunityReport.id == report_id)
    )
    report = result.scalar_one_or_none()
    if not report:
        raise HTTPException(status_code=404, detail="Report nicht gefunden")
    return report


# === Patterns ===

@router.get("/patterns", response_model=list[CommunityPatternResponse])
async def list_patterns(
    manufacturer: str | None = None,
    model: str | None = None,
    zone_type: str | None = None,
    is_positive: bool | None = None,
    limit: int = Query(default=50, le=200),
    offset: int = Query(default=0, ge=0),
    db: AsyncSession = Depends(get_db),
):
    """List community patterns with optional filters."""
    query = select(CommunityPattern)
    if manufacturer:
        query = query.where(CommunityPattern.manufacturer == manufacturer)
    if model:
        query = query.where(CommunityPattern.boat_model == model)
    if zone_type:
        query = query.where(CommunityPattern.zone_type == zone_type)
    if is_positive is not None:
        query = query.where(CommunityPattern.is_positive == is_positive)
    query = query.order_by(CommunityPattern.confidence.desc())
    query = query.offset(offset).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


@router.get("/patterns/{pattern_id}", response_model=CommunityPatternResponse)
async def get_pattern(pattern_id: int, db: AsyncSession = Depends(get_db)):
    """Get a single community pattern."""
    result = await db.execute(
        select(CommunityPattern).where(CommunityPattern.id == pattern_id)
    )
    pattern = result.scalar_one_or_none()
    if not pattern:
        raise HTTPException(status_code=404, detail="Pattern nicht gefunden")
    return pattern


# === Aggregation ===

@router.post("/aggregate", response_model=AggregationResultResponse)
async def run_aggregation(db: AsyncSession = Depends(get_db)):
    """Trigger batch aggregation of reports into patterns.

    Idempotent: deletes all existing patterns and recreates from reports.
    """
    result = await db.execute(select(CommunityReport))
    reports = result.scalars().all()

    report_dicts = []
    for r in reports:
        report_dicts.append({
            "id": r.id,
            "boat_manufacturer": r.boat_manufacturer,
            "boat_model": r.boat_model,
            "boat_year": r.boat_year,
            "hull_material": r.hull_material,
            "hull_construction": r.hull_construction,
            "propulsion": r.propulsion,
            "issues": r.issues or [],
            "positives": r.positives or [],
            "reliability": r.reliability,
        })

    pattern_dicts = aggregate_reports_to_patterns(report_dicts)

    await db.execute(CommunityPattern.__table__.delete())

    skipped_count = len([r for r in report_dicts if r.get("reliability", 0) < 0.3])
    for pd in pattern_dicts:
        db_pattern = CommunityPattern(
            manufacturer=pd["manufacturer"],
            boat_model=pd["boat_model"],
            issue_category=pd["issue_category"],
            zone_type=pd["zone_type"],
            description=pd["description"],
            report_count=pd["report_count"],
            severity_mode=pd["severity_mode"],
            typical_onset_years=pd["typical_onset_years"],
            materials_involved=pd["materials_involved"],
            construction_methods_involved=pd["construction_methods_involved"],
            confidence=pd["confidence"],
            source_report_ids=pd["source_report_ids"],
            is_positive=pd.get("is_positive", False),
        )
        db.add(db_pattern)

    await db.commit()

    return AggregationResultResponse(
        patterns_created=len(pattern_dicts),
        reports_processed=len(report_dicts) - skipped_count,
        reports_skipped=skipped_count,
        groups_below_threshold=0,
    )


# === Relevance Query ===

@router.get("/relevant")
async def get_relevant_patterns(
    manufacturer: str | None = None,
    model: str | None = None,
    boat_class: str = "cruising_sail",
    hull_material: str | None = None,
    hull_construction: str | None = None,
    max_results: int = Query(default=20, le=50),
    db: AsyncSession = Depends(get_db),
):
    """Get patterns relevant to a specific boat via 5-level relevance matching."""
    result = await db.execute(select(CommunityPattern))
    db_patterns = result.scalars().all()

    pattern_dicts = []
    for p in db_patterns:
        pattern_dicts.append({
            "id": p.id,
            "manufacturer": p.manufacturer,
            "boat_model": p.boat_model,
            "issue_category": p.issue_category,
            "zone_type": p.zone_type,
            "description": p.description,
            "report_count": p.report_count,
            "severity_mode": p.severity_mode,
            "typical_onset_years": p.typical_onset_years,
            "materials_involved": p.materials_involved,
            "construction_methods_involved": p.construction_methods_involved,
            "confidence": p.confidence,
            "source_report_ids": p.source_report_ids,
            "is_positive": p.is_positive,
        })

    negative = find_relevant_patterns(
        pattern_dicts,
        hull_material=hull_material,
        hull_construction=hull_construction,
        manufacturer=manufacturer,
        model=model,
        max_results=max_results,
        include_positive=False,
    )

    positive = find_relevant_patterns(
        pattern_dicts,
        hull_material=hull_material,
        hull_construction=hull_construction,
        manufacturer=manufacturer,
        model=model,
        max_results=max_results // 2,
        include_positive=True,
    )
    positive = [p for p in positive if p.get("is_positive")]

    return {"negative": negative, "positive": positive}
