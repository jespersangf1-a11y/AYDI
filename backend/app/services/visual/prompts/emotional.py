"""Emotional design impact prompt for yacht photos."""

from app.services.visual.prompt_context import (
    ASSESSABILITY_RULES,
    CLASS_FALLBACK_NOTICE,
    build_zone_note,
    resolve_boat_class_context,
)

# Alle 13 Bootsklassen aus BoatClass. Ohne eigenen Eintrag wuerde eine Klasse
# still gegen den Fahrtensegler-Massstab bewertet (B-3).
BOAT_CLASS_CONTEXT = {
    "small_sail": "Kleine Segelyacht (8-12m). Gemuetlichkeit und Geborgenheit sind positiv. Kompaktheit ist normal. Bewerte, ob der Raum trotz begrenzter Groesse einladend wirkt.",
    "cruising_sail": "Fahrtensegelyacht (12-18m). Balance zwischen Geborgenheit und Offenheit. Der Raum soll zum laengeren Aufenthalt einladen. Natuerliches Licht ist wichtig.",
    "racing_sail": "Regattayacht. Die emotionale Wirkung entsteht aus Purismus und Zweckform, nicht aus Wohnlichkeit. Sichtbares Laminat, offene Struktur und Kargheit sind Teil der Identitaet. Bewerte Klarheit, Konsequenz und sportliche Anmutung.",
    "daysailer": "Daysailer/Weekender. Die Wirkung entsteht im Cockpit und an Deck: Leichtigkeit, Naehe zum Wasser, klare Linien. Unter Deck genuegt eine freundliche, helle Rueckzugsecke - Luxuswirkung wird nicht erwartet.",
    "motorsailer": "Motorsegler. Der Deckssalon mit Rundumsicht ist das emotionale Zentrum: Helligkeit und Panoramablick sind die Staerke. Bewerte, ob der Uebergang vom hellen Salon ins dunklere Unterdeck bewusst gestaltet oder ein harter Bruch ist.",
    "catamaran_sail": "Segel-Katamaran. Erwartet wird Helligkeit, Weite und ein flaechiger, offener Salon mit Durchblick nach aussen. Die schmalen Rumpfkabinen duerfen hoehlenartig wirken, solange Licht und Belueftung stimmen - bewerte sie nicht am Massstab des Salons.",
    "catamaran_motor": "Motor-Katamaran. Grosszuegigkeit und fliessender Uebergang zwischen Innen- und Aussenbereich praegen den Eindruck. Erwartet wird eine loungeartige, helle Wirkung mit klarer Zonierung.",
    "small_motor": "Kleine Motoryacht (unter 12m). Freundlich, hell und unkompliziert. Kompakte Kajuete ist normal. Bewerte, ob der Aufenthalt an Bord einladend wirkt - nicht, ob der Raum beeindruckt.",
    "large_motor": "Grosse Motoryacht (18-30m). Luxurioese Grosszuegigkeit erwartet. Raeume sollen beeindrucken und gleichzeitig Wohlbefinden vermitteln. Raumdramaturgie wichtig.",
    "sport_cruiser": "Sport-Cruiser. Dynamik, Sportlichkeit und ein loungeartiges Cockpit praegen die Wirkung. Niedrige Innenhoehen sind bauartbedingt und kein emotionaler Mangel. Bewerte, ob das sportliche Versprechen des Aussendesigns innen eingeloest wird.",
    "trawler": "Trawler/Verdraenger. Erwartet werden Behaglichkeit, Soliditaet und ein wohnliches, fast hausartiges Gefuehl. Das Steuerhaus mit Aussicht ist ein emotionaler Schwerpunkt. Nicht Glamour, sondern Geborgenheit auf langer Fahrt ist der Massstab.",
    "explorer": "Explorer/Expeditionsyacht. Der Eindruck lebt von Robustheit, Ehrlichkeit der Materialien und dem Gefuehl von Autarkie. Sichtbare Technik und funktionale Raeume sind Teil der Erzaehlung, kein Mangel. Warmes Licht gegen die harte Bauweise ist ein Qualitaetsmerkmal.",
    "superyacht": "Superyacht (30m+). Architektonisches Erlebnis. Jede Sichtachse kuratiert, jeder Raum inszeniert. Emotionale Wirkung auf hoechstem Niveau erwartet.",
}

SPATIAL_EXPECTATIONS_BY_CLASS = {
    "small_sail": "Auf einer kleinen Segelyacht ist Kompaktheit NORMAL. Ein Raum, der sich trotz 2m Breite gemuetlich anfuehlt, verdient eine hohe Bewertung. Bewerte nicht nach absoluter Groesse, sondern nach Raumgefuehl relativ zur Bootsklasse.",
    "cruising_sail": "Auf einer Fahrtenyacht wird ein ausgewogenes Raumgefuehl erwartet. Nicht luxurioes, aber auch nicht beengend. Natuerliches Licht und durchdachte Proportionen sind entscheidend.",
    "racing_sail": "Auf einer Regattayacht ist ein karger, offener Innenraum die Norm. Fehlender Ausbau ist kein Mangel. Bewerte, ob die Reduktion konsequent und sauber gestaltet ist.",
    "daysailer": "Auf einem Daysailer wird unter Deck kein Wohnraum erwartet. Der emotionale Massstab liegt im Cockpit: Offenheit, Sitzkomfort, Naehe zum Wasser.",
    "motorsailer": "Auf einem Motorsegler wird ein heller Deckssalon mit Rundumsicht erwartet. Der Massstab ist der Kontrast zwischen Panorama-Ebene und geschuetztem Unterdeck.",
    "catamaran_sail": "Auf einem Segel-Katamaran wird ein breiter, heller Salon erwartet, aber schmale Rumpfkabinen sind bauartbedingt normal. Bewerte beide Bereiche mit unterschiedlichem Massstab.",
    "catamaran_motor": "Auf einem Motor-Katamaran wird viel nutzbare Flaeche und ein fliessender Uebergang nach aussen erwartet. Der Massstab ist Weite und Zonierung, nicht Deckenhoehe.",
    "small_motor": "Auf einer kleinen Motoryacht ist eine kompakte Kajuete normal. Bewerte Helligkeit und Aufenthaltsqualitaet, nicht Volumen.",
    "large_motor": "Auf einer grossen Motoryacht wird Grosszuegigkeit erwartet. Raeume sollen eine gewisse Dramaturgie haben - der Salon soll beeindrucken, die Kabinen sollen Rueckzugsort sein.",
    "sport_cruiser": "Auf einem Sport-Cruiser sind niedrige Innenhoehen bauartbedingt. Der Massstab ist die Aussenlounge und die sportliche Konsequenz der Linien.",
    "trawler": "Auf einem Trawler wird ein wohnliches, seegehendes Raumgefuehl mit durchgehender Stehhoehe erwartet. Massstab ist Behaglichkeit und Sicherheit bei Seegang, nicht Repraesentation.",
    "explorer": "Auf einer Expeditionsyacht duerfen Technik- und Vorratsraeume Wohnflaeche kosten. Massstab ist Funktion und Autarkie; Waerme entsteht ueber Licht und Materialien, nicht ueber Flaeche.",
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
        boat_class: One of the 13 BoatClass values (e.g. 'cruising_sail', 'trawler').
        zone_type: Optional zone type for context.
        context: Optional additional context dict.
        visual_context: Optional boat-specific context from BoatDNA (includes expert knowledge).

    Returns:
        German-language prompt string requesting JSON output.
    """
    class_desc, class_is_fallback = resolve_boat_class_context(boat_class, BOAT_CLASS_CONTEXT)
    spatial_expectation, _ = resolve_boat_class_context(boat_class, SPATIAL_EXPECTATIONS_BY_CLASS)
    fallback_notice = CLASS_FALLBACK_NOTICE if class_is_fallback else ""

    # Nutzerfreitext darf NICHT roh in den Prompt (Prompt-Injection, SEC-3/B-6).
    zone_note = build_zone_note(zone_type)

    visual_context_section = ""
    if visual_context:
        visual_context_section = f"\n\n{visual_context}\n"

    return f"""Du bist ein erfahrener Yachtdesigner und Innenarchitekt mit besonderem Gespuer fuer emotionale Raumwirkung. Du verstehst, warum manche Raeume als premium, einladend oder beklemmend empfunden werden. Analysiere dieses Bild.{visual_context_section}

Bootsklasse: {class_desc}{fallback_notice}{zone_note}

{spatial_expectation}
{ASSESSABILITY_RULES}
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
    "emotional_score": <float 0-100 oder null>,
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
