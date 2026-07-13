import logging
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.models import QuickAnalysisResult
from app.schemas.quick_analysis import PublicSpecs, QuickAnalysisResponse
from app.services.inference.layout_estimator import estimate_layout_from_specs

# Import available analysis modules
from app.services.analysis.ergonomics import run_ergonomics_analysis
from app.services.analysis.volume_storage import run_volume_storage_analysis
from app.services.analysis.emotional import run_emotional_analysis
from app.services.analysis.market import run_market_analysis

logger = logging.getLogger(__name__)

router = APIRouter(tags=["quick-analysis"])


# Modules available for Level 1 (estimated data)
LEVEL1_MODULES: dict = {
    "ergonomics": {
        "fn": run_ergonomics_analysis,
        "label": "Ergonomie",
    },
    "volume_storage": {
        "fn": run_volume_storage_analysis,
        "label": "Volumen & Stauraum",
    },
    "emotional": {
        "fn": run_emotional_analysis,
        "label": "Emotionales Design",
    },
    "market": {
        "fn": run_market_analysis,
        "label": "Markt & Wettbewerb",
        "needs_competitors": True,
    },
}

# Modules NOT available at Level 1
LEVEL2_ONLY_MODULES: dict = {
    "materials": "Materialdaten erforderlich (Level 2)",
    "structural": "Strukturdaten erforderlich (Level 2)",
    "cost": "Kostendaten erforderlich (Level 2)",
    "production": "CAD-Daten erforderlich (Level 2)",
    "compliance": "Detaillierte Layoutdaten erforderlich (Level 2)",
    "service_patterns": "Serviceberichte erforderlich (Level 2)",
    "brand_dna": "Referenzmodelle erforderlich (Level 2)",
}


def _count_specs_provided(specs: PublicSpecs) -> int:
    """Count how many fields the user actually supplied (required + optional)."""
    count = 2  # boat_class and length_m are always required
    optional_fields = [
        specs.beam_m, specs.draft_m, specs.displacement_kg,
        specs.cabin_count, specs.berth_count, specs.head_count,
        specs.cockpit_area_sqm, specs.salon_area_sqm, specs.pantry_type,
        specs.helm_position, specs.has_flybridge, specs.has_crew_quarters,
        specs.engine_hp, specs.engine_count, specs.fuel_capacity_l,
        specs.water_capacity_l, specs.sail_area_sqm, specs.max_speed_kn,
        specs.price_eur, specs.year, specs.brand, specs.model_name,
        specs.deck_height_mm, specs.storage_volume_l,
    ]
    count += sum(1 for f in optional_fields if f is not None)
    return count


def _extract_key_findings(warnings: list[dict], max_findings: int = 5) -> list[dict]:
    """Convert analysis warnings to key_findings format for the response."""
    return [
        {
            "finding": w.get("message", ""),
            "severity": w.get("severity", "info"),
        }
        for w in warnings[:max_findings]
    ]


def _generate_summary(boat_class: str, overall_score: float, module_results: dict) -> str:
    """Generate a German-language one-sentence summary of the overall result."""
    class_labels = {
        "small_sail": "Kleine Segelyacht",
        "cruising_sail": "Fahrtensegler",
        "large_motor": "Gro\u00dfe Motoryacht",
        "superyacht": "Superyacht",
    }
    class_label = class_labels.get(boat_class, boat_class)

    if overall_score >= 80:
        quality = "\u00dcberdurchschnittliches"
    elif overall_score >= 65:
        quality = "Solides"
    elif overall_score >= 50:
        quality = "Durchschnittliches"
    else:
        quality = "Verbesserungsw\u00fcrdiges"

    # Find the weakest available module for the summary hint
    weakest: str | None = None
    weakest_score = 101.0
    for name, result in module_results.items():
        if result.get("available") and result.get("score") is not None:
            if result["score"] < weakest_score:
                weakest_score = result["score"]
                weakest = name

    summary = f"{quality} {class_label}-Konzept"
    if weakest and weakest_score < 65:
        module_labels = {
            "ergonomics": "Ergonomie",
            "volume_storage": "Raumnutzung",
            "emotional": "Raumwirkung",
            "market": "Marktpositionierung",
        }
        summary += f" mit Optimierungspotenzial bei {module_labels.get(weakest, weakest)}"
    summary += "."
    return summary


def _build_upgrade_prompt() -> dict:
    """Build the standard upgrade prompt shown at the end of every Level 1 result."""
    return {
        "message": (
            f"Mit CAD-Daten und Materialwahl k\u00f6nnen {len(LEVEL2_ONLY_MODULES)} "
            "weitere Module ausgewertet werden."
        ),
        "additional_modules": [
            "Detaillierte Ergonomie",
            "Materialanalyse",
            "Kostenanalyse",
            "Strukturanalyse",
            "Produktionsfreundlichkeit",
            "Normenpr\u00fcfung",
            "Servicemuster",
            "Marken-DNA",
        ],
    }


@router.post("/quick-analysis", response_model=QuickAnalysisResponse, status_code=201)
async def create_quick_analysis(
    specs: PublicSpecs,
    db: AsyncSession = Depends(get_db),
):
    """Run Level 1 Schnellanalyse from public specifications.

    No authentication required. Generates an estimated layout from the provided
    specs, runs all Level 1 analysis modules against it, persists the result,
    and returns a structured response with module scores and an upgrade prompt.
    """
    # 1. Estimate layout from specs
    estimated = estimate_layout_from_specs(
        boat_class=specs.boat_class,
        length_m=specs.length_m,
        beam_m=specs.beam_m,
        cabin_count=specs.cabin_count,
        head_count=specs.head_count,
        cockpit_area_sqm=specs.cockpit_area_sqm,
        salon_area_sqm=specs.salon_area_sqm,
        deck_height_mm=specs.deck_height_mm,
        has_flybridge=specs.has_flybridge,
        has_crew_quarters=specs.has_crew_quarters,
        storage_volume_l=specs.storage_volume_l,
    )

    zones: list[dict] = estimated["zones"]
    passages: list[dict] = estimated["passages"]

    # 2. Run available Level 1 modules
    module_results: dict = {}
    available_scores: list[float] = []

    for module_name, module_info in LEVEL1_MODULES.items():
        try:
            extra_kwargs: dict = {}

            if module_info.get("needs_competitors"):
                from app.models.models import CompetitorModel

                comp_result = await db.execute(
                    select(CompetitorModel).where(CompetitorModel.boat_class == specs.boat_class)
                )
                competitors = comp_result.scalars().all()
                extra_kwargs["competitors"] = [
                    {
                        "key_metrics": c.key_metrics or {},
                        "length_m": c.length_m,
                        "price_range_eur": c.price_range_eur,
                    }
                    for c in competitors
                ]
                extra_kwargs["boat_length_m"] = specs.length_m
                if specs.price_eur is not None:
                    extra_kwargs["estimated_cost"] = specs.price_eur

            analysis_result = module_info["fn"](
                zones, passages, specs.boat_class,
                data_source="estimated",
                **extra_kwargs,
            )

            # Honour the module skip contract: a module that cannot produce a
            # reliable result returns {"available": False, ...}. Never turn that
            # (or a missing score) into a fabricated 50/100 "estimated" result
            # (Reliability rule: "never present uncertain results as facts").
            if analysis_result.get("available") is False:
                module_results[module_name] = {
                    "available": False,
                    "reason": analysis_result.get("reason", "Analyse nicht m\u00f6glich."),
                }
                continue
            if "overall_score" not in analysis_result:
                logger.warning(
                    "Quick-analysis module %s returned no overall_score; marking unavailable.",
                    module_name,
                )
                module_results[module_name] = {
                    "available": False,
                    "reason": "Kein Ergebnis (unerwartetes Modul-Format).",
                }
                continue

            score = float(analysis_result["overall_score"])
            available_scores.append(score)

            module_entry: dict = {
                "available": True,
                "score": round(score, 1),
                "confidence": "estimated",
                "key_findings": _extract_key_findings(analysis_result.get("warnings", [])),
            }

            if module_name == "market":
                metrics = analysis_result.get("metrics", {})
                module_entry["competitors_compared"] = metrics.get("competitors_analyzed", 0)
                module_entry["strengths"] = metrics.get("strengths", [])
                module_entry["weaknesses"] = metrics.get("weaknesses", [])

            module_results[module_name] = module_entry

        except Exception:
            logger.exception("Quick-analysis module %s failed", module_name)
            module_results[module_name] = {
                "available": False,
                "reason": "Analyse fehlgeschlagen.",
            }

    # 3. Mark Level 2-only modules as unavailable
    for module_name, reason in LEVEL2_ONLY_MODULES.items():
        module_results[module_name] = {"available": False, "reason": reason}

    # 4. Compute overall score
    overall_score = (
        round(sum(available_scores) / len(available_scores), 1)
        if available_scores
        else 50.0
    )

    # 5. Build and persist result
    db_result = QuickAnalysisResult(
        boat_class=specs.boat_class,
        length_m=specs.length_m,
        specs_input=specs.model_dump(),
        overall_score=overall_score,
        module_results=module_results,
        estimated_layout=estimated,
    )
    db.add(db_result)
    await db.commit()
    await db.refresh(db_result)

    return QuickAnalysisResponse(
        id=db_result.id,
        specs_provided=_count_specs_provided(specs),
        specs_inferred=estimated.get("specs_inferred", 0),
        overall_assessment={
            "score": overall_score,
            "confidence": "estimated",
            "summary": _generate_summary(specs.boat_class, overall_score, module_results),
        },
        modules=module_results,
        upgrade_prompt=_build_upgrade_prompt(),
        specs_used=specs.model_dump(),
        created_at=db_result.created_at,
    )


@router.get("/quick-analysis/{analysis_id}", response_model=QuickAnalysisResponse)
async def get_quick_analysis(
    analysis_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    """Retrieve a previously saved quick analysis result by ID."""
    db_result = await db.execute(
        select(QuickAnalysisResult).where(QuickAnalysisResult.id == analysis_id)
    )
    qa = db_result.scalar_one_or_none()
    if not qa:
        raise HTTPException(status_code=404, detail="Schnellanalyse nicht gefunden")

    estimated = qa.estimated_layout or {}

    return QuickAnalysisResponse(
        id=qa.id,
        specs_provided=_count_specs_provided(PublicSpecs(**qa.specs_input)),
        specs_inferred=estimated.get("specs_inferred", 0),
        overall_assessment={
            "score": qa.overall_score,
            "confidence": "estimated",
            "summary": _generate_summary(qa.boat_class, qa.overall_score, qa.module_results),
        },
        modules=qa.module_results,
        upgrade_prompt=_build_upgrade_prompt(),
        specs_used=qa.specs_input,
        created_at=qa.created_at,
    )
