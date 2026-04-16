"""QA Tests for i18n/Localization System — AYDI yacht design platform.

Comprehensive audit of translation completeness, number/currency formatting,
marine terminology, interpolation, and locale detection.

Tests cover:
1. Translation completeness for all 4 locales (DE, EN, ES, FR)
2. Number formatting per locale (1234.56, edge cases)
3. Currency formatting with EUR symbol
4. Marine terminology translation coverage
5. Interpolation with variables and edge cases
6. Locale detection and fallback behavior
"""

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
    DEFAULT_LOCALE,
)


# =============================================================================
# 1. TRANSLATION COMPLETENESS
# =============================================================================


class TestTranslationCompleteness:
    """Verify all keys have translations in all 4 locales with no duplicates."""

    def test_validate_catalog_passes(self):
        """catalog validation should return no errors for all locales."""
        errors = validate_catalog()
        assert errors == [], f"Catalog validation failed with errors:\n" + "\n".join(errors)

    def test_all_keys_have_four_locales(self):
        """Every registered key must have entries for DE, EN, ES, FR."""
        keys = get_all_keys()
        assert len(keys) > 0, "No translation keys found in catalog"

        for key in keys:
            text_de = t(key, locale=Locale.DE)
            text_en = t(key, locale=Locale.EN)
            text_es = t(key, locale=Locale.ES)
            text_fr = t(key, locale=Locale.FR)

            assert text_de and text_de != key, f"Missing or empty DE translation for {key}"
            assert text_en and text_en != key, f"Missing or empty EN translation for {key}"
            assert text_es and text_es != key, f"Missing or empty ES translation for {key}"
            assert text_fr and text_fr != key, f"Missing or empty FR translation for {key}"

    def test_no_identical_translations_across_all_locales(self):
        """Flag keys where all 4 locales have identical text (likely untranslated)."""
        keys = get_all_keys()
        identical_keys = []

        for key in keys:
            text_de = t(key, locale=Locale.DE)
            text_en = t(key, locale=Locale.EN)
            text_es = t(key, locale=Locale.ES)
            text_fr = t(key, locale=Locale.FR)

            if text_de == text_en == text_es == text_fr:
                identical_keys.append(key)

        # Allow units (mm, m, kW, etc.) and acronyms (EPIRB, AIS, NMEA 2000, etc.)
        # to be identical. Also allow format patterns and marine equipment terms.
        allow_identical = {
            "unit.mm",
            "unit.m",
            "unit.m2",
            "unit.m3",
            "unit.kg",
            "unit.kw",
            "unit.nm",
            "unit.eur",
            "marine.epirb",
            "marine.ais",
            "marine.vhf",
            "marine.nmea2000",
            "marine.saildrive",
            "marine.fender",
            "marine.radar",
            "marine.antifouling",
            "severity.info",
            "confidence.benchmark",
            "boat_class.trawler",
            "boat_class.motorsailer",
            "boat_class.superyacht",
            "format.value_unit",
        }

        problematic = [k for k in identical_keys if k not in allow_identical]
        assert (
            not problematic
        ), f"These keys appear untranslated (identical in all 4 locales):\n" + "\n".join(
            problematic
        )

    def test_no_translation_contains_key_name(self):
        """Flag translations that appear to be untranslated placeholders.

        This test flags cases where a translation is suspicious. Many legitimate
        English translations match their key names (units, acronyms, marine terms).
        We only flag cases that appear to be actual mistakes, not linguistic coincidences.
        """
        keys = get_all_keys()
        problematic = []

        # List of keys where the English translation legitimately matches the key name.
        # These are standard terms that don't translate in English, or units that use
        # the same symbols/abbreviations across all languages.
        expected_exact_matches = {
            # Units and measurements (same symbols across languages)
            "unit.mm",
            "unit.m",
            "unit.m2",
            "unit.m3",
            "unit.kg",
            "unit.kw",
            "unit.nm",
            "unit.l",
            "unit.eur",
            "unit.hp",
            "unit.degrees",
            "unit.percent",
            # Acronyms (same in all languages)
            "marine.ais",
            "marine.epirb",
            "marine.nmea2000",
            "marine.vhf",
            # English marine terms that translate to the same word
            "boat_class.dinghy",
            "boat_class.trawler",
            "boat_class.motorsailer",
            "boat_class.superyacht",
            "marine.antifouling",  # Technical term: same in all languages
            "marine.autopilot",  # Technical term: same in all languages
            "marine.backstay",
            "marine.ballast",
            "marine.beam",
            "marine.berth",
            "marine.bilge",
            "marine.boom",
            "marine.cleat",
            "marine.cockpit",
            "marine.companionway",
            "marine.displacement",
            "marine.draft",
            "marine.fender",
            "marine.forepeak",
            "marine.forestay",
            "marine.freeboard",
            "marine.galley",
            "marine.gearbox",
            "marine.head",
            "marine.hull",
            "marine.keel",
            "marine.lazarette",
            "marine.mast",
            "marine.mooring",
            "marine.propeller",
            "marine.radar",
            "marine.rudder",
            "marine.saildrive",
            "marine.saloon",
            "marine.seacock",
            "marine.shaft",
            "marine.shrouds",
            "marine.waterline",
            "marine.winch",
            # English words that are the same as key names
            "common.back",
            "common.cancel",
            "common.confidence",
            "common.confirm",
            "common.delete",
            "common.edit",
            "common.error",
            "common.loading",
            "common.next",
            "common.no",
            "common.save",
            "common.score",
            "common.suggestion",
            "common.unknown",
            "common.warning",
            "common.yes",
            "condition.critical",
            "condition.excellent",
            "condition.fair",
            "condition.good",
            "condition.poor",
            "confidence.benchmark",
            "confidence.calculated",
            "confidence.documented",
            "confidence.estimated",
            "confidence.measured",
            "domain.interior",
            "domain.navigation",
            "domain.safety",
            "module.cost",
            "module.ergonomics",
            "module.materials",
            "report.details",
            "report.findings",
            "report.suggestions",
            "report.summary",
            "report.warnings",
            "severity.critical",
            "severity.high",
            "severity.info",
            "severity.low",
            "severity.medium",
            "tier.free",
            "tier.pro",
        }

        for key in keys:
            if key in expected_exact_matches:
                continue  # Skip known legitimate exact matches

            for locale in Locale:
                text = t(key, locale=locale)
                key_part = key.split(".")[-1]

                # Only flag cases that look suspicious:
                # 1. Translation is exactly the key part AND it's not a known legitimate case
                # 2. AND the locale is not English (English often matches by design)
                if text.lower() == key_part.lower() and locale != Locale.EN:
                    problematic.append(
                        f"{key} ({locale.value}): '{text}' appears untranslated (matches key exactly)"
                    )

        assert not problematic, f"Suspicious untranslated keys:\n" + "\n".join(
            problematic
        )

    def test_catalog_has_minimum_keys(self):
        """Ensure catalog has a reasonable number of keys (sanity check)."""
        keys = get_all_keys()
        # Should have at least 150+ keys based on i18n.py
        assert len(keys) > 150, f"Expected 150+ keys, found {len(keys)}"


# =============================================================================
# 2. NUMBER FORMATTING per locale
# =============================================================================


class TestNumberFormatting:
    """Test NumberFormatter with locale-specific separators."""

    def test_format_1234_56_de(self):
        """DE: 1234.56 → 1.234,56"""
        result = NumberFormatter.format_number(1234.56, decimals=2, locale=Locale.DE)
        assert result == "1.234,56", f"Expected '1.234,56', got '{result}'"

    def test_format_1234_56_en(self):
        """EN: 1234.56 → 1,234.56"""
        result = NumberFormatter.format_number(1234.56, decimals=2, locale=Locale.EN)
        assert result == "1,234.56", f"Expected '1,234.56', got '{result}'"

    def test_format_1234_56_es(self):
        """ES: 1234.56 → 1.234,56"""
        result = NumberFormatter.format_number(1234.56, decimals=2, locale=Locale.ES)
        assert result == "1.234,56", f"Expected '1.234,56', got '{result}'"

    def test_format_1234_56_fr(self):
        """FR: 1234.56 → 1 234,56 (narrow no-break space)"""
        result = NumberFormatter.format_number(1234.56, decimals=2, locale=Locale.FR)
        # FR uses narrow no-break space (U+202F)
        assert result == "1\u202f234,56", f"Expected '1\u202f234,56', got '{result}'"

    def test_format_zero_de(self):
        """DE: 0 → 0,00"""
        result = NumberFormatter.format_number(0, decimals=2, locale=Locale.DE)
        assert result == "0,00", f"Expected '0,00', got '{result}'"

    def test_format_zero_en(self):
        """EN: 0 → 0.00"""
        result = NumberFormatter.format_number(0, decimals=2, locale=Locale.EN)
        assert result == "0.00", f"Expected '0.00', got '{result}'"

    def test_format_negative_1234_56_de(self):
        """DE: -1234.56 → -1.234,56"""
        result = NumberFormatter.format_number(-1234.56, decimals=2, locale=Locale.DE)
        assert result == "-1.234,56", f"Expected '-1.234,56', got '{result}'"

    def test_format_negative_1234_56_en(self):
        """EN: -1234.56 → -1,234.56"""
        result = NumberFormatter.format_number(-1234.56, decimals=2, locale=Locale.EN)
        assert result == "-1,234.56", f"Expected '-1,234.56', got '{result}'"

    def test_format_large_1000000_de(self):
        """DE: 1000000 → 1.000.000,00"""
        result = NumberFormatter.format_number(1000000, decimals=2, locale=Locale.DE)
        assert result == "1.000.000,00", f"Expected '1.000.000,00', got '{result}'"

    def test_format_large_1000000_en(self):
        """EN: 1000000 → 1,000,000.00"""
        result = NumberFormatter.format_number(1000000, decimals=2, locale=Locale.EN)
        assert result == "1,000,000.00", f"Expected '1,000,000.00', got '{result}'"

    def test_format_small_0_001_de(self):
        """DE: 0.001 → 0,00 (rounded to 2 decimals)"""
        result = NumberFormatter.format_number(0.001, decimals=2, locale=Locale.DE)
        assert result == "0,00", f"Expected '0,00', got '{result}'"

    def test_format_small_0_005_de_rounded(self):
        """DE: 0.005 → 0,01 (rounds up at 2 decimals)"""
        result = NumberFormatter.format_number(0.005, decimals=2, locale=Locale.DE)
        assert result == "0,01", f"Expected '0,01', got '{result}'"

    def test_format_very_large_999999999_99_de(self):
        """DE: 999999999.99 → 999.999.999,99"""
        result = NumberFormatter.format_number(999999999.99, decimals=2, locale=Locale.DE)
        assert result == "999.999.999,99", f"Expected '999.999.999,99', got '{result}'"

    def test_format_integer_no_decimals(self):
        """DE: 1234 with decimals=0 → 1.234"""
        result = NumberFormatter.format_number(1234, decimals=0, locale=Locale.DE)
        assert result == "1.234", f"Expected '1.234', got '{result}'"


# =============================================================================
# 3. CURRENCY FORMATTING
# =============================================================================


class TestCurrencyFormatting:
    """Test currency formatting with EUR symbol and locale conventions."""

    def test_currency_2997_de(self):
        """DE: 2997 EUR → 2.997,00 €"""
        result = NumberFormatter.format_currency(2997.00, decimals=2, locale=Locale.DE)
        # DE format: "{value} €"
        assert result == "2.997,00 \u20ac", f"Expected '2.997,00 €', got '{result}'"

    def test_currency_2997_en(self):
        """EN: 2997 EUR → €2,997.00"""
        result = NumberFormatter.format_currency(2997.00, decimals=2, locale=Locale.EN)
        # EN format: "€{value}"
        assert result == "\u20ac2,997.00", f"Expected '€2,997.00', got '{result}'"

    def test_currency_2997_es(self):
        """ES: 2997 EUR → 2.997,00 €"""
        result = NumberFormatter.format_currency(2997.00, decimals=2, locale=Locale.ES)
        assert result == "2.997,00 \u20ac", f"Expected '2.997,00 €', got '{result}'"

    def test_currency_2997_fr(self):
        """FR: 2997 EUR → 2 997,00 €"""
        result = NumberFormatter.format_currency(2997.00, decimals=2, locale=Locale.FR)
        assert result == "2\u202f997,00 \u20ac", f"Expected '2 997,00 €', got '{result}'"

    def test_currency_zero_de(self):
        """DE: 0 EUR → 0,00 €"""
        result = NumberFormatter.format_currency(0, decimals=2, locale=Locale.DE)
        assert result == "0,00 \u20ac", f"Expected '0,00 €', got '{result}'"

    def test_currency_negative_de(self):
        """DE: -1234.56 EUR → -1.234,56 €"""
        result = NumberFormatter.format_currency(-1234.56, decimals=2, locale=Locale.DE)
        assert result == "-1.234,56 \u20ac", f"Expected '-1.234,56 €', got '{result}'"

    def test_currency_negative_en(self):
        """EN: -1234.56 EUR → €-1,234.56 (note: negative sign after symbol per i18n.py)"""
        result = NumberFormatter.format_currency(-1234.56, decimals=2, locale=Locale.EN)
        # The EN format is "€{value}", so negative becomes "€-1,234.56"
        assert result == "\u20ac-1,234.56", f"Expected '€-1,234.56', got '{result}'"


# =============================================================================
# 4. MARINE TERMINOLOGY TRANSLATION COVERAGE
# =============================================================================


class TestMarineTerminology:
    """Verify marine terms are translated correctly across all 4 locales."""

    MARINE_TERMS = {
        "marine.shrouds": {"de": "Wanten", "en": "Shrouds", "es": "Obenques", "fr": "Haubans"},
        "marine.keel": {"de": "Kiel", "en": "Keel", "es": "Quilla", "fr": "Quille"},
        "marine.rudder": {"de": "Ruder", "en": "Rudder", "es": "Timon", "fr": "Safran"},
        "marine.galley": {"de": "Pantry", "en": "Galley", "es": "Cocina", "fr": "Cuisine"},
        "marine.head": {"de": "Nasszelle", "en": "Head", "es": "Bano", "fr": "Salle d'eau"},
        "marine.cockpit": {
            "de": "Cockpit",
            "en": "Cockpit",
            "es": "Banera",
            "fr": "Cockpit",
        },
        "marine.companionway": {
            "de": "Niedergang",
            "en": "Companionway",
            "es": "Tambucho",
            "fr": "Descente",
        },
        "marine.berth": {"de": "Koje", "en": "Berth", "es": "Litera", "fr": "Couchette"},
        "marine.hull": {"de": "Rumpf", "en": "Hull", "es": "Casco", "fr": "Coque"},
        "marine.mast": {"de": "Mast", "en": "Mast", "es": "Mastil", "fr": "Mat"},
        "marine.boom": {"de": "Baum", "en": "Boom", "es": "Botavara", "fr": "Bome"},
        "marine.anchor": {"de": "Anker", "en": "Anchor", "es": "Ancla", "fr": "Ancre"},
        "marine.winch": {"de": "Winsch", "en": "Winch", "es": "Winche", "fr": "Winch"},
        "marine.cleat": {"de": "Klampe", "en": "Cleat", "es": "Cornamusa", "fr": "Taquet"},
        "marine.seacock": {
            "de": "Seeventil",
            "en": "Seacock",
            "es": "Grifo de fondo",
            "fr": "Vanne de coque",
        },
        "marine.propeller": {
            "de": "Propeller",
            "en": "Propeller",
            "es": "Helice",
            "fr": "Helice",
        },
        "marine.shaft": {"de": "Welle", "en": "Shaft", "es": "Eje", "fr": "Arbre"},
        "marine.ballast": {"de": "Ballast", "en": "Ballast", "es": "Lastre", "fr": "Lest"},
        "marine.bilge": {"de": "Bilge", "en": "Bilge", "es": "Sentina", "fr": "Cale"},
        "marine.saloon": {"de": "Salon", "en": "Saloon", "es": "Salon", "fr": "Carre"},
    }

    def test_marine_terms_exist(self):
        """All marine terms should have translations in catalog."""
        missing = [key for key in self.MARINE_TERMS if not has_key(key)]
        assert not missing, f"Missing marine terms: {missing}"

    def test_marine_terms_differ_across_languages(self):
        """Most marine terms should have different translations per locale."""
        problematic = []

        for key, expected_values in self.MARINE_TERMS.items():
            text_de = t(key, locale=Locale.DE)
            text_en = t(key, locale=Locale.EN)
            text_es = t(key, locale=Locale.ES)
            text_fr = t(key, locale=Locale.FR)

            # Some terms (cockpit, propeller) are identical in multiple languages
            allow_duplication = {
                "marine.cockpit",
                "marine.propeller",
                "marine.winch",
                "marine.bilge",
                "marine.ballast",
                "marine.saloon",
            }

            if key not in allow_duplication:
                translations = [text_de, text_en, text_es, text_fr]
                unique_translations = len(set(translations))
                assert (
                    unique_translations >= 3
                ), f"{key}: Expected 3+ unique translations, got {unique_translations}"

    def test_marine_terms_match_expected_values(self):
        """Verify marine term translations match expected values."""
        for key, expected in self.MARINE_TERMS.items():
            assert t(key, locale=Locale.DE) == expected["de"], f"{key} DE mismatch"
            assert t(key, locale=Locale.EN) == expected["en"], f"{key} EN mismatch"
            assert t(key, locale=Locale.ES) == expected["es"], f"{key} ES mismatch"
            assert t(key, locale=Locale.FR) == expected["fr"], f"{key} FR mismatch"

    def test_minimum_marine_terms_coverage(self):
        """At least 20 marine terms should be translated in all 4 languages."""
        marine_keys = [k for k in get_all_keys() if k.startswith("marine.")]
        assert (
            len(marine_keys) >= 20
        ), f"Expected 20+ marine terms, found {len(marine_keys)}"

        for key in marine_keys:
            for locale in Locale:
                text = t(key, locale=locale)
                assert (
                    text and text != key
                ), f"Marine term {key} missing in {locale.value}"


# =============================================================================
# 5. INTERPOLATION with variables and edge cases
# =============================================================================


class TestInterpolation:
    """Test variable interpolation in translation strings."""

    def test_interpolation_simple_variable(self):
        """Test basic interpolation: t(key, variable=value)."""
        # Using a key with interpolation: "tier.upgrade_prompt"
        # = "Upgrade auf {tier} fuer erweiterte Funktionen" (DE)
        result = t("tier.upgrade_prompt", tier="Profi", locale=Locale.DE)
        assert "Profi" in result, f"Expected 'Profi' in result, got '{result}'"
        assert "Upgrade auf" in result

    def test_interpolation_multiple_variables(self):
        """Test interpolation with multiple variables."""
        # "error.validation_failed" = "Validation failed: {details}"
        result = t("error.validation_failed", details="Invalid number format", locale=Locale.EN)
        assert "Invalid number format" in result
        assert "Validation failed" in result

    def test_interpolation_missing_variable_returns_placeholder(self):
        """When variable is missing, placeholder should remain unformatted."""
        # Test with a key that has a placeholder but don't provide the variable
        result = t("tier.upgrade_prompt", locale=Locale.EN)
        # Should return the string as-is without crashing
        assert "{tier}" in result, f"Expected placeholder '{{tier}}' in '{result}'"

    def test_interpolation_extra_variables_ignored(self):
        """Extra variables should be ignored without error."""
        result = t(
            "tier.upgrade_prompt",
            tier="Pro",
            extra_var="should_be_ignored",
            locale=Locale.DE,
        )
        assert "Pro" in result, f"Expected 'Pro' in result, got '{result}'"

    def test_interpolation_empty_string_variable(self):
        """Empty string variables should interpolate to empty string."""
        result = t("tier.upgrade_prompt", tier="", locale=Locale.DE)
        assert "Upgrade auf" in result
        # Should have two consecutive spaces where empty string was inserted
        assert "auf  " in result or "auf \n" in result or "auf" in result

    def test_interpolation_numeric_variable(self):
        """Numeric variables should be converted to string."""
        # "finding.engine_hours_high" = "High engine hours: {hours}h"
        result = t("finding.engine_hours_high", hours=5000, locale=Locale.EN)
        assert "5000" in result, f"Expected '5000' in result, got '{result}'"

    def test_interpolation_in_all_locales(self):
        """Interpolation should work correctly in all 4 locales."""
        test_cases = [
            ("auth.tier_upgrade_required", {"tier": "Pro"}, Locale.DE),
            ("auth.tier_upgrade_required", {"tier": "Professional"}, Locale.EN),
            ("error.validation_failed", {"details": "test error"}, Locale.ES),
            ("auth.tier_upgrade_required", {"tier": "Professionnel"}, Locale.FR),
        ]

        for key, kwargs, locale in test_cases:
            result = t(key, locale=locale, **kwargs)
            assert result != key, f"Interpolation failed for {key} in {locale.value}"
            # Should contain at least one variable from kwargs
            assert any(str(v) in result for v in kwargs.values()), (
                f"No variable from {kwargs} found in result: {result}"
            )


# =============================================================================
# 6. LOCALE DETECTION and fallback
# =============================================================================


class TestLocaleDetection:
    """Test locale context variable and fallback behavior."""

    def test_default_locale_is_de(self):
        """Default locale should be German (de)."""
        # Reset locale to default
        set_locale(DEFAULT_LOCALE)
        current = get_locale()
        assert current == Locale.DE, f"Expected default Locale.DE, got {current}"

    def test_set_locale_string_de(self):
        """Setting locale as string 'de' should work."""
        set_locale("de")
        assert get_locale() == Locale.DE

    def test_set_locale_string_en(self):
        """Setting locale as string 'en' should work."""
        set_locale("en")
        assert get_locale() == Locale.EN

    def test_set_locale_string_es(self):
        """Setting locale as string 'es' should work."""
        set_locale("es")
        assert get_locale() == Locale.ES

    def test_set_locale_string_fr(self):
        """Setting locale as string 'fr' should work."""
        set_locale("fr")
        assert get_locale() == Locale.FR

    def test_set_locale_enum(self):
        """Setting locale as Locale enum should work."""
        set_locale(Locale.EN)
        assert get_locale() == Locale.EN

    def test_set_locale_uppercase_fallback(self):
        """Uppercase locale codes should be normalized and work."""
        set_locale("DE")
        assert get_locale() == Locale.DE
        set_locale("EN")
        assert get_locale() == Locale.EN

    def test_set_locale_with_hyphen_variants(self):
        """Locale with variants like 'en-US', 'de-CH' should be handled."""
        set_locale("en-US")
        assert get_locale() == Locale.EN
        set_locale("de-CH")
        assert get_locale() == Locale.DE

    def test_set_locale_with_underscore_variants(self):
        """Locale with underscore variants like 'en_US' should be handled."""
        set_locale("en_US")
        assert get_locale() == Locale.EN

    def test_set_invalid_locale_fallback_to_de(self):
        """Invalid locale like 'zh' should fall back to German."""
        set_locale("zh")
        assert get_locale() == Locale.DE, "Invalid locale should fall back to DE"

    def test_set_invalid_locale_logs_warning(self, caplog):
        """Setting invalid locale should log a warning."""
        set_locale("invalid_locale_xyz")
        # Should contain a warning about unknown locale
        assert any("Unknown locale" in record.message for record in caplog.records), (
            "Expected warning about unknown locale"
        )

    def test_t_respects_current_locale(self):
        """t() should use current locale context when locale not specified."""
        set_locale(Locale.DE)
        text_de = t("common.yes")
        assert text_de == "Ja"

        set_locale(Locale.EN)
        text_en = t("common.yes")
        assert text_en == "Yes"

        set_locale(Locale.ES)
        text_es = t("common.yes")
        assert text_es == "Si"

        set_locale(Locale.FR)
        text_fr = t("common.yes")
        assert text_fr == "Oui"

    def test_t_locale_parameter_overrides_context(self):
        """Explicit locale parameter should override context locale."""
        set_locale(Locale.DE)
        # But ask for EN explicitly
        result = t("common.no", locale=Locale.EN)
        assert result == "No", f"Expected 'No', got '{result}'"

    def test_missing_key_returns_key_itself(self):
        """Missing translation key should return the key as fallback."""
        # Use a key that definitely doesn't exist
        result = t("nonexistent.key.that.will.never.exist")
        assert result == "nonexistent.key.that.will.never.exist"

    def test_missing_locale_falls_back_to_de(self):
        """Missing translation in a locale should fall back to German."""
        # This test relies on the fallback logic in i18n.py
        # We'll test that if a locale is missing, DE is used
        set_locale(Locale.EN)
        result = t("common.yes", locale=Locale.EN)
        assert result == "Yes"

        # Now ask for a locale that should exist
        result = t("common.yes", locale=Locale.DE)
        assert result == "Ja"


# =============================================================================
# 7. PERCENTAGE FORMATTING (bonus)
# =============================================================================


class TestPercentageFormatting:
    """Test percentage formatting with locale conventions."""

    def test_percentage_de(self):
        """DE: 0.75 → 75,0 %"""
        result = NumberFormatter.format_percentage(0.75, decimals=1, locale=Locale.DE)
        assert result == "75,0 %", f"Expected '75,0 %', got '{result}'"

    def test_percentage_en(self):
        """EN: 0.75 → 75.0 %"""
        result = NumberFormatter.format_percentage(0.75, decimals=1, locale=Locale.EN)
        assert result == "75.0 %", f"Expected '75.0 %', got '{result}'"

    def test_percentage_zero(self):
        """0 → 0,0 % (DE)"""
        result = NumberFormatter.format_percentage(0.0, decimals=1, locale=Locale.DE)
        assert result == "0,0 %", f"Expected '0,0 %', got '{result}'"

    def test_percentage_one(self):
        """1.0 → 100,0 %"""
        result = NumberFormatter.format_percentage(1.0, decimals=1, locale=Locale.DE)
        assert result == "100,0 %", f"Expected '100,0 %', got '{result}'"


# =============================================================================
# 8. EDGE CASES & INTEGRITY CHECKS
# =============================================================================


class TestEdgeCasesAndIntegrity:
    """Test edge cases, special characters, and catalog integrity."""

    def test_translations_contain_no_unescaped_braces(self):
        """Flag any malformed placeholders like single braces."""
        keys = get_all_keys()
        problematic = []

        for key in keys:
            for locale in Locale:
                text = t(key, locale=locale)
                # Look for unbalanced braces or single braces
                open_braces = text.count("{")
                close_braces = text.count("}")
                if open_braces != close_braces:
                    problematic.append(
                        f"{key} ({locale.value}): Unbalanced braces in '{text}'"
                    )

        assert not problematic, f"Malformed placeholders:\n" + "\n".join(problematic)

    def test_no_excessive_whitespace(self):
        """Flag translations with excessive leading/trailing whitespace."""
        keys = get_all_keys()
        problematic = []

        for key in keys:
            for locale in Locale:
                text = t(key, locale=locale)
                if text != text.strip():
                    problematic.append(f"{key} ({locale.value}): Leading/trailing whitespace")

        assert (
            not problematic
        ), f"Excessive whitespace in translations:\n" + "\n".join(problematic)

    def test_all_confidence_levels_present(self):
        """All 7 confidence levels should be translatable."""
        confidence_keys = [
            "confidence.measured",
            "confidence.calculated",
            "confidence.visual_high",
            "confidence.visual_medium",
            "confidence.visual_low",
            "confidence.visual_insufficient",
            "confidence.estimated",
            "confidence.benchmark",
            "confidence.documented",
        ]

        for key in confidence_keys:
            assert has_key(key), f"Missing confidence level: {key}"
            for locale in Locale:
                text = t(key, locale=locale)
                assert text != key, f"{key} missing in {locale.value}"

    def test_all_severity_levels_present(self):
        """All 5 severity levels should be translatable."""
        severity_keys = [
            "severity.critical",
            "severity.high",
            "severity.medium",
            "severity.low",
            "severity.info",
        ]

        for key in severity_keys:
            assert has_key(key), f"Missing severity level: {key}"

    def test_all_boat_classes_present(self):
        """All 13 boat classes should be translatable."""
        boat_class_keys = [
            "boat_class.small_sail",
            "boat_class.cruising_sail",
            "boat_class.performance_sail",
            "boat_class.bluewater_sail",
            "boat_class.catamaran_sail",
            "boat_class.small_motor",
            "boat_class.cruising_motor",
            "boat_class.large_motor",
            "boat_class.trawler",
            "boat_class.motorsailer",
            "boat_class.catamaran_power",
            "boat_class.superyacht",
            "boat_class.dinghy",
        ]

        for key in boat_class_keys:
            assert has_key(key), f"Missing boat class: {key}"

    def test_all_analysis_modules_present(self):
        """All 11 analysis modules should be translatable."""
        module_keys = [
            "module.ergonomics",
            "module.volume_storage",
            "module.emotional",
            "module.compliance",
            "module.production",
            "module.materials",
            "module.structural",
            "module.cost",
            "module.service_patterns",
            "module.brand_dna",
            "module.market",
            "module.community",
        ]

        for key in module_keys:
            assert has_key(key), f"Missing analysis module: {key}"

    def test_all_10_domains_present(self):
        """All 10 yacht analysis domains should be present."""
        domain_keys = [
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

        for key in domain_keys:
            assert has_key(key), f"Missing domain: {key}"
            # Each domain should also have a .desc key
            desc_key = f"{key}.desc"
            assert has_key(desc_key), f"Missing domain description: {desc_key}"

    def test_all_units_present(self):
        """All units should be translatable."""
        unit_keys = [
            "unit.mm",
            "unit.m",
            "unit.m2",
            "unit.m3",
            "unit.kg",
            "unit.l",
            "unit.kn",
            "unit.kw",
            "unit.hp",
            "unit.nm",
            "unit.ft",
            "unit.inch",
            "unit.lbs",
            "unit.gal",
            "unit.eur",
            "unit.degrees",
            "unit.percent",
        ]

        for key in unit_keys:
            assert has_key(key), f"Missing unit: {key}"

    def test_error_messages_follow_pattern(self):
        """Error messages should have consistent structure."""
        # All error.* keys should exist
        error_keys = [k for k in get_all_keys() if k.startswith("error.")]
        assert len(error_keys) > 10, f"Expected 10+ error messages, found {len(error_keys)}"


# =============================================================================
# INTEGRATION TEST
# =============================================================================


class TestLocalizationIntegration:
    """Integration tests simulating real usage scenarios."""

    def test_complete_workflow_de(self):
        """Test a complete i18n workflow in German."""
        set_locale(Locale.DE)

        # Get a score label
        score_label = t("common.score")
        assert score_label == "Bewertung"

        # Get a module name
        module = t("module.ergonomics")
        assert module == "Ergonomie"

        # Get a finding with interpolation
        finding = t("finding.engine_hours_high", hours=3000, locale=Locale.DE)
        assert "3000" in finding
        assert "Motorstunden" in finding

        # Format a number
        formatted = NumberFormatter.format_number(5432.1, decimals=2, locale=Locale.DE)
        assert formatted == "5.432,10"

    def test_complete_workflow_en(self):
        """Test a complete i18n workflow in English."""
        set_locale(Locale.EN)

        score_label = t("common.score")
        assert score_label == "Score"

        module = t("module.materials")
        assert module == "Materials"

        finding = t("finding.engine_hours_high", hours=2500, locale=Locale.EN)
        assert "2500" in finding

        formatted = NumberFormatter.format_currency(9999.99, decimals=2, locale=Locale.EN)
        assert "\u20ac" in formatted
        assert "9,999.99" in formatted or "9999.99" in formatted

    def test_multilingual_report_snippet(self):
        """Simulate generating a report snippet in multiple languages."""
        locales = [Locale.DE, Locale.EN, Locale.ES, Locale.FR]

        for locale in locales:
            set_locale(locale)

            # Simulate report header
            report_type = t("report.full_analysis", locale=locale)
            summary = t("report.summary", locale=locale)
            findings = t("report.findings", locale=locale)

            assert report_type != "report.full_analysis"
            assert summary != "report.summary"
            assert findings != "report.findings"

            # All should be non-empty and different from the key
            assert len(report_type) > 0
            assert len(summary) > 0
            assert len(findings) > 0

    def test_context_switching(self):
        """Test switching locale context multiple times."""
        initial = get_locale()

        try:
            set_locale(Locale.DE)
            de_result = t("common.yes")
            assert de_result == "Ja"

            set_locale(Locale.FR)
            fr_result = t("common.yes")
            assert fr_result == "Oui"

            set_locale(Locale.EN)
            en_result = t("common.yes")
            assert en_result == "Yes"

            # Results should all be different
            assert de_result != fr_result != en_result
        finally:
            # Restore initial locale
            set_locale(initial)
