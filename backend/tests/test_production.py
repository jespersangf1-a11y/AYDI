"""Tests for production friendliness analysis module — Tasks 1 & 2."""
from tests.conftest import make_passage, make_zone

from app.services.analysis.production import (
    analyze_assembly_sequence,
    analyze_form_complexity,
    BOAT_CLASS_DEFAULTS,
)


def _default_config(boat_class: str = "cruising_sail") -> dict:
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


# ---------------------------------------------------------------------------
# analyze_assembly_sequence
# ---------------------------------------------------------------------------


def test_assembly_no_bottlenecks():
    """Ring topology — every zone has two paths to all others, no bottlenecks."""
    zones = [
        make_zone("A", "salon"),
        make_zone("B", "cabin"),
        make_zone("C", "pantry"),
        make_zone("D", "cockpit"),
    ]
    passages = [
        make_passage("A", "B"),
        make_passage("B", "C"),
        make_passage("C", "D"),
        make_passage("D", "A"),
    ]
    score, warnings, metrics = analyze_assembly_sequence(zones, passages, _default_config())
    assert score == 100.0
    assert metrics["bottleneck_count"] == 0


def test_assembly_one_bottleneck():
    """Linear chain A-B-C-D — B and C are bottlenecks."""
    zones = [
        make_zone("A", "salon"),
        make_zone("B", "cabin"),
        make_zone("C", "pantry"),
        make_zone("D", "cockpit"),
    ]
    passages = [
        make_passage("A", "B"),
        make_passage("B", "C"),
        make_passage("C", "D"),
    ]
    score, warnings, metrics = analyze_assembly_sequence(zones, passages, _default_config())
    assert score < 100.0
    assert metrics["bottleneck_count"] >= 1
    assert any(w["code"] == "MONTAGE_BOTTLENECK" for w in warnings)


def test_assembly_all_isolated():
    """Three zones, no passages — no connections, critical warning."""
    zones = [
        make_zone("X", "salon"),
        make_zone("Y", "cabin"),
        make_zone("Z", "pantry"),
    ]
    score, warnings, metrics = analyze_assembly_sequence(zones, [], _default_config())
    assert score == 0.0
    assert any(w["severity"] == "critical" for w in warnings)
    assert any(w["code"] == "MONTAGE_NO_CONNECTIONS" for w in warnings)


def test_assembly_no_zones():
    """Empty zones list — score 50, info warning."""
    score, warnings, metrics = analyze_assembly_sequence([], [], _default_config())
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
    assert any(w["code"] == "MONTAGE_NO_ZONES" for w in warnings)


def test_assembly_single_zone():
    """Single zone — trivially connected, score 100."""
    zones = [make_zone("Solo", "salon")]
    score, warnings, metrics = analyze_assembly_sequence(zones, [], _default_config())
    assert score == 100.0
    assert metrics["bottleneck_count"] == 0


# ---------------------------------------------------------------------------
# analyze_form_complexity
# ---------------------------------------------------------------------------


def test_form_all_right_angles():
    """Rectangle zones have only 90° angles — no sharp or reflex, score 100."""
    zones = [
        make_zone("Salon", "salon", polygon=[[0, 0], [4000, 0], [4000, 3000], [0, 3000]]),
        make_zone("Cabin", "cabin", polygon=[[0, 0], [2000, 0], [2000, 1500], [0, 1500]]),
    ]
    score, warnings, metrics = analyze_form_complexity(zones, _default_config())
    assert score == 100.0
    assert metrics["total_sharp_angles"] == 0
    assert metrics["total_reflex_angles"] == 0


def test_form_sharp_angles():
    """Thin triangle has one very sharp angle — score < 100, sharp >= 1."""
    # Triangle with a ~10° apex angle
    import math
    half_base = 100  # mm
    height = int(half_base / math.tan(math.radians(10)))
    polygon = [
        [0, 0],
        [2 * half_base, 0],
        [half_base, height],
    ]
    zones = [make_zone("Sharp", "salon", polygon=polygon)]
    score, warnings, metrics = analyze_form_complexity(zones, _default_config())
    assert score < 100.0
    assert metrics["total_sharp_angles"] >= 1
    assert any(w["code"] == "FORM_SHARP_ANGLE" for w in warnings)


def test_form_reflex_angle():
    """L-shape polygon has exactly one reflex (concave) vertex."""
    # CCW L-shape: [[0,0],[3000,0],[3000,1000],[1000,1000],[1000,3000],[0,3000]]
    polygon = [
        [0, 0],
        [3000, 0],
        [3000, 1000],
        [1000, 1000],
        [1000, 3000],
        [0, 3000],
    ]
    zones = [make_zone("LShape", "salon", polygon=polygon)]
    score, warnings, metrics = analyze_form_complexity(zones, _default_config())
    assert score < 100.0
    assert metrics["total_reflex_angles"] == 1
    assert any(w["code"] == "FORM_UNDERCUT" for w in warnings)


def test_form_no_zones():
    """Empty zones list — score 50, info warning."""
    score, warnings, metrics = analyze_form_complexity([], _default_config())
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
    assert any(w["code"] == "FORM_NO_ZONES" for w in warnings)
