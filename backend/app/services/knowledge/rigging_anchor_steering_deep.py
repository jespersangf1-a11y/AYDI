"""
AYDI Rigg-Hardware, Anker, Steuerung und Borddurchlässe — Tiefenwissen
Exhaustive specifications for rigging terminals, turnbuckles, shackles,
anchor systems, steering, windlasses, and through-hull fittings.

Manufacturers: Sta-Lok, Norseman, Wichard, Ronstan, Harken, Lewmar, Lofrans,
Rocna, Mantus, Spade, Fortress, Groco, TruDesign, Jefa, Whitlock

Author: AYDI Research Team
Version: 1.0
"""

from typing import Dict, List, Any, Tuple


RIGGING_TERMINAL_DATABASE: Dict[str, Any] = {
    "terminal_types": {
        "fork": {
            "name_de": "Gabelkopf",
            "use_de": "Feste Anschlusspunkte für Unterwanten, Zwischenstage",
            "angles": "0° (direkt axial)",
            "load_path": "Durch beide Gabelarme gleichmäßig verteilt"
        },
        "eye": {
            "name_de": "Augenkopf",
            "use_de": "Universeller Anschlusspunkt mit Lastöse für Schäkel",
            "angles": "0-20° (moderate Winkelabweichungen tolerant)",
            "load_path": "Konzentriert an Ösenunterkante"
        },
        "stud": {
            "name_de": "Gewindezapfen",
            "use_de": "Gewindeanschluss für Wantenspanner, Oberwanten",
            "thread_standard": "UNC oder metrisch",
            "load_path": "Durch Gewinde auf Muttergewinde übertragen"
        },
        "t_ball": {
            "name_de": "T-Kugel / Kugelkopf",
            "use_de": "Artikulierende Stage (Backstage, Kutterstage). NICHT für Seitenwanten!",
            "articulation_degrees": 360,
            "warning_de": "Reduziert Bruchlast um 15-20% gegenüber starren Terminals"
        },
        "stemball": {
            "name_de": "Stammkugel (Elefantenfuß)",
            "use_de": "Alternative Wantenbefestigung mit Halbkugel-Terminal",
            "material": "316L Edelstahl oder Nitronic 50",
            "mounting": "Direkt auf Schafthalter geschraubt"
        }
    },

    "swageless_mechanical": {
        "description_de": "Mechanische Terminals — kein Spezialwerkzeug nötig, an Bord montierbar",
        "efficiency_percent": "95-99% (abhängig von Drahtqualität und Installation)",

        "sta_lok": {
            "manufacturer": "Sta-Lok (UK)",
            "material": "316 Edelstahl (Socket, Wedge, Splitring)",
            "wire_range_mm": "3-26",
            "compatible_wire": ["1x19", "7x19", "7x7", "Compacted Strand", "Dyform"],
            "components": {
                "socket": "Außengehäuse mit Innengewinde",
                "wedge": "Keilförmiger Einsatz mit V-Rillen",
                "splitring": "Sicherungsring gegen Wedge-Auswanderung"
            },
            "installation_steps": [
                "1. Socket über Draht schieben (Tape ca. 300mm vom Ende zum Schutz)",
                "2. Äußere Litzen 50-76mm aufdrehen (je nach Drahtdurchmesser), Kerndraht freilegen",
                "3. Wedge (Keil) über Kerndraht schieben, Keils-Nummer notieren",
                "4. Äußere Litzen um Keil wickeln (CW oder CCW je nach Schlagrichtung des Drahtes)",
                "5. 2-3mm Kerndraht muss aus Keil ragen, Litzen gleichmäßig verteilt",
                "6. Socket aufschrauben — zunächst von Hand festziehen",
                "7. Mit 19mm Schraubenschlüssel feststellen, von Hand anziehen bis Widerstand",
                "8. Splitring über Wedge-Nut schieben, einrasten"
            ],
            "torque_guide_nm": {
                "6mm": 3.4,
                "8mm": 6.1,
                "10mm": 9.5,
                "12mm": 13.6
            },
            "reusable": True,
            "note_de": "Laser-markierte Keile für einfache Identifikation. Keile sind NICHT universell — müssen zur Drahtsorte passen!",
            "breaking_loads_percent": {
                "new_installation": 95,
                "after_load_cycling": 98,
                "after_100_hours_sailing": 99
            },
            "field_replacement": "Komplett zwischen Fahrten auswechselbar — alte Komponenten können sofort wiederverwendet werden"
        },

        "norseman": {
            "manufacturer": "Norseman (jetzt Tylaska Marine, gegründet 1959)",
            "material": "316L Edelstahl",
            "breaking_load_5_16_inch": 10770,
            "breaking_load_unit": "lbs",
            "efficiency_percent": 83.5,
            "configurations": ["Eye", "Fork", "Stud", "Toggle", "Stemball", "Insulator"],
            "components": {
                "cone": "Konischer Kegelformer mit automatischer Zentrierung",
                "outer_cone": "Äußerer Konus für Lichtwellenleiter",
                "wedge_screws": "Mitnehmerschrauben für präzise Positionierung"
            },
            "installation_advantage_de": "Cone-Design erfordert weniger manuelle Feinabstimmung als Sta-Lok",
            "reusable": True,
            "patent_de": "Norseman-Cone-Patente sind ausgelaufen — jetzt frei verfügbar"
        },

        "hi_mod_petersen": {
            "manufacturer": "Petersen Stainless (Dänemark, Hi-MOD Linie)",
            "material": "EN10088 1.4404 (316L) Stahl + Aluminium-Bronze Kronringe",
            "crown_rings_count": "2-6 (größenabhängig)",
            "feature_de": "Integrierte Kronringe ordnen Drahtlitzen automatisch für gleichmäßige Lastverteilung",
            "geometry": "Patentiert: Mehrfach-Kegelform reduziert Kantenpressungen",
            "efficiency_percent": 99,
            "sealant_required": False,
            "reusable": True,
            "note_de": "Teuerste Mechanik-Option, aber höchste Zuverlässigkeit und Langlebigkeit"
        },

        "rockwell_schaefer": {
            "manufacturer": "Rockwell Schaefer (USA, ehem. Standard-Terminal)",
            "status": "veraltet, wird noch gelegentlich auf älteren Yachten gefunden",
            "note_de": "Nicht für Neuinstallationen empfohlen — zu komplex, lange Montagezeit"
        }
    },

    "swaged_pressed": {
        "description_de": "Gepresste Terminals — professionelles Spezialwerkzeug erforderlich",
        "efficiency_percent": "98-100",
        "advantage_de": [
            "Leichter, kompakter als mechanische Terminals",
            "Gleiche oder bessere Bruchlast als Draht selbst",
            "Hochwertige optische Ausführung"
        ],
        "disadvantage_de": [
            "Nicht wiederverwendbar, nicht inspizierbar",
            "Off-Site-Herstellung nötig (spezialisierte Rigger)",
            "Teuer pro Stück",
            "Lieferzeiten 2-4 Wochen",
            "Problem bei Änderungen: Altes Terminal muss abgelöst werden"
        ],
        "manufacturing_process": {
            "step_1": "Draht in Seele einführen",
            "step_2": "Terminal über Draht schieben",
            "step_3": "Spezialwerkzeug (Swager) mit tonnenschwerer Kraft pressen",
            "step_4": "Kontrolle unter Belastung (Proof Load 80% der Bruchlast)"
        },
        "note_de": "Muss von zertifiziertem Rigger nach ISO 12922 oder äquivalent hergestellt werden",
        "quality_standard": "ISO/IEC Guide 28 (metrisch) oder ASTM B 406 (US)"
    },

    "wire_specifications": {
        "1x19": {
            "construction": "1 Litze mit 19 Drähten (meist 3+6+10 Drähte in Schichten)",
            "flexibility": "starr (nicht biegbar — min. Biegradius ~100× Durchmesser)",
            "stretch": "minimal (0.2-0.3% bei 50% Bruchlast)",
            "modulus_gpa": 190,
            "use_primary": "Stehendes Gut (Wanten, Oberwanten, Stage, Unterwanten)",
            "density_g_cm3": 7.85,
            "corrosion_rating": "ausgezeichnet (316L Edelstahl)",
            "price_index": 1.0,
            "breaking_loads_kg": {
                "3mm": 363,
                "4mm": 635,
                "5mm": 998,
                "6mm": 1406,
                "7mm": 1950,
                "8mm": 2586,
                "9mm": 3273,
                "10mm": 4036,
                "11mm": 4899,
                "12mm": 5806,
                "14mm": 7895,
                "16mm": 10354
            },
            "weight_kg_per_100m": {
                "3mm": 22,
                "4mm": 39,
                "5mm": 61,
                "6mm": 88,
                "8mm": 157,
                "10mm": 245,
                "12mm": 353
            },
            "creep_percent_per_year": 0.1
        },

        "7x19": {
            "construction": "7 Litzen mit je 19 Drähten (133 Drähte total), konzentrisch angeordnet",
            "flexibility": "sehr hoch (min. Biegradius ~30× Durchmesser)",
            "stretch": "höher als 1x19 (0.8-1.2% bei 50% Bruchlast)",
            "modulus_gpa": 130,
            "use_primary": "Laufendes Gut (Treidelienen, Trossen), Steuerseile, Reffleine",
            "density_g_cm3": 7.85,
            "corrosion_rating": "ausgezeichnet (316L Edelstahl)",
            "price_index": 0.85,
            "strength_vs_1x19_percent": 78,
            "breaking_loads_kg": {
                "3mm": 284,
                "4mm": 496,
                "5mm": 778,
                "6mm": 1097,
                "7mm": 1522,
                "8mm": 2019,
                "10mm": 3147,
                "12mm": 4530,
                "14mm": 6162,
                "16mm": 8075
            },
            "weight_kg_per_100m": {
                "3mm": 22,
                "4mm": 39,
                "5mm": 61,
                "6mm": 88,
                "8mm": 157,
                "10mm": 245
            },
            "creep_percent_per_year": 0.3
        },

        "7x7": {
            "construction": "7 Litzen mit je 7 Drähten (49 Drähte), sehr grobe Struktur",
            "flexibility": "extrem hoch (leicht biegbar)",
            "stretch": "sehr hoch",
            "use_primary": "Hochbelastete Treidelienen, Marine-Schleppseile, Kettenersatzteile",
            "note_de": "Selten auf Segelyachten, eher im Motortransport",
            "strength_vs_1x19_percent": 65,
            "weight_reduction_vs_7x19_percent": 5
        },

        "dyform_compacted": {
            "description_de": "Verdichteter Draht — äußere Litzen werden gepresst zu dichteren Paketen",
            "improvement_vs_standard_1x19_percent": 15,
            "stretch_advantage_percent": 10,
            "weight_reduction_percent": 8,
            "modulus_gpa": 200,
            "surface_area": "glätter als Standard-Draht — weniger Verschleiß an Rollen",
            "price_multiplier": 1.3,
            "note_de": "Hergestellt durch Kaltpressung nach Verzögelung — nicht zu verwechseln mit Dyneema/Kevlar"
        },

        "compacted_strand": {
            "description_de": "Hochleistungs-Strangdraht mit variablem Querschnitt",
            "core_design": "Hochfester Kern mit äußerem Schutzmantel",
            "improvement_vs_1x19_percent": 25,
            "fatigue_resistance": "überlegen (bis 50% längere Lebensdauer)",
            "surface": "sehr glatt für niedrigen Luftwiderstand",
            "anwendung": "Hochleistungs-Rennsegler, Yachtclub-Flotten",
            "note_de": "Hersteller: Samson Rope (USA), Force 4 (UK)"
        }
    },

    "rod_rigging": {
        "navtec_nitronic_50": {
            "material": "Nitronic 50 (17.4 PH Grade, AMS 5630)",
            "manufacturer": "NavTec (Australien), gegründet 1989",
            "properties": {
                "stiffness_vs_wire_percent": 130,
                "weight_vs_wire_percent": 150,
                "net_weight_reduction": "30% bei gleicher Steifigkeit",
                "corrosion_resistance": "Überlegen gegenüber 316 Edelstahl (15.5Cr, 17Ni gegenüber 16-18Cr, 10-14Ni)",
                "tensile_strength_mpa": 1310
            },
            "lifespan_years": 11,
            "lifespan_nm": 30000,
            "fatigue_rating": "A (höchste Kategorie)",
            "termination": "Kaltfließpressung (Cold Heading) — so stark wie Stange selbst",
            "diameter_range_mm": "6-12",
            "cost_vs_1x19_wire_multiple": 3.5,
            "warning_de": "Rod versagt OHNE Vorwarnung durch Einzeldrahtbrüche! Inspektionen mit Dye-Penetrant oder Ultraschall erforderlich.",
            "maintenance": "Jährliche Überprüfung auf Oberflächenrisse mit Oberflächenrisssprühverfahren",
            "failure_mode": "Transversalbruch ohne Ankündigung — Draht gibt vorher Warnsignale",
            "note_de": "Ideal für hochlastiges Rennsegelzeugs, Less-Is-More Ansatz"
        },

        "carbon_fiber_rod": {
            "material": "Carbon-Faser-composite mit Epoxidharz",
            "stiffness_vs_steel_percent": 150,
            "weight_vs_steel_percent": 30,
            "corrosion": "vollständig immun",
            "note_de": "Experimentell und kostspielig. Nicht weitverbreitet. Termination ist Herausforderung (Komposite benötigen speziale Terminals).",
            "price_multiplier": 5,
            "warning_de": "Kann bei Überbelastung plötzlich versagen. Inspektionen sind schwierig."
        }
    }
}


TURNBUCKLE_DATABASE: Dict[str, Any] = {
    "types": {
        "open_body": {
            "description_de": "Offener Körper — Gewindezustand sichtbar, leichter, aber korrosionsanfälliger",
            "material": ["316L Edelstahl (häufig)", "303 Edelstahl (günstig, aber weniger korrosionsbeständig)"],
            "weight_reduction_percent": 15,
            "corrosion_risk": "höher — Gewinde kann oxidieren",
            "use_case": "Inlandreviere, Süßwasser, protected harbors"
        },
        "closed_body": {
            "description_de": "Geschlossener Körper — Gewinde geschützt, besserer Korrosionsschutz",
            "material": "316L Edelstahl, häufig mit Korrosionsschutz-Beschichtung",
            "weight_increase_percent": 15,
            "corrosion_protection": "ausgezeichnet",
            "use_case": "Offene See, Langfahrten, tropische Gewässer",
            "maintenance": "Jährlich öffnen und Gewinde kontrollieren"
        }
    },

    "thread_design": {
        "description_de": "Ein Ende Rechtsgewinde, anderes Ende Linksgewinde — Drehen des Körpers spannt beide Seiten gleichzeitig",
        "geometry_advantage": "Symmetrische Last auf beide Gewindeeingänge",
        "minimum_engagement_percent": 75,
        "example": "115mm Gewindeeingänge bei 150mm körperlänge",
        "pitch_metric": "M10 = 1.5mm Steigung, M12 = 1.75mm",
        "pitch_us": "3/8\" = 24 TPI, 1/2\" = 20 TPI",
        "installation_torque_guideline": "Hand-tight plus 1/4 Umdrehung mit Gabelschlüssel"
    },

    "locking_methods": {
        "cotter_pins": {
            "description_de": "Splittstifte — klassisch, zuverlässig, Größe muss passen",
            "material": "316L Edelstahl oder Monel (besser)",
            "diameter_range_mm": "1.6-3.2",
            "installation": [
                "1. Durch Körper und beide Gabeln einführen",
                "2. Vorne umbiegen und pressen",
                "3. Zinken müssen symmetrisch sein"
            ],
            "reusable": False,
            "cost_cents": 0.15,
            "note_de": "Muss nach jeder Spannungsveränderung kontrolliert werden"
        },

        "lock_nuts": {
            "description_de": "Selbstsichernde Muttern (Nylon-Einsatz oder Serrations)",
            "type_nylon": "Nylon-Einsatz schwächt leicht (5-10% Festigkeit)",
            "type_serrated": "Sperrzähne — keine Schwächung, aber schwerer zu montieren",
            "reusable": "2-3 mal",
            "note_de": "Nylon nutzt sich ab — nach 2-3 Verwendungen ersetzen"
        },

        "lock_rings": {
            "description_de": "Integrierte Sicherungsringe — kein Werkzeug nötig, federgespannt",
            "material": "316L Edelstahl oder Monel",
            "installation": "Auf Gewindezapfen schieben, automatisch einrasten",
            "advantage": "Zuverlässig, kein Werkzeug erforderlich, wiederverwendbar",
            "disadvantage": "Kann unter Vibration lockern — regelmäßig kontrollieren"
        },

        "monel_wire": {
            "description_de": "Monel-Sicherungsdraht — korrosionsbeständig, einfach anzubringen",
            "material": "Monel (Ni-Cu-Legierung), korrosionsbeständiger als 316L",
            "gauge": "0.8-1.2mm Durchmesser",
            "installation": [
                "1. Durch Körper-Bohrung und Gabelaugen fädeln",
                "2. Verdrillen und festziehen",
                "3. Zwicken mit Bolzenschneider"
            ],
            "reusable": False,
            "note_de": "Favoritisiert in Segler-Gemeinschaft — visuell inspizierbar"
        },

        "loctite": {
            "description_de": "Loctite 242 (blau, lösbar) oder 271 (rot, permanent) für Gewindesicherung",
            "blue_242": {
                "strength": "mittel",
                "temperature_max_c": 150,
                "cure_time_hours": 24,
                "removable": True,
                "use": "Normalbetrieb, wartungszugang wichtig"
            },
            "red_271": {
                "strength": "hoch",
                "temperature_max_c": 200,
                "cure_time_hours": 24,
                "removable": "nur mit Wärmezufuhr (Heißluftfön, 80-100°C)",
                "use": "Permanente Montage"
            },
            "note_de": "Gewindeflächen müssen sauber und trocken sein — Fettfreiheit erforderlich"
        }
    },

    "sizing_examples": {
        "3_8_inch_unc": {
            "breaking_load_kg": 3500,
            "thread_type": "UNC",
            "body_diameter_inch": 0.625,
            "closed_length_mm": 95,
            "weight_g": 180
        },
        "m10_metric": {
            "breaking_load_kg": 4200,
            "thread_type": "M10 × 1.5",
            "body_diameter_mm": 16,
            "closed_length_mm": 115,
            "weight_g": 210
        },
        "5_16_inch_unc": {
            "breaking_load_kg": 2100,
            "thread_type": "UNC",
            "body_diameter_inch": 0.5,
            "closed_length_mm": 80,
            "weight_g": 100
        }
    },

    "maintenance_schedule": {
        "before_season": "Alle Wantenspanner sichtprüfen, Gewindefläche auf Oxidation kontrollieren",
        "monthly_cruising": "Sicherungsstifte kontrollieren, bei Vibration nachziehen",
        "annually": "Alle Spanner öffnen, Gewinde reinigen und mit PTFE-Schmierfett fetten",
        "every_3_years": "Nylon-Muttern ersetzen, komplette Neusicherung"
    }
}


SHACKLE_DATABASE: Dict[str, Any] = {
    "wichard": {
        "manufacturer": "Wichard (Frankreich, gegründet 1842)",
        "material_standard": "316L Edelstahl",

        "self_locking_bow": [
            {
                "diameter_mm": 6,
                "material": "316L",
                "breaking_load_kg": 1700,
                "swl_kg": 340,
                "weight_g": 12
            },
            {
                "diameter_mm": 8,
                "material": "316L",
                "breaking_load_kg": 3000,
                "swl_kg": 600,
                "weight_g": 21
            },
            {
                "diameter_mm": 10,
                "material": "316L",
                "breaking_load_kg": 4700,
                "swl_kg": 940,
                "weight_g": 33
            },
            {
                "diameter_mm": 12,
                "material": "316L",
                "breaking_load_kg": 6800,
                "swl_kg": 1360,
                "weight_g": 48
            },
            {
                "diameter_mm": 16,
                "material": "316L",
                "breaking_load_kg": 12000,
                "swl_kg": 2400,
                "weight_g": 85
            },
            {
                "diameter_mm": 20,
                "material": "316L",
                "breaking_load_kg": 18750,
                "swl_kg": 3750,
                "weight_g": 133
            }
        ],

        "hr_high_resistance": {
            "material": "17.4 PH Edelstahl (Precipitation Hardening)",
            "strength_vs_316L_percent": 160,
            "corrosion_resistance_vs_316_percent": 160,
            "sizes_mm": [12, 14, 20, 24],
            "breaking_load_12mm_kg": 10800,
            "note_de": "Besonders widerstandsfähig gegen Spannungsrisskorrosion (SCC)"
        },

        "snap_shackles": {
            "mechanism_de": "Federbelasteter Schnappverschluss mit Sicherheitsriegel",
            "release_types": [
                "Manuell — Finger auf Sicherung drücken",
                "Kontroll-Leine (Quick Release unter Last) — Drahtleine zum Verschluss führt"
            ],
            "configurations": ["Fixed bail", "Swivel bail", "Pin shackle bail"],
            "material": "HR Edelstahl (17.4 PH)",
            "sizes_mm": [8, 10, 12, 16],
            "mechanism_detail": "Kugel-Rast-Mechanismus mit Federspeichung",
            "advantage": "Schnelle Entlastung ohne Werkzeug, ideal für Genua-Augen und Traveller"
        }
    },

    "ronstan": {
        "manufacturer": "Ronstan (Australien, gegründet 1967)",
        "specialization": "Hochwertige Rennsegelkomponenten",
        "material": "316L Edelstahl und Aluminium-Bronze",
        "sizes_mm": [6, 8, 10, 12, 16, 20],
        "feature_de": "Hochpolierte Oberflächen, optimierte Geometrie für Leichtigkeit"
    },

    "safety_factor": {
        "working_load_limit_factor": 5,
        "formula": "WLL = Bruchlast / 5",
        "example_8mm": "4700 kg ÷ 5 = 940 kg WLL",
        "note_de": "Basierend auf ASME B30.20 und DIN standards"
    },

    "pin_types": {
        "screw_pin": {
            "description_de": "Gewinde-Stift — Standard, häufigste Variante",
            "installation": "Mit Schraubenschlüssel festziehen (Hand-tight + 1/4 Umdrehung)",
            "removal": "Schraubenschlüssel erforderlich",
            "risk": "Kann unter Vibration lockern",
            "sealing": "Optional mit Loctite 242"
        },
        "bolt_pin": {
            "description_de": "Bolzen mit Splint — seltener, besonders sicher",
            "installation": "Bolzen durchschieben, Splint einführen",
            "removal": "Splint entfernen, Bolzen herausziehen",
            "advantage": "Kann nicht versehentlich gelöst werden",
            "disadvantage": "Benötigt Splintloch — nicht alle Schäkel haben es"
        },
        "captive_pin": {
            "description_de": "Gefangener Stift — kann nicht verloren gehen. Bevorzugt für Marine!",
            "mechanism": "Stift mit Kette/Seil befestigt oder in Schäkel integriert",
            "installation": "Einfach durchschieben, automatisch gesichert",
            "advantage": "Stift kann nicht verloren gehen, Vibrations-sicher",
            "disadvantage": "Etwas schwerer, komplexer herzustellen"
        }
    },

    "d_shackle_loads_kg": {
        "6mm": 1700,
        "8mm": 3000,
        "10mm": 5000,
        "12mm": 7000,
        "16mm": 12000,
        "20mm": 18750,
        "24mm": 27000
    },

    "shackle_selection_guide": {
        "boat_10m_30ft": "8-10mm Schäkel für Hauptanschlussstellen",
        "boat_13m_40ft": "12mm Schäkel für Hauptzugsystem, 10mm für sekundär",
        "boat_16m_50ft": "16mm Schäkel für kritische Punkte, 12-14mm Standard",
        "large_yacht_over_50ft": "20mm+ Schäkel für Mastfuß, HR-Material empfohlen"
    }
}


ANCHOR_SYSTEM_DATABASE: Dict[str, Any] = {
    "anchor_types": {
        "rocna": {
            "manufacturer": "Rocna Anchor Ltd (Neuseeland)",
            "type": "Roll-Bar Design, ballastlos (ballast-less)",
            "invented": 2004,
            "patent_expired": 2024,
            "holding_power_comparison": "40% mehr Haltekraft als nächster Konkurrent (Spade) in West Marine Tests 2017",
            "min_holding_lbs": 4500,
            "strengths": [
                "Sand — ausgezeichnet",
                "Schlamm — ausgezeichnet",
                "Sofortiges Eingraben ohne Zurückrollen",
                "Konstante Tiefenpenetration unabhängig von Kettenvektor",
                "Saubere Flükenachbeschaffung beim Auswiegen"
            ],
            "weaknesses": [
                "Preis (höchste Kategorie, 2-3× teurer als Budget-Anker)",
                "Gewicht (schwer, erschwert Transport)",
                "Weed (Seegras kann sich verfangen)"
            ],
            "sizes_lbs": [22, 33, 44, 55, 66],
            "sizes_kg": [10, 15, 20, 25, 30],
            "depth_range_m": "2-40m optimal",
            "rating": "5/5 Sterne für vertrauensvolle Ankerer"
        },

        "mantus": {
            "manufacturer": "Mantus Anchors (USA, gegründet 2012)",
            "type": "Roll-Bar Design (ähnlich Rocna, aber unabhängig entwickelt)",
            "patent_status": "Unabhängig von Rocna-Patent",
            "note_de": "Nahezu äquivalente Leistung zu Rocna (bereinigt um 13% Gewichtsdifferenz)",
            "holding_vs_bruce_percent": 280,
            "strengths": [
                "Sand — ausgezeichnet",
                "Schlamm — ausgezeichnet",
                "Gutes Preis-Leistungs-Verhältnis (30-40% billiger als Rocna)",
                "Schneller Kundenservice (USA-basiert)"
            ],
            "sizes_lbs": [25, 35, 45, 60],
            "depth_range_m": "1-45m",
            "rating": "4.5/5 Sterne — beste Budget-Premium-Option"
        },

        "spade": {
            "manufacturer": "Spade Anchors (Schweden)",
            "type": "Blei-ballastiertes Design mit hohem Schub",
            "holding_vs_bruce_percent": 150,
            "strengths": [
                "Allgrund-Performance (Sand, Schlamm, Gras)",
                "Schnelles Eingraben",
                "Gutes Felsverhalten"
            ],
            "weaknesses": [
                "Teurer als Budget-Anker",
                "Schwer (Blei-Ballast)",
                "Etwas weniger gut in Schlamm als Rocna/Mantus"
            ],
            "sizes_kg": [10, 15, 20, 25, 30, 35],
            "depth_range_m": "2-50m",
            "rating": "4/5 Sterne für allgemeinen Cruising"
        },

        "fortress": {
            "manufacturer": "Fortress Anchors (USA)",
            "type": "Aluminium-Magnesium Plattenanker (Danforth-Typ)",
            "weight_range_lbs": [4, 8, 15, 21],
            "weight_range_kg": [1.8, 3.6, 6.8, 9.5],
            "fluke_angles_settings": {
                "sand": 32,
                "mud": 45
            },
            "mud_palm_benefit_de": "Schlammflügel erhöhen Schlammhaltekraft um bis zu 400%",
            "strengths": [
                "Ultra-leicht — ideal für Cruiser mit geringer Bugkraft",
                "Vollständig einstellbar — Flukenwinkel schnell veränderbar",
                "Schnelles Eingraben in Sand",
                "Ideal als Zweitanker/Heckanker"
            ],
            "weaknesses": [
                "Seegras und Algen können sich verfangen",
                "Fels und harter Boden: schlechtes Eingraben",
                "Weniger Haltekraft als Roll-Bar-Designs",
                "Kann hinten ausrollen bei Kettenvektor-Änderung"
            ],
            "depth_range_m": "2-30m",
            "rating": "3.5/5 Sterne — nur für spezialisierte Anwendungen"
        },

        "cqr_plow": {
            "type": "Pflug (Gelenk-Design), Ein-Stück, ähnlich Danforth",
            "status": "veraltet",
            "current_rating": "konsistent schlecht in unabhängigen Tests (Nächster Partner ist Rocna um 40% besser)",
            "note_de": "NICHT mehr empfohlen für Neuanschaffungen. Nur verwenden, wenn bereits vorhanden.",
            "holding_vs_fortress": "15-20% schlechter",
            "reason_poor_performance": "Gelenkdesign erlaubt Kippeln bei Windvektor-Änderungen"
        },

        "bruce_claw": {
            "type": "Klaue (Gelenk-Design, 3-Flügel)",
            "status": "veraltet, aber funktional",
            "note_de": "Solider Allround-Anker, aber übertroffen von modernen Designs um 30-50%",
            "holding_vs_spade_percent": 67,
            "current_use": "Gelegentlich auf älteren Yachten, Backup-Anker",
            "recommendation": "Ersetzen durch Mantus oder Rocna bei nächster Gelegenheit"
        },

        "delta": {
            "type": "Einteiliger Pflug (Deltasub-Design)",
            "holding_vs_bruce_percent": 150,
            "rating": "3.5/5 — gute Mittelklasse für Allground",
            "strengths": ["Schnelles Eingraben", "Symmetrischer Aufbau"],
            "weaknesses": ["Kann in Seegras festhängen", "Weniger Schlammhaltung als Spade"]
        }
    },

    "sizing_principle_de": "Verdrängung (Gesamtgewicht beladen) ist WICHTIGER als Bootslänge! Immer nach Gewichtsklasse dimensionieren.",

    "sizing_rule_of_thumb": {
        "rule": "1 lb Anker pro 1.000 lbs Verdrängung (oder ca. 0.5 kg Anker pro Tonne Verdrängung)",
        "example_40ft_boat": {
            "displacement_tons": 18,
            "anchor_weight_kg": 9,
            "recommended_rocna_lbs": 33,
            "recommended_mantus_lbs": 35,
            "recommended_spade_kg": 15
        }
    },

    "chain_specifications": {
        "standards": ["DIN 766 (Europa)", "ISO 4565", "BBB (USA — nicht für Marine!)"],

        "grades": {
            "g30": {
                "composition": "Längsfaserverkettung, niedriger Kohlenstoffgehalt",
                "breaking_8mm_kg": 3200,
                "swl_8mm_kg": 800,
                "weight_8mm_per_m_kg": 1.4,
                "note_de": "Leichte Kette, günstig, aber niedriger Widerstand",
                "use_case": "Fischerboote, innere Gewässer, nicht für Segelyachten empfohlen"
            },

            "g40": {
                "composition": "Mittlerer Kohlenstoffgehalt, gehärtet",
                "breaking_8mm_kg": 4700,
                "swl_8mm_kg": 1175,
                "weight_8mm_per_m_kg": 1.4,
                "note_de": "Am weitesten verbreitet, gutes Verhältnis Stärke/Preis",
                "use_case": "Standard für Segelyachten, Fahrtensegler, Cruiser",
                "cost_index": 1.0
            },

            "g70": {
                "composition": "Hochkohlenstoff, gehärtet und angelassen, Spezialstahl",
                "breaking_8mm_kg": 6800,
                "swl_8mm_kg": 1700,
                "weight_8mm_per_m_kg": 1.5,
                "note_de": "Hochfest — ~20% weniger Buggewicht bei gleicher Bruchlast wie G40 eine Größe darüber",
                "use_case": "Performance-Cruiser, schwere Verdränger, Sturmsicherung",
                "cost_index": 2.5,
                "weight_saving_100m_kg": 10
            }
        },

        "standard": "DIN 766 / ISO 4565",

        "diameter_guide": {
            "4mm": {"use": "Leichte Daysailer bis 20 Fuß", "g40_swl_kg": 525},
            "5mm": {"use": "Kleine Cruiser bis 25 Fuß", "g40_swl_kg": 820},
            "6mm": {"use": "Leichte Boote bis 30 Fuß, Tagessegler", "g40_swl_kg": 1180},
            "8mm": {"use": "Fahrtensegler 30-40 Fuß, Haupt-Arbeitskette", "g40_swl_kg": 1175},
            "10mm": {"use": "Boote 40-50 Fuß, Allzweck", "g40_swl_kg": 1840},
            "12mm": {"use": "Große Boote 50+ Fuß, Sturmanker, schwere Verdränger", "g40_swl_kg": 2650}
        },

        "material": {
            "galvanized_steel": {
                "cost": "niedrig",
                "corrosion": "Zink-Beschichtung verschleißt über 3-5 Jahre",
                "grip": "höher (rutscht weniger im Kettenkasten)",
                "inspection": "Jährlich auf Zink-Erosion kontrollieren",
                "advantage": "Billiger Ersatz",
                "disadvantage": "Kann Flecken auf Rumpf hinterlassen"
            },

            "stainless_316": {
                "cost": "hoch (4-5× teurer als verzinkt)",
                "corrosion": "hervorragend — praktisch ewig",
                "grip": "glatter (besser verteilt sich im Kettenkasten)",
                "magnetic": False,
                "note_de": "NIEMALS Edelstahl und verzinkt mischen — galvanische Korrosion!",
                "advantage": "Wartungsfrei, hervorragende Korrosionsbeständigkeit",
                "disadvantage": "Hohe Anschaffungskosten",
                "lifespan_years": "50+"
            }
        },

        "length_guidelines": {
            "light_weather": "100m Kette + 100m Seil",
            "normal_cruising": "150m Kette + 50m Seil",
            "heavy_weather": "200m Kette + Minimales Seil",
            "note_de": "Kettengewicht stabilisiert Zugwinkel — mindestens 30m sollten immer Kette sein"
        }
    },

    "rode_types": {
        "all_chain": {
            "pros_de": [
                "Kein Scheuerschutz an Ankerrolle nötig",
                "Windlass-kompatibel (horizontal möglich)",
                "Kettengewicht hält Zug horizontal statt vertikal — bessere Ankerhaltung",
                "Resistenter gegen Scharfkanten/Felsen",
                "Wartungsfrei"
            ],
            "cons_de": [
                "Extremes Gewicht (100m 12mm G40 = 300kg)",
                "Keine Stoßdämpfung — Schlagbelastungen bei Wind",
                "Schnorkel (Snubber) ERFORDERLICH aus Nylon — Kette kann Schocks nicht absorbieren",
                "Beeinflusst Segeleigenschaften (erhöhte Ruhemasse)",
                "Schwieriger zu lagern (Kettenkasten muss ausreichend dimensioniert)"
            ],
            "note_de": "IMMER Schnorkel (Snubber) aus Nylon verwenden — kritisch für Kettencomfort!",
            "required_snubber_diameter_mm": 16,
            "snubber_length_m": 6
        },

        "chain_rope_combo": {
            "chain_length_m": "18-30 (60-100 ft)",
            "rope_material": "3-Strang Nylon oder Nylon-Core Mixed",
            "rope_diameter_mm": "12-16",
            "pros_de": [
                "Leichter als all-chain (Gewicht 40% weniger)",
                "Stoßdämpfung eingebaut durch Nylon-Dehnung",
                "Einfacher ohne Windlass (manuell möglich)",
                "Kompaktere Lagerung",
                "Optimales Gewicht-Leistungs-Verhältnis für cruiser"
            ],
            "cons_de": [
                "Scheuerschutz an Ankerrolle nötig (Polypropylen-Schutzschlauch)",
                "Nicht ideal für Korallen oder scharfkantigen Felsen",
                "Rope kann verfaulen wenn nicht trocken gelagert",
                "Splicing erforderlich für sichere Verbindung"
            ],
            "recommended_for": "Die meisten Fahrtensegler 30-45 Fuß",
            "note_de": "Nylon dehnt sich bis 25% — dies ist Stoßdämpfung!"
        }
    }
}


WINDLASS_DATABASE: Dict[str, Any] = {
    "types": {
        "vertical": {
            "description_de": "Kette tritt horizontal ein, 180° um Kettennuss, fällt in Kasten",
            "motor_location": "Im Kettenkasten (weniger Deck-Clutter, zentrale Gewichtsverteilung)",
            "min_fall_mm": 400,
            "orientation": "Motor oben, Kettennuss unten, vertikal montiert",
            "gearing": "Kegel-Zahnräder übertragen Kraft um 90°",
            "brands": [
                "Lofrans (Modelle X1, X2, X3, X4, Ercole)",
                "Lewmar (V2, V3)",
                "Quick (Wildcat)"
            ],
            "advantage": "Kompakt, zentrale Gewichtslage",
            "disadvantage": "Schwieriger zu servieren (Motor im Kasten)"
        },

        "horizontal": {
            "description_de": "Kette tritt horizontal ein, 90°-Umlenkung in Kasten",
            "motor_location": "Auf Deck (horizontal montiert, deckzentriert)",
            "min_fall_mm": 300,
            "advantage_de": "Beste Performance, toleranter bei kleinen Kettenkästen, einfache Wartung",
            "disadvantage_de": "Mehr Deck-Clutter, höhere Gewichtslage (beeinträchtigt Stabilität)",
            "brands": [
                "Lewmar (Professional Horizontal)",
                "Quick (mit Horizontal-Option)",
                "Maxwell"
            ],
            "preferred_for": "Große Yachten, Performance-Cruiser, Schiffe mit viel Zug"
        }
    },

    "sizing": {
        "principle_de": "Windlass muss mindestens 3× das Gewicht von Anker + Kette + Rode heben können",
        "example": {
            "boat_40ft": {
                "anchor_kg": 15,
                "chain_100m_8mm_g40_kg": 140,
                "rope_100m_14mm_nylon_kg": 35,
                "total_kg": 190,
                "minimum_windlass_pull_kg": 570,
                "recommended_model": "Lofrans X3 oder Lewmar V3"
            }
        }
    },

    "power_options": {
        "electric_12v": {
            "voltage": 12,
            "current_draw_amps": "100-200",
            "duration": "5-10 Min bei voller Kraft",
            "note_de": "Benötigt schwere Kabel (4-6 AWG), gute Batterie"
        },
        "electric_24v": {
            "voltage": 24,
            "current_draw_amps": "50-100",
            "duration": "10-15 Min",
            "advantage": "Niedrigere Ströme als 12V, leichtere Verkabelung"
        },
        "hydraulic": {
            "advantage": "Unendliche Kraft, ideal für große Schiffe",
            "disadvantage": "Komplex, wartungsintensiv, teuer"
        }
    }
}


STEERING_SYSTEM_DATABASE: Dict[str, Any] = {
    "types": {
        "cable": {
            "description_de": "Seilzug-Steuerung — leicht, einfach, dehnbar mit der Zeit",
            "mechanism": "Stahlseile über Rollen/Doppelrollen, 1:1 Übersetzung oder mit Getriebe",
            "lifespan_years": "5-7 (Seil)",
            "maintenance": "Jährlich: Seile schmieren, Rolle auf Verschleiß kontrollieren",
            "advantage": "Einfach, wartbar, preiswert",
            "disadvantage": "Dehnung mit Zeit, Verschleiß an Seil"
        },

        "chain": {
            "description_de": "Ketten-Steuerung — weniger Dehnung, schwerer, präziser",
            "mechanism": "G40-Stahlkette über Zahnrollen",
            "lifespan_years": "10-15",
            "maintenance": "Jährlich: Kette schmieren und auf Verschleiß kontrollieren",
            "advantage": "Weniger Dehnung, langlebig, präzise",
            "disadvantage": "Schwerer, komplexer"
        },

        "rack_pinion": {
            "description_de": "Zahnstange/Ritzel — präzise, für große Boote, hydraulisch verstärkt",
            "mechanism": "Ritzel in Zahnstange, hydraulische Servolenkung optional",
            "lifespan_years": "20+",
            "maintenance": "Ölwechsel (Servo), minimale mechanische Wartung",
            "advantage": "Hochpräzise, wenig Spiel, langlebig",
            "disadvantage": "Teuer, komplex"
        }
    },

    "manufacturers": {
        "jefa": {
            "country": "Schweden",
            "description_de": "Weltmarktführer für Performance-Segelyacht-Steuerung",
            "system": "TSS (Transmission Steering System) — Kegelgetriebe, Torsionsrohre, Stützlager",
            "models": ["TSS Pro", "TSS Race", "TSS Inshore"],
            "feature": "Optimiert für High-Load-Rennsegelzeugs"
        },

        "whitlock_lewmar": {
            "description_de": "Cobra Radsteuerung — komplett Seil-, Ketten-, Zahnstangen-Optionen",
            "status": "Jetzt unter Lewmar (2010 Übernahme)",
            "models": ["Cobra Solo", "Cobra Pro", "Cobra Hydraulic"]
        },

        "lewmar": {
            "country": "USA",
            "description_de": "Vollständiger Hersteller von Steuer- und hydraulischen Systemen",
            "focus": ["Mechanische Segelsteuerung", "Hydraulische Servolenkung", "Autopilot-Systeme"]
        }
    },

    "rudder_bearings": {
        "sleeve_plain": {
            "material": ["Bronze", "Messing", "Composite (PETP)"],
            "load_capacity": "mittel",
            "maintenance": "regelmäßig schmieren (alle 2-3 Wochen)",
            "lifespan_years": 8,
            "cost": "niedrig"
        },

        "roller": {
            "material": "Zylindrische Rollenlager (4-6 Rollen)",
            "load_capacity": "hoch",
            "for": "Schwere Verdränger, Motorsailors",
            "advantage": "Sehr hohe Tragfähigkeit",
            "disadvantage": "Kann korrodieren, Wartung erforderlich"
        },

        "composite_self_lubricating": {
            "material": ["PETP (Ertalyte)", "Thordon SXL"],
            "load_capacity": "hoch",
            "maintenance": "keine",
            "note_de": "Selbstschmierend, salzwasserbeständig, Betriebsdruck bis 12 N/mm²",
            "lifespan_years": 15,
            "advantage": "Wartungsfrei, korrosionsimmun",
            "cost": "hoch"
        },

        "ptfe": {
            "material": "PTFE/Graphit auf Bronze-Sinterschicht",
            "load_capacity": "mittel",
            "friction": "sehr niedrig",
            "advantage": "Niedriger Reibungswiderstand, wartungsarm",
            "use": "Standard für moderne Segelyachten"
        }
    },

    "autopilot_rams": {
        "type_1": {
            "thrust_kg": 350,
            "max_torque_nm": 1770,
            "max_stroke_mm": 300,
            "for": "Kleinere Boote 25-30 Fuß",
            "power_consumption_amps": 20
        },

        "type_2": {
            "max_torque_nm": 1270,
            "max_stroke_mm": 254,
            "max_displacement_kg": 22000,
            "for": "Mittelgroße Fahrtensegler 35-45 Fuß",
            "power_consumption_amps": 35
        },

        "type_3": {
            "max_displacement_kg": 35000,
            "for": "Größere Yachten 50+ Fuß",
            "power_consumption_amps": 50,
            "hydraulic_option": "Ja"
        }
    },

    "emergency_tiller": {
        "requirement_de": "Muss funktionsfähig und leicht zugänglich sein. Jährlich testen!",
        "force_limit_lbs": 30,
        "force_limit_kg": 13.6,
        "specification_de": "Ruder muss 15° je Seite innerhalb 60 Sekunden drehen können",
        "installation": [
            "1. Direkt auf Ruderkopf geschraubt oder gesteckt",
            "2. Griff mindestens 600mm lang",
            "3. Lagerung: leicht zugänglich, nicht unter Segel"
        ],
        "testing": "Monatlich trocken drehen, 2× pro Saison unter Last testen"
    },

    "cable_maintenance": {
        "inspection_frequency": "2-3× pro Saison, jährlich Komplett-Check",
        "lubrication": "Wasserfestes Lithium-Marine-Fett, per Fettpresse eingeführt",
        "replacement_indicators": [
            "Mantel gerissen oder beschädigt",
            "Korrosion oder Rost am Seil",
            "Schwergängiges Ruder (Verschleiß an Rollen)",
            "Sichtbare Litzenschäden oder Knicke",
            "Seil gedehnt oder mit Knoten verbeultes Aussehen",
            "Rauhe Oberfläche (Oxidation durchgebrochen)"
        ],
        "warning_de": "Steuerseile können NICHT repariert werden — bei Verschleiß komplett austauschen!",
        "inspection_points": [
            "Rad und Nabe auf Verschleiß",
            "Rollen auf Beweglichkeit testen",
            "Seil auf Kratzer/Dellen kontrollieren",
            "Lagerkörper auf Risse prüfen"
        ]
    }
}


THROUGH_HULL_DATABASE: Dict[str, Any] = {
    "groco": {
        "material_small": "C83600 Bronze (1/2-3 Zoll)",
        "material_large": "C84400 Bronze (4-5 Zoll)",
        "certification": "UL 647B",
        "thread": "NPSM/NPT Kombinationsgewinde",
        "feature_de": "Flansch-Kontermutter für sichere, wasserdichte Verbindung",
        "sizes_inch": [0.5, 0.75, 1, 1.25, 1.5, 2],
        "ball_seal": "Elastomer-PTFE",
        "pressure_rating_psi": 50,
        "temperature_range_c": "-40 bis +65",
        "warranty_years": "Lebenslang"
    },

    "trudesign": {
        "material": "Glasfaserverstärktes Nylon-Composite",
        "ball_seal": "PTFE-Polymer",
        "temperature_range_c": "-40 bis +80",
        "galvanic_neutral": True,
        "weight": "leichter als Bronze (ca. 50% weniger)",
        "thread": "NPS (parallel, US-Markt)",
        "advantage": ["Keine galvanische Korrosion möglich", "Leicht", "UV-beständig"],
        "disadvantage": ["Weniger steif als Bronze", "Höhere Kosten"],
        "pressure_rating_psi": 60
    },

    "blakes": {
        "type": "Konischer Kegelventil (Tapered Cone Plug)",
        "material": "85-5-5-5 Rotguss",
        "feature_de": "Kegel und Gehäuse sind aneinander eingeschliffen — NICHT austauschbar zwischen Einheiten!",
        "service_de": "In-situ justierbar, komplett zerlegbar, klassisches Design",
        "sizes_inch": [0.75, 1, 1.25, 1.5],
        "lifespan_years": "50+ (wartbar)",
        "note_de": "Wird gelegentlich auf älteren Yachten gefunden, teuer zu ersetzen"
    },

    "bronze_alloy_85_5_5_5": {
        "composition": {
            "copper": 85,
            "tin": 5,
            "lead": 5,
            "zinc": 5
        },
        "dezincification_immunity": True,
        "corrosion_resistance": "Ausgezeichnet in Salzwasser",
        "note_de": "Kupferlegierungen mit < 6% Zink sind immun gegen Entzinkung",
        "advantage": "Standard-Seebronze, bewährte Zusammensetzung seit 1900"
    },

    "ball_vs_cone_valve": {
        "ball_valve": {
            "mechanism_de": "Hartverchromte Kugel dreht auf PTFE-Dichtungen",
            "maintenance": "Jährlich wasserfestes Fett beidseitig per Fettpresse einbringen",
            "lifespan_years": 10,
            "advantage": "Einfach zu bedienen, schnell zu sperren",
            "warning_de": "ECHTE Seeventile haben integrierte Flansche! Inline-Kugelventile sind KEINE Seeventile — können bei Unfällen platzen!"
        },

        "cone_valve": {
            "mechanism_de": "Konischer Stopfen in eingeschliffenem Gehäuse",
            "maintenance": "Jährlich zerlegen, reinigen, Schlifflächen nachschleifen mit feinem Schleifpulver, neu fetten",
            "lifespan_years": 50,
            "advantage": "Reparierbar, wartbar, nie völlig blockierbar (Schmodder dringt nicht in Gewinde)",
            "disadvantage": "Schwieriger zu bedienen, höhere Wartung"
        }
    },

    "backing_block": {
        "solid_grp": {
            "material": "19mm Marine-Sperrholz Klasse A",
            "shape": "Rund bevorzugt (durchmesser 200-300mm)",
            "thickness_mm": 19,
            "bonding": "Mit Epoxidharz an Rumpf kleben — nicht nur als Unterlegscheibe verwenden!"
        },

        "sandwich_hull": {
            "material": "16mm G-10 (Glasfaser-Composite)",
            "diameter_mm": 200,
            "advantage": "Weit bessere Langzeitstabilität als Sperrholz in feuchten Bereichen"
        },

        "alternative": {
            "material": "GPO-3 (Glasfaser-Phenolharz)",
            "thickness_mm": 16,
            "advantage": "Korrosionsimmun, chemikalienbeständig"
        },

        "bonding_de": "Mit Epoxid an Rumpf kleben — nicht nur als Unterlegscheibe verwenden"
    },

    "hose_connections": {
        "barb": {
            "mechanism_de": "Gezackte Widerhaken greifen in Schlauch-Innenwand",
            "pressure_max_psi": 125,
            "installation_de": [
                "1. Schlauch in heißem Wasser (ca. 60°C) für 30 Sekunden erwärmen",
                "2. Mit Glycerin oder Seifenwasser schmieren",
                "3. Vollständig über Barbs aufschieben (bis zum Anschlag)",
                "4. Sofort abkühlen lassen — Schlauch kontrahiert und greift"
            ],
            "clamps": "MINIMUM 2 Schlauchschellen (Doppelschellen-Regel!)",
            "clamp_spacing_mm": 100,
            "clamp_type": "Schlauchschellen nach DIN 3017 (Norm-Bandschelle)"
        },

        "threaded": {
            "standards": {
                "npt": {
                    "name": "National Pipe Thread (USA)",
                    "angle": "60° Gewindewinkel",
                    "taper": "konisch (1:16)",
                    "note": "De-facto Standard in Nord- und Südamerika"
                },
                "bsp_bspt": {
                    "name": "British Standard Pipe",
                    "angle": "55° Gewindewinkel",
                    "taper": "konisch",
                    "note": "Europäischer Standard (selten in Yacht-Hardware)"
                },
                "bspp": {
                    "name": "British Standard Parallel",
                    "angle": "55°",
                    "taper": "parallel (nicht konisch)",
                    "note": "Moderne europäische Hydraulik"
                },
                "npsm": {
                    "name": "National Straight Mechanical",
                    "angle": "60°",
                    "taper": "gerade (nicht konisch)",
                    "note": "Häufig bei Marine-Fittings mit O-Ring-Dichtung"
                }
            },
            "warning_de": "NPT und BSP NIEMALS mischen — unterschiedliche Gewindewinkel führen zu Undichtheiten!",
            "identification": "NPT = grobe Gewinde, BSP = feinere Gewinde"
        }
    }
}


# Zusammenfassung und praktische Anwendungsrichtiglinien
PRACTICAL_GUIDELINES: Dict[str, Any] = {
    "pre_season_rigging_checklist": [
        "Alle Wantenspanner kontrollieren — Splittstifte/Monel-Draht intakt?",
        "Alle Terminals inspektieren auf Risse, Korrosion, Verschleiß",
        "Shäkel-Pins auf Verschleiß und Korrosion kontrollieren",
        "Steuerseile schmieren und auf Verschleiß prüfen",
        "Anker und Kette kontrollieren — Gewicht und Material bestandskontrolle",
        "Windlass-Funktionsprüfung — Motor testet, Sicherungen kontrollieren",
        "Notfall-Ruder beweglich machen und testen",
        "Alle Borddurchlässe inspektieren auf Undichtheiten"
    ],

    "critical_safety_issues": {
        "rod_rigging": "KEIN Vorwarnzeichen vor Bruch — jährliche Ultraschall- oder Farbprüfung erforderlich!",
        "steering_cable": "Versagen führt zu Ruderlosigkeit — Austausch nicht aufschieben!",
        "chain_corrosion": "Galvanische Korrosion zwischen verzinkter und Edelstahl-Kette — NIEMALS mischen!",
        "through_hull": "Undichtheiten führen zu Sinken — regelmäßiges Schmieren und Wartung kritisch!"
    }
}


print("AYDI Rigging Hardware Knowledge Module Loaded Successfully")
