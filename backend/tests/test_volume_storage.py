from tests.conftest import make_passage, make_zone

from app.services.analysis.volume_storage import (
    analyze_storage_accessibility,
    analyze_storage_distribution,
    analyze_storage_ratio,
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
        make_zone("salon", "salon", polygon=[[0, 0], [5000, 0], [5000, 3000], [0, 3000]]),
        make_zone("storage1", "storage", polygon=[[0, 3000], [2000, 3000], [2000, 5000], [0, 5000]]),
        make_zone("storage2", "storage", polygon=[[3000, 3000], [5000, 3000], [5000, 5000], [3000, 5000]]),
    ]
    passages = [make_passage("salon", "storage1"), make_passage("salon", "storage2")]
    result = run_volume_storage_analysis(zones, passages, "cruising_sail")
    assert result["module"] == "volume_storage"
    assert 0 <= result["overall_score"] <= 100
    assert "storage_ratio" in result["sub_scores"]


def test_volume_boat_class_difference():
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [5000, 0], [5000, 3000], [0, 3000]]),
        make_zone("s1", "storage", polygon=[[0, 3000], [1000, 3000], [1000, 4000], [0, 4000]]),
    ]
    passages = [make_passage("salon", "s1")]
    result_small = run_volume_storage_analysis(zones, passages, "small_sail")
    result_super = run_volume_storage_analysis(zones, passages, "superyacht")
    assert result_small["overall_score"] != result_super["overall_score"]
