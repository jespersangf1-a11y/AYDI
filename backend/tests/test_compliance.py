"""Tests for compliance checker module — escape routes and fire safety."""
from tests.conftest import make_passage, make_zone
from app.services.analysis.compliance import (
    analyze_escape_routes,
    analyze_fire_safety,
    BOAT_CLASS_DEFAULTS,
)


def _default_config(boat_class="cruising_sail"):
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


# ---------------------------------------------------------------------------
# analyze_escape_routes
# ---------------------------------------------------------------------------


def test_escape_route_compliant():
    """Cabin connected to cockpit via wide passage -> score 100."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("cabin1", "cabin"),
    ]
    passages = [make_passage("cabin1", "cockpit", width_mm=700)]
    config = _default_config()
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score == 100.0
    assert metrics["cabins_compliant"] == 1


def test_escape_route_no_cockpit():
    """No cockpit -> score 0, critical warning."""
    zones = [make_zone("cabin1", "cabin")]
    passages = []
    config = _default_config()
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score == 0.0
    assert any(w["severity"] == "critical" for w in warnings)


def test_escape_route_no_cabins():
    """No sleeping zones -> score 100, info."""
    zones = [make_zone("cockpit", "cockpit"), make_zone("salon", "salon")]
    passages = [make_passage("cockpit", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score == 100.0
    assert any(w["severity"] == "info" for w in warnings)
    assert metrics["cabins_total"] == 0


def test_escape_route_unreachable():
    """Cabin with no path to cockpit -> critical."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("cabin1", "cabin"),
        make_zone("salon", "salon"),
    ]
    passages = [make_passage("cockpit", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score == 0.0
    assert any(w["severity"] == "critical" for w in warnings)
    assert metrics["cabins_compliant"] == 0


def test_escape_route_narrow_passage():
    """Escape route passage below 600mm ISO minimum -> critical, partial score."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("cabin1", "cabin"),
    ]
    passages = [make_passage("cabin1", "cockpit", width_mm=500)]
    config = _default_config()
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score == 50.0
    assert any(w["severity"] == "critical" for w in warnings)


def test_escape_route_too_long():
    """Escape route with too many hops -> warning."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("salon", "salon"),
        make_zone("pantry", "pantry"),
        make_zone("head", "head"),
        make_zone("storage1", "storage"),
        make_zone("storage2", "storage"),
        make_zone("storage3", "storage"),
        make_zone("cabin1", "cabin"),
    ]
    passages = [
        make_passage("cabin1", "storage3"),
        make_passage("storage3", "storage2"),
        make_passage("storage2", "storage1"),
        make_passage("storage1", "head"),
        make_passage("head", "pantry"),
        make_passage("pantry", "salon"),
        make_passage("salon", "cockpit"),
    ]
    config = _default_config()  # max_escape_hops = 5
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score < 100.0
    assert any(w["severity"] == "warning" for w in warnings)


# ---------------------------------------------------------------------------
# analyze_fire_safety
# ---------------------------------------------------------------------------


def test_fire_safety_good():
    """Engine far from living zones, accessible -> high score."""
    zones = [
        make_zone("engine", "engine", polygon=[[8000, 1000], [10000, 1000], [10000, 3000], [8000, 3000]]),
        make_zone("salon", "salon", polygon=[[0, 0], [4000, 0], [4000, 4000], [0, 4000]]),
    ]
    passages = [make_passage("salon", "engine")]
    config = _default_config()
    score, warnings, metrics = analyze_fire_safety(zones, passages, config)
    assert score >= 80.0
    assert metrics["engine_accessible"] is True


def test_fire_safety_no_engine():
    """No engine zone -> score 50, info."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_fire_safety(zones, [], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


def test_fire_safety_engine_too_close():
    """Engine centroid within min_engine_clearance_mm of living zone -> warning."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [500, 0], [500, 500], [0, 500]]),
        make_zone("cabin", "cabin", polygon=[[500, 0], [1000, 0], [1000, 500], [500, 500]]),
    ]
    passages = [make_passage("engine", "cabin")]
    config = _default_config()  # min_engine_clearance_mm = 600
    # Centroids: engine (250,250), cabin (750,250) -> dist = 500mm < 600mm
    score, warnings, metrics = analyze_fire_safety(zones, passages, config)
    assert score < 100.0
    assert any(w["severity"] == "warning" for w in warnings)
    assert metrics["min_clearance_mm"] < 600


def test_fire_safety_engine_inaccessible():
    """Engine not connected via passages -> critical."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("salon", "salon"),
    ]
    passages = []
    config = _default_config()
    score, warnings, metrics = analyze_fire_safety(zones, passages, config)
    assert any(w["severity"] == "critical" for w in warnings)
    assert metrics["engine_accessible"] is False
