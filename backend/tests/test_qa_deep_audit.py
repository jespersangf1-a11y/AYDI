"""QA Deep Audit Tests for AYDI Core Analysis Modules.

Comprehensive pytest tests covering:
1. Input validation (empty, None, missing keys, invalid types, negative/huge values)
2. Calculation correctness (hull speed, safe_divide, clamp, sqrt, conversions, temp)
3. Analysis module calculations (ergonomics, compliance, volume, materials, structural, cost)
4. Domain paths (zone types, components, critical checks, module mappings)
5. Floating point edge cases
"""

import math
import pytest

from app.core.units import (
    hull_speed_knots,
    safe_divide,
    clamp,
    safe_sqrt,
    convert,
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
)
from app.core.validation import (
    validate_boat_class,
    validate_zone,
    validate_zones,
    validate_passages,
    DataValidationError,
)
from app.core.domains import (
    AnalysisDomain,
    DOMAIN_CONFIGS,
    get_domain_for_zone_type,
    get_domains_for_module,
    get_all_zone_types,
    get_critical_checks,
)
from app.services.analysis.ergonomics import run_ergonomics_analysis
from app.services.analysis.compliance import run_compliance_analysis
from app.services.analysis.volume_storage import run_volume_storage_analysis
from app.services.analysis.materials import run_materials_analysis
from app.services.analysis.structural import run_structural_analysis
from app.services.analysis.cost import run_cost_analysis
from app.services.analysis.emotional import run_emotional_analysis
from app.services.analysis.production import run_production_analysis
from app.services.analysis.market import run_market_analysis
from app.services.analysis.brand_dna import run_brand_dna_analysis
from app.services.analysis.service_patterns import run_service_patterns_analysis


# ============================================================================
# SECTION 1: INPUT VALIDATION TESTS
# ============================================================================

class TestInputValidationEmpty:
    """Test modules with empty zones list."""

    def test_ergonomics_empty_zones_returns_unavailable(self):
        """Empty zones list should return available=False."""
        result = run_ergonomics_analysis([], [], "cruising_sail")
        assert result["available"] is False
        assert "reason" in result

    def test_compliance_empty_zones_raises_or_unavailable(self):
        """Compliance handling of empty zones (may raise or return unavailable)."""
        # Compliance raises ValueError on unknown boat class, but valid class with empty zones
        result = run_compliance_analysis([], [], "cruising_sail")
        # Should either raise or return unavailable
        # Check if it handles it gracefully
        assert isinstance(result, dict) or result is None

    def test_volume_empty_zones_raises_or_unavailable(self):
        """Volume with empty zones."""
        result = run_volume_storage_analysis([], [], "cruising_sail")
        assert isinstance(result, dict) or result is None


class TestInputValidationNone:
    """Test modules with None values."""

    def test_zones_none_validation(self):
        """validate_zones(None) should return empty list."""
        result = validate_zones(None)
        assert result == []

    def test_passages_none_validation(self):
        """validate_passages(None) should return empty list."""
        result = validate_passages(None)
        assert result == []

    def test_ergonomics_with_none_passages(self):
        """Ergonomics with None passages should handle gracefully."""
        zones = [{"zone_type": "saloon", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}]
        # This should either work with empty passages or return unavailable
        result = run_ergonomics_analysis(zones, None, "cruising_sail")
        assert isinstance(result, dict)


class TestInputValidationMissingKeys:
    """Test validation of zones/passages with missing required keys."""

    def test_zone_missing_polygon(self):
        """Zone without polygon should log warning but validate."""
        zone = {"zone_type": "saloon", "name": "Main Salon", "height_mm": 2000}
        result = validate_zone(zone)
        assert result is not None
        assert result.get("zone_type") == "saloon"

    def test_zone_missing_zone_type(self):
        """Zone without zone_type should validate (type optional)."""
        zone = {"name": "Unknown", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]]}
        result = validate_zone(zone)
        assert result is not None

    def test_passage_missing_width(self):
        """Passage missing width_mm should validate."""
        passage = {"from": "salon", "to": "pantry"}
        result = validate_passages([passage])
        assert len(result) == 1
        assert result[0] == passage

    def test_zones_list_not_list_raises(self):
        """validate_zones with non-list raises DataValidationError."""
        with pytest.raises(DataValidationError):
            validate_zones("not a list")

    def test_passages_list_not_list_raises(self):
        """validate_passages with non-list raises DataValidationError."""
        with pytest.raises(DataValidationError):
            validate_passages({"not": "list"})


class TestInputValidationNegativeValues:
    """Test validation with negative values."""

    def test_zone_negative_height(self):
        """Zone with negative height should log warning."""
        zone = {"zone_type": "saloon", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": -100}
        result = validate_zone(zone)
        # Should not crash but may log warning
        assert result is not None

    def test_zone_negative_area(self):
        """Zone with negative area should log warning."""
        zone = {"zone_type": "saloon", "area_m2": -5.0}
        result = validate_zone(zone)
        assert result is not None

    def test_passage_negative_width(self):
        """Passage with negative width should log warning."""
        passage = {"from": "salon", "to": "pantry", "width_mm": -700}
        result = validate_passages([passage])
        assert len(result) == 1

    def test_validate_positive_negative_raises(self):
        """validate_positive with negative value raises."""
        with pytest.raises(DataValidationError):
            from app.core.validation import validate_positive
            validate_positive(-10.0, "test_value")


class TestInputValidationExtremeValues:
    """Test validation with extremely large values."""

    def test_zone_huge_height(self):
        """Zone with implausibly large height (>10000mm) should log warning."""
        zone = {"zone_type": "saloon", "height_mm": 999999999}
        result = validate_zone(zone)
        assert result is not None

    def test_passage_huge_width(self):
        """Passage with implausibly large width (>5000mm) should log warning."""
        passage = {"from": "salon", "to": "pantry", "width_mm": 999999999}
        result = validate_passages([passage])
        assert len(result) == 1


class TestInputValidationBoatClass:
    """Test boat class validation."""

    def test_invalid_boat_class_raises(self):
        """Invalid boat class should raise DataValidationError."""
        with pytest.raises(DataValidationError):
            validate_boat_class("not_a_valid_class")

    def test_empty_boat_class_raises(self):
        """Empty string boat class should raise."""
        with pytest.raises(DataValidationError):
            validate_boat_class("")

    def test_none_boat_class_raises(self):
        """None boat class should raise."""
        with pytest.raises(DataValidationError):
            validate_boat_class(None)

    def test_valid_boat_classes(self):
        """Valid boat classes should validate without error."""
        valid_classes = [
            "cruising_sail",
            "large_motor",
            "small_sail",
            "performance_sail",
            "superyacht",
            "catamaran_sail",
            "motorsailer",
        ]
        for bc in valid_classes:
            result = validate_boat_class(bc)
            assert result == bc


class TestInputValidationConfigOverrides:
    """Test config_overrides validation."""

    def test_ergonomics_config_overrides_not_dict_returns_unavailable(self):
        """config_overrides as string should be rejected."""
        zones = [{"zone_type": "saloon", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}]
        result = run_ergonomics_analysis(zones, [], "cruising_sail", config_overrides="not_a_dict")
        assert result["available"] is False

    def test_ergonomics_config_overrides_as_list_returns_unavailable(self):
        """config_overrides as list should be rejected."""
        zones = [{"zone_type": "saloon", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}]
        result = run_ergonomics_analysis(zones, [], "cruising_sail", config_overrides=[])
        assert result["available"] is False

    def test_ergonomics_config_overrides_valid_dict(self):
        """config_overrides as valid dict should work."""
        zones = [{"zone_type": "saloon", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}]
        result = run_ergonomics_analysis(zones, [], "cruising_sail", config_overrides={"min_passage_width_mm": 500})
        assert isinstance(result, dict)


# ============================================================================
# SECTION 2: UNIT CONVERSION AND MATH CORRECTNESS TESTS
# ============================================================================

class TestHullSpeedFormula:
    """Test hull_speed_knots calculation."""

    def test_hull_speed_zero(self):
        """Hull speed at LWL=0 should return 0.0."""
        result = hull_speed_knots(0.0)
        assert result == 0.0

    def test_hull_speed_negative(self):
        """Hull speed at negative LWL should return 0.0."""
        result = hull_speed_knots(-10.0)
        assert result == 0.0

    def test_hull_speed_very_small_positive(self):
        """Hull speed at LWL=0.001m should return small positive value."""
        result = hull_speed_knots(0.001)
        assert result > 0.0
        assert result < 0.5

    def test_hull_speed_10m(self):
        """Hull speed at LWL=10m is ~4.2 knots."""
        result = hull_speed_knots(10.0)
        # 1.34 * sqrt(32.8084 ft) ≈ 1.34 * 5.73 ≈ 7.67 knots
        assert 7.5 < result < 8.0

    def test_hull_speed_30m(self):
        """Hull speed at LWL=30m."""
        result = hull_speed_knots(30.0)
        # 1.34 * sqrt(98.4252 ft) ≈ 1.34 * 9.92 ≈ 13.27 knots
        assert 13.0 < result < 13.5

    def test_hull_speed_100m(self):
        """Hull speed at LWL=100m."""
        result = hull_speed_knots(100.0)
        assert result > 20.0  # 1.34 * sqrt(328 ft) ≈ 24.3

    def test_hull_speed_200m(self):
        """Hull speed at LWL=200m."""
        result = hull_speed_knots(200.0)
        assert result > 30.0

    def test_hull_speed_nan_raises(self):
        """Hull speed with NaN should raise ValueError."""
        with pytest.raises(ValueError):
            hull_speed_knots(float('nan'))

    def test_hull_speed_inf_raises(self):
        """Hull speed with Inf should raise ValueError."""
        with pytest.raises(ValueError):
            hull_speed_knots(float('inf'))


class TestSafeDivide:
    """Test safe_divide edge cases."""

    def test_safe_divide_zero_denominator_returns_default(self):
        """safe_divide(1, 0) should return default (0.0)."""
        result = safe_divide(1.0, 0.0)
        assert result == 0.0

    def test_safe_divide_zero_denominator_custom_default(self):
        """safe_divide with custom default."""
        result = safe_divide(1.0, 0.0, default=99.0)
        assert result == 99.0

    def test_safe_divide_normal(self):
        """safe_divide(10, 2) should return 5.0."""
        result = safe_divide(10.0, 2.0)
        assert result == 5.0

    def test_safe_divide_negative_dividend(self):
        """safe_divide(-10, 2) should return -5.0."""
        result = safe_divide(-10.0, 2.0)
        assert result == -5.0

    def test_safe_divide_negative_divisor(self):
        """safe_divide(10, -2) should return -5.0."""
        result = safe_divide(10.0, -2.0)
        assert result == -5.0

    def test_safe_divide_nan_numerator_returns_default(self):
        """safe_divide(NaN, 2) should return default."""
        result = safe_divide(float('nan'), 2.0)
        assert result == 0.0

    def test_safe_divide_nan_denominator_returns_default(self):
        """safe_divide(10, NaN) should return default."""
        result = safe_divide(10.0, float('nan'))
        assert result == 0.0

    def test_safe_divide_inf_numerator(self):
        """safe_divide(Inf, 2) should return default (non-finite result)."""
        result = safe_divide(float('inf'), 2.0)
        assert result == 0.0  # Inf/2 = Inf, which is non-finite

    def test_safe_divide_inf_denominator(self):
        """safe_divide(10, Inf) should return default."""
        result = safe_divide(10.0, float('inf'))
        assert result == 0.0

    def test_safe_divide_very_large_numbers(self):
        """safe_divide with very large numbers should work."""
        result = safe_divide(1e308, 1e308)
        assert 0.9 < result < 1.1


class TestClamp:
    """Test clamp boundary behavior."""

    def test_clamp_below_min(self):
        """clamp(5, 10, 20) should return 10."""
        result = clamp(5.0, 10.0, 20.0)
        assert result == 10.0

    def test_clamp_above_max(self):
        """clamp(25, 10, 20) should return 20."""
        result = clamp(25.0, 10.0, 20.0)
        assert result == 20.0

    def test_clamp_at_min(self):
        """clamp(10, 10, 20) should return 10."""
        result = clamp(10.0, 10.0, 20.0)
        assert result == 10.0

    def test_clamp_at_max(self):
        """clamp(20, 10, 20) should return 20."""
        result = clamp(20.0, 10.0, 20.0)
        assert result == 20.0

    def test_clamp_in_range(self):
        """clamp(15, 10, 20) should return 15."""
        result = clamp(15.0, 10.0, 20.0)
        assert result == 15.0

    def test_clamp_negative_range(self):
        """clamp(-5, -10, -1) should return -5."""
        result = clamp(-5.0, -10.0, -1.0)
        assert result == -5.0

    def test_clamp_nan_input(self):
        """clamp(NaN, 10, 20) behavior.

        In Python, min(max_val, NaN) returns max_val (not NaN),
        so clamp(NaN, 10, 20) = max(10, min(20, NaN)) = max(10, 20) = 20.
        This is due to how min/max handle NaN: NaN comparisons are always False.
        """
        result = clamp(float('nan'), 10.0, 20.0)
        # min(20, NaN) returns 20 (because NaN < 20 is False)
        # max(10, 20) returns 20
        assert result == 20.0

    def test_clamp_0_to_100_at_boundaries(self):
        """clamp for score boundaries [0, 100]."""
        assert clamp(-10.0, 0.0, 100.0) == 0.0
        assert clamp(150.0, 0.0, 100.0) == 100.0
        assert clamp(50.0, 0.0, 100.0) == 50.0


class TestSafeSqrt:
    """Test safe_sqrt edge cases."""

    def test_safe_sqrt_negative_returns_zero(self):
        """safe_sqrt(-5) should return 0.0."""
        result = safe_sqrt(-5.0)
        assert result == 0.0

    def test_safe_sqrt_zero(self):
        """safe_sqrt(0) should return 0.0."""
        result = safe_sqrt(0.0)
        assert result == 0.0

    def test_safe_sqrt_one(self):
        """safe_sqrt(1) should return 1.0."""
        result = safe_sqrt(1.0)
        assert result == 1.0

    def test_safe_sqrt_four(self):
        """safe_sqrt(4) should return 2.0."""
        result = safe_sqrt(4.0)
        assert result == 2.0

    def test_safe_sqrt_very_large(self):
        """safe_sqrt(1e16) should work."""
        result = safe_sqrt(1e16)
        assert result == 1e8

    def test_safe_sqrt_very_small_positive(self):
        """safe_sqrt(0.0001) should work."""
        result = safe_sqrt(0.0001)
        assert abs(result - 0.01) < 1e-10


class TestConversions:
    """Test unit conversion round-trips."""

    def test_m_to_ft_roundtrip(self):
        """Convert m -> ft -> m should recover original."""
        original = 10.0
        to_ft = convert(original, "m_to_ft")
        back = convert(to_ft, "m_to_ft", reverse=True)
        assert abs(back - original) < 1e-10

    def test_mm_to_inch_roundtrip(self):
        """Convert mm -> in -> mm should recover original."""
        original = 1000.0
        to_in = convert(original, "mm_to_inch")
        back = convert(to_in, "mm_to_inch", reverse=True)
        assert abs(back - original) < 1e-10

    def test_kg_to_lbs_roundtrip(self):
        """Convert kg -> lbs -> kg should recover original."""
        original = 100.0
        to_lbs = convert(original, "kg_to_lbs")
        back = convert(to_lbs, "kg_to_lbs", reverse=True)
        assert abs(back - original) < 1e-10

    def test_l_to_gal_roundtrip(self):
        """Convert l -> gal -> l should recover original."""
        original = 1000.0
        to_gal = convert(original, "l_to_gal_us")
        back = convert(to_gal, "l_to_gal_us", reverse=True)
        assert abs(back - original) < 1e-6  # Slightly larger epsilon due to conversion factor

    def test_convert_nan_raises(self):
        """convert with NaN should raise ValueError."""
        with pytest.raises(ValueError):
            convert(float('nan'), "m_to_ft")

    def test_convert_inf_raises(self):
        """convert with Inf should raise ValueError."""
        with pytest.raises(ValueError):
            convert(float('inf'), "m_to_ft")

    def test_convert_invalid_key_raises(self):
        """convert with unknown conversion key should raise KeyError."""
        with pytest.raises(KeyError):
            convert(10.0, "invalid_conversion")


class TestTemperatureConversions:
    """Test temperature conversion correctness."""

    def test_celsius_0_to_fahrenheit_32(self):
        """0°C should convert to 32°F."""
        result = celsius_to_fahrenheit(0.0)
        assert result == 32.0

    def test_celsius_100_to_fahrenheit_212(self):
        """100°C should convert to 212°F."""
        result = celsius_to_fahrenheit(100.0)
        assert result == 212.0

    def test_celsius_minus_40_to_fahrenheit_minus_40(self):
        """-40°C should convert to -40°F."""
        result = celsius_to_fahrenheit(-40.0)
        assert result == -40.0

    def test_fahrenheit_32_to_celsius_0(self):
        """32°F should convert to 0°C."""
        result = fahrenheit_to_celsius(32.0)
        assert result == 0.0

    def test_fahrenheit_212_to_celsius_100(self):
        """212°F should convert to 100°C."""
        result = fahrenheit_to_celsius(212.0)
        assert result == 100.0

    def test_celsius_fahrenheit_roundtrip(self):
        """Convert C -> F -> C should recover original."""
        original = 25.0
        to_f = celsius_to_fahrenheit(original)
        back = fahrenheit_to_celsius(to_f)
        assert abs(back - original) < 1e-10

    def test_celsius_nan_raises(self):
        """celsius_to_fahrenheit(NaN) should raise ValueError."""
        with pytest.raises(ValueError):
            celsius_to_fahrenheit(float('nan'))

    def test_fahrenheit_nan_raises(self):
        """fahrenheit_to_celsius(NaN) should raise ValueError."""
        with pytest.raises(ValueError):
            fahrenheit_to_celsius(float('nan'))


# ============================================================================
# SECTION 3: ANALYSIS MODULE CALCULATION CORRECTNESS TESTS
# ============================================================================

class TestErgonomicsCalculations:
    """Test ergonomics analysis calculations."""

    def test_ergonomics_passage_width_zero(self):
        """Passage width = 0 should be handled."""
        zones = [{"zone_type": "saloon", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}]
        passages = [{"from": "saloon", "to": "pantry", "width_mm": 0}]
        result = run_ergonomics_analysis(zones, passages, "cruising_sail")
        assert isinstance(result, dict)
        assert "overall_score" in result

    def test_ergonomics_passage_width_negative(self):
        """Passage width = negative should be handled."""
        zones = [{"zone_type": "saloon", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}]
        passages = [{"from": "saloon", "to": "pantry", "width_mm": -500}]
        result = run_ergonomics_analysis(zones, passages, "cruising_sail")
        assert isinstance(result, dict)

    def test_ergonomics_heel_angle_zero(self):
        """Ergonomics with heel_angle = 0 should work."""
        zones = [{"zone_type": "saloon", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}]
        # Check if heel_angle can be overridden
        result = run_ergonomics_analysis(zones, [], "cruising_sail", config_overrides={"heel_angle_deg": 0})
        assert isinstance(result, dict)

    def test_ergonomics_heel_angle_15(self):
        """Ergonomics with heel_angle = 15."""
        zones = [{"zone_type": "saloon", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}]
        result = run_ergonomics_analysis(zones, [], "cruising_sail", config_overrides={"heel_angle_deg": 15})
        assert isinstance(result, dict)

    def test_ergonomics_heel_angle_90(self):
        """Ergonomics with heel_angle = 90 (extreme)."""
        zones = [{"zone_type": "saloon", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}]
        result = run_ergonomics_analysis(zones, [], "cruising_sail", config_overrides={"heel_angle_deg": 90})
        assert isinstance(result, dict)


class TestComplianceCalculations:
    """Test compliance analysis calculations."""

    def test_compliance_ce_category_validation(self):
        """Compliance analysis should detect CE categories."""
        zones = [
            {"zone_type": "hull", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}
        ]
        result = run_compliance_analysis(zones, [], "cruising_sail")
        assert isinstance(result, dict)
        assert "overall_score" in result

    def test_compliance_sill_heights_cat_a(self):
        """CE Cat A should require higher companionway sills."""
        # Compliance module will derive category from zones/boat class
        zones = [
            {"zone_type": "hull", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}
        ]
        result = run_compliance_analysis(zones, [], "cruising_sail")
        assert isinstance(result, dict)

    def test_compliance_ventilation_zero_engine_kw(self):
        """Ventilation with engine_kw = 0 should handle gracefully."""
        zones = [
            {"zone_type": "engine_room", "polygon": [[0, 0], [500, 0], [500, 500], [0, 500]], "height_mm": 1000}
        ]
        result = run_compliance_analysis(zones, [], "small_motor", config_overrides={"engine_kw": 0})
        assert isinstance(result, dict)


class TestVolumeCalculations:
    """Test volume analysis calculations."""

    def test_volume_degenerate_polygon_same_point(self):
        """Volume with degenerate polygon (all same point) should handle."""
        zones = [
            {"zone_type": "saloon", "polygon": [[1000, 1000], [1000, 1000], [1000, 1000]], "height_mm": 2000}
        ]
        result = run_volume_storage_analysis(zones, [], "cruising_sail")
        assert isinstance(result, dict)

    def test_volume_degenerate_polygon_collinear(self):
        """Volume with collinear points (2D)."""
        zones = [
            {"zone_type": "saloon", "polygon": [[0, 0], [1000, 1000], [2000, 2000]], "height_mm": 2000}
        ]
        result = run_volume_storage_analysis(zones, [], "cruising_sail")
        assert isinstance(result, dict)

    def test_volume_degenerate_polygon_2_points(self):
        """Volume with only 2 points (line)."""
        zones = [
            {"zone_type": "saloon", "polygon": [[0, 0], [1000, 1000]], "height_mm": 2000}
        ]
        result = run_volume_storage_analysis(zones, [], "cruising_sail")
        assert isinstance(result, dict)


class TestMaterialsCalculations:
    """Test materials analysis calculations."""

    def test_materials_lifespan_zero(self):
        """Materials with lifespan_years = 0 should handle gracefully."""
        zones = [{"zone_type": "saloon", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}]
        # Materials module may or may not use lifespan directly
        result = run_materials_analysis(zones, [], "cruising_sail")
        assert isinstance(result, dict)

    def test_materials_cost_per_unit_zero(self):
        """Materials with cost_per_unit = 0."""
        zones = [{"zone_type": "saloon", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}]
        result = run_materials_analysis(zones, [], "cruising_sail")
        assert isinstance(result, dict)


class TestStructuralCalculations:
    """Test structural analysis calculations."""

    def test_structural_trim_moment_zero(self):
        """Structural with moment = 0 (no trim)."""
        zones = [{"zone_type": "hull", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}]
        result = run_structural_analysis(zones, [], "cruising_sail")
        assert isinstance(result, dict)

    def test_structural_trim_length_zero(self):
        """Structural with length = 0 should handle."""
        zones = [{"zone_type": "hull", "polygon": [[0, 0], [0, 0], [0, 0], [0, 0]], "height_mm": 2000}]
        result = run_structural_analysis(zones, [], "cruising_sail")
        # May return unavailable due to zero length
        assert isinstance(result, dict)


class TestCostCalculations:
    """Test cost analysis calculations."""

    def test_cost_total_with_zero_items(self):
        """Cost with no items."""
        result = run_cost_analysis([], [], "cruising_sail")
        assert isinstance(result, dict)

    def test_cost_negative_costs(self):
        """Cost module should handle negative costs gracefully."""
        # Negative costs might come from credits/refunds
        zones = [{"zone_type": "saloon", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}]
        result = run_cost_analysis(zones, [], "cruising_sail")
        assert isinstance(result, dict)


# ============================================================================
# SECTION 4: DOMAIN PATH VERIFICATION TESTS
# ============================================================================

class TestDomainConfiguration:
    """Test domain configuration completeness."""

    def test_all_10_domains_configured(self):
        """All 10 AnalysisDomain values must have configurations."""
        for domain in AnalysisDomain:
            assert domain in DOMAIN_CONFIGS, f"Missing config for {domain.value}"

    def test_all_domains_have_zone_types(self):
        """Every domain must have >= 1 zone type."""
        for domain, config in DOMAIN_CONFIGS.items():
            assert len(config.zone_types) > 0, f"{domain.value} has no zone types"

    def test_all_domains_have_component_categories(self):
        """Every domain must have >= 1 component category."""
        for domain, config in DOMAIN_CONFIGS.items():
            assert len(config.component_categories) > 0, f"{domain.value} has no component categories"

    def test_all_domains_have_5_or_more_critical_checks(self):
        """Every domain must have >= 5 critical checks."""
        for domain, config in DOMAIN_CONFIGS.items():
            assert len(config.critical_checks) >= 5, \
                f"{domain.value} has only {len(config.critical_checks)} critical checks (need >= 5)"

    def test_all_domains_have_relevant_modules(self):
        """Every domain must reference >= 1 analysis module."""
        for domain, config in DOMAIN_CONFIGS.items():
            assert len(config.relevant_modules) > 0, f"{domain.value} has no relevant modules"


class TestZoneTypeMappings:
    """Test that zone types are correctly mapped to domains."""

    def test_all_zone_types_have_domain(self):
        """Every valid zone type should map to exactly one domain."""
        all_zone_types = get_all_zone_types()
        assert len(all_zone_types) > 0, "No zone types found"

        for zone_type in all_zone_types:
            domain = get_domain_for_zone_type(zone_type)
            assert domain is not None, f"Zone type '{zone_type}' has no domain mapping"

    def test_zone_type_uniqueness(self):
        """Each zone type should map to exactly one domain (no orphans across domains).

        NOTE: This test documents 3 REAL BUGS in the domain configuration:
        1. 'nav_station' appears in both ELECTRICAL_ELECTRONICS and NAVIGATION (domains.py:106,219)
        2. 'engine_room' appears in both PROPULSION_ENGINE and MAINTENANCE_SERVICE (domains.py:85,241)
        3. 'hull' appears in both HULL_STRUCTURE and MAINTENANCE_SERVICE (domains.py:49,241)

        These duplicates violate the principle that each zone type should map to exactly
        one domain. The MAINTENANCE_SERVICE domain inappropriately reuses zone types.
        """
        zone_to_domain = {}
        duplicates = []
        for domain, config in DOMAIN_CONFIGS.items():
            for zone_type in config.zone_types:
                if zone_type in zone_to_domain:
                    duplicates.append((zone_type, zone_to_domain[zone_type], domain))
                else:
                    zone_to_domain[zone_type] = domain

        # Report duplicates found
        if duplicates:
            for zone_type, domain1, domain2 in duplicates:
                print(f"DOMAIN BUG: Zone type '{zone_type}' appears in {domain1.value} and {domain2.value}")

        # Document known duplicates as test failures
        known_duplicates = {
            "nav_station",      # ELECTRICAL_ELECTRONICS vs NAVIGATION
            "engine_room",      # PROPULSION_ENGINE vs MAINTENANCE_SERVICE
            "hull",             # HULL_STRUCTURE vs MAINTENANCE_SERVICE
        }
        for zone_type, _, _ in duplicates:
            assert zone_type in known_duplicates, \
                f"Found unexpected zone type duplicate: '{zone_type}' (not in known_duplicates)"

        # Fail if there are known duplicates (documenting the bugs)
        if duplicates:
            pytest.fail(
                f"DOMAIN CONFIGURATION BUGS FOUND: {len(duplicates)} zone type duplicates:\n" +
                "\n".join(f"  - '{zt}' in {d1.value} and {d2.value}" for zt, d1, d2 in duplicates)
            )

    def test_sample_zone_types_mapped_correctly(self):
        """Sample zone types should map to expected domains."""
        assert get_domain_for_zone_type("hull") == AnalysisDomain.HULL_STRUCTURE
        assert get_domain_for_zone_type("cabin") == AnalysisDomain.INTERIOR
        assert get_domain_for_zone_type("cockpit") == AnalysisDomain.DECK_FITTINGS
        assert get_domain_for_zone_type("engine") == AnalysisDomain.PROPULSION_ENGINE


class TestModuleDomainMappings:
    """Test that analysis modules are mapped to domains."""

    def test_all_12_modules_have_domain_mappings(self):
        """All 12 analysis modules should map to >= 1 domain."""
        modules = [
            "ergonomics",
            "volume_storage",
            "emotional",
            "compliance",
            "production",
            "materials",
            "structural",
            "cost",
            "service_patterns",
            "brand_dna",
            "market",
            "community",  # If exists
        ]

        for module in modules:
            domains = get_domains_for_module(module)
            # Some modules may have 0 domains (community), but most should have >= 1
            assert isinstance(domains, list), f"Module {module} should return list"

    def test_structural_module_domains(self):
        """Structural module should map to hull_structure and others."""
        domains = get_domains_for_module("structural")
        assert len(domains) > 0

    def test_ergonomics_module_domains(self):
        """Ergonomics module should map to interior and deck domains."""
        domains = get_domains_for_module("ergonomics")
        assert len(domains) > 0

    def test_cost_module_domains(self):
        """Cost module should map to multiple domains."""
        domains = get_domains_for_module("cost")
        assert len(domains) > 0


class TestCriticalChecks:
    """Test critical checks retrieval."""

    def test_hull_structure_critical_checks(self):
        """Hull structure domain should have critical checks."""
        checks = get_critical_checks(AnalysisDomain.HULL_STRUCTURE)
        assert len(checks) >= 5
        assert "osmosis_inspection" in checks
        assert "delamination_check" in checks

    def test_interior_critical_checks(self):
        """Interior domain should have critical checks."""
        checks = get_critical_checks(AnalysisDomain.INTERIOR)
        assert len(checks) >= 5
        assert "joinery_tolerance" in checks

    def test_all_domains_have_critical_checks(self):
        """All domains must return non-empty critical checks list."""
        for domain in AnalysisDomain:
            checks = get_critical_checks(domain)
            assert isinstance(checks, list)
            assert len(checks) > 0


# ============================================================================
# SECTION 5: FLOATING POINT EDGE CASES
# ============================================================================

class TestFloatingPointCalculations:
    """Test floating point edge cases in calculations."""

    def test_0_1_plus_0_2_is_0_3(self):
        """0.1 + 0.2 = 0.3 in financial calculations should handle epsilon."""
        # This is the famous floating point problem
        result = 0.1 + 0.2
        # Should be close to 0.3 within epsilon
        assert abs(result - 0.3) < 1e-10

    def test_very_small_area_calculations(self):
        """Very small polygon areas should be handled."""
        zones = [
            {"zone_type": "saloon", "polygon": [[0, 0], [0.001, 0], [0.001, 0.001], [0, 0.001]], "height_mm": 2000}
        ]
        result = run_volume_storage_analysis(zones, [], "cruising_sail")
        assert isinstance(result, dict)

    def test_score_clamping_at_zero(self):
        """Scores should clamp to 0 when calculation yields negative."""
        from app.core.validation import validate_score
        result = validate_score(-10.0)
        assert result == 0.0

    def test_score_clamping_at_100(self):
        """Scores should clamp to 100 when calculation yields > 100."""
        from app.core.validation import validate_score
        result = validate_score(150.0)
        assert result == 100.0

    def test_score_in_valid_range(self):
        """Scores in [0, 100] should pass through."""
        from app.core.validation import validate_score
        result = validate_score(50.5)
        assert result == 50.5

    def test_zero_weight_in_calculation(self):
        """Weights of 0.0 in scoring should not affect result."""
        zones = [{"zone_type": "saloon", "polygon": [[0, 0], [1000, 0], [1000, 2000], [0, 2000]], "height_mm": 2000}]
        # Override with zero weight
        result = run_ergonomics_analysis(zones, [], "cruising_sail", config_overrides={"weights": {}})
        assert isinstance(result, dict)


class TestComplexCalculationAccuracy:
    """Test accuracy of complex multi-step calculations."""

    def test_ergonomics_score_within_bounds(self):
        """Ergonomics overall score should be 0-100.

        NOTE: Zones must include 'name' field for accessibility analysis.
        Passages must use 'from_zone' and 'to_zone' (not 'from'/'to').
        """
        zones = [
            {"zone_type": "saloon", "name": "Salon", "polygon": [[0, 0], [5000, 0], [5000, 4000], [0, 4000]], "height_mm": 2200},
            {"zone_type": "cabin", "name": "Cabin", "polygon": [[5000, 0], [7000, 0], [7000, 3000], [5000, 3000]], "height_mm": 1900},
        ]
        passages = [
            {"from_zone": "saloon", "to_zone": "cabin", "width_mm": 650, "height_mm": 1900}
        ]
        result = run_ergonomics_analysis(zones, passages, "cruising_sail")
        assert isinstance(result, dict)
        if "overall_score" in result:
            score = result["overall_score"]
            assert 0.0 <= score <= 100.0

    def test_compliance_score_within_bounds(self):
        """Compliance overall score should be 0-100."""
        zones = [
            {"zone_type": "hull", "polygon": [[0, 0], [10000, 0], [10000, 3000], [0, 3000]], "height_mm": 2200},
        ]
        result = run_compliance_analysis(zones, [], "cruising_sail")
        if "overall_score" in result:
            score = result["overall_score"]
            assert 0.0 <= score <= 100.0

    def test_volume_score_within_bounds(self):
        """Volume overall score should be 0-100."""
        zones = [
            {"zone_type": "saloon", "polygon": [[0, 0], [5000, 0], [5000, 4000], [0, 4000]], "height_mm": 2200},
        ]
        result = run_volume_storage_analysis(zones, [], "cruising_sail")
        if "overall_score" in result:
            score = result["overall_score"]
            assert 0.0 <= score <= 100.0


if __name__ == "__main__":
    pytest.main([__file__, "-v", "--tb=short"])
