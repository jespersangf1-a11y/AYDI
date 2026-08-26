"""Uebersetzung von Analysewarnungen an der Praesentationsgrenze.

**Warum nicht in den Modulen.** Die Analysemodule sind reine Funktionen; eine
reine Funktion sollte kein lokalisiertes Prosa-Ergebnis erzeugen, sondern einen
stabilen ``code`` plus die gemessenen Werte. Genau deshalb war i18n bisher
wirkungslos: Der Katalog (`app/core/i18n.py`) war vollstaendig, aber ``t()`` wurde
in **keinem** der zwoelf Analysemodule aufgerufen — ein Vollanalyse-Lauf mit
``set_locale("en")`` lieferte 237 deutsche Strings.

**Wie es jetzt laeuft.** Jede Warnung traegt ``code`` (seit dem Nachziehen der 47
fehlenden Codes ausnahmslos) und, wo Messwerte im Text stehen, ein ``params``-Dict.
``localize_warning`` setzt daraus die Meldung in der aktiven Sprache zusammen.

**Der deutsche Text bleibt immer erhalten.** Fehlt eine Uebersetzung, gewinnt der
mitgelieferte ``message``-String. Das ist bewusst so: Lieber eine korrekte
deutsche Meldung als eine luerckenhafte englische — und der Ausbau kann Modul fuer
Modul erfolgen, ohne dass zwischendurch etwas fehlt.
"""

from __future__ import annotations

import logging

from app.core.i18n import Locale, get_locale

logger = logging.getLogger(__name__)


# code -> {locale: template}. Platzhalter in geschweiften Klammern werden aus
# ``params`` gefuellt. Ein Code ohne Eintrag faellt auf den deutschen Originaltext
# zurueck — siehe Modul-Docstring.
WARNING_TRANSLATIONS: dict[str, dict[str, str]] = {}


def register(code: str, *, de: str, en: str, es: str, fr: str) -> None:
    """Eine Warnungs-Uebersetzung eintragen (alle vier Sprachen verpflichtend)."""
    WARNING_TRANSLATIONS[code] = {"de": de, "en": en, "es": es, "fr": fr}


# Zonentyp -> Bezeichnung je Sprache.
#
# In den Modulen standen dafuer hartkodierte deutsche Tabellen
# ({"engine": "Maschinenraum", ...}). Bei einer FEHLENDEN Zone ist das kein
# Nutzername, sondern eine Typbezeichnung — sie gehoert uebersetzt. Steht
# ``zone_type`` in den Parametern, fuellt localize_warning daraus ``zone_label``.
ZONE_TYPE_LABELS: dict[str, dict[str, str]] = {
    "engine": {"de": "Maschinenraum", "en": "engine room", "es": "sala de maquinas", "fr": "compartiment moteur"},
    "engine_room": {"de": "Maschinenraum", "en": "engine room", "es": "sala de maquinas", "fr": "compartiment moteur"},
    "pantry": {"de": "Pantry", "en": "galley", "es": "cocina", "fr": "cuisine"},
    "helm": {"de": "Steuerstand", "en": "helm station", "es": "puesto de gobierno", "fr": "poste de barre"},
    "head": {"de": "WC/Bad", "en": "heads", "es": "aseo", "fr": "cabinet de toilette"},
    "storage": {"de": "Stauraum", "en": "storage", "es": "estiba", "fr": "rangement"},
    "saloon": {"de": "Salon", "en": "saloon", "es": "salon", "fr": "carre"},
    "cabin": {"de": "Kabine", "en": "cabin", "es": "camarote", "fr": "cabine"},
    "cockpit": {"de": "Cockpit", "en": "cockpit", "es": "banera", "fr": "cockpit"},
}


def zone_label(zone_type: str, lang: str) -> str | None:
    """Lokalisierte Bezeichnung eines Zonentyps, sonst None."""
    entry = ZONE_TYPE_LABELS.get((zone_type or "").strip().lower())
    return entry.get(lang) if entry else None


def localize_warning(warning: dict, locale: Locale | str | None = None) -> dict:
    """Eine Warnung in die aktive Sprache uebersetzen.

    Gibt eine KOPIE zurueck; das Original bleibt unveraendert, damit
    gespeicherte Analyseergebnisse sprachneutral bleiben und spaeter in einer
    anderen Sprache dargestellt werden koennen.

    Der deutsche Originaltext bleibt als ``message_de`` erhalten, damit
    nachvollziehbar ist, was das Modul tatsaechlich gemeldet hat.
    """
    if not isinstance(warning, dict):
        return warning

    target = locale or get_locale()
    lang = target.value if isinstance(target, Locale) else str(target)

    result = dict(warning)
    code = warning.get("code")
    templates = WARNING_TRANSLATIONS.get(code or "")
    if not templates:
        return result

    template = templates.get(lang)
    if not template or lang == "de":
        return result

    params = dict(warning.get("params") or {})
    # Typbezeichnungen mit uebersetzen, statt eine deutsche Vokabel in einen
    # englischen Satz zu setzen ("Critical zone missing: Maschinenraum").
    if "zone_type" in params:
        label = zone_label(params["zone_type"], lang)
        if label:
            # Bewusst ueberschreiben: In params steht die deutsche Bezeichnung,
            # die das Modul fuer den Fallback-Text gebildet hat. Kennt die
            # Tabelle den Typ nicht (z.B. weil dort ein NUTZERdefinierter
            # Zonenname steht), liefert zone_label None und der Originalwert
            # bleibt unangetastet.
            params["zone_label"] = label
    try:
        result["message_de"] = warning.get("message")
        result["message"] = template.format(**params)
    except (KeyError, IndexError, ValueError):
        # Fehlender oder falsch benannter Platzhalter: lieber die korrekte
        # deutsche Meldung als eine halb gefuellte uebersetzte.
        logger.warning(
            "Uebersetzung fuer %s (%s) passt nicht zu den Parametern %s",
            code, lang, sorted(params),
        )
        result.pop("message_de", None)
    return result


def localize_analysis(result: dict, locale: Locale | str | None = None) -> dict:
    """Alle Warnungen eines Vollanalyse-Ergebnisses uebersetzen.

    Arbeitet auf einer flachen Kopie je Modul — das uebrige Ergebnis
    (Scores, Metriken) bleibt unangetastet.
    """
    if not isinstance(result, dict) or not isinstance(result.get("modules"), dict):
        return result

    localized_modules = {}
    for name, module_result in result["modules"].items():
        if not isinstance(module_result, dict):
            localized_modules[name] = module_result
            continue
        warnings = module_result.get("warnings")
        if not warnings:
            localized_modules[name] = module_result
            continue
        copy = dict(module_result)
        copy["warnings"] = [localize_warning(w, locale) for w in warnings]
        localized_modules[name] = copy

    out = dict(result)
    out["modules"] = localized_modules
    return out


def translation_coverage() -> dict[str, int]:
    """Wie viele Codes uebersetzt sind — fuer Tests und ehrliche Berichterstattung."""
    return {
        "translated_codes": len(WARNING_TRANSLATIONS),
        "locales_per_code": 4 if WARNING_TRANSLATIONS else 0,
    }


# ---------------------------------------------------------------------------
# Katalog
#
# Abgedeckt sind zuerst die drei Module, die JEDER Nutzer sieht — ergonomics,
# volume_storage und emotional bilden die unauthentifizierte Level-1-
# Schnellanalyse und damit den Einstieg ins Produkt.
# ---------------------------------------------------------------------------

# --- ergonomics ------------------------------------------------------------
register(
    "ERGO_PASSAGE_WIDTH_UNKNOWN",
    de="Durchgang {from_zone}→{to_zone}: Breite nicht beurteilbar — aus der importierten Geometrie nicht ableitbar.",
    en="Passage {from_zone}→{to_zone}: width cannot be assessed — not derivable from the imported geometry.",
    es="Paso {from_zone}→{to_zone}: no se puede evaluar el ancho — no derivable de la geometria importada.",
    fr="Passage {from_zone}→{to_zone} : largeur non evaluable — non deductible de la geometrie importee.",
)
register(
    "ERGO_PASSAGE_CRITICAL",
    de="Durchgang {from_zone}→{to_zone} ist kritisch schmal ({width:.0f}mm, Minimum: {minimum:.0f}mm)",
    en="Passage {from_zone}→{to_zone} is critically narrow ({width:.0f}mm, minimum: {minimum:.0f}mm)",
    es="El paso {from_zone}→{to_zone} es criticamente estrecho ({width:.0f}mm, minimo: {minimum:.0f}mm)",
    fr="Le passage {from_zone}→{to_zone} est critiquement etroit ({width:.0f}mm, minimum : {minimum:.0f}mm)",
)
register(
    "ERGO_PASSAGE_NARROW",
    de="Durchgang {from_zone}→{to_zone} ist zu schmal ({width:.0f}mm, empfohlen: {recommended:.0f}mm)",
    en="Passage {from_zone}→{to_zone} is too narrow ({width:.0f}mm, recommended: {recommended:.0f}mm)",
    es="El paso {from_zone}→{to_zone} es demasiado estrecho ({width:.0f}mm, recomendado: {recommended:.0f}mm)",
    fr="Le passage {from_zone}→{to_zone} est trop etroit ({width:.0f}mm, recommande : {recommended:.0f}mm)",
)
register(
    "ERGO_ZONE_ISOLATED",
    de="Zone '{zone}' ist isoliert (keine Durchgänge)",
    en="Zone '{zone}' is isolated (no passages)",
    es="La zona '{zone}' esta aislada (sin pasos)",
    fr="La zone '{zone}' est isolee (aucun passage)",
)
register(
    "ERGO_NO_HELM",
    de="Kein Steuerstand im Layout definiert",
    en="No helm station defined in the layout",
    es="Ningun puesto de gobierno definido en la distribucion",
    fr="Aucun poste de barre defini dans l'amenagement",
)
register(
    "ERGO_ZONE_MISSING",
    de="Kritische Zone fehlt: {zone_label}",
    en="Critical zone missing: {zone_label}",
    es="Falta una zona critica: {zone_label}",
    fr="Zone critique manquante : {zone_label}",
)
register(
    "ERGO_ZONE_UNREACHABLE",
    de="{zone_label} ist nicht erreichbar",
    en="{zone_label} is unreachable",
    es="{zone_label} no es accesible",
    fr="{zone_label} est inaccessible",
)

# --- volume_storage --------------------------------------------------------
register(
    "VOL_NO_STORAGE",
    de="Keine Stauräume im Layout definiert",
    en="No storage zones defined in the layout",
    es="Ninguna zona de estiba definida en la distribucion",
    fr="Aucun rangement defini dans l'amenagement",
)
register(
    "VOL_NO_FURNITURE_DATA",
    de="Keine Möblierungsdaten vorhanden — Bewertung nicht möglich",
    en="No furnishing data available — assessment not possible",
    es="No hay datos de mobiliario — evaluacion no posible",
    fr="Aucune donnee d'amenagement — evaluation impossible",
)
register(
    "VOL_NO_ZONES",
    de="Keine Zonen definiert — Volumennutzung kann nicht bewertet werden",
    en="No zones defined — volume utilisation cannot be assessed",
    es="Ninguna zona definida — no se puede evaluar el aprovechamiento del volumen",
    fr="Aucune zone definie — l'utilisation du volume ne peut etre evaluee",
)
register(
    "VOL_STORAGE_UNREACHABLE",
    de="Stauraum '{zone}' ist nicht erreichbar",
    en="Storage zone '{zone}' is unreachable",
    es="La zona de estiba '{zone}' no es accesible",
    fr="Le rangement '{zone}' est inaccessible",
)

# --- emotional -------------------------------------------------------------
register(
    "EMO_NO_HEIGHT_DATA",
    de="Keine Höhendaten vorhanden — Raumproportionen nicht bewertbar",
    en="No height data available — room proportions cannot be assessed",
    es="No hay datos de altura — no se pueden evaluar las proporciones",
    fr="Aucune donnee de hauteur — proportions non evaluables",
)
register(
    "EMO_NO_WINDOW_DATA",
    de="Keine Fensterdaten vorhanden — Lichtverteilung nicht bewertbar",
    en="No window data available — light distribution cannot be assessed",
    es="No hay datos de ventanas — no se puede evaluar la distribucion de luz",
    fr="Aucune donnee de fenetres — repartition de la lumiere non evaluable",
)
register(
    "EMO_NO_MATERIAL_DATA",
    de="Keine Materialdaten vorhanden — visuelle Ruhe nicht bewertbar",
    en="No material data available — visual calm cannot be assessed",
    es="No hay datos de materiales — no se puede evaluar la calma visual",
    fr="Aucune donnee de materiaux — calme visuel non evaluable",
)
register(
    "EMO_NO_COCKPIT",
    de="Kein Cockpit im Layout — Innen-Außen-Übergang nicht bewertbar",
    en="No cockpit in the layout — indoor-outdoor transition cannot be assessed",
    es="Sin banera en la distribucion — no se puede evaluar la transicion interior-exterior",
    fr="Aucun cockpit dans l'amenagement — transition interieur-exterieur non evaluable",
)
register(
    "EMO_NO_COCKPIT_PASSAGE",
    de="Kein Durchgang zum Cockpit vorhanden",
    en="No passage to the cockpit",
    es="No hay paso hacia la banera",
    fr="Aucun passage vers le cockpit",
)
register(
    "EMO_ZONE_TOO_DARK",
    de="Zone '{zone}' zu dunkel (Fensteranteil: {pct:.0%}, Ziel: {target:.0%})",
    en="Zone '{zone}' is too dark (window ratio: {pct:.0%}, target: {target:.0%})",
    es="La zona '{zone}' es demasiado oscura (proporcion de ventanas: {pct:.0%}, objetivo: {target:.0%})",
    fr="La zone '{zone}' est trop sombre (part vitree : {pct:.0%}, cible : {target:.0%})",
)
register(
    "EMO_CEILING_LOW",
    de="Deckenhöhe in '{zone}' zu niedrig ({height:.0f}mm, Minimum: {minimum:.0f}mm)",
    en="Headroom in '{zone}' is too low ({height:.0f}mm, minimum: {minimum:.0f}mm)",
    es="La altura libre en '{zone}' es insuficiente ({height:.0f}mm, minimo: {minimum:.0f}mm)",
    fr="La hauteur sous barrots dans '{zone}' est trop faible ({height:.0f}mm, minimum : {minimum:.0f}mm)",
)
