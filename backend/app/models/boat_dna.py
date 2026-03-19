"""BoatDNA — individualized yacht project identity profile.

Captures the full identity of a yacht project across 5 dimensions:
core identity, purpose/usage, builder profile, construction, and design
philosophy. Drives all analysis thresholds via BoatDNAResolver.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar

VALID_PROPULSIONS = frozenset({"sail", "motor", "sail_motor"})
VALID_USES = frozenset({
    "daysailing", "coastal_cruising", "offshore_cruising", "bluewater",
    "racing", "racing_cruiser", "weekender", "charter", "explorer",
    "sport_fishing", "flybridge_cruiser", "superyacht_private",
})
VALID_WATERS = frozenset({"sheltered", "coastal", "offshore", "ocean"})
VALID_DURATIONS = frozenset({"day", "weekend", "week", "extended", "liveaboard"})
VALID_PRODUCTION_TYPES = frozenset({"mass_production", "semi_custom", "full_custom", "one_off"})
VALID_QUALITY_TIERS = frozenset({"standard", "premium", "luxury", "superyacht"})
VALID_HULL_MATERIALS = frozenset({
    "grp_solid", "grp_sandwich", "carbon_composite",
    "aluminium", "steel", "wood_epoxy", "wood_traditional",
})
VALID_HULL_CONSTRUCTIONS = frozenset({
    "hand_layup", "vacuum_bag", "resin_infusion", "prepreg_autoclave",
    "welded", "riveted", "cold_molded", "strip_plank", "carvel",
})
VALID_CORE_MATERIALS = frozenset({"none", "balsa", "pvc_foam", "soric", "honeycomb", "cedar"})
VALID_DECK_MATERIALS = frozenset({"grp_nonskid", "teak_laid", "synthetic_teak", "cork", "paint"})
VALID_DESIGN_PRIORITIES = frozenset({
    "performance", "comfort", "luxury", "functionality",
    "tradition", "innovation", "value",
})
VALID_AESTHETIC_STYLES = frozenset({
    "classic", "modern", "retro_modern", "sporty",
    "minimalist", "traditional", "industrial",
})
VALID_INTERIOR_FOCUSES = frozenset({
    "spartan_functional", "comfortable_practical",
    "refined_elegant", "opulent_luxury",
})


def _validate_in(value, allowed: frozenset, field_name: str) -> None:
    if value not in allowed:
        raise ValueError(
            f"{field_name} must be one of {sorted(allowed)}, got '{value}'"
        )


@dataclass
class BoatDNA:
    """The complete identity profile of a specific yacht project."""

    # --- Core Identity ---
    propulsion: str
    length_m: float
    beam_m: float

    # --- Purpose & Usage ---
    primary_use: str
    operating_waters: str
    typical_crew: int
    max_crew: int
    typical_duration: str

    # --- Builder Profile ---
    production_type: str
    annual_production: int
    builder_quality_tier: str

    # --- Construction ---
    hull_material: str
    hull_construction: str
    core_material: str
    deck_material: str

    # --- Design Philosophy ---
    design_priority: str
    aesthetic_style: str
    interior_focus: str

    # --- Internal ---
    _legacy_class: str | None = field(default=None, repr=False)

    # --- Class-level presets (not a dataclass field) ---
    _PRESETS: ClassVar[dict[str, dict]] = {
        "small_sail": dict(
            propulsion="sail", length_m=10.0, beam_m=3.2,
            primary_use="coastal_cruising", operating_waters="coastal",
            typical_crew=4, max_crew=6, typical_duration="weekend",
            production_type="mass_production", annual_production=50,
            builder_quality_tier="standard",
            hull_material="grp_solid", hull_construction="hand_layup",
            core_material="none", deck_material="grp_nonskid",
            design_priority="value", aesthetic_style="modern",
            interior_focus="comfortable_practical",
        ),
        "cruising_sail": dict(
            propulsion="sail", length_m=13.0, beam_m=3.8,
            primary_use="offshore_cruising", operating_waters="offshore",
            typical_crew=4, max_crew=6, typical_duration="extended",
            production_type="semi_custom", annual_production=20,
            builder_quality_tier="premium",
            hull_material="grp_sandwich", hull_construction="resin_infusion",
            core_material="pvc_foam", deck_material="teak_laid",
            design_priority="comfort", aesthetic_style="modern",
            interior_focus="comfortable_practical",
        ),
        "large_motor": dict(
            propulsion="motor", length_m=20.0, beam_m=5.2,
            primary_use="flybridge_cruiser", operating_waters="offshore",
            typical_crew=4, max_crew=8, typical_duration="week",
            production_type="semi_custom", annual_production=10,
            builder_quality_tier="luxury",
            hull_material="grp_sandwich", hull_construction="resin_infusion",
            core_material="pvc_foam", deck_material="teak_laid",
            design_priority="comfort", aesthetic_style="modern",
            interior_focus="refined_elegant",
        ),
        "superyacht": dict(
            propulsion="motor", length_m=35.0, beam_m=7.5,
            primary_use="superyacht_private", operating_waters="ocean",
            typical_crew=6, max_crew=18, typical_duration="liveaboard",
            production_type="full_custom", annual_production=0,
            builder_quality_tier="superyacht",
            hull_material="aluminium", hull_construction="welded",
            core_material="none", deck_material="teak_laid",
            design_priority="luxury", aesthetic_style="modern",
            interior_focus="opulent_luxury",
        ),
    }

    def __post_init__(self) -> None:
        _validate_in(self.propulsion, VALID_PROPULSIONS, "propulsion")
        if not (2.5 <= self.length_m <= 100):
            raise ValueError(f"length_m must be 2.5–100, got {self.length_m}")
        if self.beam_m <= 0 or self.beam_m >= self.length_m:
            raise ValueError(
                f"beam_m must be positive and less than length_m, got {self.beam_m}"
            )
        _validate_in(self.primary_use, VALID_USES, "primary_use")
        _validate_in(self.operating_waters, VALID_WATERS, "operating_waters")
        _validate_in(self.typical_duration, VALID_DURATIONS, "typical_duration")
        _validate_in(self.production_type, VALID_PRODUCTION_TYPES, "production_type")
        _validate_in(self.builder_quality_tier, VALID_QUALITY_TIERS, "builder_quality_tier")
        _validate_in(self.hull_material, VALID_HULL_MATERIALS, "hull_material")
        _validate_in(self.hull_construction, VALID_HULL_CONSTRUCTIONS, "hull_construction")
        _validate_in(self.core_material, VALID_CORE_MATERIALS, "core_material")
        _validate_in(self.deck_material, VALID_DECK_MATERIALS, "deck_material")
        _validate_in(self.design_priority, VALID_DESIGN_PRIORITIES, "design_priority")
        _validate_in(self.aesthetic_style, VALID_AESTHETIC_STYLES, "aesthetic_style")
        _validate_in(self.interior_focus, VALID_INTERIOR_FOCUSES, "interior_focus")

    def to_dict(self) -> dict:
        """Serialize to a plain dict (excludes _legacy_class)."""
        return {
            "propulsion": self.propulsion,
            "length_m": self.length_m,
            "beam_m": self.beam_m,
            "primary_use": self.primary_use,
            "operating_waters": self.operating_waters,
            "typical_crew": self.typical_crew,
            "max_crew": self.max_crew,
            "typical_duration": self.typical_duration,
            "production_type": self.production_type,
            "annual_production": self.annual_production,
            "builder_quality_tier": self.builder_quality_tier,
            "hull_material": self.hull_material,
            "hull_construction": self.hull_construction,
            "core_material": self.core_material,
            "deck_material": self.deck_material,
            "design_priority": self.design_priority,
            "aesthetic_style": self.aesthetic_style,
            "interior_focus": self.interior_focus,
        }

    @classmethod
    def from_dict(cls, data: dict) -> BoatDNA:
        """Deserialize from a plain dict."""
        return cls(**{k: v for k, v in data.items() if not k.startswith("_")})

    @classmethod
    def from_boat_class(cls, boat_class: str) -> BoatDNA:
        """Create a BoatDNA from one of the 4 legacy class presets."""
        if boat_class not in cls._PRESETS:
            raise ValueError(
                f"Unknown boat class: '{boat_class}'. "
                f"Must be one of {sorted(cls._PRESETS)}"
            )
        dna = cls(**cls._PRESETS[boat_class])
        object.__setattr__(dna, "_legacy_class", boat_class)
        return dna

    @classmethod
    def from_public_specs(cls, specs: dict) -> BoatDNA:
        """Infer a full BoatDNA from minimal public specs (Level 1).

        Required keys: length_m, propulsion.
        Optional keys: beam_m, primary_use, operating_waters, typical_crew,
                       max_crew, typical_duration.
        """
        length = specs["length_m"]
        propulsion = specs["propulsion"]
        beam = specs.get("beam_m", length * (0.28 if propulsion == "sail" else 0.26))

        # Infer primary_use from length + propulsion
        if "primary_use" in specs:
            use = specs["primary_use"]
        elif propulsion == "sail":
            use = "coastal_cruising" if length < 12 else "offshore_cruising"
        elif propulsion == "motor":
            if length < 12:
                use = "weekender"
            elif length < 20:
                use = "flybridge_cruiser"
            else:
                use = "superyacht_private" if length >= 28 else "flybridge_cruiser"
        else:
            use = "coastal_cruising"

        # Infer operating_waters
        waters_map = {
            "daysailing": "sheltered", "weekender": "coastal",
            "coastal_cruising": "coastal", "offshore_cruising": "offshore",
            "bluewater": "ocean", "racing": "offshore",
            "racing_cruiser": "offshore", "charter": "coastal",
            "explorer": "ocean", "sport_fishing": "coastal",
            "flybridge_cruiser": "offshore",
            "superyacht_private": "ocean",
        }
        waters = specs.get("operating_waters", waters_map.get(use, "coastal"))

        # Infer production type
        if length < 12:
            prod = "mass_production"
        elif length < 20:
            prod = "semi_custom"
        else:
            prod = "full_custom"

        # Infer quality tier
        tier_map = {
            "mass_production": "standard",
            "semi_custom": "premium",
            "full_custom": "luxury",
        }
        tier = tier_map.get(prod, "luxury")
        if length >= 28:
            tier = "superyacht"

        # Infer hull
        if propulsion == "sail":
            hull_mat = "grp_solid" if length < 12 else "grp_sandwich"
            hull_con = "hand_layup" if length < 12 else "resin_infusion"
        else:
            if length >= 28:
                hull_mat, hull_con = "aluminium", "welded"
            else:
                hull_mat, hull_con = "grp_sandwich", "resin_infusion"

        crew = specs.get("typical_crew", max(2, int(length / 3)))
        max_c = specs.get("max_crew", crew + 2)
        duration = specs.get("typical_duration", "weekend" if length < 12 else "week")

        return cls(
            propulsion=propulsion, length_m=length, beam_m=beam,
            primary_use=use, operating_waters=waters,
            typical_crew=crew, max_crew=max_c, typical_duration=duration,
            production_type=prod, annual_production=20 if prod == "mass_production" else 5,
            builder_quality_tier=tier,
            hull_material=hull_mat, hull_construction=hull_con,
            core_material="pvc_foam" if "sandwich" in hull_mat else "none",
            deck_material="grp_nonskid",
            design_priority="comfort", aesthetic_style="modern",
            interior_focus="comfortable_practical",
        )
