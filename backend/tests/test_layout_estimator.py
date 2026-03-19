"""Tests for the layout estimator inference engine."""
import pytest

from app.services.inference.layout_estimator import (
    estimate_beam,
    estimate_layout_from_specs,
    BEAM_ESTIMATE_FACTORS,
    CLASS_LAYOUT_TEMPLATES,
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def zone_types(result: dict) -> list[str]:
    """Return list of zone_type values from a result dict."""
    return [z["zone_type"] for z in result["zones"]]


def zone_names(result: dict) -> list[str]:
    """Return list of zone name values from a result dict."""
    return [z["name"] for z in result["zones"]]


def passage_pairs(result: dict) -> list[tuple[str, str]]:
    """Return (from_zone, to_zone) pairs for all passages."""
    return [(p["from_zone"], p["to_zone"]) for p in result["passages"]]


# ---------------------------------------------------------------------------
# Basic smoke tests
# ---------------------------------------------------------------------------

def test_minimal_input_returns_zones_and_passages():
    """Minimal call (boat_class + length_m only) must produce zones and passages."""
    result = estimate_layout_from_specs(boat_class="small_sail", length_m=10.0)

    assert "zones" in result
    assert "passages" in result
    assert len(result["zones"]) > 0
    assert len(result["passages"]) > 0


def test_minimal_input_returns_required_keys():
    """Result dict must contain all expected top-level keys."""
    result = estimate_layout_from_specs(boat_class="cruising_sail", length_m=14.0)

    expected_keys = {
        "zones", "passages", "deck_height_mm", "confidence",
        "data_source", "specs_provided", "specs_inferred",
        "effective_beam_m", "effective_length_m",
    }
    assert expected_keys.issubset(result.keys())


# ---------------------------------------------------------------------------
# Zone composition per boat class
# ---------------------------------------------------------------------------

def test_small_sail_zones():
    """small_sail must include cockpit, salon, cabin, head, helm, engine, storage."""
    result = estimate_layout_from_specs(boat_class="small_sail", length_m=10.0)
    types = zone_types(result)

    for expected in ("cockpit", "salon", "cabin", "head", "helm", "engine", "storage"):
        assert expected in types, f"Expected zone type '{expected}' not found in small_sail layout"


def test_cruising_sail_zones():
    """cruising_sail must have all small_sail zones plus foredeck."""
    result = estimate_layout_from_specs(boat_class="cruising_sail", length_m=14.0)
    types = zone_types(result)

    for expected in ("cockpit", "salon", "cabin", "head", "helm", "engine", "storage", "foredeck"):
        assert expected in types, f"Expected zone type '{expected}' not found in cruising_sail layout"


def test_large_motor_zones():
    """large_motor must include flybridge and crew_quarters by default."""
    result = estimate_layout_from_specs(boat_class="large_motor", length_m=22.0)
    types = zone_types(result)

    assert "flybridge" in types, "large_motor should have flybridge by default"
    assert "crew_quarters" in types, "large_motor should have crew_quarters by default"


def test_superyacht_zones():
    """superyacht must include sky_lounge, beach_club, and tender_garage."""
    result = estimate_layout_from_specs(boat_class="superyacht", length_m=40.0)
    types = zone_types(result)

    for expected in ("sky_lounge", "beach_club", "tender_garage"):
        assert expected in types, f"Expected zone type '{expected}' not found in superyacht layout"


# ---------------------------------------------------------------------------
# Count-driven zone expansion
# ---------------------------------------------------------------------------

def test_cabin_count_respected():
    """Passing cabin_count=3 must produce exactly 3 cabin zones."""
    result = estimate_layout_from_specs(
        boat_class="cruising_sail", length_m=15.0, cabin_count=3
    )
    cabin_zones = [z for z in result["zones"] if z["zone_type"] == "cabin"]
    assert len(cabin_zones) == 3, f"Expected 3 cabin zones, got {len(cabin_zones)}"


def test_head_count_respected():
    """Passing head_count=2 must produce exactly 2 head zones."""
    result = estimate_layout_from_specs(
        boat_class="cruising_sail", length_m=15.0, head_count=2
    )
    head_zones = [z for z in result["zones"] if z["zone_type"] == "head"]
    assert len(head_zones) == 2, f"Expected 2 head zones, got {len(head_zones)}"


# ---------------------------------------------------------------------------
# Beam estimation and override
# ---------------------------------------------------------------------------

def test_beam_estimated_when_missing():
    """When beam_m is not provided it must be derived from length * factor."""
    length_m = 12.0
    boat_class = "cruising_sail"
    result = estimate_layout_from_specs(boat_class=boat_class, length_m=length_m)

    expected_beam = round(length_m * BEAM_ESTIMATE_FACTORS[boat_class], 2)
    assert result["effective_beam_m"] == expected_beam


def test_beam_used_when_provided():
    """When beam_m is explicitly provided it must be used verbatim."""
    result = estimate_layout_from_specs(
        boat_class="cruising_sail", length_m=14.0, beam_m=4.5
    )
    assert result["effective_beam_m"] == 4.5


# ---------------------------------------------------------------------------
# Deck height override
# ---------------------------------------------------------------------------

def test_deck_height_override():
    """A custom deck_height_mm must be applied to all generated zones."""
    custom_height = 2200.0
    result = estimate_layout_from_specs(
        boat_class="cruising_sail", length_m=14.0, deck_height_mm=custom_height
    )

    assert result["deck_height_mm"] == custom_height
    for zone in result["zones"]:
        assert zone["height_mm"] == custom_height, (
            f"Zone '{zone['name']}' has height {zone['height_mm']}, expected {custom_height}"
        )


# ---------------------------------------------------------------------------
# Optional zone suppression
# ---------------------------------------------------------------------------

def test_flybridge_excluded_when_false():
    """has_flybridge=False must result in no flybridge zone."""
    result = estimate_layout_from_specs(
        boat_class="large_motor", length_m=22.0, has_flybridge=False
    )
    types = zone_types(result)
    assert "flybridge" not in types, "flybridge zone should be absent when has_flybridge=False"


def test_crew_quarters_excluded_when_false():
    """has_crew_quarters=False must result in no crew_quarters zone."""
    result = estimate_layout_from_specs(
        boat_class="large_motor", length_m=22.0, has_crew_quarters=False
    )
    types = zone_types(result)
    assert "crew_quarters" not in types, (
        "crew_quarters zone should be absent when has_crew_quarters=False"
    )


# ---------------------------------------------------------------------------
# Area overrides
# ---------------------------------------------------------------------------

def test_cockpit_area_override():
    """A provided cockpit_area_sqm must be reflected in the cockpit zone's polygon area."""
    cockpit_sqm = 12.0
    result = estimate_layout_from_specs(
        boat_class="cruising_sail", length_m=14.0, cockpit_area_sqm=cockpit_sqm
    )

    cockpit_zones = [z for z in result["zones"] if z["zone_type"] == "cockpit"]
    assert len(cockpit_zones) == 1

    # The polygon is a rectangle; compute its area from the coordinates.
    poly = cockpit_zones[0]["polygon"]
    # poly = [[x0,y0],[x1,y0],[x1,y1],[x0,y1]]
    computed_area_sqm = abs(
        (poly[1][0] - poly[0][0]) * (poly[2][1] - poly[1][1])
    ) / 1e6
    assert abs(computed_area_sqm - cockpit_sqm) < 0.5, (
        f"Cockpit area should be ~{cockpit_sqm} sqm, got {computed_area_sqm:.2f}"
    )


# ---------------------------------------------------------------------------
# specs_provided / specs_inferred counts
# ---------------------------------------------------------------------------

def test_specs_count_minimal():
    """With only required fields, specs_provided should be 2 (boat_class + length_m)."""
    result = estimate_layout_from_specs(boat_class="small_sail", length_m=10.0)
    assert result["specs_provided"] == 2


def test_specs_count_with_optionals():
    """Each additional optional field increments specs_provided by 1."""
    result = estimate_layout_from_specs(
        boat_class="small_sail",
        length_m=10.0,
        beam_m=3.2,
        cabin_count=1,
        head_count=1,
    )
    # 2 required + 3 optional
    assert result["specs_provided"] == 5


def test_specs_inferred_greater_than_zero():
    """When no optional areas are given, specs_inferred must be > 0."""
    result = estimate_layout_from_specs(boat_class="cruising_sail", length_m=14.0)
    assert result["specs_inferred"] > 0


# ---------------------------------------------------------------------------
# Passage generation
# ---------------------------------------------------------------------------

def test_passages_generated():
    """Passages must exist and connect zones that are present in the layout."""
    result = estimate_layout_from_specs(boat_class="cruising_sail", length_m=14.0)
    names = set(zone_names(result))

    assert len(result["passages"]) > 0
    for p in result["passages"]:
        assert p["from_zone"] in names, (
            f"Passage from_zone '{p['from_zone']}' not in zone list"
        )
        assert p["to_zone"] in names, (
            f"Passage to_zone '{p['to_zone']}' not in zone list"
        )


def test_passages_have_width():
    """Every passage must have a positive width_mm."""
    result = estimate_layout_from_specs(boat_class="large_motor", length_m=22.0)
    for p in result["passages"]:
        assert p["width_mm"] > 0


# ---------------------------------------------------------------------------
# Unknown boat class fallback
# ---------------------------------------------------------------------------

def test_unknown_boat_class_fallback():
    """An unrecognised boat_class must not raise — falls back to cruising_sail template."""
    result = estimate_layout_from_specs(boat_class="hovercraft", length_m=12.0)

    # Should still return a valid layout
    assert len(result["zones"]) > 0
    assert len(result["passages"]) > 0

    # The fallback template is cruising_sail — check a characteristic zone
    types = zone_types(result)
    assert "foredeck" in types, "Unknown class fallback should use cruising_sail template (has foredeck)"


# ---------------------------------------------------------------------------
# estimate_beam standalone tests
# ---------------------------------------------------------------------------

def test_estimate_beam_known_class():
    """estimate_beam returns length * class factor for known classes."""
    for boat_class, factor in BEAM_ESTIMATE_FACTORS.items():
        result = estimate_beam(10.0, boat_class)
        assert result == round(10.0 * factor, 2)


def test_estimate_beam_unknown_class_uses_default():
    """estimate_beam uses the default factor (0.28) for unknown boat classes."""
    result = estimate_beam(10.0, "unknown_class")
    assert result == round(10.0 * 0.28, 2)
