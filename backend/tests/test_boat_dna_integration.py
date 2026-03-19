"""Integration tests — run actual analysis modules with DNA-resolved configs."""
from tests.conftest import make_zone, make_passage
from app.models.boat_dna import BoatDNA
from app.services.boat_dna_resolver import BoatDNAResolver
from app.services.analysis.ergonomics import run_ergonomics_analysis
from app.services.analysis.structural import run_structural_analysis
from app.services.analysis.compliance import run_compliance_analysis
from app.services.analysis.cost import run_cost_analysis
from app.domain.construction import CONSTRUCTION_KNOWLEDGE, get_construction_knowledge


def _basic_zones():
    return [
        make_zone("salon", "salon", polygon=[[3000, 0], [7000, 0], [7000, 3000], [3000, 3000]]),
        make_zone("cabin", "cabin", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
        make_zone("engine", "engine", polygon=[[8000, 0], [10000, 0], [10000, 1500], [8000, 1500]]),
    ]


def _basic_passages():
    return [
        make_passage("salon", "cabin", width_mm=700),
        make_passage("salon", "engine", width_mm=600),
    ]


def test_ergonomics_with_dna_overrides():
    """Ergonomics module runs successfully with DNA-resolved config."""
    dna = BoatDNA(
        propulsion="sail", length_m=14.0, beam_m=4.2,
        primary_use="racing_cruiser", operating_waters="offshore",
        typical_crew=5, max_crew=8, typical_duration="week",
        production_type="semi_custom", annual_production=10,
        builder_quality_tier="premium",
        hull_material="grp_sandwich", hull_construction="resin_infusion",
        core_material="pvc_foam", deck_material="teak_laid",
        design_priority="performance", aesthetic_style="sporty",
        interior_focus="spartan_functional",
    )
    resolved = BoatDNAResolver().resolve(dna)
    config = resolved["ergonomics"].copy()
    config.pop("weights", None)

    result = run_ergonomics_analysis(
        _basic_zones(), _basic_passages(), "cruising_sail",
        config_overrides=config,
    )
    assert result["module"] == "ergonomics"
    assert 0 <= result["overall_score"] <= 100


def test_structural_with_dna_overrides():
    dna = BoatDNA(
        propulsion="motor", length_m=18.0, beam_m=5.0,
        primary_use="flybridge_cruiser", operating_waters="offshore",
        typical_crew=4, max_crew=8, typical_duration="week",
        production_type="semi_custom", annual_production=10,
        builder_quality_tier="luxury",
        hull_material="grp_sandwich", hull_construction="resin_infusion",
        core_material="pvc_foam", deck_material="teak_laid",
        design_priority="comfort", aesthetic_style="modern",
        interior_focus="refined_elegant",
    )
    resolved = BoatDNAResolver().resolve(dna)
    config = resolved["structural"].copy()
    config.pop("weights", None)

    result = run_structural_analysis(
        _basic_zones(), _basic_passages(), "large_motor",
        config_overrides=config,
    )
    assert result["module"] == "structural"
    assert 0 <= result["overall_score"] <= 100


def test_compliance_with_dna_overrides():
    dna = BoatDNA(
        propulsion="sail", length_m=12.0, beam_m=3.8,
        primary_use="offshore_cruising", operating_waters="offshore",
        typical_crew=4, max_crew=6, typical_duration="extended",
        production_type="semi_custom", annual_production=20,
        builder_quality_tier="premium",
        hull_material="grp_sandwich", hull_construction="resin_infusion",
        core_material="pvc_foam", deck_material="teak_laid",
        design_priority="comfort", aesthetic_style="modern",
        interior_focus="comfortable_practical",
    )
    resolved = BoatDNAResolver().resolve(dna)
    config = resolved["compliance"].copy()
    config.pop("weights", None)

    result = run_compliance_analysis(
        _basic_zones(), _basic_passages(), "cruising_sail",
        config_overrides=config,
    )
    assert result["module"] == "compliance"
    assert 0 <= result["overall_score"] <= 100


def test_legacy_mode_identical():
    """Legacy boat_class without DNA produces same result as existing code."""
    zones = _basic_zones()
    passages = _basic_passages()

    # Run without DNA override — pure legacy
    result_legacy = run_ergonomics_analysis(zones, passages, "cruising_sail")

    # Run with DNA override from legacy preset — should be identical
    dna = BoatDNA.from_boat_class("cruising_sail")
    resolved = BoatDNAResolver().resolve(dna)
    config = resolved["ergonomics"].copy()
    config.pop("weights", None)

    result_dna = run_ergonomics_analysis(
        zones, passages, "cruising_sail", config_overrides=config,
    )

    assert result_legacy["overall_score"] == result_dna["overall_score"]
    assert result_legacy["sub_scores"] == result_dna["sub_scores"]


def test_racing_sailboat_full_profile():
    """12m offshore racer — all modules produce valid results."""
    dna = BoatDNA(
        propulsion="sail", length_m=12.0, beam_m=3.6,
        primary_use="racing", operating_waters="offshore",
        typical_crew=6, max_crew=8, typical_duration="day",
        production_type="one_off", annual_production=0,
        builder_quality_tier="luxury",
        hull_material="carbon_composite", hull_construction="prepreg_autoclave",
        core_material="honeycomb", deck_material="paint",
        design_priority="performance", aesthetic_style="sporty",
        interior_focus="spartan_functional",
    )
    resolved = BoatDNAResolver().resolve_and_validate(dna)
    assert "ergonomics" in resolved
    assert "structural" in resolved
    assert "overall_weights" in resolved
    # Verify racing-specific values
    assert resolved["ergonomics"]["heel_angle_deg"] == 25
    assert resolved["structural"]["max_trim_deg"] == 2.0


def test_charter_motoryacht_profile():
    """18m charter motor yacht — crew separation should be on."""
    dna = BoatDNA(
        propulsion="motor", length_m=18.0, beam_m=5.0,
        primary_use="charter", operating_waters="coastal",
        typical_crew=6, max_crew=12, typical_duration="week",
        production_type="semi_custom", annual_production=8,
        builder_quality_tier="premium",
        hull_material="grp_sandwich", hull_construction="resin_infusion",
        core_material="pvc_foam", deck_material="synthetic_teak",
        design_priority="functionality", aesthetic_style="modern",
        interior_focus="comfortable_practical",
    )
    resolved = BoatDNAResolver().resolve(dna)
    assert resolved["ergonomics"]["crew_guest_separation"] is True
    assert resolved["ergonomics"]["heel_angle_deg"] == 0


def test_construction_knowledge_entries():
    """All 6 major combos have entries."""
    expected = [
        ("grp_solid", "hand_layup"),
        ("grp_sandwich", "resin_infusion"),
        ("aluminium", "welded"),
        ("carbon_composite", "prepreg_autoclave"),
        ("wood_epoxy", "cold_molded"),
        ("steel", "welded"),
    ]
    for mat, con in expected:
        entry = get_construction_knowledge(mat, con)
        assert entry is not None, f"Missing: {mat}_{con}"
        assert "description" in entry
        assert "known_issues" in entry


def test_construction_knowledge_fallback():
    """Unknown combo returns None."""
    assert get_construction_knowledge("titanium", "3d_printed") is None


def test_cost_with_dna_overrides():
    """Cost module runs successfully with DNA-resolved config."""
    from tests.conftest import make_cost_item

    dna = BoatDNA(
        propulsion="motor", length_m=15.0, beam_m=4.5,
        primary_use="flybridge_cruiser", operating_waters="coastal",
        typical_crew=4, max_crew=8, typical_duration="week",
        production_type="semi_custom", annual_production=15,
        builder_quality_tier="premium",
        hull_material="grp_sandwich", hull_construction="resin_infusion",
        core_material="pvc_foam", deck_material="teak_laid",
        design_priority="comfort", aesthetic_style="modern",
        interior_focus="comfortable_practical",
    )
    resolved = BoatDNAResolver().resolve(dna)
    config = resolved["cost"].copy()
    config.pop("weights", None)

    items = [
        make_cost_item("material", total_cost_eur=200_000, source="quote"),
        make_cost_item("labor", total_cost_eur=150_000, source="quote"),
        make_cost_item("equipment", total_cost_eur=80_000, source="quote"),
        make_cost_item("overhead", total_cost_eur=50_000, source="budget"),
    ]
    result = run_cost_analysis(
        _basic_zones(), _basic_passages(), "large_motor",
        config_overrides=config, cost_items=items, boat_length_m=15.0,
    )
    assert result["module"] == "cost"
    assert 0 <= result["overall_score"] <= 100


def test_quality_tolerances_by_tier():
    """Quality tolerance values scale by builder_quality_tier."""
    from app.services.visual.prompt_context import QUALITY_BY_TIER

    tiers = ["standard", "premium", "luxury", "superyacht"]
    for tier in tiers:
        assert tier in QUALITY_BY_TIER
    # Verify monotonic decrease in gap tolerance across tiers
    gaps = [QUALITY_BY_TIER[t]["joinery_gap_mm"] for t in tiers]
    assert gaps == sorted(gaps, reverse=True), f"Gaps not monotonically decreasing: {gaps}"
