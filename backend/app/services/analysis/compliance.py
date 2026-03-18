"""Compliance checker module for yacht layouts.

Automated check against maritime safety norms (ISO 9094, ISO 12217,
ISO 15085, ISO 10133, ISO 13297). Pure function module — no database access.
All user-facing strings are in German.
"""
import logging
import math
from collections import deque

logger = logging.getLogger(__name__)

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 4,
        "min_engine_clearance_mm": 500,
        "min_engine_area_sqm": 0.8,
        "min_electrical_area_sqm": 0.3,
        "required_railing_zones": ["foredeck", "cockpit"],
        "ce_category": "C",
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
        },
        "weights": {
            "escape_routes": 0.30,
            "fire_safety": 0.20,
            "stability": 0.15,
            "railing": 0.10,
            "electrical_access": 0.10,
            "ce_category": 0.15,
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
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
        },
        "weights": {
            "escape_routes": 0.25,
            "fire_safety": 0.20,
            "stability": 0.20,
            "railing": 0.10,
            "electrical_access": 0.10,
            "ce_category": 0.15,
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
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
        },
        "weights": {
            "escape_routes": 0.25,
            "fire_safety": 0.25,
            "stability": 0.10,
            "railing": 0.15,
            "electrical_access": 0.10,
            "ce_category": 0.15,
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
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
        },
        "weights": {
            "escape_routes": 0.20,
            "fire_safety": 0.25,
            "stability": 0.10,
            "railing": 0.20,
            "electrical_access": 0.10,
            "ce_category": 0.15,
        },
    },
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}

_SLEEPING_ZONE_TYPES = {"cabin", "crew_quarters"}
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

    # No sleeping zones — nothing to check
    if not sleeping_zones:
        warnings.append({
            "code": "NO_SLEEPING_ZONES",
            "severity": "info",
            "message": "Keine Schlafbereiche im Layout — Fluchtwegprüfung nicht erforderlich.",
            "suggestion": "Fluchtwegprüfung entfällt bei fehlendem Schlafbereich.",
        })
        return 100.0, warnings, {"cabins_checked": 0, "cabins_compliant": 0, "cabins_total": 0}

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

    if not engine_zones:
        warnings.append({
            "code": "ISO_9094_NO_ENGINE",
            "severity": "info",
            "message": "Kein Maschinenraum im Layout — Brandschutzprüfung nicht vollständig durchführbar.",
            "suggestion": "Maschinenraum-Zone zum Layout hinzufügen.",
        })
        return 50.0, warnings, {
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
        # No living zones to compare against
        clearance_score = 100.0
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

    if not engine_accessible and other_zone_names:
        access_score = 0.0
        warnings.append({
            "code": "ISO_9094_ENGINE_INACCESSIBLE",
            "severity": "critical",
            "message": "Maschinenraum nicht über Durchgänge erreichbar (ISO 9094 Brandschutz).",
            "suggestion": "Zugang zum Maschinenraum über mindestens einen Durchgang sicherstellen.",
        })
    else:
        access_score = 100.0

    combined_score = clearance_score * 0.5 + access_score * 0.5

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
        return 50.0, warnings, {"heavy_zones": 0, "y_deviation_ratio": 0.0}

    # Compute layout Y-center from bounding box of ALL zones
    all_y: list[float] = []
    for z in zones:
        poly = z.get("polygon") or []
        for pt in poly:
            if len(pt) >= 2:
                all_y.append(pt[1])

    if not all_y:
        return 50.0, warnings, {"heavy_zones": len(heavy_zones), "y_deviation_ratio": 0.0}

    y_min = min(all_y)
    y_max = max(all_y)
    half_beam = (y_max - y_min) / 2.0

    if half_beam == 0:
        return 50.0, warnings, {"heavy_zones": len(heavy_zones), "y_deviation_ratio": 0.0}

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

    if not required_zones:
        return 100.0, warnings, {"zones_checked": 0, "zones_compliant": 0}

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
        # Only info warnings (missing data) — uncertain, penalize partially
        score = 50.0
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
        return 50.0, warnings, {"engine_area_sqm": 0.0, "accessible": False}

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

    combined_score = area_score * 0.5 + access_score * 0.5

    return combined_score, warnings, {
        "engine_area_sqm": round(total_area, 2),
        "accessible": accessible,
    }


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


def run_compliance_analysis(
    zones: list[dict],
    passages: list[dict],
    boat_class: str,
    config_overrides: dict | None = None,
) -> dict:
    """Orchestrator — runs all compliance sub-analyses.

    Returns a standardized result dict matching the AYDI analysis module contract.
    """
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

    analyses: list[tuple[str, object]] = [
        ("escape_routes", lambda: analyze_escape_routes(zones, passages, config)),
        ("fire_safety", lambda: analyze_fire_safety(zones, passages, config)),
        # Future sub-analyses: stability, railing, electrical_access, ce_category
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

    # Placeholder scores for not-yet-implemented sub-analyses
    for key in weights:
        if key not in sub_scores:
            sub_scores[key] = 50.0

    overall = sum(sub_scores.get(k, 50.0) * w for k, w in weights.items())

    for w in all_warnings:
        suggestion = w.get("suggestion")
        if suggestion and suggestion not in all_suggestions:
            all_suggestions.append(suggestion)

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    return {
        "module": "compliance",
        "overall_score": round(overall, 1),
        "sub_scores": {k: round(v, 1) for k, v in sub_scores.items()},
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
    }
