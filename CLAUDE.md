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

## Product Vision: Four Functional Pillars

AYDI serves four distinct user missions. Every feature should trace to at least one pillar. The four praxistest personas (`praxistest_runner.py`) each represent one pillar and should exercise differentiated journeys — not identical flows.

| # | Pillar | Who | What they get | Persona | Tier |
|---|--------|-----|---------------|---------|------|
| 1 | **Knowledge base / lexicon** | Anyone maintaining or repairing a boat | Standalone reference for repairs, materials, components, failure patterns — the 260-doc corpus, user-facing (browse, search, read) | — (public funnel) | Public read; full depth is a PRO selling point (`KNOWLEDGE_BASE_FULL`) |
| 2 | **Buyer's assistant** | Prospective boat buyers | Known weaknesses of a specific make/model/year, age-expected problems, photo-based condition assessment | Marc (Käufer) | FREE basic / PRO report |
| 3 | **Owner refit & customization** | Owners improving/customizing their boat | Model the boat, play through changes (cosmetic → structural), before/after scoring | Kai (Bootseigner) | PRO |
| 4 | **Professional design** | Designers & shipyard teams | New-model design work: construction, interior/exterior, team collaboration, versioned iterations | Elena (Designerin), Sarah (Werftleiterin) | PRO / ENTERPRISE |

Pillars 1–2 are the marketing funnel into 3–4. Pillar-readiness (mapped against code, 2026-07): pillar 1 has the strongest substance (corpus + API) — its user-facing wiring is the first unlock; pillar 2 is wiring work over existing backend assets (community patterns, manufacturer weak-spot DB, condition vision prompts); pillar 3 lacks the edit/what-if loop; pillar 4 (authoring, team model, ISO-12215 dimensioning, CAD export) is the largest build.

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

Zielbild: alle drei speisen ein einheitliches Scoring pro Zone und Modul.

**Ist-Zustand:** Der Orchestrator fährt **A und C** — C hängt am Modul `service_patterns`, das die
`service_reports` aus dem Kontext bekommt und deren Freitext auswertet (`_derive_text_severity`).
**B läuft daneben, nicht darin:** die visuelle Analyse wird ausschließlich über die Bild-Routen
angestoßen (`app/api/routes/images.py` → `app/services/visual/analyzer.analyze_image`), nicht vom
Orchestrator. Ihre Ergebnisse werden folglich **nicht** mit den strukturierten Modulnoten
verschmolzen: die Verschmelzung liegt fertig, aber unaufgerufen in `score_fusion.py` — siehe
**Score Fusion Weights — NICHT VERDRAHTET**.

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

**Fusion-derived codes — NICHT VERDRAHTET (Frontend-only, kein Backend emittiert sie).**
`frontend/src/components/analysis/ConfidenceBadge.tsx` und `frontend/src/types/index.ts` definieren
Badges für `measured+visual`, `visual_only` und `discrepant`. **Kein Python-Code erzeugt diese Werte.**
`score_fusion.py` vergibt bewusst *nur* kanonische Codes aus der Tabelle oben — der Kommentar in
`_fuse_both()` sagt es ausdrücklich: „avoids the non-canonical `measured+visual`". Bei Uneinigkeit
gibt es kein `discrepant`, sondern die strukturierte Confidence plus `needs_review: True` und einen
`disagreement`-Block. Diese drei Badges sind toter Code, bis ein Backend sie sendet.

| Level | Code | Gemeint war | Ist-Zustand |
|-------|------|-------------|-------------|
| Measured + Visual | `measured+visual` | Beide Quellen einig, fusioniert | Badge existiert im Frontend; Backend sendet stattdessen die Confidence der dominanten Quelle |
| Visual only | `visual_only` | Keine Strukturdaten, Bild trägt das Ergebnis | Badge existiert im Frontend; Backend sendet die Visual-Confidence selbst (`visual_high` …) |
| Discrepant | `discrepant` | Abweichung > Schwelle → geflaggt, **nicht gemittelt** | Badge existiert im Frontend; Backend liefert `needs_review: True` + `disagreement` bei der strukturierten Confidence |

Per-finding visual confidence returned by the Vision prompts is the AI's own German self-assessment (`hoch`/`mittel`/`niedrig`; materials: `sicher`/`wahrscheinlich`/`vermutet`) — the frontend normalizes these to hide low-confidence findings by default. This is distinct from the canonical `visual_*` gatekeeper codes above.

### Reliability Rules (Non-Negotiable)

1. Never present uncertain results as facts. Confidence badge on every finding.
2. AI must say "I don't know." Prompts enable "nicht beurteilbar".
3. Cross-validate when possible. CAD vs photo discrepancy → flag, don't average.
4. Human-in-the-loop for CRITICAL findings: "Befund prüfen" not "Mangel bestätigt".
5. Version-track AI assessments. Store model version.

### Module Skip Logic

A module returns `{"available": false, "reason": "..."}` when it cannot produce a reliable result.

### Fehlgeschlagene Teilanalysen (`app/services/analysis/subscore.py`)

Jedes Analysemodul zerlegt seine Arbeit in Teilanalysen und gewichtet sie zur Modulnote. Bricht eine
Teilanalyse mit einer Exception ab, darf sie **nicht** mit 0.0 in den gewichteten Mittelwert
einfließen — sonst wird ein interner Fehler dem Nutzer als schlechte Messung am Boot präsentiert.

`aggregate_subscores(sub_scores, weights, failed, default)` nimmt die fehlgeschlagenen Namen aus
**Zähler und Nenner** und normiert über die verbleibenden Gewichte. Fällt alles aus, liefert es
`None`. Regeln für die Module:
- Jedes Modul sammelt die Ausfälle in `_failed_subs` und gibt sie als **`degraded_subanalyses`**
  (sortierte Liste) im Ergebnis zurück — sichtbar, nicht stillschweigend.
- Ist `aggregate_subscores` `None` (alle Teilanalysen ausgefallen), meldet das Modul
  `{"available": false, …}` statt einer erfundenen Note.
- Verdrahtet in 11 der 12 Analysemodule: `brand_dna`, `compliance`, `cost`, `emotional`,
  `ergonomics`, `market`, `materials`, `production`, `service_patterns`, `structural`,
  `volume_storage`. **`community` nutzt es nicht** — es hat keine gewichteten Teilanalysen und
  meldet ohne Community-Daten direkt `available: false`.

Das ist die Anwendung der Grundregel „lieber *nicht beurteilbar* als geraten" auf interne Fehler.

---

## Analysis Orchestrator

When user triggers "Vollanalyse", modules execute in dependency order. Quelle der Wahrheit ist
`EXECUTION_TIERS` in `app/services/analysis/orchestrator.py` — **12 Module**, nicht 11
(`community` gehört dazu):

```
Tier 1 (parallel): ergonomics, volume_storage, emotional, compliance, community
Tier 2 (parallel): production, materials, structural
Tier 3 (sequential): cost (needs materials, structural, production)
Tier 4 (parallel): service_patterns, brand_dna, market (needs cost)
```

**Modulschlüssel ist `volume_storage`, nicht `volume`** — überall: `EXECUTION_TIERS`,
`_get_module_runners()`, `MODULE_FEATURE_MAP`, `FUSION_WEIGHTS`. (Nur der *Feature*-Enum-Name
heißt `Feature.MODULE_VOLUME`.)

Der Orchestrator führt **keine** visuelle Analyse aus und **keine** Score-Fusion: in
`orchestrator.py` kommt weder `visual` noch `fusion` vor. Er ruft ausschließlich die
strukturierten Modul-Runner auf und aggregiert deren `overall_score` in `_compute_overall_score`.

---

## Score Fusion Weights — NICHT VERDRAHTET

`app/services/analysis/score_fusion.py` existiert und ist getestet
(`tests/test_score_fusion.py`, `tests/test_qa_error_handling.py`), aber der String `score_fusion`
kommt **in keiner einzigen Datei unter `app/` vor** — es gibt keinen Aufrufer, nicht einmal einen
auskommentierten. Die geplante Verschmelzung von Pipeline A und Pipeline B findet im Produktivpfad
also nicht statt. Wer sie aktiviert, ruft `fuse_all_modules(structured, visual, boat_class)` auf
und lässt das Ergebnis in `_compute_overall_score` einfließen; der Test
`test_claude_md_spec_matches_code.py::test_score_fusion_has_no_caller_in_app_and_spec_says_so`
schlägt dann fehl und erinnert daran, diesen Abschnitt umzuschreiben.

`FUSION_WEIGHTS` (Ist-Zustand im Code, 12 Einträge):

| Module | Structured | Visual |
|--------|-----------|--------|
| ergonomics | 0.75 | 0.25 |
| volume_storage | 0.85 | 0.15 |
| emotional | 0.25 | 0.75 |
| compliance | 0.95 | 0.05 |
| production | 0.55 | 0.45 |
| materials | 0.35 | 0.65 |
| structural | 0.95 | 0.05 |
| cost | 1.00 | 0.00 |
| service_patterns | 0.65 | 0.35 |
| brand_dna | 0.35 | 0.65 |
| market | 0.60 | 0.40 |
| community | 1.00 | 0.00 |

Unbekannte Module fallen auf `DEFAULT_WEIGHTS = (0.50, 0.50)`. Das visuelle Gewicht wird zusätzlich
mit `CONFIDENCE_DISCOUNT` gedämpft (`high` 1.0, `medium` 0.8, `low` 0.5, `insufficient` 0.0) und
danach renormiert. Ab `DISAGREEMENT_THRESHOLD = 25.0` Punkten Abstand wird nicht gemischt, sondern
der strukturierte Score mit `needs_review: True` zurückgegeben.

---

## Professional Designer-Level Module Enhancements

### Ergonomics — Professional Features
- **Heel angle impact** (sailboats): effective_width = passage_width × cos(heel_angle). Der Winkel kommt aus `BOAT_CLASS_DEFAULTS["heel_angle_deg"]` je Bootsklasse; konfiguriert sind **0°, 12°, 15°, 20°, 25°** (0° = Motorklassen, dann kurzschließt `analyze_heel_impact` mit 100 Punkten). Es gibt keinen Mehrwinkel-Durchlauf — pro Analyse genau ein Winkel.
- **Morning circulation**: simulate N persons waking 07:00–09:00, each cabin→head→pantry→cockpit. Identify bottleneck passages.
- **Access complexity scoring**: direct (0 panels, 100pts), panel_1 (1 panel, 80pts), panel_2 (60pts), floor_lift (50pts), furniture_move (30pts), major_disassembly (10pts).

### Volume — Professional Features
`volume_storage.py` hat genau fünf Teilanalysen: `utilization`, `storage_ratio`,
`storage_distribution`, `storage_accessibility`, `furniture_ratio`.
- **Deadspace mapping** (Rumpf-Hüllvolumen minus zugewiesenes Zonenvolumen): **geplant, nicht implementiert.** Kein `deadspace`/`dead_space` im Backend.
- **Tank capacity vs range**: **geplant, nicht implementiert** im Analysemodul. Eine Reichweitenrechnung existiert nur als Wissensfunktion in `app/services/knowledge/yacht_systems_propulsion.py` (`endurance_hours = fuel_tank_capacity_liters / fuel_consumption_l_per_h`) — sie hängt an keinem Analysepfad.

### Emotional — Professional Features
- **Sightline ray tracing** (`analyze_sightline_rays`): 72 Strahlen (alle 5°) vom **Polygon-Schwerpunkt** jeder bewertbaren Zone. Gemessen wird die **Strahllänge bis zur Zonen-Polygonkante** (`_ray_polygon_distance`, mm → m), nicht eine Trefferklassifikation. Score = Ø Strahllänge relativ zu `min_sightline_m` (100 bei Erreichen), danach ±10 Punkte je nachdem, ob `window_area_pct` über dem Zielwert oder unter dessen Hälfte liegt. Ausgabe: `zones_evaluated`, `avg_ray_length_m`, `num_rays`.
  Die frühere Beschreibung („Strahlen von Eingangspunkten, Treffer klassifiziert als window=1.0 / passage=0.5 / wall=0.0, Openness-Ratio") beschreibt ein anderes Verfahren und steht **nicht** im Code.

### Compliance — CE Documentation Support
- **Escape hatch dimensions**: ISO 12216 min 400×520mm for emergency escape.
- **Cockpit drain capacity** (`analyze_cockpit_drain_capacity`): geprüft wird ein **Volumenstrom**, kein Volumen.
  `cockpit_volume_liters = Polygonfläche_m² × cockpit_depth_mm` (Standardtiefe 300 mm, per Zonen-Property `cockpit_depth_mm` überschreibbar);
  `required_drain_capacity_lps = cockpit_volume_liters / drain_time_s` mit `DEFAULT_COCKPIT_DRAIN_TIME_S = 300` (ISO 11812: Schnellentleerung in ~5 min), per `config["cockpit_drain_time_s"]` je Bootsklasse überschreibbar.
  Verglichen wird das gegen die Zonen-Property `drain_capacity_lps`; fehlt sie, wird die Zone **nicht** bewertet (Hinweis statt Note).
  ⚠️ Die alte Fassung `drain_capacity = cockpit_volume × 2` ist im Code ausdrücklich verworfen: sie hielt einen Literwert gegen eine l/s-Schwelle, mischte also Dimensionen und forderte ~600× den physikalischen Wert. Nicht wieder einführen.
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
- **FREE** — Level-1 quick analysis + a subset of modules (`ergonomics`, `volume_storage`, `emotional`, `market`) with `estimated` results.
- **PRO** — Level-2 full analysis, all modules, full knowledge base, visual analysis, CAD import, collaboration, versioning, multi-language, imperial units, benchmark DB.
- **ENTERPRISE (Werft)** — Pro + fleet management, API access, multi-tenancy, custom reports, priority support.

The **orchestrator** filters modules by tier: `get_allowed_modules(context.tier)`; disallowed modules are recorded in `tier_gated`, not executed. `context.tier` is populated from the authenticated user. Use `require_feature` / `require_module` at route boundaries.

**Effective tier (pillar 4, stage 2):** a user's governing tier is `max(personal tier, org tiers)` — `resolve_effective_tier` (permissions.py), resolved per request and attached as the transient `user.effective_tier` in `get_current_user` and `authenticate_websocket`. **Every tier gate reads `effective_tier(user)`** (the `getattr(user,'effective_tier',user.tier)` accessor), never `user.tier` directly — an ENTERPRISE org thereby unlocks its features for all members. `org.tier` defaults to `free` and is changeable **only** by a platform admin (`POST /admin/orgs/{id}/tier`, `require_role('admin')`) — never self-service (that would be privilege escalation). There is no billing system; tier is admin-provisioned.

### Teams & Sharing (pillar 4 — load-bearing, enforced in code)
Two layers, additive (GitHub org + repo-collaborators pattern):
- **Project sharing (stage 1):** `ProjectMember(project_id, user_id, role viewer/editor)`. Owner derived from `Project.user_id`.
- **Organizations (stage 2):** `Organization` (name, tier), `OrganizationMember(org_role owner/admin/member)`, `Project.org_id` (nullable, SET NULL on org delete — never destroys member work). Org membership grants a base project role via the central chokepoint: **org member → `editor`, org owner/admin → `owner`** on the org's projects.
- **Central access resolver:** `get_accessible_project(project_id, user, db, min_role)` (permissions.py) → effective role = max(owner-if-creator, ProjectMember role, org-derived role); **404 for no access** (no existence leak), **403 for insufficient role**. **11 der 19 Routenmodule** unter `app/api/routes/` delegieren an ihn: `costs`, `images`, `import_cad`, `layouts`, `materials`, `organizations`, `projects`, `reports`, `service_reports`, `structural_items`, `versions`. Die übrigen 8 greifen nicht auf ein einzelnes fremdes Projekt zu: `auth`, `community`, `competitors`, `knowledge`, `quick_analysis` (Level 1, unauthentifiziert) sind nicht projekt-scoped; `benchmarks` aggregiert klassenweit über alle Layouts; `invitations` handelt auf dem Einladungs-Token (Zugriff wird dort erst *erteilt*); `collaborate` gatet über `authenticate_websocket` + `require_role`. **Das ist Ist-Zustand, kein Freibrief**: neue projektbezogene Endpunkte gehen durch den Resolver. `require_org(org_id, user, db, min_role)` is the org-scope analog (member<admin<owner).
- **Invitations:** unified `Invitation` table (project XOR org, keyed by normalized email). Creation is **anti-enumeration** (identical response whether or not the email has an account — no user lookup in the response path); acceptance is always explicit (never auto-join). Legacy `POST /projects/{id}/members` is frozen/deprecated — the invitation flow is the path.
- **Brand-reference visibility** is org-scoped via the single predicate in `app/core/brand_visibility.py` — used by BOTH the CRUD endpoints AND the `brand_dna` analysis loader (they must not drift, or the analysis leaks foreign private brand DNA).
- **Live collaboration** (`/ws/collaborate/{layout_id}`): PRO+ (effective tier); org-derived roles may join; viewers cannot broadcast edits (server-enforced). Broadcast-only — nothing persisted; the client must never present ephemeral state as durable.

**DB note:** production is PostgreSQL (enforces FK actions). Dev/tests run SQLite with `PRAGMA foreign_keys=ON` (set globally in `db/database.py`) so SET NULL / CASCADE behave identically; `delete_organization` also cleans up explicitly for engine-independence.

### Security Headers
`SecurityHeadersMiddleware` in `app/core/middleware.py`, registriert in der zentralen
`add_middleware`-Registrierung. Setzt per `setdefault` auf **jede** Antwort:
`X-Content-Type-Options: nosniff`, `X-Frame-Options: DENY`, `Referrer-Policy: no-referrer`,
`Content-Security-Policy: default-src 'none'; frame-ancestors 'none'`,
`Cross-Origin-Resource-Policy: same-site`. `Strict-Transport-Security` kommt **nur** dazu, wenn
`COOKIE_SECURE` gesetzt ist — sonst würde eine lokale HTTP-Entwicklungsumgebung sich aussperren.
Der wichtigste ist `nosniff`: Nutzertext wird in JSON-Antworten zurückgespiegelt, und ohne den
Header darf ein Browser eine solche Antwort als HTML interpretieren. Die CSP ist bewusst maximal
eng — die API liefert nur Daten, kein aktives Markup.

### Zonentypen (`app/core/validation.py`)
- `VALID_ZONE_TYPES` (47 Werte) und die in `app/core/domains.py` (`DOMAIN_CONFIGS`) referenzierten
  Zonentypen sind **deckungsgleich** — verifizierbar per Mengendifferenz in beide Richtungen. Sie
  dürfen nicht auseinanderlaufen: ein Zonentyp ohne Domäne fällt still aus der Domänen-Abdeckung,
  das Ergebnis wirkt vollständig, ist es aber nicht.
- `ZONE_TYPE_ALIASES` (37 Einträge) mappt gebräuchliche Synonyme auf den kanonischen Typ, u.a.
  `galley|kitchen|kombüse|küche → pantry`, `salon|main_cabin → saloon`, `wc|toilet|bad → head`,
  `v_berth|vorschiff → forepeak`, `locker|lazarette → storage`. Alle Alias-Ziele liegen in
  `VALID_ZONE_TYPES`.
- `normalize_zone_type(zone_type)` ist der Eingang: trimmt, lowercased, löst den Alias auf.
  Unbekannte Werte kommen **unverändert (getrimmt/lowercased) zurück**, damit der Aufrufer noch
  warnen kann — nicht schweigend verworfen.

### Boat Classes (13, not 4)
`BoatClass` enum (`schemas/schemas.py`) has **13** values — everything calibrates on these:
`small_sail, cruising_sail, racing_sail, daysailer, motorsailer, catamaran_sail, catamaran_motor, small_motor, large_motor, sport_cruiser, trawler, explorer, superyacht`.
Every module ships `BOAT_CLASS_DEFAULTS` keyed on all 13. **Historical design docs under `docs/superpowers/` that describe only 4 classes are archival, not current** — do not derive enums/tests from them.

### Internationalization
`app/core/i18n.py`. Locales: **DE (default)**, EN, ES, FR (`Locale` enum). Request-scoped via `contextvars`; set in middleware. `t(key, **kwargs)` for translations; locale-aware number/currency/date formatting. Unknown locale → falls back to DE. German remains the canonical UX language; other locales are additive.

### Knowledge System
- **261** nummerierte Recherchedokumente liegen auf der Platte, **260** davon lädt der Loader — in **32** Kategorien, zusammen **850.228 Zeilen** (flach unter `app/services/knowledge/`, Namensschema `NN_MM_slug.md`; die 32 Kategorien sind die `NN`-Präfixe 01–32). Loader: `app/services/knowledge/markdown_knowledge_loader.py`.
- Die eine nicht geladene Datei ist `24_05_pumpen_sanitaer_clean.md` — eine ältere Zwischenkopie. Sie wird **absichtlich** übersprungen: `_find_markdown_files()` filtert die `BACKUP_SUFFIXES = ("_clean.md", "_backup.md", "_old.md", "_tmp.md")`. Das ist kein Fehler, sondern die Denylist.
- Slug collisions are stored under a `{category}_{subcategory}_{slug}` composite key (never silently overwritten); die erste Datei behält den nackten Slug, die kollidierende bekommt den Kompositschlüssel plus `logger.warning`.
- `KNOWLEDGE_INDEX.py` is the completeness reference; its category counts must track the real corpus (**261 auf Platte / 260 geladen / 32 Kategorien**).
- Analysis modules enrich results from this corpus (`markdown:*` sources) — see `compliance.py`, `materials.py`, `structural.py`, `production.py`.

### Deployment
See `DEPLOY.md` and `INTEGRATION_ANWEISUNG.md`. Docker Compose (`docker-compose.yml`,
`docker/Dockerfile.backend`, `docker/Dockerfile.frontend`, `docker/nginx.conf`), Render-Blueprint
(`render.yaml`), Railway (`railway.toml`). **Production checklist must set `SECRET_KEY` and
`COOKIE_SECURE=true`** or the app refuses to start (see AuthN above) — `render.yaml` setzt dafür
`ENVIRONMENT=production` fest, damit der Guard im Deployment überhaupt greift.
`docker/entrypoint.sh` fährt `alembic upgrade head` vor uvicorn und bricht bei
Migrationsfehlern ab (`set -e`): nie Traffic gegen ein unbekanntes Schema.

---

## Tech Stack

Maßgeblich sind `backend/requirements.txt` und `frontend/package.json` — nicht diese Liste.

### Backend (`backend/requirements.txt`, gepinnt)
- Python 3.12 (`docker/Dockerfile.backend`: `python:3.12-slim`; `pyproject.toml` ruff `target-version = "py312"`). Lokal läuft die Suite auch unter neueren 3.x.
- FastAPI 0.115, uvicorn 0.34, Pydantic 2.10 + pydantic-settings, SQLAlchemy 2.0.36 (asyncio), asyncpg / aiosqlite, Alembic 1.14, PostgreSQL (prod)
- PyJWT 2.10, passlib[bcrypt] 1.7.4 mit **bcrypt == 4.0.1** (höher bricht passlib)
- anthropic 0.42 (Claude Vision), ezdxf 1.4.3, numpy 2.2.1, trimesh 4.5.3, Pillow 11.1, httpx 0.28
- **Kein shapely** (entfernt: kein Import in `app/` oder `tests/`, zog aber die native GEOS-Bibliothek in jedes Image). Wieder aufnehmen, sobald echte Polygon-Geometrie (Verschneidung, Puffer) gebraucht wird.
- pytest 8.3 + pytest-asyncio 0.25
- **Kein SciPy.** Weder in `requirements.txt` noch als Import im App-Code; `import scipy` schlägt in dieser Umgebung fehl. (Treffer im `venv/` stammen aus optionalen Pfaden von trimesh/numpy/fontTools und sind keine AYDI-Abhängigkeit.)

### Frontend (`frontend/package.json`)
- React 18.3 + TypeScript 5.7 (strict), Vite 6, Tailwind CSS 3.4 (navy-*, ocean-*)
- three 0.170 / @react-three/fiber 8 + drei 9, recharts 2.15, lucide-react 0.468, react-router-dom 6.30, dompurify 3.4
- Schriften (`frontend/index.html` + `tailwind.config.js`): **Playfair Display** (`font-serif`), **Inter** (`font-sans`), **JetBrains Mono** (`font-mono`), via Google Fonts geladen. *DM Sans und Plus Jakarta Sans kommen im Projekt nicht vor.*
- Kein `import.meta.env`, keine `VITE_*`-Variablen: das Frontend ruft relativ `/api/v1` auf, im Dev leitet der Vite-Proxy `/api` und `/health` auf `http://localhost:8000` (inkl. `ws: true` für die Live-Kollaboration).

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

## Getting Started (ein neuer Durchlauf wird hiermit arbeitsfähig)

Alle Befehle unten sind an diesem Repo verifiziert. Repo-Wurzel = `AYDI/`.

### Voraussetzungen
- **Python 3.12** (Zielversion, siehe Tech Stack; neuere 3.x laufen lokal ebenfalls)
- **Node 20+** (verifiziert unter Node 24 / npm 11; `package.json` deklariert kein `engines`-Feld)
- Optional: Docker + Docker Compose (nur für den Postgres-/Container-Weg)

### Backend einrichten und starten
```bash
cd backend
pip install -r requirements.txt          # inkl. pytest — keine separate requirements-dev.txt
PYTHONPATH=. alembic upgrade head        # Schema auf Stand bringen (7 Revisionen: 000 → 006)
PYTHONPATH=. uvicorn app.main:app --reload
```
`PYTHONPATH=.` ist bei **allen** Backend-Kommandos nötig — es gibt kein installiertes Package.
`alembic.ini` zeigt auf `script_location = migrations`; die dort eingetragene `sqlalchemy.url`
wird von `migrations/env.py` zur Laufzeit durch `settings.DATABASE_URL` **überschrieben**, die
`.ini` ist also nur Fallback. Ohne gesetzte `DATABASE_URL` landet alles in der lokalen SQLite
`backend/aydi.db`.

### Frontend
```bash
cd frontend
npm install
npm run dev      # Vite auf :5173, proxyt /api und /health nach :8000
npm run build    # tsc && vite build — der tsc-Lauf ist Teil des Builds
npm run preview
```

### Docker-Weg (Postgres statt SQLite)
```bash
cp .env.example .env       # DATABASE_URL, POSTGRES_*, CORS_ORIGINS
docker compose up -d
docker compose exec backend alembic upgrade head   # im Dev-Compose bewusst manuell
```
Das Produktions-Image fährt die Migration selbst: `docker/entrypoint.sh` macht
`alembic upgrade head` und danach `exec uvicorn` — schlägt die Migration fehl, startet der
Container gar nicht.

### Environment-Variablen
Gelesen von `app/core/config.py` (`Settings`, `env_file=".env"` relativ zum Arbeitsverzeichnis):

| Variable | Default | Bedeutung |
|---|---|---|
| `ENVIRONMENT` | `development` | `production` **schärft den Boot-Guard** (siehe unten) |
| `DATABASE_URL` | `sqlite+aiosqlite:///./aydi.db` | prod: `postgresql+asyncpg://…` |
| `SECRET_KEY` | repo-öffentlicher Default | JWT-Signatur — in prod zwingend eigener Wert |
| `COOKIE_SECURE` | `False` | in prod zwingend `true` |
| `AUTH_COOKIE_ONLY` | `False` | `true` schaltet den Bearer-Header-Fallback ab |
| `COOKIE_DOMAIN` | `None` | |
| `CORS_ORIGINS` | `["http://localhost:5173"]` | JSON-Array |
| `ANTHROPIC_API_KEY` | `None` | ohne Key keine Pipeline B |
| `ANTHROPIC_MODEL` | `claude-opus-5` | Aktuelle IDs tragen **kein** Datumssuffix; `claude-sonnet-4-20250514` ist zurückgezogen (404) |
| `VISUAL_ANALYSIS_TIMEOUT_SEC` | `30` | |
| `MAX_IMAGE_SIZE_MB` / `UPLOAD_DIR` | `20` / `uploads` | |
| `ACCESS_TOKEN_EXPIRE_MINUTES` / `REFRESH_TOKEN_EXPIRE_DAYS` | `60` / `7` | |
| `TRUST_PROXY_HEADERS` | `False` | nur hinter vertrauenswürdigem Proxy auf `true` |
| `LOG_LEVEL` / `LOG_JSON` / `DATABASE_POOL_SIZE` | `INFO` / `False` / `10` | |

Der Boot-Guard `_enforce_production_security` wirft beim Start, wenn `ENVIRONMENT=production` und
`SECRET_KEY` noch der Default ist **oder** `COOKIE_SECURE` False. `render.yaml` setzt
`ENVIRONMENT=production`, `COOKIE_SECURE=true` und `AUTH_COOKIE_ONLY=true` fest und lässt
`SECRET_KEY`/`DATABASE_URL`/`ANTHROPIC_API_KEY` auf `sync: false` (Dashboard) — der Guard ist damit
im Deployment tatsächlich scharf und fällt „fail closed" aus, statt still mit dem Default-Key zu
starten.

### Tests und Praxistest
```bash
cd backend
PYTHONPATH=. python -m pytest tests/ -q        # volle Suite (~76 s)
PYTHONPATH=. python -m pytest tests/ -v        # ausführlich
PYTHONPATH=. python praxistest_full.py         # 4 Personas, Gruppen A–F, 123 Checks
PYTHONPATH=. python praxistest_runner.py       # nur Gruppe A (schreibt praxis_state.json)
```
Die Praxistests legen DB und Ergebnisse unter `backend/.praxistest/` ab
(`PRAXISTEST_OUT_DIR` überschreibt das) und setzen `DATABASE_URL` selbst — sie fassen die
Entwicklungs-DB nicht an. `pyproject.toml` setzt `asyncio_mode = "auto"`; `@pytest.mark.asyncio`
ist daher nicht nötig.
