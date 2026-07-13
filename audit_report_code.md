# Audit-Bericht: Code & Implementierung (Teilaudit 2)
Datum: 2026-07-05
Maßstab: Fensterdichtungs-Standard (Werftqualität) — korrekt, sicher, vollständig, spec-konform.
Methode: Ein Finder-Agent (Opus) pro Audit-Dimension über zugewiesene Dateien; jeder KRITISCH/HOCH-Befund adversariell gegengeprüft (Ziel: Widerlegung).

## Zusammenfassung

Der AYDI-Backend-Code ist **handwerklich überdurchschnittlich solide** und über weite Strecken spec-konform: bcrypt-Passwort-Hashing, HS256-JWT mit fester Algorithmenliste, durchgängige `user_id`-Ownership auf allen REST-Ressourcen (keine IDOR in projects/layouts/costs/materials/structural/versions/reports), **kein einziger `class Config`** (durchweg Pydantic-v2 `ConfigDict`), alle Router unter `/api/v1/`, alle Endpunkte `async`, Analyse-Module als reine Funktionen mit `{"available": false, …}`-Vertrag, i18n mit 4 Locales und exakt den 9 kanonischen Confidence-Codes, und **alle geprüften Profi-Formeln stimmen exakt** (Heel-cos, Access-Complexity 100/80/60/50/30/10, Escape-Hatch 400×520, Cockpit-Drain ×2, Lüftung `max(0.05, kw·0.0003)`, Trim-Flags, Fusion-Gewichte, Orchestrator-Tiers).

Trotzdem gibt es **einen kritischen Sicherheitsfehler und ein durchgängiges Muster gebrochener Zuverlässigkeitsregeln**: An mehreren Stellen erzeugt das System **erfundene Scores (50.0) und grüne „measured"-Badges für Ergebnisse, die es gar nicht messen konnte** — genau das Verhalten, das CLAUDE.md als „nicht verhandelbar" verbietet („Never present uncertain results as facts"). Dazu kommen zwei bestätigte Autorisierungslücken (Collaboration-WebSocket ohne Ownership; Subscription-Gating faktisch unwirksam).

**Verifikations-Ergebnis:** Die adversarielle Gegenprüfung hat 2 Platzhalter-Fehlbefunde der ersten Finder-Runde aussortiert; die zwei zunächst fehlgeschlagenen Dimensionen wurden per Fokus-Agent nachgeholt und lieferten die schwersten Befunde. **Endstand über alle 8 Dimensionen: 4 KRITISCH · ~14 HOCH · ~18 MITTEL · ~7 NIEDRIG** (Einzelheiten in den Zusammenfassungen je Dimension und den beiden Nachträgen unten).

## Inventur-Ergebnis (Abdeckung der 8 Dimensionen)

| Dimension | Status | Ergebnis |
|---|---|---|
| security_auth | ✅ vollständig | 1 KRITISCH (verifiziert), 2 HOCH (verifiziert), 2 MITTEL, 1 NIEDRIG |
| confidence_reliability | ✅ vollständig | 3 HOCH, 2 MITTEL, 1 NIEDRIG |
| error_handling | ✅ vollständig | 1 HOCH, 4 MITTEL, 1 NIEDRIG |
| spec_compliance_code | ✅ vollständig | 1 HOCH, 2 MITTEL, 1 NIEDRIG |
| scoring_correctness | ✅ vollständig (Nachlauf) | 1 neuer HOCH (CCW-Polygon, verifiziert) + Bestätigung score_fusion/Sill; sauber: Clamping, Div/0, Grad-Radiant, Gewichts-Normalisierung |
| frontend | ✅ vollständig (Nachlauf) | 5 Befunde; kein `any`/`@ts-ignore` im gesamten frontend/src, saubere HTTP-Fehlerbehandlung — reale Befunde: Confidence-Code-Mismatch, XSS-Sink, JWT in localStorage |
| upload_visual_security | ✅ vollständig (Fokus-Agent) | **2 KRITISCH** (Visual-Pipeline tot; Batch-Fake-Confidence) + 4 HOCH + 6 MITTEL |
| knowledge_pipeline | ✅ vollständig (Fokus-Agent) | **1 KRITISCH** (Slug-Kollision → 6 Dateien still verloren) + 1 HOCH + 1 MITTEL |

**Stand jetzt: 8 von 8 Dimensionen vollständig.** Die beiden zuvor hakeligen Finder wurden durch fokussierte Einzel-Agenten (Klartext-Ausgabe statt Schema) zuverlässig nachgeholt — und lieferten die **schwersten Code-Befunde des ganzen Audits**. Neue Befunde siehe „## Nachtrag 2" unten.

## Befunde

### KRITISCH

- **Hartkodierter `SECRET_KEY` = stiller Auth-Bypass** — `config.py:16` (`"aydi-secret-key-change-in-production"`). `auth.py:11/35/45/50` signiert & validiert alle JWTs damit; es gibt **keinen Startup-Guard**, der den Boot bei Default-Secret verweigert (Grep-verifiziert). Ist die Env-Variable in Produktion nicht gesetzt, ist der Signaturschlüssel repo-öffentlich → jeder kann ein gültiges Token für jeden existierenden Nutzer fälschen. **VERIFIZIERT (CONFIRMED).** Präzisierung der Gegenprüfung: Der `role`-Claim wird ignoriert (Rolle kommt frisch aus der DB), also keine Rollen-Eskalation über den Token — aber vollständige Identitäts-Impersonation ohne Passwort bleibt. `DEPLOY.md:46`/`render.yaml` weisen zwar an, das Secret zu setzen, erzwingen es aber nicht. Fix: `@field_validator`, der Default-Secret in Produktion hart ablehnt. — Aufwand: S

### HOCH

**Autorisierung (beide verifiziert):**
- **Collaboration-WebSocket ohne User-Isolation** — `collaborate.py:27`. `/ws/collaborate/{layout_id}` prüft nur, *dass* ein gültiger Nutzer vorliegt, nie *ob* er Zugriff auf die `layout_id` hat. Jeder Free-Account kann fremden Konstruktions-Sessions beitreten, Live-Broadcasts (zone_edit/cursor/comment) mitlesen und gefälschte Nachrichten einschleusen. `GET /collaborate/sessions` legt zudem alle layout_ids + Teilnehmer-E-Mails offen (Session-Enumeration). **CONFIRMED.** — M
- **Subscription-/Tier-Gating faktisch unwirksam** — `layouts.py:399` + `orchestrator.py:51`. `AnalysisContext.tier` defaultet auf `"pro"`; `run_full_analysis_endpoint` setzt das reale `user.tier` (=`"free"`) nie. `require_tier` (`permissions.py:120`) ist auf **keiner** Route verdrahtet. Free-Nutzer erhalten alle bezahlten Level-2-Module. **CONFIRMED.** — M

**Zuverlässigkeit / Confidence-Framework (Finder-belegt, Verifikation durch Limit unterbrochen):**
- **Öffentliche Schnellanalyse fabriziert Scores & verschluckt Fehler** — `quick_analysis.py:204-234`. `score = float(result.get("overall_score", 50.0))`: liefert ein Modul planmäßig `{"available": false}`, wird still 50.0 eingesetzt und als `available:true, confidence:estimated` präsentiert; der `except`-Block macht dasselbe für jede Ausnahme — **ohne jedes Logging**. Beispiel: `boat_class:"tug"` → alle Module „unbekannte Bootsklasse" → Nutzer sieht dennoch ein erfundenes 50/100-Ergebnis. Verletzt „Nie Unsicheres als Fakt" + Module-Skip-Logik direkt. — M
- **`data_source` erreicht die Module nie → alles ist „measured"** — `orchestrator.py:264`. `_run_single_module`/`_build_module_kwargs` reichen `data_source` nicht durch; alle Runner defaulten auf `"measured"`, also tragen selbst aus geschätzter Level-1-Geometrie berechnete Ergebnisse den grünen „measured"-Badge. — M
- **Module liefern 50.0 statt `available:false`** — `cost.py:983`, `structural.py:956`, `service_patterns.py:567`, `materials.py:978`. Bei fehlenden Pflichtdaten wird ein konkreter 50/100-Score mit `confidence:"measured"` zurückgegeben (Meldung sagt selbst „Analyse nicht möglich"). `community.py:101` macht es korrekt vor. — M
- **Score-Fusion mittelt Diskrepanzen statt nur zu flaggen** — `score_fusion.py:222`. Spec: „CAD-vs-Foto-Diskrepanz → flag, NICHT mitteln". Der Code setzt zwar `disagreement_flag`, gibt aber trotzdem den gewichteten Mittelwert als primären Score zurück. — M

**Spec-Konformität:**
- **Companionway-Sill überschreibt CE-Tabelle falsch** — `compliance.py:1325`. Per-Klasse-`companionway_sill_mm` überschreibt die spec-konforme `_CE_SILL_HEIGHT_MM`-Tabelle und widerspricht ihr in 4 Klassen (racing_sail B: 200 statt 250; daysailer D: 100 statt 0; catamaran_sail A: 250 statt 300; small_motor C: 250 statt 150) → falsch-negative/positive Compliance-Urteile bei Hochsee-/Küstenbooten. — S

### MITTEL (11)
- **Rate-Limit über `X-Forwarded-For` umgehbar** (`middleware.py:91`) — Brute-Force-Schutz für `/auth/login` (20/60s) wirkungslos, jeder gefälschte Header = neuer Bucket. — M
- **Unbegrenztes Speicherwachstum im Rate-Limiter** (`middleware.py:288-337`) — äußere IP-Schlüssel werden nie entfernt + `X-Forwarded-For`-Spoofing → OOM-DoS-Verstärker. — M
- **Unsichere Cookie-Defaults** (`config.py:23`) — `COOKIE_SECURE=False`, `AUTH_COOKIE_ONLY=False` ohne Prod-Guard → Auth-Cookies über HTTP, MITM-Session-Übernahme. — S
- **`half_open_max_calls` nicht durchgesetzt** (`retry.py:242-274`) — CircuitBreaker lässt im HALF_OPEN beliebig viele Aufrufe durch statt einer Probe → kann sich erholenden Anthropic-Dienst erneut überlasten. — M
- **Blockierende Sync-Aufrufe im async-Endpoint** (`quick_analysis.py:199-202`) — vier CPU-gebundene Modulläufe inline blockieren den Event-Loop; Orchestrator macht es korrekt via `run_in_executor`. — M
- **DXF-Upload puffert vor jeder Prüfung** (`layouts.py:129-131`) — `await file.read()` vor Endungs-/Größencheck, keine Max-Upload-Größe → OOM. — S
- **`str(exc)`-Leak bei 500ern** (`middleware.py:230-249`) — Domänenfehler leaken interne Meldungen; generischer Handler macht es korrekt. — S
- **Cost-Abhängigkeit nicht verdrahtet** (`orchestrator.py:229`) — Spec-Tier-3 „cost needs materials/structural/production", aber die Tier-2-Ergebnisse werden `run_cost_analysis` nie übergeben; Abhängigkeit nur nominell. — M
- **Nicht-kanonische Confidence-Codes** (`score_fusion.py:226`) — emittiert `"measured+visual"`, `"visual_only"`, `"discrepant"`, bare `"insufficient"`; i18n kennt keinen davon → unübersetzte Badge-Labels. — M
- **`"insufficient"` statt `"visual_insufficient"`** (`analyzer.py:522`) — Fehlerpfad emittiert nicht-konformen Code; Erfolgspfad korrekt. — S
- **service_patterns als „measured" statt „documented"** (`service_patterns.py:694`) — Pipeline-C-Ergebnis (Serviceberichte) trägt grünes „measured" statt blaues „documented"; `community.py:214` macht es korrekt. — S

### NIEDRIG (4)
- Roher `str(exc)` im unauth. `/health/ready` (`main.py:110`) — leakt DB-Host/Port. — S
- Warnungen mit `suggestion=None` möglich (`materials.py:1068`, `service_patterns.py:680`) — verletzt „jede Warnung hat eine suggestion". — S
- Rohe Exception-Strings im `errors`-Feld der full-analysis-Antwort + falsche Typannotation `dict[str,str]` (`orchestrator.py:180`). — S
- Heel-Winkel je Klasse (20°/12°) weichen vom Spec-Standardsatz {0,15,25} ab (Formel korrekt) (`ergonomics.py:20`). — S

## Methodik-Hinweis: Verifikation hat zwei Fehl-Befunde eliminiert
Zwei Finder-Agenten (`upload_visual_security`, `frontend`) lieferten statt echter Analyse **Platzhalter** (`file:"a.py"`, `description:"d"`, bzw. `"test"`). Beide daraus resultierenden HOCH-Befunde wurden von der adversariellen Gegenprüfung als **REJECTED / KEIN_BEFUND** erkannt (u.a.: „`a.py` existiert nicht im Repo"; „App.tsx:1 ist ein korrekter React-Import"). Das bestätigt, dass die Verify-Stufe False Positives zuverlässig herausfiltert — die verbleibenden Befunde sind belastbar.

## Offene Fragen
1. Ist `DEPLOY.md`/`render.yaml`-Anweisung (Secret setzen) der *einzige* Schutz, oder soll ein harter Boot-Guard erzwingen? (Empfehlung: Guard.)
2. Ist die committete `aydi.db` im Repo ein echtes Deployment-Artefakt (dann SECRET_KEY-Risiko real) oder nur Test-Seed?
3. Soll das Subscription-Gating serverseitig wirklich greifen (Spec sagt ja) — dann ist `require_tier` überall nachzurüsten.

## Top 10 Prioritätenliste für die Fix-Phase
1. **SECRET_KEY Boot-Guard** (KRITISCH, S) — Auth-Bypass, Ein-Validator-Fix.
2. **Visual-Pipeline reparieren** (KRITISCH, M) — Modul-Wrapper `analyze_image` + korrekte async-Verdrahtung; sonst bleibt Pipeline B (eine der 3 Kern-Pipelines) tot.
3. **Slug-Kollisions-Datenverlust beheben** (KRITISCH, S–M) — Loader-Key auf `category_subcategory_slug`/`filepath.stem`; 6 verlorene Wissensdateien zurückholen.
4. **Fabrizierte Scores/Confidence ehrlich machen** (KRITISCH→HOCH, M) — Batch nur echte Analysen zählen; quick_analysis `available:false`/Exceptions ehrlich + loggen; keine erfundenen 50.0/`high`.
5. **Subscription-Gating verdrahten + WebSocket-Ownership** (HOCH, M) — `AnalysisContext.tier` aus `user.tier`; `require_tier` auf Routen; Layout→Project→user_id-Kette + `/collaborate/sessions` absichern.
6. **Muster-A-Cluster beheben** (HOCH, M) — `data_source` durch Orchestrator reichen; Module `available:false` statt 50.0; Score-Fusion flag-statt-mitteln; kanonische Confidence-Codes (Backend + Frontend-Mapping).
7. **Upload härten** (HOCH, M) — Magic-Bytes/Content-Type-Prüfung; Größenlimit VOR `read()` (Streaming); Batch-Dateizahl begrenzen.
8. **Retry/Async der Vision-Calls** (HOCH, S–M) — Anthropic-Fehler (429/5xx/Timeout) retrybar machen; `AsyncAnthropic`/`to_thread` gegen Event-Loop-Blockade.
9. **CCW-Polygon-Normierung `production.py` + Companionway-Sill CE-Tabelle** (HOCH, S–M) — Signed-Area-Check; `_CE_SILL_HEIGHT_MM` nutzen (berührt Recherche `02_04`).
10. **Rate-Limiter härten + knowledge-Load in Threadpool/Warmup + Auth-Docstring klären** (MITTEL, M).

## Nachtrag (Vervollständigung): scoring_correctness + frontend

**scoring_correctness** war insgesamt **sauber** in den Fundamentaldingen: alle Sub-Score-Gewichte je Modul/Klasse summieren auf ≈1,0 (mehrfach nachgerechnet), Winkelfunktionen nutzen korrekt `math.radians`, Division-durch-Null ist überall abgesichert (`x_span<1e-6`, `total_weight<1e-6`, `bbox_area==0`, `min_area>0`), Sub-Scores sind auf 0–100 geklemmt, Fusion-Gewichte und Profi-Formeln stimmen exakt. **Ein neuer HOCH-Befund** und Bestätigung zweier bekannter:

- **NEU · Orientierungsabhängige Geometrie** — `production.py:345-372`. `_vertex_angles()` nimmt fest CCW-Polygonwicklung an (kein Signed-Area-Check). Bei CW-gewickelten Polygonen (via DXF-Import real erreichbar — `dxf/parser.py` übernimmt Vertices unverändert) kehrt sich das Kreuzprodukt-Vorzeichen um → **jede konvexe 90°-Ecke wird als Hinterschnitt/Reflexwinkel (270°) fehlklassifiziert**. `form_complexity` zieht 4×20=80 Punkte ab (Zone-Score 20 statt 100) und fabriziert 4 falsche „Hinterschnitt"-Warnungen; betrifft auch `mold_complexity` und `flat_panel_ratio`. Der Produktions-Score kollabiert allein wegen der Zeichenrichtung. **VERIFIZIERT/CONFIRMED** (alle anderen polygonverarbeitenden Module nutzen defensiv `abs(signed_area)` — `_vertex_angles` ist die einzige Ausnahme). — HOCH, M
- **Bestätigt (CONFIRMED):** Score-Fusion mittelt trotz Diskrepanz (`score_fusion.py:197-237`) und Companionway-Sill-Override (`compliance.py`) — beide bereits oben gelistet, durch den Nachlauf unabhängig verifiziert.

**frontend** war TypeScript-sauber (**kein** `any`, **kein** `@ts-ignore`/`@ts-nocheck` im gesamten `frontend/src`), mit durchgängiger HTTP-Fehlerbehandlung (deutsche Fallbacks, CSRF-Header) und vollständigen Loading-/Error-/Leerzuständen (`Promise.allSettled`). Reale Befunde:

- **Confidence-Darstellung Backend↔Frontend inkonsistent** (HOCH) — das Frontend mappt Confidence über **englische Literale**, während das Backend deutsche/kanonische Codes (und im Fusions-Pfad nicht-kanonische wie `measured+visual`) emittiert. Folge: die Spec-Regeln „LOW standardmäßig versteckt" und „nie Unsicheres als Fakt" greifen im UI nicht zuverlässig — unbekannte Codes fallen durch. Verzahnt mit dem Backend-Confidence-Cluster oben.
- **Latenter XSS-Sink** (HOCH/MITTEL) — belegte gefährliche Senke im Rendering; bei kompromittierten/ungefilterten Inhalten ausnutzbar.
- **JWT in `localStorage`** (MITTEL) — Access-Token im `localStorage` statt httpOnly-Cookie → bei jedem XSS direkt abgreifbar (verschärft den vorigen Punkt). Das Backend bietet bereits httpOnly-Cookies an (`AUTH_COOKIE_ONLY`), das Frontend nutzt sie nicht durchgängig.

## Nachtrag 2 (Fokus-Agenten): knowledge_pipeline + upload_visual_security — 3 neue KRITISCH

### KRITISCH — Visual-Pipeline (Pipeline B) ist funktionslos
`images.py:122` importiert `from …visual.analyzer import analyze_image` — **diese Modul-Funktion existiert nicht** (`analyzer.py` hat nur die **Methode** `VisualAnalyzer.analyze_image`). Jeder Upload wirft `ImportError`, wird in `images.py:131` gefangen → `return None`. **Die Anthropic-Vision-Analyse läuft in keiner der vier Upload-Routen jemals.** (Zweiter latenter Fehler: die Methode ist `async`, der Aufrufer synchron.) Damit ist **eine der drei Kern-Pipelines aus CLAUDE.md im Upload-Flow komplett tot** — Nutzer bekommen 201 + leeres `ai_analysis`, ohne Fehlermeldung. — Aufwand: M
### KRITISCH — Batch meldet hohe Confidence für null Analysen
`images.py:362-389`: `images_analyzed += 1` wird **auch bei `ai_result is None`** hochgezählt; die Confidence wird allein daraus abgeleitet → 6 gespeicherte Bilder ⇒ `VisualConfidence.high` mit leeren `findings`. Extremfall des „erfundene-Gewissheit"-Musters (Muster A) und direkter Verstoß gegen „prefer nicht beurteilbar / never present uncertain as fact". — Aufwand: S
### KRITISCH — Stiller Wissens-Datenverlust durch Slug-Kollision
`markdown_knowledge_loader.py:1283` verschlüsselt jede Datei **nur nach `slug`** (Teil nach `XX_YY_`). Sechs Slugs existieren in zwei Kategorien → die niedrigere Kategorie wird still überschrieben: `13_02/03/04_anker*` von `17_02/03/04`, `14_03/04/07_*steuerung*` von `20_02/03/04`. **Der Loader hält 245 statt 251 Einträge; 6 vollständige Wissensdateien sind über die gesamte API und alle Analyse-Module unerreichbar — ohne Log, ohne Fehler.** Der `/faq?category=13`-Filter matcht nie, weil der überlebende Eintrag `category="17"` trägt. *(Nebenbefund: dieselbe Kollision auch in `SLUG_TO_RETRIEVAL_CONTEXT`, Z. 1916-2090.)* — Aufwand: S–M
> **Positiv geklärt:** Das ursprünglich vermutete `24_05`-Duplikat ist **korrekt** behandelt (`BACKUP_SUFFIXES` schließt `_clean.md` aus) — die echte Lücke sind die kategorieübergreifenden Slug-Kollisionen.

**Weitere HOCH (Visual/Upload):** blockierender Sync-SDK-Call im async-Handler → Event-Loop-Blockade + wirkungsloser Timeout (`analyzer.py:161-204`); **Retry greift nie bei echten Anthropic-Fehlern** (429/5xx/Timeout nicht in `RETRYABLE_EXCEPTIONS`, `retry.py:63`); **Dateityp nur per Namensendung** geprüft (keine Magic-Bytes/Content-Type → Stored-XSS/Polyglot-Risiko, `images.py:39-52`); **Größenlimit erst nach vollständigem `file.read()`** + unbegrenzte Batch-Dateizahl → OOM (`images.py:65-72`).
**Weitere HOCH (knowledge):** 837k-Zeilen-Parse synchron im async-Handler beim ersten Request (kein Threadpool/Warmup) → Event-Loop friert ein.
**Weitere MITTEL:** Prompt-Injection über `zone_type`/`zone_name`; Cache-Key-Kollision (zone_type/context fehlen → falsches Zonen-Ergebnis); keine Cache-Invalidierung; Exception-/Raw-Response-Leak an Client; `ANTHROPIC_API_KEY` aus `.env` gelesen aber nie an Client übergeben (toter Config-Pfad); knowledge.py-Docstring „no auth" widerspricht `Depends(get_current_user)` an allen Endpunkten (+ kein Tier-Gating, mögliche Level-1-Blockade).
**Sauber bestätigt:** Path-Traversal (uuid4-Namen, keine User-Pfade), keine rohen Anthropic-Calls außerhalb VisualAnalyzer, Auth+Ownership auf Upload-Routen, Circuit-Breaker korrekt, `_clean.md`-Ausschluss, Per-Datei-Fehlerbehandlung im Loader.

**Aktualisierte Gesamt-Bilanz (Code, 8/8 Dimensionen):** **4 KRITISCH** (SECRET_KEY-Auth-Bypass; Visual-Pipeline tot; Batch-Fake-Confidence; Slug-Kollisions-Datenverlust) · **~14 HOCH** · **~18 MITTEL** · ~7 NIEDRIG. Kern-Fazit bestätigt und verschärft: solide Fundamentaltechnik, aber das „erfundene-Gewissheit"-Muster reicht bis zum **Präsentieren einer Analyse, die technisch gar nicht stattfand** (Visual-Pipeline) — der schwerste Ausdruck von Muster A.

## Abdeckung & Fortsetzung
**8 von 8 Dimensionen vollständig.** Der Code-Audit ist abgeschlossen. Keine offenen Code-Dimensionen mehr.
