"""Construction knowledge — domain reference data for yacht construction methods.

German-language descriptions, quality indicators, and known issues for
the 6 major hull material + construction method combinations.
"""

CONSTRUCTION_KNOWLEDGE: dict[str, dict] = {
    "grp_solid_hand_layup": {
        "description": "Solides GFK-Laminat in Handauflegeverfahren",
        "typical_boats": "Serienboote <15m, ältere Designs",
        "glass_resin_ratio": "40-55% Glas",
        "strengths": [
            "Bewährte Technik, einfach zu reparieren",
            "Niedrige Werkzeugkosten",
            "Gute Schlagfestigkeit",
        ],
        "weaknesses": [
            "Höheres Gewicht als Sandwich oder Infusion",
            "Qualität abhängig vom Laminierteam",
            "Schwankende Glasanteile möglich",
        ],
        "quality_indicators_visual": [
            "Gleichmäßige Gelcoat-Oberfläche ohne Orangenhaut",
            "Keine sichtbaren Lufteinschlüsse oder Trockenstellen",
            "Saubere Kanten und Übergänge",
            "Konstante Laminatstärke (prüfen an Ausschnitten)",
        ],
        "known_issues": [
            {
                "issue": "Osmotische Blasenbildung",
                "onset_years": "5-15",
                "location": "Unterwasserschiff",
                "cause": "Feuchtigkeit diffundiert durch Gelcoat ins Laminat",
            },
            {
                "issue": "Gelcoat-Rissbildung (Spinnennetze)",
                "onset_years": "3-10",
                "location": "Hochbelastete Bereiche, Ecken",
                "cause": "Zu dicker Gelcoat oder Materialermüdung",
            },
        ],
    },
    "grp_sandwich_resin_infusion": {
        "description": "GFK-Sandwich-Laminat im Vakuuminfusionsverfahren",
        "typical_boats": "Moderne Serienboote 10-25m, Performance-Cruiser",
        "glass_resin_ratio": "55-65% Glas (höher als Handlaminat)",
        "strengths": [
            "Exzellentes Steifigkeit-zu-Gewicht-Verhältnis",
            "Reproduzierbare Qualität durch Vakuumprozess",
            "Sehr gute thermische und akustische Isolation",
        ],
        "weaknesses": [
            "Höhere Werkzeugkosten (Vakuumausrüstung)",
            "Kernmaterial anfällig bei Wassereintritt",
            "Komplexere Reparatur als Massivlaminat",
        ],
        "quality_indicators_visual": [
            "Glatte, gleichmäßige Oberflächen ohne Luftblasen",
            "Keine Delamination sichtbar (Klopftest)",
            "Saubere Infusionsnähte",
            "Gleichmäßige Kerndicke",
        ],
        "known_issues": [
            {
                "issue": "Kerndelamination",
                "onset_years": "8-20",
                "location": "Deck, besonders um Hardware-Befestigungen",
                "cause": "Wassereintritt durch undichte Beschlagverschraubungen",
            },
            {
                "issue": "Druckstellen im Kernmaterial",
                "onset_years": "1-5",
                "location": "Hohe Punktlasten (Klampen, Winschen)",
                "cause": "Fehlende lokale Kernverstärkung",
            },
        ],
    },
    "aluminium_welded": {
        "description": "Geschweißte Aluminiumkonstruktion",
        "typical_boats": "Expeditionsyachten, Arbeitsboote, Custom-Yachten 12-30m",
        "strengths": [
            "Extrem robust und reparierbar",
            "Kein osmotisches Risiko",
            "Hervorragendes Gewicht-Festigkeits-Verhältnis",
            "Recyclebar",
        ],
        "weaknesses": [
            "Erfordert spezielle Schweißerqualifikation",
            "Korrosionsrisiko bei falscher Legierung oder Antifouling",
            "Elektrolyse-Gefahr bei unedleren Metallen in Kontakt",
        ],
        "quality_indicators_visual": [
            "Gleichmäßige Schweißnähte ohne Poren",
            "Keine Verfärbungen (Hinweis auf Überhitzung)",
            "Saubere Schleifarbeiten an Nähten",
            "Korrekte Anodisierung oder Beschichtung",
        ],
        "known_issues": [
            {
                "issue": "Galvanische Korrosion",
                "onset_years": "2-5",
                "location": "Unterwasserschiff, besonders Ruder und Propellerwelle",
                "cause": "Kontakt mit unedleren Metallen ohne Isolation",
            },
            {
                "issue": "Spannungsrisskorrosion",
                "onset_years": "5-15",
                "location": "Schweißnahtnähe, hochbelastete Verbindungen",
                "cause": "Falsche Legierung (5xxx statt 6xxx für Strukturteile)",
            },
        ],
        "critical_rules": [
            "NUR 5083/5086 für Unterwasser, 6082 für Struktur",
            "Kupferhaltiges Antifouling VERBOTEN",
            "Opferanoden: Zink in Salzwasser, Magnesium in Süßwasser",
        ],
    },
    "carbon_composite_prepreg_autoclave": {
        "description": "Kohlefaser-Prepreg im Autoklav-Verfahren",
        "typical_boats": "Hochleistungsyachten, Rennyachten, Superyachten",
        "strengths": [
            "Höchste Festigkeit bei geringstem Gewicht",
            "Optimaler Faservolumenanteil (60%+)",
            "Reproduzierbare Materialqualität",
        ],
        "weaknesses": [
            "Sehr hohe Material- und Werkzeugkosten",
            "Komplexe Reparatur erfordert Spezialwissen",
            "Schlagempfindlich (versteckte Delamination)",
        ],
        "quality_indicators_visual": [
            "Gleichmäßiges Fasermuster ohne Verzerrungen",
            "Keine weißen Stellen (Faserbruch)",
            "Glatte Oberfläche ohne Pinholes",
            "Scharfe Kanten und präzise Konturen",
        ],
        "known_issues": [
            {
                "issue": "Versteckte Delamination durch Schlagschaden",
                "onset_years": "0-5",
                "location": "Bug, Rumpf-Deck-Verbindung, Kielbereich",
                "cause": "Impact-Schäden oft äußerlich nicht sichtbar",
            },
            {
                "issue": "UV-Degradation der Matrix",
                "onset_years": "5-10",
                "location": "Ungeschützte Oberflächen",
                "cause": "Fehlende UV-Schutzschicht (Gelcoat/Lack)",
            },
        ],
    },
    "wood_epoxy_cold_molded": {
        "description": "Holz-Epoxid-Kaltformverfahren",
        "typical_boats": "Custom-Yachten, restaurierte Klassiker, Daysailer",
        "strengths": [
            "Hervorragendes Gewicht-Steifigkeits-Verhältnis",
            "Ästhetisch hochwertig",
            "Gute Dämpfungseigenschaften",
        ],
        "weaknesses": [
            "Sehr arbeitsintensiv",
            "Erfordert trockene, temperierte Bauhalle",
            "Epoxid-Allergie-Risiko für Werftarbeiter",
        ],
        "quality_indicators_visual": [
            "Saubere Epoxid-Versiegelung ohne Trockenstellen",
            "Gleichmäßiger Furnierverlauf",
            "Keine Blasenbildung unter der Beschichtung",
            "Saubere Schäftungen und Stöße",
        ],
        "known_issues": [
            {
                "issue": "Epoxid-Delamination",
                "onset_years": "10-20",
                "location": "Kiel-Rumpf-Verbindung, Deck-Rumpf-Verbindung",
                "cause": "Langzeitermüdung der Epoxid-Holz-Verbindung",
            },
            {
                "issue": "Feuchtigkeitseintritt durch Beschichtungsschäden",
                "onset_years": "5-15",
                "location": "Beschlagdurchbrüche, Reling-Befestigungen",
                "cause": "Mechanische Beschädigung der Epoxidversiegelung",
            },
        ],
    },
    "steel_welded": {
        "description": "Geschweißte Stahlkonstruktion",
        "typical_boats": "Langfahrtyachten, Motorschiffe >15m, Arbeitsboote",
        "strengths": [
            "Höchste Robustheit und Reparierbarkeit",
            "Bewährte Bautechnik weltweit verfügbar",
            "Magnetischer Kompass-freundlich (bei Kompensation)",
        ],
        "weaknesses": [
            "Hohes Gewicht",
            "Erfordert konsequenten Korrosionsschutz",
            "Schweißverzug muss kontrolliert werden",
        ],
        "quality_indicators_visual": [
            "Gleichmäßige Schweißnähte (keine Poren, keine Unterschnitte)",
            "Intakte Beschichtung ohne Roststellen",
            "Saubere Oberfläche ohne Zunder",
            "Korrekte Plattendicken (Ultraschall-Messung)",
        ],
        "known_issues": [
            {
                "issue": "Flächenkorrosion unter Beschichtung",
                "onset_years": "3-8",
                "location": "Bilge, Kettenlager, Ankerkasten",
                "cause": "Beschichtungsschäden und stehendes Wasser",
            },
            {
                "issue": "Lochfraß (Pitting)",
                "onset_years": "5-15",
                "location": "Unterwasserschiff, besonders Schweißnähte",
                "cause": "Lokale Beschichtungsdefekte + Salzwasser",
            },
        ],
        "thru_hull_rule": "Bronze-Seeventile, KEINE Kunststoff-Durchbrüche unter WL",
    },
}


def get_construction_knowledge(hull_material: str, hull_construction: str) -> dict | None:
    """Lookup construction knowledge for a material+construction combo.
    Returns None if no entry exists (graceful fallback)."""
    key = f"{hull_material}_{hull_construction}"
    return CONSTRUCTION_KNOWLEDGE.get(key)
