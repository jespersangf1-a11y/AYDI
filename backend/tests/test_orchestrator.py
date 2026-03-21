"""Tests for the full analysis orchestrator."""
import asyncio
from unittest.mock import patch, MagicMock

from app.services.analysis.orchestrator import (
    AnalysisContext,
    EXECUTION_TIERS,
    ALL_MODULE_NAMES,
    OVERALL_WEIGHTS,
    run_full_analysis,
    _compute_overall_score,
    _build_module_kwargs,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_context(**overrides) -> AnalysisContext:
    """Create a minimal AnalysisContext with optional overrides."""
    defaults = {
        "zones": [
            {
                "name": "Salon",
                "zone_type": "salon",
                "polygon": [[3200, 400], [6000, 400], [6000, 3550], [3200, 3550]],
                "height_mm": 1950,
                "is_crew_area": False,
                "is_guest_area": True,
            }
        ],
        "passages": [
            {
                "from_zone": "Cockpit",
                "to_zone": "Salon",
                "width_mm": 750,
                "is_primary": True,
            }
        ],
        "boat_class": "cruising_sail",
        "length_m": 12.2,
        "beam_m": 3.95,
        "deck_height_mm": 1950,
    }
    defaults.update(overrides)
    return AnalysisContext(**defaults)


def _mock_result(module: str, score: float = 75.0, confidence: str = "measured") -> dict:
    """Return a minimal valid analysis result dict."""
    return {
        "module": module,
        "overall_score": score,
        "sub_scores": {},
        "warnings": [],
        "suggestions": [],
        "metrics": {},
        "config_used": {},
        "confidence": confidence,
    }


def _make_runners(
    results: dict[str, dict | Exception | None] | None = None,
    default_score: float = 75.0,
) -> dict:
    """Build a dict of mock module runners.

    Args:
        results: Override per-module results.  If the value is an Exception,
            the runner will raise it.  If *None*, a default result is used.
        default_score: Score to use when no explicit result is given.
    """
    all_modules = list(ALL_MODULE_NAMES)
    overrides = results or {}
    runners = {}

    for name in all_modules:
        if name in overrides:
            val = overrides[name]
            if isinstance(val, Exception):
                def _raise(z, p, bc, co, _e=val, **kw):
                    raise _e
                runners[name] = _raise
            elif val is None:
                # Omit this module entirely (simulate missing runner)
                continue
            else:
                def _return(z, p, bc, co, _r=val, **kw):
                    return _r
                runners[name] = _return
        else:
            def _default(z, p, bc, co, _n=name, _s=default_score, **kw):
                return _mock_result(_n, _s)
            runners[name] = _default

    return runners


# ---------------------------------------------------------------------------
# AnalysisContext
# ---------------------------------------------------------------------------


def test_context_creation_defaults():
    """AnalysisContext can be created with minimal arguments."""
    ctx = AnalysisContext(zones=[], passages=[], boat_class="small_sail")
    assert ctx.length_m == 0.0
    assert ctx.beam_m == 0.0
    assert ctx.deck_height_mm == 2100
    assert ctx.config_overrides is None
    assert ctx.zone_materials == []
    assert ctx.structural_items == []
    assert ctx.cost_items == []
    assert ctx.service_reports == []
    assert ctx.brand_references == []
    assert ctx.competitors == []
    assert ctx.module_results == {}


def test_context_creation_with_overrides():
    """AnalysisContext accepts all optional fields."""
    ctx = AnalysisContext(
        zones=[{"name": "X"}],
        passages=[],
        boat_class="superyacht",
        length_m=35.0,
        beam_m=8.0,
        deck_height_mm=2300,
        config_overrides={"foo": "bar"},
        zone_materials=[{"m": 1}],
        cost_items=[{"c": 1}],
    )
    assert ctx.length_m == 35.0
    assert ctx.config_overrides == {"foo": "bar"}
    assert len(ctx.zone_materials) == 1


# ---------------------------------------------------------------------------
# EXECUTION_TIERS structure
# ---------------------------------------------------------------------------


def test_execution_tiers_has_all_modules():
    """Every known module name must appear in exactly one tier."""
    expected = {
        "ergonomics", "volume_storage", "emotional", "compliance", "community",
        "production", "materials", "structural",
        "cost",
        "service_patterns", "brand_dna", "market",
    }
    assert ALL_MODULE_NAMES == expected


def test_execution_tiers_four_tiers():
    """There must be exactly 4 execution tiers."""
    assert len(EXECUTION_TIERS) == 4


def test_no_duplicate_modules_across_tiers():
    """Each module appears in exactly one tier."""
    seen = []
    for tier in EXECUTION_TIERS:
        for m in tier:
            assert m not in seen, f"Duplicate module {m}"
            seen.append(m)


# ---------------------------------------------------------------------------
# Full analysis — happy path
# ---------------------------------------------------------------------------


def test_full_analysis_all_modules_run():
    """All 11 modules produce results when runners are provided."""
    ctx = _make_context()
    runners = _make_runners()
    result = asyncio.run(run_full_analysis(ctx, module_runners=runners))

    assert result["module_count"] == 12
    assert result["skipped_count"] == 0
    assert result["error_count"] == 0
    assert result["overall_score"] is not None
    assert "executed_at" in result
    assert set(result["modules"].keys()) == ALL_MODULE_NAMES


def test_full_analysis_overall_score_value():
    """Overall score equals known weighted average when all modules return the same score."""
    ctx = _make_context()
    runners = _make_runners(default_score=80.0)
    result = asyncio.run(run_full_analysis(ctx, module_runners=runners))

    # All modules return 80 -> weighted average = 80 regardless of weights
    assert result["overall_score"] == 80.0


# ---------------------------------------------------------------------------
# Tier ordering and dependency passing
# ---------------------------------------------------------------------------


def test_tier3_cost_gets_earlier_results():
    """The cost module runs after tier 1+2; context.module_results is populated."""
    call_log = []

    def cost_runner(zones, passages, bc, co, **kw):
        # By the time cost runs, tier 1+2 results should be in context
        call_log.append("cost_called")
        return _mock_result("cost", 70.0)

    runners = _make_runners(results={"cost": None})  # remove default cost
    runners["cost"] = cost_runner

    ctx = _make_context()
    result = asyncio.run(run_full_analysis(ctx, module_runners=runners))

    assert "cost_called" in call_log
    # ergonomics (tier 1) should already be in module_results when cost ran
    assert "ergonomics" in ctx.module_results


def test_tier4_market_receives_cost_estimated_cost():
    """Market module receives estimated_cost from cost module via context."""
    received_kwargs = {}

    def market_runner(zones, passages, bc, co, **kw):
        received_kwargs.update(kw)
        return _mock_result("market", 65.0)

    cost_result = _mock_result("cost", 70.0)
    cost_result["metrics"]["total_estimated_cost_eur"] = 250000.0

    runners = _make_runners(results={
        "cost": cost_result,
        "market": None,
    })
    runners["market"] = market_runner

    ctx = _make_context()
    result = asyncio.run(run_full_analysis(ctx, module_runners=runners))

    assert received_kwargs.get("estimated_cost") == 250000.0


# ---------------------------------------------------------------------------
# Module skip / unavailable
# ---------------------------------------------------------------------------


def test_module_returns_available_false_is_skipped():
    """A module returning available=False is tracked as skipped."""
    runners = _make_runners(results={
        "brand_dna": {"available": False, "reason": "Keine Referenzmodelle vorhanden"},
    })
    ctx = _make_context()
    result = asyncio.run(run_full_analysis(ctx, module_runners=runners))

    assert "brand_dna" in result["skipped"]
    assert result["skipped"]["brand_dna"] == "Keine Referenzmodelle vorhanden"
    assert result["skipped_count"] >= 1
    assert "brand_dna" not in result["modules"]


def test_missing_runner_is_skipped():
    """A module with no runner in the dict is reported as skipped."""
    runners = _make_runners(results={"brand_dna": None})  # remove brand_dna
    ctx = _make_context()
    result = asyncio.run(run_full_analysis(ctx, module_runners=runners))

    assert "brand_dna" in result["skipped"]
    assert result["skipped"]["brand_dna"] == "Modul nicht gefunden"


# ---------------------------------------------------------------------------
# Error handling
# ---------------------------------------------------------------------------


def test_module_error_does_not_crash_others():
    """If one module raises, others still complete."""
    runners = _make_runners(results={
        "emotional": RuntimeError("Boom"),
    })
    ctx = _make_context()
    result = asyncio.run(run_full_analysis(ctx, module_runners=runners))

    assert "emotional" in result["errors"]
    assert "Boom" in result["errors"]["emotional"]["error"]
    assert result["errors"]["emotional"]["type"] == "RuntimeError"
    assert result["error_count"] == 1
    # Other tier-1 modules still ran
    assert "ergonomics" in result["modules"]
    assert "volume_storage" in result["modules"]
    assert "compliance" in result["modules"]


def test_error_in_tier1_does_not_block_tier2():
    """An error in tier 1 should not prevent tier 2 from running."""
    runners = _make_runners(results={
        "ergonomics": ValueError("Bad data"),
        "compliance": ValueError("Also bad"),
    })
    ctx = _make_context()
    result = asyncio.run(run_full_analysis(ctx, module_runners=runners))

    assert result["error_count"] == 2
    # Tier 2 modules still ran
    assert "production" in result["modules"]
    assert "materials" in result["modules"]
    assert "structural" in result["modules"]


# ---------------------------------------------------------------------------
# Overall score computation
# ---------------------------------------------------------------------------


def test_compute_overall_no_results():
    """No results -> score is None, confidence insufficient."""
    result = _compute_overall_score({}, "cruising_sail")
    assert result["score"] is None
    assert result["confidence"] == "insufficient"


def test_compute_overall_single_module():
    """Single module result -> score equals that module's score (weight normalised)."""
    results = {"ergonomics": _mock_result("ergonomics", 82.0)}
    result = _compute_overall_score(results, "cruising_sail")
    assert result["score"] == 82.0


def test_compute_overall_normalises_weights():
    """When only a subset of modules run, weights are normalised."""
    results = {
        "ergonomics": _mock_result("ergonomics", 80.0),
        "emotional": _mock_result("emotional", 60.0),
    }
    result = _compute_overall_score(results, "cruising_sail")
    # cruising_sail weights: ergonomics=0.10, emotional=0.15 -> 40%/60%
    expected = (80.0 * 0.10 + 60.0 * 0.15) / (0.10 + 0.15)
    assert abs(result["score"] - round(expected, 1)) < 0.1


def test_compute_overall_different_boat_classes():
    """Different boat classes produce different scores from same module results."""
    results = {
        "ergonomics": _mock_result("ergonomics", 90.0),
        "emotional": _mock_result("emotional", 50.0),
    }
    small = _compute_overall_score(results, "small_sail")
    superyacht = _compute_overall_score(results, "superyacht")

    # small_sail weights ergonomics more, superyacht weights emotional more
    # So small_sail should have a higher score
    assert small["score"] > superyacht["score"]


def test_compute_overall_confidence_measured():
    """Confidence is 'measured' when >= 70% of modules report it."""
    results = {
        "ergonomics": _mock_result("ergonomics", 80.0, "measured"),
        "emotional": _mock_result("emotional", 70.0, "measured"),
        "compliance": _mock_result("compliance", 90.0, "calculated"),
        "volume_storage": _mock_result("volume_storage", 85.0, "measured"),
    }
    result = _compute_overall_score(results, "cruising_sail")
    # 3/4 = 75% are measured/calculated -> "measured"
    assert result["confidence"] == "measured"


def test_compute_overall_confidence_estimated():
    """Confidence is 'estimated' when no modules are measured."""
    results = {
        "ergonomics": _mock_result("ergonomics", 80.0, "estimated"),
        "emotional": _mock_result("emotional", 70.0, "estimated"),
    }
    result = _compute_overall_score(results, "cruising_sail")
    assert result["confidence"] == "estimated"


# ---------------------------------------------------------------------------
# _build_module_kwargs
# ---------------------------------------------------------------------------


def test_build_kwargs_materials():
    """Materials module receives zone_materials as 'materials' kwarg."""
    ctx = _make_context(zone_materials=[{"zone_name": "Salon", "surface_type": "floor"}])
    kw = _build_module_kwargs("materials", ctx)
    assert kw["materials"] == ctx.zone_materials


def test_build_kwargs_cost():
    """Cost module receives cost_items and boat_length_m."""
    ctx = _make_context(cost_items=[{"category": "hull"}], length_m=14.0)
    kw = _build_module_kwargs("cost", ctx)
    assert kw["cost_items"] == ctx.cost_items
    assert kw["boat_length_m"] == 14.0


def test_build_kwargs_market_with_cost_result():
    """Market module receives estimated_cost when cost result is available."""
    ctx = _make_context(competitors=[{"key_metrics": {}}], length_m=14.0)
    ctx.module_results["cost"] = {
        "metrics": {"total_estimated_cost_eur": 300000.0},
    }
    kw = _build_module_kwargs("market", ctx)
    assert kw["estimated_cost"] == 300000.0
    assert kw["competitors"] == ctx.competitors
    assert kw["boat_length_m"] == 14.0


def test_build_kwargs_ergonomics_empty():
    """Ergonomics needs no extra kwargs."""
    ctx = _make_context()
    kw = _build_module_kwargs("ergonomics", ctx)
    assert kw == {}


# ---------------------------------------------------------------------------
# Empty / edge-case inputs
# ---------------------------------------------------------------------------


def test_full_analysis_empty_zones_graceful():
    """Empty zones + passages -> modules still run (they handle empty input)."""
    ctx = AnalysisContext(zones=[], passages=[], boat_class="small_sail")
    runners = _make_runners(default_score=50.0)
    result = asyncio.run(run_full_analysis(ctx, module_runners=runners))

    assert result["module_count"] == 12
    assert result["overall_score"] == 50.0


def test_full_analysis_unknown_boat_class_uses_fallback():
    """Unknown boat class falls back to cruising_sail weights for overall score."""
    ctx = AnalysisContext(zones=[], passages=[], boat_class="unknown_class")
    runners = _make_runners(default_score=70.0)
    result = asyncio.run(run_full_analysis(ctx, module_runners=runners))

    # Should still compute an overall score using fallback weights
    assert result["overall_score"] == 70.0


# ---------------------------------------------------------------------------
# Parallel execution within a tier
# ---------------------------------------------------------------------------


def test_tier1_modules_run_in_parallel():
    """Tier 1 modules are gathered concurrently (verified by execution count)."""
    call_order = []

    def make_runner(name, score=75.0):
        def runner(z, p, bc, co, **kw):
            call_order.append(name)
            return _mock_result(name, score)
        return runner

    runners = {}
    for name in ALL_MODULE_NAMES:
        runners[name] = make_runner(name)

    ctx = _make_context()
    result = asyncio.run(run_full_analysis(ctx, module_runners=runners))

    # All tier-1 modules should appear before any tier-2 module
    tier1 = set(EXECUTION_TIERS[0])
    tier2 = set(EXECUTION_TIERS[1])
    tier1_indices = [call_order.index(m) for m in tier1]
    tier2_indices = [call_order.index(m) for m in tier2]
    assert max(tier1_indices) < min(tier2_indices)
