"""Analysewarnungen erreichen den Nutzer in seiner Sprache.

Der i18n-Katalog war vollstaendig (232 Schluessel, 0 Luecken in EN/ES/FR), aber
``t()`` wurde in **keinem** der zwoelf Analysemodule aufgerufen: Ein
Vollanalyse-Lauf mit ``set_locale("en")`` lieferte 237 deutsche Strings. Das
Problem war die Reichweite, nicht der Katalog.

Geloest an der Praesentationsgrenze: Die Module bleiben reine Funktionen und
liefern ``code`` + ``params`` + deutschen Text; ``warning_i18n`` setzt daraus die
Meldung in der aktiven Sprache zusammen. Fehlt eine Uebersetzung, gewinnt der
deutsche Originaltext — lieber korrekt deutsch als luecken haft englisch.
"""

import asyncio

import pytest

from app.core.i18n import Locale, set_locale
from app.services.analysis.orchestrator import AnalysisContext, run_full_analysis
from app.services.analysis.warning_i18n import (
    WARNING_TRANSLATIONS,
    ZONE_TYPE_LABELS,
    localize_analysis,
    localize_warning,
    zone_label,
)

LOCALES = ["de", "en", "es", "fr"]


@pytest.fixture(autouse=True)
def _reset_locale():
    yield
    set_locale(Locale.DE)


@pytest.fixture(scope="module")
def analysis() -> dict:
    zones = [
        {
            "name": name,
            "zone_type": zone_type,
            "polygon": [[0, i * 1500], [3200, i * 1500], [3200, (i + 1) * 1500], [0, (i + 1) * 1500]],
            "height_mm": 1900,
        }
        for i, (name, zone_type) in enumerate(
            [("Salon", "saloon"), ("Kabine", "cabin"), ("Nasszelle", "head"), ("Cockpit", "cockpit")]
        )
    ]
    return asyncio.run(
        run_full_analysis(
            AnalysisContext(
                zones=zones,
                passages=[{"name": "P1", "from_zone": "Salon", "to_zone": "Kabine", "width_mm": 620}],
                boat_class="cruising_sail",
                length_m=10.85,
                beam_m=3.50,
                tier="pro",
            )
        )
    )


class TestKatalog:
    def test_every_entry_has_all_four_locales(self):
        incomplete = {
            code: sorted(set(LOCALES) - set(entry))
            for code, entry in WARNING_TRANSLATIONS.items()
            if set(LOCALES) - set(entry)
        }
        assert not incomplete, f"Unvollstaendige Uebersetzungen: {incomplete}"

    def test_no_translation_is_empty(self):
        empty = [
            f"{code}/{lang}"
            for code, entry in WARNING_TRANSLATIONS.items()
            for lang, text in entry.items()
            if not text.strip()
        ]
        assert not empty, f"Leere Uebersetzungen: {empty}"

    def test_placeholders_match_across_locales(self):
        """Ein Platzhalter, den nur eine Sprache kennt, wirft zur Laufzeit."""
        import re

        pattern = re.compile(r"\{(\w+)")
        mismatched = {}
        for code, entry in WARNING_TRANSLATIONS.items():
            sets = {lang: set(pattern.findall(text)) for lang, text in entry.items()}
            if len(set(map(frozenset, sets.values()))) > 1:
                mismatched[code] = sets
        assert not mismatched, f"Platzhalter weichen ab: {mismatched}"

    def test_zone_labels_cover_all_four_locales(self):
        incomplete = {
            zt: sorted(set(LOCALES) - set(entry))
            for zt, entry in ZONE_TYPE_LABELS.items()
            if set(LOCALES) - set(entry)
        }
        assert not incomplete, f"Unvollstaendige Zonenbezeichnungen: {incomplete}"


class TestUebersetzung:
    def test_translates_with_measured_values(self):
        warning = {
            "code": "ERGO_PASSAGE_NARROW",
            "severity": "warning",
            "params": {"from_zone": "Salon", "to_zone": "Kabine", "width": 620.0, "recommended": 650.0},
            "message": "Durchgang Salon→Kabine ist zu schmal (620mm, empfohlen: 650mm)",
        }
        set_locale("en")
        result = localize_warning(warning)
        assert "too narrow" in result["message"]
        assert "620mm" in result["message"] and "650mm" in result["message"]

    def test_german_original_is_preserved(self):
        warning = {
            "code": "ERGO_NO_HELM",
            "severity": "warning",
            "message": "Kein Steuerstand im Layout definiert",
        }
        set_locale("fr")
        result = localize_warning(warning)
        assert result["message_de"] == "Kein Steuerstand im Layout definiert"

    def test_german_locale_returns_the_original(self):
        warning = {"code": "ERGO_NO_HELM", "message": "Kein Steuerstand im Layout definiert"}
        set_locale("de")
        assert localize_warning(warning)["message"] == warning["message"]

    def test_unknown_code_falls_back_to_german(self):
        warning = {"code": "GIBT_ES_NICHT", "message": "Deutscher Text"}
        set_locale("en")
        assert localize_warning(warning)["message"] == "Deutscher Text"

    def test_missing_param_falls_back_instead_of_breaking(self):
        """Lieber korrekt deutsch als halb gefuellt englisch."""
        warning = {
            "code": "ERGO_PASSAGE_NARROW",
            "params": {"from_zone": "Salon"},  # to_zone/width/recommended fehlen
            "message": "Durchgang Salon→Kabine ist zu schmal",
        }
        set_locale("en")
        assert localize_warning(warning)["message"] == warning["message"]

    def test_original_warning_is_not_mutated(self):
        """Gespeichert wird sprachneutral — dieselbe Analyse muss spaeter in einer
        anderen Sprache darstellbar bleiben."""
        warning = {"code": "ERGO_NO_HELM", "message": "Kein Steuerstand im Layout definiert"}
        set_locale("en")
        localize_warning(warning)
        assert warning["message"] == "Kein Steuerstand im Layout definiert"
        assert "message_de" not in warning


class TestZonenbezeichnungen:
    @pytest.mark.parametrize("lang,expected", [("en", "engine room"), ("fr", "compartiment moteur")])
    def test_zone_type_is_translated_too(self, lang, expected):
        """"Critical zone missing: Maschinenraum" waere halb uebersetzt gewesen."""
        warning = {
            "code": "ERGO_ZONE_MISSING",
            "params": {"zone_label": "Maschinenraum", "zone_type": "engine"},
            "message": "Kritische Zone fehlt: Maschinenraum",
        }
        set_locale(lang)
        assert expected in localize_warning(warning)["message"]

    def test_user_zone_name_is_left_alone(self):
        """Ein NUTZERdefinierter Name darf nicht 'uebersetzt' werden."""
        warning = {
            "code": "ERGO_ZONE_MISSING",
            "params": {"zone_label": "Achterkajüte Steuerbord", "zone_type": "gibt_es_nicht"},
            "message": "Kritische Zone fehlt: Achterkajüte Steuerbord",
        }
        set_locale("en")
        assert "Achterkajüte Steuerbord" in localize_warning(warning)["message"]

    def test_zone_label_returns_none_for_unknown_type(self):
        assert zone_label("voellig_unbekannt", "en") is None


class TestVollanalyse:
    def test_warnings_are_translated_in_a_real_run(self, analysis):
        set_locale("en")
        localized = analysis_warnings(localize_analysis(analysis))
        translated = [w for w in localized if w.get("message_de")]
        assert translated, "Kein einziger Befund wurde uebersetzt"

    def test_untranslated_warnings_keep_their_german_text(self, analysis):
        set_locale("en")
        for warning in analysis_warnings(localize_analysis(analysis)):
            assert warning.get("message"), "Warnung ohne Text"

    def test_scores_are_untouched_by_localisation(self, analysis):
        set_locale("fr")
        localized = localize_analysis(analysis)
        assert localized["overall_score"] == analysis["overall_score"]
        for name, module in analysis["modules"].items():
            assert localized["modules"][name].get("overall_score") == module.get("overall_score")

    def test_localisation_is_idempotent_per_locale(self, analysis):
        set_locale("es")
        once = analysis_warnings(localize_analysis(analysis))
        twice = analysis_warnings(localize_analysis(localize_analysis(analysis)))
        assert [w["message"] for w in once] == [w["message"] for w in twice]


def analysis_warnings(result: dict) -> list[dict]:
    return [w for m in result["modules"].values() for w in (m.get("warnings") or [])]
