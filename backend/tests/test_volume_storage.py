from tests.conftest import make_passage, make_zone

from app.services.analysis.volume_storage import (
    analyze_furniture_ratio,
    analyze_storage_accessibility,
    analyze_storage_distribution,
    analyze_storage_ratio,
    analyze_volume_utilization,
    run_volume_storage_analysis,
    BOAT_CLASS_DEFAULTS,
)


def _default_config(boat_class="cruising_sail"):
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


def test_storage_ratio_good():
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [5000, 0], [5000, 3000], [0, 3000]]),
        make_zone("storage1", "storage", polygon=[[0, 3000], [2000, 3000], [2000, 5000], [0, 5000]]),
        make_zone("storage2", "storage", polygon=[[2000, 3000], [4000, 3000], [4000, 5000], [2000, 5000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_storage_ratio(zones, config)
    assert score > 70.0
    assert metrics["storage_ratio"] > 0


def test_storage_ratio_none():
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_storage_ratio(zones, config)
    assert score == 0.0
    assert any(w["severity"] == "critical" for w in warnings)


def test_storage_ratio_too_low():
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [10000, 0], [10000, 10000], [0, 10000]]),
        make_zone("storage1", "storage", polygon=[[0, 0], [500, 0], [500, 1000], [0, 1000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_storage_ratio(zones, config)
    assert score < 50.0
    assert any(w["severity"] == "warning" for w in warnings)


def test_storage_distribution_spread():
    zones = [
        make_zone("s1", "storage", polygon=[[0, 0], [1000, 0], [1000, 1000], [0, 1000]]),
        make_zone("s2", "storage", polygon=[[5000, 0], [6000, 0], [6000, 1000], [5000, 1000]]),
        make_zone("s3", "storage", polygon=[[0, 5000], [1000, 5000], [1000, 6000], [0, 6000]]),
        make_zone("salon", "salon", polygon=[[1000, 1000], [5000, 1000], [5000, 5000], [1000, 5000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_storage_distribution(zones, config)
    assert score > 60.0


def test_storage_distribution_clustered():
    zones = [
        make_zone("s1", "storage", polygon=[[0, 0], [500, 0], [500, 500], [0, 500]]),
        make_zone("s2", "storage", polygon=[[500, 0], [1000, 0], [1000, 500], [500, 500]]),
        make_zone("salon", "salon", polygon=[[0, 0], [10000, 0], [10000, 10000], [0, 10000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_storage_distribution(zones, config)
    assert score < 80.0


def test_storage_accessible():
    zones = [make_zone("salon", "salon"), make_zone("storage1", "storage")]
    passages = [make_passage("salon", "storage1")]
    config = _default_config()
    score, warnings, metrics = analyze_storage_accessibility(zones, passages, config)
    assert score == 100.0


def test_storage_unreachable():
    zones = [make_zone("salon", "salon"), make_zone("storage1", "storage")]
    passages = []
    config = _default_config()
    score, warnings, metrics = analyze_storage_accessibility(zones, passages, config)
    assert score < 100.0
    assert len(warnings) > 0


def test_full_volume_analysis():
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [5000, 0], [5000, 3000], [0, 3000]],
                  properties={"furniture_area_pct": 0.35}),
        make_zone("storage1", "storage", polygon=[[0, 3000], [2000, 3000], [2000, 5000], [0, 5000]]),
        make_zone("storage2", "storage", polygon=[[3000, 3000], [5000, 3000], [5000, 5000], [3000, 5000]]),
    ]
    passages = [make_passage("salon", "storage1"), make_passage("salon", "storage2")]
    result = run_volume_storage_analysis(zones, passages, "cruising_sail")
    assert result["module"] == "volume_storage"
    assert 0 <= result["overall_score"] <= 100
    assert "storage_ratio" in result["sub_scores"]
    assert "utilization" in result["sub_scores"]
    assert "furniture_ratio" in result["sub_scores"]
    assert "storage_distribution" in result["sub_scores"]
    assert "storage_accessibility" in result["sub_scores"]
    assert len(result["sub_scores"]) == 5


def test_volume_utilization_good():
    """Zones cover ~73% of bounding box -> good score."""
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [4000, 0], [4000, 3000], [0, 3000]]),
        make_zone("cabin", "cabin", polygon=[[0, 3000], [3000, 3000], [3000, 5000], [0, 5000]]),
        make_zone("pantry", "pantry", polygon=[[3000, 3000], [4000, 3000], [4000, 5000], [3000, 5000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_volume_utilization(zones, config)
    assert score >= 80.0
    assert metrics["utilization_ratio"] > 0.6


def test_volume_utilization_poor():
    """Single small zone in large bounding box -> poor score."""
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [1000, 0], [1000, 1000], [0, 1000]]),
        make_zone("cabin", "cabin", polygon=[[9000, 9000], [10000, 9000], [10000, 10000], [9000, 10000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_volume_utilization(zones, config)
    assert score < 50.0
    assert any(w["severity"] == "warning" for w in warnings)


def test_volume_utilization_empty():
    """No zones -> degraded score 50 + info warning."""
    config = _default_config()
    score, warnings, metrics = analyze_volume_utilization([], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


def test_volume_boat_class_difference():
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [5000, 0], [5000, 3000], [0, 3000]]),
        make_zone("s1", "storage", polygon=[[0, 3000], [1000, 3000], [1000, 4000], [0, 4000]]),
    ]
    passages = [make_passage("salon", "s1")]
    result_small = run_volume_storage_analysis(zones, passages, "small_sail")
    result_super = run_volume_storage_analysis(zones, passages, "superyacht")
    assert result_small["overall_score"] != result_super["overall_score"]


def test_furniture_ratio_good():
    """All zones have furniture in acceptable range -> high score."""
    zones = [
        make_zone("salon", "salon", properties={"furniture_area_pct": 0.35}),
        make_zone("cabin", "cabin", properties={"furniture_area_pct": 0.40}),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_furniture_ratio(zones, config)
    assert score >= 80.0
    assert metrics["zones_evaluated"] == 2


def test_furniture_ratio_cramped():
    """Zone furniture > max threshold -> warning."""
    zones = [
        make_zone("cabin", "cabin", properties={"furniture_area_pct": 0.70}),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_furniture_ratio(zones, config)
    assert score < 80.0
    assert any("übermöbliert" in w["message"].lower() or "möblierung" in w["message"].lower() for w in warnings)


def test_furniture_ratio_sparse():
    """Zone furniture < min threshold -> warning."""
    zones = [
        make_zone("salon", "salon", properties={"furniture_area_pct": 0.10}),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_furniture_ratio(zones, config)
    assert score < 100.0
    assert len(warnings) > 0


def test_furniture_ratio_no_data():
    """No furniture data on any zone -> degraded score 50 + info."""
    zones = [make_zone("salon", "salon"), make_zone("cabin", "cabin")]
    config = _default_config()
    score, warnings, metrics = analyze_furniture_ratio(zones, config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
    assert metrics["zones_evaluated"] == 0


def test_furniture_ratio_mixed_data():
    """Some zones have furniture data, some don't -> only score zones with data."""
    zones = [
        make_zone("salon", "salon", properties={"furniture_area_pct": 0.35}),
        make_zone("cabin", "cabin"),  # no properties
    ]
    config = _default_config()
    score, warnings, metrics = analyze_furniture_ratio(zones, config)
    assert score > 50.0  # at least the salon is evaluated
    assert metrics["zones_evaluated"] == 1


def test_furniture_ratio_excluded_types():
    """Storage/engine zones with furniture data are ignored."""
    zones = [
        make_zone("engine1", "engine", properties={"furniture_area_pct": 0.90}),
        make_zone("storage1", "storage", properties={"furniture_area_pct": 0.90}),
        make_zone("salon", "salon", properties={"furniture_area_pct": 0.35}),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_furniture_ratio(zones, config)
    assert metrics["zones_evaluated"] == 1  # only salon
    assert score >= 80.0  # salon is fine, excluded zones ignored


def test_volume_boat_class_difference_with_furniture():
    """Different boat classes produce different scores with furniture data."""
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [5000, 0], [5000, 3000], [0, 3000]],
                  properties={"furniture_area_pct": 0.35}),
        make_zone("cabin", "cabin", polygon=[[0, 3000], [3000, 3000], [3000, 5000], [0, 5000]],
                  properties={"furniture_area_pct": 0.40}),
        make_zone("storage1", "storage", polygon=[[3000, 3000], [5000, 3000], [5000, 5000], [3000, 5000]]),
    ]
    passages = [make_passage("salon", "cabin"), make_passage("salon", "storage1")]
    result_small = run_volume_storage_analysis(zones, passages, "small_sail")
    result_super = run_volume_storage_analysis(zones, passages, "superyacht")
    # Different weights produce different overall scores
    assert result_small["overall_score"] != result_super["overall_score"]
    # Both should have all 5 sub-scores
    assert len(result_small["sub_scores"]) == 5
    assert len(result_super["sub_scores"]) == 5


def test_volume_config_overrides():
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [5000, 0], [5000, 3000], [0, 3000]]),
        make_zone("storage1", "storage", polygon=[[0, 3000], [2000, 3000], [2000, 5000], [0, 5000]]),
    ]
    passages = [make_passage("salon", "storage1")]
    result = run_volume_storage_analysis(zones, passages, "cruising_sail",
                                         config_overrides={"target_utilization": 0.99})
    assert result["config_used"]["target_utilization"] == 0.99
