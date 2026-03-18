import json
import logging
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.models import AnalysisResult, Layout, Project
from app.schemas.schemas import (
    AnalysisRequest,
    AnalysisResponse,
    DxfImportResponse,
    LayoutCreate,
    LayoutResponse,
)
from app.services.analysis.ergonomics import run_ergonomics_analysis
from app.services.analysis.volume_storage import run_volume_storage_analysis
from app.services.analysis.emotional import run_emotional_analysis
from app.services.analysis.compliance import run_compliance_analysis
from app.services.analysis.production import run_production_analysis
from app.services.dxf.parser import parse_dxf

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/projects/{project_id}", tags=["layouts"])

ANALYSIS_MODULES = {
    "ergonomics": run_ergonomics_analysis,
    "volume_storage": run_volume_storage_analysis,
    "emotional": run_emotional_analysis,
    "compliance": run_compliance_analysis,
    "production": run_production_analysis,
}


async def _get_project(project_id: UUID, db: AsyncSession) -> Project:
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="Projekt nicht gefunden")
    return project


@router.get("/layouts", response_model=list[LayoutResponse])
async def list_layouts(
    project_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    await _get_project(project_id, db)
    result = await db.execute(
        select(Layout).where(Layout.project_id == project_id).order_by(Layout.created_at.desc())
    )
    return result.scalars().all()


@router.post("/layouts", response_model=LayoutResponse, status_code=201)
async def create_layout(
    project_id: UUID,
    data: LayoutCreate,
    db: AsyncSession = Depends(get_db),
):
    await _get_project(project_id, db)
    layout = Layout(
        project_id=project_id,
        name=data.name,
        version=data.version,
        file_type="json",
        zones=[z.model_dump() for z in data.zones],
        passages=[p.model_dump() for p in data.passages],
        deck_height_mm=data.deck_height_mm,
    )
    db.add(layout)
    await db.commit()
    await db.refresh(layout)
    return layout


@router.get("/layouts/{layout_id}", response_model=LayoutResponse)
async def get_layout(
    project_id: UUID,
    layout_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    await _get_project(project_id, db)
    result = await db.execute(
        select(Layout).where(Layout.id == layout_id, Layout.project_id == project_id)
    )
    layout = result.scalar_one_or_none()
    if not layout:
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")
    return layout


@router.post("/layouts/import-dxf", response_model=DxfImportResponse)
async def import_dxf(
    project_id: UUID,
    file: UploadFile = File(...),
    name: str = Form(...),
    version: str = Form("v1.0"),
    layer_map: str | None = Form(None),
    db: AsyncSession = Depends(get_db),
):
    await _get_project(project_id, db)

    content = await file.read()
    if not file.filename or not file.filename.lower().endswith(".dxf"):
        raise HTTPException(status_code=400, detail="Nur DXF-Dateien werden unterstützt")

    custom_layer_map = None
    if layer_map:
        try:
            custom_layer_map = json.loads(layer_map)
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Ungültiges Layer-Mapping JSON")

    try:
        result = parse_dxf(content, layer_map=custom_layer_map)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    return result


@router.post("/analyze", response_model=AnalysisResponse, status_code=201)
async def run_analysis(
    project_id: UUID,
    data: AnalysisRequest,
    db: AsyncSession = Depends(get_db),
):
    project = await _get_project(project_id, db)

    if data.module not in ANALYSIS_MODULES:
        raise HTTPException(
            status_code=400,
            detail=f"Unbekanntes Analysemodul: {data.module}. Verfügbar: {list(ANALYSIS_MODULES.keys())}",
        )

    result = await db.execute(
        select(Layout).where(Layout.id == data.layout_id, Layout.project_id == project_id)
    )
    layout = result.scalar_one_or_none()
    if not layout:
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")

    zones = layout.zones or []
    passages = layout.passages or []

    analysis_fn = ANALYSIS_MODULES[data.module]
    analysis_result = analysis_fn(zones, passages, project.boat_class)

    db_result = AnalysisResult(
        project_id=project_id,
        layout_id=data.layout_id,
        module=data.module,
        overall_score=analysis_result["overall_score"],
        sub_scores=analysis_result["sub_scores"],
        warnings=analysis_result["warnings"],
        suggestions=analysis_result["suggestions"],
        metrics=analysis_result["metrics"],
        config_used=analysis_result["config_used"],
    )
    db.add(db_result)
    await db.commit()
    await db.refresh(db_result)
    return db_result


@router.get("/analyses", response_model=list[AnalysisResponse])
async def list_analyses(
    project_id: UUID,
    module: str | None = None,
    db: AsyncSession = Depends(get_db),
):
    await _get_project(project_id, db)
    query = select(AnalysisResult).where(AnalysisResult.project_id == project_id)
    if module:
        query = query.where(AnalysisResult.module == module)
    query = query.order_by(AnalysisResult.created_at.desc())
    result = await db.execute(query)
    return result.scalars().all()
