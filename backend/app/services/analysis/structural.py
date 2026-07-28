"""Structural analysis module for yacht layouts (weight distribution).

Evaluates weight distribution and center of gravity placement using
heuristic weight estimation from zone types and polygon geometry.
Pure function module — no database access.
All user-facing strings are in German.
"""
import logging
import math
from app.core.zone_types import normalisiere_zonen, warnung_unbekannte_typen
from app.services.analysis.scoring import weighted_overall, hinweis_teilanalysen

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


# ---------------------------------------------------------------------------
# Sub-analysis: Longitudinal (fore-aft) balance
# ---------------------------------------------------------------------------


def analyze_fore_aft_balance(
    zones: list[dict],
    config: dict,
) -> tuple[float | None, list[dict], dict]:
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
        # Ohne Zonen gibt es keine Massenverteilung zu messen. Die frühere 50.0
        # las sich als Messwert "mittelmäßig", war aber gar keine Messung.
        return None, warnings, {"cog_x_pct": None, "ideal_range": None, "deviation_pct": None}

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    ideal_range = config.get("ideal_cog_x_range", (0.44, 0.54))
    min_x, max_x, _, _ = _get_boat_extents(zones)
    x_span = max_x - min_x

    if x_span < 1e-6:
        warnings.append({
            "code": "STRUCTURAL_NO_EXTENT",
            "severity": "warning",
            "message": (
                "Längsverteilung nicht beurteilbar: die Zonen des Layouts haben keine "
                "Längsausdehnung, auf die eine Position bezogen werden könnte."
            ),
            "suggestion": "Polygonkoordinaten der Zonen prüfen (alle x-Werte identisch).",
            "location": "layout.zones[].polygon",
        })
        return None, warnings, {
            "cog_x_pct": None, "ideal_range": list(ideal_range), "deviation_pct": None,
        }

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
) -> tuple[float | None, list[dict], dict]:
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
        return None, warnings, {
            "cog_y_pct": None, "offset_from_center_pct": None, "tolerance_pct": None,
        }

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    tolerance = config.get("lateral_tolerance_pct", 0.05)
    _, _, min_y, max_y = _get_boat_extents(zones)
    y_span = max_y - min_y

    if y_span < 1e-6:
        warnings.append({
            "code": "STRUCTURAL_NO_EXTENT",
            "severity": "warning",
            "message": (
                "Querverteilung nicht beurteilbar: die Zonen des Layouts haben keine "
                "Querausdehnung, auf die eine Position bezogen werden könnte."
            ),
            "suggestion": "Polygonkoordinaten der Zonen prüfen (alle y-Werte identisch).",
            "location": "layout.zones[].polygon",
        })
        # Bisher volle Punktzahl: ein Layout ohne Querausdehnung galt als
        # perfekt mittig ausgewogen, obwohl es dafür keine Grundlage gibt.
        return None, warnings, {
            "cog_y_pct": None, "offset_from_center_pct": None, "tolerance_pct": tolerance,
        }

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


# ---------------------------------------------------------------------------
# Sub-analysis: Heavy zone placement
# ---------------------------------------------------------------------------


def analyze_heavy_zone_placement(
    zones: list[dict],
    config: dict,
) -> tuple[float | None, list[dict], dict]:
    """Check if heavy zones are centrally positioned.

    Returns (score 0-100 oder None, warnings, metrics). ``None`` bedeutet
    "nicht beurteilbar" — es gab keine schwere Zone zu prüfen oder keine
    Längsausdehnung, auf die sich eine Lage beziehen könnte.
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "code": "STRUCTURAL_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen für Schwerzonen-Analyse vorhanden.",
            "suggestion": "Zonen dem Layout zuweisen.",
            "location": "layout.zones",
        })
        return None, warnings, {
            "heavy_zones": [], "total_heavy_weight_kg": None, "central_ratio": None,
        }

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    central_band = config.get("central_band", (0.20, 0.80))
    min_x, max_x, _, _ = _get_boat_extents(zones)
    x_span = max_x - min_x

    heavy_zones = [z for z in zones if z.get("zone_type") in _HEAVY_ZONE_TYPES]

    if not heavy_zones:
        # Keine schwere Zone im Layout heisst nicht "Schwerpunktlage in Ordnung".
        # Die bisherige 100.0 mit central_ratio 1.0 gab eine Unbedenklichkeits-
        # bescheinigung fuer eine Pruefung, die kein Pruefobjekt hatte — und
        # erfand dazu eine Kennzahl, die nie gemessen wurde.
        warnings.append({
            "code": "STRUCTURAL_NO_HEAVY_ZONES",
            "severity": "info",
            "message": (
                "Schwerzonen-Lage nicht beurteilbar: keine schweren Zonen "
                "(Motor, Stauraum, Tanks) im Layout erkannt."
            ),
            "suggestion": "Motor-, Tank- und Stauräume im Layout definieren.",
            "location": "layout.zones",
        })
        return None, warnings, {
            "heavy_zones": [], "total_heavy_weight_kg": None, "central_ratio": None,
        }

    if x_span < 1e-6:
        # Ohne Laengsausdehnung gibt es keinen Bezug, auf den sich "mittig"
        # beziehen koennte. Auch das ist keine bestandene Pruefung.
        warnings.append({
            "code": "STRUCTURAL_NO_EXTENT",
            "severity": "warning",
            "message": (
                "Schwerzonen-Lage nicht beurteilbar: die Zonen des Layouts haben "
                "keine Längsausdehnung, auf die eine Position bezogen werden könnte."
            ),
            "suggestion": "Polygonkoordinaten der Zonen prüfen (alle x-Werte identisch).",
            "location": "layout.zones[].polygon",
        })
        return None, warnings, {
            "heavy_zones": [], "total_heavy_weight_kg": None, "central_ratio": None,
        }

    heavy_info = []
    total_heavy_weight = 0.0
    central_weight = 0.0

    for z in heavy_zones:
        w = _estimate_zone_weight(z, weight_factor)
        cx, _ = _polygon_centroid(z.get("polygon", []))
        cx_pct = (cx - min_x) / x_span
        is_central = central_band[0] <= cx_pct <= central_band[1]

        total_heavy_weight += w
        if is_central:
            central_weight += w
        else:
            severity = "critical" if cx_pct < 0.15 or cx_pct > 0.85 else "warning"
            warnings.append({
                "code": "HEAVY_ZONE_OFF_CENTER",
                "severity": severity,
                "message": (
                    f"Schwere Zone '{z.get('name', '?')}' ({z.get('zone_type')}) "
                    f"bei {cx_pct:.0%} der Bootslänge — "
                    f"außerhalb des zentralen Bereichs ({central_band[0]:.0%}–{central_band[1]:.0%})."
                ),
                "suggestion": f"Zone '{z.get('name', '?')}' weiter zur Mitte verlagern.",
            })

        heavy_info.append({
            "name": z.get("name", "?"),
            "zone_type": z.get("zone_type"),
            "centroid_x_pct": round(cx_pct, 4),
            "weight_kg": round(w, 1),
            "is_central": is_central,
        })

    if total_heavy_weight <= 0:
        # Schwere Zonen ohne Gewichtsschaetzung: das Verhaeltnis waere durch
        # null zu teilen. Der frueher eingesetzte Ersatzwert 1.0 hiess
        # "vollstaendig mittig" — eine Aussage ohne jede Grundlage.
        warnings.append({
            "code": "STRUCTURAL_NO_WEIGHT",
            "severity": "warning",
            "message": (
                "Schwerzonen-Lage nicht beurteilbar: für die schweren Zonen "
                "konnte kein Gewicht abgeschätzt werden (Fläche 0)."
            ),
            "suggestion": "Polygonflächen der Motor-, Tank- und Stauräume prüfen.",
            "location": "layout.zones[].polygon",
        })
        return None, warnings, {
            "heavy_zones": heavy_info,
            "total_heavy_weight_kg": None,
            "central_ratio": None,
        }

    central_ratio = central_weight / total_heavy_weight

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
) -> tuple[float | None, list[dict], dict]:
    """Evaluate weight distribution across three longitudinal segments.

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
        return None, warnings, {
            "segment_weights": None, "segment_fractions": None,
            "heaviest_segment": None, "cv": None,
        }

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    warn_threshold = config.get("concentration_warn_threshold", 0.55)
    min_x, max_x, _, _ = _get_boat_extents(zones)
    x_span = max_x - min_x

    if x_span < 1e-6:
        warnings.append({
            "code": "STRUCTURAL_NO_EXTENT",
            "severity": "warning",
            "message": (
                "Lastkonzentration nicht beurteilbar: die Zonen des Layouts haben keine "
                "Längsausdehnung, auf die eine Position bezogen werden könnte."
            ),
            "suggestion": "Polygonkoordinaten der Zonen prüfen (alle x-Werte identisch).",
            "location": "layout.zones[].polygon",
        })
        return None, warnings, {
            "segment_weights": None, "segment_fractions": None,
            "heaviest_segment": None, "cv": None,
        }

    # Divide into 3 equal segments
    third = x_span / 3.0
    boundaries = [min_x, min_x + third, min_x + 2 * third, max_x]
    segment_weights: dict[str, float] = {"bow": 0.0, "middle": 0.0, "stern": 0.0}

    for z in zones:
        w = _estimate_zone_weight(z, weight_factor)
        cx, _ = _polygon_centroid(z.get("polygon", []))
        # Assign to segment by centroid position
        if cx < boundaries[1]:
            segment_weights["bow"] += w
        elif cx < boundaries[2]:
            segment_weights["middle"] += w
        else:
            segment_weights["stern"] += w

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
) -> tuple[float | None, list[dict], dict]:
    """Compute CG position under different loading conditions.

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
        return None, warnings, {"conditions": None}

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    ideal_range = config.get("ideal_cog_x_range", (0.44, 0.54))
    min_x, max_x, _, _ = _get_boat_extents(zones)
    x_span = max_x - min_x

    if x_span < 1e-6:
        warnings.append({
            "code": "STRUCTURAL_NO_EXTENT",
            "severity": "warning",
            "message": (
                "Beladungszustände nicht beurteilbar: die Zonen des Layouts haben keine "
                "Längsausdehnung, auf die eine Position bezogen werden könnte."
            ),
            "suggestion": "Polygonkoordinaten der Zonen prüfen (alle x-Werte identisch).",
            "location": "layout.zones[].polygon",
        })
        return None, warnings, {"conditions": None}

    condition_results: dict[str, float] = {}
    in_range_count = 0

    for cond_name, cond in LOADING_CONDITIONS.items():
        fuel_pct = cond["fuel_pct"]
        water_pct = cond["water_pct"]
        stores_pct = cond["stores_pct"]

        total_weight = 0.0
        weighted_x = 0.0

        for z in zones:
            base_weight = _estimate_zone_weight(z, weight_factor)
            zone_type = z.get("zone_type", "")

            if zone_type == "engine":
                adjusted_weight = base_weight * (fuel_pct / 100.0)
            elif zone_type == "storage":
                adjusted_weight = base_weight * (stores_pct / 100.0)
            elif zone_type in ("head", "pantry"):
                adjusted_weight = base_weight * (water_pct / 100.0)
            else:
                adjusted_weight = base_weight

            cx, _ = _polygon_centroid(z.get("polygon", []))
            total_weight += adjusted_weight
            weighted_x += cx * adjusted_weight

        if total_weight < 1e-6:
            condition_results[cond_name] = 0.5
            continue

        cog_x = weighted_x / total_weight
        cog_x_pct = (cog_x - min_x) / x_span
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
) -> tuple[float | None, list[dict], dict]:
    """Estimate longitudinal trim angle from weight distribution.

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
        return None, warnings, {
            "trim_deg": None, "cog_x_pct": None, "ideal_midpoint_pct": None,
        }

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    ideal_range = config.get("ideal_cog_x_range", (0.44, 0.54))
    max_trim_deg = config.get("max_trim_deg", 2.0)
    min_x, max_x, _, _ = _get_boat_extents(zones)
    x_span = max_x - min_x

    if x_span < 1e-6:
        warnings.append({
            "code": "STRUCTURAL_NO_EXTENT",
            "severity": "warning",
            "message": (
                "Trimmlage nicht beurteilbar: die Zonen des Layouts haben keine "
                "Längsausdehnung, auf die eine Position bezogen werden könnte."
            ),
            "suggestion": "Polygonkoordinaten der Zonen prüfen (alle x-Werte identisch).",
            "location": "layout.zones[].polygon",
        })
        return None, warnings, {
            "trim_deg": None, "cog_x_pct": None, "ideal_midpoint_pct": None,
        }

    total_weight = 0.0
    weighted_x = 0.0

    for z in zones:
        w = _estimate_zone_weight(z, weight_factor)
        cx, _ = _polygon_centroid(z.get("polygon", []))
        total_weight += w
        weighted_x += cx * w

    if total_weight < 1e-6:
        return 50.0, warnings, {"trim_deg": 0.0, "cog_x_pct": 0.5, "ideal_midpoint_pct": 0.5}

    cog_x = weighted_x / total_weight
    cog_x_pct = (cog_x - min_x) / x_span

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
) -> dict:
    """Orchestrator — runs all structural (weight distribution) sub-analyses.

    Args:
        zones: Layout zones with polygon, zone_type, name.
        passages: Unused — accepted for API pattern consistency.
        boat_class: One of small_sail, cruising_sail, large_motor, superyacht.
        config_overrides: Optional dict to override config values.

    Returns a standardized result dict matching the AYDI analysis module contract.
    """
    # Ein Layout ohne Zonen ist kein Layout. Ohne diese Pruefung lieferten die
    # Teilanalysen ihre jeweiligen Vorgabewerte zurueck, und daraus entstand ein
    # Gesamtwert, der wie ein Befund aussah — obwohl nichts gemessen wurde.
    if not isinstance(zones, list) or len(zones) == 0:
        return {
            "module": "structural",
            "available": False,
            "reason": "Das Layout enthält keine Zonen — es gibt nichts zu bewerten.",
            "suggestions": [
                "Zonen im Layout anlegen oder ein CAD-Modell importieren."
            ],
        }

    # Zonentypen vereinheitlichen, bevor irgendeine Pruefung ihre Menge bildet.
    # Die Module suchen ihre Pruefobjekte ueber exakte Mengenzugehoerigkeit; eine
    # abweichende Schreibweise ("saloon" statt "salon", "engine_room" statt
    # "engine") liess die Menge leer bleiben und die Pruefung meldete daraufhin
    # volle Punktzahl. Siehe app/core/zone_types.py.
    zones, _unbekannte_zonentypen = normalisiere_zonen(zones)

    if boat_class not in BOAT_CLASS_DEFAULTS:
        return {"available": False, "reason": f"Unbekannte Bootsklasse: {boat_class}"}

    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    weights = config.pop("weights").copy()

    if config_overrides:
        config.update(config_overrides)

    # Short-circuit: no zones → score 50 + single info warning
    # Der frühere Kurzschluss "keine Zonen -> Gesamtnote 50.0" ist entfallen.
    # Er war seit der Leer-Layout-Prüfung weiter oben ohnehin unerreichbar und
    # hätte ein leeres Layout mit einer Zahl statt mit "nicht beurteilbar"
    # beantwortet.
    sub_scores: dict[str, float | None] = {}
    all_warnings: list[dict] = []
    all_suggestions: list[str] = []
    all_metrics: dict[str, dict] = {}

    analyses = [
        ("fore_aft", lambda: analyze_fore_aft_balance(zones, config)),
        ("lateral", lambda: analyze_lateral_balance(zones, config)),
        ("heavy_placement", lambda: analyze_heavy_zone_placement(zones, config)),
        ("load_concentration", lambda: analyze_load_concentration(zones, config)),
        ("loading_conditions", lambda: analyze_loading_conditions(zones, config)),
        ("trim", lambda: analyze_trim(zones, config)),
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

    # Unbekannte Zonentypen gehoeren in den Befund, nicht ins Protokoll: eine
    # Zone mit unbekanntem Typ ist fuer die typbezogenen Pruefungen unsichtbar.
    # Ohne diesen Hinweis liest sich das Ergebnis so, als waere sie geprueft.
    _warnung_zonentypen = warnung_unbekannte_typen(_unbekannte_zonentypen)
    if _warnung_zonentypen:
        all_warnings.append(_warnung_zonentypen)

    # Teilanalysen ohne Datengrundlage geben None zurueck und bleiben aus der
    # Rechnung heraus; ihr Gewicht verteilt sich auf die geprueften. Frueher
    # ging hier ein Vorgabewert ein — bei fehlenden Eintraegen 0.0 bzw. 50.0 —
    # und erzeugte eine Note fuer etwas, das nie geprueft wurde.
    overall, _nicht_bewertet = weighted_overall(sub_scores, weights)
    if overall is None:
        return {
            "module": "structural",
            "available": False,
            "reason": "Keine der Teilanalysen konnte mangels Datengrundlage durchgeführt werden.",
            "suggestions": [
                "Layout- und Stammdaten vervollständigen, um eine Bewertung zu ermöglichen."
            ],
        }

    for w in all_warnings:
        suggestion = w.get("suggestion")
        if suggestion and suggestion not in all_suggestions:
            all_suggestions.append(suggestion)

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    return {
        "module": "structural",
        "overall_score": round(overall, 1),
        # Eine Teilanalyse ohne Datengrundlage traegt None — sie wird als
        # solche weitergereicht statt auf eine Zahl gerundet zu werden.
        "sub_scores": {
            k: (round(v, 1) if v is not None else None)
            for k, v in sub_scores.items()
        },
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
        "confidence": data_source,
        "confidence_note": "Basiert auf geschätzten Werten aus öffentlichen Spezifikationen." if data_source == "estimated" else None,
        "coverage_note": hinweis_teilanalysen(_nicht_bewertet),
        "unassessed_sub_analyses": _nicht_bewertet,
    }
