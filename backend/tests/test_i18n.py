"""Tests for the i18n framework."""

import pytest
from app.core.i18n import (
    Locale,
    NumberFormatter,
    get_all_keys,
    get_locale,
    has_key,
    set_locale,
    t,
    validate_catalog,
)


class TestLocale:
    def test_default_locale_is_german(self):
        set_locale("de")  # Reset
        assert get_locale() == Locale.DE

    def test_set_locale_english(self):
        set_locale("en")
        assert get_locale() == Locale.EN
        set_locale("de")  # Reset

    def test_set_locale_spanish(self):
        set_locale("es")
        assert get_locale() == Locale.ES
        set_locale("de")

    def test_set_locale_french(self):
        set_locale("fr")
        assert get_locale() == Locale.FR
        set_locale("de")

    def test_set_locale_with_region(self):
        set_locale("de-DE")
        assert get_locale() == Locale.DE

    def test_set_locale_with_underscore(self):
        set_locale("en_US")
        assert get_locale() == Locale.EN
        set_locale("de")

    def test_set_locale_unknown_falls_back_to_german(self):
        set_locale("xx")
        assert get_locale() == Locale.DE

    def test_set_locale_with_enum(self):
        set_locale(Locale.FR)
        assert get_locale() == Locale.FR
        set_locale("de")


class TestTranslation:
    def test_translate_german(self):
        set_locale("de")
        assert t("common.yes") == "Ja"

    def test_translate_english(self):
        set_locale("en")
        result = t("common.yes")
        assert result == "Yes"
        set_locale("de")

    def test_translate_spanish(self):
        set_locale("es")
        assert t("common.yes") == "Si"
        set_locale("de")

    def test_translate_french(self):
        set_locale("fr")
        assert t("common.yes") == "Oui"
        set_locale("de")

    def test_translate_with_locale_override(self):
        set_locale("de")
        assert t("common.yes", locale=Locale.EN) == "Yes"

    def test_translate_missing_key_returns_key(self):
        result = t("nonexistent.key.here")
        assert result == "nonexistent.key.here"

    def test_translate_with_interpolation(self):
        set_locale("de")
        result = t("error.file_too_large", max_size="20")
        assert "20" in result
        assert "MB" in result

    def test_translate_with_missing_interpolation_var(self):
        set_locale("de")
        # Should not crash, returns text with unreplaced placeholder
        result = t("error.file_too_large")
        assert isinstance(result, str)

    def test_has_key_existing(self):
        assert has_key("common.yes") is True

    def test_has_key_missing(self):
        assert has_key("nonexistent") is False


class TestCatalogCompleteness:
    """Verify that all keys have translations in all 4 locales."""

    def test_all_keys_have_all_locales(self):
        errors = validate_catalog()
        assert errors == [], f"Missing translations:\n" + "\n".join(errors)

    def test_catalog_has_domain_keys(self):
        """All 10 analysis domains must have translation keys."""
        domains = [
            "domain.hull_structure",
            "domain.rigging_sails",
            "domain.propulsion_engine",
            "domain.electrical_electronics",
            "domain.sanitary_water",
            "domain.deck_fittings",
            "domain.interior",
            "domain.safety",
            "domain.navigation",
            "domain.maintenance_service",
        ]
        for domain in domains:
            assert has_key(domain), f"Missing domain key: {domain}"
            assert has_key(f"{domain}.desc"), f"Missing domain description: {domain}.desc"

    def test_catalog_has_module_keys(self):
        """All analysis modules must have translation keys."""
        modules = [
            "module.ergonomics", "module.volume_storage", "module.emotional",
            "module.compliance", "module.production", "module.materials",
            "module.structural", "module.cost", "module.service_patterns",
            "module.brand_dna", "module.market", "module.community",
        ]
        for module in modules:
            assert has_key(module), f"Missing module key: {module}"

    def test_catalog_has_confidence_keys(self):
        levels = [
            "confidence.measured", "confidence.calculated",
            "confidence.visual_high", "confidence.visual_medium",
            "confidence.visual_low", "confidence.visual_insufficient",
            "confidence.estimated", "confidence.benchmark", "confidence.documented",
        ]
        for level in levels:
            assert has_key(level), f"Missing confidence key: {level}"

    def test_catalog_has_boat_class_keys(self):
        classes = [
            "boat_class.small_sail", "boat_class.cruising_sail",
            "boat_class.performance_sail", "boat_class.bluewater_sail",
            "boat_class.catamaran_sail", "boat_class.small_motor",
            "boat_class.cruising_motor", "boat_class.large_motor",
            "boat_class.trawler", "boat_class.motorsailer",
            "boat_class.catamaran_power", "boat_class.superyacht",
            "boat_class.dinghy",
        ]
        for cls in classes:
            assert has_key(cls), f"Missing boat class key: {cls}"

    def test_marine_terminology_complete(self):
        """Key marine terms must exist in all 4 languages."""
        terms = [
            "marine.hull", "marine.keel", "marine.rudder", "marine.mast",
            "marine.shrouds", "marine.propeller", "marine.seacock",
            "marine.bilge", "marine.cockpit", "marine.companionway",
            "marine.galley", "marine.head", "marine.berth",
        ]
        for term in terms:
            assert has_key(term), f"Missing marine term: {term}"
            # Verify each locale has a non-empty value
            for locale in Locale:
                val = t(term, locale=locale)
                assert val != term, f"No translation for {term} in {locale.value}"
                assert len(val) > 0, f"Empty translation for {term} in {locale.value}"

    def test_minimum_key_count(self):
        """Catalog should have at least 150 keys for comprehensive coverage."""
        keys = get_all_keys()
        assert len(keys) >= 150, f"Only {len(keys)} keys — expected at least 150"


class TestNumberFormatter:
    def test_format_integer_german(self):
        result = NumberFormatter.format_number(1234, decimals=0, locale=Locale.DE)
        assert result == "1.234"

    def test_format_integer_english(self):
        result = NumberFormatter.format_number(1234, decimals=0, locale=Locale.EN)
        assert result == "1,234"

    def test_format_float_german(self):
        result = NumberFormatter.format_number(2997.50, decimals=2, locale=Locale.DE)
        assert result == "2.997,50"

    def test_format_float_english(self):
        result = NumberFormatter.format_number(2997.50, decimals=2, locale=Locale.EN)
        assert result == "2,997.50"

    def test_format_float_french(self):
        result = NumberFormatter.format_number(1234.56, decimals=2, locale=Locale.FR)
        # French uses narrow no-break space as thousands separator
        assert "1" in result
        assert "234" in result
        assert ",56" in result

    def test_format_currency_german(self):
        result = NumberFormatter.format_currency(2997.00, locale=Locale.DE)
        assert "\u20ac" in result  # Euro sign
        assert "2.997" in result

    def test_format_currency_english(self):
        result = NumberFormatter.format_currency(2997.00, locale=Locale.EN)
        assert "\u20ac" in result
        assert "2,997" in result

    def test_format_negative(self):
        result = NumberFormatter.format_number(-1234.56, decimals=2, locale=Locale.DE)
        assert result.startswith("-")
        assert "1.234,56" in result

    def test_format_zero(self):
        result = NumberFormatter.format_number(0, decimals=2, locale=Locale.DE)
        assert result == "0,00"

    def test_format_small_number(self):
        result = NumberFormatter.format_number(0.3, decimals=1, locale=Locale.DE)
        assert result == "0,3"

    def test_format_large_number(self):
        result = NumberFormatter.format_number(1234567.89, decimals=2, locale=Locale.DE)
        assert result == "1.234.567,89"

    def test_format_percentage(self):
        result = NumberFormatter.format_percentage(0.856, decimals=1, locale=Locale.DE)
        assert "85,6" in result
        assert "%" in result
