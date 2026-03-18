from tests.conftest import make_passage, make_zone

from app.services.analysis.ergonomics import (
    analyze_accessibility,
    analyze_crew_guest_separation,
    analyze_helm_ergonomics,
    analyze_passage_widths,
    analyze_path_efficiency,
    run_ergonomics_analysis,
    BOAT_CLASS_DEFAULTS,
)


def _default_config(boat_class="cruising_sail"):
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


# --- analyze_passage_widths ---

def test_passage_widths_all_good():
    passages = [make_passage("a", "b", 800), make_passage("b", "c", 750)]
    score, warnings, metrics = analyze_passage_widths(passages, _default_config())
    assert score == 100.0
    assert len(warnings) == 0


def test_passage_widths_one_narrow():
    passages = [make_passage("a", "b", 600), make_passage("b", "c", 750)]
    score, warnings, metrics = analyze_passage_widths(passages, _default_config())
    assert score < 100.0
    assert any(w["severity"] == "warning" for w in warnings)


def test_passage_widths_critical():
    passages = [make_passage("a", "b", 400)]
    score, warnings, metrics = analyze_passage_widths(passages, _default_config())
    assert score < 50.0
    assert any(w["severity"] == "critical" for w in warnings)


def test_passage_widths_empty():
    score, warnings, metrics = analyze_passage_widths([], _default_config())
    assert score == 100.0


# --- analyze_path_efficiency ---

def test_path_efficiency_connected():
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("salon", "salon"),
        make_zone("pantry", "pantry"),
    ]
    passages = [make_passage("cockpit", "salon"), make_passage("salon", "pantry")]
    score, warnings, metrics = analyze_path_efficiency(zones, passages, _default_config())
    assert score > 80.0
    assert metrics["cockpit_pantry_steps"] == 2


def test_path_efficiency_isolated_zone():
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("salon", "salon"),
        make_zone("pantry", "pantry"),
        make_zone("storage1", "storage"),
    ]
    passages = [make_passage("cockpit", "salon"), make_passage("salon", "pantry")]
    score, warnings, metrics = analyze_path_efficiency(zones, passages, _default_config())
    assert score < 100.0
    assert any("isoliert" in w["message"].lower() or "isolated" in w["message"].lower() for w in warnings)


def test_path_efficiency_no_cockpit():
    zones = [make_zone("salon", "salon"), make_zone("pantry", "pantry")]
    passages = [make_passage("salon", "pantry")]
    score, warnings, metrics = analyze_path_efficiency(zones, passages, _default_config())
    assert metrics["cockpit_pantry_steps"] == -1


# --- analyze_crew_guest_separation ---

def test_crew_guest_separation_not_required():
    config = _default_config("small_sail")
    zones = [make_zone("cabin", "cabin", is_crew_area=True), make_zone("salon", "salon", is_guest_area=True)]
    passages = [make_passage("cabin", "salon")]
    score, warnings, metrics = analyze_crew_guest_separation(zones, passages, config)
    assert score == 100.0


def test_crew_guest_separation_violation():
    config = _default_config("superyacht")
    zones = [
        make_zone("crew_cabin", "cabin", is_crew_area=True),
        make_zone("guest_salon", "salon", is_guest_area=True),
    ]
    passages = [make_passage("crew_cabin", "guest_salon")]
    score, warnings, metrics = analyze_crew_guest_separation(zones, passages, config)
    assert score < 100.0
    assert len(warnings) > 0


def test_crew_guest_separation_clean():
    config = _default_config("superyacht")
    zones = [
        make_zone("crew_cabin", "cabin", is_crew_area=True),
        make_zone("guest_salon", "salon", is_guest_area=True),
    ]
    passages = []
    score, warnings, metrics = analyze_crew_guest_separation(zones, passages, config)
    assert score == 100.0


# --- analyze_accessibility ---

def test_accessibility_all_present():
    zones = [
        make_zone("engine1", "engine"),
        make_zone("pantry1", "pantry"),
        make_zone("helm1", "helm"),
        make_zone("head1", "head"),
        make_zone("salon1", "salon"),
    ]
    passages = [
        make_passage("salon1", "engine1"),
        make_passage("salon1", "pantry1"),
        make_passage("salon1", "helm1"),
        make_passage("salon1", "head1"),
    ]
    score, warnings, metrics = analyze_accessibility(zones, passages, _default_config())
    assert score == 100.0


def test_accessibility_missing_engine():
    zones = [
        make_zone("pantry1", "pantry"),
        make_zone("helm1", "helm"),
        make_zone("head1", "head"),
    ]
    passages = [make_passage("pantry1", "helm1"), make_passage("helm1", "head1")]
    score, warnings, metrics = analyze_accessibility(zones, passages, _default_config())
    assert score < 100.0
    assert any("engine" in w["message"].lower() or "maschinenraum" in w["message"].lower() for w in warnings)


def test_accessibility_unreachable():
    zones = [
        make_zone("engine1", "engine"),
        make_zone("pantry1", "pantry"),
        make_zone("helm1", "helm"),
        make_zone("head1", "head"),
    ]
    passages = [make_passage("pantry1", "helm1")]
    score, warnings, metrics = analyze_accessibility(zones, passages, _default_config())
    assert score < 100.0


# --- analyze_helm_ergonomics ---

def test_helm_good_area():
    helm = make_zone("helm1", "helm", polygon=[[0, 0], [2000, 0], [2000, 1500], [0, 1500]])
    score, warnings, metrics = analyze_helm_ergonomics([helm], _default_config())
    assert score > 80.0


def test_helm_too_small():
    helm = make_zone("helm1", "helm", polygon=[[0, 0], [1000, 0], [1000, 1000], [0, 1000]])
    score, warnings, metrics = analyze_helm_ergonomics([helm], _default_config())
    assert score < 80.0
    assert len(warnings) > 0


def test_helm_missing():
    zones = [make_zone("salon", "salon")]
    score, warnings, metrics = analyze_helm_ergonomics(zones, _default_config())
    assert score == 0.0
    assert any(w["severity"] == "critical" for w in warnings)


# --- run_ergonomics_analysis (orchestrator) ---

def test_full_analysis_good_layout():
    zones = [
        make_zone("cockpit1", "cockpit", polygon=[[0, 0], [3000, 0], [3000, 2000], [0, 2000]]),
        make_zone("salon1", "salon", polygon=[[0, 2000], [3000, 2000], [3000, 5000], [0, 5000]]),
        make_zone("pantry1", "pantry", polygon=[[0, 5000], [3000, 5000], [3000, 7000], [0, 7000]]),
        make_zone("helm1", "helm", polygon=[[0, 7000], [2000, 7000], [2000, 8500], [0, 8500]]),
        make_zone("engine1", "engine", polygon=[[2000, 7000], [3000, 7000], [3000, 8500], [2000, 8500]]),
        make_zone("head1", "head", polygon=[[3000, 2000], [4000, 2000], [4000, 4000], [3000, 4000]]),
    ]
    passages = [
        make_passage("cockpit1", "salon1", 800),
        make_passage("salon1", "pantry1", 750),
        make_passage("pantry1", "helm1", 700),
        make_passage("pantry1", "engine1", 700),
        make_passage("salon1", "head1", 700),
    ]
    result = run_ergonomics_analysis(zones, passages, "cruising_sail")
    assert result["module"] == "ergonomics"
    assert 0 <= result["overall_score"] <= 100
    assert "passage_width" in result["sub_scores"]
    assert isinstance(result["warnings"], list)
    assert isinstance(result["config_used"], dict)


def test_full_analysis_different_boat_classes():
    zones = [
        make_zone("cockpit1", "cockpit"),
        make_zone("salon1", "salon"),
        make_zone("pantry1", "pantry"),
        make_zone("helm1", "helm"),
        make_zone("engine1", "engine"),
        make_zone("head1", "head"),
    ]
    passages = [
        make_passage("cockpit1", "salon1", 650),
        make_passage("salon1", "pantry1", 650),
        make_passage("salon1", "helm1", 650),
        make_passage("salon1", "engine1", 650),
        make_passage("salon1", "head1", 650),
    ]
    result_small = run_ergonomics_analysis(zones, passages, "small_sail")
    result_super = run_ergonomics_analysis(zones, passages, "superyacht")
    assert result_small["sub_scores"]["passage_width"] > result_super["sub_scores"]["passage_width"]


def test_full_analysis_with_config_overrides():
    zones = [make_zone("helm1", "helm"), make_zone("cockpit1", "cockpit"), make_zone("pantry1", "pantry"),
             make_zone("engine1", "engine"), make_zone("head1", "head")]
    passages = [make_passage("cockpit1", "helm1", 500), make_passage("helm1", "pantry1", 500),
                make_passage("pantry1", "engine1", 500), make_passage("pantry1", "head1", 500)]
    result = run_ergonomics_analysis(zones, passages, "cruising_sail", config_overrides={"min_passage_width_mm": 400})
    assert result["config_used"]["min_passage_width_mm"] == 400
