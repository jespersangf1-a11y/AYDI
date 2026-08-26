"""Gewichtete Zusammenfassung von Teilanalyse-Scores.

Jedes Analysemodul zerlegt seine Arbeit in Teilanalysen ("Teilscores") und
gewichtet sie zu einer Modulnote. Schlaegt eine Teilanalyse mit einer Exception
fehl, wurde sie bisher mit **0.0** in den gewichteten Mittelwert gezogen. Ein
interner Fehler wurde damit zu einer schlechten Note fuer das Boot — dem Nutzer
als Messergebnis praesentiert, obwohl gar nichts gemessen wurde. Das verletzt
die Grundregel des Systems: lieber "nicht beurteilbar" als geraten.

Diese Helfer schliessen fehlgeschlagene Teilanalysen stattdessen aus dem
Mittelwert aus und normieren ueber die verbleibenden Gewichte. Faellt alles aus,
gibt es keine Note (``None``) — der Aufrufer meldet das Modul dann als nicht
beurteilbar.
"""

from __future__ import annotations

from typing import Iterable, Mapping


def aggregate_subscores(
    sub_scores: Mapping[str, float],
    weights: Mapping[str, float],
    failed: Iterable[str] = (),
    default: float = 0.0,
) -> float | None:
    """Gewichteter Mittelwert der Teilscores ohne die fehlgeschlagenen.

    Args:
        sub_scores: Teilanalyse-Name -> Score (0-100).
        weights: Teilanalyse-Name -> Gewicht. Muss sich nicht zu 1.0 summieren;
            es wird ueber die tatsaechlich genutzten Gewichte normiert.
        failed: Namen der Teilanalysen, die mit einer Exception abgebrochen sind.
            Sie werden aus Zaehler UND Nenner genommen.
        default: Wert fuer Teilanalysen, die weder Score noch Fehler geliefert
            haben (modulabhaengig historisch 0.0 oder 50.0).

    Returns:
        Die Modulnote auf der 0-100-Skala, oder ``None``, wenn keine einzige
        Teilanalyse verwertbar war.
    """
    failed_set = set(failed)
    usable = {k: w for k, w in weights.items() if k not in failed_set}
    total_weight = sum(usable.values())
    if total_weight <= 0:
        return None
    return sum(sub_scores.get(k, default) * w for k, w in usable.items()) / total_weight
