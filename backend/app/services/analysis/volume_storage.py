"""Volume/storage analysis module for yacht layouts.

Pure function module — no database access.
"""
import logging
from collections import deque

logger = logging.getLogger(__name__)

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "min_storage_ratio": 0.15,
        "ideal_storage_ratio": 0.22,
        "min_storage_zones": 2,
        "max_distribution_imbalance": 0.6,
        "weights": {
            "storage_ratio": 0.40,
            "storage_distribution": 0.30,
            "storage_accessibility": 0.30,
        },
    },
    "cruising_sail": {
        "min_storage_ratio": 0.12,
        "ideal_storage_ratio": 0.18,
        "min_storage_zones": 3,
        "max_distribution_imbalance": 0.5,
        "weights": {
            "storage_ratio": 0.35,
            "storage_distribution": 0.35,
            "storage_accessibility": 0.30,
        },
    },
    "large_motor": {
        "min_storage_ratio": 0.10,
        "ideal_storage_ratio": 0.15,
        "min_storage_zones": 4,
        "max_distribution_imbalance": 0.4,
        "weights": {
            "storage_ratio": 0.30,
            "storage_distribution": 0.40,
            "storage_accessibility": 0.30,
        },
    },
    "superyacht": {
        "min_storage_ratio": 0.08,
        "ideal_storage_ratio": 0.12,
        "min_storage_zones": 6,
        "max_distribution_imbalance": 0.3,
        "weights": {
            "storage_ratio": 0.30,
            "storage_distribution": 0.40,
            "storage_accessibility": 0.30,
        },
    },
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}


def _polygon_area_sqmm(polygon):
    n = len(polygon)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2.0


def _centroid(polygon):
    n = len(polygon)
    if n == 0:
        return (0.0, 0.0)
    cx = sum(p[0] for p in polygon) / n
    cy = sum(p[1] for p in polygon) / n
    return (cx, cy)


def _build_adjacency(passages):
    graph = {}
    for p in passages:
        a, b = p["from_zone"], p["to_zone"]
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    return graph


def _bfs_reachable(graph, start):
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


def analyze_storage_ratio(zones, config):
    storage_zones = [z for z in zones if z["zone_type"] == "storage"]
    warnings = []

    if not storage_zones:
        warnings.append({
            "severity": "critical",
            "message": "Keine Stauräume im Layout definiert",
            "suggestion": "Stauräume (storage) zum Layout hinzufügen",
        })
        return 0.0, warnings, {"storage_ratio": 0.0, "storage_area_sqmm": 0, "total_area_sqmm": 0}

    storage_area = sum(_polygon_area_sqmm(z["polygon"]) for z in storage_zones)
    total_area = sum(_polygon_area_sqmm(z["polygon"]) for z in zones)

    if total_area == 0:
        return 0.0, warnings, {"storage_ratio": 0.0, "storage_area_sqmm": 0, "total_area_sqmm": 0}

    ratio = storage_area / total_area
    ideal = config["ideal_storage_ratio"]
    minimum = config["min_storage_ratio"]

    if ratio >= ideal:
        score = 100.0
    elif ratio >= minimum:
        score = 50.0 + (ratio - minimum) / (ideal - minimum) * 50.0
    else:
        score = (ratio / minimum) * 50.0 if minimum > 0 else 0.0
        warnings.append({
            "severity": "warning",
            "message": f"Stauraumanteil zu gering ({ratio:.1%}, empfohlen: mindestens {minimum:.1%})",
            "suggestion": f"Stauraumanteil auf mindestens {minimum:.1%} erhöhen",
        })

    return score, warnings, {"storage_ratio": round(ratio, 4), "storage_area_sqmm": storage_area, "total_area_sqmm": total_area}


def analyze_storage_distribution(zones, config):
    storage_zones = [z for z in zones if z["zone_type"] == "storage"]
    warnings = []

    if len(storage_zones) < 2:
        if storage_zones:
            warnings.append({
                "severity": "info",
                "message": f"Nur {len(storage_zones)} Stauraum definiert (empfohlen: {config['min_storage_zones']})",
                "suggestion": "Weitere Stauräume an verschiedenen Positionen hinzufügen",
            })
        return 50.0 if storage_zones else 0.0, warnings, {"imbalance": 1.0, "storage_count": len(storage_zones)}

    all_points = [p for z in zones for p in z["polygon"]]
    if not all_points:
        return 0.0, warnings, {"imbalance": 1.0, "storage_count": 0}

    min_x = min(p[0] for p in all_points)
    max_x = max(p[0] for p in all_points)
    min_y = min(p[1] for p in all_points)
    max_y = max(p[1] for p in all_points)
    bbox_diag = ((max_x - min_x) ** 2 + (max_y - min_y) ** 2) ** 0.5

    if bbox_diag == 0:
        return 100.0, warnings, {"imbalance": 0.0, "storage_count": len(storage_zones)}

    centroids = [_centroid(z["polygon"]) for z in storage_zones]
    avg_cx = sum(c[0] for c in centroids) / len(centroids)
    avg_cy = sum(c[1] for c in centroids) / len(centroids)

    avg_dist = sum(((c[0] - avg_cx) ** 2 + (c[1] - avg_cy) ** 2) ** 0.5 for c in centroids) / len(centroids)
    spread = avg_dist / bbox_diag

    imbalance = max(0.0, 1.0 - spread * 4)

    max_imbalance = config["max_distribution_imbalance"]
    if imbalance > max_imbalance:
        warnings.append({
            "severity": "warning",
            "message": f"Stauräume ungleichmäßig verteilt (Ungleichgewicht: {imbalance:.2f}, max: {max_imbalance:.2f})",
            "suggestion": "Stauräume gleichmäßiger über das Layout verteilen",
        })

    if len(storage_zones) < config["min_storage_zones"]:
        warnings.append({
            "severity": "info",
            "message": f"Wenige Stauräume ({len(storage_zones)}, empfohlen: {config['min_storage_zones']})",
            "suggestion": "Weitere Stauräume hinzufügen",
        })

    score = max(0.0, (1.0 - imbalance) * 100.0)
    return score, warnings, {"imbalance": round(imbalance, 4), "storage_count": len(storage_zones)}


def analyze_storage_accessibility(zones, passages, config):
    storage_zones = [z for z in zones if z["zone_type"] == "storage"]
    warnings = []

    if not storage_zones:
        return 100.0, warnings, {"accessible": 0, "total_storage": 0}

    graph = _build_adjacency(passages)
    non_storage = [z["name"] for z in zones if z["zone_type"] != "storage"]

    accessible = 0
    for sz in storage_zones:
        reachable = False
        for other in non_storage:
            reachable_set = _bfs_reachable(graph, other)
            if sz["name"] in reachable_set:
                reachable = True
                break
        if reachable:
            accessible += 1
        else:
            warnings.append({
                "severity": "warning",
                "message": f"Stauraum '{sz['name']}' ist nicht erreichbar",
                "suggestion": f"Durchgang zu Stauraum '{sz['name']}' hinzufügen",
            })

    total = len(storage_zones)
    score = (accessible / total) * 100.0 if total > 0 else 100.0
    return score, warnings, {"accessible": accessible, "total_storage": total}


def run_volume_storage_analysis(zones, passages, boat_class, config_overrides=None):
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
        ("storage_ratio", lambda: analyze_storage_ratio(zones, config)),
        ("storage_distribution", lambda: analyze_storage_distribution(zones, config)),
        ("storage_accessibility", lambda: analyze_storage_accessibility(zones, passages, config)),
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
        "module": "volume_storage",
        "overall_score": round(overall, 1),
        "sub_scores": {k: round(v, 1) for k, v in sub_scores.items()},
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
    }
