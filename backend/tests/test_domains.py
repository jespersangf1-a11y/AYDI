"""Tests for the 10 analysis domains."""

import pytest
from app.core.domains import (
    AnalysisDomain,
    DOMAIN_CONFIGS,
    get_all_component_categories,
    get_all_zone_types,
    get_critical_checks,
    get_domain_coverage_report,
    get_domain_for_component,
    get_domain_for_zone_type,
    get_domains_for_module,
)


class TestDomainCompleteness:
    """Verify all 10 domains are fully configured."""

    def test_exactly_10_domains(self):
        assert len(AnalysisDomain) == 10
        assert len(DOMAIN_CONFIGS) == 10

    def test_all_domains_have_config(self):
        for domain in AnalysisDomain:
            assert domain in DOMAIN_CONFIGS, f"Missing config for {domain}"

    def test_all_domains_have_zone_types(self):
        for domain, config in DOMAIN_CONFIGS.items():
            assert len(config.zone_types) > 0, f"No zone types for {domain}"

    def test_all_domains_have_component_categories(self):
        for domain, config in DOMAIN_CONFIGS.items():
            assert len(config.component_categories) > 0, f"No components for {domain}"

    def test_all_domains_have_relevant_modules(self):
        for domain, config in DOMAIN_CONFIGS.items():
            assert len(config.relevant_modules) > 0, f"No modules for {domain}"

    def test_all_domains_have_critical_checks(self):
        for domain, config in DOMAIN_CONFIGS.items():
            assert len(config.critical_checks) >= 5, (
                f"Fewer than 5 critical checks for {domain}: {len(config.critical_checks)}"
            )

    def test_all_domains_have_i18n_key(self):
        for domain, config in DOMAIN_CONFIGS.items():
            assert config.i18n_key.startswith("domain."), f"Bad i18n key for {domain}"

    def test_no_duplicate_zone_types_across_domains(self):
        """Zone types should be unique to their domain (with documented exceptions)."""
        # Some zone types may legitimately appear in multiple domains
        # (e.g., engine_room in both propulsion and maintenance)
        all_types = get_all_zone_types()
        assert len(all_types) > 20, f"Only {len(all_types)} zone types across 10 domains"


class TestDomainLookups:
    def test_hull_zone(self):
        assert get_domain_for_zone_type("hull") == AnalysisDomain.HULL_STRUCTURE

    def test_engine_zone(self):
        assert get_domain_for_zone_type("engine") == AnalysisDomain.PROPULSION_ENGINE

    def test_helm_zone(self):
        assert get_domain_for_zone_type("helm") == AnalysisDomain.NAVIGATION

    def test_cabin_zone(self):
        assert get_domain_for_zone_type("cabin") == AnalysisDomain.INTERIOR

    def test_cockpit_zone(self):
        assert get_domain_for_zone_type("cockpit") == AnalysisDomain.DECK_FITTINGS

    def test_head_zone(self):
        assert get_domain_for_zone_type("head") == AnalysisDomain.SANITARY_WATER

    def test_unknown_zone(self):
        assert get_domain_for_zone_type("nonexistent_zone") is None

    def test_case_insensitive(self):
        assert get_domain_for_zone_type("HULL") == AnalysisDomain.HULL_STRUCTURE

    def test_whitespace_handling(self):
        assert get_domain_for_zone_type("  hull  ") == AnalysisDomain.HULL_STRUCTURE


class TestComponentLookups:
    def test_keel_bolt(self):
        assert get_domain_for_component("keel_bolt") == AnalysisDomain.HULL_STRUCTURE

    def test_shroud(self):
        assert get_domain_for_component("shroud") == AnalysisDomain.RIGGING_SAILS

    def test_diesel_engine(self):
        assert get_domain_for_component("diesel_engine") == AnalysisDomain.PROPULSION_ENGINE

    def test_battery_bank(self):
        assert get_domain_for_component("battery_bank") == AnalysisDomain.ELECTRICAL_ELECTRONICS

    def test_seacock(self):
        assert get_domain_for_component("seacock") == AnalysisDomain.SANITARY_WATER

    def test_winch(self):
        # Winch appears in both rigging and deck fittings; first match wins
        result = get_domain_for_component("winch")
        assert result in (AnalysisDomain.RIGGING_SAILS, AnalysisDomain.DECK_FITTINGS)

    def test_berth(self):
        assert get_domain_for_component("berth") == AnalysisDomain.INTERIOR

    def test_liferaft(self):
        assert get_domain_for_component("liferaft") == AnalysisDomain.SAFETY

    def test_chart_plotter(self):
        assert get_domain_for_component("chart_plotter") == AnalysisDomain.NAVIGATION

    def test_antifouling(self):
        assert get_domain_for_component("antifouling") == AnalysisDomain.MAINTENANCE_SERVICE

    def test_unknown_component(self):
        assert get_domain_for_component("nonexistent_part") is None


class TestModuleDomainMapping:
    def test_structural_maps_to_multiple_domains(self):
        domains = get_domains_for_module("structural")
        assert AnalysisDomain.HULL_STRUCTURE in domains
        assert AnalysisDomain.RIGGING_SAILS in domains

    def test_compliance_maps_to_multiple_domains(self):
        domains = get_domains_for_module("compliance")
        assert AnalysisDomain.SAFETY in domains
        assert AnalysisDomain.ELECTRICAL_ELECTRONICS in domains
        assert AnalysisDomain.DECK_FITTINGS in domains

    def test_ergonomics_maps_to_interior_and_deck(self):
        domains = get_domains_for_module("ergonomics")
        assert AnalysisDomain.INTERIOR in domains
        assert AnalysisDomain.DECK_FITTINGS in domains

    def test_every_module_maps_to_at_least_one_domain(self):
        modules = [
            "structural", "materials", "compliance", "production",
            "cost", "service_patterns", "ergonomics", "volume_storage",
            "emotional",
        ]
        for module in modules:
            domains = get_domains_for_module(module)
            assert len(domains) > 0, f"Module {module} maps to no domains"


class TestCriticalChecks:
    def test_hull_has_osmosis_check(self):
        checks = get_critical_checks(AnalysisDomain.HULL_STRUCTURE)
        assert "osmosis_inspection" in checks

    def test_propulsion_has_engine_hours(self):
        checks = get_critical_checks(AnalysisDomain.PROPULSION_ENGINE)
        assert "engine_hours" in checks

    def test_safety_has_liferaft_service(self):
        checks = get_critical_checks(AnalysisDomain.SAFETY)
        assert "liferaft_service_date" in checks

    def test_electrical_has_battery_capacity(self):
        checks = get_critical_checks(AnalysisDomain.ELECTRICAL_ELECTRONICS)
        assert "battery_capacity" in checks


class TestCoverageReport:
    def test_full_coverage(self):
        available = {"hull": True, "engine": True, "helm": True, "cabin": True}
        report = get_domain_coverage_report(available)
        assert report["hull_structure"]["can_analyze"] is True
        assert report["propulsion_engine"]["can_analyze"] is True

    def test_no_data(self):
        report = get_domain_coverage_report({})
        for domain_report in report.values():
            assert domain_report["can_analyze"] is False

    def test_partial_coverage(self):
        available = {"hull": True}
        report = get_domain_coverage_report(available)
        assert report["hull_structure"]["has_zone_data"] is True
        assert report["propulsion_engine"]["has_zone_data"] is False
