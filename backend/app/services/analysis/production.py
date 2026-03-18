"""Production friendliness analysis module for yacht layouts.

Pure function module — no database access. Receives data as parameters,
returns analysis results as dicts. Evaluates manufacturing efficiency:
assembly sequence, form complexity, service access, standardization,
and cable/pipe routing.
"""
import logging
import math
from collections import deque

logger = logging.getLogger(__name__)

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "min_sharp_angle_deg": 30,
        "min_service_access_mm": 500,
        "standard_door_widths_mm": [600],
        "standard_berth_width_mm": 700,
        "standardization_tolerance_mm": 50,
        "weights": {
            "assembly_sequence": 0.15,
            "form_complexity": 0.30,
            "service_access": 0.20,
            "standardization": 0.25,
            "cable_routing": 0.10,
        },
    },
    "cruising_sail": {
        "min_sharp_angle_deg": 30,
        "min_service_access_mm": 600,
        "standard_door_widths_mm": [600, 700],
        "standard_berth_width_mm": 700,
        "standardization_tolerance_mm": 50,
        "weights": {
            "assembly_sequence": 0.20,
            "form_complexity": 0.25,
            "service_access": 0.20,
            "standardization": 0.20,
            "cable_routing": 0.15,
        },
    },
    "large_motor": {
        "min_sharp_angle_deg": 35,
        "min_service_access_mm": 700,
        "standard_door_widths_mm": [600, 700, 800],
        "standard_berth_width_mm": 800,
        "standardization_tolerance_mm": 50,
        "weights": {
            "assembly_sequence": 0.25,
            "form_complexity": 0.15,
            "service_access": 0.25,
            "standardization": 0.15,
            "cable_routing": 0.20,
        },
    },
    "superyacht": {
        "min_sharp_angle_deg": 40,
        "min_service_access_mm": 800,
        "standard_door_widths_mm": [700, 800, 900],
        "standard_berth_width_mm": 900,
        "standardization_tolerance_mm": 75,
        "weights": {
            "assembly_sequence": 0.25,
            "form_complexity": 0.10,
            "service_access": 0.25,
            "standardization": 0.10,
            "cable_routing": 0.30,
        },
    },
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}

_TECHNICAL_ZONE_TYPES = {"engine", "head"}
_GUEST_ZONE_TYPES = {"salon", "cabin"}
_SYSTEM_CONNECTIONS = [
    ("engine", "helm"),
    ("engine", "pantry"),
    ("engine", "head"),
]


# ---------------------------------------------------------------------------
# Graph helpers
# ---------------------------------------------------------------------------

def _build_adjacency(passages: list[dict]) -> dict[str, set[str]]:
    """Build undirected adjacency graph from passage list."""
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


def _bfs_path(graph: dict[str, set[str]], start: str, targets: set[str]) -> list[str] | None:
    """Return shortest path from start to any node in targets, or None."""
    if start in targets:
        return [start]
    if start not in graph:
        return None
    visited = {start}
    queue = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                if neighbor in targets:
                    return path + [neighbor]
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None


def _is_graph_connected(graph: dict[str, set[str]], nodes: set[str]) -> bool:
    """Return True if all nodes are reachable from any single node in the graph."""
    if not nodes:
        return True
    start = next(iter(nodes))
    reachable = _bfs_reachable(graph, start)
    return nodes.issubset(reachable)


# ---------------------------------------------------------------------------
# Geometry helpers
# ---------------------------------------------------------------------------

def _polygon_min_dimension(polygon: list[list[float]]) -> float:
    """Return the minimum bounding-box dimension of a polygon (width or height)."""
    if not polygon:
        return 0.0
    xs = [p[0] for p in polygon]
    ys = [p[1] for p in polygon]
    return min(max(xs) - min(xs), max(ys) - min(ys))


def _vertex_angles(polygon: list[list[float]]) -> list[tuple[float, bool]]:
    """Compute interior angles for a CCW polygon.

    Returns a list of (angle_deg, is_reflex) tuples.
    For CCW polygons, cross > 0 means a reflex vertex (interior angle > 180°).
    """
    n = len(polygon)
    if n < 3:
        return []
    results = []
    for i in range(n):
        p_prev = polygon[(i - 1) % n]
        p_curr = polygon[i]
        p_next = polygon[(i + 1) % n]
        ax = p_prev[0] - p_curr[0]
        ay = p_prev[1] - p_curr[1]
        bx = p_next[0] - p_curr[0]
        by = p_next[1] - p_curr[1]
        cross = ax * by - ay * bx
        dot = ax * bx + ay * by
        angle_rad = math.atan2(abs(cross), dot)
        angle_deg = math.degrees(angle_rad)
        # For CCW polygon, cross > 0 means reflex vertex (interior angle > 180)
        is_reflex = cross > 0
        if is_reflex:
            angle_deg = 360.0 - angle_deg
        results.append((angle_deg, is_reflex))
    return results


# ---------------------------------------------------------------------------
# Sub-analysis 1: Assembly Sequence
# ---------------------------------------------------------------------------

def analyze_assembly_sequence(
    zones: list[dict],
    passages: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Detect bottleneck zones (articulation points) by brute-force removal.

    For each zone, remove it from the graph and check whether the remaining
    connected nodes stay fully reachable. Score = 100 * (1 - bottlenecks/total).

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "code": "MONTAGE_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen definiert — Montagereihenfolge kann nicht bewertet werden.",
            "suggestion": "Zonen zum Layout hinzufügen.",
        })
        return 50.0, warnings, {"bottleneck_count": 0, "total_zones": 0, "bottleneck_zones": []}

    if len(zones) == 1:
        return 100.0, warnings, {"bottleneck_count": 0, "total_zones": 1, "bottleneck_zones": []}

    # Build adjacency using all zone names as the node set
    zone_names = {z["name"] for z in zones}
    graph = _build_adjacency(passages)

    # Zones involved in at least one passage
    connected_names = set()
    for p in passages:
        connected_names.add(p["from_zone"])
        connected_names.add(p["to_zone"])

    if not connected_names or len(connected_names) < 2:
        warnings.append({
            "code": "MONTAGE_NO_CONNECTIONS",
            "severity": "critical",
            "message": "Keine Verbindungen zwischen Zonen — Montagereihenfolge nicht beurteilbar.",
            "suggestion": "Durchgänge zwischen allen Zonen definieren.",
        })
        return 0.0, warnings, {"bottleneck_count": 0, "total_zones": len(zones), "bottleneck_zones": []}

    # Detect articulation points: zones whose removal disconnects the graph
    bottleneck_zones: list[str] = []
    for zone in zones:
        name = zone["name"]
        if name not in graph:
            # Isolated zone — not an articulation point
            continue
        # Build reduced graph without this node
        reduced: dict[str, set[str]] = {}
        for node, neighbors in graph.items():
            if node == name:
                continue
            reduced[node] = {n for n in neighbors if n != name}

        remaining_connected = {n for n in connected_names if n != name}
        if len(remaining_connected) < 2:
            # Only 1 or 0 nodes remain — trivially connected
            continue

        start = next(iter(remaining_connected))
        reachable = _bfs_reachable(reduced, start)
        if not remaining_connected.issubset(reachable):
            bottleneck_zones.append(name)
            warnings.append({
                "code": "MONTAGE_BOTTLENECK",
                "severity": "warning",
                "message": (
                    f"Zone '{name}' ist ein Engpass in der Montagereihenfolge — "
                    f"Entfernung trennt das Layout."
                ),
                "suggestion": (
                    f"Alternative Verbindungen zu Zone '{name}' herstellen, "
                    f"um Montageflexibilität zu erhöhen."
                ),
            })

    total = len(zones)
    score = 100.0 * (1.0 - len(bottleneck_zones) / total)
    score = max(0.0, min(100.0, score))

    return score, warnings, {
        "bottleneck_count": len(bottleneck_zones),
        "total_zones": total,
        "bottleneck_zones": bottleneck_zones,
    }


# ---------------------------------------------------------------------------
# Sub-analysis 2: Form Complexity
# ---------------------------------------------------------------------------

def analyze_form_complexity(
    zones: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Evaluate GFK lamination difficulty from polygon vertex angles.

    Per zone: score starts at 100, deduct 15 per sharp angle and 20 per reflex
    angle (undercut), clamped to 0. Final score is the average across zones.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []
    min_angle = config["min_sharp_angle_deg"]

    if not zones:
        warnings.append({
            "code": "FORM_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen definiert — Formkomplexität kann nicht bewertet werden.",
            "suggestion": "Zonen zum Layout hinzufügen.",
        })
        return 50.0, warnings, {"total_sharp_angles": 0, "total_reflex_angles": 0, "zones_evaluated": 0}

    zone_scores: list[float] = []
    total_sharp = 0
    total_reflex = 0

    for zone in zones:
        polygon = zone.get("polygon", [])
        angles = _vertex_angles(polygon)
        sharp_count = 0
        reflex_count = 0

        for angle_deg, is_reflex in angles:
            if is_reflex:
                reflex_count += 1
                warnings.append({
                    "code": "FORM_UNDERCUT",
                    "severity": "warning",
                    "message": (
                        f"Zone '{zone['name']}' hat einen Hinterschnitt (Reflexwinkel "
                        f"{angle_deg:.1f}°) — erschwert GFK-Laminierung."
                    ),
                    "suggestion": (
                        f"Hinterschnitt in Zone '{zone['name']}' vermeiden oder "
                        f"als separate Zone aufteilen."
                    ),
                })
            elif angle_deg < min_angle:
                sharp_count += 1
                warnings.append({
                    "code": "FORM_SHARP_ANGLE",
                    "severity": "warning",
                    "message": (
                        f"Zone '{zone['name']}' hat einen spitzen Winkel "
                        f"({angle_deg:.1f}° < {min_angle}°) — schwierig zu laminieren."
                    ),
                    "suggestion": (
                        f"Spitzen Winkel in Zone '{zone['name']}' auf mindestens "
                        f"{min_angle}° abrunden."
                    ),
                })

        zone_score = 100.0 - sharp_count * 15.0 - reflex_count * 20.0
        zone_score = max(0.0, zone_score)
        zone_scores.append(zone_score)

        total_sharp += sharp_count
        total_reflex += reflex_count

    score = sum(zone_scores) / len(zone_scores) if zone_scores else 50.0
    score = max(0.0, min(100.0, score))

    return score, warnings, {
        "total_sharp_angles": total_sharp,
        "total_reflex_angles": total_reflex,
        "zones_evaluated": len(zones),
    }


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------

def run_production_analysis(
    zones: list[dict],
    passages: list[dict],
    boat_class: str,
    config_overrides: dict | None = None,
) -> dict:
    """Run all production friendliness sub-analyses and return combined result.

    Args:
        zones: List of zone dicts (ZoneInput format).
        passages: List of passage dicts (PassageInput format).
        boat_class: One of small_sail, cruising_sail, large_motor, superyacht.
        config_overrides: Optional dict to override individual config values.

    Returns:
        Standardised analysis result dict.
    """
    if boat_class not in BOAT_CLASS_DEFAULTS:
        raise ValueError(f"Unbekannte Bootsklasse: {boat_class}")

    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    weights = config.pop("weights").copy()

    if config_overrides:
        config.update(config_overrides)

    sub_scores: dict[str, float] = {}
    all_warnings: list[dict] = []
    all_suggestions: list[str] = []
    all_metrics: dict[str, dict] = {}

    analyses = [
        ("assembly_sequence", lambda: analyze_assembly_sequence(zones, passages, config)),
        ("form_complexity", lambda: analyze_form_complexity(zones, config)),
    ]

    for name, fn in analyses:
        try:
            score, warnings, metrics = fn()
            sub_scores[name] = score
            all_warnings.extend(warnings)
            all_metrics[name] = metrics
        except Exception:
            logger.exception("Fehler in Teilanalyse %s", name)
            sub_scores[name] = 0.0
            all_warnings.append({
                "code": "PRODUCTION_ANALYSIS_ERROR",
                "severity": "critical",
                "message": f"Fehler bei der Analyse: {name}",
                "suggestion": "Layoutdaten überprüfen.",
            })

    # Remaining sub-analyses not yet implemented — placeholder scores
    for placeholder in ("service_access", "standardization", "cable_routing"):
        sub_scores[placeholder] = 50.0

    overall = sum(sub_scores.get(k, 0.0) * w for k, w in weights.items())

    for w in all_warnings:
        suggestion = w.get("suggestion")
        if suggestion and suggestion not in all_suggestions:
            all_suggestions.append(suggestion)

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    return {
        "module": "production",
        "overall_score": round(overall, 1),
        "sub_scores": {k: round(v, 1) for k, v in sub_scores.items()},
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
    }
