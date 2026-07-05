# Audit-Bericht: Recherche-Dokumente (Teilaudit 1)
Datum: 2026-07-05
Maßstab: Fensterdichtungs-Standard (Werftqualität), Goldstandard-Referenz `01_02_fenster_dichtungen.md`
Methode: Ein KI-Auditor pro Dokument, vollständige Lektüre, gegen die aus dem Goldstandard destillierte Rubrik. KRITISCH-Befunde adversariell gegengeprüft.

> **Hinweis zur Auftragslage:** Die im Master-Steuerungsdokument referenzierten Teilaudit-Prompt-Dateien (`audit_01_recherche_dokumente.md`, `audit_02…`, `audit_03…`) **existieren nicht** im Arbeitsstand. Dieser Audit wurde daher aus der Spezifikation des Master-Dokuments selbst durchgeführt (dokumentiert, kein Stopp — gemäß fester Regel).

---

## Zusammenfassung

Der Korpus umfasst **252 nummerierte Recherche-Dokumente** in 31 Kategorien (der Wissens-Index `KNOWLEDGE_INDEX.py` und mehrere Meta-Dokumente sprechen von „249" bzw. „72 Dateien" — die Zahlen sind veraltet). In mehreren Durchläufen (durch ein hartes Session-Token-Limit getrennt) sind inzwischen **110 von 252 Dokumenten vollständig tiefengeprüft** — mit mindestens einer Tiefenprüfung in **jeder der 31 Kategorien**: Dichtungs-Kernkategorien 01 (12) + 02 (8), die gesamte dünne Region 26–31 (45) und eine repräsentative Stichprobe der großen Kategorien 03–25 (45). **Über alle 110 Dokumente erfüllen nur 20 (18 %) den Fensterdichtungs-Standard** („allein lösbar"). Es gibt zwei Fehlerprofile: die umfangreichen Kategorien (01/02 + 03–25, Ø 71–85) sind fachlich substanziell, tragen aber fast durchgängig **interne Widersprüche zwischen Haupttext und Anhängen — beide als „measured"**, im Hardware-Teil bei last-/sicherheitskritischen Werten; die dünnen Kategorien 26–31 (Ø ≈ 35, 0/45) sind schlicht zu dünn und teils sachlich falsch. Der limitierende Faktor ist damit korpusweit **innere Widerspruchsfreiheit**, nicht fehlendes Wissen (Details im Nachtrag).

**Befund für die 20 geprüften Dokumente (die Dichtungs-Kernkategorien — das eigene Heimatterrain des Standards):** Durchschnittsscore **85/100**, **18 von 20** erfüllen den Fensterdichtungs-Standard hinsichtlich *Tiefe und Vollständigkeit*. Trotzdem wurden **28 HOCH/KRITISCH-Befunde** gefunden. Dieser scheinbare Widerspruch ist die zentrale Erkenntnis: **Die Dokumente sind außergewöhnlich umfangreich und vollständig, aber sie widersprechen sich systematisch selbst.** Haupttext (Abschnitte 1–26) und die 30–40 Anhänge (ANHANG A–AM) je Dokument wurden erkennbar in getrennten Erzeugungsläufen geschrieben und liefern für dasselbe Produkt / dieselbe Teilenummer / dasselbe Drehmoment / dieselbe Aushärtezeit **entgegengesetzte Werte — beide mit „Confidence: measured" gekennzeichnet.** Zwei dieser Widersprüche sind sicherheitskritisch (KRITISCH).

**Größtes Muster (bereichsübergreifend):** Interne Widersprüche zwischen Haupttext und Anhang (17 von 28 High-Severity-Befunden). **Zweitgrößtes Muster:** fehlende Navigierbarkeit (Inhaltsverzeichnis deckt Anhänge nicht ab oder fehlt ganz). **Drittes Muster (aus der Triage):** dramatischer Qualitätsabfall in den hohen Kategorien — die Sicherheits-Kategorie 29 ist der dünnste Bereich des gesamten Projekts.

---

## Inventur-Ergebnis (Soll vs. Ist)

| Aspekt | Soll (laut Spec/Index) | Ist (auf der Platte) | Bewertung |
|---|---|---|---|
| Anzahl Recherche-Dateien | „249" (Index) / „72" (Kat. 22-Titel) | **252** nummerierte `.md` | Zähl-Diskrepanz (MITTEL) |
| Kategorien | — | **31** (01–31) | vollständig durchnummeriert, keine Lücken in 01–31 |
| Duplikate | keine | **`24_05_pumpen_sanitaer.md` (3132 Z.) UND `24_05_pumpen_sanitaer_clean.md` (2486 Z.)** — dieselbe Nummer, zwei Dateien | HOCH |
| Nummern-Kollision innerhalb Kategorie | keine | Kat. 24 hat zweimal „05" | HOCH |
| Meta-Dateien | — | `IMPLEMENTATION_SUMMARY.md`, `QUICK_REFERENCE.md`, `README_WEAKPOINTS.md` (nicht Teil des Korpus) | ok |

### Struktur-Triage der 232 nicht tiefengeprüften Dokumente (objektiv, per Zeilenumfang)

Der Goldstandard und die Kategorien 01–25 liegen durchgängig bei **~3.800 Zeilen**. Ab Kategorie 26 bricht der Umfang massiv ein — ein starker Indikator für Unterschreitung des Standards, der in der Tiefenprüfung zu verifizieren ist:

| Kategorie | Thema | Zeilenumfang | Einordnung |
|---|---|---|---|
| 01–25 | Dichtungen, Kleber, Beschichtungen, Composite, Beschläge, Motoren, Elektrik, Sanitär, Gas … | 2.400–5.671 | Standard-Tiefe |
| 26 (Heizung/Klima) | 6 Dateien | 1.745–2.838 | grenzwertig |
| 27 (Persenning) | 6 Dateien | 947–3.134 | uneinheitlich, mehrheitlich dünn |
| 28 (Interieur) | 7 Dateien | 698–1.141 | **dünn** |
| **29 (Sicherheit!)** | 9 Dateien | **307–898** | **dünnster Bereich des ganzen Projekts** |
| 30 (Transport/Logistik) | 3 Dateien | 831–1.405 | dünn |
| 31 (Konstruktion/Design) | 14 Dateien | 749–1.093 | **systematisch dünn** |

Die drei dünnsten Dateien überhaupt sind sicherheitsrelevant: `29_07_mann_ueber_bord.md` (307 Z.), `29_08_lenzpumpen_notausruestung.md` (311 Z.), `29_09_sicherheit_wartung.md` (335 Z.). Für ein System, das laut CLAUDE.md „nie Unsicheres als Fakt" ausgeben und Sicherheit werftgerecht behandeln will, ist die dünnste Abdeckung ausgerechnet bei Rettungsmitteln, Mann-über-Bord und Feuerlöschung ein struktureller Widerspruch zum eigenen Anspruch.

### Eingebetteter Code-Verstoß in dünnen Dokumenten (Grep-verifiziert)

Die dünnen Dokumente der Kategorien 29 und 30 enthalten Python-Codebeispiele, die **`class Config`** verwenden — das exakt von CLAUDE.md und von den Schwesterdokumenten (z.B. `01_05:5`, `07_01:5`) verbotene Pydantic-v1-Muster. Betroffen (Grep): `29_01` (3×), `29_02` (2×), `29_03` (3×), `29_04`, `29_05`, `29_06`, `29_09`, `30_01` (4×), `30_02` (4×). Der **echte Backend-Code enthält keinen einzigen `class Config`** — der Verstoß existiert nur in diesen Recherche-Dokumenten und ist damit ein Selbstwiderspruch der Wissensbasis.

---

## Befunde

### KRITISCH (verifiziert)

- **`01_03_luken_scharnier_dichtungen_und_gasdruckfedern.md` — fehlerhafte Gasdruckfeder-Auslegungsformel (Faktor 2). VERIFIZIERT/CONFIRMED.** Die Primärformel (Z. 345) `F=(m·g·a)/(2·b·n)` enthält einen falschen Faktor 2 (Doppelzählung der `n` Federn); die korrekte Physik (Momentengleichgewicht) ist `F=(m·g·a)/(n·b)`. Der Faktor-2-Fehler ist über **~8 Stellen** propagiert (Formel Z. 345, `model_config` Z. 372, Fallstudie 35.2, ANHANG Q, ANHANG AI, FAQ) und **halbiert systematisch die Auslegungskraft** → Gasfeder zu schwach → Lukendeckel (bis 45 kg) fällt zu → Quetsch-/Sturzgefahr (das Dokument schildert genau diesen Unfall selbst, ANHANG I.2). **Fix-Richtung (wichtig, gegenüber Erstbefund korrigiert):** Nur die Beispieltabelle in Abschnitt 6.2 (Z. 357-364) ist bereits **korrekt** (ohne Faktor 2, deckt sich mit Quick-Reference R.1) — sie darf **nicht** angepasst werden; der Faktor 2 ist aus der Formel und allen Folgestellen zu entfernen. — Aufwand: M
- **`02_08_acrylat_kleber.md` — MMA-Kiel-Verdacht: bei Verifikation WIDERLEGT → herabgestuft auf NIEDRIG.** *(Korrektur des Erstbefunds.)* Die adversarielle Gegenprüfung hat den ursprünglichen KRITISCH-Verdacht entkräftet: „keel-fin bonding" (strukturelle Verklebung der **Composite-Kielflosse** — MA832 fachlich vertretbar, zäh) und „Kiel-Fundament/-Bolzen" (verschraubte **Ballastkiel**-Verbindung — Epoxid, MMA zu weich) sind **zwei verschiedene Verbindungen**; das Dokument löst die Wahl in der FAQ (Z. 1544-1545) explizit auf (Epoxid = Standard, MA832 = Sonderfall Composite/Schlagzähigkeit). Verbleibt ein Formulierungs-Nit (der Begriff „Keel-to-Hull" in Z. 252 ist unpräzise) → NIEDRIG. *(Beleg dafür, dass die Verifikationsstufe einen False-Positive-KRITISCH verhindert.)*

> **Aus der Vervollständigung (Kat. 29+31) hinzugekommen: weitere verifizierte KRITISCH-Befunde — siehe „## Nachtrag" unten.**

### HOCH (Auswahl der gravierendsten von 26; alle mit exakter Belegstelle)

**Sicherheitsrelevante Widersprüche / Falschangaben:**
- **`01_01_luken_dichtungen.md`**: Notausstiegsluke in der Größenspalte mit „400×400 mm min" angegeben, in derselben Zeile aber korrekt „ISO 12216: min 400×520 mm". Wer nur die Größenspalte liest, legt eine normwidrig zu kleine Fluchtluke aus. — S
- **`01_09_kuehlwassersystem_dichtungen.md` — gefährliche Falschinfo**: ANHANG X.1 empfiehlt verdünnte Salzsäure „NUR Edelstahl (NICHT Kupfer!)". Chlorid-haltige Salzsäure verursacht gerade bei Edelstahl (auch 316L) Lochfraß-/Spannungsrisskorrosion; die Formulierung suggeriert Unbedenklichkeit für das am stärksten gefährdete Material (Plattenwärmetauscher 316L). — S
- **`01_07_saildrive_manschetten.md`**: (a) Getriebeöl — Abschnitt 3.8 nennt „API GL-5 75W-90 als gleichwertig", ANHANG AC.1 warnt „AUSSCHLIESSLICH IPS Oil, sonst Garantieverlust/Dichtungsschaden". (b) „NIEMALS Dichtmittel" (Abschn. 3.9/12.4) vs. „Sikaflex 291i auf Flansch" (ANHANG AA.1/AA.2). — S

**Teilenummer-Kollisionen (führen zu Fehlbestellungen):**
- **`01_06_…pss.md`**: Teilenummer `21389074` einmal Volvo SD 130, einmal Volvo 150S zugeordnet; zusätzlich Aquamet-Festigkeitswerte in ANHANG B vs. AI.1 um bis zu 45 % abweichend, beide „measured". — S
- **`01_08_motordichtungen.md`**: ANHANG BB („Aftermarket-Cross-Referenz") widerspricht systematisch dem Hauptkatalog — Mischnummer `128170-01911` für 1GM/2GM/3GM (jeder hat real eigene Nummer), nicht existentes Modell „3JH25", falsche Volvo-Nummern. — M

**Vollständigkeit / fehlende Hersteller:**
- **`01_08` und `01_09` (Motor-/Kühlwasser-Dichtungen)**: decken nur Hilfsdiesel bis ~110 PS ab. Es fehlen **alle** großen Yacht-Antriebsdiesel (Caterpillar, MAN, MTU, Cummins, Scania, John Deere) sowie Volvo D3–D13/Yanmar 6LY/8LV — obwohl CLAUDE.md AYDI ausdrücklich bis „Custom/Superyacht 18m+" definiert. — L

**Technische Widersprüche Haupttext↔Anhang (beide „measured"):**
- **`02_01_pu_dichtstoffe_elastisch.md`**: TDS-Kennwerte (Shore A, Zugfestigkeit, Bruchdehnung) für Simson MSR, Sabatack 750/770, Soudaseal 270HS/240FC weichen zwischen Tabelle 3.1 und Anhang S ab; zusätzlich Markenverwechslung „Bostik ISR 70-03" vs. „Simson ISR 70-03"; Sikaflex 298 einmal nur „Sandwich-Bonding", einmal „Teakdeck-Standard >80 % Marktanteil". — M
- **`02_02_pu_…strukturell.md`**: FAQ 37/40 nennen für 292i/5200 Scherfestigkeiten (12,0/13,8 MPa), die dem Kernvergleich (3,5/1,7 MPa) widersprechen; Kielbolzen-Drehmomente in ANHANG I.2 vs. AO.4 um Faktor 2–3 abweichend ohne Erklärung. — S/M
- **`02_08_acrylat_kleber.md`**: Plexus-MA-Serie — Topfzeiten/Festigkeiten in Abschnitt 2.2 vs. Anhang O nicht nur driftend, sondern in der Reihenfolge umgekehrt; Weld-On 40 „55 MPa" vs. „14–18 MPa". — M
- **`02_04_silikon_dichtstoffe.md` — falsche Normreferenz im ausführbaren Code**: ISO 12217 (Stabilität) wird als Struktur-Begründung für Rumpf-Deck zitiert (korrekt wäre ISO 12215); der Fehler steht auch im AYDI-Compliance-Check-Dict (`iso_reference: "ISO 12217"`, Key `hull_deck_silicone`) und erzeugt damit direkt Nutzer-Befunde. — S

**Norm-/Navigations-/Fülltext-Befunde:**
- **`01_03`**: EN 13906-2 (Zug-Schraubenfedern) fälschlich als Gasdruckfeder-Norm zitiert; „ISO 11901-1" nicht verifizierbar. — S
- **`01_02` (Goldstandard selbst)**: Inhaltsverzeichnis endet bei Punkt 59; 15 weitere Anhänge (P–AD, ~970 Z. = ¼ des Dokuments) sind nicht verzeichnet/verlinkt. Zusätzlich Butyl/PMMA-Crazing-Widerspruch (Abschn. 2.2/4.2 „kein Risiko" vs. ANHANG W.2/X.2 „NIEMALS auf PMMA"). — S/M
- **`01_10_deck_beschlag_abdichtung.md`**: kein Inhaltsverzeichnis bei 3.925 Zeilen / 36 Anhängen. — S
- **`01_11_mast_manschette.md`**: SSI-Größenzuordnung in ANHANG AI unterschreitet die Mindest-Mastumfänge der eigenen Datenblätter (ANHANG R) um bis zu 175 mm → potenziell falsche Manschettengröße bestellt; zusätzlich fehlender ABYC-E-2-/ISO-Bezug bei Galvanik-Thema. — M/S
- **`02_05_polysulfid_dichtstoffe.md` — Fülltext**: ~1.300 von 3.890 Zeilen sind 175 nahezu identische „Praxisbericht"-Anekdoten + 90 FAQ, alle pauschal „Confidence: documented", mit erfundenen Forennamen ohne Quelle — verletzt „Never present uncertain results as facts" im großen Maßstab. — M

### MITTEL
- Zähl-/Bestandsdiskrepanz „249"/„72" vs. real 252 Dateien (in Index & Meta-Docs). — S
- Durchgängiges Muster „Confidence: measured" auf nicht nachprüfbaren Anekdoten-/Forumsdaten (mehrere Dokumente). — M
- Uneinheitliche Anhang-Benennung (A–AM, teils doppelte Buchstaben-Sprünge) erschwert Referenzierung. — S

### NIEDRIG
- Formatierungs-/Terminologie-Drift zwischen Haupttext und Anhängen (Einheitenschreibweise, „mm" vs. „ mm"). — S

---

## Offene Fragen (Produktentscheidungen nötig)

1. **Duplikat `24_05`**: Ist `_clean.md` die kanonische Version (die andere löschen) oder umgekehrt? Der Loader lädt evtl. beide (siehe Code-Bericht). — Produktentscheidung nötig.
2. **Kategorien 26–31**: Sollen die dünnen Dokumente (v.a. Sicherheit 29, Konstruktion 31) auf Standard-Tiefe gebracht werden, oder ist für diese Themen bewusst eine geringere Tiefe akzeptiert? Das berührt den Kern-Qualitätsanspruch.
3. **Scope-Grenze Motoren**: Soll AYDI wirklich Superyacht-Hauptdiesel (CAT/MTU/MAN) abdecken (dann sind 01_08/01_09 unvollständig), oder wird der reale Scope auf Segelyacht-Hilfsdiesel eingegrenzt (dann ist die CLAUDE.md-Scope-Aussage „18m+" zu korrigieren)?
4. **Anhänge als Quelle**: Die Anhänge (P–AM) sind der Hauptquell der Widersprüche und tragen viele „measured"-Behauptungen ohne Quelle. Sind sie kuratiert oder auto-generiert angehängt worden?

---

## Top 10 Prioritätenliste für die Fix-Phase

Sortiert nach Schweregrad × Risiko × Aufwand (S vor L bei gleicher Schwere):

1. **Gasdruckfeder-Formel `01_03` korrigieren** (KRITISCH, M) — Faktor 2 aus Formel + ~8 Folgestellen entfernen, Tabelle 6.2 unangetastet lassen. Physisch gefährlich, verifiziert.
2. **Sicherheits-Norm-Falschangaben Kat. 29 korrigieren** (KRITISCH, S–M) — HRU-Auslösetiefe `29_02` (verhindert gefährliche Fehl-„Kalibrierung" + `le=125`-Codefehler), ISO-12402-Klassen `29_01`, Karabiner-Bruchlast `29_03`, Normzitate `29_04`. Web-verifiziert, mehrere Boote/Menschen betroffen.
3. **Struktur-/Formelfehler Kat. 31 korrigieren** (KRITISCH, M) — Hydrostatik-Formel `31_02`, Ballast-Befestigung `31_03`, Kielbolzen-Drehmoment `31_08`, Ruder-Rechenbeispiele `31_09`.
4. **Salzsäure-auf-Edelstahl-Empfehlung `01_09` entfernen/korrigieren** (HOCH gefährlich, S) — Bauteilversagen 316L.
5. **Notausstiegs-Größe `01_01` (400×400 → 400×520)** + **Falsche Normreferenz `02_04` (ISO 12217 → 12215) inkl. Compliance-Code-Dict** (HOCH, S) — Normkonformität; `02_04` fließt in echte Nutzer-Befunde (berührt Code).
6. **Kat. 29 + 31 komplett auf Standard-Tiefe neu schreiben** (HOCH, L) — 0/23 erfüllen den Standard; dünnster + risikoreichster Bereich; eigener Rechercheauftrag mit Herstellertiefe + Teilenummern + korrekten Normen.
7. **Duplikat `24_05` bereinigen** (HOCH, S) — Ambiguität + Doppelladung im Loader.
8. **Systematische Body-vs-Anhang-Widerspruchsprüfung** (Kat. 01–25) (HOCH, L) — Wurzelmuster; Anhänge als „documented, unverified" statt „measured" kennzeichnen.
9. **Teilenummer-Kollisionen `01_06`/`01_08` u.a.** (HOCH, M) — Fehlbestellungsrisiko.
10. **Fehlende Inhaltsverzeichnisse / Anhang-Verlinkung** `01_02`, `01_10` + `class Config`-Verstöße in Kat. 29/30-Codebeispielen (HOCH→MITTEL, S).

*(Der frühere Top-2-Eintrag „MMA-Kiel `02_08`" wurde bei Verifikation auf NIEDRIG herabgestuft und entfernt.)*

---

## Nachtrag: Tiefenprüfung der Prioritätskategorien 29 (Sicherheit) + 31 (Konstruktion) — 23 Dokumente

Die strukturelle Triage-Hypothese („dünn = unter Standard") wurde für die beiden riskantesten dünnen Kategorien **verifiziert und mit Nachdruck bestätigt**: **0 von 23 Dokumenten erfüllen den Fensterdichtungs-Standard** (Ø-Score **35/100**; Tiefstwert 16). Anders als die Kern-Dichtungsdokumente (Kat. 01/02: umfangreich, aber widersprüchlich) sind diese Dokumente **schlicht zu dünn und teils sachlich falsch** — durchgängig fehlen Hersteller-für-Hersteller-Tiefe, Teilenummern, korrekte Normzitate; mehrfach `class Config`-Verstöße; und — am schwersten — **sicherheits- und strukturkritische Falschangaben**.

### Kategorie 29 — Sicherheit (9 Dokumente, Ø ≈ 28, alle durchgefallen) — ~11 KRITISCH
Scores: 29_01 =33, 29_02 =32, 29_03 =35, 29_04 =27, 29_05 =30, 29_06 =28, 29_07 =24, 29_08 =26, **29_09 =16 (Tiefstwert des gesamten Audits)**.
- **`29_02_rettungsinseln.md` (2× KRITISCH, web-verifiziert):** HRU-Auslösetiefe durchgängig „0,5–2 bar (≈5–20 m)" statt real **1,5–4 m (≈0,15–0,4 bar)** — ANHANG B diagnostiziert dadurch eine **normgerecht auslösende HRU fälschlich als defekt** und „kalibriert" sie auf ~10 m um (real gefährlich). Zusätzlich ISO 9650 (Freizeit, ≤12–16 Pers.) mit SOLAS (≥125 Pers.) vermischt — der falsche Kapazitätsdeckel `le=125` steht **im Pydantic-Modell einprogrammiert**.
- **`29_01_rettungswesten.md` (KRITISCH, web-verifiziert):** ISO-12402-Auftriebsklassen falsch dargestellt (erfundene 130-N-Stufe; höchste/kritischste 275-N-Stufe fehlt komplett) — Fehler zieht sich durch Herstellertabelle, Glossar und Pydantic-Enum.
- **`29_04_signalmittel.md` (2× KRITISCH):** EN 12402-4 (Rettungswesten) für Signalspiegel zitiert; IMO A.810 (EPIRB) für Pyrotechnik; ~⅓ Fülltext-Glossar; „12 Kategorien" versprochen, 6 geliefert.
- **`29_03_sicherheitsleinen.md` (KRITISCH):** Karabiner „min. 15 kN" vs. „Bruch bei 400–500 kg (≈4–5 kN)" im selben Abschnitt — Faktor-3-Widerspruch bei Fallschutz; Fallstudien-Anhang ist reiner Platzhalter.
- **`29_06`, `29_08` (2×), `29_09`:** weitere KRITISCH (falsche Normzuordnungen, fehlende sicherheitsrelevante Fehlerbilder). Durchgängig: keine Teilenummern, keine Confidence-Tags, `class Config`-Verstöße.

### Kategorie 31 — Konstruktion (14 Dokumente, Ø ≈ 40, alle durchgefallen) — ~6 KRITISCH
Scores 28–58 (bester: 31_10 Deck-Layout =58; schlechtester: 31_03 =28).
- **`31_02_hydrostatik.md` (KRITISCH, Formelfehler):** widersprüchliche Formel in Abschnitt 2.1 vs. 2.2.
- **`31_03_strukturberechnung.md` (KRITISCH):** Ballast-Befestigung — Dynamiklast-Auslegung („min. 1,5× statisches Ballast-Gewicht") unzureichend/irreführend für eine sicherheitskritische Verbindung.
- **`31_08_kielkonstruktion.md` (2× KRITISCH):** Kielbolzen-Drehmoment-Berechnung fehlerhaft + falsches Normzitat.
- **`31_09_ruder_design.md` (KRITISCH):** falsche Rechenbeispiele (Struktur/Sicherheit).
- **`31_01_rumpfformen.md` (KRITISCH):** Fließtext widerspricht der Tabelle.
Durchgängig fehlen belastbare Beispielrechnungen, ISO-12215-Scantling-Bezug und konkrete Auslegungsverfahren.

### Kategorien 26 (Heizung/Klima) + 27 (Persenning) + 28 (Interieur) + 30 (Transport) — 22 Dokumente (Ø ≈ 36, alle durchgefallen) — ~5 KRITISCH
Scores: Kat. 26 = 46/44/38/44/47/28, Kat. 27 = 41/33/30/40/27/42, Kat. 28 = 42/28/40/40/30/29/32, Kat. 30 = 30/… . **Neues Sub-Muster: Ganz-Dokument-Duplikation.** Mehrere Dokumente bestehen aus **zwei unabhängig generierten, aneinandergehängten Fassungen** (z.B. `26_03` mit „END OF DOCUMENT (3.847 Zeilen)"-Marker mitten im File) — mit **kollidierenden Fehlerbild-IDs** (`FB-26-XX-NNN` bezeichnet zweimal verschiedene Fehler → zerstört die Diagnose-Zuordnung und die AYDI-API `/heating/fault-images?category=…`), **Platzhalter-Anhängen** („weitere 1.200 Zeilen", „[wird fortgesetzt…]", nach 3 von 8 Fallstudien abgebrochen) und **erfundenen Daten** (Normen EN 14687/EN 12215-7; Hersteller-Herkünfte „Climma Finnland" vs. „Indien").
- **`30_01_bootstrailer.md` (2× KRITISCH):** **gefährlich falsche gesetzliche Grenzwerte** — „TÜV-Pflicht erst ab 3,5 t" (real 750 kg), „bremsenfreie Anhänger bis 1,5 t" (real 750 kg) — beides widerspricht sogar dem **eigenen Glossareintrag** (Z. 684); falsche Normzitate (ISO 1724, ISO 9239, DIN 1055-3); Marktführer AL-KO fehlt; keine Radmuttern-Drehmomente/Kupplungsnorm; 4/6 Pydantic-Modelle mit `class Config`.
- **`26_01_heizung_grundlagen.md` (KRITISCH):** empfiehlt an 3 Stellen giftiges **Ethylenglykol** zum Befüllen (warnt an 1 Stelle korrekt davor); **keine Gas-/CO-Dimension** (ISO 10239, CO-Melder, Lüftungsquerschnitte) trotz CO als Kernrisiko; Truma fehlt; fabrizierte Normen.
- **`26_02_diesel_heizung.md` (KRITISCH):** Fehlercode-Kollision → Fehldiagnose; einzige Lüftungsangabe „10 cm²" undifferenziert für 2–8 kW (CO-relevant zu klein); Ionisationsstrom widersprüchlich (Faktor 1000); keine Teilenummer im ganzen Dokument.
- **`28_02_polstermaterialien.md` (KRITISCH):** materialbezogener Sicherheitsfehler; durchgängig keine Teilenummern.
- Kat. 27/28 sonst ohne KRITISCH, aber durchgängig zu dünn, ohne Herstellertiefe/Teilenummern.

**Konsequenz:** Muster C (Sicherheit ist die schwächste Naht) ist über **alle vier dünnen Kategorien-Cluster** bestätigt: **0 von 45 tiefengeprüften dünnen Dokumenten (Kat. 26–31) erfüllen den Standard**, mit ~22 KRITISCH-Befunden gehäuft in Sicherheits-, Struktur-, CO/Heizungs- und Traglast-Themen. Neben dem Neuschreiben gehört die **Duplikat-/Platzhalter-Bereinigung** (kollidierende Fehlercodes, Stub-Anhänge) an die Spitze.

### Stichprobe der großen Kategorien 03–25 — 45 Dokumente (Ø 71, nur 2 erfüllen den Standard)
Um zu prüfen, ob das Kat.-01/02-Widerspruchsmuster für den gesamten umfangreichen Korpusteil gilt, wurden 2 Dokumente je Kategorie 03–25 tiefengeprüft (1 durch StructuredOutput-Abbruch verloren → 45 geprüft). **Ergebnis: bestätigt, korpusweit.** Diese Dokumente haben Goldstandard-**Tiefe** (Ø 71 vs. 35 bei den dünnen Kategorien), tragen aber fast durchgängig denselben Defekt: **Haupttext und Anhänge widersprechen sich bei denselben Werten, beide als „Confidence: measured"** — und im umfangreichen Hardware-Teil betrifft das **last-/sicherheitskritische Zahlen**. Nur **2 von 45** erfüllen den Standard („allein lösbar"); besonders schwach trotz voller Länge: **Kat. 25 (Gas, Ø 35)** und **Kat. 09 (Winschen, Ø 49)**.

Adversariell **verifizierte** KRITISCH-Widersprüche bei Sicherheits-/Lastwerten (Auswahl):
- **`08_01_decksluken.md`**: Prüfdruck der Luke 6,0 kPa (Z. 73/183) vs. 12–18 kPa (Z. 2473) vs. 49–74 kPa (Z. 2498) — Faktor >10.
- **`10_01_bloecke_grundlagen.md` (2×)**: WLL/Bruchlast der Blöcke Haupttext vs. Anhang widersprüchlich.
- **`12_01_schaekel_grundlagen.md` (2×)**: Schäkel-Festigkeit/Dimensionierung Haupttext vs. ANHANG U.
- **`11_01_klampen_grundlagen.md`**: Klampen-Last Haupttext vs. Anhang.
- **`06_06_gasschlaeuche.md`**: sicherheitsrelevanter Gasschlauch-Wert widersprüchlich.
- **`14_05_autopilot_systeme.md`**: Rudermoment-Dimensionierungsformel (Beispiel) vs. Anhang-Schnellformel.
- **`05_01_edelstahl_schrauben.md`**: Drehmoment-Korrekturfaktoren kehren die Reibungslogik um (trocken < geschmiert).
- Nicht bestätigt/herabgestuft: `05_03`, `09_01`-Formel, ein `12_01`-Sicherheitsfaktor — die Verifikation filtert auch hier Fehlbefunde heraus.

Dazu durchgängig: fehlende/uneinheitliche Inhaltsverzeichnisse, Preis-/TDS-Divergenzen (`03_01`, `03_08`, `04_07`), vereinzelt falsche Normnummern (ISO 7822 als Biegenorm; ISO-12215-5-Designwerte 3× abweichend in `04_07`), sicherheitsrelevante Materialgrenzwerte widersprüchlich (`04_01` Laminat-Schichtdicke 5–8 mm vs. 3 mm, Exothermie/Brandgefahr).

### Gesamtbild Recherche (110 tiefengeprüfte Dokumente über alle 31 Kategorien)
| Cluster | Dok. | Ø-Score | erfüllen Standard | Hauptdefekt |
|---|---|---|---|---|
| Kat. 01/02 (Dichtungen, ~3.800 Z.) | 20 | 85 | 18 | interne Widersprüche (trotz Tiefe) |
| Kat. 03–25 Stichprobe (~3.800 Z.) | 45 | 71 | 2 | **Body-vs-Anhang-Widersprüche, oft last-/sicherheitskritisch** |
| Kat. 26–31 (dünn) | 45 | 35 | 0 | zu dünn + Sachfehler + Duplikation |
| **Gesamt** | **110** | **~64** | **20 (18 %)** | **Body-vs-Anhang-Widerspruch ist der korpusweit dominante Defekt** |

Kernaussage: Der Korpus ist **umfangreich und fachlich substanziell**, aber nur ~18 % der Dokumente sind im Sinne des Fensterdichtungs-Standards „allein lösbar". Der limitierende Faktor ist nicht fehlendes Wissen, sondern **innere Widerspruchsfreiheit** — Haupttext und Anhänge tragen gegensätzliche Werte, systematisch beide als „measured".

---

## Abdeckung & Fortsetzung

**Geprüfter Umfang: 110 von 252 Dokumenten tiefengeprüft (44 %), alle 252 strukturell triagiert.** Geprüft: Dichtungs-Kernkategorien 01 (12) + 02 (8); **die gesamte dünne Region 26–31 (45)**; **repräsentative Stichprobe der großen Kategorien 03–25 (45, 2 je Kategorie)**. Damit liegt für **jede der 31 Kategorien** mindestens eine belastbare Tiefenprüfung vor. Die verbleibenden **142 Dokumente** (weitere Exemplare der Kat. 03–25) sind triagiert; die Stichprobe zeigt mit hoher Sicherheit, dass sie dasselbe Body-vs-Anhang-Widerspruchsmuster tragen.

Die Tiefenprüfung der restlichen 142 ist per Workflow fortsetzbar, liefert aber voraussichtlich **keine neuen Muster**, sondern weitere Instanzen des bereits belegten. Sinnvoller als eine Vollprüfung ist ein **gezielter Body-vs-Anhang-Diff-Durchlauf** (siehe Top 10 #8), der pro Dokument Haupttext- gegen Anhang-Werte automatisiert vergleicht und die Anhänge als „documented, unverified" umkennzeichnet.
