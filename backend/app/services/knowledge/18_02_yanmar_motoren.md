---
titel: "Yanmar Marine-Diesel — Modellreihen und Spezifikationen"
kategorie: "Motoren und Antrieb"
unterkategorie: "Yanmar Motoren"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
status: "validated"
confidence_quellen:
  - measured: "Yanmar-Werksdatenblätter, ISO-Normen, CE-Zertifizierungen"
  - documented: "Yanmar-Werkstatthandbücher, Servicebulletins, Händler-Kataloge"
  - estimated: "Erfahrungswerte aus Werftbetrieben, Eignerfeedback, Branchenkonsens"
---

# 18_02 — Yanmar Marine-Diesel — Modellreihen und Spezifikationen

> **AYDI Wissensdatei 18.02** — Kategorie 18: Motoren und Antrieb
> **Confidence-Quelle:** measured (Yanmar-Werksdatenblätter, ISO-Normen), documented (Werkstatthandbücher, Servicebulletins), estimated (Werft-Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04

---

## Inhaltsverzeichnis

1. [Firmengeschichte und Marine-Sparte](#1-firmengeschichte-und-marine-sparte)
2. [Modellnomenklatur und Baureihen-Übersicht](#2-modellnomenklatur-und-baureihen-übersicht)
3. [GM-Serie (Ältere Baureihe)](#3-gm-serie-ältere-baureihe)
4. [YM-Serie (Kompaktmotoren)](#4-ym-serie-kompaktmotoren)
5. [JH-Serie (Mittelklasse-Segelboote)](#5-jh-serie-mittelklasse-segelboote)
6. [LHA-Serie (Leistungsstarke Marinediesel)](#6-lha-serie-leistungsstarke-marinediesel)
7. [LY/LPA-Serie (6-Zylinder-Hochleistung)](#7-lylpa-serie-6-zylinder-hochleistung)
8. [BY-Serie (V8-Großmotoren)](#8-by-serie-v8-großmotoren)
9. [Saildrive-Systeme](#9-saildrive-systeme)
10. [Getriebe-Optionen](#10-getriebe-optionen)
11. [Kühlsysteme](#11-kühlsysteme)
12. [Wartungsintervalle und Servicepläne](#12-wartungsintervalle-und-servicepläne)
13. [Ersatzteile und Teilenummern](#13-ersatzteile-und-teilenummern)
14. [Bekannte Schwachstellen je Modell](#14-bekannte-schwachstellen-je-modell)
15. [Motorlager und Befestigung](#15-motorlager-und-befestigung)
16. [Instrumentierung und Überwachung](#16-instrumentierung-und-überwachung)
17. [Fehlerbilder](#17-fehlerbilder)
18. [Troubleshooting-Bäume](#18-troubleshooting-bäume)
19. [Fallstudien](#19-fallstudien)
20. [FAQ — Häufig gestellte Fragen](#20-faq)
21. [Glossar](#21-glossar)
22. [Pydantic v2 Datenmodelle](#22-pydantic-v2-datenmodelle)
23. [Preisübersicht EUR](#23-preisübersicht-eur)
24. [Quellenverzeichnis](#24-quellenverzeichnis)

---

## 1. Firmengeschichte und Marine-Sparte

### 1.1 Unternehmensgeschichte

Yanmar Co., Ltd. wurde 1912 von Magokichi Yamaoka in Osaka, Japan gegründet. Der Name „Yanmar" leitet sich vom japanischen Wort „Yanma" (Königslibelle) ab, die in Japan als Symbol für Glück und Erntereichtum gilt.

**Meilensteine:**

| Jahr | Ereignis |
|------|----------|
| 1912 | Gründung als Yamaoka Hatsudoki Kosakusho (Motorenfabrik Yamaoka) |
| 1933 | Weltweit erster praxistauglicher Kleindieselmotor (5 PS, horizontaler Einzylinder) |
| 1952 | Erster Marine-Dieselmotor für Fischereifahrzeuge |
| 1961 | Beginn der Serienproduktion von Marine-Einbaudieseln |
| 1966 | Gründung der Yanmar Diesel Engine Co., Ltd. |
| 1972 | Eintritt in den europäischen Markt für Segelboot-Dieselmotoren |
| 1976 | Einführung der GM-Baureihe (1GM, 2GM, 3GM) |
| 1983 | Vorstellung des Saildrive SD20 |
| 1991 | JH-Serie ersetzt ältere QM-Modelle |
| 1998 | Einführung der 3JH-Baureihe mit Common-Rail-Vorbereitung |
| 2005 | YM-Serie als Nachfolger der GM-Serie |
| 2010 | 4JH-CR-Serie mit Common-Rail-Einspritzung |
| 2014 | 4LHA-Serie mit Turbolader und Ladeluftkühlung |
| 2017 | 3JH40 mit Tier-II-Abgasnorm |
| 2019 | 4JH45/57/80/110 — neue Generation der JH-Baureihe |
| 2022 | BY-Serie (V8) für Megayachten und schnelle Motoryachten |
| 2024 | Überarbeitete SD60 Saildrive mit verbesserter Dichtung |

### 1.2 Marine-Sparte heute

Yanmar ist weltweit einer der führenden Hersteller von Marine-Dieselmotoren im Leistungsbereich von 9 bis 900 PS. Die Marine-Sparte umfasst:

- **Einbau-Dieselmotoren** für Segelboote (9–110 PS)
- **Einbau-Dieselmotoren** für Motorboote (40–900 PS)
- **Saildrive-Aggregate** (SD20, SD25, SD50, SD60)
- **Wendegetriebe** (KM-Serie)
- **Instrumentierung** und Überwachungssysteme
- **Generatoren** (Marine-Gensets)
- **Joystick-Manövriersysteme** (JC-Serie)

**Produktionsstandorte Marine:**

| Standort | Produktion |
|----------|-----------|
| Amagasaki, Japan | GM-, YM-, JH-Serien, Saildrives |
| Biwa, Japan | LHA-, LY-Serien |
| Maibara, Japan | BY-Serie, Großdiesel |
| Almere, Niederlande | Europäische Distribution, Anpassung |

### 1.3 Marktposition im Yachtbau

Yanmar dominiert den europäischen Segelboot-Markt für Hilfsdiesel mit geschätztem Marktanteil von 55–65 % (2025). Hauptwettbewerber:

| Hersteller | Leistungsbereich | Marktanteil (geschätzt) |
|------------|-----------------|------------------------|
| **Yanmar** | 9–900 PS | 55–65 % (Segelboote), 25–35 % (Motorboote) |
| Volvo Penta | 10–1.000 PS | 25–30 % (Segelboote), 35–45 % (Motorboote) |
| Nanni Diesel | 10–250 PS | 5–8 % |
| Beta Marine | 14–150 PS | 3–5 % |
| Vetus | 16–315 PS | 2–4 % |
| Craftsman Marine | 35–230 PS | 1–3 % |

**OEM-Kunden (Segelbootwerften, die Yanmar ab Werk verbauen):**
- Bavaria Yachts (DE) — YM- und JH-Serie
- Hanse Group (DE) — JH-Serie
- Bénéteau/Jeanneau (FR) — YM- und JH-Serie
- Dufour (FR) — JH-Serie
- Hallberg-Rassy (SE) — JH-Serie
- Najad/Hallberg-Rassy (SE) — JH-Serie
- X-Yachts (DK) — JH-Serie
- Dehler (DE) — JH-Serie
- Contest Yachts (NL) — JH-Serie
- Oyster Yachts (UK) — 4JH/4LHA-Serie

### 1.4 CE-Konformität und Abgasnormen

Alle aktuellen Yanmar-Marine-Motoren erfüllen:

- **EU RCD 2013/53/EU** (Recreational Craft Directive) — Abgasemissionen
- **IMO Tier II** — NOx-Grenzwerte für Schiffsmotoren
- **EPA Tier 3** (für US-Markt)
- **BSO II** (Bodensee-Schifffahrtsordnung) — Spezielle Abgasgrenzwerte für Binnenseen

---

## 2. Modellnomenklatur und Baureihen-Übersicht

### 2.1 Yanmar-Bezeichnungssystem

Die Yanmar-Modellbezeichnung folgt einem strukturierten Schema:

```
[Zylinderanzahl][Baureihe][Hubraum/Leistungsklasse] [-Variante]

Beispiele:
  3 JH 40       → 3 Zylinder, JH-Serie, 40 PS
  4 LHA -STP    → 4 Zylinder, LHA-Serie, STP-Variante (240 PS)
  1 YM 15       → 1 Zylinder, YM-Serie, 15 PS-Klasse
  2 GM 20       → 2 Zylinder, GM-Serie, 20 PS-Klasse
```

**Baureihen-Codes:**

| Code | Bedeutung | Leistungsbereich | Einsatz |
|------|-----------|-----------------|---------|
| GM | General Marine (ältere Serie) | 9–27 PS | Segelboote bis 10 m |
| YM | Yacht Motor (Nachfolger GM) | 14,7–29 PS | Segelboote bis 12 m |
| JH | Jacht-Hochleistung | 39–110 PS | Segelboote 10–20 m, Motorboote bis 12 m |
| LHA | Leistungs-Hochdruck-Aufladung | 240–315 PS | Motorboote 10–18 m |
| LY | Leistung-Yacht | 350–440 PS | Motorboote 12–22 m |
| LPA | Leistung-Performance-Aufladung | 315–380 PS | Schnelle Motorboote |
| BY | Big Yacht (V8) | 480–900 PS | Megayachten, schnelle Kreuzer |

**Varianten-Suffixe:**

| Suffix | Bedeutung |
|--------|-----------|
| -STP | Standard Turbo Performance |
| -DTP | Direct Turbo Performance (höhere Leistung) |
| -HTP | High Turbo Performance |
| -STE | Standard Turbo Economy |
| -CR | Common Rail |
| (C) | Sail-Drive-tauglich (SD-kompatibel) |
| (F) | Festpropeller-Version |

### 2.2 Gesamtübersicht aller aktuellen Modelle

| Modell | Zylinder | Hubraum (L) | Leistung (PS/kW) | Drehzahl (U/min) | Gewicht (kg) | Einsatz |
|--------|---------|------------|-------------------|-------------------|-------------|---------|
| 1GM10 | 1 | 0,331 | 9/6,6 | 3.400 | 42 | Jollenkreuzer, Daysailer |
| 2GM20 | 2 | 0,662 | 18/13,2 | 3.400 | 68 | Segelboote 6–8 m |
| 3GM30 | 3 | 0,993 | 27/19,9 | 3.400 | 90 | Segelboote 8–10 m |
| 1YM15 | 1 | 0,331 | 14,7/10,8 | 3.600 | 49 | Segelboote bis 8 m |
| 2YM15 | 2 | 0,570 | 14,7/10,8 | 3.000 | 68 | Segelboote 7–9 m |
| 2YM20 | 2 | 0,570 | 21/15,4 | 3.400 | 72 | Segelboote 8–10 m |
| 3YM20 | 3 | 0,854 | 21/15,4 | 2.900 | 88 | Segelboote 9–11 m |
| 3YM30 | 3 | 0,854 | 29/21,3 | 3.400 | 92 | Segelboote 10–12 m |
| 3JH40 | 3 | 1,496 | 39/29 | 3.000 | 175 | Segelboote 10–13 m |
| 4JH45 | 4 | 1,995 | 45/33 | 2.800 | 215 | Segelboote 12–14 m |
| 4JH57 | 4 | 1,995 | 57/41,9 | 3.000 | 225 | Segelboote 13–16 m |
| 4JH80 | 4 | 1,995 | 80/58,8 | 3.200 | 240 | Segelboote 14–18 m |
| 4JH110 | 4 | 2,189 | 110/80,9 | 3.300 | 265 | Segelboote 16–22 m |
| 4LHA-STP | 4 | 3,318 | 240/176 | 3.300 | 380 | Motorboote 10–14 m |
| 4LHA-DTP | 4 | 3,318 | 315/232 | 3.600 | 395 | Motorboote 12–16 m |
| 6LY-STP | 6 | 5,813 | 380/280 | 3.300 | 545 | Motorboote 14–20 m |
| 6LY-UTP | 6 | 5,813 | 440/324 | 3.300 | 560 | Motorboote 16–22 m |
| 6LPA-STP2 | 6 | 5,813 | 315/232 | 3.000 | 530 | Verdränger, Trawler |
| 8BY-220Z | 8 (V) | 5,954 | 480/353 | 3.800 | 520 | Schnelle Motorboote |
| 8BY-260Z | 8 (V) | 5,954 | 530/390 | 4.000 | 530 | Schnelle Motorboote |

---

## 3. GM-Serie (Ältere Baureihe)

### 3.1 Übersicht und historische Bedeutung

Die GM-Serie (General Marine) war über drei Jahrzehnte (ca. 1976–2008) die meistverkaufte Marine-Dieselmotorenreihe weltweit im kleinen Leistungsbereich. Schätzungsweise über 300.000 Einheiten wurden produziert. Viele dieser Motoren sind heute noch in Betrieb und werden durch die YM-Serie ersetzt, jedoch ist die Ersatzteilversorgung weiterhin gewährleistet.

### 3.2 1GM10 — Einzylinder 9 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, Einzylinder, Saugmotor |
| Hubraum | 331 cm³ |
| Bohrung × Hub | 75 × 75 mm |
| Leistung | 9 PS (6,6 kW) bei 3.400 U/min |
| Max. Drehmoment | 2,0 kgm bei 2.200 U/min |
| Verdichtungsverhältnis | 21:1 |
| Einspritzung | Indirekt, Vorkammer |
| Kühlsystem | Seewassergekühlt (direkt) |
| Startanlage | Elektrisch 12V |
| Lichtmaschine | 12V / 35A |
| Kraftstoffverbrauch | 2,3 L/h bei Volllast |
| Spez. Verbrauch | 260 g/kWh |
| Ölmenge (Wanne) | 1,4 L |
| Ölfiltertyp | Yanmar 119305-35151 |
| Gewicht (trocken) | 42 kg |
| Abmessungen (L×B×H) | 508 × 356 × 498 mm |
| Propellerdrehzahl | 2.700 U/min (mit 1:1,26 Untersetzung) |

**Getriebeoptionen:**
- Yanmar KM2A: 1:1,26 Untersetzung, mechanisch, vorwärts/rückwärts
- Yanmar KM2C: 1:1,38 Untersetzung, mechanisch
- Saildrive SD20 (Option)

**Einsatzbereich:**
- Segelboote 5–8 m (Jollenkreuzer, Daysailer)
- Verdrängergeschwindigkeit: 4–5,5 kn bei Rumpfgeschwindigkeit
- Typischer Propeller: 2-Blatt Faltpropeller 11–13" Durchmesser

**Preise (EUR, UVP 2025):**
- 1GM10 Motor solo: ca. 4.200–4.800 EUR
- 1GM10 mit KM2A-Getriebe: ca. 5.100–5.600 EUR
- 1GM10 mit SD20 Saildrive: ca. 6.800–7.400 EUR

### 3.3 2GM20 — Zweizylinder 18 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 2 Zylinder in Reihe, Saugmotor |
| Hubraum | 662 cm³ |
| Bohrung × Hub | 75 × 75 mm |
| Leistung | 18 PS (13,2 kW) bei 3.400 U/min |
| Max. Drehmoment | 3,9 kgm bei 2.400 U/min |
| Verdichtungsverhältnis | 21:1 |
| Einspritzung | Indirekt, Vorkammer |
| Kühlsystem | Süßwasser mit Seewasser-Wärmetauscher |
| Startanlage | Elektrisch 12V |
| Lichtmaschine | 12V / 55A |
| Kraftstoffverbrauch | 4,2 L/h bei Volllast |
| Spez. Verbrauch | 255 g/kWh |
| Ölmenge (Wanne) | 2,0 L |
| Ölfiltertyp | Yanmar 119305-35151 |
| Gewicht (trocken) | 68 kg |
| Abmessungen (L×B×H) | 568 × 406 × 540 mm |

**Getriebeoptionen:**
- Yanmar KM2P: 1:1,97 Untersetzung, mechanisch
- Yanmar KM2P-1: 1:2,21 Untersetzung
- Saildrive SD20 (Standardkonfiguration für Segelboote)

**Einsatzbereich:**
- Segelboote 7–10 m
- Typischer Propeller: 2-Blatt Faltpropeller 13–15" Durchmesser
- Verdrängergeschwindigkeit: 5–6,5 kn

**Preise (EUR, UVP 2025):**
- 2GM20 Motor solo: ca. 6.200–6.800 EUR
- 2GM20 mit KM2P-Getriebe: ca. 7.400–8.100 EUR
- 2GM20 mit SD20 Saildrive: ca. 8.900–9.600 EUR

### 3.4 3GM30 — Dreizylinder 27 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 3 Zylinder in Reihe, Saugmotor |
| Hubraum | 993 cm³ |
| Bohrung × Hub | 75 × 75 mm |
| Leistung | 27 PS (19,9 kW) bei 3.400 U/min |
| Max. Drehmoment | 5,8 kgm bei 2.400 U/min |
| Verdichtungsverhältnis | 21:1 |
| Einspritzung | Indirekt, Vorkammer |
| Kühlsystem | Süßwasser mit Seewasser-Wärmetauscher |
| Startanlage | Elektrisch 12V |
| Lichtmaschine | 12V / 55A |
| Kraftstoffverbrauch | 6,3 L/h bei Volllast |
| Spez. Verbrauch | 253 g/kWh |
| Ölmenge (Wanne) | 2,6 L |
| Ölfiltertyp | Yanmar 119305-35151 |
| Gewicht (trocken) | 90 kg |
| Abmessungen (L×B×H) | 628 × 406 × 555 mm |

**Getriebeoptionen:**
- Yanmar KM3A: 1:2,21 Untersetzung, mechanisch
- Yanmar KM3A-1: 1:2,62 Untersetzung
- Saildrive SD20 (beliebteste Konfiguration)

**Einsatzbereich:**
- Segelboote 8–11 m
- Typischer Propeller: 2- oder 3-Blatt Faltpropeller 14–16" Durchmesser
- Verdrängergeschwindigkeit: 5,5–7 kn

**Preise (EUR, UVP 2025):**
- 3GM30 Motor solo: ca. 7.800–8.500 EUR
- 3GM30 mit KM3A-Getriebe: ca. 9.200–10.000 EUR
- 3GM30 mit SD20 Saildrive: ca. 10.800–11.600 EUR

### 3.5 GM-Serie — Gemeinsame Merkmale und Schwachstellen

**Konstruktionsmerkmale:**
- Grauguss-Motorblock, hohe Robustheit
- Einfache mechanische Einspritzpumpe (keine Elektronik)
- Leicht zugängliche Wartungspunkte
- Bewährt zuverlässig bei regelmäßiger Wartung
- Geringe Vibrationen durch ausgewuchtete Kurbelwelle

**Bekannte Schwachstellen GM-Serie:**

| Schwachstelle | Betroffene Modelle | Symptom | Lösung |
|---------------|-------------------|---------|--------|
| Seewasserpumpen-Impeller | Alle GM | Überhitzung, reduzierter Kühlwasserdurchfluss | Impeller 128170-02070 jährlich tauschen |
| Vorkammer-Dichtung | Alle GM | Weißer Rauch, Leistungsverlust | Vorkammer 124610-11940 erneuern |
| Motorlager-Ermüdung | Alle GM >2.000h | Vibrationen, Geräusche | Lager 128170-08340 erneuern |
| Einspritzleitung korrodiert | Alle GM >15 Jahre | Dieselaustritt, Brandgefahr | Leitungen 104200-59111 erneuern |
| Auspuffkrümmer Rissbildung | 2GM20, 3GM30 | Abgase im Motorraum, Überhitzung | Krümmer 128370-13551 erneuern |
| Stopfbuchse undicht | Alle GM mit Welle | Wassereinbruch Bilge | PSS-Dichtung nachrüsten |
| Lichtmaschinen-Regler | Alle GM | Unregelmäßige Ladung, Batterie leer | Regler oder komplette LiMa tauschen |

---

## 4. YM-Serie (Kompaktmotoren)

### 4.1 Übersicht

Die YM-Serie wurde 2005 als Nachfolger der GM-Serie eingeführt und bietet bei gleichem oder geringerem Gewicht verbesserte Leistung, niedrigere Emissionen und leiseren Betrieb. Die Motoren erfüllen die RCD 2013/53/EU Abgasanforderungen.

**Gemeinsame Merkmale YM-Serie:**
- Indirekte Einspritzung (IDI) mit optimierter Vorkammer
- Süßwasserkühlung mit Seewasser-Wärmetauscher (ab 2YM)
- Elastische Motorlagerung ab Werk
- Integrierte Auspuffmischkammer (Wassergekühlter Auspuff)
- Saildrive-kompatibel (SD20/SD25)
- 12V-Elektrik, Lichtmaschine 80A (aufgerüstet)
- Motormanagement ohne Elektronik (rein mechanisch)

### 4.2 1YM15 — Einzylinder 14,7 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, Einzylinder, Saugmotor |
| Hubraum | 331 cm³ |
| Bohrung × Hub | 75 × 75 mm |
| Leistung | 14,7 PS (10,8 kW) bei 3.600 U/min |
| Max. Drehmoment | 2,5 kgm bei 2.500 U/min |
| Verdichtungsverhältnis | 21:1 |
| Einspritzung | Indirekt, Vorkammer, mechanische Pumpe |
| Kühlsystem | Seewassergekühlt (direkt) |
| Startanlage | Elektrisch 12V |
| Lichtmaschine | 12V / 80A |
| Kraftstoffverbrauch | 3,1 L/h bei Volllast |
| Spez. Verbrauch | 248 g/kWh |
| Ölmenge (Wanne) | 1,5 L |
| Ölfiltertyp | Yanmar 119305-35170 |
| Kraftstofffilter | Yanmar 104500-55710 |
| Luftfilter | Yanmar 128171-12540 |
| Gewicht (trocken) | 49 kg |
| Abmessungen (L×B×H) | 516 × 364 × 509 mm |

**Getriebeoptionen:**
- Yanmar KM2C-1: 1:1,36 Untersetzung
- Yanmar KM2C-2: 1:1,61 Untersetzung
- Saildrive SD20

**Einsatzbereich:**
- Segelboote 6–8 m
- Leistungsreserve gegenüber 1GM10 (+63 %)
- Typischer Propeller: 2-Blatt Faltpropeller 12–14" Durchmesser

**Preise (EUR, UVP 2025/26):**
- 1YM15 Motor solo: ca. 5.800–6.400 EUR
- 1YM15 mit KM2C-Getriebe: ca. 6.900–7.500 EUR
- 1YM15 mit SD20 Saildrive: ca. 8.200–8.900 EUR

### 4.3 2YM15 — Zweizylinder 14,7 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 2 Zylinder in Reihe, Saugmotor |
| Hubraum | 570 cm³ |
| Bohrung × Hub | 70 × 74 mm |
| Leistung | 14,7 PS (10,8 kW) bei 3.000 U/min |
| Max. Drehmoment | 3,2 kgm bei 2.200 U/min |
| Verdichtungsverhältnis | 22,5:1 |
| Einspritzung | Indirekt, Vorkammer |
| Kühlsystem | Süßwasser mit Seewasser-Wärmetauscher |
| Startanlage | Elektrisch 12V |
| Lichtmaschine | 12V / 80A |
| Kraftstoffverbrauch | 3,0 L/h bei Volllast |
| Spez. Verbrauch | 240 g/kWh |
| Ölmenge (Wanne) | 2,2 L |
| Ölfiltertyp | Yanmar 119305-35170 |
| Kraftstofffilter | Yanmar 104500-55710 |
| Luftfilter | Yanmar 128171-12540 |
| Gewicht (trocken) | 68 kg |
| Abmessungen (L×B×H) | 576 × 398 × 535 mm |

**Besonderheiten:**
- Gleiche Leistung wie 1YM15, aber bei niedrigerer Drehzahl → ruhigerer Lauf
- Zwei Zylinder verteilen Vibrationen besser
- Bevorzugt für Eigneryachten, bei denen Komfort wichtiger als Gewicht ist

**Getriebeoptionen:**
- Yanmar KM2P-1: 1:2,04 Untersetzung
- Yanmar KM2P-2: 1:2,36 Untersetzung
- Saildrive SD20

**Einsatzbereich:**
- Segelboote 7–9 m
- Besonders geeignet für Langfahrt (niedrige Drehzahl = weniger Verschleiß)

**Preise (EUR, UVP 2025/26):**
- 2YM15 Motor solo: ca. 7.200–7.800 EUR
- 2YM15 mit KM2P-Getriebe: ca. 8.500–9.200 EUR
- 2YM15 mit SD20 Saildrive: ca. 9.800–10.600 EUR

### 4.4 2YM20 — Zweizylinder 21 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 2 Zylinder in Reihe, Saugmotor |
| Hubraum | 570 cm³ |
| Bohrung × Hub | 70 × 74 mm |
| Leistung | 21 PS (15,4 kW) bei 3.400 U/min |
| Max. Drehmoment | 3,8 kgm bei 2.600 U/min |
| Verdichtungsverhältnis | 22,5:1 |
| Einspritzung | Indirekt, Vorkammer |
| Kühlsystem | Süßwasser mit Seewasser-Wärmetauscher |
| Startanlage | Elektrisch 12V |
| Lichtmaschine | 12V / 80A |
| Kraftstoffverbrauch | 4,5 L/h bei Volllast |
| Spez. Verbrauch | 245 g/kWh |
| Ölmenge (Wanne) | 2,2 L |
| Ölfiltertyp | Yanmar 119305-35170 |
| Kraftstofffilter | Yanmar 104500-55710 |
| Luftfilter | Yanmar 128171-12540 |
| Gewicht (trocken) | 72 kg |
| Abmessungen (L×B×H) | 576 × 398 × 535 mm |

**Getriebeoptionen:**
- Yanmar KM2P-1: 1:2,04 Untersetzung
- Yanmar KM2P-2: 1:2,36 Untersetzung
- Saildrive SD20

**Einsatzbereich:**
- Segelboote 8–10 m
- Meistverkaufte YM-Variante

**Preise (EUR, UVP 2025/26):**
- 2YM20 Motor solo: ca. 7.800–8.400 EUR
- 2YM20 mit KM2P-Getriebe: ca. 9.200–9.900 EUR
- 2YM20 mit SD20 Saildrive: ca. 10.500–11.300 EUR

### 4.5 3YM20 — Dreizylinder 21 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 3 Zylinder in Reihe, Saugmotor |
| Hubraum | 854 cm³ |
| Bohrung × Hub | 70 × 74 mm |
| Leistung | 21 PS (15,4 kW) bei 2.900 U/min |
| Max. Drehmoment | 5,1 kgm bei 2.000 U/min |
| Verdichtungsverhältnis | 22,5:1 |
| Einspritzung | Indirekt, Vorkammer |
| Kühlsystem | Süßwasser mit Seewasser-Wärmetauscher |
| Startanlage | Elektrisch 12V |
| Lichtmaschine | 12V / 80A |
| Kraftstoffverbrauch | 4,3 L/h bei Volllast |
| Spez. Verbrauch | 238 g/kWh |
| Ölmenge (Wanne) | 3,0 L |
| Ölfiltertyp | Yanmar 119305-35170 |
| Kraftstofffilter | Yanmar 104500-55710 |
| Luftfilter | Yanmar 128171-12560 |
| Gewicht (trocken) | 88 kg |
| Abmessungen (L×B×H) | 650 × 420 × 555 mm |

**Besonderheiten:**
- Gleiche Leistung wie 2YM20, aber bei nur 2.900 U/min → extrem ruhig
- Drei Zylinder ergeben nahezu vibrationsfreien Lauf
- Für Langfahrer, die maximalen Komfort bei ausreichender Leistung wünschen
- Größerer Hubraum = mehr Drehmoment bei niedrigen Drehzahlen

**Getriebeoptionen:**
- Yanmar KM3A: 1:2,21 Untersetzung
- Yanmar KM3A-1: 1:2,62 Untersetzung
- Saildrive SD20

**Preise (EUR, UVP 2025/26):**
- 3YM20 Motor solo: ca. 9.400–10.100 EUR
- 3YM20 mit KM3A-Getriebe: ca. 11.000–11.800 EUR
- 3YM20 mit SD20 Saildrive: ca. 12.400–13.200 EUR

### 4.6 3YM30 — Dreizylinder 29 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 3 Zylinder in Reihe, Saugmotor |
| Hubraum | 854 cm³ |
| Bohrung × Hub | 70 × 74 mm |
| Leistung | 29 PS (21,3 kW) bei 3.400 U/min |
| Max. Drehmoment | 5,6 kgm bei 2.600 U/min |
| Verdichtungsverhältnis | 22,5:1 |
| Einspritzung | Indirekt, Vorkammer |
| Kühlsystem | Süßwasser mit Seewasser-Wärmetauscher |
| Startanlage | Elektrisch 12V |
| Lichtmaschine | 12V / 80A |
| Kraftstoffverbrauch | 6,0 L/h bei Volllast |
| Spez. Verbrauch | 242 g/kWh |
| Ölmenge (Wanne) | 3,0 L |
| Ölfiltertyp | Yanmar 119305-35170 |
| Kraftstofffilter | Yanmar 104500-55710 |
| Luftfilter | Yanmar 128171-12560 |
| Gewicht (trocken) | 92 kg |
| Abmessungen (L×B×H) | 650 × 420 × 555 mm |

**Getriebeoptionen:**
- Yanmar KM3A: 1:2,21 Untersetzung
- Yanmar KM3A-1: 1:2,62 Untersetzung
- Saildrive SD25

**Einsatzbereich:**
- Segelboote 10–12 m
- Typischer Einsatz: Bavaria 34, Hanse 345, Jeanneau Sun Odyssey 349

**Preise (EUR, UVP 2025/26):**
- 3YM30 Motor solo: ca. 10.200–10.900 EUR
- 3YM30 mit KM3A-Getriebe: ca. 11.800–12.600 EUR
- 3YM30 mit SD25 Saildrive: ca. 13.500–14.400 EUR

### 4.7 YM-Serie — Gemeinsame Schwachstellen

| Schwachstelle | Betroffene Modelle | Symptom | Lösung |
|---------------|-------------------|---------|--------|
| Seewasserpumpen-Wellendichtung | Alle YM | Tropfen am Pumpengehäuse | Dichtung 119773-42600 erneuern |
| Thermostat klemmt (offen) | 2YM, 3YM | Motor wird nicht warm, hoher Verbrauch | Thermostat 119773-49550 tauschen |
| Kraftstoff-Förderpumpe schwach | Alle YM >3.000h | Schlechtes Startverhalten, Luftblasen | Förderpumpe 119773-52020 erneuern |
| Keilriemen-Fluchtungsfehler | 1YM15 | Quietschen, Riemenverschleiß | Riemenscheibe 119773-35130 prüfen/richten |
| Auspuffmischkammer Korrosion | Alle YM >10 Jahre | Wasseraustritt, Rost | Mischkammer erneuern (materialabhängig) |

---

## 5. JH-Serie (Mittelklasse-Segelboote)

### 5.1 Übersicht

Die JH-Serie ist Yanmars Kernprodukt für mittlere bis große Segelboote und kleine Motorboote. Seit der Einführung der ersten JH-Motoren in den 1990er Jahren hat sich die Baureihe kontinuierlich weiterentwickelt. Die aktuelle Generation (ab 2019) bietet Common-Rail-Einspritzung, elektronische Steuerung und erfüllt IMO Tier II.

**Gemeinsame Merkmale JH-Serie (aktuelle Generation):**
- Common-Rail-Einspritzung mit elektronischer Steuerung
- Süßwasserkühlung mit optimiertem Wärmetauscher
- Gummielastische Motorlagerung ab Werk
- CAN-Bus-kompatible Instrumentierung
- Integrierte Auspuffmischkammer
- Wartungsfreundliches Design mit Top-Access
- Saildrive-kompatibel (SD50, SD60)
- 12V-Elektrik, Lichtmaschine 125A standard

### 5.2 3JH40 — Dreizylinder 39 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 3 Zylinder in Reihe, Common Rail |
| Hubraum | 1.496 cm³ |
| Bohrung × Hub | 84 × 90 mm |
| Leistung | 39 PS (29 kW) bei 3.000 U/min |
| Max. Drehmoment | 8,9 kgm bei 2.200 U/min |
| Verdichtungsverhältnis | 19,5:1 |
| Einspritzung | Common Rail, elektronisch gesteuert |
| Einspritzdruck | bis 1.600 bar |
| Kühlsystem | Süßwasser mit Seewasser-Wärmetauscher |
| Thermostatöffnung | 71 °C |
| Startanlage | Elektrisch 12V, 2,0 kW Anlasser |
| Lichtmaschine | 12V / 125A |
| Kraftstoffverbrauch | 7,5 L/h bei Volllast |
| Kraftstoffverbrauch Reisefahrt | 4,8 L/h bei 2.400 U/min (ca. 70 %) |
| Spez. Verbrauch | 225 g/kWh |
| Ölmenge (Wanne) | 4,5 L |
| Ölfiltertyp | Yanmar 129150-35170 |
| Kraftstofffilter (primär) | Yanmar 129004-55810 |
| Kraftstofffilter (sekundär) | Yanmar 129A00-55800 |
| Luftfilter | Yanmar 129195-12530 |
| Gewicht (trocken) | 175 kg |
| Abmessungen (L×B×H) | 723 × 499 × 617 mm |

**Getriebeoptionen:**
- Yanmar KMH4A: 1:2,04 / 1:2,36 / 1:2,62 Untersetzung
- Yanmar KMH4A2: 1:2,81 / 1:3,05 Untersetzung
- Saildrive SD50 (Standard für Segelboote)
- Saildrive SD60 (verstärkte Variante)

**Einsatzbereich:**
- Segelboote 10–13 m (z. B. Bavaria Cruiser 37, Hanse 388, Jeanneau SO 380)
- Motorboote bis 9 m (Verdränger)
- Typischer Propeller: 3-Blatt Faltpropeller 15–17" Durchmesser

**Preise (EUR, UVP 2025/26):**
- 3JH40 Motor solo: ca. 14.500–15.800 EUR
- 3JH40 mit KMH4A-Getriebe: ca. 17.200–18.600 EUR
- 3JH40 mit SD50 Saildrive: ca. 19.800–21.400 EUR
- 3JH40 mit SD60 Saildrive: ca. 21.500–23.200 EUR

### 5.3 4JH45 — Vierzylinder 45 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 4 Zylinder in Reihe, Common Rail |
| Hubraum | 1.995 cm³ |
| Bohrung × Hub | 84 × 90 mm |
| Leistung | 45 PS (33 kW) bei 2.800 U/min |
| Max. Drehmoment | 11,8 kgm bei 2.000 U/min |
| Verdichtungsverhältnis | 19,5:1 |
| Einspritzung | Common Rail, elektronisch gesteuert |
| Einspritzdruck | bis 1.600 bar |
| Kühlsystem | Süßwasser mit Seewasser-Wärmetauscher |
| Thermostatöffnung | 71 °C |
| Startanlage | Elektrisch 12V, 2,3 kW Anlasser |
| Lichtmaschine | 12V / 125A |
| Kraftstoffverbrauch | 9,8 L/h bei Volllast |
| Kraftstoffverbrauch Reisefahrt | 6,2 L/h bei 2.200 U/min |
| Spez. Verbrauch | 222 g/kWh |
| Ölmenge (Wanne) | 5,8 L |
| Ölfiltertyp | Yanmar 129150-35170 |
| Kraftstofffilter (primär) | Yanmar 129004-55810 |
| Kraftstofffilter (sekundär) | Yanmar 129A00-55800 |
| Luftfilter | Yanmar 129195-12530 |
| Gewicht (trocken) | 215 kg |
| Abmessungen (L×B×H) | 802 × 548 × 648 mm |

**Getriebeoptionen:**
- Yanmar KMH4A: 1:2,04 / 1:2,36 / 1:2,62 Untersetzung
- Yanmar KMH4A2: 1:2,81 / 1:3,05 Untersetzung
- Saildrive SD50 (Standard)
- Saildrive SD60

**Einsatzbereich:**
- Segelboote 12–14 m (z. B. Bavaria Cruiser 40, Hanse 418, Dufour 412)
- Optimiert für niedrige Drehzahlen und langen Dauerbetrieb

**Preise (EUR, UVP 2025/26):**
- 4JH45 Motor solo: ca. 17.800–19.200 EUR
- 4JH45 mit KMH4A-Getriebe: ca. 20.500–22.100 EUR
- 4JH45 mit SD50 Saildrive: ca. 23.200–25.000 EUR
- 4JH45 mit SD60 Saildrive: ca. 25.000–27.000 EUR

### 5.4 4JH57 — Vierzylinder 57 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 4 Zylinder in Reihe, Common Rail |
| Hubraum | 1.995 cm³ |
| Bohrung × Hub | 84 × 90 mm |
| Leistung | 57 PS (41,9 kW) bei 3.000 U/min |
| Max. Drehmoment | 13,2 kgm bei 2.200 U/min |
| Verdichtungsverhältnis | 19,5:1 |
| Einspritzung | Common Rail, elektronisch gesteuert |
| Einspritzdruck | bis 1.800 bar |
| Kühlsystem | Süßwasser mit Seewasser-Wärmetauscher |
| Thermostatöffnung | 71 °C |
| Startanlage | Elektrisch 12V, 2,3 kW Anlasser |
| Lichtmaschine | 12V / 125A |
| Kraftstoffverbrauch | 12,0 L/h bei Volllast |
| Kraftstoffverbrauch Reisefahrt | 7,6 L/h bei 2.400 U/min |
| Spez. Verbrauch | 220 g/kWh |
| Ölmenge (Wanne) | 5,8 L |
| Ölfiltertyp | Yanmar 129150-35170 |
| Kraftstofffilter (primär) | Yanmar 129004-55810 |
| Kraftstofffilter (sekundär) | Yanmar 129A00-55800 |
| Luftfilter | Yanmar 129195-12530 |
| Gewicht (trocken) | 225 kg |
| Abmessungen (L×B×H) | 815 × 548 × 660 mm |

**Getriebeoptionen:**
- Yanmar KMH4A: 1:2,36 / 1:2,62 Untersetzung
- Yanmar KMH4A2: 1:2,81 / 1:3,05 / 1:3,42 Untersetzung
- Saildrive SD50
- Saildrive SD60 (empfohlen ab 4JH57)

**Einsatzbereich:**
- Segelboote 13–16 m (z. B. Hallberg-Rassy 44, X-Yacht X4.6, Contest 42CS)
- Motorboote bis 11 m (Verdränger)

**Preise (EUR, UVP 2025/26):**
- 4JH57 Motor solo: ca. 20.200–21.800 EUR
- 4JH57 mit KMH4A-Getriebe: ca. 23.500–25.200 EUR
- 4JH57 mit SD60 Saildrive: ca. 27.500–29.500 EUR

### 5.5 4JH80 — Vierzylinder 80 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 4 Zylinder in Reihe, Common Rail, Turbo |
| Hubraum | 1.995 cm³ |
| Bohrung × Hub | 84 × 90 mm |
| Leistung | 80 PS (58,8 kW) bei 3.200 U/min |
| Max. Drehmoment | 17,5 kgm bei 2.200 U/min |
| Verdichtungsverhältnis | 17,8:1 |
| Aufladung | Abgasturbolader, Ladeluftkühlung |
| Einspritzung | Common Rail, elektronisch gesteuert |
| Einspritzdruck | bis 1.800 bar |
| Kühlsystem | Süßwasser mit Seewasser-Wärmetauscher |
| Thermostatöffnung | 76 °C |
| Startanlage | Elektrisch 12V, 2,3 kW Anlasser |
| Lichtmaschine | 12V / 125A |
| Kraftstoffverbrauch | 16,5 L/h bei Volllast |
| Kraftstoffverbrauch Reisefahrt | 10,2 L/h bei 2.500 U/min |
| Spez. Verbrauch | 215 g/kWh |
| Ölmenge (Wanne) | 6,2 L |
| Ölfiltertyp | Yanmar 129150-35170 |
| Kraftstofffilter (primär) | Yanmar 129004-55810 |
| Kraftstofffilter (sekundär) | Yanmar 129A00-55800 |
| Luftfilter | Yanmar 129470-12530 |
| Gewicht (trocken) | 240 kg |
| Abmessungen (L×B×H) | 838 × 560 × 695 mm |

**Getriebeoptionen:**
- Yanmar KMH4A2: 1:2,62 / 1:2,81 / 1:3,05 / 1:3,42 Untersetzung
- Yanmar KMH61A: 1:2,91 / 1:3,23 Untersetzung (Hochleistungsgetriebe)
- Saildrive SD60

**Einsatzbereich:**
- Segelboote 14–18 m (z. B. Hallberg-Rassy 50, Oyster 495, Contest 50CS)
- Motorboote 9–13 m (Verdränger)

**Preise (EUR, UVP 2025/26):**
- 4JH80 Motor solo: ca. 24.500–26.200 EUR
- 4JH80 mit KMH4A2-Getriebe: ca. 28.200–30.400 EUR
- 4JH80 mit SD60 Saildrive: ca. 32.500–35.000 EUR

### 5.6 4JH110 — Vierzylinder 110 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 4 Zylinder in Reihe, Common Rail, Turbo |
| Hubraum | 2.189 cm³ |
| Bohrung × Hub | 87 × 92 mm |
| Leistung | 110 PS (80,9 kW) bei 3.300 U/min |
| Max. Drehmoment | 22,4 kgm bei 2.400 U/min |
| Verdichtungsverhältnis | 17,5:1 |
| Aufladung | Abgasturbolader, Ladeluftkühlung, Wastegate |
| Einspritzung | Common Rail, elektronisch gesteuert |
| Einspritzdruck | bis 2.000 bar |
| Kühlsystem | Süßwasser mit Seewasser-Wärmetauscher, ölgekühlter Turbo |
| Thermostatöffnung | 76 °C |
| Startanlage | Elektrisch 12V, 2,5 kW Anlasser |
| Lichtmaschine | 12V / 150A |
| Kraftstoffverbrauch | 22,0 L/h bei Volllast |
| Kraftstoffverbrauch Reisefahrt | 13,5 L/h bei 2.600 U/min |
| Spez. Verbrauch | 212 g/kWh |
| Ölmenge (Wanne) | 7,2 L |
| Ölfiltertyp | Yanmar 129150-35170 |
| Kraftstofffilter (primär) | Yanmar 129004-55810 |
| Kraftstofffilter (sekundär) | Yanmar 129A00-55800 |
| Luftfilter | Yanmar 129470-12530 |
| Gewicht (trocken) | 265 kg |
| Abmessungen (L×B×H) | 880 × 575 × 720 mm |

**Getriebeoptionen:**
- Yanmar KMH61A: 1:2,91 / 1:3,23 Untersetzung
- Yanmar KMH61A2: 1:3,48 / 1:3,88 Untersetzung
- Saildrive SD60

**Einsatzbereich:**
- Segelboote 16–22 m (z. B. Oyster 565, Hallberg-Rassy 57, Swan 54)
- Motorboote 10–15 m (Verdränger)
- Stärkster Motor der JH-Serie, grenzwertig für Saildrive-Betrieb

**Preise (EUR, UVP 2025/26):**
- 4JH110 Motor solo: ca. 29.800–32.000 EUR
- 4JH110 mit KMH61A-Getriebe: ca. 34.500–37.200 EUR
- 4JH110 mit SD60 Saildrive: ca. 38.500–41.500 EUR

### 5.7 JH-Serie — Gemeinsame Schwachstellen

| Schwachstelle | Betroffene Modelle | Symptom | Lösung |
|---------------|-------------------|---------|--------|
| Common-Rail-Injektor Verkokung | Alle JH (CR) >4.000h | Leistungsverlust, unrunder Lauf | Injektoren reinigen oder tauschen (129A00-53001) |
| ECU-Feuchtigkeitsempfindlichkeit | Alle JH (CR) | Startprobleme bei hoher Luftfeuchtigkeit | ECU-Gehäuse abdichten, Silicagel |
| Turbolader-Ölundichtigkeit | 4JH80, 4JH110 | Blauer Rauch, Ölverbrauch erhöht | Turbo-Dichtungssatz erneuern |
| Ladeluftkühler Korrosion | 4JH80, 4JH110 | Leistungsverlust, weißer Rauch | Ladeluftkühler erneuern |
| Wärmetauscher Zinkanode | Alle JH | Innenkorrosion, Kühlmittelverlust | Zinkanode 119574-44150 alle 250h prüfen |
| Kraftstoff-Hochdruckpumpe | Alle JH (CR) >6.000h | Druckverlust, Startprobleme | Hochdruckpumpe 129A00-51100 erneuern |
| Kabelbaum Vibrations-Bruch | 4JH45, 4JH57 (Saildrive) | Sporadische Ausfälle, Fehlercodes | Kabelbaum prüfen, Fixierung verbessern |

---

## 6. LHA-Serie (Leistungsstarke Marinediesel)

### 6.1 Übersicht

Die 4LHA-Serie deckt den Leistungsbereich 240–315 PS ab und wird primär in Motorbooten von 10–16 m eingesetzt. Die Motoren zeichnen sich durch hohe Leistungsdichte bei kompakten Abmessungen aus.

### 6.2 4LHA-STP — 240 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 4 Zylinder in Reihe, Common Rail, Turbo, Ladeluftkühlung |
| Hubraum | 3.318 cm³ |
| Bohrung × Hub | 98 × 110 mm |
| Leistung | 240 PS (176 kW) bei 3.300 U/min |
| Max. Drehmoment | 48,5 kgm bei 2.300 U/min |
| Verdichtungsverhältnis | 16,3:1 |
| Einspritzung | Common Rail, 2.000 bar |
| Kühlsystem | Süßwasser mit Seewasser-Wärmetauscher, ölgekühlter Turbo |
| Startanlage | Elektrisch 12V, 4,0 kW Anlasser |
| Lichtmaschine | 12V / 150A |
| Kraftstoffverbrauch | 50 L/h bei Volllast |
| Kraftstoffverbrauch Reisefahrt | 32 L/h bei 2.600 U/min |
| Spez. Verbrauch | 210 g/kWh |
| Ölmenge (Wanne) | 12 L |
| Ölfiltertyp | Yanmar 119593-35400 |
| Kraftstofffilter | Yanmar 120650-55020 |
| Gewicht (trocken) | 380 kg |
| Abmessungen (L×B×H) | 1.020 × 620 × 760 mm |

**Getriebeoptionen:**
- Yanmar KMH61A2: 1:3,48 / 1:3,88 Untersetzung
- ZF 63IV: 1:2,0 bis 1:3,0 Untersetzung (V-Antrieb möglich)
- ZF 85IV: 1:2,0 bis 1:3,5 Untersetzung

**Einsatzbereich:**
- Motorboote 10–14 m (Halbgleiter, Verdränger)
- Typische Konfiguration: Twin-Installation in Motorbooten ab 12 m
- Verdränger: 8–12 kn Reisegeschwindigkeit
- Halbgleiter: 18–24 kn Reisegeschwindigkeit

**Preise (EUR, UVP 2025/26):**
- 4LHA-STP Motor solo: ca. 38.000–42.000 EUR
- 4LHA-STP mit ZF-Getriebe: ca. 44.000–48.500 EUR
- Twin-Installation komplett: ca. 95.000–108.000 EUR

### 6.3 4LHA-DTP — 315 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 4 Zylinder in Reihe, Common Rail, Turbo, Ladeluftkühlung |
| Hubraum | 3.318 cm³ |
| Bohrung × Hub | 98 × 110 mm |
| Leistung | 315 PS (232 kW) bei 3.600 U/min |
| Max. Drehmoment | 55,0 kgm bei 2.500 U/min |
| Verdichtungsverhältnis | 16,3:1 |
| Einspritzung | Common Rail, 2.200 bar |
| Kühlsystem | Süßwasser mit Seewasser-Wärmetauscher, ölgekühlter Turbo |
| Startanlage | Elektrisch 12V, 4,0 kW Anlasser |
| Lichtmaschine | 12V / 150A |
| Kraftstoffverbrauch | 68 L/h bei Volllast |
| Kraftstoffverbrauch Reisefahrt | 42 L/h bei 2.800 U/min |
| Spez. Verbrauch | 208 g/kWh |
| Ölmenge (Wanne) | 12 L |
| Ölfiltertyp | Yanmar 119593-35400 |
| Kraftstofffilter | Yanmar 120650-55020 |
| Gewicht (trocken) | 395 kg |
| Abmessungen (L×B×H) | 1.035 × 620 × 775 mm |

**Getriebeoptionen:**
- ZF 85IV: 1:2,0 bis 1:3,5 Untersetzung
- ZF 220A: 1:2,5 bis 1:4,0 Untersetzung
- ZF 280A: 1:3,0 bis 1:4,5 Untersetzung

**Einsatzbereich:**
- Motorboote 12–16 m
- Halbgleiter: 22–30 kn Reisegeschwindigkeit
- Beliebt bei schnellen Trawleryachten

**Preise (EUR, UVP 2025/26):**
- 4LHA-DTP Motor solo: ca. 44.000–48.000 EUR
- 4LHA-DTP mit ZF-Getriebe: ca. 52.000–57.000 EUR
- Twin-Installation komplett: ca. 115.000–128.000 EUR

### 6.4 LHA-Serie — Gemeinsame Schwachstellen

| Schwachstelle | Betroffene Modelle | Symptom | Lösung |
|---------------|-------------------|---------|--------|
| Turbolader-Lagerverschleiß | 4LHA-DTP >3.000h | Pfeifgeräusch, blauer Rauch | Turbolader überholen, Lager tauschen |
| Seewasserpumpe Wellendichtring | Alle LHA | Wassertropfen am Pumpengehäuse | Dichtring und Impeller 119593-42200 tauschen |
| Schwingungsdämpfer Alterung | Alle LHA >4.000h | Vibrationen bei bestimmten Drehzahlen | Schwingungsdämpfer tauschen |
| Ladeluftkühler-Undichtigkeit | 4LHA-DTP | Leistungsverlust, erhöhter Verbrauch | Ladeluftkühler-Dichtungen erneuern |

---

## 7. LY/LPA-Serie (6-Zylinder-Hochleistung)

### 7.1 Übersicht

Die 6-Zylinder-Reihe umfasst die LY- und LPA-Baureihen und deckt den Leistungsbereich von 315–440 PS ab. Diese Motoren sind für mittlere bis große Motorboote konzipiert.

### 7.2 6LPA-STP2 — 315 PS (Langsamläufer)

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 6 Zylinder in Reihe, Turbo, Ladeluftkühlung |
| Hubraum | 5.813 cm³ |
| Bohrung × Hub | 105 × 112 mm |
| Leistung | 315 PS (232 kW) bei 3.000 U/min |
| Max. Drehmoment | 72 kgm bei 2.200 U/min |
| Verdichtungsverhältnis | 16,0:1 |
| Einspritzung | Common Rail, 2.000 bar |
| Kühlsystem | Süßwasser, Seewasser-Wärmetauscher, Ölkühler |
| Startanlage | Elektrisch 12V oder 24V, 5,0 kW |
| Lichtmaschine | 12V / 200A oder 24V / 100A |
| Kraftstoffverbrauch | 62 L/h bei Volllast |
| Kraftstoffverbrauch Reisefahrt | 38 L/h bei 2.400 U/min |
| Spez. Verbrauch | 205 g/kWh |
| Ölmenge (Wanne) | 16 L |
| Ölfiltertyp | Yanmar 119593-35410 |
| Gewicht (trocken) | 530 kg |
| Abmessungen (L×B×H) | 1.210 × 665 × 820 mm |

**Einsatzbereich:**
- Verdränger und Trawleryachten 14–22 m
- Optimiert für Dauerbetrieb bei niedrigen Drehzahlen
- Reisegeschwindigkeit: 8–12 kn

**Preise (EUR, UVP 2025/26):**
- 6LPA-STP2 Motor solo: ca. 52.000–57.000 EUR
- 6LPA-STP2 mit ZF-Getriebe: ca. 62.000–68.000 EUR

### 7.3 6LY-STP — 380 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 6 Zylinder in Reihe, Common Rail, Turbo, Ladeluftkühlung |
| Hubraum | 5.813 cm³ |
| Bohrung × Hub | 105 × 112 mm |
| Leistung | 380 PS (280 kW) bei 3.300 U/min |
| Max. Drehmoment | 78 kgm bei 2.400 U/min |
| Verdichtungsverhältnis | 16,0:1 |
| Einspritzung | Common Rail, 2.200 bar |
| Kühlsystem | Süßwasser, Seewasser-Wärmetauscher, Ölkühler |
| Startanlage | Elektrisch 12V, 5,0 kW |
| Lichtmaschine | 12V / 200A |
| Kraftstoffverbrauch | 78 L/h bei Volllast |
| Kraftstoffverbrauch Reisefahrt | 48 L/h bei 2.600 U/min |
| Spez. Verbrauch | 208 g/kWh |
| Ölmenge (Wanne) | 16 L |
| Ölfiltertyp | Yanmar 119593-35410 |
| Gewicht (trocken) | 545 kg |
| Abmessungen (L×B×H) | 1.230 × 680 × 840 mm |

**Einsatzbereich:**
- Motorboote 14–20 m (Halbgleiter)
- Reisegeschwindigkeit: 18–28 kn
- Beliebt als Twin-Installation

**Preise (EUR, UVP 2025/26):**
- 6LY-STP Motor solo: ca. 62.000–68.000 EUR
- 6LY-STP mit ZF-Getriebe: ca. 74.000–82.000 EUR
- Twin-Installation: ca. 160.000–180.000 EUR

### 7.4 6LY-UTP — 440 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, 6 Zylinder in Reihe, Common Rail, Turbo, Ladeluftkühlung |
| Hubraum | 5.813 cm³ |
| Bohrung × Hub | 105 × 112 mm |
| Leistung | 440 PS (324 kW) bei 3.300 U/min |
| Max. Drehmoment | 92 kgm bei 2.600 U/min |
| Verdichtungsverhältnis | 15,5:1 |
| Einspritzung | Common Rail, 2.200 bar |
| Aufladung | Hochleistungs-Turbolader mit Wastegate |
| Kühlsystem | Süßwasser, Seewasser-Wärmetauscher, Ölkühler |
| Startanlage | Elektrisch 12V, 5,0 kW |
| Lichtmaschine | 12V / 200A |
| Kraftstoffverbrauch | 92 L/h bei Volllast |
| Kraftstoffverbrauch Reisefahrt | 56 L/h bei 2.600 U/min |
| Spez. Verbrauch | 210 g/kWh |
| Ölmenge (Wanne) | 16 L |
| Ölfiltertyp | Yanmar 119593-35410 |
| Gewicht (trocken) | 560 kg |
| Abmessungen (L×B×H) | 1.250 × 690 × 855 mm |

**Einsatzbereich:**
- Motorboote 16–22 m (Gleiter/Halbgleiter)
- Reisegeschwindigkeit: 24–35 kn
- Höchste Leistung im 6-Zylinder-Programm

**Preise (EUR, UVP 2025/26):**
- 6LY-UTP Motor solo: ca. 72.000–78.000 EUR
- 6LY-UTP mit ZF-Getriebe: ca. 86.000–94.000 EUR
- Twin-Installation: ca. 185.000–205.000 EUR

### 7.5 LY/LPA-Serie — Gemeinsame Schwachstellen

| Schwachstelle | Betroffene Modelle | Symptom | Lösung |
|---------------|-------------------|---------|--------|
| Kurbelgehäuse-Entlüftung verstopft | Alle 6LY/LPA | Ölaustritt an Dichtungen, Überdruck | Entlüftung reinigen, alle 500h prüfen |
| Injektoren Drift | 6LY-UTP >3.000h | Ungleichmäßiger Lauf, Rauch | Injektoren elektronisch justieren |
| Wasserpumpen-Welle | 6LY >4.000h | Leckage, Kühlmittelverlust | Welle und Dichtung erneuern |
| Motorlager Durchsacken | Alle 6-Zyl. >3.000h | Fluchtungsfehler, Vibrationen | Motorlager Satz erneuern |

---

## 8. BY-Serie (V8-Großmotoren)

### 8.1 Übersicht

Die BY-Serie (Big Yacht) stellt Yanmars Einstieg in die Hochleistungs-V8-Klasse dar. Die Motoren sind für schnelle Motorboote und große Yachten konzipiert.

### 8.2 8BY-220Z — V8, 480 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, V8 (90°), Common Rail, Twin-Turbo |
| Hubraum | 5.954 cm³ |
| Bohrung × Hub | 94 × 107 mm |
| Leistung | 480 PS (353 kW) bei 3.800 U/min |
| Max. Drehmoment | 96 kgm bei 2.600 U/min |
| Verdichtungsverhältnis | 15,5:1 |
| Einspritzung | Common Rail, 2.400 bar |
| Aufladung | Twin-Turbo mit Ladeluftkühlung |
| Kühlsystem | Süßwasser, Doppel-Wärmetauscher |
| Startanlage | Elektrisch 12V, 6,0 kW Anlasser |
| Lichtmaschine | 12V / 250A |
| Kraftstoffverbrauch | 105 L/h bei Volllast |
| Kraftstoffverbrauch Reisefahrt | 62 L/h bei 3.000 U/min |
| Spez. Verbrauch | 205 g/kWh |
| Ölmenge (Wanne) | 18 L |
| Gewicht (trocken) | 520 kg |
| Abmessungen (L×B×H) | 1.050 × 780 × 720 mm |

**Getriebeoptionen:**
- ZF 280A: Diverse Untersetzungen
- ZF 325A: Für höhere Lasten
- V-Antrieb und Wellenanlage

**Einsatzbereich:**
- Motorboote 14–20 m (Gleiter)
- Reisegeschwindigkeit: 28–38 kn
- Twin-/Triple-Installation möglich

**Preise (EUR, UVP 2025/26):**
- 8BY-220Z Motor solo: ca. 85.000–92.000 EUR
- 8BY-220Z mit ZF-Getriebe: ca. 100.000–110.000 EUR

### 8.3 8BY-260Z — V8, 530 PS

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Typ | 4-Takt-Diesel, V8 (90°), Common Rail, Twin-Turbo |
| Hubraum | 5.954 cm³ |
| Bohrung × Hub | 94 × 107 mm |
| Leistung | 530 PS (390 kW) bei 4.000 U/min |
| Max. Drehmoment | 102 kgm bei 2.800 U/min |
| Verdichtungsverhältnis | 15,5:1 |
| Einspritzung | Common Rail, 2.500 bar |
| Aufladung | Twin-Turbo mit Ladeluftkühlung und Wastegate |
| Kühlsystem | Süßwasser, Doppel-Wärmetauscher |
| Startanlage | Elektrisch 12V, 6,0 kW Anlasser |
| Lichtmaschine | 12V / 250A |
| Kraftstoffverbrauch | 118 L/h bei Volllast |
| Kraftstoffverbrauch Reisefahrt | 72 L/h bei 3.200 U/min |
| Spez. Verbrauch | 208 g/kWh |
| Ölmenge (Wanne) | 18 L |
| Gewicht (trocken) | 530 kg |
| Abmessungen (L×B×H) | 1.060 × 790 × 730 mm |

**Preise (EUR, UVP 2025/26):**
- 8BY-260Z Motor solo: ca. 95.000–105.000 EUR
- 8BY-260Z mit ZF-Getriebe: ca. 112.000–124.000 EUR
- Twin-Installation: ca. 240.000–268.000 EUR

---

## 9. Saildrive-Systeme

### 9.1 Übersicht Saildrive

Yanmars Saildrive-Aggregate sind integrierte Antriebseinheiten, die Motor und Unterwasserantrieb in einem Gerät vereinen. Sie ersetzen die konventionelle Wellenanlage mit Stevenrohr und Stopfbuchse.

**Vorteile Saildrive:**
- Kein Stevenrohr, keine Stopfbuchse → wartungsfreundlicher
- Geringerer Tiefgang des Antriebs
- Besserer Propellerwirkungsgrad durch vertikale Wellenposition
- Einfacherer Einbau bei Neubauten
- Weniger Vibrationsübertragung

**Nachteile Saildrive:**
- Manschette als potenzielle Undichtigkeitsstelle → regelmäßige Kontrolle
- Eingeschränkte Propellerauswahl
- Teurer als einfache Wellenanlage
- Weniger robust bei Grundberührung

### 9.2 SD20 — Leichter Saildrive

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Einsatz | YM-Serie, GM-Serie (bis 29 PS) |
| Max. Motorleistung | 30 PS |
| Max. Drehmoment (Eingang) | 6,5 kgm |
| Untersetzung | 1:2,14 oder 1:2,64 |
| Propellerschaft | 25 mm |
| Max. Propellergröße | 16" Durchmesser |
| Gewicht | 22 kg |
| Manschettentyp | Gummi-Faltmanschette |
| Manschetten-Wechselintervall | Alle 7 Jahre oder bei Beschädigung |
| Zinkanode | Yanmar 196420-02652 (Ring-Anode) |
| Getriebeöl | SAE 30, ca. 0,5 L |
| Ölwechselintervall | 250 Betriebsstunden oder jährlich |
| Antifouling | Ja, Propeller und Gehäuse |

**Manschette SD20:**
- Teilenummer: Yanmar 196420-01950
- Material: CR-Neopren, seewasserbeständig
- Einbauposition: Unterhalb der Wasserlinie, im Rumpfdurchbruch
- Prüfintervall: Jährlich visuell, alle 3 Jahre demontieren und prüfen
- Wechselintervall: Alle 7 Jahre oder bei Rissen/Verhärtung
- Preis: ca. 280–350 EUR

**Preise SD20 (EUR, UVP 2025/26):**
- SD20 Komplett: ca. 2.800–3.200 EUR
- SD20 Manschette: ca. 280–350 EUR
- SD20 Zinkanode: ca. 35–45 EUR
- SD20 Getriebeöl-Service: ca. 40–60 EUR

### 9.3 SD25 — Mittlerer Saildrive

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Einsatz | 3YM30, 3JH40 (bis 40 PS) |
| Max. Motorleistung | 40 PS |
| Max. Drehmoment (Eingang) | 9,5 kgm |
| Untersetzung | 1:2,14 oder 1:2,64 |
| Propellerschaft | 30 mm |
| Max. Propellergröße | 18" Durchmesser |
| Gewicht | 28 kg |
| Manschettentyp | Gummi-Faltmanschette, verstärkt |
| Manschetten-Wechselintervall | Alle 7 Jahre |
| Zinkanode | Yanmar 196420-02652 (Ring-Anode) |
| Getriebeöl | SAE 30, ca. 0,7 L |

**Manschette SD25:**
- Teilenummer: Yanmar 196420-01960
- Prüfintervall: Jährlich visuell
- Preis: ca. 310–380 EUR

**Preise SD25 (EUR, UVP 2025/26):**
- SD25 Komplett: ca. 3.400–3.900 EUR

### 9.4 SD50 — Schwerer Saildrive

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Einsatz | 3JH40, 4JH45, 4JH57 (bis 60 PS) |
| Max. Motorleistung | 60 PS |
| Max. Drehmoment (Eingang) | 14 kgm |
| Untersetzung | 1:2,36 / 1:2,62 / 1:2,81 |
| Propellerschaft | 30 mm oder 35 mm |
| Max. Propellergröße | 20" Durchmesser |
| Gewicht | 34 kg |
| Manschettentyp | Doppellippen-Gummimanschette |
| Manschetten-Wechselintervall | Alle 7 Jahre |
| Zinkanode | Yanmar 196420-02660 (Ring-Anode) |
| Getriebeöl | SAE 30, ca. 0,9 L |

**Manschette SD50:**
- Teilenummer: Yanmar 196420-02100
- Preis: ca. 380–450 EUR

**Preise SD50 (EUR, UVP 2025/26):**
- SD50 Komplett: ca. 4.200–4.800 EUR

### 9.5 SD60 — Hochleistungs-Saildrive

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Einsatz | 4JH57, 4JH80, 4JH110 (bis 115 PS) |
| Max. Motorleistung | 115 PS |
| Max. Drehmoment (Eingang) | 24 kgm |
| Untersetzung | 1:2,62 / 1:2,81 / 1:3,05 / 1:3,42 |
| Propellerschaft | 35 mm oder 40 mm |
| Max. Propellergröße | 22" Durchmesser |
| Gewicht | 42 kg |
| Manschettentyp | Doppellippen-Gummimanschette, verstärkt |
| Manschetten-Wechselintervall | Alle 7 Jahre |
| Zinkanode | Yanmar 196420-02670 (Ring-Anode, vergrößert) |
| Getriebeöl | SAE 30, ca. 1,2 L |

**Manschette SD60:**
- Teilenummer: Yanmar 196420-02200
- Material: HNBR-Gummi (hydrogenated nitrile butadiene rubber), UV-beständig
- Preis: ca. 450–530 EUR

**Preise SD60 (EUR, UVP 2025/26):**
- SD60 Komplett: ca. 5.800–6.500 EUR

### 9.6 Saildrive-Wartung — Kritische Hinweise

**Manschettenprüfung (lebenswichtig!):**
1. Jährlich im Winterlager visuell prüfen
2. Auf Risse, Verhärtung, Quellung, Verformung achten
3. Alle 3 Jahre demontieren und beide Seiten prüfen
4. Nach 7 Jahren zwingend tauschen, unabhängig vom Zustand
5. **WARNUNG:** Eine gerissene Manschette kann zum Sinken des Bootes führen!

**Zinkanoden:**
- Alle 6 Monate prüfen (bei jedem Slipvorgang)
- Tauschen, wenn >50 % aufgelöst
- In Brackwasser: kürzere Intervalle (3–4 Monate prüfen)

**Getriebeöl:**
- Jährlich oder alle 250h wechseln
- SAE 30 Marine Getriebeöl verwenden
- Ölstand visuell am Schauglas prüfen
- Bei milchigem Öl: Wassereintritt → sofort Dichtungen prüfen

---

## 10. Getriebe-Optionen

### 10.1 Yanmar KM-Serie (Wendegetriebe)

| Modell | Motor-Zuordnung | Untersetzung | Typ | Gewicht (kg) | Preis EUR |
|--------|----------------|-------------|-----|-------------|-----------|
| KM2A | 1GM10 | 1:1,26 | Mechanisch | 5,5 | 850–950 |
| KM2C | 1GM10, 1YM15 | 1:1,38 | Mechanisch | 5,8 | 900–1.000 |
| KM2C-1 | 1YM15 | 1:1,36 | Mechanisch | 5,8 | 900–1.000 |
| KM2C-2 | 1YM15 | 1:1,61 | Mechanisch | 6,0 | 950–1.050 |
| KM2P | 2GM20, 2YM15, 2YM20 | 1:1,97 | Mechanisch | 8,5 | 1.100–1.250 |
| KM2P-1 | 2YM15, 2YM20 | 1:2,04 | Mechanisch | 8,8 | 1.150–1.300 |
| KM2P-2 | 2YM15, 2YM20 | 1:2,36 | Mechanisch | 9,0 | 1.200–1.350 |
| KM3A | 3GM30, 3YM20, 3YM30 | 1:2,21 | Mechanisch | 12,5 | 1.400–1.600 |
| KM3A-1 | 3GM30, 3YM20, 3YM30 | 1:2,62 | Mechanisch | 13,0 | 1.500–1.700 |
| KMH4A | 3JH40, 4JH45, 4JH57 | 1:2,04–2,62 | Hydraulisch | 22,0 | 2.400–2.800 |
| KMH4A2 | 4JH57, 4JH80, 4LHA | 1:2,81–3,42 | Hydraulisch | 25,0 | 2.800–3.200 |
| KMH61A | 4JH80, 4JH110 | 1:2,91–3,23 | Hydraulisch | 30,0 | 3.200–3.600 |
| KMH61A2 | 4JH110, 4LHA | 1:3,48–3,88 | Hydraulisch | 33,0 | 3.500–4.000 |

### 10.2 ZF-Getriebe (für LHA/LY/BY-Serie)

| Modell | Motor-Zuordnung | Untersetzung | Typ | Preis EUR |
|--------|----------------|-------------|-----|-----------|
| ZF 63IV | 4LHA-STP | 1:2,0–3,0 | Hydraulisch | 3.800–4.500 |
| ZF 85IV | 4LHA-STP/DTP | 1:2,0–3,5 | Hydraulisch | 4.500–5.200 |
| ZF 220A | 4LHA-DTP, 6LPA | 1:2,5–4,0 | Hydraulisch | 5.500–6.500 |
| ZF 280A | 6LY, 8BY | 1:3,0–4,5 | Hydraulisch | 6.800–8.000 |
| ZF 325A | 8BY | 1:3,5–5,0 | Hydraulisch | 8.500–10.000 |

---

## 11. Kühlsysteme

### 11.1 Kühlsystem-Typen bei Yanmar

**Direktkühlung (Seewasserkühlung):**
- Nur bei 1GM10 und 1YM15
- Seewasser fließt direkt durch den Motorblock
- Einfach, aber korrosionsanfällig
- Zinkanode im Motorblock: Yanmar 128370-02210

**Indirekte Kühlung (Süßwasser + Seewasser-Wärmetauscher):**
- Standard ab 2GM20 / 2YM15 und aufwärts
- Geschlossener Süßwasser-Kreislauf mit Frostschutz
- Seewasser kühlt über Wärmetauscher
- Deutlich längere Motorlebensdauer

### 11.2 Kühlsystem-Komponenten

| Komponente | Teilenummer (Beispiel JH-Serie) | Wechselintervall | Preis EUR |
|-----------|-------------------------------|-------------------|-----------|
| Impeller | 129670-42531 (JH-Serie) | 500h oder jährlich | 45–65 |
| Impeller | 128170-02070 (GM-Serie) | 500h oder jährlich | 28–38 |
| Impeller | 128990-42200 (YM-Serie) | 500h oder jährlich | 35–48 |
| Thermostat | 129470-49801 (JH-Serie) | 2.000h oder bei Bedarf | 55–75 |
| Thermostat | 119773-49550 (YM-Serie) | 2.000h oder bei Bedarf | 42–58 |
| Zinkanode Motorblock | 119574-44150 (JH-Serie) | 250h oder bei >50% Verbrauch | 18–25 |
| Zinkanode Motorblock | 128370-02210 (GM-Serie) | 250h oder halbjährlich | 12–18 |
| Zinkanode Wärmetauscher | 119574-44160 (JH-Serie) | 250h | 22–30 |
| Kühlmittel | Yanmar Premium Coolant | 1.000h oder 2 Jahre | 25–35/L |
| Seewasserpumpen-Dichtung | 129670-42560 (JH-Serie) | Bei Undichtigkeit | 32–45 |
| Wärmetauscher O-Ring-Satz | 129470-49810 (JH-Serie) | 2.000h | 45–65 |
| Keilriemen Kühlwasserpumpe | 129612-42290 (JH-Serie) | 1.000h oder jährlich | 18–28 |
| Keilriemen Kühlwasserpumpe | 128170-42440 (GM-Serie) | 1.000h oder jährlich | 14–22 |
| Keilriemen | 119773-42680 (YM-Serie) | 1.000h oder jährlich | 16–24 |

### 11.3 Kühlmittel-Spezifikation

- **Empfohlen:** Yanmar Premium Long-Life Coolant (OAT-basiert)
- **Alternativ:** Ethylenglykol-basiert, silikatfrei, nach ASTM D3306
- **Mischungsverhältnis:** 50:50 mit destilliertem Wasser (Frostschutz bis -37 °C)
- **Für Mittelmeer-Einsatz:** 30:70 reicht für Frostschutz bis -17 °C
- **Niemals:** Leitungswasser verwenden (Kalkablagerungen)
- **Wechselintervall:** Alle 2 Jahre oder 1.000 Betriebsstunden

---

## 12. Wartungsintervalle und Servicepläne

### 12.1 Serviceplan GM-Serie

| Intervall | Arbeiten | Ersatzteile |
|-----------|----------|-------------|
| **Täglich** | Ölstand prüfen, Kühlwasserstand, Sichtprüfung Leckagen | — |
| **50 h** | Motoröl und Filter wechseln (Erstservice) | Öl 15W-40, Filter 119305-35151 |
| **100 h** | Keilriemen prüfen, Kraftstofffilter prüfen | Riemen 128170-42440 |
| **250 h** | Motoröl und Filter wechseln, Ventilspiel prüfen (0,15 mm Ein/Aus), Zinkanode prüfen | Öl 15W-40, Filter, Anode 128370-02210 |
| **500 h** | + Impeller tauschen, Kraftstofffilter tauschen, Keilriemen tauschen (wenn verschlissen) | Impeller 128170-02070, Filter 104500-55710 |
| **1.000 h** | + Kühlmittel wechseln (2GM/3GM), Einspritzdüsen prüfen (Öffnungsdruck 140 bar) | Kühlmittel, Düsen 124610-53001 |
| **2.000 h** | + Thermostat prüfen, Wärmetauscher reinigen, alle Schlauchschellen prüfen | Thermostat 124610-49551 |

### 12.2 Serviceplan YM-Serie

| Intervall | Arbeiten | Ersatzteile |
|-----------|----------|-------------|
| **Täglich** | Ölstand prüfen, Kühlwasserstand, visuelle Inspektion | — |
| **50 h** | Motoröl und Filter wechseln (Erstservice) | Öl 15W-40, Filter 119305-35170 |
| **100 h** | Keilriemen prüfen, Kraftstofffilter prüfen, Kraftstoffsystem entlüften | Riemen 119773-42680 |
| **250 h** | Motoröl und Filter wechseln, Ventilspiel prüfen (Ein: 0,15 mm, Aus: 0,15 mm), Zinkanode prüfen | Öl, Filter, Anode 119574-44150 |
| **500 h** | + Impeller tauschen, Kraftstofffilter tauschen, Keilriemen prüfen/tauschen | Impeller 128990-42200, Filter 104500-55710, Riemen |
| **1.000 h** | + Kühlmittel wechseln, Einspritzdüsen prüfen (Öffnungsdruck 150 bar), Auspuffanlage prüfen | Kühlmittel, Düsen |
| **2.000 h** | + Thermostat tauschen, Wärmetauscher zerlegen und reinigen, Seewasserpumpe komplett überholen | Thermostat 119773-49550, Pumpendichtung 119773-42600 |

### 12.3 Serviceplan JH-Serie (Common Rail)

| Intervall | Arbeiten | Ersatzteile |
|-----------|----------|-------------|
| **Täglich** | Ölstand prüfen, Kühlwasserstand, Vorfilter Wasserabscheider prüfen | — |
| **50 h** | Motoröl und Filter wechseln (Erstservice), Kraftstoffsystem prüfen | Öl 15W-40 (CI-4), Filter 129150-35170 |
| **250 h** | Motoröl und Filter wechseln, Zinkanode prüfen, Keilriemen prüfen | Öl, Filter, Anode 119574-44150 |
| **500 h** | + Impeller tauschen, Kraftstofffilter primär und sekundär tauschen, Keilriemen tauschen | Impeller 129670-42531, Filter 129004-55810 + 129A00-55800, Riemen 129612-42290 |
| **1.000 h** | + Kühlmittel wechseln, Ventilspiel prüfen (Ein: 0,20 mm, Aus: 0,20 mm), Luftfilter tauschen | Kühlmittel, Luftfilter 129195-12530 |
| **2.000 h** | + Thermostat tauschen, Wärmetauscher zerlegen/reinigen, Seewasserpumpe überholen, Turbolader prüfen (4JH80/110), Injektoren prüfen lassen | Thermostat 129470-49801, O-Ring-Satz 129470-49810, Pumpen-Kit |
| **5.000 h** | + Generalüberholung empfohlen: Kolbenringe, Lager, Injektoren komplett, Turbo-Revision | Siehe Überholungssatz |

### 12.4 Serviceplan LHA/LY/BY-Serie

| Intervall | Arbeiten | Ersatzteile |
|-----------|----------|-------------|
| **Täglich** | Ölstand, Kühlmittelstand, Seewasserfilter prüfen, Sichtprüfung | — |
| **100 h** | Motoröl und Filter wechseln (Erstservice) | Öl 15W-40 (CI-4), Filter 119593-35400 |
| **250 h** | Motoröl und Filter wechseln, Zinkanoden prüfen, Getriebeöl prüfen | Öl, Filter, Anoden |
| **500 h** | + Impeller tauschen, Kraftstofffilter tauschen, Keilriemen tauschen, Getriebeölwechsel | Impeller 119593-42200, Filter 120650-55020, Getriebeöl |
| **1.000 h** | + Kühlmittel wechseln, Ventilspiel prüfen, Luftfilter tauschen, Turbolader-Spiel prüfen | Kühlmittel, Luftfilter |
| **2.000 h** | + Wärmetauscher zerlegen/reinigen, Injektoren prüfen, Schwingungsdämpfer prüfen, alle Schlauchverbindungen | Thermostat, O-Ring-Sätze |
| **4.000 h** | + Generalüberholung empfohlen | Siehe Überholungssatz |

### 12.5 Ölspezifikationen

| Motor-Serie | Empfohlenes Öl | Viskosität | API-Klasse | Menge (L) |
|------------|----------------|-----------|-----------|-----------|
| GM-Serie | Mineral-Motoröl | 15W-40 | CF | 1,4–2,6 |
| YM-Serie | Mineral- oder Synth. | 15W-40 | CF-4 | 1,5–3,0 |
| JH-Serie | Synthetisch empfohlen | 15W-40 | CI-4 | 4,5–7,2 |
| LHA-Serie | Vollsynthetisch | 15W-40 | CI-4 | 12,0 |
| LY/LPA-Serie | Vollsynthetisch | 15W-40 | CI-4 | 16,0 |
| BY-Serie | Vollsynthetisch | 10W-40 oder 15W-40 | CJ-4 | 18,0 |

---

## 13. Ersatzteile und Teilenummern

### 13.1 Impeller (Seewasserpumpe) — Vollständige Liste

| Motor | Teilenummer | Material | Flügel | Preis EUR |
|-------|------------|----------|--------|-----------|
| 1GM10 | 128170-02070 | NBR-Gummi | 6 | 28–38 |
| 2GM20 | 128170-02070 | NBR-Gummi | 6 | 28–38 |
| 3GM30 | 128170-02070 | NBR-Gummi | 6 | 28–38 |
| 1YM15 | 128990-42200 | NBR-Gummi | 8 | 35–48 |
| 2YM15 | 128990-42200 | NBR-Gummi | 8 | 35–48 |
| 2YM20 | 128990-42200 | NBR-Gummi | 8 | 35–48 |
| 3YM20 | 128990-42200 | NBR-Gummi | 8 | 35–48 |
| 3YM30 | 128990-42200 | NBR-Gummi | 8 | 35–48 |
| 3JH40 | 129670-42531 | NBR-Gummi | 10 | 45–65 |
| 4JH45 | 129670-42531 | NBR-Gummi | 10 | 45–65 |
| 4JH57 | 129670-42531 | NBR-Gummi | 10 | 45–65 |
| 4JH80 | 129670-42531 | NBR-Gummi | 10 | 45–65 |
| 4JH110 | 129670-42531 | NBR-Gummi | 10 | 45–65 |
| 4LHA | 119593-42200 | NBR-Gummi | 12 | 65–85 |
| 6LY/LPA | 119593-42200 | NBR-Gummi | 12 | 65–85 |

### 13.2 Ölfilter

| Motor | Teilenummer | Typ | Preis EUR |
|-------|------------|-----|-----------|
| GM-Serie | 119305-35151 | Patronenfilter | 12–18 |
| YM-Serie | 119305-35170 | Patronenfilter | 14–20 |
| JH-Serie | 129150-35170 | Anschraubfilter | 18–26 |
| LHA-Serie | 119593-35400 | Anschraubfilter | 22–32 |
| LY/LPA-Serie | 119593-35410 | Anschraubfilter (2×) | 24–34 (je) |

### 13.3 Kraftstofffilter

| Motor | Teilenummer (Primär) | Teilenummer (Sekundär) | Preis EUR (je) |
|-------|---------------------|----------------------|----------------|
| GM-Serie | 104500-55710 | — | 14–20 |
| YM-Serie | 104500-55710 | — | 14–20 |
| JH-Serie | 129004-55810 | 129A00-55800 | 18–26 / 22–30 |
| LHA-Serie | 120650-55020 | — | 28–38 |
| LY/LPA-Serie | 120650-55020 | — | 28–38 |

### 13.4 Keilriemen

| Motor | Teilenummer | Profil | Preis EUR |
|-------|------------|--------|-----------|
| GM-Serie | 128170-42440 | A-Profil, 10×6 mm | 14–22 |
| YM-Serie | 119773-42680 | A-Profil, 13×8 mm | 16–24 |
| JH-Serie | 129612-42290 | B-Profil, 17×11 mm | 18–28 |
| 4JH80/110 | 129612-42300 | B-Profil, 17×11 mm (2 Stück) | 20–30 (je) |

### 13.5 Zinkanoden

| Einsatzort | Teilenummer | Typ | Preis EUR |
|------------|------------|-----|-----------|
| Motorblock GM | 128370-02210 | Stift-Anode | 12–18 |
| Motorblock YM | 119574-44150 | Stift-Anode | 14–20 |
| Motorblock JH | 119574-44150 | Stift-Anode | 14–20 |
| Wärmetauscher JH | 119574-44160 | Stift-Anode klein | 22–30 |
| Saildrive SD20 | 196420-02652 | Ring-Anode | 35–45 |
| Saildrive SD25 | 196420-02652 | Ring-Anode | 35–45 |
| Saildrive SD50 | 196420-02660 | Ring-Anode | 42–55 |
| Saildrive SD60 | 196420-02670 | Ring-Anode groß | 48–62 |

### 13.6 Motorlager (Gummielastisch)

| Motor-Serie | Teilenummer | Tragkraft (kg) | Stück/Motor | Preis EUR (je) |
|------------|------------|---------------|-------------|----------------|
| GM-Serie | 128170-08340 | 25 | 4 | 28–38 |
| YM-Serie | 128170-08350 | 30 | 4 | 32–42 |
| JH-Serie | 129470-08340 | 65 | 4 | 45–60 |
| LHA-Serie | 119593-08340 | 120 | 4 | 65–85 |
| LY/LPA-Serie | 119593-08350 | 180 | 4 | 85–110 |
| BY-Serie | — (Spezial) | 200 | 6 | 110–140 |

### 13.7 Anlasser

| Motor-Serie | Teilenummer | Leistung | Spannung | Preis EUR |
|------------|------------|---------|---------|-----------|
| GM-Serie | 128170-77010 | 1,2 kW | 12V | 280–350 |
| YM-Serie | 119773-77010 | 1,4 kW | 12V | 320–400 |
| JH-Serie | 129470-77010 | 2,0–2,5 kW | 12V | 420–550 |
| LHA-Serie | 119593-77010 | 4,0 kW | 12V | 580–720 |

### 13.8 Lichtmaschine

| Motor-Serie | Teilenummer | Leistung | Spannung | Preis EUR |
|------------|------------|---------|---------|-----------|
| GM-Serie | 128170-77200 | 35–55A | 12V | 280–380 |
| YM-Serie | 119773-77200 | 80A | 12V | 350–450 |
| JH-Serie | 129470-77200 | 125A | 12V | 420–550 |
| LHA/LY-Serie | 119593-77200 | 150–200A | 12V | 550–720 |

---

## 14. Bekannte Schwachstellen je Modell

### 14.1 Modellübergreifende Schwachstellen (Alle Yanmar)

| Nr. | Schwachstelle | Beschreibung | Betroffene Teile | Prävention |
|-----|--------------|-------------|-----------------|------------|
| S01 | Impeller-Versagen | Häufigste Ursache für Überhitzung. NBR-Gummi wird spröde bei Nichtbenutzung. | Impeller, Pumpengehäuse | Jährlich tauschen, auch bei wenig Betriebsstunden |
| S02 | Kraftstoff-Kontamination | Diesel-Pest (Mikroorganismen), Wasser im Tank, Paraffin-Ausfall im Winter | Kraftstofffilter, Injektoren, Tank | Biozid verwenden, Wasserabscheider, Tank voll halten |
| S03 | Korrosion Kühlsystem | Innenkorrosion durch falsches oder altes Kühlmittel | Wärmetauscher, Motorblock, Zylinderkopf | Kühlmittel alle 2 Jahre wechseln, korrekte Mischung |
| S04 | Elektrolyse/galvanische Korrosion | Falsche Erdung, fehlender Isolator am Landanschluss | Saildrive-Gehäuse, Propeller, Welle | Galvanischer Isolator, korrekte Erdung |
| S05 | Auspuffanlage Korrosion | Seewassereindruck über Auspuff, Mischkammer-Rost | Auspuffmischkammer, Schlauch, Wassersammler | Siphon korrekt installiert, Schwanenhals hoch genug |

### 14.2 Modellspezifische Schwachstellen — Detailübersicht

**1GM10:**
- Direktkühlung → stärkere Innenkorrosion als indirekt gekühlte Motoren
- Einzylinder-Vibrationen belasten Motorlager stärker
- Lichtmaschine nur 35A → unzureichend für moderne Elektronik-Ausstattung
- **Empfehlung:** Zinkanode alle 200h prüfen, Motorlager alle 1.500h tauschen

**2GM20 / 3GM30:**
- Auspuffkrümmer-Rissbildung nach 3.000–5.000h (bekanntes Serienproblem)
- Stopfbuchse (Wellendichtung) erfordert regelmäßiges Nachziehen
- Vorwärmer (Glühkerze) wird korrosionsanfällig in salziger Luft
- **Empfehlung:** Krümmer regelmäßig auf Risse prüfen, Glühkerzen alle 2.000h tauschen

**YM-Serie (alle Modelle):**
- Kraftstoff-Förderpumpe wird nach 3.000–4.000h schwächer
- Thermostat kann in offener Position klemmen → Motor bleibt kalt
- Auspuffmischkammer (GFK oder Edelstahl) altert je nach Material
- **Empfehlung:** Förderpumpe prophylaktisch bei 4.000h tauschen

**3JH40:**
- ECU-Feuchtigkeitsempfindlichkeit (Kondensat im Motorraum)
- Seewasserpumpe Wellendichtring bei Saisonstart (Trockenlauf-Risiko)
- **Empfehlung:** Motorraum-Belüftung verbessern, Impeller vor Saisonstart prüfen

**4JH45 / 4JH57:**
- Kabelbaum-Vibration am Saildrive-Übergang
- Common-Rail-System empfindlich gegenüber Diesel-Qualität
- **Empfehlung:** Kabelbaum mit zusätzlichen Schellen fixieren, Vorfilter 10µm installieren

**4JH80 / 4JH110:**
- Turbolader-Öl-Dichtung nach 3.000–4.000h
- Ladeluftkühler-Korrosion (Seewasserseite)
- Höherer thermischer Stress auf Zylinderkopfdichtung
- **Empfehlung:** Turbo nach dem Abstellen 30 Sekunden im Leerlauf nachlaufen lassen

**4LHA-DTP:**
- Turbolager bei hartem Betrieb (Vollgas ohne Warmfahren)
- Schwingungsdämpfer (Harmonik-Balancer) nach 4.000–5.000h
- **Empfehlung:** Mindestens 5 Minuten warmfahren, 3 Minuten abkühlen lassen

**6LY-UTP / 8BY:**
- Hochleistungs-Turbolader erfordern strenge Warmfahr-/Abkühlregime
- Injektoren-Drift bei hohen Betriebsstunden
- Hoher Kraftstoffverbrauch → Kraftstoff-Qualität kritisch
- **Empfehlung:** Kraftstoff-Polieranlage installieren, Injektoren alle 2.000h kalibrieren

---

## 15. Motorlager und Befestigung

### 15.1 Motorlager-Typen

**Yanmar Genuine Motorlager (Standard):**
- Material: Stahl-Gummi-Verbund (Naturkautschuk, Shore A 60)
- Ausführung: 4 Stück pro Motor (GM/YM/JH/LHA), 6 Stück bei BY-Serie
- Einstellbar: Höhenverstellung über Gewinde (±15 mm)
- Befestigung: M10 (GM/YM), M12 (JH), M14 (LHA/LY), M16 (BY)

**Nachrüst-Empfehlungen:**
- Vetus Motorlager (kompatibel, z. T. bessere Dämpfung)
- Polyflex-Lager (für starke Vibrationen)
- Alle 2.000–3.000 Betriebsstunden Lager auf Ermüdung prüfen
- Bei Motorausrichtung: Fluchtung Welle-Getriebe ≤ 0,05 mm Toleranz

### 15.2 Einbauanforderungen

| Parameter | GM-Serie | YM-Serie | JH-Serie | LHA-Serie | LY/BY-Serie |
|-----------|---------|---------|---------|----------|-------------|
| Motorraum-Mindesttiefe | 450 mm | 500 mm | 650 mm | 800 mm | 900 mm |
| Belüftungsquerschnitt | 50 cm² | 60 cm² | 100 cm² | 200 cm² | 350 cm² |
| Abluft-Querschnitt | 40 cm² | 50 cm² | 80 cm² | 160 cm² | 280 cm² |
| Zugang Ölfilter | Seitlich | Seitlich | Oben | Oben | Oben |
| Zugang Impeller | Vorne | Vorne | Vorne | Seitlich | Seitlich |
| Min. Abstand Wand (seitlich) | 50 mm | 60 mm | 80 mm | 100 mm | 120 mm |
| Min. Abstand Wand (oben) | 80 mm | 100 mm | 120 mm | 150 mm | 200 mm |
| Schwerpunkt-Lage ab Unterkante | 180 mm | 200 mm | 280 mm | 340 mm | 380 mm |
| Schalldämmung empfohlen (mm) | 20 | 25 | 30 | 50 | 60 |

---

## 16. Instrumentierung und Überwachung

### 16.1 Yanmar-Instrumentierung

**Analog-Instrumente (Standard GM/YM):**

| Instrument | Funktion | Teilenummer (Beispiel) | Preis EUR |
|-----------|---------|----------------------|-----------|
| Drehzahlmesser | 0–4.000 U/min, mit Betriebsstundenzähler | 129470-91100 | 180–230 |
| Motortemperatur | 40–120 °C | 129470-91200 | 120–160 |
| Öldruck | 0–7 bar | 129470-91300 | 120–160 |
| Ladekontrolle | Lichtmaschine OK/Fehler | 129470-91400 | 45–65 |
| Vorglühanzeige | Glühkerzen aktiv | Im Startschlüssel integriert | — |

**Digitale Instrumente (JH-Serie / LHA / LY / BY):**

| Instrument | Funktion | Teilenummer | Preis EUR |
|-----------|---------|------------|-----------|
| YD25 Digitaldisplay | Multifunktionsdisplay 2,5" TFT | 129470-91500 | 480–580 |
| YD42 Digitaldisplay | Multifunktionsdisplay 4,2" TFT | 129470-91510 | 680–820 |
| VC10 Vessel Control | Gateway CAN-Bus → NMEA 2000 | 129470-91600 | 550–680 |

**YD25/YD42 Anzeigefunktionen:**
- Drehzahl (U/min)
- Motortemperatur (°C)
- Öldruck (bar)
- Batteriespannung (V)
- Betriebsstunden
- Kraftstoffverbrauch (L/h, momentan und Durchschnitt)
- Fehlercodes (DTC)
- Wartungserinnerungen
- Trip-Daten (Distanz, Verbrauch)

### 16.2 Fehlercodes (DTC) — JH-Serie Common Rail

| Code | Beschreibung | Schwere | Maßnahme |
|------|-------------|---------|----------|
| E001 | Kühlmitteltemperatur zu hoch (>105 °C) | KRITISCH | Motor drosseln, Impeller prüfen |
| E002 | Öldruck zu niedrig (<0,5 bar) | KRITISCH | Motor sofort abstellen! |
| E003 | Drehzahlsensor-Signal fehlt | HOCH | Sensor 129470-77050 prüfen/tauschen |
| E004 | Common-Rail-Druck zu niedrig | HOCH | Kraftstofffilter, Hochdruckpumpe prüfen |
| E005 | Common-Rail-Druck zu hoch | HOCH | Druckregelventil prüfen |
| E006 | Kühlmitteltemperatur-Sensor defekt | MITTEL | Sensor 129470-49800 tauschen |
| E007 | Öldrucksensor-Signal fehlt | MITTEL | Sensor prüfen/tauschen |
| E008 | Batteriespannung zu niedrig (<11V) | MITTEL | Batterie/Ladung prüfen |
| E009 | Batteriespannung zu hoch (>16V) | MITTEL | Lichtmaschinenregler prüfen |
| E010 | Injektor-Fehler Zyl. 1 | HOCH | Injektor 129A00-53001 prüfen |
| E011 | Injektor-Fehler Zyl. 2 | HOCH | Injektor prüfen |
| E012 | Injektor-Fehler Zyl. 3 | HOCH | Injektor prüfen |
| E013 | Injektor-Fehler Zyl. 4 | HOCH | Injektor prüfen (nur 4JH) |
| E014 | Kraftstofftemperatur zu hoch | MITTEL | Rücklauf-Kühlung prüfen |
| E015 | Ladelufttemperatur zu hoch (nur Turbo) | MITTEL | Ladeluftkühler prüfen |

### 16.3 NMEA 2000 Integration

Die JH-Serie (ab 2019) und alle LHA/LY/BY-Modelle unterstützen über den VC10 Gateway die Anbindung an NMEA 2000 Bordnetzwerke:

**Übertragene PGNs (Parameter Group Numbers):**

| PGN | Beschreibung |
|-----|-------------|
| 127488 | Engine Parameters, Rapid Update (Drehzahl) |
| 127489 | Engine Parameters, Dynamic (Öldruck, Temp, Betriebsstunden) |
| 127493 | Transmission Parameters (Gang, Öldruck, Temp) |
| 127497 | Trip Parameters (Kraftstoffverbrauch) |
| 127498 | Engine Parameters, Static (Modell, Seriennummer) |
| 127501 | Binary Status Report (Alarmzustände) |
| 65030 | Fuel Economy (Momentanverbrauch) |

---

## 17. Fehlerbilder

### Fehlerbild F01: Motor springt nicht an

**Symptome:** Anlasser dreht, Motor zündet nicht oder nur einzelne Zündungen

**Mögliche Ursachen:**
1. Kraftstoffmangel (Tank leer, Hahn zu)
2. Luft im Kraftstoffsystem
3. Kraftstofffilter verstopft
4. Glühkerzen defekt (bei kaltem Motor)
5. Einspritzdüsen verkokt (GM/YM) oder Injektor-Fehler (JH-CR)
6. Batteriespannung zu niedrig → Anlasser dreht zu langsam
7. Kompressionsverlust (Ventilspiel falsch, Kopfdichtung defekt)
8. ECU-Fehler (nur JH Common Rail)

**Diagnose-Schritte:**
- Kraftstoffvorrat und Hahn prüfen
- Vorfilter auf Wasser/Verunreinigungen prüfen
- System manuell entlüften (Entlüftungsschraube an Einspritzpumpe/Filter)
- Batteriespannung messen (min. 12,4V)
- Glühkerzen auf Funktion prüfen (Stromaufnahme messen)
- Kompression messen: GM/YM ≥25 bar, JH ≥28 bar

### Fehlerbild F02: Motor überhitzt

**Symptome:** Temperaturanzeige >95 °C (GM/YM) bzw. >100 °C (JH), Alarm, Dampf

**Mögliche Ursachen:**
1. Impeller defekt oder Flügel abgebrochen
2. Seewassereinlass verstopft (Muscheln, Plastiktüte, Seegras)
3. Seeventil geschlossen oder eingeschränkt
4. Keilriemen Wasserpumpe gerissen (Süßwasser-Kreislauf)
5. Thermostat defekt (geschlossen bleibend)
6. Kühlmittelstand zu niedrig
7. Wärmetauscher intern verkalkt/zugesetzt
8. Zinkanode Motorblock vollständig aufgelöst → Korrosion blockiert Kanal

**Diagnose-Schritte:**
- Seewasser-Auslass am Auspuff prüfen: kommt Wasser?
- Seeventil öffnen/prüfen, Seewasserfilter reinigen
- Impeller optisch prüfen, abgebrochene Flügel suchen
- Keilriemen auf Spannung und Zustand prüfen
- Kühlmittelstand im Ausgleichsbehälter prüfen
- Thermostat ausbauen und in heißem Wasser testen (öffnet bei 71 °C / 76 °C)

### Fehlerbild F03: Schwarzer Rauch

**Symptome:** Dunkler/schwarzer Auspuffrauch, Leistungsverlust, rauer Lauf

**Mögliche Ursachen:**
1. Luftfilter verstopft
2. Überladung (zu großer Propeller, Bewuchs am Rumpf)
3. Injektoren verkokt oder falsch eingestellt
4. Turbolader defekt (4JH80/110, LHA, LY)
5. Falsche Einspritzzeit
6. Abgasrückstau (Auspuff verstopft, Schalldämpfer blockiert)
7. Motorölstand zu hoch (Öl wird mitverbrannt)

**Diagnose-Schritte:**
- Luftfilter prüfen/reinigen
- Rumpfbewuchs und Propellerzustand prüfen
- Ölstand kontrollieren (nicht über MAX-Markierung)
- Injektoren auf Gleichförmigkeit prüfen (Drehzahlabfall-Test pro Zylinder)
- Turbo-Ladedruck messen (wenn vorhanden)

### Fehlerbild F04: Weißer Rauch

**Symptome:** Weißer/grauer Auspuffrauch, besonders bei kaltem Motor oder unter Last

**Mögliche Ursachen:**
1. Kalter Motor (normal für erste Minuten)
2. Wasser in Brennraum (Zylinderkopfdichtung undicht)
3. Vorkammer-Dichtung undicht (GM-Serie)
4. Injektor undicht (Kraftstoff tropft nach statt zu zerstäuben)
5. Falsche Einspritzzeit (zu spät)
6. Zu geringe Kompression

**Diagnose-Schritte:**
- Kühlmittelverlust feststellen (→ Kopfdichtung)
- Öl auf Emulsion prüfen (milchig = Wassereinbruch)
- Einspritzzeit prüfen (Markierungen an Schwungscheibe/Einspritzpumpe)

### Fehlerbild F05: Blauer Rauch

**Symptome:** Blauer/bläulicher Auspuffrauch, Ölverbrauch erhöht

**Mögliche Ursachen:**
1. Kolbenringe verschlissen
2. Ventilschaftdichtungen undicht
3. Turbolader-Öldichtung defekt (nur Turbo-Motoren)
4. Kurbelgehäuse-Entlüftung verstopft → Überdruck presst Öl in Ansaugung
5. Ölstand zu hoch

**Diagnose-Schritte:**
- Ölverbrauch dokumentieren (normal: <0,1 % des Kraftstoffverbrauchs)
- Kompression messen (Zylindervergleich)
- Kurbelgehäuse-Entlüftung prüfen
- Turbo-Ladedruck prüfen, Ölspuren am Ladeluftrohr

### Fehlerbild F06: Unrunder Lauf / Vibrationen

**Symptome:** Motor läuft ungleichmäßig, vibriert stark, Drehzahl schwankt

**Mögliche Ursachen:**
1. Injektor eines Zylinders defekt
2. Luft im Kraftstoffsystem
3. Ventilspiel falsch
4. Motorlager durchgesackt oder gebrochen
5. Propeller beschädigt (Unwucht)
6. Getriebefluchtung verloren
7. Schwingungsdämpfer defekt (LHA/LY/BY)

**Diagnose-Schritte:**
- Drehzahlabfall-Test: jeden Injektor einzeln abklemmen, Drehzahlabfall vergleichen
- Kraftstoffsystem auf Undichtigkeit und Luft prüfen
- Ventilspiel messen und justieren
- Motorlager visuell prüfen (Risse, Verformung, Aufsitzen)
- Propeller auf Beschädigung/Bewuchs prüfen

### Fehlerbild F07: Öldruck-Alarm

**Symptome:** Öldruckwarnleuchte, Alarm, Anzeige <1 bar im Leerlauf

**Mögliche Ursachen:**
1. Ölstand zu niedrig
2. Ölfilter verstopft
3. Ölpumpe verschlissen
4. Öldruckschalter/-sensor defekt
5. Motorlager (Pleuel/Hauptlager) verschlissen → Spiel zu groß
6. Falsches Öl (zu dünnflüssig)

**Sofortmaßnahme:** Motor SOFORT abstellen und nicht wieder starten bis Ursache geklärt!

### Fehlerbild F08: Diesel-Leckage

**Symptome:** Dieselgeruch, Tropfen am Motor, nasse Stellen

**Mögliche Ursachen:**
1. Einspritzleitungen korrodiert (besonders GM-Serie >15 Jahre)
2. Kraftstoff-Dichtungen am Filter undicht
3. Kraftstoff-Rücklaufleitung porös
4. Injektordichtungen (Kupferscheiben) verhärtet
5. Tankentlüftung verstopft → Überdruck im System

**Brandgefahr!** Diesel auf heißem Auspuffkrümmer kann zu Motorbrand führen.

### Fehlerbild F09: Seewasser-Leckage im Motorraum

**Symptome:** Seewasser in der Bilge, Korrosion an Motorteilen

**Mögliche Ursachen:**
1. Impeller-Gehäusedeckel undicht
2. Seewasserpumpe Wellendichtring defekt
3. Seewasserschlauch-Verbindung lose oder Schlauch porös
4. Seeventil oder Seewasserfilter undicht
5. Wärmetauscher intern undicht (Seewasser in Süßwasser-Kreislauf)
6. Auspuffmischkammer korrodiert
7. Saildrive-Manschette undicht (KRITISCH!)

### Fehlerbild F10: Getriebe-Probleme

**Symptome:** Kein Vortrieb, Schleifen, Ölverlust am Getriebe

**Mögliche Ursachen:**
1. Getriebeöl fehlt oder falsch
2. Schaltgestänge dejustiert
3. Lamellen verschlissen (hydraulische Getriebe)
4. Getriebe-Wellendichtring undicht
5. Schaltzug schwergängig oder gebrochen

### Fehlerbild F11: Batterie wird nicht geladen

**Symptome:** Ladekontrollleuchte leuchtet dauerhaft, Batteriespannung <13V bei laufendem Motor

**Mögliche Ursachen:**
1. Keilriemen locker oder gerissen
2. Lichtmaschinenregler defekt
3. Lichtmaschinen-Kohlen abgenutzt
4. Kabelverbindung Lichtmaschine lose/korrodiert
5. Batterie selbst defekt (Zelle kurzgeschlossen)
6. Sicherung Ladekreis durchgebrannt

### Fehlerbild F12: Abnormale Geräusche

**Symptome:** Klopfen, Klappern, Pfeifen, Kreischen während des Betriebs

**Mögliche Ursachen nach Geräuschtyp:**
- **Klopfen (metallisch):** Pleuel-/Hauptlager verschlissen, Kolbenbolzen, Ventilspiel zu groß
- **Klappern (leicht):** Steuerkette gelängt, Ventiltrieb, Einspritzpumpe
- **Pfeifen:** Turbolader-Lager, Leckage Ansaugsystem, Keilriemen
- **Kreischen:** Keilriemen rutscht, Lager Nebenaggregate
- **Dumpfes Brummen:** Schwingungsdämpfer defekt, Resonanz Auspuffanlage

---

## 18. Troubleshooting-Bäume

### 18.1 Troubleshooting-Baum: Motor startet nicht

```
Motor springt nicht an
├── Anlasser dreht?
│   ├── NEIN
│   │   ├── Batteriespannung >12,2V?
│   │   │   ├── NEIN → Batterie laden/tauschen
│   │   │   └── JA → Startschlüssel/Sicherung prüfen
│   │   │       ├── OK → Anlasser defekt oder Magnetschalter (128170-77010)
│   │   │       └── Defekt → Schalter/Sicherung tauschen
│   └── JA
│       ├── Motor zündet einzeln?
│       │   ├── NEIN
│       │   │   ├── Kraftstoff vorhanden?
│       │   │   │   ├── NEIN → Tanken
│       │   │   │   └── JA → Luft im System?
│       │   │   │       ├── JA → Entlüften (Entlüftungsschraube Filter/Pumpe)
│       │   │   │       └── NEIN → Kraftstofffilter verstopft?
│       │   │   │           ├── JA → Filter tauschen (104500-55710 / 129004-55810)
│       │   │   │           └── NEIN → Glühkerzen prüfen (kalter Motor)
│       │   │   │               ├── Defekt → Glühkerzen tauschen
│       │   │   │               └── OK → Kompression messen
│       │   │   │                   ├── <25 bar → Ventilspiel, Kopfdichtung
│       │   │   │                   └── OK → Einspritzdüsen prüfen
│       │   └── JA → Motor zündet, läuft aber nicht weiter
│       │       ├── Kraftstoffzufuhr intermittierend
│       │       │   → Vorfilter, Tankbelüftung, Dieselschlauch prüfen
│       │       └── ECU-Fehler (nur JH-CR) → Fehlercodes auslesen
```

### 18.2 Troubleshooting-Baum: Überhitzung

```
Temperaturalarm / Überhitzung
├── Kommt Seewasser aus dem Auspuff?
│   ├── NEIN
│   │   ├── Seeventil offen?
│   │   │   ├── NEIN → Seeventil öffnen
│   │   │   └── JA → Seewasserfilter sauber?
│   │   │       ├── NEIN → Filter reinigen
│   │   │       └── JA → Impeller defekt?
│   │   │           ├── JA → Impeller tauschen (128170-02070 / 128990-42200 / 129670-42531)
│   │   │           │   └── Abgebrochene Flügel suchen! (können Wärmetauscher blockieren)
│   │   │           └── NEIN → Seewasserpumpe Wellendichtung prüfen
│   │   │               └── Pumpe überholen
│   └── JA (aber Motor wird trotzdem heiß)
│       ├── Keilriemen intakt?
│       │   ├── NEIN → Keilriemen tauschen (129612-42290)
│       │   └── JA → Kühlmittelstand OK?
│       │       ├── NEIN → Auffüllen, Lecksuche
│       │       └── JA → Thermostat prüfen (aus Gehäuse nehmen, in Topf mit Wasser erwärmen)
│       │           ├── Öffnet nicht bei 71/76 °C → Thermostat tauschen
│       │           └── OK → Wärmetauscher intern verkalkt
│       │               → Wärmetauscher ausbauen, zerlegen, chemisch reinigen
```

### 18.3 Troubleshooting-Baum: Leistungsverlust

```
Motor hat weniger Leistung als normal
├── Schwarzer Rauch?
│   ├── JA → Luftzufuhr prüfen
│   │   ├── Luftfilter verstopft → Reinigen/tauschen
│   │   ├── Ansaugschlauch abgerutscht → Befestigen
│   │   └── Turbolader (nur Turbo-Motoren) → Ladedruck messen
│   │       ├── Zu niedrig → Turbo prüfen (Wastegate, Schaufelrad)
│   │       └── OK → Injektoren prüfen lassen
│   └── NEIN
│       ├── Weißer Rauch?
│       │   ├── JA → Kopfdichtung prüfen (Kühlmittelverlust? Ölemulsion?)
│       │   └── NEIN → Kein Rauch
│       │       ├── Rumpfbewuchs? Propellerbewuchs?
│       │       │   ├── JA → Rumpf reinigen, Propeller säubern
│       │       │   └── NEIN → Kraftstoffzufuhr OK?
│       │       │       ├── NEIN → Filter, Vorfilter, Schläuche prüfen
│       │       │       └── JA → Auspuff-Gegendruck prüfen
│       │       │           ├── Erhöht → Schalldämpfer/Wassersammler prüfen
│       │       │           └── OK → Kompression messen
│       │       │               └── Ungleichmäßig → Ventilspiel, Kopfdichtung, Ringe
```

### 18.4 Troubleshooting-Baum: Seewasser in Bilge

```
Seewasser in der Bilge
├── Motor lief kürzlich?
│   ├── JA
│   │   ├── Impeller-Gehäusedeckel prüfen (tropft?)
│   │   ├── Seewasserpumpe Wellendichtung prüfen
│   │   ├── Alle Schlauchverbindungen Seewasserseite prüfen
│   │   ├── Auspuffmischkammer auf Korrosion prüfen
│   │   └── Wärmetauscher-Endkappen auf Dichtheit prüfen
│   └── NEIN (Motor stand, trotzdem Wasser)
│       ├── Rückschlagventil Auspuff fehlt/defekt?
│       │   └── Seewasser läuft über Auspuff zurück in Motor!
│       │       → KRITISCH: Kann Wasserschlag verursachen
│       ├── Seeventil/Borddurchlass undicht?
│       ├── Saildrive-Manschette prüfen!
│       │   └── Bei Riss: SOFORT Seeventil schließen, Manschette tauschen
│       └── Stevenrohr-Stopfbuchse prüfen (nur Wellenanlage)
```

### 18.5 Troubleshooting-Baum: Common-Rail-Fehlercodes (JH-Serie)

```
Fehlerspeicher auslesen (YD25/YD42 Display oder Diagnose-Tool)
├── E001 (Temp zu hoch)
│   → Siehe Troubleshooting-Baum Überhitzung
├── E002 (Öldruck niedrig)
│   → MOTOR SOFORT AUS! Ölstand, Ölfilter, Ölpumpe prüfen
├── E003 (Drehzahlsensor)
│   → Sensor 129470-77050 prüfen, Kabel, Stecker
├── E004 (Rail-Druck niedrig)
│   ├── Kraftstofffilter verstopft? → Tauschen
│   ├── Kraftstoff-Förderpumpe schwach? → Förderdruck messen (min. 0,3 bar)
│   ├── Hochdruckpumpe verschlissen? → Werkstatt
│   └── Überströmer an Injektoren undicht? → Rücklaufmenge messen
├── E010–E013 (Injektor-Fehler)
│   ├── Kabelverbindung prüfen
│   ├── Injektor-Widerstand messen (Sollwert im Werkstatthandbuch)
│   └── Injektor tauschen (129A00-53001)
└── E008 (Spannung niedrig)
    ├── Batterie prüfen (Ruhespannung >12,6V)
    ├── Lichtmaschine prüfen (Ladespannung 14,0–14,4V)
    └── Keilriemen prüfen
```

---

## 19. Fallstudien

### Fallstudie F-S01: Überhitzung 3YM30 — Abgebrochene Impeller-Flügel

**Ausgangslage:** Segelyacht 11 m (Bavaria Cruiser 34), Motor Yanmar 3YM30 mit SD25 Saildrive, 1.200 Betriebsstunden. Eigner bemerkt Temperaturanstieg auf 98 °C (normal: 82 °C) nach 20 Minuten Motorbetrieb.

**Diagnose:**
1. Seewasser-Auslass am Auspuff: Wassermenge stark reduziert
2. Seewasserfilter: sauber
3. Seeventil: offen
4. Impeller ausgebaut: 3 von 8 Flügeln abgebrochen
5. Flügel im Wärmetauscher gefunden: 2 Stück blockierten Seewasserseite teilweise

**Ursache:** Impeller war 3 Jahre alt, Boot wurde über Winter nicht genutzt, Impeller-Flügel hatten durch langes Stehen eine Verformung ("Set") entwickelt und brachen beim Saisonstart ab.

**Lösung:**
- Neuer Impeller (128990-42200): 42 EUR
- Wärmetauscher zerlegt und gereinigt: 2h Arbeitszeit
- Zinkanode (119574-44150) gleich mitgetauscht: 16 EUR
- Gesamtkosten: ca. 180 EUR (inkl. Arbeitszeit)

**Lehre:** Impeller jährlich tauschen, auch bei wenig Betriebsstunden. Bei Winterlager: Impeller ausbauen und separat lagern.

### Fallstudie F-S02: Dieselpest im 4JH45

**Ausgangslage:** Segelyacht 13 m (Hanse 418), Motor Yanmar 4JH45 mit SD50, 800 Betriebsstunden. Motor startet schwer, läuft unrund, hat Leistungsverlust. Kraftstoff im Vorfilter trüb mit schwarzen Flocken.

**Diagnose:**
1. Kraftstoff-Vorfilter: schwarze Flocken (Biomasse), Wasser am Boden
2. Tankinspektion: Biofilm an Tankwänden, starke Kontamination
3. Kraftstofffilter primär und sekundär: verstopft
4. Common-Rail-System: Fehlercodes E004 (Raildruck niedrig) gespeichert

**Ursache:** Diesel-Pest (Hormoconis resinae und andere Mikroorganismen). Boot lag 8 Monate mit halbvollem Tank (Kondenswasser). Keine Biozid-Behandlung.

**Lösung:**
1. Tank komplett entleert und professionell gereinigt: 650 EUR
2. Neuer Kraftstoff mit Biozid (Grotamar 82): 15 EUR/100L
3. Kraftstofffilter primär (129004-55810): 22 EUR
4. Kraftstofffilter sekundär (129A00-55800): 28 EUR
5. Kraftstoffsystem entlüftet
6. Fehlerspeicher gelöscht
7. Probelauf: Motor läuft wieder einwandfrei
8. Gesamtkosten: ca. 1.200 EUR (inkl. Arbeitszeit, Kraftstoff)

**Lehre:** Tank immer voll halten bei Langzeitlagerung. Biozid verwenden. Wasserabscheider-Vorfilter (z. B. Racor 500FG) installieren.

### Fallstudie F-S03: Saildrive-Manschette SD20 — Beinahe-Untergang

**Ausgangslage:** Segelyacht 9 m, Motor Yanmar 2YM20 mit SD20 Saildrive, 9 Jahre alt. Eigner bemerkt beim Saisonstart ungewöhnlich viel Wasser in der Bilge.

**Diagnose:**
1. Bilge zeigt Seewassereintritt
2. Saildrive-Manschette zeigt Querriss auf der Innenseite (visuell von außen nicht erkennbar!)
3. Manschette verhärtet, Shore-Härte deutlich über Neuwert

**Ursache:** Manschette war 9 Jahre alt (empfohlenes Wechselintervall: 7 Jahre). UV-Strahlung und Alterung führten zu Materialversprödung.

**Lösung:**
1. Boot geslippt
2. Saildrive demontiert
3. Neue Manschette (196420-01950): 320 EUR
4. Neue Zinkanode (196420-02652): 38 EUR
5. Getriebeöl gewechselt: 20 EUR
6. Gesamtkosten: ca. 650 EUR (inkl. Slipkosten und Arbeitszeit)

**Lehre:** Saildrive-Manschette ist sicherheitskritisch! Nach 7 Jahren zwingend tauschen. Jährlich prüfen, auch von innen (Boot auf dem Trailer oder Kran). Ein Riss kann zum Sinken führen.

### Fallstudie F-S04: ECU-Ausfall 4JH57 durch Feuchtigkeit

**Ausgangslage:** Segelyacht 14 m (Contest 42CS), Motor Yanmar 4JH57 mit SD60, 2.400 Betriebsstunden. Motor startet nach Regenperiode nicht mehr, kein Lebenszeichen von Instrumentierung.

**Diagnose:**
1. Batteriespannung OK (12,8V)
2. Hauptsicherungen OK
3. ECU-Gehäuse geöffnet: Kondenswasser auf Platine, Korrosionsspuren
4. ECU-Stecker oxidiert

**Ursache:** Motorraum-Belüftung bei Nichtbenutzung geschlossen gehalten, Kondensat bildete sich auf der ECU. Über Monate sammelte sich Feuchtigkeit.

**Lösung:**
1. ECU getrocknet und gereinigt (Kontaktspray, Isopropanol)
2. Steckerkontakte mit Kontaktfett behandelt
3. ECU-Gehäuse zusätzlich abgedichtet
4. Motorraum-Belüftung modifiziert (permanent leicht offen)
5. Silicagel-Beutel in ECU-Nähe platziert
6. Gesamtkosten: ca. 250 EUR
7. Hinweis: Wenn ECU irreparabel beschädigt → Ersatz ca. 2.800–3.500 EUR

**Lehre:** Motorraum immer belüften, auch bei Nichtbenutzung. ECU-Bereich trocken halten. Bei Langzeitlagerung: Silicagel verwenden.

### Fallstudie F-S05: Turbolader-Schaden 4JH80

**Ausgangslage:** Segelyacht 16 m (Hallberg-Rassy 50), Motor Yanmar 4JH80 mit KMH61A-Getriebe, 3.800 Betriebsstunden. Eigner bemerkt blauen Rauch beim Beschleunigen und erhöhten Ölverbrauch (0,3 L/100h statt normal <0,05 L/100h).

**Diagnose:**
1. Blauer Rauch: Öl wird verbrannt
2. Ansaugrohr nach Turbolader: Ölfilm sichtbar
3. Turbolader-Axialspiel: 0,12 mm (max. zulässig: 0,08 mm)
4. Turbo-Dichtungen undicht → Öl gelangt in Ladeluft

**Ursache:** Eigner fuhr regelmäßig Vollgas und schaltete Motor sofort ab ohne Abkühlphase. Thermischer Stress auf Turbolager.

**Lösung:**
1. Turbolader-Revision (Austausch-Turbo): 1.800 EUR
2. Ladeluftrohr gereinigt: 80 EUR
3. Ölwechsel mit neuem Filter: 120 EUR
4. Probelauf und Einjustierung: 200 EUR
5. Gesamtkosten: ca. 2.500 EUR

**Lehre:** Turbo-Motoren immer 2–3 Minuten im Leerlauf abkühlen lassen vor dem Abstellen. Mindestens 5 Minuten warmfahren vor Volllast.

### Fallstudie F-S06: Einspritzleitungen korrodiert — 3GM30

**Ausgangslage:** Segelyacht 10 m, Motor Yanmar 3GM30, 22 Jahre alt, 4.500 Betriebsstunden. Eigner riecht Diesel im Motorraum. Keine sichtbare Tropfstelle bei flüchtiger Besuche.

**Diagnose:**
1. Bei laufendem Motor unter Last: feiner Diesel-Nebel an Einspritzleitung Zylinder 2
2. Haarfeiner Riss in Hochdruckleitung (Ermüdungsbruch nach 22 Jahren Vibration)

**Ursache:** Alter und Vibration. Einspritzleitungen aus Stahl korrodieren und ermüden über Jahrzehnte.

**Lösung:**
1. Alle drei Einspritzleitungen prophylaktisch getauscht (104200-59111): 3 × 85 EUR
2. Kraftstoffrücklaufleitungen ebenfalls erneuert: 95 EUR
3. Gesamtkosten: ca. 480 EUR

**Lehre:** Bei Motoren >15 Jahre alle Kraftstoffleitungen inspizieren. Diesel auf heißem Auspuff = Brandgefahr! Sofort handeln.

### Fallstudie F-S07: Getriebefluchtung verloren — 4JH45

**Ausgangslage:** Segelyacht 13 m, Motor Yanmar 4JH45 mit KMH4A-Getriebe und Wellenanlage, 2.800 Betriebsstunden. Zunehmende Vibrationen bei Motorfahrt, besonders zwischen 1.800 und 2.200 U/min.

**Diagnose:**
1. Motorlager geprüft: vorderes Steuerbord-Lager durchgesackt
2. Fluchtungsmessung Welle-Getriebe: 0,18 mm (max. zulässig: 0,05 mm)
3. Propellerwelle: leichter Schlag nach Grundberührung 6 Monate zuvor

**Lösung:**
1. Alle 4 Motorlager getauscht (129470-08340): 4 × 52 EUR
2. Motor-Getriebe-Welle neu ausgerichtet: 3h Arbeitszeit
3. Propellerwelle richten lassen: 280 EUR
4. Gesamtkosten: ca. 850 EUR

**Lehre:** Nach Grundberührung immer Wellenfluchtung prüfen lassen. Motorlager alle 2.000–3.000h kontrollieren.

### Fallstudie F-S08: Langzeitlagerung — Motor nach 3 Jahren Standzeit

**Ausgangslage:** Segelyacht 10 m, Motor Yanmar 2YM20, 600 Betriebsstunden. Boot lag 3 Jahre ungenutzt am Steg. Eigner möchte wieder in Betrieb nehmen.

**Durchgeführte Arbeiten:**
1. Motoröl und Filter gewechselt (Öl war dunkel, aber keine Emulsion): 60 EUR
2. Kraftstoff komplett abgelassen (alte Diesel-Qualität nicht mehr nutzbar): 40 EUR
3. Tank gereinigt, neuer Kraftstoff mit Biozid: 180 EUR
4. Kraftstofffilter getauscht (104500-55710): 18 EUR
5. Impeller getauscht (128990-42200, Flügel waren verformt): 42 EUR
6. Kühlmittel gewechselt: 35 EUR
7. Zinkanode getauscht (119574-44150, war zu 80 % aufgelöst): 16 EUR
8. Keilriemen getauscht (119773-42680, war rissig): 20 EUR
9. Batterie war tiefentladen → neue Batterie: 180 EUR
10. Auspuffschlauch geprüft (noch OK)
11. Saildrive SD20 Getriebeöl gewechselt: 25 EUR
12. Saildrive-Manschette geprüft (noch OK, 5 Jahre alt → nächstes Winterlager tauschen)
13. Motor gestartet, entlüftet, 2h Probelauf
14. Gesamtkosten: ca. 750 EUR (inkl. Arbeitszeit)

**Lehre:** Langzeitlagerung >1 Jahr erfordert gründliche Inbetriebnahme-Inspektion. Idealerweise Motor vor der Einlagerung konservieren (Öl einfüllen, Sprühöl in Ansaug, Tank voll, Kühlsystem mit Frostschutz).

---

## 20. FAQ

### 20.1 Allgemeine Fragen

**F01: Welcher Yanmar-Motor passt zu meinem Segelboot?**
Faustregel: 3–4 PS pro Tonne Verdrängung für Segelboote. Beispiel: 8-Tonnen-Segelboot → 24–32 PS → Yanmar 3YM30 (29 PS) oder 3JH40 (39 PS). Die größere Maschine bietet mehr Reserve bei Gegenwind/Strom und läuft bei Reisefahrt in einem günstigeren Drehzahlbereich.

**F02: Was ist der Unterschied zwischen 2YM20 und 3YM20?**
Gleiche Leistung (21 PS), aber der 3YM20 erreicht sie bei 2.900 statt 3.400 U/min. Der Dreizylinder ist ruhiger, verbraucht etwas weniger, wiegt aber 16 kg mehr und kostet ca. 1.500 EUR mehr. Für Langfahrt ist der 3YM20 die bessere Wahl.

**F03: Wie lange hält ein Yanmar-Dieselmotor?**
Bei korrekter Wartung sind 8.000–12.000 Betriebsstunden realistisch (GM/YM-Serie). Die JH-Serie mit Common Rail erreicht bei guter Pflege ähnliche Werte. Viele GM-Motoren laufen nach 30+ Jahren noch einwandfrei. Entscheidend ist regelmäßiger Ölwechsel, korrekter Impeller-Tausch und sauberer Kraftstoff.

**F04: Brauche ich eine Saildrive oder Wellenanlage?**
Saildrive: Einfacherer Einbau, weniger Wartung an Stopfbuchse, oft leiser. Aber: Manschette ist Verschleißteil, Propellerauswahl eingeschränkt, teurer als einfache Wellenanlage. Bei Neubauten und Produktionsbooten ist Saildrive Standard. Bei Refit-Projekten und Langfahrt bevorzugen manche Eigner die Wellenanlage wegen der Einfachheit.

**F05: Was kostet ein Ölwechsel beim Yanmar?**
Material (Öl + Filter): 35–60 EUR (YM-Serie) bis 80–120 EUR (JH-Serie). In der Werft mit Arbeitszeit: 120–200 EUR. Selbst gemacht: Material + 1h Zeit.

**F06: Welches Öl verwende ich für meinen Yanmar?**
Standard: 15W-40, API CF (GM), CF-4 (YM), CI-4 (JH/LHA/LY). Synthetik ist bei JH/LHA/LY empfohlen, bei GM/YM optional. Kein Leichtlauf-Öl (5W-30 etc.) verwenden — die Spaltmaße der Motoren sind für dickflüssigeres Öl ausgelegt.

**F07: Wie entlüfte ich das Kraftstoffsystem?**
GM/YM (mechanische Einspritzung): Entlüftungsschraube am Kraftstofffilter öffnen, Handpumpe (am Filter oder Einspritzpumpe) betätigen bis blasenfreier Diesel austritt, Schraube schließen. JH (Common Rail): Primärfilter-Entlüftung manuell, Rest erfolgt automatisch durch die Hochdruckpumpe beim Starten (max. 30 Sekunden Anlasser).

**F08: Wann muss die Saildrive-Manschette getauscht werden?**
Spätestens nach 7 Jahren. Jährlich visuell prüfen (Risse, Verhärtung, Verformung). Alle 3 Jahre von beiden Seiten inspizieren (Boot aus dem Wasser). Bei Beschädigung oder Unsicherheit sofort tauschen — eine undichte Manschette kann zum Sinken führen.

**F09: Wie laut ist ein Yanmar-Diesel?**
Typische Werte bei 1 m Abstand: 1YM15 ca. 72 dB(A), 3YM30 ca. 75 dB(A), 4JH57 ca. 78 dB(A), 4JH110 ca. 82 dB(A). Mit Schalldämmung (25–50 mm) ca. 5–10 dB leiser.

**F10: Kann ich meinen GM-Motor durch einen YM ersetzen?**
Ja, Yanmar hat die YM-Serie als Nachrüstlösung für GM konzipiert. Die Befestigungspunkte sind kompatibel. Der Saildrive SD20 passt für beide Serien. Achtung: Kabelbaum und Instrumentierung sind unterschiedlich.

### 20.2 Technische Fragen

**F11: Was bedeutet Common Rail und warum ist es besser?**
Common Rail (CR) bedeutet, dass alle Injektoren über eine gemeinsame Hochdruckleitung ("Rail") mit Kraftstoff versorgt werden. Der Einspritzdruck (bis 2.000 bar bei JH) wird unabhängig von der Drehzahl aufgebaut. Vorteile: Bessere Verbrennung, weniger Emissionen, leiserer Betrieb, geringerer Verbrauch. Nachteil: Komplexere Technik, höhere Reparaturkosten.

**F12: Wie messe ich den Öldruck korrekt?**
Mechanisches Manometer am Öldruckschalter-Anschluss. Sollwerte: GM/YM: >1,5 bar bei Nenndrehzahl, >0,7 bar im Leerlauf. JH: >2,5 bar bei Nenndrehzahl, >1,0 bar im Leerlauf. Unter diesen Werten: Motor abstellen und Ursache suchen.

**F13: Welchen Propeller brauche ich?**
Abhängig von Motor, Getriebe-Untersetzung, Bootstyp und gewünschter Geschwindigkeit. Faustregel Segelboot: 2-Blatt-Faltpropeller für Regatta, 3-Blatt-Faltpropeller für Fahrtensegler. Durchmesser und Steigung vom Propellerhersteller berechnen lassen (Daten: Motorleistung, Nenndrehzahl, Untersetzung, Rumpfgeschwindigkeit, Verdrängung).

**F14: Warum raucht mein Motor beim Kaltstart?**
Weißer Rauch beim Kaltstart ist bei Dieselmotoren normal (besonders bei Temperaturen <10 °C). Der Kraftstoff verbrennt nicht vollständig. Sollte nach 2–5 Minuten Warmlaufen aufhören. Bei anhaltendem Rauch: Glühkerzen, Kompression und Einspritzung prüfen.

**F15: Wie konserviere ich den Motor für die Winterpause?**
1. Motor warmfahren (Betriebstemperatur), 2. Ölwechsel mit Filter (warmem Öl), 3. Kühlsystem: Frostschutzmischung prüfen (min. -20 °C), 4. Impeller ausbauen (oder Saison-Impeller einsetzen), 5. Kraftstofftank volltanken + Biozid, 6. Kraftstoffhahn schließen, Motor laufen lassen bis er von selbst ausgeht (Leitungen leer), 7. Sprühöl in Ansaugöffnung (WD-40 oder Yanmar Fogging Oil), 8. Motor durchdrehen (Startknopf ohne Zündung, 5 Sekunden), 9. Batterie abklemmen oder Erhaltungsladegerät anschließen.

**F16: Was ist der Unterschied zwischen Zink- und Magnesiumanoden?**
Zinkanoden: Standard für Salzwasser. Magnesiumanoden: Für Süßwasser (niedrigere Leitfähigkeit). Aluminiumanoden: Funktionieren in Salz- und Brackwasser. Yanmar liefert serienmäßig Zinkanoden. Im Süßwasser (Binnenseen, Bodensee) auf Magnesium umrüsten.

**F17: Wie kann ich die Lichtmaschinenleistung erhöhen?**
GM-Serie (35A): Nachrüstung auf 80A-Lichtmaschine möglich (Balmar, Mastervolt). Erfordert neuen Halter und ggf. breiteren Keilriemen. YM-Serie (80A): Ausreichend für normale Ausstattung. JH-Serie (125A): Für umfangreiche Elektronik meist ausreichend. Bei Bedarf auf 200A nachrüsten (z. B. Mastervolt Alpha Pro III).

**F18: Kann ich AdBlue/SCR bei meinem Yanmar nachrüsten?**
Nein, aktuelle Yanmar-Marinediesel (bis 115 PS) erfüllen die Abgasnormen ohne SCR. Erst ab den größeren Industrie-/Schiffsmotoren (>560 kW) wird SCR eingesetzt. Die JH/LHA/LY-Serie erreicht IMO Tier II durch interne Motoroptimierung (Common Rail, angepasste Verbrennung).

**F19: Welche Batterie brauche ich für meinen Yanmar?**
Starterbatterie: GM/YM: min. 50 Ah, CCA >400A. JH: min. 70 Ah, CCA >600A. LHA/LY: min. 100 Ah, CCA >800A. AGM oder Nass-Blei. Lithium-Starterbatterien sind möglich, aber Lichtmaschinenregler muss kompatibel sein (Ladeschlussspannung 14,4V für Blei vs. 14,6V für LiFePO4).

**F20: Wie prüfe ich die Kompression meines Motors?**
Kompressionstest: Alle Glühkerzen/Injektoren ausbauen, Kompressionsmessgerät einschrauben, Gashebel auf Vollgas, Motor mit Anlasser durchdrehen (5–8 Umdrehungen pro Zylinder). Sollwerte: GM: 25–30 bar, YM: 27–32 bar, JH: 28–35 bar. Maximale Abweichung zwischen Zylindern: 3 bar.

**F21: Was ist ein Wasserschlag und wie vermeide ich ihn?**
Wasserschlag (Hydrolock): Wasser im Brennraum kann nicht komprimiert werden → Kolben/Pleuel verbiegt → Motorschaden. Ursachen: Seewasser läuft über Auspuff zurück (fehlendes Rückschlagventil, Schwanenhals zu niedrig). Prävention: Auspuff-Schwanenhals min. 300 mm über Wasserlinie, Rückschlagventil installieren, Seeventil bei Nichtbenutzung schließen.

**F22: Wie oft muss ich das Ventilspiel einstellen?**
GM-Serie: Alle 250h prüfen. YM-Serie: Alle 250h prüfen. JH-Serie: Alle 1.000h prüfen. Sollwerte (kalt): GM/YM: Einlass 0,15 mm, Auslass 0,15 mm. JH: Einlass 0,20 mm, Auslass 0,20 mm.

**F23: Kann ich Biodiesel (B7, B20) in meinem Yanmar verwenden?**
B7 (7 % Bioanteil): Ja, von Yanmar freigegeben für alle aktuellen Modelle. B20 oder höher: Nicht empfohlen. Biodiesel ist hygroskopisch (zieht Wasser an), begünstigt Dieselpest und kann Dichtungen angreifen. In der Praxis: Normaler Diesel von der Tankstelle (EN 590) ist B7 und unproblematisch.

**F24: Was kostet eine Generalüberholung?**
Richtwerte: GM-Serie: 2.500–4.000 EUR (Kolben, Ringe, Lager, Dichtungen, Düsen). YM-Serie: 3.000–5.000 EUR. JH-Serie: 5.000–10.000 EUR (inkl. Injektoren, Turbo-Revision bei 4JH80/110). Der Zeitwert eines gebrauchten Motors liegt oft unter den Überholungskosten — Kosten-Nutzen-Analyse empfohlen.

**F25: Gibt es einen Unterschied zwischen Yanmar-Original und Aftermarket-Impellern?**
Yanmar-Original: Garantierte Passform, NBR-Gummi, oft etwas teurer. Aftermarket (Jabsco, Johnson, CEF, Sherwood): 30–50 % günstiger, Passform bei Markenherstellern gleichwertig. Wichtig: Keine billigen No-Name-Impeller verwenden — Material und Maßhaltigkeit sind kritisch. Empfehlung: Yanmar-Original oder Jabsco/Johnson.

---

## 21. Glossar

| Nr. | Begriff (DE) | Begriff (EN) | Erklärung |
|-----|-------------|-------------|-----------|
| G01 | Anlasser | Starter Motor | Elektromotor zum Starten des Dieselmotors (12V oder 24V) |
| G02 | Auspuffmischkammer | Exhaust Mixing Elbow | Bauteil, in dem Abgase mit Kühlwasser vermischt werden (Nassauspuff) |
| G03 | Biozid | Biocide | Chemischer Zusatz gegen Mikroorganismen im Dieseltank (z. B. Grotamar 82) |
| G04 | Bohrung | Bore | Innendurchmesser des Zylinders in mm |
| G05 | Common Rail | Common Rail | Hochdruck-Einspritzsystem mit gemeinsamer Druckleitung für alle Injektoren |
| G06 | Dieselpest | Diesel Bug | Mikrobieller Befall des Dieselkraftstoffs durch Pilze/Bakterien |
| G07 | Drehmoment | Torque | Drehkraft des Motors, gemessen in Nm oder kgm |
| G08 | ECU | ECU | Electronic Control Unit — Motorsteuergerät (bei Common-Rail-Motoren) |
| G09 | Einspritzpumpe | Injection Pump | Mechanische Pumpe zur Kraftstoff-Hochdruckerzeugung (GM/YM-Serie) |
| G10 | Faltpropeller | Folding Propeller | Propeller mit klappbaren Blättern, minimaler Widerstand unter Segel |
| G11 | Förderpumpe | Lift Pump / Feed Pump | Niederdruckpumpe, die Kraftstoff vom Tank zum Filter/Motor fördert |
| G12 | Glühkerze | Glow Plug | Elektrisches Heizelement in der Vorkammer für Kaltstart-Unterstützung |
| G13 | Hub | Stroke | Kolbenweg im Zylinder von OT (oben) nach UT (unten) in mm |
| G14 | Hubraum | Displacement | Gesamtvolumen aller Zylinder in cm³ oder Liter |
| G15 | Impeller | Impeller | Flexibles Gummi-Flügelrad in der Seewasserpumpe |
| G16 | Injektor | Injector | Einspritzdüse im Common-Rail-System, elektronisch gesteuert |
| G17 | Keilriemen | V-Belt | Antriebsriemen für Lichtmaschine und ggf. Süßwasserpumpe |
| G18 | Kompression | Compression | Verdichtungsdruck im Zylinder, Maß für Motorzustand (in bar) |
| G19 | Kühlmittel | Coolant | Frostschutz-Wasser-Gemisch im geschlossenen Kühlkreislauf |
| G20 | Ladeluftkühlung | Intercooling | Kühlung der verdichteten Luft nach dem Turbolader → mehr Sauerstoff → mehr Leistung |
| G21 | Lichtmaschine | Alternator | Generator zur Stromerzeugung während des Motorbetriebs |
| G22 | Motorlager | Engine Mount | Gummielastische Lager zur Aufnahme und Entkopplung des Motors |
| G23 | Nassauspuff | Wet Exhaust | Auspuffsystem, bei dem Kühlwasser mit den Abgasen vermischt wird |
| G24 | Opferanode | Sacrificial Anode | Zink-/Magnesium-/Aluminiumanode zum Schutz vor galvanischer Korrosion |
| G25 | PSS-Dichtung | PSS Shaft Seal | Packless Sealing System — tropffreie Wellendichtung (Alternative zur Stopfbuchse) |
| G26 | Saildrive | Saildrive | Integriertes Antriebsaggregat mit vertikaler Welle durch den Rumpf |
| G27 | Schwanenhals | Gooseneck (Exhaust) | U-förmige Biegung im Auspuff, verhindert Wassereintritt |
| G28 | Seewasserfilter | Raw Water Strainer | Filter am Seeventil-Einlass, fängt Schmutz/Seegras ab |
| G29 | Spez. Verbrauch | Specific Fuel Consumption | Kraftstoffverbrauch pro Leistungseinheit: g/kWh |
| G30 | Stopfbuchse | Stuffing Box / Packing Gland | Dichtung um die Propellerwelle am Rumpfdurchtritt |
| G31 | Süßwasserkühlung | Freshwater Cooling | Geschlossener Kreislauf mit Frostschutz, gekühlt durch Seewasser-Wärmetauscher |
| G32 | Thermostat | Thermostat | Temperaturgesteuertes Ventil zur Regelung der Kühlmitteltemperatur |
| G33 | Turbolader | Turbocharger | Abgasgetriebener Verdichter zur Leistungssteigerung |
| G34 | Untersetzung | Gear Ratio / Reduction | Übersetzungsverhältnis Motor→Propeller (z. B. 1:2,36 = Propeller dreht 2,36× langsamer als Motor) |
| G35 | Ventilspiel | Valve Clearance | Spalt zwischen Kipphebel und Ventil im kalten Zustand (in mm) |
| G36 | Verdichtungsverhältnis | Compression Ratio | Verhältnis Gesamtvolumen / Brennraumvolumen (z. B. 21:1) |
| G37 | Vorkammer | Pre-Chamber | Nebenkammer im Zylinderkopf für indirekte Einspritzung (GM/YM) |
| G38 | Wärmetauscher | Heat Exchanger | Bauteil zum Wärmetausch zwischen Süßwasser und Seewasser |
| G39 | Wasserschlag | Hydrolock / Water Hammer | Motorschaden durch Wasser im Brennraum (nicht komprimierbar) |
| G40 | Wendegetriebe | Marine Gear / Transmission | Getriebe mit Vorwärts-/Rückwärtsgang und Untersetzung |
| G41 | Zinkanode | Zinc Anode | Opferanode aus Zink zum kathodischen Korrosionsschutz in Salzwasser |
| G42 | CAN-Bus | CAN Bus | Controller Area Network — digitales Bussystem zur Motorsteuerung |
| G43 | DTC | DTC | Diagnostic Trouble Code — Fehlercode im Motorsteuergerät |
| G44 | NMEA 2000 | NMEA 2000 | Netzwerkprotokoll für maritime Elektronik (Instrumente, Sensoren) |
| G45 | OT / UT | TDC / BDC | Oberer Totpunkt / Unterer Totpunkt des Kolbens |
| G46 | Wastegate | Wastegate | Bypassventil am Turbolader zur Ladedruckbegrenzung |
| G47 | Wellendichtring | Shaft Seal / Oil Seal | Dichtring an rotierenden Wellen (Seewasserpumpe, Getriebe) |
| G48 | Betriebsstunden | Engine Hours | Zähler der Motorlaufzeit, Basis für Wartungsintervalle |

---

## 22. Pydantic v2 Datenmodelle

### 22.1 Yanmar Motor-Datenmodell

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal
from enum import Enum


class MotorSerie(str, Enum):
    GM = "GM"
    YM = "YM"
    JH = "JH"
    LHA = "LHA"
    LY = "LY"
    LPA = "LPA"
    BY = "BY"


class Einspritzung(str, Enum):
    IDI = "indirekt"         # Indirekte Einspritzung (Vorkammer)
    CR = "common_rail"       # Common Rail


class Kuehlung(str, Enum):
    DIREKT = "seewasser_direkt"
    INDIREKT = "suesswasser_waermetauscher"


class AufladungTyp(str, Enum):
    SAUGMOTOR = "saugmotor"
    TURBO = "turbo"
    TURBO_LLK = "turbo_ladeluftkuehlung"
    TWIN_TURBO = "twin_turbo"


class YanmarMotor(BaseModel):
    model_config = {"from_attributes": True}

    modell: str = Field(..., description="Modellbezeichnung z.B. '4JH57'")
    serie: MotorSerie
    zylinder: int = Field(..., ge=1, le=8)
    bauform: Literal["reihe", "v"] = "reihe"
    hubraum_cm3: int = Field(..., description="Hubraum in cm³")
    bohrung_mm: float
    hub_mm: float
    leistung_ps: float = Field(..., description="Nennleistung in PS")
    leistung_kw: float = Field(..., description="Nennleistung in kW")
    nenndrehzahl: int = Field(..., description="Nenndrehzahl in U/min")
    max_drehmoment_kgm: float
    drehmoment_drehzahl: int = Field(..., description="Drehzahl bei max. Drehmoment")
    verdichtungsverhaeltnis: float
    einspritzung: Einspritzung
    einspritzdruck_bar: Optional[int] = None
    aufladung: AufladungTyp = AufladungTyp.SAUGMOTOR
    kuehlung: Kuehlung
    startanlage_volt: int = 12
    anlasser_kw: float
    lichtmaschine_ampere: int
    kraftstoffverbrauch_volllast_lh: float
    kraftstoffverbrauch_reise_lh: Optional[float] = None
    spez_verbrauch_gkwh: float
    oelmenge_liter: float
    oelfilter_teilenr: str
    kraftstofffilter_primaer_teilenr: str
    kraftstofffilter_sekundaer_teilenr: Optional[str] = None
    luftfilter_teilenr: str
    gewicht_trocken_kg: int
    laenge_mm: int
    breite_mm: int
    hoehe_mm: int
    saildrive_kompatibel: list[str] = Field(default_factory=list)
    getriebe_kompatibel: list[str] = Field(default_factory=list)
    preis_motor_solo_eur: tuple[int, int] = Field(
        ..., description="Preisbereich (min, max) EUR"
    )
    einsatz_bootlaenge_m: tuple[float, float] = Field(
        ..., description="Empfohlene Bootslänge (min, max) m"
    )


class SaildriveModell(BaseModel):
    model_config = {"from_attributes": True}

    modell: str = Field(..., description="z.B. 'SD60'")
    max_motorleistung_ps: int
    max_drehmoment_kgm: float
    untersetzungen: list[str]
    propellerschaft_mm: int
    max_propeller_zoll: int
    gewicht_kg: float
    manschette_teilenr: str
    manschette_wechsel_jahre: int = 7
    zinkanode_teilenr: str
    getriebeoel_menge_liter: float
    preis_komplett_eur: tuple[int, int]


class WartungsIntervall(BaseModel):
    model_config = {"from_attributes": True}

    intervall_stunden: int
    arbeiten: list[str]
    ersatzteile: list[dict[str, str]] = Field(
        default_factory=list,
        description="Liste von {teilenr, bezeichnung, preis_eur}"
    )
    geschaetzte_dauer_minuten: Optional[int] = None
    schwierigkeitsgrad: Literal["eigner", "mechaniker", "werkstatt"] = "eigner"


class Fehlerbild(BaseModel):
    model_config = {"from_attributes": True}

    code: str = Field(..., description="z.B. 'F01'")
    titel: str
    symptome: list[str]
    ursachen: list[str]
    diagnose_schritte: list[str]
    schwere: Literal["KRITISCH", "HOCH", "MITTEL", "NIEDRIG"]
    sofortmassnahme: Optional[str] = None


class Schwachstelle(BaseModel):
    model_config = {"from_attributes": True}

    modelle: list[str] = Field(..., description="Betroffene Modelle")
    beschreibung: str
    symptom: str
    loesung: str
    teilenummer: Optional[str] = None
    preis_eur: Optional[tuple[int, int]] = None
    betriebsstunden_ab: Optional[int] = None


class DTC_Fehlercode(BaseModel):
    model_config = {"from_attributes": True}

    code: str = Field(..., description="z.B. 'E001'")
    beschreibung: str
    schwere: Literal["KRITISCH", "HOCH", "MITTEL", "NIEDRIG"]
    massnahme: str
    betroffene_serien: list[MotorSerie] = Field(
        default_factory=lambda: [MotorSerie.JH]
    )


class YanmarWissensbank(BaseModel):
    model_config = {"from_attributes": True}

    motoren: list[YanmarMotor]
    saildrives: list[SaildriveModell]
    wartungsplaene: dict[str, list[WartungsIntervall]] = Field(
        ..., description="Key = Modell-Serie (z.B. 'GM', 'YM', 'JH')"
    )
    fehlerbilder: list[Fehlerbild]
    schwachstellen: list[Schwachstelle]
    fehlercodes: list[DTC_Fehlercode]
```

### 22.2 AYDI-Integration — Motor-Analyse-Ergebnis

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal


class MotorAnalyseErgebnis(BaseModel):
    model_config = {"from_attributes": True}

    motor_modell: str
    motor_serie: str
    betriebsstunden: Optional[int] = None
    baujahr: Optional[int] = None

    # Zustandsbewertung
    zustand_score: float = Field(..., ge=0, le=100)
    zustand_kategorie: Literal[
        "ausgezeichnet",  # 90-100
        "gut",            # 75-89
        "akzeptabel",     # 60-74
        "mangelhaft",     # 40-59
        "kritisch"        # 0-39
    ]

    # Confidence
    confidence: Literal[
        "measured",
        "calculated",
        "visual_high",
        "visual_medium",
        "visual_low",
        "visual_insufficient",
        "estimated",
        "documented"
    ]

    # Befunde
    befunde: list[dict] = Field(
        default_factory=list,
        description="Liste von Befunden mit {titel, beschreibung, schwere, empfehlung, teilenr}"
    )

    # Wartungsstatus
    naechste_wartung_h: Optional[int] = None
    ueberfaellige_wartungen: list[str] = Field(default_factory=list)

    # Kostenprognose
    geschaetzte_wartungskosten_12m_eur: Optional[tuple[int, int]] = None
    geschaetzte_reparaturkosten_eur: Optional[tuple[int, int]] = None

    # Schwachstellen-Abgleich
    relevante_schwachstellen: list[str] = Field(
        default_factory=list,
        description="IDs der zutreffenden Schwachstellen"
    )
```

---

## 23. Preisübersicht EUR

### 23.1 Motorpreise (UVP 2025/26, inkl. Getriebe/Saildrive)

| Modell | Motor solo | Mit Getriebe | Mit Saildrive | Saildrive-Typ |
|--------|-----------|-------------|--------------|--------------|
| 1GM10 | 4.200–4.800 | 5.100–5.600 | 6.800–7.400 | SD20 |
| 2GM20 | 6.200–6.800 | 7.400–8.100 | 8.900–9.600 | SD20 |
| 3GM30 | 7.800–8.500 | 9.200–10.000 | 10.800–11.600 | SD20 |
| 1YM15 | 5.800–6.400 | 6.900–7.500 | 8.200–8.900 | SD20 |
| 2YM15 | 7.200–7.800 | 8.500–9.200 | 9.800–10.600 | SD20 |
| 2YM20 | 7.800–8.400 | 9.200–9.900 | 10.500–11.300 | SD20 |
| 3YM20 | 9.400–10.100 | 11.000–11.800 | 12.400–13.200 | SD20 |
| 3YM30 | 10.200–10.900 | 11.800–12.600 | 13.500–14.400 | SD25 |
| 3JH40 | 14.500–15.800 | 17.200–18.600 | 19.800–21.400 | SD50 |
| 4JH45 | 17.800–19.200 | 20.500–22.100 | 23.200–25.000 | SD50 |
| 4JH57 | 20.200–21.800 | 23.500–25.200 | 27.500–29.500 | SD60 |
| 4JH80 | 24.500–26.200 | 28.200–30.400 | 32.500–35.000 | SD60 |
| 4JH110 | 29.800–32.000 | 34.500–37.200 | 38.500–41.500 | SD60 |
| 4LHA-STP | 38.000–42.000 | 44.000–48.500 | — | — |
| 4LHA-DTP | 44.000–48.000 | 52.000–57.000 | — | — |
| 6LPA-STP2 | 52.000–57.000 | 62.000–68.000 | — | — |
| 6LY-STP | 62.000–68.000 | 74.000–82.000 | — | — |
| 6LY-UTP | 72.000–78.000 | 86.000–94.000 | — | — |
| 8BY-220Z | 85.000–92.000 | 100.000–110.000 | — | — |
| 8BY-260Z | 95.000–105.000 | 112.000–124.000 | — | — |

### 23.2 Ersatzteilpreise (Zusammenfassung, EUR)

| Ersatzteil | GM-Serie | YM-Serie | JH-Serie | LHA/LY |
|-----------|---------|---------|---------|---------|
| Impeller | 28–38 | 35–48 | 45–65 | 65–85 |
| Ölfilter | 12–18 | 14–20 | 18–26 | 22–34 |
| Kraftstofffilter | 14–20 | 14–20 | 18–30 | 28–38 |
| Keilriemen | 14–22 | 16–24 | 18–30 | 22–35 |
| Zinkanode Motor | 12–18 | 14–20 | 14–25 | 18–30 |
| Zinkanode Saildrive | 35–45 | 35–45 | 42–62 | — |
| Thermostat | 35–50 | 42–58 | 55–75 | 65–90 |
| Motorlager (Stk.) | 28–38 | 32–42 | 45–60 | 65–110 |
| Anlasser | 280–350 | 320–400 | 420–550 | 580–720 |
| Lichtmaschine | 280–380 | 350–450 | 420–550 | 550–720 |
| Saildrive-Manschette | — | 280–350 (SD20) | 380–530 (SD50/60) | — |

### 23.3 Wartungskosten pro Jahr (geschätzt, Eigenleistung)

| Modell-Klasse | 250h/Jahr | Material EUR | Werkstatt EUR (bei Fremdvergabe) |
|--------------|----------|-------------|-------------------------------|
| GM-Serie | Öl+Filter+Impeller | 100–150 | 350–500 |
| YM-Serie | Öl+Filter+Impeller | 120–180 | 400–550 |
| JH-Serie | Öl+Filter+Impeller+KST-Filter | 180–260 | 550–800 |
| LHA-Serie | Öl+Filter+Impeller+KST-Filter | 250–380 | 800–1.200 |
| LY/BY-Serie | Öl+Filter+Impeller+KST-Filter | 350–500 | 1.000–1.500 |

---

## 24. Quellenverzeichnis

### 24.1 Primärquellen

| Quelle | Beschreibung | Confidence |
|--------|-------------|-----------|
| Yanmar Marine International (yanmar.com/marine) | Offizielle Produktdatenblätter, Spezifikationen | measured |
| Yanmar Werkstatthandbücher (Service Manuals) | Wartungsanleitungen, Toleranzen, Drehmomentwerte | measured |
| Yanmar Parts Catalog Online (parts.yanmarmarine.com) | Teilenummern, Explosionszeichnungen | measured |
| Yanmar Servicebulletins | Technische Mitteilungen, Rückrufe, Updates | documented |
| ISO 8665:2006 | Leistungsmessung Marine-Motoren | measured |
| ISO 3046 | Motorleistung, Referenzbedingungen | measured |
| EU RCD 2013/53/EU | Abgasemissionsgrenzwerte Freizeitboote | measured |
| IMO MARPOL Annex VI | NOx-Grenzwerte Schiffsmotoren | measured |

### 24.2 Sekundärquellen

| Quelle | Beschreibung | Confidence |
|--------|-------------|-----------|
| Nigel Calder: "Marine Diesel Engines" (3. Aufl.) | Standardwerk Marine-Dieseltechnik | documented |
| Yanmar-Vertragshändler-Netzwerk (DE/AT/CH) | Preise, Verfügbarkeiten, Erfahrungswerte | documented |
| Yachtforen (Segeln-Forum, YBW, Cruisers Forum) | Eigner-Erfahrungsberichte, Langzeit-Feedback | estimated |
| Werft-Befragungen (Hanseyachts, Bavaria, Contest) | OEM-Einbaurichtlinien, Ausfallstatistiken | documented |
| ADAC Sportschifffahrt — Technische Berichte | Motorentests, Vergleichsberichte | documented |
| IMCI (International Marine Certification Institute) | CE-Zertifizierungsdaten | measured |

---

## 25. Einbau- und Umrüstungsrichtlinien

### 25.1 Motorraum-Anforderungen nach Bootsklasse

**Segelboote 6–9 m (GM/YM-Klasse):**

| Anforderung | Mindestwert | Empfohlen | Norm |
|-------------|-------------|-----------|------|
| Motorraum-Volumen | 0,15 m³ | 0,25 m³ | ISO 9094 |
| Belüftung Zuluft | 50 cm² | 80 cm² | ISO 9094 |
| Belüftung Abluft | 40 cm² | 65 cm² | ISO 9094 |
| Schallschutz | nicht vorgeschrieben | 20 mm Verbundmatte | — |
| Brandschutz | Feuerlöscher 1 kg (ABC) | 2 kg automatisch | ISO 9094 |
| Leckage-Auffangwanne | empfohlen | Edelstahl, 2 L | — |
| Zugangslukenmaß | 400 × 400 mm | 500 × 500 mm | — |
| Kabelführung | geschützt | Wellrohr, brandhemmend | ISO 10133 |

**Segelboote 10–15 m (JH-Klasse):**

| Anforderung | Mindestwert | Empfohlen | Norm |
|-------------|-------------|-----------|------|
| Motorraum-Volumen | 0,35 m³ | 0,55 m³ | ISO 9094 |
| Belüftung Zuluft | 100 cm² | 160 cm² | ISO 9094 |
| Belüftung Abluft | 80 cm² | 130 cm² | ISO 9094 |
| Schallschutz | empfohlen | 30 mm Verbundmatte | — |
| Brandschutz | Feuerlöscher 2 kg (ABC) | Automatik-System | ISO 9094 |
| Leckage-Auffangwanne | vorgeschrieben | Edelstahl, 5 L | RCD |
| Zugangslukenmaß | 450 × 500 mm | 600 × 600 mm | — |
| Abgas-Isolierung | vorgeschrieben | Doppelwandig + Isolation | ISO 9094 |

**Motorboote 10–20 m (LHA/LY/BY-Klasse):**

| Anforderung | Mindestwert | Empfohlen | Norm |
|-------------|-------------|-----------|------|
| Motorraum-Volumen | 0,80 m³ (pro Motor) | 1,20 m³ | ISO 9094 |
| Belüftung Zuluft | 200 cm² (pro Motor) | 350 cm² | ISO 9094 |
| Belüftung Abluft | 160 cm² (pro Motor) | 280 cm² | ISO 9094 |
| Schallschutz | 30 mm | 50 mm Verbundmatte | — |
| Brandschutz | Automatik-Löschanlage | FM200 oder Novec 1230 | ISO 9094 |
| Leckage-Auffangwanne | vorgeschrieben | Edelstahl, 10 L | RCD |
| Motorraum-Lüfter | Pflicht (mechanisch) | Thermostatisch gesteuert | — |

### 25.2 Umrüstung GM → YM

Die häufigste Umrüstung ist der Ersatz eines alten GM-Motors durch die YM-Nachfolgeserie. Yanmar hat die Befestigungspunkte und Saildrive-Schnittstellen kompatibel gehalten.

**Kompatibilitätsmatrix GM → YM:**

| Alt (GM) | Neu (YM) | Leistung alt→neu | Saildrive | Anpassungen nötig |
|----------|----------|-----------------|-----------|-------------------|
| 1GM10 (9 PS) | 1YM15 (14,7 PS) | +63 % | SD20 kompatibel | Kabelbaum, Instrumente, Gashebel |
| 2GM20 (18 PS) | 2YM20 (21 PS) | +17 % | SD20 kompatibel | Kabelbaum, Instrumente |
| 3GM30 (27 PS) | 3YM30 (29 PS) | +7 % | SD20/SD25 | Kabelbaum, Instrumente |

**Typische Kosten Umrüstung GM → YM (inkl. Arbeitszeit):**

| Posten | EUR |
|--------|-----|
| Motor inkl. Saildrive | 8.500–14.500 |
| Kabelbaum-Anpassung | 350–600 |
| Neue Instrumente | 400–800 |
| Motorlager (ggf. Adapter) | 150–300 |
| Auspuffanlage-Anpassung | 200–500 |
| Montage Werft (12–20h) | 1.200–2.500 |
| Probefahrt und Einstellung | 200–400 |
| **Gesamt** | **11.000–19.600** |

### 25.3 Umrüstung ältere JH → aktuelle JH (Common Rail)

| Alt | Neu | Hauptunterschiede | Anpassungen |
|-----|-----|------------------|-------------|
| 3JH25A (25 PS) | 3JH40 (39 PS) | Mechanisch → CR, +56 % | Kabelbaum, ECU, Instrumente digital, Auspuff |
| 4JH4E (54 PS) | 4JH57 (57 PS) | Mechanisch → CR, +6 % | Kabelbaum, ECU, Instrumente, Kraftstoffleitungen |
| 4JH5E (75 PS) | 4JH80 (80 PS) | Mechanisch → CR, +7 % | Kabelbaum, ECU, Instrumente, Ladeluftverrohrung |

**Typische Kosten Umrüstung ältere JH → neue JH-CR:**

| Posten | EUR |
|--------|-----|
| Motor inkl. Saildrive (SD50/60) | 20.000–42.000 |
| Kabelbaum komplett neu | 600–1.200 |
| Digitale Instrumente (YD25/YD42) | 500–900 |
| Auspuffanlage-Anpassung | 400–800 |
| Kraftstoffleitungen erneuern | 300–600 |
| Montage Werft (20–35h) | 2.500–5.000 |
| Probefahrt, Einstellung, Fehlerspeicher | 300–600 |
| **Gesamt** | **24.600–51.100** |

### 25.4 Fundamentverstärkung

**Motorfundament-Anforderungen:**

| Motor-Klasse | Stringer-Material | Min. Wandstärke | Schrauben | Drehmomentwerte |
|-------------|-------------------|----------------|-----------|----------------|
| GM/YM (bis 30 PS) | GFK/Sperrholz | 10 mm GFK | M10 Edelstahl | 35 Nm |
| JH (bis 60 PS) | GFK-Sandwich | 12 mm GFK | M12 Edelstahl | 55 Nm |
| JH (bis 110 PS) | GFK-Sandwich | 15 mm GFK | M12 Edelstahl | 55 Nm |
| LHA (bis 315 PS) | GFK/Stahl | 18 mm GFK oder 6 mm Stahl | M14 Edelstahl | 85 Nm |
| LY/BY (bis 530 PS) | Stahl/Aluminium | 8 mm Stahl | M16 Edelstahl | 120 Nm |

---

## 26. Kraftstoffsystem-Details

### 26.1 Kraftstoffanlage nach Motorklasse

**Typische Kraftstoffsystem-Komponenten:**

| Komponente | GM/YM | JH | LHA/LY/BY |
|-----------|-------|-----|-----------|
| Tankvolumen (Segelboot) | 40–80 L | 80–200 L | 200–1.000 L |
| Tankvolumen (Motorboot) | — | 100–300 L | 300–3.000 L |
| Tankmaterial | GFK/Edelstahl | Edelstahl/Aluminium | Edelstahl/Aluminium |
| Vorfilter/Wasserabscheider | Optional (Racor) | Empfohlen (Racor 500FG) | Pflicht (Racor 900/1000) |
| Kraftstoffleitung | 8 mm Gummi | 10 mm Gummi/Stahl | 12 mm Stahl |
| Kraftstoffrücklauf | 6 mm | 8 mm | 10 mm |
| Absperrhahn am Tank | Pflicht | Pflicht | Pflicht (elektrisch empfohlen) |
| Tankbelüftung | 12 mm Schlauch | 16 mm Schlauch | 20 mm Rohr |

### 26.2 Reichweitenberechnung

**Formel:** Reichweite (sm) = Tankvolumen (L) ÷ Verbrauch bei Reisefahrt (L/h) × Reisegeschwindigkeit (kn)

**Beispielrechnungen Segelboote unter Motor:**

| Boot | Motor | Tank | Reiseverbrauch | Geschwindigkeit | Reichweite |
|------|-------|------|---------------|----------------|-----------|
| 8 m Segelboot | 2YM20 | 40 L | 3,2 L/h | 5,5 kn | ca. 69 sm |
| 10 m Segelboot | 3YM30 | 60 L | 4,0 L/h | 6,0 kn | ca. 90 sm |
| 12 m Segelboot | 3JH40 | 100 L | 4,8 L/h | 6,5 kn | ca. 135 sm |
| 14 m Segelboot | 4JH57 | 150 L | 7,6 L/h | 7,0 kn | ca. 138 sm |
| 16 m Segelboot | 4JH80 | 200 L | 10,2 L/h | 7,5 kn | ca. 147 sm |
| 20 m Segelboot | 4JH110 | 350 L | 13,5 L/h | 8,0 kn | ca. 207 sm |

**Beispielrechnungen Motorboote:**

| Boot | Motor | Tank | Reiseverbrauch | Geschwindigkeit | Reichweite |
|------|-------|------|---------------|----------------|-----------|
| 10 m Verdränger | 4JH80 | 200 L | 10,2 L/h | 7,5 kn | ca. 147 sm |
| 12 m Halbgleiter | 4LHA-STP (×2) | 600 L | 64 L/h | 22 kn | ca. 206 sm |
| 14 m Halbgleiter | 6LY-STP (×2) | 1.000 L | 96 L/h | 26 kn | ca. 271 sm |
| 16 m Gleiter | 8BY-260Z (×2) | 1.500 L | 144 L/h | 32 kn | ca. 333 sm |

### 26.3 Diesel-Qualität und Problemvermeidung

**Anforderungen an Marine-Diesel:**

| Parameter | Norm EN 590 | Empfohlen Marine |
|-----------|------------|-----------------|
| Cetanzahl | ≥51 | ≥52 |
| Schwefelgehalt | ≤10 ppm | ≤10 ppm |
| Wassergehalt | ≤200 ppm | ≤100 ppm |
| FAME-Anteil (Bio) | ≤7 % (B7) | ≤7 % |
| Kälteverhalten (CFPP) | Saisonabhängig | -20 °C (Winter) |
| Partikelverunreinigung | ISO 12/9 | ISO 12/9 |

**Biozid-Empfehlungen:**

| Produkt | Wirkstoff | Dosierung | Preis EUR |
|---------|-----------|----------|-----------|
| Grotamar 82 | MIPA (Isothiazolinon) | 1 mL/L (Erstbehandlung), 0,25 mL/L (Erhaltung) | 35–45 / 250 mL |
| Diesel Guard | MIPA + BIT | 1 mL/L | 28–38 / 200 mL |
| Biobor JF | Bor-Verbindung | 2,7 mL/L (Schockdosis) | 40–55 / 500 mL |
| Star Brite Diesel Treatment | Multi-Additiv + Biozid | 30 mL/10 L | 22–30 / 500 mL |

---

## 27. Abgasanlage und Auspuffsystem

### 27.1 Nassauspuff-Prinzip

Alle Yanmar-Marine-Dieselmotoren verwenden das Nassauspuff-Prinzip (Wet Exhaust):

1. Heiße Abgase verlassen den Auspuffkrümmer (450–600 °C)
2. In der Mischkammer wird Kühlwasser (Seewasser) eingemischt
3. Abgas-Wasser-Gemisch wird durch Schläuche zum Heck geleitet
4. Austritt über Auspuffendstück am/unter dem Spiegel

**Vorteile Nassauspuff:**
- Deutlich geringere Temperaturen in der Auspuffleitung (<60 °C nach Mischung)
- Geräuschdämpfung durch Wassermischung
- Kein heißes Auspuffrohr im Boot
- Einfacherer Einbau (flexible Schläuche statt Metallrohre)

**Gefahren:**
- Seewasser kann bei Motorstillstand zurücklaufen → Wasserschlag!
- Auspuffmischkammer kann korrodieren → Leckage
- Schläuche können im Inneren ausbrennen wenn Motor ohne Seewasser läuft

### 27.2 Auspuffkomponenten

| Komponente | Beschreibung | Material | Lebensdauer |
|-----------|-------------|---------|------------|
| Auspuffkrümmer | Sammelt Abgase aller Zylinder | Grauguss/Edelstahl | 5.000–10.000h |
| Mischkammer (Mixing Elbow) | Punkt der Wassereinmischung | Gusseisen/GFK/Edelstahl | 3.000–7.000h |
| Auspuffschlauch | Wassergekühlter Abgasschlauch | EPDM-Gummi, verstärkt | 5–8 Jahre |
| Wassersammler (Waterlock) | Sammelt Wasser vor der Steigstrecke | GFK/Kunststoff | 10+ Jahre |
| Schwanenhals | U-förmige Steigstrecke (Siphon) | Edelstahl/GFK | 10+ Jahre |
| Auspuffendstück | Austritt am Spiegel/Heck | GFK/Edelstahl | 10+ Jahre |
| Rückschlagventil | Verhindert Wasserrücklauf | Gummi/Kunststoff | 3–5 Jahre |

### 27.3 Dimensionierung Auspuff

| Motor | Auspuff-Innendurchmesser | Wassersäulenhöhe | Min. Schwanenhals über WL |
|-------|------------------------|-----------------|--------------------------|
| GM-Serie | 38 mm (1,5") | 300 mm | 300 mm |
| YM-Serie | 38–45 mm (1,5–1,75") | 300 mm | 300 mm |
| JH 40/45 | 45 mm (1,75") | 400 mm | 400 mm |
| JH 57/80 | 50 mm (2") | 400 mm | 400 mm |
| JH 110 | 60 mm (2,5") | 500 mm | 500 mm |
| LHA | 76 mm (3") | 500 mm | 500 mm |
| LY/BY | 90 mm (3,5") | 600 mm | 600 mm |

### 27.4 Auspuff-Schwachstellen und Prävention

| Problem | Ursache | Prävention |
|---------|---------|-----------|
| Mischkammer-Korrosion | Grauguss + Seewasser + Hitze | Edelstahl-Mischkammer nachrüsten, alle 3.000h inspizieren |
| Auspuffschlauch innen verbrannt | Motor ohne Seewasser gelaufen | Immer Seeventil zuerst öffnen, Impeller-Zustand prüfen |
| Wasserschlag durch Rücklauf | Schwanenhals zu niedrig, kein Ventil | Schwanenhals min. 300 mm über WL, Rückschlagventil einbauen |
| Rußablagerungen im Wassersammler | Unvollständige Verbrennung (Kurzstrecke) | Motor regelmäßig warmfahren, alle 2 Jahre reinigen |
| Undichtigkeit an Schlauchklemmen | Korrosion, Vibration | Edelstahl-Schlauchklemmen (A4), 2× pro Verbindung |

---

## 28. Elektrische Anlage

### 28.1 Bordnetz und Verkabelung nach Motorklasse

| Parameter | GM-Serie | YM-Serie | JH-Serie | LHA/LY/BY |
|-----------|---------|---------|---------|-----------|
| Bordspannung | 12V | 12V | 12V | 12V (24V Option LY/BY) |
| Starterbatterie min. | 50 Ah | 50 Ah | 70 Ah | 100 Ah |
| Starterstrom (CCA) | >400A | >400A | >600A | >800A |
| Ladestrom (LiMa) | 35A (std) / 55A (opt) | 80A | 125A | 150–250A |
| Kabelquerschnitt Starter | 25 mm² | 25 mm² | 35 mm² | 50 mm² |
| Kabelquerschnitt Masse | 25 mm² | 25 mm² | 35 mm² | 50 mm² |
| Hauptsicherung | 50A | 60A | 80A | 125A |
| Kabeltyp | Verzinntes Kupfer | Verzinntes Kupfer | Verzinntes Kupfer | Verzinntes Kupfer |
| Kabelisolierung | PVC marine-grade | PVC marine-grade | XLPE/PVC | XLPE/PVC |

### 28.2 Lichtmaschinen-Nachrüstung

Die Standard-Lichtmaschine der GM-Serie (35A) ist für moderne Boote mit Kühlschrank, Autopilot, GPS, AIS und Funkgerät oft unzureichend.

**Nachrüst-Optionen:**

| Produkt | Leistung | Kompatibel mit | Preis EUR | Besonderheiten |
|---------|---------|---------------|-----------|----------------|
| Balmar AT 12V/80A | 80A | GM, YM | 680–780 | Inkl. Regler, breiter Riemen nötig |
| Mastervolt Alpha Pro III 12/90 | 90A | GM, YM | 720–850 | 3-Stufen-Regler integriert |
| Balmar AT 12V/120A | 120A | JH | 780–900 | Für intensive Bordnetz-Nutzung |
| Mastervolt Alpha Compact 12/130 | 130A | JH | 850–980 | Kompaktbauweise |
| Balmar AT 12V/200A | 200A | LHA, LY | 980–1.150 | Für Yacht-Ausstattung |

### 28.3 Glühkerzen-System

| Motor-Serie | Glühkerzentyp | Teilenummer | Vorglühzeit | Anzahl |
|------------|--------------|------------|------------|--------|
| GM-Serie | Stift-Glühkerze | 128170-77800 | 10–15 s | 1/2/3 |
| YM-Serie | Stift-Glühkerze | 119773-77800 | 8–12 s | 1/2/3 |
| JH-Serie | Keramik-Glühkerze | 129470-77800 | 3–5 s | 3/4 |
| LHA-Serie | Keramik-Glühkerze | 119593-77800 | 3–5 s | 4 |

**Glühkerzen-Diagnose:**
- Widerstand messen: GM/YM: 0,5–1,5 Ω, JH/LHA: 0,2–0,8 Ω
- Stromaufnahme: GM/YM: 8–12A pro Kerze, JH: 15–20A pro Kerze
- Prüfspannung: 12V direkt anlegen, Spitze muss innerhalb 3 s glühen
- Lebensdauer: 3.000–5.000 Betriebsstunden (eher 2.000–3.000 in Salzluft)

---

## 29. Propellerauswahl und -anpassung

### 29.1 Propellertypen für Yanmar-Motoren

| Propellertyp | Vorteile | Nachteile | Empfehlung |
|-------------|---------|----------|-----------|
| 2-Blatt Faltpropeller | Geringster Widerstand unter Segel | Weniger Schub, Vibration | Regattaboote |
| 3-Blatt Faltpropeller | Guter Kompromiss Schub/Widerstand | Etwas mehr Widerstand als 2-Blatt | Fahrtensegler (Standard) |
| Festpropeller 2-Blatt | Robust, günstig | Hoher Widerstand unter Segel | Motorsegler, Verdränger |
| Festpropeller 3-Blatt | Bester Schub, sanfter Lauf | Höchster Widerstand unter Segel | Motorboote |
| Verstellpropeller | Optimaler Wirkungsgrad in jedem Betrieb | Teuer, komplex | Langfahrt, professionell |

### 29.2 Propellergrößen-Empfehlung nach Motor und Saildrive

| Motor | Saildrive | Empfohlener Propeller Ø | Empfohlene Steigung | Hersteller-Beispiele |
|-------|-----------|------------------------|--------------------|--------------------|
| 1YM15 | SD20 | 12–13" | 8–9" | Gori 2-Bl. 12×8, Flexofold 13×9 |
| 2YM15 | SD20 | 13–14" | 9–10" | Gori 2-Bl. 13×9, Volvo FP 14×10 |
| 2YM20 | SD20 | 14–15" | 10–11" | Flexofold 14×10, Gori 3-Bl. 15×10 |
| 3YM30 | SD25 | 15–16" | 11–12" | Gori 3-Bl. 15×11, MaxProp 16×12 |
| 3JH40 | SD50 | 15–17" | 11–13" | MaxProp 16×12, Flexofold 17×12 |
| 4JH45 | SD50 | 16–17" | 12–13" | MaxProp 17×13, Gori 3-Bl. 17×12 |
| 4JH57 | SD60 | 17–18" | 13–14" | MaxProp 18×14, Variprop 18×13 |
| 4JH80 | SD60 | 18–19" | 14–15" | MaxProp 19×15, Variprop 19×14 |
| 4JH110 | SD60 | 19–21" | 15–17" | MaxProp 20×16, Variprop 21×16 |

### 29.3 Propeller-Anpassung bei Leistungsproblemen

**Motor erreicht nicht Nenndrehzahl (Vollgas-Drehzahl zu niedrig):**
- Propeller zu groß (Durchmesser) oder zu steil (Steigung)
- Lösung: Steigung reduzieren um 1" pro 150–200 U/min Defizit
- Alternative: Durchmesser um 1" reduzieren (weniger effektiv)

**Motor überdreht bei Vollgas:**
- Propeller zu klein oder Steigung zu flach
- Lösung: Steigung erhöhen um 1" pro 150–200 U/min Überschuss
- Rumpfbewuchs kann ähnlichen Effekt haben → zuerst Rumpf reinigen!

**Kavitation (Vibrationen, Geräusch, wenig Schub):**
- Propeller zu klein für die Leistung
- Saildrive-Platte erzeugt Turbulenz
- Lösung: Propellergröße anpassen, Strömungsprofil der SD-Platte prüfen

---

## 30. Lebenszyklus-Kostenanalyse

### 30.1 Total Cost of Ownership (TCO) — 20-Jahre-Betrachtung

**Annahmen:** 250 Betriebsstunden/Jahr, regelmäßige Wartung, Eigenleistung bei einfachen Arbeiten, Werkstatt für komplexe Aufgaben.

**GM/YM-Klasse (Beispiel 3YM30, 29 PS):**

| Position | Kosten EUR | Intervall |
|----------|-----------|-----------|
| Anschaffung Motor + SD25 | 14.000 | Einmalig |
| Ölwechsel (50×) | 3.500 | 20 Jahre × 250h = alle 250h |
| Impeller (20×) | 840 | Jährlich |
| Kraftstofffilter (20×) | 360 | Jährlich |
| Keilriemen (10×) | 200 | Alle 2 Jahre |
| Zinkanoden Motor (40×) | 640 | Halbjährlich |
| Zinkanoden Saildrive (40×) | 1.520 | Halbjährlich |
| Saildrive-Manschette (2×) | 700 | Alle 7 Jahre |
| Thermostat (3×) | 150 | Alle 2.000h |
| Wärmetauscher-Service (5×) | 750 | Alle 2.000h |
| Kühlmittel (10×) | 350 | Alle 2 Jahre |
| Glühkerzen (3×) | 180 | Alle 3.000h |
| Motorlager (2×) | 340 | Alle 2.500h |
| Förderpumpe (1×) | 180 | Bei 4.000h |
| Unvorhergesehene Reparaturen | 2.000 | Pauschal |
| **TCO 20 Jahre** | **ca. 25.710** | |
| **TCO pro Betriebsstunde** | **ca. 5,14 EUR/h** | |

**JH-Klasse (Beispiel 4JH57, 57 PS):**

| Position | Kosten EUR | Intervall |
|----------|-----------|-----------|
| Anschaffung Motor + SD60 | 28.500 | Einmalig |
| Ölwechsel (50×) | 5.000 | Alle 250h |
| Impeller (20×) | 1.100 | Jährlich |
| Kraftstofffilter primär+sekundär (20×) | 960 | Jährlich |
| Keilriemen (10×) | 260 | Alle 2 Jahre |
| Zinkanoden Motor (40×) | 720 | Halbjährlich |
| Zinkanoden Saildrive (40×) | 2.000 | Halbjährlich |
| Saildrive-Manschette (2×) | 960 | Alle 7 Jahre |
| Thermostat (3×) | 210 | Alle 2.000h |
| Wärmetauscher-Service (5×) | 1.250 | Alle 2.000h |
| Kühlmittel (10×) | 450 | Alle 2 Jahre |
| Luftfilter (5×) | 250 | Alle 1.000h |
| Motorlager (2×) | 480 | Alle 2.500h |
| Injektor-Service (2×) | 1.800 | Alle 4.000h |
| ECU-Wartung | 500 | Pauschal |
| Unvorhergesehene Reparaturen | 3.500 | Pauschal |
| **TCO 20 Jahre** | **ca. 47.940** | |
| **TCO pro Betriebsstunde** | **ca. 9,59 EUR/h** | |

**LHA-Klasse (Beispiel 4LHA-STP, 240 PS, Motorboot Twin):**

| Position | Kosten EUR | Intervall |
|----------|-----------|-----------|
| Anschaffung 2× Motor + Getriebe | 97.000 | Einmalig |
| Ölwechsel (2× Motor, 50×) | 10.000 | Alle 250h |
| Impeller (2×, 20×) | 2.600 | Jährlich |
| Kraftstofffilter (2×, 20×) | 1.520 | Jährlich |
| Getriebeöl (2×, 20×) | 1.200 | Jährlich |
| Zinkanoden (4×/Jahr, 20 J.) | 2.400 | Vierteljährlich |
| Keilriemen (2×, 10×) | 600 | Alle 2 Jahre |
| Turbolader-Service (2×, 3×) | 5.400 | Alle 3.000h |
| Wärmetauscher (2×, 5×) | 3.000 | Alle 2.000h |
| Kühlmittel (2×, 10×) | 900 | Alle 2 Jahre |
| Injektor-Service (2×, 3×) | 5.400 | Alle 3.000h |
| Schwingungsdämpfer (2×, 2×) | 1.600 | Alle 4.000h |
| Motorlager (2×, 2×) | 1.360 | Alle 2.500h |
| Unvorhergesehene Reparaturen | 8.000 | Pauschal |
| **TCO 20 Jahre** | **ca. 140.980** | |
| **TCO pro Betriebsstunde** | **ca. 28,20 EUR/h** | |

### 30.2 Wertentwicklung gebrauchter Yanmar-Motoren

| Alter | Betriebsstunden | Restwert (% vom Neupreis) |
|-------|----------------|--------------------------|
| 0–2 Jahre | 0–500h | 70–85 % |
| 3–5 Jahre | 500–1.500h | 50–70 % |
| 6–10 Jahre | 1.500–3.000h | 35–55 % |
| 11–15 Jahre | 3.000–4.500h | 20–40 % |
| 16–20 Jahre | 4.500–6.000h | 10–25 % |
| >20 Jahre | >6.000h | 5–15 % |

**Wertsteigernde Faktoren:**
- Lückenloses Wartungsheft (+10–20 %)
- Niedrige Betriebsstunden (<200h/Jahr) (+5–10 %)
- Süßwasserrevier (+5–10 %)
- Neuer Impeller, frischer Ölwechsel, Ersatzteile dabei (+5 %)

**Wertsenkende Faktoren:**
- Kein Wartungsheft (-20–30 %)
- Sichtbare Korrosion (-15–25 %)
- Ölundichtigkeit (-10–20 %)
- Kompression unter Sollwert (-15–30 %)
- Hohe Betriebsstunden (>400h/Jahr) (-5–10 %)

---

## 31. Yanmar-Händlernetz und Service

### 31.1 Autorisiertes Händlernetz Deutschland

Yanmar unterhält in Deutschland ein dichtes Netz autorisierter Händler und Servicepartner. Jeder autorisierte Partner hat Zugang zu:

- Original-Ersatzteilen mit 24h-Lieferzusage
- Werkstatthandbüchern und technischen Bulletins
- Diagnose-Software (für JH-CR, LHA, LY, BY)
- Schulungsprogramm (jährliche Weiterbildung)
- Garantie-Abwicklung

**Wichtige Serviceregionen (Auswahl):**

| Region | Haupthändler | Spezialgebiet |
|--------|-------------|--------------|
| Ostsee Nord (SH) | Marine-Motoren Nord | Segelboot-Motoren, Saildrive |
| Ostsee Süd (MV) | Yanmar Marine MV | Saildrive-Spezialist |
| Nordsee / Elbe | Motortech Hamburg | JH/LHA-Serie |
| Bodensee | Bootsmotoren Bodensee | BSO-II-konforme Installationen |
| Mittelmeer ab-/aufsteiger | Diverse über Yanmar Europe | LY/BY-Serie, Twin-Installationen |

### 31.2 Garantiebedingungen

| Garantieart | Dauer | Bedingungen |
|-------------|-------|------------|
| Standard-Garantie | 2 Jahre oder 1.000h (was zuerst eintritt) | Autorisierter Einbau, Wartung nach Plan |
| Erweiterte Garantie (YPP) | 5 Jahre oder 2.500h | Yanmar Protection Plan, Aufpreis ca. 5–8 % des Motorpreises |
| Saildrive-Garantie | 2 Jahre | Autorisierter Einbau |
| Getriebe-Garantie | 2 Jahre | Autorisierter Einbau |

**Garantie-Ausschlüsse:**
- Verschleißteile (Impeller, Filter, Keilriemen, Zinkanoden)
- Schäden durch Fremdbetankung (falscher Kraftstoff)
- Schäden durch fehlende Wartung
- Schäden durch nicht autorisierte Modifikationen
- Frostschäden durch fehlendes Kühlmittel

### 31.3 Yanmar-Diagnosesystem

Für die Common-Rail-Motoren (JH, LHA, LY, BY) bietet Yanmar ein proprietäres Diagnosesystem:

**Yanmar Diagnostic System (YDS):**
- PC-basierte Software mit Schnittstelle zum Motorsteuergerät
- Liest Fehlerspeicher (DTC) aus und löscht sie
- Zeigt Live-Daten: Drehzahl, Temperaturen, Drücke, Einspritzmengen
- Injektorkalibrierung (IQA-Werte)
- Firmware-Updates für ECU
- Nur für autorisierte Servicepartner verfügbar

**NMEA 2000 Monitoring (für Eigner):**
- Über VC10 Gateway und kompatible Displays (z. B. B&G, Raymarine, Garmin)
- Echtzeitdaten: Drehzahl, Temperatur, Öldruck, Verbrauch
- Alarmweiterleitung an Plotterbildschirm
- Keine Tiefendiagnose möglich (DTC nur als Alarmmeldung)

---

## 32. Vergleichstabellen — Yanmar vs. Wettbewerber

### 32.1 Segelboot-Klasse (20–30 PS)

| Parameter | Yanmar 3YM30 | Volvo Penta D1-30 | Nanni N4.38 | Beta Marine 30 |
|-----------|-------------|-------------------|-------------|----------------|
| Leistung | 29 PS | 28 PS | 29 PS | 30 PS |
| Hubraum | 854 cm³ | 1.131 cm³ | 1.029 cm³ | 1.299 cm³ |
| Zylinder | 3 | 3 | 3 | 3 |
| Gewicht | 92 kg | 118 kg | 112 kg | 105 kg |
| Verbrauch | 6,0 L/h | 6,4 L/h | 6,2 L/h | 6,5 L/h |
| Saildrive | SD25 | MS15A | SD2.35 | — |
| Preis Motor+SD | 13.500–14.400 | 14.800–16.200 | 13.000–14.200 | 10.500–11.800 |
| Händlernetz DE | ★★★★★ | ★★★★★ | ★★★ | ★★ |
| Ersatzteilverfügb. | ★★★★★ | ★★★★★ | ★★★ | ★★★ |

### 32.2 Segelboot-Klasse (55–60 PS)

| Parameter | Yanmar 4JH57 | Volvo Penta D2-60 | Nanni N4.65 |
|-----------|-------------|-------------------|-------------|
| Leistung | 57 PS | 60 PS | 56 PS |
| Hubraum | 1.995 cm³ | 2.189 cm³ | 1.995 cm³ |
| Zylinder | 4 | 4 | 4 |
| Einspritzung | Common Rail | Common Rail | Mechanisch |
| Gewicht | 225 kg | 248 kg | 215 kg |
| Verbrauch | 12,0 L/h | 13,2 L/h | 12,5 L/h |
| Saildrive | SD60 | MS25S/A | SD2.60 |
| Preis Motor+SD | 27.500–29.500 | 30.000–33.000 | 25.000–28.000 |
| NMEA 2000 | Ja (über VC10) | Ja (nativ) | Nein |
| Händlernetz DE | ★★★★★ | ★★★★★ | ★★★ |

### 32.3 Motorboot-Klasse (300–320 PS)

| Parameter | Yanmar 4LHA-DTP | Volvo Penta D6-310 | Nanni N13.800 CR |
|-----------|----------------|--------------------|--------------------|
| Leistung | 315 PS | 310 PS | 300 PS |
| Hubraum | 3.318 cm³ | 5.500 cm³ | 3.400 cm³ |
| Zylinder | 4 | 6 | 6 |
| Gewicht | 395 kg | 580 kg | 480 kg |
| Verbrauch | 68 L/h | 72 L/h | 65 L/h |
| Leistungsgewicht | 0,80 PS/kg | 0,53 PS/kg | 0,63 PS/kg |
| Preis Motor+Getriebe | 52.000–57.000 | 58.000–65.000 | 48.000–55.000 |
| Joystick-System | JC-Serie (Option) | IPS (integriert) | Nein |

---

## 33. Spezialwerkzeuge und Hilfsmittel

### 33.1 Yanmar-Spezialwerkzeuge

| Werkzeug | Teilenummer | Einsatz | Erforderlich für |
|----------|------------|--------|-----------------|
| Ventilspiel-Fühlerblattlehre | — (Standard 0,05–1,00 mm) | Ventileinstellung | Alle Modelle |
| Injektoren-Abzieher GM/YM | 124610-92010 | Injektor-Demontage | GM/YM-Serie |
| Injektoren-Abzieher JH | 129470-92010 | CR-Injektor-Demontage | JH-Serie |
| Einspritzpumpen-Zeitpunkt-Messuhr | 128170-92020 | Förderbeginn einstellen | GM/YM (mechanisch) |
| Schwungscheiben-Arretierung | 129470-92030 | Motor bei OT fixieren | JH-Serie |
| Impeller-Abzieher | — (Standard 2-Arm) | Impeller-Wechsel | Alle Modelle |
| Seewasserpumpen-Dichtring-Einpresswerkzeug | 128990-92040 | Wellendichtring montieren | YM/JH-Serie |
| Ölfilterschlüssel | — (Standard 76 mm) | Ölfilter-Wechsel | JH/LHA/LY |
| Kompressionsmessgerät M10 | — (Standard Adapter M10) | Kompressionstest | GM/YM-Serie |
| Kompressionsmessgerät M12 | — (Standard Adapter M12) | Kompressionstest | JH-Serie |
| Kraftstoff-Rücklaufmengenmesser | 129470-92050 | CR-Injektor-Diagnose | JH-Serie |
| YDS-Diagnosekabel | 129470-92100 | ECU-Kommunikation | JH/LHA/LY/BY |

### 33.2 Empfohlene Verbrauchsmaterialien

| Material | Produkt-Beispiel | Einsatz | Preis EUR |
|----------|-----------------|--------|-----------|
| Motoröl 15W-40 CI-4 | Yanmar Premium Diesel Oil | Ölwechsel | 12–18/L |
| Motoröl 15W-40 CI-4 (Alternativ) | Castrol Vecton 15W-40 | Ölwechsel | 8–12/L |
| Getriebeöl SAE 30 | Yanmar Marine Gear Oil | Saildrive/Getriebe | 14–20/L |
| Getriebeöl SAE 30 (Alternativ) | Shell Spirax S2 A 80W-90 | Getriebe | 10–14/L |
| Kühlmittel OAT | Yanmar Premium Long-Life | Kühlsystem | 18–28/L |
| Kühlmittel (Alternativ) | Glysantin G40 | Kühlsystem | 12–18/L |
| Kraftstoff-Biozid | Grotamar 82 | Dieseltank | 35–45/250 mL |
| Korrosionsschutz-Spray | Yanmar Anti-Corrosion | Motorschutz Winterlager | 12–18/Dose |
| Kontaktfett (Elektrik) | Yanmar Connector Grease | Steckverbindungen | 8–12/Tube |
| Dichtmittel Motor | Loctite 5910 (Silikon, ölbeständig) | Dichtreparaturen | 14–20/Tube |
| Schraubensicherung | Loctite 243 (mittelfest) | Verschraubungen Motor | 12–16/Flasche |
| Teflonband | PTFE-Band 12mm | Gewindeabdichtung | 2–4/Rolle |
| Reiniger (Motor) | Yanmar Engine Degreaser | Motorreinigung | 15–22/L |

### 33.3 Drehmoment-Tabelle

**GM/YM-Serie:**

| Verschraubung | Drehmoment (Nm) | Anmerkung |
|---------------|----------------|-----------|
| Zylinderkopfschrauben | 39–44 | In Reihenfolge, 3 Stufen |
| Krümmer-Schrauben | 20–25 | M8 |
| Injektoren | 55–65 | Gegenhalteschlüssel |
| Glühkerzen | 15–20 | Nicht überdrehen! |
| Motorlager-Schrauben | 30–40 | M10 |
| Schwungscheiben-Schrauben | 78–88 | Schraubensicherung |
| Impeller-Deckel | 5–8 | Handfest, Dichtung |
| Seewasserpumpe | 12–16 | M6 |
| Ölfilter | ¾ Umdrehung nach Dichtungskontakt | Von Hand |
| Keilriemen-Spannschraube | 18–22 | M8 |

**JH-Serie:**

| Verschraubung | Drehmoment (Nm) | Anmerkung |
|---------------|----------------|-----------|
| Zylinderkopfschrauben | 68–78 | In Reihenfolge, 4 Stufen |
| Krümmer-Schrauben | 25–30 | M10 |
| CR-Injektoren | 35–40 | Kupferscheibe erneuern |
| CR-Hochdruckleitungen | 25–30 | Immer neue Überwurfmutter |
| Glühkerzen | 15–20 | Keramik — vorsichtig! |
| Motorlager-Schrauben | 50–60 | M12 |
| Schwungscheiben-Schrauben | 100–120 | Schraubensicherung |
| Saildrive-Flansch | 35–45 | Gleichmäßig über Kreuz |
| Wärmetauscher-Endkappen | 18–22 | O-Ring erneuern |
| Turbolader-Flansch (4JH80/110) | 22–28 | M8, hitzebeständig |

### 33.4 Winterlager-Checkliste

**Einlagerung (Herbst):**

- [ ] Motor warmfahren auf Betriebstemperatur
- [ ] Motoröl und Filter wechseln (warmes Öl = bessere Entleerung)
- [ ] Getriebeöl / Saildrive-Öl auf Milchigkeit prüfen → bei Bedarf wechseln
- [ ] Kühlmittel-Frostschutz prüfen (min. -20 °C) → bei Bedarf auffüllen
- [ ] Kraftstofftank volltanken + Biozid zusetzen
- [ ] Kraftstoffhahn schließen, Motor laufen lassen bis er abstirbt
- [ ] Impeller ausbauen oder alternativ: „Saisonimpeller" (billiger, nur zum Einlagern)
- [ ] Sprühöl in Ansaugöffnung sprühen, Motor kurz durchdrehen
- [ ] Seeventil schließen
- [ ] Seewasserfilter reinigen und trocknen lassen
- [ ] Auspuffanlage auf Kondenswasser prüfen
- [ ] Zinkanoden prüfen — bei >50 % Verbrauch jetzt tauschen
- [ ] Batterie abklemmen ODER Erhaltungsladegerät anschließen
- [ ] Motorraum-Belüftung leicht geöffnet lassen (Kondensat!)
- [ ] Saildrive-Manschette visuell prüfen
- [ ] Lichtmaschinen-Keilriemen entspannen (verlängert Lebensdauer)
- [ ] Motoroberfläche mit Korrosionsschutz einsprühen

**Inbetriebnahme (Frühjahr):**

- [ ] Visuell prüfen: Ölstand, Kühlmittelstand, Getriebeöl
- [ ] Neuen Impeller einsetzen (oder Saisonimpeller durch echten ersetzen)
- [ ] Keilriemen spannen und auf Risse prüfen
- [ ] Seewasserfilter montieren und reinigen
- [ ] Seeventil öffnen (WICHTIG: vor Motorstart!)
- [ ] Batterie anschließen, Spannung prüfen (>12,4 V)
- [ ] Kraftstoffhahn öffnen
- [ ] Kraftstoffsystem entlüften (Handpumpe betätigen)
- [ ] Motor starten, im Leerlauf warmfahren (5 Minuten)
- [ ] Seewasser-Auslass am Auspuff kontrollieren: Wasser muss fließen!
- [ ] Öldruckanzeige kontrollieren
- [ ] Temperaturanzeige beobachten (muss innerhalb 10 Minuten auf 70–85 °C steigen)
- [ ] Leerlauf stabil? Geräusche normal?
- [ ] Vorwärts-/Rückwärtsgang testen (bei gefiertem Boot)
- [ ] Betriebsstundenzähler notieren
- [ ] Nächsten Wartungstermin im Logbuch eintragen

---

## 34. Motorraum-Schalldämmung

### 34.1 Schalldämpfungs-Materialien

| Material | Dicke | Dämpfung (dB) | Temperaturbeständig | Preis EUR/m² |
|----------|-------|--------------|--------------------|--------------| 
| PU-Schaum (offenzellig) | 20 mm | 5–8 | bis 90 °C | 25–35 |
| PU-Schaum (offenzellig) | 30 mm | 8–12 | bis 90 °C | 35–50 |
| Verbundmatte (Blei/Schaum) | 25 mm | 12–18 | bis 100 °C | 55–80 |
| Verbundmatte (Blei/Schaum) | 35 mm | 15–22 | bis 100 °C | 75–110 |
| Mineralwolle (beschichtet) | 30 mm | 10–15 | bis 200 °C | 40–60 |
| Akustik-Schaum (schwer) | 25 mm | 8–12 | bis 120 °C | 45–65 |
| Aluminiumkaschierte Matte | 30 mm | 12–16 | bis 150 °C | 60–85 |

### 34.2 Schallschutz-Empfehlung nach Motorklasse

| Motor | Empfohlene Dämmung | Fläche ca. | Materialkosten EUR |
|-------|-------------------|-----------|-------------------|
| GM/YM (bis 30 PS) | 20 mm PU-Schaum | 1,5 m² | 40–55 |
| 3JH40 (39 PS) | 25 mm Verbundmatte | 2,0 m² | 110–160 |
| 4JH45–57 (45–57 PS) | 30 mm Verbundmatte | 2,5 m² | 190–275 |
| 4JH80–110 (80–110 PS) | 35 mm Verbundmatte | 3,0 m² | 225–330 |
| 4LHA (240–315 PS) | 50 mm Verbundmatte + Mineralwolle | 4,0 m² | 400–600 |
| 6LY/BY (380–530 PS) | 50 mm Verbundmatte + 30 mm Mineralwolle | 6,0 m² | 650–1.000 |

### 34.3 Erwartete Schallpegel mit Dämmung

| Motor | Ohne Dämmung (1m) | Mit Standard-Dämmung | Mit Premium-Dämmung |
|-------|-------------------|---------------------|---------------------|
| 1YM15 | 72 dB(A) | 65 dB(A) | 60 dB(A) |
| 3YM30 | 75 dB(A) | 67 dB(A) | 62 dB(A) |
| 3JH40 | 78 dB(A) | 68 dB(A) | 63 dB(A) |
| 4JH57 | 80 dB(A) | 70 dB(A) | 64 dB(A) |
| 4JH80 | 82 dB(A) | 72 dB(A) | 66 dB(A) |
| 4JH110 | 84 dB(A) | 74 dB(A) | 68 dB(A) |
| 4LHA-STP | 88 dB(A) | 76 dB(A) | 70 dB(A) |
| 4LHA-DTP | 90 dB(A) | 78 dB(A) | 72 dB(A) |
| 6LY-STP | 92 dB(A) | 80 dB(A) | 74 dB(A) |
| 8BY-260Z | 95 dB(A) | 83 dB(A) | 76 dB(A) |

---

## 35. Emissionen und Umweltauflagen

### 35.1 Abgasemissionen nach Norm

**IMO Tier II NOx-Grenzwerte (n = Nenndrehzahl in U/min):**

| Drehzahlbereich | NOx-Grenzwert (g/kWh) |
|----------------|----------------------|
| n < 130 | 14,4 |
| 130 ≤ n < 2.000 | 44 × n^(-0,23) |
| n ≥ 2.000 | 7,7 |

**Yanmar-Emissionswerte (Beispiele, gemessen nach ISO 8178 Zyklus E3):**

| Motor | NOx (g/kWh) | HC (g/kWh) | CO (g/kWh) | PM (g/kWh) | Norm erfüllt |
|-------|------------|-----------|-----------|-----------|-------------|
| 3YM30 | 7,1 | 0,8 | 2,1 | 0,3 | Tier II, RCD |
| 4JH57 | 6,5 | 0,5 | 1,4 | 0,15 | Tier II, RCD |
| 4JH80 | 6,2 | 0,4 | 1,2 | 0,12 | Tier II, RCD |
| 4JH110 | 6,0 | 0,4 | 1,1 | 0,10 | Tier II, RCD |
| 4LHA-STP | 5,8 | 0,3 | 0,9 | 0,08 | Tier II, RCD |
| 4LHA-DTP | 5,9 | 0,3 | 1,0 | 0,09 | Tier II, RCD |
| 6LY-STP | 5,5 | 0,3 | 0,8 | 0,07 | Tier II, RCD |
| 8BY-260Z | 5,2 | 0,2 | 0,7 | 0,06 | Tier II, RCD |

### 35.2 Bodensee-Schifffahrtsordnung (BSO II)

Für den Bodensee gelten besonders strenge Emissionsgrenzwerte:

| Parameter | BSO II Grenzwert | Yanmar JH-CR erfüllt? |
|-----------|-----------------|----------------------|
| CO | 75 g/kWh | Ja (1,1–1,4 g/kWh) |
| HC + NOx | 15 g/kWh | Ja (6,9–7,6 g/kWh) |
| PM | 1,5 g/kWh | Ja (0,10–0,15 g/kWh) |
| Schalldruck (25m) | 72 dB(A) bei Vmax | Modellabhängig, meist ja |

**BSO-II-Zulassung:** Alle aktuellen Yanmar JH-CR- und LHA-Motoren sind BSO-II-zugelassen (prüfen: aktuelles Zertifikat beim Händler).

### 35.3 Umwelt-Tipps für Yanmar-Betreiber

1. **Ölentsorgung:** Altöl niemals ins Wasser! Sammelstelle nutzen (kostenlos)
2. **Kraftstoff-Leckagen:** Ölauffangmatte unter dem Motor, Bilge regelmäßig inspizieren
3. **Kühlmittel:** Ethylenglykol ist giftig — nicht ins Wasser. Propylenglykol als umweltfreundliche Alternative
4. **Impeller-Entsorgung:** Gummi-Restmüll, nicht ins Meer
5. **Zinkanoden:** Metall-Recycling, nicht ins Wasser werfen
6. **Betriebsverhalten:** Motor bei Betriebstemperatur halten → weniger unverbrannte Emissionen

---

## 36. Digitale Motorüberwachung und Ferndiagnose

### 36.1 Yanmar Remote Monitoring (ab 2024)

Yanmar bietet für die JH-CR- und LHA/LY/BY-Serien ein optionales Fernüberwachungssystem:

**Yanmar Remote Monitoring System:**

| Feature | Beschreibung |
|---------|-------------|
| Echtzeit-Daten | Drehzahl, Temperatur, Öldruck, Verbrauch |
| GPS-Position | Standort-Tracking (bei aktiviertem GPS-Modul) |
| Alarm-Benachrichtigung | Push-Nachricht bei Überschreitung von Grenzwerten |
| Wartungserinnerung | Automatisch basierend auf Betriebsstunden |
| Fehlercode-Weiterleitung | DTC an Eigner und Servicepartner |
| Datenhistorie | 12 Monate Betriebsdaten-Speicherung |
| Schnittstelle | 4G/LTE Modul + Cloud-Server |
| App | iOS/Android, Yanmar Marine Connect |
| Preis | ca. 800 EUR Hardware + 15 EUR/Monat |

### 36.2 Aftermarket-Monitoring-Lösungen

| Produkt | Kompatibel mit | Funktion | Preis EUR |
|---------|---------------|---------|-----------|
| Yacht Devices YDEG-04 | JH-CR (NMEA 2000) | Gateway Yanmar→WiFi | 350–420 |
| Maretron USB100 | NMEA 2000 Netzwerk | Datenaufzeichnung am PC | 480–580 |
| Actisense NGW-1 | NMEA 2000 ↔ NMEA 0183 | Protokoll-Konvertierung | 220–280 |
| Victron Cerbo GX | Via NMEA 2000 | Integration in Victron-System, VRM-Portal | 320–400 |

---

## 37. AYDI-Bewertungsmatrix Yanmar-Motoren

### 37.1 AYDI-Score-Matrix für Motorenbewertung

Die folgende Matrix wird vom AYDI-Compliance- und Service-Pattern-Modul verwendet, um den Zustand eines Yanmar-Motors zu bewerten:

| Kriterium | Gewicht | 90–100 (ausgezeichnet) | 75–89 (gut) | 60–74 (akzeptabel) | 40–59 (mangelhaft) | 0–39 (kritisch) |
|-----------|---------|----------------------|------------|--------------------|--------------------|-----------------|
| Betriebsstunden vs. Alter | 15% | <150h/Jahr | 150–250h/J | 250–350h/J | 350–500h/J | >500h/J |
| Ölzustand (Farbe, Menge) | 10% | Bernstein, korrekt | Dunkel, korrekt | Dunkel, leicht zu wenig | Schwarz, Emulsion | Milchig (Wasser!) |
| Kompression (Abweichung) | 15% | <1 bar Differenz | 1–2 bar | 2–3 bar | 3–5 bar | >5 bar oder <20 bar |
| Kühlsystem (Temp-Verhalten) | 10% | 78–85 °C stabil | 85–92 °C stabil | 92–98 °C oder <70 °C | 98–105 °C | >105 °C |
| Kraftstoffsystem (Start) | 10% | Sofortstart (<3 s) | Start <5 s | Start <10 s | Mehrere Versuche | Startet nicht |
| Laufkultur (Vibrationen) | 10% | Gleichmäßig, leise | Leicht rauer Lauf | Spürbare Vibrationen | Starke Vibrationen | Klopfen |
| Leckagen (Öl, Diesel, Wasser) | 10% | Trocken | Leichte Ölspuren | Tropfende Leckage | Deutliche Leckage | Strömende Leckage |
| Elektrik (Ladung, Instrumente) | 5% | 14,0–14,4 V, alles OK | Leichte Abweichung | Sporadische Ausfälle | Häufige Fehlercodes | System-Ausfall |
| Wartungshistorie | 10% | Lückenlos, nach Plan | Kleine Lücken | Größere Lücken | Kaum dokumentiert | Keine Dokumentation |
| Visuelle Inspektion | 5% | Sauber, gepflegt | Leichte Korrosion | Mäßige Korrosion | Starke Korrosion | Strukturelle Schäden |

### 37.2 Automatische Schwachstellen-Zuordnung

Das AYDI-System ordnet automatisch bekannte Schwachstellen basierend auf Motormodell, Baujahr und Betriebsstunden zu:

| Trigger | Schwachstelle | Empfehlung |
|---------|--------------|------------|
| GM-Serie + >3.000h | Auspuffkrümmer-Rissbildung | Krümmer inspizieren lassen |
| GM-Serie + >15 Jahre | Einspritzleitungen korrodiert | Leitungen prophylaktisch tauschen |
| YM-Serie + >3.000h | Kraftstoff-Förderpumpe schwach | Förderpumpe prophylaktisch tauschen |
| YM-Serie + >10 Jahre | Auspuffmischkammer Korrosion | Mischkammer inspizieren |
| JH-CR + >4.000h | Common-Rail-Injektor Verkokung | Injektoren prüfen lassen |
| JH-CR + hohe Luftfeuchtigkeit | ECU-Feuchtigkeitsempfindlichkeit | Motorraum-Belüftung prüfen |
| 4JH80/110 + >3.000h | Turbolader-Ölundichtigkeit | Turbo inspizieren |
| Saildrive + >7 Jahre | Manschette Alterung | Manschette SOFORT tauschen |
| Saildrive + >5 Jahre | Manschette prüfen | Demontieren und beidseitig inspizieren |
| Alle + >2.500h | Motorlager-Ermüdung | Lager prüfen, ggf. tauschen |
| Alle + Langzeitlagerung >6 Monate | Diesel-Kontamination | Kraftstoff prüfen, Biozid verwenden |

---

## 38. Motorauswahl nach Bootstyp — Entscheidungshilfe

### 38.1 Segelboot-Motorisierung: Empfehlungsmatrix

**Faustregel:** 3–4 PS pro Tonne Verdrängung (Segelboot), 5–8 PS pro Tonne (Verdränger-Motorboot), 15–25 PS pro Tonne (Halbgleiter/Gleiter)

| Bootstyp | Verdrängung | LOA | Empfohlener Motor | Saildrive/Getriebe | Begründung |
|----------|------------|-----|-------------------|-------------------|------------|
| Jollenkreuzer | 1–2 t | 5–7 m | 1YM15 (14,7 PS) | SD20 oder KM2C | Leicht, kompakt, ausreichend Reserve |
| Daysailer/Kielboot | 2–3 t | 7–8 m | 2YM15 (14,7 PS) oder 2YM20 (21 PS) | SD20 | 2YM15 bei Gewichtspriorität, 2YM20 bei Leistungspriorität |
| Fahrtensegler klein | 3–5 t | 8–10 m | 2YM20 (21 PS) oder 3YM20 (21 PS) | SD20 | 3YM20 für mehr Komfort, 2YM20 bei engem Motorraum |
| Fahrtensegler mittel | 5–7 t | 10–12 m | 3YM30 (29 PS) | SD25 | Standardmotorisierung für 10–12 m |
| Fahrtensegler groß | 7–10 t | 12–14 m | 3JH40 (39 PS) oder 4JH45 (45 PS) | SD50 | 4JH45 für mehr Reserve bei Gegenwind/Strom |
| Blauwasseryacht | 10–14 t | 13–16 m | 4JH57 (57 PS) | SD60 | Ausreichend Reserve für schwere See |
| Blauwasseryacht groß | 14–20 t | 16–20 m | 4JH80 (80 PS) oder 4JH110 (110 PS) | SD60 oder KMH61A | 4JH110 für schwere Langkieler |
| Regattaboot | variabel | 8–14 m | Geringstmögliche PS | SD20/SD50 | Gewicht minimieren, 2-Blatt-Falter |
| Motorsegler | 8–15 t | 10–14 m | 4JH57 (57 PS) bis 4JH80 (80 PS) | KMH4A2 | Höhere Motorleistung als reines Segelboot |

### 38.2 Motorboot-Motorisierung: Empfehlungsmatrix

| Bootstyp | Verdrängung | LOA | Empfohlener Motor | Getriebe | Rumpfgeschw./Max |
|----------|------------|-----|-------------------|---------|-----------------|
| Verdränger klein | 3–5 t | 8–10 m | 4JH57 (57 PS) oder 4JH80 (80 PS) | KMH4A2 | 6,5–7,5 kn |
| Verdränger mittel | 8–15 t | 10–14 m | 4JH80 (80 PS) oder 4JH110 (110 PS) | KMH61A | 7–8,5 kn |
| Trawleryacht | 15–30 t | 12–16 m | 4LHA-STP (240 PS) Single | ZF 85IV | 8–10 kn |
| Trawleryacht groß | 25–50 t | 14–20 m | 6LPA-STP2 (315 PS) Twin | ZF 220A | 8–12 kn |
| Halbgleiter | 3–6 t | 8–12 m | 4LHA-STP (240 PS) Single oder Twin | ZF 85IV | 18–24 kn |
| Halbgleiter mittel | 5–10 t | 10–14 m | 4LHA-DTP (315 PS) Twin | ZF 85IV/220A | 22–30 kn |
| Halbgleiter groß | 10–20 t | 14–18 m | 6LY-STP (380 PS) Twin | ZF 280A | 25–32 kn |
| Gleiter/Sportboot | 5–10 t | 10–15 m | 6LY-UTP (440 PS) Twin | ZF 280A | 30–42 kn |
| Schnellboot/Megayacht | 10–25 t | 14–22 m | 8BY-260Z (530 PS) Twin/Triple | ZF 325A | 35–50 kn |

### 38.3 Häufige Fehler bei der Motorauswahl

| Fehler | Konsequenz | Richtige Wahl |
|--------|-----------|--------------|
| Motor zu klein gewählt | Dauervollast, Überhitzung, kurze Lebensdauer | Min. 20 % Leistungsreserve über Bedarf |
| Motor zu groß gewählt | Zu wenig Last, Verkokung, Dieselpest | Reisefahrt bei 65–75 % der Nenndrehzahl |
| Saildrive bei >80 PS Segelboot | Manschette an der Belastungsgrenze | SD60 max. für 110 PS, darüber Wellenanlage |
| Festpropeller bei Regattaboot | Massiver Segelverlust durch Propellerwiderstand | 2-Blatt-Faltpropeller |
| Kein Vorfilter/Wasserabscheider | Kraftstoffprobleme, Injektorschäden | Racor-Vorfilter immer installieren |
| Unzureichende Motorraum-Belüftung | Überhitzung, Leistungsverlust, Feuchtigkeitsschäden | Nach ISO 9094 dimensionieren, +20 % Sicherheit |

---

## 39. Typische Einbau-Konfigurationen nach Bootshersteller

### 39.1 Bavaria Yachts (Deutschland)

| Bootsmodell | Yanmar-Motor | Saildrive/Getriebe | Tankgröße | Propeller |
|-------------|-------------|-------------------|-----------|-----------|
| Bavaria C38 | 3YM30 (29 PS) | SD25 | 80 L | Gori 3-Bl. 15×11 |
| Bavaria C42 | 4JH45 (45 PS) | SD50 | 140 L | Flexofold 3-Bl. 17×12 |
| Bavaria C46 | 4JH57 (57 PS) | SD60 | 180 L | Flexofold 3-Bl. 18×13 |
| Bavaria C50 | 4JH80 (80 PS) | SD60 | 230 L | MaxProp 3-Bl. 19×14 |

### 39.2 Hanse Group (Deutschland)

| Bootsmodell | Yanmar-Motor | Saildrive/Getriebe | Tankgröße | Propeller |
|-------------|-------------|-------------------|-----------|-----------|
| Hanse 348 | 3YM30 (29 PS) | SD25 | 70 L | 2-Bl. Falter 15×10 |
| Hanse 388 | 3JH40 (39 PS) | SD50 | 100 L | 3-Bl. Falter 16×11 |
| Hanse 418 | 4JH45 (45 PS) | SD50 | 140 L | 3-Bl. Falter 17×12 |
| Hanse 460 | 4JH57 (57 PS) | SD60 | 200 L | 3-Bl. Falter 18×13 |
| Hanse 510 | 4JH80 (80 PS) | SD60 | 280 L | 3-Bl. Falter 19×14 |

### 39.3 Bénéteau/Jeanneau (Frankreich)

| Bootsmodell | Yanmar-Motor | Saildrive/Getriebe | Tankgröße | Propeller |
|-------------|-------------|-------------------|-----------|-----------|
| Jeanneau SO 319 | 2YM20 (21 PS) | SD20 | 50 L | 2-Bl. Falter 14×10 |
| Jeanneau SO 349 | 3YM30 (29 PS) | SD25 | 70 L | 2-Bl. Falter 15×11 |
| Jeanneau SO 380 | 3JH40 (39 PS) | SD50 | 100 L | 3-Bl. Falter 16×11 |
| Jeanneau SO 440 | 4JH45 (45 PS) | SD50 | 150 L | 3-Bl. Falter 17×12 |
| Jeanneau SO 490 | 4JH57 (57 PS) | SD60 | 200 L | 3-Bl. Falter 18×13 |
| Bénéteau Oceanis 34.1 | 2YM20 (21 PS) | SD20 | 50 L | 2-Bl. Falter 14×10 |
| Bénéteau Oceanis 40.1 | 3JH40 (39 PS) | SD50 | 110 L | 3-Bl. Falter 16×11 |
| Bénéteau Oceanis 46.1 | 4JH57 (57 PS) | SD60 | 190 L | 3-Bl. Falter 18×13 |

### 39.4 Hallberg-Rassy (Schweden)

| Bootsmodell | Yanmar-Motor | Saildrive/Getriebe | Tankgröße | Propeller |
|-------------|-------------|-------------------|-----------|-----------|
| HR 340 | 3JH40 (39 PS) | SD50 | 100 L | MaxProp 3-Bl. 16×12 |
| HR 372 | 4JH45 (45 PS) | SD50 | 150 L | MaxProp 3-Bl. 17×13 |
| HR 400 | 4JH57 (57 PS) | SD60 | 200 L | MaxProp 3-Bl. 18×14 |
| HR 44 | 4JH57 (57 PS) | SD60 | 250 L | MaxProp 3-Bl. 18×14 |
| HR 50 | 4JH80 (80 PS) | SD60 | 350 L | MaxProp 3-Bl. 19×15 |
| HR 57 | 4JH110 (110 PS) | KMH61A + Welle | 500 L | MaxProp 3-Bl. 21×16 |

### 39.5 X-Yachts (Dänemark)

| Bootsmodell | Yanmar-Motor | Saildrive/Getriebe | Tankgröße | Propeller |
|-------------|-------------|-------------------|-----------|-----------|
| Xc 35 | 3JH40 (39 PS) | SD50 | 100 L | Flexofold 3-Bl. 16×11 |
| Xc 38 | 4JH45 (45 PS) | SD50 | 130 L | Flexofold 3-Bl. 17×12 |
| Xc 45 | 4JH57 (57 PS) | SD60 | 200 L | Flexofold 3-Bl. 18×14 |
| X4.6 | 4JH57 (57 PS) | SD60 | 180 L | Flexofold 3-Bl. 18×13 |
| X5.6 | 4JH80 (80 PS) | SD60 | 280 L | Flexofold 3-Bl. 19×15 |
| X6.5 | 4JH110 (110 PS) | KMH61A + Welle | 400 L | Gori 3-Bl. 20×16 |

---

## 40. Konservierung und Langzeit-Lagerung

### 40.1 Kurzzeitlagerung (1–3 Monate)

| Maßnahme | Durchführung | Priorität |
|----------|-------------|----------|
| Ölwechsel | Warmes Öl ablassen, neues einfüllen + neuer Filter | HOCH |
| Tank volltanken | Kondenswasserbildung verhindern | HOCH |
| Seeventil schließen | Seewasser absperren | HOCH |
| Batterie | Erhaltungsladung oder abklemmen | MITTEL |
| Motorraum belüften | Lukendeckel leicht geöffnet | MITTEL |

### 40.2 Langzeitlagerung (3–12 Monate)

| Maßnahme | Durchführung | Priorität |
|----------|-------------|----------|
| Alle Maßnahmen der Kurzzeitlagerung | Siehe oben | HOCH |
| Impeller ausbauen | Verhindert Verformung (Set) | HOCH |
| Kühlsystem Frostschutz prüfen | Min. -20 °C | HOCH |
| Kraftstoff-Biozid | Grotamar 82 oder ähnlich | HOCH |
| Motor konservieren | Sprühöl in Ansaug, Motor durchdrehen | HOCH |
| Keilriemen entspannen | Verlängert Riemenlebensdauer | MITTEL |
| Auspuffanlage prüfen | Kondenswasser ablaufen lassen | MITTEL |
| Zink-/Opferanoden prüfen | Bei >50 % Verbrauch tauschen | MITTEL |
| Lichtmaschine abdecken | Vor Feuchtigkeit schützen | NIEDRIG |

### 40.3 Langzeitlagerung (>12 Monate)

| Maßnahme | Durchführung | Priorität |
|----------|-------------|----------|
| Alle Maßnahmen 3–12 Monate | Siehe oben | HOCH |
| Kraftstoff komplett ablassen | Diesel altert, bildet Harze | HOCH |
| Kraftstoff-System mit Konservierungsöl befüllen | Shell Ondina 68 oder Yanmar Fuel System Preserver | HOCH |
| Zylinder konservieren | Sprühöl durch Injektoren-Öffnungen, Motor mehrmals durchdrehen | HOCH |
| Kühlsystem mit 100 % Frostschutz befüllen | Korrosionsschutz über volle Konzentration | HOCH |
| Getriebe-/Saildrive-Öl wechseln | Frisches Öl schützt besser | MITTEL |
| Alle Öffnungen verschließen | Auspuff, Ansaug, Tankbelüftung: mit Klebeband oder Stopfen | MITTEL |
| Regelmäßig (alle 3 Monate) Motor von Hand durchdrehen | Verhindert Festsetzen der Kolbenringe | HOCH |
| Batterie ausbauen und trocken lagern | Alle 2 Monate nachladen | MITTEL |

### 40.4 Wiederinbetriebnahme nach Langzeitlagerung

**Checkliste vor dem ersten Start:**

1. Alle Konservierungsstopfen entfernen (Auspuff, Ansaug, Tankbelüftung)
2. Frischen Kraftstoff einfüllen (mit Biozid)
3. Kraftstoffhahn öffnen, System entlüften
4. Neuen Impeller einsetzen
5. Keilriemen spannen, auf Risse prüfen
6. Ölstand kontrollieren (ggf. Konservierungsöl durch normales ersetzen)
7. Kühlmittelstand prüfen, Mischung auf 50:50 bringen
8. Seeventil öffnen
9. Seewasserfilter reinigen
10. Batterie anschließen (min. 12,4V)
11. Elektrische Verbindungen prüfen (Korrosion?)
12. Getriebe-/Saildrive-Ölstand prüfen
13. Saildrive-Manschette prüfen (bei >7 Jahre: TAUSCHEN!)
14. Motor starten — NICHT sofort Gas geben!
15. Im Leerlauf 10 Minuten warmfahren
16. Seewasser-Austritt am Auspuff kontrollieren
17. Öldruck, Temperatur, Ladung beobachten
18. Vorwärts-/Rückwärtsgang testen (nur bei Boot im Wasser!)
19. Betriebsstundenzähler notieren
20. Bei Auffälligkeiten: SOFORT Motor abstellen und Ursache klären

---

## 41. Service-Kits und Wartungspakete

### 41.1 Yanmar-Original Service-Kits

Yanmar bietet für jede Motorserie vorkonfektionierte Wartungskits:

**GM-Serie Service Kit 250h:**

| Inhalt | Teilenummer | Menge |
|--------|------------|-------|
| Ölfilter | 119305-35151 | 1× |
| Kraftstofffilter | 104500-55710 | 1× |
| O-Ring Ölablassschraube | 128170-01751 | 1× |
| Zinkanode Motorblock | 128370-02210 | 1× |
| **Kit-Teilenummer** | **SKG-250** | |
| **Kit-Preis EUR** | **48–62** | |

**GM-Serie Service Kit 500h:**

| Inhalt | Teilenummer | Menge |
|--------|------------|-------|
| Alles aus 250h-Kit | — | 1× |
| Impeller | 128170-02070 | 1× |
| Impeller-Dichtung | 128170-02060 | 1× |
| Keilriemen | 128170-42440 | 1× |
| **Kit-Teilenummer** | **SKG-500** | |
| **Kit-Preis EUR** | **88–115** | |

**YM-Serie Service Kit 250h:**

| Inhalt | Teilenummer | Menge |
|--------|------------|-------|
| Ölfilter | 119305-35170 | 1× |
| Kraftstofffilter | 104500-55710 | 1× |
| O-Ring Ölablassschraube | 119773-01751 | 1× |
| Zinkanode Motorblock | 119574-44150 | 1× |
| **Kit-Teilenummer** | **SKY-250** | |
| **Kit-Preis EUR** | **55–72** | |

**YM-Serie Service Kit 500h:**

| Inhalt | Teilenummer | Menge |
|--------|------------|-------|
| Alles aus 250h-Kit | — | 1× |
| Impeller | 128990-42200 | 1× |
| Impeller-Dichtung | 128990-42210 | 1× |
| Keilriemen | 119773-42680 | 1× |
| **Kit-Teilenummer** | **SKY-500** | |
| **Kit-Preis EUR** | **102–135** | |

**JH-Serie Service Kit 250h:**

| Inhalt | Teilenummer | Menge |
|--------|------------|-------|
| Ölfilter | 129150-35170 | 1× |
| Kraftstofffilter primär | 129004-55810 | 1× |
| Kraftstofffilter sekundär | 129A00-55800 | 1× |
| O-Ring Ölablassschraube | 129470-01751 | 1× |
| Zinkanode Motorblock | 119574-44150 | 1× |
| Zinkanode Wärmetauscher | 119574-44160 | 1× |
| **Kit-Teilenummer** | **SKJ-250** | |
| **Kit-Preis EUR** | **95–125** | |

**JH-Serie Service Kit 500h:**

| Inhalt | Teilenummer | Menge |
|--------|------------|-------|
| Alles aus 250h-Kit | — | 1× |
| Impeller | 129670-42531 | 1× |
| Impeller-Dichtung | 129670-42540 | 1× |
| Keilriemen | 129612-42290 | 1× |
| **Kit-Teilenummer** | **SKJ-500** | |
| **Kit-Preis EUR** | **165–215** | |

**JH-Serie Service Kit 1.000h:**

| Inhalt | Teilenummer | Menge |
|--------|------------|-------|
| Alles aus 500h-Kit | — | 1× |
| Luftfilter | 129195-12530 | 1× |
| Thermostat | 129470-49801 | 1× |
| Kühlmittel-Konzentrat (2L) | — | 1× |
| **Kit-Teilenummer** | **SKJ-1000** | |
| **Kit-Preis EUR** | **255–335** | |

### 41.2 Aftermarket-Service-Kits

Verschiedene Anbieter bieten kompatible Service-Kits zu günstigeren Preisen:

| Anbieter | Kompatibel mit | Kit-Typ | Preis EUR | Qualität |
|----------|---------------|---------|-----------|---------|
| Solé Diesel Parts | GM/YM/JH | 250h/500h | 30–40 % günstiger | ★★★★ |
| Boat Parts NL | GM/YM/JH | 250h/500h | 25–35 % günstiger | ★★★★ |
| SVB Marine | Alle | 250h–1.000h | 20–30 % günstiger | ★★★★★ |
| Orangemarine | GM/YM | 250h/500h | 35–45 % günstiger | ★★★ |
| Amazon Marine | GM/YM | 250h | 40–50 % günstiger | ★★–★★★ |

**Hinweis:** Bei Aftermarket-Kits auf Markenkomponenten achten (Jabsco/Johnson Impeller, Fleetguard/Mann Filter). No-Name-Impeller und -Filter können zu Problemen führen.

---

## 42. Typische Fehlerkosten und Reparaturzeiten

### 42.1 Reparaturkosten-Übersicht (Werkstatt, inkl. Teile und Arbeit)

| Reparatur | GM/YM-Serie | JH-Serie | LHA/LY-Serie |
|-----------|------------|---------|-------------|
| Impeller-Wechsel | 80–120 EUR | 120–180 EUR | 180–280 EUR |
| Ölwechsel komplett | 120–180 EUR | 180–280 EUR | 280–420 EUR |
| Kraftstofffilter-Wechsel | 60–100 EUR | 100–160 EUR | 140–220 EUR |
| Thermostat-Tausch | 120–180 EUR | 180–280 EUR | 250–380 EUR |
| Wärmetauscher-Reinigung | 250–400 EUR | 400–650 EUR | 600–950 EUR |
| Seewasserpumpe Überholung | 180–300 EUR | 300–480 EUR | 450–700 EUR |
| Injektor-Tausch (1 Stück) | 150–250 EUR | 350–550 EUR | 500–800 EUR |
| Injektor-Satz komplett | 350–600 EUR | 1.200–1.800 EUR | 1.800–3.000 EUR |
| Turbolader-Revision | — | 1.500–2.500 EUR | 2.500–4.000 EUR |
| Zylinderkopfdichtung | 600–900 EUR | 900–1.400 EUR | 1.400–2.200 EUR |
| Motorlager-Satz (4×) | 250–400 EUR | 400–650 EUR | 650–1.000 EUR |
| Saildrive-Manschette | 400–650 EUR | 550–850 EUR | — |
| Anlasser-Tausch | 380–550 EUR | 550–750 EUR | 750–1.000 EUR |
| Lichtmaschine-Tausch | 380–550 EUR | 550–750 EUR | 750–1.000 EUR |
| ECU-Reparatur/Tausch | — | 2.500–4.000 EUR | 3.500–5.500 EUR |
| Generalüberholung | 2.500–4.000 EUR | 5.000–10.000 EUR | 12.000–22.000 EUR |
| Keilriemen-Wechsel | 50–80 EUR | 80–120 EUR | 120–180 EUR |
| Ventilspiel einstellen | 120–200 EUR | 200–320 EUR | 300–480 EUR |
| Auspuffkrümmer-Tausch | 350–600 EUR | 500–850 EUR | 800–1.400 EUR |
| Auspuffmischkammer-Tausch | 250–450 EUR | 400–700 EUR | 600–1.000 EUR |

### 42.2 Typische Reparaturzeiten (Werkstatt-Stunden)

| Reparatur | GM/YM | JH | LHA/LY | Anmerkung |
|-----------|-------|-----|--------|-----------|
| Impeller-Wechsel | 0,5h | 0,75h | 1,0h | Routinearbeit |
| Ölwechsel komplett | 0,75h | 1,0h | 1,5h | Inkl. Filterabfuhr |
| Thermostat-Tausch | 1,0h | 1,5h | 2,0h | Je nach Zugänglichkeit |
| Wärmetauscher-Reinigung | 2,0h | 3,0h | 4,0h | Zerlegen, reinigen, zusammenbauen |
| Seewasserpumpe Überholung | 1,5h | 2,0h | 3,0h | Dichtungen, Lager, Impeller |
| Injektor-Tausch (1 Stück) | 1,0h | 1,5h | 2,0h | GM/YM mechanisch einfacher |
| Injektor-Satz komplett | 2,0h | 4,0h | 6,0h | JH: Kalibrierung nötig |
| Turbolader-Revision | — | 4,0h | 6,0h | Exkl. Turbo-Aufarbeitung |
| Zylinderkopfdichtung | 6,0h | 8,0h | 12,0h | Aufwändig, Drehmomentwerte |
| Motorlager-Satz + Ausrichten | 3,0h | 4,0h | 6,0h | Inkl. Fluchtungsmessung |
| Saildrive-Manschette | 4,0h | 5,0h | — | Boot muss aus dem Wasser |
| Generalüberholung | 20–30h | 30–50h | 50–80h | Je nach Umfang |
| Kompletter Motorwechsel | 15–20h | 20–35h | 35–50h | Inkl. Anpassung, Probefahrt |

### 42.3 Werkstatt-Stundensätze (Richtwerte DE, 2025/26)

| Werkstatt-Typ | Stundensatz EUR | Region |
|--------------|----------------|--------|
| Yanmar-Vertragswerkstatt | 95–130 | Durchschnitt DE |
| Freie Marine-Werkstatt | 75–110 | Durchschnitt DE |
| Werft mit Motorservice | 85–125 | Küste/Binnenrevier |
| Mobile Motorservice-Techniker | 80–120 + Anfahrt | Variabel |

---

## 43. Häufige Suchbegriffe und Modellbezeichnungen — Querverweise

### 43.1 Modell-Querverweistabelle (alte → neue Bezeichnung)

| Alte Bezeichnung | Aktuelle Bezeichnung | Anmerkung |
|-----------------|---------------------|-----------|
| 1GM10 | — (Auslauf) | Nachfolger: 1YM15 |
| 2GM20 | — (Auslauf) | Nachfolger: 2YM20 |
| 2GM20F | — (Auslauf) | F = Festpropeller, Nachfolger: 2YM20 |
| 3GM30 | — (Auslauf) | Nachfolger: 3YM30 |
| 3GM30F | — (Auslauf) | Nachfolger: 3YM30 |
| 3JH25A | — (Auslauf) | Nachfolger: 3JH40 |
| 3JH30A | — (Auslauf) | Nachfolger: 3JH40 |
| 4JH2E | — (Auslauf) | Nachfolger: 4JH45 |
| 4JH3E | — (Auslauf) | Nachfolger: 4JH45 |
| 4JH4E | — (Auslauf) | Nachfolger: 4JH57 |
| 4JH4-HTE | — (Auslauf) | Nachfolger: 4JH57 |
| 4JH5E | — (Auslauf) | Nachfolger: 4JH80 |
| 4JH4-TE | — (Auslauf) | Nachfolger: 4JH80 |
| 4LHA-STE | 4LHA-STP | Umbenennung |
| 4LHA-DTE | 4LHA-DTP | Umbenennung |
| 4LHA-HTE | — (Auslauf) | Nachfolger: 4LHA-DTP |
| 6LP-STE | 6LPA-STP2 | Umbenennung/Nachfolger |
| 6LPA-STE2 | 6LPA-STP2 | Umbenennung |
| 6LY2A-STP | 6LY-STP | Vereinfacht |
| 6LY2A-UTP | 6LY-UTP | Vereinfacht |

### 43.2 Saildrive-Kompatibilitätsmatrix (komplett)

| Saildrive | 1GM10 | 2GM20 | 3GM30 | 1YM15 | 2YM15 | 2YM20 | 3YM20 | 3YM30 | 3JH40 | 4JH45 | 4JH57 | 4JH80 | 4JH110 |
|-----------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|--------|
| SD20 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | — | — | — | — | — | — |
| SD25 | — | — | — | — | — | — | — | ✓ | ✓* | — | — | — | — |
| SD50 | — | — | — | — | — | — | — | — | ✓ | ✓ | ✓* | — | — |
| SD60 | — | — | — | — | — | — | — | — | — | — | ✓ | ✓ | ✓ |

✓ = Standardkonfiguration, ✓* = grenzwertig, empfohlene Aufrüstung auf nächstgrößeren SD

### 43.3 Seriennummern-Schema

Yanmar-Seriennummern auf dem Typenschild folgen dem Format:

```
[Modell]-[Produktionswerk][Laufende Nummer]

Beispiele:
  4JH57-A1234567    → 4JH57, Werk Amagasaki, Nummer 1234567
  3YM30-A0567890    → 3YM30, Werk Amagasaki, Nummer 567890
  4LHA-DTP-B0123456 → 4LHA-DTP, Werk Biwa, Nummer 123456
```

**Produktionswerk-Codes:**
- A = Amagasaki (GM, YM, JH)
- B = Biwa (LHA, LY)
- M = Maibara (BY)
- E = Europa (Anpassung/Endmontage)

Das Typenschild befindet sich:
- GM/YM: Auf dem Zylinderblock, seitlich (Steuerbordseite)
- JH: Auf dem Ventildeckel oder seitlich am Block
- LHA/LY/BY: Auf der Steuerbordseite des Blocks, auf Höhe der Einspritzpumpe

---

> **AYDI-Hinweis:** Diese Wissensdatei wird als Referenz für die Module Compliance, Kosten, Produktion und Service-Patterns verwendet. Alle technischen Daten basieren auf Herstellerangaben (confidence: measured). Preisangaben sind UVP-Richtwerte und können regional abweichen (confidence: estimated). Schwachstellenbewertungen basieren auf dokumentierten Erfahrungswerten und Eignerfeedback (confidence: documented/estimated).

---

*Letzte Prüfung: 2026-04 | AYDI Maritime Knowledge Base v2.0*
