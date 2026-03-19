"""Exterior assessment prompt for yacht photos."""

BOAT_CLASS_CONTEXT = {
    "small_sail": "Kleine Segelyacht (8-12m). Funktionale Linien, Segelleistung steht im Vordergrund. Saubere Ausfuehrung wichtiger als Designinnovation.",
    "cruising_sail": "Fahrtensegelyacht (12-18m). Elegante Segellinien, harmonisches Verhaeltnis von Aufbau zu Rumpf. Gute Balance zwischen Segeleigenschaften und Komfortvolumen.",
    "large_motor": "Grosse Motoryacht (18-30m). Repraesentatives Erscheinungsbild. Ausgewogene Proportionen, elegante Linien, hochwertiger Oberflaecheneindruck.",
    "superyacht": "Superyacht (30m+). Ikonisches Design. Einzigartige Designsprache, makellose Ausfuehrung, unverwechselbare Silhouette.",
}


def get_exterior_assessment_prompt(
    boat_class: str,
    zone_type: str | None = None,
    context: dict | None = None,
) -> str:
    """Generate the exterior assessment prompt for Claude vision API.

    Args:
        boat_class: One of small_sail, cruising_sail, large_motor, superyacht.
        zone_type: Optional zone type for context.
        context: Optional additional context dict.

    Returns:
        German-language prompt string requesting JSON output.
    """
    class_desc = BOAT_CLASS_CONTEXT.get(boat_class, BOAT_CLASS_CONTEXT["cruising_sail"])

    extra = ""
    if context:
        if "length_m" in context:
            extra += f"\nBootslaenge: {context['length_m']}m."

    return f"""Du bist ein erfahrener Yachtdesigner mit besonderem Augenmerk auf Exterieur-Design und Proportionslehre. Du erkennst gute Linien, harmonische Verhaeltnisse und handwerkliche Qualitaet auf den ersten Blick. Analysiere dieses Bild.

Bootsklasse: {class_desc}{extra}

Bewerte folgende Aspekte des Exterieurs, soweit im Bild erkennbar:

1. **Linienharmonie**: Rumpflinien, Aufbaulinien, Fensterband, Uebergaenge
2. **Proportionen**: Verhaeltnis Aufbau/Rumpf, Bug/Heck-Balance, Fenstergrösse zu Wandflaeche
3. **Oberflaechenqualitaet**: Lack/Gelcoat-Zustand, Reflexionen, sichtbare Maengel
4. **Hardware**: Relingqualitaet, Beschlaege, Fender, Ankeranlage
5. **Markenkonsistenz**: Designsprache, Wiedererkennbarkeit, Stilsicherheit

WICHTIG: Wenn etwas nicht erkennbar ist, sage das explizit mit "nicht beurteilbar". Bewerte Wetter- und Lichtverhaeltnisse im Foto mit ein — ein Bild bei schlechtem Licht erlaubt weniger Detailbewertung.

Antworte ausschliesslich mit einem JSON-Objekt (kein zusaetzlicher Text):

{{
    "exterior_score": <float 0-100>,
    "assessable": <bool>,
    "line_harmony": {{
        "hull_lines": "<fliessend/harmonisch/unruhig/nicht beurteilbar>",
        "superstructure": "<integriert/akzeptabel/aufgesetzt/nicht beurteilbar>",
        "transitions": "<nahtlos/sauber/abrupt/nicht beurteilbar>",
        "assessment": "<string>"
    }},
    "proportions": {{
        "superstructure_ratio": "<ausgewogen/etwas hoch/zu massig/nicht beurteilbar>",
        "bow_stern_balance": "<harmonisch/buglastig/hecklastig/nicht beurteilbar>",
        "window_ratio": "<elegant/angemessen/zu klein/zu gross/nicht beurteilbar>",
        "assessment": "<string>"
    }},
    "surface_quality": {{
        "paint_gelcoat": "<makellos/gut/Gebrauchsspuren/beschaedigt/nicht beurteilbar>",
        "reflections": "<spiegelnd/gut/matt/stumpf/nicht beurteilbar>",
        "defects_visible": ["<string>", ...],
        "assessment": "<string>"
    }},
    "hardware": {{
        "railing_quality": "<hochwertig/solide/einfach/mangelhaft/nicht beurteilbar>",
        "fittings": "<premium/gut/funktional/billig/nicht beurteilbar>",
        "observations": ["<string>", ...]
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
