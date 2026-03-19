"""Tests for service pattern analysis module."""
from tests.conftest import make_zone, make_service_report
from app.services.analysis.service_patterns import (
    analyze_zone_type_issues,
    analyze_age_patterns,
    analyze_material_failures,
    analyze_design_warnings,
    run_service_patterns_analysis,
    BOAT_CLASS_DEFAULTS,
    SEVERITY_ORDER,
)


def _default_config(boat_class: str = "cruising_sail") -> dict:
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


# ---------------------------------------------------------------------------
# test_empty_reports
# ---------------------------------------------------------------------------


def test_empty_reports():
    """No service reports -> score 50.0 and a single info warning."""
    result = run_service_patterns_analysis([], [], "cruising_sail", service_reports=[])
    assert result["overall_score"] == 50.0
    assert result["module"] == "service_patterns"
    assert len(result["warnings"]) == 1
    assert result["warnings"][0]["severity"] == "info"
    assert result["warnings"][0]["code"] == "NO_SERVICE_REPORTS"


def test_empty_reports_none():
    """service_reports=None is treated the same as an empty list."""
    result = run_service_patterns_analysis([], [], "cruising_sail", service_reports=None)
    assert result["overall_score"] == 50.0
    assert result["warnings"][0]["code"] == "NO_SERVICE_REPORTS"


# ---------------------------------------------------------------------------
# test_no_zone_issues
# ---------------------------------------------------------------------------


def test_no_zone_issues():
    """Few low-severity reports well below threshold -> score 100 for zone_issues."""
    reports = [
        make_service_report(zone_type="cabin", severity="low"),
        make_service_report(zone_type="cabin", severity="low"),
    ]
    config = _default_config()  # high_issue_threshold = 5
    score, warnings, metrics = analyze_zone_type_issues([], reports, config)
    # 2 low reports = weight 2, below threshold 5
    assert score == 100.0
    assert metrics["problematic_zone_types"] == []
    assert not any(w["code"].startswith("SERVICE_PATTERN_") for w in warnings)


# ---------------------------------------------------------------------------
# test_zone_type_with_many_issues
# ---------------------------------------------------------------------------


def test_zone_type_with_many_issues():
    """Zone type accumulating score >= threshold -> warning generated."""
    # 2 critical (4 each) = 8 >= threshold 5
    reports = [
        make_service_report(zone_type="head", severity="critical"),
        make_service_report(zone_type="head", severity="critical"),
    ]
    config = _default_config()  # high_issue_threshold = 5
    score, warnings, metrics = analyze_zone_type_issues([], reports, config)
    assert score < 100.0
    assert any(w["code"] == "SERVICE_PATTERN_HEAD" for w in warnings)
    assert "head" in metrics["problematic_zone_types"]


# ---------------------------------------------------------------------------
# test_severity_weighting
# ---------------------------------------------------------------------------


def test_severity_weighting():
    """Critical reports count more than low-severity reports."""
    # One critical report = weight 4; one low report = weight 1
    reports_critical = [make_service_report(zone_type="engine", severity="critical")]
    reports_low = [make_service_report(zone_type="engine", severity="low")]

    config = _default_config()
    _, _, metrics_critical = analyze_zone_type_issues([], reports_critical, config)
    _, _, metrics_low = analyze_zone_type_issues([], reports_low, config)

    assert metrics_critical["zone_type_scores"]["engine"] == 4.0
    assert metrics_low["zone_type_scores"]["engine"] == 1.0


# ---------------------------------------------------------------------------
# test_age_pattern_uniform
# ---------------------------------------------------------------------------


def test_age_pattern_uniform():
    """Uniformly distributed reports across buckets -> high score, no spike warnings."""
    # One report per age bucket
    ages = [6, 18, 30, 42, 54, 65]
    reports = [make_service_report(boat_age_months=a) for a in ages]
    config = _default_config()
    score, warnings, metrics = analyze_age_patterns(reports, config)
    assert score >= 80.0
    assert not any(w["code"] == "AGE_PATTERN_WARNING" for w in warnings)
    assert metrics["spike_buckets"] == []


# ---------------------------------------------------------------------------
# test_age_pattern_spike
# ---------------------------------------------------------------------------


def test_age_pattern_spike():
    """Many reports clustered in one age window -> spike warning generated."""
    # 10 reports aged 24-35 months, 1 report in each other window
    reports = [make_service_report(boat_age_months=28) for _ in range(10)]
    reports += [make_service_report(boat_age_months=6)]
    reports += [make_service_report(boat_age_months=65)]

    config = _default_config()
    score, warnings, metrics = analyze_age_patterns(reports, config)
    assert score < 100.0
    assert any(w["code"] == "AGE_PATTERN_WARNING" for w in warnings)
    assert len(metrics["spike_buckets"]) >= 1


# ---------------------------------------------------------------------------
# test_material_failure_detected
# ---------------------------------------------------------------------------


def test_material_failure_detected():
    """Material appearing in >= min_reports_for_pattern reports -> warning."""
    reports = [
        make_service_report(materials_involved=["GFK-Laminat"]),
        make_service_report(materials_involved=["GFK-Laminat"]),
        make_service_report(materials_involved=["GFK-Laminat"]),  # 3 = threshold
    ]
    config = _default_config()  # min_reports_for_pattern = 3
    score, warnings, metrics = analyze_material_failures(reports, config)
    assert score < 100.0
    assert any(w["code"] == "MATERIAL_FAILURE_RISK" for w in warnings)
    assert "GFK-Laminat" in metrics["problematic_materials"]


# ---------------------------------------------------------------------------
# test_material_failure_none
# ---------------------------------------------------------------------------


def test_material_failure_none():
    """Material appearing below threshold -> no warning, score 100."""
    reports = [
        make_service_report(materials_involved=["Teak"]),
        make_service_report(materials_involved=["Teak"]),
        # only 2 reports, threshold is 3
    ]
    config = _default_config()
    score, warnings, metrics = analyze_material_failures(reports, config)
    assert score == 100.0
    assert not any(w["code"] == "MATERIAL_FAILURE_RISK" for w in warnings)
    assert metrics["problematic_materials"] == []


# ---------------------------------------------------------------------------
# test_design_warnings_matching_zones
# ---------------------------------------------------------------------------


def test_design_warnings_matching_zones():
    """Zone in current layout whose zone_type is historically problematic -> proactive warning."""
    # Build enough critical reports to exceed threshold for zone_type "cabin"
    reports = [
        make_service_report(zone_type="cabin", severity="critical"),
        make_service_report(zone_type="cabin", severity="critical"),
    ]
    zones = [make_zone("Schlafkabine", "cabin")]
    config = _default_config()  # high_issue_threshold = 5; 2*4=8 >= 5
    score, warnings, metrics = analyze_design_warnings(zones, reports, config)
    assert score < 100.0
    assert any(w["code"] == "LAYOUT_CORRELATED_ISSUE" for w in warnings)
    assert "cabin" in metrics["matched_zone_types"]


# ---------------------------------------------------------------------------
# test_design_warnings_no_match
# ---------------------------------------------------------------------------


def test_design_warnings_no_match():
    """Layout zones do not match any historically problematic zone_type -> score 100."""
    # Reports are about "engine", current layout only has "salon"
    reports = [
        make_service_report(zone_type="engine", severity="critical"),
        make_service_report(zone_type="engine", severity="critical"),
    ]
    zones = [make_zone("Salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_design_warnings(zones, reports, config)
    assert score == 100.0
    assert not any(w["code"] == "LAYOUT_CORRELATED_ISSUE" for w in warnings)
    assert metrics["matched_zone_count"] == 0


# ---------------------------------------------------------------------------
# test_different_boat_classes
# ---------------------------------------------------------------------------


def test_different_boat_classes():
    """Different boat classes use different thresholds -> different scores."""
    # superyacht threshold = 3, small_sail threshold = 5
    # 3 medium reports for zone_type "pantry" = weighted score 6
    # -> problematic for superyacht (threshold 3), not for small_sail (threshold 5)?
    # Actually 3*2=6 >= both thresholds 3 and 5 for superyacht and small_sail.
    # Use exactly 4 weighted points: 2 medium reports = 2*2 = 4
    # -> crosses superyacht threshold (3) but NOT small_sail threshold (5)
    reports = [
        make_service_report(zone_type="pantry", severity="medium"),
        make_service_report(zone_type="pantry", severity="medium"),
    ]

    config_small = _default_config("small_sail")   # high_issue_threshold = 5
    config_super = _default_config("superyacht")   # high_issue_threshold = 3

    score_small, _, metrics_small = analyze_zone_type_issues([], reports, config_small)
    score_super, _, metrics_super = analyze_zone_type_issues([], reports, config_super)

    # superyacht is more sensitive: 4 >= 3, so it flags the issue
    assert score_super < score_small
    assert "pantry" in metrics_super["problematic_zone_types"]
    assert "pantry" not in metrics_small["problematic_zone_types"]


# ---------------------------------------------------------------------------
# test_config_overrides
# ---------------------------------------------------------------------------


def test_config_overrides():
    """Config overrides are applied and stored in config_used."""
    reports = [make_service_report()]
    result = run_service_patterns_analysis(
        [], [], "cruising_sail",
        service_reports=reports,
        config_overrides={"high_issue_threshold": 99},
    )
    assert result["config_used"]["high_issue_threshold"] == 99


# ---------------------------------------------------------------------------
# test_warnings_sorted_by_severity
# ---------------------------------------------------------------------------


def test_warnings_sorted_by_severity():
    """Warnings in the orchestrator result must be sorted critical -> warning -> info."""
    # Mix: many critical reports for one zone type + one non-critical material
    reports = [
        make_service_report(zone_type="engine", severity="critical"),
        make_service_report(zone_type="engine", severity="critical"),
        make_service_report(materials_involved=["Sperrholz"], boat_age_months=25),
        make_service_report(materials_involved=["Sperrholz"], boat_age_months=26),
        make_service_report(materials_involved=["Sperrholz"], boat_age_months=27),
        # add missing age data to trigger AGE_PATTERN_NO_DATA info
    ]
    result = run_service_patterns_analysis(
        [], [], "cruising_sail", service_reports=reports
    )
    severities = [w["severity"] for w in result["warnings"]]
    order = [SEVERITY_ORDER.get(s, 2) for s in severities]
    assert order == sorted(order), f"Warnings not sorted by severity: {severities}"


# ---------------------------------------------------------------------------
# test_full_integration
# ---------------------------------------------------------------------------


def test_full_integration():
    """Full integration: valid reports + zones -> correct result structure."""
    zones = [
        make_zone("Salon", "salon"),
        make_zone("Kabine", "cabin"),
        make_zone("Pantry", "pantry"),
    ]
    reports = [
        make_service_report(zone_type="cabin", severity="critical",
                            boat_age_months=28, materials_involved=["GFK-Laminat"]),
        make_service_report(zone_type="cabin", severity="high",
                            boat_age_months=30, materials_involved=["GFK-Laminat"]),
        make_service_report(zone_type="pantry", severity="medium",
                            boat_age_months=12),
        make_service_report(zone_type="cabin", severity="medium",
                            boat_age_months=32, materials_involved=["GFK-Laminat"]),
        make_service_report(zone_type="salon", severity="low",
                            boat_age_months=48),
    ]
    result = run_service_patterns_analysis(zones, [], "cruising_sail", service_reports=reports)

    assert result["module"] == "service_patterns"
    assert 0 <= result["overall_score"] <= 100
    assert set(result["sub_scores"].keys()) == {
        "zone_issues", "age_patterns", "material_failures", "design_warnings"
    }
    assert all(0 <= v <= 100 for v in result["sub_scores"].values())
    assert isinstance(result["warnings"], list)
    assert isinstance(result["suggestions"], list)
    assert isinstance(result["metrics"], dict)
    assert "config_used" in result
    # All warnings must have suggestion field
    for w in result["warnings"]:
        assert "suggestion" in w, f"Warning missing suggestion: {w}"
