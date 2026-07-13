"""Tests for the cost estimation analysis module."""
from tests.conftest import make_zone, make_passage, make_cost_item
from app.services.analysis.cost import (
    BOAT_CLASS_DEFAULTS,
    SEVERITY_ORDER,
    analyze_material_costs,
    analyze_labor_estimate,
    analyze_cost_per_meter,
    analyze_cost_distribution,
    analyze_cost_risk,
    run_cost_analysis,
)


def _default_config(boat_class: str = "cruising_sail") -> dict:
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _make_balanced_items(total: float = 320_000.0) -> list[dict]:
    """Build a set of cost items whose category shares match cruising_sail ideal."""
    # ideal: material=0.38, labor=0.35, equipment=0.17, overhead=0.10
    return [
        make_cost_item("material", total_cost_eur=total * 0.38, source="quote"),
        make_cost_item("labor", total_cost_eur=total * 0.35, source="quote"),
        make_cost_item("equipment", total_cost_eur=total * 0.17, source="quote"),
        make_cost_item("overhead", total_cost_eur=total * 0.10, source="quote"),
    ]


# ---------------------------------------------------------------------------
# test_empty_cost_items
# ---------------------------------------------------------------------------


def test_empty_cost_items():
    """No cost items provided -> module reports unavailable (no fabricated score)."""
    result = run_cost_analysis([], [], "cruising_sail", cost_items=None)
    assert result["module"] == "cost"
    assert result["available"] is False
    assert "reason" in result
    assert "overall_score" not in result


# ---------------------------------------------------------------------------
# test_material_costs_reasonable
# ---------------------------------------------------------------------------


def test_material_costs_reasonable():
    """Many small material items — no single item > 15% -> score close to 100."""
    items = [
        make_cost_item("material", subcategory=f"pos_{i}", total_cost_eur=1000.0, source="quote")
        for i in range(10)
    ]
    config = _default_config()
    score, warnings, metrics = analyze_material_costs(items, config)
    assert score >= 90.0
    assert metrics["concentrated_items"] == 0
    assert not any(w["code"] == "MATERIAL_COST_HIGH" for w in warnings)


# ---------------------------------------------------------------------------
# test_material_costs_concentrated
# ---------------------------------------------------------------------------


def test_material_costs_concentrated():
    """One item makes up 80% of material costs -> MATERIAL_COST_HIGH warning."""
    items = [
        make_cost_item("material", subcategory="GFK-Laminat", total_cost_eur=80_000.0, source="quote"),
        make_cost_item("material", subcategory="Beschläge", total_cost_eur=20_000.0, source="quote"),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_material_costs(items, config)
    assert score < 100.0
    assert any(w["code"] == "MATERIAL_COST_HIGH" for w in warnings)
    assert metrics["concentrated_items"] >= 1


# ---------------------------------------------------------------------------
# test_labor_estimate_basic
# ---------------------------------------------------------------------------


def test_labor_estimate_basic():
    """Zones with known types give a non-zero estimated hours value."""
    zones = [
        make_zone("Salon", "salon"),
        make_zone("Kabine", "cabin"),
        make_zone("Pantry", "pantry"),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_labor_estimate(zones, [], config)
    assert metrics["estimated_hours"] > 0.0
    assert 0.0 <= score <= 100.0


# ---------------------------------------------------------------------------
# test_cost_per_meter_within_benchmark
# ---------------------------------------------------------------------------


def test_cost_per_meter_within_benchmark():
    """Total cost within ±20% of benchmark -> score 100."""
    benchmark = BOAT_CLASS_DEFAULTS["cruising_sail"]["benchmark_cost_per_meter"]
    boat_length = 12.0
    # Total = exactly benchmark * length (deviation = 0%)
    items = [make_cost_item("material", total_cost_eur=benchmark * boat_length, source="quote")]
    config = _default_config()
    score, warnings, metrics = analyze_cost_per_meter(items, boat_length, config)
    assert score == 100.0
    assert not any(w["code"] in ("COST_ABOVE_BENCHMARK", "COST_BELOW_BENCHMARK") for w in warnings)


# ---------------------------------------------------------------------------
# test_cost_per_meter_above_benchmark
# ---------------------------------------------------------------------------


def test_cost_per_meter_above_benchmark():
    """Total cost 60% above benchmark -> COST_ABOVE_BENCHMARK warning, score < 80."""
    benchmark = BOAT_CLASS_DEFAULTS["cruising_sail"]["benchmark_cost_per_meter"]
    boat_length = 12.0
    # 60% above benchmark
    items = [make_cost_item("material", total_cost_eur=benchmark * boat_length * 1.60, source="quote")]
    config = _default_config()
    score, warnings, metrics = analyze_cost_per_meter(items, boat_length, config)
    assert score < 80.0
    assert any(w["code"] == "COST_ABOVE_BENCHMARK" for w in warnings)
    assert metrics["deviation_pct"] > 0


# ---------------------------------------------------------------------------
# test_cost_distribution_balanced
# ---------------------------------------------------------------------------


def test_cost_distribution_balanced():
    """Items matching ideal distribution -> score close to 100."""
    items = _make_balanced_items(total=320_000.0)
    config = _default_config()
    score, warnings, metrics = analyze_cost_distribution(items, config)
    assert score >= 95.0
    assert not any(w["code"] == "COST_CONCENTRATION" for w in warnings)


# ---------------------------------------------------------------------------
# test_cost_distribution_concentrated
# ---------------------------------------------------------------------------


def test_cost_distribution_concentrated():
    """Single category > 50% of total -> COST_CONCENTRATION warning."""
    items = [
        make_cost_item("material", total_cost_eur=90_000.0, source="estimate"),
        make_cost_item("labor", total_cost_eur=5_000.0, source="estimate"),
        make_cost_item("equipment", total_cost_eur=3_000.0, source="estimate"),
        make_cost_item("overhead", total_cost_eur=2_000.0, source="estimate"),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_cost_distribution(items, config)
    assert any(w["code"] == "COST_CONCENTRATION" for w in warnings)


# ---------------------------------------------------------------------------
# test_cost_risk_all_quotes
# ---------------------------------------------------------------------------


def test_cost_risk_all_quotes():
    """All items sourced from firm quotes -> score 100."""
    items = [
        make_cost_item("material", total_cost_eur=50_000.0, source="quote"),
        make_cost_item("labor", total_cost_eur=40_000.0, source="quote"),
        make_cost_item("equipment", total_cost_eur=20_000.0, source="contract"),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_cost_risk(items, config)
    assert score == 100.0
    assert not any(w["code"] == "COST_UNCERTAINTY_HIGH" for w in warnings)
    assert metrics["quote_share"] == 1.0


# ---------------------------------------------------------------------------
# test_cost_risk_all_estimates
# ---------------------------------------------------------------------------


def test_cost_risk_all_estimates():
    """All items are rough estimates -> lower score + COST_UNCERTAINTY_HIGH."""
    items = [
        make_cost_item("material", total_cost_eur=50_000.0, source="estimate"),
        make_cost_item("labor", total_cost_eur=40_000.0, source="estimate"),
        make_cost_item("equipment", total_cost_eur=20_000.0, source="estimate"),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_cost_risk(items, config)
    assert score < 50.0
    assert any(w["code"] == "COST_UNCERTAINTY_HIGH" for w in warnings)
    assert metrics["estimate_share"] == 1.0


# ---------------------------------------------------------------------------
# test_different_boat_classes_different_benchmarks
# ---------------------------------------------------------------------------


def test_different_boat_classes_different_benchmarks():
    """Same total cost → different scores for small_sail vs superyacht."""
    boat_length = 10.0
    total_cost = 250_000.0  # well within small_sail benchmark, far below superyacht

    items = [make_cost_item("material", total_cost_eur=total_cost, source="quote")]

    result_small = run_cost_analysis(
        [], [], "small_sail", cost_items=items, boat_length_m=boat_length,
    )
    result_super = run_cost_analysis(
        [], [], "superyacht", cost_items=items, boat_length_m=boat_length,
    )

    # small_sail benchmark: 20000 €/m × 10m = 200000 → 250000 is 25% above (slight warning)
    # superyacht benchmark: 120000 €/m × 10m = 1200000 → 250000 is 79% below (big warning)
    small_cpm = result_small["metrics"].get("cost_per_meter", {}).get("cost_per_meter", 0)
    super_cpm = result_super["metrics"].get("cost_per_meter", {}).get("cost_per_meter", 0)
    # Both resolve same cost_per_meter but benchmarks differ -> scores differ
    assert result_small["sub_scores"]["cost_per_meter"] != result_super["sub_scores"]["cost_per_meter"]


# ---------------------------------------------------------------------------
# test_config_overrides
# ---------------------------------------------------------------------------


def test_config_overrides():
    """Config override for benchmark is stored in config_used and alters the score."""
    boat_length = 12.0
    total = 12.0 * 50_000.0  # cost per meter = 50000

    items = [make_cost_item("material", total_cost_eur=total, source="quote")]

    # Without override: cruising_sail benchmark = 32000 (50000 is 56% above -> score < 50)
    result_default = run_cost_analysis(
        [], [], "cruising_sail", cost_items=items, boat_length_m=boat_length,
    )

    # With override: benchmark = 50000 (exact match -> cpm score = 100)
    result_override = run_cost_analysis(
        [], [], "cruising_sail",
        config_overrides={"benchmark_cost_per_meter": 50_000},
        cost_items=items,
        boat_length_m=boat_length,
    )

    assert result_override["config_used"]["benchmark_cost_per_meter"] == 50_000
    assert result_override["sub_scores"]["cost_per_meter"] > result_default["sub_scores"]["cost_per_meter"]


# ---------------------------------------------------------------------------
# test_warnings_sorted_by_severity
# ---------------------------------------------------------------------------


def test_warnings_sorted_by_severity():
    """All warnings in the result must be ordered: critical -> warning -> info."""
    # Create items that trigger a mix of warning types:
    # - Very high material concentration (warning)
    # - All estimates (warning)
    # - Cost far above benchmark (warning)
    items = [
        make_cost_item("material", total_cost_eur=900_000.0, source="estimate"),
        make_cost_item("labor", total_cost_eur=50_000.0, source="estimate"),
    ]
    result = run_cost_analysis(
        [], [], "large_motor", cost_items=items, boat_length_m=20.0,
    )
    severities = [w["severity"] for w in result["warnings"]]
    order = [SEVERITY_ORDER.get(s, 2) for s in severities]
    assert order == sorted(order), f"Warnings not sorted: {severities}"


# ---------------------------------------------------------------------------
# test_full_integration_cruising_sail
# ---------------------------------------------------------------------------


def test_full_integration_cruising_sail():
    """Complete scenario for a 12m cruising sailboat with realistic cost data."""
    boat_length = 12.2
    benchmark = BOAT_CLASS_DEFAULTS["cruising_sail"]["benchmark_cost_per_meter"]
    total = benchmark * boat_length  # exactly on benchmark

    zones = [
        make_zone("Salon", "salon"),
        make_zone("Kabine Achtern", "cabin"),
        make_zone("Pantry", "pantry"),
        make_zone("Nasszelle", "head"),
        make_zone("Cockpit", "cockpit"),
    ]

    items = [
        make_cost_item("material", subcategory="GFK-Laminat", total_cost_eur=total * 0.20, source="quote"),
        make_cost_item("material", subcategory="Innenausbau", total_cost_eur=total * 0.10, source="quote"),
        make_cost_item("material", subcategory="Beschläge", total_cost_eur=total * 0.08, source="quote"),
        make_cost_item("labor", subcategory="Laminierung", total_cost_eur=total * 0.18, source="contract"),
        make_cost_item("labor", subcategory="Innenausbau", total_cost_eur=total * 0.17, source="quote"),
        make_cost_item("equipment", subcategory="Motor", total_cost_eur=total * 0.17, source="quote"),
        make_cost_item("overhead", total_cost_eur=total * 0.10, source="budget"),
    ]

    result = run_cost_analysis(zones, [], "cruising_sail", cost_items=items, boat_length_m=boat_length)

    assert result["module"] == "cost"
    assert 0.0 <= result["overall_score"] <= 100.0
    assert set(result["sub_scores"].keys()) == {
        "material_costs", "labor_estimate", "cost_per_meter", "distribution", "risk", "parametric_estimate"
    }
    assert all(0.0 <= v <= 100.0 for v in result["sub_scores"].values())
    # Should score well since data is well-structured
    assert result["overall_score"] >= 55.0
    # config snapshot is stored
    assert "benchmark_cost_per_meter" in result["config_used"]
    assert result["config_used"]["benchmark_cost_per_meter"] == 32_000


# ---------------------------------------------------------------------------
# test_full_integration_large_motor
# ---------------------------------------------------------------------------


def test_full_integration_large_motor():
    """Complete scenario for a 20m large motor yacht — different weights and benchmarks."""
    boat_length = 19.8
    benchmark = BOAT_CLASS_DEFAULTS["large_motor"]["benchmark_cost_per_meter"]
    total = benchmark * boat_length * 1.10  # 10% above benchmark

    zones = [
        make_zone("Salon", "salon"),
        make_zone("Master Kabine", "cabin"),
        make_zone("Gast Kabine", "cabin"),
        make_zone("Crew Kabine", "cabin", is_crew_area=True),
        make_zone("Pantry", "pantry"),
        make_zone("Maschinenraum", "engine"),
        make_zone("Nasszelle 1", "head"),
        make_zone("Nasszelle 2", "head"),
    ]

    items = [
        make_cost_item("material", total_cost_eur=total * 0.35, source="quote"),
        make_cost_item("labor", total_cost_eur=total * 0.30, source="quote"),
        make_cost_item("equipment", total_cost_eur=total * 0.20, source="quote"),
        make_cost_item("overhead", total_cost_eur=total * 0.15, source="budget"),
    ]

    result = run_cost_analysis(zones, [], "large_motor", cost_items=items, boat_length_m=boat_length)

    assert result["module"] == "cost"
    assert 0.0 <= result["overall_score"] <= 100.0
    # 10% above benchmark is within tolerance -> cost_per_meter score should be 100
    assert result["sub_scores"]["cost_per_meter"] == 100.0
    # Ideal distribution for large_motor matches input -> good distribution score
    assert result["sub_scores"]["distribution"] >= 90.0
    # Weights must be large_motor weights (cost_per_meter = 0.25)
    assert result["config_used"]["labor_rate_eur_hour"] == 65
