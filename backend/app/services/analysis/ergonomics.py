"""Ergonomics analysis module for yacht layouts.

Pure function module — no database access. Receives data as parameters,
returns analysis results as dicts.
"""
import logging
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
        "weights": {
            "passage_width": 0.30,
            "path_efficiency": 0.20,
            "crew_guest_separation": 0.05,
            "accessibility": 0.30,
            "helm_ergonomics": 0.15,
        },
    },
    "cruising_sail": {
        "min_passage_width_mm": 650,
        "critical_passage_width_mm": 500,
        "max_steps_cockpit_pantry": 10,
        "min_helm_area_sqm": 2.0,
        "min_helm_visibility_deg": 225,
        "crew_guest_separation": False,
        "weights": {
            "passage_width": 0.25,
            "path_efficiency": 0.20,
            "crew_guest_separation": 0.10,
            "accessibility": 0.25,
            "helm_ergonomics": 0.20,
        },
    },
    "large_motor": {
        "min_passage_width_mm": 750,
        "critical_passage_width_mm": 550,
        "max_steps_cockpit_pantry": 12,
        "min_helm_area_sqm": 3.0,
        "min_helm_visibility_deg": 240,
        "crew_guest_separation": True,
        "weights": {
            "passage_width": 0.20,
            "path_efficiency": 0.20,
            "crew_guest_separation": 0.25,
            "accessibility": 0.20,
            "helm_ergonomics": 0.15,
        },
    },
    "superyacht": {
        "min_passage_width_mm": 900,
        "critical_passage_width_mm": 650,
        "max_steps_cockpit_pantry": 15,
        "min_helm_area_sqm": 5.0,
        "min_helm_visibility_deg": 270,
        "crew_guest_separation": True,
        "weights": {
            "passage_width": 0.15,
            "path_efficiency": 0.20,
            "crew_guest_separation": 0.35,
            "accessibility": 0.15,
            "helm_ergonomics": 0.15,
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


def run_ergonomics_analysis(zones: list[dict], passages: list[dict], boat_class: str, config_overrides: dict | None = None) -> dict:
    if boat_class not in BOAT_CLASS_DEFAULTS:
        raise ValueError(f"Unknown boat class: {boat_class}")
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
    }
