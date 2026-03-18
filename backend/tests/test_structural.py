"""Tests for structural analysis module (weight distribution)."""
from tests.conftest import make_zone
from app.services.analysis.structural import (
    analyze_fore_aft_balance,
    analyze_lateral_balance,
    analyze_heavy_zone_placement,
    analyze_load_concentration,
    BOAT_CLASS_DEFAULTS,
    run_structural_analysis,
    SEVERITY_ORDER,
)


def _default_config(boat_class="cruising_sail"):
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


# ---------------------------------------------------------------------------
# analyze_fore_aft_balance
# ---------------------------------------------------------------------------


def test_fore_aft_balanced():
    """CoG within ideal range -> score 100."""
    zones = [
        make_zone("salon", "salon", polygon=[[4000, 0], [6000, 0], [6000, 3000], [4000, 3000]]),
        make_zone("engine", "engine", polygon=[[4500, 0], [5500, 0], [5500, 1500], [4500, 1500]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_fore_aft_balance(zones, config)
    assert score == 100.0
    assert metrics["deviation_pct"] == 0.0
    assert 0.44 <= metrics["cog_x_pct"] <= 0.54


def test_fore_aft_too_far_aft():
    """Heavy zone at stern -> CoG too far aft, warning."""
    zones = [
        make_zone("cabin", "cabin", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
        make_zone("engine", "engine", polygon=[[8000, 0], [10000, 0], [10000, 2000], [8000, 2000]]),
        make_zone("storage", "storage", polygon=[[7000, 0], [9000, 0], [9000, 2000], [7000, 2000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_fore_aft_balance(zones, config)
    assert score < 100.0
    assert any(w["code"] == "COG_TOO_FAR_AFT" for w in warnings)
    assert metrics["cog_x_pct"] > 0.54


def test_fore_aft_too_far_forward():
    """Heavy zone at bow -> CoG too far forward, warning."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
        make_zone("cabin", "cabin", polygon=[[8000, 0], [10000, 0], [10000, 2000], [8000, 2000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_fore_aft_balance(zones, config)
    assert score < 100.0
    assert any(w["code"] == "COG_TOO_FAR_FORWARD" for w in warnings)
    assert metrics["cog_x_pct"] < 0.44


def test_fore_aft_no_zones():
    """No zones -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_fore_aft_balance([], config)
    assert score == 50.0
    assert any(w["code"] == "STRUCTURAL_NO_ZONES" and w["severity"] == "info" for w in warnings)


# ---------------------------------------------------------------------------
# analyze_lateral_balance
# ---------------------------------------------------------------------------


def test_lateral_centered():
    """Symmetric layout -> score 100."""
    zones = [
        make_zone("salon", "salon", polygon=[[4000, 500], [6000, 500], [6000, 2500], [4000, 2500]]),
        make_zone("engine", "engine", polygon=[[4000, 500], [6000, 500], [6000, 2500], [4000, 2500]]),
    ]
    config = _default_config()  # lateral_tolerance_pct = 0.05
    score, warnings, metrics = analyze_lateral_balance(zones, config)
    assert score == 100.0
    assert abs(metrics["offset_from_center_pct"]) < 0.01


def test_lateral_offset():
    """Asymmetric layout -> warning, lower score."""
    # Heavy engine on starboard (low Y), light salon on port (high Y)
    # Y span 0-4000, engine centroid Y=1000, salon centroid Y=3000
    # Weighted CoG_y ≈ 34%, offset ≈ 16% >> 5% tolerance
    zones = [
        make_zone("engine", "engine", polygon=[[4000, 0], [6000, 0], [6000, 2000], [4000, 2000]]),
        make_zone("salon", "salon", polygon=[[4000, 2000], [6000, 2000], [6000, 4000], [4000, 4000]]),
    ]
    config = _default_config()  # lateral_tolerance_pct = 0.05
    score, warnings, metrics = analyze_lateral_balance(zones, config)
    assert score < 100.0
    assert any(w["code"] == "COG_LATERAL_OFFSET" for w in warnings)


def test_lateral_no_zones():
    """No zones -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_lateral_balance([], config)
    assert score == 50.0
    assert any(w["code"] == "STRUCTURAL_NO_ZONES" and w["severity"] == "info" for w in warnings)


# ---------------------------------------------------------------------------
# analyze_heavy_zone_placement
# ---------------------------------------------------------------------------


def test_heavy_placement_central():
    """Heavy zones in central band -> score 100."""
    zones = [
        make_zone("engine", "engine", polygon=[[4000, 0], [6000, 0], [6000, 2000], [4000, 2000]]),
        make_zone("storage", "storage", polygon=[[3000, 0], [5000, 0], [5000, 1000], [3000, 1000]]),
        make_zone("salon", "salon", polygon=[[0, 0], [10000, 0], [10000, 3000], [0, 3000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_heavy_zone_placement(zones, config)
    assert score == 100.0
    assert metrics["central_ratio"] == 1.0


def test_heavy_placement_off_center():
    """Heavy zone at extreme position -> penalty."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [1000, 0], [1000, 1000], [0, 1000]]),
        make_zone("salon", "salon", polygon=[[0, 0], [10000, 0], [10000, 3000], [0, 3000]]),
    ]
    config = _default_config()  # central_band = (0.20, 0.80)
    score, warnings, metrics = analyze_heavy_zone_placement(zones, config)
    # Engine centroid at X=500 out of span 0-10000 = 5%, outside 20-80%
    assert score < 100.0
    assert any(w["code"] == "HEAVY_ZONE_OFF_CENTER" for w in warnings)


def test_heavy_placement_no_heavy_zones():
    """No heavy zones -> score 100, info."""
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [3000, 0], [3000, 2000], [0, 2000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_heavy_zone_placement(zones, config)
    assert score == 100.0
    assert any(w["code"] == "STRUCTURAL_NO_HEAVY_ZONES" for w in warnings)


def test_heavy_placement_no_zones():
    """No zones -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_heavy_zone_placement([], config)
    assert score == 50.0


# ---------------------------------------------------------------------------
# analyze_load_concentration
# ---------------------------------------------------------------------------


def test_load_even():
    """Evenly distributed zones with similar weights -> high score."""
    # Use zones with similar kg/m² to achieve balanced weight distribution
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
        make_zone("pantry", "pantry", polygon=[[4000, 0], [6000, 0], [6000, 2000], [4000, 2000]]),
        make_zone("cabin", "cabin", polygon=[[8000, 0], [10000, 0], [10000, 2000], [8000, 2000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_load_concentration(zones, config)
    assert score >= 70.0
    assert not any(w["code"] == "LOAD_CONCENTRATION_HIGH" for w in warnings)


def test_load_concentrated():
    """All weight in one segment -> warning, low score."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
        make_zone("storage", "storage", polygon=[[0, 0], [3000, 0], [3000, 1000], [0, 1000]]),
        make_zone("cabin", "cabin", polygon=[[0, 0], [10000, 0], [10000, 100], [0, 100]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_load_concentration(zones, config)
    assert score < 70.0
    assert any(w["code"] == "LOAD_CONCENTRATION_HIGH" for w in warnings)


def test_load_single_zone():
    """Single zone -> all weight in one segment, warning."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [3000, 0], [3000, 2000], [0, 2000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_load_concentration(zones, config)
    assert score < 50.0
    assert any(w["code"] == "LOAD_CONCENTRATION_HIGH" for w in warnings)


def test_load_no_zones():
    """No zones -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_load_concentration([], config)
    assert score == 50.0


# ---------------------------------------------------------------------------
# Integration
# ---------------------------------------------------------------------------


def test_full_structural_analysis():
    """Complete layout -> valid result structure with all 4 sub-scores."""
    zones = [
        make_zone("cockpit", "cockpit", polygon=[[0, 0], [3800, 0], [3800, 2500], [0, 2500]]),
        make_zone("salon", "salon", polygon=[[0, 2500], [3800, 2500], [3800, 5500], [0, 5500]]),
        make_zone("engine", "engine", polygon=[[1800, 0], [3800, 0], [3800, 1500], [1800, 1500]]),
        make_zone("cabin", "cabin", polygon=[[500, 7500], [3300, 7500], [3300, 10000], [500, 10000]]),
    ]
    result = run_structural_analysis(zones, [], "cruising_sail")
    assert result["module"] == "structural"
    assert 0 <= result["overall_score"] <= 100
    assert "fore_aft" in result["sub_scores"]
    assert "lateral" in result["sub_scores"]
    assert "heavy_placement" in result["sub_scores"]
    assert "load_concentration" in result["sub_scores"]
    assert len(result["sub_scores"]) == 4


def test_structural_warnings_sorted():
    """Warnings sorted: critical -> warning -> info."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [1000, 0], [1000, 500], [0, 500]]),
        make_zone("cabin", "cabin", polygon=[[0, 0], [10000, 0], [10000, 100], [0, 100]]),
    ]
    result = run_structural_analysis(zones, [], "cruising_sail")
    severities = [w["severity"] for w in result["warnings"]]
    order = [SEVERITY_ORDER.get(s, 2) for s in severities]
    assert order == sorted(order)


def test_structural_boat_class_difference():
    """Different boat classes produce different scores."""
    zones = [
        make_zone("salon", "salon", polygon=[[3000, 0], [7000, 0], [7000, 3000], [3000, 3000]]),
        make_zone("engine", "engine", polygon=[[4000, 0], [6000, 0], [6000, 1500], [4000, 1500]]),
    ]
    result_sail = run_structural_analysis(zones, [], "small_sail")
    result_motor = run_structural_analysis(zones, [], "large_motor")
    # Different ideal ranges -> different scores
    assert result_sail["overall_score"] != result_motor["overall_score"]


def test_structural_config_overrides():
    """Config overrides applied and stored in config_used."""
    zones = [make_zone("salon", "salon")]
    result = run_structural_analysis(zones, [], "cruising_sail",
                                     config_overrides={"lateral_tolerance_pct": 0.15})
    assert result["config_used"]["lateral_tolerance_pct"] == 0.15


def test_structural_empty_input():
    """No zones -> short-circuit: score 50, single STRUCTURAL_NO_ZONES warning."""
    result = run_structural_analysis([], [], "cruising_sail")
    assert result["overall_score"] == 50.0
    assert len(result["sub_scores"]) == 4
    assert all(v == 50.0 for v in result["sub_scores"].values())
    assert len(result["warnings"]) == 1
    assert result["warnings"][0]["code"] == "STRUCTURAL_NO_ZONES"


def test_structural_unknown_zone_type():
    """Unknown zone_type uses 50 kg/m² fallback and emits no warning."""
    zones = [
        make_zone("custom", "lounge", polygon=[[3000, 0], [7000, 0], [7000, 3000], [3000, 3000]]),
        make_zone("engine", "engine", polygon=[[4000, 0], [6000, 0], [6000, 1500], [4000, 1500]]),
    ]
    result = run_structural_analysis(zones, [], "cruising_sail")
    assert 0 <= result["overall_score"] <= 100
    # No warning about unknown zone type
    assert not any("unbekannt" in w.get("message", "").lower() for w in result["warnings"])


def test_structural_critical_severity_thresholds():
    """Extreme deviation triggers critical severity."""
    # Engine at bow extreme (X=0), light zone at stern — >10% deviation
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [3000, 0], [3000, 3000], [0, 3000]]),
        make_zone("foredeck", "foredeck", polygon=[[9000, 0], [12000, 0], [12000, 3000], [9000, 3000]]),
    ]
    result = run_structural_analysis(zones, [], "cruising_sail")
    critical_warnings = [w for w in result["warnings"] if w["severity"] == "critical"]
    assert len(critical_warnings) > 0
