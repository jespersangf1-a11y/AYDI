"""
AYDI Rumpfkonstruktion — Tiefenwissen
Exhaustive technical knowledge on GFK hull construction: resins, fibers,
gelcoat, core materials, construction methods, and hull-deck joints.

Author: AYDI Research Team
Version: 1.0
"""

from typing import Dict, Any


RESIN_DATABASE: Dict[str, Any] = {
    "key_de": "Harz-Datenbank",
    "description": "Comprehensive resin type comparison for marine GFK construction",
    "orthophthalic_polyester": {
        "key_de": "Orthophthal-Polyester",
        "chemical_basis": "Polykondensation von Orthophthalsäureanhydrid, Maleinsäureanhydrid und Glykolen",
        "curing": {
            "catalyst": "MEKP (Methylethylketonperoxid) 1-2 Vol.%",
            "mechanism": "Radikalische Polymerisation — Styrol vernetzt ungesättigte Doppelbindungen",
            "pot_life_20C": "15-25 Minuten",
            "full_cure": "24-48 Stunden bei 20°C",
        },
        "mechanical_properties": {
            "tensile_strength_MPa": "60-80",
            "flexural_modulus_GPa": "2-4",
            "elongation_percent": "1-2",
            "description_de": "Schwächstes und sprödestes Harz im Bootsbau"
        },
        "osmosis_mechanism": {
            "description_de": "Anfälligster Harztyp für Osmose durch hohe Ester-Dichte",
            "step_1": "Wasser diffundiert durch Mikroporen im Gelcoat",
            "step_2": "Hydrolyse der Ester-Bindungen (C-O-C=O) im Polyester-Rückgrat",
            "step_3": "Entstehung saurer Nebenprodukte: Essigsäure, Glykol",
            "step_4": "Osmotischer Gradient: hohe Säurekonzentration zieht mehr Wasser an",
            "step_5": "Osmotischer Druck trennt Gelcoat vom Laminat — domförmige Blasen entstehen",
            "step_6": "Blasenflüssigkeit riecht nach Essig (Essigsäure)",
            "self_reinforcing": "Hydrolyse-Nebenprodukte greifen verbleibende Ester-Gruppen an — beschleunigend",
            "onset_years": "10-15 Jahre bei Dauergewässerung",
        },
        "historical_use": {
            "standard_era": "1960er bis späte 1980er Jahre",
            "reason": "Günstig, leicht verfügbar, einfach zu verarbeiten",
            "manufacturers_using": "Praktisch alle Serienwerften bis ca. 1988",
            "current_use": "Nur noch in Nicht-Marine-Anwendungen"
        },
    },
    "isophthalic_polyester": {
        "key_de": "Isophthal-Polyester",
        "molecular_difference": {
            "description_de": "Isophthalsäure (meta-substituierter Benzolring) statt Orthophthalsäure (ortho-substituiert)",
            "effects": [
                "Lineareres Molekül-Rückgrat mit weniger sterischer Hinderung",
                "Bessere Kettenausrichtung und höhere Umsetzungsraten",
                "Mehr Aromaten in der Struktur (42-50% Styrolgehalt vs. 35-45% bei Ortho)",
                "Engeres, kompakteres ausgehärtetes Polymernetzwerk"
            ]
        },
        "improvement_over_ortho": {
            "tensile_improvement": "+20% gegenüber Orthophthal",
            "flexural_improvement": "+10%",
            "water_resistance": "Deutlich besser durch engere Molekülpackung",
            "osmosis_onset_years": "15-20 Jahre mit Barrier-Coat"
        },
        "cost_premium": "+10-20% gegenüber Orthophthal",
        "manufacturer_adoption": {
            "island_packet_yachts": "Proprietäre Isophthal-Mischung mit Vinylester-Gelcoat, 10 Jahre Osmose-Garantie",
            "timeline": "Späte 1980er bis frühe 1990er Jahre als Standard",
            "current_standard": "Alle Serienwerften seit 1995 für mittlere und große Boote"
        }
    },
    "vinylester": {
        "key_de": "Vinylester",
        "chemical_basis": {
            "description_de": "Epoxid-Acryl-Hybridharz mit deutlich weniger hydrolysierbaren Ester-Gruppen",
            "mechanism": "Terminale Vinylgruppen statt durchgehender Ester-Ketten",
            "hydrolysis_resistance": "ca. 300× besser als Polyester",
        },
        "mechanical_properties": {
            "tensile_strength_MPa": "70-105",
            "tensile_modulus_GPa": "3.5",
            "water_absorption_24h_25C": "0.17%",
            "water_absorption_2h_100C": "0.59%",
            "shrinkage": "Geringer als Polyester — weniger Spannungsrisse"
        },
        "barrier_vs_full_hull": {
            "barrier_layer": {
                "description_de": "Erste 2-3 Lagen unter Gelcoat als Osmose-Schutz",
                "inner_laminate": "Polyester (günstiger)",
                "cost_benefit": "Optimales Kosten-Leistungs-Verhältnis",
                "efficacy": "Reduziert Osmose auf 25-35 Jahre bei Dauerbelastung"
            },
            "full_hull": {
                "description_de": "Durchgehend Vinylester im gesamten Laminat",
                "expected_life": "40+ Jahre osmosefrei",
                "cost_premium": "30-50% höher als Polyester-Sandwich"
            }
        },
        "major_manufacturer_adoption": {
            "jeanneau": "Sun Odyssey Serie ab 1995: erste CSM-Lage Vinylester, Rest Polyester",
            "hanse_yachts": "Hanse 342+ ab 1998: erste äußere Lagen Vinylester Barriere",
            "dufour_yachts": "Atoll und Astrophe ab 2000: Vinylester in Außenlagen mit PVC-Sandwich",
            "bavaria_yachtbau": "Handlaminiertes GFK-Sandwich mit Vinylester in obersten 3 Lagen",
            "beneteau": "Proprietäre Barrierebeschichtung (Cyclone-Harz), Details begrenzt",
            "lagoon_catamarans": "Multi-ply mit Vinylester outer barrier seit 2005 Standard"
        },
        "processing_characteristics": {
            "cure_speed": "Langsamer als Polyester (20-30 min Topfzeit vs. 15-20 min)",
            "advantage": "Langsamere Aushärtung → kompaktere Molekülstruktur → höhere Umsetzungsraten",
            "temperature_sensitivity": "Ähnlich wie Polyester, aber enger toleriert (±3°C optimal)",
            "cost_premium": "+50-100% gegenüber Standard-Polyester"
        }
    },
    "epoxy": {
        "key_de": "Epoxid-Harz",
        "chemical_basis": {
            "description_de": "Ether- und Hydroxylbindungen statt Ester-Bindungen",
            "key_advantage": "Ether-Gruppen (C-O-C) sind NICHT hydrolysierbar — fundamentale Wasserbeständigkeit",
            "network": "Dichtes dreidimensionales vernetztes Netzwerk mit kleinsten Hohlräumen"
        },
        "strength_comparison": {
            "tensile_vs_polyester": "Ca. 2× (nicht 3×!) Zugfestigkeit und Modul im Vergleich zu Polyester",
            "elongation_percent": "3.5-4.5% vs. 1-2% bei Polyester",
            "adhesion": "Überlegene Klebkraft gegenüber Polyester-Laminaten",
            "modulus_GPa": "4.5-5.5 (vs. 3.5 Vinylester, 2-3 Polyester)"
        },
        "why_not_complete_hulls": [
            "Kosten: 3-4× teurer als Polyester (150-250 €/kg vs. 50-80 €/kg)",
            "Verarbeitungskomplexität: präzise Temperaturkontrolle ±3°C, Topfzeit 20-45 min, Aminblüte-Vermeidung",
            "Sprödigkeit bei großer Dicke und thermischen Wechselbelastungen über mehrere Jahre",
            "Produktionsgeschwindigkeit: inkompatibel mit Hochvolumen-Serienfertigung (4-6 Boote/Monat gefordert)",
            "Infrastruktur: Werften haben Polyester-Equipment, Epoxid erfordert Investitionen in Lagertanks",
            "Haltbarkeit des Härters: Begrenzte Lagerung (12-18 Monate vs. 24+ Monate MEKP)"
        ],
        "as_barrier_coat": {
            "products": "WEST SYSTEM 105/205/206/207/209, Sika Sikadur 330, 3M DP460, Hexcel HexPly F369",
            "layer_count": "2-3 Schichten wet-on-wet (0.3-0.5 mm pro Lage)",
            "substrate_preparation": "Schleifen 80-120 Korn, reinigen mit Aceton, trocknen (Taupunkt <3°C)",
            "bond_type": "Nur mechanische Bindung auf Polyester (keine chemische Vernetzung!)",
            "cure_time": "7-14 Tage für volle Endfestigkeit, 80°C Post-Cure empfohlen",
            "adhesion_strength": "8-12 MPa auf feuchtem Polyester"
        },
        "uv_sensitivity": {
            "description_de": "Standard-Epoxid degradiert unter UV-Strahlung ohne Schutzschicht",
            "yellowing_rate": "Nach 6-12 Monaten outdoor sichtbar",
            "protection": "Zwingend Deckschicht (Lack, Gelcoat, UV-Folie)",
            "special_products": "MarineGuard 8000 mit UV-Absorbern und HALS (Hindered Amine Light Stabilizer)",
            "topcoat_options": "2K-Polyurethane (Awlcraft, Awl-Grip), Polysiloxane (Interthane)"
        }
    },
    "processing_errors": {
        "key_de": "Harz-Verarbeitungsfehler und Qualitätsdefekte",
        "too_much_hardener": {
            "exotherm_peak": "Spitzentemperaturen über 250°C in dicken Bereichen (5-10 cm Masse)",
            "brittleness": "Extrem spröde, Bruchdehnungung unter 0.5% (normal 1-2%)",
            "visible_defects": ["Weiße Schaum/Blasen im ausgehärteten Laminat", "Spannungsrisse radial vom Kern", "Verzug und Dimensionsinstabilität ±2-3 mm"],
            "microcracking_mechanism": "Mikrorisse entstehen bei Gelierung durch Schrumpfung von 5-8%, thermische Wechsel propagieren diese zu Makrorissen",
            "consequence": "Strukturelle Versagbarkeit unter Last nach 2-5 Jahren Eigenlastbiegung"
        },
        "too_little_hardener": {
            "symptoms": "Harz bleibt klebrig, klebt nach 48h noch an Fingern, härtet nicht aus",
            "catalyst_shelf_life": "MEKP: 12-24 Monate Haltbarkeit bei 5-25°C, altes Material versagt exponentiell",
            "detection": "Viskosität sinkt nicht, Topfzeit wird unrealistisch lang (>60 min)",
            "remedy": "Gesamte Partie entfernen, frisch gemischtes Material mit neuem Katalysator auftragen"
        },
        "temperature_effects": {
            "minimum_cure_C": "10°C absolute Untergrenze",
            "optimal_range_C": "15-27°C für marine GFK",
            "below_10C": "Stark beeinträchtigte Aushärtung, Styrol entweicht ohne Vernetzung zu erfolgen",
            "rule_of_ten": "Jede 10°C Temperaturabnahme verdoppelt die Topfzeit (15 min → 30 min → 60 min)",
            "rule_reverse": "Jede 10°C Temperaturzunahme über 25°C halbiert die Topfzeit und erhöht Exotherm",
            "winter_production": "Werften mit Beheizung >15°C und Luftaustausch; unbeheiztes Handwerk qualitätsbelastet"
        },
        "amine_blush_epoxy": {
            "description_de": "Aminblüte: Amine reagieren mit CO2 und Feuchtigkeit der Luft zu Ammonium-Carbonaten",
            "appearance": "Klebrig, ölig, wachsartig oder kristallin weiß/grau auf der Oberfläche, matter Glanz",
            "chemical_effects": ["Reduziert Oberflächenglanz um 20-40 % unmittelbar", "Verschlechtert chemische Beständigkeit gegen Laugen", "Epoxid bleibt teilweise unausgehärtet in Oberflächenschicht"],
            "prevention": "Temperatur mindestens 3°C über Taupunkt während Auftrag und Aushärtung",
            "critical_conditions": "T <10°C UND Luftfeuchtigkeit >70% oder Oberflächentemperatur <5°C",
            "remedy": "Mit Essigwasser abwischen, nachpolieren, Topcoat ggf. erneuern"
        },
        "styrene_emission_control": {
            "environmental_limit": "EU VOC-Direktive: max. 500 g/L Styrol-Gehalt seit 2004",
            "worker_exposure": "MAK-Wert Deutschland: 100 ppm (ca. 420 mg/m³) Schicht-Grenzwert",
            "reduction_methods": ["Vakuuminfusion statt Handlaminat (60% weniger Emissionen)", "NP/NPG Low-Styrene-Harze", "Belüftung 10-20 Luftwechsel/Stunde"],
            "uv_inhibition": "Low-Styrene-Harze benötigen UV-Stabilisierung gegen Vergilbung"
        }
    }
}


FIBER_DATABASE: Dict[str, Any] = {
    "key_de": "Faser-Datenbank",
    "description": "Complete fiber reinforcement reference for marine GFK construction",
    "e_glass": {
        "key_de": "E-Glas (Elektronenglas)",
        "chemical_composition": "SiO2 52-57%, Al2O3 12-16%, CaO 17-20%, B2O3 7-10%, MgO <4%, Fe2O3 <1%",
        "mechanical_properties": {
            "tensile_strength_MPa": "2400-3500",
            "tensile_modulus_GPa": "70-80",
            "elongation_percent": "2-3",
            "density_g_cm3": "2.55-2.58",
            "thermal_expansion_10_6_K": "5-6"
        },
        "advantages": [
            "Kosteneffektiv: 2-3 €/kg Roving, 4-6 €/kg CSM (vs. S-Glas 8-12 €/kg)",
            "Gute Haftung zu Polyester und Epoxid",
            "Ausreichende Festigkeit für Bootsrümpfe bis 20m",
            "Hohe Verfügbarkeit, Lagerbestände weltweit"
        ],
        "fabric_types": {
            "csm_chopped_strand_mat": {
                "key_de": "Gehackte Strangmatte",
                "basis": "Zufällig ausgerichtete E-Glas-Stränge (Fasern), gebunden mit Polyesterharz",
                "thickness_mm": "0.5-2.0",
                "weight_gsm": "300-900 g/m²",
                "applications": ["Erste Schicht (Gelcoat-Haftung)", "Spachtelschichten", "Formgebung"],
                "resin_uptake": "60-70% des Laminatgewichts ist Harz (schwach)",
                "disadvantage": "Längsfestigkeit nur 40-50% der Querfestigkeit",
                "typical_use_sequence": "Gelcoat (0.5 mm) + CSM 450g/m² (Barriere & Haftung)"
            },
            "roving_woven": {
                "key_de": "Gewebe Rovingstoff",
                "basis": "Parallel liegende Faser-Rovings in Kette und Schuss verwebt",
                "typical_weaves": ["Plain (1x1)", "Twill (2x2)", "Satin (4x1 oder 8x1)"],
                "weight_gsm": "200-600 g/m²",
                "resin_uptake": "35-45% Harz (faserreich)",
                "tensile_strength_increase": "40-60% höher als CSM gleichen Gewichts",
                "application": "Hauptstruktur des Laminats (nach CSM)",
                "fiber_orientation": "0°/90° (Kette/Schuss) — biaxial symmetrisch",
                "typical_schedule": "CSM 450g → Roving 600g biaxial → Roving 600g (0/90) → CSM 450g"
            },
            "biaxial_fabric": {
                "key_de": "Biaxiales Gewebe",
                "composition": "±45° oder 0°/90° Ausrichtung in einem Stoff",
                "weight_gsm": "300-600 g/m²",
                "typical_angles": "±45° für Torsion/Scherung, 0°/90° für Längs-/Querlast",
                "applications": ["Flanken unter Segellast", "Hull-Deck-Übergang", "Spantverbindungen"],
                "advantage": "Isotrope Eigenschaften in der Ebene (keine Schwächungsrichtung)"
            },
            "triaxial_fabric": {
                "key_de": "Triaxiales Gewebe",
                "composition": "0°, +45°, -45° in einem Stoff (häufig mit +60°, -60°)",
                "weight_gsm": "400-750 g/m²",
                "applications": ["Hochbelastete Strukturen", "Mast-Schuh-Verbindung", "Kielkutter-Rümpfe"],
                "advantage": "Gleichmäßige Festigkeitsverteilung über alle Richtungen",
                "cost_premium": "+15-20% vs. biaxial"
            },
            "unidirectional_ud": {
                "key_de": "Unidirektionales Rovinggewebe",
                "composition": "Alle Fasern in eine Richtung (0°) mit minimaler Bindung",
                "weight_gsm": "300-1200 g/m²",
                "tensile_strength": "+80% vs. multiaxiales Gewebe (höhere Faserbeladung 55-65%)",
                "applications": ["Unterstützung für Längslasten", "Mast-Partner-Struktur"],
                "limitation": "Sehr schwach in Transversalrichtung (senkrecht zu Fasern)",
                "typical_use": "Immer kombiniert mit ±45° oder CSM-Schichten"
            }
        },
        "typical_laminate_schedule_30ft_racer": {
            "description_de": "Standard GFK-Rumpf 30ft Rennboot mit E-Glas, handlaminiert",
            "stack_from_outside": [
                "Gelcoat NPG 0.5-0.8 mm",
                "CSM 450 g/m² (Haftung, Barriere)",
                "Roving 600 g/m² 0/90 (Längs- und Querfestigkeit)",
                "Roving 600 g/m² ±45 (Torsion, Scherung)",
                "Roving 600 g/m² 0/90 (Hauptlast)",
                "CSM 300 g/m² (Innenschicht, Rauheit)",
            ],
            "total_thickness_mm": "4.5-6.5 mm ohne Kern, 30-35 mm mit Sandwich",
            "dry_weight_kg": "22-28 kg/m² Rumpfoberfläche",
            "wet_weight_with_resin": "60-75 kg/m² (55-65% Harz in Hand-Laminat)",
            "bending_stiffness": "EI ≈ 150-200 Nm² bei 1 m Spannweite"
        }
    },
    "s_glass": {
        "key_de": "S-Glas (Hochfest-Glas)",
        "chemical_composition": "SiO2 65%, Al2O3 25%, MgO 10% (keine Borsäure wie E-Glas)",
        "mechanical_properties": {
            "tensile_strength_MPa": "3500-4600",
            "tensile_modulus_GPa": "85-92",
            "elongation_percent": "2-3",
            "density_g_cm3": "2.48-2.52",
            "improvement_vs_e_glass": "+20-30% Festigkeit, +15-20% Modul"
        },
        "cost_premium": "+35-50% vs. E-Glas (8-12 €/kg Roving)",
        "applications": [
            "Hochleistungs-Rennboote (VO70, Mini Transat)",
            "Großyachten über 25m (Hanse AC-Boote)",
            "Strukturen mit extremer Last (Mast-Struktur, Decklager)"
        ],
        "manufacturer_use": {
            "hanse_yachts": "S-Glas in Kielbereich und Spantenverbindungen, E-Glas im Hauptlaminat",
            "dufour": "Oberflächen mit S-Glas, Gesamthull mit E-Glas Sandwich",
            "jeanneau": "S-Glas nur in Performance-Linien (Sun Odyssey 45+ DS)"
        },
        "disadvantage": [
            "Chemische Beständigkeit gegen Säuren/Laugen schlechter als E-Glas",
            "Schwieriger zu verarbeiten (höhere Viskosität)",
            "Lagerhaltung teuer — schneller Verbrauch unrentabel"
        ]
    },
    "carbon_fiber": {
        "key_de": "Kohlenstofffaser",
        "mechanical_properties": {
            "tensile_strength_MPa": "3500-7000 (abhängig von Qualität)",
            "tensile_modulus_GPa": "230-250",
            "density_g_cm3": "1.60",
            "elongation_percent": "1-2",
            "strength_to_weight": "2.5-3× besser als E-Glas"
        },
        "galvanic_problem": {
            "description_de": "Kohlenstoff ist deutlich edler als Stahl, Aluminium und sogar Platin (Standardpotential -0.2V)",
            "electrochemical_series_ranking": "C/-0.2V < Cu/+0.34V < Ag/+0.8V (Kohlenstoff am negativsten)",
            "galvanic_couples": {
                "carbon_steel": "Potentialdifferenz 0.2-0.3V — rapide Stahl-Korrosion um C-Fasern",
                "carbon_aluminum": "Potentialdifferenz 1.5-1.7V — Aluminium korrodiert schnell (weiße Oxid-Ausblühung)",
                "carbon_stainless_316": "Potentialdifferenz 0.4-0.6V — auch 316 SS wird anodisch gelöst bei Stromanfall"
            },
            "mechanism": "Feuchter Polyester verbindet C und Metall → Galvani-Element → Strom fließt → Metall wird anodisch oxidiert",
            "consequence": "Strukturelle Versagung bei Metall-Hardware in C-Strukturen nach 3-5 Jahren",
            "prevention_methods": [
                "Isolierschicht (Epoxid-Barriere) um C-Fasern, vor Metallkontakt",
                "Nicht-metallische Hardware (Kunststoff-Scheiben, Nylon-Spacer, GFK-Scheiben)",
                "Kathodischer Schutz (Anoden) nur in salzwasser — Süßwasser problematisch",
                "Regelmäßige Wartung: jährlich Sichtprüfung, Paint-Refresh um Korrosionsstellen"
            ]
        },
        "bvid_delamination": {
            "key_de": "BVID (Barely Visible Impact Damage) — Delaminierung nach Stoß",
            "problem": "C-Faserverbunde sind sprödbruchempfindlich, Stoß erzeugt innere Delaminierung ohne Oberflächenschaden",
            "detection": "Sichtprüfung unzuverlässig (Delle <1 mm, aber Delaminierung im Laminat 50 mm²)",
            "inspection_method": "Ultraschall-Scanning (UT) oder Thermografie nach Stoß",
            "failure_risk": "Kompression nach Impact kann Restfestigkeit um 30-50% reduzieren",
            "marine_consequence": "Bootsbeschädigung nach Grundberührung nicht offensichtlich → verursacht Strukturversagen unter Segelbelastung nach Wochen/Monaten"
        },
        "repair_challenges": {
            "resin_system_compatibility": "Epoxid-Carbon erfordert Epoxid-Reparatur (nicht Polyester); Polyester-Carbon erfordert Polyester",
            "fiber_volume_fraction": "Schwer zu erreichenin Reparatur: original 55-60%, Reparatur 40-50%",
            "mechanical_properties_after": "Reparierte Stelle nur 70-80% Originalfestigkeit",
            "cost_impact": "Reparatur kostet 2-3× das Material (Arbeit, Prüfung, Finishing)"
        },
        "commercial_use": {
            "rare_in_serial_yachts": "Nur in Exklusiv-Rennbooten oder als Kosteneinsparung (Rigg, nicht Rumpf)",
            "hanse_ac45s": "AC45S (Cup-Yacht) mit Carbon-Rumpf und Sandwich-Kern (PVC)",
            "lagoon_catamaran": "Lagoon 450 SporTopTM mit Carbon-Unterstützungsstruktur (keine Vollstruktur)",
            "production_boats_rare": "< 0.1% der Serienyachtproduktion wegen Kosten (C-Faserrovingpre-peg 80-150 €/kg)"
        }
    },
    "aramid_kevlar": {
        "key_de": "Aramid-Faser (Kevlar, Twaron)",
        "mechanical_properties": {
            "tensile_strength_MPa": "2800-3600",
            "tensile_modulus_GPa": "80-130",
            "density_g_cm3": "1.44",
            "elongation_percent": "2-4",
            "characteristic": "Hoher Modul, geringe Dichte — aber geringere Druckfestigkeit als Glas"
        },
        "uv_degradation": {
            "description_de": "Aramid ist UV-empfindlich, besonders im Prepreg (Polyester-Matrix)",
            "yellow_exposure": "Gelbfärbung nach 3-6 Monaten outdoor ohne UV-Schutz",
            "strength_loss": "10-20% Festigkeitsverlust pro Jahr unter direkter Sonneneinstrahlung",
            "protection": "Zwingend Lack oder Gelcoat-Schutz (>0.3 mm)",
            "consequence": "Kaum einsetzbar im Boot-Außenlaminat; evtl. als innere Struktur (Spanten)"
        },
        "matrix_compatibility": {
            "epoxy_systems": "Aramid in Epoxid-Matrix: +30% Festigkeit, volle UV-Lebensdauer mit Topcoat",
            "polyester_systems": "Aramid-Polyester: Problematisch, da Polyester Aramid gelblich verfärbt + UV-Abbau"
        },
        "applications": [
            "Spanten-Verstärkung (innen, UV-geschützt)",
            "Stoßschutz-Laminate (Decksübergang, Reling)",
            "Hochleistungs-Riggingfasern (Leine, nicht Boot-Struktur)"
        ]
    },
    "laminate_schedule_iso_12215": {
        "key_de": "ISO 12215 Rumpf-Dimensionierungsstandard",
        "standard_reference": "ISO 12215-5:2019 (Scantling Design Rules for Monohull Boats)",
        "scope": "Vergnügungsboote 2.5-24 m Länge",
        "design_values": {
            "water_pressure_kpa": "0.01 × (Tauchtiefe in mm)",
            "design_live_load": "50 kN/m² (Windlast + Manöver)",
            "safety_factor": "1.5 Material + 1.0 Form-Sicherheitsfaktor = Gesamt 1.5"
        },
        "typical_glass_content_schedule": {
            "small_boat_5m": {
                "description_de": "5m Polyester-GFK Segelboot",
                "stack": [
                    "Gelcoat NPG 0.6 mm (UV-Schutz)",
                    "CSM 300 g/m² + Isophthal Polyester (Haftung, Barriere)",
                    "Roving 450 g/m² 0/90° (Längs-/Querlast)",
                    "Roving 450 g/m² ±45° (Torsion)",
                    "Roving 450 g/m² 0/90° (Längslast)",
                    "CSM 200 g/m² (Innenseite)"
                ],
                "total_laminate_thickness_mm": "3.5-4.5 mm",
                "resin_content_percent": "60-65%",
                "fiber_content_percent": "35-40%"
            },
            "medium_boat_12m": {
                "description_de": "12m Polyester-GFK Motor-/Segelboot mit Sandwich-Kern",
                "stack": [
                    "Gelcoat NPG 0.7 mm",
                    "CSM 450 g/m² + Isophthal Polyester (Barriere)",
                    "Roving 600 g/m² 0/90° (Längs-/Querlast)",
                    "Roving 600 g/m² ±45° (Torsion, Scherung)",
                    "Roving 600 g/m² 0/90° (Längslast)",
                    "PVC-Schaum 40-60 mm (Kernmaterial) — siehe CORE_MATERIALS_DATABASE",
                    "Roving 600 g/m² 0/90° (Längslast)",
                    "Roving 600 g/m² ±45° (Torsion rückwärts)",
                    "Roving 600 g/m² 0/90° (Längslast)",
                    "CSM 300 g/m² (Innenseite)"
                ],
                "total_laminate_thickness_mm": "35-45 mm mit Kern",
                "fiber_weight_outside": "600-800 g/m²",
                "fiber_weight_inside": "400-600 g/m²",
                "core_weight_kg_m2": "2.5-4.0 kg/m² (abhängig Dichte und Dicke)"
            },
            "large_boat_20m": {
                "description_de": "20m Yacht mit Vinylester-Barriere und PVC-Sandwich",
                "outer_laminate_mpa": "Vinylester-Barriere 2-3 Lagen (1-1.5 mm)",
                "inner_stack": [
                    "Vinylester 0.5 mm (Barriere, Osmose-Schutz)",
                    "CSM 450 g/m² Vinylester (Haftung)",
                    "Roving 750 g/m² 0/90° Isophthal (Längs-/Querfestigkeit)",
                    "Roving 750 g/m² ±45° Isophthal (Torsion)",
                    "Roving 750 g/m² 0/90° Isophthal (Längslast)",
                    "PVC-Schaum 60-80 mm (Dichte 80 kg/m³)",
                    "Roving 750 g/m² 0/90° Isophthal (Längslast Innen)",
                    "Roving 750 g/m² ±45° Isophthal (Torsion Innen)",
                    "Roving 600 g/m² 0/90° Isophthal",
                    "CSM 300 g/m² Isophthal (Innenseite)"
                ],
                "total_laminat_thickness_mm": "60-75 mm",
                "specific_weight_hull_only_kg": "100-150 kg/m² Rumpfoberfläche (Struktur + Sandwich)"
            }
        },
        "bending_moment_calculation": {
            "formula_de": "Maximales Biegemoment: M = 0.1 × disp_tonnes × Lpp_meters",
            "example_12m_boat": {
                "displacement": 15,
                "lpp": 11,
                "bending_moment_kNm": "16.5 kNm",
                "required_section_modulus_cm3": "550-800 cm³ abhängig von Materialsicherheit"
            }
        }
    }
}


GELCOAT_DATABASE: Dict[str, Any] = {
    "key_de": "Gelcoat-Datenbank",
    "description": "Comprehensive gelcoat composition, application, and aging knowledge",
    "composition": {
        "key_de": "Zusammensetzung",
        "base_resin": {
            "description_de": "Isophthal oder Orthophthal Polyester, identisch wie Rumpf-Harze",
            "percentage": "35-50 Gew.-%",
            "function": "Träger für Pigmente und Additive"
        },
        "styrene_monomer": {
            "description_de": "Flüchtiges Verdünnungsmittel und Vernetzungsmittel",
            "percentage": "20-30 Gew.-%",
            "function": "Reduktion der Viskosität, Ermöglichung der radikalischen Polymerisation",
            "emission_issue": "EU VOC <500 g/L Limit — Low-Styrene Gelcoate ~400 g/L"
        },
        "pigments": {
            "description_de": "Farbstoffe und Deckmittel",
            "percentage": "10-20 Gew.-%",
            "types": [
                "Titandioxide TiO2 (Weiß, UV-Absorber, 5-15%)",
                "Eisenoxide (Rot, Braun, Gelb 1-5%)",
                "Phthalocyanine (Blau, Grün 0.5-2%)",
                "Metallische Pulver (Silber, Gold, Kupfer 1-3%)"
            ],
            "effect_on_uv": "Dunklere Farben stärker UV-absorbierend, Weiß reflektierend"
        },
        "additives_thixotropic": {
            "description_de": "Thixotrope Agenzien verhindern Fließen auf vertikalen Flächen",
            "typical_material": "Hydrophobe Silica (kieselsäure) oder Bentonitklay",
            "percentage": "2-5 Gew.-%",
            "mechanism": "Wasserstoff-Bindung bildet 3D-Struktur bei Ruhe, bricht bei Scherung"
        },
        "additives_other": {
            "uv_absorbers": "Benzotriazol-Derivate, 1-3 Gew.-%",
            "light_stabilizers": "HALS (Hindered Amine Light Stabilizers), 0.5-2 Gew.-%",
            "impact_modifiers": "Kautschuk-Nanopartikel oder Polybutadien, 2-5 Gew.-%"
        }
    },
    "thickness_specification": {
        "optimal_thickness_mm": "0.5-0.8 mm",
        "measurement_method": "Schichtdickenmesser (magnetoinduktiv), min. 5 Punkte pro m²",
        "problems_if_below_04mm": [
            "UV-Strahlung durchdringt Pigmente → schnelle Farbverlust",
            "Keine ausreichende Haftung durch Penetration in Glasfaser",
            "Blasenbildung durch Poreninnen bei Sonneneinstrahlung"
        ],
        "problems_if_above_1_5mm": [
            "Schrumpfungsrisse (bis zu 5% Volumen-Schrumpfung bei Aushärtung)",
            "Crazing — feinste Netzwerk von Rissen",
            "Längere Austrocknung → Wasserdampf-Einschluss",
            "Thermische Spannungen verstärkt (dickere Schicht = höhere Temperaturgradienten)"
        ],
        "typical_specification_iso": {
            "small_boats_under_7m": "0.5-0.6 mm",
            "medium_boats_7_15m": "0.6-0.8 mm",
            "large_yachts_15m_plus": "0.7-1.0 mm mit Strukturverstärkung"
        }
    },
    "iso_standards": {
        "key_de": "ISO-Gelcoat-Standards",
        "iso_2768": "ISO 2768-1 Polymerglas-Laminat — allgemeine Toleranzen",
        "iso_12215": "ISO 12215-5 Rumpf Scantling Design — Gelcoat-Anforderungen",
        "iso_4617": "ISO 4617 Oberflächenqualität nach Finish",
        "npg_certification": {
            "description_de": "NPG (National Pig Growers?) — eigentlich North Pacific Group oder NMMA (National Marine Manufacturers Association)",
            "requirement": "Gelcoat muss NPG 0440 oder äquivalent erfüllen",
            "specification_areas": ["Haftung auf GFK", "UV-Beständigkeit (2000 h ASTM G154)", "Widerstand gegen Osmose"]
        }
    },
    "aging_modes": {
        "crazing": {
            "description_de": "Feines Netzwerk paralleler Risse in der Gelcoat-Oberfläche",
            "cause": "Thermische Zyklierung (Sonne tagsüber +60°C, Nacht +10°C) → zyklische Spannung",
            "mechanism": "Oberflächenschicht schrumpft schneller als darunter liegende Schichten (UV + Temperatur)",
            "progression": "Beginnt nach 3-5 Jahren, bei dunklen Farben 2-3 Jahre",
            "severity_scale": [
                "Grad 1: Einzelne Risse <10 mm, nicht wahrnehmbar auf >2 m Distanz",
                "Grad 2: Netzwerk Risse sichtbar auf 1-2 m, kein Wassereintritt",
                "Grad 3: Großflächiges Netzwerk, Wasser kann eindringen (kritisch)"
            ],
            "water_ingress": "Crazing selbst nicht wasserdicht, Wasser penetriert über Netzwerk"
        },
        "chalking": {
            "description_de": "Oberflächenpulver durch UV-Degradation der Bindermittel",
            "appearance": "Kreidiges, weißlich/graulich Pulver auf dunkler Farbe",
            "cause": "UV bricht C-H und C-C Bindungen auf, Pigmente freigesetzt",
            "timeline": "Weiße Gelcoate: 8-12 Jahre, dunkle (Blau/Rot): 4-6 Jahre",
            "water_penetration": "Chalking selbst nicht wasserdicht — Wasser penetriert verfärbte Schicht",
            "testing": "Krepp-Papier-Test (ASTM D4214): Papier auf Oberfläche drücken, abheben und kontrollieren"
        },
        "orange_peel": {
            "description_de": "Rauhe Oberflächentextur ähnlich Orangenschale",
            "cause": "Zu schnelle Aushärtung ohne Oberflächensättigung oder falsche Sprüh-Viskosität",
            "timing": "Tritt unmittelbar nach Aushärtung auf (nicht später)",
            "remedy_polishing": "Mit 1000er Schleifpapier zu 2000er/3000er aufschleifen, dann polieren",
            "prevention": "Kontrolle Topfzeit (15-25 min), Sprühviskosität 18-22 sec Ford Cup, Temperatur 18-25°C"
        },
        "star_crazing": {
            "description_de": "Strahlenförmige Risse vom zentralen Punkt ausgehend",
            "cause": "Lokale Spannungskonzentration: harte Stelle, Fremdkörper, Kratzer unter Gelcoat",
            "pattern": "Risse sternförmig 5-15 cm Durchmesser",
            "water_ingress": "Direkte Eindringstelle für Wasser in das darunter liegende Laminat",
            "causation_examples": [
                "Sandkörnchen während Auftrag eingetrocknet",
                "Unsaubere Werkzeug hinterlässt Kratzer",
                "Unterschiedliche Härtung (Temperaturzone unter Wärmelamp)"
            ]
        },
        "stress_cracking": {
            "description_de": "Risse folgen Spannungsgradienten (nicht zufällig wie Crazing)",
            "locations": "Systematisch an Kanten, Spanten, Hardware-Befestigungen",
            "cause": "Strukturelle Last erzeugt Dehnung, Gelcoat ist brittle (Dehnung <2%)",
            "mechanism": "Hull biegt unter Segelbelastung 10-50 mm pro 10 m Spannweite → Gelcoat reißt",
            "consequence": "Wassereintritt an kritischen Strukturpunkten",
            "prevention": "Dickere Gelcoat an hochbelasteten Zonen, oder elastischerer Topcoat (2K-PU)"
        },
        "yellowing": {
            "description_de": "Farbverlust durch UV-Absorption und photochemischer Abbau",
            "white_gelcoat": "Minimal bis nicht wahrnehmbar nach 10+ Jahren",
            "blue_gelcoat": "Deutlich nach 5-7 Jahren, Farbton wird grünlich-dunkelblau",
            "red_gelcoat": "Nach 3-5 Jahren rötlicher Farbton wird orange/braun",
            "mechanism": "Chromophor (Farbzentren) in Pigmenten werden durch Photonen zerstört",
            "accelerated_by": "Hohe Temperatur (+60°C beschleunigt um Faktor 2), Salzspray, Verschmutzung"
        },
        "blistering_osmotic": {
            "description_de": "Domförmige Blasen unter Gelcoat nach Wasserlagerung",
            "cause": "Siehe RESIN_DATABASE — Osmose tritt auf wenn Polyester-Harz hydrolysierende Ester-Gruppen hat",
            "gelcoat_relation": "Gelcoat kann osmotische Blasen vermeiden, wenn Barriere-Funktion erfüllt (dicht, <0.5 mm Poren)",
            "symptom_timeline": "Sichtbar nach 5-10 Jahren Dauerbelastung im Süßwasser oder Brackwasser",
            "appearance": "Blasen 5-30 mm Durchmesser, gefüllt mit Säure (riecht nach Essig)"
        }
    },
    "repair_procedures": {
        "spot_repair_small_damage": {
            "description_de": "Reparatur kleiner Kratzer oder Dellen <50 mm²",
            "steps": [
                "Areal schleifen mit 120er Korn bis raue Oberfläche entsteht (5 mm Überstand)",
                "Reinigen mit Wasser, trocknen (min. 2h bei 20°C)",
                "Konkretes Gelcoat-Matching: Farbmuster vergleichen unter Tageslicht (nicht Kunstlicht)",
                "Gelcoat auftragen (Pinsel oder Stick), leichte Überwölbung (1-2 mm)",
                "Trocknung 24h bei 20°C",
                "Feinschleifen 400er → 800er → 1500er Körnung (Nassschliff)",
                "Polieren mit Rubbing Compound, dann Fine-Polish (3M Perfect-It oder äquivalent)"
            ],
            "color_matching_challenge": "Alterung der Original-Gelcoat ist unsichtbar, neue Partie hat andere UV-Stabilisierung",
            "visibility_after_fix": "Nach 6 Monaten können Unterschiede sichtbar werden (Rand-Effekt)",
            "remedy": "Großflächigere Reparatur bis zur Spantlinie für optische Homogenität"
        },
        "area_repair_delamination": {
            "description_de": "Reparatur von Delaminierungen oder Crazing-Netzwerken >100 mm²",
            "steps": [
                "Delaminierte Schicht entfernen durch Schleifen (80-120er Korn) bis auf stabiles Laminat",
                "Bereich austrocknen (min. 3-5 Tage bei >20°C und <60% Luftfeuchtigkeit)",
                "Feuchtigkeitsmessung mit Holzfeuchtemesser: <15% vor Neulaminierung",
                "Areal reinigen (Aceton-Wischer), Oberfläche anrauen (220er Korn)",
                "Neulaminierung: Epoxid-Barriere (2-3 Lagen) + neues Gelcoat (0.6 mm)",
                "Aushärtung 7 Tage vor Schleifen",
                "Feinschleifen und Polieren wie bei Spot-Repair"
            ],
            "epoxy_choice": "WEST SYSTEM 105/205 oder 3M DP460 für marine Anwendung",
            "cure_acceleration": "Post-Cure bei 80°C/4h kann Aushärtung auf 3-5 Tage reduzieren"
        },
        "complete_hull_rebuild": {
            "description_de": "Komplette Entfernung von Gelcoat und Neulaminierung (wirtschaftlich nur an >50% Schaden)",
            "method_water_jet": "Hochdruckwasserstahl (600-1000 bar) entfernt Gelcoat in 1-2 h, aber risiko Faserherausreißen",
            "method_sanding": "Schleifen mit 80er Korn + Nassschliff — langsam (10-20 m²/Tag), aber kontrolliert",
            "method_grinding": "Schleifer mit Schleiftopf (36-60 Körnung) — Schnell (20-30 m²/Tag) aber Staubentwicklung",
            "surface_prep_after": "Mindestens 3-5 Tage Trocknung bei >20°C, <60% Luftfeuchte",
            "new_laminate": "Epoxid-Barriere (3 Lagen) + Gelcoat (0.7-0.8 mm) + optional Topcoat (2K-PU für Beständigkeit)"
        },
        "gelcoat_vs_2k_pu_decision": {
            "gelcoat_advantages": [
                "Direkt auf GFK haftbar ohne Primer",
                "Einfache Handanwendung (Pinsel, Spachtel)",
                "Günstiger (15-25 €/kg vs. 30-50 €/kg 2K-PU)",
                "Direkte Farbwahloptionen verfügbar"
            ],
            "gelcoat_disadvantages": [
                "Nicht UV-resistent ohne Topcoat (10 Jahre max.)",
                "Osmose-anfällig bei feuchtem Untergrund",
                "Crazing nach 5-10 Jahren thermische Zyklierung"
            ],
            "2k_pu_advantages": [
                "Überlegene UV-Stabilität (15-20 Jahre ohne Vergilbung)",
                "Höhere chemische Beständigkeit (Diesel, Öl, Salzwasser)",
                "Elastischer (bis 5% Dehnung ohne Risse)",
                "Glattere Oberfläche und höherer Glanz"
            ],
            "2k_pu_disadvantages": [
                "Erfordert Epoxid-Primer (additionale Kosten, Zeit)",
                "Verarbeitung komplexer (genaues Mischen, Topfzeit 20-30 min)",
                "Längere Trocknungszeit (2-3 Wochen vor Polieren)",
                "Umweltschutz: VOC-Regulierung in EU, isocyanat-Schutz erforderlich"
            ],
            "recommendation": "2K-PU für Hauptflächen (Rumpf, Deck), Gelcoat für Innenräume/geschützte Bereiche"
        }
    },
    "polishing_schedule": {
        "grit_progression": {
            "step_1_400_grit": "Grobes Anschleifen von Kratzer und Unebenheiten, nass schleifen",
            "step_2_800_grit": "Mittleres Schleifen, weißer Schleifbelag, vollständig Durchschleifen",
            "step_3_1200_grit": "Feines Schleifen, oberflächenglättend",
            "step_4_1500_grit": "Sehr feines Schleifen, Vorbereitung für Polieren",
            "step_5_2000_grit": "Feinster Schleif-Grit, mattierte Oberfläche für Polierauftrag"
        },
        "polishing_compounds": {
            "rubbing_compound": {
                "description_de": "Mittleres Polierkompondum mit Mikrokörnern (8-15 µm)",
                "removal": "Entfernt 2000er-Schleifmarken, Kratzer bis 200 µm",
                "application": "Auftrag mit Poliermaschine (Schaumpad, 1200 rpm), dann Hand-Buff"
            },
            "fine_polish": {
                "description_de": "Feines Polierkompondum ohne Kornzusatz (Chemica-Polierkompondum)",
                "removal": "Entfernt Kratzer bis 50 µm, erzeugt Hochglanz",
                "application": "Nach Rubbing Compound, 1000-1500 rpm, sanfter Druck"
            },
            "wax_sealant": {
                "description_de": "Optionale finale Versiegelung mit Carnauba-Wachs oder Synthetic",
                "duration": "6-12 Monate Schutz vor Oxidation (Vergilbung)",
                "application": "Dünn auftragen, 10 min Trocknungszeit, dann mit Tuch polieren"
            }
        }
    }
}


CORE_MATERIALS_DATABASE: Dict[str, Any] = {
    "key_de": "Kern-Materialien-Datenbank",
    "description": "Comprehensive reference for marine sandwich core materials: balsa, PVC foam, SAN foam, honeycomb",
    "end_grain_balsa": {
        "key_de": "Endholz-Balsa",
        "source": "Ochroma pyramidale (balsa tree), Central America, tropical hardwood",
        "density_kg_m3": "100-150 kg/m³ (ultra-light, 15× lighter than water)",
        "mechanical_properties": {
            "compressive_strength_parallel_mpa": "2.5-5.0 MPa (parallel to grain)",
            "compressive_strength_perpendicular_mpa": "0.5-1.5 MPa (perpendicular to grain)",
            "flexural_strength_mpa": "8-15 MPa",
            "shear_strength_mpa": "1.2-3.0 MPa",
            "modulus_mpa": "800-1500 MPa"
        },
        "why_end_grain": {
            "description_de": "Nur radiale/axiale Schnittflächen (Holzfasern stehen senkrecht zur Oberflächenschicht)",
            "advantage": "Maximale Kompressionsfestigkeit, minimale Quellung/Schwindung in Dickenrichtung",
            "vs_flat_sawn": "Flachgeschnittenes Balsa hat schlechtere Stabilität und höhere Wasserdiffusion",
            "marine_standard": "ISO 12215-5 fordert end-grain für boot cores >50 mm Dicke"
        },
        "water_absorption": {
            "timeline": "Nasse Balsa kann nach 2-4 Wochen Wasserlagerung 30-50% ihres Volumens Wasser aufnehmen",
            "mechanism": "Holzporen (mikroporous, diameter 1-100 µm) diffundieren Wasser gegen osmotischen Gradienten",
            "consequence": "Dichte erhöht sich von 100 kg/m³ auf 150-200 kg/m³, Festigkeit verringert sich um 20-40%",
            "repair_challenge": "Nasse Balsa kann nach Trocknung nur 60-70% der Originalfestigkeit erreichen",
            "prevention": "Gelcoat-Barriere muss unversehrt bleiben, Bohrungen immer versiegeln"
        },
        "frost_mechanism": {
            "description_de": "Frostaufbruch durch Wasser-Eis-Expansion in Holzporen",
            "expansion_percentage": "9% Volumenexpansion wenn Wasser zu Eis gefriert (-10°C und darunter)",
            "consequence": "Holzporen platzen, Balsa-Feuchtigkeit kann nicht mehr austrocknen",
            "result_failure": "Struktureller Zusammenbruch des Sandwichs unter Last nach einer Frost-Saison",
            "winter_danger": "Boote in kontinentalem Klima (Schweiz, Skandinavien, Nordamerika) anfällig",
            "case_examples": {
                "newport_41": "1990er Newport 41 mit Balsa-Sandwich: 60% Kernzerstörung nach 3 Wintern in Neuengland",
                "catalina_42": "Catalina Sailing Yachts (USA) hatte Balsa-Kern-Probleme an Großflächigen Decks (1988-1995)",
                "beneteau": "Beneteau frühe Modelle (vor 2000) mit unzureichend versiegeltem Balsa-Kern"
            },
            "prevention": "Sorgfältige Versiegelung, regelmäßige Inspektionen, eventuell Kern-Injektion mit Epoxid"
        },
        "creep_under_load": {
            "description_de": "Plastische Verformung des Holzes unter konstanter Last über Zeit",
            "timeline": "1-2% zusätzliche Durchbiegung nach 5 Jahren unter 50% Lastgrenze",
            "consequence": "Sandwich wird dünner → Biegefestigkeit sinkt progressiv",
            "math_model": "Durchbiegung = σ / E × (1 + β × t^n), wobei t = Zeit in Jahren, n ≈ 0.3 für Balsa",
            "practical_effect": "10 mm Durchbiegung unter Last wird 10.5-11 mm nach 5 Jahren",
            "designer_adjustment": "Überdimensionierung um +10-15% für Langzeit-Stabilität erforderlich"
        },
        "ownership_issues": {
            "newport_sailing_corporation": {
                "boat_model": "Newport 41 (1982-1995), built approximately 200 units",
                "issue": "Balsa-Kern-Delaminierung und Wasserdurchdringung nach 10-15 Jahren",
                "symptom": "Schwammige Deck-Durchbiegung beim Betreten, Geruchsentwicklung, Farb-Blasenbildung",
                "cause": "Unzureichende Gelcoat-Dicke (nur 0.4 mm) und Feuchtigkeitserwerbung an Spanten/Beschlägen",
                "owners_complaint": "Forum: Balsa Kern komplett zerstört, Reparaturkosten USD 50,000+, Warranty-Forderungen abgelehnt"
            },
            "catalina_yachts": {
                "boat_model": "Catalina 42 Sailboat (1992-2005), approx. 350 units with balsa decks",
                "issue": "Deck-Delamination und Kern-Verweichung nach 12-18 Jahren",
                "remedy_attempts": "Bootseigner versuchen Kern-Injektion mit Epoxid (teuer: USD 8,000-15,000)",
                "forum_consensus": "ybw.com, cruisersforum: Balsa war schlechte Entscheidung, PVC-Kern haette besser sein sollen"
            },
            "beneteau_first_class": {
                "boat_model": "Beneteau First 40.7, First 45.5 (1998-2008), balsa deck core",
                "issue": "Selective kern-Zone-Verweichung an hochbelasteten Stellen (Mast-Partner, Hardware-Befestigung)",
                "diagnosis": "Sonde-Test durch kleine Bohrung zeigt Wasserdurchdringung in 15-20% der Deck-Fläche",
                "owner_experience": "Reported: USD 12,000-18,000 für selektive Kern-Erneuerung in 40-ft-Bereich"
            }
        }
    },
    "pvc_foam": {
        "key_de": "PVC-Schaumstoff",
        "manufacturer_divinycell": {
            "description_de": "Divinycell H (BASF, Schweiz) — Standard für marine Sandwich-Kern seit 1990er",
            "closed_cell_structure": "93-95% geschlossene Poren, Wasserdiffusion sehr niedrig",
            "water_absorption_24h": "<3% nach 24h Wasserlagerung (vs. >30% Balsa)",
            "water_absorption_longterm": "<5% nach 1000h Wasserlagerung (vs. 50%+ Balsa)"
        },
        "density_grades": {
            "h60": {
                "density_kg_m3": "60 kg/m³",
                "compressive_strength_mpa": "0.5-0.9 MPa",
                "shear_strength_mpa": "0.5-0.8 MPa",
                "applications": "Decks, unkritische Bereiche, Kostenoptimierung",
                "thermal_insulation": "k-Wert 0.035 W/mK"
            },
            "h80": {
                "density_kg_m3": "80 kg/m³",
                "compressive_strength_mpa": "0.8-1.5 MPa",
                "shear_strength_mpa": "0.8-1.3 MPa",
                "applications": "Standard für Rumpf-Sandwich 35-50 mm Dicke",
                "typical_use": "Hanse, Dufour, Lagoon Standardkernicke"
            },
            "h100": {
                "density_kg_m3": "100 kg/m³",
                "compressive_strength_mpa": "1.2-2.0 MPa",
                "shear_strength_mpa": "1.2-1.8 MPa",
                "applications": "Hochbelastete Zonen (Kielkutter-Rümpfe, Mast-Partner, Großyachten)",
                "structural_improvement": "+30-40% Biegefestigkeit vs. H80"
            },
            "h130": {
                "density_kg_m3": "130 kg/m³",
                "compressive_strength_mpa": "2.2-3.5 MPa",
                "shear_strength_mpa": "2.0-3.0 MPa",
                "applications": "Sehr hochbelastete Zonen, Strukturspanten, Mast-Schuh",
                "limitation": "Dichte nähert sich Balsa an (100-150 kg/m³), Gewichtsvorteil sinkt"
            }
        },
        "temperature_limit": {
            "max_continuous_c": "70°C",
            "reason": "Polyvinylchlorid (PVC) erweicht oberhalb Glasübergangstemperatur (Tg ≈ 80-85°C)",
            "consequence_overtemp": "Modulus fällt um 50-70% bei 80°C, Kern kann nicht mehr Last tragen",
            "marine_context": "In tropischen Gewässern oder unter Deckslagerung (no ventilation) kann 70-75°C erreicht werden",
            "risk_scenario": "Boot in Mittelmeer unter Sonne: Decksoberfläche 55-60°C, Kern (unter Gelcoat + Laminate) kann 65-70°C erreichen"
        },
        "cross_linked_vs_linear": {
            "linear_pvc_foam": {
                "description_de": "Einfache thermoplastische PVC-Struktur, erweichbar durch Wärmezufuhr",
                "cost": "Günstiger (12-18 €/dm³)",
                "properties": "Etwas weicher, höhere Wasseraufnahme (bis 8% langfristig)",
                "workability": "Leicht zu schneiden und zu bearbeiten"
            },
            "cross_linked_pvc": {
                "description_de": "PVC mit chemischen Vernetzungsbindungen (meist Wasserstoff-Peroxid initiiert)",
                "cost": "Teurer (18-25 €/dm³)",
                "properties": "Höhere Temperaturbeständigkeit (bis 85°C), niedrigere Wasseraufnahme (<3%)",
                "divinycell_h": "Alle modernen Divinycell-Sorten sind cross-linked (Trademark: Divinycell-H)"
            },
            "manufacturer_recommendation": "Für marine Anwendung IMMER cross-linked verwenden (ISO 12215-5 fordert es)"
        }
    },
    "san_foam": {
        "key_de": "SAN-Schaumstoff (Styrol-Acryl-Nitril)",
        "typical_brand": "CoreCell (Rohacell) oder Airex (BASF, neuer Name Airex)",
        "properties_comparison": {
            "density_kg_m3": "40-130",
            "water_absorption_24h": "<1% (noch besser als PVC!)",
            "temperature_limit_c": "80-100°C (besser als PVC)",
            "cost_premium": "+40-60% vs. Divinycell PVC",
            "mechanical_properties": "Leicht besser als PVC bei gleicher Dichte"
        },
        "advantages": [
            "Überlegene Wasserbeständigkeit (closed-cell 99%)",
            "Höhere thermische Stabilität (bis 100°C)",
            "Etwas bessere Spannungsverteilung (höherer Modul)",
            "Chemische Beständigkeit gegen Laugen/Säuren"
        ],
        "disadvantages": [
            "Deutlich höherer Preis (25-35 €/dm³)",
            "Längere Verarbeitungszeit (höhere Viskosität Epoxid erforderlich)",
            "Weniger Häufig verfügbar in lokalen Lagern",
            "Nicht alle Werft-Laminierung-Parameter optimiert für SAN"
        ],
        "manufacturer_adoption": {
            "dufour_yachts": "Atoll 430 und neuer mit SAN CoreCell für Decks (Premiummodelle)",
            "hanse_yachts": "C70 Sport und höher mit SAN CoreCell in Hochlast-Zonen",
            "lagoon_catamarans": "Lagoon Seventy 7 (großen Yacht 2020+) mit SAN Kern überall"
        }
    },
    "honeycomb_core": {
        "key_de": "Wabenkernicke",
        "material_options": {
            "nomex_kevlar": {
                "description_de": "Aramid-Papier-Waben (Nomex von DuPont oder Kevlar 49)",
                "density_kg_m3": "30-100 kg/m³",
                "compressive_strength_mpa": "0.3-2.0 MPa (abhängig Dichte)",
                "water_absorption_critical": "Nomex ist hydrophil — EXTREME Wasserdiffusion wenn nicht versiegelt",
                "consequence": "Ungeschütztes Nomex-Wabe kann 50-100% Wasser aufnehmen nach Monaten",
                "requirement": "Vollständiger epoxy-Einkapselung erforderlich, keine Poren dürfen offen bleiben",
                "cost": "60-100 €/m² für Rohware"
            },
            "aluminum_honeycomb": {
                "description_de": "Aluminiums-Wabenstruktur, Zellen 3-5 mm, Wandstärke 0.05-0.1 mm",
                "density_kg_m3": "25-40 kg/m³ (ultra-leicht)",
                "compressive_strength_mpa": "1-3 MPa (trotz geringer Dichte hoch)",
                "water_absorption": "Metall nicht hygroskopisch, aber Korrosion in Salzwasser ohne Schutz",
                "galvanic_risk": "Al in Kontakt mit CFK oder Kupfer → Korrosion (siehe FIBER_DATABASE carbon_fiber)",
                "applications": "Rennboote, VO70, eher nicht Langzeitboote",
                "cost": "100-150 €/m²"
            },
            "polypropylene_honeycomb": {
                "description_de": "PP-Kunststoff-Waben, robust und wasserdicht",
                "density_kg_m3": "25-60 kg/m³",
                "water_absorption": "Minimal (<0.5%)",
                "temperature_limit_c": "80°C (ähnlich PVC)",
                "cost": "40-70 €/m² (günstiger als Nomex)",
                "disadvantage": "Etwas niedrigere Kompression als Nomex bei gleicher Dichte"
            }
        }
    },
    "failure_mechanisms_sandwich": {
        "key_de": "Fehlermechanismen in Sandwich-Strukturen",
        "debonding": {
            "description_de": "Trennung der äußeren/inneren Schicht vom Kern",
            "cause": "Unzureichende Haftung zwischen Laminat und Kern (Verschmutzung, Trennmittel-Rückstände)",
            "mechanism": "Scherkräfte in der Grenzfläche übersteigen Adhäsionskraft",
            "visual_symptom": "Hohle Stellen klopfbar (mit Klopfhammer testen), mattere Töne vs. Normalbereich",
            "progression": "Kleine Debonds wachsen unter Last → kritische Fläche >100 cm² → Bruchinitiator",
            "prevention": "Oberflächenvorbereitung Kern (anrauen, reinigen), richtige Harz-Viskosität"
        },
        "core_shear_failure": {
            "description_de": "Scherbruch des Kerns in der Dickenrichtung",
            "cause": "Zu dunne Kern bei hoher Querlast oder Impact",
            "mechanism": "Scherkraft τ = Q / A_shear übersteigt Kern-Scherfestigkeit",
            "consequence": "Zwei Laminate rutschen gegeneinander ab, Verlust der Biegefestigkeit",
            "repair": "Lokalbereich öffnen, neuen Kern einsetzen, relaminieren",
            "prevention": "Richtige Kern-Dicke nach ISO 12215 Berechnung"
        },
        "frost_related_failure": {
            "description_de": "Spezifisch für Balsa: Wasser-Eis-Expansion zerstört Zellstruktur",
            "timeline": "Erste Frostperiode (eine Nacht -5°C): lokale Schädigungen",
            "accumulation": "Drei bis fünf Frost-Zyklen pro Winter × mehrere Winter = kumulativer Schaden",
            "consequence": "Nach 3-5 Wintern ist Balsa-Kern völlig zerstört, Sandwich funktioniert nicht mehr",
            "case_severity": "Newport 41 Fallstudie: nach Winter in Neuengland war ~40% der Deck-Fläche unbenutzbar"
        },
        "thermal_stress_failure": {
            "description_de": "Unterschiedliche thermische Ausdehnung zwischen Laminat und Kern",
            "mechanism": "GFK Expansion 20-30 × 10^-6 /K, PVC Expansion 70-100 × 10^-6 /K, Balsa 0-5 × 10^-6 /K",
            "temperature_swing": "Boot sonne 60°C tagsüber, 10°C nachts = 50°C Zyklus",
            "consequence": "Spannungen 1-3 MPa entstehen, können über Zeit zu Mikrorissen führen",
            "risk_material": "PVC-Schäume höher anfällig als Balsa (paradox!) wegen höherer Expansion",
            "mitigation": "Kernmaterial mit niedriger Expansion wählen (Balsa, SAN, Nomex), oder dickere Laminate"
        },
        "compression_under_hardware": {
            "description_de": "Lokale Kompression des Kerns unter Bolzen, Winches, Padeyes",
            "cause": "Konzentrierte Last auf kleine Fläche (z.B. M10 Bolzen = 78 mm² Fläche)",
            "load_example": "Mast-Fuß 15 kN Load → Druck = 15,000 N / 78 mm² = 192 MPa",
            "consequence": "Kern unter Hardware wird ausgelenkt bis >20% Dicke-Verlust",
            "result": "Schub-Versagen des Kerns um Hardware herum",
            "prevention": "Untersperr-Platte (Backing Plate) 50×50 mm oder größer, verteilt Load auf Kern"
        }
    }
}


CONSTRUCTION_METHODS_DATABASE: Dict[str, Any] = {
    "key_de": "Konstruktions-Methoden-Datenbank",
    "description": "Marine GFK hull construction methods: hand layup, vacuum bagging, infusion, prepreg, autoclave",
    "hand_layup_spray": {
        "key_de": "Handlaminat und Spritzverfahren",
        "process_overview": "Offene Form, manuelles Auflaminieren, mit oder ohne Spritzen",
        "standard_procedure": [
            "Trennmittel auf Form auftragen (PTFE oder Wachs)",
            "Gelcoat spritzen oder streichen (Spray: 250-400 ml/min, 1-2 Psi)",
            "CSM (Chopped Strand Mat) auflegen, mit Harz durchtränken (Roller oder Bürste)",
            "Roving-Gewebe auflegen, durchtränken, Luft-Blasen ausrollen",
            "Wiederholen Schichtaufbau nach Laminat-Plan",
            "Aushärten 24-48h bei Raumtemperatur, dann Entformen"
        ],
        "glass_resin_ratio": {
            "target": "60% Glas, 40% Harz (Gewicht)",
            "industry_reality": "50-70% Glas, 30-50% Harz (hohe Variation)",
            "measurement": "Pyrolyse-Test: 500°C in Ofen, Gewicht nach abbrennen = Glasgehalt",
            "consequence_too_much_resin": "Schweres Laminat, schlechtere Festigkeit, höhere Osmose-Anfälligkeit",
            "consequence_too_much_glass": "Lufteinschlüsse, schlechte Haftung, Faserflocken (Baumwolle-Effekt)"
        },
        "weight_variation": {
            "description_de": "Hand-Laminat hat große Variabilität in Dicke und Dichte",
            "variation_range": "±10% Dicke über 1 m² Fläche ist normal",
            "cause": "Unterschiedliche Druck beim Ausrollen, variable Harz-Sättigung",
            "consequence": "Biegefestigkeit schwankt ±15% lokal, schwache Stellen unter Last anfällig",
            "quality_control": "Schichtdicken-Messer nach Aushärtung: min. 5 Punkte pro 5 m², akzeptabel ±0.5 mm"
        },
        "styrene_emissions": {
            "description_de": "Flüchtigkeit des Styrols während Laminierung und Aushärtung",
            "emission_rate_handlaminat": "10-20 g/m² Laminat (bis zu 30 g/m² bei schlechtem Timing/Temperatur)",
            "health_limit": "MAK Deutschland 100 ppm (Schicht-Grenzwert), 50 ppm (Kurzzeitwert)",
            "worker_exposure": "Offenes Hand-Laminat in Werft: typisch 20-50 ppm, Spitzenwerte bis 100+ ppm",
            "emission_reduction_methods": [
                "Low-Styrene-Harze (NPG, <500 g/L Styrol statt 700-800 g/L standard)",
                "Natürliche Belüftung (nicht möglich im Winter)",
                "Aktivkohle-Filter im Absaugsystem",
                "Vakuum-Infusion statt Handlaminat (60-70% Emissions-Reduktion)"
            ],
            "workplace_regulation": "In EU: ATEX-Zertifikat erfordert wenn Styrol-Dämpfe über 25% LEL (Lower Explosive Limit)"
        }
    },
    "vacuum_bagging": {
        "key_de": "Vakuum-Beutel-Verfahren",
        "process_overview": "Laminat wird in luftdichten Beutel eingewickelt, Vakuum entzieht Luft und Überschuss-Harz",
        "procedure": [
            "Laminat auf Form in normaler Weise auflegen (wie Handlaminat, aber feuchter, dicker)",
            "Peel-Ply (Trenn-Gewebe) auflegen, das später abgezogen wird",
            "Breather-Schicht (dickes Vlies) auflegen (saugt Harz auf, ermöglicht Luftfluss)",
            "Vakuum-Schlauch in Breather-Schicht legen",
            "Vakuum-Dichtung (Silikon-Kordel) um gesamte Fläche",
            "Vakuum-Pumpe starten (ca. 0.8 bar = -0.2 bar Unterdruck)",
            "Aushärten unter Vakuum (typisch 6-12 Stunden)"
        ],
        "resin_content_reduction": {
            "without_vacuum": "50-65% Harz (hand-laminat)",
            "with_vacuum": "30-40% Harz (vacuum bag)",
            "weight_reduction": "20-35% weniger Gesamtgewicht bei gleicher Festigkeit",
            "strength_improvement": "Weniger Poren → +10-20% Zugfestigkeit, +15-25% Scherfestigkeit"
        },
        "vacuum_pressure_specification": {
            "minimum_pressure": "-0.6 bar (-60 kPa)",
            "standard_working": "-0.75 to -0.85 bar",
            "maximum_safe": "-0.95 bar (Risiko Schaumbildung wenn höher bei Polyester)",
            "pump_capacity": "Mindestens 100 l/min Pumprate (bei 5 m² Fläche, Schlauch-Durchmesser 8-10 mm)",
            "vacuum_holding": "Typisch 6-12 Stunden bei Raumtemperatur, länger bei kühleren Bedingungen"
        },
        "error_sources_vacuum": [
            "Luftlecks in Vakuum-Dichtung → ungleichmäßige Verdichtung, schwache Stellen",
            "Zu niedriger Vakuum → unzureichende Harzentfernung, zu hoher Harz-Gehalt",
            "Zu hoher Vakuum bei Polyester → Schaum-Bildung, Blasen im Laminat",
            "Breather-Schicht zu dünn → Harz wird aufgesaugt, Breather-Drainage blockiert",
            "Zu kurze Vakuum-Zeit → oberflächlich verdichtet, innen noch porös",
            "Ungenügende Temperaturkontrolle → Styrol verdampft zu schnell, Blasen entstehen"
        ]
    },
    "vacuum_infusion_vartm": {
        "key_de": "Vakuum-Infusion (VARTM / Vakuum-Assisted Resin Transfer Molding)",
        "process_overview": "Trockene Faserstruktur wird mit Vakuum infundiert, Harz wird angesaugt",
        "procedure": [
            "Trockene Fasermatte (CSM, Roving, Biaxial) in Form legen (kein Harz!)",
            "Peel-Ply und Breather-Schicht auflegen wie bei Vacuum Bag",
            "Harz-Eintrag-Leitung (Inlet) in Form legen, Vakuum-Leitung (Outlet) in Breather",
            "Vakuum starten (typisch -0.8 bar), Harz fließt in Form → Vakuum-Front wandert",
            "Durchfluss-Rate: 1-5 kg/m² pro Minute (abhängig Faserdichte, Vakuum)",
            "Wenn Vakuum-Front die Outlet-Leitung erreicht, weiterhin 4-6 Stunden unter Vakuum aushärten"
        ],
        "fiber_content": {
            "typical_vartm": "60-70% Glas, 30-40% Harz (deutlich fasserreich als Handlaminat 50%)",
            "benefit": "Bessere Festigkeit bei geringerem Gewicht",
            "consequence": "Geringere Harz-Mengenfluss = längere Infusions-Zeit, komplexere Kontrolle"
        },
        "flow_front_control": {
            "description_de": "Die Infusions-Front (Grenzfläche Luft/Harz) muss gleichmäßig fortschreiten",
            "monitoring_method": "Sichtprüfung oder Thermokamera, oder Tracerfarbe im Harz (nicht sichtbar mit bloßem Auge)",
            "flow_rate_target": "1-2 cm/min für 4-5 m² Fläche (nicht zu schnell, nicht zu langsam)",
            "uneven_flow": "Wenn eine Kante schneller fließt → Luft wird eingeschlossen ('dry spot'), Laminat-Fehler"
        },
        "dry_spots_catastrophic": {
            "description_de": "Unbenetzte Faserbereiche, wo Harz nicht ankommt",
            "cause": "Ungleichförmige Vakuum-Druckverteilung oder falsch gelegte Einlass-Leitung",
            "consequence": "Trockene Fasern können Last nicht tragen → Bruchstelle, Delaminierung",
            "detection": "Nicht offensichtlich nach Aushärtung (Oberfläche sieht normal aus), aber Struktur-Test (UT) offenbart Lücke",
            "incidence_rate": "In Serienfertigung: 2-5% der Teile haben kleine Dry-Spots, kritisch wenn >50 cm²"
        },
        "major_manufacturer_adoption": {
            "hanse_yachts": "Hanse 315, 355 ab 2008: VARTM für Rumpf und Deck (70-80% der Produktion)",
            "dufour_yachts": "Atoll-Serie seit 2010: Vakuum-Infusion für Standard-Rümpfe <45ft",
            "lagoon_catamarans": "Multi 55, Lagoon 400: VARTM für catamaran Rümpfe (große Flächen profitieren)",
            "production_volume": "VARTM ist Standard für Serienyachtbau >6 Boote/Monat, <15 m, Kst-Druck <1000 €/Boot"
        }
    },
    "prepreg_autoclave": {
        "key_de": "Vorgetränkte Fasern (Prepreg) — Autoklaven-Verfahren",
        "material": "Glasfaser oder Carbon bereits mit Harz getränkt, teilweise ausgehärtet (B-stage)",
        "cure_profile": {
            "typical_temperature": "70-80°C für marine-Harze (nicht 120-180°C wie aerospace)",
            "heating_rate": "2-4°C pro Minute (kontrolliert, um Gasblasen zu vermeiden)",
            "hold_time_at_peak": "30-60 Minuten",
            "cooling": "Langsam abkühlen, nicht schneller als 3°C pro Minute"
        },
        "prepreg_shelf_life": {
            "at_room_temperature": "Typisch 5-7 Tage maximal (Harz vernetzt langsam)",
            "at_minus_18c": "6-12 Monate (Kühl-Lagerung erforderlich)",
            "practical_handling": "Großzügig laminieren, nicht lagern, da Kosten für Kühlung + Verschwendung"
        },
        "autoclave_size_constraint": {
            "typical_small_autoklave": "1.2 m (Breite) × 1.5 m (Länge) × 0.8 m (Höhe)",
            "boat_hull_limit": "ca. 6-8 m Länge für Komplettaushärtung",
            "larger_components": "Müssen in Schichten assembliert werden, Verbindung später geklebt oder gelaminiert"
        },
        "manufacturer_use": {
            "rare_in_production": "Prepreg + Autoklav ist sehr teuer (Ausrüstung >EUR 500,000, Prozess 24h pro Boot)",
            "aircraft_industry": "Nur in Aerospace (z.B. Pipistrel-Elektro-Flugzeuge aus Faserverbund)",
            "marine_exclusions": "Praktisch keine Standard-Serienyacht nutzt Autoklav-Prepreg (zu teuer für <30 m Boot)"
        },
        "hexcel_hexply_m79": {
            "description_de": "Hoch-Leistungs Marine Prepreg, Carbon/Epoxid, 70°C Cure",
            "specification": "Hexcel HexPly M79-5 (Uni-directional, 0°-Fasern), 70°C / 60 min",
            "mechanical_properties": {
                "tensile_strength_mpa": "2200-2400",
                "tensile_modulus_gpa": "135-145",
                "fiber_volume_fraction": "60-65%",
                "void_content_percent": "<2% (sehr hochwertig)"
            },
            "cost": "EUR 80-150 pro kg (vs. EUR 2-5 für Hand-Laminat)",
            "application": "Nur in Rennyachten, große Motorjachten, spezialisierte Bauten"
        }
    }
}


HULL_DECK_JOINT_DATABASE: Dict[str, Any] = {
    "key_de": "Rumpf-Deck-Verbindungs-Datenbank",
    "description": "Hull-deck joint design, failures, and repair methods",
    "bolted_joint": {
        "key_de": "Verschraubte Verbindung (konventionell)",
        "design": "Rumpf und Deck liegen flach nebeneinander, Bolzen durchstechen beide Laminate",
        "bolt_spacing": "Typisch 100-150 mm Lochabstand (4-6 Bolzen pro laufender Meter)",
        "typical_fastener": "M6 oder M8 (316 Stainless Steel), Nyloc-Muttern (selbstsperrende Mutter mit Kunststoff-Ring)",
        "sealing_method": "3M 5200 oder Sikaflex 292 zwischen Rumpf/Deck-Flanschen vor Montage",
        "failure_sequence": {
            "stage_1_vibration": "Segelkräfte induzieren zyklische Vibration (0.5-2 Hz) an der Rumpf-Deck-Naht",
            "stage_2_loosening": "Kontinuierliche Bewegung lockert Bolzen (Nyloc hilft, aber nicht zu 100%)",
            "stage_3_sealant_failure": "Dichtmasse (3M 5200) wird zyklisch gestaucht und gezogen, reißt nach 3-5 Jahren",
            "stage_4_water_ingress": "Wasser dringt über offene Bolzenlöcher in Deck ein (Wasserdurchsatz >0.1 L/Tag möglich)",
            "stage_5_core_destruction": "Sandwich-Kern (PVC, Balsa) wird durchfeuchtet und verweicht",
            "stage_6_structural_failure": "Kern verliert Steifigkeit → Deck verdünnt sich → weitere Wasser-Eindringung"
        },
        "water_penetration_path": "Bolzen → Sealant-Risse → Zwischen Rumpf/Deck → Kontakt mit Kern",
        "consequence_without_repair": "Nach 5-10 Jahren: Deck-Bereich neben Rumpf unbenutzbar (schwammig, riecht), Strukturversagen möglich"
    },
    "through_bolted_joint": {
        "key_de": "Durchstanzverbindung mit Unter-Platte (Through-Bolted)",
        "design": "Bolzen durchstechen ALLE Laminate (Rumpf außen + innen, Deck außen + innen), plus Unter-Platte (Backing Plate)",
        "backing_plate": {
            "material": "316 Stainless Steel oder Kunststoff (Nylon, GFK-Platte)",
            "size": "Typisch 50×50 mm oder 75×75 mm Quadrat",
            "function": "Verteilt Druckspannungen über größere Fläche, verhindert Einsinken in GFK",
            "thickness": "min. 3-5 mm für Stahl, 10-15 mm für Kunststoff"
        },
        "fastener_specification": {
            "material": "A4-70 (316 Stainless Steel, 70 ksi Mindesfestigkeit)",
            "size": "M8 × 50-80 mm Schraube + Unterlegscheibe + Nyloc-Mutter",
            "preload": "Drehmoment: 25-35 Nm für M8 mit 316 SS (Kontrollschlüssel verwenden)"
        },
        "sealing_procedure": {
            "step_1": "3M 5200 oder Sikaflex 292 auf beide Seiten der Rumpf/Deck-Flansche auftragen (3-5 mm Raupe)",
            "step_2": "Bolzen einsetzen, Unterlegscheibe und Nyloc-Mutter von unten",
            "step_3": "Drehmoment auf Zielwert (25 Nm M8) anziehen, Bolzen nicht überdrehen (Fasern-Quetschung)",
            "step_4": "Überschuss Sealant auspressen, mit Spachtel glätten",
            "step_5": "24h Aushärtung vor Belastung"
        },
        "advantage_vs_simply_bolted": [
            "Unter-Platte verhindert GFK-Einsinken → tiefere Druckkraft verteilt",
            "Geringere Druckspannungen im Laminat → weniger Mikrorisse",
            "Strukturelle Redundanz: wenn eine Bolze ausfällt, andere halten noch",
            "Wasserdichtheit besser durch Backing Plate Abdichtung"
        ]
    },
    "bonded_joint_adhesive": {
        "key_de": "Geklebte Verbindung (Adhesiv-Klebung)",
        "design": "Rumpf- und Deck-Flansche werden überlappt und nur geklebt, keine Bolzen",
        "adhesive_choice": {
            "sikaflex_292": {
                "type": "Polyurethan-Kleber, 2-komponentig",
                "processing": "Komponenten 1:1 mischen, Topfzeit 30-45 min, klebrig innerhalb 5-10 min nach Auftrag",
                "cure_time": "7 Tage für volle Festigkeit",
                "strength": "Zugfestigkeit >15 MPa (sehr stark)",
                "elongation": "100-200% (elastisch, gutfür thermische Bewegung)",
                "marine_spec": "Für Rumpf-Deck am häufigsten verwendet (Jeanneau, Lagoon)"
            },
            "3m_5200": {
                "type": "Polyurethan-Kleber, 1-komponentig",
                "processing": "Auftrag direkt aus Kartusche, Topfzeit 30-45 min, selbstabbindend",
                "cure_time": "7 Tage für volle Festigkeit",
                "strength": "Zugfestigkeit 12-14 MPa (etwas schwächer als Sikaflex 292)",
                "advantage": "Einfachere Handhabung (kein Mischen), weniger Verschwendung",
                "disadvantage": "Muss in dünnen Raupn (<5 mm) verwendet werden, sonst verdickt sich Härtung"
            },
            "plexus_mma": {
                "type": "Methyl-Methacrylat, 2-komponentig",
                "processing": "Schnelle Aushärtung (5-15 min Topfzeit), selbstgenug bei 50% Durchhärtung",
                "strength": "Zugfestigkeit 20-25 MPa (höchster Wert unter Kleber)",
                "advantage": "Schnelle Verarbeitung, ermöglicht schnelle Montage",
                "disadvantage": "Sehr exotherm (kann brennen wenn nicht richtig gemischt), chemisches Geruchsprobleme, seltener in marine Anwendung"
            }
        },
        "surface_preparation": {
            "step_1_grinding": "Beide Oberflächen (Rumpf-Flansch, Deck-Flansch) mit 80er Korn anschleifen",
            "step_2_cleaning": "Mit Aceton oder Alkohol abwischen, Staub und Öl entfernen",
            "step_3_drying": "Min. 2-3 Stunden trocknen bei >18°C und <60% Luftfeuchtigkeit",
            "step_4_primer": "Optional: Primer auftragen (Sikaflex Haftungsprimer HM336 oder 3M 08693)",
            "step_5_assembly": "Kleber auftragen, Flächen zusammenpressen, min. 24h Klemmdruck (C-Klemmen)"
        },
        "overlap_length": {
            "minimum": "30-40 mm (wenn gut geklebt)",
            "typical_specification": "50-70 mm (sicherere Auslegung)",
            "advantage": "Mehr Oberfläche = höhere Scherkraft vor Versagen"
        },
        "disadvantage_bonded": [
            "Klebung nicht inspizierbar nach Aushärtung (Bolzen können sichtgeprüft werden)",
            "Qualitätsabhängig von Oberflächen-Vorbereitung (kritisch für marine Anwendung)",
            "Thermische Wechsel können Spannungen aufbauen (unterschiedliche Wärmeausdehnungen Kleber vs. GFK)",
            "Reparatur schwieriger (Kleber muss vollständig entfernt werden vor neuer Klebung)"
        ]
    },
    "laminated_joint": {
        "key_de": "Durchlaminierte Verbindung (stärkste Methode)",
        "design": "Beim Laminieren werden Rumpf und Deck nicht getrennt, sondern kontinuierlich überlappt laminiert",
        "overlap_length": "Typisch 100-200 mm, abhängig Last und Faserdichte",
        "laminate_schedule": [
            "Rumpf außen laminieren (z.B. 4-5 Lagen Roving)",
            "Übergangszone: Rumpf und Deck wurden nebeneinander in Form montiert (Oberflächenschnittstelle)",
            "Durchgehende Lagen durchlaminieren, gleichzeitig Rumpf-Deck überlappt",
            "Deck innen laminieren"
        ],
        "fiber_orientation_critical": "Lagen müssen in Überlappszone ±45° sein (für Torsion/Scherkräfte), nicht 0/90°",
        "advantage": [
            "Stärkste Methode: Festigkeit begrenzt durch GFK Fasern, nicht durch Klebung",
            "Keine Diskontinuität in der Struktur → effiziente Lastverteilung",
            "Langzeitstabilität bestätigt (>30 Jahre ohne Versagen wenn richtig gemacht)"
        ],
        "disadvantage": [
            "Nur in Neuproduktion praktikabel (Rumpf und Deck müssen in Form relativ sein)",
            "Längere Laminierzeit (Überlappzone muss sorgfältig laminiert werden)",
            "Nicht reparierbar (Trennung der Überlappzone unmöglich ohne Zerstörung)"
        ],
        "manufacturer_standard": "Alle Premiumwerften (Hanse, Dufour, Lagoon, Jeanneau) verwenden durchlaminierte Joints bei Serienproduktion"
    },
    "failure_case_studies": {
        "bavaria_yachtbau_issue": {
            "boat_model": "Bavaria Cruiser 50 (2005-2010 era)",
            "reported_problem": "Undichte Rumpf-Deck-Verbindung, Wasser-Eindringung nach 5-7 Jahren",
            "investigation": "Forum ybw.com: Bavaria Hull-Deck Joint Failure thread, >150 Beitraege",
            "root_cause": "Sealant-Versagen durch unzureichende Oberflächenvorbereitung (Gelcoat nicht entfernt vor Klebung)",
            "consequence": "Deck-Bereich neben Rumpf wurde durchfeuchtet, Sandwich-Kern PVC gelang in Schwellungen auf",
            "owner_solutions": [
                "Komplette Rumpf-Deck-Trennung und Neulaminierung (EUR 15,000-25,000, aufwendig)",
                "Bohren von Drainagebohrungen alle 50 cm und Injektion von Epoxid-Harz (EUR 4,000-8,000, unvollständig)"
            ],
            "warranty_claim": "Bavaria lehnte ab - normal wear and tear, Boote ausserhalb Gewaehrleistung"
        },
        "hanse_atlantic": {
            "boat_model": "Hanse Atlantic (35-45 ft, 2008-2015)",
            "reported_strengths": "Durchlaminierte Rumpf-Deck-Verbindung, hochwertige Konstruktion",
            "reported_issue": "Vereinzelte Fälle von Spannungsrissen an der Rumpf-Deck-Linie (nicht primär Wassereintritt, eher optisch)",
            "analysis": "Thermische Zyklierung (Rumpf dunkelblau, Deck weiß) erzeugt differentiale Ausdehnung",
            "consequence": "Feine Crazing-Risse im Bereich der Verbindung, ästhetisch, aber keine Strukturprobleme",
            "resolution": "Hanse bot freie Reparatur (Schleifen/Neupolieren) unter Gewährleistung"
        },
        "lagoon_catamaran_water_ingress": {
            "boat_model": "Lagoon 420 (2010-2015)",
            "reported_issue": "Wasser-Eindringung an einem der beiden Rümpfe (katamaranes Sandwich)",
            "cause": "Verschraubte Rumpf-Deck-Verbindung mit unzureichender Dichtmasse zwischen Flanschen",
            "timeline": "Erstes Jahr in Betrieb Problem-frei, nach Jahr 2-3 Wassereintritt offensichtlich",
            "diagnosis": "UT-Scanning zeigte 40% der Deck-Fläche durchfeuchtet",
            "repair": "Selective Kern-Ersatz + Neulaminierung (EUR 20,000+), Kosten-Kampf mit Lagoon (Kulanz 50%)"
        }
    },
    "inspection_methods": {
        "visual_inspection": {
            "description_de": "Sichtprüfung nach außen auf Risse, Flecken, Verschmutzung",
            "frequency": "Jährlich vor Seesaison",
            "checks": [
                "Crazing oder Stress-Risse entlang Rumpf-Deck-Linie sichtbar? (von außen Licht abwinkeln)",
                "Verfärbungen oder Wasserlecks-Ausblühungen an Bolzenlöchern?",
                "Sealant sichtbar intakt oder gerissen?",
                "Rost oder Korrosion um Bolzen (bei Stahl-Befestigung)?"
            ]
        },
        "impact_testing_tap_test": {
            "description_de": "Klopfen mit Kunststoff-Hammer, Schallprüfung auf Delaminierung",
            "procedure": "Mit Gummi-Hammer alle 20-30 cm entlang Rumpf-Deck-Linie klopfen",
            "sound_normal": "Hoher, heller Ton (dumpf/dull wenn gesund laminiert)",
            "sound_problem": "Tiefer, matterer Ton weist auf Delaminierung oder Delamination hin",
            "interpretation": "Nicht 100% zuverlässig (Erfahrung erforderlich), aber schnelle Vor-Screening"
        },
        "ultrasonic_testing_ut": {
            "description_de": "Ultraschall-Prüfung mit UT-Gerät (Höhe und Durchsatzmessung)",
            "capability": "Misst tatsächliche Schichtdicke und erkennt Delaminierungen",
            "procedure": "Scanning-Kopf alle 20 cm entlang Naht, mit Gel-Kopplung auf Oberfläche",
            "resolution": "Kann Schichten bis 0.1 mm unterscheiden, Voids >10 mm² erkennen",
            "cost": "Klassisches UT-Gerät EUR 2,000-5,000, Profi-Service EUR 100-200 pro Stunde",
            "interpretation": "Erfordert Fachpersonal (Zertifizierung ISO 9712 Level 2 empfohlen)"
        },
        "thermal_imaging": {
            "description_de": "Infrarot-Thermografie, erkennt Feuchte-Zonen durch geringere Wärmekapazität",
            "principle": "Feuchte Bereiche kühlen langsamer ab nach Sonneneinstrahlung",
            "equipment": "Thermal-Kamera EUR 3,000-15,000 (spezialisiert)",
            "procedure": "Scanning nach heißem Tag, Unterschiede deutlicher",
            "advantage": "Schnelle Großflächen-Prüfung (ganze Rumpf-Deck-Linie in 10 min)",
            "limitation": "Gibt nur grobe Hinweise, nicht quantitativ"
        }
    }
}


MATERIAL_SPECIFICATIONS: Dict[str, Any] = {
    "key_de": "Material-Spezifikationen und Normen",
    "iso_12215_5_standard": {
        "title": "Scantling Design Rules for Monohull Sailing Boats",
        "scope": "Vergnügungssegelboote 2.5-24 m Rumpflänge",
        "edition": "2019 (neueste, ersetzt 2008-Version)",
        "design_methodology": "Klassifikations-basiert mit Sicherheitsfaktoren",
        "factors_considered": [
            "Bootslänge und Deplacement",
            "Rauheit des geplanten Einsatzgebietes (Wasser-Größenklassifizierung)",
            "Material (GFK, Holz, Stahl, Aluminium mit unterschiedlichen Koeffizienten)",
            "Konstruktionsart (Massiv-Laminat, Sandwich mit verschiedenen Kern-Materialien)"
        ],
        "water_classification": {
            "ocean": "Beliebige Wassertiefen, Wellenhöhe statistisch 4% >7m, Design für Sturm-Bedingungen",
            "offshore": "Unbegrenzte Wassertiefen, Wellenhöhe statistisch 4% >4m, maritimes Klima",
            "inshore": "Küstenbereich, maximale Distanz zur Küste 60nm, Wellenhöhe <3m dominiert",
            "sheltered": "Binnengewässer, Seen, Flüsse, max. Wellenhöhe 1-2m"
        },
        "bending_moment_formula": "M_design = 0.1 × Δ_tonnes × L_hull_m (vereinfacht)",
        "shear_force_formula": "Q_design = 0.05 × Δ_tonnes × g (Vertikalbeschleunigung unter Segang)",
        "torsional_moment": "T_design = 0.03 × Δ_tonnes × L_hull_m (Moment aus asymmetrischer Segelbelastung)",
        "material_safety_factors": {
            "glass_fiber_gfk": 1.5,
            "wood_hull": 2.0,
            "steel_hull": 1.8,
            "aluminum_hull": 1.8,
            "composite_carbon": 1.6
        },
        "minimum_thickness_rules": {
            "small_boat_5m_gfk": "3-4 mm Monolith-Laminat (kein Sandwich erlaubt unter 5m)",
            "medium_boat_12m_gfk_sandwich": "2-3 mm äußere Laminat + 40-60 mm Kern + 2-3 mm innere Laminat",
            "large_yacht_20m_gfk_sandwich": "3-4 mm äußere + 60-100 mm Kern + 3-4 mm innere"
        }
    },
    "astm_standards": {
        "astm_d570": {
            "title": "Water Absorption of Plastics",
            "test_method": "24h-Wasserlagerung bei 23°C, Gewichtszunahme gemessen",
            "marine_application": "Kontroll-Prüfung für Gelcoat und Resin-Systeme",
            "acceptance_criterion": "<2% für marine-Harze"
        },
        "astm_d4214": {
            "title": "Standard Test Method for Evaluating the Chalking Resistance of Organic Coatings",
            "procedure": "Krepp-Papier auf bewitterter Oberfläche drücken, abziehen, Pulver-Abrieb beurteilen",
            "grades": ["0 = Keine Kreide", "1 = Spuren", "2 = Leicht", "3 = Moderat", "4 = Schwer", "5 = Sehr schwer"],
            "marine_spec": "Grade 1-2 nach 5 Jahren Bewitterung akzeptabel"
        },
        "astm_g154": {
            "title": "Fluorescent UV Exposure of Non-Metallic Materials",
            "test_condition": "ASTM G154 Cycle 4 (UVA-340, 0.89 W/m², 60°C Bulb-Temperatur, 4h UV + 4h Kondensation)",
            "duration": "Typisch 1000-2000 Stunden (entspricht 3-5 Jahren Outdoor bei niedriger Südbreite)",
            "property_retention": "Gelcoat/Topcoat sollte 70-80% Glanz nach 1000h behalten"
        }
    },
    "european_standards": {
        "din_52614": {
            "title": "Testing of Glass Fiber Reinforced Plastics — Mechanical Test Methods",
            "tests_covered": ["Zug-Prüfung", "Biege-Prüfung", "Schub-Prüfung", "Druck-Prüfung"],
            "marine_relevance": "Deutsche Werften nutzen diese Normen für Baumaterial-Kontrolle"
        },
        "en_iso_3268": {
            "title": "Unsaturated Polyester Resins (UP) — Determination of Water Absorption",
            "method": "Ähnlich ASTM D570, europäische Harmonisierung",
            "acceptance": "Marine GFK Harze: <2% nach 24h Wasserlagerung"
        }
    },
    "manufacturer_certifications": {
        "bv_classification": {
            "certifier": "Bureau Veritas (französische Klassifikations-Gesellschaft)",
            "scope": "Klassifizierung von Segelschiffen und Motorschiffen >24m",
            "requirements": "Werften mit BV-Zertifikat müssen ISO 12215-5 + BV-Zusatz-Regeln befolgen",
            "inspection_frequency": "Nach Bau: Inspektionen während Konstruktion + Vor-Indienststellung",
            "hull_survey": "Alle 5 Jahre (außer Untersuchung), Alle 10 Jahre intensive Untersuchung"
        },
        "lloyd_register": {
            "certifier": "Lloyd's Register of Shipping (Britische Klassifikations-Gesellschaft)",
            "class_notation": "Class 100A1 für Segelboote, Class 100A1 für Motorboote",
            "material_standards": "LR Rules für GFK Hull Construction",
            "laminate_approval": "Werften müssen Laminat-Pläne zur Genehmigung einreichen vor Fertigung"
        },
        "germanischer_lloyd": {
            "certifier": "Germanischer Lloyd AG (deutsch, gegründet 1867)",
            "scope": "Kleinere Boote <24m oft ohne Klassifikation (optional)",
            "inspection": "DNV GL (Merger 2013): Inspektionen gemäß GL-Rules"
        }
    }
}


ENVIRONMENTAL_AND_DURABILITY: Dict[str, Any] = {
    "key_de": "Umwelt-Einwirkungen und Haltbarkeit",
    "uv_degradation_mechanisms": {
        "photon_energy_levels": {
            "description_de": "UV-Strahlung (280-400 nm) hat Energie-Quanten, die chemische Bindungen brechen können",
            "uv_a_wavelength_nm": "315-400 nm, Energie ~3.5 eV, schwächer",
            "uv_b_wavelength_nm": "280-315 nm, Energie ~4.0 eV, wirksamer",
            "c_c_bond_energy_ev": "~3.6 eV (leicht zu brechen)",
            "c_h_bond_energy_ev": "~4.3 eV (schwerer zu brechen)",
            "consequence": "UV bricht C-C und C-H Bindungen → Freie Radikale entstehen → Kettenabbau"
        },
        "polyester_degradation": {
            "vulnerable_bonds": ["Ester-Gruppen C(=O)-O-R: sehr anfällig, ~3.3 eV", "Aliphatische C-C: ~3.8 eV anfällig"],
            "consequence": "Polyester wird zerlegt zu kleineren Molekülen (Farbverlust-Chromophoren, Gelbung)",
            "timeline_white_gelcoat": "8-15 Jahre bis noticeable yellowing ohne UV-Schutz",
            "timeline_dark_color": "3-5 Jahre bis deutlicher Farbverlust (dunkle Farben absorbieren UV stärker)"
        },
        "epoxy_resistance": {
            "mechanism": "Ether-Bindungen C-O-C sind UV-stabiler als Ester-Bindungen",
            "consequence": "Standard-Epoxid noch UV-anfällig, aber langlebiger als Polyester",
            "protection_strategy": "Immer Topcoat (Polyurethane, Polysiloxane) über Epoxid verwenden"
        },
        "uv_absorbers": {
            "benzotriazole_compounds": "Umwandelt UV-Energie zu Wärmestrahlung, typisch 0.5-2% Gewicht",
            "hals_hindered_amine": "Hindered Amine Light Stabilizer — fängt freie Radikale ein, typisch 0.3-1% Gewicht",
            "combined_system": "Zusammen geben 20-30 Jahre Schutz (mit Pigmenten), einzeln nur 10-15 Jahre"
        }
    },
    "salt_water_exposure": {
        "chloride_penetration": {
            "mechanism": "Cl⁻ Ionen diffundieren durch Gelcoat und Laminat in mehrschichtigen GFK",
            "diffusion_rate_mm_per_year": "0.05-0.2 mm/Jahr abhängig Harz-Typ und Gelcoat-Dicke",
            "timeline_to_core": "Bei 50 mm Sandwich ohne Barriere: 10+ Jahre bis Kern erreicht wird",
            "consequence": "Chlorid korrodiert metalliche Verstärkungen (Bolzen, Insert) oder Kern-Metalle (Alu-Waben)"
        },
        "osmotic_pressure": {
            "description_de": "Salzkonzentration außen >> Konzentration in Laminat-Poren → Wasser folgt osmotischem Gradienten",
            "timeline_balsa": "5-10 Jahre bis Balsa-Kern merkbar aufquillt (9% Volumen-Expansion möglich)",
            "timeline_pvc": "15-20+ Jahre bei richtigem Gelcoat/Harz-System"
        },
        "corrosion_galvanic": {
            "description_de": "Metallische Komponenten in feuchter Umgebung bilden Galvani-Elemente",
            "stainless_steel_316": "Passivierungsschicht (Cr2O3) schützt, aber Chlorid kann bei >1000 ppm Durchdringen",
            "mild_steel_unschutz": "Rostet schnell in Salzwasser, 0.2-0.5 mm/Jahr Korrosionsrate ohne Anstrich",
            "aluminum_unschutz": "Ähnlich Stahl, 0.1-0.3 mm/Jahr; Anodisierung kann auf 0.001 mm/Jahr reduzieren"
        }
    },
    "temperature_cycling": {
        "coefficient_of_expansion": {
            "gfk_parallel_fibers": "10-15 × 10^-6 /K (relativ niedrig wegen Glas)",
            "gfk_perpendicular": "50-70 × 10^-6 /K (höher, Richtung Harz dominiert)",
            "pvc_foam": "70-100 × 10^-6 /K (höher als GFK)",
            "balsa_wood": "5-10 × 10^-6 /K (niedriger, Holz-dominiert)"
        },
        "stress_from_expansion_mismatch": {
            "example_12m_boat": {
                "delta_temperature_c": 50,
                "gfk_expansion_mm": "Length 11m × 12×10^-6 /K × 50 K = 6.6 mm",
                "pvc_core_expansion_mm": "Thickness 50 mm × 80×10^-6 /K × 50 K = 0.2 mm",
                "differential_strain": "Unterschiedliche Ausdehnungen erzeugen Spannungen 2-5 MPa an Grenzfläche"
            }
        },
        "cumulative_fatigue": {
            "mechanism": "Zyklische Spannungen (täglich Temperatur ±30°C) → Mikrorisse nach 1000+ Zyklen",
            "crack_initiation": "Nach 3-5 Jahren täglicher Sonneneinstrahlung können Mikrorisse kritisch werden",
            "propagation": "Risse wachsen unter Last (Segelwind) → größere Delaminierung möglich"
        }
    },
    "weathering_and_fading": {
        "accelerated_weathering_test_timeline": {
            "astm_g154_1000h": "Entspricht ca. 3-5 Jahren Außenlagerung in südlichem Klima",
            "astm_g154_2000h": "Entspricht ca. 5-10 Jahren Betrieb im Mittelmeerraum oder Mittelmeer",
            "correlation_factor": "Variation je nach UV-Intensität, Temperatur, Luftfeuchtigkeit am Standort"
        },
        "color_stability_ratings": {
            "excellent": "ΔE <2 nach 2000h UV (Weiß, schwarze Farben mit guten Pigmenten)",
            "good": "ΔE 2-5 nach 2000h UV (Blau, Rot, Grün mit Standard-Pigmenten)",
            "fair": "ΔE 5-10 nach 2000h UV (Economy-Farben, schneller Farbverlust sichtbar)",
            "poor": "ΔE >10 nach 2000h UV (unbrauchbar für marine Außenflächen)"
        },
        "pigment_selection": {
            "white_tio2": {
                "type": "Titanium Dioxide (TiO2) rutile structure",
                "stability": "Hervorragend, min. 10 Jahre ohne Vergilbung",
                "advantage": "UV-Reflektor, kühlt Oberfläche",
                "cost": "Basis-Pigment, niedrig"
            },
            "blue_phthalocyanine": {
                "type": "Phthalo Blue (C.I. Pigment Blue 15)",
                "stability": "Gut, 5-7 Jahre ohne sichtbaren Farbverlust",
                "disadvantage": "Absorbiert UV → wärmer, schneller Vergilbung",
                "cost": "Mittel, EUR 8-15/kg"
            },
            "red_iron_oxide": {
                "type": "Iron Oxide Red (Fe2O3, C.I. Pigment Red 101)",
                "stability": "Gut, 5-7 Jahre, dann orange-Verfärbung",
                "advantage": "Preiswert, stabil in Polyester",
                "disadvantage": "Warme Farbe, schneller vergilbt"
            },
            "metallic_aluminum": {
                "type": "Aluminum Flakes (95% rein, 5-30 µm Größe)",
                "stability": "Gut wenn richtig dispergiert",
                "concern": "Silberfarben haben höchste Vergilbungs-Tendenz aller Farben",
                "consequence": "Nach 2-3 Jahren sichtlich mehr grau/trüb"
            }
        }
    },
    "lifetime_expectation": {
        "primary_structure_gluing": {
            "well_maintained_orthophthal": "15-20 Jahre vor osmotischen Problemen sichtbar",
            "well_maintained_isophthal": "20-25 Jahre, mit Barriere-Coat 30+ Jahre",
            "well_maintained_vinylester": "35-45 Jahre bei Sorgfalt",
            "well_maintained_epoxy": "50+ Jahre (theoretisch unbegrenzt, selten getestet)"
        },
        "gelcoat_and_finish": {
            "polyester_gelcoat": "10-15 Jahre bis Crazing sichtbar, 15-20 Jahre bis Wassereintritt-Risiko",
            "polyester_with_topcoat_2kpu": "20-30 Jahre Gelcoat + 15-20 Jahre Topcoat (erneuerbar)",
            "epoxy_gelcoat_with_topcoat": "30-40 Jahre kombined wenn geschützt"
        },
        "sandwich_core": {
            "balsa_with_protection": "15-20 Jahre (hohe Frost-Risiko in kontinentalen Klimazonen)",
            "pvc_h80_with_protection": "25-30 Jahre",
            "pvc_h100_with_protection": "30-40 Jahre",
            "san_corCell_with_protection": "35-50 Jahre"
        },
        "hardware_and_fasteners": {
            "316_stainless_steel": "20-30 Jahre in Salzwasser (Localized pitting nach >10 Jahren möglich)",
            "duplex_2205": "30-40 Jahre, deutlich besser als 316",
            "painted_mild_steel": "3-5 Jahre bevor Rost signifikant, dann progressiv verschlechternd"
        }
    }
}


REPAIR_AND_MAINTENANCE_GUIDE: Dict[str, Any] = {
    "key_de": "Reparatur- und Wartungs-Richtlinien",
    "osmosis_remediation": {
        "stage_1_diagnosis": {
            "inspection": "Ultraschall-Scanning, Sonde-Test (kleine Bohrung durchs Laminat, Feuchtemessung)",
            "affected_area_assessment": "Prozentsatz der betroffenen Rumpf-Fläche ermitteln (z.B. 30% unter Wasserlinie)",
            "severity_grading": [
                "Grad 1: <10% Fläche betroffen, kleine Blasen (<50 mm²), nur kosmetisch",
                "Grad 2: 10-30% Fläche, Blasen bis 200 mm², oberflächliche Wasserdiffusion",
                "Grad 3: 30-50% Fläche, große zusammenhängende Blasen-Bereiche, strukturelle Bedenken",
                "Grad 4: >50% Fläche, Laminat-Delaminierung, Strukturversagen-Risiko"
            ]
        },
        "treatment_options": {
            "stage_1_2_injection": {
                "method": "Epoxid-Harz in Bohrungen (3-5 mm Durchmesser) in betroffene Bereiche spritzen",
                "spacing": "Bohrungen alle 200-300 mm in Gitter-Muster",
                "material": "WEST SYSTEM 105 + 205 oder 3M DP460, 1:1 Mischung",
                "injection_pressure": "2-5 bar (Handpumpen oder kleine elektrische Pumpe)",
                "drying_time_before": "Kern muss 5-10 Tage luftgetrocknet sein (Feuchte <15%), sonst Epoxid-Haftung schlecht",
                "cost": "EUR 30-80 pro m² Rumpf-Fläche (Material + Arbeit)",
                "effectiveness": "Stoppt Osmose-Progression, aber verdrängt nicht alle Flüssigkeit (70-80% Erfolg)"
            },
            "stage_3_blasting_relaminierung": {
                "method": "Gelcoat und äußere Lagen vollständig entfernen, Wasserdampfstrahlen (100 bar), neue Laminierung",
                "removal_depth": "Typisch 3-5 mm wird entfernt (alles betroffene Harz)",
                "after_removal": "7-10 Tage Trocknung erforderlich, Feuchtemessung <12%",
                "new_laminate": "Epoxid-Barriere (3 Lagen) + Gelcoat oder 2K-PU Topcoat",
                "cost": "EUR 200-400 pro m² Rumpf-Fläche",
                "duration": "6-10 Wochen Komplettboots-Projekt"
            },
            "stage_4_full_hull_replacement": {
                "description_de": "Komplette Rumpf-Trennung und Neubau (nur bei totaler Zerstörung oder wirtschaftlich sinnlos)",
                "cost_range": "EUR 50,000-150,000 je nach Bootsgröße (wirtschaftlich nur für Boote <2 Mio Euro Neuwert)",
                "alternative": "Boot abschreiben und verkaufen als Projekt/Wreck"
            }
        },
        "prevention_strategies": {
            "during_construction": [
                "Gelcoat-Dicke min. 0.6-0.8 mm (kein Dünn-Auftrag)",
                "Isophthal oder Vinylester Harz im Außenlaminat verwenden",
                "Barriere-Coat (Epoxid 2-3 Lagen) nach Gelcoat, vor Hauptlaminat"
            ],
            "post_construction": [
                "Annually: Visuelle Inspektion auf Blasen, Risse, Verfärbungen",
                "Alle 3-5 Jahre: UT-Scanning unter Wasserlinie (wenn Boot im Wasser gelagert)",
                "Aufreißen aller Durchdringungen (Bolzen, Rohre) versiegeln mit Epoxid",
                "Winterlagerung an Land (wenn möglich) — reduziert Wasserdiffusion drastisch"
            ]
        }
    },
    "delamination_repair": {
        "detection": {
            "method_1_tap_test": "Mit Gummi-Hammer klopfen, tiefer Ton deutet auf Hohlraum hin",
            "method_2_ut_scan": "Ultraschall-Scanning, zeigt Schicht-Trennung deutlich",
            "method_3_sonde_test": "Kleine Bohrung (2 mm) und Fühler einführen, Widerstand testen"
        },
        "area_preparation": {
            "step_1": "Delaminierte Schicht mit 80er Schleifpapier entfernen (5-10 mm Überstand)",
            "step_2": "Sauberklopfen: Mit Meißel und Hammer lose Teile entfernen (Schlagtechnik kritisch)",
            "step_3": "Trocknung: Min. 7 Tage bei >20°C und <60% Luftfeuchte (kritisch für Epoxid-Haftung!)"
        },
        "relaminierung": {
            "substrate": "Epoxid-Primer (Sikadur Haftungsprimer oder 3M 08693) auf trockenem Untergrund",
            "layers": [
                "CSM 300g + Epoxid 105/205",
                "Roving 450g biaxial ±45° + Epoxid",
                "Roving 450g 0/90° + Epoxid",
                "CSM 200g innerhalb + Epoxid"
            ],
            "cure_time": "7 Tage bei 20°C, oder 3-4 Tage + 80°C Post-Cure/4h"
        },
        "finishing": {
            "surface_prep": "Schleifen 400 → 800 → 1200 Körnung",
            "paint_or_gelcoat": "Optional Gelcoat oder 2K-Polyurethan-Topcoat (empfohlen)",
            "cost_per_m2": "EUR 150-300 abhängig Qualität und Finish"
        }
    },
    "seasonal_maintenance_schedule": {
        "spring_beginning_of_season": {
            "tasks": [
                "Visuelle Überprüfung Rumpf/Deck auf Kratzer, Blasen, Risse",
                "Tap-Test entlang Rumpf-Deck-Linie auf Delaminierung",
                "Polieren und Waxing von Gelcoat (Frühling ist ideal, kühler, höhere Haftung)",
                "Überprüfung aller Hardware: Bolzen auf Rost, Verschraubung straff"
            ]
        },
        "summer_in_season": {
            "tasks": [
                "Monatliche visuelle Inspektionen (schnell, 5-10 Min)",
                "Nach jedem Sturm oder großem Impact: gründliche Überprüfung auf Risse",
                "Gelcoat-Reparaturen kleinerer Kratzer (besser während Saison, nicht später)"
            ]
        },
        "autumn_end_of_season": {
            "tasks": [
                "Gründliche Überprüfung Rumpf (Boot aus dem Wasser oder Hebebock)",
                "Tap-Test Rumpf-Deck-Linie (kritisch vor Winter!)",
                "Wasserdrain-Bohrungen überprüfen (alle Durchdringungen offen?)",
                "Winterschutz: Plane über Deck (verhindert UV-Schaden, Wasserdiffusion)"
            ]
        },
        "winter_storage": {
            "tasks": [
                "Keine aktive Wartung, aber regelmäßige Überprüfung auf Wassereintritt",
                "Frost-Schutz für Boote in kontinentalem Klima: Boot ganz aus dem Wasser",
                "Trocknung: Lüftung im Innern ermöglichen (Frost-Mechanismus verhindert durch Trockenheit)"
            ]
        }
    }
}


ADVANCED_STRUCTURAL_ANALYSIS: Dict[str, Any] = {
    "key_de": "Fortgeschrittene Struktur-Analyse",
    "laminate_theory": {
        "classical_laminate_theory_clt": {
            "description_de": "Klassische Theorie für schichten-Anisotropie, basiert auf Kirchhoff-Platte-Theorie",
            "assumptions": [
                "Dunne Laminate (Dicke/Spannweite < 0.1)",
                "Lineare elastische Material (Spannungen < 50% Ultimum-Festigkeit)",
                "Keine Schub-Verformung (Kirchhoff-Hypothese: Normalen bleiben senkrecht)",
                "Vollständige Verbund zwischen Schichten (perfekte Adhäsion)"
            ],
            "principal_result": "Moment-Krümmungs-Beziehung: {M} = [D] * {k}, wobei [D] = Biegsteifigkeits-Matrix",
            "bending_stiffness_gfk_laminate": {
                "example_quasi_isotropic": {
                "constitution": "45% 0deg, 45% 90deg, 10% ±45deg (vereinfacht)",
                    "dx_nmm2": "2.5e6",
                    "dy_nmm2": "2.3e6",
                    "dxy_nmm2": "0.8e6",
                    "consequence": "Praktisch isotrope Eigenschaften (Boote mit gemischten Lagen-Orientierungen)"
                }
            }
        },
        "failure_criteria": {
            "tsai_wu_criterion": {
                "description_de": "Quadratische Interaktions-Formulierung, berücksichtigt Zug/Druck-Asymmetrie",
                "formula": "F = σ1^2/X1^2 + σ2^2/Y1^2 + 2σ1*σ2/(X1*Y1) + τ12^2/S^2 < 1",
                "where": {
                    "X1": "Zug-Festigkeit 0-Richtung (typisch 1200 MPa Glas/Epoxid)",
                    "Y1": "Zug-Festigkeit 90-Richtung (typisch 50 MPa transversal)",
                    "S": "Schub-Festigkeit (typisch 80 MPa)",
                    "failure_when": "F >= 1.0"
                }
            },
            "hashin_criterion": {
                "description_de": "Vier Versagensarten je nach Spannungs-Richtung und Last-Typ",
                "matrix_tension": "Wenn σ2 > 0: (σ2/Yt)^2 + (τ12/Sl)^2 > 1, Versagen in Matrix",
                "matrix_compression": "Wenn σ2 < 0: (-σ2 / Yc)^2 + (τ12 / Sl)^2 > 1",
                "fiber_tension": "Wenn σ1 > 0: (σ1/Xt)^2 + (τ12/Sl)^2 > 1",
                "fiber_compression": "Wenn σ1 < 0: (-σ1/Xc)^2 > 1",
                "advantage": "Genauer für faserverstarkte Kunststoffe mit unterschiedlichen Faserrichtungen"
            }
        }
    },
    "finite_element_modeling": {
        "typical_boat_fea_mesh": {
            "element_type": "Tri-axial (3-knoten triangular) oder Quad (4-knoten quadrilateral) fuer Shells",
            "shell_element_properties": {
                "in_plane_stiffness": "Membrane-Staerken in x,y Richtungen",
                "bending_stiffness": "Momente M_x, M_y, Torsions M_xy",
                "transverse_shear": "Vernachlaessigt bei Kirchhoff-Schalen (duenne Laminate)"
            },
            "typical_mesh_density": {
                "large_surfaces": "50-200 mm Element-Groesse (schnell, weniger Genauigkeit)",
                "detail_zones": "10-25 mm Element-Groesse (Rumpf-Deck-Uebergang, Mast-Schuh)",
                "elements_per_boat": "20,000-100,000 Elemente fuer komplettes Schiff (inkl. Struktur)"
            },
            "solver_software": [
                "ANSYS (kommerziell, industrie-Standard, EUR 5,000-50,000 Lizenz)",
                "ABAQUS (kommerziel, haeufig in Aerosace, auch Schiffe)",
                "Open Source: Salome-Meca, Code-Aster (frei, unbegrenzte Nutzung)",
                "CATIA V5/V6 (Dassault), integriert CAD+FEA"
            ]
        },
        "material_modeling_composites": {
            "orthotropic_material_input": {
                "elastic_moduli": ["E1 (0-Faser)", "E2 (90-Faser)", "E3 (Dickenrichtung)"],
                "shear_moduli": ["G12 (0/90)", "G13 (0/3)", "G23 (90/3)"],
                "poissons_ratio": ["ν12 (quer-Kontraktion bei Zug 0)", "ν13", "ν23"]
            },
            "gfk_example_properties": {
                "description": "Typische Werte fuer E-Glas/Epoxid 60% Fasergehalt",
                "E1_GPa": 40,
                "E2_GPa": 8,
                "E3_GPa": 6,
                "G12_GPa": 3.5,
                "G13_GPa": 3.5,
                "G23_GPa": 2.5,
                "nu12": 0.25,
                "nu13": 0.30,
                "nu23": 0.35,
                "density_g_cm3": 1.85
            },
            "sandwich_analysis": {
                "method": "Equivalent-Single-Layer (ESL) vs Multi-Layer (ML)",
                "esl_approach": "Dikke Laminate wird als homogenes Material mit gemittelten Eigenschaften behandelt",
                "advantage_esl": "Schnell (ueblicherweise 5-10× schneller als ML)",
                "limitation_esl": "Keine lokalen Spannungen in Kern, nur globale Biegung",
                "ml_approach": "Jede Einzelschicht (Laminate + Kern) wird separat modelliert",
                "accuracy_ml": "Hoechste Genauigkeit fuer lokale Spannungen und Delaminierungs-Kontrolle",
                "cost_ml": "10-100× mehr Rechenzeit je nach Laminate-Komplexitaet"
            }
        },
        "typical_fea_results_hull": {
            "example_30ft_sailboat_under_seaway": {
                "loading": "Wellengang Seegang (statistical 4% Wellenhoehe = 3m Wellen), + Windlast (Segelflaeche)",
                "maximum_bending_stress_mpa": "45-65 MPa im Rumpf-Hauptlaminat (unter Limit 200-300 MPa)",
                "maximum_shear_stress_mpa": "8-12 MPa (unter Limit 60-80 MPa)",
                "maximum_deflection_mm": "15-25 mm in Mittschiffs-Spannweite (elastisch, keine Restverformung)",
                "frequency_analysis_hz": "Erste Eigenfrequenz Rumpf 2-4 Hz, Deck 3-5 Hz",
                "damping_percent": "2-4% strukturale Daempfung (Harz-Verlust, Belastungs-Reibung)"
            },
            "sandwich_core_shear_stress": {
                "maximum_core_shear_mpa": "0.5-1.5 MPa in PVC-Schaumkern",
                "safety_margin": "Kern-Schubfestigkeit 2-3 MPa, also Sicherheitsfaktor 1.5-3.0",
                "critical_zones": "Rumpf-Deck-Ecke, Mast-Partner-Region (hoehere lokale Schub)"
            }
        }
    },
    "creep_and_fatigue": {
        "fatigue_life_prediction": {
            "s_n_curves_gfk": {
                "static_tensile_strength_mpa": "~1000 (typischer Wert)",
                "10e6_cycles_endurance_limit_percent": "40-50% statischer Festigkeit (400-500 MPa)",
                "slope_s_n_curve": "Etwa linear in log-log Darstellung: N = 10^((1000-σ)/k), k ~ 50-70",
                "consequence": "Nach 1 Mio Lastwechsel ist Festigkeit auf 45% reduziert",
                "cumulative_damage": "Miner-Regel (linear): Σ(n_i/N_i) < 1.0 bis Bruch"
            },
            "marine_load_cycles": {
                "typical_sailing_year": "100-150 Tage Segelwind Betrieb",
                "wave_induced_cycles": "0.1-0.3 Hz Wellenfrequenz (eine Welle alle 3-10 Sekunden)",
                "stress_range_per_cycle": "Variiert von Rumpf-Zone zu Zone (Spanten = hoeher)",
                "20_years_total_cycles": "100 Tage * 10^5 Sekunden/Tag * 0.2 Hz = 2 Milionen Zyklen"
            }
        },
        "creep_strain_accumulation": {
            "polyester_creep_coefficient": {
                "definition": "Zusätzliche Dehnung über Zeit bei konstanter Last",
                "example_load": "50% Ultimum-Festigkeit (500 MPa) bei Room-Temp",
                "initial_strain": "0.5% (elastisch)",
                "strain_after_5years": "0.65-0.75% (zusätzlich 0.15-0.25% Kriechung)",
                "strain_after_10years": "0.8-0.95% (sättig sich asymptotisch)"
            },
            "epoxy_vs_polyester": {
                "polyester_relative": "100 (Referenz)",
                "epoxy_relative": "20-30 (deutlich besseres Kriech-Verhalten)",
                "consequence": "Epoxid-Boote behalten Spantform länger, weniger Durchbiegung nach Jahren"
            }
        }
    },
    "impact_and_damage_tolerance": {
        "impact_scenarios": {
            "soft_impact": "Auffahren auf Sandbank (Geschwindigkeit <2 kn), Druck-Spannungen lokal bis 5-10 MPa",
            "moderate_impact": "Stoß auf Felsenformation (5-10 kn), Spannungen 20-50 MPa, Laminat-Kratzer wahrscheinlich",
            "severe_impact": "Kollision mit anderem Boot oder Hindernis (>10 kn), Spannungen >100 MPa, Delaminierung wahrscheinlich",
            "catastrophic": "Sturz-Brecher oder Felsen-Schlag, Rumpf-Loch, Wasser-Eindringung unausweichlich"
        },
        "impact_absorption": {
            "foam_core_benefit": {
                "impact_energy_dissipation": "Schaumkern absorbiert Energie durch Zell-Zusammenpressen",
                "monolithic_gfk": "Nur elastische Rückfederung, wenig Energie-Dämpfung (springt zurück wie Tennisball)",
                "sandwich_gfk": "Kern absorbiert, äußere Laminate verteilt Last, weniger lokale Spannungs-Spitzen",
                "energy_reduction": "30-50% weniger Spitzendruck in Sandwich vs. Monolith gleicher Rumpf-Gesamtgewicht"
            },
            "thickness_effect": {
                "thin_monolith_2mm": "Spitzendruck 300-400 MPa unter Aufprall (sehr kritisch, Bruch wahrscheinlich)",
                "medium_monolith_5mm": "Spitzendruck 100-150 MPa (noch kritisch)",
                "sandwich_3mm_plus_50mm_core": "Spitzendruck 30-50 MPa (sicher, nur oberflächliche Kratzer)"
            }
        },
        "barely_visible_impact_damage_bvid": {
            "marine_context": "Segelboote stoßen häufig auf Hindernisse: Boje, Seetang, Welle-Kante, kleine Felsen",
            "carbon_fiber_risk": "BVID kritisch für CFK-Boote, innere Delaminierung ohne Oberflächenschaden",
            "gfk_robustness": "GFK ist toleranter gegenüber Impact (mehr Energie-Absorption vor Bruch)"
        }
    },
    "manufacturing_tolerances_and_quality": {
        "geometric_tolerances": {
            "hull_planarity": "Rippled oder uneben Rumpf ist normal, Variation ±5-10 mm über 3m Länge akzeptabel",
            "deck_fairness": "Ähnlich, aber sichtbarer (Licht-Reflexion offenbart Unebenheiten)",
            "rumpf_deck_gap": "Typisch 2-5 mm, akzeptabel wenn konsistent; Variation >2mm ist wahrnehmbar"
        },
        "weight_control": {
            "hand_layup_variation": "±10-15% Gewicht-Abweichung zwischen identischen Booten normal",
            "vacuum_infusion_variation": "±5-8% Abweichung (besser kontrolled)",
            "consequence": "Schwere und leichte Exemplare derselben Baureihe können sich in Segeleigenschaften unterscheiden"
        },
        "fiber_waviness": {
            "cause": "Manuelle Platzierung oder Vakuum-Druck erzeugt Wellen in Fasern",
            "consequence": "Reduziert Längsfestigkeit um 10-30% lokal, aber selten strukturell kritisch",
            "detectability": "Schwer zu erkennen ohne zerstörendes Testen (UT-Scanning kann helfen)"
        }
    }
}


HYBRID_AND_ADVANCED_MATERIALS: Dict[str, Any] = {
    "key_de": "Hybrid- und fortgeschrittene Materialien",
    "carbon_glass_hybrid": {
        "rationale": {
            "description_de": "Mischt Carbon (hoher Modul, teuer) mit Glas (guentig, robust)",
            "cost_benefit": "Typ. +20-30% Gewichtsersparnis mit +50% Kostenprämie",
            "structural_optimization": "Carbon in kritischen Zonen (Unterwasserlinie, Mast-Schuh), Glas sonst"
        },
        "typical_hybrid_schedule": {
            "example_12m_hull": [
                "Gelcoat NPG 0.7 mm",
                "CSM 450g + Epoxid (Barriere)",
                "Carbon UD 400g 0deg + Epoxid (hoechste Laengs-Steifigkeit)",
                "Glass 450g Roving ±45deg + Epoxid (Torsion)",
                "Glass 450g Roving 0/90deg + Epoxid",
                "PVC Schaum 60 mm",
                "Glass 450g Roving 0/90deg + Epoxid (innen Spiegelbild)",
                "Glass 450g Roving ±45deg + Epoxid",
                "Glass CSM 300g + Epoxid",
                "Innerseite Oberflaeche"
            ]
        },
        "weight_savings_vs_pure_gfk": {
            "pure_gfk_sandwich": "600 kg Rumpf-Struktur (12m Boot)",
            "gfk_glass_hybrid": "480 kg Rumpf-Struktur (-20%)",
            "cost_delta": "EUR 5,000-8,000 mehr Material+Arbeit",
            "payoff": "Schnellere Boot, bessere Segeleigenschaften, höherer Verkaufspreis"
        }
    },
    "aramid_hybrid": {
        "kevlar_kevlar_49": {
            "description_de": "Aramid-Fasern von DuPont, Zugfestigkeit 3.6 GPa, Modul 130 GPa",
            "advantage": "Hoher Modul, sehr leicht (Dichte 1.44 g/cm3)",
            "disadvantage": "UV-empfindlich, sprodbruechig unter Druck, teuer (EUR 30-60/kg Roving)"
        },
        "typical_use": "Nicht in Boot-Außenlaminat (UV-Problem), nur innen oder mit dichtem UV-Schutz",
        "hybrid_schedule": [
            "Äußeres Laminat: Glas + Carbon wie oben",
            "Kern + innere Lagen: Aramid optional in kompression-gezogenen Zonen"
        ]
    },
    "natural_fiber_composites": {
        "flax_and_other_natural": {
            "description_de": "Bio-Fasern aus Flax, Hanf, Jute als partielle Ersatzstoffe für Glas",
            "sustainability": "Erneuerbar, Lower-Carbon-Footprint als Glas",
            "mechanical_properties": {
                "density_g_cm3": "1.4-1.5 (ähnlich Aramid, leichter als Glas 2.55)",
                "tensile_strength_mpa": "800-1500 (weniger als Glas 3000+)",
                "modulus_gpa": "27-40 (weniger als Glas 70-80)"
            },
            "problems": [
                "Feuchtigkeits-empfindlich (Quellung/Schwindung 5-10%)",
                "Verrottung ohne chemischen Schutz (mikrobiell-anfällig)",
                "Unbegrenzte Haltbarkeit in Salzwasser unklar (noch nicht 20+ Jahre getestet)"
            ],
            "current_status": "Experimentell, nicht in Serienwacht-Yachtbau etabliert (zu viele Fragen)"
        }
    }
}


PRACTICAL_CASE_STUDIES_AND_EXAMPLES: Dict[str, Any] = {
    "key_de": "Praktische Fallstudien und Beispiele",
    "case_study_1_jeanneau_sun_odyssey_45ds": {
        "boat_type": "Cruising Sailboat, 13.7m Länge, 17.5 Tonnen Diplacement",
        "production_years": "2005-2012",
        "hull_construction": {
            "outer_laminate": "Isophthal Polyester Gelcoat 0.6mm + CSM 450g + Roving 600g (0/90) + Roving 600g (±45)",
            "core_material": "PVC Divinycell H80, 50-60mm Dicke",
            "inner_laminate": "Roving 450g (0/90) + Roving 450g (±45) + CSM 300g",
            "barrier_layer": "Vinylester Epoxid-Barriere (2 Lagen) zwischen Gelcoat und Polyester",
            "total_thickness_mm": "60-75mm Sandwich"
        },
        "reported_issues": [
            "Osmose-Blasen ab 8-10 Jahren bei feuchter Lagerung (vor Barriere-Maßnahmen)",
            "Rumpf-Deck-Verbindung: Bolzen-Korrosion bei älteren Modellen (Stahl statt 316 SS)",
            "Deck-Delaminierung selten, normalerweise nur lokal an Hardware-Befestigungen"
        ],
        "owner_feedback_forums": {
            "source": "Jeanneau Owners Forum, CruisersForum.com",
            "longevity": "15+ Jahre mit richtigem Winterschutz problemfrei",
            "maintenance_key": "Jährliche Inspektion, schnelle Reparatur kleinerer Kratzer (Gelcoat)",
            "cost_estimate_repairs": "EUR 2,000-5,000 über 15 Jahre für Durchschnitts-Boot"
        },
        "structural_performance": {
            "bending_stiffness": "Gute Lateral-Steifheit, minimal Durchbiegung unter Segelwind",
            "damping": "Moderately gering (2-3% structural damping), spürbar bei Wellenschlag",
            "noise_levels": "Leichte Knackgeräusche bei Rumpf-Durchbiegung unter Windböe, normal"
        }
    },
    "case_study_2_hanse_315_vacuum_infusion": {
        "boat_type": "Cruising Sailboat, 9.6m, 8.2 Tonnen",
        "production_years": "2008-present",
        "construction_method": "Vacuum Infusion (VARTM)",
        "hull_construction": {
            "method_description": "Trockenes Glaslaminat wird unter Vakuum mit Epoxid infundiert",
            "glass_content_percent": "65-70% (höher als Hand-Laminat 50%)",
            "resin_content_percent": "30-35% (geringer, bessere Festigkeit/Gewicht)",
            "fiber_schedule": [
                "CSM 300g + Epoxid-Barriere",
                "Roving biaxial 450g (0/90)",
                "Roving biaxial 450g (±45)",
                "Roving biaxial 450g (0/90)",
                "PVC Schaum H60 40-50mm",
                "Spiegelbild innen"
            ]
        },
        "performance_vs_hand_layup": {
            "weight_reduction_percent": "-20% vs. Hand-Laminat equivalent",
            "strength_increase_percent": "+15% Zugfestigkeit durch höherer Fasergehalt",
            "cost_increase_percent": "+5-10% wegen Vakuum-Ausrüstung und Process-Kontrolle",
            "quality_consistency": "Deutlich höher, weniger Variation zwischen Exemplaren"
        },
        "reported_longevity": {
            "timeline": "12-15 Jahre Betrieb in Saltwasser (Mittelmeer/Nordeuropa)",
            "osmosis_risk": "Sehr gering (Vakuum-Infusion + Epoxid reduziert Wasserdiffusion massiv)",
            "owner_satisfaction": "Sehr hoch, Hanse gilt als Qualitäts-Werft in der Preisklasse"
        }
    },
    "case_study_3_lagoon_450_catamaran": {
        "boat_type": "Cruising Catamaran, 13.7m, 20 Tonnen",
        "production_years": "2010-present",
        "hull_construction": {
            "method": "Vakuum-Infusion mit PVC Schaum (H80-H100)",
            "two_hulls": "Jeder Rumpf separat laminiert und infundiert, später assembled",
            "structural_connections": [
                "Bridge-Deck: Durchlaminiert (kontinuierliche Lagen von Rumpf zu Rumpf)",
                "Trampoline-Befestigung: Quer-Verstrebung unter Bridge-Deck",
                "Beams: Torsions-steife Verbindung zwischen Rümpfen (kritisch für Seegang)"
            ],
            "core_materials": "Divinycell H80 Standard, H100 in hoher Last-Zonnen"
        },
        "catamaran_specific_challenges": {
            "torsion_loads": "Unsymmetrische Wellen können differenziale Lasten auf zwei Rümpfe erzeugen (große Torsions-Momente)",
            "impact_risk": "Bridge-Deck schlägt häufig gegen Wellen in verwelltem Seegang (Aquaplaning)",
            "delaminierung_risk": "Höher als Monohull wegen dynamischer Lasten und Impact",
            "remedy_design": "Dickere Lagen im Bridge-Deck, hocheres-Modul-Kern (H100 statt H80)"
        },
        "structural_monitoring": {
            "recommended_schedule": "UT-Scanning Bridge-Deck nach 5 Jahren, dann alle 3 Jahre",
            "critical_areas": "Fuß vom Beam zu Rumpf, quer-Spanten unter Bridge-Deck",
            "cost_inspection": "EUR 2,000-4,000 pro Boat für vollständige UT-Überprüfung"
        }
    },
    "case_study_4_bavaria_sailboat_repairs": {
        "company": "Bavaria Yachtbau AG (Giebelstadt, Deutschland)",
        "production_scale": "~1,000 Boote/Jahr (eine der größten deutschen Werften)",
        "typical_issues": [
            "Rumpf-Deck-Verbindung Undichtheit nach 5-7 Jahren (bolted joint problem)",
            "Deck-Delaminierung an hochbelasteten Zonen (Mast-Partner, Winde-Basis)",
            "Gelcoat-Crazing nach 10-15 Jahren, normal und nicht strukturell kritisch"
        ],
        "warranty_policy": {
            "structural": "5 Jahre (reduzierend nach Jahr 3)",
            "gelcoat_osmosis": "10 Jahre bei Einhaltung Wartungs-Vorschriften",
            "exclusions": "Mechanische Beschädigungen, unsachgemäße Wartung, Lagerung im Wasser ganzjährig"
        },
        "service_network": {
            "authorized_dealers": ">50 in Europa",
            "spare_parts_availability": "Gut bis 15 Jahre nach Bau, dann schwierig",
            "technical_support": "Zeichnungen und Gewichts-Angaben verfügbar für klassifizierte Werke"
        }
    },
    "case_study_5_composite_repair_project": {
        "scenario": "15-jährig Beneteau First 405, Osmose-Blasen und Deck-Delamination",
        "owner_location": "Mittelmeer (Kroatien), ganzjährig im Wasser",
        "diagnosis": {
            "ut_scan_result": "35% der Unterwasserlinie betroffen, Blasen 20-50mm Durchmesser",
            "deck_condition": "Delamination 0.5m2 am Mast-Partner",
            "estimated_boat_value": "EUR 80,000 (gebraucht)"
        },
        "repair_options_considered": {
            "option_1_injection_only": {
                "cost": "EUR 8,000-12,000",
                "timeline": "3-4 Wochen",
                "success_rate": "70-80% (stoppt Progression, aber bleibt schwach)",
                "decision": "Nicht empfohlen (Rumpf bleibt porös)"
            },
            "option_2_selective_blasting_and_relaminierung": {
                "cost": "EUR 25,000-35,000",
                "timeline": "8-10 Wochen",
                "scope": "Entfernen der befallenen Schichten, neue Epoxid-Barriere + Gelcoat",
                "success_rate": "95%+ (strukturell wie neu)",
                "owner_decision": "Gewählt, Werft: lokale Turkish Yard in Bodrum"
            },
            "option_3_abandon_boat": {
                "cost": "0 direkt, aber verkaufbar als Projekt-Boot für EUR 20,000-30,000",
                "decision": "Nicht gewählt (Boot ist zu wertvoll, nicht total-loss)"
            }
        },
        "execution": {
            "timing": "Winter 2022, langere Haulout möglich",
            "workflow": [
                "Wasserdampfstrahl-Entfernung Gelcoat + äußere 3mm Laminat",
                "7 Tage Trocknung unter Zelt mit Heizung",
                "Epoxid-Primer + 3 Lagen Epoxid CSM/Roving",
                "NPG Gelcoat + 2K Polyurethan Topcoat",
                "30-Tage-Aushärtung vor Wassereinsatz"
            ]
        },
        "post_repair_condition": {
            "osmosis_risk": "Minimal bei richtigem Schutz, geschätzte Lebensdauer +15-20 Jahre",
            "structural_integrity": "100% wiederhergestellt",
            "cost_recovery": "Boot-Wert gestiegen von EUR 75,000 (vor Reparatur) auf EUR 95,000 nach"
        }
    }
}


QUALITY_ASSURANCE_AND_STANDARDS: Dict[str, Any] = {
    "key_de": "Qualitätskontrolle und Normen",
    "inspection_checkpoints_during_production": {
        "pre_laminierung": [
            "Form-Reinigung und Trennmittel-Auftrag (Kontrolle: visuell, keine Kratzer in Form)",
            "Laminate-Plan-Verifikation (Material-Typ, Schicht-Reihenfolge)",
            "Katalysator und Temperatur-Kontrolle (Topfzeit messen, Aushärtungs-Verlauf)"
        ],
        "during_laminierung": [
            "Schichtdicken-Kontrolle nach jeder 2-3 Lage (Schicht-Messer, Target ±0.5mm)",
            "Blasen-Detektion (Tap-Test oder UT-Scan bei kritischen Zonen)",
            "Harz-Gehalt-Kontrolle (Visual, sollte faserreich aussehen, nicht nass)",
            "Temperatur-Überwachung (Exotherme Spitzen sollten <120°C bleiben)"
        ],
        "post_laminierung_cure": [
            "Aushärtungs-Zeit-Kontrolle (Mindest 24h bei Raumtemperatur oder 4h bei 80°C)",
            "Gelcoat-Dickenprüfung (5+ Punkte pro m2, Target 0.6-0.8mm)",
            "Oberflächenqualität-Kontrolle (Crazing, Risse, Kratzer dokumentieren)"
        ]
    },
    "final_boat_acceptance_testing": {
        "water_tightness": {
            "method": "Hose-Prüfung oder Druckluft-Test unter Oberfläche",
            "acceptance_criterion": "Keine Wasser-Eintritt nach 5-10 min bei Druck 0.5 bar",
            "typical_defects": "Durchdringung (Rohre, Bolzen) nicht versiegelt, Gelcoat-Risse"
        },
        "structural_deflection": {
            "method": "Laden mit Gewichten (Bleisäcke) in Cockpit, Durchbiegung messen",
            "load_typical": "20% von Designgewicht (für 10-Tonnen-Boot: 2 Tonnen Last)",
            "acceptance_criterion": "Durchbiegung <15-20mm, keine permanenten Verformungen nach Entlastung",
            "measurement": "Laser-Nivellier oder Stahllineal mit Lochmarkierung"
        },
        "hull_weight": {
            "method": "Wiegen des leeren Rumpfs auf Großwaage",
            "tolerance": "±5-10% von geplanten Gewicht akzeptabel",
            "exceeded_tolerance_action": "Dokumentieren und Material-Review (zu viel Harz? Fehlerhafte Schichten?)"
        }
    },
    "certification_and_classification": {
        "ce_marking_eu": {
            "requirement": "Boote >2.5m müssen CE-gekennzeichnet sein (EU Directive 94/25/EC, überarbeitet 2023)",
            "manufacturer_responsibility": "Technische Datei mit Tests und Berechnungen muss verfügbar sein",
            "notified_body": "Nur selten beteiligt (max. Kategorie C Boote selbst-zertifiziert)",
            "requirement_for_gfk": "ISO 12215-5 Scantling Design einhalten (oder gleichwertiger Standard)"
        },
        "classification_societies": {
            "lloyd_register": {
                "scope": "Boote >24m, auch kleinere auf freiwilliger Basis",
                "design_approval": "LR Rules für GFK Hulls muss eingehalten sein",
                "hull_survey": "Inspektionen während Bau und nach Indienststellung",
                "cost": "EUR 3,000-10,000 je nach Bootsgröße"
            },
            "bureau_veritas": {
                "scope": "Ähnlich Lloyd's, europaweit verbreitet",
                "additional_requirements": "Material Zertifikate (Harz, Fasern) von anerkannten Herstellern",
                "inspection_frequency": "Annual survey, 5-Jahres-Überprüfung, 10-Jahres-Spezial-Untersuchung"
            }
        }
    }
}


ADDITIONAL_TECHNICAL_REFERENCE: Dict[str, Any] = {
    "key_de": "Zusaetzliche Technische Referenzen",
    "material_suppliers_common_marine": {
        "resin_suppliers": {
            "ashland_chemical": {
                "products": "Polyester & Vinylester Harze",
                "marine_grades": "DERAKANE Vinylester Serie, üblicherweise über Distributoren",
                "geographic_presence": "Weltweit, große Lagerbestaende in Europa"
            },
            "reichhold_chemicals": {
                "products": "Isophthal & Orthophthal Polyester, Gelcoats",
                "marine_certification": "NPG zertifiziert (einige Sorten)",
                "presence": "Hauptsächlich Nordamerika und Europa"
            },
            "swancor_epoxy": {
                "products": "Epoxid-Harze, marine prepreg systems",
                "typical_use": "Rennboote, hochwertige Yachten",
                "cost_premium": "Höchste Kosten, aber beste Qualität"
            }
        },
        "fiber_suppliers": {
            "owens_corning": {
                "products": "E-Glas Roving, CSM, Fabrics",
                "marine_quality": "Hervorragende Verfügbarkeit, Standard-Material für Werften",
                "specification": "OCF brand, größer Durchmesser 15-17 µm"
            },
            "jushi_group": {
                "origin": "China, größter Glashersteller weltweit",
                "quality": "Variabel, einige Grade äquivalent Owens Corning",
                "cost": "20-30% günstiger als europäische Angebote",
                "adoption": "Zunehmend in europäischen Serienwerften"
            },
            "hexcel": {
                "products": "Carbon & Advanced Composites",
                "marine_focus": "Prepreg Systeme für Hochleistung",
                "cost": "Premium, nur in Rennbooten"
            }
        },
        "core_suppliers": {
            "divinycell_basf": {
                "product": "Divinycell H Closed-Cell PVC Foam",
                "grades": "H60, H80, H100, H130",
                "availability": "Weltweit über Distributoren",
                "price_range": "EUR 12-20/dm3 je nach Dichte"
            },
            "airex_3a": {
                "product": "Airex SAN foam (Rohacell rebranded)",
                "performance": "Leicht besser als Divinycell, höherer Preis",
                "adoption": "Premium-Werften (Dufour, Lagoon)"
            },
            "nidaplast": {
                "product": "Balsa-Kerne, endgrain",
                "supplier_region": "Ecuador/Peru, distribuiert weltweit",
                "quality_variabel": "Wichtig zu spezifizieren: Dichte, Feuchte <12% vor Einsatz"
            }
        }
    },
    "calculation_examples": {
        "example_1_simple_beam_bending": {
            "problem": "30ft segelboot unter Segelwind: Maximale Rumpf-Biegung?",
            "given": {
                "length": "9.2m (30 ft)",
                "displacement": "12 Tonnen",
                "sailing_condition": "Outer offshore, Full sail"
            },
            "iso_12215_formula": "M = 0.1 × Δ × L = 0.1 × 12 × 9.2 = 11 kNm",
            "bending_stress": "σ = M / Z, wobei Z = section modulus",
            "laminate_design": {
                "section_modulus_required_cm3": "500-700 cm3 (abhängig Material-Sicherheit)",
                "typical_sandwich": "3mm äußer GFK + 40mm PVC + 3mm innen GFK = ~1200 cm3 (genug)"
            }
        },
        "example_2_core_shear_stress": {
            "problem": "PVC-Kern unter Querlast (Welle schlägt Boot): Schubspannung?",
            "given": {
                "shear_force": "5 kN (von Wellen-Impact)",
                "sandwich_area": "2 m²",
                "core_thickness": "50 mm"
            },
            "shear_stress": "τ = Q / A = 5000 N / (2 m² × 0.05 m) = 50 kPa = 0.05 MPa",
            "acceptance": "PVC H80 Schub-Festigkeit ~ 2 MPa, also Sicherheitsfaktor 40× (massiv über-dimensioniert, normal)"
        }
    }
}



