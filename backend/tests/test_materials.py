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
