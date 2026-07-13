> **⚠️ ARCHIV — HISTORISCHER PLANUNGSSTAND (nicht maßgeblich).**
> Dieses Dokument beschreibt einen früheren Planungs-/Design-Stand und trackt den aktuellen Code **nicht**.
> Bekannte Drift: 4 statt real **13 Bootsklassen** (`BoatClass`-Enum); abweichende Sub-Analysen/Gewichte; einzelne enthaltene Tests schlagen gegen den Ist-Code fehl.
> **Maßgeblich ist `CLAUDE.md`** (plus der Code). Nicht zum Ableiten von Enums, Return-Contracts oder Tests verwenden.

# Emotional Design Score Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Implement the Emotional Design analysis module (`emotional.py`) that quantifies why a boat interior feels premium, open, cramped, or cluttered — scoring room proportions, light, sightlines, visual calm, ceiling perception, and inside-outside flow.

**Architecture:** New pure-function module following the same pattern as ergonomics.py and volume_storage.py. Six sub-analyses that each return `tuple[float, list[dict], dict]`. Data comes from zone polygons, `height_mm`, `properties` (window_area_pct, material_count), and passages. All sub-analyses gracefully degrade when optional data is absent (score 50.0 + info warning). Register in route handler.

**Tech Stack:** Python 3.12, pytest, shoelace formula for polygon area

---

## File Structure

| File | Action | Responsibility |
|------|--------|----------------|
| `backend/app/services/analysis/emotional.py` | Create | 6 sub-analyses + orchestrator |
| `backend/tests/test_emotional.py` | Create | Tests for all sub-analyses |
| `backend/app/api/routes/layouts.py` | Modify (lines 18-29) | Register `emotional` module |

## Data Dependencies

Each sub-analysis uses specific zone fields. All are optional with graceful degradation:

| Sub-analysis | Required zone fields | From passages |
|---|---|---|
| Room proportion | `polygon`, `height_mm` | — |
| Light distribution | `properties.window_area_pct` | — |
| Sightline analysis | `polygon` (entry point = first vertex) | — |
| Visual calm | `properties.material_count` | — |
| Ceiling height perception | `height_mm` | — |
| Inside-outside flow | `zone_type` | `width_mm` to cockpit |

---

### Task 1: Create emotional.py with BOAT_CLASS_DEFAULTS and helpers

**Files:**
- Create: `backend/app/services/analysis/emotional.py`
- Test: `backend/tests/test_emotional.py`

- [ ] **Step 1: Write a minimal test that imports the module**

Create `backend/tests/test_emotional.py`:

```python
from tests.conftest import make_passage, make_zone

from app.services.analysis.emotional import (
    BOAT_CLASS_DEFAULTS,
    run_emotional_analysis,
)


def _default_config(boat_class="cruising_sail"):
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


def test_emotional_module_exists():
    assert "small_sail" in BOAT_CLASS_DEFAULTS
    assert "cruising_sail" in BOAT_CLASS_DEFAULTS
    assert "large_motor" in BOAT_CLASS_DEFAULTS
    assert "superyacht" in BOAT_CLASS_DEFAULTS
    # All weights must sum to 1.0
    for bc, cfg in BOAT_CLASS_DEFAULTS.items():
        total = sum(cfg["weights"].values())
        assert abs(total - 1.0) < 0.001, f"{bc} weights sum to {total}"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `cd /c/Users/ThinkPad/Documents/AYDI/backend && PYTHONPATH=. python -m pytest tests/test_emotional.py::test_emotional_module_exists -v`
Expected: FAIL (module not found)

- [ ] **Step 3: Create the module with defaults and helpers**

Create `backend/app/services/analysis/emotional.py`:

```python
"""Emotional design score module for yacht layouts.

Quantifies spatial experience: proportions, light, sightlines, visual calm,
ceiling perception, and inside-outside flow. Pure function module — no database access.
"""
import logging
import math

logger = logging.getLogger(__name__)

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "ideal_proportion_range": (0.70, 0.85),    # height/width for cabins (per spec)
        "ideal_salon_proportion": (0.55, 0.65),     # height/width for salon (per spec)
        "target_window_ratio_salon": 0.30,
        "target_window_ratio_cabin": 0.18,
        "target_window_ratio_pantry": 0.12,
        "min_sightline_m": 1.5,
        "ideal_material_range": (3, 5),
        "min_ceiling_mm": 1750,
        "standard_ceiling_mm": 1850,
        "min_cockpit_passage_mm": 600,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.20,
            "light_distribution": 0.15,
            "sightline": 0.10,
            "visual_calm": 0.10,
            "ceiling_perception": 0.30,
            "inside_outside_flow": 0.15,
        },
    },
    "cruising_sail": {
        "ideal_proportion_range": (0.70, 0.85),
        "ideal_salon_proportion": (0.55, 0.65),
        "target_window_ratio_salon": 0.32,
        "target_window_ratio_cabin": 0.20,
        "target_window_ratio_pantry": 0.15,
        "min_sightline_m": 1.8,
        "ideal_material_range": (3, 5),
        "min_ceiling_mm": 1850,
        "standard_ceiling_mm": 1950,
        "min_cockpit_passage_mm": 650,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.20,
            "light_distribution": 0.15,
            "sightline": 0.15,
            "visual_calm": 0.10,
            "ceiling_perception": 0.25,
            "inside_outside_flow": 0.15,
        },
    },
    "large_motor": {
        "ideal_proportion_range": (0.65, 0.80),
        "ideal_salon_proportion": (0.50, 0.62),
        "target_window_ratio_salon": 0.35,
        "target_window_ratio_cabin": 0.22,
        "target_window_ratio_pantry": 0.15,
        "min_sightline_m": 2.0,
        "ideal_material_range": (3, 6),
        "min_ceiling_mm": 1950,
        "standard_ceiling_mm": 2050,
        "min_cockpit_passage_mm": 700,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.15,
            "light_distribution": 0.20,
            "sightline": 0.20,
            "visual_calm": 0.15,
            "ceiling_perception": 0.15,
            "inside_outside_flow": 0.15,
        },
    },
    "superyacht": {
        "ideal_proportion_range": (0.60, 0.75),
        "ideal_salon_proportion": (0.45, 0.58),
        "target_window_ratio_salon": 0.38,
        "target_window_ratio_cabin": 0.25,
        "target_window_ratio_pantry": 0.18,
        "min_sightline_m": 2.5,
        "ideal_material_range": (4, 6),
        "min_ceiling_mm": 2050,
        "standard_ceiling_mm": 2150,
        "min_cockpit_passage_mm": 850,
        "validation_level": "literaturbasiert",
        "weights": {
            "room_proportion": 0.10,
            "light_distribution": 0.20,
            "sightline": 0.25,
            "visual_calm": 0.20,
            "ceiling_perception": 0.10,
            "inside_outside_flow": 0.15,
        },
    },
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}


def _polygon_area_sqm(polygon: list[list[float]]) -> float:
    """Shoelace formula, returns area in square meters (input in mm)."""
    n = len(polygon)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2.0 / 1_000_000


def _polygon_bbox_dims_mm(polygon: list[list[float]]) -> tuple[float, float]:
    """Return (width_mm, depth_mm) of polygon bounding box."""
    if not polygon:
        return (0.0, 0.0)
    xs = [p[0] for p in polygon]
    ys = [p[1] for p in polygon]
    return (max(xs) - min(xs), max(ys) - min(ys))


def _max_interior_distance_m(polygon: list[list[float]]) -> float:
    """Maximum distance between any two vertices, in meters."""
    if len(polygon) < 2:
        return 0.0
    max_dist = 0.0
    for i in range(len(polygon)):
        for j in range(i + 1, len(polygon)):
            dx = polygon[i][0] - polygon[j][0]
            dy = polygon[i][1] - polygon[j][1]
            d = math.sqrt(dx * dx + dy * dy) / 1000.0
            if d > max_dist:
                max_dist = d
    return max_dist


def run_emotional_analysis(zones: list[dict], passages: list[dict], boat_class: str, config_overrides: dict | None = None) -> dict:
    """Orchestrator — runs all emotional design sub-analyses."""
    if boat_class not in BOAT_CLASS_DEFAULTS:
        raise ValueError(f"Unknown boat class: {boat_class}")
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    weights = config.pop("weights").copy()

    if config_overrides:
        config.update(config_overrides)

    sub_scores: dict[str, float] = {}
    all_warnings: list[dict] = []
    all_suggestions: list[str] = []
    all_metrics: dict[str, dict] = {}

    analyses = [
        ("room_proportion", lambda: analyze_room_proportion(zones, config)),
        ("light_distribution", lambda: analyze_light_distribution(zones, config)),
        ("sightline", lambda: analyze_sightline(zones, config)),
        ("visual_calm", lambda: analyze_visual_calm(zones, config)),
        ("ceiling_perception", lambda: analyze_ceiling_perception(zones, config)),
        ("inside_outside_flow", lambda: analyze_inside_outside_flow(zones, passages, config)),
    ]

    for name, fn in analyses:
        try:
            score, warnings, metrics = fn()
            sub_scores[name] = score
            all_warnings.extend(warnings)
            all_metrics[name] = metrics
        except Exception:
            logger.exception("Error in sub-analysis %s", name)
            sub_scores[name] = 0.0
            all_warnings.append({
                "severity": "critical",
                "message": f"Fehler bei Analyse: {name}",
                "suggestion": "Layoutdaten überprüfen",
            })

    overall = sum(sub_scores.get(k, 0) * w for k, w in weights.items())

    for w in all_warnings:
        if w.get("suggestion") and w["suggestion"] not in all_suggestions:
            all_suggestions.append(w["suggestion"])

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    return {
        "module": "emotional",
        "overall_score": round(overall, 1),
        "sub_scores": {k: round(v, 1) for k, v in sub_scores.items()},
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
    }
```

**Note:** The 6 `analyze_*` functions are not yet defined — they will be added in Tasks 2-7. The orchestrator references them via forward-compatible lambdas; calling `run_emotional_analysis` will fail until all 6 are implemented. The import test only checks `BOAT_CLASS_DEFAULTS`.

- [ ] **Step 4: Run test to verify it passes**

Run: `cd /c/Users/ThinkPad/Documents/AYDI/backend && PYTHONPATH=. python -m pytest tests/test_emotional.py::test_emotional_module_exists -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/emotional.py backend/tests/test_emotional.py
git commit -m "feat: create emotional design module scaffold with defaults"
```

---

### Task 2: Add `analyze_room_proportion` sub-analysis

Scores ceiling height / room width ratio. Ideal ratios differ by zone type (salon vs cabin) and boat class.

**Files:**
- Modify: `backend/app/services/analysis/emotional.py`
- Modify: `backend/tests/test_emotional.py`

- [ ] **Step 1: Write failing tests**

Add to `backend/tests/test_emotional.py`:

```python
from app.services.analysis.emotional import analyze_room_proportion


def test_room_proportion_good():
    """Zones with height and good proportions score high."""
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [3500, 0], [3500, 3000], [0, 3000]], height_mm=1950),
        make_zone("cabin", "cabin", polygon=[[0, 3000], [2500, 3000], [2500, 5000], [0, 5000]], height_mm=1950),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_room_proportion(zones, config)
    assert score >= 70.0
    assert metrics["zones_evaluated"] >= 1


def test_room_proportion_no_height():
    """No height data -> degraded score 50."""
    zones = [make_zone("salon", "salon"), make_zone("cabin", "cabin")]
    config = _default_config()
    score, warnings, metrics = analyze_room_proportion(zones, config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


def test_room_proportion_empty():
    """Empty zones -> 50.0."""
    config = _default_config()
    score, warnings, metrics = analyze_room_proportion([], config)
    assert score == 50.0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /c/Users/ThinkPad/Documents/AYDI/backend && PYTHONPATH=. python -m pytest tests/test_emotional.py -k "room_proportion" -v`
Expected: FAIL (ImportError)

- [ ] **Step 3: Implement**

Add to `emotional.py`, before `run_emotional_analysis`:

```python
# Zone types to evaluate for proportions (living spaces)
_PROPORTION_ZONE_TYPES = {"salon", "cabin", "pantry", "helm", "crew_quarters"}


def analyze_room_proportion(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score ceiling height / room width ratio for living spaces."""
    warnings: list[dict] = []

    evaluable = [z for z in zones if z["zone_type"] in _PROPORTION_ZONE_TYPES and z.get("height_mm") is not None]
    if not evaluable:
        warnings.append({
            "severity": "info",
            "message": "Keine Höhendaten vorhanden — Raumproportionen nicht bewertbar",
            "suggestion": "height_mm für Zonen angeben",
        })
        return 50.0, warnings, {"zones_evaluated": 0}

    ideal_salon = config["ideal_salon_proportion"]
    ideal_other = config["ideal_proportion_range"]
    zone_scores = []

    for z in evaluable:
        width, depth = _polygon_bbox_dims_mm(z["polygon"])
        shorter_dim = min(width, depth) if min(width, depth) > 0 else max(width, depth)
        if shorter_dim == 0:
            continue

        ratio = z["height_mm"] / shorter_dim
        ideal = ideal_salon if z["zone_type"] == "salon" else ideal_other
        lo, hi = ideal

        if lo <= ratio <= hi:
            zone_scores.append(100.0)
        else:
            if ratio < lo:
                deviation = (lo - ratio) / lo
            else:
                deviation = (ratio - hi) / hi
            zone_score = max(0.0, 100.0 - deviation * 150.0)
            zone_scores.append(zone_score)

            if deviation > 0.15:
                label = z["name"]
                warnings.append({
                    "severity": "warning",
                    "message": f"Raumproportionen in '{label}' ungünstig (Verhältnis: {ratio:.2f}, Ideal: {lo:.2f}–{hi:.2f})",
                    "suggestion": f"Deckenhöhe oder Raumbreite in '{label}' anpassen",
                })

    if not zone_scores:
        return 50.0, warnings, {"zones_evaluated": 0}

    score = sum(zone_scores) / len(zone_scores)
    return score, warnings, {"zones_evaluated": len(zone_scores)}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /c/Users/ThinkPad/Documents/AYDI/backend && PYTHONPATH=. python -m pytest tests/test_emotional.py -k "room_proportion" -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/emotional.py backend/tests/test_emotional.py
git commit -m "feat: add room proportion sub-analysis"
```

---

### Task 3: Add `analyze_light_distribution` sub-analysis

Scores window area as fraction of zone area, using `properties.window_area_pct`.

**Files:**
- Modify: `backend/app/services/analysis/emotional.py`
- Modify: `backend/tests/test_emotional.py`

- [ ] **Step 1: Write failing tests**

Add to `backend/tests/test_emotional.py`:

```python
from app.services.analysis.emotional import analyze_light_distribution


def test_light_distribution_good():
    """Zones with adequate window ratios score high."""
    zones = [
        make_zone("salon", "salon", properties={"window_area_pct": 0.32}),
        make_zone("cabin", "cabin", properties={"window_area_pct": 0.20}),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_light_distribution(zones, config)
    assert score >= 80.0
    assert metrics["zones_evaluated"] == 2


def test_light_distribution_dark():
    """Low window ratio -> warning."""
    zones = [make_zone("salon", "salon", properties={"window_area_pct": 0.08})]
    config = _default_config()
    score, warnings, metrics = analyze_light_distribution(zones, config)
    assert score < 80.0
    assert len(warnings) > 0


def test_light_distribution_no_data():
    """No window data -> 50.0."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_light_distribution(zones, config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
```

- [ ] **Step 2: Run tests to verify they fail**

- [ ] **Step 3: Implement**

Add to `emotional.py`, before `run_emotional_analysis`:

```python
# Target window ratio keys by zone type
_WINDOW_TARGET_KEYS = {
    "salon": "target_window_ratio_salon",
    "cabin": "target_window_ratio_cabin",
    "pantry": "target_window_ratio_pantry",
}


def analyze_light_distribution(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score natural light based on window_area_pct per zone."""
    warnings: list[dict] = []

    evaluable = []
    for z in zones:
        if z["zone_type"] not in _WINDOW_TARGET_KEYS:
            continue
        props = z.get("properties") or {}
        if "window_area_pct" in props:
            evaluable.append(z)

    if not evaluable:
        warnings.append({
            "severity": "info",
            "message": "Keine Fensterdaten vorhanden — Lichtverteilung nicht bewertbar",
            "suggestion": "window_area_pct in Zone-Eigenschaften angeben (0.0–1.0)",
        })
        return 50.0, warnings, {"zones_evaluated": 0}

    zone_scores = []
    for z in evaluable:
        pct = z["properties"]["window_area_pct"]
        target_key = _WINDOW_TARGET_KEYS[z["zone_type"]]
        target = config[target_key]

        if pct >= target:
            zone_scores.append(100.0)
        else:
            ratio = pct / target if target > 0 else 0.0
            zone_scores.append(ratio * 100.0)
            if ratio < 0.6:
                warnings.append({
                    "severity": "warning",
                    "message": f"Zone '{z['name']}' zu dunkel (Fensteranteil: {pct:.0%}, Ziel: {target:.0%})",
                    "suggestion": f"Fensterfläche in '{z['name']}' vergrößern",
                })

    score = sum(zone_scores) / len(zone_scores)
    return score, warnings, {"zones_evaluated": len(zone_scores)}
```

- [ ] **Step 4: Run tests to verify they pass**

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/emotional.py backend/tests/test_emotional.py
git commit -m "feat: add light distribution sub-analysis"
```

---

### Task 4: Add `analyze_sightline` sub-analysis

Scores maximum interior distance per zone. Longer sightlines = more spacious feel.

**Note:** The spec describes ray-tracing from entry point. This is a deliberate simplification using maximum vertex-to-vertex distance as a proxy. True ray-trace would require wall intersection geometry not yet in the data model. This approximation may overrate narrow corridors with long diagonals — acceptable for v1.

**Files:**
- Modify: `backend/app/services/analysis/emotional.py`
- Modify: `backend/tests/test_emotional.py`

- [ ] **Step 1: Write failing tests**

Add to `backend/tests/test_emotional.py`:

```python
from app.services.analysis.emotional import analyze_sightline


def test_sightline_spacious():
    """Large salon with long sightline -> good score."""
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [4000, 0], [4000, 3000], [0, 3000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_sightline(zones, config)
    assert score >= 80.0
    assert metrics["avg_sightline_m"] > 1.5


def test_sightline_cramped():
    """Tiny zone with short sightline -> low score."""
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [1000, 0], [1000, 800], [0, 800]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_sightline(zones, config)
    assert score < 80.0
    assert len(warnings) > 0


def test_sightline_empty():
    config = _default_config()
    score, warnings, metrics = analyze_sightline([], config)
    assert score == 50.0
```

- [ ] **Step 2: Run tests to verify they fail**

- [ ] **Step 3: Implement**

Add to `emotional.py`, before `run_emotional_analysis`:

```python
# Zone types where sightlines matter
_SIGHTLINE_ZONE_TYPES = {"salon", "cabin", "pantry", "helm", "cockpit"}


def analyze_sightline(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score maximum interior sightline distance per zone."""
    warnings: list[dict] = []
    min_sight = config["min_sightline_m"]

    evaluable = [z for z in zones if z["zone_type"] in _SIGHTLINE_ZONE_TYPES]
    if not evaluable:
        warnings.append({
            "severity": "info",
            "message": "Keine bewertbaren Zonen für Sichtachsen vorhanden",
            "suggestion": "Salon- oder Kabinen-Zonen zum Layout hinzufügen",
        })
        return 50.0, warnings, {"avg_sightline_m": 0.0, "zones_evaluated": 0}

    zone_scores = []
    sightlines = []

    for z in evaluable:
        dist = _max_interior_distance_m(z["polygon"])
        sightlines.append(dist)

        if dist >= min_sight * 1.5:
            zone_scores.append(100.0)
        elif dist >= min_sight:
            ratio = (dist - min_sight) / (min_sight * 0.5)
            zone_scores.append(70.0 + ratio * 30.0)
        else:
            ratio = dist / min_sight if min_sight > 0 else 0.0
            zone_scores.append(ratio * 70.0)
            warnings.append({
                "severity": "warning",
                "message": f"Sichtachse in '{z['name']}' kurz ({dist:.1f}m, empfohlen: {min_sight:.1f}m)",
                "suggestion": f"Raumgeometrie in '{z['name']}' öffnen für längere Sichtachsen",
            })

    avg_sight = sum(sightlines) / len(sightlines) if sightlines else 0.0
    score = sum(zone_scores) / len(zone_scores)
    return score, warnings, {"avg_sightline_m": round(avg_sight, 2), "zones_evaluated": len(zone_scores)}
```

- [ ] **Step 4: Run tests to verify they pass**

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/emotional.py backend/tests/test_emotional.py
git commit -m "feat: add sightline sub-analysis"
```

---

### Task 5: Add `analyze_visual_calm` sub-analysis

Scores material count per zone. 3-5 materials = ideal. <3 sterile, >7 cluttered.

**Files:**
- Modify: `backend/app/services/analysis/emotional.py`
- Modify: `backend/tests/test_emotional.py`

- [ ] **Step 1: Write failing tests**

Add to `backend/tests/test_emotional.py`:

```python
from app.services.analysis.emotional import analyze_visual_calm


def test_visual_calm_ideal():
    """4 materials = ideal range -> 100."""
    zones = [make_zone("salon", "salon", properties={"material_count": 4})]
    config = _default_config()
    score, warnings, metrics = analyze_visual_calm(zones, config)
    assert score >= 90.0


def test_visual_calm_cluttered():
    """8+ materials -> warning."""
    zones = [make_zone("salon", "salon", properties={"material_count": 9})]
    config = _default_config()
    score, warnings, metrics = analyze_visual_calm(zones, config)
    assert score < 80.0
    assert len(warnings) > 0


def test_visual_calm_sterile():
    """1 material -> warning."""
    zones = [make_zone("salon", "salon", properties={"material_count": 1})]
    config = _default_config()
    score, warnings, metrics = analyze_visual_calm(zones, config)
    assert score < 80.0
    assert len(warnings) > 0


def test_visual_calm_no_data():
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_visual_calm(zones, config)
    assert score == 50.0
```

- [ ] **Step 2: Run tests to verify they fail**

- [ ] **Step 3: Implement**

Add to `emotional.py`, before `run_emotional_analysis`:

```python
def analyze_visual_calm(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score visual complexity based on material_count per zone."""
    warnings: list[dict] = []
    ideal_lo, ideal_hi = config["ideal_material_range"]

    evaluable = []
    for z in zones:
        props = z.get("properties") or {}
        if "material_count" in props:
            evaluable.append(z)

    if not evaluable:
        warnings.append({
            "severity": "info",
            "message": "Keine Materialdaten vorhanden — visuelle Ruhe nicht bewertbar",
            "suggestion": "material_count in Zone-Eigenschaften angeben",
        })
        return 50.0, warnings, {"zones_evaluated": 0}

    zone_scores = []
    for z in evaluable:
        count = z["properties"]["material_count"]
        if ideal_lo <= count <= ideal_hi:
            zone_scores.append(100.0)
        elif count < ideal_lo:
            zone_scores.append(max(0.0, count / ideal_lo * 70.0))
            warnings.append({
                "severity": "info",
                "message": f"Zone '{z['name']}' wirkt steril ({count} Materialien, empfohlen: {ideal_lo}–{ideal_hi})",
                "suggestion": f"Materialvielfalt in '{z['name']}' erhöhen",
            })
        else:
            excess = count - ideal_hi
            zone_scores.append(max(0.0, 100.0 - excess * 15.0))
            warnings.append({
                "severity": "warning",
                "message": f"Zone '{z['name']}' wirkt unruhig ({count} Materialien, empfohlen: {ideal_lo}–{ideal_hi})",
                "suggestion": f"Materialvielfalt in '{z['name']}' reduzieren",
            })

    score = sum(zone_scores) / len(zone_scores)
    return score, warnings, {"zones_evaluated": len(zone_scores)}
```

- [ ] **Step 4: Run tests to verify they pass**

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/emotional.py backend/tests/test_emotional.py
git commit -m "feat: add visual calm sub-analysis"
```

---

### Task 6: Add `analyze_ceiling_perception` sub-analysis

Scores absolute ceiling height vs minimum and standard values.

**Files:**
- Modify: `backend/app/services/analysis/emotional.py`
- Modify: `backend/tests/test_emotional.py`

- [ ] **Step 1: Write failing tests**

Add to `backend/tests/test_emotional.py`:

```python
from app.services.analysis.emotional import analyze_ceiling_perception


def test_ceiling_good():
    """Standard height -> high score."""
    zones = [
        make_zone("salon", "salon", height_mm=1950),
        make_zone("cabin", "cabin", height_mm=1950),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_ceiling_perception(zones, config)
    assert score >= 80.0


def test_ceiling_low():
    """Below minimum -> warning."""
    zones = [make_zone("salon", "salon", height_mm=1700)]
    config = _default_config()
    score, warnings, metrics = analyze_ceiling_perception(zones, config)
    assert score < 70.0
    assert any(w["severity"] == "warning" for w in warnings)


def test_ceiling_no_data():
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_ceiling_perception(zones, config)
    assert score == 50.0
```

- [ ] **Step 2: Run tests to verify they fail**

- [ ] **Step 3: Implement**

Add to `emotional.py`, before `run_emotional_analysis`:

```python
def analyze_ceiling_perception(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score ceiling height perception relative to boat class standards."""
    warnings: list[dict] = []
    min_h = config["min_ceiling_mm"]
    std_h = config["standard_ceiling_mm"]

    evaluable = [z for z in zones if z.get("height_mm") is not None]
    if not evaluable:
        warnings.append({
            "severity": "info",
            "message": "Keine Deckenhöhendaten vorhanden — Raumhöheneindruck nicht bewertbar",
            "suggestion": "height_mm für Zonen angeben",
        })
        return 50.0, warnings, {"zones_evaluated": 0, "avg_height_mm": 0}

    zone_scores = []
    heights = []
    for z in evaluable:
        h = z["height_mm"]
        heights.append(h)

        if h >= std_h:
            zone_scores.append(100.0)
        elif h >= min_h:
            ratio = (h - min_h) / (std_h - min_h) if std_h > min_h else 1.0
            zone_scores.append(60.0 + ratio * 40.0)
        else:
            ratio = h / min_h if min_h > 0 else 0.0
            zone_scores.append(ratio * 60.0)
            warnings.append({
                "severity": "warning",
                "message": f"Deckenhöhe in '{z['name']}' zu niedrig ({h:.0f}mm, Minimum: {min_h:.0f}mm)",
                "suggestion": f"Deckenhöhe in '{z['name']}' auf mindestens {min_h:.0f}mm erhöhen",
            })

    avg_h = sum(heights) / len(heights)
    score = sum(zone_scores) / len(zone_scores)
    return score, warnings, {"zones_evaluated": len(zone_scores), "avg_height_mm": round(avg_h, 0)}
```

- [ ] **Step 4: Run tests to verify they pass**

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/emotional.py backend/tests/test_emotional.py
git commit -m "feat: add ceiling perception sub-analysis"
```

---

### Task 7: Add `analyze_inside_outside_flow` and register module

Scores transition quality between interior and cockpit (exterior). Also registers the module in the route handler.

**Files:**
- Modify: `backend/app/services/analysis/emotional.py`
- Modify: `backend/tests/test_emotional.py`
- Modify: `backend/app/api/routes/layouts.py:18-29`

- [ ] **Step 1: Write failing tests**

Add to `backend/tests/test_emotional.py`:

```python
from app.services.analysis.emotional import analyze_inside_outside_flow


def test_inside_outside_flow_good():
    """Wide passage to cockpit -> high score."""
    zones = [
        make_zone("salon", "salon"),
        make_zone("cockpit", "cockpit"),
    ]
    passages = [make_passage("salon", "cockpit", 900)]
    config = _default_config()
    score, warnings, metrics = analyze_inside_outside_flow(zones, passages, config)
    assert score >= 80.0


def test_inside_outside_flow_narrow():
    """Narrow passage to cockpit -> lower score."""
    zones = [
        make_zone("salon", "salon"),
        make_zone("cockpit", "cockpit"),
    ]
    passages = [make_passage("salon", "cockpit", 500)]
    config = _default_config()
    score, warnings, metrics = analyze_inside_outside_flow(zones, passages, config)
    assert score < 80.0
    assert len(warnings) > 0


def test_inside_outside_flow_no_cockpit():
    """No cockpit zone -> degraded score."""
    zones = [make_zone("salon", "salon")]
    passages = []
    config = _default_config()
    score, warnings, metrics = analyze_inside_outside_flow(zones, passages, config)
    assert score < 60.0


# --- Full orchestrator ---

def test_full_emotional_analysis():
    zones = [
        make_zone("salon", "salon", height_mm=1950,
                  polygon=[[0, 0], [3500, 0], [3500, 3000], [0, 3000]],
                  properties={"window_area_pct": 0.32, "material_count": 4}),
        make_zone("cabin", "cabin", height_mm=1950,
                  polygon=[[0, 3000], [2500, 3000], [2500, 5000], [0, 5000]],
                  properties={"window_area_pct": 0.20, "material_count": 3}),
        make_zone("cockpit", "cockpit",
                  polygon=[[0, 5000], [3500, 5000], [3500, 7000], [0, 7000]]),
    ]
    passages = [
        make_passage("salon", "cabin", 750),
        make_passage("salon", "cockpit", 850),
    ]
    result = run_emotional_analysis(zones, passages, "cruising_sail")
    assert result["module"] == "emotional"
    assert 0 <= result["overall_score"] <= 100
    assert len(result["sub_scores"]) == 6
    assert "room_proportion" in result["sub_scores"]
    assert "ceiling_perception" in result["sub_scores"]
    assert "inside_outside_flow" in result["sub_scores"]


def test_emotional_boat_class_difference():
    zones = [
        make_zone("salon", "salon", height_mm=1950,
                  polygon=[[0, 0], [3500, 0], [3500, 3000], [0, 3000]],
                  properties={"window_area_pct": 0.25, "material_count": 4}),
        make_zone("cockpit", "cockpit",
                  polygon=[[0, 3000], [3500, 3000], [3500, 5000], [0, 5000]]),
    ]
    passages = [make_passage("salon", "cockpit", 700)]
    result_small = run_emotional_analysis(zones, passages, "small_sail")
    result_super = run_emotional_analysis(zones, passages, "superyacht")
    assert result_small["overall_score"] != result_super["overall_score"]


def test_emotional_warnings_sorted():
    """Warnings must be sorted by severity: critical > warning > info."""
    zones = [
        make_zone("salon", "salon", height_mm=1700,
                  polygon=[[0, 0], [1000, 0], [1000, 800], [0, 800]],
                  properties={"window_area_pct": 0.05, "material_count": 9}),
    ]
    passages = []
    result = run_emotional_analysis(zones, passages, "cruising_sail")
    severities = [w["severity"] for w in result["warnings"]]
    severity_order = {"critical": 0, "warning": 1, "info": 2}
    severity_values = [severity_order.get(s, 2) for s in severities]
    assert severity_values == sorted(severity_values), f"Warnings not sorted: {severities}"


def test_emotional_config_overrides():
    zones = [make_zone("salon", "salon", height_mm=1950)]
    passages = []
    result = run_emotional_analysis(zones, passages, "cruising_sail",
                                     config_overrides={"min_ceiling_mm": 1500})
    assert result["config_used"]["min_ceiling_mm"] == 1500
```

- [ ] **Step 2: Run tests to verify they fail**

- [ ] **Step 3: Implement `analyze_inside_outside_flow`**

Add to `emotional.py`, before `run_emotional_analysis`:

```python
def analyze_inside_outside_flow(zones: list[dict], passages: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score transition quality between interior zones and cockpit."""
    warnings: list[dict] = []
    min_width = config["min_cockpit_passage_mm"]

    cockpit_zones = {z["name"] for z in zones if z["zone_type"] == "cockpit"}
    if not cockpit_zones:
        warnings.append({
            "severity": "warning",
            "message": "Kein Cockpit im Layout — Innen-Außen-Übergang nicht bewertbar",
            "suggestion": "Cockpit-Zone zum Layout hinzufügen",
        })
        return 30.0, warnings, {"cockpit_passages": 0, "max_passage_width_mm": 0}

    cockpit_passages = []
    for p in passages:
        if p["from_zone"] in cockpit_zones or p["to_zone"] in cockpit_zones:
            cockpit_passages.append(p)

    if not cockpit_passages:
        warnings.append({
            "severity": "warning",
            "message": "Kein Durchgang zum Cockpit vorhanden",
            "suggestion": "Durchgang zwischen Innenraum und Cockpit hinzufügen",
        })
        return 20.0, warnings, {"cockpit_passages": 0, "max_passage_width_mm": 0}

    max_width = max(p["width_mm"] for p in cockpit_passages)
    widths = [p["width_mm"] for p in cockpit_passages]

    passage_scores = []
    for w in widths:
        if w >= min_width * 1.3:
            passage_scores.append(100.0)
        elif w >= min_width:
            ratio = (w - min_width) / (min_width * 0.3)
            passage_scores.append(70.0 + ratio * 30.0)
        else:
            ratio = w / min_width if min_width > 0 else 0.0
            passage_scores.append(ratio * 70.0)
            warnings.append({
                "severity": "warning",
                "message": f"Cockpit-Durchgang zu schmal ({w:.0f}mm, empfohlen: {min_width:.0f}mm)",
                "suggestion": f"Cockpit-Durchgang auf mindestens {min_width:.0f}mm erweitern",
            })

    score = sum(passage_scores) / len(passage_scores)
    return score, warnings, {
        "cockpit_passages": len(cockpit_passages),
        "max_passage_width_mm": max_width,
    }
```

- [ ] **Step 4: Register module in route handler**

In `backend/app/api/routes/layouts.py`, add the import:
```python
from app.services.analysis.emotional import run_emotional_analysis
```

And add to `ANALYSIS_MODULES` dict:
```python
ANALYSIS_MODULES = {
    "ergonomics": run_ergonomics_analysis,
    "volume_storage": run_volume_storage_analysis,
    "emotional": run_emotional_analysis,
}
```

- [ ] **Step 5: Run ALL tests**

Run: `cd /c/Users/ThinkPad/Documents/AYDI/backend && PYTHONPATH=. python -m pytest tests/ -v`
Expected: All tests PASS (ergonomics + volume_storage + emotional + dxf_parser)

- [ ] **Step 6: Commit**

```bash
git add backend/app/services/analysis/emotional.py backend/tests/test_emotional.py backend/app/api/routes/layouts.py
git commit -m "feat: add emotional design analysis module with 6 sub-analyses"
```

---

## Summary

| Task | What | Files |
|------|------|-------|
| 1 | Module scaffold + defaults + orchestrator + helpers | `emotional.py`, `test_emotional.py` |
| 2 | `analyze_room_proportion` (TDD) | `emotional.py`, tests |
| 3 | `analyze_light_distribution` (TDD) | `emotional.py`, tests |
| 4 | `analyze_sightline` (TDD) | `emotional.py`, tests |
| 5 | `analyze_visual_calm` (TDD) | `emotional.py`, tests |
| 6 | `analyze_ceiling_perception` (TDD) | `emotional.py`, tests |
| 7 | `analyze_inside_outside_flow` + route registration + integration tests | `emotional.py`, tests, `layouts.py` |

Total: ~300 lines new module, ~180 lines tests, 1 new file, 1 modified route.
