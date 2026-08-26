"""Input validation framework for AYDI.

Provides defensive validation at module boundaries.
Every module validates its own input — never trust upstream data blindly.

Usage:
    from app.core.validation import validate_zones, validate_boat_class, validate_positive

    # At module entry:
    validated_zones = validate_zones(zones)
    validated_class = validate_boat_class(boat_class)
"""

from __future__ import annotations

import logging
import math
from typing import Any, TypeVar

from app.core.errors import DataValidationError

logger = logging.getLogger(__name__)

T = TypeVar("T")

# ---------------------------------------------------------------------------
# Known enums (prevent string typos)
# ---------------------------------------------------------------------------

# Einzelquelle: das BoatClass-Enum. Die Liste war zuvor von Hand gepflegt und
# gegenüber dem Enum verrutscht — fünf der dreizehn offiziellen Klassen
# (racing_sail, daysailer, catamaran_motor, sport_cruiser, explorer) wurden von
# der Validierung ABGELEHNT, obwohl das Frontend sie zur Auswahl anbietet und die
# Analysemodule BOAT_CLASS_DEFAULTS für sie führen. Gleichzeitig galten fünf
# längst umbenannte Namen weiter als gültig. Ableiten statt duplizieren schließt
# diese Fehlerquelle dauerhaft.
#
# Import-Richtung ist unkritisch: app/schemas/schemas.py importiert nichts aus
# app/core, es entsteht also kein Zyklus.
from app.schemas.schemas import BoatClass as _BoatClass  # noqa: E402

VALID_BOAT_CLASSES = frozenset(bc.value for bc in _BoatClass)

# Zurückgezogene Klassennamen früherer Fassungen → kanonischer Wert.
# Sie können noch in gespeicherten Level-1-Schnellanalysen stehen, die
# `boat_class` als freien String annehmen.
BOAT_CLASS_ALIASES = {
    # Reine Umbenennungen (identische Bezeichnung im i18n-Katalog):
    "catamaran_power": "catamaran_motor",
    # Fachlich eindeutige Zuordnungen:
    "performance_sail": "racing_sail",      # Performance-Segler → Regattasegler
    "bluewater_sail": "cruising_sail",      # Blauwasser-Segler ist ein Fahrtensegler
    # Näherungen für zurückgezogene Sammelbegriffe — bewusst als solche markiert,
    # damit niemand sie für exakte Umbenennungen hält:
    "dinghy": "daysailer",                  # Jolle: kleines, offenes Tagesboot
    "cruising_motor": "small_motor",        # Motorkreuzer: Kajütboot ohne Sportanspruch
}


def normalize_boat_class(boat_class: str) -> str:
    """Zieht einen zurückgezogenen Klassennamen auf den kanonischen Wert.

    Unbekanntes kommt unverändert (getrimmt/lowercased) zurück, damit der
    Aufrufer noch ablehnen oder warnen kann.
    """
    if not isinstance(boat_class, str):
        return boat_class
    normalized = boat_class.strip().lower()
    return BOAT_CLASS_ALIASES.get(normalized, normalized)

VALID_ZONE_TYPES = frozenset({
    # Interior
    "cabin", "saloon", "pantry", "head", "storage", "forepeak",
    "aft_cabin", "quarter_berth", "workshop",
    # Deck
    "cockpit", "foredeck", "side_deck", "flybridge", "swim_platform",
    # Engine/Systems
    "engine", "engine_room", "fuel_tank", "shaft_tunnel",
    "electrical_panel", "battery_compartment", "nav_station",
    "water_tank", "holding_tank", "shower",
    # Structure
    "hull", "keel", "rudder", "bulkhead", "frame", "transom",
    # Rigging
    "mast", "rigging", "deck_hardware", "sail_storage",
    # Safety
    "safety_locker", "liferaft_storage", "fire_station",
    # Helm
    "helm", "flybridge_helm",
    # Electrical
    "charger_area",
    # Maintenance / service
    "boatyard", "maintenance_hatch", "service_area",
    # Generic
    "crew_area", "guest_area", "technical", "void",
})

# Gebräuchliche Synonyme → kanonischer Zonentyp.
#
# Warum das nötig ist: Ein unbekannter Zonentyp wurde bisher nur geloggt und
# unverändert weitergereicht. `get_domain_for_zone_type()` liefert dafür None,
# die Zone fällt also still aus der Domänen-Abdeckung heraus — das Ergebnis wirkt
# vollständig, ist es aber nicht. Betroffen sind ausgerechnet naheliegende
# Eingaben: "galley" ist der englische Standardbegriff für die Bordküche
# (kanonisch heißt sie hier "pantry"), und eine deutschsprachige Oberfläche
# liefert plausibel "kombuese" oder "nasszelle".
ZONE_TYPE_ALIASES = {
    # Bordküche
    "galley": "pantry",
    "kitchen": "pantry",
    "kombuese": "pantry",
    "kombüse": "pantry",
    "kueche": "pantry",
    "küche": "pantry",
    # Nasszelle
    "wc": "head",
    "toilet": "head",
    "toilette": "head",
    "bathroom": "head",
    "nasszelle": "head",
    "bad": "head",
    "shower_room": "shower",
    # Wohnbereich
    "salon": "saloon",
    "main_cabin": "saloon",
    "kabine": "cabin",
    "master_cabin": "cabin",
    "owner_cabin": "cabin",
    "v_berth": "forepeak",
    "vberth": "forepeak",
    "vorschiff": "forepeak",
    "achterkabine": "aft_cabin",
    # Stauraum
    "locker": "storage",
    "lazarette": "storage",
    "cockpit_locker": "storage",
    "stowage": "storage",
    "stauraum": "storage",
    # Maschine
    "engine_bay": "engine_room",
    "motor_room": "engine_room",
    "maschinenraum": "engine_room",
    # Navigation / Steuerstand
    "chart_table": "nav_station",
    "kartentisch": "nav_station",
    "helm_station": "helm",
    "steering_position": "helm",
    # Deck
    "swim_step": "swim_platform",
    "bathing_platform": "swim_platform",
    "badeplattform": "swim_platform",
}


def passage_width(passage: dict) -> float | None:
    """Die Durchgangsbreite in mm — oder ``None``, wenn sie nicht bekannt ist.

    Ein aus DXF importierter Durchgang hat keine ableitbare Breite (siehe
    ``services/dxf/parser.py::_detect_shared_edges``); dort steht bewusst
    ``None`` statt einer erfundenen Zahl. Jeder Konsument muss diesen Fall
    behandeln, statt ihn wie eine gemessene 0 zu behandeln.
    """
    width = passage.get("width_mm") if isinstance(passage, dict) else None
    if width is None or isinstance(width, bool) or not isinstance(width, (int, float)):
        return None
    if not math.isfinite(width):
        return None
    return float(width)


def known_passage_widths(passages: list[dict] | None) -> list[float]:
    """Alle bekannten, endlichen Durchgangsbreiten — unbekannte fallen heraus."""
    if not passages:
        return []
    widths = [passage_width(p) for p in passages]
    return [w for w in widths if w is not None]


def normalize_zone_type(zone_type: str) -> str:
    """Map a zone-type synonym onto its canonical value.

    Unknown values are returned unchanged (lower-cased/trimmed) so the caller can
    still warn about them.
    """
    if not isinstance(zone_type, str):
        return zone_type
    normalized = zone_type.strip().lower()
    return ZONE_TYPE_ALIASES.get(normalized, normalized)

VALID_CONFIDENCE_LEVELS = frozenset({
    "measured", "calculated", "visual_high", "visual_medium",
    "visual_low", "visual_insufficient", "estimated", "benchmark", "documented",
})

VALID_SEVERITY_LEVELS = frozenset({
    "critical", "high", "medium", "low", "info",
})


# ---------------------------------------------------------------------------
# Primitive validators
# ---------------------------------------------------------------------------

def validate_positive(
    value: float | int | None,
    field_name: str,
    *,
    allow_zero: bool = False,
    allow_none: bool = False,
    max_value: float | None = None,
) -> float | None:
    """Validate that a numeric value is positive (and finite).

    Returns the validated value or raises DataValidationError.
    """
    if value is None:
        if allow_none:
            return None
        raise DataValidationError(f"{field_name}: value is required (got None)")

    if not isinstance(value, (int, float)):
        raise DataValidationError(f"{field_name}: expected number, got {type(value).__name__}")

    if not math.isfinite(value):
        raise DataValidationError(f"{field_name}: value must be finite, got {value}")

    if allow_zero:
        if value < 0:
            raise DataValidationError(f"{field_name}: must be >= 0, got {value}")
    else:
        if value <= 0:
            raise DataValidationError(f"{field_name}: must be > 0, got {value}")

    if max_value is not None and value > max_value:
        raise DataValidationError(f"{field_name}: must be <= {max_value}, got {value}")

    return float(value)


def validate_in_range(
    value: float | int,
    field_name: str,
    min_val: float,
    max_val: float,
) -> float:
    """Validate that a value falls within [min_val, max_val]."""
    if not isinstance(value, (int, float)):
        raise DataValidationError(f"{field_name}: expected number, got {type(value).__name__}")
    if not math.isfinite(value):
        raise DataValidationError(f"{field_name}: must be finite, got {value}")
    if value < min_val or value > max_val:
        raise DataValidationError(
            f"{field_name}: must be in [{min_val}, {max_val}], got {value}"
        )
    return float(value)


def validate_non_empty_string(
    value: str | None,
    field_name: str,
    *,
    allow_none: bool = False,
    max_length: int = 500,
) -> str | None:
    """Validate that a string is non-empty and within length limits."""
    if value is None:
        if allow_none:
            return None
        raise DataValidationError(f"{field_name}: string value is required")
    if not isinstance(value, str):
        raise DataValidationError(f"{field_name}: expected string, got {type(value).__name__}")
    stripped = value.strip()
    if not stripped:
        raise DataValidationError(f"{field_name}: string must not be empty")
    if len(stripped) > max_length:
        raise DataValidationError(f"{field_name}: string too long ({len(stripped)} > {max_length})")
    return stripped


def validate_enum(
    value: str | None,
    field_name: str,
    valid_values: frozenset[str],
    *,
    allow_none: bool = False,
) -> str | None:
    """Validate that a string is one of the allowed values."""
    if value is None:
        if allow_none:
            return None
        raise DataValidationError(f"{field_name}: value is required")
    if not isinstance(value, str):
        raise DataValidationError(f"{field_name}: expected string, got {type(value).__name__}")
    normalized = value.strip().lower()
    if normalized not in valid_values:
        raise DataValidationError(
            f"{field_name}: '{normalized}' is not valid. "
            f"Allowed: {sorted(valid_values)[:10]}{'...' if len(valid_values) > 10 else ''}"
        )
    return normalized


# ---------------------------------------------------------------------------
# Domain validators
# ---------------------------------------------------------------------------

def validate_boat_class(boat_class: str | None) -> str:
    """Validate boat class string against known classes.

    Returns normalized boat class or raises DataValidationError.
    """
    # Erst den Alias auflösen, dann prüfen — sonst scheitert ein gespeicherter
    # Altname an einer Liste, die ihn nur unter neuem Namen kennt.
    candidate = normalize_boat_class(boat_class) if isinstance(boat_class, str) else boat_class
    result = validate_enum(candidate, "boat_class", VALID_BOAT_CLASSES)
    assert result is not None  # validate_enum with allow_none=False
    return result


def validate_zone(zone: dict, index: int = 0) -> dict:
    """Validate a single zone dict at module boundary.

    Checks required fields, types, and ranges. Returns the zone
    with any fixes applied (e.g., missing optional fields get defaults).
    """
    if not isinstance(zone, dict):
        raise DataValidationError(f"Zone[{index}]: expected dict, got {type(zone).__name__}")

    # Name or ID required
    name = zone.get("name") or zone.get("id") or f"zone_{index}"

    # Zone type — Synonyme auf den kanonischen Wert ziehen, Unbekanntes nur
    # melden (nicht ablehnen). Der normalisierte Wert wird ZURÜCKGESCHRIEBEN,
    # sonst verliert die Zone ihre Domänenzuordnung.
    raw_zone_type = zone.get("zone_type") or zone.get("type", "")
    zone_type = normalize_zone_type(raw_zone_type)
    if zone_type and isinstance(raw_zone_type, str) and zone_type != raw_zone_type.strip().lower():
        logger.debug(
            "Zone type '%s' normalised to '%s' in zone '%s'", raw_zone_type, zone_type, name
        )
    if zone_type:
        if "zone_type" in zone:
            zone["zone_type"] = zone_type
        elif "type" in zone:
            zone["type"] = zone_type
    if zone_type and zone_type not in VALID_ZONE_TYPES:
        logger.warning("Unknown zone type '%s' in zone '%s'", zone_type, name)

    # Polygon validation
    polygon = zone.get("polygon", [])
    if polygon and isinstance(polygon, list):
        if len(polygon) < 3:
            logger.warning("Zone '%s' has polygon with < 3 points", name)

    # Area validation
    area = zone.get("area_m2") or zone.get("area")
    if area is not None:
        if isinstance(area, (int, float)) and (not math.isfinite(area) or area < 0):
            logger.warning("Zone '%s' has invalid area: %s", name, area)
            area = None

    # Height validation
    height = zone.get("height_mm")
    if height is not None:
        if isinstance(height, (int, float)):
            if height < 0 or height > 10000:
                logger.warning("Zone '%s' has implausible height: %s mm", name, height)

    return zone  # Return as-is but after validation logging


def validate_zones(zones: list[dict] | None) -> list[dict]:
    """Validate a list of zones. Returns validated list (may be empty)."""
    if zones is None:
        return []
    if not isinstance(zones, list):
        raise DataValidationError(f"Zones: expected list, got {type(zones).__name__}")
    return [validate_zone(z, i) for i, z in enumerate(zones)]


def validate_passages(passages: list[dict] | None) -> list[dict]:
    """Validate a list of passages. Returns validated list."""
    if passages is None:
        return []
    if not isinstance(passages, list):
        raise DataValidationError(f"Passages: expected list, got {type(passages).__name__}")

    validated = []
    for i, p in enumerate(passages):
        if not isinstance(p, dict):
            raise DataValidationError(f"Passage[{i}]: expected dict, got {type(p).__name__}")

        width = p.get("width_mm")
        if width is not None and isinstance(width, (int, float)):
            if not math.isfinite(width) or width < 0:
                logger.warning("Passage[%d] has invalid width: %s", i, width)
            elif width > 5000:
                logger.warning("Passage[%d] has implausibly large width: %s mm", i, width)

        validated.append(p)
    return validated


def validate_year(
    year: int | None,
    field_name: str,
    *,
    allow_none: bool = False,
    min_year: int = 1800,
    max_year: int = 2030,
) -> int | None:
    """Validate a year value (e.g., build year, install year)."""
    if year is None:
        if allow_none:
            return None
        raise DataValidationError(f"{field_name}: year is required")
    if not isinstance(year, int):
        raise DataValidationError(f"{field_name}: expected int, got {type(year).__name__}")
    if year < min_year or year > max_year:
        raise DataValidationError(
            f"{field_name}: year {year} out of range [{min_year}, {max_year}]"
        )
    return year


def validate_install_year(
    install_year: int | None,
    field_name: str = "install_year",
    *,
    current_year: int = 2026,
) -> int | None:
    """Validate install year — must not be in the future."""
    if install_year is None:
        return None
    if not isinstance(install_year, int):
        raise DataValidationError(f"{field_name}: expected int, got {type(install_year).__name__}")
    if install_year > current_year:
        raise DataValidationError(
            f"{field_name}: year {install_year} is in the future (current: {current_year})"
        )
    if install_year < 1800:
        raise DataValidationError(f"{field_name}: year {install_year} is implausibly old")
    return install_year


# ---------------------------------------------------------------------------
# Analysis result validators (for module output)
# ---------------------------------------------------------------------------

def validate_score(score: float | None, module_name: str = "") -> float | None:
    """Validate an analysis score (0-100 scale)."""
    if score is None:
        return None
    if not isinstance(score, (int, float)):
        logger.warning("Module %s: score is not numeric: %s", module_name, score)
        return None
    if not math.isfinite(score):
        logger.warning("Module %s: score is not finite: %s", module_name, score)
        return None
    # Clamp to valid range rather than reject
    return max(0.0, min(100.0, float(score)))


def validate_confidence(confidence: str | None) -> str:
    """Validate confidence level string."""
    if confidence is None:
        return "estimated"
    if isinstance(confidence, str) and confidence.lower() in VALID_CONFIDENCE_LEVELS:
        return confidence.lower()
    logger.warning("Unknown confidence level: %s, defaulting to 'estimated'", confidence)
    return "estimated"


def validate_severity(severity: str | None) -> str:
    """Validate severity level string."""
    if severity is None:
        return "info"
    if isinstance(severity, str) and severity.lower() in VALID_SEVERITY_LEVELS:
        return severity.lower()
    logger.warning("Unknown severity level: %s, defaulting to 'info'", severity)
    return "info"
