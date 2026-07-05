> **⚠️ ARCHIV — HISTORISCHER PLANUNGSSTAND (nicht maßgeblich).**
> Dieses Dokument beschreibt einen früheren Planungs-/Design-Stand und trackt den aktuellen Code **nicht**.
> Bekannte Drift: 4 statt real **13 Bootsklassen** (`BoatClass`-Enum); abweichende Sub-Analysen/Gewichte; einzelne enthaltene Tests schlagen gegen den Ist-Code fehl.
> **Maßgeblich ist `CLAUDE.md`** (plus der Code). Nicht zum Ableiten von Enums, Return-Contracts oder Tests verwenden.

# Volume & Storage Module Upgrade Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade the existing 3-sub-analysis volume_storage module to the full 5-sub-analysis spec from CLAUDE.md, adding volume utilization and furniture ratio analyses.

**Architecture:** The volume_storage module (`backend/app/services/analysis/volume_storage.py`) already has 3 working sub-analyses (storage_ratio, storage_distribution, storage_accessibility). We add 2 new sub-analyses (volume_utilization, furniture_ratio), update BOAT_CLASS_DEFAULTS to match the CLAUDE.md spec with 5-weight structure, and update all tests. The module follows the same pure-function pattern as ergonomics.py.

**Tech Stack:** Python 3.12, pytest, Shapely (polygon area via shoelace formula)

---

## File Structure

| File | Action | Responsibility |
|------|--------|----------------|
| `backend/app/services/analysis/volume_storage.py` | Modify | Add 2 sub-analyses, update defaults |
| `backend/tests/test_volume_storage.py` | Modify | Add tests for new sub-analyses, update existing |
| `backend/tests/conftest.py` | Modify | Extend `make_zone` helper with `properties` and `height_mm` params |

No new files. No route changes needed — `volume_storage` is already registered in `layouts.py:26-29`.

---

### Task 1: Extend `make_zone` test helper with `properties` and `height_mm`

The new sub-analyses need zone `properties` (for furniture data) and `height_mm` (for volume calculation). The shared test helper `make_zone` in `conftest.py` must support these fields.

**Files:**
- Modify: `backend/tests/conftest.py:1-18`
- Test: `backend/tests/test_volume_storage.py` (existing tests must still pass)

- [ ] **Step 1: Update `make_zone` to accept `properties` and `height_mm`**

In `backend/tests/conftest.py`, update the `make_zone` function:

```python
def make_zone(
    name: str,
    zone_type: str,
    polygon: list[list[float]] | None = None,
    is_crew_area: bool = False,
    is_guest_area: bool = False,
    visibility_angle: float | None = None,
    height_mm: float | None = None,
    properties: dict | None = None,
) -> dict:
    if polygon is None:
        polygon = [[0, 0], [2000, 0], [2000, 2000], [0, 2000]]
    zone = {
        "name": name,
        "zone_type": zone_type,
        "polygon": polygon,
        "is_crew_area": is_crew_area,
        "is_guest_area": is_guest_area,
        "visibility_angle": visibility_angle,
    }
    if height_mm is not None:
        zone["height_mm"] = height_mm
    if properties is not None:
        zone["properties"] = properties
    return zone
```

- [ ] **Step 2: Run existing tests to verify nothing breaks**

Run: `cd /c/Users/ThinkPad/Documents/AYDI/backend && PYTHONPATH=. python -m pytest tests/ -v`
Expected: All existing tests PASS (19 ergonomics + 9 volume_storage)

- [ ] **Step 3: Commit**

```bash
git add backend/tests/conftest.py
git commit -m "feat: extend make_zone helper with properties and height_mm params"
```

---

### Task 2: Update BOAT_CLASS_DEFAULTS to match CLAUDE.md spec

The current defaults have 3 weights (storage_ratio, storage_distribution, storage_accessibility). The spec calls for 5 weights that sum to 1.0 (utilization, storage_ratio, accessibility, distribution, furniture). Also add new config keys for utilization and furniture thresholds.

**Files:**
- Modify: `backend/app/services/analysis/volume_storage.py:10-55`
- Test: `backend/tests/test_volume_storage.py`

**Note:** This task changes both config key names (`ideal_storage_ratio` → `target_storage_ratio`) AND values (e.g., small_sail target drops from 0.22 to 0.18). This is an intentional scoring behavior change to align with the CLAUDE.md spec. Existing layouts may score differently after this change.

- [ ] **Step 1: Replace BOAT_CLASS_DEFAULTS AND update `analyze_storage_ratio` atomically**

**IMPORTANT:** Both changes must be applied together. If only the defaults are replaced without updating `analyze_storage_ratio`, existing tests will crash with `KeyError: 'ideal_storage_ratio'`.

In `backend/app/services/analysis/volume_storage.py`, replace lines 10-55 with:

```python
BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "target_utilization": 0.70,
        "min_utilization": 0.50,
        "target_storage_ratio": 0.18,
        "min_storage_ratio": 0.15,
        "min_storage_zones": 2,
        "max_distribution_imbalance": 0.6,
        "max_furniture_ratio": 0.55,
        "min_furniture_ratio": 0.20,
        "weights": {
            "utilization": 0.30,
            "storage_ratio": 0.25,
            "storage_accessibility": 0.20,
            "storage_distribution": 0.15,
            "furniture_ratio": 0.10,
        },
    },
    "cruising_sail": {
        "target_utilization": 0.72,
        "min_utilization": 0.50,
        "target_storage_ratio": 0.15,
        "min_storage_ratio": 0.12,
        "min_storage_zones": 3,
        "max_distribution_imbalance": 0.5,
        "max_furniture_ratio": 0.50,
        "min_furniture_ratio": 0.22,
        "weights": {
            "utilization": 0.25,
            "storage_ratio": 0.25,
            "storage_accessibility": 0.20,
            "storage_distribution": 0.15,
            "furniture_ratio": 0.15,
        },
    },
    "large_motor": {
        "target_utilization": 0.70,
        "min_utilization": 0.45,
        "target_storage_ratio": 0.12,
        "min_storage_ratio": 0.10,
        "min_storage_zones": 4,
        "max_distribution_imbalance": 0.4,
        "max_furniture_ratio": 0.50,
        "min_furniture_ratio": 0.25,
        "weights": {
            "utilization": 0.20,
            "storage_ratio": 0.20,
            "storage_accessibility": 0.25,
            "storage_distribution": 0.15,
            "furniture_ratio": 0.20,
        },
    },
    "superyacht": {
        "target_utilization": 0.65,
        "min_utilization": 0.40,
        "target_storage_ratio": 0.10,
        "min_storage_ratio": 0.08,
        "min_storage_zones": 6,
        "max_distribution_imbalance": 0.3,
        "max_furniture_ratio": 0.45,
        "min_furniture_ratio": 0.25,
        "weights": {
            "utilization": 0.15,
            "storage_ratio": 0.15,
            "storage_accessibility": 0.25,
            "storage_distribution": 0.20,
            "furniture_ratio": 0.25,
        },
    },
}
```

Also in the same file, in `analyze_storage_ratio`, change:
```python
    ideal = config["ideal_storage_ratio"]
```
to:
```python
    ideal = config["target_storage_ratio"]
```

- [ ] **Step 2: Run existing tests to verify they still pass**

Run: `cd /c/Users/ThinkPad/Documents/AYDI/backend && PYTHONPATH=. python -m pytest tests/test_volume_storage.py -v`
Expected: All 9 tests PASS (config key `ideal_storage_ratio` → `target_storage_ratio` is the only breaking rename)

- [ ] **Step 3: Commit**

```bash
git add backend/app/services/analysis/volume_storage.py backend/tests/test_volume_storage.py
git commit -m "feat: update volume_storage defaults to 5-weight CLAUDE.md spec"
```

---

### Task 3: Add `analyze_volume_utilization` sub-analysis

Measures what fraction of the hull footprint (bounding box of all zones) is covered by defined zone areas. Good boats utilize 65-75% of available space.

**Note:** This is an area-based approximation. True volumetric analysis would require hull geometry data not yet in the data model. Area utilization is a reasonable proxy.

**Files:**
- Modify: `backend/app/services/analysis/volume_storage.py`
- Modify: `backend/tests/test_volume_storage.py`

- [ ] **Step 1: Write failing tests for volume utilization**

Add to `backend/tests/test_volume_storage.py`:

```python
from app.services.analysis.volume_storage import analyze_volume_utilization


def test_volume_utilization_good():
    """Zones cover ~73% of bounding box → good score."""
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [4000, 0], [4000, 3000], [0, 3000]]),
        make_zone("cabin", "cabin", polygon=[[0, 3000], [3000, 3000], [3000, 5000], [0, 5000]]),
        make_zone("pantry", "pantry", polygon=[[3000, 3000], [4000, 3000], [4000, 5000], [3000, 5000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_volume_utilization(zones, config)
    assert score >= 80.0
    assert metrics["utilization_ratio"] > 0.6


def test_volume_utilization_poor():
    """Single small zone in large bounding box → poor score."""
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [1000, 0], [1000, 1000], [0, 1000]]),
        make_zone("cabin", "cabin", polygon=[[9000, 9000], [10000, 9000], [10000, 10000], [9000, 10000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_volume_utilization(zones, config)
    assert score < 50.0
    assert any(w["severity"] in ("warning", "critical") for w in warnings)


def test_volume_utilization_empty():
    """No zones → degraded score 50 + info warning."""
    config = _default_config()
    score, warnings, metrics = analyze_volume_utilization([], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /c/Users/ThinkPad/Documents/AYDI/backend && PYTHONPATH=. python -m pytest tests/test_volume_storage.py::test_volume_utilization_good -v`
Expected: FAIL with ImportError (analyze_volume_utilization not defined)

- [ ] **Step 3: Implement `analyze_volume_utilization`**

Add to `backend/app/services/analysis/volume_storage.py`, after the `_bfs_reachable` function (after line 101):

```python
def analyze_volume_utilization(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score how efficiently the hull footprint is used by defined zones."""
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "severity": "info",
            "message": "Keine Zonen definiert — Volumennutzung kann nicht bewertet werden",
            "suggestion": "Zonen zum Layout hinzufügen",
        })
        return 50.0, warnings, {"utilization_ratio": 0.0, "zone_area_sqmm": 0, "bbox_area_sqmm": 0}

    all_points = [p for z in zones for p in z["polygon"]]
    if not all_points:
        return 50.0, warnings, {"utilization_ratio": 0.0, "zone_area_sqmm": 0, "bbox_area_sqmm": 0}

    min_x = min(p[0] for p in all_points)
    max_x = max(p[0] for p in all_points)
    min_y = min(p[1] for p in all_points)
    max_y = max(p[1] for p in all_points)

    bbox_area = (max_x - min_x) * (max_y - min_y)
    if bbox_area == 0:
        warnings.append({
            "severity": "info",
            "message": "Zonenfläche nicht berechenbar (degenerierte Geometrie)",
            "suggestion": "Zonenpolygone überprüfen",
        })
        return 50.0, warnings, {"utilization_ratio": 0.0, "zone_area_sqmm": 0, "bbox_area_sqmm": 0}

    zone_area = sum(_polygon_area_sqmm(z["polygon"]) for z in zones)
    ratio = zone_area / bbox_area

    target = config["target_utilization"]
    minimum = config["min_utilization"]

    if ratio >= target:
        score = 100.0
    elif ratio >= minimum:
        score = 50.0 + (ratio - minimum) / (target - minimum) * 50.0
        warnings.append({
            "severity": "info",
            "message": f"Flächennutzung unter Zielwert ({ratio:.0%}, Ziel: {target:.0%})",
            "suggestion": f"Flächennutzung auf {target:.0%} erhöhen",
        })
    else:
        score = (ratio / minimum) * 50.0 if minimum > 0 else 0.0
        warnings.append({
            "severity": "warning",
            "message": f"Flächennutzung gering ({ratio:.0%}, Ziel: {target:.0%})",
            "suggestion": f"Flächennutzung auf mindestens {minimum:.0%} erhöhen",
        })

    return score, warnings, {
        "utilization_ratio": round(ratio, 4),
        "zone_area_sqmm": zone_area,
        "bbox_area_sqmm": bbox_area,
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /c/Users/ThinkPad/Documents/AYDI/backend && PYTHONPATH=. python -m pytest tests/test_volume_storage.py -k "volume_utilization" -v`
Expected: All 3 new tests PASS

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/volume_storage.py backend/tests/test_volume_storage.py
git commit -m "feat: add volume utilization sub-analysis"
```

---

### Task 4: Add `analyze_furniture_ratio` sub-analysis

Checks per-zone furniture coverage using `zone["properties"]["furniture_area_pct"]` if available. Flags zones where furniture takes >max_furniture_ratio (cramped) or <min_furniture_ratio (wasted). Gracefully degrades when no furniture data is present.

**Files:**
- Modify: `backend/app/services/analysis/volume_storage.py`
- Modify: `backend/tests/test_volume_storage.py`

- [ ] **Step 1: Write failing tests for furniture ratio**

Add to `backend/tests/test_volume_storage.py`:

```python
from app.services.analysis.volume_storage import analyze_furniture_ratio


def test_furniture_ratio_good():
    """All zones have furniture in acceptable range → high score."""
    zones = [
        make_zone("salon", "salon", properties={"furniture_area_pct": 0.35}),
        make_zone("cabin", "cabin", properties={"furniture_area_pct": 0.40}),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_furniture_ratio(zones, config)
    assert score >= 80.0
    assert metrics["zones_evaluated"] == 2


def test_furniture_ratio_cramped():
    """Zone furniture > max threshold → warning."""
    zones = [
        make_zone("cabin", "cabin", properties={"furniture_area_pct": 0.70}),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_furniture_ratio(zones, config)
    assert score < 80.0
    assert any("übermöbliert" in w["message"].lower() or "möblierung" in w["message"].lower() for w in warnings)


def test_furniture_ratio_sparse():
    """Zone furniture < min threshold → warning."""
    zones = [
        make_zone("salon", "salon", properties={"furniture_area_pct": 0.10}),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_furniture_ratio(zones, config)
    assert score < 100.0
    assert len(warnings) > 0


def test_furniture_ratio_no_data():
    """No furniture data on any zone → degraded score 50 + info."""
    zones = [make_zone("salon", "salon"), make_zone("cabin", "cabin")]
    config = _default_config()
    score, warnings, metrics = analyze_furniture_ratio(zones, config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
    assert metrics["zones_evaluated"] == 0


def test_furniture_ratio_mixed_data():
    """Some zones have furniture data, some don't → only score zones with data."""
    zones = [
        make_zone("salon", "salon", properties={"furniture_area_pct": 0.35}),
        make_zone("cabin", "cabin"),  # no properties
    ]
    config = _default_config()
    score, warnings, metrics = analyze_furniture_ratio(zones, config)
    assert score > 50.0  # at least the salon is evaluated
    assert metrics["zones_evaluated"] == 1


def test_furniture_ratio_excluded_types():
    """Storage/engine zones with furniture data are ignored."""
    zones = [
        make_zone("engine1", "engine", properties={"furniture_area_pct": 0.90}),
        make_zone("storage1", "storage", properties={"furniture_area_pct": 0.90}),
        make_zone("salon", "salon", properties={"furniture_area_pct": 0.35}),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_furniture_ratio(zones, config)
    assert metrics["zones_evaluated"] == 1  # only salon
    assert score >= 80.0  # salon is fine, excluded zones ignored
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd /c/Users/ThinkPad/Documents/AYDI/backend && PYTHONPATH=. python -m pytest tests/test_volume_storage.py::test_furniture_ratio_good -v`
Expected: FAIL with ImportError (analyze_furniture_ratio not defined)

- [ ] **Step 3: Implement `analyze_furniture_ratio`**

Add to `backend/app/services/analysis/volume_storage.py`, after `analyze_volume_utilization`:

```python
# Zone types excluded from furniture evaluation (no furniture expected)
_FURNITURE_EXCLUDED_TYPES = {"engine", "storage", "swim_platform", "tender_garage", "foredeck"}


def analyze_furniture_ratio(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Score furniture density per zone using properties.furniture_area_pct."""
    warnings: list[dict] = []
    max_ratio = config["max_furniture_ratio"]
    min_ratio = config["min_furniture_ratio"]

    evaluable = []
    for z in zones:
        if z["zone_type"] in _FURNITURE_EXCLUDED_TYPES:
            continue
        props = z.get("properties") or {}
        if "furniture_area_pct" in props:
            evaluable.append(z)

    if not evaluable:
        warnings.append({
            "severity": "info",
            "message": "Keine Möblierungsdaten vorhanden — Bewertung nicht möglich",
            "suggestion": "furniture_area_pct in Zone-Eigenschaften angeben (0.0–1.0)",
        })
        return 50.0, warnings, {"zones_evaluated": 0, "cramped": 0, "sparse": 0}

    zone_scores = []
    cramped = 0
    sparse = 0

    for z in evaluable:
        pct = z["properties"]["furniture_area_pct"]
        if pct > max_ratio:
            cramped += 1
            excess = pct - max_ratio
            zone_score = max(0.0, 100.0 - (excess / max_ratio) * 100.0)
            zone_label = z["name"]
            warnings.append({
                "severity": "warning",
                "message": f"Zone '{zone_label}' übermöbliert ({pct:.0%}, max: {max_ratio:.0%})",
                "suggestion": f"Möblierung in '{zone_label}' reduzieren",
            })
        elif pct < min_ratio:
            sparse += 1
            zone_score = max(0.0, (pct / min_ratio) * 80.0)
            zone_label = z["name"]
            warnings.append({
                "severity": "info",
                "message": f"Zone '{zone_label}' spärlich möbliert ({pct:.0%}, min: {min_ratio:.0%})",
                "suggestion": f"Möblierung in '{zone_label}' erhöhen oder Zonengröße reduzieren",
            })
        else:
            zone_score = 100.0

        zone_scores.append(zone_score)

    score = sum(zone_scores) / len(zone_scores)
    return score, warnings, {"zones_evaluated": len(evaluable), "cramped": cramped, "sparse": sparse}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd /c/Users/ThinkPad/Documents/AYDI/backend && PYTHONPATH=. python -m pytest tests/test_volume_storage.py -k "furniture_ratio" -v`
Expected: All 5 new tests PASS

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/volume_storage.py backend/tests/test_volume_storage.py
git commit -m "feat: add furniture ratio sub-analysis"
```

---

### Task 5: Wire new sub-analyses into orchestrator and update integration tests

Register `analyze_volume_utilization` and `analyze_furniture_ratio` in the `run_volume_storage_analysis` orchestrator. Update integration tests to verify all 5 sub-scores appear.

**Files:**
- Modify: `backend/app/services/analysis/volume_storage.py:241-245` (analyses list in orchestrator)
- Modify: `backend/tests/test_volume_storage.py` (integration tests)

- [ ] **Step 1: Update the analyses list in `run_volume_storage_analysis`**

In `backend/app/services/analysis/volume_storage.py`, in the `run_volume_storage_analysis` function, replace the `analyses` list:

```python
    analyses = [
        ("utilization", lambda: analyze_volume_utilization(zones, config)),
        ("storage_ratio", lambda: analyze_storage_ratio(zones, config)),
        ("storage_distribution", lambda: analyze_storage_distribution(zones, config)),
        ("storage_accessibility", lambda: analyze_storage_accessibility(zones, passages, config)),
        ("furniture_ratio", lambda: analyze_furniture_ratio(zones, config)),
    ]
```

- [ ] **Step 2: Update `test_full_volume_analysis` to check all 5 sub-scores**

In `backend/tests/test_volume_storage.py`, replace `test_full_volume_analysis`:

```python
def test_full_volume_analysis():
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [5000, 0], [5000, 3000], [0, 3000]],
                  properties={"furniture_area_pct": 0.35}),
        make_zone("storage1", "storage", polygon=[[0, 3000], [2000, 3000], [2000, 5000], [0, 5000]]),
        make_zone("storage2", "storage", polygon=[[3000, 3000], [5000, 3000], [5000, 5000], [3000, 5000]]),
    ]
    passages = [make_passage("salon", "storage1"), make_passage("salon", "storage2")]
    result = run_volume_storage_analysis(zones, passages, "cruising_sail")
    assert result["module"] == "volume_storage"
    assert 0 <= result["overall_score"] <= 100
    assert "storage_ratio" in result["sub_scores"]
    assert "utilization" in result["sub_scores"]
    assert "furniture_ratio" in result["sub_scores"]
    assert "storage_distribution" in result["sub_scores"]
    assert "storage_accessibility" in result["sub_scores"]
    assert len(result["sub_scores"]) == 5
```

- [ ] **Step 3: Add test for config overrides and boat-class differentiation**

Add to `backend/tests/test_volume_storage.py`:

```python
def test_volume_boat_class_difference_with_furniture():
    """Different boat classes produce different scores with furniture data."""
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [5000, 0], [5000, 3000], [0, 3000]],
                  properties={"furniture_area_pct": 0.35}),
        make_zone("cabin", "cabin", polygon=[[0, 3000], [3000, 3000], [3000, 5000], [0, 5000]],
                  properties={"furniture_area_pct": 0.40}),
        make_zone("storage1", "storage", polygon=[[3000, 3000], [5000, 3000], [5000, 5000], [3000, 5000]]),
    ]
    passages = [make_passage("salon", "cabin"), make_passage("salon", "storage1")]
    result_small = run_volume_storage_analysis(zones, passages, "small_sail")
    result_super = run_volume_storage_analysis(zones, passages, "superyacht")
    # Different weights produce different overall scores
    assert result_small["overall_score"] != result_super["overall_score"]
    # Both should have all 5 sub-scores
    assert len(result_small["sub_scores"]) == 5
    assert len(result_super["sub_scores"]) == 5


def test_volume_config_overrides():
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [5000, 0], [5000, 3000], [0, 3000]]),
        make_zone("storage1", "storage", polygon=[[0, 3000], [2000, 3000], [2000, 5000], [0, 5000]]),
    ]
    passages = [make_passage("salon", "storage1")]
    result = run_volume_storage_analysis(zones, passages, "cruising_sail",
                                         config_overrides={"target_utilization": 0.99})
    assert result["config_used"]["target_utilization"] == 0.99
```

- [ ] **Step 4: Run all tests**

Run: `cd /c/Users/ThinkPad/Documents/AYDI/backend && PYTHONPATH=. python -m pytest tests/ -v`
Expected: All tests PASS (19 ergonomics + ~17 volume_storage)

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/volume_storage.py backend/tests/test_volume_storage.py
git commit -m "feat: wire 5 sub-analyses in volume_storage orchestrator"
```

---

## Summary

| Task | What | Files |
|------|------|-------|
| 1 | Extend `make_zone` helper | `conftest.py` |
| 2 | Update BOAT_CLASS_DEFAULTS to 5-weight spec | `volume_storage.py`, tests |
| 3 | Add `analyze_volume_utilization` (TDD) | `volume_storage.py`, tests |
| 4 | Add `analyze_furniture_ratio` (TDD) | `volume_storage.py`, tests |
| 5 | Wire into orchestrator, integration tests | `volume_storage.py`, tests |

Total: ~100 lines new code, ~120 lines new/updated tests, 0 new files, 0 route changes.
