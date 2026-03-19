"""Tests for BoatDNA dataclass."""
import pytest
from app.models.boat_dna import BoatDNA

# ---------------------------------------------------------------------------
# Allowed value sets
# ---------------------------------------------------------------------------

VALID_PROPULSIONS = {"sail", "motor", "sail_motor"}
VALID_USES = {
    "daysailing", "coastal_cruising", "offshore_cruising", "bluewater",
    "racing", "racing_cruiser", "weekender", "charter", "explorer",
    "sport_fishing", "flybridge_cruiser", "superyacht_private",
}
VALID_WATERS = {"sheltered", "coastal", "offshore", "ocean"}
VALID_DURATIONS = {"day", "weekend", "week", "extended", "liveaboard"}
VALID_PRODUCTION_TYPES = {"mass_production", "semi_custom", "full_custom", "one_off"}
VALID_QUALITY_TIERS = {"standard", "premium", "luxury", "superyacht"}


def _make_dna(**overrides) -> BoatDNA:
    """Build a valid BoatDNA with sensible defaults, overriding specific fields."""
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


def test_valid_construction():
    """A BoatDNA with all valid fields constructs without error."""
    dna = _make_dna()
    assert dna.propulsion == "sail"
    assert dna.length_m == 12.0
    assert dna._legacy_class is None


def test_validation_invalid_propulsion():
    with pytest.raises(ValueError, match="propulsion"):
        _make_dna(propulsion="nuclear")


def test_validation_length_too_small():
    with pytest.raises(ValueError, match="length_m"):
        _make_dna(length_m=1.0)


def test_validation_length_too_large():
    with pytest.raises(ValueError, match="length_m"):
        _make_dna(length_m=150.0)


def test_validation_beam_negative():
    with pytest.raises(ValueError, match="beam_m"):
        _make_dna(beam_m=-1.0)


def test_validation_beam_exceeds_length():
    with pytest.raises(ValueError, match="beam_m"):
        _make_dna(length_m=10.0, beam_m=15.0)


def test_validation_invalid_use():
    with pytest.raises(ValueError, match="primary_use"):
        _make_dna(primary_use="submarine")


def test_validation_invalid_waters():
    with pytest.raises(ValueError, match="operating_waters"):
        _make_dna(operating_waters="space")


def test_validation_invalid_duration():
    with pytest.raises(ValueError, match="typical_duration"):
        _make_dna(typical_duration="yearly")


def test_validation_invalid_production_type():
    with pytest.raises(ValueError, match="production_type"):
        _make_dna(production_type="3d_printed")


def test_validation_invalid_quality_tier():
    with pytest.raises(ValueError, match="builder_quality_tier"):
        _make_dna(builder_quality_tier="ultra")


# ---------------------------------------------------------------------------
# from_boat_class
# ---------------------------------------------------------------------------

LEGACY_CLASSES = ["small_sail", "cruising_sail", "large_motor", "superyacht"]


@pytest.mark.parametrize("boat_class", LEGACY_CLASSES)
def test_from_boat_class_valid(boat_class):
    """Each preset produces a valid BoatDNA with _legacy_class set."""
    dna = BoatDNA.from_boat_class(boat_class)
    assert dna._legacy_class == boat_class
    assert dna.length_m > 0
    assert dna.propulsion in VALID_PROPULSIONS


def test_from_boat_class_unknown():
    with pytest.raises(ValueError, match="Unknown boat class"):
        BoatDNA.from_boat_class("submarine")


def test_from_boat_class_small_sail_profile():
    dna = BoatDNA.from_boat_class("small_sail")
    assert dna.propulsion == "sail"
    assert dna.length_m == 10.0
    assert dna.builder_quality_tier == "standard"
    assert dna.production_type == "mass_production"


def test_from_boat_class_superyacht_profile():
    dna = BoatDNA.from_boat_class("superyacht")
    assert dna.propulsion == "motor"
    assert dna.length_m == 35.0
    assert dna.builder_quality_tier == "superyacht"
    assert dna.production_type == "full_custom"


# ---------------------------------------------------------------------------
# from_public_specs
# ---------------------------------------------------------------------------


def test_from_public_specs_minimal():
    """Just length + propulsion fills all fields."""
    dna = BoatDNA.from_public_specs({"length_m": 10.0, "propulsion": "sail"})
    assert dna._legacy_class is None
    assert dna.beam_m > 0
    assert dna.primary_use in VALID_USES
    assert dna.operating_waters in VALID_WATERS


def test_from_public_specs_preserves_provided():
    """Provided values are not overwritten by heuristics."""
    dna = BoatDNA.from_public_specs({
        "length_m": 12.0, "propulsion": "motor",
        "primary_use": "charter", "beam_m": 4.0,
    })
    assert dna.primary_use == "charter"
    assert dna.beam_m == 4.0


def test_from_public_specs_beam_inference():
    """Beam inferred from length when not provided."""
    dna = BoatDNA.from_public_specs({"length_m": 10.0, "propulsion": "sail"})
    assert abs(dna.beam_m - 10.0 * 0.28) < 0.01


def test_from_public_specs_no_legacy_flag():
    dna = BoatDNA.from_public_specs({"length_m": 10.0, "propulsion": "sail"})
    assert dna._legacy_class is None


def test_from_public_specs_missing_required():
    with pytest.raises((ValueError, KeyError)):
        BoatDNA.from_public_specs({"propulsion": "sail"})  # no length


# ---------------------------------------------------------------------------
# Round-trip
# ---------------------------------------------------------------------------


@pytest.mark.parametrize("boat_class", LEGACY_CLASSES)
def test_round_trip(boat_class):
    """from_boat_class -> to_dict -> from_dict produces identical DNA (minus _legacy_class)."""
    dna = BoatDNA.from_boat_class(boat_class)
    restored = BoatDNA.from_dict(dna.to_dict())
    assert restored.to_dict() == dna.to_dict()


# ---------------------------------------------------------------------------
# Construction knowledge
# ---------------------------------------------------------------------------

from app.domain.construction import CONSTRUCTION_KNOWLEDGE, get_construction_knowledge


def test_construction_knowledge_has_six_entries():
    assert len(CONSTRUCTION_KNOWLEDGE) == 6


def test_construction_knowledge_required_keys():
    required = {"description", "typical_boats", "strengths", "weaknesses",
                "quality_indicators_visual", "known_issues"}
    for key, entry in CONSTRUCTION_KNOWLEDGE.items():
        assert required.issubset(entry.keys()), f"Missing keys in {key}"


def test_construction_knowledge_lookup_hit():
    entry = get_construction_knowledge("aluminium", "welded")
    assert entry is not None
    assert "description" in entry


def test_construction_knowledge_lookup_miss():
    assert get_construction_knowledge("titanium", "3d_printed") is None
