"""
AYDI Beschichtungs- und Dichtungssystem-Tiefenwissen
Exhaustive technical specifications for marine sealants, paints, varnishes, and epoxy systems.

Covers: Sikaflex, 3M, Bostik/Simson, West System, International, Hempel, Jotun, Epifanes
Application guides, compatibility matrices, cure times, coverage rates

Author: AYDI Research Team
Version: 1.0
"""

from typing import Dict, List, Any


SEALANT_DATABASE: Dict[str, Any] = {
    "types_comparison": {
        "polyurethane": {
            "name_de": "Polyurethan (PU)",
            "adhesion": "sehr hoch",
            "flexibility": "gut",
            "uv_resistance": "variabel",
            "paintable": True,
            "sandable": True,
            "underwater": True,
            "cure_mechanism": "Feuchtigkeitsaushärtung",
            "brands": ["Sikaflex 291/291i", "3M 5200", "Bostik 920"],
            "avoid_with": ["ABS", "Polycarbonat (Lexan)"],
            "best_for_de": "Strukturelle Verbindungen, Rumpf/Deck-Naht, Unterwasser"
        },
        "ms_polymer": {
            "name_de": "MS-Polymer / SMP (Silyl-modifiziertes Polymer)",
            "adhesion": "hoch",
            "flexibility": "hervorragend",
            "uv_resistance": "gut",
            "paintable": True,
            "sandable": True,
            "underwater": True,
            "cure_mechanism": "Feuchtigkeitsaushärtung",
            "brands": ["Sikaflex 591", "3M 4000UV", "3M 4200", "Bostik 940"],
            "advantage_de": "Frei von Isocyanat, Zinn, Lösungsmittel. Vergilbt nicht.",
            "best_for_de": "Deck-Hardware, Fenster, Universalabdichtung"
        },
        "polysulfide": {
            "name_de": "Polysulfid",
            "adhesion": "hoch",
            "flexibility": "gut",
            "uv_resistance": "gut",
            "paintable": True,
            "sandable": True,
            "underwater": True,
            "cure_mechanism": "Chemische Härtung (2K) oder Feuchtigkeitsaushärtung (1K)",
            "brands": ["BoatLife Life-Calk"],
            "chemical_resistance": "hervorragend",
            "best_for_de": "Teakdeck-Fugen (beständig gegen Teak-Öle), Unterwasser, traditionelle Bordnähte"
        },
        "silicone": {
            "name_de": "Silikon",
            "adhesion": "niedrig-mittel",
            "flexibility": "hervorragend",
            "uv_resistance": "gut",
            "paintable": False,
            "sandable": False,
            "underwater": "nur bedingt",
            "cure_mechanism": "Feuchtigkeitsaushärtung (Essigsäure oder neutral)",
            "brands": ["3M Marine Grade Silicone", "Dow Corning 795"],
            "note_de": "NICHT übermalbar! Silikonreste verhindern Haftung aller anderen Dichtmassen und Farben.",
            "best_for_de": "Kunststoff-Fenster, flexible Verbindungen über Wasser"
        },
        "butyl_tape": {
            "name_de": "Butylband / Butyl Tape",
            "adhesion": "mittel",
            "flexibility": "hervorragend",
            "uv_resistance": "gut (wenn abgedeckt)",
            "paintable": False,
            "sandable": False,
            "underwater": False,
            "cure_mechanism": "Nicht aushärtend (bleibt dauerhaft plastisch)",
            "brands": ["Bed-It Tape", "Compass Marine Butyl"],
            "specs": {"width_mm": 12.7, "thickness_mm": 1.6, "roll_length_m": 15},
            "best_for_de": "Bettung von Deck-Hardware, Luken, Klammern — wo spätere Demontage gewünscht"
        }
    },

    "application_matrix": {
        "description_de": "Welcher Dichtstoff für welche Anwendung",
        "applications": {
            "hull_deck_joint": {"recommended": ["3M 5200", "Sikaflex 291i"], "reason_de": "Höchste Klebkraft, strukturelle Verbindung, permanent"},
            "through_hull_below_wl": {"recommended": ["3M 5200", "Sikaflex 291"], "reason_de": "Permanent, wasserdicht, unterwasserbeständig"},
            "deck_hardware_removable": {"recommended": ["3M 4200", "Butyl Tape", "Sikaflex 591"], "reason_de": "Demontierbar, gute Dichtigkeit"},
            "deck_hardware_permanent": {"recommended": ["3M 5200", "Sikaflex 291"], "reason_de": "Maximale Festigkeit"},
            "windows_acrylic": {"recommended": ["3M 4000UV", "Sikaflex 295 UV"], "reason_de": "Vergilbt nicht, UV-beständig, greift Acryl nicht an"},
            "windows_glass": {"recommended": ["Sikaflex 295 UV", "Dow Corning 795"], "reason_de": "Strukturelle Verklebung, langzeitstabil"},
            "teak_deck_fugen": {"recommended": ["Sikaflex 290i DC", "BoatLife Life-Calk", "Bostik Simson DC"], "reason_de": "Beständig gegen Teak-Öle"},
            "keel_bolts": {"recommended": ["3M 5200"], "reason_de": "Höchste Festigkeit, permanent, wasserdicht"},
            "chainplates": {"recommended": ["Butyl Tape", "Sikaflex 591"], "reason_de": "Muss nachstellbar/demontierbar bleiben"},
            "engine_mounts": {"recommended": ["3M 4200", "Sikaflex 291"], "reason_de": "Vibrationsdämpfend, demontierbar"}
        }
    },

    "sikaflex_range": {
        "291i": {
            "type": "1K Polyurethan",
            "shore_a": 40,
            "elongation_percent": 600,
            "tensile_mpa": 2.5,
            "tack_free_min": 60,
            "full_cure_days": 3,
            "temp_range_c": "-40 bis +90",
            "imo_compliant": True,
            "note_de": "Marine-Universalkleber, IMO-zugelassen"
        },
        "295_uv": {
            "type": "1K Polyurethan",
            "shore_a": 35,
            "elongation_percent": 500,
            "tensile_psi": 290,
            "tack_free_min": 60,
            "temp_range_c": "-50 bis +90",
            "note_de": "Für Fensterverklebung und Unterwasser"
        },
        "591": {
            "type": "STP (Silanterminiertes Polymer)",
            "shore_a": 45,
            "elongation_percent": 600,
            "tensile_mpa": 1.8,
            "skin_formation_min": 35,
            "working_time_min": 20,
            "isocyanate_free": True,
            "tin_free": True,
            "pvc_free": True,
            "bonds_to": ["Gelcoat", "GFK", "Edelstahl", "Aluminium", "Kupfer", "Messing", "Bronze", "Holz", "Sperrholz"],
            "note_de": "Modernste Formel: frei von Isocyanat, Zinn, PVC. IMO FTP Part 5."
        },
        "290i_dc": {
            "type": "1K Polyurethan (Deck Caulk)",
            "note_de": "Speziell für Teakdeck-Fugen. Bond-Breaker (PE-Band) am Fugengrund verwenden!"
        }
    },

    "3m_range": {
        "5200": {
            "type": "Permanent Polyurethan",
            "tensile_psi": 700,
            "shore_a": 55,
            "elongation_percent": 400,
            "full_cure_days": "7-10",
            "note_de": "PERMANENT — nahezu unmöglich zu entfernen! Nur wo keine Demontage geplant."
        },
        "5200_fc": {
            "type": "Fast Cure Polyurethan",
            "tensile_psi": 1000,
            "shore_a": 60,
            "elongation_percent": 850,
            "tack_free_hours": "1-2",
            "full_cure_hours": 48,
            "overlap_shear_psi": 600
        },
        "4200": {
            "type": "Semi-permanentes Polyurethan",
            "tensile_psi": 300,
            "tack_free_hours": 1,
            "full_cure_hours": 24,
            "note_de": "Demontierbar mit Werkzeug. Für Hardware die später abgebaut werden muss."
        },
        "4000_uv": {
            "type": "SMP (Silanmodifiziertes Polymer)",
            "tensile_psi": 250,
            "shore_a": 40,
            "elongation_percent": 790,
            "tack_free_min": 20,
            "full_cure_hours": 24,
            "uv_resistant": True,
            "non_yellowing": True,
            "note_de": "Für Kunststoff-Fenster! Greift Acryl/Lexan NICHT an (anders als PU)."
        }
    }
}


EPOXY_SYSTEMS: Dict[str, Any] = {
    "west_system": {
        "manufacturer": "West System (Gougeon Brothers, USA)",
        "base_resin": {
            "product": "105 Epoxy Resin",
            "viscosity_cp": 1000,
            "color": "Klar, hellgelb",
            "shrinkage": "Keine (kein Lösungsmittel)",
            "bonds_to": ["Holz", "GFK", "Verstärkungsgewebe", "Schaum", "Composite", "Metall"]
        },
        "hardeners": {
            "205_fast": {
                "mix_ratio_weight": "5:1",
                "mix_ratio_volume_pumps": "3:1",
                "pot_life_min_72f": "9-12",
                "working_time_min": "60-70",
                "full_cure_hours": "6-8",
                "min_temp_c": 4,
                "best_for_de": "Standardarbeiten, schnelle Aushärtung, kalte Temperaturen"
            },
            "206_slow": {
                "mix_ratio_weight": "5:1",
                "pot_life_min_72f": "20-25",
                "working_time_min": "90-110",
                "full_cure_hours": "10-15",
                "min_temp_c": 16,
                "best_for_de": "Große Flächen, Laminierarbeiten, warme Temperaturen"
            },
            "207_special_clear": {
                "mix_ratio_volume": "3:1",
                "pot_life_min_72f": "22-26",
                "working_time_min": "110-120",
                "full_cure_hours": "10-15",
                "min_temp_c": 16,
                "uv_inhibitor": True,
                "best_for_de": "Klarlack-Finish, sichtbare Holzoberflächen, UV-Schutz"
            },
            "209_extra_slow": {
                "mix_ratio_volume": "3:1",
                "mix_ratio_weight": "3.5:1",
                "pot_life_hours": "3-4",
                "working_time_min": "110-120",
                "full_cure_hours": "20-24",
                "min_temp_c": 21,
                "best_for_de": "Große Mischmengen, komplexe Arbeiten, sehr lange Verarbeitungszeit"
            }
        },
        "fillers": {
            "403_microfibers": {"type": "Fasermischung", "use_de": "Verdicken für großflächige Verklebungen", "sandability": "schwer"},
            "404_high_density": {"type": "Hochdicht", "use_de": "Hardware-Verklebung, zyklische Hochlast", "sandability": "sehr schwer"},
            "405_filleting_blend": {"type": "Holzfarben (Nussschalen)", "use_de": "Sichtbare Kehlen, Holzarbeiten", "sandability": "mittel"},
            "406_colloidal_silica": {"type": "Kolloidale Kieselsäure", "use_de": "Viskositätskontrolle, Überkopf-Arbeiten, strukturell", "sandability": "schwer"},
            "407_low_density": {"type": "Microballoons", "use_de": "Spachtelarbeiten, leicht schleifbar", "sandability": "leicht"},
            "410_microlight": {"type": "Hochformuliert", "use_de": "Optimal für Spachtelarbeiten, leichteste Variante", "sandability": "sehr leicht"}
        },
        "amine_blush": {
            "cause_de": "Amine im Härter reagieren mit CO2 und Feuchtigkeit — bildet wachsartige Oberfläche",
            "conditions": "RH > 70%, Oberfläche < 15°C, Temperatur < 15°C",
            "optimal_range_c": "15-25",
            "prevention_de": "Warm aushärten lassen, Luftfeuchtigkeit < 70%, 5°C über Taupunkt bleiben",
            "remediation_de": "Mit Lösungsmittel abwaschen (frisch) oder schleifen (ausgehärtet)"
        }
    },
    "resin_comparison": {
        "epoxy": {"bond_strength": "höchste", "water_resistance": "wasserdicht (molekular)", "secondary_bond": "hervorragend", "flexibility": "besser", "cost": "3-4× Polyester", "cure": "mittel-langsam"},
        "polyester": {"bond_strength": "niedrig", "water_resistance": "absorbiert Wasser", "secondary_bond": "schlecht", "flexibility": "steif", "cost": "Basis", "cure": "schnell"},
        "vinylester": {"bond_strength": "mittel", "water_resistance": "besser als Polyester", "secondary_bond": "mittel", "flexibility": "steif", "cost": "1.5-2× Polyester", "cure": "mittel"}
    }
}


PAINT_SYSTEMS: Dict[str, Any] = {
    "antifouling": {
        "international": {
            "micron_extra": {"type": "SPC (Self-Polishing)", "seasons": "1-2", "biocide": "Kupferoxid + Zineb", "for": "Segelboote, Bewegung nötig"},
            "trilux_33": {"type": "SPC", "note_de": "Speziell für ALUMINIUM, Antriebe, Außenborder — sicher auf Leichtmetall!"},
            "cruiser": {"type": "SPC", "for": "Langsamere Segelboote"},
            "ultra_eu": {"type": "Hart-Matrix", "for": "Schnelle Motorboote, Regatta"}
        },
        "hempel": {
            "mille_nct": {
                "type": "SPC mit Nanokapseln",
                "coverage_m2_l": 13,
                "touch_dry_20c_hours": 2,
                "recoat_min_20c_hours": 4,
                "immersion_min_hours": 24,
                "immersion_max_months": 9,
                "suitable": ["GFK", "Holz", "Sperrholz", "Stahl"],
                "not_suitable": "Aluminium und Leichtmetalle",
                "colors": ["Grau", "Schwarz", "Weiß", "Dunkelblau", "True Blue", "Rot"],
                "thinner": "Hempel Thinner 808 (Nr. 3)"
            },
            "silic_one": {
                "type": "Biozid-frei (Silikon + Hydrogel)",
                "biocide": "KEINE — keine Kupfer, keine Biozide",
                "mechanism_de": "Verhindert Anhaftung, erleichtert Abtrennung beim Segeln",
                "dft_microns": 80,
                "not_suitable": "Holzboote",
                "note_de": "Zukunft des Antifoulings — umweltfreundlich, aber nur für aktiv genutzte Boote"
            }
        },
        "jotun": {
            "seaquantum_ultra_s": {"type": "Silyl-Acrylat SPC", "performance": "Bis 15% Antriebseffizienz-Gewinn", "service_months": "bis 90"},
            "seaquantum_classic_s": {"type": "Silyl-Acrylat SPC", "for": "Mittel-aktive Fahrzeuge"}
        },
        "application_specs": {
            "dft_per_coat_microns": {"min": 50, "standard": "50-75", "max": 75},
            "total_dft_2_coats_microns": "120-150",
            "coats_minimum": 2,
            "extra_coat_de": "Zusätzliche Schicht am Wasserpass und an Vorderkanten empfohlen",
            "coverage_m2_per_l": "8-13 (je nach Produkt)"
        }
    },

    "topside": {
        "international_perfection": {
            "type": "2K Polyurethan",
            "mix_ratio": "2:1 (Basis:Härter)",
            "thinner": "Interlux Thinner No. 9 (5-10%)",
            "durability_years": 5,
            "chemical_resistance": ["Diesel", "Benzin", "Öl", "milde Säuren", "Laugen"],
            "application_temp_c": "10-35",
            "note_de": "Ultimative Hochglanz-Oberfläche, professionelles Ergebnis"
        },
        "alkyd_vs_polyurethane": {
            "1k_alkyd": {
                "pros_de": ["Einfache Pinsel-Anwendung", "Cremige Verarbeitung", "Leicht zu schleifen", "Einfache Ausbesserung"],
                "cons_de": ["Geringere Haltbarkeit (3-4 Jahre)", "Mäßige Glanzbeständigkeit", "Fleckenanfällig"],
                "repairability": "hervorragend"
            },
            "2k_polyurethane": {
                "pros_de": ["Überlegene Glanzbeständigkeit", "Farbstabilität", "Härte", "Chemikalien-/Abriebfestigkeit", "Langlebigkeit (5+ Jahre)"],
                "cons_de": ["Komplexe Verarbeitung", "Giftige Dämpfe", "Wetterabhängig", "Kurze Topfzeit"],
                "repairability": "schwierig — neue Schicht haftet schlecht auf alter"
            }
        },
        "awlgrip_vs_alexseal": {
            "awlgrip": {"hardness": "härtestes PU", "repairability": "schlecht", "toxicity": "hoch", "roller": "schwierig (tippt nötig)"},
            "alexseal": {"hardness": "Acryl-Urethan-Hybrid", "repairability": "hervorragend", "toxicity": "benutzerfreundlich", "roller": "möglich ohne Tippen (Additiv)"}
        }
    },

    "varnish": {
        "comparison": {
            "international_compass": {
                "type": "PU-Hochglanz",
                "surface_hardness": "hoch",
                "uv_resistance": "sehr gut",
                "recoat_hours": 3,
                "oily_wood": True,
                "coats_bare_wood": "1× verdünnt + 3-5× unverdünnt, P320-400 Zwischenschliff"
            },
            "epifanes_clear": {
                "type": "1K Tungöl/Phenolharz/Alkydharz",
                "surface_hardness": "mittel-hoch",
                "uv_resistance": "sehr gut (Aluminium-UV-Partikel)",
                "elasticity": "hoch",
                "note_de": "Klassiker! Bestbewertet nach 1-Jahres-Freiland-Test."
            },
            "le_tonkinois": {
                "type": "Leinöl-basiert",
                "uv_protection": "KEINE UV-Filter",
                "coverage_m2_l": 20,
                "advantage_de": "Einfachste Anwendung, keine Verdünnung, reißt nicht an Fugen",
                "disadvantage_de": "Weichere Oberfläche, kein UV-Schutz, häufiger nachstreichen"
            }
        },
        "system_over_epoxy": {
            "description_de": "Epoxid als Basis + Lack als UV-Schutz = optimales System",
            "procedure": "2-3 Epoxid-Schichten → Schleifen P220 → Lack (6-10 Schichten)",
            "critical_de": "Epoxid MUSS UV-geschützt werden — vergilbt und reißt innerhalb 1-2 Monaten ohne Schutz",
            "epoxy_advantage_de": "Feuchtigkeitsbarriere reduziert Quellen/Schwinden des Holzes"
        },
        "coats_by_climate": {
            "nordeuropa": "6-8 Schichten",
            "mittelmeer": "8-10 Schichten",
            "tropen": "10-12 Schichten",
            "note_de": "Mehr UV-Belastung = mehr Schichten nötig"
        }
    },

    "primers": {
        "international_interprotect": {
            "type": "2K Epoxid-Polyamid",
            "mix_ratio": "3:1 (Volumen)",
            "coverage_m2_l": 9,
            "dft_microns": 360,
            "volume_solids_percent": 45,
            "voc_g_l": 464,
            "application_temp_c": "10-35",
            "thinner": "International Epoxy Thinner No. 7 (YTA061)",
            "recoatable_months": 6,
            "substrates": ["Polyester", "Vinylester", "Epoxid", "Stahl", "Aluminium", "Ferrozement", "Holz"],
            "note_de": "Universalprimer über und unter Wasser"
        },
        "hempel_light_primer": {
            "type": "2K Epoxid",
            "coverage_m2_l": 8.2,
            "anti_corrosion": "Zinkphosphat",
            "substrates": ["GFK", "Holz", "Stahl", "Aluminium"],
            "dust_dry_10c_hours": 6,
            "sand_ready_20c_hours": 24,
            "thinner": "Hempel Thinner 845"
        },
        "osmosis_barrier": {
            "international_gelshield_200": {
                "type": "Schnelltrocknender Epoxid-Primer",
                "coats_for_protection": 5,
                "total_dft_microns": 250,
                "min_temp_c": 5,
                "coats_per_day": "Mehrere möglich",
                "colors": ["Grün", "Grau (abwechselnd für Schichtkontrolle)"],
                "note_de": "Grün/Grau abwechselnd auftragen — so sieht man, ob jede Schicht deckend aufgetragen wurde"
            }
        },
        "sanding_grit_sequence": {
            "strip_old_paint": "80er Korn (Exzenterschleifer)",
            "feather_edges": "120er Korn",
            "hull_prep_final": "220er Korn",
            "between_primer_coats": "P320-400",
            "before_topcoat": "P400-600",
            "wet_sand_final": "P800-1500 → Polieren"
        }
    }
}


POLYURETHANE_CHEMISTRY: Dict[str, Any] = {
    "1k_pu_curing": {
        "mechanism": "Feuchtigkeitsaushärtung durch Wasser",
        "reaction_equation_de": "Polyol-NCO + H2O → Polyol-NH-CO-O-H → CO2 + Polyurea (Netzwerk)",
        "water_source": ["Materialfeuchte (Holz, GFK)", "Luftfeuchtigkeit", "Feuchtigkeit im Untergrund"],
        "optimal_conditions": {
            "temperature_c": "15-25",
            "relative_humidity_percent": "40-80",
            "note_de": "Zu trocken = langsame Aushärtung, zu feucht = oberflächlich ausgehärtet, innen noch flüssig"
        },
        "cure_stages": {
            "stage_1_surface_skin": {"minutes": "15-30", "appearance": "Oberfläche berührungsresistent, innen noch flüssig"},
            "stage_2_tack_free": {"hours": "1-2", "description": "Nicht mehr klebrig, aber inneres noch aushärtend"},
            "stage_3_demontierbar": {"days": "1-2", "description": "Mit Werkzeug entfernbar, mit Kraft abziehbar"},
            "stage_4_full_strength": {"days": "3-7", "description": "Optimale Festigkeit, Flexibilität, chemische Beständigkeit erreicht"}
        },
        "co2_production": {
            "note_de": "CO2-Gas wird freigesetzt — kann kleine Gasblasen in der Masse erzeugen",
            "prevention": "Langsames Auftragen, Walzen zum Entlüften, leichte Verdünnung mit Lösungsmittel"
        }
    },

    "2k_pu_curing": {
        "mechanism": "Chemische Härtung (Isocyanat + Polyol)",
        "reaction_equation_de": "Polyol-OH + Isocyanat-NCO → Polyol-O-CO-NH-Polyol (Urethan-Bindung)",
        "stoichiometry": "Isocyanat-Gruppen müssen äquimolar mit Polyol-Gruppen vorhanden sein",
        "pot_life_definition": "Zeit, in der sich die Viskosität verdoppelt (arbeitbar bleibt)",
        "factors_affecting_pot_life": {
            "temperature": "Erhöhung um 10°C → Halbierung der Topfzeit",
            "catalyst_type": "Tertiäre Amine katalysieren die Reaktion",
            "isocyanate_equivalent": "Höhere NCO-Äquivalente = schnellere Härtung",
            "humidity": "Höhere Luftfeuchtigkeit = leicht verzögert"
        },
        "cure_stages": {
            "stage_1_pot_life": {"hours": "0.5-2 (je nach System)", "action": "Verarbeitbar"},
            "stage_2_tack_free": {"hours": "2-4", "description": "Oberfläche nicht mehr klebrig"},
            "stage_3_light_traffic": {"hours": "8-24", "description": "Leichte Belastung erlaubt"},
            "stage_4_full_cure": {"days": "3-7", "description": "Volle Härte und Festigkeit"}
        }
    },

    "substrate_interaction": {
        "gelcoat": {
            "chemistry": "Ungesättigtes Polyesterharz mit Styrolverstärkung",
            "compatibility_pu": "Sehr gut — PU haftet kraftschlüssig",
            "surface_prep_de": "Schleifen P80-120, Feuchtigkeit < 5%",
            "lifetime_of_gelcoat": "15-20 Jahre, danach Oxidation/Cracking",
            "aged_gelcoat_issue": "Wachsfilm und UV-degradation reduzieren Haftung",
            "solution_de": "Gründlich schrubben und schleifen, ggf. Haftvermittler verwenden"
        },
        "gfrp_carbon": {
            "chemistry": "Epoxid- oder Polyesterharz-Matrix mit Glas- oder Kohlefasern",
            "compatibility_pu": "Hervorragend mit gut vorbereiteter Oberfläche",
            "issue_with_aged_cfrp": "Harz kann vergilbt sein, Oberfläche mit UV-Partikeln bedeckt",
            "surface_prep": "Schleifen P120-220, Blasen mit Druckluft, Trockenheit > 24h"
        },
        "wood": {
            "moisture_content_critical": "Holz mit > 20% Feuchtegehalt = Quellung nach Abdichtung",
            "ideal_moisture": "12-18%",
            "surface_prep": "Schleifen P120-220, bürsten mit Stahlbürste",
            "protection": "PU erhöht Quellung/Schwindung von Holz — Oberflächenfinish erforderlich",
            "teak_specific": "Höher Ölgehalt — gründlich entfetten vor Abdichtung"
        },
        "aluminum": {
            "oxidation_layer": "Aluminium-Oxid-Schicht (Al2O3) ist porös und mehlig",
            "issue": "PU haftet schlecht auf unreinem Aluminium",
            "surface_prep": "Schleifen P80-120, Chromat-Primer (z.B. Zinc Chromate) empfohlen",
            "note_de": "Neue Aluminiumoberfläche oxidiert schnell — rasch nach Schleifen abdichten"
        },
        "stainless_steel": {
            "passivation_layer": "Chrom-Oxid-Schicht ist glatt und nicht porös",
            "issue": "PU haftet schwach, besonders unter Wasser",
            "surface_prep": "Rauendes Schleifen erforderlich (P80-120), oder Haftvermittler",
            "best_practice": "Sikaflex 291i mit Primer, oder 3M 5200 mit Oberflächenrauung"
        }
    }
}


CURE_TIME_FACTORS: Dict[str, Any] = {
    "temperature_influence": {
        "description_de": "Aushärtungsgeschwindigkeit folgt exponentieller Temperaturabhängigkeit",
        "10_degree_rule": "Jede 10°C Erhöhung → 2-3× schnellere Reaktion",
        "critical_temp_ranges": {
            "below_5c": {"issue": "Praktisch keine Aushärtung", "recommendation": "Beheizte Werkstatt oder Wärmestrahler"},
            "5_to_15c": {"rate": "Langsam", "days": "5-7 bei 1K-PU"},
            "15_to_25c": {"rate": "Optimal", "days": "3-5 bei 1K-PU"},
            "25_to_35c": {"rate": "Schnell", "days": "2-3 bei 1K-PU"},
            "above_35c": {"issue": "Zu schnell, Blasenbildung, ungleichmäßig", "recommendation": "Beschattung, Ventilation"}
        }
    },

    "humidity_influence": {
        "low_humidity_lt_30percent": {
            "effect_on_1k_pu": "Sehr langsame Aushärtung — zu wenig Wasser für Reaktion",
            "effect_on_2k_pu": "Unbeeinflusst — Aushärtung durch chemische Reaktion",
            "recommendation_de": "Feuchttücher auf frisch aufgetragene Masse legen, oder mit Sprayer befeuchten"
        },
        "optimal_humidity_40_80percent": {
            "effect": "Ideale Bedingungen für 1K-PU Aushärtung",
            "note": "Nicht zu feucht (> 80%) — führt zu oberflächlicher Aushärtung, innen flüssig"
        },
        "high_humidity_gt_80percent": {
            "risk_1k_pu": "Oberflächlichkeitsblüte (auch 'amine blush' genannt)",
            "risk_2k_pu": "Wassereinschlüsse, Bläschen in der Oberfläche",
            "prevention": "Luftzirkulation, Heizung, Entfeuchtung vor Auftrag"
        }
    },

    "thickness_effect": {
        "thin_layers_le_3mm": {"cure_time": "Schnell (Haut in Minuten)", "issue": "Schnelle Oberflächenaushärtung, innere Aushärtung folgt später"},
        "medium_3_to_10mm": {"cure_time": "Moderat (Tage)", "note": "Standard-Anwendung für Fugen und Klebungen"},
        "thick_layers_gt_10mm": {"cure_time": "Sehr langsam (Wochen)", "issue": "Exotherme Reaktion, Wärmeentwicklung kann zu Rissen führen", "recommendation": "In mehreren Schichten auftragen"}
    },

    "product_specific": {
        "sikaflex_291i": {
            "surface_skin_temp_20c": "15-30 min",
            "tack_free_temp_20c": "1-2 hours",
            "initial_set_temp_20c": "2-3 days",
            "full_cure_temp_20c": "3-7 days",
            "note_de": "Längere Aushärtung bei Dickschichten oder niedriger Temperatur"
        },
        "3m_5200": {
            "tack_free_temp_20c": "1-2 hours",
            "demountable_temp_20c": "1-2 days",
            "full_strength_temp_20c": "7-10 days",
            "high_strength_application_de": "Mindestens 24h warten vor Belastung"
        },
        "west_system_105_205": {
            "exotherm_temp_rise_c": "Up to 15°C in thick layers",
            "full_cure_8h_temp_20c": "Yes (60-70°C exotherm)",
            "7day_strength_percent": "90-95%",
            "30day_strength_percent": "100%"
        }
    }
}


COMMON_MISTAKES_AND_REMEDIATION: Dict[str, Any] = {
    "moisture_contamination": {
        "symptom": "Weiße Flöckchen/Pulver auf Oberfläche, mangelnde Haftung",
        "cause": "Zu hohe Luftfeuchtigkeit während/nach Auftrag",
        "prevention": "Luftfeuchtigkeit < 80%, Wärmequelle verwenden, Oberfläche abdecken",
        "remedy_if_fresh": "Mit fusselfreiem Tuch und Lösungsmittel abwischen, neu aufbringen",
        "remedy_if_cured": "Mit feiner Bürste oder Schleifer entfernen (P220-320), neu grundieren"
    },

    "gas_inclusions": {
        "symptom": "Blasen oder kleine Löcher in der Oberfläche",
        "cause_1k_pu": "CO2-Freisetzung, zu schnelles Auftragen, nicht gewalzt",
        "cause_2k_pu": "Zu schnelle Aushärtung, unzureichendes Entlüften nach Mischen",
        "prevention": "Langsames gleichmäßiges Auftragen, mit Schaumrolle/Bürste walzen, nicht zu dick in einer Schicht",
        "remedy_if_minor": "Abschleifen P120-180, lokal neu grundieren und auftragen",
        "remedy_if_major": "Gesamte Schicht abschleifen, neu aufbringen"
    },

    "adhesion_failure": {
        "symptom": "Abdichtung 'springt ab' oder lässt sich leicht abziehen",
        "cause_1": "Verschmutzte Oberfläche (Staub, Öl, Wachs, Silikon)",
        "cause_2": "Unzureichende Oberflächenrauhung",
        "cause_3": "Falscher Dichtstoff für Substrat (z.B. PU auf Silikon-Resten)",
        "cause_4": "Aged substrate (verwitterte Oberfläche, Algenbewuchs)",
        "prevention": "Gründliche Oberflächenvorbereitung: Reinigung → Schleifen → Trocknung",
        "remedy": "Dichtstoff entfernen, Substrat bis auf Rohmaterial schleifen, reinigen, neu abdichten"
    },

    "yellowing_and_chalking": {
        "symptom": "Gelbverfärbung und kreidiger Belag auf der Oberfläche",
        "cause_1k_polyurethane": "UV-Degradation ohne UV-Filter (z.B. alte Sikaflex 290i)",
        "cause_polyester": "Alterung und Oxidation des Harzes",
        "prevention": "UV-resistente Formeln verwenden (Sikaflex 591, 3M 4000UV) oder mit Lack überstreichen",
        "remedy": "Oberflächliches Abschleifen und Überstreichen mit UV-stabilem Lack"
    },

    "incomplete_cure": {
        "symptom": "Dichtstoff bleibt weich und klebrig nach erwarteter Aushärtungszeit",
        "cause_1k_pu": "Zu geringe Luftfeuchtigkeit (< 30%)",
        "cause_2k_pu": "Falsches Mischverhältnis oder kontaminierter Härter",
        "cause_thick_application": "Zu dicke Schicht, Inneres nicht aushärtend",
        "remedy_if_reachable": "Abschleifen entfernen, in dünneren Schichten neu auftragen",
        "remedy_temperature": "Beheizte Werkstatt (20-25°C) verwenden oder warten"
    },

    "mixing_errors_2k_systems": {
        "symptom": "Ungleichmäßige Konsistenz, Streifenmuster, schnelles Verhärten",
        "cause": "Zu schnelles Mischen (Luft eingerührt), falsches Verhältnis",
        "prevention": "Langsam und gründlich mischen, digitale Waage für exaktes Mischen verwenden",
        "remedy": "Entsorgen und neu anmischen — einmal vermischte 2K-Systeme können nicht 'gerettet' werden"
    },

    "substrate_swelling": {
        "symptom": "Holzoberfläche quillt auf, Dichtstoff sitzt locker",
        "cause": "Holz mit > 20% Feuchtegehalt, oder Feuchte dringt nach Abdichtung ein",
        "prevention": "Holzfeuchte messen (12-18% optimal), Oberseite dichtstoff-geschützt halten",
        "remedy": "Trocknen (mindestens 3-4 Wochen an Luft), Dichtstoff entfernen, austrocknen, neu abdichten"
    }
}


SURFACE_PREPARATION_DETAILED: Dict[str, Any] = {
    "cleaning_sequence": {
        "step_1_visual_inspection": "Oberflächenart bestimmen, Verschmutzung bewerten",
        "step_2_gross_contamination": "Algen, Muschelkalk, Schlamm mit Hochdruckstrahler (< 80 bar für GFK!) oder Bürste entfernen",
        "step_3_oil_contamination": "Fett/Öl mit seifenhaltiger Lösung oder organischem Reiniger (z.B. Spiritus) abwischen",
        "step_4_silicone_removal": "Silikon mit Silikonentferner-Spray oder Verdünnung auflösen — ESSENTIELL vor PU!",
        "step_5_drying": "Mindestens 24 Stunden an Luft trocknen, Holz ggf. 48-72 Stunden"
    },

    "abrasion_grit_selection": {
        "p_80_100": {"purpose": "Entfernung alter Beschichtung, starke Verschmutzung, Rostnässe", "substrate": "Stahl, alte Lackschichten", "follow_up": "Nachschleifen mit P120-220"},
        "p_120_150": {"purpose": "Oberflächenaufrauhung GFK/Gelcoat, Kanten federn", "substrate": "GFK, Holz, Aluminium", "follow_up": "P220-320"},
        "p_220": {"purpose": "Final prep vor Abdichtung/Grundierung", "substrate": "Alle Substrate", "follow_up": "Keine weitere Behandlung"},
        "p_320_400": {"purpose": "Zwischen Primer-Schichten, Feinschliff", "substrate": "Alle", "note": "Nur mit feuchter Körnung (Nassschliff)"},
        "p_600_1000": {"purpose": "Hochglanz-Finishes, polierbar", "substrate": "Lackoberflächen", "wet_sand_only": True}
    },

    "substrate_specific_prep": {
        "polyester_gel_coat": {
            "steps": [
                "Visuell auf Risse, Blasen, Kratzer prüfen",
                "Mit Hochdruckstrahler (mild) oder Bürste reinigen",
                "P80-120 schleifen, um Wachsfilm zu entfernen",
                "Mit P220 nachschleifen",
                "Druckluft blasen, fusselfreies Tuch abwischen",
                "Mindestens 2 Stunden trocknen vor Auftrag"
            ],
            "typical_problem": "Wachsfilm in neuem Gelcoat macht Haftung schwierig",
            "solution": "Gründlich schleifen — mindestens 2 Minuten pro m² mit Schleifer"
        },
        "wood_bare_or_coated": {
            "bare_wood": [
                "Feuchte messen (zielwert 12-18%)",
                "Splitter aufrauhern",
                "P120-180 schleifen (mit Körnung des Holzes)",
                "Taumittel ausbürsten (Holzfasern aufrauhern)",
                "Mit feuchtem Tuch nachwischen (leicht anfeuchten, nicht nass)",
                "24-48 Stunden trocknen",
                "Leicht mit P220 schleifen (feinen Flaum entfernen)",
                "Sofort grundieren/abdichten (Holz verzieht sich)"
            ],
            "coated_wood": [
                "Alte Schicht auf Haftung prüfen",
                "P80-120 schleifen zur Entfernung loser Schichten",
                "P220 Feinschliff",
                "Reinigung und Trocknung wie bare wood"
            ],
            "special_woods": {
                "teak": "Höchste Ölkonzentration — mit Lösungsmittel/Verdünner abschrubben, trocknen",
                "mahagoni": "Tannine können Verfärbung verursachen — gut trocknen",
                "fichte": "Weiche Holzart — weniger aggresiv schleifen"
            }
        },
        "aluminum_bare": {
            "steps": [
                "NICHT mit Hochdruckstrahler (< 10 bar nur!)  — Gefahr der Oberflächenrauung",
                "Mit Bürste und Wasser reinigen",
                "Mit P80-120 (Trockenschliff) schleifen — Oxidhaut entfernen",
                "Mit P220 nachschleifen und glätten",
                "Mit Lappentuch und Spiritus abwischen",
                "Chromat-Primer (z.B. Zink-Chromat) auftragen ODER Sikaflex 591 mit Haftvermittler",
                "Nicht zu lange vor Abdichtung warten — Alu oxidiert schnell"
            ],
            "critical": "Nackte Aluminium-Oberfläche ist hochreaktiv und oxidiert in Stunden"
        },
        "stainless_steel": {
            "steps": [
                "Mit Druckluft oder Bürste reinigen (nicht mit Stahlbürste — Eisenverunreinigung)",
                "Mit P80-120 schleifen (muss rau sein für PU-Haftung)",
                "Mit P220 nachschleifen",
                "Mit feuchtem Tuch abwischen (Chromat-Schicht ist inert)",
                "Mit Haftvermittler (z.B. 3M Primer) oder hochwertigem Dichtstoff (3M 5200) arbeiten"
            ],
            "passive_layer": "Chromoxid-Schicht ist chemisch sehr stabil — schwache Haftung natürlich"
        }
    }
}


COMPATIBILITY_MATRIX: Dict[str, Any] = {
    "sealant_to_substrate": {
        "sikaflex_291_matrix": {
            "gelcoat_gfrp": "Ausgezeichnet — Standard",
            "wood": "Hervorragend — gründlich schleifen",
            "aluminum": "Gut — rauhen erforderlich, Primer empfohlen",
            "stainless": "Mittel — Haftvermittler erforderlich",
            "pvc_kunststoff": "Schlecht — vermeiden",
            "acryl_kunststoff": "Schlecht — greift an",
            "polycarbonat_lexan": "NICHT geeignet",
            "kautschuk": "Hervorragend",
            "edelstein": "Ausgezeichnet"
        },
        "3m_5200_matrix": {
            "gelcoat_gfrp": "Ausgezeichnet",
            "wood": "Ausgezeichnet",
            "aluminum": "Ausgezeichnet",
            "stainless": "Ausgezeichnet",
            "kunststoff": "Variabel — Testung erforderlich",
            "note_de": "Greift NICHT-reaktive Kunststoffe an, aber Haftvermittler bei PVC/Acryl empfohlen"
        },
        "sikaflex_591_smp_matrix": {
            "all_substrates": "Sehr gute Universalkompatibilität",
            "special_advantage": "Haftet auf feuchteren Oberflächen als Polyurethan",
            "kunststoff": "Sicherer — keine chemische Reaktion"
        }
    },

    "paint_over_sealant": {
        "polyurethane_sealants": {
            "paintable": True,
            "dry_time_before_paint_hours": 24,
            "primer_required": "Epoxy-Primer empfohlen für Struktur",
            "note_de": "Nur wenn Dichtstoff 'ausdrücklich übermalbar' ist"
        },
        "silicone_sealants": {
            "paintable": False,
            "note_de": "Silikone sind NICHT übermalbar — Farbe haftet nicht, reißt ab",
            "cross_contamination": "Auch Silikonreste verhindern Haftung aller Farben und anderen Dichtmassen!"
        },
        "ms_polymer_sealants": {
            "paintable": True,
            "dry_time_hours": 24,
            "advantage_de": "MS-Polymer kann überstrichen werden (anders als ältere PU)"
        }
    }
}


TECHNICAL_SPECIFICATIONS_INTERNATIONAL: Dict[str, Any] = {
    "international_perfection_2k_pu": {
        "product_code": "YSB001",
        "composition": "2K Polyurethan Topcoat",
        "mix_ratio_volume": "2 Basis : 1 Härter",
        "coverage_wet_m2_l_at_100_dft": 10,
        "dft_dry_microns": 75,
        "volume_solids_percent": 55,
        "voc_g_l": 340,
        "application_equipment": ["Airless spray (0.5mm tip)", "Roller (medium pile)", "Brush (synthetic bristles)"],
        "application_conditions": {
            "temperature_c": "10-35 (20-25 optimal)",
            "relative_humidity_percent": "40-80",
            "substrate_temp_c": "Minimum 3°C above dew point"
        },
        "drying_times_at_20c": {
            "tack_free_min": 8,
            "hard_dry_hours": 16,
            "recoatable_min_hours": 24,
            "full_cure_days": 7
        },
        "thinner": {"type": "Interlux Thinner No. 9", "percent": "5-10%"},
        "shelf_life_base": "3 years unopened",
        "shelf_life_hardener": "18 months unopened",
        "pot_life_ml_at_20c_hours": "4-6 (depending on batch)",
        "typical_coverage_per_liter": "8-9 m² (at 100 microns DFT)",
        "colors_available": ["Traditional White", "Ivory", "Light Gray", "Navy Blue", "International Orange", "Gloss Black"],
        "surface_hardness_shore_d": 85,
        "flexibility_mm_mandrel": 3,
        "water_resistance": "Excellent",
        "fuel_resistance": "Good (diesel, gasoline, kerosene)",
        "acid_resistance": "Good (dilute acids)",
        "abrasion_resistance": "Excellent (Taber wheels, 1000 cycles < 20mg loss)",
        "gloss_level_60_degree": 85,
        "gloss_retention_2yr_florida_exposure": ">70%",
        "impact_resistance_forward_inch_lbs": 40,
        "impact_resistance_reverse_inch_lbs": 30
    },

    "hempel_mille_nct_antifouling": {
        "product_code": "20001",
        "type": "Self-Polishing Antifouling (SPC) with nano-capsules",
        "coverage_m2_l": 13,
        "dft_per_coat_microns": 75,
        "total_dft_recommended_microns": 150,
        "application_temp_c": "5-35",
        "pot_life_unlimited": True,
        "touch_dry_20c_hours": 2,
        "recoat_min_hours": 4,
        "immersion_time_min_hours": 24,
        "immersion_time_max_months": 9,
        "drying_time_full_hours": 72,
        "suitable_substrates": ["GRP/FRP", "Wood", "Plywood", "Steel"],
        "not_suitable": ["Aluminium", "Copper"],
        "biocide_content_percent": "48",
        "biocide_type": "Copper-based with Pyrithione Zinc",
        "release_mechanism": "Nano-capsule controlled release",
        "colors_available": ["Grey", "Black", "White", "Dark Blue", "True Blue", "Red"],
        "thinner": "Hempel Thinner 808 (No. 3)",
        "thinner_percent_max": 10,
        "shelf_life_years": 2,
        "density_kg_l": 1.65,
        "viscosity_kinematic_mm2_s": 90,
        "iso_gloss_60_degrees": "Matt (20°)"
    }
}


ENVIRONMENTAL_AND_HEALTH: Dict[str, Any] = {
    "voc_volatile_organic_compounds": {
        "definition_de": "Organische Stoffe mit Dampfdruck > 10 Pa bei 20°C",
        "typical_2k_polyurethane_g_l": "340-400",
        "typical_1k_polyurethane_g_l": "100-200",
        "typical_epoxy_g_l": "150-250",
        "typical_alkyd_g_l": "400-500",
        "health_effects": "Kopfschmerzen, Schwindel, Atemwegsreizung bei hoher Konzentration",
        "worker_safety": {
            "ventilation_required": True,
            "respiratory_protection": "Halbmaske mit organischem Lösungsmittelfilter",
            "skin_protection": "Chemikalienbeständige Handschuhe (Nitril unzureichend)",
            "eye_protection": "Schutzbrille"
        }
    },

    "isocyanate_hazards": {
        "found_in": "2K Polyurethane, 2K Epoxy (weniger)",
        "health_risk": "Respiratorische Sensibilisierung (Asthma), chronische Atemwegserkrankungen",
        "exposure_limits_ppm": {
            "OEL_germany_MAK": 0.005,
            "short_term_exposure": 0.02
        },
        "precautions": [
            "Immer Atemschutz (Halbmaske mit P2-Filter)",
            "Gutes Lüftungssystem",
            "Hautschutz — keine Hautkontakt",
            "Training erforderlich für 2K-Arbeiten"
        ]
    },

    "environmental_regulations": {
        "eu_directive_2004_42_ec": {
            "name": "VOC-Richtlinie für Beschichtungen",
            "phase_in": "2010",
            "limits_2k_polyurethane_g_l": 400,
            "limits_1k_polyurethane_g_l": 340
        },
        "imo_ftp_requirements": {
            "applies_to": "Internationale Schiffe > 500 BRZ",
            "fire_safety_coatings": "Müssen IMO FTP Part 5 entsprechen",
            "testing_standard": "ISO 5660-1 (Cone Calorimeter)"
        }
    }
}
