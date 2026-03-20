"""Tests for CommunityPatternAggregator and CommunityKnowledgeEngine."""
import pytest
from tests.conftest import make_community_report, make_community_pattern


# =========================================================================
# Aggregator Tests
# =========================================================================

class TestAggregatorBasic:
    def test_three_reports_create_pattern(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(
                boat_manufacturer="Bavaria",
                boat_model="38 Cruiser",
                issues=[{
                    "category": "material_degradation",
                    "zone_type": "hull",
                    "description": "Osmoseblasen am Unterwasserschiff",
                    "severity": "major",
                    "boat_age_months": 60 + i * 12,
                }],
            )
            for i in range(3)
        ]
        patterns = aggregate_reports_to_patterns(reports)
        matching = [p for p in patterns if p["manufacturer"] == "Bavaria"
                    and p["boat_model"] == "38 Cruiser"
                    and p["issue_category"] == "material_degradation"]
        assert len(matching) >= 1
        p = matching[0]
        assert p["report_count"] == 3
        assert p["is_positive"] is False

    def test_two_reports_below_threshold(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(
                boat_manufacturer="Hanse",
                boat_model="415",
                issues=[{
                    "category": "hardware",
                    "zone_type": "deck",
                    "description": "Relingstützen lockern",
                    "severity": "minor",
                    "boat_age_months": 36,
                }],
            )
            for _ in range(2)
        ]
        patterns = aggregate_reports_to_patterns(reports)
        matching = [p for p in patterns if p["manufacturer"] == "Hanse"
                    and p["boat_model"] == "415"
                    and p["issue_category"] == "hardware"]
        assert len(matching) == 0


class TestAggregatorSeverityAndOnset:
    def test_severity_mode(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(issues=[{
                "category": "structural", "zone_type": "hull",
                "description": "Riss", "severity": sev, "boat_age_months": 60,
            }])
            for sev in ["major", "major", "critical"]
        ]
        patterns = aggregate_reports_to_patterns(reports)
        structural = [p for p in patterns if p["issue_category"] == "structural"
                      and p["manufacturer"] == "Bavaria"]
        assert len(structural) >= 1
        assert structural[0]["severity_mode"] == "major"  # mode is major (2 vs 1)

    def test_onset_median(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(issues=[{
                "category": "cosmetic", "zone_type": "deck",
                "description": "Verfärbung", "severity": "cosmetic",
                "boat_age_months": months,
            }])
            for months in [24, 36, 60]
        ]
        patterns = aggregate_reports_to_patterns(reports)
        matching = [p for p in patterns if p["issue_category"] == "cosmetic"]
        assert len(matching) >= 1
        # median of [24, 36, 60] months = 36 months = 3.0 years
        assert matching[0]["typical_onset_years"] == 3.0


class TestAggregatorConfidence:
    def test_confidence_formula(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(
                reliability=0.8,
                issues=[{
                    "category": "electrical", "zone_type": "engine_room",
                    "description": "Kabelbruch", "severity": "major",
                    "boat_age_months": 48,
                }],
            )
            for _ in range(5)
        ]
        patterns = aggregate_reports_to_patterns(reports)
        matching = [p for p in patterns if p["issue_category"] == "electrical"]
        assert len(matching) >= 1
        # confidence = min(1.0, 5/10) × mean(0.8) = 0.5 × 0.8 = 0.4
        assert abs(matching[0]["confidence"] - 0.4) < 0.01

    def test_low_reliability_skipped(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(
                reliability=0.2,  # below 0.3 threshold
                issues=[{
                    "category": "design_flaw", "zone_type": "cabin",
                    "description": "Schlechtes Design", "severity": "minor",
                    "boat_age_months": 12,
                }],
            )
            for _ in range(5)
        ]
        patterns = aggregate_reports_to_patterns(reports)
        matching = [p for p in patterns if p["issue_category"] == "design_flaw"]
        assert len(matching) == 0  # all reports filtered out


class TestAggregatorPositive:
    def test_positive_patterns_aggregated(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(
                issues=[],
                positives=[{
                    "category": "structural",
                    "zone_type": "hull",
                    "description": "Hervorragende Kielstruktur",
                }],
            )
            for _ in range(3)
        ]
        patterns = aggregate_reports_to_patterns(reports)
        positives = [p for p in patterns if p["is_positive"] is True]
        assert len(positives) >= 1
        assert positives[0]["report_count"] == 3


class TestAggregatorConstructionLevel:
    def test_cross_manufacturer_construction_patterns(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(
                boat_manufacturer=mfr,
                boat_model=None,
                hull_material="grp_solid",
                hull_construction="hand_layup",
                issues=[{
                    "category": "material_degradation", "zone_type": "hull",
                    "description": "Print-through sichtbar", "severity": "cosmetic",
                    "boat_age_months": 36,
                }],
            )
            for mfr in ["Bavaria", "Hanse", "Jeanneau"]
        ]
        patterns = aggregate_reports_to_patterns(reports)
        # Should create a construction-level pattern (manufacturer=None)
        construction = [p for p in patterns if p["manufacturer"] is None
                        and "hand_layup" in (p.get("construction_methods_involved") or [])]
        assert len(construction) >= 1


class TestAggregatorIdempotent:
    def test_running_twice_same_result(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(issues=[{
                "category": "hardware", "zone_type": "deck",
                "description": "Beschlag lose", "severity": "minor",
                "boat_age_months": 24,
            }])
            for _ in range(4)
        ]
        result1 = aggregate_reports_to_patterns(reports)
        result2 = aggregate_reports_to_patterns(reports)
        assert len(result1) == len(result2)
        for p1, p2 in zip(
            sorted(result1, key=lambda p: (p["manufacturer"] or "", p["issue_category"])),
            sorted(result2, key=lambda p: (p["manufacturer"] or "", p["issue_category"])),
        ):
            assert p1["report_count"] == p2["report_count"]
            assert p1["severity_mode"] == p2["severity_mode"]


# =========================================================================
# Engine Tests (pure-function version)
# =========================================================================

class TestEngineExactModel:
    def test_exact_model_match_relevance_1(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [make_community_pattern(manufacturer="Bavaria", boat_model="38 Cruiser")]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Bavaria", model="38 Cruiser",
        )
        assert len(result) == 1
        assert result[0]["relevance"] == 1.0
        assert result[0]["match_reason"] == "exact_model"

    def test_no_match_returns_empty(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [make_community_pattern(manufacturer="Hanse", boat_model="415")]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Bavaria", model="38 Cruiser",
        )
        model_matches = [r for r in result if r["match_reason"] == "exact_model"]
        assert len(model_matches) == 0


class TestEngineManufacturer:
    def test_manufacturer_wide_match(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [make_community_pattern(manufacturer="Bavaria", boat_model=None)]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Bavaria", model="40 Sport",
        )
        mfr_matches = [r for r in result if r["match_reason"] == "manufacturer"]
        assert len(mfr_matches) == 1
        assert mfr_matches[0]["relevance"] == 0.8


class TestEngineConstructionMethod:
    def test_construction_method_match(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [make_community_pattern(
            manufacturer=None, boat_model=None,
            construction_methods_involved=["hand_layup"],
            materials_involved=["grp_solid"],
        )]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Jeanneau", model="Sun Odyssey 410",
        )
        construction_matches = [r for r in result if r["match_reason"] == "construction_method"]
        assert len(construction_matches) == 1
        assert construction_matches[0]["relevance"] == 0.6


class TestEngineMaterial:
    def test_material_only_match(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [make_community_pattern(
            manufacturer=None, boat_model=None,
            materials_involved=["grp_solid"],
            construction_methods_involved=["resin_infusion"],
        )]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Unknown", model=None,
        )
        mat_matches = [r for r in result if r["match_reason"] == "material"]
        assert len(mat_matches) == 1
        assert mat_matches[0]["relevance"] == 0.4


class TestEngineZoneCategory:
    def test_zone_category_fallback(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [make_community_pattern(
            manufacturer="SomeOther", boat_model="X99",
            zone_type="deck", issue_category="material_degradation",
            materials_involved=["aluminium"],
            construction_methods_involved=["welded"],
        )]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Bavaria", model="38",
        )
        zone_matches = [r for r in result if r["match_reason"] == "zone_category"]
        assert len(zone_matches) == 1
        assert zone_matches[0]["relevance"] == 0.3


class TestEngineDeduplication:
    def test_same_pattern_highest_relevance_wins(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [make_community_pattern(manufacturer="Bavaria", boat_model="38 Cruiser")]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Bavaria", model="38 Cruiser",
        )
        ids = [r["pattern_id"] for r in result]
        assert len(ids) == len(set(ids))


class TestEngineMaxResults:
    def test_results_capped(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [
            make_community_pattern(
                manufacturer="Bavaria", boat_model=None,
                zone_type=f"zone_{i}", source_report_ids=[i],
            )
            for i in range(30)
        ]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Bavaria", model="38",
            max_results=10,
        )
        assert len(result) <= 10


class TestEnginePositive:
    def test_positive_patterns_returned(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [make_community_pattern(
            manufacturer="Bavaria", boat_model="38 Cruiser",
            is_positive=True, severity_mode="positive",
            description="Hervorragende Kielstruktur",
        )]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Bavaria", model="38 Cruiser",
            include_positive=True,
        )
        assert len(result) == 1
        assert result[0]["is_positive"] is True
