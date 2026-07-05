import json
import logging
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.permissions import get_current_user
from app.db.database import get_db
from app.models.models import AnalysisResult, Layout, Project, User
from app.schemas.schemas import (
    AnalysisRequest,
    AnalysisResponse,
    DxfImportResponse,
    FullAnalysisRequest,
    LayoutCreate,
    LayoutResponse,
)
from app.services.analysis.ergonomics import run_ergonomics_analysis
from app.services.analysis.volume_storage import run_volume_storage_analysis
from app.services.analysis.emotional import run_emotional_analysis
from app.services.analysis.compliance import run_compliance_analysis
from app.services.analysis.production import run_production_analysis
from app.services.analysis.materials import run_materials_analysis
from app.services.analysis.structural import run_structural_analysis
from app.services.analysis.cost import run_cost_analysis
from app.services.analysis.service_patterns import run_service_patterns_analysis
from app.services.analysis.brand_dna import run_brand_dna_analysis
from app.services.analysis.market import run_market_analysis
from app.services.dxf.parser import parse_dxf
from sqlalchemy.orm import selectinload
from app.models.models import CostItem, ServiceReport, ZoneMaterial, BrandReferenceModel

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/projects/{project_id}", tags=["layouts"])

ANALYSIS_MODULES = {
    "ergonomics": run_ergonomics_analysis,
    "volume_storage": run_volume_storage_analysis,
    "emotional": run_emotional_analysis,
    "compliance": run_compliance_analysis,
    "production": run_production_analysis,
    "materials": run_materials_analysis,
    "structural": run_structural_analysis,
    "cost": run_cost_analysis,
    "service_patterns": run_service_patterns_analysis,
    "brand_dna": run_brand_dna_analysis,
    "market": run_market_analysis,
}


async def _get_project(project_id: UUID, user: User, db: AsyncSession) -> Project:
    result = await db.execute(
        select(Project).where(Project.id == project_id, Project.user_id == user.id)
    )
    project = result.scalar_one_or_none()
    if not project:
        raise HTTPException(status_code=404, detail="Projekt nicht gefunden")
    return project


@router.get("/layouts", response_model=list[LayoutResponse])
async def list_layouts(
    project_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await _get_project(project_id, _user, db)
    result = await db.execute(
        select(Layout).where(Layout.project_id == project_id).order_by(Layout.created_at.desc())
    )
    return result.scalars().all()


@router.post("/layouts", response_model=LayoutResponse, status_code=201)
async def create_layout(
    project_id: UUID,
    data: LayoutCreate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await _get_project(project_id, _user, db)
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
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await _get_project(project_id, _user, db)
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
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await _get_project(project_id, _user, db)

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
        logger.warning("DXF parse validation error: %s", e)
        raise HTTPException(status_code=400, detail="Ungültige DXF-Datei. Bitte Format und Layer prüfen.")

    return result


async def _load_materials_for_analysis(layout_id: UUID, db: AsyncSession) -> list[dict]:
    """Load zone_material assignments with eagerly-loaded material data."""
    result = await db.execute(
        select(ZoneMaterial)
        .where(ZoneMaterial.layout_id == layout_id)
        .options(selectinload(ZoneMaterial.material))
    )
    zone_mats = result.scalars().all()

    assembled = []
    for zm in zone_mats:
        material = zm.material
        if material:
            assembled.append({
                "zone_name": zm.zone_name,
                "surface_type": zm.surface_type,
                "area_sqm": zm.area_sqm,
                "material": {
                    "name": material.name,
                    "category": material.category,
                    "subcategory": material.subcategory,
                    "cost_per_unit": material.cost_per_unit,
                    "cost_unit": material.cost_unit,
                    "lifespan_years": material.lifespan_years,
                    "maintenance_interval_months": material.maintenance_interval_months,
                    "maintenance_cost_factor": material.maintenance_cost_factor,
                    "known_issues": material.known_issues or [],
                    "properties": material.properties or {},
                },
            })
    return assembled


async def _load_cost_items(layout_id: UUID, db: AsyncSession) -> list[dict]:
    """Load cost items for a layout."""
    result = await db.execute(
        select(CostItem).where(CostItem.layout_id == layout_id)
    )
    items = result.scalars().all()
    return [
        {
            "category": item.category,
            "subcategory": item.subcategory,
            "description": item.description,
            "quantity": item.quantity,
            "unit": item.unit,
            "unit_cost_eur": item.unit_cost_eur,
            "total_cost_eur": item.total_cost_eur,
            "zone_name": item.zone_name,
            "source": item.source,
        }
        for item in items
    ]


async def _load_service_reports(project_id: UUID, db: AsyncSession) -> list[dict]:
    """Load service reports for a project (or its boat class)."""
    result = await db.execute(
        select(ServiceReport).where(ServiceReport.project_id == project_id)
    )
    reports = result.scalars().all()
    return [
        {
            "report_type": r.report_type,
            "category": r.category,
            "zone_type": r.zone_type,
            "description": r.description,
            "severity": r.severity,
            "boat_age_months": r.boat_age_months,
            "materials_involved": r.materials_involved or [],
            "cost_eur": r.cost_eur,
        }
        for r in reports
    ]


async def _load_brand_references(boat_class: str, db: AsyncSession) -> list[dict]:
    """Load brand reference models for the same boat class."""
    result = await db.execute(
        select(BrandReferenceModel).where(BrandReferenceModel.boat_class == boat_class)
    )
    refs = result.scalars().all()
    return [
        {
            "features": ref.features or {},
            "materials": (ref.features or {}).get("material_palette", []),
            "style_tags": (ref.features or {}).get("interior_style_tags", []),
        }
        for ref in refs
    ]


async def _load_competitors(boat_class: str, length_m: float, db: AsyncSession) -> list[dict]:
    """Load competitor models for the same boat class within ±15% length."""
    from app.models.models import CompetitorModel

    result = await db.execute(
        select(CompetitorModel).where(CompetitorModel.boat_class == boat_class)
    )
    all_competitors = result.scalars().all()
    tolerance = 0.15
    filtered = [
        c for c in all_competitors
        if c.length_m is None or abs(c.length_m - length_m) / length_m <= tolerance
    ]
    return [
        {
            "key_metrics": c.key_metrics or {},
            "length_m": c.length_m,
            "price_range_eur": c.price_range_eur,
        }
        for c in filtered
    ]


async def _load_structural_items(layout_id: UUID, db: AsyncSession) -> list[dict]:
    """Load structural items for a layout."""
    from app.models.models import StructuralItem

    result = await db.execute(
        select(StructuralItem).where(StructuralItem.layout_id == layout_id)
    )
    items = result.scalars().all()
    return [
        {
            "name": item.name,
            "item_type": item.item_type,
            "zone_name": item.zone_name,
            "weight_kg": item.weight_kg,
            "position_x_mm": item.position_x_mm,
            "position_y_mm": item.position_y_mm,
            "position_z_mm": item.position_z_mm,
            "dimensions": item.dimensions,
            "properties": item.properties,
        }
        for item in items
    ]


@router.post("/analyze", response_model=AnalysisResponse, status_code=201)
async def run_analysis(
    project_id: UUID,
    data: AnalysisRequest,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    project = await _get_project(project_id, _user, db)

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

    # Load extra data for modules that need it
    extra_kwargs: dict = {}
    if data.module == "materials":
        extra_kwargs["materials"] = await _load_materials_for_analysis(data.layout_id, db)
    elif data.module == "cost":
        extra_kwargs["cost_items"] = await _load_cost_items(data.layout_id, db)
        extra_kwargs["boat_length_m"] = project.length_m
    elif data.module == "service_patterns":
        extra_kwargs["service_reports"] = await _load_service_reports(project_id, db)
    elif data.module == "brand_dna":
        extra_kwargs["brand_references"] = await _load_brand_references(project.boat_class, db)
    elif data.module == "market":
        extra_kwargs["competitors"] = await _load_competitors(project.boat_class, project.length_m, db)
        extra_kwargs["boat_length_m"] = project.length_m

    analysis_fn = ANALYSIS_MODULES[data.module]
    analysis_result = analysis_fn(
        zones, passages, project.boat_class,
        config_overrides=data.config_overrides,
        **extra_kwargs,
    )

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
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await _get_project(project_id, _user, db)
    query = select(AnalysisResult).where(AnalysisResult.project_id == project_id)
    if module:
        query = query.where(AnalysisResult.module == module)
    query = query.order_by(AnalysisResult.created_at.desc())
    result = await db.execute(query)
    return result.scalars().all()


@router.post("/full-analysis", status_code=201)
async def run_full_analysis_endpoint(
    project_id: UUID,
    data: FullAnalysisRequest,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Run all applicable analysis modules on a layout."""
    from app.services.analysis.orchestrator import run_full_analysis, AnalysisContext

    project = await _get_project(project_id, _user, db)

    result = await db.execute(
        select(Layout).where(
            Layout.id == data.layout_id, Layout.project_id == project_id
        )
    )
    layout = result.scalar_one_or_none()
    if not layout:
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")

    # Load all supporting data in parallel-ish fashion
    zone_materials = await _load_materials_for_analysis(data.layout_id, db)
    structural_items = await _load_structural_items(data.layout_id, db)
    cost_items = await _load_cost_items(data.layout_id, db)
    service_reports = await _load_service_reports(project_id, db)
    brand_refs = await _load_brand_references(project.boat_class, db)
    competitors = await _load_competitors(
        project.boat_class, project.length_m, db
    )

    context = AnalysisContext(
        zones=layout.zones or [],
        passages=layout.passages or [],
        boat_class=project.boat_class,
        # Enforce the caller's real subscription tier server-side. Without this
        # the context defaulted to "pro", so free-tier users received every
        # paid Level-2 module (paywall bypass).
        tier=_user.tier,
        length_m=project.length_m,
        beam_m=project.beam_m,
        deck_height_mm=layout.deck_height_mm or 2100,
        config_overrides=data.config_overrides,
        zone_materials=zone_materials,
        structural_items=structural_items,
        cost_items=cost_items,
        service_reports=service_reports,
        brand_references=brand_refs,
        competitors=competitors,
    )

    analysis_result = await run_full_analysis(context)

    # Store individual module results in DB
    for module_name, module_result in analysis_result["modules"].items():
        db_result = AnalysisResult(
            project_id=project_id,
            layout_id=data.layout_id,
            module=module_name,
            overall_score=module_result.get("overall_score", 0),
            sub_scores=module_result.get("sub_scores", {}),
            warnings=module_result.get("warnings", []),
            suggestions=module_result.get("suggestions", []),
            metrics=module_result.get("metrics", {}),
            config_used=module_result.get("config_used", {}),
        )
        db.add(db_result)

    await db.commit()

    return analysis_result
