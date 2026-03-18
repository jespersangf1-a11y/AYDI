"""DXF file parser for yacht layout import.

Extracts zones and passages from DXF layers using ezdxf.
"""
import io
import logging

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


def _detect_shared_edges(zones, tolerance=100.0):
    passages = []
    for i, z1 in enumerate(zones):
        for j, z2 in enumerate(zones):
            if j <= i:
                continue
            p1 = z1["polygon"]
            p2 = z2["polygon"]
            min_dist = float("inf")
            for pt1 in p1:
                for pt2 in p2:
                    dist = ((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2) ** 0.5
                    min_dist = min(min_dist, dist)
            if min_dist <= tolerance:
                passages.append({
                    "from_zone": z1["name"],
                    "to_zone": z2["name"],
                    "width_mm": max(tolerance, min_dist),
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
