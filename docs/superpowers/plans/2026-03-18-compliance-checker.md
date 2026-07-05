> **⚠️ ARCHIV — HISTORISCHER PLANUNGSSTAND (nicht maßgeblich).**
> Dieses Dokument beschreibt einen früheren Planungs-/Design-Stand und trackt den aktuellen Code **nicht**.
> Bekannte Drift: 4 statt real **13 Bootsklassen** (`BoatClass`-Enum); abweichende Sub-Analysen/Gewichte; einzelne enthaltene Tests schlagen gegen den Ist-Code fehl.
> **Maßgeblich ist `CLAUDE.md`** (plus der Code). Nicht zum Ableiten von Enums, Return-Contracts oder Tests verwenden.

# Compliance Checker Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Automated check of yacht layouts against maritime safety norms (ISO 9094, ISO 12217, ISO 15085, ISO 10133/13297) with CE category validation.

**Architecture:** Pure-function analysis module following the established pattern — `BOAT_CLASS_DEFAULTS` with per-class thresholds/weights, independent sub-analysis functions returning `(score, warnings, metrics)`, orchestrator with weighted sum. Norm version references stored in `config_used`. Compliance levels (conforming/warning/violation) map to existing severity system (info/warning/critical).

**Tech Stack:** Python 3.12, pytest, no external dependencies beyond stdlib.

---

## File Structure

| Action | File | Responsibility |
|--------|------|---------------|
| Create | `backend/app/services/analysis/compliance.py` | All 6 sub-analyses + orchestrator |
| Create | `backend/tests/test_compliance.py` | ~22 tests for all sub-analyses + integration |
| Modify | `backend/app/api/routes/layouts.py:18-31` | Import + register `compliance` module |

## Reference: Existing Patterns

- **Sub-analysis signature:** `analyze_X(zones, [passages,] config) -> tuple[float, list[dict], dict]`
- **Warning dict:** `{"severity": "critical"|"warning"|"info", "message": "German text", "suggestion": "German text"}`
- **Empty/missing input:** return `50.0` + info warning, never raise
- **Orchestrator:** iterate sub-analyses in try/except, weighted sum, sort warnings by severity
- **Test helpers:** `make_zone()`, `make_passage()` from `tests/conftest.py`
- **Test config helper:** `_default_config(boat_class)` that pops weights from copied defaults

## Design Notes

**Data limitations:** The compliance module works with available data (zones, passages, polygons, properties). Where full compliance assessment would require data not in the model (hull geometry, waterline height, fire extinguisher positions), the module degrades gracefully with info-level warnings explaining what data is missing.

**Norm references in warnings:** Each warning message is prefixed with the relevant ISO norm and version (e.g., `"ISO 9094:2015 — ..."`), making it self-documenting. The `norm_versions` dict in `config_used` provides the full reference.

**Compliance level mapping:** ISO compliance levels map to existing severity: violation → critical, warning → warning, conforming → no warning (or info for near-boundary).

---

### Task 1: Scaffold + analyze_escape_routes

**Files:**
- Create: `backend/app/services/analysis/compliance.py`
- Create: `backend/tests/test_compliance.py`

- [ ] **Step 1: Write failing tests for escape routes**

```python
from tests.conftest import make_passage, make_zone

from app.services.analysis.compliance import (
    analyze_escape_routes,
    BOAT_CLASS_DEFAULTS,
)


def _default_config(boat_class="cruising_sail"):
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


def test_escape_route_compliant():
    """Cabin connected to cockpit via wide passage -> score 100."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("cabin1", "cabin"),
    ]
    passages = [make_passage("cabin1", "cockpit", width_mm=700)]
    config = _default_config()
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score == 100.0
    assert metrics["cabins_compliant"] == 1


def test_escape_route_no_cockpit():
    """No cockpit -> score 0, critical warning."""
    zones = [make_zone("cabin1", "cabin")]
    passages = []
    config = _default_config()
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score == 0.0
    assert any(w["severity"] == "critical" for w in warnings)


def test_escape_route_no_cabins():
    """No sleeping zones -> score 100, info."""
    zones = [make_zone("cockpit", "cockpit"), make_zone("salon", "salon")]
    passages = [make_passage("cockpit", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score == 100.0
    assert any(w["severity"] == "info" for w in warnings)
    assert metrics["cabins_total"] == 0


def test_escape_route_unreachable():
    """Cabin with no path to cockpit -> critical."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("cabin1", "cabin"),
        make_zone("salon", "salon"),
    ]
    passages = [make_passage("cockpit", "salon")]  # cabin1 not connected
    config = _default_config()
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score == 0.0
    assert any(w["severity"] == "critical" for w in warnings)
    assert metrics["cabins_compliant"] == 0


def test_escape_route_narrow_passage():
    """Escape route passage below 600mm ISO minimum -> critical, partial score."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("cabin1", "cabin"),
    ]
    passages = [make_passage("cabin1", "cockpit", width_mm=500)]
    config = _default_config()
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score == 50.0  # Reachable but noncompliant -> 50 pts
    assert any(w["severity"] == "critical" for w in warnings)


def test_escape_route_too_long():
    """Escape route with too many hops -> warning."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("salon", "salon"),
        make_zone("pantry", "pantry"),
        make_zone("head", "head"),
        make_zone("storage1", "storage"),
        make_zone("storage2", "storage"),
        make_zone("storage3", "storage"),
        make_zone("cabin1", "cabin"),
    ]
    # 7 hops: cabin1->storage3->storage2->storage1->head->pantry->salon->cockpit
    passages = [
        make_passage("cabin1", "storage3"),
        make_passage("storage3", "storage2"),
        make_passage("storage2", "storage1"),
        make_passage("storage1", "head"),
        make_passage("head", "pantry"),
        make_passage("pantry", "salon"),
        make_passage("salon", "cockpit"),
    ]
    config = _default_config()  # max_escape_hops = 5
    score, warnings, metrics = analyze_escape_routes(zones, passages, config)
    assert score < 100.0
    assert any(w["severity"] == "warning" for w in warnings)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_compliance.py -v`
Expected: FAIL with `ModuleNotFoundError` or `ImportError`

- [ ] **Step 3: Implement scaffold and analyze_escape_routes**

```python
"""Compliance checker module for yacht layouts.

Automated check against maritime safety norms (ISO 9094, ISO 12217,
ISO 15085, ISO 10133). Pure function module — no database access.
"""
import logging
from collections import deque

logger = logging.getLogger(__name__)

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 4,
        "min_engine_clearance_mm": 500,
        "min_engine_area_sqm": 0.8,
        "min_electrical_area_sqm": 0.3,
        "required_railing_zones": ["foredeck", "cockpit"],
        "ce_category": "C",
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
        },
        "weights": {
            "escape_routes": 0.30,
            "fire_safety": 0.20,
            "stability": 0.15,
            "railing": 0.10,
            "electrical_access": 0.10,
            "ce_category": 0.15,
        },
    },
    "cruising_sail": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 5,
        "min_engine_clearance_mm": 600,
        "min_engine_area_sqm": 1.2,
        "min_electrical_area_sqm": 0.5,
        "required_railing_zones": ["foredeck", "cockpit"],
        "ce_category": "A",
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
        },
        "weights": {
            "escape_routes": 0.25,
            "fire_safety": 0.20,
            "stability": 0.20,
            "railing": 0.10,
            "electrical_access": 0.10,
            "ce_category": 0.15,
        },
    },
    "large_motor": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 6,
        "min_engine_clearance_mm": 800,
        "min_engine_area_sqm": 2.0,
        "min_electrical_area_sqm": 0.8,
        "required_railing_zones": ["foredeck", "cockpit", "flybridge", "swim_platform"],
        "ce_category": "A",
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
        },
        "weights": {
            "escape_routes": 0.25,
            "fire_safety": 0.25,
            "stability": 0.10,
            "railing": 0.15,
            "electrical_access": 0.10,
            "ce_category": 0.15,
        },
    },
    "superyacht": {
        "min_escape_width_mm": 600,
        "max_escape_hops": 8,
        "min_engine_clearance_mm": 1000,
        "min_engine_area_sqm": 4.0,
        "min_electrical_area_sqm": 1.5,
        "required_railing_zones": ["foredeck", "cockpit", "flybridge", "swim_platform"],
        "ce_category": "A",
        "norm_versions": {
            "ISO_9094": "2015",
            "ISO_12217": "2015",
            "ISO_15085": "2003",
            "ISO_10133": "2012",
            "ISO_13297": "2014",
        },
        "weights": {
            "escape_routes": 0.20,
            "fire_safety": 0.25,
            "stability": 0.10,
            "railing": 0.20,
            "electrical_access": 0.10,
            "ce_category": 0.15,
        },
    },
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}

_SLEEPING_ZONE_TYPES = {"cabin", "crew_quarters"}


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


def _centroid(polygon: list[list[float]]) -> tuple[float, float]:
    """Return centroid of polygon vertices."""
    n = len(polygon)
    if n == 0:
        return (0.0, 0.0)
    cx = sum(p[0] for p in polygon) / n
    cy = sum(p[1] for p in polygon) / n
    return (cx, cy)


def _build_adjacency(passages: list[dict]) -> dict[str, set[str]]:
    """Build bidirectional adjacency graph from passages."""
    graph: dict[str, set[str]] = {}
    for p in passages:
        a, b = p["from_zone"], p["to_zone"]
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    return graph


def _bfs_reachable(graph: dict[str, set[str]], start: str) -> set[str]:
    """Return all zones reachable from start via BFS."""
    if start not in graph:
        return {start}
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


def _bfs_path(graph: dict[str, set[str]], start: str, targets: set[str]) -> list[str] | None:
    """Return shortest path (zone name list) from start to any target, or None."""
    if start in targets:
        return [start]
    if start not in graph:
        return None
    visited = {start}
    queue: deque[tuple[str, list[str]]] = deque([(start, [start])])
    while queue:
        node, path = queue.popleft()
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                new_path = path + [neighbor]
                if neighbor in targets:
                    return new_path
                visited.add(neighbor)
                queue.append((neighbor, new_path))
    return None


def _widest_passage_between(passages: list[dict], zone_a: str, zone_b: str) -> float:
    """Return widest passage width between two zones, or 0 if none."""
    widths = []
    for p in passages:
        if (p["from_zone"] == zone_a and p["to_zone"] == zone_b) or \
           (p["from_zone"] == zone_b and p["to_zone"] == zone_a):
            widths.append(p["width_mm"])
    return max(widths) if widths else 0.0


def analyze_escape_routes(zones: list[dict], passages: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Check ISO 9094 escape routes: every sleeping zone must reach cockpit."""
    warnings: list[dict] = []
    min_width = config["min_escape_width_mm"]
    max_hops = config["max_escape_hops"]
    norm_ver = config["norm_versions"]["ISO_9094"]

    sleeping_zones = [z for z in zones if z["zone_type"] in _SLEEPING_ZONE_TYPES]
    cockpit_names = {z["name"] for z in zones if z["zone_type"] == "cockpit"}

    if not sleeping_zones:
        warnings.append({
            "severity": "info",
            "message": "Keine Schlafkabinen definiert — Fluchtwegeprüfung nicht anwendbar",
            "suggestion": "Kabinen zum Layout hinzufügen",
        })
        return 100.0, warnings, {"cabins_checked": 0, "cabins_compliant": 0, "cabins_total": 0}

    if not cockpit_names:
        warnings.append({
            "severity": "critical",
            "message": f"ISO 9094:{norm_ver} — Kein Cockpit definiert, Fluchtweg kann nicht bewertet werden",
            "suggestion": "Cockpit-Zone zum Layout hinzufügen",
        })
        return 0.0, warnings, {"cabins_checked": len(sleeping_zones), "cabins_compliant": 0, "cabins_total": len(sleeping_zones)}

    graph = _build_adjacency(passages)
    compliant = 0
    reachable_count = 0

    for sz in sleeping_zones:
        path = _bfs_path(graph, sz["name"], cockpit_names)

        if path is None:
            warnings.append({
                "severity": "critical",
                "message": f"ISO 9094:{norm_ver} §6.3 — Kabine '{sz['name']}' hat keinen Fluchtweg zum Cockpit",
                "suggestion": f"Fluchtweg von '{sz['name']}' zum Cockpit sicherstellen",
            })
            continue

        reachable_count += 1
        hops = len(path) - 1
        hop_ok = hops <= max_hops
        if not hop_ok:
            warnings.append({
                "severity": "warning",
                "message": f"ISO 9094:{norm_ver} — Fluchtweg von '{sz['name']}' zu lang ({hops} Durchgänge, max: {max_hops})",
                "suggestion": f"Direktere Verbindung von '{sz['name']}' zum Cockpit schaffen",
            })

        width_ok = True
        for i in range(len(path) - 1):
            width = _widest_passage_between(passages, path[i], path[i + 1])
            if width < min_width:
                width_ok = False
                warnings.append({
                    "severity": "critical",
                    "message": f"ISO 9094:{norm_ver} §6.3 — Fluchtweg {path[i]}→{path[i+1]} zu schmal ({width:.0f}mm, Minimum: {min_width:.0f}mm)",
                    "suggestion": f"Fluchtweg-Durchgang auf mindestens {min_width:.0f}mm erweitern",
                })

        if width_ok and hop_ok:
            compliant += 1

    total = len(sleeping_zones)
    if total == 0:
        score = 100.0
    else:
        # Fully compliant: 100 pts, reachable but noncompliant: 50 pts, unreachable: 0 pts
        noncompliant_reachable = reachable_count - compliant
        score = (compliant * 100.0 + noncompliant_reachable * 50.0) / total

    return score, warnings, {"cabins_checked": total, "cabins_compliant": compliant, "cabins_total": total}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. pytest tests/test_compliance.py -v`
Expected: All 5 escape route tests PASS

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/compliance.py backend/tests/test_compliance.py
git commit -m "feat: add compliance checker scaffold with escape route analysis"
```

---

### Task 2: analyze_fire_safety

**Files:**
- Modify: `backend/app/services/analysis/compliance.py`
- Modify: `backend/tests/test_compliance.py`

- [ ] **Step 1: Write failing tests for fire safety**

Add to `test_compliance.py`:

```python
from app.services.analysis.compliance import analyze_fire_safety


def test_fire_safety_good():
    """Engine far from living zones, accessible -> high score."""
    zones = [
        make_zone("engine", "engine", polygon=[[8000, 1000], [10000, 1000], [10000, 3000], [8000, 3000]]),
        make_zone("salon", "salon", polygon=[[0, 0], [4000, 0], [4000, 4000], [0, 4000]]),
    ]
    passages = [make_passage("salon", "engine")]
    config = _default_config()
    score, warnings, metrics = analyze_fire_safety(zones, passages, config)
    assert score >= 80.0
    assert metrics["engine_accessible"] is True


def test_fire_safety_no_engine():
    """No engine zone -> score 50, info."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_fire_safety(zones, [], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


def test_fire_safety_engine_too_close():
    """Engine centroid within min_engine_clearance_mm of living zone -> warning."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [500, 0], [500, 500], [0, 500]]),
        make_zone("cabin", "cabin", polygon=[[500, 0], [1000, 0], [1000, 500], [500, 500]]),
    ]
    passages = [make_passage("engine", "cabin")]
    config = _default_config()  # min_engine_clearance_mm = 600
    # Centroids: engine (250,250), cabin (750,250) -> dist = 500mm < 600mm
    score, warnings, metrics = analyze_fire_safety(zones, passages, config)
    assert score < 100.0
    assert any(w["severity"] == "warning" for w in warnings)
    assert metrics["min_clearance_mm"] < 600


def test_fire_safety_engine_inaccessible():
    """Engine not connected via passages -> critical."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("salon", "salon"),
    ]
    passages = []  # No passages at all
    config = _default_config()
    score, warnings, metrics = analyze_fire_safety(zones, passages, config)
    assert any(w["severity"] == "critical" for w in warnings)
    assert metrics["engine_accessible"] is False
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_compliance.py::test_fire_safety_good -v`
Expected: FAIL with `ImportError`

- [ ] **Step 3: Implement analyze_fire_safety**

Add to `compliance.py`:

```python
_LIVING_ZONE_TYPES = {"salon", "cabin", "pantry", "crew_quarters", "helm"}


def analyze_fire_safety(zones: list[dict], passages: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Check ISO 9094 fire safety: engine distance from living spaces, extinguisher access."""
    warnings: list[dict] = []
    min_clearance = config["min_engine_clearance_mm"]
    norm_ver = config["norm_versions"]["ISO_9094"]

    engine_zones = [z for z in zones if z["zone_type"] == "engine"]
    living_zones = [z for z in zones if z["zone_type"] in _LIVING_ZONE_TYPES]

    if not engine_zones:
        warnings.append({
            "severity": "info",
            "message": "Kein Maschinenraum definiert — Brandschutzprüfung eingeschränkt",
            "suggestion": "Maschinenraum-Zone (engine) zum Layout hinzufügen",
        })
        return 50.0, warnings, {"engine_zones": 0, "min_clearance_mm": 0.0, "engine_accessible": False}

    # Check clearance: minimum centroid distance between engine and living zones
    min_dist = float("inf")
    for ez in engine_zones:
        ec = _centroid(ez["polygon"])
        for lz in living_zones:
            lc = _centroid(lz["polygon"])
            dist = ((ec[0] - lc[0]) ** 2 + (ec[1] - lc[1]) ** 2) ** 0.5
            if dist < min_dist:
                min_dist = dist

    if min_dist == float("inf"):
        min_dist = 0.0

    clearance_score = 100.0
    if living_zones and min_dist < min_clearance:
        clearance_score = (min_dist / min_clearance) * 80.0 if min_clearance > 0 else 0.0
        warnings.append({
            "severity": "warning",
            "message": f"ISO 9094:{norm_ver} — Maschinenraum zu nah an Wohnbereich ({min_dist:.0f}mm, empfohlen: {min_clearance:.0f}mm)",
            "suggestion": f"Abstand zwischen Maschinenraum und Wohnbereich auf mindestens {min_clearance:.0f}mm erhöhen",
        })

    # Check engine accessibility (extinguisher access)
    graph = _build_adjacency(passages)
    engine_accessible = False
    for ez in engine_zones:
        reachable = _bfs_reachable(graph, ez["name"])
        if len(reachable) > 1:
            engine_accessible = True
            break

    access_score = 100.0
    if not engine_accessible:
        access_score = 0.0
        warnings.append({
            "severity": "critical",
            "message": f"ISO 9094:{norm_ver} — Maschinenraum nicht zugänglich (kein Feuerlöscher-Zugang)",
            "suggestion": "Durchgang zum Maschinenraum hinzufügen",
        })

    score = clearance_score * 0.5 + access_score * 0.5
    return score, warnings, {
        "engine_zones": len(engine_zones),
        "min_clearance_mm": round(min_dist, 0),
        "engine_accessible": engine_accessible,
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. pytest tests/test_compliance.py -v`
Expected: All tests PASS (escape route + fire safety)

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/compliance.py backend/tests/test_compliance.py
git commit -m "feat: add fire safety analysis to compliance module"
```

---

### Task 3: analyze_stability_impact

**Files:**
- Modify: `backend/app/services/analysis/compliance.py`
- Modify: `backend/tests/test_compliance.py`

- [ ] **Step 1: Write failing tests for stability**

Add to `test_compliance.py`:

```python
from app.services.analysis.compliance import analyze_stability_impact


def test_stability_centered():
    """Engine on centerline -> high score."""
    zones = [
        make_zone("engine", "engine", polygon=[[4000, 1000], [6000, 1000], [6000, 3000], [4000, 3000]]),
        make_zone("salon", "salon", polygon=[[0, 0], [4000, 0], [4000, 4000], [0, 4000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_stability_impact(zones, config)
    assert score >= 80.0
    assert metrics["y_deviation_ratio"] < 0.3


def test_stability_no_heavy_zones():
    """No engine/storage -> score 50, info."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_stability_impact(zones, config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


def test_stability_off_center():
    """Engine far from Y-centerline -> warning."""
    zones = [
        make_zone("engine", "engine", polygon=[[4000, 0], [6000, 0], [6000, 500], [4000, 500]]),
        make_zone("salon", "salon", polygon=[[0, 0], [4000, 0], [4000, 4000], [0, 4000]]),
    ]
    config = _default_config()
    # Layout Y range: 0-4000, center = 2000
    # Engine centroid Y = 250, deviation = |250-2000|/2000 = 0.875
    score, warnings, metrics = analyze_stability_impact(zones, config)
    assert score < 50.0
    assert any(w["severity"] == "warning" for w in warnings)
    assert metrics["y_deviation_ratio"] > 0.3
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_compliance.py::test_stability_centered -v`
Expected: FAIL with `ImportError`

- [ ] **Step 3: Implement analyze_stability_impact**

Add to `compliance.py`:

```python
_HEAVY_ZONE_TYPES = {"engine", "storage"}


def analyze_stability_impact(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Simplified ISO 12217 stability check: heavy zones should be centered on beam axis."""
    warnings: list[dict] = []
    norm_ver = config["norm_versions"]["ISO_12217"]

    heavy_zones = [z for z in zones if z["zone_type"] in _HEAVY_ZONE_TYPES]

    if not heavy_zones:
        warnings.append({
            "severity": "info",
            "message": "Keine schweren Zonen (Maschinenraum/Stauräume) definiert — Stabilitätsprüfung nicht möglich",
            "suggestion": "Maschinenraum und Stauräume zum Layout hinzufügen",
        })
        return 50.0, warnings, {"heavy_zones": 0, "y_deviation_ratio": 0.0}

    all_points = [p for z in zones for p in z["polygon"]]
    if not all_points:
        return 50.0, warnings, {"heavy_zones": len(heavy_zones), "y_deviation_ratio": 0.0}

    min_y = min(p[1] for p in all_points)
    max_y = max(p[1] for p in all_points)
    center_y = (min_y + max_y) / 2.0
    half_beam = (max_y - min_y) / 2.0

    if half_beam == 0:
        return 50.0, warnings, {"heavy_zones": len(heavy_zones), "y_deviation_ratio": 0.0}

    deviations = []
    for hz in heavy_zones:
        hc = _centroid(hz["polygon"])
        deviation = abs(hc[1] - center_y) / half_beam
        deviations.append(deviation)

    avg_deviation = sum(deviations) / len(deviations)

    if avg_deviation > 0.3:
        warnings.append({
            "severity": "warning",
            "message": f"ISO 12217:{norm_ver} — Schwere Zonen nicht zentriert (Abweichung: {avg_deviation:.0%})",
            "suggestion": "Maschinenraum und schwere Stauräume näher zur Mittschiffs-Achse platzieren",
        })

    score = max(0.0, (1.0 - avg_deviation) * 100.0)
    return score, warnings, {
        "heavy_zones": len(heavy_zones),
        "y_deviation_ratio": round(avg_deviation, 4),
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. pytest tests/test_compliance.py -v`
Expected: All tests PASS

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/compliance.py backend/tests/test_compliance.py
git commit -m "feat: add stability impact analysis to compliance module"
```

---

### Task 4: analyze_railing_requirements + analyze_electrical_access

**Files:**
- Modify: `backend/app/services/analysis/compliance.py`
- Modify: `backend/tests/test_compliance.py`

- [ ] **Step 1: Write failing tests for railing and electrical access**

Add to `test_compliance.py`:

```python
from app.services.analysis.compliance import (
    analyze_railing_requirements,
    analyze_electrical_access,
)


# --- Railing ---

def test_railing_compliant():
    """Cockpit with has_railing=True -> score 100."""
    zones = [
        make_zone("cockpit", "cockpit", properties={"has_railing": True}),
        make_zone("foredeck", "foredeck", properties={"has_railing": True}),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_railing_requirements(zones, config)
    assert score == 100.0
    assert metrics["zones_compliant"] == 2


def test_railing_no_deck_zones():
    """No exposed deck zones -> score 100."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_railing_requirements(zones, config)
    assert score == 100.0
    assert metrics["zones_checked"] == 0


def test_railing_violation():
    """Cockpit with has_railing=False -> critical."""
    zones = [
        make_zone("cockpit", "cockpit", properties={"has_railing": False}),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_railing_requirements(zones, config)
    assert score < 100.0
    assert any(w["severity"] == "critical" for w in warnings)


def test_railing_no_data():
    """Cockpit without has_railing property -> info warning, score 50."""
    zones = [make_zone("cockpit", "cockpit")]
    config = _default_config()
    score, warnings, metrics = analyze_railing_requirements(zones, config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


# --- Electrical Access ---

def test_electrical_good():
    """Engine zone adequate size and accessible -> high score."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
        make_zone("salon", "salon"),
    ]
    passages = [make_passage("engine", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_electrical_access(zones, passages, config)
    assert score >= 80.0
    assert metrics["accessible"] is True


def test_electrical_no_engine():
    """No engine zone -> score 50, info."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_electrical_access(zones, [], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


def test_electrical_too_small():
    """Engine zone below minimum area -> warning."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [500, 0], [500, 500], [0, 500]]),
        make_zone("salon", "salon"),
    ]
    passages = [make_passage("engine", "salon")]
    config = _default_config()  # min_electrical_area_sqm = 0.5
    # Engine area = 0.25 sqm < 0.5
    score, warnings, metrics = analyze_electrical_access(zones, passages, config)
    assert score < 100.0
    assert any(w["severity"] == "warning" for w in warnings)


def test_electrical_inaccessible():
    """Engine not connected via passages -> critical."""
    zones = [
        make_zone("engine", "engine", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
        make_zone("salon", "salon"),
    ]
    passages = []
    config = _default_config()
    score, warnings, metrics = analyze_electrical_access(zones, passages, config)
    assert any(w["severity"] == "critical" for w in warnings)
    assert metrics["accessible"] is False
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_compliance.py::test_railing_compliant -v`
Expected: FAIL with `ImportError`

- [ ] **Step 3: Implement analyze_railing_requirements and analyze_electrical_access**

Add to `compliance.py`:

```python
def analyze_railing_requirements(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Check ISO 15085 railing requirements for exposed deck zones."""
    warnings: list[dict] = []
    norm_ver = config["norm_versions"]["ISO_15085"]
    required_types = set(config.get("required_railing_zones", []))

    required_zones = [z for z in zones if z["zone_type"] in required_types]

    if not required_zones:
        return 100.0, warnings, {"zones_checked": 0, "zones_compliant": 0}

    compliant = 0
    violations = 0

    for z in required_zones:
        props = z.get("properties") or {}
        has_railing = props.get("has_railing")

        if has_railing is True:
            compliant += 1
        elif has_railing is False:
            violations += 1
            warnings.append({
                "severity": "critical",
                "message": f"ISO 15085:{norm_ver} — Zone '{z['name']}' benötigt Reling",
                "suggestion": f"Reling für Zone '{z['name']}' vorsehen",
            })
        else:
            warnings.append({
                "severity": "info",
                "message": f"ISO 15085:{norm_ver} — Reling-Status für '{z['name']}' nicht angegeben",
                "suggestion": f"has_railing in Zone-Eigenschaften für '{z['name']}' setzen",
            })

    total = len(required_zones)
    if violations > 0:
        score = max(0.0, (1.0 - violations / total) * 100.0)
    elif compliant == 0:
        score = 50.0  # No data at all
    else:
        score = 100.0

    return score, warnings, {
        "zones_checked": total,
        "zones_compliant": compliant,
    }


def analyze_electrical_access(zones: list[dict], passages: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Check ISO 10133 electrical compartment dimensions and accessibility."""
    warnings: list[dict] = []
    min_area = config["min_electrical_area_sqm"]
    norm_ver_10133 = config["norm_versions"]["ISO_10133"]
    norm_ver_13297 = config["norm_versions"]["ISO_13297"]
    norm_ref = f"ISO 10133:{norm_ver_10133}/13297:{norm_ver_13297}"

    engine_zones = [z for z in zones if z["zone_type"] == "engine"]

    if not engine_zones:
        warnings.append({
            "severity": "info",
            "message": f"{norm_ref} — Kein Maschinenraum definiert — Elektro-Zugang nicht prüfbar",
            "suggestion": "Maschinenraum-Zone zum Layout hinzufügen",
        })
        return 50.0, warnings, {"engine_area_sqm": 0.0, "accessible": False}

    total_area = sum(_polygon_area_sqm(ez["polygon"]) for ez in engine_zones)

    area_score = 100.0
    if total_area < min_area:
        ratio = total_area / min_area if min_area > 0 else 0.0
        area_score = ratio * 80.0
        warnings.append({
            "severity": "warning",
            "message": f"{norm_ref} — Maschinenraum zu klein ({total_area:.1f}m², empfohlen: {min_area:.1f}m²)",
            "suggestion": f"Maschinenraum auf mindestens {min_area:.1f}m² vergrößern",
        })

    graph = _build_adjacency(passages)
    accessible = False
    for ez in engine_zones:
        reachable = _bfs_reachable(graph, ez["name"])
        if len(reachable) > 1:
            accessible = True
            break

    access_score = 100.0
    if not accessible:
        access_score = 0.0
        warnings.append({
            "severity": "critical",
            "message": f"{norm_ref} — Elektro-/Maschinenraum nicht zugänglich",
            "suggestion": "Wartungszugang zum Maschinenraum sicherstellen",
        })

    score = area_score * 0.5 + access_score * 0.5
    return score, warnings, {
        "engine_area_sqm": round(total_area, 2),
        "accessible": accessible,
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. pytest tests/test_compliance.py -v`
Expected: All tests PASS

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/compliance.py backend/tests/test_compliance.py
git commit -m "feat: add railing and electrical access analyses to compliance module"
```

---

### Task 5: analyze_ce_category + orchestrator + route registration

**Files:**
- Modify: `backend/app/services/analysis/compliance.py`
- Modify: `backend/tests/test_compliance.py`
- Modify: `backend/app/api/routes/layouts.py:18-31`

- [ ] **Step 1: Write failing tests for CE category and integration**

Add to `test_compliance.py`:

```python
from app.services.analysis.compliance import (
    analyze_ce_category,
    run_compliance_analysis,
)


# --- CE Category ---

def test_ce_category_compliant():
    """All required zones present for CE category A -> score 100."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("engine", "engine"),
        make_zone("helm", "helm"),
        make_zone("cabin1", "cabin"),
        make_zone("head", "head"),
        make_zone("pantry", "pantry"),
    ]
    config = _default_config()  # ce_category = "A"
    score, warnings, metrics = analyze_ce_category(zones, config)
    assert score == 100.0
    assert len(metrics["missing_zones"]) == 0


def test_ce_category_missing_zones():
    """Missing required zones -> warnings."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("helm", "helm"),
    ]
    config = _default_config()  # ce_category = "A", requires 6 zone types
    score, warnings, metrics = analyze_ce_category(zones, config)
    assert score < 100.0
    assert len(warnings) > 0
    assert len(metrics["missing_zones"]) > 0


def test_ce_category_d_minimal():
    """Only helm -> score 100 for CE category D."""
    zones = [make_zone("helm", "helm")]
    config = _default_config("small_sail")
    config["ce_category"] = "D"  # Only needs helm
    score, warnings, metrics = analyze_ce_category(zones, config)
    assert score == 100.0


# --- Integration ---

def test_full_compliance_analysis():
    """Complete layout -> valid result structure with all 6 sub-scores."""
    zones = [
        make_zone("cockpit", "cockpit", properties={"has_railing": True}),
        make_zone("salon", "salon", polygon=[[3000, 0], [7000, 0], [7000, 4000], [3000, 4000]]),
        make_zone("cabin1", "cabin", polygon=[[0, 0], [3000, 0], [3000, 2000], [0, 2000]]),
        make_zone("engine", "engine", polygon=[[7000, 1000], [9000, 1000], [9000, 3000], [7000, 3000]]),
        make_zone("helm", "helm"),
        make_zone("head", "head"),
        make_zone("pantry", "pantry"),
    ]
    passages = [
        make_passage("cockpit", "salon"),
        make_passage("salon", "cabin1"),
        make_passage("salon", "engine"),
        make_passage("salon", "helm"),
        make_passage("salon", "head"),
        make_passage("salon", "pantry"),
    ]
    result = run_compliance_analysis(zones, passages, "cruising_sail")
    assert result["module"] == "compliance"
    assert 0 <= result["overall_score"] <= 100
    assert "escape_routes" in result["sub_scores"]
    assert "fire_safety" in result["sub_scores"]
    assert "stability" in result["sub_scores"]
    assert "railing" in result["sub_scores"]
    assert "electrical_access" in result["sub_scores"]
    assert "ce_category" in result["sub_scores"]
    assert len(result["sub_scores"]) == 6
    assert "norm_versions" in result["config_used"]


def test_compliance_warnings_sorted():
    """Warnings should be sorted: critical -> warning -> info."""
    zones = [
        make_zone("cabin1", "cabin"),  # No cockpit -> critical escape warning
        make_zone("engine", "engine", polygon=[[0, 0], [500, 0], [500, 500], [0, 500]]),  # Small engine
    ]
    result = run_compliance_analysis(zones, [], "cruising_sail")
    severities = [w["severity"] for w in result["warnings"]]
    order = [SEVERITY_ORDER.get(s, 2) for s in severities]
    assert order == sorted(order)


def test_compliance_boat_class_difference():
    """Different boat classes produce different scores."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("cabin1", "cabin"),
        make_zone("engine", "engine"),
        make_zone("helm", "helm"),
        make_zone("salon", "salon"),
    ]
    passages = [
        make_passage("cockpit", "salon"),
        make_passage("salon", "cabin1"),
        make_passage("salon", "engine"),
    ]
    result_small = run_compliance_analysis(zones, passages, "small_sail")
    result_super = run_compliance_analysis(zones, passages, "superyacht")
    assert result_small["overall_score"] != result_super["overall_score"]


def test_compliance_config_overrides():
    """Config overrides are applied and stored in config_used."""
    zones = [make_zone("cockpit", "cockpit"), make_zone("cabin1", "cabin")]
    passages = [make_passage("cockpit", "cabin1")]
    result = run_compliance_analysis(zones, passages, "cruising_sail",
                                     config_overrides={"max_escape_hops": 2})
    assert result["config_used"]["max_escape_hops"] == 2


def test_compliance_empty_input():
    """Empty zones and passages -> degraded scores, no crash."""
    result = run_compliance_analysis([], [], "cruising_sail")
    assert 0 <= result["overall_score"] <= 100
    assert len(result["sub_scores"]) == 6
    assert len(result["warnings"]) > 0
```

Also add the import for `SEVERITY_ORDER`:

```python
from app.services.analysis.compliance import (
    analyze_escape_routes,
    analyze_fire_safety,
    analyze_stability_impact,
    analyze_railing_requirements,
    analyze_electrical_access,
    analyze_ce_category,
    run_compliance_analysis,
    BOAT_CLASS_DEFAULTS,
    SEVERITY_ORDER,
)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_compliance.py::test_ce_category_compliant -v`
Expected: FAIL with `ImportError`

- [ ] **Step 3: Implement analyze_ce_category and run_compliance_analysis**

Add to `compliance.py`:

```python
_CE_REQUIRED_ZONES = {
    "A": {"cockpit", "engine", "helm", "cabin", "head", "pantry"},
    "B": {"cockpit", "engine", "helm", "cabin", "head"},
    "C": {"cockpit", "engine", "helm"},
    "D": {"helm"},
}

_CE_ZONE_LABELS = {
    "cockpit": "Cockpit",
    "engine": "Maschinenraum",
    "helm": "Steuerstand",
    "cabin": "Kabine",
    "head": "WC/Bad",
    "pantry": "Pantry",
}


def analyze_ce_category(zones: list[dict], config: dict) -> tuple[float, list[dict], dict]:
    """Check if layout supports the target CE category."""
    warnings: list[dict] = []
    target = config["ce_category"]

    required = _CE_REQUIRED_ZONES.get(target, set())
    zone_types_present = {z["zone_type"] for z in zones}

    missing = required - zone_types_present

    for m in sorted(missing):
        label = _CE_ZONE_LABELS.get(m, m)
        warnings.append({
            "severity": "warning",
            "message": f"CE-Kategorie {target} — Erforderliche Zone fehlt: {label}",
            "suggestion": f"{label} zum Layout hinzufügen für CE-Kategorie {target}",
        })

    present = required - missing
    score = (len(present) / len(required)) * 100.0 if required else 100.0

    return score, warnings, {
        "target_category": target,
        "required_zones": sorted(required),
        "missing_zones": sorted(missing),
    }


def run_compliance_analysis(zones: list[dict], passages: list[dict], boat_class: str, config_overrides: dict | None = None) -> dict:
    """Orchestrator — runs all compliance sub-analyses."""
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
        ("escape_routes", lambda: analyze_escape_routes(zones, passages, config)),
        ("fire_safety", lambda: analyze_fire_safety(zones, passages, config)),
        ("stability", lambda: analyze_stability_impact(zones, config)),
        ("railing", lambda: analyze_railing_requirements(zones, config)),
        ("electrical_access", lambda: analyze_electrical_access(zones, passages, config)),
        ("ce_category", lambda: analyze_ce_category(zones, config)),
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
        "module": "compliance",
        "overall_score": round(overall, 1),
        "sub_scores": {k: round(v, 1) for k, v in sub_scores.items()},
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
    }
```

- [ ] **Step 4: Register module in layouts.py**

Add import at top of `backend/app/api/routes/layouts.py`:

```python
from app.services.analysis.compliance import run_compliance_analysis
```

Add to `ANALYSIS_MODULES` dict:

```python
ANALYSIS_MODULES = {
    "ergonomics": run_ergonomics_analysis,
    "volume_storage": run_volume_storage_analysis,
    "emotional": run_emotional_analysis,
    "compliance": run_compliance_analysis,
}
```

- [ ] **Step 5: Run all tests to verify everything passes**

Run: `cd backend && PYTHONPATH=. pytest tests/ -v`
Expected: All tests PASS (71 existing + ~22 new compliance tests = ~93 total)

- [ ] **Step 6: Commit**

```bash
git add backend/app/services/analysis/compliance.py backend/tests/test_compliance.py backend/app/api/routes/layouts.py
git commit -m "feat: add CE category analysis, orchestrator, and register compliance module"
```
