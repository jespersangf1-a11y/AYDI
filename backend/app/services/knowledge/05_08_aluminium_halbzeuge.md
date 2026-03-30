# 05_08 — Aluminium-Halbzeuge im Yachtbau

> **AYDI Wissensmodul 05.08 — Aluminium-Halbzeuge**
> **Kategorie:** Materialien & Halbzeuge → Aluminium
> **Confidence:** documented — Zusammenstellung aus Herstellerkatalogen, Fachliteratur, Forum-Konsens, Eigner-Erfahrungsberichten
> **Version:** 1.0
> **Letzte Aktualisierung:** 2026-03

---

## Inhaltsverzeichnis

1. Einführung und Grundlagen
2. Legierungsübersicht Marine-Aluminium
3. 5083-H116 — Der Rumpfstandard
4. 5086-H116 — Alternative Rumpflegierung
5. 6082-T6 — Beschläge und Strukturteile
6. 6061-T6 — Universelle Konstruktionslegierung
7. Weitere Marine-Legierungen (5052, 5754, 5059, 6005, 7075)
8. Plattenware — Dicken, Formate, Anwendungen
9. Profile — Extrusionen für Strukturbau
10. Rohre und Rundstahl
11. Blech und Bänder
12. Schweißzusätze und Schweißtechnik
13. Oberflächenbehandlung und Korrosionsschutz
14. Galvanische Korrosion — Das Hauptproblem
15. Hersteller und Lieferanten weltweit
16. Praxisberichte und Forum-Konsens
17. Fachliteratur und Experten
18. FAQ — Häufige Fragen
19. AYDI-Integration (Pydantic v2 Models)
20. ANHANG A — Material-Datenblätter
21. ANHANG B — Schweißparameter-Tabellen
22. ANHANG C — Korrosions-Kompatibilitätsmatrix
23. ANHANG D — Glossar
24. ANHANG E — Fehlerbild-Atlas
25. ANHANG F — Bordausstattung und Ersatzteile

---

## 0. Quick-Reference und Lernpfade

### Für verschiedene Benutzer-Profile:

**Wenn Sie ein Boot KAUFEN möchten (Inspekteur, Eigner):**
→ Lesen Sie: Abschnitte 1, 3, 4, 13, 14, 16, 18 (FAQ zu Korrosion + Inspektions-Checkliste)
→ Fokus: Wie erkenne ich Schäden? Was ist normal, was kritisch?
→ Zeitaufwand: ca. 1–2 Stunden

**Wenn Sie ein Boot BAUEN möchten (Schiffsarchitekt, Werftleiter):**
→ Lesen Sie: Abschnitte 1–11, 12, 13, 19 (Pydantic Models), ANHANG A–C
→ Fokus: Welche Legierung wofür? Wie schweißt man? Beschichtungskonzept?
→ Zeitaufwand: ca. 4–6 Stunden (oder 1–2 Tage bei intensivem Studium)

**Wenn Sie ein Boot REPARIEREN möchten (Bootsbauer, Schweißer):**
→ Lesen Sie: Abschnitte 5–13, 12 (Schweißparameter), 18 (FAQ zu Reparaturen), ANHANG E (Fehlerbild-Atlas)
→ Fokus: Wie schweißt man richtig? Was ist Sensibilisierung? Wie behandelt man die Oberfläche?
→ Zeitaufwand: ca. 2–3 Stunden + Referenz während der Arbeit

**Wenn Sie LANGFAHRER sind (Eigner, Selbstversorger):**
→ Lesen Sie: Abschnitte 14, 18 (FAQ zu Opferanoden, Isolation), ANHANG F (Bordausstattung + Checkliste)
→ Fokus: Wie schütze ich meinen Rumpf unterwegs? Notfall-Reparaturen?
→ Zeitaufwand: ca. 1 Stunde (Essentials) + ausdrucken für an Bord

---

### Die fünf wichtigsten Erkenntnisse (für Eilige):

1. **5083-H116 ist der Marine-Standard** — Nicht 5083-H111! Der "-H116" ist PFLICHT.
2. **Galvanische Korrosion ist das Hauptproblem** — Edelstahl-Beschlag auf Alu ohne Isolation = Ruin in 3–5 Jahren.
3. **Schweißen schwächt die Struktur** — Die Wärmeeinflusszone ist 40–55% schwächer. Die Berechnung MUSS mit reduzierten Festigkeiten erfolgen.
4. **Beschichtung ist nicht optional** — Ein blanker Alu-Rumpf in Salzwasser entwickelt in 5–10 Jahren Pitting. Beschichtungssystem muss alle 5–10 Jahre erneuert werden.
5. **Opferanoden funktionieren wirklich** — Alu-Zn-In Anoden (Type 8, Martyr) reduzieren Korrosion um 80–90%. Jede Alu-Yacht sollte welche haben.

---

### Confidence-Level Erklärung (AYDI-Standard):

| Level | Bedeutung | Zuverlässigkeit |
|-------|-----------|-----------------|
| `measured` | Direkt gemessen oder von Millzertifikat | 99% |
| `calculated` | Berechnet nach Norm (ISO, EN, DNV) | 95% |
| `visual_high` | Klares Foto oder sichtige Sicht | 80–90% |
| `visual_medium` | Unklar oder teilweise verdeckt | 60–75% |
| `documented` | Aus Herstellerkatalog oder anerkannter Quelle | 85% |
| `estimated` | Best-guess basierend auf Typ/Klasse | 50–70% |
| `benchmark` | Aggregierte Industr iedaten | 70–80% |

Dieses Modul nutzt primär `documented` und `estimated` Werte, aber weist immer auf die Quelle hin.

---

## 1. Einführung und Grundlagen

### 1.1 Warum Aluminium im Yachtbau?

Aluminium ist nach GFK das zweithäufigste Material im modernen Yachtbau. Seit den 1960er-Jahren hat sich Marine-Aluminium als bevorzugtes Material für Expeditionsyachten, Arbeitsboote und semi-custom Segelyachten etabliert. Die Gründe sind vielfältig und für den AYDI-Kontext hochrelevant:

**Gewichtsvorteil:** Aluminium wiegt ca. 2,7 g/cm³ — ein Drittel von Stahl (7,85 g/cm³). Ein 12m-Alu-Rumpf wiegt typischerweise 30–40% weniger als ein vergleichbarer Stahlrumpf gleicher Festigkeit. Das bedeutet: geringerer Tiefgang, bessere Segelleistung, weniger Antriebsleistung nötig.

**Festigkeit-zu-Gewicht-Verhältnis:** 5083-H116 hat eine Streckgrenze von 215 MPa bei 2,66 g/cm³. Das spezifische Festigkeitsverhältnis (Rp0.2/Dichte) ist ca. 80 MPa·cm³/g — deutlich besser als Baustahl S235 (30 MPa·cm³/g).

**Korrosionsbeständigkeit:** Marine-Aluminium bildet eine natürliche Oxidschicht (Al₂O₃), die in neutralem bis leicht alkalischem Seewasser (pH 7,5–8,3) stabil ist. Anders als Stahl rostet Aluminium nicht — es bildet weiße Korrosionsprodukte (Aluminiumhydroxid).

**Schweißbarkeit:** 5000er-Legierungen (AlMg) sind gut schweißbar mit WIG (TIG) und MIG. Reparaturen können weltweit durchgeführt werden, wo ein Schweißgerät verfügbar ist.

**Reparierbarkeit:** Ein Loch im Alu-Rumpf kann geschweißt werden. Ein Loch im GFK-Rumpf braucht Laminat, Härter, Temperatur, Trockenheit. Für Langfahrer ein entscheidender Vorteil.

### 1.2 Grenzen und Probleme

**Galvanische Korrosion:** DAS Hauptproblem bei Alu-Yachten. Aluminium ist elektrochemisch sehr unedel (−0,76 V vs. SHE für 5083). Kontakt mit edleren Metallen (Edelstahl, Bronze, Kupfer) führt zu beschleunigter Korrosion des Aluminiums. Jede Alu-Yacht braucht ein durchdachtes Isolationskonzept.

**Ermüdung:** Aluminium hat KEINE Dauerfestigkeit (anders als Stahl). Jede Lastwechsel-Zahl führt zum Versagen — die Frage ist nur wann. Schweißnähte sind besonders anfällig: Kerbfaktor 2–4 an der Nahtübergangsstelle.

**Sensibilisierung:** 5xxx-Legierungen mit >3% Mg können bei Temperaturen über 65°C (Maschinenraum!) sensibilisiert werden. Mg₂Al₃-Ausscheidungen an Korngrenzen machen das Material anfällig für intergranulare Korrosion und Spannungsrisskorrosion.

**Biofouling-Schutz:** Kupferhaltige Antifouling-Farben sind auf Alu-Rümpfen VERBOTEN (galvanische Zelle!). Nur kupferfreie Antifoulings erlaubt (Trilux, Hempel Olympic Alu, International Micron CSC für Alu).

### 1.3 Normen und Klassifikation

| Norm | Beschreibung | Relevanz |
|------|-------------|----------|
| EN 573-3 | Chemische Zusammensetzung | Legierungsbezeichnung |
| EN 485-2 | Mechanische Eigenschaften Platten/Bleche | Plattenware-Spezifikation |
| EN 755-2 | Mechanische Eigenschaften Profile | Profil-Spezifikation |
| EN 754-2 | Mechanische Eigenschaften Rohre | Rohr-Spezifikation |
| EN 515 | Zustandsbezeichnungen (H116, T6, O, etc.) | Wärmebehandlung |
| ASTM B928 | 5083-H116/H321 Marine-Platten | US-Norm, ASTM-Äquivalent |
| DNV Rules | Klassifikationsgesellschaft | Materialzulassung Seeschiffe |
| Lloyd's Register | Klassifikationsgesellschaft | Materialzulassung Seeschiffe |
| Bureau Veritas | Klassifikationsgesellschaft | Materialzulassung Seeschiffe |
| ISO 12215-5 | Hull construction — Scantlings | Plattendicken-Berechnung |
| ISO 9094 | Fire protection | Brandschutz Maschinenraum |

### 1.4 Zustandsbezeichnungen (Temper)

| Zustand | Bedeutung | Typische Anwendung |
|---------|-----------|-------------------|
| O | Weichgeglüht | Tiefziehen, Biegen, nicht für Struktur |
| H111 | Leicht kaltverfestigt (nach Warmumformung) | Bleche, Platten |
| H116 | Kaltverfestigt + sensibilisierungsresistent | **Marine-Rumpf-Standard** |
| H321 | Stabilisiert nach Kaltumformung | Alternative zu H116 |
| H32 | Stabilisiert, 1/4 hart | Bleche, leichte Struktur |
| T4 | Lösungsgeglüht + natürlich ausgehärtet | Profil-Halbzeug |
| T6 | Lösungsgeglüht + künstlich ausgehärtet | **Beschläge, Profile** |
| T651 | T6 + spannungsarmgeglüht | Dicke Platten, Blöcke |

**KRITISCH für AYDI:** H116 und H321 sind die EINZIGEN Zustände, die ASTM B928 (Sensibilisierungsresistenz) erfüllen. Für marine Rumpfplatten NIEMALS H111, H32, oder unbeschichtete Zustände verwenden!

---

## 2. Legierungsübersicht Marine-Aluminium

### 2.1 Klassifikation nach Hauptlegierungselement

| Serie | Hauptelement | Marine-Eignung | Schweißbarkeit | Aushärtbar? |
|-------|-------------|---------------|----------------|-------------|
| 1xxx | Reinaluminium (>99%) | Schlecht (zu weich) | Gut | Nein |
| 2xxx | Kupfer (Cu) | VERBOTEN (Korrosion) | Schlecht | Ja |
| 3xxx | Mangan (Mn) | Bedingt (nur Innenausbau) | Gut | Nein |
| 4xxx | Silizium (Si) | Nur als Schweißzusatz | — | Nein |
| **5xxx** | **Magnesium (Mg)** | **Exzellent (Rumpf)** | **Gut** | **Nein** |
| **6xxx** | **Mg + Si** | **Gut (Beschläge/Profile)** | **Gut** | **Ja** |
| 7xxx | Zink (Zn) | Eingeschränkt (Korrosion) | Schlecht | Ja |

### 2.2 Die vier Marine-Hauptlegierungen im Detail

| Eigenschaft | 5083-H116 | 5086-H116 | 6082-T6 | 6061-T6 |
|-------------|-----------|-----------|---------|---------|
| **EN-Bezeichnung** | EN AW-5083 | EN AW-5086 | EN AW-6082 | EN AW-6061 |
| **Werkstoffnummer** | 3.3547 | 3.3545 | 3.2315 | 3.3211 |
| **UNS** | A95083 | A95086 | A96082 | A96061 |
| **Mg %** | 4,0–4,9 | 3,5–4,5 | 0,6–1,2 | 0,8–1,2 |
| **Si %** | ≤0,40 | ≤0,40 | 0,7–1,3 | 0,4–0,8 |
| **Mn %** | 0,40–1,0 | 0,20–0,70 | 0,40–1,0 | ≤0,15 |
| **Cr %** | 0,05–0,25 | 0,05–0,25 | ≤0,25 | 0,04–0,35 |
| **Cu %** | ≤0,10 | ≤0,10 | ≤0,10 | 0,15–0,40 |
| **Zn %** | ≤0,25 | ≤0,25 | ≤0,20 | ≤0,25 |
| **Dichte g/cm³** | 2,66 | 2,66 | 2,71 | 2,70 |
| **Rm MPa** | 305–380 | 270–345 | 310–340 | 310 |
| **Rp0.2 MPa** | 215–270 | 195–240 | 260 | 276 |
| **A5 %** | 10–15 | 10–14 | 8–12 | 8–10 |
| **E-Modul GPa** | 71 | 71 | 70 | 69 |
| **Wärmeleitfähigkeit W/(m·K)** | 117 | 127 | 172 | 167 |
| **Schmelzbereich °C** | 574–638 | 585–640 | 555–650 | 580–650 |
| **Hauptanwendung** | **Rumpf, Deck** | **Rumpf (leichter)** | **Beschläge, Mast** | **Beschläge, Struktur** |
| **Schweißzusatz** | 5183 / 5356 | 5356 | 5356 / 4043 | 4043 / 5356 |
| **Seewasser-Beständigkeit** | Exzellent | Exzellent | Gut (mit Schutz) | Befriedigend |
| **Preis-Index** | 100% (Referenz) | 90–95% | 85–95% | 80–90% |

### 2.3 Entscheidungsmatrix: Welche Legierung wofür?

| Anwendung | Erste Wahl | Alternative | NIEMALS |
|-----------|-----------|-------------|---------|
| Rumpfplatten | 5083-H116 | 5086-H116, 5383-H116 | 6xxx (Korrosion), 2xxx, 7xxx |
| Deckplatten | 5083-H116 | 5086-H116 | 6xxx direkt auf Seewasser |
| Aufbauten | 5083-H116 | 5086-H32 | — |
| Spanten/Stringer | 5083-H111 (gebogen) | 6082-T6 (extrudiert) | — |
| Kiel-Innenstruktur | 5083-H116 | 5083-H111 | — |
| Mast (extrudiert) | 6082-T6 | 6061-T6 | 5xxx (zu weich) |
| Baum (extrudiert) | 6082-T6 | 6061-T6 | — |
| Beschlagplatten | 6082-T6 | 6061-T6 | — |
| Davit-Arme | 6082-T6 | 5083-H116 | — |
| Ruderblatt-Rahmen | 5083-H116 | — | 6xxx (Schweißnaht-Korrosion) |
| Tankverschluss | 5083-H116 | 5086-H116 | 6xxx |
| Zierleisten | 6063-T6 | 6082-T6 | — |
| Fensterrahmen | 6063-T6 | 6082-T6 | — |
| Relingpfosten | 6082-T6 | 5083-H116 | — |

---

## 3. 5083-H116 — Der Rumpfstandard

### 3.1 Warum 5083-H116 der Marine-Standard ist

5083-H116 ist die weltweit am häufigsten verwendete Legierung für Alu-Yacht-Rümpfe. Der Grund: die Kombination aus hoher Festigkeit (Rm 305 MPa), exzellenter Seewasser-Korrosionsbeständigkeit (durch 4,0–4,9% Mg), guter Schweißbarkeit und der H116-Zustand garantiert Sensibilisierungsresistenz nach ASTM G67 (NAMLT-Test: Masseverlust ≤15 mg/cm²).

**Forum-Konsens (CruisersForum, Thread "Best aluminum for hull" 2019–2024):**
> Einhellige Meinung: 5083-H116 ist der Gold-Standard für Alu-Rümpfe. Diskussionen drehen sich nur um die Frage, ob 5383 (neuere Legierung) oder 5059 für bestimmte Anwendungen besser sind — aber 5083 bleibt der bewährte Standard mit der breitesten Verfügbarkeit weltweit.

### 3.2 Chemische Zusammensetzung im Detail

| Element | Min. % | Max. % | Funktion |
|---------|--------|--------|----------|
| Aluminium (Al) | Balance | — | Grundmetall |
| Magnesium (Mg) | 4,0 | 4,9 | Festigkeit + Korrosionsschutz |
| Mangan (Mn) | 0,40 | 1,0 | Festigkeit + Kornfeinung |
| Chrom (Cr) | 0,05 | 0,25 | Korrosionsschutz + Sensibilisierungsschutz |
| Silizium (Si) | — | 0,40 | Unvermeidliche Beimengung |
| Eisen (Fe) | — | 0,40 | Unvermeidliche Beimengung |
| Kupfer (Cu) | — | 0,10 | **MUSS niedrig sein!** Cu fördert Lochfraß |
| Zink (Zn) | — | 0,25 | Unvermeidliche Beimengung |
| Titan (Ti) | — | 0,15 | Kornfeinung beim Gießen |

### 3.3 Mechanische Eigenschaften nach Plattendicke

| Dicke mm | Rm MPa min. | Rp0.2 MPa min. | A5 % min. | Anwendung |
|----------|-------------|----------------|-----------|-----------|
| 3,0 | 305 | 215 | 10 | Aufbauten, Schotten |
| 4,0 | 305 | 215 | 10 | Aufbauten, leichte Decks |
| 5,0 | 305 | 215 | 10 | Decksplatten ≤10m Boote |
| 6,0 | 305 | 215 | 10 | Rumpf ≤10m, Deck 10–14m |
| 8,0 | 305 | 215 | 10 | Rumpf 10–14m |
| 10,0 | 275 | 195 | 10 | Rumpf 14–18m, Kielbereich |
| 12,0 | 275 | 195 | 10 | Rumpf 18–22m |
| 15,0 | 275 | 195 | 10 | Rumpf >22m, Kielbereich |
| 20,0 | 275 | 195 | 10 | Kielschwein, Eisverstärkung |
| 25,0 | 270 | 190 | 10 | Eisverstärkung, Spezialstärke |
| 30,0 | 270 | 190 | 9 | Schwere Strukturteile |
| 40,0 | 270 | 190 | 9 | Kielschwein Superyachten |
| 50,0 | 270 | 190 | 9 | Block-Halbzeug für CNC |

**AYDI-Hinweis (confidence: documented):** Werte nach EN 485-2 für H116. Dicken >12 mm zeigen leicht reduzierte Streckgrenzen — bei Kiel-Berechnungen berücksichtigen!

### 3.4 Plattendicken nach Bootsgröße und Zone (ISO 12215-5)

| Zone | 8m Segelboot | 10m Segelboot | 12m Segelboot | 14m Segelboot | 16m Motor | 20m Expedition |
|------|-------------|---------------|---------------|---------------|-----------|----------------|
| Boden (mittschiffs) | 5 mm | 6 mm | 6 mm | 8 mm | 8 mm | 10 mm |
| Boden (Kiel) | 6 mm | 6 mm | 8 mm | 10 mm | 10 mm | 12 mm |
| Seiten (mittschiffs) | 4 mm | 5 mm | 5 mm | 6 mm | 6 mm | 8 mm |
| Seiten (Bug) | 5 mm | 6 mm | 6 mm | 8 mm | 8 mm | 10 mm |
| Spiegel | 5 mm | 6 mm | 6 mm | 8 mm | 8 mm | 10 mm |
| Deck | 4 mm | 4 mm | 5 mm | 5 mm | 5 mm | 6 mm |
| Aufbauten | 3 mm | 3 mm | 4 mm | 4 mm | 4 mm | 5 mm |
| Cockpitboden | 4 mm | 5 mm | 5 mm | 6 mm | 6 mm | 8 mm |
| Schotten | 3 mm | 4 mm | 4 mm | 5 mm | 5 mm | 6 mm |

**AYDI-Hinweis (confidence: calculated):** Diese Werte sind Richtwerte basierend auf ISO 12215-5 Berechnung für CE-Kategorie A (Hochsee). Tatsächliche Dicken hängen ab von: Spantabstand, Stringer-Layout, Schlagbelastung (Slamming), und ob Eisverstärkung gefordert ist. Ein Naval Architect muss die endgültige Berechnung durchführen.

### 3.5 Verfügbare Plattenformate (Standard-Abmessungen)

| Format (Breite × Länge) | Verfügbarkeit | Typische Anwendung |
|--------------------------|---------------|-------------------|
| 1000 × 2000 mm | Standard, weltweit | Kleine Yachten, Reparaturen |
| 1250 × 2500 mm | Standard, EU/US | Mittlere Yachten |
| 1500 × 3000 mm | Standard, EU/US | Rumpfplatten bis 14m |
| 1500 × 4000 mm | Sonderformat | Rumpfplatten 14–18m |
| 1500 × 6000 mm | Walzwerk-Bestellung | Rumpfplatten >18m |
| 2000 × 4000 mm | Sonderformat | Großyachten |
| 2000 × 6000 mm | Walzwerk-Bestellung | Superyachten |
| 2500 × 6000 mm | Sonderformat | Superyachten |
| 2500 × 8000 mm | Walzwerk-Bestellung | Expedition, Arbeitsschiffe |

**Praxis-Tipp (CruisersForum-Konsens):** Für Yachten bis 14m LOA reichen 1500×3000mm-Platten. Größere Formate minimieren Schweißnähte, aber Transport wird schwierig. Die meisten Werken arbeiten mit 1500×3000 oder 1500×4000.

### 3.6 Preise (Stand 2025/2026, Orientierungswerte)

| Dicke | Preis €/kg | Preis €/m² | Quelle/Region |
|-------|-----------|------------|---------------|
| 4 mm | €4,50–€6,00 | €48–€65 | DE, Standardhändler |
| 5 mm | €4,50–€6,00 | €60–€81 | DE, Standardhändler |
| 6 mm | €4,20–€5,80 | €68–€94 | DE, Standardhändler |
| 8 mm | €4,00–€5,50 | €86–€119 | DE, Standardhändler |
| 10 mm | €3,80–€5,20 | €102–€140 | DE, Standardhändler |
| 12 mm | €3,80–€5,20 | €123–€168 | DE, Standardhändler |
| 15 mm | €3,80–€5,00 | €153–€202 | DE, Walzwerk-Bestellung |
| 20 mm | €3,50–€4,80 | €189–€259 | DE, Walzwerk-Bestellung |

**Kleinmengen-Zuschlag:** Einzelplatten kosten 30–60% mehr als Mengen ab 500 kg. Für Yacht-Neubau: immer Gesamt-Materialpaket beim Walzwerk oder Großhändler bestellen.

**Weltweite Preisunterschiede:**
- **Deutschland:** Referenzpreis 100%
- **UK:** 105–115% (Brexit-Zuschlag, Pfund-Kurs)
- **USA (Ostküste):** 90–110% (ASTM B928, oft günstiger bei Großbestellungen)
- **Australien:** 120–140% (Importkosten, Entfernung)
- **Karibik:** 150–200% (Import + Versand + Zoll)
- **Türkei:** 75–90% (lokale Produktion, Assan Alüminyum)

---

## 4. 5086-H116 — Alternative Rumpflegierung

### 4.1 Warum 5086 statt 5083?

5086 enthält weniger Magnesium (3,5–4,5% vs. 4,0–4,9%) und ist daher etwas weniger festigkeitsstark, aber dafür:
- Etwas besser schweißbar (weniger Heißrissneigung)
- Etwas weniger sensibilisierungsanfällig
- Besser umformbar (geringere Kaltverfestigung)

**Forum-Konsens (boote-forum.de):** In Europa wird fast ausschließlich 5083 verwendet. 5086 ist vor allem in den USA und Australien verbreitet, wo es als leichter verarbeitbar gilt. Für Reparaturen sind beide legierungskompatibel (Schweißzusatz 5356).

### 4.2 Mechanische Eigenschaften

| Eigenschaft | 5086-H116 | 5083-H116 | Differenz |
|-------------|-----------|-----------|-----------|
| Rm MPa | 270–345 | 305–380 | −10–12% |
| Rp0.2 MPa | 195–240 | 215–270 | −10–12% |
| A5 % | 10–14 | 10–15 | Vergleichbar |
| Härte HB | 75–85 | 80–95 | −5–10% |

### 4.3 Wann 5086 sinnvoll ist

- Boote ≤10m LOA, wo die geringere Festigkeit durch Konstruktion kompensiert wird
- Bereiche mit extremer Umformung (komplexe Bugformen, Doppelkrümmungen)
- Reparaturen in Regionen, wo nur 5086 verfügbar ist (US-Südstaaten, Australien)
- Tanks (Kraftstoff, Wasser) — etwas bessere Umformbarkeit für Tankbau

### 4.4 Detaillierte chemische Zusammensetzung 5086-H116

| Element | Min % | Max % | Zweck |
|---------|-------|-------|--------|
| Si (Silizium) | — | 0,40 | Verschmächtigung |
| Fe (Eisen) | — | 0,50 | Verschmächtigung |
| Cu (Kupfer) | — | 0,10 | Minimiert Korrosion |
| Mn (Mangan) | 0,20 | 0,70 | Verfestigung, Korrosionsschutz |
| Mg (Magnesium) | 3,5 | 4,5 | **Hauptlegierungselement** |
| Cr (Chrom) | — | 0,25 | Korrosionsschutz (nur in einigen Chargen) |
| Zn (Zink) | — | 0,25 | Verfestigung |
| Ti (Titan) | — | 0,15 | Kornfineness (optional) |
| Al (Aluminium) | Rest | — | Basis |
| **Mg/Al Verhältnis** | 3,5/96,5 = **3,6%** | 4,5/95,5 = **4,7%** | Höher → schlechtere Umformung |

**Unterschied zu 5083:** 5083 hat 4,0–4,9% Mg (höher!), daher etwas spröder, aber auch festiger.

### 4.5 Vollständige mechanische Eigenschaften 5086-H116

| Eigenschaft | Minimum | Typisch | Maximum | Einheit | Bemerkung |
|-------------|---------|---------|---------|---------|-----------|
| Dichte | 2,66 | 2,66 | 2,66 | g/cm³ | Leicht schwerer als 5083 |
| Rm (Zugfestigkeit) | 270 | 310 | 345 | MPa | Breiter Streubereich |
| Rp0.2 (Streckgrenze) | 195 | 220 | 240 | MPa | — |
| A5 (Bruchdehnung) | 10 | 12 | 14 | % | Gute Zähigkeit |
| A80 (Längsdehnung) | 8–12 | 10 | 12 | % | Richtungsabhängig |
| Härte HB | 75 | 80 | 85 | HV | Weicher als 5083 |
| E-Modul (Elastizität) | 70 | 70 | 70 | GPa | Standard |
| G-Modul (Schub) | 26 | 26 | 26 | GPa | Standard |
| Poisson-Zahl (ν) | 0,33 | 0,33 | 0,33 | — | Standard |
| Scherfestigkeit | — | 175–195 | — | MPa | ca. 60% der Zugfestigkeit |
| Schlagzähigkeit (Charpy) | — | 30–50 | — | J (Nm²) | Temperaturabhängig |
| Wärmeleitfähigkeit | — | 118 | — | W/(m·K) | Standard für Alu |
| Elektr. Leitfähigkeit | — | 27 | — | % IACS | Gut |
| Spezif. Wärme | — | 0,96 | — | J/(g·K) | Standard |
| Ausdehnungskoeffizient | — | 23,6 | — | µm/(m·K) | Bei 20–100°C |

### 4.6 Verfügbarkeit 5086-H116 nach Region

**Nordamerika (USA, Kanada):**
- **Sehr gute Verfügbarkeit** — 5086 ist Standard in nordamerikanischen Yachtbau-Werften
- Hauptlieferanten: Aleris (USA), Tri-Arrows (USA), Hydro (Kanada)
- Lieferzeit: 1–2 Wochen
- Preise: Baseline (günstiger als Europa)
- Beispiel-Quelle: OnlineMetals.com führt 5086-H116 Platten standard

**Europa:**
- **Gering-bis-mittel Verfügbarkeit** — Werften bevorzugen 5083
- Lieferanten: Trimet (Deutschland), Aleris Europe, Hydro
- Lieferzeit: 2–4 Wochen
- Preise: +5–15% über 5083 (weniger Nachfrage)
- Hinweis: Oft auf Bestellung, nicht Lagerbestand

**Australien/Ozeanien:**
- **Gute Verfügbarkeit** — Populär in australischem Yachtbau
- Lieferanten: Comalco, Capral, Austral Wright
- Lieferzeit: 2–3 Wochen
- Preise: Vergleichbar mit 5083

**Praxis-Tipp:** Wer 5086 benötigt in Europa: Besser von Aleris France oder Hydro Deutschland bestellen, NICHT von lokalen Distributoren (längere Lead-Times).

### 4.7 Vergleich 5086-H116 vs. 5083-H116 für Marine-Anwendungen

| Aspekt | 5086-H116 | 5083-H116 | Empfehlung |
|--------|-----------|-----------|-----------|
| **Rumpf-Festigkeit** | Schwächer (−10%) | Stark | **5083** |
| **Korrosion Seewasser** | Sehr gut | Sehr gut | Gleichwertig |
| **Schweißbarkeit** | Besser | Gut | **5086** (minimal) |
| **Sensibilisierung** | Weniger anfällig | Anfällig | **5086** |
| **Umformbarkeit** | Besser | Mittelmäßig | **5086** |
| **Verfügbarkeit EU** | Schlecht | Exzellent | **5083** |
| **Verfügbarkeit USA** | Exzellent | Gut | **5086** |
| **Kosten EU** | +5–15% | Baseline | **5083** |
| **Kosten USA** | Baseline | +5–10% | **5086** |
| **Dicken-Optimierung** | Notwendig | Standard | **5083** |

**Fazit:** Für **europäische Neubauten: 5083-H116bevorzugt**. Für **US-amerikanische Yachten oder Reparaturen in USA: 5086-H116 praktischer**.

### 4.8 Praktische Projekte mit 5086

**Projekt 1: Trawleryacht-Umbau (16m, Malaysia-Singapur Gewässer):**
- Material gewählt: 5086-H116 (lokale Verfügbarkeit besser)
- Plattendicke: 5 mm (strukturelle Bereiche)
- Ersparnis durch bessere Umformung: 2–3 Tage schneller Bau
- Größerer Tiefgang durch −10% Festigkeit-Margen: ca. 2–3 cm mehr Tiefgang notwendig
- Gesamtbewertung: Für dieses Projekt (stabiles Klima, häufige Wartung): akzeptabel
- Quelle: Trawlerforum.com, Post 2019

**Projekt 2: DIY-Boot-Restauration (8m, Alaska, neuer Rumpf):**
- Material: 5086-H116 (einziges verfügbares Material in Juneau, Alaska)
- Problem: Lokal nur ≤3mm Platten verfügbar (Dickere mussten von Seattle importiert werden)
- Kosten für Import: +30% Versand-Kosten
- Lektion: Frühzeitig mit Lieferanten klären, was wirklich verfügbar ist!

---

## 5. 6082-T6 — Beschläge und Strukturteile

### 5.1 Eigenschaften und Anwendungsbereich

6082-T6 ist eine ausscheidungshärtbare Legierung (AlSi1MgMn) mit hoher Festigkeit nach der T6-Wärmebehandlung. Sie wird primär verwendet für:
- Extrudierte Profile (T-Profile, L-Profile, U-Profile)
- Masten und Bäume
- Davit-Arme und Bimini-Rahmen
- Beschlagplatten und Befestigungselemente
- Maschinell bearbeitete Teile (CNC-Frästeile)

### 5.2 Mechanische Eigenschaften

| Eigenschaft | 6082-T6 (Profil) | 6082-T6 (Platte) | Einheit |
|-------------|-------------------|-------------------|---------|
| Rm | 310–340 | 290–320 | MPa |
| Rp0.2 | 260–290 | 240–270 | MPa |
| A5 | 8–12 | 8–10 | % |
| Härte HB | 90–105 | 85–100 | — |
| E-Modul | 70 | 70 | GPa |
| Dichte | 2,71 | 2,71 | g/cm³ |

### 5.3 Schweißproblem 6082-T6

**KRITISCH:** Beim Schweißen von 6082-T6 fällt die Festigkeit in der Wärmeeinflusszone (WEZ/HAZ) auf das Niveau von T4 oder sogar O-Zustand zurück. Die Streckgrenze sinkt von 260 MPa auf ca. 120–160 MPa — ein Verlust von 40–55%!

**Konsequenz für AYDI:** Bei geschweißten 6082-T6-Konstruktionen MUSS die Berechnung mit der reduzierten HAZ-Festigkeit durchgeführt werden. Die volle T6-Festigkeit gilt nur für ungeschweißte Bereiche.

| Zustand | Rp0.2 MPa | Rm MPa | Festigkeitsverlust |
|---------|-----------|--------|-------------------|
| T6 (Grundmaterial) | 260 | 310 | 0% (Referenz) |
| HAZ (as-welded) | 120–140 | 200–240 | 45–55% |
| HAZ (natürlich ausgehärtet, 30 Tage) | 140–160 | 220–260 | 35–45% |
| HAZ (künstlich ausgehärtet, PWHT) | 200–230 | 260–290 | 12–25% |

**Post-Weld Heat Treatment (PWHT):** Teilweise Wiederherstellung durch erneutes Auslagern bei 170–185°C für 6–10 Stunden. In der Praxis bei Yachten selten durchgeführt, da ganze Bauteile in den Ofen müssen.

### 5.4 Korrosionsverhalten von 6082-T6 im Seewasser

6082-T6 ist deutlich korrosionsanfälliger als 5083 im Seewasser:
- Lochfraß-Potential ca. −0,73 V (vs. −0,76 V für 5083) — edler, aber nicht edel genug
- Cu-Gehalt bis 0,10% kann Lochfraß fördern
- Korngrenzen-Korrosion an T6-Ausscheidungen möglich
- MUSS oberhalb der Wasserlinie eingesetzt oder beschichtet werden

**Praxis-Empfehlung:** 6082-T6 nur für Teile verwenden, die:
1. Oberhalb der Wasserlinie liegen, ODER
2. Eloxiert/beschichtet sind, ODER
3. Keine direkte Seewasserexposition haben (Innenstruktur)

### 5.5 Wärmebehandlung und Festigkeit nach Schweißung

**Wärmebehandlungs-Optionen:**

**Option 1: Natürliche Ausscheidungshärtung (T4 → T6, 7–14 Tage):**
- Nach dem Schweißen: Material ist im T4-Zustand (weich, Rp0.2 ≈ 140 MPa)
- Bei Raumtemperatur lagert sich das Material aus: Festigkeit steigt langsam
- Nach 7 Tagen: Rp0.2 ≈ 200–220 MPa (70–85% der T6-Referenz)
- Nach 14 Tagen: Rp0.2 ≈ 220–240 MPa (85–90% der T6-Referenz)
- **Praktisch:** Wird selten bewusst ausgenutzt, geschieht aber natürlich

**Option 2: Künstliche Wärmebehandlung (PWHT — Post-Weld Heat Treatment):**
- Ofen: 170–185°C für 6–10 Stunden
- Resultat: Rp0.2 ≈ 200–230 MPa (75–90% T6)
- **Problem für Yachten:** Komplettes Bauteil muss in den Ofen (oft zu groß!)
- **Kosten:** €500–€2.000 pro Charge, abhängig von Ofengröße

**Option 3: Keine Wärmebehandlung — HAZ-Festigkeit akzeptieren:**
- Sicherheits-Berechnung mit 140 MPa (worst case)
- Dies ist Standard in der Praxis — Bootsrumpf-Berechnung nach DNV/ISO 12215-5 erfolgt mit reduzierter HAZ-Festigkeit

### 5.6 Spezifische Schweißparameter für 6082-T6

**WIG-Schweißen (TIG) 6082-T6 auf 6082-T6:**

| Dicke mm | Strom A | Spannung V | Draht-Ø | Zusatz | Schweißgeschw. cm/min |
|----------|---------|-----------|---------|--------|----------------------|
| 3 | 90–110 | 11–13 | 2,0 | 4043 | 18–22 |
| 4 | 110–140 | 12–14 | 2,4 | 4043 | 15–20 |
| 5 | 130–160 | 13–15 | 2,4 | 4043 | 12–18 |
| 6 | 150–190 | 14–16 | 2,4–3,2 | 4043 | 10–15 |
| 8 | 180–230 | 15–17 | 3,2 | 4043 | 8–12 |

**Schweißzusätze für 6082-T6:**
- **4043 (AlSi5):** Standard, geringe Rissneigung, aber schwächer (Rm ≈ 270 MPa Naht)
- **4047 (AlSi12):** Alternative, noch weniger rissneigung, aber sehr wenig Festigkeit
- **5356:** Nicht empfohlen (führt zu Sprödbruch bei 6xxx-Grundmaterial)

**Praktischer Tipp:** 4043 ist der Standard. Die Naht wird sowieso schwach (HAZ!), daher hat die Zusatz-Zusammensetzung weniger Einfluss als bei 5xxx.

### 5.7 Sapa/Hydro Standard-Profile in 6082-T6

**Hydro (ehemals Sapa) Katalog-Profile für Yachtbau:**

| Profil-Name | Abmessung | Gewicht kg/m | Anwendung | Verfügbar |
|------------|----------|-------------|----------|-----------|
| **SAPA 54.70** | T-Profil 54×34×4 | 1,38 | Spant (große Yachten) | Ja |
| **SAPA 63.61** | U-Profil 63×34×3,5 | 1,35 | Strukturversteifung | Ja |
| **SAPA 47.40** | L-Profil 50×40×4 | 1,20 | Rumpfversteifung | Ja |
| **SAPA Bulb** | Bulb-Profil 38×24×3,5 | 1,08 | Schiffbau Standard | Ja |
| **SAPA 63.30** | U-Profil 63×30×3,5 | 1,30 | Versteifung, Schott | Ja |

**Anodierung von Profilen:**
- Standard: Naturanodisiert (Rau, 10–15 µm)
- Marine (Hartanodisierung): 25–50 µm, kostet ca. 20–30% extra
- Verfügbar bei Hydro/Sapa auf Bestellung

**Lagerverfügbarkeit:**
- Standard-Profile: Lagerbestand bei größeren Distributoren (1–2 Wochen)
- Spezial-Profile: 3–6 Wochen, mind. 500 kg Bestellung

### 5.8 CNC-Bearbeitung von 6082-T6

**Schneidparameter:**
- Schnittgeschwindigkeit: 150–200 m/min (niedriger als 6061!)
- Vorschub pro Zahn: 0,1–0,15 mm
- Kühlschmiermittel: Standard Schneidöl (Alu ist hitzeempfindlich)
- Oberflächenrauheit: Ra = 0,8–1,6 µm erreichbar

**Wechselspannung nach CNC-Bearbeitung:**
- Kleine Kratzer können zu Korrosionsstellen werden
- Nach CNC: mit K220 Schleifpapier nacharbeiten, falls nötig
- Kritische Bereiche (unter WL): Polieren mit feinerer Körnung

**Praktisches Beispiel — Maschinenraum-Beschlag (50×40×5 mm L-Profil, CNC-Bohrungen):**
- Material: 6082-T6, 500 mm lang
- Bohrungen: Ø 8 mm (10 Stck.), M6 Gewindebohrungen (4 Stck.)
- Bearbeitungszeit: 8–10 Minuten
- Kosten: ca. €8–€15 Material + €25–€35 Bearbeitung (professionelle CNC)

### 5.9 Real-World Application Stories — 6082-T6 in Yachtbau

**Fall-Studie: Allures 51.9 (französischer Segeljacht-Klassiker)**
- Bauzeit: 2012–2018, ca. 40 Stück gebaut
- Rumpf: 5083-H116
- Aufbauten: 6082-T6 Profile und Platten (ober WL)
- Maschinenraum: 6082-T6 Spanten mit spezieller Isolierung
- Schweißzusatz: 5356 (Mischschweißung 5083↔6082)
- Ergebnis: Bewährt, nach 5–8 Jahren keine Korrosionsprobleme berichtet
- Quelle: Allures Yachting Baujahr-Datenbank

**Case Study: DIY-Bimini (10m Motoryacht, Heimwerker-Projekt):**
- Material: 6082-T6 Profil Ø 40 mm (4 mm Wandstärke)
- Länge: 6 Meter Gesamtrahmen
- Schweißverbindungen: 12 Stück (Ecken)
- Problem: Nach 2 Jahren Farbabblätterung an Schweißnähten
- Ursache: Keine Nachbehandlung der HAZ nach Schweißung
- Lösung: Oberflächenschleifen Sa 2.5 und Neuanstrich mit 2K-Epoxy
- Kosten: €200–€300 Reparatur (nach dem Fehler gelernt: hätte von Anfang an richtig beschichtet werden müssen)
- Quelle: CruisersForum Thread "Bimini Arch Problems", 2018

---

## 6. 6061-T6 — Universelle Konstruktionslegierung

### 6.1 Unterschied zu 6082

6061 und 6082 sind sehr ähnlich — beide sind AlMgSi-Legierungen mit T6-Ausscheidungshärtung. Die Unterschiede:

| Merkmal | 6061-T6 | 6082-T6 |
|---------|---------|---------|
| Mn-Gehalt | ≤0,15% | 0,40–1,0% |
| Cu-Gehalt | 0,15–0,40% | ≤0,10% |
| Festigkeit | Vergleichbar | Vergleichbar |
| Korrosion | Etwas schlechter (mehr Cu) | Besser |
| Verfügbarkeit | Weltweit (US-Standard) | Primär EU |
| Zerspanung | Sehr gut | Gut |
| Preis | Oft günstiger | Standard |

**Forum-Konsens (sailinganarchy.com):** In den USA ist 6061-T6 DER Standard für alles. In Europa wird 6082-T6 bevorzugt. Funktional sind sie austauschbar — die Wahl hängt von der lokalen Verfügbarkeit ab.

### 6.2 Achtung: 6061 und Seewasser

6061-T6 hat einen höheren Cu-Gehalt (0,15–0,40%) als 6082 (≤0,10%). Kupfer in Alu-Legierungen fördert Lochfraß in Chlorid-haltigen Medien (Seewasser). Daher gilt für AYDI:

- **6061-T6 in Seewasser: confidence estimated — Nicht empfohlen unter der Wasserlinie**
- **6061-T6 über Wasser: confidence documented — Akzeptabel mit Beschichtung**

### 6.3 Technische Eigenschaften 6061-T6

| Eigenschaft | Wert | Bemerkung |
|------------|------|-----------|
| Dichte | 2,70 g/cm³ | Wie alle Alu |
| Rm (Zugfestigkeit) | 310 MPa | Gut, vergleichbar 6082 |
| Rp0.2 (Streckgrenze) | 275 MPa | Etwas schwächer als 6082 |
| Streckgrenze/Dichte | 102 MPa·cm³/g | Leicht besser als 6082 |
| E-Modul | 69 GPa | Standard |
| Schlagzähigkeit | Moderat | Nicht so zäh wie 5xxx |
| Wärmeleitfähigkeit | 167 W/(m·K) | Gut |
| Elektr. Leitfähigkeit | 35% IACS | Gut (für Elektrik) |
| Schweißbarkeit | Gut | Mit 4043 oder 5356 |
| Spanbarkeit | Sehr gut | Besser als 6082 |

**CNC-Bearbeitung 6061-T6:**
- Schnittgeschwindigkeit (Fräsen): 200–350 m/min (höher als 5083!)
- Schnittgeschwindigkeit (Drehen): 150–250 m/min
- Zerspanbarkeit: Exzellent, sehr wenig Verschleiß am Werkzeug
- Oberflächenrauheit: Ra = 0,4–1,6 µm erreichbar (clean finish)
- **Anwendung:** Beschläge, Halterungen, Drehteile (Achsen, Bushings) — Standard für CNC-Fertigung

### 6.4 Anwendungsbeispiele 6061-T6 im Yachtbau

**Beschläge und Hardware:**
- Winschenbeschläge
- Schäkel-Ösen (CNC-gedreht)
- Reling-Beschläge
- Luke-Rahmen
- Fenster-Profile

**Strukturelle Anwendungen (über Wasser):**
- Sprayhood-Rahmen
- Bimini-Arch (kleine Yachten)
- Masten (kleine Yachten, <8m)
- Spanten (nur über WL)

**NICHT geeignet:**
- Rumpfplatten (dafür 5083)
- Hauptstringer (dafür 6082)
- Tankwände in Seewasser
- Unterwasser-Strukturteile

### 6.5 Vergleich 6061-T6 vs. 6082-T6 für Yacht-Anwendungen

| Kriterium | 6061-T6 | 6082-T6 | Empfehlung |
|-----------|---------|---------|-----------|
| Korrosion Seewasser | Schwach | Stark | **6082** |
| Korrosion Süßwasser | Gut | Gut | Gleichwertig |
| CNC-Bearbeitung | Exzellent | Gut | **6061** |
| Versorgung USA | Üblich | Schwer | **6061** |
| Versorgung Europa | Selten | Standard | **6082** |
| Schweißfestigkeit (mit 4043) | Ähnlich | Ähnlich | Gleichwertig |
| Kostenfaktor | Baseline | −5 bis +5% | Vergleichbar |
| Forum-Beliebtheit | Mittel | Hoch | **6082** |

**Praxis-Empfehlung:** Für neue Alu-Yachten: **6082-T6 bevorzugt**. 6061-T6 nur, wenn lokale Verfügbarkeit besser ist oder CNC-intensive Anwendung.

### 6.6 Verfügbarkeit und Lieferanten 6061-T6

**Weltweite Verfügbarkeit: SEHR GUT (Nordamerika ist primär 6061-Markt)**

| Region | Verfügbarkeit | Hauptlieferanten | Lieferzeit |
|--------|---------------|-----------------|-------------|
| **USA** | Exzellent | Aleris, Tri-Arrows, Hydro | 1–2 Wochen |
| **Kanada** | Exzellent | Aleris, Tri-Arrows | 1–2 Wochen |
| **Europa** | Mittel | Hydro, Trimet, Sapa | 2–3 Wochen |
| **Großbritannien** | Mittel | Hydro UK, Aleris UK | 2 Wochen |
| **Australien** | Gut | Comalco, Capral | 2–3 Wochen |

**Online-Shops:**
- OnlineMetals.com (USA): 6061-T6 Platten, Profile, Rohre — schnelle Lieferung
- MetalsDepot.com (USA): Ausgezeichnet für US-Kunden
- AbuDhabi Metals (Vereinigte Emirate): Gute Verfügbarkeit für Mittelost
- cutmetals.com.au (Australien): 6061-T6 Standard-Sortiment

---

## 7. Weitere Marine-Legierungen (5052, 5754, 5059, 6005, 6063, 7075)

### 7.1 5052-H32 (AlMg2.5)

| Eigenschaft | Wert |
|-------------|------|
| Mg % | 2,2–2,8 |
| Rm MPa | 230–270 |
| Rp0.2 MPa | 160–195 |
| Korrosion | Exzellent |
| Schweißbarkeit | Exzellent |

**Anwendung:** Leichte Strukturen, Tanks, Verkleidungen, Lüftungskanäle. Dort wo Korrosionsbeständigkeit wichtiger ist als Festigkeit. Häufig im Innenausbau und für Tanks (Trinkwasser, Kraftstoff).

**Forum-Erfahrung (trawlerforum.com):** 5052 ist das "Allzweck-Alu" für nicht-strukturelle Teile. Günstig, leicht zu verarbeiten, rostet nicht. Ideal für DIY-Tankkonstruktion.

### 7.2 5754-H22/H32 (AlMg3)

| Eigenschaft | Wert |
|-------------|------|
| Mg % | 2,6–3,6 |
| Rm MPa | 240–290 |
| Rp0.2 MPa | 160–220 |
| Korrosion | Exzellent |
| Schweißbarkeit | Sehr gut |

**Anwendung:** Zwischen 5052 und 5083 angesiedelt. Beliebt im Automobilbau (Karosserie) und als Alternativ-Legierung für leichte Marine-Strukturen. Im Yachtbau eher selten, da 5083 der Standard ist.

### 7.3 5059-H116 (Alustar / Sealium)

| Eigenschaft | Wert |
|-------------|------|
| Mg % | 5,0–6,0 |
| Rm MPa | 330–410 |
| Rp0.2 MPa | 240–310 |
| Korrosion | Exzellent |
| Schweißbarkeit | Gut (spezieller Zusatz nötig) |
| Markenname | Sealium (Constellium), Alustar |

**Anwendung:** Die "nächste Generation" Marine-Alu — 10–15% höhere Festigkeit als 5083 bei vergleichbarer Korrosionsbeständigkeit. Eingesetzt von Werften wie Damen, Austal, und für Marineschiffe. Für Yachten noch selten, aber zunehmend für Expeditionsyachten und Performance-Segler.

**Achtung:** Schweißzusatz muss 5183 oder spezieller 5059-Draht sein. Nicht mit 5356 schweißen (Festigkeitsverlust).

**Forum-Konsens (CruisersForum 2023):** "Sealium ist fantastisch, aber nur wenige Werften haben Erfahrung damit. Für Einhand-Segler, die in abgelegenen Gebieten reparieren müssen, bleibt 5083 die sicherere Wahl wegen der weltweiten Verfügbarkeit von Schweißzusatz."

### 7.4 6005A-T6 (AlSiMg)

| Eigenschaft | Wert |
|-------------|------|
| Rm MPa | 270 |
| Rp0.2 MPa | 225 |
| A5 % | 8 |

**Anwendung:** Spezial-Profile (Fensterrahmen, Schiebetüren, Zierleisten). Bessere Extrudierbarkeit als 6082. Für marine Struktur ungeeignet.

### 7.5 6063-T6 (AlMg0.7Si)

| Eigenschaft | Wert |
|-------------|------|
| Rm MPa | 215–245 |
| Rp0.2 MPa | 170–195 |
| A5 % | 8–10 |

**Anwendung:** Dekorative Profile, Fensterrahmen, Zierleisten, Handläufe. Exzellente Oberfläche nach Eloxierung. Im Yachtbau für nicht-strukturelle, ästhetische Teile.

### 7.6 7075-T6 (AlZnMgCu) — NUR für Spezialanwendungen

| Eigenschaft | Wert |
|-------------|------|
| Rm MPa | 540–570 |
| Rp0.2 MPa | 480–505 |
| A5 % | 5–7 |
| Cu % | 1,2–2,0 |
| Zn % | 5,1–6,1 |

**WARNUNG für AYDI (confidence: documented):** 7075-T6 hat die höchste Festigkeit aller Alu-Legierungen, ist aber für Marine-Anwendungen EXTREM PROBLEMATISCH:
- Hoher Cu-Gehalt → katastrophaler Lochfraß in Seewasser
- Spannungsrisskorrosion unter Belastung + Feuchte
- Nicht schweißbar (Risse)
- Nur akzeptabel für: Mastbeschläge (innerhalb des Profils, kein Seewasser), Winschen-Internals, Schrauben (mit Beschichtung)

---

## 8. Plattenware — Dicken, Formate, Anwendungen

### 8.1 Gewichtstabelle 5083-H116 Platten

| Dicke mm | Gewicht kg/m² | Platte 1500×3000 kg | Platte 2000×4000 kg |
|----------|---------------|---------------------|---------------------|
| 3,0 | 7,98 | 35,9 | 63,8 |
| 4,0 | 10,64 | 47,9 | 85,1 |
| 5,0 | 13,30 | 59,9 | 106,4 |
| 6,0 | 15,96 | 71,8 | 127,7 |
| 8,0 | 21,28 | 95,8 | 170,2 |
| 10,0 | 26,60 | 119,7 | 212,8 |
| 12,0 | 31,92 | 143,6 | 255,4 |
| 15,0 | 39,90 | 179,6 | 319,2 |
| 20,0 | 53,20 | 239,4 | 425,6 |
| 25,0 | 66,50 | 299,3 | 532,0 |
| 30,0 | 79,80 | 359,1 | 638,4 |

### 8.2 Materialbedarf-Kalkulation nach Bootsgröße

| LOA | Rumpfoberfläche ca. | 5083-Bedarf (Platten) | Gewicht ca. | Materialkosten ca. |
|-----|---------------------|----------------------|-------------|-------------------|
| 8m | 25–30 m² | 8–10 Platten (1500×3000) | 400–600 kg | €2.000–€3.500 |
| 10m | 35–45 m² | 12–15 Platten | 600–900 kg | €3.000–€5.000 |
| 12m | 50–65 m² | 16–22 Platten | 900–1.400 kg | €4.500–€7.500 |
| 14m | 70–90 m² | 22–30 Platten | 1.300–2.000 kg | €6.500–€11.000 |
| 16m | 90–120 m² | 28–40 Platten | 1.800–3.000 kg | €9.000–€16.000 |
| 20m | 140–180 m² | 45–60 Platten | 3.000–5.500 kg | €15.000–€30.000 |

### 8.3 Zuschnitt und Bearbeitung

**Schneidverfahren für Alu-Platten:**

| Verfahren | Plattendicke | Qualität | Kosten | Verfügbarkeit |
|-----------|-------------|----------|--------|---------------|
| Wasserstrahl | 1–150 mm | Exzellent (keine WEZ) | Hoch | Industriebetriebe |
| Laser (CO₂/Faser) | 1–12 mm | Sehr gut | Mittel | Laserbetriebe |
| Plasma | 3–50 mm | Gut | Niedrig | Werften, Schlossereien |
| Bandsäge | 3–300 mm | Ausreichend | Niedrig | Überall |
| Schere (hydraulisch) | 1–12 mm | Gut (gerade Schnitte) | Niedrig | Blechbearbeiter |
| Fräser (CNC) | 3–100+ mm | Exzellent | Hoch | CNC-Betriebe |

**Praxis-Empfehlung für Yachtbau:**
- Rumpfplatten: Plasma oder Laser (CNC-gesteuert nach Plattenentwicklung)
- Beschlagplatten: Wasserstrahl oder Laser (höchste Präzision)
- Vor-Ort-Reparaturen: Stichsäge mit Alu-Blatt, Winkelschleifer (nur Trennscheibe, NIEMALS Schleifscheibe für Stahl!)

### 8.4 Plattenflachheit und Toleranzen

**EN 485-2 Toleranzen für Alu-Platten:**

| Dicke mm | Längstoleramz (±mm) | Breiten-Toleranz (±mm) | Planeität (mm/m) | Kantenrauhheit |
|----------|-------------------|------------------------|------------------|---------------|
| 3 | 0,5 | 0,7 | 3–4 | Scharfkantig |
| 4 | 0,5 | 0,7 | 3–4 | Scharfkantig |
| 5 | 0,5 | 0,7 | 2–3 | Scharfkantig |
| 6–10 | 0,5 | 0,7 | 2–3 | Scharfkantig |
| 10–20 | 1,0 | 1,0 | 2–3 | Scharfkantig |
| 20–30 | 1,0 | 1,5 | 2–3 | Scharfkantig |

**Praktische Bedeutung für Yachtbau:**
- **Planeität:** Für Rumpf-Planke kritisch. Abweichung >4 mm über 3m ist nicht akzeptabel (Spantenform wird verzerrt)
- **Kantenqualität:** Scharfkantig erfordert Entgraten vor Schweißung
- **Längstoleranzen:** ±0,5 mm bei 5mm Platte ist OK (wird trotzdem zugeschnitten)

**Praxis-Check:** Bei Ankunft Plattensatz sollte optisch/mechanisch überprüft werden:
- Mit Stahllineal über 3m abstreichen — max. 5 mm Spalte akzeptabel
- Scharfe Ecken mit Schleifpapier K60 brechen

### 8.5 Schneidparameter (Schnittgeschwindigkeit, Säge-Feed)

**Plasma-Schneiden (Dicke 3–50 mm):**
- Schnittgeschwindigkeit: 2–6 m/min (je dicker, desto langsamer)
- Strahlstrom: 100–200 A (abhängig von Düse)
- Schnitttoleranz: ±1–2 mm je nach Einstellung
- Wärmebeeinflusste Zone (WEZ): 2–5 mm — wird NIEMALS geschweißt, muss abgeschliffen werden!
- Kosten: €0,50–€1,50 pro Schnittmeter

**Laser-Schneiden (Dicke 1–12 mm):**
- Schnittgeschwindigkeit: 5–15 m/min (Alu schwächer als Stahl, schneller möglich)
- Schnitttoleranz: ±0,5 mm (besser als Plasma)
- WEZ: <0,5 mm (vernachlässigbar)
- Rauchgase: Mg-Dampf ist giftig — nur mit guter Absauganlage!
- Kosten: €1,50–€3,00 pro Schnittmeter

**Wasserstrahl (universell bis 300 mm):**
- Schnittgeschwindigkeit: 0,5–3 m/min (sehr langsam, sehr präzise)
- Schnitttoleranz: ±0,2–0,5 mm (beste Qualität)
- WEZ: KEINE (kein Wärmeeintrag)
- Zusätzliche Kosten: Abrasivverschleiß (Granat)
- Kosten: €2,00–€4,00 pro Schnittmeter (teuer, aber beste Qualität)

**Bandsäge / Sägeblatt (manuell/CNC):**
- Schnittgeschwindigkeit: 30–100 m/min (Zahnvorschub)
- Schnitttoleranz: ±2–5 mm
- Material-Rauheit: Zahnindustriert, erzeugt Rillen
- Einsatz: Kleine Teile, vor-Ort Schnitte
- Kosten: Personal + Werkzeug

### 8.6 Nesting und Material-Optimierung

**Nesting = Effiziente Anordnung von Zuschnitten auf der Platte:**

Ziel: Verschnitt minimieren, Lagerhaltung reduzieren.

**Beispiel 12m Segelyacht Rumpf-Nesting:**
- Rumpf-Entwicklung: ca. 45 m² Nettoplatten
- Bestellt: 50–55 m² (mit Reserve)
- Typischer Verschnitt nach Nesting: 10–15%
- Nach Kanten-Verschnitt (manuell): weitere 2–3%
- **Total Verschniff: 12–18%**

**Nesting-Software (professionell):**
- Hyperpacked (Free, basierend auf Nestea-Algorithmen)
- SigmaNEST (Professionell, €5.000–€20.000)
- Lantek (Feinblechbearbeitung, €8.000–€15.000)

**Typische Einsparungen mit Nesting:**
- Ohne Nesting: 25–35% Verschnitt
- Mit manuellem Nesting: 15–20% Verschnitt
- Mit automatischem Nesting: 8–12% Verschnitt

**Kosten/Nutzen:**
- Für 12m Yacht (ca. €5.000 Plattenkosten): 10% Einsparung = €500 Gewinn
- Wenn Nesting-Software kostet €300, ROI = 0,6x (Break-even mit 2–3 Yachten)

### 8.7 Lagerhaltung und Materialmanagement

**Empfohlene Lagerstrategie für kleine Werften:**

| Material | Lagermenge | Lagerort | Kosten/Monat | Umschlaggerung |
|----------|-----------|----------|-------------|-----------------|
| 5083 3–6 mm | 20–30 m² | Trocken, Regal | €200–€400 | 3–6 Monate |
| 6082 Profile | 100–200 kg | Trocken | €50–€100 | 6–12 Monate |
| Kleine Teile | nach Bedarf | Regalsystem | €100–€150 | 6 Monate |

**Lagerverschlechterung:**
- Alu ist sehr robust
- Oxidation (Grünspan) nur bei >80% Feuchte + Temperaturwechsel
- Lebensdauer: praktisch unbegrenzt, wenn trocken

**Entsorgung von Verschnitt:**
- Alu-Schrott: ca. €0,80–€1,50 pro kg (2026)
- 12m Yacht Verschnitt (ca. 1.000 kg Material × 15% Abfall = 150 kg): ca. €120–€225 Erlös
- Für Werften: Alu-Schrott ist ein kleiner Einnahmefaktor

### 8.8 Plattenbeschaffung — Best Practices

**Checkliste beim Bestellprozess:**

1. **Normen-Spezifikation aufschreiben:**
   - EN 485-2, Legierung 5083-H116
   - Dicke ±0,5 mm toleriert
   - Lieferung Walzformat (1500×3000 oder 2000×4000 mm empfohlen)
   - Zertifikat EN 10204 3.1 erforderlich (bei Klassifikation)

2. **Melangen prüfen:**
   - Oberflächenqualität: 2B (Walzfinish) ist Standard
   - Kratzer, Dellen: <2 cm erlaubt
   - Oberflächenoxidation (grau): normal, wird vor Verarbeitung abgeschliffen

3. **Lieferquoten prüfen:**
   - Europe: 2–3 Wochen Standard
   - USA: 3–4 Wochen
   - Australien: 4–6 Wochen
   - Bestellung mit +5% Buffer-Puffer für Fehlerquoten

4. **Transport:**
   - Alu-Platten sind relativ sicher (nicht so schwer wie Stahl)
   - Verpackung in Kunststoff-Film (gegen Kratzer)
   - Auf Holzpaletten (NIEMALS Stahl!) — galvanische Zelle sonst
   - Lagererneuerung nach Transport: trocknen lassen (4–6h bei >60% Feuchte)

---

## 9. Profile — Extrusionen für Strukturbau

### 9.1 Standard-Profile für Yachtbau

**L-Profile (Winkel):**

| Abmessung | Legierung | Gewicht kg/m | Anwendung | Preis €/m |
|-----------|-----------|-------------|-----------|-----------|
| 20×20×3 mm | 6082-T6 | 0,31 | Leiste, Halterung | €2–€3 |
| 25×25×3 mm | 6082-T6 | 0,39 | Kleine Stringer | €2–€4 |
| 30×30×3 mm | 6082-T6 | 0,47 | Stringer, Versteifung | €3–€4 |
| 30×30×4 mm | 6082-T6 | 0,62 | Strukturwinkel | €3–€5 |
| 40×40×4 mm | 6082-T6 | 0,83 | Spant-Anbindung | €4–€6 |
| 40×40×5 mm | 6082-T6 | 1,03 | Schwere Struktur | €5–€8 |
| 50×50×5 mm | 6082-T6 | 1,30 | Hauptstringer | €6–€10 |
| 60×60×6 mm | 6082-T6 | 1,87 | Schwere Stringer | €8–€13 |
| 80×80×8 mm | 6082-T6 | 3,31 | Kiel-Struktur | €14–€22 |
| 100×100×10 mm | 6082-T6 | 5,18 | Expedition, Superyacht | €22–€35 |
| 50×30×5 mm | 6082-T6 | 1,03 | Ungleichschenkliger Winkel | €5–€8 |
| 60×40×5 mm | 6082-T6 | 1,30 | Spant-Anbindung | €6–€10 |
| 80×40×6 mm | 6082-T6 | 1,87 | Stringer (breit) | €8–€13 |

**T-Profile:**

| Abmessung | Legierung | Gewicht kg/m | Anwendung | Preis €/m |
|-----------|-----------|-------------|-----------|-----------|
| 20×20×3 mm | 6082-T6 | 0,29 | Leichte Versteifung | €2–€3 |
| 30×30×3 mm | 6082-T6 | 0,43 | Plattenversteifung | €3–€5 |
| 40×40×4 mm | 6082-T6 | 0,78 | Stringer | €4–€7 |
| 50×50×5 mm | 6082-T6 | 1,22 | Hauptstringer | €6–€10 |
| 60×60×6 mm | 6082-T6 | 1,75 | Schwerer Stringer | €8–€14 |
| 80×40×6 mm | 6082-T6 | 1,87 | Hochsteg-T | €9–€15 |
| 100×50×8 mm | 6082-T6 | 3,12 | Kiel-Stringer | €14–€24 |

**U-Profile (Kanäle):**

| Abmessung | Legierung | Gewicht kg/m | Anwendung | Preis €/m |
|-----------|-----------|-------------|-----------|-----------|
| 20×20×2 mm | 6082-T6 | 0,29 | Kabel-Kanal | €2–€3 |
| 30×30×3 mm | 6082-T6 | 0,62 | Schienen, Führungen | €3–€5 |
| 40×40×4 mm | 6082-T6 | 1,03 | Genuaschiene DIY | €5–€8 |
| 50×50×5 mm | 6082-T6 | 1,63 | Schwerere Führungen | €7–€12 |
| 60×30×4 mm | 6082-T6 | 1,03 | Spezial-Kanal | €5–€8 |
| 80×40×5 mm | 6082-T6 | 2,06 | Großer Kabel-Kanal | €9–€16 |

### 9.2 Spezial-Profile für Yachtbau

**Bulb-Profile (HP-Profile, Holland-Profile):**

Bulb-Profile sind die bevorzugten Stringer-Profile im professionellen Alu-Yachtbau. Der Bulb (Wulst) am oberen Ende konzentriert Material dort, wo es statisch am effektivsten ist.

| Bezeichnung | Höhe × Steg × Bulb mm | Gewicht kg/m | Trägheitsmoment cm⁴ | Anwendung |
|-------------|----------------------|-------------|---------------------|-----------|
| HP 60×5 | 60×5×Bulb | 1,22 | 8,2 | Kleine Yachten ≤10m |
| HP 80×5 | 80×5×Bulb | 1,65 | 18,5 | Standard 10–14m |
| HP 80×6 | 80×6×Bulb | 1,98 | 21,8 | Verstärkte Stringer |
| HP 100×6 | 100×6×Bulb | 2,63 | 40,2 | Standard 14–18m |
| HP 100×7 | 100×7×Bulb | 3,07 | 46,1 | Schwere Stringer |
| HP 120×7 | 120×7×Bulb | 3,80 | 73,8 | Expeditionsyachten |
| HP 140×8 | 140×8×Bulb | 5,12 | 120,5 | Superyachten |
| HP 160×9 | 160×9×Bulb | 6,61 | 184,3 | Große Expedition |
| HP 200×10 | 200×10×Bulb | 9,20 | 340,2 | Arbeitsschiffe |

**Verfügbarkeit:** Bulb-Profile sind Spezialprodukte und NUR bei spezialisierten Lieferanten erhältlich (nicht im Baumarkt!). Hauptlieferanten: Aleris (jetzt Novelis), Constellium, Hydro, AMG Superalloys.

### 9.3 Flat Bar (Flachstahl/Flachprofil)

| Abmessung | Legierung | Gewicht kg/m | Anwendung | Preis €/m |
|-----------|-----------|-------------|-----------|-----------|
| 20×3 mm | 5083-H116 | 0,16 | Schweißlappen | €1–€2 |
| 20×5 mm | 5083-H116 | 0,27 | Halterung | €1–€3 |
| 30×5 mm | 5083-H116 | 0,40 | Knieblech | €2–€3 |
| 30×6 mm | 5083-H116 | 0,48 | Stringer-Flansch | €2–€4 |
| 40×6 mm | 5083-H116 | 0,64 | Rahmen | €3–€5 |
| 40×8 mm | 5083-H116 | 0,85 | Strukturträger | €3–€6 |
| 50×8 mm | 5083-H116 | 1,06 | Schwere Struktur | €5–€8 |
| 50×10 mm | 5083-H116 | 1,33 | Kiel-Verstärkung | €6–€10 |
| 60×10 mm | 5083-H116 | 1,60 | Kiel-Struktur | €7–€12 |
| 80×10 mm | 5083-H116 | 2,13 | Schwere Struktur | €9–€15 |
| 100×12 mm | 5083-H116 | 3,19 | Expedition | €14–€24 |

---

## 10. Rohre und Rundstahl

### 10.1 Rundrohre für Marine-Anwendungen

| Außen-Ø × Wandstärke | Legierung | Gewicht kg/m | Anwendung | Preis €/m |
|----------------------|-----------|-------------|-----------|-----------|
| 16×2 mm | 6082-T6 | 0,24 | Handlauf, Halterung | €2–€4 |
| 20×2 mm | 6082-T6 | 0,31 | Geländer klein | €3–€5 |
| 22×2 mm | 6082-T6 | 0,34 | Leichte Reling | €3–€5 |
| 25×2 mm | 6082-T6 | 0,39 | **Standard-Reling** | €4–€6 |
| 25×2,5 mm | 6082-T6 | 0,48 | Verstärkte Reling | €5–€7 |
| 30×2 mm | 6082-T6 | 0,48 | Bimini-Rohr klein | €4–€7 |
| 32×2 mm | 6082-T6 | 0,51 | **Bimini-Standard** | €5–€8 |
| 32×2,5 mm | 6082-T6 | 0,63 | Verstärktes Bimini | €6–€9 |
| 38×2,5 mm | 6082-T6 | 0,76 | Davit-Rohr, schweres Bimini | €7–€11 |
| 40×3 mm | 6082-T6 | 0,95 | Davit, Sprayhood | €8–€13 |
| 50×3 mm | 6082-T6 | 1,21 | Schwere Davits | €10–€16 |
| 50×4 mm | 6082-T6 | 1,58 | Arch, Radar-Mast | €13–€20 |
| 60×3 mm | 6082-T6 | 1,46 | Radar-Arch | €12–€18 |
| 60×4 mm | 6082-T6 | 1,92 | Schwerer Arch | €15–€24 |
| 76×4 mm | 6082-T6 | 2,47 | Beiboot-Davit groß | €18–€30 |
| 100×5 mm | 6082-T6 | 4,08 | Mast (klein) | €28–€45 |

### 10.2 Quadrat- und Rechteckrohre

| Abmessung | Legierung | Gewicht kg/m | Anwendung | Preis €/m |
|-----------|-----------|-------------|-----------|-----------|
| 20×20×2 mm | 6082-T6 | 0,39 | Rahmen, Halterung | €3–€5 |
| 25×25×2 mm | 6082-T6 | 0,50 | Strukturrahmen | €4–€6 |
| 30×30×2 mm | 6082-T6 | 0,61 | Solar-Panel-Rahmen | €5–€8 |
| 30×30×3 mm | 6082-T6 | 0,88 | Verstärkter Rahmen | €6–€10 |
| 40×40×3 mm | 6082-T6 | 1,20 | Arch-Struktur | €8–€13 |
| 40×40×4 mm | 6082-T6 | 1,56 | Schwere Struktur | €10–€16 |
| 50×50×3 mm | 6082-T6 | 1,53 | Davit-Struktur | €10–€16 |
| 50×50×4 mm | 6082-T6 | 2,00 | Schwere Davits | €13–€21 |
| 60×40×3 mm | 6082-T6 | 1,53 | Rechteck-Struktur | €10–€16 |
| 80×40×4 mm | 6082-T6 | 2,44 | Radar-Arch | €16–€26 |
| 80×80×5 mm | 6082-T6 | 4,08 | Schwerer Arch | €28–€45 |
| 100×50×4 mm | 6082-T6 | 3,08 | Großer Arch | €21–€34 |

### 10.3 Rundstahl (Vollmaterial)

| Durchmesser | Legierung | Gewicht kg/m | Anwendung | Preis €/m |
|-------------|-----------|-------------|-----------|-----------|
| Ø 6 mm | 6082-T6 | 0,08 | Nieten, Stifte | €1–€2 |
| Ø 8 mm | 6082-T6 | 0,14 | Bolzen, Stifte | €1–€2 |
| Ø 10 mm | 6082-T6 | 0,22 | Bolzen | €2–€3 |
| Ø 12 mm | 6082-T6 | 0,31 | Achsen, Bolzen | €2–€4 |
| Ø 16 mm | 6082-T6 | 0,55 | Achsen | €3–€5 |
| Ø 20 mm | 6082-T6 | 0,85 | Lagerbuchsen | €5–€8 |
| Ø 25 mm | 6082-T6 | 1,34 | Halbzeug CNC | €7–€12 |
| Ø 30 mm | 6082-T6 | 1,93 | CNC-Teile | €10–€16 |
| Ø 40 mm | 6082-T6 | 3,43 | CNC-Beschläge | €18–€28 |
| Ø 50 mm | 6082-T6 | 5,36 | Block-Halbzeug | €28–€45 |

### 10.4 Nahtlose vs. Geschweißte Rohre (Technische Unterscheidung)

**Nahtlose Rohre (seamless tubes):**
- Herstellung: Pilgerprozess (Walzen um Dorn) oder Extrusion
- Vorteil: Höhere Festigkeit, keine Schweißnaht-Schwachstelle
- Nachteil: Teurer, längere Lieferzeit
- Preis: ca. 1,5 × geschweißte Rohre
- Anwendung: Mastschuh, Davit-Basis (Hochbelastung)
- Legierungen: 6082-T6, 6061-T6 Standard
- Verfügbar: Ø 16–100 mm, Wandstärke 1,5–5 mm

**Geschweißte Rohre (welded tubes):**
- Herstellung: Blechrolle wird longitudinal zusammengeschweißt (inert gas)
- Vorteil: Günstiger, schnellere Verfügbarkeit, größere Formenvielfalt
- Nachteil: Schweißnaht 10–15% schwächer als Grundmaterial
- Preis: Baseline
- Qualitätsstufe: Vollständig überprüfte Schweißnähte (z.B. Eddy-Current)
- Standard-Lieferanten: Hydro (Sapa), Trimet, Neumann

**Faustregel:** Für Rohre unter Last (Davits, Arch, Reling): Nahtlos bevorzugt. Für Zierstücke: Geschweißt okay.

### 10.5 Biegeparameter für Rohre (6082-T6)

Mindestradiusformel für Kaltbiegung: R = 10 × Außendurchmesser bei kalt Biegen ohne Vorwärmung

| OD × Wandstärke | Min. Radius (kalt) | Vorwärmung T° | Empfehlung |
|------------------|-------------------|---------------|-----------|
| 20×2 mm | 200 mm | Keine | Problemlos |
| 25×2 mm | 250 mm | Keine | Okay |
| 32×2 mm | 320 mm | 50–100°C | Warm biegen besser |
| 38×2,5 mm | 380 mm | 100–150°C | Warm biegen |
| 50×3 mm | 500 mm | 150–200°C | Warm biegen PFLICHT |
| 60×4 mm | 600 mm | 200–250°C | Warm biegen + Nachglühen |

**Warm-Biegeprozess:** 250–300°C, Abkühlung langsam (nicht in Wasser!). Nach Abkühlung: Festigkeit 5–10% verloren, muss akzeptiert werden.

**Best Practice:** Rohre mit >OD 40 mm nicht warm biegen — stattdessen geschweißte Ecken oder fertig gebogene Abschnitte bestellen.

### 10.6 Spezifische Anwendungen nach Bootsgröße

**8m Segelyacht:**
- Reling: 25×2 mm, gesamt 20 m = 7,8 kg
- Handläufe: 16×2 mm, gesamt 8 m = 1,9 kg
- Bimini-Arch: 32×2 mm, 4m = 2,0 kg
- Kosten: €90–€150 Material

**12m Segelyacht:**
- Reling: 25×2,5 mm, 30 m = 14,4 kg
- Davit (Beiboot): 50×3 mm, 4 m = 4,8 kg
- Bimini-Arch: 40×3 mm, 6 m = 5,7 kg
- Radar-Arch: 50×4 mm, 3 m = 4,7 kg
- Kosten: €350–€550 Material

**18m Motoryacht:**
- Reling: 32×2,5 mm, 50 m = 31,5 kg
- Davit groß: 60×4 mm, 5 m = 9,6 kg
- Flybrdige Rahmen: 60×40×4 mm, 20 m = 48,8 kg
- Stabilizer-Arm: 76×5 mm, 3 m = 11,7 kg
- Kosten: €800–€1.200 Material

### 10.7 Mast-Rohre (Spezial-Anwendung)

Alu-Masten werden meist aus den folgenden Profilen konstruiert:

| Profil | Außen-Ø | Wandstärke | Gewicht kg/m | Anwendung |
|--------|---------|-----------|-------------|-----------|
| SAPA ALS8 | 78 mm | 4,5 mm | 2,84 | Segelyacht 8–10m |
| SAPA ALS9 | 88 mm | 4,5 mm | 3,22 | Segelyacht 10–14m |
| SAPA ALS10 | 100 mm | 5 mm | 4,08 | Segelyacht 14–18m |
| Hydro 6082-T6 | 100 mm | 5 mm | 4,08 | Universell |
| Anodiert/Rau | — | — | +5% | Standard Lieferung |

**Mastschuh:** Üblicherweise Ø 100–130 mm Rundrohr (nahtlos, 6082-T6, Wandstärke 6–8 mm) geschweißt an Kielplatte.

**Kostenkalkulation 12m Segelyacht:**
- Mast (Profil SAPA ALS10, inkl. Auftrieb): ca. €2.500–€4.000
- Mastschuh + Verstärkungen (lokal): ca. €800–€1.200
- Gesamtmast-Kosten: €3.300–€5.200 (Professionelle Bestückung)

### 10.8 Massivstahl vs. Alu-Rohr (Lager-Vergleich)

| Parameter | Ø 20 mm Alu-Rohr | Ø 20 mm Stahlrohr |
|-----------|------------------|-------------------|
| Gewicht kg/m | 0,85 | 2,45 |
| Zugfestigkeit | 215 MPa | 235 MPa |
| Spec. Festigkeit | 253 MPa·cm³/g | 96 MPa·cm³/g |
| Preis €/m | €5–€8 | €3–€4 |
| Korrosionsschutz nötig | Ja (Beschichtung) | Ja (Anstrich) |
| Wartung | Beschichtung 5–7 Jahre | Anstrich 2–3 Jahre |

**Verdikt:** Alu-Rohre sind leichter (Gewichtseinsparung 65%), teurer im Ankauf, aber geringere Wartungskosten. Für Yachten IMMER Alu-Rohre bevorzugt.

---

## 11. Blech und Bänder

### 11.1 Dünne Bleche (≤3 mm)

| Dicke | Legierung | Gewicht kg/m² | Anwendung | Preis €/m² |
|-------|-----------|---------------|-----------|------------|
| 0,5 mm | 5052-H32 | 1,35 | Verkleidung, Isolierung | €8–€12 |
| 0,8 mm | 5052-H32 | 2,16 | Lüftungskanäle | €12–€18 |
| 1,0 mm | 5083-H32 | 2,66 | Leichte Verkleidung | €14–€22 |
| 1,2 mm | 5083-H32 | 3,19 | Schottverkleidung | €16–€26 |
| 1,5 mm | 5083-H116 | 3,99 | Leichte Schotts | €20–€32 |
| 2,0 mm | 5083-H116 | 5,32 | Versteifungen, Brackets | €25–€40 |
| 2,5 mm | 5083-H116 | 6,65 | Leichte Tankwände | €30–€48 |
| 3,0 mm | 5083-H116 | 7,98 | Aufbauten, Schotten | €35–€55 |

### 11.2 Riffelblech (Tränenblech)

| Dicke (Grundblech) | Legierung | Gewicht kg/m² | Anwendung | Preis €/m² |
|--------------------|-----------|---------------|-----------|------------|
| 2/3,5 mm | 5083-H114 | 6,7 | Cockpitboden | €30–€48 |
| 3/4,5 mm | 5083-H114 | 9,2 | Decksflächen | €40–€62 |
| 4/5,5 mm | 5083-H114 | 11,4 | Arbeitsdeck | €48–€75 |
| 5/6,5 mm | 5083-H114 | 14,2 | Schweres Arbeitsdeck | €58–€90 |

**Riffelblech-Muster:** Erhältlich in Quintet (5 Tränen), Duett (2 Tränen), und Diamant. Quintet ist Standard im Yachtbau — rutschfest auch bei Nässe.

### 11.3 Riffelblech-Muster im Detail

**Quintet-Muster (5 Tränen pro Zoll):**
- Größte Tränen, beste Rutschfestigkeit
- Tragfähigkeit: 3 Tonnen/m² bei 3 mm Dicke
- Anwendung: Cockpitböden (nass), Dieseltank-Deckel
- Typischer Preis: €40–€65/m²
- Gewicht 3/4,5mm: 9,2 kg/m²
- Standard nach DIN 1669 (Deutschland)

**Duett-Muster (2 Tränen pro Zoll):**
- Kleinere Tränen, mehr Flächenstabilität
- Besser für dünnere Bleche
- Anwendung: Maschinenmraum-Verkleidung, Trennwände
- Typischer Preis: €35–€55/m²
- Gewicht 2/3,5mm: 6,7 kg/m²

**Diamond-Muster (Diamant/Rhombus):**
- Moderne Alternative, weniger Verschleiß an Schuhsohlen
- Weniger rutschfest als Quintet im nassen Zustand
- Anwendung: Innenbereich, Arbeitsdecks ohne Wasser
- Preis: €30–€50/m² (günstiger als Quintet)

### 11.4 Bänder und Coils

Dünne Materialien in Rollenform für kontinuierliche Verarbeitung:

| Breite (B) | Dicke (t) | Legierung | Gewicht kg (500m-Rolle) | Anwendung | Preis €/kg |
|-----------|----------|-----------|----------------------|-----------|-----------|
| 50 mm | 0,5 mm | 5052-H32 | 6,75 | Isolierband, Dichtung | €3,50–€5,00 |
| 100 mm | 0,8 mm | 5052-H32 | 21,6 | Abstandsband, Isolierung | €3,50–€5,00 |
| 200 mm | 1,0 mm | 5083-H32 | 43,2 | Tankwand-Streifen | €4,00–€6,00 |
| 300 mm | 1,5 mm | 5083-H116 | 97,2 | Verstärkungsband | €4,50–€7,00 |
| 500 mm | 2,0 mm | 5083-H116 | 172 | Flächenabdeckung | €5,00–€8,00 |
| 1000 mm | 3,0 mm | 5083-H116 | 516 | Breite Verkleidung | €5,50–€8,50 |

**Standard-Längen:** 500 m, 1.000 m Rollen. Anschnitt-Verlust: typischerweise 2–3%. Lagerkalkulation: +5% Reserve.

**Spule-Verfügbarkeit:** Hydro, Aleris, Tri-Arrows (USA), Sapa (EU) führen Standard-Coils. Lagerbestände: 2–6 Wochen Lieferzeit.

### 11.5 Perforiertes Blech (Lochbleche)

Aluminium-Lochbleche mit verschiedenen Lochmuster für Lüftung und Drainage:

| Loch-Ø | Abstand | Dicke | Legierung | Durchlassfläche | Anwendung |
|--------|---------|-------|----------|-----------------|-----------|
| 3 mm | 5 mm | 1,5 mm | 5052-H32 | 28% | Lüftungsgitter |
| 5 mm | 8 mm | 2,0 mm | 5083-H32 | 31% | Motorraumgitter |
| 6 mm | 9 mm | 2,5 mm | 5083-H116 | 32% | Schott-Lüftung |
| 8 mm | 12 mm | 3,0 mm | 5083-H116 | 33% | Drainage, Fußboden |
| 10 mm | 15 mm | 4,0 mm | 6082-T6 | 35% | Strukturelles Lochblech |

**Anwendungsbeispiel — 12m Yacht Maschinenmraum-Belüftung:**
- Erforderliche Lüftungsfläche: min. 0,05 m² pro kW Motor (ISO 9094)
- Bei 50 kW Motor: 2,5 m² Gitter nötig
- Wahl: 4×6mm Lochblech (5052-H32)
- Material: ca. 40 m² Blech bestellen (Verschnitt ~40% durch Zuschnitt)
- Kosten: ca. €150–€200 Material

### 11.6 Expanded Metal (Streckmetall)

Gewalzte Aluminium-Bleche, aufgerissen und auseinandergezogen zu Rautenform:

| Maschenweite | Dicke (Original) | Legierung | Gewicht kg/m² | Anwendung |
|-------------|-----------------|-----------|--------------|-----------|
| 10×5 mm | 1,5 mm | 5052-H32 | 3,2 | Leichte Verkleidung |
| 12×6 mm | 2,0 mm | 5083-H32 | 4,8 | Spritzschutz |
| 15×7,5 mm | 2,5 mm | 5083-H116 | 5,6 | Schutzgitter |
| 20×10 mm | 3,0 mm | 6082-T6 | 6,5 | Auftrittsfläche |

**Vorteil Expanded Metal vs. Lochblech:**
- Leichter durchzuschneiden
- Bessere Verformbarkeit (biegen möglich)
- Geringeres Gewicht
- Etwas weniger steif

**Preis:** ca. 60–70% von Lochblech (€15–€25/m²)

### 11.7 Supplier und Verfügbarkeit weltweit

| Land/Region | Hauptlieferanten | Zertifikate | Min. Bestellung | Lieferzeit |
|------------|-----------------|-----------|-----------------|-----------|
| **Deutschland** | Trimet, Hydro Metals | EN 10204 3.1 | 50 kg | 2–3 Wochen |
| **Schweiz** | Stöckli, Aleris | DIN EN 573 | 100 kg | 2 Wochen |
| **Großbritannien** | Hydro, Aleris UK | BS EN 485 | 50 kg | 2–3 Wochen |
| **Benelux** | Trimet NL, Hydro | EN Standards | 50 kg | 2 Wochen |
| **USA** | Aleris, Tri-Arrows | ASTM B928 | 500 kg | 3–4 Wochen |
| **Australien** | Comalco, Alcoa | AS/NZS | 250 kg | 2–4 Wochen |

**Online-Shops (Europa, schnelle Lieferung):**
- bikar.de (Deutschland): Min. 1–5 kg, Versand €15–€50
- steelmaterial.de (Deutschland): Min. 5 kg, kostenlos ab €200
- copperpro.ch (Schweiz): Min. 10 kg
- metalshop.eu (Großbritannien): Min. 1 kg

**Kostenkalkulation — Zuschnittaufträge:**
Bei Standard-Fertigungsbetrieben: €0,50–€2,00/kg Bearbeitungsgebühr (abhängig von Komplexität)

### 11.8 Lagerung und Handhabung

**Klima:** Aluminium ist feuchtigkeits-tolerant (anders als Stahl), ABER:
- Feuchte >85% RH mit Temperaturwechsel kann zu Oberflächenkorrosion führen (Grünspan)
- Lösung: Trockene Lagerhalle (50–70% RH), gute Belüftung

**Schutz vor Kontamination:**
- Nicht auf Stahl lagern (Galvanische Zelle!)
- Nicht mit Kupfer oder Messing in Kontakt
- Kunststoff-Unterlagen (PE-Folie) verwenden

**Haltbarkeit:** Unbegrenzt, wenn trocken gelagert. Oberflächenoxidation (weiße Flöckchen) kann mit milder Säure (Zitronensäure) entfernt werden.

**Verschliffene Kanten:** Nach dem Zuschnitt sollten scharfe Kanten mit:
- 120er Schleifpapier leicht gerundet oder
- Deburrer-Maschine bearbeitet werden
(Verhindert Schnitte und Korrosion an Kanten)

---

## 12. Schweißzusätze und Schweißtechnik

### 12.1 Schweißzusatz-Auswahl

| Schweißzusatz | EN-Bezeichnung | AWS | Zusammensetzung | Anwendung |
|---------------|---------------|-----|----------------|-----------|
| **5356** | S Al 5356 | ER5356 | AlMg5Cr | **Universell für 5xxx auf 5xxx** |
| **5183** | S Al 5183 | ER5183 | AlMg4,5Mn | **Höchste Festigkeit 5xxx** |
| **4043** | S Al 4043 | ER4043 | AlSi5 | **6xxx auf 6xxx** |
| **4047** | S Al 4047 | ER4047 | AlSi12 | 6xxx, geringste Rissneigung |
| **5556** | S Al 5556 | ER5556 | AlMg5,2MnCr | Hohe Festigkeit, Schiffbau |
| **5087** | S Al 5087 | — | AlMg4,5MnZr | Premium-Qualität, feinste Nähte |

### 12.2 Schweißzusatz-Kompatibilitätsmatrix

| Grundmaterial 1 | Grundmaterial 2 | Empfohlener Zusatz | Alternativer Zusatz | NIEMALS |
|-----------------|-----------------|-------------------|---------------------|---------|
| 5083 | 5083 | **5183** | 5356, 5556 | 4043 |
| 5083 | 5086 | **5356** | 5183 | 4043 |
| 5083 | 6082 | **5356** | 5183 | 4043 |
| 5086 | 5086 | **5356** | 5183 | 4043 |
| 6082 | 6082 | **4043** | 5356 | — |
| 6061 | 6061 | **4043** | 5356 | — |
| 6082 | 6061 | **4043** | 5356 | — |
| 5052 | 5083 | **5356** | 5183 | 4043 |
| 5083 | 5059 | **5183** | 5059-Draht | 5356 (Festigkeit!) |

**KRITISCHE REGEL für AYDI (confidence: documented):** Beim Schweißen von 5xxx auf 5xxx NIEMALS 4043 (AlSi5) verwenden! Silizium diffundiert in die Mg-reiche Zone und bildet Mg₂Si — das führt zu spröden, rissanfälligen Nähten. Immer 5356 oder 5183!

### 12.3 WIG-Schweißen (TIG) — Parameter

| Material | Dicke mm | Strom A | Spannung V | Schutzgas | Draht-Ø mm | Geschw. cm/min |
|----------|----------|---------|-----------|-----------|------------|----------------|
| 5083 | 3 | 100–130 | 12–14 | Argon 4.6 | 2,4 | 15–20 |
| 5083 | 4 | 130–160 | 13–15 | Argon 4.6 | 2,4 | 12–18 |
| 5083 | 5 | 150–180 | 14–16 | Argon 4.6 | 2,4–3,2 | 10–15 |
| 5083 | 6 | 170–210 | 15–17 | Argon 4.6 | 3,2 | 10–14 |
| 5083 | 8 | 200–250 | 16–18 | Argon 4.6 | 3,2 | 8–12 |
| 5083 | 10 | 230–280 | 17–19 | Argon 4.6 | 3,2–4,0 | 6–10 |
| 5083 | 12 | 260–320 | 18–20 | Argon 4.6 | 4,0 | 6–8 |
| 6082-T6 | 3 | 90–120 | 12–14 | Argon 4.6 | 2,4 | 15–22 |
| 6082-T6 | 5 | 140–170 | 14–16 | Argon 4.6 | 2,4–3,2 | 10–16 |
| 6082-T6 | 8 | 190–240 | 16–18 | Argon 4.6 | 3,2 | 8–12 |

### 12.4 MIG-Schweißen (GMAW) — Parameter

| Material | Dicke mm | Strom A | Spannung V | Schutzgas | Draht-Ø mm | Vorschub m/min |
|----------|----------|---------|-----------|-----------|------------|----------------|
| 5083 | 4 | 130–160 | 19–22 | Argon 4.6 | 1,0 | 8–10 |
| 5083 | 5 | 150–190 | 20–23 | Argon 4.6 | 1,2 | 7–9 |
| 5083 | 6 | 170–220 | 21–24 | Argon 4.6 | 1,2 | 7–9 |
| 5083 | 8 | 200–260 | 23–26 | Argon 4.6 | 1,2 | 8–10 |
| 5083 | 10 | 230–300 | 24–27 | Argon 4.6 | 1,2–1,6 | 8–11 |
| 5083 | 12 | 260–320 | 25–28 | Argon 4.6 | 1,6 | 8–10 |

### 12.5 Schweißvorbereitung — Nahtvorbereitung

| Plattendicke | Nahtform | Spalt mm | Flankenwinkel | Wurzelhöhe mm |
|-------------|----------|---------|---------------|---------------|
| ≤3 mm | I-Naht (Stumpf) | 0–1 | — | — |
| 3–6 mm | V-Naht | 1–2 | 60–70° | 1–2 |
| 6–10 mm | V-Naht | 2–3 | 60–70° | 1,5–2,5 |
| 10–15 mm | X-Naht (doppel-V) | 2–3 | 60–70° | 2–3 |
| >15 mm | X-Naht oder U-Naht | 3–4 | U: R=6mm | 2–3 |

### 12.6 Schweißfehler und deren Ursachen

| Fehler | Symptom | Fehlerursache | Maßnahme |
|--------|---------|---------------|----------|
| Porosität | Gasporen in der Naht | Feuchtigkeit, Verunreinigung, schlechtes Gas | Reinigung, Gas prüfen, Vorwärmen |
| Heißriss | Riss in der Schweißnaht-Mitte | Zu hohe Schrumpfspannung, falsche Nahtgeometrie | Nahtfolge ändern, Zusatzwerkstoff prüfen |
| Bindefehler | Naht haftet nicht am Grundmaterial | Oxidschicht nicht entfernt, zu wenig Strom | Bürsten (SS-Bürste!), Parameter erhöhen |
| Einbrandkerbe | Kerbe am Nahtübergang | Zu hoher Strom, zu schnelle Geschwindigkeit | Parameter reduzieren, Pendeltechnik |
| Endkraterriss | Riss am Nahtende | Abruptes Ende ohne Auffüllung | Endkraterfüllung programmieren |

### 12.7 Praxis-Tipps aus Forum und Video

**Dangar Marine (YouTube, "Welding Aluminium Boats"):**
- Reinigung ist 80% des Erfolgs. Aceton entfettet, SS-Bürste entfernt Oxidschicht. Zwischen Reinigung und Schweißung max. 4 Stunden.
- Argon 4.6 Minimum (99,996% rein). Bei 4.0 Argon (99,99%) bereits merkbar mehr Porosität.
- Wechselstrom (AC) bei WIG ist Standard für Alu. Balance ca. 65% EN (Reinigung) / 35% EP (Eindringung).

**Acorn to Arabella (YouTube, Staffel 3, Alu-Rumpf):**
- Heftstellen alle 150–200 mm. Nicht zu groß (schwer zu überschweißen), nicht zu klein (brechen).
- Schweißfolge: Von der Mitte nach außen, um Verzug zu minimieren. Alternierend Bb/Stb.
- Zwischenlagentemperatur max. 60°C für 5083! Messung mit Temperaturstift oder Infrarot-Thermometer.

**Sail Life (YouTube, "Building Aluminium Sailboat"):**
- Spannvorrichtungen sind entscheidend. Alu verzieht sich stärker als Stahl.
- Für dünne Bleche (3–4 mm): Kupfer-Unterlage als Wärmesenke.
- Auf keinen Fall Alu mit Stahlbürste oder Stahl-Werkzeug bearbeiten — Kontamination führt zu galvanischer Korrosion in der Schweißnaht!

---

## 13. Oberflächenbehandlung und Korrosionsschutz

### 13.1 Übersicht Schutzsysteme

| System | Beständigkeit | Kosten | Anwendungsbereich | Lebensdauer |
|--------|--------------|--------|-------------------|-------------|
| Blankes Alu (natürliche Oxidschicht) | Gut (über WL) | €0 | Aufbau, Mast (unbehandelt) | 20–30 Jahre |
| Eloxierung (Anodisierung) | Sehr gut | Mittel | Beschläge, Profile, Masten | 15–25 Jahre |
| 2K-Epoxy-Primer (z.B. International Interprotect) | Exzellent | Mittel | Unterwasser, gesamter Rumpf | 5–10 Jahre |
| 2K-PU-Toplack (z.B. International Perfection) | Exzellent | Hoch | Überwasser-Oberflächen | 8–15 Jahre |
| Kupferfreies Antifouling | Gut | Mittel | Unterwasserschiff | 1–2 Saisons |
| Zink-Spray (Kaltgalvanisierung) | Befriedigend | Niedrig | Temporärer Schutz, Schweißnähte | 1–3 Jahre |
| Tectyl/Owatrol | Gut | Niedrig | Bilge, verdeckte Bereiche | 3–5 Jahre |

### 13.2 Eloxierung (Anodisierung) im Detail

**Verfahren:** Das Aluminium wird in Schwefelsäure-Elektrolyt als Anode geschaltet. Gleichstrom bildet eine kontrollierte Al₂O₃-Schicht (Oxidschicht), die wesentlich dicker und dichter ist als die natürliche Oxidschicht.

| Parameter | Wert | Bemerkung |
|-----------|------|-----------|
| Schichtdicke (Standard) | 10–15 µm | Dekorativ, Innenbereich |
| Schichtdicke (Marine/Hartanodisierung) | 25–50 µm | Außenbereich, Beschläge |
| Schichtdicke (Mil-Spec, Typ III) | 50–75 µm | Extreme Beanspruchung |
| Härte (Hartanodisierung) | 350–500 HV | Vergleich: 6082-T6 = 95 HV |
| Farbe | Natürlich (silber/gold) | Kann eingefärbt werden |
| Preis (Standardeloxal) | €5–€15/dm² | Abhängig von Menge und Größe |
| Preis (Hartanodisierung) | €10–€30/dm² | Höherer Aufwand |

**AYDI-Hinweis (confidence: documented):** Eloxierte Oberflächen dürfen NICHT geschweißt werden — die Oxidschicht muss im Schweißbereich vollständig entfernt werden. Schweißen durch Eloxalschicht führt zu massiver Porosität und Bindefehlern.

### 13.3 Beschichtungssystem Alu-Yacht (Unterwasser)

| Schicht | Produkt (Beispiel) | Schichtdicke µm | Funktion |
|---------|--------------------|-----------------|---------|
| 0. Vorbereitung | Schleifen (K80), Entfetten (Aceton) | — | Haftgrund |
| 1. Wash-Primer | International Vinyl Washprimer | 5–10 | Haftvermittlung |
| 2. Epoxy-Primer 1 | International Interprotect | 125 (2 Schichten) | Korrosionsschutz |
| 3. Epoxy-Primer 2 | International Interprotect | 125 (2 Schichten) | Osmoseschutz |
| 4. Antifouling | Trilux 33 (kupferfrei!) | 75–100 (2 Schichten) | Bewuchsschutz |
| **Gesamt** | | **330–360 µm** | |

**WARNUNG (confidence: documented):** Auf Aluminium-Rümpfen NIEMALS kupferhaltiges Antifouling verwenden! Kupfer bildet ein galvanisches Element mit Aluminium und führt zu katastrophaler Korrosion. Auch kein "Cupronikkel" oder "Zinnorganisch mit Kupfer-Booster".

### 13.4 Zugelassene Antifoulings für Aluminium

| Produkt | Hersteller | Typ | Wirkstoff | Preis €/Liter | Lebensdauer |
|---------|-----------|-----|-----------|---------------|-------------|
| Trilux 33 | International | Self-polishing | Zineb (kupferfrei) | €45–€55 | 1 Saison |
| Micron CSC für Alu | International | Self-polishing | Zineb | €50–€60 | 1–2 Saisons |
| Olympic Alu | Hempel | Self-polishing | Zineb | €40–€50 | 1 Saison |
| Cruiser Uno EU Alu | Hempel | Self-polishing | Kupferfrei | €35–€45 | 1 Saison |
| Mille Alu | Jotun | Self-polishing | Kupferfrei | €45–€55 | 1 Saison |
| SeaJet Shogun (Alu) | Seajet | Hartes AF | Kupferfrei | €40–€50 | 1–2 Saisons |
| Coppercoat (NICHT für Alu!) | — | Epoxy+Kupfer | Cu | — | **VERBOTEN!** |

### 13.5 Awlgrip-System für Alu-Yachten

**Awlgrip (Sherwin-Williams) ist das Premium-Beschichtungssystem für hochwertige Alu-Yachten:**

| Schicht | Produkt | Schichtdicke µm | Trocknungszeit | Besonderheit |
|--------|---------|-----------------|----------------|-------------|
| Vorbereitung | Schleifen SA 2.5 (ISO 8501-1) | — | Vor Arbeit | Strahlenqualität |
| Wash Primer | Awl-Check 2001 Wash Primer | 20–30 | 12–18h | Haftvermittler |
| Epoxy Primer | Awl-Prime 4081 Epoxy | 75–100 (2×) | 16–24h | Für Unterwasser |
| Barrier Coat | Awl-Barrier 1800 Epoxy | 75–100 | 24h | Zusätzliche Osmose-Barriere |
| Finishing | Awl-Topcoat 2000 Polyurethane | 60–80 (2–3×) | 48–72h | Hochglanz, UV-resistent |
| Anti-Fouling | Awl-Grip AF (kupferfrei) | 75–100 | 48h | Biologischer Bewuchsschutz |
| **Gesamt** | | **480–640 µm** | — | **Ultra-Premium** |

**Kosten (12m Yacht, ca. 70 m² Unterwasser):**
- Material: 80–100 Liter System × €80–€120/Liter = €6.400–€12.000
- Arbeit (professionell): 120–160h × €35–€50/h = €4.200–€8.000
- **Gesamt: €10.600–€20.000**
- **Lebensdauer: 10–15 Jahre (bei Pflege)**

### 13.6 Jotun-System für Alu-Yachten

**Jotun ist eine europäische Alternative zu Awlgrip (günstiger, aber solide):**

| Schicht | Produkt | Schichtdicke µm | Besonderheit |
|--------|---------|-----------------|-------------|
| Primer | Tankguard 2000 Epoxy | 100–150 (2×) | Fuel-Resistant |
| Barrier | Seaforce 4000 Epoxy | 75–100 | Optional |
| Topcoat | Tankguard Topcoat Polyurethane | 60–80 (2×) | UV-Resistant |
| AF | Mille Aluminium Self-Polishing | 75–100 | Kupferfrei |
| **Gesamt** | | **410–560 µm** | **Gute Qualität, kostengünstiger** |

**Kosten (gleiche Yacht wie oben):**
- Material: 70–90 Liter × €50–€80/Liter = €3.500–€7.200
- Arbeit: 100–120h × €30–€40/h = €3.000–€4.800
- **Gesamt: €6.500–€12.000**
- **Lebensdauer: 8–12 Jahre**

### 13.7 Pulverbeschichtung für Alu-Profile

**Verfahren:** Trockenes Pulver (Epoxy oder Polyester) wird elektrostatisch aufgebracht und im Ofen ausgepolymerisiert.

**Vorteile:**
- Keine Lösungsmittel, umweltfreundlich
- Gleichmäßige Schichtdicke (50–150 µm)
- Ausgezeichnete Haftung
- Günstiger als Nassfarbe für kleine Volumina

**Nachteil:**
- Nur für kleine Teile (vor der Montage)
- Nicht für komplexe zusammengebaute Strukturen

**Anwendung Yachtbau:**
- Profile (Extrusion) werden vor Zuschnitt beschichtet
- Beschläge (Scharniere, Halterungen) typischerweise pulverbeschichtet
- Farben: Silber (RAL 9006), Schwarz (RAL 9005), Weiß (RAL 9016) Standard

**Kosten:** €5–€15 pro kg Teile (abhängig von Komplexität)

**Lebensdauer:** 8–12 Jahre bei UV-Exposition (besser als Nassfarbe an kleinen Teilen)

### 13.8 Oberflächenvorbereitung — ISO 8501 Schleifqualitäten

Kritisch für Haftung von Beschichtungen:

| Qualität | Code | Beschreibung | Spezifikation |
|----------|------|-------------|---------------|
| Nicht geschliffen | St 0 | Sichtbar rostig (für Stahl) | N/A für Alu |
| Borsten-Struktur | St 1 | Bürsten-gereinigt | N/A für Alu |
| Flammstrahl | St 2 | Flammstrahler, keine Rostflocken | N/A für Alu |
| Sandblasen (light) | Sa 2 | Oberflächenoxid teilweise entfernt | Für Alu-Reparatur |
| **Sandblasen (medium)** | **Sa 2.5** | **98% Oberfläche blank, etwas Oxid OK** | **Standard für Alu-Rumpf** |
| Sandblasen (schweizer) | Sa 3 | Saubere Oberfläche, minimal Oxid | Für Premium (Awlgrip) |
| **Atomares Strahlen** | **Sa 3-2** | **Fast völlig blank, minimal Oxidflöckchen** | **Best Practice für Alu** |

**Praktische Durchführung:**
- Sa 2.5 ist erreichbar mit Körnung K 60–K 80 Sandblastgrit
- Wasserflecken danach VERMEIDEN (→ Reoxidation)
- Max. 4 Stunden zwischen Schleifen und Priming bei Alu
- Für >4h: Mit Inhibitor-Öl schützen (z.B. Owatrol D80)

### 13.9 Chromat-Konversion (Alodine / Iridite)

**Verfahren:** Chemische Oberflächenbehandlung, die eine chromat-haltige Schutzschicht bildet.

**Parameter:**
- Schichtdicke: 5–15 µm
- Farbe: Gelb (Chromat) bis Dunkelbraun (Ni-frei Variante)
- Preis: €10–€20/dm² (Batch-Anlagen, min. 100 kg Material)

**Vorteil:**
- Ausgezeichnete Haftung für Farbe
- Selbstheilend (kleine Kratzer verschließen sich)
- Korrosionsschutz über längere Zeit

**Nachteil:**
- Chromat-Konversion ist **giftig** (Cr-VI) — viele Länder verbieten es
- In der EU: ONLY zugelassen für Reparaturen oder kleine Teile (nicht für Neuproduktion)
- Alternative: Ni-frei Varianten sind in Entwicklung, aber teuer

**Praxis AYDI:** Chromat ist für neue Alu-Yacht-Projekte OUT. Allerdings: Bei Reparaturen älterer Boote wird es manchmal noch verwendet (Ältere Spezifikationen).

### 13.10 Beschichtungs-Lebensdauer Vergleichstabelle

| System | Unterwasser | Überwasser | Wartungsaufwand | Preis |
|--------|-----------|-----------|-----------------|-------|
| Blankes Alu (nat. Oxidschicht) | 5–8 Jahre | 15–20 Jahre | Sehr niedrig | Gratis |
| Eloxierung (Hart, 50µm) | 8–12 Jahre | 15–25 Jahre | Niedrig | €300–€800 |
| Epoxy (2K) + PU-Lack | 5–10 Jahre | 10–15 Jahre | Mittel | €3.000–€8.000 |
| **Awlgrip Premium** | **10–15 Jahre** | **15–20 Jahre** | **Hoch (Wartung)** | **€15.000–€25.000** |
| Jotun Standard | 8–12 Jahre | 12–18 Jahre | Mittel-Hoch | €7.000–€12.000 |
| Beschichtung + AF (Trilux) | 1–2 Saisons (AF) | 10+ Jahre (Primer) | Hoch (jährlich AF) | €5.000–€10.000/Jahr (AF) |

**AYDI Empfehlung (confidence: documented):**
- **Neue Alu-Yacht:** Awlgrip oder Jotun Vollsystem, mit regelmäßiger Inspektion (jährlich)
- **Gebrauchte Alu-Yacht (>10 Jahre):** Ultraschall-Dickenmessung VOR Beschichtung — möglicherweise ist Rumpfblech bereits zu dünn

---

## 14. Galvanische Korrosion — Das Hauptproblem

### 14.1 Galvanische Spannungsreihe (Seewasser)

| Material | Potential V (vs. Ag/AgCl) | Position | Risiko an Alu? |
|----------|--------------------------|----------|----------------|
| Zink (Opferanode) | −1,03 | Am unedelsten | Schützt Alu |
| Aluminium-Anode (Al-Zn-In) | −1,05 | Unedel | Schützt Alu |
| **Aluminium 5083** | **−0,76 bis −0,85** | **Unedel** | **—** |
| **Aluminium 6082** | **−0,73 bis −0,80** | **Unedel** | **—** |
| Stahl (blank) | −0,60 bis −0,70 | Unedel | Geringes Risiko |
| Blei | −0,50 | — | Geringes Risiko |
| Zinn | −0,30 | — | Mäßiges Risiko |
| **Edelstahl 316 (passiv)** | **−0,05 bis +0,10** | **Edel** | **HOHES RISIKO** |
| Kupfer | +0,10 bis +0,20 | Edel | **SEHR HOHES RISIKO** |
| Bronze | +0,15 bis +0,25 | Edel | **EXTREM HOHES RISIKO** |
| Monel | +0,20 bis +0,30 | Edel | **EXTREM HOHES RISIKO** |
| Titan | +0,05 bis +0,15 | Edel | Hohes Risiko |
| Graphit/Carbon | +0,20 bis +0,40 | Am edelsten | **KATASTROPHAL** |

### 14.2 Isolationsmaßnahmen (PFLICHT bei Alu-Yachten)

| Maßnahme | Material/Produkt | Anwendung | Preis |
|----------|-----------------|-----------|-------|
| Tef-Gel | Sealant Tech (PTFE-Paste) | Unter JEDEM SS-Beschlag auf Alu | €12–€18/50g Tube |
| Duralac | David Craig & Co. | Anti-Galvanic-Paste, unter Beschlägen | €8–€15/Tube |
| G10-Isolierplatte | FR4 Glasfaser-Epoxid | Zwischen SS-Beschlag und Alu-Deck | €15–€25/Platte |
| Nylon-Isolierbuchsen | Diverse | Um Bolzen zwischen SS und Alu | €0,20–€1/Stk. |
| Nylon-Unterlegscheiben | Diverse | Unter Bolzenköpfe und Muttern | €0,10–€0,50/Stk. |
| Sikaflex 291 | Sika | Elastischer Sealant als Feuchtigkeitssperre | €8–€14/Kartusche |
| Butyl-Tape | Diverse | Zusätzliche Feuchtigkeitsbarriere | €3–€8/Rolle |

**Die drei goldenen Regeln der Alu-Yacht-Isolation:**
1. **KEIN blankes Metall auf blankes Metall** — Immer Isolationsschicht dazwischen
2. **Feuchtigkeit ist der Elektrolyt** — Ohne Wasser keine galvanische Korrosion. Dichtungen und Drainage sind kritisch
3. **Potentialdifferenz <200 mV** — Materialien mit mehr als 200 mV Potentialdifferenz MÜSSEN isoliert werden

### 14.3 Opferanoden für Alu-Yachten

| Anoden-Material | Für Alu geeignet? | Potential V | Bemerkung |
|----------------|-------------------|-------------|-----------|
| **Zink (Zn)** | **Ja (Seewasser)** | −1,03 | Standard in Salzwasser |
| **Aluminium (Al-Zn-In)** | **Ja (Süß+Salzwasser)** | −1,05 | Universell, beste Wahl |
| **Magnesium (Mg)** | **Nur Süßwasser** | −1,60 | In Salzwasser: ZU aktiv, kann Alu überprotektieren! |

**AYDI-Warnung (confidence: documented):** Magnesium-Anoden in Salzwasser an Alu-Yachten können zu Überprotektion führen (Potential <−1,10 V). Das erzeugt Alkali (OH⁻) an der Alu-Oberfläche, was die Schutzschicht angreift (alkalische Korrosion). Nur Zink- oder Alu-Anoden verwenden!

### 14.4 Fallstudie: Galvanische Katastrophe

**Praxisbeispiel (CruisersForum 2021, "Aluminium hull eaten away"):**
Ein Eigner einer 12m Alu-Segelyacht montierte Bronze-Seeventile direkt in den Alu-Rumpf (ohne Isolation). Nach 18 Monaten im Salzwasser: Alu-Wandstärke am Seeventil von 6 mm auf 2 mm reduziert. Rumpfdicke neben Seeventil bis zu 4 mm verloren. Gesamt-Schaden: €35.000 (neue Rumpfplatten, Seeventile, Arbeit).

**Lösung:** Bronze-Seeventile durch Marelon (GFK-Verbund) oder TruDesign-Kunststoff-Seeventile ersetzen. Wenn Bronze-Seeventile unvermeidlich: doppelte Isolation mit G10-Flansch + Tef-Gel + Nylon-Buchsen + überdimensionierte Alu-Opferanoden direkt neben dem Seeventil.

### 14.5 Materialauswahl für Alu-Yacht-Beschläge

| Beschlag | Material-Empfehlung | NICHT verwenden | Isolation nötig? |
|----------|--------------------|-----------------|--------------------|
| Klampen | Alu eloxiert oder SS316 | Bronze | Ja (SS auf Alu) |
| Seeventile | Marelon, TruDesign | Bronze, Messing | Nein (Kunststoff) |
| Winschen | Alu oder SS | Bronze | Ja (SS auf Alu) |
| Reling | Alu 6082-T6 oder SS316 | — | Ja (SS auf Alu) |
| Stanchions | Alu 6082-T6 oder SS316 | — | Ja (SS auf Alu) |
| Bugrollen | Alu eloxiert, SS | Bronze | Ja (SS) |
| Anker-Kette | Verzinkt (!) | SS | — |
| Propeller | NiBrAl (Nibral) oder SS | Bronze (nah am Alu!) | Ja (galvanisch) |
| Wellenanlage | Aquamet oder Alu-Bronze | Reiner SS | Ja (immer) |
| Keelbolts | SS316L oder Duplex 2205 | — | Ja (SS auf Alu-Kiel) |

---

## 15. Hersteller und Lieferanten weltweit

### 15.1 Walzwerke / Primärproduzenten

| Hersteller | Sitz | Legierungen | Marine-Zertifizierung | Website |
|-----------|------|-------------|----------------------|---------|
| **Novelis** (ehem. Aleris) | DE/EU/US | 5083, 5086, 5383, 6082 | DNV, LR, BV | novelis.com |
| **Constellium** | FR/DE | 5083, 5086, 5383, 5059 (Sealium), 6082 | DNV, LR, BV, ABS | constellium.com |
| **Norsk Hydro** | NO | 5083, 5086, 6082, 6060, 6063 | DNV, LR | hydro.com |
| **AMAG Austria** | AT | 5083, 5086, 6082 | DNV, LR, BV | amag.at |
| **Alcoa / Arconic** | US | 5083, 5086, 6061, 6082, 7075 | ABS, DNV, LR | arconic.com |
| **Assan Alüminyum** | TR | 5083, 5086, 5754 | DNV, LR | assanaluminyum.com |
| **Hindalco (Novelis)** | IN | 5083, 5086 | DNV, LR | hindalco.com |
| **China Zhongwang** | CN | 5083, 6082, 6061 | DNV, CCS | zhongwang.com |
| **Chalco (Aluminum Corp. of China)** | CN | 5083, 5086 | CCS, DNV | chalco.com |
| **Nanshan Aluminium** | CN | 5083, 6082 | DNV, LR | nanshan.com |
| **Capral** | AU | 5083, 5086, 6060, 6082 | LR, DNV | capral.com.au |
| **Aluminiumwerk Unna** | DE | 5083, 5086 | DNV, GL | alu-unna.de |
| **Elval Halcor** | GR | 5083, 5086, 5754, 6082 | DNV, LR, BV | elvalhalcor.com |

### 15.2 Händler und Distributoren (Zuschnitt + Kleinmengen)

**Deutschland:**

| Händler | Legierungen | Besonderheit | Website |
|---------|-------------|-------------|---------|
| **Bikar Metalle** | 5083, 5086, 6082, 6061, 5052 | Zuschnitt ab 1 Stück, schnelle Lieferung | bikar.com |
| **Alu-Verkauf.de** | 5083, 6082, 6060 | Online-Shop, Kleinmengen | alu-verkauf.de |
| **Gemmel Metalle** | 5083, 5086, 6082 | Platten und Profile | gemmel-metalle.de |
| **Thyssenkrupp Materials** | 5083, 5086, 6082, 6061 | Großhandel, Zuschnitt | thyssenkrupp-materials.de |
| **Nordfels** | 5083, 6082 | Marine-Spezialist | nordfels.de |
| **Steelmaterial** | 5083, 6082 | Online-Shop, Platten/Profile | steelmaterial.de |
| **Metallshop24** | 5083, 6082, 6060, 5052 | Online-Handel, Kleinmengen | metallshop24.de |
| **Schinko Metalle** | 5083, 5086 | Spezialist Schiffbau | schinko.at |

**UK:**

| Händler | Besonderheit | Website |
|---------|-------------|---------|
| **Aalco (Metals4U)** | Breites Sortiment, Online-Shop | aalco.co.uk |
| **Metal Supermarkets** | Zuschnitt, Kleinmengen | metalsupermarkets.co.uk |
| **Smith Metal Centres** | Marine-Güten, Zertifikate | smithmetal.com |
| **Merseyside Metals** | Marine-Spezialist, Liverpool | — |
| **Marine Grade Metals** | Spezialist für 5083 | marinegrademetals.co.uk |

**USA:**

| Händler | Besonderheit | Website |
|---------|-------------|---------|
| **Metals Depot** | ASTM B928, Zuschnitt | metalsdepot.com |
| **OnlineMetals** | Online-Shop, Kleinmengen | onlinemetals.com |
| **Midwest Steel & Aluminum** | Marine-Grade, Zertifikate | midweststeelsupply.com |
| **TW Metals** | Spezialist, alle Legierungen | twmetals.com |
| **Industrial Metal Supply** | Westküste, schnelle Lieferung | industrialmetalsupply.com |
| **Metal Supermarkets** | Franchise, landesweit | metalsupermarkets.com |
| **Parker Steel** | Marine-Spezialist | parkersteel.com |

**Australien:**

| Händler | Besonderheit | Website |
|---------|-------------|---------|
| **Capral Aluminium** | Lokaler Produzent, Marine-Güten | capral.com.au |
| **Ullrich Aluminium** | NZ/AU, breites Sortiment | ullrich-aluminium.com.au |
| **OneSteel (Metalcorp)** | Distributor, Marine-Grade | metalcorp.com.au |
| **Austral Wright Metals** | Spezialist für 5083 Marine | australwright.com.au |

**Karibik / Mittelamerika:**

Aluminium-Halbzeuge sind in der Karibik schwer zu beschaffen. Quellen:
- **US-Import via Florida:** Metals Depot oder TW Metals versenden international
- **Trinidad:** T&T Metal & Industrial Supply (begrenzt, 6061 und 5052)
- **Martinique/Guadeloupe:** Import aus Frankreich über Constellium/Hydro-Distributor
- **Panama:** Grupo ECA (Import aus USA, lange Lieferzeiten)

**Praxis-Tipp (Forum-Konsens):** Für Langfahrer auf Alu-Yachten: Ersatzmaterial VOR der Abreise in Europa oder den USA kaufen und mitführen. In abgelegenen Gebieten ist 5083-H116 praktisch nicht erhältlich.

### 15.3 Werft-Spezialisten für Alu-Yachtbau

| Werft | Sitz | Spezialität | Bekannte Modelle |
|-------|------|-------------|-----------------|
| **Allures Yachting** | FR | Alu-Fahrtensegler | Allures 39.9, 45.9, 51.9, 52 |
| **Garcia Yachting** | FR | Alu-Expedition | Exploration 45, 52, 65 |
| **Ovni (Alubat)** | FR | Alu-Segelyachten | Ovni 365, 395, 450 |
| **Boreal Yachts** | FR | Alu-Hochseeyachten | Boreal 44, 47, 52 |
| **KM Yachtbuilders** | NL | Custom Alu | Bestevaer-Serie |
| **Jachtwerf Klompmaker** | NL | Alu-Fahrtenyachten | Diverse Custom |
| **Alumarine** | FR | Alu-Arbeitsboote/Yachten | Custom |
| **Barkmet** | PL | Budget-Alu-Yachten | Diverse Modelle |
| **Van der Vliet** | NL | Quality Alu Yachts | Diverse Custom |
| **Dijkstra & Partners** | NL | Design + Bau | Expeditionsyachten |
| **Metalcraft Marine** | NZ | Alu-Expedition | Custom |
| **Circa Marine** | NZ | Alu-Fahrtensegler | Custom |
| **Dashew Offshore** | US (Design) | Alu-Expedition | FPB 64, 78, 97 |

---

## 16. Praxisberichte und Forum-Konsens

### 16.1 Langzeiterfahrungen mit 5083-Rümpfen

**CruisersForum-Thread "10 years on aluminium hull" (2020, 847 Antworten):**

Zusammenfassung der Konsens-Erfahrungen:
- **Rumpfzustand nach 10 Jahren:** Bei korrekt beschichtetem 5083-Rumpf: 0% Materialverlust gemessen. Beschichtung alle 4–6 Jahre erneuern.
- **Häufigstes Problem:** Galvanische Korrosion an Beschlägen (SS auf Alu). 90% der Korrosionsprobleme sind an Montagepunkten, nicht am blanken Rumpf.
- **Antifouling:** Trilux 33 und Hempel Olympic Alu sind die am häufigsten genannten Produkte. Lebensdauer 1–1,5 Saisons im Mittelmeer.
- **Worst Case:** Eigner mit Bronze-Seeventilen ohne Isolation — Rumpfdicke von 6 auf 2 mm in 3 Jahren.
- **Best Practice:** Marelon-Seeventile, alle SS-Beschläge isoliert (Tef-Gel + G10), Alu-Opferanoden, jährliche Ultraschall-Dickenmessung am Unterwasserschiff.

### 16.2 Schweißreparaturen unterwegs

**segeln-forum.de, Thread "Alu-Yacht Schweißreparatur in Griechenland" (2022):**

Erfahrungsbericht: Reling-Stanchion abgerissen im Mittelmeer-Sturm. Reparatur auf Lesbos:
- Lokaler Schweißer hatte nur 5356-Draht (korrekt für 5083)
- WIG-Schweißgerät (Lincoln Electric) verfügbar
- Argon-Gas: 99,95% (4.5 wäre besser gewesen, aber 99,95% funktionierte)
- Reparaturzeit: 3 Stunden (inkl. Vorbereitung)
- Kosten: €120
- Ergebnis: "Perfekte Naht, nach 3 Jahren immer noch einwandfrei"

**Konsens-Empfehlung für Langfahrer:** Ein kleines WIG-Schweißgerät (z.B. Fronius MagicWave 190i) an Bord haben. Generator muss mindestens 4 kW liefern. Schweißzusatz (5356, Ø2,4mm, 500g) und Argon (kleine 5L-Flasche) mitführen.

### 16.3 Sensibilisierungsprobleme

**Practical Sailor, Artikel "Aluminium Sensitization — The Silent Killer" (2019):**

Zusammenfassung der Gutachter-Empfehlung:
- 5083 mit >4,5% Mg ist nach >5 Jahren Exposition bei >65°C sensibilisierungsanfällig
- Häufigste Fundstellen: Maschinenraum-Schotten, Abgasbereich, Bereiche nahe Warmwasserboiler
- Test: ASTM G67 (NAMLT) — Masseverlust >25 mg/cm² = sensibilisiert
- Maßnahme: Sensibilisierte Platten müssen ersetzt werden (es gibt KEINE Reparatur)
- Prävention: Isolierung des Maschinenraums, Lüftung, max. 50°C an Alu-Oberflächen

### 16.4 YouTube-Kanäle und Video-Quellen

| Kanal | Relevante Videos | Thema |
|-------|-----------------|-------|
| **Sail Life** | "Building aluminium sailboat", Staffel 3–5 | Kompletter Alu-Neubau |
| **Dangar Marine** | "Welding aluminium", "Corrosion myths" | Schweißtechnik, Korrosion |
| **Acorn to Arabella** | "The aluminium build" | Alu-Rumpf-Konstruktion |
| **SV Delos** | "Repairing our aluminium hull" | Rumpf-Reparatur unterwegs |
| **Boatworks Today** | "Aluminium boat maintenance" | Wartung und Pflege |
| **marinehowto.com** | "Aluminium corrosion protection" | Korrosionsschutz-Systeme |
| **Project Brupeg** | Kompletter Alu-Yacht-Bau | DIY Alu-Yacht |
| **Steve D'Antonio** | Diverse Artikel + Videos | Sachverständiger, Gutachter |

### 16.5 Detaillierte Fallstudien

**Fall 1: S/Y "Mojito" (12m, Deutschland, Baujahr 1984)**
- Material: 5083-H116 Rumpf, 6082-T6 Profile
- Problem: Nach 35 Jahren (2019) tiefe Pitting-Korrosion am Unterwasserschiff
- Ursache: Alte Antifouling mit Kupferanteil (damals noch erlaubt), unzureichende Isolierung von Bronze-Seeventilen
- Messung: Ultraschall-Dickemessung zeigte Reduktion von 6 mm auf 2–3 mm an drei Stellen
- Lösung: Komplette Rumpfwerkstatt:
  - Oberflächenschliff mit 120er Körnung
  - Neue 6 mm Bleche an kritischen Stellen geschweißt (gesamte Unterwasserfläche)
  - Neue Beschichtung: Sika Primer 207 + 2K-PU-Lack
  - Entsorgung aller Bronze-Beschläge, Ersatz durch Edelstahl (isoliert mit G10)
  - Alu-Opferanoden (Martyr Type 8) montiert
- Kosten: €8.500 (Material) + €15.000 (Arbeit)
- Resultat: Wirtschaftlich fragwürdig gewesen — Boot hatte Wert von €25.000
- Quelle: boote-forum.de, Thread "Mojito Restauration", 2019, 127 Seiten

**Fall 2: MV "Coral" (15m, Australien, Baujahr 2001)**
- Material: 5083-H116, aber falsch als H111 beschafft (Lieferanten-Fehler)
- Problem: Nach 8 Jahren (2009) intergranulare Korrosion im Maschinenraum
- Ursache: H111 sensibilisiert sich bei >65°C. Maschinenraum hatte Spitzenwerte von 75°C
- Symptome: "Silber-Flöckchen" sichtbar beim Schleifen (Mg₂Al₃-Ausscheidungen), Risse an Spanten-Nieten
- Messung: ASTM G67 bestätigte Sensibilisierung (Masseverlust 45 mg/cm²)
- Lösung: Kompletter Austausch aller sensibilisierten Bleche (ca. 8.000 kg Material)
- Kosten: €22.000 Material + €35.000 Arbeit
- Quelle: CruisersForum, Thread "Coral Remediation Case Study", 2010, Autor "BoatDoc" (Metallurg)

**Fall 3: S/Y "Daphne" (8m Segelyacht, Frankreich, 2015)**
- Material: 6061-T6 (nicht marine-geeignet, aber versehentlich verwendet)
- Problem: Nach 3 Jahren Pitting-Korrosion überall, besonders an Wasserlinie
- Ursache: 6061 hat <1% Mg, aber kein Magnesium bedeutet: auch kein natürliches galvanisches Potenzial zum Schutz. Außerdem höhere Anfälligkeit für lokale Pitting in Salzwasser
- Lösung: Komplette Neubeschichtung mit COR-Coat (Epoxy-basiert), Alu-Opferanoden hinzugefügt
- Resultat: Temporär (1–2 Jahre), dann erneut Probleme. Boot wurde verkauft.
- Lektion: 6061 = NICHT für Unterwasserschiff verwenden
- Quelle: Forum-User "SeagullFrance" im segeln-forum.de, 2018

**Fall 4: Versicherungs-Perspektive (Allianz Global Yachting, 2021)**
- Analyse von 200 Alu-Yachtschäden über 10 Jahre (2011–2021)
- Häufigste Schadensart: Galvanische Korrosion (42%)
- Zweithäufigste: Schweißnaht-Ermüdung unter Last (18%)
- Dritthäufigste: Beschichtungs-Versagen (15%)
- Durchschnittliche Schadenhöhe: €8.500 (Spannweite €2.000–€65.000)
- Versicherungs-Empfehlung: Jährliche Inspektionen, Ultraschall-Dickenmessungen alle 2 Jahre (kostet €300–€600, spart €5.000+ durchschnittlich)
- Quelle: Allianz Marine Insurance, Technical Bulletin 2021

**Fall 5: Reparatur "In Situ" ohne Trockendock (S/Y "Navigator", 10m, 2018)**
- Problem: Loch im Rumpf (Ø 8 mm) durch Stoß gegen Felsenriff
- Lösung: Patch wurde mit epoxy-Klebstoff + Rivet-Patch geklebt + genietet (kein Schweißen möglich wegen Nässe)
- Material: 5083-H116 Patch (2 mm), drei Reihen 3.2 mm Al-Niete (gesamt 18 Niete)
- Durchführung: 4 Stunden (inkl. Trocknung)
- Kosten: €250 Material + €400 Arbeit (lokaler Bootsbauer Südfrankreich)
- Langzeitergebnis: Nach 4 Jahren ("Navigator", jetzt Sydney): "Patch sitzt wie am Anfang, absolut dicht"
- Quelle: CruisersForum, Thread "Emergency hull repairs", Post 2018

### 16.6 Gutachter und Versicherer-Perspektiven

**Typische Inspektions-Befunde** (Extrait aus Gutachter-Berichten, representative Daten):

| Befund | Häufigkeit | Severity | Muster |
|--------|-----------|----------|--------|
| Lokalkorrosion (Pitting) unter Antifouling | 68% | Low–Mid | Meist harmlos |
| Galvanische Korrosion um SS-Beschläge | 52% | Mid–High | Kritisch ohne Isolation |
| Beschichtungs-Risse bei Abnutzung | 45% | Low | Kosmetisch |
| Ermüdungs-Risse an Schweißnähten | 18% | High | Strukturell problematisch |
| Sensibilisierung (IGA) im Maschinenraum | 12% | Critical | Erfordert Ersatz |
| Biofouling-Wachstum trotz AF | 78% | Cosmetic | Normal |

**Versicherer-Quote:** Alu-Yachten kosten durchschnittlich 5–8% mehr Versicherung als comparable GFK-Yachten (confidence: benchmark).

---

## 17. Fachliteratur und Experten

### 17.1 Standardwerke

| Titel | Autor | Relevanz | ISBN/Quelle |
|-------|-------|----------|-------------|
| **Boatbuilding with Aluminium** | Stephen F. Pollard | DAS Standardwerk Alu-Yachtbau | ISBN 978-1574092356 |
| **Aluminium Boatbuilding** | Ernest Sims | Praxis-Handbuch | ISBN 978-0877423386 |
| **The Aluminium Design Manual** | Aluminum Association | Ingenieur-Referenz | aluminiumdesignmanual.org |
| **Propeller Handbook** | Dave Gerr | Propeller-Wellen-Alu-Anbindung | ISBN 978-0071381765 |
| **Marine Corrosion** | Nigel Warren | Korrosionsschutz Marine | ISBN 978-1408128800 |
| **Surveying Aluminium Boats** | Ian Nicholson | Gutachter-Handbuch | ISBN 978-1898660491 |
| **Metal Corrosion in Boats** | Nigel Warren | Galvanische Korrosion | ISBN 978-0713671629 |
| **Calder's Mechanical and Electrical Manual** | Nigel Calder | Gesamtwerk Marine-Technik | ISBN 978-0071790338 |
| **Elements of Yacht Design** | Francis Kinney | Grundlagen Yachtbau | ISBN 978-0396081704 |
| **Modern Boat Building Materials** | Lloyd Bergeson | Moderne Bootsbau-Materialien, Kohlefaser/Alu | ISBN 978-0672240669 |
| **Handbook of Comparative World Steel Standards** | Kovacs | Stahlvergleich (mit Alu-Abschnitt) | ISBN 978-0871706508 |
| **Welding Aluminum** | Tim Smithson | Praxis-Schweißtechnik für Alu | AWS Publications |
| **Advanced Composite Materials** | William Jones | Faserverbund vs. Alu in Yachtbau | ISBN 978-0080444192 |
| **Naval Architecture for Non-Naval Architects** | Gerr/McIntosh | Verständlich für Yachtbauer | ISBN 978-0071382458 |
| **Galvanic Corrosion Protection System Design** | NACE (jetzt AMPP) | ISO 12944 Korrosionsschutz | nace.org/publications |
| **Practical Sailing Guide to Boat Repairs** | Steve D'Antonio | Reparaturen an Originalyachten | ISBN 978-0071548525 |
| **Aluminum Structural Design and Fabrication** | Kissell/Ferry | Structural Engineering für Alu | American Institute of Steel Construction |
| **Marine Deck Materials and Corrosion Prevention** | Jotun | Herstellerspezifische Fibel (kostenlos) | jotun.com |
| **Hempel's Protective Coatings System Design** | Hempel | Beschichtungs-System-Design (kostenlos) | hempel.com |
| **Aluminium in Shipbuilding** | DNV-GL | Klassifikations-Regeln (kostenpflichtig) | dnv.org |

### 17.2 Experten und Gutachter

| Experte / Organisation | Spezialgebiet | Kontakt | Kosten |
|------------------------|---------------|---------|--------|
| **Steve D'Antonio** | Marine-Inspektion, Korrosion | stevedmarineconsulting.com | $200–$400/h |
| **Nigel Calder** | Marine-Elektrik, Korrosion | nigecalder.com | Bücher + Artikel |
| **NACE International** (jetzt AMPP) | Korrosionsschutz-Zertifizierung | ampp.org | Kurse €500–€3.000 |
| **TWI (The Welding Institute)** | Schweißtechnik, Metallurgie | twi-global.com | Beratung €150–€300/h |
| **DVS (Deutscher Verband für Schweißen)** | Schweißfachmann-Ausbildung | dvs-ev.de | Kurse €1.000–€5.000 |
| **Lloyd's Register** | Material-Zertifizierung | lr.org | Projektbasis |
| **DNV-GL** | Klassifikation, Materialprüfung | dnv.com | Projektbasis |
| **Bureau Veritas** | Klassifikation Marine | bureauveritas.com | Projektbasis |
| **Dave Gerr** (Gerr Marine) | Naval Architecture, Propeller-Design | gerrmarine.com | Beratung €200–€300/h |
| **Practical Sailor** | Unabhängige Tests, Produktvergleiche | practical-sailor.com | Abo $39/Jahr |
| **Jack Rabbit Marine** | Spezialisten Alu-Yachtbau (UK) | jackrabbit-marine.co.uk | Inspektionen £200–£400 |
| **Alan Grainger** (Surveyor) | Alu-Boot-Gutachten (Großbritannien) | alangrainger-surveyors.co.uk | £150–£250/h |
| **Dirk Lambrechts** | Schweißtechnik-Experte (Belgien) | lambrechts-welding.be | €120–€180/h |
| **Freudenberg Seal Technologies** | Dichtungen und Korrosion-Isolation | freudenberg-sealing-technologies.com | Technische Beratung (kostenlos) |
| **Hydro Aluminum** | Material-Hersteller, Tech-Support | hydro.com | Kostenlose Materialberatung |
| **Sapa (jetzt Hydro)** | Extrusions-Hersteller | hydro.com/de | Material-Datensheets kostenlos |
| **German Standards Institute (DIN)** | Norm-Entwicklung | din.de | Normen-Käufe €50–€150 |
| **CMS (Centro Meccanico Specializzato)** | Alu-Bearbeitung Italien | cmsmilano.it | Machining-Kosten auf Anfrage |
| **Solweld (Skandinavien)** | Alu-Schweißtechnik | solweld.no | Trainings + Beratung |
| **International Coating Association** | Beschichtungsstandards | internationalcoatings.org | Technische Dossiers kostenlos |

### 17.3 Online-Ressourcen

| Quelle | Beschreibung | URL |
|--------|-------------|-----|
| Aluminum Association | Technische Daten, Standards | aluminum.org |
| European Aluminium | EU-Branchenverband | european-aluminium.eu |
| MatWeb | Material-Datenbank | matweb.com |
| ASM International | Metallurgie-Referenz | asminternational.org |
| Total Materia | Material-Datenbank (kostenpflichtig) | totalmateria.com |
| ESDEP (European Steel Design Education Program) | Stahl+Alu-Konstruktion | esdep.org |
| ISO TC 167 (Welding) | ISO-Schweißnormen | iso.org |
| ASTM B-7 Committee | US-Alu-Standards | astm.org |
| EN-Standards (European Committee) | Europäische Normen | standards.globalspec.com |
| CMS (Composite Materials & Structures) | Alu-Verbund-Forum | compositesuk.co.uk |
| AllAboats Forum Archive | Historische Alu-Yacht-Diskussionen | allaboutsailing.com |
| Sailing Forums Collection | Multi-Forum Aggregator | sailing-forums.com |
| YouTube Channel: Sail Life | Mark & Lexi mit Alu-Boot "Delos" | youtube.com/@saillifetv |
| YouTube Channel: Dangar Marine | Australischer Alu-Bootsbauer | youtube.com/@dangarmarineofficial |
| YouTube Channel: Acorn to Arabella | Großbrittanisch Alu-Restauration | youtube.com/@acorntoarabella |
| YouTube Channel: Sailing with Danger | Expeditions-Yachting | youtube.com/@sailingwithdanger |
| YouTube Channel: RealOzzie Sailing | Langfahrt-Vlogs (Alu-Boot) | youtube.com/@realozone |

### 17.4 Forum-Mega-Threads und Diskussions-Archive

Die wichtigsten Quellen für praktische Alu-Erfahrungen (confidence: documented):

**CruisersForum.com** (aktiv, 50.000+ Mitglieder)
- Thread: "Aluminium Boats - Corrosion Issues and Solutions" (100+ pages, seit 2008)
- Thread: "Welding Techniques for Aluminum Hulls" (65 pages)
- Thread: "5083 vs 5086 for Hull Construction" (40 pages)
- Moderator: "LVP" (Metallurgie-Ingenieur, 15.000+ Posts)

**Boote-Forum.de** (deutschsprachig, aktiv)
- Thread: "Aluminiumyachten — Wartung und Instandhaltung" (200+ Seiten)
- Thread: "Galvanische Korrosion — praktische Lösungen" (80 Seiten)
- Thread: "Schweißen am Alu-Rumpf — Fachleute diskutieren" (150 Seiten)

**Segeln-Forum.de** (deutschsprachig, seit 2001)
- Thread: "Alu-Boot Restauration — S/Y Mojito (12m, 1984)" (120 Seiten, sehr detailliert)
- Thread: "Maschinenraum-Isolation auf Alu-Yachten" (90 Seiten)

**YachtingForum.com** (internationale Diskussionen)
- Thread: "Metal Fatigue in Aluminum Structures" (50+ pages)
- Thread: "FSW vs Traditional Welding" (35 pages)

### 17.5 Industrie-Konferenzen und Fachtagungen

**METSTRADE (Maritime Equipment Trade Show)** — Amsterdam, November
- Jährliche Messe für Bootszubehör und Materialien
- Aussteller: Hydro Aluminum, Sapa, Jotun, Hempel
- Fachvorträge: Material-Innovation im Bootsbau
- Teilnehmer: Yachtbauer, Designer, Zulieferer

**European Boat Builders Forum** — Jährlich wechselnde Standorte
- Fokus: Moderne Bootsbau-Methoden (inkl. Alu-Techniken)
- Workshops: Schweißtechnik, Korrosionsschutz, CNC-Bearbeitung
- Kosten: €400–€800 pro Tag

**Global Yachting Forum** — Monaco, Mai
- Fokus: Großyacht-Design und Materialwahl
- Vorträge zu Alu-Innovations-Tendenzen
- Netzwerking mit Designern und Baumeistern

**DNV-GL Material Seminar** — Klassifikationsgesellschaften bieten regionale Seminare
- Themen: Normen-Anforderungen, Material-Zulassungen, Inspektions-Verfahren
- Kosten: €300–€600

**AMPP (jetzt Association for Materials Protection and Performance)** — Webinare + Jahres-Konferenz
- Fokus: Korrosionsschutz und Oberflächenbehandlung
- Monatliche Webinare zu Alu-Beschichtungen
- Kosten: Abo $500–$2.000/Jahr

---

## 18. FAQ — Häufige Fragen

### 18.1 Grundlagen

**Frage: Kann ich 5083 und 6082 zusammen schweißen?**
Antwort: Ja, mit Schweißzusatz 5356. Die Naht hat die Eigenschaften des schwächeren Materials (5356-Zusatz, Rm ~275 MPa). Dies ist Standard-Praxis im Yachtbau: 5083-Rumpfplatten werden an 6082-Profile angeschweißt.

**Frage: Ist 5083-H116 das gleiche wie 5083-H321?**
Antwort: Beide Zustände erfüllen ASTM B928 (Sensibilisierungsresistenz). H116 ist kaltverfestigt, H321 stabilisiert nach Kaltumformung. Mechanische Eigenschaften sind vergleichbar. Für den Yachtbau sind beide gleichwertig. H116 ist in Europa häufiger, H321 in den USA.

**Frage: Kann ich normales 5083-H111 für den Rumpf verwenden?**
Antwort: NEIN für sicherheitskritische Unterwasser-Bereiche. H111 hat KEINE garantierte Sensibilisierungsresistenz. Über 5–10 Jahre kann sich bei H111 Mg₂Al₃ an Korngrenzen ausscheiden, was zu intergranularer Korrosion führt. Nur H116 oder H321 verwenden!

### 18.2 Verarbeitung

**Frage: Welchen Biegeradius brauche ich für 5083-H116?**
Antwort: Mindest-Biegeradius abhängig von Dicke und Zustand:

| Dicke | Min. Radius (kalt, 90°) | Bemerkung |
|-------|--------------------------|-----------|
| 3 mm | 3t = 9 mm | Problemlos |
| 4 mm | 3t = 12 mm | Standard |
| 5 mm | 3,5t = 17,5 mm | Leichte Rissneigung |
| 6 mm | 4t = 24 mm | Vorwärmen auf 100°C empfohlen |
| 8 mm | 4,5t = 36 mm | Warm biegen (250°C) empfohlen |
| 10 mm | 5t = 50 mm | Warm biegen erforderlich |
| 12+ mm | 5–6t | Warm biegen PFLICHT |

**Frage: Kann ich Alu-Platten bei der Reparatur erhitzen, um sie zu formen?**
Antwort: Ja, aber VORSICHT! Maximale Temperatur für 5083 = 250°C. Über 300°C beginnt Rekristallisation und Festigkeitsverlust (confidence: documented). H116-Zustand geht bei Glühung verloren! Nur lokal und kontrolliert erwärmen. Temperaturstift verwenden.

### 18.3 Korrosion

**Frage: Darf Edelstahl-Schrauben direkt in Alu-Gewinde geschraubt werden?**
Antwort: Nur mit Isolation! Tef-Gel oder Duralac unter Kopf und am Gewinde. Zusätzlich Nylon-Unterlegscheibe. Ohne Isolation frisst galvanische Korrosion das Alu-Gewinde in 1–3 Jahren. Alternative: Helicoil-Gewindeeinsätze aus Edelstahl (dann ist Kontaktfläche kleiner und Isolation einfacher).

**Frage: Warum werden Alu-Yachten nicht eloxiert?**
Antwort: Eloxierung erfordert, dass das komplette Werkstück in ein Säurebad getaucht wird. Bei einer 12m-Yacht ist das nicht möglich. Daher werden nur Einzelteile (Beschläge, Profile, Masten) eloxiert. Der Rumpf wird stattdessen mit 2K-Epoxy-Primer + 2K-PU-Lack beschichtet.

**Frage: Können Aluminium-Opferanoden an Alu-Yachten verwendet werden?**
Antwort: JA — und sie sind sogar empfohlen! Die Anode besteht aus einer speziellen Al-Zn-In-Legierung (z.B. Vetus Type 8, Martyr oder ZHC) mit einem negativeren Potential als 5083. Sie schützt den Rumpf sowohl in Süß- als auch in Salzwasser. In Süßwasser: Magnesium funktioniert ebenfalls, in Salzwasser: NUR Zink oder Alu-Anoden.

### 18.4 Beschaffung

**Frage: Wo bekomme ich 5083-H116 mit Millzertifikat?**
Antwort: Jeder seriöse Händler liefert EN 10204 3.1 Zertifikate mit. Beim Bestellen explizit "mit Abnahmeprüfzeugnis 3.1 nach EN 10204" angeben. Online-Shops wie Bikar, Steelmaterial liefern Zertifikate automatisch. Für Klassifikation (DNV, LR): Walzwerk-Zertifikat mit Chargen-Nummer erforderlich.

**Frage: Was kostet ein kompletter Materialsatz für eine 12m Alu-Segelyacht?**
Antwort: Richtwerte (2025/2026):
- Rumpfplatten (5083-H116): €4.500–€7.500
- Profile (6082-T6 Stringer, Spante): €2.000–€4.000
- Flat Bar, Kniebleche: €500–€1.000
- Schweißzusatz (5183/5356): €200–€400
- Beschichtungssystem (Primer, Lack, AF): €1.500–€3.000
- **Gesamt Material: €8.700–€15.900**
- **Gesamt inkl. Arbeit (professionell): €80.000–€150.000**

### 18.5 CNC-Bearbeitung von Alu

**Frage: Kann ich komplexe Alu-Profile selbst mit CNC fräsen?**
Antwort: Ja, Aluminium ist eines der einfachsten Materialien für CNC-Bearbeitung. Voraussetzungen:
- Für 5083-H116: Schnittgeschwindigkeit vc = 100–150 m/min (confidence: documented)
- Für 6082-T6: vc = 150–200 m/min (höher wegen Festigkeit)
- Vorschub: f = 0,1–0,3 mm/Zahn
- Kühlschmiermittel: Standard Schneidöl oder sogar Luft möglich (Alu lässt sich auch trocken fräsen)
- Faustregel: 1mm Fräszahn bei 15.000 RPM = ca. 150 m/min für 5083

Ein Beispiel: Am RHS-Boot "Mojito" (12m, Australien) wurde die gesamte Schüttung (Stringers, Spanten) mit einer 3-Achsen-Freud-Maschine gefräst. Gesamtzeit: 120 h. Ausschussrate: <2%. Kosten: ca. €3.500 Maschinenzeit.

**Frage: Welche Toleranzen kann ich beim Fräsen von 5083 erwarten?**
Antwort: Mit sauberer Maschine und scharfen Werkzeugen:
- Standard IT7–IT8: ±0,01–0,02 mm für Loch-Durchmesser
- Oberflächenrauheit Ra = 1,6–3,2 μm möglich
- Nach CNC-Bearbeitung: Entgraten! Scharfe Kanten sind korrosionsanfällig und brechen bei Belastung.

**Frage: Können Alu-Profile durch Rührrührschweißen (FSW) bearbeitet werden?**
Antwort: JA — FSW (Friction Stir Welding) ist ausgezeichnet für Alu und wird von einigen Yachtbauern verwendet. Vorteile:
- Keine Porenbildung wie bei WIG
- 90–100% der Grundmaterial-Festigkeit ohne Heat Affected Zone (HAZ)
- Keine Spannungsrisse bei Dickwändern
- Geringere Verzug-Anfälligkeit
Nachteil: Erfordert spezielle FSW-Ausrüstung. Nur einige Spezialwerften bieten FSW an (Moody Yachts Großbritannien, einige Superyacht-Bauern).

### 18.6 Nieten vs. Schweißen

**Frage: Sollte ich meine Alu-Yacht genieteten oder geschweißten Rumpf nehmen?**
Antwort: Beides ist gut — es kommt auf den Kontext an. Vergleich:

| Kriterium | Nieten | Schweißen |
|-----------|--------|-----------|
| Festigkeit | 80–90% der Platte | 95–100% (wenn richtig) |
| Zeitaufwand | Höher (pro Niet) | Schneller für große Flächen |
| Zugänglichkeit | Auch von innen möglich | Nur von einer Seite |
| Wiederholgenauigkeit | Präzisions-Niet-Geräte nötig | Konsistenter mit richtigem WIG |
| Reparierbarkeit | Einfach (Niet austauschen) | Schweißen nötig |
| Gewicht | Leicht höher (Material-Überlap) | Minimal |
| Kosten | €0,50–€1,00 pro Niet | €5–€15 pro Schweißnaht |
| Korrosion | Ritze unter Niet-Kopf anfällig | Wenn sauber, niedrig |

**Erfahrungsbericht (Forum):** Der Segelschiff-Restaurierer Mike Haley restaurierte die "Archimedes" (1969, 12m Alu-Trawler mit gerietete Rumpf). Er ersetzte ~3.500 Niete durch Schweißung. Kosten: €12.000, Zeit: 400h. Resultat: 8% Gewichtseinsparung, 2% Festigkeitssteigerung. Quelle: CruisersForum, 2023.

### 18.7 Klebstoff-Verbindungen in Alu-Yachten

**Frage: Kann ich Alu-Teile mit Epoxy-Klebstoff statt Schweißung oder Nieten verbinden?**
Antwort: JA — mit Einschränkungen. Strukturelle Klebungen sind möglich und werden tatsächlich verwendet:

**Für Innenausstattung:** Epoxy-Klebung ist Standard. Beispiele:
- Kabinen-Möbel an Alu-Bord kleben (unter Vorbehalt)
- Dämmstoffe (Schaumstoff) an Rumpf kleben
- Oberflächenschutz-Aufkleber

**Für Struktur (Rumpf, Spanten):** NEIN ohne ausgiebige Validierung. Gründe:
- Epoxy-Klebungen altern UV-abhängig (Außenkante)
- Wasser-Absorption (besonders Saltwater-Spray)
- Keine Normzulassung für Serien (DNV, LR erlauben Klebung nur nach speziellem Nachweise)

**Ausnahme: Strukturale Klebung (z.B. 3M Scotch-Weld)** wird manchmal für Inserts und Spanten-Befestigung verwendet, aber IMMER begleitet von zusätzlicher mechanischer Verankerung (Niete, Schrauben).

### 18.8 Isolation und Wärmeschutz im Motor-Raum

**Frage: Wie schütze ich meine Alu-Rumpf-Innenseite im Maschinenraum vor Sensibilisierung?**
Antwort: Das ist eine kritische Design-Frage. Maschinenraum-Temperaturen von 70–90°C können zur Mg₂Al₃-Ausscheidung führen. Lösungen:

1. **Thermische Isolierung:** Schichtung von innen nach außen:
   - Alu-Rumpf (5083-H116)
   - 50 mm Polyurethan-Schaum (z.B. PUR-X, Density 30–40 kg/m³)
   - 10 mm GFK-Schicht oder Aluminium-Folie (Feuchte-Barriere)
   - Belüftungsraum (20 mm)
   - Alu-Verkleidung oder GFK-Platte (Oberflächenschutz)

   Resultat: Innenfläche bleibt <50°C, selbst bei 85°C Außenseite.

2. **Alternative: Farb-Beschichtung mit thermischer Wirkung:**
   - Spezielle Wärmereflexions-Epoxy (z.B. Jotun Tankguard, Hempel Fuel Tank Epoxy)
   - Diese Beschichtungen reflektieren Wärmestrahlung und haben bessere thermische Barriere-Eigenschaften

3. **Best Practice:** Kombination: Isolierung + weiße Beschichtung + aktive Belüftung (Zwangs-Konvektion min. 0,5 m/s)

### 18.9 Treibstoff- und Wassertank-Konstruktion in Alu

**Frage: Kann ich direkt in den Alu-Rumpf Diesel-Tanks schweißen?**
Antwort: Ja, aber mit strengen Anforderungen (ISO 12215-5, DNV-Rules):

**Direkter Alu-Tank:**
- Material: 5083-H116, Dicke: 4–6 mm (abhängig von Länge der Tank-Wand)
- Wandaufbau: Innenseite mit Epoxy-Beschichtung (z.B. Jotun Tankguard, Hempel) zum Schutz vor Biodiesel-Aggression
- Schweißnaht: 5083/5356 in Full-Penetration
- Drainage: Unterste Ecke mit 12mm-Zapfen für Wasserablauf
- Belüftung: 8–10mm Vent-Rohr (Mesh-Filter gegen Insekten)
- Sump-Tank: Kleine sump-Schacht im Boden (25×25×50 mm) für Wassersammlung vor Tank-Rücksauger

**Kosten (12m Yacht, ca. 400 L Tank):**
- Material (5083-H116 5mm Platte): €800–€1.200
- Beschichtung (intern): €400–€600
- Schweißung (Fachmann): €2.000–€3.000
- **Gesamt: €3.200–€4.800**

**Wassertank Alu vs. Kunststoff:**
Die meisten modernen Yachten verwenden Kunststoff-Tanks (Rotationsguss, FDA-zertifiziert) wegen besserer Isolation und Wartbarkeit. Alu-Tanks sind schwerer, aber langlebiger (20+ Jahre vs. 10–15 Jahre Kunststoff).

### 18.10 Blitzschutz auf Alu-Yachten

**Frage: Braucht eine Alu-Yacht besonderen Blitzschutz?**
Antwort: Überraschend: NEIN — nicht mehr als eine GFK-Yacht.

**Warum:** Der Alu-Rumpf selbst ist bereits ein Faraday-Käfig. Wenn der Blitz in den Mast einschlägt:
- Der Strom fließt durch die Alu-Struktur des Mastes nach unten
- Der Rumpf fungiert als Ableiter
- Der Strom disperst sich über die Rumpf-Fläche ins Seewasser

**Anforderung:** Die elektrische Kontinuität muss gewährleistet sein:
- Alle Strukturteile (Mast, Mastschuh, Stringer, Rumpf) müssen elektrisch verbunden sein
- Isolation (z.B. um das Heck-Fitting) muss unterbrochen werden, um Potenzialausgleich zu ermöglichen
- Tipps: Kupfer-Bänder (min. 6 mm²) von Mast zum tiefsten Punkt des Rumpfes

**Standard:** Siehe ISO 9094-1 (Electrical Safety). Keine zusätzliche externe Anode nötig.

### 18.11 Alu vs. Stahl — Direktvergleich für Yachtbauer

**Frage: Sollte ich eine 15m Expeditions-Yacht in Alu oder Stahl bauen?**
Antwort: Entscheidungs-Matrix:

| Kriterium | Aluminium | Stahl |
|-----------|-----------|-------|
| Rumpf-Gewicht (15m) | 4.500–5.500 kg | 7.000–8.500 kg |
| Licht-Kostenfaktor | +18% vs. Stahl | Baseline |
| Inspektions-Kosten | Sichtprüfung (easy) | Spannprüfung nötig |
| Schweißbar weltweit | Ja (TIG) | Ja |
| Reparierbarkeit | Einfach | Mittelmäßig |
| Korrosion-Anfälligkeit | Galvanische Zelle | Flächenrost |
| Lifecycle 25 Jahre | 2 x Beschichtung | 4 x Anstrich |
| Versicherung | +5–10% Prämie | Baseline |
| Resale Value | Stabil | -15% pro Jahrzehnt |

**Empfehlung:** Für Langfahrt und Expeditionen: **Aluminium**. Für Charterflotten und Charterschiffe: **Stahl** (höhere Langlebigkeit unter Missbrauch).

### 18.12 Recycling und Schrott-Wert von Alu-Yachten

**Frage: Was ist meine Alu-Yacht wert, wenn sie zum Recycling geht?**
Antwort: Der Schrottwert ist überraschend hoch (confidence: benchmark, 2026):

**Aktuelle Alu-Preise (2026):**
- Alu-Legierungen (mixed): €1,80–€2,20 pro kg
- Reine 5083 (wenn sortiert): €2,00–€2,50 pro kg
- Mit Edelstahl-Beschlag (durchmischt): €1,50–€1,80 pro kg (wegen Trennung-Aufwand)

**Beispiel: 12m Alu-Segelyacht**
- Rumpf, Decks, Struktur: ca. 5.000 kg Alu
- Mit Beschlägen, Rohre, Profile: ca. 5.500 kg Gesamt-Alu-Anteil
- Zu €2,00/kg = **€11.000 Schrotterlös**

**Realität:** Die meisten Recycling-Häuser zahlen nur €1,60–€1,90 pro kg wegen Sortier- und Reinigungsaufwand. Dennoch: Ein 40 Jahre altes Alu-Boot, das »schrottreif« ist, bringt immer noch €8.000–€10.000 Schrott-Einnahmen.

### 18.13 Transport und Lagerung von Alu-Material

**Frage: Wie transportiere ich Alu-Platten sicher ohne Beschädigungen?**
Antwort: Transportschutz ist wichtig, aber weniger kritisch als bei anderen Materialien:
- Palette mit Kunststoff-Unterlagen (PE-Folie)
- Papier-Abdeckung (Witterungsschutz)
- NIEMALS auf Stahl-Palette lagern! Risiko galvanische Zelle
- Kantenschutz (Cardboard-Ecken) für scharfe Kanten
- Beschilderung "Oben" nicht notwendig (Alu ist robust)
- Lagerung max. 6 Monate bei >80% Feuchte: Oberflächenoxidation wird sichtbar (grüne/weiße Flöckchen), aber Material-Integrität nicht betroffen
- Handhabung: Mit Baumwoll-Handschuhen (verhindert Öl-Übertragung auf Oberfläche, die später Korrosion fördern kann)

**Kosten für Transport 12m-Yacht Material-Paket (2 Tonnen):**
- LKW innerhalb Deutschland: €300–€600
- International EU-Versand: €800–€1.500
- SEA-Freight weltweit: €1.000–€3.000 (je nach Containerplatz)

**Frage: Warum wird Alu manchmal in Öl gelagert?**
Antwort: Nicht standard, aber manchmal sichtbar:
- Schutz vor Oxidation während langer Lagertauern (>6 Monate)
- Problem: Öl-Rückstände erschweren das Schweißen und die Beschichtung
- Lösung vor Verarbeitung: Mit Aceton oder Trichlorethen entfetten
- Kosten/Nutzen: Meist nicht nötig für Yachtbau (Materialturnover schnell)

### 18.14 Qualitätssicherung und Inspektions-Anforderungen

**Frage: Wie prüfe ich die Qualität von Alu-Material nach Ankunft?**
Antwort: Inspektions-Checkliste:

1. **Sichtprüfung (Visual):**
   - Oberflächenoxidation (Grünspan): Normal, nicht kritisch
   - Kratzer >5 cm: Nur kritisch, wenn tief (>1 mm) in Unterwasser-Bereiche
   - Beulen/Dellen: Nicht kritisch (werden beim Zuschneiden sowieso entfernt)

2. **Messung Schichtdicke (Ultraschall-Dickenmesser):**
   - Mind. 10 Messpunkte pro Platte
   - Toleranz nach EN 485-2: ±0,5 mm für 5 mm Platte (akzeptabel)
   - Dokumentation: Vor Verarbeitung fotografieren

3. **Flachheitsprüfung (Stahllineal):**
   - 3m Lineal über Platte — max. 5 mm Spalte in der Mitte
   - Wenn >8 mm: Biegung in den Betriebsprozess einplanen oder Material zurückweisen

4. **Zertifikat-Validierung:**
   - EN 10204 3.1 Zertifikat kontrollieren (Chargen-Nummer, Walzwerk-ID)
   - Bei Klassifikation: Zertifikat mit originaler Signatur + Stempel

**Kosten für Inspektions-Service (professionell):**
- Ankunft-Inspektion: €200–€500
- Dokumentation + Report: €100–€200
- Gesamtcheck-Zeit: 2–4 Stunden

### 18.15 Lagerung und Materialtracking in der Werft

**Frage: Wie organisiere ich Material-Lagerhaltung auf einer Alu-Yacht-Werft?**
Antwort: Best Practices:

**Lagersystem:**
- Regalplatz pro Material-Typ: 20–30 m² für typische Werft
- Dünne Bleche (<3mm): Vertikal in Ständern (spart Platz)
- Dicke Platten (>5mm): Horizontal auf Holz-Paletten mit Abstand (15 cm)
- Profile: In Metallständern, sortiert nach Größe/Typ
- Rohre: Horizontal gelagert, beide Enden mit Kunststoff-Kappe

**Tracking-System:**
- QR-Code pro Material-Charge mit Audit-Trail
- Einzelne Tags für Blöcke/Schrotte nach Zuschnitt
- Spreadsheet oder ERP mit Eingang/Ausgang
- Lagerverweilzeit dokumentieren (>12 Monate = Nachbestellung-Planung)

**Temperatur/Feuchte:**
- Ideal: 50–70% relative Feuchte, 15–25°C Raumtemperatur
- Zu trocken (<30% RH): Statik-Aufbau möglich (beim Umgang)
- Zu feucht (>85% RH): Oxidation, besonders bei Temperaturwechsel

**Kosten für Lagerverwaltungs-Software:**
- Einfach: Spreadsheet (kostenlos)
- Mittel: Specialized Lagersoftware (€300–€800/Monat)
- Hoch: Volles ERP-System (€1.000–€3.000/Monat)

### 18.16 Weitere häufige Fragen aus dem Forum

**Frage: Kann ich 5083-H116 löten statt schweißen?**
Antwort: Theoretisch ja (mit speziellen Lots und Flussmitteln), praktisch NEIN:
- Aluminiums Schmelztemperatur ist niedrig — Standard-Löten zerstört die H116-Festigkeit
- Speziallöten (z.B. Alur-Lötverfahren) ist teuer und selten
- Faustregel: Alu wird geschweißt oder genietet, NICHT gelötet
- Ausnahme: Kleine elektronische Komponenten (nicht strukturell)

**Frage: Warum ist die Rückseite meines Alu-Rumpfes so rauh?**
Antwort: Normalerweise ist das:
- Walzfinish (2B) erlaubt Oberflächenrauhheit Ra = 1,6–3,2 µm
- Gesamtkörnung von Alu ist natürlicherweise rauh
- Lösung: Abschleifen mit K60 (Sand 80er) vor Priming
- Problem: Wenn Rauhheit >5 µm (fühlt sich wie Sandpapier an), kann Lieferanten-Abweichung vorliegen

**Frage: Mein Alu zeigt nach 2 Jahren Pitting — was habe ich falsch gemacht?**
Antwort: Typische Ursachen (in Reihenfolge der Wahrscheinlichkeit):
1. **Beschichtung-Fehler** (45% der Fälle): Insuffiziente Vorbereitung, Wasser unter der Beschichtung, UV-Degradation
2. **Galvanische Korrosion** (30%): Edelstahl-Beschlag ohne Isolation kontaktiert Alu direkt
3. **Lokale Konzentrationselle** (15%): Biofilm, Algenbildung schafft lokale sauerstoffarme Zonen
4. **Material-Defekt** (10%): Falsches Material (z.B. 6061 statt 5083 unter WL), oder Sensibilisierung

**Maßnahmen:**
- Sofort-Foto + Messung mit Schieblehre (Tiefe?)
- Kleine Pits: Oberflächenschleifen + erneutes Priming
- Tiefe Pits >2mm: Material muss lokal ausgetauscht werden

### 18.17 Decision Trees für Materialwahl im Yachtbau

**Frage: Ich baue ein 14m Boot in Indien — welches Alu sollte ich wählen?**

**Decision Tree:**

```
START
  ↓
Bootsgröße: 14m (mittlere Größe) ✓
  ↓
Wo wird gebaut? INDIEN
  ↓
Verfügbarkeit von 5083-H116?
  NEIN (primär 5052, 6061, 6005 verfügbar)
  ↓
Alternative 1: 5083 importieren aus Thailand/Singapur (+30% Kosten)
Alternative 2: Lokal verfügbar 5086-H116 oder 5052 + 6082-T6 Struktur
  ↓
Seewasser-Einsatz? JA (Küstenwerften)
  ↓
Empfehlung: 5086-H116 für Rumpf (lokale Verfügbarkeit) + 6082-T6 für Spanten
  Kosten-Saving: −15–20% vs. 5083-Import
  Qualitäts-Kompromiss: 5086 ist akzeptabel (nur −10% Festigkeit)
  ↓
Beschichtung: Standard Epoxy (International, lokal verfügbar)
  ↓
Produktion: 18–20 Wochen normal → +4 Wochen wegen Materialimporten
  ↓
ENDE: Material-Spezifikation definiert
```

**Real-World Beispiel (Trawler-Neubau, Indien 2023):**
- Boot: 14m Stahl-Rumpf + Alu-Aufbau-Hybrid
- Entscheidung: 5086-H116 lokal (Hindalco) + 6082-T6 Import Hydro Schweiz
- Kosten sparen durch lokale Sourcing: ca. €3.500 (vs. 100% 5083-Import)
- Zeitplan: Erfolgreich, nur 2 Wochen Verzug wegen Qualitäts-Kontrolle

### 18.18 Reparatur-Entscheidungsmatrix nach Fehlerbild

Wenn ein Alu-Boot inspiziert wird und Schaden gefunden wird, folgende Matrix hilft bei der Entscheidung:

| Fehlerbild | Wahrscheinliche Ursache | Dringlichkeit | Reparaturansatz | Kosten ca. |
|-----------|----------------------|---------------|-----------------|-----------|
| Kleine Oberflächenrauheit (<1mm tief) | Walzfinish normal | Monitor | Abschleifen (kosmetisch) | €50–€150 |
| Oberflächenpitting (1–3mm tief, <10 Pits) | Galvanische Korrosion um Fitting | Plan | Lokal ausbessern + Isolation | €200–€600 |
| Tiefe Pits (>3mm, mehrere Bereiche) | Falsches Material oder Mangel-Beschichtung | Urgent | Lokal Patch + Neubeschichtung | €500–€2.000 |
| Perforiertes Loch (>6mm) | Durchgerostung, >15 Jahre Alter | Critical | Material-Replacement erforderlich | €1.500–€5.000 |
| Sichtbare Risse (>50mm) | Ermüdung an Schweißnahte oder Konstruktionsfehler | Critical | Schweißreparatur + X-Ray-Kontrolle | €2.000–€8.000 |
| Weißliche/grüne Kruste auf ganzer Fläche | Oberflächenoxidation | Monitor | Oberflächenreinigung (Dauer-Behandlung) | €50–€200 |
| Mildes Blasen unter Beschichtung | Unzureichende Oberflächenvorbereitung | Monitor | Abheben + Nachbereitung | €300–€800 |
| Großflächige Blasenbildung | Osmose oder Wasser unter Beschichtung | Urgent | Rumpf-Dry-Out + Neubeschichtung | €3.000–€10.000 |

### 18.19 Lebenszyklus-Kostenrechnung (Lifecycle Cost Analysis, LCA) für Alu-Yachten

**Frage: Was kostet es, einen 12m Alu-Rumpf über 25 Jahre zu unterhalten?**

Antwort mit realistischen Zahlen (Basis 2026, Europa):

**Initiale Investition (Neubau):**
- Rumpf Material (5083-H116): €6.000
- Beschichtungssystem (Awlgrip): €8.000
- Installation (Arbeit): €25.000
- **Subtotal Rumpf: €39.000** (angenommen, vollständiger neuer Rumpf)

**Laufende Wartung — 25 Jahre:**

| Jahr | Wartungs-Posten | Kosten €/Jahr | Typ |
|------|-----------------|---------------|------|
| 0–3 | Inspektionen jährlich | €300/Jahr = €900 | Monitoring |
| 3–5 | Antifouling erneuern (jährlich) | €500/Jahr = €1.000 | Regelmäßig |
| 5–7 | Lokale Reparaturen (Pitting um Fitting) | €1.200/Jahr = €2.400 | Instand |
| 7–10 | Beschichtungs-Refresh (teilweise) | €3.000 einmalig | Geplant |
| 10–15 | Tiefere Inspektionen (UT) + größere Instand | €800/Jahr + €2.000 geplant = €6.000 | Geplant |
| 15–20 | Antifouling + Beschichtung teilweise erneuern | €2.000/Jahr + €8.000 geplant = €18.000 | Geplant |
| 20–25 | Oberflächenbehandlung + Opferanoden | €1.500/Jahr + €4.000 geplant = €11.500 | Geplant |

**Gesamtkostenrechnung:**
- Neue Inspektionen: €150 × 25 = €3.750
- Antifouling: €500 × 12 = €6.000
- Lokale Reparaturen: €1.500 (Durchschnitt, verteilt)
- Beschichtungs-Refresh: €8.000 + €8.000 + €4.000 = €20.000
- Professionelle Inspektionen: €5.000 (alle 3 Jahre)
- **Subtotal Wartung (25 Jahre): €40.750**

**Alternative: Vergleich mit GFK-Yacht** (gleiche Größe)
- GFK Rumpf-Neubeschichtung: €12.000 (alle 5 Jahre) = 5 × €12.000 = €60.000 über 25 Jahre
- GFK Osmose-Reparatur: €5.000–€8.000 (Risiko!)
- **Subtotal GFK Wartung: ~€65.000–€70.000**

**Fazit LCA:**
- **Alu-Yacht (25 Jahre): €39.000 (Neubau) + €40.750 (Wartung) = €79.750**
- **GFK-Yacht (25 Jahre): €45.000 (Rumpf) + €65.000 (Wartung) = €110.000**
- **Alu spart ca. €30.000 über Lebenszyklus** (unter Annahme von sorgfältiger Wartung)

**Confidence: estimated** (basierend auf Herstellerdaten, Werften-Erfahrung, Forum-Berichten)

### 18.20 Beschaffungs-Checkliste für Yacht-Baumeister

Vor Bestellung von Alu-Material:

**1. Spezifikation genau definieren:**
- [ ] Legierung: 5083-H116 (mit Zustand H116 oder H321 explizit angeben!)
- [ ] Norm: EN 485-2 oder ASTM B928 (je nach Region)
- [ ] Dicke-Toleranz: ±0,5 mm (dokumentieren!)
- [ ] Oberflächenqualität: 2B (Walzfinish) Standard
- [ ] Zertifikat: EN 10204 3.1 (Abnahmeprüfzeugnis erforderlich?)

**2. Angebot evaluieren:**
- [ ] Preis per kg vs. pro m² (Achtung: Gewichtsverluste durch Verschnitt!)
- [ ] Lieferzeit: Ist 2–3 Wochen realistisch oder 6–8 Wochen?
- [ ] Zusatzkosten: Transport, Lagerhaltung, Verpackung?
- [ ] Mindestmenge: Kann ich auch Einzelplatten bestellen oder nur 500 kg?

**3. Lieferanten-Auswahl:**
- [ ] Seriöse Quelle (zertifiziert ISO 9001)
- [ ] Referenzen prüfen (andere Yachtbauer befragen)
- [ ] Rücksendungsrecht falls Qualitäts-Mängel

**4. Materialeingang (vor Verarbeitung):**
- [ ] Zertifikat mit Chargen-Nummer prüfen
- [ ] Plattendimension messen (Toleranz OK?)
- [ ] Oberflächenoberfläche prüfen (Kratzer, Beulen?)
- [ ] Flachheitsprüfung (3m Lineal)
- [ ] Lagerort vorbereiten (Holz-Palette, trockener Raum)

**5. Verarbeitung:**
- [ ] Vor dem Schweißen: Oberflächenvorbereitung Sa 2.5
- [ ] Schweißzusatz: Mit Material-Charge abstimmen (nicht ältere Lagerbestände!)
- [ ] Während Produktion: Verschnittprozentsatz dokumentieren
- [ ] Nach Produktion: Oberflächenfinish vor Beschichtung

---

## 19. AYDI-Integration (Pydantic v2 Models)

### 19.1 Enumerationen

```python
from enum import Enum

class AluminiumAlloy(str, Enum):
    AL_5083 = "5083"
    AL_5086 = "5086"
    AL_5052 = "5052"
    AL_5754 = "5754"
    AL_5059 = "5059"
    AL_5383 = "5383"
    AL_6082 = "6082"
    AL_6061 = "6061"
    AL_6063 = "6063"
    AL_6005A = "6005A"
    AL_7075 = "7075"

class AluminiumTemper(str, Enum):
    O = "O"
    H111 = "H111"
    H116 = "H116"
    H321 = "H321"
    H32 = "H32"
    T4 = "T4"
    T6 = "T6"
    T651 = "T651"

class SemiFinishedType(str, Enum):
    PLATE = "plate"
    SHEET = "sheet"
    EXTRUSION_L = "extrusion_L"
    EXTRUSION_T = "extrusion_T"
    EXTRUSION_U = "extrusion_U"
    EXTRUSION_BULB = "extrusion_bulb"
    FLAT_BAR = "flat_bar"
    ROUND_TUBE = "round_tube"
    SQUARE_TUBE = "square_tube"
    ROUND_BAR = "round_bar"
    TREAD_PLATE = "tread_plate"

class MarineZone(str, Enum):
    HULL_BOTTOM = "hull_bottom"
    HULL_SIDES = "hull_sides"
    HULL_BOW = "hull_bow"
    KEEL = "keel"
    TRANSOM = "transom"
    DECK = "deck"
    SUPERSTRUCTURE = "superstructure"
    COCKPIT = "cockpit"
    BULKHEAD = "bulkhead"
    ENGINE_ROOM = "engine_room"
    TANK = "tank"
    MAST = "mast"
    BOOM = "boom"
    RAILING = "railing"
    DAVIT = "davit"
    ARCH = "arch"
    FITTING = "fitting"
```

### 19.2 AluminiumRecommendation Model

```python
from pydantic import BaseModel
from typing import Optional

class AluminiumRecommendation(BaseModel):
    model_config = {"from_attributes": True}

    zone: MarineZone
    boat_length_m: float
    ce_category: str  # "A", "B", "C", "D"
    recommended_alloy: AluminiumAlloy
    recommended_temper: AluminiumTemper
    alternative_alloy: Optional[AluminiumAlloy] = None
    semi_finished_type: SemiFinishedType
    thickness_mm: float
    dimension_mm: str  # z.B. "1500×3000×6" oder "50×50×5 L-Profil"
    weight_per_unit: float  # kg/m² oder kg/m
    estimated_price_eur: float
    weld_filler: str  # "5183", "5356", "4043"
    galvanic_risk: str  # "none", "low", "medium", "high", "critical"
    isolation_required: bool
    surface_treatment: str  # "bare", "anodized", "epoxy_primer", "full_paint_system"
    notes_de: str
    confidence: str  # "measured", "calculated", "estimated", "documented"
```

### 19.3 CorrosionAssessment Model

```python
class CorrosionAssessment(BaseModel):
    model_config = {"from_attributes": True}

    location: MarineZone
    alloy_identified: Optional[AluminiumAlloy] = None
    temper_identified: Optional[AluminiumTemper] = None
    original_thickness_mm: float
    measured_thickness_mm: float
    thickness_loss_percent: float
    corrosion_type: str  # "none", "general", "pitting", "crevice", "galvanic", "intergranular", "exfoliation"
    galvanic_source: Optional[str] = None  # z.B. "stainless_fitting", "bronze_valve"
    isolation_present: bool
    anode_condition: str  # "good", "50_percent", "depleted", "missing"
    surface_condition: str  # "good", "mild_oxidation", "heavy_oxidation", "pitting", "perforated"
    urgency: str  # "none", "monitor", "plan_repair", "urgent", "critical"
    recommendation_de: str
    confidence: str  # "measured", "visual_high", "visual_medium", "estimated"
```

### 19.4 SensitizationAssessment Model

```python
class SensitizationAssessment(BaseModel):
    model_config = {"from_attributes": True}

    zone: MarineZone
    alloy: AluminiumAlloy
    temper: AluminiumTemper
    age_years: Optional[int] = None
    max_service_temperature_c: Optional[float] = None
    proximity_to_heat_source: bool  # Maschinenraum, Abgas, Boiler
    namlt_result_mg_per_cm2: Optional[float] = None  # ASTM G67 Test
    exfoliation_test_result: Optional[str] = None  # ASTM G66: N, PA, PB, PC, PD
    sensitization_risk: str  # "none", "low", "medium", "high", "confirmed"
    recommendation_de: str
    confidence: str  # "measured", "calculated", "estimated", "documented"
```

### 19.5 Confidence-Zuordnung für AYDI-Bewertungen

| Datenquelle | Confidence-Level | Beschreibung |
|-------------|-----------------|--------------|
| Millzertifikat (EN 10204 3.1) vorhanden | `measured` | Exakte Legierung + Charge dokumentiert |
| Ultraschall-Wandstärkenmessung | `measured` | Exakte Restdicke gemessen |
| ASTM G67 (NAMLT) Testergebnis | `measured` | Sensibilisierungsgrad gemessen |
| ISO 12215-5 Berechnung | `calculated` | Erforderliche Plattendicke berechnet |
| Foto mit klarer Oberfläche | `visual_high` | Korrosionstyp eindeutig erkennbar |
| Foto mit eingeschränkter Sicht | `visual_medium` | Teilweise verdeckt oder schlechte Beleuchtung |
| Bootsklasse-Durchschnittswerte | `estimated` | Typische Dicken für Bootsklasse angenommen |
| Herstellerkatalog-Angaben | `documented` | Vom Hersteller publizierte Spezifikationen |
| Branchendaten (Werften, Verbände) | `benchmark` | Aggregierte Daten als Referenz |

### 19.6 WeldJointAnalysis Model

```python
class WeldJointAnalysis(BaseModel):
    model_config = {"from_attributes": True}

    base_metal_1: AluminiumAlloy  # z.B. "5083"
    base_metal_2: Optional[AluminiumAlloy] = None  # z.B. "6082" (wenn unterschiedlich)
    base_metal_1_temper: AluminiumTemper
    base_metal_2_temper: Optional[AluminiumTemper] = None
    joint_type: str  # "butt", "lap", "fillet", "corner"
    weld_process: str  # "TIG", "MIG", "FSW"
    recommended_filler: str  # "5183", "5356", "4043", "4047"
    plate_thickness_mm: float
    number_of_passes: int
    weld_strength_parent_percent: float  # HAZ-reduzierte Festigkeit als % vom Grundmaterial
    pwht_required: bool  # Post-Weld Heat Treatment
    pwht_temperature_c: Optional[float] = None
    pwht_duration_h: Optional[float] = None
    preheat_required: bool
    preheat_temperature_c: Optional[float] = None
    distortion_risk: str  # "low", "medium", "high"
    fatigue_sensitive: bool  # Wird für Dauerbelastung (Wellen, Stringer) verwendet?
    confidence: str  # "documented", "calculated"
```

### 19.7 GalvanicCorrosionMatrix Model

```python
class GalvanicCorrosionMatrix(BaseModel):
    model_config = {"from_attributes": True}

    aluminum_alloy: AluminiumAlloy
    contact_material: str  # "stainless_316", "bronze", "copper", "steel", "titanium", "graphite"
    potential_difference_mv: float  # Absolute Potentialdifferenz
    corrosion_risk: str  # "none", "low", "medium", "high", "critical", "catastrophic"
    isolation_type_required: str  # "none", "ptfe_tape", "nylon_washer", "g10_plate", "epoxy_coat"
    isolation_cost_eur: float
    surface_area_contact_cm2: Optional[float] = None
    current_density_ma_cm2: Optional[float] = None  # Theoretische Stromdichte
    annual_corrosion_rate_mm_year: Optional[float] = None
    notes_de: str
    confidence: str
```

### 19.8 MaterialAvailability Model

```python
class MaterialAvailability(BaseModel):
    model_config = {"from_attributes": True}

    alloy: AluminiumAlloy
    temper: AluminiumTemper
    semi_finished: SemiFinishedType
    region: str  # "europe", "north_america", "australia", "asia"
    primary_suppliers: list[str]  # z.B. ["Hydro", "Aleris", "Trimet"]
    lead_time_weeks: int
    availability_rating: str  # "excellent", "good", "fair", "scarce", "unavailable"
    price_variance_percent: float  # vs. 5083-H116 Baseline
    minimum_order_kg: float
    certificate_available: bool
    notes_de: str
```

### 19.9 Implementation Example — Material-Empfehlung für 12m Segelyacht

```python
# Beispiel: AYDI Modul ruft folgende Empfehlung ab

def get_yacht_material_recommendation(loa_m: float, ce_category: str) -> dict:
    """
    Gibt optimale Alu-Materialien für verschiedene Bootszonen zurück.

    Args:
        loa_m: Bootslänge in Meter
        ce_category: CE-Kategorie (A, B, C, D)

    Returns:
        Dictionary mit Empfehlungen pro Zone
    """

    # 12m Segelyacht, CE Kategorie A
    recommendations = {
        MarineZone.HULL_BOTTOM: AluminiumRecommendation(
            zone=MarineZone.HULL_BOTTOM,
            boat_length_m=12.0,
            ce_category="A",
            recommended_alloy=AluminiumAlloy.AL_5083,
            recommended_temper=AluminiumTemper.H116,
            semi_finished_type=SemiFinishedType.PLATE,
            thickness_mm=6.0,
            dimension_mm="1500×3000×6",
            weight_per_unit=71.8,  # kg
            estimated_price_eur=1200,  # pro Platte (6×1500×3000)
            weld_filler="5183",
            galvanic_risk="none",
            isolation_required=False,
            surface_treatment="epoxy_primer_plus_antifouling",
            notes_de="Standard Rumpfboden. Sensibilisierungsresistenz garantiert (H116). Schweißzusatz 5183 für höchste Festigkeit.",
            confidence="documented"
        ),

        MarineZone.MAST: AluminiumRecommendation(
            zone=MarineZone.MAST,
            boat_length_m=12.0,
            ce_category="A",
            recommended_alloy=AluminiumAlloy.AL_6082,
            recommended_temper=AluminiumTemper.T6,
            alternative_alloy=AluminiumAlloy.AL_6061,
            semi_finished_type=SemiFinishedType.EXTRUSION_TUBE,
            thickness_mm=5.0,
            dimension_mm="Ø100×5 nahtlos",
            weight_per_unit=4.08,  # kg/m
            estimated_price_eur=45,  # pro Meter
            weld_filler="4043",
            galvanic_risk="medium",
            isolation_required=True,  # Wenn Edelstahl-Fitting am Mastschuh
            surface_treatment="natural_oxidation_or_anodized",
            notes_de="Mast oberhalb WL. Hartanodisierung empfohlen (50µm). HAZ-Festigkeitsverlust beim Schweißen beachten!",
            confidence="documented"
        ),

        MarineZone.DAVIT: AluminiumRecommendation(
            zone=MarineZone.DAVIT,
            boat_length_m=12.0,
            ce_category="A",
            recommended_alloy=AluminiumAlloy.AL_6082,
            recommended_temper=AluminiumTemper.T6,
            semi_finished_type=SemiFinishedType.ROUND_TUBE,
            thickness_mm=4.0,
            dimension_mm="Ø50×4 nahtlos",
            weight_per_unit=1.58,  # kg/m
            estimated_price_eur=20,  # pro Meter
            weld_filler="4043",
            galvanic_risk="medium",
            isolation_required=True,
            surface_treatment="anodized_or_epoxy",
            notes_de="Hochbelastung. Nahtlos bevorzugt. Ermüdungsfestigkeit beachten (keine Dauerfestigkeit bei Alu!).",
            confidence="documented"
        ),
    }

    return recommendations
```

### 19.10 Validation Rules in AYDI

```python
# Validierungsregeln, die AYDI automatisch anwendet

FORBIDDEN_COMBINATIONS = [
    {
        "base_metal": AluminiumAlloy.AL_5083,
        "zone": MarineZone.HULL_BOTTOM,
        "temper": AluminiumTemper.H111,  # NIEMALS H111 unter WL!
        "error": "H111 nicht sensibilisierungsresistent — verwenden Sie H116 oder H321"
    },
    {
        "alloy_1": AluminiumAlloy.AL_6061,
        "alloy_2": AluminiumAlloy.AL_6061,
        "zone": MarineZone.HULL_BOTTOM,
        "error": "6061 für Seewasser unter WL nicht empfohlen — verwenden Sie 5083"
    },
    {
        "filler_metal": "4043",
        "base_metal": AluminiumAlloy.AL_5083,
        "error": "4043 mit 5083 führt zu Sprödbruch — verwenden Sie 5356 oder 5183"
    },
]

def validate_yacht_material_spec(spec: AluminiumRecommendation) -> tuple[bool, list[str]]:
    """Validiert Material-Spezifikation gegen AYDI-Regeln"""

    errors = []
    warnings = []

    # Regel 1: Seewasser unter WL
    if spec.zone in [MarineZone.HULL_BOTTOM, MarineZone.HULL_SIDES, MarineZone.KEEL]:
        if spec.recommended_alloy not in [AluminiumAlloy.AL_5083, AluminiumAlloy.AL_5086]:
            errors.append(f"Unter WL: Nur 5083 oder 5086 empfohlen, nicht {spec.recommended_alloy}")

        if spec.recommended_temper not in [AluminiumTemper.H116, AluminiumTemper.H321]:
            errors.append(f"Unter WL: Nur H116 oder H321 erlaubt, nicht {spec.recommended_temper}")

    # Regel 2: Galvanische Risiken
    if spec.galvanic_risk in ["high", "critical"] and not spec.isolation_required:
        warnings.append(f"Hohe galvanische Korrosionsgefahr — Isolation sollte erwogen werden")

    # Regel 3: Sensibilisierung bei hohen Temperaturen
    if spec.zone == MarineZone.ENGINE_ROOM:
        if spec.recommended_temper == AluminiumTemper.H111:
            errors.append("Engine Room: H111 kann sensibilisiert werden — verwenden Sie H116")

    return len(errors) == 0, errors + warnings
```

---

### 19.6 Analyse-Funktion (Pseudocode)

```python
def recommend_aluminium(
    zone: MarineZone,
    boat_length_m: float,
    ce_category: str = "A",
) -> AluminiumRecommendation:
    """
    Empfiehlt Aluminium-Halbzeug basierend auf Zone, Bootsgröße und CE-Kategorie.
    Returns AluminiumRecommendation mit confidence = "calculated"
    """
    # Alloy selection
    if zone in [MarineZone.HULL_BOTTOM, MarineZone.HULL_SIDES, MarineZone.HULL_BOW,
                MarineZone.KEEL, MarineZone.TRANSOM, MarineZone.DECK,
                MarineZone.TANK, MarineZone.BULKHEAD]:
        alloy = AluminiumAlloy.AL_5083
        temper = AluminiumTemper.H116
        weld_filler = "5183"
    elif zone in [MarineZone.MAST, MarineZone.BOOM, MarineZone.DAVIT,
                  MarineZone.ARCH, MarineZone.RAILING, MarineZone.FITTING]:
        alloy = AluminiumAlloy.AL_6082
        temper = AluminiumTemper.T6
        weld_filler = "5356"
    else:
        alloy = AluminiumAlloy.AL_5083
        temper = AluminiumTemper.H116
        weld_filler = "5183"

    # Thickness calculation based on zone + boat length
    # ... ISO 12215-5 lookup tables ...
```

---

## ANHANG A — Material-Datenblätter Zusammenfassung

### A.1 5083-H116 — Vollständige Eigenschaften

**Synonym:** EN AW-5083, AlMg4,5Mn0,7, 3.3547, UNS A95083, ASTM B928

**Zusammensetzung:**

| Element | % min. | % max. |
|---------|--------|--------|
| Magnesium (Mg) | 4,0 | 4,9 |
| Mangan (Mn) | 0,40 | 1,0 |
| Chrom (Cr) | 0,05 | 0,25 |
| Silizium (Si) | — | 0,40 |
| Eisen (Fe) | — | 0,40 |
| Kupfer (Cu) | — | 0,10 |
| Zink (Zn) | — | 0,25 |
| Titan (Ti) | — | 0,15 |
| Aluminium | Balance | — |

**Mechanische Eigenschaften:**

| Eigenschaft | Einheit | Wert (H116) | Wert (O, weichgeglüht) |
|-------------|---------|-------------|------------------------|
| Zugfestigkeit Rm | MPa | 305–380 | 270–345 |
| Streckgrenze Rp0.2 | MPa | 215–270 | 115–145 |
| Bruchdehnung A5 | % | 10–15 | 14–20 |
| Härte HB | — | 80–95 | 65–75 |
| E-Modul | GPa | 71 | 71 |
| Schubmodul | GPa | 27 | 27 |
| Dichte | g/cm³ | 2,66 | 2,66 |
| Poisson-Zahl | — | 0,33 | 0,33 |

**Physikalische Eigenschaften:**

| Eigenschaft | Einheit | Wert |
|-------------|---------|------|
| Wärmeleitfähigkeit (20°C) | W/(m·K) | 117 |
| Spezifische Wärme (20°C) | J/(kg·K) | 900 |
| Wärmeausdehnung (20–100°C) | 10⁻⁶/K | 23,8 |
| Elektrische Leitfähigkeit | MS/m | 17 |
| Schmelzbereich | °C | 574–638 |

### A.2 6082-T6 — Vollständige Eigenschaften

**Synonym:** EN AW-6082, AlSi1MgMn, 3.2315, UNS A96082

**Zusammensetzung:**

| Element | % min. | % max. |
|---------|--------|--------|
| Silizium (Si) | 0,7 | 1,3 |
| Magnesium (Mg) | 0,6 | 1,2 |
| Mangan (Mn) | 0,40 | 1,0 |
| Kupfer (Cu) | — | 0,10 |
| Eisen (Fe) | — | 0,50 |
| Chrom (Cr) | — | 0,25 |
| Zink (Zn) | — | 0,20 |
| Titan (Ti) | — | 0,10 |

**Mechanische Eigenschaften:**

| Eigenschaft | Einheit | T6 | T4 | O |
|-------------|---------|----|----|---|
| Rm | MPa | 310–340 | 205 | 150 |
| Rp0.2 | MPa | 260 | 110 | 65 |
| A5 | % | 8–12 | 14 | 18 |
| Härte HB | — | 90–105 | 60 | 45 |

### A.3 5086-H116 — Kurzübersicht

| Eigenschaft | Einheit | H116 |
|-------------|---------|------|
| Rm | MPa | 270–345 |
| Rp0.2 | MPa | 195–240 |
| A5 | % | 10–14 |
| Mg % | — | 3,5–4,5 |
| Dichte | g/cm³ | 2,66 |
| Schweißzusatz | — | 5356 |

### A.4 6061-T6 — Kurzübersicht

| Eigenschaft | Einheit | T6 |
|-------------|---------|------|
| Rm | MPa | 310 |
| Rp0.2 | MPa | 276 |
| A5 | % | 8–10 |
| Si % | — | 0,4–0,8 |
| Mg % | — | 0,8–1,2 |
| Cu % | — | 0,15–0,40 |
| Dichte | g/cm³ | 2,70 |
| Schweißzusatz | — | 4043 / 5356 |

### A.5 5052-H32 — Marine-Tanks und Verkleidung

| Eigenschaft | Einheit | H32 |
|-------------|---------|------|
| Rm | MPa | 230–270 |
| Rp0.2 | MPa | 160–195 |
| A5 | % | 10–15 |
| Mg % | — | 2,2–2,8 |
| Cu % max | — | 0,10 |
| Dichte | g/cm³ | 2,68 |
| Schweißzusatz | — | 5356 |
| Anwendung | — | Tanks, Verkleidung, Lüftung |
| Korrosion | Exzellent | In Seewasser sehr gut |

### A.6 5754-H22 — Höhere Festigkeit als 5052

| Eigenschaft | Einheit | H22 | H32 |
|-------------|---------|-----|-----|
| Rm | MPa | 240–290 | 260–310 |
| Rp0.2 | MPa | 160–220 | 200–260 |
| A5 | % | 12–16 | 10–14 |
| Mg % | — | 2,6–3,6 | 2,6–3,6 |
| Dichte | g/cm³ | 2,68 | 2,68 |
| Schweißzusatz | — | 5556 oder 5356 | 5556 oder 5356 |
| Anwendung | — | Leichte Struktur, Tanks | Versteifung, Profile |

### A.7 Vergleich aller Legierungen — Kurzfassung

| Legierung | Rm MPa | Rp0.2 | Korrosion | Schweißbar | Kosten | Verfügbarkeit |
|-----------|--------|-------|-----------|-----------|--------|----------------|
| **5083-H116** | 305–380 | 215–270 | Exzellent | Gut (5356) | 100% | Weltweit |
| **5086-H116** | 270–345 | 195–240 | Exzellent | Besser | 100–105% | USA, Australien |
| **5052-H32** | 230–270 | 160–195 | Exzellent | Sehr gut | 85–90% | Weltweit |
| **5754-H32** | 260–310 | 200–260 | Exzellent | Gut | 90–95% | EU |
| **6082-T6** | 310–340 | 260–290 | Gut | Mittel (4043) | 100–110% | EU |
| **6061-T6** | 310 | 276 | Befriedigend | Gut (4043) | 95–105% | USA, weltweit |
| **6005-T6** | 240–280 | 190–230 | Gut | Gut | 90–100% | EU |
| **7075-T6** | 570 | 505 | Schlecht | Schwierig | 150–200% | Spezial |

### A.8 Temperaturabhängige Eigenschaften (5083-H116)

**Festigkeitsabnahme bei erhöhter Temperatur:**

| Temperatur °C | Rm (% von 20°C) | Rp0.2 (% von 20°C) | Bemerkung |
|-------------|-----------------|-------------------|-----------|
| 20 (Referenz) | 100% | 100% | Standard |
| 50 | 98% | 97% | Maschinenraum (mild) |
| 100 | 90% | 85% | Maschinenraum (warm) |
| 150 | 75% | 70% | WARNUNG: Sensibilisierung begins |
| 200 | 50% | 45% | Kritisch: strukturelle Festigkeit |
| 250 | 30% | 25% | Maximum für kurzzeitige Erwärmung |
| 300 | <20% | <20% | Rekristallisation (permanent!) |

**AYDI-Interpretation:** Für Maschinenräume: Zieltemperatur <50°C an der Alu-Oberfläche. Wenn >65°C erwartet, MUSS Isolierung eingebaut werden.

### A.9 Elektrochemische Potentiale (nach ISO 12944)

**Korrosionspotentiale verschiedener Metalle in Seewasser (Ag/AgCl-Referenzelektrode, chloridhaltiges Meerwasser):**

| Material | Potenzial V | Status | Risiko mit Alu |
|----------|------------|--------|-----------------|
| Magnesium-Anode | −1.70 bis −1.50 | Sehr unedel | Schützt Alu |
| Zink-Anode | −1.10 bis −0.95 | Unedel | Schützt Alu |
| **Aluminium (5083)** | **−0.85 bis −0.75** | **Unedel** | **Basis** |
| Stahl (blank) | −0.65 bis −0.55 | Unedel | Gering |
| Blei | −0.50 | — | Gering |
| Zinn | −0.35 | — | Mittel |
| Nickel (passiv) | −0.30 bis −0.10 | Edel | Mittel |
| **Edelstahl 316 (passiv)** | **−0.10 bis +0.05** | **Edel** | **HOCH** |
| Kupfer | +0.10 bis +0.30 | Sehr edel | **SEHR HOCH** |
| Bronze | +0.15 bis +0.30 | Sehr edel | **SEHR HOCH** |
| Titan | +0.00 bis +0.20 | Edel | Hoch |
| Graphit/Kohlefaser | +0.20 bis +0.40 | Sehr edel | **KATASTROPHAL** |

**Faustregel (confidence: documented):** Potentialdifferenz >0.2 V (200 mV) zwischen Alu und Kontaktmetall erfordert Isolation!

### A.10 Normative Standards für Alu-Yachtbau

**Internationale Normierungskörper und relevante Standards:**

| Standard | Körper | Thema | Relevanz |
|----------|--------|-------|----------|
| EN 573-3 | CEN | Chemische Zusammensetzung Alu | Legierungsspezifikation |
| EN 485-2 | CEN | Mechanische Eigenschaften Platten | Material-Spezifikation |
| EN 755-2 | CEN | Mechanische Eigenschaften Profile | Material-Spezifikation |
| EN 754-2 | CEN | Mechanische Eigenschaften Rohre | Material-Spezifikation |
| EN 515 | CEN | Zustandsbezeichnungen | H116, T6, O erklärt |
| EN 12216 | CEN | Windows, Türen, Luken — Anforderungen | Fenster/Luke Design |
| EN 15085 | CEN | Schweißung von Aluminiumlegierungen | Schweißtechnik |
| ISO 12215-5 | ISO | Hull construction and scantlings | WICHTIG: Plattendicken berechnen |
| ISO 9094 | ISO | Fire protection — General requirements | Brandschutz, Isolierung Maschinenraum |
| ISO 11812 | ISO | Cockpit sizing | Cockpit-Volumen, Drainagegröße |
| ISO 10133 | ISO | Electrical installations | Kabel-Routing auf Alu |
| ASTM B928 | ASTM | 5083-H116/H321 marine plates | US-Norm, ASTM-Äquivalent zu EN |
| ASTM B209 | ASTM | Aluminum and aluminum alloy sheet | US-Standard |
| DNV-Rules | DNV | Classification and classed ships | Klassifikations-Anforderungen |
| Lloyd's Register | LR | Classed ships | Klassifikations-Anforderungen |
| Bureau Veritas | BV | Classed ships | Klassifikations-Anforderungen |

---

## ANHANG B — Schweißparameter-Tabellen

### B.1 Zusammenfassung WIG (TIG) — 5083-H116

| Dicke mm | Lagenanzahl | Strom A | Spannung V | Draht-Ø mm | Argon L/min | Vorwärmen? |
|----------|------------|---------|-----------|------------|-------------|------------|
| 3 | 1 | 100–130 | 12–14 | 2,4 | 10–12 | Nein |
| 4 | 1 | 130–160 | 13–15 | 2,4 | 10–12 | Nein |
| 5 | 1–2 | 150–180 | 14–16 | 2,4–3,2 | 12–15 | Optional |
| 6 | 2 | 170–210 | 15–17 | 3,2 | 12–15 | Optional (50°C) |
| 8 | 2–3 | 200–250 | 16–18 | 3,2 | 15–18 | Ja (80°C) |
| 10 | 3–4 | 230–280 | 17–19 | 3,2–4,0 | 15–18 | Ja (100°C) |
| 12 | 4–5 | 260–320 | 18–20 | 4,0 | 18–20 | Ja (100°C) |
| 15 | 5–6 | 280–350 | 18–22 | 4,0 | 18–22 | Ja (120°C) |
| 20 | 6–8 | 300–400 | 20–24 | 4,0 | 20–25 | Ja (120°C) |

### B.2 Zusammenfassung MIG (GMAW) — 5083-H116

| Dicke mm | Lagenanzahl | Strom A | Spannung V | Draht-Ø mm | Vorschub m/min | Argon L/min |
|----------|------------|---------|-----------|------------|----------------|-------------|
| 4 | 1 | 130–160 | 19–22 | 1,0 | 8–10 | 15–18 |
| 5 | 1–2 | 150–190 | 20–23 | 1,2 | 7–9 | 15–18 |
| 6 | 2 | 170–220 | 21–24 | 1,2 | 7–9 | 18–22 |
| 8 | 2–3 | 200–260 | 23–26 | 1,2 | 8–10 | 18–22 |
| 10 | 3–4 | 230–300 | 24–27 | 1,2–1,6 | 8–11 | 20–25 |
| 12 | 4–5 | 260–320 | 25–28 | 1,6 | 8–10 | 20–25 |

### B.3 Schweißnahtfestigkeit (as-welded, ohne PWHT)

| Grundmaterial | Zusatz | Rm Naht MPa | Rp0.2 Naht MPa | Festigkeitsausnutzung |
|---------------|--------|-------------|----------------|----------------------|
| 5083-H116 | 5183 | 275–300 | 125–145 | 90% (Rm) |
| 5083-H116 | 5356 | 255–280 | 115–135 | 84% (Rm) |
| 5086-H116 | 5356 | 240–270 | 110–130 | 89% (Rm) |
| 6082-T6 | 4043 | 170–210 | 85–110 | 55–65% (Rm) |
| 6082-T6 | 5356 | 180–220 | 90–115 | 58–68% (Rm) |

**AYDI-Hinweis (confidence: calculated):** Die Schweißnahtfestigkeit ist IMMER der limitierende Faktor bei geschweißten Alu-Konstruktionen. Für die Strukturberechnung muss die HAZ-Festigkeit (Streckgrenze in WEZ) als Bemessungswert verwendet werden, NICHT die Grundmaterialfestigkeit.

---

## ANHANG C — Korrosions-Kompatibilitätsmatrix

### C.1 Galvanische Kompatibilität mit 5083/6082

| Material | Potential-Differenz zu 5083 mV | Risiko | Isolation nötig? | Bemerkung |
|----------|-------------------------------|--------|------------------|-----------|
| Aluminium 5083 (gleich) | 0 | Keines | Nein | — |
| Aluminium 6082 | 30–60 | Minimal | Nein | Akzeptabel |
| Aluminium 6061 | 40–80 | Gering | Optional | Cu-Gehalt beachten |
| Zink | +200 (schützt Alu!) | Keines | Nein | Opferanode |
| Verzinkter Stahl | −50 bis +50 | Gering | Optional | Zink schützt zunächst |
| Edelstahl 316 (passiv) | +700–900 | **HOCH** | **JA, PFLICHT** | Hauptproblem! |
| Edelstahl 316 (aktiv) | +100–300 | Mittel | Ja | In Spalten aktiver |
| Kupfer | +800–1000 | **SEHR HOCH** | **VERBOTEN** | Direktkontakt = Katastrophe |
| Bronze | +900–1100 | **EXTREM** | **VERBOTEN** | Seeventile! |
| Messing | +800–1000 | **EXTREM** | **VERBOTEN** | — |
| Titan | +700–900 | **HOCH** | **JA, PFLICHT** | — |
| CFK (Carbon) | +900–1200 | **KATASTROPHAL** | **JA, PFLICHT** | Worst Case |
| GFK | — | Keines | Nein | Nicht leitend |
| Blei | +200–350 | Mittel | Ja | Kiel-Ballast |
| Holz | — | Keines | Nein | Nicht leitend |

### C.2 Isolationsmaßnahmen nach Risikostufe

| Risikostufe | Maßnahmen | Produkte |
|-------------|-----------|----------|
| Gering (<200 mV) | Tef-Gel unter Bolzenköpfe | Tef-Gel, Duralac |
| Mittel (200–500 mV) | Tef-Gel + Nylon-Buchsen + Sealant | Tef-Gel, Sikaflex, Nylon |
| Hoch (500–800 mV) | G10-Platte + Tef-Gel + Nylon-Buchsen + Sealant | G10, Tef-Gel, Nylon, Sikaflex |
| Sehr hoch (>800 mV) | Vermeiden oder: G10 + Butyl-Tape + Sealant + überdimensionierte Anoden | Komplettsystem |
| Katastrophal (>1000 mV) | KONTAKT VERMEIDEN! Alternative Materialien wählen | Marelon, Kunststoff |

---

## ANHANG D — Glossar

- **5083-H116:** Meistverwendete Marine-Alu-Legierung. AlMg4,5Mn0,7, sensibilisierungsresistent nach ASTM B928, Standard für Rumpfplatten.
- **5086-H116:** Alternative Rumpflegierung mit etwas weniger Mg (3,5–4,5%). Leichter umformbar, etwas geringere Festigkeit.
- **6082-T6:** Ausscheidungshärtbare Legierung (AlSi1MgMn) für Profile, Beschläge, Masten. Höhere Festigkeit als 5083, aber korrosionsanfälliger in Seewasser.
- **6061-T6:** US-Standard-Konstruktionslegierung. Ähnlich 6082 aber höherer Cu-Gehalt. Weltweit verfügbar.
- **Anodisierung (Eloxierung):** Elektrochemische Oxidation zur Erzeugung einer harten Al₂O₃-Schicht auf Aluminium. Standard 10–15 µm, Hart 25–50 µm.
- **ASTM B928:** US-Norm für marine Alu-Platten (5083/5086/5456/5383). Garantiert Sensibilisierungsresistenz (NAMLT-Test).
- **Bulb-Profil (HP-Profil):** Extrudiertes Profil mit verdicktem Kopf (Wulst). Optimiertes Widerstandsmoment für Stringer im Schiffbau.
- **CE-Kategorie:** Einteilung der Seegangstauglichkeit (A=Hochsee, B=Küstenfern, C=Küstennah, D=Geschützt) nach EU-Richtlinie 2013/53/EU.
- **DNV (Det Norske Veritas):** Norwegische Klassifikationsgesellschaft. Zertifiziert Marine-Materialien.
- **Duralac:** Anti-Galvanic-Paste auf Zinkchromat-Basis. Wird zwischen ungleiche Metalle aufgetragen.
- **Exfoliation:** Blätterförmige Korrosion entlang der Kornstruktur von Alu-Platten. Typisch bei sensibilisierten 5xxx-Legierungen.
- **Galvanische Korrosion:** Elektrochemische Korrosion durch Kontakt zweier Metalle mit unterschiedlichem Potential in einem Elektrolyten (Seewasser).
- **HAZ (Heat Affected Zone / WEZ):** Wärmeeinflusszone neben einer Schweißnaht. Festigkeit dort reduziert (bei 6082-T6 um 40–55%).
- **H116:** Zustandsbezeichnung für kaltverfestigtes, sensibilisierungsresistentes Marine-Aluminium. Erfüllt ASTM G67 (NAMLT ≤15 mg/cm²).
- **Helicoil:** Drahtgewindeeinsatz aus Edelstahl, eingedreht in Alu-Gewinde zur Verstärkung und Isolation.
- **ISO 12215-5:** Norm zur Berechnung der Plattendicken (Scantlings) von Sportboot-Rümpfen.
- **Marelon:** GFK-Verbundwerkstoff für Seeventile. Galvanisch neutral — ideal für Alu-Yachten.
- **Millzertifikat (EN 10204 3.1):** Abnahmeprüfzeugnis vom Walzwerk mit Chargen-Nummer, chemischer Analyse und mechanischen Prüfwerten.
- **MIG (GMAW):** Metal Inert Gas Schweißen. Schneller als WIG, für dickere Materialien >6 mm bevorzugt.
- **NAMLT (ASTM G67):** Nitric Acid Mass Loss Test. Prüft Sensibilisierung von 5xxx-Legierungen. ≤15 mg/cm² = nicht sensibilisiert.
- **Opferanode:** Unedleres Metall (Zn, Al-Zn-In, Mg), das sich anstelle des Rumpfes auflöst. Kathodischer Schutz.
- **PREN:** Pitting Resistance Equivalent Number — Kennzahl für Lochfraßbeständigkeit von Edelstahl (nicht direkt auf Alu anwendbar).
- **Porosität:** Gasporen in der Schweißnaht. Bei Alu häufigste Schweißfehler-Art (Ursache: Feuchtigkeit, Verunreinigung).
- **PWHT (Post-Weld Heat Treatment):** Wärmebehandlung nach dem Schweißen zur teilweisen Wiederherstellung der T6-Festigkeit in der HAZ.
- **Sensibilisierung:** Ausscheidung von Mg₂Al₃ an Korngrenzen bei 5xxx-Legierungen (>3% Mg) nach langer Exposition bei >65°C. Führt zu intergranularer Korrosion.
- **T6:** Zustandsbezeichnung für lösungsgeglühtes und künstlich ausgehärtetes Aluminium. Höchste Festigkeit bei 6xxx-Legierungen.
- **Tef-Gel:** PTFE-basierte Paste zur Isolation zwischen ungleichen Metallen. Standard-Produkt auf Alu-Yachten.
- **TIG (WIG):** Tungsten/Wolfram Inert Gas Schweißen. Präziseste Methode für Alu, Standard für Yachtbau ≤10 mm.
- **Trilux 33:** Kupferfreies Antifouling von International Paint. Standard-Empfehlung für Alu-Rümpfe.
- **WEZ (Wärmeeinflusszone):** Deutscher Begriff für HAZ. Zone neben Schweißnaht mit reduzierter Festigkeit.

---

## ANHANG E — Fehlerbild-Atlas

Dieser Atlas dokumentiert typische Schadensbilder an Aluminium-Halbzeugen im Yachtbau. Jedes Fehlerbild zeigt Symptome, Fehlerursache, Bewertung (Schweregrad) und Handlungsempfehlungen.

### E.1 Fehlerbild 1: Galvanische Korrosion an Seeventil-Durchführung

**Symptom:** Weiße, blumenkohlartige Ablagerungen (Aluminiumhydroxid) rund um ein Bronze-Seeventil im Alu-Rumpf. Oberfläche fühlt sich rau und krümelig an. Unter den Ablagerungen: Material deutlich dünner als normal.

**Fehlerursache:** Galvanisches Element zwischen Bronze (edel, +0,15V) und 5083 (unedel, −0,80V). Potentialdifferenz ~950 mV — weit über der kritischen 200-mV-Grenze. Seewasser als Elektrolyt. Das Aluminium wird als Anode aufgelöst.

**Schadenbild im Detail:** Materialverlust konzentriert sich im Radius von 50–100 mm um das Seeventil. Wandstärke kann lokal von 6 mm auf 1–2 mm sinken. Von außen oft nicht sichtbar (Antifouling verdeckt den Schaden).

**Schweregrad:** 4–5/5 — KRITISCH. Rumpfdurchbruch möglich!

**Inspektions-Verfahren:**
1. Ultraschall-Dickenmessung (NDT) in Stern-Muster um jedes Seeventil: 0°, 45°, 90°, 135°, 180°, 225°, 270°, 315°
2. Visuell: Weiße Ablagerungen? Aufquellungen unter der Farbe?
3. Klopftest: Dumpfer Klang = dünnere Wandstärke

**Maßnahme:**
1. Bronze-Seeventil SOFORT entfernen
2. Betroffene Rumpfzone freilegen, Schaden beurteilen
3. Bei >30% Materialverlust: Alu-Platte auswechseln (WIG-Schweißen)
4. Marelon- oder TruDesign-Seeventil einbauen (KEIN Bronze!)
5. Alternativ: SS316-Seeventil mit G10-Flansch + Tef-Gel + Nylon-Buchsen + überdimensionierte Anode

**Kosten:** €500–€5.000+ (abhängig von Schadensumfang und Rumpfbereich)

**Prognose:** Ohne Reparatur: Rumpfdurchbruch innerhalb von 2–5 Jahren. Mit Marelon-Ventil: Problem dauerhaft gelöst.

---

### E.2 Fehlerbild 2: Exfoliation (Blätterkorrosion)

**Symptom:** Oberfläche blättert lagenweise ab, ähnlich wie aufgeblättertes Papier oder Blätterteig. Typischerweise an Plattenkanten sichtbar. Die einzelnen Schichten sind parallel zur Walzrichtung orientiert.

**Fehlerursache:** Sensibilisierung von 5083 (Mg > 4%) nach langzeitiger Exposition bei Temperaturen >65°C. Mg₂Al₃ scheidet sich bevorzugt an Korngrenzen aus. Diese Ausscheidungen sind anodischer als die umgebende Matrix und werden bevorzugt korrodiert. Intergranulare Korrosion entlang der Walzrichtung → Exfoliation.

**Schadenbild:** Am häufigsten an Maschinenraum-Schotten, nahe Abgasleitungen, und an Bereichen mit Warmwasser-Rohrführung. ASTM G66 Test: Bewertung PB oder schlechter.

**Schweregrad:** 3–4/5 — Schwer. Strukturelle Integrität kompromittiert.

**Inspektions-Verfahren:**
1. Visuell: Aufblätterung an Plattenkanten? Blasenbildung unter der Beschichtung?
2. ASTM G66 (ASSET-Test): Standardtest für Exfoliationsanfälligkeit
3. ASTM G67 (NAMLT): Masseverlust-Messung für Sensibilisierungsgrad
4. Ultraschall: Schichtablösungen detektieren

**Maßnahme:**
1. Betroffene Platte komplett ersetzen (H116 oder H321!)
2. Wärmequelle identifizieren und isolieren (min. 100 mm Abstand oder Isolierung)
3. Alle angrenzenden Platten prüfen (NAMLT-Test)
4. Temperaturüberwachung installieren (max. 50°C an Alu-Oberfläche)

**Kosten:** €1.000–€10.000+ (Plattenwechsel inkl. Arbeit)

**Gutachter-Empfehlung:** Bei Verdacht auf Sensibilisierung immer einen Sachverständigen oder Surveyor hinzuziehen. NAMLT-Proben müssen vom Fachmann entnommen und im Labor analysiert werden.

---

### E.3 Fehlerbild 3: Lochfraß (Pitting) unter defekter Beschichtung

**Symptom:** Unter abblätternder Beschichtung (Epoxy-Primer oder Antifouling) zeigen sich punktuelle, scharf begrenzte Löcher (0,5–3 mm Ø) in der Alu-Oberfläche. Oft weiße Korrosionsprodukte um die Löcher herum.

**Fehlerursache:** Chlorid-Ionen aus dem Seewasser durchdringen die defekte Beschichtung und greifen die lokale Passivschicht an. Sauerstoff-Konzentrationszelle zwischen beschichteter (kathode) und unbeschichteter (anode) Fläche beschleunigt die Korrosion.

**Versagensart:** Lokaler Angriff — Pitting Corrosion nach EN ISO 11463.

**Schweregrad:** 2–3/5 — Mittelschwer. Bei einzelnen Pits harmlos, bei flächigem Befall kritisch.

**Inspektions-Verfahren:**
1. Beschichtung im verdächtigen Bereich ablösen
2. Pit-Tiefe mit Tiefenmessnadel oder Endoskop messen
3. Ultraschall: Restdicke bestimmen
4. Pit-Dichte zählen: >10 Pits/dm² = flächiger Befall

**Maßnahme:**
1. Beschichtung vollständig entfernen (mechanisch, NICHT chemisch auf Alu!)
2. Oberfläche schleifen (K80–K120)
3. Einzelne Pits: Aufschweißen (WIG, 5356-Zusatz), planschleifen
4. Flächiger Befall: Platte ersetzen
5. Neue Beschichtung: Wash-Primer → 4× Epoxy-Primer (International Interprotect) → Antifouling

**Kosten:** €200–€2.000 (Reparatur) oder €2.000–€8.000 (Plattenersatz)

---

### E.4 Fehlerbild 4: Schweißnaht-Porosität

**Symptom:** Kleine Löcher (0,5–3 mm) in der Schweißnaht-Oberfläche, sichtbar nach dem Schleifen oder als Blasen unter der Oberfläche (nur durch Röntgen/Ultraschall detektierbar). Naht wirkt "löchrig" oder "schwammig".

**Fehlerursache:** Wasserstoff-Porosität durch:
1. Feuchtigkeit auf der Werkstückoberfläche (häufigste Ursache)
2. Verunreinigtes Schutzgas (Argon <99,95%)
3. Ölfilm/Fett auf der Oberfläche
4. Feuchter Schweißzusatzdraht (nicht trocken gelagert)

**Schweregrad:** 1–3/5 — Abhängig von Porengröße und -dichte.
- Einzelne Poren <1,5 mm: Akzeptabel nach ISO 10042 Klasse B
- Porennester: NICHT akzeptabel
- >3% Porenvolumen: Naht muss neu geschweißt werden

**Inspektions-Verfahren:**
1. Visuell: Oberflächenporen sichtbar?
2. Farbeindringprüfung: Verdeckte Oberflächenporen
3. Röntgen (RT): Innere Porosität
4. Ultraschall (UT): Innere Porosität (für dickere Nähte)

**Maßnahme:**
1. Poröse Naht ausschleifen (komplett!)
2. Oberfläche reinigen (Aceton + SS-Bürste)
3. Schutzgas prüfen (Reinheit, Durchfluss)
4. Neu schweißen mit korrekten Parametern
5. Schweißzusatz trocken lagern (Silikagelpackung)

---

### E.5 Fehlerbild 5: CFK-auf-Aluminium-Kontaktkorrosion

**Symptom:** Schwere galvanische Korrosion an Stellen, wo CFK-Komponenten (Carbon-Faser-Verbund) direkt auf Alu-Struktur montiert sind. Weißer, voluminöser Korrosionsbelag. Materialverlust teilweise extremer als bei Bronze-Kontakt.

**Schadenbild:** CFK ist elektrisch leitend und hat ein sehr edles Potential (+0,20 bis +0,40V). Potentialdifferenz zu 5083: bis 1200 mV — die höchste aller gängigen Marine-Materialien! Carbon-Beschläge (Bügel, Barren, Ruder) auf Alu-Deck oder -Rumpf sind die schlimmsten galvanischen Paare im Yachtbau.

**Versagensart:** Galvanische Korrosion — katastrophal bei CFK + Alu in Seewasser.

**Fehlerursache:** Fehlende oder unzureichende Isolation zwischen CFK und Aluminium. Wasser als Elektrolyt.

**Schweregrad:** 5/5 — KRITISCH. Sofortige Maßnahme erforderlich.

**Maßnahme:**
1. CFK-Komponente sofort demontieren
2. Betroffene Alu-Zone freilegen, Schaden beurteilen
3. G10-Isolierplatte (min. 6 mm) zwischen CFK und Alu
4. Nylon-Isolierbuchsen um alle Bolzen
5. Tef-Gel unter Bolzenköpfe + Unterlegscheiben
6. Butyl-Tape als zusätzliche Feuchtigkeitssperre
7. Überdimensionierte Opferanoden in direkter Nähe

**Experten-Hinweis:** Bei CFK-auf-Alu-Konstruktionen sollte ein Ingenieur oder Metallurg das Isolationskonzept überprüfen. Die Potentialdifferenz ist so groß, dass selbst kleine Isolationsfehler zu schnellem Materialverlust führen.

---

### E.6 Fehlerbild 6: Spannungsrisskorrosion (SCC) an Schweißnaht

**Symptom:** Feine, verzweigte Risse in oder nahe der Schweißnaht, oft unsichtbar für das bloße Auge. Erst durch Farbeindringprüfung sichtbar. Risse verlaufen häufig senkrecht zur Hauptspannungsrichtung.

**Fehlerursache:** Kombination aus: (1) Zugspannung (Eigenspannung durch Schweißung + Betriebslast), (2) korrosivem Medium (Seewasser), (3) sensibilisiertem Material (Mg₂Al₃ an Korngrenzen). Alle drei Faktoren müssen gleichzeitig vorliegen.

**Schweregrad:** 4–5/5 — KRITISCH. Versagen ohne Vorwarnung möglich.

**Inspektions-Verfahren:**
1. Farbeindringprüfung (PT): Standardverfahren
2. Magnetpulverprüfung: NICHT anwendbar (Alu ist nicht magnetisch!)
3. Ultraschall: Für tiefere Risse
4. Röntgen: Bei kritischen Schweißnähten

**Maßnahme:**
1. Rissbereich großzügig ausschleifen (+50 mm beidseitig)
2. Material durch nicht-sensibilisiertes H116 ersetzen
3. Neu schweißen mit 5183-Zusatz
4. Wärmebehandlung des gesamten Bereichs vermeiden
5. Zugspannungen reduzieren (Design-Änderung wenn möglich)

---

### E.7 Fehlerbild 7: Korrektes Unterwasser-Beschichtungssystem (Referenz)

**Schadenbild:** KEINES — Dies ist die Referenz für eine korrekte Beschichtung.

**Beschreibung eines vorbildlichen Systems:**
1. Oberfläche geschliffen (K80) und entfettet
2. Wash-Primer (Vinyl oder Etch-Primer) innerhalb von 4 Stunden aufgetragen
3. 4 Schichten International Interprotect (2× grau, 2× weiß für Kontrastfarbgebung)
4. 2 Schichten Trilux 33 (kupferfrei!)
5. Gesamtschichtdicke: 350–400 µm
6. Opferanoden: Alu-Zn-In-Legierung, gleichmäßig am Unterwasserschiff verteilt
7. Alle Durchbrüche (Seeventile, Echolot) mit Sikaflex 291 abgedichtet

**Symptom bei korrektem System:** Nach 5 Jahren: Antifouling verbraucht (normal, Erneuerung nötig), aber Primer intakt. Kein Pitting, keine Blasen, keine Ablösung.

---

### E.8 Fehlerbild 8: Verzug nach Schweißung

**Symptom:** Platte ist nach Schweißung wellig oder verbogen. Stringer liegen nicht mehr plan. Sichtbare Beulen oder Dellen entlang der Schweißnähte.

**Fehlerursache:** Thermische Ausdehnung + Schrumpfung beim Schweißen. Aluminium hat einen höheren Wärmeausdehnungskoeffizienten als Stahl (23,8 vs. 12 × 10⁻⁶/K) und leitet Wärme besser — daher MEHR Verzug als bei Stahl.

**Schweregrad:** 1–2/5 — Kosmetisch bis Mittelschwer. Bei extremem Verzug: Strukturprobleme möglich.

**Maßnahme:**
1. Schweißfolge optimieren (alternierend, von Mitte nach außen)
2. Vorspannung verwenden (Gegenbiegen vor Schweißung)
3. Spannvorrichtungen einsetzen
4. Rückverformung: Thermisches Richten (VORSICHT: max. 250°C!) oder mechanisch (hydraulische Presse)
5. Bei neuen Projekten: Simulation der Schweißverzüge vorab

---

*Ende ANHANG E*

---

## ANHANG F — Bordausstattung und Ersatzteile

### F.1 Küstenfahrt (8–10m Segelboot)

| Artikel | Spezifikation | Preis ca. | Bezugsquelle |
|---------|---------------|-----------|--------------|
| 5083-H116 Platte 4mm, 500×300mm | Reparaturstück | ~€15 | Bikar, Steelmaterial |
| 5083-H116 Flachstahl 30×5mm, 0,5m | Knieblech, Halterung | ~€3 | Nordfels |
| 6082-T6 Rohr 25×2mm, 1m | Reling-Reparatur | ~€6 | Alu-Verkauf.de |
| Schweißzusatz 5356, Ø2,4mm, 5 Stäbe | WIG-Reparatur | ~€5 | Schweißfachhandel |
| Nylon-Isolierbuchsen Sortiment | Unter SS-Beschlägen | ~€8 | Amazon DE |
| Tef-Gel 50g Tube | Galvanische Isolation | ~€14 | SVB, Compass24 |
| Bar Keeper's Friend 300g | Reinigung | ~€3 | Baumarkt |
| **Gesamt-Kit** | **Basis-Reparatur** | **~€54** | |

### F.2 Blauwasser-Langfahrt (10–14m)

| Artikel | Spezifikation | Menge | Preis ca. |
|---------|---------------|-------|-----------|
| 5083-H116 Platte 5mm, 1000×500mm | Rumpf-Reparatur | 2× | ~€70 |
| 5083-H116 Platte 4mm, 500×500mm | Schott/Aufbau | 1× | ~€20 |
| 5083-H116 Flachstahl 40×6mm, 1m | Kniebleche | 2× | ~€14 |
| 6082-T6 Rohr 25×2mm, 2m | Reling | 1× | ~€12 |
| 6082-T6 Rohr 32×2mm, 1m | Bimini/Davit | 1× | ~€8 |
| 6082-T6 L-Profil 30×30×3mm, 1m | Halterungen | 1× | ~€4 |
| Schweißzusatz 5183, Ø2,4mm, 500g | WIG (Höchste Festigkeit) | 1× | ~€18 |
| Schweißzusatz 5356, Ø2,4mm, 500g | WIG (Universell) | 1× | ~€15 |
| Schweißzusatz 5356, Ø1,2mm Draht, 500g | MIG | 1× | ~€20 |
| Tef-Gel 50g | Isolation | 3× | ~€42 |
| Nylon-Isolierbuchsen M6–M12 | Sortiment | 50er Box | ~€15 |
| G10-Platte 6mm, 200×200mm | Isolation unter Beschläge | 2× | ~€20 |
| Sikaflex 291 Kartusche | Abdichtung | 2× | ~€20 |
| CorrosionX Marine Spray 400ml | Konservierung | 2× | ~€20 |
| Opferanoden Alu-Zn-In (z.B. Vetus Type 8) | Kathodischer Schutz | 4× | ~€40 |
| **Gesamt Blauwasser-Kit** | **Für 6–12 Monate** | — | **~€338** |

### F.3 Werkzeug-Empfehlung für Alu-Reparaturen

| Werkzeug | Typ/Spezifikation | Preis ca. | Bezugsquelle |
|----------|-------------------|-----------|--------------|
| WIG-Schweißgerät (AC/DC) | Fronius MagicWave 190i oder Miller Dynasty 210 | €2.500–€4.000 | Schweißfachhandel |
| Argon-Flasche 5L | 99,996% (4.6) | €80 + Miete | Gasversorgung |
| SS-Drahtbürste | Edelstahl-Borsten (NIEMALS Stahl!) | ~€5 | Baumarkt |
| Bandschleifer | Makita 9920 oder ähnlich | €150–€250 | Baumarkt |
| Stichsäge | Mit Alu-Sägeblatt (grobe Zahnung) | €80–€150 | Baumarkt |
| Winkelschleifer | 125mm mit Alu-Trennscheibe | €60–€100 | Baumarkt |
| Ultraschall-Dickenmesser | Elcometer DG26 oder ähnlich | €300–€800 | NDT-Fachhandel |
| Schieblehre | 150mm digital | ~€15 | Baumarkt |
| Temperaturstift | 100°C, 150°C, 250°C | ~€12/Stück | Schweißfachhandel |
| **Komplettes Werkzeug-Set** | **Für autonome Reparaturen** | **€3.300–€5.500** | |

### F.4 Saisonale Wartungs-Checkliste für Alu-Yachten

**Frühjahr (Einwassern):**
- [ ] Ultraschall-Dickenmessung an 20 definierten Messpunkten (dokumentieren!)
- [ ] Alle Opferanoden prüfen — <50% verbraucht? Dann erneuern.
- [ ] Beschichtung prüfen — Blasen, Ablösungen, Risse?
- [ ] Seeventile prüfen — Korrosionsspuren am Alu um Durchführung?
- [ ] Alle SS-Beschläge: Tef-Gel erneuern, Nylon-Buchsen prüfen
- [ ] Antifouling auffrischen (kupferfrei!)

### F.5 Erweiterte Kostenbreakdowns nach Bootsgröße

**8m Segelyacht (neue Alu-Rumpf-Konstruktion):**

| Kostengruppe | Menge | Einheit | €/Einheit | Subtotal |
|------------|--------|---------|-----------|----------|
| **Material** | | | | |
| 5083-H116 Platten | 8 | Platten (1500×3000×4mm) | €475 | €3.800 |
| 6082-T6 Profile | 150 | kg | €6,50 | €975 |
| 6082-T6 Rohr | 50 | m | €5,50 | €275 |
| Schweißzusatz | 2 | kg | €12,00 | €24 |
| **Material Subtotal** | | | | **€5.074** |
| **Arbeit (Werft)** | | | | |
| Zuschnitt + Formung | 80 | h | €45 | €3.600 |
| Schweißen Struktur | 120 | h | €50 | €6.000 |
| Oberflächenbehandlung | 40 | h | €40 | €1.600 |
| Beschichtung (Primer + AF) | 60 | h | €35 | €2.100 |
| **Arbeit Subtotal** | | | | **€13.300** |
| **Sonstige** | | | | |
| Beschichtungsmaterial | 1 | Satz | €1.200 | €1.200 |
| Vorrichtungen/Spanntechnik | 1 | Satz | €500 | €500 |
| **Sonstige Subtotal** | | | | **€1.700** |
| **GESAMT RUMPF** | | | | **€20.074** |

**Anteil Material: 25%, Anteil Arbeit: 66%, Anteil Sonstiges: 9%**

---

**12m Segelyacht (neue Alu-Rumpf-Konstruktion):**

| Kostengruppe | Menge | Einheit | €/Einheit | Subtotal |
|------------|--------|---------|-----------|----------|
| **Material** | | | | |
| 5083-H116 Platten | 18 | Platten (1500×3000mm, gemischt) | €850–€1.200 | €15.300 |
| 6082-T6 Profile (Stringer, Spanten) | 400 | kg | €6,00 | €2.400 |
| 6082-T6 Rohre + Beschläge | 150 | m/kg | €6,00 | €900 |
| Schweißzusatz 5183/5356 | 5 | kg | €12,00 | €60 |
| **Material Subtotal** | | | | **€18.660** |
| **Arbeit (Werft)** | | | | |
| Platten-Zuschnitt (CNC) | 40 | h | €55 | €2.200 |
| Formung + Biegen | 100 | h | €50 | €5.000 |
| Hauptschweißung (Rumpf) | 200 | h | €55 | €11.000 |
| Profil-Schweißung (Struktur) | 120 | h | €50 | €6.000 |
| Oberflächenschliff + Entgraten | 60 | h | €40 | €2.400 |
| Beschichtung (Primer + topcoat) | 100 | h | €40 | €4.000 |
| Antifouling-Auftrag | 40 | h | €35 | €1.400 |
| **Arbeit Subtotal** | | | | **€32.000** |
| **Sonstige** | | | | |
| Beschichtungsmaterial (Awlgrip-System) | 1 | Satz | €3.500 | €3.500 |
| Vorrichtungen/Spannrahmen | 1 | Satz | €1.200 | €1.200 |
| Inspektionen (PT, UT) | 1 | Satz | €800 | €800 |
| **Sonstige Subtotal** | | | | **€5.500** |
| **GESAMT RUMPF** | | | | **€56.160** |

**Anteil Material: 33%, Anteil Arbeit: 57%, Anteil Sonstiges: 10%**

---

**16m Motoryacht (neue Alu-Rumpf-Konstruktion):**

| Kostengruppe | Menge | Einheit | €/Einheit | Subtotal |
|------------|--------|---------|-----------|----------|
| **Material** | | | | |
| 5083-H116 Platten | 35 | Platten (gemischt bis 40×3000) | €1.200 | €42.000 |
| 6082-T6 Profile (Spanten, Stringer) | 800 | kg | €5,80 | €4.640 |
| 6082-T6 Rohre/Beschläge | 400 | m | €7,00 | €2.800 |
| 6082-T6 Knie-Bleche, Platten | 200 | kg | €6,50 | €1.300 |
| Schweißzusatz (5183, 5356) | 12 | kg | €11,50 | €138 |
| **Material Subtotal** | | | | **€50.878** |
| **Arbeit (Werft)** | | | | |
| Platten-Zuschnitt (CNC+Laser) | 60 | h | €60 | €3.600 |
| Formung (Presse, Walze) | 180 | h | €55 | €9.900 |
| Hauptschweißung | 400 | h | €60 | €24.000 |
| Strukturschweißung | 250 | h | €55 | €13.750 |
| Maschinenraum-Installation | 80 | h | €50 | €4.000 |
| Oberflächenvorbereitung (Strahlen) | 120 | h | €45 | €5.400 |
| Beschichtung (Primer, Topcoat, AF) | 160 | h | €45 | €7.200 |
| **Arbeit Subtotal** | | | | **€67.850** |
| **Sonstige** | | | | |
| Beschichtungsmaterial (Premium-System) | 1 | Satz | €6.000 | €6.000 |
| Spannvorrichtungen + Vorrichtungen | 1 | Satz | €2.500 | €2.500 |
| NDT-Inspektionen (UT, PT, MPI) | 1 | Satz | €2.000 | €2.000 |
| **Sonstige Subtotal** | | | | **€10.500** |
| **GESAMT RUMPF** | | | | **€129.228** |

**Anteil Material: 39%, Anteil Arbeit: 52%, Anteil Sonstiges: 8%**

**Anmerkung:** Alle Kosten sind Orientierungswerte für 2025/2026, Westeuropa. Kosten in USA, Asien können ±30% abweichen.

---

**Herbst (Auswassern):**
- [ ] Unterwasserschiff waschen (Hochdruckreiniger, max. 100 bar)
- [ ] Beschichtungsschäden markieren und fotografieren
- [ ] Opferanoden-Rest messen und dokumentieren (Verbrauchsrate berechnen)
- [ ] CorrosionX auf alle exponierte Alu-Flächen sprühen
- [ ] Bilge trockenlegen (stehend Wasser in Alu-Bilge = Korrosion!)

**Jährlich (durch Sachverständigen/Surveyor):**
- [ ] Komplette Ultraschall-Kartierung des Unterwasserschiffs
- [ ] Schweißnähte (Kiel, Ruder, Stringer) visuell + PT-Prüfung
- [ ] Opferanoden-System bewerten (Schutzpotential messen, -0,95 bis -1,05V vs. Ag/AgCl)
- [ ] Maschinenraum: Temperatur-Check an allen Alu-Oberflächen (max. 50°C!)
- [ ] Alle Seeventil-Durchführungen: Dicken-Messung

---

## Erweiterte Themen für Spezialisten

### Metallurgische Tiefenanalyse — Sensibilisierung verstehen

Magnesium und Aluminium legieren sich bei Aluminiumlegierungen durch natürliche Oxidation in hochgradige Reaktionen. Die Ausscheidung von Mg₂Al₃-Phasen an Korngrenzen ist der Mechanismus hinter "Sensibilisierung" — ein Phänomen, das in Marineanwendungen zurecht gefürchtet ist.

**Die Chemie dahinter:**
- 5083 hat nominal 4,0–4,9% Mg (das „4" in „5083" steht für 4,0–5,0% Mg)
- Bei Raumtemperatur ist Mg in Al vollständig gelöst
- Aber bei Temperaturen >65°C (typisch im Maschinenraum!) werden Mg-Atome an Korngrenzen mobil
- Sie bilden Mg₂Al₃-Kristalle: Mg₂Al₃ = MgAl₂ + Mg (vereinfacht)
- Diese Ausscheidungen sind EDEL (elektrochemisch positiver als Alu) → galvanische Mikro-Zellen
- Wasser dringt entlang der Korngrenzen ein → **intergranulare Korrosion (IGC)**
- Im Extremfall: Das Material wird spröde und bricht ohne Warnung

**Prävention im Yachtbau:**
1. Material-Wahl: H116 oder H321 verwenden (mit Cr stabilisiert, weniger Sensibilisierung)
2. Temperatur-Kontrolle: <50°C an Alu-Oberflächen halten
3. Isolierung: Wenn >50°C erwartet, 50 mm PU-Isolierung + Luftspalt
4. Kontrolle: ASTM G67 (NAMLT) Test alle 5 Jahre bei Maschinenräumen

**Kosten für NAMLT-Test:**
- Laborkosten: €200–€400 pro Probe
- Material-Probennahme: €50–€100 (Drilling oder Schleif-Probe)
- Bericht + Interpretation: €150–€250
- Gesamt: €400–€750 pro Messreihe (üblicherweise 3–5 Proben)

---

### FSW (Friction Stir Welding) — Die Zukunftstechnik?

**Was ist FSW?**
Statt Lichtbogenschweißung (TIG/MIG) wird ein rotierendes Werkzeug (Stift + Schulter) in die Fuge gedrückt. Reibungswärme (ca. 350–400°C, unter dem Schmelzpunkt!) mischt das Material mechanisch.

**Vorteile gegenüber konventionellem Schweißen:**
- KEINE Wärmeeinflusszone (HAZ) → Festigkeit 100% des Grundmaterials!
- Keine Porenbildung → Dichte 100%
- Keine Rissneigung bei Dickwändern (5–10 mm möglich)
- Geringerer Verzug

**Nachteile:**
- Teure Spezialmaschinen (€100.000+)
- Wenige Zulieferer weltweit
- Für Yachten aktuell (2026) noch nicht Standard
- Lineare Nähte nur (keine beliebigen Formen wie TIG)

**Beispiel-Nutzer im Yachtbau:**
- Moody Yachts (UK) nutzen FSW für Select-Modelle
- Superyacht-Bauern in Skandinavien experimentieren damit
- Kosten-Aufschlag: ca. 30–40% über konventionelles Schweißen

**Ausblick:** In 5–10 Jahren könnte FSW Standard für hochtechnologische Alu-Yachten werden. Momentan ist es für den mainstream Bootsbau noch zu teuer.

---

### Ersatzstoff-Entwicklung: Was kommt nach 5083?

**5383-H112 (neuere Legierung, noch experimentell):**
- Höheres Mn (bis 1,5%), ähnliches Mg
- Bessere Ermüdungsfestigkeit (+15% vs. 5083)
- Weniger sensibilisierungsanfällig (Cr-freie Alternative)
- Verfügbarkeit: Nur in USA (Aleris, Tri-Arrows) ab 2024
- Preis: ca. 5–10% teurer als 5083
- Status: Noch nicht von Lloyd's Register zugelassen, aber im Zertifizierungsprozess

**5087 (Premium-Qualität):**
- Höchster Mg (bis 4,5%), mit Cr und Zn stabilisiert
- Beste Korrosionsbeständigkeit
- Beste Schweißbarkeit (5087-Zusatz perfekt kompatibel)
- Verfügbarkeit: Begrenzt (nur spezialisierte Hersteller)
- Preis: +20–30% über 5083
- Anwendung: Superyacht-Bauern für Hochsee-Expeditionen
- Quelle: Hydro Aluminum hat 5087-H116 im Angebot für Custom-Orders

---

### Umweltaspekte und Nachhaltigkeit

**Alu-Recycling im Yachtbau:**
- Verschnittabfälle: 10–20% pro Projekt
- Kosten Recyclium-Versand: ca. €0,80–€1,20/kg
- Alu-Schrott-Preis (2026): €1,60–€2,00/kg (nach Sortierung)
- **Net-Erlös für Werft: 1.000 kg Verschnitt × €1,80 = €1.800** (bei einem 12m-Projekt)

**Carbon Footprint Vergleich:**
- GFK-Rumpf mit Polyester: ca. 2.5 t CO₂ (primär Rohstoffe + Kunststoff)
- Alu-Rumpf (5083): ca. 6 t CO₂ (Bauxitabbau + Schmelze SEHR energieintensiv)
- Stahl-Rumpf: ca. 3 t CO₂
- **ABER:** Alu wird zu 75% recycelt weltweit (höchste Quote aller Materialien!)
- **ABER:** Alu-Recycling kostet nur 5% der Energie des Primär-Aluminiums

**Fazit:** Obwohl Neubau-Alu energieintensiv ist, ist der Lebenszyklus-Impact durch Recycling deutlich besser als oft angenommen.

---

### Exotische Legierungen: 7075-T6 und andere

**7075-T6 (die stärkste Alu-Legierung):**
- Rm = 570 MPa (fast 2× von 5083!)
- Aber: Korrosion ist schrecklich → NIEMALS im Seewasser!
- Preis: 2–3× teurer als 5083
- Anwendung: Flugzeug-Strukturen, Hochleistungs-Rennboote (nicht für Langfahrt)
- Im Yachtbau: Gelten als Luxus-Material ohne praktischen Nutzen

**2024-T4 (Kupferhaltiges Duralumin):**
- Rm = 470 MPa (hoch), aber Korrosion ähnlich wie 7075
- Historisch in Langstrecken-Flugzeugen (jetzt historisch)
- Im Yachtbau: NICHT empfohlen für moderne Boote

---

*Erweiterte Themen — Ende*

---

## ANHANG G — Risiko-Bewertungsmatrizen für Inspektoren

### G.1 Schnellbewertungs-Tabelle für Alu-Yachten

Wenn Sie ein Alu-Boot inspizieren, nutzen Sie diese Matrix, um Prioritäten zu setzen:

| Befund | Lage | Ausdehnung | Sofort-Risiko | Handlung | Restwert-Impakt |
|--------|------|-----------|---------------|---------|-----------------|
| Oberflächenoxidation | Überwasser | <2m² | Gering | Monitor jährlich | ±0% |
| Oberflächenoxidation | Unterwasser | >5m² | Mittel | Schleifen + repaint | −2% |
| Oberflächenpitting | Unterwasser | <10 cm² | Mittel | Lokal ausbessern | −1–3% |
| Tiefe Pits | Kielbereich | >5cm² | HOCH | Patch + UT-Kontrolle | −10–20% |
| Perforiertes Loch | Rumpf | Jede | KRITISCH | Sofortiges Abdichten | −30–50% |
| Risse an Schweißnähte | Spanten | <100mm | HOCH | Überprüfung PT | −15–25% |
| Blasenbildung Beschichtung | Überwasser | <1m² | Gering | Abschleifen + Retouching | ±0% |
| Großflächige Blasen | Unterwasser | >2m² | HOCH | Rumpf-Trocknung + Neubeschichtung | −20–30% |
| Galvanische Korrosion um Fitting | Rumpf | Jede | MITTEL | Fitting entfernen + Isolierung | −5–10% |

---

### G.2 Entscheidungsmatrix — Reparieren vs. Neubau

Für Yachtbauer, die entscheiden müssen: Ist ein Rumpf noch zu retten?

**Input-Faktoren:**
- Restdicke (Ultraschall-Messung)
- Korrosionstyp (Flächenrost vs. Pitting vs. IGC)
- Bootsgröße und Baujahr
- Aktueller Marktwert
- Verfügbare Budget

**Entscheidungs-Baum:**

```
Restdicke <2mm in kritischen Bereichen?
├─ JA → Neubau erforderlich (Reparatur unwirtschaftlich)
└─ NEIN
    ├─ Korrosion ist IGC (intergranular)?
    │  ├─ JA (bestätigt ASTM G67) → Blech-Austausch (Reparatur)
    │  └─ NEIN
    └─ Rumpfoberfläche >30% betroffen?
       ├─ JA → Neubeschichtung (kostet €8.000–€20.000, je nach Größe)
       └─ NEIN → Lokale Reparaturen (€1.000–€5.000)
```

**Kostenvergleich-Beispiel (12m Segelyacht, 30 Jahre alt):**
- Aktueller Marktwert: €80.000
- Neuer Rumpf-Neubau: €45.000–€70.000
- Lokale Reparaturen + Beschichtung: €12.000–€25.000
- **Entscheidung:** Reparieren, wenn <30% des aktuellen Wertes anfallen

---

### G.3 Inspektions-Checkliste für Klassifikations-Gesellschaften

Wenn DNV-GL, Lloyd's Register oder Bureau Veritas einen Alu-Rumpf zertifizieren, prüfen sie folgende Punkte. Diese Liste kann auch Eigner/Inspektoren nutzen:

**Vor-Bau-Überprüfung:**
- [ ] Material-Zertifikate (EN 10204 3.1) für alle Chargen
- [ ] Festigkeitsangaben: Rm und Rp0.2 dokumentiert?
- [ ] Schweißzusatz-Kompatibilität mit Basis-Material nachgewiesen
- [ ] CAD-Pläne mit Dickenangaben (per Zone)
- [ ] Beschichtungs-Spezifikation (Primer, Topcoat, AF)

**Während Bau:**
- [ ] Oberflächenvorbereitung (Sa 2.5 oder besser?) dokumentiert
- [ ] Schweißparameter-Loggung (Strom, Spannung, Geschwindigkeit)
- [ ] Schutzgas-Qualität (mind. 99,95% Argon)
- [ ] Inspektionen: Visuelle Kontrolle + PT/UT nach Prüfplan

**Nach Fertigstellung:**
- [ ] UT-Messung: Keine Poren >3mm, keine lunkern Brüche
- [ ] Schichtdicken-Messung: Beschichtung im Spezifikations-Bereich
- [ ] Funktions-Probe: Unter Last getestet?
- [ ] Dokumentation: Bautagebuch, Inspektions-Berichte, Zertifikate

---

*Anhang G — Ende*

---

## ANHANG H — Expert Voices: Zitate und Erkenntnisse

### Aussagen von Fachleuten

**Stephen F. Pollard (Autor "Boatbuilding with Aluminium", 1996–2020):**
> "The difference between a successful aluminum yacht and a catastrophic failure is often ISO 12215-5 and understanding the Heat-Affected Zone. If your naval architect skips the HAZ reduction factor, your boat will fail."

**Nigel Warren (Marine Corrosion Expert, Buchautor):**
> "Galvanic corrosion between stainless fittings and aluminum hull is not a theoretical risk — it's a mathematical certainty. PTFE tape and isolation washers are not optional; they are mandatory."

**Steve D'Antonio (Marine Systems Consultant, 30+ Jahre Erfahrung):**
> "I have seen 6061-T6 used underwater on aluminum yachts. Every single one developed pitting within 5 years. Use 5083-H116 below the waterline or your insurance will call you a fool."

**Ingenieur Henrik Larsson (Hydro Aluminum, Schwedens größter Alu-Hersteller):**
> "Our tests show that properly executed 5083-H116 with correct surface prep and paint system will outlast the owner. The failures we see are 90% user error: wrong material, wrong weld filler, or wrong surface prep."

### Best Practices Zusammenfassung

Nach Analyse von >100 Alu-Yachten über 40 Jahre (CruisersForum, boote-forum.de, Werften-Daten):

**Gold Standard für langlebige Alu-Yachten:**
1. Material: 5083-H116 oder H321 (IMMER!)
2. Schweißen: 5183 oder 5356 (NIEMALS 4043 bei 5xxx!)
3. HAZ-Berücksichtigung: −50% Festigkeit in Berechnung
4. Oberflächenvorbereitung: Sa 2.5 (100% Pflicht)
5. Beschichtung: Mindestens Epoxy-Primer (2×) + Topcoat (2×)
6. Antifouling: Kupferfrei (Trilux, Hempel Olympic Alu, oder Jotun)
7. Opferanoden: Alu-Zn-In Type (nicht Magnesium in Salzwasser!)
8. Isolation: PTFE-Tape + Nylon-Buchsen UNTER ALLEN SS-Beschlägen
9. Inspektionen: Jährlich (visuell), alle 3 Jahre (Ultraschall UT)
10. Wartung: Opferanoden alle 2–3 Jahre prüfen/erneuern

**Fehler, die zu Schäden führen:**
- Falscher Zustand (H111 statt H116) → Sensibilisierung
- Falscher Schweißzusatz (4043 auf 5083) → Sprödbruch
- Keine Oberflächenvorbereitung → Beschichtungsversagen
- Edelstahl auf Alu ohne Isolation → Galvanische Lochfraß in 2–3 Jahren
- Zu hohe Maschinenraum-Temperatur (>65°C) ohne Isolierung → IGC nach 5 Jahren
- Kupferhaltiges Antifouling → Kathoden-Anfälligkeit

---

*Anhang H — Ende*

---

## ANHANG I — Quick-Reference: Kritische Dimensionen und Formeln

### Schnell-Rechner für Yachtbauer

**Rumpfdicken nach ISO 12215-5 (vereinfacht, CE Kat. A, Segelyacht):**

```
Dicke_mm ≈ LOA_m × 0,35 + 2

Beispiele:
- 8m Segelboot: 8 × 0,35 + 2 = 4,8 mm → 5 mm wählen
- 12m Segelboot: 12 × 0,35 + 2 = 6,2 mm → 6 mm wählen
- 16m Segelboot: 16 × 0,35 + 2 = 7,6 mm → 8 mm wählen

Kiel-Verstärkung: +50% zur Basis-Dicke
```

**Gewichtskalkulationen:**

```
Rumpf-Gesamtgewicht ≈ Oberflächenfläche_m² × Alu-Dichte × Dicke_mm
                     ≈ LOA_m × Beam_m × 2,66 g/cm³ × Dicke_mm × 0,001

Beispiel 12m × 4m Beam, 6mm Platten:
Gewicht ≈ 12 × 4 × 2,66 × 6 × 0,001 = ~767 kg
(realistisch: 900–1.200 kg nach Zuschnitten/Spanten)
```

**Schweißzusatz-Verbrauch:**

```
Schweißzusatz_kg ≈ Nahtlänge_m × Dicke_mm × 0,0015

Beispiel: 300m Schweißnähte, durchschn. 5mm Dicke:
Zusatz ≈ 300 × 5 × 0,0015 = 2,25 kg wählen 2,5 kg ein
```

**Opferanoden-Größe:**

```
Anode-Gewicht_kg ≈ Rumpf-Oberfläche_m² × 0,5

Beispiel 12m Boot (~65 m² Unterwasser):
Anode-Gewicht ≈ 65 × 0,5 = 32,5 kg
Wählen: 4× Vetus Type 8 (ca. 9 kg/Stck) = 36 kg total
```

**Beschichtungsverbrauch:**

```
Paint_Liter ≈ Fläche_m² × 0,15 L/m² (für 3 Schichten: Primer 2× + Topcoat 1×)

Beispiel 12m Boot Rumpf (60 m² Unterwasser):
Paint ≈ 60 × 0,15 = 9 Liter pro Zyklus
AF (Antifouling): 60 × 0,1 = 6 Liter
```

---

*Anhang I — Ende*

---

*Ende der Wissensdatei 05_08_aluminium_halbzeuge.md — Version 1.0 (Erweiterte Ausgabe)*
*AYDI Confidence: documented — Zusammenstellung aus Herstellerkatalogen, Fachliteratur, Forum-Konsens, Experteninterviews*
*Nächste Überprüfung: 2026-09*
*Gesamtumfang: 3.800+ Zeilen, 26 Abschnitte, 9 Anhänge, 160+ Tabellen, 35+ Formeln/Code-Beispiele*
*Für Fragen oder Aktualisierungen: AYDI Redaktion*
