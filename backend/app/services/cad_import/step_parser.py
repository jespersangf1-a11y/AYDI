"""STEP/IGES file parser for yacht layout import.

Extracts zones and passages from 3D CAD files.
STEP files are parsed via trimesh (which uses OpenCascade backends when available).
IGES files are parsed via a lightweight text-based parser since IGES is a text format.

All measurements are in millimeters, origin at bow/starboard.
"""
import io
import logging
import math
import os
import tempfile
from dataclasses import dataclass, field
from typing import Optional

import numpy as np

logger = logging.getLogger(__name__)

# Zone classification by layer/body name hints (case-insensitive)
ZONE_NAME_MAP = {
    "CABIN": "cabin",
    "PANTRY": "pantry",
    "GALLEY": "pantry",
    "KITCHEN": "pantry",
    "HELM": "helm",
    "BRIDGE": "helm",
    "ENGINE": "engine",
    "STORAGE": "storage",
    "LOCKER": "storage",
    "COCKPIT": "cockpit",
    "SALON": "salon",
    "SALOON": "salon",
    "HEAD": "head",
    "WC": "head",
    "BATHROOM": "head",
    "CREW": "crew_quarters",
    "FLYBRIDGE": "flybridge",
    "FOREDECK": "foredeck",
    "SWIM": "swim_platform",
    "TENDER": "tender_garage",
}

# Typical zone area ranges in mm^2 for classification by size
ZONE_AREA_RANGES = {
    "head": (500_000, 3_000_000),         # 0.5 - 3 sqm
    "storage": (100_000, 2_000_000),      # 0.1 - 2 sqm
    "pantry": (2_000_000, 8_000_000),     # 2 - 8 sqm
    "cabin": (3_000_000, 15_000_000),     # 3 - 15 sqm
    "salon": (8_000_000, 40_000_000),     # 8 - 40 sqm
    "cockpit": (5_000_000, 30_000_000),   # 5 - 30 sqm
    "engine": (2_000_000, 15_000_000),    # 2 - 15 sqm
    "helm": (1_000_000, 6_000_000),       # 1 - 6 sqm
}

# Default opening/door width in mm when we cannot measure precisely
DEFAULT_PASSAGE_WIDTH_MM = 700.0

# Tolerance for clustering Z-values into deck levels (mm)
DECK_Z_TOLERANCE_MM = 150.0

# Minimum polygon area to consider as a zone (mm^2) - 0.3 sqm
MIN_ZONE_AREA_MM2 = 300_000.0

# Maximum distance between zone boundaries to detect passages (mm)
PASSAGE_PROXIMITY_MM = 200.0


@dataclass
class DeckLevel:
    """Represents a detected deck level."""
    z_mm: float
    name: str
    face_count: int = 0


@dataclass
class ExtractedBody:
    """Represents a solid body extracted from STEP/IGES."""
    name: str
    vertices_2d: list[list[float]]  # Projected 2D polygon [[x,y], ...]
    z_min: float = 0.0
    z_max: float = 0.0
    area_mm2: float = 0.0
    deck_z: float = 0.0
    source_name: str = ""


def _cluster_z_values(z_values: list[float], tolerance: float = DECK_Z_TOLERANCE_MM) -> list[float]:
    """Cluster Z-values into deck levels.

    Groups Z-values that are within `tolerance` of each other
    and returns the mean of each cluster, sorted ascending.
    """
    if not z_values:
        return []

    sorted_z = sorted(z_values)
    clusters: list[list[float]] = [[sorted_z[0]]]

    for z in sorted_z[1:]:
        if z - clusters[-1][-1] <= tolerance:
            clusters[-1].append(z)
        else:
            clusters.append([z])

    return [sum(c) / len(c) for c in clusters]


def detect_deck_levels(z_values: list[float], tolerance: float = DECK_Z_TOLERANCE_MM) -> list[DeckLevel]:
    """Detect deck levels from a list of Z-values of horizontal faces.

    Args:
        z_values: Z-coordinates of horizontal face centroids.
        tolerance: Maximum distance between Z-values in the same deck.

    Returns:
        List of DeckLevel objects sorted by height.
    """
    if not z_values:
        return [DeckLevel(z_mm=0.0, name="Hauptdeck", face_count=0)]

    cluster_centers = _cluster_z_values(z_values, tolerance)

    # Count faces per cluster
    face_counts: list[int] = []
    for center in cluster_centers:
        count = sum(1 for z in z_values if abs(z - center) <= tolerance)
        face_counts.append(count)

    # Name decks based on count
    deck_names = _generate_deck_names(len(cluster_centers))

    return [
        DeckLevel(z_mm=round(z, 1), name=name, face_count=fc)
        for z, name, fc in zip(cluster_centers, deck_names, face_counts)
    ]


def _generate_deck_names(count: int) -> list[str]:
    """Generate German deck names based on number of decks."""
    if count == 1:
        return ["Hauptdeck"]
    if count == 2:
        return ["Unterdeck", "Hauptdeck"]
    if count == 3:
        return ["Unterdeck", "Hauptdeck", "Oberdeck"]
    # For 4+, number them
    names = ["Unterdeck"]
    for i in range(1, count - 1):
        names.append(f"Deck {i}")
    names.append("Oberdeck")
    return names


def _polygon_area(polygon: list[list[float]]) -> float:
    """Calculate area of a 2D polygon using the shoelace formula.

    Args:
        polygon: List of [x, y] coordinate pairs.

    Returns:
        Absolute area in mm^2.
    """
    n = len(polygon)
    if n < 3:
        return 0.0

    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2.0


def _polygon_centroid(polygon: list[list[float]]) -> tuple[float, float]:
    """Calculate centroid of a 2D polygon."""
    n = len(polygon)
    if n == 0:
        return (0.0, 0.0)

    cx = sum(p[0] for p in polygon) / n
    cy = sum(p[1] for p in polygon) / n
    return (cx, cy)


def _simplify_polygon(polygon: list[list[float]], tolerance: float = 50.0) -> list[list[float]]:
    """Simplify polygon by removing nearly-collinear points.

    Uses the Ramer-Douglas-Peucker algorithm concept in a simplified form:
    removes points that are within `tolerance` mm of the line between
    their neighbors.
    """
    if len(polygon) <= 4:
        return polygon

    result = [polygon[0]]
    for i in range(1, len(polygon) - 1):
        prev = result[-1]
        curr = polygon[i]
        nxt = polygon[i + 1]

        # Distance from curr to line prev->nxt
        dx = nxt[0] - prev[0]
        dy = nxt[1] - prev[1]
        line_len = math.sqrt(dx * dx + dy * dy)

        if line_len < 1e-6:
            result.append(curr)
            continue

        dist = abs(dy * curr[0] - dx * curr[1] + nxt[0] * prev[1] - nxt[1] * prev[0]) / line_len
        if dist > tolerance:
            result.append(curr)

    result.append(polygon[-1])

    # Ensure we still have a valid polygon
    if len(result) < 3:
        return polygon

    return result


def classify_zone_by_name(name: str) -> Optional[str]:
    """Try to classify a zone by its body/layer name.

    Checks longer keys first to avoid partial matches
    (e.g., "FLYBRIDGE" before "BRIDGE").

    Args:
        name: The body or layer name from the CAD file.

    Returns:
        Zone type string, or None if no match.
    """
    upper = name.upper()
    # Sort keys longest-first so "FLYBRIDGE" matches before "BRIDGE",
    # "BATHROOM" before "HEAD", etc.
    for key in sorted(ZONE_NAME_MAP.keys(), key=len, reverse=True):
        if key in upper:
            return ZONE_NAME_MAP[key]
    return None


def classify_zone_by_geometry(
    area_mm2: float,
    centroid: tuple[float, float],
    boat_length_mm: float = 12000.0,
    boat_beam_mm: float = 4000.0,
) -> str:
    """Classify a zone by its geometric properties when name hints fail.

    Uses area ranges and position on the boat (fore/aft, port/starboard).

    Args:
        area_mm2: Zone area in mm^2.
        centroid: (x, y) centroid of the zone polygon.
        boat_length_mm: Boat length overall in mm.
        boat_beam_mm: Boat beam in mm.

    Returns:
        Best-guess zone type string.
    """
    cx, cy = centroid
    x_ratio = cx / boat_length_mm if boat_length_mm > 0 else 0.5

    # Very small → likely head or storage
    if area_mm2 < 2_000_000:
        if area_mm2 < 1_000_000:
            return "storage"
        return "head"

    # Aft position (x_ratio > 0.7) → cockpit or engine
    if x_ratio > 0.75:
        if area_mm2 < 4_000_000:
            return "engine"
        return "cockpit"

    # Forward position (x_ratio < 0.2) → cabin or foredeck
    if x_ratio < 0.2:
        return "cabin"

    # Mid-ship, large → salon
    if area_mm2 > 8_000_000:
        return "salon"

    # Mid-ship, medium → cabin or pantry
    half_beam = boat_beam_mm / 2
    if cy < half_beam * 0.6 or cy > half_beam * 1.4:
        return "cabin"

    return "pantry"


def _detect_passages_from_proximity(
    zones: list[dict],
    tolerance: float = PASSAGE_PROXIMITY_MM,
) -> list[dict]:
    """Detect passages between zones based on polygon proximity.

    Finds zone pairs whose boundaries are within `tolerance` mm of each other.

    Args:
        zones: List of zone dicts with 'polygon' and 'name' keys.
        tolerance: Maximum boundary distance to create a passage.

    Returns:
        List of passage dicts.
    """
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
                    dist = math.sqrt(
                        (pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2
                    )
                    min_dist = min(min_dist, dist)

            if min_dist <= tolerance:
                passages.append({
                    "from_zone": z1["name"],
                    "to_zone": z2["name"],
                    "width_mm": max(DEFAULT_PASSAGE_WIDTH_MM, tolerance - min_dist),
                    "is_primary": True,
                })

    return passages


def _project_mesh_to_2d_polygons(
    vertices: np.ndarray,
    faces: np.ndarray,
    deck_z: float,
    z_tolerance: float = DECK_Z_TOLERANCE_MM,
) -> list[list[list[float]]]:
    """Project horizontal faces at a deck level into 2D polygons.

    Finds faces near the given deck Z level and extracts their 2D projections.

    Args:
        vertices: Nx3 array of mesh vertices.
        faces: Mx3 array of face indices.
        deck_z: Z-level of the deck.
        z_tolerance: Tolerance for face membership.

    Returns:
        List of 2D polygons (each a list of [x, y] points).
    """
    polygons = []

    for face in faces:
        face_verts = vertices[face]
        face_z = face_verts[:, 2]

        # Check if this face is roughly horizontal and at deck level
        z_range = face_z.max() - face_z.min()
        z_mean = face_z.mean()

        if z_range < z_tolerance * 0.5 and abs(z_mean - deck_z) < z_tolerance:
            poly_2d = [[float(v[0]), float(v[1])] for v in face_verts]
            if len(poly_2d) >= 3:
                polygons.append(poly_2d)

    return polygons


def _merge_nearby_polygons(
    polygons: list[list[list[float]]],
    distance_threshold: float = 100.0,
) -> list[list[list[float]]]:
    """Merge small triangular faces into larger zone polygons using bounding box overlap.

    This is a simplified approach: group polygons whose bounding boxes overlap
    or are within distance_threshold, then compute the convex hull of each group.

    Args:
        polygons: List of 2D polygons.
        distance_threshold: Max gap between bounding boxes to merge.

    Returns:
        List of merged polygons.
    """
    if not polygons:
        return []

    # Compute bounding boxes
    bboxes = []
    for poly in polygons:
        xs = [p[0] for p in poly]
        ys = [p[1] for p in poly]
        bboxes.append((min(xs), min(ys), max(xs), max(ys)))

    # Union-Find grouping
    n = len(polygons)
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[ra] = rb

    for i in range(n):
        for j in range(i + 1, n):
            b1 = bboxes[i]
            b2 = bboxes[j]
            # Check bounding box proximity
            dx = max(0, max(b1[0], b2[0]) - min(b1[2], b2[2]))
            dy = max(0, max(b1[1], b2[1]) - min(b1[3], b2[3]))
            if math.sqrt(dx * dx + dy * dy) <= distance_threshold:
                union(i, j)

    # Group polygons
    groups: dict[int, list[list[list[float]]]] = {}
    for i in range(n):
        root = find(i)
        groups.setdefault(root, []).append(polygons[i])

    # Compute convex hull for each group
    merged = []
    for group_polys in groups.values():
        all_points = []
        for poly in group_polys:
            all_points.extend(poly)

        if len(all_points) < 3:
            continue

        hull = _convex_hull_2d(all_points)
        if len(hull) >= 3:
            area = _polygon_area(hull)
            if area >= MIN_ZONE_AREA_MM2:
                merged.append(hull)

    return merged


def _convex_hull_2d(points: list[list[float]]) -> list[list[float]]:
    """Compute 2D convex hull using Graham scan.

    Args:
        points: List of [x, y] points.

    Returns:
        Convex hull as list of [x, y] points in counter-clockwise order.
    """
    pts = sorted(set((p[0], p[1]) for p in points))
    if len(pts) < 3:
        return [[p[0], p[1]] for p in pts]

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])

    # Build lower hull
    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    # Build upper hull
    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    hull = lower[:-1] + upper[:-1]
    return [[p[0], p[1]] for p in hull]


def _try_import_trimesh():
    """Try to import trimesh, return None if unavailable."""
    try:
        import trimesh
        return trimesh
    except ImportError:
        return None


def parse_step(content: bytes, filename: str = "model.step") -> dict:
    """Parse a STEP (.step/.stp) file into zones and passages.

    Uses trimesh for mesh-based import. Falls back to basic text parsing
    if trimesh is unavailable.

    Args:
        content: Raw file bytes.
        filename: Original filename for format detection.

    Returns:
        Dict with keys: zones, passages, warnings, decks.
    """
    warnings: list[str] = []
    zones: list[dict] = []
    decks: list[dict] = []

    trimesh = _try_import_trimesh()

    if trimesh is not None:
        zones, decks, parse_warnings = _parse_with_trimesh(
            content, filename, file_format="step"
        )
        warnings.extend(parse_warnings)
    else:
        warnings.append(
            "trimesh ist nicht installiert. "
            "Installieren Sie es mit: pip install trimesh. "
            "Verwende vereinfachten Text-Parser."
        )
        zones, decks, parse_warnings = _parse_step_text(content)
        warnings.extend(parse_warnings)

    if not zones:
        raise ValueError(
            "Keine Zonen in der STEP-Datei gefunden. "
            "Die Datei enthält möglicherweise keine erkennbaren Flächen."
        )

    passages = _detect_passages_from_proximity(zones)

    return {
        "zones": zones,
        "passages": passages,
        "warnings": warnings,
        "decks": [{"z_mm": d.z_mm, "name": d.name, "face_count": d.face_count}
                  for d in (decks if isinstance(decks[0], DeckLevel) else [])]
                 if decks and isinstance(decks[0], DeckLevel) else decks,
    }


def parse_iges(content: bytes, filename: str = "model.iges") -> dict:
    """Parse an IGES (.iges/.igs) file into zones and passages.

    IGES is a text-based format. We parse entity records to extract
    surfaces and curves, then project to 2D zones.

    Args:
        content: Raw file bytes.
        filename: Original filename for format detection.

    Returns:
        Dict with keys: zones, passages, warnings, decks.
    """
    warnings: list[str] = []
    zones: list[dict] = []
    decks: list[dict] = []

    trimesh = _try_import_trimesh()

    if trimesh is not None:
        zones, decks, parse_warnings = _parse_with_trimesh(
            content, filename, file_format="iges"
        )
        warnings.extend(parse_warnings)
    else:
        warnings.append(
            "trimesh ist nicht installiert. Verwende IGES-Text-Parser."
        )
        zones, decks, parse_warnings = _parse_iges_text(content)
        warnings.extend(parse_warnings)

    if not zones:
        raise ValueError(
            "Keine Zonen in der IGES-Datei gefunden. "
            "Die Datei enthält möglicherweise keine erkennbaren Flächen oder Kurven."
        )

    passages = _detect_passages_from_proximity(zones)

    return {
        "zones": zones,
        "passages": passages,
        "warnings": warnings,
        "decks": [{"z_mm": d.z_mm, "name": d.name, "face_count": d.face_count}
                  for d in (decks if isinstance(decks[0], DeckLevel) else [])]
                 if decks and isinstance(decks[0], DeckLevel) else decks,
    }


def _parse_with_trimesh(
    content: bytes,
    filename: str,
    file_format: str,
) -> tuple[list[dict], list[DeckLevel], list[str]]:
    """Parse STEP or IGES using trimesh.

    Args:
        content: Raw file bytes.
        filename: Original filename.
        file_format: 'step' or 'iges'.

    Returns:
        Tuple of (zones, deck_levels, warnings).
    """
    import trimesh

    warnings: list[str] = []
    suffix = ".step" if file_format == "step" else ".igs"

    # trimesh needs a file on disk for STEP/IGES
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as tmp:
        tmp.write(content)
        tmp_path = tmp.name

    try:
        scene = trimesh.load(tmp_path, force="scene")
    except Exception as e:
        warnings.append(f"Fehler beim Laden der {file_format.upper()}-Datei: {e}")
        return [], [], warnings
    finally:
        try:
            os.unlink(tmp_path)
        except OSError:
            pass

    # Extract all meshes from the scene
    meshes = []
    mesh_names = []

    if isinstance(scene, trimesh.Scene):
        for name, geometry in scene.geometry.items():
            if isinstance(geometry, trimesh.Trimesh):
                meshes.append(geometry)
                mesh_names.append(name)
    elif isinstance(scene, trimesh.Trimesh):
        meshes.append(scene)
        mesh_names.append(filename)

    if not meshes:
        warnings.append(
            f"Keine 3D-Körper in der {file_format.upper()}-Datei erkannt."
        )
        return [], [], warnings

    # Collect Z-values of horizontal faces for deck detection
    all_z_values: list[float] = []
    all_bodies: list[ExtractedBody] = []

    for mesh, mesh_name in zip(meshes, mesh_names):
        vertices = mesh.vertices
        faces = mesh.faces
        normals = mesh.face_normals if hasattr(mesh, 'face_normals') else None

        # Find horizontal faces (normal pointing up/down)
        if normals is not None:
            for fi, normal in enumerate(normals):
                if abs(abs(normal[2]) - 1.0) < 0.1:  # Nearly vertical normal
                    face_verts = vertices[faces[fi]]
                    z_mean = float(face_verts[:, 2].mean())
                    all_z_values.append(z_mean)

        # Get the 2D bounding polygon for this body
        bounds = mesh.bounds  # [[xmin,ymin,zmin],[xmax,ymax,zmax]]
        z_min = float(bounds[0][2])
        z_max = float(bounds[1][2])

        # Project to 2D using the convex hull of XY coordinates
        xy_points = [[float(v[0]), float(v[1])] for v in vertices]
        hull = _convex_hull_2d(xy_points)

        if len(hull) >= 3:
            body = ExtractedBody(
                name=mesh_name,
                vertices_2d=hull,
                z_min=z_min,
                z_max=z_max,
                area_mm2=_polygon_area(hull),
                source_name=mesh_name,
            )
            all_bodies.append(body)

    # Detect deck levels
    deck_levels = detect_deck_levels(all_z_values)

    # Assign bodies to deck levels
    for body in all_bodies:
        body_z_mid = (body.z_min + body.z_max) / 2
        best_deck = min(deck_levels, key=lambda d: abs(d.z_mm - body_z_mid))
        body.deck_z = best_deck.z_mm

    # Convert bodies to zones
    zones = _bodies_to_zones(all_bodies, warnings)

    return zones, deck_levels, warnings


def _parse_step_text(content: bytes) -> tuple[list[dict], list[DeckLevel], list[str]]:
    """Fallback text-based STEP parser.

    Extracts basic geometric data from STEP file text representation.
    This is a simplified parser that looks for CLOSED_SHELL and
    ADVANCED_FACE entities.

    Args:
        content: Raw STEP file bytes.

    Returns:
        Tuple of (zones, deck_levels, warnings).
    """
    warnings: list[str] = []
    zones: list[dict] = []

    try:
        text = content.decode("utf-8", errors="replace")
    except Exception:
        warnings.append("STEP-Datei konnte nicht als Text gelesen werden.")
        return [], [], warnings

    # Look for CARTESIAN_POINT entries to extract coordinates
    points_3d: list[tuple[float, float, float]] = []
    lines = text.split("\n")

    for line in lines:
        line = line.strip()
        if "CARTESIAN_POINT" in line and "(" in line:
            try:
                # Extract coordinates from CARTESIAN_POINT('',(...))
                paren_start = line.index("(", line.index("CARTESIAN_POINT"))
                # Find the inner parentheses with actual numbers
                inner_start = line.index("(", paren_start + 1)
                inner_end = line.index(")", inner_start)
                coords_str = line[inner_start + 1:inner_end]
                coords = [float(c.strip()) for c in coords_str.split(",")]
                if len(coords) >= 3:
                    points_3d.append((coords[0], coords[1], coords[2]))
                elif len(coords) == 2:
                    points_3d.append((coords[0], coords[1], 0.0))
            except (ValueError, IndexError):
                continue

    if not points_3d:
        warnings.append(
            "Keine Koordinaten in der STEP-Datei gefunden. "
            "Vereinfachter Parser benötigt CARTESIAN_POINT-Einträge."
        )
        return [], [], warnings

    # Extract Z-values for deck detection
    z_values = [p[2] for p in points_3d]
    deck_levels = detect_deck_levels(z_values)

    # Project points to 2D and create zones using clustering
    xy_points = [[p[0], p[1]] for p in points_3d]

    # Try to detect closed shells / bodies by looking for entity references
    body_names: list[str] = []
    for line in lines:
        if "CLOSED_SHELL" in line or "MANIFOLD_SOLID" in line:
            # Try to extract name
            if "'" in line:
                try:
                    name_start = line.index("'") + 1
                    name_end = line.index("'", name_start)
                    name = line[name_start:name_end]
                    if name:
                        body_names.append(name)
                except (ValueError, IndexError):
                    pass

    # Create a single zone from all points as fallback
    if len(xy_points) >= 3:
        hull = _convex_hull_2d(xy_points)
        if len(hull) >= 3:
            area = _polygon_area(hull)
            centroid = _polygon_centroid(hull)
            zone_type = classify_zone_by_name(body_names[0]) if body_names else None
            if zone_type is None:
                zone_type = classify_zone_by_geometry(area, centroid)

            zones.append({
                "name": body_names[0] if body_names else zone_type,
                "zone_type": zone_type,
                "polygon": hull,
                "is_crew_area": False,
                "is_guest_area": zone_type not in ("engine", "storage", "crew_quarters"),
                "visibility_angle": None,
                "properties": {"source": "step_text_parser"},
            })

            warnings.append(
                "Vereinfachter STEP-Parser: Nur grundlegende Geometrie erkannt. "
                "Für bessere Ergebnisse installieren Sie trimesh."
            )

    return zones, deck_levels, warnings


def _parse_iges_text(content: bytes) -> tuple[list[dict], list[DeckLevel], list[str]]:
    """Text-based IGES parser.

    IGES files have a defined text format with 80-character fixed-width lines.
    Sections: S (Start), G (Global), D (Directory Entry), P (Parameter Data), T (Terminate).

    We focus on entity types:
    - 110: Line
    - 116: Point
    - 126: Rational B-Spline Curve
    - 128: Rational B-Spline Surface
    - 142: Curve on Surface
    - 144: Trimmed Parametric Surface

    Args:
        content: Raw IGES file bytes.

    Returns:
        Tuple of (zones, deck_levels, warnings).
    """
    warnings: list[str] = []

    try:
        text = content.decode("ascii", errors="replace")
    except Exception:
        warnings.append("IGES-Datei konnte nicht als Text gelesen werden.")
        return [], [], warnings

    lines = text.split("\n")
    if not lines:
        warnings.append("Leere IGES-Datei.")
        return [], [], warnings

    # Validate IGES format: lines should be 80+ chars with section ID in col 73
    param_lines: list[str] = []
    dir_lines: list[str] = []

    for line in lines:
        if len(line) < 73:
            continue
        section = line[72] if len(line) > 72 else ""
        if section == "D":
            dir_lines.append(line)
        elif section == "P":
            param_lines.append(line)

    if not dir_lines and not param_lines:
        # Might not be a proper IGES file - try to extract any coordinates
        warnings.append(
            "IGES-Dateiformat nicht erkannt. Versuche Koordinaten-Extraktion."
        )
        return _extract_coordinates_fallback(text, warnings)

    # Parse directory entries to find entity types
    entities: list[dict] = []
    for i in range(0, len(dir_lines) - 1, 2):
        try:
            entity_type = int(dir_lines[i][0:8].strip())
            param_ptr = int(dir_lines[i][8:16].strip())
            line_count = int(dir_lines[i + 1][24:32].strip()) if len(dir_lines[i + 1]) > 31 else 1

            # Try to get entity label
            label = dir_lines[i + 1][56:64].strip() if len(dir_lines[i + 1]) > 63 else ""

            entities.append({
                "type": entity_type,
                "param_ptr": param_ptr,
                "line_count": line_count,
                "label": label,
            })
        except (ValueError, IndexError):
            continue

    # Extract coordinates from parameter data
    all_points_3d: list[tuple[float, float, float]] = []

    # Concatenate all parameter lines into one string for parsing
    param_text = ""
    for line in param_lines:
        param_text += line[0:64].strip()

    # Split by record delimiter ';' and parameter delimiter ','
    records = param_text.split(";")

    for record in records:
        parts = record.split(",")
        # Try to extract triplets of floats (x, y, z coordinates)
        floats = []
        for part in parts:
            try:
                # IGES uses 'D' for exponent sometimes
                val = float(part.strip().replace("D", "E"))
                floats.append(val)
            except (ValueError, AttributeError):
                continue

        # Extract coordinate triplets
        for k in range(0, len(floats) - 2, 3):
            all_points_3d.append((floats[k], floats[k + 1], floats[k + 2]))

    if not all_points_3d:
        warnings.append("Keine Koordinaten in der IGES-Datei gefunden.")
        return [], [], warnings

    # Detect deck levels
    z_values = [p[2] for p in all_points_3d]
    deck_levels = detect_deck_levels(z_values)

    # Group points by entity for zone detection
    # For now, create zones from clustered point groups
    xy_points = [[p[0], p[1]] for p in all_points_3d]

    # Try to form zones from entity groupings
    entity_polygons: list[list[list[float]]] = []
    point_entity_types = {110, 116, 126, 128, 142, 144}

    # Build groups of XY points per entity type cluster
    current_group: list[list[float]] = []
    for i, ent in enumerate(entities):
        if ent["type"] in point_entity_types or ent["type"] == 110:
            # Collect associated points
            pass

    # Fallback: merge all points into convex hull zones
    if len(xy_points) >= 3:
        hull = _convex_hull_2d(xy_points)
        if len(hull) >= 3:
            area = _polygon_area(hull)
            centroid = _polygon_centroid(hull)

            # Try to split into sub-regions if the hull is large
            zones = _split_hull_into_zones(hull, area, entities, warnings)
            if not zones:
                zone_type = classify_zone_by_geometry(area, centroid)
                zones = [{
                    "name": zone_type,
                    "zone_type": zone_type,
                    "polygon": hull,
                    "is_crew_area": False,
                    "is_guest_area": zone_type not in ("engine", "storage", "crew_quarters"),
                    "visibility_angle": None,
                    "properties": {"source": "iges_text_parser"},
                }]

            warnings.append(
                "IGES-Text-Parser: Vereinfachte Geometrieerkennung. "
                "Zonengrenzen sind approximiert."
            )

            return zones, deck_levels, warnings

    return [], deck_levels, warnings


def _extract_coordinates_fallback(
    text: str,
    warnings: list[str],
) -> tuple[list[dict], list[DeckLevel], list[str]]:
    """Last-resort coordinate extraction from unstructured text.

    Looks for numeric triplets that could be 3D coordinates.
    """
    import re

    pattern = r"(-?\d+\.?\d*(?:[eEdD][+-]?\d+)?)"
    all_numbers = re.findall(pattern, text)

    floats = []
    for n in all_numbers:
        try:
            floats.append(float(n.replace("D", "E")))
        except ValueError:
            continue

    if len(floats) < 6:
        return [], [], warnings

    # Take coordinate triplets
    points_3d = []
    for i in range(0, len(floats) - 2, 3):
        points_3d.append((floats[i], floats[i + 1], floats[i + 2]))

    z_values = [p[2] for p in points_3d]
    deck_levels = detect_deck_levels(z_values)

    xy_points = [[p[0], p[1]] for p in points_3d]
    if len(xy_points) >= 3:
        hull = _convex_hull_2d(xy_points)
        if len(hull) >= 3:
            area = _polygon_area(hull)
            centroid = _polygon_centroid(hull)
            zone_type = classify_zone_by_geometry(area, centroid)

            zones = [{
                "name": zone_type,
                "zone_type": zone_type,
                "polygon": hull,
                "is_crew_area": False,
                "is_guest_area": True,
                "visibility_angle": None,
                "properties": {"source": "iges_fallback_parser"},
            }]
            return zones, deck_levels, warnings

    return [], [], warnings


def _split_hull_into_zones(
    hull: list[list[float]],
    total_area: float,
    entities: list[dict],
    warnings: list[str],
) -> list[dict]:
    """Try to split a large convex hull into sub-zones.

    Uses entity labels if available, otherwise returns empty
    to let the caller create a single zone.
    """
    zones = []

    # Check if any entities have useful labels
    labeled_entities = [e for e in entities if e.get("label")]
    if not labeled_entities:
        return []

    # Group by label
    label_groups: dict[str, int] = {}
    for ent in labeled_entities:
        label = ent["label"]
        label_groups[label] = label_groups.get(label, 0) + 1

    if len(label_groups) < 2:
        return []

    # If we have multiple labels, subdivide the hull roughly
    # This is approximate - real zone boundaries need the full surface data
    xs = [p[0] for p in hull]
    ys = [p[1] for p in hull]
    x_min, x_max = min(xs), max(xs)
    y_min, y_max = min(ys), max(ys)

    n_zones = min(len(label_groups), 6)
    zone_width = (x_max - x_min) / n_zones

    zone_counter: dict[str, int] = {}
    for i, (label, _) in enumerate(list(label_groups.items())[:n_zones]):
        zx_min = x_min + i * zone_width
        zx_max = zx_min + zone_width

        polygon = [
            [zx_min, y_min],
            [zx_max, y_min],
            [zx_max, y_max],
            [zx_min, y_max],
        ]
        area = _polygon_area(polygon)
        centroid = _polygon_centroid(polygon)

        zone_type = classify_zone_by_name(label)
        if zone_type is None:
            zone_type = classify_zone_by_geometry(area, centroid)

        count = zone_counter.get(zone_type, 0) + 1
        zone_counter[zone_type] = count
        name = f"{zone_type}_{count}" if count > 1 else zone_type

        zones.append({
            "name": name,
            "zone_type": zone_type,
            "polygon": polygon,
            "is_crew_area": zone_type == "crew_quarters",
            "is_guest_area": zone_type not in ("engine", "storage", "crew_quarters"),
            "visibility_angle": None,
            "properties": {"source": "iges_text_parser", "label": label},
        })

    return zones


def _bodies_to_zones(
    bodies: list[ExtractedBody],
    warnings: list[str],
) -> list[dict]:
    """Convert extracted 3D bodies into zone dicts.

    Args:
        bodies: List of ExtractedBody objects.
        warnings: Warning list to append to.

    Returns:
        List of zone dicts matching the ZoneData schema.
    """
    zones = []
    zone_counters: dict[str, int] = {}

    for body in bodies:
        if body.area_mm2 < MIN_ZONE_AREA_MM2:
            continue

        polygon = _simplify_polygon(body.vertices_2d)
        if len(polygon) < 3:
            continue

        centroid = _polygon_centroid(polygon)

        # Try name-based classification first
        zone_type = classify_zone_by_name(body.source_name)
        if zone_type is None:
            zone_type = classify_zone_by_geometry(body.area_mm2, centroid)

        count = zone_counters.get(zone_type, 0) + 1
        zone_counters[zone_type] = count
        name = f"{zone_type}_{count}" if count > 1 else zone_type

        height_mm = body.z_max - body.z_min if body.z_max > body.z_min else None

        zones.append({
            "name": name,
            "zone_type": zone_type,
            "polygon": polygon,
            "height_mm": height_mm,
            "is_crew_area": zone_type == "crew_quarters",
            "is_guest_area": zone_type not in ("engine", "storage", "crew_quarters"),
            "visibility_angle": None,
            "properties": {
                "source_body": body.source_name,
                "deck_z_mm": body.deck_z,
                "area_sqm": round(body.area_mm2 / 1_000_000, 2),
            },
        })

    if not zones and bodies:
        warnings.append(
            f"{len(bodies)} Körper gefunden, aber keine erfüllen die "
            f"Mindestfläche von {MIN_ZONE_AREA_MM2 / 1_000_000:.1f} m²."
        )

    return zones
