"""
AYDI Expert-Community-Wissen
Knowledge extracted from expert YouTube channels, forums, and maritime publications.

Sources:
- BootsProfis (bootsprofis.tv / YouTube, 300+ videos)
- YACHT-TV (yacht.de / YouTube, 86k+ subscribers)
- Marietim / Marie Schneider (YouTube, 27k+ subscribers)
- Blauwasser.de (Cruising knowledge base)
- boote-forum.de (German boat owner forum)
- segeln-forum.de (German sailing forum)
- yacht-forum.de (YACHT magazine forum)
- Pantaenius (Marine insurance knowledge)
- float Magazin (Maritime lifestyle + tech)
- Palstek (Practical sailing magazine)
- SVB (Marine chandlery tech articles)

Author: AYDI Research Team
Version: 2.0
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
from enum import Enum


class KnowledgeSource(Enum):
    BOOTSPROFIS = "bootsprofis"
    YACHT_TV = "yacht_tv"
    MARIETIM = "marietim"
    BLAUWASSER = "blauwasser"
    BOOTE_FORUM = "boote_forum"
    SEGELN_FORUM = "segeln_forum"
    YACHT_FORUM = "yacht_forum"
    PANTAENIUS = "pantaenius"
    FLOAT_MAGAZIN = "float_magazin"
    PALSTEK = "palstek"
    SVB = "svb"
    ADAC_SKIPPER = "adac_skipper"
    PRACTICAL_SAILOR = "practical_sailor"


class ExpertiseArea(Enum):
    HULL_INSPECTION = "hull_inspection"
    OSMOSIS = "osmosis"
    RIGGING = "rigging"
    ENGINE = "engine"
    ELECTRICAL = "electrical"
    TEAK_DECK = "teak_deck"
    SEACOCKS = "seacocks"
    ANTIFOULING = "antifouling"
    PURCHASE_GUIDANCE = "purchase_guidance"
    KEEL = "keel"
    SANDWICH_CORE = "sandwich_core"
    GALVANIC_CORROSION = "galvanic_corrosion"
    SHORE_POWER = "shore_power"
    PLUMBING = "plumbing"
    WINTERIZATION = "winterization"


@dataclass
class ExpertInsight:
    """Ein einzelner Expertenbeitrag mit Quellenangabe"""
    topic: str
    insight_de: str
    technical_detail: str
    source: KnowledgeSource
    expertise_area: ExpertiseArea
    confidence: str  # "verified", "expert_consensus", "single_source", "anecdotal"
    practical_relevance: str  # "critical", "high", "medium", "low"


# ============================================================================
# BOOTSKAUF-EXPERTISE — Bootskauf-Wissen aus Gutachterpraxis
# Source: BootsProfis, Blauwasser.de, yacht.de
# ============================================================================

PURCHASE_EXPERTISE: Dict[str, Any] = {
    "pre_purchase_inspection": {
        "source": ["bootsprofis", "blauwasser", "yacht"],
        "description_de": "Systematische Vorgehensweise bei der Gebrauchtboot-Besichtigung",
        "steps": [
            {
                "phase": "Erstbesichtigung (im Wasser)",
                "duration_hours": 2,
                "checks": [
                    "Gesamteindruck: Pflegezustand, Sauberkeit, Rost an Deck",
                    "Rigg-Sichtkontrolle von Deck aus",
                    "Motor-Kurztest: Öl-Check, Kaltstart, Abgasfarbe",
                    "Innenlayout: Feuchtigkeit, Geruch, Schimmelspuren",
                    "Bilge: Wasserstand, Ölspuren, Korrosionsspuren",
                    "Elektrik: Schalttafel, Kabelzustand sichtbar",
                    "Fenster/Luken: Dichtigkeit, Beschläge",
                    "Ruder: Spiel am Steuerrad/Pinne testen"
                ],
                "red_flags": [
                    "Muffiger Geruch unter Deck = Wassereinbruch",
                    "Öliger Film in Bilge = Motorproblem oder undichte Stopfbuchse",
                    "Blaue Abgase bei Dieselmotor = Ölverbrennung",
                    "Stark verschmutzte Bilge = mangelnde Pflege generell",
                    "Schimmel an Polstern = chronisches Feuchtigkeitsproblem"
                ]
            },
            {
                "phase": "Detailinspektion (an Land / Kran)",
                "duration_hours": 4,
                "checks": [
                    "Unterwasserschiff: Antifouling-Zustand, Osmoseblasen",
                    "Feuchtemessung: Systematisch am Rumpf mit Tramex/Sovren",
                    "Kielbolzen: Verfärbungen, Risse am Übergang",
                    "Seeventile: Material (Bronze vs. Messing), Gangbarkeit",
                    "Ruderanlage: Lagerspiel, Dichtungen",
                    "Propeller: Schlagschäden, Korrosion",
                    "Wellendichtung: Tropfrate, Zustand Packung/Simmerring",
                    "Rumpf/Deck-Verbindung: Risse, Undichtigkeiten"
                ],
                "critical_measurements": {
                    "moisture_readings": {
                        "acceptable_grp": "< 15% relative Feuchte",
                        "concern": "15-25% — weitere Untersuchung nötig",
                        "critical": "> 25% — Osmose wahrscheinlich",
                        "tool": "Tramex Skipper Plus oder Sovereign Moisturemeter",
                        "note": "Messungen immer bei trockenem Boot, mind. 2 Wochen nach Kranen"
                    },
                    "keel_bolt_check": {
                        "method": "Visuelle Inspektion + Klopftest",
                        "red_flag": "Rostfahnen an Kielbolzen-Austrittstellen",
                        "critical": "Bewegung des Kiels bei seitlicher Belastung",
                        "note_de": "Bei Gusseisen-Kielen besonders kritisch — innere Korrosion nicht sichtbar"
                    }
                }
            },
            {
                "phase": "Probefahrt / Seatrial",
                "duration_hours": 3,
                "checks": [
                    "Motor: Laufkultur, Vibrationen, Temperatur unter Last",
                    "Getriebe: Schalten vorwärts/rückwärts, Geräusche",
                    "Ruder: Ansprechverhalten, Kurs-Stabilität",
                    "Rigg unter Last: Knackgeräusche, Wantenspannung",
                    "Segel: Profilform, Verschleiß, Nähte",
                    "Dichtigkeit: Fenster/Luken bei Krängung",
                    "Elektronik: GPS, Log, Echolot, Autopilot",
                    "Pumpen: Lenz, WC, Frischwasser testen"
                ]
            }
        ],
        "cost_guidance": {
            "gutachten_basic": "€400-€800 (Sichtprüfung + Feuchtemessung)",
            "gutachten_full": "€800-€1500 (Komplett inkl. Bericht)",
            "gutachten_osmose": "€300-€500 (Spezial-Osmosegutachten)",
            "rigg_check_specialist": "€400-€700",
            "motor_check_specialist": "€200-€400",
            "note_de": "Kosten für Gutachten amortisieren sich fast immer — versteckte Mängel kosten ein Vielfaches"
        }
    },

    "price_negotiation_factors": {
        "source": ["bootsprofis", "blauwasser"],
        "description_de": "Preisrelevante Mängel und deren Wertminderung",
        "factors": [
            {"issue": "Osmose Stadium 1 (Blasen < 5mm)", "discount_percent": "5-10%", "repair_cost": "€3.000-€5.000"},
            {"issue": "Osmose Stadium 2 (Blasen > 10mm, Laminat feucht)", "discount_percent": "15-25%", "repair_cost": "€8.000-€15.000"},
            {"issue": "Rigg älter als 12 Jahre", "discount_percent": "8-15%", "repair_cost": "€5.000-€12.000 (Neuverstayung)"},
            {"issue": "Motor > 4000h", "discount_percent": "10-20%", "repair_cost": "€8.000-€25.000 (Austausch)"},
            {"issue": "Teakdeck undicht", "discount_percent": "10-20%", "repair_cost": "€15.000-€40.000 (Neubelag)"},
            {"issue": "Seeventile aus Messing (nicht DZR)", "discount_percent": "3-5%", "repair_cost": "€2.000-€4.000 (Austausch)"},
            {"issue": "Elektronik veraltet (> 10 Jahre)", "discount_percent": "5-10%", "repair_cost": "€3.000-€8.000"},
            {"issue": "Segel > 8 Jahre / > 15.000 sm", "discount_percent": "5-10%", "repair_cost": "€3.000-€10.000 (Neusegel)"},
            {"issue": "Sandwichkern feucht (Deck)", "discount_percent": "15-30%", "repair_cost": "€10.000-€30.000"},
            {"issue": "Kielbolzen korrodiert", "discount_percent": "20-40%", "repair_cost": "€5.000-€15.000"}
        ]
    },

    "boat_age_expectations": {
        "source": ["bootsprofis", "yacht_gutachter"],
        "description_de": "Typische Alterungserscheinungen nach Bootsjahren",
        "expectations": {
            "0-5_jahre": {
                "zustand": "Neuwertig bis sehr gut",
                "typische_maengel": [
                    "Garantie-Themen bei Serienwerften",
                    "Kleinere Elektrik-Nacharbeiten",
                    "Gelcoat-Kratzer am Wasserpass"
                ]
            },
            "5-10_jahre": {
                "zustand": "Gut gepflegt = fast neuwertig",
                "typische_maengel": [
                    "Antifouling muss erneuert werden",
                    "Polster zeigen UV-Alterung",
                    "Dichtungen an Fenstern/Luken beginnen zu altern",
                    "Impeller und Verschleißteile Motor"
                ]
            },
            "10-15_jahre": {
                "zustand": "Mittlerer Zustand, Investitionen nötig",
                "typische_maengel": [
                    "Stehendes Gut muss erneuert werden (Versicherungspflicht)",
                    "Osmose kann beginnen (insbesondere Polyester-Boote)",
                    "Teakdeck-Fugen müssen nachgebessert werden",
                    "Elektronik veraltet",
                    "Motor hat 2000-4000h — Generalüberholung planen"
                ]
            },
            "15-25_jahre": {
                "zustand": "Intensive Pflege oder 'Projekt'",
                "typische_maengel": [
                    "Osmose wahrscheinlich bei Polyester-Booten",
                    "Kielbolzen-Kontrolle zwingend erforderlich",
                    "Seeventile müssen kontrolliert/ausgetauscht werden",
                    "Teakdeck ggf. komplett erneuern",
                    "Tankinspektion (Diesel/Wasser)",
                    "Ruderlagerwechsel",
                    "Komplette Neuverstayung des Riggs"
                ]
            },
            "25_plus_jahre": {
                "zustand": "Liebhaberstück oder umfassendes Refit",
                "typische_maengel": [
                    "Osmosesanierung oft bereits durchgeführt (prüfen!)",
                    "Motor-Austausch wahrscheinlich nötig",
                    "Gesamtes Rigg inkl. Mast prüfen (Ermüdung)",
                    "Bordnetze (Kabel, Schalter) komplett prüfen",
                    "Tanksanierung/-austausch",
                    "GFK-Laminat im Unterwasserbereich prüfen (Hydrolyse)",
                    "Strukturelle Integrität: Schotten, Stringer, Rumpf/Deck"
                ]
            }
        }
    }
}


# ============================================================================
# OSMOSE-EXPERTISE — Detailwissen aus Gutachterpraxis und Forschung
# Source: BootsProfis, Blauwasser.de, NautiCare, ADAC Skipper, Yachtcare
# ============================================================================

OSMOSIS_EXPERT_KNOWLEDGE: Dict[str, Any] = {
    "mechanism_detailed": {
        "source": ["blauwasser", "nauticare", "adac_skipper"],
        "description_de": "Detaillierter Osmose-Mechanismus bei GFK-Booten",
        "process": [
            "1. Wasser diffundiert durch Gelcoat (semipermeable Membran)",
            "2. Wasser löst wasserlösliche Stoffe im Laminat (Ester, unausgehärtete Harze)",
            "3. Osmotischer Druck baut sich auf (bis zu 7 bar gemessen)",
            "4. Blasenbildung zwischen Gelcoat und Laminat",
            "5. Blaseninhalt: Essigsäure-artige Flüssigkeit (stechender Geruch)",
            "6. Progressives Eindringen in tiefere Laminatschichten",
            "7. Hydrolyse des Polyesterharzes — Strukturverlust"
        ],
        "stages": {
            "stage_1_initial": {
                "description_de": "Einzelne kleine Blasen (< 5mm) im Gelcoat",
                "severity": "low",
                "structural_impact": "none",
                "repair_complexity": "simple",
                "cost_estimate": "€1.500-€3.000",
                "method": "Blasen öffnen, trocknen, Epoxid-Spachtel, Epoxid-Sperrschicht"
            },
            "stage_2_moderate": {
                "description_de": "Flächige Blasenbildung, Blasen 5-15mm, Gelcoat weich",
                "severity": "moderate",
                "structural_impact": "minimal",
                "repair_complexity": "moderate",
                "cost_estimate": "€5.000-€10.000",
                "method": "Gelcoat komplett entfernen, trocknen (2-6 Monate), Epoxid-Sperrschicht (min. 350µm)"
            },
            "stage_3_severe": {
                "description_de": "Laminat durchfeuchtet, Blasen > 15mm, Laminat delaminiert",
                "severity": "high",
                "structural_impact": "moderate — Festigkeitsverlust bis 30%",
                "repair_complexity": "complex",
                "cost_estimate": "€10.000-€20.000",
                "method": "Laminat-Sanierung: Gelcoat + beschädigtes Laminat entfernen, Trocknung, Neulaminierung mit Epoxid"
            },
            "stage_4_critical": {
                "description_de": "Fortgeschrittene Hydrolyse, Laminat brüchig, Strukturversagen möglich",
                "severity": "critical",
                "structural_impact": "severe — Boot ggf. wirtschaftlicher Totalschaden",
                "repair_complexity": "major_rebuild",
                "cost_estimate": "€20.000-€50.000+",
                "method": "Unter Umständen nicht mehr wirtschaftlich reparierbar"
            }
        },
        "risk_factors": {
            "resin_type": {
                "orthophthalic_polyester": "Höchstes Risiko — Standard bei Serienbooten vor 2000",
                "isophthalic_polyester": "Mittleres Risiko — bessere Wasserbeständigkeit",
                "vinylester": "Niedriges Risiko — hervorragend wasserdicht",
                "epoxy": "Sehr niedriges Risiko — quasi osmosefrei"
            },
            "water_temperature": {
                "tropical_28plus": "Risiko 3x höher als in nordischen Gewässern",
                "mediterranean_20_28": "Risiko 2x höher als in nordischen Gewässern",
                "nordic_under_20": "Basis-Risiko",
                "note_de": "Temperatur ist der stärkste Beschleunigungsfaktor"
            },
            "builder_quality": {
                "description_de": "Verarbeitungsqualität entscheidet über Osmoserisiko",
                "factors": [
                    "Lufteinschlüsse im Laminat erhöhen Risiko massiv",
                    "Unvollständige Aushärtung = mehr lösliche Bestandteile",
                    "Gelcoat-Dicke < 0.5mm = unzureichender Schutz",
                    "Gelcoat-Dicke optimal: 0.6-0.8mm"
                ]
            }
        },
        "prevention": {
            "new_boat": "Epoxid-Sperrschicht (min. 6 Lagen, 350µm trocken) vor erstem Einwässern",
            "existing_boat": "Jährliche Feuchtemessung nach dem Kranen",
            "coppercoat_note": "Coppercoat-Epoxid-Antifouling bietet gleichzeitig Osmoseschutz",
            "storage": "Winterlager an Land reduziert Risiko deutlich"
        },
        "repair_drying": {
            "description_de": "Trocknungszeiten sind der kritischste Faktor bei der Osmosesanierung",
            "natural_drying": "6-12 Monate an Land in überdachtem Bereich",
            "forced_drying": "2-4 Monate bei 40°C mit Infrarot-Heizplatten",
            "moisture_target": "< 6% Restfeuchte vor Neubeschichtung",
            "measurement": "Messung mit kalibrierten Feuchtemessgerät (Tramex)",
            "common_error_de": "Häufigster Fehler: Zu früh beschichtet — Feuchtigkeit eingeschlossen"
        }
    },
    "detection_methods": {
        "source": ["yacht", "bootsprofis", "nauticare"],
        "description_de": "Methoden zur Osmose-Erkennung und Diagnose",
        "methods": [
            {
                "method": "Feuchtemessung (Moisture Meter)",
                "tool": "Tramex Skipper Plus oder Sovereign Moisturemeter",
                "procedure_de": "Boot mindestens 2 Wochen nach Kranen trocknen lassen. Systematische Messung in Rasterform (50cm Abstand). Immer gleicher Anpressdruck.",
                "thresholds": {
                    "acceptable": "< 15% relative Feuchte",
                    "investigation_needed": "15-25% — weitere Untersuchung",
                    "osmosis_likely": "> 25% — Osmose wahrscheinlich",
                    "critical": "> 35% — schwere Durchfeuchtung"
                },
                "note_de": "Messwerte sind RELATIV, nicht absolut. Immer Vergleichsmessung an bekannt trockener Stelle."
            },
            {
                "method": "UV-Licht-Test (Fluoreszenztest)",
                "tool": "UV-Prüflampe (365nm Wellenlänge)",
                "procedure_de": "Gelcoat anschleifen (sauber, trocken). UV-Lampe im abgedunkelten Bereich auf Oberfläche richten. Osmose-Ester fluoreszieren als dunkle Flecken.",
                "advantage_de": "Erkennt Osmose BEVOR Blasen sichtbar sind — Früherkennung!",
                "source": "yacht (Osmose-Spezial Teil 2)"
            },
            {
                "method": "Blasen-Stichprobe",
                "tool": "Spitzes Teppichmesser oder Stechbeitel-Ecke",
                "procedure_de": "Blase aufstechen, Flüssigkeit auffangen. Geruchstest: stechend-sauer = Essigsäure = Osmose. Farbtest: gelblich-braun = fortgeschritten.",
                "timing_de": "Optimaler Testzeitpunkt: Herbst nach 6 Monaten im Wasser (Blasen auf Maximum)",
                "source": "yacht (Osmose-Spezial)"
            },
            {
                "method": "Klopftest (Tap Test)",
                "tool": "Gummihammer oder Münze",
                "procedure_de": "Systematisch über Rumpf/Deck klopfen. Gesundes Laminat = heller Klang. Delamination/Feuchtigkeit = dumpfer, hohler Klang.",
                "limitation_de": "Nur grobe Einschätzung, nicht quantitativ",
                "source": "bootsprofis"
            },
            {
                "method": "Roto-Blast / Sandstrahltest",
                "tool": "Roto-Blast Gerät",
                "procedure_de": "Gelcoat-Oberfläche wird kontrolliert abgetragen. Ermöglicht Sichtprüfung des darunterliegenden Laminats.",
                "source": "yacht"
            }
        ]
    }
}


# ============================================================================
# RIGG-EXPERTISE — Rigging Knowledge from Experts
# Source: Blauwasser.de, Pantaenius, VBS, Schultz-Segel
# ============================================================================

RIGGING_EXPERT_KNOWLEDGE: Dict[str, Any] = {
    "standing_rigging_lifespan": {
        "source": ["blauwasser", "pantaenius", "vbs"],
        "description_de": "Lebensdauer und Inspektionsintervalle für stehendes Gut",
        "wire_1x19": {
            "material": "1x19 Edelstahldraht (V4A / 316)",
            "lifespan_years": "12-15 Jahre",
            "lifespan_nm": "ca. 20.000 sm",
            "inspection_interval": "Jährlich ab Jahr 8",
            "failure_mode": "Ermüdungsbruch einzelner Drähte, Korrosion an Terminals",
            "check_method": "Finger entlangfahren — gebrochener Draht bildet Knubbel",
            "insurance_requirement": "Versicherungen verlangen Erneuerung nach 10-15 Jahren"
        },
        "rod_rigging": {
            "material": "Nitronic 50 / Dyform Rod",
            "lifespan_years": "15-20 Jahre",
            "lifespan_nm": "ca. 30.000 sm",
            "inspection_interval": "Jährlich ab Jahr 10",
            "failure_mode": "Ermüdungsriss am Endstück-Übergang (Head)",
            "check_method": "Farbeindringprüfung (Dye Penetrant) an Köpfen",
            "note_de": "Rod versagt plötzlich ohne Vorwarnung — Draht warnt durch Einzeldrahtbrüche"
        },
        "textile_rigging": {
            "material": "Dyneema / PBO",
            "lifespan_years": "8-12 Jahre (Dyneema), 5-8 Jahre (PBO mit UV-Schutz)",
            "inspection_interval": "Jährlich",
            "failure_mode": "UV-Degradation, Kriechen (Creep) bei Dauerbelastung",
            "check_method": "Sichtkontrolle auf Verfärbung, Durchmesserveränderung",
            "note_de": "PBO muss zwingend UV-geschützt werden (Mantel), Dyneema kriecht unter Last"
        },
        "common_failure_points": [
            {
                "location": "Terminal/Want-Übergang (Pressung/Walzterminal)",
                "failure_de": "Haarrisse in Pressterminals — häufigste Versagensursache",
                "check": "Lupe, Farbeindringprüfung",
                "source": "pantaenius"
            },
            {
                "location": "Wantenspanner (Turnbuckle)",
                "failure_de": "Korrosion im Gewinde, besonders bei seltenem Nachstellen",
                "check": "Gangbarkeit prüfen, Korrosion im Gewindegang",
                "source": "blauwasser"
            },
            {
                "location": "Mastfuß / Decksbereich",
                "failure_de": "Wasseransammlung am Mastfuß führt zu Korrosion der Wantenrollen",
                "check": "Drainage prüfen, Mastmanschette kontrollieren",
                "source": "bootsprofis"
            },
            {
                "location": "Salinge (Spreaders)",
                "failure_de": "Risse an Salingumdrehungen/Winkelstücken durch Dauerbelastung",
                "check": "Sichtkontrolle auf Verformung und Risse",
                "source": "vbs"
            },
            {
                "location": "Wantdurchführung (Chainplate)",
                "failure_de": "Wassereinbruch am Deck-Durchgang, Korrosion von innen nicht sichtbar",
                "check": "Von innen und außen prüfen, Dichtigkeit",
                "source": "blauwasser"
            }
        ]
    },

    "rigg_loss_causes": {
        "source": ["pantaenius", "blauwasser"],
        "description_de": "Häufigste Ursachen für Riggverlust (Demasting)",
        "causes": [
            {
                "cause": "Ermüdungsversagen am Terminal",
                "frequency": "35% aller Riggverluste",
                "prevention": "Regelmäßige Inspektion + rechtzeitige Erneuerung"
            },
            {
                "cause": "Fehlende Wartung des stehenden Guts",
                "frequency": "25%",
                "prevention": "Jährliche Rigg-Inspektion durch Fachmann"
            },
            {
                "cause": "Überlastung durch falsches Segeln (zu viel Tuch bei zu viel Wind)",
                "frequency": "20%",
                "prevention": "Rechtzeitig reffen, Trimm beachten"
            },
            {
                "cause": "Korrosion durch mangelnde Wasserabführung",
                "frequency": "10%",
                "prevention": "Drainage an Mastfuß, Wantenverbindungen kontrollieren"
            },
            {
                "cause": "Materialfehler / Produktionsfehler",
                "frequency": "5%",
                "prevention": "Renommierte Rigg-Hersteller verwenden"
            },
            {
                "cause": "Kollision / Grundberührung",
                "frequency": "5%",
                "prevention": "Seemannschaft"
            }
        ]
    },
    "pantaenius_damage_statistics": {
        "source": ["pantaenius"],
        "description_de": "Rigg-Schadensstatistik aus Versicherungsdaten (Pantaenius, 3-Jahres-Zeitraum)",
        "total_mast_failures": 500,
        "period": "3 Jahre",
        "typical_cost_42ft": {
            "range": "30.000-100.000 EUR",
            "includes": "Mastprofil, stehendes Gut, alle Segel, Deckschäden, Elektronik",
            "note_de": "Kann bei älteren Booten zum wirtschaftlichen Totalschaden führen"
        },
        "common_failure_areas": [
            {
                "area": "Halteplatten und Befestigungen",
                "failure_de": "Platten verschieben oder kippen sich. Rissbildung und Muldenverformung sichtbar."
            },
            {
                "area": "Bolzen und Stifte",
                "failure_de": "Bolzen/Stifte zu klein oder falsch dimensioniert. Beschädigung an Bolzensitzen, Terminalverformung, Lümmelbeschlag-Probleme."
            },
            {
                "area": "Draht und Splinte",
                "failure_de": "Splinte dürfen NICHT wiederverwendet werden. Materialfestigkeit nimmt bei wiederholtem Biegen ab."
            },
            {
                "area": "Mastprofil",
                "failure_de": "Haarrisse am Mastfuß, Kerben, Dellen, starke Korrosion beeinträchtigen die Festigkeit."
            }
        ],
        "rigg_check_tools": {
            "spinlock_rig_sense_pro": {
                "description_de": "Misst Wantenspannung bis 8 Tonnen",
                "use": "Präzise Einstellung der Riggspannung",
                "cost": "ca. 350 EUR"
            },
            "zollstock_methode": {
                "description_de": "Einfache Methode mit Zollstock zur Riggspannungs-Kontrolle",
                "cost": "0 EUR"
            },
            "dye_penetrant": {
                "description_de": "Farbeindringprüfung für Risse an Terminals und Köpfen",
                "use": "Rod-Rigging-Inspektion, Pressverbindungen",
                "cost": "ca. 30-50 EUR pro Set"
            }
        }
    }
}


# ============================================================================
# SEEVENTIL-EXPERTISE — Seacock Knowledge from Forums and Experts
# Source: boote-forum.de, segeln-forum.de, float Magazin, Marietim
# ============================================================================

SEACOCK_EXPERT_KNOWLEDGE: Dict[str, Any] = {
    "material_comparison": {
        "source": ["boote_forum", "segeln_forum", "float_magazin", "marietim"],
        "description_de": "Materialvergleich für Seeventile und Borddurchlässe",
        "materials": {
            "bronze_din_1705": {
                "name_de": "Rotguss / Bronze (CuSn7ZnPb / CC491K)",
                "suitable": True,
                "lifespan_years": "30-50 Jahre",
                "dezincification_risk": "none",
                "galvanic_note": "Verträglich mit Edelstahl und GFK",
                "cost": "hoch",
                "maintenance": "Jährlich Gangbarkeit prüfen, ggf. Fett nachsetzen",
                "note_de": "Goldstandard für Seewasseranwendungen. Schwere Qualität erkennbar am Gewicht."
            },
            "brass_standard": {
                "name_de": "Messing (CuZn37 / Standard)",
                "suitable": False,
                "lifespan_years": "3-15 Jahre (je nach Salzgehalt)",
                "dezincification_risk": "CRITICAL — Zink wird im Salzwasser herausgelöst",
                "galvanic_note": "Vorsicht bei Kombination mit Edelstahl (verstärkt Korrosion)",
                "cost": "niedrig",
                "failure_description_de": "Material wird porös, bröckelig, kupferfarben. Kann ohne Vorwarnung brechen.",
                "note_de": "NIEMALS für Unterwasser-Borddurchlässe verwenden! Lebensgefährlich."
            },
            "brass_dzr": {
                "name_de": "DZR-Messing (Entzinkungsbeständig, CW602N)",
                "suitable": True,
                "lifespan_years": "15-25 Jahre",
                "dezincification_risk": "very_low",
                "galvanic_note": "Besser als Standard-Messing, nicht so gut wie Bronze",
                "cost": "mittel",
                "note_de": "Guter Kompromiss. DZR-Kennzeichnung auf dem Bauteil prüfen."
            },
            "stainless_316": {
                "name_de": "Edelstahl V4A (1.4404 / 316L)",
                "suitable": "conditional",
                "lifespan_years": "20-40 Jahre (wenn belüftet)",
                "dezincification_risk": "none",
                "galvanic_note": "Kann bei Sauerstoffmangel Spaltkorrosion entwickeln",
                "cost": "mittel-hoch",
                "failure_description_de": "Spaltkorrosion in schlecht belüfteten Bereichen (z.B. GFK-eingebettet)",
                "note_de": "Nur mit korrekter Installation und Belüftung geeignet."
            },
            "composite_trudesign": {
                "name_de": "Glasfaserverstärktes Polyamid (TruDesign / Forespar Marelon)",
                "suitable": True,
                "lifespan_years": "Theoretisch unbegrenzt (keine Korrosion)",
                "dezincification_risk": "none",
                "galvanic_note": "Komplett galvanisch neutral — keine Korrosionsprobleme",
                "cost": "mittel",
                "note_de": "Zunehmend Standard bei Neubauten. Kein Bewuchs durch Kupferabgabe."
            }
        },
        "inspection_guidelines": {
            "annual": [
                "Gangbarkeit aller Seeventile prüfen (auf- und zudrehen)",
                "Sichtprüfung auf Verfärbung (Kupferfarbe = Entzinkung)",
                "Schlauchschellen: Doppelschellen auf Wasserleitung-Seite",
                "Schlauchzustand: Risse, Verhärtung, Quetschstellen"
            ],
            "five_yearly": [
                "Seeventile ausbauen und Material prüfen",
                "Borddurchlass-Dichtung (Lanolin/Teflon) erneuern",
                "Schläuche komplett erneuern wenn verhärtet"
            ],
            "critical_rule_de": "Jedes Seeventil muss innerhalb von Sekunden erreichbar und bedienbar sein. Holzpfropfen bei jedem Durchlass griffbereit!"
        }
    }
}


# ============================================================================
# MOTOR-EXPERTISE — Engine Knowledge from Forums and Experts
# Source: no-frills-sailing, bootsprofis, boote-forum
# ============================================================================

ENGINE_EXPERT_KNOWLEDGE: Dict[str, Any] = {
    "common_problems_by_brand": {
        "source": ["boote_forum", "no_frills_sailing", "bootsprofis"],
        "volvo_penta": {
            "known_issues": [
                {
                    "model_range": "MD2000-Serie (MD2010, MD2020, MD2030, MD2040)",
                    "issue_de": "Berüchtigte Serie mit häufigen Defekten",
                    "problems": [
                        "Elektrik-Probleme: Korrodierte Stecker und Kabelschuhe",
                        "Dichtungsversagen: Öl-Leckagen an diversen Stellen",
                        "Impeller-Pumpe: Gehäusekorrosion, häufiger Wechsel nötig",
                        "Saildrive-Dichtung: Leckt nach 5-8 Jahren, teurer Austausch",
                        "Thermostaten bleiben hängen — Überhitzungsgefahr"
                    ],
                    "note_de": "Die 2000er Serie gilt als schlechteste VP-Serie für Segelboote"
                },
                {
                    "model_range": "D1/D2-Serie (D1-13, D1-20, D1-30, D2-40, D2-55, D2-75)",
                    "issue_de": "Deutlich besser als Vorgänger, aber nicht problemfrei",
                    "problems": [
                        "Saildrive 130S: Membran muss alle 7 Jahre getauscht werden (€600-€1200)",
                        "Kühlwasserpumpe: Impeller-Wechsel alle 200h oder jährlich",
                        "Abgas-Elbow: Korrodiert nach 5-8 Jahren (€300-€600)",
                        "Kraftstofffilter verstopft bei Algenbildung im Tank"
                    ]
                }
            ],
            "maintenance_costs_de": "VP-Teile ca. 30-50% teurer als Yanmar-Pendants",
            "parts_availability": "Gut weltweit, aber teuer",
            "service_network": "Exzellent in Europa, gut weltweit"
        },
        "yanmar": {
            "known_issues": [
                {
                    "model_range": "1GM/2GM/3GM-Serie",
                    "issue_de": "Zuverlässige Klassiker mit überschaubaren Problemen",
                    "problems": [
                        "Rohwasserpumpe: Impeller-Wechsel regelmäßig nötig",
                        "Motorlager verhärten nach 10-15 Jahren",
                        "Auspuff-Wassersammler kann korrodieren",
                        "Einspritzpumpe bei sehr hohen Laufstunden (>5000h)"
                    ]
                },
                {
                    "model_range": "3JH/4JH-Serie (aktuell)",
                    "issue_de": "Aktuelle Generation, sehr zuverlässig",
                    "problems": [
                        "Saildrive SD60: Ähnliche Membran-Thematik wie VP",
                        "Elektronik-Steuerung empfindlich gegen Feuchtigkeit",
                        "Turbolader (bei Turbo-Versionen) braucht Warmfahren/Abkühlung"
                    ]
                }
            ],
            "maintenance_costs_de": "Günstiger als Volvo Penta, Teile gut verfügbar",
            "parts_availability": "Sehr gut weltweit, besonders in Asien",
            "service_network": "Gut, breites Händlernetz"
        },
        "beta_marine": {
            "known_issues": [
                {
                    "model_range": "Beta 14-50 (Kubota-Basis)",
                    "issue_de": "Solide Industriemotoren als Bootsantrieb",
                    "problems": [
                        "Marinisierung manchmal nicht perfekt: Wärmetauscher zu klein",
                        "Ersatzteile: Kubota-Teile günstig, Beta-spezifische teurer",
                        "Anlasser-Magnetschalter bei Feuchtigkeit störanfällig"
                    ]
                }
            ],
            "maintenance_costs_de": "Am günstigsten der drei, Kubota-Teile weltweit verfügbar",
            "parts_availability": "Kubota-Teile überall, spezifische Marineteile schwieriger",
            "service_network": "Begrenzt, aber Kubota-Werkstätten können helfen"
        }
    },

    "maintenance_golden_rules": {
        "source": ["bootsprofis", "blauwasser", "boote_forum"],
        "description_de": "Goldene Regeln der Bootsdiesel-Wartung",
        "rules": [
            {
                "rule_de": "Motor einmal pro Woche unter Last laufen lassen",
                "detail_de": "Mindestens 30 Minuten bei 70-80% Drehzahl — verhindert Verglasung der Zylinder und Sulfatierung"
            },
            {
                "rule_de": "Impeller jedes Frühjahr wechseln, auch wenn er gut aussieht",
                "detail_de": "Trockener Impeller bricht beim ersten Start und Stücke verstopfen den Wärmetauscher"
            },
            {
                "rule_de": "Ölwechsel alle 100-150h ODER jährlich (was zuerst kommt)",
                "detail_de": "Auch Boote mit wenig Motorstunden brauchen jährlichen Ölwechsel — Feuchtigkeit im Öl"
            },
            {
                "rule_de": "Dieselfilter immer doppelt (Vorfilter + Feinfilter)",
                "detail_de": "Racor-Vorfilter mit Wasserabscheider als Standard. Ersatzfilter an Bord!"
            },
            {
                "rule_de": "Kühlwasser nie mit normalem Leitungswasser mischen",
                "detail_de": "Immer destilliertes Wasser + Korrosionsschutzmittel verwenden"
            },
            {
                "rule_de": "Zinkanode am Motor/Saildrive jedes Jahr prüfen",
                "detail_de": "Wenn > 50% aufgebraucht: sofort wechseln. Aufgebrauchte Anoden = ungeschützter Motor"
            },
            {
                "rule_de": "Getriebe-Ölstand regelmäßig prüfen",
                "detail_de": "Milchiges Öl = Wassereinbruch = Dichtung defekt → sofort handeln"
            }
        ]
    }
}


# ============================================================================
# TEAKDECK-EXPERTISE — Teak Deck Knowledge from Forums
# Source: segeln-forum, boote-forum, yacht-forum, frag-jochen.de
# ============================================================================

TEAK_DECK_EXPERT_KNOWLEDGE: Dict[str, Any] = {
    "common_problems": {
        "source": ["segeln_forum", "boote_forum", "yacht_forum"],
        "description_de": "Häufige Teakdeck-Probleme und ihre Ursachen",
        "problems": [
            {
                "problem_de": "Fugen lösen sich (Dreiflankenhaftung)",
                "mechanism_de": "Sikaflex haftet an Boden UND beiden Seitenflanken. Spannung bei Holzquellen/Schwinden reißt Fuge von den Flanken ab.",
                "prevention": "Bond-Breaker (PE-Band) am Fugengrund verwenden — nur Zweiflanken-Haftung!",
                "repair": "Alte Fuge komplett entfernen, Flanken reinigen, Bond-Breaker einlegen, neu verfugen",
                "source": "frag-jochen"
            },
            {
                "problem_de": "Deck undicht — Wasser unter dem Teak",
                "mechanism_de": "Schrauben/Nägel zur Befestigung durchdringen GFK-Deck. Bei Fugenversagen sickert Wasser über Schraubenlöcher ins Sandwich/Kernmaterial.",
                "consequence_de": "Sandwichkern wird feucht → Kernfäule (bei Balsa) → Delamination → strukturelle Schwächung",
                "prevention": "Jede Befestigung mit Sikaflex/Epoxid abdichten",
                "repair_cost": "€15.000-€40.000 bei Komplettsanierung",
                "source": "segeln_forum"
            },
            {
                "problem_de": "Teak zu dünn geschliffen",
                "mechanism_de": "Eigentümer schleifen Deck jährlich → nach 15-20 Jahren sind Planken auf < 5mm → Schraubenköpfe werden sichtbar",
                "minimum_thickness": "6mm Plankendicke als Minimum",
                "original_thickness": "8-10mm bei Neubau",
                "note_de": "Teak NICHT schleifen, nur mit Seifenwasser reinigen!",
                "source": "bootsprofis"
            },
            {
                "problem_de": "Sikaflex verflüssigt sich / wird klebrig",
                "mechanism_de": "UV-Strahlung + Hitze lassen altes Sikaflex 290DC/298 weich werden",
                "solution_de": "Komplett entfernen und mit neuem Material verfugen",
                "alternative_products": [
                    "Sikaflex 290i DC (aktuell)",
                    "Saba Deck Caulk (primerlos)",
                    "MSR MS1000 Marine (primerlos)",
                    "WKT Marine Caulk"
                ],
                "source": "yacht_forum"
            }
        ]
    },

    "teak_alternatives": {
        "source": ["yacht_tv", "float_magazin"],
        "description_de": "Alternativen zum traditionellen Teakdeck",
        "alternatives": [
            {
                "material": "Flexiteek / Synthetic Teak",
                "description_de": "PVC-basiertes synthetisches Teak",
                "lifespan": "10-15 Jahre",
                "cost_vs_teak": "60-70% der Teak-Kosten",
                "pros": ["Kein Fugen-Problem", "Rutschfest", "Geringes Gewicht", "Umweltfreundlicher"],
                "cons": ["Wird heiß in der Sonne", "Nicht reparierbar", "Optik nicht identisch"],
                "brands": ["Flexiteek", "Esthec", "Bolidt", "Permateek", "Tek-Dek"]
            },
            {
                "material": "Cork Composite",
                "description_de": "Kork-Verbundwerkstoff als Decksbelag",
                "lifespan": "15-20 Jahre",
                "cost_vs_teak": "80% der Teak-Kosten",
                "pros": ["Hervorragende Dämmung", "Rutschfest nass/trocken", "Bleibt kühl", "Leicht"],
                "cons": ["Empfindlicher gegen mechanische Beschädigung", "Weniger traditionelle Optik"],
                "brands": ["Marinedeck", "SeaCorkClassic"]
            }
        ]
    }
}


# ============================================================================
# ELEKTRIK-EXPERTISE — Electrical Expert Knowledge
# Source: segeln-forum, Victron Energy, bootstechnik.de, Mastervolt
# ============================================================================

ELECTRICAL_EXPERT_KNOWLEDGE: Dict[str, Any] = {
    "galvanic_corrosion_shore_power": {
        "source": ["segeln_forum", "victron", "bootstechnik", "mastervolt"],
        "description_de": "Galvanische Korrosion durch Landstrom — das unterschätzte Problem",
        "mechanism": {
            "description_de": "Wenn das Boot am Landstrom hängt, wird der Schutzleiter (PE) mit dem Bootskörper verbunden. Über den Schutzleiter entsteht eine galvanische Verbindung zu anderen Booten und der Steginfrastruktur (Stahlspundwand).",
            "consequence_de": "Unterwassermetalle (Propeller, Welle, Saildrive, Kiel) werden unkontrolliert als Opferanode aufgelöst",
            "typical_damage": [
                "Propeller-Korrosion (rosa Verfärbung bei Bronze)",
                "Saildrive-Gehäuse-Auflösung",
                "Kiel-Korrosion (bei Gusseisen)",
                "Wellendichtung-Zerstörung",
                "Zinkanoden überraschend schnell aufgebraucht"
            ]
        },
        "solutions": [
            {
                "solution": "Trenntransformator (Isolation Transformer)",
                "description_de": "Galvanische Trennung zwischen Landnetz und Bordnetz",
                "effectiveness": "100% Schutz",
                "cost": "€800-€2.500 je nach Leistung",
                "brands": ["Victron", "Mastervolt", "Philippi"],
                "note_de": "Beste Lösung, insbesondere für Dauerlieger"
            },
            {
                "solution": "Galvanischer Isolator (Galvanic Isolator)",
                "description_de": "Sperrt galvanische Gleichströme, lässt Schutzleiter-Funktion für Wechselstrom bestehen",
                "effectiveness": "80-90% Schutz",
                "cost": "€100-€400",
                "brands": ["Victron", "Sterling Power", "ProMariner"],
                "note_de": "Preiswertere Alternative zum Trenntrafo, aber nicht so zuverlässig"
            },
            {
                "solution": "Landstrom nur zum Laden, dann trennen",
                "description_de": "Boot nicht dauerhaft am Landstrom lassen",
                "effectiveness": "Reduziert Expositionszeit",
                "cost": "€0",
                "note_de": "Praktisch oft schwierig durchzusetzen"
            }
        ]
    },

    "stray_current": {
        "source": ["segeln_forum", "gmm_yacht"],
        "description_de": "Kriechstrom / Streustrom — verursacht massive Korrosion",
        "mechanism_de": "Fehlerhafte Isolierung oder beschädigte Kabel lassen DC-Strom durch Seewasser fließen. Selbst Milliampere verursachen rapide Korrosion (schlimmer als galvanische Korrosion).",
        "signs": [
            "Zinkanoden extrem schnell aufgebraucht (Wochen statt Monate)",
            "Sichtbare Korrosion an Unterwassermetallen",
            "Blasenbildung an metallischen Oberflächen",
            "Metallischer Geschmack im Wasser um das Boot"
        ],
        "diagnosis": {
            "step_1": "Alle Verbraucher ausschalten",
            "step_2": "Multimeter (DC mA) zwischen Minuspol Batterie und Masse",
            "step_3": "Kriechstrom messen — akzeptabel: < 10mA, kritisch: > 50mA",
            "step_4": "Sicherungen einzeln entfernen um Quelle zu finden"
        },
        "prevention": [
            "Korrekte 2-Leiter-Verkabelung (kein Rumpf als Rückleiter!)",
            "Regelmäßige Isolationsmessung der Bordverkabelung",
            "Kabelschuhe crimpen UND löten, Schrumpfschlauch",
            "Marine-Grade Kabel mit Verzinnung verwenden"
        ]
    },

    "battery_sizing_real_world": {
        "source": ["blauwasser", "bootsprofis"],
        "description_de": "Praxiswissen zur Batterie-Dimensionierung",
        "rules_of_thumb": [
            {
                "rule": "Verbrauchs-Batteriebank = 3x täglicher Verbrauch",
                "detail": "Bei 100Ah täglichem Verbrauch → 300Ah Blei-Säure (50% DoD) oder 150Ah LiFePO4 (80% DoD)"
            },
            {
                "rule": "Starterbatterie IMMER separate Bank",
                "detail": "Mindestens 1x CCA-Anforderung des Motors. Nie die Starterbatterie für Verbraucher nutzen."
            },
            {
                "rule": "LiFePO4-Umstieg lohnt ab 200Ah Bankgröße",
                "detail": "Gewichtsersparnis + nutzbare Kapazität kompensieren den höheren Preis"
            },
            {
                "rule": "Ladegerät = 15-25% der Bankkapazität",
                "detail": "Bei 300Ah Bank → 50-75A Ladegerät optimal"
            }
        ]
    }
}


# ============================================================================
# ANTIFOULING-EXPERTISE — Antifouling Knowledge
# Source: SVB, float Magazin, segeln-forum, boote-forum
# ============================================================================

ANTIFOULING_EXPERT_KNOWLEDGE: Dict[str, Any] = {
    "types_comparison": {
        "source": ["svb", "float_magazin", "boote_forum"],
        "description_de": "Antifouling-Typen im Vergleich",
        "types": {
            "self_polishing": {
                "name_de": "Selbstpolierendes Antifouling (SPC)",
                "mechanism_de": "Biozid wird kontinuierlich freigesetzt, Oberfläche erneuert sich durch Wasserbewegung",
                "lifespan": "1-2 Saisons",
                "best_for": "Segelboote (Bewegung nötig), Regatta",
                "drawback": "Bei Dauer-Liegern weniger effektiv",
                "brands": ["International Micron Extra", "Hempel Mille Xtra", "Jotun SeaQuantum"],
                "cost_per_season": "€200-€400 (für 35ft)"
            },
            "hard_matrix": {
                "name_de": "Hart-Matrix Antifouling",
                "mechanism_de": "Biozid in harter Farbschicht eingebettet, wird langsam ausgelaugt",
                "lifespan": "1 Saison",
                "best_for": "Trailboote, häufig aus dem Wasser",
                "drawback": "Schichtaufbau über Jahre, muss irgendwann ab",
                "brands": ["International Cruiser One", "Hempel Hard Racing"],
                "cost_per_season": "€150-€300"
            },
            "coppercoat_epoxy": {
                "name_de": "Kupfer-Epoxid (Coppercoat)",
                "mechanism_de": "Kupferpulver in Epoxidharz — Kupferoxid-Schicht bildet sich natürlich",
                "lifespan": "10-15 Jahre",
                "best_for": "Langfahrtsegler, Dauerlieger",
                "drawback": "Hohe Einmalkosten, aufwändige Applikation, erstes Jahr mäßig",
                "cost_initial": "€1.400-€2.500 (Material) + €1.000-€2.000 (Applikation)",
                "cost_per_year_amortized": "€150-€300",
                "note_de": "Polarisiert: Fans schwören darauf, Kritiker bemängeln erstes Jahr. Applikationsqualität entscheidend.",
                "application_rules": [
                    "Schichten nass-in-nass auftragen (nicht durchtrocknen lassen)",
                    "Mindestens 4 Schichten",
                    "Temperatur 15-25°C, Luftfeuchtigkeit < 80%",
                    "Oberfläche muss absolut trocken und fettfrei sein",
                    "Im ersten Jahr regelmäßig tauchen/reinigen — Kupferoxid muss sich erst bilden"
                ]
            },
            "ultrasonic": {
                "name_de": "Ultraschall-Antifouling",
                "mechanism_de": "Ultraschallwellen verhindern Ansatz von Mikroorganismen",
                "lifespan": "Unbegrenzt (Transducer 5-10 Jahre)",
                "best_for": "Zusätzlich zu konventionellem AF, besonders an Welle/Propeller",
                "drawback": "Als alleiniger Schutz unzureichend, besonders in warmen Gewässern",
                "cost": "€500-€3.000",
                "note_de": "Ergänzung, kein Ersatz für konventionelles Antifouling"
            }
        }
    },

    "environmental_regulations": {
        "source": ["adac_skipper", "svb"],
        "description_de": "Umweltvorschriften für Antifouling",
        "regulations": [
            {
                "region": "EU / Deutschland",
                "rules": [
                    "TBT (Tributylzinn) seit 2003 weltweit verboten (IMO AFS Convention)",
                    "Kupfer-basierte AF erlaubt, aber in einigen Binnengewässern eingeschränkt",
                    "In den Niederlanden strengere Kupfer-Grenzwerte",
                    "Schweden: Kupfer-AF in Ostsee stark eingeschränkt"
                ]
            },
            {
                "region": "Ostsee",
                "rules": [
                    "Brackwasser = geringerer Bewuchs, weniger AF nötig",
                    "Schweden/Finnland: Kupfer-Grenzwert 8.3µg Cu/cm²/Tag",
                    "Empfehlung: Hart-Matrix oder biozidfreie Alternativen"
                ]
            }
        ]
    }
}


# ============================================================================
# SANDWICH/GFK-EXPERTISE — Composite Repair Knowledge
# Source: yacht.de, NautiCare, boote-forum, segeln-forum
# ============================================================================

COMPOSITE_EXPERT_KNOWLEDGE: Dict[str, Any] = {
    "sandwich_core_problems": {
        "source": ["yacht", "boote_forum", "segeln_forum"],
        "description_de": "Sandwich-Kern-Probleme und ihre Behebung",
        "core_types_risk": {
            "endgrain_balsa": {
                "rot_risk": "HIGH",
                "moisture_absorption": "Sehr hoch wenn Wasser eindringt",
                "failure_mode_de": "Balsa saugt Wasser auf wie ein Schwamm, fault, wird zu Brei",
                "detection": "Soft Spots bei Drucktest, Feuchtemessung erhöht",
                "repair_complexity": "Hoch — betroffener Bereich muss ausgeschnitten und ersetzt werden",
                "note_de": "JEDE Durchbohrung von Balsa-Sandwich muss mit Epoxid versiegelt werden!"
            },
            "pvc_closed_cell": {
                "rot_risk": "LOW",
                "moisture_absorption": "Sehr gering (geschlossene Zellen)",
                "failure_mode_de": "Delamination von Kern und Deckschicht, Scherversagen unter Last",
                "detection": "Klopftest (dumpfer Klang = Delamination), Ultraschall",
                "note_de": "Deutlich feuchtigkeitsresistenter als Balsa, aber teurer"
            },
            "san_foam": {
                "rot_risk": "VERY_LOW",
                "moisture_absorption": "Minimal",
                "failure_mode_de": "Ähnlich PVC, etwas bessere Schersteifigkeit",
                "note_de": "Premium-Alternative, z.B. Gurit Corecell"
            }
        },
        "repair_methods": [
            {
                "method": "Injektionsverfahren (kleine Delamination)",
                "steps_de": [
                    "5-6mm Löcher in obere Deckschicht bohren (Raster 50mm)",
                    "Epoxidharz mit Spritzen injizieren bis es aus Nachbarlöchern austritt",
                    "Folie auflegen und mit Gewichten belasten (Vakuum ideal)",
                    "24h aushärten lassen",
                    "Löcher mit Gelcoat verschließen"
                ],
                "resin": "Epoxid (BK) — kein Polyester (schwindet beim Aushärten)",
                "suitable_for": "Delamination < 0.5m², Kern intakt"
            },
            {
                "method": "Kern-Austausch (großflächige Schäden)",
                "steps_de": [
                    "Obere Deckschicht in betroffenem Bereich entfernen",
                    "Nassen/faulen Kern komplett ausräumen",
                    "Fläche trocknen (Wochen bei Balsa-Fäule)",
                    "Neuen Kern einsetzen (PVC/SAN empfohlen als Ersatz für Balsa)",
                    "Obere Laminatschicht neu aufbauen (Epoxid + Glasfaser)",
                    "Schleifen, Gelcoat, Finish"
                ],
                "suitable_for": "Großflächige Kernfäule, strukturelle Bereiche"
            }
        ]
    },

    "grp_gelcoat_damage": {
        "source": ["nauticare", "yacht"],
        "description_de": "GFK-Gelcoat-Schäden und Reparatur",
        "damage_types": [
            {
                "type": "Crazing (Haarrisse)",
                "cause_de": "UV-Alterung, Flexbewegung, Schlag",
                "severity": "cosmetic bis minor",
                "repair": "Schleifen, Epoxid-Spachtel, Gelcoat nachspritzen"
            },
            {
                "type": "Star Cracks (Sternrisse)",
                "cause_de": "Punktueller Schlag (Dalbenberührung, Fenderauge)",
                "severity": "minor — Wassereintrittspfad",
                "repair": "V-förmig ausschleifen, Epoxid füllen, Gelcoat"
            },
            {
                "type": "Print-Through (Faserabbild)",
                "cause_de": "UV-Schrumpfung des Gelcoats macht Faserstruktur sichtbar",
                "severity": "cosmetic",
                "repair": "Schleifen und Neugelcoat — oder akzeptieren"
            },
            {
                "type": "Chalking (Kreidung)",
                "cause_de": "UV-Degradation der Gelcoat-Oberfläche",
                "severity": "cosmetic",
                "repair": "Polieren (Rubbing Compound), ggf. Neugelcoat bei starker Kreidung"
            }
        ]
    }
}


# ============================================================================
# WINTERLAGER-EXPERTISE — Winterization Knowledge
# Source: blauwasser, svb, palstek
# ============================================================================

WINTERIZATION_EXPERT_KNOWLEDGE: Dict[str, Any] = {
    "checklist": {
        "source": ["blauwasser", "svb", "palstek"],
        "description_de": "Professionelle Einwinterungs-Checkliste",
        "motor": [
            "Ölwechsel (Motor + Getriebe) — NICHT im Frühjahr, Säuren im Altöl greifen Dichtungen an",
            "Kühlwasserkreislauf mit Frostschutz spülen (Propylenglykol, nicht Ethylenglykol)",
            "Impeller ausbauen und NEBEN der Pumpe aufbewahren (nicht eingebaut lassen = verformt)",
            "Dieseltank VOLL machen (verhindert Kondenswasser → kein Dieselpest)",
            "Kraftstofffilter wechseln und Biozid zusetzen",
            "Auspuff-Wassersammler leeren",
            "Saildrive-Ölstand prüfen, Membran-Dichtung inspizieren"
        ],
        "wassersystem": [
            "Komplettes Frischwassersystem entleeren",
            "Pumpen trockenlaufen lassen (kurz, um Restwasser zu entfernen)",
            "WC-System komplett spülen und entleeren",
            "Frostschutzmittel in alle Leitungen (lebensmittelecht: Propylenglykol)",
            "Boiler entleeren"
        ],
        "elektrik": [
            "Batterien voll aufladen",
            "Ladegerät im Erhaltungsmodus lassen (wenn Landstrom vorhanden)",
            "Alternativ: Batterien an Land lagern und monatlich nachladen",
            "Alle Verbraucher ausschalten, Hauptschalter AUS",
            "LiFePO4-Batterien: BMS in Wintermodus, Temperaturüberwachung"
        ],
        "rumpf_deck": [
            "Unterwasserschiff reinigen und Antifouling-Zustand dokumentieren",
            "Seeventile schließen und öffnen (Gangbarkeit prüfen)",
            "Persenning aufziehen — Luftzirkulation sicherstellen!",
            "Alle Luken einen Spalt offen lassen (Belüftung gegen Schimmel)",
            "Polster hochstellen oder rausnehmen"
        ],
        "rigg": [
            "Fallen abnehmen oder vom Mast wegbinden (Schlagen beschädigt Mast)",
            "Wantenspanner lockern (je nach Werft-Empfehlung)",
            "Rollreff-Anlage entspannen",
            "Segel trocken lagern, lose gerollt (nicht in Segelsäcken)"
        ]
    }
}


# ============================================================================
# ENERGIE-SYSTEME — Energy System Knowledge from Cruising Community
# Source: Hafenkino, Sailing Uma, SV Delos, Blauwasser.de, SVB
# ============================================================================

ENERGY_SYSTEMS_EXPERT_KNOWLEDGE: Dict[str, Any] = {
    "solar_systems": {
        "source": ["hafenkino", "svb", "blauwasser"],
        "description_de": "Solaranlagen für Segelyachten — Praxiswissen",
        "daily_yield": {
            "large_system_400w_plus": "4+ kWh/Tag bei Sonnenschein (Mai, Mittelmeer)",
            "medium_system_200w": "2-3 kWh/Tag (Sommer, Nordeuropa)",
            "small_system_100w": "0.8-1.5 kWh/Tag",
            "note_de": "Ertrag stark abhängig von Ausrichtung, Verschattung durch Rigg, und Neigungswinkel"
        },
        "panel_types": {
            "rigid_monocrystalline": {
                "efficiency": "20-22%",
                "lifespan": "20-25 Jahre",
                "pros": ["Höchste Effizienz", "Langlebig", "Preiswerter pro Watt"],
                "cons": ["Schwer", "Starr", "Bruchgefahr"],
                "mounting": "Davits, Bimini-Gestell, Deckaufbau"
            },
            "semi_flexible": {
                "efficiency": "18-20%",
                "lifespan": "5-10 Jahre",
                "pros": ["Leicht", "Anpassbar an Deckform", "Einfache Montage"],
                "cons": ["Kürzere Lebensdauer", "Hitzeempfindlich", "Delaminiert oft"],
                "note_de": "Nicht direkt auf Deck kleben — Hinterlüftung nötig, sonst überhitzt Zelle"
            }
        },
        "charge_controllers": {
            "mppt_vs_pwm": {
                "mppt": "Maximum Power Point Tracking — 15-30% mehr Ertrag als PWM. Standard ab 200W.",
                "pwm": "Pulse Width Modulation — einfacher, günstiger, nur für kleine Systeme < 100W sinnvoll",
                "brands": ["Victron SmartSolar MPPT", "Votronic MPP", "EPEver Tracer"]
            }
        }
    },

    "wind_generators": {
        "source": ["hafenkino", "blauwasser"],
        "description_de": "Windgeneratoren an Bord — Praxiserfahrungen",
        "minimum_power": "400W für sinnvolle Erträge",
        "daily_yield_trade_winds": "~2 kWh/Tag (Passatgebiet, Ägäis-Sommer)",
        "daily_yield_variable": "0.5-1.5 kWh/Tag (Nordeuropa, variable Winde)",
        "brands": [
            {"name": "Superwind 350", "power": "350W", "noise": "leise", "quality": "hoch", "cost": "~2.000 EUR"},
            {"name": "Silentwind 400+", "power": "420W", "noise": "leise", "quality": "hoch", "cost": "~1.800 EUR"},
            {"name": "Rutland 1200", "power": "500W", "noise": "laut bei Starkwind", "quality": "mittel", "cost": "~1.200 EUR"}
        ],
        "installation_notes": [
            "Montage auf Heckbügel mindestens 2m über Deck (Sicherheit + Windausbeute)",
            "Vibrationsdämpfer zwingend erforderlich",
            "Bremsschalter/Kurzschlussschalter für Sturm und Wartung"
        ]
    },

    "battery_systems_real_world": {
        "source": ["sailing_uma", "sv_delos", "hafenkino", "blauwasser"],
        "description_de": "Batterie-Praxiserfahrungen aus der Langfahrt-Community",
        "lifepo4_setups": [
            {
                "boat": "Sailing Uma (Pearson 36, 1972)",
                "bank": "12x Battle Born 100Ah 12V",
                "total_capacity": "1.200 Ah @ 12V (14.400 Wh)",
                "specs_per_battery": {
                    "weight": "14 kg (31 lbs)",
                    "dimensions": "324 x 175 x 229 mm",
                    "continuous_discharge": "100A",
                    "surge": "200A (30 Sek)",
                    "cycles": "3.000-5.000",
                    "warranty": "10 Jahre"
                },
                "experience_de": "20.000+ Seemeilen, inkl. Elektro-Antrieb für beide Saildrives"
            },
            {
                "boat": "SV Delos (Amel Super Maramu 53ft)",
                "bank": "8x Battle Born 100Ah",
                "total_capacity": "400 Ah @ 24V (9.600 Wh)",
                "experience_de": "4+ Saisons getestet, exzellente Performance, Spannung bleibt hoch auch bei 100A Entladung"
            },
            {
                "boat": "Hafenkino (Langfahrt-Setup)",
                "bank": "Victron LiFePO4 Smart 12.8V/200Ah",
                "monitoring": "Victron Cerbo GX (Zentrale Steuereinheit)",
                "experience_de": "Solarladen von 65% auf 85% an sonnigem Tag bei laufenden Verbrauchern"
            }
        ],
        "maintenance_budget_rule": {
            "source": "sv_delos",
            "annual_general": "1.5% des Bootswertes (Pumpen, Impeller, Ölwechsel, Segelreparaturen)",
            "annual_major": "1.5-3% des Bootswertes (Rigg, Segel, Helling, Antifouling)",
            "example": "100.000 EUR Boot = 1.500-4.500 EUR/Jahr (DIY)",
            "note_de": "Bei professioneller Arbeit deutlich höher. SV Delos: Range 1-5% über 10 Jahre."
        }
    },

    "watermaker_systems": {
        "source": ["blauwasser", "yacht"],
        "description_de": "Watermaker/Wassermacher für Yachten",
        "principle": "Hochdruck-Umkehrosmose: Seewasser wird durch Membran gepresst, Salz und Verunreinigungen zurückgehalten",
        "components": [
            "Seewasser-Einlass über Seeventil",
            "Grobfilter: Algen, Sand, große Partikel",
            "Sedimentfilter: 5 µm Feinheit",
            "Hochdruckpumpe (60-80 bar)",
            "RO-Membran (Umkehrosmose)",
            "Produktwasser-Auslass (trinkbar)",
            "Konzentrat-Auslass (Salzwasser zurück ins Meer)"
        ],
        "brands": [
            {"name": "Schenker", "origin": "Italien", "capacity": "30-150 L/h", "note": "Energieeffizient, beliebt bei Langfahrt"},
            {"name": "Spectra", "origin": "USA", "capacity": "20-80 L/h", "note": "Clark-Pumpe, sehr energieeffizient (4-6 Ah/Liter)"},
            {"name": "AQUATEC", "origin": "Deutschland", "capacity": "50-200 L/h", "note": "Robuste Hochdruck-Systeme"},
            {"name": "AQUAbibe", "origin": "Deutschland", "capacity": "50-140 L/h", "note": "Kompakt, gut für Retrofit"},
            {"name": "Dessalator", "origin": "Frankreich", "capacity": "30-100 L/h", "note": "Solider Klassiker"}
        ],
        "maintenance": [
            "Konservierung bei Nichtgebrauch > 5 Tage (Biozid-Lösung)",
            "Vorfilter regelmäßig wechseln (alle 250-500 Betriebsstunden)",
            "RO-Membran: Lebensdauer 3-7 Jahre bei korrekter Pflege",
            "Nie in Hafenwasser oder verschmutztem Wasser betreiben",
            "Salinity-Sensor kalibrieren (Produktwasser muss < 500 ppm TDS sein)"
        ]
    }
}


# ============================================================================
# EQUIPMENT-TESTS — Spezifische Testresultate aus YACHT-TV und SVB
# Source: yacht.de, SVB, Practical Sailor
# ============================================================================

EQUIPMENT_TEST_KNOWLEDGE: Dict[str, Any] = {
    "anchor_tests": {
        "source": ["yacht"],
        "description_de": "Anker-Vergleichstests (YACHT Magazin)",
        "yacht_test_2024": {
            "location": "Flensburger Förde",
            "method": "6 Anker getestet mit Taucher-Beobachtung unter Wasser",
            "findings": [
                {"brand": "Plastimo", "result_de": "Testsieger der letzten 3 Tests. Schnelles, sicheres Eingraben. Dauerhafter Halt."},
                {"brand": "Fortress", "result_de": "Hielt nur auf Sandgrund zuverlässig. Auf Schlick/Seegras eingeschränkt."}
            ],
            "key_insight_de": "Die Grundeinstellung (Winkel der Flügel) entscheidet über die Haltekraft"
        }
    },

    "winch_tests": {
        "source": ["yacht"],
        "description_de": "Einhand-Winsch-Kurbeln und Elektro-Winschen",
        "single_hand_cranks": [
            {"brand": "Antal Speedylock", "type": "Einhand", "tested": True},
            {"brand": "Harken Carbo OneTouch", "type": "Einhand", "tested": True},
            {"brand": "Lewmar One-Touch", "type": "Einhand", "tested": True},
            {"brand": "Ronstan Quick-Lock", "type": "Einhand", "tested": True}
        ],
        "electric_winches": [
            {"brand": "Seldén E40rev", "feature": "Elektrische Winsch mit Rückwärtsgang", "note": "Für Rollreff ideal"},
            {"brand": "Ewincher", "feature": "Konvertiert jede Winsch zur E-Winsch", "note": "Nachrüstlösung"}
        ]
    },

    "fire_safety_tests": {
        "source": ["yacht"],
        "description_de": "Feuerlöscher-Tests speziell für Boote",
        "lithium_battery_fires": {
            "tested_products": [
                {"name": "Lithium X6 (Bavaria)", "type": "Speziallöscher Lithium"},
                {"name": "P6.0 (CW Fire)", "type": "Speziallöscher"},
                {"name": "Pro-Line Water Lithium (Gloria)", "type": "Wassernebel"},
                {"name": "G6 SDJ Gel (Jockel)", "type": "Gel-Löscher"}
            ],
            "key_finding_de": "LiFePO4 thermisch deutlich sicherer als NMC-Lithium. Bei NMC Thermal Runaway sehr schwer zu löschen."
        },
        "automatic_systems": {
            "maus_system": {
                "origin": "Schweiz",
                "type": "Aerosol-Löschsystem",
                "advantage_de": "Hinterlässt keine Rückstände. Automatische Auslösung.",
                "use_case": "Motorraum, Batteriekasten"
            }
        }
    },

    "navigation_electronics_tests": {
        "source": ["yacht", "svb"],
        "description_de": "Kartenplotter und Navigations-Elektronik Tests",
        "chartplotters_2024": [
            {
                "brand": "B&G",
                "model": "Zeus S (Einstieg) / Zeus³ 12 (Premium)",
                "display": "SolarMAX HD (sonnenlichttauglich, polarisiert, regentauglich)",
                "connectivity": "NMEA 2000",
                "cartography": ["C-MAP", "Navionics", "NV Digital"],
                "note": "8mm Flush-Mount-Profil"
            },
            {
                "brand": "Raymarine",
                "model": "Axiom 2 Pro",
                "os": "Android-basiert",
                "note": "Individualisierbar mit Apps"
            },
            {
                "brand": "Q-Experience",
                "model": "Q2",
                "origin": "Finnland",
                "os": "Android-basiert",
                "note": "Newcomer, gut positioniert zwischen Platzhirschen"
            }
        ],
        "electronic_compasses_test": {
            "devices_tested": 8,
            "manufacturers": 6,
            "price_range": "200-857 EUR",
            "source": "yacht"
        },
        "autopilot_safety": {
            "documented_rammings": 5,
            "cause_de": "Autopilot-Nutzung ohne ausreichende Wachsamkeit",
            "source": "yacht"
        }
    },

    "life_safety_tests": {
        "source": ["yacht"],
        "description_de": "Rettungsmittel-Tests",
        "life_rafts": {
            "test_2015": {
                "models_tested": 6,
                "method": "Pool-Test mit künstlichen Wellen und Wind",
                "problems_found": [
                    "Mangelhafte Qualität bei günstigen Modellen",
                    "Nutzloses Equipment (stumpfe Messer, undichte Pumpen)",
                    "Wassereintrittsprobleme durch Drainage-Öffnungen"
                ]
            },
            "standard": "ISO 9650-2 (Küstengewässer, 24 Stunden)"
        },
        "life_jackets": {
            "classes": {
                "150_newton": "Standard Hochsee, 15-16 Modelle getestet",
                "275_newton": "Schwerwetter/Offshore, 9+ automatische Schwimmwesten getestet"
            },
            "major_test": "24 Automatik-Schwimmwesten im Vergleich",
            "standard": "EN ISO 12402"
        }
    },

    "gelcoat_polish_tests": {
        "source": ["yacht"],
        "description_de": "Politur und Gelcoat-Pflege Vergleichstests",
        "tested_brands": [
            "Vosschemie / Yachtcare (Polyglanz)",
            "3M Poliersysteme",
            "Dr. Keddo Simarflüssig",
            "Dinitrol",
            "Rot-Weiß",
            "Maincare",
            "Möwe",
            "Polish & Protect",
            "Renskib"
        ],
        "recommendations": {
            "for_chalking": "Rubbing Compound (grob) → Politur (fein) → Wachsversiegelung",
            "for_maintenance": "Carnauba-Wachs als Langzeitschutz",
            "machine_type": "Exzenter-Poliermaschine bevorzugt (weniger Risiko als Rotationspolierer)"
        }
    },

    "sail_material_knowledge": {
        "source": ["yacht", "blauwasser"],
        "description_de": "Segeltuch-Materialwissen",
        "materials": {
            "dacron_dc": {
                "name": "Dacron (Dimension Polyant DC-Material)",
                "type": "Gewebtes Polyester",
                "use": "Standardsegel, Fahrtensegel",
                "lifespan": "8-15 Jahre",
                "note_de": "Robuster Allrounder, UV-beständig"
            },
            "dcx_xply": {
                "name": "DCX (DC mit X-Ply Schicht)",
                "type": "Hybrid — gewebtes Polyester + diagonale Faserlage",
                "advantage_de": "Bessere Dehnungsfestigkeit diagonal, verbesserte mechanische Festigkeit, UV-Schutz",
                "use": "Verbesserte Fahrtensegel"
            },
            "aramid_laminate": {
                "name": "Quantum XRP Ultra Aramid Black",
                "type": "Laminatsegel",
                "use": "Performance-Fahrtensegel bis 40 Fuß",
                "note_de": "Bessere Profilstabilität als reines Dacron"
            }
        }
    }
}


# ============================================================================
# GFK-REPARATUR DETAIL — Spezifische Reparaturanleitungen
# Source: Marietim, Sail Life, NautiCare, yacht.de
# ============================================================================

GFK_REPAIR_DETAILED: Dict[str, Any] = {
    "gelcoat_repair_marietim_method": {
        "source": ["marietim"],
        "description_de": "Gelcoat-Reparatur nach Marietim-Methode (Polyester statt Epoxid)",
        "philosophy_de": "Materialkompatibilität: Gelcoat ist Polyester, daher Reparatur auch mit Polyester — nicht Epoxid",
        "steps": [
            "1. Haarrisse mit Dremel-Fräser V-förmig öffnen (2-3mm breit, 2mm tief)",
            "2. Staub und Fett entfernen (Aceton)",
            "3. Mit Polyesterharz (+ Härter) füllen — NICHT Epoxid",
            "4. Glattziehen und leicht überfüllen (Schwund beim Aushärten)",
            "5. Nach Aushärtung plan schleifen (120er → 240er → 400er → 800er)",
            "6. Komplette neue Gelcoat-Schicht aufspritzen oder rollen",
            "7. Nassschliff 1000er → 1500er → 2000er, dann polieren"
        ],
        "advantage_de": "Einheitliches Polyester-System — keine Haftungsprobleme zwischen Epoxid und Polyester",
        "note_de": "Bei strukturellen Schäden (tiefer als Gelcoat): IMMER Epoxid + Glasfaser verwenden"
    },

    "blister_repair_procedure": {
        "source": ["sail_life", "nauticare"],
        "description_de": "Professionelle Blasen-Reparatur (Osmose-Einzelblasen)",
        "tools": ["36er Schleifscheibe", "Winkelschleifer", "Teppichmesser (spitz)", "Epoxidharz", "Glasfasergewebe"],
        "critical_rule_de": "Vertiefung muss 20x BREITER als TIEF sein — flache Mulde, kein Krater!",
        "steps": [
            "1. Blase mit spitzem Messer aufstechen, Flüssigkeit auffangen",
            "2. Geruchstest: stechend-sauer = Osmose bestätigt",
            "3. Mit 36er Schleifscheibe Blase und beschädigtes Laminat abtragen",
            "4. Nicht tiefer schleifen als letzte beschädigte Laminatschicht",
            "5. Mulde muss 20x breiter als tief sein (z.B. 3mm tief = 60mm breit)",
            "6. Glasfasermatten in gestaffelten Größen schneiden (größte = Muldengröße)",
            "7. Nass-in-nass laminieren: Epoxid → Glasfaser → Epoxid → nächste Lage",
            "8. Epoxid-Sperrschicht über gesamten Reparaturbereich (min. 300µm)",
            "9. Nach vollständiger Aushärtung: Schleifen → Primer → Antifouling"
        ]
    },

    "grp_layering_sequence": {
        "source": ["marietim"],
        "description_de": "Reihenfolge der Lagen bei GFK-Reparaturen",
        "method": "Große Lage zuerst (unten), dann kleiner werdend nach oben",
        "reason_de": "Kraftfluss: äußere Schicht trägt die Last. Große Basis, verjüngt sich nach außen."
    },

    "deck_soft_spot_repair": {
        "source": ["yacht", "sail_life"],
        "description_de": "Weiche Stellen im Deck (Sandwich-Delamination) reparieren",
        "diagnosis": [
            "Drucktest: Mit Fuß/Hand drücken — gibt nach = Soft Spot",
            "Klopftest: Dumpfer Klang vs. heller Klang bei gesundem Laminat",
            "Feuchtemessung: Erhöhte Werte im betroffenen Bereich"
        ],
        "repair_injection": {
            "suitable_for": "Delamination < 0.5m², Kern noch intakt (nur abgelöst)",
            "steps": [
                "5-6mm Löcher in obere Deckschicht bohren (Raster 50-80mm)",
                "Epoxidharz mit Spritzen injizieren bis aus Nachbarlöchern austritt",
                "Folie auflegen, mit Gewichten/Vakuum belasten",
                "24h aushärten lassen",
                "Löcher mit Gelcoat verschließen"
            ]
        },
        "repair_core_replacement": {
            "suitable_for": "Kernfäule, Balsazerfall, große Bereiche",
            "steps": [
                "Obere Laminatschicht vorsichtig entfernen (Stichsäge, Multitool)",
                "Faulen Kern komplett ausräumen (bei Balsa: alles raus!)",
                "Fläche trocknen — bei Balsa-Fäule: WOCHEN",
                "Neuen Kern einsetzen: PVC-Schaum (Divinycell) oder SAN (Corecell)",
                "NICHT wieder Balsa einsetzen — Upgrade auf PVC/SAN!",
                "Kern mit Epoxid einkleben (Thixotropie-Zusatz für Standfestigkeit)",
                "Obere Laminatschicht neu aufbauen (Epoxid + Glasfaser, 2-3 Lagen)",
                "Gelcoat oder Antislip-Farbe als Finish"
            ],
            "note_de": "Bei strukturellen Decksbereichen (Winschen, Klampen): unbedingt Kernverstärkung einplanen"
        }
    },

    "interior_refit_materials": {
        "source": ["no_frills_sailing"],
        "description_de": "Materialien für Interior-Refit (bewährte Praxis)",
        "wood": {
            "teak_massiv": "Für sichtbare Flächen, Kanten, Handläufe",
            "birch_plywood_4mm": "Für Deckenverkleidungen",
            "oak_battens": "Unterkonstruktion, weiß gestrichen"
        },
        "adhesives": {
            "pur_glue_d4": "PUR-Kleber (D4-Klassifizierung) — sehr stark, wasserfest",
            "epoxy_coating": "2 volle Epoxid-Schichten auf Unterkonstruktion"
        },
        "varnish_system": {
            "product": "International Gold Spar Varnish",
            "procedure_de": "4-Schicht-System mit abnehmender Verdünnung",
            "layers": [
                "Schicht 1: 50% Verdünnung (dringt tief ins Holz)",
                "Schicht 2: 30% Verdünnung",
                "Schicht 3: 10% Verdünnung",
                "Schicht 4+: Unverdünnt (mind. 3 Schichten unverdünnt)"
            ]
        }
    },

    "shore_power_standards": {
        "source": ["bootstechnik"],
        "description_de": "Norm-gerechter Landanschluss",
        "standard": "DIN EN 60092-507:2024-12 (Elektrische Installationen auf Schiffen, Teil 507: Yachten)",
        "components": [
            "CEE-Stecker (blau, 230V, 16A für Yachten)",
            "FI/RCD-Schutzschalter (30mA Auslösestrom)",
            "Leitungsschutzschalter (B- oder C-Charakteristik)",
            "Trenntransformator (optional aber empfohlen)",
            "Galvanischer Isolator (Minimum)",
            "Erdungsschiene"
        ],
        "note_de": "Landanschluss ist häufigste Ursache für galvanische Korrosion — Schutzmaßnahmen zwingend"
    }
}


# ============================================================================
# ASSESSMENT FUNCTION
# ============================================================================

def get_expert_knowledge_for_topic(topic: str) -> Dict[str, Any]:
    """
    Retrieves expert knowledge for a given topic area.

    Args:
        topic: One of the ExpertiseArea enum values

    Returns:
        Dict with relevant expert knowledge
    """
    topic_mapping = {
        "hull_inspection": {"purchase": PURCHASE_EXPERTISE, "composite": COMPOSITE_EXPERT_KNOWLEDGE, "gfk_repair": GFK_REPAIR_DETAILED},
        "osmosis": {"osmosis": OSMOSIS_EXPERT_KNOWLEDGE, "composite": COMPOSITE_EXPERT_KNOWLEDGE, "gfk_repair": GFK_REPAIR_DETAILED},
        "rigging": {"rigging": RIGGING_EXPERT_KNOWLEDGE},
        "engine": {"engine": ENGINE_EXPERT_KNOWLEDGE},
        "electrical": {"electrical": ELECTRICAL_EXPERT_KNOWLEDGE, "energy": ENERGY_SYSTEMS_EXPERT_KNOWLEDGE},
        "teak_deck": {"teak": TEAK_DECK_EXPERT_KNOWLEDGE, "gfk_repair": GFK_REPAIR_DETAILED},
        "seacocks": {"seacocks": SEACOCK_EXPERT_KNOWLEDGE},
        "antifouling": {"antifouling": ANTIFOULING_EXPERT_KNOWLEDGE},
        "purchase_guidance": {"purchase": PURCHASE_EXPERTISE},
        "sandwich_core": {"composite": COMPOSITE_EXPERT_KNOWLEDGE, "gfk_repair": GFK_REPAIR_DETAILED},
        "galvanic_corrosion": {"electrical": ELECTRICAL_EXPERT_KNOWLEDGE, "energy": ENERGY_SYSTEMS_EXPERT_KNOWLEDGE},
        "shore_power": {"electrical": ELECTRICAL_EXPERT_KNOWLEDGE, "gfk_repair": GFK_REPAIR_DETAILED},
        "winterization": {"winterization": WINTERIZATION_EXPERT_KNOWLEDGE},
        "energy_systems": {"energy": ENERGY_SYSTEMS_EXPERT_KNOWLEDGE},
        "equipment": {"equipment": EQUIPMENT_TEST_KNOWLEDGE},
        "safety": {"equipment": EQUIPMENT_TEST_KNOWLEDGE},
        "navigation": {"equipment": EQUIPMENT_TEST_KNOWLEDGE},
        "gfk_repair": {"gfk_repair": GFK_REPAIR_DETAILED, "composite": COMPOSITE_EXPERT_KNOWLEDGE},
    }
    return topic_mapping.get(topic, {})


def get_all_expert_sources() -> List[Dict[str, str]]:
    """Returns list of all expert knowledge sources used."""
    return [
        {"name": "BootsProfis", "type": "youtube", "url": "https://bootsprofis.tv", "focus": "Bootsgutachten, Kaufberatung, Sailing"},
        {"name": "YACHT-TV", "type": "youtube", "url": "https://yacht.de", "focus": "Yachttests, Technik, DIY"},
        {"name": "Marietim", "type": "youtube", "url": "https://marietim.ch", "focus": "Bootskauf, Materialien, Borddurchlässe"},
        {"name": "Blauwasser.de", "type": "web", "url": "https://blauwasser.de", "focus": "Langfahrt, Technik, Bootskauf"},
        {"name": "boote-forum.de", "type": "forum", "url": "https://boote-forum.de", "focus": "Community-Erfahrung, Reparaturen"},
        {"name": "segeln-forum.de", "type": "forum", "url": "https://segeln-forum.de", "focus": "Segeln, Technik, Refit"},
        {"name": "YACHT-Forum", "type": "forum", "url": "https://forum.yacht.de", "focus": "Technik, Diskussionen"},
        {"name": "Pantaenius", "type": "insurance", "url": "https://pantaenius.com", "focus": "Rigg-Schäden, Schadensstatistik"},
        {"name": "float Magazin", "type": "magazine", "url": "https://floatmagazin.de", "focus": "Maritime Technik und Lifestyle"},
        {"name": "Palstek", "type": "magazine", "url": "https://palstek.de", "focus": "Praxis-Seemannschaft"},
        {"name": "SVB", "type": "chandlery", "url": "https://svb.de", "focus": "Antifouling-Tests, Produktvergleiche"},
        {"name": "ADAC Skipper", "type": "web", "url": "https://skipper.adac.de", "focus": "Ratgeber, Osmose, Sicherheit"},
        {"name": "NautiCare", "type": "web", "url": "https://nauticare.de", "focus": "GFK-Reparatur, Osmose-Sanierung"},
        {"name": "bootstechnik.de", "type": "web", "url": "https://bootstechnik.de", "focus": "Elektrik, Landanschluss"},
        {"name": "frag-jochen.de", "type": "web", "url": "https://frag-jochen.de", "focus": "Teakdeck-Sanierung"},
        {"name": "Victron Energy", "type": "manufacturer", "url": "https://victronenergy.com", "focus": "Bordstrom, Galvanische Korrosion"},
        {"name": "Mastervolt", "type": "manufacturer", "url": "https://mastervolt.de", "focus": "Korrosionsschutz, Bordstrom"},
        {"name": "Sail Life", "type": "youtube", "url": "https://saillifechannel.com", "focus": "DIY-Refit, GFK-Reparatur, Osmose"},
        {"name": "Sailing Uma", "type": "youtube", "url": "https://sailinguma.com", "focus": "Elektro-Antrieb, LiFePO4, Off-Grid"},
        {"name": "SV Delos", "type": "youtube", "url": "https://svdelos.com", "focus": "Langfahrt-Wartung, Budget, Batteriesysteme"},
        {"name": "Hafenkino.blog", "type": "blog", "url": "https://hafenkino.blog", "focus": "Energiemanagement, Solar, Langfahrt"},
        {"name": "No-Frills-Sailing", "type": "blog", "url": "https://no-frills-sailing.com", "focus": "Interior-Refit, Holzarbeiten, Lackierung"},
    ]
