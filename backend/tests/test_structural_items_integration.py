"""
Tests: measured StructuralItems enter the structural analysis as point masses.

Closes the audit finding "StructuralItems are loaded but never handed to the
structural module" — and pins the physics: a measured mass must visibly move
the CG/trim/loading results, tanks must scale with fill level, and items
without position/weight must be skipped WITH a warning (never silently).
"""

from app.services.analysis.structural import (
    analyze_fore_aft_balance,
    analyze_lateral_balance,
    analyze_loading_conditions,
    analyze_trim,
    run_structural_analysis,
    BOAT_CLASS_DEFAULTS,
)

# Symmetric two-zone layout, 10 m × 3 m, CG exactly at 50 %
ZONES = [
    {"name": "Vorschiff", "zone_type": "cabin",
     "polygon": [[0, 0], [5000, 0], [5000, 3000], [0, 3000]]},
    {"name": "Achterschiff", "zone_type": "cabin",
     "polygon": [[5000, 0], [10000, 0], [10000, 3000], [5000, 3000]]},
]

HEAVY_AFT_ITEM = {
    "name": "Motor", "item_type": "engine", "weight_kg": 2000.0,
    "position_x_mm": 9500.0, "position_y_mm": 1500.0, "position_z_mm": None,
}


def _config() -> dict:
    config = BOAT_CLASS_DEFAULTS["cruising_sail"].copy()
    config.pop("weights", None)
    return config


def test_measured_mass_shifts_fore_aft_cog():
    _, _, base = analyze_fore_aft_balance(ZONES, _config())
    _, _, with_item = analyze_fore_aft_balance(
        ZONES, _config(), structural_items=[HEAVY_AFT_ITEM]
    )
    assert with_item["cog_x_pct"] > base["cog_x_pct"], (
        "2 t at x=9.5 m must pull the CG toward that end"
    )


def test_measured_mass_shifts_trim():
    _, _, base = analyze_trim(ZONES, _config())
    _, _, with_item = analyze_trim(
        ZONES, _config(), structural_items=[HEAVY_AFT_ITEM]
    )
    assert with_item["trim_deg"] != base["trim_deg"]
    assert with_item["cog_x_pct"] > base["cog_x_pct"]


def test_measured_mass_shifts_lateral_cog():
    item = dict(HEAVY_AFT_ITEM, position_y_mm=2900.0)  # far starboard
    _, _, base = analyze_lateral_balance(ZONES, _config())
    _, _, with_item = analyze_lateral_balance(
        ZONES, _config(), structural_items=[item]
    )
    assert with_item["cog_y_pct"] > base["cog_y_pct"]


def test_tank_items_scale_with_loading_condition():
    tank = {
        "name": "Dieseltank", "item_type": "fuel_tank", "weight_kg": 400.0,
        "position_x_mm": 9000.0, "position_y_mm": 1500.0,
    }
    _, _, metrics = analyze_loading_conditions(
        ZONES, _config(), structural_items=[tank]
    )
    conditions = metrics["conditions"]
    # Full fuel pulls the CG further toward the tank than nearly-empty fuel
    assert conditions["full_departure"] > conditions["arrival"], conditions


def test_fixed_items_do_not_scale_with_condition():
    _, _, metrics = analyze_loading_conditions(
        ZONES, _config(), structural_items=[HEAVY_AFT_ITEM]
    )
    conditions = metrics["conditions"]
    # An engine is fixed mass: its CG contribution is condition-independent.
    # (Zone weights still vary slightly, but full vs arrival must not differ
    # as much as for a tank at the same position.)
    assert abs(conditions["full_departure"] - conditions["arrival"]) < 0.02


def test_items_without_position_are_skipped_with_warning():
    incomplete = {"name": "Batterie", "item_type": "battery", "weight_kg": 60.0,
                  "position_x_mm": None, "position_y_mm": None}
    result = run_structural_analysis(
        ZONES, [], "cruising_sail",
        structural_items=[HEAVY_AFT_ITEM, incomplete],
    )
    measured = result["metrics"]["measured_items"]
    assert measured["count"] == 1
    assert measured["skipped_without_position_or_weight"] == 1
    codes = {w["code"] for w in result["warnings"]}
    assert "STRUCTURAL_ITEMS_SKIPPED" in codes
    assert "STRUCTURAL_MEASURED_ITEMS_USED" in codes


def test_no_items_keeps_previous_behaviour():
    base = run_structural_analysis(ZONES, [], "cruising_sail")
    explicit_none = run_structural_analysis(
        ZONES, [], "cruising_sail", structural_items=None
    )
    assert base["sub_scores"] == explicit_none["sub_scores"]
    assert "measured_items" not in base["metrics"]


def test_run_reports_measured_share():
    result = run_structural_analysis(
        ZONES, [], "cruising_sail", structural_items=[HEAVY_AFT_ITEM]
    )
    measured = result["metrics"]["measured_items"]
    assert measured["total_weight_kg"] == 2000.0
    assert 0 < measured["share_of_model_weight_pct"] <= 100


# ---------------------------------------------------------------------------
# Regressions from the adversarial review (frame dilation, double counting,
# sub-model inconsistency, tank-type substring matching)
# ---------------------------------------------------------------------------


def test_bow_item_outside_extents_pulls_cog_forward():
    # KRITISCH regression: extending the evaluation frame by item positions
    # INVERTED the direction — 100 kg anchor chain AHEAD of the zones raised
    # cog_x_pct and warned "zu weit achtern". Physically bow weight must pull
    # the CG toward the bow (lower pct), frame fixed to zone extents.
    anchor = {"name": "Ankerkette", "item_type": "anchor_chain",
              "weight_kg": 100.0, "position_x_mm": -2000.0, "position_y_mm": 1500.0}
    _, _, base = analyze_fore_aft_balance(ZONES, _config())
    _, warnings, with_item = analyze_fore_aft_balance(
        ZONES, _config(), structural_items=[anchor]
    )
    assert with_item["cog_x_pct"] < base["cog_x_pct"], (
        "bow weight must move the CG toward the bow, not aft"
    )
    assert not any(w["code"] == "COG_TOO_FAR_AFT" for w in warnings)
    assert 0.0 <= with_item["cog_x_pct"] <= 1.0


def test_tiny_lateral_outlier_does_not_zero_the_score():
    # 15 kg outboard on a davit at y=4500 previously collapsed the lateral
    # score to 0 by dilating the y-frame. With a fixed frame the physical
    # offset of 15 kg on ~2 t model mass is negligible.
    outboard = {"name": "Außenborder", "item_type": "other",
                "weight_kg": 15.0, "position_x_mm": 9000.0, "position_y_mm": 4500.0}
    score, _, metrics = analyze_lateral_balance(
        ZONES, _config(), structural_items=[outboard]
    )
    assert score == 100.0, metrics


def test_measured_engine_replaces_engine_zone_heuristic():
    # HOCH regression: the 350 kg/m² engine-zone heuristic already CONTAINS
    # the engine. A measured engine assigned to that zone must replace the
    # zone's share, not stack on it (double counting kipped CG/trim).
    zones = ZONES + [
        {"name": "Motorraum", "zone_type": "engine",
         "polygon": [[8000, 1000], [10000, 1000], [10000, 2000], [8000, 2000]]},
    ]
    engine = {"name": "Volvo", "item_type": "engine", "weight_kg": 700.0,
              "zone_name": "Motorraum",
              "position_x_mm": 9000.0, "position_y_mm": 1500.0}
    _, _, zone_only = analyze_fore_aft_balance(zones, _config())
    _, _, with_measured = analyze_fore_aft_balance(
        zones, _config(), structural_items=[engine]
    )
    # Engine-zone heuristic: 2 m² × 350 = 700 kg — measured 700 kg at the
    # zone centroid must leave the CG (nearly) unchanged, not shift it twice.
    assert abs(with_measured["cog_x_pct"] - zone_only["cog_x_pct"]) < 0.01, (
        zone_only, with_measured,
    )


def test_deduction_reported_in_metrics():
    engine = {"name": "Volvo", "item_type": "engine", "weight_kg": 500.0,
              "zone_name": "Achterschiff",
              "position_x_mm": 7500.0, "position_y_mm": 1500.0}
    result = run_structural_analysis(
        ZONES, [], "cruising_sail", structural_items=[engine]
    )
    measured = result["metrics"]["measured_items"]
    assert measured["deducted_from_zone_heuristics_kg"] == 500.0


def test_heavy_placement_sees_measured_engine_without_engine_zone():
    # HOCH regression: with no engine ZONE, heavy_placement returned 100
    # ("keine schweren Zonen") although a measured 2-t engine sat at 95 %.
    result = run_structural_analysis(
        ZONES, [], "cruising_sail", structural_items=[HEAVY_AFT_ITEM]
    )
    assert result["sub_scores"]["heavy_placement"] < 100.0
    codes = {w["code"] for w in result["warnings"]}
    assert "HEAVY_ZONE_OFF_CENTER" in codes
    assert "STRUCTURAL_NO_HEAVY_ZONES" not in codes


def test_load_concentration_sees_measured_items():
    result = run_structural_analysis(
        ZONES, [], "cruising_sail", structural_items=[HEAVY_AFT_ITEM]
    )
    fractions = result["metrics"]["load_concentration"]["segment_fractions"]
    assert fractions["stern"] > fractions["bow"], fractions


def test_watermaker_is_fixed_mass_not_water_ballast():
    # MITTEL regression: substring matching scaled a 'watermaker' with the
    # water fill level — a fixed machine vanished from light_ship.
    watermaker = {"name": "Wassermacher", "item_type": "other",
                  "weight_kg": 80.0, "position_x_mm": 8000.0,
                  "position_y_mm": 1500.0}
    _, _, metrics = analyze_loading_conditions(
        ZONES, _config(), structural_items=[watermaker]
    )
    conditions = metrics["conditions"]
    assert abs(conditions["light_ship"] - conditions["full_departure"]) < 0.02


def test_outside_extents_item_flagged():
    anchor = {"name": "Ankerkette", "item_type": "anchor_chain",
              "weight_kg": 100.0, "position_x_mm": -2000.0,
              "position_y_mm": 1500.0}
    result = run_structural_analysis(
        ZONES, [], "cruising_sail", structural_items=[anchor]
    )
    measured = result["metrics"]["measured_items"]
    assert measured["outside_zone_extents"] == ["Ankerkette"]
    codes = {w["code"] for w in result["warnings"]}
    assert "STRUCTURAL_ITEM_OUTSIDE_EXTENTS" in codes
