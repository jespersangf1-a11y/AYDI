"""Zentrale Auskunft über die 13 unterstützten Bootsklassen.

Zwei Fragen, eine Antwort je Frage:
  * Welche Klassenschlüssel sind überhaupt zulässig? → aus dem ``BoatClass``-Enum.
  * Wie heißt eine Klasse für Nutzer? → aus dem i18n-Katalog.

Beides bewusst *abgeleitet* statt hier noch einmal aufgeschrieben. Vor dieser
Zusammenführung gab es drei Listen nebeneinander: eine feste Tabelle in diesem
Modul, ``VALID_BOAT_CLASSES`` aus dem Enum und der i18n-Katalog mit DE/EN/ES/FR.
Solche Listen laufen auseinander — und eine Klasse, die in einer davon fehlt,
fällt still aus der Prüfung oder erscheint im Bericht als roher englischer
Schlüssel. Läuft hier etwas auseinander, schlägt der Import fehl, nicht der
Nutzer auf.
"""

from app.core.i18n import t
from app.schemas.schemas import BoatClass

#: Alle zulässigen Klassenschlüssel, in der Reihenfolge des Enums.
BOAT_CLASSES: tuple[str, ...] = tuple(bc.value for bc in BoatClass)

#: i18n-Schlüssel je Klasse.
_LABEL_KEY = "boat_class.{}"


def label_for(boat_class: str, locale: str | None = None) -> str:
    """Bezeichnung einer Klasse in der aktiven Sprache.

    Fällt auf den Schlüssel selbst zurück. Das sollte für geprüfte Eingaben nie
    eintreten und ist nur dafür da, dass ein Altbestand-Datensatz mit einem
    nicht mehr geführten Schlüssel noch etwas anzeigt, statt eine Ausnahme
    auszulösen.
    """
    schluessel = _LABEL_KEY.format(boat_class)
    bezeichnung = t(schluessel) if locale is None else t(schluessel, locale=locale)
    # t() gibt bei unbekanntem Schlüssel den Schlüssel zurück.
    return boat_class if bezeichnung == schluessel else bezeichnung


def is_known(boat_class: str) -> bool:
    return boat_class in _KNOWN


_KNOWN = frozenset(BOAT_CLASSES)

#: Deutsche Bezeichnungen — als Abbildung für Aufrufer, die eine Tabelle
#: erwarten. Wird beim Import aus dem i18n-Katalog gefüllt, nicht gepflegt.
BOAT_CLASS_LABELS: dict[str, str] = {bc: label_for(bc, "de") for bc in BOAT_CLASSES}

# Wächter: jede Klasse braucht eine Bezeichnung. Ohne diese Zeile wäre eine
# neue Enum-Variante ohne i18n-Eintrag erst im Bericht aufgefallen — dort dann
# als englischer Schlüssel mitten im deutschen Text.
_ohne_bezeichnung = sorted(bc for bc, name in BOAT_CLASS_LABELS.items() if name == bc)
if _ohne_bezeichnung:
    raise RuntimeError(
        "Bootsklassen ohne i18n-Bezeichnung (boat_class.<schluessel> in "
        f"app/core/i18n.py ergaenzen): {', '.join(_ohne_bezeichnung)}"
    )
