"""Structural analysis module for yacht layouts (weight distribution).

Evaluates weight distribution and center of gravity placement using
heuristic weight estimation from zone types and polygon geometry.
Pure function module — no database access.
All user-facing strings are in German.
"""
import logging

logger = logging.getLogger(__name__)

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "ideal_cog_x_range": (0.42, 0.52),
        "lateral_tolerance_pct": 0.03,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 0.7,
        "weights": {
            "fore_aft": 0.35,
            "lateral": 0.25,
            "heavy_placement": 0.20,
            "load_concentration": 0.20,
        },
    },
    "cruising_sail": {
        "ideal_cog_x_range": (0.44, 0.54),
        "lateral_tolerance_pct": 0.05,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 1.0,
        "weights": {
            "fore_aft": 0.30,
            "lateral": 0.25,
            "heavy_placement": 0.25,
            "load_concentration": 0.20,
        },
    },
    "large_motor": {
        "ideal_cog_x_range": (0.48, 0.58),
        "lateral_tolerance_pct": 0.08,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 1.3,
        "weights": {
            "fore_aft": 0.25,
            "lateral": 0.25,
            "heavy_placement": 0.30,
            "load_concentration": 0.20,
        },
    },
    "superyacht": {
        "ideal_cog_x_range": (0.46, 0.56),
        "lateral_tolerance_pct": 0.06,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 1.6,
        "weights": {
            "fore_aft": 0.25,
            "lateral": 0.25,
            "heavy_placement": 0.30,
            "load_concentration": 0.20,
        },
    },
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}

ZONE_WEIGHT_KG_PER_SQM: dict[str, float] = {
    "engine": 350,
    "storage": 150,
    "tender_garage": 200,
    "pantry": 120,
    "head": 100,
    "salon": 80,
    "cabin": 70,
    "crew_quarters": 70,
    "helm": 60,
    "cockpit": 40,
    "flybridge": 35,
    "foredeck": 25,
    "swim_platform": 30,
}

_DEFAULT_WEIGHT_KG_PER_SQM = 50.0

_HEAVY_ZONE_TYPES = {"engine", "storage", "tender_garage"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _polygon_area_sqm(polygon: list[list[float]]) -> float:
    """Compute polygon area in square meters (input in mm)."""
    n = len(polygon)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2.0 / 1_000_000


def _polygon_centroid(polygon: list[list[float]]) -> tuple[float, float]:
    """Compute centroid of polygon (input and output in mm)."""
    n = len(polygon)
    if n == 0:
        return 0.0, 0.0
    if n < 3:
        cx = sum(p[0] for p in polygon) / n
        cy = sum(p[1] for p in polygon) / n
        return cx, cy
    signed_area = 0.0
    cx = 0.0
    cy = 0.0
    for i in range(n):
        j = (i + 1) % n
        cross = polygon[i][0] * polygon[j][1] - polygon[j][0] * polygon[i][1]
        signed_area += cross
        cx += (polygon[i][0] + polygon[j][0]) * cross
        cy += (polygon[i][1] + polygon[j][1]) * cross
    signed_area /= 2.0
    if abs(signed_area) < 1e-10:
        cx = sum(p[0] for p in polygon) / n
        cy = sum(p[1] for p in polygon) / n
        return cx, cy
    cx /= 6.0 * abs(signed_area)
    cy /= 6.0 * abs(signed_area)
    return cx, cy


def _estimate_zone_weight(zone: dict, weight_factor: float) -> float:
    """Estimate zone weight in kg from type, area, and boat class factor."""
    polygon = zone.get("polygon", [])
    area_sqm = _polygon_area_sqm(polygon)
    zone_type = zone.get("zone_type", "")
    kg_per_sqm = ZONE_WEIGHT_KG_PER_SQM.get(zone_type, _DEFAULT_WEIGHT_KG_PER_SQM)
    return area_sqm * kg_per_sqm * weight_factor


def _get_boat_extents(zones: list[dict]) -> tuple[float, float, float, float]:
    """Get bounding box of all zone polygons: (min_x, max_x, min_y, max_y) in mm."""
    all_x = []
    all_y = []
    for z in zones:
        for p in z.get("polygon", []):
            all_x.append(p[0])
            all_y.append(p[1])
    if not all_x:
        return 0.0, 0.0, 0.0, 0.0
    return min(all_x), max(all_x), min(all_y), max(all_y)


# ---------------------------------------------------------------------------
# Sub-analysis: Longitudinal (fore-aft) balance
# ---------------------------------------------------------------------------


def analyze_fore_aft_balance(
    zones: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Evaluate fore-aft weight balance via weighted X-centroid.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "code": "STRUCTURAL_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen für Längsverteilungsanalyse vorhanden.",
            "suggestion": "Zonen dem Layout zuweisen.",
        })
        return 50.0, warnings, {"cog_x_pct": 0.0, "ideal_range": [0, 0], "deviation_pct": 0.0}

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    ideal_range = config.get("ideal_cog_x_range", (0.44, 0.54))
    min_x, max_x, _, _ = _get_boat_extents(zones)
    x_span = max_x - min_x

    if x_span < 1e-6:
        return 50.0, warnings, {"cog_x_pct": 0.5, "ideal_range": list(ideal_range), "deviation_pct": 0.0}

    total_weight = 0.0
    weighted_x = 0.0

    for z in zones:
        w = _estimate_zone_weight(z, weight_factor)
        cx, _ = _polygon_centroid(z.get("polygon", []))
        total_weight += w
        weighted_x += cx * w

    if total_weight < 1e-6:
        return 50.0, warnings, {"cog_x_pct": 0.5, "ideal_range": list(ideal_range), "deviation_pct": 0.0}

    cog_x = weighted_x / total_weight
    cog_x_pct = (cog_x - min_x) / x_span

    # Score
    deviation = 0.0
    if ideal_range[0] <= cog_x_pct <= ideal_range[1]:
        deviation = 0.0
        score = 100.0
    else:
        if cog_x_pct < ideal_range[0]:
            deviation = ideal_range[0] - cog_x_pct
        else:
            deviation = cog_x_pct - ideal_range[1]
        # 6.67 per percentage point → score reaches 0 at 15 pp deviation
        score = max(0.0, 100.0 - deviation * 100.0 * 6.67)

    # Warnings
    if cog_x_pct < ideal_range[0]:
        severity = "critical" if deviation > 0.10 else "warning"
        warnings.append({
            "code": "COG_TOO_FAR_FORWARD",
            "severity": severity,
            "message": (
                f"Gewichtsschwerpunkt bei {cog_x_pct:.0%} der Bootslänge — "
                f"zu weit vorne (Ideal: {ideal_range[0]:.0%}–{ideal_range[1]:.0%})."
            ),
            "suggestion": "Schwere Ausrüstung weiter achtern verlagern.",
        })
    elif cog_x_pct > ideal_range[1]:
        severity = "critical" if deviation > 0.10 else "warning"
        warnings.append({
            "code": "COG_TOO_FAR_AFT",
            "severity": severity,
            "message": (
                f"Gewichtsschwerpunkt bei {cog_x_pct:.0%} der Bootslänge — "
                f"zu weit achtern (Ideal: {ideal_range[0]:.0%}–{ideal_range[1]:.0%})."
            ),
            "suggestion": "Schwere Ausrüstung weiter nach vorne verlagern.",
        })

    return score, warnings, {
        "cog_x_pct": round(cog_x_pct, 4),
        "ideal_range": list(ideal_range),
        "deviation_pct": round(deviation, 4),
    }


# ---------------------------------------------------------------------------
# Sub-analysis: Lateral balance
# ---------------------------------------------------------------------------


def analyze_lateral_balance(
    zones: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Evaluate port-starboard weight balance via weighted Y-centroid.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "code": "STRUCTURAL_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen für Querverteilungsanalyse vorhanden.",
            "suggestion": "Zonen dem Layout zuweisen.",
        })
        return 50.0, warnings, {"cog_y_pct": 0.5, "offset_from_center_pct": 0.0, "tolerance_pct": 0.0}

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    tolerance = config.get("lateral_tolerance_pct", 0.05)
    _, _, min_y, max_y = _get_boat_extents(zones)
    y_span = max_y - min_y

    if y_span < 1e-6:
        return 100.0, warnings, {"cog_y_pct": 0.5, "offset_from_center_pct": 0.0, "tolerance_pct": tolerance}

    total_weight = 0.0
    weighted_y = 0.0

    for z in zones:
        w = _estimate_zone_weight(z, weight_factor)
        _, cy = _polygon_centroid(z.get("polygon", []))
        total_weight += w
        weighted_y += cy * w

    if total_weight < 1e-6:
        return 50.0, warnings, {"cog_y_pct": 0.5, "offset_from_center_pct": 0.0, "tolerance_pct": tolerance}

    cog_y = weighted_y / total_weight
    cog_y_pct = (cog_y - min_y) / y_span
    offset = abs(cog_y_pct - 0.5)

    if offset <= tolerance:
        score = 100.0
    else:
        excess = offset - tolerance
        # 10 per percentage point -> score reaches 0 at 10 pp beyond tolerance
        score = max(0.0, 100.0 - excess * 100.0 * 10.0)

    if offset > tolerance:
        severity = "critical" if offset > tolerance * 2 else "warning"
        warnings.append({
            "code": "COG_LATERAL_OFFSET",
            "severity": severity,
            "message": (
                f"Gewichtsschwerpunkt {offset:.1%} seitlich versetzt — "
                f"Toleranz: ±{tolerance:.0%} von Mittschiffs."
            ),
            "suggestion": "Schwere Ausrüstung symmetrischer verteilen.",
        })

    return score, warnings, {
        "cog_y_pct": round(cog_y_pct, 4),
        "offset_from_center_pct": round(offset, 4),
        "tolerance_pct": tolerance,
    }
