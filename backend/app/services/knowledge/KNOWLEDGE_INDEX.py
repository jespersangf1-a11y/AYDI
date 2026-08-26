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
    "12_deck_hardware_deep": {
        "title": "Deck-Hardware Tiefenwissen",
        "module": "deck_hardware_deep",
        "description": "Exhaustive technical specifications for all marine deck hardware",
        "subcategories": {
            "12.1_winches": {
                "title": "Winschen-Datenbank",
                "status": "implemented",
                "entries": "Harken (Radial/Performa/Electric 15-80), Lewmar EVO, Andersen, Antal, Spinlock — Zugkraft, Übersetzung, Wartung, Troubleshooting",
            },
            "12.2_blocks": {
                "title": "Blöcke & Umlenkrollen",
                "status": "implemented",
                "entries": "Lastberechnung, Umlenkfaktoren, Kugel-/Nadel-/Gleitlager, Harken/Lewmar/Antal/Ronstan Specs",
            },
            "12.3_cleats": {
                "title": "Klampen & Klemmen",
                "status": "implemented",
                "entries": "Hornklampen, Camcleats, Clamcleats — Materialien (316SS, Bronze, Aluminium), Dimensionierung",
            },
            "12.4_tracks": {
                "title": "Schienensysteme",
                "status": "implemented",
                "entries": "T-Track 22-32mm, Lewmar Specs, Großschotwagen, Genua-Schienen, Montage-Befestigung",
            },
            "12.5_hatches": {
                "title": "Luken-Datenbank",
                "status": "implemented",
                "entries": "Lewmar (Low/Ultra-Low/Ocean Profile), Goiot, Bomar — Sandwich-Deck-Montage, Dichtungsprofile",
            },
            "12.6_portlights": {
                "title": "Bullaugen & Fenster",
                "status": "implemented",
                "entries": "Acryl vs Polycarbonat vs Glas, Dichtungsmethoden, UV-Beständigkeit, Nachschleifen",
            },
            "12.7_stanchions": {
                "title": "Relingsstützen & Drahtseile",
                "status": "implemented",
                "entries": "Fußtypen, Höhenanforderungen ISO 15085, Drahtseil-Materialien, Dyneema-Alternativen",
            },
            "12.8_pad_eyes": {
                "title": "Augenplatten & Beschlagsbefestigung",
                "status": "implemented",
                "entries": "Wichard Specs, Sicherheitsfaktoren, Backing-Plate-Berechnung, Kernverstärkung",
            },
            "12.9_maintenance": {
                "title": "Wartungsmatrix Deck-Hardware",
                "status": "implemented",
                "entries": "Schmierungsintervalle, Ersatzteil-Planung, Winterlagerung, Service-Kits",
            },
            "12.10_quality_origin": {
                "title": "Qualitäts- und Herkunftsmatrix",
                "status": "implemented",
                "entries": "Premiumhersteller vs Budgetmarken, OEM-Lieferketten, Fälschungserkennung",
            },
            "12.11_installation": {
                "title": "Best Practices Montage",
                "status": "implemented",
                "entries": "Kernverstärkung, Dichtungstechniken, Schraubendrehmomente, Anti-Knarr-Maßnahmen",
            },
        },
    },
    "13_coatings_sealants_deep": {
        "title": "Beschichtungs- und Dichtungssystem-Tiefenwissen",
        "module": "coatings_sealants_deep",
        "description": "Exhaustive technical specifications for marine sealants, paints, varnishes, and epoxy systems",
        "subcategories": {
            "13.1_sealants": {
                "title": "Dichtmassen-Datenbank",
                "status": "implemented",
                "entries": "PU/MS-Polymer/Polysulfid/Silikon/Butyl-Vergleich, Sikaflex (291i/295UV/591/290i DC), 3M (5200/4200/4000UV), Anwendungsmatrix",
            },
            "13.2_epoxy": {
                "title": "Epoxid-Systeme",
                "status": "implemented",
                "entries": "West System (105 Harz, 205-209 Härter, Füller 403-410), Aminröte, Harz-Vergleich Polyester/Vinylester/Epoxid",
            },
            "13.3_paint_systems": {
                "title": "Lacksysteme",
                "status": "implemented",
                "entries": "Antifouling (International/Hempel/Jotun), Topside 2K-PU, Alkyd vs PU, Awlgrip vs Alexseal, Holzlacke",
            },
            "13.4_polyurethane_chemistry": {
                "title": "PU-Chemie",
                "status": "implemented",
                "entries": "Isocyanat-Reaktionen, Feuchtehärtung, Topfzeit-Faktoren, Haftungsmechanismen",
            },
            "13.5_cure_factors": {
                "title": "Aushärtungsfaktoren",
                "status": "implemented",
                "entries": "Temperatur/Feuchte-Matrizen, Arrhenius-Modell, Mindest-/Maximalwerte, Taupunkt-Berechnung",
            },
            "13.6_common_mistakes": {
                "title": "Typische Fehler & Behebung",
                "status": "implemented",
                "entries": "Haftungsversagen, Blasenbildung, Kraterbildung, Ablösung — Ursachen und Reparatur",
            },
            "13.7_surface_prep": {
                "title": "Oberflächenvorbereitung Detail",
                "status": "implemented",
                "entries": "GFK/Holz/Aluminium/Edelstahl-spezifisch, Schleifgrade, Reinigung, Primer-Auswahl",
            },
            "13.8_compatibility": {
                "title": "Kompatibilitätsmatrix",
                "status": "implemented",
                "entries": "Sealant-auf-Sealant, Lack-auf-Lack, Primer-Substrate, Lösemittel-Verträglichkeit",
            },
            "13.9_specs_international": {
                "title": "Technische Spezifikationen (International Paint)",
                "status": "implemented",
                "entries": "Ergiebigkeit, Schichtdicken, Überarbeitungszeiten, Produktreihen-Vergleich",
            },
            "13.10_environmental": {
                "title": "Umwelt & Gesundheit",
                "status": "implemented",
                "entries": "VOC-Grenzwerte, Biozid-Regulierung, Atemschutz, Entsorgung, EU-Richtlinien",
            },
        },
    },
    "14_rigging_anchor_steering_deep": {
        "title": "Rigg-Hardware, Anker, Steuerung & Borddurchlässe — Tiefenwissen",
        "module": "rigging_anchor_steering_deep",
        "description": "Exhaustive specifications for rigging terminals, anchors, steering systems, and through-hull fittings",
        "subcategories": {
            "14.1_rigging_terminals": {
                "title": "Rigg-Terminals",
                "status": "implemented",
                "entries": "Sta-Lok/Norseman/Hi-MOD, Draht 1x19/7x19/Dyform, Stabrigg Navtec Nitronic 50, Montage-Drehmomente",
            },
            "14.2_turnbuckles": {
                "title": "Wantenspanner",
                "status": "implemented",
                "entries": "Offen/geschlossen, Sicherungsmethoden (Splinte/Draht/Loctite), Dimensionierung, Hebelberechnung",
            },
            "14.3_shackles": {
                "title": "Schäkel-Datenbank",
                "status": "implemented",
                "entries": "Wichard Specs, D-Schäkel-Lasten, Schnappschäkel, Bolzentypen, WLL vs Bruchlast",
            },
            "14.4_anchor_systems": {
                "title": "Ankersysteme",
                "status": "implemented",
                "entries": "7 Ankertypen (Rocna/Mantus/Spade/Fortress/CQR/Bruce/Delta), Kettengüten G30-G70, Roden-Typen, Dimensionierung",
            },
            "14.5_windlass": {
                "title": "Ankerwindenl",
                "status": "implemented",
                "entries": "Vertikal/Horizontal, Lofrans/Lewmar/Quick, Elektrische Dimensionierung, Kettennuss-Kompatibilität",
            },
            "14.6_steering": {
                "title": "Steueranlagen",
                "status": "implemented",
                "entries": "Seilzug/Kette/Zahnstange, Jefa/Whitlock, Ruder-Lager, Autopilot-Hydraulik, Notpinne",
            },
            "14.7_through_hulls": {
                "title": "Borddurchlässe",
                "status": "implemented",
                "entries": "Groco/TruDesign/Blakes, Bronze-Legierungen, Kugel- vs Kegelhahn, Schlauchanschlüsse, Elektrolyse-Schutz",
            },
            "14.8_practical_guidelines": {
                "title": "Praktische Richtlinien",
                "status": "implemented",
                "entries": "Rigg-Inspektion (rig-check), Anker-Dimensionierung, Steueranlagen-Wartung, Borddurchlass-Inspektion",
            },
        },
    },
    # =========================================================================
    # 15. RUMPFKONSTRUKTION TIEFENWISSEN (hull_construction_deep.py)
    # =========================================================================
    "15_hull_construction_deep": {
        "title": "Rumpfkonstruktion — Vollständiges Tiefenwissen",
        "status": "implemented",
        "module": "hull_construction_deep.py",
        "description": "Harz-/Faser-/Gelcoat-/Kernmaterial-Datenbanken, Konstruktionsmethoden, Rumpf-Deck-Verbindungen, Strukturanalyse, Reparatur, QA, ISO 12215",
        "subcategories": {
            "15.1_resins": {"title": "Harzsysteme", "status": "implemented", "entries": "Orthophthal-/Isophthal-Polyester, Vinylester, Epoxid, Phenol — Mechanik, Chemie, Osmose-Risiko"},
            "15.2_fibers": {"title": "Fasertypen", "status": "implemented", "entries": "E-Glas, S-Glas, Carbon HM/HT/IM, Aramid/Kevlar, Basalt, UHMWPE — Kennwerte, Hybrid-Laminate"},
            "15.3_gelcoat": {"title": "Gelcoat-Systeme", "status": "implemented", "entries": "Iso-NPG, Vinylester-Gelcoat, Epoxid-Primer, Fehlerbild-Katalog (Crazing, Pinholes, Chalking)"},
            "15.4_core_materials": {"title": "Kernmaterialien", "status": "implemented", "entries": "End-Grain Balsa, PVC Divinycell, SAN CoreCell, Nomex/Alu/PP-Honeycomb — Feuchteaufnahme, Kompression"},
            "15.5_construction_methods": {"title": "Bauverfahren", "status": "implemented", "entries": "Handlaminat, Vakuumsack, VARTM/SCRIMP Infusion, Prepreg/Autoklav — Faseranteile, QA-Methoden"},
            "15.6_hull_deck_joints": {"title": "Rumpf-Deck-Verbindungen", "status": "implemented", "entries": "Verschraubt, Durchbolzt, Verklebt (3M 5200/Sikaflex 292/Plexus), Überlaminiert — Versagensmodi"},
            "15.7_structural_analysis": {"title": "Strukturanalyse", "status": "implemented", "entries": "Laminat-Theorie (CLT), FEA-Grundlagen, ISO 12215 Scantling, Spannungsverteilung"},
            "15.8_repair": {"title": "Reparaturverfahren", "status": "implemented", "entries": "Osmose-Sanierung, Strukturreparatur, Gelcoat-Ausbesserung, Kernersatz, Blister-Behandlung"},
            "15.9_materials_specs": {"title": "Materialspezifikationen", "status": "implemented", "entries": "Mechanische Kennwerte-Tabellen, Temperaturbeständigkeit, UV-Resistenz"},
            "15.10_environment": {"title": "Umwelt & Alterung", "status": "implemented", "entries": "Osmose-Mechanismen, UV-Degradation, Hydrolyse, Temperaturzyklen, Ermüdung"},
            "15.11_hybrid_advanced": {"title": "Hybrid & Fortgeschrittene Materialien", "status": "implemented", "entries": "Carbon-Glas-Hybride, Infusionsepoxid, Nano-Modifikation, Bio-Composites"},
            "15.12_case_studies": {"title": "Fallstudien", "status": "implemented", "entries": "Reale Rumpfschäden, Osmose-Fälle, Strukturversagen, Reparatur-Dokumentation"},
            "15.13_qa_standards": {"title": "QA & Normen", "status": "implemented", "entries": "ISO 12215, CE 2013/53/EU, Lloyd's/DNV-Klassifikation, Prüfverfahren"},
            "15.14_reference": {"title": "Technische Referenzdaten", "status": "implemented", "entries": "Umrechnungstabellen, Materialkennwerte-Vergleich, Harz-Mischverhältnisse"},
        },
    },
    # =========================================================================
    # 16. KIEL / RUDER / UNTERWASSER (keel_rudder_underwater_deep.py)
    # =========================================================================
    "16_keel_rudder_underwater_deep": {
        "title": "Kiel, Ruder & Unterwasserschiff — Tiefenwissen",
        "status": "implemented",
        "module": "keel_rudder_underwater_deep.py",
        "description": "Kieltypen & -bolzen, Ruderanlagen, Antifouling-Systeme, Opferanoden, Integrierte Warnungen",
        "subcategories": {
            "16.1_keels": {"title": "Kielsysteme", "status": "implemented", "entries": "5 Kieltypen, 4 Bolzenmaterialien, 5 Inspektionsmethoden, Bavaria Match Recall, Cheeki Rafiki"},
            "16.2_rudders": {"title": "Ruderanlagen", "status": "implemented", "entries": "Spaten-/Skeg-/Zwillingsruder, 3 Lagersysteme, 3 Dichtungssysteme, Verschleißmessung"},
            "16.3_antifouling": {"title": "Antifouling", "status": "implemented", "entries": "Ablativ/Hart/Foul-Release/Kupferfrei, Kompatibilitätsmatrix, 3 Regulierungsrahmen"},
            "16.4_anodes": {"title": "Opferanoden", "status": "implemented", "entries": "Zink/Magnesium/Aluminium, 1%-Regel, 50%-Austausch, Galvanische Spannungsreihe"},
            "16.5_warnings": {"title": "Integrierte Warnungen", "status": "implemented", "entries": "Kielbolzen-Korrosion, Alu-Kupfer-Kontakt, Ruder-Delamination, Osmose-Kiel"},
        },
    },
    # =========================================================================
    # 17. MOTOR & ANTRIEB (engine_drivetrain_deep.py)
    # =========================================================================
    "17_engine_drivetrain_deep": {
        "title": "Motor & Antriebsstrang — Tiefenwissen",
        "status": "implemented",
        "module": "engine_drivetrain_deep.py",
        "description": "Marine-Diesel-Datenbank, Kühlsystem, Abgasanlage, Kraftstoffsystem, Antriebsstrang, Steueranlage",
        "subcategories": {
            "17.1_engines": {"title": "Marine-Diesel", "status": "implemented", "entries": "Yanmar/Volvo Penta/Nanni/Beta Marine, Leistungskurven, Wartungsintervalle, Common-Rail vs mechanisch"},
            "17.2_cooling": {"title": "Kühlsystem", "status": "implemented", "entries": "Seewasser-/Frischwasser-Kreislauf, Impeller, Wärmetauscher, Mischkrümmer (häufigstes Versagen)"},
            "17.3_exhaust": {"title": "Abgasanlage", "status": "implemented", "entries": "Nass-/Trockenabgas, Mischkrümmer Guss-/Edelstahl, Hydrolock-Risiko, Abgasschlauch-Inspektio"},
            "17.4_fuel": {"title": "Kraftstoffsystem", "status": "implemented", "entries": "Diesel Bug, Racor-Filter, Tankinspektion, EN 590, Wasserabscheider"},
            "17.5_drivetrain": {"title": "Antriebsstrang", "status": "implemented", "entries": "Wellenanlage 0.05mm, PSS-Dichtung, Saildrive-Membran 7-10J, Propeller fest/falt/verstellbar"},
            "17.6_steering": {"title": "Steueranlage", "status": "implemented", "entries": "Seilzug/Kette/Zahnstange, Hydraulik, Autopilot-Integration, Notpinne"},
        },
    },
    # =========================================================================
    # 18. ELEKTRIK (electrical_systems_deep.py)
    # =========================================================================
    "18_electrical_systems_deep": {
        "title": "Elektrische Systeme — Tiefenwissen",
        "status": "implemented",
        "module": "electrical_systems_deep.py",
        "description": "Batterien, Verkabelung, Verbindungstechnik, Absicherung, Landstrom, Wechselrichter, Korrosionsschutz",
        "subcategories": {
            "18.1_batteries": {"title": "Batteriesysteme", "status": "implemented", "entries": "AGM/Gel/LiFePO4/Blei, BMS, Ladeprofile, ABYC E-13, Kapazitätsberechnung"},
            "18.2_wiring": {"title": "Verkabelung", "status": "implemented", "entries": "ABYC E-11, 3%/10%-Spannungsfall, Querschnittsberechnung, Kabeltypen verzinnt/Marine-Grade"},
            "18.3_connections": {"title": "Verbindungstechnik", "status": "implemented", "entries": "Crimpung (Ratchet-Presszangen), Lötverbot ABYC, Schrumpfschlauch, Korrosionsschutz"},
            "18.4_fusing": {"title": "Absicherung", "status": "implemented", "entries": "ANL/ATO/MIDI/Streifensicherung, 150%-Regel, Batterie-Hauptschalter, Leitungsschutz"},
            "18.5_shore_power": {"title": "Landstrom", "status": "implemented", "entries": "230V AC, Trenntrafo vs Galvanischer Isolator, FI-Schutz 30mA, Polaritätsprüfung"},
            "18.6_inverter_gen": {"title": "Wechselrichter & Generatoren", "status": "implemented", "entries": "Victron/Mastervolt/Whisper, Reine Sinuswelle, Fischer Panda, Parallelschaltung"},
            "18.7_corrosion": {"title": "Korrosionsschutz", "status": "implemented", "entries": "Streustrom 10-1000x Beschleunigung, Galvanischer Isolator, ICCP, Erdungskonzepte"},
            "18.8_warnings": {"title": "Kritische Warnungen", "status": "implemented", "entries": "Lithium-Thermal-Runaway, AC-Leckstrom im Wasser, Falsche Polarität, Überlastung"},
        },
    },
    # =========================================================================
    # 19. SANITÄR / INTERIEUR / SICHERHEIT (sanitary_interior_safety_deep.py)
    # =========================================================================
    "19_sanitary_interior_safety_deep": {
        "title": "Sanitär, Interieur & Sicherheit — Tiefenwissen",
        "status": "implemented",
        "module": "sanitary_interior_safety_deep.py",
        "description": "Seeventile, Toiletten, Gas, Interieur, Feuchtigkeit, Brandschutz, Leckabwehr, Stabilität, Normen",
        "subcategories": {
            "19.1_seacocks": {"title": "Seeventile", "status": "implemented", "entries": "Groco/TruDesign/Blakes, Bronze DZR vs Komposit, Kugel-/Kegelhahn, Wartungsintervalle"},
            "19.2_toilets": {"title": "Toilettensysteme", "status": "implemented", "entries": "Manuell/Elektrisch/Vakuum, Jabsco/Raritan, Fäkalientank, Joker-Ventile, Geruchsprobleme"},
            "19.3_gas": {"title": "Gasinstallation", "status": "implemented", "entries": "EN ISO 10239, Gasprüfung, Gaswarner, Gaskasten-Drainage, Schlauch-Lebensdauer"},
            "19.4_interior": {"title": "Interieur", "status": "implemented", "entries": "Sperrholz Marine-Grade, Furniere, Polster, Isolierung, Schimmelprävention"},
            "19.5_moisture": {"title": "Feuchtigkeit & Kondensation", "status": "implemented", "entries": "Taupunktberechnung, Dampfsperre, Ventilation, Feuchtemessung, Schimmelbekämpfung"},
            "19.6_fire_safety": {"title": "Brandschutz", "status": "implemented", "entries": "ISO 9094, Feuerlöscher-Typen, Löschanlage Motorraum, Fluchtwege, Rauchmelder"},
            "19.7_leak_defense": {"title": "Leckabwehr", "status": "implemented", "entries": "Bilgepumpen elektrisch/manuell, Hochwasseralarm, Lenzventile, Notmaßnahmen"},
            "19.8_stability": {"title": "Stabilität & Seetüchtigkeit", "status": "implemented", "entries": "ISO 12217, CE-Kategorien A-D, AVS, GZ-Kurve, Beladungsoptimierung"},
            "19.9_standards": {"title": "Normen & Vorschriften", "status": "implemented", "entries": "CE 2013/53/EU, ISO-Sammlung, BSH, ABYC, Flaggenstaatanforderungen"},
        },
    },
    # =========================================================================
    # 20. RIGG / SEGEL / TEAKDECK (rigging_sails_deck_deep.py)
    # =========================================================================
    "20_rigging_sails_deck_deep": {
        "title": "Rigg, Segel & Teakdeck — Tiefenwissen",
        "status": "implemented",
        "module": "rigging_sails_deck_deep.py",
        "description": "Stehendes Rigg, Masten, Segel, Teakdeck, Decksbeschlag-Montage, Fehlerbehebung, Wartung",
        "subcategories": {
            "20.1_standing_rigging": {"title": "Stehendes Rigg", "status": "implemented", "entries": "1x19/7x19/Dyform/Rod, Nitronic 50, Terminals, Inspektionsmethoden, Lebensdauer 10-15J"},
            "20.2_masts": {"title": "Masten & Bäume", "status": "implemented", "entries": "Aluminium 6082-T6, Carbon, Profil-Querschnitte, Salingwinkel, Mastfuß"},
            "20.3_sails": {"title": "Segel", "status": "implemented", "entries": "Dacron/Laminat/3DL, Segelschnitt, UV-Schutz, Nähte, Lebensdauer-Faktoren"},
            "20.4_teak_deck": {"title": "Teakdeck", "status": "implemented", "entries": "Sikaflex 298/290 DC PRO, Bond Breaker, Burma vs Plantation, Dicke 8-10mm, Schleifen"},
            "20.5_hardware_mounting": {"title": "Decksbeschlag-Montage", "status": "implemented", "entries": "Backing-Plates, Dichtung Butylband/Sikaflex, Kernverstärkung, Drehmomente"},
            "20.6_troubleshooting": {"title": "Rigg-Fehlerbehebung", "status": "implemented", "entries": "Drahtbruch, Korrosion, Lose Terminals, Mastfall-Probleme, Not-Reparatur"},
            "20.7_sail_maintenance": {"title": "Segel-Wartung", "status": "implemented", "entries": "Waschen, UV-Schutz erneuern, Nähte prüfen, Lagerung, Reparatur-Patches"},
            "20.8_teak_maintenance": {"title": "Teakdeck-Wartung", "status": "implemented", "entries": "Reinigung, Fugen-Erneuerung, Schleifen, Öl vs unbehandelt, Leck-Diagnose"},
            "20.9_installation_standards": {"title": "Montage-Standards", "status": "implemented", "entries": "ISO-Vorgaben, ABYC H-27, Drehmoment-Tabellen, Sealant-Auswahl, Schraubentypen"},
        },
    },
    # =========================================================================
    # 21. ALTERUNG / LEBENSZYKLUS / HERSTELLER (aging_lifecycle_manufacturers_deep.py)
    # =========================================================================
    "21_aging_lifecycle_manufacturers_deep": {
        "title": "Alterung, Lebenszyklus & Hersteller-Datenbank",
        "status": "implemented",
        "module": "aging_lifecycle_manufacturers_deep.py",
        "description": "Material-Lebensdauern (16 Materialien), Degradationszyklen, 23 Hersteller-Profile (Segel/Motor/Custom)",
        "subcategories": {
            "21.1_material_lifespans": {"title": "Material-Lebensdauern", "status": "implemented", "entries": "16 Materialien mit min/typ/max Lebensdauer, Degradationsmechanismen, Inspektionsmethoden"},
            "21.2_degradation_cycles": {"title": "Degradationszyklen", "status": "implemented", "entries": "3 selbstverstärkende Zyklen: Feuchtigkeit→Steifigkeit, Osmose→Mikrorisse, Korrosion→Dichtung"},
            "21.3_sail_manufacturers": {"title": "Segel-Yacht-Hersteller", "status": "implemented", "entries": "11 Werften: Bavaria, Hanse, Jeanneau, Beneteau, Hallberg-Rassy, X-Yachts, Oyster, Swan, Dehler, Najad, Contest"},
            "21.4_motor_manufacturers": {"title": "Motor-Yacht-Hersteller", "status": "implemented", "entries": "8 Werften: Princess, Sunseeker, Fairline, Nimbus, Linssen, Grand Banks, Nordhavn, Boston Whaler"},
            "21.5_custom_manufacturers": {"title": "Custom-/Semi-Custom-Werften", "status": "implemented", "entries": "4 Werften: Baltic Yachts, Southern Wind, Wally, Spirit Yachts"},
        },
    },
    # =========================================================================
    # 22. MARKDOWN-WISSENSDATEIEN (261 nummerierte Dateien, 32 Kategorien, ~850K Zeilen;
    #     davon 260 kanonisch geladen — siehe description)
    # =========================================================================
    "22_markdown_knowledge": {
        "title": "Markdown-Wissensdatenbank — Vollständige Materialreferenz",
        "status": "implemented",
        "module": "markdown_knowledge_loader.py → load_all_markdown_knowledge()",
        "description": (
            "261 nummerierte Markdown-Dateien in 32 Kategorien (850.268 Zeilen). "
            "Eine davon (24_05_..._clean.md) ist eine Backup-Variante und wird vom "
            "Loader ausgeschlossen → 260 kanonische Dateien geladen (847.782 Zeilen) "
            "(Slug-Kollisionen unter Komposit-Schlüssel bewahrt, kein stilles Überschreiben). "
            "Kategorie 32 (Designsprachen & Stile) ergänzt die technische Materialreferenz "
            "um Exterieur-/Interieur-Designwissen über Marken, Epochen und Jahre. "
            "Vollintegriert via knowledge_retrieval.py → Analysis-Module → API."
        ),
        "entries": 260,
        "subcategories": {
            "22.1_dichtungen_profile": {
                "title": "01 — Dichtungen und Profile",
                "status": "implemented",
                "entries": 12,
                "details": [
                    "01_01 Fenster-Dichtungen", "01_02 Luken-Dichtungen",
                    "01_03 Luken-Scharnier-Dichtungen & Gasdruckfedern",
                    "01_04 Niedergangs-Dichtungen", "01_05 Borddurchlass-Dichtungen",
                    "01_06 Wellenabdichtung (Stopfbuchse/Lippendichtung/PSS)",
                    "01_07 Saildrive-Manschetten", "01_08 Motordichtungen",
                    "01_09 Kühlwassersystem-Dichtungen",
                    "01_10 Deck-Beschlag-Abdichtung", "01_11 Mast-Manschette",
                    "01_12 Steuerkoker/Ruderschaft-Abdichtung",
                ],
            },
            "22.2_dichtstoffe_kleber": {
                "title": "02 — Dichtstoffe und Kleber",
                "status": "implemented",
                "entries": 13,
                "details": [
                    "02_01 PU-Dichtstoffe elastisch", "02_02 PU-Dichtstoffe permanent/strukturell",
                    "02_03 Teakdeck-Fugenmasse", "02_04 Silikon-Dichtstoffe",
                    "02_05 Polysulfid-Dichtstoffe", "02_06 Butylband",
                    "02_07 Epoxid-Kleber", "02_08 Acrylat-Kleber",
                    "02_09 Sekundenkleber Marine", "02_10 Kontaktkleber",
                    "02_11 Primer für Dichtstoffe", "02_12 Reiniger und Entfetter",
                    "02_13 Anti-Seize-Pasten",
                ],
            },
            "22.3_beschichtungen_farben": {
                "title": "03 — Beschichtungen und Farben",
                "status": "implemented",
                "entries": 16,
                "details": [
                    "03_01 Antifouling selbstpolierend", "03_02 Antifouling hart",
                    "03_03 Antifouling kupferfrei", "03_04 Foul-Release-Silikon",
                    "03_05 Coppercoat/Permanentsysteme", "03_06 Unterwasser-Primer",
                    "03_07 Epoxid Barrier Coat / Osmoseschutz",
                    "03_08 Topside-Lack 2K PU", "03_09 Topside-Lack 1K",
                    "03_10 Klarlack für Holz", "03_11 Teak-Öl und Pflege",
                    "03_12 Gelcoat-Reparaturmaterial", "03_13 Fairing Compounds/Spachtel",
                    "03_14 Edelstahl-Pflegemittel & Passivierung",
                    "03_15 Aluminium-Beschichtungssysteme", "03_16 Bilgenfarbe",
                ],
            },
            "22.4_harze_fasern_verbundwerkstoffe": {
                "title": "04 — Harze, Fasern & Verbundwerkstoffe",
                "status": "implemented",
                "entries": 12,
                "details": [
                    "04_01 Polyester-Harz", "04_02 Vinylester-Harz",
                    "04_03 Epoxid-Harz", "04_04 Füllstoffe für Harze",
                    "04_05 E-Glas Gewebe und Gelege", "04_06 S-Glas",
                    "04_07 Carbongewebe", "04_08 Aramidgewebe",
                    "04_09 Hybridgewebe", "04_10 Kernmaterial Endkorn-Balsa",
                    "04_11 Kernmaterial PVC-Schaum", "04_12 Kernmaterial SAN-Schaum",
                ],
            },
            "22.5_halbzeuge_beschlaege": {
                "title": "05 — Halbzeuge und Beschläge",
                "status": "implemented",
                "entries": 10,
                "details": [
                    "05_01 Edelstahl-Schrauben", "05_02 Edelstahl-Bolzen & Muttern",
                    "05_03 Bronze-Schrauben & Bolzen", "05_04 Nieten",
                    "05_05 Gewindeeinsätze", "05_06 Backing Plates",
                    "05_07 Edelstahl-Halbzeuge", "05_08 Aluminium-Halbzeuge",
                    "05_09 Bronze-Armaturen",
                    "05_10 Galvanische Spannungsreihe & Thru-Hulls",
                ],
            },
            "22.6_systeme": {
                "title": "06 — Systeme (Schläuche und Leitungen)",
                "status": "implemented",
                "entries": 9,
                "details": [
                    "06_01 Kühlwasserschläuche",
                    "06_02 Auspuffschläuche (Wet/Dry Exhaust)",
                    "06_03 Sanitärschläuche (permeationsfest)",
                    "06_04 Kraftstoffschläuche (Diesel/Benzin)",
                    "06_05 Trinkwasserschläuche (KTW/FDA-konform)",
                    "06_06 Gasschläuche (Propan/Butan LPG)",
                    "06_07 Hydraulikschläuche (Ruder/Winschen/Stabilisatoren)",
                    "06_08 Bilgenschläuche und Lenzleitungen",
                    "06_09 Deckwaschschläuche und Ankerspül-Systeme",
                ],
            },
            "22.7_seeventile_borddurchlaesse": {
                "title": "07 — Seeventile und Borddurchlässe",
                "status": "implemented",
                "entries": 6,
                "details": [
                    "07_01 Seeventile (Bronze/Messing/Komposit)",
                    "07_02 Borddurchlässe und Rumpfdurchführungen",
                    "07_03 Seeventilhähne (Kugel-/Kegelhahn)",
                    "07_04 Seewasserfilter und Seiher",
                    "07_05 Schlauchverbindungen und Stutzen",
                    "07_06 Opferanoden und Korrosionsschutz",
                ],
            },
            "22.8_luken_fenster_bullaugen": {
                "title": "08 — Luken, Fenster und Bullaugen",
                "status": "implemented",
                "entries": 5,
                "details": [
                    "08_01 Decksluken (Lewmar/Goiot/Bomar)",
                    "08_02 Bullaugen und Seitenfenster",
                    "08_03 Windschutzscheiben und Frontfenster",
                    "08_04 Lukenbeschläge und Gasdruckfedern",
                    "08_05 Luken- und Fensterdichtungen",
                ],
            },
            "22.9_winschen": {
                "title": "09 — Winschen",
                "status": "implemented",
                "entries": 7,
                "details": [
                    "09_01 Winschen Grundlagen und Typen",
                    "09_02 Harken Winschen",
                    "09_03 Lewmar Winschen",
                    "09_04 Andersen Winschen",
                    "09_05 Antal Winschen",
                    "09_06 Elektrische Winschen und Nachrüstung",
                    "09_07 Winschen Wartung und Troubleshooting",
                ],
            },
            "22.10_bloecke_umlenkrollen": {
                "title": "10 — Blöcke und Umlenkrollen",
                "status": "implemented",
                "entries": 5,
                "details": [
                    "10_01 Blöcke Grundlagen und Typen",
                    "10_02 Harken Blöcke",
                    "10_03 Lewmar, Antal und Ronstan Blöcke",
                    "10_04 Hochlast-Blöcke und Umlenkrollen",
                    "10_05 Blöcke Wartung und Troubleshooting",
                ],
            },
            "22.11_klampen_klemmen_schienensysteme": {
                "title": "11 — Klampen, Klemmen und Schienensysteme",
                "status": "implemented",
                "entries": 5,
                "details": [
                    "11_01 Klampen Grundlagen und Typen",
                    "11_02 Cam Cleats und Klemmen",
                    "11_03 Schienensysteme und Schlitten",
                    "11_04 Relingsstützen und Sicherheitsleinen",
                    "11_05 Augenplatten und Decksbeschläge",
                ],
            },
            "22.12_schaekel_wirbel_verbinder": {
                "title": "12 — Schäkel, Wirbel und Verbinder",
                "status": "implemented",
                "entries": 5,
                "details": [
                    "12_01 Schäkel Grundlagen und Typen",
                    "12_02 Wirbel und Drehgelenke",
                    "12_03 Bolzen, Splinte und Sicherungselemente",
                    "12_04 Schnappschäkel und Karabiner",
                    "12_05 Verbinder Wartung und Troubleshooting",
                ],
            },
            "22.13_ankersysteme_festmacher": {
                "title": "13 — Ankersysteme und Festmacher",
                "status": "implemented",
                "entries": 8,
                "details": [
                    "13_01 Anker Grundlagen und Typen",
                    "13_02 Ankerketten und Kettenvorlauf",
                    "13_03 Ankerwinden",
                    "13_04 Ankergeschirr und Zubehör",
                    "13_05 Festmacherleinen und Fender",
                    "13_06 Ankerbucht und Bugbeschläge",
                    "13_07 Mooring-Systeme",
                    "13_08 Ankersysteme Wartung und Troubleshooting",
                ],
            },
            "22.14_steueranlagen_autopilot": {
                "title": "14 — Steueranlagen und Autopilot",
                "status": "implemented",
                "entries": 8,
                "details": [
                    "14_01 Steueranlagen Grundlagen",
                    "14_02 Mechanische Steuerung (Seilzug/Kette/Zahnstange)",
                    "14_03 Hydraulische Steuerung",
                    "14_04 Ruderanlage und Lager",
                    "14_05 Autopilot-Systeme",
                    "14_06 Notruder und Notsteuerung",
                    "14_07 Steuerräder und Pinnen",
                    "14_08 Steueranlagen Wartung und Troubleshooting",
                ],
            },
            "22.15_rollreffanlagen_furler": {
                "title": "15 — Rollreffanlagen und Furler",
                "status": "implemented",
                "entries": 4,
                "details": [
                    "15_01 Rollreffanlagen Grundlagen",
                    "15_02 Grosssegel-Rollreff",
                    "15_03 Furler Hersteller",
                    "15_04 Rollreffanlagen Wartung und Troubleshooting",
                ],
            },
            "22.16_segel": {
                "title": "16 — Segel",
                "status": "implemented",
                "entries": 8,
                "details": [
                    "16_01 Segel Grundlagen und Typen",
                    "16_02 Großsegel",
                    "16_03 Vorsegel (Genua/Fock/Sturmfock)",
                    "16_04 Spinnaker und Gennaker",
                    "16_05 Segeltuch und Materialien",
                    "16_06 Segelmacher und Hersteller",
                    "16_07 Segelschnitt und Trimm",
                    "16_08 Segel Wartung und Reparatur",
                ],
            },
            "22.17_anker_kette": {
                "title": "17 — Anker und Kette",
                "status": "implemented",
                "entries": 8,
                "details": [
                    "17_01 Ankertypen und Grundlagen",
                    "17_02 Ankerketten",
                    "17_03 Ankerwinden",
                    "17_04 Ankergeschirr und Zubehör",
                    "17_05 Snubber und Kettenstopper",
                    "17_06 Ankertechniken und Manöver",
                    "17_07 Ankerbucht und Design",
                    "17_08 Anker Wartung und Troubleshooting",
                ],
            },
            "22.18_motoren_antrieb": {
                "title": "18 — Motoren und Antrieb",
                "status": "implemented",
                "entries": 14,
                "details": [
                    "18_01 Marine-Diesel Grundlagen",
                    "18_02 Yanmar Motoren",
                    "18_03 Volvo Penta",
                    "18_04 Beta, Nanni, Vetus",
                    "18_05 Kühlsystem",
                    "18_06 Abgasanlage",
                    "18_07 Getriebe und Saildrive",
                    "18_08 Wellenanlage",
                    "18_09 Propeller",
                    "18_10 Motorlager und Einbau",
                    "18_11 Elektroantrieb",
                    "18_12 Bugstrahlruder",
                    "18_13 Motor Wartung",
                    "18_14 Motor Troubleshooting",
                ],
            },
            "22.19_kraftstoffsystem": {
                "title": "19 — Kraftstoffsystem",
                "status": "implemented",
                "entries": 4,
                "details": [
                    "19_01 Kraftstofftanks Grundlagen",
                    "19_02 Kraftstofffilter und Abscheider",
                    "19_03 Kraftstoffleitungen und Armaturen",
                    "19_04 Kraftstoffsystem Wartung und Troubleshooting",
                ],
            },
            "22.20_steuerung": {
                "title": "20 — Steuerung",
                "status": "implemented",
                "entries": 6,
                "details": [
                    "20_01 Steuerung Grundlagen",
                    "20_02 Hydraulische Steuerung",
                    "20_03 Ruderanlage und Lager",
                    "20_04 Steuerräder und Pinnen",
                    "20_05 Notsteuerung",
                    "20_06 Steuerung Wartung und Troubleshooting",
                ],
            },
            "22.21_autopilot": {
                "title": "21 — Autopilot",
                "status": "implemented",
                "entries": 5,
                "details": [
                    "21_01 Autopilot Grundlagen",
                    "21_02 Autopilot Hersteller-Vergleich",
                    "21_03 Windfahnen-Selbststeueranlage",
                    "21_04 Autopilot Installation und Kalibrierung",
                    "21_05 Autopilot Wartung und Troubleshooting",
                ],
            },
            "22.22_elektrik": {
                "title": "22 — Elektrik",
                "status": "implemented",
                "entries": 12,
                "details": [
                    "22_01 Elektrik Grundlagen",
                    "22_02 Batterien",
                    "22_03 Kabel und Leitungen",
                    "22_04 Ladegeräte und Laderegler",
                    "22_05 Solaranlage",
                    "22_06 Windgenerator",
                    "22_07 Wechselrichter und Landstrom",
                    "22_08 Schalttafeln und Sicherungen",
                    "22_09 Beleuchtung",
                    "22_10 Galvanische Korrosion und Blitzschutz",
                    "22_11 Generatoren",
                    "22_12 Elektrik Wartung und Troubleshooting",
                ],
            },
            "22.23_elektronik_navigation": {
                "title": "23 — Elektronik/Navigation",
                "status": "implemented",
                "entries": 8,
                "details": [
                    "23_01 Navigation Grundlagen",
                    "23_02 Kartenplotter und MFD",
                    "23_03 Radar und AIS",
                    "23_04 UKW-Funk und Kommunikation",
                    "23_05 Instrumente und Sensoren",
                    "23_06 NMEA 2000 Vernetzung",
                    "23_07 Antennen und Installation",
                    "23_08 Elektronik Wartung und Troubleshooting",
                ],
            },
            "22.24_sanitaer": {
                "title": "24 — Sanitär",
                "status": "implemented",
                "entries": 7,
                "details": [
                    "24_01 Bordtoiletten",
                    "24_02 Fäkalientanks",
                    "24_03 Frischwassersystem",
                    "24_04 Warmwasserbereiter",
                    "24_05 Pumpen Sanitär",
                    "24_06 Rohrleitungen und Armaturen Sanitär",
                    "24_07 Sanitär Wartung",
                ],
            },
            "22.25_gas_und_kochen": {
                "title": "25 — Gas und Kochen",
                "status": "implemented",
                "entries": 4,
                "details": [
                    "25_01 Gasanlage Grundlagen",
                    "25_02 Kocher und Backofen",
                    "25_03 Gasflaschenlagerung",
                    "25_04 Gas Sicherheit und Wartung",
                ],
            },
            "22.26_heizung_klima": {
                "title": "26 — Heizung/Klima",
                "status": "implemented",
                "entries": 6,
                "details": [
                    "26_01 Heizung Grundlagen",
                    "26_02 Diesel-Heizung",
                    "26_03 Klimaanlage",
                    "26_04 Isolation und Lüftung",
                    "26_05 Wärmepumpe",
                    "26_06 Heizung/Klima Wartung",
                ],
            },
            "22.27_persenning": {
                "title": "27 — Persenning",
                "status": "implemented",
                "entries": 6,
                "details": [
                    "27_01 Persenning Grundlagen",
                    "27_02 Bimini und Sprayhood",
                    "27_03 Cockpitverdecke",
                    "27_04 Winterplanen",
                    "27_05 Sonnensegel und Polster",
                    "27_06 Persenning Wartung",
                ],
            },
            "22.28_interieur_materialien": {
                "title": "28 — Interieur-Materialien",
                "status": "implemented",
                "entries": 7,
                "details": [
                    "28_01 Interieur Holz",
                    "28_02 Polstermaterialien",
                    "28_03 Bodenbeläge",
                    "28_04 Oberflächen und Lacke",
                    "28_05 Beschläge Interieur",
                    "28_06 Countertops und Arbeitsflächen",
                    "28_07 Interieur Wartung",
                ],
            },
            "22.29_sicherheitsausruestung": {
                "title": "29 — Sicherheitsausrüstung",
                "status": "implemented",
                "entries": 9,
                "details": [
                    "29_01 Rettungswesten",
                    "29_02 Rettungsinseln",
                    "29_03 Sicherheitsleinen",
                    "29_04 Signalmittel",
                    "29_05 Feuerlöscheinrichtungen",
                    "29_06 Erste Hilfe",
                    "29_07 Mann über Bord",
                    "29_08 Lenzpumpen und Notausrüstung",
                    "29_09 Sicherheit Wartung",
                ],
            },
            "22.30_trailer_transport": {
                "title": "30 — Trailer/Transport",
                "status": "implemented",
                "entries": 3,
                "details": [
                    "30_01 Bootstrailer",
                    "30_02 Kranarbeiten und Slippen",
                    "30_03 Transport und Lagerung",
                ],
            },
            "22.31_design_konstruktion": {
                "title": "31 — Design/Konstruktion",
                "status": "implemented",
                "entries": 14,
                "details": [
                    "31_01 Rumpfformen",
                    "31_02 Hydrostatik",
                    "31_03 Strukturberechnung",
                    "31_04 Rigg-Dimensionierung",
                    "31_05 Gewichtsmanagement",
                    "31_06 Propellerauslegung",
                    "31_07 Tankplanung",
                    "31_08 Kielkonstruktion",
                    "31_09 Ruder-Design",
                    "31_10 Deck-Layout",
                    "31_11 Interieur-Layout",
                    "31_12 Laminatplan",
                    "31_13 CAD-Tools",
                    "31_14 Design/Konstruktion Wartung",
                ],
            },
            "22.32_zusatz_materialien": {
                "title": "04+ — Zusätzliche Materialien",
                "status": "implemented",
                "entries": 6,
                "details": [
                    "04_xx Honeycomb Core", "04_xx SORIC/Lantor",
                    "04_xx Vakuuminfusions-Zubehör", "04_xx Trennmittel",
                    "04_xx GFK-Reparatur-Sets",
                ],
            },
            "22.33_designsprachen_stile": {
                "title": "32 — Designsprachen und Stile",
                "status": "implemented",
                "entries": 9,
                "details": [
                    "32_01 Serien-Segelcruiser (Beneteau, Jeanneau, Bavaria, Hanse, Dufour, Elan, Dehler, Catalina)",
                    "32_02 Blauwasser-Cruiser (Hallberg-Rassy, Najad, Malö, Oyster, Amel, Contest, Swan, Hinckley, Morris …)",
                    "32_03 Performance-Cruiser + Rating-Rule-Evolution (X-Yachts, J/Boats, Grand Soleil, Solaris, First, ClubSwan)",
                    "32_04 Multihulls/Katamarane (Lagoon, Fountaine Pajot, Leopard, Bali, Catana, Outremer, Gunboat, HH, Sunreef)",
                    "32_05 Motor-Sportcruiser (Sunseeker, Princess, Fairline, Azimut, Ferretti, Riva, Pershing, Galeon, Wally)",
                    "32_06 Trawler/Explorer/Downeast (Nordhavn, Grand Banks, Fleming, Kadey-Krogen, Hinckley, Sabre, MJM)",
                    "32_07 Superyachten & Studios (Feadship, Lürssen, Amels, Heesen, Benetti, Sanlorenzo; Øino, Winch, Disdale …)",
                    "32_08 Epochen/Taxonomie/Designer (7 Epochen, 13 Stil-Kategorien, Design-Vokabular, legendäre Designer)",
                    "32_09 Quer-Synthese: Design-Muster & Klassifikator-Signale (Pipeline-B-Cues, brand_dna-Priors)",
                ],
            },
        },
    },
}
