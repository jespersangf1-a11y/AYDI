"""Structural analysis module for yacht layouts (weight distribution).

Evaluates weight distribution and center of gravity placement using
heuristic weight estimation from zone types and polygon geometry.
Pure function module — no database access.
All user-facing strings are in German.
"""
import logging
import math

logger = logging.getLogger(__name__)

# Try to import knowledge databases for enriched structural analysis
try:
    from app.services.knowledge.hull_construction_deep import (
        CONSTRUCTION_METHODS_DATABASE,
        HULL_DECK_JOINT_DATABASE,
    )
except ImportError:
    CONSTRUCTION_METHODS_DATABASE = {}
    HULL_DECK_JOINT_DATABASE = {}

try:
    from app.services.knowledge.keel_rudder_underwater_deep import (
        KEEL_DATABASE,
    )
except ImportError:
    KEEL_DATABASE = {}

# Import central knowledge retrieval for markdown knowledge integration
try:
    from app.services.knowledge.knowledge_retrieval import (
        get_knowledge_for_structural_analysis as _get_md_structural_knowledge,
        MARKDOWN_LOADER_AVAILABLE as _MD_AVAILABLE,
    )
except ImportError:
    _MD_AVAILABLE = False

    def _get_md_structural_knowledge(*a, **kw):
        return {}

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "ideal_cog_x_range": (0.42, 0.52),
        "lateral_tolerance_pct": 0.03,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 0.7,
        "max_trim_deg": 2.0,
        "weights": {
            "fore_aft": 0.30,
            "lateral": 0.21,
            "heavy_placement": 0.17,
            "load_concentration": 0.17,
            "loading_conditions": 0.10,
            "trim": 0.05,
        },
    },
    "cruising_sail": {
        "ideal_cog_x_range": (0.44, 0.54),
        "lateral_tolerance_pct": 0.05,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 1.0,
        "max_trim_deg": 2.0,
        "weights": {
            "fore_aft": 0.26,
            "lateral": 0.21,
            "heavy_placement": 0.21,
            "load_concentration": 0.17,
            "loading_conditions": 0.10,
            "trim": 0.05,
        },
    },
    "large_motor": {
        "ideal_cog_x_range": (0.48, 0.58),
        "lateral_tolerance_pct": 0.08,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 1.3,
        "max_trim_deg": 1.0,
        "weights": {
            "fore_aft": 0.21,
            "lateral": 0.21,
            "heavy_placement": 0.26,
            "load_concentration": 0.17,
            "loading_conditions": 0.10,
            "trim": 0.05,
        },
    },
    "racing_sail": {
        "ideal_cog_x_range": (0.45, 0.55),
        "lateral_tolerance_pct": 0.02,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 0.6,
        "max_trim_deg": 2.0,
        "weights": {
            "fore_aft": 0.34,
            "lateral": 0.21,
            "heavy_placement": 0.13,
            "load_concentration": 0.17,
            "loading_conditions": 0.10,
            "trim": 0.05,
        },
    },
    "daysailer": {
        "ideal_cog_x_range": (0.43, 0.53),
        "lateral_tolerance_pct": 0.03,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 0.75,
        "max_trim_deg": 2.0,
        "weights": {
            "fore_aft": 0.30,
            "lateral": 0.21,
            "heavy_placement": 0.17,
            "load_concentration": 0.17,
            "loading_conditions": 0.10,
            "trim": 0.05,
        },
    },
    "motorsailer": {
        "ideal_cog_x_range": (0.46, 0.56),
        "lateral_tolerance_pct": 0.05,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 1.1,
        "max_trim_deg": 1.5,
        "weights": {
            "fore_aft": 0.26,
            "lateral": 0.21,
            "heavy_placement": 0.21,
            "load_concentration": 0.17,
            "loading_conditions": 0.10,
            "trim": 0.05,
        },
    },
    "catamaran_sail": {
        "ideal_cog_x_range": (0.44, 0.54),
        "lateral_tolerance_pct": 0.04,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 0.85,
        "max_trim_deg": 1.5,
        "weights": {
            "fore_aft": 0.28,
            "lateral": 0.21,
            "heavy_placement": 0.19,
            "load_concentration": 0.17,
            "loading_conditions": 0.10,
            "trim": 0.05,
        },
    },
    "catamaran_motor": {
        "ideal_cog_x_range": (0.48, 0.58),
        "lateral_tolerance_pct": 0.07,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 1.2,
        "max_trim_deg": 1.0,
        "weights": {
            "fore_aft": 0.21,
            "lateral": 0.21,
            "heavy_placement": 0.26,
            "load_concentration": 0.17,
            "loading_conditions": 0.10,
            "trim": 0.05,
        },
    },
    "small_motor": {
        "ideal_cog_x_range": (0.47, 0.57),
        "lateral_tolerance_pct": 0.06,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 1.0,
        "max_trim_deg": 1.0,
        "weights": {
            "fore_aft": 0.21,
            "lateral": 0.21,
            "heavy_placement": 0.26,
            "load_concentration": 0.17,
            "loading_conditions": 0.10,
            "trim": 0.05,
        },
    },
    "sport_cruiser": {
        "ideal_cog_x_range": (0.48, 0.58),
        "lateral_tolerance_pct": 0.07,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 1.1,
        "max_trim_deg": 1.0,
        "weights": {
            "fore_aft": 0.21,
            "lateral": 0.21,
            "heavy_placement": 0.26,
            "load_concentration": 0.17,
            "loading_conditions": 0.10,
            "trim": 0.05,
        },
    },
    "trawler": {
        "ideal_cog_x_range": (0.49, 0.59),
        "lateral_tolerance_pct": 0.08,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 1.4,
        "max_trim_deg": 1.0,
        "weights": {
            "fore_aft": 0.21,
            "lateral": 0.21,
            "heavy_placement": 0.26,
            "load_concentration": 0.17,
            "loading_conditions": 0.10,
            "trim": 0.05,
        },
    },
    "explorer": {
        "ideal_cog_x_range": (0.47, 0.57),
        "lateral_tolerance_pct": 0.06,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 1.5,
        "max_trim_deg": 1.5,
        "weights": {
            "fore_aft": 0.26,
            "lateral": 0.21,
            "heavy_placement": 0.21,
            "load_concentration": 0.17,
            "loading_conditions": 0.10,
            "trim": 0.05,
        },
    },
    "superyacht": {
        "ideal_cog_x_range": (0.46, 0.56),
        "lateral_tolerance_pct": 0.06,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 1.6,
        "max_trim_deg": 1.0,
        "weights": {
            "fore_aft": 0.21,
            "lateral": 0.21,
            "heavy_placement": 0.26,
            "load_concentration": 0.17,
            "loading_conditions": 0.10,
            "trim": 0.05,
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
    cx /= 6.0 * signed_area
    cy /= 6.0 * signed_area
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


def _valid_point_masses(structural_items: list[dict] | None) -> list[dict]:
    """Measured structural items usable as point masses.

    Requires finite weight_kg > 0 and an X position. Measured weights are
    real kg — the same unit as the zone heuristic (area × kg/m² × class
    factor), so combining both into one CG model is unit-consistent.
    """
    if not structural_items:
        return []
    masses: list[dict] = []
    for item in structural_items:
        try:
            weight = float(item.get("weight_kg") or 0.0)
        except (TypeError, ValueError):
            continue
        x = item.get("position_x_mm")
        if not math.isfinite(weight) or weight <= 0 or x is None:
            continue
        y = item.get("position_y_mm")
        masses.append({
            "name": item.get("name") or item.get("item_type") or "Element",
            "item_type": str(item.get("item_type") or "").lower(),
            "zone_name": item.get("zone_name"),
            "weight_kg": weight,
            "x_mm": float(x),
            "y_mm": float(y) if y is not None else None,
        })
    return masses


def _clamp01(value: float) -> float:
    return max(0.0, min(1.0, value))


def _point_in_polygon(x: float, y: float, polygon: list[list[float]]) -> bool:
    """Ray-casting point-in-polygon test."""
    n = len(polygon)
    if n < 3:
        return False
    inside = False
    j = n - 1
    for i in range(n):
        xi, yi = polygon[i][0], polygon[i][1]
        xj, yj = polygon[j][0], polygon[j][1]
        if (yi > y) != (yj > y):
            x_cross = (xj - xi) * (y - yi) / (yj - yi) + xi
            if x < x_cross:
                inside = not inside
        j = i
    return inside


# Exact tank types (schema enum) — substring matching wrongly treated a
# 'watermaker' as water ballast and a generic 'tank' as fuel.
_FUEL_TANK_TYPES = {"fuel_tank"}
_WATER_TANK_TYPES = {"water_tank"}
# Item types that count as "heavy placement" concerns regardless of weight,
# plus a weight threshold for anything else.
_HEAVY_ITEM_TYPES = {"engine", "ballast", "fuel_tank", "water_tank"}
_HEAVY_ITEM_MIN_KG = 150.0


def _build_weight_model(
    zones: list[dict],
    weight_factor: float,
    structural_items: list[dict] | None,
) -> tuple[list[dict], list[dict], list[dict]]:
    """Effective weight model combining zone heuristics and measured masses.

    The kg/m² zone heuristic already CONTAINS typical equipment weight (an
    engine zone is 350 kg/m² because of the engine). A measured engine must
    therefore REPLACE its zone's heuristic share, not stack on top of it —
    otherwise the same physical mass is counted twice. Masses are assigned to
    a zone by explicit zone_name first, else by point-in-polygon; the zone's
    heuristic weight is reduced by the assigned measured weight (min 0).

    Returns (zone_entries, masses, outside_masses):
      zone_entries: [{zone, weight (effective), cx, cy}]
      masses: valid point masses, each with "assigned_zone" (name or None)
      outside_masses: masses whose X lies outside the zone extents
        (legitimate — e.g. anchor locker — but flagged for transparency;
        the evaluation frame stays the zone extents, see analyses).
    """
    masses = _valid_point_masses(structural_items)
    zones_by_name = {z.get("name"): z for z in zones if z.get("name")}
    reductions: dict[int, float] = {}

    for mass in masses:
        zone = None
        zone_name = mass.get("zone_name")
        if zone_name and zone_name in zones_by_name:
            zone = zones_by_name[zone_name]
        elif mass["y_mm"] is not None:
            for z in zones:
                if _point_in_polygon(mass["x_mm"], mass["y_mm"], z.get("polygon", [])):
                    zone = z
                    break
        mass["assigned_zone"] = zone.get("name") if zone else None
        if zone is not None:
            reductions[id(zone)] = reductions.get(id(zone), 0.0) + mass["weight_kg"]

    zone_entries: list[dict] = []
    for z in zones:
        heuristic = _estimate_zone_weight(z, weight_factor)
        effective = max(0.0, heuristic - reductions.get(id(z), 0.0))
        cx, cy = _polygon_centroid(z.get("polygon", []))
        zone_entries.append({"zone": z, "weight": effective, "cx": cx, "cy": cy})

    min_x, max_x, _, _ = _get_boat_extents(zones)
    outside = [m for m in masses if not (min_x <= m["x_mm"] <= max_x)]
    return zone_entries, masses, outside


def _condition_adjusted_item_weight(mass: dict, fuel_pct: float, water_pct: float) -> float:
    """Loading-condition weight of a measured item: exact tank types scale
    with their fill level, everything else (engine, ballast, battery,
    watermaker …) is fixed mass."""
    if mass["item_type"] in _FUEL_TANK_TYPES:
        return mass["weight_kg"] * (fuel_pct / 100.0)
    if mass["item_type"] in _WATER_TANK_TYPES:
        return mass["weight_kg"] * (water_pct / 100.0)
    return mass["weight_kg"]


# ---------------------------------------------------------------------------
# Sub-analysis: Longitudinal (fore-aft) balance
# ---------------------------------------------------------------------------


def analyze_fore_aft_balance(
    zones: list[dict],
    config: dict,
    *,
    structural_items: list[dict] | None = None,
) -> tuple[float, list[dict], dict]:
    """Evaluate fore-aft weight balance via weighted X-centroid.

    Measured structural items (weight_kg + position) enter the CG model as
    point masses alongside the heuristic zone weights.

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
    # Evaluation frame stays the ZONE extents: ideal_cog_x_range is calibrated
    # to the hull/zone bounding box. Extending the frame by item positions
    # shifted every percentage and even inverted warning directions.
    min_x, max_x, _, _ = _get_boat_extents(zones)
    x_span = max_x - min_x

    if x_span < 1e-6:
        return 50.0, warnings, {"cog_x_pct": 0.5, "ideal_range": list(ideal_range), "deviation_pct": 0.0}

    zone_entries, masses, _ = _build_weight_model(zones, weight_factor, structural_items)

    total_weight = 0.0
    weighted_x = 0.0

    for entry in zone_entries:
        total_weight += entry["weight"]
        weighted_x += entry["cx"] * entry["weight"]

    for mass in masses:
        total_weight += mass["weight_kg"]
        weighted_x += mass["x_mm"] * mass["weight_kg"]

    if total_weight < 1e-6:
        return 50.0, warnings, {"cog_x_pct": 0.5, "ideal_range": list(ideal_range), "deviation_pct": 0.0}

    cog_x = weighted_x / total_weight
    cog_x_pct = _clamp01((cog_x - min_x) / x_span)

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
    *,
    structural_items: list[dict] | None = None,
) -> tuple[float, list[dict], dict]:
    """Evaluate port-starboard weight balance via weighted Y-centroid.

    Measured items with a Y position enter the model as point masses.

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
    # Fixed zone frame — see analyze_fore_aft_balance
    _, _, min_y, max_y = _get_boat_extents(zones)
    y_span = max_y - min_y

    if y_span < 1e-6:
        return 100.0, warnings, {"cog_y_pct": 0.5, "offset_from_center_pct": 0.0, "tolerance_pct": tolerance}

    zone_entries, all_masses, _ = _build_weight_model(zones, weight_factor, structural_items)
    # Only items with a Y position can enter a lateral model
    masses = [m for m in all_masses if m["y_mm"] is not None]

    total_weight = 0.0
    weighted_y = 0.0

    for entry in zone_entries:
        total_weight += entry["weight"]
        weighted_y += entry["cy"] * entry["weight"]

    for mass in masses:
        total_weight += mass["weight_kg"]
        weighted_y += mass["y_mm"] * mass["weight_kg"]

    if total_weight < 1e-6:
        return 50.0, warnings, {"cog_y_pct": 0.5, "offset_from_center_pct": 0.0, "tolerance_pct": tolerance}

    cog_y = weighted_y / total_weight
    cog_y_pct = _clamp01((cog_y - min_y) / y_span)
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


# ---------------------------------------------------------------------------
# Sub-analysis: Heavy zone placement
# ---------------------------------------------------------------------------


def analyze_heavy_zone_placement(
    zones: list[dict],
    config: dict,
    *,
    structural_items: list[dict] | None = None,
) -> tuple[float, list[dict], dict]:
    """Check if heavy zones AND heavy measured items are centrally positioned.

    Measured heavy items (engine/ballast/tanks, or anything ≥150 kg) are
    evaluated like heavy zones — a measured 2-t engine must not disappear
    from this sub-score just because no engine ZONE was drawn.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "code": "STRUCTURAL_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen für Schwerzonen-Analyse vorhanden.",
            "suggestion": "Zonen dem Layout zuweisen.",
        })
        return 50.0, warnings, {
            "heavy_zones": [], "total_heavy_weight_kg": 0.0, "central_ratio": 0.0,
        }

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    central_band = config.get("central_band", (0.20, 0.80))
    min_x, max_x, _, _ = _get_boat_extents(zones)
    x_span = max_x - min_x

    zone_entries, masses, _ = _build_weight_model(zones, weight_factor, structural_items)
    heavy_entries = [
        e for e in zone_entries if e["zone"].get("zone_type") in _HEAVY_ZONE_TYPES
    ]
    heavy_masses = [
        m for m in masses
        if m["item_type"] in _HEAVY_ITEM_TYPES or m["weight_kg"] >= _HEAVY_ITEM_MIN_KG
    ]

    if not heavy_entries and not heavy_masses:
        warnings.append({
            "code": "STRUCTURAL_NO_HEAVY_ZONES",
            "severity": "info",
            "message": (
                "Keine schweren Zonen (Motor, Stauraum) und keine schweren "
                "gemessenen Elemente im Layout erkannt."
            ),
            "suggestion": "Motor- und Stauräume im Layout definieren.",
        })
        return 100.0, warnings, {
            "heavy_zones": [], "total_heavy_weight_kg": 0.0, "central_ratio": 1.0,
        }

    if x_span < 1e-6:
        return 100.0, warnings, {
            "heavy_zones": [], "total_heavy_weight_kg": 0.0, "central_ratio": 1.0,
        }

    heavy_info = []
    total_heavy_weight = 0.0
    central_weight = 0.0

    def _evaluate_heavy_point(
        label: str, kind: str, weight: float, cx_pct: float, suggestion: str
    ) -> None:
        nonlocal total_heavy_weight, central_weight
        if weight <= 0:
            return
        is_central = central_band[0] <= cx_pct <= central_band[1]
        total_heavy_weight += weight
        if is_central:
            central_weight += weight
        else:
            severity = "critical" if cx_pct < 0.15 or cx_pct > 0.85 else "warning"
            warnings.append({
                "code": "HEAVY_ZONE_OFF_CENTER",
                "severity": severity,
                "message": (
                    f"{label} bei {cx_pct:.0%} der Bootslänge — außerhalb des "
                    f"zentralen Bereichs ({central_band[0]:.0%}–{central_band[1]:.0%})."
                ),
                "suggestion": suggestion,
            })
        heavy_info.append({
            "name": label,
            "zone_type": kind,
            "centroid_x_pct": round(cx_pct, 4),
            "weight_kg": round(weight, 1),
            "is_central": is_central,
        })

    for entry in heavy_entries:
        z = entry["zone"]
        cx_pct = _clamp01((entry["cx"] - min_x) / x_span)
        _evaluate_heavy_point(
            f"Schwere Zone '{z.get('name', '?')}' ({z.get('zone_type')})",
            str(z.get("zone_type")),
            entry["weight"],
            cx_pct,
            f"Zone '{z.get('name', '?')}' weiter zur Mitte verlagern.",
        )

    for mass in heavy_masses:
        cx_pct = _clamp01((mass["x_mm"] - min_x) / x_span)
        _evaluate_heavy_point(
            f"Gemessenes Element '{mass['name']}' ({mass['item_type']}, "
            f"{mass['weight_kg']:.0f} kg)",
            f"item:{mass['item_type']}",
            mass["weight_kg"],
            cx_pct,
            f"Element '{mass['name']}' weiter zur Mitte verlagern.",
        )

    central_ratio = central_weight / total_heavy_weight if total_heavy_weight > 0 else 1.0

    # Score: penalty per off-center zone proportional to its weight
    score = 100.0
    for hz in heavy_info:
        if not hz["is_central"]:
            penalty = (hz["weight_kg"] / total_heavy_weight) * 50.0
            score -= penalty
    score = max(0.0, score)

    # Enrich with keel knowledge for structural considerations
    if KEEL_DATABASE and total_heavy_weight > 500:  # Only for larger boats
        try:
            keel_types = KEEL_DATABASE.get("keel_types", {})
            long_keel = keel_types.get("long_keel", {})
            if long_keel:
                fd = long_keel.get("force_distribution_de", {})
                max_stress = fd.get("max_stress_location_de")
                if max_stress and central_ratio < 0.6:
                    warnings.append({
                        "code": "KEEL_BOLT_STRESS_RISK",
                        "severity": "warning",
                        "message": (
                            f"Mit {central_ratio:.0%} der Schwere außerhalb der zentralen Zone "
                            f"besteht erhöhtes Risiko für Kielbolt-Versagen "
                            f"(max. Spannungskonzentration am Übergang Kielgrat zu Rumpf)."
                        ),
                        "suggestion": (
                            f"Schwerverteilung prüfen; schwere Zonen nach innen verlagern um "
                            f"Biegemomente auf Kielbolzen zu minimieren."
                        ),
                    })
        except (KeyError, TypeError, AttributeError):
            pass

    return score, warnings, {
        "heavy_zones": heavy_info,
        "total_heavy_weight_kg": round(total_heavy_weight, 1),
        "central_ratio": round(central_ratio, 4),
    }


# ---------------------------------------------------------------------------
# Sub-analysis: Load concentration
# ---------------------------------------------------------------------------


def analyze_load_concentration(
    zones: list[dict],
    config: dict,
    *,
    structural_items: list[dict] | None = None,
) -> tuple[float, list[dict], dict]:
    """Evaluate weight distribution across three longitudinal segments.

    Measured items are binned into the segments as point masses (their zone's
    heuristic weight is reduced accordingly — no double counting).

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "code": "STRUCTURAL_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen für Lastkonzentrationsanalyse vorhanden.",
            "suggestion": "Zonen dem Layout zuweisen.",
        })
        return 50.0, warnings, {
            "segment_weights": {}, "segment_fractions": {},
            "heaviest_segment": None, "cv": 0.0,
        }

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    warn_threshold = config.get("concentration_warn_threshold", 0.55)
    min_x, max_x, _, _ = _get_boat_extents(zones)
    x_span = max_x - min_x

    if x_span < 1e-6:
        return 50.0, warnings, {
            "segment_weights": {}, "segment_fractions": {},
            "heaviest_segment": None, "cv": 0.0,
        }

    # Divide into 3 equal segments
    third = x_span / 3.0
    boundaries = [min_x, min_x + third, min_x + 2 * third, max_x]
    segment_weights: dict[str, float] = {"bow": 0.0, "middle": 0.0, "stern": 0.0}

    zone_entries, masses, _ = _build_weight_model(zones, weight_factor, structural_items)

    def _bin_weight(x: float, weight: float) -> None:
        if x < boundaries[1]:
            segment_weights["bow"] += weight
        elif x < boundaries[2]:
            segment_weights["middle"] += weight
        else:
            segment_weights["stern"] += weight

    for entry in zone_entries:
        _bin_weight(entry["cx"], entry["weight"])

    for mass in masses:
        # Clamp outside items into the boat frame for binning (anchor locker
        # ahead of the zones belongs to the bow segment)
        _bin_weight(min(max(mass["x_mm"], min_x), max_x), mass["weight_kg"])

    total = sum(segment_weights.values())
    if total < 1e-6:
        return 50.0, warnings, {
            "segment_weights": segment_weights, "segment_fractions": {},
            "heaviest_segment": None, "cv": 0.0,
        }

    fractions = {k: v / total for k, v in segment_weights.items()}

    # Coefficient of variation
    mean_w = total / 3.0
    variance = sum((v - mean_w) ** 2 for v in segment_weights.values()) / 3.0
    std_dev = variance ** 0.5
    cv = std_dev / mean_w if mean_w > 0 else 0.0

    score = max(0.0, 100.0 * (1.0 - cv))

    heaviest = max(fractions, key=fractions.get)

    # Warnings
    for name, frac in fractions.items():
        if frac > 0.70:
            warnings.append({
                "code": "LOAD_CONCENTRATION_HIGH",
                "severity": "critical",
                "message": (
                    f"Segment '{name}' trägt {frac:.0%} des Gesamtgewichts — "
                    f"stark ungleichmäßige Verteilung."
                ),
                "suggestion": f"Gewicht aus Segment '{name}' umverteilen.",
            })
        elif frac > warn_threshold:
            warnings.append({
                "code": "LOAD_CONCENTRATION_HIGH",
                "severity": "warning",
                "message": (
                    f"Segment '{name}' trägt {frac:.0%} des Gesamtgewichts — "
                    f"Richtwert: max. {warn_threshold:.0%}."
                ),
                "suggestion": f"Gewicht aus Segment '{name}' gleichmäßiger verteilen.",
            })

    return score, warnings, {
        "segment_weights": {k: round(v, 1) for k, v in segment_weights.items()},
        "segment_fractions": {k: round(v, 4) for k, v in fractions.items()},
        "heaviest_segment": heaviest,
        "cv": round(cv, 4),
    }


# ---------------------------------------------------------------------------
# Sub-analysis: Loading conditions
# ---------------------------------------------------------------------------

LOADING_CONDITIONS = {
    "light_ship": {"fuel_pct": 0, "water_pct": 0, "stores_pct": 0},
    "full_departure": {"fuel_pct": 100, "water_pct": 100, "stores_pct": 100},
    "arrival": {"fuel_pct": 10, "water_pct": 10, "stores_pct": 50},
    "worst_case": {"fuel_pct": 50, "water_pct": 30, "stores_pct": 30},
}


def analyze_loading_conditions(
    zones: list[dict],
    config: dict,
    *,
    structural_items: list[dict] | None = None,
) -> tuple[float, list[dict], dict]:
    """Compute CG position under different loading conditions.

    Measured items enter each condition as point masses; tank-typed items
    scale with the condition's fill level, all others are fixed mass.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "code": "STRUCTURAL_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen für Beladungszustandsanalyse vorhanden.",
            "suggestion": "Zonen dem Layout zuweisen.",
        })
        return 50.0, warnings, {"conditions": {}}

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    ideal_range = config.get("ideal_cog_x_range", (0.44, 0.54))
    # Fixed zone frame — see analyze_fore_aft_balance
    min_x, max_x, _, _ = _get_boat_extents(zones)
    x_span = max_x - min_x

    if x_span < 1e-6:
        return 50.0, warnings, {"conditions": {}}

    zone_entries, masses, _ = _build_weight_model(zones, weight_factor, structural_items)

    condition_results: dict[str, float] = {}
    in_range_count = 0

    for cond_name, cond in LOADING_CONDITIONS.items():
        fuel_pct = cond["fuel_pct"]
        water_pct = cond["water_pct"]
        stores_pct = cond["stores_pct"]

        total_weight = 0.0
        weighted_x = 0.0

        for entry in zone_entries:
            base_weight = entry["weight"]
            zone_type = entry["zone"].get("zone_type", "")

            if zone_type == "engine":
                adjusted_weight = base_weight * (fuel_pct / 100.0)
            elif zone_type == "storage":
                adjusted_weight = base_weight * (stores_pct / 100.0)
            elif zone_type in ("head", "pantry"):
                adjusted_weight = base_weight * (water_pct / 100.0)
            else:
                adjusted_weight = base_weight

            total_weight += adjusted_weight
            weighted_x += entry["cx"] * adjusted_weight

        for mass in masses:
            adjusted = _condition_adjusted_item_weight(mass, fuel_pct, water_pct)
            total_weight += adjusted
            weighted_x += mass["x_mm"] * adjusted

        if total_weight < 1e-6:
            condition_results[cond_name] = 0.5
            continue

        cog_x = weighted_x / total_weight
        cog_x_pct = _clamp01((cog_x - min_x) / x_span)
        condition_results[cond_name] = round(cog_x_pct, 4)

        if ideal_range[0] <= cog_x_pct <= ideal_range[1]:
            in_range_count += 1
        else:
            if cog_x_pct < ideal_range[0]:
                direction = "zu weit vorne"
            else:
                direction = "zu weit achtern"
            warnings.append({
                "code": "LOADING_COG_OUT_OF_RANGE",
                "severity": "warning",
                "message": (
                    f"Beladungszustand '{cond_name}': Schwerpunkt bei "
                    f"{cog_x_pct:.0%} — {direction} "
                    f"(Ideal: {ideal_range[0]:.0%}–{ideal_range[1]:.0%})."
                ),
                "suggestion": (
                    f"Gewichtsverteilung für Beladungszustand '{cond_name}' optimieren."
                ),
            })

    total_conditions = len(LOADING_CONDITIONS)
    score = (in_range_count / total_conditions) * 100.0 if total_conditions > 0 else 50.0

    return score, warnings, {"conditions": condition_results}


# ---------------------------------------------------------------------------
# Sub-analysis: Trim
# ---------------------------------------------------------------------------


def analyze_trim(
    zones: list[dict],
    config: dict,
    *,
    structural_items: list[dict] | None = None,
) -> tuple[float, list[dict], dict]:
    """Estimate longitudinal trim angle from weight distribution.

    Measured items enter the trim CG as point masses.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "code": "STRUCTURAL_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen für Trimmanalyse vorhanden.",
            "suggestion": "Zonen dem Layout zuweisen.",
        })
        return 50.0, warnings, {"trim_deg": 0.0, "cog_x_pct": 0.0, "ideal_midpoint_pct": 0.0}

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    ideal_range = config.get("ideal_cog_x_range", (0.44, 0.54))
    max_trim_deg = config.get("max_trim_deg", 2.0)
    # Fixed zone frame — see analyze_fore_aft_balance
    min_x, max_x, _, _ = _get_boat_extents(zones)
    x_span = max_x - min_x

    if x_span < 1e-6:
        return 50.0, warnings, {"trim_deg": 0.0, "cog_x_pct": 0.5, "ideal_midpoint_pct": 0.5}

    zone_entries, masses, _ = _build_weight_model(zones, weight_factor, structural_items)

    total_weight = 0.0
    weighted_x = 0.0

    for entry in zone_entries:
        total_weight += entry["weight"]
        weighted_x += entry["cx"] * entry["weight"]

    for mass in masses:
        total_weight += mass["weight_kg"]
        weighted_x += mass["x_mm"] * mass["weight_kg"]

    if total_weight < 1e-6:
        return 50.0, warnings, {"trim_deg": 0.0, "cog_x_pct": 0.5, "ideal_midpoint_pct": 0.5}

    cog_x = weighted_x / total_weight
    cog_x_pct = _clamp01((cog_x - min_x) / x_span)

    # Ideal midpoint in mm
    ideal_midpoint_pct = (ideal_range[0] + ideal_range[1]) / 2.0
    ideal_midpoint_x = min_x + x_span * ideal_midpoint_pct
    trim_offset_mm = cog_x - ideal_midpoint_x
    boat_length_mm = x_span

    correction_factor = 2.0
    trim_deg = math.degrees(math.atan2(trim_offset_mm, boat_length_mm)) * correction_factor

    # Score
    abs_trim = abs(trim_deg)
    if abs_trim <= max_trim_deg:
        score = 100.0
    elif abs_trim >= max_trim_deg * 2.0:
        score = 0.0
    else:
        score = 100.0 * (1.0 - (abs_trim - max_trim_deg) / max_trim_deg)

    if abs_trim > max_trim_deg:
        direction = "buglastig" if trim_deg > 0 else "hecklastig"
        warnings.append({
            "code": "TRIM_EXCESSIVE",
            "severity": "warning",
            "message": (
                f"Geschätzter Trimm {abs_trim:.1f}° ({direction}) — "
                f"Maximalwert: {max_trim_deg:.1f}°."
            ),
            "suggestion": "Gewichtsverteilung anpassen, um den Trimm zu reduzieren.",
        })

    return score, warnings, {
        "trim_deg": round(trim_deg, 2),
        "cog_x_pct": round(cog_x_pct, 4),
        "ideal_midpoint_pct": round(ideal_midpoint_pct, 4),
    }


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


def run_structural_analysis(
    zones: list[dict],
    passages: list[dict],
    boat_class: str,
    config_overrides: dict | None = None,
    data_source: str = "measured",
    structural_items: list[dict] | None = None,
) -> dict:
    """Orchestrator — runs all structural (weight distribution) sub-analyses.

    Args:
        zones: Layout zones with polygon, zone_type, name.
        passages: Unused — accepted for API pattern consistency.
        boat_class: One of the 13 BoatClass values.
        config_overrides: Optional dict to override config values.
        structural_items: Measured items (weight_kg, position_*_mm) — enter
            the CG/trim/loading models as point masses. Previously these were
            collected via the API but silently ignored by the analysis.

    Returns a standardized result dict matching the AYDI analysis module contract.
    """
    if boat_class not in BOAT_CLASS_DEFAULTS:
        return {"available": False, "reason": f"Unbekannte Bootsklasse: {boat_class}"}

    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    weights = config.pop("weights").copy()

    if config_overrides:
        config.update(config_overrides)

    # Short-circuit: no zones → structural analysis is not possible. Report as
    # unavailable rather than fabricating a 50/100 score for absent data.
    if not zones:
        return {
            "module": "structural",
            "available": False,
            "reason": "Keine Zonen für Strukturanalyse vorhanden.",
            "suggestions": ["Zonen dem Layout zuweisen."],
        }

    sub_scores: dict[str, float] = {}
    all_warnings: list[dict] = []
    all_suggestions: list[str] = []
    all_metrics: dict[str, dict] = {}

    analyses = [
        ("fore_aft", lambda: analyze_fore_aft_balance(
            zones, config, structural_items=structural_items)),
        ("lateral", lambda: analyze_lateral_balance(
            zones, config, structural_items=structural_items)),
        ("heavy_placement", lambda: analyze_heavy_zone_placement(
            zones, config, structural_items=structural_items)),
        ("load_concentration", lambda: analyze_load_concentration(
            zones, config, structural_items=structural_items)),
        ("loading_conditions", lambda: analyze_loading_conditions(
            zones, config, structural_items=structural_items)),
        ("trim", lambda: analyze_trim(
            zones, config, structural_items=structural_items)),
    ]

    for name, fn in analyses:
        try:
            score, warnings, metrics = fn()
            sub_scores[name] = score
            all_warnings.extend(warnings)
            all_metrics[name] = metrics
        except Exception:
            logger.exception("Error in structural sub-analysis %s", name)
            sub_scores[name] = 0.0
            all_warnings.append({
                "code": "STRUCTURAL_ANALYSIS_ERROR",
                "severity": "critical",
                "message": f"Fehler bei Strukturanalyse: {name}",
                "suggestion": "Layoutdaten überprüfen.",
            })

    overall = sum(sub_scores.get(k, 50.0) * w for k, w in weights.items())

    # Honest provenance for measured items: report what entered the model,
    # what was deducted from zone heuristics (double-count prevention), what
    # lies outside the evaluation frame, and what was skipped.
    if structural_items:
        weight_factor = config.get("boat_class_weight_factor", 1.0)
        zone_entries, masses, outside = _build_weight_model(
            zones, weight_factor, structural_items
        )
        measured_weight = sum(m["weight_kg"] for m in masses)
        effective_heuristic = sum(e["weight"] for e in zone_entries)
        raw_heuristic = sum(_estimate_zone_weight(z, weight_factor) for z in zones)
        deducted = raw_heuristic - effective_heuristic
        model_weight = measured_weight + effective_heuristic
        skipped = len(structural_items) - len(masses)
        all_metrics["measured_items"] = {
            "count": len(masses),
            "total_weight_kg": round(measured_weight, 1),
            "share_of_model_weight_pct": (
                round(measured_weight / model_weight * 100.0, 1)
                if model_weight > 1e-6
                else 0.0
            ),
            "deducted_from_zone_heuristics_kg": round(deducted, 1),
            "outside_zone_extents": [m["name"] for m in outside],
            "skipped_without_position_or_weight": skipped,
        }
        if masses:
            all_warnings.append({
                "code": "STRUCTURAL_MEASURED_ITEMS_USED",
                "severity": "info",
                "message": (
                    f"{len(masses)} gemessene Strukturelemente "
                    f"({measured_weight:.0f} kg) fließen in alle Gewichts-Teilanalysen "
                    f"ein; zugeordnete Zonenheuristik wurde um {deducted:.0f} kg "
                    "entlastet (keine Doppelzählung). Übrige Gewichte bleiben "
                    "heuristisch aus Zonenflächen geschätzt."
                ),
                "suggestion": None,
            })
        if outside:
            names = ", ".join(m["name"] for m in outside)
            all_warnings.append({
                "code": "STRUCTURAL_ITEM_OUTSIDE_EXTENTS",
                "severity": "info",
                "message": (
                    f"Element(e) außerhalb der Zonen-Ausdehnung: {names} — "
                    "zulässig (z.B. Ankerkasten), Bewertungsrahmen bleibt die "
                    "Zonen-Bounding-Box; Positionsreferenz bitte prüfen."
                ),
                "suggestion": None,
            })
        unknown_tanks = [
            m for m in masses
            if "tank" in m["item_type"]
            and m["item_type"] not in (_FUEL_TANK_TYPES | _WATER_TANK_TYPES)
        ]
        if unknown_tanks:
            names = ", ".join(m["name"] for m in unknown_tanks)
            all_warnings.append({
                "code": "STRUCTURAL_TANK_TYPE_UNKNOWN",
                "severity": "info",
                "message": (
                    f"Tanktyp nicht zuordenbar ({names}) — als Festmasse "
                    "gerechnet. Für Beladungszustände item_type 'fuel_tank' "
                    "oder 'water_tank' verwenden."
                ),
                "suggestion": None,
            })
        if skipped > 0:
            all_warnings.append({
                "code": "STRUCTURAL_ITEMS_SKIPPED",
                "severity": "warning",
                "message": (
                    f"{skipped} Strukturelement(e) ohne positives Gewicht oder "
                    "X-Position wurden NICHT berücksichtigt."
                ),
                "suggestion": (
                    "Gewicht (> 0 kg) und Längsposition (X) der Strukturelemente "
                    "erfassen, damit sie in die Analyse eingehen."
                ),
            })

    for w in all_warnings:
        suggestion = w.get("suggestion")
        if suggestion and suggestion not in all_suggestions:
            all_suggestions.append(suggestion)

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    # =========================================================================
    # MARKDOWN KNOWLEDGE ENRICHMENT — structural data from composites/fasteners
    # =========================================================================

    knowledge_enrichment = {}
    if _MD_AVAILABLE:
        try:
            md_knowledge = _get_md_structural_knowledge(
                hull_material="grp",
                hull_construction=None,
                core_material=None,
            )
            knowledge_enrichment["markdown_fastener_data"] = md_knowledge.get("markdown_fastener_data", [])
            knowledge_enrichment["markdown_composite_data"] = md_knowledge.get("markdown_composite_data", [])

            # Add structural fehlerbilder as info warnings
            for fd in md_knowledge.get("markdown_fastener_data", [])[:5]:
                for fb in fd.get("fehlerbilder", [])[:1]:
                    all_warnings.append({
                        "code": "MD_STRUCTURAL_FEHLERBILD",
                        "severity": "info",
                        "message": (
                            f"[Wissensdatenbank: {fd.get('title', '')}] "
                            f"{fb.get('title', '')}: {fb.get('symptom', '')[:120]}"
                        ),
                        "suggestion": fb.get("massnahme", "")[:120] if fb.get("massnahme") else None,
                        "source": f"markdown:{fd.get('slug', '')}",
                    })
        except Exception:
            logger.exception("Error enriching structural with markdown knowledge")

    return {
        "module": "structural",
        "overall_score": round(overall, 1),
        "sub_scores": {k: round(v, 1) for k, v in sub_scores.items()},
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
        "confidence": data_source,
        "confidence_note": "Basiert auf geschätzten Werten aus öffentlichen Spezifikationen." if data_source == "estimated" else None,
        "knowledge_enrichment": knowledge_enrichment if knowledge_enrichment else None,
    }
