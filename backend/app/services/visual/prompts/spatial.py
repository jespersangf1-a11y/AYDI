"""Spatial analysis prompt for yacht interior/exterior photos."""

BOAT_CLASS_CONTEXT = {
    "small_sail": "Kleine Segelyacht (8-12m). Jeder Zentimeter zaehlt. Kompakte Raeume sind normal und akzeptabel. Bewerte nach Funktionalitaet, nicht nach Grosszuegigkeit.",
    "cruising_sail": "Fahrtensegelyacht (12-18m). Balance zwischen Funktion und Komfort. Moderate Raumgroessen erwartet. Ergonomie und Stauraumnutzung sind wichtig.",
    "large_motor": "Grosse Motoryacht (18-30m). Komfort und Luxus werden erwartet. Grosszuegige Raeume, klare Zonierung, Privatshaere zwischen Gaesten und Crew.",
    "superyacht": "Superyacht (30m+). Hoechste Ansprueche an Raumgestaltung. Architektonische Qualitaet, kuratierte Sichtachsen, dramaturgischer Raumfluss.",
}


def get_spatial_analysis_prompt(
    boat_class: str,
    zone_type: str | None = None,
    context: dict | None = None,
) -> str:
    """Generate the spatial analysis prompt for Claude vision API.

    Args:
        boat_class: One of small_sail, cruising_sail, large_motor, superyacht.
        zone_type: Optional zone type (e.g. 'salon', 'cabin') for focused analysis.
        context: Optional additional context dict.

    Returns:
        German-language prompt string requesting JSON output.
    """
    class_desc = BOAT_CLASS_CONTEXT.get(boat_class, BOAT_CLASS_CONTEXT["cruising_sail"])

    zone_instruction = ""
    if zone_type:
        zone_labels = {
            "salon": "Salon (Hauptwohnbereich)",
            "cabin": "Kabine (Schlafbereich)",
            "pantry": "Pantry (Kuechenbereich)",
            "head": "Nasszelle (Bad/WC)",
            "cockpit": "Cockpit (Aussenbereich)",
            "helm": "Steuerstand",
            "engine": "Maschinenraum",
        }
        label = zone_labels.get(zone_type, zone_type)
        zone_instruction = f"\nDieses Bild zeigt speziell: {label}. Bewerte mit Fokus auf die typischen Anforderungen dieses Raumtyps."

    extra_context = ""
    if context:
        if "length_m" in context:
            extra_context += f"\nBootslaenge: {context['length_m']}m."
        if "beam_m" in context:
            extra_context += f"\nBootsbreite: {context['beam_m']}m."

    return f"""Du bist ein erfahrener Yachtdesigner und Raumplaner mit ueber 20 Jahren Erfahrung im Yachtbau. Analysiere dieses Bild einer Yacht.

Bootsklasse: {class_desc}{extra_context}{zone_instruction}

Bewerte folgende Aspekte basierend auf dem, was du im Bild erkennen kannst:

1. **Raumproportionen**: Verhaeltnis von Hoehe zu Breite, Raumwirkung
2. **Ergonomie**: Bewegungsfreiheit, Durchgangsbreiten (soweit erkennbar)
3. **Stauraum**: Sichtbare Stauraumloesungen, Effizienz der Raumnutzung
4. **Geschaetzte Abmessungen**: Schaetze sichtbare Masse (Durchgangsbreiten, Deckenhoehe, Raumtiefe) relativ zu erkennbaren Referenzobjekten

WICHTIG: Wenn etwas nicht erkennbar ist, sage das explizit mit "nicht beurteilbar". Erfinde keine Werte. Sei ehrlich ueber die Grenzen dessen, was aus einem Foto abgeleitet werden kann.

Antworte ausschliesslich mit einem JSON-Objekt in folgendem Format (kein zusaetzlicher Text):

{{
    "spatial_score": <float 0-100>,
    "assessable": <bool>,
    "estimated_dimensions": {{
        "ceiling_height_mm": <int oder null>,
        "room_width_mm": <int oder null>,
        "passage_width_mm": <int oder null>,
        "notes": "<string: Erklaerung der Schaetzgrundlage>"
    }},
    "ergonomics": {{
        "movement_freedom": "<gut/eingeschraenkt/beengt/nicht beurteilbar>",
        "passage_assessment": "<string>",
        "seating_comfort": "<string oder nicht beurteilbar>"
    }},
    "storage_visible": {{
        "solutions_identified": ["<string>", ...],
        "utilization": "<effizient/angemessen/verbesserungswuerdig/nicht beurteilbar>"
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
    "cannot_assess": ["<string: Aspekt der nicht bewertet werden kann>", ...]
}}"""
