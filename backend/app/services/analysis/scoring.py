"""Gemeinsame Gewichtung der Teilanalysen.

Hintergrund
-----------
Jedes Analysemodul besteht aus mehreren Teilanalysen, deren Noten über feste
Gewichte zu einer Modulnote verrechnet werden. Bisher lief das in jedem Modul
als ``sum(sub_scores.get(k, <Vorgabe>) * w for k, w in weights.items())``.

Damit gab es keine Möglichkeit auszudrücken, dass eine Teilanalyse *nicht
beurteilbar* war. Wer nichts zu prüfen hatte, musste eine Zahl liefern — und
lieferte meist 100.0. Eine Relingprüfung ohne auffindbare Decksbereiche, eine
Notausstiegsprüfung ohne erkannte Kabinen und eine Lenzprüfung ohne gefundenes
Cockpit meldeten so volle Punktzahl. Das ist eine Freigabe für etwas, das nie
untersucht wurde, und widerspricht der Grundregel des Projekts: lieber
"nicht beurteilbar" als geraten (siehe CLAUDE.md).

Vereinbarung
------------
Eine Teilanalyse gibt ``None`` als Note zurück, wenn ihr die Grundlage fehlt.
``weighted_overall`` lässt sie dann aus und verteilt ihr Gewicht auf die
tatsächlich geprüften Teilanalysen. Die Modulnote steht damit für das, was
geprüft wurde — nicht mehr und nicht weniger. Welche Teilanalysen ausgelassen
wurden, wird zurückgegeben und gehört in die Modulantwort, damit in der
Oberfläche nachvollziehbar bleibt, worauf sich die Note stützt.

Fällt jede Teilanalyse aus, gibt es keine Note. Dann meldet das Modul sich als
nicht beurteilbar, statt eine Zahl zu erfinden.
"""

# Note einer Teilanalyse, der die Datengrundlage fehlt. Bewusst ``None`` und
# nicht 0 oder 50: beides wären Zahlen, die sich in der Oberfläche nicht von
# einer gemessenen unterscheiden lassen.
NICHT_BEWERTBAR = None


def weighted_overall(
    sub_scores: dict[str, float | None],
    weights: dict[str, float],
) -> tuple[float | None, list[str]]:
    """Verrechnet die Teilnoten zu einer Modulnote.

    Teilanalysen mit der Note ``None`` bleiben unberücksichtigt; ihr Gewicht
    wird auf die übrigen verteilt (das verbleibende Gewicht wird auf 1
    normiert). Teilanalysen, für die es gar keinen Eintrag gibt, gelten
    ebenfalls als nicht bewertet — früher gingen sie mit einem Vorgabewert in
    die Rechnung ein, obwohl ihr Fehlen in aller Regel ein Fehlschlag war.

    Rückgabe: (Modulnote oder ``None``, Namen der nicht bewerteten Teilanalysen)
    """
    bewertet: dict[str, float] = {}
    nicht_bewertet: list[str] = []

    for name, gewicht in weights.items():
        note = sub_scores.get(name)
        if note is None:
            # Eine Teilanalyse, die für diese Bootsklasse ohnehin mit Gewicht 0
            # geführt wird (etwa Krängung bei einer Motoryacht), ist kein
            # Datenausfall. Sie in die Lückenliste zu schreiben würde einen
            # Mangel melden, wo die Klassenvorgabe die Prüfung gar nicht vorsieht.
            if gewicht > 0.0:
                nicht_bewertet.append(name)
        else:
            bewertet[name] = gewicht

    # Teilanalysen ohne Gewicht in der Klassenvorgabe würden sonst stillschweigend
    # unter den Tisch fallen. Sie zählen nicht in die Note, sind aber auch kein
    # Ausfall — sie tauchen deshalb nicht in ``nicht_bewertet`` auf.

    gewichtssumme = sum(bewertet.values())
    if gewichtssumme <= 0.0:
        return None, nicht_bewertet

    gesamt = sum(
        float(sub_scores[name]) * gewicht / gewichtssumme
        for name, gewicht in bewertet.items()
    )
    return gesamt, nicht_bewertet


def hinweis_teilanalysen(nicht_bewertet: list[str]) -> str | None:
    """Satz für die Oberfläche, welche Teilprüfungen entfallen sind.

    Gibt ``None`` zurück, wenn alles geprüft werden konnte — dann gibt es auch
    nichts einzuschränken.
    """
    if not nicht_bewertet:
        return None
    return (
        "Nicht bewertet mangels Datengrundlage: "
        + ", ".join(sorted(nicht_bewertet))
        + ". Die Modulnote bezieht sich nur auf die geprüften Teilanalysen."
    )
