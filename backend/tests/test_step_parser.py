"""Tests for STEP/IGES CAD import parser.

Tests cover:
- Deck level detection (Z-clustering)
- Zone classification by name and geometry
- Polygon operations (area, centroid, convex hull, simplification)
- Passage detection from proximity
- STEP text parsing
- IGES text parsing
- Empty/invalid file handling
- Body-to-zone conversion
- Coordinate fallback extraction
"""
import math
import pytest

from app.services.cad_import.step_parser import (
    DECK_Z_TOLERANCE_MM,
    MIN_ZONE_AREA_MM2,
    DeckLevel,
    ExtractedBody,
    _bodies_to_zones,
    _cluster_z_values,
    _convex_hull_2d,
    _detect_passages_from_proximity,
    _extract_coordinates_fallback,
    _merge_nearby_polygons,
    _parse_iges_text,
    _parse_step_text,
    _polygon_area,
    _polygon_centroid,
    _simplify_polygon,
    classify_zone_by_geometry,
    classify_zone_by_name,
    detect_deck_levels,
    parse_iges,
    parse_step,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _make_rect(x1, y1, x2, y2):
    """Create a rectangular polygon in counter-clockwise order."""
    return [[x1, y1], [x2, y1], [x2, y2], [x1, y2]]


def _rect_area(x1, y1, x2, y2):
    return abs((x2 - x1) * (y2 - y1))


# ---------------------------------------------------------------------------
# 1. Deck level detection
# ---------------------------------------------------------------------------

class TestDeckDetection:
    def test_single_deck(self):
        """Single cluster of Z-values produces one deck."""
        z_values = [0.0, 10.0, 5.0, 15.0, 20.0]
        decks = detect_deck_levels(z_values)
        assert len(decks) == 1
        assert decks[0].name == "Hauptdeck"

    def test_two_decks(self):
        """Two well-separated Z-clusters produce two decks."""
        z_values = [0.0, 50.0, 25.0, 2000.0, 2050.0, 2025.0]
        decks = detect_deck_levels(z_values)
        assert len(decks) == 2
        assert decks[0].name == "Unterdeck"
        assert decks[1].name == "Hauptdeck"
        assert decks[0].z_mm < decks[1].z_mm

    def test_three_decks(self):
        """Three Z-clusters produce three named decks."""
        z_values = [0.0, 50.0, 2000.0, 2050.0, 4000.0, 4050.0]
        decks = detect_deck_levels(z_values)
        assert len(decks) == 3
        assert decks[0].name == "Unterdeck"
        assert decks[1].name == "Hauptdeck"
        assert decks[2].name == "Oberdeck"

    def test_empty_z_values(self):
        """Empty Z-values list produces default single deck."""
        decks = detect_deck_levels([])
        assert len(decks) == 1
        assert decks[0].name == "Hauptdeck"
        assert decks[0].z_mm == 0.0

    def test_z_clustering_tolerance(self):
        """Points within tolerance are grouped into same deck."""
        tolerance = DECK_Z_TOLERANCE_MM
        z_values = [100.0, 100.0 + tolerance * 0.5, 100.0 + tolerance * 0.9]
        decks = detect_deck_levels(z_values, tolerance=tolerance)
        assert len(decks) == 1

    def test_z_clustering_separation(self):
        """Points beyond tolerance form separate decks."""
        tolerance = DECK_Z_TOLERANCE_MM
        z_values = [100.0, 100.0 + tolerance * 3]
        decks = detect_deck_levels(z_values, tolerance=tolerance)
        assert len(decks) == 2

    def test_face_counts(self):
        """Each deck reports correct face count."""
        z_values = [0.0, 10.0, 20.0, 2000.0]
        decks = detect_deck_levels(z_values)
        assert len(decks) == 2
        assert decks[0].face_count == 3  # 0, 10, 20
        assert decks[1].face_count == 1  # 2000


# ---------------------------------------------------------------------------
# 2. Zone classification
# ---------------------------------------------------------------------------

class TestZoneClassification:
    def test_classify_by_name_exact(self):
        """Exact name matches return correct zone type."""
        assert classify_zone_by_name("CABIN") == "cabin"
        assert classify_zone_by_name("SALON") == "salon"
        assert classify_zone_by_name("ENGINE") == "engine"

    def test_classify_by_name_substring(self):
        """Substrings in body names are recognized."""
        assert classify_zone_by_name("Main_CABIN_port") == "cabin"
        assert classify_zone_by_name("upper_flybridge_01") == "flybridge"
        assert classify_zone_by_name("aft_cockpit") == "cockpit"
        assert classify_zone_by_name("crew_area_01") == "crew_quarters"

    def test_classify_by_name_case_insensitive(self):
        """Classification is case-insensitive."""
        assert classify_zone_by_name("helm") == "helm"
        assert classify_zone_by_name("Helm") == "helm"
        assert classify_zone_by_name("HELM") == "helm"

    def test_classify_by_name_no_match(self):
        """Unrecognized names return None."""
        assert classify_zone_by_name("body_42") is None
        assert classify_zone_by_name("solid_part") is None

    def test_classify_by_geometry_small(self):
        """Small areas classify as storage or head."""
        assert classify_zone_by_geometry(500_000, (6000, 2000)) == "storage"
        assert classify_zone_by_geometry(1_500_000, (6000, 2000)) == "head"

    def test_classify_by_geometry_aft(self):
        """Aft-positioned zones classify as cockpit or engine."""
        boat_len = 12000.0
        # x_ratio > 0.75, large area -> cockpit
        assert classify_zone_by_geometry(
            5_000_000, (10000, 2000), boat_length_mm=boat_len
        ) == "cockpit"
        # x_ratio > 0.75, small area -> engine
        assert classify_zone_by_geometry(
            3_000_000, (10000, 2000), boat_length_mm=boat_len
        ) == "engine"

    def test_classify_by_geometry_forward(self):
        """Forward-positioned zones classify as cabin."""
        assert classify_zone_by_geometry(
            5_000_000, (1000, 2000), boat_length_mm=12000.0
        ) == "cabin"

    def test_classify_by_geometry_midship_large(self):
        """Large midship zones classify as salon."""
        assert classify_zone_by_geometry(
            10_000_000, (6000, 2000), boat_length_mm=12000.0
        ) == "salon"


# ---------------------------------------------------------------------------
# 3. Polygon operations
# ---------------------------------------------------------------------------

class TestPolygonOps:
    def test_polygon_area_rectangle(self):
        """Rectangle area calculation is correct."""
        poly = _make_rect(0, 0, 3000, 2000)
        assert _polygon_area(poly) == pytest.approx(6_000_000.0)

    def test_polygon_area_triangle(self):
        """Triangle area is correct."""
        poly = [[0, 0], [4000, 0], [2000, 3000]]
        assert _polygon_area(poly) == pytest.approx(6_000_000.0)

    def test_polygon_area_degenerate(self):
        """Fewer than 3 points returns 0."""
        assert _polygon_area([[0, 0], [100, 100]]) == 0.0
        assert _polygon_area([]) == 0.0

    def test_polygon_centroid(self):
        """Centroid of a rectangle is at center."""
        poly = _make_rect(0, 0, 4000, 2000)
        cx, cy = _polygon_centroid(poly)
        assert cx == pytest.approx(2000.0)
        assert cy == pytest.approx(1000.0)

    def test_convex_hull_rectangle(self):
        """Convex hull of rectangle vertices reproduces the rectangle."""
        points = [[0, 0], [1000, 0], [1000, 500], [0, 500]]
        hull = _convex_hull_2d(points)
        assert len(hull) == 4
        assert _polygon_area(hull) == pytest.approx(500_000.0)

    def test_convex_hull_with_interior_points(self):
        """Interior points are excluded from hull."""
        points = [
            [0, 0], [1000, 0], [1000, 1000], [0, 1000],
            [500, 500],  # interior point
        ]
        hull = _convex_hull_2d(points)
        assert len(hull) == 4

    def test_simplify_polygon_keeps_corners(self):
        """Rectangle corners survive simplification."""
        poly = _make_rect(0, 0, 5000, 3000)
        simplified = _simplify_polygon(poly, tolerance=50.0)
        assert len(simplified) >= 4

    def test_simplify_polygon_removes_collinear(self):
        """Collinear intermediate points are removed."""
        poly = [
            [0, 0], [1000, 0], [2000, 0], [3000, 0],  # bottom edge w/ extras
            [3000, 2000], [0, 2000],
        ]
        simplified = _simplify_polygon(poly, tolerance=50.0)
        assert len(simplified) < len(poly)


# ---------------------------------------------------------------------------
# 4. Passage detection
# ---------------------------------------------------------------------------

class TestPassageDetection:
    def test_adjacent_zones_create_passage(self):
        """Two zones with close boundaries produce a passage."""
        zones = [
            {"name": "salon", "polygon": _make_rect(0, 0, 3000, 2000)},
            {"name": "pantry", "polygon": _make_rect(3050, 0, 6000, 2000)},
        ]
        passages = _detect_passages_from_proximity(zones, tolerance=200.0)
        assert len(passages) == 1
        assert passages[0]["from_zone"] == "salon"
        assert passages[0]["to_zone"] == "pantry"

    def test_distant_zones_no_passage(self):
        """Zones far apart produce no passage."""
        zones = [
            {"name": "salon", "polygon": _make_rect(0, 0, 3000, 2000)},
            {"name": "cabin", "polygon": _make_rect(5000, 0, 8000, 2000)},
        ]
        passages = _detect_passages_from_proximity(zones, tolerance=200.0)
        assert len(passages) == 0

    def test_multiple_passages(self):
        """Three zones in a row produce two passages."""
        zones = [
            {"name": "cabin", "polygon": _make_rect(0, 0, 2000, 2000)},
            {"name": "salon", "polygon": _make_rect(2050, 0, 5000, 2000)},
            {"name": "cockpit", "polygon": _make_rect(5050, 0, 8000, 2000)},
        ]
        passages = _detect_passages_from_proximity(zones, tolerance=200.0)
        assert len(passages) == 2

    def test_empty_zones_no_crash(self):
        """Empty zone list produces no passages."""
        passages = _detect_passages_from_proximity([], tolerance=200.0)
        assert passages == []


# ---------------------------------------------------------------------------
# 5. STEP text parser
# ---------------------------------------------------------------------------

class TestStepTextParser:
    def test_valid_cartesian_points(self):
        """STEP text with CARTESIAN_POINT entries produces zones."""
        step_text = (
            "ISO-10303-21;\n"
            "HEADER;\n"
            "ENDSEC;\n"
            "DATA;\n"
            "#1=CARTESIAN_POINT('',(0.0,0.0,0.0));\n"
            "#2=CARTESIAN_POINT('',(5000.0,0.0,0.0));\n"
            "#3=CARTESIAN_POINT('',(5000.0,3000.0,0.0));\n"
            "#4=CARTESIAN_POINT('',(0.0,3000.0,0.0));\n"
            "#5=CARTESIAN_POINT('',(2500.0,1500.0,2000.0));\n"
            "ENDSEC;\n"
            "END-ISO-10303-21;\n"
        )
        content = step_text.encode("utf-8")
        zones, decks, warnings = _parse_step_text(content)
        assert len(zones) >= 1
        assert zones[0]["zone_type"] in (
            "salon", "cockpit", "cabin", "pantry", "head", "storage", "engine", "helm"
        )

    def test_step_with_named_body(self):
        """STEP text with CLOSED_SHELL name hint classifies zone."""
        step_text = (
            "ISO-10303-21;\n"
            "DATA;\n"
            "#10=CLOSED_SHELL('SALON',(#11,#12));\n"
            "#1=CARTESIAN_POINT('',(0.0,0.0,0.0));\n"
            "#2=CARTESIAN_POINT('',(8000.0,0.0,0.0));\n"
            "#3=CARTESIAN_POINT('',(8000.0,4000.0,0.0));\n"
            "#4=CARTESIAN_POINT('',(0.0,4000.0,0.0));\n"
            "ENDSEC;\n"
        )
        content = step_text.encode("utf-8")
        zones, _, _ = _parse_step_text(content)
        assert len(zones) >= 1
        assert zones[0]["zone_type"] == "salon"

    def test_step_no_coordinates(self):
        """STEP file with no coordinates produces empty result + warning."""
        step_text = "ISO-10303-21;\nHEADER;\nENDSEC;\nDATA;\nENDSEC;\n"
        zones, _, warnings = _parse_step_text(step_text.encode("utf-8"))
        assert len(zones) == 0
        assert any("Keine Koordinaten" in w for w in warnings)


# ---------------------------------------------------------------------------
# 6. IGES text parser
# ---------------------------------------------------------------------------

class TestIgesTextParser:
    def _make_iges_content(self, param_data: str, dir_entries: list[str] = None) -> bytes:
        """Build a minimal IGES file with given parameter data."""
        lines = []
        # Start section
        lines.append(f"{'Test IGES file':<72}S      1")
        # Global section
        lines.append(f"{'1H,,1H;,7Hmodel ;,4Htest,32,38,6,308,15,,1.0,1,2HMM,1,0.1;':<72}G      1")
        # Directory entries (if provided)
        if dir_entries:
            for i, de in enumerate(dir_entries):
                lines.append(f"{de:<72}D{i+1:7d}")
        # Parameter data
        for i, pd_line in enumerate(param_data.split("\n")):
            if pd_line.strip():
                lines.append(f"{pd_line:<72}P{i+1:7d}")
        # Terminate
        lines.append(f"{'S      1G      1D      0P      0':<72}T      1")
        return "\n".join(lines).encode("ascii")

    def test_iges_with_coordinates(self):
        """IGES file with coordinate data produces zones."""
        # Simple parameter data with coordinate-like values
        param_data = "116,0.0,0.0,0.0;116,5000.0,0.0,0.0;116,5000.0,3000.0,0.0;116,0.0,3000.0,0.0;"
        content = self._make_iges_content(param_data)
        zones, decks, warnings = _parse_iges_text(content)
        assert len(zones) >= 1

    def test_iges_empty_file(self):
        """Empty IGES content produces warning."""
        zones, decks, warnings = _parse_iges_text(b"")
        assert len(zones) == 0
        assert any("Leere" in w or "nicht erkannt" in w for w in warnings)

    def test_iges_invalid_format(self):
        """Non-IGES text triggers fallback parser."""
        content = b"This is not an IGES file at all, just random text."
        zones, decks, warnings = _parse_iges_text(content)
        assert any("nicht erkannt" in w for w in warnings)


# ---------------------------------------------------------------------------
# 7. Empty / invalid file handling
# ---------------------------------------------------------------------------

class TestErrorHandling:
    def test_parse_step_empty_raises(self):
        """Empty STEP file raises ValueError."""
        with pytest.raises(ValueError, match="Keine Zonen"):
            parse_step(b"", filename="empty.step")

    def test_parse_iges_empty_raises(self):
        """Empty IGES file raises ValueError."""
        with pytest.raises(ValueError, match="Keine Zonen"):
            parse_iges(b"", filename="empty.igs")

    def test_parse_step_no_geometry_raises(self):
        """STEP with no parseable geometry raises ValueError."""
        content = b"ISO-10303-21;\nHEADER;\nENDSEC;\nDATA;\nENDSEC;\n"
        with pytest.raises(ValueError, match="Keine Zonen"):
            parse_step(content, filename="empty.step")

    def test_parse_step_returns_expected_keys(self):
        """Valid STEP parse returns dict with required keys."""
        step_text = (
            "#1=CARTESIAN_POINT('',(0.0,0.0,0.0));\n"
            "#2=CARTESIAN_POINT('',(6000.0,0.0,0.0));\n"
            "#3=CARTESIAN_POINT('',(6000.0,4000.0,0.0));\n"
            "#4=CARTESIAN_POINT('',(0.0,4000.0,0.0));\n"
        )
        result = parse_step(step_text.encode("utf-8"), filename="test.step")
        assert "zones" in result
        assert "passages" in result
        assert "warnings" in result
        assert "decks" in result
        assert isinstance(result["zones"], list)
        assert isinstance(result["passages"], list)
        assert isinstance(result["warnings"], list)


# ---------------------------------------------------------------------------
# 8. Body-to-zone conversion
# ---------------------------------------------------------------------------

class TestBodiesToZones:
    def test_body_with_sufficient_area(self):
        """Body larger than MIN_ZONE_AREA converts to zone."""
        body = ExtractedBody(
            name="test_body",
            vertices_2d=_make_rect(0, 0, 3000, 2000),
            z_min=0, z_max=2000,
            area_mm2=6_000_000,
            source_name="CABIN_port",
        )
        warnings = []
        zones = _bodies_to_zones([body], warnings)
        assert len(zones) == 1
        assert zones[0]["zone_type"] == "cabin"
        assert zones[0]["height_mm"] == 2000.0

    def test_body_too_small_excluded(self):
        """Body smaller than MIN_ZONE_AREA is excluded with warning."""
        body = ExtractedBody(
            name="tiny",
            vertices_2d=_make_rect(0, 0, 100, 100),
            z_min=0, z_max=100,
            area_mm2=10_000,
            source_name="tiny_part",
        )
        warnings = []
        zones = _bodies_to_zones([body], warnings)
        assert len(zones) == 0
        assert any("Mindestfläche" in w for w in warnings)

    def test_multiple_bodies_unique_names(self):
        """Multiple bodies of same type get numbered names."""
        bodies = [
            ExtractedBody(
                name=f"cab_{i}",
                vertices_2d=_make_rect(i * 4000, 0, i * 4000 + 3000, 2000),
                z_min=0, z_max=2000,
                area_mm2=6_000_000,
                source_name=f"CABIN_{i}",
            )
            for i in range(3)
        ]
        warnings = []
        zones = _bodies_to_zones(bodies, warnings)
        assert len(zones) == 3
        names = [z["name"] for z in zones]
        assert len(set(names)) == 3  # all unique

    def test_crew_area_flag(self):
        """Crew quarters body sets is_crew_area flag."""
        body = ExtractedBody(
            name="crew",
            vertices_2d=_make_rect(0, 0, 3000, 2000),
            z_min=0, z_max=2000,
            area_mm2=6_000_000,
            source_name="CREW_quarters_aft",
        )
        warnings = []
        zones = _bodies_to_zones([body], warnings)
        assert len(zones) == 1
        assert zones[0]["is_crew_area"] is True
        assert zones[0]["is_guest_area"] is False


# ---------------------------------------------------------------------------
# 9. Merge nearby polygons
# ---------------------------------------------------------------------------

class TestMergePolygons:
    def test_overlapping_triangles_merge(self):
        """Adjacent triangles merge into one polygon."""
        t1 = [[0, 0], [2000, 0], [1000, 2000]]
        t2 = [[2000, 0], [4000, 0], [3000, 2000]]
        merged = _merge_nearby_polygons([t1, t2], distance_threshold=200.0)
        # Should merge into one or two polys depending on proximity
        assert len(merged) >= 1
        # Total area should be roughly preserved
        total_area = sum(_polygon_area(p) for p in merged)
        assert total_area > 0

    def test_distant_polygons_stay_separate(self):
        """Distant polygons remain separate."""
        p1 = _make_rect(0, 0, 1000, 1000)
        p2 = _make_rect(5000, 5000, 6000, 6000)
        merged = _merge_nearby_polygons([p1, p2], distance_threshold=100.0)
        assert len(merged) == 2

    def test_empty_input(self):
        """Empty input returns empty output."""
        assert _merge_nearby_polygons([]) == []


# ---------------------------------------------------------------------------
# 10. Coordinate fallback extraction
# ---------------------------------------------------------------------------

class TestCoordinateFallback:
    def test_extracts_from_numeric_text(self):
        """Numeric triplets in text are extracted as coordinates."""
        text = "some data 0.0 0.0 0.0 more text 5000.0 0.0 0.0 and 5000.0 3000.0 0.0 also 0.0 3000.0 0.0"
        warnings = []
        zones, decks, w = _extract_coordinates_fallback(text, warnings)
        assert len(zones) >= 1

    def test_insufficient_numbers(self):
        """Too few numbers produces no zones."""
        text = "hello 1.0 2.0"
        warnings = []
        zones, decks, w = _extract_coordinates_fallback(text, warnings)
        assert len(zones) == 0
