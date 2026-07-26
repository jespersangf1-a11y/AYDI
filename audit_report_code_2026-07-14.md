# Audit-Bericht: Code & Implementierung (Teilaudit 2 — Re-Audit Post-Fix)

Datum: 2026-07-14
Maßstab: Qualität, Spec-Konsistenz (CLAUDE.md) und funktionale Robustheit der AYDI-Codebasis.
Methodik: 9 Prüfbereiche (a–i) parallel gegen den **aktuellen** Code auditiert; jeder KRITISCH/HOCH-Befund adversariell gegen den echten Code gegenverifiziert (`CONFIRMED_OPEN` / `ALREADY_RESOLVED` / `NOT_A_DEFECT`). Audit-only — kein Code verändert.

> **Kontext:** Dies ist ein **Re-Audit nach der Fix-Phase**. Die ursprünglichen 4 KRITISCH + ~14 HOCH-Befunde (`audit_report_code.md`) wurden bereits behoben (SECRET_KEY-Boot-Guard, tote Visual-Pipeline, Auth/Ownership, Frontend-XSS/Confidence u.a.) und sind hier als **RESOLVED** bestätigt. Dieser Bericht dokumentiert den **verbleibenden** Befundstand — v.a. Punkte, die der erste Fix-Durchlauf nicht abdeckte, plus MITTEL/NIEDRIG.

---

## Gesamtzustand in fünf Sätzen

Die Kern-Sicherheitsfundamente sind nach der Fix-Phase solide: SECRET_KEY-Produktions-Boot-Guard, bcrypt+JWT, Cookie+CSRF, Rate-Limiting, robuste Bild-Upload-Validierung (Pillow-Inhaltsprüfung gegen Polyglots) und Prompt-Injection-Schutz (zone_type-Allowlist, nur numerische Kontext-Interpolation) sind vorhanden und korrekt — ebenso Retry/Circuit-Breaker, JSON-Parse-Fallback und Orchestrator-Fehlerisolierung. **Der rote Faden der verbleibenden Befunde ist nicht „kaputt", sondern „halb verdrahtet":** Fähigkeiten sind korrekt implementiert, aber im Live-Pfad nicht aktiv oder nur teilweise angeschlossen. Die vier gravierendsten Muster: (1) **Tier-Gating** ist nur im Orchestrator-Pfad aktiv — der Einzelmodul-Endpunkt `/analyze` und alle PRO-Feature-Routen (Visual, CAD-Import, Versionen, Benchmarks, Collaboration) sind ungegated → **Paywall-Bypass für FREE-Nutzer**; (2) die **13-Bootsklassen-Kalibrierung** ist an mehreren Kernstellen weiter nur 4-klassig (Vision-Prompts, OVERALL_WEIGHTS, BoatDNA, Report-Labels, i18n) — 9 Klassen fallen still auf „cruising_sail"; (3) die korrekte **Score-Fusion** (flag-statt-mitteln) ist in **keinem** Live-Pfad verdrahtet; (4) **brand_dna/market** fabrizieren weiter 50.0-Scores mit „measured"-Badge bei fehlenden Daten. Keine KRITISCH-Befunde mehr offen; die verbleibenden HOCH-Befunde sind konzentriert auf Tier-Gating, i18n-Reichweite, CAD-Import-Robustheit und Testabdeckung.

**Zahlen:** 9/9 Bereiche geprüft · ~48 OPEN-Befunde · davon **0 KRITISCH, ~13 HOCH** (14 KRITISCH/HOCH-Kandidaten verifiziert) · Rest MITTEL/NIEDRIG · mehrere frühere Fixes als RESOLVED bestätigt.

---

## Bereichsübergreifende Muster (die wertvollsten Befunde)

Diese vier Muster tauchen in mehreren Prüfbereichen auf — sie sind der eigentliche Kern:

### Muster CG-1 — Tier-Gating nur im Orchestrator, nicht an den Route-Grenzen (HOCH)
CLAUDE.md fordert explizit: *„Gating is enforced server-side … Use `require_feature` / `require_module` at route boundaries."* `require_feature`/`require_module` (core/subscription.py) werden aber **in keiner Route** aufgerufen (nur der Full-Analysis-Pfad reicht `tier` an den Orchestrator weiter). Gefunden in **e_api** und **f_security** (zwei Blickwinkel, gleiche Wurzel).
- `layouts.py` `run_analysis` (POST `/projects/{id}/analyze`, ~Z.298-359): kein `require_module` → FREE-Nutzer kann PRO-Module (structural, cost, materials, production, compliance, service_patterns, brand_dna, community) einzeln ausführen. **CONFIRMED_OPEN.**
- `images.py` (analyze/upload/batch, Z.207/275/365/477), `import_cad.py` (Z.62/99), `layouts.py` import-dxf (Z.124), `versions.py`, `benchmarks.py`, `community.py`, `collaborate.py`: alle nur `Depends(get_current_user)`, kein Feature-Gate. **CONFIRMED_OPEN.**
- Der frühere Fix (Orchestrator-Modulfilter via `get_allowed_modules`, `tier=_user.tier`) ist RESOLVED — deckt aber genau diese Standalone-Pfade nicht ab.

### Muster CG-2 — 13-Bootsklassen-Kalibrierung an Kernstellen weiter nur 4-klassig (HOCH)
CLAUDE.md: *„Boat class calibrates everything"* / *„13 values … everything calibrates on these … 4-class docs are archival."* Real fallen 9 Klassen still auf `cruising_sail` (Segelyacht) zurück — auch reine Motor-/Katamaran-/Racing-Klassen. Gefunden in **a_prompts, b_scoring, d_datamodel, e_api, g_i18n**:
- Vision-Prompts `BOAT_CLASS_CONTEXT` + `QUALITY_STANDARDS_BY_CLASS` + `SPATIAL_EXPECTATIONS_BY_CLASS` (alle 6 prompt-Dateien) = 4 Keys. **CONFIRMED_OPEN.**
- `orchestrator.py` `OVERALL_WEIGHTS` (Z.295-345) = 4 Keys → Motorklassen mit Segelgewichtung bewertet.
- `models/boat_dna.py` `_PRESETS`/`from_boat_class` (Z.89-195) = 4 (wirft ValueError für die 9; aktuell ohne Aufrufer → latent).
- `reports/pdf_generator.py` `BOAT_CLASS_LABELS` = 4; `i18n.py` boat_class-Keys für 5 nicht-existente Klassen, 5 echte fehlen.

### Muster CG-3 — Korrekt implementierte Fähigkeiten sind nicht ins Live-Pipeline verdrahtet (MITTEL)
Gefunden in **b_scoring** und **c_errors**: `score_fusion.py` (flag-statt-mitteln, `needs_review`, kanonische Fusion-Codes) ist korrekt + unit-getestet, wird aber **nirgends in `backend/app/` aufgerufen** — nur in Tests. `orchestrator.run_full_analysis` kombiniert visuelle Ergebnisse gar nicht (kein `visual_results`-Parameter, keine Fusionsstufe; `overall` nur aus strukturierten Scores). → Die gesamte Score-Fusion inkl. des früheren flag-statt-mitteln-Fixes und der Reliability-Rule-3-Transparenz (CAD-vs-Foto → flag) ist **im echten Analyselauf unerreichbar**. Ebenso: Reliability-Rule-4 („Befund prüfen") ist in i18n definiert, aber im Visual-Code nicht angewandt.

### Muster CG-4 — i18n nur an den Rändern; Produktkern ist hartcodiertes Deutsch (HOCH)
Gefunden in **g_i18n**: `core/i18n.py` ist sauber (4 Locales, ~200 Keys), aber nur in Middleware/Auth/Subscription verdrahtet. Alle **13 Analyse-Module** geben hartcodiertes Deutsch aus (`t()` wird nie aufgerufen; compliance.py allein ~161 Literale). Das **Frontend hat gar keine i18n** (keine Library, kein Umschalter, hartcodiertes `de-DE`). Das laut Spec als PRO zugesicherte multi-language ist damit praktisch nicht lieferbar. **CONFIRMED_OPEN.**

---

## Befunde nach Prüfbereich

### a) Vision-/AI-Prompts
- **[HOCH / M / OPEN]** Bootsklassen-Kalibrierung nur 4/13 (alle 6 prompt-Dateien; `.get(boat_class, ...['cruising_sail'])`). Siehe CG-2. **CONFIRMED_OPEN.** — `services/visual/prompts/*.py`
- **[HOCH / S / OPEN]** Build-Quality-Prompt gibt Selbsteinschätzung als `confidence_overall` aus, Gatekeeper liest nur `confidence` → KI-Sicherheit für interior_detail/exterior_detail immer Default 0.6; LOW/INSUFFICIENT-Gating greift dort nicht. **CONFIRMED_OPEN.** — `prompts/quality.py:156` vs `confidence.py:187`
- **[MITTEL / M / OPEN]** Keine Schema-/Range-Validierung nach JSON-Parse; Scores nicht auf 0–100 geklemmt (`spatial_score=150` propagiert). — `analyzer.py:_parse_json_response/_extract_score`
- **[MITTEL / M / OPEN]** Reliability-Rule 4 („Befund prüfen" statt „Mangel bestätigt") im Visual-Code nicht angewandt; i18n-Keys `finding.check_required`/`defect_confirmed` ungenutzt. — `analyzer.py`
- **[MITTEL / S / OPEN]** findings-Arrays (spatial/materials/exterior/helm) ohne per-Finding-Konfidenz und ohne Bild-Ortsangabe (Spec: „Confidence badge on ALL results / every finding has a location reference"). — `prompts/spatial.py:93-100` u.a.
- **[SAUBER]** Prompts stark yachtspezifisch, JSON gefordert, „nicht beurteilbar" aktiviert; Gatekeeper HIGH/MEDIUM/LOW/INSUFFICIENT mit `is_usable` korrekt.

### b) Scoring- & Fusionslogik
- **[MITTEL / S / OPEN]** `brand_dna` fabriziert `overall_score:50.0` + `confidence:"measured"` bei zu wenig Referenzmodellen statt `available:false` — **das in cost/materials/structural/service_patterns bereits gefixte Anti-Pattern, hier übersehen.** — `brand_dna.py:795-823`
- **[MITTEL / S / OPEN]** `market` identisch: 50.0 + "measured" bei zu wenig Wettbewerbern. — `market.py:888-916`
- **[MITTEL / M / OPEN]** `OVERALL_WEIGHTS` nur 4/13 Klassen (Motorklassen mit Segelgewichtung). Siehe CG-2. — `orchestrator.py:295-345,360`
- **[MITTEL / M / OPEN]** Score-Fusion nicht ins Live-Pipeline verdrahtet. Siehe CG-3. — `score_fusion.py` (gesamt)
- **[MITTEL / M / OPEN]** Unerklärte Magic Numbers: `structural.py:893 correction_factor=2.0` (verdoppelt Trimmwinkel, steuert TRIM_EXCESSIVE), `community.py:137-141` (0.50/0.30/0.20), `emotional.py:377/523`, `ergonomics.py:392`, `materials.py` Issue-Penalty.
- **[NIEDRIG / S / OPEN]** `service_patterns` hat in keiner `OVERALL_WEIGHTS`-Klasse ein Gewicht → Score dekorativ ohne Einfluss auf `overall_score`. — `orchestrator.py:295-345`
- **[NIEDRIG / M / OPEN]** Sub-Metrik-Fallback 50.0 statt „nicht beurteilbar" in einzelnen emotional/compliance-Teil-Analysen bei fehlenden Daten. — `emotional.py`, `compliance.py` (mehrere)
- **[SAUBER/RESOLVED]** Fusion-Gewichte bit-genau spec-konform (alle 11 Module, `score_fusion.py:14-27`); Discrepancy-Handling flag-statt-mitteln korrekt (`:210-234`); Divide-by-Zero/None/Leere-Liste durchgängig abgesichert.

### c) Fehlerbehandlung & Edge Cases
- **[MITTEL / S / OPEN]** Batch-Endpoint umgeht das `is_usable`-Confidence-Gate: `_analysis_succeeded()` prüft nur `analysis is not None`/`not error`, nicht `confidence.is_usable` → unbrauchbare Low-Confidence-Analysen zählen in `images_analyzed` und in die anzahlbasierte Confidence (>5 → „high"). — `images.py:173-181,420,440-447`
- **[MITTEL / M / OPEN]** Retry-`timeout=60` bindet den blockierenden Sync-SDK-Call nicht (`asyncio.wait_for` kann Sync nicht preempten; SDK ohne `timeout=` → ~600s Default). — `analyzer.py:64,166-214` + `retry.py`
- **[NIEDRIG / S / OPEN]** Single-Upload setzt `ai_analysis_version="1.0"` auch bei Fehl-Analyse (Truthiness statt `_analysis_succeeded`). — `images.py:249,318,523`
- **[NIEDRIG / S / OPEN]** Circuit-Breaker/Retry-State nicht thread-safe (prozessweiter `_breakers`-Singleton, Mutation ohne Lock; check-then-set). — `retry.py:287-351`
- **[NIEDRIG / S / OPEN]** Bildqualität nur Auflösungs-/Dateigrößen-Proxy — keine Schärfe/Belichtung. — `confidence.py:111-142`
- **[SAUBER/RESOLVED]** Vision-Retry/Circuit-Breaker mit Non/Retryable-Klassifizierung; JSON-Parse mehrstufiger Fallback (kein Roh-Leak); Orchestrator `return_exceptions=True` isoliert Modulfehler; Upload-Edge-Cases (leer/korrupt/oversize/Format, PIL-Inhaltsprüfung); „nicht beurteilbar"-Pfad.

### d) Datenmodell-Konsistenz
- **[MITTEL / S / OPEN]** Zwei gleichnamige Enums `VisualConfidence` mit widersprüchlichen Werten: `schemas/images.py:20-24` (`high/medium/low/insufficient`, nicht-kanonisch, wird in `BatchAnalysisResponse` serialisiert) vs. `services/visual/confidence.py:25-29` (kanonisch `visual_*`). — Batch-API gibt `medium` statt `visual_medium` aus.
- **[MITTEL / M / OPEN]** Confidence-Vokabular über 4 Repräsentationen fragmentiert (quick_analysis `ConfidenceLevel`, 2× `VisualConfidence`, `VALID_CONFIDENCE_LEVELS`) — keine Single Source of Truth. — `schemas/quick_analysis.py:9-13` u.a.
- **[MITTEL / M / OPEN]** BoatDNA `_PRESETS`/`from_boat_class` nur 4/13 (ValueError für 9; latent, kein Aufrufer). Siehe CG-2. — `models/boat_dna.py:89-195`
- **[NIEDRIG / S / OPEN]** Redundante, ungenutzte ORM-Modelle `Zone`/`Passage` mit divergentem Feldsatz vs. JSON-`ZoneData`/`PassageData`. — `models/models.py:92-113`
- **[NIEDRIG / S / OPEN]** `User.role/tier/locale/unit_system` als freie String-Spalten ohne Enum/CHECK-Constraint. — `models/models.py:330-335`
- **[SAUBER]** BoatClass-Enum korrekt 13 Werte; Pydantic v2 durchgängig (kein `class Config`); ORM/Pydantic-Felder konsistent.

### e) API-Vollständigkeit
- **[HOCH / S / OPEN]** `/analyze` umgeht Tier-Gating. Siehe CG-1. **CONFIRMED_OPEN.** — `layouts.py:298-359`
- **[HOCH / M / OPEN]** `require_feature`/`require_module` an keiner Route-Grenze verwendet. Siehe CG-1. **CONFIRMED_OPEN.** — `subscription.py:211/227` (definiert, ungenutzt)
- **[NIEDRIG / M / OPEN]** Report-„PDF"-Export liefert nur JSON (`pdf_generator.py` erzeugt dict, kein PDF/FileResponse); Feature.REPORT_EXPORT_PDF ohne Implementierung.
- **[NIEDRIG / L / OPEN]** ENTERPRISE-Feature-Flags (fleet_management/api_access/custom_reports/multi_tenancy) ohne zugehörige Endpunkte.
- **[SAUBER]** Alle namentlich versprochenen Endpunkte (Import, Diff, Reports, Benchmarks, Auth, Collaboration, Versioning) real implementiert — keine TODO/NotImplemented/pass-Stubs.

### f) Sicherheit
- **[HOCH / M / OPEN]** Bezahlmodule via `/analyze` ohne Tier-Gating (Paywall-Bypass). Siehe CG-1. **CONFIRMED_OPEN.** — `layouts.py:298-359`
- **[HOCH / M / OPEN]** Visual-Analyse- und CAD-Import-Endpunkte nicht tier-gegated (PRO offen für FREE). **CONFIRMED_OPEN.** — `images.py`, `import_cad.py`
- **[MITTEL / M / OPEN]** Service-Report-CRUD ohne Ownership-Check (IDOR): read/update/delete per UUID ohne Verkettung zu `Project.user_id`. — `service_reports.py:19/58/71/93`
- **[MITTEL / S / OPEN]** STEP/IGES-Upload unbegrenzt in Speicher (`await file.read()` ohne Cap; images/DXF haben 20/25 MB-Cap). Siehe auch i). — `import_cad.py:72,109`
- **[NIEDRIG / S / OPEN]** Absoluter Server-Dateipfad in Bild-API-Responses (`file_path`). — `schemas/images.py:42`
- **[RESOLVED]** SECRET_KEY/COOKIE_SECURE-Boot-Guard vorhanden (`config.py:44-65`); Upload-Validierung + Prompt-Injection-Schutz robust bestätigt.

### g) Internationalisierung
- **[HOCH / L / OPEN]** Alle 13 Analyse-Module geben hartcodiertes Deutsch aus (`t()` nie aufgerufen). Siehe CG-4. **CONFIRMED_OPEN.** — `services/analysis/*.py`
- **[HOCH / L / OPEN]** Frontend ohne jegliche i18n (keine Library/Umschalter, hartcodiertes `de-DE`, kein Accept-Language). **CONFIRMED_OPEN.** — `frontend/src/`
- **[MITTEL / S / OPEN]** LocaleMiddleware als innerste Middleware → Fehler-/CSRF-/RateLimit-Antworten immer DE. — `middleware.py:364-368`
- **[MITTEL / S / OPEN]** i18n `boat_class`-Keys stimmen nicht mit dem 13-Enum überein (5 Phantom-Klassen, 5 echte fehlen). — `i18n.py:395-407`
- **[MITTEL / M / OPEN]** Persistierte `User.locale`-Präferenz wird nirgends ausgewertet. — `models.py:334`
- **[NIEDRIG / S / OPEN]** `validate_catalog()` prüft keine Enum-Deckung; Fusions-Codes (measured+visual/visual_only/discrepant) fehlen im Katalog. — `i18n.py:260-270,370-378`
- **[SAUBER]** i18n-Infrastruktur selbst (4 Locales, Formatierung, Fachterminologie) sauber.

### h) Testabdeckung
- **[HOCH / L / OPEN]** Keine HTTP-Route/Endpoint-Tests (kein TestClient/AsyncClient) → Auth-, Ownership-, CSRF-, Tier-Gating-Grenzen nicht regressionsgesichert. **CONFIRMED_OPEN.** — `backend/tests/`
- **[HOCH / M / OPEN]** Kern-Auth-Modul `core/auth.py` komplett ungetestet (JWT create/decode inkl. access-vs-refresh-type, bcrypt). **CONFIRMED_OPEN.** — `core/auth.py`
- **[HOCH / L / OPEN]** Keine Frontend-Tests (kein Framework installiert) → gefixte XSS-Sanitisierung (DOMPurify) + Confidence-Filter ungetestet. **CONFIRMED_OPEN.** — `frontend/package.json`
- **[MITTEL / S / OPEN]** Produktions-Boot-Guard `_enforce_production_security` ohne Regressionstest. — `config.py:44-65`
- **[MITTEL / S / OPEN]** `require_role`/Ownership-Kette (permissions.py) ungetestet.
- **[NIEDRIG / S / OPEN]** Korrupte/abgeschnittene Bilddaten (nicht dekodierbar) nicht explizit getestet. — `test_visual_analysis.py`
- **[SAUBER]** Alle 14 Analyse-Module + score_fusion/orchestrator/visual/CAD/i18n/units/subscription/retry/validation unit-getestet; Edge-Cases aus (c) größtenteils abgedeckt; 1115 Tests grün.

### i) Performance/Skalierung
- **[HOCH / S / OPEN]** STEP/IGES-Parsing synchron im async-Handler (kein `to_thread`) → blockiert den Event-Loop für ALLE Requests (Kontrast: images offloadet korrekt). **CONFIRMED_OPEN.** — `import_cad.py:80,117`
- **[HOCH / S / OPEN]** STEP/IGES-Upload ohne Größenlimit (`await file.read()`) → Memory-Exhaustion. **CONFIRMED_OPEN.** — `import_cad.py:72,109`
- **[HOCH / M / OPEN]** Batch-Bildanalyse streng sequenziell (bis 20 Vision-Calls, je bis ~60–180s, in einem Request; DB-Connection die ganze Zeit gehalten). **CONFIRMED_OPEN.** — `images.py:386-431`
- **[MITTEL / L / OPEN]** Keine Queue/Background-Jobs für minutenlange Vision-Analysen (kein Celery/RQ/BackgroundTasks). — `images.py`
- **[MITTEL / S / OPEN]** `upload_quick_analysis_image` ruft blockierenden Vision-Call ohne `to_thread` auf (im Gegensatz zu den Schwester-Endpunkten). — `images.py:500-505`
- **[MITTEL / M / OPEN]** O(n²)/O(n²·m²)-Algorithmen im CAD-Parser (`_merge_nearby_polygons`, `_detect_passages_from_proximity`) — Shapely vorhanden, aber ungenutzt. — `cad_import/step_parser.py`
- **[NIEDRIG]** Service-`VisualAnalyzer.analyze_batch` ebenfalls sequenziell; kein Concurrency-Limit/Semaphore für Vision-Calls.

---

## Spec-Code-Abgleich (für Teilaudit 3)

Die wichtigsten Spec↔Code-Deltas (CLAUDE.md-Abschnitt → Code-Realität), die Teilaudit 3 aufgreifen sollte:
1. **Subscription Tiers** („enforced server-side … require_feature/require_module at route boundaries") → nur Orchestrator-Pfad gated; alle Standalone-PRO-Routen offen. (CG-1)
2. **Boat Classes (13, not 4)** („everything calibrates on these") → 4-klassig in Vision-Prompts, OVERALL_WEIGHTS, BoatDNA, Report-Labels, i18n. (CG-2)
3. **Analysis Orchestrator / Score Fusion** („combines structured + visual per module") → Fusion existiert, wird aber nicht aufgerufen; Orchestrator kombiniert visuelle Ergebnisse nicht. (CG-3)
4. **i18n** („load-bearing and enforced in code" / PRO „multi-language") → Produktkern hartcodiertes DE; Frontend ohne i18n. (CG-4)
5. **Reliability Rule 1** („never present uncertain results as facts") → brand_dna/market 50.0 mit „measured".
6. **Reliability Rule 3** („CAD vs photo discrepancy → flag, don't average") → korrekt implementiert, aber dormant.
7. **Reliability Rule 4** („Befund prüfen not Mangel bestätigt") → im Visual-Code nicht angewandt.
8. **Confidence-Framework** (kanonische Codes) → Batch-API emittiert nicht-kanonisches `medium` statt `visual_medium`.

---

## Top-10-Prioritätenliste (Schaden × Hebelwirkung × niedriger Aufwand)

| # | Maßnahme | Bereich | Schwere/Aufwand |
|---|---|---|---|
| 1 | **`require_module` in `/analyze` + `require_feature`/`require_tier` an allen PRO-Routen** (Visual, CAD, Versions, Benchmarks, Community, Collaboration) | e+f | HOCH / S–M |
| 2 | **brand_dna + market auf `available:false`** statt 50.0/„measured" (analog cost/materials) | b | MITTEL / S |
| 3 | **STEP/IGES: `to_thread` + Größenlimit + 413** (Event-Loop-Block + Memory-DoS) | i+f | HOCH / S |
| 4 | **Score-Fusion in den Orchestrator verdrahten** (visual_results → fuse → overall) — aktiviert flag-statt-mitteln + Rule 3 | b+c | MITTEL / M |
| 5 | **13-Klassen-Kalibrierung**: BOAT_CLASS_CONTEXT/QUALITY/SPATIAL + OVERALL_WEIGHTS + BoatDNA + Report-Labels + i18n auf alle 13 | a+b+d+g | HOCH / M |
| 6 | **quality.py `confidence_overall`→`confidence`** (bzw. Gatekeeper beide lesen) — reaktiviert LOW/INSUFFICIENT für Quality | a | HOCH / S |
| 7 | **HTTP-Endpoint-Tests** für Auth/Ownership/CSRF/Tier-Gating + `core/auth.py`-Unit-Tests + Boot-Guard-Test | h | HOCH / M–L |
| 8 | **i18n im Produktkern**: Analyse-Modul-Strings durch `t()`; Frontend-i18n einführen | g | HOCH / L |
| 9 | **Batch-Bildanalyse**: `asyncio.gather`+Semaphore oder Background-Job; `is_usable`-Gate im Batch respektieren; `upload_quick_analysis_image` via `to_thread` | c+i | HOCH→MITTEL / M |
| 10 | **Service-Report-Ownership** (IDOR) + Confidence-Enum konsolidieren + Pfad-Leak in Image-Response | d+f | MITTEL / S–M |

---

## Abdeckung

Alle 9 Prüfbereiche (a–i) gegen den aktuellen Post-Fix-Code geprüft; jeder KRITISCH/HOCH-Befund adversariell gegen den echten Code verifiziert (14 als `CONFIRMED_OPEN` bestätigt). Backend vollständig; Frontend in Bezug auf i18n und Tests einbezogen. Kein Code verändert (Audit-only). Der ursprüngliche `audit_report_code.md` (Vor-Fix-Stand) bleibt als Historie erhalten.

---

## Nachtrag 21.07.2026 — Neue Befunde aus Produktvision-Mapping + Säule-1-Umsetzung

Beim Code-Mapping der vier Produktvision-Säulen (Lexikon / Kaufberatung / Eigner-Refit / Profi-Design) und der anschließenden Freischaltung von Säule 1 (Lexikon) wurden **neue, im Re-Audit vom 14.07. nicht erfasste Defekte** gefunden. Die Säule-1-nahen wurden **im selben Durchlauf gefixt** (Status FIXED, verifiziert: 1128 Tests grün, tsc sauber, E2E gegen live Server); der Rest ist OPEN und gehört zur Verdrahtungsarbeit der Säulen 2–4.

### FIXED (21.07., mit Regressionstests)
- **[HOCH → FIXED]** Knowledge-Frontend rief nicht-existente Endpunkte (`/knowledge/categories/{id}`, `/manufacturers/` statt `/manufacturer/`) mit falschen Response-Shapes → KnowledgePage fiel still auf **6 Mock-Kategorien** zurück; der 252-Dokumente-Korpus war für Nutzer unsichtbar. → Neuer Contract: `GET /knowledge/corpus/categories` + `GET /knowledge/corpus/documents/{key}`; `knowledge-api.ts` neu; Mock-Fallback entfernt (echte Fehleranzeige). — `knowledge.py`, `knowledge-api.ts`, `KnowledgePage.tsx`
- **[HOCH → FIXED]** Kein Endpunkt/keine Ansicht zum **Lesen** eines Korpus-Artikels. → `CorpusDocumentResponse` (rekursive Sektions-Hierarchie) + neue `KnowledgeArticle.tsx` (A11y: Escape/Fokus-Trap/Scroll-Lock; sichere Inline-Markdown-Darstellung ohne HTML-Injection; ⚠️-ZU-PRÜFEN-Flags als gekennzeichnete Prüfvermerk-Callouts).
- **[HOCH → FIXED]** Knowledge-Routen verlangten Login trotz „public"-Docstring (401 für anonyme Besucher; Level-1-Funnel tot). → Alle Knowledge-GET-Endpunkte public read-only; `KNOWLEDGE_BASE_FULL`-Tiefen-Gating bleibt dokumentierte Produktentscheidung. — `knowledge.py`
- **[HOCH → FIXED]** `/knowledge/manufacturer/{name}` prüfte Wrapper-Keys `found`/`profile`, die `get_manufacturer_knowledge()` nie liefert → **jeder** reale Treffer wurde als „not found" gemeldet. Zusätzlich: string-förmige `known_problems` (z. B. Dehler) wurden **zeichenweise** in 48 Ein-Buchstaben-„Schwächen" zerlegt; leere Herstellernamen im Korpus matchten **jede** Anfrage. → Mapping auf reale DB-Feldnamen + Typ-Guards + Leername-Filter. — `knowledge.py`, `knowledge_retrieval.py:1340`
- **[HOCH → FIXED]** Titel-Extraktion las nur Zeile 0 → **103/251 Artikel** (ganze Kategorien 09–28 mit YAML-Frontmatter) hatten `title=""`, UI hätte rohe Slugs gezeigt, Titelsuche verfehlte sie. → Frontmatter-Strip + erstes H1 im Gesamttext + Frontmatter-`title:`-Fallback. — `markdown_knowledge_loader.py:parse_knowledge_file`
- **[HOCH → FIXED]** Tabellen-Parser filterte **leere Mittelzellen** → Werte rutschten unter falsche Spaltenköpfe (Preise/Drehmomente/Zulassungen in ~100 Dateien — fachlich falsche Anzeige). → positionstreuer Split. — `markdown_knowledge_loader.py:_parse_markdown_table`
- **[HOCH → FIXED]** Cold-Start-Parse (~15 s, 840K Zeilen) lief lazy **im Event-Loop des ersten (jetzt öffentlichen) Requests** → fror nach jedem Restart den gesamten Prozess inkl. `/health` ein. → Lifespan-Warmup via `asyncio.to_thread` vor Traffic-Annahme + `to_thread` in den Corpus-Handlern. — `main.py`, `knowledge.py`
- **[HOCH → FIXED]** **Fresh-Install-Boot kaputt:** `seed.py:1713` legte Demo-Projekte mit `user_id=None` an — seit dem User-Isolation-Fix (NOT NULL) crashte **jeder Boot mit leerer Datenbank** (jede Neuinstallation/jedes frische Deployment) im Lifespan. Die lokale `aydi.db` kaschierte das. → Seed legt Demo-User (Zufallspasswort, kein Login-Konto) an und hängt die Demo-Projekte daran. — `seed.py`
- **[MITTEL → FIXED]** Such-Debounce-Races (stale Timer + Out-of-order-Responses), Modal schloss bei Textselektion, kein Body-Scroll-Lock, Suchfehler als „keine Treffer" maskiert, Artikel-Fehler stumm, `aria-label` invertiert, `Object.keys`-Spalten-Reorder bei numerischen Headern (→ Tabellen jetzt als `{columns, rows}`). — `KnowledgePage.tsx`, `KnowledgeArticle.tsx`, Schemas

### Nachtrag 21.07. (abends) — Säule 2 (Kaufberatung) verdrahtet
- **[HOCH → FIXED]** `PublicSpecs.brand/model_name/year` treiben jetzt einen **Buyer-Report**: neuer Service `buyer_insights.py` (Werft-Schwachstellen-DB mit Baujahr-Fenster-Logik `2000_2012`/`pre_/post_/1980s`, Alters-Erwartungen aus `MATERIAL_LIFESPAN_DATABASE`, Community-Matching), public `GET /quick-analysis/buyer-insights` + Integration in POST/GET `/quick-analysis` + `BuyerInsightsPanel` im Frontend. Verifiziert: 1149 Tests (21 neue), tsc, E2E.
- **[HOCH → FIXED, Top-1 der Gesamt-Prioritätenliste teilweise]** **Tier-Gating an der `/analyze`-Route-Grenze**: `get_allowed_modules(_user.tier)`-Guard → FREE-Nutzer können PRO-Module nicht mehr einzeln ausführen (403). Die übrigen PRO-Routen (images, import_cad, versions, benchmarks, collaborate) bleiben OPEN. Zusätzlich 422-Guard für `available:false` (vorher latenter KeyError→500). — `layouts.py:run_analysis`
- **[HOCH → TEILWEISE FIXED]** `community`-Verdrahtung: Modul in `ANALYSIS_MODULES`, Loader + Relevanz-Matching (`find_relevant_patterns`, nur Identitäts-Treffer ≥0.8) implementiert, `context.community_patterns` wird befüllt. **Bewusste Dormanz auf Level 2:** `Project` hat keine Hersteller-/Modell-Felder — ohne Identität wird ehrlich `[]` übergeben (Modul meldet „nicht verfügbar") statt der DB-weiten Pattern-Suppe, die fremde Werft-Probleme als Befund ausgegeben hätte. Aktivierung: Project-Identitätsfelder (OPEN, Migration nötig). Level 1 (Buyer-Report) nutzt Community bereits mit Identitäts-Matching.
### Nachtrag 21.07. (nachts) — Säule 3 (Eigner-Refit-Loop) verdrahtet
- **[HOCH → FIXED]** **Layouts sind nicht mehr unveränderlich:** `PATCH /projects/{pid}/layouts/{lid}` (LayoutUpdate: name/version/zones/passages/deck_height) mit **Auto-Snapshot des Vorzustands** als LayoutVersion vor jeder Änderung — der Kern-Loop „ändern → analysieren → vergleichen" ist damit erstmals möglich. UI: „Version sichern"-Button, Versions-**Vorschau** (klar getrennt) vs. echtes **Wiederherstellen** (PATCH inkl. deck_height aus Meta-Snapshot), **Vorher/Nachher-Score-Vergleich** zweier Läufe desselben Moduls mit Sub-Score-Deltas.
- **[KRITISCH → FIXED, WIP-Befund]** Der adversariale Review fand einen **von der WIP-Tab-Umstellung stammenden** Totalausfall: Route `/projects/:id/*` (Splat), Code las aber `useParams().tab` → `activeTab` blieb immer „overview", **alle Nicht-Übersichts-Tabs waren im Browser unerreichbar** (History/Analyse/Kosten inkl. der gesamten neuen Refit-UI). Fix: Splat-Segment lesen. — `ProjectDetail.tsx`
- **Adversarialer Review (13 Befunde) — alle behoben:** Versionsnummern-**Race** (read-max-then-insert ohne Lock/Constraint → doppelte „Version N" + möglicher stiller Verlust einer angewendeten Änderung) → `with_for_update` + `UniqueConstraint(layout_id, version_number)` + Migration `002_layout_version_integrity` + 409; **unvollständiger Snapshot** (deck_height/name nicht versioniert → Restore stellte den Vorzustand nicht her) → `layout_meta_snapshot`; **Phantom-Versionen** bei explizitem `null` → 422-Ablehnung; Versions-API akzeptierte Snapshots, die Restore nie einspielen kann → typisiert `list[ZoneData]`; Restore ohne Snapshot hätte Layout **geleert** → Guard; Score-Vergleich mischte **Läufe verschiedener Layouts** (Äpfel/Birnen als Refit-Wirkung) → layout_id-Filter + „veraltet"-Kennzeichnung; nach Restore blieben alte Scores/Diffs stehen → Invalidierung; Preview-Zustand war nicht beendbar → „beenden"-Button; Projektwechsel behielt fremdes Layout → Null-safe-Reset; A11y der Hover-Buttons → focus-within. Tests: 11 (4 neue: null-PATCH, zones=[], Meta-Restore-Roundtrip, Constraint).
- **Neue Migration:** `migrations/versions/002_layout_version_integrity.py` (Unique-Constraint + layout_meta_snapshot; batch_alter für SQLite). Vor Deploy: `alembic upgrade head`.

### Nachtrag 22.07. — Säule-3-Ausbau: Material-Zuweisungs-UI
- **[MITTEL → FIXED]** Material-Zuweisung hatte **keinerlei UI** (Backend-CRUD existierte, „Optik-Individualisierung" war API-only). Neu: Tab „Materialien" in ProjectDetail + `ZoneMaterialsPanel` (Zuweisen mit oberflächenbewusstem Flächen-Prefill — Boden/Decke: Polygonfläche, Wand: Umfang×Deckshöhe, sonst leer; Liste je Zone; Löschen; „Materialanalyse ausführen" mit „Änderungen noch nicht analysiert"-Hinweis, der Tab-Wechsel überlebt und nach erfolgreichem Lauf zurückgesetzt wird).
- **Adversarialer Review (6 Befunde) — alle behoben:** (HOCH) **Doppelzuweisung Zone+Oberfläche doppelt-zählte Fläche/Kosten/Gewicht** in der Materialanalyse und ließ das ersetzte Material weiter warnen → Backend 409 auf (zone, surface)-Duplikat + UI-**Swap-Semantik** („Ersetzen" löscht die alte Zuweisung); (MITTEL) Backend validierte `ZoneMaterialCreate` nicht (area ≤ 0 hätte Kosten/Gewicht **subtrahiert** und den Score geschönt; freie surface_types; Phantom-Zonen) → `gt=0` + `Literal`-Oberflächen + Zonen-Existenzprüfung 422; (MITTEL) Wand-Prefill nutzte fälschlich die Bodenfläche als „aus Geometrie geschätzt" (Faktor >2 daneben); (MITTEL) veraltetes/verlorenes Änderungs-Flag; (NIEDRIG) Materialkatalog-Kappung bei 100 → „Unbekanntes Material"; (NIEDRIG) fehlender Concurrency-Guard bei parallelen Analysen. Tests: `test_zone_materials_api.py` (6 — CRUD, Ownership, Validierung, 409-Duplikat, **Analyse-Integration**).

### Nachtrag 26.07. (2) — Säule 3 komplett: grafischer Zonen-Editor + Säule-4-Entscheidungsvorlage
- **[FEATURE]** **Zonen-Editor-MVP** (`LayoutEditor.tsx` + „Bearbeiten"-Modus im Layouts-Tab): Eckpunkte ziehen (50-mm-Raster), Zonen verschieben/umbenennen/typisieren/löschen/anlegen, Punkte einfügen (Kantenmitte) / entfernen (Alt+Klick); Speichern via PATCH — Vorzustand wird automatisch versioniert. Damit ist der Kern-Workflow von Säule 3 ohne externe DXF/JSON-Dateien bedienbar.
- **Adversarialer Review (5 Befunde) — alle behoben:** (HOCH) Rename-per-Tastendruck mit Namens-String-Match **korrumpierte Passagen fremder Zonen** bei transienten Namenskollisionen → Passagen werden in der Session **über Zonen-Indizes** geführt, Namen erst beim Speichern zurückgemappt; (HOCH) ungespeicherte Änderungen gingen bei Tab-/Layout-Wechsel und „Verwerfen" **kommentarlos verloren** → Dirty-Flag mit Confirm-Guards (Tab, Layout-Karte, Verwerfen) + `beforeunload`; (HOCH) Umbenennen/Löschen **verwaiste** `zone_name`-Referenzen (Material/Struktur/Kosten) → **Server-Kaskade** `LayoutUpdate.zone_renames` (PATCH aktualisiert ZoneMaterial/StructuralItem/CostItem) + Warn-Dialoge bei Zonen-Löschung; (MITTEL) fehlendes PointerCapture/`pointercancel` (Drag riss am SVG-Rand ab bzw. „klebte" am Cursor) → `setPointerCapture` + `buttons`-Check; (MITTEL) Pydantic-422-Arrays wurden als „[object Object]" angezeigt → `request()` formatiert Feld+Meldung, Name-Input auf 100 Zeichen begrenzt. Test: Rename-Kaskade in `test_layout_update_api.py`.
- **[ENTSCHEIDUNGSVORLAGE]** `entscheidungsvorlage_team_modell.md` (Säule 4): Ist-Aufnahme (8 Ownership-Helper als Chokepoints, tote `shipyard_id`, mehrteilnehmerfähige Collab hinter Owner-Gate), Optionen A (Projekt-Sharing) / B (Org-Modell) / C (Stufenplan), **Empfehlung C** — wartet auf Owner-Entscheidung.

### Nachtrag 26.07. — Säule-3-Ausbau: Strukturelemente (Messdaten → Analyse) + UI
- **[MITTEL → FIXED, Audit-OPEN geschlossen]** **„StructuralItems werden geladen, aber dem structural-Modul nie übergeben":** `run_structural_analysis(..., structural_items=...)` — gemessene Gewichte/Positionen fließen jetzt als **Punktmassen in alle sechs Gewichts-Teilanalysen** (fore_aft, lateral, heavy_placement, load_concentration, loading_conditions, trim); Orchestrator-kwargs-Branch + `/analyze`-Branch verdrahtet. Tank-Typen (`fuel_tank`/`water_tank`) skalieren mit dem Füllstand des Beladungszustands. Neuer Tab „Struktur" + `StructuralItemsPanel` (Erfassen/Liste/Löschen mit Confirm, Inline-„Position nachtragen" via PATCH).
- **Adversarialer Review (8 Befunde, numerisch reproduziert) — alle behoben:** **(KRITISCH, eigener Designfehler)** Die Rahmendehnung um Item-Positionen **invertierte die Bewertungsrichtung** — 100 kg Ankerkette VOR den Zonen erzeugte „zu weit achtern", 15 kg am Davit kippte den Lateral-Score auf 0 → **fixer Zonen-Referenzrahmen + Clamp**, Items außerhalb werden als Info ausgewiesen; **(HOCH)** Doppelzählung mit der Zonenheuristik (350 kg/m²-Motorzone ENTHÄLT den Motor — gemessener Motor stapelte obendrauf) → `_build_weight_model` mit **Zonen-Entlastung** (zone_name-Zuordnung oder Punkt-in-Polygon, Heuristik um Messgewicht reduziert, `deducted_from_zone_heuristics_kg` in der Metrik); **(HOCH)** heavy_placement/load_concentration ignorierten Items (38 % des Scores widersprachen dem CG-Modell; gemessener 2-t-Motor ohne Motorzone → fälschlich 100 Punkte) → beide integriert; **(HOCH)** `parseFloat('2.000')=2` — deutsche Zahlformate wurden still falsch geparst, während die UI selbst `de-DE` anzeigt → strikter `parseLocaleNumber` (beide Panels); **(MITTEL)** Schema ohne Validierung (negative/NaN-Gewichte, freie item_types) → `gt=0`+`allow_inf_nan=False`+`Literal`-Typen; **(MITTEL)** Substring-Tank-Heuristik („watermaker" verlor Gewicht in light_ship) → exakte Typen + Info bei unzuordenbarem Tank; **(NIEDRIG)** Vollanalyse resettete Änderungs-Hinweise nicht; **(NIEDRIG)** Löschen-und-neu-erfassen-UX trotz PATCH. Tests: `test_structural_items_integration.py` (16 — Physik + alle Review-Regressionen).

- **Adversarialer Review der Säule-2-Umsetzung (23 Befunde) — alle behoben,** darunter 4 Ehrlichkeits-HOCHs, die erst der Review fand: (a) 18/23 Werft-Einträge nutzten andere Problem-Keys (`known_problems_minimal`/`_documented`/`known_issue`) → falscher Persilschein für Jeanneau/Hallberg-Rassy/Dufour — jetzt alle Key-Varianten + `period`-Fenster gelesen; (b) Alters-Logik übersah wegen striktem `lifespan_range`-Key genau die kritischsten Komponenten (Draht-Rigg, Saildrive-Membran, Gusskrümmer, Sanitärschläuche) → Varianten-Auflösung inkl. String-Ranges; (c) Positiv-Bilanzen („virtually none documented") wurden als Problem-Karte gerendert → jetzt grüne Track-Record-Note; (d) Level-5-`zone_category`-Fallback der Engine spülte fremde Werft-Muster als „dokumentiert" in den Report → Relevanz-Filter ≥0.8. Dazu: Token-basiertes Marken-Matching (Hanseat≠Hanse, „Sun"≠Sunseeker), Verbrauchsteile (Anoden/Impeller) als Info-Wartungsposten statt „major überschritten", Baujahr-Bounds 1900–2100 (Frontend+Schema; vorher erzeugte Tippfehler „202" einen seriös wirkenden „1824-Jahre"-Report), toleranter GET-Lesepfad für Alt-Datensätze, deutsche Formate („2000–2012", „15–20 %"), EN-Quelltexte im UI gekennzeichnet.
- **[MITTEL / OPEN]** `StructuralItems` (gemessene Gewichte/Positionen) werden geladen, aber dem `structural`-Modul **nie übergeben** (`_build_module_kwargs` ohne Branch; Modul-Signatur nimmt sie nicht an). — `orchestrator.py:228-253`
- **[MITTEL / OPEN]** Collaborate-WS: `_user_owns_layout` lässt **nur den Eigentümer** in die Session (2. Teammitglied kann nie beitreten); `zone_edit`/`comment` werden nicht persistiert; kein Frontend-WS-Client. — `collaborate.py:47,97-105`
- **[MITTEL / OPEN]** Kein Layout-`PUT/PATCH/DELETE`; Versionen per UI nicht anlegbar; Diff nur Geometrie (kein Score-/Kosten-Delta); Snapshot-Anzeige ≠ Analyse-Stand. — `layouts.py`, `versions.py`, `ProjectDetail.tsx`
- **[NIEDRIG / OPEN]** `_load_brand_references` filtert nur nach `boat_class`, ignoriert `shipyard_id`; Brand-References ohne Ownership. — `layouts.py:235-248`
- **[NIEDRIG / OPEN]** Umgebungs-Hinweis: lokale Dev-Umgebung driftete vom Pin (`bcrypt 5.0.0` statt `==4.0.1` → passlib-Crash beim ersten Hashing; `pytest-asyncio`/`email-validator` fehlten). Lokal behoben; kein Code-Defekt, aber Argument für ein venv-Setup-Skript.

### Nachtrag 26.07. (3) — Säule 4 Stufe 1: Projekt-Sharing (Entscheidung „Option C")
Owner-Entscheidung **„C" (Stufenplan)** umgesetzt: Projekt-Sharing jetzt, Org-Modell als spätere Ausbaustufe. Verifiziert: **1196 Tests grün** (+13 zum Stand vor Stufe 1), tsc 0 Fehler.

**Gebaut:**
- **Datenmodell + Migration `003_project_sharing`:** `ProjectMember` (project_id, user_id, role `viewer`/`editor`, `uq_project_member`); Owner bleibt aus `Project.user_id` abgeleitet (kein Rollen-Eintrag). Zusätzlich `created_by_user_id` (nullable, SET NULL) auf `brand_reference_models`, `materials`, `competitor_models`. **Vor Deploy: `alembic upgrade head`** (002 + 003 ausstehend).
- **Zentraler Access-Helper** `get_accessible_project(project_id, user, db, min_role)` in `core/permissions.py`: Owner immer; Mitglied nach Rolle; **404 ohne Zugriff** (kein Existenz-Leak), **403 bei zu niedriger Rolle** (deutsch). Default `min_role="editor"` ist bewusst: ein vergessener Callsite sperrt zu viel statt zu wenig. Alle **9 Routen-Dateien** delegieren ihre `_verify_project_ownership`/`_get_user_project`-Helper; **13 GET-Callsites** explizit auf `min_role="viewer"`.
- **Members-Endpoints:** GET (Owner+Mitglieder; Owner als synthetischer Eintrag), POST (owner-only; 404 unbekannte E-Mail, 409 Duplikat mit Rollenwechsel-Hinweis, 409 Owner-Selbst-Add), DELETE (owner-only, **außer Selbst-Austritt**). Projekt-DELETE bleibt owner-only; Projekt-PATCH ist editor-Level (dokumentierte Entscheidung: Metadaten-Pflege gehört zur kollaborativen Refit-Arbeit).
- **Collab-WS freigeschaltet:** Audit-OPEN „nur Eigentümer kann Session beitreten" geschlossen — `_layout_access_role` (owner/editor/viewer), PRO-Tier-Gate (4003), `user_info.role` im Broadcast.
- **Frontend:** `Project.access_role`, Teilen-Dialog (`ShareDialog.tsx`, owner-only Button), „Geteilt · Bearbeiten/Nur Lesen"-Badges (ProjectDetail-Metakarte + Dashboard-Karten), api.ts-Member-Funktionen.

**Adversarialer Security-Review (2 Linsen, 13 Befunde) — alle behoben:**
- **(HOCH)** Collab-WS: Viewer konnte trotz Nur-Lesen-Rolle `zone_edit` broadcasten → rollenbewusster Block (`error`-Frame, Session bleibt offen); unbekannte Message-Typen für Viewer ebenfalls blockiert. — `collaborate.py`
- **(HOCH)** `/class-benchmarks` aggregierte **fremde Projektdaten ohne Tier-Gate und ohne k-Anonymität** (n=1 → min=max=mean identifiziert ein einzelnes fremdes Boot) → `require_tier(BENCHMARK_DATABASE)` + `_MIN_SAMPLE_SIZE=5` mit deutscher Begründung statt Metriken. — `benchmarks.py`
- **(HOCH)** Global-Ressourcen-IDOR: `Material` und `CompetitorModel` waren von **jedem** eingeloggten Nutzer änder-/löschbar (speisen fremde Analysen; Material-Delete kaskadiert in fremde Zonenzuweisungen) → `created_by_user_id` + Creator/Admin-Guard (Legacy-Zeilen ohne Creator = admin-managed) + **409 bei Material-Delete in Verwendung** (Kaskade hätte fremde Projekte still beschädigt). Brand-References analog (bereits beim Bau). — `materials.py`, `competitors.py`
- **(HOCH)** Audit-Trail-Spoofing: `LayoutVersionCreate.changed_by` kam vom Client → Feld aus dem Schema entfernt, server-seitig `_user.email`; zusätzlich `parent_version_id`-Validierung gegen **dasselbe** Layout (FK allein akzeptierte fremde Layout-Versionen). — `versions.py`, `schemas/versions.py`
- **(MITTEL)** `update_project` lieferte `access_role` nicht (UI-Badge kippte nach PATCH) → gemeinsamer `_attach_access_role`-Helper für GET/PATCH/CREATE; 409-Duplikat-Detail um Rollenwechsel-Hinweis ergänzt. — `projects.py`
- **(MITTEL)** Viewer-UI zeigte Schreib-Buttons, die server-seitig 403 ernten → `canEdit`-Gating (Bearbeiten, Vollanalyse ×2, Einzelanalyse-Selector, Version sichern ×2, Wiederherstellen) mit deutschen Tooltips; `readOnly`-Prop für `ZoneMaterialsPanel`/`StructuralItemsPanel` (Formulare/Löschen ausgeblendet, Analyse-Button deaktiviert, Hinweis-Karte). — `ProjectDetail.tsx`, Panels
- **(NIEDRIG, dokumentierter Trade-off)** `POST /members` unterscheidet 404 „unbekannte E-Mail" von 409 „bereits Mitglied" → **E-Mail-Enumeration durch Projekt-Owner** möglich. Akzeptiert für Stufe 1: Angreifer muss eingeloggt + Projekt-Owner sein, globales IP-Rate-Limiting greift, und eine opake Antwort würde den legitimen Hauptfall („Tippfehler in der E-Mail") unlösbar machen. Re-Evaluation in Stufe 2 (Org-Modell mit Einladungs-Flow).

**Tests:** `test_project_sharing_api.py` (11 — Owner/Editor/Viewer/Stranger-Matrix, Selbst-Austritt/Entzug, `access_role` in PATCH-Antwort, server-gesetztes `changed_by` inkl. Spoof-Versuch, Benchmark-Gate FREE→403 + k-Anonymität n=1, Competitor-Guard), `test_zone_materials_api.py` (+2 — Material-Guard Creator/Legacy/Fremd, Delete-in-Use-409).

### Nachtrag 27.07. — Säule 4 Stufe 2: Organisations-Modell, Einladungen, Live-Kollaboration
Aufbauend auf Stufe 1 (Option C). Design über ein Judge-Panel (3 Linsen: Security / Product / Simplicity) erarbeitet; Synthese der konvergenten Entscheidungen. Verifiziert: **1216 Backend-Tests grün** (+20 neu), tsc 0 Fehler, `npm run build` grün, Migration-004-Round-Trip (SQLite) getestet.

**Gebaut — Backend:**
- **Datenmodell + Migration `004_organizations`** (additiv, inspector-guarded, SQLite-batch-kompatibel, idempotent, Round-Trip-getestet): `organizations` (name, tier default `free`, created_by), `organization_members` (org_role owner/admin/member, `uq_org_member`), unified `invitations` (email normalisiert, project_id XOR organization_id per CHECK, role, status pending/accepted/declined/revoked, expires_at, `ix_invitations_email_status`), `projects.org_id` + `brand_reference_models.org_id` (beide nullable FK **SET NULL** — Org-Löschung macht Projekte wieder privat, zerstört nie Mitglieder-Arbeit). **Vor Deploy: `alembic upgrade head`** (002+003+004 ausstehend).
- **Effective Tier** (`resolve_effective_tier`, `effective_tier`-Accessor in `permissions.py`): effektiver Tarif = max(persönlich, Org-Tarife), pro Request aufgelöst (kein Cache → Austritt/Downgrade greift sofort). An **einem Chokepoint** (`get_current_user` + `authenticate_websocket`) als transientes `user.effective_tier` angehängt; alle Gates lesen `getattr(user,'effective_tier',user.tier)` — der Fallback hält die bestehenden Tests (Bare-User via dependency_overrides) grün. Umgestellt: `require_tier`, `/analyze` (get_allowed_modules + AnalysisContext), Collab-WS, Benchmarks (erbt).
- **Org-Zugriff im zentralen Chokepoint:** `_effective_project_role` = max(Owner-wenn-Ersteller, ProjectMember-Rolle, org-abgeleitete Rolle). Mapping **org owner/admin → Projekt-`owner`, org member → `editor`** (bewusste Produktentscheidung: im Werft-Team ist Bearbeiten die Regel; Elena behält via admin→owner Kontrolle über Mitarbeiter-Projekte). `project_members` **addiert** nur Zugriff (externe Gäste), schränkt nie ein. `get_accessible_project` darauf umgebaut; **404 ohne Zugriff, 403 bei zu niedriger Rolle** bleiben. Org-Rollen-Leiter `require_org`/`get_org_role` (member<admin<owner) analog.
- **Org-Endpoints** (`routes/organizations.py`): CRUD (Erstellen offen für alle, Cap 5 eigene, Ersteller wird owner; GET nur eigene Orgs; Umbenennen owner/admin; Löschen owner-only → Projekte werden privat); Mitglieder (Rollen-PATCH **owner-only**, Last-Owner-Schutz, Selbst-Austritt außer letztem Owner); **Flottenübersicht** `GET /orgs/{id}/projects` (require `FLEET_MANAGEMENT` auf effektivem Tarif — erste echte Einlösung des toten ENTERPRISE-Flags); Org-Einladungen (Admin lädt Mitglieder, **nur Owner lädt Admins**).
- **Tier-Governance ohne Billing:** `org.tier` ausschließlich über `POST /admin/orgs/{id}/tier` (`require_role('admin')`) änderbar — **einziger Pfad**. `PATCH /orgs` hat kein tier-Feld. Erstellung hardcodet `free`. Das schließt den Eskalationspfad „Org anlegen → enterprise setzen → alles gratis".
- **Einladungs-Flow** (`routes/invitations.py` + Projekt-/Org-Endpoints): E-Mail-basiert (kein User-FK → Einladung an noch nicht registrierte Adresse greift nach Registrierung via `/invitations/mine`-E-Mail-Match). **Anti-Enumeration:** Erstellen liefert identische 201-Antwort bei bekannter/unbekannter E-Mail (kein User-Lookup im Antwortpfad). Annehmen recipient-only (404 für andere — IDs nicht abfragbar), idempotent, 410 bei abgelaufen/zurückgezogen, **nie Auto-Accept**. Konflikte nur bei owner-sichtbaren Fakten (bereits Mitglied/offene Einladung/Owner-Selbst). Abuse-Cap 50 offene/Einlader. Normalisierung (lower+trim) an Schreib- UND Match-Stelle. Rollen-PATCH für Projekt-Mitglieder (löst den Stufe-1-Workaround „entfernen+neu teilen" ab).
- **Legacy `POST /members` eingefroren** (deprecated): bleibt byte-identisch, damit die 11 Stufe-1-Matrix-Tests unverändert grün bleiben; das Frontend nutzt ausschließlich den Einladungs-Pfad. Rest-Enumeration dokumentiert, Sunset in Stufe 3.
- **Brand-References org-scoped** (`competitors.py`): Sichtbarkeit org-Zeilen→Org-Mitglieder, persönliche→Ersteller, Legacy/Seed (beide NULL)→global lesbar (speisen weiter jede brand_dna-Analyse); Mutation org owner/admin, Ersteller oder Plattform-Admin. Freetext-`shipyard_id` **in place deprecated** (keine Auto-Migration — Freitext ist keine verlässliche Tenancy-Grenze).

**Gebaut — Frontend (tsc grün, build grün):**
- **Live-Kollaboration** (`useCollaboration.ts` + `CollabPanel.tsx` + Overlay in `LayoutViewer.tsx`): Präsenz, Live-Cursor (mm-Koordinaten via `getScreenCTM`), Zonen-Auswahl-Highlight, **ephemere** Kommentare (dauerhaft als „nicht gespeichert" gekennzeichnet). **Kein** Remote-Apply von `zone_edit` (keine OT/Persistenz → würde unbestätigten Fremdstand als Fakt zeigen; stattdessen Aktivitäts-Hinweis). Backoff-Reconnect; 4001/4003 terminal. Vite-`/api`-Proxy `ws:true`. Opt-in „Live-Session beitreten".
- **Einladungs-UI:** `ShareDialog` auf Einladungen umgestellt (E-Mail-Einladung, ausstehende Liste + Widerruf, Inline-Rollenwechsel; ehrlicher Hinweis „keine E-Mail wird versendet"); `InvitationsInbox` (Banner im Dashboard, Annehmen/Ablehnen, aktualisiert Projektliste).
- **Org-Verwaltung** (`OrganizationsPage` + Route + Nav „Organisationen"): Orgs anlegen/wählen, Mitglieder + Rollen (owner-only) + Entfernen, Einladen, Flottenübersicht (ehrliche ENTERPRISE-Sperr-Meldung), Löschen. `ProjectDetail`: Org-Zuordnungs-Selektor (owner-only) „Privat/Organisation".

**Tests:** `test_org_access_matrix.py`, `test_invitations.py` (9), `test_migration_004.py` (2 — Round-Trip + Idempotenz).

**Adversarialer Review (4 Linsen — Tenancy/AuthZ, Correctness/Regression, Honesty/Reliability, Migration/Data — je Befund adversariell verifiziert; 9 Roh → 8 bestätigt, 5 distinkt) — alle behoben:**
- **(HOCH)** **brand_dna-Analyse leakte fremde PRIVATE Brand-References:** der Analyse-Loader `_load_brand_references(boat_class, db)` lud **alle** Zeilen einer Bootsklasse ungefiltert; das Modul spiegelt Referenz-Inhalte (Topologie-Lücken, Proportions-Signaturen) in seine Warnungen → ein beliebiger PRO-Nutzer konnte über `brand_dna` die private Brand-DNA einer fremden Org auslesen (die org-Scoping-Kontrolle aus `competitors.py` war auf dem Analysepfad komplett umgangen). → Sichtbarkeitsprädikat in **`app/core/brand_visibility.py`** zentralisiert (`can_see_brand_ref`/`get_my_org_ids`), Loader nimmt jetzt `user` und filtert identisch zu den CRUD-Endpunkten; beide Call-Sites (`/analyze`, `/full-analysis`) übergeben `_user`; `competitors.py` nutzt dasselbe Prädikat (kein Drift mehr). — `layouts.py`, `competitors.py`, `brand_visibility.py`
- **(HOCH)** **Org-Admin konnte Org-OWNER entfernen:** `remove_org_member` prüfte nur `min_role="admin"` + Last-Owner — kein Rang-Vergleich, während Rollen-PATCH bewusst owner-only ist. Ein Admin konnte co-Owner/co-Admins über den Delete-Pfad hinauswerfen (Rollen-Administration über Höhergestellte). → Rang-Guard: Owner dürfen jeden entfernen (Peers inkl.), alle anderen nur **strikt niedrigere** Rollen (Admin entfernt nur Mitglieder). — `organizations.py`
- **(HOCH)** **WS-Ablehnung schloss vor `accept()`:** die Denial-Pfade (4001/4003) riefen `websocket.close()` vor `accept()` → Starlette weist auf HTTP-Ebene ab, der Browser sieht generisches 1006 statt des Custom-Codes → der Frontend-Client konnte „kein Zugriff/Tarif" nicht erkennen und **reconnnectete endlos**. → `await websocket.accept()` vor jedem `close(code, reason)`; zusätzlich Frontend-Cap `MAX_RECONNECTS=6` (stray 1006 hämmert nicht mehr ewig). — `collaborate.py`, `useCollaboration.ts`
- **(MITTEL)** **Last-Owner-Guard TOCTOU-Race:** `_owner_count` war ein ungelocktes SELECT-COUNT; unter PostgreSQL READ COMMITTED konnten zwei gleichzeitige Demote/Remove je 2 Owner sehen und beide durchlaufen → Org ohne Owner. → `_locked_owner_count` mit `with_for_update()` (serialisiert Prüfung+Mutation in derselben Transaktion), an allen drei Stellen. — `organizations.py`
- **(MITTEL)** **SQLite erzwang keine FKs → Org-Delete SET NULL/Cascade wirkte in Dev/Test nicht** (die gesamte Test-Suite validierte Tenancy gegen eine Engine ohne FK-Enforcement). → `PRAGMA foreign_keys=ON` global für alle SQLite-Verbindungen (`db/database.py`, greift auch für Test-Engines) **und** `delete_organization` räumt jetzt **explizit** auf (Projekte/Brand-Refs org_id→NULL, Members/Invitations gelöscht) — korrekt auf jeder Engine. Volle Suite bleibt mit aktivem FK-Enforcement grün (kein Fallout).
- **(REFUTED)** „004-Downgrade `drop_constraint` bricht auf SQLite" — gegen echtes SQLite reproduziert: der benannte `create_foreign_key`/`drop_constraint`-Batch-Round-Trip funktioniert; kein Defekt.

**Neue/erweiterte Tests (Review-Fixes):** Loader-Sichtbarkeit (Org-Member sieht, Fremder nicht), Admin-kann-Owner/Admin-nicht-entfernen (nur Mitglied), Org-Delete-Aufräumen (Projekt privat + Members/Invitations weg, Projekt überlebt). **Stand: 1219 Backend-Tests grün, tsc 0, build grün.**

**Bekannte, dokumentierte Grenzen (Stufe 3):** Live-WS hat noch keine Integrationstests (braucht `async_session`-Injektion auf die Test-DB — bestehende Infra-Lücke, gilt schon für Stufe 1); WS-Sitzungen behalten Connect-Zeit-Autorisierung bis Disconnect (HTTP re-gated pro Request; ein `force_disconnect(user, layout)`-Hook bei Member-Entzug ist Stufe-3-Arbeit); eingefrorenes `POST /members` behält seine Enumeration (nur noch API, kein Frontend-Pfad); kein Billing (org.tier admin-gesetzt); RLS (Postgres) weiterhin offen — Vorbedingung für echten Mehr-Tenant-Betrieb.
