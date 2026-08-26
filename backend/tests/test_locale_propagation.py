"""Sprache und Accept-Language-Auswertung.

Zwei Befunde:

* **Locale ging im Executor verloren.** Der Orchestrator schickt jedes
  Analysemodul mit ``run_in_executor`` in einen Worker-Thread. Der startet mit
  LEEREN ``contextvars`` — die anfragebezogene Sprache (in der Middleware per
  contextvar gesetzt) fiel im Modul stumm auf Deutsch zurueck. Heute faellt das
  nicht auf, weil noch kein Analysemodul ``t()`` benutzt; genau deshalb waere es
  eine Falle fuer den ersten, der es tut.
* **Accept-Language ignorierte die Qualitaetswerte.** Es gewann der erste
  unterstuetzte Eintrag statt des am hoechsten gewichteten: Bei
  ``de;q=0.2, en;q=0.9`` kam Deutsch heraus, obwohl der Browser ausdruecklich
  Englisch bevorzugt.
"""

import asyncio

import pytest

from app.core.i18n import Locale, get_locale, set_locale
from app.core.middleware import LocaleMiddleware
from app.services.analysis.orchestrator import AnalysisContext, _run_single_module


class _FakeRequest:
    def __init__(self, accept_language: str = "", lang: str | None = None):
        self.query_params = {"lang": lang} if lang else {}
        self.headers = {"accept-language": accept_language}


@pytest.fixture
def detector() -> LocaleMiddleware:
    return LocaleMiddleware.__new__(LocaleMiddleware)


class TestAcceptLanguageQualitaetswerte:
    @pytest.mark.parametrize(
        "header,expected",
        [
            ("de;q=0.2, en;q=0.9", "en"),      # hoeheres q gewinnt
            ("en-GB;q=0.3, fr;q=0.8", "fr"),   # Regionalcode wird auf die Sprache reduziert
            ("es, de;q=0.1", "es"),            # ohne q gilt q=1.0
            ("de, en", "de"),                  # bei Gleichstand die Reihenfolge
            ("fr", "fr"),
        ],
    )
    def test_highest_quality_wins(self, detector, header, expected):
        assert detector._detect_locale(_FakeRequest(header)) == expected

    def test_q_zero_means_not_acceptable(self, detector):
        assert detector._detect_locale(_FakeRequest("de;q=0, en")) == "en"

    def test_unsupported_languages_are_skipped(self, detector):
        assert detector._detect_locale(_FakeRequest("zz;q=0.9, de;q=0.1")) == "de"

    def test_malformed_q_does_not_crash(self, detector):
        assert detector._detect_locale(_FakeRequest("en;q=kaputt, fr;q=0.5")) == "fr"

    @pytest.mark.parametrize("header", ["", "   ", ",,,", "zz, yy"])
    def test_falls_back_to_german(self, detector, header):
        assert detector._detect_locale(_FakeRequest(header)) == "de"

    def test_explicit_lang_parameter_wins(self, detector):
        assert detector._detect_locale(_FakeRequest("de;q=0.9", lang="fr")) == "fr"

    def test_unsupported_lang_parameter_is_ignored(self, detector):
        assert detector._detect_locale(_FakeRequest("fr", lang="zz")) == "fr"


class TestLocaleErreichtDasModul:
    def test_locale_survives_the_executor_dispatch(self):
        seen: dict[str, object] = {}

        def runner(zones, passages, boat_class, config_overrides, **kwargs):
            seen["locale"] = get_locale()
            return {"module": "fake", "overall_score": 50.0}

        async def scenario():
            set_locale(Locale.EN)
            context = AnalysisContext(zones=[], passages=[], boat_class="cruising_sail")
            await _run_single_module("fake", runner, context)

        asyncio.run(scenario())
        assert seen["locale"] == Locale.EN, (
            "Das Analysemodul lief mit einem leeren Kontext und fiel auf die "
            "Standardsprache zurueck."
        )

    def test_each_module_sees_the_same_locale(self):
        """Auch bei parallel laufenden Modulen darf keiner die Sprache verlieren."""
        seen: list[object] = []

        def runner(zones, passages, boat_class, config_overrides, **kwargs):
            seen.append(get_locale())
            return {"module": "fake", "overall_score": 50.0}

        async def scenario():
            set_locale(Locale.FR)
            context = AnalysisContext(zones=[], passages=[], boat_class="cruising_sail")
            await asyncio.gather(
                *(_run_single_module(f"fake{i}", runner, context) for i in range(5))
            )

        asyncio.run(scenario())
        assert seen == [Locale.FR] * 5
