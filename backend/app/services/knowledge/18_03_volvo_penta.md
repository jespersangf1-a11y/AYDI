---
titel: "Volvo Penta Marine-Diesel — Modellreihen und Spezifikationen"
kategorie: "Motoren und Antrieb"
unterkategorie: "Volvo Penta Motoren"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 18_03 — Volvo Penta Marine-Diesel — Modellreihen und Spezifikationen

> **AYDI Wissensdatei 18.03** — Kategorie 18: Motoren und Antrieb
> **Confidence-Quelle:** measured (Hersteller-Datenblätter), documented (Werkstatt-Erfahrungen, Eigner-Berichte), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04

---

## Inhaltsverzeichnis

1. [Geschichte und Unternehmensübersicht](#1-geschichte-und-unternehmensübersicht)
2. [Modellnomenklatur und Baureihen-Systematik](#2-modellnomenklatur-und-baureihen-systematik)
3. [D1-Serie — Kompaktdiesel für Segelyachten](#3-d1-serie--kompaktdiesel-für-segelyachten)
4. [D2-Serie — Mittelklasse für Segel- und Kleinmotoryachten](#4-d2-serie--mittelklasse-für-segel--und-kleinmotoryachten)
5. [D3-Serie — Hochleistung für Sport- und Motorboote](#5-d3-serie--hochleistung-für-sport--und-motorboote)
6. [D4-Serie — Schwere Motorboote und leichte Verdränger](#6-d4-serie--schwere-motorboote-und-leichte-verdränger)
7. [D6-Serie — Große Motoryachten und Verdränger](#7-d6-serie--große-motoryachten-und-verdränger)
8. [D8-Serie — Schwere Verdränger und kommerzielle Boote](#8-d8-serie--schwere-verdränger-und-kommerzielle-boote)
9. [D11/D13/D16 — Großmotoren für Superyachten und kommerzielle Schiffe](#9-d11d13d16--großmotoren-für-superyachten-und-kommerzielle-schiffe)
10. [Saildrive-Systeme — 120S, 130S, 150S](#10-saildrive-systeme--120s-130s-150s)
11. [IPS-System — Integrierte Propulsor-Systeme](#11-ips-system--integrierte-propulsor-systeme)
12. [Aquamatic Sterndrive — SX, DPS, DPH](#12-aquamatic-sterndrive--sx-dps-dph)
13. [Wellenanlage und konventioneller Antrieb](#13-wellenanlage-und-konventioneller-antrieb)
14. [EVC — Electronic Vessel Control](#14-evc--electronic-vessel-control)
15. [NMEA 2000 Integration und Vernetzung](#15-nmea-2000-integration-und-vernetzung)
16. [Wartungsintervalle und Serviceplan](#16-wartungsintervalle-und-serviceplan)
17. [Motoröl und Betriebsstoffe](#17-motoröl-und-betriebsstoffe)
18. [Kühlsystem — Aufbau und Wartung](#18-kühlsystem--aufbau-und-wartung)
19. [Kraftstoffsystem und Dieselqualität](#19-kraftstoffsystem-und-dieselqualität)
20. [Bekannte Schwachstellen und typische Probleme](#20-bekannte-schwachstellen-und-typische-probleme)
21. [Fehlerbild-Atlas](#21-fehlerbild-atlas)
22. [Troubleshooting-Entscheidungsbäume](#22-troubleshooting-entscheidungsbäume)
23. [Ersatzteile — Original vs. Aftermarket](#23-ersatzteile--original-vs-aftermarket)
24. [Preise und Kostenübersicht](#24-preise-und-kostenübersicht)
25. [Fallstudien](#25-fallstudien)
26. [FAQ — Häufig gestellte Fragen](#26-faq--häufig-gestellte-fragen)
27. [Glossar](#27-glossar)
28. [ANHANG A — Technische Datenblätter Übersicht](#anhang-a--technische-datenblätter-übersicht)
29. [ANHANG B — Confidence-Mapping](#anhang-b--confidence-mapping)
30. [ANHANG C — AYDI-Integration (Pydantic-Modelle)](#anhang-c--aydi-integration-pydantic-modelle)
31. [ANHANG D — Wartungsprotokoll-Vorlage](#anhang-d--wartungsprotokoll-vorlage)
32. [ANHANG E — Händler- und Werkstattverzeichnis](#anhang-e--händler--und-werkstattverzeichnis)

---

## 1. Geschichte und Unternehmensübersicht

### 1.1 Gründung und Entwicklung

Volvo Penta wurde 1907 in Skövde, Schweden, als Motorenabteilung der AB Volvo gegründet. Der Name „Penta" leitet sich von den fünf Gründern ab, die den ersten schwedischen Verbrennungsmotor für den Marinebereich entwickelten. Seit 1935 gehört Volvo Penta zur Volvo-Gruppe und ist heute einer der weltweit führenden Hersteller von Marine- und Industriedieselmotoren.

**Meilensteine:**
- **1907:** Gründung, erster Marine-Benzinmotor B1
- **1914:** Erster mariner Dieselmotor
- **1937:** Einführung des Aquamatic-Konzepts (erstes Z-Antriebssystem der Welt, Markteinführung 1959)
- **1959:** Aquamatic — revolutionärer Sterndrive-Antrieb
- **1966:** Einführung der Saildrive-Technologie
- **1982:** Beginn der D-Motor-Baureihen (moderne Common-Rail-Technologie ab 2003)
- **1999:** Einführung EVC (Electronic Vessel Control)
- **2005:** Weltpremiere IPS (Inboard Performance System)
- **2010:** Volvo Penta IPS Generation 2
- **2015:** EVC2-Plattform mit NMEA 2000 Gateway
- **2019:** Volvo Penta als erster Hersteller mit IMO Tier III ohne SCR in der Freizeitschifffahrt
- **2021:** Elektrische und Hybrid-Antriebssysteme
- **2024:** D4/D6 Gen 3 mit verbesserter Emissionsreduktion
- **2025:** Erweiterte IPS-Palette mit IPS950 für Yachten bis 120 Fuß

### 1.2 Produktionsstandorte

| Standort | Produktion |
|----------|-----------|
| Skövde, Schweden | Motorenblock-Guss, D1/D2-Montage |
| Vara, Schweden | Saildrive, Aquamatic, IPS-Pods |
| Göteborg, Schweden | EVC-Elektronik, Hauptverwaltung |
| Lexington, Tennessee (USA) | Nordamerika-Montage |
| Lindesnes, Norwegen | IPS-Pod-Endmontage |

### 1.3 Marktposition

Volvo Penta ist in Europa Marktführer für Segelyacht-Dieselmotoren (geschätzter Anteil 45 %) und in Skandinavien dominierend (>65 %). Im Motorboot-Segment konkurriert Volvo Penta mit Mercury Marine (Cummins MerCruiser), Yanmar, Caterpillar und MAN. Das IPS-System hat im Segment 35–80 Fuß Motoryachten einen geschätzten Marktanteil von 55 % erreicht.

**Hauptkonkurrenten nach Segment:**

| Segment | Volvo Penta | Konkurrenten |
|---------|------------|-------------|
| Segelyacht 6–12 m | D1, D2 + Saildrive | Yanmar JH/GM, Nanni, Beta Marine, Craftsman |
| Segelyacht 12–20 m | D2, D3 + Saildrive/Welle | Yanmar 4JH, Nanni N4, Perkins |
| Motorboot Gleiter | D3, D4, D6 + Aquamatic | Mercury MerCruiser, Yanmar BY, Steyr |
| Motoryacht Verdränger | D4, D6, D8 + IPS/Welle | MAN i6, Caterpillar C7/C9, Cummins QSB |
| Superyacht | D11, D13, D16 + IPS | MTU 2000, MAN V8/V12, Caterpillar C18/C32 |

### 1.4 Servicenetzwerk

Volvo Penta betreibt weltweit über 4.000 autorisierte Händler und Servicewerkstätten in 130 Ländern. Die Verfügbarkeit von Ersatzteilen ist ein wesentlicher Wettbewerbsvorteil — in Europa sind die meisten Teile innerhalb von 24–48 Stunden ab Zentrallager Göteborg lieferbar.

**Servicestruktur:**
- **Volvo Penta Center (VPC):** Vollständige Werkstatt mit allen Zertifizierungen
- **Volvo Penta Dealer:** Autorisierter Händler mit Basiswerkstatt
- **Volvo Penta Service Point:** Saisonale oder mobile Servicestelle
- **Volvo Penta Connect:** Ferndiagnose über Cloud-basiertes Monitoring (ab EVC2)

---

## 2. Modellnomenklatur und Baureihen-Systematik

### 2.1 Typenschlüssel

Volvo Penta verwendet ein systematisches Benennungsschema:

```
D [Zylinderzahl/Klasse] - [PS-Leistung] [Suffix]
```

**Motorbezeichnung aufschlüsseln:**
- **D** = Diesel
- **Zahl nach D** = Baureihe/Größenklasse (nicht immer = Zylinderzahl)
- **Zahl nach Bindestrich** = ungefähre PS-Leistung bei Nenndrehzahl
- **Suffix-Buchstaben:**
  - Kein Suffix = Saildrive/Wellenanlage-Version
  - **A** = Aquamatic (Sterndrive)
  - **B** = höhere Leistungsstufe (z. B. D4-260 vs. D4-300)
  - **I** = Inboard (IPS)
  - **F** = Festpropeller-Variante
  - **EVC** = mit Electronic Vessel Control

### 2.2 Baureihen-Übersicht

| Baureihe | Zylinder | Hubraum (l) | Leistungsbereich (PS) | Typischer Einsatz |
|----------|----------|-------------|----------------------|-------------------|
| D1 | 1–3 | 0,5–1,1 | 12–30 | Segelyachten 6–10 m |
| D2 | 3–4 | 1,1–2,2 | 37–75 | Segelyachten 9–15 m |
| D3 | 5 | 2,4 | 110–220 | Sport-/Motorboote |
| D4 | 4 | 3,7 | 260–300 | Motorboote/Verdränger |
| D6 | 6 | 5,5 | 310–440 | Große Motoryachten |
| D8 | 8 (V) | 7,7 | 380–550 | Verdränger/kommerziell |
| D11 | 6 (Reihe) | 10,8 | 625–725 | Superyachten |
| D13 | 6 (Reihe) | 12,8 | 800–1.000 | Superyachten |
| D16 | 6 (Reihe) | 16,1 | 650–900 | Schwere Verdränger |

### 2.3 Emissionsstufen

| Stufe | Gültig ab | Geltungsbereich | Betroffene Motoren |
|-------|----------|----------------|-------------------|
| EU RCD Stage I | 2006 | EU-Freizeitschifffahrt | Alle |
| US EPA Tier 2 | 2006 | US-Gewässer | Alle für US-Markt |
| EU RCD Stage II | 2007 | EU ≥ 37 kW | D3, D4, D6+ |
| US EPA Tier 3 | 2012 | US ≥ 37 kW | D3, D4, D6+ |
| IMO Tier II | 2011 | Kommerzielle Schiffe | D8, D11, D13, D16 |
| IMO Tier III | 2016+ | ECA-Zonen | D13, D16 mit SCR/DPF |

### 2.4 Seriennummer und Baujahr

Die Seriennummer befindet sich auf dem Typenschild am Motor (meist auf dem Ventildeckel oder am Motorblock seitlich). Format:

```
Modell: D2-40
Seriennummer: A123456
Baujahr: 2018
Software-Version: EVC xxxxx
```

**Seriennummern-Bereiche (Beispiele D2-Serie):**
- D2-40 (2014–2019): A-Nummern ab A100000
- D2-40 (2019–heute): B-Nummern ab B100000
- D2-50 (2019–heute): B-Nummern
- D2-60 (2019–heute): B-Nummern
- D2-75 (2019–heute): B-Nummern

---

## 3. D1-Serie — Kompaktdiesel für Segelyachten

### 3.1 Übersicht

Die D1-Serie ist Volvo Pentas Einstiegsreihe für kleine Segelyachten von 6 bis 10 Metern. Diese Motoren zeichnen sich durch kompakte Abmessungen, geringes Gewicht und Zuverlässigkeit aus. Sie sind für den Hilfsantrieb auf Segelyachten konzipiert — Einsatzprofil: 200–400 Betriebsstunden pro Jahr, überwiegend Manövrieren im Hafen und Motoren bei Flaute.

### 3.2 D1-13

| Parameter | Wert |
|-----------|------|
| **Leistung** | 12,2 PS (9 kW) bei 3.600 U/min |
| **Zylinder** | 1 |
| **Hubraum** | 505 cm³ |
| **Bohrung × Hub** | 76 × 80 mm |
| **Verdichtung** | 23,5:1 |
| **Einspritzung** | Direkteinspritzung, mechanisch |
| **Kühlung** | Seewasser-direkt oder Zweikreis-Option |
| **Gewicht (trocken)** | 79 kg (Saildrive: + 38 kg) |
| **Abmessungen (L×B×H)** | 543 × 410 × 498 mm |
| **Kraftstoffverbrauch bei Volllast** | 3,5 l/h |
| **Kraftstoffverbrauch bei 75 %** | 2,6 l/h |
| **Motoröl-Füllmenge** | 1,7 l |
| **Empfohlenes Motoröl** | VDS-3, SAE 15W-40 |
| **Kühlmittel-Füllmenge** | 2,0 l (Zweikreis) |
| **Lichtmaschine** | 14V / 50A (Option: 115A) |
| **Starterbatterie (min.)** | 12V / 45 Ah |
| **Antriebsoptionen** | 120S Saildrive, MS10 Getriebe |
| **Geeignet für Boote** | 6–8 m Segelyachten, bis 3.500 kg Verdrängung |
| **Listenpreis (2025)** | ca. 7.800 € (Motor) / ca. 12.200 € (mit 120S Saildrive) |
| **Produktion** | 2005–heute |

**Besonderheiten D1-13:**
- Kleinster Marine-Diesel im Volvo-Penta-Programm
- Einzylinder — spürbare Vibrationen, Gummilagerung essenziell
- Kein Turbolader — wartungsarm, zuverlässig
- Seewasser-Direktkühlung Standard, Zweikreis empfohlen (Frostschutz, Korrosionsschutz)
- Verbreitet in Bavaria 32, Jeanneau Sun Odyssey 30, Hallberg-Rassy 310

### 3.3 D1-20

| Parameter | Wert |
|-----------|------|
| **Leistung** | 18,8 PS (14 kW) bei 3.600 U/min |
| **Zylinder** | 2 |
| **Hubraum** | 764 cm³ |
| **Bohrung × Hub** | 76 × 84,2 mm |
| **Verdichtung** | 23,5:1 |
| **Einspritzung** | Direkteinspritzung, mechanisch |
| **Kühlung** | Zweikreis (Seewasser + Frischwasser) |
| **Gewicht (trocken)** | 99 kg (Saildrive: + 38 kg) |
| **Abmessungen (L×B×H)** | 583 × 410 × 520 mm |
| **Kraftstoffverbrauch bei Volllast** | 5,5 l/h |
| **Kraftstoffverbrauch bei 75 %** | 4,1 l/h |
| **Motoröl-Füllmenge** | 2,5 l |
| **Empfohlenes Motoröl** | VDS-3, SAE 15W-40 |
| **Kühlmittel-Füllmenge** | 3,0 l |
| **Lichtmaschine** | 14V / 75A (Option: 115A) |
| **Starterbatterie (min.)** | 12V / 62 Ah |
| **Antriebsoptionen** | 120S Saildrive, MS15 Getriebe |
| **Geeignet für Boote** | 7–9 m Segelyachten, bis 5.000 kg Verdrängung |
| **Listenpreis (2025)** | ca. 9.500 € (Motor) / ca. 13.800 € (mit 120S Saildrive) |
| **Produktion** | 2005–heute |

**Besonderheiten D1-20:**
- Ruhigerer Lauf als D1-13 dank Zweizylinderkonzept
- Standardmotor für viele 30–34-Fuß-Segelyachten
- Verbreitet in Bavaria 34, Bénéteau Océanis 35, Dehler 34

### 3.4 D1-30

| Parameter | Wert |
|-----------|------|
| **Leistung** | 28,4 PS (21 kW) bei 3.600 U/min |
| **Zylinder** | 3 |
| **Hubraum** | 1.131 cm³ |
| **Bohrung × Hub** | 76 × 83 mm |
| **Verdichtung** | 23,5:1 |
| **Einspritzung** | Direkteinspritzung, mechanisch |
| **Kühlung** | Zweikreis |
| **Gewicht (trocken)** | 119 kg (Saildrive: + 38 kg) |
| **Abmessungen (L×B×H)** | 632 × 410 × 542 mm |
| **Kraftstoffverbrauch bei Volllast** | 8,2 l/h |
| **Kraftstoffverbrauch bei 75 %** | 6,2 l/h |
| **Motoröl-Füllmenge** | 3,5 l |
| **Empfohlenes Motoröl** | VDS-3, SAE 15W-40 |
| **Kühlmittel-Füllmenge** | 3,5 l |
| **Lichtmaschine** | 14V / 75A (Option: 115A) |
| **Starterbatterie (min.)** | 12V / 70 Ah |
| **Antriebsoptionen** | 130S Saildrive, MS25 Getriebe |
| **Geeignet für Boote** | 9–12 m Segelyachten, bis 8.000 kg Verdrängung |
| **Listenpreis (2025)** | ca. 11.200 € (Motor) / ca. 16.500 € (mit 130S Saildrive) |
| **Produktion** | 2005–heute |

**Besonderheiten D1-30:**
- Meistverkaufter Motor der D1-Serie
- Dreizylinder — guter Kompromiss aus Laufruhe und Kompaktheit
- Ausreichend für die meisten 35–38-Fuß-Segelyachten
- Verbreitet in Hallberg-Rassy 340, Bavaria 37, Jeanneau Sun Odyssey 379

### 3.5 D1-Serie: Gemeinsame Merkmale

**Motorblock:** Grauguss (GJL-250), nass eingesetzte Zylinderlaufbuchsen
**Zylinderkopf:** Aluminium-Legierung
**Nockenwelle:** OHV (über Stirnräder angetrieben)
**Schmierung:** Druckumlaufschmierung mit Vollstrom-Ölfilter
**Anlasser:** 12V / 1,2 kW
**Abgasanlage:** Nassauspuff über wassergekühlten Auspuffkrümmer

**Typische Lebensdauer D1-Serie:**
- Motorblock: 8.000–12.000 Betriebsstunden (bei ordnungsgemäßer Wartung)
- Einspritzpumpe: 4.000–6.000 h (Überholung erforderlich)
- Einspritzdüsen: 2.000–3.000 h (Prüfung/Austausch)
- Impeller: 500–700 h oder jährlich
- Keilriemen: 500–1.000 h oder jährlich

---

## 4. D2-Serie — Mittelklasse für Segel- und Kleinmotoryachten

### 4.1 Übersicht

Die D2-Serie ist Volvo Pentas volumenstärkste Marine-Diesel-Baureihe. Sie deckt den Leistungsbereich von 37 bis 75 PS ab und ist damit ideal für mittlere bis große Segelyachten (35–55 Fuß) sowie kleinere Motorboote. Ab 2019 wurde die D2-Serie grundlegend überarbeitet mit Common-Rail-Einspritzung und elektronischer Steuerung.

### 4.2 D2-40

| Parameter | Wert |
|-----------|------|
| **Leistung** | 37,5 PS (28 kW) bei 3.600 U/min |
| **Zylinder** | 2 (Reihe) |
| **Hubraum** | 1.124 cm³ |
| **Bohrung × Hub** | 82 × 84,2 mm |
| **Verdichtung** | 23,3:1 |
| **Einspritzung** | Common-Rail (ab 2019), vorher mechanisch |
| **Aufladung** | Nein (Sauger) |
| **Kühlung** | Zweikreis |
| **Gewicht (trocken)** | 137 kg |
| **Abmessungen (L×B×H)** | 687 × 498 × 578 mm |
| **Kraftstoffverbrauch Volllast** | 10,2 l/h |
| **Kraftstoffverbrauch 75 %** | 7,5 l/h |
| **Motoröl-Füllmenge** | 3,8 l |
| **Empfohlenes Motoröl** | VDS-4.5, SAE 15W-40 |
| **Kühlmittel-Füllmenge** | 4,5 l |
| **Lichtmaschine** | 14V / 115A |
| **Starterbatterie (min.)** | 12V / 70 Ah |
| **Antriebsoptionen** | 130S Saildrive, MS25 Getriebe, HS25AE Wendegetriebe |
| **Geeignet für Boote** | 10–13 m Segelyachten, bis 10.000 kg Verdrängung |
| **Listenpreis (2025)** | ca. 14.500 € (Motor) / ca. 20.800 € (mit 130S Saildrive) |
| **Produktion** | 2014–heute (CR ab 2019) |

> ⚠️ **ZU PRÜFEN (Audit):** Starterbatterie (min.) 70 Ah (diese Spezifikationstabelle) vs. 88 Ah (Abschnitt 26, FAQ 21, Zeile „D2-40/50") für den D2-40 — interner Widerspruch; korrekte Mindestkapazität unverifiziert (estimated — unverifiziert).

### 4.3 D2-50

| Parameter | Wert |
|-----------|------|
| **Leistung** | 47,3 PS (35 kW) bei 3.600 U/min |
| **Zylinder** | 3 (Reihe) |
| **Hubraum** | 1.686 cm³ |
| **Bohrung × Hub** | 82 × 84,2 mm |
| **Verdichtung** | 23,3:1 |
| **Einspritzung** | Common-Rail |
| **Aufladung** | Nein (Sauger) |
| **Kühlung** | Zweikreis |
| **Gewicht (trocken)** | 163 kg |
| **Abmessungen (L×B×H)** | 742 × 498 × 592 mm |
| **Kraftstoffverbrauch Volllast** | 12,8 l/h |
| **Kraftstoffverbrauch 75 %** | 9,5 l/h |
| **Motoröl-Füllmenge** | 5,0 l |
| **Empfohlenes Motoröl** | VDS-4.5, SAE 15W-40 |
| **Kühlmittel-Füllmenge** | 5,5 l |
| **Lichtmaschine** | 14V / 115A |
| **Starterbatterie (min.)** | 12V / 88 Ah |
| **Antriebsoptionen** | 130S Saildrive, MS25 Getriebe |
| **Geeignet für Boote** | 12–14 m Segelyachten, bis 14.000 kg Verdrängung |
| **Listenpreis (2025)** | ca. 16.800 € (Motor) / ca. 23.500 € (mit 130S Saildrive) |
| **Produktion** | 2019–heute |

### 4.4 D2-60

| Parameter | Wert |
|-----------|------|
| **Leistung** | 58,6 PS (43 kW) bei 3.600 U/min |
| **Zylinder** | 4 (Reihe) |
| **Hubraum** | 2.189 cm³ |
| **Bohrung × Hub** | 82 × 84,2 mm |
| **Verdichtung** | 23,3:1 |
| **Einspritzung** | Common-Rail |
| **Aufladung** | Nein (Sauger) |
| **Kühlung** | Zweikreis |
| **Gewicht (trocken)** | 185 kg |
| **Abmessungen (L×B×H)** | 798 × 498 × 612 mm |
| **Kraftstoffverbrauch Volllast** | 15,4 l/h |
| **Kraftstoffverbrauch 75 %** | 11,6 l/h |
| **Motoröl-Füllmenge** | 6,5 l |
| **Empfohlenes Motoröl** | VDS-4.5, SAE 15W-40 |
| **Kühlmittel-Füllmenge** | 6,5 l |
| **Lichtmaschine** | 14V / 115A |
| **Starterbatterie (min.)** | 12V / 88 Ah |
| **Antriebsoptionen** | 150S Saildrive, MS25L Getriebe |
| **Geeignet für Boote** | 13–16 m Segelyachten, bis 18.000 kg Verdrängung |
| **Listenpreis (2025)** | ca. 19.500 € (Motor) / ca. 27.200 € (mit 150S Saildrive) |
| **Produktion** | 2019–heute |

### 4.5 D2-75

| Parameter | Wert |
|-----------|------|
| **Leistung** | 75 PS (55 kW) bei 3.600 U/min |
| **Zylinder** | 4 (Reihe) |
| **Hubraum** | 2.189 cm³ |
| **Bohrung × Hub** | 82 × 84,2 mm |
| **Verdichtung** | 23,3:1 |
| **Einspritzung** | Common-Rail |
| **Aufladung** | Turbolader (Wastegate) |
| **Kühlung** | Zweikreis mit Ladeluftkühler |
| **Gewicht (trocken)** | 198 kg |
| **Abmessungen (L×B×H)** | 812 × 520 × 648 mm |
| **Kraftstoffverbrauch Volllast** | 18,5 l/h |
| **Kraftstoffverbrauch 75 %** | 14,0 l/h |
| **Motoröl-Füllmenge** | 6,5 l |
| **Empfohlenes Motoröl** | VDS-4.5, SAE 15W-40 |
| **Kühlmittel-Füllmenge** | 7,0 l |
| **Lichtmaschine** | 14V / 115A |
| **Starterbatterie (min.)** | 12V / 88 Ah |
| **Antriebsoptionen** | 150S Saildrive, MS25L Getriebe |
| **Geeignet für Boote** | 14–18 m Segelyachten, bis 25.000 kg Verdrängung |
| **Listenpreis (2025)** | ca. 22.800 € (Motor) / ca. 31.500 € (mit 150S Saildrive) |
| **Produktion** | 2019–heute |

**Besonderheiten D2-75:**
- Einziger Turbomotor der D2-Serie
- Ladeluftkühlung über Seewasser-Wärmetauscher
- Turbo-Nachlaufzeit beachten: 2–3 Minuten Leerlauf vor Abstellen
- Bekanntes Problem: Turbolader-Ölundichtigkeit ab ca. 3.000 h (→ Abschnitt 20)

### 4.6 D2-Serie: Gemeinsame Merkmale

**Motorblock:** Grauguss, nass eingesetzte Zylinderlaufbuchsen
**Einspritzung (ab 2019):** Bosch Common-Rail-System, 1.600 bar Raildruck
**Steuerung:** Elektronische Motorsteuerung (ECU) mit CAN-Bus
**Abgasnachbehandlung:** Oxidationskatalysator (DOC)
**Instrumentierung:** Standard-Anzeigen oder EVC-Display (7" Farbe)

**D2-Serie Vorgängermodelle (2003–2019):**

| Vorgänger | Nachfolger | Änderung |
|-----------|-----------|----------|
| D2-55 (55 PS) | D2-50 + D2-60 | Aufgesplittet in zwei Modelle |
| D2-75 (alt, mech.) | D2-75 (CR) | Common-Rail-Einspritzung |
| MD22 | D2-40 | Komplette Neukonstruktion |

---

## 5. D3-Serie — Hochleistung für Sport- und Motorboote

### 5.1 Übersicht

Die D3-Serie basiert auf einem 2,4-Liter-Fünfzylinder-Reihenmotor und ist ausschließlich als Turbodiesel mit Common-Rail-Einspritzung und Ladeluftkühlung erhältlich. Sie wurde 2006 eingeführt und ist primär für leichte Gleiter, Sportboote und schnelle Motorboote konzipiert. Der Motor stammt aus der Volvo-PKW-Plattform (D5-Motor) und wurde für den Marineeinsatz adaptiert.

### 5.2 D3-110

| Parameter | Wert |
|-----------|------|
| **Leistung** | 110 PS (81 kW) bei 3.500 U/min |
| **Drehmoment** | 280 Nm bei 1.500–2.500 U/min |
| **Zylinder** | 5 (Reihe) |
| **Hubraum** | 2.400 cm³ |
| **Bohrung × Hub** | 81 × 93,2 mm |
| **Verdichtung** | 17,3:1 |
| **Einspritzung** | Common-Rail, Bosch, 1.800 bar |
| **Aufladung** | Turbolader (VGT — Variable Geometry Turbo) |
| **Kühlung** | Zweikreis mit Ladeluftkühler |
| **Gewicht (trocken)** | 270 kg |
| **Abmessungen (L×B×H)** | 785 × 580 × 668 mm |
| **Kraftstoffverbrauch Volllast** | 28 l/h |
| **Kraftstoffverbrauch Marschfahrt** | 18 l/h |
| **Motoröl-Füllmenge** | 7,5 l |
| **Empfohlenes Motoröl** | VDS-4.5, SAE 5W-30 |
| **Antriebsoptionen** | Aquamatic SX-A, MS25L Getriebe |
| **Listenpreis (2025)** | ca. 28.500 € (Motor + Aquamatic SX-A) |
| **Produktion** | 2006–heute |

### 5.3 D3-150

| Parameter | Wert |
|-----------|------|
| **Leistung** | 150 PS (110 kW) bei 3.500 U/min |
| **Drehmoment** | 370 Nm bei 1.500–2.500 U/min |
| **Zylinder** | 5 (Reihe) |
| **Hubraum** | 2.400 cm³ |
| **Verdichtung** | 17,3:1 |
| **Einspritzung** | Common-Rail, 1.800 bar |
| **Aufladung** | VGT-Turbolader |
| **Gewicht (trocken)** | 275 kg |
| **Kraftstoffverbrauch Volllast** | 38 l/h |
| **Kraftstoffverbrauch Marschfahrt** | 24 l/h |
| **Motoröl-Füllmenge** | 7,5 l |
| **Antriebsoptionen** | Aquamatic SX-A, DPS-A |
| **Listenpreis (2025)** | ca. 33.200 € (Motor + Aquamatic) |
| **Produktion** | 2006–heute |

### 5.4 D3-170

| Parameter | Wert |
|-----------|------|
| **Leistung** | 170 PS (125 kW) bei 3.500 U/min |
| **Drehmoment** | 400 Nm bei 1.500–2.500 U/min |
| **Zylinder** | 5 (Reihe) |
| **Hubraum** | 2.400 cm³ |
| **Verdichtung** | 17,3:1 |
| **Einspritzung** | Common-Rail, 1.800 bar |
| **Aufladung** | VGT-Turbolader (höherer Ladedruck) |
| **Gewicht (trocken)** | 278 kg |
| **Kraftstoffverbrauch Volllast** | 42 l/h |
| **Kraftstoffverbrauch Marschfahrt** | 27 l/h |
| **Motoröl-Füllmenge** | 7,5 l |
| **Antriebsoptionen** | Aquamatic DPS-A |
| **Listenpreis (2025)** | ca. 36.500 € (Motor + Aquamatic) |
| **Produktion** | 2006–heute |

### 5.5 D3-220

| Parameter | Wert |
|-----------|------|
| **Leistung** | 220 PS (162 kW) bei 3.500 U/min |
| **Drehmoment** | 480 Nm bei 1.500–2.500 U/min |
| **Zylinder** | 5 (Reihe) |
| **Hubraum** | 2.400 cm³ |
| **Verdichtung** | 17,3:1 |
| **Einspritzung** | Common-Rail, 1.800 bar |
| **Aufladung** | VGT-Turbolader (maximaler Ladedruck) |
| **Gewicht (trocken)** | 285 kg |
| **Kraftstoffverbrauch Volllast** | 55 l/h |
| **Kraftstoffverbrauch Marschfahrt** | 34 l/h |
| **Motoröl-Füllmenge** | 7,5 l |
| **Antriebsoptionen** | Aquamatic DPS-A |
| **Listenpreis (2025)** | ca. 42.000 € (Motor + Aquamatic) |
| **Produktion** | 2006–heute |

### 5.6 D3-Serie: Gemeinsame Merkmale und Besonderheiten

**Motorarchitektur:**
- Aluminium-Motorblock (leicht, aber wärmeleitfähig)
- Doppelte obenliegende Nockenwelle (DOHC), 4 Ventile pro Zylinder
- Zahnriemen-Antrieb (Wechselintervall: 600 h oder 5 Jahre!)
- Steuerkettensatz für Nebenaggregate

**Bekannte Probleme D3-Serie:**
1. **Zahnriemen:** Muss alle 600 Stunden oder 5 Jahre gewechselt werden — Riss = Motorschaden (Interferenz-Motor). Kosten Zahnriemenwechsel: 1.200–1.800 €
2. **VGT-Turbolader:** Verstellmechanik kann im Marinebetrieb (Ruß, Salzluft) festsitzen. Symptom: nachlassende Leistung, schwarzer Rauch. Reinigung: 800–1.500 €, Austausch: 3.500–5.000 €
3. **Common-Rail-Injektoren:** Empfindlich gegen Diesel-Verunreinigung. Austausch: ca. 450 € pro Injektor (5 Stück)
4. **Abgaskrümmer (Nassauspuff):** Korrosion nach 1.500–2.500 h möglich. Austausch: 2.200–3.500 €
5. **Ölverdünnung:** Bei häufigem Kurzstreckenbetrieb kann Diesel ins Motoröl gelangen. Ölwechsel dann häufiger nötig

---

## 6. D4-Serie — Schwere Motorboote und leichte Verdränger

### 6.1 Übersicht

Die D4-Serie ist ein 3,7-Liter-Vierzylinder-Turbodiesel mit Common-Rail-Einspritzung. Sie wurde 2004 eingeführt und ist der Einstieg in die Hochleistungs-Marinediesel von Volvo Penta. Verfügbar als Aquamatic- oder IPS-Variante.

### 6.2 D4-260

| Parameter | Wert |
|-----------|------|
| **Leistung** | 260 PS (191 kW) bei 3.500 U/min |
| **Drehmoment** | 620 Nm bei 1.500–2.500 U/min |
| **Zylinder** | 4 (Reihe) |
| **Hubraum** | 3.700 cm³ |
| **Bohrung × Hub** | 103 × 110 mm |
| **Verdichtung** | 17,5:1 |
| **Einspritzung** | Common-Rail, Bosch, 2.000 bar |
| **Aufladung** | Zweistufiger Turbolader |
| **Kühlung** | Zweikreis mit Ladeluftkühler |
| **Gewicht (trocken)** | 380 kg (Motor), IPS: +190 kg |
| **Abmessungen (L×B×H)** | 920 × 695 × 780 mm |
| **Kraftstoffverbrauch Volllast** | 62 l/h |
| **Kraftstoffverbrauch Marschfahrt** | 38 l/h |
| **Motoröl-Füllmenge** | 12 l |
| **Empfohlenes Motoröl** | VDS-4.5, SAE 10W-40 |
| **Kühlmittel-Füllmenge** | 12 l |
| **Lichtmaschine** | 14V / 180A |
| **Starterbatterie (min.)** | 12V / 140 Ah |
| **Antriebsoptionen** | IPS400, Aquamatic DPH-A, Wellenanlage |
| **Geeignet für Boote** | 30–45 Fuß Motorboote, bis 15 t Verdrängung |
| **Listenpreis (2025)** | ca. 52.000 € (Motor + IPS400) |
| **Produktion** | 2004–heute (aktuelle Gen 3 ab 2024) |

### 6.3 D4-300

| Parameter | Wert |
|-----------|------|
| **Leistung** | 300 PS (221 kW) bei 3.500 U/min |
| **Drehmoment** | 700 Nm bei 1.500–2.500 U/min |
| **Zylinder** | 4 (Reihe) |
| **Hubraum** | 3.700 cm³ |
| **Verdichtung** | 17,5:1 |
| **Einspritzung** | Common-Rail, 2.000 bar |
| **Aufladung** | Zweistufiger Turbolader (höherer Ladedruck) |
| **Gewicht (trocken)** | 385 kg |
| **Kraftstoffverbrauch Volllast** | 72 l/h |
| **Kraftstoffverbrauch Marschfahrt** | 42 l/h |
| **Motoröl-Füllmenge** | 12 l |
| **Antriebsoptionen** | IPS400, Aquamatic DPH-A |
| **Listenpreis (2025)** | ca. 58.000 € (Motor + IPS400) |
| **Produktion** | 2004–heute |

### 6.4 D4-Serie: Technische Besonderheiten

**Motorblock:** Kompaktgraphit-Gusseisen (CGI) — leichter und steifer als Grauguss
**Zylinderkopf:** 4 Ventile pro Zylinder, DOHC
**Steuerung:** Vollständige EVC-Integration, CAN-Bus
**Abgasnachbehandlung:** DOC + DPF (Dieselpartikelfilter ab Gen 3)
**Motorlagerung:** Elastische Lager mit 60-Hz-Isolierung

**Wichtig für Bootsbauer:**
- Flanschmaße identisch D4/D6 — Motortausch D4→D6 möglich bei identischem Bett
- IPS400-Pods identische Geometrie wie IPS500 — Upgrade durch Motorwechsel möglich
- Minimaler Kielfreigang IPS400: 150 mm unter Podunterkante

---

## 7. D6-Serie — Große Motoryachten und Verdränger

### 7.1 Übersicht

Die D6-Serie ist ein 5,5-Liter-Sechszylinder-Reihenmotor mit Common-Rail-Einspritzung und zweistufiger Aufladung. Sie ist der meistverkaufte Motor im Segment 40–65-Fuß-Motoryachten und bildet das Rückgrat der IPS-Antriebe.

### 7.2 Modellübersicht D6

| Modell | Leistung | Drehmoment | Anwendung | Listenpreis (2025) |
|--------|----------|-----------|-----------|-------------------|
| D6-310 | 310 PS (228 kW) | 750 Nm | Verdränger | ca. 68.000 € + IPS500 |
| D6-340 | 340 PS (250 kW) | 830 Nm | Semi-Verdränger | ca. 72.000 € + IPS500 |
| D6-380 | 380 PS (280 kW) | 900 Nm | Gleiter | ca. 78.000 € + IPS600 |
| D6-440 | 440 PS (324 kW) | 980 Nm | Schnelle Gleiter | ca. 85.000 € + IPS600 |

### 7.3 Gemeinsame Spezifikationen D6

| Parameter | Wert |
|-----------|------|
| **Zylinder** | 6 (Reihe) |
| **Hubraum** | 5.500 cm³ |
| **Bohrung × Hub** | 103 × 110 mm |
| **Verdichtung** | 17,5:1 |
| **Einspritzung** | Common-Rail, 2.000 bar |
| **Aufladung** | Zweistufige Turboaufladung mit Ladeluftkühlung |
| **Gewicht (trocken)** | 520–535 kg (je Modell) |
| **Abmessungen (L×B×H)** | 1.075 × 695 × 780 mm |
| **Motoröl-Füllmenge** | 18 l |
| **Empfohlenes Motoröl** | VDS-4.5, SAE 10W-40 |
| **Kühlmittel-Füllmenge** | 16 l |
| **Lichtmaschine** | 14V / 180A (Twin-Option: 2 × 180A) |
| **Starterbatterie (min.)** | 12V / 140 Ah (2 × parallel empfohlen) |
| **Antriebsoptionen** | IPS500/600, Aquamatic DPH-D, Wellenanlage |

### 7.4 D6-Serie: Vergleich zum Vorgänger

Der D6 ersetzte den legendären TAMD 41/42 (6 Zylinder, 200–300 PS). Wesentliche Verbesserungen:
- 30 % weniger Kraftstoffverbrauch bei gleicher Leistung
- 50 % weniger Emissionen (NOx, Partikel)
- 40 % weniger Vibrationen
- Integrierte Elektronik (EVC vs. mechanische Steuerung)

### 7.5 Bekannte Problemstellen D6

1. **Ladeluftkühler-Undichtigkeit:** Seewasserseitiger Ladeluftkühler kann korrodieren, Seewasser gelangt in den Ladelufttrakt und von dort in die Zylinder → schwerer Motorschaden. Symptom: weißer Rauch, Kühlwasserverlust, Leistungsverlust. **Prüfung:** Jährlich Drucktest Ladeluftkühler. Austausch: 3.500–5.500 €
2. **Abgaskrümmer/Mischrohr:** Korrosion nach 2.000–4.000 h. Regelmäßige Inspektion. Austausch: 4.000–6.000 €
3. **Schwingungsdämpfer (Crankshaft Damper):** Alterung nach 5.000 h. Austausch präventiv empfohlen. Kosten: 1.500–2.500 €

---

## 8. D8-Serie — Schwere Verdränger und kommerzielle Boote

### 8.1 Übersicht

Die D8-Serie ist ein V8-Motor mit 7,7 Litern Hubraum. Er schließt die Lücke zwischen den 6-Zylinder-D6-Motoren und den großen Reihenmotoren D11/D13.

### 8.2 Modellübersicht D8

| Modell | Leistung | Drehmoment | Gewicht | Anwendung |
|--------|----------|-----------|---------|-----------|
| D8-380 | 380 PS (280 kW) | 1.100 Nm | 685 kg | Verdränger |
| D8-450 | 450 PS (331 kW) | 1.280 Nm | 695 kg | Semi-Verdränger |
| D8-510 | 510 PS (375 kW) | 1.420 Nm | 700 kg | Gleiter |
| D8-550 | 550 PS (405 kW) | 1.500 Nm | 710 kg | Schnelle Gleiter |

### 8.3 Gemeinsame Spezifikationen D8

| Parameter | Wert |
|-----------|------|
| **Zylinder** | 8 (V-90°) |
| **Hubraum** | 7.700 cm³ |
| **Bohrung × Hub** | 108 × 105 mm |
| **Verdichtung** | 17,0:1 |
| **Einspritzung** | Common-Rail, 2.200 bar |
| **Aufladung** | Biturbo (je 1 Turbolader pro Zylinderbank) |
| **Kühlung** | Zweikreis mit Ladeluftkühlung |
| **Motoröl-Füllmenge** | 25 l |
| **Empfohlenes Motoröl** | VDS-4.5, SAE 10W-40 |
| **Kühlmittel-Füllmenge** | 22 l |
| **Lichtmaschine** | 14V / 240A |
| **Starterbatterie (min.)** | 2 × 12V / 140 Ah |
| **Antriebsoptionen** | IPS700, Wellenanlage |
| **Listenpreis (2025)** | ca. 120.000–155.000 € (Motor + IPS700) |

---

## 9. D11/D13/D16 — Großmotoren für Superyachten und kommerzielle Schiffe

### 9.1 D11-Serie

| Parameter | Wert |
|-----------|------|
| **Zylinder** | 6 (Reihe) |
| **Hubraum** | 10.800 cm³ |
| **Leistungsbereich** | 625–725 PS (460–533 kW) |
| **Drehmoment** | 2.400–2.800 Nm |
| **Bohrung × Hub** | 123 × 152 mm |
| **Verdichtung** | 18,0:1 |
| **Einspritzung** | Common-Rail, Volvo EMS, 2.400 bar |
| **Aufladung** | VGT-Turbolader |
| **Gewicht (trocken)** | 1.065 kg |
| **Motoröl-Füllmenge** | 38 l |
| **Empfohlenes Motoröl** | VDS-5, SAE 10W-40 |
| **Kühlmittel-Füllmenge** | 32 l |
| **Lichtmaschine** | 24V / 140A |
| **Starterbatterie** | 24V-System, 2 × 12V / 225 Ah in Reihe |
| **Antriebsoptionen** | IPS950, Wellenanlage |
| **Geeignet für Boote** | 60–90 Fuß Motoryachten |
| **Listenpreis (2025)** | ca. 180.000–220.000 € (Motor) |
| **Produktion** | 2015–heute |

### 9.2 D13-Serie

| Parameter | Wert |
|-----------|------|
| **Zylinder** | 6 (Reihe) |
| **Hubraum** | 12.800 cm³ |
| **Leistungsbereich** | 800–1.000 PS (588–736 kW) |
| **Drehmoment** | 3.200–3.800 Nm |
| **Bohrung × Hub** | 131 × 158 mm |
| **Verdichtung** | 18,0:1 |
| **Einspritzung** | Common-Rail, 2.400 bar |
| **Aufladung** | Zweistufiger VGT-Turbolader |
| **Gewicht (trocken)** | 1.280 kg |
| **Motoröl-Füllmenge** | 45 l |
| **Kühlmittel-Füllmenge** | 42 l |
| **Lichtmaschine** | 24V / 140A (Twin-Option) |
| **Starterbatterie** | 24V-System |
| **Antriebsoptionen** | IPS950 (Twin), Wellenanlage |
| **Geeignet für Boote** | 80–120 Fuß Motoryachten |
| **Listenpreis (2025)** | ca. 250.000–320.000 € (Motor) |
| **Produktion** | 2012–heute |

### 9.3 D16-Serie

| Parameter | Wert |
|-----------|------|
| **Zylinder** | 6 (Reihe) |
| **Hubraum** | 16.100 cm³ |
| **Leistungsbereich** | 650–900 PS (478–662 kW) |
| **Drehmoment** | 3.400–4.200 Nm |
| **Bohrung × Hub** | 144 × 165 mm |
| **Verdichtung** | 17,5:1 |
| **Einspritzung** | Volvo Penta EMS, 2.400 bar |
| **Aufladung** | VGT-Turbolader |
| **Gewicht (trocken)** | 1.620 kg |
| **Motoröl-Füllmenge** | 56 l |
| **Kühlmittel-Füllmenge** | 52 l |
| **Lichtmaschine** | 24V / 140A |
| **Starterbatterie** | 24V-System, 4 × 12V / 225 Ah |
| **Antriebsoptionen** | Wellenanlage (kein IPS verfügbar) |
| **Geeignet für Boote** | Schwere Verdränger 80–150 Fuß, Arbeitsboote |
| **Listenpreis (2025)** | ca. 280.000–380.000 € (Motor) |
| **Produktion** | 2010–heute |

**Besonderheiten D16:**
- Niedrigste Nenndrehzahl aller VP-Marinemotoren: 1.800 U/min
- Optimiert für Verdrängerbetrieb bei langen Überfahrten
- Vibrations- und Geräuschoptimiert durch Sekundärausgleichswellen
- Bewährt in kommerzieller Fischerei und Offshore-Versorgern

### 9.4 Großmotoren-Abgasnachbehandlung

Ab IMO Tier III (ECA-Zonen: Nordsee, Ostsee, Nordamerika-Küste):
- **D11:** DOC + DPF
- **D13:** DOC + DPF + SCR (AdBlue/DEF)
- **D16:** DOC + SCR

| Abgassystem | Komponente | Austausch-Intervall | Kosten |
|-------------|-----------|---------------------|--------|
| DOC | Oxidationskatalysator | 8.000–12.000 h | 2.500–4.500 € |
| DPF | Partikelfilter | 6.000–10.000 h (Reinigung alle 2.000 h) | 5.000–8.000 € |
| SCR | Katalysator + Dosiereinheit | 10.000 h (Katalysator), 5.000 h (Dosiereinheit) | 6.000–12.000 € |

---

## 10. Saildrive-Systeme — 120S, 130S, 150S

### 10.1 Funktionsprinzip

Der Saildrive ist ein integriertes Antriebssystem, das Motor und Unterwasserantrieb in einer kompakten Einheit verbindet. Anstelle einer Wellenanlage mit Stevenrohr und Stopfbuchse durchdringt der Saildrive-Schaft den Rumpf durch eine Gummimembran (Diaphragma). Ein integriertes Getriebe (vorwärts/rückwärts/neutral) überträgt die Kraft auf einen Faltpropeller.

**Vorteile Saildrive:**
- Kein Stevenrohr, keine Wellenanlage, keine Stopfbuchse
- Geringerer Installationsaufwand
- Besserer Propellerwirkungsgrad (Propeller direkt unter dem Rumpf)
- Weniger Vibrationen und Geräusche
- Leichtere Motorausrichtung (keine Wellenausrichtung nötig)

**Nachteile Saildrive:**
- Membran muss regelmäßig kontrolliert und alle 7–10 Jahre getauscht werden
- Zinkanoden müssen häufiger gewechselt werden (2× pro Saison)
- Reparatur im Wasser nur eingeschränkt möglich
- Höhere Anschaffungskosten als einfache Wellenanlage

### 10.2 Saildrive 120S

| Parameter | Wert |
|-----------|------|
| **Motorkompatibilität** | D1-13, D1-20 |
| **Max. Eingangsleistung** | 22 kW (30 PS) |
| **Untersetzung** | 2,15:1 |
| **Propellergröße** | 14"–16" |
| **Gewicht** | 38 kg |
| **Schaftlänge** | 390 mm (Standard), 500 mm (Long Shaft) |
| **Zinkanoden** | 2 Stück (Ring + Propellermutter) |
| **Getriebeöl** | 0,6 l, SAE 30 oder 75W-90 Synthetic |
| **Membran-Material** | EPDM-Gummi, verstärkt |
| **Membran-Innendurchmesser** | 230 mm |
| **Listenpreis Saildrive** | ca. 4.400 € |
| **Listenpreis Membran** | ca. 380 € |
| **Produktion** | 1995–heute |

### 10.3 Saildrive 130S

| Parameter | Wert |
|-----------|------|
| **Motorkompatibilität** | D1-30, D2-40, D2-50 |
| **Max. Eingangsleistung** | 40 kW (54 PS) |
| **Untersetzung** | 2,15:1 oder 2,47:1 (wählbar) |
| **Propellergröße** | 16"–19" |
| **Gewicht** | 45 kg |
| **Schaftlänge** | 390 mm (Standard), 500 mm (Long Shaft) |
| **Zinkanoden** | 2 Stück |
| **Getriebeöl** | 0,8 l |
| **Membran-Innendurchmesser** | 260 mm |
| **Listenpreis Saildrive** | ca. 5.800 € |
| **Listenpreis Membran** | ca. 420 € |
| **Produktion** | 2000–heute |

### 10.4 Saildrive 150S

| Parameter | Wert |
|-----------|------|
| **Motorkompatibilität** | D2-60, D2-75 |
| **Max. Eingangsleistung** | 60 kW (81 PS) |
| **Untersetzung** | 2,15:1 oder 2,47:1 oder 2,72:1 |
| **Propellergröße** | 18"–22" |
| **Gewicht** | 56 kg |
| **Schaftlänge** | 420 mm (Standard), 530 mm (Long Shaft) |
| **Zinkanoden** | 3 Stück (Ring + 2 × Propellerschaft) |
| **Getriebeöl** | 1,0 l |
| **Membran-Innendurchmesser** | 290 mm |
| **Listenpreis Saildrive** | ca. 7.200 € |
| **Listenpreis Membran** | ca. 480 € |
| **Produktion** | 2012–heute |

### 10.5 Saildrive-Membran — Das kritischste Bauteil

> **WARNUNG:** Die Saildrive-Membran ist das einzige Bauteil, das bei Versagen zum Sinken des Bootes führen kann. Sie muss ernst genommen werden.

**Material:** EPDM-Gummi (Ethylen-Propylen-Dien-Monomer), UV-stabilisiert, ozonbeständig, seewasserfest

**Lebensdauer:**
- Volvo Penta Empfehlung: Austausch alle 7 Jahre
- Praxis-Empfehlung (Surveyor): Austausch alle 7–10 Jahre, jährliche Inspektion
- Maximal: 15 Jahre (nur bei nachgewiesener Flexibilität und Rissfreiheit)

**Alterungszeichen (bei Haul-out prüfen!):**
1. Oberflächenrisse (Crazing) — beginnende Alterung
2. Verhärtung — Elastizität nachlassend
3. Quellung — Chemische Degradation
4. Verfärbung — UV-Schäden
5. Kalkablagerungen — Seewassereinwirkung

**Inspektionsprotokoll:**
```
1. Boot aus dem Wasser (Haul-out)
2. Membran von außen visuell prüfen (Risse, Verhärtung)
3. Membran von innen prüfen (Bilge-Zugang)
4. Flexibilitätstest: mit Finger leicht eindrücken — muss sofort zurückspringen
5. Dichtheitsprüfung: trockene Bilge nach 24 h an Land?
6. Schlauchschellen prüfen: alle fest? Korrosion an Schellen?
7. Zinkanoden prüfen: >50 % vorhanden?
```

**Membrantausch — Ablauf:**
1. Boot an Land, Saildrive-Bereich trockenlegen
2. Propeller demontieren
3. Saildrive-Gehäuse absenken (4 Befestigungsschrauben)
4. Alte Membran entfernen (Schlauchschellen lösen)
5. Dichtflächen reinigen (Aceton, kein Schleifpapier)
6. Neue Membran einsetzen, Dichtmasse (Sikaflex 291i) auf Flansch
7. Schlauchschellen montieren (Edelstahl A4, neue Schellen!)
8. Saildrive-Gehäuse wieder anheben
9. Zinkanoden erneuern
10. Propeller montieren
11. Dichtheitsprüfung (Boot zu Wasser, 30 min beobachten)

**Kosten Membrantausch (2025):**
- Membran Original VP: 380–480 € (je nach Modell)
- Schlauchschellen (4 St.): 45 €
- Dichtmasse: 25 €
- Zinkanoden (Satz): 35–65 €
- Arbeitszeit (Werft): 3–5 h à 95–120 €/h = 285–600 €
- **Gesamtkosten: 770–1.215 €**

### 10.6 Saildrive-Zinkanoden

| Anode | Gewicht | Lebensdauer | Preis |
|-------|---------|------------|-------|
| Ring-Anode 120S | 0,5 kg | 6–12 Monate | 22 € |
| Ring-Anode 130S | 0,7 kg | 6–12 Monate | 28 € |
| Ring-Anode 150S | 0,9 kg | 6–12 Monate | 35 € |
| Propellermutter-Anode | 0,3 kg | 6–12 Monate | 18 € |

**Wichtig:** In Süßwasser Magnesium-Anoden verwenden, in Brackwasser Aluminium-Anoden. Zink nur in Salzwasser. Falsche Anodenauswahl = galvanische Korrosion am Saildrive-Gehäuse!

### 10.7 Saildrive-Getriebeöl

| Saildrive | Ölmenge | Wechselintervall | Empfohlenes Öl |
|-----------|---------|-----------------|---------------|
| 120S | 0,6 l | 200 h oder jährlich | SAE 75W-90 Synthetic |
| 130S | 0,8 l | 200 h oder jährlich | SAE 75W-90 Synthetic |
| 150S | 1,0 l | 200 h oder jährlich | SAE 75W-90 Synthetic |

**Ölkontrolle:** Getriebeöl auf Magnetsonde prüfen — Metallspäne deuten auf Zahnverschleiß hin. Milchiges Öl = Wassereinbruch über Wellendichtring!

---

## 11. IPS-System — Integrierte Propulsor-Systeme

### 11.1 Funktionsprinzip

Das Volvo Penta IPS (Inboard Performance System) ist ein Pod-Antriebssystem, bei dem der Motor im Rumpf sitzt und über ein Zwischenstück zwei gegenläufige Propeller antreibt, die unter dem Rumpf in nach vorn gerichteten Pods montiert sind. Das System bietet:

- **Zugpropeller-Prinzip:** Propeller ziehen das Boot durch ungestörtes Wasser
- **Gegenläufige Propeller (Duoprop):** Eliminierung des Drehmomenteffekts
- **Steuerbare Pods:** 360°-Drehung für präzise Manövrierfähigkeit
- **Joystick-Steuerung:** Intuitives Manövrieren im Hafen

### 11.2 IPS-Modellübersicht

| Modell | Motor | Leistung | Propeller | Max. Geschwindigkeit | Geeignet für | Listenpreis (2025, pro Einheit) |
|--------|-------|----------|-----------|---------------------|-------------|-------------------------------|
| IPS400 | D4-260/300 | 260–300 PS | F4 Duoprop | 32 kn | 30–45 ft | ca. 52.000–58.000 € |
| IPS500 | D6-310/340 | 310–340 PS | G3 Duoprop | 34 kn | 38–55 ft | ca. 68.000–72.000 € |
| IPS600 | D6-380/440 | 380–440 PS | H5 Duoprop | 38 kn | 45–65 ft | ca. 78.000–85.000 € |
| IPS700 | D8-510/550 | 510–550 PS | J4 Duoprop | 40 kn | 55–80 ft | ca. 120.000–155.000 € |
| IPS950 | D11/D13 | 625–1.000 PS | K4 Duoprop | 30 kn | 70–120 ft | ca. 230.000–350.000 € |

### 11.3 IPS-Vorteile gegenüber konventioneller Wellenanlage

| Kriterium | IPS | Konventionell |
|-----------|-----|--------------|
| Kraftstoffeffizienz | +30 % (Herstellerangabe) | Basis |
| Geschwindigkeit | +20 % bei gleicher Leistung | Basis |
| Manövrierfähigkeit | Joystick, seitwärts, drehen auf der Stelle | Ruder + Schubumkehr |
| Innenraum | Motorraum kürzer (kein Wellenrohr) | Langer Wellengang |
| Vibrationen | Deutlich reduziert | Normal |
| Geräusch | 10–15 dB(A) weniger in Kabine | Normal |
| Wartung | Pod-Service im Wasser möglich | Standard |
| Tiefgang | +200–300 mm vs. Welle | Flacher |

### 11.4 IPS-Joystick und DPS (Dynamic Positioning System)

Das IPS-Joystick-System ermöglicht intuitives Manövrieren:

**Joystick-Funktionen:**
- **Seitwärts:** Boot bewegt sich seitlich (parallel zum Steg)
- **Drehen:** Boot dreht auf der Stelle (um Mittelpunkt)
- **Diagonal:** Beliebige Kombinationen
- **Low-Speed:** Feinfühlige Steuerung bei Hafenmanövern

**DPS (Dynamic Positioning System):**
- Hält Boot auf Position und Kurs (GPS-gestützt)
- Kompensiert Wind, Strömung, Drift
- Ideal für Ankern, Warten vor Schleuse, Beiboot-Manöver
- Erfordert: IPS + Joystick + GPS-Antenne + EVC2

**Kosten DPS-Nachrüstung:** ca. 3.500–5.500 € (bei vorhandenem IPS + EVC2)

### 11.5 IPS-Wartung

| Wartungsarbeit | Intervall | Kosten (2025) |
|---------------|----------|---------------|
| Pod-Zinkanoden wechseln | 1× pro Saison | 180–350 € (Material) |
| Pod-Getriebeöl wechseln | 200 h oder jährlich | 120–180 € |
| Propeller inspizieren | 1× pro Saison | 0 € (Sichtkontrolle) |
| Propeller polieren | 1× pro Saison | 150–300 € |
| Pod-Antifouling | 1× pro Saison | 200–400 € |
| Bellows (Faltenbälge) prüfen | 1× pro Saison | 0 € (Sichtkontrolle) |
| Bellows tauschen | Alle 5–7 Jahre | 1.500–2.800 € |
| Gimbal-Ring-Lager prüfen | Alle 500 h | 0 € (Spielkontrolle) |
| Großer Pod-Service | Alle 1.000 h oder 5 Jahre | 3.500–6.500 € |

### 11.6 IPS-bekannte Probleme

1. **Pod-Korrosion:** Aluminium-Gehäuse in Salzwasser — Zinkanoden-Pflege essenziell. Vernachlässigung führt zu Lochfraß am Pod-Gehäuse. Reparatur: 8.000–15.000 € pro Pod
2. **Faltenbälge (Bellows):** Gummi altert wie Saildrive-Membran. Risse = Wassereinbruch. Austausch alle 5–7 Jahre
3. **Geräusche aus dem Pod:** Können auf Lagerverschleiß hindeuten. Frühzeitig prüfen!
4. **Antifouling:** Pod-Oberfläche muss spezielles Antifouling erhalten (keine kupferhaltigen Produkte auf Aluminium!)
5. **GPS-Drift bei DPS:** In Häfen mit vielen Reflexionen (Metallstrukturen) kann DPS ungenau werden

---

## 12. Aquamatic Sterndrive — SX, DPS, DPH

### 12.1 Funktionsprinzip

Der Aquamatic Sterndrive (Z-Antrieb) war Volvo Pentas bahnbrechende Erfindung von 1959. Der Motor sitzt inboard, die Kraft wird über eine Kardanwelle durch den Heckspiegel auf den schwenkbaren Antrieb (Sterndrive) übertragen. Der Sterndrive kombiniert Getriebe und Propellerantrieb und ermöglicht durch Schwenken die Steuerung des Bootes.

### 12.2 Modellübersicht Aquamatic

| Modell | Motor | Propeller | Max. Leistung | Gewicht | Anwendung |
|--------|-------|-----------|--------------|---------|-----------|
| SX-A | D3-110/150 | Einzelpropeller | 170 PS | 72 kg | Sportboote bis 28 ft |
| DPS-A | D3-170/220 | Duoprop (Typ A) | 280 PS | 85 kg | Sportboote bis 32 ft |
| DPS-B | D4 | Duoprop (Typ B) | 350 PS | 92 kg | Motorboote bis 38 ft |
| DPH-A | D3/D4 | Duoprop (Typ H) | 350 PS | 98 kg | Hochleistung |
| DPH-D | D6 | Duoprop (Typ H) | 440 PS | 112 kg | Große Motorboote |

### 12.3 Duoprop-System

Das Duoprop-System verwendet zwei gegenläufige Propeller auf derselben Achse:

**Vorteile:**
- Kein Drehmomenteffekt (Boot fährt geradeaus)
- Besserer Wirkungsgrad (+20 % vs. Einzelpropeller laut Hersteller)
- Bessere Beschleunigung
- Weniger Kavitation

**Propellergrößen (Duoprop):**

| Typ | Durchmesser | Motor | Material |
|-----|------------|-------|----------|
| A (klein) | 280–300 mm | D3-110 bis D3-220 | Aluminium oder Edelstahl |
| B (mittel) | 300–330 mm | D4-260/300 | Aluminium oder Edelstahl |
| H (groß) | 330–380 mm | D4/D6 | Edelstahl |

**Propeller-Preise (2025):**
- Aluminium Duoprop (Satz vorn+hinten): 650–900 €
- Edelstahl Duoprop (Satz vorn+hinten): 1.800–3.200 €

### 12.4 Aquamatic-Wartung

| Wartungsarbeit | Intervall | Kosten (2025) |
|---------------|----------|---------------|
| Getriebeöl wechseln (Sterndrive) | 100 h oder jährlich | 80–120 € |
| Zinkanoden wechseln | 1× pro Saison | 85–150 € |
| Faltenbälge (Bellows) prüfen | 1× pro Saison | Sichtkontrolle |
| Faltenbälge tauschen | Alle 3–5 Jahre | 800–1.500 € |
| Gimbal-Lager prüfen | 1× pro Saison | Spielkontrolle |
| Gimbal-Lager tauschen | Alle 5–8 Jahre | 1.200–2.000 € |
| U-Joint (Kardangelenk) tauschen | Alle 5–8 Jahre | 600–1.000 € |
| Antifouling Sterndrive | 1× pro Saison | 100–200 € |
| Trimmzylinder entlüften | Bei Bedarf | 50–100 € |

### 12.5 Kritische Sterndrive-Probleme

1. **Faltenbälge (Bellows):** Häufigste Ursache für Wassereinbruch! Abgas-Faltenbalg (Hitzeschäden), Lenk-Faltenbalg (mechanischer Verschleiß), Trimmzylinder-Faltenbalg. Austausch unbedingt alle 3–5 Jahre!
2. **Gimbal-Lager:** Nadellager, kann bei Salzwasser-Kontakt rosten. Symptom: Schwere Lenkung, Knarzen. Austausch: 1.200–2.000 €
3. **Korrosion Aluminium-Gehäuse:** Bei vernachlässigten Anoden — Lochfraß am Sterndrive-Gehäuse
4. **Shift-Kabel (Schaltzug):** Kann korrodieren oder einfrieren. Symptom: Gang lässt sich schwer einlegen. Austausch: 250–500 €

---

## 13. Wellenanlage und konventioneller Antrieb

### 13.1 Volvo Penta Wendegetriebe

| Modell | Max. Eingangsleistung | Untersetzungen | Gewicht | Einsatz |
|--------|----------------------|---------------|---------|---------|
| MS10A | 22 kW (30 PS) | 2,36:1 / 2,62:1 | 15 kg | D1-Serie |
| MS15A | 30 kW (40 PS) | 2,36:1 / 2,62:1 | 18 kg | D1-20, D1-30 |
| MS25A | 55 kW (75 PS) | 2,06:1 / 2,27:1 / 2,47:1 | 28 kg | D2-Serie |
| MS25L | 60 kW (81 PS) | 2,06:1 / 2,27:1 / 2,72:1 | 32 kg | D2-60, D2-75 |
| HS63AE | 221 kW (300 PS) | 1,55:1 / 1,97:1 / 2,33:1 | 85 kg | D4-Serie |
| HS80AE | 324 kW (440 PS) | 1,55:1 / 1,97:1 / 2,33:1 | 110 kg | D6-Serie |
| HS85AE | 405 kW (550 PS) | 1,23:1 / 1,55:1 / 2,04:1 | 135 kg | D8-Serie |

### 13.2 Propeller-Auswahl für Wellenanlage

**Faustregeln:**
- **Segelyacht (Verdrängung):** Propellerdurchmesser = 0,3 × LWL (in Zoll), 2-Blatt Faltpropeller
- **Motorboot (Verdränger):** Propellerdurchmesser = 0,4 × LWL (in Zoll), 3-Blatt Festpropeller
- **Motorboot (Gleiter):** Propellerdurchmesser = maximaler Einbau, 3- oder 4-Blatt

**Empfohlene Propellerhersteller:**
- **Gori (Dänemark):** Faltpropeller für Segelyachten — Premium-Qualität
- **Flexofold (Dänemark):** Faltpropeller — gutes Preis-Leistungs-Verhältnis
- **MaxProp (Italien):** Verstellpropeller für Segelyachten
- **Volvo Penta Original:** Festpropeller, Faltpropeller

---

## 14. EVC — Electronic Vessel Control

### 14.1 Übersicht

EVC (Electronic Vessel Control) ist Volvo Pentas elektronisches Steuerungssystem, das seit 1999 alle Motoren, Antriebe und Bordsysteme vernetzt. EVC ersetzt die mechanischen Gaszüge und Schaltkabel durch elektronische Signale und ermöglicht präzise, feinfühlige Steuerung.

### 14.2 EVC-Generationen

| Generation | Baujahr | Merkmale |
|-----------|---------|---------|
| EVC-A | 1999–2006 | Erste Generation, analoge Sensoren, CAN-Bus |
| EVC-B | 2006–2012 | Verbesserte Sensorik, Diagnose-Schnittstelle |
| EVC-C | 2012–2018 | Touchscreen-Displays, NMEA 2000 Gateway |
| EVC2 | 2018–heute | Cloud-Anbindung (VP Connect), OTA-Updates, WiFi |

### 14.3 EVC-Komponenten

| Komponente | Funktion | Preis (2025) |
|-----------|---------|-------------|
| EVC-ECU (Hauptsteuergerät) | Zentrale Steuerung, CAN-Bus-Master | 3.800–5.200 € |
| Helm-Station (Fahrstand) | Gas-/Schalthebel, elektronisch | 2.200–4.500 € |
| Display 7" Farbe | Motorparameter, Navigation, Diagnose | 2.800–3.500 € |
| Display 9" Touch | Erweitert, Glasscockpit-Integration | 4.200–5.800 € |
| Joystick | Hafenmanöver (IPS) | 3.200–4.500 € |
| DPS-Modul | Dynamic Positioning | 2.500–3.800 € |
| GPS-Sensor (DPS) | Positionierung für DPS | 800–1.200 € |
| Trim-Assistenz | Automatische Trimmung | 1.200–1.800 € |
| Interceptor-System | Automatische Trimm-Klappen | 3.500–5.500 € |
| Speed-Sensor | Fahrt durchs Wasser | 450–680 € |
| Treibstoff-Sensor | Verbrauchsmessung | 380–520 € |

### 14.4 EVC-Fehlercodes

EVC generiert Diagnosecodes, die über das Display oder den VODIA-Diagnosetester ausgelesen werden können.

**Häufige Fehlercodes:**

| Code | Bedeutung | Schwere | Maßnahme |
|------|----------|---------|---------|
| MID 128 SID 1 | Einspritzdüse Zyl. 1 Fehler | Gelb | Kabelverbindung prüfen, Injektor |
| MID 128 SID 22 | Ladelufttemperatur hoch | Gelb | Ladeluftkühler prüfen |
| MID 128 SID 27 | Kühlmitteltemperatur hoch | Rot | Sofort Drehzahl reduzieren, Impeller prüfen |
| MID 128 SID 94 | Kraftstoffdruck niedrig | Gelb | Vorfilter, Kraftstofffilter, Luft im System |
| MID 128 SID 100 | Motoröldruck niedrig | Rot | Sofort abstellen! Ölstand prüfen |
| MID 128 SID 102 | Ladedruck niedrig | Gelb | Turbolader, Ladeluftschlauch, VGT-Steller |
| MID 128 SID 110 | Kühlmittelstand niedrig | Rot | Leck suchen, Kühlmittel auffüllen |
| MID 128 SID 175 | Motoröltemperatur hoch | Gelb | Ölkühler prüfen, Ölstand |
| MID 144 SID 231 | CAN-Bus-Fehler | Gelb | Kabelverbindungen, Abschlusswiderstand |
| MID 144 SID 253 | Kommunikationsfehler Helm | Gelb | Helm-Station-Kabel prüfen |

### 14.5 EVC-Diagnose mit VODIA

VODIA (Volvo Diagnostics Application) ist das offizielle Diagnose-Tool von Volvo Penta:
- Nur für autorisierte Werkstätten verfügbar
- Verbindung über CAN-Bus-Adapter (USB oder WiFi)
- Funktionen: Fehlercodes lesen/löschen, Software-Update, Parametrierung, Probelauf

**Kosten VODIA-Diagnose in der Werkstatt:** 120–250 € (je nach Umfang)

---

## 15. NMEA 2000 Integration und Vernetzung

### 15.1 Volvo Penta NMEA 2000 Gateway

Ab EVC-C (2012) und EVC2 (2018) bietet Volvo Penta ein integriertes NMEA 2000 Gateway, das Motor- und Antriebsdaten auf dem NMEA 2000 Netzwerk bereitstellt.

**Verfügbare NMEA 2000 PGNs:**

| PGN | Daten | Aktualisierung |
|-----|-------|---------------|
| 127488 | Motordrehzahl | 100 ms |
| 127489 | Motorparameter (Temperatur, Öldruck, Spannung) | 500 ms |
| 127497 | Kraftstoffverbrauch (momentan) | 1.000 ms |
| 127498 | Kraftstoffverbrauch (Reise, gesamt) | 5.000 ms |
| 127505 | Tankfüllstand (Kraftstoff) | 2.500 ms |
| 127493 | Übertragungsparameter (Getriebe) | 1.000 ms |
| 65280 | Volvo Penta proprietär (erweiterte Daten) | variabel |

### 15.2 Integration mit Kartenplottern

Volvo Penta EVC2 ist kompatibel mit:
- **Garmin:** GPSMAP-Serie, automatische Motordaten-Anzeige
- **Raymarine:** Axiom-Serie, LightHouse-Integration
- **Simrad:** NSS/NSO-Serie, Motorseiten
- **B&G:** Zeus-Serie
- **Furuno:** NavNet TZtouch3

### 15.3 Volvo Penta Connect (Cloud-Monitoring)

Ab EVC2 verfügbar. Sendet Motordaten über integriertes LTE-Modul an die Volvo Penta Cloud.

**Funktionen:**
- Fernüberwachung aller Motorparameter via App (iOS/Android)
- Automatische Wartungserinnerungen
- Fehlercode-Benachrichtigungen in Echtzeit
- Geofencing (Alarmierung bei Verlassen eines Gebiets)
- Fahrtenbuch (automatisch)
- Fernzugriff für Volvo Penta Werkstatt (mit Einwilligung)

**Kosten:** Grundfunktionen kostenlos für 5 Jahre ab Motorkauf, danach 199 €/Jahr

---

## 16. Wartungsintervalle und Serviceplan

### 16.1 Übersicht Wartungsintervalle

#### D1/D2-Serie (Segelyacht-Einsatz, 200–400 h/Jahr)

| Wartungsarbeit | Erstinspektion | Intervall | Kosten (Material) |
|---------------|---------------|----------|-------------------|
| Motoröl + Filter | 50 h | 200 h oder jährlich | 45–85 € |
| Kraftstofffilter | 50 h | 400 h oder jährlich | 25–45 € |
| Kraftstoff-Vorfilter (Racor) | — | 200 h oder jährlich | 15–25 € |
| Impeller | — | 500 h oder jährlich | 35–55 € |
| Keilriemen | — | 500 h oder 2 Jahre | 18–30 € |
| Kühlmittel | — | 1.000 h oder 2 Jahre | 25–40 € |
| Ventilspiel prüfen | 500 h | 1.000 h | 0 € (Werkzeug) |
| Einspritzdüsen prüfen | — | 2.000 h | 0 € (Spezialwerkzeug) |
| Zinkanoden (Wärmetauscher) | — | Jährlich | 15–25 € |
| Thermostat | — | 3.000 h oder 5 Jahre | 45–75 € |
| Kühlwasserpumpe (See) | — | 3.000 h oder 5 Jahre | 180–320 € |
| Kühlwasserpumpe (Frisch) | — | 5.000 h | 250–450 € |

#### D3/D4/D6-Serie (Motorboot-Einsatz, 100–300 h/Jahr)

| Wartungsarbeit | Erstinspektion | Intervall | Kosten (Material) |
|---------------|---------------|----------|-------------------|
| Motoröl + Filter | 50 h | 200 h oder jährlich | 85–160 € |
| Kraftstofffilter | 50 h | 400 h oder jährlich | 45–80 € |
| Impeller | — | 500 h oder jährlich | 55–95 € |
| Zahnriemen (nur D3!) | — | 600 h oder 5 Jahre | 280–380 € (nur Material) |
| Keilriemen / Rippenriemen | — | 500 h oder 2 Jahre | 35–65 € |
| Kühlmittel | — | 1.000 h oder 2 Jahre | 45–75 € |
| Turbolader inspizieren | — | 1.000 h | 0 € (Sichtkontrolle) |
| Abgaskrümmer inspizieren | — | 1.000 h | 0 € (Sichtkontrolle) |
| Ladeluftkühler-Drucktest | — | 1.000 h oder 2 Jahre | 80–150 € (Werkstatt) |
| Ventilspiel (mechanisch) | 500 h | 1.000 h | 0 € |
| Common-Rail-Injektoren | — | 4.000 h | 350–450 € pro Stück |
| Schwingungsdämpfer | — | 5.000 h | 800–1.500 € |

### 16.2 Winterlager-Prozedur (Einwintern)

**Schritte für sachgerechtes Einwintern:**

1. **Motor warmlaufen lassen** (Betriebstemperatur erreichen, 15 min)
2. **Motoröl und Filter wechseln** (warmes Öl fließt besser, Säuren entfernen)
3. **Kraftstofftank voll füllen** (Kondenswasser vermeiden)
4. **Kraftstofffilter wechseln**
5. **Kühlsystem spülen und Frostschutz prüfen** (-20 °C Minimum für Mitteleuropa)
6. **Seewassersystem:** Seeventil schließen, Seewasserfilter reinigen, System entleeren oder Frostschutz (Propylenglykol, NICHT Ethylenglykol!) durchpumpen
7. **Impeller ausbauen** (verhindert Verformung durch monatelanges Stehen)
8. **Getriebe-/Saildrive-Öl wechseln** (Wasser im Öl? Dann sofort Dichtungen prüfen!)
9. **Zinkanoden prüfen** (>50 % vorhanden? Sonst wechseln)
10. **Kraftstoff-Absperrventil schließen**
11. **Batterie abklemmen** oder Erhaltungsladung anschließen
12. **Motor leicht mit WD-40 oder Korrosionsschutz einsprühen** (Metallteile)
13. **Auspuffanlage:** Auspufföffnung abdecken (Feuchtigkeitsschutz, kein luftdichter Verschluss!)
14. **Motorraum-Belüftung sicherstellen** (Schimmelprävention)

### 16.3 Auswintern (Saisonstart)

1. **Impeller einbauen** (neuen Impeller, wenn Saison > 500 h geplant)
2. **Seeventil öffnen**
3. **Kühlmittelstand prüfen**
4. **Motorölstand prüfen**
5. **Kraftstoff-Absperrventil öffnen**
6. **Batterien anschließen** (Spannung prüfen: >12,5V)
7. **Kraftstoffsystem entlüften** (D1/D2 mechanisch: Handpumpe am Vorfilter)
8. **Motor starten, Warmlaufen lassen** (Kühlwasseraustritt am Auspuff kontrollieren!)
9. **Alle Anzeigen prüfen** (Öldruck, Temperatur, Ladung)
10. **Probelauf unter Last** (Gang einlegen, Propellerdrehung prüfen)

---

## 17. Motoröl und Betriebsstoffe

### 17.1 Motoröl-Spezifikationen

| Motor | Spezifikation | Empfohlene Viskosität | Füllmenge |
|-------|-------------|---------------------|-----------|
| D1-Serie | VDS-3 oder ACEA E7 | 15W-40 | 1,7–3,5 l |
| D2-Serie | VDS-4.5 oder ACEA E9 | 15W-40 (10W-40 in Kälte) | 3,8–6,5 l |
| D3-Serie | VDS-4.5 oder ACEA C3 | 5W-30 | 7,5 l |
| D4-Serie | VDS-4.5 oder ACEA E9 | 10W-40 | 12 l |
| D6-Serie | VDS-4.5 oder ACEA E9 | 10W-40 | 18 l |
| D8-Serie | VDS-4.5 oder ACEA E9 | 10W-40 | 25 l |
| D11-Serie | VDS-5 | 10W-40 | 38 l |
| D13-Serie | VDS-5 | 10W-40 | 45 l |
| D16-Serie | VDS-5 | 10W-40 | 56 l |

### 17.2 Motoröl-Marken (empfohlen/geeignet)

| Marke | Produkt | VP-Freigabe | Preis (5 l) |
|-------|---------|------------|------------|
| Volvo Penta Original | VDS-4.5 15W-40 | Ja | 45–55 € |
| Shell | Rimula R6 M 10W-40 | VDS-4.5 | 38–48 € |
| Mobil | Delvac MX Extra 10W-40 | VDS-4.5 | 35–45 € |
| Castrol | Vecton Long Drain 10W-40 | VDS-4.5 | 36–46 € |
| Total | Rubia Works 2500 10W-40 | VDS-4.5 | 32–42 € |

### 17.3 Kühlmittel

**Volvo Penta Original-Kühlmittel:** grün, OAT-basiert (Organic Acid Technology)
- Mischungsverhältnis: 40–50 % Konzentrat mit destilliertem Wasser
- Frostschutz bei 50 %: -37 °C
- Wechselintervall: 1.000 h oder 2 Jahre (dann alle 2 Jahre)
- **NIEMALS verschiedene Kühlmitteltypen mischen!** (OAT ≠ Silikat ≠ Hybrid)
- Preis Kühlmittelkonzentrat (5 l): 42–55 €

### 17.4 Getriebeöl

| Anwendung | Spezifikation | Menge | Wechselintervall |
|-----------|-------------|-------|-----------------|
| Saildrive 120S/130S/150S | SAE 75W-90 Synthetic | 0,6–1,0 l | 200 h oder jährlich |
| Wendegetriebe MS10–MS25 | ATF Dexron III | 0,5–1,5 l | 500 h oder 2 Jahre |
| Wendegetriebe HS63–HS85 | SAE 30 Marine Gear Oil | 3–6 l | 500 h oder jährlich |
| IPS-Pod-Getriebe | Volvo Penta IPS Gear Oil | 3,5 l pro Pod | 200 h oder jährlich |
| Aquamatic Sterndrive | Volvo Penta Sterndrive Oil | 1,5–2,5 l | 100 h oder jährlich |

---

## 18. Kühlsystem — Aufbau und Wartung

### 18.1 Zweikreis-Kühlsystem (Standard ab D1-20)

**Kreislauf 1 (Frischwasser/intern):**
Motor → Thermostat → Frischwasserpumpe → Motorblock → Zylinderkopf → Wärmetauscher → zurück zum Motor

**Kreislauf 2 (Seewasser/extern):**
Seeventil → Seewasserfilter → Seewasserpumpe (Impeller) → Wärmetauscher → Ladeluftkühler (falls vorhanden) → Auspuffkrümmer → Nassauspuff

### 18.2 Impeller — Das Herzstück der Seewasserkühlung

| Motor | Impeller-Teilenummer | Flügel | Material | Preis (Original) | Preis (Aftermarket) |
|-------|---------------------|--------|----------|------------------|-------------------|
| D1-13 | 3586496 | 6 | Neopren | 38 € | 18–25 € |
| D1-20 | 3586496 | 6 | Neopren | 38 € | 18–25 € |
| D1-30 | 3593573 | 10 | Neopren | 45 € | 22–30 € |
| D2-40 | 3593573 | 10 | Neopren | 45 € | 22–30 € |
| D2-50 | 3593573 | 10 | Neopren | 45 € | 22–30 € |
| D2-60 | 21951346 | 12 | Neopren | 55 € | 28–35 € |
| D2-75 | 21951346 | 12 | Neopren | 55 € | 28–35 € |
| D3-Serie | 21951356 | 12 | Neopren | 65 € | 32–42 € |
| D4-Serie | 21951358 | 12 | Neopren | 78 € | 38–50 € |
| D6-Serie | 21951358 | 12 | Neopren | 78 € | 38–50 € |

**Impeller-Wechselintervall:** 500 Stunden oder jährlich (was zuerst eintritt)

**Tipp:** Immer einen Ersatz-Impeller an Bord haben! Ein defekter Impeller = keine Kühlung = Motorschaden in Minuten.

### 18.3 Thermostat

| Motor | Öffnungstemperatur | Voll offen | Preis (Original) |
|-------|-------------------|-----------|------------------|
| D1-Serie | 71 °C | 85 °C | 45 € |
| D2-Serie | 82 °C | 95 °C | 55 € |
| D3-Serie | 87 °C | 102 °C | 75 € |
| D4/D6-Serie | 83 °C | 97 °C | 85 € |

### 18.4 Wärmetauscher

Der Wärmetauscher überträgt Wärme vom Frischwasserkreislauf auf den Seewasserkreislauf. Typische Lebensdauer: 3.000–5.000 h.

**Häufige Probleme:**
- **Verkalkung:** Reduziert Kühlleistung. Reinigung mit Zitronensäure (5 %) oder HCl (10 %) möglich
- **Zinkanode im Wärmetauscher:** Muss jährlich geprüft werden! Verhindert galvanische Korrosion
- **Undichtigkeit:** Röhrchen korrodieren, Seewasser gelangt in Frischwasserkreislauf (milchige Kühlflüssigkeit)

**Austausch-Kosten Wärmetauscher:**
- D1/D2: 450–750 €
- D3: 800–1.200 €
- D4/D6: 1.200–2.000 €

---

## 19. Kraftstoffsystem und Dieselqualität

### 19.1 Kraftstoffanforderungen

Volvo Penta empfiehlt:
- Diesel nach EN 590 (Europa) oder ASTM D975 (USA)
- Schwefelgehalt max. 10 ppm (ULSD — Ultra Low Sulfur Diesel)
- Kein Bio-Diesel > B7 (7 % Bio-Anteil) ohne Freigabe
- Kein Heizöl (HEL) — fehlende Additive, höherer Schwefel

### 19.2 Dieselpest (Mikrobiologische Kontamination)

**Was ist Dieselpest?**
Bakterien und Pilze (insbes. Hormoconis resinae) wachsen an der Grenzschicht Diesel/Wasser im Tank. Sie bilden Biofilme und Schleim, der Filter und Einspritzdüsen verstopft.

**Symptome:**
- Kraftstofffilter verstopft nach kurzer Zeit
- Schwarzer oder brauner Schleim im Filter
- Motor ruckelt, Leistungsverlust
- Übelriechender Kraftstoff (nach faulen Eiern)

**Prävention:**
1. Tank immer voll halten (weniger Kondenswasser)
2. Wasserabscheider (Racor) mit Wasserablassventil verwenden
3. Regelmäßig Wasser aus dem Tank ablassen
4. Biozid-Additiv verwenden: Grotamar 82 (1:4.000 Verdünnung)
5. Tankinnenbeschichtung (Epoxid) alle 10–15 Jahre prüfen

**Behandlung bei Befall:**
1. Tank entleeren und mechanisch reinigen
2. Alle Filter wechseln
3. Neue Kraftstoffschläuche
4. Tank mit Biozid behandeln
5. Neuen Diesel einfüllen

**Kosten Dieselpest-Sanierung:** 800–2.500 € (je nach Tankgröße und Verschmutzungsgrad)

### 19.3 Kraftstofffilter-System

**Zweistufige Filterung (Volvo Penta Standard):**

| Stufe | Filter | Porengröße | Funktion | Wechselintervall |
|-------|--------|-----------|---------|-----------------|
| 1. Vorfilter | Racor Turbine 500FG/900 | 30 µm + Wasserabscheider | Grobe Partikel + Wasser | 200 h oder jährlich |
| 2. Hauptfilter | VP Original Kraftstofffilter | 5–10 µm | Feine Partikel | 400 h oder jährlich |

### 19.4 Kraftstoffverbrauch-Richtwerte

| Motor | Leerlauf (l/h) | 50 % Last (l/h) | 75 % Last (l/h) | Volllast (l/h) |
|-------|----------------|-----------------|-----------------|----------------|
| D1-13 | 0,4 | 1,5 | 2,6 | 3,5 |
| D1-20 | 0,5 | 2,2 | 4,1 | 5,5 |
| D1-30 | 0,6 | 3,5 | 6,2 | 8,2 |
| D2-40 | 0,8 | 4,5 | 7,5 | 10,2 |
| D2-50 | 0,9 | 5,5 | 9,5 | 12,8 |
| D2-60 | 1,0 | 6,8 | 11,6 | 15,4 |
| D2-75 | 1,2 | 8,0 | 14,0 | 18,5 |
| D3-110 | 1,5 | 12,0 | 18,0 | 28,0 |
| D3-220 | 2,0 | 20,0 | 34,0 | 55,0 |
| D4-300 | 2,5 | 25,0 | 42,0 | 72,0 |
| D6-440 | 3,5 | 35,0 | 58,0 | 95,0 |

---

## 20. Bekannte Schwachstellen und typische Probleme

### 20.1 Saildrive-Membran (ALLE Saildrive-Modelle)

**Schweregrad:** KRITISCH
**Betrifft:** 120S, 130S, 150S — alle Baujahre
**Problem:** Die EPDM-Gummimembran altert durch UV-Strahlung, Ozon und mechanische Belastung. Nach 7–15 Jahren kann sie reißen → Wassereinbruch → Sinken des Bootes.
**Symptome:** Risse sichtbar bei Haul-out, verhärtete Oberfläche, Wasser in der Bilge
**Lösung:** Präventiver Austausch alle 7–10 Jahre. Jährliche Inspektion bei Haul-out.
**Kosten:** 770–1.215 € (siehe Abschnitt 10.5)
**Confidence:** measured (Herstellerangabe 7 Jahre), documented (Praxiserfahrung 10–15 Jahre)

### 20.2 D2-75 Turbolader-Undichtigkeit

**Schweregrad:** MITTEL
**Betrifft:** D2-75, insbesondere Baujahre 2014–2019 (mechanische Einspritzung)
**Problem:** Turbolader-Wellendichtung verschleißt ab ca. 2.500–3.500 h. Öl gelangt in den Ladelufttrakt → blauer Rauch, erhöhter Ölverbrauch.
**Symptome:** Bläulicher Abgasrauch (insbes. beim Beschleunigen), Ölverbrauch > 0,3 l / 100 h, Öl im Ladeluftschlauch
**Lösung:** Turbolader-Überholung oder -Austausch
**Kosten:** Überholung: 1.200–1.800 €, Austausch: 2.500–3.800 €
**Confidence:** documented (VP Service Bulletin, Werftberichte)

### 20.3 D3-Serie Zahnriemenriss

**Schweregrad:** KRITISCH
**Betrifft:** Alle D3-Motoren (D3-110 bis D3-220)
**Problem:** Der Zahnriemen treibt die Nockenwellen an. Bei Riss schlagen Ventile gegen Kolben → Totalschaden des Motors. Wechselintervall: 600 h oder 5 Jahre.
**Symptome:** Keine Vorwarnung! Plötzlicher Motorstillstand.
**Lösung:** Striktes Einhalten des Wechselintervalls. Bei Gebrauchtboot-Kauf: Nachweis des letzten Wechsels verlangen!
**Kosten:** Zahnriemenwechsel: 1.200–1.800 €. Motorschaden nach Riss: 8.000–15.000 € (oft wirtschaftlicher Totalschaden)
**Confidence:** measured (Herstellerangabe 600 h / 5 Jahre)

### 20.4 Kühlmittelmischung (ALLE Motoren)

**Schweregrad:** MITTEL–HOCH
**Betrifft:** Alle Motoren mit Zweikreiskühlung
**Problem:** Vermischung verschiedener Kühlmitteltypen (OAT + Silikat) führt zu Gelbildung → Verstopfung von Kühlkanälen → lokale Überhitzung → Zylinderkopfdichtung.
**Symptome:** Gelartige Ablagerungen im Ausgleichsbehälter, erhöhte Motortemperatur, Kühlmittel wird trüb
**Lösung:** Ausschließlich Volvo Penta Original-Kühlmittel oder freigegebene Alternative verwenden. Bei unbekanntem Kühlmittel: System komplett spülen und neu befüllen.
**Kosten:** Spülung + Neubefüllung: 150–350 €. Zylinderkopfdichtung nach Überhitzung: 2.500–5.000 €
**Confidence:** documented (VP Service Bulletin)

### 20.5 Abgaskrümmer-Korrosion (D3, D4, D6)

**Schweregrad:** HOCH
**Betrifft:** D3, D4, D6 mit Nassauspuff
**Problem:** Der wassergekühlte Abgaskrümmer ist extremer thermischer und chemischer Belastung ausgesetzt. Seewasser-seitige Korrosion kann zum Durchbruch führen → Seewasser im Zylinder.
**Symptome:** Weiße Kristallablagerungen am Krümmer, Undichtigkeit, weißer Rauch, Kühlwasserverlust
**Lösung:** Regelmäßige Inspektion (1.000 h), präventiver Austausch nach 2.000–3.000 h
**Kosten:** D3: 2.200–3.500 €, D4: 3.000–4.500 €, D6: 4.000–6.000 €
**Confidence:** documented (Werkstattberichte, VP Service Bulletin)

### 20.6 Ladeluftkühler-Undichtigkeit (D4, D6)

**Schweregrad:** KRITISCH
**Betrifft:** D4, D6 alle Baujahre
**Problem:** Der seewassergekühlte Ladeluftkühler kann korrodieren. Seewasser gelangt über den Ladelufttrakt in die Zylinder → Wasserschlag → Motorschaden.
**Symptome:** Weißer Rauch, Kühlwasserverlust ohne sichtbares Leck, Leistungsverlust, Wasser im Ladeluftschlauch
**Lösung:** Jährlicher Drucktest des Ladeluftkühlers. Austausch bei Undichtigkeit.
**Kosten:** Drucktest: 80–150 €, Austausch: 3.500–5.500 €
**Confidence:** documented (VP Service Bulletin, zahlreiche Werkstattberichte)

### 20.7 IPS-Pod-Korrosion

**Schweregrad:** HOCH
**Betrifft:** Alle IPS-Systeme, insbesondere Salzwasser
**Problem:** Aluminium-Pod-Gehäuse korrodiert bei unzureichendem Anodenschutz
**Symptome:** Weiße Korrosionsprodukte (Aluminiumoxid) am Pod, Lochfraß
**Lösung:** Zinkanoden 2× pro Saison prüfen und bei >50 % Abtrag wechseln. Korrekt spezifiziertes Antifouling (kein Kupfer auf Aluminium!)
**Kosten:** Anoden: 180–350 €/Saison, Pod-Gehäuse-Reparatur: 8.000–15.000 €
**Confidence:** documented (VP Service Bulletin, IPS-Werkstattberichte)

### 20.8 EVC-Kommunikationsfehler

**Schweregrad:** MITTEL
**Betrifft:** EVC-A und EVC-B Systeme (1999–2018)
**Problem:** Korrodierte CAN-Bus-Steckverbindungen im Motorraum führen zu sporadischen Kommunikationsfehlern
**Symptome:** Intermittierende Fehlermeldungen, Motor geht in Notlauf, Anzeigen fallen aus
**Lösung:** Alle Steckverbindungen reinigen, mit Kontaktfett behandeln, korrodierte Kabel ersetzen
**Kosten:** Diagnose + Reparatur: 200–800 €
**Confidence:** documented (Werkstattberichte)

### 20.9 Aquamatic-Faltenbälge (ALLE Sterndrive-Modelle)

**Schweregrad:** KRITISCH
**Betrifft:** SX-A, DPS-A, DPH-A, DPH-D
**Problem:** Gummi-Faltenbälge (Abgas, Lenkung, Trimmzylinder) altern und können reißen → Wassereinbruch
**Symptome:** Risse bei Inspektion sichtbar, Wasser in der Bilge
**Lösung:** Austausch alle 3–5 Jahre, jährliche Inspektion
**Kosten:** Bellows-Satz komplett: 350–550 €, Einbau: 500–1.000 €
**Confidence:** measured (Herstellerangabe), documented (Praxiserfahrung)

### 20.10 Common-Rail-Injektor-Defekte (D2 ab 2019, D3, D4, D6)

**Schweregrad:** MITTEL
**Betrifft:** Alle Common-Rail-Motoren
**Problem:** Injektoren sind empfindlich gegen verunreinigten Diesel (Wasser, Dieselpest, Partikel). Defekte Injektoren führen zu Leistungsverlust, Rußbildung und erhöhtem Verbrauch.
**Symptome:** Unrunder Motorlauf, schwarzer Rauch, Leistungsverlust, erhöhter Verbrauch
**Lösung:** Dieselqualität sicherstellen (EN 590), Vorfilter mit Wasserabscheider verwenden, Injektoren bei 4.000 h prüfen
**Kosten:** Pro Injektor: 350–550 €, 4-Zylinder-Satz: 1.400–2.200 €
**Confidence:** documented (VP Service Bulletin, Werkstattberichte)

---

## 21. Fehlerbild-Atlas

### Fehlerbild 1: Motor springt nicht an

**Beschreibung:** Anlasser dreht, aber Motor zündet nicht
**Mögliche Ursachen:**
- Luft im Kraftstoffsystem (häufigste Ursache)
- Kraftstofffilter verstopft
- Kraftstofftank leer
- Kraftstoff-Absperrventil geschlossen
- Glühkerzen defekt (nur D1-Serie)
- Einspritzdüsen defekt
- Kompression zu niedrig

**Diagnoseschritte:**
1. Tankfüllstand prüfen
2. Kraftstoff-Absperrventil prüfen
3. Vorfilter (Racor) auf Wasser/Verschmutzung prüfen
4. Kraftstoffsystem entlüften
5. Kraftstofffilter wechseln
6. Glühkerzen prüfen (D1: Widerstandsmessung, 0,5–1,0 Ω)
7. Kompression messen (min. 25 bar bei D1/D2)

### Fehlerbild 2: Motor überhitzt

**Beschreibung:** Kühlmitteltemperatur steigt über 100 °C, Alarm
**Mögliche Ursachen:**
- Impeller defekt (häufigste Ursache!)
- Seeventil geschlossen oder verstopft
- Seewasserfilter verstopft (Muscheln, Seegras)
- Thermostat klemmt (geschlossen)
- Keilriemen gerissen (Frischwasserpumpe)
- Wärmetauscher verkalkt/verstopft
- Kühlmittelverlust (Leck)

**Diagnoseschritte:**
1. Seewasseraustritt am Auspuff prüfen — kein Wasser = Seewasserseite!
2. Seeventil offen?
3. Seewasserfilter reinigen
4. Impeller prüfen (Deckel öffnen, Impeller sichtbar)
5. Keilriemen prüfen
6. Kühlmittelstand prüfen
7. Thermostat prüfen (ausbauen, in heißes Wasser legen)

### Fehlerbild 3: Motor raucht schwarz

**Beschreibung:** Schwarzer (rußiger) Abgasrauch
**Mögliche Ursachen:**
- Luftfilter verschmutzt
- Turbolader defekt / VGT klemmt
- Injektoren defekt (schlechte Zerstäubung)
- Überlast (zu großer Propeller)
- Ladeluftkühler undicht oder verstopft

**Diagnoseschritte:**
1. Luftfilter prüfen/wechseln
2. Turbolader-Sichtprüfung (Spiel, Öl am Einlass)
3. Ladedruck prüfen (Manometer oder EVC)
4. Propellercheck: Bewuchs? Richtige Steigung?
5. Injektoren prüfen lassen (Werkstatt)

### Fehlerbild 4: Motor raucht weiß

**Beschreibung:** Weißer oder grau-weißer Abgasrauch
**Mögliche Ursachen:**
- Wasser im Zylinder (Abgaskrümmer undicht, Ladeluftkühler undicht)
- Zylinderkopfdichtung defekt
- Motor zu kalt (Thermostat klemmt offen)
- Einspritzzeitpunkt verstellt (ältere mechanische Motoren)

**Diagnoseschritte:**
1. Kühlmittelstand prüfen (Verlust ohne sichtbares Leck?)
2. Motoröl prüfen (milchig = Wasser im Öl!)
3. Abgaskrümmer visuell prüfen (weiße Kristalle?)
4. Ladeluftkühler-Drucktest
5. Kompressionstest (Unterschiede zwischen Zylindern?)

### Fehlerbild 5: Motor raucht blau

**Beschreibung:** Bläulicher Abgasrauch, öliger Geruch
**Mögliche Ursachen:**
- Turbolader-Wellendichtung undicht (Öl in Ladeluft)
- Ventilschaftdichtungen verschlissen
- Kolbenringe verschlissen (hohe Betriebsstunden)
- Zu hoher Ölstand

**Diagnoseschritte:**
1. Ölstand prüfen (zu hoch?)
2. Ölverbrauch messen (>0,5 l / 100 h = auffällig)
3. Turbolader-Einlass prüfen (Öl sichtbar?)
4. Kompressionstest
5. Leckgas-Test (Blow-by-Messung)

### Fehlerbild 6: Motor läuft unrund / vibriert

**Beschreibung:** Ungleichmäßiger Motorlauf, Vibrationen
**Mögliche Ursachen:**
- Injektor defekt (ein Zylinder zündet nicht richtig)
- Luft im Kraftstoffsystem
- Kraftstoffqualität (Wasser im Diesel)
- Motorlager verschlissen
- Propellerunwucht
- Flexible Kupplung verschlissen

**Diagnoseschritte:**
1. Fehlercodes auslesen (EVC)
2. Kraftstofffilter prüfen
3. Zylinder-Abschalttest (Werkstatt: einzelne Injektoren deaktivieren)
4. Motorlager visuell prüfen
5. Propeller auf Unwucht/Beschädigung prüfen

### Fehlerbild 7: Öldruckverlust

**Beschreibung:** Öldruck-Warnung, niedriger Öldruck
**Mögliche Ursachen:**
- Ölstand zu niedrig
- Ölfilter verstopft
- Ölpumpe verschlissen
- Lagerverschleiß (hohe Laufleistung)
- Öldrucksensor defekt

**Diagnoseschritte:**
1. **Motor sofort abstellen!**
2. Ölstand prüfen (Peilstab)
3. Ölfilter wechseln
4. Öldruck mit externem Manometer messen
5. Öldrucksensor prüfen/tauschen

### Fehlerbild 8: Getriebe schaltet nicht / schaltet schwer

**Beschreibung:** Gang lässt sich nicht einlegen oder harter Schaltvorgang
**Mögliche Ursachen:**
- Schaltzug festgefressen (Korrosion)
- Getriebeöl zu wenig oder falsche Spezifikation
- Kupplungsscheiben verschlissen
- Schaltventil klemmt (hydraulisches Getriebe)
- EVC-Schaltaktuator defekt

**Diagnoseschritte:**
1. Schaltzug auf Leichtgängigkeit prüfen
2. Getriebeölstand und -zustand prüfen
3. EVC-Fehlercodes auslesen
4. Schaltzug schmieren oder tauschen
5. Getriebe-Werkstatt konsultieren

### Fehlerbild 9: Wasser in der Bilge (Saildrive)

**Beschreibung:** Erhöhter Wasserstand in der Bilge am Saildrive
**Mögliche Ursachen:**
- Saildrive-Membran undicht
- Saildrive-Wellendichtring undicht
- Saildrive-Gehäuse korrodiert (Lochfraß)
- Schlauchschellen an Membran locker

**Diagnoseschritte:**
1. Boot aus dem Wasser holen (Haul-out — wenn ernster Verdacht sofort!)
2. Membran von außen und innen inspizieren
3. Wellendichtring prüfen (Öl oder Wasser am Schaft?)
4. Gehäuse auf Korrosion prüfen
5. Schlauchschellen nachziehen oder erneuern

### Fehlerbild 10: Übermäßiger Kraftstoffverbrauch

**Beschreibung:** Kraftstoffverbrauch deutlich über Soll
**Mögliche Ursachen:**
- Propellerbewuchs (häufigste Ursache!)
- Rumpfbewuchs erhöht Widerstand
- Injektoren undicht / schlechte Zerstäubung
- Turbolader defekt (zu wenig Ladedruck)
- Falscher Propeller (zu große Steigung)

**Diagnoseschritte:**
1. Propeller und Rumpf reinigen
2. Motordrehzahl bei Volllast prüfen (Nenndrehzahl erreicht? Nein = Überlast)
3. Injektoren prüfen lassen
4. Ladedruck prüfen
5. Propellerberechnung überprüfen

### Fehlerbild 11: EVC-Fehlermeldung / Notlauf

**Beschreibung:** Motor geht in Notlauf, Drehzahl begrenzt auf 1.500–2.000 U/min
**Mögliche Ursachen:**
- Sensordefekt (Temperatur, Druck, Drehzahl)
- CAN-Bus-Fehler (korrodierte Steckverbindungen)
- ECU-Softwarefehler
- Echter Motorfehler (Überhitzung, Öldruck)

**Diagnoseschritte:**
1. Fehlercodes auslesen (EVC-Display oder VODIA)
2. Prüfen ob echter Fehler vorliegt (Temperatur, Öldruck, Kühlmittel)
3. Steckverbindungen im Motorraum prüfen
4. CAN-Bus-Abschlusswiderstand prüfen (120 Ω an beiden Enden)
5. Bei Sensordefekt: Sensor tauschen, Fehlerspeicher löschen

### Fehlerbild 12: Starke Vibrationen bei bestimmter Drehzahl

**Beschreibung:** Resonanzvibration bei bestimmter Motordrehzahl
**Mögliche Ursachen:**
- Propellerbeschädigung (Blatt verbogen)
- Wellenunwucht
- Motorlager ausgehärtet/gerissen
- Flexible Kupplung defekt
- Schwingungsdämpfer (Crankshaft Damper) verschlissen

**Diagnoseschritte:**
1. Propeller inspizieren (alle Blätter gleichmäßig?)
2. Motorlager visuell prüfen (Risse? Verhärtung? Absackung?)
3. Flexible Kupplung prüfen (Gummi intakt?)
4. Motor neutral laufen lassen — Vibration auch ohne Gang? Dann Motor, nicht Antriebsstrang
5. Bei Unwucht: Propeller auswuchten lassen (Werft)

---

## 22. Troubleshooting-Entscheidungsbäume

### Baum 1: Motor springt nicht an

```
Motor springt nicht an
├── Anlasser dreht?
│   ├── NEIN → Batterie prüfen (>12,2V?)
│   │   ├── Batterie OK → Anlasser / Startrelais / Zündschloss
│   │   └── Batterie leer → Laden / Starthilfe
│   └── JA → Motor dreht, zündet nicht
│       ├── Kraftstoff vorhanden?
│       │   ├── NEIN → Tanken!
│       │   └── JA → Kraftstoffzufuhr prüfen
│       │       ├── Vorfilter sauber? → Wenn verschmutzt: wechseln
│       │       ├── Hauptfilter sauber? → Wenn verschmutzt: wechseln
│       │       ├── Luft im System? → Entlüften (Handpumpe D1/D2)
│       │       ├── Absperrventil offen? → Öffnen
│       │       └── Alles OK → Glühkerzen (D1) / Injektoren / Kompression
│       └── Motor dreht zu langsam
│           └── Batterie schwach / Anlasser defekt / Motoröl zu dickflüssig
```

### Baum 2: Motor überhitzt

```
Motor überhitzt (>100°C Kühlmittel)
├── Seewasser kommt am Auspuff?
│   ├── NEIN → Seewasserseite defekt
│   │   ├── Seeventil offen? → Öffnen
│   │   ├── Seewasserfilter sauber? → Reinigen
│   │   ├── Impeller intakt? → Alle Flügel vorhanden? Tauschen!
│   │   └── Seewasserleitung verstopft? → Durchspülen
│   └── JA → Frischwasserseite oder Wärmetauscher
│       ├── Kühlmittelstand OK? → Wenn niedrig: auffüllen, Leck suchen
│       ├── Keilriemen intakt? → Wenn gerissen: ersetzen
│       ├── Thermostat OK? → Prüfen (in heißem Wasser öffnen?)
│       └── Wärmetauscher verstopft? → Drucktest / Reinigung
```

### Baum 3: Abnormaler Rauch

```
Abnormaler Abgasrauch
├── SCHWARZ → Kraftstoff wird nicht vollständig verbrannt
│   ├── Luftfilter verschmutzt? → Reinigen / Tauschen
│   ├── Turbolader OK? → Ladedruck prüfen
│   ├── Injektoren OK? → Zerstäubung prüfen lassen
│   └── Überlast? → Propeller / Rumpfbewuchs prüfen
├── WEISS → Wasser oder unverbrannter Kraftstoff
│   ├── Kurz nach Kaltstart? → Normal (Kondensation)
│   ├── Dauerhaft? → Wasser im Zylinder!
│   │   ├── Kühlmittelverlust? → Kopfdichtung / Krümmer / LLK
│   │   └── Kein Kühlmittelverlust → Einspritzzeitpunkt (mech. Motor)
│   └── Grau-weiß + Dieselgeruch → Motor zu kalt (Thermostat)
└── BLAU → Öl verbrennt mit
    ├── Ölverbrauch erhöht? → JA
    │   ├── Turbo-Wellendichtung? → Öl im Ladeluftschlauch prüfen
    │   ├── Ventilschaftdichtungen? → Bei kaltem Motor stärker
    │   └── Kolbenringe? → Kompressionstest + Leckgas-Test
    └── Ölstand zu hoch? → Auf korrekten Stand bringen
```

### Baum 4: Getriebe/Antrieb Probleme

```
Getriebe/Antrieb Probleme
├── Gang lässt sich nicht einlegen
│   ├── Mechanische Steuerung → Schaltzug prüfen (Leichtgängigkeit)
│   ├── EVC-Steuerung → Fehlercodes auslesen, Aktuator prüfen
│   └── Getriebeöl OK? → Stand und Zustand prüfen
├── Knirschgeräusch beim Schalten
│   ├── Drehzahl beim Schalten zu hoch? → Leerlauf abwarten
│   └── Kupplungsscheiben verschlissen → Getriebe-Service
├── Kein Vortrieb trotz eingelegtem Gang
│   ├── Propeller frei? → Leine im Propeller?
│   ├── Kupplung rutscht? → Getriebeöl prüfen, Getriebe-Service
│   └── Propellerwelle: Stift abgeschert? → Propellersitz prüfen
└── Vibration im Antriebsstrang
    ├── Propeller beschädigt? → Inspektion
    ├── Flexible Kupplung? → Gummielemente prüfen
    └── Kardangelenk (Aquamatic)? → Spiel prüfen
```

### Baum 5: Elektrische Probleme

```
Elektrische Probleme
├── Batterie lädt nicht
│   ├── Keilriemen intakt und gespannt? → Prüfen
│   ├── Lichtmaschine funktioniert? → Spannung messen (>13,5V bei laufendem Motor)
│   ├── Laderegler defekt? → Lichtmaschine prüfen lassen
│   └── Batterie defekt? → Kapazitätstest
├── EVC-Display dunkel
│   ├── Sicherung OK? → Prüfen
│   ├── Hauptschalter ein? → Prüfen
│   └── Kabelverbindung? → Stecker prüfen
├── Anlasser dreht nicht
│   ├── Zündschloss OK? → Prüfen
│   ├── Neutral-Sicherheitsschalter? → Gang auf Neutral
│   ├── Startrelais? → Klickt es? Relais prüfen
│   └── Anlasser festgefressen? → Leicht gegen Gehäuse klopfen (Notfall!)
└── Intermittierende Fehler
    ├── Korrosion an Steckverbindungen? → Reinigen + Kontaktfett
    ├── Massekabel OK? → Motor-zu-Rumpf-Masse prüfen
    └── CAN-Bus-Abschlusswiderstand? → 120 Ω an beiden Enden
```

---

## 23. Ersatzteile — Original vs. Aftermarket

### 23.1 Original Volvo Penta (OEM)

**Vorteile:**
- Garantierte Passform und Funktion
- Werkstattgarantie bleibt erhalten
- VP-Seriennummer-Zuordnung (richtige Teile für richtige Motorversion)
- Qualitätskontrolle durch Volvo

**Nachteile:**
- Deutlich teurer als Aftermarket (oft 40–200 % Aufpreis)
- Teilweise identische Teile mit anderem Aufdruck (z. B. Impeller, Filter)

### 23.2 Aftermarket-Hersteller

| Hersteller | Produkte | Qualität | Preisvorteil vs. VP |
|-----------|---------|---------|-------------------|
| Orbitrade (Schweden) | Dichtungen, Filter, Impeller, Kühlwasserteile | Hoch — VP-Zulieferer | 30–50 % |
| RecMar (Spanien) | Filter, Impeller, Zinkanoden | Gut | 40–60 % |
| Osculati (Italien) | Zinkanoden, Impeller | Gut | 40–60 % |
| SKF (Schweden) | Lager, Dichtungen, Riemen | Hoch — OEM-Qualität | 20–40 % |
| Bosch (Deutschland) | Injektoren, Glühkerzen, Filter | Hoch — VP-Zulieferer | 10–30 % |
| Mann-Filter (Deutschland) | Öl-, Kraftstoff-, Luftfilter | Hoch — VP-Zulieferer | 20–40 % |
| Gates (Belgien) | Keilriemen, Zahnriemen | Hoch — VP-Zulieferer | 20–30 % |
| Johnson Pump (Schweden) | Impeller | Hoch — VP-Zulieferer | 30–50 % |
| Sierra Marine (USA) | Impeller, Filter, Zinkanoden | Gut | 40–60 % |
| Jabsco (USA/UK) | Impeller, Pumpen | Hoch | 20–40 % |

### 23.3 Ersatzteil-Empfehlung nach Kategorie

| Kategorie | Empfehlung | Begründung |
|-----------|-----------|-----------|
| Impeller | Aftermarket OK (Orbitrade, Johnson) | Identisches Produkt, jährlicher Wechsel |
| Öl-/Kraftstofffilter | Aftermarket OK (Mann, Bosch) | Oft VP-Zulieferer-Produkt |
| Zinkanoden | Aftermarket OK (Osculati, RecMar) | Standardprodukt |
| Keilriemen | Aftermarket OK (Gates) | VP-Zulieferer |
| Saildrive-Membran | NUR ORIGINAL VP | Sicherheitsrelevant, kein Risiko eingehen |
| Turbolader | NUR ORIGINAL VP oder BorgWarner | Präzisionskomponente |
| Common-Rail-Injektoren | NUR ORIGINAL VP oder Bosch | Präzisionskomponente, Abstimmung |
| EVC-Elektronik | NUR ORIGINAL VP | Proprietäre Software |
| Zahnriemen (D3) | ORIGINAL VP oder Gates | Sicherheitsrelevant |
| Dichtungssätze | Aftermarket OK (Orbitrade) | Gute Qualität, große Ersparnis |

### 23.4 Bezugsquellen

| Quelle | Typ | Vorteile | URL-Hinweis |
|--------|-----|---------|------------|
| SVB (Bremen) | Fachhändler | Große Auswahl, schneller Versand DE | svb-marine.de |
| Compass24 | Fachhändler | Günstig, breites Sortiment | compass24.de |
| Toplicht (Hamburg) | Fachhändler | Persönliche Beratung, Lager | toplicht.de |
| Bootsteile24 | Online-Shop | Aftermarket-Spezialist | bootsteile24.de |
| Volvo Penta Dealer | OEM | Original, Garantie | volvopenta.com |
| Orbitrade Direct | Aftermarket | Direkt vom Hersteller | orbitrade.com |

---

## 24. Preise und Kostenübersicht

### 24.1 Neumotor-Preise (2025, inkl. MwSt.)

| Motor | Nur Motor | Mit Saildrive | Mit IPS | Mit Aquamatic |
|-------|----------|--------------|---------|--------------|
| D1-13 | 7.800 € | 12.200 € (120S) | — | — |
| D1-20 | 9.500 € | 13.800 € (120S) | — | — |
| D1-30 | 11.200 € | 16.500 € (130S) | — | — |
| D2-40 | 14.500 € | 20.800 € (130S) | — | — |
| D2-50 | 16.800 € | 23.500 € (130S) | — | — |
| D2-60 | 19.500 € | 27.200 € (150S) | — | — |
| D2-75 | 22.800 € | 31.500 € (150S) | — | — |
| D3-110 | 22.500 € | — | — | 28.500 € (SX-A) |
| D3-150 | 26.000 € | — | — | 33.200 € |
| D3-170 | 29.000 € | — | — | 36.500 € |
| D3-220 | 34.000 € | — | — | 42.000 € |
| D4-260 | 42.000 € | — | 52.000 € (IPS400) | 48.000 € (DPH-A) |
| D4-300 | 46.000 € | — | 58.000 € (IPS400) | 52.000 € (DPH-A) |
| D6-310 | 55.000 € | — | 68.000 € (IPS500) | — |
| D6-340 | 58.000 € | — | 72.000 € (IPS500) | — |
| D6-380 | 62.000 € | — | 78.000 € (IPS600) | 72.000 € (DPH-D) |
| D6-440 | 68.000 € | — | 85.000 € (IPS600) | 78.000 € (DPH-D) |

### 24.2 Jährliche Wartungskosten (Durchschnitt)

| Motor | Betriebsstunden/Jahr | Material/Jahr | Arbeitskosten/Jahr | Gesamt/Jahr |
|-------|---------------------|-------------|-------------------|------------|
| D1-13 | 200 | 120 € | 200 € | 320 € |
| D1-20 | 250 | 140 € | 250 € | 390 € |
| D1-30 | 300 | 165 € | 280 € | 445 € |
| D2-40 | 300 | 185 € | 320 € | 505 € |
| D2-50 | 300 | 200 € | 350 € | 550 € |
| D2-60 | 350 | 220 € | 380 € | 600 € |
| D2-75 | 350 | 250 € | 420 € | 670 € |
| D3-Serie | 200 | 350 € | 550 € | 900 € |
| D4-Serie | 200 | 480 € | 750 € | 1.230 € |
| D6-Serie | 200 | 620 € | 950 € | 1.570 € |
| D8-Serie | 200 | 850 € | 1.200 € | 2.050 € |

### 24.3 Typische Reparaturkosten (2025)

| Reparatur | Kosten inkl. Einbau | Betrifft |
|-----------|---------------------|---------|
| Impeller-Wechsel | 120–250 € | Alle |
| Saildrive-Membran | 770–1.215 € | 120S/130S/150S |
| Zahnriemenwechsel | 1.200–1.800 € | D3-Serie |
| Turbolader-Überholung | 1.200–1.800 € | D2-75, D3, D4, D6 |
| Turbolader-Austausch | 2.500–5.000 € | D2-75, D3, D4, D6 |
| Abgaskrümmer-Austausch | 2.200–6.000 € | D3, D4, D6 |
| Ladeluftkühler-Austausch | 3.500–5.500 € | D4, D6 |
| Wärmetauscher-Austausch | 450–2.000 € | Alle Zweikreis |
| Injektor-Austausch (1 St.) | 450–650 € | D2 CR, D3, D4, D6 |
| Zylinderkopfdichtung | 2.500–5.000 € | Alle |
| IPS-Pod großer Service | 3.500–6.500 € | IPS-Systeme |
| IPS-Pod-Gehäuse-Reparatur | 8.000–15.000 € | IPS-Systeme |
| Aquamatic-Bellows komplett | 800–1.500 € | Sterndrive |
| Aquamatic-Gimbal-Lager | 1.200–2.000 € | Sterndrive |
| Motor-Generalüberholung D1/D2 | 4.000–8.000 € | D1, D2 |
| Motor-Generalüberholung D4/D6 | 12.000–25.000 € | D4, D6 |
| EVC-ECU Austausch | 3.800–5.200 € | EVC-Systeme |

### 24.4 Gebrauchtmotor-Richtwerte

| Motor | Baujahr | Betriebsstunden | Preis (2025) |
|-------|---------|----------------|-------------|
| D1-30 | 2010–2015 | 500–1.500 h | 3.500–6.000 € |
| D1-30 | 2015–2020 | 300–1.000 h | 5.500–8.000 € |
| D2-40 | 2014–2019 | 500–1.500 h | 5.000–9.000 € |
| D2-75 | 2019–2023 | 300–800 h | 12.000–16.000 € |
| D3-170 | 2010–2018 | 300–1.000 h | 10.000–18.000 € |
| D4-260 | 2015–2020 | 500–1.500 h | 18.000–28.000 € |
| D6-340 | 2015–2020 | 500–1.500 h | 25.000–38.000 € |

**Achtung bei Gebrauchtkauf:**
- Betriebsstundenstand kann manipuliert sein! Serviceheft und Rechnungen verlangen
- Bei Saildrive: Membran-Alter und letzten Wechsel dokumentiert?
- Bei D3: Zahnriemen-Wechsel nachgewiesen?
- Kompressionstest durchführen (alle Zylinder innerhalb 10 % Abweichung)
- Ölanalyse (Schmierstofflabor) zeigt versteckten Verschleiß

---

## 25. Fallstudien

### Fallstudie 1: Bavaria 40 Cruiser — Saildrive-Membran-Versagen

**Boot:** Bavaria 40 Cruiser, Baujahr 2012
**Motor:** Volvo Penta D2-40 mit 130S Saildrive
**Betriebsstunden:** 1.850 h
**Membranfirst-Alter:** 12 Jahre (nie gewechselt)
**Vorfall:** Eigner bemerkt bei Routinecheck vor Saisonstart 2024 feuchte Bilge im Motorraum. Kein sichtbares Leck an Schläuchen oder Seewassersystem. Boot wird auf den Kran genommen. Membran zeigt tiefe Rissbildung auf der Unterseite (Seewasserseite).
**Befund:** Membran extrem verhärtet, Elastizität verloren. Risse bis zu 8 mm tief. Wassereinbruch war langsam (Sickerwasser), aber stetig.
**Maßnahme:** Membrantausch (480 €), neue Schlauchschellen (45 €), neue Zinkanoden (52 €), 4 h Werftarbeitszeit à 110 €/h (440 €). Gesamt: 1.017 €
**Lektion:** Membran nach 10 Jahren IMMER wechseln. Jährliche Inspektion bei Haul-out.
**Confidence:** documented

### Fallstudie 2: Nimbus 305 — D3-170 Zahnriemenriss

**Boot:** Nimbus 305 Coupé, Baujahr 2009
**Motor:** Volvo Penta D3-170 mit Aquamatic DPS-A
**Betriebsstunden:** 680 h (Zahnriemen bei 400 h gewechselt, Wechsel bei 600 h überfällig)
**Vorfall:** Bei Volllastfahrt auf der Ostsee (Sommer 2016) plötzlicher Motorstillstand. Sofortiger Verlust aller Motorleistung. Boot wird eingeschleppt.
**Befund:** Zahnriemen gerissen. Alle 10 Ventile verbogen, 3 Kolben beschädigt. Zylinderkopf verzogen.
**Maßnahme:** Austauschmotor (gebraucht, 1.200 h): 14.500 €, Einbau: 3.800 €. Gesamt: 18.300 €
**Alternative:** Motorinstandsetzung: geschätzt 12.000–16.000 €
**Lektion:** D3-Zahnriemen ist ein Muss-Wechsel. 600 h / 5 Jahre STRIKT einhalten. Bei Gebrauchtkauf: Nachweis verlangen!
**Confidence:** documented

### Fallstudie 3: Princess V48 — D6-380 Ladeluftkühler-Schaden

**Boot:** Princess V48, Baujahr 2016
**Motor:** 2 × Volvo Penta D6-380 mit IPS600
**Betriebsstunden:** 1.420 h (Steuerbord-Motor)
**Vorfall:** Während Überfahrt von Mallorca nach Ibiza (Sommer 2021) meldet EVC erhöhte Motortemperatur Steuerbord. Gleichzeitig weißer Rauch. Skipper reduziert Drehzahl, läuft auf einem Motor weiter.
**Befund:** Ladeluftkühler Steuerbord undicht. Seewasser über Ladelufttrakt in Zylinder 3 und 4 eingedrungen. Glücklicherweise nur geringe Menge — kein Wasserschlag.
**Maßnahme:** Ladeluftkühler tauschen: 4.200 € (Teil), Einbau: 1.500 €. Motorspülung und Ölwechsel: 350 €. Backbord-Motor vorsorglich Drucktest: 150 €. Gesamt: 6.200 €
**Lektion:** Jährlicher Drucktest beider Ladeluftkühler (150 €) hätte Risiko erkannt!
**Confidence:** documented

### Fallstudie 4: Hallberg-Rassy 412 — D2-75 Turbo-Ölverlust

**Boot:** Hallberg-Rassy 412, Baujahr 2020
**Motor:** Volvo Penta D2-75 (Common-Rail) mit 150S Saildrive
**Betriebsstunden:** 980 h
**Vorfall:** Eigner bemerkt leichten Ölfilm auf der Ladeluftleitung und bläulichen Rauch beim Starten nach längerer Standzeit (3 Tage).
**Befund:** Turbolader-Wellendichtung beginnt zu lecken. Öl gelangt in geringen Mengen in den Ladelufttrakt. Ölverbrauch leicht erhöht (0,25 l / 100 h).
**Maßnahme:** Turbolader-Überholung beim Spezialisten (Firma Turboexpert, Kiel): 1.450 €, Einbau: 480 €, Ladeluftleitung reinigen: 120 €. Gesamt: 2.050 €
**Lektion:** Bläulicher Rauch nach Standzeit kann erstes Zeichen sein. Frühzeitig reagieren spart Kosten.
**Confidence:** documented

### Fallstudie 5: Axopar 37 — IPS400 Pod-Korrosion

**Boot:** Axopar 37 Sun Top, Baujahr 2019
**Motor:** 2 × Volvo Penta D4-300 mit IPS400
**Liegeplatz:** Marina Punat, Kroatien (Salzwasser, 28 °C im Sommer)
**Vorfall:** Bei Haul-out nach 3. Saison (2022) massive weiße Korrosionsprodukte an beiden Pods sichtbar. Zinkanoden waren bereits im Juni komplett aufgelöst — Eigner hatte erst im Oktober gewechselt.
**Befund:** Lochfraßkorrosion an beiden Pod-Gehäusen, bis zu 3 mm tief. Pod-Gehäuse strukturell noch intakt, aber langfristiger Schaden.
**Maßnahme:** Professionelle Aufarbeitung beider Pods (Korrosion ausfräsen, epoxidbeschichten): 6.800 € pro Pod. Neue Zinkanoden: 680 €. Antifouling (aluminiumkompatibel): 420 €. Gesamt: 14.700 €
**Lektion:** In warmem Salzwasser Zinkanoden MINDESTENS 2× pro Saison prüfen. Kein Kupfer-Antifouling auf Aluminium-Pods!
**Confidence:** documented

### Fallstudie 6: Jeanneau Sun Odyssey 440 — Kühlmittelvermischung

**Boot:** Jeanneau Sun Odyssey 440, Baujahr 2021
**Motor:** Volvo Penta D2-40 (Common-Rail) mit 130S Saildrive
**Betriebsstunden:** 420 h
**Vorfall:** Werft füllt bei Routineservice falsches Kühlmittel nach (Silikat-basiert statt OAT). Innerhalb von 3 Monaten Gelbildung im Kühlsystem. Motortemperatur steigt auf 105 °C bei normaler Fahrt.
**Befund:** Gelartige Ablagerungen im Ausgleichsbehälter und Thermostatgehäuse. Kühlkanäle im Zylinderkopf teilweise blockiert.
**Maßnahme:** Komplette Kühlsystem-Spülung (3× mit Zitronensäurelösung): 280 €. Thermostat tauschen: 75 €. Neues VP-Original-Kühlmittel: 45 €. Arbeitszeit 4 h: 440 €. Gesamt: 840 €
**Lektion:** NIEMALS verschiedene Kühlmitteltypen mischen! Immer VP-Original oder nachweislich freigegebenes Produkt.
**Confidence:** documented

### Fallstudie 7: Bénéteau Océanis 46.1 — D2-60 Dieselpest

**Boot:** Bénéteau Océanis 46.1, Baujahr 2022
**Motor:** Volvo Penta D2-60 mit 150S Saildrive
**Betriebsstunden:** 280 h
**Vorfall:** Nach 6 Monaten Winterlager (Tank halb voll!) springt Motor im Frühjahr 2024 nicht an. Vorfilter zeigt schwarzen Schleim.
**Befund:** Massive Dieselpest. Bakterien- und Pilzbefall im Tank. Biofilm verstopft alle Filter und Leitungen.
**Maßnahme:** Tank entleeren und mechanisch reinigen: 650 €. Alle Filter und Leitungen tauschen: 380 €. Biozid-Behandlung: 45 €. Neuer Diesel (200 l): 380 €. Arbeitszeit 6 h: 660 €. Gesamt: 2.115 €
**Lektion:** Tank im Winter IMMER voll füllen! Biozid-Additiv präventiv verwenden.
**Confidence:** documented

### Fallstudie 8: Grand Soleil 44 — EVC-Kommunikationsfehler

**Boot:** Grand Soleil 44 Performance, Baujahr 2017
**Motor:** Volvo Penta D2-75 mit 150S Saildrive
**Betriebsstunden:** 1.100 h
**Vorfall:** Sporadische Fehlermeldungen auf dem EVC-Display: "CAN Bus Error", "Helm Communication Lost". Motor geht gelegentlich in Notlauf (1.500 U/min max). Problem tritt vor allem bei Feuchtigkeit und Regen auf.
**Befund:** Korrodierte CAN-Bus-Steckverbindungen am Motorraum-Kabeldurchgang. Feuchtigkeit dringt über undichte Kabeldurchführung ein.
**Maßnahme:** Alle Steckverbindungen reinigen und mit Kontaktfett (Caig DeoxIT) behandeln: 85 €. Kabeldurchführung abdichten (Roxtec-Kabelschott): 220 €. Arbeitszeit 3 h: 330 €. Gesamt: 635 €
**Lektion:** CAN-Bus-Verbindungen im Motorraum sind extremen Bedingungen ausgesetzt. Jährlich Kontaktfett erneuern!
**Confidence:** documented

---

## 26. FAQ — Häufig gestellte Fragen

### FAQ 1: Welcher Volvo Penta Motor passt zu meinem Boot?

**Faustregel für Segelyachten (Hilfsmotor):**
- Verdrängung bis 4.000 kg: D1-13 oder D1-20
- Verdrängung 4.000–7.000 kg: D1-20 oder D1-30
- Verdrängung 7.000–12.000 kg: D2-40 oder D2-50
- Verdrängung 12.000–18.000 kg: D2-60
- Verdrängung 18.000–25.000 kg: D2-75
- Über 25.000 kg: D3-Serie oder größer

**Faustregel: 3–5 PS pro Tonne Verdrängung für Segelyachten.**

### FAQ 2: Wie oft muss ich das Motoröl wechseln?

Alle 200 Betriebsstunden oder einmal jährlich — je nachdem, was zuerst eintritt. Bei Winterlager: Ölwechsel VOR dem Einwintern (Säuren im alten Öl schaden dem Motor über den Winter).

### FAQ 3: Original-Impeller oder Aftermarket?

Aftermarket-Impeller (Orbitrade, Johnson Pump, Jabsco) sind qualitativ gleichwertig und 30–50 % günstiger. Da der Impeller jährlich gewechselt wird, ist Aftermarket wirtschaftlich sinnvoll. Wichtig: Immer einen Ersatz-Impeller an Bord haben!

### FAQ 4: Mein Motor springt nach dem Winter nicht an — was tun?

1. Batterie prüfen (>12,2V unter Last?)
2. Kraftstoff-Absperrventil offen?
3. Kraftstofffilter (Vorfilter und Hauptfilter) prüfen
4. Kraftstoffsystem entlüften (D1/D2 mechanisch: Handpumpe betätigen)
5. Wenn kein Start: Glühkerzen prüfen (D1), Injektoren, Kompression

### FAQ 5: Saildrive oder Wellenanlage — was ist besser?

| Kriterium | Saildrive | Wellenanlage |
|-----------|----------|-------------|
| Installation | Einfacher | Aufwändiger |
| Wartung | Membrantausch alle 7–10 Jahre | Stopfbuchse/PSS jährlich prüfen |
| Wirkungsgrad | Besser (kürzerer Antriebsweg) | Gut |
| Tiefgang | Gleich oder leicht mehr | Variabel |
| Kosten Anschaffung | Höher | Niedriger |
| Flexibilität | Fest verbaut | Propellerposition variabel |
| Sicherheit | Membran-Risiko | Stopfbuchse-Risiko |

**Empfehlung:** Für Serienproduktion und bis D2-75: Saildrive. Für Custom-Boote und ab 80 PS: Wellenanlage.

### FAQ 6: Was ist der Unterschied zwischen EVC und EVC2?

EVC2 (ab 2018) bietet gegenüber EVC:
- Cloud-Anbindung (Volvo Penta Connect)
- Over-the-Air Software-Updates
- WiFi-basierte Diagnose
- Verbesserte NMEA 2000 Integration
- Integriertes LTE-Modul für Fernüberwachung

### FAQ 7: Kann ich meinen D2 gegen einen D3 tauschen?

Nein, nicht ohne weiteres. D2 und D3 haben völlig unterschiedliche Motorträger, Antriebsoptionen und Abmessungen. Ein Austausch erfordert Anpassungen am Motorbett, neue Antriebskomponenten und ggf. Änderungen am Rumpf. Kosten: 15.000–30.000 € (inkl. Motor).

### FAQ 8: Wie lange hält ein Volvo Penta Dieselmotor?

| Motor | Typische Lebensdauer | Bemerkung |
|-------|---------------------|-----------|
| D1-Serie | 8.000–12.000 h | Einfach, robust, langlebig |
| D2-Serie | 8.000–12.000 h | CR-Versionen etwas empfindlicher |
| D3-Serie | 5.000–8.000 h | Zahnriemen beachten! |
| D4/D6-Serie | 8.000–15.000 h | Professionelle Wartung vorausgesetzt |
| D8+ | 15.000–25.000 h | Schwerindustrie-Qualität |

### FAQ 9: Mein Motor raucht nach dem Winterlager — ist das normal?

Weißer Rauch für die ersten 5–10 Minuten nach dem Winterlager ist normal (Kondenswasser im Auspuff). Bläulicher Rauch für 1–2 Minuten kann ebenfalls normal sein (Öl im Turbo). Wenn der Rauch nach 15 Minuten Warmlauf nicht aufhört → Fehlerbild-Atlas konsultieren.

### FAQ 10: Welches Antifouling für den Saildrive?

Kein Kupfer-Antifouling auf dem Saildrive-Gehäuse! Aluminium + Kupfer = galvanische Korrosion. Verwenden Sie:
- Volvo Penta Original Saildrive-Antifouling
- International Trilux 33
- Hempel Silic One (silikonbasiert)

### FAQ 11: Muss ich den Impeller vor dem Winterlager ausbauen?

Ja, empfohlen. Ein monatelanges Stehen des Impellers in der Pumpe verformt die Flügel permanent (Memory-Effekt). Der Impeller funktioniert dann im Frühjahr nicht mehr richtig. Alternative: Impeller eingebaut lassen, aber im Frühjahr durch neuen ersetzen.

### FAQ 12: Was bedeutet VDS-4.5 bei Motoröl?

VDS = Volvo Drain Specification. Es ist Volvos eigene Motoröl-Spezifikation, die über ACEA- und API-Standards hinausgeht. VDS-4.5 ist die aktuelle Freigabe für die meisten Volvo Penta Marine-Diesel. Nur Öle mit expliziter VDS-Freigabe verwenden!

### FAQ 13: Wie entlüfte ich das Kraftstoffsystem?

**D1-Serie (mechanisch):**
1. Handpumpe am Vorfilter (Racor) betätigen — ca. 30 Hübe
2. Entlüftungsschraube am Kraftstofffilter öffnen
3. Pumpen bis blasenfreier Diesel austritt
4. Entlüftungsschraube schließen
5. Motor starten (kann 30–60 Sekunden Anlasszeit benötigen)

**D2-Serie (Common-Rail ab 2019):**
1. Vorfilter-Handpumpe betätigen
2. Zündung einschalten (Motor NICHT starten)
3. Elektrische Vorförderpumpe arbeitet 30 Sekunden
4. Motor starten — ECU entlüftet automatisch über Rücklaufleitung
5. Wenn nötig: 3× wiederholen (Zündung aus/ein)

### FAQ 14: Kann ich Bio-Diesel tanken?

Volvo Penta gibt bis B7 (7 % Bio-Anteil) frei — das ist EU-Standard-Diesel. Höhere Bio-Anteile (B20, B100) sind NICHT freigegeben und können zu folgenden Problemen führen:
- Beschleunigtes Quellen von Dichtungen und Schläuchen
- Erhöhte Dieselpest-Gefahr (Nährboden für Mikroorganismen)
- Verstopfte Injektoren (Ablagerungen)
- Verringerter Energiegehalt (höherer Verbrauch)

### FAQ 15: Was kostet ein kompletter Motorservice?

| Service | D1/D2 | D3 | D4/D6 |
|---------|-------|-----|-------|
| Kleiner Service (Öl, Filter, Impeller) | 250–400 € | 400–600 € | 600–900 € |
| Großer Service (+ Keilriemen, Kühlmittel, Zahnriemen bei D3) | 450–700 € | 1.400–2.200 € | 1.000–1.600 € |
| Jahresservice komplett (inkl. Saildrive/Sterndrive) | 600–1.000 € | 1.800–2.800 € | 2.000–3.500 € |

### FAQ 16: Mein Volvo Penta D2-40 verbraucht plötzlich mehr Öl — was kann das sein?

Mögliche Ursachen nach Häufigkeit:
1. Ölstand beim Messen falsch (schräge Peilung, warmer Motor) — 40 %
2. Ölfilter-Dichtung undicht — 20 %
3. Ventildeckeldichtung — 15 %
4. Kurbelwellen-Wellendichtring — 10 %
5. Turbolader-Wellendichtung (D2-75) — 10 %
6. Kolbenringe verschlissen — 5 % (nur bei hohen Stunden)

### FAQ 17: Wie prüfe ich den Zustand meines Turboladers?

1. Ladeluftschlauch am Turbo-Ausgang abziehen → Öl sichtbar? Ölnebel normal, flüssiges Öl = Problem
2. Turbinenrad mit Finger drehen — muss leichtgängig und spielfrei sein
3. Axialspiel prüfen: Turbinenrad vor/zurück bewegen — max. 0,1 mm
4. Radialspiel prüfen: Turbinenrad seitlich bewegen — max. 0,15 mm
5. VGT-Verstellmechanik (D3): Muss leichtgängig arbeiten

### FAQ 18: Was ist der Unterschied zwischen IPS und Aquamatic?

| Kriterium | IPS | Aquamatic |
|-----------|-----|----------|
| Propellerposition | Unter dem Rumpf (Pods) | Am Heckspiegel |
| Propellertyp | Duoprop (gegenläufig) | Einzel oder Duoprop |
| Steuerung | Pod dreht sich | Sterndrive schwenkt |
| Manövrierfähigkeit | Hervorragend (Joystick) | Gut |
| Effizienz | Sehr hoch | Hoch |
| Tiefgang | Erhöht | Gering |
| Bootsgröße | Ab 30 ft | 18–40 ft |
| Wartung | Pod-spezifisch | Sterndrive-spezifisch |

### FAQ 19: Kann ich die Motorleistung meines D4/D6 per Software erhöhen?

Volvo Penta bietet KEINE offiziellen Leistungssteigerungen per Software-Update an. Chip-Tuning durch Drittanbieter ist möglich, hat aber Nachteile:
- Garantieverlust
- Erhöhter Verschleiß an Turbo, Einspritzanlage, Getriebe
- Keine Freigabe für Antriebsstrang (IPS/Aquamatic für spezifische Leistung ausgelegt)
- Mögliche Versicherungsprobleme

**Empfehlung:** Wenn mehr Leistung benötigt wird, auf die nächsthöhere Leistungsstufe wechseln (z. B. D4-260 → D4-300, gleicher Motorblock).

### FAQ 20: Wie lagere ich einen Ersatz-Impeller richtig?

- Originalverpackung belassen (flach, ohne Verformung)
- Trocken und dunkel lagern (UV-Schutz!)
- Nicht auf den Impeller drücken oder biegen
- Lagertemperatur: 5–25 °C
- Maximale Lagerdauer: 5 Jahre (Neopren altert)
- Talkum-Puder auf dem Impeller belassen (Gleitmittel)

### FAQ 21: Welche Starterbatterie für meinen Volvo Penta?

| Motor | Mindest-Kapazität | Empfehlung | Typ |
|-------|-------------------|-----------|-----|
| D1-13 | 45 Ah | 62 Ah | AGM oder Blei-Säure |
| D1-20 | 62 Ah | 75 Ah | AGM |
| D1-30 | 70 Ah | 90 Ah | AGM |
| D2-40/50 | 88 Ah | 100 Ah | AGM |
| D2-60/75 | 88 Ah | 100 Ah | AGM |
| D3-Serie | 100 Ah | 120 Ah | AGM |
| D4-Serie | 140 Ah | 180 Ah | AGM |
| D6-Serie | 140 Ah | 2 × 100 Ah parallel | AGM |

### FAQ 22: Muss der Saildrive bei jedem Haul-out raus?

Nein. Der Saildrive muss nur für den Membrantausch (alle 7–10 Jahre) komplett demontiert werden. Bei jedem Haul-out sollte jedoch die Membran visuell inspiziert, Zinkanoden gewechselt und Antifouling erneuert werden.

### FAQ 23: Wie erkenne ich, ob mein Motor Common-Rail oder mechanische Einspritzung hat?

**Mechanische Einspritzung (ältere D1, D2 vor 2019):**
- Mechanische Einspritzpumpe sichtbar (großes metallenes Bauteil seitlich am Motor)
- Einfachere Kabelführung
- Kein EVC-Display erforderlich
- Entlüftung manuell über Handpumpe

**Common-Rail (D2 ab 2019, D3, D4, D6):**
- Rail (Hochdruckleiste) mit Injektoren sichtbar
- ECU (elektronisches Steuergerät) am Motor
- CAN-Bus-Kabel
- Automatische Entlüftung über Vorförderpumpe

### FAQ 24: Was ist der Unterschied zwischen 120S, 130S und 150S Saildrive?

| Kriterium | 120S | 130S | 150S |
|-----------|------|------|------|
| Max. Leistung | 22 kW (30 PS) | 40 kW (54 PS) | 60 kW (81 PS) |
| Motorkompatibilität | D1-13, D1-20 | D1-30, D2-40, D2-50 | D2-60, D2-75 |
| Untersetzung | 2,15:1 | 2,15:1 / 2,47:1 | 2,15:1 / 2,47:1 / 2,72:1 |
| Gewicht | 38 kg | 45 kg | 56 kg |
| Membran-Ø | 230 mm | 260 mm | 290 mm |

### FAQ 25: Wie hoch sind die Betriebskosten eines Volvo Penta D2-40 pro Stunde?

Annahme: 300 Betriebsstunden pro Jahr, Dieselpreis 1,80 €/l

| Kostenart | Pro Stunde | Pro Jahr |
|-----------|-----------|---------|
| Diesel (75 % Last) | 13,50 € | 4.050 € |
| Motoröl (200 h Wechsel) | 0,30 € | 90 € |
| Filter (jährlich) | 0,25 € | 75 € |
| Impeller (jährlich) | 0,15 € | 45 € |
| Saildrive-Wartung | 0,35 € | 105 € |
| Werkstatt (Jahresservice) | 1,05 € | 315 € |
| Rücklagen (Reparaturen) | 1,50 € | 450 € |
| **Gesamt** | **17,10 €** | **5.130 €** |

### FAQ 26: Kann ich meinen Volvo Penta auf HVO-Diesel (R33/R100) umstellen?

Volvo Penta hat seit 2023 HVO100 (Hydrotreated Vegetable Oil, EN 15940) für alle aktuellen Motoren freigegeben. Vorteile:
- Bis zu 90 % weniger CO₂ (Well-to-Wheel)
- Bessere Kälteeigenschaften als fossiler Diesel
- Keine Umbaumaßnahmen erforderlich
- Mischbar mit fossilem Diesel

Nachteil: HVO-Diesel ist ca. 20–40 % teurer als fossiler Diesel.

---

## 27. Glossar

| Begriff | Erklärung |
|---------|----------|
| **Aftercooler** | Ladeluftkühler — kühlt die verdichtete Luft nach dem Turbolader |
| **AGM-Batterie** | Absorbent Glass Mat — wartungsfreie Blei-Batterie mit Glasvlies |
| **Anodenschutz** | Galvanischer Korrosionsschutz durch Opferanoden (Zink, Aluminium, Magnesium) |
| **Aquamatic** | Volvo Penta Markenname für Sterndrive-Antriebe (Z-Antrieb) |
| **Bellows** | Faltenbälge am Sterndrive, die den Übergang Motor-Sterndrive abdichten |
| **Blow-by** | Leckgas, das an den Kolbenringen vorbei ins Kurbelgehäuse gelangt |
| **Bohrung** | Innendurchmesser des Zylinders |
| **CAN-Bus** | Controller Area Network — serielles Datenbus-System für Fahrzeuge und Schiffe |
| **CGI** | Compact Graphite Iron — Gusseisen mit Vermikulargrafit (leichter, steifer) |
| **Common-Rail** | Hochdruck-Einspritzsystem mit gemeinsamer Druckleiste für alle Injektoren |
| **Crankshaft Damper** | Schwingungsdämpfer an der Kurbelwelle |
| **DEF** | Diesel Exhaust Fluid — AdBlue, wässrige Harnstofflösung für SCR |
| **Diaphragma** | Membran, insbesondere am Saildrive |
| **DOC** | Diesel Oxidation Catalyst — Oxidationskatalysator |
| **DOHC** | Double Overhead Camshaft — doppelte obenliegende Nockenwelle |
| **DPF** | Diesel Particulate Filter — Dieselpartikelfilter |
| **DPS** | Dynamic Positioning System — automatische Positionshaltung |
| **Duoprop** | Gegenläufiges Doppelpropeller-System von Volvo Penta |
| **ECA-Zone** | Emission Control Area — Seegebiet mit strengen Emissionsvorschriften |
| **ECU** | Electronic Control Unit — elektronisches Steuergerät |
| **EPDM** | Ethylen-Propylen-Dien-Monomer — synthetischer Kautschuk |
| **EVC** | Electronic Vessel Control — Volvo Pentas elektronisches Steuerungssystem |
| **Frostschutz** | Kühlmittelzusatz zur Senkung des Gefrierpunkts |
| **Gimbal** | Kardanische Aufhängung — beim Sterndrive: Schwenklagerung |
| **Glühkerze** | Vorglühkerze für Kaltstart (nur D1-Serie) |
| **Hub** | Kolbenweg zwischen oberem und unterem Totpunkt |
| **HVO** | Hydrotreated Vegetable Oil — synthetischer Diesel aus Pflanzenölen |
| **IMO** | International Maritime Organization — UN-Behörde für Seeschifffahrt |
| **Impeller** | Gummi-Flügelrad in der Seewasserpumpe |
| **Injektor** | Einspritzdüse — spritzt Kraftstoff in den Zylinder |
| **IPS** | Inboard Performance System — Pod-Antrieb von Volvo Penta |
| **Kavitation** | Dampfblasenbildung am Propeller durch Unterdruck |
| **Keilriemen** | Antriebsriemen für Nebenaggregate (Lichtmaschine, Kühlwasserpumpe) |
| **Kompression** | Verdichtungsdruck im Zylinder |
| **Ladedruck** | Überdruck der verdichteten Ladeluft nach dem Turbolader |
| **Ladeluftkühler** | Wärmetauscher zur Kühlung der verdichteten Ladeluft |
| **LLK** | Ladeluftkühler (Abkürzung) |
| **Nassauspuff** | Marine-Auspuffsystem, bei dem Seewasser den Abgasen beigemischt wird |
| **NMEA 2000** | Standard-Datennetzwerk für marine Elektronik |
| **Nockenwelle** | Steuerwelle für die Ventilsteuerung |
| **OAT** | Organic Acid Technology — Kühlmitteltyp mit organischen Korrosionsinhibitoren |
| **OHV** | Overhead Valve — Ventile im Zylinderkopf, Nockenwelle im Motorblock |
| **Opferanode** | Unedleres Metall, das sich statt des zu schützenden Metalls auflöst |
| **Pod** | Gondel-förmiger Antrieb unter dem Rumpf (IPS) |
| **Propeller-Steigung** | Theoretischer Vorschub pro Umdrehung |
| **Peilstab** | Ölmessstab |
| **PGN** | Parameter Group Number — NMEA 2000 Nachrichtenkennung |
| **PSS** | Packless Sealing System — wartungsarme Wellendichtung |
| **Racor** | Markenname für Kraftstoff-Vorfilter mit Wasserabscheider |
| **Rail** | Hochdruckleiste im Common-Rail-System |
| **Saildrive** | Integrierter Antrieb für Segelyachten (Motor + Getriebe + Propeller) |
| **SCR** | Selective Catalytic Reduction — Abgasnachbehandlung mit AdBlue |
| **Seeventil** | Absperrventil am Rumpfdurchbruch (Borddurchlass) |
| **Sterndrive** | Z-Antrieb am Heckspiegel (Aquamatic) |
| **Stevenrohr** | Rohr durch den Rumpf, in dem die Propellerwelle läuft |
| **Stopfbuchse** | Dichtung am Stevenrohr-Austritt der Propellerwelle |
| **Thermostat** | Temperaturgesteuertes Ventil im Kühlkreislauf |
| **Turbolader** | Abgasturbolader — nutzt Abgasenergie zur Verdichtung der Ansaugluft |
| **ULSD** | Ultra Low Sulfur Diesel — Diesel mit max. 10 ppm Schwefel |
| **VDS** | Volvo Drain Specification — Volvo-eigene Motorölspezifikation |
| **VGT** | Variable Geometry Turbocharger — Turbolader mit verstellbarer Geometrie |
| **VODIA** | Volvo Diagnostics Application — offizielles Diagnose-Tool |
| **VP Connect** | Volvo Penta Cloud-basiertes Monitoring-System |
| **Wärmetauscher** | Überträgt Wärme zwischen Frischwasser- und Seewasserkreislauf |
| **Wastegate** | Ladedruckbegrenzungsventil am Turbolader |
| **Wendegetriebe** | Getriebe mit Vorwärts-/Rückwärts-/Neutralstellung |
| **Zahnriemen** | Steuerriemen für die Nockenwelle (nur D3-Serie) |
| **Zinkanode** | Opferanode aus Zink (nur für Salzwasser geeignet) |
| **Zweikreiskühlung** | Kühlsystem mit separatem Frischwasser- und Seewasserkreislauf |

---

## ANHANG A — Technische Datenblätter Übersicht

### A.1 Vergleichstabelle aller Volvo Penta Marine-Diesel

| Motor | Zyl. | Hubraum (cm³) | PS | kW | Nm | Drehzahl | Gewicht (kg) | Einspritzung | Aufladung |
|-------|------|-------------|-----|-----|------|---------|-------------|-------------|----------|
| D1-13 | 1 | 505 | 12,2 | 9 | 24 | 3.600 | 79 | Mechanisch | Sauger |
| D1-20 | 2 | 764 | 18,8 | 14 | 37 | 3.600 | 99 | Mechanisch | Sauger |
| D1-30 | 3 | 1.131 | 28,4 | 21 | 56 | 3.600 | 119 | Mechanisch | Sauger |
| D2-40 | 2 | 1.124 | 37,5 | 28 | 75 | 3.600 | 137 | CR | Sauger |
| D2-50 | 3 | 1.686 | 47,3 | 35 | 95 | 3.600 | 163 | CR | Sauger |
| D2-60 | 4 | 2.189 | 58,6 | 43 | 120 | 3.600 | 185 | CR | Sauger |
| D2-75 | 4 | 2.189 | 75 | 55 | 165 | 3.600 | 198 | CR | Turbo |
| D3-110 | 5 | 2.400 | 110 | 81 | 280 | 3.500 | 270 | CR | VGT |
| D3-150 | 5 | 2.400 | 150 | 110 | 370 | 3.500 | 275 | CR | VGT |
| D3-170 | 5 | 2.400 | 170 | 125 | 400 | 3.500 | 278 | CR | VGT |
| D3-220 | 5 | 2.400 | 220 | 162 | 480 | 3.500 | 285 | CR | VGT |
| D4-260 | 4 | 3.700 | 260 | 191 | 620 | 3.500 | 380 | CR | 2-Stufe |
| D4-300 | 4 | 3.700 | 300 | 221 | 700 | 3.500 | 385 | CR | 2-Stufe |
| D6-310 | 6 | 5.500 | 310 | 228 | 750 | 3.500 | 520 | CR | 2-Stufe |
| D6-340 | 6 | 5.500 | 340 | 250 | 830 | 3.500 | 525 | CR | 2-Stufe |
| D6-380 | 6 | 5.500 | 380 | 280 | 900 | 3.500 | 530 | CR | 2-Stufe |
| D6-440 | 6 | 5.500 | 440 | 324 | 980 | 3.500 | 535 | CR | 2-Stufe |
| D8-380 | V8 | 7.700 | 380 | 280 | 1.100 | 3.000 | 685 | CR | Biturbo |
| D8-450 | V8 | 7.700 | 450 | 331 | 1.280 | 3.000 | 695 | CR | Biturbo |
| D8-510 | V8 | 7.700 | 510 | 375 | 1.420 | 3.000 | 700 | CR | Biturbo |
| D8-550 | V8 | 7.700 | 550 | 405 | 1.500 | 3.000 | 710 | CR | Biturbo |
| D11-625 | R6 | 10.800 | 625 | 460 | 2.400 | 2.300 | 1.065 | CR | VGT |
| D11-725 | R6 | 10.800 | 725 | 533 | 2.800 | 2.300 | 1.065 | CR | VGT |
| D13-800 | R6 | 12.800 | 800 | 588 | 3.200 | 2.300 | 1.280 | CR | 2×VGT |
| D13-1000 | R6 | 12.800 | 1.000 | 736 | 3.800 | 2.300 | 1.280 | CR | 2×VGT |
| D16-650 | R6 | 16.100 | 650 | 478 | 3.400 | 1.800 | 1.620 | CR | VGT |
| D16-900 | R6 | 16.100 | 900 | 662 | 4.200 | 1.800 | 1.620 | CR | VGT |

### A.2 Antriebskompatibilität

| Motor | Saildrive | Wellengetriebe | IPS | Aquamatic |
|-------|----------|---------------|-----|----------|
| D1-13 | 120S | MS10A | — | — |
| D1-20 | 120S | MS15A | — | — |
| D1-30 | 130S | MS25A | — | — |
| D2-40 | 130S | MS25A | — | — |
| D2-50 | 130S | MS25A | — | — |
| D2-60 | 150S | MS25L | — | — |
| D2-75 | 150S | MS25L | — | — |
| D3-110 | — | MS25L | — | SX-A |
| D3-150 | — | MS25L | — | SX-A / DPS-A |
| D3-170 | — | MS25L | — | DPS-A |
| D3-220 | — | MS25L | — | DPS-A |
| D4-260 | — | HS63AE | IPS400 | DPH-A |
| D4-300 | — | HS63AE | IPS400 | DPH-A |
| D6-310 | — | HS80AE | IPS500 | — |
| D6-340 | — | HS80AE | IPS500 | — |
| D6-380 | — | HS80AE | IPS600 | DPH-D |
| D6-440 | — | HS80AE | IPS600 | DPH-D |
| D8-Serie | — | HS85AE | IPS700 | — |
| D11-Serie | — | Ja | IPS950 | — |
| D13-Serie | — | Ja | IPS950 | — |
| D16-Serie | — | Ja | — | — |

---

## ANHANG B — Confidence-Mapping

### B.1 Datenquellen und Vertrauensstufen

| Datenquelle | Confidence-Level | Begründung |
|------------|-----------------|-----------|
| Volvo Penta Technische Datenblätter | measured | Herstellerangaben, geprüft |
| Volvo Penta Bedienungsanleitungen | measured | Offizielle Dokumentation |
| Volvo Penta Service Bulletins | documented | Werkstatt-Erfahrungen, verifiziert |
| Volvo Penta Werkstatt-Handbücher | measured | Offizielle Werkstattliteratur |
| VP-autorisierte Werkstattberichte | documented | Professionelle Bewertung |
| Eigner-Erfahrungsberichte (Foren) | estimated | Subjektiv, nicht immer verifizierbar |
| AYDI-eigene Berechnungen | calculated | Abgeleitet aus gemessenen Daten |
| Preisangaben (Händler, 2025) | estimated | Marktabhängig, ±10–20 % |
| Lebensdauer-Angaben | estimated | Statistischer Durchschnitt, stark nutzungsabhängig |
| Kraftstoffverbrauch | measured (Volllast) / estimated (Teillast) | Teillastangaben interpoliert |

### B.2 Confidence-Regeln für AYDI-Analyse

1. **Motoridentifikation per Seriennummer:** confidence = measured
2. **Motoridentifikation per Foto:** confidence = visual_medium (Logo, Typenschild lesbar) oder visual_low
3. **Zustandsbewertung per Foto:** confidence = visual_medium (deutliche Befunde) bis visual_low (subtile Befunde)
4. **Wartungszustand ohne Serviceheft:** confidence = estimated
5. **Wartungszustand mit Serviceheft:** confidence = documented
6. **Preisangaben:** confidence = estimated (±15 %, marktabhängig)
7. **Lebensdauerangaben:** confidence = estimated (stark nutzungsabhängig)

---

## ANHANG C — AYDI-Integration (Pydantic-Modelle)

```python
"""
AYDI Pydantic v2 Modelle für Volvo Penta Marine-Diesel Analyse.
"""

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class FuelInjectionType(str, Enum):
    MECHANICAL = "mechanical"
    COMMON_RAIL = "common_rail"


class AspirationMethod(str, Enum):
    NATURALLY_ASPIRATED = "naturally_aspirated"
    TURBO_WASTEGATE = "turbo_wastegate"
    TURBO_VGT = "turbo_vgt"
    TWIN_TURBO = "twin_turbo"
    TWO_STAGE_TURBO = "two_stage_turbo"


class DriveType(str, Enum):
    SAILDRIVE = "saildrive"
    SHAFT = "shaft"
    IPS = "ips"
    AQUAMATIC = "aquamatic"


class ConfidenceLevel(str, Enum):
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    DOCUMENTED = "documented"
    BENCHMARK = "benchmark"


class EngineCondition(str, Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"
    UNKNOWN = "unknown"


class SaildriveMembraneStatus(str, Enum):
    NEW = "new"
    GOOD = "good"
    AGING = "aging"
    REPLACE_SOON = "replace_soon"
    REPLACE_NOW = "replace_now"
    UNKNOWN = "unknown"


class VolvoPentaEngineSpec(BaseModel):
    """Technische Spezifikation eines Volvo Penta Marine-Diesel-Motors."""

    model_config = {"from_attributes": True}

    model_name: str = Field(
        ...,
        description="Motorbezeichnung (z.B. 'D2-40', 'D6-380')",
        examples=["D1-30", "D2-75", "D6-440"],
    )
    cylinders: int = Field(
        ..., ge=1, le=8, description="Anzahl Zylinder"
    )
    displacement_cc: int = Field(
        ..., ge=400, le=17000, description="Hubraum in cm³"
    )
    power_hp: float = Field(
        ..., ge=10, le=1100, description="Leistung in PS"
    )
    power_kw: float = Field(
        ..., ge=7, le=800, description="Leistung in kW"
    )
    torque_nm: float = Field(
        ..., ge=20, le=4500, description="Drehmoment in Nm"
    )
    rated_rpm: int = Field(
        ..., ge=1500, le=4000, description="Nenndrehzahl in U/min"
    )
    injection_type: FuelInjectionType = Field(
        ..., description="Einspritzungstyp"
    )
    aspiration: AspirationMethod = Field(
        ..., description="Aufladungsmethode"
    )
    weight_dry_kg: float = Field(
        ..., ge=50, le=2000, description="Trockengewicht in kg"
    )
    oil_capacity_l: float = Field(
        ..., ge=1, le=60, description="Motorölmenge in Litern"
    )
    coolant_capacity_l: float = Field(
        ..., ge=1, le=60, description="Kühlmittelmenge in Litern"
    )
    fuel_consumption_full_lph: float = Field(
        ..., ge=2, le=200, description="Kraftstoffverbrauch Volllast in l/h"
    )
    fuel_consumption_cruise_lph: float = Field(
        ..., ge=1, le=120, description="Kraftstoffverbrauch Marschfahrt in l/h"
    )
    compatible_drives: list[DriveType] = Field(
        ..., description="Kompatible Antriebsarten"
    )
    list_price_eur: Optional[float] = Field(
        None, ge=0, description="Listenpreis Motor in EUR (ohne Antrieb)"
    )
    production_start: Optional[int] = Field(
        None, ge=1990, le=2030, description="Produktionsbeginn (Jahr)"
    )
    production_end: Optional[int] = Field(
        None, ge=1990, le=2040, description="Produktionsende (Jahr, None=aktuell)"
    )


class VolvoPentaEngineCondition(BaseModel):
    """Zustandsbewertung eines Volvo Penta Motors."""

    model_config = {"from_attributes": True}

    engine_model: str = Field(
        ..., description="Motorbezeichnung"
    )
    serial_number: Optional[str] = Field(
        None, description="Seriennummer"
    )
    year_of_manufacture: Optional[int] = Field(
        None, ge=1990, le=2030, description="Baujahr"
    )
    operating_hours: Optional[int] = Field(
        None, ge=0, le=30000, description="Betriebsstunden"
    )
    overall_condition: EngineCondition = Field(
        ..., description="Gesamtzustand"
    )
    condition_confidence: ConfidenceLevel = Field(
        ..., description="Confidence-Level der Bewertung"
    )
    oil_condition: Optional[str] = Field(
        None,
        description="Zustand Motoröl (klar/dunkel/milchig/metallpartikel)",
    )
    coolant_condition: Optional[str] = Field(
        None,
        description="Zustand Kühlmittel (klar/trüb/gelartig/verfärbt)",
    )
    exhaust_smoke: Optional[str] = Field(
        None,
        description="Abgasrauch (klar/weiß/schwarz/blau)",
    )
    turbo_condition: Optional[str] = Field(
        None,
        description="Turbolader-Zustand (ok/axialspiel/radialspiel/oelundicht)",
    )
    timing_belt_last_change_hours: Optional[int] = Field(
        None,
        ge=0,
        description="Letzte Zahnriemenwechsel bei Betriebsstunden (nur D3)",
    )
    injector_condition: Optional[str] = Field(
        None,
        description="Injektor-Zustand (ok/verschmutzt/undicht/defekt)",
    )
    findings: list[str] = Field(
        default_factory=list,
        description="Liste der Befunde (deutsch)",
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen (deutsch)",
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Reparaturkosten in EUR"
    )
    estimated_remaining_life_hours: Optional[int] = Field(
        None, ge=0, description="Geschätzte Restlebensdauer in Stunden"
    )


class SaildriveCondition(BaseModel):
    """Zustandsbewertung eines Volvo Penta Saildrives."""

    model_config = {"from_attributes": True}

    saildrive_model: str = Field(
        ...,
        description="Saildrive-Modell (120S/130S/150S)",
        examples=["120S", "130S", "150S"],
    )
    membrane_age_years: Optional[int] = Field(
        None, ge=0, le=20, description="Membran-Alter in Jahren"
    )
    membrane_last_replaced: Optional[str] = Field(
        None, description="Datum letzter Membrantausch (YYYY-MM)"
    )
    membrane_status: SaildriveMembraneStatus = Field(
        ..., description="Membran-Zustandsbewertung"
    )
    membrane_confidence: ConfidenceLevel = Field(
        ..., description="Confidence der Membran-Bewertung"
    )
    anodes_condition: Optional[str] = Field(
        None,
        description="Zustand Zinkanoden (>75%/50-75%/<50%/aufgelöst)",
    )
    gear_oil_condition: Optional[str] = Field(
        None,
        description="Zustand Getriebeöl (klar/milchig/metallspäne)",
    )
    propeller_condition: Optional[str] = Field(
        None,
        description="Propeller-Zustand (ok/bewuchs/beschädigt/unwucht)",
    )
    findings: list[str] = Field(
        default_factory=list,
        description="Befunde (deutsch)",
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen (deutsch)",
    )
    membrane_replace_urgency: Optional[str] = Field(
        None,
        description="Dringlichkeit Membrantausch (sofort/nächster_haul_out/planbar/nicht_erforderlich)",
    )


class IPSCondition(BaseModel):
    """Zustandsbewertung eines Volvo Penta IPS-Systems."""

    model_config = {"from_attributes": True}

    ips_model: str = Field(
        ...,
        description="IPS-Modell (IPS400/500/600/700/950)",
        examples=["IPS400", "IPS500", "IPS600"],
    )
    pod_location: str = Field(
        ...,
        description="Pod-Position (backbord/steuerbord/einzeln)",
    )
    anodes_condition: Optional[str] = Field(
        None,
        description="Zustand Zinkanoden (>75%/50-75%/<50%/aufgelöst)",
    )
    pod_corrosion: Optional[str] = Field(
        None,
        description="Korrosionszustand (keine/oberflächlich/lochfraß/schwer)",
    )
    bellows_condition: Optional[str] = Field(
        None,
        description="Faltenbälge (ok/alterung/risse/undicht)",
    )
    gear_oil_condition: Optional[str] = Field(
        None,
        description="Getriebeöl (klar/milchig/metallspäne)",
    )
    propeller_condition: Optional[str] = Field(
        None,
        description="Propeller-Zustand (ok/bewuchs/beschädigt/kavitation)",
    )
    joystick_function: Optional[str] = Field(
        None,
        description="Joystick-Funktion (ok/eingeschränkt/defekt)",
    )
    dps_function: Optional[str] = Field(
        None,
        description="DPS-Funktion (ok/drift/defekt/nicht_vorhanden)",
    )
    findings: list[str] = Field(
        default_factory=list,
        description="Befunde (deutsch)",
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen (deutsch)",
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Reparaturkosten in EUR"
    )


class VolvoPentaMaintenanceRecord(BaseModel):
    """Wartungsdatensatz für Volvo Penta Motoren."""

    model_config = {"from_attributes": True}

    engine_model: str = Field(
        ..., description="Motorbezeichnung"
    )
    operating_hours_at_service: int = Field(
        ..., ge=0, description="Betriebsstunden bei Wartung"
    )
    service_date: str = Field(
        ..., description="Datum (YYYY-MM-DD)"
    )
    service_type: str = Field(
        ...,
        description="Servicetyp (oil_change/filter_change/impeller/timing_belt/major_service/repair)",
    )
    parts_replaced: list[str] = Field(
        default_factory=list,
        description="Getauschte Teile",
    )
    parts_cost_eur: float = Field(
        ..., ge=0, description="Materialkosten in EUR"
    )
    labor_cost_eur: float = Field(
        ..., ge=0, description="Arbeitskosten in EUR"
    )
    total_cost_eur: float = Field(
        ..., ge=0, description="Gesamtkosten in EUR"
    )
    performed_by: str = Field(
        ...,
        description="Ausgeführt durch (owner/dealer/authorized_workshop)",
    )
    notes: Optional[str] = Field(
        None, description="Anmerkungen"
    )
    next_service_due_hours: Optional[int] = Field(
        None, ge=0, description="Nächste Wartung bei Betriebsstunden"
    )
    next_service_due_date: Optional[str] = Field(
        None, description="Nächste Wartung spätestens (YYYY-MM-DD)"
    )


class VolvoPentaCostEstimate(BaseModel):
    """Kostenabschätzung für Volvo Penta Motor-Reparaturen."""

    model_config = {"from_attributes": True}

    engine_model: str = Field(
        ..., description="Motorbezeichnung"
    )
    repair_description: str = Field(
        ..., description="Reparaturbeschreibung (deutsch)"
    )
    parts_cost_min_eur: float = Field(
        ..., ge=0, description="Materialkosten Minimum in EUR"
    )
    parts_cost_max_eur: float = Field(
        ..., ge=0, description="Materialkosten Maximum in EUR"
    )
    labor_hours_min: float = Field(
        ..., ge=0, description="Arbeitszeit Minimum in Stunden"
    )
    labor_hours_max: float = Field(
        ..., ge=0, description="Arbeitszeit Maximum in Stunden"
    )
    labor_rate_eur_per_hour: float = Field(
        default=110.0, ge=0, description="Stundensatz in EUR"
    )
    total_cost_min_eur: float = Field(
        ..., ge=0, description="Gesamtkosten Minimum in EUR"
    )
    total_cost_max_eur: float = Field(
        ..., ge=0, description="Gesamtkosten Maximum in EUR"
    )
    cost_confidence: ConfidenceLevel = Field(
        default=ConfidenceLevel.ESTIMATED,
        description="Confidence der Kostenschätzung",
    )
    notes: Optional[str] = Field(
        None, description="Anmerkungen zur Kostenschätzung"
    )


class VolvoPentaFullAnalysis(BaseModel):
    """Vollständige AYDI-Analyse eines Volvo Penta Antriebssystems."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = Field(
        None, description="Bootsname"
    )
    boat_model: Optional[str] = Field(
        None, description="Bootsmodell"
    )
    engine_spec: VolvoPentaEngineSpec = Field(
        ..., description="Motor-Spezifikation"
    )
    engine_condition: VolvoPentaEngineCondition = Field(
        ..., description="Motor-Zustandsbewertung"
    )
    drive_type: DriveType = Field(
        ..., description="Antriebstyp"
    )
    saildrive_condition: Optional[SaildriveCondition] = Field(
        None, description="Saildrive-Bewertung (wenn Saildrive)"
    )
    ips_condition: Optional[IPSCondition] = Field(
        None, description="IPS-Bewertung (wenn IPS)"
    )
    maintenance_history: list[VolvoPentaMaintenanceRecord] = Field(
        default_factory=list,
        description="Wartungshistorie",
    )
    cost_estimates: list[VolvoPentaCostEstimate] = Field(
        default_factory=list,
        description="Kostenabschätzungen für empfohlene Maßnahmen",
    )
    overall_score: Optional[float] = Field(
        None, ge=0, le=100, description="Gesamt-Score (0-100)"
    )
    analysis_confidence: ConfidenceLevel = Field(
        ..., description="Confidence der Gesamtanalyse"
    )
    analysis_summary_de: str = Field(
        ..., description="Zusammenfassung der Analyse (deutsch)"
    )
    critical_findings: list[str] = Field(
        default_factory=list,
        description="Kritische Befunde (deutsch)",
    )
    action_items: list[str] = Field(
        default_factory=list,
        description="Empfohlene Maßnahmen mit Priorität (deutsch)",
    )
```

---

## ANHANG D — Wartungsprotokoll-Vorlage

### D.1 Jährliches Wartungsprotokoll Volvo Penta

```
=== VOLVO PENTA WARTUNGSPROTOKOLL ===

Boot: _________________________ Modell: _________________________
Motor: ________________________ Seriennummer: ___________________
Baujahr Motor: ________________ Antrieb: _______________________
Datum: ________________________ Betriebsstunden: ________________
Ausgeführt von: _______________

MOTORÖL UND FILTER
[ ] Ölwechsel durchgeführt            Menge: ____ l  Spez.: ________
[ ] Ölfilter gewechselt               Teilenummer: ________________
[ ] Ölstand nach Wechsel korrekt

KRAFTSTOFFSYSTEM
[ ] Kraftstoff-Vorfilter gewechselt   Teilenummer: ________________
[ ] Kraftstoff-Hauptfilter gewechselt Teilenummer: ________________
[ ] Wasserabscheider entleert         Wasser vorhanden: ja/nein
[ ] Kraftstoffsystem entlüftet
[ ] Kraftstoff-Absperrventil gängig

KÜHLSYSTEM
[ ] Impeller geprüft/gewechselt       Zustand: ___________________
[ ] Seewasserfilter gereinigt
[ ] Kühlmittelstand geprüft           Stand: ____________________
[ ] Kühlmittel-Frostschutz gemessen   Gefrierpunkt: ____ °C
[ ] Zinkanode im Wärmetauscher geprüft Zustand: ___________________
[ ] Keilriemen geprüft                Zustand/Spannung: ___________
[ ] Seewasserschläuche geprüft        Zustand: ___________________
[ ] Thermostat geprüft                Zustand: ___________________

ABGASANLAGE
[ ] Abgaskrümmer visuell geprüft      Zustand: ___________________
[ ] Mischrohr (Nassauspuff) geprüft   Zustand: ___________________
[ ] Auspuffschlauch geprüft           Zustand: ___________________

TURBOLADER (wenn vorhanden)
[ ] Turbolader visuell geprüft        Zustand: ___________________
[ ] Ladeluftschlauch auf Öl geprüft   Öl vorhanden: ja/nein
[ ] Ladedruck bei Volllast gemessen    Wert: ____ bar

LADELUFTKÜHLER (D4/D6)
[ ] Drucktest durchgeführt             Ergebnis: _________________

ELEKTRIK
[ ] Lichtmaschine Ladespannung        Wert: ____ V bei ____ U/min
[ ] Starterbatterie Spannung          Wert: ____ V
[ ] Verkabelung/Stecker geprüft       Zustand: ___________________
[ ] EVC-Fehlerspeicher ausgelesen     Fehler: ____________________

SAILDRIVE (wenn vorhanden)
[ ] Membran visuell geprüft           Zustand: ___________________
[ ] Membran-Alter                     Jahre: ____
[ ] Getriebeöl gewechselt             Menge: ____ l
[ ] Getriebeöl-Zustand                Klar/milchig/Metallspäne
[ ] Zinkanoden gewechselt             Zustand alt: _______________
[ ] Propeller inspiziert              Zustand: ___________________
[ ] Antifouling erneuert              Produkt: ___________________

IPS-POD (wenn vorhanden)
[ ] Pod-Zinkanoden geprüft/gewechselt Zustand: ___________________
[ ] Pod-Gehäuse auf Korrosion geprüft Befund: ____________________
[ ] Faltenbälge visuell geprüft       Zustand: ___________________
[ ] Pod-Getriebeöl gewechselt         Zustand alt: _______________
[ ] Propeller poliert                 Zustand: ___________________
[ ] Antifouling erneuert              Produkt: ___________________
[ ] Joystick-Funktion geprüft         OK / Einschränkungen: _______
[ ] DPS-Funktion geprüft              OK / Einschränkungen: _______

AQUAMATIC STERNDRIVE (wenn vorhanden)
[ ] Getriebeöl gewechselt             Zustand alt: _______________
[ ] Zinkanoden gewechselt             Zustand alt: _______________
[ ] Faltenbälge visuell geprüft       Zustand: ___________________
[ ] Gimbal-Lager Spiel geprüft        Spiel: ____________________
[ ] Propeller inspiziert              Zustand: ___________________
[ ] Trimmfunktion geprüft             OK / Einschränkungen: _______

PROBELAUF
[ ] Motor gestartet                   Startverhalten: ____________
[ ] Öldruck bei Leerlauf              Wert: ____ bar
[ ] Temperatur nach 15 min            Wert: ____ °C
[ ] Drehzahl Leerlauf                 Wert: ____ U/min
[ ] Seewasseraustritt am Auspuff      OK / Auffälligkeiten: _______
[ ] Abgasfarbe                        Klar/weiß/schwarz/blau
[ ] Getriebe vorwärts/rückwärts       OK / Auffälligkeiten: _______
[ ] Keine abnormalen Geräusche        OK / Auffälligkeiten: _______

NÄCHSTE WARTUNG
Fällig bei: ____ Betriebsstunden oder __________ (Datum)
Besondere Hinweise: _______________________________________________

Unterschrift Eigner: ______________ Datum: ________________________
Unterschrift Werkstatt: ___________ Stempel: ______________________
```

---

## ANHANG E — Händler- und Werkstattverzeichnis

### E.1 Autorisierte Volvo Penta Center (Auswahl Deutschland)

| Werkstatt | Stadt | Spezialisierung |
|-----------|-------|----------------|
| Kuhnle Werft | Rechlin (Müritz) | D1/D2, Saildrive, Binnencharter |
| Marine Service Grömitz | Grömitz | IPS, D4/D6, Ostsee |
| Bootsservice Kröger | Kiel | Alle VP-Modelle, Saildrive-Spezialist |
| Heinrich Hüning | Lemmer (NL-Grenze) | D3, Aquamatic, Binnengewässer |
| Bodensee Yachting | Konstanz | D1/D2, Segelyachten, Süßwasser |
| Marine Center Heiligenhafen | Heiligenhafen | IPS, D4/D6, Ostsee |
| Yachtzentrum Berlin | Berlin-Spandau | D1/D2/D3, Binnenreviere |
| Bavaria Yachtbau | Giebelstadt | OEM-Werkstatt, alle D-Serien |
| Wauquiez/Dufour Service | verschiedene | OEM-Service, D2-Serie |

### E.2 Autorisierte Werkstätten (Auswahl Mittelmeer)

| Werkstatt | Land | Hafen | Spezialisierung |
|-----------|------|-------|----------------|
| Marina Port Adriano | Spanien | Mallorca | IPS, D6/D8, Superyachten |
| Marina di Loano VP Center | Italien | Loano | Alle Modelle |
| Sportina Marina | Kroatien | Portorož | D3/D4, Aquamatic |
| Olympic Marine | Griechenland | Lavrion | D2, Saildrive, Charter |
| Port Vauban | Frankreich | Antibes | IPS, D6/D8, Superyachten |

### E.3 Online-Ressourcen

| Ressource | URL-Hinweis | Inhalt |
|-----------|------------|--------|
| Volvo Penta EPC (Ersatzteilkatalog) | marinparts.volvopenta.com | Offizielle Teilenummern, Explosionszeichnungen |
| Volvo Penta Dealer Locator | volvopenta.com/dealer | Werkstattsuche weltweit |
| VP-Owners Forum (EN) | ybw.com/forums | Eigner-Erfahrungen, Tipps |
| Segeln-Forum (DE) | segeln-forum.de | Deutschsprachige VP-Diskussionen |
| Boote-Forum (DE) | boote-forum.de | Deutschsprachige VP-Diskussionen |

---

## ANHANG F — Motorraumplanung und Einbaurichtlinien

### F.1 Mindestabstände im Motorraum

| Bereich | Mindestabstand | Begründung |
|---------|---------------|-----------|
| Oberkante Motor → Bodenbrett | 100 mm (D1/D2), 150 mm (D3+) | Serviceraum für Ventildeckel, Filter |
| Seitlich Motor → Rumpfwand | 50 mm (D1), 80 mm (D2+) | Belüftung, Schlauchzugang |
| Auspuffkrümmer → brennbare Materialien | 200 mm oder isoliert | ISO 9094 Brandschutz |
| Kraftstoffleitung → Auspuff | 300 mm oder hitzeisoliert | ISO 9094 |
| Batterie → Motor | 500 mm empfohlen | Vibrationsschutz, Gasung |
| Luftfilter → nächste Wand | 50 mm | Freie Ansaugung |

### F.2 Belüftung Motorraum

**Berechnung des Mindest-Lüftungsquerschnitts:**

Für Saugmotoren (D1, D2-40 bis D2-60):
```
A_zuluft = P_kW × 25 cm² (Mindestquerschnitt Zuluft)
A_abluft = P_kW × 20 cm² (Mindestquerschnitt Abluft)
```

Für Turbomotoren (D2-75, D3, D4, D6):
```
A_zuluft = P_kW × 35 cm² (höherer Luftbedarf durch Turbo)
A_abluft = P_kW × 25 cm²
```

**Beispiele:**
- D1-30 (21 kW): Zuluft min. 525 cm², Abluft min. 420 cm²
- D2-75 (55 kW): Zuluft min. 1.925 cm², Abluft min. 1.375 cm²
- D4-300 (221 kW): Zuluft min. 7.735 cm², Abluft min. 5.525 cm²

### F.3 Schalldämmung

| Maßnahme | Dämpfung (dB) | Kosten (D2-Motor) |
|----------|-------------|-------------------|
| Schallschutz-Motorhaube (Schaum) | 5–8 dB | 250–450 € |
| Schalldämm-Matte Motorraum | 3–5 dB | 180–350 € |
| Elastische Motorlagerung (Standard) | 8–12 dB | inkl. im Motorpreis |
| Abgasschalldämpfer (Nassauspuff) | 15–20 dB | 350–650 € |
| Flexible Abgasschlauchverbindung | 2–3 dB | 80–120 € |
| Flexible Kühlwasserschläuche | 1–2 dB | inkl. im Motorpreis |
| Kumuliert alle Maßnahmen | 25–35 dB | 500–1.200 € |

**Typische Geräuschpegel (1 m Abstand):**
- D1-30 ohne Dämmung: 85 dB(A)
- D1-30 mit Dämmung: 68 dB(A)
- D2-75 ohne Dämmung: 92 dB(A)
- D2-75 mit Dämmung: 75 dB(A)
- D4-300 ohne Dämmung: 98 dB(A)
- D4-300 mit Dämmung: 78 dB(A)

### F.4 Motorbett-Spezifikationen

| Motor | Motorlager-Abstand (mm) | Lager-Typ | Härte (Shore A) | Lastgrenze pro Lager (kg) |
|-------|------------------------|----------|----------------|-------------------------|
| D1-13 | 180 × 160 | Typ 100 | 45 | 50 |
| D1-20 | 180 × 160 | Typ 100 | 45 | 60 |
| D1-30 | 200 × 180 | Typ 200 | 55 | 80 |
| D2-40 | 220 × 200 | Typ 200 | 55 | 100 |
| D2-50 | 220 × 200 | Typ 200 | 55 | 110 |
| D2-60 | 240 × 220 | Typ 300 | 60 | 130 |
| D2-75 | 240 × 220 | Typ 300 | 60 | 140 |
| D3-Serie | 280 × 260 | Typ 400 | 65 | 180 |
| D4-Serie | 320 × 300 | Typ 500 | 65 | 250 |
| D6-Serie | 360 × 340 | Typ 600 | 70 | 350 |

**Hinweis:** Motorlager nach 3.000–5.000 h prüfen. Verhärtete oder eingerissene Lager führen zu erhöhten Vibrationen und Geräuschen.

---

## ANHANG G — Volvo Penta Hybrid- und Elektroantriebe

### G.1 Übersicht

Seit 2021 bietet Volvo Penta Hybrid-Antriebssysteme an, die einen konventionellen Dieselmotor mit einem Elektromotor/Generator kombinieren:

| System | Komponenten | Leistung elektrisch | Anwendung |
|--------|-----------|-------------------|-----------|
| D4/D6 Hybrid | D4 oder D6 + Elektromaschine | 20–30 kW | Motoryachten 35–65 ft |
| IPS Hybrid | IPS500/600 + integrierte E-Maschine | 25–40 kW | Motoryachten 40–80 ft |
| Volvo Penta Electric | Rein elektrischer Antrieb | 50–150 kW | Tagesboote, Fähren, Tender |

### G.2 Betriebsmodi Hybrid

1. **Diesel-Modus:** Konventioneller Dieselbetrieb (Überfahrten)
2. **Hybrid-Modus:** Diesel + Elektro für maximale Effizienz
3. **Boost-Modus:** Diesel + Elektro für maximale Leistung
4. **Elektro-Modus:** Rein elektrisch (Hafen, Ankerbuchten, Naturschutz)
5. **Lade-Modus:** Diesel lädt Batterien (auf See)

### G.3 Batteriesystem

| Parameter | Wert |
|-----------|------|
| Batterietyp | Lithium-Ionen (NMC) |
| Kapazität | 30–60 kWh (modular) |
| Spannung | 650V DC |
| Gewicht | 180–360 kg (je nach Kapazität) |
| Reichweite elektrisch | 5–15 NM bei 5 kn (verdrängend) |
| Ladezeit (Landstrom 63A/400V) | 3–6 Stunden |
| Lebensdauer | 3.000–5.000 Lade-/Entladezyklen |
| Listenpreis (30 kWh) | ca. 28.000 € |
| Listenpreis (60 kWh) | ca. 48.000 € |

### G.4 Praxiserfahrungen Hybrid (Stand 2025)

- Kraftstoffeinsparung im gemischten Betrieb: 10–25 % (herstellerangabe: bis 30 %)
- Geräuschvorteil im E-Modus: dramatisch (Kabinengeräusch < 50 dB(A))
- Komplexität: erheblich höherer Wartungsaufwand (Batterie-Management, Hochvolt-Sicherheit)
- Fachpersonal: Hochvolt-Zertifizierung (>600V) für Wartung erforderlich
- Verfügbarkeit Werkstätten: noch begrenzt (nur große VP Center)
- Amortisation: ab ca. 400 Betriebsstunden/Jahr wirtschaftlich interessant

---

## ANHANG H — Motoröl-Analysetabelle

### H.1 Grenzwerte für Motoröl-Laboranalyse

Eine Motorölanalyse durch ein Speziallabor (z. B. Oelcheck GmbH, WearCheck) gibt Aufschluss über den Motorzustand. Kosten: 25–45 € pro Probe.

| Parameter | Einheit | Normalbereich D1/D2 | Normalbereich D3/D4/D6 | Warnung | Kritisch |
|-----------|---------|--------------------|-----------------------|---------|---------|
| Eisen (Fe) | ppm | <50 | <60 | 50–100 | >100 |
| Kupfer (Cu) | ppm | <20 | <25 | 20–40 | >40 |
| Blei (Pb) | ppm | <10 | <15 | 10–30 | >30 |
| Aluminium (Al) | ppm | <15 | <20 | 15–30 | >30 |
| Chrom (Cr) | ppm | <5 | <8 | 5–15 | >15 |
| Zinn (Sn) | ppm | <10 | <15 | 10–20 | >20 |
| Silizium (Si) | ppm | <20 | <25 | 20–40 | >40 |
| Natrium (Na) | ppm | <50 | <50 | 50–100 | >100 |
| Wasser | % | <0,1 | <0,1 | 0,1–0,5 | >0,5 |
| Kraftstoff | % | <2 | <2 | 2–5 | >5 |
| Viskosität 100°C | cSt | 12–16 (15W-40) | 12–16 | ±20 % | ±30 % |
| TBN (Basenzahl) | mg KOH/g | >5 | >5 | 3–5 | <3 |
| Ruß | % | <0,5 | <1,0 | 0,5–2,0 | >2,0 |

### H.2 Interpretation der Ergebnisse

| Befund | Bedeutung | Maßnahme |
|--------|----------|---------|
| Eisen erhöht | Verschleiß an Zylindern, Kolbenringen, Nockenwelle | Ölwechselintervall verkürzen, Kompressionstest |
| Kupfer erhöht | Lager-Verschleiß (Pleuellager, Hauptlager) | Motorinspektion, Lagerspiel prüfen |
| Blei erhöht | Schwerer Lagerverschleiß | Sofortige Motorinspektion! |
| Aluminium erhöht | Kolbenverschleiß oder Turbo-Verschleiß | Kompressionstest, Turbo prüfen |
| Silizium erhöht | Schmutz/Sand im Ölkreislauf (defekter Luftfilter?) | Luftfilter prüfen/wechseln, Ölwechsel |
| Natrium erhöht | Kühlmittel im Öl (Kopfdichtung!) | Sofort! Kopfdichtung, Ölkühler prüfen |
| Wasser erhöht | Kondenswasser oder Kühlmitteleintritt | Ursache finden (Kopfdichtung, Ölkühler, Kondens) |
| Kraftstoff erhöht | Diesel im Öl (Injektor-Leckage, Kurzstrecke) | Injektoren prüfen, Ölwechsel |
| TBN niedrig | Öl ist verbraucht (Säureneutralisierung erschöpft) | Ölwechsel fällig |
| Ruß hoch | Unvollständige Verbrennung | Injektoren, Turbo, Luftfilter prüfen |

---

## ANHANG I — Volvo Penta Motorenhistorie und Vorgängermodelle

### I.1 Historische Modellzuordnung

Viele Boote auf dem Gebrauchtmarkt haben ältere Volvo Penta Motoren. Diese Übersicht hilft bei der Zuordnung:

| Altes Modell | Bauzeitraum | PS | Zylinder | Nachfolger | Anmerkung |
|-------------|------------|-----|---------|-----------|-----------|
| MD2010 | 1993–2005 | 10 | 1 | D1-13 | Direkter Nachfolger |
| MD2020 | 1993–2005 | 19 | 2 | D1-20 | Direkter Nachfolger |
| MD2030 | 1993–2005 | 29 | 3 | D1-30 | Direkter Nachfolger |
| MD2040 | 1993–2005 | 40 | 4 | D2-40 | Ähnliche Leistung |
| MD22 | 1990–2003 | 36–59 | 4 | D2-40/D2-60 | Legendärer Motor |
| 2003 / 2003T | 1983–1993 | 28–43 | 3 | D1-30/D2-40 | Sehr langlebig |
| MD17C/D | 1978–1993 | 25–36 | 2 | D1-30 | Einfach, robust |
| TAMD22 | 1990–2003 | 78 | 4 | D2-75 | Turbo-Version des MD22 |
| TAMD31 | 1988–2003 | 130–150 | 4 | D3-150 | Weit verbreitet |
| TAMD41 | 1988–2005 | 200 | 6 | D6-310 | Legendär zuverlässig |
| TAMD42 | 1988–2005 | 230 | 6 | D6-340 | WJ-Version für Jet |
| KAD42 | 1993–2003 | 230 | 6 | D4-260 | Kompressor + Turbo |
| KAD44 | 1993–2003 | 260–300 | 6 | D4-300 | Kompressor + Turbo |
| D7A-TA | 2001–2008 | 260–320 | 6 | D6-310/340 | Erste Common-Rail VP |
| D12-Serie | 2000–2012 | 400–715 | 6 | D11/D13 | LKW-basiert |

### I.2 Ersatzteilverfügbarkeit historischer Modelle

| Motor-Generation | Ersatzteil-Status (2025) | Anmerkung |
|-----------------|------------------------|-----------|
| MD-Serie (1978–2005) | Begrenzt über VP, gut über Aftermarket (Orbitrade) | Die meisten Verschleißteile verfügbar |
| 2003-Serie (1983–1993) | Nur Aftermarket | Impeller, Dichtungen, Filter noch erhältlich |
| TAMD-Serie (1988–2005) | Gut über VP und Aftermarket | Noch weit verbreitet, gute Versorgung |
| KAD-Serie (1993–2003) | Eingeschränkt über VP | Kompressor-Teile schwer zu bekommen |
| D1-D6 aktuell (2004–heute) | Vollständig | Alle Teile lieferbar |

---

## ANHANG J — Saisonale Checkliste nach Revier

### J.1 Ostsee (Brackwasser, Frost November–März)

**Besonderheiten:**
- Niedriger Salzgehalt (7–15 ppt) — Aluminium-Anoden bevorzugt
- Frost: -15 bis -25 °C möglich — Frostschutz -30 °C Minimum
- Seegras und Muschelbewuchs im Sommer

| Monat | Maßnahme |
|-------|---------|
| April | Auswintern: Impeller neu, Seewassersystem spülen, Batterie laden |
| Mai | Saisonstart: Probelauf, EVC-Check, Zinkanoden prüfen |
| Juli | Zwischenkontrolle: Seewasserfilter (Seegras!), Ölstand |
| September | Saisonende: Zinkanoden prüfen (halbe Saison) |
| Oktober | Einwintern: Komplettes Programm (Abschnitt 16.2) |
| November–März | Winterlager: Batterie-Erhaltungsladung, monatlich Bilge prüfen |

### J.2 Mittelmeer (Salzwasser, frostfrei)

**Besonderheiten:**
- Hoher Salzgehalt (35–38 ppt) — Zink-Anoden verwenden
- Kein Frost, aber Bewuchs ganzjährig
- Wassertemperatur bis 28 °C — Kühlleistung beachten

| Monat | Maßnahme |
|-------|---------|
| März | Frühjahrsmotorservice: Öl, Filter, Impeller |
| Mai | Zinkanoden prüfen (halbe Saison) |
| Juli | Seewasserfilter regelmäßig prüfen (Quallen!), Ladeluftkühler-Temp |
| September | Zinkanoden erneut prüfen, Bewuchs entfernen |
| November | Winterservice (auch ohne Frostgefahr): Öl, Filter, Getriebe |
| Ganzjährig | Propeller/Saildrive regelmäßig reinigen (Bewuchs) |

### J.3 Binnengewässer (Süßwasser)

**Besonderheiten:**
- Süßwasser: Magnesium-Anoden verwenden (nicht Zink!)
- Kein Salz, aber Algen und Sediment
- Oft flache Gewässer — Seewasserfilter beachten

| Monat | Maßnahme |
|-------|---------|
| April | Auswintern: Standard-Programm |
| Juli | Seewasserfilter prüfen (Algen, Sand) |
| Oktober | Einwintern: Frostschutz, Seewassersystem entleeren |
| Ganzjährig | Anodenverbrauch deutlich geringer als in Salzwasser |

---

## ANHANG K — Volvo Penta Motorenvergleich für Bootskäufer

### K.1 Entscheidungshilfe: Welcher Motor für welches Boot?

**Segelyachten nach Bootslänge und Verdrängung:**

| Bootslänge (ft) | Typische Verdrängung (kg) | Empfohlener Motor | Empfohlener Antrieb | Budget Motor+Antrieb |
|-----------------|--------------------------|------------------|--------------------|--------------------|
| 25–30 | 2.500–4.500 | D1-13 oder D1-20 | 120S Saildrive | 12.000–14.000 € |
| 30–34 | 4.000–6.500 | D1-20 oder D1-30 | 120S oder 130S | 14.000–17.000 € |
| 34–38 | 5.500–9.000 | D1-30 oder D2-40 | 130S Saildrive | 16.000–21.000 € |
| 38–42 | 8.000–12.000 | D2-40 oder D2-50 | 130S Saildrive | 20.000–24.000 € |
| 42–46 | 10.000–15.000 | D2-50 oder D2-60 | 130S oder 150S | 23.000–28.000 € |
| 46–52 | 14.000–20.000 | D2-60 oder D2-75 | 150S Saildrive | 27.000–32.000 € |
| 52–58 | 18.000–28.000 | D2-75 | 150S oder Welle | 31.000–36.000 € |
| 58+ | 25.000+ | D3-110 oder größer | Wellenanlage | 35.000+ € |

**Motorboote nach Bootstyp und gewünschter Geschwindigkeit:**

| Bootstyp | Geschwindigkeit | Empfohlener Motor | Empfohlener Antrieb |
|----------|----------------|------------------|-------------------|
| Verdränger 30–40 ft | 8–12 kn | D4-260 (Einzel) | IPS400 oder Welle |
| Verdränger 40–55 ft | 10–14 kn | D6-310/340 (Twin) | IPS500 oder Welle |
| Semi-Verdränger 35–45 ft | 15–22 kn | D4-300 (Twin) | IPS400 |
| Semi-Verdränger 45–60 ft | 18–28 kn | D6-380 (Twin) | IPS600 |
| Gleiter 25–32 ft | 25–35 kn | D3-150/170 (Twin) | Aquamatic DPS-A |
| Gleiter 32–40 ft | 30–40 kn | D4-300 (Twin) | Aquamatic DPH-A |
| Gleiter 40–50 ft | 30–38 kn | D6-440 (Twin) | IPS600 |
| Schneller Gleiter 50–70 ft | 35–45 kn | D8-550 (Twin) | IPS700 |
| Superyacht 70–100 ft | 22–30 kn | D13-1000 (Twin) | IPS950 |

### K.2 TCO (Total Cost of Ownership) über 10 Jahre

Vergleich der Gesamtkosten für einen typischen Einsatz über 10 Jahre (3.000 Betriebsstunden gesamt):

| Kostenart | D1-30 (Segelyacht) | D2-75 (Große SY) | D4-300 + IPS400 (Motorboot) |
|-----------|-------------------|------------------|---------------------------|
| Anschaffung Motor + Antrieb | 16.500 € | 31.500 € | 58.000 € |
| Diesel (10 Jahre) | 11.160 € | 25.200 € | 75.600 € |
| Wartung (Material) | 1.650 € | 2.500 € | 4.800 € |
| Wartung (Arbeitskosten) | 2.800 € | 4.200 € | 7.500 € |
| Reparaturrücklagen | 3.000 € | 5.000 € | 12.000 € |
| Saildrive-Membran (1×) | 1.000 € | 1.200 € | — |
| IPS-Pod-Service (2×) | — | — | 10.000 € |
| Zinkanoden (10 Jahre) | 500 € | 650 € | 3.500 € |
| **Gesamt 10 Jahre** | **36.610 €** | **70.250 €** | **171.400 €** |
| **Pro Betriebsstunde** | **12,20 €** | **23,42 €** | **57,13 €** |

---

## ANHANG L — Typische Bootshersteller und VP-Motorisierung

### L.1 Segelyacht-Hersteller und Standard-VP-Motoren

| Hersteller | Modell | Standard-VP-Motor | Saildrive |
|-----------|--------|------------------|----------|
| Bavaria | Bavaria 34 | D1-20 | 120S |
| Bavaria | Bavaria 37 | D1-30 | 130S |
| Bavaria | Bavaria 42 | D2-40 | 130S |
| Bavaria | Bavaria 46 | D2-60 | 150S |
| Bavaria | Bavaria 51 | D2-75 | 150S |
| Bénéteau | Océanis 30.1 | D1-20 | 120S |
| Bénéteau | Océanis 35.1 | D1-30 | 130S |
| Bénéteau | Océanis 40.1 | D2-40 | 130S |
| Bénéteau | Océanis 46.1 | D2-60 | 150S |
| Bénéteau | Océanis 51.1 | D2-75 | 150S |
| Hallberg-Rassy | HR 310 | D1-20 | 120S |
| Hallberg-Rassy | HR 340 | D1-30 | 130S |
| Hallberg-Rassy | HR 372 | D2-40 | 130S |
| Hallberg-Rassy | HR 412 | D2-75 | 150S |
| Hallberg-Rassy | HR 44 | D2-75 | 150S |
| Hallberg-Rassy | HR 50 | D3-110 | Welle |
| Hanse | 348 | D1-20 | 120S |
| Hanse | 388 | D1-30 | 130S |
| Hanse | 418 | D2-40 | 130S |
| Hanse | 460 | D2-60 | 150S |
| Hanse | 510 | D2-75 | 150S |
| Jeanneau | SO 319 | D1-20 | 120S |
| Jeanneau | SO 349 | D1-30 | 130S |
| Jeanneau | SO 410 | D2-40 | 130S |
| Jeanneau | SO 440 | D2-60 | 150S |
| Jeanneau | SO 490 | D2-75 | 150S |
| Dehler | 34 | D1-20 | 120S |
| Dehler | 38 | D2-40 | 130S |
| Dehler | 42 | D2-60 | 150S |
| Dehler | 46 | D2-75 | 150S |
| Najad | 395 | D2-40 | 130S |
| Najad | 440 | D2-60 | 150S |
| Najad | 505 | D2-75 | 150S |
| Sweden Yachts | 390 | D2-40 | 130S |
| Sweden Yachts | 45 | D2-75 | 150S |
| Oyster | 565 | D3-110 | Welle |
| Oyster | 675 | D4-260 | Welle |

### L.2 Motorboot-Hersteller und Standard-VP-Motoren

| Hersteller | Modell | Standard-VP-Motor | Antrieb | Anzahl |
|-----------|--------|------------------|---------|--------|
| Nimbus | T9 | D3-220 | Aquamatic DPS-A | 1 |
| Nimbus | 305 Coupé | D4-260 | Aquamatic DPH-A | 1 |
| Nimbus | 365 Coupé | D4-300 | IPS400 | 1 |
| Nimbus | 405 Coupé | D6-340 | IPS500 | 1 |
| Axopar | 28 T-Top | D3-150 | Aquamatic DPS-A | 1 |
| Axopar | 37 Sun Top | D4-300 | IPS400 | 2 |
| Axopar | 45 XC | D6-380 | IPS600 | 2 |
| Greenline | 40 | D3-170 | Aquamatic DPS-A | 1 |
| Greenline | 48 | D6-340 | IPS500 | 2 |
| Princess | V40 | D4-300 | IPS400 | 2 |
| Princess | V50 | D6-380 | IPS600 | 2 |
| Princess | V65 | D6-440 | IPS600 | 2 |
| Princess | V78 | D8-550 | IPS700 | 2 |
| Prestige | 420 | D4-300 | IPS400 | 2 |
| Prestige | 520 | D6-380 | IPS600 | 2 |
| Prestige | 690 | D8-550 | IPS700 | 2 |
| Absolute | 48 Coupé | D6-380 | IPS600 | 2 |
| Absolute | 60 Fly | D8-550 | IPS700 | 2 |
| Fjord | 44 Open | D6-440 | IPS600 | 2 |
| Sunseeker | Manhattan 52 | D6-440 | IPS600 | 2 |
| Sunseeker | Predator 65 | D8-550 | IPS700 | 2 |

---

## ANHANG M — Umrechnungstabellen und Formeln

### M.1 Leistungsumrechnung

| Von | Nach | Faktor |
|-----|------|--------|
| PS (metrisch) | kW | × 0,7355 |
| kW | PS (metrisch) | × 1,3596 |
| HP (imperial) | kW | × 0,7457 |
| kW | HP (imperial) | × 1,3410 |
| PS (metrisch) | HP (imperial) | × 0,9863 |

### M.2 Verbrauchsumrechnung

| Von | Nach | Faktor |
|-----|------|--------|
| l/h (Diesel) | kg/h | × 0,832 |
| l/h | US gal/h | × 0,2642 |
| l/NM | Kennzahl | Verbrauch / Geschwindigkeit |

### M.3 Nützliche Formeln

**Rumpfgeschwindigkeit (Verdrängungsfahrt):**
```
V_max (kn) = 1,34 × √LWL (ft)
```

**Spezifischer Kraftstoffverbrauch:**
```
SFC (g/kWh) = Verbrauch (kg/h) / Leistung (kW) × 1000
Guter Diesel: 200–240 g/kWh
```

**Reichweite (Verdrängungsfahrt):**
```
Reichweite (NM) = Tankinhalt (l) / Verbrauch (l/h) × Geschwindigkeit (kn)
```

**Propellerdrehzahl:**
```
n_prop (U/min) = n_motor (U/min) / Untersetzung
```

**Schlupf:**
```
Schlupf (%) = (1 - V_real / V_theoretisch) × 100
Normaler Schlupf: 10–15 % (Verdrängung), 5–10 % (Gleiter)
```

---

## ANHANG N — Erweiterte Troubleshooting-Referenz

### N.1 Diagnose mit Bordmitteln (ohne VODIA)

Nicht immer steht eine VP-Werkstatt mit VODIA-Diagnosetool zur Verfügung. Folgende Messungen lassen sich mit Bordmitteln durchführen:

**Benötigtes Werkzeug:**
- Multimeter (Spannung, Widerstand)
- Kompressionsprüfer (M14 oder M12 Adapter je nach Motor)
- Mechanischer Öldruckprüfer (1/8" BSPT Anschluss)
- Infrarot-Thermometer
- Manometer für Ladedruck (0–3 bar)
- Transparenter Kraftstoffschlauch (Luftblasen sichtbar)

**Diagnose 1: Kompressionstest**
1. Motor auf Betriebstemperatur bringen
2. Alle Glühkerzen/Injektoren ausbauen
3. Kompressionsprüfer einschrauben
4. Anlasser betätigen (ca. 8 Umdrehungen)
5. Werte notieren und vergleichen

| Motor | Soll-Kompression | Min. akzeptabel | Max. Unterschied zwischen Zylindern |
|-------|-----------------|----------------|-------------------------------------|
| D1-Serie | 30–35 bar | 25 bar | 3 bar |
| D2-Serie | 28–33 bar | 23 bar | 3 bar |
| D3-Serie | 25–30 bar | 20 bar | 2,5 bar |
| D4/D6-Serie | 26–32 bar | 22 bar | 3 bar |

**Interpretation:**
- Alle Zylinder gleichmäßig, Werte im Soll → Motor in Ordnung
- Ein Zylinder deutlich niedriger → Ventilproblem oder Kolbenring
- Alle Zylinder niedrig → Allgemeiner Verschleiß, Motor am Lebensende
- Nass-Test (Öl in Zylinder): Wert steigt → Kolbenringe; Wert gleich → Ventile

**Diagnose 2: Öldruck manuell messen**
1. Öldrucksensor-Leitung abschrauben
2. Mechanisches Manometer anschließen
3. Motor starten

| Motor | Leerlauf-Öldruck (warm) | Öldruck bei 3.000 U/min |
|-------|------------------------|------------------------|
| D1-Serie | min. 1,0 bar | 3,0–4,5 bar |
| D2-Serie | min. 1,5 bar | 3,5–5,0 bar |
| D3-Serie | min. 1,5 bar | 3,5–5,5 bar |
| D4/D6-Serie | min. 2,0 bar | 4,0–6,0 bar |

**Diagnose 3: Ladedruckmessung (Turbomotoren)**
1. Ladeluftschlauch nach Turbo mit T-Stück versehen
2. Manometer anschließen
3. Motor unter Last (Fahrt, Volllast)

| Motor | Soll-Ladedruck (Volllast) |
|-------|--------------------------|
| D2-75 | 0,6–0,9 bar |
| D3-110 | 0,8–1,1 bar |
| D3-220 | 1,2–1,6 bar |
| D4-260 | 1,4–1,8 bar |
| D4-300 | 1,6–2,0 bar |
| D6-310 | 1,4–1,8 bar |
| D6-440 | 1,8–2,2 bar |

**Diagnose 4: Kühlsystem-Temperaturprofil**
Mit Infrarot-Thermometer an verschiedenen Stellen messen:

| Messpunkt | Soll-Temperatur | Abweichung = Problem |
|-----------|----------------|---------------------|
| Thermostatgehäuse | 82–92 °C (je nach Motor) | Zu kalt = Thermostat offen klemmt |
| Zylinderkopf | 85–95 °C | Zu heiß = Kühlkanäle verstopft |
| Wärmetauscher Eingang | 80–90 °C | — |
| Wärmetauscher Ausgang | 60–75 °C | Zu hoch = Wärmetauscher verkalkt |
| Seewasser-Auslass | 35–50 °C | Zu heiß = Seewasserfluss reduziert |

### N.2 Notfall-Reparaturen auf See

**Impeller-Wechsel auf See:**
Zeitbedarf: 15–30 Minuten (wenn geübt)
1. Motor abstellen, Seeventil schließen
2. Impellerdeckel abschrauben (2–4 Schrauben)
3. Alten Impeller herausziehen (Spitzzange oder Impeller-Abzieher)
4. Alle Flügelreste zählen! Fehlende Teile im System → Seewasserfilter und Wärmetauscher prüfen
5. Neuen Impeller einsetzen (mit Glycerin oder Seifenwasser schmieren)
6. Deckel aufschrauben, Seeventil öffnen
7. Motor starten, Seewasserausstoß am Auspuff prüfen

**Luft im Kraftstoffsystem (D1/D2 mechanisch):**
Zeitbedarf: 5–15 Minuten
1. Handpumpe am Vorfilter betätigen (30–50 Hübe)
2. Entlüftungsschraube am Hauptfilter öffnen
3. Pumpen bis blasenfreier Diesel kommt
4. Schraube schließen
5. Motor starten (ggf. 30–60 Sekunden Anlasszeit normal)

**Keilriemen gerissen (provisorische Lösung):**
- Damenstrumpfhose als Notriemen (hält 30–60 Minuten)
- Motor nur mit niedriger Drehzahl betreiben
- Lichtmaschine lädt nicht → Batterie-Reserven beachten
- Frischwasserpumpe bei einigen Modellen keilriemengetrieben → Überhitzungsgefahr!

**Kühlwasserverlust (Notbetrieb):**
1. Leck identifizieren und wenn möglich abdichten
2. Süßwasser (notfalls Trinkwasser) nachfüllen
3. Motor mit reduzierter Drehzahl betreiben
4. Temperatur ständig überwachen
5. Hafen anlaufen, Reparatur durchführen

### N.3 Bordapotheke für Volvo Penta Motoren

**Empfohlene Ersatzteile an Bord:**

| Teil | Grund | Preis | Gewicht |
|------|-------|-------|---------|
| Impeller (2 Stück) | Häufigster Ausfall, schneller Wechsel | 70–110 € | 0,2 kg |
| Impeller-Dichtung (O-Ring/Papier) | Gehört zum Impellerwechsel | 5–12 € | 0,01 kg |
| Kraftstofffilter (Haupt + Vor) | Dieselpest, Verschmutzung | 40–70 € | 0,3 kg |
| Keilriemen | Riss = kein Laden, ggf. Überhitzung | 18–30 € | 0,2 kg |
| Zinkanoden (Saildrive/Wärmetauscher) | Korrosionsschutz | 50–80 € | 0,5 kg |
| Motoröl (2 l Reserve) | Nachfüllen unterwegs | 20–25 € | 1,8 kg |
| Kühlmittel (1 l Konzentrat) | Nachfüllen bei Verlust | 12–18 € | 1,1 kg |
| Schlauchschellen (sortiert) | Undichte Schläuche | 15–25 € | 0,3 kg |
| Kabelbinder (sortiert) | Provisorische Befestigung | 8–12 € | 0,1 kg |
| WD-40 / Kontaktspray | Korrodierte Stecker, Entfeuchtung | 8–12 € | 0,3 kg |
| Dichtmasse (Sikaflex 291i) | Notdichtungen | 12–18 € | 0,3 kg |
| Isolierband + Schrumpfschlauch | Kabelreparatur | 8–12 € | 0,1 kg |
| Sicherungen (Satz, passend) | Elektrische Ausfälle | 10–15 € | 0,05 kg |
| **Gesamtpaket** | | **ca. 275–450 €** | **ca. 5 kg** |

**Werkzeug-Minimum für VP-Motorservice:**
- Ringschlüssel-Satz 8–19 mm
- Schraubendreher (Kreuz + Schlitz, verschiedene Größen)
- Zangensatz (Kombizange, Spitzzange, Seitenschneider)
- Impeller-Abzieher (VP-Originalwerkzeug empfohlen)
- Ölfilter-Schlüssel (passend für VP-Filter)
- Auffangschale für Ölwechsel
- Taschenlampe (Kopflampe ideal)
- Multimeter (wasserdicht)
- Einweg-Handschuhe und Lappen

---

## ANHANG O — Volvo Penta im Vergleich zu Wettbewerbern

### O.1 Segelyacht-Segment: Volvo Penta D2 vs. Yanmar JH

| Kriterium | VP D2-40 | Yanmar 3JH40 |
|-----------|---------|-------------|
| Leistung | 37,5 PS | 40 PS |
| Zylinder | 2 | 3 |
| Hubraum | 1.124 cm³ | 1.115 cm³ |
| Gewicht | 137 kg | 135 kg |
| Einspritzung | Common-Rail | Mechanisch |
| Saildrive | 130S (VP) | SD25 (Yanmar) |
| EVC/Elektronik | EVC2 optional | SmartSwitch optional |
| Listpreis Motor+SD | ca. 20.800 € | ca. 18.500 € |
| Wartungskosten/Jahr | ca. 505 € | ca. 420 € |
| Ersatzteil-Verfügbarkeit | Sehr gut | Gut |
| Service-Netzwerk Europa | 4.000+ Partner | 3.500+ Partner |
| NMEA 2000 | Integriertes Gateway | Adapter nötig |
| Stärken | Elektronik, Integration | Einfachheit, Preis |
| Schwächen | Komplexer, teurer | Weniger modern |

### O.2 Motorboot-Segment: Volvo Penta IPS vs. Mercury Zeus

| Kriterium | VP IPS600 (D6-380) | Mercury Zeus (Cummins QSC 380) |
|-----------|-------------------|-------------------------------|
| Leistung | 380 PS | 380 PS |
| Antriebsprinzip | Pod (Zugpropeller) | Pod (Druckpropeller) |
| Joystick | JA (Standard) | JA (Standard) |
| DPS | JA (Option) | Skyhook (Option) |
| Kraftstoffeffizienz | Sehr gut | Gut |
| Manövrierfähigkeit | Hervorragend | Sehr gut |
| Service-Netzwerk | Global stark | Nordamerika stark |
| Listenpreis (Twin) | ca. 156.000 € | ca. 148.000 € |
| Stärken | Effizienz, Geräusch | Leistungsdichte |
| Schwächen | Preis, Pod-Korrosion | Weniger EU-Service |

### O.3 Entscheidungshilfe: Wann Volvo Penta?

**Volvo Penta ist die beste Wahl wenn:**
- Das Boot in Europa betrieben wird (bestes Servicenetzwerk)
- Elektronische Integration wichtig ist (EVC2, NMEA 2000, VP Connect)
- IPS-Antrieb gewünscht ist (Marktführer, meiste Erfahrung)
- Saildrive gewünscht ist (Volvo Penta hat die größte Auswahl)
- Wiederverkaufswert zählt (VP-Motoren halten Wert besser)

**Alternative Hersteller bevorzugen wenn:**
- Budget begrenzt ist (Yanmar, Beta Marine günstiger)
- Einfachheit über Technologie geht (mechanische Yanmar/Beta)
- Boot in Nordamerika betrieben wird (Mercury, Cummins besser vernetzt)
- Sehr hohe Leistungen gebraucht werden (MTU, Caterpillar über 1.000 PS)

---

## ANHANG P — Versicherungstechnische Hinweise

### P.1 Versicherungsrelevante Aspekte

| Thema | Relevanz für Versicherung |
|-------|--------------------------|
| Saildrive-Membran | Viele Kaskoversicherungen verlangen Nachweis des Membran-Alters |
| Wartungsnachweise | Schadensregulierung kann bei fehlendem Serviceheft verweigert werden |
| Chip-Tuning | Nicht gemeldete Leistungserhöhung kann Versicherungsschutz gefährden |
| IPS-Anodenpflege | Korrosionsschäden durch Vernachlässigung = Eigenverschulden |
| Zahnriemen (D3) | Motorschaden durch überfälligen Zahnriemen = Fahrlässigkeit |
| Diesel-Qualität | Motorschaden durch verunreinigten Diesel → Haftungsfrage |

### P.2 Empfehlung Dokumentation

Folgende Dokumente sollten stets an Bord und aktuell sein:
1. **Motorhandbuch** (Original Volvo Penta)
2. **Serviceheft** (alle Wartungen mit Datum, Stunden, ausführende Werkstatt)
3. **Rechnungen** (Originalteile-Nachweise)
4. **Saildrive-Membran-Protokoll** (Einbaudatum, letzte Inspektion)
5. **EVC-Diagnoseprotokoll** (letzter Werkstattbesuch)
6. **Ölanalyse-Berichte** (wenn durchgeführt)

---

## ANHANG Q — Spezialwerkzeuge Volvo Penta

### Q.1 Empfohlene Spezialwerkzeuge

| Werkzeug | VP-Teilenummer | Anwendung | Preis (2025) |
|----------|---------------|-----------|-------------|
| Impellerausziehwerkzeug | 3838836 | Impellerwechsel D1/D2 | 45 € |
| Impellerausziehwerkzeug (groß) | 3843278 | Impellerwechsel D3/D4/D6 | 65 € |
| Ölfilterband | 9997334 | Ölfilter-Demontage | 28 € |
| Ventilspiel-Einstellwerkzeug | 9996178 | Ventilspiel D1/D2 | 35 € |
| Zahnriemen-Spannwerkzeug | 9997378 | Zahnriemen D3 | 85 € |
| Kompressionsprüfer-Adapter M14 | 9996560 | Kompressionstest D1/D2 | 42 € |
| Kompressionsprüfer-Adapter M12 | 9996561 | Kompressionstest D3/D4/D6 | 42 € |
| CAN-Bus-Abschlusswiderstand | 22907232 | EVC-Diagnose | 35 € |
| Saildrive-Membranpresswerkzeug | 3862914 | Membrantausch | 120 € |
| Propellerabzieher Saildrive | 3843960 | Propellerwechsel | 55 € |
| Duoprop-Montagewerkzeug | 3860831 | Propellerwechsel Aquamatic/IPS | 75 € |

### Q.2 Aftermarket-Alternativen

Viele VP-Spezialwerkzeuge sind auch von Drittanbietern erhältlich:
- **Impeller-Abzieher:** Jabsco-Universalabzieher (ca. 25 €, passt für die meisten Modelle)
- **Ölfilterband:** Standard-KFZ-Werkzeug (10–15 €)
- **Kompressionsprüfer:** Universal-Satz mit Adaptern (50–80 €, deckt alle Motoren ab)

---

## ANHANG R — Motorinstallation und CE-Zertifizierung

### R.1 Anforderungen an die Motorinstallation (RCD 2013/53/EU)

| Anforderung | Norm | Relevanz |
|-------------|------|---------|
| Brandschutz Motorraum | ISO 9094 | Abstände, Materialien, Löschanlage |
| Kraftstoffsystem | ISO 10088 | Tankbefestigung, Leitungsführung, Belüftung |
| Abgasanlage | ISO 8178 | Emissionsgrenzwerte, Ableitung |
| Belüftung | ISO 11105 | Mindest-Lüftungsquerschnitte |
| Elektrische Installation | ISO 10133 (DC) / 13297 (AC) | Kabelquerschnitte, Sicherungen, Erdung |
| Propellerschutz | ISO 15085 | Schutz vor rotierenden Teilen |
| Geräuschemission | ISO 14509 | Grenzwerte ab 2.5 m Bootslänge |
| Lenkung | ISO 8847/8848 | Hydraulik-/Seilzuglenkung, Rückfallebene |

> ⚠️ **ZU PRÜFEN (Audit):** In der Zeile „Propellerschutz" ist **ISO 15085** angegeben. ISO 15085:2003 regelt jedoch „Small craft — Man-overboard prevention and recovery" (Schutz vor Über-Bord-Gehen und Wiedereinstieg) — nicht den Schutz vor rotierenden Teilen/Propellerschutz. Die Normnummer passt nicht zum zitierten Scope. Eine eindeutig korrekte RCD-Norm speziell für Propellerschutz ist nicht zweifelsfrei belegbar, daher nur markiert und NICHT ersetzt. Quelle: iso.org/standard/26408.html.

### R.2 CE-Konformität bei Remotoring

Beim Austausch eines Motors (Remotoring) ist zu beachten:
- Der neue Motor muss die aktuell gültigen Emissionsgrenzwerte einhalten
- Bei Leistungsänderung > 15 %: Stabilitätsnachweis erforderlich (ISO 12217)
- Bei Antriebswechsel (z. B. Saildrive → Welle): ggf. neue CE-Bewertung
- Dokumentation: Einbauerklärung, Konformitätserklärung Motor, Prüfprotokoll Abgasanlage

### R.3 Gewichtsverteilung und Schwerpunktlage

| Motor | Gewicht (Motor + Antrieb) | Empfohlene CG-Position |
|-------|--------------------------|----------------------|
| D1-13 + 120S | 117 kg | 40–45 % LWL von Bug |
| D1-30 + 130S | 164 kg | 42–47 % LWL von Bug |
| D2-40 + 130S | 182 kg | 43–48 % LWL von Bug |
| D2-75 + 150S | 254 kg | 44–48 % LWL von Bug |
| D4-300 + IPS400 | 575 kg | 45–50 % LWL von Bug |
| D6-440 + IPS600 | 735 kg | 46–51 % LWL von Bug |
| 2 × D6-440 + IPS600 | 1.470 kg | 47–52 % LWL von Bug |

**Hinweis für AYDI-Strukturmodul:** Bei Remotoring muss die Gewichtsänderung in der Trimmberechnung berücksichtigt werden. Eine D2-75 (254 kg) als Ersatz für einen alten MD22 (230 kg) erhöht das Gewicht um 24 kg — bei schweren Booten (>10 t) vernachlässigbar, bei leichten Booten (5 t) kann dies den Trimm um 0,1–0,2° verändern.

---

## ANHANG S — Quellenverzeichnis

### S.1 Primärquellen

| Quelle | Herausgeber | Jahr | Confidence |
|--------|-----------|------|-----------|
| Volvo Penta Marine Diesel Engines — Product Range Guide | Volvo Penta AB | 2025 | measured |
| Volvo Penta Operator's Manual D1 | Volvo Penta AB | 2024 | measured |
| Volvo Penta Operator's Manual D2 | Volvo Penta AB | 2024 | measured |
| Volvo Penta Workshop Manual D3 | Volvo Penta AB | 2023 | measured |
| Volvo Penta Workshop Manual D4/D6 | Volvo Penta AB | 2024 | measured |
| Volvo Penta IPS Installation Manual | Volvo Penta AB | 2024 | measured |
| Volvo Penta Saildrive Service Manual | Volvo Penta AB | 2023 | measured |
| Volvo Penta EVC System Description | Volvo Penta AB | 2024 | measured |
| Volvo Penta Service Bulletin Collection | Volvo Penta AB | 2019–2025 | documented |
| Volvo Penta Genuine Parts Catalog (EPC) | Volvo Penta AB | 2025 | measured |

### S.2 Sekundärquellen

| Quelle | Typ | Confidence |
|--------|-----|-----------|
| Nigel Calder: Marine Diesel Engines (5th Ed.) | Fachbuch | documented |
| Nigel Calder: Boatowner's Mechanical & Electrical Manual | Fachbuch | documented |
| Don Casey: Sailboat Maintenance Manual | Fachbuch | documented |
| Segeln-Forum.de (D-Motor-Threads) | Forum | estimated |
| Boote-Forum.de (VP-Erfahrungsberichte) | Forum | estimated |
| YBW.com (VP Owners Section) | Forum | estimated |
| Cruisers Forum (VP Engine Section) | Forum | estimated |
| Oelcheck GmbH — Motorölanalyse-Grenzwerte | Fachquelle | measured |
| TÜV Nord — Bootsmotorenprüfung | Normen | measured |

---

*Ende der Wissensdatei 18.03 — Volvo Penta Marine-Diesel*
*AYDI Maritime Knowledge Base v2.0 — Stand April 2026*
*Confidence: measured (Herstellerdaten), documented (Werkstattberichte), estimated (Preise/Lebensdauer)*
