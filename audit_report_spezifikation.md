# Audit-Bericht: Spezifikation & CLAUDE.md (Teilaudit 3)
Datum: 2026-07-05
Maßstab: Vollständigkeit & Widerspruchsfreiheit der Architektur-/Domänendokumente — untereinander, gegen den Code (Teilaudit 2) und gegen die Recherche (Teilaudit 1).

> **Methodenhinweis:** Dieser Bericht stützt sich auf (a) die belegten Befunde aus Teilaudit 1 und 2, (b) direkte Inline-Prüfung von CLAUDE.md, `KNOWLEDGE_INDEX.py`, der Verzeichnisstruktur und `score_fusion.py`/`orchestrator.py`, und (c) einen Nachlauf-Workflow, der **6 der 15 Design-/Plan-Dokumente unter `docs/superpowers/`** gegen den Code geprüft hat (Ergebnis im „## Nachtrag"). Damit ist die zuvor offene Design-Doc-Dimension zum größten Teil geschlossen.

---

## Zusammenfassung

CLAUDE.md ist als *Engineering-Spezifikation* präzise und in den geprüften Kernpunkten **bemerkenswert code-treu** — Score-Fusion-Gewichte, Orchestrator-Tiers, Confidence-Codes und die Profi-Formeln stimmen exakt zwischen Spec und Code überein (in Teilaudit 2 verifiziert). Das ist Werftqualität an der Naht Spec↔Code.

Die Schwächen liegen woanders: **CLAUDE.md ist unvollständig** — mehrere real gebaute und produktiv relevante Subsysteme (Authentifizierung/Autorisierung, Subscription-/Tier-Modell, Internationalisierung, das 252-Dokumente-Wissenssystem, Deployment) sind in der Spezifikation **gar nicht beschrieben**. Und an der Naht **Spec↔Recherche** gibt es einen echten Domänenwiderspruch (Motor-Scope; ISO-Normen), während die **Meta-/Index-Dokumente veraltet** sind (Zählstände „249"/„72" statt real 252) und **verwaiste Recherche-Duplikate außerhalb des Korpus** existieren.

**Kern-Muster:** Nicht „Spec sagt A, Code macht B" (das ist überwiegend konsistent), sondern **„Code/Realität tut C, D, E — Spec schweigt dazu"**. Die Spezifikation beschreibt die *Analyse-Engine* exzellent, aber nicht die *Plattform drumherum*.

---

## Inventur-Ergebnis (Spec-/Doku-Bestand)

| Dokument | Zeilen | Rolle | Zustand |
|---|---|---|---|
| `CLAUDE.md` | 231 | Maßgebliche Spec | code-treu in Kernformeln; Lücken bei Plattform-Themen |
| `docs/superpowers/plans/*` (10) | 600–4.226 | Umsetzungspläne pro Modul | **nicht auf Aktualität geprüft (offen)** |
| `docs/superpowers/specs/*` (5) | 314–638 | Design-Docs pro Modul | **nicht auf Aktualität geprüft (offen)** |
| `KNOWLEDGE_INDEX.py` | 1.418 | Wissens-Index | Zählstände veraltet (249/72 vs. 252) |
| `IMPLEMENTATION_SUMMARY.md`, `QUICK_REFERENCE.md`, `README_WEAKPOINTS.md` | 290–404 | Knowledge-Meta | Currency-Check offen |
| `DEPLOY.md` (100), `INTEGRATION_ANWEISUNG.md` (222) | — | Betrieb/Integration | außerhalb CLAUDE.md, nicht referenziert |
| `backend/QA_AUDIT_REPORT.md`, `PRAXISTEST_PROTOKOLL.md`, `VERIFICATION_PROTOCOL.md` | 202–214 | frühere QA-Protokolle | Currency-Check offen |
| **Verwaiste Recherche außerhalb Korpus** | | | **Duplikat-Risiko (siehe HOCH)** |
| — `marine_window_gaskets_research.md` (root) | 705 | dupliziert Thema `01_02` | verwaist |
| — `knowledge_base/marine_propeller_shaft_seals_wellenabdichtung.md` | 1.606 | dupliziert `01_06` | verwaist |
| — `research/Borddurchlass-*.md` (3 Dateien) | 210–1.056 | dupliziert `01_05`/`07_02` | verwaist |
| — `Forschung_Niedergang_Dichtungen_2026.md` (root) | 738 | Recherche-Fragment | verwaist |
| Committete Skill-Packs (`.claude/`, `bencium-skills/`, `vercel-skills/`, `nextlevel-skills/`, `accesslint-skills/`, `ui-ux-pro-max/`) | — | Fremd-Tooling im Repo | Repo-Hygiene (NIEDRIG) |

---

## Befunde

### KRITISCH
- Keine. (Die sicherheitskritischen Befunde liegen in Code (Teilaudit 2) und Recherche (Teilaudit 1), nicht in der Spezifikation selbst.)

### HOCH

- **CLAUDE.md dokumentiert Sicherheit/Auth gar nicht.** Das reale System hat ein vollständiges AuthN/AuthZ-Modell (JWT, bcrypt, Ownership, Rollen — `permissions.py`, `auth.py`) und einen KRITISCH-Sicherheitsfehler (SECRET_KEY, Teilaudit 2). CLAUDE.md erwähnt weder Auth noch Secret-Management noch die zwei Nutzerlevel als *authentifizierte* Grenze. Eine Spec, die die sicherheitskritischste Komponente nicht beschreibt, kann sie auch nicht als Anforderung erzwingen. — Aufwand: M
- **CLAUDE.md dokumentiert das Subscription-/Tier-Modell nicht.** `subscription.py` definiert FREE/… mit modul-genauem Gating und der expliziten Regel „Gating is enforced server-side" — im Code aber unwirksam (Teilaudit 2, HOCH). CLAUDE.md beschreibt „Level 1/Level 2" nur funktional, nicht als bezahlte, serverseitig durchzusetzende Schranke. Spec-Lücke mit direkter Sicherheits-/Geschäftskonsequenz. — M
- **Spec↔Recherche-Scope-Widerspruch (Motoren).** CLAUDE.md definiert den Scope bis „Custom/Superyacht 18m+" und die Wissensbasis führt Motoryacht-Werften (Princess, Sunseeker, Nordhavn) als Zielgruppe. Die einzigen Motordichtungs-Dokumente (`01_08`, `01_09`) decken jedoch nur Hilfsdiesel ≤110 PS ab — **kein** CAT/MTU/MAN/Cummins/Scania, kein Volvo D3–D13. Entweder ist die Recherche unvollständig oder der Spec-Scope zu weit; beides zusammen ist ein Widerspruch. — L
- **Verwaiste Recherche-Duplikate außerhalb des Korpus.** `marine_window_gaskets_research.md`, `knowledge_base/marine_propeller_shaft_seals_*`, `research/Borddurchlass-*` und `Forschung_Niedergang_Dichtungen_2026.md` duplizieren Themen, die im gepflegten Korpus (`01_02`, `01_06`, `01_05`/`07_02`) bereits abgedeckt sind. Sie werden vom Loader nicht geladen, sind aber im Repo und driften inhaltlich auseinander → wer sie findet, bekommt evtl. veraltete/abweichende Fakten. Der Loader lädt zudem potenziell das **Duplikat `24_05`** doppelt (Teilaudit 2, Dimension knowledge_pipeline — noch zu verifizieren). — M

### MITTEL

- **ISO 12215 fehlt in der CLAUDE.md-Normtabelle.** Die Spec listet für Layout 12217/9094/15085/11812/12216/10133/13297, aber **nicht ISO 12215 „Hull construction and scantlings"** — obwohl `structural` ein Kernmodul mit Scantling-/Laminatplan-Bezug ist und die Recherche (`04_*`, `15_*`) explizit auf 12215 aufbaut. Passend dazu der Recherche-Befund `02_04`: dort wird fälschlich ISO 12217 (Stabilität) für Struktur zitiert — dieselbe Verwechslung, die die unvollständige Spec-Tabelle begünstigt. — S
- **Confidence-Code-Set: Spec vs. Code-Realität.** CLAUDE.md definiert 9 kanonische Codes; `score_fusion.py` emittiert zusätzlich nicht-kanonische Werte (`measured+visual`, `visual_only`, `discrepant`, bare `insufficient`) (Teilaudit 2). Die Spec müsste entweder Fusions-Codes definieren oder der Code sich auf die 9 beschränken. — M
- **Orchestrator-Cost-Abhängigkeit: nominell in Spec, nicht im Datenfluss.** CLAUDE.md „Tier 3: cost (needs materials, structural, production)". Im Code stimmt nur die Reihenfolge, die Daten werden `run_cost_analysis` nie übergeben (Teilaudit 2). Spec suggeriert eine Kopplung, die es nicht gibt. — M
- **Zählstände in Index/Meta veraltet.** `KNOWLEDGE_INDEX.py` und Kategorie-Titel nennen „249 Recherche-Dokumente" bzw. „72 Dateien, 270K+ Zeilen"; real sind es **252** nummerierte Dateien in 31 Kategorien (~840K Zeilen). Der Index als „Referenz für Vollständigkeit" (eigener Docstring) ist damit selbst nicht vollständigkeits-treu. — S
- **Companionway-Sill: Spec-Tabelle vs. per-Klasse-Overrides.** CLAUDE.md/Code-Tabelle A/B/C/D=300/250/150/0, aber `compliance.py` überschreibt sie klassenweise abweichend (Teilaudit 2, HOCH). Spec beschreibt die kanonische Tabelle, der Code weicht ab — die Spec müsste die Klassen-Overrides entweder legitimieren oder der Code die Tabelle nutzen. — S

### NIEDRIG
- **Fremd-Skill-Packs im Repo.** Sechs Skill-Verzeichnisse (`.claude/skills`, `bencium-skills`, `vercel-skills`, `nextlevel-skills`, `accesslint-skills`, `ui-ux-pro-max`) sind eingecheckt und blähen das Repo/den Audit-Suchraum auf. `.gitignore` wurde modifiziert (evtl. bereits adressiert). — S
- **Betriebsdokumente nicht aus CLAUDE.md verlinkt.** `DEPLOY.md`, `INTEGRATION_ANWEISUNG.md` existieren, sind aber in der Spec nicht referenziert; ein Entwickler findet den Deploy-Pfad (und die SECRET_KEY-Pflicht!) nur zufällig. — S

---

## Offene Fragen
1. **Design-Docs-Aktualität**: Beschreiben die 15 `docs/superpowers/`-Dokumente (bis 4.226 Zeilen) den Ist-Zustand, oder sind es historische Pläne? Das ist die größte offene Prüfung (siehe Abdeckung) und entscheidet, ob sie Referenz oder Archiv sind.
2. **Soll CLAUDE.md die Plattform-Schicht (Auth, Subscription, i18n, Wissenssystem, Deploy) aufnehmen** oder gibt es dafür bewusst separate Docs? Ohne Aufnahme bleibt die Spec als „Definitive Engineering Specification" (eigener Titel) unvollständig.
3. **Scope-Entscheidung Motoren** (siehe Recherche-Bericht, Offene Frage 3) — betrifft Spec UND Recherche.
4. **Verwaiste Root-/`research/`-/`knowledge_base/`-Dateien**: löschen, archivieren oder in den Korpus überführen?

## Top 10 Prioritätenliste für die Fix-Phase
1. **Auth/Sicherheit in CLAUDE.md spezifizieren** (HOCH, M) — inkl. SECRET_KEY-Pflicht (verzahnt mit Code-Top-1).
2. **Subscription-/Tier-Modell in CLAUDE.md spezifizieren** (HOCH, M) — als serverseitige Schranke.
3. **Scope-Entscheidung Motoren treffen & in Spec+Recherche angleichen** (HOCH, L).
4. **Verwaiste Recherche-Duplikate bereinigen** (HOCH, M) — inkl. `24_05`-Duplikat.
5. **ISO 12215 in CLAUDE.md-Normtabelle ergänzen** (MITTEL, S) — behebt zugleich die Wurzel des `02_04`-Recherche-Fehlers.
6. **Confidence-Code-Set Spec↔Code angleichen** (MITTEL, M) — Fusions-Codes definieren oder eliminieren.
7. **Cost-Abhängigkeit: Spec-Text an Code angleichen oder Datenfluss verdrahten** (MITTEL, M).
8. **Index/Meta-Zählstände auf 252/31 aktualisieren** (MITTEL, S).
9. **Design-Docs-Konsistenzprüfung durchführen** (offene Dimension, L) — 15 Dokumente gegen Code diffen.
10. **Betriebsdocs aus CLAUDE.md verlinken + Skill-Packs aus Repo entfernen** (NIEDRIG, S).

## Nachtrag: Konsistenz der Design-/Plan-Dokumente (`docs/superpowers/`) — 6 geprüft

**Ergebnis: Alle 6 geprüften Design-Specs/Pläne sind gegenüber dem gebauten Code veraltet.** Zwei systematische Drifts durchziehen sie und beantworten zugleich Offene Frage 1 (die Docs sind **historische Pläne, keine gültige Referenz**):

1. **Datenmodell veraltet (4 → 13 Bootsklassen):** Jede Doc beschreibt nur die 4 Legacy-Klassen (`small_sail`, `cruising_sail`, `large_motor`, `superyacht`); der reale Code (`schemas.py` `BoatClass`-Enum) hat **13** (u.a. `racing_sail`, `trawler`, `explorer`, `catamaran_*`). Alle Modul-`BOAT_CLASS_DEFAULTS` hängen an den 13.
2. **Sub-Analysen & Gewichte gedriftet:** structural 4→6, ergonomics 5→8, compliance 6→10, materials 5→8 — mit neu verteilten Gewichten, die in **keiner** Doc stehen.

**Neue Befunde:**
- **HOCH — `specs/2026-03-18-aydi-phase1-design.md`**: `BoatClass` als 4-Werte-Enum spezifiziert; Code hat 13. Wer Enum/Validierung/Tests aus der Spec ableitet, baut ein 4-Klassen-System und lehnt die 9 produktiv aktiven Klassen ab. — M
- **HOCH — `specs/2026-03-18-structural-analysis-design.md`**: Return-Contract-Abweichung — Spec legt genau 4 `sub_scores`-Keys fest, Code liefert 6 (zusätzlich `loading_conditions`, `trim`). Ein Consumer, der 4 Keys erwartet, validiert die Antwort als fehlerhaft. — M
- **HOCH — `plans/2026-03-18-compliance-checker.md`**: Der **eigene Integrationstest** des Plans assertet `len(sub_scores) == 6`; der Code registriert **10** Sub-Analysen (escape_hatch/cockpit_drain/companionway_sill/ventilation zusätzlich, passend zu CLAUDE.md). **Der Plan-Test würde gegen den aktuellen Code fehlschlagen.** — M
- **HOCH — `plans/2026-03-18-material-analysis.md`**: analog — Plan-Test assertet `== 5`, Code hat **8** (lifecycle_cost/uv_exposure/moisture_risk). **Test schlägt fehl.** — M
- **MITTEL — `specs/2026-03-19-boat-dna-design.md`**: baut auf der inzwischen **ungültigen** Kern-Invariante „Existing modules Unchanged / nur 4 Klassen / alle 457 Tests grün". Real wurden alle Module verändert; `BoatDNA.from_boat_class` kennt nur 4 Presets, während das Enum 13 anbietet → `boat_class='trawler'` wirft `ValueError`, obwohl das Enum die Klasse zulässt. — M
- **MITTEL (mehrfach):** veraltete Gewichts-/Klassentabellen in structural-, compliance-, material-Docs.
- **NIEDRIG — `specs/2026-03-19-community-intelligence-design.md`**: als einzige gut synchron (Orchestrator-Tier-1, `score_fusion`, `OVERALL_WEIGHTS` stimmen) — nur die `BOAT_CLASS_DEFAULTS`-Tabelle listet 4 statt 13 Klassen.

**Muster-Konsequenz (Erweiterung von Muster D):** Nicht nur CLAUDE.md, auch die Modul-Design-Docs tracken den Code nicht. Zwei Docs enthalten sogar **Tests, die gegen den Ist-Code fehlschlagen** — sie sind damit aktiv irreführend, nicht bloß unvollständig. Empfehlung: als „Archiv/historisch" kennzeichnen oder auf den 13-Klassen-/erweiterten-Sub-Analysen-Stand heben.

---

## Abdeckung & Fortsetzung
**Abgedeckt:** CLAUDE.md-Vollständigkeit, Spec↔Code (verzahnt mit Teilaudit 2), Spec↔Recherche (Kernpunkte), Bestandsinventur/Duplikate, **6 der 15 Design-Docs** (die kern-modulnahen). **Offen:** die restlichen 9 `docs/superpowers/`-Dokumente (emotional-, production-, volume-storage-, community-intelligence-Plan, ui-ux-polish, aydi-phase1-Plan) — angesichts des durchgängigen Musters ist bei ihnen dasselbe Veraltungsbild zu erwarten; Stichprobe genügt zur Bestätigung.
