"""Serviceberichte muessen die Note senken — und zwar nach Schwere.

Zwei zusammenhaengende Defekte, beide reproduziert:

* **Schwere ohne Wirkung.** Die vier urspruenglichen Teilanalysen sind reine
  MUSTER-Detektoren ("haeuft sich etwas an einer Stelle?"). Keine bewertete, wie
  schlimm das Gemeldete ist. Gemessen: zehn kosmetische ``low``-Berichte und zehn
  ``critical``-Totalschaeden ergaben identisch 90,0. Da der Modulwert in die
  Gesamtnote eingeht, HOB ein gemeldeter Schaden die Bewertung sogar an.
* **Nicht-monotone Note.** Ab 31 Berichten verlangte ein relativer Filter, dass
  eine Zone sich vom Zonen-Mittelwert abhebt. Bei nur einem betroffenen Zonentyp
  ist der Mittelwert genau dessen Wert — der Befund wurde also ausgerechnet dann
  unterdrueckt, wenn die Evidenz am eindeutigsten war. Gemessen: 60 Totalschaeden
  (93,8) wurden besser bewertet als 20 (90,0).
"""

import pytest

from app.services.analysis.service_patterns import (
    BOAT_CLASS_DEFAULTS,
    analyze_severity_burden,
    run_service_patterns_analysis,
)

ZONES = [
    {
        "name": "Rumpf",
        "zone_type": "hull",
        "polygon": [[0, 0], [3000, 0], [3000, 2000], [0, 2000]],
        "height_mm": 1900,
    },
    {
        "name": "Salon",
        "zone_type": "saloon",
        "polygon": [[0, 2000], [3000, 2000], [3000, 4000], [0, 4000]],
        "height_mm": 1950,
    },
]


def _reports(count: int, severity: str = "critical", zone_type: str = "hull") -> list[dict]:
    return [
        {
            "report_type": "repair",
            "category": "hull_structure",
            "zone_type": zone_type,
            "severity": severity,
            "description": f"Schaden {i}",
            "boat_age_months": 36,
            "cost_eur": 5000.0,
        }
        for i in range(count)
    ]


def _score(count: int, severity: str = "critical") -> float:
    result = run_service_patterns_analysis(
        zones=ZONES,
        passages=[],
        boat_class="cruising_sail",
        service_reports=_reports(count, severity),
    )
    return result["overall_score"]


class TestSchwereWirktSichAus:
    def test_critical_scores_worse_than_low(self):
        assert _score(10, "critical") < _score(10, "low"), (
            "Zehn Totalschaeden duerfen nicht dieselbe Note ergeben wie zehn "
            "kosmetische Befunde."
        )

    def test_severity_order_is_monotonic(self):
        scores = [_score(10, s) for s in ("low", "medium", "high", "critical")]
        assert scores == sorted(scores, reverse=True), (
            f"Note muss mit steigender Schwere fallen, ist aber {scores}"
        )

    def test_single_critical_report_costs_real_points(self):
        """Ein kritischer Totalschaden darf kein 95er-Zeugnis ergeben."""
        assert _score(1, "critical") < _score(1, "low")

    def test_severity_burden_is_part_of_the_module(self):
        result = run_service_patterns_analysis(
            zones=ZONES, passages=[], boat_class="cruising_sail",
            service_reports=_reports(3),
        )
        assert "severity_burden" in result["sub_scores"]


class TestMehrSchadenNiemalsBessereNote:
    @pytest.mark.parametrize("severity", ["low", "medium", "high", "critical"])
    def test_score_never_rises_with_more_reports(self, severity):
        counts = [1, 5, 10, 20, 30, 31, 40, 60, 100]
        scores = [_score(n, severity) for n in counts]
        for (n_prev, s_prev), (n_now, s_now) in zip(
            zip(counts, scores), zip(counts[1:], scores[1:])
        ):
            assert s_now <= s_prev + 1e-9, (
                f"{severity}: {n_now} Berichte ({s_now}) wurden besser bewertet "
                f"als {n_prev} ({s_prev})."
            )

    def test_findings_do_not_vanish_past_the_relative_gate(self):
        """Der relative Filter darf Befunde nicht ausgerechnet bei viel Evidenz abschalten."""
        few = run_service_patterns_analysis(
            zones=ZONES, passages=[], boat_class="cruising_sail",
            service_reports=_reports(20),
        )
        many = run_service_patterns_analysis(
            zones=ZONES, passages=[], boat_class="cruising_sail",
            service_reports=_reports(60),
        )
        assert len(many["warnings"]) >= len(few["warnings"]), (
            "60 Totalschaeden ergaben weniger Warnungen als 20."
        )


class TestSeverityBurdenEinzeln:
    def test_clean_inspection_is_not_a_burden(self):
        reports = [
            {"report_type": "inspection", "severity": "low", "description": "ohne Befund"}
        ]
        score, warnings, metrics = analyze_severity_burden(reports, {})
        assert score == 100.0
        assert metrics["counted_reports"] == 0
        assert not warnings

    def test_critical_report_raises_a_critical_warning(self):
        score, warnings, _ = analyze_severity_burden(_reports(1, "critical"), {})
        assert score < 100.0
        assert any(w["severity"] == "critical" for w in warnings)

    def test_every_warning_carries_a_suggestion(self):
        """Projektkonvention: jede Warnung hat einen Handlungsvorschlag."""
        _, warnings, _ = analyze_severity_burden(_reports(5, "critical"), {})
        assert all(w.get("suggestion") for w in warnings)

    def test_score_stays_on_scale(self):
        for count in (1, 50, 500):
            score, _, _ = analyze_severity_burden(_reports(count), {})
            assert 0.0 <= score <= 100.0


def test_weights_still_sum_to_one_for_every_boat_class():
    """Der BoatDNA-Resolver verlaesst sich auf diese Invariante."""
    for boat_class, config in BOAT_CLASS_DEFAULTS.items():
        total = sum(config["weights"].values())
        assert abs(total - 1.0) < 1e-9, f"{boat_class}: Summe {total}"
