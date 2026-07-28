"""Volume/storage analysis module for yacht layouts.

Pure function module — no database access.
"""
import logging
from collections import deque
from app.core.zone_types import normalisiere_zonen, warnung_unbekannte_typen
from app.services.analysis.scoring import weighted_overall, hinweis_teilanalysen

logger = logging.getLogger(__name__)

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "target_utilization": 0.70,
        "min_utilization": 0.50,
        "target_storage_ratio": 0.18,
        "min_storage_ratio": 0.15,
        "min_storage_zones": 2,
        "max_distribution_imbalance": 0.6,
        "max_furniture_ratio": 0.55,
        "min_furniture_ratio": 0.20,
        "weights": {
            "utilization": 0.30,
            "storage_ratio": 0.25,
            "storage_accessibility": 0.20,
            "storage_distribution": 0.15,
            "furniture_ratio": 0.10,
        },
    },
    "cruising_sail": {
        "target_utilization": 0.72,
        "min_utilization": 0.50,
        "target_storage_ratio": 0.15,
        "min_storage_ratio": 0.12,
        "min_storage_zones": 3,
        "max_distribution_imbalance": 0.5,
        "max_furniture_ratio": 0.50,
        "min_furniture_ratio": 0.22,
        "weights": {
            "utilization": 0.25,
            "storage_ratio": 0.25,
            "storage_accessibility": 0.20,
            "storage_distribution": 0.15,
            "furniture_ratio": 0.15,
        },
    },
    "large_motor": {
        "target_utilization": 0.70,
        "min_utilization": 0.45,
        "target_storage_ratio": 0.12,
        "min_storage_ratio": 0.10,
        "min_storage_zones": 4,
        "max_distribution_imbalance": 0.4,
        "max_furniture_ratio": 0.50,
        "min_furniture_ratio": 0.25,
        "weights": {
            "utilization": 0.20,
            "storage_ratio": 0.20,
            "storage_accessibility": 0.25,
            "storage_distribution": 0.15,
            "furniture_ratio": 0.20,
        },
    },
    "racing_sail": {
        "target_utilization": 0.80,
        "min_utilization": 0.55,
        "target_storage_ratio": 0.15,
        "min_storage_ratio": 0.10,
        "min_storage_zones": 2,
        "max_distribution_imbalance": 0.65,
        "max_furniture_ratio": 0.45,
        "min_furniture_ratio": 0.12,
        "weights": {
            "utilization": 0.35,
            "storage_ratio": 0.20,
            "storage_accessibility": 0.15,
            "storage_distribution": 0.10,
            "furniture_ratio": 0.20,
        },
    },
    "daysailer": {
        "target_utilization": 0.68,
        "min_utilization": 0.48,
        "target_storage_ratio": 0.16,
        "min_storage_ratio": 0.12,
        "min_storage_zones": 2,
        "max_distribution_imbalance": 0.60,
        "max_furniture_ratio": 0.52,
        "min_furniture_ratio": 0.18,
        "weights": {
            "utilization": 0.28,
            "storage_ratio": 0.25,
            "storage_accessibility": 0.20,
            "storage_distribution": 0.15,
            "furniture_ratio": 0.12,
        },
    },
    "motorsailer": {
        "target_utilization": 0.70,
        "min_utilization": 0.48,
        "target_storage_ratio": 0.14,
        "min_storage_ratio": 0.11,
        "min_storage_zones": 3,
        "max_distribution_imbalance": 0.50,
        "max_furniture_ratio": 0.50,
        "min_furniture_ratio": 0.22,
        "weights": {
            "utilization": 0.23,
            "storage_ratio": 0.23,
            "storage_accessibility": 0.22,
            "storage_distribution": 0.16,
            "furniture_ratio": 0.16,
        },
    },
    "catamaran_sail": {
        "target_utilization": 0.71,
        "min_utilization": 0.49,
        "target_storage_ratio": 0.14,
        "min_storage_ratio": 0.11,
        "min_storage_zones": 3,
        "max_distribution_imbalance": 0.48,
        "max_furniture_ratio": 0.50,
        "min_furniture_ratio": 0.21,
        "weights": {
            "utilization": 0.24,
            "storage_ratio": 0.23,
            "storage_accessibility": 0.21,
            "storage_distribution": 0.16,
            "furniture_ratio": 0.16,
        },
    },
    "catamaran_motor": {
        "target_utilization": 0.68,
        "min_utilization": 0.45,
        "target_storage_ratio": 0.12,
        "min_storage_ratio": 0.10,
        "min_storage_zones": 4,
        "max_distribution_imbalance": 0.40,
        "max_furniture_ratio": 0.50,
        "min_furniture_ratio": 0.25,
        "weights": {
            "utilization": 0.20,
            "storage_ratio": 0.20,
            "storage_accessibility": 0.25,
            "storage_distribution": 0.15,
            "furniture_ratio": 0.20,
        },
    },
    "small_motor": {
        "target_utilization": 0.68,
        "min_utilization": 0.45,
        "target_storage_ratio": 0.13,
        "min_storage_ratio": 0.10,
        "min_storage_zones": 3,
        "max_distribution_imbalance": 0.45,
        "max_furniture_ratio": 0.50,
        "min_furniture_ratio": 0.24,
        "weights": {
            "utilization": 0.21,
            "storage_ratio": 0.21,
            "storage_accessibility": 0.24,
            "storage_distribution": 0.15,
            "furniture_ratio": 0.19,
        },
    },
    "sport_cruiser": {
        "target_utilization": 0.66,
        "min_utilization": 0.42,
        "target_storage_ratio": 0.11,
        "min_storage_ratio": 0.09,
        "min_storage_zones": 4,
        "max_distribution_imbalance": 0.38,
        "max_furniture_ratio": 0.48,
        "min_furniture_ratio": 0.26,
        "weights": {
            "utilization": 0.18,
            "storage_ratio": 0.18,
            "storage_accessibility": 0.26,
            "storage_distribution": 0.17,
            "furniture_ratio": 0.21,
        },
    },
    "trawler": {
        "target_utilization": 0.64,
        "min_utilization": 0.40,
        "target_storage_ratio": 0.10,
        "min_storage_ratio": 0.08,
        "min_storage_zones": 5,
        "max_distribution_imbalance": 0.35,
        "max_furniture_ratio": 0.46,
        "min_furniture_ratio": 0.25,
        "weights": {
            "utilization": 0.17,
            "storage_ratio": 0.17,
            "storage_accessibility": 0.26,
            "storage_distribution": 0.19,
            "furniture_ratio": 0.21,
        },
    },
    "explorer": {
        "target_utilization": 0.64,
        "min_utilization": 0.39,
        "target_storage_ratio": 0.09,
        "min_storage_ratio": 0.07,
        "min_storage_zones": 6,
        "max_distribution_imbalance": 0.32,
        "max_furniture_ratio": 0.45,
        "min_furniture_ratio": 0.25,
        "weights": {
            "utilization": 0.16,
            "storage_ratio": 0.16,
            "storage_accessibility": 0.25,
            "storage_distribution": 0.21,
            "furniture_ratio": 0.22,
        },
    },
    "superyacht": {
        "target_utilization": 0.65,
        "min_utilization": 0.40,
        "target_storage_ratio": 0.10,
        "min_storage_ratio": 0.08,
        "min_storage_zones": 6,
        "max_distribution_imbalance": 0.3,
        "max_furniture_ratio": 0.45,
        "min_furniture_ratio": 0.25,
        "weights": {
            "utilization": 0.15,
            "storage_ratio": 0.15,
            "storage_accessibility": 0.25,
            "storage_distribution": 0.20,
            "furniture_ratio": 0.25,
        },
    },
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}


def _polygon_area_sqmm(polygon: list[list[float]]) -> float:
    n = len(polygon)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2.0


def _centroid(polygon: list[list[float]]) -> tuple[float, float]:
    n = len(polygon)
    if n == 0:
        return (0.0, 0.0)
    cx = sum(p[0] for p in polygon) / n
    cy = sum(p[1] for p in polygon) / n
    return (cx, cy)


def _build_adjacency(passages: list[dict]) -> dict[str, set[str]]:
    graph: dict[str, set[str]] = {}
    for p in passages:
        a, b = p["from_zone"], p["to_zone"]
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    return graph


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


def analyze_volume_utilization(zones: list[dict], config: dict) -> tuple[float | None, list[dict], dict]:
    """Score how efficiently the hull footprint is used by defined zones.

    Area-based approximation — true volumetric analysis would require hull geometry data.
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "severity": "info",
            "message": "Keine Zonen definiert — Volumennutzung kann nicht bewertet werden",
            "suggestion": "Zonen zum Layout hinzufügen",
        })
        # 50.0 war eine Zahl ohne Messung: sie ging voll gewichtet in die
        # Modulnote ein und war in der Oberflaeche nicht von einem Messwert zu
        # unterscheiden.
        return None, warnings, {"utilization_ratio": None, "zone_area_sqmm": None, "bbox_area_sqmm": None}

    all_points = [p for z in zones for p in z["polygon"]]
    if not all_points:
        warnings.append({
            "severity": "info",
            "message": "Keine Polygondaten vorhanden — Volumennutzung kann nicht bewertet werden",
            "suggestion": "Zonenpolygone überprüfen",
        })
        return None, warnings, {"utilization_ratio": None, "zone_area_sqmm": None, "bbox_area_sqmm": None}

    min_x = min(p[0] for p in all_points)
    max_x = max(p[0] for p in all_points)
    min_y = min(p[1] for p in all_points)
    max_y = max(p[1] for p in all_points)

    bbox_area = (max_x - min_x) * (max_y - min_y)
    if bbox_area == 0:
        warnings.append({
            "severity": "info",
            "message": "Zonenfläche nicht berechenbar (degenerierte Geometrie)",
            "suggestion": "Zonenpolygone überprüfen",
        })
        return None, warnings, {"utilization_ratio": None, "zone_area_sqmm": None, "bbox_area_sqmm": None}

    zone_area = sum(_polygon_area_sqmm(z["polygon"]) for z in zones)
    ratio = zone_area / bbox_area

    target = config["target_utilization"]
    minimum = config["min_utilization"]

    if ratio >= target:
        score = 100.0
    elif ratio >= minimum:
        score = 50.0 + (ratio - minimum) / (target - minimum) * 50.0
        warnings.append({
            "severity": "info",
            "message": f"Flächennutzung unter Zielwert ({ratio:.0%}, Ziel: {target:.0%})",
            "suggestion": f"Flächennutzung auf {target:.0%} erhöhen",
        })
    else:
        score = (ratio / minimum) * 50.0 if minimum > 0 else 0.0
        warnings.append({
            "severity": "warning",
            "message": f"Flächennutzung gering ({ratio:.0%}, Ziel: {target:.0%})",
            "suggestion": f"Flächennutzung auf mindestens {minimum:.0%} erhöhen",
        })

    return score, warnings, {
        "utilization_ratio": round(ratio, 4),
        "zone_area_sqmm": zone_area,
        "bbox_area_sqmm": bbox_area,
    }


# Zone types excluded from furniture evaluation (no furniture expected)
_FURNITURE_EXCLUDED_TYPES = {"engine", "storage", "swim_platform", "tender_garage", "foredeck"}


def analyze_furniture_ratio(zones: list[dict], config: dict) -> tuple[float | None, list[dict], dict]:
    """Score furniture density per zone using properties.furniture_area_pct."""
    warnings: list[dict] = []
    max_ratio = config["max_furniture_ratio"]
    min_ratio = config["min_furniture_ratio"]

    evaluable = []
    for z in zones:
        if z["zone_type"] in _FURNITURE_EXCLUDED_TYPES:
            continue
        props = z.get("properties") or {}
        if "furniture_area_pct" in props:
            evaluable.append(z)

    if not evaluable:
        warnings.append({
            "severity": "info",
            "message": "Keine Möblierungsdaten vorhanden — Bewertung nicht möglich",
            "suggestion": "furniture_area_pct in Zone-Eigenschaften angeben (0.0–1.0)",
        })
        # Ohne eine einzige Angabe zur Moeblierung gibt es nichts zu mitteln.
        # Die bisherige 50.0 stand fuer "mittelmaessig" und behauptete damit ein
        # Ergebnis, wo keine Eingangsgroesse vorlag.
        return None, warnings, {"zones_evaluated": 0, "cramped": None, "sparse": None}

    zone_scores = []
    cramped = 0
    sparse = 0

    for z in evaluable:
        pct = z["properties"]["furniture_area_pct"]
        if pct > max_ratio:
            cramped += 1
            excess = pct - max_ratio
            zone_score = max(0.0, 100.0 - (excess / max_ratio) * 100.0)
            zone_label = z["name"]
            warnings.append({
                "severity": "warning",
                "message": f"Zone '{zone_label}' übermöbliert ({pct:.0%}, max: {max_ratio:.0%})",
                "suggestion": f"Möblierung in '{zone_label}' reduzieren",
            })
        elif pct < min_ratio:
            sparse += 1
            zone_score = max(0.0, (pct / min_ratio) * 80.0)
            zone_label = z["name"]
            warnings.append({
                "severity": "info",
                "message": f"Zone '{zone_label}' spärlich möbliert ({pct:.0%}, min: {min_ratio:.0%})",
                "suggestion": f"Möblierung in '{zone_label}' erhöhen oder Zonengröße reduzieren",
            })
        else:
            zone_score = 100.0

        zone_scores.append(zone_score)

    score = sum(zone_scores) / len(zone_scores)
    return score, warnings, {"zones_evaluated": len(evaluable), "cramped": cramped, "sparse": sparse}


def analyze_storage_ratio(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score ratio of storage area to total layout area."""
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
    ideal = config["target_storage_ratio"]
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


def analyze_storage_distribution(zones: list[dict], config: dict) -> tuple[float | None, list[dict], dict]:
    """Score how evenly storage zones are distributed across the layout."""
    storage_zones = [z for z in zones if z["zone_type"] == "storage"]
    warnings = []

    if len(storage_zones) < 2:
        if storage_zones:
            warnings.append({
                "severity": "info",
                "message": f"Nur {len(storage_zones)} Stauraum definiert (empfohlen: {config['min_storage_zones']})",
                "suggestion": "Weitere Stauräume an verschiedenen Positionen hinzufügen",
            })
        # Verteilung setzt mindestens zwei Stauraeume voraus — ein einzelner
        # Stauraum ist weder gleichmaessig noch ungleichmaessig verteilt. Die
        # frueheren Werte (50.0 bzw. 0.0) nannten dazu ein Ungleichgewicht von
        # 1.0, das nie berechnet wurde. Das Fehlen von Stauraum an sich meldet
        # bereits analyze_storage_ratio als kritischen Befund.
        warnings.append({
            "code": "STORAGE_DISTRIBUTION_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                f"Stauraumverteilung nicht beurteilbar: {len(storage_zones)} Stauraum "
                "im Layout, für eine Verteilungsaussage sind mindestens zwei nötig."
            ),
            "suggestion": "Weitere Stauräume an verschiedenen Positionen anlegen.",
            "location": "layout.zones",
        })
        return None, warnings, {"imbalance": None, "storage_count": len(storage_zones)}

    all_points = [p for z in zones for p in z["polygon"]]
    if not all_points:
        # Ohne Polygondaten gibt es keine Bezugsgroesse. 0.0 mit einem
        # Ungleichgewicht von 1.0 war ein erfundener Schlechtwert.
        warnings.append({
            "code": "STORAGE_DISTRIBUTION_NOT_ASSESSABLE",
            "severity": "warning",
            "message": "Stauraumverteilung nicht beurteilbar: keine Polygondaten im Layout.",
            "suggestion": "Zonenpolygone prüfen bzw. Layout erneut importieren.",
            "location": "layout.zones.polygon",
        })
        return None, warnings, {"imbalance": None, "storage_count": len(storage_zones)}

    min_x = min(p[0] for p in all_points)
    max_x = max(p[0] for p in all_points)
    min_y = min(p[1] for p in all_points)
    max_y = max(p[1] for p in all_points)
    bbox_diag = ((max_x - min_x) ** 2 + (max_y - min_y) ** 2) ** 0.5

    if bbox_diag == 0:
        # Entartete Geometrie ohne Ausdehnung. Die frueheren 100.0 mit einem
        # Ungleichgewicht von 0.0 hiessen "perfekt verteilt" — fuer ein Layout,
        # dessen Ausdehnung sich nicht bestimmen laesst.
        warnings.append({
            "code": "STORAGE_DISTRIBUTION_NOT_ASSESSABLE",
            "severity": "warning",
            "message": "Stauraumverteilung nicht beurteilbar: das Layout hat keine messbare Ausdehnung.",
            "suggestion": "Zonenpolygone auf entartete Geometrie prüfen.",
            "location": "layout.zones.polygon",
        })
        return None, warnings, {"imbalance": None, "storage_count": len(storage_zones)}

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


def analyze_storage_accessibility(zones: list[dict], passages: list[dict], config: dict) -> tuple[float | None, list[dict], dict]:
    """Score whether storage zones are reachable via passage graph."""
    storage_zones = [z for z in zones if z["zone_type"] == "storage"]
    warnings = []

    if not storage_zones:
        # Kein Stauraum heisst nicht "alle Stauraeume erreichbar". Die frueheren
        # 100.0 waren eine Erreichbarkeitsbestaetigung fuer eine leere Menge.
        warnings.append({
            "code": "STORAGE_ACCESS_NOT_ASSESSABLE",
            "severity": "info",
            "message": "Erreichbarkeit der Stauräume nicht beurteilbar: das Layout enthält keine Stauräume.",
            "suggestion": "Stauräume (storage) im Layout anlegen.",
            "location": "layout.zones",
        })
        return None, warnings, {"accessible": None, "total_storage": 0}

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

    # total ist hier zwangslaeufig > 0 — die leere Menge kehrt oben zurueck.
    total = len(storage_zones)
    score = (accessible / total) * 100.0
    return score, warnings, {"accessible": accessible, "total_storage": total}


def run_volume_storage_analysis(zones: list[dict], passages: list[dict], boat_class: str, config_overrides: dict | None = None, data_source: str = "measured") -> dict:
    # Ein Layout ohne Zonen ist kein Layout. Ohne diese Pruefung lieferten die
    # Teilanalysen ihre jeweiligen Vorgabewerte zurueck, und daraus entstand ein
    # Gesamtwert, der wie ein Befund aussah — obwohl nichts gemessen wurde.
    if not isinstance(zones, list) or len(zones) == 0:
        return {
            "module": "volume_storage",
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

    sub_scores = {}
    all_warnings = []
    all_suggestions = []
    all_metrics = {}

    analyses = [
        ("utilization", lambda: analyze_volume_utilization(zones, config)),
        ("storage_ratio", lambda: analyze_storage_ratio(zones, config)),
        ("storage_distribution", lambda: analyze_storage_distribution(zones, config)),
        ("storage_accessibility", lambda: analyze_storage_accessibility(zones, passages, config)),
        ("furniture_ratio", lambda: analyze_furniture_ratio(zones, config)),
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
            "module": "volume_storage",
            "available": False,
            "reason": "Keine der Teilanalysen konnte mangels Datengrundlage durchgeführt werden.",
            "suggestions": [
                "Layout- und Stammdaten vervollständigen, um eine Bewertung zu ermöglichen."
            ],
        }

    for w in all_warnings:
        if w.get("suggestion") and w["suggestion"] not in all_suggestions:
            all_suggestions.append(w["suggestion"])

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    return {
        "module": "volume_storage",
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
