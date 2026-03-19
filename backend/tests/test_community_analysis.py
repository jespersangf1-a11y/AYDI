"""Tests for Community Intelligence analysis module."""
import pytest


def _make_pattern(
    severity="major", relevance=0.8, confidence=0.7, report_count=5,
    category="material_degradation", zone_type="hull",
    description="Osmoseblasen am Unterwasserschiff", typical_onset_years=6.0,
    is_positive=False, match_reason="manufacturer",
):
    return {
        "pattern_id": 1, "relevance": relevance, "category": category,
        "zone_type": zone_type, "description": description, "report_count": report_count,
        "severity": severity, "typical_onset_years": typical_onset_years,
        "materials_involved": ["grp_solid"], "confidence": confidence,
        "match_reason": match_reason, "is_positive": is_positive,
    }

def _make_positive(**kwargs):
    defaults = {"severity": "positive", "is_positive": True,
                "description": "Kielstruktur direkt laminiert", "category": "structural"}
    defaults.update(kwargs)
    return _make_pattern(**defaults)

def _zones():
    return [{"name": "salon", "zone_type": "salon"}]

def _passages():
    return [{"from_zone": "salon", "to_zone": "cockpit", "width_mm": 700}]


class TestSkipLogic:
    def test_no_patterns_returns_unavailable(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=[])
        assert result["available"] is False
        assert "Keine Community-Daten" in result["reason"]

    def test_none_patterns_returns_unavailable(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=None)
        assert result["available"] is False


class TestKnownIssuesScoring:
    def test_critical_pattern_reduces_score_heavily(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern(severity="critical", relevance=1.0, confidence=1.0)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        assert result["available"] is True
        assert result["sub_scores"]["known_issues"]["score"] < 80

    def test_minor_pattern_reduces_score_slightly(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern(severity="minor", relevance=0.5, confidence=0.5)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        assert result["sub_scores"]["known_issues"]["score"] > 90

    def test_multiple_patterns_accumulate(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [
            _make_pattern(severity="major", relevance=0.8, confidence=0.7),
            _make_pattern(severity="major", relevance=0.6, confidence=0.6, zone_type="deck", description="Teakfugen undicht"),
        ]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        single_result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=[patterns[0]])
        assert result["sub_scores"]["known_issues"]["score"] < single_result["sub_scores"]["known_issues"]["score"]

    def test_score_floors_at_zero(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern(severity="critical", relevance=1.0, confidence=1.0) for _ in range(10)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        assert result["sub_scores"]["known_issues"]["score"] >= 0


class TestPositiveReputationScoring:
    def test_no_positives_returns_neutral(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=[_make_pattern()])
        assert result["sub_scores"]["positive_reputation"]["score"] == 50

    def test_positives_increase_score(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=[_make_positive(relevance=1.0, confidence=0.9)])
        assert result["sub_scores"]["positive_reputation"]["score"] > 50

    def test_positive_score_caps_at_100(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_positive(relevance=1.0, confidence=1.0) for _ in range(20)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        assert result["sub_scores"]["positive_reputation"]["score"] <= 100


class TestDataCoverageScoring:
    def test_few_patterns_low_coverage(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=[_make_pattern()])
        assert result["sub_scores"]["data_coverage"]["score"] < 20

    def test_many_patterns_high_coverage(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern(zone_type=f"zone_{i}") for i in range(20)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        assert result["sub_scores"]["data_coverage"]["score"] == 100


class TestOverallScore:
    def test_overall_is_weighted_combination(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=[_make_pattern(), _make_positive()])
        ki = result["sub_scores"]["known_issues"]["score"]
        pr = result["sub_scores"]["positive_reputation"]["score"]
        dc = result["sub_scores"]["data_coverage"]["score"]
        assert abs(result["overall_score"] - (ki * 0.50 + pr * 0.30 + dc * 0.20)) < 0.1


class TestWarningsAndSuggestions:
    def test_critical_pattern_generates_warning(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=[_make_pattern(severity="critical", confidence=0.5)])
        assert len(result["warnings"]) == 1
        w = result["warnings"][0]
        assert w["code"] == "COMMUNITY_KNOWN_ISSUE"
        assert w["severity"] == "critical"
        assert "COMMUNITY:" in w["message"]
        assert "Berichte" in w["message"]

    def test_major_pattern_generates_warning(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=[_make_pattern(severity="major", confidence=0.5)])
        assert len(result["warnings"]) == 1
        assert result["warnings"][0]["severity"] == "warning"

    def test_minor_pattern_no_warning(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=[_make_pattern(severity="minor", confidence=0.5)])
        assert len(result["warnings"]) == 0

    def test_low_confidence_filtered(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=[_make_pattern(severity="critical", confidence=0.2)])
        assert len(result["warnings"]) == 0

    def test_each_warning_has_suggestion(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=[_make_pattern(severity="critical", confidence=0.5)])
        assert len(result["suggestions"]) == len(result["warnings"])
        assert result["suggestions"][0]["code"] == "COMMUNITY_CHECK_RECOMMENDATION"
        assert "sorgfältig" in result["suggestions"][0]["message"]


class TestConfigOverrides:
    def test_custom_min_confidence(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail",
            config_overrides={"min_confidence": 0.5},
            community_patterns=[_make_pattern(severity="critical", confidence=0.35)])
        assert len(result["warnings"]) == 0


class TestMetrics:
    def test_metrics_present(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=[_make_pattern(), _make_positive()])
        m = result["metrics"]
        assert m["total_patterns_found"] == 2
        assert m["negative_patterns"] == 1
        assert m["positive_patterns"] == 1
        assert "most_common_category" in m
        assert "earliest_typical_onset_years" in m


class TestReturnFormat:
    def test_standard_module_return(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=[_make_pattern()])
        assert result["module"] == "community"
        assert result["available"] is True
        assert "overall_score" in result
        assert "sub_scores" in result
        assert "warnings" in result
        assert "suggestions" in result
        assert "metrics" in result
        assert result["confidence"] == "documented"
        assert "config_used" in result
