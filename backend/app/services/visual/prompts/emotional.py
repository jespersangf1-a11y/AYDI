"""Emotional design impact prompt for yacht photos."""

BOAT_CLASS_CONTEXT = {
    "small_sail": "Kleine Segelyacht (8-12m). Gemuetlichkeit und Geborgenheit sind positiv. Kompaktheit ist normal. Bewerte, ob der Raum trotz begrenzter Groesse einladend wirkt.",
    "cruising_sail": "Fahrtensegelyacht (12-18m). Balance zwischen Geborgenheit und Offenheit. Der Raum soll zum laengeren Aufenthalt einladen. Natuerliches Licht ist wichtig.",
    "large_motor": "Grosse Motoryacht (18-30m). Luxurioese Grosszuegigkeit erwartet. Raeume sollen beeindrucken und gleichzeitig Wohlbefinden vermitteln. Raumdramaturgie wichtig.",
    "superyacht": "Superyacht (30m+). Architektonisches Erlebnis. Jede Sichtachse kuratiert, jeder Raum inszeniert. Emotionale Wirkung auf hoechstem Niveau erwartet.",
}

SPATIAL_EXPECTATIONS_BY_CLASS = {
    "small_sail": "Auf einer kleinen Segelyacht ist Kompaktheit NORMAL. Ein Raum, der sich trotz 2m Breite gemuetlich anfuehlt, verdient eine hohe Bewertung. Bewerte nicht nach absoluter Groesse, sondern nach Raumgefuehl relativ zur Bootsklasse.",
    "cruising_sail": "Auf einer Fahrtenyacht wird ein ausgewogenes Raumgefuehl erwartet. Nicht luxurioes, aber auch nicht beengend. Natuerliches Licht und durchdachte Proportionen sind entscheidend.",
    "large_motor": "Auf einer grossen Motoryacht wird Grosszuegigkeit erwartet. Raeume sollen eine gewisse Dramaturgie haben — der Salon soll beeindrucken, die Kabinen sollen Rueckzugsort sein.",
    "superyacht": "Auf einer Superyacht wird architektonische Rauminszenierung erwartet. Jede Sichtachse, jeder Uebergang, jede Materialwahl muss einem Gesamtkonzept folgen.",
}


def get_emotional_impact_prompt(
    boat_class: str,
    zone_type: str | None = None,
    context: dict | None = None,
    visual_context: str | None = None,
) -> str:
    """Generate the emotional design impact prompt for Claude vision API.

    Args:
        boat_class: One of small_sail, cruising_sail, large_motor, superyacht.
        zone_type: Optional zone type for context.
        context: Optional additional context dict.
        visual_context: Optional boat-specific context from BoatDNA (includes expert knowledge).

    Returns:
        German-language prompt string requesting JSON output.
    """
    class_desc = BOAT_CLASS_CONTEXT.get(boat_class, BOAT_CLASS_CONTEXT["cruising_sail"])
    spatial_expectation = SPATIAL_EXPECTATIONS_BY_CLASS.get(boat_class, SPATIAL_EXPECTATIONS_BY_CLASS["cruising_sail"])

    zone_note = ""
    if zone_type:
        zone_note = f"\nDieser Bereich ist: {zone_type}."

    visual_context_section = ""
    if visual_context:
        visual_context_section = f"\n\n{visual_context}\n"

    return f"""Du bist ein erfahrener Yachtdesigner und Innenarchitekt mit besonderem Gespuer fuer emotionale Raumwirkung. Du verstehst, warum manche Raeume als premium, einladend oder beklemmend empfunden werden. Analysiere dieses Bild.{visual_context_section}

Bootsklasse: {class_desc}{zone_note}

{spatial_expectation}

Bewerte die emotionale Wirkung dieses Raums aus der Perspektive eines anspruchsvollen Kunden:

1. **Erster Eindruck**: Was ist die unmittelbare emotionale Reaktion beim Betrachten?
2. **Raumwahrnehmung**: Wirkt der Raum grosszuegig/kompakt/beengt/einladend/klinisch/ueberladen?
3. **Proportionen**: Deckenhoehe im Verhaeltnis zur Breite, Moebeldichte
4. **Licht**: Natuerliches Licht, Lichtverteilung, dunkle Zonen
5. **Material-Wirkung**: Visueller Eindruck der Materialien, Harmonie, Anzahl sichtbarer Materialien
6. **Sichtachsen**: Blickfuehrung beim Eintreten, visuelle Tiefe, Fensterausblicke, Endpunkt des Blicks
7. **Stilbewertung**: Designstil, Zeitlosigkeit, Kohaerenz, Zielgruppe

REGELN:
1. Kalibriere die Bewertung an der Bootsklasse — ein kompakter Salon auf einer 10m-Yacht ist KEIN Mangel.
2. Bei Renderings: bewerte die GEPLANTE Wirkung, nicht die Renderqualitaet.
3. Sei EHRLICH — beschoenige keine Probleme, aber sei auch nicht ueberkritisch.

Antworte ausschliesslich mit einem JSON-Objekt (kein zusaetzlicher Text):

{{
    "emotional_score": <float 0-100>,
    "assessable": <bool>,
    "first_impression": {{
        "description": "<string: 1-2 Saetze zum Gesamteindruck>",
        "keywords": ["<string>", ...]
    }},
    "spatial_perception": {{
        "dominant_feeling": "<grosszuegig/angemessen/kompakt/beengt/nicht beurteilbar>",
        "feels_appropriate_for_class": <bool>,
        "reasoning": "<string: warum passt oder passt nicht zur Bootsklasse>"
    }},
    "proportions": {{
        "ceiling_impression": "<hoch/angemessen/niedrig/nicht beurteilbar>",
        "width_impression": "<grosszuegig/angemessen/eng/nicht beurteilbar>",
        "furniture_density": "<aufgeraeumt/ausgewogen/voll/ueberladen/nicht beurteilbar>",
        "assessment": "<string>"
    }},
    "light": {{
        "natural_light": "<reichlich/angemessen/wenig/dunkel/nicht beurteilbar>",
        "distribution": "<gleichmaessig/akzeptabel/ungleichmaessig/nicht beurteilbar>",
        "dark_zones_visible": <bool>,
        "notes": "<string>"
    }},
    "materials_impression": {{
        "material_count_visible": <int>,
        "harmony": "<harmonisch/akzeptabel/dissonant/nicht beurteilbar>",
        "dominant_material": "<string: z.B. Teak, Hochglanzlack, Leder>",
        "what_works": "<string oder null>",
        "what_clashes": "<string oder null>"
    }},
    "sightlines": {{
        "entry_view_target": "<string: was sieht man beim Eintreten zuerst>",
        "view_depth": "<tief/mittel/flach/nicht beurteilbar>",
        "visual_endpoint": "<Fenster/Wand/Moebel/offen/nicht beurteilbar>",
        "sightline_quality": "<inszeniert/gut/neutral/blockiert/nicht beurteilbar>"
    }},
    "style": {{
        "tags": ["<string: z.B. modern, klassisch, skandinavisch>", ...],
        "consistency": "<durchgehend/weitgehend/bruchig/nicht beurteilbar>",
        "era_feeling": "<zeitlos/aktuell/veraltet/nicht beurteilbar>",
        "target_audience": "<string: z.B. junges Paar, Familie, Eigner 50+>"
    }},
    "improvement_suggestions": [
        {{
            "area": "<string: welcher Bereich>",
            "current_state": "<string: was ist jetzt>",
            "suggested_change": "<string: was wuerde helfen>",
            "expected_impact": "<hoch/mittel/gering>",
            "confidence": "<hoch/mittel/niedrig>"
        }}
    ],
    "confidence": "<hoch/mittel/niedrig>",
    "cannot_assess": ["<string>", ...]
}}"""
