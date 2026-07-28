"""Compliance checker module for yacht layouts.

Automated check against maritime safety norms (ISO 9094, ISO 12217,
ISO 15085, ISO 10133, ISO 13297). Pure function module — no database access.
All user-facing strings are in German.
"""
import logging
import math
from collections import deque
from app.core.zone_types import normalisiere_zonen, warnung_unbekannte_typen
from app.services.analysis.scoring import weighted_overall, hinweis_teilanalysen

logger = logging.getLogger(__name__)

# Try to import knowledge databases for electrical and safety compliance
try:
    from app.services.knowledge.electrical_systems_deep import (
        CRITICAL_WARNINGS,
    )
except ImportError:
    CRITICAL_WARNINGS = {}

try:
    from app.services.knowledge.sanitary_interior_safety_deep import (
        STANDARDS_DATABASE,
        FIRE_SAFETY_DATABASE,
        STABILITY_DATABASE,
        GAS_INSTALLATION_DATABASE,
    )
except ImportError:
    STANDARDS_DATABASE = {}
    FIRE_SAFETY_DATABASE = {}
    STABILITY_DATABASE = {}
    GAS_INSTALLATION_DATABASE = {}

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 4,
        "min_engine_clearance_mm": 500,
        "min_engine_area_sqm": 0.8,
        "min_electrical_area_sqm": 0.3,
        "required_railing_zones": ["foredeck", "cockpit"],
        "ce_category": "C",
        "cockpit_depth_mm": 300,
        "companionway_sill_mm": 150,
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
            "ISO_12216": "2002",
            "ISO_11812": "2001",
        },
        "weights": {
            "escape_routes": 0.24,
            "fire_safety": 0.16,
            "stability": 0.12,
            "railing": 0.08,
            "electrical_access": 0.08,
            "ce_category": 0.12,
            "escape_hatch": 0.05,
            "cockpit_drain": 0.05,
            "companionway_sill": 0.05,
            "ventilation": 0.05,
        },
    },
    "cruising_sail": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 5,
        "min_engine_clearance_mm": 600,
        "min_engine_area_sqm": 1.2,
        "min_electrical_area_sqm": 0.5,
        "required_railing_zones": ["foredeck", "cockpit"],
        "ce_category": "A",
        "cockpit_depth_mm": 300,
        "companionway_sill_mm": 300,
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
            "ISO_12216": "2002",
            "ISO_11812": "2001",
        },
        "weights": {
            "escape_routes": 0.20,
            "fire_safety": 0.16,
            "stability": 0.16,
            "railing": 0.08,
            "electrical_access": 0.08,
            "ce_category": 0.12,
            "escape_hatch": 0.05,
            "cockpit_drain": 0.05,
            "companionway_sill": 0.05,
            "ventilation": 0.05,
        },
    },
    "large_motor": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 6,
        "min_engine_clearance_mm": 800,
        "min_engine_area_sqm": 2.0,
        "min_electrical_area_sqm": 0.8,
        "required_railing_zones": ["foredeck", "cockpit", "flybridge", "swim_platform"],
        "ce_category": "A",
        "cockpit_depth_mm": 300,
        "companionway_sill_mm": 300,
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
            "ISO_12216": "2002",
            "ISO_11812": "2001",
        },
        "weights": {
            "escape_routes": 0.20,
            "fire_safety": 0.20,
            "stability": 0.08,
            "railing": 0.12,
            "electrical_access": 0.08,
            "ce_category": 0.12,
            "escape_hatch": 0.05,
            "cockpit_drain": 0.05,
            "companionway_sill": 0.05,
            "ventilation": 0.05,
        },
    },
    "racing_sail": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 4,
        "min_engine_clearance_mm": 500,
        "min_engine_area_sqm": 0.6,
        "min_electrical_area_sqm": 0.25,
        "required_railing_zones": ["foredeck", "cockpit"],
        "ce_category": "B",
        "cockpit_depth_mm": 300,
        "companionway_sill_mm": 200,
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
            "ISO_12216": "2002",
            "ISO_11812": "2001",
        },
        "weights": {
            "escape_routes": 0.22,
            "fire_safety": 0.16,
            "stability": 0.14,
            "railing": 0.08,
            "electrical_access": 0.08,
            "ce_category": 0.12,
            "escape_hatch": 0.05,
            "cockpit_drain": 0.05,
            "companionway_sill": 0.05,
            "ventilation": 0.05,
        },
    },
    "daysailer": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 4,
        "min_engine_clearance_mm": 500,
        "min_engine_area_sqm": 0.7,
        "min_electrical_area_sqm": 0.3,
        "required_railing_zones": ["foredeck", "cockpit"],
        "ce_category": "D",
        "cockpit_depth_mm": 300,
        "companionway_sill_mm": 100,
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
            "ISO_12216": "2002",
            "ISO_11812": "2001",
        },
        "weights": {
            "escape_routes": 0.24,
            "fire_safety": 0.16,
            "stability": 0.12,
            "railing": 0.08,
            "electrical_access": 0.08,
            "ce_category": 0.12,
            "escape_hatch": 0.05,
            "cockpit_drain": 0.05,
            "companionway_sill": 0.05,
            "ventilation": 0.05,
        },
    },
    "motorsailer": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 5,
        "min_engine_clearance_mm": 650,
        "min_engine_area_sqm": 1.3,
        "min_electrical_area_sqm": 0.5,
        "required_railing_zones": ["foredeck", "cockpit"],
        "ce_category": "B",
        "cockpit_depth_mm": 300,
        "companionway_sill_mm": 250,
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
            "ISO_12216": "2002",
            "ISO_11812": "2001",
        },
        "weights": {
            "escape_routes": 0.20,
            "fire_safety": 0.18,
            "stability": 0.14,
            "railing": 0.08,
            "electrical_access": 0.08,
            "ce_category": 0.12,
            "escape_hatch": 0.05,
            "cockpit_drain": 0.05,
            "companionway_sill": 0.05,
            "ventilation": 0.05,
        },
    },
    "catamaran_sail": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 5,
        "min_engine_clearance_mm": 600,
        "min_engine_area_sqm": 1.0,
        "min_electrical_area_sqm": 0.4,
        "required_railing_zones": ["foredeck", "cockpit"],
        "ce_category": "A",
        "cockpit_depth_mm": 300,
        "companionway_sill_mm": 250,
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
            "ISO_12216": "2002",
            "ISO_11812": "2001",
        },
        "weights": {
            "escape_routes": 0.20,
            "fire_safety": 0.16,
            "stability": 0.16,
            "railing": 0.08,
            "electrical_access": 0.08,
            "ce_category": 0.12,
            "escape_hatch": 0.05,
            "cockpit_drain": 0.05,
            "companionway_sill": 0.05,
            "ventilation": 0.05,
        },
    },
    "catamaran_motor": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 6,
        "min_engine_clearance_mm": 800,
        "min_engine_area_sqm": 1.8,
        "min_electrical_area_sqm": 0.7,
        "required_railing_zones": ["foredeck", "cockpit", "flybridge"],
        "ce_category": "A",
        "cockpit_depth_mm": 300,
        "companionway_sill_mm": 300,
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
            "ISO_12216": "2002",
            "ISO_11812": "2001",
        },
        "weights": {
            "escape_routes": 0.20,
            "fire_safety": 0.20,
            "stability": 0.08,
            "railing": 0.12,
            "electrical_access": 0.08,
            "ce_category": 0.12,
            "escape_hatch": 0.05,
            "cockpit_drain": 0.05,
            "companionway_sill": 0.05,
            "ventilation": 0.05,
        },
    },
    "small_motor": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 5,
        "min_engine_clearance_mm": 700,
        "min_engine_area_sqm": 1.5,
        "min_electrical_area_sqm": 0.6,
        "required_railing_zones": ["foredeck", "cockpit"],
        "ce_category": "C",
        "cockpit_depth_mm": 300,
        "companionway_sill_mm": 250,
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
            "ISO_12216": "2002",
            "ISO_11812": "2001",
        },
        "weights": {
            "escape_routes": 0.21,
            "fire_safety": 0.19,
            "stability": 0.09,
            "railing": 0.09,
            "electrical_access": 0.08,
            "ce_category": 0.12,
            "escape_hatch": 0.05,
            "cockpit_drain": 0.05,
            "companionway_sill": 0.05,
            "ventilation": 0.05,
        },
    },
    "sport_cruiser": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 6,
        "min_engine_clearance_mm": 800,
        "min_engine_area_sqm": 1.8,
        "min_electrical_area_sqm": 0.7,
        "required_railing_zones": ["foredeck", "cockpit", "flybridge"],
        "ce_category": "A",
        "cockpit_depth_mm": 300,
        "companionway_sill_mm": 300,
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
            "ISO_12216": "2002",
            "ISO_11812": "2001",
        },
        "weights": {
            "escape_routes": 0.20,
            "fire_safety": 0.20,
            "stability": 0.08,
            "railing": 0.12,
            "electrical_access": 0.08,
            "ce_category": 0.12,
            "escape_hatch": 0.05,
            "cockpit_drain": 0.05,
            "companionway_sill": 0.05,
            "ventilation": 0.05,
        },
    },
    "trawler": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 7,
        "min_engine_clearance_mm": 900,
        "min_engine_area_sqm": 2.2,
        "min_electrical_area_sqm": 0.8,
        "required_railing_zones": ["foredeck", "cockpit", "flybridge"],
        "ce_category": "A",
        "cockpit_depth_mm": 300,
        "companionway_sill_mm": 300,
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
            "ISO_12216": "2002",
            "ISO_11812": "2001",
        },
        "weights": {
            "escape_routes": 0.20,
            "fire_safety": 0.20,
            "stability": 0.08,
            "railing": 0.12,
            "electrical_access": 0.08,
            "ce_category": 0.12,
            "escape_hatch": 0.05,
            "cockpit_drain": 0.05,
            "companionway_sill": 0.05,
            "ventilation": 0.05,
        },
    },
    "explorer": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 8,
        "min_engine_clearance_mm": 1000,
        "min_engine_area_sqm": 2.8,
        "min_electrical_area_sqm": 1.0,
        "required_railing_zones": ["foredeck", "cockpit", "flybridge", "swim_platform"],
        "ce_category": "A",
        "cockpit_depth_mm": 300,
        "companionway_sill_mm": 300,
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
            "ISO_12216": "2002",
            "ISO_11812": "2001",
        },
        "weights": {
            "escape_routes": 0.1765,
            "fire_safety": 0.1961,
            "stability": 0.0980,
            "railing": 0.1373,
            "electrical_access": 0.0784,
            "ce_category": 0.1176,
            "escape_hatch": 0.0490,
            "cockpit_drain": 0.0490,
            "companionway_sill": 0.0490,
            "ventilation": 0.0490,
        },
    },
    "superyacht": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 8,
        "min_engine_clearance_mm": 1000,
        "min_engine_area_sqm": 4.0,
        "min_electrical_area_sqm": 1.5,
        "required_railing_zones": ["foredeck", "cockpit", "flybridge", "swim_platform"],
        "ce_category": "A",
        "cockpit_depth_mm": 300,
        "companionway_sill_mm": 300,
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
            "ISO_12216": "2002",
            "ISO_11812": "2001",
        },
        "weights": {
            "escape_routes": 0.16,
            "fire_safety": 0.20,
            "stability": 0.08,
            "railing": 0.16,
            "electrical_access": 0.08,
            "ce_category": 0.12,
            "escape_hatch": 0.05,
            "cockpit_drain": 0.05,
            "companionway_sill": 0.05,
            "ventilation": 0.05,
        },
    },
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}

_SLEEPING_ZONE_TYPES = {"cabin", "crew_quarters"}

_CE_REQUIRED_ZONES = {
    "A": {"cockpit", "engine", "helm", "cabin", "head", "pantry"},
    "B": {"cockpit", "engine", "helm", "cabin", "head"},
    "C": {"cockpit", "engine", "helm"},
    "D": {"helm"},
}

_CE_ZONE_LABELS = {
    "cockpit": "Cockpit",
    "engine": "Maschinenraum",
    "helm": "Steuerstand",
    "cabin": "Kabine",
    "head": "WC/Bad",
    "pantry": "Pantry",
}
_LIVING_ZONE_TYPES = {"salon", "cabin", "pantry", "crew_quarters", "helm"}
_HEAVY_ZONE_TYPES = {"engine", "storage"}


# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------


def _polygon_area_sqm(polygon: list[list[float]]) -> float:
    """Shoelace formula — returns area in square meters (polygon in mm)."""
    n = len(polygon)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2.0 / 1_000_000


def _centroid(polygon: list[list[float]]) -> tuple[float, float]:
    """Return centroid as average of polygon vertices (in mm)."""
    if not polygon:
        return (0.0, 0.0)
    cx = sum(p[0] for p in polygon) / len(polygon)
    cy = sum(p[1] for p in polygon) / len(polygon)
    return (cx, cy)


def _build_adjacency(passages: list[dict]) -> dict[str, set[str]]:
    """Build bidirectional adjacency graph from passages."""
    graph: dict[str, set[str]] = {}
    for p in passages:
        a, b = p["from_zone"], p["to_zone"]
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    return graph


def _bfs_reachable(graph: dict[str, set[str]], start: str) -> set[str]:
    """Return all nodes reachable from start via BFS."""
    if start not in graph:
        return {start}
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


def _bfs_path(
    graph: dict[str, set[str]],
    start: str,
    targets: set[str],
) -> list[str] | None:
    """BFS shortest path from start to any node in targets.

    Returns the list of zone names (including start and target), or None
    if no path exists.
    """
    if not targets:
        return None
    if start in targets:
        return [start]
    if start not in graph:
        return None

    visited = {start}
    # Queue entries: (current_node, path_so_far)
    queue: deque[tuple[str, list[str]]] = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        for neighbor in graph.get(node, set()):
            if neighbor in targets:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None


def _widest_passage_between(passages: list[dict], zone_a: str, zone_b: str) -> float:
    """Return the widest passage width_mm between zone_a and zone_b (bidirectional)."""
    best = 0.0
    for p in passages:
        if (p["from_zone"] == zone_a and p["to_zone"] == zone_b) or (
            p["from_zone"] == zone_b and p["to_zone"] == zone_a
        ):
            if p["width_mm"] > best:
                best = p["width_mm"]
    return best


# ---------------------------------------------------------------------------
# Sub-analysis: escape routes (ISO 9094)
# ---------------------------------------------------------------------------


def analyze_escape_routes(
    zones: list[dict],
    passages: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check escape route compliance per ISO 9094.

    Every sleeping zone must have a path to a cockpit zone with:
    - max hops <= max_escape_hops
    - all passage widths along path >= min_escape_width_mm

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    sleeping_zones = [z for z in zones if z["zone_type"] in _SLEEPING_ZONE_TYPES]
    cockpit_zones = {z["name"] for z in zones if z["zone_type"] == "cockpit"}

    # Kein Schlafbereich auffindbar — es wurde nichts geprueft. Frueher stand
    # hier volle Punktzahl; das las sich wie eine bestandene Fluchtwegpruefung,
    # obwohl kein einziger Weg verfolgt wurde. Ob wirklich keine Kabine
    # vorhanden ist oder nur keine als solche erfasst wurde, laesst sich von
    # hier aus nicht entscheiden — also wird nicht bewertet.
    if not sleeping_zones:
        warnings.append({
            "code": "NO_SLEEPING_ZONES",
            "severity": "info",
            "message": "Keine Schlafbereiche im Layout — die Fluchtwegprüfung nach ISO 9094 konnte nicht durchgeführt werden.",
            "suggestion": "Schlafbereiche als Zonentyp cabin, aft_cabin, quarter_berth oder crew_quarters erfassen, damit die Fluchtwege geprüft werden können.",
            "location": "layout",
        })
        return None, warnings, {"cabins_checked": 0, "cabins_compliant": 0, "cabins_total": 0}

    # No cockpit — all cabins are unreachable
    if not cockpit_zones:
        warnings.append({
            "code": "ISO_9094_NO_COCKPIT",
            "severity": "critical",
            "message": "Kein Cockpit im Layout — Fluchtwege nach ISO 9094 nicht prüfbar.",
            "suggestion": "Cockpit-Zone zum Layout hinzufügen.",
        })
        return 0.0, warnings, {
            "cabins_checked": len(sleeping_zones),
            "cabins_compliant": 0,
            "cabins_total": len(sleeping_zones),
        }

    graph = _build_adjacency(passages)
    min_width = config["min_escape_width_mm"]
    max_hops = config["max_escape_hops"]

    total = len(sleeping_zones)
    compliant = 0
    noncompliant_reachable = 0

    for zone in sleeping_zones:
        name = zone["name"]
        path = _bfs_path(graph, name, cockpit_zones)

        if path is None:
            warnings.append({
                "code": "ISO_9094_ESCAPE_ROUTE",
                "severity": "critical",
                "message": f"Schlafbereich '{name}' hat keinen Fluchtweg zum Cockpit (ISO 9094).",
                "suggestion": f"Fluchtwegverbindung von '{name}' zum Cockpit herstellen.",
            })
            # unreachable — contributes 0 pts
            continue

        hops = len(path) - 1  # number of passages traversed
        hop_ok = hops <= max_hops

        if not hop_ok:
            warnings.append({
                "code": "ISO_9094_ESCAPE_ROUTE_TOO_LONG",
                "severity": "warning",
                "message": (
                    f"Fluchtweg von '{name}' zum Cockpit zu lang "
                    f"({hops} Schritte, Maximum: {max_hops}, ISO 9094)."
                ),
                "suggestion": f"Fluchtwegverbindung von '{name}' verkürzen.",
            })

        # Check widths along path edges
        width_ok = True
        for i in range(len(path) - 1):
            w = _widest_passage_between(passages, path[i], path[i + 1])
            if w < min_width:
                width_ok = False
                warnings.append({
                    "code": "ISO_9094_ESCAPE_WIDTH",
                    "severity": "critical",
                    "message": (
                        f"Fluchtweg '{path[i]} → {path[i + 1]}': Breite {w:.0f} mm "
                        f"unterschreitet ISO 9094 Minimum ({min_width:.0f} mm)."
                    ),
                    "suggestion": f"Breite des Durchgangs '{path[i]} → {path[i + 1]}' auf mindestens {min_width:.0f} mm erhöhen.",
                })
                break  # one width warning per cabin path is enough

        if width_ok and hop_ok:
            compliant += 1
        else:
            noncompliant_reachable += 1

    # Scoring: compliant=100pts, reachable-but-noncompliant=50pts, unreachable=0pts
    score = (compliant * 100.0 + noncompliant_reachable * 50.0) / total

    return score, warnings, {
        "cabins_checked": total,
        "cabins_compliant": compliant,
        "cabins_total": total,
    }


# ---------------------------------------------------------------------------
# Sub-analysis: fire safety (ISO 9094)
# ---------------------------------------------------------------------------


def analyze_fire_safety(
    zones: list[dict],
    passages: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check fire safety compliance per ISO 9094.

    Checks:
    1. Clearance: centroid distance between engine and living zones.
    2. Accessibility: engine zone must be reachable via passages.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    engine_zones = [z for z in zones if z["zone_type"] == "engine"]
    living_zones = [z for z in zones if z["zone_type"] in _LIVING_ZONE_TYPES]

    # Ohne Maschinenraum gibt es weder einen Brandschutzabstand noch einen
    # Zugang zu pruefen. Frueher standen hier 50.0 — eine Zahl, die sich in der
    # Oberflaeche von einer gemessenen nicht unterscheiden liess.
    if not engine_zones:
        warnings.append({
            "code": "ISO_9094_NO_ENGINE",
            "severity": "info",
            "message": (
                "Kein Maschinenraum im Layout gefunden — die Brandschutzprüfung "
                "nach ISO 9094 konnte nicht durchgeführt werden."
            ),
            "suggestion": "Maschinenraum als Zonentyp engine im Layout erfassen.",
            "location": "layout",
        })
        return None, warnings, {
            "engine_zones": 0,
            "min_clearance_mm": None,
            "engine_accessible": False,
        }

    min_clearance = config["min_engine_clearance_mm"]

    # --- Clearance check ---
    min_dist: float | None = None
    if living_zones:
        for eng in engine_zones:
            eng_cx, eng_cy = _centroid(eng["polygon"])
            for liv in living_zones:
                liv_cx, liv_cy = _centroid(liv["polygon"])
                dist = math.sqrt((eng_cx - liv_cx) ** 2 + (eng_cy - liv_cy) ** 2)
                if min_dist is None or dist < min_dist:
                    min_dist = dist

    if min_dist is None:
        # Kein Wohnbereich, zu dem sich ein Abstand messen liesse. Frueher 100.0 —
        # der Abstand galt damit als eingehalten, obwohl er nie gemessen wurde.
        clearance_score = None
        warnings.append({
            "code": "ISO_9094_NO_LIVING_ZONES",
            "severity": "info",
            "message": (
                "Keine Wohnbereiche im Layout gefunden — der Brandschutzabstand "
                "zum Maschinenraum konnte nicht gemessen werden."
            ),
            "suggestion": (
                "Wohnbereiche als Zonentyp salon, cabin, pantry oder head erfassen, "
                "damit der Abstand zum Maschinenraum geprüft werden kann."
            ),
            "location": "layout",
        })
    elif min_dist >= min_clearance:
        clearance_score = 100.0
    else:
        ratio = min_dist / min_clearance if min_clearance > 0 else 0.0
        clearance_score = ratio * 100.0
        warnings.append({
            "code": "ISO_9094_ENGINE_CLEARANCE",
            "severity": "warning",
            "message": (
                f"Maschinenraum zu nahe an Wohnbereichen "
                f"({min_dist:.0f} mm Abstand, Minimum: {min_clearance:.0f} mm, ISO 9094)."
            ),
            "suggestion": f"Maschinenraum weiter von Wohnbereichen entfernen (mindestens {min_clearance:.0f} mm).",
        })

    # --- Accessibility check ---
    graph = _build_adjacency(passages)
    engine_names = {z["name"] for z in engine_zones}
    other_zone_names = {z["name"] for z in zones if z["name"] not in engine_names}

    engine_accessible = False
    if other_zone_names:
        # Check if at least one non-engine zone can reach at least one engine zone
        for eng_name in engine_names:
            reachable = _bfs_reachable(graph, eng_name)
            if reachable & other_zone_names:
                engine_accessible = True
                break

    if not other_zone_names:
        # Nur Maschinenraumzonen im Layout — es gibt keinen Bereich, von dem aus
        # eine Erreichbarkeit zu pruefen waere. Frueher fiel dieser Fall in den
        # else-Zweig und ergab volle Punktzahl.
        access_score = None
        warnings.append({
            "code": "ISO_9094_ACCESS_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                "Das Layout enthält ausschließlich Maschinenraumzonen — die "
                "Erreichbarkeit des Maschinenraums konnte nicht geprüft werden."
            ),
            "suggestion": "Übrige Zonen des Bootes im Layout erfassen.",
            "location": "layout",
        })
    elif not engine_accessible:
        access_score = 0.0
        warnings.append({
            "code": "ISO_9094_ENGINE_INACCESSIBLE",
            "severity": "critical",
            "message": "Maschinenraum nicht über Durchgänge erreichbar (ISO 9094 Brandschutz).",
            "suggestion": "Zugang zum Maschinenraum über mindestens einen Durchgang sicherstellen.",
        })
    else:
        access_score = 100.0

    # Enrich with fire safety knowledge from database
    if FIRE_SAFETY_DATABASE:
        try:
            # Check for critical fire safety risks
            critical_hazards = FIRE_SAFETY_DATABASE.get("critical_hazards", [])
            for hazard in critical_hazards[:2]:  # Top 2 hazards
                if isinstance(hazard, dict):
                    warnings.append({
                        "code": "FIRE_SAFETY_HAZARD",
                        "severity": "warning",
                        "message": (
                            f"Brandschutz-Risiko: {hazard.get('hazard_name', '?')} — "
                            f"{hazard.get('description', '?')}"
                        ),
                        "suggestion": (
                            f"Brandschutzplan und Evakuierungsrouten überprüfen. "
                            f"{hazard.get('mitigation', 'Brandschutzstandards beachten.')}"
                        ),
                    })
        except (KeyError, TypeError, AttributeError):
            pass

    # Abstand und Erreichbarkeit zaehlen je zur Haelfte. Faellt eine der beiden
    # Pruefungen mangels Daten aus, traegt die andere allein — und wenn beide
    # ausfallen, gibt es keine Note.
    combined_score, _ = weighted_overall(
        {"clearance": clearance_score, "access": access_score},
        {"clearance": 0.5, "access": 0.5},
    )

    return combined_score, warnings, {
        "engine_zones": len(engine_zones),
        "min_clearance_mm": round(min_dist) if min_dist is not None else None,
        "engine_accessible": engine_accessible,
    }


# ---------------------------------------------------------------------------
# Sub-analysis: stability impact (ISO 12217)
# ---------------------------------------------------------------------------


def analyze_stability_impact(
    zones: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check stability impact by evaluating Y-axis balance of heavy zones (ISO 12217).

    Heavy zones (engine, storage) should be centered on the Y-axis.
    Significant deviation from the Y-centerline indicates a potential stability risk.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []
    norm_ref = config.get("norm_versions", {}).get("ISO_12217", "2015")

    heavy_zones = [z for z in zones if z["zone_type"] in _HEAVY_ZONE_TYPES]

    if not heavy_zones:
        warnings.append({
            "code": "ISO_12217_NO_HEAVY_ZONES",
            "severity": "info",
            "message": "Keine schweren Zonen (Maschine/Stauraum) gefunden — Stabilitätsprüfung nicht vollständig durchführbar.",
            "suggestion": "Maschinen- und Stauraumzonen zum Layout hinzufügen.",
            "norm": f"ISO 12217:{norm_ref}",
        })
        # Frueher 50.0: eine Zahl fuer eine Pruefung, die nicht stattfand.
        return None, warnings, {"heavy_zones": 0, "y_deviation_ratio": 0.0}

    # Compute layout Y-center from bounding box of ALL zones
    all_y: list[float] = []
    for z in zones:
        poly = z.get("polygon") or []
        for pt in poly:
            if len(pt) >= 2:
                all_y.append(pt[1])

    if not all_y:
        # Frueher 50.0: eine Zahl fuer eine Pruefung, die nicht stattfand.
        return None, warnings, {"heavy_zones": len(heavy_zones), "y_deviation_ratio": 0.0}

    y_min = min(all_y)
    y_max = max(all_y)
    half_beam = (y_max - y_min) / 2.0

    if half_beam == 0:
        # Frueher 50.0: eine Zahl fuer eine Pruefung, die nicht stattfand.
        return None, warnings, {"heavy_zones": len(heavy_zones), "y_deviation_ratio": 0.0}

    y_center = y_min + half_beam

    # Compute average Y-deviation ratio for heavy zones
    deviations: list[float] = []
    for z in heavy_zones:
        _, cy = _centroid(z.get("polygon") or [])
        deviation_ratio = abs(cy - y_center) / half_beam
        deviations.append(deviation_ratio)

    avg_deviation = sum(deviations) / len(deviations)

    if avg_deviation > 0.3:
        warnings.append({
            "code": "ISO_12217_STABILITY_IMBALANCE",
            "severity": "warning",
            "message": (
                f"Schwere Zonen (Maschine/Stauraum) sind nicht ausreichend zentriert "
                f"(Y-Abweichung: {avg_deviation:.1%}, ISO 12217:{norm_ref})."
            ),
            "suggestion": "Schwere Zonen näher zur Längsachse des Bootes verschieben.",
            "norm": f"ISO 12217:{norm_ref}",
        })

    score = max(0.0, (1.0 - avg_deviation) * 100.0)

    return score, warnings, {
        "heavy_zones": len(heavy_zones),
        "y_deviation_ratio": round(avg_deviation, 4),
    }


# ---------------------------------------------------------------------------
# Sub-analysis: railing requirements (ISO 15085)
# ---------------------------------------------------------------------------


def analyze_railing_requirements(
    zones: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check railing compliance for exposed deck zones per ISO 15085.

    Each zone whose zone_type is in required_railing_zones is checked for
    the `has_railing` property:
    - True  → compliant
    - False → critical violation
    - missing → info (data not available)

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []
    norm_ref = config.get("norm_versions", {}).get("ISO_15085", "2003")

    required_types: list[str] = config.get("required_railing_zones", [])
    required_zones = [z for z in zones if z["zone_type"] in required_types]

    # Kein relingpflichtiger Decksbereich auffindbar. Volle Punktzahl waere hier
    # eine Freigabe nach ISO 15085 fuer ein Deck, das nie betrachtet wurde.
    if not required_zones:
        warnings.append({
            "code": "RAILING_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                "Keine relingpflichtigen Decksbereiche im Layout gefunden — die "
                f"Relingprüfung nach ISO {norm_ref} konnte nicht durchgeführt werden."
            ),
            "suggestion": (
                "Decksbereiche mit einem der Zonentypen "
                + ", ".join(required_types)
                + " erfassen, damit die Reling geprüft werden kann."
            ),
            "location": "layout",
        })
        return None, warnings, {"zones_checked": 0, "zones_compliant": 0}

    total = len(required_zones)
    compliant = 0
    violations = 0

    for z in required_zones:
        name = z["name"]
        props = z.get("properties") or {}
        has_railing = props.get("has_railing")

        if has_railing is True:
            compliant += 1
        elif has_railing is False:
            violations += 1
            warnings.append({
                "code": "ISO_15085_RAILING_MISSING",
                "severity": "critical",
                "message": (
                    f"Zone '{name}' hat kein Reling/Sicherungsgeländer "
                    f"(ISO 15085:{norm_ref})."
                ),
                "suggestion": f"Reling/Sicherungsgeländer für Zone '{name}' gemäß ISO 15085 vorsehen.",
                "norm": f"ISO 15085:{norm_ref}",
            })
        else:
            # has_railing is None or key is missing
            warnings.append({
                "code": "ISO_15085_RAILING_DATA_MISSING",
                "severity": "info",
                "message": (
                    f"Zone '{name}': Reling-Eigenschaft nicht angegeben "
                    f"(ISO 15085:{norm_ref})."
                ),
                "suggestion": f"Reling-Status für Zone '{name}' in den Zoneneigenschaften hinterlegen.",
                "norm": f"ISO 15085:{norm_ref}",
            })

    if violations > 0:
        score = max(0.0, (1.0 - violations / total) * 100.0)
    elif compliant == 0:
        # Zu keiner Zone lag eine Reling-Angabe vor. Frueher 50.0 — eine Zahl,
        # die sich von einer gemessenen nicht unterscheiden liess.
        score = None
    else:
        score = 100.0

    return score, warnings, {"zones_checked": total, "zones_compliant": compliant}


# ---------------------------------------------------------------------------
# Sub-analysis: electrical access (ISO 10133 / ISO 13297)
# ---------------------------------------------------------------------------


def analyze_electrical_access(
    zones: list[dict],
    passages: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check electrical compartment accessibility and sizing per ISO 10133 / ISO 13297.

    Uses engine zones as proxy for the electrical compartment.
    Checks:
    1. Total engine zone area vs min_electrical_area_sqm.
    2. Engine zone reachable via passages (BFS connectivity > 1 node).

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []
    norm_ref_10133 = config.get("norm_versions", {}).get("ISO_10133", "2012")
    norm_ref_13297 = config.get("norm_versions", {}).get("ISO_13297", "2014")
    norm_label = f"ISO 10133:{norm_ref_10133} / ISO 13297:{norm_ref_13297}"

    engine_zones = [z for z in zones if z["zone_type"] == "engine"]

    if not engine_zones:
        warnings.append({
            "code": "ISO_10133_NO_ENGINE",
            "severity": "info",
            "message": "Kein Maschinenraum im Layout — Elektrische Zugänglichkeitsprüfung nicht durchführbar.",
            "suggestion": "Maschinenraum-Zone zum Layout hinzufügen.",
            "norm": norm_label,
        })
        # Frueher 50.0: eine Zahl fuer eine Pruefung, die nicht stattfand.
        return None, warnings, {"engine_area_sqm": 0.0, "accessible": False}

    min_area = config.get("min_electrical_area_sqm", 0.5)

    # --- Area check ---
    total_area = sum(_polygon_area_sqm(z.get("polygon") or []) for z in engine_zones)

    if total_area < min_area:
        area_score = (total_area / min_area) * 80.0 if min_area > 0 else 0.0
        warnings.append({
            "code": "ISO_10133_ELECTRICAL_AREA_TOO_SMALL",
            "severity": "warning",
            "message": (
                f"Elektrischer Zugangsbereich zu klein "
                f"({total_area:.2f} m², Minimum: {min_area:.2f} m², {norm_label})."
            ),
            "suggestion": f"Maschinenraum-/Elektrozugang auf mindestens {min_area:.2f} m² vergrößern.",
            "norm": norm_label,
        })
    else:
        area_score = 100.0

    # --- Accessibility check (BFS) ---
    graph = _build_adjacency(passages)
    engine_names = {z["name"] for z in engine_zones}

    accessible = False
    for eng_name in engine_names:
        reachable = _bfs_reachable(graph, eng_name)
        if len(reachable) > 1:
            accessible = True
            break

    if not accessible:
        access_score = 0.0
        warnings.append({
            "code": "ISO_10133_ELECTRICAL_INACCESSIBLE",
            "severity": "critical",
            "message": (
                f"Maschinenraum/Elektroanlage nicht über Durchgänge erreichbar "
                f"({norm_label})."
            ),
            "suggestion": "Zugang zum Maschinenraum über mindestens einen Durchgang sicherstellen.",
            "norm": norm_label,
        })
    else:
        access_score = 100.0

    # Enrich with electrical critical warnings from knowledge database
    if CRITICAL_WARNINGS:
        try:
            # Add warnings about typical marine electrical issues
            general_warnings = CRITICAL_WARNINGS.get("general_critical_issues", [])
            for crit_issue in general_warnings[:2]:  # Top 2 critical issues
                if isinstance(crit_issue, dict):
                    warnings.append({
                        "code": "ELECTRICAL_CRITICAL_RISK",
                        "severity": "warning",
                        "message": (
                            f"Marine-Elektroanlage: Kritisches Risiko — "
                            f"{crit_issue.get('description', '?')}"
                        ),
                        "suggestion": (
                            f"Elektroanlage gemäß ABYC E-11 und DIN 13297 überprüfen. "
                            f"{crit_issue.get('mitigation', '?')}"
                        ),
                    })
        except (KeyError, TypeError, AttributeError):
            pass

    combined_score = area_score * 0.5 + access_score * 0.5

    return combined_score, warnings, {
        "engine_area_sqm": round(total_area, 2),
        "accessible": accessible,
    }


# ---------------------------------------------------------------------------
# Sub-analysis: CE category compliance
# ---------------------------------------------------------------------------


def analyze_ce_category(
    zones: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check CE category zone requirements.

    Verifies that all zone types required for the target CE category are present
    in the layout.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    target_category = config.get("ce_category", "A")
    required = _CE_REQUIRED_ZONES.get(target_category, set())

    present = {z["zone_type"] for z in zones}
    missing = required - present

    for zone_type in sorted(missing):
        label = _CE_ZONE_LABELS.get(zone_type, zone_type)
        warnings.append({
            "code": "CE_CATEGORY_ZONE_MISSING",
            "severity": "warning",
            "message": (
                f"CE-Kategorie {target_category}: Zone '{label}' fehlt im Layout."
            ),
            "suggestion": f"Zone '{label}' zum Layout hinzufügen (CE-Kategorie {target_category}).",
        })

    if required:
        present_required = present & required
        score = (len(present_required) / len(required)) * 100.0
    else:
        score = 100.0

    return score, warnings, {
        "target_category": target_category,
        "required_zones": sorted(required),
        "missing_zones": sorted(missing),
    }


# ---------------------------------------------------------------------------
# Sub-analysis: escape hatch dimensions (ISO 12216)
# ---------------------------------------------------------------------------


_ESCAPE_HATCH_MIN_WIDTH_MM = 400
_ESCAPE_HATCH_MIN_HEIGHT_MM = 520


def analyze_escape_hatch_dimensions(
    zones: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check emergency escape hatch dimensions per ISO 12216.

    Cabins and crew quarters must have hatches of at least 400 mm × 520 mm.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []
    norm_ref = config.get("norm_versions", {}).get("ISO_12216", "2002")

    cabin_zones = [z for z in zones if z["zone_type"] in _SLEEPING_ZONE_TYPES]

    # Ohne erkannte Kabine gibt es keinen Notausstieg zu vermessen.
    if not cabin_zones:
        warnings.append({
            "code": "ESCAPE_HATCH_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                "Keine Kabinen im Layout gefunden — die Notausstiegsmaße nach "
                f"ISO {norm_ref} konnten nicht geprüft werden."
            ),
            "suggestion": (
                "Kabinen als Zonentyp cabin, aft_cabin, quarter_berth oder "
                "crew_quarters erfassen, damit die Notausstiege geprüft werden können."
            ),
            "location": "layout",
        })
        return None, warnings, {"cabins_checked": 0, "cabins_compliant": 0}

    total = 0
    compliant = 0
    has_data = False

    for z in cabin_zones:
        props = z.get("properties") or {}
        hatch_w = props.get("hatch_width_mm")
        hatch_h = props.get("hatch_height_mm")

        if hatch_w is None or hatch_h is None:
            continue

        has_data = True
        total += 1

        if hatch_w >= _ESCAPE_HATCH_MIN_WIDTH_MM and hatch_h >= _ESCAPE_HATCH_MIN_HEIGHT_MM:
            compliant += 1
        else:
            warnings.append({
                "code": "ISO_12216_HATCH_TOO_SMALL",
                "severity": "warning",
                "message": (
                    f"Notluke in Zone '{z['name']}' zu klein "
                    f"({hatch_w:.0f} × {hatch_h:.0f} mm, "
                    f"Minimum: {_ESCAPE_HATCH_MIN_WIDTH_MM} × {_ESCAPE_HATCH_MIN_HEIGHT_MM} mm, "
                    f"ISO 12216:{norm_ref})."
                ),
                "suggestion": (
                    f"Notluke in Zone '{z['name']}' auf mindestens "
                    f"{_ESCAPE_HATCH_MIN_WIDTH_MM} × {_ESCAPE_HATCH_MIN_HEIGHT_MM} mm vergrößern."
                ),
            })

    if not has_data:
        warnings.append({
            "code": "ISO_12216_NO_HATCH_DATA",
            "severity": "info",
            "message": "Keine Lukenmaße vorhanden.",
            "suggestion": "Lukenmaße (hatch_width_mm, hatch_height_mm) in den Zoneneigenschaften hinterlegen.",
        })
        # Frueher 50.0: eine Zahl fuer eine Pruefung, die nicht stattfand.
        return None, warnings, {"cabins_checked": 0, "cabins_compliant": 0}

    score = (compliant / total) * 100.0 if total > 0 else None

    return score, warnings, {
        "cabins_checked": total,
        "cabins_compliant": compliant,
    }


# ---------------------------------------------------------------------------
# Sub-analysis: cockpit drain capacity (ISO 11812)
# ---------------------------------------------------------------------------


def analyze_cockpit_drain_capacity(
    zones: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check cockpit drain capacity per ISO 11812.

    Cockpit drains must handle cockpit volume × 2 in liters per second.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []
    norm_ref = config.get("norm_versions", {}).get("ISO_11812", "2001")

    cockpit_zones = [z for z in zones if z["zone_type"] == "cockpit"]

    # Ohne erfasstes Cockpit gibt es keine Lenzleistung zu berechnen.
    if not cockpit_zones:
        warnings.append({
            "code": "COCKPIT_DRAIN_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                "Kein Cockpit im Layout gefunden — die Lenzleistung nach "
                f"ISO {norm_ref} konnte nicht geprüft werden."
            ),
            "suggestion": (
                "Cockpit als Zonentyp cockpit erfassen, damit die erforderliche "
                "Lenzleistung berechnet werden kann."
            ),
            "location": "layout",
        })
        return None, warnings, {"cockpits_checked": 0, "cockpits_compliant": 0}

    default_depth_mm = config.get("cockpit_depth_mm", 300)
    total = 0
    compliant = 0
    has_data = False

    for z in cockpit_zones:
        props = z.get("properties") or {}
        area_sqm = _polygon_area_sqm(z.get("polygon") or [])
        if area_sqm <= 0:
            continue

        depth_mm = props.get("cockpit_depth_mm", default_depth_mm)
        cockpit_volume_liters = area_sqm * depth_mm / 1000.0 * 1000.0
        required_drain_capacity = cockpit_volume_liters * 2.0

        drain_capacity = props.get("drain_capacity_lps")
        if drain_capacity is None:
            continue

        has_data = True
        total += 1

        if drain_capacity >= required_drain_capacity:
            compliant += 1
        else:
            ratio = drain_capacity / required_drain_capacity if required_drain_capacity > 0 else 0.0
            warnings.append({
                "code": "ISO_11812_DRAIN_INSUFFICIENT",
                "severity": "warning",
                "message": (
                    f"Cockpit '{z['name']}': Abflusskapazität {drain_capacity:.1f} l/s "
                    f"unzureichend (benötigt: {required_drain_capacity:.1f} l/s, "
                    f"ISO 11812:{norm_ref})."
                ),
                "suggestion": (
                    f"Abflusskapazität für Cockpit '{z['name']}' auf mindestens "
                    f"{required_drain_capacity:.1f} l/s erhöhen."
                ),
            })

    if not has_data:
        warnings.append({
            "code": "ISO_11812_NO_DRAIN_DATA",
            "severity": "info",
            "message": "Keine Abflussdaten vorhanden.",
            "suggestion": "Abflusskapazität (drain_capacity_lps) in den Cockpit-Zoneneigenschaften hinterlegen.",
        })
        # Frueher 50.0: eine Zahl fuer eine Pruefung, die nicht stattfand.
        return None, warnings, {"cockpits_checked": 0, "cockpits_compliant": 0}

    if total > 0:
        score = (compliant / total) * 100.0
    else:
        score = None

    return score, warnings, {
        "cockpits_checked": total,
        "cockpits_compliant": compliant,
    }


# ---------------------------------------------------------------------------
# Sub-analysis: companionway sill height (CE category)
# ---------------------------------------------------------------------------


_CE_SILL_HEIGHT_MM = {
    "A": 300,
    "B": 250,
    "C": 150,
    "D": 0,
}

_INTERIOR_ZONE_TYPES = {"salon", "cabin", "pantry"}


def analyze_companionway_sill(
    zones: list[dict],
    passages: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check companionway sill heights based on CE category.

    Sill heights at cockpit-to-interior passages must meet CE category minimums.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    ce_category = config.get("ce_category", "A")
    min_sill = config.get("companionway_sill_mm", _CE_SILL_HEIGHT_MM.get(ce_category, 300))

    # Fuer Entwurfskategorie D gibt es keine Suellhoehe. Die Pruefung entfaellt
    # damit — sie gilt aber nicht als bestanden. Frueher floss hier eine 100 in
    # die Modulnote ein, was Kategorie-D-Boote gegenueber Kategorie A ohne
    # sachlichen Grund besser aussehen liess.
    if min_sill <= 0:
        warnings.append({
            "code": "SILL_NOT_APPLICABLE",
            "severity": "info",
            "message": (
                f"Entwurfskategorie {ce_category} sieht keine Mindestsüllhöhe vor — "
                "die Prüfung entfällt."
            ),
            "suggestion": (
                "Keine Maßnahme erforderlich. Bei geplantem Einsatz in einer "
                "höheren Entwurfskategorie die Süllhöhe entsprechend vorsehen."
            ),
            "location": "layout",
        })
        return None, warnings, {"sills_checked": 0, "sills_compliant": 0}

    zone_type_map = {z["name"]: z["zone_type"] for z in zones}
    cockpit_names = {z["name"] for z in zones if z["zone_type"] == "cockpit"}
    interior_names = {z["name"] for z in zones if z["zone_type"] in _INTERIOR_ZONE_TYPES}

    # Find passages from cockpit to interior zones
    companionway_passages = []
    for p in passages:
        from_z, to_z = p["from_zone"], p["to_zone"]
        if (from_z in cockpit_names and to_z in interior_names) or \
           (to_z in cockpit_names and from_z in interior_names):
            companionway_passages.append(p)

    # Kein Niedergang zwischen Cockpit und Innenraum auffindbar — es gibt keine
    # Suelle zu messen. Volle Punktzahl waere eine Aussage ueber etwas, das gar
    # nicht gefunden wurde.
    if not companionway_passages:
        warnings.append({
            "code": "SILL_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                "Kein Niedergang zwischen Cockpit und Innenraum gefunden — die "
                f"Süllhöhe für Entwurfskategorie {ce_category} konnte nicht geprüft werden."
            ),
            "suggestion": (
                "Durchgang zwischen Cockpit und Innenraum im Layout anlegen, damit "
                "die Süllhöhe geprüft werden kann."
            ),
            "location": "layout",
        })
        return None, warnings, {"sills_checked": 0, "sills_compliant": 0}

    total = 0
    compliant = 0
    has_data = False

    for p in companionway_passages:
        props = p.get("properties") or {}
        sill_height = props.get("sill_height_mm")

        if sill_height is None:
            continue

        has_data = True
        total += 1

        if sill_height >= min_sill:
            compliant += 1
        else:
            warnings.append({
                "code": "CE_COMPANIONWAY_SILL_LOW",
                "severity": "warning",
                "message": (
                    f"Niedergang '{p['from_zone']} → {p['to_zone']}': "
                    f"Süllhöhe {sill_height:.0f} mm unter Minimum {min_sill:.0f} mm "
                    f"(CE-Kategorie {ce_category})."
                ),
                "suggestion": (
                    f"Süllhöhe des Niedergangs '{p['from_zone']} → {p['to_zone']}' "
                    f"auf mindestens {min_sill:.0f} mm erhöhen."
                ),
            })

    if not has_data:
        warnings.append({
            "code": "CE_NO_SILL_DATA",
            "severity": "info",
            "message": "Keine Süllhöhen-Daten vorhanden.",
            "suggestion": "Süllhöhen (sill_height_mm) in den Durchgangseigenschaften hinterlegen.",
        })
        # Frueher 50.0: eine Zahl fuer eine Pruefung, die nicht stattfand.
        return None, warnings, {"sills_checked": 0, "sills_compliant": 0}

    score = (compliant / total) * 100.0 if total > 0 else None

    return score, warnings, {
        "sills_checked": total,
        "sills_compliant": compliant,
    }


# ---------------------------------------------------------------------------
# Sub-analysis: ventilation requirements
# ---------------------------------------------------------------------------


def analyze_ventilation(
    zones: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check engine room and battery compartment ventilation requirements.

    Engine rooms need ventilation area proportional to engine power.
    Battery compartments need minimum 0.02 m² ventilation.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    engine_zones = [z for z in zones if z["zone_type"] == "engine"]
    battery_zones = [z for z in zones if (z.get("properties") or {}).get("has_battery", False)]

    zones_to_check = []
    zonen_ohne_leistungsangabe: list[str] = []

    for z in engine_zones:
        props = z.get("properties") or {}
        # Fruehere Fassung: props.get("engine_kw", 50). Fehlte die Angabe, rechnete
        # die Pruefung mit 50 kW weiter, als sei die Leistung bekannt. Bei 50 kW
        # greift der Sockelwert 0,05 m² — die Anforderung wurde also fuer jede
        # groessere Maschine zu niedrig angesetzt und das Ergebnis sah bestanden
        # aus. Ohne Angabe wird jetzt nur noch gegen den Sockelwert geprueft, und
        # das steht als Einschraenkung im Befund.
        engine_kw = props.get("engine_kw")
        if engine_kw is None:
            required = 0.05
            zonen_ohne_leistungsangabe.append(z["name"])
        else:
            required = max(0.05, engine_kw * 0.0003)
        zones_to_check.append((z, required, "Maschinenraum"))

    if zonen_ohne_leistungsangabe:
        warnings.append({
            "code": "VENTILATION_ENGINE_POWER_UNKNOWN",
            "severity": "warning",
            "message": (
                "Motorleistung nicht angegeben für: "
                + ", ".join(zonen_ohne_leistungsangabe)
                + ". Geprüft wurde nur gegen den Sockelwert 0,050 m²; die "
                "leistungsabhängige Anforderung konnte nicht ermittelt werden."
            ),
            "suggestion": (
                "Motorleistung (properties.engine_kw) je Maschinenraum erfassen. "
                "Erforderlich sind max(0,05; kW × 0,0003) m²."
            ),
            "location": "layout",
        })

    for z in battery_zones:
        if z["zone_type"] != "engine":  # avoid double-checking engine zones with batteries
            zones_to_check.append((z, 0.02, "Batterieraum"))
        else:
            # Engine zone with battery — already checked above, but add battery requirement
            for i, (existing_z, req, label) in enumerate(zones_to_check):
                if existing_z["name"] == z["name"]:
                    zones_to_check[i] = (existing_z, max(req, 0.02), label)
                    break

    # Weder Maschinenraum noch Batterieraum auffindbar. Es wurde nichts geprueft.
    if not zones_to_check:
        warnings.append({
            "code": "VENTILATION_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                "Kein Maschinen- oder Batterieraum im Layout gefunden — die "
                "Belüftungsprüfung konnte nicht durchgeführt werden."
            ),
            "suggestion": (
                "Maschinenraum als Zonentyp engine erfassen bzw. "
                "properties.has_battery bei Batterieräumen setzen."
            ),
            "location": "layout",
        })
        return None, warnings, {"zones_checked": 0, "zones_compliant": 0}

    total = 0
    compliant = 0
    has_data = False

    for z, required_area, label in zones_to_check:
        props = z.get("properties") or {}
        vent_area = props.get("ventilation_area_sqm")

        if vent_area is None:
            continue

        has_data = True
        total += 1

        if vent_area >= required_area:
            compliant += 1
        else:
            warnings.append({
                "code": "VENTILATION_INSUFFICIENT",
                "severity": "warning",
                "message": (
                    f"{label} '{z['name']}': Belüftungsfläche {vent_area:.3f} m² "
                    f"unter Minimum {required_area:.3f} m²."
                ),
                "suggestion": (
                    f"Belüftungsfläche für '{z['name']}' auf mindestens "
                    f"{required_area:.3f} m² erhöhen."
                ),
            })

    if not has_data:
        warnings.append({
            "code": "VENTILATION_NO_DATA",
            "severity": "info",
            "message": (
                "Keine Belüftungsdaten vorhanden — die Belüftungsflächen konnten "
                "nicht mit der Anforderung verglichen werden."
            ),
            "suggestion": "Belüftungsfläche (ventilation_area_sqm) in den Zoneneigenschaften hinterlegen.",
            "location": "layout",
        })
        # Frueher 50.0 — eine Zahl fuer eine Pruefung, die nicht stattgefunden hat.
        return None, warnings, {"zones_checked": 0, "zones_compliant": 0}

    score = (compliant / total) * 100.0 if total > 0 else None

    return score, warnings, {
        "zones_checked": total,
        "zones_compliant": compliant,
    }


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


def run_compliance_analysis(
    zones: list[dict],
    passages: list[dict],
    boat_class: str,
    config_overrides: dict | None = None,
    data_source: str = "measured",
) -> dict:
    """Orchestrator — runs all compliance sub-analyses.

    Returns a standardized result dict matching the AYDI analysis module contract.
    """
    # Ein Layout ohne Zonen ist kein Layout. Ohne diese Pruefung lieferten die
    # Teilanalysen ihre jeweiligen Vorgabewerte zurueck, und daraus entstand ein
    # Gesamtwert, der wie ein Befund aussah — die Konformitaetspruefung meldete
    # fuer ein leeres Layout volle Punktzahl bei Fluchtwegen, Notausstieg,
    # Reling und Cockpitlenzung. Das ist die gefaehrlichste Form einer falschen
    # Auskunft: eine Freigabe fuer etwas, das nie geprueft wurde.
    if not isinstance(zones, list) or len(zones) == 0:
        return {
            "module": "compliance",
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

    sub_scores: dict[str, float | None] = {}
    all_warnings: list[dict] = []
    all_suggestions: list[str] = []
    all_metrics: dict[str, dict] = {}

    analyses: list[tuple[str, object]] = [
        ("escape_routes", lambda: analyze_escape_routes(zones, passages, config)),
        ("fire_safety", lambda: analyze_fire_safety(zones, passages, config)),
        ("stability", lambda: analyze_stability_impact(zones, config)),
        ("railing", lambda: analyze_railing_requirements(zones, config)),
        ("electrical_access", lambda: analyze_electrical_access(zones, passages, config)),
        ("ce_category", lambda: analyze_ce_category(zones, config)),
        ("escape_hatch", lambda: analyze_escape_hatch_dimensions(zones, config)),
        ("cockpit_drain", lambda: analyze_cockpit_drain_capacity(zones, config)),
        ("companionway_sill", lambda: analyze_companionway_sill(zones, passages, config)),
        ("ventilation", lambda: analyze_ventilation(zones, config)),
    ]

    for name, fn in analyses:
        try:
            score, warnings, metrics = fn()
            sub_scores[name] = score
            all_warnings.extend(warnings)
            all_metrics[name] = metrics
        except Exception:
            logger.exception("Error in compliance sub-analysis %s", name)
            sub_scores[name] = 0.0
            all_warnings.append({
                "code": "ANALYSIS_ERROR",
                "severity": "critical",
                "message": f"Fehler bei Compliance-Analyse: {name}",
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
            "module": "compliance",
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
        "module": "compliance",
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
