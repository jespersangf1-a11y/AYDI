"""Tests for BoatDNAResolver — backward compat + continuous scaling."""
import pytest
from app.models.boat_dna import BoatDNA
from app.services.boat_dna_resolver import BoatDNAResolver

# Import BOAT_CLASS_DEFAULTS from every module
from app.services.analysis.ergonomics import BOAT_CLASS_DEFAULTS as ERGO_DEFAULTS
from app.services.analysis.compliance import BOAT_CLASS_DEFAULTS as COMP_DEFAULTS
from app.services.analysis.structural import BOAT_CLASS_DEFAULTS as STRUCT_DEFAULTS
from app.services.analysis.production import BOAT_CLASS_DEFAULTS as PROD_DEFAULTS
from app.services.analysis.cost import BOAT_CLASS_DEFAULTS as COST_DEFAULTS
from app.services.analysis.emotional import BOAT_CLASS_DEFAULTS as EMO_DEFAULTS
from app.services.analysis.materials import BOAT_CLASS_DEFAULTS as MAT_DEFAULTS
from app.services.analysis.volume_storage import BOAT_CLASS_DEFAULTS as VOL_DEFAULTS
from app.services.analysis.brand_dna import BOAT_CLASS_DEFAULTS as BRAND_DEFAULTS
from app.services.analysis.market import BOAT_CLASS_DEFAULTS as MARKET_DEFAULTS
from app.services.analysis.service_patterns import BOAT_CLASS_DEFAULTS as SP_DEFAULTS

ALL_MODULE_DEFAULTS = {
    "ergonomics": ERGO_DEFAULTS,
    "compliance": COMP_DEFAULTS,
    "structural": STRUCT_DEFAULTS,
    "production": PROD_DEFAULTS,
    "cost": COST_DEFAULTS,
    "emotional": EMO_DEFAULTS,
    "materials": MAT_DEFAULTS,
    "volume_storage": VOL_DEFAULTS,
    "brand_dna": BRAND_DEFAULTS,
    "market": MARKET_DEFAULTS,
    "service_patterns": SP_DEFAULTS,
}

LEGACY_CLASSES = ["small_sail", "cruising_sail", "large_motor", "superyacht"]


# ---------------------------------------------------------------------------
# Backward compatibility — most critical tests
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("boat_class", LEGACY_CLASSES)
def test_backward_compat(boat_class):
    """Resolved config for legacy preset must exactly match BOAT_CLASS_DEFAULTS."""
    dna = BoatDNA.from_boat_class(boat_class)
    resolved = BoatDNAResolver().resolve(dna)

    for module_name, module_defaults in ALL_MODULE_DEFAULTS.items():
        legacy = module_defaults[boat_class].copy()
        legacy_weights = legacy.pop("weights")
        legacy_config = legacy

        res = resolved[module_name].copy()
        res_weights = res.pop("weights")
        res_config = res

        assert res_config == legacy_config, (
            f"{boat_class}/{module_name}: config mismatch.\n"
            f"Expected: {legacy_config}\nGot: {res_config}"
        )
        assert res_weights == legacy_weights, (
            f"{boat_class}/{module_name}: weights mismatch.\n"
            f"Expected: {legacy_weights}\nGot: {res_weights}"
        )


# ---------------------------------------------------------------------------
# Custom DNA helper
# ---------------------------------------------------------------------------

def _custom_dna(**overrides) -> BoatDNA:
    """Build a custom (non-legacy) DNA for testing continuous formulas."""
    defaults = dict(
        propulsion="sail", length_m=12.0, beam_m=3.8,
        primary_use="coastal_cruising", operating_waters="coastal",
        typical_crew=4, max_crew=6, typical_duration="weekend",
        production_type="semi_custom", annual_production=20,
        builder_quality_tier="premium",
        hull_material="grp_sandwich", hull_construction="resin_infusion",
        core_material="pvc_foam", deck_material="grp_nonskid",
        design_priority="comfort", aesthetic_style="modern",
        interior_focus="comfortable_practical",
    )
    defaults.update(overrides)
    return BoatDNA(**defaults)


# ---------------------------------------------------------------------------
# Continuous scaling — ergonomics
# ---------------------------------------------------------------------------

def test_passage_width_scales_with_length():
    short = _custom_dna(length_m=10.0)
    long = _custom_dna(length_m=16.0)
    r = BoatDNAResolver()
    assert r.resolve(short)["ergonomics"]["min_passage_width_mm"] < \
           r.resolve(long)["ergonomics"]["min_passage_width_mm"]


def test_heel_angle_by_propulsion():
    sail = _custom_dna(propulsion="sail")
    motor = _custom_dna(propulsion="motor", primary_use="flybridge_cruiser")
    r = BoatDNAResolver()
    assert r.resolve(sail)["ergonomics"]["heel_angle_deg"] > 0
    assert r.resolve(motor)["ergonomics"]["heel_angle_deg"] == 0


def test_heel_angle_racing_highest():
    racing = _custom_dna(primary_use="racing")
    cruising = _custom_dna(primary_use="coastal_cruising")
    r = BoatDNAResolver()
    assert r.resolve(racing)["ergonomics"]["heel_angle_deg"] >= \
           r.resolve(cruising)["ergonomics"]["heel_angle_deg"]


def test_motorsailer_reduced_heel():
    sail = _custom_dna(propulsion="sail")
    ms = _custom_dna(propulsion="sail_motor")
    r = BoatDNAResolver()
    assert 0 < r.resolve(ms)["ergonomics"]["heel_angle_deg"] < \
           r.resolve(sail)["ergonomics"]["heel_angle_deg"]


def test_crew_separation_charter_large():
    dna = _custom_dna(
        propulsion="motor", length_m=18.0, beam_m=5.0,
        primary_use="charter", typical_crew=6, max_crew=12,
    )
    assert BoatDNAResolver().resolve(dna)["ergonomics"]["crew_guest_separation"] is True


def test_crew_separation_small_private():
    dna = _custom_dna(length_m=10.0, typical_crew=3)
    assert BoatDNAResolver().resolve(dna)["ergonomics"]["crew_guest_separation"] is False


# ---------------------------------------------------------------------------
# Continuous scaling — compliance
# ---------------------------------------------------------------------------

def test_ce_category_from_waters():
    r = BoatDNAResolver()
    assert r.resolve(_custom_dna(operating_waters="ocean"))["compliance"]["ce_category"] == "A"
    assert r.resolve(_custom_dna(operating_waters="coastal"))["compliance"]["ce_category"] == "C"
    assert r.resolve(_custom_dna(operating_waters="sheltered"))["compliance"]["ce_category"] == "D"


def test_ce_category_b_for_small_offshore():
    dna = _custom_dna(length_m=8.0, beam_m=2.5, operating_waters="offshore")
    assert BoatDNAResolver().resolve(dna)["compliance"]["ce_category"] == "B"


# ---------------------------------------------------------------------------
# Continuous scaling — structural
# ---------------------------------------------------------------------------

def test_cog_range_sail_vs_motor():
    sail = _custom_dna(propulsion="sail")
    motor = _custom_dna(propulsion="motor", primary_use="flybridge_cruiser")
    r = BoatDNAResolver()
    sail_range = r.resolve(sail)["structural"]["ideal_cog_x_range"]
    motor_range = r.resolve(motor)["structural"]["ideal_cog_x_range"]
    assert sail_range[0] < motor_range[0]  # sail COG more forward


def test_trim_limit_by_propulsion():
    sail = _custom_dna(propulsion="sail")
    motor = _custom_dna(propulsion="motor", primary_use="flybridge_cruiser")
    r = BoatDNAResolver()
    assert r.resolve(sail)["structural"]["max_trim_deg"] == 2.0
    assert r.resolve(motor)["structural"]["max_trim_deg"] == 1.0


def test_weight_factor_scales_with_length():
    short = _custom_dna(length_m=8.0, beam_m=2.5)
    long = _custom_dna(length_m=30.0, beam_m=7.0)
    r = BoatDNAResolver()
    assert r.resolve(short)["structural"]["boat_class_weight_factor"] < \
           r.resolve(long)["structural"]["boat_class_weight_factor"]


# ---------------------------------------------------------------------------
# Continuous scaling — production
# ---------------------------------------------------------------------------

def test_flat_panel_by_production_type():
    r = BoatDNAResolver()
    mass = _custom_dna(production_type="mass_production")
    oneoff = _custom_dna(production_type="one_off")
    assert r.resolve(mass)["production"]["target_flat_panel_ratio"] == 0.70
    assert r.resolve(oneoff)["production"]["target_flat_panel_ratio"] == 0.40


def test_door_widths_superyacht_no_600():
    dna = _custom_dna(builder_quality_tier="superyacht")
    widths = BoatDNAResolver().resolve(dna)["production"]["standard_door_widths_mm"]
    assert 600 not in widths
    assert 700 in widths


# ---------------------------------------------------------------------------
# Continuous scaling — cost
# ---------------------------------------------------------------------------

def test_cost_benchmark_scales_with_tier():
    r = BoatDNAResolver()
    tiers = ["standard", "premium", "luxury", "superyacht"]
    benchmarks = []
    for tier in tiers:
        dna = _custom_dna(builder_quality_tier=tier)
        benchmarks.append(r.resolve(dna)["cost"]["benchmark_cost_per_meter"])
    assert benchmarks == sorted(benchmarks)  # strictly increasing


# ---------------------------------------------------------------------------
# Weight validation
# ---------------------------------------------------------------------------

def test_all_module_weights_sum_to_one():
    """For custom DNA, all module weight dicts must sum to 1.0."""
    profiles = [
        _custom_dna(),
        _custom_dna(propulsion="motor", primary_use="sport_fishing", length_m=9.0, beam_m=3.0),
        _custom_dna(propulsion="sail", primary_use="racing", length_m=15.0, beam_m=4.0),
        _custom_dna(builder_quality_tier="superyacht", length_m=30.0, beam_m=7.0),
    ]
    r = BoatDNAResolver()
    for dna in profiles:
        resolved = r.resolve(dna)
        for module_name, config in resolved.items():
            if module_name == "overall_weights":
                total = sum(config.values())
                assert abs(total - 1.0) < 1e-9, f"overall_weights sum={total} for {dna}"
                continue
            weights = config.get("weights", {})
            if weights:
                total = sum(weights.values())
                assert abs(total - 1.0) < 1e-9, (
                    f"{module_name} weights sum={total} for {dna}"
                )


# ---------------------------------------------------------------------------
# Required keys
# ---------------------------------------------------------------------------

def test_resolver_produces_all_required_keys():
    """Custom DNA config must have every key from BOAT_CLASS_DEFAULTS."""
    dna = _custom_dna()
    resolved = BoatDNAResolver().resolve(dna)
    for module_name, module_defaults in ALL_MODULE_DEFAULTS.items():
        reference = module_defaults["cruising_sail"]
        for key in reference:
            assert key in resolved[module_name], (
                f"{module_name} missing key '{key}'"
            )


# ---------------------------------------------------------------------------
# Edge cases
# ---------------------------------------------------------------------------

def test_extreme_small_boat():
    dna = _custom_dna(length_m=3.0, beam_m=1.5)
    resolved = BoatDNAResolver().resolve(dna)
    for module_name, config in resolved.items():
        if module_name == "overall_weights":
            continue
        for key, val in config.items():
            if key == "weights":
                continue
            if isinstance(val, (int, float)):
                assert val >= 0, f"{module_name}.{key} = {val} < 0"


def test_extreme_large_boat():
    dna = _custom_dna(
        propulsion="motor", length_m=50.0, beam_m=10.0,
        primary_use="superyacht_private", builder_quality_tier="superyacht",
        production_type="one_off",
    )
    resolved = BoatDNAResolver().resolve(dna)
    for module_name, config in resolved.items():
        if module_name == "overall_weights":
            continue
        for key, val in config.items():
            if key == "weights":
                continue
            if isinstance(val, (int, float)):
                assert val >= 0, f"{module_name}.{key} = {val} < 0"
