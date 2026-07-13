# Audit-Bericht GESAMT — AYDI Vollständiger Qualitätsaudit
Datum: 2026-07-05
Zusammenführung von Teilaudit 1 (Recherche), 2 (Code), 3 (Spezifikation).
Maßstab durchgehend: **Fensterdichtungs-Standard** — „Könnte jemand sein Problem allein mit dieser einen Stelle lösen?"

---

## Gesamtzustand in fünf Sätzen

AYDI ist substanziell und über weite Strecken auf hohem Niveau gebaut: ein sauber strukturiertes FastAPI-Backend mit korrekten Kernformeln und exakter Spec-Code-Treue bei der Analyse-Engine, dazu ein außergewöhnlich umfangreicher Wissenskorpus (252 Dokumente, ~840.000 Zeilen). Der Qualitätsanspruch bricht jedoch **an drei wiederkehrenden Nähten**: (1) Das System und der Korpus präsentieren **Unsicheres/Unbekanntes als gemessene Gewissheit** — genau die eine Regel, die CLAUDE.md als „nicht verhandelbar" bezeichnet. (2) **Zwei Wahrheitsquellen driften auseinander** — Haupttext vs. Anhang im Korpus, Spec vs. Code-Realität, Design-Docs vs. gebauter Code, kanonische vs. tatsächlich emittierte Confidence-Codes. (3) **Sicherheit und Sicherheits-kritisches sind am schwächsten abgedeckt** — die dünnsten Recherche-Dokumente sind ausgerechnet Rettungsmittel/MOB/Feuerlöschung (Kat. 29: **0 von 9 erfüllen den Standard**), und die schwersten verifizierten Einzelfehler betreffen Auth (SECRET_KEY), die Gasdruckfeder-Auslegung, die Rettungsinsel-Auslösetiefe und mehrere Strukturberechnungen (Kiel, Ruder, Ballast). Der Kern ist gut; die Ränder, an denen Gefahr entsteht, sind es noch nicht.

**Einschränkung der Aussagekraft:** Ein hartes Session-Token-Limit zwang die Tiefenprüfung in mehrere Durchläufe. Aktueller Stand: **110 von 252 Recherche-Dokumenten** tiefengeprüft — **mindestens eine Tiefenprüfung in jeder der 31 Kategorien** (Kernkategorien 01/02 + gesamte dünne Region 26–31 + repräsentative Stichprobe 03–25), alle 252 triagiert; **Code-Audit vollständig (8/8 Dimensionen)**; **6 von 15 Design-Docs** geprüft. Damit ist der Audit inhaltlich repräsentativ für das Gesamtprojekt. **Kernzahl: von 110 tiefengeprüften Recherche-Dokumenten erfüllen nur 20 (18 %) den Fensterdichtungs-Standard.** Die Befunde sind belastbar (KRITISCH-Befunde adversariell gegengeprüft — die Verifikation hat u.a. einen KRITISCH-Verdacht widerlegt und mehrere Platzhalter-Fehlbefunde aussortiert); die Recherche-Abdeckung ist mit 17 % noch unvollständig (Details je Teilbericht).

---

## Muster, die bereichsübergreifend auftreten

Diese Muster sind der eigentliche Kern des Audits — sie sind keine Einzelfälle, sondern strukturell:

### Muster A — „Erfundene Gewissheit" (in allen drei Bereichen)
Das System behauptet Präzision, die es nicht hat.
- **Recherche:** Widersprüchliche Werte für dasselbe Produkt, **beide** mit „Confidence: measured"; ~1.300 Zeilen unverifizierbare Forum-Anekdoten pauschal als „documented" (`02_05`).
- **Code:** Fabrizierte 50.0-Scores bei fehlenden Daten statt `available:false`; `data_source` erreicht die Module nie, alles wird „measured"; CAD-vs-Foto-Diskrepanz wird gemittelt statt geflaggt; quick_analysis erfindet Ergebnisse und loggt nichts. **Der Extremfall:** die Batch-Foto-Analyse meldet `VisualConfidence.high` für **null tatsächlich gelaufene Analysen** — weil die Visual-Pipeline (Pipeline B) durch einen Import-Bug (`images.py:122`) **komplett tot** ist. Das System präsentiert also eine Analyse mit hoher Zuverlässigkeit, die technisch **nie stattgefunden hat**.
- **Spec:** CLAUDE.md formuliert die Regel „Never present uncertain results as facts" prominent — die Realität verletzt sie an mindestens 6 Code-Stellen und flächig im Korpus.
→ **Höchste Hebelwirkung des gesamten Audits.** Ein System, das „nicht beurteilbar" sagen können soll, tut es an den entscheidenden Stellen nicht.

### Muster B — Body-vs-Anhang-Widerspruch: der korpusweit dominante Defekt
Die Stichprobe über alle großen Kategorien (03–25) hat dies vom „Kat.-01/02-Muster" zum **projektweiten Hauptbefund** erhoben: **Nur 20 von 110 tiefengeprüften Dokumenten (18 %) erfüllen den Standard**, und der mit Abstand häufigste Grund ist, dass **Haupttext (Abschn. 1–26) und Anhänge (P–AM) für denselben Wert Gegensätzliches behaupten — systematisch beide als „Confidence: measured"**.
- **Nicht kosmetisch, sondern sicherheitsrelevant:** Im Hardware-Teil trifft der Widerspruch **Traglasten, Bruchlasten, Prüfdrücke, Drehmomente, Sicherheitsfaktoren** — adversariell **verifiziert** u.a. bei Decksluken (Prüfdruck 6 vs. 12–18 vs. 49–74 kPa), Blöcken/Schäkeln/Klampen (WLL/Festigkeit), Gasschläuchen, Autopilot-Rudermoment, Schrauben-Drehmoment.
- **Spec/Code-Ausprägung:** kanonisches Confidence-Set vs. tatsächlich emittierte Codes; Spec-Sill-Tabelle vs. Code-Overrides; Index-Zählstand „249"/„72" vs. real 252/245.
→ Ursache: additive Erzeugung (Anhänge nachträglich angehängt) ohne Rückabgleich mit dem Haupttext. Der einzig skalierbare Fix ist ein **systematischer Haupttext-vs-Anhang-Diff über den gesamten Korpus** (nicht Einzelkorrekturen) plus Umkennzeichnung der Anhänge als „documented, unverified".

### Muster C — Sicherheit ist die dünnste Naht (über die gesamte dünne Region bestätigt)
Die Tiefenprüfung **aller** dünnen Kategorien bestätigt das Muster mit Nachdruck: **Kat. 26–31 — 0 von 45 Dokumenten erfüllen den Standard** (Ø ≈ 35/100). Die dünnsten Dokumente sind zugleich die mit den **meisten sicherheits-/strukturkritischen Sachfehlern** (~22 KRITISCH), viele **web-verifiziert**: Rettungsinsel-HRU-Auslösetiefe falsch (führt zu gefährlicher Fehl-„Kalibrierung"), ISO-12402-Rettungswestenklassen falsch, Karabiner-Bruchlast um Faktor 3 widersprüchlich, Hydrostatik-/Kielbolzen-/Ruder-Formeln fehlerhaft, **Trailer-Grenzwerte gefährlich falsch (TÜV/750 kg)**, **giftiges Ethylenglykol als Heizmittel empfohlen + fehlende CO/Gas-Dimension**. Dazu der verifizierte Gasdruckfeder-Faktor-2-Fehler, der Code-Auth-Bypass und die gefährliche Salzsäure-auf-Edelstahl-Empfehlung. → Der Bereich mit dem höchsten Schadenspotenzial ist der am wenigsten werftgerecht ausgearbeitete. *(Ausnahme-Ehrlichkeit: der zunächst als KRITISCH geführte MMA-Kiel-Widerspruch wurde bei Verifikation als Fehlbefund erkannt und entfernt.)*

### Muster G — Duplikation, Platzhalter, Fabrikation (dünne Kategorien 26–31)
Ein von Kat. 01/02 verschiedenes Zerfallsbild: **ganze Dokumente sind zweimal generiert und aneinandergehängt** (z.B. `26_03` mit „END OF DOCUMENT"-Marker mitten im File), mit **kollidierenden Fehlerbild-IDs** (`FB-26-XX-NNN` doppelt vergeben → zerstört Diagnose-Zuordnung und die AYDI-API `/heating/fault-images`), **Stub-Anhängen** („weitere 1.200 Zeilen", „[wird fortgesetzt]") und **erfundenen Fakten** (Normnummern, Hersteller-Herkünfte, Marktanteile). Diese Dokumente täuschen Umfang vor, ohne ihn zu liefern.

### Muster D — Dokumentation tracked den Code nicht
Zwei Ausprägungen: (a) **CLAUDE.md schweigt zur Plattform-Schicht** — Auth, Subscription/Tier, i18n, das 252-Dokumente-Wissenssystem und Deployment sind im Code real, in der Spec nicht spezifiziert — und genau dort sitzen die schwersten Code-Befunde (SECRET_KEY, Tier-Bypass, WebSocket). (b) **Die Modul-Design-Docs sind veraltet** — alle 6 geprüften `docs/superpowers/`-Dokumente beschreiben noch 4 statt 13 Bootsklassen und den alten Sub-Analysen-Stand; zwei Pläne enthalten sogar **Integrationstests, die gegen den heutigen Code fehlschlagen** (`len(sub_scores)==6`/`==5` vs. real 10/8). Undokumentiert = nicht erzwingbar; falsch dokumentiert = aktiv irreführend.

### Muster E — Normen/Internationalisierung als durchgängig schwache Ader
ISO-Verwechslungen ziehen sich durch alle Ebenen: Recherche (`02_04`: ISO 12217 statt 12215; `01_03`: EN 13906-2 falsch), Code (Compliance-Dict mit falscher ISO-Referenz), Spec (ISO 12215 fehlt in der Normtabelle). Eine einzige Wissenslücke pflanzt sich über alle drei Bereiche fort.

### Muster F — Duplikate & Verwaistes
Duplikat `24_05_*`/`_clean`, verwaiste Root-Recherchen (`marine_window_gaskets_research.md` etc.), committete Fremd-Skill-Packs. Housekeeping-Drift, niedrige Schwere, aber Widerspruchsquelle.

---

## Projektweite Top-10-Prioritätenliste (aus den drei Teil-Top-10)

Sortiert nach Schaden × Hebelwirkung × (niedriger) Aufwand. Verzahnte Befunde sind zusammengefasst.

| # | Maßnahme | Bereich | Schwere/Aufwand | Warum genau hier |
|---|---|---|---|---|
| 1 | **SECRET_KEY Boot-Guard** (Default-Secret in Prod hart ablehnen) | Code | KRITISCH / S | Auth-Bypass, Ein-Validator-Fix, maximale Schaden/Aufwand-Ratio |
| 2 | **Gasdruckfeder-Formel `01_03` korrigieren** (Faktor 2) | Recherche | KRITISCH / M | Physisch gefährliche Fehlauslegung, reproduzierbar falsch |
| 3 | **Sicherheits-/Struktur-Sachfehler Kat. 26–31 korrigieren** (HRU-Tiefe `29_02`+`le=125`, ISO-12402 `29_01`, Karabiner `29_03`, Hydrostatik `31_02`, Kielbolzen `31_08`, Ruder `31_09`, Ballast `31_03`, Trailer-Grenzwerte `30_01`, Ethylenglykol/CO `26_01`) | Recherche | KRITISCH / M | ~22 web-verifizierte Fehler in leib-/strukturkritischen Themen; **0/45 erfüllen Standard** |
| 4 | **Visual-Pipeline (Pipeline B) reparieren + „Erfundene Gewissheit" beheben** (Import-Bug `analyze_image`; Batch zählt nur echte Analysen; kein 50.0; `data_source` durchreichen; `available:false`; flag-statt-mitteln; Logging) | Code | KRITISCH + HOCH-Cluster / M–L | Pipeline B läuft aktuell **nie**; höchste Hebelwirkung; stellt die #1-Nichtverhandelbar-Regel wieder her |
| 5 | **Gefährliche Falschinfo `01_09` (Salzsäure auf Edelstahl) entfernen** | Recherche | HOCH / S | Bauteilversagen 316L; Ein-Zeilen-Fix |
| 6 | **Autorisierung schließen: Subscription-Gating verdrahten + WebSocket-Ownership** | Code | HOCH / M | Bezahlschranke + Cross-Tenant-Leck; beides `user.tier`/Ownership-Ketten |
| 7 | **Compliance-/Norm-Cluster** (Notausstieg 400×520 `01_01`; Companionway-Sill-Tabelle `compliance.py`; ISO 12215 in Spec+`02_04`) | alle 3 | HOCH→MITTEL / S | Ein Normwissens-Fix behebt verzahnte Befunde in Recherche+Code+Spec |
| 8 | **Body-vs-Anhang-Widerspruchs-Sweep über den Korpus** (Anhänge als „documented, unverified" umkennzeichnen) | Recherche | HOCH / L | Wurzel von Muster A+B im Korpus; eigener Durchlauf nötig |
| 9 | **Stiller Wissens-Datenverlust + Duplikate beheben** (Slug-Kollision → 6 Dateien verloren, `loader:1283`; Root-/`research/`-Dubletten; Index-Zählstände 252/31/245) | Recherche+Spec+Code | KRITISCH→MITTEL / S–M | 6 Wissensdateien produktiv unerreichbar, ohne Fehler |
| 10 | **CLAUDE.md um die Plattform-Schicht ergänzen** (Auth+SECRET_KEY-Pflicht, Subscription, i18n, Wissenssystem, Deploy-Verlinkung) | Spec | HOCH / M | Macht die schwersten Code-Themen erst spezifiziert & erzwingbar |

**Reihenfolge-Begründung:** #1–#3 sind die drei bestätigten/belegten KRITISCH-Befunde (Gefahr zuerst, kleinster Aufwand vorn). #4 ist der teuerste, aber mit Abstand hebelstärkste Einzelblock — er repariert das projektweite Muster A und die Kernregel. #5–#7 sind kleine, hochwirksame Sicherheits-/Norm-Fixes. #8–#10 sind die strukturellen Aufräumarbeiten (eigene Aufträge), die die Wurzeln von B/D/F ziehen.

---

## Abdeckung & nächste Schritte

| Teilaudit | Abgedeckt | Offen |
|---|---|---|
| 1 Recherche | **110/252** tiefengeprüft (jede der 31 Kat. abgedeckt: 01/02 + dünne Region 26–31 + Stichprobe 03–25); 252 triagiert; KRITISCH verifiziert | 142 weitere Kat.-03–25-Dokumente (voraussichtlich dasselbe Muster) |
| 2 Code | **8/8 Dimensionen — Audit abgeschlossen** (4 KRITISCH · ~14 HOCH) | — |
| 3 Spezifikation | CLAUDE.md, Spec↔Code, Spec↔Recherche, Bestand, **6/15 Design-Docs** | 9 restliche Design-Docs (Stichprobe genügt) |

**Der Audit ist inhaltlich abgeschlossen und repräsentativ:** Code 8/8, Spec vollständig, Recherche über alle 31 Kategorien mit 110 Tiefenprüfungen. Die drei Muster (Widersprüche in den umfangreichen Kategorien, Dünne+Sachfehler in 26–31, Duplikation) sind belegt und stabil. Verbleibende Arbeit ist keine Erkenntnis-, sondern **Fix-Arbeit**: (1) die 4 KRITISCH-Code-Fixes (SECRET_KEY, Visual-Pipeline, Slug-Kollision, Fake-Confidence); (2) ein **mechanischer Haupttext-vs-Anhang-Diff über alle 252 Recherche-Dokumente** (skaliert besser als weitere Einzel-Audits der 142 Restdokumente, die voraussichtlich kein neues Muster liefern); (3) Neuschreiben der Kategorien 26–31 auf Standard-Tiefe; (4) CLAUDE.md + Design-Docs auf den Ist-Stand heben.

Dieser Durchlauf hat **keinen Code, kein Dokument und keine Recherche-Datei verändert** — die vier Audit-Berichte (`audit_report_recherche.md`, `audit_report_code.md`, `audit_report_spezifikation.md`, `audit_report_GESAMT.md`) sind die einzigen Artefakte.
