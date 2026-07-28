"""Central registry of the 13 supported boat classes.

Single source of truth for:
  * which class keys are accepted at all (input validation), and
  * the German label shown to users.

Before this module existed, German labels were defined twice — in
``quick_analysis.py`` and in ``reports/pdf_generator.py`` — and both maps
covered only 4 of the 13 classes, so nine classes leaked their raw English
enum key into German user-facing prose. The frontend already had all 13
German names in its project-create form; this brings the backend in line.
"""

# Ordered as the frontend project-create form presents them.
BOAT_CLASS_LABELS: dict[str, str] = {
    "small_sail": "Kleine Segelyacht",
    "cruising_sail": "Fahrtensegler",
    "racing_sail": "Regattayacht",
    "daysailer": "Daysailer",
    "motorsailer": "Motorsailer",
    "catamaran_sail": "Segel-Katamaran",
    "catamaran_motor": "Motor-Katamaran",
    "small_motor": "Kleine Motoryacht",
    "large_motor": "Große Motoryacht",
    "sport_cruiser": "Sport Cruiser",
    "trawler": "Trawler",
    "explorer": "Explorer",
    "superyacht": "Superyacht",
}

BOAT_CLASSES: tuple[str, ...] = tuple(BOAT_CLASS_LABELS)


def label_for(boat_class: str) -> str:
    """German label for a class key, falling back to the key itself.

    The fallback should never be reached for validated input — it exists so
    that historical rows with a class key no longer in the registry still
    render something rather than raising.
    """
    return BOAT_CLASS_LABELS.get(boat_class, boat_class)


def is_known(boat_class: str) -> bool:
    return boat_class in BOAT_CLASS_LABELS
