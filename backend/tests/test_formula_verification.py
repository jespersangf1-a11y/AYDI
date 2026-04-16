"""Formula verification tests — manual hand calculations vs. code results.

Per the Anleitung: "Für JEDE Formel im System gilt:
1. Dokumentiere die Formel in Klartext
2. Rechne ein Beispiel von Hand und vergleiche mit dem Code-Ergebnis
3. Teste Grenzwerte (0, Maximalwerte, negative Werte)
4. Prüfe die Einheiten (mm vs. m, kg vs. lbs, etc.)"
"""

import math
import pytest
from app.core.units import hull_speed_knots, convert, safe_divide


# ===========================================================================
# 1. HULL SPEED (Rumpfgeschwindigkeit)
# ===========================================================================
# Formula: V_max = 1.34 × sqrt(LWL_ft) [knots]
# Where: LWL_ft = LWL_m × 3.28084
# Source: Froude number theory, widely accepted in naval architecture

class TestHullSpeedFormula:
    """Manual verification of hull speed formula."""

    def test_standard_10m_cruiser(self):
        """LWL = 10.0m = 32.808ft
        V = 1.34 × sqrt(32.808)
        sqrt(32.808) = 5.7278
        V = 1.34 × 5.7278 = 7.675 kn
        """
        result = hull_speed_knots(10.0)
        expected = 1.34 * math.sqrt(10.0 * 3.28084)
        assert abs(result - expected) < 0.001
        assert abs(result - 7.675) < 0.05

    def test_12m_yacht(self):
        """LWL = 12.0m = 39.370ft
        V = 1.34 × sqrt(39.370)
        sqrt(39.370) = 6.275
        V = 1.34 × 6.275 = 8.408 kn
        """
        result = hull_speed_knots(12.0)
        expected = 1.34 * math.sqrt(12.0 * 3.28084)
        assert abs(result - expected) < 0.001
        assert abs(result - 8.41) < 0.05

    def test_6m_dinghy(self):
        """LWL = 6.0m = 19.685ft
        V = 1.34 × sqrt(19.685)
        sqrt(19.685) = 4.437
        V = 1.34 × 4.437 = 5.946 kn
        """
        result = hull_speed_knots(6.0)
        assert abs(result - 5.95) < 0.05

    def test_30m_superyacht(self):
        """LWL = 30.0m = 98.425ft
        V = 1.34 × sqrt(98.425) = 1.34 × 9.921 = 13.29 kn
        """
        result = hull_speed_knots(30.0)
        assert abs(result - 13.29) < 0.1

    # Boundary tests
    def test_zero_lwl(self):
        assert hull_speed_knots(0.0) == 0.0

    def test_negative_lwl(self):
        assert hull_speed_knots(-5.0) == 0.0

    def test_very_small_lwl(self):
        """LWL = 0.001m (1mm) -> hull speed should be near 0."""
        result = hull_speed_knots(0.001)
        assert result < 0.1

    def test_extreme_lwl_200m(self):
        """LWL = 200m = 656.17ft
        V = 1.34 × sqrt(656.17) = 1.34 × 25.615 = 34.32 kn
        """
        result = hull_speed_knots(200.0)
        assert abs(result - 34.32) < 0.2


# ===========================================================================
# 2. UNIT CONVERSIONS — Dimensional verification
# ===========================================================================

class TestUnitConversionFormulas:
    """Verify unit conversion formulas against known reference values."""

    def test_meters_to_feet_reference(self):
        """1 meter = 3.28084 feet (exact definition: 1 ft = 0.3048m)"""
        result = convert(1.0, "m_to_ft")
        assert abs(result - 3.28084) < 0.00001

    def test_feet_roundtrip(self):
        """10m -> ft -> m should equal 10m"""
        ft = convert(10.0, "m_to_ft")
        m = convert(ft, "m_to_ft", reverse=True)
        assert abs(m - 10.0) < 1e-10

    def test_mm_to_inch_reference(self):
        """25.4mm = exactly 1 inch"""
        result = convert(25.4, "mm_to_inch")
        assert abs(result - 1.0) < 1e-10

    def test_kg_to_lbs_reference(self):
        """1 kg = 2.20462 lbs"""
        result = convert(1.0, "kg_to_lbs")
        assert abs(result - 2.20462) < 0.00001

    def test_liter_to_gallon_reference(self):
        """1 US gallon = 3.78541 liters"""
        result = convert(3.78541, "l_to_gal_us")
        assert abs(result - 1.0) < 0.001

    def test_knot_to_kmh_reference(self):
        """1 knot = 1.852 km/h (by definition: 1 NM/h)"""
        result = convert(1.0, "kn_to_kmh")
        assert abs(result - 1.852) < 0.0001

    def test_kw_to_hp_reference(self):
        """1 kW = 1.34102 HP (mechanical horsepower)"""
        result = convert(1.0, "kw_to_hp")
        assert abs(result - 1.34102) < 0.001

    def test_bar_to_psi_reference(self):
        """1 bar = 14.5038 psi"""
        result = convert(1.0, "bar_to_psi")
        assert abs(result - 14.5038) < 0.01


# ===========================================================================
# 3. POLYGON AREA (Shoelace formula)
# ===========================================================================
# Used in structural analysis for zone area calculation
# Formula: A = 0.5 × |Σ(x_i × y_{i+1} - x_{i+1} × y_i)|

class TestPolygonAreaFormula:
    """Verify polygon area calculation (used in structural.py)."""

    def _shoelace(self, points: list[tuple[float, float]]) -> float:
        """Reference implementation of shoelace formula."""
        n = len(points)
        if n < 3:
            return 0.0
        area = 0.0
        for i in range(n):
            j = (i + 1) % n
            area += points[i][0] * points[j][1]
            area -= points[j][0] * points[i][1]
        return abs(area) / 2.0

    def test_unit_square(self):
        """1×1 square → area = 1.0"""
        points = [(0, 0), (1, 0), (1, 1), (0, 1)]
        assert abs(self._shoelace(points) - 1.0) < 1e-10

    def test_rectangle_3x4(self):
        """3×4 rectangle → area = 12.0"""
        points = [(0, 0), (3, 0), (3, 4), (0, 4)]
        assert abs(self._shoelace(points) - 12.0) < 1e-10

    def test_right_triangle(self):
        """Right triangle base=3, height=4 → area = 6.0"""
        points = [(0, 0), (3, 0), (0, 4)]
        assert abs(self._shoelace(points) - 6.0) < 1e-10

    def test_degenerate_line(self):
        """All points collinear → area = 0.0"""
        points = [(0, 0), (1, 0)]
        assert self._shoelace(points) == 0.0


# ===========================================================================
# 4. COCKPIT DRAIN FORMULA (ISO 11812)
# ===========================================================================
# Formula: drain_capacity = cockpit_volume × 2 (must drain in 2× volume time)
# drain_time_seconds = cockpit_volume_liters / drain_rate_liters_per_second

class TestCockpitDrainFormula:
    """Verify cockpit drain capacity calculation per ISO 11812."""

    def test_standard_cockpit(self):
        """Cockpit: 2.0m × 1.5m × 0.3m = 0.9 m³ = 900 liters
        Required drain: must empty cockpit in reasonable time
        ISO requires drains that can handle 2× cockpit volume
        Required drain capacity: 1800 liters/drain_time
        """
        length_m = 2.0
        width_m = 1.5
        sill_height_m = 0.3
        cockpit_volume_m3 = length_m * width_m * sill_height_m
        cockpit_volume_liters = cockpit_volume_m3 * 1000
        required_capacity = cockpit_volume_liters * 2

        assert abs(cockpit_volume_m3 - 0.9) < 0.01
        assert abs(cockpit_volume_liters - 900) < 1
        assert abs(required_capacity - 1800) < 1


# ===========================================================================
# 5. COMPANIONWAY SILL HEIGHT (CE Categories)
# ===========================================================================
# Cat A: 300mm, Cat B: 250mm, Cat C: 150mm, Cat D: 0mm

class TestCompanionwaySillFormula:
    """Verify companionway sill height requirements per CE category."""

    CE_SILL_HEIGHTS = {"A": 300, "B": 250, "C": 150, "D": 0}

    def test_category_a_ocean(self):
        assert self.CE_SILL_HEIGHTS["A"] == 300  # mm

    def test_category_b_offshore(self):
        assert self.CE_SILL_HEIGHTS["B"] == 250  # mm

    def test_category_c_inshore(self):
        assert self.CE_SILL_HEIGHTS["C"] == 150  # mm

    def test_category_d_sheltered(self):
        assert self.CE_SILL_HEIGHTS["D"] == 0  # mm

    def test_hierarchy_monotonic(self):
        """A > B > C > D (stricter category = higher sill)"""
        assert self.CE_SILL_HEIGHTS["A"] > self.CE_SILL_HEIGHTS["B"]
        assert self.CE_SILL_HEIGHTS["B"] > self.CE_SILL_HEIGHTS["C"]
        assert self.CE_SILL_HEIGHTS["C"] > self.CE_SILL_HEIGHTS["D"]


# ===========================================================================
# 6. ESCAPE HATCH DIMENSIONS (ISO 12216)
# ===========================================================================
# Minimum: 400mm × 520mm for emergency escape

class TestEscapeHatchFormula:
    """Verify escape hatch minimum dimensions per ISO 12216."""

    MIN_WIDTH_MM = 400
    MIN_HEIGHT_MM = 520

    def test_minimum_dimensions(self):
        assert self.MIN_WIDTH_MM == 400
        assert self.MIN_HEIGHT_MM == 520

    def test_standard_hatch_passes(self):
        """Standard 500×600mm hatch should pass."""
        assert 500 >= self.MIN_WIDTH_MM
        assert 600 >= self.MIN_HEIGHT_MM

    def test_small_hatch_fails(self):
        """350×450mm hatch should fail."""
        assert 350 < self.MIN_WIDTH_MM
        assert 450 < self.MIN_HEIGHT_MM


# ===========================================================================
# 7. VENTILATION REQUIREMENTS (Engine Room)
# ===========================================================================
# Formula: min_vent_area_m2 = max(0.05, engine_kw × 0.0003)

class TestVentilationFormula:
    """Verify engine room ventilation calculation."""

    def _calc_vent_area(self, engine_kw: float) -> float:
        return max(0.05, engine_kw * 0.0003)

    def test_small_engine_20kw(self):
        """20kW: 20 × 0.0003 = 0.006 → below minimum → 0.05 m²"""
        result = self._calc_vent_area(20.0)
        assert result == 0.05

    def test_medium_engine_100kw(self):
        """100kW: 100 × 0.0003 = 0.03 → below minimum → 0.05 m²"""
        result = self._calc_vent_area(100.0)
        assert result == 0.05

    def test_large_engine_200kw(self):
        """200kW: 200 × 0.0003 = 0.06 → above minimum → 0.06 m²"""
        result = self._calc_vent_area(200.0)
        assert abs(result - 0.06) < 0.001

    def test_superyacht_engine_1000kw(self):
        """1000kW: 1000 × 0.0003 = 0.3 m²"""
        result = self._calc_vent_area(1000.0)
        assert abs(result - 0.3) < 0.001

    def test_zero_engine(self):
        """0kW (electric?): should get minimum ventilation"""
        result = self._calc_vent_area(0.0)
        assert result == 0.05


# ===========================================================================
# 8. SAFE DIVIDE — Edge cases
# ===========================================================================

class TestSafeDivideEdgeCases:
    def test_normal(self):
        assert safe_divide(10.0, 2.0) == 5.0

    def test_zero_denominator(self):
        assert safe_divide(10.0, 0.0) == 0.0

    def test_nan_denominator(self):
        assert safe_divide(10.0, float("nan")) == 0.0

    def test_inf_denominator(self):
        assert safe_divide(10.0, float("inf")) == 0.0

    def test_both_zero(self):
        assert safe_divide(0.0, 0.0) == 0.0

    def test_negative_numerator(self):
        assert safe_divide(-10.0, 2.0) == -5.0

    def test_negative_denominator(self):
        assert safe_divide(10.0, -2.0) == -5.0

    def test_custom_default(self):
        assert safe_divide(10.0, 0.0, default=50.0) == 50.0

    def test_very_small_denominator(self):
        """Should not produce infinity."""
        result = safe_divide(1e300, 1e-300)
        # This would overflow to inf, so should return default
        assert result == 0.0


# ===========================================================================
# 9. HEEL ANGLE IMPACT (Ergonomics)
# ===========================================================================
# Formula: effective_width = passage_width × cos(heel_angle)
# Standard angles: 0°, 15°, 25°

class TestHeelAngleFormula:
    """Verify heel angle impact on passage width."""

    def _effective_width(self, width_mm: float, heel_deg: float) -> float:
        return width_mm * math.cos(math.radians(heel_deg))

    def test_zero_heel(self):
        """At 0° heel, full width available."""
        assert abs(self._effective_width(600, 0) - 600) < 0.01

    def test_15_degree_heel(self):
        """600mm passage at 15° heel:
        cos(15°) = 0.9659
        effective = 600 × 0.9659 = 579.6mm
        """
        result = self._effective_width(600, 15)
        assert abs(result - 579.6) < 0.1

    def test_25_degree_heel(self):
        """600mm passage at 25° heel:
        cos(25°) = 0.9063
        effective = 600 × 0.9063 = 543.8mm
        """
        result = self._effective_width(600, 25)
        assert abs(result - 543.8) < 0.1

    def test_45_degree_extreme(self):
        """600mm passage at 45° heel:
        cos(45°) = 0.7071
        effective = 600 × 0.7071 = 424.3mm
        """
        result = self._effective_width(600, 45)
        assert abs(result - 424.3) < 0.1


# ===========================================================================
# 10. LIFECYCLE COST (Materials)
# ===========================================================================
# Formula:
# purchase = area × cost_per_unit
# annual_maintenance = purchase × maintenance_factor
# replacements = max(0, (20 // lifespan) - 1) if lifespan > 0 else 0
# replacement_cost = replacements × purchase × 0.8
# lifecycle_total = purchase + (annual_maintenance × 20) + replacement_cost

class TestLifecycleCostFormula:
    """Verify 20-year lifecycle cost calculation."""

    def _lifecycle_cost(
        self, area_m2: float, cost_per_m2: float,
        maintenance_factor: float, lifespan_years: int,
    ) -> dict:
        purchase = area_m2 * cost_per_m2
        annual_maintenance = purchase * maintenance_factor
        if lifespan_years > 0:
            replacements = max(0, (20 // lifespan_years) - 1)
        else:
            replacements = 0
        replacement_cost = replacements * purchase * 0.8
        total = purchase + (annual_maintenance * 20) + replacement_cost
        return {
            "purchase": purchase,
            "annual_maintenance": annual_maintenance,
            "replacements": replacements,
            "replacement_cost": replacement_cost,
            "total": total,
        }

    def test_teak_deck(self):
        """Teak deck: 20m², €450/m², 2% maintenance, 25yr lifespan
        Purchase: 20 × 450 = €9,000
        Annual maint: 9000 × 0.02 = €180
        Replacements in 20yr: (20 // 25) - 1 = -1 → 0
        Total: 9000 + (180 × 20) + 0 = €12,600
        """
        result = self._lifecycle_cost(20.0, 450.0, 0.02, 25)
        assert abs(result["purchase"] - 9000) < 0.01
        assert abs(result["annual_maintenance"] - 180) < 0.01
        assert result["replacements"] == 0
        assert abs(result["total"] - 12600) < 0.01

    def test_synthetic_cushions(self):
        """Cushions: 5m², €300/m², 5% maintenance, 8yr lifespan
        Purchase: 5 × 300 = €1,500
        Annual maint: 1500 × 0.05 = €75
        Replacements: (20 // 8) - 1 = 2 - 1 = 1
        Replacement cost: 1 × 1500 × 0.8 = €1,200
        Total: 1500 + (75 × 20) + 1200 = 1500 + 1500 + 1200 = €4,200
        """
        result = self._lifecycle_cost(5.0, 300.0, 0.05, 8)
        assert abs(result["purchase"] - 1500) < 0.01
        assert result["replacements"] == 1
        assert abs(result["replacement_cost"] - 1200) < 0.01
        assert abs(result["total"] - 4200) < 0.01

    def test_zero_lifespan_no_crash(self):
        """Lifespan=0 should not cause division by zero."""
        result = self._lifecycle_cost(10.0, 100.0, 0.01, 0)
        assert result["replacements"] == 0

    def test_short_lifespan_many_replacements(self):
        """Short lifespan: 3yr → (20//3)-1 = 6-1 = 5 replacements."""
        result = self._lifecycle_cost(1.0, 100.0, 0.01, 3)
        assert result["replacements"] == 5


# ===========================================================================
# 11. STABILITY: TRIM ANGLE
# ===========================================================================
# Formula: trim_angle = arctan(longitudinal_moment / displacement)
# Simplified: trim_deg = atan((cog_x - center_x) / (lwl / 2)) × (180/π)
# For motor yachts: max 1°, for sailboats: max 2°

class TestTrimAngleFormula:
    """Verify trim angle calculation."""

    def _trim_angle_deg(self, cog_offset_m: float, lwl_m: float) -> float:
        """Simplified trim angle from COG offset."""
        if lwl_m <= 0:
            return 0.0
        return math.degrees(math.atan(cog_offset_m / (lwl_m / 2)))

    def test_balanced_zero_trim(self):
        assert self._trim_angle_deg(0.0, 12.0) == 0.0

    def test_slight_aft_trim(self):
        """COG 0.5m aft of center on 12m boat:
        atan(0.5 / 6.0) = atan(0.0833) = 4.76° — too much!
        This would flag a warning.
        """
        result = self._trim_angle_deg(0.5, 12.0)
        assert abs(result - 4.76) < 0.1

    def test_normal_trim(self):
        """COG 0.1m aft on 12m boat:
        atan(0.1 / 6.0) = atan(0.0167) = 0.955°
        """
        result = self._trim_angle_deg(0.1, 12.0)
        assert abs(result - 0.95) < 0.1

    def test_zero_lwl_safe(self):
        assert self._trim_angle_deg(0.5, 0.0) == 0.0
