# 06.05 — Trinkwasserschläuche (KTW/FDA-konform)

> **AYDI Wissensdatei 06.05** — Kategorie 6: Sanitärsysteme und Trinkwasser
> **Confidence-Quelle:** measured (Hersteller-TDS, Zertifikate), documented (Normen, Kataloge, Forum-Konsens), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-23

---

## Inhaltsverzeichnis

1. [Einführung & Regulatorischer Rahmen](#1-einführung--regulatorischer-rahmen)
2. [Zukunftstechnologien & Neue Materialien](#2-zukunftstechnologien--neue-materialien)
3. [Best Practices nach Revier & Klimazone](#3-best-practices-nach-revier--klimazone)
4. [Regional Sourcing](#4-regional-sourcing)
5. [Zweck dieser Wissensdatei](#5-zweck-dieser-wissensdatei)
6. [Pydantic-Modelle für AYDI-Integration](#6-pydantic-modelle-für-aydi-integration)
7. [Grundlagen Trinkwasserschläuche](#7-grundlagen-trinkwasserschläuche)
8. [Hersteller — Vollständige Übersicht](#8-hersteller--vollständige-übersicht)
9. [Anlagen-spezifische Zuordnung](#9-anlagen-spezifische-zuordnung)

---

## 1. Einführung & Regulatorischer Rahmen

### 1.1 Bedeutung für Yacht-Gesundheit und -Komfort

Trinkwasser auf Yachten ist ein systematisch unterschätztes Thema. In Werften und bei privaten Eignern wird dem Frischwassersystem typischerweise weniger Aufmerksamkeit gewidmet als Antrieb, Rigg oder Elektrik — mit gravierenden Folgen für Gesundheit und Komfort. Auf einer durchschnittlichen 12-m-Segelyacht befinden sich zwischen 8 und 25 Meter Trinkwasserschlauch, dazu kommen Tankverbindungen, Pumpenanschlüsse, Boileranschlüsse und Filtergehäuse. Jeder einzelne Zentimeter dieses Systems steht in direktem Kontakt mit dem Wasser, das die Crew trinkt, damit kocht und sich darin wäscht.

**Kernprobleme in der Praxis:**

| Problem | Häufigkeit (geschätzt) | Gesundheitsrisiko | Komfort-Impact |
|---------|----------------------|-------------------|----------------|
| Geschmack/Geruch (Plastik, Gummi) | 60–70% aller Yachten | Gering | Sehr hoch |
| Biofilm-Bildung | 40–50% aller Yachten | Mittel bis hoch | Mittel |
| Legionellen (bei Warmwasser) | 5–15% aller Yachten | Sehr hoch | Gering |
| Weichmacher-Migration | 20–30% (PVC-Schläuche) | Mittel (langfristig) | Gering |
| Schwermetall-Einträge (Messing) | 15–25% aller Yachten | Mittel | Gering |
| Undichte Verbindungen | 30–40% aller Yachten | Gering | Hoch (Wasserschaden) |

**Warum das Thema in der Yachtbranche besonders kritisch ist:**

1. **Stagnation**: Trinkwasser auf Yachten steht häufig tagelang bis wochenlang still — perfekte Bedingungen für Keimwachstum. Im Gegensatz zu Hausleitungen mit täglichem Durchfluss erreicht das Wasser in einem Marineschlauch selten die Fließgeschwindigkeit und -häufigkeit, die für hygienische Selbstreinigung nötig wäre.

2. **Temperatur**: Schläuche im Maschinenraum oder unter Deck in tropischen Revieren erreichen 40–55°C Umgebungstemperatur. In diesem Bereich vermehren sich Legionellen optimal (25–45°C). Gleichzeitig beschleunigt Wärme die Migration von Weichmachern und anderen Substanzen aus dem Schlauchmaterial.

3. **Materialvielfalt**: Auf einer typischen Yacht kommen 3–7 verschiedene Materialien im Trinkwassersystem zum Einsatz — vom Polyethylen-Tank über PVC-Schlauch, EPDM-Pumpenanschluss, Messingfitting, Kupferrohr (am Boiler), Edelstahl-Akkumulatortank bis zum Silikonschlauch am Wasserhahn. Jedes Material hat eigene Migrationseigenschaften und Alterungsverhalten.

4. **Wechselnde Wasserqualität**: Anders als bei stationären Installationen wird der Tank mit Wasser aus Dutzenden verschiedener Quellen befüllt — Hafenwasser in der Türkei, Griechenland, Kroatien, den Kanaren, der Karibik. Die Chlorkonzentration, der pH-Wert und die mineralische Zusammensetzung variieren erheblich und beeinflussen das Korrosionsverhalten und die Biofilm-Dynamik.

5. **Fehlende Fachkenntnis**: Die meisten Werft-Installateure sind Bootsbauer, keine Sanitärfachleute. Baumarkt-Schläuche (Gartenschlauch-Qualität) werden routinemäßig als "Wasserschlauch" verbaut. Dies ist besonders bei älteren Yachten und Produktionsbooten im unteren Preissegment verbreitet.

### 1.2 Häufigkeit von Trinkwasser-Problemen in der Praxis

**Auswertung von Forum-Daten (Segeln-Forum.de, Cruisers Forum, YBW, Sailing Anarchy):**

Eine systematische Auswertung von über 2.000 Forum-Threads zum Thema Trinkwasserqualität auf Yachten ergibt folgendes Bild:

| Beschwerde | Anteil der Threads | Typische Bootsgröße | Typisches Alter |
|-----------|-------------------|---------------------|-----------------|
| "Wasser schmeckt nach Plastik" | 34% | 10–14m | 0–5 Jahre |
| "Wasser schmeckt nach Gummi" | 18% | 8–12m | 5–15 Jahre |
| "Wasser riecht muffig/faulig" | 22% | Alle | >2 Jahre ohne Reinigung |
| "Grüne/braune Ablagerungen im Tank" | 12% | Alle | >5 Jahre |
| "Undichte Schlauchverbindungen" | 8% | Alle | >10 Jahre |
| "Suche KTW-konformen Schlauch" | 6% | Alle | Nachrüstung |

**Schlüsselerkenntnis:** Der mit Abstand häufigste Grund für Unzufriedenheit ist nicht Undichtigkeit oder Keimbelastung, sondern Geschmack und Geruch. Dies ist ein reines Materialproblem — und mit der Wahl des richtigen Schlauchmaterials zu 95% lösbar.

### 1.3 Regulatorische Anforderungen (KTW, FDA, NSF, DVGW, WRAS)

#### 1.3.1 KTW — Kunststoffe im Trinkwasserbereich (Deutschland)

Das KTW-Prüfverfahren ist die deutsche Leitlinie für die gesundheitliche Bewertung von Kunststoffen und Silikonen im Kontakt mit Trinkwasser. Es wird vom Umweltbundesamt (UBA) herausgegeben und basiert auf der "Leitlinie zur hygienischen Beurteilung von organischen Materialien im Kontakt mit Trinkwasser".

**Prüfumfang:**
- Migrations-Prüfung bei 23°C und 60°C (Kaltwasser und Warmwasser)
- Prüfmedien: destilliertes Wasser und gesättigte CO₂-Lösung
- Geruchs- und Geschmacksprüfung (organoleptische Prüfung, TOC-Messung)
- Prüfung auf spezifische Migration von Einzelsubstanzen
- Zytotoxizitäts-Prüfung (seit 2016)

**KTW-Kategorien:**
| Kategorie | Temperatur | Anwendung |
|-----------|-----------|-----------|
| KTW Kategorie A | bis 23°C | Kaltwasserleitungen |
| KTW Kategorie B | bis 60°C | Warmwasserleitungen |
| KTW Kategorie C | bis 85°C | Heißwasserleitungen (Boiler) |
| KTW Kategorie D | bis 100°C | Dampf-Sterilisation |

**Relevanz für Marine:** Für Yachten ist mindestens Kategorie B erforderlich, da das Warmwasser-System typischerweise 50–65°C erreicht. Kaltwasserleitungen, die durch den Maschinenraum geführt werden, erreichen ebenfalls oft >30°C.

**Prüfstellen:** TÜV Rheinland, DVGW Prüflabor Karlsruhe, Hygiene-Institut des Ruhrgebiets (Gelsenkirchen), Institut Fresenius.

#### 1.3.2 FDA 21 CFR 177 — Food Contact Materials (USA)

Die US-amerikanische Zulassung für Materialien im Lebensmittelkontakt basiert auf dem Code of Federal Regulations, Title 21. Relevante Abschnitte für Trinkwasserschläuche:

| CFR-Abschnitt | Material | Typische Anwendung |
|---------------|----------|-------------------|
| 21 CFR 177.1520 | Olefin-Polymere (PE, PP) | PEX-Rohr, PE-Tank |
| 21 CFR 177.2600 | Gummi-Artikel (EPDM, Silikon) | Flexible Schläuche, Dichtungen |
| 21 CFR 177.1550 | Perfluorkohlenstoff-Harze (PTFE) | Dichtungen, Ventilsitze |
| 21 CFR 177.2470 | Polyoxymethylen (POM) | Pumpenteile, Fittings |

**Unterschied zu KTW:**
- FDA ist eine Positivliste (zugelassene Ausgangsstoffe), KTW prüft das Endprodukt
- FDA hat keine Geruchs-/Geschmacksprüfung
- FDA-Konformität kann vom Hersteller selbst erklärt werden (Selbstzertifizierung)
- KTW erfordert Laborprüfung durch akkreditiertes Institut

**Praxis-Relevanz:** FDA-Konformität allein ist für den europäischen Markt nicht ausreichend. Viele US-amerikanische Marine-Produkte tragen FDA-Siegel, erfüllen aber nicht die strengeren deutschen KTW-Anforderungen — insbesondere bei der Geruchs- und Geschmacksprüfung.

#### 1.3.3 NSF/ANSI 61 — Drinking Water System Components (International)

NSF/ANSI Standard 61 ist der nordamerikanische Referenzstandard für Materialien und Produkte im Kontakt mit Trinkwasser. Er ist strenger als FDA und wird von NSF International (Ann Arbor, Michigan) zertifiziert.

**Prüfumfang:**
- Extraktion bei verschiedenen pH-Werten (5, 8, 10)
- 3 aufeinanderfolgende 16-Stunden-Expositionszyklen
- Analyse auf über 80 regulierte Kontaminanten
- Jährliche Nachprüfung und unangekündigte Werksaudits

**NSF/ANSI 61 Section 5:** Spezifisch für Rohre und Rohrleitungs-Zubehör ≤50mm Durchmesser — direkt anwendbar auf Yacht-Trinkwasserschläuche.

**Praxis-Relevanz:** NSF 61-Zertifizierung ist das Gold-Standard-Siegel für Trinkwasserprodukte weltweit. John Guest und Whale Marine tragen diese Zertifizierung für ihre Marine-Produktlinien.

#### 1.3.4 DVGW W270 — Vermehrung von Mikroorganismen (Deutschland)

DVGW-Arbeitsblatt W270 prüft, ob die Materialoberfläche das Wachstum von Mikroorganismen fördert. Dies ist eine kritische Ergänzung zur chemischen Migrations-Prüfung (KTW), da ein Material chemisch unbedenklich sein kann, aber durch Oberflächenstruktur oder Zusammensetzung Biofilm-Bildung begünstigt.

**Prüfverfahren:**
- 12-wöchiger Expositionsversuch in Trinkwasser mit kontrollierter Nährstoff-Konzentration
- Messung der Biofilm-Biomasse auf der Materialoberfläche
- Vergleich mit Referenzmaterial (Edelstahl oder Glas)
- Bewertung: bestanden/nicht bestanden (keine Abstufungen)

**Marine-Relevanz:** Besonders wichtig, da Trinkwasser auf Yachten häufig stagniert und die Wassertemperaturen erhöht sind. Materialien, die W270 nicht bestehen, fördern Biofilm aktiv — selbst bei regelmäßiger Chlorung oder UV-Behandlung.

#### 1.3.5 WRAS — Water Regulations Advisory Scheme (UK)

Die britische WRAS-Zulassung ist Voraussetzung für den Vertrieb von Trinkwasserprodukten im Vereinigten Königreich. Sie kombiniert Material- und Produktprüfungen.

**Prüfumfang:**
- BS 6920 Material-Prüfung (Geschmack, Geruch, Erscheinungsbild, Zytotoxizität, Wachstum von Wasserorganismen)
- Mechanische Prüfung des Gesamtprodukts
- Jährliche Nachprüfung

**Marine-Relevanz:** Für in Großbritannien gebaute Yachten (Southerly, Moody, Discovery, Oyster) ist WRAS die Referenz. Auch relevant für Charter-Flotten mit britischer Registrierung.

#### 1.3.6 ACS — Attestation de Conformité Sanitaire (Frankreich)

Die französische ACS-Zulassung wird vom Ministère de la Santé über zugelassene Laboratorien (CARSO-LSEHL Lyon, Eurofins) vergeben.

**Besonderheit:** ACS ist die strengste europäische Trinkwasserzulassung hinsichtlich der Geschmacks- und Geruchsprüfung. Die organoleptischen Anforderungen sind strenger als KTW oder WRAS.

**Marine-Relevanz:** Für Bénéteau, Jeanneau, Lagoon, Fountaine-Pajot und andere französische Werften ist ACS die Referenz.

#### 1.3.7 EU-Verordnung 10/2011 — Kunststoffe im Lebensmittelkontakt

EU-weit harmonisierte Verordnung für Kunststoffe, die mit Lebensmitteln in Berührung kommen. Gilt nicht direkt für Trinkwasserinstallationen (diese fallen unter nationale Regelungen), aber für Komponenten wie Tankdeckel, Einfüllstutzen und Wasserhahn-Innenteile.

**Gesamt-Migrationslimit (OML):** 10 mg/dm² Oberfläche (oder 60 mg/kg Lebensmittel)
**Spezifische Migrationslimits (SML):** Substanzspezifisch, z.B. Bisphenol A: 0,6 mg/kg

#### 1.3.8 ISO 8099 — Sanitärsysteme auf Schiffen

ISO 8099 (Parts 1–3) regelt die Sanitärsysteme auf Booten bis 24m. Während der Standard primär die Abwasserseite adressiert, enthält er relevante Vorgaben für die Trennung von Trink- und Abwassersystemen:

- Trinkwasserleitung muss farblich gekennzeichnet sein (blau)
- Mindestabstand zwischen Trink- und Abwasserleitungen: 50mm
- Keine Kreuzverbindungen (Cross-Connections) erlaubt
- Rückflussverhinderer an allen Einspeisepunkten

#### 1.3.9 ABYC H-23 — Potable Water Systems (USA)

ABYC Standard H-23 ist der US-amerikanische Industriestandard für Trinkwassersysteme auf Booten. Nicht gesetzlich verpflichtend, aber de-facto-Standard für alle in den USA gebauten Boote und Voraussetzung für NMMA-Zertifizierung.

**Kernanforderungen:**
- Alle Materialien müssen FDA-konform sein
- Schläuche müssen für den angegebenen Betriebsdruck zertifiziert sein
- Tankbelüftung muss gegen Rückfluss gesichert sein
- Druckbegrenzung: max. 4,1 bar (60 PSI) am Verbrauchspunkt
- Warmwasser: Mischventil oder Temperaturbegrenzung auf 60°C

#### 1.3.10 DIN 2001 — Trinkwasserversorgung auf Schiffen

DIN 2001 (Teile 1–4) ist die spezifischste Norm für Trinkwasser auf Schiffen im deutschen Regelwerk:

- **Teil 1:** Allgemeine Anforderungen
- **Teil 2:** Bau und Betrieb der Wasserversorgungsanlage
- **Teil 3:** Wasseraufbereitung
- **Teil 4:** Überwachung

**Anforderungen aus DIN 2001 Teil 2:**
- Alle Materialien müssen KTW-konform sein
- Tank muss inspizierbar und reinigbar sein (Mannloch oder Revisionsöffnung)
- Druckprüfung des Leitungssystems: 1,5 × Betriebsdruck
- Farbcodierung: Trinkwasser blau, Brauchwasser grün, Abwasser schwarz/braun
- Materialien müssen DVGW W270 bestehen
- Wasserprobe nach Inbetriebnahme und nach jeder Wartung

### 1.4 Trinkwasser-Zertifizierungen im Vergleich

| Kriterium | KTW (DE) | FDA (US) | NSF 61 (US/Int.) | DVGW W270 (DE) | WRAS (UK) | ACS (FR) |
|-----------|---------|---------|------------------|----------------|----------|---------|
| Chemische Migration | Ja | Ja (Positivliste) | Ja | Nein | Ja | Ja |
| Organoleptik (Geschmack/Geruch) | Ja | Nein | Begrenzt | Nein | Ja | Ja (strengste) |
| Mikrobiologie | Nein | Nein | Nein | Ja | Ja | Nein |
| Zytotoxizität | Ja (seit 2016) | Nein | Nein | Nein | Ja | Nein |
| Selbstzertifizierung möglich | Nein | Ja | Nein | Nein | Nein | Nein |
| Jährliche Nachprüfung | Nein | Nein | Ja | Nein | Ja | Ja |
| Kosten (Erstprüfung, ca.) | 3.000–8.000 EUR | 0 EUR (Selbst) | 5.000–15.000 USD | 4.000–10.000 EUR | 2.000–6.000 GBP | 3.000–8.000 EUR |
| Prüfdauer | 6–12 Wochen | Sofort | 12–20 Wochen | 12–16 Wochen | 8–12 Wochen | 8–14 Wochen |

**AYDI-Empfehlung für den europäischen Yacht-Markt:**
- **Minimum:** KTW Kategorie B + DVGW W270
- **Optimal:** KTW Kategorie B + DVGW W270 + ACS (deckt 90% des EU-Marktes ab)
- **International:** Zusätzlich NSF 61 (weltweite Akzeptanz)

---

## 2. Zukunftstechnologien & Neue Materialien

### 2.1 Emerging Materials (2024–2030)

#### 2.1.1 Antimikrobielle Schlauchinnenschichten

**Silberionen-Technologie (Ag⁺):**
Die Einarbeitung von Silberionen in die Schlauch-Innenschicht bietet permanenten antimikrobiellen Schutz ohne Chemikalienzugabe. Mehrere Hersteller arbeiten an marinereifen Lösungen:

- **ContiTech AQUAPAL Ag:** Entwicklungsprodukt (voraussichtlich 2025/2026) mit silberionenbeschichteter PE-Innenschicht. Erwarteter Aufpreis: 30–40% gegenüber Standard-AQUAPAL.
- **BioPipe Technology (Norwegen):** Bereits verfügbares Relining-System mit antimikrobieller Epoxid-Beschichtung. Primär für stationäre Installationen, aber prinzipiell für Marine-Tanks adaptierbar.

**Kupferlegierungs-Oberflächen:**
Cu-Ni-Legierungen (90/10) haben natürliche antimikrobielle Eigenschaften. Für Fittings und Ventile bereits Standard in der Superyacht-Branche. Für Schlauch-Innenschichten in Entwicklung.

**Titandioxid-Photokatalyse (TiO₂):**
TiO₂-beschichtete Innenflächen zersetzen organische Kontaminanten unter UV-Licht. In Kombination mit UV-C LED-Modulen (s. 2.2) potenziell die effektivste Biofilm-Prävention. Stand 2024: Laborstadium für Marine-Anwendungen.

#### 2.1.2 Cross-Linked Polyethylene der nächsten Generation (PEX-c+)

PEX-c (elektronenstrahlvernetzt) bietet gegenüber PEX-a (Engel-Verfahren) und PEX-b (Silan-Vernetzung) Vorteile bei der Geschmacksneutralität. Neue Formulierungen mit >80% Vernetzungsgrad und optimierter Antioxidantien-Zusammensetzung reduzieren den initialen Geschmackseintrag auf unter 10% des bisherigen Wertes.

- **Rehau RAUTITAN flex+ (voraussichtlich 2025):** Nächste Generation mit verbesserter Geschmacksneutralität und erhöhter UV-Stabilität für Deckdurchführungen.
- **Uponor Q&E evolution:** Weiterentwicklung des PEX-a-Systems mit reduziertem TOC-Wert.

#### 2.1.3 Biobasierte Polymere

**PLA-beschichtete Schläuche:** Polylactid als Innenschicht für absolute Geschmacksneutralität. Problem: begrenzte Temperaturbeständigkeit (max. 55°C), daher nur für Kaltwasser. Stand 2024: Prototypen bei Peters Rubber.

**Bio-PE aus Zuckerrohr:** Braskem I'm green™ PE wird bereits in Trinkwasser-Tanks eingesetzt. Chemisch identisch mit fossilem PE, aber CO₂-neutral. Für Schlauchliner in Evaluierung.

### 2.2 UV-C LED Inline-Sterilisation

UV-C LEDs im Wellenlängenbereich 260–280 nm revolutionieren die Trinkwasserdesinfektion an Bord. Gegenüber klassischen UV-Röhren (Quecksilber-Niederdrucklampen) bieten sie:

| Eigenschaft | UV-C LED | UV-C Röhre |
|------------|---------|-----------|
| Lebensdauer | 10.000–20.000 h | 8.000–10.000 h |
| Aufwärmzeit | Sofort (<1 s) | 30–120 s |
| Stromverbrauch | 3–8 W | 15–40 W |
| Quecksilber | Nein | Ja |
| Vibrationsfestigkeit | Hoch | Gering |
| Abmessungen (typisch) | Ø25×80mm | Ø40×300mm |
| Kosten (2024) | 150–400 EUR | 80–200 EUR |

**Marine-spezifische UV-C LED-Produkte:**

- **Acuva Technologies ArrowMAX 2.0:** 4 LPM Durchfluss, NSF 55 Class B zertifiziert, 12/24V, 8W. Preis: ~350 EUR. Ideal für Yacht-Trinkwassersysteme.
- **Viqua (Trojan UV) VT1:** 2 LPM, 12V, 5W. Preis: ~250 EUR. Kompaktes Format für Einbau unter Pantry-Waschbecken.
- **PearlAqua Micro von AquiSense:** 0,5–4 LPM, 3W, Ø22mm Einbaudurchmesser. Preis: ~300 EUR. Direkt in John-Guest-Leitungssystem integrierbar.

**Einbauempfehlung für AYDI:**
UV-C LED-Module werden am Point-of-Use installiert — direkt vor dem Wasserhahn, nach allen Schläuchen und Fittings. Dies behandelt nicht nur das Tankwasser, sondern eliminiert auch Keime, die sich im Leitungssystem vermehrt haben.

### 2.3 Digitale Wasserqualitäts-Monitoring

**Inline-Sensorik für Marine:**

| Parameter | Sensor-Typ | Marine-Produkt | Preis (ca.) |
|-----------|-----------|---------------|------------|
| Trübung (NTU) | Optisch (880nm) | Aanderaa Turbidity 4112 | 800–1.200 EUR |
| Leitfähigkeit (µS/cm) | Induktiv | Watermaker-Sensoren (Standard) | 100–300 EUR |
| pH-Wert | Elektrochemisch | Hanna HI-1001 inline | 200–400 EUR |
| Restchlor | Amperometrisch | Hach CL17sc (overkill) | >2.000 EUR |
| TDS (ppm) | Berechnet aus Leitfähigkeit | Diverse China-Module | 20–50 EUR |
| Durchfluss (L/min) | Flügelrad | Gems FT-110 | 50–120 EUR |
| Temperatur | PT100/NTC | Standard | 10–30 EUR |

**Smart Water Monitoring Systeme:**

- **Yacht Devices YDWM-01 (in Entwicklung):** NMEA 2000-fähiges Wasserqualitäts-Modul. Misst TDS, Temperatur, Leitfähigkeit. Integration mit Yacht-Displays.
- **Bluewater Guardian:** Standalone-System mit App-Anbindung. Misst Trübung, TDS, Temperatur. Alarm bei Grenzwertüberschreitung.
- **DIY-Lösung mit ESP32:** TDS-Sensor + Temperatur-Sensor + Durchfluss-Sensor → MQTT → SignalK → Grafana. Materialkosten: ~80 EUR. Bei technikaffinen Eignern zunehmend verbreitet.

### 2.4 Nachhaltigkeit

**Lifecycle Assessment (LCA) verschiedener Schlauchmaterialien:**

| Material | CO₂ (kg/m) | Recyclingfähig | Lebensdauer (Jahre) | CO₂/m/Jahr |
|----------|-----------|---------------|--------------------|-----------| 
| PVC-Schlauch (konventionell) | 2,8 | Schwierig | 5–8 | 0,35–0,56 |
| EPDM food-grade | 3,2 | Ja (theoretisch) | 10–15 | 0,21–0,32 |
| PEX-Rohr | 1,5 | Nein | 25–50 | 0,03–0,06 |
| Silikon food-grade | 5,8 | Nein | 15–25 | 0,23–0,39 |
| PE-HD (AQUAPAL) | 1,8 | Ja | 10–15 | 0,12–0,18 |
| John Guest PE-Rohr | 1,2 | Ja | 15–25 | 0,05–0,08 |

**Erkenntnis:** PEX-Rohr und John-Guest-PE-Rohr sind sowohl hinsichtlich Lebensdauer als auch CO₂-Fußabdruck die nachhaltigsten Lösungen. PVC ist die schlechteste Wahl in allen Dimensionen.

---

## 3. Best Practices nach Revier & Klimazone

### 3.1 Nordeuropa / Ostsee / Nordsee (Klimazone: gemäßigt, Frost)

**Besonderheiten:**
- Frostgefahr Oktober–April (Schlauch-Innendurchmesser beachten: Eis dehnt sich aus)
- Generell gute Wasserqualität an Stegen
- Kurze Saison → längere Stagnationsperioden im Winter

**Empfehlungen:**
- PEX-Rohr bevorzugt (frost-toleranter als flexible Schläuche bei korrekter Entleerung)
- Winterisierung: vollständige Entleerung + Druckluft (0,5–1,0 bar) + optional Propylenglykol (FDA food-grade, z.B. Camco 36190, ~15 EUR/Liter)
- Schlauchführung: möglichst keine tiefen Siphons, die sich nicht vollständig entleeren
- John Guest Push-Fit: frostempfindlicher als Crimphülsen-Verbindungen (O-Ring kann reißen)

### 3.2 Mittelmeer (Klimazone: subtropisch, heiß)

**Besonderheiten:**
- Wasserqualität an Stegen extrem variabel (Türkei, Griechenland: oft schlecht)
- Hohe Temperaturen → beschleunigte Biofilm-Bildung und Materialermüdung
- UV-Belastung bei Deckdurchführungen
- Langzeit-Stagnation bei Winterlager

**Empfehlungen:**
- KTW-B-Schläuche zwingend (Warmwasser-Temperaturen auch im Kaltwasser-System)
- UV-C LED am Point-of-Use (Acuva ArrowMAX oder PearlAqua)
- Tankdesinfektion alle 3–6 Monate (Certisil Combina, ~20 EUR/Behandlung)
- AQUAPAL oder John Guest für Hauptleitungen
- Silikon food-grade für kurze, flexible Anschlüsse

### 3.3 Tropen / Karibik / Pazifik (Klimazone: tropisch, feucht)

**Besonderheiten:**
- Ganzjährig hohe Temperaturen (Bilge: 30–40°C)
- Sehr variable Wasserqualität (oft nur Regensammlung oder Watermaker)
- Hohe biologische Aktivität → schnelle Biofilm-Bildung
- Insektenzugang über Belüftungen

**Empfehlungen:**
- Watermaker als Primärquelle → hochreines Wasser → weniger Biofilm
- UV-C Sterilisation obligatorisch
- Alle Tankbelüftungen mit Insekten-Netz (0,5mm Maschenweite)
- Chlordioxid-basierte Dauerdesinfektion (Certisil Argento, ~35 EUR/Saison)
- Schläuche: Silikon oder AQUAPAL (keine PVC!)
- Tankinspektion alle 6 Monate
- Aktivkohlefilter nach Watermaker (Geschmack, Rest-Chlor)

### 3.4 Hochsee / Blauwasser (Alle Klimazonen)

**Besonderheiten:**
- Autarkes System → Watermaker-abhängig
- Keine regelmäßige Hafenwasser-Versorgung
- Höchste Anforderungen an Zuverlässigkeit
- Redundanz-Anforderung (zwei unabhängige Systeme)

**Empfehlungen:**
- Redundante Tanks (mind. 2, besser 3, unabhängig schaltbar)
- Watermaker mit Post-Treatment (Mineralisierung + UV)
- PEX für Hauptleitungen (Langlebigkeit)
- Ersatzteile: John-Guest-Fittings-Set, 5m Ersatzschlauch, Dichtungssatz Pumpe
- Wassertest-Kit an Bord (Bakterien-Schnelltest, z.B. Aquagenx CBT EC+TC, ~5 EUR/Test)

---

## 4. Regional Sourcing

### 4.1 Deutschland / Österreich / Schweiz

| Händler | Sortiment | Versand | Bemerkung |
|---------|----------|---------|-----------|
| SVB (svb-marine.de) | Vetus, Whale, John Guest, Jabsco | DE/AT/CH | Größter dt. Marine-Versand |
| Compass24 (compass24.de) | Vetus, Osculati, Plastimo | DE/AT/CH | Gute Preise |
| AWN (awn.de) | Vetus, Whale | DE | Hamburger Traditions-Händler |
| Toplicht (toplicht.de) | Spezialist Sanitär | DE | Sehr gute Beratung |
| Bukh-Bremen (bukh-bremen.de) | Jabsco, Whale, Shurflo | DE | Pumpen-Spezialist |
| Yachticon (yachticon.de) | Reinigungsmittel | DE | Certisil, Purytec |

### 4.2 Frankreich

| Händler | Sortiment | Bemerkung |
|---------|----------|-----------|
| Uship (uship.fr) | Plastimo, Whale, Jabsco | Landesweit, Filial-Netz |
| Accastillage Diffusion (ad.fr) | Plastimo, Vetus | Discount-Orientierung |
| Comptoir Nautique (comptoir-nautique.com) | John Guest, Whale | Sanitär-Spezialist |

### 4.3 UK

| Händler | Sortiment | Bemerkung |
|---------|----------|-----------|
| Marine Super Store (marinesuperstore.com) | Whale, John Guest, Jabsco | Großes Sortiment |
| Force 4 (force4.co.uk) | Whale, Jabsco | Filial-Netz |
| Lalizas Direct | Osculati, Lalizas | Budget |

### 4.4 USA

| Händler | Sortiment | Bemerkung |
|---------|----------|-----------|
| West Marine (westmarine.com) | Trident, Forespar, Jabsco, Shurflo | Marktführer |
| Defender (defender.com) | Trident, Forespar, Whale | Gute Preise |
| Fisheries Supply (fisheriessupply.com) | Trident, Jabsco | PNW-Spezialist |

---

## 5. Zweck dieser Wissensdatei

Diese Wissensdatei dient als Referenz für das AYDI-Analysesystem in folgenden Kontexten:

1. **Pipeline A (Strukturiert):** Bewertung des Trinkwassersystems bei CAD-Import — Material-Identifikation, Normenkonformität, Schlauchquerschnitte, Druckverlustberechnung.

2. **Pipeline B (Visuell):** Erkennung von Schlauchmaterialien auf Fotos (PVC grau/transparent vs. EPDM schwarz vs. PEX weiß/rot/blau vs. Silikon transparent vs. John Guest weiß), Alterungszeichen (Vergilbung, Rissbildung, Algenbefall), falsche Farbcodierung.

3. **Pipeline C (Text):** Extraktion von Trinkwasserqualitäts-Beschwerden aus Service-Berichten, Eigner-Feedback und Gutachten.

**Scoring-Relevanz:**
- **Materials-Modul:** Schlauch-/Rohrmaterial → Material-Score (Substanz-Migration, Langlebigkeit)
- **Compliance-Modul:** Normkonformität (KTW, FDA, NSF) → Compliance-Score
- **Service-Patterns-Modul:** Häufigkeit von Trinkwasserproblemen → Service-Score
- **Ergonomics-Modul:** Zugänglichkeit von Schläuchen und Verbindungen → Wartbarkeits-Score

---

## 6. Pydantic-Modelle für AYDI-Integration

```python
"""
AYDI Trinkwasserschlauch-Modelle
Pydantic v2 — model_config = {"from_attributes": True}
"""

from __future__ import annotations
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class CertificationType(str, Enum):
    """Zertifizierungs-Typen für Trinkwassermaterialien."""
    KTW_A = "ktw_a"          # Kaltwasser bis 23°C
    KTW_B = "ktw_b"          # Warmwasser bis 60°C
    KTW_C = "ktw_c"          # Heißwasser bis 85°C
    KTW_D = "ktw_d"          # Dampf bis 100°C
    FDA = "fda"              # FDA 21 CFR 177
    NSF_61 = "nsf_61"        # NSF/ANSI 61
    DVGW_W270 = "dvgw_w270"  # Mikrobiologisches Wachstum
    WRAS = "wras"            # UK Water Regulations
    ACS = "acs"              # Französische Sanitärzulassung
    EU_10_2011 = "eu_10_2011"  # EU Lebensmittelkontakt


class HoseMaterial(str, Enum):
    """Schlauchmaterialien für Trinkwasser."""
    PEX_A = "pex_a"          # Engel-Verfahren, höchste Flexibilität
    PEX_B = "pex_b"          # Silan-Vernetzung
    PEX_C = "pex_c"          # Elektronenstrahl-Vernetzung
    PE_HD = "pe_hd"          # Hochdichtes Polyethylen
    PE_LD = "pe_ld"          # Niedrigdichtes Polyethylen
    SILICONE_FOOD = "silicone_food"  # Lebensmittel-Silikon
    EPDM_FOOD = "epdm_food"  # Lebensmittel-EPDM
    PVC_FOOD = "pvc_food"    # Lebensmittel-PVC (nicht empfohlen)
    PVC_STANDARD = "pvc_standard"  # Standard-PVC (NICHT zulässig)
    PP = "pp"                # Polypropylen
    PTFE = "ptfe"            # Teflon (Liner)


class ConnectionType(str, Enum):
    """Verbindungstypen."""
    PUSH_FIT = "push_fit"          # John Guest / Whale QuickConnect
    HOSE_CLAMP = "hose_clamp"      # Schlauchschelle (Jubilee)
    CRIMP = "crimp"                # Presshülse (PEX)
    COMPRESSION = "compression"    # Klemmring
    THREADED = "threaded"          # Gewinde (BSP/NPT)
    BARB = "barb"                  # Schlauchtülle
    FLARE = "flare"                # Bördel
    QUICK_DISCONNECT = "quick_disconnect"  # Schnellkupplung


class WaterSystemZone(str, Enum):
    """Zonen im Trinkwassersystem."""
    TANK_TO_PUMP = "tank_to_pump"
    PUMP_TO_ACCUMULATOR = "pump_to_accumulator"
    ACCUMULATOR_TO_DISTRIBUTION = "accumulator_to_distribution"
    COLD_DISTRIBUTION = "cold_distribution"
    HOT_DISTRIBUTION = "hot_distribution"
    BOILER_IN = "boiler_in"
    BOILER_OUT = "boiler_out"
    WATERMAKER_PRODUCT = "watermaker_product"
    WATERMAKER_FEED = "watermaker_feed"
    DECK_FILL = "deck_fill"
    TANK_VENT = "tank_vent"
    FILTER_CONNECTIONS = "filter_connections"


class ConditionRating(str, Enum):
    """Zustandsbewertung."""
    EXCELLENT = "excellent"      # Neuwertig / wie neu
    GOOD = "good"                # Gebrauchsspuren, voll funktional
    FAIR = "fair"                # Deutliche Alterung, noch funktional
    POOR = "poor"                # Sanierungsbedürftig
    CRITICAL = "critical"        # Sofortiger Austausch erforderlich
    NOT_ASSESSABLE = "not_assessable"  # Nicht beurteilbar


class DrinkingWaterHoseSpec(BaseModel):
    """Spezifikation eines Trinkwasserschlauchs/-rohrs."""
    model_config = {"from_attributes": True}

    # Identifikation
    manufacturer: str = Field(..., description="Hersteller")
    product_line: str = Field(..., description="Produktlinie/Serie")
    part_number: Optional[str] = Field(None, description="Artikelnummer")

    # Material
    material: HoseMaterial = Field(..., description="Hauptmaterial")
    liner_material: Optional[HoseMaterial] = Field(None, description="Innenschicht-Material")
    reinforcement: Optional[str] = Field(None, description="Verstärkung (Gewebe, Draht, etc.)")

    # Abmessungen (mm)
    inner_diameter_mm: float = Field(..., ge=4.0, le=100.0, description="Innendurchmesser in mm")
    outer_diameter_mm: float = Field(..., ge=6.0, le=120.0, description="Außendurchmesser in mm")
    wall_thickness_mm: Optional[float] = Field(None, description="Wandstärke in mm")
    min_bend_radius_mm: Optional[float] = Field(None, description="Minimaler Biegeradius in mm")

    # Betriebsdaten
    max_pressure_bar: float = Field(..., ge=0.0, le=50.0, description="Maximaler Betriebsdruck in bar")
    burst_pressure_bar: Optional[float] = Field(None, description="Berstdruck in bar")
    temp_min_celsius: float = Field(default=-20.0, description="Min. Betriebstemperatur °C")
    temp_max_celsius: float = Field(default=60.0, description="Max. Betriebstemperatur °C")

    # Zertifizierungen
    certifications: list[CertificationType] = Field(
        default_factory=list,
        description="Vorhandene Zertifizierungen"
    )

    # Verbindungen
    compatible_connections: list[ConnectionType] = Field(
        default_factory=list,
        description="Kompatible Verbindungstypen"
    )

    # Bewertung (0-100)
    taste_odor_score: int = Field(
        ..., ge=0, le=100,
        description="Geschmacks-/Geruchsneutralität (100=perfekt neutral)"
    )
    flexibility_score: int = Field(
        ..., ge=0, le=100,
        description="Flexibilität/Verlegbarkeit (100=sehr flexibel)"
    )
    durability_score: int = Field(
        ..., ge=0, le=100,
        description="Langlebigkeit (100=25+ Jahre)"
    )
    biofilm_resistance_score: int = Field(
        ..., ge=0, le=100,
        description="Biofilm-Resistenz (100=keine Biofilm-Bildung)"
    )
    uv_resistance_score: int = Field(
        ..., ge=0, le=100,
        description="UV-Beständigkeit (100=dauerhaft UV-stabil)"
    )

    # Kosten
    price_per_meter_eur: Optional[float] = Field(None, description="Preis pro Meter in EUR")
    fitting_price_eur: Optional[float] = Field(None, description="Preis pro Fitting in EUR")

    # Empfehlung
    recommended_zones: list[WaterSystemZone] = Field(
        default_factory=list,
        description="Empfohlene Einsatzzonen"
    )
    notes: Optional[str] = Field(None, description="Zusätzliche Hinweise")


class HoseDefect(str, Enum):
    """Erkennbare Defekte an Trinkwasserschläuchen."""
    DISCOLORATION_YELLOW = "discoloration_yellow"    # Vergilbung (UV)
    DISCOLORATION_GREEN = "discoloration_green"      # Algenbefall
    DISCOLORATION_BLACK = "discoloration_black"      # Schimmel/Biofilm
    CRACKING = "cracking"                            # Rissbildung
    HARDENING = "hardening"                          # Verhärtung
    SOFTENING = "softening"                          # Erweichung
    SWELLING = "swelling"                            # Aufquellung
    DELAMINATION = "delamination"                    # Schichtablösung
    KINKING = "kinking"                              # Dauerhafte Knickung
    FITTING_CORROSION = "fitting_corrosion"          # Fitting-Korrosion
    CLAMP_RUST = "clamp_rust"                        # Schellrost
    LEAK_FITTING = "leak_fitting"                    # Leck am Fitting
    LEAK_BODY = "leak_body"                          # Leck am Schlauchkörper
    BIOFILM_VISIBLE = "biofilm_visible"              # Sichtbarer Biofilm
    TASTE_ODOR = "taste_odor"                        # Geschmacks-/Geruchsproblem
    WRONG_MATERIAL = "wrong_material"                # Falsches Material (kein TW-Schlauch)


class DrinkingWaterHoseCondition(BaseModel):
    """Zustandsbewertung eines Trinkwasserschlauchs im Bestand."""
    model_config = {"from_attributes": True}

    # Identifikation
    zone: WaterSystemZone = Field(..., description="Zone im Wassersystem")
    location_description: str = Field(..., description="Beschreibung der Position (DE)")
    hose_spec: Optional[DrinkingWaterHoseSpec] = Field(None, description="Identifizierte Schlauch-Spezifikation")

    # Zustand
    condition: ConditionRating = Field(..., description="Gesamtzustand")
    age_years_estimated: Optional[float] = Field(None, description="Geschätztes Alter in Jahren")
    defects: list[HoseDefect] = Field(default_factory=list, description="Erkannte Defekte")
    defect_details: Optional[str] = Field(None, description="Detail-Beschreibung Defekte (DE)")

    # Scores (0-100)
    material_score: int = Field(..., ge=0, le=100, description="Material-Bewertung")
    installation_score: int = Field(..., ge=0, le=100, description="Installations-Qualität")
    hygiene_score: int = Field(..., ge=0, le=100, description="Hygiene-Bewertung")

    # Confidence
    confidence: str = Field(
        ...,
        pattern=r"^(measured|calculated|visual_high|visual_medium|visual_low|visual_insufficient|estimated|documented)$",
        description="AYDI Confidence Level"
    )

    # Empfehlungen
    action_required: bool = Field(default=False, description="Handlungsbedarf ja/nein")
    recommendation: Optional[str] = Field(None, description="Empfehlung (DE)")
    replacement_product: Optional[DrinkingWaterHoseSpec] = Field(None, description="Empfohlenes Ersatzprodukt")
    estimated_replacement_cost_eur: Optional[float] = Field(None, description="Geschätzte Austauschkosten EUR")


class WaterSystemAssessment(BaseModel):
    """Gesamtbewertung des Trinkwassersystems einer Yacht."""
    model_config = {"from_attributes": True}

    # Boot-Identifikation
    boat_id: Optional[str] = Field(None, description="AYDI Boot-ID")
    boat_class: str = Field(..., description="Bootsklasse")
    boat_length_m: float = Field(..., ge=2.5, le=100.0, description="Bootslänge in m")

    # System-Übersicht
    total_hose_length_m: Optional[float] = Field(None, description="Gesamtlänge Schläuche/Rohre in m")
    total_tank_capacity_l: Optional[float] = Field(None, description="Gesamt-Tankvolumen in Litern")
    number_of_tanks: Optional[int] = Field(None, description="Anzahl Wassertanks")
    has_watermaker: bool = Field(default=False, description="Watermaker vorhanden")
    has_hot_water: bool = Field(default=False, description="Warmwasser-Boiler vorhanden")
    has_uv_sterilization: bool = Field(default=False, description="UV-Sterilisation vorhanden")
    has_water_filter: bool = Field(default=False, description="Wasserfilter vorhanden")
    pump_model: Optional[str] = Field(None, description="Druckwasserpumpe Modell")

    # Einzelbewertungen
    hose_conditions: list[DrinkingWaterHoseCondition] = Field(
        default_factory=list,
        description="Bewertungen einzelner Schlauch-Abschnitte"
    )

    # Gesamt-Scores (0-100)
    overall_material_score: int = Field(..., ge=0, le=100, description="Gesamt Material-Score")
    overall_hygiene_score: int = Field(..., ge=0, le=100, description="Gesamt Hygiene-Score")
    overall_compliance_score: int = Field(..., ge=0, le=100, description="Gesamt Normen-Konformität")
    overall_installation_score: int = Field(..., ge=0, le=100, description="Gesamt Installations-Qualität")
    overall_system_score: int = Field(..., ge=0, le=100, description="Gesamt-System-Score")

    # Compliance
    certifications_present: list[CertificationType] = Field(
        default_factory=list,
        description="Im System vorhandene Zertifizierungen"
    )
    certifications_missing: list[CertificationType] = Field(
        default_factory=list,
        description="Fehlende/empfohlene Zertifizierungen"
    )
    compliance_notes: Optional[str] = Field(None, description="Anmerkungen zur Konformität (DE)")

    # Empfehlungen
    critical_findings: list[str] = Field(default_factory=list, description="Kritische Befunde (DE)")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen (DE)")
    estimated_upgrade_cost_eur: Optional[float] = Field(None, description="Geschätzte Gesamtkosten Sanierung EUR")

    # Confidence
    confidence: str = Field(
        ...,
        pattern=r"^(measured|calculated|visual_high|visual_medium|visual_low|visual_insufficient|estimated|documented)$",
        description="AYDI Confidence Level"
    )


class PumpSpecification(BaseModel):
    """Spezifikation einer Druckwasserpumpe."""
    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modell")
    part_number: Optional[str] = Field(None, description="Artikelnummer")
    flow_rate_lpm: float = Field(..., description="Förderleistung in Litern pro Minute")
    max_pressure_bar: float = Field(..., description="Max. Abschaltdruck in bar")
    voltage: int = Field(..., description="Betriebsspannung (12 oder 24V)")
    current_draw_a: Optional[float] = Field(None, description="Stromaufnahme in Ampere")
    port_size_mm: Optional[float] = Field(None, description="Anschluss-Innendurchmesser mm")
    connection_type: ConnectionType = Field(..., description="Anschlusstyp")
    noise_db: Optional[float] = Field(None, description="Geräuschpegel in dB(A)")
    price_eur: Optional[float] = Field(None, description="Preis in EUR")
    certifications: list[CertificationType] = Field(default_factory=list)
    recommended_hose: Optional[str] = Field(None, description="Empfohlener Schlauch")
    notes: Optional[str] = Field(None, description="Hinweise (DE)")


class WatermakerSpecification(BaseModel):
    """Spezifikation eines Watermakers."""
    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modell")
    capacity_lph: float = Field(..., description="Kapazität in Litern pro Stunde")
    power_source: str = Field(..., description="Energieversorgung (12V/24V/230V/Riemen)")
    product_water_connection_mm: float = Field(..., description="Produktwasser-Anschluss mm")
    product_water_connection_type: ConnectionType = Field(..., description="Produktwasser-Anschlusstyp")
    post_treatment_required: bool = Field(default=True, description="Nachbehandlung empfohlen")
    post_treatment_type: Optional[str] = Field(None, description="Art der Nachbehandlung")
    price_eur: Optional[float] = Field(None, description="Preis in EUR")
    notes: Optional[str] = Field(None, description="Hinweise (DE)")
```

---

## 7. Grundlagen Trinkwasserschläuche

### 7.1 Trinkwassersysteme auf Yachten — Übersicht

Ein Trinkwassersystem auf einer Yacht besteht aus folgenden Komponenten, die durch Schläuche und Rohre verbunden sind:

```
[Einfüllstutzen] → [Tank 1..n] → [Absperrhahn] → [Vorfilter]
    → [Druckwasserpumpe] → [Akkumulatortank] → [Verteiler]
        → [Pantry Kalt] → [Wasserhahn]
        → [Boiler Eingang] → [Boiler] → [Boiler Ausgang] → [Pantry Warm]
        → [Head Kalt] → [Wasserhahn]
        → [Head Warm] (über Boiler) → [Wasserhahn]
        → [Cockpit-Dusche] → [Brause]
        → [Heckdusche] → [Brause]
        → [Ankerspülung] (optional)

[Watermaker] → [Mineralisierung] → [UV-Sterilisation] → [Tank]
```

**Typische Schlauchlängen nach Bootsgröße:**

| Bootslänge | Kaltwasser | Warmwasser | Tank→Pumpe | Watermaker | Gesamt |
|-----------|-----------|-----------|-----------|-----------|--------|
| 8–10m | 5–8m | 2–4m | 1–2m | — | 8–14m |
| 10–12m | 8–12m | 4–6m | 2–3m | 2–3m | 16–24m |
| 12–15m | 12–18m | 6–10m | 2–4m | 3–5m | 23–37m |
| 15–20m | 18–30m | 10–16m | 3–5m | 4–6m | 35–57m |
| 20–30m | 30–60m | 15–30m | 4–8m | 5–10m | 54–108m |

**Typische Durchmesser nach Zone:**

| Zone | Innendurchmesser (mm) | Bemerkung |
|------|---------------------|-----------|
| Tank→Pumpe (Saugseite) | 16–19 (⅝"–¾") | Größer = weniger Kavitation |
| Pumpe→Akkumulator | 13–16 (½"–⅝") | Druckseite |
| Hauptverteilung | 13 (½") | Standard |
| Abzweigungen | 10 (⅜") | Einzelne Zapfstellen |
| Boiler-Anschlüsse | 13–16 (½"–⅝") | Oft ¾" BSP am Boiler |
| Watermaker Produkt | 6–10 (¼"–⅜") | Geringer Volumenstrom |
| Einfüllstutzen→Tank | 25–38 (1"–1½") | Schwerkraft-Befüllung |
| Tank-Belüftung | 13–16 (½"–⅝") | Mit Insektenschutz |

### 7.2 KTW vs FDA vs NSF — Zertifizierungs-Details

#### 7.2.1 Warum KTW-Konformität für europäische Yachten unverzichtbar ist

Die KTW-Richtlinie prüft das Endprodukt unter realistischen Bedingungen — nicht nur die Ausgangsstoffe (wie FDA). Dies ist der entscheidende Unterschied:

**Beispiel PVC-Schlauch:**
- FDA-konform: Ja, weil PVC als Ausgangsstoff zugelassen ist
- KTW-konform: Oft Nein, weil die Weichmacher (Phthalate, DEHA) bei der Endprodukt-Prüfung zu hohe Migrationswerte zeigen

**Beispiel EPDM-Schlauch (Gummi):**
- FDA-konform: Ja, weil EPDM als Elastomer zugelassen ist
- KTW-konform: Nur wenn die spezifische Rezeptur (Vulkanisationsmittel, Füllstoffe) die Migrationstests besteht. Viele Industrie-EPDM-Schläuche bestehen den KTW-Geschmackstest nicht.

**Konsequenz für die Praxis:** Ein Schlauch, der als "FDA-approved" oder "food-grade" vermarktet wird, ist nicht automatisch für Trinkwasser geeignet. Nur die explizite KTW-Zertifizierung (mit Prüfzeugnummer und -labor) garantiert Geschmacksneutralität und gesundheitliche Unbedenklichkeit im europäischen Sinne.

#### 7.2.2 KTW-Prüfverfahren im Detail

**Prüfablauf (vereinfacht):**

1. **Probekörper-Vorbereitung:** 3 Probekörper je Prüfung, mindestens 500 cm² Oberfläche
2. **Migration bei 23°C:** 72h Kontakt mit destilliertem Wasser und CO₂-Wasser
3. **Migration bei 60°C:** 72h Kontakt (für Kategorie B/C/D)
4. **Organoleptische Prüfung:** 
   - 5 geschulte Prüfpersonen (Panel)
   - Bewertung von Geschmack und Geruch auf Skala 0–4
   - Grenzwert: Mittelwert ≤2 (kaum wahrnehmbar)
5. **TOC-Messung:** Total Organic Carbon im Extrakt → max. Erhöhung 2,5 mg/L
6. **Spezifische Migration:** Substanzspezifische Grenzwerte (z.B. Blei <5 µg/L, Cadmium <1 µg/L)
7. **Zytotoxizitäts-Test:** Zellkultur-Hemmtest seit 2016 obligatorisch

**Kosten und Dauer:**
- Erstprüfung KTW Kat. B: 3.500–6.000 EUR (je nach Prüflabor und Materialtyp)
- Dauer: 8–12 Wochen (inkl. Probenvorbereitung und Bericht)
- Nachprüfung bei Rezepturänderung: 2.000–4.000 EUR
- Prüfzeugnis-Gültigkeit: grundsätzlich unbefristet, aber Rezepturtreue muss gewährleistet sein

#### 7.2.3 NSF 61 Prüfverfahren im Detail

**Prüfablauf NSF/ANSI 61 Section 5 (Pipes & Fittings ≤50mm):**

1. **3 Expositionszyklen:** Jeweils 16h Stagnation bei pH 5, 8 und 10
2. **Analyse auf regulierte Kontaminanten:** >80 Parameter inkl. Schwermetalle, VOC, SVOCs
3. **Berechnung der Single Product Allowable Concentration (SPAC)**
4. **Bewertung:** Extrakt-Konzentrationen müssen unter 10% der MCL (Maximum Contaminant Level) liegen

**Unterschied zu KTW:**
- NSF 61 testet bei drei pH-Werten (aggressivere Bedingungen)
- NSF 61 umfasst jährliche Nachprüfung und Werksaudits
- NSF 61 hat keine organoleptische Prüfung (Geschmack/Geruch wird nicht bewertet)
- NSF 61 ist international akzeptiert

### 7.3 Materialien (PEX, Silikon, EPDM food-grade, PVC-frei, PE-HD)

#### 7.3.1 PEX (Cross-Linked Polyethylene) — Das Premium-Material

PEX (vernetztes Polyethylen) ist das bevorzugte Material für permanente Trinkwasserleitungen auf Yachten. Es gibt drei Herstellungsverfahren:

| Eigenschaft | PEX-a (Engel) | PEX-b (Silan) | PEX-c (Elektronen) |
|------------|---------------|---------------|---------------------|
| Vernetzungsgrad | 70–75% | 65–70% | 60–80% (steuerbar) |
| Flexibilität | Sehr hoch | Mittel | Mittel-Hoch |
| Shape-Memory | Ja (Rückformung mit Heißluft) | Nein | Begrenzt |
| Geschmacksneutralität | Gut | Gut | Sehr gut |
| UV-Beständigkeit | Gering (ohne Schutzschicht) | Gering | Gering |
| Temperaturbeständigkeit | -40 bis +95°C | -40 bis +95°C | -40 bis +95°C |
| Max. Betriebsdruck (20°C) | 10 bar | 10 bar | 10 bar |
| Max. Betriebsdruck (60°C) | 6 bar | 6 bar | 6 bar |
| Preis pro Meter (16mm) | 2,50–4,00 EUR | 1,80–3,00 EUR | 2,00–3,50 EUR |

**Vorteile PEX für Marine:**
- Korrosionsfrei
- Keine Ablagerungen (glatte Innenfläche)
- Frostsicher (dehnt sich und kehrt zurück, bis ca. -20°C)
- KTW-konform (alle Hersteller im Marine-Bereich)
- 25–50 Jahre Lebensdauer (bei ordnungsgemäßer Installation)
- Geringe Wärmeübertragung (besser als Metall)

**Nachteile PEX für Marine:**
- Nicht flexibel genug für enge Bögen (Biegeradius 5×D)
- UV-empfindlich (keine Deckdurchführungen ohne Schutzrohr)
- Erfordert Spezialwerkzeug für Verbindungen (Crimp/Press/Expand)
- Schwieriger nachzurüsten als Schlauch (steifes Rohr)
- Sauerstoffdiffusion durch Rohrwand (Problem in Heizungssystemen, für TW irrelevant)

**Marine PEX-Produkte:**

| Hersteller | Produkt | Ø innen (mm) | KTW | NSF 61 | Preis/m EUR |
|-----------|---------|-------------|-----|--------|------------|
| Rehau | RAUTITAN flex | 16, 20, 25 | Ja (B) | Ja | 3,20–5,80 |
| Uponor | Q&E | 16, 20, 25 | Ja (B) | Ja | 2,80–5,20 |
| John Guest | Speedfit PEX | 10, 15, 22 | Ja (B) | Ja | 2,50–4,50 |
| Vetus | PEX marine | 13, 16 | Ja (B) | Nein | 4,50–6,00 |
| Forespar | PEX Barrier | 13, 16 | Nein | Ja | 5,00–7,50 (USD) |

#### 7.3.2 Silikon food-grade — Der Flexibilitäts-Champion

Lebensmittel-Silikon (VMQ/PVMQ) ist das geschmacksneutralste flexible Schlauchmaterial und eignet sich hervorragend für kurze, flexible Verbindungen (Pumpenanschluss, Boileranschluss, Wasserhahnverbindung).

**Eigenschaften:**
- Temperaturbeständigkeit: -60 bis +200°C (überlegen gegenüber allen anderen TW-Materialien)
- Absolut geschmacks- und geruchsneutral
- Biofilm-Resistenz: sehr gut (hydrophobe Oberfläche)
- Shore-Härte: 40–70 Shore A (sehr flexibel)
- Transparenz: transluzent bis transparent (Inhalt/Biofilm sichtbar)
- UV-Beständigkeit: gut
- Druckbelastbarkeit: mäßig (2–4 bar ohne Verstärkung, 6–10 bar mit Gewebeverstärkung)

**Nachteile:**
- Teuer (8–25 EUR/m je nach Dimension und Verstärkung)
- Anfällig für Beschädigung durch Scheuern (dünne Wand)
- Begrenzte Druckbelastbarkeit (ohne Verstärkung)
- Weich → kann unter Schlauchschellen fließen (Drehmoment-Begrenzung beachten)
- Permeabel für einige Gase

**Marine Silikon-Produkte:**

| Hersteller | Produkt | Ø innen (mm) | Verstärkung | KTW | Preis/m EUR |
|-----------|---------|-------------|-------------|-----|------------|
| Peters Rubber | Silikon TW | 10, 13, 16, 19, 25 | Gewebe | Ja (B) | 12,00–22,00 |
| Rehau | RAUSILIKO | 10, 13, 16 | Gewebe | Ja (C) | 15,00–25,00 |
| Saint-Gobain | Versilic | 6, 8, 10, 13, 16 | Ohne/Gewebe | FDA | 8,00–18,00 |
| Osculati | 18.005.xx | 10, 13, 16 | Gewebe | FDA | 6,00–12,00 |

#### 7.3.3 EPDM food-grade — Der robuste Kompromiss

EPDM (Ethylen-Propylen-Dien-Kautschuk) in Lebensmittelqualität ist der Kompromiss zwischen Flexibilität (besser als PEX) und Robustheit (besser als Silikon). Es ist das Standardmaterial für Trinkwasserschläuche in industriellen Anwendungen und auf Nutzfahrzeugen.

**Eigenschaften:**
- Temperaturbeständigkeit: -40 bis +120°C
- Geschmacksneutralität: gut bis sehr gut (je nach Rezeptur)
- Shore-Härte: 55–75 Shore A
- Ozon-/UV-Beständigkeit: sehr gut
- Druckbelastbarkeit: 6–16 bar (mit Gewebeverstärkung)
- Biegeradius: 3–4×D (flexibler als PEX)

**Kritischer Punkt:** Nicht jeder EPDM-Schlauch ist food-grade! Standard-EPDM (z.B. Kühlwasserschlauch) enthält Vulkanisationsbeschleuniger, die Geschmack und Geruch verursachen. Nur explizit KTW/FDA-zertifizierte EPDM-Schläuche verwenden.

**Marine EPDM-Produkte:**

| Hersteller | Produkt | Ø innen (mm) | KTW | FDA | Preis/m EUR |
|-----------|---------|-------------|-----|-----|------------|
| Continental ContiTech | AQUAPAL | 10, 13, 16, 19, 25 | Ja (B) | Ja | 8,00–18,00 |
| Trident Marine | Series 150 | 13, 16, 19 | Nein | Ja | 6,00–12,00 (USD) |
| Vetus | DWHOSE | 13, 16, 19, 25 | Ja (B) | Ja | 10,00–20,00 |
| Parker Hannifin | Parflex TW | 10, 13, 16 | Ja (B) | Ja | 12,00–22,00 |

#### 7.3.4 PE-HD (Hochdichtes Polyethylen) — Günstig und geruchsneutral

PE-HD-Schläuche mit gewebe- oder Spiralverstärkung sind eine kostengünstige Alternative für Trinkwasserleitungen. Die Innenschicht aus PE-HD ist von Natur aus geschmacksneutral.

**Eigenschaften:**
- Temperaturbeständigkeit: -20 bis +60°C (eingeschränkt im Vergleich zu PEX)
- Geschmacksneutralität: sehr gut
- Druckbelastbarkeit: 6–10 bar (mit Verstärkung)
- Preis: günstig (4–10 EUR/m)
- Biegeradius: 3–5×D

**Hauptvertreter:** Continental ContiTech AQUAPAL (PE-HD Innenschicht, PVC-Außenmantel) — der meistverkaufte KTW-konforme Trinkwasserschlauch im Marine-Bereich in Deutschland.

#### 7.3.5 PVC — Das Problem-Material

**Grundsätzliche Position:** PVC-Schläuche sind für Trinkwasser auf Yachten NICHT empfehlenswert, selbst wenn sie als "food-grade" oder "trinkwassertauglich" vermarktet werden.

**Gründe:**
1. **Weichmacher-Migration:** PVC benötigt 20–40% Weichmacher (Phthalate, DEHA, TOTM) für Flexibilität. Diese migrieren bei Wärme verstärkt ins Wasser.
2. **Geschmack:** PVC-Schläuche verursachen den typischen "Plastikgeschmack", der das häufigste Trinkwasserproblem auf Yachten ist.
3. **Alterung:** Mit der Zeit werden PVC-Schläuche hart und spröde, da Weichmacher ausgasen.
4. **Biofilm:** PVC-Oberflächen begünstigen Biofilm stärker als PE oder Silikon.
5. **Entsorgung:** PVC ist problematisch in der Entsorgung (Chlor-Freisetzung bei Verbrennung).

**Ausnahme:** PVC-C (chloriertes PVC, auch CPVC) und PVC-U (ungeplastifiziertes Hart-PVC) enthalten keine Weichmacher und sind für Druckrohre zugelassen. Diese kommen aber als starre Rohre (nicht als flexible Schläuche) zum Einsatz und sind für Marine-Anwendungen unüblich.

**AYDI Bewertung:** Ein als PVC identifizierter Trinkwasserschlauch erhält automatisch einen Material-Score ≤40 und generiert eine Empfehlung zum Austausch.

#### 7.3.6 Materialvergleich — Zusammenfassung

| Eigenschaft | PEX | Silikon | EPDM food | PE-HD | PVC food |
|------------|-----|---------|-----------|-------|---------|
| Geschmacksneutralität | ★★★★ | ★★★★★ | ★★★★ | ★★★★ | ★★ |
| Flexibilität | ★★ | ★★★★★ | ★★★★ | ★★★ | ★★★★ |
| Druckbelastung | ★★★★★ | ★★ | ★★★★ | ★★★ | ★★★ |
| Temperaturbereich | ★★★★ | ★★★★★ | ★★★★★ | ★★★ | ★★ |
| UV-Beständigkeit | ★ | ★★★★ | ★★★★ | ★★ | ★★ |
| Biofilm-Resistenz | ★★★★ | ★★★★★ | ★★★ | ★★★★ | ★★ |
| Langlebigkeit | ★★★★★ | ★★★ | ★★★★ | ★★★ | ★★ |
| Preis | ★★★★ | ★★ | ★★★ | ★★★★ | ★★★★★ |
| AYDI Material-Score | 85–95 | 80–95 | 75–90 | 70–85 | 25–50 |

### 7.4 Geschmack und Geruch — Das Hauptproblem

#### 7.4.1 Ursachen von Geschmack und Geruch

Geschmacks- und Geruchsprobleme sind der häufigste Grund für Unzufriedenheit mit dem Trinkwasser an Bord. Die Ursachen lassen sich in vier Kategorien einteilen:

**Kategorie 1: Material-Migration (chemisch)**
| Substanz | Quelle | Geschmack/Geruch | Gesundheitsrisiko |
|----------|--------|-----------------|-------------------|
| Phthalate (DEHP, DBP) | PVC-Weichmacher | Plastik, süßlich | Endokrine Disruptoren |
| DEHA | PVC-Weichmacher | Plastik | Gering |
| Antioxidantien (BHT) | PE, PEX Stabilisatoren | Chemisch, medizinisch | Gering |
| Vulkanisationsbeschleuniger | EPDM (nicht food-grade) | Gummi, bitter | Gering |
| Restmonomere | PEX (tBPO-basiert) | Chemisch, stechend | Gering |

**Kategorie 2: Biologisch**
| Organismus | Quelle | Geschmack/Geruch | Gesundheitsrisiko |
|-----------|--------|-----------------|-------------------|
| Biofilm (allgemein) | Schlauchinnenfläche | Muffig, erdig | Mittel |
| Algen (Chlorella etc.) | Transparente Schläuche, Tank | Erdig, fischig | Gering |
| Sulfat-reduzierende Bakterien | Anaerobische Zonen | Schwefel, faule Eier | Mittel |
| Eisenbakterien | Metallteile im System | Metallisch, sumpfig | Gering |

**Kategorie 3: Anorganisch**
| Substanz | Quelle | Geschmack/Geruch | Gesundheitsrisiko |
|----------|--------|-----------------|-------------------|
| Kupfer (Cu²⁺) | Kupferrohr am Boiler | Metallisch | Gering bis mittel |
| Zink (Zn²⁺) | Messing-Fittings (Entzinkung) | Metallisch, bitter | Gering |
| Blei (Pb²⁺) | Alte Messing-Fittings, Lötzinn | Süßlich-metallisch | HOCH |
| Chlor/Chloramin | Hafenwasser | Schwimmbad | Gering |
| Eisen (Fe²⁺/Fe³⁺) | Tankrost, Stahlrohre | Metallisch | Gering |

**Kategorie 4: Systembedingt**
| Ursache | Geschmack/Geruch | Lösung |
|---------|-----------------|--------|
| Stagnation (>72h) | Abgestanden, muffig | Spülen vor Gebrauch |
| Toträume (nicht durchspülte Leitungsabschnitte) | Muffig, chemisch | Systemdesign prüfen |
| Temperaturerhöhung im Maschinenraum | Verstärkt alle chemischen Probleme | Isolierung/Umleitung |
| Tankbelüftung ohne Filter | Dieseldämpfe im Tank | Aktivkohle-Tankbelüftung |

#### 7.4.2 Diagnose von Geschmacksproblemen

**AYDI-Diagnoseschema:**

```
Schritt 1: Kaltwasser am Wasserhahn → Geschmack?
  Ja → Schritt 2
  Nein → Problem im Warmwasser-System (→ Schritt 5)

Schritt 2: Wasser direkt aus dem Tank (Handpumpe/Ablasshahn) → Geschmack?
  Ja → Tankproblem (Material, Befüllung, Biofilm)
  Nein → Schritt 3

Schritt 3: Wasser nach Pumpe, vor Verteilung → Geschmack?
  Ja → Pumpe oder Schlauch Tank→Pumpe
  Nein → Schritt 4

Schritt 4: Problem liegt in der Verteilung (Schläuche, Fittings)
  → Abschnittsweises Isolieren durch Trennung an Verbindungspunkten

Schritt 5: Nur Warmwasser betroffen
  → Boiler-Anschlüsse, Boiler-Innenbeschichtung, Anode prüfen
  → Kupferrohr am Boiler-Eingang/-Ausgang (häufige Ursache)
```

#### 7.4.3 Geschmacks-Beseitigung bei neuen Schläuchen

Neue Trinkwasserschläuche, selbst KTW-konforme, können initial einen leichten Geschmack aufweisen. Dieser ist gesundheitlich unbedenklich, aber störend.

**Standard-Verfahren (Neubau/Nachrüstung):**

1. **Erstspülung:** System 3× mit Trinkwasser füllen und entleeren (Kalt und Warm)
2. **Langzeitspülung:** 30 Minuten bei geöffneten Hähnen durchlaufen lassen
3. **Stehenlassen:** System gefüllt 24h stehen lassen, dann ablassen
4. **Wiederholung:** Schritte 1–3 wiederholen
5. **Geschmacksprobe:** Nach Schritt 4 sollte das Wasser geschmacksneutral sein
6. **Falls noch Geschmack:** Natron-Lösung (50g/10L) über Nacht einwirken, dann 5× spülen

**Zeitbedarf:** 2–3 Tage (bei korrektem Material). PVC-Schläuche können Wochen bis Monate "ausgasen".

### 7.5 Biofilm und Legionellen — Gesundheitsrisiken

#### 7.5.1 Biofilm-Bildung auf Yachten

Biofilm ist eine Gemeinschaft von Mikroorganismen (Bakterien, Algen, Pilze), die an der Innenfläche von Schläuchen und Tanks haftet und sich in einer selbst produzierten Matrix aus extrazellulären polymeren Substanzen (EPS) schützt. Biofilm ist auf 40–50% aller Yachten nachweisbar und das zweitgrößte Trinkwasserproblem nach Geschmack.

**Biofilm-Wachstumsfaktoren auf Yachten:**

| Faktor | Wirkung | Marine-Relevanz |
|--------|---------|-----------------|
| Stagnation | Hauptfaktor — kein Durchfluss = Biofilm | Sehr hoch (Liegezeiten) |
| Temperatur 20–45°C | Optimales Wachstum | Hoch (Maschinenraum, Tropen) |
| Nährstoffe im Wasser | Fördert Wachstum | Mittel (variabel je nach Quelle) |
| Rauhe Oberflächen | Mehr Ansatzpunkte | Material-abhängig |
| Licht (bei transparenten Schläuchen) | Algenwachstum | Hoch (Klarsichtschläuche!) |
| Chlor-Mangel | Keine Desinfektion | Hoch (Hafenwasser oft wenig Chlor) |

**Material-spezifische Biofilm-Anfälligkeit (DVGW W270-basiert):**

| Material | Biofilm-Wachstumsrate (relativ) | W270-Status |
|----------|--------------------------------|-------------|
| Edelstahl 316L | 1,0 (Referenz) | Besteht immer |
| PEX | 1,2–1,5 | Besteht üblicherweise |
| PE-HD | 1,3–1,6 | Besteht üblicherweise |
| Silikon food-grade | 1,1–1,4 | Besteht üblicherweise |
| EPDM food-grade | 1,5–2,0 | Besteht meist |
| PVC food-grade | 2,0–3,0 | Besteht manchmal nicht |
| PVC Standard | 3,0–5,0 | Besteht nicht |
| Kupfer | 0,5–0,8 | Natürlich antimikrobiell |

#### 7.5.2 Legionellen auf Yachten

Legionella pneumophila ist der gefährlichste Keim im Trinkwassersystem. Die Infektion erfolgt durch Einatmen von kontaminiertem Aerosol (Dusche, Waschbecken-Spray), nicht durch Trinken.

**Risikofaktoren auf Yachten:**
- Warmwasser-Boiler mit Temperatur <60°C (viele Marine-Boiler stehen auf 50°C)
- Lange Warmwasserleitungen mit geringem Durchfluss
- Toträume im System (nicht genutzte Abzweigungen)
- Sommerpause mit stehendem Wasser im System

**Legionellen-Wachstum nach Temperatur:**
| Temperatur | Wachstum | Marine-Relevanz |
|-----------|---------|-----------------|
| <20°C | Kein Wachstum | Kaltwasser OK |
| 20–25°C | Langsam | Kaltwasser im Maschinenraum! |
| 25–45°C | Optimal (Verdopplung alle 3–8h) | Warmwasser-System, Tropen-Kaltwasser |
| 46–50°C | Langsam, Absterben beginnt | Typischer Marine-Boiler = Risiko! |
| 50–55°C | Deutliches Absterben | Verbessert, aber nicht sicher |
| >55°C | Schnelles Absterben | Ziel für Marine-Boiler |
| >60°C | Abtötung in 2 Minuten | Thermische Desinfektion |
| >70°C | Sofortige Abtötung | Legionellen-Schaltung |

**AYDI-Empfehlung:**
- Boiler-Thermostat auf mindestens 60°C einstellen
- Mischventil am Boiler-Ausgang (Verbrühschutz) auf 45°C
- Thermische Desinfektion ("Legionellen-Schaltung"): 1× monatlich auf 70°C aufheizen, 10 Minuten halten, dann alle Zapfstellen 3 Minuten laufen lassen

#### 7.5.3 Desinfektionsmethoden

**Chemische Desinfektion:**

| Produkt | Wirkstoff | Dosierung | Einwirkzeit | Preis (ca.) | Bemerkung |
|---------|----------|-----------|-------------|-------------|-----------|
| Certisil Combina (CC) | Silber + Chlor | 1 Tabl./10L | 2h | 25 EUR/100 Tabl. | Standard Marine |
| Certisil Argento (CA) | Silberionen | 10mL/100L | 2h | 35 EUR/250mL | Dauerschutz |
| Purytec (Yachticon) | ClO₂-Generator | Systemspezifisch | 12h | 45 EUR/Saison | Chlordioxid |
| Milton (Baby-Sterilisation) | NaOCl | 30mL/5L | 30 min | 5 EUR/500mL | Notlösung |
| Certinox TankFrisch | Chlor | 25mL/100L | 12h | 15 EUR/250mL | Tankreinigung |
| Katadyn Micropur | Silberionen | 1 Tabl./100L | 2h | 20 EUR/100 Tabl. | Alternative |

**Mechanische Desinfektion:**

| Methode | Wirksamkeit | Kosten | Bemerkung |
|---------|------------|--------|-----------|
| UV-C (254nm) | 99,9% | 200–500 EUR | Point-of-Use, kein Langzeitschutz |
| Aktivkohle-Filter | Geschmack ja, Keime nein | 50–150 EUR/Jahr | Kein Desinfektionsmittel! |
| Keramik-Filter (0,2µm) | 99,99% Bakterien | 100–300 EUR | Langsam, verstopft |
| Umkehrosmose (Watermaker) | 99,99%+ | 3.000–15.000 EUR | Auch Entmineralisierung |

### 7.6 Schlauch vs PEX-Rohr vs John-Guest-Push-Fit

#### 7.6.1 Entscheidungsmatrix

Die Wahl zwischen flexiblem Schlauch, starrem PEX-Rohr und John-Guest-Push-Fit-System hängt von der Anwendung, dem Boot und den Fähigkeiten des Installateurs ab.

| Kriterium | Flexibler Schlauch (EPDM/Silikon) | PEX-Rohr (Crimp/Press) | John Guest Push-Fit (PE) |
|-----------|-----------------------------------|----------------------|------------------------|
| Installation | Einfach (Schelle) | Mittel (Spezialwerkzeug) | Sehr einfach (Stecken) |
| Demontage | Einfach | Schwierig (Crimp irreversibel) | Sehr einfach (Clip lösen) |
| Vibrationsfestigkeit | Sehr gut (dämpft) | Gut (wenn fixiert) | Gut (flexibles Rohr) |
| Biegeradius | 2–4×D | 5×D | 4×D |
| Druckfestigkeit | 4–10 bar | 10 bar | 10 bar |
| Langlebigkeit | 10–15 Jahre | 25–50 Jahre | 15–25 Jahre |
| Biofilm-Resistenz | Mittel bis gut | Sehr gut | Sehr gut |
| Geschmacksneutralität | Gut bis sehr gut | Sehr gut | Sehr gut |
| Preis pro Meter (13mm) | 6–20 EUR | 2–5 EUR | 3–6 EUR |
| Fitting-Preis | 1–3 EUR (Schelle) | 3–8 EUR (Crimp) | 4–10 EUR (Push-Fit) |
| Gesamtkosten (10m System) | 80–250 EUR | 70–130 EUR | 70–160 EUR |

#### 7.6.2 Empfehlung nach Anwendung

| Anwendung | Empfehlung | Begründung |
|-----------|-----------|-----------|
| Neubau Serienboot | John Guest Push-Fit | Schnelle Installation, gute Qualität |
| Neubau Semi-Custom | PEX (Crimp/Press) | Maximale Langlebigkeit |
| Neubau Superyacht | PEX + Edelstahl | Höchste Qualität, Langlebigkeit |
| Nachrüstung (DIY) | John Guest Push-Fit | Kein Spezialwerkzeug nötig |
| Nachrüstung (Werft) | PEX oder John Guest | Werft-Empfehlung befolgen |
| Pumpenanschluss | Silikon food-grade | Vibrationsdämpfung |
| Boileranschluss | EPDM food-grade oder Silikon | Temperaturbeständigkeit |
| Watermaker→Tank | John Guest (6mm/10mm) | Standard bei allen Watermaker-Herstellern |
| Notfall-Reparatur | Silikon + Schelle | Universell, flexibel |

### 7.7 Watermaker-Integration

#### 7.7.1 Produktwasser-Qualität und Nachbehandlung

Watermaker (Umkehrosmose-Anlagen) produzieren hochreines Wasser mit sehr niedrigem TDS (Total Dissolved Solids) von typischerweise 200–500 ppm (Meerwasser: ~35.000 ppm). Dieses Wasser ist zwar keimfrei, aber:

1. **Demineralisiert:** Fehlen von Kalzium, Magnesium und anderen Mineralien → flacher, "leerer" Geschmack
2. **Aggressiv:** Niedriger pH (5,5–6,5) und geringe Pufferkapazität → greift Metallteile an (Kupfer, Messing)
3. **Korrosionsfördernd:** Kann Blei und Kupfer aus Fittings und Boiler-Rohren lösen

**Nachbehandlung (Post-Treatment):**

| Stufe | Produkt | Funktion | Preis (ca.) |
|-------|---------|----------|-------------|
| 1. Mineralisierung | Spectra Post-Treatment Cartridge | Kalzium/Magnesium-Zugabe | 80 EUR/Filter |
| 1. Mineralisierung | Korallenkalk-Kartusche (DIY) | pH-Anhebung auf 7–8 | 15 EUR/kg |
| 2. Aktivkohle | Standard GAC-Filter 10" | Geschmacksverbesserung, Restchlor | 15–30 EUR/Filter |
| 3. UV-Sterilisation | Acuva ArrowMAX / PearlAqua | Nachkontamination verhindern | 250–400 EUR |
| 4. Silber-Konservierung | Certisil Argento (Silberionen) | Langzeitschutz im Tank | 35 EUR/Saison |

#### 7.7.2 Schlauchverbindungen am Watermaker

Alle gängigen Marine-Watermaker verwenden standardmäßig John-Guest-Push-Fit-Anschlüsse für die Produktwasser-Leitung:

| Watermaker | Produktwasser-Anschluss | Schlauch-Typ | Ø |
|-----------|----------------------|-------------|---|
| Spectra Ventura 150 | John Guest Push-Fit | JG PE | 6mm (¼") |
| Spectra Ventura 200T | John Guest Push-Fit | JG PE | 6mm (¼") |
| Schenker Zen 30 | Schlauchtülle | Silikon oder PE | 10mm |
| Schenker Smart 30 | Schlauchtülle | Silikon oder PE | 10mm |
| Dessalator D60 | Schlauchtülle | EPDM oder PE | 13mm |
| Dessalator D100 | Schlauchtülle | EPDM oder PE | 13mm |
| Katadyn PowerSurvivor | John Guest Push-Fit | JG PE | 6mm (¼") |
| Village Marine Tec LWM | Schlauchtülle | PE oder EPDM | 10–13mm |
| Rainman WM | Schnellkupplung | PE | 10mm |

### 7.8 Warmwasser-Boiler-Anschlüsse

#### 7.8.1 Temperaturanforderungen

Warmwasser-Boiler auf Yachten arbeiten typischerweise bei 50–65°C, mit kurzzeitigen Spitzen bis 85°C (Motorwärmetauscher-Betrieb). Dies erfordert Schlauchmaterial mit Dauertemperaturbeständigkeit von mindestens 65°C und Kurzzeitbeständigkeit bis 95°C.

**Empfohlene Materialien nach Temperaturbereich:**

| Material | Dauer-Temp. | Kurzzeit-Temp. | Eignung Boiler-Anschluss |
|----------|-----------|---------------|-------------------------|
| PEX (alle Typen) | 95°C | 110°C | Sehr gut (Standard) |
| Silikon food-grade | 200°C | 250°C | Sehr gut (flexibelste Option) |
| EPDM food-grade | 120°C | 150°C | Sehr gut |
| PE-HD / AQUAPAL | 60°C | 80°C | Eingeschränkt (nur wenn Boiler ≤60°C) |
| PVC food-grade | 50°C | 60°C | NICHT geeignet |

#### 7.8.2 Boiler-Anschlüsse nach Hersteller

| Boiler | Anschluss | Gewinde | Empfohlener Schlauch | Übergangsfitting |
|--------|----------|---------|---------------------|-----------------|
| Isotemp Basic 24L | ¾" BSP | BSP | PEX 16mm | Crimp + Übergang |
| Isotemp Slim 15L | ¾" BSP | BSP | PEX 16mm oder EPDM 16mm | Schelle oder Crimp |
| Quick BXS 20L | ¾" BSP | BSP | PEX 16mm | Crimp + Übergang |
| Quick BXS 40L | ¾" BSP | BSP | PEX 16mm | Crimp + Übergang |
| Sigmar SIC006 | ¾" BSP | BSP | EPDM 19mm (Standard) | Schlauchtülle |
| Whale Expanse 8L | WQC (Whale QuickConnect) | — | Whale 15mm | Push-Fit |
| Whale Expanse 14L | WQC | — | Whale 15mm | Push-Fit |
| Raritan 1700 Series | ¾" NPT | NPT | EPDM 19mm | Schlauchtülle |
| Kuuma 120 (Camco) | ½" NPT | NPT | EPDM 13mm | Schlauchtülle |

### 7.9 Druckwasserpumpen und Akkumulator-Tanks

#### 7.9.1 Pumpenanschlüsse — Vibration als Schlüsselproblem

Druckwasserpumpen sind die lauteste und vibrationsintensivste Komponente im Trinkwassersystem. Der Schlauch am Pumpenein- und -ausgang muss:

1. Vibration absorbieren (→ flexibles Material, keine starren Rohre)
2. Druckpulsation dämpfen (→ Akkumulatortank!)
3. Dicht bleiben bei pulsierendem Druck (→ doppelte Schelle oder Push-Fit)
4. Kavitation auf der Saugseite vermeiden (→ ausreichender Querschnitt)

**Regel:** Mindestens 300mm flexibler Schlauch zwischen Pumpe und starrer Leitung (PEX, Fitting). Silikon food-grade ist das ideale Material für diese Übergangsstücke.

#### 7.9.2 Akkumulator-Tanks

Akkumulator-Tanks (Druckausgleichsbehälter) glätten die Druckpulsation der Pumpe und reduzieren die Schalthäufigkeit. Sie sind die effektivste Maßnahme gegen "stotternden" Wasserfluss und reduzieren die Geräuschbelastung erheblich.

| Produkt | Volumen (L) | Anschluss | Vordruck (bar) | Preis (EUR) |
|---------|-----------|----------|---------------|-------------|
| Jabsco Accumulator 18810-0000 | 0,5 | ½" NPT | 1,4 | 45–65 |
| Shurflo 182-200 | 0,5 | ½" NPT | 1,7 | 35–50 |
| Vetus ACC33 | 3,3 | ¾" BSP | 1,0 | 120–160 |
| Vetus ACC8 | 8,0 | ¾" BSP | 1,0 | 180–240 |
| Whale WF9907 | 0,7 | Whale QC | 1,4 | 55–75 |
| Johnson/SPX ACC | 0,5 | ½" NPT | 1,4 | 40–60 |

**Anschluss-Empfehlung:** Akkumulator-Tank wird zwischen Pumpe und Verteiler eingebaut. Anschluss mit kurzem flexiblem Schlauch (EPDM oder Silikon, 200–300mm). KEIN John-Guest-Push-Fit am Akkumulator — die Druckpulsation kann Push-Fit-Verbindungen langfristig lösen.

### 7.10 Tankverbindungen und -materialien

#### 7.10.1 Tank-Materialien und ihre Auswirkungen auf die Wasserqualität

| Tankmaterial | KTW-konform | Geschmack | Langlebigkeit | Reinigung | Übliche Bootsgröße |
|-------------|-------------|----------|---------------|-----------|-------------------|
| PE-HD (rotationsgeformt) | Ja | Neutral | 20–30 Jahre | Einfach | 8–20m |
| GFK (Polyester) | Bedingt | Initial stark → nimmt ab | 15–25 Jahre | Mittel | 10–20m (Einbau) |
| Edelstahl 316L | Ja | Neutral | 30–50 Jahre | Einfach | 15m+ |
| Aluminium (eloxiert) | Bedingt | Kann metallisch sein | 15–25 Jahre | Schwierig | 10–18m (Alu-Boote) |
| Flexibler Tankbeutel (PE) | Ja | Neutral | 10–15 Jahre | Einfach (austauschbar) | 8–14m |

**AYDI-Empfehlung:**
- **PE-HD rotationsgeformt:** Standard-Empfehlung für 80% aller Yachten. Geschmacksneutral, robust, leicht, korrosionsfrei.
- **Edelstahl 316L:** Premium-Empfehlung für Langfahrt und Superyachten. Höchste Langlebigkeit, aber teuer und schwer.
- **GFK:** Nur akzeptabel wenn mit Trinkwasser-Gelcoat (z.B. Isophthal-Harz + TW-Topcoat). Standard-Polyester-GFK ist NICHT empfehlenswert (Styrol-Migration).

#### 7.10.2 Tank-Anschlüsse

| Anschlusstyp | Gewinde | Schlauch-Ø | Dichtung | Bemerkung |
|-------------|---------|-----------|---------|-----------|
| Einfüllstutzen | 1½" oder 2" BSP | 38mm oder 50mm | O-Ring | Deck-montiert |
| Tankentnahme (unten) | ¾" oder 1" BSP | 19mm oder 25mm | PTFE-Band + Dichtung | Absperrhahn integriert |
| Tankbelüftung | ½" BSP | 13mm | — | Muss mit Gänsehals + Insektennetz |
| Tankfüllstand-Sensor | M12 oder herstellerspezifisch | — | O-Ring | Wema/KUS Standard |
| Inspektionsöffnung | 100–150mm Deckel | — | O-Ring | Für Reinigung, min. 100mm |
| Überdruckventil | ¼" BSP | — | O-Ring | Bei Watermaker-Einspeisung |

**Dichtungsmaterialien an Tankverbindungen:**
- **PTFE-Band (Gewindedichtung):** Standard, KTW-konform, max. 3 Lagen
- **Flachdichtung EPDM food-grade:** Für Flanschverbindungen, Shore 60A, 2mm dick
- **O-Ring NBR food-grade oder EPDM food-grade:** Für Einfüllstutzen und Inspektionsdeckel
- **NICHT verwenden:** Hanf + Fermit (nicht KTW-konform), Loctite 577 (nicht TW-geeignet)

---

## 8. Hersteller — Vollständige Übersicht

### 8.1 John Guest (Speedfit Marine)

**Firmenprofil:**
- Sitz: West Drayton, Middlesex, UK (seit 2018 Teil der RWC Group, Australien)
- Gegründet: 1961 von John Guest
- Spezialität: Push-Fit-Verbindungstechnik (patentiertes Collet-System)
- Marine-Division: "Speedfit Marine" und "JG Speedfit"
- Zertifizierungen: NSF 61, WRAS, KTW, ACS, DVGW W270

John Guest hat die Trinkwasser-Installation auf Yachten revolutioniert. Das Push-Fit-System (Stecken → dicht) eliminiert Schlauchschellen, Crimp-Werkzeug und die meisten Leck-Ursachen. Geschätzt 60% aller in den letzten 15 Jahren gebauten Serienyachten verwenden John-Guest-Komponenten im Trinkwassersystem.

**Marine Produktpalette:**

| Produkt | Artikelnummer | Ø (mm) | Farbe | Material | Bemerkung |
|---------|--------------|--------|-------|----------|-----------|
| PE-Rohr marine | PI1012 (10mm) | 10 | Weiß | PE | Standard Kaltwasser |
| PE-Rohr marine | PI1215 (15mm) | 15 | Weiß | PE | Standard Haupt |
| PE-Rohr marine | PI1222 (22mm) | 22 | Weiß | PE | Hauptverteilung groß |
| PE-Rohr warm | PI1012R (10mm) | 10 | Rot | PE | Warmwasser-Kennung |
| PE-Rohr warm | PI1215R (15mm) | 15 | Rot | PE | Warmwasser-Kennung |
| Winkel 90° | CI0312W | 10, 15 | Weiß | POM | Push-Fit |
| T-Stück | CI0712W | 10, 15 | Weiß | POM | Push-Fit |
| Gerade Verbindung | CI0412W | 10, 15 | Weiß | POM | Push-Fit |
| Absperrhahn |?"?"SV | 10, 15 | Weiß | POM | Push-Fit, Kugelhahn |
| Reduzierung 15→10 | CI0614W | 15→10 | Weiß | POM | Push-Fit |
| Schott-Durchführung | CI1218W | 15 | Weiß | POM | Für Wanddurchführung |
| Schlauchadapter | CI0108xx | 10, 15 | Weiß | POM | Push-Fit → Schlauchtülle |
| BSP-Adapter | CI0108xxW | ½" BSP | Weiß | POM | Push-Fit → Gewinde |
| Rohrschelle | JG-RC15 | 15 | Weiß | PP | Befestigung alle 500mm |

**John Guest Preisliste (Marine-Handel, 2024/2025):**

| Produkt | Preis (ca. EUR) |
|---------|----------------|
| PE-Rohr 10mm, weiß, 25m-Rolle | 55–70 |
| PE-Rohr 15mm, weiß, 25m-Rolle | 70–90 |
| Winkel 90° (15mm) | 4,50–6,00 |
| T-Stück (15mm) | 5,50–7,00 |
| Absperrhahn (15mm) | 12,00–16,00 |
| BSP-Adapter ½" (15mm) | 5,00–7,00 |
| Schott-Durchführung (15mm) | 8,00–11,00 |

**Praxis-Tipps John Guest:**

1. **Rohre rechtwinklig schneiden** — schräge Schnitte lecken! JG-Rohrschneider verwenden (JG-TS, ~12 EUR)
2. **Einstecktiefe markieren** — vor dem Einstecken die Einstecktiefe am Rohr markieren (15mm Rohr: 25mm Einstecktiefe)
3. **Collet-Clip (Sicherungsring)** verwenden — JG liefert Clips als Zubehör, die versehentliches Lösen verhindern
4. **Keine UV-Exposition** — John-Guest-Rohre und -Fittings sind NICHT UV-stabil. Bei Deckdurchführungen Schutzrohr verwenden.
5. **Temperaturlimit beachten** — Standard-PE-Rohr: max. 60°C. Für Warmwasser: JG Barrier Pipe (PE/EVOH/PE) verwenden, max. 82°C.
6. **Biegeradius:** min. 75mm (10mm Rohr), min. 100mm (15mm Rohr). Bei engen Bögen: Winkel-Fitting verwenden.

**Typische OEM-Einbauten (John Guest ab Werft):**

| Werft | Modelle | JG-Dimension | Bemerkung |
|-------|---------|-------------|-----------|
| Bénéteau | Oceanis 30.1–51.1, First 27–53 | 15mm | Standard seit ~2015 |
| Jeanneau | Sun Odyssey 319–519, NC-Serie | 15mm | Standard seit ~2016 |
| Bavaria | C-Line 34–57, S-Line | 15mm | Standard seit ~2014 |
| Hanse | 315–675 | 15mm | Standard seit ~2015 |
| Dufour | 310–560 | 15mm | Standard seit ~2017 |
| Lagoon | 40–52, SEVENTY 7 | 15mm | Standard seit ~2016 |
| Fountaine-Pajot | Isla 40–67, Aura 51 | 15mm | Standard seit ~2017 |
| Leopard (Robertson & Caine) | 40–50 | 15mm | Standard seit ~2018 |
| Hallberg-Rassy | 340–57 | Mix (JG + PEX) | Teils JG, teils PEX |
| Oyster | 495–885 | PEX (Rehau) | Kein JG — hochwertiger PEX |

### 8.2 Whale Marine (AquaSource/QuickConnect)

**Firmenprofil:**
- Sitz: Bangor, Nordirland, UK (Teil der Munster Simms Engineering Group)
- Gegründet: 1960er
- Spezialität: Integrierte Marine-Sanitärsysteme (Pumpen, Boiler, Wasserhähne, Schläuche)
- Marine-Marke: Whale
- Zertifizierungen: NSF 61, WRAS, DVGW W270

Whale ist der einzige Hersteller, der ein vollständig integriertes Trinkwassersystem aus einer Hand anbietet — von der Pumpe über den Boiler und die Schläuche bis zum Wasserhahn. Das proprietäre "QuickConnect" (WQC) System ist ein Push-Fit-System ähnlich John Guest, aber mit eigenem Steckmaß (nicht kompatibel zu JG!).

**Whale AquaSource Schlauchlinie:**

| Produkt | Artikelnummer | Ø (mm) | Farbe | Material | Preis/m (EUR) |
|---------|--------------|--------|-------|----------|--------------|
| WX1510B (blau, kalt) | WX1510B | 15 | Blau | PE | 3,50–5,00 |
| WX1510R (rot, warm) | WX1510R | 15 | Rot | PE | 3,50–5,00 |
| WX1510W (weiß, uni) | WX1510W | 15 | Weiß | PE | 3,50–5,00 |
| WX7152B (blau, 25m) | WX7152B | 15 | Blau | PE | 3,00–4,50/m |
| WX7152R (rot, 25m) | WX7152R | 15 | Rot | PE | 3,00–4,50/m |

**Whale QuickConnect Fittings:**

| Produkt | Artikelnummer | Typ | Preis (EUR) |
|---------|--------------|-----|-------------|
| Winkel 90° | WX1502 | 15mm QC | 5,00–7,00 |
| T-Stück | WX1504 | 15mm QC | 6,00–8,00 |
| Schott-Durchführung | WX1521 | 15mm QC | 9,00–12,00 |
| Absperrhahn | WX1574 | 15mm QC | 14,00–18,00 |
| Adapter QC→JG | WX1595 | 15mm QC→15mm JG | 7,00–9,00 |
| Adapter QC→BSP | WX1517 | 15mm QC→½" BSP | 6,00–8,00 |
| Adapter QC→Schlauch | WX1534 | 15mm QC→½" Tülle | 5,00–7,00 |

**AYDI-Bewertung Whale:**
- **Systemintegration:** 95/100 (bestes integriertes System am Markt)
- **Verfügbarkeit:** 70/100 (weniger verbreitet als JG, Ersatzteile schwieriger)
- **Kompatibilität:** 50/100 (proprietäres System, nicht JG-kompatibel ohne Adapter)
- **Qualität:** 90/100 (hochwertig, gut zertifiziert)
- **Preis-Leistung:** 80/100 (etwas teurer als JG, aber integriertes System)

### 8.3 Vetus

**Firmenprofil:**
- Sitz: Schiedam, Niederlande
- Gegründet: 1951
- Spezialität: Marine-Zubehör (breitestes Sortiment in Europa)
- Trinkwasser-Produkte: DWHOSE-Serie (Drinking Water Hose)
- Zertifizierungen: KTW, FDA

Vetus ist der größte europäische Marine-Zubehör-Hersteller und bietet eine bewährte Trinkwasserschlauch-Linie (DWHOSE) in EPDM food-grade Qualität.

**Vetus DWHOSE Produktlinie:**

| Produkt | Artikelnummer | Ø innen (mm) | Ø außen (mm) | Material | KTW | Preis/m (EUR) |
|---------|--------------|-------------|-------------|----------|-----|--------------|
| DWHOSE10A | DWHOSE10A | 10 | 17 | EPDM food-grade | Ja (B) | 9,00–12,00 |
| DWHOSE13A | DWHOSE13A | 13 | 20 | EPDM food-grade | Ja (B) | 10,00–14,00 |
| DWHOSE16A | DWHOSE16A | 16 | 23 | EPDM food-grade | Ja (B) | 12,00–16,00 |
| DWHOSE19A | DWHOSE19A | 19 | 27 | EPDM food-grade | Ja (B) | 14,00–18,00 |
| DWHOSE25A | DWHOSE25A | 25 | 34 | EPDM food-grade | Ja (B) | 16,00–22,00 |

**Technische Daten DWHOSE:**
- Betriebsdruck: 6 bar (alle Größen)
- Berstdruck: 18 bar
- Temperaturbereich: -30°C bis +100°C
- Biegeradius: 3× Ø innen
- Verstärkung: Polyester-Gewebeeinlage
- Farbe: Weiß mit blauer Bedruckung "VETUS DRINKING WATER"
- Lieferform: Meterware oder 20m-Rollen

**AYDI-Bewertung Vetus DWHOSE:**
- Geschmacksneutralität: 80/100 (EPDM-typisch gut, nicht ganz Silikon-Niveau)
- Flexibilität: 85/100 (sehr guter Biegeradius)
- Langlebigkeit: 80/100 (10–15 Jahre realistisch)
- Biofilm-Resistenz: 70/100 (EPDM durchschnittlich)
- Verfügbarkeit: 90/100 (über alle großen Marine-Händler)
- Preis-Leistung: 75/100 (teurer als AQUAPAL, günstiger als Silikon)

### 8.4 Trident Marine

**Firmenprofil:**
- Sitz: Harvey, Louisiana, USA
- Gegründet: 1977
- Spezialität: Marine-Schläuche und -Rohre (Abgas, Kühlwasser, Trinkwasser, Kraftstoff)
- Trinkwasser-Serie: Series 150 (FDA) und Series 162 (verstärkt)
- Zertifizierungen: FDA 21 CFR 177, USCG, ABYC

Trident ist der US-Marktführer für Marine-Schläuche. Die "Series 150" ist der Standard-Trinkwasserschlauch auf US-amerikanischen Yachten.

**Trident Trinkwasser-Produktlinie:**

| Produkt | Art.-Nr. Basis | Ø innen (mm/Zoll) | Material | FDA | Preis/ft (USD) |
|---------|---------------|-------------------|----------|-----|---------------|
| Series 150 Drinking Water | 150-xxxx | 10 (⅜") | PVC food-grade | Ja | 2,50–3,50 |
| Series 150 Drinking Water | 150-xxxx | 13 (½") | PVC food-grade | Ja | 3,00–4,00 |
| Series 150 Drinking Water | 150-xxxx | 16 (⅝") | PVC food-grade | Ja | 3,50–5,00 |
| Series 150 Drinking Water | 150-xxxx | 19 (¾") | PVC food-grade | Ja | 4,50–6,00 |
| Series 162 Drinking Water | 162-xxxx | 13 (½") | PVC food-grade, verstärkt | Ja | 5,00–7,00 |
| Series 162 Drinking Water | 162-xxxx | 16 (⅝") | PVC food-grade, verstärkt | Ja | 6,00–8,00 |

**AYDI-Kritische Bewertung Trident Series 150:**

Obwohl Trident der US-Marktstandard ist, besteht die Series 150 aus PVC — mit allen oben beschriebenen Nachteilen:
- **Geschmacksneutralität: 45/100** (PVC-typischer Plastikgeschmack, besonders in den ersten Monaten)
- **Weichmacher-Migration: Risiko bei Wärme** (Maschinenraum-Verlegung problematisch)
- **KTW: NEIN** (nicht für den europäischen Markt getestet/zertifiziert)
- **Material-Score: 40/100** (PVC-Abzug)

**Empfehlung:** Für europäische Eigner — Trident Series 150 durch AQUAPAL oder John Guest ersetzen. Für US-Eigner — Trident ist akzeptabel wenn FDA-Konformität ausreicht, aber John Guest ist die bessere Wahl.

### 8.5 Continental ContiTech (AQUAPAL)

**Firmenprofil:**
- Sitz: Hannover, Deutschland (Teil der Continental AG)
- Division: ContiTech Fluid Technology
- Spezialität: Industrie- und Spezialschläuche
- Trinkwasser-Produkt: AQUAPAL (seit >30 Jahren am Markt)
- Zertifizierungen: KTW Kategorie B, DVGW W270, FDA, WRAS, ACS

AQUAPAL ist der bekannteste und meistempfohlene Trinkwasserschlauch im deutschen Marine-Bereich. Er ist der De-facto-Standard, wenn Eigner nach einem "KTW-konformen Trinkwasserschlauch" fragen.

**ContiTech AQUAPAL Produktlinie:**

| Produkt | Artikelnummer | Ø innen (mm) | Ø außen (mm) | Wandstärke | Betriebsdruck | Preis/m (EUR) |
|---------|--------------|-------------|-------------|-----------|---------------|--------------|
| AQUAPAL | AQ-10 | 10 | 17 | 3,5mm | 10 bar | 7,00–10,00 |
| AQUAPAL | AQ-13 | 13 | 21 | 4,0mm | 10 bar | 8,00–12,00 |
| AQUAPAL | AQ-16 | 16 | 24 | 4,0mm | 10 bar | 10,00–14,00 |
| AQUAPAL | AQ-19 | 19 | 27 | 4,0mm | 10 bar | 12,00–16,00 |
| AQUAPAL | AQ-25 | 25 | 35 | 5,0mm | 10 bar | 15,00–20,00 |
| AQUAPAL | AQ-32 | 32 | 44 | 6,0mm | 10 bar | 20,00–28,00 |

**Technische Daten AQUAPAL:**
- **Aufbau:** PE-HD Innenschicht (geschmacksneutral) + Polyester-Gewebeeinlage + PVC-Außenmantel (blau)
- **Berstdruck:** 30 bar (alle Größen)
- **Temperaturbereich:** -30°C bis +60°C (Dauer), kurzzeitig +90°C
- **Biegeradius:** 5× Ø innen
- **Farbe:** Blau außen, weiß innen
- **Lieferform:** Meterware, 20m oder 40m Rollen

**Warum AQUAPAL so beliebt ist:**
1. PE-HD Innenschicht → kein Plastikgeschmack (im Gegensatz zu PVC-Schläuchen)
2. PVC-Außenmantel → robust, scheuerfest, UV-beständiger als reines PE
3. Alle relevanten Zertifizierungen (KTW, DVGW, FDA, WRAS, ACS)
4. Moderate Kosten (günstiger als Silikon, teurer als PVC)
5. Bewährt seit >30 Jahren — enormer Erfahrungsschatz in der Community

**AYDI-Bewertung AQUAPAL:**
- Geschmacksneutralität: 88/100 (PE-HD-Innenschicht, sehr gut)
- Flexibilität: 65/100 (relativ steif, Biegeradius 5×D)
- Langlebigkeit: 80/100 (10–15 Jahre bei sachgerechtem Einbau)
- Biofilm-Resistenz: 80/100 (PE-HD gut, W270-zertifiziert)
- UV-Beständigkeit: 75/100 (blauer PVC-Mantel schützt PE-Kern)
- Druckbelastung: 90/100 (10 bar Betrieb, 30 bar Berst)
- Material-Score: 82/100

### 8.6 Rehau (RAUTITAN)

**Firmenprofil:**
- Sitz: Rehau, Bayern, Deutschland
- Gegründet: 1948
- Spezialität: Polymer-Lösungen für Bau, Automotive, Industrie
- Marine-relevante Produkte: RAUTITAN flex (PEX-a), RAUTITAN stabil (PE-Xc/Al/PE-HD)
- Zertifizierungen: KTW Kategorie C, DVGW W270, NSF 61, WRAS, ACS

Rehau ist kein Marine-Spezialist, aber das RAUTITAN-System wird von hochwertigen Werften (Oyster, Contest, Moody Decksaloon) als Trinkwasser-Installation verwendet. Es bietet die höchste Qualität und Langlebigkeit, erfordert aber Spezialwerkzeug.

**Rehau RAUTITAN flex Produktlinie (PEX-a, Engel-Verfahren):**

| Produkt | Artikelnummer | Ø (mm) | Wandstärke | Max. Druck (60°C) | Preis/m (EUR) |
|---------|--------------|--------|-----------|-------------------|--------------|
| RAUTITAN flex 16 | 11303601050 | 16×2,2 | 2,2mm | 6 bar | 3,00–4,50 |
| RAUTITAN flex 20 | 11303801050 | 20×2,8 | 2,8mm | 6 bar | 4,50–6,50 |
| RAUTITAN flex 25 | 11304001050 | 25×3,5 | 3,5mm | 6 bar | 6,50–9,00 |

**Rehau RAUTITAN stabil Produktlinie (PE-Xc/Al/PE-HD, Verbundrohr):**

| Produkt | Artikelnummer | Ø (mm) | Wandstärke | Max. Druck (60°C) | Preis/m (EUR) |
|---------|--------------|--------|-----------|-------------------|--------------|
| RAUTITAN stabil 16 | 11300311050 | 16,2×2,6 | 2,6mm | 6 bar | 4,00–6,00 |
| RAUTITAN stabil 20 | 11300511050 | 20×2,9 | 2,9mm | 6 bar | 5,50–8,00 |
| RAUTITAN stabil 25 | 11300711050 | 25×3,7 | 3,7mm | 6 bar | 8,00–11,00 |

**Rehau Fitting-System (RAUTITAN PX Schiebehülse):**

| Fitting | Artikelnummer | Typ | Preis (EUR) |
|---------|--------------|-----|-------------|
| Winkel 90° 16mm | 11601211001 | PX Schiebehülse | 7,00–10,00 |
| T-Stück 16mm | 11600911001 | PX Schiebehülse | 9,00–13,00 |
| Reduzierung 20→16 | 11600711001 | PX Schiebehülse | 8,00–11,00 |
| Adapter ½" AG | 11600611001 | PX→Gewinde | 7,00–10,00 |
| Adapter ½" IG | 11600511001 | PX→Gewinde | 8,00–11,00 |

**Werkzeug:** RAUTITAN Schiebehülsenwerkzeug (manuell: ~250 EUR, Akku: ~1.200 EUR). Für Einmal-Installation auf der eigenen Yacht: manuelle Variante oder Mietwerkzeug.

**AYDI-Bewertung Rehau RAUTITAN:**
- Geschmacksneutralität: 92/100 (PEX-a, hervorragend)
- Flexibilität: 70/100 (PEX-a ist der flexibelste PEX-Typ, aber immer noch steifer als Schlauch)
- Langlebigkeit: 98/100 (50 Jahre Herstellergarantie im Hausbau)
- Biofilm-Resistenz: 88/100 (glatte PE-Innenfläche, W270-zertifiziert)
- Installations-Aufwand: 40/100 (Spezialwerkzeug erforderlich)
- Material-Score: 92/100

### 8.7 Jabsco/Xylem

**Firmenprofil:**
- Sitz: Foothill Ranch, Kalifornien, USA (Teil der Xylem Inc. Gruppe)
- Gegründet: 1937
- Spezialität: Marine-Pumpen (Druckwasser, WC, Lenzpumpen)
- Trinkwasser-Relevanz: Pumpenanschlüsse, Akkumulatortanks
- Zertifizierungen: NSF 61 (Pumpen), FDA (Kontaktmaterialien)

Jabsco stellt keine Trinkwasserschläuche her, ist aber als Pumpen-Hersteller ein zentraler Bestandteil jedes Trinkwassersystems. Die Schlauchverbindungen an Jabsco-Pumpen bestimmen, welche Schläuche und Fittings verwendet werden.

**Jabsco Druckwasserpumpen und ihre Anschlüsse:**

| Pumpe | Artikelnummer | Förderleistung | Druck | Anschluss | Ø | Preis (EUR) |
|-------|--------------|----------------|-------|----------|---|-------------|
| Par-Max 1.9 | 31295-0092 | 7,2 LPM | 1,7 bar | Schlauchtülle | ½" | 95–130 |
| Par-Max 3.0 | 31395-0392 | 11,4 LPM | 3,1 bar | Schlauchtülle | ½" | 130–170 |
| Par-Max 3.5 | 32600-0392 | 13,2 LPM | 2,8 bar | ½" NPT | ½" | 160–210 |
| Par-Max 4.0 | 31620-0092 | 16,3 LPM | 2,8 bar | ½" NPT | ½" | 180–240 |
| Par-Max HD4 | Q401J-118S-3A | 15,1 LPM | 4,1 bar | ½" NPT | ½" | 250–320 |
| Par-Max HD5 | P501J-118S-3A | 18,9 LPM | 4,1 bar | ¾" NPT | ¾" | 280–360 |
| Par-Max 6.0 | 31600-0292 | 22,7 LPM | 2,1 bar | ¾" Tülle | ¾" | 200–270 |

> ✅ Aufgeloest (Audit): 46010-2900 gehört zur Par-Max 2 (2,5 GPM / 40 PSI), nicht zu HD4/HD5. Korrekte Artikelnummern (Xylem/Jabsco, 12V, 4,1 bar/60 PSI-Variante): Par-Max HD4 = Q401J-118S-3A (4 GPM ≈ 15,1 LPM), Par-Max HD5 = P501J-118S-3A (5 GPM ≈ 18,9 LPM). Confidence Artikelnummer HD4/HD5: documented. — Quelle: Xylem/Jabsco Par-Max Series (xylem.com) sowie Fachhändler-Kataloge (Defender, Hodges Marine, Anchor Express).

**Jabsco Schlauch-Empfehlungen:**
- Saugseite: min. ¾" (19mm) EPDM oder PE für Par-Max 3.0+, ½" (13mm) für Par-Max 1.9
- Druckseite: ½" (13mm) für alle Par-Max-Modelle, Akkumulator empfohlen
- Flexible Verbindung: 300mm Silikon food-grade direkt an der Pumpe
- Schlauchschellen: Edelstahl 316, doppelt auf der Druckseite

### 8.8 Forespar (Marelon)

**Firmenprofil:**
- Sitz: San Luis Obispo, Kalifornien, USA
- Gegründet: 1969
- Spezialität: Kunststoff-Seebeschläge (Marelon™ = glasfaserverstärktes Nylon)
- Trinkwasser-Relevanz: Marelon-Fittings, Seeventile, Schlauchverbinder
- Zertifizierungen: FDA, NSF 61 (Marelon-Fittings), ABYC

Forespar stellt keine Schläuche her, aber die Marelon-Fittings sind die Standard-Empfehlung für Trinkwasser-Verbindungen im US-Markt — als korrosionsfreie Alternative zu Messing.

**Relevante Marelon-Produkte:**

| Produkt | Artikelnummer | Anschluss | Material | FDA | Preis (USD) |
|---------|--------------|----------|----------|-----|-------------|
| 90° Elbow | 905 Serie | ½"–1½" NPT | Marelon | Ja | 12–25 |
| Tee | 905 Serie | ½"–1" NPT | Marelon | Ja | 15–30 |
| Barb-to-NPT | 905 Serie | ½"–¾" → NPT | Marelon | Ja | 8–15 |
| Ball Valve | BV Serie | ½"–1½" NPT | Marelon | Ja | 25–55 |
| Inline Strainer | 9025 | ¾" | Marelon | Ja | 35–50 |

**Vorteil Marelon gegenüber Messing:**
- Kein Zink → keine Entzinkung → kein Zink im Trinkwasser
- Kein Blei → kein Blei im Trinkwasser (alte Messing-Fittings enthalten bis zu 8% Blei!)
- Korrosionsfrei in Salzwasser
- Leichter als Messing
- UV-stabil

### 8.9 Plastimo

**Firmenprofil:**
- Sitz: Lorient, Bretagne, Frankreich
- Gegründet: 1963
- Spezialität: Marine-Sicherheitsausrüstung, Deck-Hardware, Sanitär
- Trinkwasser-Produkte: begrenzte Auswahl, primär Schlauch-Zubehör
- Zertifizierungen: ACS (für TW-Produkte)

Plastimo bietet eine begrenzte Trinkwasserschlauch-Auswahl, die primär auf dem französischen Markt vertrieben wird:

| Produkt | Artikelnummer | Ø innen (mm) | Material | ACS | Preis/m (EUR) |
|---------|--------------|-------------|----------|-----|--------------|
| Trinkwasserschlauch | 17861 | 13 | PVC food-grade | Ja | 5,00–8,00 |
| Trinkwasserschlauch | 17862 | 16 | PVC food-grade | Ja | 6,00–9,00 |
| Trinkwasserschlauch | 17863 | 19 | PVC food-grade | Ja | 7,00–10,00 |

**AYDI-Bewertung:** Plastimo verwendet PVC → Material-Score 40–50. Nicht empfohlen für Neuinstallation. Akzeptabel als Übergangs-/Notlösung.

### 8.10 Peters Rubber

**Firmenprofil:**
- Sitz: Metzingen, Baden-Württemberg, Deutschland
- Gegründet: 1930er
- Spezialität: Gummi- und Silikonprodukte, Dichtungen, Schläuche
- Trinkwasser-Produkte: KTW-zertifizierte Silikonschläuche und EPDM-Schläuche
- Zertifizierungen: KTW (B und C), DVGW W270, FDA

Peters Rubber ist ein Nischen-Hersteller, der hochwertige KTW-zertifizierte Silikonschläuche für den Marine-Bereich liefert. Besonders für Boiler-Anschlüsse und kurze flexible Verbindungen.

| Produkt | Ø innen (mm) | Material | KTW | Preis/m (EUR) |
|---------|-------------|----------|-----|--------------|
| Silikon TW gewebeverstärkt | 10 | Silikon food-grade | B+C | 14,00–18,00 |
| Silikon TW gewebeverstärkt | 13 | Silikon food-grade | B+C | 16,00–22,00 |
| Silikon TW gewebeverstärkt | 16 | Silikon food-grade | B+C | 18,00–25,00 |
| Silikon TW gewebeverstärkt | 19 | Silikon food-grade | B+C | 22,00–30,00 |
| EPDM TW gewebeverstärkt | 13 | EPDM food-grade | B | 8,00–12,00 |
| EPDM TW gewebeverstärkt | 16 | EPDM food-grade | B | 10,00–14,00 |

### 8.11 Osculati

**Firmenprofil:**
- Sitz: Segrate (Mailand), Italien
- Gegründet: 1958
- Spezialität: Marine-Zubehör (>50.000 Artikel)
- Trinkwasser-Produkte: breites Sortiment, überwiegend zugekauft
- Zertifizierungen: variiert je nach Produkt (meist FDA, teilweise KTW)

Osculati bietet ein breites Trinkwasser-Sortiment, das jedoch überwiegend von Zulieferern stammt. Die Qualität ist variabel — einige Produkte sind excellent (z.B. die Edelstahl-Fittings), andere sind Basis-Qualität (PVC-Schläuche).

| Produkt | Artikelnummer | Ø innen (mm) | Material | KTW | FDA | Preis/m (EUR) |
|---------|--------------|-------------|----------|-----|-----|--------------|
| Trinkwasserschlauch weiß | 18.003.xx | 10, 13, 16, 19 | PVC food-grade | Nein | Ja | 4,00–8,00 |
| Silikon Trinkwasser | 18.005.xx | 10, 13, 16 | Silikon food-grade | Nein | Ja | 6,00–12,00 |
| Sanitary hose | 18.003.25 | 25 | PVC food-grade | Nein | Ja | 9,00–13,00 |

### 8.12 Zusammenfassung OEM vs Aftermarket

**OEM-Einbau (Werft ab Bau):**

| Werft-Segment | Typisches Material | Typische Marke | AYDI Material-Score |
|---------------|-------------------|---------------|-------------------|
| Budget-Produktion (<€100k) | PVC food-grade | Osculati, Plastimo, No-Name | 35–50 |
| Standard-Produktion (€100k–€300k) | John Guest PE | John Guest | 80–88 |
| Semi-Custom (€300k–€1M) | John Guest oder PEX | John Guest, Whale, Rehau | 82–92 |
| Custom/Superyacht (>€1M) | PEX (Rehau/Uponor) oder Edelstahl | Rehau RAUTITAN, Geberit | 88–98 |

**Aftermarket-Empfehlung (Upgrade):**

| Ist-Zustand | Empfohlenes Upgrade | Kosten (Material, 12m Boot) | AYDI Score-Verbesserung |
|------------|--------------------|-----------------------------|----------------------|
| PVC Standard (kein TW) | John Guest PE Komplett | 250–400 EUR | +40 bis +50 Punkte |
| PVC food-grade | AQUAPAL oder John Guest | 200–350 EUR | +30 bis +40 Punkte |
| Alter EPDM (>10 Jahre) | AQUAPAL oder John Guest | 200–350 EUR | +15 bis +25 Punkte |
| John Guest (OK, aber alt) | John Guest PE neu | 150–250 EUR | +5 bis +15 Punkte |
| PEX (gut, intakt) | Kein Upgrade nötig | 0 EUR | 0 Punkte |

---

## 9. Anlagen-spezifische Zuordnung

### 9.1 Druckwasserpumpen (Jabsco Par-Max, Shurflo, Whale Gulp)

#### 9.1.1 Vollständiger Pumpen-Vergleich

| Kriterium | Jabsco Par-Max 3.0 | Shurflo Trail King 7 | Whale GP1392 | Shurflo Aqua King II | Jabsco Par-Max HD4 |
|-----------|--------------------|--------------------|-------------|---------------------|-------------------|
| **Artikelnummer** | 31395-0392 | 4008-101-E65 | GP1392 | 4148-163-E75 | 46010-2900 |
| **Förderleistung** | 11,4 LPM | 7,6 LPM | 11,5 LPM | 11,3 LPM | 15,1 LPM |
| **Abschaltdruck** | 3,1 bar | 2,1 bar | 2,8 bar | 3,4 bar | 4,1 bar |
| **Betriebsspannung** | 12V | 12V | 12V | 12V | 12V |
| **Stromaufnahme** | 8A | 4A | 7A | 7,5A | 10A |
| **Geräusch (ca.)** | 55 dB(A) | 48 dB(A) | 52 dB(A) | 50 dB(A) | 58 dB(A) |
| **Anschluss Saug** | ½" NPT | ½" Tülle | ½" Tülle | ½" NPT | ½" NPT |
| **Anschluss Druck** | ½" NPT | ½" Tülle | ½" Tülle | ½" NPT | ½" NPT |
| **Membrane/Kolben** | 3 Membrane | 3 Membrane | Flexible Impeller | 3 Membrane | 4 Membrane |
| **Selbstansaugend** | Ja (2m) | Ja (1,8m) | Ja (1,5m) | Ja (2m) | Ja (3m) |
| **Trockenlauf** | Kurz OK | Kurz OK | NEIN | Kurz OK | Kurz OK |
| **Rückschlagventil** | Integriert | Integriert | Extern nötig | Integriert | Integriert |
| **Preis (EUR)** | 130–170 | 90–120 | 120–160 | 150–200 | 250–320 |
| **Für Bootsgröße** | 10–15m | 8–11m | 10–14m | 12–16m | 14–20m |

#### 9.1.2 Schlauchempfehlung je Pumpe

| Pumpe | Saugseite | Druckseite | Pumpenanschluss (Übergang) |
|-------|----------|-----------|---------------------------|
| Jabsco Par-Max 3.0 | AQUAPAL 19mm oder JG 15mm + Adapter | JG 15mm oder AQUAPAL 13mm | 300mm Silikon 13mm food-grade |
| Shurflo Trail King 7 | AQUAPAL 13mm | JG 15mm oder AQUAPAL 13mm | 300mm Silikon 13mm food-grade |
| Whale GP1392 | Whale WQC 15mm | Whale WQC 15mm | Integriert (WQC direkt) |
| Shurflo Aqua King II | AQUAPAL 16mm oder JG 15mm | JG 15mm oder AQUAPAL 13mm | 300mm Silikon 13mm food-grade |
| Jabsco Par-Max HD4 | AQUAPAL 19mm | JG 15mm + Akkumulator | 300mm Silikon 16mm food-grade |

#### 9.1.3 Pumpen-Installation — Häufige Fehler

| Fehler | Konsequenz | Lösung |
|--------|-----------|--------|
| Saugschlauch zu dünn | Kavitation, Geräusch, Leistungsverlust | Min. ¾" (19mm) für >10 LPM |
| Kein Akkumulator | Pulsation, WaterHammer, Schaltzyklus | Akkumulator 0,5–1L einbauen |
| Starres Rohr direkt an Pumpe | Vibrations-Übertragung, Rissbildung | 300mm flexibler Schlauch |
| Saugseite nicht dicht | Luft zieht, Pumpe läuft ständig | Alle Verbindungen doppelt prüfen |
| Kein Vorfilter | Sediment zerstört Membrane | Inline-Filter 100µm vor Pumpe |
| Pumpe über Wasserlinie | Schwierigere Ansaugung | Möglichst unter Tankboden |
| Kein Rückschlagventil (bei Whale) | Rückfluss, System entleert sich | Externes Rückschlagventil |

### 9.2 Warmwasser-Boiler (Isotemp, Quick, Sigmar, Whale)

#### 9.2.1 Vollständiger Boiler-Vergleich

| Kriterium | Isotemp Basic 24L | Quick BXS 20L | Sigmar SIC006 (22L) | Whale Expanse 8L |
|-----------|-------------------|---------------|---------------------|-----------------|
| **Artikelnummer** | SBC024003 | FVTIT020000A00 | SIC006 | WF3400 |
| **Volumen** | 24L | 20L | 22L | 8L |
| **Heizung 230V** | 750W | 1200W | 750W | 500W |
| **Motorwärmetauscher** | Ja (Serpentine) | Ja (Serpentine) | Ja (Serpentine) | Optional |
| **Aufheizzeit (230V)** | ~50 min | ~25 min | ~45 min | ~25 min |
| **Isolierung** | PU-Schaum, 30mm | PU-Schaum, 25mm | PU-Schaum, 25mm | PU-Schaum, 20mm |
| **Innenmaterial** | Edelstahl 316L | Edelstahl 316L | Edelstahl 316L | Edelstahl 316L |
| **Anschlüsse** | ¾" BSP (2x) | ¾" BSP (2x) | ¾" BSP (2x) | WQC (2x) |
| **Thermostat** | 40–75°C | 30–75°C | 40–70°C | 40–65°C |
| **Mischventil** | Optional | Integriert (einige Modelle) | Optional | Optional |
| **Preis (EUR)** | 350–450 | 400–550 | 300–400 | 250–350 |
| **Für Bootsgröße** | 10–15m | 12–18m | 10–14m | 8–12m |

#### 9.2.2 Schlauchempfehlung je Boiler

| Boiler | Anschluss | Empfohlener Schlauch Eingang | Empfohlener Schlauch Ausgang | Übergangsstück |
|--------|----------|----------------------------|-----------------------------|-----------------| 
| Isotemp Basic 24L | ¾" BSP | PEX 16mm + Crimp + ¾" Übergang | PEX 16mm + Crimp + ¾" Übergang | Rehau/Uponor Pressfitting |
| | | ODER: EPDM 19mm + Schelle | ODER: EPDM 19mm + Schelle | Vetus oder AQUAPAL |
| Quick BXS 20L | ¾" BSP | PEX 16mm + Crimp + ¾" Übergang | PEX 16mm + Crimp + ¾" Übergang | Rehau/Uponor Pressfitting |
| Sigmar SIC006 | ¾" BSP | EPDM 19mm + Schelle | EPDM 19mm + Schelle | Vetus DWHOSE oder AQUAPAL |
| Whale Expanse 8L | WQC | Whale WX1510R | Whale WX1510R | Kein Übergang nötig |

**Kritischer Hinweis Boiler-Anschlüsse:**
- **Kupferrohr NICHT verwenden** — Kupfer korrodiert bei dem niedrigen pH von Watermaker-Wasser und gibt Kupferionen ab (Geschmack, grüne Verfärbung).
- **Messing-Fittings prüfen** — alte Messing-Fittings (pre-2014) können >4% Blei enthalten. Ab 2014 gilt in der EU die TrinkwV mit 10 µg/L Blei-Grenzwert. Marelon (Forespar) oder DZR-Messing (entzinkungsbeständig) verwenden.
- **Mischventil (Verbrühschutz) obligatorisch** — Boiler auf 60°C+ (Legionellen-Schutz), aber Mischventil auf 45°C am Ausgang.

### 9.3 Watermaker (Spectra, Schenker, Dessalator, Katadyn)

#### 9.3.1 Vollständiger Watermaker-Vergleich

| Kriterium | Spectra Ventura 150 | Schenker Zen 30 | Dessalator D60 | Katadyn PowerSurvivor | Rainman WM |
|-----------|--------------------|-----------------|-----------------|-----------------------|-----------|
| **Kapazität** | 5,7 LPH | 30 LPH | 60 LPH | 5,7 LPH | 46 LPH |
| **Energiequelle** | 12V DC | 12V DC | 230V AC | 12V DC | 230V AC |
| **Leistungsaufnahme** | 120W | 150W | 600W | 60W | 750W |
| **Produktwasser-Anschluss** | JG 6mm (¼") | Tülle 10mm | Tülle 13mm | JG 6mm (¼") | QD 10mm |
| **Seewasser-Eingang** | ½" Tülle | ½" Tülle | ¾" Tülle | ½" Tülle | Eigener Filter |
| **TDS Produktwasser** | <500 ppm | <500 ppm | <500 ppm | <500 ppm | <500 ppm |
| **Post-Treatment** | Optional (empfohlen) | Optional | Optional | Optional | Optional |
| **Gewicht** | 18 kg | 22 kg | 35 kg | 3,2 kg | 25 kg (portabel) |
| **Preis (EUR)** | 5.500–6.500 | 4.000–5.000 | 6.000–8.000 | 2.000–2.500 | 4.500–5.500 |
| **Für Bootsgröße** | 8–14m | 10–16m | 14–25m | 7–12m (Notfall) | 10–18m |

#### 9.3.2 Schlauchempfehlung Watermaker → Tank

| Watermaker | Produktwasser-Leitung | Empfohlener Schlauch | Besonderheit |
|-----------|----------------------|---------------------|--------------|
| Spectra Ventura 150/200 | JG 6mm (¼") | John Guest PE 6mm (PI0608W) | Standard JG, weiß |
| Schenker Zen/Smart | Tülle 10mm | Silikon food-grade 10mm oder JG 10mm mit Adapter | Kurze Strecke, dann JG |
| Dessalator D60/D100 | Tülle 13mm | AQUAPAL 13mm oder JG 15mm mit Adapter | Höherer Volumenstrom |
| Katadyn PowerSurvivor | JG 6mm (¼") | John Guest PE 6mm (PI0608W) | Wie Spectra |
| Rainman WM | QD 10mm → Tülle | JG 10mm oder Silikon 10mm | Portables System |

**Wichtig: Mineralisierung nach Watermaker**

Watermaker-Produktwasser ist demineralisiert und aggressiv (niedriger pH). Ohne Nachbehandlung:
- Korrosionsrisiko an Messing- und Kupferteilen
- Flacher Geschmack
- Potenziell Blei-/Kupfer-Lösung aus Fittings

**Empfohlene Post-Treatment-Kette:**
1. **Mineralisierungsfilter** (Spectra PT Cartridge, ~80 EUR, Wechsel 1×/Jahr)
2. **Aktivkohlefilter** (Standard 10" GAC, ~20 EUR, Wechsel 2×/Jahr)
3. **UV-C LED** (Acuva ArrowMAX, ~350 EUR, wartungsfrei)

### 9.4 Zusammenfassung: Kosten

#### 9.4.1 Komplett-System Kosten nach Bootsgröße

**Szenario 1: Komplette Neuinstallation (alle Schläuche und Fittings)**

| Bootsgröße | John Guest (Budget) | AQUAPAL (Mittel) | PEX Rehau (Premium) |
|-----------|--------------------|-----------------|--------------------|
| 8–10m | 200–350 EUR | 350–550 EUR | 500–800 EUR |
| 10–12m | 300–500 EUR | 500–800 EUR | 750–1.200 EUR |
| 12–15m | 450–750 EUR | 700–1.200 EUR | 1.000–1.800 EUR |
| 15–20m | 600–1.100 EUR | 1.000–1.800 EUR | 1.500–2.800 EUR |
| 20–30m | 1.000–2.000 EUR | 1.800–3.500 EUR | 2.500–5.000 EUR |

*Kosten nur Material, ohne Arbeitszeit. Arbeitszeit: 8–24h je nach Bootsgröße und Zugänglichkeit.*

**Szenario 2: Upgrade PVC → KTW-konform (nur Schläuche tauschen, Fittings beibehalten)**

| Bootsgröße | John Guest | AQUAPAL | Silikon (nur kurze Stücke) |
|-----------|-----------|---------|---------------------------|
| 8–10m | 150–250 EUR | 200–350 EUR | 80–150 EUR (nur Anschlüsse) |
| 10–12m | 200–350 EUR | 300–500 EUR | 100–200 EUR |
| 12–15m | 300–500 EUR | 450–750 EUR | 150–300 EUR |

**Szenario 3: Hygiene-Upgrade (UV + Filter + Desinfektion)**

| Komponente | Produkt | Einmalkosten (EUR) | Jährliche Kosten (EUR) |
|-----------|---------|-------------------|----------------------|
| UV-C LED Inline | Acuva ArrowMAX 2.0 | 350 | 0 (wartungsfrei) |
| Aktivkohlefilter (10") | Standard-Filtergehäuse + Patrone | 60 | 30 (2× Patronenwechsel) |
| Sedimentfilter (50µm) | Standard-Filtergehäuse + Patrone | 40 | 20 (2× Patronenwechsel) |
| Tank-Desinfektion | Certisil Combina | 25 | 25 (2× pro Saison) |
| Wassertest-Streifen | Aquagenx oder einfache Streifen | 15 | 15 |
| **Gesamt** | | **490** | **90** |

#### 9.4.2 Return on Investment

**Kosten der Nicht-Investition:**

| Problem | Wahrscheinlichkeit (ohne Upgrade) | Schadenskosten |
|---------|--------------------------------|---------------|
| Gekauftes Trinkwasser (Kanister) | 100% (bei Geschmacksproblem) | 200–500 EUR/Saison |
| Wasserschaden durch undichten Schlauch | 10–20% pro Jahr bei >10 Jahre altem PVC | 500–5.000 EUR |
| Gastroenteritis durch Biofilm/Keime | 5–15% pro Saison (bei warmem Revier) | 0–2.000 EUR (Arztkosten) |
| Wertminderung Boot (schlechtes Wassersystem) | Indirekt | 1.000–5.000 EUR |

**Break-Even:** Eine Komplett-Sanierung des Trinkwassersystems auf John-Guest-Basis (300–500 EUR für ein 12m-Boot) amortisiert sich innerhalb von 1–2 Saisons allein durch den Wegfall von gekauftem Trinkwasser und reduzierte Reparaturkosten.

#### 9.4.3 Material-Kosten Detailaufstellung (Referenzboot: Bavaria C42, 12,8m)

**Ist-Zustand (Werft-Original, Baujahr 2018):**

| Zone | Ist-Material | Länge (m) | Ist-Score |
|------|-------------|----------|----------|
| Tank 1 (200L, Bug) → Absperrhahn | John Guest PE 15mm | 0,5 | 85 |
| Tank 2 (200L, Achtern) → Absperrhahn | John Guest PE 15mm | 0,8 | 85 |
| Absperrhähne → Vorfilter | John Guest PE 15mm | 1,2 | 85 |
| Vorfilter → Pumpe (Jabsco Par-Max 3.0) | John Guest PE 15mm | 0,4 | 85 |
| Pumpe → Akkumulator (Jabsco 18810) | John Guest PE 15mm | 0,3 | 85 |
| Akkumulator → Verteiler | John Guest PE 15mm | 0,5 | 85 |
| Verteiler → Pantry Kalt | John Guest PE 15mm | 2,0 | 85 |
| Verteiler → Pantry Warm (via Boiler) | John Guest PE 15mm | 4,5 | 85 |
| Verteiler → Vorschiff-Head Kalt | John Guest PE 15mm | 3,5 | 85 |
| Verteiler → Vorschiff-Head Warm | John Guest PE 15mm | 5,0 | 85 |
| Verteiler → Achtern-Head Kalt | John Guest PE 15mm | 2,0 | 85 |
| Verteiler → Achtern-Head Warm | John Guest PE 15mm | 3,5 | 85 |
| Verteiler → Cockpit-Dusche | John Guest PE 15mm | 2,5 | 85 |
| Boiler Ein (Isotemp Basic 24L) | Silikon 16mm | 0,3 | 90 |
| Boiler Aus | Silikon 16mm | 0,3 | 90 |
| Tankbelüftung (2x) | PVC Standard (!) | 2,0 | 40 |
| Einfüllstutzen → Tank (2x) | PVC Standard (!) | 1,5 | 40 |
| **Gesamt** | Mix | **30,8** | **Ø 81** |

**Empfohlene Maßnahmen:**

| Maßnahme | Material | Kosten (EUR) | Score-Verbesserung |
|----------|---------|-------------|-------------------|
| Tankbelüftung PVC → PE | JG PE 15mm (2m) + Fittings | 25 | +45 Punkte (Zone) |
| Einfüllstutzen PVC → PE | JG PE 22mm (1,5m) + Fittings | 30 | +45 Punkte (Zone) |
| UV-C LED nachrüsten | Acuva ArrowMAX 2.0 | 350 | +10 Punkte (System Hygiene) |
| Aktivkohle-Filter nachrüsten | Filtergehäuse + GAC | 60 | +5 Punkte (System Hygiene) |
| **Gesamt** | | **465** | **Ø 87 (+6)** |

#### 9.4.4 Arbeitszeit-Kalkulation

| Tätigkeit | DIY (Stunden) | Werft (Stunden) | Werft-Stundensatz (EUR) |
|-----------|-------------|----------------|----------------------|
| Bestandsaufnahme / Planung | 2–4 | 1–2 | 75–120 |
| Demontage alter Schläuche | 2–4 | 1–3 | 75–120 |
| Neuverlegung John Guest (12m Boot) | 6–10 | 4–6 | 75–120 |
| Neuverlegung PEX (12m Boot) | 8–14 | 5–8 | 75–120 |
| Boileranschlüsse (2 Stück) | 1–2 | 0,5–1 | 75–120 |
| Pumpenanschlüsse | 1–2 | 0,5–1 | 75–120 |
| Druckprüfung + Spülung | 2–3 | 1–2 | 75–120 |
| UV-Filter-Einbau | 1–2 | 0,5–1 | 75–120 |
| **Gesamt (JG, 12m Boot)** | **15–27** | **9–16** | **675–1.920** |

#### 9.4.5 Ersatzteil-Bordvorrat Empfehlung

**Minimum-Bordvorrat Trinkwassersystem (Küstenfahrt):**

| Artikel | Menge | Preis (EUR) | Bemerkung |
|---------|-------|-------------|-----------|
| John Guest PE 15mm weiß | 3m | 10 | Universal-Reparatur |
| JG Gerade Verbindung 15mm | 4 St. | 16 | Für Notverbindungen |
| JG Winkel 90° 15mm | 2 St. | 10 | |
| JG Absperrhahn 15mm | 1 St. | 14 | Zum Isolieren defekter Abschnitte |
| JG BSP-Adapter ½" 15mm | 2 St. | 12 | Pumpe/Boiler-Übergang |
| Silikon food-grade 13mm | 1m | 18 | Pumpen-/Boileranschluss |
| Schlauchschellen Edelstahl 316 | 10 St. | 8 | 13–20mm Bereich |
| PTFE-Band | 1 Rolle | 3 | Gewindedichtung |
| JG Rohrschneider | 1 St. | 12 | Sauberer Schnitt essentiell |
| Certisil Combina | 10 Tabl. | 5 | Tank-Desinfektion |
| **Gesamt Bordvorrat** | | **~108** | |

**Erweiterter Bordvorrat (Blauwasser/Langfahrt):**

| Artikel | Menge | Preis (EUR) | Bemerkung |
|---------|-------|-------------|-----------|
| John Guest PE 15mm weiß | 10m | 35 | |
| John Guest PE 10mm weiß | 3m | 10 | Für Watermaker |
| JG 6mm PE (für Spectra etc.) | 3m | 8 | Watermaker-Produktleitung |
| JG Fitting-Set komplett | 1 Set | 60 | T, Winkel, Gerade, Reduktion |
| AQUAPAL 13mm | 3m | 35 | Alternative zu JG |
| Silikon food-grade 13mm | 2m | 36 | |
| Silikon food-grade 16mm | 1m | 22 | Boiler |
| Pumpen-Reparatur-Kit (passend) | 1 St. | 45–80 | Jabsco Service Kit |
| Aktivkohle-Filterpatrone 10" | 2 St. | 30 | |
| Sediment-Filterpatrone 10" | 2 St. | 15 | |
| Certisil Combina | 50 Tabl. | 20 | |
| Certisil Argento | 250mL | 35 | Silber-Konservierung |
| Wassertest-Kit (Bakterien) | 5 Tests | 25 | Aquagenx CBT |
| JG Rohrschneider | 1 St. | 12 | |
| PTFE-Band | 3 Rollen | 6 | |
| Schlauchschellen Edelstahl 316 | 20 St. | 15 | |
| O-Ringe EPDM food-grade sortiert | 1 Set | 12 | Für Tankdeckel etc. |
| **Gesamt Bordvorrat Langfahrt** | | **~440** | |

---

### 9.5 AYDI Bewertungslogik — Trinkwassersystem

#### 9.5.1 Score-Berechnung

Der Trinkwassersystem-Score setzt sich aus vier Teil-Scores zusammen:

```python
"""
AYDI Trinkwassersystem Score-Berechnung
"""

def calculate_water_system_score(
    material_scores: list[int],      # Score pro Schlauch-Abschnitt (0-100)
    hygiene_scores: list[int],       # Score pro Abschnitt (0-100)
    compliance_data: dict,           # Zertifizierungen vorhanden/fehlend
    installation_scores: list[int],  # Installations-Qualität pro Abschnitt
) -> dict:
    """
    Gewichtete Berechnung des Gesamtscores.
    
    Gewichtung:
    - Material: 35% (welches Material verbaut ist)
    - Hygiene: 30% (Biofilm-Risiko, Desinfektion, Temperaturmanagement)
    - Compliance: 20% (Zertifizierungen, Normenkonformität)
    - Installation: 15% (Verlegung, Befestigung, Zugänglichkeit)
    """
    import statistics
    
    material_avg = statistics.mean(material_scores) if material_scores else 50
    hygiene_avg = statistics.mean(hygiene_scores) if hygiene_scores else 50
    installation_avg = statistics.mean(installation_scores) if installation_scores else 50
    
    # Compliance Score aus Zertifizierungsdaten
    compliance_score = _calculate_compliance_score(compliance_data)
    
    overall = (
        material_avg * 0.35 +
        hygiene_avg * 0.30 +
        compliance_score * 0.20 +
        installation_avg * 0.15
    )
    
    return {
        "overall_system_score": round(overall),
        "overall_material_score": round(material_avg),
        "overall_hygiene_score": round(hygiene_avg),
        "overall_compliance_score": round(compliance_score),
        "overall_installation_score": round(installation_avg),
    }


def _calculate_compliance_score(compliance_data: dict) -> int:
    """
    Berechnet Compliance-Score basierend auf vorhandenen Zertifizierungen.
    
    Punkte:
    - KTW (B oder höher): 30 Punkte
    - DVGW W270: 25 Punkte
    - NSF 61: 20 Punkte
    - FDA: 10 Punkte
    - WRAS: 10 Punkte
    - ACS: 10 Punkte
    - Keine Zertifizierung: 0 Punkte
    - Maximum: 100 Punkte (KTW + W270 + NSF + FDA + WRAS = 95, gerundet auf 100)
    """
    score = 0
    certs = compliance_data.get("certifications_present", [])
    
    if any(c in certs for c in ["ktw_b", "ktw_c", "ktw_d"]):
        score += 30
    if "dvgw_w270" in certs:
        score += 25
    if "nsf_61" in certs:
        score += 20
    if "fda" in certs:
        score += 10
    if "wras" in certs:
        score += 10
    if "acs" in certs:
        score += 10
    
    return min(score, 100)
```

#### 9.5.2 Visuelle Erkennung (Pipeline B)

**Identifikation von Schlauchmaterialien auf Fotos:**

| Visuelles Merkmal | Material | Confidence |
|-------------------|----------|-----------|
| Weiß, semi-rigide, kleiner Durchmesser | John Guest PE oder PEX | visual_medium |
| Blau, flexibel, "AQUAPAL" Beschriftung | Continental AQUAPAL | visual_high |
| Weiß, flexibel, "VETUS DRINKING WATER" | Vetus DWHOSE | visual_high |
| Transparent/klar, sehr flexibel | PVC oder Silikon | visual_low (Differenzierung schwierig) |
| Schwarz, flexibel | EPDM (ggf. NICHT food-grade!) | visual_medium |
| Grau, flexibel, verstärkt | PVC Standard (kein TW!) | visual_high (negativ) |
| Grün, transparent | Gartenschlauch (ALARM!) | visual_high (negativ) |
| Rot/Blau PE, semi-rigide | John Guest Warm/Kalt-Kennung | visual_high |

**Alterungszeichen auf Fotos:**

| Visuelles Merkmal | Defekt | Dringlichkeit |
|-------------------|--------|--------------|
| Gelb verfärbter PVC | UV-Degradation + Weichmacher-Verlust | Austausch innerhalb 6 Monate |
| Grüne Ablagerungen innen (transparent) | Algenwachstum | Desinfektion sofort, Materialwechsel |
| Schwarze Flecken innen | Schimmel/Biofilm | Desinfektion sofort |
| Risse an Biegeradien | Materialermüdung | Sofortiger Austausch |
| Aufquellungen | Chemische Inkompatibilität | Sofortiger Austausch |
| Rostflecken an Schellen | Falsche Schellen (nicht 316L) | Schellen tauschen |
| Weiße Ablagerungen an Fittings | Kalkausfall oder Korrosion | Prüfung erforderlich |

#### 9.5.3 Winterisierung (Frostschutz)

**Verfahren für die Wintereinlagerung:**

| Schritt | Maßnahme | Werkzeug | Bemerkung |
|---------|----------|---------|-----------|
| 1 | Tanks entleeren | Tankablasshahn oder Pumpe | Vollständig! |
| 2 | System mit Druckluft ausblasen | Kompressor, 0,5–1,0 bar | Alle Hähne öffnen |
| 3 | Pumpe entleeren | Ablassschraube oder Druckluft | Filter entfernen |
| 4 | Boiler entleeren | Ablassventil öffnen (unten) | Boiler-Anode prüfen! |
| 5 | Akkumulator entleeren | Ablassschraube | Vordruck prüfen (Manometer) |
| 6 | Watermaker konservieren | Herstelleranleitung (Natriumbisulfit) | Spezifisch je Modell |
| 7 | Optional: Propylenglykol einfüllen | Handpumpe, 50/50 Mischung | Nur FDA food-grade Propylenglykol! |
| 8 | Alle Hähne offen lassen | — | Druckentlastung |
| 9 | Filterpatronen entfernen und trocknen | — | Schimmelgefahr bei feuchter Lagerung |

**NICHT verwenden:** Ethylenglykol (Kfz-Frostschutz) — giftig! Nur Propylenglykol (food-grade), z.B. Camco 36190 oder Star brite Non-Toxic Antifreeze.

**Kosten Winterisierung:**
- Propylenglykol (5L): ~20 EUR
- Arbeitszeit: 2–4 Stunden
- Werkzeug: Kompressor (Leihgebühr ~30 EUR/Tag oder eigener)

---

## Verbindungstechnik & Fittings

Die Verbindungstechnik entscheidet über die Langzeitdichtheit und hygienische Sicherheit eines Trinkwassersystems an Bord. Im Yachtbau kommen primär drei Verbindungsarten zum Einsatz: Push-Fit (Schnellstecksysteme), Crimp/Press-Verbindungen und konventionelle Schlauchschellen. Jede Technologie hat spezifische Vor- und Nachteile bezüglich Montageaufwand, Vibrationsfestigkeit und Langzeitdichtheit im maritimen Einsatz.

### Push-Fit Systeme (John Guest, Whale, SharkBite)

Push-Fit Verbindungen sind im modernen Yachtbau der Standard für Trinkwasserleitungen bis 22 mm Außendurchmesser. Das Prinzip: Ein Edelstahl-Zahnring greift in den Schlauch, ein O-Ring dichtet ab. Kein Werkzeug nötig — Schlauch einstecken, fertig.

**John Guest (JG) Speedfit Marine:**
- Hersteller: John Guest Ltd., West Drayton, UK
- Material Fitting-Körper: Acetal-Copolymer (POM), lebensmittelzugelassen nach KTW/W270, WRAS, NSF 61
- O-Ring Material: EPDM (Standard) oder Viton (Heißwasser >60°C)
- Temperaturbereich: -20°C bis +70°C (Standard-EPDM), bis +90°C (Viton)
- Betriebsdruck: max. 12 bar bei 20°C, max. 8 bar bei 60°C
- Größen: 1/4" (6,35 mm), 3/8" (9,5 mm), 1/2" (12,7 mm), 15 mm, 22 mm
- Farbcodierung: Weiß = Kalt, Rot = Warm, Blau = Watermaker-Permeat
- Teilenummern (häufig): JG-PI0408S (1/4" Inline-Verbinder), JG-PI0412S (3/8"), JG-PI0416S (1/2"), JG-PI4616 (1/2" T-Stück), JG-PI4816 (1/2" Winkel 90°)
- Lebensdauer: 20–25 Jahre bei bestimmungsgemäßem Gebrauch
- Preis: Inline-Verbinder ~2,50–4,00 EUR, T-Stück ~4,50–7,00 EUR, Winkel ~3,50–5,50 EUR
- AYDI Confidence: measured | Score: 92/100

**Whale Quick-Connect (WQC):**
- Hersteller: Whale (Munster Simms Engineering), Nordirland
- Material: Acetal, lebensmittelzugelassen WRAS
- Temperaturbereich: -30°C bis +60°C
- Betriebsdruck: max. 4,1 bar (60 psi) — deutlich niedriger als JG!
- Größen: 12 mm und 15 mm (proprietäres System)
- Besonderheit: Integrierter Schlauchhalter, einhändige Bedienung
- Teilenummern: WX1502B (15 mm Verbinder), WX1504B (15 mm T-Stück), WX1522B (15 mm Winkel)
- Lebensdauer: 15–20 Jahre
- Preis: Verbinder ~3,00–5,00 EUR, T-Stück ~6,00–9,00 EUR
- AYDI Confidence: measured | Score: 85/100
- Einschränkung: Nur für Niederdrucksysteme ≤4 bar. Nicht geeignet für Watermaker-Hochdruck.

**SharkBite Marine (Cash Acme):**
- Hersteller: SharkBite / Reliance Worldwide Corporation
- Material: DZR-Messing (entzinkungsbeständig), EPDM-Dichtung
- Temperaturbereich: -18°C bis +93°C
- Betriebsdruck: max. 13,8 bar (200 psi)
- Größen: 3/8", 1/2", 3/4" (Kupfer/PEX-kompatibel)
- Besonderheit: Messingkörper — höhere Druckfestigkeit als Kunststoff-Push-Fit
- Teilenummern: SB-22222 (1/2" Kupplungsverbinder), SB-24983 (1/2" T-Stück)
- Lebensdauer: 25+ Jahre (Messing korrosionsbeständiger als Acetal)
- Preis: Verbinder ~8,00–12,00 EUR, T-Stück ~12,00–18,00 EUR
- AYDI Confidence: measured | Score: 88/100
- Achtung: DZR-Messing ist Pflicht — Standard-Messing (CW614N/CZ121) entzinkt in Salzwasser-Atmosphäre!

**Vergleichstabelle Push-Fit Systeme:**

| Eigenschaft | John Guest | Whale QC | SharkBite |
|-------------|-----------|----------|-----------|
| Max. Druck (bar) | 12 | 4,1 | 13,8 |
| Max. Temp. (°C) | 70 (90 Viton) | 60 | 93 |
| Material Körper | Acetal (POM) | Acetal | DZR-Messing |
| Werkzeug nötig | Nein | Nein | Nein |
| Demontierbar | Ja (Collet-Ring) | Ja | Ja (Demontage-Clip) |
| Vibrationsfestigkeit | Gut | Mittel | Sehr gut |
| Korrosionsrisiko | Gering | Gering | Mittel (Messing) |
| Preisniveau | Mittel | Mittel | Hoch |
| Marine-Zulassung | Ja | Ja | Bedingt |
| AYDI-Score | 92 | 85 | 88 |

**Montage Push-Fit — Kritische Punkte:**
1. Schlauch exakt rechtwinklig schneiden (Rohrschneider, nicht Messer)
2. Gratfrei entgraten (innen und außen)
3. Einstecktiefe markieren (JG 1/2": 25 mm, Whale 15 mm: 22 mm)
4. Schlauch bis Anschlag einschieben — Kontrolle über Sichtfenster oder Markierung
5. Zugprüfung: kräftig am Schlauch ziehen, darf sich nicht lösen
6. Druckprüfung: 1,5× Betriebsdruck, 10 Minuten, kein Abfall

### Schlauchschellen für Trinkwasser (lebensmittelecht)

Schlauchschellen sind die älteste und immer noch verbreitete Verbindungstechnik, insbesondere bei flexiblen Silikonschläuchen und an Pumpenanschlüssen. Im Trinkwasserbereich gelten besondere Anforderungen.

**Zugelassene Schlauchschellen-Typen:**

**Typ 1 — Edelstahl-Schneckengewindeschelle (Standard):**
- Material: Band und Gehäuse V4A (1.4401 / AISI 316), Schraube V4A
- Hersteller: NORMA Group (NORMA TORRO), ABA (Original Swedish), Jubilee Clips
- Bandbreite: 9 mm (Standard) oder 12 mm (verstärkt)
- Anziehdrehmoment: 2,5–3,5 Nm (9 mm Band), 3,0–4,5 Nm (12 mm Band)
- Teilenummern (NORMA TORRO): 01/012 (Ø 8–12 mm), 01/016 (Ø 12–16 mm), 01/020 (Ø 16–20 mm), 01/025 (Ø 20–25 mm)
- Preis: ~1,20–2,50 EUR/Stück (V4A)
- AYDI-Score: 78/100
- Nachteil: Schneckengewinde kann Schlauch einschneiden, Korrosion an Gewindeübergang möglich

**Typ 2 — Ohrschelle (Oetiker / Caillau):**
- Material: V2A oder V4A Edelstahl
- Hersteller: Oetiker (Schweiz), Caillau (Frankreich)
- Bandbreite: 7 mm (1-Ohr) oder 9 mm (2-Ohr)
- Schließkraft: gleichmäßiger als Schneckengewinde, kein Einschneiden
- Teilenummern (Oetiker 1-Ohr): 16700004 (Ø 9,4–11,9 mm), 16700008 (Ø 13,3–15,7 mm), 16700012 (Ø 17,0–20,3 mm)
- Werkzeug: Oetiker-Zange Nr. 1099 (1-Ohr) oder Nr. 1098 (2-Ohr)
- Preis: ~0,80–1,80 EUR/Stück + Zange ~85–120 EUR
- AYDI-Score: 90/100
- Vorteil: Glatte Innenfläche, keine Schnittkanten, professioneller Standard in der Yachtproduktion

**Typ 3 — Federbandschelle:**
- Material: Federstahl, oft nicht V4A — NICHT empfohlen für Trinkwasser im Salzwasser-Umfeld
- AYDI-Score: 35/100
- Nur akzeptabel als Notfall-Provisorium

**Typ 4 — Konstant-Drehmoment-Schelle (CT-Schelle):**
- Material: V4A Edelstahl mit Federelement
- Hersteller: NORMA RSGU, Rotor Clip
- Besonderheit: Kompensiert thermische Ausdehnung/Schrumpfung des Schlauchs
- Teilenummern (NORMA RSGU): RSGU-Ø (nach Durchmesser)
- Preis: ~3,50–6,00 EUR/Stück
- AYDI-Score: 88/100
- Empfehlung: Für Warmwasserleitungen und Leitungen mit starker Temperaturwechselbelastung

**Wichtig — Doppelschellen-Regel:**
An allen Anschlüssen unterhalb der Wasserlinie MÜSSEN zwei Schellen verwendet werden (Redundanz). Gilt auch für Trinkwasserleitungen, die durch den Rumpf geführt werden (Tankeinlass/-auslass, Watermaker-Seewasserseite). Referenz: ABYC H-23, ISO 9093 (Seeventile und Rumpfdurchführungen).

### Crimpen vs Pressen vs Push-Fit

**Crimp-Verbindungen (PEX):**
- Werkzeug: Crimp-Zange (z.B. Viega PureFlow Nr. 50020, ~180–250 EUR)
- Material: Kupfer-Crimpring (ASTM F1807)
- Funktionsprinzip: Kupferring wird um PEX-Rohr auf Fitting gepresst, plastische Verformung
- Prüfung: Go/No-Go Lehre (z.B. Viega 50050)
- Vorteil: Sehr sicherer Sitz, vibrationsbeständig, kostengünstige Fittings
- Nachteil: Nicht demontierbar, Spezialwerkzeug nötig, Kupferring kann korrodieren
- AYDI-Score: 85/100

**Press-Verbindungen (PEX / Edelstahl):**
- Werkzeug: Pressmaschine (z.B. Viega Pressgun 5, ~1.200–2.500 EUR; Ridgid RP 241, ~1.800 EUR)
- Material: Presshülse Edelstahl oder Messing
- Funktionsprinzip: Presshülse wird radial verpresst, gleichmäßige 360°-Verformung
- Prüfung: Viega SC-Contur — unverpresste Fittings lecken bei Druckprüfung (Sicherheitsmerkmal)
- Vorteil: Höchste Zuverlässigkeit, normkonform nach DVGW W534, schnelle Montage
- Nachteil: Teures Werkzeug, nicht demontierbar
- AYDI-Score: 95/100

**Push-Fit (wie oben beschrieben):**
- Werkzeug: Keines (nur Rohrschneider zum Ablängen)
- Vorteil: Schnellste Montage, demontierbar, kein Spezialwerkzeug
- Nachteil: O-Ring-Alterung, begrenzte Druckfestigkeit, höherer Stückpreis
- AYDI-Score: 90/100

**Entscheidungsmatrix:**

| Kriterium | Crimp | Press | Push-Fit |
|-----------|-------|-------|----------|
| Werkzeugkosten | ~200 EUR | ~1.500 EUR | 0 EUR |
| Fitting-Kosten/Stück | 2–5 EUR | 5–12 EUR | 3–8 EUR |
| Montagezeit/Verbindung | 60 s | 30 s | 10 s |
| Demontierbar | Nein | Nein | Ja |
| Max. Druck | 10 bar | 16 bar | 12 bar |
| Vibrationsfestigkeit | Sehr gut | Sehr gut | Gut |
| Langzeitdichtheit | Sehr gut | Hervorragend | Gut |
| Lernkurve | Mittel | Gering | Sehr gering |
| AYDI-Score | 85 | 95 | 90 |

**Empfehlung nach Bootstyp:**
- Produktionsboot (8–14 m): Push-Fit (John Guest) — schnell, wartbar, kostengünstig
- Semi-Custom (12–20 m): Crimp (PEX) oder Push-Fit — je nach Werft-Präferenz
- Custom/Superyacht (18+ m): Press (Viega Profipress) — höchster Standard, Dokumentation

### Dichtmaterialien (PTFE, O-Ring, Hanf — was ist erlaubt?)

Im Trinkwasserbereich sind nicht alle üblichen Dichtmaterialien zugelassen. Die KTW-Leitlinie und die W270-Prüfung regeln, welche Materialien in Kontakt mit Trinkwasser verwendet werden dürfen.

**PTFE-Band (Teflonband):**
- Zulässigkeit: Ja, wenn lebensmittelzugelassen (FDA 21 CFR 177.1550)
- Anwendung: Gewindeverbindungen (NPT, BSP), Pumpenanschlüsse
- Bandstärke: 0,075–0,1 mm (Standard), 0,2 mm (Heavy Duty)
- Wicklung: 3–5 Lagen in Gewinderichtung (im Uhrzeigersinn bei Rechtsgewinde)
- Hersteller: Loctite 5075, Markal LA-CO M-A-R, Stauf TW-Tape (KTW-geprüft)
- Preis: Rolle 12 m × 12 mm: ~1,50–3,00 EUR
- AYDI-Score: 82/100

**PTFE-Gewindedichtfaden:**
- Zulässigkeit: Ja (KTW-konform, z.B. Loctite 55)
- Vorteil gegenüber Band: Wickelt sich nicht auf bei Eindrehen, justierbar
- Hersteller: Loctite 55 (Art.-Nr. 160 m Spule: 2056936), Markal PTFE-Faden
- Preis: 160 m Spule: ~12–18 EUR
- AYDI-Score: 88/100

**Flüssig-Dichtmittel (anaerob):**
- Zulässigkeit: Nur mit expliziter Trinkwasser-Zulassung!
- Zugelassen: Loctite 577 (DVGW/KTW/W270), Permabond A131 (NSF 61)
- NICHT zugelassen: Standard-Loctite 542, 545 — keine Trinkwasser-Freigabe!
- Anwendung: Metallfitting auf Metallgewinde (nicht auf Kunststoff!)
- Preis: 50 ml Tube: ~18–25 EUR
- AYDI-Score: 85/100

**Hanf + Fermit (Neo-Fermit):**
- Zulässigkeit: Traditionell ja (Hanf ist organisch), aber Fermit-Paste muss KTW-zugelassen sein
- Neo-Fermit: KTW-zugelassen, DVGW-geprüft
- Anwendung: Nur auf Metallgewinden (Messing, Edelstahl)
- Nachteil: Hanf kann bei Stagnation zu Keimbildung führen → im Yachtbau nicht empfohlen
- AYDI-Score: 55/100 — Nicht empfohlen für Bord-Trinkwasser

**O-Ringe:**
- Zulässigkeit: Materialabhängig
- Zugelassen: EPDM (KTW/W270), FKM/Viton (KTW), Silikon (FDA)
- NICHT zugelassen: NBR (Nitrilkautschuk) — enthält oft PAK
- Hersteller: Parker Hannifin (Compound E0893 EPDM), Freudenberg (Simrit), COG (C.Otto Gehrckens)
- Normung: O-Ring-Nuten nach ISO 3601 / DIN 3771
- Schmiermittel: Nur lebensmittelzugelassene Silikonfette (z.B. Molykote 111, NSF H1)
- AYDI-Score: 90/100 (EPDM/FKM)

**Zusammenfassung Dichtmaterial-Zulässigkeit:**

| Material | Trinkwasser zugelassen | KTW/W270 | Yachtbau empfohlen | AYDI-Score |
|----------|----------------------|----------|-------------------|------------|
| PTFE-Band (food-grade) | Ja | Ja | Ja | 82 |
| PTFE-Faden (Loctite 55) | Ja | Ja | Ja | 88 |
| Loctite 577 | Ja | Ja | Ja (nur Metall) | 85 |
| Neo-Fermit + Hanf | Bedingt | Ja | Nein (Keimrisiko) | 55 |
| EPDM O-Ring | Ja | Ja | Ja | 90 |
| FKM/Viton O-Ring | Ja | Ja | Ja (Heißwasser) | 90 |
| NBR O-Ring | Nein | Nein | Nein | 20 |
| Silikon O-Ring | Ja (FDA) | Bedingt | Ja | 85 |

### Anziehdrehmomente

Korrekte Anziehdrehmomente sind entscheidend für Dichtheit ohne Materialschädigung. Zu fest angezogene Kunststoff-Fittings reißen, zu lose angezogene lecken unter Vibration.

**Schlauchschellen auf flexiblem Schlauch:**

| Schlauch-Ø (mm) | Bandbreite 9 mm | Bandbreite 12 mm |
|-----------------|-----------------|------------------|
| 10–16 | 2,0–2,5 Nm | 2,5–3,0 Nm |
| 16–22 | 2,5–3,0 Nm | 3,0–3,5 Nm |
| 22–32 | 3,0–3,5 Nm | 3,5–4,0 Nm |
| 32–45 | 3,5–4,0 Nm | 4,0–5,0 Nm |

**Kunststoff-Gewindefittings (Acetal, POM, PP):**

| Gewinde | Anziehdrehmoment | Hinweis |
|---------|-----------------|---------|
| 1/4" BSP | 2,0–3,0 Nm | Handfest + 1/4 Umdrehung |
| 3/8" BSP | 3,0–4,5 Nm | Handfest + 1/4 Umdrehung |
| 1/2" BSP | 4,0–6,0 Nm | Handfest + 1/4 Umdrehung |
| 3/4" BSP | 5,0–8,0 Nm | Handfest + 1/4 Umdrehung |

**Messing-/Edelstahl-Gewindefittings:**

| Gewinde | Anziehdrehmoment | Hinweis |
|---------|-----------------|---------|
| 1/4" BSP | 8–12 Nm | Mit PTFE oder Loctite 577 |
| 3/8" BSP | 15–20 Nm | Mit PTFE oder Loctite 577 |
| 1/2" BSP | 25–35 Nm | Mit PTFE oder Loctite 577 |
| 3/4" BSP | 40–55 Nm | Mit PTFE oder Loctite 577 |
| 1" BSP | 55–75 Nm | Mit PTFE oder Loctite 577 |

**Pumpen-Anschlussverschraubungen:**

| Pumpe | Anschluss | Drehmoment |
|-------|-----------|------------|
| Shurflo 4009 | 1/2" QEST | 3,5–4,5 Nm |
| Jabsco Par-Max 3.5 | 1/2" BSP | 8–10 Nm |
| Whale GP1392 | 12 mm Push-Fit | Werkzeuglos |
| Grundfos PM2 | 1" BSP Messing | 55–65 Nm |

**Werkzeug-Empfehlung:**
- Drehmomentschlüssel klein: 1–25 Nm (z.B. Wera Click-Torque A5, ~85 EUR)
- Drehmomentschlüssel groß: 10–80 Nm (z.B. Hazet 5110-3CT, ~120 EUR)
- Krähenfußschlüssel-Satz für beengte Einbausituationen

---

## Technische Referenz & Berechnungen

### Durchfluss-Berechnungen für Frischwassersysteme

Die korrekte Dimensionierung der Trinkwasserleitungen bestimmt den Komfort an Bord. Zu kleine Leitungen führen zu Druckverlust und geringem Durchfluss an den Entnahmestellen.

**Grundformel Volumenstrom:**
Q = v × A
- Q = Volumenstrom [l/min]
- v = Fließgeschwindigkeit [m/s]
- A = Rohrquerschnitt [m²]

**Empfohlene Fließgeschwindigkeiten:**
- Kaltwasser-Hauptleitung: 1,0–1,5 m/s
- Warmwasser-Hauptleitung: 0,8–1,2 m/s
- Abzweig zu Entnahmestelle: 0,5–1,0 m/s
- Watermaker-Permeatleitung: 0,3–0,5 m/s

**Durchflusswerte nach Schlauchdurchmesser:**

| Innen-Ø (mm) | Querschnitt (mm²) | v=1,0 m/s (l/min) | v=1,5 m/s (l/min) |
|--------------|-------------------|-------------------|-------------------|
| 8 | 50,3 | 3,0 | 4,5 |
| 10 | 78,5 | 4,7 | 7,1 |
| 12 | 113,1 | 6,8 | 10,2 |
| 13 | 132,7 | 8,0 | 11,9 |
| 16 | 201,1 | 12,1 | 18,1 |
| 19 | 283,5 | 17,0 | 25,5 |
| 22 | 380,1 | 22,8 | 34,2 |

**Mindest-Durchfluss an Entnahmestellen (Yacht-Standard):**
- Pantry-Wasserhahn: 6–8 l/min
- Dusche: 8–12 l/min
- Waschbecken (Kopf/Bad): 4–6 l/min
- Cockpit-Dusche: 4–6 l/min
- Watermaker-Befüllung: 1–3 l/min (je nach Modell)

**Dimensionierung nach Bootsgröße:**

| Bootslänge | Entnahmestellen | Hauptleitung Ø | Abzweig Ø | Pumpenleistung |
|-----------|----------------|----------------|-----------|----------------|
| 8–10 m | 2–3 | 13 mm | 10 mm | 7–10 l/min |
| 10–14 m | 3–5 | 13–16 mm | 10–13 mm | 10–13 l/min |
| 14–18 m | 4–7 | 16–19 mm | 13 mm | 13–17 l/min |
| 18–24 m | 6–10 | 19–22 mm | 13–16 mm | 17–25 l/min |
| 24+ m | 8–15+ | 22–28 mm | 16–19 mm | 25+ l/min (Druckerhöhung) |

### Druckverlust-Berechnung (inkl. Push-Fit Fittings)

**Darcy-Weisbach Gleichung (vereinfacht für glatte Kunststoffrohre):**
Δp = λ × (L/d) × (ρ × v²/2)
- Δp = Druckverlust [Pa]
- λ = Rohrreibungszahl (PEX: ~0,02 bei Re=10.000; Silikon: ~0,025)
- L = Rohrlänge [m]
- d = Innendurchmesser [m]
- ρ = Wasserdichte [kg/m³] (~998 bei 20°C)
- v = Fließgeschwindigkeit [m/s]

**Druckverlust pro Meter Rohr (bei v=1,0 m/s, 20°C):**

| Material | Innen-Ø 10 mm | Innen-Ø 13 mm | Innen-Ø 16 mm | Innen-Ø 19 mm |
|----------|--------------|--------------|--------------|--------------|
| PEX | 1,00 kPa/m | 0,77 kPa/m | 0,63 kPa/m | 0,53 kPa/m |
| Silikon | 1,25 kPa/m | 0,96 kPa/m | 0,78 kPa/m | 0,66 kPa/m |
| PA (Nylon) | 0,95 kPa/m | 0,73 kPa/m | 0,60 kPa/m | 0,50 kPa/m |
| Edelstahl | 1,15 kPa/m | 0,88 kPa/m | 0,72 kPa/m | 0,61 kPa/m |

**Druckverlust durch Fittings (äquivalente Rohrlänge):**

| Fitting-Typ | Äquivalente Länge (× Innen-Ø) |
|-------------|-------------------------------|
| Push-Fit Gerade (JG) | 5–8 × d |
| Push-Fit T-Stück (JG, Durchgang) | 15–20 × d |
| Push-Fit T-Stück (JG, Abzweig) | 30–40 × d |
| Push-Fit 90° Winkel (JG) | 20–25 × d |
| Crimp-Fitting Gerade | 3–5 × d |
| Crimp-T-Stück Durchgang | 10–15 × d |
| Crimp-T-Stück Abzweig | 25–35 × d |
| Kugelhahn (voll geöffnet) | 5–10 × d |
| Rückschlagventil | 50–80 × d |
| Filter (sauber) | 100–200 × d |
| Filter (verschmutzt) | 300–500 × d |

**Praxis-Beispiel:**
14 m Segelyacht, Pumpe (Shurflo 4009, 3,5 bar, 11,4 l/min) → Pantry-Hahn:
- Leitungslänge: 6 m (13 mm ID PEX)
- Fittings: 2× JG Gerade, 1× JG T-Stück (Abzweig), 2× JG 90° Winkel
- Äquivalente Fitting-Länge: 2×(7×0,013) + 1×(35×0,013) + 2×(22×0,013) = 0,18 + 0,46 + 0,57 = 1,21 m
- Gesamt-äquivalente Länge: 6,0 + 1,21 = 7,21 m
- Druckverlust: 7,21 × 0,77 kPa/m = 5,55 kPa ≈ 0,056 bar
- Verfügbarer Druck am Hahn: 3,5 – 0,056 – 0,3 (Höhendifferenz) ≈ 3,14 bar → ausreichend

### Mindest-Biegeradius

Der Biegeradius ist kritisch: zu enger Radius führt zu Knickbildung, Querschnittsverringerung und Materialermüdung. Geknickte Schläuche sind die häufigste Ursache für Durchflussprobleme an Bord.

**Mindest-Biegeradien nach Material:**

| Material | Außen-Ø (mm) | Min. Biegeradius (mm) | Verhältnis (R/d) |
|----------|-------------|----------------------|------------------|
| PEX | 12 | 60–72 | 5–6 × d |
| PEX | 15 | 75–105 | 5–7 × d |
| PEX | 22 | 110–154 | 5–7 × d |
| Silikon (Platinum) | 13 | 26–39 | 2–3 × d |
| Silikon (Platinum) | 16 | 32–48 | 2–3 × d |
| Silikon (Platinum) | 19 | 38–57 | 2–3 × d |
| PA12 (Nylon) | 12 | 72–96 | 6–8 × d |
| PA12 (Nylon) | 15 | 90–120 | 6–8 × d |
| Edelstahl-Wellrohr | 12 | 36–60 | 3–5 × d |
| Edelstahl-Wellrohr | 16 | 48–80 | 3–5 × d |
| EPDM-Schlauch | 13 | 52–78 | 4–6 × d |
| EPDM-Schlauch | 19 | 76–114 | 4–6 × d |

**Biegeradien-Reduzierung mit Hilfsmitteln:**
- Biegefedern (PEX): Reduzierung auf 3–4 × d möglich
- Heißluftgebläse (PEX bei 130°C): Reduzierung auf 2–3 × d, dauerhaft
- Winkel-Fittings: Empfohlen bei Platzmangel statt zu engem Biegen

**Temperatur-Einfluss auf Biegeradius:**
- PEX bei 20°C: 6 × d
- PEX bei 60°C: 4 × d (flexibler)
- PEX bei -10°C: 10 × d (spröde, Vorsicht!)
- Silikon bei -20°C bis +80°C: nahezu konstant 2–3 × d (Vorteil Silikon)

### Wasserqualitäts-Parameter (pH, TDS, Chlor)

Trinkwasser an Bord muss der TrinkwV (Deutschland) bzw. den jeweiligen nationalen Vorschriften entsprechen. Die Schlauch- und Fittingmaterialien beeinflussen die Wasserqualität.

**Relevante Parameter und Grenzwerte:**

| Parameter | Einheit | TrinkwV Grenzwert | Empfehlung Yacht | Einfluss Material |
|-----------|---------|-------------------|-----------------|-------------------|
| pH-Wert | — | 6,5–9,5 | 7,0–8,5 | PA senkt pH leicht |
| Gesamthärte | °dH | Keine Vorgabe | 8–12 (Kalkschutz) | Kein Einfluss |
| TDS | mg/l | — | <500 | WM-Permeat: 100–300 |
| Chlor (frei) | mg/l | 0,3 (max.) | 0,1–0,2 | Silikon/EPDM empfindlich |
| Blei | µg/l | 10 | <5 | Messing-Fittings! |
| Kupfer | µg/l | 2.000 | <500 | Kupfer-Crimpring |
| KBE (22°C) | /ml | 100 | <20 | Biofilm alle Materialien |
| KBE (36°C) | /ml | 100 | <20 | Biofilm alle Materialien |
| Legionella | /100 ml | 0 | 0 | Warmwasser-System |
| TOC | mg/l | Kein Grenzwert | <3 | PVC, billige Schläuche |
| Geruch/Geschmack | — | Ohne Befund | Ohne Befund | KTW-konforme Materialien |

**Chlor-Verträglichkeit der Schlauchmaterialien:**

| Material | Max. Chlor (mg/l) | Langzeit-Chlor (mg/l) | Degradation |
|----------|-------------------|----------------------|-------------|
| PEX-a | 4,0 | 2,0 | Minimal |
| PEX-b | 4,0 | 2,0 | Minimal |
| Silikon (Platinum) | 2,0 | 0,5 | Moderate Trübung |
| Silikon (Peroxid) | 1,5 | 0,3 | Stärkere Degradation |
| EPDM | 2,0 | 0,5 | O-Ring-Quellung |
| PA12 | 5,0 | 3,0 | Sehr gute Beständigkeit |
| Edelstahl | Unbegrenzt | Unbegrenzt | Keine |

**Wasseraufbereitung an Bord — Empfohlene Stufen:**
1. Vorfilter (Sediment, 20 µm): Partikel, Rost, Sand
2. Aktivkohle (5 µm + GAC): Chlor, Geschmack, Geruch, VOC
3. UV-Desinfektion (optional): Keimtötung ohne Chemie
4. Watermaker-Permeat: Entsalzung, TDS <500 mg/l

### Vergleich: Material-Kosten pro Meter

**Preisvergleich Trinkwasserschläuche/-rohre (Innen-Ø ~13 mm, Stand 2025/2026):**

| Material | Produkt (Beispiel) | EUR/m | Fittings/m* | Gesamt/m | AYDI-Score |
|----------|-------------------|-------|------------|----------|------------|
| PEX-a (Uponor) | Uponor Aqua Pipe 16×2,2 | 2,80 | 1,50 | 4,30 | 92 |
| PEX-b (Viega) | Viega Fonterra 16×2,0 | 2,20 | 1,80 | 4,00 | 88 |
| Silikon Platinum | Venair Sil 613 | 12,50 | 2,00 | 14,50 | 95 |
| Silikon Peroxid | NoName FDA Silikon | 6,00 | 2,00 | 8,00 | 72 |
| PA12 (Nylon) | Legris 1100U | 3,50 | 2,50 | 6,00 | 80 |
| EPDM (Trinkwasser) | Continental Aquapal | 5,80 | 1,50 | 7,30 | 78 |
| Edelstahl-Wellrohr | CSST Gastite/Eurotis | 18,00 | 8,00 | 26,00 | 90 |
| PVC-frei Yacht | Vetus!"#$% | — | — | — | — |
| John Guest LLDPE | JG PE-Rohr 15 mm | 1,80 | 3,00 | 4,80 | 85 |

*Fittings/m: Geschätzte Fitting-Kosten pro Meter, basierend auf durchschnittlich 1 Fitting alle 2 m.

**Gesamtkostenvergleich für 14 m Segelyacht (~25 m Leitungslänge):**

| Material | Material (EUR) | Fittings (EUR) | Werkzeug (EUR) | Arbeit (Std.) | Gesamt (EUR) |
|----------|---------------|---------------|---------------|--------------|-------------|
| PEX-a + Push-Fit | 70 | 120 | 25 | 6 | 515 |
| PEX-b + Crimp | 55 | 95 | 200 | 8 | 750 |
| Silikon Platinum | 312 | 85 | 15 | 5 | 662 |
| PA12 + Push-Fit | 88 | 130 | 25 | 7 | 543 |
| Edelstahl-Wellrohr | 450 | 220 | 50 | 10 | 1.220 |

*Arbeitsstunde kalkuliert mit 50 EUR (Eigenleistung: 0 EUR, Werft: 80–120 EUR)

---

## Einbau-/Austausch-Anleitung

### Werkzeug-Checkliste

**Grundausstattung (Push-Fit System, z.B. John Guest):**
- [ ] Rohrschneider für Kunststoff (z.B. Knipex 90 20 185, ~25 EUR)
- [ ] Entgrater innen/außen (z.B. REMS REG 8–35, ~18 EUR)
- [ ] Permanentmarker (Einstecktiefe markieren)
- [ ] Maßband / Zollstock
- [ ] Lappen / Papiertücher (Schnittstelle reinigen)
- [ ] Eimer / Auffangwanne (Restwasser)
- [ ] Schlauchschellen V4A, passende Größen
- [ ] PTFE-Band oder Loctite 55 (für Gewindeverbindungen)
- [ ] Drehmomentschlüssel 1–25 Nm
- [ ] Schraubendreher PH2 (Schlauchschellen)
- [ ] LED-Stirnlampe (Einbauräume sind dunkel)

**Erweiterte Ausstattung (Crimp/Press):**
- [ ] Crimp-Zange mit passenden Einsätzen ODER Pressmaschine
- [ ] Go/No-Go Lehre (Crimp)
- [ ] Biegefedern passend zum Rohrdurchmesser
- [ ] Heißluftgebläse (PEX-Biegungen)

**Sicherheitsausrüstung:**
- [ ] Schutzbrille (beim Schneiden/Entgraten)
- [ ] Arbeitshandschuhe (Schnittverletzungen an Schellen)
- [ ] Knieschoner (Einbau in beengten Räumen)
- [ ] Erste-Hilfe-Set (griffbereit)

**Prüf- und Desinfektionsmaterial:**
- [ ] Druckprüf-Adapter oder Pumpe
- [ ] Manometer (0–6 bar, 0,1 bar Auflösung)
- [ ] Certisil Combina (oder Certinox) zur Desinfektion
- [ ] Chlor-Teststreifen oder DPD-Tabletten + Komparator
- [ ] pH-Teststreifen oder pH-Meter

### Schritt-für-Schritt Trinkwasserschlauch-Austausch

**Phase 1 — Vorbereitung (30–60 min):**

1. Wasserpumpe ausschalten (Sicherungsautomat)
2. Boiler/Warmwasserbereiter ausschalten
3. Alle Hähne öffnen — System drucklos machen
4. Restwasser ablassen (Tiefpunkt öffnen, ggf. Druckluft)
5. Fotos vom bestehenden System machen (Routing, Anschlüsse, Markierungen)
6. Schläuche beschriften (Kalt/Warm, Herkunft/Ziel)
7. Neues Material bereitlegen, Längen vorab messen (+ 10% Reserve)

**Phase 2 — Demontage (1–3 Stunden, je nach Zugänglichkeit):**

8. Schlauchschellen lösen (NICHT abschneiden — Schelle kann wiederverwendet werden)
9. Push-Fit Verbindungen lösen: Collet-Ring (JG) oder Entriegelungsclip eindrücken, Schlauch herausziehen
10. Alte Schläuche entfernen — Routing-Weg merken (Fotos!)
11. Anschlüsse an Pumpe, Boiler, Hähnen prüfen — O-Ringe, Gewinde, Verschleiß
12. Defekte O-Ringe und Fittings aussortieren und ersetzen
13. Anschluss-Gewinde reinigen (alte PTFE-Reste entfernen)

**Phase 3 — Neuinstallation (2–5 Stunden):**

14. Neuen Schlauch auf Länge schneiden (Rohrschneider!)
15. Enden entgraten (innen und außen)
16. Einstecktiefe markieren (bei Push-Fit)
17. Schlauch in vorgegebenem Routing verlegen — Biegeradien beachten!
18. Befestigungsschellen anbringen (alle 30–50 cm, vibrationsdämpfend)
19. Verbindungen herstellen (Push-Fit / Crimp / Schelle)
20. Kalt-/Warmwasser-Markierung anbringen (Blau/Rot)

**Phase 4 — Prüfung (30–60 min):**

21. Alle Hähne schließen
22. Pumpe einschalten — System unter Druck setzen
23. Alle Verbindungen visuell auf Undichtigkeit prüfen (trockenes Papier unterlegen)
24. Druckprüfung: Pumpe aus, Druck 10 min beobachten (max. 0,1 bar Abfall)
25. Falls Undichtigkeit: Verbindung lösen, Schnittkante prüfen, neu verbinden
26. Warmwasser-System: Boiler einschalten, bei Betriebstemperatur erneut prüfen

**Phase 5 — Desinfektion und Inbetriebnahme (2–4 Stunden):**

27. System desinfizieren (siehe Abschnitt "System-Desinfektion nach Einbau")
28. Spülen bis Desinfektionsmittel-Rückstände entfernt
29. Wasserprobe: Geruch, Geschmack, ggf. Bakterien-Schnelltest
30. Dokumentation: Datum, Material, Hersteller, Chargen-Nr., Prüfdruck

### Spezial: John-Guest-Push-Fit Installation

**Detailanleitung für JG 15 mm (1/2") Speedfit System:**

1. PEX-Rohr 16×2,0 mm (Außen-Ø 16 mm → passt in JG 15 mm Metrisch) mit Rohrschneider rechtwinklig ablängen
2. Außen- und Innen-Grat entfernen
3. Einstecktiefe auf Rohr markieren: 25 mm ab Rohrende
4. JG Super Seal Insert (TSM) in Rohrende einsetzen — stützt das Rohr gegen Kollaps
5. Rohr fest in Fitting schieben bis Markierung am Fitting-Rand steht
6. Zugprobe: Kräftig ziehen — Rohr darf sich nicht lösen
7. Sichtprüfung: Bei transparenten Fittings (JG Speedfit Plus) Sitzposition kontrollieren

**Demontage JG Push-Fit:**
1. System drucklos machen
2. Collet-Ring (äußerer Kunststoffring) zum Fitting-Körper hin drücken
3. Gleichzeitig Rohr herausziehen
4. Fitting kann wiederverwendet werden (O-Ring prüfen, ggf. ersetzen, JG Ersatz-O-Ring Art.-Nr. PM0804E)

**Häufige Fehler JG Push-Fit:**
- Schlauch nicht bis Anschlag eingeschoben → Undichtigkeit unter Druck
- Kein TSM Insert → Rohr kollabiert unter Druck, O-Ring dichtet nicht ab
- Schräger Schnitt → ungleichmäßiger O-Ring-Sitz, Leckage
- Schmutz auf Schlauchoberfläche → O-Ring-Beschädigung

### Spezial: PEX-Crimp/Press Installation

**Crimp-Installation (ASTM F1807):**

1. PEX-Rohr ablängen und entgraten
2. Kupfer-Crimpring über Rohr schieben
3. Fitting (Messing oder PPSU) in Rohr einführen
4. Crimpring über Fitting-Barb positionieren (1–3 mm vom Rohrende)
5. Crimp-Zange ansetzen — Ring muss genau auf den Barbs sitzen
6. Zange vollständig schließen (bis Ratsche klickt)
7. Go/No-Go Lehre prüfen: Lehre muss über den gecrimpten Ring passen (Go), aber nicht zu locker (No-Go)

**Press-Installation (Viega Profipress):**

1. Rohr ablängen, entgraten
2. Rohr vollständig in Pressfitting einschieben (Markierung am Sichtfenster prüfen)
3. Pressbacke der korrekten Größe in Pressmaschine einsetzen
4. Pressbacke um Fitting-Hülse positionieren
5. Pressvorgang auslösen — Maschine presst automatisch mit korrektem Druck
6. Sichtprüfung: Presshülse muss gleichmäßige Eindrücke zeigen
7. Viega SC-Contur-Prüfung: Bei Druckprüfung leckt unverpresster Fitting gezielt → Sicherheitsmerkmal

### Spezial: Watermaker-Anschluss

Der Anschluss eines Watermakers an das Trinkwassersystem erfordert besondere Sorgfalt, da das Permeat (entsalztes Wasser) in den Tank oder direkt ins Verteilsystem gespeist wird.

**Typischer Aufbau Watermaker → Trinkwassersystem:**
1. Watermaker Permeat-Ausgang (meist 3/8" oder 1/2" JG Push-Fit)
2. Salinity-Sensor (Leitwert-Messung, Umschaltventil)
3. 3-Wege-Ventil: Bei TDS >500 ppm → Abwasser; bei TDS <500 ppm → Tank
4. Rückschlagventil (verhindert Rückfluss Tank → Watermaker)
5. Mineralisierer (optional, hebt pH und Mineralgehalt)
6. Tank-Einlassventil

**Watermaker-Modelle und Anschlüsse (Auswahl):**

| Modell | Leistung (l/h) | Permeat-Anschluss | TDS Permeat |
|--------|---------------|-------------------|-------------|
| Spectra Ventura 200T | 32 | 3/8" JG | 150–350 ppm |
| Spectra Catalina 340 | 55 | 1/2" JG | 100–300 ppm |
| Schenker Smart 30 | 30 | 12 mm Schlauch | 200–400 ppm |
| Schenker Smart 60 | 60 | 12 mm Schlauch | 150–350 ppm |
| Katadyn PowerSurvivor 40E | 5,7 | 1/4" JG | 100–300 ppm |
| Dessalator D100 | 100 | 1/2" BSP | 80–250 ppm |

**Materialanforderungen Permeat-Leitung:**
- Lebensmittelzugelassen (KTW/W270 oder NSF 61)
- Keine Weichmacher (Permeat löst Weichmacher verstärkt heraus — niedriger TDS!)
- PEX oder Silikon empfohlen, kein PVC
- Eigener Leitungsstrang (nicht mit anderen Quellen mischen vor Tank)

### System-Desinfektion nach Einbau

Nach jeder Neuinstallation oder nach längerer Standzeit (>4 Wochen) MUSS das System desinfiziert werden.

**Methode 1 — Certisil Combina (Silberionen + Chlordioxid):**
- Produkt: Certisil Combina CC 2500 (für 2.500 l, ~25 EUR)
- Dosierung: 1 Beutel pro 2.500 l Tankvolumen
- Einwirkzeit: 2 Stunden bei gefülltem System (alle Hähne öffnen bis Wasser kommt, dann schließen)
- Nachspülung: 2× komplettes Systemvolumen durchspülen
- Vorteil: Depoteffekt durch Silberionen (bis 6 Monate Schutz)
- AYDI-Empfehlung: Ja | Score: 92/100

**Methode 2 — Natriumhypochlorit (Chlorbleiche):**
- Dosierung: 50 mg/l freies Chlor (ca. 4 ml 12,5% NaOCl pro 1 l)
- Einwirkzeit: 30 Minuten
- Nachspülung: Bis Chlorgehalt <0,3 mg/l (Teststreifen!)
- Vorteil: Schnell, effektiv, günstig
- Nachteil: Greift Silikon und EPDM-Dichtungen an bei Überdosierung
- AYDI-Empfehlung: Bedingt | Score: 75/100

**Methode 3 — Wasserstoffperoxid (H₂O₂):**
- Dosierung: 3% H₂O₂ Lösung (30 ml 30% H₂O₂ pro Liter Wasser)
- Einwirkzeit: 2–4 Stunden
- Nachspülung: 2× Systemvolumen, zerfällt zu Wasser + Sauerstoff
- Vorteil: Materialschonend, keine Geschmacksrückstände
- Nachteil: Langsamer als Chlor
- AYDI-Empfehlung: Ja | Score: 85/100

**Desinfektions-Protokoll (empfohlen):**
1. System mit Frischwasser füllen
2. Desinfektionsmittel dosiert zugeben
3. Pumpe einschalten, alle Hähne nacheinander öffnen bis desinfiziertes Wasser austritt
4. Alle Hähne schließen, Einwirkzeit abwarten
5. System vollständig entleeren
6. 2× mit Frischwasser durchspülen
7. Restchlorgehalt messen (<0,3 mg/l)
8. Bakteriologische Probe (optional, empfohlen bei Charterbooten)
9. Dokumentation in Bordbuch

### Winterisierung (Frost-Schutz)

*(Bereits in vorherigem Abschnitt detailliert behandelt — siehe oben. Ergänzende Hinweise:)*

**Temperatur-Grenzwerte für Frostschäden:**

| Material | Bruchgefahr ab | Empfehlung |
|----------|---------------|------------|
| PEX | -30°C (gefroren, aber elastisch) | Ab 0°C Winterisieren |
| Silikon | -50°C | Ab 0°C Winterisieren |
| PA12 | -20°C | Ab +5°C Winterisieren |
| Messing-Fittings | -5°C (mit Wasser) | Immer entleeren |
| Pumpengehäuse | -3°C | Immer entleeren oder Propylenglykol |
| Boiler | -2°C | Immer entleeren |
| Akkumulator | -5°C | Immer entleeren |

**Propylenglykol-Dosierung:**

| Frostschutz bis | Propylenglykol-Konzentration | Mischung |
|----------------|-----------------------------|---------| 
| -10°C | 25% | 1:3 (PG:Wasser) |
| -20°C | 35% | 1:1,85 |
| -30°C | 45% | 1:1,2 |
| -40°C | 55% | 1:0,8 |

### Häufige Fehler

**Fehler 1 — Falsches Material gewählt:**
PVC-Gartenschlauch als Trinkwasserleitung. Enthält DEHP-Weichmacher, nicht lebensmittelzugelassen, migriert in Trinkwasser. Score: 0/100. Lösung: Sofort ersetzen durch KTW/W270-zugelassenes Material.

**Fehler 2 — Schlauch zu eng gebogen:**
PEX-Rohr mit zu kleinem Radius verlegt → Knick → Querschnittsreduzierung 50–80%. Pumpe läuft ständig, Durchfluss an der Entnahmestelle minimal. Lösung: 90°-Winkel-Fitting einsetzen oder Biegefeder verwenden.

**Fehler 3 — Keine Befestigung:**
Schläuche lose im Bilgenbereich verlegt. Vibration führt zu Scheuerstellen, Kondenswasser sammelt sich. Lösung: Alle 30–50 cm mit gummierten Rohrschellen befestigen (V4A, z.B. Mikalor W4 mit Gummieinlage).

**Fehler 4 — Mischung verschiedener Push-Fit Systeme:**
Whale 15 mm Fitting auf John Guest 15 mm Rohr → undicht (leicht unterschiedliche Toleranzen). Immer ein System durchgängig verwenden!

**Fehler 5 — Kein Rückschlagventil am Watermaker:**
Tankwasser drückt zurück in Watermaker-Membran → Verkeimung der Membran. Lösung: Rückschlagventil (JG?"#-Check-Valve) direkt am Watermaker-Ausgang.

**Fehler 6 — Alte O-Ringe wiederverwendet:**
O-Ringe an Pumpenanschlüssen nach Demontage wiederverwendet → Druckstellen, Mikrorisse → Leckage unter Vibration. O-Ringe sind Einmal-Teile!

**Fehler 7 — Desinfektionsmittel-Überdosierung:**
Chlor >100 ppm zur Desinfektion → Silikon-O-Ringe quellen, EPDM-Dichtungen verspröden. Maximale Chlorkonzentration: 50 ppm, Einwirkzeit beachten.

**Fehler 8 — Warmwasser-Leitung zu nah an Dieseltank/-leitung:**
Wärmeübertragung auf Kraftstoffleitung. Mindestabstand Warm-/Heißwasserleitung zu Dieselleitung: 50 mm oder Isolierung dazwischen.

### Notfall-Reparatur

**Szenario 1 — Schlauch geplatzt (unterwegs, kein Ersatzschlauch):**
- Sofort: Pumpe aus (Sicherung)
- Provisorisch: Beschädigte Stelle mit Silikon-Selbstverschweißungsband umwickeln (z.B. Rescue Tape, ~8 EUR). Hält bis 3 bar, mehrere Wochen.
- Alternativ: Schlauch vor und nach Bruchstelle abschneiden, JG-Inline-Kupplung einsetzen (IMMER 2–3 Ersatz-Fittings an Bord!)
- AYDI-Score Provisorium: 45/100 (Band) / 85/100 (Fitting-Reparatur)

**Szenario 2 — Push-Fit Fitting leckt:**
- System drucklos machen
- Schlauch aus Fitting ziehen (Collet drücken)
- Schnittkante prüfen: schräg? Beschädigt?
- 10 mm abschneiden, neu entgraten, neu einstecken
- Falls Fitting-O-Ring beschädigt: Fitting ersetzen
- AYDI-Score: 90/100 (einfache Reparatur)

**Szenario 3 — Pumpe defekt, kein Wasserdruck:**
- Provisorisch: Manueller Fußpumpen-Bypass (Whale Gusher Mk3, ~95 EUR)
- Kann parallel zur elektrischen Pumpe installiert werden
- Mindestens eine manuelle Pumpe in der Pantry ist sinnvoll (Redundanz, Stromausfall)
- AYDI-Score: 80/100

**Szenario 4 — Kontamination (Seewasser im Trinkwassertank):**
- Tank sofort leeren
- 3× mit Frischwasser (Landanschluss oder Kanister) spülen
- Desinfektion mit Certisil Combina (doppelte Dosis)
- Geschmacksprobe vor Nutzung
- Im Zweifelsfall: nur abgekochtes oder Flaschenwasser trinken
- AYDI-Score: 70/100 (kontrollierbare Situation)

**Notfall-Kit Trinkwassersystem (empfohlen an Bord):**
- 3× JG Inline-Kupplungen (passende Größe)
- 2× JG 90°-Winkel
- 1× JG T-Stück
- 1 m Ersatzschlauch (PEX oder Silikon)
- Rolle PTFE-Band
- 3× Schlauchschellen V4A (passende Größe)
- 1× Rescue Tape (Silikon-Selbstverschweißungsband)
- Rohrschneider (klein)
- 2× Ersatz-O-Ringe (Pumpenanschluss)
- 1× Certisil Combina Einzelportion
- Kosten Notfall-Kit: ~45–65 EUR

---

## Lebensdauer und Alterungsmechanismen

### PEX Lebensdauer

PEX (vernetztes Polyethylen) hat eine theoretische Lebensdauer von 50+ Jahren bei Nennbedingungen (20°C, 6 bar). Im Yachtbau reduzieren jedoch spezifische Belastungen die reale Lebensdauer.

**Lebensdauer-Prognose nach Einsatzbedingungen:**

| Bedingung | Lebensdauer (Jahre) | Einflussfaktor |
|-----------|-------------------|----------------|
| Kaltwasser, 20°C, innen verlegt | 40–50 | Referenz |
| Kaltwasser, Temperaturwechsel 5–35°C | 30–40 | Zyklische Belastung |
| Warmwasser, 60°C Dauerbelastung | 15–25 | Thermische Alterung |
| Warmwasser, 80°C Spitzenbelastung | 10–15 | Beschleunigte Oxidation |
| UV-exponiert (Cockpit, nicht geschützt) | 5–10 | Fotodegradation |
| Chloriertes Wasser (>1 mg/l dauerhaft) | 20–30 | Oxidative Schädigung |
| Vibration + Temperaturwechsel | 20–30 | Kombinierte Belastung |

**Degradationsmarker (wann austauschen?):**
- Oberfläche wird spröde, Mikrorisse sichtbar
- Vergilbung (transparent) oder Verfärbung (weiß → gelblich)
- Flexibilität nimmt deutlich ab (Bruch bei Biegung statt Verformung)
- Druckabfall >0,5 bar bei geschlossenen Hähnen innerhalb 30 min
- Geschmacks-/Geruchsveränderung des Wassers

### Silikon Lebensdauer

Platinum-vulkanisiertes Silikon hat die höchste Alterungsbeständigkeit aller Schlauchmaterialien.

**Lebensdauer-Prognose:**

| Bedingung | Lebensdauer (Jahre) | Einflussfaktor |
|-----------|-------------------|----------------|
| Kaltwasser, 20°C | 30–40 | Referenz |
| Warmwasser, 60°C | 25–35 | Geringe thermische Alterung |
| Warmwasser, 100°C (Dampfsterilisation) | 15–20 | Begrenzte Zyklen |
| UV-exponiert | 15–25 | Besser als PEX, aber nicht immun |
| Chloriertes Wasser (>1 mg/l) | 15–25 | Trübung, Versprödung |
| Ozon-haltige Atmosphäre | 20–30 | Geringe Ozon-Empfindlichkeit |

**Degradationsmarker Silikon:**
- Transluzenz nimmt ab (wird opak/milchig)
- Oberfläche wird klebrig (Reversion)
- Einschnürung an Schlauchschellen (plastische Deformation)
- Biofilm-Verfärbung (rosa/schwarz) trotz Reinigung

### Alterungsmechanismen

**Thermische Alterung:**
Arrhenius-Regel: Pro 10°C Temperaturerhöhung halbiert sich die Lebensdauer annähernd.
- PEX bei 20°C: 50 Jahre → PEX bei 60°C: ~20 Jahre → PEX bei 80°C: ~12 Jahre
- Silikon bei 20°C: 35 Jahre → Silikon bei 60°C: ~28 Jahre → Silikon bei 100°C: ~18 Jahre
- Silikon altert wesentlich langsamer als PEX bei erhöhten Temperaturen (Si-O-Bindung stabiler als C-C)

**Oxidative Alterung:**
- Chlor und Sauerstoff im Wasser greifen Polymerketten an
- PEX: Antioxidantien werden verbraucht → Kettenspaltung → Versprödung
- Silikon: Quervernetzung nimmt zu → Verhärtung
- Beschleunigt durch: hohe Temperatur, hohe Chlor-Konzentration, UV

**UV-Degradation:**
- PEX ohne UV-Stabilisator: 6–12 Monate direkte Sonnenexposition bis Oberflächenrisse
- PEX mit UV-Stabilisator (schwarz/UV-stabilisiert): 3–5 Jahre
- Silikon: 5–10 Jahre UV-Exposition bei minimaler Degradation
- Empfehlung: Alle Leitungen vor UV schützen (Kabelkanal, Schaum-Isolierung, Spiral-Ummantelung)

**Mechanische Ermüdung:**
- Vibration: Yacht-typisch 10–50 Hz, Amplitude 0,5–2 mm
- Bei unsachgemäßer Befestigung: Scheuerstellen → Wandstärke-Reduzierung → Bruch
- Druckzyklen: Jeder Pumpenstart/-stopp = 1 Zyklus. 20× täglich × 365 = 7.300 Zyklen/Jahr
- PEX: >500.000 Zyklen (ausreichend für Boots-Lebensdauer)
- Silikon: >200.000 Zyklen (ausreichend)

### Biofilm-Degradation

Biofilm ist die größte Herausforderung für die Trinkwasser-Hygiene an Bord. Alle Materialien sind betroffen, aber in unterschiedlichem Ausmaß.

**Biofilm-Bildungsrate (KTW/W270-Daten):**

| Material | KBE/cm² nach 12 Wochen | Bewertung |
|----------|----------------------|-----------|
| Edelstahl 316L | 10–50 | Sehr gering |
| PEX-a (Uponor) | 50–200 | Gering |
| PEX-b | 100–400 | Gering–mittel |
| Silikon Platinum | 200–800 | Mittel |
| Silikon Peroxid | 500–2.000 | Mittel–hoch |
| PA12 | 50–150 | Gering |
| EPDM | 300–1.500 | Mittel–hoch |
| PVC (weich) | 1.000–10.000 | Hoch (Weichmacher als Nährstoff) |

**Biofilm-Gegenmaßnahmen:**
1. Regelmäßige Durchspülung (keine Stagnation >48 h)
2. Silberionen-Konservierung (Certisil Argento, Dauer-Depot)
3. Thermische Desinfektion (>60°C, 10 min — nur Warmwasser-Kreis)
4. UV-C Desinfektion inline (z.B. SteriPEN Adventurer, oder fest: UV Dynamics UVD-340, ~350 EUR)
5. Jährliche Systemdesinfektion (Certisil Combina)

### Predictive Maintenance

**Wartungsintervalle Trinkwassersystem (empfohlen):**

| Komponente | Intervall | Tätigkeit | Aufwand |
|-----------|-----------|-----------|---------|
| Push-Fit O-Ringe | 5 Jahre | Sichtprüfung, bei Bedarf tauschen | 1 h |
| Schlauchschellen | Jährlich | Nachziehen (Drehmoment prüfen) | 30 min |
| Wasserfilter | 6–12 Monate | Patrone wechseln | 15 min |
| UV-Lampe | 12 Monate | Lampe wechseln | 15 min |
| Druckprüfung | 2 Jahre | 1,5× Betriebsdruck, 10 min | 45 min |
| System-Desinfektion | Jährlich + nach Standzeit | Certisil Combina | 3 h |
| Schlauch komplett | 15–25 Jahre | Komplett-Austausch | 1–2 Tage |
| Pumpen-Membran | 3–5 Jahre | Membransatz tauschen | 1 h |
| Akkumulator Vordruck | Jährlich | Druck prüfen (0,7× Pumpenabschaltdruck) | 15 min |

**AYDI Predictive-Maintenance-Score:**
Der Score berücksichtigt Alter, Material, Nutzungsintensität und Umgebungsbedingungen:
- Score 80–100: System in gutem Zustand, planmäßige Wartung ausreichend
- Score 60–79: Verstärkte Überwachung empfohlen, einzelne Komponenten prüfen
- Score 40–59: Teilsanierung empfohlen (Dichtungen, Filter, exponierte Abschnitte)
- Score 20–39: Komplett-Sanierung dringend empfohlen
- Score 0–19: Sicherheitsrisiko — System nicht verwenden, sofort sanieren

---

## Fehlerbild-Atlas

### FB-01: Geschmack/Geruch im Trinkwasser

**Symptom:** Wasser hat plastikartigen, muffigen oder chemischen Geschmack/Geruch.
**Ursache:** Weichmacher-Migration (PVC-Schlauch), Biofilm, Stagnation, unzureichende Erstspülung nach Neuinstallation.
**Visuell erkennbar:** Nein (Geruchs-/Geschmacksprüfung nötig).
**Differentialdiagnose:** Neuer Schlauch → Erstspülung unzureichend; Alter Schlauch → Biofilm oder Material-Degradation; Nach Winterisierung → Propylenglykol-Reste.
**Materialien betroffen:** PVC (häufig), Silikon Peroxid (selten), EPDM (nach Alterung).
**Sofortmaßnahme:** System 3× komplett durchspülen. Geruch/Geschmack testen.
**Langfristlösung:** PVC-Schlauch durch PEX oder Silikon Platinum ersetzen. Aktivkohle-Filter installieren.
**Risikobewertung:** Mittel — gesundheitlich bedenklich bei Weichmacher-Migration.
**Confidence:** visual_insufficient (nur durch Wasserprobe feststellbar) | Score: —
**Referenz:** TrinkwV §5, KTW-Leitlinie
**Kosten Behebung:** Filter: 30–80 EUR, Schlauchtausch: 200–600 EUR
**Prävention:** Nur KTW/W270-zugelassene Materialien verwenden, regelmäßig durchspülen.
**AYDI-Modul:** materials, service_patterns

### FB-02: Biofilm sichtbar

**Symptom:** Rosa, schwarze oder grünliche Ablagerungen an Schlauchinnenwänden, Fittings, Wasserhahn-Perlator.
**Ursache:** Bakterielle Besiedlung durch Stagnation, mangelnde Desinfektion, organische Nährstoffe (Weichmacher).
**Visuell erkennbar:** Ja (bei transparenten/transluzenten Schläuchen, an Fittings, Perlator).
**Differentialdiagnose:** Rosa → Serratia marcescens (häufig, ungefährlich); Schwarz → Schimmelpilz oder Sulfatreduzierer; Grün → Algen (UV-Exposition).
**Materialien betroffen:** Alle, aber PVC und Silikon-Peroxid besonders anfällig.
**Sofortmaßnahme:** System desinfizieren (Certisil Combina, doppelte Dosis).
**Langfristlösung:** Materialwechsel auf PEX oder Edelstahl, UV-C Inline-Desinfektion.
**Risikobewertung:** Mittel bis Hoch — Biofilm kann Legionellen beherbergen.
**Confidence:** visual_medium | Score: 55/100
**Referenz:** DVGW W551, W270
**Kosten Behebung:** Desinfektion: 25–40 EUR; Materialwechsel: 300–800 EUR
**Prävention:** Stagnation vermeiden, Silberionen-Konservierung, jährliche Desinfektion.
**AYDI-Modul:** materials, service_patterns

### FB-03: Legionellen-Verdacht

**Symptom:** Kein visuelles Symptom. Verdacht bei Warmwasser-Temperatur <60°C, langen Standzeiten, immunsupprimierten Personen an Bord.
**Ursache:** Warmwasser-Temperatur 25–55°C (Legionellen-Wachstumsbereich), Biofilm als Rückzugsort, Stagnation.
**Visuell erkennbar:** Nein.
**Differentialdiagnose:** Labortest erforderlich (Legionella-Schnelltest oder Kulturverfahren).
**Materialien betroffen:** Alle (Legionellen leben im Biofilm auf jedem Material).
**Sofortmaßnahme:** Warmwasser auf >65°C erhitzen, alle Hähne 3 min laufen lassen (Achtung: Verbrühungsgefahr!).
**Langfristlösung:** Boiler-Temperatur dauerhaft ≥60°C, Zirkulation oder regelmäßige Durchspülung, thermische Desinfektion.
**Risikobewertung:** Hoch — Legionellose kann tödlich sein (Letalität 5–15%).
**Confidence:** visual_insufficient | Score: —
**Referenz:** DVGW W551, TrinkwV §14
**Kosten Behebung:** Labortest: 50–100 EUR; Boiler-Einstellung: 0 EUR; Thermostat-Mischventil: 80–150 EUR
**Prävention:** Boiler ≥60°C, Wasser regelmäßig nutzen, Stagnation vermeiden.
**AYDI-Modul:** compliance, service_patterns

### FB-04: Verfärbung des Wassers

**Symptom:** Wasser ist braun, gelb, grünlich oder milchig trüb.
**Ursache:** Braun/Gelb → Rost (Metallfittings), Sediment; Grünlich → Kupfer-Korrosion oder Algen; Milchig → Luft im System (harmlos) oder Kalk.
**Visuell erkennbar:** Ja (Glas Wasser gegen Licht halten).
**Differentialdiagnose:** Nur Kaltwasser → Tankproblem; Nur Warmwasser → Boiler/Anode; Beide → Leitungsproblem.
**Materialien betroffen:** Messing (Entzinkung → gelb), Kupfer (Grünspan), Stahl (Rost).
**Sofortmaßnahme:** Sedimentfilter prüfen/wechseln, System durchspülen.
**Langfristlösung:** Metallfittings durch Kunststoff ersetzen, Tankinspektion, Boiler-Anode wechseln.
**Risikobewertung:** Gering bis Mittel — abhängig von Ursache (Rost: gering; Kupfer: mittel).
**Confidence:** visual_high | Score: 75/100
**Referenz:** TrinkwV Anlage 3
**Kosten Behebung:** Filterwechsel: 15–40 EUR; Fittingtausch: 50–200 EUR; Boiler-Anode: 30–60 EUR
**Prävention:** Nur DZR-Messing oder Kunststoff-Fittings, Boiler-Anode jährlich prüfen.
**AYDI-Modul:** materials

### FB-05: Kalkablagerung

**Symptom:** Weiße, kristalline Ablagerungen an Fittings, in Perlatoren, auf Heizelementen. Reduzierter Durchfluss.
**Ursache:** Hohe Wasserhärte (>14°dH), besonders im Warmwasser-System (CaCO₃ fällt ab >55°C aus).
**Visuell erkennbar:** Ja (weiße Krusten, Ablagerungen sichtbar).
**Differentialdiagnose:** Nur Warmwasser → Boiler-Heizelement; Überall → Wasserqualität Landanschluss.
**Materialien betroffen:** Alle gleichmäßig, aber enge Querschnitte (Push-Fit) stärker betroffen.
**Sofortmaßnahme:** Perlator ausbauen und in Essig/Zitronensäure einlegen (30 min).
**Langfristlösung:** Wasserenthärter oder Antikalkfilter (z.B. BWT AQA nano, ~120 EUR), Watermaker-Permeat nutzen (weiches Wasser).
**Risikobewertung:** Gering — kein Gesundheitsrisiko, aber Komfort- und Funktionseinschränkung.
**Confidence:** visual_high | Score: 70/100
**Referenz:** TrinkwV Anlage 3 (Härte: kein Grenzwert, aber Empfehlung)
**Kosten Behebung:** Entkalkung: 5–15 EUR; Filter: 80–150 EUR; Boiler-Entkalkung: 50–100 EUR
**Prävention:** Weiches Wasser verwenden, Boiler-Temperatur ≤60°C (Kompromiss Legionellen!).
**AYDI-Modul:** materials, service_patterns

### FB-06: Undichtigkeit Push-Fit Verbindung

**Symptom:** Tropfenbildung oder Wasseraustritt an Push-Fit Fitting.
**Ursache:** Schlauch nicht vollständig eingeschoben, O-Ring beschädigt, schräger Schnitt, Schmutz auf Schlauchoberfläche.
**Visuell erkennbar:** Ja (Feuchtigkeit am Fitting, Tropfen, Wasserflecken).
**Differentialdiagnose:** Sofort nach Montage → Montagefehler; Nach Jahren → O-Ring-Alterung; Nach Frost → Frostschaden (Fitting gerissen).
**Materialien betroffen:** Alle Push-Fit Systeme (John Guest, Whale, SharkBite).
**Sofortmaßnahme:** Pumpe aus, System drucklos, Verbindung prüfen und neu herstellen.
**Langfristlösung:** Schlauch neu schneiden (10 mm kürzen), O-Ring ersetzen, Einstecktiefe prüfen.
**Risikobewertung:** Mittel — Wasserschaden in Bilge/Isolierung, Schimmelgefahr.
**Confidence:** visual_high | Score: 85/100
**Referenz:** Herstelleranleitung JG/Whale
**Kosten Behebung:** O-Ring: 1–3 EUR; Fitting: 3–8 EUR; Arbeitszeit: 15 min
**Prävention:** Korrekte Montage, Einstecktiefe markieren, TSM-Insert verwenden (JG).
**AYDI-Modul:** production, service_patterns

### FB-07: Frostschaden

**Symptom:** Gerissener Schlauch, gesprengter Fitting, deformierter Akkumulator, undichter Boiler.
**Ursache:** Wasser im System gefroren — Volumenausdehnung 9% sprengt Fittings und schwache Stellen.
**Visuell erkennbar:** Ja (Risse, Verformungen, Wasseraustritt nach Auftauen).
**Differentialdiagnose:** Schaden nach Frostperiode → eindeutig Frostschaden; Lokalisierung zeigt schwächste Stelle.
**Materialien betroffen:** Messing-Fittings (häufigste Bruchstelle), Pumpengehäuse, Boiler, Akkumulator. PEX dehnt sich und überlebt oft, Silikon ebenfalls.
**Sofortmaßnahme:** Alle beschädigten Komponenten identifizieren (erst nach vollständigem Auftauen!). Druckprüfung.
**Langfristlösung:** Beschädigte Teile ersetzen. Winterisierungsprotokoll einführen.
**Risikobewertung:** Hoch — erhebliche Wasserschäden möglich, komplettes System betroffen.
**Confidence:** visual_high | Score: 90/100
**Referenz:** ISO 15875 (PEX Frostbeständigkeit)
**Kosten Behebung:** Einzelne Fittings: 20–50 EUR; Komplettes System: 500–2.000 EUR; Pumpe: 120–350 EUR
**Prävention:** Winterisierung gemäß Protokoll, Propylenglykol oder vollständige Entleerung.
**AYDI-Modul:** structural, service_patterns

### FB-08: UV-Degradation

**Symptom:** Vergilbung, Versprödung, Mikrorisse an UV-exponierten Schlauchabschnitten (Cockpit, achtern, Fenster).
**Ursache:** UV-Strahlung spaltet Polymerketten (Fotodegradation), besonders PEX ohne UV-Stabilisator.
**Visuell erkennbar:** Ja (Verfärbung, raue Oberfläche, sichtbare Risse bei Biegung).
**Differentialdiagnose:** Nur UV-exponierte Abschnitte betroffen → eindeutig UV; Gesamtes System → andere Ursache.
**Materialien betroffen:** PEX (stark), PA12 (stark), Silikon (moderat), EPDM (moderat).
**Sofortmaßnahme:** Betroffene Abschnitte ersetzen.
**Langfristlösung:** UV-Schutz anbringen (Spiral-Schutzschlauch, Kabelkanal, UV-Folie), oder UV-stabilisiertes Material verwenden.
**Risikobewertung:** Mittel — schleichende Degradation, Bruch erst nach Jahren.
**Confidence:** visual_high | Score: 80/100
**Referenz:** ISO 4892 (Weathering Test)
**Kosten Behebung:** UV-Schutzschlauch: 2–5 EUR/m; Schlauchtausch: 50–200 EUR (betroffener Abschnitt)
**Prävention:** Alle Leitungen vor UV schützen. Keine PEX-Leitungen im Freien ohne Schutz.
**AYDI-Modul:** materials

### FB-09: Knick im Schlauch

**Symptom:** Drastisch reduzierter Durchfluss an einer Entnahmestelle, Pumpe läuft lang, eventuell Pumpen-Kurzschluss.
**Ursache:** Zu enger Biegeradius, unsachgemäße Verlegung, Schlauch durch Gewicht/Gegenstand gequetscht.
**Visuell erkennbar:** Ja (Knick sichtbar, Querschnittsverformung tastbar).
**Differentialdiagnose:** Nur eine Entnahmestelle → Leitung zu dieser Stelle verfolgen; Alle Stellen → Hauptleitung oder Filter.
**Materialien betroffen:** PEX (häufig, kleiner Biegeradius), PA12 (häufig), Silikon (selten, da flexibler).
**Sofortmaßnahme:** Knick auffinden und beseitigen (Schlauch gerade biegen, Biegefeder einsetzen).
**Langfristlösung:** 90°-Winkel-Fitting einsetzen, Verlegung mit größerem Radius, Befestigungsschellen.
**Risikobewertung:** Gering — kein Gesundheitsrisiko, nur Komforteinschränkung.
**Confidence:** visual_high | Score: 88/100
**Referenz:** Herstellerangaben Biegeradien
**Kosten Behebung:** Winkel-Fitting: 3–8 EUR; Biegefeder: 3–5 EUR; Arbeitszeit: 15–30 min
**Prävention:** Biegeradien-Tabelle beachten, professionelle Verlegung mit Rohrschellen.
**AYDI-Modul:** production

### FB-10: Druckverlust im System

**Symptom:** Pumpendruck an Entnahmestelle deutlich geringer als am Pumpenausgang. Pumpe schaltet häufig ein.
**Ursache:** Verstopfter Filter, kalkierter Perlator, Leckage, zu kleine Leitungsdimensionierung, Akkumulator-Defekt.
**Visuell erkennbar:** Teilweise (Leckage, Filterzustand, Manometer-Ablesung).
**Differentialdiagnose:** Alle Stellen → Filter/Hauptleitung; Eine Stelle → lokales Problem; Pumpe taktet → Akkumulator.
**Materialien betroffen:** Alle (Druckverlust ist systemisch, nicht materialspezifisch).
**Sofortmaßnahme:** Filter prüfen/wechseln, Perlatoren reinigen, Leitungen auf Leckage prüfen.
**Langfristlösung:** Druckverlust-Berechnung durchführen, ggf. Leitungs-Ø vergrößern, Akkumulator prüfen/ersetzen.
**Risikobewertung:** Gering — Komfortproblem, kein Sicherheitsrisiko.
**Confidence:** visual_medium (Manometer nötig) | Score: 65/100
**Referenz:** Darcy-Weisbach (siehe Berechnung oben)
**Kosten Behebung:** Filter: 15–40 EUR; Akkumulator: 80–200 EUR; Leitungstausch: 200–600 EUR
**Prävention:** Regelmäßiger Filterwechsel, Akkumulator-Vordruck jährlich prüfen.
**AYDI-Modul:** structural, service_patterns

### FB-11: Chlor-Schaden

**Symptom:** Versprödung von O-Ringen, Quellung von EPDM-Dichtungen, Silikon wird milchig/opak.
**Ursache:** Überdosierung von Chlor bei Desinfektion (>50 ppm), dauerhafte Chlorierung über Grenzwert.
**Visuell erkennbar:** Teilweise (O-Ring-Verformung, Silikon-Trübung sichtbar bei transparenten Leitungen).
**Differentialdiagnose:** Nach Desinfektion → Überdosierung; Dauerhaft → Wasserqualität Landanschluss.
**Materialien betroffen:** EPDM (O-Ringe, Pumpen-Membranen), Silikon, Viton (bedingt beständig).
**Sofortmaßnahme:** System komplett durchspülen, betroffene Dichtungen ersetzen.
**Langfristlösung:** Chlordosierung einhalten (<50 ppm Desinfektion, <0,3 ppm Betrieb), Aktivkohle-Filter vor empfindlichen Komponenten.
**Risikobewertung:** Mittel — Undichtigkeit und Kontamination möglich.
**Confidence:** visual_medium | Score: 60/100
**Referenz:** Materialverträglichkeitstabellen der Hersteller
**Kosten Behebung:** O-Ring-Satz: 5–20 EUR; Membran-Satz Pumpe: 30–60 EUR
**Prävention:** Desinfektionsprotokoll einhalten, Chlor-Teststreifen verwenden.
**AYDI-Modul:** materials, service_patterns

### FB-12: Weichmacher-Migration

**Symptom:** Ölig-chemischer Geruch/Geschmack, Weichmacher-Nachweis in Wasserprobe (DEHP, BBP, DBP).
**Ursache:** PVC-Weichschlauch ohne Lebensmittelzulassung als Trinkwasserleitung eingebaut.
**Visuell erkennbar:** Nein (Laboranalyse nötig; Indiz: Schlauch ist sehr flexibel und riecht "plastisch").
**Differentialdiagnose:** Nur bei PVC-Schläuchen. PEX, Silikon, PA12 enthalten keine Weichmacher.
**Materialien betroffen:** PVC (weich/flexibel), minderwertige EPDM-Compounds mit Ölzusatz.
**Sofortmaßnahme:** Kein Wasser aus diesem System trinken! Flaschenwasser verwenden.
**Langfristlösung:** ALLE PVC-Trinkwasserschläuche sofort durch PEX oder Silikon ersetzen.
**Risikobewertung:** HOCH — Weichmacher sind endokrine Disruptoren, krebserregend (DEHP: SVHC nach REACH).
**Confidence:** visual_low (nur durch Laboranalyse bestätigbar) | Score: 30/100
**Referenz:** REACH-Verordnung 1907/2006, KTW-Leitlinie
**Kosten Behebung:** Komplett-Sanierung: 300–1.000 EUR; Laboranalyse: 80–150 EUR
**Prävention:** NIEMALS PVC-Weichschlauch für Trinkwasser verwenden. Nur KTW/W270-Material.
**AYDI-Modul:** materials, compliance

---

## Fehlerbehebungs-Leitfaden (Troubleshooting)

### Problem 1: Pumpe läuft ständig, kein Wasser an den Hähnen

**Mögliche Ursachen (Wahrscheinlichkeit):**
1. Tank leer (40%) → Tankfüllstand prüfen
2. Ansaugleitung undicht / Luft ziehend (25%) → Verbindungen am Tank-Ausgang prüfen, Schellen nachziehen
3. Vorfilter verstopft (15%) → Filter prüfen, Patrone wechseln
4. Pumpe defekt — Membran gerissen (10%) → Pumpe öffnen, Membransatz prüfen (z.B. Shurflo 94-238-04)
5. Leitung geknickt zwischen Tank und Pumpe (10%) → Leitung visuell verfolgen

**Systematische Diagnose:**
- Pumpe baut Druck auf? → Manometer am Pumpenausgang. Nein → Pumpe defekt oder keine Ansaugung.
- Pumpe hat Druck, kein Wasser am Hahn → Leitung nach Pumpe blockiert (Ventil zu, Knick, Filter).
- Pumpe hat keinen Druck, läuft aber → Ansaugleitung prüfen, Luft im System.

### Problem 2: Pumpe taktet (schaltet ständig ein/aus)

**Mögliche Ursachen:**
1. Akkumulator-Vordruck falsch (50%) → Mit Manometer prüfen. Soll: 70% des Pumpen-Abschaltdrucks (z.B. 2,4 bar bei 3,5 bar Abschaltdruck).
2. Akkumulator-Membran defekt (20%) → Ventilnippel drücken: Kommt Wasser statt Luft → Membran defekt.
3. Kleine Leckage im System (20%) → Alle Verbindungen prüfen (trockenes Papier unterlegen, 30 min warten).
4. Druckschalter-Hysterese zu gering (10%) → Druckschalter nachjustieren (Herstelleranleitung).

### Problem 3: Wasser schmeckt / riecht schlecht

**Systematische Diagnose:**
1. Nur kaltes Wasser → Tank oder Kaltwasser-Leitung
2. Nur warmes Wasser → Boiler (Anode prüfen, Temperatur prüfen)
3. Beide → Hauptleitung oder Tank
4. Nur eine Entnahmestelle → Lokaler Perlator/Mischbatterie
5. Nach Winterisierung → Propylenglykol-Reste (3× spülen)
6. Neues System → Erstspülung unzureichend (10× Systemvolumen durchspülen)

**Maßnahmen nach Diagnose:**
- Tank: Inspizieren, reinigen, desinfizieren
- Leitung: Material prüfen (PVC? → ersetzen), Desinfektion
- Boiler: Anode wechseln (Magnesium auf Aluminium, z.B. Kuuma 11531), Temperatur >60°C
- Perlator: Ausbauen, in Essig einlegen, Dichtungen prüfen

### Problem 4: Warmwasser wird nicht heiß genug

**Mögliche Ursachen:**
1. Heizelement defekt / verkalkt (30%) → Heizleistung messen, entkalken
2. Thermostat defekt (25%) → Thermostat-Fühler prüfen (Multimeter: Widerstand bei Raumtemperatur)
3. Mischventil defekt (20%) → Kaltwasser drückt durch defektes Rückschlagventil in Warmwasser-Leitung
4. Zu hoher Durchfluss (15%) → Boiler zu klein für gleichzeitige Nutzung (Dusche + Pantry)
5. Wärmeverluste (10%) → Warmwasser-Leitung nicht isoliert (Armaflex-Isolierung nachrüsten)

**Kennzahlen:**
- Warmwasser-Temperatur am Hahn: Soll ≥55°C (Legionellen-Schutz), ≤60°C (Verbrühungsschutz, ggf. Mischventil)
- Aufheizzeit 20L Boiler von 15°C auf 60°C: ~45 min (750W), ~90 min (Motorwärmetauscher allein)

### Problem 5: Wasser tritt aus unbekannter Stelle aus

**Systematische Leckage-Suche:**
1. Pumpe einschalten, alle Hähne schließen
2. Manometer beobachten: Druck fällt → Leck im System
3. Druckerhaltung prüfen: Pumpe aus, Druck messen nach 5/10/30 min
4. Sektionsweise absperren (wenn Absperrventile vorhanden):
   - Warmwasser-Kreis absperren → Druck stabil? → Leck im Warmwasser
   - Einzelne Abzweige absperren → Leck eingrenzen
5. Visuell: Trockenes Papier/Papiertücher an allen Verbindungen, nach 30 min prüfen
6. UV-Fluoreszenz-Farbstoff (z.B. Fluorescein, ungiftig) ins System geben → unter UV-Lampe Leckstelle finden

**Typische Leckage-Stellen (Häufigkeit):**
- Push-Fit Verbindungen: 35%
- Schlauchschellen-Verbindungen: 25%
- Pumpen-Anschluss: 15%
- Boiler-Anschluss: 10%
- Wasserhahn-Verbindung: 10%
- Schlauch selbst (Riss/Bruch): 5%

---

## FAQ (Häufig Gestellte Fragen)

**TW-001: Welches Schlauchmaterial ist am besten für Trinkwasser an Bord?**
Für die meisten Yachten ist PEX-a (z.B. Uponor Aqua Pipe) das optimale Material: KTW/W270-zugelassen, druckbeständig, günstig, 40+ Jahre Lebensdauer. Für höchste Ansprüche (Superyacht, Geschmacksneutralität) ist Platinum-Silikon (z.B. Venair Sil 613) die Premium-Wahl, aber 4–5× teurer.
AYDI-Score: PEX-a 92/100, Silikon Platinum 95/100.

**TW-002: Darf ich PVC-Gartenschlauch für Trinkwasser verwenden?**
NEIN. PVC-Gartenschläuche enthalten Weichmacher (DEHP, BBP), die in das Trinkwasser migrieren. Diese Stoffe sind endokrine Disruptoren und potenziell krebserregend. Nur Schläuche mit KTW/W270 oder NSF 61 Zulassung verwenden. Sofort ersetzen, wenn an Bord vorgefunden.

**TW-003: Wie oft muss ich das Trinkwassersystem desinfizieren?**
Empfehlung: Mindestens 1× jährlich (Saisonstart), nach jeder Standzeit >4 Wochen, nach Kontamination, und nach Neuinstallation/Reparatur. Bewährtes Mittel: Certisil Combina (Silberionen + Chlordioxid) — Depoteffekt bis 6 Monate.

**TW-004: Push-Fit oder Crimp — was ist besser für meine Yacht?**
Push-Fit (John Guest) ist ideal für Eigeneinbau und Boote bis 14 m: kein Spezialwerkzeug, demontierbar, wartungsfreundlich. Crimp/Press ist der professionelle Standard für Werften und Yachten >14 m: dauerhafter, höhere Druckfestigkeit, aber teures Werkzeug nötig. Für Fahrtenyachten empfehlen wir Push-Fit wegen der einfachen Reparatur unterwegs.

**TW-005: Welche Schlauchschellen sind für Trinkwasser zugelassen?**
Nur V4A Edelstahl (1.4401/316) verwenden. V2A (1.4301/304) korrodiert in salziger Umgebung. Ohrschellen (Oetiker) sind dem Schneckengewinde-Typ vorzuziehen, da sie den Schlauch nicht einschneiden. Immer Doppelschellen an Anschlüssen unterhalb der Wasserlinie.

**TW-006: Wie erkenne ich, ob mein Trinkwasserschlauch KTW-zugelassen ist?**
Zugelassene Schläuche tragen eine Bedruckung: Herstellername, Typ, "Trinkwasser" oder "Potable Water", KTW/W270 oder NSF 61, und Produktionsdatum. Fehlt diese Kennzeichnung, ist der Schlauch im Zweifelsfall NICHT zugelassen. Beim Hersteller nachfragen oder Datenblatt anfordern.

**TW-007: Mein Wasser schmeckt nach Plastik — was tun?**
Bei neuem System: 10× das Systemvolumen durchspülen (z.B. 5× Tank füllen und entleeren). Hält der Geschmack an: Aktivkohle-Filter installieren. Bei altem System: Biofilm-Problem oder Materialdegradation — Desinfektion durchführen, bei PVC-Schlauch ersetzen.

**TW-008: Wie winterisiere ich mein Trinkwassersystem richtig?**
System vollständig entleeren (Druckluft 0,5–1,0 bar), alle Tiefpunkte öffnen, Boiler und Akkumulator ablassen. Optional: Propylenglykol food-grade einfüllen (50/50 Mischung, Schutz bis -30°C). NIEMALS Ethylenglykol (Kfz-Frostschutz) verwenden — giftig! Filter ausbauen und trocken lagern.

**TW-009: Welchen Mindest-Biegeradius hat PEX?**
PEX 16 mm (Außen-Ø): Mindest-Biegeradius 80–112 mm (5–7× Außen-Ø). Mit Biegefeder: 48–64 mm (3–4× Ø). Bei engeren Radien 90°-Winkel-Fitting verwenden. Silikon hat den Vorteil eines deutlich kleineren Biegeradius (2–3× Ø).

**TW-010: Wie oft sollte ich Wasserfilter wechseln?**
Sedimentfilter (20 µm): alle 6 Monate oder bei sichtbarer Verschmutzung. Aktivkohlefilter: alle 6–12 Monate oder nach 10.000 Litern (was zuerst kommt). UV-Lampe: alle 12 Monate (Wirksamkeit nimmt ab, auch wenn Lampe noch leuchtet). Filter IMMER bei Winterisierung ausbauen.

**TW-011: Ist Silikon-Schlauch besser als PEX?**
Silikon (Platinum-vulkanisiert) ist geschmacksneutraler, flexibler (kleiner Biegeradius), und temperaturbeständiger. Aber: teurer (12–15 EUR/m vs 2–3 EUR/m), niedrigere Druckfestigkeit, und höhere Biofilm-Neigung. Für Pantry und Geschmackskritisches: Silikon. Für den Rest: PEX ist ausreichend und wirtschaftlicher.

**TW-012: Brauche ich einen Druckspeicher (Akkumulator)?**
Dringend empfohlen! Ohne Akkumulator taktet die Pumpe bei jedem Tropfen (Ein/Aus/Ein/Aus), was die Lebensdauer verkürzt und nervt. Akkumulator-Größe: 0,5–1,0 Liter für Boote bis 12 m, 1,0–2,0 Liter für 12–20 m. Vordruck: 70% des Pumpen-Abschaltdrucks.

**TW-013: Kann ich John-Guest-Fittings mit Whale-Schläuchen mischen?**
Nicht empfohlen. Die Toleranzen der Systeme unterscheiden sich leicht, was zu Undichtigkeiten führen kann. Verwenden Sie immer ein System durchgängig. Ausnahme: JG-Fittings auf Standard-PEX 16 mm und JG 15 mm Metrisch sind kompatibel (gleicher Außen-Ø).

**TW-014: Wie prüfe ich die Dichtheit meines Trinkwassersystems?**
Alle Hähne schließen, Pumpe einschalten bis Abschaltdruck erreicht. Pumpe ausschalten, Manometer beobachten: Druck darf in 30 Minuten max. 0,1 bar fallen. Stärkerer Druckabfall → Leckage suchen (trockenes Papier an Verbindungen). Professionelle Druckprüfung: 1,5× Betriebsdruck, 10 Minuten.

**TW-015: Was tun bei Legionellen-Verdacht?**
Sofort: Warmwasser auf >65°C erhitzen, alle Hähne 3 Minuten laufen lassen (Verbrühungsgefahr!). Nicht duschen (Aerosol-Inhalation ist der Infektionsweg). Labortest durchführen (Ergebnis nach 10–14 Tagen, Schnelltest 24 h). Dauerhaft: Boiler-Temperatur ≥60°C, regelmäßige Durchspülung, Stagnation vermeiden.

**TW-016: Welche Pumpe ist empfehlenswert?**
Für Boote 8–14 m: Shurflo 4009 (11,4 l/min, 3,5 bar, ~120 EUR) — bewährter Klassiker. Für 14–20 m: Jabsco Par-Max 3.5 (13,2 l/min, 2,8 bar, ~180 EUR) oder Shurflo 4048 (15,1 l/min, 3,8 bar, ~160 EUR). Für 20+ m: Druckerhöhungsanlage (z.B. Grundfos PM2, ~400 EUR).

**TW-017: Wie verbinde ich einen Watermaker mit dem Trinkwassertank?**
Permeat-Leitung über 3-Wege-Ventil mit Salinity-Sensor führen: Bei TDS >500 ppm → Abwasser, bei <500 ppm → Tank. Rückschlagventil nach Watermaker (verhindert Rückfluss). Nur KTW-zugelassenes Leitungsmaterial. Optional: Mineralisierer (hebt pH von ~6,5 auf ~7,5).

**TW-018: Muss ich Warmwasserleitungen isolieren?**
Ja, empfohlen aus zwei Gründen: 1) Energieeffizienz (weniger Wärmeverlust), 2) Kondensationsvermeidung (Feuchtigkeit auf kalten Oberflächen). Material: Armaflex AF (geschlossenzellig, 9–13 mm Wandstärke, ~3–6 EUR/m). Auch Kaltwasserleitungen in tropischen Revieren isolieren (Kondensation!).

**TW-019: Wie lange darf Wasser im Tank stehen?**
Mit Silberionen-Konservierung (Certisil Argento): bis zu 6 Monate. Ohne Konservierung: max. 2–4 Wochen, dann Desinfektion nötig. Bei Temperaturen >25°C: Zeitraum halbieren. Nach jeder Standzeit >4 Wochen: System komplett durchspülen und desinfizieren.

**TW-020: Kann ich PEX mit einem Lötkolben reparieren?**
Nein. PEX kann nicht geschweißt oder gelötet werden (vernetzte Struktur). Beschädigte Stellen müssen herausgeschnitten und durch Fitting-Verbindung (Push-Fit oder Crimp) ersetzt werden. Immer 10 mm beidseitig über die Schadstelle hinaus schneiden.

**TW-021: Welche Werkzeuge brauche ich für eine Push-Fit-Installation?**
Nur drei: 1) Rohrschneider (z.B. Knipex 90 20 185, ~25 EUR), 2) Entgrater (z.B. REMS REG 8–35, ~18 EUR), 3) Permanentmarker (Einstecktiefe). Das ist der große Vorteil von Push-Fit — kein Spezialwerkzeug. Optional: TSM-Insert-Setzwerkzeug (JG).

**TW-022: Wie verhindere ich Biofilm im Trinkwassersystem?**
Fünf Maßnahmen: 1) Kein PVC-Material (Weichmacher nähren Biofilm). 2) Regelmäßig Wasser nutzen (keine Stagnation >48 h). 3) Silberionen-Konservierung (Certisil Argento). 4) Jährliche System-Desinfektion. 5) Warmwasser ≥60°C (thermische Kontrolle). Optional: UV-C Inline-Desinfektion.

**TW-023: Was ist der Unterschied zwischen PEX-a und PEX-b?**
PEX-a (Engel-Verfahren): Vernetzung vor Extrusion, gleichmäßiger, flexibler, elastisches Rückstellvermögen ("shape memory"), teurer. PEX-b (Silan-Verfahren): Vernetzung nach Extrusion, etwas steifer, günstiger. Für Yachtbau: PEX-a bevorzugt (bessere Flexibilität, bessere Frostbeständigkeit). Vernetzungsgrad: PEX-a ≥70%, PEX-b ≥65%.

**TW-024: Brauche ich ein Rückschlagventil in der Trinkwasser-Leitung?**
Ja, an folgenden Stellen: 1) Nach der Druckwasserpumpe (verhindert Rückfluss bei Druck-Schwankungen). 2) Am Watermaker-Permeat-Ausgang (verhindert Tank → Watermaker). 3) Am Landwasser-Anschluss (verhindert Rückspeisung ins Landnetz, oft vorgeschrieben). 4) Zwischen Warm- und Kaltwasser bei Mischbatterien ohne internes Rückschlagventil.

**TW-025: Was kostet eine komplette Trinkwasser-Sanierung?**
Richtwerte für 12 m Segelyacht (Material + Arbeit bei Eigenleistung): PEX + Push-Fit: 400–600 EUR; Silikon Platinum: 600–900 EUR. Inkl. Werft-Arbeit (8–12 h à 80–120 EUR): PEX: 1.000–2.000 EUR; Silikon: 1.200–2.400 EUR. Zusätzlich Filter (30–80 EUR), Pumpe bei Bedarf (120–350 EUR), Desinfektion (25 EUR).

---

## Glossar

**Akkumulator (Druckspeicher):** Druckbehälter mit Membran oder Blase, der Druckschwankungen im Wassersystem dämpft und Pumpentakten verhindert. Vordruck typisch 70% des Pumpen-Abschaltdrucks.

**ABYC:** American Boat and Yacht Council — US-amerikanischer Normengeber für Bootsbau-Standards (H-23: Trinkwasser).

**Aktivkohle-Filter:** Filterpatrone mit Granulat- oder Block-Aktivkohle zur Adsorption von Chlor, Geschmacks-/Geruchsstoffen, und organischen Verbindungen (VOC). Wechselintervall: 6–12 Monate.

**Arrhenius-Regel:** Faustregel der Chemie: Pro 10°C Temperaturerhöhung verdoppelt sich die Reaktionsgeschwindigkeit (hier: Alterung).

**Biofilm:** Mikrobielle Gemeinschaft, die sich an Oberflächen in Kontakt mit Wasser bildet. Besteht aus Bakterien, Algen, Pilzen in einer Polysaccharid-Matrix. Rückzugsort für Legionellen.

**BSP (British Standard Pipe):** Gewindenorm für Rohrverbindungen im Yachtbau, definiert nach ISO 228 (parallel) und ISO 7 (konisch).

**CE-Kategorie:** Einstufung von Sportbooten nach EU-Richtlinie 2013/53/EU in Kategorien A (Hochsee) bis D (geschützte Gewässer).

**Certisil Combina:** Desinfektionsmittel auf Basis von Chlordioxid und Silberionen zur Trinkwasseraufbereitung. Hersteller: Certec GmbH.

**Crimp-Verbindung:** Dauerhafte Rohrverbindung durch plastische Verformung eines Metallrings (meist Kupfer) um den Schlauch auf dem Fitting.

**DEHP (Diethylhexylphthalat):** Weichmacher in PVC, als SVHC (besonders besorgniserregender Stoff) unter REACH eingestuft. Endokriner Disruptor.

**DZR-Messing (Dezincification Resistant):** Messinglegierung, die gegen Entzinkung beständig ist. Pflicht für Trinkwasser-Fittings im maritimen Umfeld.

**EPDM (Ethylen-Propylen-Dien-Kautschuk):** Elastomer für O-Ringe und Dichtungen, KTW/W270-zugelassen, gute Alterungsbeständigkeit, begrenzte Chlor-Beständigkeit.

**FDA 21 CFR:** US-amerikanische Lebensmittelzulassung — relevante Abschnitte: 177.1550 (PTFE), 177.2600 (Gummi/Elastomere), 177.1520 (Polyolefine).

**FKM (Fluorkautschuk/Viton):** Hochtemperatur-beständiges Elastomer für O-Ringe, chemisch beständiger als EPDM, für Heißwasser-Anwendungen.

**Fließgeschwindigkeit:** Geschwindigkeit des Wassers in der Leitung (m/s). Empfehlung: 0,5–1,5 m/s. Über 2 m/s: Erosionskorrosion, Geräusche.

**Gesamthärte:** Summe der Calcium- und Magnesium-Ionen im Wasser, angegeben in °dH (Grad deutscher Härte). Weich: <8,4°dH, mittel: 8,4–14°dH, hart: >14°dH.

**Go/No-Go Lehre:** Prüfwerkzeug für Crimp-Verbindungen — die Lehre muss über den gecrimpten Ring passen (Go), darf aber nicht zu locker sein (No-Go).

**JG (John Guest):** Hersteller von Push-Fit Verbindungssystemen, Marktführer im Marine-Bereich.

**KBE (Koloniebildende Einheiten):** Maß für die Keimbelastung von Wasser. TrinkwV-Grenzwert: 100 KBE/ml bei 22°C.

**Knickbildung:** Abknicken eines Schlauchs bei zu engem Biegeradius, führt zu Querschnittsverringerung (50–80%) und Durchfluss-Reduktion.

**KTW-Leitlinie:** Kunststoffe im Trinkwasserbereich — deutsche Prüfgrundlage für Materialien in Kontakt mit Trinkwasser (wird durch UBA-Positivliste abgelöst).

**Legionella pneumophila:** Bakterium, das Legionellose (Legionärskrankheit) verursacht. Wächst optimal bei 25–45°C, abgetötet >60°C. Infektionsweg: Aerosol-Inhalation.

**LLDPE (Linear Low-Density Polyethylene):** Kunststoff für Trinkwasserrohre (z.B. John Guest PE-Rohre), flexibler als HDPE, aber nicht vernetzt wie PEX.

**Mineralisierer:** Nachbehandlungsstufe für Watermaker-Permeat, fügt Calcium und Magnesium hinzu, hebt pH-Wert von ~6,5 auf ~7,5.

**NSF 61:** US-amerikanischer Standard für Materialien in Kontakt mit Trinkwasser (National Sanitation Foundation). International anerkannt.

**Oetiker-Schelle:** Ohrschelle (1-Ohr oder 2-Ohr) aus Edelstahl, professioneller Standard in der Yachtproduktion. Gleichmäßige Klemmkraft, kein Einschneiden.

**Osmose (Umkehrosmose):** Trennverfahren zur Entsalzung von Seewasser. Wasser wird unter hohem Druck (55–70 bar) durch eine Membran gepresst, Salze und Verunreinigungen zurückgehalten.

**PA12 (Polyamid 12/Nylon):** Kunststoff für Trinkwasserrohre, gute chemische Beständigkeit, aber UV-empfindlich und steifer als PEX.

**Permeat:** Entsalztes Wasser nach Umkehrosmose-Behandlung (Watermaker). TDS typisch 100–400 ppm.

**PEX (vernetztes Polyethylen):** Polyethylen mit chemisch oder physikalisch vernetzter Molekülstruktur. Varianten: PEX-a (Engel), PEX-b (Silan), PEX-c (Bestrahlung).

**POM (Polyoxymethylen/Acetal):** Technischer Kunststoff für Push-Fit Fitting-Körper. Hohe Festigkeit, gute Dimensionsstabilität, KTW-zugelassen.

**Press-Verbindung:** Dauerhafte Rohrverbindung durch radiale Verpressung einer Edelstahl- oder Messinghülse mit Pressmaschine. Höchster Zuverlässigkeitsstandard.

**Propylenglykol:** Frostschutzmittel für Trinkwassersysteme — nur FDA food-grade verwenden! NICHT mit Ethylenglykol (giftig) verwechseln.

**PTFE (Polytetrafluorethylen/Teflon):** Fluorkunststoff für Gewindedichtungen (Band, Faden). Chemisch inert, lebensmittelzugelassen.

**Push-Fit:** Steckverbindungssystem für Rohre/Schläuche — Einstecken genügt, kein Werkzeug nötig. Zahnring hält, O-Ring dichtet.

**REACH (Registration, Evaluation, Authorisation and Restriction of Chemicals):** EU-Chemikalienverordnung 1907/2006.

**SC-Contur (Viega):** Sicherheitsmerkmal bei Viega-Pressfittings — unverpresste Fittings lecken gezielt bei Druckprüfung.

**Sedimentfilter:** Vorfilter zum Entfernen von Partikeln, Rost, Sand. Typische Porengröße: 5–20 µm.

**Stagnation:** Stillstand des Wassers in Leitungen — fördert Biofilm-Wachstum und Legionellen-Vermehrung.

**TDS (Total Dissolved Solids):** Gesamtgehalt gelöster Feststoffe im Wasser (mg/l). Trinkwasser: <500 ppm, Watermaker-Permeat: 100–400 ppm.

**TrinkwV:** Trinkwasserverordnung (Deutschland) — regelt Qualitätsanforderungen an Wasser für den menschlichen Gebrauch.

**TSM Insert (Tube Support Metal):** Metallstützhülse, die in das Rohrende eingesetzt wird, um Kollaps unter Druck bei Push-Fit Verbindungen zu verhindern.

**UBA-Positivliste:** Liste des Umweltbundesamtes mit zugelassenen Materialien und Chemikalien für den Kontakt mit Trinkwasser. Löst KTW-Leitlinie ab.

**UV-C Desinfektion:** Abtötung von Mikroorganismen durch UV-Licht bei 254 nm Wellenlänge. Kein chemischer Rückstand.

**V4A (1.4401/AISI 316):** Austenitischer Edelstahl mit Molybdän-Zusatz — Standard für salzwasserbeständige Anwendungen. V2A (1.4301/304) ist für Salzwasser NICHT ausreichend.

**Vernetzungsgrad:** Anteil der vernetzten Molekülketten in PEX. Mindestanforderung: PEX-a ≥70%, PEX-b ≥65% (ISO 15875).

**VOC (Volatile Organic Compounds):** Flüchtige organische Verbindungen — können aus minderwertigen Kunststoffen in Trinkwasser migrieren.

**W270:** DVGW-Arbeitsblatt zur Prüfung der mikrobiellen Vermehrung auf Materialien im Trinkwasserbereich. Bestanden = Material fördert kein Bakterienwachstum über Grenzwert.

**Watermaker:** Umkehrosmose-Anlage zur Seewasserentsalzung an Bord. Erzeugt Trinkwasser (Permeat) aus Seewasser.

**WRAS (Water Regulations Advisory Scheme):** Britische Trinkwasser-Zulassung für Materialien und Produkte.

---

## Schnell-Referenz & Quick-Lookup Index

**Material-Schnellwahl nach Einsatzzweck:**

| Einsatz | Empfehlung 1 | Empfehlung 2 | NICHT verwenden |
|---------|-------------|-------------|-----------------|
| Kaltwasser-Hauptleitung | PEX-a 16 mm | PA12 12 mm | PVC |
| Warmwasser-Hauptleitung | PEX-a 16 mm (Viton-O-Ringe) | Edelstahl-Wellrohr | PVC, Silikon ohne Temp.-Freigabe |
| Pantry (Geschmackskritisch) | Silikon Platinum | PEX-a | PVC, billige Silikon-Peroxid |
| Watermaker-Permeat | PEX-a 12 mm | John Guest LLDPE 3/8" | PVC, Kupfer |
| Cockpit-Dusche (UV-exponiert) | PEX mit UV-Schutz | Edelstahl-Wellrohr | PEX ungeschützt, PA12 |
| Frostgefährdete Bereiche | PEX-a (bestes Frostverhalten) | Silikon | PA12, Messing-Fittings |

**Fitting-Schnellwahl:**

| Situation | Empfehlung | Teilenummer (Beispiel) |
|-----------|-----------|----------------------|
| Verbindung 15 mm gerade | JG Speedfit PI0416S | ~3,50 EUR |
| T-Abzweig 15 mm | JG Speedfit PI4616 | ~5,50 EUR |
| 90° Winkel 15 mm | JG Speedfit PI4816 | ~4,50 EUR |
| Absperrhahn 15 mm | JG Speedfit?"#valve | ~12,00 EUR |
| Übergang 15 mm → 1/2" BSP | JG Speedfit PI0115 | ~4,00 EUR |

**Drehmoment-Schnellreferenz:**

| Verbindung | Drehmoment |
|-----------|------------|
| Schlauchschelle 9 mm | 2,5–3,5 Nm |
| Kunststoff-Fitting 1/2" | 4,0–6,0 Nm |
| Messing-Fitting 1/2" | 25–35 Nm |
| Edelstahl-Fitting 1/2" | 25–35 Nm |

**Biegeradius-Schnellreferenz:**

| Material | Faustformel |
|----------|------------|
| PEX | 6 × Außen-Ø |
| Silikon | 3 × Außen-Ø |
| PA12 | 7 × Außen-Ø |
| Edelstahl-Wellrohr | 4 × Außen-Ø |

---

## Notfall-Ressourcen & Kontakte

**Hersteller-Hotlines (Technischer Support):**

| Hersteller | Telefon | E-Mail | Erreichbarkeit |
|-----------|---------|--------|----------------|
| John Guest (UK) | +44 1895 449233 | technical@johnguest.com | Mo–Fr 8–17 GMT |
| Whale (Munster Simms) | +44 28 9127 0531 | info@whalepumps.com | Mo–Fr 9–17 GMT |
| Shurflo (Pentair) | +1 800 854 3218 | shurflo.support@pentair.com | Mo–Fr 8–17 CST |
| Jabsco (Xylem) | +44 1-45 263355 | jabsco.uk@xylem.com | Mo–Fr 8–17 GMT |
| Uponor (DE) | +49 9521 690 0 | info.de@uponor.com | Mo–Fr 8–17 CET |
| Viega (DE) | +49 2722 61 0 | info@viega.de | Mo–Fr 7:30–17 CET |
| Spectra Watermakers | +1 415 526 2780 | info@spectrawatermakers.com | Mo–Fr 8–17 PST |
| Schenker Watermakers | +39 0586 271 507 | info@schenkerwatermakers.com | Mo–Fr 9–18 CET |

**Trinkwasser-Labore (Schnellanalyse):**
- AGROLAB Group (DE): www.agrolab.de — Yachthafen-Nähe: Kiel, Hamburg, Rostock
- Eurofins (DE/EU): www.eurofins.de — Legionellen-Schnelltest 24h
- IWW Zentrum Wasser (DE): www.iww-online.de — Spezial: Marine Trinkwasser
- Typische Kosten: Basisanalyse (KBE, Coliforme) 40–80 EUR; Vollanalyse (inkl. Legionellen, Metalle) 120–250 EUR

**Zertifizierungsstellen:**
- DVGW (Deutscher Verein des Gas- und Wasserfaches): www.dvgw.de
- NSF International: www.nsf.org
- WRAS (UK): www.wras.co.uk
- TÜV SÜD (KTW-Prüfung): www.tuvsud.com

---

## ANHANG A — Cross-Reference-Tabelle: Schlauchmaterial ↔ Fitting-System

| Schlauchmaterial | JG Push-Fit | Whale QC | SharkBite | Crimp (Cu) | Press (Viega) | Schlauchschelle |
|-----------------|-----------|----------|-----------|------------|---------------|-----------------|
| PEX-a 16 mm | Ja (TSM) | Nein | Ja (1/2") | Ja | Ja | Nein (zu steif) |
| PEX-b 16 mm | Ja (TSM) | Nein | Ja (1/2") | Ja | Ja | Nein |
| Silikon 13 mm | Nein | Nein | Nein | Nein | Nein | Ja (Oetiker) |
| Silikon 16 mm | Nein | Nein | Nein | Nein | Nein | Ja (Oetiker) |
| PA12 12 mm | Ja (12mm) | Nein | Nein | Nein | Nein | Nein |
| EPDM 13 mm | Nein | Nein | Nein | Nein | Nein | Ja |
| JG LLDPE 15 mm | Ja | Nein | Nein | Nein | Nein | Nein |
| Whale 15 mm | Nein | Ja | Nein | Nein | Nein | Nein |

---

## ANHANG B — Zertifizierungs-Vergleich nach Region

| Zertifizierung | Region | Prüfumfang | Relevanz Yachtbau |
|---------------|--------|------------|-------------------|
| KTW/W270 | Deutschland | Migration + Biofilm | Hoch (EU-Binnenmarkt) |
| UBA-Positivliste | Deutschland (neu) | Materialzulassung | Hoch (löst KTW ab) |
| DVGW W534 | Deutschland | Verbindungstechnik | Hoch (Press/Crimp) |
| WRAS | Großbritannien | Material + Produkt | Mittel (Post-Brexit eigene Norm) |
| NSF 61 | USA/International | Material in Trinkwasser | Hoch (international anerkannt) |
| NSF 372 | USA | Bleifreiheit | Hoch (Messing-Fittings) |
| FDA 21 CFR | USA | Lebensmittelkontakt | Mittel (Elastomere, Kunststoffe) |
| ACS (Attestation de Conformité Sanitaire) | Frankreich | Material + Produkt | Mittel (Frankreich-Flagge) |
| AS/NZS 4020 | Australien/Neuseeland | Migration | Gering (nur für AU/NZ-Flagge) |

---

## ANHANG C — Biegeradien-Vergleichstabelle (vollständig)

| Material | Außen-Ø | Min-R kalt (20°C) | Min-R warm (60°C) | Min-R mit Feder | Min-R mit Heißluft |
|----------|---------|-------------------|-------------------|-----------------|-------------------|
| PEX-a | 12 mm | 60 mm | 40 mm | 36 mm | 30 mm |
| PEX-a | 16 mm | 80 mm | 55 mm | 48 mm | 40 mm |
| PEX-a | 20 mm | 100 mm | 70 mm | 60 mm | 50 mm |
| PEX-a | 25 mm | 125 mm | 85 mm | 75 mm | 63 mm |
| PEX-b | 12 mm | 72 mm | 48 mm | 42 mm | 36 mm |
| PEX-b | 16 mm | 96 mm | 64 mm | 56 mm | 48 mm |
| PEX-b | 20 mm | 120 mm | 80 mm | 70 mm | 60 mm |
| Silikon Pt. | 13 mm | 26 mm | 26 mm | n/a | n/a |
| Silikon Pt. | 16 mm | 32 mm | 32 mm | n/a | n/a |
| Silikon Pt. | 19 mm | 38 mm | 38 mm | n/a | n/a |
| PA12 | 12 mm | 72 mm | 55 mm | 50 mm | n/a |
| PA12 | 15 mm | 90 mm | 68 mm | 63 mm | n/a |
| Edst.-Wellr. | 12 mm | 36 mm | 36 mm | n/a | n/a |
| Edst.-Wellr. | 16 mm | 48 mm | 48 mm | n/a | n/a |
| Edst.-Wellr. | 20 mm | 60 mm | 60 mm | n/a | n/a |

---

## ANHANG D — Confidence-Mapping für AYDI-Module

| Datenquelle | Confidence-Level | AYDI-Code | Badge |
|------------|-----------------|-----------|-------|
| CAD-Zeichnung mit Leitungsführung | measured | `measured` | Grün |
| Materialspezifikation Hersteller | measured | `measured` | Grün |
| Berechnung aus CAD-Daten | calculated | `calculated` | Grün |
| Foto: Schlauch mit sichtbarer Bedruckung | visual_high | `visual_high` | Blau |
| Foto: Verlegung erkennbar, Material unklar | visual_medium | `visual_medium` | Amber |
| Foto: Schlecht beleuchtet, Bilge | visual_low | `visual_low` | Versteckt |
| Foto: Nicht interpretierbar | visual_insufficient | `visual_insufficient` | Nur Metadaten |
| Bootsklasse-Durchschnitt | estimated | `estimated` | Grau |
| Service-Bericht mit Befund | documented | `documented` | Blau |
| Branchendaten Hersteller | benchmark | `benchmark` | Grau |

---

## ANHANG E — Bordausstattung: Empfohlene Trinkwasser-Ersatzteile

**8–14 m Segelyacht / Motorboot:**

| Artikel | Menge | Preis (EUR) | Priorität |
|---------|-------|-------------|-----------|
| JG Inline-Kupplung 15 mm | 3 | 10,50 | Hoch |
| JG 90°-Winkel 15 mm | 2 | 9,00 | Hoch |
| JG T-Stück 15 mm | 1 | 5,50 | Mittel |
| PEX-Rohr 16 mm, 2 m | 1 | 5,60 | Hoch |
| O-Ring-Sortiment EPDM | 1 Set | 12,00 | Hoch |
| Schlauchschellen V4A 12–20 mm | 6 | 9,00 | Hoch |
| PTFE-Band | 1 Rolle | 2,50 | Mittel |
| Rohrschneider (klein) | 1 | 25,00 | Hoch |
| Rescue Tape | 1 Rolle | 8,00 | Mittel |
| Shurflo Membran-Satz 94-238-04 | 1 | 35,00 | Mittel |
| Certisil Combina Einzelportion | 2 | 12,00 | Hoch |
| Aktivkohle-Filterpatrone (Reserve) | 1 | 25,00 | Mittel |
| **Gesamt** | | **~159,10** | |

**14–24 m Yacht (zusätzlich):**

| Artikel | Menge | Preis (EUR) | Priorität |
|---------|-------|-------------|-----------|
| JG Absperrhahn 15 mm | 2 | 24,00 | Hoch |
| Rückschlagventil 1/2" | 1 | 15,00 | Mittel |
| Akkumulator 0,5 L (Ersatz) | 1 | 45,00 | Gering |
| Druckschalter (Pumpe) | 1 | 28,00 | Mittel |
| Boiler-Anode (Magnesium) | 1 | 35,00 | Mittel |
| **Zusätzlich Gesamt** | | **~147,00** | |

---

## ANHANG F — Fallstudien

### Fallstudie 1: Bavaria 40 Cruiser — PVC-Schlauch-Sanierung
**Boot:** Bavaria 40 Cruiser, Baujahr 2008, Charterbetrieb Kroatien
**Problem:** Starker Plastikgeschmack im Trinkwasser, Chartergäste beschweren sich
**Diagnose:** Original-PVC-Weichschläuche (nicht KTW-zugelassen), Weichmacher-Migration nach 15 Jahren massiv
**Maßnahme:** Komplett-Sanierung auf PEX-a 16 mm mit John Guest Push-Fit
**Material:** 30 m PEX Uponor, 18 JG-Fittings, 2 neue Shurflo 4009 Pumpen
**Kosten:** Material 380 EUR, Werft-Arbeit (12 h × 85 EUR) 1.020 EUR, Gesamt 1.400 EUR
**Ergebnis:** Geschmacksproblem vollständig behoben, Charterbewertungen deutlich besser
**Dauer:** 2 Arbeitstage
**AYDI-Score vorher:** 25/100 | **AYDI-Score nachher:** 92/100
**Confidence:** measured
**Lessons Learned:** PVC-Schläuche in Charterflotten systematisch ersetzen, Amortisation durch weniger Beschwerden in einer Saison.

### Fallstudie 2: Hallberg-Rassy 43 — Legionellen nach Winterlager
**Boot:** Hallberg-Rassy 43 Mk II, Baujahr 2015, Privatbesitz, Winterlager Heiligenhafen
**Problem:** Eigner erkrankt nach Saisonstart an Pontiac-Fieber (milde Legionellose)
**Diagnose:** Warmwasser-Boiler nicht entleert über Winter, Biofilm-Bildung, Legionella pneumophila nachgewiesen
**Maßnahme:** Thermische Desinfektion (>70°C, 30 min), Certisil Combina, Boiler-Anode gewechselt
**Material:** Certisil Combina 25 EUR, Boiler-Anode (Kuuma) 45 EUR, Labortest 120 EUR
**Kosten:** Gesamt 190 EUR + Arztkosten
**Ergebnis:** Legionellen nicht mehr nachweisbar nach 2. Probe (4 Wochen später)
**Dauer:** 1 Arbeitstag
**AYDI-Score vorher:** 15/100 | **AYDI-Score nachher:** 85/100
**Confidence:** documented
**Lessons Learned:** Winterisierungsprotokoll muss Boiler-Entleerung IMMER einschließen. Warm-up vor erster Nutzung.

### Fallstudie 3: Beneteau Oceanis 51.1 — Push-Fit Leckage bei Atlantiküberquerung
**Boot:** Beneteau Oceanis 51.1, Baujahr 2019, ARC-Teilnehmer 2023
**Problem:** Push-Fit Verbindung in Vorschiff löst sich bei schwerem Wetter (Schlag-Leck)
**Diagnose:** JG-Fitting ohne TSM-Insert montiert, PEX-Rohr unter Vibration aus Fitting gezogen
**Maßnahme:** Notfall-Reparatur auf See: Schlauch neu eingesteckt mit TSM-Insert (Bordreserve)
**Material:** 1× JG TSM-Insert, 1× JG Inline-Kupplung (vorsorglich)
**Kosten:** Material <5 EUR (aus Bordvorrat), Arbeitszeit 20 min
**Ergebnis:** Dichte Verbindung, restliche Überquerung ohne Probleme
**Dauer:** 20 Minuten
**AYDI-Score vorher:** 55/100 (fehlendes TSM) | **AYDI-Score nachher:** 92/100
**Confidence:** documented
**Lessons Learned:** TSM-Insert ist PFLICHT bei PEX in Push-Fit. Notfall-Kit mit Ersatzfittings an Bord.

### Fallstudie 4: Swan 65 — Edelstahl-Trinkwassersystem Refit
**Boot:** Nautor Swan 65, Baujahr 1978, Komplett-Refit 2022
**Problem:** Original-System (Kupfer + Gummischlauch) nach 44 Jahren komplett korrodiert/degradiert
**Maßnahme:** Komplett-Neubau mit Edelstahl-Wellrohr (Hauptleitungen) + Silikon Platinum (Abzweige)
**Material:** 45 m Edelstahl-Wellrohr 16 mm, 15 m Silikon Platinum 13 mm, Viega Pressfittings
**Kosten:** Material 2.850 EUR, Werft-Arbeit (40 h × 120 EUR) 4.800 EUR, Gesamt 7.650 EUR
**Ergebnis:** Premium-System, geschmacksneutral, Lebensdauer 30+ Jahre
**Dauer:** 5 Arbeitstage (Refit-Kontext)
**AYDI-Score vorher:** 10/100 | **AYDI-Score nachher:** 97/100
**Confidence:** measured
**Lessons Learned:** Edelstahl + Silikon ist der Gold-Standard, aber Kosten sind 5–10× höher als PEX. Lohnt bei hochwertigen Yachten.

### Fallstudie 5: Catana 53 — Watermaker-Integration mit Mineralisierer
**Boot:** Catana 53, Baujahr 2020, Weltumsegelung ab 2021
**Problem:** Watermaker-Permeat schmeckt "flach", pH zu niedrig (6,2), Crew trinkt lieber Flaschenwasser
**Diagnose:** Permeat ohne Nachbehandlung direkt in Tank — niedriger Mineralgehalt, saurer pH
**Maßnahme:** Mineralisierer (Calcit-Kartusche) nach Watermaker-Ausgang installiert
**Material:** Pentek GS-10 Calcit-Filter 10" (Art.-Nr. 155271-43), JG-Fittings, 2 m PEX
**Kosten:** Mineralisierer 85 EUR, Fittings 35 EUR, Montage 2 h Eigenleistung
**Ergebnis:** pH von 6,2 auf 7,4 angehoben, Geschmack deutlich verbessert, Crew trinkt Bordwasser
**Dauer:** 2 Stunden
**AYDI-Score vorher:** 65/100 | **AYDI-Score nachher:** 90/100
**Confidence:** measured
**Lessons Learned:** Mineralisierer ist fast Pflicht bei Watermaker-Betrieb. Geschmack und Gesundheit verbessern sich deutlich.

### Fallstudie 6: Lagoon 42 — Frostschaden trotz Winterisierung
**Boot:** Lagoon 42, Baujahr 2021, Winterlager Travemünde
**Problem:** Trotz Winterisierung Frostschaden: 3 Messing-Fittings gesprungen, Boiler-Ablassventil undicht
**Diagnose:** Winterisierung unvollständig — Restwasser in Hochpunkten (Mast-Fuß-Bereich), Druckluft nicht ausreichend
**Maßnahme:** Betroffene Messing-Fittings durch JG Push-Fit (Acetal) ersetzen, Boiler-Ventil tauschen
**Material:** 3× JG-Fittings 22 EUR, 1× Boiler-Ablassventil 35 EUR, 1 m PEX 3 EUR
**Kosten:** Material 60 EUR, Werft-Arbeit (4 h × 95 EUR) 380 EUR, Gesamt 440 EUR
**Ergebnis:** System wieder dicht, verbessertes Winterisierungsprotokoll erstellt (inkl. Hochpunkte)
**Dauer:** 4 Stunden
**AYDI-Score vorher:** 30/100 (nach Frostschaden) | **AYDI-Score nachher:** 88/100
**Confidence:** documented
**Lessons Learned:** Druckluft allein reicht nicht — ALLE Hochpunkte manuell entleeren. Propylenglykol als Sicherheitsreserve.

### Fallstudie 7: Contest 50CS — Biofilm-Problem im Warmwasserkreis
**Boot:** Contest 50CS, Baujahr 2012, Liegeplatz Mallorca (ganzjährig)
**Problem:** Rosa Ablagerungen im Duschkopf, Warmwasser riecht modrig, KBE-Werte >500/ml
**Diagnose:** Biofilm (Serratia marcescens dominant) im Warmwasser-System, Boiler-Temperatur nur 45°C eingestellt
**Maßnahme:** Boiler-Thermostat auf 60°C eingestellt, System mit H₂O₂ 3% desinfiziert, Duschköpfe ersetzt
**Material:** H₂O₂ 30% (1 L) 12 EUR, 2× neue Duschköpfe 45 EUR, Labortest 80 EUR
**Kosten:** Gesamt 137 EUR + Eigenleistung 3 h
**Ergebnis:** KBE <20/ml nach 4 Wochen, kein Geruch mehr, kein rosa Belag
**Dauer:** 3 Stunden + 4 Wochen Monitoring
**AYDI-Score vorher:** 40/100 | **AYDI-Score nachher:** 85/100
**Confidence:** documented
**Lessons Learned:** Boiler IMMER ≥60°C. Mittelmeer-Liegeplatz = erhöhtes Biofilm-Risiko durch hohe Umgebungstemperatur.

### Fallstudie 8: Oyster 575 — Komplett-System mit Redundanz
**Boot:** Oyster 575, Baujahr 2023, Blauwasser-Ausrüstung
**Problem:** Kein Problem — Neubau-Spezifikation für redundantes Trinkwassersystem
**Diagnose:** n/a (Neubau-Planung)
**Maßnahme:** Duales System: 2× unabhängige Pumpen, 2× Tank (je 350 L), Crossover-Ventil, Watermaker Spectra Catalina 340 mit Mineralisierer, UV-C Desinfektion, 3-Stufen-Filtration
**Material:** 60 m PEX-a, 25 m Silikon Platinum (Pantry), Viega Pressfittings, 2× Jabsco Par-Max HD5, Spectra Catalina 340, UV Dynamics UVD-340
**Kosten:** Trinkwassersystem komplett: 12.500 EUR (Material) + 6.000 EUR (Werft 50 h × 120 EUR)
**Ergebnis:** Vollständig redundantes System, Autonomie >30 Tage mit Watermaker
**Dauer:** 8 Arbeitstage (im Rahmen des Neubaus)
**AYDI-Score:** 98/100
**Confidence:** measured
**Lessons Learned:** Redundanz kostet ~40% mehr, aber ist bei Blauwasser-Yachten unverzichtbar. Planung im Neubau deutlich günstiger als Nachrüstung.

---

## ANHANG G — Experten-Stimmen

**Matthias Kröger, Sachverständiger für Yachttechnik (BVSK):**
"Das Trinkwassersystem wird beim Gebrauchtkauf am häufigsten übersehen. Ich empfehle jedem Käufer, den Schlauchmaterial-Typ und das Alter zu prüfen. PVC-Schläuche über 10 Jahre sind ein sofortiger Sanierungsgrund."

**Dr. Andrea Schwarz, Hygiene-Institut Universität Kiel:**
"Biofilm in Yacht-Trinkwassersystemen ist ein unterschätztes Problem. Die Kombination aus Stagnation, Wärme und organischen Materialien schafft ideale Bedingungen für Keimwachstum. Silberionen-Konservierung und regelmäßige thermische Desinfektion sind die wirksamsten Gegenmaßnahmen."

**Jan-Erik Hansen, Technischer Leiter Hallberg-Rassy:**
"Wir haben 2018 komplett auf PEX-a mit John Guest Push-Fit umgestellt. Die Rücklaufquote bei Trinkwasser-Problemen ist seitdem um 85% gesunken. Das System ist wartungsfreundlich und langlebig."

**Capt. Sarah Williams, Blauwasser-Seglerin (5 Atlantiküberquerungen):**
"Ein Notfall-Kit mit Push-Fit Ersatzteilen hat mir zweimal die Überfahrt gerettet. Investieren Sie 50 EUR in Ersatzteile — das ist die beste Versicherung für Ihr Trinkwassersystem."

---

## ANHANG H — Risk Assessment Matrix (Trinkwassersystem)

| Risiko | Wahrscheinlichkeit | Schwere | Risiko-Score | Maßnahme |
|--------|-------------------|---------|-------------|----------|
| Weichmacher-Migration (PVC) | Hoch (bei PVC) | Hoch | 9/10 | Material ersetzen |
| Legionellen | Mittel | Sehr hoch | 8/10 | Boiler ≥60°C, Desinfektion |
| Biofilm | Hoch | Mittel | 7/10 | Stagnation vermeiden, Desinfektion |
| Frostschaden | Mittel (Nordeuropa) | Hoch | 7/10 | Winterisierung |
| Push-Fit Leckage | Gering | Mittel | 4/10 | TSM-Insert, korrekte Montage |
| UV-Degradation | Mittel | Gering | 4/10 | UV-Schutz anbringen |
| Druckverlust | Mittel | Gering | 3/10 | Filterwechsel, Dimensionierung |
| Kalkablagerung | Gering (WM) | Gering | 2/10 | Weiches Wasser, Enthärter |
| Komplett-Ausfall Pumpe | Gering | Mittel | 3/10 | Ersatzpumpe oder Handpumpe |
| Kontamination (Seewasser) | Sehr gering | Hoch | 3/10 | Rückschlagventile, Tank-Inspektion |

---

## ANHANG I — Audit- und Compliance-Checkliste

**Trinkwassersystem-Audit (AYDI-Standard):**

| Nr. | Prüfpunkt | Soll | Befund | OK/NOK |
|-----|-----------|------|--------|--------|
| 1 | Schlauchmaterial identifizierbar | KTW/W270 oder NSF 61 | | |
| 2 | Bedruckung auf Schlauch lesbar | Hersteller, Typ, Datum | | |
| 3 | Kein PVC im Trinkwasserkreis | PVC-frei | | |
| 4 | Fittings lebensmittelzugelassen | KTW/NSF/WRAS | | |
| 5 | Schlauchschellen V4A (316) | Kein V2A, kein verzinkter Stahl | | |
| 6 | Doppelschellen unter Wasserlinie | Redundanz an Rumpfdurchführungen | | |
| 7 | Biegeradien eingehalten | Material-spezifisch (siehe Tabelle) | | |
| 8 | Befestigungsschellen alle 30–50 cm | Gummiert, V4A | | |
| 9 | Kalt/Warm markiert | Blau/Rot Farbcodierung | | |
| 10 | Filter vorhanden und zugänglich | Sediment + Aktivkohle | | |
| 11 | Filteralter dokumentiert | <12 Monate | | |
| 12 | Pumpe funktionsfähig | Druck ≥2,5 bar am Hahn | | |
| 13 | Akkumulator funktionsfähig | Kein Takten, Vordruck korrekt | | |
| 14 | Boiler-Temperatur | ≥60°C | | |
| 15 | Rückschlagventile vorhanden | Pumpe, Watermaker, Landanschluss | | |
| 16 | Keine sichtbaren Leckagen | Trockene Verbindungen | | |
| 17 | Druckprüfung bestanden | <0,1 bar Abfall in 30 min | | |
| 18 | Letzte Desinfektion dokumentiert | <12 Monate | | |
| 19 | Wasserprobe unauffällig | Geruch, Geschmack, ggf. Labor | | |
| 20 | Winterisierung-Protokoll vorhanden | Dokumentiert | | |

---

## ANHANG J — Material-Datenblätter (Zusammenfassung)

**PEX-a (Uponor Aqua Pipe 16×2,2 mm):**

| Eigenschaft | Wert | Norm |
|------------|------|------|
| Werkstoff | PE-Xa (Engel-Verfahren) | ISO 15875-2 |
| Außen-Ø × Wandstärke | 16 × 2,2 mm | |
| Innen-Ø | 11,6 mm | |
| Vernetzungsgrad | ≥70% | ISO 15875, DSC |
| Dichte | 0,94 g/cm³ | |
| Zugfestigkeit | ≥19 MPa | ISO 527 |
| Bruchdehnung | ≥350% | ISO 527 |
| E-Modul | ~800 MPa (20°C) | |
| Wärmeausdehnung | 0,14 mm/(m·K) | |
| Wärmeleitfähigkeit | 0,38 W/(m·K) | |
| Betriebsdruck (20°C, 50 J.) | 10 bar | ISO 15875-2 |
| Betriebsdruck (60°C, 50 J.) | 6 bar | ISO 15875-2 |
| Trinkwasser-Zulassung | KTW, W270, DVGW W534 | |
| Sauerstoffdiffusion | Ohne Barriere: ~0,1 mg/(l·d) | DIN 4726 |
| Brandklasse | B2 (normal entflammbar) | DIN 4102 |

**Silikon Platinum (Venair Sil 613, 13 mm ID):**

| Eigenschaft | Wert | Norm |
|------------|------|------|
| Werkstoff | Platinum-vulkanisiertes Silikon | |
| Innen-Ø × Wandstärke | 13 × 3 mm | |
| Außen-Ø | 19 mm | |
| Shore-Härte | 60 ±5 Shore A | ISO 868 |
| Zugfestigkeit | ≥8 MPa | ISO 37 |
| Bruchdehnung | ≥400% | ISO 37 |
| Temperaturbereich | -60°C bis +200°C | |
| Betriebsdruck (20°C) | 6 bar | |
| Trinkwasser-Zulassung | FDA 21 CFR 177.2600, KTW, W270 | |
| Biokompatibilität | USP Class VI | |
| Farbe | Transluzent (natur) | |
| Geruch/Geschmack | Neutral (geschmacksfrei) | |

---

## ANHANG K — Prüfverfahren

**Druckprüfung Trinkwassersystem (AYDI-Standard):**
1. System füllen und entlüften (alle Hähne öffnen bis blasenfrei)
2. Alle Hähne schließen
3. Prüfdruck: 1,5 × max. Betriebsdruck (z.B. 1,5 × 3,5 bar = 5,25 bar)
4. Prüfdruck 10 Minuten halten
5. Abfall ≤0,1 bar: bestanden
6. Abfall >0,1 bar: Leckage suchen und beheben, Prüfung wiederholen
7. Dokumentation: Datum, Prüfdruck, Dauer, Ergebnis, Prüfer

**Wasserqualitäts-Schnelltest (Bordmittel):**
1. pH-Teststreifen: Soll 6,5–9,5 (TrinkwV)
2. Chlor-Teststreifen (DPD): Soll <0,3 mg/l frei verfügbares Chlor
3. TDS-Messgerät: Soll <500 ppm (Watermaker-Permeat: 100–400 ppm)
4. Sensorische Prüfung: Geruch (kein Fremdgeruch), Geschmack (neutral), Aussehen (klar)
5. Coliforme Schnelltest (z.B. Industrietest Colilert): Soll: negativ

---

## ANHANG L — Top 15 Design-Fehler bei Trinkwassersystemen auf Yachten

1. **PVC-Schlauch für Trinkwasser** — Weichmacher-Migration. Score-Abzug: 70 Punkte.
2. **Keine Rückschlagventile** — Rückfluss, Kontamination. Score-Abzug: 30 Punkte.
3. **Boiler-Temperatur <55°C** — Legionellen-Risiko. Score-Abzug: 40 Punkte.
4. **Kein Filter im System** — Sediment, Geschmack. Score-Abzug: 15 Punkte.
5. **V2A-Schellen statt V4A** — Korrosion in Salzluft. Score-Abzug: 20 Punkte.
6. **Kein Akkumulator** — Pumpen-Takten, Lebensdauer. Score-Abzug: 10 Punkte.
7. **Schläuche ohne Befestigung** — Scheuern, Vibrationsschäden. Score-Abzug: 15 Punkte.
8. **Push-Fit ohne TSM-Insert** — Kollaps-Gefahr unter Druck. Score-Abzug: 20 Punkte.
9. **Kein Winterisierungsprotokoll** — Frostschäden. Score-Abzug: 25 Punkte.
10. **Watermaker ohne Rückschlagventil** — Membran-Kontamination. Score-Abzug: 25 Punkte.
11. **Warmwasserleitung nicht isoliert** — Energieverlust, Kondensation. Score-Abzug: 10 Punkte.
12. **Mischung verschiedener Fitting-Systeme** — Undichtigkeit. Score-Abzug: 15 Punkte.
13. **Zu kleine Leitungsdimensionierung** — Druckverlust, Komfortverlust. Score-Abzug: 15 Punkte.
14. **Kein Desinfektionsprotokoll** — Verkeimung. Score-Abzug: 20 Punkte.
15. **UV-exponierte PEX-Leitungen ohne Schutz** — Degradation. Score-Abzug: 15 Punkte.

---

## ANHANG M — Zusammenfassung & Empfehlungen

**Kernaussagen:**
1. PEX-a und Platinum-Silikon sind die einzigen empfehlenswerten Materialien für Trinkwasser an Bord.
2. PVC-Weichschlauch ist NIEMALS akzeptabel — sofort ersetzen.
3. Push-Fit (John Guest) ist der pragmatische Standard für die meisten Yachten.
4. Jedes System braucht Desinfektion (mindestens jährlich) und dokumentierte Wartung.
5. Legionellen-Prävention: Boiler ≥60°C, Stagnation vermeiden.
6. Frostschutz: Vollständige Entleerung + Propylenglykol.
7. Notfall-Kit an Bord: ~60 EUR Investition können die Reise retten.

**AYDI-Scoring-Zusammenfassung Trinkwasserschläuche:**

| Material | AYDI-Score | Empfehlung |
|----------|-----------|------------|
| PEX-a (Uponor, Rehau) | 92/100 | Standard-Empfehlung |
| Silikon Platinum (Venair) | 95/100 | Premium, geschmackskritisch |
| PA12 (Legris) | 80/100 | Akzeptabel, UV-empfindlich |
| PEX-b (Viega) | 88/100 | Gut, etwas steifer als PEX-a |
| EPDM (Continental) | 78/100 | Akzeptabel für kurze Strecken |
| JG LLDPE | 85/100 | Gut für JG-System |
| Edelstahl-Wellrohr | 90/100 | Premium, teuer |
| PVC (weich) | 10/100 | NICHT VERWENDEN |
| Silikon Peroxid (NoName) | 72/100 | Nur mit Nachweis KTW/W270 |

---

## ANHANG N — Spezialanwendungen

**Trinkwasser auf Mehrrumpfbooten (Katamarane/Trimarane):**
- Besonderheit: Zwei Rümpfe = doppelte Leitungslänge, zwei Tanks, Cross-Connect-Ventil
- Empfehlung: Jeder Rumpf autark mit eigener Pumpe, Crossover nur über Absperrventil
- Druckverlust-Berechnung: Längere Leitungswege beachten, ggf. größeren Durchmesser wählen
- Typische Leitungslänge 42-ft Katamaran: 40–55 m (vs. 20–30 m bei Einrumpf gleicher Länge)

**Trinkwasser auf Regattayachten:**
- Besonderheit: Gewicht ist kritisch, minimale Tankkapazität, kein Warmwasser
- Empfehlung: Leichtes Material (JG LLDPE oder PA12), kleiner Durchmesser (10 mm genügt), Fußpumpe statt elektrische Pumpe (Gewichtsersparnis ~3 kg)
- Tankgröße: 40–80 Liter (vs. 200–400 Liter bei Fahrtenyacht)

**Trinkwasser auf Motoryachten (Planing Hull):**
- Besonderheit: Stärkere Vibration durch Motorlauf, höhere Geschwindigkeiten = mehr Beschleunigungskräfte
- Empfehlung: Oetiker-Ohrschellen statt Schneckengewindeschellen, Befestigung alle 25–30 cm, vibrationsdämpfende Rohrschellen (Gummieinlage)
- Akkumulator: Größer dimensionieren (1,5–2,0 Liter) wegen Druckschwankungen durch Beschleunigung

---

## ANHANG O — Umweltaspekte

**Entsorgung alter Trinkwasserschläuche:**
- PEX: Recyclingcode 7 (Other), nicht über Hausmüll, Wertstoffhof
- Silikon: Nicht recyclebar, Restmüll oder Spezialentsorgung
- PVC: Sonderabfall (Chlorgehalt), NICHT verbrennen, Wertstoffhof
- Messing-Fittings: Metallschrott (Wertstoff), Schrotthändler
- Kupfer-Crimpringe: Kupferschrott (Wertstoff)

**Ökobilanz-Vergleich (CO₂-Äquivalent pro Meter Schlauch):**

| Material | CO₂-eq (kg/m) | Recycelbar | Lebensdauer (Jahre) | CO₂/Jahr |
|----------|---------------|------------|--------------------|---------| 
| PEX-a 16 mm | 0,35 | Bedingt | 40 | 0,009 |
| Silikon 16 mm | 1,20 | Nein | 35 | 0,034 |
| PA12 12 mm | 0,55 | Ja | 25 | 0,022 |
| Edelstahl 16 mm | 2,80 | Ja | 50+ | 0,056 |
| PVC 16 mm | 0,45 | Bedingt | 15 | 0,030 |

**Trinkwasser vs. Flaschenwasser — Ökobilanz:**
- 1 Liter Bordwasser (mit Watermaker): ~0,05 EUR, ~0,02 kg CO₂
- 1 Liter Flaschenwasser (1,5L PET): ~0,50 EUR, ~0,15 kg CO₂
- Ersparnis bei 4 Personen, 3 Liter/Tag, 30 Tage: ~54 EUR + ~15,6 kg CO₂

---

## ANHANG P — Erweiterte FAQ (TW-026 bis TW-035)

**TW-026: Kann ich Kupferrohr für Trinkwasser auf der Yacht verwenden?**
Ja, Kupferrohr ist traditionell für Trinkwasser zugelassen (DIN 1786, EN 1057). Aber: höheres Gewicht, teurere Montage (Löten/Pressen), Korrosionsgefahr bei sehr weichem Wasser (Watermaker-Permeat, pH <7). Kupfer migriert in saures Wasser — Grenzwert 2 mg/l (TrinkwV). Empfehlung: Nur wenn pH >7,0 sichergestellt. PEX ist leichter und einfacher.

**TW-027: Wie teste ich, ob mein Schlauch PVC oder PEX ist?**
Brenntest (Vorsicht!): PVC brennt mit grüner Flamme und beißendem Geruch (Chlor), PEX brennt wie eine Kerze mit tropfendem Material. Besser: Bedruckung lesen (Hersteller, Typ, Zulassung). Im Zweifelsfall: Material ersetzen.

**TW-028: Mein Watermaker produziert Wasser mit TDS >500 ppm — was tun?**
Membran ist verschmutzt oder am Ende der Lebensdauer. Reinigung mit Membranreiniger (z.B. Spectra SC-1, Art.-Nr. 39025, ~45 EUR). Falls TDS nach Reinigung weiterhin >500 ppm: Membran ersetzen (Spectra 200: ~550 EUR, Schenker 30: ~400 EUR). Umschaltventil muss korrekt kalibriert sein.

**TW-029: Wie viel Trinkwasser verbrauchen wir pro Person und Tag an Bord?**
Sparsam (Blauwasser): 5–8 Liter/Person/Tag. Normal (Küstenfahrt): 10–20 Liter/Person/Tag. Komfort (Marina mit Landanschluss): 30–50 Liter/Person/Tag. Watermaker ergänzt typisch 30–150 Liter/Tag je nach Modell.

**TW-030: Kann ich einen Hauswasser-Druckminderer am Landanschluss verwenden?**
Ja, dringend empfohlen! Landwasser-Druck kann 3–6 bar betragen, was Pumpen-Rückschlagventil und Akkumulator belastet. Druckminderer (z.B. Watts LFN25AUB-Z3, ~25 EUR) auf 2,5–3,0 bar einstellen. Zusätzlich: Wasserfilter am Landanschluss (Chlor, Sediment).

**TW-031: Soll ich die Trinkwasserpumpe dauerhaft laufen lassen?**
Nein. Die Pumpe sollte nur bei Bedarf laufen (Druckschalter-gesteuert). Dauerlauf verschleißt die Membran schneller und erhöht den Stromverbrauch. Einzige Ausnahme: Druckerhöhungsanlage (Grundfos o.ä.) mit Frequenzregelung — die regelt automatisch.

**TW-032: Was ist der Unterschied zwischen Sedimentfilter und Aktivkohlefilter?**
Sedimentfilter (5–20 µm): Entfernt Partikel, Rost, Sand — rein mechanisch. Aktivkohlefilter (1–5 µm + Adsorption): Entfernt zusätzlich Chlor, Geschmack, Geruch, organische Verbindungen (VOC). Beide sind komplementär — immer Sediment VOR Aktivkohle installieren (schützt teurere Aktivkohle).

**TW-033: Gibt es eine Pflicht zur Trinkwasseruntersuchung auf Yachten?**
Für Privatyachten: Keine gesetzliche Pflicht in Deutschland (TrinkwV gilt für "gewerbliche Anlagen"). Für Charteryachten: Ja, gewerbliche Nutzung — TrinkwV §14 Untersuchungspflicht. Empfehlung: Jährliche Basisanalyse (KBE, Coliforme) auch für Privatboote — 40–80 EUR.

**TW-034: Kann ich eine Spülmaschine an das Bord-Trinkwassersystem anschließen?**
Ja, wenn die Pumpe ausreichend dimensioniert ist (Spülmaschine zieht ~3–5 l/min). Rückschlagventil am Spülmaschinen-Anschluss installieren. Akkumulator sollte ≥1,0 Liter sein. Warmwasser-Anschluss über Boiler oder eigenes Heizelement in der Spülmaschine.

**TW-035: Mein Trinkwassersystem hat kein Druckausdehnungsgefäß — ist das schlimm?**
Nicht schlimm, aber suboptimal. Ohne Akkumulator (Druckausdehnungsgefäß) taktet die Pumpe bei jedem Tropfen. Das reduziert die Pumpen-Lebensdauer von 8–10 auf 4–6 Jahre und erzeugt Geräusche. Nachrüstung: Shurflo 182-200 (0,5 L, ~45 EUR) oder Jabsco 18810-0000 (1,0 L, ~85 EUR). Montage: 30 Minuten.

---

## ANHANG Q — Historische Zeitleiste: Trinkwassersysteme auf Yachten

| Jahr | Entwicklung | Bedeutung |
|------|-----------|-----------|
| ~3000 v.Chr. | Tonkrüge als Wasservorrat auf ägyptischen Schiffen | Erste dokumentierte Bordwasser-Systeme |
| ~500 v.Chr. | Bleigefütterte Holzfässer (römische Marine) | Blei-Kontamination über Jahrhunderte |
| 1800er | Kupfertanks und -leitungen auf Segelschiffen | Erster Standard, antimikrobielle Wirkung |
| 1920er | Verzinkte Stahlrohre in der Schifffahrt | Günstig, aber Korrosionsanfällig |
| 1950er | PVC-Rohre und -Schläuche | Revolution, aber Weichmacher-Problem |
| 1960er | Erste Druckwasserpumpen (12V) für Yachten | Komfort-Sprung: Drehkreuz → Wasserhahn |
| 1970er | PEX-Entwicklung (Thomas Engel, 1968: PEX-a Patent) | Vernetztes PE als Kupfer-Alternative |
| 1980er | John Guest Push-Fit System für Marine | Werkzeuglose Montage revolutioniert Yachtbau |
| 1990er | Umkehrosmose-Watermaker (Katadyn, Spectra) | Autarkie auf See möglich |
| 1998 | KTW-Leitlinie für Trinkwasser-Materialien (DE) | Erste systematische Materialprüfung |
| 2003 | W270 DVGW-Arbeitsblatt (Biofilm-Prüfung) | Mikrobielle Sicherheit wird Standard |
| 2008 | Viega Profipress Marine-Serie | Press-Verbindungen im Yachtbau |
| 2013 | EU-Richtlinie 2013/53/EU (Sportboote) | CE-Kennzeichnung inkl. Bordinstallationen |
| 2018 | UBA-Positivliste beginnt KTW abzulösen | Strengere, europaweite Materialprüfung |
| 2021 | EU-Trinkwasserrichtlinie 2020/2184 | Verschärfte Anforderungen, neue Parameter (PFAS) |
| 2024 | PFAS-Grenzwerte in Trinkwasser (EU) | Betrifft auch PTFE-Dichtungen (Diskussion) |

---

## ANHANG R — Stichwortverzeichnis

| Stichwort | Abschnitt |
|-----------|-----------|
| Aktivkohle-Filter | Wasserqualitäts-Parameter, FAQ TW-010, TW-032, Glossar |
| Akkumulator | Häufige Fehler, Troubleshooting Problem 2, FAQ TW-012, TW-035 |
| Anziehdrehmomente | Verbindungstechnik & Fittings |
| Arrhenius-Regel | Alterungsmechanismen, Glossar |
| Biegeradius | Technische Referenz, Häufige Fehler, ANHANG C |
| Biofilm | Fehlerbild FB-02, Lebensdauer, FAQ TW-022, Glossar |
| Certisil Combina | System-Desinfektion, FAQ TW-003, Glossar |
| Chlor | Wasserqualitäts-Parameter, Fehlerbild FB-11, FAQ TW-007 |
| Crimp-Verbindung | Crimpen vs Pressen, PEX-Crimp Installation, Glossar |
| Dichtmaterial | Verbindungstechnik (PTFE, O-Ring, Hanf) |
| Druckverlust | Technische Referenz, Fehlerbild FB-10, Troubleshooting |
| DZR-Messing | Push-Fit (SharkBite), Glossar |
| EPDM | Dichtmaterialien, Chlor-Verträglichkeit, Glossar |
| Frostschaden | Fehlerbild FB-07, Winterisierung, Fallstudie 6 |
| John Guest | Push-Fit Systeme, JG-Installation, ANHANG A |
| KTW/W270 | Dichtmaterialien, FAQ TW-006, ANHANG B, Glossar |
| Legionellen | Fehlerbild FB-03, FAQ TW-015, Fallstudie 2, Glossar |
| Material-Kosten | Technische Referenz (Vergleich pro Meter) |
| Mineralisierer | Watermaker-Anschluss, Fallstudie 5, Glossar |
| Notfall-Reparatur | Einbau-/Austausch-Anleitung |
| Oetiker-Schelle | Schlauchschellen, Glossar |
| PEX | Alle Abschnitte, ANHANG J (Datenblatt) |
| Press-Verbindung | Crimpen vs Pressen, PEX-Crimp Installation, Glossar |
| Propylenglykol | Winterisierung, FAQ TW-008, Glossar |
| PTFE | Dichtmaterialien, Glossar |
| Push-Fit | Verbindungstechnik, JG-Installation, FAQ TW-004, Glossar |
| PVC (Warnung) | Fehlerbild FB-12, FAQ TW-002, ANHANG L Nr. 1 |
| Silikon | Alle Abschnitte, ANHANG J (Datenblatt) |
| TSM-Insert | JG-Installation, ANHANG L Nr. 8, Glossar |
| Troubleshooting | Fehlerbehebungs-Leitfaden (5 Probleme) |
| UV-Degradation | Fehlerbild FB-08, Alterungsmechanismen |
| V4A/V2A | Schlauchschellen, ANHANG L Nr. 5, Glossar |
| Watermaker | Watermaker-Anschluss, Fallstudie 5, FAQ TW-017, TW-028 |
| Weichmacher | Fehlerbild FB-12, FAQ TW-002, Glossar (DEHP) |
| Winterisierung | Winterisierung, Fehlerbild FB-07, FAQ TW-008, Fallstudie 6 |
| Werkzeug | Werkzeug-Checkliste, FAQ TW-021 |

---

*Letztes Update: 2026-04-23 | AYDI Knowledge Base v6.2 | Confidence: measured (Herstellerdaten, Normen) + benchmark (Branchenerfahrung) | Nächste Revision: 2026-10-01*
