"""
AYDI Wissens-Index — Vollständiges Inhaltsverzeichnis aller Wissensbereiche.

Jeder Eintrag: Bereich → Status (implemented/partial/missing) → Modul-Pfad

Dieses Verzeichnis dient als Referenz für die Vollständigkeit des Wissenssystems.
"""

KNOWLEDGE_INDEX = {
    # =========================================================================
    # 1. MATERIALIEN (Werkstoffe)
    # =========================================================================
    "1_materialien": {
        "title": "Materialien und Werkstoffe",
        "status": "implemented",
        "module": "db/seed.py → SEED_MATERIALS (54 Materialien)",
        "subcategories": {
            "1.1_holz": {
                "title": "Hölzer",
                "status": "implemented",
                "entries": 8,
                "details": [
                    "Teak (Burma, Plantation)", "Iroko", "Accoya", "Marine Sperrholz BS 1088",
                    "Mahagoni", "Zedernholz", "Bamboo Marine",
                ],
                "has_properties": True,
                "has_failure_modes": True,
                "has_installation_methods": True,
                "has_water_ingress": True,
                "extended_knowledge": {
                    "module": "craftsmanship_wood.py → WOOD_SPECIES_MARINE",
                    "entries": 9,
                    "details": [
                        "Teak Burma (Dichte, Festigkeit, Ölgehalt, Siliziumgehalt, Gleichgewichtsfeuchte)",
                        "Iroko (Kambala)", "Eiche (Gerbsäure-Warnung!)", "Esche (Biegefestigkeit)",
                        "Lärche (historisch)", "Kork (Isolierung/Belag)", "Accoya (acetyliert)",
                        "Mahagoni (Khaya/Sapele)", "Marine Sperrholz BS 1088 (Kantenversiegelung)",
                    ],
                    "includes": [
                        "Holzfeuchte-Gleichgewichtstabellen pro Klima",
                        "Jahresring-Orientierung (quarter-sawn)",
                        "Harzgehalt und Extraktstoffe",
                        "Dampfbiegen-Parameter pro Holzart (STEAM_BENDING_PARAMS)",
                    ],
                },
                "missing": [
                    "Zedernholz-Detailwissen (Western Red Cedar vs Alaska Yellow Cedar)",
                    "Bambus Marine — Verarbeitungshinweise",
                ],
            },
            "1.2_composites": {
                "title": "Faserverstärkte Kunststoffe",
                "status": "implemented",
                "entries": 8,
                "details": [
                    "GFK Polyester Handlaminat", "GFK Vinylester", "GFK Vakuuminfusion",
                    "Carbon-Prepreg", "Carbon-Infusion", "Aramid/Kevlar",
                    "Glasfaser-Epoxid", "Basaltfaser",
                ],
                "missing": [
                    "Flachs-Epoxid (Bio-Composites)",
                    "Recycled-Carbon",
                    "Thermoplastische Composites",
                ],
            },
            "1.3_metalle": {
                "title": "Metalle und Legierungen",
                "status": "implemented",
                "entries": 6,
                "missing": [
                    "Kupfer-Nickel (CuNi 90/10 — Rohre, Seekühlung)",
                    "Monel 400 (Nieten, Propellerwellen)",
                    "Zink (Opferanoden — Zusammensetzung, Reinheit)",
                    "Magnesium-Anoden (Süßwasser)",
                    "Aluminium-Anoden (Brackwasser)",
                    "Blei (Kielballast — Legierung, Guss)",
                    "Inconel (Abgasanlagen)",
                ],
            },
            "1.4_kernmaterialien": {
                "title": "Sandwich-Kernmaterialien",
                "status": "implemented",
                "entries": 5,
                "missing": [
                    "Airex C70 (Linear-SAN)",
                    "Coosa Board (Composite-Platte als Holzersatz)",
                ],
            },
            "1.5_textilien": {
                "title": "Textilien und Polster",
                "status": "implemented",
                "entries": 6,
                "has_sewing_specs": True,
                "extended_knowledge": {
                    "module": "craftsmanship.py → SAIL_FABRICS, MARINE_FOAM_TYPES",
                    "entries": 7,
                    "details": [
                        "Segeltuch: Dacron, Laminat/Mylar, Hydra Net/DCF, Pentex",
                        "Schaumstoff: Geschlossenzellig PE, Offenzellig PU Marine, Drymesh",
                    ],
                },
                "missing": [
                    "Gore-Tex Marine (Foul-Weather-Materialien)",
                ],
            },
            "1.6_beschichtungen": {
                "title": "Beschichtungen, Lacke, Farben",
                "status": "implemented",
                "entries": 6,
                "missing": [
                    "Primer-Typen im Detail (Epoxid, Zinkphosphat, Wash-Primer)",
                    "Zwischenbeschichtungen (Tie-Coats)",
                    "Spezial: Propellerfarbe, Unterwasseranstrich-Varianten",
                ],
            },
            "1.7_dichtungen_und_dichtstoffe": {
                "title": "Dichtungen, Dichtstoffe, Profile",
                "status": "implemented",
                "module": "craftsmanship_seals.py → SEAL_MATERIALS, SEAL_PROFILES, MEDIA_COMPATIBILITY",
                "entries": "7 Materialien, 9 Profiltypen, 6×14 Verträglichkeitsmatrix",
                "details": [
                    "EPDM — Zusammensetzung, Shore-Härte, Alterung, Anwendungen",
                    "NBR/Nitril — Ölbeständigkeit, ACN-Gehalt",
                    "FKM/Viton — Hochtemperatur, Kraftstoffbeständigkeit",
                    "Silikon (VMQ) — Lebensmittelecht, Rückstellverhalten",
                    "Neopren (CR) — selbstverlöschend, Maschinenraum",
                    "Butylkautschuk — Dichtband, Gasdichtigkeit",
                    "PTFE — Universal-Chemikalienbeständigkeit, Kaltfluss",
                    "O-Ringe — Nutberechnung, Kompression, Extrusionsgrenzen",
                    "Lippendichtungen — Einbauregeln, Wellenoberfläche",
                    "Gleitringdichtungen — PSS, Volvo Saildrive, Tides Marine",
                    "Stopfbuchse — Packungsmaterial, Nachstellregeln",
                    "Luken-Profile — D/P/E/Omega/Torpedo-Profil",
                    "Fenster-Abdichtung — Sikaflex, EPDM-Rahmen, Bullaugen",
                    "Ruderkoker — Lip-Seal, PSS, Stopfbuchse",
                    "Rumpfdurchbrüche — Bettung, Flachdichtung, Backing Plate",
                ],
                "missing": [
                    "PU-Schaum-Dichtungen — Zellstruktur, Kompressibilität",
                    "Flachdichtungen im Detail (Klingersil, Gylon)",
                ],
            },
            "1.8_klebstoffe": {
                "title": "Klebstoffe und Harze",
                "status": "partial",
                "entries": 4,
                "missing": [
                    "Epoxidharze im Detail (West System 105/205, 105/206, 105/209)",
                    "Vinylesterharz (Spezifikationen, Styrolgehalt)",
                    "Polyesterharz (Ortho vs ISO-NPG — chemische Zusammensetzung)",
                    "Methacrylat-Klebstoff (Plexus, für Verbundwerkstoffe)",
                    "Cyanacrylat (Sekundenkleber — wann im Bootsbau?)",
                    "Kontaktkleber Marine (Polster, Isolierung)",
                    "Heißkleber (wann erlaubt, wann nicht)",
                ],
            },
            "1.9_glas_fenster": {"title": "Glas und Fenster", "status": "implemented", "entries": 4},
            "1.10_isolierung": {"title": "Isolierung", "status": "implemented", "entries": 4},
            "1.11_elektrik": {"title": "Elektrik-Materialien", "status": "implemented", "entries": 3},
        },
    },

    # =========================================================================
    # 2. VERARBEITUNGSTECHNIKEN (Craftsmanship)
    # =========================================================================
    "2_verarbeitung": {
        "title": "Verarbeitungstechniken",
        "status": "implemented",
        "subcategories": {
            "2.1_naehen_textil": {
                "title": "Nähen und Textilverarbeitung",
                "status": "implemented",
                "module": "craftsmanship.py",
                "entries": "7 Garne, 8 Stichmuster, 10 Kompatibilitäten, 5 Nadeltypen, 4 Segelstoffe, 3 RV, 3 Druckknöpfe, 4 Keder, 2 Klett, 3 Schaumstoff",
                "new_additions": [
                    "SAIL_FABRICS: Dacron, Laminat/Mylar, Hydra Net/DCF, Pentex",
                    "MARINE_ZIPPERS: YKK AquaGuard, Lenzip, YKK Vislon",
                    "MARINE_SNAP_FASTENERS: Loxx/Tenax, DOT, Edelstahl",
                    "KEDER_PIPING: Rundkeder 6/8mm, Liektau, Flachkeder",
                    "MARINE_VELCRO: UV-beständig, 3M Dual Lock",
                    "MARINE_FOAM_TYPES: Geschlossenzellig PE, PU Marine, Drymesh",
                ],
                "missing": [
                    "Segelmacher-Spezialwissen (Segelschnitt, Panel-Layout, Luff-Curve)",
                    "Persenning-Schnittmuster (Bimini, Sprayhood, Lazy-Bag)",
                ],
            },
            "2.2_holzarbeit": {
                "title": "Holzarbeit und Tischlerei",
                "status": "implemented",
                "module": "craftsmanship_wood.py",
                "entries": "13 Verbindungen, 11 Oberflächen, 4 Biegetechniken, 6 Anpasstechniken, 9 Holzarten, 5 Dampfbiegen, 2 CNC/Drehen",
                "new_additions": [
                    "WOOD_SPECIES_MARINE: 9 Holzarten mit Dichte, Festigkeit, Dauerhaftigkeitsklasse, Gleichgewichtsfeuchte",
                    "STEAM_BENDING_PARAMS: Dampfbiege-Parameter für Eiche, Esche, Lärche, Mahagoni, Teak",
                    "WOOD_CNC_MARINE: CNC-Fräsen und Drechseln für Marine-Teile",
                ],
                "missing": [
                    "Holzkern-Ersatz bei Sandwich-Reparatur",
                ],
            },
            "2.3_laminieren": {
                "title": "Laminieren und Composite-Verarbeitung",
                "status": "implemented",
                "module": "craftsmanship_lamination.py",
                "entries": "10 Techniken, 14 Fasertypen, 7 Harzsysteme, 8 Laminatpläne, 8 Reparaturen",
                "missing": [
                    "Formenbau (Plug → Negativ → Bauteil)",
                    "Trennmittel-Systeme (PVA, Wachs, semi-permanent)",
                    "3D-Druck im Bootsbau (Tooling, Prototypen)",
                    "Faservolumengehalt-Messung (Veraschung, Salpetersäure)",
                ],
            },
            "2.4_lackieren_beschichten": {
                "title": "Lackieren, Beschichten, Oberflächenfinish",
                "status": "implemented",
                "module": "craftsmanship_coating.py",
                "entries": "15 Lacksysteme, 7 Vorbereitung, 8 Auftragsmethoden, 16 Defekte, 4 Polituren, 2 Folien, 3 Metallbehandlungen",
                "new_additions": [
                    "POLISHING_SYSTEMS: Grobpolitur, Mittelpolitur, Hochglanz, Wachs/Keramik",
                    "FOIL_WRAPPING: Gegossene Vinylfolie, Bedruckte Beschriftung",
                    "METAL_SURFACE_TREATMENTS: Eloxierung, Feuerverzinkung, Pulverbeschichtung",
                ],
                "missing": [],
            },
            "2.5_verschraubungen_beschlaege": {
                "title": "Verschraubungen, Beschläge, Befestigungen",
                "status": "implemented",
                "module": "craftsmanship_fasteners.py",
                "entries": "16 Befestiger, 13 Decksmontagen, 8 Durchbrüche, 15 Rigg, 10 Dichtmittel, 6 Gewindearten, 5 Loctite, 3 Schweißverfahren",
                "new_additions": [
                    "THREAD_TYPES_MARINE: Metrisch grob/fein, UNC, UNF, BSP, Whitworth",
                    "THREAD_LOCKING: Loctite 222/243/271/638/577",
                    "WELDING_MARINE: WIG/TIG Edelstahl 316, Aluminium 5083, Siliziumbronze",
                ],
                "missing": [
                    "Bolzenberechnung (Scherfestigkeit, Auszugswerte pro Material)",
                ],
            },
            "2.6_individuelle_anpassung": {
                "title": "Individuelle Anpassungen und Einbauten",
                "status": "implemented",
                "module": "craftsmanship_custom.py",
                "entries": "8 Passtechniken, 12 Innenausbau, 5 Fairness, 10 Toleranzen, 8 Metallarbeit, 8 Systeme",
                "missing": [
                    "Schablonieren mit 3D-Scanner",
                    "Retrofit-Planung (Nachrüstung in bestehende Boote)",
                    "Gewichts- und Schwerpunktoptimierung bei Umbauten",
                ],
            },
            "2.7_dichtungen_einbau": {
                "title": "Dichtungseinbau und -bewertung",
                "status": "implemented",
                "module": "craftsmanship_seals.py",
                "entries": "7 Materialien, 9 Profiltypen, 6×14 Medienverträglichkeit, O-Ring-Nutberechnung, Kompressionsverhalten, Inspektionskriterien",
                "details": [
                    "SEAL_MATERIALS: EPDM, NBR, FKM/Viton, Silikon, Neopren, Butyl, PTFE",
                    "SEAL_PROFILES: O-Ring, Lippendichtung, Gleitringdichtung (PSS), Stopfbuchse, "
                    "Luken-Profile (D/P/E/Omega/Torpedo), Fenster-Abdichtung, Ruderkoker, Rumpfdurchbrüche",
                    "MEDIA_COMPATIBILITY: 6 Materialien × 14 Medien (A/B/C/X)",
                    "O_RING_SIZING: DIN 3771 Normgrößen, Nutberechnung, Extrusionsgrenzen",
                    "COMPRESSION_BEHAVIOR: ISO 815 Prüfung, Shore-Härte-Auswahl",
                    "SEALING_SURFACE_PREPARATION: Rauheit, Planheit, Reinigungsprotokolle",
                    "SEAL_INSPECTION_CRITERIA: Visuell, Funktional, Installationsqualität",
                    "assess_seal_installation(): Bewertungsfunktion (0-100 Score)",
                ],
            },
        },
    },

    # =========================================================================
    # 3. KONSTRUKTIONSWISSEN (Structural Knowledge)
    # =========================================================================
    "3_konstruktion": {
        "title": "Konstruktions- und Strukturwissen",
        "status": "implemented",
        "module": "construction_weakpoints.py",
        "subcategories": {
            "3.1_schwachstellen": {
                "title": "Schwachstellenanalyse (FMEA)",
                "status": "implemented",
                "entries": "24 Zonen, 11 Verbindungstypen, 20 Verschleißmuster",
            },
            "3.2_galvanische_korrosion": {
                "title": "Galvanische Korrosion",
                "status": "implemented",
                "entries": "26 Materialpaarungen",
            },
            "3.3_wassereinbruch": {
                "title": "Wassereinbruch-Vektoren",
                "status": "implemented",
                "entries": "In ZONE_WEAKPOINTS integriert",
            },
            "3.4_bauverfahren_risiken": {
                "title": "Bauverfahrens-Risiken",
                "status": "implemented",
                "entries": "10 Bauverfahren",
            },
            "3.5_rumpfformen": {
                "title": "Rumpfformen und Hydrodynamik",
                "status": "implemented",
                "module": "hull_forms_hydrodynamics.py",
                "entries": "9 Rumpftypen, 9 Kieltypen, 6 Rudertypen, 4 Propeller-Konfig, 8 Hydro-Kennwerte, 6 Stabilitätskonzepte, 7 Bauweisen",
                "details": [
                    "HULL_TYPES: Verdränger, Semi-Displacement, Gleiter, SWATH, Katamaran, Trimaran, Rundboden, Knickspant, Multi-Chine",
                    "KEEL_TYPES: Langkiel, Kurzkiel, Bulb, T-Kiel, Schwenk, Hub, Kimm, Schwert, Canting",
                    "RUDDER_TYPES: Spatenruder, Skeg, Langkiel-Ruder, Balanced, Doppelruder, Heckspiegel",
                    "HYDRODYNAMIC_COEFFICIENTS: Cp, Cb, Cwp, Cm, D/L-Ratio, SA/D-Ratio, S/L-Ratio, Froude",
                    "STABILITY_CONCEPTS: GZ-Kurve, GM, AVS, STIX, ISO 12217, Downflooding",
                    "RESISTANCE_COMPONENTS: Reibung, Wellenbildung, Form, Anhänge, Wind, Seegang",
                    "HULL_CONSTRUCTION_METHODS: GFK Hand/Vakuum/Sandwich, Aluminium, Stahl, Holz-Epoxid, Ferrozement",
                    "assess_hull_design(): Bewertungsfunktion",
                ],
            },
        },
    },

    # =========================================================================
    # 4. ERFAHRUNGSWISSEN (Community Knowledge)
    # =========================================================================
    "4_erfahrung": {
        "title": "Erfahrungswissen und Community-Berichte",
        "status": "implemented",
        "module": "db/seed.py → community reports (225+)",
        "subcategories": {
            "4.1_hersteller": {"title": "Hersteller-spezifische Berichte", "status": "implemented"},
            "4.2_modell": {"title": "Modell-spezifische Berichte", "status": "implemented"},
            "4.3_material_degradation": {"title": "Material-Alterungsberichte", "status": "implemented"},
            "4.4_reparatur": {
                "title": "Reparatur-Erfahrungen",
                "status": "partial",
                "missing": [
                    "Kosten-Erfahrungen pro Reparaturart",
                    "Erfolgsraten verschiedener Reparaturmethoden",
                    "DIY vs Werft — Qualitätsunterschiede",
                ],
            },
        },
    },

    # =========================================================================
    # 5. NORMEN UND STANDARDS
    # =========================================================================
    "5_normen": {
        "title": "Normen, Standards und Vorschriften",
        "status": "implemented",
        "module": "norms_standards.py",
        "subcategories": {
            "5.1_iso_small_craft": {
                "title": "ISO Kleinfahrzeuge",
                "status": "implemented",
                "entries": "18 ISO-Normen mit Volltext-Beschreibung",
            },
            "5.2_ce_kategorien": {
                "title": "CE-Kategorien (A, B, C, D)",
                "status": "implemented",
                "entries": "4 Kategorien mit Wind/Wellen/Stabilitätsanforderungen",
            },
            "5.3_abyc": {
                "title": "ABYC Standards (US)",
                "status": "implemented",
                "entries": "8 Standards (E-11, H-24, H-33, A-22, H-27, P-1, TE-4, S-9)",
            },
            "5.4_rcd": {
                "title": "Recreational Craft Directive (EU 2013/53/EU)",
                "status": "implemented",
            },
            "5.5_klassifikation": {
                "title": "Klassifikationsgesellschaften",
                "status": "implemented",
                "entries": "6 (Lloyd's, DNV, BV, RINA, ABS, TÜV SÜD)",
            },
            "5.6_sicherheit": {
                "title": "Sicherheitsausrüstung",
                "status": "implemented",
                "entries": "Rettungswesten, Feuerlöscher, Signalmittel, EPIRB, Rettungsinseln, COLREG",
            },
            "5.7_umwelt": {
                "title": "Umweltvorschriften",
                "status": "implemented",
                "entries": "EPA Tier 3, EU Stage V, MARPOL, TBT-Verbot, Biofouling",
            },
            "5.8_gutachten": {
                "title": "Gutachten und Inspektion",
                "status": "implemented",
                "entries": "5 Gutachtentypen (Kaufgutachten, Versicherung, Zustand, Osmose, Rigg)",
            },
        },
    },

    # =========================================================================
    # 6. MARKT- UND WETTBEWERBSWISSEN
    # =========================================================================
    "6_markt": {
        "title": "Markt- und Wettbewerbswissen",
        "status": "implemented",
        "module": "db/seed.py → SEED_COMPETITORS (50 Modelle)",
    },

    # =========================================================================
    # 7. BORDSYSTEME (Yacht Systems)
    # =========================================================================
    "7_bordsysteme": {
        "title": "Bordsysteme — Yacht Systems",
        "status": "implemented",
        "subcategories": {
            "7.1_elektrik": {
                "title": "Elektrik und Elektronik",
                "status": "implemented",
                "module": "yacht_systems_electrical.py",
                "entries": "10 Kabeltypen, 8 Batteriesysteme, 11 Ladesysteme, 9 Verteilung, "
                           "5 Erdung, 6 Steckverbinder, 8 Navigationselektronik, 6 Beleuchtung, "
                           "10 Fehlerdiagnosen",
                "functions": ["calculate_cable_size()", "assess_electrical_installation()"],
            },
            "7.2_sanitaer": {
                "title": "Sanitär- und Rohrleitungssysteme",
                "status": "implemented",
                "module": "yacht_systems_plumbing.py",
                "entries": "8 Rohrmaterialien, 8 Schlauchtypen, 8 Seeventile, 10 Pumpen, "
                           "Frischwasser/Sanitär/Kraftstoff/Gas-Systeme, Winterfest-Prozeduren",
                "functions": ["assess_plumbing_installation()"],
            },
            "7.3_rigg": {
                "title": "Rigg- und Segelsysteme",
                "status": "implemented",
                "module": "yacht_systems_rigging.py",
                "entries": "8 stehendes Gut, 9 Endverbindungen, 12 laufendes Gut, 8 Tauwerk, "
                           "12 Winschen/Hardware, 6 Mast/Baum, 8 Segeltypen, Inspektionskriterien",
                "functions": ["assess_rigging_condition()"],
            },
            "7.4_antrieb": {
                "title": "Antriebs- und Motorsysteme",
                "status": "implemented",
                "module": "yacht_systems_propulsion.py",
                "entries": "9 Motortypen (Yanmar, Volvo, Beta, Torqeedo etc.), 7 Antriebsstrang, "
                           "7 Propellertypen, 4 Kühlsysteme, 4 Abgassysteme, 5 Getriebe, "
                           "Verbrauchsdatenbank, Wartungsplan (100h-2000h)",
                "functions": ["assess_propulsion_system()"],
            },
        },
    },

    # =========================================================================
    # 8. FORENSISCHE ANALYSE (Failure Analysis)
    # =========================================================================
    "8_forensik": {
        "title": "Forensische Analyse — Versagensmuster und Degradation",
        "status": "implemented",
        "module": "forensic_failure_analysis.py",
        "subcategories": {
            "8.1_material_wechselwirkungen": {
                "title": "Material-Material-Versagensszenarien",
                "status": "implemented",
                "entries": "14 dokumentierte Versagensmuster mit Mechanismus, Onset und Prävention",
            },
            "8.2_degradationskreislaeufe": {
                "title": "Kumulative Degradationskreisläufe",
                "status": "implemented",
                "entries": "6 selbstverstärkende Kreisläufe (Feuchtigkeit, Osmose, Korrosion, Schimmel, Stray Current, Osmoseblase)",
            },
            "8.3_feuchtigkeitspfade": {
                "title": "Versteckte Feuchtigkeitspfade",
                "status": "implemented",
                "entries": "13 versteckte Wasserwege mit Ausbreitungsradius und Erkennung",
            },
            "8.4_chemische_unvertraeglichkeiten": {
                "title": "Chemische Unverträglichkeiten",
                "status": "implemented",
                "entries": "10 Materialpaarungen (Polyester/Styropor, Silikon/Lack, Kupfer-AF/Alu, etc.)",
            },
            "8.5_osmose": {
                "title": "Osmose-Komplettwissen",
                "status": "implemented",
                "entries": "Mechanismus, Onset pro Harztyp, Tropeneffekt, Inspektion, Prävention, Reparatur",
            },
            "8.6_laminatfehler": {
                "title": "Laminatfehler-Systematik",
                "status": "implemented",
                "entries": "7 Fehlertypen mit Festigkeitsminderung in %, Glas-Harz-Verhältnistabelle",
            },
            "8.7_galvanische_reihe": {
                "title": "Galvanische Spannungsreihe Marine",
                "status": "implemented",
                "entries": "17 Materialien (Carbon → Magnesium) mit Potentialwerten",
            },
            "8.8_teakdeck": {
                "title": "Teakdeck-Versagenswissen",
                "status": "implemented",
                "entries": "Dreiseitige Haftung, Bond Breaker, 5 häufigste Fehler, Plankendicke, Fugentechnik",
            },
        },
    },

    # =========================================================================
    # 9. INSPEKTION (Survey & Assessment)
    # =========================================================================
    "9_inspektion": {
        "title": "Inspektion und Zustandsbewertung",
        "status": "implemented",
        "module": "inspection_knowledge.py",
        "subcategories": {
            "9.1_inspektionszonen": {
                "title": "Inspektionszonen (12 Bereiche)",
                "status": "implemented",
                "entries": "267+ Prüfpunkte über 12 Zonen (Unterwasser, Deck, Rigg, Motor, Elektrik, etc.)",
            },
            "9.2_gutachtentypen": {
                "title": "Gutachtentypen",
                "status": "implemented",
                "entries": "5 Typen (Kauf, Versicherung, Zustand, Osmose, Rigg) mit Dauer/Kosten",
            },
            "9.3_ndt_methoden": {
                "title": "Zerstörungsfreie Prüfverfahren",
                "status": "implemented",
                "entries": "7 Methoden (Feuchtemessung, Klopftest, Farbeindringprüfung, Ultraschall, Thermographie, Endoskop)",
            },
            "9.4_gelcoat_bewertung": {
                "title": "Gelcoat-Zustandsbewertung",
                "status": "implemented",
                "entries": "8 Schadenstypen (Crazing, Star Cracking, Osmose, Chalking, Print-through, etc.)",
            },
            "9.5_qualitaetsstufen": {
                "title": "Qualitätsstufen nach Bootstyp",
                "status": "implemented",
                "entries": "Serie vs Semi-Custom vs Custom/Superyacht — 8 Kriterien mit Grenzwerten",
            },
        },
    },

    # =========================================================================
    # 10. PRAXISERFAHRUNG (Practical Experience)
    # =========================================================================
    "10_praxiserfahrung": {
        "title": "Praxiserfahrung und Community-Wissen",
        "status": "implemented",
        "module": "practical_experience.py",
        "subcategories": {
            "10.1_hersteller_muster": {
                "title": "Hersteller-spezifische Schwachstellen",
                "status": "implemented",
                "entries": "13 Hersteller (Bavaria, Hanse, Jeanneau, Beneteau, Hallberg-Rassy, Najad, X-Yachts, Oyster, Dehler, Dufour, Contest, Moody, Feeling)",
            },
            "10.2_versagensfaelle": {
                "title": "Dokumentierte Versagensfälle",
                "status": "implemented",
                "entries": "17 reale Fälle mit Ursachenanalyse inkl. Saildrive-Membran, Landstrom-Korrosion, Teakdeck-Kernfäule, Mastfuß-Kompression, Messing-Seeventil, Rigg-Ermüdung",
            },
            "10.3_verarbeitungsqualitaet": {
                "title": "Verarbeitungsqualität als Hauptvariable",
                "status": "implemented",
                "entries": "Qualitätsvergleichstabelle, Indikatoren, Community-Weisheiten",
            },
            "10.4_seeventile": {
                "title": "Seeventil-Praxiswissen",
                "status": "implemented",
                "entries": "Bronze vs Messing, Dezinkierung, Doppelschellen-Regel, Schlauch-Permeation",
            },
            "10.5_kernmaterial": {
                "title": "Kernmaterial-Praxiswissen",
                "status": "implemented",
                "entries": "Balsa/PVC/SAN/Honeycomb — Golden Rule: Solid Insert bei jedem Durchbruch",
            },
        },
    },

    # =========================================================================
    # 11. EXPERT COMMUNITY KNOWLEDGE (YouTube, Foren, Fachzeitschriften)
    # =========================================================================
    "11_expert_community": {
        "title": "Experten-Community-Wissen aus YouTube, Foren und Fachpublikationen",
        "status": "implemented",
        "module": "expert_community_knowledge.py",
        "sources": "17 Quellen: BootsProfis, YACHT-TV, Marietim, Blauwasser.de, boote-forum.de, segeln-forum.de, yacht-forum.de, Pantaenius, float Magazin, Palstek, SVB, ADAC Skipper, NautiCare, bootstechnik.de, frag-jochen.de, Victron, Mastervolt",
        "subcategories": {
            "11.1_bootskauf": {
                "title": "Bootskauf-Expertise (Gutachterpraxis)",
                "status": "implemented",
                "entries": "3-Phasen-Inspektion (Erstbesichtigung, Detailinspektion, Probefahrt), Preisverhandlungs-Faktoren (10 Mängel mit Wertminderung), Alterserwartungen (5 Altersklassen)",
            },
            "11.2_osmose_detail": {
                "title": "Osmose-Detailwissen",
                "status": "implemented",
                "entries": "4-Stadien-Klassifikation, Risikofaktoren (Harztyp, Wassertemperatur, Verarbeitungsqualität), Trocknungsverfahren, Präventionsmaßnahmen",
            },
            "11.3_rigg_expertise": {
                "title": "Rigg-Expertenwissen",
                "status": "implemented",
                "entries": "Lebensdauer Draht/Rod/Textil, 5 häufigste Versagenspunkte, 6 Riggverlust-Ursachen mit Häufigkeit",
            },
            "11.4_seeventil_detail": {
                "title": "Seeventil-Materialvergleich",
                "status": "implemented",
                "entries": "5 Materialien (Bronze, Messing, DZR, Edelstahl, Composite) mit Lebensdauer und Risiko",
            },
            "11.5_motor_expertise": {
                "title": "Motor-Expertenwissen",
                "status": "implemented",
                "entries": "3 Marken detailliert (Volvo Penta, Yanmar, Beta Marine), 7 Goldene Wartungsregeln",
            },
            "11.6_teakdeck": {
                "title": "Teakdeck-Problematik",
                "status": "implemented",
                "entries": "4 häufige Probleme (Fugen, Undichtigkeit, Abschleifen, Sikaflex), Alternativen (Flexiteek, Kork)",
            },
            "11.7_elektrik_galvanik": {
                "title": "Elektrik und Galvanische Korrosion",
                "status": "implemented",
                "entries": "Landstrom-Korrosion (Mechanismus + 3 Lösungen), Kriechstrom-Diagnose, Batterie-Dimensionierung",
            },
            "11.8_antifouling": {
                "title": "Antifouling-Vergleich",
                "status": "implemented",
                "entries": "4 Typen (SPC, Hart-Matrix, Coppercoat, Ultraschall), Umweltvorschriften EU/Ostsee",
            },
            "11.9_composite_reparatur": {
                "title": "GFK/Sandwich-Reparaturwissen",
                "status": "implemented",
                "entries": "3 Kern-Risikoprofile, 2 Reparaturmethoden, 4 Gelcoat-Schadenstypen",
            },
            "11.10_winterlager": {
                "title": "Einwinterungs-Checkliste",
                "status": "implemented",
                "entries": "Vollständige Checkliste: Motor, Wassersystem, Elektrik, Rumpf/Deck, Rigg",
            },
            "11.11_energiesysteme": {
                "title": "Energiesysteme (Solar, Wind, Batterien, Watermaker)",
                "status": "implemented",
                "entries": "Solar-Erträge, Panel-Typen, MPPT vs PWM, 3 Windgeneratoren, LiFePO4-Praxis (Uma/Delos/Hafenkino), Watermaker (5 Marken)",
            },
            "11.12_equipment_tests": {
                "title": "Equipment-Vergleichstests (YACHT, SVB)",
                "status": "implemented",
                "entries": "Anker, Winschen, Feuerlöscher (Lithium), Kartenplotter, Rettungsmittel, Polituren, Segeltuch",
            },
            "11.13_gfk_reparatur_detail": {
                "title": "GFK-Reparatur Detailanleitungen",
                "status": "implemented",
                "entries": "Gelcoat-Reparatur (Marietim-Methode), Blasen-Reparatur (20:1-Regel), Deck-Soft-Spots, Interior-Refit, Landstrom-Normen",
            },
            "11.14_osmose_diagnostik": {
                "title": "Osmose-Diagnostik-Methoden",
                "status": "implemented",
                "entries": "5 Erkennungsmethoden: Feuchtemessung (Tramex), UV-Fluoreszenz, Blasen-Stichprobe, Klopftest, Roto-Blast",
            },
            "11.15_rigg_versicherung": {
                "title": "Rigg-Schadensstatistik (Pantaenius)",
                "status": "implemented",
                "entries": "500 Mastbrüche/3 Jahre, Kosten 30-100k EUR, Rig-Sense Pro, Farbeindringprüfung",
            },
            "11.16_gebrauchtboot_markt": {
                "title": "Gebrauchtboot-Marktwissen",
                "status": "implemented",
                "entries": "Preisbereiche nach Größe, Gutachterkosten, 7 Todsünden beim Bootskauf, 22 dokumentierte Versagensfälle",
            },
        },
    },
}
