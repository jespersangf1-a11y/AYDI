# AYDI Phase 1 — Full Implementation Design

## Overview

AYDI (AI Yacht Design Intelligence) is a domain-specific analysis platform for yacht shipyards. It analyzes existing yacht layout designs and provides structured feedback on ergonomics, spatial efficiency, and storage. Boat-class-specific evaluation logic is the core differentiator.

Phase 1 implements the complete foundation: backend API, two analysis modules (ergonomics + volume/storage), DXF import pipeline, frontend with project creation UI, Docker infrastructure, and comprehensive tests.

## Architecture

```
┌──────────────┐     ┌──────────────────┐     ┌────────────┐
│   Frontend   │────▶│  FastAPI Backend  │────▶│ PostgreSQL │
│  React + TS  │     │   Python 3.12     │     │    16      │
│  Vite + TW   │     │                  │     │            │
└──────────────┘     │  ┌────────────┐  │     └────────────┘
                     │  │  Analysis   │  │
                     │  │  Modules    │  │
                     │  │ (pure fn)   │  │
                     │  └────────────┘  │
                     │  ┌────────────┐  │
                     │  │ DXF Parser │  │
                     │  │ (ezdxf)    │  │
                     │  └────────────┘  │
                     └──────────────────┘
```

## 1. Data Model

### Project
| Field | Type | Notes |
|-------|------|-------|
| id | UUID | PK, server-generated |
| name | String(200) | required |
| description | Text | optional |
| boat_class | Enum | small_sail, cruising_sail, large_motor, superyacht |
| length_m | Float | hull length in meters |
| beam_m | Float | hull beam in meters |
| status | Enum | draft, active, review, archived (default: draft) |
| created_at | DateTime | auto |
| updated_at | DateTime | auto on update |

### Layout
| Field | Type | Notes |
|-------|------|-------|
| id | UUID | PK |
| project_id | UUID FK | references Project |
| name | String(200) | required |
| version | String(50) | e.g. "v1.0" |
| file_path | String | optional, for DXF source |
| file_type | String(20) | "json" or "dxf" |
| zones | JSON | array of zone objects |
| passages | JSON | array of passage objects |
| deck_height_mm | Integer | default 2100 |
| created_at | DateTime | auto |
| updated_at | DateTime | auto |

### Zone (JSON structure within Layout.zones)
```json
{
  "name": "salon",
  "zone_type": "salon",
  "polygon": [[0, 0], [3000, 0], [3000, 2500], [0, 2500]],
  "is_crew_area": false,
  "is_guest_area": true,
  "visibility_angle": null
}
```
`visibility_angle` (float|null): only relevant for helm zones (degrees of forward visibility). Defaults to boat-class default if null.
zone_type values: cabin, pantry, helm, engine, storage, cockpit, salon, head

### Passage (JSON structure within Layout.passages)
```json
{
  "from_zone": "salon",
  "to_zone": "pantry",
  "width_mm": 750,
  "is_primary": true
}
```

### AnalysisResult
| Field | Type | Notes |
|-------|------|-------|
| id | UUID | PK |
| project_id | UUID FK | references Project |
| layout_id | UUID FK | references Layout |
| module | String(50) | "ergonomics", "volume_storage" |
| overall_score | Float | 0-100 |
| sub_scores | JSON | dict of sub-analysis scores |
| warnings | JSON | array of warning objects |
| suggestions | JSON | array of suggestion strings |
| metrics | JSON | raw metric data |
| config_used | JSON | thresholds/weights applied |
| created_at | DateTime | auto |

### Zone / Passage ORM Models
Defined but not actively used in Phase 1. Exist for future normalization.

## 1b. Pydantic Schemas (request/response)

File: `backend/app/schemas/schemas.py` — Pydantic v2 with `model_config = ConfigDict(from_attributes=True)`.

```python
# Enums
class BoatClass(str, Enum): small_sail, cruising_sail, large_motor, superyacht
class ProjectStatus(str, Enum): draft, active, review, archived

# Project
class ProjectCreate(BaseModel):
    name: str
    description: str | None = None
    boat_class: BoatClass
    length_m: float
    beam_m: float

class ProjectUpdate(BaseModel):  # all optional
    name: str | None = None
    description: str | None = None
    boat_class: BoatClass | None = None
    length_m: float | None = None
    beam_m: float | None = None
    status: ProjectStatus | None = None

class ProjectResponse(BaseModel):
    id: UUID
    name: str
    description: str | None
    boat_class: BoatClass
    length_m: float
    beam_m: float
    status: ProjectStatus
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

# Zone / Passage (for JSON validation within Layout)
class ZoneData(BaseModel):
    name: str
    zone_type: str  # cabin|pantry|helm|engine|storage|cockpit|salon|head
    polygon: list[list[float]]  # [[x,y], ...] in mm
    is_crew_area: bool = False
    is_guest_area: bool = False
    visibility_angle: float | None = None  # degrees, for helm zones

class PassageData(BaseModel):
    from_zone: str
    to_zone: str
    width_mm: float
    is_primary: bool = True

# Layout
class LayoutCreate(BaseModel):
    name: str
    version: str = "v1.0"
    zones: list[ZoneData]
    passages: list[PassageData]
    deck_height_mm: int = 2100

class LayoutResponse(BaseModel):
    id: UUID
    project_id: UUID
    name: str
    version: str
    file_path: str | None
    file_type: str | None
    zones: list[ZoneData]
    passages: list[PassageData]
    deck_height_mm: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

# Analysis
class AnalysisRequest(BaseModel):
    layout_id: UUID
    module: str  # "ergonomics" | "volume_storage"

class WarningData(BaseModel):
    severity: str  # "critical" | "warning" | "info"
    message: str   # German
    suggestion: str  # German

class AnalysisResponse(BaseModel):
    id: UUID
    project_id: UUID
    layout_id: UUID
    module: str
    overall_score: float
    sub_scores: dict[str, float]
    warnings: list[WarningData]
    suggestions: list[str]
    metrics: dict
    config_used: dict
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

# DXF Import
class DxfImportResponse(BaseModel):
    zones: list[ZoneData]
    passages: list[PassageData]
    warnings: list[str]  # parse warnings

# Error
class ErrorResponse(BaseModel):
    detail: str
    errors: list[str] | None = None
```

## 1c. Database Session & Config

**`backend/app/db/database.py`:**
- Creates `AsyncEngine` via `create_async_engine(settings.DATABASE_URL)`
- Creates `async_sessionmaker` bound to engine
- Provides `async def get_db() -> AsyncGenerator[AsyncSession, None]` as FastAPI dependency

**`backend/app/core/config.py`:**
```python
class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql+asyncpg://aydi:aydi@localhost:5432/aydi"
    CORS_ORIGINS: list[str] = ["http://localhost:5173"]
    model_config = SettingsConfigDict(env_file=".env")
```

**Design decisions:**
- All FastAPI route handlers are `async def`
- All DB access uses `AsyncSession` via `Depends(get_db)`
- Analysis modules are synchronous pure functions (CPU-bound, no IO) — called directly from async routes
- Seed data: `backend/app/db/seed.py` is a standalone async script run via `python -m app.db.seed`
- No pagination in Phase 1 (explicit decision — dataset size is small)

## 1d. API-to-Module Bridge

The analysis route in `layouts.py` handles the orchestration:
1. Receives `AnalysisRequest` (layout_id, module)
2. Loads `Layout` from DB via `AsyncSession`
3. Loads `Project` to get `boat_class`
4. Extracts `zones` and `passages` from Layout JSON fields
5. Calls the pure-function module: `run_{module}_analysis(zones, passages, boat_class)`
6. Creates `AnalysisResult` ORM object from the returned dict
7. Saves to DB, returns `AnalysisResponse`

This keeps analysis modules free of DB concerns.

## 2. API Endpoints

All prefixed with `/api/v1/`. Analysis endpoints live in `layouts.py` (not a separate file).

### Projects
- `GET /projects` — list all, optional `?status=active`
- `POST /projects/` — create (body: name, boat_class, length_m, beam_m, description?)
- `GET /projects/{id}` — get by ID
- `PATCH /projects/{id}` — partial update
- `DELETE /projects/{id}` — delete (cascades layouts + results)

### Layouts
- `GET /projects/{id}/layouts` — list project layouts
- `POST /projects/{id}/layouts` — create (body: name, version, zones, passages, deck_height_mm?)
- `GET /projects/{id}/layouts/{lid}` — get specific layout
- `POST /projects/{id}/layouts/import-dxf` — multipart DXF upload, returns parsed layout for review

### Analysis
- `POST /projects/{id}/analyze` — trigger (body: layout_id, module)
- `GET /projects/{id}/analyses` — list results, optional `?module=ergonomics`

### System
- `GET /health` — returns `{"status": "healthy"}`
- `GET /docs` — Swagger UI (auto by FastAPI)

## 3. Ergonomics Analysis Module

File: `backend/app/services/analysis/ergonomics.py`

### BOAT_CLASS_DEFAULTS
| Parameter | small_sail | cruising_sail | large_motor | superyacht |
|-----------|-----------|--------------|-------------|-----------|
| min_passage_width_mm | 600 | 650 | 750 | 900 |
| critical_passage_width_mm | 450 | 500 | 550 | 650 |
| max_steps_cockpit_pantry | 8 | 10 | 12 | 15 |
| min_helm_area_sqm | 1.5 | 2.0 | 3.0 | 5.0 |
| min_helm_visibility_deg | 225 | 225 | 240 | 270 |
| crew_guest_separation | false | false | true | true |

### Weights (per boat class)
| Sub-analysis | small_sail | cruising_sail | large_motor | superyacht |
|-------------|-----------|--------------|-------------|-----------|
| passage_width | 0.30 | 0.25 | 0.20 | 0.15 |
| path_efficiency | 0.20 | 0.20 | 0.20 | 0.20 |
| crew_guest_separation | 0.05 | 0.10 | 0.25 | 0.35 |
| accessibility | 0.30 | 0.25 | 0.20 | 0.15 |
| helm_ergonomics | 0.15 | 0.20 | 0.15 | 0.15 |

### Sub-analyses

1. **analyze_passage_widths(passages, config)** → score, warnings, metrics
   - Score: 100 if all passages >= min_width; linear penalty per passage below
   - Critical warning if any passage < critical_width
   - Warning if passage < min_width but >= critical_width

2. **analyze_path_efficiency(zones, passages, config)** → score, warnings, metrics
   - Build adjacency graph from passages
   - BFS: cockpit→pantry path length vs max_steps
   - Detect isolated zones (no passages)
   - Detect disconnected subgraphs
   - Score penalty for each issue

3. **analyze_crew_guest_separation(zones, passages, config)** → score, warnings, metrics
   - Only scored if config.crew_guest_separation is true
   - Find passages connecting crew and guest areas
   - Each shared passage = penalty
   - Returns 100 if separation not required

4. **analyze_accessibility(zones, passages, config)** → score, warnings, metrics
   - Required zones: engine, pantry, helm, head
   - Check each exists and is reachable via BFS from any other zone
   - Penalty per missing or unreachable critical zone

5. **analyze_helm_ergonomics(zones, config)** → score, warnings, metrics
   - Find helm zone, calculate area from polygon (Shoelace formula)
   - Check area >= min_helm_area_sqm
   - Check visibility_angle if provided (field in zone data or default)
   - Score based on area ratio + visibility ratio

### Orchestrator
`run_ergonomics_analysis(zones, passages, boat_class, config_overrides=None) → dict`
- Merges config_overrides into BOAT_CLASS_DEFAULTS[boat_class]
- Runs all 5 sub-analyses independently (try/except each)
- Combines scores using boat-class weights
- Sorts warnings by severity (critical → warning → info)
- Returns: module, overall_score, sub_scores, warnings, suggestions, metrics, config_used

## 4. Volume/Storage Analysis Module

File: `backend/app/services/analysis/volume_storage.py`

### BOAT_CLASS_DEFAULTS
| Parameter | small_sail | cruising_sail | large_motor | superyacht |
|-----------|-----------|--------------|-------------|-----------|
| min_storage_ratio | 0.15 | 0.12 | 0.10 | 0.08 |
| ideal_storage_ratio | 0.22 | 0.18 | 0.15 | 0.12 |
| min_storage_zones | 2 | 3 | 4 | 6 |
| max_distribution_imbalance | 0.6 | 0.5 | 0.4 | 0.3 |

### Weights
| Sub-analysis | small_sail | cruising_sail | large_motor | superyacht |
|-------------|-----------|--------------|-------------|-----------|
| storage_ratio | 0.40 | 0.35 | 0.30 | 0.30 |
| storage_distribution | 0.30 | 0.35 | 0.40 | 0.40 |
| storage_accessibility | 0.30 | 0.30 | 0.30 | 0.30 |

### Sub-analyses

1. **analyze_storage_ratio(zones, config)** → score, warnings, metrics
   - Calculate total area of storage zones vs total area of all zones (Shoelace formula)
   - Score: 100 if ratio >= ideal, linear scale down to 0 if ratio = 0
   - Warning if ratio < min_storage_ratio
   - Critical if no storage zones exist

2. **analyze_storage_distribution(zones, config)** → score, warnings, metrics
   - Calculate centroid of each storage zone
   - Measure spread relative to overall layout bounding box
   - Score penalizes clustering (all storage in one area)
   - Warning if distribution imbalance > max_distribution_imbalance
   - Info if fewer than min_storage_zones

3. **analyze_storage_accessibility(zones, passages, config)** → score, warnings, metrics
   - For each storage zone, check if reachable via passages from main living areas
   - Score based on percentage of accessible storage zones
   - Warning for each unreachable storage zone

### Orchestrator
`run_volume_storage_analysis(zones, passages, boat_class, config_overrides=None) → dict`
Same pattern as ergonomics orchestrator.

## 5. DXF Import Pipeline

File: `backend/app/services/dxf/parser.py`

### Layer Mapping (default, configurable)
```python
DEFAULT_LAYER_MAP = {
    "CABIN": "cabin",
    "PANTRY": "pantry",
    "GALLEY": "pantry",
    "HELM": "helm",
    "ENGINE": "engine",
    "STORAGE": "storage",
    "COCKPIT": "cockpit",
    "SALON": "salon",
    "SALOON": "salon",
    "HEAD": "head",
    "WC": "head",
    "BATHROOM": "head",
}
```

### Processing Steps
1. Read DXF file with ezdxf
2. Iterate modelspace entities
3. For each layer matching the layer map:
   - Extract closed LWPOLYLINE/POLYLINE entities
   - Convert coordinates to mm (handle unit detection from DXF header)
   - Create zone dict with name (layer + index), zone_type, polygon
4. Extract passages from "PASSAGE" layer (lines/polylines with width attribute)
5. If no explicit passages found, auto-detect: find zone pairs sharing edges within tolerance
6. Return parsed zones + passages as a dict (not saved yet — user reviews first)

### API Integration
- `POST /api/v1/projects/{id}/layouts/import-dxf`
- Accepts multipart form: file (DXF), name, version, layer_map (optional JSON override)
- Returns parsed layout preview (zones + passages)
- User then calls `POST /api/v1/projects/{id}/layouts` with the reviewed data to save

### Error Handling
- Invalid DXF format → 400 with details
- No zones found → 400 with warning
- Unsupported entity types → logged as info, skipped

## 6. Frontend

### Component Tree
```
App
├── AppShell (sidebar + main area)
│   ├── Sidebar
│   │   ├── Logo
│   │   ├── NavItem (Dashboard)
│   │   └── NavItem (Projekte)
│   └── MainContent
│       ├── Dashboard (project list)
│       ├── ProjectDetail
│       │   ├── ProjectInfo
│       │   ├── LayoutList
│       │   ├── AnalysisResults
│       │   │   ├── ScoreGauge
│       │   │   ├── SubScoreBars
│       │   │   └── WarningList
│       │   └── LayoutViewer (SVG)
│       └── ProjectCreate (form)
```

### Design Tokens (Tailwind)
```
navy-50 through navy-950 — dark blues for backgrounds/text
ocean-50 through ocean-950 — accent blues for interactive elements
```

### Project Creation Form
Fields:
- Name (text, required)
- Beschreibung (textarea, optional)
- Bootsklasse (select: Kleine Segelyacht / Fahrtensegler / Große Motoryacht / Superyacht)
- Länge in Metern (number, required)
- Breite in Metern (number, required)
- Layout-Upload (file input: .json or .dxf, optional)

On submit: POST to create project, optionally POST layout or import-dxf.

### Routing (client-side state, no router library)
Views: `dashboard` | `project-detail` | `project-create`
Managed via useState in App.tsx.

### API Client
`src/services/api.ts` — typed functions for every endpoint, using fetch.

### LayoutViewer (SVG rendering)
- Renders zone polygons as SVG `<polygon>` elements
- Coordinate mapping: mm → viewBox with auto-fit to container
- Zones colored by zone_type (consistent color map)
- Zone names displayed as labels at centroid
- Passages rendered as lines between zone centroids with width indicator
- Hover tooltip showing zone name, type, area
- No editing — view-only in Phase 1

### All UI text in German.

## 7. Infrastructure

### docker-compose.yml
```yaml
services:
  db:
    image: postgres:16-alpine
    environment: POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD
    volumes: pgdata
    ports: 5432
  backend:
    build: docker/Dockerfile.backend
    depends_on: db
    environment: DATABASE_URL
    ports: 8000
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000
  frontend:
    build: docker/Dockerfile.frontend
    depends_on: backend
    ports: 5173
```

### Dockerfile.backend
- Python 3.12-slim base
- Copy requirements.txt, pip install
- Copy app code
- WORKDIR /app/backend

### Dockerfile.frontend
- Node 20-alpine base
- Copy package.json, npm install
- Copy src code
- npm run build → serve with nginx or npm run preview

### .env.example
```
DATABASE_URL=postgresql+asyncpg://aydi:aydi@db:5432/aydi
POSTGRES_DB=aydi
POSTGRES_USER=aydi
POSTGRES_PASSWORD=aydi
CORS_ORIGINS=http://localhost:5173
```

## 8. Seed Data

Three projects as specified:
1. **Meridian 40 Cruiser** (12.2m cruising_sail) — full layout with 9 zones, 8 passages, intentionally suboptimal passages
2. **Nordic 28 Weekender** (8.5m small_sail) — draft, no layout
3. **Avalon 65 Flybridge** (19.8m large_motor) — draft, no layout

## 9. Tests

### test_ergonomics.py (19+ tests)
- Test each sub-analysis independently
- Test with perfect layout → score near 100
- Test with problematic layout → low scores + correct warnings
- Test boat class comparison: same layout, different classes → different scores
- Test config_overrides
- Test edge cases: empty zones, no passages, missing helm

### test_volume_storage.py
- Test storage ratio calculation
- Test distribution scoring
- Test accessibility
- Test boat class differences
- Test edge: no storage zones → critical warning

### test_dxf_parser.py
- Test with valid DXF file (create minimal test DXF in fixture)
- Test layer mapping
- Test coordinate extraction
- Test passage detection
- Test invalid file handling
- Test custom layer map override

## 10. File Inventory

```
backend/
  app/
    __init__.py
    main.py
    api/
      __init__.py
      routes/
        __init__.py
        projects.py
        layouts.py
    core/
      __init__.py
      config.py
    models/
      __init__.py
      models.py
    schemas/
      __init__.py
      schemas.py
    services/
      __init__.py
      analysis/
        __init__.py
        ergonomics.py
        volume_storage.py
      dxf/
        __init__.py
        parser.py
    db/
      __init__.py
      database.py
      seed.py
  migrations/
    env.py
    script.py.mako
    versions/
      (initial migration)
  tests/
    __init__.py
    conftest.py
    test_ergonomics.py
    test_volume_storage.py
    test_dxf_parser.py
    fixtures/
      test_layout.dxf
  alembic.ini
  requirements.txt

frontend/
  src/
    components/
      analysis/
        ScoreGauge.tsx
        SubScoreBars.tsx
        WarningList.tsx
        LayoutViewer.tsx
      dashboard/
        Dashboard.tsx
        ProjectDetail.tsx
        ProjectCreate.tsx
      layout/
        AppShell.tsx
    services/
      api.ts
    types/
      index.ts
    styles/
      globals.css
    App.tsx
    main.tsx
  public/
    index.html
  package.json
  vite.config.ts
  tailwind.config.js
  tsconfig.json

docker/
  Dockerfile.backend
  Dockerfile.frontend
docker-compose.yml
.env.example
CLAUDE.md
```
