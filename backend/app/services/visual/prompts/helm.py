"""Helm station ergonomics prompt for yacht photos."""

BOAT_CLASS_CONTEXT = {
    "small_sail": "Kleine Segelyacht (8-12m). Kompakter Steuerstand, oft im Cockpit integriert. Wenige Instrumente, direktes Steuern. Ueberblick und Handhabung wichtig.",
    "cruising_sail": "Fahrtensegelyacht (12-18m). Gut organisierter Steuerstand mit Kartenplotter, Instrumenten, Winschenkontrollen. Ergonomie fuer Langfahrt wichtig.",
    "large_motor": "Grosse Motoryacht (18-30m). Professioneller Steuerstand mit umfangreicher Elektronik. Gute Sicht, logische Instrumentenanordnung, Komfort fuer laengeres Steuern.",
    "superyacht": "Superyacht (30m+). Bruecke mit professionellem Anspruch. Volle Instrumentierung, redundante Systeme, 360-Grad-Sicht, ergonomischer Kapitaensplatz.",
}


def get_helm_ergonomics_prompt(
    boat_class: str,
    zone_type: str | None = None,
    context: dict | None = None,
) -> str:
    """Generate the helm ergonomics prompt for Claude vision API.

    Args:
        boat_class: One of small_sail, cruising_sail, large_motor, superyacht.
        zone_type: Optional zone type for context.
        context: Optional additional context dict.

    Returns:
        German-language prompt string requesting JSON output.
    """
    class_desc = BOAT_CLASS_CONTEXT.get(boat_class, BOAT_CLASS_CONTEXT["cruising_sail"])

    return f"""Du bist ein erfahrener Yachtkapitaen und Steuerstand-Ergonomie-Experte. Du hast hunderte Steuerstdaende verschiedener Yachten bewertet und weisst, was einen guten Arbeitsplatz am Steuer ausmacht. Analysiere dieses Bild.

Bootsklasse: {class_desc}

Bewerte den Steuerstand nach folgenden Kriterien, soweit im Bild erkennbar:

1. **Instrumentenlayout**: Logische Anordnung, Gruppierung zusammengehoeriger Instrumente, Ablesewinkel, Blendfreiheit
2. **Sicht**: Voraus-Sicht, Sicht zu den Seiten, Sicht nach achtern, tote Winkel durch Aufbauten
3. **Ergonomie**: Sitzposition, Greifdistanzen, Steuerrad-/Pinnnenposition, Ablagen fuer Getraenke/Karten
4. **Informationshierarchie**: Sind die wichtigsten Instrumente (Geschwindigkeit, Tiefe, Navigation) am besten sichtbar? Sekundaere Informationen im Hintergrund?

WICHTIG: Wenn etwas nicht erkennbar ist, sage das explizit mit "nicht beurteilbar". Bewerte die Instrumente nicht nach Marke oder Alter, sondern nach Anordnung und Ergonomie.

Antworte ausschliesslich mit einem JSON-Objekt (kein zusaetzlicher Text):

{{
    "helm_score": <float 0-100>,
    "assessable": <bool>,
    "visibility": {{
        "forward": "<hervorragend/gut/eingeschraenkt/schlecht/nicht beurteilbar>",
        "lateral": "<gut/akzeptabel/eingeschraenkt/nicht beurteilbar>",
        "aft": "<gut/akzeptabel/eingeschraenkt/nicht beurteilbar>",
        "blind_spots": ["<string>", ...],
        "assessment": "<string>"
    }},
    "instrument_layout": {{
        "logical_grouping": "<durchdacht/akzeptabel/unstrukturiert/nicht beurteilbar>",
        "readability": "<hervorragend/gut/schwierig/nicht beurteilbar>",
        "glare_protection": "<vorhanden/teilweise/fehlend/nicht beurteilbar>",
        "instruments_identified": ["<string>", ...],
        "assessment": "<string>"
    }},
    "ergonomics": {{
        "seating": "<ergonomisch/akzeptabel/unbequem/nicht beurteilbar>",
        "reach_distances": "<optimal/akzeptabel/zu weit/nicht beurteilbar>",
        "wheel_position": "<gut/akzeptabel/ungeuenstig/nicht beurteilbar>",
        "storage_at_helm": "<ausreichend/knapp/fehlend/nicht beurteilbar>",
        "assessment": "<string>"
    }},
    "information_hierarchy": {{
        "primary_instruments_prominent": <bool oder null>,
        "secondary_instruments_background": <bool oder null>,
        "assessment": "<string>"
    }},
    "findings": [
        {{
            "aspect": "<string>",
            "observation": "<string>",
            "rating": "<positiv/neutral/negativ>",
            "suggestion": "<string oder null>"
        }}
    ],
    "confidence": "<hoch/mittel/niedrig>",
    "cannot_assess": ["<string>", ...]
}}"""
