# CLAUDE.md – AYDI v6 — Definitive Engineering Specification

## What This Project Is

AYDI (AI Yacht Design Intelligence) is a domain-specific analysis platform for yacht design. It operates across three input modalities (structured data, visual data, text data) and two user levels (public quick-analysis, professional design tool). It diagnoses, scores, and suggests improvements by combining structural measurement, visual perception analysis, and accumulated industry experience.

**Critical design principles:**
- Every result carries a confidence level. Estimates are never presented as facts.
- The system prefers "nicht beurteilbar" (cannot assess) over a guess.
- Boat class calibrates everything: standards for an 8m sailboat differ fundamentally from a 30m motor yacht.
- German for all user-facing text. English for all code.
- Pydantic v2: `model_config = {"from_attributes": True}` — NEVER `class Config`.

---

## Two User Levels

**Level 1 (Schnellanalyse)** — No login. Enter public specs (length, beam, cabin count...) and/or upload photos. Get instant estimated analysis. This is the marketing funnel and data collection mechanism.

**Level 2 (Profi-Werkzeug)** — Authenticated. Full CAD import, material database, structural data, cost data, service reports, collaboration, versioning. Deep professional analysis with measured confidence.

Both levels use the same analysis engine. Level 1 infers missing data from boat-class templates. Level 2 uses exact measurements. Every result shows which level it came from.

Level 2 is the authenticated boundary and maps onto subscription tiers (FREE/PRO/ENTERPRISE) with server-side module gating — see **Platform Architecture → Authentication** and **→ Subscription Tiers** below.

---

## Three Analysis Pipelines

```
Pipeline A — Structured (CAD, specs, databases)
  Engine: Python analysis modules
  Confidence: "measured" (Level 2) or "estimated" (Level 1)

Pipeline B — Visual (photos, renderings)
  Engine: Claude Vision API with domain-specific prompts
  Confidence: "visual_high", "visual_medium", "visual_low", "visual_insufficient"

Pipeline C — Text (service reports, feedback)
  Engine: NLP extraction + pattern matching
  Confidence: "documented"
```

All three feed into a unified scoring framework per zone and per module.

---

## Domain Knowledge: Yacht Construction Standards

### Regulatory Framework

**CE Marking (EU Recreational Craft Directive 2013/53/EU):**
Mandatory for boats 2.5–24m sold in the EU. Assigns design categories:
- **Category A (Ocean)**: Wind force >8 Beaufort, significant wave height >4m
- **Category B (Offshore)**: Wind force ≤8, wave height ≤4m
- **Category C (Inshore)**: Wind force ≤6, wave height ≤2m
- **Category D (Sheltered)**: Wind force ≤4, wave height ≤0.3m

Layout implications: Category A requires more emergency exits, larger escape hatches, higher companionway sills, more secure stowage for heavy items.

**Key ISO Standards for Layout Design:**
| Standard | Scope | Layout Impact |
|----------|-------|--------------|
| ISO 12217 (2015/2022) | Stability | Weight distribution, tank placement, CG limits |
| ISO 9094 (2015) | Fire protection | Min distances engine↔combustibles, escape routes |
| ISO 15085 (2003) | Man-overboard prevention | Railing heights, deck edge protection |
| ISO 11812 (2020) | Cockpits | Cockpit volume, drain sizing, sill heights |
| ISO 12216 (2020) | Windows/hatches | Opening sizes, emergency exit dimensions |
| ISO 10133/13297 | Electrical | Panel access, cable routing, battery ventilation |
| ISO 12215 (2019, Parts 1–9) | Hull construction & scantlings | Laminate/plate thickness, stiffener spacing, panel dimensioning — **basis of the `structural` module** |
| ISO 12215-8 | Rudders | Rudder force & stock scantling |
| ISO 12215-9 | Keels & appendages | Keel-attachment loads, ballast-fixing safety factors |

> **Note:** ISO 12217 is *stability* (weight/CG), NOT structure. Structural scantlings are ISO 12215. Do not cite 12217 for laminate/scantling questions (a recurring confusion in source material).

### Build Quality Standards by Boat Class

**Production Sailboat (8–14m, €80k–€300k):**
- Joinery tolerances: 2–3mm gaps acceptable
- Gelcoat: minor orange peel acceptable, no runs
- Teak deck: machine-laid acceptable, caulking seams 4–6mm
- Interior: veneer over plywood standard, solid wood edge banding

**Semi-Custom Cruiser (12–20m, €300k–€1.5M):**
- Joinery tolerances: 1–2mm max gaps, consistent throughout
- Gelcoat: smooth, no visible defects from 1m distance
- Teak deck: hand-laid preferred, caulking seams 3–5mm
- Interior: solid wood or high-grade veneer, no visible fasteners

**Custom/Superyacht (18m+, €1.5M+):**
- Joinery tolerances: <1mm, no visible gaps
- Paint/gelcoat: mirror finish, zero defects
- Teak deck: hand-selected planks, grain-matched, caulking seams 3–4mm
- Interior: book-matched veneer, soft-close everything, marine-grade tinned cable

### Material Domain Knowledge

- **Teak**: Burma Grade A vs plantation. Issues: black staining, lifting, UV checking.
- **GFK/FRP**: Quality = laminate consistency, gelcoat 0.5-0.8mm. Issues: osmotic blistering, stress cracking.
- **Stainless 316L**: Must be 316L not 304 for salt water. Issues: tea staining, crevice corrosion.
- **Marine Plywood**: BS 1088 standard. Issues: delamination, wood movement, finish failure.
- **Marine Leather/Vinyl**: UV treated, mold resistant. Issues: UV fading, stitching failure, vinyl cracking.

---

## Confidence & Reliability Framework

| Level | Code | Meaning | Display |
|-------|------|---------|---------|
| Measured | `measured` | From exact CAD/database | Green badge |
| Calculated | `calculated` | Derived from measured | Green badge |
| Visual High | `visual_high` | Clear photo, unambiguous | Blue badge |
| Visual Medium | `visual_medium` | Decent photo, some uncertainty | Amber badge |
| Visual Low | `visual_low` | Poor photo or ambiguous | Hidden by default |
| Visual Insufficient | `visual_insufficient` | Cannot assess | Metadata only |
| Estimated | `estimated` | Inferred from specs/class averages | Gray badge |
| Benchmark | `benchmark` | From aggregated industry data | Gray badge |
| Documented | `documented` | From service reports/text | Blue badge |

**Fusion-derived codes** (emitted by `score_fusion.py` when combining structured + visual):

| Level | Code | Meaning | Display |
|-------|------|---------|---------|
| Measured + Visual | `measured+visual` | Both sources agree, fused | Green badge |
| Visual only | `visual_only` | No structured data, visual carried it | Amber badge |
| Discrepant | `discrepant` | Sources disagree > threshold → flagged, **not averaged** (returns structured score + `needs_review`) | Orange badge |

Per-finding visual confidence returned by the Vision prompts is the AI's own German self-assessment (`hoch`/`mittel`/`niedrig`; materials: `sicher`/`wahrscheinlich`/`vermutet`) — the frontend normalizes these to hide low-confidence findings by default. This is distinct from the canonical `visual_*` gatekeeper codes above.

### Reliability Rules (Non-Negotiable)

1. Never present uncertain results as facts. Confidence badge on every finding.
2. AI must say "I don't know." Prompts enable "nicht beurteilbar".
3. Cross-validate when possible. CAD vs photo discrepancy → flag, don't average.
4. Human-in-the-loop for CRITICAL findings: "Befund prüfen" not "Mangel bestätigt".
5. Version-track AI assessments. Store model version.

### Module Skip Logic

A module returns `{"available": false, "reason": "..."}` when it cannot produce a reliable result.

---

## Analysis Orchestrator

When user triggers "Vollanalyse", modules execute in dependency order:

```
Tier 1 (parallel): ergonomics, volume, emotional, compliance
Tier 2 (parallel): production, materials, structural + visual analysis
Tier 3 (sequential): cost (needs materials, structural, production)
Tier 4 (parallel): service_patterns, brand_dna, market (needs cost)
```

Score fusion combines structured + visual results per module.

---

## Score Fusion Weights

| Module | Structured | Visual |
|--------|-----------|--------|
| ergonomics | 0.75 | 0.25 |
| volume | 0.85 | 0.15 |
| emotional | 0.25 | 0.75 |
| compliance | 0.95 | 0.05 |
| production | 0.55 | 0.45 |
| materials | 0.35 | 0.65 |
| structural | 0.95 | 0.05 |
| cost | 1.00 | 0.00 |
| service_patterns | 0.65 | 0.35 |
| brand_dna | 0.35 | 0.65 |
| market | 0.60 | 0.40 |

---

## Professional Designer-Level Module Enhancements

### Ergonomics — Professional Features
- **Heel angle impact** (sailboats): effective_width = passage_width × cos(heel_angle). Standard angles: 0°, 15°, 25°.
- **Morning circulation**: simulate N persons waking 07:00–09:00, each cabin→head→pantry→cockpit. Identify bottleneck passages.
- **Access complexity scoring**: direct (0 panels, 100pts), panel_1 (1 panel, 80pts), panel_2 (60pts), floor_lift (50pts), furniture_move (30pts), major_disassembly (10pts).

### Volume — Professional Features
- **Deadspace mapping**: hull bounding volume minus assigned zone volume = wasted space.
- **Tank capacity vs range**: fuel/water tank volumes determine cruising range at given speed.

### Emotional — Professional Features
- **Sightline ray tracing**: 360° rays from entry points, classify hits (window=1.0, passage=0.5, wall=0.0), compute openness ratio.

### Compliance — CE Documentation Support
- **Escape hatch dimensions**: ISO 12216 min 400×520mm for emergency escape.
- **Cockpit drain capacity**: ISO 11812 drain_capacity = cockpit_volume × 2 (seconds).
- **Companionway sill heights**: Cat A=300mm, B=250mm, C=150mm, D=0mm. These are the CE **floor**; a per-boat-class override (`companionway_sill_mm`) may only make the requirement *stricter*, never fall below the category minimum (`compliance.py` uses `max(override, CE-floor)`).
- **Ventilation requirements**: engine room = max(0.05, engine_kw × 0.0003) m².

### Materials — Lifecycle Analysis
- **20-year lifecycle cost**: purchase + maintenance + replacements over 20 years.
- **UV exposure risk**: flag materials in high-UV zones (deck, south windows) without UV resistance.
- **Moisture risk mapping**: flag wood-based materials in head/pantry/engine without proper sealing.

### Structural — Loading Conditions
- **Loading conditions**: light_ship, full_departure, arrival, worst_case (asymmetric tanks).
- **Trim calculation**: longitudinal trim angle per loading condition. Flag >1° motor, >2° sail.

### Production — Manufacturing Analysis
- **Mold complexity scoring**: hull curvature, deck level changes, window count, hard chine vs round.
- **Flat panel ratio**: percentage of interior from flat panels. Target: >70% production, >50% semi-custom.

### Cost — Parametric Estimation
- **Parametric cost models**: base_cost_per_m × LOA with category breakdown per boat class.

---

## Platform Architecture

The analysis engine (above) runs inside a platform layer. These subsystems are load-bearing and enforced in code — treat them as spec, not incidental.

### Authentication & Authorization
- **AuthN**: JWT (HS256, PyJWT), `access_token` + `refresh_token`. Passwords hashed with **bcrypt** via passlib `CryptContext`. Core: `app/core/auth.py`, routes: `app/api/routes/auth.py`.
- **AuthZ — roles**: `admin`, `user`, `viewer` (`app/core/permissions.py`, `require_role(*roles)`). Admin-only endpoints (e.g. `/collaborate/sessions`) gate on this.
- **AuthZ — ownership**: mutating/reading resources verify the resource chains back to `user_id` (Layout → Project → user). Never trust a client-supplied owner.
- **`SECRET_KEY` is mandatory in production.** `config.py` refuses to boot (`_enforce_production_security`) if `ENVIRONMENT=production` and the secret is still the default, or if `COOKIE_SECURE` is False. Never ship the default secret. Startup logs a warning if the default is in use.
- **Two auth transports**: bearer token (Authorization header) and httpOnly cookie + CSRF token for mutating requests. Level 1 (Schnellanalyse) is unauthenticated; Level 2 is the authenticated boundary.

### Subscription Tiers (server-side gating)
`app/core/subscription.py`. Gating is enforced **server-side** — frontend hiding is never sufficient. Tiers are cumulative:
- **FREE** — Level-1 quick analysis + a subset of modules (ergonomics, volume, emotional, market) with `estimated` results.
- **PRO** — Level-2 full analysis, all modules, full knowledge base, visual analysis, CAD import, collaboration, versioning, multi-language, imperial units, benchmark DB.
- **ENTERPRISE (Werft)** — Pro + fleet management, API access, multi-tenancy, custom reports, priority support.

The **orchestrator** filters modules by tier: `get_allowed_modules(context.tier)`; disallowed modules are recorded in `tier_gated`, not executed. `context.tier` is populated from the authenticated user. Use `require_feature` / `require_module` at route boundaries.

### Boat Classes (13, not 4)
`BoatClass` enum (`schemas/schemas.py`) has **13** values — everything calibrates on these:
`small_sail, cruising_sail, racing_sail, daysailer, motorsailer, catamaran_sail, catamaran_motor, small_motor, large_motor, sport_cruiser, trawler, explorer, superyacht`.
Every module ships `BOAT_CLASS_DEFAULTS` keyed on all 13. **Historical design docs under `docs/superpowers/` that describe only 4 classes are archival, not current** — do not derive enums/tests from them.

### Internationalization
`app/core/i18n.py`. Locales: **DE (default)**, EN, ES, FR (`Locale` enum). Request-scoped via `contextvars`; set in middleware. `t(key, **kwargs)` for translations; locale-aware number/currency/date formatting. Unknown locale → falls back to DE. German remains the canonical UX language; other locales are additive.

### Knowledge System
- **252** numbered research documents across **31** categories under `app/services/knowledge/` (`NN_MM_slug.md`, ~840K lines total). Loaded by `markdown_knowledge_loader.py`.
- Slug collisions are stored under a `{category}_{subcategory}_{slug}` composite key (never silently overwritten).
- `KNOWLEDGE_INDEX.py` is the completeness reference; its category counts must track the real corpus (252/31).
- Analysis modules enrich results from this corpus (`markdown:*` sources) — see `compliance.py`, `materials.py`, `structural.py`, `production.py`.

### Deployment
See `DEPLOY.md` and `INTEGRATION_ANWEISUNG.md`. Docker Compose (`docker-compose.yml`, `docker/Dockerfile.backend`). **Production checklist must set `SECRET_KEY` and `COOKIE_SECURE=true`** or the app refuses to start (see AuthN above).

---

## Tech Stack

### Backend
- Python 3.12, FastAPI, PostgreSQL 16, SQLAlchemy 2.0 (async/asyncpg), Alembic, Pydantic v2
- Anthropic SDK (Claude Vision), ezdxf, trimesh, Shapely, NumPy, SciPy, Pillow
- pytest

### Frontend
- React 18 + TypeScript (strict), Vite 6, Tailwind CSS 3.4 (navy-*, ocean-*)
- Three.js / React Three Fiber, Recharts, Lucide React
- DM Sans, Plus Jakarta Sans, JetBrains Mono

---

## Conventions

- Routes: `/api/v1/`. Async everywhere. Pydantic v2 model_config.
- Analysis: pure functions, no DB, standardized return dict.
- Visual: always through VisualAnalyzer, never raw API calls. Prompts in `/prompts/`.
- Confidence badges on ALL results. LOW hidden by default.
- Every warning has a suggestion. Every finding has a location reference.
- German UX, English code. Coordinates: mm. Scores: 0-100. Costs: EUR.
- Tests: `PYTHONPATH=. pytest tests/ -v`

---

## Development Commands

```bash
docker compose up -d
cd backend && PYTHONPATH=. uvicorn app.main:app --reload
cd backend && PYTHONPATH=. pytest tests/ -v
cd frontend && npm run dev
```
