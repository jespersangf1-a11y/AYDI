"""Tests for the layout diff service.

Run with:
    PYTHONPATH=. pytest tests/test_layout_diff.py -v
"""
from tests.conftest import make_zone, make_passage
from app.services.diff.layout_diff import compute_layout_diff, _polygon_area


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def make_layout(zones=None, passages=None) -> dict:
    """Build a minimal layout dict."""
    return {"zones": zones or [], "passages": passages or []}


# ---------------------------------------------------------------------------
# Tests: identical and empty layouts
# ---------------------------------------------------------------------------

def test_identical_layouts():
    """Two identical layouts produce no changes and has_changes=False."""
    zones = [
        make_zone("Salon", "salon"),
        make_zone("Pantry", "pantry"),
    ]
    passages = [make_passage("Salon", "Pantry")]
    layout = make_layout(zones, passages)
    result = compute_layout_diff(layout, layout)

    assert result["summary"]["has_changes"] is False
    assert result["summary"]["zones_added"] == 0
    assert result["summary"]["zones_removed"] == 0
    assert result["summary"]["zones_modified"] == 0
    assert result["summary"]["passages_added"] == 0
    assert result["summary"]["passages_removed"] == 0
    assert result["summary"]["passages_modified"] == 0
    assert result["summary"]["zones_unchanged"] == 2
    assert set(result["zones"]["unchanged"]) == {"Salon", "Pantry"}


def test_empty_layouts():
    """Two empty layouts produce no changes."""
    result = compute_layout_diff(make_layout(), make_layout())

    assert result["summary"]["has_changes"] is False
    assert result["summary"]["total_area_change_sqm"] == 0.0
    assert result["zones"]["added"] == []
    assert result["zones"]["removed"] == []
    assert result["passages"]["added"] == []


# ---------------------------------------------------------------------------
# Tests: zone changes
# ---------------------------------------------------------------------------

def test_zone_added():
    """A zone present in B but not in A is detected in the added list."""
    zone_a = make_zone("Salon", "salon")
    zone_new = make_zone("Kabine", "cabin")
    layout_a = make_layout([zone_a])
    layout_b = make_layout([zone_a, zone_new])

    result = compute_layout_diff(layout_a, layout_b)

    assert result["summary"]["zones_added"] == 1
    assert result["summary"]["has_changes"] is True
    added_names = [e["name"] for e in result["zones"]["added"]]
    assert "Kabine" in added_names
    assert result["summary"]["zones_unchanged"] == 1


def test_zone_removed():
    """A zone present in A but not in B is detected in the removed list."""
    zone_a = make_zone("Salon", "salon")
    zone_removed = make_zone("Maschinenraum", "engine")
    layout_a = make_layout([zone_a, zone_removed])
    layout_b = make_layout([zone_a])

    result = compute_layout_diff(layout_a, layout_b)

    assert result["summary"]["zones_removed"] == 1
    assert result["summary"]["has_changes"] is True
    removed_names = [e["name"] for e in result["zones"]["removed"]]
    assert "Maschinenraum" in removed_names


def test_zone_modified_polygon():
    """A polygon change is detected and area_change_sqm is included."""
    poly_a = [[0, 0], [2000, 0], [2000, 2000], [0, 2000]]  # 4 000 000 mm²  = 4 m²
    poly_b = [[0, 0], [3000, 0], [3000, 2000], [0, 2000]]  # 6 000 000 mm²  = 6 m²

    zone_a = make_zone("Salon", "salon", polygon=poly_a)
    zone_b = make_zone("Salon", "salon", polygon=poly_b)
    layout_a = make_layout([zone_a])
    layout_b = make_layout([zone_b])

    result = compute_layout_diff(layout_a, layout_b)

    assert result["summary"]["zones_modified"] == 1
    mod = result["zones"]["modified"][0]
    assert mod["name"] == "Salon"

    poly_change = next(c for c in mod["changes"] if c["field"] == "polygon")
    # area_change_sqm should be positive (larger polygon in B)
    assert poly_change["area_change_sqm"] > 0
    assert "area_change_sqm" in poly_change


def test_zone_modified_type():
    """A zone_type change is detected in the modified list."""
    zone_a = make_zone("Raum", "salon")
    zone_b = make_zone("Raum", "cabin")   # same name, different type
    layout_a = make_layout([zone_a])
    layout_b = make_layout([zone_b])

    result = compute_layout_diff(layout_a, layout_b)

    assert result["summary"]["zones_modified"] == 1
    mod = result["zones"]["modified"][0]
    type_change = next(c for c in mod["changes"] if c["field"] == "zone_type")
    assert type_change["old"] == "salon"
    assert type_change["new"] == "cabin"


def test_zone_renamed():
    """A renamed zone appears as one removal and one addition (different keys)."""
    zone_old = make_zone("Wohnraum", "salon")
    zone_new = make_zone("Salon", "salon")
    layout_a = make_layout([zone_old])
    layout_b = make_layout([zone_new])

    result = compute_layout_diff(layout_a, layout_b)

    assert result["summary"]["zones_added"] == 1
    assert result["summary"]["zones_removed"] == 1
    assert result["summary"]["zones_modified"] == 0
    assert result["summary"]["zones_unchanged"] == 0


# ---------------------------------------------------------------------------
# Tests: passage changes
# ---------------------------------------------------------------------------

def test_passage_added():
    """A passage present in B but not in A is detected in the added list."""
    passage_new = make_passage("Salon", "Kabine")
    layout_a = make_layout()
    layout_b = make_layout(passages=[passage_new])

    result = compute_layout_diff(layout_a, layout_b)

    assert result["summary"]["passages_added"] == 1
    assert result["summary"]["has_changes"] is True
    added = result["passages"]["added"][0]
    assert added["from_zone"] == "Salon"
    assert added["to_zone"] == "Kabine"


def test_passage_removed():
    """A passage present in A but not in B is detected in the removed list."""
    passage_old = make_passage("Cockpit", "Salon")
    layout_a = make_layout(passages=[passage_old])
    layout_b = make_layout()

    result = compute_layout_diff(layout_a, layout_b)

    assert result["summary"]["passages_removed"] == 1
    removed = result["passages"]["removed"][0]
    assert removed["from_zone"] == "Cockpit"
    assert removed["to_zone"] == "Salon"


def test_passage_width_changed():
    """A width_mm change is captured in the modified passages list."""
    passage_a = make_passage("Salon", "Pantry", width_mm=700)
    passage_b = make_passage("Salon", "Pantry", width_mm=850)
    layout_a = make_layout(passages=[passage_a])
    layout_b = make_layout(passages=[passage_b])

    result = compute_layout_diff(layout_a, layout_b)

    assert result["summary"]["passages_modified"] == 1
    mod = result["passages"]["modified"][0]
    assert mod["from_zone"] == "Salon"
    assert mod["to_zone"] == "Pantry"

    width_change = next(c for c in mod["changes"] if c["field"] == "width_mm")
    assert width_change["old"] == 700
    assert width_change["new"] == 850


# ---------------------------------------------------------------------------
# Tests: combined and summary accuracy
# ---------------------------------------------------------------------------

def test_multiple_changes():
    """All change types are detected simultaneously in a mixed diff."""
    z_kept = make_zone("Salon", "salon")
    z_only_a = make_zone("Lager", "storage")
    z_only_b = make_zone("Flybridge", "flybridge")
    z_modified_a = make_zone("Pantry", "pantry", polygon=[[0, 0], [1000, 0], [1000, 1000], [0, 1000]])
    z_modified_b = make_zone("Pantry", "pantry", polygon=[[0, 0], [2000, 0], [2000, 1000], [0, 1000]])

    p_kept = make_passage("Salon", "Pantry", width_mm=700)
    p_only_a = make_passage("Salon", "Lager", width_mm=600)
    p_only_b = make_passage("Salon", "Flybridge", width_mm=800)
    p_modified_a = make_passage("Cockpit", "Salon", width_mm=720)
    p_modified_b = make_passage("Cockpit", "Salon", width_mm=900)

    layout_a = make_layout(
        zones=[z_kept, z_only_a, z_modified_a],
        passages=[p_kept, p_only_a, p_modified_a],
    )
    layout_b = make_layout(
        zones=[z_kept, z_only_b, z_modified_b],
        passages=[p_kept, p_only_b, p_modified_b],
    )

    result = compute_layout_diff(layout_a, layout_b)
    s = result["summary"]

    assert s["zones_added"] == 1
    assert s["zones_removed"] == 1
    assert s["zones_modified"] == 1
    assert s["zones_unchanged"] == 1
    assert s["passages_added"] == 1
    assert s["passages_removed"] == 1
    assert s["passages_modified"] == 1
    assert s["has_changes"] is True


def test_area_change_calculation():
    """total_area_change_sqm reflects the difference in total zone polygon area."""
    # Zone A: 2000×2000 = 4 000 000 mm² = 4 m²
    poly_a = [[0, 0], [2000, 0], [2000, 2000], [0, 2000]]
    # Zone B: 3000×2000 = 6 000 000 mm² = 6 m²
    poly_b = [[0, 0], [3000, 0], [3000, 2000], [0, 2000]]

    layout_a = make_layout([make_zone("Salon", "salon", polygon=poly_a)])
    layout_b = make_layout([make_zone("Salon", "salon", polygon=poly_b)])

    result = compute_layout_diff(layout_a, layout_b)

    # 6 m² − 4 m² = 2 m²
    assert result["summary"]["total_area_change_sqm"] == 2.0


def test_summary_counts_correct():
    """Summary counts match the actual list lengths for all categories."""
    zones_a = [make_zone(f"Zone{i}", "salon") for i in range(4)]
    # Remove Zone0, keep Zone1-Zone3, add Zone4, modify Zone2 type
    zone2_modified = make_zone("Zone2", "cabin")
    zones_b = [make_zone("Zone1", "salon"), zone2_modified,
               make_zone("Zone3", "salon"), make_zone("Zone4", "cabin")]

    layout_a = make_layout(zones_a)
    layout_b = make_layout(zones_b)

    result = compute_layout_diff(layout_a, layout_b)
    s = result["summary"]

    assert s["zones_added"] == len(result["zones"]["added"])
    assert s["zones_removed"] == len(result["zones"]["removed"])
    assert s["zones_modified"] == len(result["zones"]["modified"])
    assert s["zones_unchanged"] == len(result["zones"]["unchanged"])
    assert s["passages_added"] == len(result["passages"]["added"])
    assert s["passages_removed"] == len(result["passages"]["removed"])
    assert s["passages_modified"] == len(result["passages"]["modified"])


# ---------------------------------------------------------------------------
# Unit test for the internal _polygon_area helper
# ---------------------------------------------------------------------------

def test_polygon_area_unit_square():
    """A 1000×1000 mm square has area 1 000 000 mm²."""
    poly = [[0, 0], [1000, 0], [1000, 1000], [0, 1000]]
    assert _polygon_area(poly) == 1_000_000.0


def test_polygon_area_degenerate():
    """Fewer than 3 vertices returns 0."""
    assert _polygon_area([]) == 0.0
    assert _polygon_area([[0, 0]]) == 0.0
    assert _polygon_area([[0, 0], [1000, 0]]) == 0.0
