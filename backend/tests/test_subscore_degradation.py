"""Eine Teilanalyse ohne Ergebnis darf keine schlechte Note erzeugen.

Jedes Analysemodul zerlegt seine Arbeit in gewichtete Teilanalysen. Zwei Faelle
duerfen dabei nicht als Note in den Mittelwert eingehen: die Teilanalyse hat
keine Datengrundlage, oder sie stuerzt ab. Frueher gingen beide mit 0.0 (bzw.
einem Vorgabewert) ein — ein interner Fehler wurde so zu einer schlechten
Bewertung des Bootes und dem Nutzer als Messergebnis praesentiert. Das
widerspricht der Grundregel "lieber nicht beurteilbar als geraten".

Beide Faelle tragen jetzt ``None`` und werden von ``weighted_overall`` aus
Zaehler UND Nenner genommen. (Bis zur Zusammenfuehrung von main und
audit/fixes-checkpoint gab es dafuer zwei getrennte Mechanismen,
``scoring.weighted_overall`` und ``subscore.aggregate_subscores``; letzterer
ist entfallen.)

Erwartetes Verhalten:
* Eine ausgefallene Teilanalyse wird aus Zaehler UND Nenner genommen.
* Ein Absturz erscheint als kritische Warnung und in ``degraded_subanalyses``.
* Faellt jede Teilanalyse aus, meldet das Modul ``available: False``.
"""

import pytest

from app.services.analysis import ergonomics
from app.services.analysis.scoring import NICHT_BEWERTBAR, weighted_overall


class TestWeightedOverall:
    def test_weighted_mean_without_gaps(self):
        note, ausgelassen = weighted_overall({"a": 80.0, "b": 40.0}, {"a": 0.5, "b": 0.5})
        assert note == pytest.approx(60.0)
        assert ausgelassen == []

    def test_weights_are_renormalised(self):
        """Gewichte muessen sich nicht zu 1.0 summieren."""
        note, _ = weighted_overall({"a": 80.0, "b": 40.0}, {"a": 1.0, "b": 3.0})
        assert note == pytest.approx(50.0)

    def test_unassessable_subanalysis_is_excluded_not_zeroed(self):
        weights = {"a": 0.5, "b": 0.5}
        note, ausgelassen = weighted_overall({"a": 80.0, "b": NICHT_BEWERTBAR}, weights)
        assert note == pytest.approx(80.0), "b wurde offenbar als 0 mitgerechnet"
        assert ausgelassen == ["b"]
        # Zum Vergleich das alte Verhalten, das hier ausdruecklich NICHT gilt:
        alt = sum({"a": 80.0, "b": 0.0}[k] * w for k, w in weights.items())
        assert alt == pytest.approx(40.0)

    def test_missing_entry_counts_as_unassessed(self):
        """Ein fehlender Eintrag ist ein Ausfall, kein Vorgabewert."""
        note, ausgelassen = weighted_overall({"a": 80.0}, {"a": 0.5, "b": 0.5})
        assert note == pytest.approx(80.0)
        assert ausgelassen == ["b"]

    def test_all_unassessable_returns_none(self):
        note, ausgelassen = weighted_overall({}, {"a": 0.5, "b": 0.5})
        assert note is None
        assert sorted(ausgelassen) == ["a", "b"]

    def test_empty_weights_return_none(self):
        note, ausgelassen = weighted_overall({"a": 80.0}, {})
        assert note is None
        assert ausgelassen == []

    def test_zero_weighted_subanalysis_is_not_a_gap(self):
        """Gewicht 0 in der Klassenvorgabe heisst 'nicht vorgesehen', nicht 'fehlt'."""
        note, ausgelassen = weighted_overall({"a": 80.0}, {"a": 1.0, "b": 0.0})
        assert note == pytest.approx(80.0)
        assert ausgelassen == []


def _layout():
    zones = [
        {
            "name": name,
            "zone_type": zone_type,
            "polygon": [[0, i * 1500], [3000, i * 1500], [3000, (i + 1) * 1500], [0, (i + 1) * 1500]],
            "height_mm": 1950,
        }
        for i, (name, zone_type) in enumerate(
            [("Salon", "saloon"), ("Kabine", "cabin"), ("Nasszelle", "head"), ("Cockpit", "cockpit")]
        )
    ]
    passages = [
        {"name": "P1", "from_zone": "Salon", "to_zone": "Kabine", "width_mm": 620},
        {"name": "P2", "from_zone": "Salon", "to_zone": "Nasszelle", "width_mm": 600},
    ]
    return zones, passages


def _run(**kwargs):
    zones, passages = _layout()
    return ergonomics.run_ergonomics_analysis(
        zones=zones, passages=passages, boat_class="cruising_sail", **kwargs
    )


class TestModuleDegradation:
    def test_baseline_runs_clean(self):
        result = _run()
        assert result.get("available", True) is True
        assert result["degraded_subanalyses"] == []
        assert 0 <= result["overall_score"] <= 100

    def test_single_failure_does_not_drag_score_to_zero(self, monkeypatch):
        baseline = _run()["overall_score"]

        def boom(*args, **kwargs):
            raise RuntimeError("Teilanalyse kaputt")

        # Eine der gewichteten Teilanalysen zum Absturz bringen.
        target = "analyze_passage_widths"
        assert hasattr(ergonomics, target)
        monkeypatch.setattr(ergonomics, target, boom)

        degraded = _run()
        assert degraded.get("available", True) is True, "Ein Ausfall darf das Modul nicht abschalten"
        assert degraded["degraded_subanalyses"] == ["passage_width"], (
            f"Erwartet wurde genau die abgestuerzte Teilanalyse, "
            f"bekommen: {degraded['degraded_subanalyses']}"
        )
        assert any(
            w.get("severity") == "critical" for w in degraded["warnings"]
        ), "Der Ausfall muss als kritische Warnung erscheinen"
        # Kern der Sache: die Note bleibt im Bereich der uebrigen Teilanalysen,
        # statt durch eine 0.0 nach unten gezogen zu werden.
        assert degraded["overall_score"] > baseline * 0.5, (
            f"Note stuerzte von {baseline} auf {degraded['overall_score']} — "
            f"die fehlgeschlagene Teilanalyse wurde offenbar als 0 mitgerechnet."
        )

    def test_total_failure_reports_unavailable(self, monkeypatch):
        def boom(*args, **kwargs):
            raise RuntimeError("alles kaputt")

        for attr in dir(ergonomics):
            if attr.startswith("analyze_"):
                monkeypatch.setattr(ergonomics, attr, boom)

        result = _run()
        assert result.get("available") is False
        assert "Teilanalysen" in result.get("reason", "")
        assert result.get("warnings"), "Die Einzelfehler muessen erhalten bleiben"
