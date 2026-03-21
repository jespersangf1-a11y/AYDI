"""
Handwerks-Wissensdatenbank — Detailwissen über Verarbeitungstechniken im Yachtbau.

Deckt ab:
- Garne, Fäden, Zwirne (marine-tauglich)
- Stichmuster und Nahttypen
- Material-Naht-Kompatibilität
- Nahtqualitätsbewertung
- Nadeln und Nähwerkzeuge
- Verbindungstechniken (Kleben, Laminieren, Schrauben, Nieten, Schweißen)
- Befestigungselemente (Schrauben, Bolzen, Nieten, Beschläge)
- Oberflächenbehandlung und Finish
"""

from __future__ import annotations

# =============================================================================
# GARNE UND FÄDEN (Thread / Yarn Database)
# =============================================================================

MARINE_THREADS = {
    # --- Polyester (Standard-Marine) ---
    "polyester_v92": {
        "name": "Beschichtetes Polyester V-92",
        "material": "polyester",
        "tex": 300,
        "break_strength_n": 135,
        "uv_resistance_hours": 2000,
        "color_retention": "good",
        "water_absorption_pct": 0.4,
        "melting_point_c": 260,
        "suitable_for": ["canvas", "cockpit_cushions", "bimini", "sprayhood", "lazy_bag"],
        "not_suitable_for": ["segel_hochlast", "dauerhafte_unterwasser", "tragstruktur"],
        "cost_per_m": 0.008,
        "typical_stitch_lengths_mm": [3, 4, 5],
        "needle_sizes": ["#18", "#20", "#22"],
        "notes": "Standard-Marinegarn für Persenning und Cockpitpolster. UV-beschichtet, aber nach 5-7 Jahren Nachrüstung nötig.",
        "assessment_criteria": {
            "excellent": "Gleichmäßige Beschichtung, kein Faserflug, Reißfestigkeit >130N",
            "acceptable": "Leichte Unregelmäßigkeiten, Reißfestigkeit 100-130N",
            "poor": "Beschichtung abblätternd, Fasern sichtbar, Reißfestigkeit <100N",
        },
    },
    "polyester_v138": {
        "name": "Beschichtetes Polyester V-138",
        "material": "polyester",
        "tex": 400,
        "break_strength_n": 200,
        "uv_resistance_hours": 2000,
        "color_retention": "good",
        "water_absorption_pct": 0.4,
        "melting_point_c": 260,
        "suitable_for": ["schwere_persenning", "bimini_verstärkt", "segelreparatur", "polster_hochbelastet"],
        "not_suitable_for": ["feine_innenpolster", "dekorative_nähte"],
        "cost_per_m": 0.012,
        "typical_stitch_lengths_mm": [4, 5, 6],
        "needle_sizes": ["#20", "#22", "#25"],
        "notes": "Schweres Marinegarn für belastete Nähte. Doppelt so stark wie V-92.",
    },
    # --- PTFE / Teflon (Premium) ---
    "ptfe_standard": {
        "name": "PTFE/Teflon Marinegarn",
        "material": "PTFE",
        "tex": 200,
        "break_strength_n": 90,
        "uv_resistance_hours": 15000,
        "color_retention": "excellent",
        "water_absorption_pct": 0.01,
        "melting_point_c": 327,
        "suitable_for": ["segel", "genua", "großsegel", "code_zero", "spinnaker_naht",
                         "hochlast_persenning", "dauerhafte_außennähte", "fensterrahmen_naht"],
        "not_suitable_for": ["kostenoptimierte_projekte"],
        "cost_per_m": 0.045,
        "typical_stitch_lengths_mm": [3, 4, 5],
        "needle_sizes": ["#16", "#18", "#20"],
        "notes": "Goldstandard für Segelnähte. Praktisch kein UV-Abbau, keine Wasseraufnahme. "
                 "Teuer, aber Lebensdauer 3-5x länger als Polyester.",
        "assessment_criteria": {
            "excellent": "Glatte, gleichmäßige Oberfläche, weißer Glanz, kein Ausfransen",
            "acceptable": "Leichte Rauheit, minimale Verfärbung",
            "poor": "Aufgespleißte Fasern, bräunliche Verfärbung, Festigkeitsverlust",
        },
    },
    "ptfe_heavy": {
        "name": "PTFE Schwer (Großsegel/Genua)",
        "material": "PTFE",
        "tex": 400,
        "break_strength_n": 180,
        "uv_resistance_hours": 15000,
        "color_retention": "excellent",
        "water_absorption_pct": 0.01,
        "melting_point_c": 327,
        "suitable_for": ["großsegel_hochlast", "genua_1", "sturmfock", "trysegel",
                         "reffreihen", "verstärkungen", "schothörner"],
        "not_suitable_for": ["leichte_stoffe", "dekorative_nähte"],
        "cost_per_m": 0.080,
        "typical_stitch_lengths_mm": [4, 5, 6],
        "needle_sizes": ["#20", "#22", "#25"],
        "notes": "Für Hochlast-Segelnähte. Verwendet an Schothörnern, Reffreihen, Cunningham-Verstärkungen.",
    },
    # --- Dyneema / UHMWPE (Ultra-Hochfest) ---
    "dyneema_thread": {
        "name": "Dyneema/UHMWPE Hochfestgarn",
        "material": "UHMWPE",
        "tex": 200,
        "break_strength_n": 320,
        "uv_resistance_hours": 5000,
        "color_retention": "moderate",
        "water_absorption_pct": 0.0,
        "melting_point_c": 144,
        "suitable_for": ["regattasegel", "laminatsegel", "strukturnähte", "keder",
                         "schäkel_loops", "gurtband_befestigung"],
        "not_suitable_for": ["bereiche_mit_hitze", "motorseitig", "auspuff_nähe"],
        "cost_per_m": 0.12,
        "typical_stitch_lengths_mm": [3, 4],
        "needle_sizes": ["#16", "#18"],
        "notes": "Höchste Reißfestigkeit aller Marinegarne. Vorsicht: schmilzt bei nur 144°C! "
                 "Nicht in der Nähe von Motoren oder Auspuffanlagen verwenden.",
        "assessment_criteria": {
            "excellent": "Gleichmäßige Oberfläche, keine Fibrillen, volle Festigkeit",
            "acceptable": "Leichte Fibrillenbildung an Umlenkpunkten",
            "poor": "Sichtbare Fibrillen, Durchmesserreduktion, Schmelzspuren",
        },
    },
    # --- Nylon / Polyamid ---
    "nylon_bonded": {
        "name": "Nylon Bonded (Polster/Leder)",
        "material": "nylon_bonded",
        "tex": 150,
        "break_strength_n": 95,
        "uv_resistance_hours": 800,
        "color_retention": "moderate",
        "water_absorption_pct": 4.5,
        "melting_point_c": 220,
        "suitable_for": ["innenpolster", "ledernähte", "teppichkanten", "vorhänge",
                         "innenverkleidung", "kabinentextilien"],
        "not_suitable_for": ["außen_permanent", "segel", "cockpit", "salzwasserkontakt"],
        "cost_per_m": 0.005,
        "typical_stitch_lengths_mm": [2.5, 3, 3.5],
        "needle_sizes": ["#14", "#16", "#18"],
        "notes": "Nur für Innenbereich! Hohe Wasseraufnahme (4.5%) macht es für Außen ungeeignet. "
                 "Exzellent für Lederpolster im Salon.",
    },
    # --- Kevlar/Aramid ---
    "aramid_thread": {
        "name": "Kevlar/Aramid Hochfestgarn",
        "material": "aramid",
        "tex": 250,
        "break_strength_n": 280,
        "uv_resistance_hours": 500,
        "color_retention": "poor",
        "water_absorption_pct": 3.5,
        "melting_point_c": 427,
        "suitable_for": ["strukturnähte_innen", "motorseitige_nähte", "hitzebereich",
                         "feuerfeste_abdeckungen", "maschinenraum_isolierung"],
        "not_suitable_for": ["außen_uv_exponiert", "segel_außenhaut", "dauerbiege"],
        "cost_per_m": 0.09,
        "typical_stitch_lengths_mm": [4, 5, 6],
        "needle_sizes": ["#20", "#22"],
        "notes": "Extrem hitzebeständig (427°C), aber SEHR UV-empfindlich! "
                 "Nur im geschützten Bereich verwenden. Vergilbt und verliert schnell Festigkeit im Sonnenlicht.",
    },
}

# =============================================================================
# STICHMUSTER UND NAHTTYPEN (Stitch Patterns & Seam Types)
# =============================================================================

STITCH_PATTERNS = {
    "geradstich_301": {
        "name": "Geradstich (Lockstitch 301)",
        "iso_designation": "301",
        "thread_count": 2,
        "description": "Standard-Steppstich mit Ober- und Unterfaden. Flachste Naht.",
        "strength_rating": 0.7,
        "flexibility_rating": 0.5,
        "water_tightness": 0.3,
        "suitable_materials": ["segeltuch", "canvas", "sunbrella", "marine_vinyl", "leder", "alcantara"],
        "not_suitable_for": ["hochelastische_stoffe", "neopren", "stark_dehnbar"],
        "typical_applications": ["säume", "flachnähte", "versteifungen", "keder_einfassung"],
        "stitch_length_recommendations": {
            "leichtes_material": {"mm": 2.5, "stitches_per_cm": 4},
            "mittleres_material": {"mm": 3.5, "stitches_per_cm": 3},
            "schweres_material": {"mm": 5.0, "stitches_per_cm": 2},
        },
        "quality_assessment": {
            "oberfaden_spannung": "Stiche gleichmäßig, Verschlingung in der Materialmitte",
            "naht_gerade": "Abweichung max. 1mm auf 10cm",
            "anfang_ende": "Min. 3 Stiche Rückwärtsnähen oder Verriegelung",
            "probleme": [
                "Schlaufenbildung auf Unterseite = Oberfadenspannung zu gering",
                "Oberfaden sichtbar auf Unterseite = Unterfadenspannung zu gering",
                "Fadenabriss = Nadel stumpf oder Fadenführung falsch",
                "Naht kräuselt = Stichlänge zu kurz für Materialstärke",
            ],
        },
    },
    "zickzack_304": {
        "name": "Zickzack-Stich (Zigzag 304)",
        "iso_designation": "304",
        "thread_count": 2,
        "description": "Flexibler Stich, der Dehnung aufnimmt. Standard für elastische Materialien.",
        "strength_rating": 0.6,
        "flexibility_rating": 0.9,
        "water_tightness": 0.4,
        "suitable_materials": ["neopren", "elastische_stoffe", "segeltuch_an_verstärkungen",
                                "scheuerschutz", "gurtband_auf_segel"],
        "not_suitable_for": ["hochlast_strukturnähte", "keder_direkt"],
        "typical_applications": ["segelreparatur", "patch_aufnähen", "elastische_säume",
                                  "webbing_auf_segel", "scheuerschutz_aufnähen"],
        "stitch_length_recommendations": {
            "leichtes_material": {"mm": 2.0, "breite_mm": 3, "stitches_per_cm": 5},
            "mittleres_material": {"mm": 3.0, "breite_mm": 5, "stitches_per_cm": 3},
            "schweres_material": {"mm": 4.0, "breite_mm": 7, "stitches_per_cm": 2.5},
        },
        "quality_assessment": {
            "symmetrie": "Zickzack-Muster gleichmäßig, keine Seitenabweichung",
            "stichbreite": "Konstant über gesamte Nahtlänge",
            "probleme": [
                "Einseitiger Zug = Transporteur ungleichmäßig oder Material verzogen",
                "Stiche greifen nicht = Breite zu schmal für Materialstärke",
                "Material wellt = Stichlänge zu kurz, Material wird zusammengeschoben",
            ],
        },
    },
    "dreifach_zickzack_308": {
        "name": "Dreifach-Zickzack (Triple Zigzag 308)",
        "iso_designation": "308",
        "thread_count": 2,
        "description": "Drei Stiche pro Zickzack-Bewegung. Extrem dehnbar und reißfest.",
        "strength_rating": 0.8,
        "flexibility_rating": 1.0,
        "water_tightness": 0.5,
        "suitable_materials": ["segel", "spinnaker", "gennaker", "neopren", "gurtband"],
        "not_suitable_for": ["feine_innenpolster", "dekorative_nähte"],
        "typical_applications": ["segel_hochlast", "gurtband_befestigung", "spinnaker_nähte",
                                  "dehnbare_verbindungen"],
    },
    "overlockstich_504": {
        "name": "Overlock / Kettelstich (504)",
        "iso_designation": "504",
        "thread_count": 3,
        "description": "Umschlingt die Schnittkante. Verhindert Ausfransen, moderate Festigkeit.",
        "strength_rating": 0.5,
        "flexibility_rating": 0.8,
        "water_tightness": 0.2,
        "suitable_materials": ["teppich", "vorhänge", "innenverkleidung", "leichte_stoffe"],
        "not_suitable_for": ["segel", "außen_hochlast", "canvas_persenning"],
        "typical_applications": ["kantenversäuberung", "teppichkanten", "vorhang_säume",
                                  "innenverkleidung_kanten"],
        "quality_assessment": {
            "kantenumschlingung": "Fäden müssen Kante vollständig umschließen",
            "gleichmäßigkeit": "Fadenspannung auf beiden Seiten identisch",
            "probleme": [
                "Kante rollt = Differentialtransport falsch eingestellt",
                "Schlaufen an Kante = Greiferfadenspannung zu gering",
                "Stoff wird zusammengezogen = Differentialtransport zu stark",
            ],
        },
    },
    "doppelsteppstich_301x2": {
        "name": "Doppelsteppstich / Doppelnaht (2x 301)",
        "iso_designation": "301x2",
        "thread_count": 4,
        "description": "Zwei parallele Geradstiche. Standard für belastete Marine-Nähte.",
        "strength_rating": 0.9,
        "flexibility_rating": 0.5,
        "water_tightness": 0.5,
        "suitable_materials": ["canvas", "segeltuch", "marine_vinyl", "sunbrella",
                                "schweres_leder", "persenning"],
        "not_suitable_for": ["elastische_stoffe_allein"],
        "typical_applications": ["persenning_hauptnähte", "bimini_nähte", "polsterbezüge_belastet",
                                  "markisen", "cockpitverdeck"],
        "stitch_length_recommendations": {
            "standard": {"mm": 4.0, "abstand_mm": 6, "stitches_per_cm": 2.5},
            "hochlast": {"mm": 3.0, "abstand_mm": 8, "stitches_per_cm": 3},
        },
        "quality_assessment": {
            "parallelität": "Beide Nähte exakt parallel, Abstand konstant ±0.5mm",
            "nahtbild": "Beide Reihen identische Stichlänge und Spannung",
            "kreuzungspunkte": "Anfang und Ende beider Nähte verriegelt",
            "probleme": [
                "Nähte laufen zusammen = Materialführung unpräzise",
                "Eine Naht lockerer = Spannungsunterschied zwischen den Nähten",
                "Material verzogen = Beide Nähte in gleicher Richtung genäht statt alternierend",
            ],
        },
    },
    "kappnaht_felled_seam": {
        "name": "Kappnaht / Felled Seam",
        "iso_designation": "felled",
        "thread_count": 4,
        "description": "Eine Stofflage wird umgeklappt und umschließt die andere. "
                       "Stärkste und wasserdichteste textile Naht.",
        "strength_rating": 1.0,
        "flexibility_rating": 0.4,
        "water_tightness": 0.9,
        "suitable_materials": ["segeltuch", "canvas_schwer", "persenning", "technische_textilien"],
        "not_suitable_for": ["dünne_stoffe", "polster", "dekorative_nähte"],
        "typical_applications": ["segel_bahnnähte", "sturmpersenning", "rettungsinsel_hüllen",
                                  "hochlast_canvas"],
        "quality_assessment": {
            "umklappung": "Saubere, gleichmäßige Faltkante, kein Rohmaterial sichtbar",
            "nahtbreite": "Umklappung min. 8mm, besser 12mm",
            "stichdurchgang": "Alle 4 Fäden müssen durch alle Materiallagen gehen",
            "probleme": [
                "Material rutscht aus Falte = Vorfalzen nötig, evtl. Kleber",
                "Ungleichmäßige Faltkante = Material nicht richtig vorgebügelt",
                "Naht bricht auf = Stichlänge zu lang für Materialstärke",
            ],
        },
    },
    "blindstich_103": {
        "name": "Blindstich / Blind Hem (103)",
        "iso_designation": "103",
        "thread_count": 1,
        "description": "Unsichtbare Naht auf der Außenseite. Nur für dekorative Anwendungen.",
        "strength_rating": 0.3,
        "flexibility_rating": 0.7,
        "water_tightness": 0.1,
        "suitable_materials": ["leder", "alcantara", "vorhänge", "feine_polster"],
        "not_suitable_for": ["belastete_nähte", "außen", "segel", "persenning"],
        "typical_applications": ["salonpolster_säume", "vorhänge", "kopfkissen",
                                  "lederverkleidung_kanten"],
    },
    "sattlerstich_hand": {
        "name": "Sattlerstich / Saddle Stitch (Hand)",
        "iso_designation": "hand",
        "thread_count": 2,
        "description": "Handnaht mit zwei Nadeln und gewachstem Garn. Jeder Stich wird von "
                       "beiden Seiten durchgeführt. Stärkste Handnaht — wenn ein Faden reißt, "
                       "hält die Naht trotzdem.",
        "strength_rating": 0.95,
        "flexibility_rating": 0.5,
        "water_tightness": 0.6,
        "suitable_materials": ["leder", "schweres_canvas", "segeltuch", "gurtband"],
        "not_suitable_for": ["massenproduktion", "dünne_stoffe"],
        "typical_applications": ["segelreparatur_vor_ort", "leder_restaurierung",
                                  "gurtband_hochlast", "kauschen_nähen", "beschlag_schlaufen"],
        "quality_assessment": {
            "stichwinkel": "Jeder Stich im exakt gleichen Winkel (45°)",
            "fadenspannung": "Gleichmäßig auf beiden Seiten, leichte Einziehung im Material",
            "stichbild": "Gleichmäßige Abstände, kein Faden sichtbar verdreht",
            "wachsung": "Faden gleichmäßig gewachst, kein Wachsüberschuss an Oberfläche",
            "probleme": [
                "Ungleiche Stichwinkel = Nadel nicht senkrecht durchgeführt",
                "Faden verdreht = Vor jedem Durchzug nicht entwirrt",
                "Stiche zu locker = Faden nach jedem Stich nicht festgezogen",
            ],
        },
    },
}

# =============================================================================
# MATERIAL-NAHT-KOMPATIBILITÄTSMATRIX
# =============================================================================

MATERIAL_STITCH_COMPATIBILITY = {
    "segeltuch_dacron": {
        "recommended_threads": ["ptfe_standard", "ptfe_heavy", "polyester_v138"],
        "recommended_stitches": ["kappnaht_felled_seam", "doppelsteppstich_301x2", "geradstich_301"],
        "stitch_length_mm": 4,
        "needle_type": "cutting_point",
        "needle_size_range": "#18-#22",
        "thread_tension": "medium_high",
        "notes": "Dacron ist verzeihendes Material. PTFE-Garn für maximale Haltbarkeit. "
                 "Kappnaht an Bahnnähten, Doppelsteppstich an Verstärkungen.",
    },
    "segeltuch_laminat": {
        "recommended_threads": ["dyneema_thread", "ptfe_heavy"],
        "recommended_stitches": ["dreifach_zickzack_308", "doppelsteppstich_301x2"],
        "stitch_length_mm": 3,
        "needle_type": "ball_point",
        "needle_size_range": "#14-#18",
        "thread_tension": "low_medium",
        "notes": "VORSICHT: Laminatsegel sind empfindlich! Jedes Nadelloch schwächt die Folie. "
                 "Kugelspitznadel verwenden um Fasern zu verdrängen statt zu schneiden. "
                 "Minimale Stichzahl, dafür hochfeste Garne.",
    },
    "spinnaker_nylon": {
        "recommended_threads": ["polyester_v92", "ptfe_standard"],
        "recommended_stitches": ["dreifach_zickzack_308", "zickzack_304"],
        "stitch_length_mm": 2.5,
        "needle_type": "ball_point",
        "needle_size_range": "#10-#14",
        "thread_tension": "low",
        "notes": "Spinnaker-Nylon ist extrem dünn (30-50g/m²). Feinste Nadeln verwenden. "
                 "Zickzack-Stich MUSS dehnbar sein, da Spinnaker sich stark dehnt.",
    },
    "sunbrella_canvas": {
        "recommended_threads": ["polyester_v92", "polyester_v138"],
        "recommended_stitches": ["doppelsteppstich_301x2", "geradstich_301", "kappnaht_felled_seam"],
        "stitch_length_mm": 4,
        "needle_type": "cutting_point",
        "needle_size_range": "#16-#20",
        "thread_tension": "medium",
        "notes": "Sunbrella ist lösung-gefärbt — Farbe geht nicht durch Nähte verloren. "
                 "UV-beständiges Polyestergarn ist ausreichend. Kappnaht an exponierten Nähten.",
    },
    "marine_vinyl_pvc": {
        "recommended_threads": ["polyester_v92", "nylon_bonded"],
        "recommended_stitches": ["geradstich_301", "doppelsteppstich_301x2"],
        "stitch_length_mm": 3.5,
        "needle_type": "wedge_point",
        "needle_size_range": "#16-#20",
        "thread_tension": "medium",
        "notes": "Keilspitznadel für sauberes Eindringen in PVC-Beschichtung. "
                 "Zu enge Stiche perforieren das Material und Wasser dringt ein!",
    },
    "marine_leder": {
        "recommended_threads": ["nylon_bonded", "polyester_v92"],
        "recommended_stitches": ["geradstich_301", "sattlerstich_hand", "blindstich_103"],
        "stitch_length_mm": 3,
        "needle_type": "cutting_triangle",
        "needle_size_range": "#16-#20",
        "thread_tension": "medium_low",
        "notes": "Dreikantige Schneidnadel für saubere Löcher im Leder. "
                 "Sattlerstich bei Reparaturen und Premium-Polstern. "
                 "PTFE-Garn nur bei Außenleder (Cockpit), innen reicht Nylon.",
    },
    "alcantara_synthetic": {
        "recommended_threads": ["nylon_bonded", "polyester_v92"],
        "recommended_stitches": ["geradstich_301", "blindstich_103"],
        "stitch_length_mm": 2.5,
        "needle_type": "ball_point",
        "needle_size_range": "#12-#16",
        "thread_tension": "low",
        "notes": "Alcantara ist empfindlich — nur Kugelspitznadel! "
                 "Nadelspuren sind auf Mikrofaser sehr sichtbar. "
                 "Farblich passenden Faden verwenden, da Stiche auf Velours sichtbar sind.",
    },
    "teppich_marine": {
        "recommended_threads": ["polyester_v138"],
        "recommended_stitches": ["overlockstich_504", "zickzack_304"],
        "stitch_length_mm": 5,
        "needle_type": "ball_point",
        "needle_size_range": "#18-#22",
        "thread_tension": "medium",
        "notes": "Overlock für Kantenversäuberung ist Pflicht. "
                 "Kugelspitze verhindert Beschädigung der Faserschlaufen.",
    },
    "grp_laminat_bei_reparatur": {
        "recommended_threads": ["dyneema_thread", "ptfe_heavy"],
        "recommended_stitches": ["sattlerstich_hand"],
        "stitch_length_mm": 8,
        "needle_type": "curved_sail",
        "needle_size_range": "#22-#25",
        "thread_tension": "high",
        "notes": "GFK-Reparatur mit Nähten: Nur bei provisorischen Reparaturen auf See! "
                 "Vorbohren mit 1.5mm Bohrer, dann Sattlerstich mit Dyneema. "
                 "Danach mit Epoxid versiegeln.",
    },
    "gurtband_polyester": {
        "recommended_threads": ["polyester_v138", "dyneema_thread"],
        "recommended_stitches": ["doppelsteppstich_301x2", "zickzack_304"],
        "stitch_length_mm": 3,
        "needle_type": "cutting_point",
        "needle_size_range": "#20-#25",
        "thread_tension": "high",
        "notes": "Gurtband an Segeln: Box-Stitch-Muster (Quadrat mit X). "
                 "Mindestens 3 Reihen Doppelsteppstich bei Schothorn-Verstärkungen. "
                 "Dyneema für Regatta, Polyester V-138 für Fahrtensegel.",
    },
}

# =============================================================================
# NADELTYPEN (Needle Types)
# =============================================================================

NEEDLE_TYPES = {
    "cutting_point": {
        "name": "Schneidspitze / Cutting Point",
        "description": "Schneidet das Material beim Durchdringen. Für gewebte Materialien.",
        "suitable_for": ["canvas", "segeltuch_dacron", "sunbrella", "persenning", "schwere_stoffe"],
        "not_suitable_for": ["laminatsegel", "spinnaker", "elastische_stoffe", "strickwaren"],
        "hole_characteristic": "Sauberes, definiertes Loch, selbstschließend bei dichtem Gewebe",
        "risk": "Bei falscher Größe reißt der Faden des Gewebes statt verdrängt zu werden",
    },
    "ball_point": {
        "name": "Kugelspitze / Ball Point",
        "description": "Verdrängt Fasern statt sie zu schneiden. Für Strick- und Laminatmaterialien.",
        "suitable_for": ["laminatsegel", "spinnaker", "neopren", "alcantara", "teppich", "stretch"],
        "not_suitable_for": ["schweres_canvas", "leder", "dickes_segeltuch"],
        "hole_characteristic": "Fasern werden zur Seite geschoben, schließen sich nach dem Durchgang",
        "risk": "Bei zu dichtem Material kann die Nadel abbrechen",
    },
    "wedge_point": {
        "name": "Keilspitze / Wedge Point",
        "description": "Keilförmige Spitze für beschichtete Materialien wie Vinyl und PVC.",
        "suitable_for": ["marine_vinyl", "pvc_beschichtet", "gummi_beschichtet"],
        "not_suitable_for": ["unbehandelte_stoffe", "segel", "leder"],
        "hole_characteristic": "Schneidet sauber durch Beschichtung ohne zu reißen",
    },
    "cutting_triangle": {
        "name": "Dreikant-Schneidspitze / Leather Triangle",
        "description": "Dreikantige Klinge für Leder. Schneidet sauberes dreieckiges Loch.",
        "suitable_for": ["leder", "schweres_leder", "kunstleder_dick"],
        "not_suitable_for": ["stoff", "segeltuch", "vinyl"],
        "hole_characteristic": "Dreieckiges Loch, das sich um den Faden schließt",
        "risk": "Bei zu großer Nadel entstehen sichtbare Perforationen im Leder",
    },
    "curved_sail": {
        "name": "Gebogene Segelnadel / Curved Sail Needle",
        "description": "Halbrunde Nadel für Handnähte an schwer zugänglichen Stellen.",
        "suitable_for": ["segelreparatur", "canvas_reparatur", "polsterreparatur",
                         "gurtband_handnähte"],
        "not_suitable_for": ["maschinenarbeit"],
        "hole_characteristic": "Wie Schneidspitze, aber gebogene Führung für eingeschränkten Zugang",
    },
}

# =============================================================================
# VERBINDUNGSTECHNIKEN — DETAIL (Joining Techniques)
# =============================================================================

JOINING_TECHNIQUES = {
    # --- Kleben (Adhesive Bonding) ---
    "epoxy_structural": {
        "name": "Strukturelles Epoxid-Kleben",
        "category": "adhesive",
        "materials": ["grp", "carbon", "holz", "metall_vorbereitet", "schaum"],
        "strength_mpa": {"shear": 25, "tensile": 40, "peel": 8},
        "temperature_range_c": {"application": [15, 35], "service": [-40, 80]},
        "cure_time_hours": {"handling": 4, "full": 24, "post_cure_optional": 48},
        "surface_preparation": {
            "grp": "Schleifen P80, aceton-entfetten, trocknen 2h",
            "carbon": "Schleifen P120, Plasma-Vorbehandlung oder Schleifvlies, entfetten",
            "holz": "Frische Oberfläche (max 8h alt), staubfrei, Feuchte <12%",
            "metall": "Strahlen SA 2.5, Primer innerhalb 4h, entfetten",
        },
        "quality_criteria": {
            "excellent": "Gleichmäßige Klebschichtdicke 0.2-0.5mm, keine Luftblasen, "
                        "100% Benetzung beider Fügepartner",
            "acceptable": "Klebschichtdicke 0.1-0.8mm, vereinzelte Poren <1mm, >95% Benetzung",
            "poor": "Ungleichmäßige Dicke, sichtbare Lufteinschlüsse, mangelhafte Benetzung",
        },
        "common_failures": [
            {"failure": "Adhäsionsbruch", "cause": "Oberfläche nicht vorbereitet, fettig, feucht",
             "prevention": "Strikte Einhaltung der Oberflächenvorbereitung"},
            {"failure": "Kohäsionsbruch", "cause": "Falsches Mischverhältnis Harz:Härter",
             "prevention": "Exaktes Mischverhältnis nach Datenblatt (Waage!)"},
            {"failure": "Aushärteversagen", "cause": "Temperatur unter 15°C während Aushärtung",
             "prevention": "Heizstrahler, Wärmedecke, Werkstatttemperatur min. 18°C"},
        ],
        "inspection_methods": [
            "Klopftest (Hohlstellen klingen hohl)",
            "Ultraschall (Klebschichtdicke und Porigkeit)",
            "Zerstörende Prüfung an Probestück (Zug, Scherung)",
        ],
    },
    "pu_sealant_bond": {
        "name": "PU-Dichtkleben (Sikaflex-Typ)",
        "category": "sealant_adhesive",
        "materials": ["grp_deck", "holz", "aluminium", "edelstahl", "glas"],
        "strength_mpa": {"shear": 2.5, "tensile": 3, "peel": 4},
        "temperature_range_c": {"application": [10, 35], "service": [-40, 90]},
        "cure_time_hours": {"skin": 0.5, "through": 72},
        "surface_preparation": {
            "grp": "Schleifen P80, Primer je nach Produkt",
            "holz": "Sauber, trocken, grundiert",
            "metall": "Entfetten, Primer zwingend erforderlich",
        },
        "quality_criteria": {
            "excellent": "Durchgängige Raupe ohne Unterbrechung, Dreiecksprofil 2:1 (Breite:Tiefe), "
                        "Primer vollständig abgelüftet",
            "acceptable": "Leichte Unregelmäßigkeiten, Raupe geschlossen",
            "poor": "Unterbrechungen, zu dünn, Primer fehlt",
        },
        "common_failures": [
            {"failure": "Dichtungsversagen an Decksbeschlägen", "cause": "Kein Primer, Oberfläche feucht",
             "prevention": "Primer IMMER verwenden, trockene Oberfläche, min. 10°C"},
            {"failure": "Rissbildung im Dichtstoff", "cause": "Fugengeometrie falsch (zu flach)",
             "prevention": "Optimale Fugengeometrie: Breite = 2× Tiefe"},
        ],
    },
    # --- Laminieren (Lamination) ---
    "wet_layup": {
        "name": "Handlaminat / Wet Layup",
        "category": "lamination",
        "fiber_volume_fraction_pct": {"typical": 30, "good": 35, "excellent": 40},
        "void_content_pct": {"typical": 5, "good": 3, "target": 2},
        "quality_criteria": {
            "faserbenetzung": "Alle Fasern vollständig vom Harz durchdrungen, keine trockenen Stellen",
            "luftblasen": "Keine sichtbaren Blasen >2mm, Rollentechnik bis Blasenfreiheit",
            "überlappung": "Lagen überlappen min. 50mm, versetzt (nicht alle am gleichen Punkt)",
            "harzgehalt": "Laminat darf nicht tropfen (zu viel Harz) oder matt erscheinen (zu wenig)",
            "oberflächengüte": "Gleichmäßig, keine Falten, keine Faserbündel sichtbar",
        },
        "common_failures": [
            {"failure": "Delaminierung", "cause": "Luftblasen zwischen Lagen",
             "prevention": "Jede Lage gründlich rollen, von Mitte nach außen"},
            {"failure": "Faserbrücke an Ecken", "cause": "Fasermatte liegt nicht an Innenecke an",
             "prevention": "Ecken mit Keder (Filler) auffüllen, Matte andrücken"},
            {"failure": "Exothermie-Schaden", "cause": "Zu viele Lagen auf einmal laminiert",
             "prevention": "Max. 4 Lagen auf einmal, dann abkühlen lassen"},
        ],
    },
    "vacuum_infusion": {
        "name": "Vakuuminfusion",
        "category": "lamination",
        "fiber_volume_fraction_pct": {"typical": 50, "good": 55, "excellent": 60},
        "void_content_pct": {"typical": 2, "good": 1, "target": 0.5},
        "quality_criteria": {
            "vakuum": "Min. -0.9 bar, Leckrate <25 mbar/5min",
            "harzfront": "Gleichmäßig von Anguss zu Absaugung, keine trockenen Inseln",
            "temperatur": "Harz und Form auf min. 20°C temperiert",
            "füllzeit": "Innerhalb der Topfzeit des Harzsystems abgeschlossen",
        },
        "common_failures": [
            {"failure": "Trockene Stellen (Dry Spots)", "cause": "Fließhilfe falsch verlegt, Falten in Folie",
             "prevention": "Fließhilfe diagonal verlegen, Folie faltenfrei einziehen"},
            {"failure": "Race Tracking", "cause": "Harz fließt am Rand schneller als in der Mitte",
             "prevention": "Randabdichtung, korrekte Fließhilfengeometrie"},
        ],
    },
    # --- Schrauben (Bolted Joints) ---
    "bolted_structural": {
        "name": "Strukturelle Schraubverbindung",
        "category": "mechanical",
        "materials": ["edelstahl_316", "bronze", "titan"],
        "quality_criteria": {
            "drehmoment": "Angezogen nach Herstellervorgabe mit Drehmomentschlüssel",
            "unterlegscheibe": "Verstärkungsscheibe unter dem Kopf bei GFK (min. ⌀ 3× Bohrung)",
            "dichtung": "Zwischen Beschlag und Deck: Dichtmasse (Sikaflex) oder EPDM-Dichtung",
            "vorbohren": "Bohrung 0.5mm größer als Schaft, keine ausgebrochenen Ränder",
            "galvanische_trennung": "Isolierbuchse bei unterschiedlichen Metallen",
        },
        "common_failures": [
            {"failure": "Ausreißen aus GFK", "cause": "Keine Verstärkungsplatte, zu kleine Unterlegscheibe",
             "prevention": "Edelstahl-Gegenplatte unter Deck, Lastverteilung"},
            {"failure": "Spaltkorrosion unter Beschlag", "cause": "Dichtung fehlt, Wasser unter Beschlag",
             "prevention": "Dichtmassebett, Edelstahl 316L, regelmäßig nachziehen"},
        ],
        "torque_guidelines": {
            "M6_316": {"nm": 8, "note": "Handlauf, Klampe leicht"},
            "M8_316": {"nm": 20, "note": "Klampe mittel, Beschlag"},
            "M10_316": {"nm": 40, "note": "Relingstütze, Winsch"},
            "M12_316": {"nm": 70, "note": "Wantenplatte, Kielbolzen"},
            "M16_316": {"nm": 170, "note": "Kielbolzen schwer, Motorlager"},
        },
    },
    # --- Nieten (Riveted Joints) ---
    "riveted_joint": {
        "name": "Nietverbindung",
        "category": "mechanical",
        "rivet_types": {
            "monel_blind": {
                "name": "Monel-Blindniet",
                "material": "Monel 400 (Nickel-Kupfer)",
                "suitable_for": ["aluminium_auf_aluminium", "edelstahl_auf_aluminium"],
                "not_suitable_for": ["unterwasser_hochlast"],
                "galvanic_note": "Monel ist galvanisch neutral — sicherste Wahl für gemischte Metalle",
            },
            "aluminium_blind": {
                "name": "Aluminium-Blindniet",
                "material": "Aluminium 5052",
                "suitable_for": ["aluminium_auf_aluminium"],
                "not_suitable_for": ["edelstahl_verbindung", "kupfer_verbindung"],
                "galvanic_note": "Nur Aluminium auf Aluminium — sonst galvanische Korrosion",
            },
            "stainless_blind": {
                "name": "Edelstahl-Blindniet",
                "material": "Edelstahl 316",
                "suitable_for": ["edelstahl_auf_edelstahl", "edelstahl_auf_grp"],
                "not_suitable_for": ["aluminium_verbindung"],
                "galvanic_note": "Nicht mit Aluminium kombinieren! Potentialdifferenz >0.5V",
            },
        },
        "quality_criteria": {
            "setzkopf": "Nietsetzkopf bündig, nicht eingerissen, gleichmäßig geformt",
            "bohrung": "Bohrung max. 0.1mm größer als Nietschaft",
            "abstand": "Randabstand min. 2× Nietdurchmesser, Reihenabstand 3-5× Durchmesser",
        },
    },
}

# =============================================================================
# NAHTQUALITÄTS-BEWERTUNGSMATRIX (Seam Quality Assessment)
# =============================================================================

SEAM_QUALITY_ASSESSMENT = {
    "visual_inspection": {
        "name": "Visuelle Nahtinspektion",
        "criteria": [
            {
                "criterion": "Stichlänge",
                "weight": 0.15,
                "excellent": "Alle Stiche exakt gleich lang (±0.3mm), korrekte Länge für Material",
                "good": "Stiche gleichmäßig (±0.5mm), Länge angemessen",
                "acceptable": "Stiche leicht unregelmäßig (±1mm)",
                "poor": "Stiche deutlich ungleichmäßig (>1mm Variation)",
                "critical": "Ausgelassene Stiche, Doppelstiche, chaotisches Bild",
            },
            {
                "criterion": "Fadenspannung",
                "weight": 0.20,
                "excellent": "Verschlingung exakt in Materialmitte, Naht flach, kein Kräuseln",
                "good": "Verschlingung nahe Materialmitte, Naht liegt flach",
                "acceptable": "Leicht einseitige Verschlingung, minimales Kräuseln",
                "poor": "Schlaufen auf einer Seite sichtbar, Naht kräuselt deutlich",
                "critical": "Faden liegt lose auf, hält nicht, Schlaufenbildung",
            },
            {
                "criterion": "Nahtgeradeführung",
                "weight": 0.10,
                "excellent": "Naht folgt exakt der Linie, Abweichung <0.5mm auf 10cm",
                "good": "Naht gerade, Abweichung <1mm auf 10cm",
                "acceptable": "Leichte Wellung, Abweichung <2mm auf 10cm",
                "poor": "Deutliche Wellung, Abweichung >2mm",
                "critical": "Naht mäandert, verfehlt Nähgut stellenweise",
            },
            {
                "criterion": "Anfang und Ende (Verriegelung)",
                "weight": 0.15,
                "excellent": "Saubere Verriegelung (min. 3 Rückwärtsstiche oder Knoten), "
                            "Fäden bündig abgeschnitten, kein Ausfransen",
                "good": "Verriegelung vorhanden, Fäden kurz",
                "acceptable": "Verriegelung vorhanden, Fäden etwas lang",
                "poor": "Verriegelung fehlt an einem Ende",
                "critical": "Keine Verriegelung — Naht kann sich von alleine auflösen",
            },
            {
                "criterion": "Garnqualität und -wahl",
                "weight": 0.20,
                "excellent": "Optimal für Einsatzzweck (z.B. PTFE außen, Nylon innen), "
                            "kein Faserflug, gleichmäßige Dicke, UV-beständig wo nötig",
                "good": "Geeignetes Garn, guter Zustand",
                "acceptable": "Garn geeignet, aber nicht optimal (z.B. Polyester statt PTFE außen)",
                "poor": "Falsches Garn für Anwendung (z.B. Nylon außen)",
                "critical": "Haushaltsgarn, Baumwolle auf Marine-Anwendung — inakzeptabel",
            },
            {
                "criterion": "Nadelwahl passend zum Material",
                "weight": 0.10,
                "excellent": "Nadeltyp exakt passend (Kugel für Laminat, Schneide für Canvas, "
                            "Dreieck für Leder), korrekte Größe",
                "good": "Nadeltyp korrekt, Größe angemessen",
                "acceptable": "Nadeltyp bedingt geeignet, Lochbild akzeptabel",
                "poor": "Falsche Nadel — zu große Löcher oder beschädigte Fasern",
                "critical": "Komplett falsche Nadel — Laminat perforiert, Leder gerissen",
            },
            {
                "criterion": "Nahtdichtheit (bei Außenanwendung)",
                "weight": 0.10,
                "excellent": "Naht mit Nahtdichtband versiegelt ODER Kappnaht ODER "
                            "Dichtmittel in Naht eingearbeitet",
                "good": "Nahttyp ist wasserdicht (Kappnaht) ohne zusätzliche Dichtung",
                "acceptable": "Naht nicht wasserdicht, aber Material darunter schützt",
                "poor": "Offene Naht an exponierter Stelle ohne Schutz",
                "critical": "Wasser dringt direkt durch Naht in Innenraum",
            },
        ],
    },
    "structural_testing": {
        "name": "Nahtfestigkeitsprüfung",
        "methods": [
            {
                "method": "Grab-Test (DIN EN ISO 13934-2)",
                "description": "Manueller Zugversuch an Nahtprobe 100×50mm",
                "pass_criteria": "Naht hält >80% der Materialfestigkeit",
                "typical_values": {
                    "segeltuch_kappnaht_ptfe": "95% der Materialfestigkeit",
                    "canvas_doppelnaht_polyester": "85% der Materialfestigkeit",
                    "vinyl_geradstich_polyester": "75% der Materialfestigkeit",
                    "spinnaker_zickzack_polyester": "70% der Materialfestigkeit",
                },
            },
            {
                "method": "Seam Slippage Test",
                "description": "Prüft ob Material an der Naht verrutscht unter Last",
                "pass_criteria": "Kein Schlupf >3mm bei 50% der Gebrauchslast",
            },
            {
                "method": "UV-Beständigkeitstest",
                "description": "Nahtproben 500h UV-Bestrahlung, dann Zugversuch",
                "pass_criteria": "Reißfestigkeit >70% des Ausgangswerts",
            },
        ],
    },
}

# =============================================================================
# OBERFLÄCHENBEHANDLUNG UND FINISH (Surface Treatment)
# =============================================================================

SURFACE_TREATMENTS = {
    "gelcoat_application": {
        "name": "Gelcoat-Auftrag",
        "target_thickness_mm": {"min": 0.4, "optimal": 0.6, "max": 0.8},
        "quality_criteria": {
            "schichtdicke": "Gleichmäßig 0.5-0.7mm, gemessen mit Nassfilm-Dickenmessgerät",
            "porenfrei": "Keine Pinholes, keine Lufteinschlüsse >0.5mm",
            "farbgleichmäßigkeit": "Keine Schlieren, keine Farbunterschiede",
            "temperatur": "Verarbeitungstemperatur 18-25°C, Formtemperatur ±2°C",
        },
        "common_defects": [
            {"defect": "Pinholes", "cause": "Luft in Gelcoat, zu schnelles Spritzen",
             "prevention": "Gelcoat entgasen, Spritzdruck reduzieren, Kreuzgang-Technik"},
            {"defect": "Ablaufnasen", "cause": "Zu dick aufgetragen, Form nicht waagerecht",
             "prevention": "Max. 0.4mm pro Durchgang, Form waagerecht"},
            {"defect": "Sternrisse (Star Cracking)", "cause": "Gelcoat zu dick oder zu spröde",
             "prevention": "Max. 0.8mm gesamt, flexibilisierten Gelcoat verwenden"},
            {"defect": "Krater", "cause": "Silikonverunreinigung auf Form",
             "prevention": "Form gründlich reinigen, kein Silikon in Werkstatt"},
        ],
    },
    "antifouling_application": {
        "name": "Antifouling-Anstrich",
        "layers": {"primer": 1, "antifouling": 2, "wasserlinie_extra": 1},
        "quality_criteria": {
            "schichtdicke": "Min. 150µm trocken (Gesamtaufbau), Wasserlinie +50µm",
            "overlap": "Mindestens 5cm über vorherige Wasserlinie hinaus",
            "trocknung": "Mindest-Überarbeitungszeit zwischen Schichten einhalten",
            "schliff": "Vorherige Schicht angeschliffen (P180), staubfrei",
        },
    },
    "teak_deck_finishing": {
        "name": "Teak-Deck Endbehandlung",
        "caulking_assessment": {
            "material": "Zweikomponenten-PU (Sikaflex 290 DC Pro oder Simson ISR 70-03)",
            "width_mm": {"min": 3, "optimal": 5, "max": 8},
            "depth_mm": {"min": 4, "optimal": 6},
            "ratio_width_depth": "Optimal 2:1 (Breite:Tiefe)",
            "quality_criteria": {
                "excellent": "Fugen gleichmäßig gefüllt, bündig mit Teak-Oberfläche, "
                            "keine Blasen, Haftung auf beiden Fugenrändern",
                "good": "Fugen gefüllt, leichte Unebenheiten, Haftung ok",
                "acceptable": "Vereinzelte Unebenheiten, keine offenen Stellen",
                "poor": "Ablösung an Fugenkanten, Blasen sichtbar",
                "critical": "Fugen offen, Wasser dringt unter Teak — Kernfäule-Risiko!",
            },
            "common_failures": [
                {"failure": "Adhäsionsverlust an Teakkante", "cause": "Kein Primer, Teak fettig/ölig",
                 "prevention": "Fugenkanten mit Aceton reinigen, Primer auftragen, min. 30min ablüften"},
                {"failure": "Blasen in Fugenmasse", "cause": "Feuchtigkeit im Holz bei Verarbeitung",
                 "prevention": "Nur bei trockenem Holz (<12% Feuchte) verfugen, nie bei Regen"},
                {"failure": "Rissbildung der Fuge", "cause": "Fugengeometrie falsch (zu flach)",
                 "prevention": "Mindesttiefe 4mm, Breite:Tiefe = 2:1"},
            ],
        },
        "oiling_assessment": {
            "product_types": ["Teak-Öl (traditionell)", "Teak-Sealer (modern)", "Unbehandelt (Silber-Patina)"],
            "frequency_months": {"tropen": 3, "mittelmeer": 6, "nordeuropa": 12},
            "quality_criteria": {
                "excellent": "Öl gleichmäßig eingezogen, keine Pfützen, Holz seidig matt, "
                            "kein Kleben nach 24h",
                "poor": "Öl steht auf Oberfläche, klebrig, Staubeinschlüsse",
            },
        },
    },
}

# ============================================================================
# SAIL FABRIC TYPES — Segeltuch-Typen
# ============================================================================

SAIL_FABRICS = {
    "dacron_woven": {
        "name": "Dacron (gewebtes Polyester)",
        "name_de": "Dacron Segeltuch (gewebt)",
        "fiber": "Polyester (PET)",
        "weave": "Taftbindung oder Ripstop",
        "weight_range_g_m2": {"light": 100, "medium": 200, "heavy": 340},
        "stretch_bias_percent": 3.5,
        "stretch_fill_percent": 1.0,
        "uv_resistance": "gut (8-12 Jahre)",
        "cost_rating": 2,
        "typical_use": ["Rollgenua", "Großsegel (Fahrtenyacht)", "Vorsegel"],
        "care": "Spülen mit Süßwasser, nicht im Knicken lagern",
    },
    "laminate_mylar": {
        "name": "Laminat-Segel (Mylar/PET-Film)",
        "name_de": "Laminatsegel (Mylar)",
        "construction": "Faser-Gitter zwischen zwei PET-Folien laminiert",
        "fibers_available": ["Dyneema", "Technora", "Carbon", "Aramid/Kevlar"],
        "stretch_bias_percent": 0.5,
        "uv_resistance": "mäßig (3-6 Jahre, Delamination bei UV)",
        "cost_rating": 4,
        "typical_use": ["Regatta-Großsegel", "Performance-Genua", "Code 0"],
        "failure_mode": "Delamination der Folien — Blasenbildung sichtbar",
    },
    "hydra_net": {
        "name": "Hydra Net (Dyneema® Composite Fabric)",
        "name_de": "Hydra Net (DCF / Cuben Fiber)",
        "construction": "Orientierte Dyneema-Fasern in PE-Matrix laminiert",
        "weight_advantage": "50-70% leichter als Dacron bei gleicher Festigkeit",
        "stretch": "minimal (<0.5%)",
        "uv_resistance": "schlecht — UV-empfindlich, muss geschützt werden",
        "cost_rating": 5,
        "typical_use": ["Leichtwind-Segel", "Gennaker", "Storm-Segel (Gewichtsvorteil)"],
        "sewing_note": "Nicht nähbar — nur geklebt oder ultrasonisch geschweißt",
    },
    "pentex": {
        "name": "PEN (Pentex / Polyethylennaphthalat)",
        "name_de": "Pentex Segeltuch",
        "fiber": "PEN-Faser (30% weniger Stretch als Dacron)",
        "stretch_bias_percent": 2.0,
        "uv_resistance": "gut (besser als Dacron)",
        "cost_rating": 3,
        "typical_use": ["Fahrtensegel mit Performance-Anspruch", "Langfahrt-Großsegel"],
    },
}

# ============================================================================
# MARINE ZIPPERS — Reißverschlüsse für Marine-Anwendungen
# ============================================================================

MARINE_ZIPPERS = {
    "ykk_aquaguard": {
        "name": "YKK AquaGuard®",
        "name_de": "YKK AquaGuard wasserdichter RV",
        "type": "Spiralreißverschluss mit PU-Beschichtung",
        "water_resistance": "wasserdicht (IPX6 getestet)",
        "sizes": ["#5 (Standard)", "#8 (Heavy Duty)", "#10 (Extra Heavy)"],
        "material": "Polyester-Spirale, Zink- oder Kunststoff-Schieber",
        "uv_resistance": "gut",
        "typical_use": ["Sprayhood", "Bimini", "Persenning", "Lazy Bag"],
        "maintenance": "Alle 3 Monate mit Zipper-Wax behandeln",
    },
    "lenzip": {
        "name": "Lenzip Marine",
        "name_de": "Lenzip Marine-Reißverschluss",
        "type": "Zahnreißverschluss (Kunststoff-Vislon)",
        "water_resistance": "spritzwasserdicht",
        "sizes": ["#8", "#10", "#15 (für große Verdecke)"],
        "material": "Delrin-Zähne, Messing-Schieber",
        "advantage": "Robuster als Spirale, einfacher zu reparieren",
        "typical_use": ["Cockpitverdecke", "Dodger", "Bimini-Seitenwände"],
    },
    "ykk_vislon": {
        "name": "YKK Vislon® Marine",
        "name_de": "YKK Vislon Kunststoffzahn-RV",
        "type": "Geformte Kunststoff-Zähne",
        "sizes": ["#5", "#8", "#10"],
        "corrosion_resistance": "ausgezeichnet (kein Metall)",
        "typical_use": ["Segelpersenning", "Segel-Lazy-Bag"],
    },
}

# ============================================================================
# MARINE SNAP FASTENERS — Druckknöpfe
# ============================================================================

MARINE_SNAP_FASTENERS = {
    "loxx_tenax": {
        "name": "Loxx/Tenax",
        "name_de": "Loxx (Tenax) Druckknopf",
        "material": "Messing vernickelt oder Edelstahl",
        "spring_force_n": 25,
        "pull_open_force_n": 50,
        "sizes_mm": [15, 20],
        "base_types": ["Schraube (Holz/GFK)", "Nietbasis", "Stoffbasis (unten)"],
        "advantage": "Höchste Haltekraft, Standard im Yachtbau",
        "installation": "Loch stanzen, Oberteil mit Werkzeug pressen, Unterteil schrauben/nieten",
    },
    "common_sense_dot": {
        "name": "DOT Common Sense",
        "name_de": "DOT Druckknopf",
        "material": "Messing vernickelt",
        "spring_force_n": 15,
        "pull_open_force_n": 30,
        "sizes_mm": [15],
        "base_types": ["Schraube", "Nietbasis"],
        "note": "Günstiger als Loxx, aber geringere Haltekraft",
    },
    "snap_stainless": {
        "name": "Snap Fastener Stainless",
        "name_de": "Druckknopf Edelstahl (Rostfrei)",
        "material": "AISI 316 Edelstahl",
        "corrosion_resistance": "höchste — für Hochsee",
        "typical_use": ["Sonnensegel-Befestigung", "Cockpit-Kissen"],
    },
}

# ============================================================================
# PIPING AND KEDER — Keder und Einziehprofile
# ============================================================================

KEDER_PIPING = {
    "keder_round_6mm": {
        "name_de": "Rundkeder 6mm",
        "material": "PVC-Kern mit Polyester-Fahne",
        "diameter_mm": 6,
        "rail_slot_mm": 7,
        "use": "Standard-Kederleiste für Persenning und Bimini",
        "max_load_n_per_m": 500,
    },
    "keder_round_8mm": {
        "name_de": "Rundkeder 8mm",
        "material": "PVC-Kern mit Polyester-Fahne",
        "diameter_mm": 8,
        "rail_slot_mm": 9,
        "use": "Heavy-Duty Kederleiste, große Verdecke",
    },
    "bolt_rope": {
        "name_de": "Liektau (Bolt Rope)",
        "material": "Polyester-Seil 4-8mm",
        "use": "Segeleinfassung in Mast- und Baum-Nut",
        "sewing": "Eingenäht in Liektasche mit Sattlerstich",
    },
    "flat_keder": {
        "name_de": "Flachkeder",
        "material": "PVC oder Polyester",
        "width_mm": 15,
        "thickness_mm": 3,
        "use": "Kissen-Einfassung, dekoratives Piping",
    },
}

# ============================================================================
# HOOK-AND-LOOP (VELCRO) MARINE — Klettband Marine
# ============================================================================

MARINE_VELCRO = {
    "standard_marine": {
        "name_de": "Klettband Marine UV-beständig",
        "hook_material": "Polyester (UV-stabilisiert)",
        "loop_material": "Polyester-Flausch",
        "width_mm": [20, 25, 50],
        "peel_strength_n_per_25mm": 8,
        "uv_resistance_years": 5,
        "adhesive_type": "Acrylat-Kleber (PSA)",
        "sew_on": True,
        "typical_use": ["Segel-Lazybag-Verschluss", "Cockpit-Kissen-Sicherung"],
        "maintenance": "Regelmäßig von Fusseln befreien, sonst nachlassende Haltekraft",
    },
    "3m_dual_lock": {
        "name_de": "3M Dual Lock (Pilzkopf-Verschluss)",
        "type": "Pilzkopf-Verschluss (kein echtes Klett)",
        "material": "Polypropylen",
        "peel_strength_n_per_25mm": 35,
        "advantage": "5x stärker als normales Klett, definierte Öffnungskraft",
        "typical_use": ["Instrumenten-Befestigung", "Tablet/Chartplotter-Halterung"],
    },
}

# ============================================================================
# FOAM TYPES — Polster-Schaumstofftypen
# ============================================================================

MARINE_FOAM_TYPES = {
    "closed_cell_pe": {
        "name_de": "Geschlossenzelliger PE-Schaum (Plastazote)",
        "density_kg_m3": 45,
        "water_absorption": "0% — nimmt kein Wasser auf",
        "use": "Kissen-Kern Cockpit, Sitzpolster im Außenbereich",
        "compression_hardness_kpa": 8,
        "note": "Komfort begrenzt — eher für Sitz- als Liegepolster",
    },
    "open_cell_pu_marine": {
        "name_de": "Offenzelliger PU-Schaum (Marine-Grade)",
        "density_kg_m3": {"standard": 35, "high_resilience": 50},
        "water_absorption": "Nimmt Wasser auf — Bezug muss wasserdicht sein",
        "use": "Salon-Polster, Kojen-Matratzen, Rückenlehnen",
        "compression_hardness_kpa": {"soft": 3, "medium": 5, "firm": 8},
        "antimicrobial": "Marine-Grade mit Anti-Schimmel-Behandlung",
    },
    "drymesh_spacer": {
        "name_de": "Drymesh / 3D-Abstandsgewirk",
        "thickness_mm": [6, 10, 20],
        "water_absorption": "0% — komplett durchlüftet",
        "use": "Anti-Kondensat-Matratzenauflage, Belüftungsschicht",
        "note": "Kein Polster, sondern Belüftungsunterlage gegen Schimmel",
    },
}

# =============================================================================
# BEWERTUNGSFUNKTIONEN (Assessment Functions)
# =============================================================================

def assess_thread_for_application(thread_id: str, application: str, exposure: str = "outdoor") -> dict:
    """Bewertet ob ein Garn für eine Anwendung geeignet ist."""
    thread = MARINE_THREADS.get(thread_id)
    if not thread:
        return {"suitable": False, "reason": f"Garn '{thread_id}' nicht in Datenbank"}

    score = 50  # Basis
    findings = []

    # UV-Bewertung für Außenanwendung
    if exposure == "outdoor":
        uv_hrs = thread.get("uv_resistance_hours", 0)
        if uv_hrs >= 10000:
            score += 25
            findings.append({"type": "strength", "text": f"Exzellente UV-Beständigkeit ({uv_hrs}h)"})
        elif uv_hrs >= 3000:
            score += 10
            findings.append({"type": "info", "text": f"Gute UV-Beständigkeit ({uv_hrs}h)"})
        elif uv_hrs >= 1000:
            findings.append({"type": "warning", "text": f"Begrenzte UV-Beständigkeit ({uv_hrs}h) — regelmäßige Kontrolle nötig"})
        else:
            score -= 30
            findings.append({"type": "critical", "text": f"Unzureichende UV-Beständigkeit ({uv_hrs}h) — NICHT für Außenanwendung!"})

    # Wasseraufnahme
    water = thread.get("water_absorption_pct", 0)
    if water > 2.0 and exposure == "outdoor":
        score -= 20
        findings.append({"type": "warning", "text": f"Hohe Wasseraufnahme ({water}%) — Festigkeitsverlust bei Nässe"})

    # Anwendungseignung
    suitable = thread.get("suitable_for", [])
    not_suitable = thread.get("not_suitable_for", [])

    if application in not_suitable:
        score -= 40
        findings.append({"type": "critical", "text": f"Garn explizit NICHT geeignet für '{application}'"})
    elif application in suitable:
        score += 20
        findings.append({"type": "strength", "text": f"Garn optimal für '{application}'"})

    return {
        "thread": thread["name"],
        "application": application,
        "exposure": exposure,
        "score": max(0, min(100, score)),
        "suitable": score >= 50,
        "findings": findings,
    }


def assess_stitch_pattern(stitch_id: str, material: str, load_type: str = "normal") -> dict:
    """Bewertet ob ein Stichmuster zu einem Material und Belastungstyp passt."""
    stitch = STITCH_PATTERNS.get(stitch_id)
    if not stitch:
        return {"suitable": False, "reason": f"Stichmuster '{stitch_id}' nicht in Datenbank"}

    compat = MATERIAL_STITCH_COMPATIBILITY.get(material, {})

    score = 50
    findings = []

    # Ist dieses Muster empfohlen für das Material?
    recommended = compat.get("recommended_stitches", [])
    if stitch_id in recommended:
        score += 30
        findings.append({"type": "strength", "text": f"'{stitch['name']}' ist empfohlener Stich für '{material}'"})
    else:
        # Prüfe ob Material in den geeigneten Materialien des Stichs liegt
        suitable = stitch.get("suitable_materials", [])
        not_suitable = stitch.get("not_suitable_for", [])
        if material in not_suitable:
            score -= 40
            findings.append({"type": "critical", "text": f"'{stitch['name']}' ist NICHT geeignet für '{material}'"})
        elif material in suitable:
            score += 10
            findings.append({"type": "info", "text": f"Stich grundsätzlich geeignet, aber nicht erste Wahl"})

    # Belastungsbewertung
    strength = stitch.get("strength_rating", 0.5)
    if load_type == "high" and strength < 0.7:
        score -= 20
        findings.append({"type": "warning", "text": f"Festigkeit ({strength}) gering für Hochlast-Anwendung"})
    elif load_type == "high" and strength >= 0.9:
        score += 15
        findings.append({"type": "strength", "text": f"Hohe Festigkeit ({strength}) — geeignet für Hochlast"})

    return {
        "stitch": stitch["name"],
        "material": material,
        "load_type": load_type,
        "score": max(0, min(100, score)),
        "suitable": score >= 50,
        "findings": findings,
        "recommended_thread": compat.get("recommended_threads", [None])[0],
        "recommended_needle": compat.get("needle_type", "universal"),
    }


def get_full_recommendation(material: str, location: str = "outdoor", load: str = "normal") -> dict:
    """Gibt eine vollständige Verarbeitungsempfehlung für ein Material."""
    compat = MATERIAL_STITCH_COMPATIBILITY.get(material, {})

    if not compat:
        return {"error": f"Kein Kompatibilitätseintrag für '{material}'"}

    threads = [MARINE_THREADS.get(t, {"name": t}) for t in compat.get("recommended_threads", [])]
    stitches = [STITCH_PATTERNS.get(s, {"name": s}) for s in compat.get("recommended_stitches", [])]

    return {
        "material": material,
        "location": location,
        "load": load,
        "recommended_threads": [
            {
                "name": t.get("name", "?"),
                "uv_hours": t.get("uv_resistance_hours", 0),
                "break_strength_n": t.get("break_strength_n", 0),
                "cost_per_m": t.get("cost_per_m", 0),
            }
            for t in threads
        ],
        "recommended_stitches": [
            {
                "name": s.get("name", "?"),
                "strength": s.get("strength_rating", 0),
                "flexibility": s.get("flexibility_rating", 0),
                "water_tightness": s.get("water_tightness", 0),
            }
            for s in stitches
        ],
        "needle_type": compat.get("needle_type", "universal"),
        "needle_size": compat.get("needle_size_range", "unknown"),
        "stitch_length_mm": compat.get("stitch_length_mm", 4),
        "thread_tension": compat.get("thread_tension", "medium"),
        "notes": compat.get("notes", ""),
    }
