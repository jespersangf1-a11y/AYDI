"""Spatial analysis prompt for yacht interior/exterior photos."""

from app.services.visual.prompt_context import (
    ASSESSABILITY_RULES,
    CLASS_FALLBACK_NOTICE,
    build_zone_note,
    resolve_boat_class_context,
    safe_zone_label,
)

# Alle 13 Bootsklassen aus BoatClass. Ohne eigenen Eintrag wuerde eine Klasse
# still gegen den Fahrtensegler-Massstab bewertet (B-3) — fachlich falsch und
# fuer den Nutzer unsichtbar.
BOAT_CLASS_CONTEXT = {
    "small_sail": "Kleine Segelyacht (8-12m). Jeder Zentimeter zaehlt. Kompakte Raeume sind normal und akzeptabel. Bewerte nach Funktionalitaet, nicht nach Grosszuegigkeit.",
    "cruising_sail": "Fahrtensegelyacht (12-18m). Balance zwischen Funktion und Komfort. Moderate Raumgroessen erwartet. Ergonomie und Stauraumnutzung sind wichtig.",
    "racing_sail": "Regattayacht. Der Innenraum ist Gewichtsfrage: spartanisch, offen, ohne schwere Moebel. Pipe-Kojen, freiliegende Struktur und fehlender Komfortausbau sind KEIN Mangel. Bewerte Zugaenglichkeit zu Trimm- und Riggpunkten, Sicherheit in Schraeglage, Stauraum fuer Segel.",
    "daysailer": "Daysailer/Weekender. Minimaler Innenausbau, oft nur Sitzbaenke, Notkoje und Stauraum. Stehhoehe wird NICHT erwartet. Das Cockpit ist der Hauptaufenthaltsraum — bewerte dort Sitzlaenge, Ergonomie und Bedienbarkeit.",
    "motorsailer": "Motorsegler. Deckssalon mit Rundumsicht und hohes Freibord ergeben grosszuegigere Innenmasse als bei einem reinen Segler gleicher Laenge. Erwarte Stehhoehe durchgehend, Innensteuerstand und den Uebergang Deckssalon-Unterdeck als kritische Stelle.",
    "catamaran_sail": "Segel-Katamaran. Raumlogik voellig anders als beim Einrumpfboot: breiter Salon auf Brueckendeckniveau, Kabinen in schmalen Ruempfen. Bewerte Salonbreite und Sichtachsen grosszuegig, Rumpfkabinen dagegen am Massstab schmaler Gaenge und begrenzter Kojenbreite. Keine Schraeglage — dafuer Nickbewegung.",
    "catamaran_motor": "Motor-Katamaran. Sehr grosse nutzbare Flaeche auf dem Brueckendeck, oft Flybridge. Erwarte grosszuegigen Salon, ebene Uebergaenge innen/aussen und klare Zonierung. Rumpfkabinen bleiben schmal — das ist bauartbedingt und kein Mangel.",
    "small_motor": "Kleine Motoryacht (unter 12m). Kompakte Kajuete, oft nur eine Nasszelle und eine Kabine. Der Fahrstand und die Aussenplicht dominieren. Bewerte funktionale Raumnutzung und Bewegungsfreiheit an Bord, nicht Grosszuegigkeit.",
    "large_motor": "Grosse Motoryacht (18-30m). Komfort und Luxus werden erwartet. Grosszuegige Raeume, klare Zonierung, Privatsphaere zwischen Gaesten und Crew.",
    "sport_cruiser": "Sport-Cruiser. Sportliches, flaches Profil, dadurch niedrige Innenhoehen und oft eingeschraenkte Stehhoehe — bauartbedingt, kein Mangel. Schwerpunkt liegt auf Cockpit, Sonnenliegen und Badeplattform. Unterdecks zaehlt cleverer Stauraum mehr als Volumen.",
    "trawler": "Trawler/Verdraenger. Voluminoeser, kastiger Aufbau mit hohem Innenraum. Erwarte durchgehende Stehhoehe, Steuerhaus mit Sitzplatz, seegehende Details: Handlaeufe, geschlossene Stauraeume, kurze sichere Wege bei Seegang. Langfahrt-Vorraete brauchen viel Stauraum.",
    "explorer": "Explorer/Expeditionsyacht. Selbstversorgung ueber lange Zeitraeume. Sehr grosser Stauraum, Werkstatt, Technikraeume und Vorratslager sind funktionale Pflicht und duerfen Wohnflaeche kosten. Bewerte Robustheit, Wartungszugaenge und sichere Wege hoeher als Eleganz.",
    "superyacht": "Superyacht (30m+). Hoechste Ansprueche an Raumgestaltung. Architektonische Qualitaet, kuratierte Sichtachsen, dramaturgischer Raumfluss. Getrennte Crew- und Gastwege werden erwartet.",
}


def get_spatial_analysis_prompt(
    boat_class: str,
    zone_type: str | None = None,
    context: dict | None = None,
    visual_context: str | None = None,
) -> str:
    """Generate the spatial analysis prompt for Claude vision API.

    Args:
        boat_class: One of the 13 BoatClass values (e.g. 'cruising_sail', 'trawler').
        zone_type: Optional zone type (e.g. 'salon', 'cabin') for focused analysis.
        context: Optional additional context dict.
        visual_context: Optional boat-specific context from BoatDNA (includes expert knowledge).

    Returns:
        German-language prompt string requesting JSON output.
    """
    class_desc, class_is_fallback = resolve_boat_class_context(boat_class, BOAT_CLASS_CONTEXT)
    fallback_notice = CLASS_FALLBACK_NOTICE if class_is_fallback else ""

    zone_instruction = ""
    if zone_type:
        # Unbekannter zone_type: der Rohwert (Nutzerfreitext) darf NICHT in den
        # Prompt interpoliert werden (Prompt-Injection-Schutz, SEC-3/B-6).
        label = safe_zone_label(zone_type)
        if label is None:
            zone_instruction = build_zone_note(zone_type)
        else:
            zone_instruction = (
                f"\nDieses Bild zeigt speziell: {label}. "
                "Bewerte mit Fokus auf die typischen Anforderungen dieses Raumtyps."
            )

    extra_context = ""
    if context:
        if "length_m" in context:
            extra_context += f"\nBootslaenge: {context['length_m']}m."
        if "beam_m" in context:
            extra_context += f"\nBootsbreite: {context['beam_m']}m."

    visual_context_section = ""
    if visual_context:
        visual_context_section = f"\n\n{visual_context}\n"

    return f"""Du bist ein erfahrener Yachtdesigner und Raumplaner mit ueber 20 Jahren Erfahrung im Yachtbau. Analysiere dieses Bild einer Yacht.{visual_context_section}

Bootsklasse: {class_desc}{fallback_notice}{extra_context}{zone_instruction}
{ASSESSABILITY_RULES}
Bewerte folgende Aspekte basierend auf dem, was du im Bild erkennen kannst:

1. **Raumproportionen**: Verhaeltnis von Hoehe zu Breite, Raumwirkung
2. **Ergonomie**: Bewegungsfreiheit, Durchgangsbreiten (soweit erkennbar)
3. **Stauraum**: Sichtbare Stauraumloesungen, Effizienz der Raumnutzung
4. **Geschaetzte Abmessungen**: Schaetze sichtbare Masse (Durchgangsbreiten, Deckenhoehe, Raumtiefe) relativ zu erkennbaren Referenzobjekten

WICHTIG: Wenn etwas nicht erkennbar ist, sage das explizit mit "nicht beurteilbar". Erfinde keine Werte. Sei ehrlich ueber die Grenzen dessen, was aus einem Foto abgeleitet werden kann.

Antworte ausschliesslich mit einem JSON-Objekt in folgendem Format (kein zusaetzlicher Text):

{{
    "spatial_score": <float 0-100 oder null>,
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
