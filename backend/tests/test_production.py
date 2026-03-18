"""Tests for production friendliness analysis module — Tasks 1, 2, 3, 4 & 5."""
from tests.conftest import make_passage, make_zone

from app.services.analysis.production import (
    analyze_assembly_sequence,
    analyze_form_complexity,
    analyze_service_access,
    analyze_standardization,
    analyze_cable_routing,
    run_production_analysis,
    BOAT_CLASS_DEFAULTS,
    SEVERITY_ORDER,
)


def _default_config(boat_class: str = "cruising_sail") -> dict:
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


# ---------------------------------------------------------------------------
# analyze_assembly_sequence
# ---------------------------------------------------------------------------


def test_assembly_no_bottlenecks():
    """Ring topology — every zone has two paths to all others, no bottlenecks."""
    zones = [
        make_zone("A", "salon"),
        make_zone("B", "cabin"),
        make_zone("C", "pantry"),
        make_zone("D", "cockpit"),
    ]
    passages = [
        make_passage("A", "B"),
        make_passage("B", "C"),
        make_passage("C", "D"),
        make_passage("D", "A"),
    ]
    score, warnings, metrics = analyze_assembly_sequence(zones, passages, _default_config())
    assert score == 100.0
    assert metrics["bottleneck_count"] == 0


def test_assembly_one_bottleneck():
    """Linear chain A-B-C-D — B and C are bottlenecks."""
    zones = [
        make_zone("A", "salon"),
        make_zone("B", "cabin"),
        make_zone("C", "pantry"),
        make_zone("D", "cockpit"),
    ]
    passages = [
        make_passage("A", "B"),
        make_passage("B", "C"),
        make_passage("C", "D"),
    ]
    score, warnings, metrics = analyze_assembly_sequence(zones, passages, _default_config())
    assert score < 100.0
    assert metrics["bottleneck_count"] >= 1
    assert any(w["code"] == "MONTAGE_BOTTLENECK" for w in warnings)


def test_assembly_all_isolated():
    """Three zones, no passages — no connections, critical warning."""
    zones = [
        make_zone("X", "salon"),
        make_zone("Y", "cabin"),
        make_zone("Z", "pantry"),
    ]
    score, warnings, metrics = analyze_assembly_sequence(zones, [], _default_config())
    assert score == 0.0
    assert any(w["severity"] == "critical" for w in warnings)
    assert any(w["code"] == "MONTAGE_NO_CONNECTIONS" for w in warnings)


def test_assembly_no_zones():
    """Empty zones list — score 50, info warning."""
    score, warnings, metrics = analyze_assembly_sequence([], [], _default_config())
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
    assert any(w["code"] == "MONTAGE_NO_ZONES" for w in warnings)


def test_assembly_single_zone():
    """Single zone — trivially connected, score 100."""
    zones = [make_zone("Solo", "salon")]
    score, warnings, metrics = analyze_assembly_sequence(zones, [], _default_config())
    assert score == 100.0
    assert metrics["bottleneck_count"] == 0


# ---------------------------------------------------------------------------
# analyze_form_complexity
# ---------------------------------------------------------------------------


def test_form_all_right_angles():
    """Rectangle zones have only 90° angles — no sharp or reflex, score 100."""
    zones = [
        make_zone("Salon", "salon", polygon=[[0, 0], [4000, 0], [4000, 3000], [0, 3000]]),
        make_zone("Cabin", "cabin", polygon=[[0, 0], [2000, 0], [2000, 1500], [0, 1500]]),
    ]
    score, warnings, metrics = analyze_form_complexity(zones, _default_config())
    assert score == 100.0
    assert metrics["total_sharp_angles"] == 0
    assert metrics["total_reflex_angles"] == 0


def test_form_sharp_angles():
    """Thin triangle has one very sharp angle — score < 100, sharp >= 1."""
    # Triangle with a ~10° apex angle
    import math
    half_base = 100  # mm
    height = int(half_base / math.tan(math.radians(10)))
    polygon = [
        [0, 0],
        [2 * half_base, 0],
        [half_base, height],
    ]
    zones = [make_zone("Sharp", "salon", polygon=polygon)]
    score, warnings, metrics = analyze_form_complexity(zones, _default_config())
    assert score < 100.0
    assert metrics["total_sharp_angles"] >= 1
    assert any(w["code"] == "FORM_SHARP_ANGLE" for w in warnings)


def test_form_reflex_angle():
    """L-shape polygon has exactly one reflex (concave) vertex."""
    # CCW L-shape: [[0,0],[3000,0],[3000,1000],[1000,1000],[1000,3000],[0,3000]]
    polygon = [
        [0, 0],
        [3000, 0],
        [3000, 1000],
        [1000, 1000],
        [1000, 3000],
        [0, 3000],
    ]
    zones = [make_zone("LShape", "salon", polygon=polygon)]
    score, warnings, metrics = analyze_form_complexity(zones, _default_config())
    assert score < 100.0
    assert metrics["total_reflex_angles"] == 1
    assert any(w["code"] == "FORM_UNDERCUT" for w in warnings)


def test_form_no_zones():
    """Empty zones list — score 50, info warning."""
    score, warnings, metrics = analyze_form_complexity([], _default_config())
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
    assert any(w["code"] == "FORM_NO_ZONES" for w in warnings)


# ---------------------------------------------------------------------------
# analyze_service_access
# ---------------------------------------------------------------------------


def test_service_access_good():
    """Technical zones connected via wide passages -> high score."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("salon", "salon"),
        make_zone("head", "head"),
    ]
    passages = [
        make_passage("engine", "salon", width_mm=800),
        make_passage("head", "salon", width_mm=800),
    ]
    config = _default_config()  # min_service_access_mm = 600
    score, warnings, metrics = analyze_service_access(zones, passages, config)
    assert score >= 80.0
    assert metrics["accessible_count"] == 2


def test_service_access_narrow():
    """Technical zone connected but narrow passage -> partial score."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("salon", "salon"),
    ]
    passages = [make_passage("engine", "salon", width_mm=400)]
    config = _default_config()  # min_service_access_mm = 600
    score, warnings, metrics = analyze_service_access(zones, passages, config)
    assert score == 50.0
    assert any(w["severity"] == "warning" for w in warnings)


def test_service_access_inaccessible():
    """Technical zone with no passages -> critical, score 0."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("salon", "salon"),
    ]
    passages = []
    config = _default_config()
    score, warnings, metrics = analyze_service_access(zones, passages, config)
    assert score == 0.0
    assert any(w["severity"] == "critical" for w in warnings)
    assert metrics["accessible_count"] == 0


def test_service_access_no_technical():
    """No technical zones -> score 50, info."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_service_access(zones, [], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


# ---------------------------------------------------------------------------
# analyze_standardization
# ---------------------------------------------------------------------------


def test_standardization_all_standard():
    """All passages and cabins match standard sizes -> score 100."""
    zones = [
        make_zone("cabin1", "cabin", polygon=[[0, 0], [2000, 0], [2000, 700], [0, 700]]),
    ]
    passages = [make_passage("cabin1", "salon", width_mm=600)]
    config = _default_config()  # standard_door_widths_mm=[600,700], berth=700, tolerance=50
    score, warnings, metrics = analyze_standardization(zones, passages, config)
    assert score == 100.0
    assert metrics["passage_match_ratio"] == 1.0


def test_standardization_non_standard_passage():
    """Passage with non-standard width -> lower score."""
    zones = [
        make_zone("cabin1", "cabin", polygon=[[0, 0], [2000, 0], [2000, 700], [0, 700]]),
    ]
    passages = [make_passage("cabin1", "salon", width_mm=450)]
    config = _default_config()
    score, warnings, metrics = analyze_standardization(zones, passages, config)
    assert score < 100.0
    assert any(w["severity"] == "warning" for w in warnings)


def test_standardization_non_standard_berth():
    """Cabin with non-standard berth width -> lower score."""
    zones = [
        make_zone("cabin1", "cabin", polygon=[[0, 0], [2000, 0], [2000, 500], [0, 500]]),
    ]
    passages = [make_passage("cabin1", "salon", width_mm=600)]
    config = _default_config()
    score, warnings, metrics = analyze_standardization(zones, passages, config)
    assert score < 100.0
    assert any(w["severity"] == "warning" for w in warnings)


def test_standardization_no_data():
    """No passages and no cabins -> score 50, info."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_standardization(zones, [], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


# ---------------------------------------------------------------------------
# analyze_cable_routing
# ---------------------------------------------------------------------------


def test_cable_routing_clean():
    """All system connections route through technical zones -> score 100."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("helm", "helm"),
        make_zone("pantry", "pantry"),
        make_zone("head", "head"),
        make_zone("storage", "storage"),
    ]
    passages = [
        make_passage("engine", "storage"),
        make_passage("storage", "helm"),
        make_passage("storage", "pantry"),
        make_passage("storage", "head"),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_cable_routing(zones, passages, config)
    assert score == 100.0
    assert metrics["guest_crossings"] == 0


def test_cable_routing_through_guest():
    """System connection routes through salon -> lower score."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("salon", "salon"),
        make_zone("helm", "helm"),
        make_zone("pantry", "pantry"),
        make_zone("head", "head"),
    ]
    passages = [
        make_passage("engine", "salon"),
        make_passage("salon", "helm"),
        make_passage("salon", "pantry"),
        make_passage("salon", "head"),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_cable_routing(zones, passages, config)
    assert score < 100.0
    assert metrics["guest_crossings"] > 0
    assert any(w["severity"] == "warning" for w in warnings)


def test_cable_routing_no_path():
    """System zones not connected -> critical."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("helm", "helm"),
    ]
    passages = []
    config = _default_config()
    score, warnings, metrics = analyze_cable_routing(zones, passages, config)
    assert score < 50.0
    assert any(w["severity"] == "critical" for w in warnings)


def test_cable_routing_no_system_zones():
    """No system zones -> score 50, info."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_cable_routing(zones, [], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


# ---------------------------------------------------------------------------
# Integration
# ---------------------------------------------------------------------------


def test_full_production_analysis():
    """Complete layout -> valid result structure with all 5 sub-scores."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("salon", "salon", polygon=[[3000, 0], [7000, 0], [7000, 4000], [3000, 4000]]),
        make_zone("cabin1", "cabin", polygon=[[0, 0], [2000, 0], [2000, 700], [0, 700]]),
        make_zone("engine", "engine", polygon=[[7000, 1000], [9000, 1000], [9000, 3000], [7000, 3000]]),
        make_zone("helm", "helm"),
        make_zone("head", "head"),
        make_zone("pantry", "pantry"),
    ]
    passages = [
        make_passage("cockpit", "salon", width_mm=700),
        make_passage("salon", "cabin1", width_mm=600),
        make_passage("salon", "engine", width_mm=700),
        make_passage("salon", "helm", width_mm=600),
        make_passage("salon", "head", width_mm=600),
        make_passage("salon", "pantry", width_mm=600),
    ]
    result = run_production_analysis(zones, passages, "cruising_sail")
    assert result["module"] == "production"
    assert 0 <= result["overall_score"] <= 100
    assert "assembly_sequence" in result["sub_scores"]
    assert "form_complexity" in result["sub_scores"]
    assert "service_access" in result["sub_scores"]
    assert "standardization" in result["sub_scores"]
    assert "cable_routing" in result["sub_scores"]
    assert len(result["sub_scores"]) == 5


def test_production_warnings_sorted():
    """Warnings should be sorted: critical -> warning -> info."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("helm", "helm"),
    ]
    result = run_production_analysis(zones, [], "cruising_sail")
    severities = [w["severity"] for w in result["warnings"]]
    order = [SEVERITY_ORDER.get(s, 2) for s in severities]
    assert order == sorted(order)


def test_production_boat_class_difference():
    """Different boat classes produce different scores."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("salon", "salon"),
        make_zone("engine", "engine"),
        make_zone("helm", "helm"),
        make_zone("head", "head"),
        make_zone("cabin1", "cabin", polygon=[[0, 0], [2000, 0], [2000, 700], [0, 700]]),
    ]
    passages = [
        make_passage("cockpit", "salon", width_mm=600),
        make_passage("salon", "engine", width_mm=600),
        make_passage("salon", "helm", width_mm=600),
        make_passage("salon", "head", width_mm=600),
        make_passage("salon", "cabin1", width_mm=600),
    ]
    result_small = run_production_analysis(zones, passages, "small_sail")
    result_super = run_production_analysis(zones, passages, "superyacht")
    assert result_small["overall_score"] != result_super["overall_score"]


def test_production_config_overrides():
    """Config overrides are applied and stored in config_used."""
    zones = [make_zone("cockpit", "cockpit"), make_zone("cabin1", "cabin")]
    passages = [make_passage("cockpit", "cabin1")]
    result = run_production_analysis(zones, passages, "cruising_sail",
                                     config_overrides={"min_service_access_mm": 900})
    assert result["config_used"]["min_service_access_mm"] == 900


def test_production_empty_input():
    """Empty zones and passages -> degraded scores, no crash."""
    result = run_production_analysis([], [], "cruising_sail")
    assert 0 <= result["overall_score"] <= 100
    assert len(result["sub_scores"]) == 5
    assert len(result["warnings"]) > 0
