# Community Intelligence Phase 1 Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add a Community Intelligence system that surfaces real-world owner experiences as actionable findings in AYDI's analysis pipeline — data models, pattern aggregation, relevance engine, standalone analysis module, API endpoints, and orchestrator integration.

**Architecture:** Two new DB models (CommunityReport, CommunityPattern) store owner experience data. A CommunityPatternAggregator batch-processes reports into patterns (≥3 reports = pattern). A CommunityKnowledgeEngine queries patterns with 5-level relevance matching. A standalone `community` analysis module (pure function) scores findings. The orchestrator runs it in Tier 1. API endpoints provide CRUD + aggregation + relevance queries.

**Tech Stack:** Python 3.12, FastAPI, SQLAlchemy 2.0, Pydantic v2, pytest

**Spec:** `docs/superpowers/specs/2026-03-19-community-intelligence-design.md`

---

### Task 1: Database Models

**Files:**
- Modify: `backend/app/models/models.py`

- [ ] **Step 1: Write CommunityReport and CommunityPattern models**

Add after the existing `ImageUpload` model (end of file):

```python
class CommunityReport(Base):
    """Individual experience report from forum post or owner feedback."""
    __tablename__ = "community_reports"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    source_forum = Column(String(100), nullable=False)
    source_url = Column(String(500), nullable=True)
    source_date = Column(Date, nullable=True)
    boat_manufacturer = Column(String(100), nullable=False)
    boat_model = Column(String(100), nullable=True)
    boat_year = Column(Integer, nullable=True)
    hull_material = Column(String(50), nullable=True)
    hull_construction = Column(String(50), nullable=True)
    propulsion = Column(String(20), nullable=True)
    issues = Column(JSON, nullable=False, default=list)
    positives = Column(JSON, default=list)
    reliability = Column(Float, nullable=False)
    raw_text = Column(Text, nullable=True)

    __table_args__ = (
        Index("ix_community_reports_manufacturer_model", "boat_manufacturer", "boat_model"),
        Index("ix_community_reports_hull", "hull_material", "hull_construction"),
    )


class CommunityPattern(Base):
    """Aggregated pattern derived from ≥3 independent reports."""
    __tablename__ = "community_patterns"

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    manufacturer = Column(String(100), nullable=True)
    boat_model = Column(String(100), nullable=True)
    issue_category = Column(String(50), nullable=False)
    zone_type = Column(String(50), nullable=True)
    description = Column(String(500), nullable=False)
    report_count = Column(Integer, nullable=False)
    severity_mode = Column(String(20), nullable=False)
    typical_onset_years = Column(Float, nullable=True)
    materials_involved = Column(JSON, nullable=True)
    construction_methods_involved = Column(JSON, nullable=True)
    confidence = Column(Float, nullable=False)
    source_report_ids = Column(JSON, nullable=False)
    is_positive = Column(Boolean, nullable=False, default=False)

    __table_args__ = (
        Index("ix_community_patterns_manufacturer_model", "manufacturer", "boat_model"),
        Index("ix_community_patterns_category", "issue_category"),
        Index("ix_community_patterns_zone", "zone_type"),
    )
```

Add these imports at the top of the file if not already present: `Date`, `Text`, `Boolean`, `Index`.

- [ ] **Step 2: Verify the app starts and tables are created**

Run: `cd backend && PYTHONPATH=. python -c "from app.models.models import CommunityReport, CommunityPattern; print('Models imported OK')"`
Expected: `Models imported OK`

- [ ] **Step 3: Commit**

```bash
git add backend/app/models/models.py
git commit -m "feat: add CommunityReport and CommunityPattern database models"
```

---

### Task 2: Pydantic Schemas & Test Factories

**Files:**
- Modify: `backend/app/schemas/schemas.py`
- Modify: `backend/tests/conftest.py`

- [ ] **Step 1: Add Pydantic schemas**

Add to `backend/app/schemas/schemas.py`:

```python
class CommunityIssue(BaseModel):
    category: str
    zone_type: str
    description: str
    severity: str
    boat_age_months: int | None = None


class CommunityPositive(BaseModel):
    category: str
    zone_type: str
    description: str


class CommunityReportCreate(BaseModel):
    source_forum: str
    source_url: str | None = None
    source_date: date | None = None
    boat_manufacturer: str
    boat_model: str | None = None
    boat_year: int | None = None
    hull_material: str | None = None
    hull_construction: str | None = None
    propulsion: str | None = None
    issues: list[CommunityIssue] = []
    positives: list[CommunityPositive] = []
    reliability: float
    raw_text: str | None = None


class CommunityReportResponse(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime | None = None
    source_forum: str
    source_url: str | None = None
    source_date: date | None = None
    boat_manufacturer: str
    boat_model: str | None = None
    boat_year: int | None = None
    hull_material: str | None = None
    hull_construction: str | None = None
    propulsion: str | None = None
    issues: list[dict] = []
    positives: list[dict] = []
    reliability: float
    raw_text: str | None = None
    model_config = ConfigDict(from_attributes=True)


class CommunityPatternResponse(BaseModel):
    id: int
    created_at: datetime
    manufacturer: str | None = None
    boat_model: str | None = None
    issue_category: str
    zone_type: str | None = None
    description: str
    report_count: int
    severity_mode: str
    typical_onset_years: float | None = None
    materials_involved: list[str] | None = None
    construction_methods_involved: list[str] | None = None
    confidence: float
    source_report_ids: list[int]
    is_positive: bool
    model_config = ConfigDict(from_attributes=True)


class AggregationResultResponse(BaseModel):
    patterns_created: int
    reports_processed: int
    reports_skipped: int
    groups_below_threshold: int
```

Add `date` to the imports at the top: `from datetime import datetime, date`.

- [ ] **Step 2: Add test factory functions**

Add to `backend/tests/conftest.py`:

```python
def make_community_report(
    source_forum="boote-forum.de",
    boat_manufacturer="Bavaria",
    boat_model="38 Cruiser",
    boat_year=2018,
    hull_material="grp_solid",
    hull_construction="hand_layup",
    propulsion="sail",
    issues=None,
    positives=None,
    reliability=0.8,
    source_url=None,
    source_date=None,
    raw_text=None,
):
    if issues is None:
        issues = [{
            "category": "material_degradation",
            "zone_type": "hull",
            "description": "Osmoseblasen am Unterwasserschiff nach 6 Jahren",
            "severity": "major",
            "boat_age_months": 72,
        }]
    return {
        "source_forum": source_forum,
        "source_url": source_url,
        "source_date": source_date,
        "boat_manufacturer": boat_manufacturer,
        "boat_model": boat_model,
        "boat_year": boat_year,
        "hull_material": hull_material,
        "hull_construction": hull_construction,
        "propulsion": propulsion,
        "issues": issues,
        "positives": positives or [],
        "reliability": reliability,
        "raw_text": raw_text,
    }


def make_community_pattern(
    manufacturer="Bavaria",
    boat_model="38 Cruiser",
    issue_category="material_degradation",
    zone_type="hull",
    description="Osmoseblasen am Unterwasserschiff",
    report_count=5,
    severity_mode="major",
    typical_onset_years=6.0,
    materials_involved=None,
    construction_methods_involved=None,
    confidence=0.7,
    source_report_ids=None,
    is_positive=False,
):
    return {
        "manufacturer": manufacturer,
        "boat_model": boat_model,
        "issue_category": issue_category,
        "zone_type": zone_type,
        "description": description,
        "report_count": report_count,
        "severity_mode": severity_mode,
        "typical_onset_years": typical_onset_years,
        "materials_involved": materials_involved or ["grp_solid"],
        "construction_methods_involved": construction_methods_involved or ["hand_layup"],
        "confidence": confidence,
        "source_report_ids": source_report_ids or [1, 2, 3, 4, 5],
        "is_positive": is_positive,
    }
```

- [ ] **Step 3: Verify imports work**

Run: `cd backend && PYTHONPATH=. python -c "from app.schemas.schemas import CommunityReportCreate, CommunityPatternResponse, AggregationResultResponse; print('Schemas OK')"`
Expected: `Schemas OK`

- [ ] **Step 4: Commit**

```bash
git add backend/app/schemas/schemas.py backend/tests/conftest.py
git commit -m "feat: add community Pydantic schemas and test factories"
```

---

### Task 3: Community Analysis Module

**Files:**
- Create: `backend/app/services/analysis/community.py`
- Create: `backend/tests/test_community_analysis.py`

- [ ] **Step 1: Write failing tests**

Create `backend/tests/test_community_analysis.py`:

```python
"""Tests for Community Intelligence analysis module."""
import pytest


# === Fixtures ===

def _make_pattern(
    severity="major",
    relevance=0.8,
    confidence=0.7,
    report_count=5,
    category="material_degradation",
    zone_type="hull",
    description="Osmoseblasen am Unterwasserschiff",
    typical_onset_years=6.0,
    is_positive=False,
    match_reason="manufacturer",
):
    return {
        "pattern_id": 1,
        "relevance": relevance,
        "category": category,
        "zone_type": zone_type,
        "description": description,
        "report_count": report_count,
        "severity": severity,
        "typical_onset_years": typical_onset_years,
        "materials_involved": ["grp_solid"],
        "confidence": confidence,
        "match_reason": match_reason,
        "is_positive": is_positive,
    }


def _make_positive(**kwargs):
    defaults = {
        "severity": "positive",
        "is_positive": True,
        "description": "Kielstruktur direkt laminiert",
        "category": "structural",
    }
    defaults.update(kwargs)
    return _make_pattern(**defaults)


def _zones():
    return [{"name": "salon", "zone_type": "salon"}]


def _passages():
    return [{"from_zone": "salon", "to_zone": "cockpit", "width_mm": 700}]


# === Skip logic ===

class TestSkipLogic:
    def test_no_patterns_returns_unavailable(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=[])
        assert result["available"] is False
        assert "Keine Community-Daten" in result["reason"]

    def test_none_patterns_returns_unavailable(self):
        from app.services.analysis.community import run_community_analysis
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=None)
        assert result["available"] is False


# === Known issues scoring ===

class TestKnownIssuesScoring:
    def test_critical_pattern_reduces_score_heavily(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern(severity="critical", relevance=1.0, confidence=1.0)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        assert result["available"] is True
        score = result["sub_scores"]["known_issues"]["score"]
        assert score < 80  # critical with full relevance+confidence should reduce significantly

    def test_minor_pattern_reduces_score_slightly(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern(severity="minor", relevance=0.5, confidence=0.5)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        score = result["sub_scores"]["known_issues"]["score"]
        assert score > 90  # minor with low relevance should barely affect

    def test_multiple_patterns_accumulate(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [
            _make_pattern(severity="major", relevance=0.8, confidence=0.7),
            _make_pattern(severity="major", relevance=0.6, confidence=0.6, zone_type="deck",
                          description="Teakfugen undicht"),
        ]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        score = result["sub_scores"]["known_issues"]["score"]
        # Two major patterns should reduce more than one
        single = [patterns[0]]
        single_result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=single)
        assert score < single_result["sub_scores"]["known_issues"]["score"]

    def test_score_floors_at_zero(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern(severity="critical", relevance=1.0, confidence=1.0) for _ in range(10)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        score = result["sub_scores"]["known_issues"]["score"]
        assert score >= 0


# === Positive reputation scoring ===

class TestPositiveReputationScoring:
    def test_no_positives_returns_neutral(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern()]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        assert result["sub_scores"]["positive_reputation"]["score"] == 50

    def test_positives_increase_score(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_positive(relevance=1.0, confidence=0.9)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        assert result["sub_scores"]["positive_reputation"]["score"] > 50

    def test_positive_score_caps_at_100(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_positive(relevance=1.0, confidence=1.0) for _ in range(20)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        assert result["sub_scores"]["positive_reputation"]["score"] <= 100


# === Data coverage scoring ===

class TestDataCoverageScoring:
    def test_few_patterns_low_coverage(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern()]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        score = result["sub_scores"]["data_coverage"]["score"]
        assert score < 20  # 1 out of 20 max_patterns

    def test_many_patterns_high_coverage(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern(zone_type=f"zone_{i}") for i in range(20)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        score = result["sub_scores"]["data_coverage"]["score"]
        assert score == 100


# === Overall score ===

class TestOverallScore:
    def test_overall_is_weighted_combination(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern(), _make_positive()]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        ki = result["sub_scores"]["known_issues"]["score"]
        pr = result["sub_scores"]["positive_reputation"]["score"]
        dc = result["sub_scores"]["data_coverage"]["score"]
        expected = ki * 0.50 + pr * 0.30 + dc * 0.20
        assert abs(result["overall_score"] - expected) < 0.1


# === Warnings and suggestions ===

class TestWarningsAndSuggestions:
    def test_critical_pattern_generates_warning(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern(severity="critical", confidence=0.5)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        assert len(result["warnings"]) == 1
        w = result["warnings"][0]
        assert w["code"] == "COMMUNITY_KNOWN_ISSUE"
        assert w["severity"] == "critical"
        assert "COMMUNITY:" in w["message"]
        assert "Berichte" in w["message"]

    def test_major_pattern_generates_warning(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern(severity="major", confidence=0.5)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        assert len(result["warnings"]) == 1
        assert result["warnings"][0]["severity"] == "warning"

    def test_minor_pattern_no_warning(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern(severity="minor", confidence=0.5)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        assert len(result["warnings"]) == 0

    def test_low_confidence_filtered(self):
        from app.services.analysis.community import run_community_analysis
        # cruising_sail min_confidence is 0.3
        patterns = [_make_pattern(severity="critical", confidence=0.2)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        assert len(result["warnings"]) == 0

    def test_each_warning_has_suggestion(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern(severity="critical", confidence=0.5)]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        assert len(result["suggestions"]) == len(result["warnings"])
        s = result["suggestions"][0]
        assert s["code"] == "COMMUNITY_CHECK_RECOMMENDATION"
        assert "sorgfältig" in s["message"]


# === Config overrides ===

class TestConfigOverrides:
    def test_custom_min_confidence(self):
        from app.services.analysis.community import run_community_analysis
        # Pattern at confidence 0.35 — default min is 0.3 (pass), override to 0.5 (fail)
        patterns = [_make_pattern(severity="critical", confidence=0.35)]
        result = run_community_analysis(
            _zones(), _passages(), "cruising_sail",
            config_overrides={"min_confidence": 0.5},
            community_patterns=patterns,
        )
        assert len(result["warnings"]) == 0


# === Metrics ===

class TestMetrics:
    def test_metrics_present(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern(), _make_positive()]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        m = result["metrics"]
        assert m["total_patterns_found"] == 2
        assert m["negative_patterns"] == 1
        assert m["positive_patterns"] == 1
        assert "most_common_category" in m
        assert "earliest_typical_onset_years" in m


# === Return format ===

class TestReturnFormat:
    def test_standard_module_return(self):
        from app.services.analysis.community import run_community_analysis
        patterns = [_make_pattern()]
        result = run_community_analysis(_zones(), _passages(), "cruising_sail", community_patterns=patterns)
        assert result["module"] == "community"
        assert result["available"] is True
        assert "overall_score" in result
        assert "sub_scores" in result
        assert "warnings" in result
        assert "suggestions" in result
        assert "metrics" in result
        assert result["confidence"] == "documented"
        assert "config_used" in result
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_community_analysis.py -v`
Expected: FAIL (module not found)

- [ ] **Step 3: Implement the community analysis module**

Create `backend/app/services/analysis/community.py`:

```python
"""Community Intelligence analysis module.

Scores community-reported patterns (forum experiences, owner feedback)
for a specific boat. Pure function, no DB access.
"""
from collections import Counter


BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "max_patterns": 15,
        "min_confidence": 0.4,
        "severity_weights": {"critical": 25, "major": 15, "minor": 5, "cosmetic": 2},
    },
    "cruising_sail": {
        "max_patterns": 20,
        "min_confidence": 0.3,
        "severity_weights": {"critical": 25, "major": 15, "minor": 5, "cosmetic": 2},
    },
    "large_motor": {
        "max_patterns": 20,
        "min_confidence": 0.3,
        "severity_weights": {"critical": 25, "major": 15, "minor": 5, "cosmetic": 2},
    },
    "superyacht": {
        "max_patterns": 25,
        "min_confidence": 0.2,
        "severity_weights": {"critical": 25, "major": 15, "minor": 5, "cosmetic": 2},
    },
}

ZONE_LABELS = {
    "hull": "den Rumpfbereich",
    "deck": "das Deck",
    "cockpit": "das Cockpit",
    "galley": "die Pantry",
    "head": "den Nassbereich",
    "cabin": "die Kabine",
    "engine_room": "den Motorraum",
    "bilge": "die Bilge",
    "rigging": "das Rigg",
    "salon": "den Salon",
    "helm": "den Steuerstand",
}


def run_community_analysis(
    zones: list[dict],
    passages: list[dict],
    boat_class: str = "cruising_sail",
    config_overrides: dict | None = None,
    *,
    community_patterns: list[dict] | None = None,
) -> dict:
    """Analyze community knowledge patterns for this boat.

    Args:
        zones: Layout zones (standard parameter, not used directly).
        passages: Layout passages (standard parameter, not used directly).
        boat_class: Boat class for default config lookup.
        config_overrides: Optional config overrides from BoatDNA resolver.
        community_patterns: List of pattern dicts from CommunityKnowledgeEngine.

    Returns:
        Standard analysis module result dict.
    """
    if not community_patterns:
        return {"available": False, "reason": "Keine Community-Daten verfügbar."}

    # Build config
    defaults = BOAT_CLASS_DEFAULTS.get(boat_class, BOAT_CLASS_DEFAULTS["cruising_sail"]).copy()
    if config_overrides:
        defaults.update(config_overrides)
    config = defaults

    max_patterns = config["max_patterns"]
    min_confidence = config["min_confidence"]
    severity_weights = config["severity_weights"]

    # Split patterns
    negative = [p for p in community_patterns if not p.get("is_positive", False)]
    positive = [p for p in community_patterns if p.get("is_positive", False)]

    # --- Sub-scores ---

    # Known issues score: start at 100, subtract per negative pattern
    known_issues_score = 100.0
    for p in negative:
        weight = severity_weights.get(p.get("severity", "minor"), 5)
        relevance = p.get("relevance", 0.5)
        confidence = p.get("confidence", 0.5)
        known_issues_score -= weight * relevance * confidence
    known_issues_score = max(0.0, known_issues_score)

    # Positive reputation score: start at 50 (neutral), add per positive
    positive_reputation_score = 50.0
    for p in positive:
        relevance = p.get("relevance", 0.5)
        confidence = p.get("confidence", 0.5)
        positive_reputation_score += 10 * relevance * confidence
    positive_reputation_score = min(100.0, positive_reputation_score)

    # Data coverage score
    total_count = len(community_patterns)
    data_coverage_score = min(100.0, total_count / max_patterns * 100)

    # --- Overall score ---
    overall_score = (
        known_issues_score * 0.50
        + positive_reputation_score * 0.30
        + data_coverage_score * 0.20
    )

    # --- Warnings (critical/major patterns above min_confidence) ---
    warnings = []
    for p in negative:
        if p.get("severity") not in ("critical", "major"):
            continue
        if p.get("confidence", 0) < min_confidence:
            continue
        warnings.append({
            "code": "COMMUNITY_KNOWN_ISSUE",
            "severity": "critical" if p["severity"] == "critical" else "warning",
            "zone": p.get("zone_type"),
            "message": (
                f"COMMUNITY: {p['description']} "
                f"({p.get('report_count', 0)} Berichte)"
            ),
            "source": "community",
            "confidence": "documented",
        })

    # --- Suggestions (one per warning) ---
    suggestions = []
    for i, w in enumerate(warnings):
        p = [p for p in negative
             if p.get("severity") in ("critical", "major")
             and p.get("confidence", 0) >= min_confidence][i]
        zone_label = ZONE_LABELS.get(p.get("zone_type", ""), p.get("zone_type", "diesen Bereich"))
        onset = p.get("typical_onset_years")
        onset_text = f" (typisch nach {onset:.0f} Jahren)" if onset else ""
        suggestions.append({
            "code": "COMMUNITY_CHECK_RECOMMENDATION",
            "zone": p.get("zone_type"),
            "message": (
                f"Prüfen Sie {zone_label} besonders sorgfältig — "
                f"bekanntes Problem bei vergleichbaren Booten{onset_text}."
            ),
            "priority": "high" if p["severity"] == "critical" else "medium",
            "source": "community",
        })

    # --- Metrics ---
    categories = [p.get("category", "unknown") for p in community_patterns]
    category_counts = Counter(categories)
    most_common = category_counts.most_common(1)[0][0] if category_counts else None

    onset_values = [p["typical_onset_years"] for p in negative if p.get("typical_onset_years") is not None]
    earliest_onset = min(onset_values) if onset_values else None

    return {
        "module": "community",
        "available": True,
        "overall_score": round(overall_score, 1),
        "sub_scores": {
            "known_issues": {
                "score": round(known_issues_score, 1),
                "label": "Bekannte Probleme",
                "details": [
                    {"description": p["description"], "severity": p.get("severity"),
                     "relevance": p.get("relevance"), "report_count": p.get("report_count")}
                    for p in negative
                ],
            },
            "positive_reputation": {
                "score": round(positive_reputation_score, 1),
                "label": "Positive Erfahrungen",
                "details": [
                    {"description": p["description"], "relevance": p.get("relevance"),
                     "report_count": p.get("report_count")}
                    for p in positive
                ],
            },
            "data_coverage": {
                "score": round(data_coverage_score, 1),
                "label": "Datenabdeckung",
                "details": {"total_patterns": total_count, "max_patterns": max_patterns},
            },
        },
        "warnings": warnings,
        "suggestions": suggestions,
        "metrics": {
            "total_patterns_found": total_count,
            "negative_patterns": len(negative),
            "positive_patterns": len(positive),
            "most_common_category": most_common,
            "earliest_typical_onset_years": earliest_onset,
        },
        "config_used": config,
        "confidence": "documented",
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. pytest tests/test_community_analysis.py -v`
Expected: ALL PASS

- [ ] **Step 5: Run full test suite for regressions**

Run: `cd backend && PYTHONPATH=. pytest tests/ -v`
Expected: ALL PASS (522+ tests)

- [ ] **Step 6: Commit**

```bash
git add backend/app/services/analysis/community.py backend/tests/test_community_analysis.py
git commit -m "feat: add community analysis module with tests"
```

---

### Task 4: CommunityPatternAggregator

**Files:**
- Create: `backend/app/services/community/__init__.py`
- Create: `backend/app/services/community/aggregator.py`
- Create: `backend/tests/test_community.py`

- [ ] **Step 1: Write failing tests for the aggregator**

Create `backend/app/services/community/__init__.py` (empty file).

Create `backend/tests/test_community.py`:

```python
"""Tests for CommunityPatternAggregator and CommunityKnowledgeEngine."""
import pytest
from tests.conftest import make_community_report


# =========================================================================
# Aggregator Tests
# =========================================================================

class TestAggregatorBasic:
    def test_three_reports_create_pattern(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(
                boat_manufacturer="Bavaria",
                boat_model="38 Cruiser",
                issues=[{
                    "category": "material_degradation",
                    "zone_type": "hull",
                    "description": "Osmoseblasen am Unterwasserschiff",
                    "severity": "major",
                    "boat_age_months": 60 + i * 12,
                }],
            )
            for i in range(3)
        ]
        patterns = aggregate_reports_to_patterns(reports)
        matching = [p for p in patterns if p["manufacturer"] == "Bavaria"
                    and p["boat_model"] == "38 Cruiser"
                    and p["issue_category"] == "material_degradation"]
        assert len(matching) >= 1
        p = matching[0]
        assert p["report_count"] == 3
        assert p["is_positive"] is False

    def test_two_reports_below_threshold(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(
                boat_manufacturer="Hanse",
                boat_model="415",
                issues=[{
                    "category": "hardware",
                    "zone_type": "deck",
                    "description": "Relingstützen lockern",
                    "severity": "minor",
                    "boat_age_months": 36,
                }],
            )
            for _ in range(2)
        ]
        patterns = aggregate_reports_to_patterns(reports)
        matching = [p for p in patterns if p["manufacturer"] == "Hanse"
                    and p["boat_model"] == "415"
                    and p["issue_category"] == "hardware"]
        assert len(matching) == 0


class TestAggregatorSeverityAndOnset:
    def test_severity_mode(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(issues=[{
                "category": "structural", "zone_type": "hull",
                "description": "Riss", "severity": sev, "boat_age_months": 60,
            }])
            for sev in ["major", "major", "critical"]
        ]
        patterns = aggregate_reports_to_patterns(reports)
        structural = [p for p in patterns if p["issue_category"] == "structural"
                      and p["manufacturer"] == "Bavaria"]
        assert len(structural) >= 1
        assert structural[0]["severity_mode"] == "major"  # mode is major (2 vs 1)

    def test_onset_median(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(issues=[{
                "category": "cosmetic", "zone_type": "deck",
                "description": "Verfärbung", "severity": "cosmetic",
                "boat_age_months": months,
            }])
            for months in [24, 36, 60]
        ]
        patterns = aggregate_reports_to_patterns(reports)
        matching = [p for p in patterns if p["issue_category"] == "cosmetic"]
        assert len(matching) >= 1
        # median of [24, 36, 60] months = 36 months = 3.0 years
        assert matching[0]["typical_onset_years"] == 3.0


class TestAggregatorConfidence:
    def test_confidence_formula(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(
                reliability=0.8,
                issues=[{
                    "category": "electrical", "zone_type": "engine_room",
                    "description": "Kabelbruch", "severity": "major",
                    "boat_age_months": 48,
                }],
            )
            for _ in range(5)
        ]
        patterns = aggregate_reports_to_patterns(reports)
        matching = [p for p in patterns if p["issue_category"] == "electrical"]
        assert len(matching) >= 1
        # confidence = min(1.0, 5/10) × mean(0.8) = 0.5 × 0.8 = 0.4
        assert abs(matching[0]["confidence"] - 0.4) < 0.01

    def test_low_reliability_skipped(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(
                reliability=0.2,  # below 0.3 threshold
                issues=[{
                    "category": "design_flaw", "zone_type": "cabin",
                    "description": "Schlechtes Design", "severity": "minor",
                    "boat_age_months": 12,
                }],
            )
            for _ in range(5)
        ]
        patterns = aggregate_reports_to_patterns(reports)
        matching = [p for p in patterns if p["issue_category"] == "design_flaw"]
        assert len(matching) == 0  # all reports filtered out


class TestAggregatorPositive:
    def test_positive_patterns_aggregated(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(
                issues=[],
                positives=[{
                    "category": "structural",
                    "zone_type": "hull",
                    "description": "Hervorragende Kielstruktur",
                }],
            )
            for _ in range(3)
        ]
        patterns = aggregate_reports_to_patterns(reports)
        positives = [p for p in patterns if p["is_positive"] is True]
        assert len(positives) >= 1
        assert positives[0]["report_count"] == 3


class TestAggregatorConstructionLevel:
    def test_cross_manufacturer_construction_patterns(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(
                boat_manufacturer=mfr,
                boat_model=None,
                hull_material="grp_solid",
                hull_construction="hand_layup",
                issues=[{
                    "category": "material_degradation", "zone_type": "hull",
                    "description": "Print-through sichtbar", "severity": "cosmetic",
                    "boat_age_months": 36,
                }],
            )
            for mfr in ["Bavaria", "Hanse", "Jeanneau"]
        ]
        patterns = aggregate_reports_to_patterns(reports)
        # Should create a construction-level pattern (manufacturer=None)
        construction = [p for p in patterns if p["manufacturer"] is None
                        and "hand_layup" in (p.get("construction_methods_involved") or [])]
        assert len(construction) >= 1


class TestAggregatorIdempotent:
    def test_running_twice_same_result(self):
        from app.services.community.aggregator import aggregate_reports_to_patterns

        reports = [
            make_community_report(issues=[{
                "category": "hardware", "zone_type": "deck",
                "description": "Beschlag lose", "severity": "minor",
                "boat_age_months": 24,
            }])
            for _ in range(4)
        ]
        result1 = aggregate_reports_to_patterns(reports)
        result2 = aggregate_reports_to_patterns(reports)
        assert len(result1) == len(result2)
        # Compare pattern contents (ignoring source_report_ids which may differ)
        for p1, p2 in zip(
            sorted(result1, key=lambda p: (p["manufacturer"] or "", p["issue_category"])),
            sorted(result2, key=lambda p: (p["manufacturer"] or "", p["issue_category"])),
        ):
            assert p1["report_count"] == p2["report_count"]
            assert p1["severity_mode"] == p2["severity_mode"]
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_community.py -v -k "Aggregator"`
Expected: FAIL (module not found)

- [ ] **Step 3: Implement the aggregator**

Create `backend/app/services/community/aggregator.py`:

```python
"""Batch aggregation of community reports into patterns.

Pure function version: takes list of report dicts, returns list of pattern dicts.
The DB-backed wrapper (used by API endpoint) calls this function.
"""
from collections import Counter, defaultdict
from dataclasses import dataclass
from statistics import median


MIN_REPORTS_FOR_PATTERN = 3
MIN_RELIABILITY = 0.3


@dataclass
class AggregationResult:
    patterns_created: int
    reports_processed: int
    reports_skipped: int
    groups_below_threshold: int


def aggregate_reports_to_patterns(reports: list[dict]) -> list[dict]:
    """Aggregate community reports into patterns.

    Args:
        reports: List of report dicts (from DB or test factories).

    Returns:
        List of pattern dicts ready for DB insertion or direct use.
    """
    # Filter low-reliability reports
    valid_reports = [r for r in reports if r.get("reliability", 0) >= MIN_RELIABILITY]

    patterns = []

    # --- Negative patterns ---
    # Explode issues into individual tuples
    issue_entries = []
    for idx, report in enumerate(valid_reports):
        for issue in report.get("issues", []):
            issue_entries.append({
                "report_idx": idx,
                "report": report,
                "category": issue.get("category", "unknown"),
                "zone_type": issue.get("zone_type"),
                "description": issue.get("description", ""),
                "severity": issue.get("severity", "minor"),
                "boat_age_months": issue.get("boat_age_months"),
            })

    # Pass 1: Model-level grouping
    model_groups = defaultdict(list)
    for entry in issue_entries:
        mfr = entry["report"].get("boat_manufacturer")
        model = entry["report"].get("boat_model")
        if mfr and model:
            key = (mfr, model, entry["category"], entry["zone_type"])
            model_groups[key].append(entry)

    for (mfr, model, category, zone_type), entries in model_groups.items():
        if len(entries) < MIN_REPORTS_FOR_PATTERN:
            continue
        patterns.append(_build_pattern(entries, mfr, model, category, zone_type))

    # Pass 2: Manufacturer-level grouping
    mfr_groups = defaultdict(list)
    for entry in issue_entries:
        mfr = entry["report"].get("boat_manufacturer")
        if mfr:
            key = (mfr, entry["category"], entry["zone_type"])
            mfr_groups[key].append(entry)

    for (mfr, category, zone_type), entries in mfr_groups.items():
        if len(entries) < MIN_REPORTS_FOR_PATTERN:
            continue
        # Skip if already covered by a model-level pattern
        existing = [p for p in patterns
                    if p["manufacturer"] == mfr and p["issue_category"] == category
                    and p["zone_type"] == zone_type and p["boat_model"] is not None]
        if existing:
            continue
        patterns.append(_build_pattern(entries, mfr, None, category, zone_type))

    # Pass 3: Construction-level grouping (cross-manufacturer)
    construction_groups = defaultdict(list)
    for entry in issue_entries:
        hull_mat = entry["report"].get("hull_material")
        hull_con = entry["report"].get("hull_construction")
        if hull_mat:
            key = (hull_mat, hull_con, entry["category"], entry["zone_type"])
            construction_groups[key].append(entry)

    for (hull_mat, hull_con, category, zone_type), entries in construction_groups.items():
        if len(entries) < MIN_REPORTS_FOR_PATTERN:
            continue
        # Only create if reports come from ≥2 different manufacturers
        manufacturers = set(e["report"].get("boat_manufacturer") for e in entries)
        if len(manufacturers) < 2:
            continue
        p = _build_pattern(entries, None, None, category, zone_type)
        p["materials_involved"] = [hull_mat] if hull_mat else []
        p["construction_methods_involved"] = [hull_con] if hull_con else []
        patterns.append(p)

    # --- Positive patterns ---
    positive_entries = []
    for idx, report in enumerate(valid_reports):
        for pos in report.get("positives", []):
            positive_entries.append({
                "report_idx": idx,
                "report": report,
                "category": pos.get("category", "unknown"),
                "zone_type": pos.get("zone_type"),
                "description": pos.get("description", ""),
                "severity": "positive",
                "boat_age_months": None,
            })

    # Group positives by (manufacturer, model, category, zone_type)
    pos_groups = defaultdict(list)
    for entry in positive_entries:
        mfr = entry["report"].get("boat_manufacturer")
        model = entry["report"].get("boat_model")
        key = (mfr, model, entry["category"], entry["zone_type"])
        pos_groups[key].append(entry)

    for (mfr, model, category, zone_type), entries in pos_groups.items():
        if len(entries) < MIN_REPORTS_FOR_PATTERN:
            continue
        p = _build_pattern(entries, mfr, model, category, zone_type)
        p["is_positive"] = True
        p["severity_mode"] = "positive"
        patterns.append(p)

    return patterns


def _build_pattern(
    entries: list[dict],
    manufacturer: str | None,
    model: str | None,
    category: str,
    zone_type: str | None,
) -> dict:
    """Build a pattern dict from a group of issue entries."""
    report_count = len(entries)

    # Severity mode
    severities = [e["severity"] for e in entries]
    severity_mode = Counter(severities).most_common(1)[0][0]

    # Description mode
    descriptions = [e["description"] for e in entries]
    description = Counter(descriptions).most_common(1)[0][0]

    # Onset median
    age_values = [e["boat_age_months"] for e in entries if e.get("boat_age_months") is not None]
    typical_onset_years = round(median(age_values) / 12, 1) if len(age_values) >= 3 else None

    # Confidence
    reliabilities = [e["report"].get("reliability", 0.5) for e in entries]
    mean_reliability = sum(reliabilities) / len(reliabilities) if reliabilities else 0.5
    confidence = round(min(1.0, report_count / 10) * mean_reliability, 2)

    # Materials and construction from reports
    materials = list(set(
        e["report"].get("hull_material") for e in entries
        if e["report"].get("hull_material")
    ))
    constructions = list(set(
        e["report"].get("hull_construction") for e in entries
        if e["report"].get("hull_construction")
    ))

    # Source report indices (placeholder — real DB version would use IDs)
    report_indices = list(set(e["report_idx"] for e in entries))

    return {
        "manufacturer": manufacturer,
        "boat_model": model,
        "issue_category": category,
        "zone_type": zone_type,
        "description": description,
        "report_count": report_count,
        "severity_mode": severity_mode,
        "typical_onset_years": typical_onset_years,
        "materials_involved": materials or None,
        "construction_methods_involved": constructions or None,
        "confidence": confidence,
        "source_report_ids": report_indices,
        "is_positive": False,
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. pytest tests/test_community.py -v -k "Aggregator"`
Expected: ALL PASS

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/community/__init__.py backend/app/services/community/aggregator.py backend/tests/test_community.py
git commit -m "feat: add CommunityPatternAggregator with tests"
```

---

### Task 5: CommunityKnowledgeEngine

**Files:**
- Create: `backend/app/services/community/engine.py`
- Modify: `backend/tests/test_community.py` (add engine tests)

- [ ] **Step 1: Write failing tests for the engine**

Add to `backend/tests/test_community.py`:

```python
from tests.conftest import make_community_pattern


# =========================================================================
# Engine Tests (pure-function version)
# =========================================================================

class TestEngineExactModel:
    def test_exact_model_match_relevance_1(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [make_community_pattern(manufacturer="Bavaria", boat_model="38 Cruiser")]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Bavaria", model="38 Cruiser",
        )
        assert len(result) == 1
        assert result[0]["relevance"] == 1.0
        assert result[0]["match_reason"] == "exact_model"

    def test_no_match_returns_empty(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [make_community_pattern(manufacturer="Hanse", boat_model="415")]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Bavaria", model="38 Cruiser",
        )
        # Hanse 415 won't match Bavaria 38 at model/manufacturer level
        # but might match at construction level if materials match
        model_matches = [r for r in result if r["match_reason"] == "exact_model"]
        assert len(model_matches) == 0


class TestEngineManufacturer:
    def test_manufacturer_wide_match(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [make_community_pattern(manufacturer="Bavaria", boat_model=None)]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Bavaria", model="40 Sport",
        )
        mfr_matches = [r for r in result if r["match_reason"] == "manufacturer"]
        assert len(mfr_matches) == 1
        assert mfr_matches[0]["relevance"] == 0.8


class TestEngineConstructionMethod:
    def test_construction_method_match(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [make_community_pattern(
            manufacturer=None, boat_model=None,
            construction_methods_involved=["hand_layup"],
            materials_involved=["grp_solid"],
        )]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Jeanneau", model="Sun Odyssey 410",
        )
        construction_matches = [r for r in result if r["match_reason"] == "construction_method"]
        assert len(construction_matches) == 1
        assert construction_matches[0]["relevance"] == 0.6


class TestEngineMaterial:
    def test_material_only_match(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [make_community_pattern(
            manufacturer=None, boat_model=None,
            materials_involved=["grp_solid"],
            construction_methods_involved=["resin_infusion"],  # different construction
        )]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Unknown", model=None,
        )
        mat_matches = [r for r in result if r["match_reason"] == "material"]
        assert len(mat_matches) == 1
        assert mat_matches[0]["relevance"] == 0.4


class TestEngineZoneCategory:
    def test_zone_category_fallback(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [make_community_pattern(
            manufacturer="SomeOther", boat_model="X99",
            zone_type="deck", issue_category="material_degradation",
            materials_involved=["aluminium"],  # different material
            construction_methods_involved=["welded"],
        )]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Bavaria", model="38",
        )
        zone_matches = [r for r in result if r["match_reason"] == "zone_category"]
        assert len(zone_matches) == 1
        assert zone_matches[0]["relevance"] == 0.3


class TestEngineDeduplication:
    def test_same_pattern_highest_relevance_wins(self):
        from app.services.community.engine import find_relevant_patterns

        # This pattern matches at both model-level (1.0) and manufacturer-level (0.8)
        patterns = [make_community_pattern(manufacturer="Bavaria", boat_model="38 Cruiser")]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Bavaria", model="38 Cruiser",
        )
        # Should appear only once with highest relevance
        ids = [r["pattern_id"] for r in result]
        assert len(ids) == len(set(ids))  # no duplicates


class TestEngineMaxResults:
    def test_results_capped(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [
            make_community_pattern(
                manufacturer="Bavaria", boat_model=None,
                zone_type=f"zone_{i}", source_report_ids=[i],
            )
            for i in range(30)
        ]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Bavaria", model="38",
            max_results=10,
        )
        assert len(result) <= 10


class TestEnginePositive:
    def test_positive_patterns_returned(self):
        from app.services.community.engine import find_relevant_patterns

        patterns = [make_community_pattern(
            manufacturer="Bavaria", boat_model="38 Cruiser",
            is_positive=True, severity_mode="positive",
            description="Hervorragende Kielstruktur",
        )]
        result = find_relevant_patterns(
            patterns, hull_material="grp_solid", hull_construction="hand_layup",
            manufacturer="Bavaria", model="38 Cruiser",
            include_positive=True,
        )
        assert len(result) == 1
        assert result[0]["is_positive"] is True
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_community.py -v -k "Engine"`
Expected: FAIL (module not found)

- [ ] **Step 3: Implement the engine**

Create `backend/app/services/community/engine.py`:

```python
"""Community Knowledge Engine — relevance-based pattern matching.

Pure function version for testability. The DB-backed async version
wraps this with SQLAlchemy queries.
"""


def find_relevant_patterns(
    all_patterns: list[dict],
    hull_material: str | None = None,
    hull_construction: str | None = None,
    manufacturer: str | None = None,
    model: str | None = None,
    max_results: int = 20,
    include_positive: bool = False,
) -> list[dict]:
    """5-level relevance search against a list of pattern dicts.

    Args:
        all_patterns: All available patterns (from DB or test data).
        hull_material: Boat's hull material (BoatDNA value).
        hull_construction: Boat's hull construction method.
        manufacturer: Boat manufacturer name.
        model: Boat model name.
        max_results: Maximum patterns to return.
        include_positive: If True, include positive patterns in results.

    Returns:
        List of pattern dicts augmented with relevance, match_reason, pattern_id.
        Sorted by relevance × confidence descending.
    """
    # Filter by positive/negative
    candidates = all_patterns
    if not include_positive:
        candidates = [p for p in candidates if not p.get("is_positive", False)]

    # Collect matches with relevance scores
    matches: dict[int, dict] = {}  # pattern_id -> best match

    for idx, pattern in enumerate(candidates):
        pattern_id = pattern.get("id", idx)
        p_mfr = pattern.get("manufacturer")
        p_model = pattern.get("boat_model")
        p_materials = pattern.get("materials_involved") or []
        p_constructions = pattern.get("construction_methods_involved") or []

        best_relevance = 0.0
        best_reason = None

        # Level 1: Exact model match
        if (manufacturer and model and p_mfr
                and p_mfr.lower() == manufacturer.lower()
                and p_model and p_model.lower() == model.lower()):
            best_relevance = 1.0
            best_reason = "exact_model"

        # Level 2: Manufacturer-wide (pattern has no model)
        if (manufacturer and p_mfr
                and p_mfr.lower() == manufacturer.lower()
                and p_model is None
                and best_relevance < 0.8):
            best_relevance = 0.8
            best_reason = "manufacturer"

        # Level 3: Construction method match (cross-manufacturer patterns)
        if (hull_material and hull_construction
                and p_mfr is None
                and hull_material in p_materials
                and hull_construction in p_constructions
                and best_relevance < 0.6):
            best_relevance = 0.6
            best_reason = "construction_method"

        # Level 4: Material-specific (cross-manufacturer, material only)
        if (hull_material
                and p_mfr is None
                and hull_material in p_materials
                and best_relevance < 0.4):
            best_relevance = 0.4
            best_reason = "material"

        # Level 5: Zone + Category fallback (any pattern)
        if (pattern.get("zone_type") and pattern.get("issue_category")
                and best_relevance < 0.3):
            best_relevance = 0.3
            best_reason = "zone_category"

        if best_relevance > 0 and best_reason:
            # Keep highest relevance per pattern_id
            if pattern_id not in matches or matches[pattern_id]["relevance"] < best_relevance:
                matches[pattern_id] = {
                    "pattern_id": pattern_id,
                    "relevance": best_relevance,
                    "category": pattern.get("issue_category", "unknown"),
                    "zone_type": pattern.get("zone_type"),
                    "description": pattern.get("description", ""),
                    "report_count": pattern.get("report_count", 0),
                    "severity": pattern.get("severity_mode", "minor"),
                    "typical_onset_years": pattern.get("typical_onset_years"),
                    "materials_involved": pattern.get("materials_involved") or [],
                    "confidence": pattern.get("confidence", 0.5),
                    "match_reason": best_reason,
                    "is_positive": pattern.get("is_positive", False),
                }

    # Sort by relevance × confidence, truncate
    sorted_matches = sorted(
        matches.values(),
        key=lambda m: m["relevance"] * m["confidence"],
        reverse=True,
    )

    return sorted_matches[:max_results]
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. pytest tests/test_community.py -v -k "Engine"`
Expected: ALL PASS

- [ ] **Step 5: Run full test suite**

Run: `cd backend && PYTHONPATH=. pytest tests/ -v`
Expected: ALL PASS

- [ ] **Step 6: Commit**

```bash
git add backend/app/services/community/engine.py backend/tests/test_community.py
git commit -m "feat: add CommunityKnowledgeEngine with 5-level relevance matching"
```

---

### Task 6: API Endpoints

**Files:**
- Create: `backend/app/api/routes/community.py`
- Modify: `backend/app/main.py`

- [ ] **Step 1: Create the community router**

Create `backend/app/api/routes/community.py`:

```python
"""Community Intelligence API endpoints."""
from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.models import CommunityReport, CommunityPattern
from app.schemas.schemas import (
    AggregationResultResponse,
    CommunityReportCreate,
    CommunityReportResponse,
    CommunityPatternResponse,
)
from app.services.community.aggregator import aggregate_reports_to_patterns
from app.services.community.engine import find_relevant_patterns

router = APIRouter(prefix="/community", tags=["community"])


# === Reports ===

@router.post("/reports", response_model=CommunityReportResponse, status_code=201)
async def create_report(
    report: CommunityReportCreate,
    db: AsyncSession = Depends(get_db),
):
    """Create a community report."""
    db_report = CommunityReport(
        source_forum=report.source_forum,
        source_url=report.source_url,
        source_date=report.source_date,
        boat_manufacturer=report.boat_manufacturer,
        boat_model=report.boat_model,
        boat_year=report.boat_year,
        hull_material=report.hull_material,
        hull_construction=report.hull_construction,
        propulsion=report.propulsion,
        issues=[issue.model_dump() for issue in report.issues],
        positives=[pos.model_dump() for pos in report.positives],
        reliability=report.reliability,
        raw_text=report.raw_text,
    )
    db.add(db_report)
    await db.commit()
    await db.refresh(db_report)
    return db_report


@router.get("/reports", response_model=list[CommunityReportResponse])
async def list_reports(
    manufacturer: str | None = None,
    model: str | None = None,
    hull_material: str | None = None,
    limit: int = Query(default=50, le=200),
    offset: int = Query(default=0, ge=0),
    db: AsyncSession = Depends(get_db),
):
    """List community reports with optional filters."""
    query = select(CommunityReport)
    if manufacturer:
        query = query.where(CommunityReport.boat_manufacturer == manufacturer)
    if model:
        query = query.where(CommunityReport.boat_model == model)
    if hull_material:
        query = query.where(CommunityReport.hull_material == hull_material)
    query = query.order_by(CommunityReport.created_at.desc())
    query = query.offset(offset).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


@router.get("/reports/{report_id}", response_model=CommunityReportResponse)
async def get_report(report_id: int, db: AsyncSession = Depends(get_db)):
    """Get a single community report."""
    result = await db.execute(
        select(CommunityReport).where(CommunityReport.id == report_id)
    )
    report = result.scalar_one_or_none()
    if not report:
        raise HTTPException(status_code=404, detail="Report nicht gefunden")
    return report


# === Patterns ===

@router.get("/patterns", response_model=list[CommunityPatternResponse])
async def list_patterns(
    manufacturer: str | None = None,
    model: str | None = None,
    hull_material: str | None = None,
    zone_type: str | None = None,
    is_positive: bool | None = None,
    limit: int = Query(default=50, le=200),
    offset: int = Query(default=0, ge=0),
    db: AsyncSession = Depends(get_db),
):
    """List community patterns with optional filters."""
    query = select(CommunityPattern)
    if manufacturer:
        query = query.where(CommunityPattern.manufacturer == manufacturer)
    if model:
        query = query.where(CommunityPattern.boat_model == model)
    if zone_type:
        query = query.where(CommunityPattern.zone_type == zone_type)
    if is_positive is not None:
        query = query.where(CommunityPattern.is_positive == is_positive)
    query = query.order_by(CommunityPattern.confidence.desc())
    query = query.offset(offset).limit(limit)
    result = await db.execute(query)
    return result.scalars().all()


@router.get("/patterns/{pattern_id}", response_model=CommunityPatternResponse)
async def get_pattern(pattern_id: int, db: AsyncSession = Depends(get_db)):
    """Get a single community pattern."""
    result = await db.execute(
        select(CommunityPattern).where(CommunityPattern.id == pattern_id)
    )
    pattern = result.scalar_one_or_none()
    if not pattern:
        raise HTTPException(status_code=404, detail="Pattern nicht gefunden")
    return pattern


# === Aggregation ===

@router.post("/aggregate", response_model=AggregationResultResponse)
async def run_aggregation(db: AsyncSession = Depends(get_db)):
    """Trigger batch aggregation of reports into patterns.

    Idempotent: deletes all existing patterns and recreates from reports.
    """
    # Load all reports
    result = await db.execute(select(CommunityReport))
    reports = result.scalars().all()

    # Convert to dicts for the pure-function aggregator
    report_dicts = []
    for r in reports:
        report_dicts.append({
            "id": r.id,
            "boat_manufacturer": r.boat_manufacturer,
            "boat_model": r.boat_model,
            "boat_year": r.boat_year,
            "hull_material": r.hull_material,
            "hull_construction": r.hull_construction,
            "propulsion": r.propulsion,
            "issues": r.issues or [],
            "positives": r.positives or [],
            "reliability": r.reliability,
        })

    # Run aggregation
    pattern_dicts = aggregate_reports_to_patterns(report_dicts)

    # Delete existing patterns
    await db.execute(
        CommunityPattern.__table__.delete()
    )

    # Insert new patterns
    skipped_count = len([r for r in report_dicts if r.get("reliability", 0) < 0.3])
    for pd in pattern_dicts:
        db_pattern = CommunityPattern(
            manufacturer=pd["manufacturer"],
            boat_model=pd["boat_model"],
            issue_category=pd["issue_category"],
            zone_type=pd["zone_type"],
            description=pd["description"],
            report_count=pd["report_count"],
            severity_mode=pd["severity_mode"],
            typical_onset_years=pd["typical_onset_years"],
            materials_involved=pd["materials_involved"],
            construction_methods_involved=pd["construction_methods_involved"],
            confidence=pd["confidence"],
            source_report_ids=pd["source_report_ids"],
            is_positive=pd.get("is_positive", False),
        )
        db.add(db_pattern)

    await db.commit()

    return AggregationResultResponse(
        patterns_created=len(pattern_dicts),
        reports_processed=len(report_dicts) - skipped_count,
        reports_skipped=skipped_count,
        groups_below_threshold=0,  # Not tracked in pure-function version
    )


# === Relevance Query ===

@router.get("/relevant")
async def get_relevant_patterns(
    manufacturer: str | None = None,
    model: str | None = None,
    boat_class: str = "cruising_sail",
    hull_material: str | None = None,
    hull_construction: str | None = None,
    propulsion: str | None = None,
    max_results: int = Query(default=20, le=50),
    db: AsyncSession = Depends(get_db),
):
    """Get patterns relevant to a specific boat via 5-level relevance matching."""
    # Load all patterns from DB
    result = await db.execute(select(CommunityPattern))
    db_patterns = result.scalars().all()

    # Convert to dicts
    pattern_dicts = []
    for p in db_patterns:
        pattern_dicts.append({
            "id": p.id,
            "manufacturer": p.manufacturer,
            "boat_model": p.boat_model,
            "issue_category": p.issue_category,
            "zone_type": p.zone_type,
            "description": p.description,
            "report_count": p.report_count,
            "severity_mode": p.severity_mode,
            "typical_onset_years": p.typical_onset_years,
            "materials_involved": p.materials_involved,
            "construction_methods_involved": p.construction_methods_involved,
            "confidence": p.confidence,
            "source_report_ids": p.source_report_ids,
            "is_positive": p.is_positive,
        })

    # Run relevance engine (negative patterns)
    negative = find_relevant_patterns(
        pattern_dicts,
        hull_material=hull_material,
        hull_construction=hull_construction,
        manufacturer=manufacturer,
        model=model,
        max_results=max_results,
        include_positive=False,
    )

    # Run relevance engine (positive patterns)
    positive = find_relevant_patterns(
        pattern_dicts,
        hull_material=hull_material,
        hull_construction=hull_construction,
        manufacturer=manufacturer,
        model=model,
        max_results=max_results // 2,
        include_positive=True,
    )
    positive = [p for p in positive if p.get("is_positive")]

    return {"negative": negative, "positive": positive}
```

- [ ] **Step 2: Register the router in main.py**

Add to `backend/app/main.py` imports:

```python
from app.api.routes import community
```

Add after the last `app.include_router(...)`:

```python
app.include_router(community.router, prefix="/api/v1")
```

- [ ] **Step 3: Verify the app starts**

Run: `cd backend && PYTHONPATH=. python -c "from app.main import app; print(f'{len(app.routes)} routes registered')"`
Expected: Route count increased by ~7

- [ ] **Step 4: Commit**

```bash
git add backend/app/api/routes/community.py backend/app/main.py
git commit -m "feat: add community API endpoints and register router"
```

---

### Task 7: Orchestrator, Score Fusion & BoatDNA Resolver Integration

**Files:**
- Modify: `backend/app/services/analysis/orchestrator.py`
- Modify: `backend/app/services/analysis/score_fusion.py`
- Modify: `backend/app/services/boat_dna_resolver.py`
- Create: `backend/tests/test_community_integration.py`

- [ ] **Step 1: Write failing integration tests**

Create `backend/tests/test_community_integration.py`:

```python
"""Integration tests for Community Intelligence with orchestrator and resolver."""
import pytest
from tests.conftest import make_zone, make_passage, make_community_pattern


class TestOrchestratorIntegration:
    def test_community_in_execution_tiers(self):
        from app.services.analysis.orchestrator import EXECUTION_TIERS
        tier1 = EXECUTION_TIERS[0]
        assert "community" in tier1

    def test_community_in_overall_weights(self):
        from app.services.analysis.orchestrator import OVERALL_WEIGHTS
        for boat_class in ["small_sail", "cruising_sail", "large_motor", "superyacht"]:
            assert "community" in OVERALL_WEIGHTS[boat_class]

    def test_build_module_kwargs_community(self):
        from app.services.analysis.orchestrator import _build_module_kwargs, AnalysisContext
        context = AnalysisContext(
            zones=[make_zone()],
            passages=[make_passage()],
            boat_class="cruising_sail",
        )
        context.community_patterns = [make_community_pattern()]
        kwargs = _build_module_kwargs("community", context)
        assert "community_patterns" in kwargs
        assert len(kwargs["community_patterns"]) == 1

    def test_community_module_runs_in_orchestrator(self):
        """Full orchestrator run with community patterns."""
        import asyncio
        from app.services.analysis.orchestrator import run_full_analysis, AnalysisContext

        context = AnalysisContext(
            zones=[make_zone(), make_zone(name="cockpit", zone_type="cockpit")],
            passages=[make_passage()],
            boat_class="cruising_sail",
        )
        context.community_patterns = [
            make_community_pattern(severity_mode="major", confidence=0.7),
        ]

        result = asyncio.get_event_loop().run_until_complete(run_full_analysis(context))
        # Community module should be in results
        module_names = [m["module"] for m in result.get("modules", [])]
        assert "community" in module_names


class TestScoreFusionIntegration:
    def test_community_in_fusion_weights(self):
        from app.services.analysis.score_fusion import FUSION_WEIGHTS
        assert "community" in FUSION_WEIGHTS
        assert FUSION_WEIGHTS["community"] == (1.0, 0.0)


class TestBoatDNAResolverIntegration:
    def test_resolver_includes_community_config(self):
        from app.models.boat_dna import BoatDNA
        from app.services.boat_dna_resolver import BoatDNAResolver

        dna = BoatDNA.from_boat_class("cruising_sail")
        resolver = BoatDNAResolver()
        result = resolver.resolve(dna)

        assert "community" in result
        assert "min_confidence" in result["community"]
        assert "max_patterns" in result["community"]

    def test_resolver_overall_weights_include_community(self):
        from app.models.boat_dna import BoatDNA
        from app.services.boat_dna_resolver import BoatDNAResolver

        dna = BoatDNA.from_boat_class("cruising_sail")
        resolver = BoatDNAResolver()
        result = resolver.resolve(dna)

        assert "overall_weights" in result
        assert "community" in result["overall_weights"]
        assert result["overall_weights"]["community"] > 0

    def test_all_weights_sum_to_one(self):
        from app.models.boat_dna import BoatDNA
        from app.services.boat_dna_resolver import BoatDNAResolver

        for bc in ["small_sail", "cruising_sail", "large_motor", "superyacht"]:
            dna = BoatDNA.from_boat_class(bc)
            resolver = BoatDNAResolver()
            result = resolver.resolve(dna)
            weights = result["overall_weights"]
            total = sum(weights.values())
            assert abs(total - 1.0) < 0.001, f"{bc}: weights sum to {total}"
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_community_integration.py -v`
Expected: FAIL

- [ ] **Step 3: Modify orchestrator.py**

In `backend/app/services/analysis/orchestrator.py`:

**a)** Add `community_patterns` to `AnalysisContext` dataclass (add after existing fields):

```python
    community_patterns: list[dict] = field(default_factory=list)
```

**b)** Add `"community"` to `EXECUTION_TIERS[0]`:

Change:
```python
    ["ergonomics", "volume_storage", "emotional", "compliance"],
```
To:
```python
    ["ergonomics", "volume_storage", "emotional", "compliance", "community"],
```

**c)** Add community import to `_get_module_runners()`:

```python
    from app.services.analysis.community import run_community_analysis
```

And add to the runners dict:

```python
    "community": run_community_analysis,
```

**d)** Add community case to `_build_module_kwargs()`:

```python
    elif module == "community":
        kwargs["community_patterns"] = context.community_patterns
```

**e)** Add `"community": 0.05` to each entry in `OVERALL_WEIGHTS`. To maintain sum = 1.0, subtract 0.05 from the largest-weighted module in each class:

- `"small_sail"`: reduce `"ergonomics"` from 0.20 to 0.15, add `"community": 0.05`
- `"cruising_sail"`: reduce `"ergonomics"` from 0.20 to 0.15, add `"community": 0.05`
- `"large_motor"`: reduce `"emotional"` from 0.20 to 0.15, add `"community": 0.05`
- `"superyacht"`: reduce `"emotional"` from 0.25 to 0.20, add `"community": 0.05`

- [ ] **Step 4: Modify score_fusion.py**

In `backend/app/services/analysis/score_fusion.py`, add to `FUSION_WEIGHTS`:

```python
    "community": (1.0, 0.0),
```

- [ ] **Step 5: Modify boat_dna_resolver.py**

In `backend/app/services/boat_dna_resolver.py`:

**a)** Add import of community BOAT_CLASS_DEFAULTS in `_build_legacy_configs()`:

```python
    from app.services.analysis.community import BOAT_CLASS_DEFAULTS as community_defaults
```

And add to the config building:

```python
    configs[bc]["community"] = community_defaults.get(bc, {})
```

**b)** Add `_resolve_community(self, dna)` method:

```python
    def _resolve_community(self, dna):
        """Resolve community module config from BoatDNA."""
        config = {
            "max_patterns": 20,
            "min_confidence": 0.3,
            "severity_weights": {"critical": 25, "major": 15, "minor": 5, "cosmetic": 2},
        }

        # Superyacht tier: more patterns relevant, lower confidence threshold
        if dna.builder_quality_tier == "superyacht":
            config["max_patterns"] = 25
            config["min_confidence"] = 0.2

        # Small boats: fewer patterns expected
        if dna.length_m < 10:
            config["max_patterns"] = 15
            config["min_confidence"] = 0.4

        return config
```

**c)** Call `_resolve_community` in `_resolve_custom()` and add to result dict.

**d)** Add `"community"` to `_resolve_overall_weights()`:

```python
    weights["community"] = 0.05
    # Increase for mass production boats (more community data available)
    if dna.production_type == "mass_production":
        weights["community"] = 0.08
```

- [ ] **Step 6: Run integration tests**

Run: `cd backend && PYTHONPATH=. pytest tests/test_community_integration.py -v`
Expected: ALL PASS

- [ ] **Step 7: Run full test suite**

Run: `cd backend && PYTHONPATH=. pytest tests/ -v`
Expected: ALL PASS

- [ ] **Step 8: Commit**

```bash
git add backend/app/services/analysis/orchestrator.py backend/app/services/analysis/score_fusion.py backend/app/services/boat_dna_resolver.py backend/tests/test_community_integration.py
git commit -m "feat: integrate community module into orchestrator, score fusion, and BoatDNA resolver"
```

---

### Task 8: Seed Data

**Files:**
- Modify: `backend/app/db/seed.py`

- [ ] **Step 1: Add seed_community_data function**

Add to `backend/app/db/seed.py`:

```python
async def seed_community_data(db):
    """Seed realistic community reports and run aggregation."""
    from app.models.models import CommunityReport, CommunityPattern
    from app.services.community.aggregator import aggregate_reports_to_patterns

    # Check if data already exists
    result = await db.execute(select(CommunityReport).limit(1))
    if result.scalar_one_or_none():
        logger.info("Community data already seeded")
        return

    reports_data = [
        # Bavaria 38 — Osmose (5 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Bavaria",
            "boat_model": "38 Cruiser",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "hull",
                "description": "Osmoseblasen am Unterwasserschiff",
                "severity": "major",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.8 + i * 0.02,
        } for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de", "cruisersforum.com",
            "boote-forum.de", "sailboatowners.com",
        ])],

        # Bavaria 38 — Hull/deck fastener loosening (4 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Bavaria",
            "boat_model": "38 Cruiser",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "deck",
                "description": "Rumpf/Deck-Verschraubung lockert nach 5-8 Jahren",
                "severity": "major",
                "boat_age_months": 60 + i * 6,
            }],
            "positives": [],
            "reliability": 0.75 + i * 0.05,
        } for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de", "cruisersforum.com", "boote-forum.de",
        ])],

        # Hanse 415 — Railing loosening (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Hanse",
            "boat_model": "415",
            "boat_year": 2017,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "deck",
                "description": "Relingstützen lockern sich nach 3-5 Jahren",
                "severity": "minor",
                "boat_age_months": 36 + i * 12,
            }],
            "positives": [],
            "reliability": 0.7,
        } for i, forum in enumerate([
            "segeln-forum.de", "boote-forum.de", "myhanse.com",
        ])],

        # Hanse 415 — Galley countertop (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Hanse",
            "boat_model": "415",
            "boat_year": 2018,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "galley",
                "description": "Arbeitsplatten splittern an Kanten",
                "severity": "cosmetic",
                "boat_age_months": 12 + i * 6,
            }],
            "positives": [],
            "reliability": 0.65,
        } for i, forum in enumerate([
            "myhanse.com", "boote-forum.de", "segeln-forum.de",
        ])],

        # Hallberg-Rassy 40 — Positive: keel (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Hallberg-Rassy",
            "boat_model": "40",
            "boat_year": 2016,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [],
            "positives": [{
                "category": "structural",
                "zone_type": "hull",
                "description": "Kielstruktur direkt laminiert — von Gutachtern besser bewertet als modular",
            }],
            "reliability": 0.9,
        } for forum in [
            "segeln-forum.de", "cruisersforum.com", "ybw.com",
        ]],

        # Cross-manufacturer GRP hand_layup — Print-through (4 reports from 3 mfrs)
        *[{
            "source_forum": "boote-forum.de",
            "boat_manufacturer": mfr,
            "boat_model": None,
            "boat_year": 2016,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "cosmetic",
                "zone_type": "hull",
                "description": "Print-through der Gewebestruktur sichtbar",
                "severity": "cosmetic",
                "boat_age_months": 36 + i * 12,
            }],
            "positives": [],
            "reliability": 0.7,
        } for i, mfr in enumerate([
            "Bavaria", "Hanse", "Jeanneau", "Dufour",
        ])],

        # Jeanneau Sun Odyssey — Chainplate cracks (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Jeanneau",
            "boat_model": "Sun Odyssey 410",
            "boat_year": 2012 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "rigging",
                "description": "Haarrisse an Wantenplatten nach 8-12 Jahren",
                "severity": "critical",
                "boat_age_months": 96 + i * 12,
            }],
            "positives": [],
            "reliability": 0.85,
        } for i, forum in enumerate([
            "cruisersforum.com", "segeln-forum.de", "sailboatowners.com",
        ])],

        # Bavaria general — Positive: price/value (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Bavaria",
            "boat_model": None,
            "boat_year": None,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [],
            "positives": [{
                "category": "design_flaw",  # using as "value" proxy
                "zone_type": "cabin",
                "description": "Gutes Preis-Leistungs-Verhältnis für Innenraum und Ausstattung",
            }],
            "reliability": 0.7,
        } for forum in [
            "boote-forum.de", "segeln-forum.de", "boote-forum.de",
        ]],
    ]

    # Insert reports
    for rd in reports_data:
        report = CommunityReport(**rd)
        db.add(report)
    await db.flush()

    # Run aggregation
    all_reports = (await db.execute(select(CommunityReport))).scalars().all()
    report_dicts = [{
        "id": r.id,
        "boat_manufacturer": r.boat_manufacturer,
        "boat_model": r.boat_model,
        "hull_material": r.hull_material,
        "hull_construction": r.hull_construction,
        "propulsion": r.propulsion,
        "issues": r.issues or [],
        "positives": r.positives or [],
        "reliability": r.reliability,
    } for r in all_reports]

    pattern_dicts = aggregate_reports_to_patterns(report_dicts)
    for pd in pattern_dicts:
        pattern = CommunityPattern(
            manufacturer=pd["manufacturer"],
            boat_model=pd["boat_model"],
            issue_category=pd["issue_category"],
            zone_type=pd["zone_type"],
            description=pd["description"],
            report_count=pd["report_count"],
            severity_mode=pd["severity_mode"],
            typical_onset_years=pd["typical_onset_years"],
            materials_involved=pd["materials_involved"],
            construction_methods_involved=pd["construction_methods_involved"],
            confidence=pd["confidence"],
            source_report_ids=pd["source_report_ids"],
            is_positive=pd.get("is_positive", False),
        )
        db.add(pattern)

    await db.commit()
    logger.info(f"Seeded {len(reports_data)} community reports → {len(pattern_dicts)} patterns")
```

Add the import at the top of seed.py:

```python
from sqlalchemy import select
```

Call `seed_community_data` at the end of the existing `seed()` function:

```python
    await seed_community_data(db)
```

- [ ] **Step 2: Run full test suite**

Run: `cd backend && PYTHONPATH=. pytest tests/ -v`
Expected: ALL PASS

- [ ] **Step 3: Commit**

```bash
git add backend/app/db/seed.py
git commit -m "feat: add community intelligence seed data with realistic yacht reports"
```

---

### Task Summary

| Task | Component | New Files | Modified Files |
|------|-----------|-----------|----------------|
| 1 | Database Models | — | models.py |
| 2 | Schemas + Factories | — | schemas.py, conftest.py |
| 3 | Analysis Module | community.py, test_community_analysis.py | — |
| 4 | Aggregator | aggregator.py, \_\_init\_\_.py, test_community.py | — |
| 5 | Engine | engine.py | test_community.py |
| 6 | API Endpoints | community.py (routes) | main.py |
| 7 | Integration | test_community_integration.py | orchestrator.py, score_fusion.py, boat_dna_resolver.py |
| 8 | Seed Data | — | seed.py |
