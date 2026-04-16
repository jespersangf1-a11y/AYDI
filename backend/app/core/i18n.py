"""Internationalization (i18n) framework for AYDI.

Supports DE (default), EN, ES, FR with marine-specific terminology.
All user-facing strings must go through this module.

Usage:
    from app.core.i18n import t, set_locale, get_locale, Locale

    # Set locale for current request (typically in middleware)
    set_locale("en")

    # Translate a key
    message = t("analysis.hull.osmosis_risk")
    # With interpolation
    message = t("analysis.value_with_unit", value="3,5", unit="mm")
"""

from __future__ import annotations

import contextvars
import logging
from enum import Enum
from typing import Any

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Locale enum
# ---------------------------------------------------------------------------

class Locale(str, Enum):
    DE = "de"
    EN = "en"
    ES = "es"
    FR = "fr"


DEFAULT_LOCALE = Locale.DE

# Context variable for request-scoped locale
_current_locale: contextvars.ContextVar[Locale] = contextvars.ContextVar(
    "current_locale", default=DEFAULT_LOCALE
)


def set_locale(locale: str | Locale) -> None:
    """Set the locale for the current async context."""
    if isinstance(locale, str):
        try:
            locale = Locale(locale.lower().split("-")[0].split("_")[0])
        except ValueError:
            logger.warning("Unknown locale %r, falling back to %s", locale, DEFAULT_LOCALE.value)
            locale = DEFAULT_LOCALE
    _current_locale.set(locale)


def get_locale() -> Locale:
    """Get the locale for the current async context."""
    return _current_locale.get()


# ---------------------------------------------------------------------------
# Number / currency / date formatting
# ---------------------------------------------------------------------------

class NumberFormatter:
    """Locale-aware number formatting following German/international conventions."""

    # (thousands_sep, decimal_sep, currency_symbol, currency_position, date_format)
    FORMATS: dict[Locale, dict[str, str]] = {
        Locale.DE: {
            "thousands_sep": ".",
            "decimal_sep": ",",
            "currency_fmt": "{value} \u20ac",
            "date_fmt": "%d.%m.%Y",
        },
        Locale.EN: {
            "thousands_sep": ",",
            "decimal_sep": ".",
            "currency_fmt": "\u20ac{value}",
            "date_fmt": "%m/%d/%Y",
        },
        Locale.ES: {
            "thousands_sep": ".",
            "decimal_sep": ",",
            "currency_fmt": "{value} \u20ac",
            "date_fmt": "%d/%m/%Y",
        },
        Locale.FR: {
            "thousands_sep": "\u202f",  # narrow no-break space
            "decimal_sep": ",",
            "currency_fmt": "{value} \u20ac",
            "date_fmt": "%d/%m/%Y",
        },
    }

    @classmethod
    def format_number(
        cls,
        value: float | int,
        decimals: int = 2,
        locale: Locale | None = None,
    ) -> str:
        """Format a number with locale-appropriate separators.

        Examples:
            DE: 1.234,56
            EN: 1,234.56
            FR: 1 234,56
        """
        if locale is None:
            locale = get_locale()

        fmt = cls.FORMATS[locale]

        if isinstance(value, int) or (isinstance(value, float) and value == int(value) and decimals == 0):
            int_val = int(value)
            # Format integer part with thousands separator
            neg = int_val < 0
            s = str(abs(int_val))
            groups = []
            while s:
                groups.append(s[-3:])
                s = s[:-3]
            int_str = fmt["thousands_sep"].join(reversed(groups))
            if decimals > 0:
                frac_str = "0" * decimals
                result = f"{int_str}{fmt['decimal_sep']}{frac_str}"
            else:
                result = int_str
            return f"-{result}" if neg else result

        # Float formatting
        neg = value < 0
        abs_val = abs(value)
        # Round first
        rounded = round(abs_val, decimals)
        int_part = int(rounded)
        frac_part = rounded - int_part

        # Integer part with thousands
        s = str(int_part)
        groups = []
        while s:
            groups.append(s[-3:])
            s = s[:-3]
        int_str = fmt["thousands_sep"].join(reversed(groups))

        # Decimal part
        frac_str = f"{frac_part:.{decimals}f}"[2:]  # strip "0."

        result = f"{int_str}{fmt['decimal_sep']}{frac_str}"
        return f"-{result}" if neg else result

    @classmethod
    def format_currency(
        cls,
        value: float | int,
        decimals: int = 2,
        locale: Locale | None = None,
    ) -> str:
        """Format a currency value (EUR) with locale conventions.

        Examples:
            DE: 2.997,00 EUR
            EN: EUR2,997.00
        """
        if locale is None:
            locale = get_locale()

        formatted_value = cls.format_number(value, decimals=decimals, locale=locale)
        return cls.FORMATS[locale]["currency_fmt"].format(value=formatted_value)

    @classmethod
    def format_percentage(
        cls,
        value: float,
        decimals: int = 1,
        locale: Locale | None = None,
    ) -> str:
        """Format a percentage value."""
        if locale is None:
            locale = get_locale()
        return f"{cls.format_number(value * 100, decimals=decimals, locale=locale)} %"


# ---------------------------------------------------------------------------
# Translation catalog
# ---------------------------------------------------------------------------

# The catalog is a nested dict: key -> {locale -> text}
# Keys use dot notation: "category.subcategory.key"
# Interpolation uses {variable_name} syntax.

_CATALOG: dict[str, dict[Locale, str]] = {}


def _register(key: str, de: str, en: str, es: str, fr: str) -> None:
    """Register a translation key with all 4 locale values."""
    _CATALOG[key] = {
        Locale.DE: de,
        Locale.EN: en,
        Locale.ES: es,
        Locale.FR: fr,
    }


# ---------------------------------------------------------------------------
# Translation function
# ---------------------------------------------------------------------------

def t(key: str, locale: Locale | None = None, **kwargs: Any) -> str:
    """Translate a key, optionally with variable interpolation.

    Args:
        key: Dot-notation translation key (e.g. "error.not_found")
        locale: Override locale (default: current context locale)
        **kwargs: Variables for interpolation

    Returns:
        Translated string, or the key itself if not found (with warning).
    """
    if locale is None:
        locale = get_locale()

    entry = _CATALOG.get(key)
    if entry is None:
        logger.warning("Missing translation key: %s", key)
        return key

    text = entry.get(locale)
    if text is None:
        # Fallback to German (always complete)
        text = entry.get(Locale.DE)
        if text is None:
            logger.warning("Missing translation for key %s in any locale", key)
            return key

    if kwargs:
        try:
            text = text.format(**kwargs)
        except KeyError as exc:
            logger.warning(
                "Missing interpolation variable %s for key %s", exc, key
            )
            # Return text with un-interpolated placeholders rather than crash
    return text


def has_key(key: str) -> bool:
    """Check if a translation key exists."""
    return key in _CATALOG


def get_all_keys() -> list[str]:
    """Return all registered translation keys (for testing/validation)."""
    return sorted(_CATALOG.keys())


def validate_catalog() -> list[str]:
    """Validate that all keys have translations for all 4 locales.

    Returns list of error messages (empty = valid).
    """
    errors = []
    for key, translations in _CATALOG.items():
        for locale in Locale:
            if locale not in translations or not translations[locale]:
                errors.append(f"Missing {locale.value} translation for: {key}")
    return errors


# ---------------------------------------------------------------------------
# Register all translations
# ---------------------------------------------------------------------------
# Organized by category. Each _register call ensures all 4 locales exist.

# ---- General / Common ----
_register("common.yes", "Ja", "Yes", "Si", "Oui")
_register("common.no", "Nein", "No", "No", "Non")
_register("common.unknown", "Unbekannt", "Unknown", "Desconocido", "Inconnu")
_register("common.not_available", "Nicht verfuegbar", "Not available", "No disponible", "Non disponible")
_register("common.not_assessable", "Nicht beurteilbar", "Cannot assess", "No evaluable", "Non evaluable")
_register("common.error", "Fehler", "Error", "Error", "Erreur")
_register("common.warning", "Warnung", "Warning", "Advertencia", "Avertissement")
_register("common.suggestion", "Empfehlung", "Suggestion", "Sugerencia", "Suggestion")
_register("common.score", "Bewertung", "Score", "Puntuacion", "Score")
_register("common.confidence", "Konfidenz", "Confidence", "Confianza", "Confiance")
_register("common.loading", "Wird geladen...", "Loading...", "Cargando...", "Chargement...")
_register("common.save", "Speichern", "Save", "Guardar", "Enregistrer")
_register("common.cancel", "Abbrechen", "Cancel", "Cancelar", "Annuler")
_register("common.delete", "Loeschen", "Delete", "Eliminar", "Supprimer")
_register("common.edit", "Bearbeiten", "Edit", "Editar", "Modifier")
_register("common.back", "Zurueck", "Back", "Atras", "Retour")
_register("common.next", "Weiter", "Next", "Siguiente", "Suivant")
_register("common.confirm", "Bestaetigen", "Confirm", "Confirmar", "Confirmer")

# ---- Auth ----
_register("auth.login_required", "Authentifizierung erforderlich", "Authentication required", "Autenticacion requerida", "Authentification requise")
_register("auth.invalid_credentials", "Ungueltiger Benutzername oder Passwort", "Invalid username or password", "Nombre de usuario o contrasena invalidos", "Nom d'utilisateur ou mot de passe invalide")
_register("auth.token_expired", "Sitzung abgelaufen. Bitte erneut anmelden.", "Session expired. Please log in again.", "Sesion expirada. Por favor, inicie sesion de nuevo.", "Session expiree. Veuillez vous reconnecter.")
_register("auth.insufficient_permissions", "Unzureichende Berechtigungen", "Insufficient permissions", "Permisos insuficientes", "Permissions insuffisantes")
_register("auth.tier_upgrade_required", "Upgrade auf {tier} erforderlich fuer diese Funktion", "Upgrade to {tier} required for this feature", "Se requiere actualizacion a {tier} para esta funcion", "Mise a niveau vers {tier} requise pour cette fonctionnalite")

# ---- Subscription Tiers ----
_register("tier.free", "Kostenlos", "Free", "Gratuito", "Gratuit")
_register("tier.pro", "Profi", "Pro", "Profesional", "Professionnel")
_register("tier.enterprise", "Werft / Enterprise", "Shipyard / Enterprise", "Astillero / Enterprise", "Chantier / Enterprise")
_register("tier.upgrade_prompt", "Upgrade auf {tier} fuer erweiterte Funktionen", "Upgrade to {tier} for advanced features", "Actualice a {tier} para funciones avanzadas", "Passez a {tier} pour des fonctionnalites avancees")

# ---- Errors ----
_register("error.not_found", "Nicht gefunden", "Not found", "No encontrado", "Non trouve")
_register("error.project_not_found", "Projekt nicht gefunden", "Project not found", "Proyecto no encontrado", "Projet non trouve")
_register("error.layout_not_found", "Layout nicht gefunden", "Layout not found", "Diseno no encontrado", "Disposition non trouvee")
_register("error.invalid_input", "Ungueltige Eingabe", "Invalid input", "Entrada invalida", "Entree invalide")
_register("error.validation_failed", "Validierung fehlgeschlagen: {details}", "Validation failed: {details}", "Validacion fallida: {details}", "Validation echouee : {details}")
_register("error.server_error", "Interner Serverfehler. Bitte spaeter erneut versuchen.", "Internal server error. Please try again later.", "Error interno del servidor. Intente de nuevo mas tarde.", "Erreur interne du serveur. Veuillez reessayer plus tard.")
_register("error.timeout", "Zeitueberschreitung. Bitte erneut versuchen.", "Request timed out. Please try again.", "Tiempo de espera agotado. Intente de nuevo.", "Delai d'attente depasse. Veuillez reessayer.")
_register("error.rate_limited", "Zu viele Anfragen. Bitte warten Sie einen Moment.", "Too many requests. Please wait a moment.", "Demasiadas solicitudes. Espere un momento.", "Trop de requetes. Veuillez patienter.")
_register("error.file_too_large", "Datei zu gross (max. {max_size} MB)", "File too large (max {max_size} MB)", "Archivo demasiado grande (max. {max_size} MB)", "Fichier trop volumineux (max. {max_size} Mo)")
_register("error.unsupported_format", "Nicht unterstuetztes Dateiformat: {format}", "Unsupported file format: {format}", "Formato de archivo no soportado: {format}", "Format de fichier non supporte : {format}")
_register("error.cad_parse_failed", "CAD-Datei konnte nicht gelesen werden. Unterstuetzte Formate: STEP, IGES, DXF.", "Could not parse CAD file. Supported formats: STEP, IGES, DXF.", "No se pudo leer el archivo CAD. Formatos soportados: STEP, IGES, DXF.", "Impossible de lire le fichier CAO. Formats supportes : STEP, IGES, DXF.")
_register("error.photo_low_resolution", "Fotoaufloesung zu niedrig. Mindestens {min_width}x{min_height} Pixel erforderlich.", "Photo resolution too low. Minimum {min_width}x{min_height} pixels required.", "Resolucion de foto demasiado baja. Se requieren al menos {min_width}x{min_height} pixeles.", "Resolution photo trop basse. Minimum {min_width}x{min_height} pixels requis.")
_register("error.api_unavailable", "Externer Dienst derzeit nicht erreichbar. Ergebnisse koennen unvollstaendig sein.", "External service currently unavailable. Results may be incomplete.", "Servicio externo no disponible actualmente. Los resultados pueden ser incompletos.", "Service externe actuellement indisponible. Les resultats peuvent etre incomplets.")
_register("error.partial_failure", "Einige Analysemodule konnten nicht ausgefuehrt werden. Verfuegbare Ergebnisse werden angezeigt.", "Some analysis modules could not be executed. Available results are shown.", "Algunos modulos de analisis no pudieron ejecutarse. Se muestran los resultados disponibles.", "Certains modules d'analyse n'ont pas pu etre executes. Les resultats disponibles sont affiches.")
_register("error.division_by_zero", "Berechnungsfehler: Division durch Null bei {context}", "Calculation error: division by zero at {context}", "Error de calculo: division por cero en {context}", "Erreur de calcul : division par zero a {context}")
_register("error.negative_value", "Ungueltiger negativer Wert: {field} = {value}", "Invalid negative value: {field} = {value}", "Valor negativo invalido: {field} = {value}", "Valeur negative invalide : {field} = {value}")
_register("error.future_date", "Datum liegt in der Zukunft: {field} = {value}", "Date is in the future: {field} = {value}", "La fecha esta en el futuro: {field} = {value}", "La date est dans le futur : {field} = {value}")

# ---- 10 Analysis Domains ----
_register("domain.hull_structure", "Rumpf & Struktur", "Hull & Structure", "Casco y estructura", "Coque et structure")
_register("domain.rigging_sails", "Rigg & Segel", "Rigging & Sails", "Aparejo y velas", "Greement et voiles")
_register("domain.propulsion_engine", "Antrieb & Motor", "Propulsion & Engine", "Propulsion y motor", "Propulsion et moteur")
_register("domain.electrical_electronics", "Elektrik & Elektronik", "Electrical & Electronics", "Electrica y electronica", "Electrique et electronique")
_register("domain.sanitary_water", "Sanitaer & Wasser", "Sanitary & Water", "Sanitario y agua", "Sanitaire et eau")
_register("domain.deck_fittings", "Deck & Beschlaege", "Deck & Fittings", "Cubierta y herrajes", "Pont et accastillage")
_register("domain.interior", "Innenausbau", "Interior Fitout", "Interior", "Amenagement interieur")
_register("domain.safety", "Sicherheit", "Safety", "Seguridad", "Securite")
_register("domain.navigation", "Navigation", "Navigation", "Navegacion", "Navigation")
_register("domain.maintenance_service", "Wartung & Service", "Maintenance & Service", "Mantenimiento y servicio", "Maintenance et entretien")

# Domain descriptions
_register("domain.hull_structure.desc", "GFK/CFK-Laminate, Osmose, Kielbolzen, Rumpfform, Stabilitaet, Strukturberechnungen, Verdraengung, Schwerpunktlage", "GRP/CFRP laminates, osmosis, keel bolts, hull shape, stability, structural calculations, displacement, center of gravity", "Laminados GRP/CFRP, osmosis, pernos de quilla, forma del casco, estabilidad, calculos estructurales, desplazamiento, centro de gravedad", "Stratifies PRV/PRFC, osmose, boulons de quille, forme de coque, stabilite, calculs structurels, deplacement, centre de gravite")
_register("domain.rigging_sails.desc", "Mastprofil, Wanten, Verstagung, Rollreffanlage, Segelschnitt, Beschlaege, Bloecke, Fallen, Trimm", "Mast profile, shrouds, rigging, roller furling, sail cut, fittings, blocks, halyards, trim", "Perfil del mastil, obenques, jarcia, enrollador, corte de velas, herrajes, motones, drizas, trimado", "Profil de mat, haubans, greement, enrouleur, coupe de voile, accastillage, poulies, drisses, reglage")
_register("domain.propulsion_engine.desc", "Dieselmotor, Saildrive, Wellenanlage, Propeller, Kraftstoffsystem, Kuehlkreislauf, Abgasanlage, Getriebe", "Diesel engine, saildrive, shaft system, propeller, fuel system, cooling circuit, exhaust system, gearbox", "Motor diesel, saildrive, sistema de eje, helice, sistema de combustible, circuito de refrigeracion, sistema de escape, caja de cambios", "Moteur diesel, saildrive, ligne d'arbre, helice, circuit carburant, circuit de refroidissement, echappement, boite de vitesses")
_register("domain.electrical_electronics.desc", "Batteriebank, Ladegeraete, Solarpanels, Verkabelung, Sicherungen, Bord-Netzwerk, Bussysteme (NMEA 2000, SignalK)", "Battery bank, chargers, solar panels, wiring, fuses, onboard network, bus systems (NMEA 2000, SignalK)", "Banco de baterias, cargadores, paneles solares, cableado, fusibles, red a bordo, sistemas de bus (NMEA 2000, SignalK)", "Banc de batteries, chargeurs, panneaux solaires, cablage, fusibles, reseau de bord, systemes bus (NMEA 2000, SignalK)")
_register("domain.sanitary_water.desc", "Frischwassertank, Watermaker, Pumpen, Seeventile, Toilettensystem, Abwasser, Schlauchfuehrung", "Fresh water tank, watermaker, pumps, seacocks, toilet system, wastewater, hose routing", "Tanque de agua dulce, potabilizadora, bombas, grifos de mar, sistema de inodoro, aguas residuales, recorrido de mangueras", "Reservoir d'eau douce, dessalinisateur, pompes, vannes de coque, systeme WC, eaux usees, cheminement des tuyaux")
_register("domain.deck_fittings.desc", "Klampen, Winschen, Ankergeschirr, Relingstuetzen, Lukendichtungen, Fensterdichtungen, Teakdeck, Leinenfuehrung", "Cleats, winches, anchor gear, stanchions, hatch seals, window seals, teak deck, line routing", "Cornamusas, winches, equipo de ancla, candeleros, juntas de escotilla, juntas de ventana, cubierta de teca, guia de cabos", "Taquets, winchs, mouillage, chandeliers, joints de panneau, joints de hublot, pont en teck, chemin de cordages")
_register("domain.interior.desc", "Kojen, Pantry, Nasszelle, Polster, Holzarbeiten, Isolation, Belueftung, Stauraum", "Berths, galley, wet room, upholstery, joinery, insulation, ventilation, stowage", "Literas, cocina, bano, tapiceria, carpinteria, aislamiento, ventilacion, almacenamiento", "Couchettes, cuisine, salle d'eau, sellerie, menuiserie, isolation, ventilation, rangement")
_register("domain.safety.desc", "Rettungsinsel, Sicherheitsgurte, Feuerschutz, Lenzpumpen, Seenotmittel, EPIRB, AIS, Blitzschutz", "Life raft, safety harnesses, fire protection, bilge pumps, distress signals, EPIRB, AIS, lightning protection", "Balsa salvavidas, arneses de seguridad, proteccion contra incendios, bombas de achique, senales de socorro, EPIRB, AIS, proteccion contra rayos", "Radeau de survie, harnais de securite, protection incendie, pompes de cale, moyens de detresse, EPIRB, AIS, protection foudre")
_register("domain.navigation.desc", "Kartenplotter, Autopilot, Radar, AIS, Windmesser, Log/Lot, Kompass, Funkgeraete", "Chart plotter, autopilot, radar, AIS, wind instruments, log/depth sounder, compass, radios", "Plotter de cartas, piloto automatico, radar, AIS, anemometro, corredera/sonda, compas, radios", "Traceur de cartes, pilote automatique, radar, AIS, anemometre, loch/sondeur, compas, radios")
_register("domain.maintenance_service.desc", "Wartungsintervalle, Winterlager, Antifouling, Zinkanoden, Oelwechsel, Dichtungstausch, Inspektionsprotokolle", "Maintenance intervals, winter storage, antifouling, zinc anodes, oil change, seal replacement, inspection protocols", "Intervalos de mantenimiento, almacenamiento invernal, antifouling, anodos de zinc, cambio de aceite, cambio de juntas, protocolos de inspeccion", "Intervalles de maintenance, hivernage, antifouling, anodes de zinc, vidange, remplacement joints, protocoles d'inspection")

# ---- Analysis Modules ----
_register("module.ergonomics", "Ergonomie", "Ergonomics", "Ergonomia", "Ergonomie")
_register("module.volume_storage", "Volumen & Stauraum", "Volume & Storage", "Volumen y almacenamiento", "Volume et rangement")
_register("module.emotional", "Design & Aesthetik", "Design & Aesthetics", "Diseno y estetica", "Design et esthetique")
_register("module.compliance", "Normen & Zulassung", "Compliance & Certification", "Normativa y certificacion", "Normes et certification")
_register("module.production", "Fertigung & Qualitaet", "Production & Quality", "Fabricacion y calidad", "Production et qualite")
_register("module.materials", "Materialien", "Materials", "Materiales", "Materiaux")
_register("module.structural", "Struktur & Festigkeit", "Structure & Strength", "Estructura y resistencia", "Structure et resistance")
_register("module.cost", "Kosten", "Cost", "Costes", "Couts")
_register("module.service_patterns", "Service & Wartungsmuster", "Service & Maintenance Patterns", "Patrones de servicio y mantenimiento", "Schemas de service et maintenance")
_register("module.brand_dna", "Marken-DNA", "Brand DNA", "ADN de marca", "ADN de marque")
_register("module.market", "Marktanalyse", "Market Analysis", "Analisis de mercado", "Analyse de marche")
_register("module.community", "Community-Intelligence", "Community Intelligence", "Inteligencia comunitaria", "Intelligence communautaire")

# ---- Confidence Levels ----
_register("confidence.measured", "Gemessen", "Measured", "Medido", "Mesure")
_register("confidence.calculated", "Berechnet", "Calculated", "Calculado", "Calcule")
_register("confidence.visual_high", "Visuell (hoch)", "Visual (high)", "Visual (alto)", "Visuel (eleve)")
_register("confidence.visual_medium", "Visuell (mittel)", "Visual (medium)", "Visual (medio)", "Visuel (moyen)")
_register("confidence.visual_low", "Visuell (niedrig)", "Visual (low)", "Visual (bajo)", "Visuel (faible)")
_register("confidence.visual_insufficient", "Visuell (unzureichend)", "Visual (insufficient)", "Visual (insuficiente)", "Visuel (insuffisant)")
_register("confidence.estimated", "Geschaetzt", "Estimated", "Estimado", "Estime")
_register("confidence.benchmark", "Benchmark", "Benchmark", "Referencia", "Reference")
_register("confidence.documented", "Dokumentiert", "Documented", "Documentado", "Documente")

# ---- Severity Levels ----
_register("severity.critical", "Kritisch", "Critical", "Critico", "Critique")
_register("severity.high", "Hoch", "High", "Alto", "Eleve")
_register("severity.medium", "Mittel", "Medium", "Medio", "Moyen")
_register("severity.low", "Niedrig", "Low", "Bajo", "Faible")
_register("severity.info", "Info", "Info", "Info", "Info")

# ---- Condition Ratings ----
_register("condition.excellent", "Ausgezeichnet", "Excellent", "Excelente", "Excellent")
_register("condition.good", "Gut", "Good", "Bueno", "Bon")
_register("condition.fair", "Befriedigend", "Fair", "Aceptable", "Passable")
_register("condition.poor", "Mangelhaft", "Poor", "Deficiente", "Mediocre")
_register("condition.critical", "Kritisch", "Critical", "Critico", "Critique")

# ---- Boat Classes ----
_register("boat_class.small_sail", "Kleine Segelyacht", "Small Sailboat", "Velero pequeno", "Petit voilier")
_register("boat_class.cruising_sail", "Fahrtensegler", "Cruising Sailboat", "Velero de crucero", "Voilier de croisiere")
_register("boat_class.performance_sail", "Performance-Segler", "Performance Sailboat", "Velero de regata", "Voilier de performance")
_register("boat_class.bluewater_sail", "Blauwasser-Segler", "Bluewater Cruiser", "Velero de altura", "Voilier hauturier")
_register("boat_class.catamaran_sail", "Segel-Katamaran", "Sailing Catamaran", "Catamaran de vela", "Catamaran a voile")
_register("boat_class.small_motor", "Kleines Motorboot", "Small Motorboat", "Lancha pequena", "Petit bateau a moteur")
_register("boat_class.cruising_motor", "Motorkreuzer", "Motor Cruiser", "Crucero a motor", "Vedette de croisiere")
_register("boat_class.large_motor", "Grosse Motoryacht", "Large Motor Yacht", "Yate a motor grande", "Grand yacht a moteur")
_register("boat_class.trawler", "Trawler", "Trawler", "Trawler", "Chalutier")
_register("boat_class.motorsailer", "Motorsailer", "Motorsailer", "Motovelero", "Motonautisme a voile")
_register("boat_class.catamaran_power", "Motor-Katamaran", "Power Catamaran", "Catamaran a motor", "Catamaran a moteur")
_register("boat_class.superyacht", "Superyacht", "Superyacht", "Superyate", "Superyacht")
_register("boat_class.dinghy", "Jolle / Dinghy", "Dinghy", "Bote / Dinghy", "Deriveur")

# ---- Units ----
_register("unit.mm", "mm", "mm", "mm", "mm")
_register("unit.m", "m", "m", "m", "m")
_register("unit.m2", "m\u00b2", "m\u00b2", "m\u00b2", "m\u00b2")
_register("unit.m3", "m\u00b3", "m\u00b3", "m\u00b3", "m\u00b3")
_register("unit.kg", "kg", "kg", "kg", "kg")
_register("unit.l", "Liter", "liters", "litros", "litres")
_register("unit.kn", "Knoten", "knots", "nudos", "noeuds")
_register("unit.kw", "kW", "kW", "kW", "kW")
_register("unit.hp", "PS", "HP", "CV", "CV")
_register("unit.nm", "Seemeilen", "nautical miles", "millas nauticas", "milles nautiques")
_register("unit.ft", "Fuss", "feet", "pies", "pieds")
_register("unit.inch", "Zoll", "inches", "pulgadas", "pouces")
_register("unit.lbs", "Pfund", "pounds", "libras", "livres")
_register("unit.gal", "Gallonen", "gallons", "galones", "gallons")
_register("unit.eur", "EUR", "EUR", "EUR", "EUR")
_register("unit.degrees", "Grad", "degrees", "grados", "degres")
_register("unit.percent", "Prozent", "percent", "por ciento", "pour cent")

# ---- Analysis Warnings / Findings (structural) ----
_register("finding.check_required", "Befund pruefen", "Finding requires review", "Hallazgo requiere revision", "Constat a verifier")
_register("finding.defect_confirmed", "Mangel bestaetigt", "Defect confirmed", "Defecto confirmado", "Defaut confirme")
_register("finding.osmosis_risk", "Osmoseverdacht im Unterwasserschiff", "Osmosis risk in underwater hull", "Riesgo de osmosis en obra viva", "Risque d'osmose sur la carene")
_register("finding.keel_bolt_check", "Kielbolzen-Pruefung empfohlen", "Keel bolt inspection recommended", "Inspeccion de pernos de quilla recomendada", "Inspection des boulons de quille recommandee")
_register("finding.gelcoat_damage", "Gelcoat-Schaeden festgestellt", "Gelcoat damage detected", "Danos en gelcoat detectados", "Dommages gelcoat detectes")
_register("finding.delamination_risk", "Delaminationsrisiko", "Delamination risk", "Riesgo de delaminacion", "Risque de delamination")
_register("finding.corrosion_detected", "Korrosion festgestellt", "Corrosion detected", "Corrosion detectada", "Corrosion detectee")
_register("finding.seal_replacement", "Dichtungstausch empfohlen", "Seal replacement recommended", "Reemplazo de juntas recomendado", "Remplacement des joints recommande")
_register("finding.wiring_issue", "Verkabelungsproblem erkannt", "Wiring issue detected", "Problema de cableado detectado", "Probleme de cablage detecte")
_register("finding.pump_wear", "Pumpenverschleiss festgestellt", "Pump wear detected", "Desgaste de bomba detectado", "Usure de pompe detectee")
_register("finding.teak_condition", "Teakdeck-Zustand bewerten", "Assess teak deck condition", "Evaluar estado de cubierta de teca", "Evaluer l'etat du pont en teck")
_register("finding.rigging_fatigue", "Rigg-Ermuedung moeglich", "Rigging fatigue possible", "Posible fatiga del aparejo", "Fatigue du greement possible")
_register("finding.engine_hours_high", "Hohe Motorstunden: {hours}h", "High engine hours: {hours}h", "Altas horas de motor: {hours}h", "Heures moteur elevees : {hours}h")

# ---- Analysis Suggestions ----
_register("suggestion.professional_inspection", "Professionelle Inspektion empfohlen", "Professional inspection recommended", "Inspeccion profesional recomendada", "Inspection professionnelle recommandee")
_register("suggestion.material_upgrade", "Material-Upgrade in Betracht ziehen: {material}", "Consider material upgrade: {material}", "Considerar mejora de material: {material}", "Envisager une amelioration du materiau : {material}")
_register("suggestion.maintenance_overdue", "Wartung ueberfaellig: {component} (letzter Service: {last_date})", "Maintenance overdue: {component} (last service: {last_date})", "Mantenimiento vencido: {component} (ultimo servicio: {last_date})", "Maintenance en retard : {component} (dernier entretien : {last_date})")
_register("suggestion.replace_component", "Komponente ersetzen: {component} (Alter: {age} Jahre)", "Replace component: {component} (age: {age} years)", "Reemplazar componente: {component} (edad: {age} anos)", "Remplacer le composant : {component} (age : {age} ans)")
_register("suggestion.alternative_available", "Alternative verfuegbar: {alternative} (Hersteller: {manufacturer})", "Alternative available: {alternative} (manufacturer: {manufacturer})", "Alternativa disponible: {alternative} (fabricante: {manufacturer})", "Alternative disponible : {alternative} (fabricant : {manufacturer})")

# ---- Compliance / Standards ----
_register("compliance.ce_category", "CE-Kategorie", "CE Category", "Categoria CE", "Categorie CE")
_register("compliance.ce_a_ocean", "Kategorie A — Hochsee", "Category A — Ocean", "Categoria A — Oceanica", "Categorie A — Hauturiere")
_register("compliance.ce_b_offshore", "Kategorie B — Kueste", "Category B — Offshore", "Categoria B — Costera", "Categorie B — Semi-hauturiere")
_register("compliance.ce_c_inshore", "Kategorie C — Kuechengewaesser", "Category C — Inshore", "Categoria C — Aguas costeras", "Categorie C — Cotiere")
_register("compliance.ce_d_sheltered", "Kategorie D — Geschuetzt", "Category D — Sheltered", "Categoria D — Protegida", "Categorie D — Eaux abritees")
_register("compliance.iso_reference", "ISO {standard} ({year}): {title}", "ISO {standard} ({year}): {title}", "ISO {standard} ({year}): {title}", "ISO {standard} ({year}) : {title}")
_register("compliance.escape_route_missing", "Fluchtweg fehlt in Zone {zone}", "Escape route missing in zone {zone}", "Ruta de escape faltante en zona {zone}", "Issue de secours manquante dans la zone {zone}")
_register("compliance.fire_safety_violation", "Brandschutzverstoesz in {zone}: {details}", "Fire safety violation in {zone}: {details}", "Violacion de seguridad contra incendios en {zone}: {details}", "Infraction securite incendie dans {zone} : {details}")
_register("compliance.railing_height_insufficient", "Relinghoehe unzureichend: {actual}mm (Minimum: {required}mm)", "Railing height insufficient: {actual}mm (minimum: {required}mm)", "Altura de barandilla insuficiente: {actual}mm (minimo: {required}mm)", "Hauteur de filiere insuffisante : {actual}mm (minimum : {required}mm)")

# ---- Structural Analysis ----
_register("structural.weight_balance", "Gewichtsverteilung", "Weight Distribution", "Distribucion de peso", "Repartition des masses")
_register("structural.cog_position", "Schwerpunktlage bei {position}", "Center of gravity at {position}", "Centro de gravedad en {position}", "Centre de gravite a {position}")
_register("structural.trim_angle", "Trimmwinkel: {angle} Grad", "Trim angle: {angle} degrees", "Angulo de trimado: {angle} grados", "Angle d'assiette : {angle} degres")
_register("structural.trim_warning", "Trimmwinkel ueberschreitet {max_deg} Grad fuer {boat_class}", "Trim angle exceeds {max_deg} degrees for {boat_class}", "Angulo de trimado excede {max_deg} grados para {boat_class}", "Angle d'assiette depasse {max_deg} degres pour {boat_class}")
_register("structural.hull_speed", "Rumpfgeschwindigkeit: {speed} kn", "Hull speed: {speed} kn", "Velocidad de casco: {speed} kn", "Vitesse de coque : {speed} kn")
_register("structural.stability_adequate", "Stabilitaet ausreichend", "Stability adequate", "Estabilidad adecuada", "Stabilite adequate")
_register("structural.stability_marginal", "Stabilitaet grenzwertig", "Stability marginal", "Estabilidad marginal", "Stabilite limite")
_register("structural.stability_insufficient", "Stabilitaet unzureichend", "Stability insufficient", "Estabilidad insuficiente", "Stabilite insuffisante")

# ---- Materials Analysis ----
_register("materials.lifecycle_cost", "20-Jahres-Lebenszykluskosten: {cost}", "20-year lifecycle cost: {cost}", "Costo de ciclo de vida de 20 anos: {cost}", "Cout du cycle de vie sur 20 ans : {cost}")
_register("materials.uv_risk", "UV-Risiko: {material} in Zone {zone} ohne UV-Schutz", "UV risk: {material} in zone {zone} without UV protection", "Riesgo UV: {material} en zona {zone} sin proteccion UV", "Risque UV : {material} dans la zone {zone} sans protection UV")
_register("materials.moisture_risk", "Feuchterisiko: {material} in Zone {zone} nicht versiegelt", "Moisture risk: {material} in zone {zone} not sealed", "Riesgo de humedad: {material} en zona {zone} sin sellar", "Risque d'humidite : {material} dans la zone {zone} non etanche")
_register("materials.compatibility_warning", "Material-Kompatibilitaet: {mat_a} und {mat_b} — galvanische Korrosionsgefahr", "Material compatibility: {mat_a} and {mat_b} — galvanic corrosion risk", "Compatibilidad de materiales: {mat_a} y {mat_b} — riesgo de corrosion galvanica", "Compatibilite des materiaux : {mat_a} et {mat_b} — risque de corrosion galvanique")

# ---- Cost Analysis ----
_register("cost.benchmark_comparison", "Benchmark: {actual} vs. Referenz {benchmark} ({boat_class})", "Benchmark: {actual} vs. reference {benchmark} ({boat_class})", "Referencia: {actual} vs. referencia {benchmark} ({boat_class})", "Reference : {actual} vs. reference {benchmark} ({boat_class})")
_register("cost.total_estimated", "Geschaetzte Gesamtkosten: {total}", "Estimated total cost: {total}", "Costo total estimado: {total}", "Cout total estime : {total}")
_register("cost.per_meter", "Kosten pro Meter: {cost_per_m}", "Cost per meter: {cost_per_m}", "Costo por metro: {cost_per_m}", "Cout par metre : {cost_per_m}")

# ---- Marine Terminology (frequently used in analysis output) ----
_register("marine.hull", "Rumpf", "Hull", "Casco", "Coque")
_register("marine.keel", "Kiel", "Keel", "Quilla", "Quille")
_register("marine.rudder", "Ruder", "Rudder", "Timon", "Safran")
_register("marine.mast", "Mast", "Mast", "Mastil", "Mat")
_register("marine.boom", "Baum", "Boom", "Botavara", "Bome")
_register("marine.shrouds", "Wanten", "Shrouds", "Obenques", "Haubans")
_register("marine.forestay", "Vorstag", "Forestay", "Estay de proa", "Etai")
_register("marine.backstay", "Achterstag", "Backstay", "Estay de popa", "Pataras")
_register("marine.winch", "Winsch", "Winch", "Winche", "Winch")
_register("marine.cleat", "Klampe", "Cleat", "Cornamusa", "Taquet")
_register("marine.anchor", "Anker", "Anchor", "Ancla", "Ancre")
_register("marine.mooring", "Festmacher", "Mooring line", "Amarra", "Amarre")
_register("marine.fender", "Fender", "Fender", "Defensa", "Pare-battage")
_register("marine.bilge", "Bilge", "Bilge", "Sentina", "Cale")
_register("marine.cockpit", "Cockpit", "Cockpit", "Banera", "Cockpit")
_register("marine.companionway", "Niedergang", "Companionway", "Tambucho", "Descente")
_register("marine.galley", "Pantry", "Galley", "Cocina", "Cuisine")
_register("marine.head", "Nasszelle", "Head", "Bano", "Salle d'eau")
_register("marine.berth", "Koje", "Berth", "Litera", "Couchette")
_register("marine.saloon", "Salon", "Saloon", "Salon", "Carre")
_register("marine.forepeak", "Vorpiek", "Forepeak", "Pique de proa", "Peak avant")
_register("marine.lazarette", "Lazarett / Achterpiek", "Lazarette", "Lazareto", "Coqueron arriere")
_register("marine.waterline", "Wasserlinie", "Waterline", "Linea de flotacion", "Ligne de flottaison")
_register("marine.freeboard", "Freibord", "Freeboard", "Francobordo", "Franc-bord")
_register("marine.draft", "Tiefgang", "Draft", "Calado", "Tirant d'eau")
_register("marine.beam", "Breite", "Beam", "Manga", "Bau")
_register("marine.loa", "Laenge ueber alles", "Length overall", "Eslora total", "Longueur hors tout")
_register("marine.lwl", "Wasserlinienlaenge", "Waterline length", "Eslora en flotacion", "Longueur a la flottaison")
_register("marine.displacement", "Verdraengung", "Displacement", "Desplazamiento", "Deplacement")
_register("marine.ballast", "Ballast", "Ballast", "Lastre", "Lest")
_register("marine.seacock", "Seeventil", "Seacock", "Grifo de fondo", "Vanne de coque")
_register("marine.through_hull", "Borddurchlass", "Through-hull fitting", "Pasacascos", "Passe-coque")
_register("marine.propeller", "Propeller", "Propeller", "Helice", "Helice")
_register("marine.saildrive", "Saildrive", "Saildrive", "Saildrive", "Saildrive")
_register("marine.shaft", "Welle", "Shaft", "Eje", "Arbre")
_register("marine.gearbox", "Getriebe", "Gearbox", "Caja reductora", "Inverseur")
_register("marine.zinc_anode", "Zinkanode", "Zinc anode", "Anodo de zinc", "Anode de zinc")
_register("marine.antifouling", "Antifouling", "Antifouling", "Antifouling", "Antifouling")
_register("marine.epirb", "EPIRB", "EPIRB", "EPIRB", "EPIRB")
_register("marine.ais", "AIS", "AIS", "AIS", "AIS")
_register("marine.vhf", "UKW-Funk", "VHF Radio", "Radio VHF", "Radio VHF")
_register("marine.chart_plotter", "Kartenplotter", "Chart Plotter", "Plotter de cartas", "Traceur de cartes")
_register("marine.autopilot", "Autopilot", "Autopilot", "Piloto automatico", "Pilote automatique")
_register("marine.radar", "Radar", "Radar", "Radar", "Radar")
_register("marine.depth_sounder", "Echolot", "Depth Sounder", "Sonda", "Sondeur")
_register("marine.wind_instrument", "Windmesser", "Wind Instrument", "Anemometro", "Anemometre")
_register("marine.nmea2000", "NMEA 2000", "NMEA 2000", "NMEA 2000", "NMEA 2000")

# ---- Report / UI Labels ----
_register("report.full_analysis", "Vollanalyse", "Full Analysis", "Analisis completo", "Analyse complete")
_register("report.quick_analysis", "Schnellanalyse", "Quick Analysis", "Analisis rapido", "Analyse rapide")
_register("report.summary", "Zusammenfassung", "Summary", "Resumen", "Resume")
_register("report.details", "Details", "Details", "Detalles", "Details")
_register("report.findings", "Befunde", "Findings", "Hallazgos", "Constats")
_register("report.suggestions", "Empfehlungen", "Suggestions", "Recomendaciones", "Recommandations")
_register("report.warnings", "Warnungen", "Warnings", "Advertencias", "Avertissements")
_register("report.score_overview", "Bewertungsuebersicht", "Score Overview", "Resumen de puntuaciones", "Apercu des scores")
_register("report.generated_at", "Erstellt am {date}", "Generated on {date}", "Generado el {date}", "Genere le {date}")
_register("report.data_level", "Datenniveau: {level}", "Data level: {level}", "Nivel de datos: {level}", "Niveau de donnees : {level}")
_register("report.level_1", "Level 1 — Schnellanalyse (geschaetzt)", "Level 1 — Quick Analysis (estimated)", "Nivel 1 — Analisis rapido (estimado)", "Niveau 1 — Analyse rapide (estime)")
_register("report.level_2", "Level 2 — Profi-Werkzeug (gemessen)", "Level 2 — Professional Tool (measured)", "Nivel 2 — Herramienta profesional (medido)", "Niveau 2 — Outil professionnel (mesure)")

# ---- Value with unit (generic pattern) ----
_register("format.value_unit", "{value} {unit}", "{value} {unit}", "{value} {unit}", "{value} {unit}")
_register("format.range", "{min} bis {max} {unit}", "{min} to {max} {unit}", "{min} a {max} {unit}", "{min} a {max} {unit}")
_register("format.approx", "ca. {value} {unit}", "approx. {value} {unit}", "aprox. {value} {unit}", "env. {value} {unit}")
_register("format.min_required", "Mindestens {value} {unit} erforderlich", "Minimum {value} {unit} required", "Se requiere al menos {value} {unit}", "Minimum {value} {unit} requis")
_register("format.max_allowed", "Maximal {value} {unit} zulaessig", "Maximum {value} {unit} allowed", "Maximo {value} {unit} permitido", "Maximum {value} {unit} autorise")
