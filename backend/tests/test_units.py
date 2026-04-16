"""Tests for the unit conversion system."""

import math
import pytest
from app.core.units import (
    UnitSystem,
    celsius_to_fahrenheit,
    clamp,
    convert,
    convert_dimensions,
    convert_power,
    convert_volume,
    convert_weight,
    fahrenheit_to_celsius,
    hull_speed_knots,
    safe_divide,
    safe_sqrt,
)


class TestBasicConversions:
    def test_meters_to_feet(self):
        result = convert(10.0, "m_to_ft")
        assert abs(result - 32.8084) < 0.001

    def test_feet_to_meters_reverse(self):
        result = convert(32.8084, "m_to_ft", reverse=True)
        assert abs(result - 10.0) < 0.001

    def test_mm_to_inches(self):
        result = convert(25.4, "mm_to_inch")
        assert abs(result - 1.0) < 0.001

    def test_kg_to_lbs(self):
        result = convert(1.0, "kg_to_lbs")
        assert abs(result - 2.20462) < 0.001

    def test_liters_to_gallons(self):
        result = convert(3.78541, "l_to_gal_us")
        assert abs(result - 1.0) < 0.01

    def test_kw_to_hp(self):
        result = convert(100.0, "kw_to_hp")
        assert abs(result - 134.102) < 0.1

    def test_kw_to_ps(self):
        result = convert(100.0, "kw_to_ps")
        assert abs(result - 135.962) < 0.1

    def test_knots_to_mph(self):
        result = convert(10.0, "kn_to_mph")
        assert abs(result - 11.5078) < 0.01

    def test_knots_to_kmh(self):
        result = convert(10.0, "kn_to_kmh")
        assert abs(result - 18.52) < 0.01

    def test_bar_to_psi(self):
        result = convert(1.0, "bar_to_psi")
        assert abs(result - 14.5038) < 0.01

    def test_m2_to_ft2(self):
        result = convert(1.0, "m2_to_ft2")
        assert abs(result - 10.7639) < 0.01

    def test_unknown_key_raises(self):
        with pytest.raises(KeyError):
            convert(1.0, "nonexistent_conversion")

    def test_nan_raises(self):
        with pytest.raises(ValueError):
            convert(float("nan"), "m_to_ft")

    def test_inf_raises(self):
        with pytest.raises(ValueError):
            convert(float("inf"), "m_to_ft")


class TestTemperature:
    def test_celsius_to_fahrenheit_boiling(self):
        assert abs(celsius_to_fahrenheit(100.0) - 212.0) < 0.01

    def test_celsius_to_fahrenheit_freezing(self):
        assert abs(celsius_to_fahrenheit(0.0) - 32.0) < 0.01

    def test_fahrenheit_to_celsius_body(self):
        assert abs(fahrenheit_to_celsius(98.6) - 37.0) < 0.01

    def test_roundtrip(self):
        original = 23.5
        result = fahrenheit_to_celsius(celsius_to_fahrenheit(original))
        assert abs(result - original) < 0.001

    def test_nan_raises(self):
        with pytest.raises(ValueError):
            celsius_to_fahrenheit(float("nan"))


class TestBatchConversions:
    def test_dimensions_metric(self):
        result = convert_dimensions(12.5, 4.2, 1.8, UnitSystem.METRIC)
        assert result["length"] == 12.5
        assert result["beam"] == 4.2
        assert result["draft"] == 1.8
        assert result["unit"] == "m"

    def test_dimensions_imperial(self):
        result = convert_dimensions(12.5, 4.2, 1.8, UnitSystem.IMPERIAL)
        assert abs(result["length"] - 41.0) < 0.1
        assert result["unit"] == "ft"

    def test_weight_metric_kg(self):
        result = convert_weight(500.0, UnitSystem.METRIC)
        assert result["value"] == 500.0
        assert result["unit"] == "kg"

    def test_weight_metric_tonnes(self):
        result = convert_weight(12000.0, UnitSystem.METRIC)
        assert result["value"] == 12.0
        assert result["unit"] == "t"

    def test_weight_imperial(self):
        result = convert_weight(100.0, UnitSystem.IMPERIAL)
        assert abs(result["value"] - 220.0) < 1.0
        assert result["unit"] == "lbs"

    def test_volume_metric(self):
        result = convert_volume(500.0, UnitSystem.METRIC)
        assert result["value"] == 500.0
        assert result["unit"] == "l"

    def test_volume_imperial(self):
        result = convert_volume(500.0, UnitSystem.IMPERIAL)
        assert abs(result["value"] - 132.1) < 0.1
        assert result["unit"] == "gal"

    def test_power_metric(self):
        result = convert_power(75.0, UnitSystem.METRIC)
        assert result["value"] == 75.0
        assert result["unit"] == "kW"

    def test_power_imperial(self):
        result = convert_power(75.0, UnitSystem.IMPERIAL)
        assert abs(result["value"] - 101.0) < 1.0
        assert result["unit"] == "HP"


class TestHullSpeed:
    """Verify hull speed formula with manual calculations."""

    def test_hull_speed_10m(self):
        # V_max = 1.34 * sqrt(32.81 ft) = 1.34 * 5.728 = 7.68 kn
        result = hull_speed_knots(10.0)
        assert abs(result - 7.68) < 0.05

    def test_hull_speed_zero(self):
        assert hull_speed_knots(0.0) == 0.0

    def test_hull_speed_negative(self):
        assert hull_speed_knots(-5.0) == 0.0

    def test_hull_speed_nan_raises(self):
        with pytest.raises(ValueError):
            hull_speed_knots(float("nan"))

    def test_hull_speed_superyacht_150m(self):
        # LWL ~140m -> 459ft -> sqrt(459)=21.42 -> 1.34*21.42=28.7kn
        result = hull_speed_knots(140.0)
        assert 28.0 < result < 30.0  # Plausibility check

    def test_hull_speed_small_dinghy_3m(self):
        # LWL=3m -> 9.84ft -> sqrt(9.84)=3.137 -> 1.34*3.137=4.2kn
        result = hull_speed_knots(3.0)
        assert abs(result - 4.2) < 0.2


class TestSafeDivide:
    def test_normal_division(self):
        assert safe_divide(10.0, 2.0) == 5.0

    def test_divide_by_zero(self):
        assert safe_divide(10.0, 0.0) == 0.0

    def test_divide_by_zero_custom_default(self):
        assert safe_divide(10.0, 0.0, default=50.0) == 50.0

    def test_divide_by_inf(self):
        assert safe_divide(10.0, float("inf")) == 0.0

    def test_divide_by_nan(self):
        assert safe_divide(10.0, float("nan")) == 0.0

    def test_result_inf(self):
        # Very small denominator -> overflow
        assert safe_divide(1e308, 1e-308) == 0.0

    def test_negative_values(self):
        assert safe_divide(-10.0, 2.0) == -5.0


class TestClamp:
    def test_within_range(self):
        assert clamp(5.0, 0.0, 10.0) == 5.0

    def test_below_min(self):
        assert clamp(-5.0, 0.0, 10.0) == 0.0

    def test_above_max(self):
        assert clamp(15.0, 0.0, 10.0) == 10.0

    def test_at_boundary(self):
        assert clamp(0.0, 0.0, 10.0) == 0.0
        assert clamp(10.0, 0.0, 10.0) == 10.0


class TestSafeSqrt:
    def test_positive(self):
        assert abs(safe_sqrt(9.0) - 3.0) < 1e-10

    def test_zero(self):
        assert safe_sqrt(0.0) == 0.0

    def test_negative_returns_zero(self):
        assert safe_sqrt(-4.0) == 0.0
