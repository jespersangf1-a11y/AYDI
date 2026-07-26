# Audit-Bericht: Spezifikation & CLAUDE.md (Teilaudit 3 — Re-Audit Post-Fix)

Datum: 2026-07-14
Maßstab: Vollständigkeit, interne Widerspruchsfreiheit und Übereinstimmung der Spezifikations-/Architekturdokumente mit der Code-Realität (Teilaudit 2) und der Wissensbasis (Teilaudit 1).
Methodik: Direkte Lektüre aller Spec-, Mandats- und Meta-Dokumente; Abgleich gegen die frischen Teilaudit-1/2-Berichte; jede Spec↔Code-Aussage gegen den Ist-Code verifiziert. Kein Dokument verändert — nur der Bericht ist das Ergebnis.

> **Kontext:** Re-Audit **nach der Fix-Phase**. Der ursprüngliche `audit_report_spezifikation.md` (2026-07-05, CLAUDE.md 231 Zeilen) ist Vor-Fix. Die jetzige CLAUDE.md hat **286 Zeilen** mit einer neuen „Platform Architecture"-Sektion. Dieser Bericht (a) bestätigt, welche alten T3-Lücken die Fix-Phase geschlossen hat, und (b) deckt die vom Master-Brief geforderten NEUEN Dimensionen ab (10 Systemdomänen, Modul-Doku-Gleichwertigkeit, Persona-/Edge-Case-Abdeckung, Aktualität der Mandats-Dokumente). Querverweise: `audit_report_recherche.md` (T1), `audit_report_code_2026-07-14.md` (T2).

---

## Gesamtzustand in fünf Sätzen

Die Fix-Phase hat **CLAUDE.md nachgezogen**: Auth/Secret-Management, Subscription-Tiers, i18n, das 252-Dokumente-Wissenssystem, Deployment, ISO 12215, die Fusions-Confidence-Codes und die Companionway-Sill-Regel sind jetzt spezifiziert — praktisch die **gesamte alte Teilaudit-3-Lückenliste ist auf der Spec-Seite geschlossen**, und die veralteten Design-Docs unter `docs/superpowers/` tragen jetzt Archiv-Banner. CLAUDE.md ist damit als „Definitive Engineering Specification" heute weitgehend vollständig und code-treu. **Die Schwäche ist weitergewandert**, nicht verschwunden: Die drei **Validierungs-/Mandats-Dokumente** (`VERIFICATION_PROTOCOL.md`, `QA_AUDIT_REPORT.md`, `PRAXISTEST_PROTOKOLL.md`, alle April 2026) sind **eingefroren im Vor-Fix-Zustand und geben teils falsche Entwarnung** — sie melden „Tier-Gating 15/15 PASS", „XSS überall geblockt" und „keine generischen Fallbacks" grün, also genau die Punkte, die Teilaudit 2 als HOCH/CONFIRMED_OPEN führt. Zusätzlich zeigen die vom Brief geforderten neuen Dimensionen echte Spec-Lücken: die **10 Systemdomänen** sind ungleich tief ausgearbeitet (vier werden von fachfremden Modulen mit Fabrikations-50.0 vertreten) und in CLAUDE.md gar nicht als Taxonomie geführt; die **vier Personas** haben dekorative Rollen ohne differenzierte Journey; und die namentlich genannten **Edge-Cases** (schlechte Fotos, CAD-vs-Foto-Widerspruch, Tier-/Sprachwechsel mitten in der Session) sind nicht spezifiziert. Die strukturelle Kernerkenntnis (Schritt 3): **Die Spezifikation ist jetzt ehrlich — die Test-/QA-Protokolle, die für sie bürgen, sind es nicht.**

**Zahlen:** 0 KRITISCH · ~4 HOCH · Rest MITTEL/NIEDRIG · ~10 alte T3-Befunde als RESOLVED bestätigt.

---

## Inventur-Ergebnis (Spec-/Doku-Bestand, Ist-Stand)

| Dokument | Zeilen | Rolle | Zustand (Post-Fix) |
|---|---|---|---|
| `CLAUDE.md` | **286** (war 231) | Maßgebliche Spec | **stark verbessert**: Platform-Architecture-Sektion ergänzt; code-treu in Kernformeln |
| `backend/VERIFICATION_PROTOCOL.md` | 217 | „Systemlogik"-Mandat-Output (Apr 2026) | **veraltet** (Python 3.10, 875 Tests); PARTIAL/OPEN-Punkte nie nachgezogen |
| `backend/QA_AUDIT_REPORT.md` | ~202 | „Code-QA"-Mandat-Output (Apr 2026) | **veraltet + falsche Entwarnung** (XSS, Tier-Gating, „21 Kategorien") |
| `backend/PRAXISTEST_PROTOKOLL.md` | 215 | „Praxis-Test"-Mandat-Output (Apr 2026) | **veraltet + falsche Entwarnung** (Tier-Gating, 50.0-Scores als PASS) |
| `backend/praxistest_runner.py` / `praxistest_full.py` | — | Praxistest-Code (4 Personas) | Rollen dekorativ (nur Log-Label) |
| `docs/superpowers/specs/*` (5) + `plans/*` (10) | 314–4.226 | Modul-Design/-Pläne | **Archiv-Banner gesetzt** → als historisch markiert (RESOLVED) |
| `KNOWLEDGE_INDEX.py` | ~1.418 | Wissens-Index | **auf 252/31/~840K aktualisiert** (RESOLVED) |
| `DEPLOY.md` (100), `INTEGRATION_ANWEISUNG.md` (222) | — | Betrieb/Integration | **jetzt aus CLAUDE.md referenziert** (RESOLVED) |
| Verwaiste Recherche (`marine_window_gaskets_research.md`, `knowledge_base/…`, `research/…`, `Forschung_…`) | — | Themen-Dubletten | **weiter im Repo** (OPEN, T1-Housekeeping) |
| **Nicht existent** | | | `audit_00_MASTER_uebersicht.md`, `docs/modules/`, `docs/visual/` — im Brief referenziert, **im Repo nicht vorhanden** |

> **Nicht querverifizierbar in diesem Durchlauf:** Ein Master-Steuerdokument `audit_00_MASTER_uebersicht.md` mit dem „Einheitlichen Berichtsformat" existiert nicht als Datei; das Format wurde aus den bestehenden Teilberichten übernommen. `docs/modules/` und `docs/visual/` (im Brief als Hauptkandidaten genannt) existieren nicht — Modul-/Visual-Spezifikation lebt ausschließlich in CLAUDE.md + Code.

---

## Bereichsübergreifendes Kern-Muster

### Muster SPEC-1 — Die Validierungs-Dokumente bürgen für einen Zustand, den es nicht (mehr) gibt (HOCH)
Die drei „Mandats"-Outputs sind auf **April 2026** eingefroren (Python 3.10; Testzahlen 875 / 1114 / 1114 — die aktuelle Suite hat ~1115). Sie werden aber nicht als veraltet markiert und lesen sich als gültige Freigabe. Dabei geben sie **grünes Licht auf genau die Lücken, die Teilaudit 2 als HOCH bestätigt hat**:
- **`PRAXISTEST_PROTOKOLL.md` F1–F4 „Subscription-Tiers 15/15 PASS"** + **`QA_AUDIT_REPORT.md` #1 „Alle API-Endpunkte haben Auth-Prüfung ✅"** → getestet wurde die Tier-**Konfiguration** (`subscription.py`-Hierarchie) und die **Authentifizierung**, **nicht** die Autorisierungs-Durchsetzung an den Route-Grenzen. Teilaudit 2 (CG-1, HOCH, CONFIRMED_OPEN) belegt: `require_feature`/`require_module` werden nirgends aufgerufen; `/analyze` umgeht das Gating. → Die Protokolle vermelden die Bezahlschranke als dicht, die real offen ist.
- **`QA_AUDIT_REPORT.md` #5 „Injection (…XSS…) überall geblockt ✅"** + **`PRAXISTEST` E4 „kein serverseitiges Sanitizing nötig"** → falsch für den `dangerouslySetInnerHTML`-Renderpfad; die Fix-Phase musste DOMPurify nachrüsten (T2, Frontend-Fix). Die Protokolle haben XSS aktiv als Nicht-Problem abgehakt.
- **`QA_AUDIT_REPORT.md` #9 „keine generischen Fallbacks ✅"** → widerlegt durch die **eigene** Domänen-Tabelle in `PRAXISTEST_PROTOKOLL.md` (C2 Rigging→Materials 50.0, C3 Propulsion→Service Patterns 50.0, C9 Navigation→Cost 50.0, C10 Maintenance→Service Patterns 50.0).
- **50.0-Fabrikations-Scores als „✅ PASS" protokolliert** (`PRAXISTEST` C2/C3/C9/C10, Brand DNA, Market) → genau das Anti-Pattern, das Teilaudit 2 (b_scoring) in `brand_dna.py`/`market.py` als OPEN führt. Der Praxistest wertet einen fabrizierten Fallback-Score als bestandenes Ergebnis.

→ **Wertvollster Spec-Befund:** Der Validierungs-Layer ist selbst eine Fehlerquelle — er dokumentiert unverifizierte/falsche Freigaben und würde einen Leser glauben lassen, die HOCH-Befunde aus T2 seien erledigt.

---

## Befunde nach Prüfbereich

### a) Interne Konsistenz zwischen Dokumenten
- **[MITTEL / S / OPEN]** Zählstände driften über die Dokumente: Testzahlen **875** (`VERIFICATION_PROTOCOL`) vs **1114** (`QA_AUDIT`, `PRAXISTEST`) vs **~1115** (aktuelle Suite/CLAUDE.md-Umfeld); Wissens-Kategorien **„21 Kategorien"** (`QA_AUDIT` #22) vs **31** (`KNOWLEDGE_INDEX.py`, CLAUDE.md). Der Kategorien-Zählstand wurde im Index korrigiert, im QA-Report nicht. — `QA_AUDIT_REPORT.md:161`
- **[SAUBER]** Kernformeln/Gewichte/Confidence-Codes/Tiers stimmen zwischen CLAUDE.md und den Protokollen bzw. dem Code exakt überein (in T2 verifiziert). Terminologie „boat_class/Bootsklasse" konsistent; Domänen-Namen EN im Code (Hull/Rigging), DE in i18n („Rumpf & Struktur") — je Ebene konsistent.

### b) Domänenwissen-Tiefe
- **[MITTEL / M / OPEN]** CLAUDE.md verankert das Domänenwissen **nicht am eigenen Qualitätsmaßstab.** Teilaudit 1 auditiert den Korpus gegen den „Fensterdichtungs-Standard" (Werfttiefe: Hersteller, Teilenummern, korrekte Normen, allein-lösbar). CLAUDE.md hat „Build Quality Standards by Boat Class", benennt aber den Tiefenstandard, an dem die 252 Recherche-Dokumente gemessen werden, nirgends — Spec und Wissensbasis-Qualitätsbar sind entkoppelt (Brief-Dimension d). — Ref. T1 „Fensterdichtungs-Standard"
- **[SAUBER/RESOLVED]** Das Yachtbau-Fachwissen in CLAUDE.md ist spezifisch und normverankert (CE-Kategorien A–D, ISO-Tabelle inkl. **ISO 12215 mit explizitem Hinweis gegen die 12217-Verwechslung**, Werkstoffkunde). Die alte Muster-E-Wurzel (fehlende 12215) ist behoben. — `CLAUDE.md:61-74`

### c) Abgleich mit Code-Realität (Teilaudit 2)
Wichtige Verschiebung: Wo früher die **Spec** hinterherhinkte, ist jetzt in mehreren Fällen die **Spec korrekt und der Code die Abweichung** — das sind Produktentscheidungen „Code an Spec anziehen", keine Doku-Fehler.
- **[HOCH / — / OPEN(Code)]** CLAUDE.md fordert korrekt „**Use `require_feature`/`require_module` at route boundaries**" (Z.232) — der Code tut es nicht (T2 CG-1). Spec führt, Code lagt. → Kein Spec-Fix, sondern Code-Fix. — Ref. `audit_report_code_2026-07-14.md` CG-1
- **[MITTEL / — / OPEN(Code)]** CLAUDE.md „Score fusion combines structured + visual results per module" (Z.155) — im Orchestrator nicht verdrahtet (T2 CG-3). Spec beschreibt ein Verhalten, das der Code nicht ausführt. — Ref. T2 CG-3
- **[MITTEL / — / OPEN(Code)]** CLAUDE.md Tier-4 „service_patterns, brand_dna, market (needs cost)" (Z.152) — brand_dna/market fabrizieren 50.0 bei fehlenden Daten statt `available:false` (T2 b_scoring); die dokumentierte Cost-Abhängigkeit (Tier 3) wird im Datenfluss nicht durchgereicht. — Ref. T2 b_scoring
- **[RESOLVED]** Fusions-Confidence-Codes (`measured+visual`/`visual_only`/`discrepant`) jetzt in CLAUDE.md dokumentiert (Z.120-126); Companionway-Sill-`max(override, CE-floor)`-Regel dokumentiert (Z.194) und im Code gefixt; BoatClass als **13** dokumentiert (Z.234-237). — alte T3-MITTEL/HOCH geschlossen

### d) Abgleich mit Recherche-Dokumenten (Teilaudit 1)
- **[HOCH / L / OPEN]** **Scope-Widerspruch Motoren** unverändert offen: CLAUDE.md definiert den Scope bis „Custom/Superyacht 18m+" (Z.90), die Wissensbasis (`01_08`/`01_09`) deckt aber nur Hilfsdiesel ≤110 PS ab — kein CAT/MTU/MAN/Cummins/Volvo D3–D13. Entweder Recherche unvollständig oder Spec-Scope zu weit. Produktentscheidung nötig. — Ref. T1 Offene Frage 3
- **[MITTEL / M / OPEN]** **Verwaiste Recherche-Duplikate** weiterhin im Repo (`marine_window_gaskets_research.md`, `knowledge_base/marine_propeller_shaft_seals_*`, `research/Borddurchlass-*`, `Forschung_Niedergang_Dichtungen_2026.md`) — duplizieren Korpusthemen (`01_02`/`01_06`/`01_05`/`07_02`), vom Loader nicht geladen, driften inhaltlich. — Ref. T1
- **[RESOLVED]** Duplikat `24_05`: Loader schließt die `_clean.md`-Backup-Variante korrekt aus (kein Doppel-Load); Slug-Kollisionen jetzt unter Komposit-Key gespeichert (CLAUDE.md Z.244). Index-Zählstände auf 252/31 korrigiert. — alte T3/T1-Befunde geschlossen

### e) Vollständigkeit der Persona-/Edge-Case-Abdeckung
- **[MITTEL / M / OPEN]** **Vier Personas — gleichwertig, aber durchweg oberflächlich; Rollen dekorativ.** Kai (Bootseigner), Sarah (Werftleiterin), Marc (Käufer), Elena (Designerin) haben Rollen, die natürlich auf Tiers abbilden (Sarah→ENTERPRISE/Werft, Elena→PRO, Kai/Marc→FREE/PRO). Das `role`-Feld ist aber nur ein **Log-Label** (`praxistest_runner.py:85`) — es wird der Registrierung nie übergeben (nur email/password/full_name, Z.76-80), treibt weder Tier noch Berechtigungen. Alle vier durchlaufen **identische Flows**; Sarahs ENTERPRISE-Journey (Fleet/Multi-Tenancy) wird nie ausgeübt. Keine Persona ist „nur skizziert" — alle sind Name+Label auf einem Flow. — `praxistest_runner.py:68-90`
- **[MITTEL / M / OPEN]** **Die vom Brief namentlich genannten Edge-Cases sind nicht spezifiziert/getestet:** schlechte Fotos (Visual-Pipeline im Praxistest ausgeklammert, `PRAXISTEST:196`), widersprüchliche Daten (CAD-vs-Foto), Tier-Übergang mitten in der Session (nur statischer „Downgrade-Impact", kein Wechsel), Mehrsprachigkeits-Wechsel mitten in der Session (nur Per-Locale-Formatierung). — `PRAXISTEST_PROTOKOLL.md` Gruppen D/E
- **[SAUBER]** Generische Input-Edge-Cases (Null/NaN/Inf/Negativ/Extrem/Leer/SQL-Injection/unbekannte Klasse) sind gut abgedeckt und verifiziert. — `VERIFICATION_PROTOCOL.md §3`, `PRAXISTEST` E1-E6

### f) Aktualität
- **[HOCH / S / OPEN]** **Die drei Mandats-/QA-Dokumente sind nicht als veraltet markiert** und geben falsche Entwarnung (Muster SPEC-1). Anders als die Design-Docs (jetzt mit Archiv-Banner) lesen sich `QA_AUDIT_REPORT.md`/`PRAXISTEST_PROTOKOLL.md`/`VERIFICATION_PROTOCOL.md` als gültige Freigabe des Ist-Stands. — `backend/*.md` (Apr 2026)
- **[MITTEL / S / OPEN]** **`.env.local` (QA BUG-001, KRITISCH) nur teil-aufgelöst:** die Datei ist jetzt gegitignored (`.gitignore` `.env.*` + `!.env.example`), **existiert aber lokal weiter** (300 B); die im QA-Report selbst geforderten Folgeschritte (**API-Key-Rotation, Git-History-Bereinigung**) sind aus dem Repo nicht verifizierbar und ausstehend. Ein einmal committeter Key bleibt in der History kompromittiert, bis sie bereinigt wird. — `QA_AUDIT_REPORT.md:11-21`
- **[MITTEL / M / OPEN]** **10 Systemdomänen nicht in CLAUDE.md geführt + ungleich tief.** Das reale 10-Domänen-System (`app/core/domains.py`, 29 Tests) — Hull, Rigging, Propulsion, Electrical, Sanitary, Deck, Interior, Safety, Navigation, Maintenance — wird in CLAUDE.md **nicht dokumentiert** (das Wort „domain" erscheint nur als „domain-specific" + Überschrift „Domain Knowledge"). CLAUDE.md führt drei **nicht abgeglichene** Taxonomien: 11 Analyse-Module (Fusions-Tabelle), 31 Wissens-Kategorien, und — nur im Code — 10 Domänen. Tiefe **ungleich** (Brief Schritt 1.3): Hull→Structural (real, 79.6) und Interior→Volume (real, 52.5) sind ausgearbeitet; **Rigging/Propulsion/Navigation/Maintenance** haben kein eigenes Analyse-Modul und werden von fachfremden Modulen mit Fabrikations-50.0 vertreten. — `CLAUDE.md` (fehlt), `PRAXISTEST_PROTOKOLL.md` C1-C10
- **[MITTEL / M / OPEN]** **Analyse-Module ungleich dokumentiert (Brief Schritt 1.4).** „Professional Designer-Level Module Enhancements" beschreibt Sub-Analysen für 8 Module (ergonomics, volume, emotional, compliance, materials, structural, production, cost). **service_patterns, brand_dna, market** (in der Fusions-Tabelle gelistet) haben **keine** Sub-Analyse-/Eingabe-/Warning-Code-Dokumentation; `community` ist ein Modul mit Design-Doc, fehlt aber ganz in der Fusions-Tabelle. Genau die zwei undokumentierten Module (brand_dna, market) sind die, die T2 für 50.0-Fabrikation flaggt — undokumentiert = kein Soll, gegen das der Code prüfbar ist. Warning-Codes und `BOAT_CLASS_DEFAULTS`-Struktur sind für **kein** Modul in der Spec (Brief fordert beides). — `CLAUDE.md:177-211`
- **[RESOLVED]** Design-/Plan-Docs unter `docs/superpowers/` tragen jetzt Archiv-Banner („⚠️ ARCHIV — HISTORISCHER PLANUNGSSTAND … Maßgeblich ist CLAUDE.md … Nicht zum Ableiten von Enums/Tests verwenden"). Die alte HOCH-Bewertung „aktiv irreführend" ist entschärft (Inhalt weiter 4-klassig, aber klar markiert). — `docs/superpowers/specs/*`, `plans/*`

---

## Schritt 3: Zusammenführender Blick

Die alte T3-Kernaussage war „Code/Realität tut C, D, E — Spec schweigt". Die Fix-Phase hat dieses Schweigen weitgehend beendet: **CLAUDE.md hat mit dem Code aufgeschlossen.** Die Living-Document-Lücke ist damit aber nicht geschlossen, sondern **eine Ebene weitergewandert** — zu den **Validierungs-/Mandats-Dokumenten**. Diese sind auf den April-2026-Stand eingefroren, tragen (anders als die Design-Docs) kein Veraltungs-Signal, und bescheinigen dem System grün, was Teilaudit 2 als HOCH offen führt (Tier-Gating, XSS, generische Fallbacks) — inklusive der Protokollierung fabrizierter 50.0-Scores als „PASS". Der Effekt ist gefährlicher als eine bloß unvollständige Spec: **ein Dokument, das fälschlich Entwarnung gibt, verhindert aktiv, dass die offene Lücke bearbeitet wird.** Zweitens zeigen die vom Brief erzwungenen Prüfachsen (10 Domänen, Modul-Doku, Personas, benannte Edge-Cases), dass **Vollständigkeit behauptet statt ausgeübt** wurde: „22/22 Ja", „116 PASS" und „alle 10 Domänen liefern Ergebnisse" verdecken, dass vier Domänen nur einen Fabrikations-Proxy haben, die Personas rollenlos identisch laufen und die risikoreichsten Edge-Cases (Foto-Qualität, Quell-Widerspruch, Tier-/Sprachwechsel) nie getestet wurden. **Die Spezifikation ist heute ehrlich; die Protokolle, die für sie bürgen, sind es noch nicht** — sie auf den Ist-Stand zu heben (oder als historisch zu markieren) ist die wichtigste strukturelle Konsequenz dieses Teilaudits.

---

## Top-10-Prioritätenliste (Teilaudit 3)

| # | Maßnahme | Schwere/Aufwand | Warum |
|---|---|---|---|
| 1 | **Mandats-/QA-Dokumente auf Ist-Stand heben ODER als „ARCHIV (Apr 2026, vor-fix)" markieren** — und die falschen Freigaben (Tier-Gating, XSS, generische Fallbacks) korrigieren | HOCH / S–M | Verhindern, dass falsche Entwarnung die T2-HOCH-Lücken verdeckt (Muster SPEC-1) |
| 2 | **`.env.local`: API-Key rotieren + Git-History bereinigen** (BFG/filter-branch), lokale Datei bestätigen | HOCH / M | Kompromittiertes Secret bleibt in History; Gitignore allein heilt es nicht |
| 3 | **Scope-Entscheidung Motoren treffen** und in CLAUDE.md + Recherche angleichen | HOCH / L | Spec↔Recherche-Widerspruch; berührt T1 + T3 |
| 4 | **10 Systemdomänen in CLAUDE.md aufnehmen** + Verhältnis Domäne↔Modul↔Wissens-Kategorie klären; die 4 Proxy-Domänen (Rigging/Propulsion/Navigation/Maintenance) als solche kennzeichnen oder mit eigener Logik hinterlegen | MITTEL / M | Brief Schritt 1.3; deckt die Fabrikations-50.0-Proxys auf |
| 5 | **service_patterns/brand_dna/market/community in CLAUDE.md dokumentieren** (Sub-Analysen, Inputs, Warning-Codes) | MITTEL / M | Brief Schritt 1.4; schafft das Soll gegen das T2-50.0-Fabrikation prüft |
| 6 | **Persona-Journeys differenzieren** — Rolle→Tier verdrahten (Sarah=ENTERPRISE etc.), je Persona eigener Pfad | MITTEL / M | Brief e; macht F1-F4/Enterprise real testbar statt abstrakt |
| 7 | **Benannte Edge-Cases spezifizieren+testen**: schlechte Fotos, CAD-vs-Foto-Widerspruch, Tier-/Sprachwechsel in-Session | MITTEL / M | Brief e; genau die Risikofälle fehlen |
| 8 | **Domänenwissen-Tiefenstandard in CLAUDE.md verankern** (Fensterdichtungs-Standard als expliziter Bar für den Korpus) | MITTEL / S | Brief d; koppelt Spec an die T1-Qualitätsmesslatte |
| 9 | **Zählstände vereinheitlichen** (Testzahl, „21"→31 Kategorien in QA-Report) | MITTEL / S | interne Konsistenz |
| 10 | **Verwaiste Recherche-Dubletten bereinigen** (Root/`research/`/`knowledge_base/`) | NIEDRIG / M | Housekeeping; Widerspruchsquelle |

---

## Abdeckung

CLAUDE.md (vollständig, Post-Fix), alle drei Mandats-Outputs (`VERIFICATION_PROTOCOL`, `QA_AUDIT_REPORT`, `PRAXISTEST_PROTOKOLL`) + Praxistest-Code, `docs/superpowers/` (Banner-Stichprobe), `KNOWLEDGE_INDEX.py`-Zählstände, `DEPLOY.md`/`INTEGRATION_ANWEISUNG.md`-Verlinkung, Spec↔Code (verzahnt mit `audit_report_code_2026-07-14.md`), Spec↔Recherche (verzahnt mit `audit_report_recherche.md`). **Nicht querverifizierbar in diesem Durchlauf:** ein Master-Steuerdokument `audit_00_MASTER_uebersicht.md`, `docs/modules/`, `docs/visual/` — existieren nicht. Der ursprüngliche `audit_report_spezifikation.md` (Vor-Fix) bleibt als Historie erhalten. Kein Dokument verändert (Audit-only).
