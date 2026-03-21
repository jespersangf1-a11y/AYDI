"""Emotional design score module for yacht layouts.

Quantifies spatial experience: proportions, light, sightlines, visual calm,
ceiling perception, and inside-outside flow. Pure function module — no database access.
"""
import logging
import math

logger = logging.getLogger(__name__)

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "ideal_proportion_range": (0.70, 0.85),
        "ideal_salon_proportion": (0.55, 0.65),
        "target_window_ratio_salon": 0.30,
        "target_window_ratio_cabin": 0.18,
        "target_window_ratio_pantry": 0.12,
        "min_sightline_m": 1.5,
        "ideal_material_range": (3, 5),
        "min_ceiling_mm": 1750,
        "standard_ceiling_mm": 1850,
        "min_cockpit_passage_mm": 600,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.18,
            "light_distribution": 0.14,
            "sightline": 0.09,
            "visual_calm": 0.09,
            "ceiling_perception": 0.26,
            "inside_outside_flow": 0.14,
            "sightline_rays": 0.10,
        },
    },
    "cruising_sail": {
        "ideal_proportion_range": (0.70, 0.85),
        "ideal_salon_proportion": (0.55, 0.65),
        "target_window_ratio_salon": 0.32,
        "target_window_ratio_cabin": 0.20,
        "target_window_ratio_pantry": 0.15,
        "min_sightline_m": 1.8,
        "ideal_material_range": (3, 5),
        "min_ceiling_mm": 1850,
        "standard_ceiling_mm": 1950,
        "min_cockpit_passage_mm": 650,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.18,
            "light_distribution": 0.14,
            "sightline": 0.14,
            "visual_calm": 0.09,
            "ceiling_perception": 0.22,
            "inside_outside_flow": 0.13,
            "sightline_rays": 0.10,
        },
    },
    "large_motor": {
        "ideal_proportion_range": (0.65, 0.80),
        "ideal_salon_proportion": (0.50, 0.62),
        "target_window_ratio_salon": 0.35,
        "target_window_ratio_cabin": 0.22,
        "target_window_ratio_pantry": 0.15,
        "min_sightline_m": 2.0,
        "ideal_material_range": (3, 6),
        "min_ceiling_mm": 1950,
        "standard_ceiling_mm": 2050,
        "min_cockpit_passage_mm": 700,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.14,
            "light_distribution": 0.18,
            "sightline": 0.18,
            "visual_calm": 0.13,
            "ceiling_perception": 0.13,
            "inside_outside_flow": 0.14,
            "sightline_rays": 0.10,
        },
    },
    "racing_sail": {
        "ideal_proportion_range": (0.70, 0.90),
        "ideal_salon_proportion": (0.55, 0.70),
        "target_window_ratio_salon": 0.25,
        "target_window_ratio_cabin": 0.15,
        "target_window_ratio_pantry": 0.10,
        "min_sightline_m": 1.3,
        "ideal_material_range": (2, 4),
        "min_ceiling_mm": 1700,
        "standard_ceiling_mm": 1800,
        "min_cockpit_passage_mm": 550,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.2444,
            "light_distribution": 0.1111,
            "sightline": 0.0556,
            "visual_calm": 0.0667,
            "ceiling_perception": 0.3000,
            "inside_outside_flow": 0.1111,
            "sightline_rays": 0.1111,
        },
    },
    "daysailer": {
        "ideal_proportion_range": (0.70, 0.85),
        "ideal_salon_proportion": (0.55, 0.68),
        "target_window_ratio_salon": 0.28,
        "target_window_ratio_cabin": 0.17,
        "target_window_ratio_pantry": 0.12,
        "min_sightline_m": 1.5,
        "ideal_material_range": (3, 5),
        "min_ceiling_mm": 1700,
        "standard_ceiling_mm": 1800,
        "min_cockpit_passage_mm": 600,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.18,
            "light_distribution": 0.14,
            "sightline": 0.09,
            "visual_calm": 0.09,
            "ceiling_perception": 0.26,
            "inside_outside_flow": 0.14,
            "sightline_rays": 0.10,
        },
    },
    "motorsailer": {
        "ideal_proportion_range": (0.68, 0.82),
        "ideal_salon_proportion": (0.50, 0.62),
        "target_window_ratio_salon": 0.34,
        "target_window_ratio_cabin": 0.21,
        "target_window_ratio_pantry": 0.15,
        "min_sightline_m": 1.9,
        "ideal_material_range": (3, 5),
        "min_ceiling_mm": 1900,
        "standard_ceiling_mm": 2000,
        "min_cockpit_passage_mm": 700,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.1633,
            "light_distribution": 0.1633,
            "sightline": 0.1633,
            "visual_calm": 0.1122,
            "ceiling_perception": 0.1531,
            "inside_outside_flow": 0.1429,
            "sightline_rays": 0.1020,
        },
    },
    "catamaran_sail": {
        "ideal_proportion_range": (0.68, 0.82),
        "ideal_salon_proportion": (0.52, 0.64),
        "target_window_ratio_salon": 0.33,
        "target_window_ratio_cabin": 0.20,
        "target_window_ratio_pantry": 0.14,
        "min_sightline_m": 1.8,
        "ideal_material_range": (3, 5),
        "min_ceiling_mm": 1850,
        "standard_ceiling_mm": 1950,
        "min_cockpit_passage_mm": 650,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.1753,
            "light_distribution": 0.1546,
            "sightline": 0.1237,
            "visual_calm": 0.0928,
            "ceiling_perception": 0.2062,
            "inside_outside_flow": 0.1443,
            "sightline_rays": 0.1031,
        },
    },
    "catamaran_motor": {
        "ideal_proportion_range": (0.65, 0.80),
        "ideal_salon_proportion": (0.50, 0.62),
        "target_window_ratio_salon": 0.35,
        "target_window_ratio_cabin": 0.22,
        "target_window_ratio_pantry": 0.15,
        "min_sightline_m": 2.0,
        "ideal_material_range": (3, 6),
        "min_ceiling_mm": 1900,
        "standard_ceiling_mm": 2000,
        "min_cockpit_passage_mm": 700,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.14,
            "light_distribution": 0.18,
            "sightline": 0.18,
            "visual_calm": 0.13,
            "ceiling_perception": 0.13,
            "inside_outside_flow": 0.14,
            "sightline_rays": 0.10,
        },
    },
    "small_motor": {
        "ideal_proportion_range": (0.65, 0.80),
        "ideal_salon_proportion": (0.50, 0.62),
        "target_window_ratio_salon": 0.34,
        "target_window_ratio_cabin": 0.21,
        "target_window_ratio_pantry": 0.15,
        "min_sightline_m": 1.9,
        "ideal_material_range": (3, 5),
        "min_ceiling_mm": 1850,
        "standard_ceiling_mm": 1950,
        "min_cockpit_passage_mm": 650,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.1515,
            "light_distribution": 0.1717,
            "sightline": 0.1616,
            "visual_calm": 0.1212,
            "ceiling_perception": 0.1515,
            "inside_outside_flow": 0.1414,
            "sightline_rays": 0.1010,
        },
    },
    "sport_cruiser": {
        "ideal_proportion_range": (0.63, 0.78),
        "ideal_salon_proportion": (0.48, 0.60),
        "target_window_ratio_salon": 0.36,
        "target_window_ratio_cabin": 0.24,
        "target_window_ratio_pantry": 0.16,
        "min_sightline_m": 2.1,
        "ideal_material_range": (3, 6),
        "min_ceiling_mm": 1850,
        "standard_ceiling_mm": 1950,
        "min_cockpit_passage_mm": 750,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.13,
            "light_distribution": 0.18,
            "sightline": 0.20,
            "visual_calm": 0.14,
            "ceiling_perception": 0.11,
            "inside_outside_flow": 0.14,
            "sightline_rays": 0.10,
        },
    },
    "trawler": {
        "ideal_proportion_range": (0.62, 0.77),
        "ideal_salon_proportion": (0.48, 0.60),
        "target_window_ratio_salon": 0.33,
        "target_window_ratio_cabin": 0.21,
        "target_window_ratio_pantry": 0.14,
        "min_sightline_m": 2.0,
        "ideal_material_range": (3, 6),
        "min_ceiling_mm": 1900,
        "standard_ceiling_mm": 2000,
        "min_cockpit_passage_mm": 750,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.1354,
            "light_distribution": 0.1771,
            "sightline": 0.1771,
            "visual_calm": 0.1354,
            "ceiling_perception": 0.1250,
            "inside_outside_flow": 0.1458,
            "sightline_rays": 0.1042,
        },
    },
    "explorer": {
        "ideal_proportion_range": (0.60, 0.75),
        "ideal_salon_proportion": (0.46, 0.58),
        "target_window_ratio_salon": 0.37,
        "target_window_ratio_cabin": 0.25,
        "target_window_ratio_pantry": 0.17,
        "min_sightline_m": 2.3,
        "ideal_material_range": (4, 6),
        "min_ceiling_mm": 1950,
        "standard_ceiling_mm": 2050,
        "min_cockpit_passage_mm": 800,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.10,
            "light_distribution": 0.18,
            "sightline": 0.22,
            "visual_calm": 0.17,
            "ceiling_perception": 0.10,
            "inside_outside_flow": 0.13,
            "sightline_rays": 0.10,
        },
    },
    "superyacht": {
        "ideal_proportion_range": (0.60, 0.75),
        "ideal_salon_proportion": (0.45, 0.58),
        "target_window_ratio_salon": 0.38,
        "target_window_ratio_cabin": 0.25,
        "target_window_ratio_pantry": 0.18,
        "min_sightline_m": 2.5,
        "ideal_material_range": (4, 6),
        "min_ceiling_mm": 2050,
        "standard_ceiling_mm": 2150,
        "min_cockpit_passage_mm": 850,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.09,
            "light_distribution": 0.18,
            "sightline": 0.23,
            "visual_calm": 0.18,
            "ceiling_perception": 0.09,
            "inside_outside_flow": 0.13,
            "sightline_rays": 0.10,
        },
    },
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}


def _polygon_area_sqm(polygon: list[list[float]]) -> float:
    """Shoelace formula, returns area in square meters (input in mm)."""
    n = len(polygon)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2.0 / 1_000_000


def _polygon_bbox_dims_mm(polygon: list[list[float]]) -> tuple[float, float]:
    """Return (width_mm, depth_mm) of polygon bounding box."""
    if not polygon:
        return (0.0, 0.0)
    xs = [p[0] for p in polygon]
    ys = [p[1] for p in polygon]
    return (max(xs) - min(xs), max(ys) - min(ys))


def _max_interior_distance_m(polygon: list[list[float]]) -> float:
    """Maximum distance between any two vertices, in meters."""
    if len(polygon) < 2:
        return 0.0
    max_dist = 0.0
    for i in range(len(polygon)):
        for j in range(i + 1, len(polygon)):
            dx = polygon[i][0] - polygon[j][0]
            dy = polygon[i][1] - polygon[j][1]
            d = math.sqrt(dx * dx + dy * dy) / 1000.0
            if d > max_dist:
                max_dist = d
    return max_dist


_PROPORTION_ZONE_TYPES = {"salon", "cabin", "pantry", "helm", "crew_quarters"}


def analyze_room_proportion(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score ceiling height / room width ratio for living spaces."""
    warnings: list[dict] = []

    evaluable = [z for z in zones if z["zone_type"] in _PROPORTION_ZONE_TYPES and z.get("height_mm") is not None]
    if not evaluable:
        warnings.append({
            "severity": "info",
            "message": "Keine Höhendaten vorhanden — Raumproportionen nicht bewertbar",
            "suggestion": "height_mm für Zonen angeben",
        })
        return 50.0, warnings, {"zones_evaluated": 0}

    ideal_salon = config["ideal_salon_proportion"]
    ideal_other = config["ideal_proportion_range"]
    zone_scores = []

    for z in evaluable:
        width, depth = _polygon_bbox_dims_mm(z["polygon"])
        shorter_dim = min(width, depth) if min(width, depth) > 0 else max(width, depth)
        if shorter_dim == 0:
            continue

        ratio = z["height_mm"] / shorter_dim
        ideal = ideal_salon if z["zone_type"] == "salon" else ideal_other
        lo, hi = ideal

        if lo <= ratio <= hi:
            zone_scores.append(100.0)
        else:
            if ratio < lo:
                deviation = (lo - ratio) / lo
            else:
                deviation = (ratio - hi) / hi
            zone_score = max(0.0, 100.0 - deviation * 150.0)
            zone_scores.append(zone_score)

            if deviation > 0.15:
                label = z["name"]
                warnings.append({
                    "severity": "warning",
                    "message": f"Raumproportionen in '{label}' ungünstig (Verhältnis: {ratio:.2f}, Ideal: {lo:.2f}–{hi:.2f})",
                    "suggestion": f"Deckenhöhe oder Raumbreite in '{label}' anpassen",
                })

    if not zone_scores:
        return 50.0, warnings, {"zones_evaluated": 0}

    score = sum(zone_scores) / len(zone_scores)
    return score, warnings, {"zones_evaluated": len(zone_scores)}


_WINDOW_TARGET_KEYS = {
    "salon": "target_window_ratio_salon",
    "cabin": "target_window_ratio_cabin",
    "pantry": "target_window_ratio_pantry",
}


def analyze_light_distribution(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score natural light based on window_area_pct per zone."""
    warnings: list[dict] = []

    evaluable = []
    for z in zones:
        if z["zone_type"] not in _WINDOW_TARGET_KEYS:
            continue
        props = z.get("properties") or {}
        if "window_area_pct" in props:
            evaluable.append(z)

    if not evaluable:
        warnings.append({
            "severity": "info",
            "message": "Keine Fensterdaten vorhanden — Lichtverteilung nicht bewertbar",
            "suggestion": "window_area_pct in Zone-Eigenschaften angeben (0.0–1.0)",
        })
        return 50.0, warnings, {"zones_evaluated": 0}

    zone_scores = []
    for z in evaluable:
        pct = z["properties"]["window_area_pct"]
        target_key = _WINDOW_TARGET_KEYS[z["zone_type"]]
        target = config[target_key]

        if pct >= target:
            zone_scores.append(100.0)
        else:
            ratio = pct / target if target > 0 else 0.0
            zone_scores.append(ratio * 100.0)
            if ratio < 0.6:
                warnings.append({
                    "severity": "warning",
                    "message": f"Zone '{z['name']}' zu dunkel (Fensteranteil: {pct:.0%}, Ziel: {target:.0%})",
                    "suggestion": f"Fensterfläche in '{z['name']}' vergrößern",
                })

    score = sum(zone_scores) / len(zone_scores)
    return score, warnings, {"zones_evaluated": len(zone_scores)}


_SIGHTLINE_ZONE_TYPES = {"salon", "cabin", "pantry", "helm", "cockpit"}


def analyze_sightline(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score maximum interior sightline distance per zone.

    Simplification: uses max vertex-to-vertex distance as proxy for ray-trace.
    """
    warnings: list[dict] = []
    min_sight = config["min_sightline_m"]

    evaluable = [z for z in zones if z["zone_type"] in _SIGHTLINE_ZONE_TYPES]
    if not evaluable:
        warnings.append({
            "severity": "info",
            "message": "Keine bewertbaren Zonen für Sichtachsen vorhanden",
            "suggestion": "Salon- oder Kabinen-Zonen zum Layout hinzufügen",
        })
        return 50.0, warnings, {"avg_sightline_m": 0.0, "zones_evaluated": 0}

    zone_scores = []
    sightlines = []

    for z in evaluable:
        dist = _max_interior_distance_m(z["polygon"])
        sightlines.append(dist)

        if dist >= min_sight * 1.5:
            zone_scores.append(100.0)
        elif dist >= min_sight:
            ratio = (dist - min_sight) / (min_sight * 0.5)
            zone_scores.append(70.0 + ratio * 30.0)
        else:
            ratio = dist / min_sight if min_sight > 0 else 0.0
            zone_scores.append(ratio * 70.0)
            warnings.append({
                "severity": "warning",
                "message": f"Sichtachse in '{z['name']}' kurz ({dist:.1f}m, empfohlen: {min_sight:.1f}m)",
                "suggestion": f"Raumgeometrie in '{z['name']}' öffnen für längere Sichtachsen",
            })

    avg_sight = sum(sightlines) / len(sightlines) if sightlines else 0.0
    score = sum(zone_scores) / len(zone_scores)
    return score, warnings, {"avg_sightline_m": round(avg_sight, 2), "zones_evaluated": len(zone_scores)}


def analyze_visual_calm(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score visual complexity based on material_count per zone."""
    warnings: list[dict] = []
    ideal_lo, ideal_hi = config["ideal_material_range"]

    evaluable = []
    for z in zones:
        props = z.get("properties") or {}
        if "material_count" in props:
            evaluable.append(z)

    if not evaluable:
        warnings.append({
            "severity": "info",
            "message": "Keine Materialdaten vorhanden — visuelle Ruhe nicht bewertbar",
            "suggestion": "material_count in Zone-Eigenschaften angeben",
        })
        return 50.0, warnings, {"zones_evaluated": 0}

    zone_scores = []
    for z in evaluable:
        count = z["properties"]["material_count"]
        if ideal_lo <= count <= ideal_hi:
            zone_scores.append(100.0)
        elif count < ideal_lo:
            zone_scores.append(max(0.0, count / ideal_lo * 70.0))
            warnings.append({
                "severity": "info",
                "message": f"Zone '{z['name']}' wirkt steril ({count} Materialien, empfohlen: {ideal_lo}–{ideal_hi})",
                "suggestion": f"Materialvielfalt in '{z['name']}' erhöhen",
            })
        else:
            excess = count - ideal_hi
            zone_scores.append(max(0.0, 100.0 - excess * 15.0))
            warnings.append({
                "severity": "warning",
                "message": f"Zone '{z['name']}' wirkt unruhig ({count} Materialien, empfohlen: {ideal_lo}–{ideal_hi})",
                "suggestion": f"Materialvielfalt in '{z['name']}' reduzieren",
            })

    score = sum(zone_scores) / len(zone_scores)
    return score, warnings, {"zones_evaluated": len(zone_scores)}


def analyze_ceiling_perception(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score ceiling height perception relative to boat class standards."""
    warnings: list[dict] = []
    min_h = config["min_ceiling_mm"]
    std_h = config["standard_ceiling_mm"]

    evaluable = [z for z in zones if z.get("height_mm") is not None]
    if not evaluable:
        warnings.append({
            "severity": "info",
            "message": "Keine Deckenhöhendaten vorhanden — Raumhöheneindruck nicht bewertbar",
            "suggestion": "height_mm für Zonen angeben",
        })
        return 50.0, warnings, {"zones_evaluated": 0, "avg_height_mm": 0}

    zone_scores = []
    heights = []
    for z in evaluable:
        h = z["height_mm"]
        heights.append(h)

        if h >= std_h:
            zone_scores.append(100.0)
        elif h >= min_h:
            ratio = (h - min_h) / (std_h - min_h) if std_h > min_h else 1.0
            zone_scores.append(60.0 + ratio * 40.0)
        else:
            ratio = h / min_h if min_h > 0 else 0.0
            zone_scores.append(ratio * 60.0)
            warnings.append({
                "severity": "warning",
                "message": f"Deckenhöhe in '{z['name']}' zu niedrig ({h:.0f}mm, Minimum: {min_h:.0f}mm)",
                "suggestion": f"Deckenhöhe in '{z['name']}' auf mindestens {min_h:.0f}mm erhöhen",
            })

    avg_h = sum(heights) / len(heights)
    score = sum(zone_scores) / len(zone_scores)
    return score, warnings, {"zones_evaluated": len(zone_scores), "avg_height_mm": round(avg_h, 0)}


def analyze_inside_outside_flow(zones: list[dict], passages: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score transition quality between interior zones and cockpit."""
    warnings: list[dict] = []
    min_width = config["min_cockpit_passage_mm"]

    cockpit_zones = {z["name"] for z in zones if z["zone_type"] == "cockpit"}
    if not cockpit_zones:
        warnings.append({
            "severity": "warning",
            "message": "Kein Cockpit im Layout — Innen-Außen-Übergang nicht bewertbar",
            "suggestion": "Cockpit-Zone zum Layout hinzufügen",
        })
        return 30.0, warnings, {"cockpit_passages": 0, "max_passage_width_mm": 0}

    cockpit_passages = []
    for p in passages:
        if p["from_zone"] in cockpit_zones or p["to_zone"] in cockpit_zones:
            cockpit_passages.append(p)

    if not cockpit_passages:
        warnings.append({
            "severity": "warning",
            "message": "Kein Durchgang zum Cockpit vorhanden",
            "suggestion": "Durchgang zwischen Innenraum und Cockpit hinzufügen",
        })
        return 20.0, warnings, {"cockpit_passages": 0, "max_passage_width_mm": 0}

    max_width = max(p["width_mm"] for p in cockpit_passages)
    widths = [p["width_mm"] for p in cockpit_passages]

    passage_scores = []
    for w in widths:
        if w >= min_width * 1.3:
            passage_scores.append(100.0)
        elif w >= min_width:
            ratio = (w - min_width) / (min_width * 0.3)
            passage_scores.append(70.0 + ratio * 30.0)
        else:
            ratio = w / min_width if min_width > 0 else 0.0
            passage_scores.append(ratio * 70.0)
            warnings.append({
                "severity": "warning",
                "message": f"Cockpit-Durchgang zu schmal ({w:.0f}mm, empfohlen: {min_width:.0f}mm)",
                "suggestion": f"Cockpit-Durchgang auf mindestens {min_width:.0f}mm erweitern",
            })

    score = sum(passage_scores) / len(passage_scores)
    return score, warnings, {
        "cockpit_passages": len(cockpit_passages),
        "max_passage_width_mm": max_width,
    }


def _polygon_centroid(polygon: list[list[float]]) -> tuple[float, float]:
    """Compute centroid of a polygon (input in mm)."""
    n = len(polygon)
    if n == 0:
        return (0.0, 0.0)
    cx = sum(p[0] for p in polygon) / n
    cy = sum(p[1] for p in polygon) / n
    return (cx, cy)


def _ray_polygon_distance(origin: tuple[float, float], angle_rad: float, polygon: list[list[float]]) -> float:
    """Distance from origin to polygon boundary along ray direction."""
    dx = math.cos(angle_rad)
    dy = math.sin(angle_rad)
    min_dist = float('inf')
    n = len(polygon)
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        ex, ey = x2 - x1, y2 - y1
        denom = dx * ey - dy * ex
        if abs(denom) < 1e-10:
            continue
        t = ((x1 - origin[0]) * ey - (y1 - origin[1]) * ex) / denom
        u = ((x1 - origin[0]) * dy - (y1 - origin[1]) * dx) / denom
        if t > 1e-6 and 0 <= u <= 1:
            min_dist = min(min_dist, t)
    return min_dist if min_dist < float('inf') else 0.0


def analyze_sightline_rays(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """True 360-degree ray tracing from zone centroids for sightline analysis."""
    warnings: list[dict] = []
    min_sight = config["min_sightline_m"]
    num_rays = 72  # every 5 degrees

    evaluable = [z for z in zones if z["zone_type"] in _SIGHTLINE_ZONE_TYPES and z.get("polygon")]
    if not evaluable:
        warnings.append({
            "severity": "info",
            "message": "Keine bewertbaren Zonen für Sichtachsen-Raytracing vorhanden",
            "suggestion": "Salon- oder Kabinen-Zonen mit Polygondaten zum Layout hinzufügen",
        })
        return 50.0, warnings, {"zones_evaluated": 0, "avg_ray_length_m": 0.0}

    zone_scores = []
    all_avg_lengths = []

    for z in evaluable:
        polygon = z["polygon"]
        if len(polygon) < 3:
            continue

        centroid = _polygon_centroid(polygon)
        props = z.get("properties") or {}
        window_area_pct = props.get("window_area_pct", 0.0)

        # Determine target window ratio for this zone type
        target_key = _WINDOW_TARGET_KEYS.get(z["zone_type"])
        target_pct = config.get(target_key, 0.20) if target_key else 0.20

        # Cast rays
        ray_lengths = []
        for r in range(num_rays):
            angle = 2.0 * math.pi * r / num_rays
            dist_mm = _ray_polygon_distance(centroid, angle, polygon)
            ray_lengths.append(dist_mm / 1000.0)  # convert to meters

        avg_ray_length = sum(ray_lengths) / len(ray_lengths) if ray_lengths else 0.0
        all_avg_lengths.append(avg_ray_length)

        # Score based on average ray length vs min_sightline_m
        if avg_ray_length >= min_sight:
            base_score = 100.0
        else:
            base_score = (avg_ray_length / min_sight * 100.0) if min_sight > 0 else 0.0

        # Openness bonus/penalty based on window_area_pct
        if window_area_pct > target_pct:
            base_score = min(100.0, base_score + 10.0)
        elif window_area_pct < target_pct * 0.5:
            base_score = max(0.0, base_score - 10.0)

        zone_scores.append(base_score)

        if base_score < 60.0:
            warnings.append({
                "severity": "warning",
                "message": (
                    f"Sichtachsen in '{z['name']}' eingeschränkt "
                    f"(Ø Strahllänge: {avg_ray_length:.1f}m, empfohlen: {min_sight:.1f}m)"
                ),
                "suggestion": f"Raumgeometrie in '{z['name']}' öffnen oder Fensterfläche vergrößern",
            })

    if not zone_scores:
        return 50.0, warnings, {"zones_evaluated": 0, "avg_ray_length_m": 0.0}

    overall_avg_length = sum(all_avg_lengths) / len(all_avg_lengths)
    score = sum(zone_scores) / len(zone_scores)

    return score, warnings, {
        "zones_evaluated": len(zone_scores),
        "avg_ray_length_m": round(overall_avg_length, 2),
        "num_rays": num_rays,
    }


def run_emotional_analysis(zones: list[dict], passages: list[dict], boat_class: str, config_overrides: dict | None = None, data_source: str = "measured") -> dict:
    """Orchestrator — runs all emotional design sub-analyses."""
    if boat_class not in BOAT_CLASS_DEFAULTS:
        raise ValueError(f"Unknown boat class: {boat_class}")
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    weights = config.pop("weights").copy()

    if config_overrides:
        config.update(config_overrides)

    sub_scores: dict[str, float] = {}
    all_warnings: list[dict] = []
    all_suggestions: list[str] = []
    all_metrics: dict[str, dict] = {}

    analyses = [
        ("room_proportion", lambda: analyze_room_proportion(zones, config)),
        ("light_distribution", lambda: analyze_light_distribution(zones, config)),
        ("sightline", lambda: analyze_sightline(zones, config)),
        ("visual_calm", lambda: analyze_visual_calm(zones, config)),
        ("ceiling_perception", lambda: analyze_ceiling_perception(zones, config)),
        ("inside_outside_flow", lambda: analyze_inside_outside_flow(zones, passages, config)),
        ("sightline_rays", lambda: analyze_sightline_rays(zones, config)),
    ]

    for name, fn in analyses:
        try:
            score, warnings, metrics = fn()
            sub_scores[name] = score
            all_warnings.extend(warnings)
            all_metrics[name] = metrics
        except Exception:
            logger.exception("Error in sub-analysis %s", name)
            sub_scores[name] = 0.0
            all_warnings.append({
                "severity": "critical",
                "message": f"Fehler bei Analyse: {name}",
                "suggestion": "Layoutdaten überprüfen",
            })

    overall = sum(sub_scores.get(k, 0) * w for k, w in weights.items())

    for w in all_warnings:
        if w.get("suggestion") and w["suggestion"] not in all_suggestions:
            all_suggestions.append(w["suggestion"])

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    return {
        "module": "emotional",
        "overall_score": round(overall, 1),
        "sub_scores": {k: round(v, 1) for k, v in sub_scores.items()},
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
        "confidence": data_source,
        "confidence_note": "Basiert auf geschätzten Werten aus öffentlichen Spezifikationen." if data_source == "estimated" else None,
    }
