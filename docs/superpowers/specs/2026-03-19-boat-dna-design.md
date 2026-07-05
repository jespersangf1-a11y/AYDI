> **⚠️ ARCHIV — HISTORISCHER PLANUNGSSTAND (nicht maßgeblich).**
> Dieses Dokument beschreibt einen früheren Planungs-/Design-Stand und trackt den aktuellen Code **nicht**.
> Bekannte Drift: 4 statt real **13 Bootsklassen** (`BoatClass`-Enum); abweichende Sub-Analysen/Gewichte; einzelne enthaltene Tests schlagen gegen den Ist-Code fehl.
> **Maßgeblich ist `CLAUDE.md`** (plus der Code). Nicht zum Ableiten von Enums, Return-Contracts oder Tests verwenden.

# Boat DNA — Individualized Boat Profile System

**Date:** 2026-03-19
**Status:** Design
**Replaces:** Rigid 4-class boat classification (small_sail, cruising_sail, large_motor, superyacht)

## Problem

The current system uses 4 hardcoded boat classes to drive all analysis thresholds, weights, and quality standards. A 12m offshore racer and a 12m gentleman's daysailer both map to "cruising_sail" despite having fundamentally different analysis requirements. The system needs to adapt to the **individual boat**, not a bucket.

## Approach: Resolver Layer (Backward-Compatible)

Rather than replacing `BOAT_CLASS_DEFAULTS` in all 11 modules (high blast radius, 457+ tests to update), we introduce a **resolver layer** that sits above the existing module infrastructure:

1. `BoatDNA` dataclass captures the full identity of a yacht project
2. `BoatDNAResolver` translates a DNA profile into the exact config dicts modules already consume
3. The 4 legacy classes become **presets** — named starting points that produce a BoatDNA
4. Modules keep their current signatures (`zones, passages, boat_class, config_overrides`)
5. DNA-resolved configs flow in as `config_overrides`, overriding the class defaults

**Key invariant:** A project with no BoatDNA behaves 100% identically to today.

## Architecture

```
                  BoatDNA (dataclass)
                       │
                       ▼
              BoatDNAResolver.resolve(dna)
                       │
         ┌─────────────┼─────────────────┐
         ▼             ▼                  ▼
  {"ergonomics":   {"compliance":    {"cost":
   {config...}}     {config...}}      {config...}}   ... (11 modules)
         │             │                  │
         ▼             ▼                  ▼
   config_overrides  config_overrides   config_overrides
         │             │                  │
         ▼             ▼                  ▼
   run_ergonomics()  run_compliance()  run_cost()
   (unchanged)       (unchanged)       (unchanged)
```

## Deliverables

### 1. `backend/app/models/boat_dna.py` — BoatDNA Dataclass

A pure Python dataclass (no ORM). Fields organized in 5 groups:

**Core Identity:**
- `propulsion: str` — "sail", "motor", "sail_motor"
- `length_m: float`
- `beam_m: float`

**Purpose & Usage:**
- `primary_use: str` — "daysailing", "coastal_cruising", "offshore_cruising", "bluewater", "racing", "racing_cruiser", "weekender", "charter", "explorer", "sport_fishing", "flybridge_cruiser", "superyacht_private"
- `operating_waters: str` — "sheltered", "coastal", "offshore", "ocean"
- `typical_crew: int`
- `max_crew: int`
- `typical_duration: str` — "day", "weekend", "week", "extended", "liveaboard"

**Builder Profile:**
- `production_type: str` — "mass_production", "semi_custom", "full_custom", "one_off"
- `annual_production: int` — 0 for one-off
- `builder_quality_tier: str` — "standard", "premium", "luxury", "superyacht"

**Construction:**
- `hull_material: str` — "grp_solid", "grp_sandwich", "carbon_composite", "aluminium", "steel", "wood_epoxy", "wood_traditional"
- `hull_construction: str` — "hand_layup", "vacuum_bag", "resin_infusion", "prepreg_autoclave", "welded", "riveted", "cold_molded", "strip_plank", "carvel"
- `core_material: str` — "none", "balsa", "pvc_foam", "soric", "honeycomb", "cedar"
- `deck_material: str` — "grp_nonskid", "teak_laid", "synthetic_teak", "cork", "paint"

**Design Philosophy:**
- `design_priority: str` — "performance", "comfort", "luxury", "functionality", "tradition", "innovation", "value"
- `aesthetic_style: str` — "classic", "modern", "retro_modern", "sporty", "minimalist", "traditional", "industrial"
- `interior_focus: str` — "spartan_functional", "comfortable_practical", "refined_elegant", "opulent_luxury"

**Class Methods:**

`BoatDNA.from_boat_class(boat_class: str) -> BoatDNA`
Maps legacy class names to canonical DNA profiles:
- `"small_sail"` → sail, 10m, 3.2m beam, coastal_cruising, coastal waters, 4 crew, mass_production, standard tier, grp_solid, hand_layup, etc.
- `"cruising_sail"` → sail, 13m, 3.8m beam, offshore_cruising, offshore waters, 6 crew, semi_custom, premium tier, grp_sandwich, resin_infusion, etc.
- `"large_motor"` → motor, 20m, 5.2m beam, flybridge_cruiser, offshore waters, 8 crew, semi_custom, luxury tier, grp_sandwich, resin_infusion, etc.
- `"superyacht"` → motor, 35m, 7.5m beam, superyacht_private, ocean waters, 12+6 crew, full_custom, superyacht tier, aluminium, welded, etc.

These profiles are chosen so that `BoatDNAResolver().resolve(BoatDNA.from_boat_class(cls))` reproduces the current `BOAT_CLASS_DEFAULTS[cls]` values exactly.

Note: `from_public_specs()` with the same length/propulsion will NOT produce the same DNA as `from_boat_class()`, because `from_boat_class()` is a curated preset while `from_public_specs()` uses generic heuristics.

`BoatDNA.from_public_specs(specs: dict) -> BoatDNA`
Level 1 heuristic inference from minimal input. Required: `length_m`, `propulsion`. Optional: `beam_m`, `primary_use`, `operating_waters`, `crew`. Fills gaps using:
- `beam_m` ≈ `length_m * 0.28` (sail) or `length_m * 0.26` (motor)
- `primary_use` from length + propulsion lookup table
- `operating_waters` from primary_use
- Production type from length ranges
- Quality tier from production type
- Hull material from propulsion + length heuristics
- All other fields from sensible defaults

**Validation:**
- `propulsion` must be in allowed set
- `length_m` must be 2.5–100
- `beam_m` must be positive and < length_m
- `primary_use` must be in allowed set
- Fields with constrained value sets are validated on construction

### 2. `backend/app/services/boat_dna_resolver.py` — Config Generator

Stateless class with one public method:

```python
class BoatDNAResolver:
    def resolve(self, dna: BoatDNA) -> dict[str, dict]:
        """Returns {module_name: config_dict_with_weights} for all 11 modules,
        plus "overall_weights" key for orchestrator weights."""

    def resolve_and_validate(self, dna: BoatDNA) -> dict[str, dict]:
        """resolve() + assert all weight sums == 1.0 and required keys present."""
```

Each module's config is generated by a private method. The resolver produces dicts with the **exact same keys** that `BOAT_CLASS_DEFAULTS` uses today, including the `"weights"` sub-dict.

#### Resolution Strategy: Two-Tier Approach

**For legacy presets** (`from_boat_class()`): The resolver uses **direct lookup tables** (`_LEGACY_CONFIGS`) that contain the exact values from current `BOAT_CLASS_DEFAULTS`. This guarantees perfect backward compatibility — no formula drift, no rounding errors.

**For custom DNA profiles**: The resolver uses **continuous formulas** that interpolate sensibly across the multi-dimensional DNA space. These formulas are designed to produce reasonable values for any valid DNA, but are NOT constrained to hit the legacy preset values exactly.

```python
class BoatDNAResolver:
    # Exact copies of current BOAT_CLASS_DEFAULTS for backward compat
    _LEGACY_CONFIGS: dict[str, dict[str, dict]] = {
        "small_sail": { "ergonomics": {...}, "compliance": {...}, ... },
        "cruising_sail": { ... },
        "large_motor": { ... },
        "superyacht": { ... },
    }

    def resolve(self, dna: BoatDNA) -> dict[str, dict]:
        # If DNA came from a legacy preset, return exact legacy values
        if dna._legacy_class:
            return self._LEGACY_CONFIGS[dna._legacy_class].copy()
        # Otherwise, compute from continuous formulas
        return self._resolve_custom(dna)
```

The `BoatDNA` dataclass carries a private `_legacy_class: str | None` field set by `from_boat_class()` and `None` for all other construction paths.

#### Per-Module Resolution Logic (Custom DNA)

The following tables describe how continuous formulas generate config values for custom (non-legacy) DNA profiles. These are **design guidelines for implementation** — the exact constants may be tuned during implementation to produce sensible values across the DNA space.

**Ergonomics** (`_resolve_ergonomics`):
| Config Key | Resolution Logic |
|---|---|
| `min_passage_width_mm` | Base from duration: day=550, weekend=575, week/extended/liveaboard=600. Scale: +15mm per meter above 8m. Clamp 500–1000. Racing override: 500 flat. |
| `critical_passage_width_mm` | `min_passage_width_mm - 150`, clamped ≥400 |
| `max_steps_cockpit_pantry` | racing/daysailing=5, weekend=8, length>18=15, else=10 |
| `min_helm_area_sqm` | 1.5 + (length-8)*0.15, clamped 1.5–6.0 |
| `min_helm_visibility_deg` | sheltered=200, coastal=225, offshore=240, ocean=270 |
| `crew_guest_separation` | True if crew>4 AND use in (charter, superyacht_private, explorer) AND length>15 |
| `heel_angle_deg` | 0 for motor; sail: racing=25, racing_cruiser=20, else=20 (matches legacy default); sail_motor: half of sail value |
| **weights** | See weights table below |

**Ergonomics weights:**
| Weight Key | Logic |
|---|---|
| `passage_width` | 0.23 base, -0.02 per tier above standard, clamped 0.13–0.23 |
| `path_efficiency` | 0.15 base, +0.02 if crew_sep required |
| `crew_guest_separation` | 0.04 if no separation; scales to 0.30 when separation + superyacht tier |
| `accessibility` | 0.22 base, -0.02 per tier above standard, clamped 0.13–0.22 |
| `helm_ergonomics` | 0.11–0.14, higher for offshore/ocean |
| `heel_impact` | 0.10 if sail, 0.0 if motor |
| `morning_circulation` | 0.08 constant |
| `access_complexity` | 0.07 constant |
| Normalization | All weights are normalized to sum to 1.0 after individual calculation |

**Compliance** (`_resolve_compliance`):
| Config Key | Resolution Logic |
|---|---|
| `ce_category` | ocean="A", offshore="A"/"B" (A if length≥12, B if <12), coastal="C", sheltered="D" |
| `companionway_sill_mm` | A=300, B=250, C=150, D=0 |
| `cockpit_depth_mm` | 300 (constant, ISO requirement) |
| `min_escape_width_mm` | 600 (constant, ISO requirement) |
| `max_escape_hops` | ceil(length / 2.5), clamped 4–10 |
| `min_engine_clearance_mm` | Lookup by propulsion + length: sail<12m=500, sail≥12m=600, motor<18m=700, motor≥18m=800+, clamped 500–1200 |
| `min_engine_area_sqm` | 0.4 + length*0.04 for sail; 0.5 + length*0.08 for motor, clamped 0.5–5.0 |
| `min_electrical_area_sqm` | 0.15 + length*0.015 for sail; 0.1 + length*0.02 for motor, clamped 0.2–2.0 |
| `required_railing_zones` | Always ["foredeck","cockpit"]; add "flybridge" for motor length>15; add "swim_platform" for motor length>18 |
| `norm_versions` | Constant dict (ISO standards don't vary by boat) |
| **weights** | escape_routes: 0.16–0.24, fire_safety: 0.16–0.20, stability: 0.08–0.16, railing: 0.08–0.16, electrical_access: 0.08, ce_category: 0.12, escape_hatch/cockpit_drain/companionway_sill/ventilation: 0.05 each. Normalized to 1.0. |

**Structural** (`_resolve_structural`):
| Config Key | Resolution Logic |
|---|---|
| `ideal_cog_x_range` | Sail: base (0.42, 0.52), shift +0.02 for cruising uses, +0.03 for racing. Motor: base (0.46, 0.56), shift +0.02 for standard uses, +0.04 for sport_fishing. |
| `lateral_tolerance_pct` | Sail: 0.03 base, +0.02 for cruising, -0.015 for racing. Motor: 0.06 base, +0.02 for larger boats. Clamped 0.015–0.10. |
| `central_band` | (0.20, 0.80) constant |
| `concentration_warn_threshold` | 0.55 constant |
| `boat_class_weight_factor` | 0.5 + length*0.035, clamped 0.6–2.0 |
| `max_trim_deg` | Sail/sail_motor: 2.0; Motor: 1.0 |
| **weights** | fore_aft: 0.21–0.30 (higher for sail); lateral: 0.21; heavy_placement: 0.17–0.26 (higher for motor); load_concentration: 0.17; loading_conditions: 0.10; trim: 0.05. Normalized to 1.0. |

**Production** (`_resolve_production`):
| Config Key | Resolution Logic |
|---|---|
| `min_sharp_angle_deg` | standard/premium=30, luxury=35, superyacht=40 |
| `min_service_access_mm` | 500 + quality_tier_index*100 (standard=0, premium=1, luxury=2, superyacht=3), clamped 500–900 |
| `standard_door_widths_mm` | standard=[600]; premium=[600,700]; luxury=[600,700,800]; superyacht=[700,800,900] |
| `standard_berth_width_mm` | standard/premium=700, luxury=800, superyacht=900 |
| `standardization_tolerance_mm` | standard/premium/luxury=50, superyacht=75 |
| `target_flat_panel_ratio` | mass_production=0.70, semi_custom=0.60, full_custom=0.50, one_off=0.40 |
| **weights** | assembly_sequence: higher for mass_production (0.13→0.21); form_complexity: higher for small/standard (0.25→0.09); service_access: higher for luxury+ (0.17→0.21); standardization: higher for mass_production (0.21→0.09); cable_routing: higher for luxury+ (0.09→0.25); mold_complexity: 0.08; flat_panel_ratio: 0.07. Normalized to 1.0. |

**Cost** (`_resolve_cost`):
| Config Key | Resolution Logic |
|---|---|
| `benchmark_cost_per_meter` | Lookup by quality tier: standard=20000, premium=32000, luxury=65000, superyacht=120000 |
| `labor_rate_eur_hour` | standard=55, premium=60, luxury=65, superyacht=75 |
| `boat_length_m` | 0 (set by orchestrator at runtime) |
| `ideal_distribution` | By production_type — mass_production: material=0.40/labor=0.35/equipment=0.15/overhead=0.10; semi_custom: material=0.38/labor=0.35/equipment=0.17/overhead=0.10; full_custom: material=0.35/labor=0.30/equipment=0.20/overhead=0.15; one_off: material=0.30/labor=0.30/equipment=0.25/overhead=0.15 |
| `parametric_model` | `base_cost_per_m` = benchmark_cost_per_meter. Category split by propulsion: sail gets higher deck_rigging_pct; motor gets higher systems_pct. |
| **weights** | material_costs: 0.18–0.23; labor_estimate: 0.18; cost_per_meter: 0.18–0.23 (higher for luxury); distribution: 0.13; risk: 0.18; parametric_estimate: 0.10. Normalized to 1.0. |

**Emotional** (`_resolve_emotional`):
| Config Key | Resolution Logic |
|---|---|
| `ideal_proportion_range` | Scales with interior_focus: spartan=(0.75,0.90), comfortable=(0.70,0.85), refined=(0.65,0.80), opulent=(0.60,0.75) |
| `ideal_salon_proportion` | spartan=(0.60,0.70), comfortable=(0.55,0.65), refined=(0.50,0.62), opulent=(0.45,0.58) |
| `target_window_ratio_salon` | 0.28 + interior_focus_index*0.03, clamped 0.28–0.40 |
| `target_window_ratio_cabin` | 0.16 + interior_focus_index*0.03, clamped 0.16–0.28 |
| `target_window_ratio_pantry` | 0.10 + interior_focus_index*0.02, clamped 0.10–0.20 |
| `min_sightline_m` | 1.2 + length*0.04, clamped 1.2–3.0 |
| `ideal_material_range` | spartan=(2,4), comfortable=(3,5), refined=(3,6), opulent=(4,7) |
| `min_ceiling_mm` | 1700 + (length-8)*13, clamped 1700–2100 |
| `standard_ceiling_mm` | min_ceiling_mm + 100 |
| `min_cockpit_passage_mm` | Same as ergonomics min_passage_width_mm |
| `validation_level` | "literaturbasiert" (constant) |
| **weights** | room_proportion: 0.09–0.18 (higher for small/performance); light_distribution: 0.14–0.18; sightline: 0.09–0.23 (higher for luxury); visual_calm: 0.09–0.18 (higher for luxury); ceiling_perception: 0.09–0.26 (higher for small); inside_outside_flow: 0.13–0.14; sightline_rays: 0.10. Normalized to 1.0. |

**Materials** (`_resolve_materials`):
| Config Key | Resolution Logic |
|---|---|
| `min_lifespan_years` | standard=15, premium=20, luxury=20, superyacht=25 |
| `max_annual_maintenance_pct` | standard=0.03, premium=0.025, luxury=0.02, superyacht=0.015 |
| `max_zone_weight_kg_sqm` | standard=25, premium=30, luxury=35, superyacht=40 |
| `max_annualized_cost_per_sqm` | standard=50, premium=75, luxury=100, superyacht=150 |
| **weights** | durability: 0.17–0.25 (higher for standard); maintenance: 0.17–0.21; known_issues: 0.17–0.21 (higher for luxury); compatibility: 0.13–0.17 (higher for luxury); weight: 0.09–0.13; lifecycle_cost: 0.08; uv_exposure: 0.04; moisture_risk: 0.03. Normalized to 1.0. |

**Volume/Storage** (`_resolve_volume`):
| Config Key | Resolution Logic |
|---|---|
| `target_utilization` | performance/racing=0.78, cruising=0.72, comfort=0.70, luxury=0.65 |
| `min_utilization` | target - 0.22, clamped ≥0.35 |
| `target_storage_ratio` | performance=0.18, cruising=0.15, comfort=0.12, luxury=0.10 |
| `min_storage_ratio` | target - 0.03, clamped ≥0.08 |
| `min_storage_zones` | 2 + ceil(length/6), clamped 2–6 |
| `max_distribution_imbalance` | 0.6 if length<14, 0.5 if 14–20, 0.4 if >20 |
| `max_furniture_ratio` | spartan=0.55, comfortable=0.50, refined=0.50, opulent=0.45 |
| `min_furniture_ratio` | spartan=0.15, comfortable=0.20, refined=0.22, opulent=0.25 |
| **weights** | utilization: 0.20–0.30 (higher for performance); storage_ratio: 0.20–0.25; storage_accessibility: 0.20–0.25; storage_distribution: 0.15; furniture_ratio: 0.10–0.20 (higher for luxury). Normalized to 1.0. |

**Brand DNA, Market, Service Patterns** (`_resolve_brand_dna`, `_resolve_market`, `_resolve_service_patterns`):
Configs for these modules are less dependent on individual boat identity and more on segment/class. The resolver maps DNA to the closest legacy class for these modules initially, with room to refine later. Mapping: length<14 + sail → small_sail; length<20 + sail → cruising_sail; length<28 + motor → large_motor; else → superyacht.

#### Overall Weights Resolution

The orchestrator's `OVERALL_WEIGHTS` dict is also generated by the resolver under the `"overall_weights"` key:

```python
def _resolve_overall_weights(self, dna: BoatDNA) -> dict[str, float]:
```

Logic (approximate ranges, normalized to 1.0):
- **ergonomics**: 0.10–0.20 (higher for performance/racing/small)
- **volume_storage**: 0.05–0.15 (higher for cruising, lower for luxury)
- **emotional**: 0.10–0.25 (higher for luxury/comfort)
- **compliance**: 0.10–0.15 (higher for offshore/ocean)
- **production**: 0.10 (roughly constant)
- **materials**: 0.10–0.15 (higher for luxury/superyacht)
- **structural**: 0.05–0.10
- **cost**: 0.05–0.10 (higher for mass_production/value)
- **brand_dna**: 0.0–0.10 (0 if not applicable; included when length>12 or premium+)
- **market**: 0.0–0.05 (0 if not applicable; included for luxury+ or length>15)

#### Backward Compatibility Guarantee

For each legacy class `c` in {small_sail, cruising_sail, large_motor, superyacht}:

```python
dna = BoatDNA.from_boat_class(c)
resolved = BoatDNAResolver().resolve(dna)
for module_name in ALL_MODULES:
    legacy_config = module.BOAT_CLASS_DEFAULTS[c].copy()
    legacy_weights = legacy_config.pop("weights")
    resolved_config = resolved[module_name].copy()
    resolved_weights = resolved_config.pop("weights")
    assert resolved_config == legacy_config    # Same config values
    assert resolved_weights == legacy_weights  # Same weight values
```

This is guaranteed by the two-tier approach: legacy presets use direct lookup tables (`_LEGACY_CONFIGS`) containing exact copies of `BOAT_CLASS_DEFAULTS`. No formula is involved for legacy presets.

### 3. `backend/app/domain/construction.py` — Construction Knowledge

Pure data module. A dict `CONSTRUCTION_KNOWLEDGE` keyed by `"{hull_material}_{hull_construction}"`:

```python
CONSTRUCTION_KNOWLEDGE = {
    "grp_solid_hand_layup": {
        "description": "Solides GFK-Laminat in Handauflegeverfahren",
        "typical_boats": "Serienboote <15m, ältere Designs",
        "glass_resin_ratio": "40-55% Glas",
        "strengths": [...],
        "weaknesses": [...],
        "quality_indicators_visual": [...],
        "known_issues": [
            {"issue": "...", "onset_years": "5-15", "location": "...", "cause": "..."},
        ],
    },
    "grp_sandwich_resin_infusion": { ... },
    "aluminium_welded": { ... },
    "carbon_composite_prepreg_autoclave": { ... },
    "wood_epoxy_cold_molded": { ... },
    "steel_welded": { ... },
}
```

Entries cover the 6 major construction method/material combinations from the spec. Each entry includes German descriptions, quality indicators for visual analysis, and known issues with onset timelines.

Additionally contains `CRITICAL_RULES` for construction types that have safety-critical requirements (e.g., aluminium alloy selection, antifouling compatibility).

**Fallback for unknown combinations:** When `f"{dna.hull_material}_{dna.hull_construction}"` has no entry in `CONSTRUCTION_KNOWLEDGE`, the visual context builder omits the construction-specific section. No error — the prompt works without it, just with less specificity.

### 4. `backend/app/services/visual/prompt_context.py` — Visual Context Builder

```python
def build_visual_context(dna: BoatDNA) -> str:
    """Generate German-language boat profile string for visual analysis prompts."""
```

Produces a structured text block containing:
1. **BOOTSPROFIL** — type, dimensions, use, waters, construction
2. **ERWARTETE QUALITÄTSSTANDARDS** — joinery gaps, surface finish, fastener visibility (from quality tolerance logic)
3. **KONSTRUKTIONSSPEZIFISCHE PRÜFPUNKTE** — quality indicators from CONSTRUCTION_KNOWLEDGE (omitted if no entry for this hull_material+hull_construction combo)
4. **BEWERTE NACH DIESEN STANDARDS** — instruction to judge by this boat's standards, not abstract classes

Label dicts (`USE_LABELS`, `WATERS_LABELS`, etc.) map enum values to German display strings.

**Quality tolerance logic** (used by prompt context builder, not a separate resolver method):

```python
QUALITY_BY_TIER = {
    "standard":   {"joinery_gap_mm": 3.0, "gelcoat": "leichte Orangenhaut akzeptabel", "fastener": "abgedeckt"},
    "premium":    {"joinery_gap_mm": 1.5, "gelcoat": "glatt, keine sichtbaren Fehler", "fastener": "verdeckt"},
    "luxury":     {"joinery_gap_mm": 0.8, "gelcoat": "Spiegelfinish", "fastener": "unsichtbar"},
    "superyacht": {"joinery_gap_mm": 0.5, "gelcoat": "Spiegelfinish, perfekt", "fastener": "unsichtbar"},
}
```

Additional quality details for teak deck, weld quality, and laminate consistency are conditionally included based on `deck_material`, `hull_material`, and `hull_construction`.

### 5. Tests

#### `backend/tests/test_boat_dna.py` — Model Tests (~15 tests)

- `test_from_boat_class_*` (4 tests) — Each preset produces valid DNA with all fields populated
- `test_from_boat_class_sets_legacy_flag` — `_legacy_class` is set to the class name
- `test_from_public_specs_minimal` — Just length + propulsion fills all fields
- `test_from_public_specs_rich` — Provided values are preserved, not overwritten
- `test_from_public_specs_beam_inference` — Beam calculated from length when omitted
- `test_from_public_specs_no_legacy_flag` — `_legacy_class` is None
- `test_validation_invalid_propulsion` — ValueError for unknown propulsion
- `test_validation_length_range` — Length must be 2.5–100
- `test_validation_invalid_use` — ValueError for unknown primary_use
- `test_all_presets_round_trip` — from_boat_class → to_dict → from_dict produces identical DNA

#### `backend/tests/test_boat_dna_resolver.py` — Resolver Tests (~35 tests)

**Backward compatibility (4 tests, most critical):**
- `test_backward_compat_small_sail` — Resolved config matches BOAT_CLASS_DEFAULTS["small_sail"] for ALL 11 modules (configs AND weights)
- `test_backward_compat_cruising_sail` — Same for cruising_sail
- `test_backward_compat_large_motor` — Same for large_motor
- `test_backward_compat_superyacht` — Same for superyacht

These tests import `BOAT_CLASS_DEFAULTS` from each module and assert exact equality.

**Continuous scaling (custom DNA profiles):**
- `test_passage_width_scales_with_length` — 10m boat gets narrower passages than 14m
- `test_heel_angle_by_propulsion` — Sail gets non-zero heel, motor gets 0
- `test_heel_angle_by_use` — Racing gets 25°, daysailing gets lower
- `test_motorsailer_gets_reduced_heel` — sail_motor gets heel but less than pure sail
- `test_crew_separation_logic` — Only triggers for charter/superyacht with >4 crew and >15m
- `test_ce_category_from_waters` — ocean→A, coastal→C, sheltered→D
- `test_ce_category_b_for_small_offshore` — offshore + length<12 → B
- `test_production_targets_by_type` — mass=0.70 flat panel, one_off=0.40
- `test_cost_benchmark_scales_with_tier` — standard<premium<luxury<superyacht
- `test_cog_range_by_propulsion` — Sail gets forward range, motor gets centered
- `test_weight_factor_scales_with_length` — Short=light factor, long=heavy factor
- `test_trim_limit_by_propulsion` — Sail=2.0°, motor=1.0°
- `test_quality_tolerances_by_tier` — Standard=3mm gaps, superyacht=0.5mm
- `test_door_widths_superyacht_no_600` — Superyacht gets [700,800,900], not [600,700,800,900]

**Weight validation:**
- `test_all_module_weights_sum_to_one` — For 20 random DNA profiles, all weight dicts sum to 1.0 (within float tolerance 1e-9)
- `test_overall_weights_sum_to_one` — Same for overall weights

**Required keys validation:**
- `test_resolver_produces_all_required_keys` — For each module, resolved config has every key that BOAT_CLASS_DEFAULTS contains

**Edge cases:**
- `test_extreme_small_boat` — 3m dinghy produces sane configs (no negative values, no divisions by zero)
- `test_extreme_large_boat` — 50m superyacht produces sane configs

#### `backend/tests/test_boat_dna_integration.py` — Integration Tests (~10 tests)

- `test_ergonomics_with_dna_overrides` — Run ergonomics module with DNA-resolved config, verify valid result
- `test_structural_with_dna_overrides` — Same for structural
- `test_compliance_with_dna_overrides` — Same for compliance
- `test_cost_with_dna_overrides` — Same for cost
- `test_legacy_mode_identical` — Run module with boat_class only (no DNA), verify identical to existing test results
- `test_racing_sailboat_profile` — Full profile for a 12m offshore racer, verify all modules produce valid results
- `test_charter_motoryacht_profile` — Full profile for an 18m charter motor yacht
- `test_construction_knowledge_lookup` — Verify CONSTRUCTION_KNOWLEDGE entries exist for common material+construction combos
- `test_construction_knowledge_fallback` — Unknown combo returns None gracefully
- `test_visual_context_generation` — build_visual_context produces non-empty German string with expected sections

## What's NOT in Scope

- **No DB migration** — `boat_dna_json` column designed but not migrated
- **No API endpoints** — PUT/GET for DNA profile are a follow-up
- **No frontend wizard** — DNA creation UI is a separate spec
- **No prompt rewrite** — `build_visual_context()` is ready to use but not wired into VisualAnalyzer
- **No module signature changes** — Modules keep `(zones, passages, boat_class, config_overrides)`
- **No orchestrator wiring** — Resolver is built and tested; orchestrator integration is a thin follow-up step
- **No removal of BOAT_CLASS_DEFAULTS** — They remain as fallback/seed data
- **No Alembic migration** — DB changes deferred

## File Summary

| File | Type | Purpose |
|---|---|---|
| `backend/app/models/boat_dna.py` | New | BoatDNA dataclass + presets + from_public_specs |
| `backend/app/services/boat_dna_resolver.py` | New | Full resolver with per-module config generation + legacy lookup tables |
| `backend/app/domain/construction.py` | New | CONSTRUCTION_KNOWLEDGE reference data |
| `backend/app/services/visual/prompt_context.py` | New | build_visual_context() for visual prompts |
| `backend/tests/test_boat_dna.py` | New | Model tests |
| `backend/tests/test_boat_dna_resolver.py` | New | Resolver tests + backward compat assertions |
| `backend/tests/test_boat_dna_integration.py` | New | End-to-end with actual modules |
| Existing modules | Unchanged | No modifications to any analysis module |
| Existing tests | Unchanged | All 457 tests continue passing |
