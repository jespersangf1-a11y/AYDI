from tests.conftest import make_passage, make_zone

from app.services.analysis.emotional import (
    BOAT_CLASS_DEFAULTS,
    analyze_ceiling_perception,
    analyze_inside_outside_flow,
    analyze_light_distribution,
    analyze_room_proportion,
    analyze_sightline,
    analyze_visual_calm,
    run_emotional_analysis,
)


def _default_config(boat_class="cruising_sail"):
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


def test_emotional_module_exists():
    assert "small_sail" in BOAT_CLASS_DEFAULTS
    assert "cruising_sail" in BOAT_CLASS_DEFAULTS
    assert "large_motor" in BOAT_CLASS_DEFAULTS
    assert "superyacht" in BOAT_CLASS_DEFAULTS
    for bc, cfg in BOAT_CLASS_DEFAULTS.items():
        total = sum(cfg["weights"].values())
        assert abs(total - 1.0) < 0.001, f"{bc} weights sum to {total}"


# --- analyze_room_proportion ---

def test_room_proportion_good():
    """Zones with height and good proportions score high."""
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [3500, 0], [3500, 3000], [0, 3000]], height_mm=1950),
        make_zone("cabin", "cabin", polygon=[[0, 3000], [2500, 3000], [2500, 5000], [0, 5000]], height_mm=1950),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_room_proportion(zones, config)
    assert score >= 70.0
    assert metrics["zones_evaluated"] >= 1


def test_room_proportion_no_height():
    """No height data -> degraded score 50."""
    zones = [make_zone("salon", "salon"), make_zone("cabin", "cabin")]
    config = _default_config()
    score, warnings, metrics = analyze_room_proportion(zones, config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


def test_room_proportion_empty():
    """Empty zones -> 50.0."""
    config = _default_config()
    score, warnings, metrics = analyze_room_proportion([], config)
    assert score == 50.0


# --- analyze_light_distribution ---

def test_light_distribution_good():
    """Zones with adequate window ratios score high."""
    zones = [
        make_zone("salon", "salon", properties={"window_area_pct": 0.32}),
        make_zone("cabin", "cabin", properties={"window_area_pct": 0.20}),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_light_distribution(zones, config)
    assert score >= 80.0
    assert metrics["zones_evaluated"] == 2


def test_light_distribution_dark():
    """Low window ratio -> warning."""
    zones = [make_zone("salon", "salon", properties={"window_area_pct": 0.08})]
    config = _default_config()
    score, warnings, metrics = analyze_light_distribution(zones, config)
    assert score < 80.0
    assert len(warnings) > 0


def test_light_distribution_no_data():
    """No window data -> 50.0."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_light_distribution(zones, config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


# --- analyze_sightline ---

def test_sightline_spacious():
    """Large salon with long sightline -> good score."""
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [4000, 0], [4000, 3000], [0, 3000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_sightline(zones, config)
    assert score >= 80.0
    assert metrics["avg_sightline_m"] > 1.5


def test_sightline_cramped():
    """Tiny zone with short sightline -> low score."""
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [1000, 0], [1000, 800], [0, 800]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_sightline(zones, config)
    assert score < 80.0
    assert len(warnings) > 0


def test_sightline_empty():
    config = _default_config()
    score, warnings, metrics = analyze_sightline([], config)
    assert score == 50.0


# --- analyze_visual_calm ---

def test_visual_calm_ideal():
    """4 materials = ideal range -> 100."""
    zones = [make_zone("salon", "salon", properties={"material_count": 4})]
    config = _default_config()
    score, warnings, metrics = analyze_visual_calm(zones, config)
    assert score >= 90.0


def test_visual_calm_cluttered():
    """8+ materials -> warning."""
    zones = [make_zone("salon", "salon", properties={"material_count": 9})]
    config = _default_config()
    score, warnings, metrics = analyze_visual_calm(zones, config)
    assert score < 80.0
    assert len(warnings) > 0


def test_visual_calm_sterile():
    """1 material -> warning."""
    zones = [make_zone("salon", "salon", properties={"material_count": 1})]
    config = _default_config()
    score, warnings, metrics = analyze_visual_calm(zones, config)
    assert score < 80.0
    assert len(warnings) > 0


def test_visual_calm_no_data():
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_visual_calm(zones, config)
    assert score == 50.0


# --- analyze_ceiling_perception ---

def test_ceiling_good():
    """Standard height -> high score."""
    zones = [
        make_zone("salon", "salon", height_mm=1950),
        make_zone("cabin", "cabin", height_mm=1950),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_ceiling_perception(zones, config)
    assert score >= 80.0


def test_ceiling_low():
    """Below minimum -> warning."""
    zones = [make_zone("salon", "salon", height_mm=1700)]
    config = _default_config()
    score, warnings, metrics = analyze_ceiling_perception(zones, config)
    assert score < 70.0
    assert any(w["severity"] == "warning" for w in warnings)


def test_ceiling_no_data():
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_ceiling_perception(zones, config)
    assert score == 50.0


# --- analyze_inside_outside_flow ---

def test_inside_outside_flow_good():
    """Wide passage to cockpit -> high score."""
    zones = [make_zone("salon", "salon"), make_zone("cockpit", "cockpit")]
    passages = [make_passage("salon", "cockpit", 900)]
    config = _default_config()
    score, warnings, metrics = analyze_inside_outside_flow(zones, passages, config)
    assert score >= 80.0


def test_inside_outside_flow_narrow():
    """Narrow passage to cockpit -> lower score."""
    zones = [make_zone("salon", "salon"), make_zone("cockpit", "cockpit")]
    passages = [make_passage("salon", "cockpit", 500)]
    config = _default_config()
    score, warnings, metrics = analyze_inside_outside_flow(zones, passages, config)
    assert score < 80.0
    assert len(warnings) > 0


def test_inside_outside_flow_no_cockpit():
    """No cockpit zone -> degraded score."""
    zones = [make_zone("salon", "salon")]
    passages = []
    config = _default_config()
    score, warnings, metrics = analyze_inside_outside_flow(zones, passages, config)
    assert score < 60.0


# --- Full orchestrator ---

def test_full_emotional_analysis():
    zones = [
        make_zone("salon", "salon", height_mm=1950,
                  polygon=[[0, 0], [3500, 0], [3500, 3000], [0, 3000]],
                  properties={"window_area_pct": 0.32, "material_count": 4}),
        make_zone("cabin", "cabin", height_mm=1950,
                  polygon=[[0, 3000], [2500, 3000], [2500, 5000], [0, 5000]],
                  properties={"window_area_pct": 0.20, "material_count": 3}),
        make_zone("cockpit", "cockpit",
                  polygon=[[0, 5000], [3500, 5000], [3500, 7000], [0, 7000]]),
    ]
    passages = [
        make_passage("salon", "cabin", 750),
        make_passage("salon", "cockpit", 850),
    ]
    result = run_emotional_analysis(zones, passages, "cruising_sail")
    assert result["module"] == "emotional"
    assert 0 <= result["overall_score"] <= 100
    assert len(result["sub_scores"]) == 7
    assert "room_proportion" in result["sub_scores"]
    assert "ceiling_perception" in result["sub_scores"]
    assert "inside_outside_flow" in result["sub_scores"]


def test_emotional_warnings_sorted():
    """Warnings must be sorted by severity: critical > warning > info."""
    zones = [
        make_zone("salon", "salon", height_mm=1700,
                  polygon=[[0, 0], [1000, 0], [1000, 800], [0, 800]],
                  properties={"window_area_pct": 0.05, "material_count": 9}),
    ]
    passages = []
    result = run_emotional_analysis(zones, passages, "cruising_sail")
    severities = [w["severity"] for w in result["warnings"]]
    severity_order = {"critical": 0, "warning": 1, "info": 2}
    severity_values = [severity_order.get(s, 2) for s in severities]
    assert severity_values == sorted(severity_values), f"Warnings not sorted: {severities}"


def test_emotional_boat_class_difference():
    zones = [
        make_zone("salon", "salon", height_mm=1950,
                  polygon=[[0, 0], [3500, 0], [3500, 3000], [0, 3000]],
                  properties={"window_area_pct": 0.25, "material_count": 4}),
        make_zone("cockpit", "cockpit",
                  polygon=[[0, 3000], [3500, 3000], [3500, 5000], [0, 5000]]),
    ]
    passages = [make_passage("salon", "cockpit", 700)]
    result_small = run_emotional_analysis(zones, passages, "small_sail")
    result_super = run_emotional_analysis(zones, passages, "superyacht")
    assert result_small["overall_score"] != result_super["overall_score"]


def test_emotional_config_overrides():
    zones = [make_zone("salon", "salon", height_mm=1950)]
    passages = []
    result = run_emotional_analysis(zones, passages, "cruising_sail",
                                     config_overrides={"min_ceiling_mm": 1500})
    assert result["config_used"]["min_ceiling_mm"] == 1500
