"""Report generation endpoints for AYDI analysis reports."""
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.permissions import get_current_user
from app.db.database import get_db
from app.models.models import AnalysisResult, Layout, Project, Report, User
from app.schemas.schemas import ReportRequest, ReportResponse
from app.services.reports.pdf_generator import generate_report

router = APIRouter(prefix="/projects/{project_id}", tags=["reports"])


async def _get_project(project_id: UUID, user: User, db: AsyncSession) -> Project:
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.user_id == user.id)
    )
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="Projekt nicht gefunden")
    return project


@router.post("/reports", response_model=ReportResponse, status_code=201)
async def create_report(
    project_id: UUID,
    data: ReportRequest,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> Report:
    """
    Generate a structured report for a layout by combining all available analysis results.

    report_type: "full" | "summary" | "executive"
    """
    project = await _get_project(project_id, _user, db)

    # Verify layout belongs to this project
    layout_result = await db.execute(
        select(Layout).where(Layout.id == data.layout_id, Layout.project_id == project_id)
    )
    layout = layout_result.scalar_one_or_none()
    if not layout:
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")

    # Load all analysis results for this layout
    analyses_result = await db.execute(
        select(AnalysisResult)
        .where(
            AnalysisResult.layout_id == data.layout_id,
            AnalysisResult.project_id == project_id,
        )
        .order_by(AnalysisResult.created_at.desc())
    )
    all_analyses = analyses_result.scalars().all()

    # Deduplicate: keep only the most recent result per module
    seen_modules: set[str] = set()
    deduplicated: list[AnalysisResult] = []
    for ar in all_analyses:
        if ar.module not in seen_modules:
            seen_modules.add(ar.module)
            deduplicated.append(ar)

    if not deduplicated:
        raise HTTPException(status_code=422, detail="Keine Analyseergebnisse vorhanden")

    # Convert ORM objects to plain dicts for the generator
    project_dict = {
        "name": project.name,
        "description": project.description,
        "boat_class": project.boat_class,
        "length_m": project.length_m,
        "beam_m": project.beam_m,
        "status": project.status,
    }
    layout_dict = {
        "name": layout.name,
        "version": layout.version,
        "deck_height_mm": layout.deck_height_mm,
    }
    analysis_dicts = [
        {
            "module": ar.module,
            "overall_score": ar.overall_score,
            "sub_scores": ar.sub_scores or {},
            "warnings": ar.warnings or [],
            "suggestions": ar.suggestions or [],
            "metrics": ar.metrics or {},
            "config_used": ar.config_used or {},
        }
        for ar in deduplicated
    ]

    report_data = generate_report(
        project=project_dict,
        layout=layout_dict,
        analysis_results=analysis_dicts,
        report_type=data.report_type,
    )

    db_report = Report(
        project_id=project_id,
        layout_id=data.layout_id,
        report_type=data.report_type,
        report_data=report_data,
    )
    db.add(db_report)
    await db.commit()
    await db.refresh(db_report)
    return db_report


@router.get("/reports", response_model=list[ReportResponse])
async def list_reports(
    project_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> list[Report]:
    """List all generated reports for a project, most recent first."""
    await _get_project(project_id, _user, db)
    result = await db.execute(
        select(Report)
        .where(Report.project_id == project_id)
        .order_by(Report.created_at.desc())
    )
    return result.scalars().all()


@router.get("/reports/{report_id}", response_model=ReportResponse)
async def get_report(
    project_id: UUID,
    report_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
) -> Report:
    """Get a specific report by ID."""
    await _get_project(project_id, _user, db)
    result = await db.execute(
        select(Report).where(Report.id == report_id, Report.project_id == project_id)
    )
    report = result.scalar_one_or_none()
    if not report:
        raise HTTPException(status_code=404, detail="Bericht nicht gefunden")
    return report
