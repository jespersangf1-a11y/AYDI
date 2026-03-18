"""Tests for structural analysis module (weight distribution)."""
from tests.conftest import make_zone
from app.services.analysis.structural import (
    analyze_fore_aft_balance,
    BOAT_CLASS_DEFAULTS,
)


def _default_config(boat_class="cruising_sail"):
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


# ---------------------------------------------------------------------------
# analyze_fore_aft_balance
# ---------------------------------------------------------------------------


def test_fore_aft_balanced():
    """CoG within ideal range -> score 100."""
    zones = [
        make_zone("salon", "salon", polygon=[[4000, 0], [6000, 0], [6000, 3000], [4000, 3000]]),
        make_zone("engine", "engine", polygon=[[4500, 0], [5500, 0], [5500, 1500], [4500, 1500]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_fore_aft_balance(zones, config)
    assert score == 100.0
    assert metrics["deviation_pct"] == 0.0
    assert 0.44 <= metrics["cog_x_pct"] <= 0.54


def test_fore_aft_too_far_aft():
    """Heavy zone at stern -> CoG too far aft, warning."""
    zones = [
        make_zone("cabin", "cabin", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
        make_zone("engine", "engine", polygon=[[8000, 0], [10000, 0], [10000, 2000], [8000, 2000]]),
        make_zone("storage", "storage", polygon=[[7000, 0], [9000, 0], [9000, 2000], [7000, 2000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_fore_aft_balance(zones, config)
    assert score < 100.0
    assert any(w["code"] == "COG_TOO_FAR_AFT" for w in warnings)
    assert metrics["cog_x_pct"] > 0.54


def test_fore_aft_too_far_forward():
    """Heavy zone at bow -> CoG too far forward, warning."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
        make_zone("cabin", "cabin", polygon=[[8000, 0], [10000, 0], [10000, 2000], [8000, 2000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_fore_aft_balance(zones, config)
    assert score < 100.0
    assert any(w["code"] == "COG_TOO_FAR_FORWARD" for w in warnings)
    assert metrics["cog_x_pct"] < 0.44


def test_fore_aft_no_zones():
    """No zones -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_fore_aft_balance([], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
