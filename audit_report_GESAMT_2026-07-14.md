# Audit-Bericht GESAMT — AYDI Vollständiger Qualitätsaudit (Post-Fix-Stand)

Datum: 2026-07-14
Zusammenführung von Teilaudit 1 (Recherche), 2 (Code), 3 (Spezifikation).
Maßstab durchgehend: **Fensterdichtungs-Standard** — „Könnte jemand sein Problem allein mit dieser einen Stelle lösen?"
Quellen: `audit_report_recherche.md` (T1, 2026-07-05), `audit_report_code_2026-07-14.md` (T2, Re-Audit), `audit_report_spezifikation_2026-07-14.md` (T3, Re-Audit).

> **Kontext:** Dies ist der **Post-Fix-Gesamtbericht**. Zwischen dem ursprünglichen Audit (2026-07-05) und heute lief eine Fix-Phase, die die **4 KRITISCH- und den Großteil der ~14 HOCH-Code-Befunde behoben**, CLAUDE.md um die Plattform-Schicht ergänzt, die Design-Docs mit Archiv-Bannern versehen und die dünnen Recherche-Kategorien (28/29/31) auf Werfttiefe gehoben hat (Letzteres teils on-disk/untracked, in der QC-Pipeline des Users). Der ursprüngliche `audit_report_GESAMT.md` (Vor-Fix) bleibt als Historie erhalten.

---

## Gesamtzustand in fünf Sätzen

AYDI steht nach der Fix-Phase deutlich besser da als beim Erstaudit: die sicherheitskritische Auth-Lücke (SECRET_KEY-Boot-Guard), die tote Visual-Pipeline, der stille Wissens-Datenverlust und die gröbsten „erfundene-Gewissheit"-Stellen im Code sind behoben, CLAUDE.md ist von einer lückenhaften Engine-Spec zu einer weitgehend vollständigen, code-treuen Plattform-Spec gewachsen, und die dünnsten Sicherheits-Recherchekategorien wurden vertieft. **Der Kern ist damit solide — die verbleibende Arbeit sitzt an drei Nähten:** (1) im Code ist vieles **korrekt gebaut, aber nicht verdrahtet** — Tier-Gating greift nicht an den Route-Grenzen (Bezahlschranke offen), die korrekte Score-Fusion ist dormant, i18n endet an den Rändern, und die 13-Bootsklassen-Kalibrierung ist an Kernstellen weiter nur 4-klassig; (2) die **Validierungs-Dokumente selbst geben falsche Entwarnung** — die QA-/Praxistest-Protokolle bescheinigen genau die offenen Punkte (Tier-Gating, XSS, generische Fallbacks) als „PASS" und protokollieren fabrizierte 50.0-Scores als Erfolg; (3) der **Recherche-Korpus** trägt weiterhin sein dominierendes Muster (Haupttext-vs-Anhang-Widersprüche, beide „measured") und 295 bewusst offengelassene Fach-Flags — die verbleibende Domänen-Entscheidungsarbeit des Users. Kurz: **Gefahr wurde erfolgreich abgebaut; die Restlücken sind Verdrahtung, ehrliche Protokolle und Fach-Kuratierung — nicht mehr Grundsubstanz.**

**Zahlen (Post-Fix):** 0 KRITISCH offen · ~13 HOCH (Code) + ~4 HOCH (Spec) · Recherche: 105/399 Flags aufgelöst, 295 offen (User-Domäne), Body-vs-Anhang-Sweep ausstehend.

---

## Muster, die bereichsübergreifend auftreten (Post-Fix)

### Muster CG — „Halb verdrahtet": korrekt gebaut, im Live-Pfad nicht aktiv (Code, dominant)
Das neue Leitmuster von Teilaudit 2. Fähigkeiten sind implementiert und getestet, aber nicht angeschlossen:
- **Tier-Gating** nur im Orchestrator, nicht an Route-Grenzen → `/analyze` + alle PRO-Routen (Visual, CAD, Versions, Benchmarks, Collab) offen für FREE (Paywall-Bypass). *(T2 CG-1, HOCH, CONFIRMED_OPEN)*
- **Score-Fusion** (flag-statt-mitteln, Rule 3) korrekt + getestet, aber im Orchestrator nirgends aufgerufen. *(T2 CG-3)*
- **i18n** sauber, aber nur an Middleware/Auth-Rändern; alle 13 Analyse-Module + das Frontend hartcodiert Deutsch. *(T2 g, CG-4)*
- **13-Bootsklassen** in der Spec dokumentiert, im Code weiter 4/13 (Vision-Prompts, OVERALL_WEIGHTS, BoatDNA, Report-Labels). *(T2 CG-2)*

### Muster SPEC-1 — Die Validierungs-Dokumente bürgen für einen Zustand, den es nicht gibt (Spec, neu)
Die drei Mandats-Outputs (`VERIFICATION_PROTOCOL`, `QA_AUDIT_REPORT`, `PRAXISTEST_PROTOKOLL`, alle April 2026) sind eingefroren und **geben grünes Licht auf genau die Muster-CG-Lücken**: „Tier-Gating 15/15 PASS", „XSS überall geblockt", „keine generischen Fallbacks" — alle drei von Teilaudit 2 widerlegt. Sie protokollieren zudem fabrizierte 50.0-Scores als „✅ PASS". → Ein Dokument, das fälschlich Entwarnung gibt, verhindert aktiv die Bearbeitung der offenen Lücke. *(T3 Muster SPEC-1, HOCH)*

### Muster A — „Erfundene Gewissheit" (reduziert, nicht beseitigt)
Die schwersten Instanzen sind gefixt (tote Pipeline, Batch-`confidence.high` für null Analysen, zentrale 50.0-Fabrikation in cost/materials/structural/service_patterns). **Rest:** `brand_dna.py`/`market.py` fabrizieren weiter 50.0 mit „measured" *(T2 b_scoring)*; vier Proxy-Domänen liefern denselben 50.0 *(T3)*; und die Praxistest-Protokolle werten das als Erfolg *(SPEC-1)*. Die Nicht-Verhandelbar-Regel #1 ist an diesen Stellen weiter verletzt.

### Muster D — Dokumentation vs. Code: jetzt teils invertiert (verbessert)
Früher „Spec schweigt". Heute: **CLAUDE.md hat aufgeschlossen** (Auth, Subscription, i18n, Wissenssystem, ISO 12215, Fusions-Codes, Sill-Regel dokumentiert) und die Design-Docs tragen Archiv-Banner. An mehreren Stellen ist die **Spec jetzt korrekt und der Code die Abweichung** (Spec fordert `require_feature` an Route-Grenzen — Code tut es nicht) → Fix-Richtung „Code an Spec anziehen". Die verbliebene Doku-Drift sitzt in den **nicht markierten Mandats-Dokumenten** (Muster SPEC-1).

### Muster B — Body-vs-Anhang-Widerspruch (Recherche, weiter dominant)
Unverändert der korpusweit häufigste Defekt: Haupttext und Anhänge behaupten für Traglasten/Bruchlasten/Drehmomente/Prüfdrücke Gegensätzliches, systematisch beide „measured". Der einzig skalierbare Fix (mechanischer Haupttext-vs-Anhang-Diff über alle 252 Dokumente + Anhänge als „documented, unverified" umkennzeichnen) ist noch ausstehend. *(T1 Muster B)*

### Muster C — Sicherheit als dünnste Naht (teilweise adressiert)
Die dünnsten + fehlerreichsten Kategorien (28 Interieur, 29 Sicherheit, 31 Konstruktion) wurden in der Fix-Phase web-verifiziert auf Werfttiefe gehoben (on-disk/untracked, QC-Pipeline). 105/399 web-verifizierbare Flags aufgelöst; **295 bleiben bewusst offen** (echt mehrdeutig, paywalled Normtext) — die Fach-Entscheidungsarbeit des Users. *(T1 + Memory research-audit-sweep-2026-07)*

### Muster E — Normen/i18n als schwache Ader (Wurzel gefixt, Reichweite offen)
Die ISO-12215-Wurzel ist in CLAUDE.md behoben (Tabelle + expliziter Hinweis gegen 12217-Verwechslung). Die i18n-**Reichweite** bleibt offen (Muster CG-4: Produktkern hartcodiert DE).

### Muster F — Duplikate & Verwaistes (teilweise behoben)
`24_05`-Doppelladung entschärft (Loader schließt `_clean.md` aus; Slug-Kollisionen unter Komposit-Key). **Rest:** verwaiste Root-/`research/`-/`knowledge_base/`-Recherche-Dubletten weiter im Repo.

---

## Projektweite Top-10-Prioritätenliste (Post-Fix, aus den drei frischen Teil-Top-10)

Sortiert nach Schaden × Hebelwirkung × (niedriger) Aufwand. Verzahnte Befunde zusammengefasst.

| # | Maßnahme | Bereich | Schwere/Aufwand | Warum genau hier |
|---|---|---|---|---|
| 1 | **Tier-Gating an den Route-Grenzen verdrahten** (`require_module` in `/analyze`; `require_feature` an allen PRO-Routen) | Code | HOCH / S–M | Offene Bezahlschranke; Spec fordert es bereits korrekt (T2 CG-1 / T3 c) |
| 2 | **Mandats-/QA-Dokumente ehrlich machen** — falsche Freigaben (Tier-Gating, XSS, generische Fallbacks) korrigieren oder Dokumente als „ARCHIV (vor-fix)" markieren | Spec | HOCH / S–M | Verhindert, dass falsche Entwarnung #1/#4 verdeckt (Muster SPEC-1) |
| 3 | **`.env.local`: API-Key rotieren + Git-History bereinigen** | Spec/Ops | HOCH / M | Kompromittiertes Secret bleibt in History; Gitignore heilt es nicht (QA BUG-001) |
| 4 | **brand_dna/market → `available:false` statt 50.0/„measured"** | Code | MITTEL / S | Letzte zentrale „erfundene Gewissheit"; Praxistest wertet sie fälschlich als PASS (Muster A + SPEC-1) |
| 5 | **CAD-Import: `to_thread` + Upload-Größenlimit** (STEP/IGES) | Code | HOCH / S | Event-Loop-Block für alle Requests + Memory-DoS (T2 i/f) |
| 6 | **13-Klassen-Kalibrierung im Code** (Prompts, OVERALL_WEIGHTS, BoatDNA, Labels) **+ 10 Domänen & Proxy-Domänen in CLAUDE.md** dokumentieren | Code+Spec | HOCH / M | 9 Klassen fallen still auf Segel-Default; 4 Domänen nur Fabrikations-Proxy (T2 CG-2 / T3) |
| 7 | **Score-Fusion in den Orchestrator verdrahten** (aktiviert flag-statt-mitteln + Rule 3) | Code | MITTEL / M | Ganze Fusion inkl. früherem Fix ist dormant (T2 CG-3) |
| 8 | **i18n in den Produktkern** (Analyse-Modul-Strings via `t()`; Frontend-i18n einführen) | Code | HOCH / L | PRO-„multi-language" real nicht lieferbar (T2 CG-4) |
| 9 | **Testabdeckung schließen** (HTTP-Route/Auth/Ownership/Tier-Tests; `core/auth.py`; Persona-differenzierte + Edge-Case-Tests: schlechte Fotos, CAD-vs-Foto, Tier-/Sprachwechsel) | Code+Spec | HOCH / M–L | Genau die Grenzen aus #1 sind ungetestet; Personas/Edge-Cases nur behauptet (T2 h / T3 e) |
| 10 | **Recherche: Body-vs-Anhang-Diff-Sweep + Motor-Scope-Entscheidung + Dubletten-Bereinigung** | Recherche+Spec | HOCH / L | Wurzelmuster B; Scope-Widerspruch Spec↔Recherche; 295 Flags = User-Domäne (T1 / T3 d) |

**Reihenfolge-Begründung:** #1–#3 sind die höchsten Schaden/Aufwand-Ratios (offene Bezahlschranke, falsche Entwarnung, kompromittiertes Secret). #4–#7 stellen die Nicht-Verhandelbar-Regel und die dokumentierten Verhaltensweisen wieder her (kleine bis mittlere Eingriffe, hohe Hebelwirkung). #8–#10 sind die größeren strukturellen Aufträge (i18n-Reichweite, Test-Fundament, Korpus-Sweep), die eigene Durchläufe verdienen.

---

## Abdeckung & nächste Schritte

| Teilaudit | Abgedeckt | Status |
|---|---|---|
| 1 Recherche | 110/252 tiefengeprüft (jede der 31 Kat.), 252 triagiert; Kat. 28/29/31 vertieft; 105/399 Flags aufgelöst | KRITISCH gefixt (teils on-disk); **295 Flags + Body-vs-Anhang-Sweep = User-Domäne/offen** |
| 2 Code | 9/9 Prüfbereiche (a–i), Post-Fix, KRITISCH/HOCH adversariell verifiziert | 0 KRITISCH offen, ~13 HOCH — Detail in `audit_report_code_2026-07-14.md` |
| 3 Spezifikation | CLAUDE.md (vollständig), 3 Mandats-Docs, Design-Docs, Index, Spec↔Code/↔Recherche | ~10 alte Befunde RESOLVED; ~4 HOCH neu/offen — Detail in `audit_report_spezifikation_2026-07-14.md` |

**Der Audit ist inhaltlich abgeschlossen und repräsentativ.** Die drei Muster-Cluster (Verdrahtung im Code, falsche Entwarnung in den Protokollen, Kuratierung im Korpus) sind belegt und stabil. Verbleibende Arbeit ist überwiegend **Fix-/Entscheidungsarbeit**, keine Erkenntnisarbeit: (1) die Muster-CG-Verdrahtung im Code (Top #1, #5–#8); (2) die Ehrlichmachung der Validierungs-Protokolle (#2); (3) die Ops-Härtung (#3); (4) der mechanische Korpus-Diff + die 295 Fach-Flags als User-Domäne (#10).

Dieser Durchlauf hat **keinen Code, kein Dokument und keine Recherche-Datei verändert** — die frischen Teilberichte (`audit_report_code_2026-07-14.md`, `audit_report_spezifikation_2026-07-14.md`) und dieser Gesamtbericht sind die einzigen Artefakte; die Vor-Fix-Originale (`audit_report_*.md`, 2026-07-05) bleiben als Historie erhalten.
