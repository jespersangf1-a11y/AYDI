"""Unit conversion system for AYDI.

Supports metric (default) and imperial units.
All internal calculations use metric (SI). Conversion happens
only at input/output boundaries.

Coordinates: mm (internal)
Lengths: m (internal)
Weights: kg (internal)
Volumes: liters (internal)
Speeds: knots (internal, nautical standard)
Costs: EUR (internal)
Temperatures: Celsius (internal)
"""

from __future__ import annotations

import math
from enum import Enum
from typing import NamedTuple


class UnitSystem(str, Enum):
    METRIC = "metric"
    IMPERIAL = "imperial"


class ConversionFactor(NamedTuple):
    """Multiply metric value by this factor to get imperial."""
    to_imperial: float
    metric_unit: str
    imperial_unit: str


# ---------------------------------------------------------------------------
# Conversion factors: metric -> imperial
# ---------------------------------------------------------------------------

CONVERSIONS: dict[str, ConversionFactor] = {
    # Length
    "mm_to_inch": ConversionFactor(1.0 / 25.4, "mm", "in"),
    "m_to_ft": ConversionFactor(3.28084, "m", "ft"),
    "m_to_yard": ConversionFactor(1.09361, "m", "yd"),
    "km_to_nm": ConversionFactor(0.539957, "km", "NM"),
    "nm_to_nm": ConversionFactor(1.0, "NM", "NM"),  # already nautical
    "m_to_fathom": ConversionFactor(0.546807, "m", "ftm"),

    # Area
    "m2_to_ft2": ConversionFactor(10.7639, "m\u00b2", "ft\u00b2"),

    # Volume
    "l_to_gal_us": ConversionFactor(0.264172, "l", "gal"),
    "l_to_gal_imp": ConversionFactor(0.219969, "l", "imp gal"),
    "m3_to_ft3": ConversionFactor(35.3147, "m\u00b3", "ft\u00b3"),

    # Weight / Mass
    "kg_to_lbs": ConversionFactor(2.20462, "kg", "lbs"),
    "kg_to_ton_metric": ConversionFactor(0.001, "kg", "t"),
    "kg_to_ton_long": ConversionFactor(0.000984207, "kg", "long ton"),

    # Speed
    "kn_to_mph": ConversionFactor(1.15078, "kn", "mph"),
    "kn_to_kmh": ConversionFactor(1.852, "kn", "km/h"),
    "ms_to_kn": ConversionFactor(1.94384, "m/s", "kn"),

    # Power
    "kw_to_hp": ConversionFactor(1.34102, "kW", "HP"),
    "kw_to_ps": ConversionFactor(1.35962, "kW", "PS"),

    # Pressure
    "kpa_to_psi": ConversionFactor(0.145038, "kPa", "psi"),
    "bar_to_psi": ConversionFactor(14.5038, "bar", "psi"),

    # Temperature (handled specially — not a simple multiplication)
}


def convert(
    value: float,
    conversion_key: str,
    *,
    reverse: bool = False,
) -> float:
    """Convert a value using a named conversion.

    Args:
        value: The numeric value to convert.
        conversion_key: Key from CONVERSIONS dict (e.g. "m_to_ft").
        reverse: If True, convert imperial -> metric instead.

    Returns:
        Converted value.

    Raises:
        KeyError: If conversion_key is unknown.
        ValueError: If value is not finite.
    """
    if not math.isfinite(value):
        raise ValueError(f"Cannot convert non-finite value: {value}")

    factor = CONVERSIONS[conversion_key]

    if reverse:
        if factor.to_imperial == 0:
            raise ValueError(f"Cannot reverse-convert with zero factor: {conversion_key}")
        return value / factor.to_imperial
    return value * factor.to_imperial


def celsius_to_fahrenheit(celsius: float) -> float:
    """Convert Celsius to Fahrenheit."""
    if not math.isfinite(celsius):
        raise ValueError(f"Cannot convert non-finite temperature: {celsius}")
    return celsius * 9.0 / 5.0 + 32.0


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """Convert Fahrenheit to Celsius."""
    if not math.isfinite(fahrenheit):
        raise ValueError(f"Cannot convert non-finite temperature: {fahrenheit}")
    return (fahrenheit - 32.0) * 5.0 / 9.0


# ---------------------------------------------------------------------------
# Batch conversion helpers
# ---------------------------------------------------------------------------

def convert_dimensions(
    length_m: float,
    beam_m: float,
    draft_m: float,
    system: UnitSystem = UnitSystem.METRIC,
) -> dict[str, float | str]:
    """Convert standard yacht dimensions to the requested unit system.

    Returns dict with values and unit labels.
    """
    if system == UnitSystem.METRIC:
        return {
            "length": length_m,
            "beam": beam_m,
            "draft": draft_m,
            "unit": "m",
        }
    return {
        "length": round(convert(length_m, "m_to_ft"), 1),
        "beam": round(convert(beam_m, "m_to_ft"), 1),
        "draft": round(convert(draft_m, "m_to_ft"), 1),
        "unit": "ft",
    }


def convert_weight(
    kg: float,
    system: UnitSystem = UnitSystem.METRIC,
) -> dict[str, float | str]:
    """Convert weight to the requested unit system."""
    if system == UnitSystem.METRIC:
        if kg >= 1000:
            return {"value": round(kg / 1000, 2), "unit": "t"}
        return {"value": round(kg, 1), "unit": "kg"}
    lbs = convert(kg, "kg_to_lbs")
    if lbs >= 2240:  # long ton threshold
        return {"value": round(convert(kg, "kg_to_ton_long"), 2), "unit": "long ton"}
    return {"value": round(lbs, 0), "unit": "lbs"}


def convert_volume(
    liters: float,
    system: UnitSystem = UnitSystem.METRIC,
) -> dict[str, float | str]:
    """Convert volume to the requested unit system."""
    if system == UnitSystem.METRIC:
        return {"value": round(liters, 1), "unit": "l"}
    return {"value": round(convert(liters, "l_to_gal_us"), 1), "unit": "gal"}


def convert_speed(
    knots: float,
    system: UnitSystem = UnitSystem.METRIC,
) -> dict[str, float | str]:
    """Convert speed. Knots are the international standard for maritime."""
    # Knots are universal in maritime — always return knots
    return {"value": round(knots, 1), "unit": "kn"}


def convert_power(
    kw: float,
    system: UnitSystem = UnitSystem.METRIC,
) -> dict[str, float | str]:
    """Convert power to the requested unit system."""
    if system == UnitSystem.METRIC:
        return {"value": round(kw, 1), "unit": "kW"}
    return {"value": round(convert(kw, "kw_to_hp"), 0), "unit": "HP"}


# ---------------------------------------------------------------------------
# Hull speed formula (frequently used, needs correct unit handling)
# ---------------------------------------------------------------------------

def hull_speed_knots(lwl_m: float) -> float:
    """Calculate theoretical hull speed in knots from waterline length in meters.

    Formula: V_max = 1.34 * sqrt(LWL_ft) [knots]
    Or equivalently: V_max = 2.43 * sqrt(LWL_m) [km/h] then convert.

    Args:
        lwl_m: Waterline length in meters. Must be >= 0.

    Returns:
        Hull speed in knots. Returns 0.0 for lwl_m <= 0.

    Raises:
        ValueError: If lwl_m is not finite.
    """
    if not math.isfinite(lwl_m):
        raise ValueError(f"LWL must be finite, got: {lwl_m}")
    if lwl_m <= 0:
        return 0.0

    lwl_ft = convert(lwl_m, "m_to_ft")
    return 1.34 * math.sqrt(lwl_ft)


# ---------------------------------------------------------------------------
# Safe math helpers (for analysis modules)
# ---------------------------------------------------------------------------

def safe_divide(
    numerator: float,
    denominator: float,
    *,
    default: float = 0.0,
    context: str = "",
) -> float:
    """Division with zero/infinity protection.

    Args:
        numerator: The dividend.
        denominator: The divisor.
        default: Value to return on division by zero or non-finite result.
        context: Description for logging (optional).

    Returns:
        Result or default value.
    """
    if denominator == 0 or not math.isfinite(denominator):
        return default
    result = numerator / denominator
    if not math.isfinite(result):
        return default
    return result


def clamp(value: float, min_val: float, max_val: float) -> float:
    """Clamp a value to [min_val, max_val] range."""
    return max(min_val, min(max_val, value))


def safe_sqrt(value: float, *, context: str = "") -> float:
    """Square root with negative-value protection."""
    if value < 0:
        return 0.0
    return math.sqrt(value)
