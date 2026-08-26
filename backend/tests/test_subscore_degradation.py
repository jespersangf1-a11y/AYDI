"""Eine fehlgeschlagene Teilanalyse darf keine schlechte Note erzeugen.

Jedes Analysemodul zerlegt seine Arbeit in gewichtete Teilanalysen. Bricht eine
davon mit einer Exception ab, wurde sie frueher mit **0.0** in den gewichteten
Mittelwert gezogen: Ein interner Fehler wurde so zu einer schlechten Bewertung
des Bootes — und dem Nutzer als Messergebnis praesentiert. Das widerspricht der
Grundregel "lieber nicht beurteilbar als geraten".

Erwartetes Verhalten:
* Eine fehlgeschlagene Teilanalyse wird aus Zaehler UND Nenner genommen.
* Sie erscheint als kritische Warnung und in ``degraded_subanalyses``.
* Faellt jede Teilanalyse aus, meldet das Modul ``available: False``.
"""

import pytest

from app.services.analysis import ergonomics
from app.services.analysis.subscore import aggregate_subscores


class TestAggregateSubscores:
    def test_weighted_mean_without_failures(self):
        result = aggregate_subscores({"a": 80.0, "b": 40.0}, {"a": 0.5, "b": 0.5})
        assert result == pytest.approx(60.0)

    def test_weights_are_renormalised(self):
        """Gewichte muessen sich nicht zu 1.0 summieren."""
        result = aggregate_subscores({"a": 80.0, "b": 40.0}, {"a": 1.0, "b": 3.0})
        assert result == pytest.approx(50.0)

    def test_failed_subanalysis_is_excluded_not_zeroed(self):
        scores = {"a": 80.0}
        weights = {"a": 0.5, "b": 0.5}
        assert aggregate_subscores(scores, weights, failed=["b"]) == pytest.approx(80.0)
        # Zum Vergleich das alte Verhalten: b als 0.0 mitgerechnet.
        assert aggregate_subscores(scores, weights, failed=[], default=0.0) == pytest.approx(40.0)

    def test_all_failed_returns_none(self):
        assert aggregate_subscores({}, {"a": 0.5, "b": 0.5}, failed=["a", "b"]) is None

    def test_empty_weights_return_none(self):
        assert aggregate_subscores({"a": 80.0}, {}) is None

    def test_missing_score_uses_default(self):
        assert aggregate_subscores({}, {"a": 1.0}, default=50.0) == pytest.approx(50.0)


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
