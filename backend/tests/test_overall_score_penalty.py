"""Ein dokumentierter Schaden darf die Gesamtnote nie anheben.

`service_patterns` bewertet, was dem Boot nachweislich zugestossen ist. Als
gewichtetes Mitglied des Mittelwerts hob es die Gesamtnote, sobald sein Wert
ueber dem bisherigen Mittel lag — gemessen stieg sie durch zwei gemeldete
Schaeden (1x kritisch, 1x hoch) von 63,0 auf 64,0.

Der Ursprung war sichtbar in den Gewichten: OVERALL_WEIGHTS summierte sich in
allen Klassen auf **1.05**, und die ueberzaehligen 0.05 waren exakt das
nachtraeglich angehaengte service_patterns-Gewicht.

Jetzt geht das Modul als ABZUG ein: 100 Punkte (nichts gemeldet) kosten nichts,
jeder Punkt darunter zieht anteilig ab. Damit ist das Vorzeichen garantiert.
Die HOEHE des Abzugs bleibt ueber OVERALL_WEIGHTS steuerbar — sie ist eine
Produktentscheidung, das Vorzeichen war ein Fehler.
"""

import asyncio

import pytest

from app.services.analysis.orchestrator import (
    OVERALL_WEIGHTS,
    PENALTY_MODULES,
    AnalysisContext,
    run_full_analysis,
)
from tests.conftest import make_service_report

ZONES = [
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
PASSAGES = [{"name": "P1", "from_zone": "Salon", "to_zone": "Kabine", "width_mm": 620}]


def _overall(reports: list[dict]) -> float:
    context = AnalysisContext(
        zones=ZONES,
        passages=PASSAGES,
        boat_class="cruising_sail",
        length_m=10.85,
        beam_m=3.50,
        tier="pro",
        service_reports=reports,
    )
    return asyncio.run(run_full_analysis(context))["overall_score"]


def _reports(count: int, severity: str) -> list[dict]:
    return [
        make_service_report(severity=severity, description=f"Schaden {i}")
        for i in range(count)
    ]


class TestGewichte:
    def test_design_weights_sum_to_one_without_penalty_modules(self):
        """Die frueheren 1.05 waren das Symptom des Vorzeichenfehlers."""
        for boat_class, weights in OVERALL_WEIGHTS.items():
            design = sum(w for m, w in weights.items() if m not in PENALTY_MODULES)
            assert abs(design - 1.0) < 1e-9, f"{boat_class}: Entwurfsgewichte summieren auf {design}"

    def test_service_patterns_is_a_penalty_module(self):
        assert "service_patterns" in PENALTY_MODULES

    def test_penalty_modules_have_a_weight(self):
        """Ohne Gewicht waere der Abzug immer null — der Fix waere wirkungslos."""
        for boat_class, weights in OVERALL_WEIGHTS.items():
            for module in PENALTY_MODULES:
                assert weights.get(module, 0.0) > 0, f"{boat_class}: {module} ohne Gewicht"


class TestSchadenSenktNiemalsGegenteilig:
    def test_a_single_critical_report_does_not_raise_the_score(self):
        assert _overall(_reports(1, "critical")) <= _overall([])

    def test_score_falls_monotonically_with_damage(self):
        clean = _overall([])
        low = _overall(_reports(1, "low"))
        critical = _overall(_reports(1, "critical"))
        many = _overall(_reports(3, "critical"))
        assert clean >= low >= critical >= many, (
            f"Nicht monoton: sauber={clean}, 1x low={low}, "
            f"1x critical={critical}, 3x critical={many}"
        )

    @pytest.mark.parametrize("severity", ["low", "medium", "high", "critical"])
    def test_more_reports_never_improve_the_score(self, severity):
        scores = [_overall(_reports(n, severity)) for n in (0, 1, 5, 20)]
        for previous, current in zip(scores, scores[1:]):
            assert current <= previous + 1e-9, f"{severity}: {scores}"

    def test_severity_is_reflected_in_the_overall_score(self):
        assert _overall(_reports(3, "critical")) < _overall(_reports(3, "low"))


class TestAbzugBleibtBegrenzt:
    def test_score_stays_on_scale(self):
        for count in (0, 1, 50):
            score = _overall(_reports(count, "critical"))
            assert 0.0 <= score <= 100.0

    def test_clean_history_costs_nothing(self):
        """Eine dokumentierte, unauffaellige Inspektion ist kein Mangel."""
        clean_inspection = [
            {
                "report_type": "inspection",
                "category": "interior",
                "zone_type": "cabin",
                "severity": "low",
                "description": "Routinepruefung ohne Befund",
                "boat_age_months": 24,
            }
        ]
        # Darf hoechstens minimal unter dem Wert ohne Berichte liegen, nie darueber.
        assert _overall(clean_inspection) <= _overall([]) + 1e-9
