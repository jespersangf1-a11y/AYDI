"""DXF file parser for yacht layout import.

Extracts zones and passages from DXF layers using ezdxf.
"""
import io
import logging
import math

import ezdxf

logger = logging.getLogger(__name__)

DEFAULT_LAYER_MAP = {
    "CABIN": "cabin",
    "PANTRY": "pantry",
    "GALLEY": "pantry",
    "HELM": "helm",
    "ENGINE": "engine",
    "STORAGE": "storage",
    "COCKPIT": "cockpit",
    "SALON": "salon",
    "SALOON": "salon",
    "HEAD": "head",
    "WC": "head",
    "BATHROOM": "head",
}


def _extract_polygon(entity):
    if entity.dxftype() == "LWPOLYLINE":
        points = list(entity.get_points(format="xy"))
        if len(points) >= 3:
            return [[float(x), float(y)] for x, y in points]
    elif entity.dxftype() == "POLYLINE":
        points = [(v.dxf.location.x, v.dxf.location.y) for v in entity.vertices]
        if len(points) >= 3:
            return [[float(x), float(y)] for x, y in points]
    return None


def _bounds(polygon):
    """(min_x, min_y, max_x, max_y) einer Punktliste, oder None wenn unbrauchbar."""
    xs = [p[0] for p in polygon if len(p) >= 2 and math.isfinite(p[0])]
    ys = [p[1] for p in polygon if len(p) >= 2 and math.isfinite(p[1])]
    if not xs or not ys:
        return None
    return min(xs), min(ys), max(xs), max(ys)


def _detect_shared_edges(zones, tolerance=100.0):
    """Findet aneinandergrenzende Zonen — OHNE eine Durchgangsbreite zu erfinden.

    Wichtig: ``min_dist`` ist der Abstand der naechstgelegenen ECKPUNKTE zweier
    Polygone. Das ist ein Nachbarschaftstest, keine Durchgangsbreite. Frueher
    wurde daraus ``width_mm = max(tolerance, min_dist)`` gebildet: Bei zwei
    aneinandergrenzenden Zonen ist ``min_dist`` praktisch 0, es kamen also immer
    exakt 100 mm heraus — eine frei erfundene Zahl. Die Ergonomie meldete
    daraufhin fuer JEDEN aus DXF importierten Durchgang "kritisch schmal
    (100mm)" und versah den Befund mit dem Konfidenzsiegel ``measured``.

    Eine Tuerbreite laesst sich aus benachbarten Raumpolygonen allein nicht
    ableiten — dafuer braeuchte es die Wandoeffnung selbst. Also wird die
    Nachbarschaft gemeldet und die Breite ehrlich als unbekannt markiert
    (``width_mm = None``); die Ergonomie behandelt solche Durchgaenge als
    nicht beurteilbar.

    Zur Laufzeit: Die Eckpunkt-Paarschleife ist O(n^2*m^2) und lief ohne
    Vorfilter — eine 0,37-MB-DXF blockierte den Event-Loop ueber 40 s. Ein
    Bounding-Box-Test vorweg verwirft die grosse Mehrheit der Zonenpaare in O(1).
    """
    passages = []
    prepared = [(z, _bounds(z.get("polygon") or [])) for z in zones]

    for i, (z1, b1) in enumerate(prepared):
        if b1 is None:
            continue
        for j in range(i + 1, len(prepared)):
            z2, b2 = prepared[j]
            if b2 is None:
                continue
            # Bounding-Box-Vorfilter: liegen die Huellen weiter als die Toleranz
            # auseinander, kann kein Eckpunktpaar naeher sein.
            if (
                b1[0] - b2[2] > tolerance
                or b2[0] - b1[2] > tolerance
                or b1[1] - b2[3] > tolerance
                or b2[1] - b1[3] > tolerance
            ):
                continue

            p1 = z1["polygon"]
            p2 = z2["polygon"]
            min_dist = float("inf")
            for pt1 in p1:
                if not (math.isfinite(pt1[0]) and math.isfinite(pt1[1])):
                    continue
                for pt2 in p2:
                    if not (math.isfinite(pt2[0]) and math.isfinite(pt2[1])):
                        continue
                    # Quadrierter Abstand: spart die Wurzel im heissesten Pfad und
                    # vermeidet den OverflowError bei sehr grossen Koordinaten.
                    dx = pt1[0] - pt2[0]
                    dy = pt1[1] - pt2[1]
                    dist_sq = dx * dx + dy * dy
                    if dist_sq < min_dist:
                        min_dist = dist_sq
                        if min_dist == 0.0:
                            break
                if min_dist == 0.0:
                    break

            if min_dist <= tolerance * tolerance:
                passages.append({
                    "from_zone": z1["name"],
                    "to_zone": z2["name"],
                    # Aus der Zonengeometrie NICHT ableitbar — siehe Docstring.
                    "width_mm": None,
                    "width_source": "unknown",
                    "is_primary": True,
                })
    return passages


def parse_dxf(content, layer_map=None):
    mapping = layer_map if layer_map is not None else DEFAULT_LAYER_MAP
    warnings = []

    try:
        bio = io.BytesIO(content)
        stream = io.TextIOWrapper(bio, encoding="utf-8", errors="replace")
        doc = ezdxf.read(stream)
    except Exception as e:
        raise ValueError(f"Ungültige DXF-Datei: {e}")

    msp = doc.modelspace()
    zones = []
    passage_lines = []
    zone_counters = {}

    for entity in msp:
        layer = entity.dxf.layer.upper()

        if layer == "PASSAGE":
            passage_lines.append(entity)
            continue

        zone_type = mapping.get(layer)
        if zone_type is None:
            continue

        polygon = _extract_polygon(entity)
        if polygon is None:
            logger.info("Skipping unsupported entity type %s on layer %s", entity.dxftype(), layer)
            warnings.append(f"Übersprungen: {entity.dxftype()} auf Layer {layer}")
            continue

        count = zone_counters.get(zone_type, 0) + 1
        zone_counters[zone_type] = count
        name = f"{zone_type}_{count}" if count > 1 else zone_type

        zones.append({
            "name": name,
            "zone_type": zone_type,
            "polygon": polygon,
            "is_crew_area": False,
            "is_guest_area": False,
            "visibility_angle": None,
        })

    if not zones:
        raise ValueError("Keine Zonen in der DXF-Datei gefunden. Prüfen Sie die Layer-Namen.")

    passages = []
    if passage_lines:
        for entity in passage_lines:
            if entity.dxftype() == "LINE":
                warnings.append("PASSAGE-Layer Linie erkannt (Durchgang wird automatisch zugeordnet)")
        passages = _detect_shared_edges(zones)
    else:
        passages = _detect_shared_edges(zones)

    return {
        "zones": zones,
        "passages": passages,
        "warnings": warnings,
    }
