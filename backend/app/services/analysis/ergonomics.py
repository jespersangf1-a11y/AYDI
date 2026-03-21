"""Ergonomics analysis module for yacht layouts.

Pure function module — no database access. Receives data as parameters,
returns analysis results as dicts.
"""
import logging
import math
from collections import deque

logger = logging.getLogger(__name__)

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "min_passage_width_mm": 600,
        "critical_passage_width_mm": 450,
        "max_steps_cockpit_pantry": 8,
        "min_helm_area_sqm": 1.5,
        "min_helm_visibility_deg": 225,
        "crew_guest_separation": False,
        "heel_angle_deg": 20,
        "weights": {
            "passage_width": 0.23,
            "path_efficiency": 0.15,
            "crew_guest_separation": 0.04,
            "accessibility": 0.22,
            "helm_ergonomics": 0.11,
            "heel_impact": 0.10,
            "morning_circulation": 0.08,
            "access_complexity": 0.07,
        },
    },
    "cruising_sail": {
        "min_passage_width_mm": 650,
        "critical_passage_width_mm": 500,
        "max_steps_cockpit_pantry": 10,
        "min_helm_area_sqm": 2.0,
        "min_helm_visibility_deg": 225,
        "crew_guest_separation": False,
        "heel_angle_deg": 20,
        "weights": {
            "passage_width": 0.19,
            "path_efficiency": 0.15,
            "crew_guest_separation": 0.08,
            "accessibility": 0.19,
            "helm_ergonomics": 0.14,
            "heel_impact": 0.10,
            "morning_circulation": 0.08,
            "access_complexity": 0.07,
        },
    },
    "large_motor": {
        "min_passage_width_mm": 750,
        "critical_passage_width_mm": 550,
        "max_steps_cockpit_pantry": 12,
        "min_helm_area_sqm": 3.0,
        "min_helm_visibility_deg": 240,
        "crew_guest_separation": True,
        "heel_angle_deg": 0,
        "weights": {
            "passage_width": 0.17,
            "path_efficiency": 0.17,
            "crew_guest_separation": 0.21,
            "accessibility": 0.17,
            "helm_ergonomics": 0.13,
            "heel_impact": 0.0,
            "morning_circulation": 0.08,
            "access_complexity": 0.07,
        },
    },
    "racing_sail": {
        "min_passage_width_mm": 500,
        "critical_passage_width_mm": 400,
        "max_steps_cockpit_pantry": 5,
        "min_helm_area_sqm": 1.5,
        "min_helm_visibility_deg": 240,
        "crew_guest_separation": False,
        "heel_angle_deg": 25,
        "weights": {
            "passage_width": 0.25,
            "path_efficiency": 0.13,
            "crew_guest_separation": 0.02,
            "accessibility": 0.20,
            "helm_ergonomics": 0.15,
            "heel_impact": 0.15,
            "morning_circulation": 0.05,
            "access_complexity": 0.05,
        },
    },
    "daysailer": {
        "min_passage_width_mm": 550,
        "critical_passage_width_mm": 450,
        "max_steps_cockpit_pantry": 6,
        "min_helm_area_sqm": 1.5,
        "min_helm_visibility_deg": 225,
        "crew_guest_separation": False,
        "heel_angle_deg": 20,
        "weights": {
            "passage_width": 0.22,
            "path_efficiency": 0.14,
            "crew_guest_separation": 0.04,
            "accessibility": 0.21,
            "helm_ergonomics": 0.13,
            "heel_impact": 0.10,
            "morning_circulation": 0.08,
            "access_complexity": 0.08,
        },
    },
    "motorsailer": {
        "min_passage_width_mm": 650,
        "critical_passage_width_mm": 500,
        "max_steps_cockpit_pantry": 9,
        "min_helm_area_sqm": 2.5,
        "min_helm_visibility_deg": 230,
        "crew_guest_separation": False,
        "heel_angle_deg": 15,
        "weights": {
            "passage_width": 0.1979,
            "path_efficiency": 0.1563,
            "crew_guest_separation": 0.0625,
            "accessibility": 0.1979,
            "helm_ergonomics": 0.1458,
            "heel_impact": 0.0833,
            "morning_circulation": 0.0833,
            "access_complexity": 0.0729,
        },
    },
    "catamaran_sail": {
        "min_passage_width_mm": 600,
        "critical_passage_width_mm": 480,
        "max_steps_cockpit_pantry": 8,
        "min_helm_area_sqm": 2.5,
        "min_helm_visibility_deg": 235,
        "crew_guest_separation": False,
        "heel_angle_deg": 15,
        "weights": {
            "passage_width": 0.2083,
            "path_efficiency": 0.1563,
            "crew_guest_separation": 0.0521,
            "accessibility": 0.2083,
            "helm_ergonomics": 0.1354,
            "heel_impact": 0.0833,
            "morning_circulation": 0.0833,
            "access_complexity": 0.0729,
        },
    },
    "catamaran_motor": {
        "min_passage_width_mm": 650,
        "critical_passage_width_mm": 500,
        "max_steps_cockpit_pantry": 10,
        "min_helm_area_sqm": 2.5,
        "min_helm_visibility_deg": 240,
        "crew_guest_separation": False,
        "heel_angle_deg": 0,
        "weights": {
            "passage_width": 0.2045,
            "path_efficiency": 0.1818,
            "crew_guest_separation": 0.0682,
            "accessibility": 0.2159,
            "helm_ergonomics": 0.1591,
            "heel_impact": 0.0,
            "morning_circulation": 0.0909,
            "access_complexity": 0.0795,
        },
    },
    "small_motor": {
        "min_passage_width_mm": 600,
        "critical_passage_width_mm": 480,
        "max_steps_cockpit_pantry": 9,
        "min_helm_area_sqm": 2.0,
        "min_helm_visibility_deg": 235,
        "crew_guest_separation": False,
        "heel_angle_deg": 0,
        "weights": {
            "passage_width": 0.2093,
            "path_efficiency": 0.1860,
            "crew_guest_separation": 0.0581,
            "accessibility": 0.2209,
            "helm_ergonomics": 0.1512,
            "heel_impact": 0.0,
            "morning_circulation": 0.0930,
            "access_complexity": 0.0814,
        },
    },
    "sport_cruiser": {
        "min_passage_width_mm": 600,
        "critical_passage_width_mm": 500,
        "max_steps_cockpit_pantry": 10,
        "min_helm_area_sqm": 3.0,
        "min_helm_visibility_deg": 245,
        "crew_guest_separation": False,
        "heel_angle_deg": 0,
        "weights": {
            "passage_width": 0.1954,
            "path_efficiency": 0.1839,
            "crew_guest_separation": 0.0690,
            "accessibility": 0.2069,
            "helm_ergonomics": 0.1724,
            "heel_impact": 0.0,
            "morning_circulation": 0.0920,
            "access_complexity": 0.0805,
        },
    },
    "trawler": {
        "min_passage_width_mm": 650,
        "critical_passage_width_mm": 550,
        "max_steps_cockpit_pantry": 11,
        "min_helm_area_sqm": 2.5,
        "min_helm_visibility_deg": 240,
        "crew_guest_separation": False,
        "heel_angle_deg": 0,
        "weights": {
            "passage_width": 0.2000,
            "path_efficiency": 0.2000,
            "crew_guest_separation": 0.0588,
            "accessibility": 0.2118,
            "helm_ergonomics": 0.1529,
            "heel_impact": 0.0,
            "morning_circulation": 0.0941,
            "access_complexity": 0.0824,
        },
    },
    "explorer": {
        "min_passage_width_mm": 700,
        "critical_passage_width_mm": 600,
        "max_steps_cockpit_pantry": 12,
        "min_helm_area_sqm": 3.0,
        "min_helm_visibility_deg": 250,
        "crew_guest_separation": True,
        "heel_angle_deg": 12,
        "weights": {
            "passage_width": 0.16,
            "path_efficiency": 0.17,
            "crew_guest_separation": 0.15,
            "accessibility": 0.18,
            "helm_ergonomics": 0.13,
            "heel_impact": 0.05,
            "morning_circulation": 0.08,
            "access_complexity": 0.08,
        },
    },
    "superyacht": {
        "min_passage_width_mm": 900,
        "critical_passage_width_mm": 650,
        "max_steps_cockpit_pantry": 15,
        "min_helm_area_sqm": 5.0,
        "min_helm_visibility_deg": 270,
        "crew_guest_separation": True,
        "heel_angle_deg": 0,
        "weights": {
            "passage_width": 0.13,
            "path_efficiency": 0.17,
            "crew_guest_separation": 0.30,
            "accessibility": 0.13,
            "helm_ergonomics": 0.12,
            "heel_impact": 0.0,
            "morning_circulation": 0.08,
            "access_complexity": 0.07,
        },
    },
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}
REQUIRED_ZONES = ["engine", "pantry", "helm", "head"]


def _polygon_area_sqm(polygon: list[list[float]]) -> float:
    n = len(polygon)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2.0 / 1_000_000


def _build_adjacency(passages: list[dict]) -> dict[str, set[str]]:
    graph: dict[str, set[str]] = {}
    for p in passages:
        a, b = p["from_zone"], p["to_zone"]
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    return graph


def _bfs_distance(graph: dict[str, set[str]], start: str, end: str) -> int:
    if start not in graph:
        return -1
    visited = {start}
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        if node == end:
            return dist
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
    return -1


def _bfs_reachable(graph: dict[str, set[str]], start: str) -> set[str]:
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


def analyze_passage_widths(passages: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    if not passages:
        return 100.0, [], {"total_passages": 0, "narrow_passages": 0, "critical_passages": 0}

    min_width = config["min_passage_width_mm"]
    critical_width = config["critical_passage_width_mm"]
    warnings = []
    narrow = 0
    critical = 0

    for p in passages:
        w = p["width_mm"]
        if w < critical_width:
            critical += 1
            warnings.append({
                "severity": "critical",
                "message": f"Durchgang {p['from_zone']}→{p['to_zone']} ist kritisch schmal ({w:.0f}mm, Minimum: {critical_width:.0f}mm)",
                "suggestion": f"Durchgangsbreite auf mindestens {min_width:.0f}mm erweitern",
            })
        elif w < min_width:
            narrow += 1
            warnings.append({
                "severity": "warning",
                "message": f"Durchgang {p['from_zone']}→{p['to_zone']} ist zu schmal ({w:.0f}mm, empfohlen: {min_width:.0f}mm)",
                "suggestion": f"Durchgangsbreite auf mindestens {min_width:.0f}mm erweitern",
            })

    total = len(passages)
    ok_count = total - narrow - critical
    score = (ok_count / total) * 100.0
    if critical > 0:
        score = max(0.0, score - (critical / total) * 50.0)

    return score, warnings, {"total_passages": total, "narrow_passages": narrow, "critical_passages": critical}


def analyze_path_efficiency(zones: list[dict], passages: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    warnings = []
    graph = _build_adjacency(passages)
    zone_names = {z["name"] for z in zones}

    connected_names = set()
    for p in passages:
        connected_names.add(p["from_zone"])
        connected_names.add(p["to_zone"])
    isolated = zone_names - connected_names
    for name in isolated:
        warnings.append({
            "severity": "warning",
            "message": f"Zone '{name}' ist isoliert (keine Durchgänge)",
            "suggestion": f"Durchgang zu Zone '{name}' hinzufügen",
        })

    cockpit_zones = [z["name"] for z in zones if z["zone_type"] == "cockpit"]
    pantry_zones = [z["name"] for z in zones if z["zone_type"] == "pantry"]
    cockpit_pantry_steps = -1
    if cockpit_zones and pantry_zones:
        cockpit_pantry_steps = _bfs_distance(graph, cockpit_zones[0], pantry_zones[0])
        if cockpit_pantry_steps > config["max_steps_cockpit_pantry"]:
            warnings.append({
                "severity": "warning",
                "message": f"Weg Cockpit→Pantry zu lang ({cockpit_pantry_steps} Schritte, max: {config['max_steps_cockpit_pantry']})",
                "suggestion": "Direktere Verbindung zwischen Cockpit und Pantry schaffen",
            })

    score = 100.0
    if isolated:
        score -= len(isolated) * 10
    if cockpit_pantry_steps > config["max_steps_cockpit_pantry"]:
        excess = cockpit_pantry_steps - config["max_steps_cockpit_pantry"]
        score -= excess * 10
    if connected_names:
        start = next(iter(connected_names))
        reachable = _bfs_reachable(graph, start)
        if connected_names - reachable:
            score -= 30
    score = max(0.0, min(100.0, score))

    return score, warnings, {"cockpit_pantry_steps": cockpit_pantry_steps, "isolated_zones": list(isolated), "total_zones": len(zones)}


def analyze_crew_guest_separation(zones: list[dict], passages: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    if not config.get("crew_guest_separation"):
        return 100.0, [], {"separation_required": False, "shared_passages": 0}

    crew_zones = {z["name"] for z in zones if z.get("is_crew_area")}
    guest_zones = {z["name"] for z in zones if z.get("is_guest_area")}
    warnings = []
    shared = 0

    for p in passages:
        from_crew = p["from_zone"] in crew_zones
        from_guest = p["from_zone"] in guest_zones
        to_crew = p["to_zone"] in crew_zones
        to_guest = p["to_zone"] in guest_zones

        if (from_crew and to_guest) or (from_guest and to_crew):
            shared += 1
            warnings.append({
                "severity": "warning",
                "message": f"Durchgang {p['from_zone']}→{p['to_zone']} verbindet Crew- und Gastbereich",
                "suggestion": "Separate Durchgänge für Crew und Gäste planen",
            })

    total_relevant = max(len(passages), 1)
    score = max(0.0, 100.0 - (shared / total_relevant) * 100.0)

    return score, warnings, {"separation_required": True, "shared_passages": shared}


def analyze_accessibility(zones: list[dict], passages: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    zone_types = {z["zone_type"]: z["name"] for z in zones}
    graph = _build_adjacency(passages)
    warnings = []
    missing = []
    unreachable = []

    for req in REQUIRED_ZONES:
        if req not in zone_types:
            missing.append(req)
            zone_label = {"engine": "Maschinenraum", "pantry": "Pantry", "helm": "Steuerstand", "head": "WC/Bad"}.get(req, req)
            warnings.append({
                "severity": "critical",
                "message": f"Kritische Zone fehlt: {zone_label}",
                "suggestion": f"{zone_label} in das Layout aufnehmen",
            })
        else:
            zone_name = zone_types[req]
            all_zone_names = [z["name"] for z in zones if z["name"] != zone_name]
            reachable = False
            for other in all_zone_names:
                if _bfs_distance(graph, other, zone_name) >= 0:
                    reachable = True
                    break
            if not reachable and all_zone_names:
                unreachable.append(req)
                zone_label = {"engine": "Maschinenraum", "pantry": "Pantry", "helm": "Steuerstand", "head": "WC/Bad"}.get(req, req)
                warnings.append({
                    "severity": "warning",
                    "message": f"{zone_label} ist nicht erreichbar",
                    "suggestion": f"Durchgang zu {zone_label} hinzufügen",
                })

    total_required = len(REQUIRED_ZONES)
    present_and_reachable = total_required - len(missing) - len(unreachable)
    score = (present_and_reachable / total_required) * 100.0

    return score, warnings, {"missing_zones": missing, "unreachable_zones": unreachable, "required_zones": REQUIRED_ZONES}


def analyze_helm_ergonomics(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    helm_zones = [z for z in zones if z["zone_type"] == "helm"]
    warnings = []

    if not helm_zones:
        warnings.append({
            "severity": "critical",
            "message": "Kein Steuerstand im Layout definiert",
            "suggestion": "Steuerstand-Zone (helm) zum Layout hinzufügen",
        })
        return 0.0, warnings, {"helm_area_sqm": 0, "visibility_angle": 0}

    helm = helm_zones[0]
    area = _polygon_area_sqm(helm["polygon"])
    min_area = config["min_helm_area_sqm"]

    vis_angle = helm.get("visibility_angle") or config["min_helm_visibility_deg"]
    min_vis = config["min_helm_visibility_deg"]

    area_ratio = min(area / min_area, 1.0) if min_area > 0 else 1.0
    area_score = area_ratio * 50.0

    if area < min_area:
        warnings.append({
            "severity": "warning",
            "message": f"Steuerstand zu klein ({area:.1f}m², empfohlen: {min_area:.1f}m²)",
            "suggestion": f"Steuerstand auf mindestens {min_area:.1f}m² vergrößern",
        })

    vis_ratio = min(vis_angle / min_vis, 1.0) if min_vis > 0 else 1.0
    vis_score = vis_ratio * 50.0

    if vis_angle < min_vis:
        warnings.append({
            "severity": "warning",
            "message": f"Sichtwinkel am Steuerstand zu gering ({vis_angle:.0f}°, empfohlen: {min_vis:.0f}°)",
            "suggestion": f"Sichtwinkel auf mindestens {min_vis:.0f}° erweitern",
        })

    score = area_score + vis_score
    return score, warnings, {"helm_area_sqm": area, "visibility_angle": vis_angle}


_ACCESS_COMPLEXITY_SCORES = {
    "direct": 100,
    "panel_1": 80,
    "panel_2": 60,
    "floor_lift": 50,
    "furniture_move": 30,
    "major_disassembly": 10,
}

_TECHNICAL_ZONE_TYPES = {"engine", "head", "storage"}


def analyze_heel_impact(passages: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score passage usability under sailing heel conditions."""
    heel_angle = config.get("heel_angle_deg", 0)
    if heel_angle == 0:
        return 100.0, [], {"heel_angle_deg": 0, "affected_passages": 0}

    if not passages:
        return 100.0, [], {"heel_angle_deg": heel_angle, "affected_passages": 0}

    critical_width = config["critical_passage_width_mm"]
    cos_heel = math.cos(math.radians(heel_angle))
    warnings: list[dict] = []
    below_critical = 0

    for p in passages:
        effective_width = p["width_mm"] * cos_heel
        if effective_width < critical_width:
            below_critical += 1
            warnings.append({
                "severity": "warning",
                "message": (
                    f"Durchgang {p['from_zone']}→{p['to_zone']} unter Krängung zu schmal "
                    f"({effective_width:.0f}mm bei {heel_angle}° Krängung, Minimum: {critical_width:.0f}mm)"
                ),
                "suggestion": f"Durchgangsbreite auf mindestens {critical_width / cos_heel:.0f}mm erweitern für sichere Nutzung unter Krängung",
            })

    total = len(passages)
    ok_count = total - below_critical
    score = (ok_count / total) * 100.0

    return score, warnings, {
        "heel_angle_deg": heel_angle,
        "affected_passages": below_critical,
        "total_passages": total,
    }


def _bfs_path(graph: dict[str, set[str]], start: str, targets: set[str]) -> str | None:
    """BFS to find nearest target zone from start. Returns zone name or None."""
    if start in targets:
        return start
    if start not in graph:
        return None
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                if neighbor in targets:
                    return neighbor
                visited.add(neighbor)
                queue.append(neighbor)
    return None


def _bfs_path_edges(graph: dict[str, set[str]], start: str, end: str) -> list[tuple[str, str]]:
    """BFS returning the list of edges (passage connections) on the shortest path."""
    if start == end:
        return []
    if start not in graph:
        return []
    visited = {start}
    queue = deque([(start, [])])
    while queue:
        node, path = queue.popleft()
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                new_path = path + [(node, neighbor)]
                if neighbor == end:
                    return new_path
                visited.add(neighbor)
                queue.append((neighbor, new_path))
    return []


def analyze_morning_circulation(zones: list[dict], passages: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score morning routine traffic flow: cabin→head→pantry→cockpit."""
    warnings: list[dict] = []
    graph = _build_adjacency(passages)

    cabin_zones = [z["name"] for z in zones if z["zone_type"] == "cabin"]
    head_zones = {z["name"] for z in zones if z["zone_type"] == "head"}
    pantry_zones = {z["name"] for z in zones if z["zone_type"] == "pantry"}
    cockpit_zones = {z["name"] for z in zones if z["zone_type"] == "cockpit"}

    if not cabin_zones:
        return 100.0, [], {"bottleneck_count": 0, "missing_paths": 0, "morning_cabin_capacity": 0}

    morning_cabin_capacity = config.get("morning_cabin_capacity", len(cabin_zones))
    total_passages = max(len(passages), 1)

    # Track how many cabin paths use each passage (as edge tuple)
    passage_usage: dict[tuple[str, str], int] = {}
    missing_paths = 0

    for cabin in cabin_zones[:morning_cabin_capacity]:
        # cabin → head → pantry → cockpit
        route_segments = [
            (cabin, head_zones),
            (None, pantry_zones),  # from previous target
            (None, cockpit_zones),
        ]
        current = cabin
        path_broken = False

        for start_override, target_set in route_segments:
            start = start_override if start_override is not None else current
            target = _bfs_path(graph, start, target_set)
            if target is None:
                missing_paths += 1
                path_broken = True
                break
            edges = _bfs_path_edges(graph, start, target)
            for edge in edges:
                # Normalize edge to be order-independent
                key = (min(edge[0], edge[1]), max(edge[0], edge[1]))
                passage_usage[key] = passage_usage.get(key, 0) + 1
            current = target

        if path_broken:
            continue

    # Count bottlenecks (passages used by >2 cabin paths)
    bottleneck_count = sum(1 for count in passage_usage.values() if count > 2)

    for edge, count in passage_usage.items():
        if count > 2:
            warnings.append({
                "severity": "warning",
                "message": f"Durchgang {edge[0]}↔{edge[1]} ist Engpass im Morgenverkehr ({count} Kabinenwege)",
                "suggestion": "Alternativen Durchgang oder breiteren Zugang schaffen",
            })

    score = 100.0 - (bottleneck_count / total_passages * 50) - (missing_paths * 20)
    score = max(0.0, min(100.0, score))

    return score, warnings, {
        "bottleneck_count": bottleneck_count,
        "missing_paths": missing_paths,
        "morning_cabin_capacity": morning_cabin_capacity,
        "passage_usage": {f"{k[0]}↔{k[1]}": v for k, v in passage_usage.items()},
    }


def analyze_access_complexity(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score ease of access to technical zones based on access type."""
    warnings: list[dict] = []

    technical_zones = [z for z in zones if z["zone_type"] in _TECHNICAL_ZONE_TYPES]
    if not technical_zones:
        return 100.0, [], {"technical_zones_evaluated": 0}

    zone_scores = []
    for z in technical_zones:
        props = z.get("properties") or {}
        access_type = props.get("access_type", "direct")
        access_score = _ACCESS_COMPLEXITY_SCORES.get(access_type, 50)
        zone_scores.append(access_score)

        if access_score < 50:
            zone_label = {"engine": "Maschinenraum", "head": "WC/Bad", "storage": "Stauraum"}.get(z["zone_type"], z["name"])
            warnings.append({
                "severity": "warning",
                "message": f"Zugang zu '{z['name']}' ({zone_label}) schwierig: {access_type} (Bewertung: {access_score}/100)",
                "suggestion": f"Einfacheren Zugang zu '{z['name']}' schaffen (z.B. Inspektionsluken oder abnehmbare Paneele)",
            })

    score = sum(zone_scores) / len(zone_scores)

    return score, warnings, {
        "technical_zones_evaluated": len(zone_scores),
        "avg_access_score": round(score, 1),
    }


def run_ergonomics_analysis(zones: list[dict], passages: list[dict], boat_class: str, config_overrides: dict | None = None, data_source: str = "measured") -> dict:
    # Input validation
    if not isinstance(zones, list) or len(zones) == 0:
        return {
            "available": False,
            "reason": "Unzureichende Eingabedaten: zones muss eine nicht-leere Liste sein",
        }

    if not isinstance(passages, list):
        return {
            "available": False,
            "reason": "Unzureichende Eingabedaten: passages muss eine Liste sein",
        }

    if not isinstance(config_overrides, (dict, type(None))):
        return {
            "available": False,
            "reason": "Unzureichende Eingabedaten: config_overrides muss ein Dictionary sein",
        }

    if boat_class not in BOAT_CLASS_DEFAULTS:
        return {
            "available": False,
            "reason": f"Unzureichende Eingabedaten: Unbekannte Bootsklasse: {boat_class}",
        }

    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    weights = config.pop("weights").copy()

    if config_overrides:
        config.update(config_overrides)

    sub_scores = {}
    all_warnings = []
    all_suggestions = []
    all_metrics = {}

    analyses = [
        ("passage_width", lambda: analyze_passage_widths(passages, config)),
        ("path_efficiency", lambda: analyze_path_efficiency(zones, passages, config)),
        ("crew_guest_separation", lambda: analyze_crew_guest_separation(zones, passages, config)),
        ("accessibility", lambda: analyze_accessibility(zones, passages, config)),
        ("helm_ergonomics", lambda: analyze_helm_ergonomics(zones, config)),
        ("heel_impact", lambda: analyze_heel_impact(passages, config)),
        ("morning_circulation", lambda: analyze_morning_circulation(zones, passages, config)),
        ("access_complexity", lambda: analyze_access_complexity(zones, config)),
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
        "module": "ergonomics",
        "overall_score": round(overall, 1),
        "sub_scores": {k: round(v, 1) for k, v in sub_scores.items()},
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
        "confidence": data_source,
        "confidence_note": "Basiert auf geschätzten Werten aus öffentlichen Spezifikationen." if data_source == "estimated" else None,
    }
