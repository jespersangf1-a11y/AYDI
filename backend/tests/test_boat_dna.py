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
