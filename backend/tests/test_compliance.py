"""Tests for compliance checker module — escape routes and fire safety."""
from tests.conftest import make_passage, make_zone
from app.services.analysis.compliance import (
    analyze_escape_routes,
    analyze_fire_safety,
    analyze_stability_impact,
    analyze_railing_requirements,
    analyze_electrical_access,
    analyze_ce_category,
    run_compliance_analysis,
    BOAT_CLASS_DEFAULTS,
    SEVERITY_ORDER,
)


def _default_config(boat_class="cruising_sail"):
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


# ---------------------------------------------------------------------------
# analyze_escape_routes
# ---------------------------------------------------------------------------


def test_escape_route_compliant():
    """Cabin connected to cockpit via wide passage -> score 100."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("cabin1", "cabin"),
    ]
    passages = [make_passage("cabin1", "cockpit", width_mm=700)]
    config = _default_config()
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score == 100.0
    assert metrics["cabins_compliant"] == 1


def test_escape_route_no_cockpit():
    """No cockpit -> score 0, critical warning."""
    zones = [make_zone("cabin1", "cabin")]
    passages = []
    config = _default_config()
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score == 0.0
    assert any(w["severity"] == "critical" for w in warnings)


def test_escape_route_no_cabins():
    """No sleeping zones -> score 100, info."""
    zones = [make_zone("cockpit", "cockpit"), make_zone("salon", "salon")]
    passages = [make_passage("cockpit", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score == 100.0
    assert any(w["severity"] == "info" for w in warnings)
    assert metrics["cabins_total"] == 0


def test_escape_route_unreachable():
    """Cabin with no path to cockpit -> critical."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("cabin1", "cabin"),
        make_zone("salon", "salon"),
    ]
    passages = [make_passage("cockpit", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score == 0.0
    assert any(w["severity"] == "critical" for w in warnings)
    assert metrics["cabins_compliant"] == 0


def test_escape_route_narrow_passage():
    """Escape route passage below 600mm ISO minimum -> critical, partial score."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("cabin1", "cabin"),
    ]
    passages = [make_passage("cabin1", "cockpit", width_mm=500)]
    config = _default_config()
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score == 50.0
    assert any(w["severity"] == "critical" for w in warnings)


def test_escape_route_too_long():
    """Escape route with too many hops -> warning."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("salon", "salon"),
        make_zone("pantry", "pantry"),
        make_zone("head", "head"),
        make_zone("storage1", "storage"),
        make_zone("storage2", "storage"),
        make_zone("storage3", "storage"),
        make_zone("cabin1", "cabin"),
    ]
    passages = [
        make_passage("cabin1", "storage3"),
        make_passage("storage3", "storage2"),
        make_passage("storage2", "storage1"),
        make_passage("storage1", "head"),
        make_passage("head", "pantry"),
        make_passage("pantry", "salon"),
        make_passage("salon", "cockpit"),
    ]
    config = _default_config()  # max_escape_hops = 5
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score < 100.0
    assert any(w["severity"] == "warning" for w in warnings)


# ---------------------------------------------------------------------------
# analyze_fire_safety
# ---------------------------------------------------------------------------


def test_fire_safety_good():
    """Engine far from living zones, accessible -> high score."""
    zones = [
        make_zone("engine", "engine", polygon=[[8000, 1000], [10000, 1000], [10000, 3000], [8000, 3000]]),
        make_zone("salon", "salon", polygon=[[0, 0], [4000, 0], [4000, 4000], [0, 4000]]),
    ]
    passages = [make_passage("salon", "engine")]
    config = _default_config()
    score, warnings, metrics = analyze_fire_safety(zones, passages, config)
    assert score >= 80.0
    assert metrics["engine_accessible"] is True


def test_fire_safety_no_engine():
    """No engine zone -> score 50, info."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_fire_safety(zones, [], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


def test_fire_safety_engine_too_close():
    """Engine centroid within min_engine_clearance_mm of living zone -> warning."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [500, 0], [500, 500], [0, 500]]),
        make_zone("cabin", "cabin", polygon=[[500, 0], [1000, 0], [1000, 500], [500, 500]]),
    ]
    passages = [make_passage("engine", "cabin")]
    config = _default_config()  # min_engine_clearance_mm = 600
    # Centroids: engine (250,250), cabin (750,250) -> dist = 500mm < 600mm
    score, warnings, metrics = analyze_fire_safety(zones, passages, config)
    assert score < 100.0
    assert any(w["severity"] == "warning" for w in warnings)
    assert metrics["min_clearance_mm"] < 600


def test_fire_safety_engine_inaccessible():
    """Engine not connected via passages -> critical."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("salon", "salon"),
    ]
    passages = []
    config = _default_config()
    score, warnings, metrics = analyze_fire_safety(zones, passages, config)
    assert any(w["severity"] == "critical" for w in warnings)
    assert metrics["engine_accessible"] is False


# ---------------------------------------------------------------------------
# analyze_stability_impact
# ---------------------------------------------------------------------------


def test_stability_centered():
    """Engine on centerline -> high score."""
    zones = [
        make_zone("engine", "engine", polygon=[[4000, 1000], [6000, 1000], [6000, 3000], [4000, 3000]]),
        make_zone("salon", "salon", polygon=[[0, 0], [4000, 0], [4000, 4000], [0, 4000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_stability_impact(zones, config)
    assert score >= 80.0
    assert metrics["y_deviation_ratio"] < 0.3


def test_stability_no_heavy_zones():
    """No engine/storage -> score 50, info."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_stability_impact(zones, config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


def test_stability_off_center():
    """Engine far from Y-centerline -> warning."""
    zones = [
        make_zone("engine", "engine", polygon=[[4000, 0], [6000, 0], [6000, 500], [4000, 500]]),
        make_zone("salon", "salon", polygon=[[0, 0], [4000, 0], [4000, 4000], [0, 4000]]),
    ]
    config = _default_config()
    # Layout Y range: 0-4000, center = 2000
    # Engine centroid Y = 250, deviation = |250-2000|/2000 = 0.875
    score, warnings, metrics = analyze_stability_impact(zones, config)
    assert score < 50.0
    assert any(w["severity"] == "warning" for w in warnings)
    assert metrics["y_deviation_ratio"] > 0.3


# ---------------------------------------------------------------------------
# analyze_railing_requirements
# ---------------------------------------------------------------------------


def test_railing_compliant():
    """Cockpit with has_railing=True -> score 100."""
    zones = [
        make_zone("cockpit", "cockpit", properties={"has_railing": True}),
        make_zone("foredeck", "foredeck", properties={"has_railing": True}),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_railing_requirements(zones, config)
    assert score == 100.0
    assert metrics["zones_compliant"] == 2


def test_railing_no_deck_zones():
    """No exposed deck zones -> score 100."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_railing_requirements(zones, config)
    assert score == 100.0
    assert metrics["zones_checked"] == 0


def test_railing_violation():
    """Cockpit with has_railing=False -> critical."""
    zones = [
        make_zone("cockpit", "cockpit", properties={"has_railing": False}),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_railing_requirements(zones, config)
    assert score < 100.0
    assert any(w["severity"] == "critical" for w in warnings)


def test_railing_no_data():
    """Cockpit without has_railing property -> info warning, score 50."""
    zones = [make_zone("cockpit", "cockpit")]
    config = _default_config()
    score, warnings, metrics = analyze_railing_requirements(zones, config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


# ---------------------------------------------------------------------------
# analyze_electrical_access
# ---------------------------------------------------------------------------


def test_electrical_good():
    """Engine zone adequate size and accessible -> high score."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
        make_zone("salon", "salon"),
    ]
    passages = [make_passage("engine", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_electrical_access(zones, passages, config)
    assert score >= 80.0
    assert metrics["accessible"] is True


def test_electrical_no_engine():
    """No engine zone -> score 50, info."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_electrical_access(zones, [], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


def test_electrical_too_small():
    """Engine zone below minimum area -> warning."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [500, 0], [500, 500], [0, 500]]),
        make_zone("salon", "salon"),
    ]
    passages = [make_passage("engine", "salon")]
    config = _default_config()  # min_electrical_area_sqm = 0.5
    # Engine area = 0.25 sqm < 0.5
    score, warnings, metrics = analyze_electrical_access(zones, passages, config)
    assert score < 100.0
    assert any(w["severity"] == "warning" for w in warnings)


def test_electrical_inaccessible():
    """Engine not connected via passages -> critical."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
        make_zone("salon", "salon"),
    ]
    passages = []
    config = _default_config()
    score, warnings, metrics = analyze_electrical_access(zones, passages, config)
    assert any(w["severity"] == "critical" for w in warnings)
    assert metrics["accessible"] is False


# ---------------------------------------------------------------------------
# analyze_ce_category
# ---------------------------------------------------------------------------


def test_ce_category_compliant():
    """All required zones present for CE category A -> score 100."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("engine", "engine"),
        make_zone("helm", "helm"),
        make_zone("cabin1", "cabin"),
        make_zone("head", "head"),
        make_zone("pantry", "pantry"),
    ]
    config = _default_config()  # ce_category = "A"
    score, warnings, metrics = analyze_ce_category(zones, config)
    assert score == 100.0
    assert len(metrics["missing_zones"]) == 0


def test_ce_category_missing_zones():
    """Missing required zones -> warnings."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("helm", "helm"),
    ]
    config = _default_config()  # ce_category = "A", requires 6 zone types
    score, warnings, metrics = analyze_ce_category(zones, config)
    assert score < 100.0
    assert len(warnings) > 0
    assert len(metrics["missing_zones"]) > 0


def test_ce_category_d_minimal():
    """Only helm -> score 100 for CE category D."""
    zones = [make_zone("helm", "helm")]
    config = _default_config("small_sail")
    config["ce_category"] = "D"  # Only needs helm
    score, warnings, metrics = analyze_ce_category(zones, config)
    assert score == 100.0


# ---------------------------------------------------------------------------
# Integration
# ---------------------------------------------------------------------------


def test_full_compliance_analysis():
    """Complete layout -> valid result structure with all 6 sub-scores."""
    zones = [
        make_zone("cockpit", "cockpit", properties={"has_railing": True}),
        make_zone("salon", "salon", polygon=[[3000, 0], [7000, 0], [7000, 4000], [3000, 4000]]),
        make_zone("cabin1", "cabin", polygon=[[0, 0], [3000, 0], [3000, 2000], [0, 2000]]),
        make_zone("engine", "engine", polygon=[[7000, 1000], [9000, 1000], [9000, 3000], [7000, 3000]]),
        make_zone("helm", "helm"),
        make_zone("head", "head"),
        make_zone("pantry", "pantry"),
    ]
    passages = [
        make_passage("cockpit", "salon"),
        make_passage("salon", "cabin1"),
        make_passage("salon", "engine"),
        make_passage("salon", "helm"),
        make_passage("salon", "head"),
        make_passage("salon", "pantry"),
    ]
    result = run_compliance_analysis(zones, passages, "cruising_sail")
    assert result["module"] == "compliance"
    assert 0 <= result["overall_score"] <= 100
    assert "escape_routes" in result["sub_scores"]
    assert "fire_safety" in result["sub_scores"]
    assert "stability" in result["sub_scores"]
    assert "railing" in result["sub_scores"]
    assert "electrical_access" in result["sub_scores"]
    assert "ce_category" in result["sub_scores"]
    assert len(result["sub_scores"]) == 6
    assert "norm_versions" in result["config_used"]


def test_compliance_warnings_sorted():
    """Warnings should be sorted: critical -> warning -> info."""
    zones = [
        make_zone("cabin1", "cabin"),  # No cockpit -> critical escape warning
        make_zone("engine", "engine", polygon=[[0, 0], [500, 0], [500, 500], [0, 500]]),
    ]
    result = run_compliance_analysis(zones, [], "cruising_sail")
    severities = [w["severity"] for w in result["warnings"]]
    order = [SEVERITY_ORDER.get(s, 2) for s in severities]
    assert order == sorted(order)


def test_compliance_boat_class_difference():
    """Different boat classes produce different scores."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("cabin1", "cabin"),
        make_zone("engine", "engine"),
        make_zone("helm", "helm"),
        make_zone("salon", "salon"),
    ]
    passages = [
        make_passage("cockpit", "salon"),
        make_passage("salon", "cabin1"),
        make_passage("salon", "engine"),
    ]
    result_small = run_compliance_analysis(zones, passages, "small_sail")
    result_super = run_compliance_analysis(zones, passages, "superyacht")
    assert result_small["overall_score"] != result_super["overall_score"]


def test_compliance_config_overrides():
    """Config overrides are applied and stored in config_used."""
    zones = [make_zone("cockpit", "cockpit"), make_zone("cabin1", "cabin")]
    passages = [make_passage("cockpit", "cabin1")]
    result = run_compliance_analysis(zones, passages, "cruising_sail",
                                     config_overrides={"max_escape_hops": 2})
    assert result["config_used"]["max_escape_hops"] == 2


def test_compliance_empty_input():
    """Empty zones and passages -> degraded scores, no crash."""
    result = run_compliance_analysis([], [], "cruising_sail")
    assert 0 <= result["overall_score"] <= 100
    assert len(result["sub_scores"]) == 6
    assert len(result["warnings"]) > 0
