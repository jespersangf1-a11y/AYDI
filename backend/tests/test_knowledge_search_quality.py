"""Die Lexikon-Suche ist die Kernbedienung von Produktsaeule 1.

Zwei gemessene Defekte, die diese Tests festhalten:

1. **Das Dokument selbst war nie ein Treffer.** Gesucht wurde nur in FAQ, Glossar,
   Fehlerbildern und Erfahrungsberichten — nie im Dokumenttitel. Wer
   "Fenster-Dichtungen" eingab, bekam zwei zufaellige Beifang-Treffer, aber nicht
   den gleichnamigen Artikel.
2. **Keine Sortierung.** Treffer kamen in Korpus-Iterationsreihenfolge und wurden
   bei ``max_results`` willkuerlich abgeschnitten. Eine Suche nach "Osmose" zeigte
   auf den ersten Plaetzen FAQ-Eintraege aus Dichtstoff-Dokumenten; das
   Osmoseschutz-Dokument war nicht unter den ersten fuenf.

Ausserdem werden jetzt Tabellen durchsucht — dort stehen im Korpus die harten
Daten (Teilenummern, Masse, Preise).
"""

import time

import pytest

from app.services.knowledge.markdown_knowledge_loader import (
    get_markdown_knowledge,
    search_markdown_knowledge,
)


@pytest.fixture(scope="module", autouse=True)
def warm_corpus():
    """Korpus und Suchindex einmal aufbauen, damit Zeitmessungen aussagekraeftig sind."""
    get_markdown_knowledge()
    search_markdown_knowledge("aufwaermen")


class TestDokumentTreffer:
    def test_document_is_found_by_its_own_title(self):
        results = search_markdown_knowledge("Fenster-Dichtungen", max_results=5)
        assert results, "Keine Treffer fuer einen echten Dokumenttitel"
        assert results[0]["type"] == "dokument", (
            f"Oberster Treffer sollte der Artikel selbst sein, ist aber "
            f"{results[0]['type']} aus {results[0]['source']}"
        )
        assert results[0]["source"] == "fenster_dichtungen"

    def test_document_hit_carries_navigable_metadata(self):
        """Ohne Kategorie/Slug kann die Oberflaeche den Treffer nicht verlinken."""
        results = search_markdown_knowledge("Fenster-Dichtungen", max_results=5)
        doc = next(r for r in results if r["type"] == "dokument")
        assert doc["source"]
        assert doc["title"]
        assert doc["category"]

    def test_search_by_slug_words_also_finds_the_document(self):
        results = search_markdown_knowledge("antifouling selbstpolierend", max_results=5)
        assert any(
            r["type"] == "dokument" and "antifouling" in r["source"] for r in results
        )


class TestRelevanzSortierung:
    def test_whole_word_match_outranks_substring(self):
        """"Ankerkette" darf nicht hinter Komposita landen."""
        results = search_markdown_knowledge("Ankerkette", max_results=10)
        assert results
        assert any("anker" in r["source"] for r in results[:5])

    def test_results_are_capped_at_max_results(self):
        assert len(search_markdown_knowledge("Osmose", max_results=3)) <= 3
        assert len(search_markdown_knowledge("Osmose", max_results=50)) <= 50

    def test_more_results_is_a_superset_of_fewer(self):
        """Stabile Sortierung: Die Top-3 muessen in den Top-20 an gleicher Stelle stehen."""
        few = search_markdown_knowledge("Osmose", max_results=3)
        many = search_markdown_knowledge("Osmose", max_results=20)
        assert [(r["type"], r["source"]) for r in few] == [
            (r["type"], r["source"]) for r in many[:3]
        ]

    def test_relevant_document_reaches_the_top_ten(self):
        results = search_markdown_knowledge("Osmose", max_results=10)
        assert any("osmose" in r["source"] for r in results), (
            "Das Osmose-Dokument taucht nicht unter den ersten zehn Treffern auf"
        )


class TestTabellenUndFeldabdeckung:
    def test_table_content_is_searchable(self):
        """Teilenummern, Masse und Preise stehen im Korpus in Tabellen."""
        results = search_markdown_knowledge("Kathodenschutz", max_results=10)
        assert results, "Begriff aus einer Tabelle wurde nicht gefunden"

    def test_result_types_are_known(self):
        allowed = {"dokument", "faq", "glossary", "fehlerbild", "erfahrungsbericht", "tabelle"}
        for query in ("Osmose", "EPDM", "Sikaflex"):
            for result in search_markdown_knowledge(query, max_results=20):
                assert result["type"] in allowed, f"Unbekannter Treffertyp: {result['type']}"

    def test_every_result_names_its_source(self):
        for result in search_markdown_knowledge("EPDM", max_results=20):
            assert result.get("source"), f"Treffer ohne Quellenangabe: {result}"


class TestRandfaelle:
    @pytest.mark.parametrize("query", ["", "   ", "\n"])
    def test_empty_query_returns_nothing(self, query):
        assert search_markdown_knowledge(query) == []

    def test_unknown_term_returns_nothing(self):
        assert search_markdown_knowledge("zzz_gibt_es_nicht_zzz") == []

    def test_search_is_case_insensitive(self):
        lower = search_markdown_knowledge("epdm", max_results=5)
        upper = search_markdown_knowledge("EPDM", max_results=5)
        assert [(r["type"], r["source"]) for r in lower] == [
            (r["type"], r["source"]) for r in upper
        ]

    def test_regex_metacharacters_do_not_crash(self):
        """Der Begriff geht in ein Wortgrenzen-Muster ein — er muss escaped werden."""
        for query in ["C++", "3M 5200 (schwarz)", "a|b", "[test]", "1.5mm"]:
            search_markdown_knowledge(query, max_results=5)  # darf nicht werfen


class TestSuchgeschwindigkeit:
    """Vorher rund 400 ms je Abfrage — fuer eine Lexikon-Suche unbrauchbar."""

    def test_miss_is_fast(self):
        start = time.perf_counter()
        search_markdown_knowledge("zzz_gibt_es_nicht_zzz", max_results=20)
        elapsed = time.perf_counter() - start
        assert elapsed < 0.2, f"Fehltreffer-Suche dauerte {elapsed*1000:.0f} ms"

    def test_common_term_stays_responsive(self):
        start = time.perf_counter()
        search_markdown_knowledge("Osmose", max_results=20)
        elapsed = time.perf_counter() - start
        assert elapsed < 1.0, f"Suche nach einem haeufigen Begriff dauerte {elapsed*1000:.0f} ms"
