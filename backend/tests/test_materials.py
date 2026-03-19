"""Tests for material & quality analysis module."""
from tests.conftest import make_material, make_zone_material
from app.services.analysis.materials import (
    analyze_material_durability,
    analyze_maintenance_burden,
    BOAT_CLASS_DEFAULTS,
)


def _default_config(boat_class="cruising_sail"):
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


# ---------------------------------------------------------------------------
# analyze_material_durability
# ---------------------------------------------------------------------------


def test_durability_all_long_lived():
    """All materials outlast min lifespan -> score 100."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(lifespan_years=25)),
        make_zone_material("cabin", "wall", 8.0, make_material(lifespan_years=30)),
    ]
    config = _default_config()  # min_lifespan_years = 20
    score, warnings, metrics = analyze_material_durability(zone_mats, config)
    assert score == 100.0
    assert metrics["compliant_count"] == 2


def test_durability_short_lived():
    """Material with lifespan below min -> warning, lower score."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(lifespan_years=10)),
        make_zone_material("cabin", "wall", 8.0, make_material(lifespan_years=25)),
    ]
    config = _default_config()  # min_lifespan_years = 20
    score, warnings, metrics = analyze_material_durability(zone_mats, config)
    assert score < 100.0
    assert any(w["severity"] == "warning" for w in warnings)
    assert any(w["code"] == "MATERIAL_SHORT_LIFE" for w in warnings)
    assert metrics["compliant_count"] == 1


def test_durability_no_lifespan_data():
    """Material without lifespan_years -> info warning."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(lifespan_years=None)),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_material_durability(zone_mats, config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


def test_durability_no_materials():
    """No material assignments -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_material_durability([], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


# ---------------------------------------------------------------------------
# analyze_maintenance_burden
# ---------------------------------------------------------------------------


def test_maintenance_low():
    """Low maintenance cost -> score 100."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0,
            make_material(cost_per_unit=100.0, maintenance_cost_factor=0.01)),
    ]
    config = _default_config()  # max_annual_maintenance_pct = 0.025
    score, warnings, metrics = analyze_maintenance_burden(zone_mats, config)
    assert score >= 80.0
    assert metrics["annual_maintenance_eur"] > 0


def test_maintenance_high():
    """High maintenance cost -> warning, lower score."""
    zone_mats = [
        make_zone_material("salon", "floor", 50.0,
            make_material(cost_per_unit=200.0, maintenance_cost_factor=0.10)),
    ]
    config = _default_config()  # max_annual_maintenance_pct = 0.025
    score, warnings, metrics = analyze_maintenance_burden(zone_mats, config)
    assert score < 80.0
    assert any(w["code"] == "MAINTENANCE_HIGH" for w in warnings)


def test_maintenance_no_materials():
    """No materials -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_maintenance_burden([], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


from app.services.analysis.materials import (
    analyze_known_issues,
    analyze_material_compatibility,
    analyze_material_weight,
)


# ---------------------------------------------------------------------------
# analyze_known_issues
# ---------------------------------------------------------------------------


def test_known_issues_none():
    """Materials with no known issues -> score 100."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(known_issues=[])),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_known_issues(zone_mats, config)
    assert score == 100.0
    assert metrics["total_issues"] == 0


def test_known_issues_critical():
    """Material with critical known issue -> low score."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(
            known_issues=[{"issue": "Delamination bei Feuchtigkeit", "severity": "critical"}],
        )),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_known_issues(zone_mats, config)
    assert score < 70.0
    assert any(w["code"] == "KNOWN_ISSUE_CRITICAL" for w in warnings)


def test_known_issues_medium():
    """Material with medium known issue -> partial score reduction."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(
            known_issues=[{"issue": "Verfärbung nach 5 Jahren", "severity": "medium"}],
        )),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_known_issues(zone_mats, config)
    assert score < 100.0
    assert score >= 70.0
    assert any(w["code"] == "KNOWN_ISSUE_MEDIUM" for w in warnings)


def test_known_issues_no_materials():
    """No materials -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_known_issues([], config)
    assert score == 50.0


# ---------------------------------------------------------------------------
# analyze_material_compatibility
# ---------------------------------------------------------------------------


def test_compatibility_ok():
    """Non-metal materials in same zone -> no issues."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(subcategory="wood")),
        make_zone_material("salon", "wall", 8.0, make_material(subcategory="composite")),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_material_compatibility(zone_mats, config)
    assert score == 100.0
    assert metrics["incompatibility_count"] == 0


def test_compatibility_galvanic():
    """Two different metals in same zone -> galvanic corrosion warning."""
    zone_mats = [
        make_zone_material("engine_room", "wall", 5.0, make_material(
            name="Alu-Platte", subcategory="metal",
            properties={"metal_type": "aluminum"},
        )),
        make_zone_material("engine_room", "ceiling", 5.0, make_material(
            name="Edelstahl-Verkleidung", subcategory="metal",
            properties={"metal_type": "stainless_steel"},
        )),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_material_compatibility(zone_mats, config)
    assert score < 100.0
    assert any(w["code"] == "MATERIAL_INCOMPATIBLE" for w in warnings)
    assert metrics["incompatibility_count"] >= 1


def test_compatibility_no_materials():
    """No materials -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_material_compatibility([], config)
    assert score == 50.0


# ---------------------------------------------------------------------------
# analyze_material_weight
# ---------------------------------------------------------------------------


def test_weight_normal():
    """Normal weight materials -> score 100."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(
            properties={"density_kg_m3": 650, "thickness_mm": 20},
        )),
    ]
    config = _default_config()  # max_zone_weight_kg_sqm = 30.0
    # Weight = 650 * 0.020 = 13 kg/sqm < 30
    score, warnings, metrics = analyze_material_weight(zone_mats, config)
    assert score == 100.0


def test_weight_heavy():
    """Heavy materials -> warning, lower score."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(
            name="Marmor", properties={"density_kg_m3": 2700, "thickness_mm": 30},
        )),
    ]
    config = _default_config()  # max_zone_weight_kg_sqm = 30.0
    # Weight = 2700 * 0.030 = 81 kg/sqm > 30
    score, warnings, metrics = analyze_material_weight(zone_mats, config)
    assert score < 100.0
    assert any(w["code"] == "MATERIAL_HEAVY" for w in warnings)


def test_weight_no_density():
    """Material without density data -> info, partial score."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(properties={})),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_material_weight(zone_mats, config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


def test_weight_no_materials():
    """No materials -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_material_weight([], config)
    assert score == 50.0


from app.services.analysis.materials import run_materials_analysis, SEVERITY_ORDER


# ---------------------------------------------------------------------------
# Integration
# ---------------------------------------------------------------------------


def test_full_materials_analysis():
    """Complete material assignments -> valid result structure with all 5 sub-scores."""
    zone_mats = [
        make_zone_material("salon", "floor", 15.0, make_material(
            name="Teak", lifespan_years=25, cost_per_unit=250.0,
            maintenance_cost_factor=0.02, subcategory="wood",
            properties={"density_kg_m3": 650, "thickness_mm": 20},
        )),
        make_zone_material("cabin", "wall", 12.0, make_material(
            name="Marine-Sperrholz", lifespan_years=20, cost_per_unit=80.0,
            maintenance_cost_factor=0.01, subcategory="wood",
            properties={"density_kg_m3": 550, "thickness_mm": 15},
        )),
        make_zone_material("head", "floor", 3.0, make_material(
            name="Keramikfliese", lifespan_years=30, cost_per_unit=120.0,
            maintenance_cost_factor=0.005, subcategory="composite",
            properties={"density_kg_m3": 2200, "thickness_mm": 8},
        )),
    ]
    result = run_materials_analysis([], [], "cruising_sail", materials=zone_mats)
    assert result["module"] == "materials"
    assert 0 <= result["overall_score"] <= 100
    assert "durability" in result["sub_scores"]
    assert "maintenance" in result["sub_scores"]
    assert "known_issues" in result["sub_scores"]
    assert "compatibility" in result["sub_scores"]
    assert "weight" in result["sub_scores"]
    assert len(result["sub_scores"]) == 8


def test_materials_warnings_sorted():
    """Warnings should be sorted: critical -> warning -> info."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(
            lifespan_years=5,
            known_issues=[{"issue": "Bruch", "severity": "critical"}],
        )),
    ]
    result = run_materials_analysis([], [], "cruising_sail", materials=zone_mats)
    severities = [w["severity"] for w in result["warnings"]]
    order = [SEVERITY_ORDER.get(s, 2) for s in severities]
    assert order == sorted(order)


def test_materials_boat_class_difference():
    """Different boat classes produce different scores."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(
            lifespan_years=18, cost_per_unit=100.0,
            maintenance_cost_factor=0.025,
            properties={"density_kg_m3": 800, "thickness_mm": 25},
        )),
    ]
    result_small = run_materials_analysis([], [], "small_sail", materials=zone_mats)
    result_super = run_materials_analysis([], [], "superyacht", materials=zone_mats)
    # small_sail: min_lifespan=15 (compliant), superyacht: min_lifespan=25 (not compliant)
    assert result_small["overall_score"] != result_super["overall_score"]


def test_materials_config_overrides():
    """Config overrides are applied and stored in config_used."""
    zone_mats = [make_zone_material()]
    result = run_materials_analysis([], [], "cruising_sail", materials=zone_mats,
                                    config_overrides={"min_lifespan_years": 30})
    assert result["config_used"]["min_lifespan_years"] == 30


def test_materials_empty_input():
    """No material assignments -> degraded scores, no crash."""
    result = run_materials_analysis([], [], "cruising_sail", materials=[])
    assert 0 <= result["overall_score"] <= 100
    assert len(result["sub_scores"]) == 8
    assert len(result["warnings"]) > 0
