"""End-to-End-Nachweis: Vollanalyse eines vollstaendig gefuellten Projekts.

Warum dieser Test existiert: Die Testsuite pruefte die Analysemodule einzeln,
aber nie den Fall, den das Produkt eigentlich verkauft — ein Profi-Projekt mit
Materialien, Kosten, Serviceberichten, Wettbewerbern und Marken-Referenzen, das
durch ALLE Module laeuft. Der Praxistest behauptete diesen Fall zu pruefen,
erwartete dabei aber >= 10 Module fuer einen FREE-Nutzer, der per Tarif nur vier
bekommt. Der Flaggschiff-Pfad war damit faktisch ungetestet.

Geprueft wird:
* Mit vollstaendigen Daten laufen alle 12 Module durch — nichts wird uebersprungen.
* Mit leeren Daten wird ehrlich uebersprungen (Grund im Klartext), statt zu raten.
* Tarif-Gating greift serverseitig und meldet die gesperrten Module getrennt.
* Zonentyp-Synonyme ("galley") verlieren ihre Domaenenzuordnung nicht.
"""

import asyncio

import pytest

from app.services.analysis.orchestrator import (
    ALL_MODULE_NAMES,
    AnalysisContext,
    run_full_analysis,
)
from tests.conftest import (
    make_competitor,
    make_cost_item,
    make_service_report,
    make_zone_material,
)


def _zones() -> list[dict]:
    layout = [
        ("Vorschiff", "forepeak", 1850),
        ("Bugkabine", "cabin", 1900),
        ("Nasszelle", "head", 1950),
        ("Salon", "saloon", 1980),
        ("Kombuese", "galley", 1950),      # Synonym — muss auf "pantry" ziehen
        ("Achterkabine", "aft_cabin", 1880),
        ("Maschinenraum", "engine_room", 1400),
        ("Cockpit", "cockpit", 2000),
    ]
    return [
        {
            "name": name,
            "zone_type": zone_type,
            "polygon": [
                [0, i * 1500],
                [3200, i * 1500],
                [3200, (i + 1) * 1500],
                [0, (i + 1) * 1500],
            ],
            "height_mm": height,
        }
        for i, (name, zone_type, height) in enumerate(layout)
    ]


def _passages() -> list[dict]:
    pairs = [
        ("Vorschiff", "Bugkabine", 600),
        ("Bugkabine", "Salon", 620),
        ("Salon", "Nasszelle", 580),
        ("Salon", "Kombuese", 700),
        ("Salon", "Achterkabine", 610),
        ("Achterkabine", "Cockpit", 650),
    ]
    return [
        {"name": f"P{i}", "from_zone": a, "to_zone": b, "width_mm": w}
        for i, (a, b, w) in enumerate(pairs)
    ]


def _full_context(tier: str = "pro") -> AnalysisContext:
    """Ein Projekt, in dem jedes Modul die Daten findet, die es braucht."""
    return AnalysisContext(
        zones=_zones(),
        passages=_passages(),
        boat_class="cruising_sail",
        length_m=10.85,
        beam_m=3.50,
        tier=tier,
        zone_materials=[
            make_zone_material(zone_name="Salon", surface_type="floor", area_sqm=8.0),
            make_zone_material(zone_name="Nasszelle", surface_type="wall", area_sqm=4.0),
            make_zone_material(zone_name="Bugkabine", surface_type="ceiling", area_sqm=6.0),
        ],
        structural_items=[
            {
                "name": "Rumpflaminat",
                "item_type": "hull_laminate",
                "thickness_mm": 12.0,
                "material": "GFK",
                "mass_kg": 1800.0,
            },
            {
                "name": "Kielbolzen",
                "item_type": "keel_bolt",
                "material": "316L",
                "mass_kg": 2400.0,
            },
        ],
        cost_items=[
            make_cost_item(category="material", unit_cost_eur=38_000.0, quantity=1.0),
            make_cost_item(category="labor", unit_cost_eur=65.0, quantity=180.0, unit="hour"),
        ],
        service_reports=[
            make_service_report(
                report_type="repair",
                category="sanitary_water",
                zone_type="head",
                severity="high",
                description="Seeventil undicht",
                boat_age_months=96,
                cost_eur=450.0,
            ),
            make_service_report(
                report_type="maintenance",
                category="propulsion_engine",
                zone_type="engine_room",
                severity="low",
                description="Impeller gewechselt",
                boat_age_months=84,
                cost_eur=120.0,
            ),
        ],
        brand_references=[
            {"model_name": f"HR {n}", "boat_class": "cruising_sail", "model_year": 2014 + i}
            for i, n in enumerate([31, 34, 36, 40])
        ],
        competitors=[make_competitor(length_m=10.3 + i * 0.3) for i in range(6)],
        community_patterns=[
            {"pattern": "Osmose an Rumpfunterseite", "count": 12, "boat_class": "cruising_sail"},
            {"pattern": "Ruderlager-Spiel", "count": 7, "boat_class": "cruising_sail"},
        ],
    )


@pytest.fixture(scope="module")
def full_result() -> dict:
    return asyncio.run(run_full_analysis(_full_context()))


class TestVollanalyseMitVollstaendigenDaten:
    def test_every_module_runs(self, full_result):
        missing = sorted(ALL_MODULE_NAMES - set(full_result["modules"]))
        assert not missing, (
            f"Module ohne Ergebnis: {missing}. "
            f"Uebersprungen: {full_result['skipped']} | Fehler: {full_result['errors']}"
        )

    def test_nothing_is_skipped_or_errored(self, full_result):
        assert full_result["skipped"] == {}
        assert full_result["errors"] == {}
        assert full_result["tier_gated"] == {}

    def test_no_module_ran_degraded(self, full_result):
        degraded = {
            name: result["degraded_subanalyses"]
            for name, result in full_result["modules"].items()
            if result.get("degraded_subanalyses")
        }
        assert not degraded, f"Teilanalysen abgestuerzt: {degraded}"

    def test_overall_score_is_on_scale(self, full_result):
        assert 0.0 <= full_result["overall_score"] <= 100.0
        assert full_result["overall_confidence"]

    def test_every_module_carries_a_score(self, full_result):
        without = [
            name
            for name, result in full_result["modules"].items()
            if result.get("overall_score") is None
        ]
        assert not without, f"Module ohne Note: {without}"

    def test_zone_synonym_keeps_its_domain(self, full_result):
        """'galley' muss als 'pantry' in der Interieur-Domaene ankommen."""
        coverage = full_result["domain_coverage"]
        assert coverage["interior"]["has_zone_data"] is True


class TestEhrlicheLuecken:
    """Ohne Daten wird uebersprungen — nicht geraten."""

    @pytest.fixture(scope="class")
    def bare_result(self) -> dict:
        context = AnalysisContext(
            zones=_zones(),
            passages=_passages(),
            boat_class="cruising_sail",
            length_m=10.85,
            beam_m=3.50,
            tier="pro",
        )
        return asyncio.run(run_full_analysis(context))

    def test_data_hungry_modules_are_skipped(self, bare_result):
        for module in ("materials", "cost", "service_patterns", "brand_dna", "market"):
            assert module in bare_result["skipped"], (
                f"{module} lieferte ohne Daten ein Ergebnis statt sich zu enthalten: "
                f"{bare_result['modules'].get(module)}"
            )

    def test_skip_reasons_are_human_readable(self, bare_result):
        for module, reason in bare_result["skipped"].items():
            assert isinstance(reason, str) and len(reason) > 15, (
                f"{module} nennt keinen brauchbaren Grund: {reason!r}"
            )

    def test_layout_only_modules_still_work(self, bare_result):
        for module in ("ergonomics", "volume_storage", "emotional", "compliance"):
            assert module in bare_result["modules"]


class TestTarifGating:
    @pytest.fixture(scope="class")
    def free_result(self) -> dict:
        return asyncio.run(run_full_analysis(_full_context(tier="free")))

    def test_pro_modules_are_gated_not_executed(self, free_result):
        for module in ("structural", "cost", "materials", "compliance"):
            assert module in free_result["tier_gated"]
            assert module not in free_result["modules"]

    def test_free_modules_still_run(self, free_result):
        for module in ("ergonomics", "volume_storage", "emotional"):
            assert module in free_result["modules"]

    def test_gating_is_reported_separately_from_skipping(self, free_result):
        overlap = set(free_result["tier_gated"]) & set(free_result["skipped"])
        assert not overlap, f"Modul doppelt gemeldet: {overlap}"
