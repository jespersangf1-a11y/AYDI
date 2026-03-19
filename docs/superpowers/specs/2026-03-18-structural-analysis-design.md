# Structural Analysis (Weight Distribution) — Design Spec

## Overview

Pure-function analysis module that evaluates weight distribution and center of gravity placement in yacht layouts. Uses heuristic weight estimation from zone types and polygon geometry — no additional data models or user input required.

The module answers: **Is the layout weight well-balanced for this boat class?**

## Scope

**In scope:**
- Longitudinal (fore-aft) weight balance via weighted centroid calculation
- Lateral (port-starboard) weight balance
- Heavy zone placement assessment (engine, storage, tanks — should be low and central)
- Load concentration analysis (even distribution across boat thirds)
- Boat-class-specific thresholds and weights

**Out of scope:**
- Actual structural engineering calculations (FEA, stress analysis)
- Material strength analysis (covered by Materials module)
- Stability calculations per ISO 12217 (covered by Compliance module)
- Manual weight input or integration with Materials module weight data

## Architecture

### Module Pattern

Follows the established AYDI analysis module pattern exactly:

```
backend/app/services/analysis/structural.py
    → run_structural_analysis(zones, passages, boat_class, config_overrides=None) → dict
```

Pure function. No database access. Receives zone/passage dicts, returns standardized result dict.

### Weight Estimation Heuristic

Each zone's weight is estimated as: `polygon_area_sqm × weight_per_sqm × boat_class_factor`

**Base weight per zone_type (kg/m²):**

| zone_type | kg/m² | Rationale |
|-----------|-------|-----------|
| engine | 350 | Motor, generator, fuel tanks, machinery |
| storage | 150 | Filled storage lockers, chain locker |
| tender_garage | 200 | Tender, davit, water toys |
| pantry | 120 | Appliances, countertops, plumbing |
| head | 100 | Sanitary fittings, tiles, plumbing |
| salon | 80 | Furniture, entertainment systems |
| cabin | 70 | Berth, wardrobe, soft furnishings |
| crew_quarters | 70 | Same as cabin |
| helm | 60 | Instruments, console, electronics |
| cockpit | 40 | Open area, light fixtures |
| flybridge | 35 | Open deck, light equipment |
| foredeck | 25 | Open deck, anchor gear |
| swim_platform | 30 | Platform structure |

**Boat class scaling factors:**

| Boat class | Factor | Rationale |
|-----------|--------|-----------|
| small_sail | 0.7 | Lighter construction, minimal equipment |
| cruising_sail | 1.0 | Reference baseline |
| large_motor | 1.3 | Heavier fit-out, more equipment |
| superyacht | 1.6 | Premium materials, extensive systems |

### Centroid Calculation

Zone centroid via standard polygon centroid formula (Shoelace variant):

```
Cx = (1 / 6A) × Σ (xi + xi+1)(xi·yi+1 − xi+1·yi)
Cy = (1 / 6A) × Σ (yi + yi+1)(xi·yi+1 − xi+1·yi)
```

Where `A` is the **signed** area from the shoelace formula. CLAUDE.md states polygons are counter-clockwise (positive signed area), so `abs(A)` is safe. The implementation should use `abs(A)` defensively.

Weighted center of gravity: `CoG = Σ(centroid_i × weight_i) / Σ(weight_i)`

Normalized to boat dimensions: CoG_x as percentage of max X span (0% = bow, 100% = stern), CoG_y as percentage of max Y span (0% = starboard, 100% = port).

**Unknown zone types:** If a zone's `zone_type` is not in `ZONE_WEIGHT_KG_PER_SQM`, use a default fallback of 50 kg/m² and emit no warning (future zone types should not block analysis).

## Sub-Analyses

### 1. Longitudinal Balance (fore_aft)

**What it checks:** Weighted X-centroid as percentage of boat length.

**Ideal range per boat class:**

| Boat class | Ideal CoG_x range | Rationale |
|-----------|-------------------|-----------|
| small_sail | 42–52% | Forward bias for upwind performance |
| cruising_sail | 44–54% | Slightly aft for comfort under sail |
| large_motor | 48–58% | Aft bias for planing hull trim |
| superyacht | 46–56% | Balanced for displacement hull |

**Scoring:**
- CoG_x within ideal range → score 100
- Each 1% outside range → score decreases by 6.67 (reaches 0 at 15% deviation)
- `score = max(0, 100 - abs(deviation_from_nearest_bound) × 6.67)`

**Warning codes:**
- `COG_TOO_FAR_FORWARD` (severity: warning/critical based on deviation)
- `COG_TOO_FAR_AFT` (severity: warning/critical based on deviation)
- Critical threshold: >10% outside ideal range

**Metrics:**
- `cog_x_pct`: actual CoG X percentage
- `ideal_range`: [min, max] for the boat class
- `deviation_pct`: distance from nearest ideal bound (0 if within range)

### 2. Lateral Balance (lateral)

**What it checks:** Weighted Y-centroid as percentage of boat beam. 50% = perfectly centered.

**Tolerance per boat class:**

| Boat class | Max offset from 50% | Rationale |
|-----------|---------------------|-----------|
| small_sail | ±3% | Heeling sensitivity, narrow beam |
| cruising_sail | ±5% | Moderate sensitivity |
| large_motor | ±8% | Wider beam, more tolerant |
| superyacht | ±6% | Wide but expectations high |

**Scoring:**
- Offset ≤ tolerance → score 100
- Each 1% beyond tolerance → score decreases by 10 (reaches 0 at 10% over)
- `score = max(0, 100 - max(0, abs(offset) - tolerance) × 10)`

**Warning code:** `COG_LATERAL_OFFSET`
- Warning if offset > tolerance
- Critical if offset > 2× tolerance

**Metrics:**
- `cog_y_pct`: actual CoG Y percentage
- `offset_from_center_pct`: absolute deviation from 50%
- `tolerance_pct`: allowed offset for this boat class

### 3. Heavy Zone Placement (heavy_placement)

**What it checks:** Whether heavy zones (engine, storage, tender_garage) are positioned centrally along the boat.

**Definition of "central":** X-position of zone centroid falls within the middle 60% of the boat length (20%–80% of X span).

**Heavy zone types:** `engine`, `storage`, `tender_garage`

**Scoring:**
- Start at 100
- Each heavy zone outside the central 60%: penalty based on weight proportion
- `penalty = (zone_weight / total_heavy_weight) × 50`
- Minimum score: 0

**Warning codes:**
- `HEAVY_ZONE_OFF_CENTER` — heavy zone outside central band
- Severity: warning (marginal), critical (extreme position, <15% or >85%)

**Metrics:**
- `heavy_zones`: list of {name, zone_type, centroid_x_pct, weight_kg, is_central}
- `total_heavy_weight_kg`: sum of heavy zone weights
- `central_ratio`: fraction of heavy weight that is centrally placed

### 4. Load Concentration (load_concentration)

**What it checks:** Whether weight is evenly distributed across three longitudinal segments (bow third, middle third, stern third).

**Segments:** Divide X span into 3 equal segments. Assign each zone to the segment containing its centroid.

**Scoring:**
- Calculate weight fraction per segment
- Ideal: each segment carries ~33%
- Score based on coefficient of variation (CV = std_dev / mean)
- CV = 0 → score 100 (perfectly even)
- CV ≥ 1.0 → score 0 (extremely uneven)
- `score = max(0, 100 × (1 - CV))`
- Warning triggered when any segment carries >55% of total weight

**Warning code:** `LOAD_CONCENTRATION_HIGH`
- Severity: warning (one segment >55%), critical (one segment >70%)

**Metrics:**
- `segment_weights`: {bow: kg, middle: kg, stern: kg}
- `segment_fractions`: {bow: pct, middle: pct, stern: pct}
- `heaviest_segment`: name of heaviest segment
- `cv`: coefficient of variation

## BOAT_CLASS_DEFAULTS

```python
BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "ideal_cog_x_range": (0.42, 0.52),
        "lateral_tolerance_pct": 0.03,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 0.7,
        "weights": {
            "fore_aft": 0.35,
            "lateral": 0.25,
            "heavy_placement": 0.20,
            "load_concentration": 0.20,
        },
    },
    "cruising_sail": {
        "ideal_cog_x_range": (0.44, 0.54),
        "lateral_tolerance_pct": 0.05,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 1.0,
        "weights": {
            "fore_aft": 0.30,
            "lateral": 0.25,
            "heavy_placement": 0.25,
            "load_concentration": 0.20,
        },
    },
    "large_motor": {
        "ideal_cog_x_range": (0.48, 0.58),
        "lateral_tolerance_pct": 0.08,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 1.3,
        "weights": {
            "fore_aft": 0.25,
            "lateral": 0.25,
            "heavy_placement": 0.30,
            "load_concentration": 0.20,
        },
    },
    "superyacht": {
        "ideal_cog_x_range": (0.46, 0.56),
        "lateral_tolerance_pct": 0.06,
        "central_band": (0.20, 0.80),
        "concentration_warn_threshold": 0.55,
        "boat_class_weight_factor": 1.6,
        "weights": {
            "fore_aft": 0.25,
            "lateral": 0.25,
            "heavy_placement": 0.30,
            "load_concentration": 0.20,
        },
    },
}
```

## Orchestrator

```python
def run_structural_analysis(
    zones: list[dict],
    passages: list[dict],  # unused — accepted for API pattern consistency
    boat_class: str,
    config_overrides: dict | None = None,
) -> dict:
```

**`passages` is unused** by this module. All sub-analyses operate on zones only. The parameter exists for consistent API signature across all modules.

**Flow:**
1. Look up `BOAT_CLASS_DEFAULTS[boat_class]`, copy config, pop `weights`
2. Apply `config_overrides` if provided
3. If no zones: return overall score 50.0 with `STRUCTURAL_NO_ZONES` info warning
4. Run each sub-analysis in try/except (on error: score 0 + critical warning)
5. Compute weighted overall score from sub-scores using weights
6. Deduplicate suggestions, sort warnings by severity (critical → warning → info)

**Return dict (identical to all other modules):**
```python
{
    "module": "structural",
    "overall_score": round(weighted_sum, 1),  # 0-100
    "sub_scores": {"fore_aft": float, "lateral": float, "heavy_placement": float, "load_concentration": float},
    "warnings": [...],  # sorted by severity
    "suggestions": [...],  # deduplicated
    "metrics": {"fore_aft": {...}, "lateral": {...}, "heavy_placement": {...}, "load_concentration": {...}},
    "config_used": config,  # weights popped, overrides applied
}
```

**`config_used` note:** `weights` is popped before storing (consistent with other modules). `ZONE_WEIGHT_KG_PER_SQM` is a module-level constant and not stored in `config_used`. The `boat_class_weight_factor` IS stored since it varies per boat class.

**Empty input:** Each sub-analysis independently returns score 50.0 + info warning when no zones are provided. The orchestrator also short-circuits at the top level.

## Warning Codes Summary

| Code | Severity | Trigger |
|------|----------|---------|
| `COG_TOO_FAR_FORWARD` | warning/critical | CoG_x below ideal range |
| `COG_TOO_FAR_AFT` | warning/critical | CoG_x above ideal range |
| `COG_LATERAL_OFFSET` | warning/critical | CoG_y offset > tolerance |
| `HEAVY_ZONE_OFF_CENTER` | warning/critical | Heavy zone outside central 60% |
| `LOAD_CONCENTRATION_HIGH` | warning/critical | Segment carries >55% / >70% weight |
| `STRUCTURAL_NO_ZONES` | info | No zones provided |
| `STRUCTURAL_NO_HEAVY_ZONES` | info | No heavy zones found |

All warning messages in German. Every warning includes a suggestion.

## Files

| File | Action | Responsibility |
|------|--------|----------------|
| `backend/app/services/analysis/structural.py` | CREATE | BOAT_CLASS_DEFAULTS, ZONE_WEIGHT_KG_PER_SQM, helpers, 4 sub-analyses, orchestrator |
| `backend/tests/test_structural.py` | CREATE | ~20 tests covering all sub-analyses + integration |
| `backend/app/api/routes/layouts.py` | MODIFY | Import + register in ANALYSIS_MODULES |

## Testing Strategy

- **Per sub-analysis:** balanced input → score 100, imbalanced input → lower score + correct warnings, empty input → score 50 + info
- **Boat class differentiation:** same layout produces different scores for different boat classes
- **Config overrides:** verify custom thresholds are applied and stored in config_used
- **Warning sort order:** critical → warning → info
- **Edge cases:** single zone, all zones same position, extremely asymmetric layout
