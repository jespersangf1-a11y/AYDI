"""
AYDI Wood Craftsmanship Knowledge Base
Master boatbuilder reference for yacht joinery, finishing, and wood working techniques.
40 years of marine woodworking expertise encoded.

All descriptions and technical notes in German for the German yacht design system.
Code comments in English.
"""

# ============================================================================
# WOOD JOINTS FOR MARINE APPLICATIONS
# ============================================================================

WOOD_JOINTS = {
    "scarph_joint": {
        "name": "Schäftung (Scarph Joint)",
        "description": "Scharfkante Verbindung mit überlappender Schäftlinie. Klassische Methode zum Verbinden von Längshölzern wie Kieln, Stringern und Spantköpfen. Längenverhältnis typisch 8-12:1 für volle Festigkeit.",
        "strength_rating": 0.95,
        "water_resistance": "excellent",
        "suitable_for": [
            "keel_extension",
            "stem_scarph",
            "stringers_longitudinal",
            "beam_scarph",
            "gunwale_rail"
        ],
        "tools_required": [
            "sharp_hand_plane",
            "circular_saw_with_guide",
            "belt_sander",
            "marking_gauge",
            "straightedge_3m"
        ],
        "typical_errors": [
            "Schäftlänge zu kurz (Mindestwert 8x Holzdicke)",
            "Ungleichmäßige Pressflächenspannung durch Verformung",
            "Keine Übergangsfasen an den Kanten",
            "Leimauftrag nicht vollständig in der gesamten Kontaktfläche",
            "Holzfeuchte über 15% bei der Verleimung"
        ],
        "quality_criteria": {
            "excellent": "Fugenlinie kaum sichtbar, Druck-Markierung auf gesamter Fläche erkennbar, Spaltung null",
            "good": "Feine Fugenlinie erkennbar, Druck-Markierung auf >90% der Fläche, kein Spalt",
            "acceptable": "Sichtbare Fugenlinie, Druck-Markierung auf >75% der Fläche, Spalte <0.5mm",
            "poor": "Breite Fugenlinie, ungleichmäßige Druckverteilung, Spalte >0.5mm"
        },
        "grain_direction_requirements": "Längsfasern parallel zur Schäftachse. Faserwinkel max. 5° zu Schäftlinie für maximale Festigkeit.",
        "adhesive_recommendation": "Epoxidharz 2-Komponenten (z.B. West System) oder modernes Polyurethan-Holzleim (z.B. Titebond III). Nicht geeignet: Weißleim für ständig feuchte Bereiche.",
        "clamping_time_hours": 24,
        "clamping_pressure_kpa": 800,
        "glue_line_thickness_mm": 0.2,
        "common_failures": [
            "Spaltung durch zu hohe Presswerkzeug-Spannung (>1000 kPa)",
            "Schäftung reißt longitudinal durch Holzfeuchte-Änderung",
            "Leimfuge versagt durch unzureichende Oberflächenrauheit (Ra >3.2)",
            "Wassereindringung an Kanten durch fehlende Versiegelung"
        ],
        "moisture_content_requirement_pct": "9-14%",
        "minimum_scarph_ratio": 8,
        "angle_tolerance_deg": 0.5
    },

    "mortise_tenon": {
        "name": "Zapfenverbindung (Mortise & Tenon)",
        "description": "Klassische Holzverbindung mit rechteckigem Zapfen in passender Öffnung. Für Spanten, Versteifungen und strukturelle Übergänge. Durch die große Leimfläche und die formschlüssige Passung sehr robust und wartbar (nicht verklebt=zerlegbar für Reparaturen).",
        "strength_rating": 0.92,
        "water_resistance": "very_good",
        "suitable_for": [
            "frame_to_timber",
            "beam_stiffeners",
            "deck_beam_connections",
            "cabin_posts",
            "rail_stanchions"
        ],
        "tools_required": [
            "mortise_chisel_set",
            "tenon_saw",
            "sliding_bevel",
            "mortise_gauge",
            "layout_knife"
        ],
        "typical_errors": [
            "Zapfendicke > 1/3 der Balkenbreite → Holzschwächung",
            "Zapfenlänge < 5x Zapfendicke → unzureichende Leimfläche",
            "Schultern nicht plan und parallel → Fugenkluft",
            "Bohrungen zu nah beisammen → Holzausrisse beim Ausstemmeln",
            "Passung zu lose (>0.3mm Spiel) oder zu eng (<-0.1mm)"
        ],
        "quality_criteria": {
            "excellent": "Passung perfekt 0 bis +0.05mm, Schultern vollflächig, keine Rockellawellen",
            "good": "Passung 0 bis +0.1mm, Schultern zu >95% anliegend, minimal Spielraum",
            "acceptable": "Passung 0 bis +0.2mm, Schultern zu >85% anliegend, geringer Spielraum akzeptabel",
            "poor": "Passung >0.2mm oder <-0.05mm, Schultern nicht vollflächig anliegend"
        },
        "grain_direction_requirements": "Zapfen parallel zu Längsfasern; Öffnung quer zur Faser für maximale Formstabilität",
        "adhesive_recommendation": "Epoxidharz oder Hotmelt-Leim für Montage mit sofort hoher Selbstspannkraft. Optional: Trockenfit (ohne Leim) für Zerlegbarkeit.",
        "clamping_time_hours": 12,
        "clamping_pressure_kpa": 500,
        "glue_line_thickness_mm": 0.15,
        "common_failures": [
            "Schub-Versagen des Zapfens durch Scherkräfte parallel zur Faser",
            "Ausrisse an Zapfen-Schultern unter Biegung",
            "Holzfeuchte-Quelling führt zu Zapfen-Druckversagen (Pressspannungen >50 N/mm²)",
            "Formverlust durch zeitabhängiges Kriechverhalten unter Last"
        ],
        "tenon_thickness_ratio": 0.33,
        "tenon_length_ratio": 5.0,
        "tenon_clearance_mm": 0.1,
        "shoulders_required": True
    },

    "dovetail": {
        "name": "Schwalbenschwanz (Dovetail Joint)",
        "description": "Traditionelle Eckverbindung mit Schwalbenschwanz-Profilen. Hauptsächlich für Schreinerarbeiten in Kajüte/Interieur, aber auch für strukturelle Brückensägen-Verbindungen im Schiffsinneren. Hohe Scherfestigkeit, formschlüssig gegen Zug.",
        "strength_rating": 0.88,
        "water_resistance": "good",
        "suitable_for": [
            "cabin_joinery",
            "drawer_construction",
            "interior_cabinetry",
            "bulkhead_assembly",
            "hatch_frames_interior"
        ],
        "tools_required": [
            "dovetail_saw",
            "chisels_1_to_50mm",
            "dovetail_marker_template",
            "sliding_bevel",
            "layout_knife"
        ],
        "typical_errors": [
            "Schwalbenwinkel zu steil (>1:6) → Spaltgefahr bei Quellung",
            "Zapfendicke an Spitze <3mm → Ausbruch-Anfälligkeit",
            "Basenlinie nicht präzise markiert → Höhenunterschiede",
            "Sägelinien nicht lotrecht → Passungsprobleme",
            "Pins zu eng nebeneinander (<8mm) → Schwäche und Ausrisse"
        ],
        "quality_criteria": {
            "excellent": "Alle Zapfen passen spielfrei ein, keine sichtbaren Fugen bei zusammengepresster Verbindung",
            "good": "Zapfen passen mit leichtem Druck, minimale sichtbare Fugen",
            "acceptable": "Zapfen passen, sichtbare Fugen 0.2-0.5mm, erfordern Leimfüllung",
            "poor": "Zu lose oder zu eng, große Fugen oder Blockierungen"
        },
        "grain_direction_requirements": "Längsfasern parallel zu Schwalbenschwanz-Längsachse; Tails und Pins senkrecht zur Schichtebene",
        "adhesive_recommendation": "Epoxidharz oder Holzleim mit langer offener Zeit (30-60 min) zum Zusammenpassen. Optional trocken für Zerlegbarkeit.",
        "clamping_time_hours": 6,
        "clamping_pressure_kpa": 300,
        "glue_line_thickness_mm": 0.2,
        "common_failures": [
            "Ausbruch an Zapfen-Spitzen unter Druck",
            "Schälung unter Biegekräften wenn Winkel zu steil",
            "Schwellung/Quellung führt zu Blockierung und inneren Spannungen",
            "Wasseraufnahme an Fugen-Oberkanten durch fehlende Versiegelung"
        ],
        "dovetail_angle_ratio": 6.0,
        "minimum_pin_thickness_mm": 3,
        "angle_tolerance_deg": 1.0
    },

    "tongue_groove": {
        "name": "Nut und Feder (Tongue & Groove)",
        "description": "Längskante-zu-Längskante Verbindung mit Nut und entsprechender Feder. Standard für Planken-Verlegung, Deckbelags und Verkleidungen. Ermöglicht freie Quellung/Schwindung in Breite ohne sichtbare Fugenöffnung.",
        "strength_rating": 0.85,
        "water_resistance": "excellent",
        "suitable_for": [
            "deck_planking",
            "cabin_lining",
            "hull_planking_secondary",
            "interior_wall_panels",
            "floor_boards"
        ],
        "tools_required": [
            "table_saw_or_spindle_moulder",
            "tongue_groove_cutter_set",
            "circular_saw_for_trimming",
            "straightedge",
            "plane_for_fitting"
        ],
        "typical_errors": [
            "Nut zu tief (>40% Holzdicke) → Schwächung der Stege",
            "Feder zu dick (>60% Nuttiefe) → Blockierung und Spannungen",
            "Rauheit in der Nut >3.2µm → Kratzer und Quellwiderstand",
            "Keine Anpassung an Holzfeuchte-Schwankungen geplant → Spalten oder Unebenheiten",
            "Zu straffe Presspassung → nicht montierbar oder Beschädigungen"
        ],
        "quality_criteria": {
            "excellent": "Planken sitzen plan aneinander, Federn gleiten leicht in Nuten ohne Verkanten",
            "good": "Planken überwiegend plan, Federn passen spielfrei",
            "acceptable": "Planken mit 1-2mm Höhenunterschieden, Federn mit leichtem Spiel 0.2mm",
            "poor": "Sichtbare Stufen oder Spalten, Federn zu locker oder blockiert"
        },
        "grain_direction_requirements": "Längsfasern entlang der Planken-Länge; Nut-Tiefe mit Jahrringsystem für stabiles Verhalten",
        "adhesive_recommendation": "Optional: Epoxidharz-Dünnschicht auf Feder für dauerhaften Halt. Normalerweise trocken verlegt.",
        "clamping_time_hours": 0,
        "dry_fit_installation": True,
        "common_failures": [
            "Quellung führt zu Fugen-Öffnung (bis 5mm bei extremer Feuchteänderung)",
            "Feder reißt unter Quellspannung → Lockerung und Wasseraufnahme",
            "Rauheit in der Nut sammelt Schmutz und Algen (besonders unter Deck)",
            "Druckstellen an Federn-Übergängen bei unebener Unterkonstruktion"
        ],
        "groove_depth_ratio": 0.4,
        "tongue_thickness_ratio": 0.6,
        "clearance_mm": 0.2,
        "surface_finish_ra_um": 1.6
    },

    "butt_joint": {
        "name": "Stumpfstoß (Butt Joint)",
        "description": "Einfachste Verbindung: zwei Holzflächen stoßen aneinander. Minimale Leimfläche, daher bei Yachten nur für unkritische Stellen mit Verstärkungsplatte/Biscuit/Dübel. Wird oft durch bessere Methoden ersetzt.",
        "strength_rating": 0.50,
        "water_resistance": "poor",
        "suitable_for": [
            "non_structural_panels",
            "backing_blocks",
            "simple_blocking",
            "temporary_assemblies"
        ],
        "tools_required": [
            "miter_saw",
            "table_saw",
            "straightedge",
            "clamps_multiple"
        ],
        "typical_errors": [
            "Oberflächen nicht plan und parallel → Spalten in der Leimfuge",
            "Keine Verstärkung → sofortiges Versagen unter Schub",
            "Oberflächenrauhheit <0.8µm (zu glatt) → Leimhaftung unzureichend",
            "Leimauftrag einseitig → ungleichmäßige Verfestigung",
            "Holzfeuchte>16% → Quellung und Pressspannungs-Ausfall"
        ],
        "quality_criteria": {
            "excellent": "Nicht verwendet für strukturelle Anwendungen",
            "good": "Nicht verwendet für strukturelle Anwendungen",
            "acceptable": "Mit innerer Verstärkung (Biscuit/Lamelle, Dübel, Platte) für unkritische Stellen",
            "poor": "Ohne Verstärkung unzureichend"
        },
        "grain_direction_requirements": "Längsfasern sollten parallel zur Stoßebene laufen für maximale Haltbarkeit",
        "adhesive_recommendation": "Epoxidharz mit Verstärkungsplatte dahinter notwendig. Allein-Leimung unzureichend.",
        "clamping_time_hours": 24,
        "reinforcement_required": True,
        "common_failures": [
            "Leimfugen-Versagen durch minimale Kontaktfläche (nur Linienkontakt)",
            "Schub-Rutschung beider Teile gegeneinander bei Belastung",
            "Wasser-Eindringung an den Stirnflächen",
            "Holzfeuchte-Bewegung erzeugt innere Spannungen und Risse"
        ]
    },

    "rabbet_joint": {
        "name": "Falzverbindung (Rabbet Joint)",
        "description": "L-förmig ausgesparte Verbindung mit Stufe zur Erhöhung der Leimfläche und Formschluss. Für Ecken, Kanten und Futter-Befestigungen. Bessere Alternative zum Stumpfstoß.",
        "strength_rating": 0.72,
        "water_resistance": "very_good",
        "suitable_for": [
            "cabin_framing",
            "hatch_assembly",
            "trim_attachment",
            "door_frame_assembly",
            "cabinet_corners"
        ],
        "tools_required": [
            "table_saw_with_rabbet_head",
            "router_with_rabbet_bit",
            "hand_plane",
            "marking_gauge",
            "straightedge"
        ],
        "typical_errors": [
            "Falz-Tiefe zu tief (>50% Materialstärke) → Schwächung",
            "Stufenhöhe nicht einheitlich → unebene Oberflächen",
            "Rauhheit in Falz >3.2µm → Kratzer und Wassersammlung",
            "Keine Anpassung an Quellung geplant → Spalten oder Verformung",
            "Zu enge Pressung → Holzausrisse an Innenkanten"
        ],
        "quality_criteria": {
            "excellent": "Falz präzise, beide Teile bündig aneinander, keine Stufen",
            "good": "Falz präzise, minimale Stufen <0.2mm",
            "acceptable": "Falz vorhanden, Stufen <0.5mm, erfordern minimales Nachschleifen",
            "poor": "Unregelmäßige Falz oder große Höhenunterschiede"
        },
        "grain_direction_requirements": "Längsfasern sollten mit Falz-Kanten ausgerichtet sein für saubere Bearbeitung",
        "adhesive_recommendation": "Epoxidharz oder moderner Polyurethan-Holzleim. Ausreichende Haftung durch Formschluss.",
        "clamping_time_hours": 12,
        "clamping_pressure_kpa": 400,
        "glue_line_thickness_mm": 0.2,
        "common_failures": [
            "Spaltung an der Falz-Innenkante unter Zug",
            "Quellung führt zu Versatz und Stufen-Bildung",
            "Wasser-Eindringung an Falz-Oberkante (horizontal exponiert)",
            "Leimfugen-Versagen bei unzureichender Oberflächen-Vorbereitung"
        ],
        "rabbet_depth_ratio": 0.4,
        "rabbet_width_ratio": 0.8
    },

    "splined_joint": {
        "name": "Federverbindung (Splined Joint)",
        "description": "Zwei zueinander senkrechte Teile werden durch eingeklebte Holzfedern verbunden. Federn laufen mit Faserlänge für maximale Stabilität. Für Eck- und T-Verbindungen in Spanten, Versteifungen und Rahmenbau.",
        "strength_rating": 0.90,
        "water_resistance": "excellent",
        "suitable_for": [
            "frame_connections",
            "structural_joints",
            "T_joints",
            "corner_assemblies",
            "bulk_attachment"
        ],
        "tools_required": [
            "router_with_slot_cutter",
            "table_saw_for_spline_milling",
            "straightedge",
            "sliding_bevel",
            "clamps_multiple"
        ],
        "typical_errors": [
            "Slot zu tief (>50% Holzdicke) → Schwächung beider Teile",
            "Federn zu dünn (<3mm Dicke) → Bruchgefahr beim Eintreiben",
            "Slot-Rauheit >3.2µm → Schwierige Installation und Kratzer",
            "Keine Anpassung an Quellung geplant → Pressspannungen und Risse",
            "Federn-Länge nicht ausreichend (min. 3x Holzdicke)"
        ],
        "quality_criteria": {
            "excellent": "Federn sitzen spielfrei und bündig mit Oberflächen, kein Spiel",
            "good": "Federn sitzen spielfrei, geringer Höhenunterschied <0.1mm",
            "acceptable": "Federn sitzen, geringe Höhenunterschiede <0.3mm, erfordern Nachschleifen",
            "poor": "Federn zu locker oder zu eng, große Höhenunterschiede"
        },
        "grain_direction_requirements": "Federn-Längsfasern parallel zu Slots für Formstabilität. Slots senkrecht zu Oberflächen.",
        "adhesive_recommendation": "Epoxidharz oder Polyurethan-Holzleim. Dünnschicht-Auftrag auf Federn-Seitenflächen.",
        "clamping_time_hours": 12,
        "clamping_pressure_kpa": 400,
        "glue_line_thickness_mm": 0.15,
        "common_failures": [
            "Federn reißen längs unter zu hohem Pressdruck oder Quellung",
            "Ausrisse an Slot-Kanten durch zu scharfe Fräser oder Pressung",
            "Wasser-Eindringung an Slot-Oberkanten (z.B. Deck-Anschlüsse)",
            "Leimversagen durch unzureichende Slot-Oberflächenrauheit"
        ],
        "slot_depth_ratio": 0.4,
        "spline_thickness_ratio": 0.5,
        "spline_length_ratio": 3.0
    },

    "laminated_bend": {
        "name": "Leistenlaminat / Kaltverformung (Laminated Bend)",
        "description": "Mehrschichtige, dünne Holzstreifen (Lamellen) werden gebogen und zusammengepresst. Ermöglicht kleinere Krümmungsradien als Dampfbiegung. Verwendet für Spanten, Deckenspringe, Rahmen-Biegungen.",
        "strength_rating": 0.88,
        "water_resistance": "excellent",
        "suitable_for": [
            "curved_frames",
            "deck_beams_curved",
            "coaming_bends",
            "rail_bends",
            "structural_curves"
        ],
        "tools_required": [
            "lamination_press_or_clamps",
            "bend_mold_form",
            "table_saw_for_lamella_milling",
            "layout_tools",
            "measurement_devices"
        ],
        "typical_errors": [
            "Lamellen zu dick (>3mm) → Bruchgefahr beim Biegen",
            "Krümmungsradius zu klein → Rissgefahr oder Bruch",
            "Leimauftrag ungleichmäßig → Delamination später",
            "Pressdruck zu hoch (>1200 kPa) → Ausrisse oder Verformung",
            "Holzfeuchte zu niedrig (<9%) → Bruchgefahr; zu hoch (>16%) → Quellung"
        ],
        "quality_criteria": {
            "excellent": "Laminat hält Form perfekt, keine Risse oder Delamination, gleichmäßige Krümmung",
            "good": "Laminat hält Form, minimale Risse <100mm, kaum Delamination",
            "acceptable": "Laminat weitgehend stabil, kleine Risse oder Delamination an Kanten erlaubt",
            "poor": "Laminat verzogen, Risse oder Delamination signifikant"
        },
        "grain_direction_requirements": "Längsfasern parallel zur Lamellen-Längsachse für maximale Biegefestigkeit",
        "adhesive_recommendation": "Epoxidharz oder Polyurethan-Leim mit Zwangsclips/Presswerkzeug. Auftrag auf beide Seiten.",
        "clamping_time_hours": 24,
        "clamping_pressure_kpa": 800,
        "glue_line_thickness_mm": 0.2,
        "common_failures": [
            "Delamination durch unzureichenden Leimauftrag oder Pressdruck",
            "Längsspannungen führen zu Rissen quer zur Faser",
            "Quellung/Schwindung führt zu Verformung nach dem Pressen",
            "Bruch beim Abheben aus der Form wenn Radius zu klein"
        ],
        "minimum_radius_mm": 300,
        "lamella_thickness_mm": 2,
        "lamella_thickness_ratio": 30,
        "moisture_content_requirement_pct": "10-14%"
    },

    "epoxy_scarf": {
        "name": "Epoxid-Schäftung (Epoxy Scarph)",
        "description": "Moderne Variante der Schäftung mit Epoxidharz-System, oft mit Glasfaser-Verstärkung. Ermöglicht schmalere Schäfte (4-6:1 Verhältnis statt 8-12:1). Standard in modernem Yachtbau.",
        "strength_rating": 0.98,
        "water_resistance": "excellent",
        "suitable_for": [
            "keel_and_stem",
            "mast_scarf",
            "structural_beams",
            "spars",
            "longitudinal_stiffeners"
        ],
        "tools_required": [
            "power_planer_or_thickness_planer",
            "circular_saw_with_guide",
            "vacuum_bag_or_clamp_frame",
            "epoxy_mixing_and_application_kit",
            "heat_source_for_cure_acceleration"
        ],
        "typical_errors": [
            "Epoxid-Verhältnis nicht exakt (falsches Gemisch) → unvollständige Aushärtung",
            "Holz-Oberfläche zu glatt (Ra <0.8µm) → schlechte mechanische Verankerung",
            "Schaft-Winkel zu klein (<10°) → Rissempfindlichkeit",
            "Temperatur bei Aushärtung <15°C oder >30°C → verlängerte Aushärtung oder Schäden",
            "Druck ungleichmäßig angewendet → Luftblasen oder trockene Stellen"
        ],
        "quality_criteria": {
            "excellent": "Fugenlinie kaum sichtbar, keine Luftblasen, volle Farbdurchdringung, Hochglanz-Oberflächenfinish",
            "good": "Feine Fugenlinie, wenige Luftbläschen, gleichmäßige Färbung",
            "acceptable": "Sichtbare Fugenlinie, kleine Luftbläschen erlaubt, kann überschliffen werden",
            "poor": "Große Luftblasen, Trennung, fehlende Verfestigung"
        },
        "grain_direction_requirements": "Längsfasern parallel zur Schäftachse. Schäft-Winkel min. 10°, ideal 12-15°.",
        "adhesive_recommendation": "Zweikomponenten-Epoxidharz mit langer offener Zeit (30-60 min). Optional mit Glasfaser-Gewebe verstärkt.",
        "clamping_time_hours": 24,
        "clamping_pressure_kpa": 600,
        "glue_line_thickness_mm": 0.3,
        "common_failures": [
            "Risse entlang der Fugenlinie durch Spannungskonzentration",
            "Wassereindringung an Fugenkanten wenn nicht richtig versiegelt",
            "Ausfall durch UV-Einstrahlung (ungeschützte Epoxid-Oberflächen)",
            "Thermisches Versagen durch Temperaturgradienten in Schäft-Ecken"
        ],
        "scarph_ratio": 6,
        "scarph_angle_deg": 12,
        "epoxy_pot_life_min": 45,
        "cure_temperature_range_c": [15, 25]
    },

    "biscuit_joint": {
        "name": "Lamellenverbindung (Biscuit Joint)",
        "description": "Kleine linsenförmige Holzlamellen (Biscuits) werden in Slots in zwei Werkstücke eingeleimt. Einfach und schnell, aber nur für Oberflächen-Verbindungen, nicht für strukturelle Lasten.",
        "strength_rating": 0.60,
        "water_resistance": "good",
        "suitable_for": [
            "edge_joining",
            "flat_panel_assembly",
            "furniture_joints",
            "non_structural_alignment"
        ],
        "tools_required": [
            "biscuit_jointer_machine",
            "clamps_multiple",
            "marking_gauge",
            "straightedge"
        ],
        "typical_errors": [
            "Biscuits zu nah beieinander (<50mm Abstand) → zu viel Material entfernt",
            "Slots nicht aligned → Werkstücke versetzen sich",
            "Zu viel Leim-Auftrag → Quellung und Versatz",
            "Pressdruck ungleichmäßig → Höhenunterschiede",
            "Feuchtigkeit zu hoch (>15%) → extreme Quellung der Biscuits"
        ],
        "quality_criteria": {
            "excellent": "Fugen spielfrei und plan, kein Versatz, Biscuits kaum sichtbar",
            "good": "Fugen spielfrei, minimaler Versatz <0.2mm",
            "acceptable": "Fugen mit geringem Spiel, Versatz <0.5mm erfordert Nachschleifen",
            "poor": "Versatz oder Höhenunterschiede >0.5mm"
        },
        "grain_direction_requirements": "Längsfasern parallel zu Biscuit-Längslänge für maximale Haltung",
        "adhesive_recommendation": "Standard-Holzleim oder Polyurethan-Leim mit kurzer offener Zeit (10-15 min).",
        "clamping_time_hours": 6,
        "clamping_pressure_kpa": 300,
        "glue_line_thickness_mm": 0.2,
        "common_failures": [
            "Biscuits quellen asymmetrisch → Werkstücke versetzen sich",
            "Slots zu tief oder zu nah an Kanten → Ausrisse",
            "Leimversagen bei zu niedriger Holzfeuchte (<8%) oder zu hoher (>16%)",
            "Schubversagen unter Längskräften"
        ],
        "biscuit_spacing_mm": 150,
        "slot_depth_mm": 20
    },

    "finger_joint": {
        "name": "Keilzinkenverbindung (Finger Joint)",
        "description": "Mehrere kleine Zapfen und Öffnungen alternierend (wie verflochtene Finger). Hohe Leimfläche und Formschluss. Industrielle Methode für Längenverlängerung in modernen Yachten.",
        "strength_rating": 0.93,
        "water_resistance": "excellent",
        "suitable_for": [
            "beam_lengthening",
            "structural_elongation",
            "large_timber_assembly",
            "mast_scarph_alternative",
            "composite_beam_building"
        ],
        "tools_required": [
            "finger_joint_cutter_machine",
            "tenoning_machine",
            "press_or_clamp_frame",
            "alignment_jigs"
        ],
        "typical_errors": [
            "Finger-Pitch nicht korrekt (>20mm für dünne Hölzer) → zu wenige Kontaktflächen",
            "Finger-Tiefe zu groß (>40% Holzdicke) → Schwächung",
            "Oberflächenrauheit >3.2µm → schlechte Haftung",
            "Pressdruck ungleichmäßig → manche Finger klaffend",
            "Holzfeuchte nicht angepasst → massive Quellung und Risse"
        ],
        "quality_criteria": {
            "excellent": "Alle Finger sitzen spielfrei, keine Klaffungen oder Risse, ebene Oberfläche",
            "good": "Finger sitzen spielfrei, minimale Klaffung <0.1mm",
            "acceptable": "Finger sitzen mit sehr leichtem Spiel, Klaffung <0.3mm",
            "poor": "Lose Finger oder große Klaffungen"
        },
        "grain_direction_requirements": "Längsfasern parallel zu Finger-Längsachse für maximale Scherungsresistenz",
        "adhesive_recommendation": "Epoxidharz oder hochwertige Polyurethan-Leim mit langer offener Zeit (45-60 min).",
        "clamping_time_hours": 24,
        "clamping_pressure_kpa": 800,
        "glue_line_thickness_mm": 0.2,
        "common_failures": [
            "Quellung führt zu Rissen zwischen Fingern",
            "Scherkräfte parallel zur Faser verursachen Spannungskonzentration an Finger-Ansätzen",
            "Wasser-Eindringung an Finger-Spitzen (wenn horizontal)",
            "Ungleichmäßige Presswerkzeug-Spannung führt zu lokalen Ausfällen"
        ],
        "finger_pitch_mm": 15,
        "finger_depth_ratio": 0.4,
        "finger_minimum_thickness_mm": 4
    },

    "half_lap": {
        "name": "Überblattung (Half Lap Joint)",
        "description": "Zwei Teile werden gleich tief eingefräst (jeweils 50% der Holzdicke), sodass sie plan nebeneinander liegen. Für kreuzende Balken, Rahmen-Ecken und Versteifungen.",
        "strength_rating": 0.82,
        "water_resistance": "very_good",
        "suitable_for": [
            "crossing_beams",
            "frame_corners",
            "deck_beam_assembly",
            "stiffener_attachment",
            "framing_intersections"
        ],
        "tools_required": [
            "table_saw_with_depth_stop",
            "router_with_straight_bit",
            "sliding_bevel",
            "straightedge",
            "marking_gauge"
        ],
        "typical_errors": [
            "Tiefe nicht genau 50% (z.B. 45% oder 55%) → Unebenheiten",
            "Schnittkanten nicht senkrecht → Rockellawellen",
            "Oberflächenrauheit >3.2µm → schlechte Passung und Haftung",
            "Keine Anpassung an Quellung geplant → Pressspannungen",
            "Pressdruck ungleichmäßig → teilweise Lufteinschlüsse"
        ],
        "quality_criteria": {
            "excellent": "Beide Teile liegen plan aneinander, keine Stufen oder Kanten",
            "good": "Teile überwiegend plan, geringer Höhenunterschied <0.1mm",
            "acceptable": "Teile mit Höhenunterschieden <0.3mm, erfordern Schleifen",
            "poor": "Sichtbare Stufen oder Unebenheiten"
        },
        "grain_direction_requirements": "Längsfasern sollten mit Schnittrichtung ausgerichtet sein für saubere Bearbeitung",
        "adhesive_recommendation": "Epoxidharz oder Polyurethan-Leim mit gleichmäßigem Auftrag auf beide Flächen.",
        "clamping_time_hours": 12,
        "clamping_pressure_kpa": 500,
        "glue_line_thickness_mm": 0.2,
        "common_failures": [
            "Schubversagen wenn Lap-Länge zu kurz (<3x Holzdicke)",
            "Ausrisse an Schnittkanten unter Biegung",
            "Quellung führt zu Höhenunterschieden und Spannungen",
            "Wasser-Eindringung an den freiliegenden Stirnflächen"
        ],
        "lap_depth_ratio": 0.5,
        "lap_length_ratio": 3.0
    },

    "through_bolt": {
        "name": "Durchgangsbolzen mit Holz (Through Bolt with Wood)",
        "description": "Stahlbolzen mit großen Unterlegscheiben und Muttern durch Holz-Teile. Für maximale Haltbarkeit und Nachrüstbarkeit. Häufig kombiniert mit Holzspielern für Lastverteilung.",
        "strength_rating": 0.96,
        "water_resistance": "excellent",
        "suitable_for": [
            "keel_attachment",
            "mast_step_connection",
            "chainplate_attachment",
            "structural_reinforcement",
            "high_load_connections"
        ],
        "tools_required": [
            "drill_with_large_bit",
            "wrench_set",
            "torque_wrench",
            "countersink_tool",
            "measuring_device"
        ],
        "typical_errors": [
            "Bohrung zu nah an Kanten (<50mm) → Ausrisse",
            "Bolzen-Größe nicht zu Belastung abgestimmt → Überschreitung von zul. Spannung",
            "Unterlegscheibe zu klein → Holzquerung und Spannungskonzentration",
            "Keine Isolierung Holz-Metall → Kontaktelektrolyse und Oxidation",
            "Zu straffe Anzugskraft → Holzausrisse oder Verformung"
        ],
        "quality_criteria": {
            "excellent": "Bolzen sitzt sicher, Unterlegscheiben vollflächig, kein Spiel, gutes Erscheinungsbild",
            "good": "Bolzen sitzt sicher, Unterlegscheiben haben minimale Spiel <0.2mm",
            "acceptable": "Bolzen hält, Unterlegscheiben-Spiel bis 0.5mm akzeptabel",
            "poor": "Bolzen locker oder Holzausrisse sichtbar"
        },
        "grain_direction_requirements": "Bohrung sollte mit Längsfasern-Richtung abgestimmt sein um Spalten zu vermeiden",
        "adhesive_recommendation": "Optional: Epoxidharz um Bohrung kann Haltbarkeit erhöhen, aber nicht notwendig.",
        "clamping_time_hours": 0,
        "fastener_installation_dry": True,
        "common_failures": [
            "Korrosion durch Kontakt Stahl-Holz in Salzwassereumgebung",
            "Spalten um Bohrung unter Zug durch zu hohe Anzugskraft",
            "Lockerung durch Vibrationen wenn nicht gegen Verdrehen gesichert",
            "Holzausrisse beim Bohren wenn nicht richtig geführt",
            "Galvanische Korrosion wenn verzinkte und edelstahl Teile gemischt"
        ],
        "bolt_diameter_mm": 12,
        "washers_required": True,
        "isolation_washer_material": "nylon_or_plastic",
        "edge_distance_mm": 50,
        "hole_tolerances_mm": [0, 0.5]
    }
}


# ============================================================================
# WOOD FINISHING SYSTEMS FOR MARINE ENVIRONMENTS
# ============================================================================

WOOD_FINISHING = {
    "teak_oil": {
        "name": "Teaköl (Teak Oil)",
        "description": "Dünnflüssiges Öl auf Basis von Tung-/Leinöl mit UV-Schutz-Additiven. Eindringende Behandlung für massive Teakhölzer, besonders an Deck. Natürliches Aussehen, minimale Glanzentwicklung, erfordert häufige Wartung (3-4 Wochen).",
        "coats_required": 3,
        "prep_between_coats": "Leichte Oberflächen-Rauheit (150er Körnung), trocken auswischen",
        "drying_time_hours": 24,
        "recoat_window_hours": 48,
        "uv_protection": 0.45,
        "water_protection": 0.70,
        "maintenance_interval_months": 1,
        "suitable_woods": ["teak", "afromosia", "iroko"],
        "application_method": "Bürstung oder Tauchen, Überschuss abwischen",
        "temperature_range_c": [10, 30],
        "humidity_max_pct": 80,
        "quality_criteria": {
            "wet_film_thickness_um": 120,
            "appearance": "Seidenmatter Glanz, gleichmäßige Färbung, keine Tropfmarken",
            "adhesion_test": "Cross-hatch kein Abblättern (ASTM D3359 Bewertung 5B)"
        },
        "common_defects": [
            {
                "defect": "Fleckige Färbung",
                "cause": "Ungleichmäßiger Auftrag oder Holzoberflächen-Saugfähigkeit variiert",
                "prevention": "Gleichmäßiger Auftrag mit guter Bürstenführung, Priming-Dünnschicht wenn nötig"
            },
            {
                "defect": "Raue Oberfläche nach Trocknung",
                "cause": "Holzfasern aufgerichtet durch Feuchtigkeit, zu grobe Schleifrauheit",
                "prevention": "Nach 1. Coat mit 180er/220er leicht schleifen, trocken auswischen"
            },
            {
                "defect": "Schnelle Grauung (4-6 Wochen)",
                "cause": "UV-Schutz insuffizient oder Salzwasser-Oberflächenoxidation",
                "prevention": "Hochqualitatives Öl mit UV-Additiven, regelmäßige Wartung alle 3 Wochen"
            },
            {
                "defect": "Klebrige Oberfläche",
                "cause": "Zu lange Wartungsintervalle, Öl-Abbau durch UV",
                "prevention": "Regelmäßige Reinigung und Nachölung vor Klebigkeit"
            }
        ],
        "reapplication_interval_weeks": 4,
        "uv_stabilizer_type": "Benzophenone or HALS",
        "solids_content_pct": 45,
        "film_thickness_dry_um": 40
    },

    "danish_oil": {
        "name": "Dänisches Öl (Danish Oil)",
        "description": "Eindringendes Öl mit Harzanteil (Polyurethan oder ähnlich) für innenräume und geschützte Außenbereiche. Bildet dünne harte Schicht ohne Filmbildung. Einfach zu unterhalten, natürliches Aussehen.",
        "coats_required": 2,
        "prep_between_coats": "220er Schleifrauheit, trocken auswischen",
        "drying_time_hours": 6,
        "recoat_window_hours": 24,
        "uv_protection": 0.25,
        "water_protection": 0.60,
        "maintenance_interval_months": 3,
        "suitable_woods": ["walnut", "oak", "maple", "interior_only"],
        "application_method": "Bürstung oder Tauchen, Überschuss nach 30 min abwischen",
        "temperature_range_c": [15, 25],
        "humidity_max_pct": 70,
        "quality_criteria": {
            "wet_film_thickness_um": 100,
            "appearance": "Seidenmatter natürlicher Glanz, intensivierte Holzfasern",
            "adhesion_test": "Cross-hatch kein Abblättern"
        },
        "common_defects": [
            {
                "defect": "Helle Flecken nach Trocknung",
                "cause": "Unvollständige Überschuss-Entfernung oder Holzporensammlung",
                "prevention": "Gründliches Abwischen nach 20-30 min, evtl. Zweitgang"
            },
            {
                "defect": "Glanzunterschiede zwischen Holzbereichen",
                "cause": "Unterschiedliche Holzporengrößen (Früh-/Spätholz) und Saugfähigkeit",
                "prevention": "Gleichmäßige Auftragsmenge, evtl. Primer für porenreiches Holz"
            },
            {
                "defect": "Flockbildung (kleine Partikel)",
                "cause": "Staub während Trocknung oder Holzfasern-Quellung",
                "prevention": "Staubfreie Umgebung, leichte 220er Schleifrauheit vor Coat"
            }
        ],
        "reapplication_interval_months": 6,
        "uv_stabilizer_type": "Limited HALS",
        "solids_content_pct": 30,
        "film_thickness_dry_um": 15,
        "not_suitable_for": ["exterior_deck", "constant_wet_immersion"]
    },

    "marine_varnish_spar": {
        "name": "Marine-Lack Spar-Typ (Marine Varnish, Spar Type)",
        "description": "Hochelastisches Finish auf Alkydharz-Basis für bewegliche Holzteile (Deck, Schalustern, Schotten). Flexibilität verhindert Rissbildung unter Holzfeuchte-Quelling. Klassische traditionelle Marine-Lösung.",
        "coats_required": 4,
        "prep_between_coats": "220er Schleifrauheit, trocken auswischen",
        "drying_time_hours": 16,
        "recoat_window_hours": 24,
        "uv_protection": 0.65,
        "water_protection": 0.88,
        "maintenance_interval_months": 12,
        "suitable_woods": ["oak", "teak", "mahogany", "cedar"],
        "application_method": "Dünne Äußerung mit Kunsthaarbürste, 2-3 Überstriche",
        "temperature_range_c": [10, 25],
        "humidity_max_pct": 75,
        "quality_criteria": {
            "wet_film_thickness_um": 150,
            "appearance": "Klarer Hochglanz mit perfekter Opazität, keine Dunsthöfe",
            "adhesion_test": "Cross-hatch 5B, kein Abblättern"
        },
        "common_defects": [
            {
                "defect": "Risse und Abblättern nach wenigen Monaten",
                "cause": "Zu steife Lackfilm (mangelnde Flexibilität), unzureichende Oberflächenrauheit",
                "prevention": "High-Flex Spar-Lacke verwenden, 220er Körnung, max. 3 Coats pro Saison"
            },
            {
                "defect": "Orange-Peel Textur",
                "cause": "Zu geringe Verdünnung, falsche Luftfeuchte oder Oberflächentemperatur",
                "prevention": "Genaue Verdünnung nach Herstellerangaben (max. 10%), optimale Bedingungen (15-20°C, <70% RH)"
            },
            {
                "defect": "Sackgasse / Sagging (Durchhang)",
                "cause": "Zu viel Material aufgetragen oder zu hohe Temperatur",
                "prevention": "Dünne Schichten verwenden, kühlere Bedingungen, gute Belüftung"
            },
            {
                "defect": "Grauung und Raue Oberfläche nach 6-9 Monaten",
                "cause": "UV-Strahlung durchdringt Lack-Film, Holz-Oberflächenoxidation",
                "prevention": "Jährlich abschleifen und nachbessern, High-Tech UV-Filter verwenden"
            },
            {
                "defect": "Klebrige oder klebrige Oberfläche",
                "cause": "Unvollständige Aushärtung (zu feuchte/kalte Bedingungen) oder alte Schichten",
                "prevention": "Mindestens 48h Aushärtung in warmen trockenen Bedingungen, alte Schichten abschleifen"
            }
        ],
        "reapplication_interval_months": 12,
        "annual_maintenance_required": True,
        "uv_stabilizer_type": "Carbon Black or Inorganic Pigments",
        "solids_content_pct": 45,
        "film_thickness_dry_um": 60
    },

    "epoxy_seal": {
        "name": "Epoxidversiegelung (Epoxy Seal)",
        "description": "Zwei-Komponenten-Epoxidharz als Grundierung und Versiegelung. Hart, wasserdicht, extrem langlebig. Für Holz-Strukturen, feuchte Bereiche und Reparaturen.",
        "coats_required": 1,
        "prep_between_coats": "N/A (monocoat) or 220er für weitere Schichten",
        "drying_time_hours": 24,
        "recoat_window_hours": 48,
        "uv_protection": 0.50,
        "water_protection": 0.99,
        "maintenance_interval_months": 24,
        "suitable_woods": ["all_woods_especially_end_grain"],
        "application_method": "Bürste oder Roller, gleichmäßig dünne Schicht",
        "temperature_range_c": [15, 25],
        "humidity_max_pct": 75,
        "pot_life_minutes": 45,
        "quality_criteria": {
            "wet_film_thickness_um": 200,
            "appearance": "Kristallklare oder leicht gelbliche Tönung, hoher Glanz, keine Einschlüsse",
            "adhesion_test": "Cross-hatch 5B, Immersion test nach ASTM D1141"
        },
        "common_defects": [
            {
                "defect": "Luftblasen und Pinhole",
                "cause": "Luft im Epoxid beim Mischen oder Auftrag, feuchtes Holz",
                "prevention": "Langsames Mischen ohne Schäumen, feuchtigkeitsmessung <14%, evtl. Vakuum-Entgasung"
            },
            {
                "defect": "Unvollständige Aushärtung (klebrig)",
                "cause": "Falsches Verhältnis Harz:Härter oder zu kalte Bedingungen",
                "prevention": "Genaues Verhältnis nach Herstellerangaben, min. 18°C, mind. 48h Aushärtung"
            },
            {
                "defect": "Weiße Rückstände (Blooming)",
                "cause": "Aminabbau durch UV-Strahlung, zuerst weiße Oberflächen",
                "prevention": "Nicht der Sonne aussetzen ohne UV-schützende Topcoat, evtl. transparente UV-Versiegelung"
            },
            {
                "defect": "Verlaufmarken oder Strukturen",
                "cause": "Ungleichmäßiger Auftrag, Pinsel-Markierungen",
                "prevention": "Dünne gleichmäßige Äußerung, hochwertige Bürste oder Roller"
            }
        ],
        "reapplication_interval_months": 24,
        "cure_temperature_range_c": [15, 25],
        "full_cure_time_days": 7,
        "uv_stabilizer_type": "UV-blocking topcoat recommended",
        "solids_content_pct": 100,
        "film_thickness_dry_um": 100
    },

    "polyurethane_2k": {
        "name": "Polyurethan 2K (Polyurethane 2-Component)",
        "description": "Hochperformant 2-K-Polyurethan-Lack für Yacht-Deck und strukturelle Bereiche. Extrem hart, UV-resistent, wasserfest. Modernes System mit guter Verarbeitbarkeit.",
        "coats_required": 3,
        "prep_between_coats": "180-220er Schleifrauheit, Staub entfernen mit Tuch",
        "drying_time_hours": 8,
        "recoat_window_hours": 16,
        "uv_protection": 0.75,
        "water_protection": 0.95,
        "maintenance_interval_months": 24,
        "suitable_woods": ["all_exterior_woods"],
        "application_method": "Bürste oder HVLP-Spritzanlage, dünne gleichmäßige Schichten",
        "temperature_range_c": [10, 25],
        "humidity_max_pct": 70,
        "pot_life_minutes": 60,
        "quality_criteria": {
            "wet_film_thickness_um": 120,
            "appearance": "Hochglanzoberfläche, kristallklar, absolut gleichmäßig",
            "adhesion_test": "Cross-hatch 5B, ASTM D3359"
        },
        "common_defects": [
            {
                "defect": "Gelbfärbung über Zeit",
                "cause": "UV-Einstrahlung auch bei beständigen PU-Systemen, Alkydrückstände",
                "prevention": "Aliphatic Polyurethan verwenden (nicht Aromatic), gute UV-Filter"
            },
            {
                "defect": "Blasenbildung",
                "cause": "Wasserdampf-Eintritt von unten, feuchtes Holz oder Grundierung",
                "prevention": "Holzfeuchte prüfen (<12%), gute Grundierung, Feuchtebarriere"
            },
            {
                "defect": "Raue Oberfläche nach Trocknung",
                "cause": "Staub während Trocknung oder zu grobe Oberflächenrauheit",
                "prevention": "Staubfreier Bereich, 220er Schleifrauheit, feuchte Tücher vor Auftrag"
            },
            {
                "defect": "Hohlenschlag / Cratering",
                "cause": "Silikon-Kontamination oder Tensid in Luft",
                "prevention": "Keine Silikon-Produkte in Nähe, hochreine Spritzanlage, Aktivkohle-Filter"
            }
        ],
        "reapplication_interval_months": 24,
        "cure_temperature_range_c": [10, 25],
        "gloss_level": "high",
        "uv_stabilizer_type": "UV absorber + HALS",
        "solids_content_pct": 55,
        "film_thickness_dry_um": 70,
        "two_pack_mixing_ratio_exact": True
    },

    "cetol_marine": {
        "name": "Cetol Marine (Cetol Marine Finish)",
        "description": "Spezial-Finish für bewegliche Holzteile (Schotten, Fenster-Rahmen) mit hoher Elastizität. Wasser- und UV-geschützt, wartungsfreundlich (erneut streichen ohne Abschliff möglich).",
        "coats_required": 2,
        "prep_between_coats": "Kurzes Anrauen mit 320er, Staub entfernen",
        "drying_time_hours": 12,
        "recoat_window_hours": 24,
        "uv_protection": 0.70,
        "water_protection": 0.90,
        "maintenance_interval_months": 18,
        "suitable_woods": ["all_exterior_painted_applications"],
        "application_method": "Bürste (Kunsthaar) oder Roller, dünne Schichten",
        "temperature_range_c": [10, 25],
        "humidity_max_pct": 75,
        "quality_criteria": {
            "wet_film_thickness_um": 130,
            "appearance": "Semi-gloss bis Hochglanz, gleichmäßig ohne Striemen",
            "adhesion_test": "Cross-hatch 5B"
        },
        "common_defects": [
            {
                "defect": "Ablösung bei Risse-Bildung",
                "cause": "Holz-Bewegung größer als Lack-Elastizität",
                "prevention": "Gute Grundierung, dünne Schichten, gute Haftung sicherstellen"
            },
            {
                "defect": "Mattierung nach 12 Monaten",
                "cause": "Oberflächenoxidation und UV-Abbau",
                "prevention": "Regelmäßige Reinigung und leichte Nachbespannung alle 18 Monate"
            }
        ],
        "reapplication_interval_months": 18,
        "uv_stabilizer_type": "HALS and Pigments",
        "solids_content_pct": 48,
        "film_thickness_dry_um": 65
    },

    "tung_oil": {
        "name": "Tungöl (Tung Oil)",
        "description": "Natürliches einziehendes Öl mit hohem Trocknungsvermögen (ohne Härter). Für innenräume und Möbel. Natürliche Schönheit ohne filmbildendes Finish.",
        "coats_required": 4,
        "prep_between_coats": "Leichte Oberflächen-Rauheit 220er, trocken",
        "drying_time_hours": 12,
        "recoat_window_hours": 24,
        "uv_protection": 0.15,
        "water_protection": 0.50,
        "maintenance_interval_months": 2,
        "suitable_woods": ["interior_woods_high_grain"],
        "application_method": "Bürstung oder Tauchen, Überschuss nach 15 min abwischen",
        "temperature_range_c": [15, 25],
        "humidity_max_pct": 70,
        "quality_criteria": {
            "appearance": "Naturholz-Oberfläche, seidig, keine Glossigkeit",
            "adhesion_test": "Nicht filmbildend, keine Peeling-Gefahr"
        },
        "common_defects": [
            {
                "defect": "Klebrige Oberfläche dauerhaft",
                "cause": "Zu viel Material aufgetragen, feuchte Bedingungen",
                "prevention": "Gründliches Abwischen nach 15 min, gute Belüftung"
            }
        ],
        "reapplication_interval_weeks": 8,
        "not_suitable_for": ["exterior_high_weathering", "marine_deck"]
    },

    "linseed_oil_boiled": {
        "name": "Gekochtes Leinöl (Boiled Linseed Oil)",
        "description": "Natürliches Öl mit Trockner-Zusätzen für traditionelle Anwendungen. Historischer Standard für Yachtholz, aber langsam und weniger wirksam als moderne Öle.",
        "coats_required": 6,
        "prep_between_coats": "220er Körnung, trocken",
        "drying_time_hours": 24,
        "recoat_window_hours": 48,
        "uv_protection": 0.20,
        "water_protection": 0.55,
        "maintenance_interval_months": 4,
        "suitable_woods": ["all_woods_traditional"],
        "application_method": "Bürstung oder Tauchen",
        "temperature_range_c": [15, 25],
        "humidity_max_pct": 70,
        "quality_criteria": {
            "appearance": "Natürliches Matt-Finish, Holzfasern sichtbar"
        },
        "common_defects": [
            {
                "defect": "Sehr langsame Trocknung",
                "cause": "Natürliche Trockner unzureichend",
                "prevention": "Warme Bedingungen, gute Belüftung, evtl. Trockner hinzufügen"
            },
            {
                "defect": "Flöckchen auf Oberfläche",
                "cause": "Staub, Oxidationsprodukte",
                "prevention": "Staubfreie Umgebung"
            }
        ],
        "reapplication_interval_months": 6,
        "traditional_application": True
    },

    "paint_system_2k": {
        "name": "Lacksystem 2K (Paint System 2-Component)",
        "description": "Deckende Weiß- oder Farbschicht mit Grund und Decklack (beide 2K). Für Kajüten-Innenwände, technische Bereiche, Schalustern.",
        "coats_required": 3,
        "prep_between_coats": "150-220er je nach Schicht",
        "drying_time_hours": 8,
        "recoat_window_hours": 16,
        "uv_protection": 1.0,
        "water_protection": 0.95,
        "maintenance_interval_months": 36,
        "suitable_woods": ["all_woods_for_priming"],
        "application_method": "Bürste, Roller oder Spritzanlage",
        "temperature_range_c": [10, 25],
        "humidity_max_pct": 70,
        "quality_criteria": {
            "wet_film_thickness_um": 150,
            "appearance": "Gleichmäßiger Farb-Auftrag, volle Deckkraft",
            "adhesion_test": "Cross-hatch 5B ASTM D3359"
        },
        "common_defects": [
            {
                "defect": "Wölfig-Aussehen (Seidenglanz-Unterschiede)",
                "cause": "Unterschiedliche Saugfähigkeit Holz oder Grundschicht-Qualität",
                "prevention": "Gute Grundierung, hochwertige Primer"
            }
        ],
        "reapplication_interval_months": 36,
        "full_protection": True
    },

    "wax_finish": {
        "name": "Wachsfinish (Wax Finish)",
        "description": "Natürliches Finish mit Bienenwachs oder Carnaubawachs. Nur für Interieur oder sehr geschützte Außen-Stellen. Schöne Ästhetik, aber wenig Schutz.",
        "coats_required": 2,
        "prep_between_coats": "Polieren mit weicher Bürste",
        "drying_time_hours": 2,
        "recoat_window_hours": 24,
        "uv_protection": 0.05,
        "water_protection": 0.40,
        "maintenance_interval_months": 1,
        "suitable_woods": ["interior_only"],
        "application_method": "Auftragen mit Tuch, Polieren mit Bürste",
        "temperature_range_c": [15, 25],
        "humidity_max_pct": 70,
        "quality_criteria": {
            "appearance": "Sanfter Glanz, natürliche Holzfasern sichtbar"
        },
        "common_defects": [
            {
                "defect": "Flecken und Wasser-Ringe",
                "cause": "Wasser-Empfindlichkeit, fehlender Schutz",
                "prevention": "Nicht für feuchte Bereiche verwenden"
            }
        ],
        "reapplication_interval_weeks": 4,
        "interior_use_only": True
    },

    "unfinished_teak": {
        "name": "Unbehandeltes Teak (Unfinished Teak)",
        "description": "Teakholz ohne Oberflächenbehandlung. Weathers zu Silbergrau. Manchmal in modernem Design bevorzugt, aber keine Substanzschutz.",
        "coats_required": 0,
        "drying_time_hours": 0,
        "uv_protection": 0.0,
        "water_protection": 0.30,
        "maintenance_interval_months": 0,
        "suitable_woods": ["teak_only"],
        "application_method": "Keine",
        "quality_criteria": {
            "appearance": "Naturholz, silbergrau nach 1-2 Jahren Witterung"
        },
        "common_defects": [
            {
                "defect": "Flächige Grauung und Struktur-Rauhheit",
                "cause": "UV und Witterungs-Eintrag",
                "prevention": "Regelmäßige Bürstung mit weicher Bürste zur Entfernung loser Fasern"
            }
        ],
        "no_finish_applied": True,
        "natural_weathering": True
    }
}


# ============================================================================
# WOOD BENDING TECHNIQUES
# ============================================================================

WOOD_BENDING = {
    "steam_bending": {
        "name": "Dampfbiegung (Steam Bending)",
        "description": "Holz wird mit Dampf erweicht und dann um Form gebogen. Klassische Methode für Spanten und Rahmen.",
        "min_radius_by_thickness_ratio": 15,
        "suitable_species": ["oak", "ash", "elm", "beech"],
        "steam_time_per_mm": 1.0,
        "clamping_time_hours": 24,
        "clamping_pressure_kpa": 400,
        "common_failures": [
            "Holz reißt wenn Dampfdauer zu kurz",
            "Zu schnelle Abkühlung führt zu Rückfederung",
            "Ungleichmäßige Dampf-Eindringung bei dickem Material",
            "Oberflächenschrunden wenn zu schnell getrocknet"
        ],
        "quality_criteria": {
            "dimensional_accuracy_mm": 2,
            "spring_back_pct": 10,
            "surface_quality": "Keine Risse, minimale Oberflächenrauhheit"
        },
        "moisture_content_pct": "12-15%",
        "steam_box_temperature_c": 100,
        "cooling_time_hours": 12
    },

    "laminate_bending": {
        "name": "Leistenlaminat (Laminate Bending)",
        "description": "Dünne Holzstreifen (Lamellen) werden gebogen und mit Epoxid verklebt. Ermöglicht kleinere Radien als Dampfbiegung.",
        "min_radius_by_thickness_ratio": 8,
        "suitable_species": ["all_species"],
        "lamella_thickness_mm": 2,
        "clamping_time_hours": 24,
        "clamping_pressure_kpa": 800,
        "common_failures": [
            "Delamination durch unzureichenden Leim-Auftrag",
            "Risse in Lamellen während Biegung",
            "Rückfederung nach Entform wenn Radius zu klein"
        ],
        "quality_criteria": {
            "radius_accuracy_mm": 3,
            "delamination_none": True,
            "cracks_none": True
        },
        "adhesive_type": "Epoxy resin",
        "moisture_content_pct": "10-14%"
    },

    "kerf_bending": {
        "name": "Kerfbiegung (Kerf Bending)",
        "description": "Dünne Sägeschnitte (Kerfe) schwächen das Holz, um Biegung ohne Dampf zu ermöglichen. Für komplexe Kurven.",
        "min_radius_by_thickness_ratio": 5,
        "suitable_species": ["all_species"],
        "kerf_depth_ratio": 0.7,
        "kerf_spacing_mm": 10,
        "clamping_time_hours": 12,
        "common_failures": [
            "Kerfe zu tief → Material bricht",
            "Zu wenige Kerfe → Biegung unvollständig",
            "Bruch an Kerfen wenn zu schnell gebogen"
        ],
        "quality_criteria": {
            "radius_tolerance_mm": 5,
            "no_splintering": True
        }
    },

    "hot_water_soak": {
        "name": "Heißwassertränkung (Hot Water Soak)",
        "description": "Holz wird in heißem Wasser eingeweicht, dann gebogen. Weniger aggressiv als Dampf, für dünne Teile.",
        "min_radius_by_thickness_ratio": 20,
        "suitable_species": ["all_species"],
        "soak_time_hours": 4,
        "soak_temperature_c": 80,
        "clamping_time_hours": 24,
        "common_failures": [
            "Zu kurze Eintauchzeit → unvollständige Durchfeuchtung",
            "Zu schnelles Trocknen → Risse während Trocknung"
        ],
        "quality_criteria": {
            "even_bending": True,
            "minimal_cracking": True
        }
    }
}


# ============================================================================
# WOOD FITTING TECHNIQUES FOR PRECISION ASSEMBLY
# ============================================================================

WOOD_FITTING_TECHNIQUES = {
    "scribing": {
        "name": "Anreißen (Scribing)",
        "description": "Markieren von Schnittlinien und Formen mit Anreißwerkzeugen. Basis der Präzisions-Holzbearbeitung.",
        "tools_required": ["marking_gauge", "layout_knife", "pencil_sharp", "straightedge"],
        "accuracy_mm": 0.5,
        "when_to_use": "Vor jedem Schnitt oder Hobeln, besonders bei Schmiege-Linien",
        "quality_criteria": {
            "line_sharpness": "Klar definiert, nicht ausgefranst",
            "accuracy": "Toleranz ±0.5mm",
            "visibility": "Sichtbar ohne zu tief zu ritzen"
        },
        "common_mistakes": [
            "Zu stumpfes Anreißwerkzeug → unscharfe Linien",
            "Zu fest angedrückt → Beschädigungen oder ungenaue Linien",
            "Holzfeuchte nicht beachtet → Linienverzug durch Quellung"
        ]
    },

    "spiling": {
        "name": "Abpausen / Schablonieren (Spiling / Template Transfer)",
        "description": "Übertragen komplexer Konturen (z.B. Schiffsseiten-Anpassung) von vorhandenem Holz oder Baunetzlisten auf neues Material.",
        "tools_required": ["spile_board", "compass_pencil_or_tracing_rod", "layout_knife"],
        "accuracy_mm": 2,
        "when_to_use": "Bei Planken-Anpassung, Übergängen, komplexen Formen an bestehende Strukturen",
        "quality_criteria": {
            "contour_accuracy": "±2mm zu Original",
            "repeatability": "Mehrere Spile halten gleiche Form",
            "marking_clarity": "Deutlich übertragen auf Werkstoff"
        },
        "common_mistakes": [
            "Spile-Dicke nicht beachtet → Größenunterschied beim Übertrag",
            "Nicht orthogonal angesetzt → Winkel und Versatz",
            "Material-Bewegung während Spilenprozess → Verfälschung"
        ]
    },

    "template_transfer": {
        "name": "Schablonen-Übertrag (Template Transfer)",
        "description": "Nutzung von Sperrholz- oder Kunststoff-Schablonen zur genauen Wiederholung von Formen (z.B. identische Spanten).",
        "tools_required": ["template_plywood", "pencil", "marking_knife", "clamps"],
        "accuracy_mm": 1,
        "when_to_use": "Serienfertigung, identische Teile, Spanten-Reihen",
        "quality_criteria": {
            "form_accuracy": "±1mm zu Schablone",
            "repeatability": "Alle Teile identisch",
            "edge_finish": "Saubere Kanten ohne Ausrisse"
        },
        "common_mistakes": [
            "Schablone nicht fest genug gehalten → Versatz",
            "Stift oder Markierungswerkzeug angewinkelt → Linienverzug",
            "Schablone verschleißt → Größenänderung nach mehreren Überträgen"
        ]
    },

    "dry_fit_protocol": {
        "name": "Trockenpassung (Dry Fit Protocol)",
        "description": "Zusammensetzen aller Teile ohne Leim zur Kontrolle der Passung und Montierbarkeit vor final-Leimung.",
        "tools_required": ["all_assembly_clamps", "straightedge", "measuring_device", "shims"],
        "accuracy_mm": 0.5,
        "when_to_use": "Vor jeder Haupt-Verleimung (Spanten, Rahmen, Strukturen)",
        "quality_criteria": {
            "all_parts_fit": "Ohne erzwungene Passung",
            "alignment": "Alle Teile halten geplante Ausrichtung",
            "gaps": "Größer <0.5mm wenn sichtbar"
        },
        "common_mistakes": [
            "Keine Trockenpassung (direkt leim-Einsatz) → späte Probleme",
            "Fehler bei Trockenpassung nicht korrigiert → unbrauchbares Endprodukt",
            "Zu straffe Passung bei Trockenpassung → Passung gelöst nach Quellung"
        ]
    },

    "gap_filling_epoxy": {
        "name": "Spalten-Verfüllung Epoxid (Gap Filling with Epoxy)",
        "description": "Füllen von Fugen und Spalten mit angefärbtem Epoxidharz für visuelles Verschwinden.",
        "tools_required": ["epoxy_two_part", "putty_knife", "scraper", "sandpaper"],
        "accuracy_mm": 0.2,
        "when_to_use": "Nach Trockenpassung wenn Spalte 0.2-2mm; kleinere Spalte mit Holz-Spachteln, größere mit speziellen Methoden",
        "quality_criteria": {
            "appearance": "Spalten verschwunden nach Schleifen",
            "strength": "Epoxid-Füllung mindestens gleich hart wie Holz",
            "durability": "Keine Risse unter Quellung/Schwindung"
        },
        "common_mistakes": [
            "Spalte nicht gereinigt → Epoxid-Haftung schwach",
            "Zu viel Material überschüssig → Verschliff schwierig",
            "Epoxid-Farbe nicht angepasst → sichtbar nach Finish"
        ]
    },

    "fairing_longboard": {
        "name": "Längsspannung (Fairing with Longboard)",
        "description": "Längschleifen mit langen Schleifbohlen (Längsspaner) um flächigen Verlauf zu erreichen. Kritisch für Deck und Rumpf.",
        "tools_required": ["fairing_longboard_2m", "sanding_block", "straightedge", "pencil"],
        "accuracy_mm": 1,
        "when_to_use": "Nach Oberflächenrauheit-Sanding, Schritt vor Finish-Coating",
        "quality_criteria": {
            "surface_flatness": "Max. 1mm Hochpunkt über 2m",
            "smoothness": "Ra <1.6µm vor Finish",
            "no_ripples": "Keine Längs-Wellen erkennbar"
        },
        "common_mistakes": [
            "Zu grobe Körnung → Kratzer statt Fairing",
            "Nicht mit Schiffslängachse gearbeitet → Querwellen",
            "Zu wenig Material abgetragen → unebene Bereiche bleiben"
        ]
    }
}


# ============================================================================
# WOOD TOOL MARKS AND SURFACE QUALITY ASSESSMENT
# ============================================================================

WOOD_TOOL_ASSESSMENT = {
    "plane_marks": {
        "name": "Hobelmarkierungen (Plane Marks)",
        "acceptable_criteria": [
            "Feine parallele Linien, max. 0.5mm tief",
            "Gleichmäßig über gesamte Fläche",
            "Nicht sichtbar nach leichtem Schleifen mit 150er",
            "Mit Faserlauf, nicht quer zur Faser"
        ],
        "unacceptable_criteria": [
            "Tiefe Kratzer >1mm (Hobeleisen stumpf)",
            "Ungleichmäßige Markierungen (Messer nicht eben)",
            "Risse oder Ausrisse an Kanten",
            "Quermarkierungen (gegen Faserlauf gehobelt)"
        ],
        "how_to_fix": "Mit 120-150er Schleifer überarbeiten, oder bei sehr tiefen Kratzern nachhoben mit schärferem Hobel"
    },

    "router_marks": {
        "name": "Fräsermarkierungen (Router Marks)",
        "acceptable_criteria": [
            "Glatte Oberfläche nach Fräsen mit sauberen Schneidkanten",
            "Zirkular-Markierungen sichtbar aber fein (von Fräser-Drehzahl)",
            "Keine Brandflecken (zu schnelle Vorschub)",
            "Keine Ausrisse an Kanten bei richtiger Fräs-Richtung"
        ],
        "unacceptable_criteria": [
            "Raue aufgewölbte Fasern (zu hohe Drehzahl oder stumpfer Fräser)",
            "Brandflecken oder Verfärbungen (zu langsamer Vorschub)",
            "Ausrisse oder Splitter (falscher Fräs-Richtung oder schlechtes Material)",
            "Tiefe Kratzer oder Rauheit"
        ],
        "how_to_fix": "Mit scharfem Fräser und angepasster Drehzahl/Vorschub nachfräsen, oder mit Schleifer nacharbeiten"
    },

    "saw_marks": {
        "name": "Sägemarkierungen (Saw Marks)",
        "acceptable_criteria": [
            "Kanten-Qualität: max. 0.3mm Unebenheit bei guter Säge",
            "Schnittflächenrauhheit Ra <3.2µm akzeptabel",
            "Keine Brandflecken oder Verfärbungen",
            "Keine großen Ausrisse an Austritten"
        ],
        "unacceptable_criteria": [
            "Raue Kanten >0.5mm (schlechte Säge oder dumpfes Blatt)",
            "Brandflecken oder Verfärbungen (zu schneller Schnitt oder stumpf)",
            "Große Ausrisse am Austritt des Schnitts",
            "Schräger Schnitt oder Wölbung"
        ],
        "how_to_fix": "Mit Handhobel oder Schleifer Kanten glätten, bei großen Ausrissen nachhobeln"
    },

    "chisel_marks": {
        "name": "Meiselmarkierungen (Chisel Marks)",
        "acceptable_criteria": [
            "Saubere Schnittflächen ohne Ausrisse oder Kratzer",
            "Ebene Meißel-Spur erkennbar aber nicht zu tief",
            "Oberfläche glatt, kein Abbrecherwerk",
            "Saubere Ecken und Kanten"
        ],
        "unacceptable_criteria": [
            "Raue oder ausgefranste Oberflächen (stumpfer Meißel)",
            "Große Kratzer oder Dellen",
            "Ausrisse an Ecken oder Längsfasern",
            "Unebene Oberfläche mit Hochpunkten"
        ],
        "how_to_fix": "Mit schärferem Meißel nacharbeiten, oder mit Schleifestein die Meißel-Schneide schärfen"
    },

    "sanding_grades": {
        "name": "Schleif-Körnungen und Qualität (Sanding Grades)",
        "acceptable_criteria": {
            "60_to_80_grit": "Grobe Oberflächenentfernung, Kratzer bis 300µm akzeptabel",
            "100_to_150_grit": "Mittel, max. 100µm Kratzer sichtbar, aber Vorbereitung auf Finish",
            "180_to_220_grit": "Fein, max. 20µm Kratzer, direkt vor Finish-Coating",
            "above_320_grit": "Sehr fein, <5µm Kratzer, selten notwendig (Lack-Rauhheit erzeugt)"
        },
        "unacceptable_criteria": {
            "skipping_grits": "Z.B. direkt 60er zu 220er = Kratzer bleiben und neue nicht erzeugt",
            "over_sanding_fine": "Z.B. 320-400er vor Lackierung = Lack kann nicht haften, zu glatt",
            "sanding_against_grain": "Querkratzer eingebracht, schwer zu entfernen",
            "using_dull_paper": "Polieren statt Schleifen, Heat statt Abrasion"
        },
        "how_to_fix": "Folgende Körnung eine oder zwei Stufen groberabwärts, dann wieder aufwärts durchschleifen"
    }
}


# ============================================================================
# WOOD SPECIES PROPERTIES — Holzarten-Detailwissen
# ============================================================================

WOOD_SPECIES_MARINE = {
    "teak_burma": {
        "name_de": "Teak (Burma / Myanmar)",
        "botanical": "Tectona grandis",
        "density_kg_m3": 650,
        "bending_strength_mpa": 97,
        "compression_strength_mpa": 55,
        "modulus_of_elasticity_gpa": 12.3,
        "shrinkage_radial_percent": 2.5,
        "shrinkage_tangential_percent": 5.8,
        "natural_oil_content": "hoch — natürliche Öligkeit macht Teak wasserabweisend",
        "silica_content_percent": 1.4,
        "durability_class": 1,
        "grain_orientation_marine": "Stehende Jahresringe für Decksplanken (quarter-sawn)",
        "equilibrium_moisture_content_percent": {"temperate": 12, "tropical": 15, "heated_interior": 8},
        "typical_use": ["Decksbelag", "Cockpit", "Innenausbau", "Handläufe", "Schwimmplattform"],
        "tool_wear": "Hoch — Siliziumdioxid stumpft Klingen schnell ab, HM-bestückte Werkzeuge verwenden",
    },
    "iroko": {
        "name_de": "Iroko (Kambala)",
        "botanical": "Milicia excelsa",
        "density_kg_m3": 640,
        "bending_strength_mpa": 87,
        "durability_class": 1,
        "typical_use": ["Teak-Alternative für Deck", "Ruderblatt-Kern", "Außenverkleidung"],
        "note": "Guter Teak-Ersatz, aber ohne natürlichen Ölgehalt — muss behandelt werden",
        "interlocked_grain": True,
        "gluing": "Gut mit Epoxid, Kontaktflächen frisch schleifen (Kalziumoxalat-Einlagerungen)",
    },
    "eiche": {
        "name_de": "Eiche (Europäische Stieleiche)",
        "botanical": "Quercus robur",
        "density_kg_m3": 710,
        "bending_strength_mpa": 95,
        "durability_class": 2,
        "tannin_content": "hoch — reagiert mit Eisen/Stahl (schwarze Verfärbung!)",
        "typical_use": ["Klassische Spanten", "Kielholz", "Ruderschaft (historisch)", "Innenausbau klassisch"],
        "warning": "NIEMALS Edelstahl-Schrauben ohne Isolierung — Gerbsäure greift Stahl an und erzeugt schwarze Flecken",
        "steam_bending": "Hervorragend geeignet — klassisches Biegeholz",
    },
    "esche": {
        "name_de": "Esche (Gemeine Esche)",
        "botanical": "Fraxinus excelsior",
        "density_kg_m3": 690,
        "bending_strength_mpa": 105,
        "durability_class": 5,
        "typical_use": ["Pinne", "Ruder (Dinghy)", "Riemen/Paddel", "Bootshaken"],
        "note": "Hohe Biegefestigkeit aber NICHT dauerhaft im Außenbereich — nur mit Schutzlack",
        "steam_bending": "Sehr gut geeignet",
    },
    "laerche": {
        "name_de": "Lärche (Europäische Lärche)",
        "botanical": "Larix decidua",
        "density_kg_m3": 590,
        "bending_strength_mpa": 93,
        "durability_class": 3,
        "resin_content": "mittel — natürliche Harzkanäle",
        "typical_use": ["Planken (historisch/klassisch)", "Kimmholz", "Masten (traditionell)"],
        "note": "Traditionelles Bootsbauholz in Europa, gute Dauerhaftigkeit für Nadelholz",
    },
    "kork": {
        "name_de": "Kork (Korkrinde)",
        "botanical": "Quercus suber",
        "density_kg_m3": 120,
        "thermal_conductivity_w_mk": 0.04,
        "water_absorption": "minimal bei geschlossener Oberfläche",
        "typical_use": ["Bodenbelag (als Korkparkett)", "Isolierung", "Anti-Rutsch-Belag", "Vibrationsdämpfung"],
        "note": "Leicht, warm, rutschfest — als Decksbelag-Alternative zunehmend beliebt",
        "installation": "Verklebt auf ebener Unterlage, versiegelt mit PU-Lack (2K)",
    },
    "accoya": {
        "name_de": "Accoya® (acetylierte Kiefer)",
        "botanical": "Pinus radiata (modifiziert)",
        "density_kg_m3": 510,
        "durability_class": 1,
        "modification": "Acetylierung — Holz wird auf molekularer Ebene wasserabweisend",
        "dimensional_stability": "75% weniger Quellen/Schwinden als unbehandeltes Holz",
        "typical_use": ["Außenverkleidung", "Decksbelag", "Fensterrahmen", "Lukenrahmen"],
        "advantage": "Dauerhaftigkeit wie Teak, aus nachhaltiger Quelle, kein Tropenholz",
    },
    "mahagoni": {
        "name_de": "Mahagoni (Khaya / Sapele)",
        "botanical": "Khaya ivorensis / Entandrophragma cylindricum",
        "density_kg_m3": 560,
        "bending_strength_mpa": 80,
        "durability_class": 2,
        "typical_use": ["Innenausbau", "Planken (Carvel)", "Ruderblatt", "Steuerräder"],
        "gluing": "Sehr gut mit Epoxid",
        "finish": "Nimmt Lack und Öl hervorragend an — klassische Yacht-Optik",
    },
    "marine_plywood_bs1088": {
        "name_de": "Marine-Sperrholz BS 1088",
        "standard": "BS 1088:2003 (British Standard)",
        "core_species": "Okoumé (Aucoumea klaineana) oder Meranti",
        "adhesive": "WBP (Weather and Boil Proof) — Phenolharz",
        "void_free": True,
        "thicknesses_mm": [4, 6, 9, 12, 15, 18, 22, 25],
        "typical_use": ["Schotten", "Laminier-Unterlage", "Innenmöbel", "Bodenplatten"],
        "edge_sealing": "ALLE Kanten mit Epoxid versiegeln — sonst Delamination durch Wasser",
    },
}

# ============================================================================
# STEAM BENDING PARAMETERS — Dampfbiegen Parametertabellen
# ============================================================================

STEAM_BENDING_PARAMS = {
    "eiche": {
        "steam_time_min_per_25mm": 60,
        "min_radius_to_thickness_ratio": 2.5,
        "moisture_content_percent": 25,
        "strap_required": True,
        "spring_back_percent": 10,
    },
    "esche": {
        "steam_time_min_per_25mm": 45,
        "min_radius_to_thickness_ratio": 2.0,
        "moisture_content_percent": 25,
        "strap_required": True,
        "spring_back_percent": 8,
    },
    "laerche": {
        "steam_time_min_per_25mm": 60,
        "min_radius_to_thickness_ratio": 4.0,
        "moisture_content_percent": 20,
        "strap_required": True,
        "spring_back_percent": 12,
        "note": "Vorsichtig — Harz kann austreten, Rissneigung bei engem Radius",
    },
    "mahagoni": {
        "steam_time_min_per_25mm": 50,
        "min_radius_to_thickness_ratio": 6.0,
        "moisture_content_percent": 20,
        "strap_required": True,
        "spring_back_percent": 15,
        "note": "Nur moderate Biegungen möglich, für enge Radien besser Lamellenbiegung",
    },
    "teak": {
        "steam_time_min_per_25mm": 90,
        "min_radius_to_thickness_ratio": 8.0,
        "note": "Teak ist SCHLECHT biegbar — hoher Ölgehalt, besser Lamellentechnik",
    },
}

# ============================================================================
# CNC AND TURNING — CNC-Fräsen und Drechseln Marine
# ============================================================================

WOOD_CNC_MARINE = {
    "cnc_routing": {
        "name_de": "CNC-Fräsen Marine-Holzteile",
        "applications": [
            "Namenschilder und Beschriftungen",
            "Handlauf-Profile",
            "Schablonen für Wiederhol-Teile",
            "Einbau-Ausschnitte (Instrumente, Lautsprecher)",
            "Dekor-Elemente (Wappen, Logos)",
        ],
        "tool_recommendation": {
            "softwood": "Spiralnutfräser HSS, Vorschub 2000-4000 mm/min",
            "hardwood_teak": "VHM-Fräser (Vollhartmetall), Vorschub 1000-2000 mm/min",
            "marine_plywood": "Diamant-bestückter Fräser für saubere Kanten",
        },
        "dust_extraction": "Absaugung MUSS laufen — Teak-Staub ist gesundheitsschädlich (Sensibilisierung)",
    },
    "turning_lathe": {
        "name_de": "Drechseln Marine-Teile",
        "applications": [
            "Handläufe (Rundprofil)",
            "Flaggenstock",
            "Zierknöpfe und Endstücke",
            "Klampen (traditionell, aus Teak)",
            "Winschgriffe",
        ],
        "wood_recommendation": "Teak, Mahagoni, Eiche — feinkörnig, dicht, splitterfrei",
        "finishing_on_lathe": "Schleifen bis P400, dann Teaköl oder Bootslack während Rotation auftragen",
    },
}

# ============================================================================
# ASSESSMENT FUNCTION FOR WOOD JOINT QUALITY AND SUITABILITY
# ============================================================================

def assess_wood_joint(joint_type, wood_species, location, load_type, moisture_content_pct=12, temperature_c=20):
    """
    Bewerts einen Holzverbindung hinsichtlich Eignung, Qualität und Lebensdauer im Marineeinsatz.

    Args:
        joint_type: Schlüssel aus WOOD_JOINTS dict (z.B. 'scarph_joint')
        wood_species: Holzsorte (z.B. 'teak', 'oak', 'mahogany')
        location: 'interior', 'exterior', 'underwater', 'deck', 'cabin'
        load_type: 'compression', 'tension', 'shear', 'bending', 'torsion'
        moisture_content_pct: Aktuelle Holzfeuchte (Standard 12%)
        temperature_c: Arbeitstemperatur (Standard 20°C)

    Returns:
        dict mit keys:
            - suitability_score (0-1): Gesamteignung für Anwendungsfall
            - findings: list of Observations
            - recommendations: list of Technical Recommendations
            - estimated_service_life_years: Geschätzte Lebensdauer
            - critical_points: list of Failure Risk Points
            - notes: dict with German technical comments
    """

    if joint_type not in WOOD_JOINTS:
        return {
            "error": f"Unknown joint type: {joint_type}",
            "available_joints": list(WOOD_JOINTS.keys())
        }

    joint_data = WOOD_JOINTS[joint_type]
    score = 0.0
    findings = []
    recommendations = []
    critical_points = []

    # Base suitability from joint type
    base_strength = joint_data["strength_rating"]
    score += base_strength * 0.4

    # Water resistance suitability
    if location in ["underwater", "exterior"]:
        water_resist_map = {
            "excellent": 1.0,
            "very_good": 0.95,
            "good": 0.85,
            "acceptable": 0.70,
            "poor": 0.30
        }
        water_score = water_resist_map.get(joint_data.get("water_resistance", "good"), 0.7)
        score += water_score * 0.3
        findings.append(f"Wasser-Resistenz bewertet: {joint_data.get('water_resistance', 'unknown')}")
    else:
        score += 1.0 * 0.3

    # Load-type compatibility
    load_compatibility = {
        "scarph_joint": {"tension": 1.0, "compression": 1.0, "shear": 0.9, "bending": 0.85, "torsion": 0.7},
        "mortise_tenon": {"shear": 1.0, "compression": 0.95, "tension": 0.85, "bending": 0.90, "torsion": 0.6},
        "dovetail": {"shear": 1.0, "tension": 0.95, "compression": 0.85, "bending": 0.80, "torsion": 0.5},
        "tongue_groove": {"compression": 0.95, "tension": 0.70, "shear": 0.70, "bending": 0.80, "torsion": 0.4},
        "butt_joint": {"compression": 0.50, "shear": 0.40, "tension": 0.30, "bending": 0.35, "torsion": 0.2},
        "rabbet_joint": {"shear": 0.90, "compression": 0.85, "tension": 0.70, "bending": 0.75, "torsion": 0.5},
        "splined_joint": {"shear": 0.95, "compression": 0.90, "tension": 0.85, "bending": 0.88, "torsion": 0.7},
        "laminated_bend": {"bending": 1.0, "compression": 0.85, "tension": 0.80, "shear": 0.70, "torsion": 0.6},
        "epoxy_scarf": {"tension": 1.0, "compression": 0.98, "bending": 0.95, "shear": 0.90, "torsion": 0.85},
        "biscuit_joint": {"shear": 0.70, "compression": 0.65, "tension": 0.50, "bending": 0.55, "torsion": 0.3},
        "finger_joint": {"tension": 0.95, "compression": 0.95, "shear": 0.92, "bending": 0.90, "torsion": 0.75},
        "half_lap": {"shear": 0.90, "compression": 0.85, "tension": 0.65, "bending": 0.80, "torsion": 0.55},
        "through_bolt": {"tension": 1.0, "compression": 1.0, "shear": 0.95, "bending": 0.90, "torsion": 0.80}
    }

    load_compat = load_compatibility.get(joint_type, {}).get(load_type, 0.5)
    score += load_compat * 0.3
    findings.append(f"Lasttyp-Kompatibilität ({load_type}): {load_compat:.0%}")

    # Moisture content penalty
    if moisture_content_pct < 9:
        score -= 0.1
        findings.append("WARNUNG: Holzfeuchte zu niedrig (<9%) - Risiko von Quellung bei Feuchtigkeitsaufnahme")
        critical_points.append("Holzfeuchte-bedingte Spannungen unter zyklischen Bedingungen")
    elif moisture_content_pct > 16:
        score -= 0.15
        findings.append("WARNUNG: Holzfeuchte zu hoch (>16%) - Quellung und Pressspannungs-Probleme")
        critical_points.append("Übermaßiges Quellen und interne Spannungen")
    else:
        findings.append(f"Holzfeuchte optimal ({moisture_content_pct}%)")

    # Service life estimation
    if score > 0.90:
        service_life = 30
        quality_rating = "Ausgezeichnet"
    elif score > 0.80:
        service_life = 20
        quality_rating = "Sehr Gut"
    elif score > 0.70:
        service_life = 15
        quality_rating = "Gut"
    elif score > 0.60:
        service_life = 10
        quality_rating = "Befriedigend"
    else:
        service_life = 5
        quality_rating = "Ausreichend (Kritisch)"

    # Location-specific adjustments
    if location == "underwater":
        service_life *= 0.8
        recommendations.append("Unterwasser-Bereich: Strenge Inspektions-Intervalle (jährlich), biologischer Bewuchs prüfen")
        critical_points.append("Biologische Zersetzung unter Wasserlinie (Holzwürmer, Pilze)")
    elif location == "deck":
        service_life *= 0.95
        recommendations.append("Deck: UV-Schutz kritisch, Wartung alle 12 Monate erforderlich")
        critical_points.append("UV-Strahlung und Salzwasser-Zyklus erzeugt Quellung/Schwindung")
    elif location == "cabin":
        service_life *= 1.1
        recommendations.append("Kabinen-Interior: Geschützte Umgebung erlaubt längere Lebensdauer")

    # Specific technical recommendations
    if joint_type == "scarph_joint" or joint_type == "epoxy_scarf":
        recommendations.append(f"Schäft-Länge: min. {joint_data.get('minimum_scarph_ratio', 8)}x Holzdicke")
        recommendations.append("Oberflächenrauhheit Ra 1.6-3.2µm vor Leimung erforderlich")
        recommendations.append("Pressdruck: 600-1000 kPa, Aushärtungszeit min. 24 Stunden bei 18-22°C")

    if joint_data.get("clamping_pressure_kpa"):
        recommendations.append(f"Pressdruck-Bereich: {joint_data['clamping_pressure_kpa']-100} bis {joint_data['clamping_pressure_kpa']+200} kPa")

    if joint_data.get("glue_line_thickness_mm"):
        recommendations.append(f"Leimfugen-Dicke: {joint_data['glue_line_thickness_mm']} mm (Toleranz ±0.1mm)")

    recommendations.append(f"Ideal Holzfeuchte bei Verleimung: {joint_data.get('moisture_content_requirement_pct', '9-14')}%")

    # Compile final score
    score = max(0.0, min(1.0, score))

    return {
        "joint_type": joint_type,
        "wood_species": wood_species,
        "location": location,
        "load_type": load_type,
        "suitability_score": round(score, 3),
        "quality_rating": quality_rating,
        "estimated_service_life_years": service_life,
        "findings": findings,
        "recommendations": recommendations,
        "critical_points": critical_points,
        "maintenance_required": service_life <= 15,
        "maintenance_interval_months": 12 if location == "exterior" else 24,
        "notes": {
            "strength_base": joint_data["strength_rating"],
            "water_resistance": joint_data.get("water_resistance", "unknown"),
            "adhesive": joint_data.get("adhesive_recommendation", "See joint data"),
            "clamping_time_hours": joint_data.get("clamping_time_hours", 24),
            "common_failures": joint_data.get("common_failures", [])
        }
    }


# ============================================================================
# QUICK REFERENCE QUALITY STANDARDS
# ============================================================================

QUALITY_STANDARDS = {
    "surface_finish_ra_um": {
        "rough_sawn": 6.3,
        "hand_planed": 3.2,
        "machine_planed": 1.6,
        "fine_sanded_220": 0.8,
        "extra_fine_sanded_320": 0.4,
        "before_finish_coating": 1.6
    },
    "moisture_content_ranges_pct": {
        "fresh_sawn": "25-60%",
        "air_dried": "12-20%",
        "kiln_dried_standard": "10-15%",
        "ideal_before_finishing": "9-14%",
        "ideal_before_assembly": "8-12%",
        "marine_exposure": "10-18% (variabel)"
    },
    "clamping_pressure_typical_kpa": {
        "light_assembly": 200,
        "standard_joinery": 400,
        "structural_joints": 600,
        "scarph_joints": 800,
        "finger_joints": 800,
        "maximum_safe": 1200
    },
    "glue_line_thickness_mm": {
        "minimum": 0.1,
        "ideal": 0.2,
        "maximum_before_weakness": 0.5
    }
}


# End of craftsmanship_wood.py
