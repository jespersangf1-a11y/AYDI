"""Einheitliche Schreibweise der Zonentypen.

Warum es diese Datei gibt
-------------------------
Im Projekt existierten zwei Wortlisten nebeneinander:

* ``VALID_ZONE_TYPES`` in ``app/core/validation.py`` kannte ``saloon`` und
  ``engine_room``.
* Die elf Analysemodule prüfen auf ``salon`` und ``engine`` — ebenso die
  Seed-Daten.

Beide Seiten hielten sich für richtig, und keine merkte etwas davon. Die Folgen
waren still und ernst, weil die Module ihre Prüfmengen über exakte
Mengenzugehörigkeit bilden (``z["zone_type"] in _SLEEPING_ZONE_TYPES``):

* Ein Layout mit ``saloon`` war für die Wohnbereichsprüfung schlicht nicht
  vorhanden — der Brandschutzabstand zum Motorraum wurde nie gemessen.
* Ein Layout mit ``engine_room`` hatte für die Lüftungsprüfung keinen
  Motorraum. Sie meldete daraufhin volle Punktzahl.
* ``salon`` wiederum stand nicht in ``VALID_ZONE_TYPES`` und erzeugte bei jedem
  Import die Protokollzeile "Unknown zone type" — für Daten, die überall sonst
  im Projekt als richtig galten.

Eine falsche Schreibweise durfte also dazu führen, dass eine Sicherheitsprüfung
ausfällt und das Ergebnis trotzdem als bestanden aussieht. Deshalb gibt es ab
hier genau eine Liste, und alles andere wird darauf abgebildet.

Verwendung
----------
``normalisiere_zonentyp`` bildet eine Eingabe auf die kanonische Schreibweise
ab. ``normalisiere_zonen`` wendet das auf eine ganze Zonenliste an und meldet
zurück, welche Typen unbekannt blieben — unbekannt heißt: die Zone geht in
keine typbezogene Prüfung ein, und das muss dem Anwender gesagt werden, statt
es in einer Protokolldatei zu vergraben.
"""

# Kanonische Schreibweisen. Maßgeblich sind die Formen, die die Analysemodule
# und die Seed-Daten verwenden — sie zu ändern hieße, elf Module und den
# Datenbestand anzufassen; die Synonymtabelle darunter ist der billigere und
# sicherere Weg.
KANONISCHE_ZONENTYPEN = frozenset({
    # Innenraum
    "cabin", "salon", "pantry", "head", "storage", "forepeak",
    "aft_cabin", "quarter_berth", "workshop", "crew_quarters", "shower",
    # Deck
    "cockpit", "foredeck", "side_deck", "flybridge", "swim_platform",
    # Maschine und Systeme
    "engine", "fuel_tank", "shaft_tunnel", "electrical_panel",
    "battery_compartment", "nav_station", "water_tank", "holding_tank",
    "tender_garage",
    # Struktur
    "hull", "keel", "rudder", "bulkhead", "frame", "transom",
    # Rigg
    "mast", "rigging", "deck_hardware", "sail_storage",
    # Sicherheit
    "safety_locker", "liferaft_storage", "fire_station",
    # Steuerstand
    "helm", "flybridge_helm",
    # Allgemein
    "crew_area", "guest_area", "technical", "void",
})

# Abweichende Schreibweisen auf die kanonische Form. Enthalten sind die im
# Projekt tatsächlich aufgetretenen Varianten (britisch/amerikanisch, mit und
# ohne Unterstrich, deutsche Bezeichnungen aus CAD-Importen) — nicht alles
# Denkbare, sondern das, was zu einem stillen Prüfausfall geführt hat.
SYNONYME: dict[str, str] = {
    # Salon
    "saloon": "salon",
    "main_saloon": "salon",
    "main_salon": "salon",
    "sallon": "salon",
    "lounge": "salon",
    "hauptsalon": "salon",
    # Pantry / Kombüse
    "galley": "pantry",
    "kitchen": "pantry",
    "kombuese": "pantry",
    "kombüse": "pantry",
    "kueche": "pantry",
    "küche": "pantry",
    # Maschinenraum
    "engine_room": "engine",
    "engineroom": "engine",
    "engine_bay": "engine",
    "machinery": "engine",
    "machinery_space": "engine",
    "maschinenraum": "engine",
    "motorraum": "engine",
    # Kabinen
    "berth": "cabin",
    "stateroom": "cabin",
    "master_cabin": "cabin",
    "master_stateroom": "cabin",
    "vip_cabin": "cabin",
    "owner_suite": "cabin",
    "owners_cabin": "cabin",
    "guest_cabin": "cabin",
    "kabine": "cabin",
    "koje": "cabin",
    "fwd_cabin": "cabin",
    "forward_cabin": "cabin",
    # Mannschaft
    "crew": "crew_quarters",
    "crew_cabin": "crew_quarters",
    "crew_mess": "crew_quarters",
    "mannschaftsraum": "crew_quarters",
    # Nasszelle
    "heads": "head",
    "toilet": "head",
    "wc": "head",
    "bathroom": "head",
    "nasszelle": "head",
    "bad": "head",
    # Stauraum
    "locker": "storage",
    "lazarette": "storage",
    "stowage": "storage",
    "garage": "tender_garage",
    "stauraum": "storage",
    # Deck
    "bow": "foredeck",
    "fore_deck": "foredeck",
    "vordeck": "foredeck",
    "deck": "side_deck",
    "sidedeck": "side_deck",
    "badeplattform": "swim_platform",
    "swimplatform": "swim_platform",
    # Steuerstand
    "wheelhouse": "helm",
    "pilothouse": "helm",
    "steering": "helm",
    "steuerstand": "helm",
    "ruderhaus": "helm",
    # Cockpit
    "aft_cockpit": "cockpit",
    "centre_cockpit": "cockpit",
    "center_cockpit": "cockpit",
    # Navigation
    "navstation": "nav_station",
    "chart_table": "nav_station",
    "kartentisch": "nav_station",
}


def normalisiere_zonentyp(wert: object) -> str:
    """Bildet eine Zonentyp-Angabe auf die kanonische Schreibweise ab.

    Unbekannte Angaben werden unverändert (nur getrimmt und kleingeschrieben)
    zurückgegeben. Sie werden bewusst nicht auf einen Vorgabewert gezwungen:
    eine Zone einfach als ``salon`` zu behandeln, weil man ihren Typ nicht
    kennt, wäre wieder eine Behauptung. Sie fällt stattdessen aus den
    typbezogenen Prüfungen heraus — und ``ist_bekannt`` macht das sichtbar.
    """
    if not isinstance(wert, str):
        return ""
    schluessel = wert.strip().lower().replace("-", "_").replace(" ", "_")
    if not schluessel:
        return ""
    return SYNONYME.get(schluessel, schluessel)


def ist_bekannt(zonentyp: str) -> bool:
    """Ob der (bereits normalisierte) Typ in einer Prüfung berücksichtigt wird."""
    return zonentyp in KANONISCHE_ZONENTYPEN


def normalisiere_zonen(zonen: list[dict]) -> tuple[list[dict], list[str]]:
    """Vereinheitlicht die Zonentypen einer ganzen Liste.

    Gibt (neue Zonenliste, unbekannt gebliebene Typen) zurück. Die Zonen werden
    flach kopiert, damit die Eingabedaten des Aufrufers unangetastet bleiben —
    die Analysemodule sind laut CLAUDE.md reine Funktionen.
    """
    ergebnis: list[dict] = []
    unbekannt: list[str] = []

    for zone in zonen:
        if not isinstance(zone, dict):
            continue
        kopie = dict(zone)
        roh = kopie.get("zone_type") or kopie.get("type") or ""
        typ = normalisiere_zonentyp(roh)
        kopie["zone_type"] = typ
        if typ and not ist_bekannt(typ) and typ not in unbekannt:
            unbekannt.append(typ)
        ergebnis.append(kopie)

    return ergebnis, unbekannt


def warnung_unbekannte_typen(unbekannt: list[str]) -> dict | None:
    """Befund für unbekannte Zonentypen — oder ``None``, wenn alle bekannt sind.

    Diese Warnung ist wichtiger, als sie aussieht: eine Zone mit unbekanntem Typ
    ist für die typbezogenen Prüfungen unsichtbar. Ohne diesen Hinweis liest
    sich das Ergebnis so, als sei sie geprüft und in Ordnung.
    """
    if not unbekannt:
        return None
    return {
        "code": "UNKNOWN_ZONE_TYPE",
        "severity": "warning",
        "message": (
            "Unbekannte Zonentypen: "
            + ", ".join(sorted(unbekannt))
            + ". Diese Zonen gehen in die typbezogenen Prüfungen "
            "(Flucht, Notausstieg, Reling, Lüftung, Brandschutz) nicht ein."
        ),
        "suggestion": (
            "Zonentyp auf eine bekannte Bezeichnung setzen, zum Beispiel "
            "salon, cabin, pantry, head, cockpit, engine, storage."
        ),
        "location": "layout",
    }
