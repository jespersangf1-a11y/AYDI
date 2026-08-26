"""CLAUDE.md-Konvention: "Every warning has a suggestion."

Gemessen war das nicht erfuellt: In einem vollstaendigen Analyselauf trugen 17 von
90 Warnungen keinen Handlungsvorschlag. Betroffen waren ausgerechnet die aus dem
Wissenskorpus angereicherten Befunde — der Nutzer erfuhr also von einem
Fehlerbild, aber nicht, was er dagegen tun kann.

Ursache war zweistufig:
1. Der Fehlerbild-Extraktor kannte nur einen Teil der Beschriftungen, unter denen
   der Korpus die Massnahme fuehrt ("Loesung", "Behebung", "Massnahme" ohne
   Eszett) und las Katalog-Tabellen gar nicht aus. Dadurch hatten 663 von 985
   Fehlerbildern keine Massnahme.
2. Wo der Korpus wirklich keine Massnahme hinterlegt, lieferte der Code
   ``suggestion: None`` statt eines Verweises.

Dieser Test haelt beide Korrekturen fest.
"""

import asyncio

import pytest

from app.services.analysis.orchestrator import AnalysisContext, run_full_analysis
from app.services.knowledge.markdown_knowledge_loader import get_all_fehlerbilder
from tests.conftest import (
    make_competitor,
    make_cost_item,
    make_service_report,
    make_zone_material,
)


def _context() -> AnalysisContext:
    """Ein Projekt, in dem moeglichst viele Module tatsaechlich Warnungen erzeugen."""
    layout = [
        ("Vorschiff", "forepeak"),
        ("Kabine", "cabin"),
        ("Nasszelle", "head"),
        ("Salon", "saloon"),
        ("Pantry", "pantry"),
        ("Maschine", "engine_room"),
        ("Cockpit", "cockpit"),
    ]
    zones = [
        {
            "name": name,
            "zone_type": zone_type,
            "polygon": [
                [0, i * 1500],
                [3200, i * 1500],
                [3200, (i + 1) * 1500],
                [0, (i + 1) * 1500],
            ],
            "height_mm": 1900,
        }
        for i, (name, zone_type) in enumerate(layout)
    ]
    passages = [
        {"name": f"P{i}", "from_zone": a, "to_zone": b, "width_mm": w}
        for i, (a, b, w) in enumerate(
            [
                ("Vorschiff", "Kabine", 600),
                ("Kabine", "Salon", 620),
                ("Salon", "Nasszelle", 580),
                ("Salon", "Pantry", 700),
            ]
        )
    ]
    return AnalysisContext(
        zones=zones,
        passages=passages,
        boat_class="cruising_sail",
        length_m=10.85,
        beam_m=3.50,
        tier="pro",
        zone_materials=[make_zone_material(zone_name="Salon")],
        structural_items=[
            {
                "name": "Rumpf",
                "item_type": "hull_laminate",
                "thickness_mm": 12.0,
                "material": "GFK",
                "mass_kg": 1800.0,
            }
        ],
        cost_items=[make_cost_item()],
        service_reports=[make_service_report(severity="critical")],
        brand_references=[
            {"model_name": f"HR {n}", "boat_class": "cruising_sail", "model_year": 2015}
            for n in (31, 34, 36)
        ],
        competitors=[make_competitor(length_m=10.3 + i * 0.3) for i in range(6)],
        community_patterns=[
            {"pattern": "Osmose", "count": 9, "boat_class": "cruising_sail"}
        ],
    )


@pytest.fixture(scope="module")
def analysis() -> dict:
    return asyncio.run(run_full_analysis(_context()))


def _all_warnings(analysis: dict) -> list[tuple[str, dict]]:
    return [
        (module, warning)
        for module, result in analysis["modules"].items()
        for warning in (result.get("warnings") or [])
    ]


class TestJedeWarnungHatEinenVorschlag:
    def test_the_run_actually_produces_warnings(self, analysis):
        """Schutz gegen einen leeren Testlauf, der alles gruen faerbt."""
        assert len(_all_warnings(analysis)) >= 40

    def test_every_warning_has_a_suggestion(self, analysis):
        missing = [
            f"{module}: {warning.get('code') or warning.get('message', '')[:60]}"
            for module, warning in _all_warnings(analysis)
            if not (warning.get("suggestion") or "").strip()
        ]
        assert not missing, (
            f"{len(missing)} Warnungen ohne Handlungsvorschlag "
            f"(CLAUDE.md: 'Every warning has a suggestion'): {missing[:10]}"
        )

    def test_every_warning_has_a_severity(self, analysis):
        allowed = {"critical", "warning", "info"}
        wrong = [
            (module, warning.get("severity"))
            for module, warning in _all_warnings(analysis)
            if warning.get("severity") not in allowed
        ]
        assert not wrong, f"Unbekannte Schweregrade: {wrong[:10]}"

    def test_suggestions_are_not_placeholders(self, analysis):
        """Ein Vorschlag muss etwas aussagen, nicht nur das Feld fuellen."""
        too_short = [
            (module, warning.get("suggestion"))
            for module, warning in _all_warnings(analysis)
            if 0 < len((warning.get("suggestion") or "").strip()) < 15
        ]
        assert not too_short, f"Inhaltsleere Vorschläge: {too_short[:10]}"


class TestFehlerbildExtraktion:
    """Der Korpus fuehrt dieselben Felder unter verschiedenen Beschriftungen.

    Vor der Vereinheitlichung: 985 Fehlerbilder, davon nur 322 mit Massnahme und
    428 ohne jedes Feld ausser dem Titel.
    """

    @pytest.fixture(scope="class")
    def fehlerbilder(self) -> list[dict]:
        return get_all_fehlerbilder()

    def test_corpus_yields_failure_patterns(self, fehlerbilder):
        assert len(fehlerbilder) >= 900

    def test_remedy_is_extracted_for_a_large_share(self, fehlerbilder):
        with_remedy = [f for f in fehlerbilder if (f.get("massnahme_de") or "").strip()]
        assert len(with_remedy) >= 480, (
            f"Nur {len(with_remedy)} von {len(fehlerbilder)} Fehlerbildern haben eine "
            f"Maßnahme (erwartet >= 480). Vermutlich kennt der Extraktor eine "
            f"Beschriftung oder Tabellenform nicht mehr."
        )

    def test_symptom_is_extracted_for_a_large_share(self, fehlerbilder):
        with_symptom = [f for f in fehlerbilder if (f.get("symptom_de") or "").strip()]
        assert len(with_symptom) >= 600

    def test_most_entries_carry_more_than_a_title(self, fehlerbilder):
        fields = ("symptom_de", "ursache_de", "massnahme_de", "haeufigkeit_de")
        title_only = [
            f for f in fehlerbilder if not any((f.get(x) or "").strip() for x in fields)
        ]
        assert len(title_only) <= 260, (
            f"{len(title_only)} Fehlerbilder bestehen nur aus einem Titel "
            f"(erwartet <= 260)."
        )

    def test_every_entry_has_a_title(self, fehlerbilder):
        assert all((f.get("title_de") or "").strip() for f in fehlerbilder)
