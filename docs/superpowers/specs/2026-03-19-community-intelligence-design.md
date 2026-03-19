# Community Intelligence — Phase 1: Knowledge Base, Pattern Engine & Module Integration

## Goal

Add a Community Intelligence system that surfaces real-world owner experiences (forum reports, owner feedback) as actionable findings in AYDI's analysis pipeline. Phase 1 focuses on the data model, pattern aggregation, relevance engine, and integration as a standalone analysis module — without building the forum crawler or NLP extraction pipeline.

## Scope

**In scope (Phase 1):**
- `CommunityReport` and `CommunityPattern` database models
- `CommunityKnowledgeEngine` service for 5-level relevance matching
- `CommunityPatternAggregator` for batch report→pattern aggregation
- `community` analysis module (standalone, pure function, like existing 11 modules)
- API endpoints for CRUD + aggregation + relevance queries
- Seed data with 15–20 realistic reports based on known yacht issues
- Orchestrator + BoatDNA Resolver integration

**Out of scope (Phase 2+):**
- Forum crawler (Celery, robots.txt, rate limiting)
- NLP extraction via Claude API
- Deduplication of natural-language reports
- Manufacturer response workflow
- Frontend UI for community data

## Architecture

```
                    ┌──────────────────────┐
                    │   API Endpoints      │
                    │  /community/reports   │
                    │  /community/patterns  │
                    │  /community/aggregate │
                    │  /community/relevant  │
                    └──────────┬───────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
    ┌─────────────────┐ ┌───────────┐ ┌─────────────────────┐
    │ CommunityReport │ │ Aggregator│ │ CommunityKnowledge  │
    │ CommunityPattern│ │ (Batch)   │ │ Engine (Query)      │
    │ (DB Models)     │ │           │ │                     │
    └─────────────────┘ └───────────┘ └──────────┬──────────┘
                                                  │ patterns
                                                  ▼
                                        ┌───────────────────┐
                                        │ community.py      │
                                        │ (Analysis Module)  │
                                        │ Pure function      │
                                        └───────────────────┘
                                                  │ result dict
                                                  ▼
                                        ┌───────────────────┐
                                        │ Orchestrator      │
                                        │ (Tier 1, parallel)│
                                        └───────────────────┘
```

---

## 1. Data Model

Two new SQLAlchemy models in `backend/app/models/models.py`.

### CommunityReport

Individual experience report from a forum post, owner feedback, or manual entry.

| Column | Type | Constraints | Description |
|--------|------|------------|-------------|
| `id` | Integer | PK, autoincrement | |
| `created_at` | DateTime | default=utcnow | When report was added to AYDI |
| `updated_at` | DateTime | onupdate=utcnow | |
| `source_forum` | String(100) | NOT NULL | e.g. "boote-forum.de", "cruisersforum.com" |
| `source_url` | String(500) | nullable | Link to original post |
| `source_date` | Date | nullable | Date of original post |
| `boat_manufacturer` | String(100) | NOT NULL | e.g. "Bavaria", "Hanse", "Hallberg-Rassy" |
| `boat_model` | String(100) | nullable | e.g. "38 Cruiser", "415" |
| `boat_year` | Integer | nullable | Build year |
| `hull_material` | String(50) | nullable | BoatDNA values: "grp_solid", "aluminium", etc. |
| `hull_construction` | String(50) | nullable | BoatDNA values: "hand_layup", "welded", etc. |
| `propulsion` | String(20) | nullable | "sail", "motor", "sail_motor" |
| `issues` | JSON | NOT NULL, default=[] | List of issue dicts (see below) |
| `positives` | JSON | default=[] | List of positive finding dicts |
| `reliability` | Float | NOT NULL, 0.0–1.0 | Trustworthiness of this report |
| `raw_text` | Text | nullable | Original text for traceability |

**Issue dict structure:**
```python
{
    "category": str,        # "structural", "material_degradation", "hardware",
                            # "electrical", "cosmetic", "design_flaw"
    "zone_type": str,       # "hull", "deck", "cockpit", "galley", "head",
                            # "cabin", "engine_room", "bilge", "rigging"
    "description": str,     # German, concise
    "severity": str,        # "critical", "major", "minor", "cosmetic"
    "boat_age_months": int  # Age of boat when issue appeared
}
```

**Positive dict structure:**
```python
{
    "category": str,    # Same categories as issues
    "zone_type": str,   # Same zones
    "description": str  # German, concise
}
```

### CommunityPattern

Aggregated pattern derived from ≥3 independent reports.

| Column | Type | Constraints | Description |
|--------|------|------------|-------------|
| `id` | Integer | PK, autoincrement | |
| `created_at` | DateTime | default=utcnow | |
| `updated_at` | DateTime | onupdate=utcnow | |
| `manufacturer` | String(100) | nullable | null = cross-manufacturer pattern |
| `model` | String(100) | nullable | null = manufacturer-wide pattern |
| `issue_category` | String(50) | NOT NULL | Same categories as report issues |
| `zone_type` | String(50) | nullable | Same zones as report issues |
| `description` | String(500) | NOT NULL | German, concise |
| `report_count` | Integer | NOT NULL | Number of independent reports |
| `severity_mode` | String(20) | NOT NULL | Mode of severity values: "critical", "major", "minor", "cosmetic" |
| `typical_onset_years` | Float | nullable | Median boat age at issue onset |
| `materials_involved` | JSON | nullable | List of material strings |
| `construction_methods_involved` | JSON | nullable | List of construction method strings |
| `confidence` | Float | NOT NULL, 0.0–1.0 | Statistical confidence |
| `source_report_ids` | JSON | NOT NULL | List of report IDs backing this pattern |
| `is_positive` | Boolean | NOT NULL, default=False | True for positive patterns |
| `manufacturer_response` | JSON | nullable | Reserved for Phase 2 |

**Indexes:**
- `(manufacturer, model)`
- `(issue_category)`
- `(hull_material, hull_construction)` — on CommunityReport for construction-method queries
- `(zone_type)`

---

## 2. CommunityKnowledgeEngine (Service)

**Location:** `backend/app/services/community/engine.py`

```python
class CommunityKnowledgeEngine:
    """Queries community patterns relevant to a specific boat."""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def get_relevant_patterns(
        self,
        dna: BoatDNA,
        manufacturer: str | None = None,
        model: str | None = None,
        max_results: int = 20,
    ) -> list[dict]:
        """5-level relevance search, deduplicated, sorted by relevance."""

    async def get_positive_patterns(
        self,
        dna: BoatDNA,
        manufacturer: str | None = None,
        model: str | None = None,
        max_results: int = 10,
    ) -> list[dict]:
        """Same logic but for positive findings."""
```

### 5-Level Relevance Matching

Each level is a separate DB query. Results are deduplicated by `pattern_id`, scored by `relevance × confidence`, sorted descending, truncated to `max_results`.

| Level | Match Criteria | Relevance Score | Example |
|-------|---------------|-----------------|---------|
| 1. Exact model | `manufacturer + model` | 1.0 | "Bavaria 38 Cruiser" |
| 2. Manufacturer-wide | `manufacturer` (model=null on pattern) | 0.8 | "Bavaria generell" |
| 3. Construction method | `hull_material + hull_construction` (via source reports) | 0.6 | "Alle Hand-Layup GFK Boote" |
| 4. Material-specific | `hull_material` alone | 0.4 | "Alle GFK Boote" |
| 5. Zone+Category | `zone_type + issue_category` (no boat filter) | 0.3 | "Generelle Deck-Probleme" |

Level 3 requires a join: patterns whose `source_report_ids` reference reports with matching `hull_material + hull_construction`. Alternative: denormalize `construction_methods_involved` on the pattern and query that directly.

**Design decision:** Use `construction_methods_involved` JSON field on `CommunityPattern` for Level 3 matching. Avoids join, pattern already has this data from aggregation.

### Return Format

```python
{
    "pattern_id": int,
    "relevance": float,         # 0.0–1.0 from matching level
    "category": str,
    "zone_type": str | None,
    "description": str,         # German
    "report_count": int,
    "severity": str,
    "typical_onset_years": float | None,
    "materials_involved": list[str],
    "confidence": float,
    "match_reason": str,        # "exact_model", "manufacturer", "construction_method",
                                # "material", "zone_category"
}
```

---

## 3. CommunityPatternAggregator (Batch)

**Location:** `backend/app/services/community/aggregator.py`

```python
class CommunityPatternAggregator:
    """Aggregates community_reports into community_patterns."""

    def __init__(self, db: AsyncSession):
        self.db = db

    async def aggregate(self) -> AggregationResult:
        """Full re-aggregation. Idempotent — deletes all patterns, rebuilds from reports."""
```

### Aggregation Logic

1. **Filter:** Skip reports with `reliability < 0.3`.

2. **Grouping:** Each report's issues are exploded into individual `(manufacturer, model, category, zone_type)` tuples. Three grouping passes:
   - **Model-level:** Group by `(manufacturer, model, category, zone_type)` where model is not null.
   - **Manufacturer-level:** Group by `(manufacturer, NULL, category, zone_type)` across all models.
   - **Construction-level:** Group by `(hull_material, hull_construction, category, zone_type)` — stored as cross-manufacturer patterns with `manufacturer=NULL`.

3. **Threshold:** Groups with <3 reports are discarded.

4. **Severity:** Mode (most frequent value) of severity across all issues in the group.

5. **Onset calculation:** Median of `boat_age_months` across all issues, converted to years. Null if fewer than 3 issues have `boat_age_months`.

6. **Confidence:**
   ```
   confidence = min(1.0, report_count / 10) × mean(report.reliability for reports in group)
   ```

7. **Description:** Most frequent `description` string from the issues in the group (mode).

8. **Materials/Construction:** Collect unique `hull_material` and `hull_construction` values from the reports in the group.

9. **Positive patterns:** Same logic applied to `positives` from reports. Stored with `is_positive=True`.

10. **Idempotent:** Each run deletes all existing `CommunityPattern` rows and recreates from scratch.

### Return Value

```python
@dataclass
class AggregationResult:
    patterns_created: int
    reports_processed: int
    reports_skipped: int       # reliability < 0.3
    groups_below_threshold: int # had <3 reports
```

---

## 4. Community Analysis Module

**Location:** `backend/app/services/analysis/community.py`

Standalone pure-function module following the exact pattern of all 11 existing modules.

```python
BOAT_CLASS_DEFAULTS = {
    "small_sail":    {"max_patterns": 15, "min_confidence": 0.4,
                      "severity_weights": {"critical": 25, "major": 15, "minor": 5, "cosmetic": 2}},
    "cruising_sail": {"max_patterns": 20, "min_confidence": 0.3,
                      "severity_weights": {"critical": 25, "major": 15, "minor": 5, "cosmetic": 2}},
    "large_motor":   {"max_patterns": 20, "min_confidence": 0.3,
                      "severity_weights": {"critical": 25, "major": 15, "minor": 5, "cosmetic": 2}},
    "superyacht":    {"max_patterns": 25, "min_confidence": 0.2,
                      "severity_weights": {"critical": 25, "major": 15, "minor": 5, "cosmetic": 2}},
}

def run_community_analysis(
    community_patterns: list[dict],
    zones: list[dict],
    boat_class: str = "cruising_sail",
    config_overrides: dict | None = None,
) -> dict:
```

### Skip Logic

```python
if not community_patterns:
    return {"available": False, "reason": "Keine Community-Daten verfügbar."}
```

### Sub-Scores

| Sub-Score | Range | Logic |
|-----------|-------|-------|
| `known_issues_score` | 0–100 | Start at 100, subtract `severity_weight × relevance × confidence` per negative pattern. Floor at 0. |
| `positive_reputation_score` | 0–100 | Start at 50 (neutral), add points per positive pattern. Cap at 100. |
| `data_coverage_score` | 0–100 | `min(100, len(patterns) / max_patterns × 100)`. More data = higher confidence in assessment. |

### Overall Score

```python
overall_score = (
    known_issues_score * 0.50 +
    positive_reputation_score * 0.30 +
    data_coverage_score * 0.20
)
```

### Warnings

Each pattern with `severity ∈ {"critical", "major"}` and `confidence ≥ min_confidence` generates a warning:

```python
{
    "code": "COMMUNITY_KNOWN_ISSUE",
    "severity": "critical" if pattern["severity"] == "critical" else "warning",
    "zone": pattern["zone_type"],
    "message": f"⚠️ COMMUNITY: {pattern['description']} ({pattern['report_count']} Berichte)",
    "source": "community",
    "confidence": "community",
}
```

### Suggestions

For each warning, a suggestion is generated:
```python
{
    "code": "COMMUNITY_CHECK_RECOMMENDATION",
    "zone": pattern["zone_type"],
    "message": f"Prüfen Sie {ZONE_LABELS[pattern['zone_type']]} besonders sorgfältig — "
               f"bekanntes Problem bei vergleichbaren Booten "
               f"(typisch nach {pattern['typical_onset_years']:.0f} Jahren).",
    "priority": "high" if pattern["severity"] == "critical" else "medium",
    "source": "community",
}
```

### Confidence Level

New confidence level: `"community"` — sits between `documented` and `benchmark` in the hierarchy. All community findings carry this confidence.

### Return Dict

Standard module return format:
```python
{
    "module": "community",
    "available": True,
    "overall_score": float,
    "sub_scores": {
        "known_issues": {"score": float, "label": "Bekannte Probleme", "details": [...]},
        "positive_reputation": {"score": float, "label": "Positive Erfahrungen", "details": [...]},
        "data_coverage": {"score": float, "label": "Datenabdeckung", "details": [...]},
    },
    "warnings": [...],
    "suggestions": [...],
    "metrics": {
        "total_patterns_found": int,
        "negative_patterns": int,
        "positive_patterns": int,
        "most_common_category": str,
        "earliest_typical_onset_years": float | None,
    },
    "confidence": "community",
}
```

---

## 5. Orchestrator & BoatDNA Resolver Integration

### Orchestrator Changes

In `backend/app/services/analysis/orchestrator.py`:

1. Before Tier 1 dispatch, call `CommunityKnowledgeEngine.get_relevant_patterns()` and `get_positive_patterns()`.
2. Add `community` module to Tier 1 (parallel, no dependencies).
3. Pass combined patterns as `community_patterns` parameter.

```python
# In run_full_analysis():
engine = CommunityKnowledgeEngine(db)
community_patterns = await engine.get_relevant_patterns(dna, manufacturer, model)
community_positives = await engine.get_positive_patterns(dna, manufacturer, model)
all_community = community_patterns + community_positives

# Tier 1 becomes:
tier1 = await asyncio.gather(
    run_module("ergonomics", context),
    run_module("volume", context),
    run_module("emotional", context),
    run_module("compliance", context),
    run_module("community", context, community_patterns=all_community),
)
```

### BoatDNA Resolver Changes

In `backend/app/services/boat_dna_resolver.py`:

1. Add `BOAT_CLASS_DEFAULTS` import from `community` module.
2. Add `_resolve_community(dna)` method — returns config overrides based on DNA:
   - `min_confidence`: lower for superyacht tier (more patterns relevant)
   - `max_patterns`: higher for longer boats and complex builds
3. Add `"community"` weight to `_resolve_overall_weights(dna)`:
   - Default weight: 0.05 (low — community data is supplementary)
   - Increase to 0.08 for boats with `production_type == "mass_production"` (more community data likely available)
   - Increase to 0.10 when manufacturer is known and has many reports

### Score Fusion

In `backend/app/services/analysis/score_fusion.py`:

Add community module weight: `{"structured": 1.0, "visual": 0.0}` — purely data-driven, no visual component.

---

## 6. API Endpoints

**Location:** `backend/app/api/routes/community.py`

### Reports

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/api/v1/community/reports` | Required | Create a community report |
| `GET` | `/api/v1/community/reports` | Required | List reports (filters: manufacturer, model, category, hull_material) |
| `GET` | `/api/v1/community/reports/{id}` | Required | Get single report |

### Patterns

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET` | `/api/v1/community/patterns` | Required | List patterns (filters: manufacturer, model, hull_material, zone_type, is_positive) |
| `GET` | `/api/v1/community/patterns/{id}` | Required | Get pattern with linked report IDs |

### Aggregation

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `POST` | `/api/v1/community/aggregate` | Admin | Trigger batch aggregation, returns AggregationResult |

### Relevance Query

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| `GET` | `/api/v1/community/relevant` | Required | Get relevant patterns for a boat (query params: manufacturer, model, boat_class, hull_material, hull_construction, propulsion) |

---

## 7. Pydantic Schemas

**Location:** `backend/app/schemas/schemas.py` (additions)

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

class CommunityReportResponse(CommunityReportCreate):
    id: int
    created_at: datetime
    updated_at: datetime | None = None
    model_config = {"from_attributes": True}

class CommunityPatternResponse(BaseModel):
    id: int
    created_at: datetime
    manufacturer: str | None = None
    model: str | None = None
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
    model_config = {"from_attributes": True}

class AggregationResultResponse(BaseModel):
    patterns_created: int
    reports_processed: int
    reports_skipped: int
    groups_below_threshold: int
```

---

## 8. Seed Data

**Location:** `backend/app/db/seed.py` — new `seed_community_data()` function.

15–20 realistic reports based on well-known yacht issues:

1. **Bavaria 38 — Osmose** (5 reports, grp_solid, hand_layup, 5–8 years onset)
2. **Bavaria 38 — Rumpf/Deck-Verschraubung lockert** (4 reports, 5–8 years)
3. **Hanse 415 — Relingstützen lockern** (3 reports, 3–5 years)
4. **Hanse 415 — Galley-Arbeitsplatten splittern** (3 reports, 12–18 months)
5. **Hallberg-Rassy 40 — Positive: Kielstruktur** (3 reports, positive)
6. **Generic GRP hand_layup — Print-through** (4 reports, cross-manufacturer)
7. **Generic aluminium — Galvanische Korrosion** (3 reports, cross-manufacturer)
8. **Generic teak deck — Caulking-Probleme** (3 reports, cross-manufacturer)
9. **Jeanneau Sun Odyssey — Chainplate-Risse** (3 reports, 8–12 years)
10. **Bavaria allgemein — Positive: Preis-Leistung** (3 reports, positive)

After seeding reports, `seed_community_data()` calls `CommunityPatternAggregator.aggregate()` to create patterns automatically.

---

## 9. File Structure

### New Files

| File | Purpose | ~Lines |
|------|---------|--------|
| `backend/app/services/community/__init__.py` | Package init | 5 |
| `backend/app/services/community/engine.py` | CommunityKnowledgeEngine | ~150 |
| `backend/app/services/community/aggregator.py` | CommunityPatternAggregator | ~200 |
| `backend/app/services/analysis/community.py` | Analysis module (pure function) | ~250 |
| `backend/app/api/routes/community.py` | API endpoints | ~150 |
| `backend/tests/test_community.py` | Engine + Aggregator tests | ~250 |
| `backend/tests/test_community_analysis.py` | Analysis module tests | ~200 |

### Modified Files

| File | Change |
|------|--------|
| `backend/app/models/models.py` | +CommunityReport, +CommunityPattern models (~60 lines) |
| `backend/app/schemas/schemas.py` | +6 Pydantic schemas (~80 lines) |
| `backend/app/main.py` | +1 router registration line |
| `backend/app/services/analysis/orchestrator.py` | +community module dispatch in Tier 1 (~15 lines) |
| `backend/app/services/analysis/score_fusion.py` | +community weight entry (~2 lines) |
| `backend/app/services/boat_dna_resolver.py` | +_resolve_community(), +community in overall_weights (~40 lines) |
| `backend/app/db/seed.py` | +seed_community_data() (~150 lines) |
| `backend/tests/conftest.py` | +make_community_report(), +make_community_pattern() (~30 lines) |

### Untouched

All 11 existing analysis modules remain completely unchanged. Zero regression risk.

---

## 10. Testing Strategy

### Unit Tests — Engine (`test_community.py`)

- `test_exact_model_match` — Bavaria 38 patterns found with relevance 1.0
- `test_manufacturer_wide_match` — Bavaria patterns (no model) found with relevance 0.8
- `test_construction_method_match` — GRP hand_layup patterns found with relevance 0.6
- `test_material_match` — GRP patterns found with relevance 0.4
- `test_zone_category_match` — Generic deck patterns found with relevance 0.3
- `test_deduplication` — Same pattern from multiple levels appears only once (highest relevance wins)
- `test_max_results` — Results capped at max_results
- `test_empty_database` — Returns empty list, no error
- `test_positive_patterns` — Only returns is_positive=True patterns

### Unit Tests — Aggregator (`test_community.py`)

- `test_basic_aggregation` — 3+ reports → pattern created
- `test_below_threshold` — 2 reports → no pattern
- `test_severity_mode` — Most frequent severity wins
- `test_onset_median` — Correct median calculation
- `test_confidence_formula` — Confidence = min(1, count/10) × mean(reliability)
- `test_low_reliability_skipped` — Reports with reliability < 0.3 excluded
- `test_idempotent` — Running twice produces same result
- `test_positive_patterns_aggregated` — Positive findings also aggregated
- `test_construction_level_grouping` — Cross-manufacturer patterns created

### Unit Tests — Analysis Module (`test_community_analysis.py`)

- `test_no_patterns_unavailable` — Empty patterns → available=False
- `test_known_issues_scoring` — Critical patterns reduce score more than minor
- `test_positive_reputation_scoring` — Positive patterns increase score
- `test_data_coverage_scoring` — More patterns → higher coverage score
- `test_warnings_generated` — Critical/major patterns become warnings
- `test_suggestions_generated` — Each warning gets a suggestion
- `test_min_confidence_filter` — Low-confidence patterns filtered by config
- `test_overall_score_weights` — 50% issues + 30% positive + 20% coverage
- `test_config_overrides` — Custom config via boat_class_defaults
- `test_metrics` — Correct metrics in output

### Integration Tests

- `test_orchestrator_with_community` — Full analysis run includes community module
- `test_boat_dna_resolver_community` — Resolver produces community config overrides
- `test_seed_data_aggregation` — Seed data produces expected patterns
