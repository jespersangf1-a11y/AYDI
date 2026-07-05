> **⚠️ ARCHIV — HISTORISCHER PLANUNGSSTAND (nicht maßgeblich).**
> Dieses Dokument beschreibt einen früheren Planungs-/Design-Stand und trackt den aktuellen Code **nicht**.
> Bekannte Drift: 4 statt real **13 Bootsklassen** (`BoatClass`-Enum); abweichende Sub-Analysen/Gewichte; einzelne enthaltene Tests schlagen gegen den Ist-Code fehl.
> **Maßgeblich ist `CLAUDE.md`** (plus der Code). Nicht zum Ableiten von Enums, Return-Contracts oder Tests verwenden.

# Structural Analysis (Weight Distribution) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a structural analysis module that evaluates weight distribution and center of gravity placement in yacht layouts using heuristic weight estimation from zone geometry.

**Architecture:** Pure-function analysis module following the established AYDI pattern. No new data models or DB access. Estimates zone weights from `zone_type` + polygon area + boat class factor, computes weighted centroid, and evaluates 4 sub-analyses: longitudinal balance, lateral balance, heavy zone placement, load concentration.

**Tech Stack:** Python 3.12, pytest

---

## File Structure

| File | Action | Responsibility |
|------|--------|----------------|
| `backend/app/services/analysis/structural.py` | CREATE | BOAT_CLASS_DEFAULTS, ZONE_WEIGHT_KG_PER_SQM, helpers, 4 sub-analyses, orchestrator |
| `backend/tests/test_structural.py` | CREATE | 22 tests (4-5 per sub-analysis + 7 integration) |
| `backend/app/api/routes/layouts.py` | MODIFY | Import + register `"structural": run_structural_analysis` |

---

### Task 1: Helpers + analyze_fore_aft_balance + tests

**Files:**
- Create: `backend/app/services/analysis/structural.py`
- Create: `backend/tests/test_structural.py`

- [ ] **Step 1: Write failing tests**

```python
"""Tests for structural analysis module (weight distribution)."""
from tests.conftest import make_zone
from app.services.analysis.structural import (
    analyze_fore_aft_balance,
    BOAT_CLASS_DEFAULTS,
)


def _default_config(boat_class="cruising_sail"):
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


# ---------------------------------------------------------------------------
# analyze_fore_aft_balance
# ---------------------------------------------------------------------------


def test_fore_aft_balanced():
    """CoG within ideal range -> score 100."""
    # Two zones centered around 49% of X span (0-10000mm)
    zones = [
        make_zone("salon", "salon", polygon=[[4000, 0], [6000, 0], [6000, 3000], [4000, 3000]]),
        make_zone("engine", "engine", polygon=[[4500, 0], [5500, 0], [5500, 1500], [4500, 1500]]),
    ]
    config = _default_config()  # ideal_cog_x_range = (0.44, 0.54)
    score, warnings, metrics = analyze_fore_aft_balance(zones, config)
    assert score == 100.0
    assert metrics["deviation_pct"] == 0.0
    assert 0.44 <= metrics["cog_x_pct"] <= 0.54


def test_fore_aft_too_far_aft():
    """Heavy zone at stern -> CoG too far aft, warning."""
    zones = [
        make_zone("cockpit", "cockpit", polygon=[[0, 0], [2000, 0], [2000, 3000], [0, 3000]]),
        make_zone("engine", "engine", polygon=[[0, 0], [2000, 0], [2000, 1500], [0, 1500]]),
    ]
    # Both zones at X=0-2000, max span = 3000 (from all zones).
    # CoG will be near X=1000 out of 0-3000 span — that's ~33%, below ideal 44%.
    # Actually centroid of both zones is around X=1000 / max_x=2000 = 50% ...
    # Let me use a layout that clearly pushes CoG aft:
    zones = [
        make_zone("cabin", "cabin", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
        make_zone("engine", "engine", polygon=[[8000, 0], [10000, 0], [10000, 2000], [8000, 2000]]),
        make_zone("storage", "storage", polygon=[[7000, 0], [9000, 0], [9000, 2000], [7000, 2000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_fore_aft_balance(zones, config)
    assert score < 100.0
    assert any(w["code"] == "COG_TOO_FAR_AFT" for w in warnings)
    assert metrics["cog_x_pct"] > 0.54


def test_fore_aft_too_far_forward():
    """Heavy zone at bow -> CoG too far forward, warning."""
    # Engine at bow (low X), light cabin at stern (high X)
    # X=0 is bow per CLAUDE.md coordinate system
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
        make_zone("cabin", "cabin", polygon=[[8000, 0], [10000, 0], [10000, 2000], [8000, 2000]]),
    ]
    config = _default_config()  # ideal_cog_x_range = (0.44, 0.54)
    score, warnings, metrics = analyze_fore_aft_balance(zones, config)
    assert score < 100.0
    assert any(w["code"] == "COG_TOO_FAR_FORWARD" for w in warnings)
    assert metrics["cog_x_pct"] < 0.44


def test_fore_aft_no_zones():
    """No zones -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_fore_aft_balance([], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. python -m pytest tests/test_structural.py -v`
Expected: FAIL — module `structural` does not exist

- [ ] **Step 3: Create structural.py with BOAT_CLASS_DEFAULTS, helpers, and fore_aft sub-analysis**

```python
"""Structural analysis module for yacht layouts (weight distribution).

Evaluates weight distribution and center of gravity placement using
heuristic weight estimation from zone types and polygon geometry.
Pure function module — no database access.
All user-facing strings are in German.
"""
import logging

logger = logging.getLogger(__name__)

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

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}

ZONE_WEIGHT_KG_PER_SQM: dict[str, float] = {
    "engine": 350,
    "storage": 150,
    "tender_garage": 200,
    "pantry": 120,
    "head": 100,
    "salon": 80,
    "cabin": 70,
    "crew_quarters": 70,
    "helm": 60,
    "cockpit": 40,
    "flybridge": 35,
    "foredeck": 25,
    "swim_platform": 30,
}

_DEFAULT_WEIGHT_KG_PER_SQM = 50.0

_HEAVY_ZONE_TYPES = {"engine", "storage", "tender_garage"}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _polygon_area_sqm(polygon: list[list[float]]) -> float:
    """Compute polygon area in square meters (input in mm)."""
    n = len(polygon)
    if n < 3:
        return 0.0
    area = 0.0
    for i in range(n):
        j = (i + 1) % n
        area += polygon[i][0] * polygon[j][1]
        area -= polygon[j][0] * polygon[i][1]
    return abs(area) / 2.0 / 1_000_000


def _polygon_centroid(polygon: list[list[float]]) -> tuple[float, float]:
    """Compute centroid of polygon (input and output in mm)."""
    n = len(polygon)
    if n == 0:
        return 0.0, 0.0
    if n < 3:
        cx = sum(p[0] for p in polygon) / n
        cy = sum(p[1] for p in polygon) / n
        return cx, cy
    signed_area = 0.0
    cx = 0.0
    cy = 0.0
    for i in range(n):
        j = (i + 1) % n
        cross = polygon[i][0] * polygon[j][1] - polygon[j][0] * polygon[i][1]
        signed_area += cross
        cx += (polygon[i][0] + polygon[j][0]) * cross
        cy += (polygon[i][1] + polygon[j][1]) * cross
    signed_area /= 2.0
    if abs(signed_area) < 1e-10:
        cx = sum(p[0] for p in polygon) / n
        cy = sum(p[1] for p in polygon) / n
        return cx, cy
    cx /= 6.0 * signed_area
    cy /= 6.0 * signed_area
    return cx, cy


def _estimate_zone_weight(zone: dict, weight_factor: float) -> float:
    """Estimate zone weight in kg from type, area, and boat class factor."""
    polygon = zone.get("polygon", [])
    area_sqm = _polygon_area_sqm(polygon)
    zone_type = zone.get("zone_type", "")
    kg_per_sqm = ZONE_WEIGHT_KG_PER_SQM.get(zone_type, _DEFAULT_WEIGHT_KG_PER_SQM)
    return area_sqm * kg_per_sqm * weight_factor


def _get_boat_extents(zones: list[dict]) -> tuple[float, float, float, float]:
    """Get bounding box of all zone polygons: (min_x, max_x, min_y, max_y) in mm."""
    all_x = []
    all_y = []
    for z in zones:
        for p in z.get("polygon", []):
            all_x.append(p[0])
            all_y.append(p[1])
    if not all_x:
        return 0.0, 0.0, 0.0, 0.0
    return min(all_x), max(all_x), min(all_y), max(all_y)


# ---------------------------------------------------------------------------
# Sub-analysis: Longitudinal (fore-aft) balance
# ---------------------------------------------------------------------------


def analyze_fore_aft_balance(
    zones: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Evaluate fore-aft weight balance via weighted X-centroid.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "code": "STRUCTURAL_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen für Längsverteilungsanalyse vorhanden.",
            "suggestion": "Zonen dem Layout zuweisen.",
        })
        return 50.0, warnings, {"cog_x_pct": 0.0, "ideal_range": [0, 0], "deviation_pct": 0.0}

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    ideal_range = config.get("ideal_cog_x_range", (0.44, 0.54))
    min_x, max_x, _, _ = _get_boat_extents(zones)
    x_span = max_x - min_x

    if x_span < 1e-6:
        return 50.0, warnings, {"cog_x_pct": 0.5, "ideal_range": list(ideal_range), "deviation_pct": 0.0}

    total_weight = 0.0
    weighted_x = 0.0

    for z in zones:
        w = _estimate_zone_weight(z, weight_factor)
        cx, _ = _polygon_centroid(z.get("polygon", []))
        total_weight += w
        weighted_x += cx * w

    if total_weight < 1e-6:
        return 50.0, warnings, {"cog_x_pct": 0.5, "ideal_range": list(ideal_range), "deviation_pct": 0.0}

    cog_x = weighted_x / total_weight
    cog_x_pct = (cog_x - min_x) / x_span

    # Score
    if ideal_range[0] <= cog_x_pct <= ideal_range[1]:
        deviation = 0.0
        score = 100.0
    else:
        if cog_x_pct < ideal_range[0]:
            deviation = ideal_range[0] - cog_x_pct
        else:
            deviation = cog_x_pct - ideal_range[1]
        score = max(0.0, 100.0 - deviation * 100.0 * 6.67)

    # Warnings
    if cog_x_pct < ideal_range[0]:
        severity = "critical" if deviation > 0.10 else "warning"
        warnings.append({
            "code": "COG_TOO_FAR_FORWARD",
            "severity": severity,
            "message": (
                f"Gewichtsschwerpunkt bei {cog_x_pct:.0%} der Bootslänge — "
                f"zu weit vorne (Ideal: {ideal_range[0]:.0%}–{ideal_range[1]:.0%})."
            ),
            "suggestion": "Schwere Ausrüstung weiter achtern verlagern.",
        })
    elif cog_x_pct > ideal_range[1]:
        severity = "critical" if deviation > 0.10 else "warning"
        warnings.append({
            "code": "COG_TOO_FAR_AFT",
            "severity": severity,
            "message": (
                f"Gewichtsschwerpunkt bei {cog_x_pct:.0%} der Bootslänge — "
                f"zu weit achtern (Ideal: {ideal_range[0]:.0%}–{ideal_range[1]:.0%})."
            ),
            "suggestion": "Schwere Ausrüstung weiter nach vorne verlagern.",
        })

    return score, warnings, {
        "cog_x_pct": round(cog_x_pct, 4),
        "ideal_range": list(ideal_range),
        "deviation_pct": round(deviation, 4),
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. python -m pytest tests/test_structural.py -v`
Expected: 4 PASS

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/structural.py backend/tests/test_structural.py
git commit -m "feat: add structural analysis module with fore-aft balance"
```

---

### Task 2: analyze_lateral_balance + tests

**Files:**
- Modify: `backend/app/services/analysis/structural.py`
- Modify: `backend/tests/test_structural.py`

- [ ] **Step 1: Write failing tests**

Append to `test_structural.py`:

```python
from app.services.analysis.structural import analyze_lateral_balance


# ---------------------------------------------------------------------------
# analyze_lateral_balance
# ---------------------------------------------------------------------------


def test_lateral_centered():
    """Symmetric layout -> score 100."""
    zones = [
        make_zone("salon", "salon", polygon=[[4000, 500], [6000, 500], [6000, 2500], [4000, 2500]]),
        make_zone("engine", "engine", polygon=[[4000, 500], [6000, 500], [6000, 2500], [4000, 2500]]),
    ]
    config = _default_config()  # lateral_tolerance_pct = 0.05
    score, warnings, metrics = analyze_lateral_balance(zones, config)
    assert score == 100.0
    assert abs(metrics["offset_from_center_pct"]) < 0.01


def test_lateral_offset():
    """Asymmetric layout -> warning, lower score."""
    # Heavy engine on starboard (low Y), light salon on port (high Y)
    # Y span 0-4000, engine centroid Y=1000, salon centroid Y=3000
    # Weighted CoG_y ≈ 34%, offset ≈ 16% >> 5% tolerance
    zones = [
        make_zone("engine", "engine", polygon=[[4000, 0], [6000, 0], [6000, 2000], [4000, 2000]]),
        make_zone("salon", "salon", polygon=[[4000, 2000], [6000, 2000], [6000, 4000], [4000, 4000]]),
    ]
    config = _default_config()  # lateral_tolerance_pct = 0.05
    score, warnings, metrics = analyze_lateral_balance(zones, config)
    assert score < 100.0
    assert any(w["code"] == "COG_LATERAL_OFFSET" for w in warnings)


def test_lateral_no_zones():
    """No zones -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_lateral_balance([], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
```

- [ ] **Step 2: Run tests to verify new tests fail**

Run: `cd backend && PYTHONPATH=. python -m pytest tests/test_structural.py::test_lateral_centered -v`
Expected: FAIL — `analyze_lateral_balance` not defined

- [ ] **Step 3: Implement analyze_lateral_balance**

Append to `structural.py`:

```python
# ---------------------------------------------------------------------------
# Sub-analysis: Lateral balance
# ---------------------------------------------------------------------------


def analyze_lateral_balance(
    zones: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Evaluate port-starboard weight balance via weighted Y-centroid.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "code": "STRUCTURAL_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen für Querverteilungsanalyse vorhanden.",
            "suggestion": "Zonen dem Layout zuweisen.",
        })
        return 50.0, warnings, {"cog_y_pct": 0.5, "offset_from_center_pct": 0.0, "tolerance_pct": 0.0}

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    tolerance = config.get("lateral_tolerance_pct", 0.05)
    _, _, min_y, max_y = _get_boat_extents(zones)
    y_span = max_y - min_y

    if y_span < 1e-6:
        return 100.0, warnings, {"cog_y_pct": 0.5, "offset_from_center_pct": 0.0, "tolerance_pct": tolerance}

    total_weight = 0.0
    weighted_y = 0.0

    for z in zones:
        w = _estimate_zone_weight(z, weight_factor)
        _, cy = _polygon_centroid(z.get("polygon", []))
        total_weight += w
        weighted_y += cy * w

    if total_weight < 1e-6:
        return 50.0, warnings, {"cog_y_pct": 0.5, "offset_from_center_pct": 0.0, "tolerance_pct": tolerance}

    cog_y = weighted_y / total_weight
    cog_y_pct = (cog_y - min_y) / y_span
    offset = abs(cog_y_pct - 0.5)

    if offset <= tolerance:
        score = 100.0
    else:
        excess = offset - tolerance
        score = max(0.0, 100.0 - excess * 100.0 * 10.0)

    if offset > tolerance:
        severity = "critical" if offset > tolerance * 2 else "warning"
        warnings.append({
            "code": "COG_LATERAL_OFFSET",
            "severity": severity,
            "message": (
                f"Gewichtsschwerpunkt {offset:.1%} seitlich versetzt — "
                f"Toleranz: ±{tolerance:.0%} von Mittschiffs."
            ),
            "suggestion": "Schwere Ausrüstung symmetrischer verteilen.",
        })

    return score, warnings, {
        "cog_y_pct": round(cog_y_pct, 4),
        "offset_from_center_pct": round(offset, 4),
        "tolerance_pct": tolerance,
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. python -m pytest tests/test_structural.py -v`
Expected: 7 PASS

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/structural.py backend/tests/test_structural.py
git commit -m "feat: add lateral balance sub-analysis"
```

---

### Task 3: analyze_heavy_zone_placement + analyze_load_concentration + tests

**Files:**
- Modify: `backend/app/services/analysis/structural.py`
- Modify: `backend/tests/test_structural.py`

- [ ] **Step 1: Write failing tests**

Append to `test_structural.py`:

```python
from app.services.analysis.structural import (
    analyze_heavy_zone_placement,
    analyze_load_concentration,
)


# ---------------------------------------------------------------------------
# analyze_heavy_zone_placement
# ---------------------------------------------------------------------------


def test_heavy_placement_central():
    """Heavy zones in central band -> score 100."""
    zones = [
        make_zone("engine", "engine", polygon=[[4000, 0], [6000, 0], [6000, 2000], [4000, 2000]]),
        make_zone("storage", "storage", polygon=[[3000, 0], [5000, 0], [5000, 1000], [3000, 1000]]),
        make_zone("salon", "salon", polygon=[[0, 0], [10000, 0], [10000, 3000], [0, 3000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_heavy_zone_placement(zones, config)
    assert score == 100.0
    assert metrics["central_ratio"] == 1.0


def test_heavy_placement_off_center():
    """Heavy zone at extreme position -> penalty."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [1000, 0], [1000, 1000], [0, 1000]]),
        make_zone("salon", "salon", polygon=[[0, 0], [10000, 0], [10000, 3000], [0, 3000]]),
    ]
    config = _default_config()  # central_band = (0.20, 0.80)
    score, warnings, metrics = analyze_heavy_zone_placement(zones, config)
    # Engine centroid at X=500 out of span 0-10000 = 5%, outside 20-80%
    assert score < 100.0
    assert any(w["code"] == "HEAVY_ZONE_OFF_CENTER" for w in warnings)


def test_heavy_placement_no_heavy_zones():
    """No heavy zones -> score 100, info."""
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [3000, 0], [3000, 2000], [0, 2000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_heavy_zone_placement(zones, config)
    assert score == 100.0
    assert any(w["code"] == "STRUCTURAL_NO_HEAVY_ZONES" for w in warnings)


def test_heavy_placement_no_zones():
    """No zones -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_heavy_zone_placement([], config)
    assert score == 50.0


# ---------------------------------------------------------------------------
# analyze_load_concentration
# ---------------------------------------------------------------------------


def test_load_even():
    """Evenly distributed zones with similar weights -> high score."""
    # Use zones with similar kg/m² to achieve balanced weight distribution
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
        make_zone("pantry", "pantry", polygon=[[4000, 0], [6000, 0], [6000, 2000], [4000, 2000]]),
        make_zone("cabin", "cabin", polygon=[[8000, 0], [10000, 0], [10000, 2000], [8000, 2000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_load_concentration(zones, config)
    assert score >= 70.0
    assert not any(w["code"] == "LOAD_CONCENTRATION_HIGH" for w in warnings)


def test_load_concentrated():
    """All weight in one segment -> warning, low score."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
        make_zone("storage", "storage", polygon=[[0, 0], [3000, 0], [3000, 1000], [0, 1000]]),
        make_zone("cabin", "cabin", polygon=[[0, 0], [10000, 0], [10000, 100], [0, 100]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_load_concentration(zones, config)
    assert score < 70.0
    assert any(w["code"] == "LOAD_CONCENTRATION_HIGH" for w in warnings)


def test_load_single_zone():
    """Single zone -> all weight in one segment, warning."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [3000, 0], [3000, 2000], [0, 2000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_load_concentration(zones, config)
    assert score < 50.0
    assert any(w["code"] == "LOAD_CONCENTRATION_HIGH" for w in warnings)


def test_load_no_zones():
    """No zones -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_load_concentration([], config)
    assert score == 50.0
```

- [ ] **Step 2: Run tests to verify new tests fail**

Run: `cd backend && PYTHONPATH=. python -m pytest tests/test_structural.py::test_heavy_placement_central -v`
Expected: FAIL — `analyze_heavy_zone_placement` not defined

- [ ] **Step 3: Implement analyze_heavy_zone_placement**

Append to `structural.py`:

```python
# ---------------------------------------------------------------------------
# Sub-analysis: Heavy zone placement
# ---------------------------------------------------------------------------


def analyze_heavy_zone_placement(
    zones: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check if heavy zones are centrally positioned.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "code": "STRUCTURAL_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen für Schwerzonen-Analyse vorhanden.",
            "suggestion": "Zonen dem Layout zuweisen.",
        })
        return 50.0, warnings, {
            "heavy_zones": [], "total_heavy_weight_kg": 0.0, "central_ratio": 0.0,
        }

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    central_band = config.get("central_band", (0.20, 0.80))
    min_x, max_x, _, _ = _get_boat_extents(zones)
    x_span = max_x - min_x

    heavy_zones = [z for z in zones if z.get("zone_type") in _HEAVY_ZONE_TYPES]

    if not heavy_zones:
        warnings.append({
            "code": "STRUCTURAL_NO_HEAVY_ZONES",
            "severity": "info",
            "message": "Keine schweren Zonen (Motor, Stauraum) im Layout erkannt.",
            "suggestion": "Motor- und Stauräume im Layout definieren.",
        })
        return 100.0, warnings, {
            "heavy_zones": [], "total_heavy_weight_kg": 0.0, "central_ratio": 1.0,
        }

    if x_span < 1e-6:
        return 100.0, warnings, {
            "heavy_zones": [], "total_heavy_weight_kg": 0.0, "central_ratio": 1.0,
        }

    heavy_info = []
    total_heavy_weight = 0.0
    central_weight = 0.0

    for z in heavy_zones:
        w = _estimate_zone_weight(z, weight_factor)
        cx, _ = _polygon_centroid(z.get("polygon", []))
        cx_pct = (cx - min_x) / x_span
        is_central = central_band[0] <= cx_pct <= central_band[1]

        total_heavy_weight += w
        if is_central:
            central_weight += w
        else:
            severity = "critical" if cx_pct < 0.15 or cx_pct > 0.85 else "warning"
            warnings.append({
                "code": "HEAVY_ZONE_OFF_CENTER",
                "severity": severity,
                "message": (
                    f"Schwere Zone '{z.get('name', '?')}' ({z.get('zone_type')}) "
                    f"bei {cx_pct:.0%} der Bootslänge — "
                    f"außerhalb des zentralen Bereichs ({central_band[0]:.0%}–{central_band[1]:.0%})."
                ),
                "suggestion": f"Zone '{z.get('name', '?')}' weiter zur Mitte verlagern.",
            })

        heavy_info.append({
            "name": z.get("name", "?"),
            "zone_type": z.get("zone_type"),
            "centroid_x_pct": round(cx_pct, 4),
            "weight_kg": round(w, 1),
            "is_central": is_central,
        })

    central_ratio = central_weight / total_heavy_weight if total_heavy_weight > 0 else 1.0

    # Score: penalty per off-center zone proportional to its weight
    score = 100.0
    for hz in heavy_info:
        if not hz["is_central"]:
            penalty = (hz["weight_kg"] / total_heavy_weight) * 50.0
            score -= penalty
    score = max(0.0, score)

    return score, warnings, {
        "heavy_zones": heavy_info,
        "total_heavy_weight_kg": round(total_heavy_weight, 1),
        "central_ratio": round(central_ratio, 4),
    }
```

- [ ] **Step 4: Implement analyze_load_concentration**

Append to `structural.py`:

```python
# ---------------------------------------------------------------------------
# Sub-analysis: Load concentration
# ---------------------------------------------------------------------------


def analyze_load_concentration(
    zones: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Evaluate weight distribution across three longitudinal segments.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "code": "STRUCTURAL_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen für Lastkonzentrationsanalyse vorhanden.",
            "suggestion": "Zonen dem Layout zuweisen.",
        })
        return 50.0, warnings, {
            "segment_weights": {}, "segment_fractions": {},
            "heaviest_segment": None, "cv": 0.0,
        }

    weight_factor = config.get("boat_class_weight_factor", 1.0)
    warn_threshold = config.get("concentration_warn_threshold", 0.55)
    min_x, max_x, _, _ = _get_boat_extents(zones)
    x_span = max_x - min_x

    if x_span < 1e-6:
        return 50.0, warnings, {
            "segment_weights": {}, "segment_fractions": {},
            "heaviest_segment": None, "cv": 0.0,
        }

    # Divide into 3 equal segments
    third = x_span / 3.0
    boundaries = [min_x, min_x + third, min_x + 2 * third, max_x]
    segment_names = ["bow", "middle", "stern"]
    segment_weights: dict[str, float] = {"bow": 0.0, "middle": 0.0, "stern": 0.0}

    for z in zones:
        w = _estimate_zone_weight(z, weight_factor)
        cx, _ = _polygon_centroid(z.get("polygon", []))
        # Assign to segment by centroid position
        if cx < boundaries[1]:
            segment_weights["bow"] += w
        elif cx < boundaries[2]:
            segment_weights["middle"] += w
        else:
            segment_weights["stern"] += w

    total = sum(segment_weights.values())
    if total < 1e-6:
        return 50.0, warnings, {
            "segment_weights": segment_weights, "segment_fractions": {},
            "heaviest_segment": None, "cv": 0.0,
        }

    fractions = {k: v / total for k, v in segment_weights.items()}

    # Coefficient of variation
    mean_w = total / 3.0
    variance = sum((v - mean_w) ** 2 for v in segment_weights.values()) / 3.0
    std_dev = variance ** 0.5
    cv = std_dev / mean_w if mean_w > 0 else 0.0

    score = max(0.0, 100.0 * (1.0 - cv))

    heaviest = max(fractions, key=fractions.get)

    # Warnings
    for name, frac in fractions.items():
        if frac > 0.70:
            warnings.append({
                "code": "LOAD_CONCENTRATION_HIGH",
                "severity": "critical",
                "message": (
                    f"Segment '{name}' trägt {frac:.0%} des Gesamtgewichts — "
                    f"stark ungleichmäßige Verteilung."
                ),
                "suggestion": f"Gewicht aus Segment '{name}' umverteilen.",
            })
        elif frac > warn_threshold:
            warnings.append({
                "code": "LOAD_CONCENTRATION_HIGH",
                "severity": "warning",
                "message": (
                    f"Segment '{name}' trägt {frac:.0%} des Gesamtgewichts — "
                    f"Richtwert: max. {warn_threshold:.0%}."
                ),
                "suggestion": f"Gewicht aus Segment '{name}' gleichmäßiger verteilen.",
            })

    return score, warnings, {
        "segment_weights": {k: round(v, 1) for k, v in segment_weights.items()},
        "segment_fractions": {k: round(v, 4) for k, v in fractions.items()},
        "heaviest_segment": heaviest,
        "cv": round(cv, 4),
    }
```

- [ ] **Step 5: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. python -m pytest tests/test_structural.py -v`
Expected: 15 PASS (4 fore_aft + 3 lateral + 4 heavy_placement + 4 load_concentration)

- [ ] **Step 6: Commit**

```bash
git add backend/app/services/analysis/structural.py backend/tests/test_structural.py
git commit -m "feat: add heavy zone placement and load concentration sub-analyses"
```

---

### Task 4: Orchestrator + integration tests + route registration

**Files:**
- Modify: `backend/app/services/analysis/structural.py`
- Modify: `backend/tests/test_structural.py`
- Modify: `backend/app/api/routes/layouts.py`

- [ ] **Step 1: Write failing integration tests**

Append to `test_structural.py`:

```python
from app.services.analysis.structural import run_structural_analysis, SEVERITY_ORDER


# ---------------------------------------------------------------------------
# Integration
# ---------------------------------------------------------------------------


def test_full_structural_analysis():
    """Complete layout -> valid result structure with all 4 sub-scores."""
    zones = [
        make_zone("cockpit", "cockpit", polygon=[[0, 0], [3800, 0], [3800, 2500], [0, 2500]]),
        make_zone("salon", "salon", polygon=[[0, 2500], [3800, 2500], [3800, 5500], [0, 5500]]),
        make_zone("engine", "engine", polygon=[[1800, 0], [3800, 0], [3800, 1500], [1800, 1500]]),
        make_zone("cabin", "cabin", polygon=[[500, 7500], [3300, 7500], [3300, 10000], [500, 10000]]),
    ]
    result = run_structural_analysis(zones, [], "cruising_sail")
    assert result["module"] == "structural"
    assert 0 <= result["overall_score"] <= 100
    assert "fore_aft" in result["sub_scores"]
    assert "lateral" in result["sub_scores"]
    assert "heavy_placement" in result["sub_scores"]
    assert "load_concentration" in result["sub_scores"]
    assert len(result["sub_scores"]) == 4


def test_structural_warnings_sorted():
    """Warnings sorted: critical -> warning -> info."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [1000, 0], [1000, 500], [0, 500]]),
        make_zone("cabin", "cabin", polygon=[[0, 0], [10000, 0], [10000, 100], [0, 100]]),
    ]
    result = run_structural_analysis(zones, [], "cruising_sail")
    severities = [w["severity"] for w in result["warnings"]]
    order = [SEVERITY_ORDER.get(s, 2) for s in severities]
    assert order == sorted(order)


def test_structural_boat_class_difference():
    """Different boat classes produce different scores."""
    zones = [
        make_zone("salon", "salon", polygon=[[3000, 0], [7000, 0], [7000, 3000], [3000, 3000]]),
        make_zone("engine", "engine", polygon=[[4000, 0], [6000, 0], [6000, 1500], [4000, 1500]]),
    ]
    result_sail = run_structural_analysis(zones, [], "small_sail")
    result_motor = run_structural_analysis(zones, [], "large_motor")
    # Different ideal ranges -> different scores
    assert result_sail["overall_score"] != result_motor["overall_score"]


def test_structural_config_overrides():
    """Config overrides applied and stored in config_used."""
    zones = [make_zone("salon", "salon")]
    result = run_structural_analysis(zones, [], "cruising_sail",
                                     config_overrides={"lateral_tolerance_pct": 0.15})
    assert result["config_used"]["lateral_tolerance_pct"] == 0.15


def test_structural_empty_input():
    """No zones -> short-circuit: score 50, single STRUCTURAL_NO_ZONES warning."""
    result = run_structural_analysis([], [], "cruising_sail")
    assert result["overall_score"] == 50.0
    assert len(result["sub_scores"]) == 4
    assert all(v == 50.0 for v in result["sub_scores"].values())
    assert len(result["warnings"]) == 1
    assert result["warnings"][0]["code"] == "STRUCTURAL_NO_ZONES"


def test_structural_unknown_zone_type():
    """Unknown zone_type uses 50 kg/m² fallback and emits no warning."""
    zones = [
        make_zone("custom", "lounge", polygon=[[3000, 0], [7000, 0], [7000, 3000], [3000, 3000]]),
        make_zone("engine", "engine", polygon=[[4000, 0], [6000, 0], [6000, 1500], [4000, 1500]]),
    ]
    result = run_structural_analysis(zones, [], "cruising_sail")
    assert 0 <= result["overall_score"] <= 100
    # No warning about unknown zone type
    assert not any("unbekannt" in w.get("message", "").lower() for w in result["warnings"])


def test_structural_critical_severity_thresholds():
    """Extreme deviation triggers critical severity."""
    # Engine at bow extreme (X=0), light zone at stern — >10% deviation
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [3000, 0], [3000, 3000], [0, 3000]]),
        make_zone("foredeck", "foredeck", polygon=[[9000, 0], [12000, 0], [12000, 3000], [9000, 3000]]),
    ]
    result = run_structural_analysis(zones, [], "cruising_sail")
    critical_warnings = [w for w in result["warnings"] if w["severity"] == "critical"]
    assert len(critical_warnings) > 0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. python -m pytest tests/test_structural.py::test_full_structural_analysis -v`
Expected: FAIL — `run_structural_analysis` not defined

- [ ] **Step 3: Implement orchestrator**

Append to `structural.py`:

```python
# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


def run_structural_analysis(
    zones: list[dict],
    passages: list[dict],
    boat_class: str,
    config_overrides: dict | None = None,
) -> dict:
    """Orchestrator — runs all structural (weight distribution) sub-analyses.

    Args:
        zones: Layout zones with polygon, zone_type, name.
        passages: Unused — accepted for API pattern consistency.
        boat_class: One of small_sail, cruising_sail, large_motor, superyacht.
        config_overrides: Optional dict to override config values.

    Returns a standardized result dict matching the AYDI analysis module contract.
    """
    if boat_class not in BOAT_CLASS_DEFAULTS:
        raise ValueError(f"Unknown boat class: {boat_class}")

    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    weights = config.pop("weights").copy()

    if config_overrides:
        config.update(config_overrides)

    # Short-circuit: no zones → score 50 + single info warning
    if not zones:
        return {
            "module": "structural",
            "overall_score": 50.0,
            "sub_scores": {k: 50.0 for k in weights},
            "warnings": [{
                "code": "STRUCTURAL_NO_ZONES",
                "severity": "info",
                "message": "Keine Zonen für Strukturanalyse vorhanden.",
                "suggestion": "Zonen dem Layout zuweisen.",
            }],
            "suggestions": ["Zonen dem Layout zuweisen."],
            "metrics": {},
            "config_used": config,
        }

    sub_scores: dict[str, float] = {}
    all_warnings: list[dict] = []
    all_suggestions: list[str] = []
    all_metrics: dict[str, dict] = {}

    analyses = [
        ("fore_aft", lambda: analyze_fore_aft_balance(zones, config)),
        ("lateral", lambda: analyze_lateral_balance(zones, config)),
        ("heavy_placement", lambda: analyze_heavy_zone_placement(zones, config)),
        ("load_concentration", lambda: analyze_load_concentration(zones, config)),
    ]

    for name, fn in analyses:
        try:
            score, warnings, metrics = fn()
            sub_scores[name] = score
            all_warnings.extend(warnings)
            all_metrics[name] = metrics
        except Exception:
            logger.exception("Error in structural sub-analysis %s", name)
            sub_scores[name] = 0.0
            all_warnings.append({
                "code": "ANALYSIS_ERROR",
                "severity": "critical",
                "message": f"Fehler bei Strukturanalyse: {name}",
                "suggestion": "Layoutdaten überprüfen.",
            })

    overall = sum(sub_scores.get(k, 50.0) * w for k, w in weights.items())

    for w in all_warnings:
        suggestion = w.get("suggestion")
        if suggestion and suggestion not in all_suggestions:
            all_suggestions.append(suggestion)

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    return {
        "module": "structural",
        "overall_score": round(overall, 1),
        "sub_scores": {k: round(v, 1) for k, v in sub_scores.items()},
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
    }
```

- [ ] **Step 4: Update layouts.py — add import and register module**

In `backend/app/api/routes/layouts.py`:

Add import (after the materials import):

```python
from app.services.analysis.structural import run_structural_analysis
```

Add to `ANALYSIS_MODULES` dict:

```python
    "structural": run_structural_analysis,
```

- [ ] **Step 5: Run ALL tests to verify everything passes**

Run: `cd backend && PYTHONPATH=. python -m pytest tests/ -v`
Expected: All pass (~171: 149 existing + 22 structural tests)

- [ ] **Step 6: Commit**

```bash
git add backend/app/services/analysis/structural.py backend/tests/test_structural.py backend/app/api/routes/layouts.py
git commit -m "feat: add structural analysis orchestrator and register module"
```

---

## Test Summary

| Sub-analysis | Tests | Coverage |
|---|---|---|
| fore_aft_balance | 4 | balanced, too far aft, too far forward, no zones |
| lateral_balance | 3 | centered, offset, no zones |
| heavy_zone_placement | 4 | central, off-center, no heavy zones, no zones |
| load_concentration | 4 | even, concentrated, single zone, no zones |
| integration | 7 | full layout, warnings sorted, boat class diff, overrides, empty, unknown zone type, critical severity |
| **Total** | **22** | |
