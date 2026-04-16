# backend/app/api/routes/benchmarks.py
"""Public class benchmarks — aggregated from all layouts of a given boat class."""
from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.permissions import get_current_user
from app.db.database import get_db
from app.models.models import AnalysisResult, Layout, Project, User

router = APIRouter(tags=["benchmarks"])


def _polygon_area_sqm(polygon: list[list[float]]) -> float:
    """Shoelace formula, returns area in sqm."""
    n = len(polygon)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2e6


def _compute_stats(values: list[float]) -> dict:
    """Compute basic statistics for a list of values."""
    if not values:
        return {"mean": 0, "median": 0, "min": 0, "max": 0, "count": 0}
    values_sorted = sorted(values)
    n = len(values_sorted)
    mid = n // 2
    median = values_sorted[mid] if n % 2 else (values_sorted[mid - 1] + values_sorted[mid]) / 2
    return {
        "mean": round(sum(values) / n, 2),
        "median": round(median, 2),
        "min": round(min(values), 2),
        "max": round(max(values), 2),
        "count": n,
    }


@router.get("/class-benchmarks/{boat_class}")
async def get_class_benchmarks(
    boat_class: str,
    _user: User = Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    """Return aggregated benchmarks for a boat class from all stored layouts."""
    result = await db.execute(
        select(Project, Layout)
        .join(Layout, Layout.project_id == Project.id)
        .where(Project.boat_class == boat_class)
    )
    rows = result.all()

    if not rows:
        return {
            "boat_class": boat_class,
            "sample_size": 0,
            "metrics": {},
            "message": "Keine Daten für diese Bootsklasse vorhanden.",
        }

    passage_widths: list[float] = []
    deck_heights: list[float] = []
    zone_counts: list[int] = []
    total_areas: list[float] = []
    storage_ratios: list[float] = []
    cabin_counts: list[int] = []

    for project, layout in rows:
        zones = layout.zones or []
        passages = layout.passages or []

        zone_counts.append(len(zones))
        deck_heights.append(float(layout.deck_height_mm))

        for p in passages:
            if isinstance(p, dict) and "width_mm" in p:
                passage_widths.append(float(p["width_mm"]))

        total_area = 0.0
        storage_area = 0.0
        cabins = 0
        for z in zones:
            if not isinstance(z, dict):
                continue
            area = _polygon_area_sqm(z.get("polygon", []))
            total_area += area
            if z.get("zone_type") == "storage":
                storage_area += area
            if z.get("zone_type") == "cabin":
                cabins += 1

        total_areas.append(total_area)
        cabin_counts.append(cabins)
        if total_area > 0:
            storage_ratios.append(storage_area / total_area)

    # Fetch analysis scores
    score_result = await db.execute(
        select(AnalysisResult.module, AnalysisResult.overall_score)
        .join(Project, AnalysisResult.project_id == Project.id)
        .where(Project.boat_class == boat_class)
    )
    score_rows = score_result.all()
    scores_by_module: dict[str, list[float]] = {}
    for module, score in score_rows:
        scores_by_module.setdefault(module, []).append(float(score))

    return {
        "boat_class": boat_class,
        "sample_size": len(rows),
        "metrics": {
            "passage_width_mm": _compute_stats(passage_widths),
            "deck_height_mm": _compute_stats(deck_heights),
            "zone_count": _compute_stats([float(z) for z in zone_counts]),
            "total_area_sqm": _compute_stats(total_areas),
            "storage_ratio": _compute_stats(storage_ratios),
            "cabin_count": _compute_stats([float(c) for c in cabin_counts]),
        },
        "analysis_scores": {
            module: _compute_stats(scores)
            for module, scores in scores_by_module.items()
        },
    }
