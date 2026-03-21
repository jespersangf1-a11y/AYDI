"""Full analysis orchestrator -- runs all applicable modules in dependency order."""
import asyncio
import logging
from datetime import datetime, timezone
from dataclasses import dataclass, field

logger = logging.getLogger(__name__)


@dataclass
class AnalysisContext:
    """All data needed by analysis modules."""

    zones: list[dict]
    passages: list[dict]
    boat_class: str
    length_m: float = 0.0
    beam_m: float = 0.0
    deck_height_mm: int = 2100
    config_overrides: dict | None = None
    # Optional data for specific modules
    zone_materials: list[dict] = field(default_factory=list)
    structural_items: list[dict] = field(default_factory=list)
    cost_items: list[dict] = field(default_factory=list)
    service_reports: list[dict] = field(default_factory=list)
    brand_references: list[dict] = field(default_factory=list)
    competitors: list[dict] = field(default_factory=list)
    community_patterns: list[dict] = field(default_factory=list)
    # Results from previous tiers (populated during execution)
    module_results: dict[str, dict] = field(default_factory=dict)


# Execution tiers -- modules in same tier can run in parallel
EXECUTION_TIERS: list[list[str]] = [
    # Tier 1: Independent core modules
    ["ergonomics", "volume_storage", "emotional", "compliance", "community"],
    # Tier 2: Independent but may use optional data
    ["production", "materials", "structural"],
    # Tier 3: Depends on tier 1+2 results
    ["cost"],
    # Tier 4: Cross-referencing modules
    ["service_patterns", "brand_dna", "market"],
]

# All module names across all tiers
ALL_MODULE_NAMES: set[str] = {m for tier in EXECUTION_TIERS for m in tier}


def _get_module_runners() -> dict:
    """Lazy import of all module runner functions.

    Imports are deferred to avoid circular-import issues and to allow
    the orchestrator module to be imported cheaply in tests.
    """
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
    from app.services.analysis.community import run_community_analysis

    return {
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


async def run_full_analysis(
    context: AnalysisContext,
    module_runners: dict | None = None,
    confidence_threshold: float = 0.7,
) -> dict:
    """Execute all applicable modules in dependency order.

    Args:
        context: All layout/project data needed by the modules.
        module_runners: Optional dict of module_name -> callable for testing.
            When *None* the real module functions are imported.
        confidence_threshold: Threshold for overall confidence determination.
            Defaults to 0.7.

    Returns:
        Dict with per-module results, overall score, and metadata.
    """
    if module_runners is None:
        module_runners = _get_module_runners()

    results: dict[str, dict] = {}
    skipped: dict[str, str] = {}
    errors: dict[str, str] = {}

    for tier_idx, tier_modules in enumerate(EXECUTION_TIERS):
        tasks: list = []
        module_names: list[str] = []

        for module_name in tier_modules:
            runner = module_runners.get(module_name)
            if runner is None:
                skipped[module_name] = "Modul nicht gefunden"
                continue
            module_names.append(module_name)
            tasks.append(
                _run_single_module(module_name, runner, context)
            )

        if tasks:
            tier_results = await asyncio.gather(*tasks, return_exceptions=True)

            for name, result in zip(module_names, tier_results):
                if isinstance(result, Exception):
                    logger.error("Module %s failed: %s", name, result)
                    errors[name] = {"error": str(result), "type": type(result).__name__}
                elif isinstance(result, dict) and result.get("available") is False:
                    skipped[name] = result.get("reason", "Nicht verfuegbar")
                elif isinstance(result, dict):
                    results[name] = result
                    # Store in context so later tiers can reference earlier results
                    context.module_results[name] = result

    # Compute overall weighted score
    overall = _compute_overall_score(results, context.boat_class, confidence_threshold)

    return {
        "modules": results,
        "skipped": skipped,
        "errors": errors,
        "overall_score": overall["score"],
        "overall_confidence": overall["confidence"],
        "module_count": len(results),
        "skipped_count": len(skipped),
        "error_count": len(errors),
        "executed_at": datetime.now(timezone.utc).isoformat(),
    }


def _build_module_kwargs(name: str, context: AnalysisContext) -> dict:
    """Build extra keyword arguments for a specific module runner."""
    kwargs: dict = {}

    if name == "materials":
        kwargs["materials"] = context.zone_materials
    elif name == "cost":
        kwargs["cost_items"] = context.cost_items
        kwargs["boat_length_m"] = context.length_m
    elif name == "service_patterns":
        kwargs["service_reports"] = context.service_reports
    elif name == "brand_dna":
        kwargs["brand_references"] = context.brand_references
    elif name == "market":
        kwargs["competitors"] = context.competitors
        kwargs["boat_length_m"] = context.length_m
        # Pass estimated cost from the cost module if it ran earlier
        cost_result = context.module_results.get("cost")
        if cost_result:
            total = cost_result.get("metrics", {}).get("total_estimated_cost_eur")
            if total is not None:
                kwargs["estimated_cost"] = total
    elif name == "community":
        kwargs["community_patterns"] = context.community_patterns

    return kwargs


async def _run_single_module(
    name: str,
    runner,
    context: AnalysisContext,
) -> dict:
    """Run a single analysis module with appropriate kwargs.

    The module runners are synchronous pure functions, so they are
    dispatched to a thread-pool executor to avoid blocking the event loop.
    """
    kwargs = _build_module_kwargs(name, context)

    loop = asyncio.get_event_loop()
    result = await loop.run_in_executor(
        None,
        lambda: runner(
            context.zones,
            context.passages,
            context.boat_class,
            context.config_overrides,
            **kwargs,
        ),
    )
    return result


# ---------------------------------------------------------------------------
# Overall score computation
# ---------------------------------------------------------------------------

# Module weights for computing overall score per boat class
OVERALL_WEIGHTS: dict[str, dict[str, float]] = {
    "small_sail": {
        "ergonomics": 0.15,
        "volume_storage": 0.15,
        "emotional": 0.10,
        "compliance": 0.15,
        "production": 0.10,
        "materials": 0.10,
        "structural": 0.10,
        "cost": 0.10,
        "community": 0.05,
    },
    "cruising_sail": {
        "ergonomics": 0.10,
        "volume_storage": 0.15,
        "emotional": 0.15,
        "compliance": 0.10,
        "production": 0.10,
        "materials": 0.10,
        "structural": 0.10,
        "cost": 0.10,
        "brand_dna": 0.05,
        "community": 0.05,
    },
    "large_motor": {
        "ergonomics": 0.10,
        "volume_storage": 0.10,
        "emotional": 0.15,
        "compliance": 0.10,
        "production": 0.10,
        "materials": 0.15,
        "structural": 0.10,
        "cost": 0.05,
        "brand_dna": 0.05,
        "market": 0.05,
        "community": 0.05,
    },
    "superyacht": {
        "ergonomics": 0.10,
        "volume_storage": 0.05,
        "emotional": 0.20,
        "compliance": 0.10,
        "production": 0.10,
        "materials": 0.15,
        "structural": 0.05,
        "cost": 0.05,
        "brand_dna": 0.10,
        "market": 0.05,
        "community": 0.05,
    },
}


def _compute_overall_score(results: dict[str, dict], boat_class: str, confidence_threshold: float = 0.7) -> dict:
    """Compute weighted overall score from module results.

    Weights are normalised by the sum of weights for modules that actually
    produced a score, so skipped/failed modules do not drag the result down.

    Args:
        results: Dict of module name to result dict.
        boat_class: Boat class for weight lookup.
        confidence_threshold: Threshold for determining overall confidence
            from measured module count ratio. Defaults to 0.7.
    """
    weights = OVERALL_WEIGHTS.get(boat_class, OVERALL_WEIGHTS["cruising_sail"])

    total_weight = 0.0
    weighted_sum = 0.0

    for module, result in results.items():
        score = result.get("overall_score")
        if score is None:
            continue
        w = weights.get(module, 0.0)
        if w > 0:
            weighted_sum += score * w
            total_weight += w

    if total_weight == 0:
        return {"score": None, "confidence": "insufficient"}

    # Normalise by actual weights used (in case some modules were skipped)
    overall = weighted_sum / total_weight

    # Confidence: if most modules are "measured" / "calculated", overall is too
    confidences = [r.get("confidence", "estimated") for r in results.values()]
    measured_count = sum(
        1 for c in confidences if c in ("measured", "calculated")
    )
    if measured_count >= len(confidences) * confidence_threshold:
        confidence = "measured"
    elif measured_count > 0:
        confidence = "calculated"
    else:
        confidence = "estimated"

    return {"score": round(overall, 1), "confidence": confidence}
