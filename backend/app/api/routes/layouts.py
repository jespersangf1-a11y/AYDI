import json
import logging
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Form
from sqlalchemy import func, select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.permissions import effective_tier, get_accessible_project, get_current_user
from app.db.database import get_db
from app.models.models import AnalysisResult, AnalysisRun, Layout, LayoutVersion, Project, User
from app.schemas.schemas import (
    AnalysisRequest,
    AnalysisResponse,
    AnalysisRunResponse,
    DxfImportResponse,
    FullAnalysisRequest,
    LayoutCreate,
    LayoutResponse,
    LayoutUpdate,
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

from app.services.analysis.community import run_community_analysis

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
    "community": run_community_analysis,
}


async def _load_community_patterns(
    db: AsyncSession,
    manufacturer: str | None = None,
    model: str | None = None,
) -> list[dict]:
    """Load community patterns relevance-matched to a boat identity.

    IMPORTANT: run_community_analysis does NO matching of its own — feeding
    it the whole DB would score/warn this boat with problems of FOREIGN
    manufacturers as "documented". Without an identity we therefore return []
    and the module honestly reports "Keine Community-Daten verfügbar."
    (`Project` currently has no manufacturer/model fields — once they exist,
    passing them here activates Level-2 community analysis.)
    """
    if not manufacturer and not model:
        return []
    try:
        from app.models.models import CommunityPattern
        from app.services.community.engine import find_relevant_patterns

        result = await db.execute(select(CommunityPattern))
        pattern_dicts = [
            {
                "id": p.id,
                "manufacturer": p.manufacturer,
                "boat_model": p.boat_model,
                "issue_category": p.issue_category,
                "category": p.issue_category,
                "zone_type": p.zone_type,
                "description": p.description,
                "report_count": p.report_count,
                "severity_mode": p.severity_mode,
                "severity": p.severity_mode,
                "typical_onset_years": p.typical_onset_years,
                "materials_involved": p.materials_involved,
                "construction_methods_involved": p.construction_methods_involved,
                "confidence": p.confidence,
                "is_positive": p.is_positive,
            }
            for p in result.scalars().all()
        ]
        matched = find_relevant_patterns(
            pattern_dicts,
            manufacturer=manufacturer,
            model=model,
            include_positive=True,
        )
        # Identity-level matches only (>= 0.8) — the zone_category fallback
        # (0.3) would attribute foreign manufacturers' problems to this boat.
        return [p for p in matched if p.get("relevance", 0.0) >= 0.8]
    except Exception:
        logger.exception("Loading community patterns failed; continuing without")
        return []


async def _get_project(
    project_id: UUID, user: User, db: AsyncSession, min_role: str = "editor"
) -> Project:
    """Access-checked fetch: owner or shared member with >= min_role
    (pillar 4, stage 1 — see core.permissions.get_accessible_project)."""
    return await get_accessible_project(project_id, user, db, min_role)


@router.get("/layouts", response_model=list[LayoutResponse])
async def list_layouts(
    project_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await _get_project(project_id, _user, db, min_role="viewer")
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


@router.patch("/layouts/{layout_id}", response_model=LayoutResponse)
async def update_layout(
    project_id: UUID,
    layout_id: UUID,
    data: LayoutUpdate,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Update a layout (pillar 3: owner refit loop).

    Layouts were previously immutable — no update endpoint existed, so the
    edit → re-analyze → compare loop was impossible. Every applied update
    auto-snapshots the PREVIOUS state as a LayoutVersion first, so edits are
    never destructive and version diff / restore always has a base.
    """
    await _get_project(project_id, _user, db)
    # Row lock serializes concurrent PATCHes (and version numbering) on the
    # same layout — without it, two parallel edits could snapshot the same
    # base state and silently lose one applied change. SQLAlchemy's SQLite
    # dialect ignores FOR UPDATE (single-writer anyway); PostgreSQL locks.
    result = await db.execute(
        select(Layout)
        .where(Layout.id == layout_id, Layout.project_id == project_id)
        .with_for_update()
    )
    layout = result.scalar_one_or_none()
    if not layout:
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")

    changed_fields = data.model_dump(
        exclude_unset=True, exclude={"change_summary", "zone_renames"}
    )
    # Explicit nulls would pass the "any changes?" gate but be applied by
    # nothing — creating phantom versions while lying to the client that the
    # field was cleared. All updatable columns are non-nullable: reject.
    null_fields = sorted(k for k, v in changed_fields.items() if v is None)
    if null_fields:
        raise HTTPException(
            status_code=422,
            detail=f"null ist für diese Felder nicht erlaubt: {', '.join(null_fields)}",
        )
    if not changed_fields:
        raise HTTPException(
            status_code=422,
            detail="Keine Änderungen angegeben (name, version, zones, passages oder deck_height_mm).",
        )

    # Auto-snapshot the CURRENT state (geometry AND meta) before applying
    max_result = await db.execute(
        select(func.max(LayoutVersion.version_number)).where(
            LayoutVersion.layout_id == layout_id
        )
    )
    next_version_number = (max_result.scalar_one_or_none() or 0) + 1
    snapshot = LayoutVersion(
        layout_id=layout_id,
        version_number=next_version_number,
        zones_snapshot=layout.zones or [],
        passages_snapshot=layout.passages or [],
        layout_meta_snapshot={
            "name": layout.name,
            "version": layout.version,
            "deck_height_mm": layout.deck_height_mm,
        },
        change_summary=(
            f"Auto-Snapshot vor Änderung: {data.change_summary}"
            if data.change_summary
            else "Auto-Snapshot vor Layout-Änderung"
        ),
        changed_by=_user.email,
    )
    db.add(snapshot)

    # Apply exactly the fields that passed the gate (model_dump already
    # serialized nested zone/passage models to plain dicts).
    for field_name, value in changed_fields.items():
        setattr(layout, field_name, value)

    # Cascade zone renames to name-referencing rows (materials, structural
    # items, cost items) — otherwise a rename silently orphans them and the
    # next analysis drops their weights/costs without a trace.
    if data.zone_renames:
        from sqlalchemy import update as sa_update
        from app.models.models import CostItem, StructuralItem, ZoneMaterial

        for old_name, new_name in data.zone_renames.items():
            if not new_name or old_name == new_name:
                continue
            for model in (ZoneMaterial, StructuralItem, CostItem):
                await db.execute(
                    sa_update(model)
                    .where(
                        model.layout_id == layout_id,
                        model.zone_name == old_name,
                    )
                    .values(zone_name=new_name)
                )

    try:
        await db.commit()
    except IntegrityError:
        await db.rollback()
        raise HTTPException(
            status_code=409,
            detail=(
                "Gleichzeitige Änderung erkannt (Versionsnummern-Konflikt) — "
                "bitte erneut versuchen."
            ),
        )
    await db.refresh(layout)
    return layout


@router.get("/layouts/{layout_id}", response_model=LayoutResponse)
async def get_layout(
    project_id: UUID,
    layout_id: UUID,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    await _get_project(project_id, _user, db, min_role="viewer")
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

    # Validate the extension BEFORE buffering the whole file, and bound the read
    # so an oversized upload cannot exhaust memory before any check runs.
    if not file.filename or not file.filename.lower().endswith(".dxf"):
        raise HTTPException(status_code=400, detail="Nur DXF-Dateien werden unterstützt")
    _MAX_DXF_BYTES = 25 * 1024 * 1024  # 25 MB
    content = await file.read(_MAX_DXF_BYTES + 1)
    if len(content) > _MAX_DXF_BYTES:
        raise HTTPException(
            status_code=413,
            detail=f"Datei zu gross. Maximal {_MAX_DXF_BYTES // (1024 * 1024)} MB erlaubt.",
        )
    if not content:
        raise HTTPException(status_code=400, detail="Leere Datei hochgeladen.")

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


async def _load_brand_references(boat_class: str, user, db: AsyncSession) -> list[dict]:
    """Load brand reference models for the same boat class — filtered to rows
    the caller may SEE (pillar 4, stage 2). The brand_dna module echoes
    reference-derived content (topology gaps, proportion signatures) back into
    its warnings, so loading foreign org rows here would leak private brand DNA
    that org-scoping exists to protect. Same predicate as the CRUD endpoints."""
    from app.core.brand_visibility import can_see_brand_ref, get_my_org_ids

    result = await db.execute(
        select(BrandReferenceModel).where(BrandReferenceModel.boat_class == boat_class)
    )
    refs = result.scalars().all()
    my_org_ids = await get_my_org_ids(user, db)
    return [
        {
            "features": ref.features or {},
            "materials": (ref.features or {}).get("material_palette", []),
            "style_tags": (ref.features or {}).get("interior_style_tags", []),
        }
        for ref in refs
        if can_see_brand_ref(ref, user, my_org_ids)
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

    # Server-side tier gating at the route boundary (CLAUDE.md: "Use
    # require_feature / require_module at route boundaries"). Without this,
    # FREE users could run every paid Level-2 module individually even though
    # /full-analysis gates them — a paywall bypass.
    from app.core.subscription import get_allowed_modules

    _eff_tier = effective_tier(_user)
    if data.module not in get_allowed_modules(_eff_tier):
        raise HTTPException(
            status_code=403,
            detail=(
                f"Modul '{data.module}' ist im Tarif '{_eff_tier}' nicht "
                "enthalten — Upgrade auf PRO erforderlich."
            ),
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
        extra_kwargs["brand_references"] = await _load_brand_references(project.boat_class, _user, db)
    elif data.module == "market":
        extra_kwargs["competitors"] = await _load_competitors(project.boat_class, project.length_m, db)
        extra_kwargs["boat_length_m"] = project.length_m
    elif data.module == "structural":
        extra_kwargs["structural_items"] = await _load_structural_items(data.layout_id, db)
    elif data.module == "community":
        extra_kwargs["community_patterns"] = await _load_community_patterns(db)

    analysis_fn = ANALYSIS_MODULES[data.module]
    analysis_result = analysis_fn(
        zones, passages, project.boat_class,
        config_overrides=data.config_overrides,
        **extra_kwargs,
    )

    # Module skip contract: {"available": False, "reason": ...} means the
    # module cannot produce a reliable result. Surface that honestly instead
    # of crashing on the missing overall_score (latent KeyError) or storing
    # a fabricated 0-score row.
    if analysis_result.get("available") is False:
        raise HTTPException(
            status_code=422,
            detail=(
                f"Modul '{data.module}' nicht auswertbar: "
                f"{analysis_result.get('reason', 'Keine ausreichenden Daten.')}"
            ),
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
    await _get_project(project_id, _user, db, min_role="viewer")
    query = select(AnalysisResult).where(AnalysisResult.project_id == project_id)
    if module:
        query = query.where(AnalysisResult.module == module)
    query = query.order_by(AnalysisResult.created_at.desc())
    result = await db.execute(query)
    return result.scalars().all()


@router.get("/analysis-runs", response_model=list[AnalysisRunResponse])
async def list_analysis_runs(
    project_id: UUID,
    layout_id: UUID | None = None,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """List full-analysis run headers for a project (H-3), newest first.

    Each run's per-module results are retrievable via GET /analyses?run_id=...
    (filtered client-side by the returned run id).
    """
    await _get_project(project_id, _user, db, min_role="viewer")
    query = select(AnalysisRun).where(AnalysisRun.project_id == project_id)
    if layout_id:
        query = query.where(AnalysisRun.layout_id == layout_id)
    query = query.order_by(AnalysisRun.created_at.desc())
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
    brand_refs = await _load_brand_references(project.boat_class, _user, db)
    competitors = await _load_competitors(
        project.boat_class, project.length_m, db
    )
    community_patterns = await _load_community_patterns(db)

    context = AnalysisContext(
        zones=layout.zones or [],
        passages=layout.passages or [],
        boat_class=project.boat_class,
        # Enforce the caller's real subscription tier server-side. Without this
        # the context defaulted to "pro", so free-tier users received every
        # paid Level-2 module (paywall bypass). Effective tier includes org.
        tier=effective_tier(_user),
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
        community_patterns=community_patterns,
    )

    analysis_result = await run_full_analysis(context)

    # Persist a run header (H-3) so this Vollanalyse stays reconstructable —
    # overall score/confidence and which modules ran — then link every module
    # row to it via run_id.
    run = AnalysisRun(
        project_id=project_id,
        layout_id=data.layout_id,
        overall_score=analysis_result.get("overall_score"),
        overall_confidence=analysis_result.get("overall_confidence"),
        module_count=analysis_result.get("module_count", 0),
        skipped_count=analysis_result.get("skipped_count", 0),
        error_count=analysis_result.get("error_count", 0),
        tier=analysis_result.get("tier"),
    )
    db.add(run)
    await db.flush()  # obtain run.id before linking results

    for module_name, module_result in analysis_result["modules"].items():
        db_result = AnalysisResult(
            project_id=project_id,
            layout_id=data.layout_id,
            run_id=run.id,
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

    analysis_result["run_id"] = str(run.id)
    return analysis_result
