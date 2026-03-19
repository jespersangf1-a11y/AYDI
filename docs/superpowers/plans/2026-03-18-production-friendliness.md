# Production Friendliness Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build Module 5 — a production friendliness analysis module that evaluates manufacturing efficiency of yacht layouts, detecting assembly bottlenecks, complex forms, service access issues, non-standard dimensions, and cable routing through guest spaces.

**Architecture:** Pure-function analysis module following the established AYDI pattern (BOAT_CLASS_DEFAULTS, 5 sub-analyses, orchestrator). Each sub-analysis returns `(score, warnings, metrics)`. The orchestrator combines them via boat-class-specific weighted sum. Module is registered in `layouts.py` ANALYSIS_MODULES dict.

**Tech Stack:** Python 3.12, math (angle computation), collections.deque (BFS), pytest

---

## File Structure

| File | Responsibility |
|---|---|
| `backend/app/services/analysis/production.py` | CREATE — BOAT_CLASS_DEFAULTS, 5 sub-analyses, orchestrator |
| `backend/tests/test_production.py` | CREATE — ~28 tests covering all sub-analyses + integration |
| `backend/app/api/routes/layouts.py` | MODIFY line 22 — add import + register in ANALYSIS_MODULES |

No changes to `conftest.py` — existing `make_zone()` and `make_passage()` helpers are sufficient.

---

## Design Decisions

### Sub-Analysis 1: Assembly Sequence (`analyze_assembly_sequence`)

Detects access-blocking installation order dependencies by finding **bottleneck zones** — zones whose removal disconnects other zones from the layout graph.

**Algorithm:** For each zone, temporarily remove it from the adjacency graph and BFS from any remaining node. If the remaining graph is disconnected, the zone is a bottleneck. O(V*(V+E)), acceptable for yacht layouts (<20 zones).

**Scoring:** `100 * (1 - bottleneck_count / total_zones)`. Warning per bottleneck zone.

### Sub-Analysis 2: Form Complexity (`analyze_form_complexity`)

Evaluates GFK (fiberglass) lamination difficulty by analyzing polygon vertex angles.

**Algorithm:** For each zone polygon, compute interior angles at each vertex. Count sharp angles (< `min_sharp_angle_deg`, default 30°) and reflex angles (> 180°, indicating concavities/undercuts).

**Scoring:** Per zone: `100 - sharp_count * 15 - reflex_count * 20`, clamped to [0, 100]. Overall: average of all zone scores.

### Sub-Analysis 3: Service Access Post-Build (`analyze_service_access`)

Checks that technical zones (engine, head) remain accessible with adequate passage width for maintenance.

**Algorithm:** For each technical zone, find widest connecting passage. Compare against `min_service_access_mm`.

**Scoring:** Per zone: wide enough = 100, exists but narrow = 50, no connection = 0. Average across technical zones.

### Sub-Analysis 4: Standardization (`analyze_standardization`)

Checks if key dimensions match standard module sizes (standard berth widths, door widths).

**Algorithm:** Check passage widths against standard door widths (with tolerance). Check cabin zone minimum Y-dimension against standard berth width. Score = 60% passage match ratio + 40% cabin match ratio.

### Sub-Analysis 5: Cable/Pipe Routing (`analyze_cable_routing`)

Evaluates whether logical system connections (engine↔helm, engine↔pantry, engine↔head) can be routed without crossing guest living spaces.

**Algorithm:** For each system pair, BFS path. Penalize each guest zone (salon, cabin) on the path. Score per connection: no guest crossings = 100, with crossings = `100 - 25 * guest_count` (min 0), no path = 0.

### BOAT_CLASS_DEFAULTS

```python
BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "min_sharp_angle_deg": 30,
        "min_service_access_mm": 500,
        "standard_door_widths_mm": [600],
        "standard_berth_width_mm": 700,
        "standardization_tolerance_mm": 50,
        "weights": {
            "assembly_sequence": 0.15,
            "form_complexity": 0.30,
            "service_access": 0.20,
            "standardization": 0.25,
            "cable_routing": 0.10,
        },
    },
    "cruising_sail": {
        "min_sharp_angle_deg": 30,
        "min_service_access_mm": 600,
        "standard_door_widths_mm": [600, 700],
        "standard_berth_width_mm": 700,
        "standardization_tolerance_mm": 50,
        "weights": {
            "assembly_sequence": 0.20,
            "form_complexity": 0.25,
            "service_access": 0.20,
            "standardization": 0.20,
            "cable_routing": 0.15,
        },
    },
    "large_motor": {
        "min_sharp_angle_deg": 35,
        "min_service_access_mm": 700,
        "standard_door_widths_mm": [600, 700, 800],
        "standard_berth_width_mm": 800,
        "standardization_tolerance_mm": 50,
        "weights": {
            "assembly_sequence": 0.25,
            "form_complexity": 0.15,
            "service_access": 0.25,
            "standardization": 0.15,
            "cable_routing": 0.20,
        },
    },
    "superyacht": {
        "min_sharp_angle_deg": 40,
        "min_service_access_mm": 800,
        "standard_door_widths_mm": [700, 800, 900],
        "standard_berth_width_mm": 900,
        "standardization_tolerance_mm": 75,
        "weights": {
            "assembly_sequence": 0.25,
            "form_complexity": 0.10,
            "service_access": 0.25,
            "standardization": 0.10,
            "cable_routing": 0.30,
        },
    },
}
```

Weight rationale:
- **small_sail**: Form complexity dominates (small workshop GFK), standardization important (cost-sensitive), cable routing least concern (simple systems)
- **cruising_sail**: Balanced, form complexity still significant, cable routing grows
- **large_motor**: Assembly sequence and service access dominate (complex builds), cable routing important (many systems)
- **superyacht**: Cable routing dominates (complex integrated systems, strict guest/crew separation), assembly and service access critical, form less relevant (custom molds)

---

### Task 1: BOAT_CLASS_DEFAULTS, helpers, and analyze_assembly_sequence

**Files:**
- Create: `backend/app/services/analysis/production.py`
- Create: `backend/tests/test_production.py`

- [ ] **Step 1: Write failing tests for analyze_assembly_sequence**

```python
"""Tests for production friendliness analysis module."""
from tests.conftest import make_passage, make_zone
from app.services.analysis.production import (
    analyze_assembly_sequence,
    BOAT_CLASS_DEFAULTS,
)


def _default_config(boat_class="cruising_sail"):
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


# ---------------------------------------------------------------------------
# analyze_assembly_sequence
# ---------------------------------------------------------------------------


def test_assembly_no_bottlenecks():
    """Ring topology (every zone has 2+ connections) -> score 100."""
    zones = [
        make_zone("salon", "salon"),
        make_zone("cockpit", "cockpit"),
        make_zone("engine", "engine"),
    ]
    passages = [
        make_passage("salon", "cockpit"),
        make_passage("cockpit", "engine"),
        make_passage("engine", "salon"),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_assembly_sequence(zones, passages, config)
    assert score == 100.0
    assert metrics["bottleneck_count"] == 0


def test_assembly_one_bottleneck():
    """Linear chain: middle zone is bottleneck -> score < 100."""
    zones = [
        make_zone("cabin", "cabin"),
        make_zone("salon", "salon"),
        make_zone("cockpit", "cockpit"),
    ]
    passages = [
        make_passage("cabin", "salon"),
        make_passage("salon", "cockpit"),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_assembly_sequence(zones, passages, config)
    assert score < 100.0
    assert metrics["bottleneck_count"] >= 1
    assert any(w["severity"] == "warning" for w in warnings)


def test_assembly_all_isolated():
    """No passages -> all zones isolated, score 0."""
    zones = [
        make_zone("cabin", "cabin"),
        make_zone("salon", "salon"),
        make_zone("cockpit", "cockpit"),
    ]
    passages = []
    config = _default_config()
    score, warnings, metrics = analyze_assembly_sequence(zones, passages, config)
    assert score == 0.0
    assert any(w["severity"] == "critical" for w in warnings)


def test_assembly_no_zones():
    """No zones -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_assembly_sequence([], [], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


def test_assembly_single_zone():
    """Single zone, no bottlenecks possible -> score 100."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_assembly_sequence(zones, [], config)
    assert score == 100.0
    assert metrics["bottleneck_count"] == 0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_production.py -v`
Expected: FAIL — module `production` does not exist

- [ ] **Step 3: Write BOAT_CLASS_DEFAULTS, helpers, and analyze_assembly_sequence**

```python
"""Production friendliness analysis module for yacht layouts.

Evaluates manufacturing efficiency: assembly sequence, form complexity,
service access, standardization, and cable/pipe routing.
Pure function module — no database access.
All user-facing strings are in German.
"""
import logging
import math
from collections import deque

logger = logging.getLogger(__name__)

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "min_sharp_angle_deg": 30,
        "min_service_access_mm": 500,
        "standard_door_widths_mm": [600],
        "standard_berth_width_mm": 700,
        "standardization_tolerance_mm": 50,
        "weights": {
            "assembly_sequence": 0.15,
            "form_complexity": 0.30,
            "service_access": 0.20,
            "standardization": 0.25,
            "cable_routing": 0.10,
        },
    },
    "cruising_sail": {
        "min_sharp_angle_deg": 30,
        "min_service_access_mm": 600,
        "standard_door_widths_mm": [600, 700],
        "standard_berth_width_mm": 700,
        "standardization_tolerance_mm": 50,
        "weights": {
            "assembly_sequence": 0.20,
            "form_complexity": 0.25,
            "service_access": 0.20,
            "standardization": 0.20,
            "cable_routing": 0.15,
        },
    },
    "large_motor": {
        "min_sharp_angle_deg": 35,
        "min_service_access_mm": 700,
        "standard_door_widths_mm": [600, 700, 800],
        "standard_berth_width_mm": 800,
        "standardization_tolerance_mm": 50,
        "weights": {
            "assembly_sequence": 0.25,
            "form_complexity": 0.15,
            "service_access": 0.25,
            "standardization": 0.15,
            "cable_routing": 0.20,
        },
    },
    "superyacht": {
        "min_sharp_angle_deg": 40,
        "min_service_access_mm": 800,
        "standard_door_widths_mm": [700, 800, 900],
        "standard_berth_width_mm": 900,
        "standardization_tolerance_mm": 75,
        "weights": {
            "assembly_sequence": 0.25,
            "form_complexity": 0.10,
            "service_access": 0.25,
            "standardization": 0.10,
            "cable_routing": 0.30,
        },
    },
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}

_TECHNICAL_ZONE_TYPES = {"engine", "head"}

_GUEST_ZONE_TYPES = {"salon", "cabin"}

_SYSTEM_CONNECTIONS = [
    ("engine", "helm"),
    ("engine", "pantry"),
    ("engine", "head"),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _build_adjacency(passages: list[dict]) -> dict[str, set[str]]:
    """Build undirected adjacency graph from passages."""
    graph: dict[str, set[str]] = {}
    for p in passages:
        a, b = p["from_zone"], p["to_zone"]
        graph.setdefault(a, set()).add(b)
        graph.setdefault(b, set()).add(a)
    return graph


def _bfs_reachable(graph: dict[str, set[str]], start: str) -> set[str]:
    """Return all nodes reachable from start via BFS."""
    visited = {start}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, set()):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return visited


def _bfs_path(
    graph: dict[str, set[str]], start: str, targets: set[str],
) -> list[str] | None:
    """BFS shortest path from start to any node in targets. Returns path list or None."""
    if start in targets:
        return [start]
    visited = {start}
    queue = deque([(start, [start])])
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


def _is_graph_connected(graph: dict[str, set[str]], all_nodes: set[str]) -> bool:
    """Check if all_nodes are connected in graph."""
    if not all_nodes:
        return True
    start = next(iter(all_nodes))
    reachable = set()
    queue = deque([start])
    reachable.add(start)
    while queue:
        node = queue.popleft()
        for neighbor in graph.get(node, set()):
            if neighbor in all_nodes and neighbor not in reachable:
                reachable.add(neighbor)
                queue.append(neighbor)
    return reachable == all_nodes


def _polygon_min_dimension(polygon: list[list[float]]) -> float:
    """Return the minimum bounding-box dimension (width or height) of a polygon in mm."""
    if len(polygon) < 3:
        return 0.0
    xs = [p[0] for p in polygon]
    ys = [p[1] for p in polygon]
    width = max(xs) - min(xs)
    height = max(ys) - min(ys)
    return min(width, height)


def _vertex_angles(polygon: list[list[float]]) -> list[tuple[float, bool]]:
    """Compute interior angles for each vertex of a CCW polygon.

    Returns list of (angle_degrees, is_reflex).
    For CCW polygons, a negative cross product indicates a reflex (concave) vertex.
    """
    n = len(polygon)
    if n < 3:
        return []
    results = []
    for i in range(n):
        p_prev = polygon[(i - 1) % n]
        p_curr = polygon[i]
        p_next = polygon[(i + 1) % n]

        ax = p_prev[0] - p_curr[0]
        ay = p_prev[1] - p_curr[1]
        bx = p_next[0] - p_curr[0]
        by = p_next[1] - p_curr[1]

        cross = ax * by - ay * bx
        dot = ax * bx + ay * by

        angle_rad = math.atan2(abs(cross), dot)
        angle_deg = math.degrees(angle_rad)

        # For CCW polygon, cross > 0 means reflex vertex (interior angle > 180)
        is_reflex = cross > 0
        if is_reflex:
            angle_deg = 360.0 - angle_deg

        results.append((angle_deg, is_reflex))
    return results


# ---------------------------------------------------------------------------
# Sub-analysis: Assembly sequence
# ---------------------------------------------------------------------------


def analyze_assembly_sequence(
    zones: list[dict],
    passages: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Detect access-blocking installation order dependencies.

    Finds bottleneck zones whose removal disconnects the layout graph,
    indicating constrained assembly sequences.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "code": "MONTAGE_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen für Montagereihenfolge-Analyse vorhanden.",
            "suggestion": "Zonen zum Layout hinzufügen.",
        })
        return 50.0, warnings, {"bottleneck_count": 0, "bottleneck_zones": [], "total_zones": 0}

    zone_names = {z["name"] for z in zones}

    if len(zone_names) <= 1:
        return 100.0, warnings, {"bottleneck_count": 0, "bottleneck_zones": [], "total_zones": len(zone_names)}

    graph = _build_adjacency(passages)

    # Check overall connectivity first
    all_in_graph = zone_names & (set(graph.keys()) | {n for neighbors in graph.values() for n in neighbors})
    disconnected = zone_names - all_in_graph
    if len(all_in_graph) <= 1 and len(zone_names) > 1:
        warnings.append({
            "code": "MONTAGE_NO_CONNECTIONS",
            "severity": "critical",
            "message": "Keine Durchgänge definiert — Montagereihenfolge kann nicht analysiert werden.",
            "suggestion": "Durchgänge zwischen Zonen definieren.",
        })
        return 0.0, warnings, {"bottleneck_count": 0, "bottleneck_zones": [], "total_zones": len(zone_names)}

    # Find bottleneck zones (articulation points via brute-force removal)
    bottlenecks = []
    for zone_name in sorted(zone_names):
        remaining = zone_names - {zone_name}
        # Build subgraph without this zone
        sub_graph: dict[str, set[str]] = {}
        for z in remaining:
            sub_graph[z] = {n for n in graph.get(z, set()) if n in remaining}
        # Check if remaining connected nodes are still connected
        connected_remaining = remaining & (set(sub_graph.keys()) | {n for neighbors in sub_graph.values() for n in neighbors})
        if connected_remaining and not _is_graph_connected(sub_graph, connected_remaining):
            bottlenecks.append(zone_name)

    for bn in bottlenecks:
        warnings.append({
            "code": "MONTAGE_BOTTLENECK",
            "severity": "warning",
            "message": f"Zone '{bn}' ist ein Montage-Engpass — Entfernung trennt andere Zonen ab.",
            "suggestion": f"Alternativen Zugang um Zone '{bn}' herum schaffen, um Montagereihenfolge zu flexibilisieren.",
        })

    ratio = len(bottlenecks) / len(zone_names)
    score = max(0.0, 100.0 * (1.0 - ratio))

    return score, warnings, {
        "bottleneck_count": len(bottlenecks),
        "bottleneck_zones": bottlenecks,
        "total_zones": len(zone_names),
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. pytest tests/test_production.py -v`
Expected: 5 PASS

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/production.py backend/tests/test_production.py
git commit -m "feat: add production module — BOAT_CLASS_DEFAULTS and assembly sequence analysis"
```

---

### Task 2: analyze_form_complexity

**Files:**
- Modify: `backend/app/services/analysis/production.py`
- Modify: `backend/tests/test_production.py`

- [ ] **Step 1: Write failing tests for analyze_form_complexity**

Append to `test_production.py`:

```python
from app.services.analysis.production import analyze_form_complexity


# ---------------------------------------------------------------------------
# analyze_form_complexity
# ---------------------------------------------------------------------------


def test_form_all_right_angles():
    """Rectangle zones (all 90° angles) -> score 100."""
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [4000, 0], [4000, 3000], [0, 3000]]),
        make_zone("cabin", "cabin", polygon=[[0, 0], [2000, 0], [2000, 2000], [0, 2000]]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_form_complexity(zones, config)
    assert score == 100.0
    assert metrics["sharp_angle_count"] == 0
    assert metrics["reflex_angle_count"] == 0


def test_form_sharp_angles():
    """Triangle with a sharp angle (< 30°) -> score < 100."""
    # Triangle with angles approx 10°, 80°, 90° — sharp vertex at origin
    zones = [
        make_zone("salon", "salon", polygon=[[0, 0], [5000, 0], [5000, 900]]),
    ]
    config = _default_config()  # min_sharp_angle_deg = 30
    score, warnings, metrics = analyze_form_complexity(zones, config)
    assert score < 100.0
    assert metrics["sharp_angle_count"] >= 1
    assert any(w["severity"] == "warning" for w in warnings)


def test_form_reflex_angle():
    """L-shaped polygon with a reflex angle -> score < 100."""
    # L-shape: has one reflex (concave) vertex
    zones = [
        make_zone("salon", "salon", polygon=[
            [0, 0], [3000, 0], [3000, 1000],
            [1000, 1000], [1000, 3000], [0, 3000],
        ]),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_form_complexity(zones, config)
    assert score < 100.0
    assert metrics["reflex_angle_count"] == 1
    assert any(w["severity"] == "warning" for w in warnings)


def test_form_no_zones():
    """No zones -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_form_complexity([], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
```

- [ ] **Step 2: Run tests to verify new tests fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_production.py::test_form_all_right_angles -v`
Expected: FAIL — `analyze_form_complexity` not defined

- [ ] **Step 3: Implement analyze_form_complexity**

Add to `production.py`:

```python
# ---------------------------------------------------------------------------
# Sub-analysis: Form complexity
# ---------------------------------------------------------------------------


def analyze_form_complexity(
    zones: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Evaluate GFK lamination difficulty from polygon geometry.

    Sharp angles (< min_sharp_angle_deg) and reflex angles (> 180°, concavities)
    increase lamination complexity and mold difficulty.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "code": "FORM_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen für Formkomplexitäts-Analyse vorhanden.",
            "suggestion": "Zonen zum Layout hinzufügen.",
        })
        return 50.0, warnings, {"sharp_angle_count": 0, "reflex_angle_count": 0, "zones_analyzed": 0}

    min_angle = config.get("min_sharp_angle_deg", 30)
    total_sharp = 0
    total_reflex = 0
    zone_scores = []

    for zone in zones:
        polygon = zone.get("polygon", [])
        if len(polygon) < 3:
            zone_scores.append(100.0)
            continue

        angles = _vertex_angles(polygon)
        sharp = sum(1 for deg, reflex in angles if not reflex and deg < min_angle)
        reflex = sum(1 for _, is_reflex in angles if is_reflex)

        total_sharp += sharp
        total_reflex += reflex

        zone_score = max(0.0, 100.0 - sharp * 15.0 - reflex * 20.0)
        zone_scores.append(zone_score)

    if total_sharp > 0:
        warnings.append({
            "code": "FORM_SHARP_ANGLE",
            "severity": "warning",
            "message": (
                f"{total_sharp} spitze Winkel (< {min_angle}°) erschweren "
                f"GFK-Laminierung und Formenbau."
            ),
            "suggestion": "Spitze Ecken abrunden oder Winkel vergrößern.",
        })

    if total_reflex > 0:
        warnings.append({
            "code": "FORM_UNDERCUT",
            "severity": "warning",
            "message": (
                f"{total_reflex} konkave Ecken (Hinterschneidungen) "
                f"erschweren Entformung und Laminierung."
            ),
            "suggestion": "Konkave Formen vermeiden oder in separate Bauteile aufteilen.",
        })

    score = sum(zone_scores) / len(zone_scores) if zone_scores else 50.0

    return score, warnings, {
        "sharp_angle_count": total_sharp,
        "reflex_angle_count": total_reflex,
        "zones_analyzed": len(zone_scores),
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. pytest tests/test_production.py -v`
Expected: 9 PASS (5 assembly + 4 form)

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/production.py backend/tests/test_production.py
git commit -m "feat: add form complexity sub-analysis to production module"
```

---

### Task 3: analyze_service_access and analyze_standardization

**Files:**
- Modify: `backend/app/services/analysis/production.py`
- Modify: `backend/tests/test_production.py`

- [ ] **Step 1: Write failing tests for analyze_service_access**

Append to `test_production.py`:

```python
from app.services.analysis.production import analyze_service_access


# ---------------------------------------------------------------------------
# analyze_service_access
# ---------------------------------------------------------------------------


def test_service_access_good():
    """Technical zones connected via wide passages -> high score."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("salon", "salon"),
        make_zone("head", "head"),
    ]
    passages = [
        make_passage("engine", "salon", width_mm=800),
        make_passage("head", "salon", width_mm=800),
    ]
    config = _default_config()  # min_service_access_mm = 600
    score, warnings, metrics = analyze_service_access(zones, passages, config)
    assert score >= 80.0
    assert metrics["accessible_count"] == 2


def test_service_access_narrow():
    """Technical zone connected but narrow passage -> partial score."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("salon", "salon"),
    ]
    passages = [make_passage("engine", "salon", width_mm=400)]
    config = _default_config()  # min_service_access_mm = 600
    score, warnings, metrics = analyze_service_access(zones, passages, config)
    assert score == 50.0
    assert any(w["severity"] == "warning" for w in warnings)


def test_service_access_inaccessible():
    """Technical zone with no passages -> critical, score 0."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("salon", "salon"),
    ]
    passages = []
    config = _default_config()
    score, warnings, metrics = analyze_service_access(zones, passages, config)
    assert score == 0.0
    assert any(w["severity"] == "critical" for w in warnings)
    assert metrics["accessible_count"] == 0


def test_service_access_no_technical():
    """No technical zones -> score 50, info."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_service_access(zones, [], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
```

- [ ] **Step 2: Write failing tests for analyze_standardization**

Append to `test_production.py`:

```python
from app.services.analysis.production import analyze_standardization


# ---------------------------------------------------------------------------
# analyze_standardization
# ---------------------------------------------------------------------------


def test_standardization_all_standard():
    """All passages and cabins match standard sizes -> score 100."""
    zones = [
        make_zone("cabin1", "cabin", polygon=[[0, 0], [2000, 0], [2000, 700], [0, 700]]),
    ]
    passages = [
        make_passage("cabin1", "salon", width_mm=600),
    ]
    config = _default_config()  # standard_door_widths_mm=[600,700], berth=700, tolerance=50
    score, warnings, metrics = analyze_standardization(zones, passages, config)
    assert score == 100.0
    assert metrics["passage_match_ratio"] == 1.0


def test_standardization_non_standard_passage():
    """Passage with non-standard width -> lower score."""
    zones = [
        make_zone("cabin1", "cabin", polygon=[[0, 0], [2000, 0], [2000, 700], [0, 700]]),
    ]
    passages = [
        make_passage("cabin1", "salon", width_mm=450),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_standardization(zones, passages, config)
    assert score < 100.0
    assert any(w["severity"] == "warning" for w in warnings)


def test_standardization_non_standard_berth():
    """Cabin with non-standard berth width -> lower score."""
    zones = [
        make_zone("cabin1", "cabin", polygon=[[0, 0], [2000, 0], [2000, 500], [0, 500]]),
    ]
    passages = [
        make_passage("cabin1", "salon", width_mm=600),
    ]
    config = _default_config()  # standard_berth_width_mm = 700, tolerance = 50
    # Min dimension = 500, standard = 700, tolerance = 50 -> not matching
    score, warnings, metrics = analyze_standardization(zones, passages, config)
    assert score < 100.0
    assert any(w["severity"] == "warning" for w in warnings)


def test_standardization_no_data():
    """No passages and no cabins -> score 50, info."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_standardization(zones, [], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
```

- [ ] **Step 3: Run tests to verify new tests fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_production.py::test_service_access_good -v`
Expected: FAIL — `analyze_service_access` not defined

- [ ] **Step 4: Implement analyze_service_access**

Add to `production.py`:

```python
# ---------------------------------------------------------------------------
# Sub-analysis: Service access post-build
# ---------------------------------------------------------------------------


def analyze_service_access(
    zones: list[dict],
    passages: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check that technical zones remain accessible for maintenance.

    Technical zones (engine, head) need passage connections wide enough
    for service personnel and tools.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    tech_zones = [z for z in zones if z["zone_type"] in _TECHNICAL_ZONE_TYPES]

    if not tech_zones:
        warnings.append({
            "code": "SERVICE_NO_TECH_ZONES",
            "severity": "info",
            "message": "Keine technischen Zonen (Maschine, Nasszelle) für Service-Zugangs-Analyse vorhanden.",
            "suggestion": "Technische Zonen zum Layout hinzufügen.",
        })
        return 50.0, warnings, {"accessible_count": 0, "narrow_count": 0, "total_technical": 0}

    min_width = config.get("min_service_access_mm", 600)
    zone_scores = []
    accessible_count = 0
    narrow_count = 0

    for tz in tech_zones:
        tz_name = tz["name"]
        # Find widest passage connected to this zone
        widest = 0.0
        connected = False
        for p in passages:
            if p["from_zone"] == tz_name or p["to_zone"] == tz_name:
                connected = True
                widest = max(widest, p.get("width_mm", 0))

        if not connected:
            zone_scores.append(0.0)
            warnings.append({
                "code": "SERVICE_INACCESSIBLE",
                "severity": "critical",
                "message": f"Technische Zone '{tz_name}' hat keinen Durchgang — Service nach Einbau nicht möglich.",
                "suggestion": f"Servicezugang zu '{tz_name}' über mindestens einen Durchgang sicherstellen.",
            })
        elif widest < min_width:
            zone_scores.append(50.0)
            narrow_count += 1
            accessible_count += 1
            warnings.append({
                "code": "SERVICE_NARROW",
                "severity": "warning",
                "message": (
                    f"Servicezugang zu '{tz_name}': {widest:.0f} mm < Minimum {min_width} mm — "
                    f"Wartung erschwert."
                ),
                "suggestion": f"Durchgang zu '{tz_name}' auf mindestens {min_width} mm verbreitern.",
            })
        else:
            zone_scores.append(100.0)
            accessible_count += 1

    score = sum(zone_scores) / len(zone_scores) if zone_scores else 50.0

    return score, warnings, {
        "accessible_count": accessible_count,
        "narrow_count": narrow_count,
        "total_technical": len(tech_zones),
    }
```

- [ ] **Step 5: Implement analyze_standardization**

Add to `production.py`:

```python
# ---------------------------------------------------------------------------
# Sub-analysis: Standardization
# ---------------------------------------------------------------------------


def analyze_standardization(
    zones: list[dict],
    passages: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check if key dimensions match standard module sizes.

    Standard door widths and berth widths reduce manufacturing cost and allow
    use of prefabricated components.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    standard_doors = config.get("standard_door_widths_mm", [600, 700])
    standard_berth = config.get("standard_berth_width_mm", 700)
    tolerance = config.get("standardization_tolerance_mm", 50)

    cabin_zones = [z for z in zones if z["zone_type"] == "cabin"]
    has_passages = len(passages) > 0
    has_cabins = len(cabin_zones) > 0

    if not has_passages and not has_cabins:
        warnings.append({
            "code": "STANDARD_NO_DATA",
            "severity": "info",
            "message": "Keine Durchgänge oder Kabinen für Standardisierungs-Analyse vorhanden.",
            "suggestion": "Durchgänge und Kabinen zum Layout hinzufügen.",
        })
        return 50.0, warnings, {
            "passage_match_ratio": 0.0,
            "cabin_match_ratio": 0.0,
            "non_standard_passages": 0,
            "non_standard_cabins": 0,
        }

    # --- Passage width standardization ---
    passage_matches = 0
    non_standard_passages = 0
    for p in passages:
        w = p.get("width_mm", 0)
        if any(abs(w - std) <= tolerance for std in standard_doors):
            passage_matches += 1
        else:
            non_standard_passages += 1

    passage_ratio = passage_matches / len(passages) if passages else 0.0

    if non_standard_passages > 0:
        std_str = ", ".join(f"{s} mm" for s in standard_doors)
        warnings.append({
            "code": "STANDARD_PASSAGE_NONSTANDARD",
            "severity": "warning",
            "message": (
                f"{non_standard_passages} Durchgang/Durchgänge mit nicht-standardisierten Breiten "
                f"(Standard: {std_str}, Toleranz ±{tolerance} mm)."
            ),
            "suggestion": "Durchgangsbreiten an Standardmaße anpassen für günstigere Fertigung.",
        })

    # --- Cabin berth standardization ---
    cabin_matches = 0
    non_standard_cabins = 0
    for cz in cabin_zones:
        polygon = cz.get("polygon", [])
        min_dim = _polygon_min_dimension(polygon)
        if abs(min_dim - standard_berth) <= tolerance:
            cabin_matches += 1
        else:
            non_standard_cabins += 1

    cabin_ratio = cabin_matches / len(cabin_zones) if cabin_zones else 0.0

    if non_standard_cabins > 0:
        warnings.append({
            "code": "STANDARD_BERTH_NONSTANDARD",
            "severity": "warning",
            "message": (
                f"{non_standard_cabins} Kabine(n) mit nicht-standardisierter Kojenbreite "
                f"(Standard: {standard_berth} mm, Toleranz ±{tolerance} mm)."
            ),
            "suggestion": f"Kojenbreite auf Standard {standard_berth} mm anpassen.",
        })

    # Combined score: 60% passages, 40% cabins
    if has_passages and has_cabins:
        score = passage_ratio * 60.0 + cabin_ratio * 40.0
    elif has_passages:
        score = passage_ratio * 100.0
    else:
        score = cabin_ratio * 100.0

    return score, warnings, {
        "passage_match_ratio": round(passage_ratio, 2),
        "cabin_match_ratio": round(cabin_ratio, 2),
        "non_standard_passages": non_standard_passages,
        "non_standard_cabins": non_standard_cabins,
    }
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. pytest tests/test_production.py -v`
Expected: 17 PASS (5 assembly + 4 form + 4 service + 4 standardization)

- [ ] **Step 7: Commit**

```bash
git add backend/app/services/analysis/production.py backend/tests/test_production.py
git commit -m "feat: add service access and standardization sub-analyses to production module"
```

---

### Task 4: analyze_cable_routing

**Files:**
- Modify: `backend/app/services/analysis/production.py`
- Modify: `backend/tests/test_production.py`

- [ ] **Step 1: Write failing tests for analyze_cable_routing**

Append to `test_production.py`:

```python
from app.services.analysis.production import analyze_cable_routing


# ---------------------------------------------------------------------------
# analyze_cable_routing
# ---------------------------------------------------------------------------


def test_cable_routing_clean():
    """All system connections route through technical/crew zones -> score 100."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("helm", "helm"),
        make_zone("pantry", "pantry"),
        make_zone("head", "head"),
        make_zone("storage", "storage"),
    ]
    passages = [
        make_passage("engine", "storage"),
        make_passage("storage", "helm"),
        make_passage("storage", "pantry"),
        make_passage("storage", "head"),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_cable_routing(zones, passages, config)
    assert score == 100.0
    assert metrics["guest_crossings"] == 0


def test_cable_routing_through_guest():
    """System connection routes through salon (guest zone) -> lower score."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("salon", "salon"),
        make_zone("helm", "helm"),
        make_zone("pantry", "pantry"),
        make_zone("head", "head"),
    ]
    passages = [
        make_passage("engine", "salon"),
        make_passage("salon", "helm"),
        make_passage("salon", "pantry"),
        make_passage("salon", "head"),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_cable_routing(zones, passages, config)
    assert score < 100.0
    assert metrics["guest_crossings"] > 0
    assert any(w["severity"] == "warning" for w in warnings)


def test_cable_routing_no_path():
    """System zones not connected -> critical, score 0."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("helm", "helm"),
    ]
    passages = []
    config = _default_config()
    score, warnings, metrics = analyze_cable_routing(zones, passages, config)
    assert score < 50.0
    assert any(w["severity"] == "critical" for w in warnings)


def test_cable_routing_no_system_zones():
    """No system zones present -> score 50, info."""
    zones = [make_zone("salon", "salon")]
    config = _default_config()
    score, warnings, metrics = analyze_cable_routing(zones, [], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_production.py::test_cable_routing_clean -v`
Expected: FAIL — `analyze_cable_routing` not defined

- [ ] **Step 3: Implement analyze_cable_routing**

Add to `production.py`:

```python
# ---------------------------------------------------------------------------
# Sub-analysis: Cable/pipe routing
# ---------------------------------------------------------------------------


def analyze_cable_routing(
    zones: list[dict],
    passages: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Evaluate cable/pipe routing paths between connected systems.

    Checks if logical system connections (engine↔helm, engine↔pantry,
    engine↔head) can be routed without crossing guest living spaces.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    zone_type_map = {z["name"]: z["zone_type"] for z in zones}
    present_types = {z["zone_type"] for z in zones}

    # Find applicable system connections
    applicable = []
    for src_type, dst_type in _SYSTEM_CONNECTIONS:
        if src_type in present_types and dst_type in present_types:
            applicable.append((src_type, dst_type))

    if not applicable:
        warnings.append({
            "code": "CABLE_NO_SYSTEMS",
            "severity": "info",
            "message": "Keine Systemverbindungen (Maschine↔Helm, Maschine↔Pantry, Maschine↔Nasszelle) zu prüfen.",
            "suggestion": "Technische Zonen zum Layout hinzufügen.",
        })
        return 50.0, warnings, {"connections_checked": 0, "guest_crossings": 0, "missing_paths": 0}

    graph = _build_adjacency(passages)
    connection_scores = []
    total_guest_crossings = 0
    missing_paths = 0

    for src_type, dst_type in applicable:
        # Find zone names of each type
        src_names = {z["name"] for z in zones if z["zone_type"] == src_type}
        dst_names = {z["name"] for z in zones if z["zone_type"] == dst_type}

        best_score = None
        best_guest_count = 0

        for src_name in src_names:
            path = _bfs_path(graph, src_name, dst_names)
            if path is not None:
                # Count guest zones on path (excluding start and end)
                intermediate = path[1:-1] if len(path) > 2 else []
                guest_count = sum(
                    1 for node in intermediate
                    if zone_type_map.get(node) in _GUEST_ZONE_TYPES
                )
                path_score = max(0.0, 100.0 - guest_count * 25.0)
                if best_score is None or path_score > best_score:
                    best_score = path_score
                    best_guest_count = guest_count

        if best_score is None:
            connection_scores.append(0.0)
            missing_paths += 1
            warnings.append({
                "code": "CABLE_PATH_MISSING",
                "severity": "critical",
                "message": (
                    f"Kein Leitungsweg zwischen {src_type.capitalize()} und "
                    f"{dst_type.capitalize()} vorhanden."
                ),
                "suggestion": f"Durchgänge zwischen {src_type.capitalize()} und {dst_type.capitalize()} schaffen.",
            })
        else:
            connection_scores.append(best_score)
            total_guest_crossings += best_guest_count
            if best_guest_count > 0:
                warnings.append({
                    "code": "CABLE_GUEST_CROSSING",
                    "severity": "warning",
                    "message": (
                        f"Leitungsweg {src_type.capitalize()}↔{dst_type.capitalize()} "
                        f"kreuzt {best_guest_count} Gastzonen — Wartung stört Gäste."
                    ),
                    "suggestion": (
                        f"Alternativen Kabelweg über technische Zonen oder Crew-Bereiche schaffen."
                    ),
                })

    score = sum(connection_scores) / len(connection_scores) if connection_scores else 50.0

    return score, warnings, {
        "connections_checked": len(applicable),
        "guest_crossings": total_guest_crossings,
        "missing_paths": missing_paths,
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. pytest tests/test_production.py -v`
Expected: 21 PASS (5 + 4 + 4 + 4 + 4)

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/production.py backend/tests/test_production.py
git commit -m "feat: add cable routing sub-analysis to production module"
```

---

### Task 5: Orchestrator, integration tests, and route registration

**Files:**
- Modify: `backend/app/services/analysis/production.py`
- Modify: `backend/tests/test_production.py`
- Modify: `backend/app/api/routes/layouts.py` (line 22)

- [ ] **Step 1: Write failing integration tests**

Append to `test_production.py`:

```python
from app.services.analysis.production import run_production_analysis, SEVERITY_ORDER


# ---------------------------------------------------------------------------
# Integration
# ---------------------------------------------------------------------------


def test_full_production_analysis():
    """Complete layout -> valid result structure with all 5 sub-scores."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("salon", "salon", polygon=[[3000, 0], [7000, 0], [7000, 4000], [3000, 4000]]),
        make_zone("cabin1", "cabin", polygon=[[0, 0], [2000, 0], [2000, 700], [0, 700]]),
        make_zone("engine", "engine", polygon=[[7000, 1000], [9000, 1000], [9000, 3000], [7000, 3000]]),
        make_zone("helm", "helm"),
        make_zone("head", "head"),
        make_zone("pantry", "pantry"),
    ]
    passages = [
        make_passage("cockpit", "salon", width_mm=700),
        make_passage("salon", "cabin1", width_mm=600),
        make_passage("salon", "engine", width_mm=700),
        make_passage("salon", "helm", width_mm=600),
        make_passage("salon", "head", width_mm=600),
        make_passage("salon", "pantry", width_mm=600),
    ]
    result = run_production_analysis(zones, passages, "cruising_sail")
    assert result["module"] == "production"
    assert 0 <= result["overall_score"] <= 100
    assert "assembly_sequence" in result["sub_scores"]
    assert "form_complexity" in result["sub_scores"]
    assert "service_access" in result["sub_scores"]
    assert "standardization" in result["sub_scores"]
    assert "cable_routing" in result["sub_scores"]
    assert len(result["sub_scores"]) == 5


def test_production_warnings_sorted():
    """Warnings should be sorted: critical -> warning -> info."""
    zones = [
        make_zone("engine", "engine"),
        make_zone("helm", "helm"),
    ]
    result = run_production_analysis(zones, [], "cruising_sail")
    severities = [w["severity"] for w in result["warnings"]]
    order = [SEVERITY_ORDER.get(s, 2) for s in severities]
    assert order == sorted(order)


def test_production_boat_class_difference():
    """Different boat classes produce different scores."""
    zones = [
        make_zone("cockpit", "cockpit"),
        make_zone("salon", "salon"),
        make_zone("engine", "engine"),
        make_zone("helm", "helm"),
        make_zone("head", "head"),
        make_zone("cabin1", "cabin", polygon=[[0, 0], [2000, 0], [2000, 700], [0, 700]]),
    ]
    passages = [
        make_passage("cockpit", "salon", width_mm=600),
        make_passage("salon", "engine", width_mm=600),
        make_passage("salon", "helm", width_mm=600),
        make_passage("salon", "head", width_mm=600),
        make_passage("salon", "cabin1", width_mm=600),
    ]
    result_small = run_production_analysis(zones, passages, "small_sail")
    result_super = run_production_analysis(zones, passages, "superyacht")
    assert result_small["overall_score"] != result_super["overall_score"]


def test_production_config_overrides():
    """Config overrides are applied and stored in config_used."""
    zones = [make_zone("cockpit", "cockpit"), make_zone("cabin1", "cabin")]
    passages = [make_passage("cockpit", "cabin1")]
    result = run_production_analysis(zones, passages, "cruising_sail",
                                     config_overrides={"min_service_access_mm": 900})
    assert result["config_used"]["min_service_access_mm"] == 900


def test_production_empty_input():
    """Empty zones and passages -> degraded scores, no crash."""
    result = run_production_analysis([], [], "cruising_sail")
    assert 0 <= result["overall_score"] <= 100
    assert len(result["sub_scores"]) == 5
    assert len(result["warnings"]) > 0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_production.py::test_full_production_analysis -v`
Expected: FAIL — `run_production_analysis` not defined

- [ ] **Step 3: Implement orchestrator**

Add to `production.py`:

```python
# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


def run_production_analysis(
    zones: list[dict],
    passages: list[dict],
    boat_class: str,
    config_overrides: dict | None = None,
) -> dict:
    """Orchestrator — runs all production friendliness sub-analyses.

    Returns a standardized result dict matching the AYDI analysis module contract.
    """
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

    analyses: list[tuple[str, object]] = [
        ("assembly_sequence", lambda: analyze_assembly_sequence(zones, passages, config)),
        ("form_complexity", lambda: analyze_form_complexity(zones, config)),
        ("service_access", lambda: analyze_service_access(zones, passages, config)),
        ("standardization", lambda: analyze_standardization(zones, passages, config)),
        ("cable_routing", lambda: analyze_cable_routing(zones, passages, config)),
    ]

    for name, fn in analyses:
        try:
            score, warnings, metrics = fn()
            sub_scores[name] = score
            all_warnings.extend(warnings)
            all_metrics[name] = metrics
        except Exception:
            logger.exception("Error in production sub-analysis %s", name)
            sub_scores[name] = 0.0
            all_warnings.append({
                "code": "ANALYSIS_ERROR",
                "severity": "critical",
                "message": f"Fehler bei Produktionsanalyse: {name}",
                "suggestion": "Layoutdaten überprüfen.",
            })

    overall = sum(sub_scores.get(k, 50.0) * w for k, w in weights.items())

    for w in all_warnings:
        suggestion = w.get("suggestion")
        if suggestion and suggestion not in all_suggestions:
            all_suggestions.append(suggestion)

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    return {
        "module": "production",
        "overall_score": round(overall, 1),
        "sub_scores": {k: round(v, 1) for k, v in sub_scores.items()},
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
    }
```

- [ ] **Step 4: Register module in layouts.py**

In `backend/app/api/routes/layouts.py`, add import on line 22:

```python
from app.services.analysis.production import run_production_analysis
```

And update `ANALYSIS_MODULES` dict to include:

```python
ANALYSIS_MODULES = {
    "ergonomics": run_ergonomics_analysis,
    "volume_storage": run_volume_storage_analysis,
    "emotional": run_emotional_analysis,
    "compliance": run_compliance_analysis,
    "production": run_production_analysis,
}
```

- [ ] **Step 5: Run all tests to verify everything passes**

Run: `cd backend && PYTHONPATH=. pytest tests/ -v`
Expected: All tests pass (ergonomics: 19, volume_storage: 20, emotional: 24+, dxf_parser: 8, compliance: 29, production: 26)

- [ ] **Step 6: Commit**

```bash
git add backend/app/services/analysis/production.py backend/tests/test_production.py backend/app/api/routes/layouts.py
git commit -m "feat: add production friendliness orchestrator and register module"
```

---

## Test Summary

| Sub-analysis | Tests | Coverage |
|---|---|---|
| assembly_sequence | 5 | no bottlenecks, one bottleneck, all isolated, no zones, single zone |
| form_complexity | 4 | all right angles, sharp angles, reflex angles, no zones |
| service_access | 4 | good access, narrow, inaccessible, no technical zones |
| standardization | 4 | all standard, non-standard passage, non-standard berth, no data |
| cable_routing | 4 | clean routes, through guest, no paths, no system zones |
| integration | 5 | full layout, warnings sorted, boat class diff, config overrides, empty input |
| **Total** | **26** | |
