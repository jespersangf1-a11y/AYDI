"""Tests for market & competitor analysis module."""
from tests.conftest import make_zone, make_competitor
from app.services.analysis.market import (
    BOAT_CLASS_DEFAULTS,
    SEVERITY_ORDER,
    analyze_metric_comparison,
    analyze_competitive_position,
    analyze_price_positioning,
    analyze_layout_uniqueness,
    analyze_market_gaps,
    run_market_analysis,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _default_config(boat_class: str = "cruising_sail") -> dict:
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


def _five_identical_competitors(key_metrics: dict | None = None) -> list[dict]:
    """Return 5 identical competitors — minimum for cruising_sail."""
    return [make_competitor(key_metrics=key_metrics) for _ in range(5)]


def _layout_metrics_at_avg() -> dict:
    """Layout metrics that exactly match competitor defaults."""
    return {
        "cockpit_area_sqm": 8.0,
        "salon_area_sqm": 14.0,
        "cabin_count": 2,
        "head_count": 1,
        "berth_count": 4,
        "storage_volume_l": 600.0,
        "deck_height_mm": 1950.0,
    }


# ---------------------------------------------------------------------------
# test_empty_competitors
# ---------------------------------------------------------------------------


def test_empty_competitors():
    """No competitors at all -> score 50, info warning about insufficient data."""
    result = run_market_analysis([], [], "cruising_sail", competitors=[])
    assert result["overall_score"] == 50.0
    assert any(w["severity"] == "info" for w in result["warnings"])
    assert any("MARKET_INSUFFICIENT_COMPETITORS" in w["code"] for w in result["warnings"])


# ---------------------------------------------------------------------------
# test_insufficient_competitors
# ---------------------------------------------------------------------------


def test_insufficient_competitors():
    """Fewer competitors than min_competitors -> score 50, info warning."""
    competitors = [make_competitor() for _ in range(3)]  # cruising_sail needs 5
    result = run_market_analysis([], [], "cruising_sail", competitors=competitors)
    assert result["overall_score"] == 50.0
    assert any("MARKET_INSUFFICIENT_COMPETITORS" in w["code"] for w in result["warnings"])
    # All sub-scores should be 50
    for score in result["sub_scores"].values():
        assert score == 50.0


# ---------------------------------------------------------------------------
# test_metrics_at_average
# ---------------------------------------------------------------------------


def test_metrics_at_average():
    """Layout exactly at competitor average for all metrics -> high metric_comparison score."""
    competitors = _five_identical_competitors()
    layout_metrics = _layout_metrics_at_avg()
    config = _default_config()
    score, warnings, metrics = analyze_metric_comparison(layout_metrics, competitors, config)
    # No metric deviates >20% -> score 100
    assert score == 100.0
    assert metrics["deviating_count"] == 0
    # No deviation warnings
    deviation_warnings = [w for w in warnings if "BELOW" in w["code"] or "ABOVE" in w["code"]]
    assert len(deviation_warnings) == 0


# ---------------------------------------------------------------------------
# test_metrics_below_average
# ---------------------------------------------------------------------------


def test_metrics_below_average():
    """Layout with cabin_count well below competitor average -> warning issued."""
    competitors = _five_identical_competitors()
    # cabin_count 2 → average 2, layout has 0 → deviation -100%
    layout_metrics = {**_layout_metrics_at_avg(), "cabin_count": 0}
    config = _default_config()
    score, warnings, metrics = analyze_metric_comparison(layout_metrics, competitors, config)
    assert score < 100.0
    below_warnings = [w for w in warnings if "BELOW" in w["code"]]
    assert len(below_warnings) >= 1
    assert any("CABIN_COUNT" in w["code"] for w in below_warnings)
    assert metrics["deviating_count"] >= 1


# ---------------------------------------------------------------------------
# test_metrics_above_average
# ---------------------------------------------------------------------------


def test_metrics_above_average():
    """Layout with cockpit area well above competitor average -> above-average info note."""
    competitors = _five_identical_competitors()
    # cockpit 8.0 → average 8.0, layout has 20.0 → deviation +150%
    layout_metrics = {**_layout_metrics_at_avg(), "cockpit_area_sqm": 20.0}
    config = _default_config()
    score, warnings, metrics = analyze_metric_comparison(layout_metrics, competitors, config)
    above_warnings = [w for w in warnings if "ABOVE" in w["code"]]
    assert len(above_warnings) >= 1
    assert any("COCKPIT" in w["code"] for w in above_warnings)
    assert metrics["deviating_count"] >= 1


# ---------------------------------------------------------------------------
# test_competitive_position_strong
# ---------------------------------------------------------------------------


def test_competitive_position_strong():
    """Layout outperforms competitors on multiple metrics -> score > 50."""
    competitors = _five_identical_competitors()
    # Push cabin_count, salon_area, and cockpit above 110% of avg
    layout_metrics = {
        **_layout_metrics_at_avg(),
        "cockpit_area_sqm": 10.0,   # +25%
        "salon_area_sqm": 18.0,     # +29%
        "cabin_count": 3,           # +50%
    }
    config = _default_config()
    score, warnings, metrics = analyze_competitive_position(layout_metrics, competitors, config)
    assert score > 50.0
    assert len(metrics["strengths"]) >= 2
    assert len(metrics["weaknesses"]) == 0


# ---------------------------------------------------------------------------
# test_competitive_position_weak
# ---------------------------------------------------------------------------


def test_competitive_position_weak():
    """Layout underperforms on multiple metrics -> score < 50."""
    competitors = _five_identical_competitors()
    layout_metrics = {
        **_layout_metrics_at_avg(),
        "cabin_count": 1,           # -50%
        "salon_area_sqm": 8.0,      # -43%
        "storage_volume_l": 200.0,  # -67%
    }
    config = _default_config()
    score, warnings, metrics = analyze_competitive_position(layout_metrics, competitors, config)
    assert score < 50.0
    assert len(metrics["weaknesses"]) >= 2
    weakness_warnings = [w for w in warnings if "COMPETITIVE_WEAKNESS" in w["code"]]
    assert len(weakness_warnings) >= 2


# ---------------------------------------------------------------------------
# test_price_within_range
# ---------------------------------------------------------------------------


def test_price_within_range():
    """Estimated cost within ±15% of competitor median -> score 100."""
    competitors = _five_identical_competitors()  # price_range mid = 200_000
    config = _default_config()
    layout_metrics = _layout_metrics_at_avg()
    score, warnings, metrics = analyze_price_positioning(
        layout_metrics, competitors, 200_000.0, config
    )
    assert score == 100.0
    assert metrics["competitor_median_price"] == 200_000.0
    assert not any("OUTLIER" in w["code"] for w in warnings)


# ---------------------------------------------------------------------------
# test_price_outlier_high
# ---------------------------------------------------------------------------


def test_price_outlier_high():
    """Estimated cost significantly above competitor median -> PRICE_OUTLIER_HIGH warning."""
    competitors = _five_identical_competitors()  # median = 200_000
    config = _default_config()
    layout_metrics = _layout_metrics_at_avg()
    score, warnings, metrics = analyze_price_positioning(
        layout_metrics, competitors, 400_000.0, config  # +100%
    )
    assert score < 100.0
    assert any(w["code"] == "PRICE_OUTLIER_HIGH" for w in warnings)


# ---------------------------------------------------------------------------
# test_price_outlier_low
# ---------------------------------------------------------------------------


def test_price_outlier_low():
    """Estimated cost significantly below competitor median -> PRICE_OUTLIER_LOW warning."""
    competitors = _five_identical_competitors()  # median = 200_000
    config = _default_config()
    layout_metrics = _layout_metrics_at_avg()
    score, warnings, metrics = analyze_price_positioning(
        layout_metrics, competitors, 80_000.0, config  # -60%
    )
    assert score < 100.0
    assert any(w["code"] == "PRICE_OUTLIER_LOW" for w in warnings)


# ---------------------------------------------------------------------------
# test_layout_too_similar
# ---------------------------------------------------------------------------


def test_layout_too_similar():
    """Layout metrics nearly identical to all competitors -> LAYOUT_TOO_SIMILAR warning."""
    competitors = _five_identical_competitors()
    # Metrics at average — deviation well below 20% threshold for all
    layout_metrics = _layout_metrics_at_avg()
    config = _default_config()
    score, warnings, metrics = analyze_layout_uniqueness(layout_metrics, competitors, config)
    assert any(w["code"] == "LAYOUT_TOO_SIMILAR" for w in warnings)
    assert metrics["unique_ratio"] < 0.20


# ---------------------------------------------------------------------------
# test_layout_appropriately_unique
# ---------------------------------------------------------------------------


def test_layout_appropriately_unique():
    """Layout differs on roughly half the metrics -> high uniqueness score."""
    competitors = _five_identical_competitors()
    # Make ~half the metrics deviate >20% from competitor avg
    layout_metrics = {
        "cockpit_area_sqm": 8.0,       # same
        "salon_area_sqm": 14.0,        # same
        "cabin_count": 2,              # same
        "head_count": 1,               # same
        "berth_count": 6,              # +50% deviation
        "storage_volume_l": 300.0,     # -50% deviation
        "deck_height_mm": 2100.0,      # +7.7% — borderline, below threshold
    }
    config = _default_config()
    score, warnings, metrics = analyze_layout_uniqueness(layout_metrics, competitors, config)
    # Should have at least 2 unique metrics (berth_count and storage_volume_l)
    assert metrics["unique_count"] >= 2
    # No extreme warnings
    assert not any(w["code"] == "LAYOUT_TOO_UNUSUAL" for w in warnings)


# ---------------------------------------------------------------------------
# test_market_gaps_found
# ---------------------------------------------------------------------------


def test_market_gaps_found():
    """Layout exceeds max competitor value on a metric -> gap identified."""
    competitors = [
        make_competitor(key_metrics={**_layout_metrics_at_avg(), "cabin_count": 2})
        for _ in range(5)
    ]
    # Layout has 5 cabins — above every competitor
    layout_metrics = {**_layout_metrics_at_avg(), "cabin_count": 5}
    config = _default_config()
    score, warnings, metrics = analyze_market_gaps(layout_metrics, competitors, config)
    assert metrics["gap_count"] >= 1
    gap_metrics = [g["metric"] for g in metrics["gaps"]]
    assert "cabin_count" in gap_metrics
    assert any("MARKET_GAP_ABOVE_CABIN_COUNT" in w["code"] for w in warnings)
    assert score > 60.0


# ---------------------------------------------------------------------------
# test_different_boat_classes
# ---------------------------------------------------------------------------


def test_different_boat_classes():
    """Different boat classes use different min_competitors and weights -> distinct scores."""
    # small_sail needs 5 competitors; supply exactly 5
    small_sail_competitors = [make_competitor() for _ in range(5)]
    result_small = run_market_analysis(
        [], [], "small_sail", competitors=small_sail_competitors, boat_length_m=10.0
    )

    # superyacht only needs 3 competitors
    superyacht_competitors = [
        make_competitor(
            key_metrics={
                "salon_area_sqm": 80.0,
                "cabin_count": 5,
                "head_count": 6,
                "crew_quarters_count": 2,
                "deck_height_mm": 2200.0,
            }
        )
        for _ in range(3)
    ]
    result_super = run_market_analysis(
        [], [], "superyacht", competitors=superyacht_competitors, boat_length_m=35.0
    )

    # Both should produce valid results (not the insufficient-competitors fallback)
    assert result_small["module"] == "market"
    assert result_super["module"] == "market"
    assert len(result_small["sub_scores"]) == 5
    assert len(result_super["sub_scores"]) == 5
    # Weights differ between classes so overall scores may differ
    # (just verifying both are computable and in range)
    assert 0 <= result_small["overall_score"] <= 100
    assert 0 <= result_super["overall_score"] <= 100


# ---------------------------------------------------------------------------
# test_full_integration
# ---------------------------------------------------------------------------


def test_full_integration():
    """Full run with realistic zones and competitors produces valid result structure."""
    zones = [
        make_zone("Cockpit", "cockpit",
                  polygon=[[0, 0], [3000, 0], [3000, 3000], [0, 3000]],
                  height_mm=1950),
        make_zone("Salon", "salon",
                  polygon=[[3000, 0], [7000, 0], [7000, 3000], [3000, 3000]],
                  height_mm=1950),
        make_zone("Kabine 1", "cabin",
                  polygon=[[7000, 0], [9000, 0], [9000, 2000], [7000, 2000]],
                  height_mm=1900, properties={"berth_count": 2}),
        make_zone("Kabine 2", "cabin",
                  polygon=[[7000, 2000], [9000, 2000], [9000, 3500], [7000, 3500]],
                  height_mm=1900, properties={"berth_count": 2}),
        make_zone("Nasszelle", "head",
                  polygon=[[9000, 0], [10500, 0], [10500, 1500], [9000, 1500]],
                  height_mm=1900),
        make_zone("Stauraum", "storage",
                  polygon=[[9000, 1500], [10500, 1500], [10500, 3500], [9000, 3500]],
                  height_mm=800),
    ]

    competitors = [
        make_competitor(
            key_metrics={
                "cockpit_area_sqm": 9.0,
                "salon_area_sqm": 12.0,
                "cabin_count": 2,
                "head_count": 1,
                "berth_count": 4,
                "storage_volume_l": 550.0,
                "deck_height_mm": 1930.0,
            },
            length_m=12.0,
            price_range_eur={"min": 170_000, "max": 210_000},
        )
        for _ in range(5)
    ]

    result = run_market_analysis(
        zones,
        [],
        "cruising_sail",
        competitors=competitors,
        boat_length_m=12.0,
        estimated_cost=190_000.0,
    )

    assert result["module"] == "market"
    assert 0 <= result["overall_score"] <= 100
    assert set(result["sub_scores"].keys()) == {
        "metric_comparison",
        "competitive_position",
        "price_positioning",
        "uniqueness",
        "gaps",
    }
    assert "layout_metrics" in result["metrics"]
    assert result["config_used"] is not None
    # Warnings sorted by severity
    severities = [w["severity"] for w in result["warnings"]]
    order = [SEVERITY_ORDER.get(s, 2) for s in severities]
    assert order == sorted(order)


# ---------------------------------------------------------------------------
# test_no_estimated_cost
# ---------------------------------------------------------------------------


def test_no_estimated_cost():
    """No estimated cost provided -> price_positioning score 50 and info warning."""
    competitors = _five_identical_competitors()
    config = _default_config()
    layout_metrics = _layout_metrics_at_avg()
    score, warnings, metrics = analyze_price_positioning(
        layout_metrics, competitors, None, config
    )
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
    assert any("PRICE_NO_DATA" in w["code"] for w in warnings)
    assert metrics["estimated_cost"] is None
