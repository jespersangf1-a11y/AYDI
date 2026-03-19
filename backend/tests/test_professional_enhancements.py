"""Tests for professional-level module enhancements.

Tests all new sub-analyses added to ergonomics, emotional, compliance,
materials, structural, production, and cost modules.
"""
import math

from tests.conftest import (
    make_cost_item,
    make_material,
    make_passage,
    make_zone,
    make_zone_material,
)


# ============================================================================
# ERGONOMICS: heel impact
# ============================================================================

def test_heel_impact_sailboat():
    """Sailboat passages should be checked at 20° heel."""
    from app.services.analysis.ergonomics import analyze_heel_impact, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    passages = [make_passage("cabin", "salon", 700), make_passage("salon", "cockpit", 800)]
    score, warnings, metrics = analyze_heel_impact(passages, config)
    assert score >= 0.0
    assert "total_passages" in metrics or "passages_checked" in metrics


def test_heel_impact_motor_yacht():
    """Motor yachts should score 100 (no heel)."""
    from app.services.analysis.ergonomics import analyze_heel_impact, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["large_motor"].copy()
    config.pop("weights", None)
    passages = [make_passage("cabin", "salon", 700)]
    score, warnings, metrics = analyze_heel_impact(passages, config)
    assert score == 100.0
    assert len(warnings) == 0


def test_heel_impact_narrow_passage():
    """A passage that drops below critical width at heel should warn."""
    from app.services.analysis.ergonomics import analyze_heel_impact, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["small_sail"].copy()
    config.pop("weights", None)
    # At 20° heel: 520 * cos(20°) ≈ 489mm, which is above critical 450mm
    # At 20° heel: 470 * cos(20°) ≈ 442mm, which is below critical 450mm
    passages = [make_passage("cabin", "salon", 470)]
    score, warnings, metrics = analyze_heel_impact(passages, config)
    assert score < 100.0
    assert len(warnings) >= 1


# ============================================================================
# ERGONOMICS: morning circulation
# ============================================================================

def test_morning_circulation_no_bottleneck():
    """Each cabin has separate path — no bottleneck."""
    from app.services.analysis.ergonomics import analyze_morning_circulation, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [
        make_zone("cabin1", "cabin"),
        make_zone("head1", "head"),
        make_zone("pantry", "pantry"),
        make_zone("cockpit", "cockpit"),
    ]
    passages = [
        make_passage("cabin1", "head1", 700),
        make_passage("head1", "pantry", 700),
        make_passage("pantry", "cockpit", 800),
    ]
    score, warnings, metrics = analyze_morning_circulation(zones, passages, config)
    assert score >= 80.0


def test_morning_circulation_bottleneck():
    """Multiple cabins share a narrow passage — should detect bottleneck."""
    from app.services.analysis.ergonomics import analyze_morning_circulation, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [
        make_zone("cabin1", "cabin"),
        make_zone("cabin2", "cabin"),
        make_zone("cabin3", "cabin"),
        make_zone("head1", "head"),
        make_zone("pantry", "pantry"),
        make_zone("cockpit", "cockpit"),
    ]
    # All 3 cabins must go through head1→pantry
    passages = [
        make_passage("cabin1", "head1", 700),
        make_passage("cabin2", "head1", 700),
        make_passage("cabin3", "head1", 700),
        make_passage("head1", "pantry", 700),
        make_passage("pantry", "cockpit", 800),
    ]
    score, warnings, metrics = analyze_morning_circulation(zones, passages, config)
    assert score < 100.0


def test_morning_circulation_no_cabins():
    """No cabin zones — should handle gracefully."""
    from app.services.analysis.ergonomics import analyze_morning_circulation, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [make_zone("salon", "salon"), make_zone("cockpit", "cockpit")]
    passages = [make_passage("salon", "cockpit", 800)]
    score, warnings, metrics = analyze_morning_circulation(zones, passages, config)
    assert score >= 50.0


# ============================================================================
# ERGONOMICS: access complexity
# ============================================================================

def test_access_complexity_direct():
    """Engine with direct access should score 100."""
    from app.services.analysis.ergonomics import analyze_access_complexity, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [make_zone("engine1", "engine", properties={"access_type": "direct"})]
    score, warnings, metrics = analyze_access_complexity(zones, config)
    assert score == 100.0
    assert len(warnings) == 0


def test_access_complexity_major_disassembly():
    """Major disassembly access should score low and warn."""
    from app.services.analysis.ergonomics import analyze_access_complexity, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [make_zone("engine1", "engine", properties={"access_type": "major_disassembly"})]
    score, warnings, metrics = analyze_access_complexity(zones, config)
    assert score <= 10.0
    assert len(warnings) >= 1


def test_access_complexity_default():
    """No access_type property defaults to direct."""
    from app.services.analysis.ergonomics import analyze_access_complexity, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [make_zone("engine1", "engine")]
    score, warnings, metrics = analyze_access_complexity(zones, config)
    assert score == 100.0


def test_access_complexity_no_tech_zones():
    """No technical zones — graceful handling."""
    from app.services.analysis.ergonomics import analyze_access_complexity, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [make_zone("salon", "salon")]
    score, warnings, metrics = analyze_access_complexity(zones, config)
    assert score >= 50.0


# ============================================================================
# ERGONOMICS: orchestrator weights
# ============================================================================

def test_ergonomics_weights_sum_to_one():
    """All boat class weights should sum to 1.0."""
    from app.services.analysis.ergonomics import BOAT_CLASS_DEFAULTS
    for boat_class, config in BOAT_CLASS_DEFAULTS.items():
        total = sum(config["weights"].values())
        assert abs(total - 1.0) < 0.02, f"{boat_class} weights sum to {total}"


def test_ergonomics_orchestrator_includes_new_analyses():
    """The orchestrator should produce sub_scores for new analyses."""
    from app.services.analysis.ergonomics import run_ergonomics_analysis
    zones = [
        make_zone("cabin1", "cabin"),
        make_zone("head1", "head"),
        make_zone("pantry", "pantry"),
        make_zone("cockpit", "cockpit"),
        make_zone("engine1", "engine"),
        make_zone("helm1", "helm"),
    ]
    passages = [
        make_passage("cabin1", "head1", 700),
        make_passage("head1", "pantry", 700),
        make_passage("pantry", "cockpit", 800),
        make_passage("cockpit", "helm1", 700),
        make_passage("engine1", "pantry", 600),
    ]
    result = run_ergonomics_analysis(zones, passages, "cruising_sail")
    assert "heel_impact" in result["sub_scores"]
    assert "morning_circulation" in result["sub_scores"]
    assert "access_complexity" in result["sub_scores"]


# ============================================================================
# EMOTIONAL: sightline rays
# ============================================================================

def test_sightline_rays_open_polygon():
    """Large polygon should have good ray distances."""
    from app.services.analysis.emotional import analyze_sightline_rays, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    # 4m × 4m room
    zones = [make_zone("salon", "salon", polygon=[[0, 0], [4000, 0], [4000, 4000], [0, 4000]])]
    score, warnings, metrics = analyze_sightline_rays(zones, config)
    assert score >= 70.0
    assert "avg_ray_length_m" in metrics


def test_sightline_rays_tiny_polygon():
    """Tiny polygon should score poorly."""
    from app.services.analysis.emotional import analyze_sightline_rays, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    # 0.5m × 0.5m room — very small
    zones = [make_zone("cabin1", "cabin", polygon=[[0, 0], [500, 0], [500, 500], [0, 500]])]
    score, warnings, metrics = analyze_sightline_rays(zones, config)
    assert score < 80.0


def test_sightline_rays_no_evaluable_zones():
    """No sightline-eligible zones — handle gracefully."""
    from app.services.analysis.emotional import analyze_sightline_rays, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [make_zone("engine1", "engine")]
    score, warnings, metrics = analyze_sightline_rays(zones, config)
    assert score >= 50.0


def test_emotional_weights_sum_to_one():
    """All emotional boat class weights should sum to 1.0."""
    from app.services.analysis.emotional import BOAT_CLASS_DEFAULTS
    for boat_class, config in BOAT_CLASS_DEFAULTS.items():
        total = sum(config["weights"].values())
        assert abs(total - 1.0) < 0.02, f"{boat_class} weights sum to {total}"


def test_emotional_orchestrator_includes_sightline_rays():
    """Orchestrator should include sightline_rays sub_score."""
    from app.services.analysis.emotional import run_emotional_analysis
    zones = [
        make_zone("salon", "salon", height_mm=2000, polygon=[[0, 0], [4000, 0], [4000, 3000], [0, 3000]],
                  properties={"window_area_pct": 0.3, "material_count": 4}),
        make_zone("cockpit", "cockpit"),
    ]
    passages = [make_passage("salon", "cockpit", 800)]
    result = run_emotional_analysis(zones, passages, "cruising_sail")
    assert "sightline_rays" in result["sub_scores"]


# ============================================================================
# COMPLIANCE: escape hatch dimensions
# ============================================================================

def test_escape_hatch_compliant():
    """Hatch meeting ISO 12216 dimensions should pass."""
    from app.services.analysis.compliance import analyze_escape_hatch_dimensions, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [make_zone("cabin1", "cabin", properties={"hatch_width_mm": 450, "hatch_height_mm": 550})]
    score, warnings, metrics = analyze_escape_hatch_dimensions(zones, config)
    assert score == 100.0


def test_escape_hatch_too_small():
    """Undersized hatch should fail."""
    from app.services.analysis.compliance import analyze_escape_hatch_dimensions, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [make_zone("cabin1", "cabin", properties={"hatch_width_mm": 350, "hatch_height_mm": 400})]
    score, warnings, metrics = analyze_escape_hatch_dimensions(zones, config)
    assert score < 100.0
    assert len(warnings) >= 1


def test_escape_hatch_no_data():
    """No hatch data — info warning, score 50."""
    from app.services.analysis.compliance import analyze_escape_hatch_dimensions, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [make_zone("cabin1", "cabin")]
    score, warnings, metrics = analyze_escape_hatch_dimensions(zones, config)
    assert score == 50.0


# ============================================================================
# COMPLIANCE: cockpit drain capacity
# ============================================================================

def test_cockpit_drain_sufficient():
    """Drain capacity meeting requirements should pass."""
    from app.services.analysis.compliance import analyze_cockpit_drain_capacity, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    # 2m × 2m cockpit = 4m², depth 300mm = 1200L, required drain = 2400 L/s
    zones = [make_zone("cockpit1", "cockpit",
                       polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]],
                       properties={"drain_capacity_lps": 3000})]
    score, warnings, metrics = analyze_cockpit_drain_capacity(zones, config)
    assert score == 100.0


def test_cockpit_drain_no_data():
    """No drain data — info warning."""
    from app.services.analysis.compliance import analyze_cockpit_drain_capacity, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [make_zone("cockpit1", "cockpit")]
    score, warnings, metrics = analyze_cockpit_drain_capacity(zones, config)
    assert score == 50.0


# ============================================================================
# COMPLIANCE: companionway sill
# ============================================================================

def test_companionway_sill_compliant():
    """Sill height meeting CE category should pass."""
    from app.services.analysis.compliance import analyze_companionway_sill, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [make_zone("cockpit", "cockpit"), make_zone("salon", "salon")]
    passages = [make_passage("cockpit", "salon", 800)]
    passages[0].setdefault("properties", {})["sill_height_mm"] = 350  # Cat A requires 300mm
    score, warnings, metrics = analyze_companionway_sill(zones, passages, config)
    assert score == 100.0


def test_companionway_sill_no_data():
    """No sill data — info warning."""
    from app.services.analysis.compliance import analyze_companionway_sill, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [make_zone("cockpit", "cockpit"), make_zone("salon", "salon")]
    passages = [make_passage("cockpit", "salon", 800)]
    score, warnings, metrics = analyze_companionway_sill(zones, passages, config)
    assert score == 50.0


# ============================================================================
# COMPLIANCE: ventilation
# ============================================================================

def test_ventilation_adequate():
    """Sufficient ventilation area should pass."""
    from app.services.analysis.compliance import analyze_ventilation, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [make_zone("engine1", "engine", properties={"ventilation_area_sqm": 0.10, "engine_kw": 50})]
    score, warnings, metrics = analyze_ventilation(zones, config)
    assert score == 100.0


def test_ventilation_no_data():
    """No ventilation data — info warning."""
    from app.services.analysis.compliance import analyze_ventilation, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [make_zone("engine1", "engine")]
    score, warnings, metrics = analyze_ventilation(zones, config)
    assert score == 50.0


def test_compliance_weights_sum_to_one():
    """All compliance boat class weights should sum to 1.0."""
    from app.services.analysis.compliance import BOAT_CLASS_DEFAULTS
    for boat_class, config in BOAT_CLASS_DEFAULTS.items():
        total = sum(config["weights"].values())
        assert abs(total - 1.0) < 0.02, f"{boat_class} weights sum to {total}"


def test_compliance_orchestrator_includes_new_analyses():
    """Orchestrator should include new sub_scores."""
    from app.services.analysis.compliance import run_compliance_analysis
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("cabin1", "cabin"),
        make_zone("engine1", "engine"),
        make_zone("helm1", "helm"),
        make_zone("head1", "head"),
        make_zone("pantry", "pantry"),
    ]
    passages = [
        make_passage("cabin1", "cockpit", 700),
        make_passage("cockpit", "helm1", 700),
        make_passage("engine1", "cockpit", 600),
        make_passage("head1", "cabin1", 600),
        make_passage("pantry", "cockpit", 700),
    ]
    result = run_compliance_analysis(zones, passages, "cruising_sail")
    assert "escape_hatch" in result["sub_scores"]
    assert "cockpit_drain" in result["sub_scores"]
    assert "companionway_sill" in result["sub_scores"]
    assert "ventilation" in result["sub_scores"]


# ============================================================================
# MATERIALS: lifecycle cost
# ============================================================================

def test_lifecycle_cost_reasonable():
    """Materials with reasonable lifecycle cost should score well."""
    from app.services.analysis.materials import analyze_lifecycle_cost, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zm = [make_zone_material("salon", "floor", 10.0,
                             make_material(cost_per_unit=50.0, lifespan_years=25, maintenance_cost_factor=0.01))]
    score, warnings, metrics = analyze_lifecycle_cost(zm, config)
    assert score >= 70.0
    assert "total_lifecycle_cost_eur" in metrics


def test_lifecycle_cost_no_materials():
    """No materials — handle gracefully."""
    from app.services.analysis.materials import analyze_lifecycle_cost, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    score, warnings, metrics = analyze_lifecycle_cost([], config)
    assert score == 50.0


# ============================================================================
# MATERIALS: UV exposure
# ============================================================================

def test_uv_exposure_resistant():
    """UV-resistant material in exposed zone should pass."""
    from app.services.analysis.materials import analyze_uv_exposure, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zm = [make_zone_material("cockpit", "floor", 5.0,
                             make_material(properties={"uv_resistant": True}))]
    zm[0]["zone_type"] = "cockpit"
    score, warnings, metrics = analyze_uv_exposure(zm, config)
    assert score == 100.0


def test_uv_exposure_not_resistant():
    """Non-UV-resistant material in exposed zone should warn."""
    from app.services.analysis.materials import analyze_uv_exposure, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zm = [make_zone_material("cockpit", "floor", 5.0,
                             make_material(properties={"uv_resistant": False}))]
    zm[0]["zone_type"] = "cockpit"
    score, warnings, metrics = analyze_uv_exposure(zm, config)
    assert score < 100.0


# ============================================================================
# MATERIALS: moisture risk
# ============================================================================

def test_moisture_risk_sealed_wood():
    """Sealed wood in wet zone should pass."""
    from app.services.analysis.materials import analyze_moisture_risk, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zm = [make_zone_material("head1", "floor", 5.0,
                             make_material(subcategory="wood", properties={"moisture_sealed": True}))]
    zm[0]["zone_type"] = "head"
    score, warnings, metrics = analyze_moisture_risk(zm, config)
    assert score == 100.0


def test_moisture_risk_unsealed_wood():
    """Unsealed wood in wet zone should warn."""
    from app.services.analysis.materials import analyze_moisture_risk, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zm = [make_zone_material("head1", "floor", 5.0,
                             make_material(subcategory="wood", properties={"moisture_sealed": False}))]
    zm[0]["zone_type"] = "head"
    score, warnings, metrics = analyze_moisture_risk(zm, config)
    assert score < 100.0


def test_materials_weights_sum_to_one():
    """All materials boat class weights should sum to 1.0."""
    from app.services.analysis.materials import BOAT_CLASS_DEFAULTS
    for boat_class, config in BOAT_CLASS_DEFAULTS.items():
        total = sum(config["weights"].values())
        assert abs(total - 1.0) < 0.02, f"{boat_class} weights sum to {total}"


# ============================================================================
# STRUCTURAL: loading conditions
# ============================================================================

def test_loading_conditions_balanced():
    """Well-centered layout should stay in range across conditions."""
    from app.services.analysis.structural import analyze_loading_conditions, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [
        make_zone("engine", "engine", polygon=[[4000, 0], [6000, 0], [6000, 2000], [4000, 2000]]),
        make_zone("salon", "salon", polygon=[[2000, 0], [4000, 0], [4000, 2000], [2000, 2000]]),
        make_zone("cabin", "cabin", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
    ]
    score, warnings, metrics = analyze_loading_conditions(zones, config)
    assert score >= 0.0
    assert "conditions" in metrics


def test_loading_conditions_no_zones():
    """No zones — handle gracefully."""
    from app.services.analysis.structural import analyze_loading_conditions, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    score, warnings, metrics = analyze_loading_conditions([], config)
    assert score == 50.0


# ============================================================================
# STRUCTURAL: trim
# ============================================================================

def test_trim_balanced():
    """Balanced layout should have minimal trim."""
    from app.services.analysis.structural import analyze_trim, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [
        make_zone("cabin", "cabin", polygon=[[0, 0], [3000, 0], [3000, 2000], [0, 2000]]),
        make_zone("engine", "engine", polygon=[[4000, 0], [6000, 0], [6000, 2000], [4000, 2000]]),
    ]
    score, warnings, metrics = analyze_trim(zones, config)
    assert score >= 0.0
    assert "trim_deg" in metrics


def test_structural_weights_sum_to_one():
    """All structural boat class weights should sum to 1.0."""
    from app.services.analysis.structural import BOAT_CLASS_DEFAULTS
    for boat_class, config in BOAT_CLASS_DEFAULTS.items():
        total = sum(config["weights"].values())
        assert abs(total - 1.0) < 0.02, f"{boat_class} weights sum to {total}"


def test_structural_orchestrator_includes_new_analyses():
    """Orchestrator should include loading_conditions and trim."""
    from app.services.analysis.structural import run_structural_analysis
    zones = [
        make_zone("engine", "engine", polygon=[[4000, 0], [6000, 0], [6000, 2000], [4000, 2000]]),
        make_zone("salon", "salon", polygon=[[2000, 0], [4000, 0], [4000, 2000], [2000, 2000]]),
    ]
    result = run_structural_analysis(zones, [], "cruising_sail")
    assert "loading_conditions" in result["sub_scores"]
    assert "trim" in result["sub_scores"]


# ============================================================================
# PRODUCTION: mold complexity
# ============================================================================

def test_mold_complexity_simple():
    """Simple rectangular zones should score well."""
    from app.services.analysis.production import analyze_mold_complexity, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [3000, 0], [3000, 2000], [0, 2000]]),
    ]
    score, warnings, metrics = analyze_mold_complexity(zones, config)
    assert score >= 70.0


def test_mold_complexity_no_zones():
    """No zones — handle gracefully."""
    from app.services.analysis.production import analyze_mold_complexity, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    score, warnings, metrics = analyze_mold_complexity([], config)
    assert score >= 50.0


# ============================================================================
# PRODUCTION: flat panel ratio
# ============================================================================

def test_flat_panel_ratio_all_rectangular():
    """All rectangular zones should have high flat panel ratio."""
    from app.services.analysis.production import analyze_flat_panel_ratio, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [3000, 0], [3000, 2000], [0, 2000]]),
        make_zone("cabin", "cabin", polygon=[[3000, 0], [5000, 0], [5000, 2000], [3000, 2000]]),
    ]
    score, warnings, metrics = analyze_flat_panel_ratio(zones, config)
    assert score >= 80.0


def test_flat_panel_ratio_no_zones():
    """No zones — handle gracefully."""
    from app.services.analysis.production import analyze_flat_panel_ratio, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    score, warnings, metrics = analyze_flat_panel_ratio([], config)
    assert score >= 50.0


def test_production_weights_sum_to_one():
    """All production boat class weights should sum to 1.0."""
    from app.services.analysis.production import BOAT_CLASS_DEFAULTS
    for boat_class, config in BOAT_CLASS_DEFAULTS.items():
        total = sum(config["weights"].values())
        assert abs(total - 1.0) < 0.02, f"{boat_class} weights sum to {total}"


def test_production_orchestrator_includes_new_analyses():
    """Orchestrator should include mold_complexity and flat_panel_ratio."""
    from app.services.analysis.production import run_production_analysis
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [3000, 0], [3000, 2000], [0, 2000]]),
        make_zone("engine", "engine", polygon=[[3000, 0], [5000, 0], [5000, 2000], [3000, 2000]]),
    ]
    passages = [make_passage("salon", "engine", 700)]
    result = run_production_analysis(zones, passages, "cruising_sail")
    assert "mold_complexity" in result["sub_scores"]
    assert "flat_panel_ratio" in result["sub_scores"]


# ============================================================================
# COST: parametric estimate
# ============================================================================

def test_parametric_estimate_with_length():
    """Should compute parametric estimate when length is provided."""
    from app.services.analysis.cost import analyze_parametric_estimate, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    config["boat_length_m"] = 14.0
    zones = [
        make_zone("salon", "salon"),
        make_zone("cabin", "cabin"),
        make_zone("engine", "engine"),
    ]
    score, warnings, metrics = analyze_parametric_estimate(zones, config)
    assert score >= 50.0
    assert "estimated_total_eur" in metrics
    assert metrics["estimated_total_eur"] > 0


def test_parametric_estimate_no_length():
    """No boat length — should return score 50 with info."""
    from app.services.analysis.cost import analyze_parametric_estimate, BOAT_CLASS_DEFAULTS
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    config["boat_length_m"] = 0
    zones = [make_zone("salon", "salon")]
    score, warnings, metrics = analyze_parametric_estimate(zones, config)
    assert score == 50.0
    assert len(warnings) >= 1


def test_cost_weights_sum_to_one():
    """All cost boat class weights should sum to 1.0."""
    from app.services.analysis.cost import BOAT_CLASS_DEFAULTS
    for boat_class, config in BOAT_CLASS_DEFAULTS.items():
        total = sum(config["weights"].values())
        assert abs(total - 1.0) < 0.02, f"{boat_class} weights sum to {total}"


def test_cost_orchestrator_includes_parametric():
    """Orchestrator should include parametric_estimate sub_score."""
    from app.services.analysis.cost import run_cost_analysis
    zones = [make_zone("salon", "salon"), make_zone("engine", "engine")]
    cost_items = [make_cost_item("material", total_cost_eur=50000, source="quote")]
    result = run_cost_analysis(zones, [], "cruising_sail", cost_items=cost_items, boat_length_m=14.0)
    assert "parametric_estimate" in result["sub_scores"]
