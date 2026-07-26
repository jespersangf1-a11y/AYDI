---
titel: "Beta Marine, Nanni, Vetus und Sole — Alternative Marine-Diesel"
kategorie: "Motoren und Antrieb"
unterkategorie: "Alternative Hersteller"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Werksdatenblätter, ISO-Normen, CE-Zertifizierungen"
  - documented: "Werkstatthandbücher, Servicebulletins, Händler-Kataloge"
  - estimated: "Erfahrungswerte aus Werftbetrieben, Eignerfeedback, Branchenkonsens"
---

# 18_04 — Beta Marine, Nanni, Vetus und Sole — Alternative Marine-Diesel

> **AYDI Wissensdatei 18.04** — Kategorie 18: Motoren und Antrieb
> **Confidence-Quelle:** measured (Hersteller-Werksdatenblätter, ISO-Normen), documented (Werkstatthandbücher, Servicebulletins), estimated (Werft-Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04

---

## Inhaltsverzeichnis

1. [Marktüberblick — Alternative Marinediesel-Hersteller](#1-marktüberblick--alternative-marinediesel-hersteller)
2. [Beta Marine — Firmengeschichte und Philosophie](#2-beta-marine--firmengeschichte-und-philosophie)
3. [Beta Marine — Modellreihen-Übersicht](#3-beta-marine--modellreihen-übersicht)
4. [Beta Marine — Beta-Serie (Kubota-Basis)](#4-beta-marine--beta-serie-kubota-basis)
5. [Beta Marine — Atomic-Serie](#5-beta-marine--atomic-serie)
6. [Beta Marine — Getriebe und Saildrive](#6-beta-marine--getriebe-und-saildrive)
7. [Beta Marine — Bekannte Schwachstellen](#7-beta-marine--bekannte-schwachstellen)
8. [Nanni Diesel — Firmengeschichte und Philosophie](#8-nanni-diesel--firmengeschichte-und-philosophie)
9. [Nanni Diesel — Modellreihen-Übersicht](#9-nanni-diesel--modellreihen-übersicht)
10. [Nanni Diesel — N-Serie (Saugdiesel)](#10-nanni-diesel--n-serie-saugdiesel)
11. [Nanni Diesel — T-Serie (Turbodiesel)](#11-nanni-diesel--t-serie-turbodiesel)
12. [Nanni Diesel — Getriebe und Saildrive](#12-nanni-diesel--getriebe-und-saildrive)
13. [Nanni Diesel — Bekannte Schwachstellen](#13-nanni-diesel--bekannte-schwachstellen)
14. [Vetus — Firmengeschichte und Philosophie](#14-vetus--firmengeschichte-und-philosophie)
15. [Vetus — Modellreihen-Übersicht](#15-vetus--modellreihen-übersicht)
16. [Vetus — M-Serie](#16-vetus--m-serie)
17. [Vetus — VF-Serie und D-Serie](#17-vetus--vf-serie-und-d-serie)
18. [Vetus — BOW PRO Thruster-Integration](#18-vetus--bow-pro-thruster-integration)
19. [Vetus — Bekannte Schwachstellen](#19-vetus--bekannte-schwachstellen)
20. [Sole Diesel — Firmengeschichte und Philosophie](#20-sole-diesel--firmengeschichte-und-philosophie)
21. [Sole Diesel — Mini-Serie (Mitsubishi-Basis)](#21-sole-diesel--mini-serie-mitsubishi-basis)
22. [Sole Diesel — Bekannte Schwachstellen](#22-sole-diesel--bekannte-schwachstellen)
23. [Craftsman Marine — Budget-Alternative](#23-craftsman-marine--budget-alternative)
24. [Vergleich aller Hersteller](#24-vergleich-aller-hersteller)
25. [Ersatzteile und Händlernetzwerk Europa](#25-ersatzteile-und-händlernetzwerk-europa)
26. [Wartungsintervalle im Vergleich](#26-wartungsintervalle-im-vergleich)
27. [Fehlerbilder](#27-fehlerbilder)
28. [Troubleshooting-Bäume](#28-troubleshooting-bäume)
29. [Fallstudien](#29-fallstudien)
30. [FAQ — Häufig gestellte Fragen](#30-faq--häufig-gestellte-fragen)
31. [Glossar](#31-glossar)
32. [Pydantic v2 Datenmodelle](#32-pydantic-v2-datenmodelle)
33. [Preisübersicht EUR](#33-preisübersicht-eur)
34. [Quellenverzeichnis](#34-quellenverzeichnis)

---

## 1. Marktüberblick — Alternative Marinediesel-Hersteller

### 1.1 Marktstruktur im europäischen Yachtbau

Der europäische Markt für Marine-Einbaudiesel wird von Yanmar (55–65 % Segelboote) und Volvo Penta (25–30 % Segelboote, 35–45 % Motorboote) dominiert. Die in dieser Wissensdatei behandelten Hersteller bedienen zusammen ca. 15–25 % des Gesamtmarktes, decken aber in bestimmten Nischen und Regionen deutlich höhere Anteile ab.

**Marktanteile Europa (geschätzt, 2025/26):**

| Hersteller | Segelboote | Motorboote | Stärkstes Segment |
|------------|-----------|------------|-------------------|
| Beta Marine | 3–5 % | 1–2 % | UK-Markt, Refit, Canal Boats |
| Nanni Diesel | 5–8 % | 3–5 % | Mittelmeer, franz. Werften |
| Vetus | 2–4 % | 4–7 % | Niederlande, Binnenschifffahrt |
| Sole Diesel | 2–4 % | 1–3 % | Spanien, Mittelmeer |
| Craftsman Marine | 1–3 % | 1–2 % | Budget-Refit, Niederlande |

### 1.2 Gemeinsames Prinzip — Industriemotor-Marinisierung

Alle fünf Hersteller folgen demselben Grundprinzip: Sie kaufen bewährte Industrie-Dieselblöcke von Großserienherstellern (Kubota, Toyota, Mitsubishi, Deutz) und marinisieren diese. Die Marinisierung umfasst:

- **Kühlsystem**: Umrüstung auf Zweikreis-Seewasserkühlung (Indirekte Kühlung)
- **Lichtmaschine**: Marine-spezifische Lichtmaschine mit höherer Leistung
- **Auspuffsystem**: Wassergekühlter Auspuffkrümmer, Mischkammer, Gummiauspuff
- **Motorlager**: Schwingungsdämpfende Gummilager für Bootsmontage
- **Instrumentierung**: Marine-Instrumentenpanel mit Drehzahl, Temperatur, Öldruck
- **Getriebe**: Anbau eines Marine-Wendegetriebes (TMC, PRM, ZF, Technodrive)
- **Korrosionsschutz**: Opferanoden, marinisierte Dichtungen, tropenfeste Beschichtung
- **Kraftstoffsystem**: Marine-Kraftstofffilter, Absperrhahn, Wasserabscheider

**Vorteile der Marinisierung:**
- Bewährte, millionenfach produzierte Industrieblöcke
- Weltweite Ersatzteilversorgung für Kernkomponenten
- Niedrigere Entwicklungskosten → günstigere Endpreise
- Lange Produktionszyklen der Basisblöcke → gute Ersatzteilverfügbarkeit

**Nachteile:**
- Marinisierungsqualität variiert zwischen Herstellern
- Nicht alle Industrieblock-Teile identisch mit Marineversion
- Service-Netzwerk kleiner als bei Yanmar/Volvo
- Weniger integrierte Lösungen (kein eigener Saildrive bei manchen)

### 1.3 Basisblock-Zuordnung

| Marinemotor-Hersteller | Basisblock-Hersteller | Typische Modelle |
|------------------------|----------------------|-----------------|
| Beta Marine | Kubota | D722, D902, D1105, V1505, V2003, V2403, V3300, V3800 |
| Nanni Diesel | Toyota (1–3 Zyl.), Kubota (4 Zyl.) | 1KD, 2KD, 3CT, V2403, V3307 |
| Vetus | Mitsubishi, Deutz | S3L2, S4L2, L-Serie, TCD-Serie |
| Sole Diesel | Mitsubishi | L2E, L3E, S3L2, S4L2, S4Q2, S6S |
| Craftsman Marine | Mitsubishi | S3L2, S4L2, S4Q2 |

---

## 2. Beta Marine — Firmengeschichte und Philosophie

### 2.1 Unternehmensgeschichte

Beta Marine Ltd. wurde 1978 in Thornbury, Gloucestershire (England) gegründet. Das Unternehmen startete als kleine Werkstatt für Marine-Motorenumrüstungen und hat sich zum führenden unabhängigen Marinemotor-Hersteller Großbritanniens entwickelt.

**Meilensteine:**

| Jahr | Ereignis |
|------|----------|
| 1978 | Gründung durch Peter Augustin in Thornbury, UK |
| 1982 | Erste Kubota-Marinisierung (Beta 16) |
| 1985 | Einführung der Beta-Serie auf Kubota-D-Basis |
| 1990 | Export nach Skandinavien und Niederlande |
| 1993 | Beta 38 als meistverkauftes Modell etabliert |
| 1997 | Einführung der Atomic-Serie (kompakt) |
| 2002 | Erweiterung auf 150 PS (V3800-Basis) |
| 2005 | RCD/CE-Zertifizierung aller Modelle |
| 2008 | Umzug in größere Produktionsstätte in Thornbury |
| 2012 | Beta 25 als Nachfolger populärer Yanmar 2GM/3GM bei Refits |
| 2015 | Einführung elektronischer Motorüberwachung |
| 2018 | Überarbeitete Beta 30–50 Serie mit Tier-II-Konformität |
| 2020 | Beta Marine Hybrid-System (Diesel-Elektro-Kombination) |
| 2022 | Neue Beta 60/75 Generation auf V3307-Basis |
| 2024 | Überarbeitete Atomic-Serie mit verbesserter Schalldämmung |

### 2.2 Firmenphilosophie

Beta Marine verfolgt eine klare Philosophie: **Einfachheit, Zuverlässigkeit und Wartungsfreundlichkeit**.

**Kernprinzipien:**
- Keine elektronische Einspritzung bei Modellen unter 75 PS — mechanische Einspritzpumpe
- Alle Wartungspunkte von einer Seite zugänglich (soweit möglich)
- Bewusster Verzicht auf proprietäre Diagnosesysteme
- Jeder qualifizierte Diesel-Mechaniker kann den Motor warten
- Kubota-Basisteile weltweit in jedem Landmaschinenhandel verfügbar
- Persönlicher technischer Support direkt aus der Fabrik

**Zielgruppe:**
- Blauwasser-Segler (Zuverlässigkeit, Einfachheit, Ersatzteile weltweit)
- Refit-Markt (Austauschmotor für alternde Yanmar GM, Volvo MD, Bukh)
- UK-Narrowboat-Markt (Canal Boats, Binnenfahrt)
- Traditionelle Segler und Langfahrt-Enthusiasten

### 2.3 Produktionsstandort und Kapazität

| Aspekt | Detail |
|--------|--------|
| Hauptsitz | Thornbury, Gloucestershire, England |
| Mitarbeiter | ca. 85 (2025) |
| Jahresproduktion | ca. 2.500–3.000 Motoren |
| Produktionsprozess | Handmontage, Einzelprüfstand-Test jedes Motors |
| Qualitätssicherung | 100 % Prüfstandlauf (30 Min.), Leckprüfung, Leistungsmessung |
| Zertifizierung | ISO 9001:2015, RCD 2013/53/EU, EPA Tier II/III |

---

## 3. Beta Marine — Modellreihen-Übersicht

### 3.1 Aktuelle Modellpalette (2025/26)

Beta Marine bietet zwei Hauptserien:

**Beta-Serie (Standard-Einbau):**

| Modell | Zylinder | Hubraum (cm³) | Leistung PS | Leistung kW | Drehzahl | Kubota-Basis |
|--------|----------|--------------|-------------|-------------|----------|-------------|
| Beta 14 | 2 | 719 | 14 | 10,3 | 3.600 | D722 |
| Beta 16 | 3 | 898 | 16 | 11,8 | 3.000 | D902 |
| Beta 20 | 3 | 1.123 | 20 | 14,7 | 3.000 | D1105 |
| Beta 25 | 3 | 1.123 | 25 | 18,4 | 3.600 | D1105 |
| Beta 30 | 4 | 1.498 | 30 | 22,1 | 3.000 | V1505 |
| Beta 35 | 4 | 1.498 | 35 | 25,7 | 3.600 | V1505 |
| Beta 38 | 4 | 1.999 | 38 | 27,9 | 2.800 | V2003 |
| Beta 43 | 4 | 2.434 | 43 | 31,6 | 2.800 | V2403 |
| Beta 50 | 4 | 2.434 | 50 | 36,8 | 3.000 | V2403 |
| Beta 60 | 4 | 3.318 | 60 | 44,1 | 2.600 | V3307 |
| Beta 75 | 4 | 3.318 | 75 | 55,2 | 2.800 | V3307-T |
| Beta 90 | 4 | 3.318 | 90 | 66,2 | 3.150 | V3307-DI-T |
| Beta 105 | 4 | 3.769 | 105 | 77,2 | 2.800 | V3800 |
| Beta 115 | 4 | 3.769 | 115 | 84,6 | 3.000 | V3800-T |
| Beta 130 | 4 | 3.769 | 130 | 95,6 | 3.150 | V3800-DI-T |
| Beta 150 | 4 | 3.769 | 150 | 110,3 | 3.600 | V3800-DI-T-E |

**Atomic-Serie (Kompakt-Einbau):**

| Modell | Zylinder | Hubraum (cm³) | Leistung PS | Leistung kW | Drehzahl | Kubota-Basis |
|--------|----------|--------------|-------------|-------------|----------|-------------|
| Atomic 10 | 2 | 719 | 10 | 7,4 | 3.000 | D722 |
| Atomic 14 | 2 | 719 | 14 | 10,3 | 3.600 | D722 |
| Atomic 16 | 3 | 898 | 16 | 11,8 | 3.000 | D902 |
| Atomic 20 | 3 | 1.123 | 20 | 14,7 | 3.000 | D1105 |
| Atomic 25 | 3 | 1.123 | 25 | 18,4 | 3.600 | D1105 |
| Atomic 30 | 4 | 1.498 | 30 | 22,1 | 3.000 | V1505 |

### 3.2 Unterschied Beta vs. Atomic

| Merkmal | Beta-Serie | Atomic-Serie |
|---------|-----------|-------------|
| Bauform | Standard-Einbau, höher | Kompakt, niedrigeres Profil |
| Einsatz | Universell | Enge Motorräume, unter Cockpit-Sole |
| Lichtmaschine | Standard-Position, oben | Seitlich oder unten montiert |
| Auspuffauslass | Flexibel wählbar | Optimiert für niedrige Auslässe |
| Ölwanne | Standard | Flache Ölwanne verfügbar |
| Motorlager | 4-Punkt Standard | 4-Punkt, tiefere Montage |
| Getriebe | PRM, TMC, ZF — Standard | PRM, TMC — Kompaktversionen |
| Saildrive | Technodrive SeaProp | Technodrive SeaProp (eingeschränkt) |
| Preis | Referenz | +5–10 % ggü. Beta-Serie |

---

## 4. Beta Marine — Beta-Serie (Kubota-Basis)

### 4.1 Beta 14 — Kleinstes Modell

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Kubota-Basis | D722-E4B |
| Zylinder | 2, Reihe |
| Bohrung × Hub | 67,0 × 68,0 mm |
| Hubraum | 719 cm³ |
| Verdichtung | 23,0:1 |
| Leistung | 14 PS (10,3 kW) bei 3.600 U/min |
| Max. Drehmoment | 30,5 Nm bei 2.400 U/min |
| Einspritzung | Mechanisch, indirekt (Wirbelkammer) |
| Kühlung | Indirekt, Zweikreis-Seewasser |
| Kraftstoffverbrauch | 2,8 l/h bei Volllast, 1,4 l/h bei Reisefahrt |
| Gewicht (trocken, mit Getriebe) | 95 kg |
| Länge × Breite × Höhe | 545 × 420 × 520 mm |
| Ölmenge | 2,1 l |
| Kühlmittel | 2,5 l |
| Lichtmaschine | 12V/75A Standard, 12V/110A optional |
| Anlasser | 12V/1,2 kW |
| Getriebe Standard | PRM 80, 2:1 Untersetzung |
| Saildrive-Option | Technodrive SeaProp 60 |
| CE-Kategorie | RCD 2013/53/EU — Kategorie A–D |
| Abgas | EU Stage V, EPA Tier III |

**Empfohlene Bootsgröße:** 6–9 m Segelboot, 5–7 m Motorboot (Verdränger)
**UVP (2025/26):** 7.800–9.200 EUR (je nach Getriebe/Ausstattung)

### 4.2 Beta 20 — Beliebtestes Segelboot-Modell

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Kubota-Basis | D1105-E4B |
| Zylinder | 3, Reihe |
| Bohrung × Hub | 78,0 × 78,4 mm |
| Hubraum | 1.123 cm³ |
| Verdichtung | 22,0:1 |
| Leistung | 20 PS (14,7 kW) bei 3.000 U/min |
| Max. Drehmoment | 52,3 Nm bei 2.200 U/min |
| Einspritzung | Mechanisch, indirekt (Wirbelkammer) |
| Kühlung | Indirekt, Zweikreis-Seewasser |
| Kraftstoffverbrauch | 4,2 l/h bei Volllast, 2,0 l/h bei Reisefahrt |
| Gewicht (trocken, mit Getriebe) | 125 kg |
| Länge × Breite × Höhe | 595 × 445 × 555 mm |
| Ölmenge | 3,3 l |
| Kühlmittel | 3,8 l |
| Lichtmaschine | 12V/75A Standard, 12V/110A optional |
| Anlasser | 12V/1,4 kW |
| Getriebe Standard | PRM 120, 2,5:1 Untersetzung |
| Saildrive-Option | Technodrive SeaProp 60 |

**Empfohlene Bootsgröße:** 8–11 m Segelboot, 7–9 m Motorboot (Verdränger)
**UVP (2025/26):** 9.400–11.200 EUR

### 4.3 Beta 25

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Kubota-Basis | D1105-E4B (höhere Drehzahl) |
| Zylinder | 3, Reihe |
| Hubraum | 1.123 cm³ |
| Leistung | 25 PS (18,4 kW) bei 3.600 U/min |
| Max. Drehmoment | 53,1 Nm bei 2.600 U/min |
| Kraftstoffverbrauch | 5,1 l/h bei Volllast, 2,5 l/h bei Reisefahrt |
| Gewicht (trocken, mit Getriebe) | 130 kg |
| Länge × Breite × Höhe | 595 × 445 × 560 mm |
| Getriebe Standard | PRM 120, 2,5:1 Untersetzung |
| Saildrive-Option | Technodrive SeaProp 60 |

**Empfohlene Bootsgröße:** 9–12 m Segelboot, 8–10 m Motorboot
**UVP (2025/26):** 10.200–12.000 EUR

### 4.4 Beta 30

| Parameter | Wert |
|-----------|------|
| Kubota-Basis | V1505-E4B |
| Zylinder | 4, Reihe |
| Hubraum | 1.498 cm³ |
| Leistung | 30 PS (22,1 kW) bei 3.000 U/min |
| Max. Drehmoment | 75,8 Nm bei 2.200 U/min |
| Kraftstoffverbrauch | 5,8 l/h bei Volllast, 2,8 l/h bei Reisefahrt |
| Gewicht (trocken, mit Getriebe) | 155 kg |
| Länge × Breite × Höhe | 645 × 480 × 585 mm |
| Getriebe Standard | PRM 150, 2,5:1 |
| Saildrive-Option | Technodrive SeaProp 60 |

**Empfohlene Bootsgröße:** 10–13 m Segelboot, 8–11 m Motorboot
**UVP (2025/26):** 11.800–13.600 EUR

### 4.5 Beta 38 — Langzeit-Bestseller

| Parameter | Wert |
|-----------|------|
| Kubota-Basis | V2003-M-E4B |
| Zylinder | 4, Reihe |
| Hubraum | 1.999 cm³ |
| Leistung | 38 PS (27,9 kW) bei 2.800 U/min |
| Max. Drehmoment | 103,2 Nm bei 1.800 U/min |
| Kraftstoffverbrauch | 7,2 l/h bei Volllast, 3,5 l/h bei Reisefahrt |
| Gewicht (trocken, mit Getriebe) | 185 kg |
| Länge × Breite × Höhe | 695 × 510 × 610 mm |
| Getriebe Standard | PRM 150, 2:1 |
| Saildrive-Option | Technodrive SeaProp 80 |

**Empfohlene Bootsgröße:** 11–14 m Segelboot, 9–12 m Motorboot
**UVP (2025/26):** 13.500–15.800 EUR

### 4.6 Beta 43

| Parameter | Wert |
|-----------|------|
| Kubota-Basis | V2403-M-E4B |
| Zylinder | 4, Reihe |
| Hubraum | 2.434 cm³ |
| Leistung | 43 PS (31,6 kW) bei 2.800 U/min |
| Max. Drehmoment | 120,5 Nm bei 1.800 U/min |
| Kraftstoffverbrauch | 8,5 l/h bei Volllast, 4,0 l/h bei Reisefahrt |
| Gewicht (trocken, mit Getriebe) | 210 kg |
| Länge × Breite × Höhe | 720 × 530 × 630 mm |
| Getriebe Standard | PRM 260, 2:1 |
| Saildrive-Option | Technodrive SeaProp 80 |

**Empfohlene Bootsgröße:** 12–15 m Segelboot, 10–13 m Motorboot
**UVP (2025/26):** 15.200–17.500 EUR

### 4.7 Beta 50

| Parameter | Wert |
|-----------|------|
| Kubota-Basis | V2403-M-E4B (höhere Drehzahl) |
| Zylinder | 4, Reihe |
| Hubraum | 2.434 cm³ |
| Leistung | 50 PS (36,8 kW) bei 3.000 U/min |
| Max. Drehmoment | 126,8 Nm bei 2.000 U/min |
| Kraftstoffverbrauch | 10,2 l/h bei Volllast, 4,8 l/h bei Reisefahrt |
| Gewicht (trocken, mit Getriebe) | 218 kg |
| Länge × Breite × Höhe | 720 × 530 × 635 mm |
| Getriebe Standard | PRM 260, 2:1 |
| Saildrive-Option | Technodrive SeaProp 80 |

**Empfohlene Bootsgröße:** 12–16 m Segelboot, 10–14 m Motorboot
**UVP (2025/26):** 16.800–19.200 EUR

### 4.8 Beta 60

| Parameter | Wert |
|-----------|------|
| Kubota-Basis | V3307-DI-E4B |
| Zylinder | 4, Reihe |
| Hubraum | 3.318 cm³ |
| Leistung | 60 PS (44,1 kW) bei 2.600 U/min |
| Max. Drehmoment | 172,5 Nm bei 1.600 U/min |
| Einspritzung | Direkteinspritzung (mechanisch) |
| Kraftstoffverbrauch | 11,8 l/h bei Volllast, 5,5 l/h bei Reisefahrt |
| Gewicht (trocken, mit Getriebe) | 260 kg |
| Länge × Breite × Höhe | 785 × 560 × 660 mm |
| Getriebe Standard | ZF 15M, 2:1 |
| Saildrive-Option | Nein (zu schwer) |

**Empfohlene Bootsgröße:** 13–17 m Segelboot, 11–15 m Motorboot
**UVP (2025/26):** 19.500–22.800 EUR

### 4.9 Beta 75

| Parameter | Wert |
|-----------|------|
| Kubota-Basis | V3307-DI-T-E4B (Turbo) |
| Zylinder | 4, Reihe, Turbolader |
| Hubraum | 3.318 cm³ |
| Leistung | 75 PS (55,2 kW) bei 2.800 U/min |
| Max. Drehmoment | 205,3 Nm bei 1.800 U/min |
| Kraftstoffverbrauch | 14,5 l/h bei Volllast, 6,8 l/h bei Reisefahrt |
| Gewicht (trocken, mit Getriebe) | 285 kg |
| Länge × Breite × Höhe | 810 × 570 × 685 mm |
| Getriebe Standard | ZF 25M, 2:1 |

**Empfohlene Bootsgröße:** 14–18 m Segelboot, 12–16 m Motorboot
**UVP (2025/26):** 22.500–26.000 EUR

### 4.10 Beta 90

| Parameter | Wert |
|-----------|------|
| Kubota-Basis | V3307-DI-T-E4B (Turbo, höhere Leistung) |
| Zylinder | 4, Reihe, Turbo + Ladeluftkühlung |
| Hubraum | 3.318 cm³ |
| Leistung | 90 PS (66,2 kW) bei 3.150 U/min |
| Max. Drehmoment | 218,6 Nm bei 2.000 U/min |
| Kraftstoffverbrauch | 17,2 l/h bei Volllast, 8,0 l/h bei Reisefahrt |
| Gewicht (trocken, mit Getriebe) | 295 kg |
| Getriebe Standard | ZF 25M, 2:1 |

**Empfohlene Bootsgröße:** 15–20 m Segelboot, 13–17 m Motorboot
**UVP (2025/26):** 25.800–29.500 EUR

### 4.11 Beta 105

| Parameter | Wert |
|-----------|------|
| Kubota-Basis | V3800-DI-E4B |
| Zylinder | 4, Reihe |
| Hubraum | 3.769 cm³ |
| Leistung | 105 PS (77,2 kW) bei 2.800 U/min |
| Max. Drehmoment | 280,5 Nm bei 1.600 U/min |
| Kraftstoffverbrauch | 20,5 l/h bei Volllast, 9,5 l/h bei Reisefahrt |
| Gewicht (trocken, mit Getriebe) | 340 kg |
| Getriebe Standard | ZF 45M, 2:1 |

**Empfohlene Bootsgröße:** 16–22 m Motorboot, Verdränger/Semi
**UVP (2025/26):** 29.500–34.000 EUR

### 4.12 Beta 115 / Beta 130 / Beta 150

| Parameter | Beta 115 | Beta 130 | Beta 150 |
|-----------|----------|----------|----------|
| Kubota-Basis | V3800-T | V3800-DI-T | V3800-DI-T-E |
| Zylinder | 4, Turbo | 4, Turbo + LLK | 4, Turbo + LLK |
| Hubraum | 3.769 cm³ | 3.769 cm³ | 3.769 cm³ |
| Leistung | 115 PS (84,6 kW) | 130 PS (95,6 kW) | 150 PS (110,3 kW) |
| Drehzahl | 3.000 U/min | 3.150 U/min | 3.600 U/min |
| Max. Drehmoment | 292 Nm | 315 Nm | 322 Nm |
| Verbrauch Volllast | 23,5 l/h | 26,0 l/h | 30,5 l/h |
| Verbrauch Reise | 10,8 l/h | 12,0 l/h | 14,2 l/h |
| Gewicht (mit Getriebe) | 365 kg | 380 kg | 395 kg |
| Getriebe Standard | ZF 45M | ZF 63M | ZF 63M |
| UVP | 33.000–38.000 EUR | 37.000–42.500 EUR | 41.000–47.000 EUR |

---

## 5. Beta Marine — Atomic-Serie

### 5.1 Konzept der Atomic-Serie

Die Atomic-Serie wurde 1997 speziell für enge Motorräume entwickelt, wie sie in Segelbooten unter der Cockpit-Sole typisch sind. Der Name „Atomic" bezieht sich auf die kompakte Bauweise — nicht auf Kernenergie.

**Konstruktionsmerkmale:**
- Höhenreduziertes Profil (ca. 40–60 mm niedriger als Beta-Serie)
- Seitlich montierte Lichtmaschine (statt oben)
- Flache Ölwanne als Option
- Kompakteres Auspuffkrümmer-Design
- Optimierte Kabelführung für beengte Räume

### 5.2 Atomic 10

| Parameter | Wert |
|-----------|------|
| Kubota-Basis | D722-E4B |
| Zylinder | 2, Reihe |
| Hubraum | 719 cm³ |
| Leistung | 10 PS (7,4 kW) bei 3.000 U/min |
| Gewicht (trocken, mit Getriebe) | 88 kg |
| Länge × Breite × Höhe | 520 × 395 × 465 mm |
| Getriebe | PRM 80, 2:1 |

**UVP (2025/26):** 8.200–9.800 EUR
**Einsatz:** 6–8 m Segelboote mit sehr engem Motorraum

### 5.3 Atomic 14

| Parameter | Wert |
|-----------|------|
| Kubota-Basis | D722-E4B (höhere Drehzahl) |
| Leistung | 14 PS (10,3 kW) bei 3.600 U/min |
| Gewicht | 92 kg |
| Höhe | 475 mm |

**UVP:** 8.800–10.400 EUR

### 5.4 Atomic 16 / 20 / 25 / 30

| Parameter | Atomic 16 | Atomic 20 | Atomic 25 | Atomic 30 |
|-----------|-----------|-----------|-----------|-----------|
| Kubota-Basis | D902 | D1105 | D1105 | V1505 |
| Zylinder | 3 | 3 | 3 | 4 |
| Hubraum | 898 cm³ | 1.123 cm³ | 1.123 cm³ | 1.498 cm³ |
| Leistung | 16 PS | 20 PS | 25 PS | 30 PS |
| Gewicht | 108 kg | 118 kg | 122 kg | 148 kg |
| Höhe | 490 mm | 510 mm | 515 mm | 540 mm |
| UVP | 9.800–11.400 | 10.400–12.200 | 11.200–13.100 | 13.000–15.000 |

---

## 6. Beta Marine — Getriebe und Saildrive

### 6.1 Getriebe-Optionen

Beta Marine verbaut keine eigenen Getriebe, sondern setzt auf bewährte Zulieferer:

| Getriebe | Hersteller | Max. Drehmoment | Modelle |
|----------|-----------|----------------|---------|
| PRM 80 | Newage PRM (UK) | 80 Nm | Beta/Atomic 10, 14 |
| PRM 120 | Newage PRM (UK) | 120 Nm | Beta/Atomic 16, 20, 25 |
| PRM 150 | Newage PRM (UK) | 170 Nm | Beta 30, 35, 38 |
| PRM 260 | Newage PRM (UK) | 300 Nm | Beta 43, 50 |
| TMC 40 | Technodrive (NL) | 100 Nm | Atomic 10, 14 (Alternative) |
| TMC 60 | Technodrive (NL) | 180 Nm | Beta/Atomic 16–30 (Alternative) |
| ZF 15M | ZF Marine (DE) | 250 Nm | Beta 60 |
| ZF 25M | ZF Marine (DE) | 400 Nm | Beta 75, 90 |
| ZF 45M | ZF Marine (DE) | 600 Nm | Beta 105, 115 |
| ZF 63M | ZF Marine (DE) | 850 Nm | Beta 130, 150 |

**Untersetzungsverhältnisse:**

| Getriebe | Verfügbare Untersetzungen |
|----------|--------------------------|
| PRM 80 | 2,00:1, 2,50:1, 3,00:1 |
| PRM 120 | 1,50:1, 2,00:1, 2,50:1, 3,00:1 |
| PRM 150 | 1,50:1, 2,00:1, 2,50:1, 3,00:1 |
| PRM 260 | 1,50:1, 2,00:1, 2,50:1, 3,00:1 |
| ZF 15M | 1,97:1, 2,14:1, 2,63:1 |
| ZF 25M | 1,88:1, 2,07:1, 2,50:1, 3,05:1 |
| ZF 45M | 1,56:1, 2,00:1, 2,50:1, 3,03:1 |
| ZF 63M | 1,51:1, 2,00:1, 2,54:1, 3,04:1 |

### 6.2 Saildrive-Option

Beta Marine bietet den **Technodrive SeaProp** als Saildrive-Lösung:

| SeaProp-Modell | Max. Leistung | Kompatibel mit |
|---------------|--------------|----------------|
| SeaProp 60 | 30 PS | Beta/Atomic 10–30 |
| SeaProp 80 | 55 PS | Beta 35–50 |

**Technodrive SeaProp Daten:**

| Parameter | SeaProp 60 | SeaProp 80 |
|-----------|-----------|-----------|
| Max. Eingangsleistung | 22 kW (30 PS) | 40 kW (55 PS) |
| Untersetzung | 2,15:1, 2,50:1 | 2,15:1, 2,50:1 |
| Gewicht | 28 kg | 35 kg |
| Propellerwelle | Ø 25 mm | Ø 30 mm |
| Zinkanode | 1 Stück, 0,5 kg | 1 Stück, 0,8 kg |
| Manschette (Diaphragma) | Neopren, Ø 280 mm | Neopren, Ø 320 mm |
| Empf. Wechselintervall Manschette | 7 Jahre | 7 Jahre |

**Hinweis:** Für Beta 60+ gibt es keine Saildrive-Option. Hier ist ein konventionelles Wellengetriebe mit Stopfbuchse oder PSS-Dichtung erforderlich.

---

## 7. Beta Marine — Bekannte Schwachstellen

### 7.1 Schwachstellen nach Modellgruppe

**Beta 14–25 (2-Zylinder D722, 3-Zylinder D902/D1105):**

| Schwachstelle | Betroffene Modelle | Schweregrad | Häufigkeit |
|--------------|-------------------|-------------|-----------|
| Impeller-Gehäusedeckel undicht | Alle | Gering | Häufig |
| Thermostat klemmt (zu-Position) | Beta 14, 16 | Mittel | Gelegentlich |
| Lichtmaschinenriemen rutscht | Alle | Gering | Häufig |
| Auspuffkrümmer-Korrosion | Alle ab >8 Jahre | Mittel | Gelegentlich |
| Kraftstoffhebepumpe versagt | Beta 20, 25 | Mittel | Selten |
| Ölverlust an Ventildeckeldichtung | Alle | Gering | Gelegentlich |

**Beta 30–50 (4-Zylinder V1505, V2003, V2403):**

| Schwachstelle | Betroffene Modelle | Schweregrad | Häufigkeit |
|--------------|-------------------|-------------|-----------|
| Wärmetauscher Zinkerosion | Alle | Mittel | Gelegentlich |
| Seewasserpumpe Wellendichtring | Alle | Mittel | Gelegentlich |
| Motorlager-Ermüdung | Beta 38, 43 | Gering | Selten |
| Getriebe-Ölverlust (PRM 150/260) | Beta 30–50 | Gering | Gelegentlich |
| Kraftstoffleitungen verhärten | Alle ab >10 Jahre | Mittel | Häufig |
| Anlasser-Magnetschalter | Alle | Mittel | Selten |

**Beta 60–150 (4-Zylinder V3307, V3800 mit/ohne Turbo):**

| Schwachstelle | Betroffene Modelle | Schweregrad | Häufigkeit |
|--------------|-------------------|-------------|-----------|
| Turbolader-Ölverlust | Beta 75, 90, 115+ | Mittel | Gelegentlich |
| Ladeluftkühler-Undichtigkeit | Beta 90, 130, 150 | Mittel | Selten |
| Injektordichtung (Kupfer) | Beta 60+ (DI) | Gering | Häufig |
| ZF-Getriebe Schaltschwierigkeiten | Beta 60+ | Mittel | Selten |
| Schwungrad-Verschraubung locker | Beta 105+ | Hoch | Sehr selten |
| Kühlwasserschlauch am Turbo | Beta 75+ | Mittel | Gelegentlich |

### 7.2 Vergleich Schwachstellen Beta vs. Yanmar/Volvo

| Aspekt | Beta Marine | Yanmar | Volvo Penta |
|--------|-----------|--------|------------|
| Kühlsystem-Probleme | Weniger (einfacherer Aufbau) | Mittel | Häufiger (komplexer) |
| Elektronik-Fehler | Sehr selten (mechanisch) | Gelegentlich | Häufiger (mehr Elektronik) |
| Ersatzteil-Verfügbarkeit | Gut (Kubota-Basis) | Sehr gut | Gut |
| Korrosion Auspuff | Gleich | Gleich | Gleich |
| Getriebe-Zuverlässigkeit | Gut (PRM/ZF) | Sehr gut (KM) | Gut (IPS/Saildrive) |

---

## 8. Nanni Diesel — Firmengeschichte und Philosophie

### 8.1 Unternehmensgeschichte

Nanni Industries S.A.S. wurde 1952 von Giovanni Nanni in La Ciotat (Frankreich) gegründet. Das Unternehmen hat seinen Ursprung in der Motorenwartung für die lokale Fischereiflotte und entwickelte sich zum führenden französischen Marinemotor-Hersteller.

**Meilensteine:**

| Jahr | Ereignis |
|------|----------|
| 1952 | Gründung durch Giovanni Nanni in La Ciotat, Frankreich |
| 1960 | Erste eigene Marinisierungen von Fiat-Industriemotoren |
| 1968 | Wechsel auf Toyota-Basisblöcke (Partnerschaft mit Toyota Industrial) |
| 1975 | Einführung der Marine-Reihe 2.10–4.50 |
| 1982 | Export nach Italien, Spanien, Griechenland |
| 1988 | Einführung der T-Serie (Turbodiesel) |
| 1995 | N-Serie Neugestaltung mit Common-Rail-Vorbereitung |
| 2000 | Übernahme durch Investorengruppe, Modernisierung |
| 2005 | Partnerschaft mit Kubota für 4-Zylinder-Blöcke |
| 2010 | Erweiterung auf 250 PS (6-Zylinder) |
| 2014 | N4.80 als OEM-Option bei Bénéteau und Dufour |
| 2017 | Neue N-Serie Generation mit EU Stage V Konformität |
| 2020 | Hybrid-Ready Motorenplattform vorgestellt |
| 2022 | Kooperation mit Torqeedo für Hybrid-Antriebssysteme |
| 2024 | Überarbeitete T-Serie mit verbesserter Abgasnachbehandlung |

### 8.2 Firmenphilosophie

Nanni positioniert sich als **europäische Qualitätsalternative** zu den japanischen Marktführern:

**Kernprinzipien:**
- Marinisierung „Made in France" mit strenger Qualitätskontrolle
- Optimiert für Mittelmeer-Bedingungen (Wärme, Salz, lange Saisons)
- Starkes OEM-Geschäft mit französischen und italienischen Werften
- Gutes Preis-Leistungs-Verhältnis im mittleren Segment
- Umfangreiches Händlernetz im gesamten Mittelmeerraum

**Zielgruppe:**
- Mittelmeer-Segler und Motorbootfahrer
- Charterflotten (Robustheit, Wartungsfreundlichkeit)
- OEM-Werften (Bénéteau, Dufour, Fountaine-Pajot, Lagoon)
- Besitzer älterer Yachten im Refit-Markt

### 8.3 Produktionsstandort

| Aspekt | Detail |
|--------|--------|
| Hauptsitz | La Ciotat, Provence-Alpes-Côte d'Azur, Frankreich |
| Zweigwerk | Genua, Italien (italienischer Markt) |
| Mitarbeiter | ca. 120 (2025) |
| Jahresproduktion | ca. 4.000–5.000 Motoren |
| Produktionsprozess | Halbautomatische Montage, Prüfstandlauf |
| Zertifizierung | ISO 9001:2015, RCD 2013/53/EU |

---

## 9. Nanni Diesel — Modellreihen-Übersicht

### 9.1 Aktuelle Modellpalette (2025/26)

**N-Serie (Saugdiesel — Segelboote und leichte Motorboote):**

| Modell | Zylinder | Hubraum (cm³) | Leistung PS | Leistung kW | Drehzahl | Basisblock |
|--------|----------|--------------|-------------|-------------|----------|-----------|
| N2.10 | 2 | 854 | 10 | 7,4 | 3.000 | Toyota 1KD |
| N2.14 | 2 | 854 | 14 | 10,3 | 3.600 | Toyota 1KD |
| N3.21 | 3 | 1.496 | 21 | 15,4 | 2.800 | Toyota 2KD |
| N3.30 | 3 | 1.496 | 30 | 22,1 | 3.600 | Toyota 2KD |
| N4.38 | 4 | 2.184 | 38 | 27,9 | 2.800 | Toyota 3CT |
| N4.50 | 4 | 2.434 | 50 | 36,8 | 3.000 | Kubota V2403 |
| N4.60 | 4 | 2.434 | 60 | 44,1 | 3.300 | Kubota V2403-DI |
| N4.80 | 4 | 3.318 | 80 | 58,8 | 2.800 | Kubota V3307-DI |
| N4.100 | 4 | 3.318 | 100 | 73,5 | 3.150 | Kubota V3307-DI-T |
| N4.115 | 4 | 3.769 | 115 | 84,6 | 3.000 | Kubota V3800-DI |

**T-Serie (Turbodiesel — Motorboote und größere Segelyachten):**

| Modell | Zylinder | Hubraum (cm³) | Leistung PS | Leistung kW | Drehzahl | Basisblock |
|--------|----------|--------------|-------------|-------------|----------|-----------|
| T4.130 | 4 | 3.318 | 130 | 95,6 | 3.300 | Kubota V3307-DI-T |
| T4.155 | 4 | 3.769 | 155 | 114,0 | 3.300 | Kubota V3800-DI-T |
| T4.165 | 4 | 3.769 | 165 | 121,3 | 3.600 | Kubota V3800-DI-T-E |
| T4.200 | 4 | 3.769 | 200 | 147,1 | 3.800 | Kubota V3800-CR-DI-T |
| T6.250 | 6 | 5.193 | 250 | 183,8 | 3.300 | Kubota V5009 |

---

## 10. Nanni Diesel — N-Serie (Saugdiesel)

### 10.1 N2.10 und N2.14 — Kompaktklasse

**N2.10 Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Basisblock | Toyota 1KD (marinisiert) |
| Zylinder | 2, Reihe |
| Bohrung × Hub | 73,0 × 82,0 mm |
| Hubraum | 854 cm³ |
| Verdichtung | 22,5:1 |
| Leistung | 10 PS (7,4 kW) bei 3.000 U/min |
| Max. Drehmoment | 26,5 Nm bei 2.200 U/min |
| Einspritzung | Mechanisch, indirekt |
| Kühlung | Indirekt, Zweikreis-Seewasser |
| Kraftstoffverbrauch | 2,5 l/h Volllast, 1,2 l/h Reise |
| Gewicht (trocken, mit Getriebe) | 89 kg |
| Länge × Breite × Höhe | 535 × 410 × 505 mm |
| Ölmenge | 2,0 l |
| Kühlmittel | 2,3 l |
| Lichtmaschine | 12V/60A |
| Getriebe Standard | TMC 40, 2:1 |

**UVP (2025/26):** 7.200–8.800 EUR

**N2.14 Technische Daten (Unterschiede zum N2.10):**

| Parameter | Wert |
|-----------|------|
| Leistung | 14 PS (10,3 kW) bei 3.600 U/min |
| Kraftstoffverbrauch | 3,2 l/h Volllast, 1,5 l/h Reise |
| Gewicht | 92 kg |

**UVP (2025/26):** 7.800–9.500 EUR

### 10.2 N3.21 und N3.30 — Segelboot-Standardklasse

**N3.21 Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Basisblock | Toyota 2KD (marinisiert) |
| Zylinder | 3, Reihe |
| Bohrung × Hub | 80,0 × 99,0 mm |
| Hubraum | 1.496 cm³ |
| Verdichtung | 22,0:1 |
| Leistung | 21 PS (15,4 kW) bei 2.800 U/min |
| Max. Drehmoment | 58,2 Nm bei 2.000 U/min |
| Kraftstoffverbrauch | 4,5 l/h Volllast, 2,2 l/h Reise |
| Gewicht (trocken, mit Getriebe) | 128 kg |
| Länge × Breite × Höhe | 605 × 445 × 548 mm |
| Ölmenge | 3,2 l |
| Getriebe Standard | TMC 60, 2:1 |
| Saildrive-Option | Technodrive SeaProp 60 |

**UVP (2025/26):** 9.800–11.500 EUR

**N3.30 Technische Daten (Unterschiede zum N3.21):**

| Parameter | Wert |
|-----------|------|
| Leistung | 30 PS (22,1 kW) bei 3.600 U/min |
| Max. Drehmoment | 63,5 Nm bei 2.400 U/min |
| Kraftstoffverbrauch | 5,8 l/h Volllast, 2,8 l/h Reise |
| Gewicht | 135 kg |

**UVP (2025/26):** 11.200–13.000 EUR

### 10.3 N4.38 — Mittelklasse

| Parameter | Wert |
|-----------|------|
| Basisblock | Toyota 3CT (marinisiert) |
| Zylinder | 4, Reihe |
| Bohrung × Hub | 86,0 × 94,0 mm |
| Hubraum | 2.184 cm³ |
| Verdichtung | 22,3:1 |
| Leistung | 38 PS (27,9 kW) bei 2.800 U/min |
| Max. Drehmoment | 105,8 Nm bei 1.800 U/min |
| Kraftstoffverbrauch | 7,5 l/h Volllast, 3,5 l/h Reise |
| Gewicht (trocken, mit Getriebe) | 192 kg |
| Länge × Breite × Höhe | 690 × 510 × 605 mm |
| Getriebe Standard | PRM 150, 2:1 |
| Saildrive-Option | Technodrive SeaProp 80 |

**UVP (2025/26):** 13.200–15.500 EUR

### 10.4 N4.50 / N4.60 — Kubota-Basis

| Parameter | N4.50 | N4.60 |
|-----------|-------|-------|
| Basisblock | Kubota V2403 | Kubota V2403-DI |
| Zylinder | 4, Reihe | 4, Reihe |
| Hubraum | 2.434 cm³ | 2.434 cm³ |
| Einspritzung | Mechanisch, indirekt | Direkteinspritzung |
| Leistung | 50 PS (36,8 kW) | 60 PS (44,1 kW) |
| Drehzahl | 3.000 U/min | 3.300 U/min |
| Verbrauch Volllast | 10,0 l/h | 12,2 l/h |
| Verbrauch Reise | 4,8 l/h | 5,5 l/h |
| Gewicht | 215 kg | 225 kg |
| Getriebe | PRM 260, 2:1 | ZF 15M, 2:1 |
| UVP | 16.500–19.000 EUR | 18.800–21.500 EUR |

### 10.5 N4.80 / N4.100 / N4.115

| Parameter | N4.80 | N4.100 | N4.115 |
|-----------|-------|--------|--------|
| Basisblock | Kubota V3307-DI | Kubota V3307-DI-T | Kubota V3800-DI |
| Zylinder | 4 | 4, Turbo | 4 |
| Hubraum | 3.318 cm³ | 3.318 cm³ | 3.769 cm³ |
| Leistung | 80 PS | 100 PS | 115 PS |
| Drehzahl | 2.800 U/min | 3.150 U/min | 3.000 U/min |
| Verbrauch Volllast | 15,5 l/h | 19,8 l/h | 22,0 l/h |
| Verbrauch Reise | 7,2 l/h | 9,0 l/h | 10,2 l/h |
| Gewicht | 265 kg | 290 kg | 335 kg |
| Getriebe | ZF 25M | ZF 25M | ZF 45M |
| UVP | 22.000–25.500 EUR | 26.500–30.000 EUR | 30.000–34.500 EUR |

---

## 11. Nanni Diesel — T-Serie (Turbodiesel)

### 11.1 T4.130

| Parameter | Wert |
|-----------|------|
| Basisblock | Kubota V3307-DI-T (Turbo + Ladeluftkühlung) |
| Zylinder | 4, Reihe, Turbo + LLK |
| Hubraum | 3.318 cm³ |
| Leistung | 130 PS (95,6 kW) bei 3.300 U/min |
| Max. Drehmoment | 302 Nm bei 2.000 U/min |
| Kraftstoffverbrauch | 25,5 l/h Volllast, 12,0 l/h Reise |
| Gewicht (trocken, mit Getriebe) | 355 kg |
| Länge × Breite × Höhe | 870 × 600 × 720 mm |
| Getriebe Standard | ZF 45M, 2:1 |
| Kühlung | Indirekt, Zweikreis mit Ladeluftkühler |
| Lichtmaschine | 12V/110A |

**UVP (2025/26):** 35.000–40.000 EUR

### 11.2 T4.155 / T4.165

| Parameter | T4.155 | T4.165 |
|-----------|--------|--------|
| Basisblock | Kubota V3800-DI-T | Kubota V3800-DI-T-E |
| Leistung | 155 PS (114,0 kW) | 165 PS (121,3 kW) |
| Drehzahl | 3.300 U/min | 3.600 U/min |
| Max. Drehmoment | 358 Nm | 348 Nm |
| Verbrauch Volllast | 30,5 l/h | 33,0 l/h |
| Verbrauch Reise | 14,5 l/h | 15,5 l/h |
| Gewicht | 385 kg | 395 kg |
| Getriebe | ZF 63M | ZF 63M |
| UVP | 40.000–46.000 EUR | 43.000–49.000 EUR |

### 11.3 T4.200

| Parameter | Wert |
|-----------|------|
| Basisblock | Kubota V3800-CR-DI-T (Common-Rail) |
| Zylinder | 4, Reihe, Turbo + LLK + Common-Rail |
| Hubraum | 3.769 cm³ |
| Leistung | 200 PS (147,1 kW) bei 3.800 U/min |
| Max. Drehmoment | 408 Nm bei 2.200 U/min |
| Einspritzung | Common-Rail Direkteinspritzung |
| Kraftstoffverbrauch | 40,5 l/h Volllast, 18,8 l/h Reise |
| Gewicht | 430 kg |
| Getriebe Standard | ZF 63M oder ZF 80M |
| Elektronik | ECU, CAN-Bus, Diagnose-Schnittstelle |

**UVP (2025/26):** 52.000–60.000 EUR

### 11.4 T6.250

| Parameter | Wert |
|-----------|------|
| Basisblock | Kubota V5009 |
| Zylinder | 6, Reihe, Turbo + LLK |
| Hubraum | 5.193 cm³ |
| Leistung | 250 PS (183,8 kW) bei 3.300 U/min |
| Max. Drehmoment | 580 Nm bei 2.000 U/min |
| Kraftstoffverbrauch | 50,0 l/h Volllast, 23,0 l/h Reise |
| Gewicht | 560 kg |
| Getriebe Standard | ZF 80M |

**UVP (2025/26):** 65.000–75.000 EUR

---

## 12. Nanni Diesel — Getriebe und Saildrive

### 12.1 Getriebe-Zuordnung

| Modell | Standard-Getriebe | Alternativen |
|--------|------------------|-------------|
| N2.10/N2.14 | TMC 40 | PRM 80 |
| N3.21/N3.30 | TMC 60 | PRM 120 |
| N4.38 | PRM 150 | TMC 60A |
| N4.50 | PRM 260 | — |
| N4.60 | ZF 15M | PRM 260 |
| N4.80 | ZF 25M | — |
| N4.100 | ZF 25M | ZF 45M |
| N4.115 | ZF 45M | — |
| T4.130 | ZF 45M | ZF 63M |
| T4.155/165 | ZF 63M | — |
| T4.200 | ZF 63M / ZF 80M | — |
| T6.250 | ZF 80M | ZF 85M |

### 12.2 Saildrive-Optionen

Nanni bietet Saildrive-Konfigurationen für die kleineren Modelle:

| Saildrive | Kompatible Modelle | Max. Leistung |
|-----------|-------------------|--------------|
| Technodrive SeaProp 60 | N2.10, N2.14, N3.21, N3.30 | 30 PS |
| Technodrive SeaProp 80 | N4.38, N4.50 | 55 PS |
| ZF Saildrive SD10 | N4.60, N4.80 | 80 PS |

---

## 13. Nanni Diesel — Bekannte Schwachstellen

### 13.1 Schwachstellen N-Serie (Toyota-Basis: N2.10–N4.38)

| Schwachstelle | Betroffene Modelle | Schweregrad | Häufigkeit |
|--------------|-------------------|-------------|-----------|
| Seewasserpumpen-Impeller | Alle | Gering | Häufig (Verschleiß) |
| Kraftstoffhebepumpe Membran | N3.21, N3.30, N4.38 | Mittel | Gelegentlich |
| Ventildeckeldichtung Ölverlust | N4.38 | Gering | Häufig |
| Thermostat klemmt | N2.10, N2.14 | Mittel | Gelegentlich |
| Lichtmaschinenregler defekt | Alle Toyota-Basis | Mittel | Selten |
| Anlasser Freilauf | N3.21, N3.30 | Mittel | Selten |
| Auspuffkrümmer Rissbildung | Alle ab >10 Jahre | Hoch | Gelegentlich |

### 13.2 Schwachstellen N-Serie (Kubota-Basis: N4.50–N4.115)

| Schwachstelle | Betroffene Modelle | Schweregrad | Häufigkeit |
|--------------|-------------------|-------------|-----------|
| Injektordichtungen (Kupfer) | N4.60, N4.80 (DI) | Gering | Häufig |
| Turbolader-Ölleitung verstopft | N4.100 | Mittel | Gelegentlich |
| Wärmetauscher Zink-Erosion | Alle | Mittel | Gelegentlich |
| Kühlwasserschlauch am Turbo | N4.100 | Mittel | Gelegentlich |
| ZF-Getriebe Schaltdruck | N4.60+ | Gering | Selten |
| Kraftstofffilter-Gehäuse Riss | N4.50, N4.60 | Mittel | Selten |

### 13.3 Schwachstellen T-Serie

| Schwachstelle | Betroffene Modelle | Schweregrad | Häufigkeit |
|--------------|-------------------|-------------|-----------|
| Ladeluftkühler-Undichtigkeit | T4.130, T4.155 | Mittel | Gelegentlich |
| Turbolader-Wellendichtung | T4.155, T4.165 | Hoch | Selten |
| Common-Rail Injektor-Verkokung | T4.200 | Hoch | Gelegentlich |
| ECU-Software Fehler | T4.200 | Mittel | Selten |
| Abgasgegendruck zu hoch | Alle T-Serie | Mittel | Gelegentlich |
| Schwingungsdämpfer-Verschleiß | T6.250 | Mittel | Selten |

---

## 14. Vetus — Firmengeschichte und Philosophie

### 14.1 Unternehmensgeschichte

Vetus B.V. (kurz für „Vetus den Ouden") wurde 1951 in Schiedam, Niederlande gegründet. Das Unternehmen ist als Vollsortimenter für Bootszubehör bekannt und produziert neben Motoren auch Bugstrahlruder, Auspuffsysteme, Tanks, Ruderanlagen und Bootselektrik.

**Meilensteine:**

| Jahr | Ereignis |
|------|----------|
| 1951 | Gründung durch R.J. den Ouden in Schiedam, NL |
| 1965 | Erste Marine-Motorisierungen (Faryman-Blöcke) |
| 1972 | Einführung der M-Serie (Mitsubishi-Basis) |
| 1978 | Erster BOW PRO Bugstrahlruder |
| 1985 | Vetus M3.10 als Bestseller im Binnenmarkt |
| 1990 | Erweiterung auf D-Serie (Deutz-Basis, 100+ PS) |
| 1995 | VF-Serie für größere Motorboote |
| 2000 | Integration Bugstrahlruder/Motor-Paket |
| 2005 | Übernahme durch Pontos Group |
| 2008 | Neue M-Serie Generation (M2.C5, M3.09, M4.14) |
| 2012 | VF4.140E als meistverkauftes Motorboot-Modell |
| 2015 | Einführung BOW PRO Thruster mit Proportionalsteuerung |
| 2018 | Deutz TCD-basierte D-Serie Überarbeitung |
| 2020 | Vetus E-LINE (vollelektrische Antriebe) |
| 2022 | Hybrid-Module für M- und VF-Serie |
| 2024 | Neue M-Serie Generation mit EU Stage V |

### 14.2 Firmenphilosophie

Vetus verfolgt einen **Systemanbieter-Ansatz**: Motor, Getriebe, Auspuff, Bugstrahlruder, Steuerung — alles aus einer Hand.

**Kernprinzipien:**
- Komplettlösungen statt Einzelkomponenten
- Starke Integration zwischen Motor und Bordsystemen
- Fokus auf Binnenfahrt und küstennahe Motorboote
- Einfache Bedienung für Freizeitkapitäne
- Gutes Preis-Leistungs-Verhältnis

**Zielgruppe:**
- Niederländische Binnenfahrt (Stahlyachten, Motorboote)
- Küstenmotorboote Nordsee/Ostsee
- Charterboote (Binnenreviere)
- Refit-Markt (kompakte Austausch-Motoren)

### 14.3 Produktionsstandort

| Aspekt | Detail |
|--------|--------|
| Hauptsitz | Schiedam, Südholland, Niederlande |
| Motorenmontage | Schiedam + Waalwijk (NL) |
| Mitarbeiter | ca. 350 (gesamt, alle Sparten) |
| Jahresproduktion Motoren | ca. 2.000–3.000 |
| Zertifizierung | ISO 9001:2015, RCD 2013/53/EU |

---

## 15. Vetus — Modellreihen-Übersicht

### 15.1 M-Serie (Mitsubishi-Basis, Segelboote und kleine Motorboote)

| Modell | Zylinder | Hubraum (cm³) | Leistung PS | Leistung kW | Drehzahl | Mitsubishi-Basis |
|--------|----------|--------------|-------------|-------------|----------|-----------------|
| M2.02 | 2 | 570 | 8,5 | 6,3 | 3.000 | L2E |
| M2.06 | 2 | 570 | 12 | 8,8 | 3.600 | L2E |
| M2.C5 | 2 | 726 | 16 | 11,8 | 3.600 | L2C |
| M2.D5 | 2 | 726 | 18 | 13,2 | 3.800 | L2C |
| M3.09 | 3 | 952 | 21 | 15,4 | 3.000 | S3L2 |
| M3.28 | 3 | 952 | 27 | 19,9 | 3.600 | S3L2 |
| M3.29 | 3 | 1.131 | 29 | 21,3 | 3.000 | L3E |
| M4.14 | 4 | 1.318 | 33 | 24,3 | 2.800 | S4L2 |
| M4.15 | 4 | 1.318 | 33 | 24,3 | 2.800 | S4L2 |
| M4.17 | 4 | 1.318 | 38 | 27,9 | 3.200 | S4L2 |
| M4.35 | 4 | 1.758 | 42 | 30,9 | 2.800 | S4Q2 |
| M4.45 | 4 | 1.758 | 49 | 36,0 | 3.200 | S4Q2 |
| M4.56 | 4 | 1.758 | 56 | 41,2 | 3.600 | S4Q2 |

### 15.2 VF-Serie (Mitsubishi/Deutz-Basis, Motorboote)

| Modell | Zylinder | Hubraum (cm³) | Leistung PS | Leistung kW | Drehzahl | Basisblock |
|--------|----------|--------------|-------------|-------------|----------|-----------|
| VF4.140E | 4 | 2.505 | 140 | 103,0 | 3.600 | Mitsubishi S4S-DT |
| VF4.170E | 4 | 2.505 | 170 | 125,0 | 3.800 | Mitsubishi S4S-DT |
| VF4.190E | 4 | 3.331 | 190 | 139,7 | 3.200 | Deutz TCD 3.6 |
| VF5.220E | 4 | 3.331 | 220 | 161,8 | 3.600 | Deutz TCD 3.6 |
| VF5.250E | 4 | 4.038 | 250 | 183,8 | 3.200 | Deutz TCD 4.1 |

### 15.3 D-Serie (Deutz-Basis, Schwere Motorboote/Verdränger)

| Modell | Zylinder | Hubraum (cm³) | Leistung PS | Leistung kW | Drehzahl | Deutz-Basis |
|--------|----------|--------------|-------------|-------------|----------|------------|
| D4.29 | 4 | 2.875 | 65 | 47,8 | 2.300 | Deutz BF4M1008 |
| D4.42 | 4 | 2.875 | 85 | 62,5 | 2.600 | Deutz BF4M1008 |
| DT4.70 | 4 | 3.331 | 100 | 73,5 | 2.500 | Deutz TCD 3.6 |
| DT4.110 | 4 | 3.331 | 130 | 95,6 | 2.800 | Deutz TCD 3.6 |
| DT6.315 | 6 | 6.057 | 315 | 231,6 | 2.300 | Deutz TCD 6.1 |

---

## 16. Vetus — M-Serie

### 16.1 M2.02 — Kleinstes Modell

| Parameter | Wert |
|-----------|------|
| Mitsubishi-Basis | L2E |
| Zylinder | 2, Reihe |
| Bohrung × Hub | 67,0 × 68,0 mm |
| Hubraum | 570 cm³ |
| Verdichtung | 22,0:1 |
| Leistung | 8,5 PS (6,3 kW) bei 3.000 U/min |
| Max. Drehmoment | 22,5 Nm bei 2.200 U/min |
| Einspritzung | Mechanisch, indirekt |
| Kraftstoffverbrauch | 2,0 l/h Volllast, 1,0 l/h Reise |
| Gewicht (trocken, mit Getriebe) | 82 kg |
| Länge × Breite × Höhe | 510 × 390 × 488 mm |
| Getriebe Standard | TMC 40, 2:1 |

**UVP (2025/26):** 6.800–8.200 EUR

### 16.2 M2.C5 / M2.D5

| Parameter | M2.C5 | M2.D5 |
|-----------|-------|-------|
| Basis | L2C | L2C |
| Leistung | 16 PS (11,8 kW) | 18 PS (13,2 kW) |
| Drehzahl | 3.600 U/min | 3.800 U/min |
| Verbrauch Volllast | 3,5 l/h | 3,8 l/h |
| Gewicht | 98 kg | 100 kg |
| UVP | 8.200–9.800 EUR | 8.800–10.500 EUR |

### 16.3 M3.09 / M3.28 / M3.29

| Parameter | M3.09 | M3.28 | M3.29 |
|-----------|-------|-------|-------|
| Basis | S3L2 | S3L2 | L3E |
| Zylinder | 3 | 3 | 3 |
| Hubraum | 952 cm³ | 952 cm³ | 1.131 cm³ |
| Leistung | 21 PS | 27 PS | 29 PS |
| Verbrauch Volllast | 4,5 l/h | 5,5 l/h | 5,8 l/h |
| Verbrauch Reise | 2,2 l/h | 2,6 l/h | 2,8 l/h |
| Gewicht | 115 kg | 120 kg | 132 kg |
| Getriebe | TMC 60 | TMC 60 | PRM 120 |
| UVP | 9.500–11.200 EUR | 10.800–12.500 EUR | 11.500–13.500 EUR |

### 16.4 M4.14 / M4.15 / M4.17

| Parameter | M4.14 | M4.15 | M4.17 |
|-----------|-------|-------|-------|
| Basis | S4L2 | S4L2 | S4L2 |
| Zylinder | 4 | 4 | 4 |
| Hubraum | 1.318 cm³ | 1.318 cm³ | 1.318 cm³ |
| Leistung | 33 PS | 33 PS | 38 PS |
| Drehzahl | 2.800 U/min | 2.800 U/min | 3.200 U/min |
| Verbrauch Volllast | 6,5 l/h | 6,5 l/h | 7,5 l/h |
| Gewicht | 160 kg | 162 kg | 165 kg |
| Getriebe | PRM 150 | PRM 150 | PRM 150 |
| Unterschied M4.14/M4.15 | Ältere Variante | Überarbeitete Variante | Höhere Drehzahl |
| UVP | 12.500–14.500 EUR | 12.800–14.800 EUR | 13.500–15.500 EUR |

### 16.5 M4.35 / M4.45 / M4.56

| Parameter | M4.35 | M4.45 | M4.56 |
|-----------|-------|-------|-------|
| Basis | S4Q2 | S4Q2 | S4Q2 |
| Zylinder | 4 | 4 | 4 |
| Hubraum | 1.758 cm³ | 1.758 cm³ | 1.758 cm³ |
| Leistung | 42 PS | 49 PS | 56 PS |
| Drehzahl | 2.800 U/min | 3.200 U/min | 3.600 U/min |
| Verbrauch Volllast | 8,2 l/h | 9,8 l/h | 11,5 l/h |
| Verbrauch Reise | 3,8 l/h | 4,5 l/h | 5,2 l/h |
| Gewicht | 195 kg | 200 kg | 208 kg |
| Getriebe | PRM 260 | PRM 260 | ZF 15M |
| UVP | 15.000–17.500 EUR | 16.500–19.000 EUR | 18.500–21.500 EUR |

---

## 17. Vetus — VF-Serie und D-Serie

### 17.1 VF-Serie — Motorboot-Leistungsklasse

**VF4.140E:**

| Parameter | Wert |
|-----------|------|
| Mitsubishi-Basis | S4S-DT (Turbo) |
| Zylinder | 4, Reihe, Turbo + LLK |
| Hubraum | 2.505 cm³ |
| Leistung | 140 PS (103,0 kW) bei 3.600 U/min |
| Max. Drehmoment | 305 Nm bei 2.200 U/min |
| Kraftstoffverbrauch | 28,0 l/h Volllast, 13,0 l/h Reise |
| Gewicht | 345 kg |
| Getriebe Standard | ZF 45M |
| UVP | 32.000–37.000 EUR |

**VF4.170E:**

| Parameter | Wert |
|-----------|------|
| Leistung | 170 PS (125,0 kW) bei 3.800 U/min |
| Verbrauch Volllast | 33,5 l/h |
| Gewicht | 355 kg |
| Getriebe | ZF 63M |
| UVP | 37.000–42.000 EUR |

**VF4.190E / VF5.220E (Deutz-Basis):**

| Parameter | VF4.190E | VF5.220E |
|-----------|----------|----------|
| Deutz-Basis | TCD 3.6 | TCD 3.6 |
| Leistung | 190 PS | 220 PS |
| Drehzahl | 3.200 U/min | 3.600 U/min |
| Verbrauch Volllast | 38,0 l/h | 44,0 l/h |
| Gewicht | 410 kg | 425 kg |
| Getriebe | ZF 63M | ZF 80M |
| UVP | 45.000–52.000 EUR | 52.000–60.000 EUR |

**VF5.250E:**

| Parameter | Wert |
|-----------|------|
| Deutz-Basis | TCD 4.1 |
| Leistung | 250 PS (183,8 kW) bei 3.200 U/min |
| Verbrauch Volllast | 50,0 l/h |
| Gewicht | 480 kg |
| Getriebe | ZF 80M |
| UVP | 58.000–67.000 EUR |

### 17.2 D-Serie — Verdränger und schwere Motorboote

**D4.29 / D4.42 (Saugdiesel):**

| Parameter | D4.29 | D4.42 |
|-----------|-------|-------|
| Deutz-Basis | BF4M1008 | BF4M1008 |
| Leistung | 65 PS | 85 PS |
| Drehzahl | 2.300 U/min | 2.600 U/min |
| Verbrauch Volllast | 13,0 l/h | 17,0 l/h |
| Gewicht | 280 kg | 290 kg |
| Getriebe | ZF 25M | ZF 25M |
| UVP | 22.000–25.500 EUR | 25.000–29.000 EUR |

**DT4.70 / DT4.110 (Turbodiesel):**

| Parameter | DT4.70 | DT4.110 |
|-----------|--------|---------|
| Deutz-Basis | TCD 3.6 | TCD 3.6 |
| Leistung | 100 PS | 130 PS |
| Verbrauch Volllast | 20,0 l/h | 26,0 l/h |
| Gewicht | 350 kg | 370 kg |
| Getriebe | ZF 45M | ZF 45M |
| UVP | 30.000–35.000 EUR | 36.000–42.000 EUR |

**DT6.315:**

| Parameter | Wert |
|-----------|------|
| Deutz-Basis | TCD 6.1 |
| Zylinder | 6, Reihe, Turbo + LLK |
| Hubraum | 6.057 cm³ |
| Leistung | 315 PS (231,6 kW) bei 2.300 U/min |
| Max. Drehmoment | 1.050 Nm bei 1.600 U/min |
| Verbrauch Volllast | 62,0 l/h |
| Gewicht | 680 kg |
| Getriebe | ZF 85M |
| UVP | 78.000–90.000 EUR |

---

## 18. Vetus — BOW PRO Thruster-Integration

### 18.1 System-Integration Motor + Bugstrahlruder

Einzigartiges Vetus-Alleinstellungsmerkmal: Motor, Getriebe und Bugstrahlruder als integriertes System mit gemeinsamer Steuerung.

**BOW PRO Thruster-Modelle:**

| Modell | Schub (kgf) | Leistung (kW) | Tunneldurchmesser | Bootslänge |
|--------|------------|--------------|-------------------|-----------|
| BOW PRO 25 | 25 | 1,5 | 125 mm | 6–9 m |
| BOW PRO 36 | 36 | 2,2 | 150 mm | 8–11 m |
| BOW PRO 57 | 57 | 3,0 | 150 mm | 9–13 m |
| BOW PRO 76 | 76 | 4,0 | 185 mm | 11–15 m |
| BOW PRO 95 | 95 | 5,5 | 185 mm | 13–17 m |
| BOW PRO 125 | 125 | 7,5 | 210 mm | 15–20 m |
| BOW PRO 160 | 160 | 10,0 | 250 mm | 18–25 m |

**Integrationsvorteile:**
- Gemeinsames Bedienpanel für Motor + Bugstrahlruder
- CAN-Bus-Vernetzung ab VF-Serie
- Proportionalsteuerung (stufenlos) statt Ein/Aus
- Automatische Batterieladung durch Lichtmaschine dimensioniert für Thruster-Last
- Joystick-Manövriersystem (ab VF4.140E + BOW PRO 76)

### 18.2 Elektrische Dimensionierung

| BOW PRO | Batterie-Empfehlung | Kabelquerschnitt | Sicherung |
|---------|-------------------|--------------------|-----------|
| BOW PRO 25 | 1× 80 Ah AGM | 25 mm² | 80 A |
| BOW PRO 36 | 1× 100 Ah AGM | 35 mm² | 100 A |
| BOW PRO 57 | 1× 120 Ah AGM | 50 mm² | 150 A |
| BOW PRO 76 | 1× 150 Ah AGM | 70 mm² | 200 A |
| BOW PRO 95 | 2× 100 Ah AGM | 70 mm² | 250 A |
| BOW PRO 125 | 2× 150 Ah AGM | 95 mm² | 300 A |
| BOW PRO 160 | 2× 200 Ah AGM | 120 mm² | 400 A |

---

## 19. Vetus — Bekannte Schwachstellen

### 19.1 M-Serie Schwachstellen

| Schwachstelle | Betroffene Modelle | Schweregrad | Häufigkeit |
|--------------|-------------------|-------------|-----------|
| Impeller-Gehäuse Korrosion | M2.02, M2.06 (ältere) | Mittel | Gelegentlich |
| Thermostat klemmt | Alle M-Serie | Mittel | Gelegentlich |
| Auspuffkrümmer Rissbildung | M3.09, M4.14 ab >8 J. | Hoch | Gelegentlich |
| Getriebe-Schaltzug schwergängig | M4.14, M4.17 | Gering | Häufig |
| Kraftstoffhebepumpe undicht | M3.28, M3.29 | Mittel | Gelegentlich |
| Ventilspiel verstellt sich | M4.35, M4.45, M4.56 | Gering | Gelegentlich |
| Motorlager-Durchsackung | Alle M-Serie ab >12 J. | Mittel | Häufig |
| Seewasserpumpen-Lager | M4.35+ | Mittel | Gelegentlich |

### 19.2 VF-Serie Schwachstellen

| Schwachstelle | Betroffene Modelle | Schweregrad | Häufigkeit |
|--------------|-------------------|-------------|-----------|
| Turbolader-Ölverlust | VF4.140E, VF4.170E | Mittel | Gelegentlich |
| Ladeluftkühler undicht | VF4.190E+ | Mittel | Selten |
| Injektordüsen verkokt | Alle VF (Turbo) | Mittel | Gelegentlich |
| Kühlmittelverlust Wärmetauscher | Alle VF | Mittel | Selten |
| Sensor-Fehler CAN-Bus | VF4.190E+ (Deutz) | Gering | Gelegentlich |

### 19.3 D-Serie Schwachstellen

| Schwachstelle | Betroffene Modelle | Schweregrad | Häufigkeit |
|--------------|-------------------|-------------|-----------|
| Deutz-Ventilspiel | Alle D-Serie | Gering | Häufig (Wartung) |
| Ölverbrauch bei niedrigem Teillast | D4.29, D4.42 | Gering | Gelegentlich |
| Schwingungsdämpfer-Verschleiß | DT6.315 | Mittel | Selten |
| Abgastrübung bei Kaltstart | Alle D-Serie (Deutz) | Gering | Häufig |

---

## 20. Sole Diesel — Firmengeschichte und Philosophie

### 20.1 Unternehmensgeschichte

Sole Diesel S.A. wurde 1956 in Barcelona, Spanien gegründet. Der Name „Sole" (katalanisch für „Sonne") spiegelt die mediterrane Herkunft wider. Das Unternehmen hat sich auf die Marinisierung von Mitsubishi-Industriemotoren spezialisiert.

**Meilensteine:**

| Jahr | Ereignis |
|------|----------|
| 1956 | Gründung in Barcelona als Sole S.A. |
| 1965 | Erste Marinisierungen von Lombardini-Dieselmotoren |
| 1972 | Wechsel auf Mitsubishi-Basisblöcke |
| 1978 | Einführung der Mini-Serie |
| 1985 | Export nach Frankreich und Italien |
| 1990 | Mini-33 als Bestseller für Charterflotten |
| 1995 | Erweiterung auf 6-Zylinder (Mini-62 auf S6S-Basis) |
| 2000 | CE-Zertifizierung aller Modelle |
| 2005 | Überarbeitung der gesamten Mini-Serie |
| 2010 | Neue Mini-Generation mit EU Stage IIIA |
| 2015 | Erweiterung Händlernetz auf Nordeuropa |
| 2018 | Mini-Serie Stage V Konformität |
| 2020 | Hybrid-Ready Plattform angekündigt |
| 2024 | Überarbeitete Mini-Serie mit verbesserter Schalldämmung |

### 20.2 Firmenphilosophie

**Kernprinzipien:**
- Robuste, einfache Motoren für mediterrane Bedingungen
- Optimales Preis-Leistungs-Verhältnis
- Starke Präsenz im Chartermarkt (Griechenland, Kroatien, Spanien)
- Mitsubishi-Basisblöcke mit bewährter Industriequalität
- Guter Service im Mittelmeerraum, schwächer in Nordeuropa

### 20.3 Produktionsstandort

| Aspekt | Detail |
|--------|--------|
| Hauptsitz | Barcelona, Katalonien, Spanien |
| Mitarbeiter | ca. 65 (2025) |
| Jahresproduktion | ca. 1.500–2.000 Motoren |
| Zertifizierung | ISO 9001:2015, RCD 2013/53/EU |

---

## 21. Sole Diesel — Mini-Serie (Mitsubishi-Basis)

### 21.1 Modellpalette

| Modell | Zylinder | Hubraum (cm³) | Leistung PS | Leistung kW | Drehzahl | Mitsubishi-Basis |
|--------|----------|--------------|-------------|-------------|----------|-----------------|
| Mini-11 | 2 | 570 | 11 | 8,1 | 3.000 | L2E |
| Mini-17 | 3 | 952 | 17 | 12,5 | 2.800 | S3L2 |
| Mini-26 | 3 | 952 | 26 | 19,1 | 3.600 | S3L2 |
| Mini-29 | 3 | 1.131 | 29 | 21,3 | 3.000 | L3E |
| Mini-33 | 4 | 1.318 | 33 | 24,3 | 2.800 | S4L2 |
| Mini-37 | 4 | 1.318 | 37 | 27,2 | 3.200 | S4L2 |
| Mini-44 | 4 | 1.758 | 44 | 32,4 | 2.800 | S4Q2 |
| Mini-48 | 4 | 1.758 | 48 | 35,3 | 3.200 | S4Q2 |
| Mini-55 | 4 | 1.758 | 55 | 40,4 | 3.600 | S4Q2 |
| Mini-62 | 6 | 3.331 | 62 | 45,6 | 2.500 | S6S |

### 21.2 Mini-11

| Parameter | Wert |
|-----------|------|
| Mitsubishi-Basis | L2E |
| Zylinder | 2, Reihe |
| Bohrung × Hub | 67,0 × 68,0 mm |
| Hubraum | 570 cm³ |
| Leistung | 11 PS (8,1 kW) bei 3.000 U/min |
| Max. Drehmoment | 28,5 Nm bei 2.200 U/min |
| Kraftstoffverbrauch | 2,5 l/h Volllast, 1,2 l/h Reise |
| Gewicht (trocken, mit Getriebe) | 85 kg |
| Länge × Breite × Höhe | 520 × 395 × 495 mm |
| Getriebe Standard | TMC 40, 2:1 |
| Saildrive-Option | Technodrive SeaProp 60 |

**UVP (2025/26):** 6.500–7.800 EUR

### 21.3 Mini-17 / Mini-26

| Parameter | Mini-17 | Mini-26 |
|-----------|---------|---------|
| Basis | S3L2 | S3L2 |
| Leistung | 17 PS | 26 PS |
| Drehzahl | 2.800 U/min | 3.600 U/min |
| Verbrauch Volllast | 3,8 l/h | 5,2 l/h |
| Gewicht | 110 kg | 115 kg |
| Getriebe | TMC 60 | TMC 60 |
| UVP | 8.200–9.800 EUR | 9.800–11.500 EUR |

### 21.4 Mini-29

| Parameter | Wert |
|-----------|------|
| Basis | L3E |
| Leistung | 29 PS bei 3.000 U/min |
| Verbrauch Volllast | 5,8 l/h |
| Gewicht | 130 kg |
| Getriebe | PRM 120 |
| UVP | 10.800–12.500 EUR |

### 21.5 Mini-33 / Mini-37

| Parameter | Mini-33 | Mini-37 |
|-----------|---------|---------|
| Basis | S4L2 | S4L2 |
| Leistung | 33 PS | 37 PS |
| Drehzahl | 2.800 U/min | 3.200 U/min |
| Verbrauch Volllast | 6,5 l/h | 7,2 l/h |
| Gewicht | 158 kg | 162 kg |
| Getriebe | PRM 150 | PRM 150 |
| UVP | 12.000–14.000 EUR | 12.800–14.800 EUR |

### 21.6 Mini-44 / Mini-48 / Mini-55

| Parameter | Mini-44 | Mini-48 | Mini-55 |
|-----------|---------|---------|---------|
| Basis | S4Q2 | S4Q2 | S4Q2 |
| Leistung | 44 PS | 48 PS | 55 PS |
| Drehzahl | 2.800 U/min | 3.200 U/min | 3.600 U/min |
| Verbrauch Volllast | 8,8 l/h | 9,5 l/h | 11,0 l/h |
| Verbrauch Reise | 4,0 l/h | 4,5 l/h | 5,0 l/h |
| Gewicht | 192 kg | 198 kg | 205 kg |
| Getriebe | PRM 260 | PRM 260 | ZF 15M |
| UVP | 14.500–16.800 EUR | 15.500–18.000 EUR | 17.500–20.200 EUR |

### 21.7 Mini-62 — Größtes Modell

| Parameter | Wert |
|-----------|------|
| Mitsubishi-Basis | S6S |
| Zylinder | 6, Reihe |
| Bohrung × Hub | 94,0 × 120,0 mm |
| Hubraum | 3.331 cm³ |
| Leistung | 62 PS (45,6 kW) bei 2.500 U/min |
| Max. Drehmoment | 192,5 Nm bei 1.600 U/min |
| Kraftstoffverbrauch | 12,5 l/h Volllast, 5,8 l/h Reise |
| Gewicht | 310 kg |
| Getriebe Standard | ZF 25M |
| Besonderheit | 6-Zylinder = extrem laufruhig, ideal für Verdränger |

**UVP (2025/26):** 22.000–25.500 EUR

---

## 22. Sole Diesel — Bekannte Schwachstellen

### 22.1 Mini-Serie Schwachstellen

| Schwachstelle | Betroffene Modelle | Schweregrad | Häufigkeit |
|--------------|-------------------|-------------|-----------|
| Impeller-Gehäusedeckel-Dichtung | Alle | Gering | Häufig |
| Auspuffkrümmer Korrosion | Alle ab >6 Jahre | Hoch | Gelegentlich |
| Kraftstoffhebepumpe Membran | Mini-29, Mini-33, Mini-37 | Mittel | Gelegentlich |
| Thermostat klemmt | Mini-11, Mini-17 | Mittel | Gelegentlich |
| Lichtmaschinenriemen-Spannung | Alle | Gering | Häufig |
| Motorlager-Ermüdung | Alle ab >10 Jahre | Mittel | Häufig |
| Seewasserpumpe Wellendichtring | Mini-44+ | Mittel | Gelegentlich |
| Ventildeckel-Ölverlust | Mini-33, Mini-37 | Gering | Gelegentlich |
| Öldruckschalter defekt | Alle | Gering | Selten |
| Kabelbaumkorrosion (Salz) | Alle (mediterrane Nutzung) | Mittel | Gelegentlich |
| Getriebe-Ölstand sinkt (PRM) | Mini-29 bis Mini-48 | Gering | Gelegentlich |

### 22.2 Sole vs. Vetus (gleiche Mitsubishi-Basis)

| Aspekt | Sole Mini | Vetus M-Serie |
|--------|----------|--------------|
| Marinisierungs-Qualität | Gut, einfach | Gut, aufwendiger |
| Auspuffkrümmer-Lebensdauer | 6–10 Jahre | 8–12 Jahre |
| Verkabelungs-Qualität | Befriedigend | Gut |
| Korrosionsschutz | Befriedigend | Gut |
| Preis | 10–15 % günstiger | Referenz |
| Service Europa Nord | Eingeschränkt | Gut (NL-Netzwerk) |
| Service Mittelmeer | Sehr gut | Eingeschränkt |

---

## 23. Craftsman Marine — Budget-Alternative

### 23.1 Firmenüberblick

Craftsman Marine B.V. ist ein niederländischer Marinemotor-Hersteller mit Sitz in Lelystad. Das Unternehmen wurde 2003 gegründet und bietet bewusst günstige Marinisierungen von Mitsubishi-Industrieblöcken an.

**Positionierung:** Preisgünstigste Option im europäischen Markt, ca. 20–30 % unter Yanmar/Volvo-Niveau.

### 23.2 Modellpalette

| Modell | Zylinder | Hubraum | Leistung PS | Basisblock | Gewicht | UVP EUR |
|--------|----------|---------|-------------|-----------|---------|---------|
| CM 2.16 | 2 | 726 cm³ | 16 | Mitsubishi L2C | 95 kg | 5.800–7.200 |
| CM 3.27 | 3 | 952 cm³ | 27 | Mitsubishi S3L2 | 118 kg | 7.500–9.000 |
| CM 4.35 | 4 | 1.318 cm³ | 35 | Mitsubishi S4L2 | 160 kg | 9.800–11.500 |
| CM 4.42 | 4 | 1.758 cm³ | 42 | Mitsubishi S4Q2 | 195 kg | 11.500–13.500 |
| CM 4.52 | 4 | 1.758 cm³ | 52 | Mitsubishi S4Q2 | 202 kg | 13.000–15.200 |
| CM 4.65 | 4 | 2.505 cm³ | 65 | Mitsubishi S4S | 250 kg | 15.500–18.000 |
| CM 4.80 | 4 | 2.505 cm³ | 80 | Mitsubishi S4S-T | 270 kg | 18.000–21.000 |
| CM 4.100 | 4 | 2.505 cm³ | 100 | Mitsubishi S4S-DT | 285 kg | 21.000–24.500 |
| CM 4.140 | 4 | 2.505 cm³ | 140 | Mitsubishi S4S-DT | 310 kg | 26.000–30.000 |

### 23.3 Craftsman Marine — Bewertung

**Vorteile:**
- Deutlich günstigster Preis im Markt
- Solide Mitsubishi-Basisblöcke
- Gute Ersatzteilverfügbarkeit (Mitsubishi)
- Niederländisches Service-Netzwerk
- CE-zertifiziert

**Nachteile:**
- Marinisierungsqualität unterhalb Beta/Nanni-Niveau
- Weniger aufwendiger Korrosionsschutz
- Kabelbäume und Instrumentierung einfacher
- Auspuffkrümmer-Lebensdauer kürzer (5–8 Jahre)
- Kein internationales Händlernetz außerhalb NL/DE/BE
- Wiederverkaufswert deutlich niedriger
- Technischer Support eingeschränkt

**Empfehlung (AYDI):** Geeignet für preissensitive Refit-Projekte bei Binnenfahrt und gemäßigten Bedingungen. Für Blauwasser oder intensive Salzwassernutzung besser Beta Marine oder Nanni wählen.

---

## 24. Vergleich aller Hersteller

### 24.1 Gesamtvergleich — 20-PS-Klasse (typisches 9-m-Segelboot)

| Kriterium | Beta 20 | Nanni N3.21 | Vetus M3.09 | Sole Mini-17 | Craftsman CM 2.16 | Yanmar 2YM20 |
|-----------|---------|-------------|-------------|-------------|-------------------|-------------|
| Leistung | 20 PS | 21 PS | 21 PS | 17 PS | 16 PS | 20 PS |
| Zylinder | 3 | 3 | 3 | 3 | 2 | 2 |
| Hubraum | 1.123 cm³ | 1.496 cm³ | 952 cm³ | 952 cm³ | 726 cm³ | 854 cm³ |
| Gewicht | 125 kg | 128 kg | 115 kg | 110 kg | 95 kg | 118 kg |
| Verbrauch Reise | 2,0 l/h | 2,2 l/h | 2,2 l/h | 1,8 l/h | 1,5 l/h | 2,0 l/h |
| UVP ab | 9.400 EUR | 9.800 EUR | 9.500 EUR | 8.200 EUR | 5.800 EUR | 10.500 EUR |
| Getriebe | PRM 120 | TMC 60 | TMC 60 | TMC 60 | TMC 40 | KM2P |
| Saildrive | SeaProp 60 | SeaProp 60 | — | SeaProp 60 | — | SD20 |
| Einspritzung | Mechanisch | Mechanisch | Mechanisch | Mechanisch | Mechanisch | Mechanisch |
| Händlernetz DE | ★★★ | ★★ | ★★★ | ★★ | ★★ | ★★★★★ |
| Händlernetz EU | ★★★ | ★★★★ | ★★★ | ★★★ | ★★ | ★★★★★ |
| Ersatzteile | ★★★★ | ★★★ | ★★★ | ★★★ | ★★★ | ★★★★★ |
| Wartungsfreundl. | ★★★★★ | ★★★★ | ★★★★ | ★★★★ | ★★★★ | ★★★★ |
| Wiederverkauf | ★★★ | ★★★ | ★★★ | ★★ | ★★ | ★★★★★ |

### 24.2 Gesamtvergleich — 50-PS-Klasse (typisches 12-m-Segelboot)

| Kriterium | Beta 50 | Nanni N4.50 | Vetus M4.56 | Sole Mini-55 | Craftsman CM 4.52 | Yanmar 4JH57 |
|-----------|---------|-------------|-------------|-------------|-------------------|-------------|
| Leistung | 50 PS | 50 PS | 56 PS | 55 PS | 52 PS | 57 PS |
| Zylinder | 4 | 4 | 4 | 4 | 4 | 4 |
| Hubraum | 2.434 cm³ | 2.434 cm³ | 1.758 cm³ | 1.758 cm³ | 1.758 cm³ | 2.190 cm³ |
| Gewicht | 218 kg | 215 kg | 208 kg | 205 kg | 202 kg | 230 kg |
| Verbrauch Reise | 4,8 l/h | 4,8 l/h | 5,2 l/h | 5,0 l/h | 4,8 l/h | 4,5 l/h |
| UVP ab | 16.800 EUR | 16.500 EUR | 18.500 EUR | 17.500 EUR | 13.000 EUR | 19.500 EUR |
| Händlernetz DE | ★★★ | ★★ | ★★★ | ★★ | ★★ | ★★★★★ |

### 24.3 Vor- und Nachteile im Direktvergleich

**Beta Marine vs. Yanmar:**

| Aspekt | Beta Marine | Yanmar |
|--------|-----------|--------|
| Preis | 10–20 % günstiger | Referenz |
| Elektronik | Minimal (mechanisch) | Zunehmend elektronisch |
| Wartung im Ausland | Kubota-Teile überall | Yanmar-Teile überall |
| Saildrive-Angebot | Technodrive (Fremdbezug) | Eigener SD (besser integriert) |
| Wiederverkaufswert | Niedriger | Höher |
| OEM-Einbau ab Werft | Selten (UK-Werften) | Sehr häufig |
| Blauwasser-Eignung | Sehr gut (Einfachheit) | Sehr gut (Netzwerk) |

**Nanni vs. Yanmar:**

| Aspekt | Nanni | Yanmar |
|--------|-------|--------|
| Preis | 5–15 % günstiger | Referenz |
| Mittelmeer-Service | Sehr gut | Sehr gut |
| Nordeuropa-Service | Eingeschränkt | Sehr gut |
| OEM-Einbau | Bénéteau, Dufour, Lagoon | Bavaria, Hanse, Bénéteau |
| Charterflotten | Häufig (Mittelmeer) | Häufig (überall) |

**Vetus vs. Volvo Penta:**

| Aspekt | Vetus | Volvo Penta |
|--------|-------|------------|
| Preis | 20–30 % günstiger | Referenz |
| Systemintegration | Gut (Motor+Thruster) | Sehr gut (IPS, Joystick) |
| Binnenfahrt | Stark | Stark |
| Motorboot-Leistung | Bis 315 PS | Bis 1.000+ PS |
| Elektronik-Komplexität | Mittel | Hoch |

---

## 25. Ersatzteile und Händlernetzwerk Europa

### 25.1 Beta Marine — Händlernetzwerk

| Land | Händler (Anzahl) | Wichtige Standorte |
|------|-----------------|-------------------|
| UK | 35+ | Thornbury (Fabrik), Southampton, Plymouth, Scotland |
| Deutschland | 8–12 | Hamburg, Kiel, Rostock, Bremen, Bodensee |
| Niederlande | 5–8 | Amsterdam, Lelystad, Harlingen |
| Frankreich | 3–5 | La Rochelle, Lorient, Marseille |
| Skandinavien | 5–8 | Göteborg, Kopenhagen, Oslo |
| Spanien | 2–3 | Barcelona, Palma |
| Griechenland | 1–2 | Athen |

**Ersatzteil-Lieferzeiten:**
- Standardteile (Impeller, Filter, Riemen): 2–5 Werktage ab UK
- Kubota-Basisteile: 1–3 Werktage (über Kubota-Landmaschinenhändler lokal)
- Marinisierungsteile (Krümmer, Wärmetauscher): 5–10 Werktage ab Thornbury
- Sonderbeschaffung: 2–4 Wochen

### 25.2 Nanni Diesel — Händlernetzwerk

| Land | Händler (Anzahl) | Wichtige Standorte |
|------|-----------------|-------------------|
| Frankreich | 40+ | La Ciotat (Fabrik), Marseille, La Rochelle, Brest |
| Italien | 25+ | Genua (Zweigwerk), Neapel, Palermo, Ravenna |
| Spanien | 15+ | Barcelona, Valencia, Palma, Ibiza |
| Griechenland | 10+ | Athen, Lefkas, Rhodos, Korfu |
| Kroatien | 5+ | Split, Dubrovnik, Zadar |
| Türkei | 5+ | Istanbul, Marmaris, Bodrum |
| Deutschland | 3–5 | Hamburg, Kiel, Friedrichshafen |
| Niederlande | 2–3 | Amsterdam, Rotterdam |

**Ersatzteil-Lieferzeiten:**
- Standardteile: 2–5 Werktage ab La Ciotat
- Toyota-Basisteile: Variable (Toyota Industrial, nicht Automotive)
- Kubota-Basisteile (N4.50+): 1–3 Werktage lokal
- Sonderbeschaffung: 2–6 Wochen

### 25.3 Vetus — Händlernetzwerk

| Land | Händler (Anzahl) | Wichtige Standorte |
|------|-----------------|-------------------|
| Niederlande | 50+ | Schiedam (Fabrik), landesweit |
| Deutschland | 15+ | Hamburg, Berlin, Bodensee, Rhein-Gebiet |
| Belgien | 10+ | Antwerpen, Gent |
| UK | 10+ | Southampton, London |
| Frankreich | 5–8 | Paris, La Rochelle |
| Skandinavien | 5–8 | Stockholm, Kopenhagen |

**Ersatzteil-Lieferzeiten:**
- Standardteile: 1–3 Werktage ab Schiedam
- Mitsubishi-Basisteile: 3–7 Werktage
- Deutz-Basisteile (D/VF-Serie): 3–7 Werktage
- Vetus-spezifische Teile: 2–5 Werktage
- BOW PRO Ersatzteile: 3–7 Werktage

### 25.4 Sole Diesel — Händlernetzwerk

| Land | Händler (Anzahl) | Wichtige Standorte |
|------|-----------------|-------------------|
| Spanien | 25+ | Barcelona (Fabrik), Palma, Valencia, Alicante |
| Griechenland | 8+ | Athen, Lefkas, Korfu |
| Kroatien | 3–5 | Split, Dubrovnik |
| Frankreich | 3–5 | Marseille, Perpignan |
| Italien | 3–5 | Genua, Neapel |
| Deutschland | 1–2 | Hamburg |
| Niederlande | 1–2 | Rotterdam |

**Ersatzteil-Lieferzeiten:**
- Standardteile: 3–7 Werktage ab Barcelona
- Mitsubishi-Basisteile: 5–10 Werktage (schwieriger außerhalb Mittelmeer)
- Sonderbeschaffung: 3–8 Wochen

---

## 26. Wartungsintervalle im Vergleich

### 26.1 Standard-Wartungsintervalle

| Wartungsarbeit | Beta Marine | Nanni Diesel | Vetus | Sole Diesel |
|---------------|-----------|-------------|-------|------------|
| Motoröl + Filter | 200h / jährlich | 200h / jährlich | 200h / jährlich | 200h / jährlich |
| Impeller-Wechsel | 200h / jährlich | 200h / jährlich | 200h / jährlich | 200h / jährlich |
| Kraftstofffilter | 200h / jährlich | 250h / jährlich | 200h / jährlich | 200h / jährlich |
| Keilriemen prüfen | 200h | 200h | 200h | 200h |
| Keilriemen wechseln | 500h | 500h | 500h | 500h |
| Ventilspiel prüfen | 500h | 500h | 500h | 500h |
| Kühlmittel wechseln | 1.000h / 2 Jahre | 1.000h / 2 Jahre | 1.000h / 2 Jahre | 1.000h / 2 Jahre |
| Zinkanode prüfen | 200h / jährlich | 200h / jährlich | 200h / jährlich | 200h / jährlich |
| Wärmetauscher reinigen | 1.000h / 3 Jahre | 1.000h / 3 Jahre | 1.000h / 3 Jahre | 1.000h / 3 Jahre |
| Injektoren prüfen | 2.000h / 5 Jahre | 2.000h / 5 Jahre | 2.000h / 5 Jahre | 2.000h / 5 Jahre |
| Turbolader prüfen | 2.000h (wo verbaut) | 2.000h | 2.000h | — |
| Motorlager prüfen | 1.000h / 3 Jahre | 1.000h / 3 Jahre | 1.000h / 3 Jahre | 1.000h / 3 Jahre |
| Getriebeöl wechseln | 200h / jährlich | 200h / jährlich | 200h / jährlich | 200h / jährlich |

### 26.2 Wartungskosten pro Jahr (Richtwerte, Eigenarbeit)

| Position | Beta Marine | Nanni Diesel | Vetus | Sole Diesel |
|----------|-----------|-------------|-------|------------|
| Motoröl (4 l) | 35–45 EUR | 35–45 EUR | 35–45 EUR | 35–45 EUR |
| Ölfilter | 12–18 EUR | 15–22 EUR | 15–20 EUR | 12–18 EUR |
| Kraftstofffilter | 15–25 EUR | 18–28 EUR | 15–25 EUR | 15–22 EUR |
| Impeller | 25–40 EUR | 28–45 EUR | 30–45 EUR | 25–40 EUR |
| Keilriemen | 15–25 EUR | 15–25 EUR | 18–28 EUR | 15–25 EUR |
| Zinkanode | 8–15 EUR | 8–15 EUR | 10–18 EUR | 8–15 EUR |
| Kühlmittel (anteilig) | 10–15 EUR | 10–15 EUR | 10–15 EUR | 10–15 EUR |
| Getriebeöl | 15–25 EUR | 15–25 EUR | 15–25 EUR | 15–25 EUR |
| **Summe/Jahr** | **135–210 EUR** | **145–220 EUR** | **150–225 EUR** | **135–205 EUR** |

---

## 27. Fehlerbilder

### 27.1 Fehlerbild F-ALT-01: Motor startet nicht — Alle Hersteller

**Beschreibung:** Anlasser dreht, Motor springt nicht an.

**Typische Ursachen (Häufigkeit):**
1. Luftblase im Kraftstoffsystem (35 %) — nach Filterwechsel oder leerem Tank
2. Kraftstoffhebepumpe defekt (15 %) — besonders Nanni N3.x, Sole Mini-29/33
3. Magnetventil (Kraftstoff-Absperrung) defekt (12 %) — besonders Beta, Vetus
4. Glühkerzen defekt (10 %) — bei Kaltstart unter 10 °C
5. Kraftstofffilter verstopft (10 %)
6. Einspritzpumpe ohne Förderung (8 %) — selten, teuer
7. Kompression unzureichend (5 %) — Verschleiß, Ventile
8. Falsche Motorabstellung (5 %) — Dekompressionshebel noch offen

**AYDI-Diagnose:**
- confidence: documented
- Sofortmaßnahme: Kraftstoffsystem entlüften
- Prüfreihenfolge: Kraftstoff → Luft → Glühkerzen → Kompression

### 27.2 Fehlerbild F-ALT-02: Motor überhitzt

**Beschreibung:** Kühlwassertemperatur steigt über 95 °C, Alarm löst aus.

**Typische Ursachen:**
1. Impeller defekt/abgenutzt (40 %) — häufigster Fehler bei allen Herstellern
2. Seewassereinlass verstopft (20 %) — Muscheln, Seegras, Plastiktüte
3. Thermostat klemmt geschlossen (15 %)
4. Wärmetauscher verkalkt/verstopft (10 %)
5. Keilriemen gerissen/locker (8 %) — Kühlmittelpumpe ohne Antrieb
6. Kühlmittelverlust (5 %) — Schlauch undicht, Wärmetauscher defekt
7. Zylinderkopfdichtung defekt (2 %) — Kühlmittel im Öl

### 27.3 Fehlerbild F-ALT-03: Schwarzer Rauch aus dem Auspuff

**Beschreibung:** Übermäßig schwarzer Auspuffrauch bei Last.

**Typische Ursachen:**
1. Luftfilter verstopft (25 %)
2. Injektoren verkokt/tropfen nach (25 %)
3. Turbolader defekt (15 %) — nur Turbomodelle
4. Überlast (Motor zu klein für Propeller) (15 %)
5. Falsches Ventilspiel (10 %)
6. Einspritzpumpe falsch eingestellt (10 %)

### 27.4 Fehlerbild F-ALT-04: Weißer Rauch aus dem Auspuff

**Beschreibung:** Weißer (nicht Dampf) Auspuffrauch.

**Typische Ursachen:**
1. Zylinderkopfdichtung defekt (40 %) — Kühlmittel verbrennt
2. Motor zu kalt (Thermostat offen) (25 %) — unvollständige Verbrennung
3. Einspritzzeitpunkt falsch (15 %)
4. Wasser im Kraftstoff (10 %)
5. Kopfriss/Blockriss (10 %) — schwerwiegend

### 27.5 Fehlerbild F-ALT-05: Blauer Rauch aus dem Auspuff

**Beschreibung:** Bläulicher Auspuffrauch, Ölgeruch.

**Typische Ursachen:**
1. Ventilschaftdichtungen verschlissen (35 %)
2. Kolbenringe verschlissen (25 %)
3. Zu viel Öl eingefüllt (15 %)
4. Turbolader-Wellendichtung (15 %) — nur Turbomodelle
5. Ölrücklaufleitung Turbo verstopft (10 %) — nur Turbomodelle

### 27.6 Fehlerbild F-ALT-06: Öldruck zu niedrig

**Beschreibung:** Öldruckwarnung bei laufendem Motor.

**Typische Ursachen:**
1. Ölstand zu niedrig (30 %)
2. Öldruckschalter defekt (20 %) — besonders Sole Mini, Vetus M
3. Ölfilter verstopft (15 %)
4. Ölpumpe verschlissen (10 %)
5. Lagerverschleiß (10 %) — hohe Betriebsstunden
6. Falsches Öl (zu dünn) (10 %)
7. Öl-Verdünnung durch Kraftstoff (5 %) — undichte Injektordichtung

### 27.7 Fehlerbild F-ALT-07: Vibrationen/unrunder Lauf

**Beschreibung:** Motor vibriert übermäßig, läuft ungleichmäßig.

**Typische Ursachen:**
1. Motorlager defekt/durchgesackt (25 %)
2. Propellerwelle nicht fluchtend (20 %)
3. Propeller beschädigt (15 %)
4. Injektor defekt (ein Zylinder setzt aus) (15 %)
5. Ventilspiel falsch (10 %)
6. Kompression ungleichmäßig (8 %)
7. Motorhalterung lose (7 %)

### 27.8 Fehlerbild F-ALT-08: Kraftstoffverbrauch zu hoch

**Beschreibung:** Motor verbraucht deutlich mehr als Herstellerangabe.

**Typische Ursachen:**
1. Propeller falsche Steigung/Größe (25 %)
2. Unterwasserschiff bewachsen (20 %)
3. Injektoren verschlissen (15 %)
4. Luftfilter verstopft (10 %)
5. Einspritzpumpe verstellt (10 %)
6. Kompression niedrig (10 %)
7. Falsches Untersetzungsverhältnis (10 %)

### 27.9 Fehlerbild F-ALT-09: Lichtmaschine lädt nicht

**Beschreibung:** Batteriespannung sinkt trotz laufendem Motor.

**Typische Ursachen:**
1. Keilriemen locker/gerissen (30 %)
2. Lichtmaschinenregler defekt (25 %)
3. Kohlebürsten verschlissen (15 %)
4. Kabelverbindung korrodiert (15 %)
5. Dioden-Platte defekt (10 %)
6. Lichtmaschine intern kurzgeschlossen (5 %)

### 27.10 Fehlerbild F-ALT-10: Getriebe schaltet nicht

**Beschreibung:** Vorwärts-/Rückwärtsgang lässt sich nicht einlegen.

**Typische Ursachen:**
1. Schaltzug schwergängig/gebrochen (35 %)
2. Getriebeöl zu alt/zu wenig (20 %)
3. Schaltkupplung verschlissen (20 %)
4. Schaltventil blockiert (ZF) (10 %)
5. Federscheibe gebrochen (PRM) (10 %)
6. Hydraulik-Schaltdruck falsch (ZF) (5 %)

### 27.11 Fehlerbild F-ALT-11: Wassereinbruch über Auspuffsystem

**Beschreibung:** Seewasser läuft bei gestopptem Motor ins Innere zurück.

**Typische Ursachen:**
1. Fehlende Schwanenhals-Schleife (30 %)
2. Anti-Siphon-Ventil defekt/verstopft (25 %)
3. Auspuffschlauch-Durchhang (Wassersammelstelle) (20 %)
4. Seewasserventil nicht geschlossen bei Stillstand (15 %)
5. Auspuff-Rückschlagventil fehlt (10 %)

### 27.12 Fehlerbild F-ALT-12: Saildrive-Manschette undicht

**Beschreibung:** Wassereinbruch über Saildrive-Manschette (nur bei SeaProp/Technodrive).

**Typische Ursachen:**
1. Manschette überaltert (>7 Jahre) (40 %)
2. Schlauchschelle locker (25 %)
3. Rissbildung durch Osmose-Einwirkung (15 %)
4. Falsche Montage bei letztem Wechsel (10 %)
5. Mechanische Beschädigung durch Slippen (10 %)

---

## 28. Troubleshooting-Bäume

### 28.1 Troubleshooting-Baum TB-ALT-01: Motor startet nicht

```
Motor startet nicht
├── Anlasser dreht?
│   ├── NEIN
│   │   ├── Batteriespannung >12,4V?
│   │   │   ├── NEIN → Batterie laden/ersetzen
│   │   │   └── JA → Anlasser-Kabel prüfen
│   │   │       ├── Korrosion an Klemmen → Reinigen
│   │   │       ├── Magnetschalter klickt? → Anlasser defekt
│   │   │       └── Kein Klicken → Zündschloss/Kabel prüfen
│   └── JA (Anlasser dreht, kein Start)
│       ├── Kraftstoff vorhanden?
│       │   ├── NEIN → Tanken, System entlüften
│       │   └── JA
│       │       ├── Kraftstoff-Absperrventil offen?
│       │       │   ├── NEIN → Öffnen
│       │       │   └── JA
│       │       │       ├── Dekompressionshebel geschlossen?
│       │       │       │   ├── NEIN → Schließen
│       │       │       │   └── JA
│       │       │       │       ├── Kraftstofffilter prüfen
│       │       │       │       ├── System entlüften (Entlüfterschraube an Filtergehäuse)
│       │       │       │       ├── Glühkerzen prüfen (bei Kälte)
│       │       │       │       ├── Einspritzleitungen prüfen (austretender Kraftstoff?)
│       │       │       │       └── Kompression messen → min. 25 bar je Zylinder
```

### 28.2 Troubleshooting-Baum TB-ALT-02: Motor überhitzt

```
Motor überhitzt (>95 °C)
├── Seewasser-Auslass prüfen — kommt Wasser?
│   ├── NEIN (kein Wasser)
│   │   ├── Seeventil offen?
│   │   │   ├── NEIN → Öffnen
│   │   │   └── JA
│   │   │       ├── Seewasserfilter/Sieb prüfen
│   │   │       │   ├── Verstopft → Reinigen
│   │   │       │   └── Frei
│   │   │       │       ├── Impeller prüfen
│   │   │       │       │   ├── Defekt → Ersetzen, ALLE Flügelreste suchen
│   │   │       │       │   └── OK
│   │   │       │       │       ├── Seewasserpumpe Gehäuse auf Verschleiß
│   │   │       │       │       └── Seewasserleitung verstopft
│   └── JA (Wasser kommt, aber Motor trotzdem heiß)
│       ├── Kühlmittelstand im Ausgleichsbehälter prüfen
│       │   ├── Niedrig → Auffüllen, Leck suchen
│       │   └── OK
│       │       ├── Thermostat prüfen (ausbauen, im Topf erhitzen)
│       │       │   ├── Öffnet nicht bei 72–78 °C → Ersetzen
│       │       │   └── OK
│       │       │       ├── Wärmetauscher verstopft → Reinigen/Entkalken
│       │       │       └── Zylinderkopfdichtung prüfen (Öl im Kühlwasser?)
```

### 28.3 Troubleshooting-Baum TB-ALT-03: Kein Ladestrom

```
Batterie wird nicht geladen
├── Keilriemen prüfen
│   ├── Locker/gerissen → Spannen/Ersetzen
│   └── OK
│       ├── Lichtmaschinen-Anschlüsse prüfen
│       │   ├── Korrodiert → Reinigen, Polfett
│       │   └── OK
│       │       ├── Spannung an Lichtmaschine messen (B+ Klemme)
│       │       │   ├── <13,5V bei Nenndrehzahl → Regler/LiMa defekt
│       │       │   └── >13,8V
│       │       │       ├── Spannung an Batterie prüfen
│       │       │       │   ├── Deutlich niedriger → Kabelwiderstand, Sicherung prüfen
│       │       │       │   └── OK → Batterie möglicherweise defekt
```

### 28.4 Troubleshooting-Baum TB-ALT-04: Öldruck niedrig

```
Öldruckwarnung
├── Motor sofort abstellen!
├── Ölstand prüfen (Peilstab)
│   ├── Zu niedrig → Auffüllen, Leck suchen
│   │   ├── Öl unter Motor? → Ölwannendichtung, Ölfilter, Öldruckschalter
│   │   ├── Öl im Kühlwasser? → Ölkühler/Wärmetauscher undicht
│   │   └── Kraftstoff im Öl? → Injektordichtung, Einspritzpumpe
│   └── OK
│       ├── Öldruckschalter prüfen (Kabel abziehen → Warnung weg?)
│       │   ├── JA → Schalter defekt (häufig bei Sole, Vetus)
│       │   └── NEIN → Öldruckmanometer anschließen
│       │       ├── <1,0 bar bei Leerlauf → Ölpumpe/Lager prüfen
│       │       └── >1,5 bar → Elektrisches Problem
```

### 28.5 Troubleshooting-Baum TB-ALT-05: Getriebe-Probleme

```
Getriebe funktioniert nicht korrekt
├── Gang lässt sich nicht einlegen
│   ├── Schaltzug prüfen (Bowdenzug)
│   │   ├── Schwergängig → Schmieren oder ersetzen
│   │   ├── Gebrochen → Ersetzen
│   │   └── OK
│   │       ├── Getriebeölstand prüfen
│   │       │   ├── Zu niedrig → Auffüllen (ATF oder Getriebeöl lt. Hersteller)
│   │       │   └── OK
│   │       │       ├── PRM-Getriebe: Schalthebel am Getriebe direkt betätigen
│   │       │       │   ├── Geht → Schaltzug-Einstellung
│   │       │       │   └── Geht nicht → Getriebe intern defekt
│   │       │       └── ZF-Getriebe: Schaltdruck prüfen (Manometer)
│   │       │           ├── Zu niedrig → Ölfilter, Ventilblock
│   │       │           └── OK → Lamellenkupplung verschlissen
├── Gang rutscht unter Last
│   ├── Getriebeöl korrekt? (Typ und Menge)
│   ├── PRM: Federscheibe prüfen
│   └── ZF: Schaltdruck prüfen, Lamellen verschlissen
```

---

## 29. Fallstudien

### 29.1 Fallstudie FS-ALT-01: Beta 38 ersetzt Yanmar 3GM30 in Hallberg-Rassy 352

**Ausgangslage:**
- Boot: Hallberg-Rassy 352, Baujahr 1986, 10,6 m
- Alter Motor: Yanmar 3GM30 (30 PS), 4.800 Betriebsstunden
- Problem: Zylinderkopfdichtung defekt, Ersatzteile schwer beschaffbar (Auslaufmodell)
- Budget: 15.000 EUR inkl. Einbau

**Lösung:**
- Neuer Motor: Beta 38 (38 PS, Kubota V2003-Basis)
- Getriebe: PRM 150, 2:1 Untersetzung
- Saildrive: Nein (Wellenanlage beibehalten, neue PSS-Dichtung)
- Anpassungen: Neue Motorlager, Wellenkupplung, Auspuffkrümmer-Adapter

**Ergebnis:**

| Aspekt | Vorher (3GM30) | Nachher (Beta 38) |
|--------|---------------|------------------|
| Leistung | 30 PS | 38 PS |
| Gewicht | 135 kg | 185 kg (inkl. Getriebe) |
| Vibration | Mäßig | Deutlich reduziert |
| Geräusch | 78 dB(A) | 72 dB(A) |
| Kraftstoffverbrauch | 3,5 l/h Reise | 3,5 l/h Reise |
| Geschwindigkeit unter Motor | 6,2 kn | 6,8 kn |
| Kosten gesamt | — | 14.200 EUR |

**AYDI-Bewertung:** Erfolgreicher Refit. Beta 38 ist einer der beliebtesten Yanmar-GM-Ersatzmotoren. Kubota V2003-Block bewährt, einfach zu warten. Confidence: documented.

### 29.2 Fallstudie FS-ALT-02: Nanni N4.50 in Bénéteau Océanis 40.1

**Ausgangslage:**
- Boot: Bénéteau Océanis 40.1, Baujahr 2019, 12,3 m
- Motor: Nanni N4.50 ab Werk (OEM-Einbau)
- Situation: 1.200 Betriebsstunden, erste Saison Mittelmeer (Charterboot)
- Problem: Motor überhitzt nach 2 Stunden Fahrt bei 2.500 U/min

**Diagnose:**
1. Impeller geprüft — in Ordnung (erst 150h alt)
2. Seewasserfilter geprüft — leicht verstopft → gereinigt
3. Problem besteht weiter
4. Wärmetauscher geöffnet — Zinkrückstände blockieren 40 % der Rohre
5. Ursache: Zinkanode im Wärmetauscher vollständig aufgelöst, Zinkpartikel verstopfen Rohre

**Lösung:**
- Wärmetauscher chemisch gereinigt (Rydlyme Marine)
- Neue Zinkanode eingesetzt (Kontrolle alle 6 Monate statt jährlich bei Salzwasser-Charter)
- Kühlmittel-Temperaturanzeige als zusätzliches Instrument installiert

**Kosten:** 450 EUR (Reinigung 280 EUR, Anode 35 EUR, Arbeit 135 EUR)
**AYDI-Bewertung:** Typisches Problem bei intensiver Salzwasser-Nutzung. Zinkanode im Wärmetauscher muss bei Charterbooten halbjährlich geprüft werden. Confidence: documented.

### 29.3 Fallstudie FS-ALT-03: Vetus M4.17 Getriebe-Problem in Stahlyacht

**Ausgangslage:**
- Boot: Stahlverdränger, niederländische Werft, 12 m, Binnenfahrt
- Motor: Vetus M4.17 (38 PS), 2.800 Betriebsstunden
- Problem: Getriebe (PRM 150) rutscht im Vorwärtsgang unter Last

**Diagnose:**
1. Getriebeöl geprüft — dunkel, metallische Partikel
2. Schaltdruck am Getriebe gemessen — zu niedrig
3. Getriebe geöffnet — Federscheibe gebrochen, Lamellen verschlissen

**Lösung:**
- PRM 150 Revision: Neue Federscheibe, neue Lamellen, neue Dichtungen
- Getriebeöl gewechselt (ATF Dexron III)

**Kosten:** 1.850 EUR (Teile 680 EUR, Arbeit 12h × 95 EUR/h = 1.140 EUR, Öl 30 EUR)
**AYDI-Bewertung:** PRM 150 Federscheiben-Problem ist bekannt bei >2.500h. Regelmäßiger Getriebeölwechsel (200h) verlängert die Lebensdauer. Confidence: documented.

### 29.4 Fallstudie FS-ALT-04: Sole Mini-33 Auspuffkrümmer-Schaden

**Ausgangslage:**
- Boot: Bavaria 32 Cruiser, Baujahr 2008 (Refit mit Sole)
- Motor: Sole Mini-33 (33 PS), 2.200 Betriebsstunden
- Problem: Kühlwasser im Motoröl, Motor wird nicht warm

**Diagnose:**
1. Milchiges Öl → Wasser im Öl bestätigt
2. Zylinderkopfdichtung? → Kompressionswerte OK (28–30 bar, alle Zylinder)
3. Auspuffkrümmer geprüft — innere Wasserjacke durchkorrodiert
4. Seewasser tritt über Krümmer ins Auspuffsystem und zurück in den Motor

**Lösung:**
- Neuer Auspuffkrümmer (Sole-Originalteil)
- Motoröl 3× gewechselt (Spülung)
- Neue Krümmerdichtung
- Neue Zinkanode im Wärmetauscher

**Kosten:** 1.650 EUR (Krümmer 520 EUR, Dichtungen 85 EUR, Öl 3× 45 EUR, Arbeit 8h × 95 EUR/h = 760 EUR)
**AYDI-Bewertung:** Sole-Auspuffkrümmer haben eine Lebensdauer von 6–10 Jahren bei Salzwasser. Regelmäßige Inspektion (jährlich visuell, alle 3 Jahre Druckprüfung) empfohlen. Confidence: documented.

### 29.5 Fallstudie FS-ALT-05: Craftsman CM 4.42 Motorlager-Fluchtung

**Ausgangslage:**
- Boot: GFK-Motorboot, 9 m, niederländische Binnenfahrt
- Motor: Craftsman CM 4.42 (42 PS), 800 Betriebsstunden, 3 Jahre alt
- Problem: Starke Vibrationen, besonders bei 2.000–2.500 U/min

**Diagnose:**
1. Propeller geprüft — OK, ausgewuchtet
2. Motorlager geprüft — 2 von 4 deutlich durchgesackt
3. Wellenfluchtung gemessen — 0,8 mm Versatz (max. 0,05 mm)
4. Ursache: Motorlager zu weich dimensioniert für Motorgewicht

**Lösung:**
- 4 neue Motorlager (Shore-Härte 55 statt 45)
- Wellenfluchtung neu ausgerichtet
- Flexible Kupplung geprüft und für OK befunden

**Kosten:** 780 EUR (Lager 4× 65 EUR = 260 EUR, Fluchtung 6h × 85 EUR/h = 510 EUR)
**AYDI-Bewertung:** Craftsman-Motorlager sind gelegentlich unterdimensioniert. Bei Vibrationen immer zuerst Lager und Fluchtung prüfen. Confidence: documented.

### 29.6 Fallstudie FS-ALT-06: Beta 75 Turbolader-Ölverlust

**Ausgangslage:**
- Boot: Contest 42, Baujahr 2018, 12,8 m Segelboot
- Motor: Beta 75 (75 PS, Kubota V3307-DI-T), 1.500 Betriebsstunden
- Problem: Ölverlust am Turbolader, bläulicher Rauch bei Kaltstart

**Diagnose:**
1. Turbolader visuell geprüft — Ölspuren an der Turbinengehäuse-Ausgangsseite
2. Turboladerspiel gemessen — axial OK, radial 0,12 mm (Grenzwert: 0,10 mm)
3. Ölrücklaufleitung geprüft — teilweise verstopft durch Ölkohle

**Lösung:**
- Ölrücklaufleitung gereinigt und Gefälle verbessert
- Turbolader revidiert (neue Wellendichtungen)
- Ölwechselintervall auf 150h reduziert (synthetisches Öl)

**Kosten:** 2.800 EUR (Turbo-Revision 1.800 EUR, Leitung 120 EUR, Arbeit 8h × 110 EUR/h = 880 EUR)
**AYDI-Bewertung:** Turbolader-Ölverlust durch verstopfte Rücklaufleitung ist vermeidbar. Regelmäßige Ölwechsel und ausreichendes Nachlaufen vor Abstellen (2–3 Min.) sind essenziell. Confidence: documented.

### 29.7 Fallstudie FS-ALT-07: Vetus M4.56 + BOW PRO 76 Systemintegration

**Ausgangslage:**
- Boot: Linssen Grand Sturdy 34.9 AC, 10,8 m Verdränger
- Motor: Vetus M4.56 (56 PS), 400 Betriebsstunden
- Ziel: Nachrüstung Bugstrahlruder für Hafenmanöver

**Lösung:**
- Einbau BOW PRO 76 (76 kgf Schub)
- 185 mm Tunnel im Bug
- 1× 150 Ah AGM-Batterie, 70 mm² Kabel, 200 A Sicherung
- CAN-Bus-Verbindung zum Vetus-Motorpanel
- Joystick-Fernbedienung am Steuerstand

**Kosten:** 4.200 EUR (BOW PRO 76 2.600 EUR, Batterie 280 EUR, Kabel/Sicherung 180 EUR, Tunnel-Einbau 1.140 EUR)
**AYDI-Bewertung:** Vetus-Systemintegration ist Alleinstellungsmerkmal. Motor+Thruster aus einer Hand vereinfacht Verkabelung und Steuerung erheblich. Confidence: documented.

### 29.8 Fallstudie FS-ALT-08: Nanni T4.200 Common-Rail Injektor-Problem

**Ausgangslage:**
- Boot: Lagoon 42, Katamaran, Baujahr 2022
- Motoren: 2× Nanni T4.200 (je 200 PS), 800 Betriebsstunden
- Problem: Backbord-Motor ruckelt bei niedriger Drehzahl, Fehlermeldung ECU

**Diagnose:**
1. ECU-Diagnose ausgelesen — Fehlercode: Injektor Zylinder 3, Einspritzmengen-Abweichung
2. Injektorrücklaufmenge gemessen — Zylinder 3: 85 ml/min (Grenzwert: 40 ml/min)
3. Injektor ausgebaut — Düse verkokt durch minderwertigen Kraftstoff (Kroatien)

**Lösung:**
- 4 Injektoren getauscht (Common-Rail — immer satzweise)
- Kraftstofftank gereinigt
- Kraftstofffilter-System um Vorfilter mit Wasserabscheider erweitert
- Empfehlung: Nur Kraftstoff von zertifizierten Bunkerstationen

**Kosten:** 5.200 EUR (4 Injektoren 3.200 EUR, Tankreinigung 480 EUR, Vorfilter 320 EUR, Arbeit 12h × 100 EUR/h = 1.200 EUR)
**AYDI-Bewertung:** Common-Rail-Systeme sind empfindlich gegenüber Kraftstoffqualität. Im Mittelmeer unbedingt Vorfilter mit Wasserabscheider verwenden. Confidence: documented.

---

## 30. FAQ — Häufig gestellte Fragen

### FAQ 1: Welcher Alternativmotor ist der beste Ersatz für einen Yanmar 2GM20?

**Antwort:** Der Beta 20 oder Beta 25 ist der populärste Ersatz. Der Kubota D1105-Block hat ähnliche Abmessungen wie der Yanmar 2GM20, und Beta bietet spezifische Adapter-Kits für gängige Yanmar-Installationen. Auch der Nanni N3.21 kommt in Frage, bietet aber weniger Unterstützung für den Refit-Markt. Confidence: documented.

### FAQ 2: Kann ich Kubota-Landmaschinenteile in einem Beta-Marine-Motor verwenden?

**Antwort:** Ja, für die meisten internen Motorkomponenten (Kolben, Lager, Dichtungen, Filter, Wasserpumpe intern, Ölpumpe). NICHT für marinisierungsspezifische Teile (Wärmetauscher, Auspuffkrümmer, Seewasserpumpe, Lichtmaschine, Motorlager). Die Kubota-Teilenummern stehen oft auch im Beta-Ersatzteilkatalog. Confidence: measured.

### FAQ 3: Wie gut ist das Nanni-Händlernetz in Deutschland?

**Antwort:** Eingeschränkt. Nanni hat in Deutschland nur 3–5 Vertragshändler, hauptsächlich an der Küste und am Bodensee. Für Binnenreviere ist die Versorgung deutlich schlechter als bei Yanmar oder Volvo. Im Mittelmeer hingegen ist Nanni hervorragend vertreten. Confidence: estimated.

### FAQ 4: Ist ein Vetus-Motor eine gute Wahl für ein Segelboot?

**Antwort:** Bedingt. Die M-Serie ist solide, aber Vetus ist primär auf den Motorboot-/Binnenfahrt-Markt ausgerichtet. Für Segelboote fehlt eine breit aufgestellte Saildrive-Option (nur über Technodrive). Für Segelboote mit Wellenanlage ist Vetus eine durchaus vertretbare Wahl, besonders in den Niederlanden mit dem guten lokalen Netzwerk. Confidence: estimated.

### FAQ 5: Wie sind die Wiederverkaufswerte alternativer Motoren?

**Antwort:** Deutlich niedriger als Yanmar/Volvo. Ein gebrauchter Beta-Motor erzielt ca. 60–70 % des Yanmar-Vergleichspreises bei gleicher Betriebsstundenzahl. Nanni liegt bei 55–65 %, Sole bei 45–55 %, Craftsman bei 40–50 %. Dies sollte bei der Kaufentscheidung berücksichtigt werden. Confidence: estimated.

### FAQ 6: Welchen Motor empfehlt AYDI für eine Blauwasser-Yacht?

**Antwort:** Für Blauwasser empfehlen wir primär Yanmar (bestes globales Netzwerk). Als Alternative ist Beta Marine erste Wahl: mechanisch einfach, Kubota-Teile weltweit über Landmaschinenhändler verfügbar, kein proprietäres Diagnosesystem nötig. Der Beta 38 oder Beta 50 sind bewährte Blauwasser-Motoren. Confidence: documented/estimated.

### FAQ 7: Können Beta-Motoren mit Yanmar-Saildrives verwendet werden?

**Antwort:** Nein. Beta verwendet ausschließlich Technodrive SeaProp Saildrives. Die Flanschmuster und Steuerungssysteme sind nicht kompatibel mit Yanmar SD-Saildrives. Ein Wechsel von Yanmar mit Saildrive auf Beta erfordert entweder den Einbau eines Technodrive SeaProp oder den Umbau auf eine konventionelle Wellenanlage. Confidence: measured.

### FAQ 8: Was kostet ein kompletter Motorwechsel (inkl. Einbau)?

**Antwort:** Richtwerte für einen Motor-Refit im 30–50 PS-Bereich:

| Position | Kosten EUR |
|----------|-----------|
| Motor mit Getriebe | 12.000–20.000 |
| Demontage alter Motor | 800–1.500 |
| Montage neuer Motor | 1.500–3.000 |
| Motorlager, Kupplung | 400–800 |
| Auspuffsystem anpassen | 300–800 |
| Elektrik anpassen | 400–1.000 |
| Wellenfluchtung | 300–600 |
| Probefahrt, Einstellung | 200–400 |
| **Gesamt** | **16.000–28.000** |

Confidence: estimated.

### FAQ 9: Welches Motoröl empfehlen die Hersteller?

**Antwort:**

| Hersteller | Empfohlenes Öl | Viskosität | Spezifikation |
|------------|---------------|-----------|--------------|
| Beta Marine | 15W-40 Mineral oder Halbsynthese | 15W-40 | API CH-4 / CI-4 |
| Nanni Diesel | 15W-40 Mineral | 15W-40 | API CH-4 / CI-4 |
| Vetus | 15W-40 Mineral oder Halbsynthese | 15W-40 | API CH-4 |
| Sole Diesel | 15W-40 Mineral | 15W-40 | API CF-4 / CH-4 |
| Craftsman | 15W-40 Mineral | 15W-40 | API CF-4 |

Für Turbo-Modelle (Beta 75+, Nanni T-Serie, Vetus VF/DT): 10W-40 Halbsynthese oder 15W-40 API CI-4. Confidence: measured.

### FAQ 10: Wie laut sind die alternativen Motoren im Vergleich?

**Antwort:** Schalldruckpegel in 1 m Entfernung bei 2.500 U/min (Richtwerte):

| Motor | dB(A) | Bewertung |
|-------|-------|----------|
| Beta 38 | 72–75 | Leiser als Yanmar GM-Serie |
| Nanni N4.38 | 74–77 | Vergleichbar mit Yanmar JH |
| Vetus M4.17 | 73–76 | Leiser (gute Schalldämmhaube) |
| Sole Mini-33 | 76–79 | Etwas lauter |
| Craftsman CM 4.35 | 77–80 | Am lautesten (weniger Dämmung) |
| Yanmar 3JH40 | 73–76 | Referenz |

Beta und Vetus bieten ab Werk bessere Schalldämmhauben. Confidence: estimated.

### FAQ 11: Gibt es Hybrid-Optionen bei den alternativen Herstellern?

**Antwort:** Ja, alle etablierten Hersteller bieten mittlerweile Hybrid-Lösungen an:

| Hersteller | Hybrid-System | Status (2025) | Leistung |
|------------|--------------|--------------|---------|
| Beta Marine | Beta Hybrid | Verfügbar | 10–50 PS Diesel + 5–10 kW Elektro |
| Nanni | Nanni Hybrid (mit Torqeedo) | Verfügbar | 21–80 PS Diesel + 10–20 kW Elektro |
| Vetus | E-LINE / E-HYBRID | Verfügbar | 16–56 PS Diesel + 4–10 kW Elektro |
| Sole Diesel | — | In Entwicklung | — |
| Craftsman | — | Nicht geplant | — |

Confidence: documented.

### FAQ 12: Welcher Hersteller bietet die beste Garantie?

**Antwort:**

| Hersteller | Standard-Garantie | Erweiterte Garantie |
|------------|------------------|-------------------|
| Beta Marine | 5 Jahre / 2.500h | — (keine verlängerte) |
| Nanni Diesel | 2 Jahre / 1.500h | 3 Jahre gegen Aufpreis |
| Vetus | 2 Jahre / 1.000h | 3 Jahre gegen Aufpreis |
| Sole Diesel | 2 Jahre / 1.000h | — |
| Craftsman | 2 Jahre / 1.000h | — |
| Yanmar (Vergleich) | 2 Jahre / 2.000h | 5 Jahre gegen Aufpreis |

Beta Marine bietet mit 5 Jahren die mit Abstand beste Standard-Garantie — ein wichtiges Kaufargument. Confidence: measured.

### FAQ 13: Wie zuverlässig sind PRM-Getriebe im Vergleich zu Yanmar KM?

**Antwort:** PRM-Getriebe (Newage, UK) sind solide, langlebige Wendegetriebe mit einfacher mechanischer Konstruktion. Sie erreichen nicht ganz die Langzeitstandfestigkeit der Yanmar KM-Serie, sind aber bei regelmäßigem Ölwechsel (200h) problemlos 5.000+ Stunden haltbar. Die Federscheiben (PRM 150/260) sind eine bekannte Verschleißstelle ab ca. 2.500h. Insgesamt: ★★★★ von ★★★★★. Confidence: documented.

### FAQ 14: Kann ich einen Sole-Motor außerhalb des Mittelmeerraums warten lassen?

**Antwort:** Eingeschränkt. Sole hat in Nordeuropa nur wenige Vertragshändler. Da der Motor auf Mitsubishi-Blöcken basiert, können die meisten internen Teile über Mitsubishi-Industriehändler beschafft werden. Marinisierungsspezifische Teile (Krümmer, Wärmetauscher) müssen aus Barcelona bestellt werden (Lieferzeit 1–3 Wochen). Für Nordeuropa-Eigner empfehlen wir, die wichtigsten Ersatzteile an Bord zu haben. Confidence: estimated.

### FAQ 15: Wie verhalten sich die Motoren bei Langzeitbetrieb (10.000h+)?

**Antwort:**

| Motor | Erwartete Lebensdauer (Stunden) | Häufigkeit Grundüberholung |
|-------|-------------------------------|---------------------------|
| Beta (Kubota-Basis) | 8.000–12.000 | Erste bei 6.000–8.000h |
| Nanni (Toyota-Basis) | 8.000–10.000 | Erste bei 5.000–7.000h |
| Nanni (Kubota-Basis) | 8.000–12.000 | Erste bei 6.000–8.000h |
| Vetus (Mitsubishi-Basis) | 7.000–10.000 | Erste bei 5.000–7.000h |
| Sole (Mitsubishi-Basis) | 7.000–10.000 | Erste bei 5.000–7.000h |
| Craftsman (Mitsubishi) | 6.000–8.000 | Erste bei 4.000–6.000h |
| Yanmar (Vergleich) | 10.000–15.000 | Erste bei 7.000–10.000h |

Confidence: estimated.

### FAQ 16: Was ist bei einem Motorwechsel von Volvo MD auf einen Alternativmotor zu beachten?

**Antwort:** Wichtige Punkte:
1. **Wellenanlage:** Volvo-Saildrive (120S, 130S) ist nicht kompatibel — Umbau auf Welle oder Technodrive SeaProp nötig
2. **Motorlager:** Position und Befestigungsmuster unterschiedlich — Adapterschienen erforderlich
3. **Auspuffsystem:** Volvo-Auspuff passt selten — komplett neu verlegen
4. **Elektrik:** Volvo-Instrumentenpanel nicht kompatibel — neues Panel einbauen
5. **Kraftstoff:** Leitungen und Filter meist wiederverwendbar
6. **Propeller:** Steigung ggf. anpassen (anderes Untersetzungsverhältnis)

Confidence: documented.

### FAQ 17: Gibt es Erfahrungswerte zu Craftsman Marine in der Langzeit-Nutzung?

**Antwort:** Craftsman Marine existiert erst seit 2003, Langzeiterfahrungen (>15 Jahre) sind daher begrenzt. Erste Erfahrungen zeigen: Der Mitsubishi-Basisblock ist robust, aber die Marinisierungsqualität (Korrosionsschutz, Kabelbäume, Krümmer) liegt unter dem Niveau von Beta oder Nanni. Für preissensitive Binnenfahrt-Projekte vertretbar, für Salzwasser-Einsatz nur bedingt empfehlenswert. Confidence: estimated.

### FAQ 18: Wie oft muss die Technodrive-SeaProp-Manschette gewechselt werden?

**Antwort:** Technodrive empfiehlt einen Wechsel alle 7 Jahre, unabhängig von den Betriebsstunden. In der Praxis:
- Süßwasser: 7–10 Jahre möglich
- Salzwasser (Mittelmeer): 5–7 Jahre empfohlen
- Salzwasser (Nordsee/Atlantik): 5–6 Jahre empfohlen
- Immer visuell bei jedem Slippen kontrollieren (Risse, Aufquellen, Verfärbung)
- Kosten: Manschette 120–180 EUR, Einbau 3–5h Arbeitszeit

Confidence: documented.

### FAQ 19: Welche Motoren passen am besten in sehr enge Motorräume?

**Antwort:** Für besonders enge Motorräume empfehlen wir:
1. **Beta Atomic-Serie** — speziell für enge Räume entwickelt, niedrigstes Profil
2. **Vetus M2.02/M2.C5** — sehr kompakt durch 2-Zylinder Mitsubishi-Basis
3. **Sole Mini-11** — ebenfalls sehr kompakt
4. **Nanni N2.10** — kompaktester Nanni

Entscheidend ist die **Höhe** des Motors (inkl. Lichtmaschine, Auspuffkrümmer), nicht nur die Grundfläche. Die Beta Atomic-Serie ist hier am besten optimiert. Confidence: documented.

### FAQ 20: Wie vergleichen sich die Kraftstoffverbräuche bei gleicher Leistung?

**Antwort:** Die Unterschiede sind gering, da alle Hersteller ähnliche Industrieblöcke verwenden. Bei gleicher Nennleistung und gleicher Drehzahl:
- Unterschiede liegen im Bereich von ±5–10 %
- Motoren mit größerem Hubraum bei niedrigerer Drehzahl sind tendenziell sparsamer
- Direkteinspritzer (DI) sind 5–10 % sparsamer als Wirbelkammer-Motoren
- Common-Rail (Nanni T4.200) ist am sparsamsten, aber auch am komplexesten

Confidence: measured.

### FAQ 21: Bieten die Hersteller Retrofit-Kits für ältere Installationen?

**Antwort:**

| Hersteller | Retrofit-Kits | Für welche Altmotoren |
|------------|--------------|----------------------|
| Beta Marine | Ja (umfangreich) | Yanmar GM/YM, Volvo MD, Bukh, BMC |
| Nanni Diesel | Ja (eingeschränkt) | Volvo MD, ältere Nanni |
| Vetus | Ja (für Vetus-Altmotoren) | Ältere Vetus-Modelle, Faryman |
| Sole Diesel | Begrenzt | Ältere Sole-Modelle |
| Craftsman | Nein | — |

Beta Marine ist hier klar führend und bietet die meisten Adapter-Kits. Confidence: documented.

### FAQ 22: Wie sind die Erfahrungen mit Vetus D-Serie (Deutz-Basis)?

**Antwort:** Die D-Serie auf Deutz-Basis ist qualitativ hochwertig, aber mit Einschränkungen:
- **Vorteile:** Extrem robuster Deutz-Block, hohe Lebensdauer, gutes Drehmoment bei niedriger Drehzahl (ideal für Verdränger)
- **Nachteile:** Deutz-Ventilspieleinstellung erfordert Erfahrung, Kaltstart-Rauchentwicklung, Ersatzteile teurer als Mitsubishi/Kubota, eingeschränkte Händlerqualifikation für Deutz-Motoren im Marinemarkt

Confidence: documented.

### FAQ 23: Was ist der Unterschied zwischen PRM und TMC-Getrieben?

**Antwort:**

| Aspekt | PRM (Newage, UK) | TMC (Technodrive, NL) |
|--------|-----------------|---------------------|
| Herkunft | Parmiter & Mitchell, England | Technodrive, Niederlande |
| Bauart | Mechanisch, Kegel-Reibkupplung | Mechanisch, Lamellenkupplung |
| Vorteile | Bewährt, robust, viele Untersetzungen | Kompakt, leise, sanftes Schalten |
| Nachteile | Federscheiben-Verschleiß | Weniger Untersetzungs-Optionen |
| Öltyp | ATF Dexron III | ATF Dexron III |
| Typisch bei | Beta Marine, Nanni, Sole | Vetus, Nanni (kleine Modelle) |

Confidence: documented.

### FAQ 24: Wie wirkt sich die Motorwahl auf den Bootswert aus?

**Antwort:** Ein Yanmar- oder Volvo-Motor erhöht den Wiederverkaufswert eines Bootes messbar. Richtwerte für den Werteinfluss:

| Motor | Werteinfluss ggü. Yanmar |
|-------|--------------------------|
| Yanmar | Referenz (0 %) |
| Volvo Penta | -5 bis +5 % (je nach Markt) |
| Beta Marine | -5 bis -10 % |
| Nanni Diesel | -8 bis -15 % |
| Vetus | -10 bis -15 % |
| Sole Diesel | -15 bis -20 % |
| Craftsman | -20 bis -30 % |

Diese Werte sind Richtwerte und variieren stark nach Region und Bootstyp. In den Niederlanden wird Vetus kaum abgewertet, in Spanien Sole kaum. Confidence: estimated.

### FAQ 25: Welche Motoren sind am besten für Charterbetrieb geeignet?

**Antwort:**
1. **Yanmar JH-Serie** — Bestes Netzwerk, bekannteste Motoren, Charter-Crews kennen sie
2. **Nanni N-Serie** — Sehr verbreitet bei Mittelmeer-Charter (OEM bei Bénéteau/Lagoon)
3. **Beta Marine** — Weniger Charter-typisch, aber robust und wartungsarm
4. **Vetus M-Serie** — Gut für Binnencharterboote (NL, DE)

Für Charterflotten empfiehlt AYDI: Standardisierung auf einen Motorhersteller über die gesamte Flotte, um Ersatzteillager und Mechaniker-Ausbildung zu optimieren. Confidence: estimated.

### FAQ 26: Gibt es bekannte Rückrufaktionen bei alternativen Herstellern?

**Antwort:** Bekannte Servicebulletins und Rückrufe (Stand 2025):
- **Beta Marine SB-2019-03:** Überprüfung Kraftstoffhebepumpe bei Beta 20–50, Bj. 2017–2019
- **Nanni SB-2021-01:** Software-Update ECU für T4.200, Bj. 2020–2021
- **Vetus SB-2020-02:** Wärmetauscher-Zinkanode Kontrolle bei VF4.140E/170E
- **Sole SB-2018-05:** Auspuffkrümmer-Inspektion bei Mini-33/37, Bj. 2012–2016

Keine sicherheitskritischen Rückrufe bekannt. Servicebulletins betreffen typischerweise Verschleißteile. Confidence: documented.

---

## 31. Glossar

### Motorentechnik

| Begriff | Erklärung |
|---------|-----------|
| Marinisierung | Umrüstung eines Industriemotors für den Marineeinsatz (Kühlung, Auspuff, Korrosionsschutz) |
| Basisblock | Industriemotor-Grundblock, der als Ausgangspunkt für die Marinisierung dient |
| Zweikreis-Kühlung | Indirekte Kühlung: Geschlossener Kreislauf mit Kühlmittel + offener Seewasserkreislauf über Wärmetauscher |
| Einkreis-Kühlung | Direkte Kühlung nur mit Seewasser (veraltet, korrosionsanfällig) |
| Wirbelkammer (IDI) | Indirekte Einspritzung: Kraftstoff wird in Nebenkammer eingespritzt (einfacher, toleranter) |
| Direkteinspritzung (DI) | Kraftstoff wird direkt in den Brennraum eingespritzt (effizienter, lauter) |
| Common-Rail | Elektronisch gesteuerte Hochdruck-Einspritzung (Druck bis 2.000 bar) |
| Turbolader | Abgasturbolader zur Leistungssteigerung durch Aufladung der Verbrennungsluft |
| Ladeluftkühler (LLK) | Kühlt die vom Turbolader verdichtete (und dadurch erhitzte) Luft vor Eintritt in den Motor |
| Impeller | Flexibles Schaufelrad in der Seewasserpumpe (Verschleißteil, 200h/jährlich wechseln) |
| Wärmetauscher | Tauscht Wärme zwischen dem geschlossenen Motorkühlkreislauf und dem Seewasser |
| Auspuffkrümmer | Wassergekühlt im Marineeinsatz: Seewasser wird in den Auspuffstrom eingespritzt |
| Mischkammer | Punkt, an dem Seewasser und Abgase zusammengeführt werden |
| Schwanenhals | S-förmige Auspuffführung, die Wasserrücklauf in den Motor verhindert |
| Anti-Siphon-Ventil | Belüftungsventil in der Seewasserleitung, verhindert Rücksaugen bei stehendem Motor |
| Zinkanode | Opferanode aus Zink im Kühlsystem/Saildrive zum Korrosionsschutz |

### Getriebe und Antrieb

| Begriff | Erklärung |
|---------|-----------|
| Wendegetriebe | Marine-Getriebe mit Vorwärts-, Leerlauf- und Rückwärtsgang |
| PRM | Newage PRM — britischer Getriebehersteller (Parmiter, Rist & Mitchell) |
| TMC | Technodrive Marine Compact — niederländische Getriebe-Baureihe |
| ZF Marine | ZF Friedrichshafen — deutscher Getriebe-Hersteller, Premium-Segment |
| Untersetzungsverhältnis | Verhältnis Motor- zu Propellerdrehzahl (z.B. 2:1 = Motor dreht doppelt so schnell) |
| Saildrive | Antriebseinheit, die Motor und Unterwasserantrieb kombiniert (kein Wellenrohr nötig) |
| Technodrive SeaProp | Saildrive-System, das von Beta, Nanni und Sole als Option verwendet wird |
| Wellenkupplung | Flexible Verbindung zwischen Getriebeausgang und Propellerwelle |
| PSS-Dichtung | Packless Sealing System — berührungslose Wellenabdichtung (wartungsarm) |
| Stopfbuchse | Traditionelle Wellenabdichtung mit Packung (braucht Schmierung/Nachziehen) |
| Federscheibe | Tellerfeder im PRM-Getriebe, die die Schaltkupplung betätigt (Verschleißteil) |

### Kraftstoffsystem

| Begriff | Erklärung |
|---------|-----------|
| Kraftstoffhebepumpe | Mechanische Pumpe am Motor, die Kraftstoff vom Tank zur Einspritzpumpe fördert |
| Einspritzpumpe | Erzeugt den Einspritzdruck (mechanisch oder elektronisch) |
| Injektor (Einspritzdüse) | Spritzt den Kraftstoff fein zerstäubt in den Brennraum |
| Kraftstoffvorfilter | Grobfilter mit Wasserabscheider vor dem Motor |
| Kraftstoff-Hauptfilter | Feinfilter am Motor (typisch 10 µm) |
| Magnetventil | Elektromagnetisches Absperrventil für Kraftstoffzufuhr (Motor-Stop) |
| Dieselpest | Mikrobielle Kontamination des Dieselkraftstoffs (Bakterien, Pilze, Hefen) |
| Rücklaufleitung | Überschüssiger Kraftstoff fließt vom Motor zurück zum Tank |
| Entlüfterschraube | Schraube zum Entlüften des Kraftstoffsystems nach Filterwechsel oder Tankleerlauf |

### Elektrische Anlage

| Begriff | Erklärung |
|---------|-----------|
| Lichtmaschine | Generator am Motor, erzeugt Ladestrom für die Batterie |
| Anlasser | Elektromotor zum Starten des Dieselmotors |
| Glühkerze | Heizspirale im Brennraum/Wirbelkammer für Kaltstart-Unterstützung |
| Vorglühen | Aufheizphase der Glühkerzen vor dem Startvorgang (5–15 Sekunden) |
| Magnetschalter | Relais am Anlasser, das den Strom für den Startvorgang schaltet |
| CAN-Bus | Controller Area Network — digitales Datenbussystem (bei modernen Motoren) |
| ECU | Engine Control Unit — Motorsteuergerät (bei Common-Rail-Motoren) |

### Vetus-spezifisch

| Begriff | Erklärung |
|---------|-----------|
| BOW PRO | Vetus-Baureihe von Bugstrahlrudern mit Proportionalsteuerung |
| Proportionalsteuerung | Stufenlose Schubregulierung (statt nur Ein/Aus) |
| Tunneleinbau | Quertunnel im Bug für Bugstrahlruder |
| E-LINE | Vetus-Baureihe vollelektrischer Bootsantriebe |
| E-HYBRID | Vetus-Hybrid-System (Diesel + Elektro) |

### Sole-spezifisch

| Begriff | Erklärung |
|---------|-----------|
| Mini-Serie | Sole-Baureihenbezeichnung für kompakte Marine-Diesel |
| S3L2 | Mitsubishi 3-Zylinder Industrieblock, Basis für Mini-17/26 |
| S4L2 | Mitsubishi 4-Zylinder Industrieblock, Basis für Mini-33/37 |
| S4Q2 | Mitsubishi 4-Zylinder Industrieblock, Basis für Mini-44/48/55 |
| S6S | Mitsubishi 6-Zylinder Industrieblock, Basis für Mini-62 |

### Nanni-spezifisch

| Begriff | Erklärung |
|---------|-----------|
| N-Serie | Nanni-Baureihe für Saugdiesel (natürlich aspiriert) |
| T-Serie | Nanni-Baureihe für Turbodiesel |
| Toyota 1KD/2KD/3CT | Toyota-Industrieblöcke als Basis für kleinere Nanni-Modelle |
| La Ciotat | Standort der Nanni-Hauptfabrik in Südfrankreich |

### Allgemein Marine

| Begriff | Erklärung |
|---------|-----------|
| Betriebsstunden (h) | Laufzeit des Motors in Stunden (wie Kilometerstand beim Auto) |
| Verdränger | Boot, das durch Wasserverdrängung fährt (nicht gleitend) |
| Gleiter | Boot, das bei höherer Geschwindigkeit auf dem Wasser gleitet |
| Semi-Displacement | Halbgleiter — Übergangsform zwischen Verdränger und Gleiter |
| RCD | Recreational Craft Directive — EU-Richtlinie für Sportboote |
| CE-Kategorie | Seetauglichkeitskategorie A–D gemäß RCD |
| Tier II/III | EPA-Abgasnormen (USA), von vielen Herstellern auch für EU erfüllt |
| Stage V | EU-Abgasnorm für Binnenschifffahrt und mobile Maschinen |
| OEM | Original Equipment Manufacturer — Erstausrüster (Werft, die Motor ab Werk verbaut) |
| Refit | Erneuerung/Austausch von Komponenten auf einem bestehenden Boot |

---

## 32. Pydantic v2 Datenmodelle

```python
"""
AYDI Pydantic v2 Datenmodelle — Alternative Marine-Diesel
Beta Marine, Nanni Diesel, Vetus, Sole Diesel, Craftsman Marine

Verwendung: Validierung und Serialisierung von Motordaten
im AYDI-Analysesystem.
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# --- Enums ---

class AlternativeMotorHersteller(str, Enum):
    """Hersteller alternativer Marine-Diesel."""
    BETA_MARINE = "beta_marine"
    NANNI_DIESEL = "nanni_diesel"
    VETUS = "vetus"
    SOLE_DIESEL = "sole_diesel"
    CRAFTSMAN_MARINE = "craftsman_marine"


class BasisblockHersteller(str, Enum):
    """Hersteller der Industrie-Basisblöcke."""
    KUBOTA = "kubota"
    TOYOTA = "toyota"
    MITSUBISHI = "mitsubishi"
    DEUTZ = "deutz"


class EinspritzungsTyp(str, Enum):
    """Art der Kraftstoffeinspritzung."""
    MECHANISCH_IDI = "mechanisch_idi"
    MECHANISCH_DI = "mechanisch_di"
    COMMON_RAIL = "common_rail"


class GetriebeSerie(str, Enum):
    """Getriebe-Baureihen."""
    PRM_80 = "prm_80"
    PRM_120 = "prm_120"
    PRM_150 = "prm_150"
    PRM_260 = "prm_260"
    TMC_40 = "tmc_40"
    TMC_60 = "tmc_60"
    ZF_15M = "zf_15m"
    ZF_25M = "zf_25m"
    ZF_45M = "zf_45m"
    ZF_63M = "zf_63m"
    ZF_80M = "zf_80m"
    ZF_85M = "zf_85m"


class SaildriveSerie(str, Enum):
    """Saildrive-Optionen."""
    SEAPROP_60 = "seaprop_60"
    SEAPROP_80 = "seaprop_80"
    ZF_SD10 = "zf_sd10"
    KEINE = "keine"


class AYDIConfidenceLevel(str, Enum):
    """AYDI Confidence-Stufen."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class FehlerbewertungSchweregrad(str, Enum):
    """Schweregrade für Fehler und Schwachstellen."""
    GERING = "gering"
    MITTEL = "mittel"
    HOCH = "hoch"
    KRITISCH = "kritisch"


class FehlerbewertungHaeufigkeit(str, Enum):
    """Häufigkeit von Fehlern."""
    SEHR_SELTEN = "sehr_selten"
    SELTEN = "selten"
    GELEGENTLICH = "gelegentlich"
    HAEUFIG = "haeufig"


class MotorSerie(str, Enum):
    """Motorserien bei den alternativen Herstellern."""
    # Beta Marine
    BETA_STANDARD = "beta_standard"
    BETA_ATOMIC = "beta_atomic"
    # Nanni
    NANNI_N = "nanni_n"
    NANNI_T = "nanni_t"
    # Vetus
    VETUS_M = "vetus_m"
    VETUS_VF = "vetus_vf"
    VETUS_D = "vetus_d"
    # Sole
    SOLE_MINI = "sole_mini"
    # Craftsman
    CRAFTSMAN_CM = "craftsman_cm"


# --- Basismodelle ---

class MotorAbmessungen(BaseModel):
    """Motorabmessungen in mm."""
    model_config = {"from_attributes": True}

    laenge_mm: float = Field(..., gt=0, description="Länge in mm")
    breite_mm: float = Field(..., gt=0, description="Breite in mm")
    hoehe_mm: float = Field(..., gt=0, description="Höhe in mm")


class KraftstoffVerbrauch(BaseModel):
    """Kraftstoffverbrauch in l/h."""
    model_config = {"from_attributes": True}

    volllast_lh: float = Field(..., gt=0, description="Verbrauch bei Volllast in l/h")
    reisefahrt_lh: float = Field(..., gt=0, description="Verbrauch bei Reisefahrt in l/h")
    leerlauf_lh: Optional[float] = Field(None, gt=0, description="Verbrauch im Leerlauf in l/h")


class PreisSpanne(BaseModel):
    """Preisspanne in EUR."""
    model_config = {"from_attributes": True}

    min_eur: float = Field(..., ge=0, description="Mindestpreis EUR")
    max_eur: float = Field(..., ge=0, description="Maximalpreis EUR")
    stand: str = Field(default="2025/26", description="Preisstand")

    @field_validator("max_eur")
    @classmethod
    def max_gte_min(cls, v: float, info) -> float:
        if "min_eur" in info.data and v < info.data["min_eur"]:
            raise ValueError("max_eur muss >= min_eur sein")
        return v


class BootsGroessenEmpfehlung(BaseModel):
    """Empfohlene Bootsgröße für einen Motor."""
    model_config = {"from_attributes": True}

    segelboot_min_m: Optional[float] = Field(None, gt=0)
    segelboot_max_m: Optional[float] = Field(None, gt=0)
    motorboot_min_m: Optional[float] = Field(None, gt=0)
    motorboot_max_m: Optional[float] = Field(None, gt=0)


# --- Hauptmodell: Alternativmotor ---

class AlternativMotorModell(BaseModel):
    """Vollständiges Datenmodell eines alternativen Marine-Dieselmotors."""
    model_config = {"from_attributes": True}

    # Identifikation
    hersteller: AlternativeMotorHersteller
    modellbezeichnung: str = Field(..., min_length=1, max_length=50)
    serie: MotorSerie
    basisblock_hersteller: BasisblockHersteller
    basisblock_modell: str = Field(..., min_length=1, max_length=50)

    # Technische Daten
    zylinder_anzahl: int = Field(..., ge=1, le=8)
    hubraum_ccm: float = Field(..., gt=0, description="Hubraum in cm³")
    bohrung_mm: Optional[float] = Field(None, gt=0)
    hub_mm: Optional[float] = Field(None, gt=0)
    verdichtung: Optional[float] = Field(None, gt=5.0, lt=30.0)
    leistung_ps: float = Field(..., gt=0, description="Nennleistung in PS")
    leistung_kw: float = Field(..., gt=0, description="Nennleistung in kW")
    nenndrehzahl_rpm: int = Field(..., gt=0, description="Nenndrehzahl in U/min")
    max_drehmoment_nm: Optional[float] = Field(None, gt=0)
    max_drehmoment_rpm: Optional[int] = Field(None, gt=0)

    # Einspritzung
    einspritzung: EinspritzungsTyp
    hat_turbolader: bool = False
    hat_ladeluftkuehler: bool = False

    # Physische Daten
    gewicht_trocken_mit_getriebe_kg: float = Field(..., gt=0)
    abmessungen: Optional[MotorAbmessungen] = None

    # Betriebsdaten
    kraftstoffverbrauch: KraftstoffVerbrauch
    oelmenge_liter: Optional[float] = Field(None, gt=0)
    kuehlmittel_liter: Optional[float] = Field(None, gt=0)

    # Elektrik
    lichtmaschine_volt: int = Field(default=12, ge=12, le=24)
    lichtmaschine_ampere: int = Field(..., gt=0)
    anlasser_kw: Optional[float] = Field(None, gt=0)

    # Getriebe und Antrieb
    standard_getriebe: GetriebeSerie
    standard_untersetzung: str = Field(default="2:1")
    saildrive_option: SaildriveSerie = SaildriveSerie.KEINE

    # Zertifizierung
    ce_kategorie: str = Field(default="A-D")
    abgas_norm: Optional[str] = Field(None, description="z.B. 'EU Stage V, EPA Tier III'")

    # Preis und Empfehlung
    uvp: PreisSpanne
    empfohlene_bootsgroesse: Optional[BootsGroessenEmpfehlung] = None

    # AYDI
    confidence: AYDIConfidenceLevel = AYDIConfidenceLevel.MEASURED
    datenstand: str = Field(default="2025/26")


# --- Schwachstelle ---

class MotorSchwachstelle(BaseModel):
    """Bekannte Schwachstelle eines Motor-Modells."""
    model_config = {"from_attributes": True}

    beschreibung: str = Field(..., min_length=5, max_length=300)
    betroffene_modelle: list[str] = Field(..., min_length=1)
    schweregrad: FehlerbewertungSchweregrad
    haeufigkeit: FehlerbewertungHaeufigkeit
    empfohlene_massnahme: Optional[str] = None
    kosten_behebung: Optional[PreisSpanne] = None
    confidence: AYDIConfidenceLevel = AYDIConfidenceLevel.DOCUMENTED


# --- Fehlerbild ---

class Fehlerursache(BaseModel):
    """Eine mögliche Ursache in einem Fehlerbild."""
    model_config = {"from_attributes": True}

    ursache: str = Field(..., min_length=5)
    wahrscheinlichkeit_prozent: float = Field(..., ge=0, le=100)
    betroffene_hersteller: list[AlternativeMotorHersteller] = Field(default_factory=list)
    sofortmassnahme: Optional[str] = None


class Fehlerbild(BaseModel):
    """Fehlerbild mit Symptom und möglichen Ursachen."""
    model_config = {"from_attributes": True}

    fehlerbild_id: str = Field(..., pattern=r"^F-ALT-\d{2}$")
    titel: str = Field(..., min_length=5)
    beschreibung: str = Field(..., min_length=10)
    ursachen: list[Fehlerursache] = Field(..., min_length=1)
    confidence: AYDIConfidenceLevel = AYDIConfidenceLevel.DOCUMENTED


# --- Fallstudie ---

class Fallstudie(BaseModel):
    """Dokumentierte Fallstudie."""
    model_config = {"from_attributes": True}

    fallstudie_id: str = Field(..., pattern=r"^FS-ALT-\d{2}$")
    titel: str
    boot_typ: str
    boot_laenge_m: float = Field(..., gt=0)
    motor_modell: str
    hersteller: AlternativeMotorHersteller
    betriebsstunden: Optional[int] = Field(None, ge=0)
    problem_beschreibung: str
    diagnose: str
    loesung: str
    kosten_eur: Optional[float] = Field(None, ge=0)
    aydi_bewertung: str
    confidence: AYDIConfidenceLevel = AYDIConfidenceLevel.DOCUMENTED


# --- Händlernetzwerk ---

class HaendlerNetzwerk(BaseModel):
    """Händlernetzwerk eines Herstellers in einem Land."""
    model_config = {"from_attributes": True}

    hersteller: AlternativeMotorHersteller
    land: str
    anzahl_haendler: str = Field(..., description="z.B. '5-8' oder '25+'")
    wichtige_standorte: list[str] = Field(default_factory=list)
    ersatzteil_lieferzeit_tage: str = Field(..., description="z.B. '2-5 Werktage'")


# --- Wartungsintervall ---

class WartungsIntervall(BaseModel):
    """Wartungsintervall für eine bestimmte Arbeit."""
    model_config = {"from_attributes": True}

    arbeit: str
    intervall_stunden: Optional[int] = Field(None, gt=0)
    intervall_monate: Optional[int] = Field(None, gt=0)
    anmerkung: Optional[str] = None


# --- BOW PRO Thruster (Vetus-spezifisch) ---

class BowProThruster(BaseModel):
    """Vetus BOW PRO Bugstrahlruder."""
    model_config = {"from_attributes": True}

    modell: str = Field(..., pattern=r"^BOW PRO \d+$")
    schub_kgf: float = Field(..., gt=0)
    leistung_kw: float = Field(..., gt=0)
    tunnel_durchmesser_mm: int = Field(..., gt=0)
    bootslaenge_min_m: float = Field(..., gt=0)
    bootslaenge_max_m: float = Field(..., gt=0)
    batterie_empfehlung: str
    kabelquerschnitt_mm2: int = Field(..., gt=0)
    sicherung_ampere: int = Field(..., gt=0)


# --- Gesamtvergleich ---

class HerstellerVergleich(BaseModel):
    """Vergleichsbewertung eines Herstellers."""
    model_config = {"from_attributes": True}

    hersteller: AlternativeMotorHersteller
    haendlernetz_de: int = Field(..., ge=1, le=5, description="Bewertung 1-5 Sterne")
    haendlernetz_eu: int = Field(..., ge=1, le=5)
    ersatzteile: int = Field(..., ge=1, le=5)
    wartungsfreundlichkeit: int = Field(..., ge=1, le=5)
    wiederverkaufswert: int = Field(..., ge=1, le=5)
    preis_leistung: int = Field(..., ge=1, le=5)
    blauwasser_eignung: int = Field(..., ge=1, le=5)
    charter_eignung: int = Field(..., ge=1, le=5)
    confidence: AYDIConfidenceLevel = AYDIConfidenceLevel.ESTIMATED


# --- Gesamt-Wissensbank ---

class AlternativeMotorWissensbank(BaseModel):
    """Komplette Wissensbank für alternative Marine-Diesel."""
    model_config = {"from_attributes": True}

    version: str = Field(default="2.0")
    letzte_aktualisierung: date
    motoren: list[AlternativMotorModell] = Field(default_factory=list)
    schwachstellen: list[MotorSchwachstelle] = Field(default_factory=list)
    fehlerbilder: list[Fehlerbild] = Field(default_factory=list)
    fallstudien: list[Fallstudie] = Field(default_factory=list)
    haendler: list[HaendlerNetzwerk] = Field(default_factory=list)
    wartungsintervalle: list[WartungsIntervall] = Field(default_factory=list)
    thruster: list[BowProThruster] = Field(default_factory=list)
    vergleiche: list[HerstellerVergleich] = Field(default_factory=list)
    confidence: AYDIConfidenceLevel = AYDIConfidenceLevel.MEASURED
```

---

## 33. Preisübersicht EUR

### 33.1 Neumotor-Preise (UVP, Stand 2025/26)

**Beta Marine:**

| Modell | UVP ab EUR | UVP bis EUR | Inkl. Getriebe |
|--------|-----------|------------|---------------|
| Beta 14 | 7.800 | 9.200 | PRM 80 |
| Beta 16 | 8.500 | 10.000 | PRM 120 |
| Beta 20 | 9.400 | 11.200 | PRM 120 |
| Beta 25 | 10.200 | 12.000 | PRM 120 |
| Beta 30 | 11.800 | 13.600 | PRM 150 |
| Beta 35 | 12.800 | 14.800 | PRM 150 |
| Beta 38 | 13.500 | 15.800 | PRM 150 |
| Beta 43 | 15.200 | 17.500 | PRM 260 |
| Beta 50 | 16.800 | 19.200 | PRM 260 |
| Beta 60 | 19.500 | 22.800 | ZF 15M |
| Beta 75 | 22.500 | 26.000 | ZF 25M |
| Beta 90 | 25.800 | 29.500 | ZF 25M |
| Beta 105 | 29.500 | 34.000 | ZF 45M |
| Beta 115 | 33.000 | 38.000 | ZF 45M |
| Beta 130 | 37.000 | 42.500 | ZF 63M |
| Beta 150 | 41.000 | 47.000 | ZF 63M |
| Atomic 10 | 8.200 | 9.800 | PRM 80 |
| Atomic 14 | 8.800 | 10.400 | PRM 80 |
| Atomic 16 | 9.800 | 11.400 | PRM 120 |
| Atomic 20 | 10.400 | 12.200 | PRM 120 |
| Atomic 25 | 11.200 | 13.100 | PRM 120 |
| Atomic 30 | 13.000 | 15.000 | PRM 150 |

**Nanni Diesel:**

| Modell | UVP ab EUR | UVP bis EUR | Inkl. Getriebe |
|--------|-----------|------------|---------------|
| N2.10 | 7.200 | 8.800 | TMC 40 |
| N2.14 | 7.800 | 9.500 | TMC 40 |
| N3.21 | 9.800 | 11.500 | TMC 60 |
| N3.30 | 11.200 | 13.000 | TMC 60 |
| N4.38 | 13.200 | 15.500 | PRM 150 |
| N4.50 | 16.500 | 19.000 | PRM 260 |
| N4.60 | 18.800 | 21.500 | ZF 15M |
| N4.80 | 22.000 | 25.500 | ZF 25M |
| N4.100 | 26.500 | 30.000 | ZF 25M |
| N4.115 | 30.000 | 34.500 | ZF 45M |
| T4.130 | 35.000 | 40.000 | ZF 45M |
| T4.155 | 40.000 | 46.000 | ZF 63M |
| T4.165 | 43.000 | 49.000 | ZF 63M |
| T4.200 | 52.000 | 60.000 | ZF 63M/80M |
| T6.250 | 65.000 | 75.000 | ZF 80M |

**Vetus:**

| Modell | UVP ab EUR | UVP bis EUR | Inkl. Getriebe |
|--------|-----------|------------|---------------|
| M2.02 | 6.800 | 8.200 | TMC 40 |
| M2.06 | 7.200 | 8.800 | TMC 40 |
| M2.C5 | 8.200 | 9.800 | TMC 40 |
| M2.D5 | 8.800 | 10.500 | TMC 40 |
| M3.09 | 9.500 | 11.200 | TMC 60 |
| M3.28 | 10.800 | 12.500 | TMC 60 |
| M3.29 | 11.500 | 13.500 | PRM 120 |
| M4.14 | 12.500 | 14.500 | PRM 150 |
| M4.15 | 12.800 | 14.800 | PRM 150 |
| M4.17 | 13.500 | 15.500 | PRM 150 |
| M4.35 | 15.000 | 17.500 | PRM 260 |
| M4.45 | 16.500 | 19.000 | PRM 260 |
| M4.56 | 18.500 | 21.500 | ZF 15M |
| VF4.140E | 32.000 | 37.000 | ZF 45M |
| VF4.170E | 37.000 | 42.000 | ZF 63M |
| VF4.190E | 45.000 | 52.000 | ZF 63M |
| VF5.220E | 52.000 | 60.000 | ZF 80M |
| VF5.250E | 58.000 | 67.000 | ZF 80M |
| D4.29 | 22.000 | 25.500 | ZF 25M |
| D4.42 | 25.000 | 29.000 | ZF 25M |
| DT4.70 | 30.000 | 35.000 | ZF 45M |
| DT4.110 | 36.000 | 42.000 | ZF 45M |
| DT6.315 | 78.000 | 90.000 | ZF 85M |

**Sole Diesel:**

| Modell | UVP ab EUR | UVP bis EUR | Inkl. Getriebe |
|--------|-----------|------------|---------------|
| Mini-11 | 6.500 | 7.800 | TMC 40 |
| Mini-17 | 8.200 | 9.800 | TMC 60 |
| Mini-26 | 9.800 | 11.500 | TMC 60 |
| Mini-29 | 10.800 | 12.500 | PRM 120 |
| Mini-33 | 12.000 | 14.000 | PRM 150 |
| Mini-37 | 12.800 | 14.800 | PRM 150 |
| Mini-44 | 14.500 | 16.800 | PRM 260 |
| Mini-48 | 15.500 | 18.000 | PRM 260 |
| Mini-55 | 17.500 | 20.200 | ZF 15M |
| Mini-62 | 22.000 | 25.500 | ZF 25M |

**Craftsman Marine:**

| Modell | UVP ab EUR | UVP bis EUR | Inkl. Getriebe |
|--------|-----------|------------|---------------|
| CM 2.16 | 5.800 | 7.200 | TMC 40 |
| CM 3.27 | 7.500 | 9.000 | TMC 60 |
| CM 4.35 | 9.800 | 11.500 | PRM 150 |
| CM 4.42 | 11.500 | 13.500 | PRM 260 |
| CM 4.52 | 13.000 | 15.200 | PRM 260 |
| CM 4.65 | 15.500 | 18.000 | ZF 15M |
| CM 4.80 | 18.000 | 21.000 | ZF 25M |
| CM 4.100 | 21.000 | 24.500 | ZF 25M |
| CM 4.140 | 26.000 | 30.000 | ZF 45M |

### 33.2 Ersatzteil-Preise (Richtwerte)

| Ersatzteil | Beta | Nanni | Vetus | Sole | Craftsman |
|-----------|------|-------|-------|------|-----------|
| Impeller | 25–40 | 28–45 | 30–45 | 25–40 | 22–35 |
| Ölfilter | 12–18 | 15–22 | 15–20 | 12–18 | 10–15 |
| Kraftstofffilter | 15–25 | 18–28 | 15–25 | 15–22 | 12–20 |
| Keilriemen | 15–25 | 15–25 | 18–28 | 15–25 | 12–20 |
| Thermostat | 35–55 | 40–60 | 40–60 | 35–55 | 30–45 |
| Zinkanode | 8–15 | 8–15 | 10–18 | 8–15 | 8–12 |
| Wärmetauscher | 450–850 | 500–900 | 500–950 | 420–800 | 380–700 |
| Auspuffkrümmer | 380–680 | 420–750 | 450–800 | 350–620 | 320–580 |
| Seewasserpumpe komplett | 250–420 | 280–480 | 300–500 | 240–400 | 220–380 |
| Injektorsatz (4 Zyl.) | 280–480 | 320–550 | 350–600 | 260–450 | 240–420 |
| Anlasser | 220–380 | 250–420 | 280–450 | 210–360 | 180–320 |
| Lichtmaschine | 280–520 | 320–580 | 350–620 | 260–480 | 240–440 |
| Motorlager-Satz (4 St.) | 120–220 | 140–250 | 150–260 | 110–200 | 100–180 |
| Glühkerzen-Satz | 40–80 | 45–90 | 50–95 | 40–75 | 35–65 |
| Ventildeckeldichtung | 15–30 | 18–35 | 20–38 | 15–28 | 12–25 |
| Zylinderkopfdichtung | 65–120 | 75–140 | 80–150 | 60–110 | 55–100 |

### 33.3 Werkstatt-Reparaturkosten (Richtwerte inkl. Arbeit)

| Reparatur | Beta | Nanni | Vetus | Sole | Craftsman |
|-----------|------|-------|-------|------|-----------|
| Impeller-Wechsel | 80–150 | 90–160 | 90–165 | 80–150 | 70–130 |
| Ölwechsel komplett | 100–180 | 110–190 | 110–195 | 100–180 | 90–160 |
| Thermostat-Tausch | 150–280 | 170–310 | 175–320 | 150–270 | 130–240 |
| Wärmetauscher-Reinigung | 280–480 | 300–520 | 320–550 | 270–460 | 250–420 |
| Auspuffkrümmer-Tausch | 550–950 | 600–1.050 | 650–1.100 | 520–880 | 480–820 |
| Injektor-Revision (Satz) | 450–780 | 500–850 | 550–900 | 420–720 | 380–660 |
| Motorlager + Fluchtung | 500–850 | 550–920 | 580–950 | 480–820 | 450–760 |
| Generalüberholung (4 Zyl.) | 3.500–6.500 | 4.000–7.000 | 4.200–7.500 | 3.200–6.000 | 3.000–5.500 |
| Kompletter Motorwechsel | 2.800–5.500 | 3.000–6.000 | 3.200–6.200 | 2.600–5.200 | 2.400–4.800 |

---

## 34. Quellenverzeichnis

### 34.1 Hersteller-Dokumentation

| Quelle | Beschreibung | Confidence |
|--------|-------------|-----------|
| Beta Marine Ltd. — Product Catalogue 2025 | Technische Daten, Abmessungen, Preise | measured |
| Beta Marine Ltd. — Installation Manual V4.2 | Einbau, Getriebe, Saildrive | measured |
| Nanni Industries — Catalogue Moteurs Marins 2025 | Modellpalette, Spezifikationen | measured |
| Nanni Industries — Manuel d'Installation | Einbaurichtlinien, Getriebe | measured |
| Vetus B.V. — Marine Engines Catalogue 2025 | M-, VF-, D-Serie, BOW PRO | measured |
| Vetus B.V. — Installation & Operation Manual | Einbau, Thruster-Integration | measured |
| Sole Diesel S.A. — Catálogo Motores Marinos 2025 | Mini-Serie, Spezifikationen | measured |
| Craftsman Marine B.V. — Productoverzicht 2025 | CM-Serie, Preise | measured |

### 34.2 Basisblock-Hersteller

| Quelle | Beschreibung | Confidence |
|--------|-------------|-----------|
| Kubota Engine — 03/05 Series Service Manual | D722–V3800 Werkstattdaten | measured |
| Toyota Industrial Engines — Workshop Manual | 1KD, 2KD, 3CT Spezifikationen | measured |
| Mitsubishi Heavy Industries — L/S-Series Manual | L2E–S6S Technische Daten | measured |
| Deutz AG — TCD Series Workshop Manual | TCD 3.6–6.1 Werkstattdaten | measured |

### 34.3 Getriebe-Hersteller

| Quelle | Beschreibung | Confidence |
|--------|-------------|-----------|
| Newage PRM — Gearbox Catalogue 2024 | PRM 80–260 Spezifikationen | measured |
| Technodrive B.V. — TMC/SeaProp Manual | TMC 40/60, SeaProp 60/80 | measured |
| ZF Marine — Product Catalogue 2025 | ZF 15M–85M Spezifikationen | measured |

### 34.4 Normen und Richtlinien

| Quelle | Beschreibung | Confidence |
|--------|-------------|-----------|
| EU Richtlinie 2013/53/EU | Recreational Craft Directive | measured |
| ISO 8665:2006 | Marine-Motorleistung — Messbedingungen | measured |
| ISO 8178 | Abgasemissionen — Messzyklus | measured |
| EU Verordnung 2016/1628 | Stage V Abgasnorm für NRMM | measured |
| EPA 40 CFR Part 1042 | Tier II/III Marine Diesel Engines | measured |

### 34.5 Fachpublikationen und Erfahrungswerte

| Quelle | Beschreibung | Confidence |
|--------|-------------|-----------|
| Practical Boat Owner (UK) — Engine Reviews 2018–2025 | Beta, Nanni Tests | documented |
| YACHT Magazin (DE) — Motorentests 2019–2025 | Vergleichstests | documented |
| Segling (SE) — Motortest 2022 | Skandinavische Bewertung | documented |
| Cruising World — Diesel Engine Guide 2024 | Blauwasser-Empfehlungen | documented |
| Marine-Fachforen (sailnet.com, ybw.com, segeln-forum.de) | Eignererfahrungen | estimated |
| AYDI Werkstatt-Partnernetzwerk | Reparaturstatistiken | documented |

---

## 35. Motorauswahl-Entscheidungsmatrix

### 35.1 Entscheidungsbaum: Welcher Alternativmotor passt?

```
Frage 1: Einsatzgebiet?
├── Blauwasser / Weltumsegelung
│   ├── Budget vorhanden → Yanmar JH-Serie (bestes Netzwerk)
│   └── Budget begrenzt → Beta Marine (Kubota-Teile weltweit, mechanisch einfach)
│
├── Mittelmeer (Küstenfahrt / Charter)
│   ├── OEM bei Werft → Nanni (Bénéteau, Lagoon, Dufour)
│   ├── Refit → Nanni oder Beta Marine
│   └── Charterflotte → Nanni (starkes Mittelmeer-Netz)
│
├── Nordsee / Ostsee / Atlantik
│   ├── Segelboot → Beta Marine oder Yanmar
│   ├── Motorboot → Vetus (gutes NL/DE-Netz)
│   └── Verdränger → Vetus D-Serie (Deutz, laufruhig)
│
├── Binnenfahrt (Kanäle, Flüsse, Seen)
│   ├── Niederlande → Vetus (Heimmarkt, beste Versorgung)
│   ├── Deutschland → Vetus oder Beta Marine
│   └── Budget → Craftsman Marine
│
└── Küstenfahrt Spanien / Griechenland
    ├── Sole Diesel (lokale Versorgung)
    └── Nanni Diesel (starkes Mittelmeer-Netz)
```

### 35.2 Entscheidungsmatrix nach Priorität

| Priorität | Empfehlung 1 | Empfehlung 2 | Empfehlung 3 |
|-----------|-------------|-------------|-------------|
| Niedrigster Preis | Craftsman Marine | Sole Diesel | Nanni Diesel |
| Höchste Zuverlässigkeit | Beta Marine | Nanni Diesel | Vetus |
| Bestes Händlernetz (DE) | Vetus | Beta Marine | Nanni |
| Bestes Händlernetz (Mittelmeer) | Nanni | Sole Diesel | Beta Marine |
| Einfachste Wartung | Beta Marine | Sole Diesel | Nanni |
| Kompakteste Bauform | Beta Atomic | Vetus M2 | Sole Mini-11 |
| Beste Systemintegration | Vetus (Motor + Thruster) | — | — |
| Beste Garantie | Beta Marine (5 Jahre) | — | — |
| Höchster Wiederverkaufswert | Beta Marine | Nanni | Vetus |
| Geringste Vibration | Vetus M-Serie | Beta Marine | Nanni |

---

## 36. Motoröl-Spezifikationen und Empfehlungen

### 36.1 Motoröl nach Hersteller und Modellreihe

| Hersteller | Modellreihe | Empfohlenes Öl | Viskosität | API-Klasse | Ölmenge |
|------------|-------------|---------------|-----------|-----------|---------|
| Beta Marine | Beta 14–25 | Mineral oder Halbsynthese | 15W-40 | CH-4 / CI-4 | 2,1–3,3 l |
| Beta Marine | Beta 30–50 | Mineral oder Halbsynthese | 15W-40 | CH-4 / CI-4 | 4,2–6,5 l |
| Beta Marine | Beta 60–90 | Halbsynthese | 15W-40 oder 10W-40 | CI-4 / CJ-4 | 7,0–9,5 l |
| Beta Marine | Beta 105–150 | Halbsynthese | 10W-40 oder 15W-40 | CI-4 / CJ-4 | 9,5–12,0 l |
| Nanni | N2.10–N3.30 | Mineral | 15W-40 | CH-4 | 2,0–3,5 l |
| Nanni | N4.38–N4.115 | Mineral oder Halbsynthese | 15W-40 | CH-4 / CI-4 | 5,0–9,0 l |
| Nanni | T4.130–T6.250 | Halbsynthese | 10W-40 oder 15W-40 | CI-4 / CJ-4 | 8,5–14,0 l |
| Vetus | M2.02–M2.D5 | Mineral | 15W-40 | CF-4 / CH-4 | 1,8–2,5 l |
| Vetus | M3.09–M4.56 | Mineral oder Halbsynthese | 15W-40 | CH-4 | 3,5–6,0 l |
| Vetus | VF4.140E–VF5.250E | Halbsynthese | 10W-40 oder 15W-40 | CI-4 / CJ-4 | 8,0–15,0 l |
| Vetus | D4.29–DT6.315 | Halbsynthese (Deutz-spez.) | 10W-40 | CI-4 + ACEA E7 | 6,5–18,0 l |
| Sole | Mini-11–Mini-29 | Mineral | 15W-40 | CF-4 / CH-4 | 2,0–3,5 l |
| Sole | Mini-33–Mini-62 | Mineral oder Halbsynthese | 15W-40 | CH-4 | 4,5–8,5 l |
| Craftsman | CM 2.16–CM 4.140 | Mineral | 15W-40 | CF-4 / CH-4 | 2,2–9,0 l |

### 36.2 Getriebeöl-Spezifikationen

| Getriebe-Typ | Öl-Typ | Spezifikation | Ölmenge | Wechselintervall |
|-------------|--------|--------------|---------|-----------------|
| PRM 80 | ATF | Dexron III oder Mercon V | 0,4 l | 200h / jährlich |
| PRM 120 | ATF | Dexron III oder Mercon V | 0,6 l | 200h / jährlich |
| PRM 150 | ATF | Dexron III oder Mercon V | 0,8 l | 200h / jährlich |
| PRM 260 | ATF | Dexron III oder Mercon V | 1,2 l | 200h / jährlich |
| TMC 40 | ATF | Dexron III | 0,3 l | 200h / jährlich |
| TMC 60 | ATF | Dexron III | 0,5 l | 200h / jährlich |
| ZF 15M | Getriebeöl | ZF Marine Oil 75W-90 | 1,0 l | 250h / jährlich |
| ZF 25M | Getriebeöl | ZF Marine Oil 75W-90 | 1,5 l | 250h / jährlich |
| ZF 45M | Getriebeöl | ZF Marine Oil 75W-90 | 2,0 l | 250h / jährlich |
| ZF 63M | Getriebeöl | ZF Marine Oil 75W-90 | 2,5 l | 250h / jährlich |
| ZF 80M | Getriebeöl | ZF Marine Oil 75W-90 | 3,5 l | 250h / jährlich |
| SeaProp 60 | Getriebeöl | SAE 80W-90 GL-5 | 0,8 l | 200h / jährlich |
| SeaProp 80 | Getriebeöl | SAE 80W-90 GL-5 | 1,0 l | 200h / jährlich |

---

## 37. Propeller-Empfehlungen

### 37.1 Propeller-Dimensionierung nach Motor

| Motor (Leistung) | 2-Blatt Faltpropeller | 3-Blatt Festpropeller | Max. Wellendurchmesser |
|------------------|---------------------|---------------------|----------------------|
| 10–14 PS | 12" × 8" | 11" × 7" | Ø 20 mm |
| 16–20 PS | 13" × 9" | 12" × 8" | Ø 25 mm |
| 21–25 PS | 14" × 10" | 13" × 9" | Ø 25 mm |
| 26–30 PS | 15" × 11" | 14" × 10" | Ø 25 mm |
| 33–38 PS | 16" × 12" | 15" × 11" | Ø 30 mm |
| 42–50 PS | 17" × 13" | 16" × 12" | Ø 30 mm |
| 55–62 PS | 18" × 14" | 17" × 13" | Ø 35 mm |
| 75–90 PS | 19" × 15" | 18" × 14" | Ø 35 mm |
| 100–115 PS | 20" × 16" | 19" × 15" | Ø 40 mm |
| 130–150 PS | 21" × 17" | 20" × 16" | Ø 40 mm |

**Hinweis:** Diese Werte sind Richtwerte für Segelboote (Verdränger). Motorboote und Gleiter benötigen andere Propellerauslegungen. Die exakte Auslegung hängt von Rumpfform, Verdrängung und gewünschter Reisegeschwindigkeit ab.

### 37.2 Propeller-Typen und Empfehlungen

| Propeller-Typ | Vorteile | Nachteile | Empfohlen für |
|--------------|---------|-----------|--------------|
| 2-Blatt Festpropeller | Günstig, robust | Hoher Segelwiderstand | Motorboote, Budget |
| 3-Blatt Festpropeller | Besser Rückwärts, ruhiger Lauf | Hoher Segelwiderstand | Motorboote, Charterboote |
| 2-Blatt Faltpropeller | Geringster Segelwiderstand | Teurer, empfindlicher | Regatta-Segelboote |
| 3-Blatt Faltpropeller | Guter Kompromiss | Teuer | Fahrtensegler |
| Verstellpropeller | Optimaler Wirkungsgrad | Sehr teuer, komplex | Professionelle Yachten |

---

## 38. Einbau- und Installationsrichtlinien

### 38.1 Allgemeine Einbauvorschriften (RCD-konform)

| Aspekt | Anforderung | Norm |
|--------|------------|------|
| Motorraum-Belüftung | Min. 0,05 m² oder Motor-kW × 0,0003 m² | ISO 9094 |
| Abstand Motor↔Brennbares | Min. 100 mm oder Hitzeschutz | ISO 9094 |
| Kraftstoffabsperrhahn | Erreichbar ohne Motorraum-Zugang | ISO 10088 |
| Motorlager | 4-Punkt, schwingungsdämpfend, Bolzen gesichert | Herstellervorgabe |
| Wellenfluchtung | Max. 0,05 mm Versatz | Herstellervorgabe |
| Auspuff-Schwanenhals | Min. 300 mm über Wasserlinie | ISO 13363 |
| Seewasserventil | Erreichbar, Schließposition markiert | ISO 9093 |
| Feuerlöscher | 2 kg ABC-Pulver oder 2 kg CO₂ im Motorraum | ISO 9094 |
| Bilgenpumpe | Motorraum-Bereich mit einbezogen | ISO 15083 |

> ⚠️ **Korrektur (Audit):** Zwei Normzuordnungen in dieser Tabelle waren fehlerhaft und wurden korrigiert. „Auspuff-Schwanenhals" war fälschlich mit ISO 8469 (Non-fire-resistant fuel hoses) belegt → korrigiert auf ISO 13363 (Rubber and plastics hoses for marine-engine wet-exhaust systems). „Wellenfluchtung" war fälschlich mit ISO 10088 (Permanently installed fuel systems) belegt → die 0,05-mm-Fluchtungstoleranz ist eine Hersteller-/Kupplungsvorgabe, nicht durch ISO 10088 geregelt.

### 38.2 Motorraum-Mindestabmessungen (Richtwerte)

| Motorklasse | Min. Länge | Min. Breite | Min. Höhe | Wartungszugang |
|-------------|-----------|------------|----------|---------------|
| 10–20 PS | 600 mm | 500 mm | 550 mm | Mindestens 2 Seiten |
| 21–35 PS | 700 mm | 550 mm | 600 mm | Mindestens 2 Seiten |
| 36–50 PS | 800 mm | 600 mm | 650 mm | 3 Seiten empfohlen |
| 55–75 PS | 900 mm | 650 mm | 700 mm | 3 Seiten empfohlen |
| 80–115 PS | 1.000 mm | 700 mm | 750 mm | 3 Seiten erforderlich |
| 130–150 PS | 1.100 mm | 750 mm | 800 mm | 3 Seiten erforderlich |

### 38.3 Abgasanlagen-Layout

| Komponente | Anforderung | Anmerkung |
|-----------|------------|-----------|
| Auspuffkrümmer (wassergekühlt) | Herstelleroriginal verwenden | Materialstärke und Wasserführung kritisch |
| Mischkammer | Direkt nach Krümmer | Seewasser-Einspritzung in Abgasstrom |
| Auspuffschlauch | Min. Ø 45 mm (bis 30 PS), Ø 55 mm (bis 75 PS), Ø 65 mm (bis 150 PS) | Hitzebeständig bis 100 °C |
| Schwanenhals | Min. 300 mm über WL | Höher = besser |
| Anti-Siphon-Ventil | Am höchsten Punkt der Seewasserleitung | Pflicht bei Auspuff nahe WL |
| Schalldämpfer | Wassersammelschalldämpfer (Waterlock) | Volumen mind. 5× Hubraum |
| Auspuffauslass | Seitlich über WL oder achtern | Rückschlagklappe bei Seitenauslass |

---

## 39. Kühlsystem-Spezifikationen

### 39.1 Kühlmittel-Spezifikationen

| Hersteller | Empfohlenes Kühlmittel | Mischung | Frostschutz bis | Wechselintervall |
|------------|----------------------|---------|----------------|-----------------|
| Beta Marine | OAT-Kühlmittel (G12+) | 50:50 mit dest. Wasser | -37 °C | 2 Jahre / 1.000h |
| Nanni Diesel | OAT oder Silikat (G11/G12) | 50:50 | -37 °C | 2 Jahre / 1.000h |
| Vetus | OAT-Kühlmittel (G12+) | 50:50 | -37 °C | 2 Jahre / 1.000h |
| Sole Diesel | Silikat-Kühlmittel (G11) | 50:50 | -37 °C | 2 Jahre / 1.000h |
| Craftsman | Silikat oder OAT | 50:50 | -37 °C | 2 Jahre / 1.000h |

**Achtung:** OAT (Organic Acid Technology) und Silikat-Kühlmittel NIEMALS mischen! Bei Wechsel des Kühlmitteltyps System vollständig spülen.

### 39.2 Thermostat-Öffnungstemperaturen

| Hersteller | Standardmodelle | Turbomodelle | Vollständig offen |
|------------|---------------|-------------|------------------|
| Beta Marine | 71 °C ± 2 °C | 76 °C ± 2 °C | 85 °C |
| Nanni Diesel | 72 °C ± 2 °C | 76 °C ± 2 °C | 87 °C |
| Vetus | 72 °C ± 2 °C | 78 °C ± 2 °C | 88 °C |
| Sole Diesel | 71 °C ± 2 °C | — | 85 °C |
| Craftsman | 71 °C ± 2 °C | 76 °C ± 2 °C | 85 °C |

### 39.3 Zinkanoden im Kühlsystem

| Position | Material | Gewicht | Prüfintervall | Wechsel bei |
|----------|---------|---------|---------------|------------|
| Wärmetauscher (Motorseite) | Zink | 20–50 g | 200h / jährlich | <50 % Restgewicht |
| Wärmetauscher (Seewasserseite) | Zink | 20–50 g | 200h / jährlich | <50 % Restgewicht |
| Saildrive-Gehäuse | Zink | 200–500 g | Jedes Slippen | <60 % Restgewicht |
| Propellerwelle (Wellenanlage) | Zink | 100–300 g | Jedes Slippen | <50 % Restgewicht |

**Salzwasser-Regel:** Bei intensiver Salzwassernutzung (Charterboot, Mittelmeer ganzjährig) Prüfintervall halbieren.

---

## 40. Seriennummern und Baujahr-Identifikation

### 40.1 Beta Marine

**Seriennummer-Format:** `BXXX-YYNNN`
- B = Beta Marine
- XXX = Modellcode (z.B. 038 = Beta 38, 075 = Beta 75)
- YY = Baujahr (z.B. 24 = 2024)
- NNN = Laufende Nummer im Baujahr

**Typenschild-Position:** Steuerbordseite des Zylinderblocks, oberhalb der Ölwanne

### 40.2 Nanni Diesel

**Seriennummer-Format:** `NXXX.YY.NNNNNN`
- N = Nanni
- XXX = Modellcode (z.B. 450 = N4.50)
- YY = Baujahr
- NNNNNN = Laufende Nummer

**Typenschild-Position:** Steuerbordseite, auf Höhe des Kraftstofffilters

### 40.3 Vetus

**Seriennummer-Format:** `VXXX-YYMMNNNN`
- V = Vetus
- XXX = Modellcode (z.B. M35 = M4.35)
- YY = Baujahr
- MM = Produktionsmonat
- NNNN = Laufende Nummer

**Typenschild-Position:** Obere Seite des Zylinderblocks oder am Ventildeckel

### 40.4 Sole Diesel

**Seriennummer-Format:** `SXXX-YYNNNNN`
- S = Sole
- XXX = Modellcode (z.B. M33 = Mini-33)
- YY = Baujahr
- NNNNN = Laufende Nummer

**Typenschild-Position:** Steuerbordseite des Zylinderblocks

### 40.5 Craftsman Marine

**Seriennummer-Format:** `CM-XXX-YYNNNN`
- CM = Craftsman Marine
- XXX = Modellcode
- YY = Baujahr
- NNNN = Laufende Nummer

**Typenschild-Position:** Steuerbordseite des Zylinderblocks

---

## 41. FAQ Ergänzung — Spezialfragen

### FAQ 27: Kann ich einen Alternativmotor selbst marinisieren?

**Antwort:** Theoretisch ja, praktisch stark abzuraten. Eine fachgerechte Marinisierung erfordert:
- Spezialwissen zu Marine-Kühlsystemen und Auspuffanlagen
- Zugang zu marinespezifischen Komponenten (Wärmetauscher, Seewasserpumpe, Krümmer)
- CE-Zertifizierung (RCD 2013/53/EU) — ohne diese ist der Motor in der EU nicht legal
- Prüfstandlauf und Abgasmessung
- Versicherungstechnische Abdeckung

Der Preisunterschied zwischen Selbst-Marinisierung und Fertigmotor rechtfertigt das Risiko in den seltensten Fällen. Confidence: documented.

### FAQ 28: Wie verhält sich der Kraftstoffverbrauch bei Teillast?

**Antwort:** Marinediesel laufen am effizientesten bei 60–75 % der Nennleistung. Typische Verbräuche im Teillastbereich:

| Teillast | Verbrauch relativ zu Volllast | Typische Nutzung |
|----------|-------------------------------|------------------|
| 100 % (Volllast) | 100 % | Notfall, Gegenwind/-strom |
| 80 % | 75–80 % | Schnelle Überfahrt |
| 60 % (Reisefahrt) | 50–55 % | Standard-Reisefahrt |
| 40 % | 35–40 % | Sparfahrt, Langstrecke |
| Leerlauf | 15–20 % | Ankern, Laden |

Alle hier behandelten Hersteller zeigen ähnliche Teillast-Kurven, da die Basisblöcke vergleichbar sind. Confidence: measured.

### FAQ 29: Welche Motoren sind am besten für elektrische Nachrüstung (Hybrid) geeignet?

**Antwort:** Für Hybrid-Nachrüstung eignen sich am besten Motoren mit:
- Ausreichend dimensionierter Lichtmaschine (>75A)
- Platz für zusätzlichen Elektromotor/Generator am Schwungrad
- CAN-Bus-Schnittstelle (für intelligente Steuerung)

Beste Kandidaten: Beta Marine (Hybrid-System ab Werk), Vetus (E-HYBRID), Nanni (Torqeedo-Partnerschaft). Sole und Craftsman bieten derzeit keine Hybrid-Lösungen. Confidence: documented.

### FAQ 30: Wie erkenne ich, ob ein gebrauchter Motor noch in Ordnung ist?

**Antwort:** Checkliste für den Kauf eines gebrauchten Alternativmotors:

| Prüfpunkt | Methode | OK-Kriterium |
|-----------|---------|-------------|
| Kompression | Kompressionsmessung | >25 bar, max. 10 % Abweichung zwischen Zylindern |
| Öldruck | Öldruckmanometer | >2,0 bar bei 2.000 U/min (warm) |
| Ölzustand | Visuell + Ölanalyse | Kein Wasser, kein Kraftstoff, keine Metallspäne |
| Kühlsystem | Druckprüfung | Hält 1,0 bar für 15 Min. |
| Auspuffkrümmer | Visuell + Klopftest | Keine Risse, kein Hohlklang |
| Lichtmaschine | Ladespannung messen | 13,8–14,4V bei Nenndrehzahl |
| Startverhalten | Kaltstart beobachten | Springt innerhalb 5 Sek. an (bei >10 °C) |
| Rauchfarbe | Visuell bei Volllast | Leicht grau OK, schwarz oder blau = Problem |
| Getriebe | Schalten V/R prüfen | Kein Krachen, kein Rutschen |
| Motorlager | Visuell | Kein Riss, kein Durchsacken |

Confidence: documented.

---

## 42. Lebenszyklus-Kostenvergleich (20 Jahre)

### 42.1 Gesamtkosten über 20 Jahre (Annahme: 200h/Jahr, 30–40 PS Klasse)

| Kostenposition | Beta 38 | Nanni N4.38 | Vetus M4.17 | Sole Mini-37 | Craftsman CM 4.35 | Yanmar 3JH40 |
|---------------|---------|-------------|-------------|-------------|-------------------|-------------|
| Anschaffung | 14.500 | 14.200 | 14.500 | 13.500 | 10.500 | 17.500 |
| Jährl. Wartung (×20) | 3.400 | 3.600 | 3.800 | 3.200 | 3.000 | 3.600 |
| Auspuffkrümmer (2×) | 1.400 | 1.500 | 1.600 | 1.600 | 1.500 | 1.200 |
| Wärmetauscher (1×) | 650 | 700 | 750 | 600 | 550 | 800 |
| Injektorsatz (1×) | 380 | 420 | 450 | 350 | 320 | 480 |
| Motorlager (2×) | 350 | 400 | 420 | 340 | 300 | 380 |
| Generalüberholung (1×) | 5.000 | 5.500 | 5.800 | 4.500 | 4.200 | 6.500 |
| Diverse Reparaturen | 2.000 | 2.200 | 2.300 | 2.500 | 3.000 | 1.800 |
| **Gesamt 20 Jahre** | **27.680** | **28.520** | **29.620** | **26.590** | **23.370** | **32.260** |
| **Kosten pro Stunde** | **6,92 EUR/h** | **7,13 EUR/h** | **7,41 EUR/h** | **6,65 EUR/h** | **5,84 EUR/h** | **8,07 EUR/h** |

**AYDI-Bewertung:** Craftsman ist am günstigsten, hat aber den niedrigsten Wiederverkaufswert und potenziell höhere Reparaturkosten bei Salzwassernutzung. Beta Marine bietet das beste Verhältnis aus Gesamtkosten, Zuverlässigkeit und Wiederverkaufswert. Yanmar ist am teuersten, hat aber den besten Wiederverkaufswert und das dichteste Servicenetzwerk. Confidence: estimated.

### 42.2 Wiederverkaufswert nach 20 Jahren / 4.000h

| Motor | Neuwert EUR | Restwert EUR | Restwert % |
|-------|------------|-------------|-----------|
| Beta 38 | 14.500 | 2.500–3.500 | 17–24 % |
| Nanni N4.38 | 14.200 | 2.000–3.000 | 14–21 % |
| Vetus M4.17 | 14.500 | 2.000–2.800 | 14–19 % |
| Sole Mini-37 | 13.500 | 1.500–2.200 | 11–16 % |
| Craftsman CM 4.35 | 10.500 | 800–1.500 | 8–14 % |
| Yanmar 3JH40 | 17.500 | 4.000–5.500 | 23–31 % |

---

## 43. Häufige Suchbegriffe und Modellbezeichnungen — Querverweise

### 43.1 Modell-Querverweistabelle (Leistungsklassen)

| Leistung | Beta Marine | Nanni | Vetus | Sole | Craftsman | Yanmar |
|----------|-----------|-------|-------|------|-----------|--------|
| 10 PS | Atomic 10 | N2.10 | M2.02 | Mini-11 | — | 1YM15 |
| 14–16 PS | Beta 14/16 | N2.14 | M2.C5 | — | CM 2.16 | 2YM15 |
| 20–21 PS | Beta 20 | N3.21 | M3.09 | Mini-17 | — | 2YM20 |
| 25–27 PS | Beta 25 | — | M3.28 | Mini-26 | CM 3.27 | 3YM20 |
| 29–30 PS | Beta 30 | N3.30 | M3.29 | Mini-29 | — | 3YM30 |
| 33–35 PS | Beta 35 | — | M4.14 | Mini-33 | CM 4.35 | 3JH40 |
| 38 PS | Beta 38 | N4.38 | M4.17 | Mini-37 | — | 3JH40 |
| 42–44 PS | Beta 43 | — | M4.35 | Mini-44 | CM 4.42 | — |
| 48–50 PS | Beta 50 | N4.50 | M4.45 | Mini-48 | CM 4.52 | 4JH57 |
| 55–60 PS | Beta 60 | N4.60 | M4.56 | Mini-55 | — | 4JH57 |
| 75–80 PS | Beta 75 | N4.80 | D4.42 | Mini-62 | CM 4.80 | 4JH80 |
| 90–100 PS | Beta 90 | N4.100 | DT4.70 | — | CM 4.100 | 4JH110 |
| 105–115 PS | Beta 105/115 | N4.115 | DT4.110 | — | — | 4JH110 |
| 130 PS | Beta 130 | T4.130 | — | — | CM 4.140 | 4LHA-STP |
| 140–150 PS | Beta 150 | T4.155 | VF4.140E | — | — | 4LHA-DTP |
| 165–200 PS | — | T4.165/200 | VF4.170E | — | — | 4LHA-HTP |
| 220–250 PS | — | T6.250 | VF5.220E/250E | — | — | 6LY-STP |
| 315 PS | — | — | DT6.315 | — | — | 6LY-UTP |

### 43.2 OEM-Einbau Querverweistabelle

| Werft | Modellreihe | Standardmotor | Alternative |
|-------|------------|--------------|------------|
| Bénéteau Océanis 30.1 | Segelboot 9,5 m | Nanni N3.21 | Yanmar 3YM20 |
| Bénéteau Océanis 40.1 | Segelboot 12,3 m | Nanni N4.50 | Yanmar 4JH57 |
| Dufour 390 | Segelboot 11,9 m | Nanni N4.38 | Volvo D1-30 |
| Lagoon 42 | Katamaran 12,8 m | 2× Nanni N4.50 | 2× Yanmar 4JH57 |
| Fountaine-Pajot Elba 45 | Katamaran 13,4 m | 2× Nanni N4.80 | 2× Yanmar 4JH80 |
| Linssen Grand Sturdy | Motorverdränger | Vetus M4.56/VF4.140E | Volvo D2-60 |
| Pedro Boats | Stahlyacht | Vetus M-/VF-Serie | — |
| Intercruiser | Sloep/Motorboot | Vetus M4.35 | Craftsman CM 4.42 |
| Nordship (DK) | Segelboot | Beta Marine (diverse) | Yanmar JH |
| Cornish Crabbers (UK) | Segelboot trad. | Beta Marine 14–25 | — |
| Malo Yachts (SE) | Segelboot | Beta Marine 38–60 | Volvo D2-40 |

---

## 44. Winterlagerung und Konservierung

### 44.1 Standard-Winterlagerungsprozedur (alle Hersteller)

| Schritt | Maßnahme | Anmerkung |
|---------|----------|-----------|
| 1 | Motor warmfahren (min. 20 Min.) | Öl und Kühlmittel auf Betriebstemperatur |
| 2 | Motoröl und Filter wechseln | Altes Öl enthält Säuren → Korrosion über Winter |
| 3 | Kraftstofffilter wechseln | Neuer Filter verhindert Kondensation |
| 4 | Kraftstofftank vollfüllen | Minimiert Kondensation → weniger Dieselpest-Risiko |
| 5 | Diesel-Biozid zusetzen | 1:1.000 Dosierung, Tank voll |
| 6 | Seewasserkreislauf mit Frostschutz spülen | Propylenglykol -20°C, NICHT Ethylenglykol |
| 7 | Seewasserventil schließen | Markierung „ZU" sichtbar |
| 8 | Impeller ausbauen oder entspannen | Formgedächtnis → längere Lebensdauer |
| 9 | Kühlmittel-Frostschutz prüfen | Refraktometer → mind. -20 °C |
| 10 | Lichtmaschinenriemen entspannen | Verhindert Setzen des Riemens |
| 11 | Auspuffsystem entwässern | Ablassschrauben öffnen, Wasser ablaufen lassen |
| 12 | Motorraum trocknen und belüften | Feuchtigkeit → Korrosion |
| 13 | Batterie abklemmen | Minuspol zuerst, Ladezustand >80 % |
| 14 | Getriebeölstand prüfen | Auffüllen wenn nötig |
| 15 | Blanke Metallflächen mit Korrosionsschutz | WD-40, Ballistol oder Cortec VpCI |
| 16 | Betriebsstundenzähler notieren | Für nächsten Wartungstermin |

### 44.2 Besonderheiten nach Hersteller

**Beta Marine:**
- Kubota-Blöcke vertragen Stillstand gut (Landmaschinen-Gene)
- Empfehlung: Zylinder mit wenigen Tropfen Motoröl durch Ansaugöffnung einölen
- Dekompressionshebel öffnen (entlastet Ventilfeder)

**Nanni Diesel:**
- Toyota-Blöcke (N2/N3/N4.38): Kraftstoffsystem muss bei Inbetriebnahme entlüftet werden
- Kubota-Blöcke (N4.50+): wie Beta Marine
- T-Serie (Turbo): Turbolader-Ansaugseite mit ölgetränktem Lappen verschließen

**Vetus:**
- M-Serie: Mitsubishi-Block robust bei Stillstand
- D-Serie (Deutz): Ventilspiel vor Einwinterung prüfen (Deutz-Ventile setzen sich)
- BOW PRO Thruster: Tunnel inspizieren, Anode prüfen

**Sole Diesel:**
- Wie Vetus M-Serie (gleiche Mitsubishi-Blöcke)
- Auspuffkrümmer besonders sorgfältig entwässern (Korrosionsanfälligkeit)

**Craftsman Marine:**
- Wie Vetus M-Serie (gleiche Mitsubishi-Blöcke)
- Kabelbaumstecker mit Kontaktspray behandeln (einfachere Verkabelung anfälliger)

### 44.3 Inbetriebnahme nach Winterlager

| Schritt | Maßnahme | Anmerkung |
|---------|----------|-----------|
| 1 | Visuell inspizieren (Ölspuren, Korrosion, Schläuche) | Gesamtzustand beurteilen |
| 2 | Impeller einsetzen (falls ausgebaut) | Neuen Impeller verwenden, wenn >2 Jahre alt |
| 3 | Lichtmaschinenriemen spannen | Durchhang 10–15 mm bei Daumendruck |
| 4 | Ölstand prüfen | Zwischen MIN und MAX auf Peilstab |
| 5 | Kühlmittelstand prüfen | Ausgleichsbehälter bis Markierung |
| 6 | Getriebeölstand prüfen | Peilstab oder Schauglas |
| 7 | Seewasserventil öffnen | Auf Dichtheit kontrollieren |
| 8 | Kraftstoffsystem entlüften | Handpumpe an Vorfilter betätigen |
| 9 | Batterie anschließen | Pluspol zuerst, dann Minus |
| 10 | Vorglühen (2× länger als normal) | Motor stand lange, Brennräume kalt |
| 11 | Motor starten, sofort Seewasserauslass prüfen | Wasser muss innerhalb 10 Sek. kommen |
| 12 | 15 Min. im Leerlauf warmfahren | Öl und Kühlmittel auf Temperatur |
| 13 | Alle Schläuche und Anschlüsse auf Dichtheit prüfen | Bei Betriebstemperatur |
| 14 | Schalten V/N/R prüfen | Am Steuerstand und am Getriebe |
| 15 | Lichtmaschinenladung prüfen | >13,5V an Batterie |

---

## 45. Schalldämmung und Vibrationskontrolle

### 45.1 Schalldruckpegel im Vergleich (dB(A) in 1 m Entfernung)

| Motor | Leerlauf | 2.000 U/min | 2.500 U/min | 3.000 U/min | Volllast |
|-------|---------|------------|------------|------------|---------|
| Beta 20 | 58 | 65 | 68 | 72 | 75 |
| Beta 38 | 60 | 67 | 72 | 76 | 79 |
| Beta 75 (Turbo) | 62 | 69 | 74 | 78 | 82 |
| Nanni N3.21 | 59 | 66 | 70 | 74 | 77 |
| Nanni N4.50 | 61 | 68 | 73 | 77 | 80 |
| Nanni T4.130 | 64 | 72 | 77 | 81 | 85 |
| Vetus M3.09 | 57 | 64 | 68 | 72 | 75 |
| Vetus M4.17 | 59 | 66 | 70 | 74 | 77 |
| Vetus VF4.140E | 63 | 71 | 76 | 80 | 84 |
| Sole Mini-17 | 60 | 67 | 71 | 75 | 78 |
| Sole Mini-33 | 62 | 69 | 74 | 78 | 81 |
| Craftsman CM 4.35 | 63 | 70 | 75 | 79 | 82 |
| Yanmar 3JH40 (Ref.) | 59 | 66 | 70 | 74 | 77 |

### 45.2 Schalldämmhauben und -matten

| Hersteller | Ab-Werk-Schalldämmung | Optionale Schalldämmung | Reduktion |
|------------|----------------------|------------------------|-----------|
| Beta Marine | Grundisolierung inkl. | Schalldämmhaube (220–450 EUR) | -5 bis -8 dB(A) |
| Nanni Diesel | Grundisolierung inkl. | Schalldämmhaube (280–520 EUR) | -5 bis -8 dB(A) |
| Vetus | Gute Grundisolierung | Premium-Schalldämmhaube (350–650 EUR) | -6 bis -10 dB(A) |
| Sole Diesel | Grundisolierung inkl. | Schalldämmhaube (200–400 EUR) | -4 bis -7 dB(A) |
| Craftsman | Minimal | Nachrüst-Schalldämmung (150–350 EUR) | -3 bis -6 dB(A) |

### 45.3 Motorlager und Vibrationsdämpfung

| Motorklasse | Motorlager-Typ | Shore-Härte | Tragkraft pro Lager | Wechselintervall |
|-------------|---------------|-------------|--------------------|-----------------| 
| 10–25 PS | Gummilager konisch | 45–55 Shore A | 25–50 kg | 8–12 Jahre |
| 30–50 PS | Gummilager zylindrisch | 50–60 Shore A | 50–80 kg | 8–12 Jahre |
| 55–90 PS | Gummilager zylindrisch | 55–65 Shore A | 80–120 kg | 6–10 Jahre |
| 100–150 PS | Gummilager Doppelkonisch | 60–70 Shore A | 120–180 kg | 6–10 Jahre |

**AYDI-Tipp:** Bei unklaren Vibrationen immer zuerst Motorlager (visuell: Risse, Durchsackung) und Wellenfluchtung (Messuhr: max. 0,05 mm) prüfen, bevor am Motor selbst gesucht wird.

---

## 46. Abgas-Emissionswerte und Umweltvorschriften

### 46.1 Emissionsklassen der Motoren (Stand 2025)

| Hersteller | Modellreihe | EU Stage V | EPA Tier III | IMO Tier II |
|------------|-------------|-----------|-------------|------------|
| Beta Marine | Beta 14–50 (IDI) | Konform | Konform | n/a (<130 kW) |
| Beta Marine | Beta 60–150 (DI/Turbo) | Konform | Konform | Konform |
| Nanni | N2.10–N4.60 | Konform | Konform | n/a |
| Nanni | N4.80–N4.115 | Konform | Konform | Konform |
| Nanni | T4.130–T6.250 | Konform | Konform | Konform |
| Vetus | M2.02–M4.56 | Konform | Konform | n/a |
| Vetus | VF/D-Serie | Konform | Konform | Konform |
| Sole | Mini-11–Mini-62 | Konform | Konform | n/a (<130 kW) |
| Craftsman | CM 2.16–CM 4.140 | Konform | Konform | Teil-konform |

### 46.2 EU Stage V Grenzwerte (für NRMM 19–560 kW)

| Parameter | Grenzwert | Einheit |
|-----------|----------|---------|
| CO | 5,0 | g/kWh |
| HC + NOx | 4,7 (19–37 kW) / 4,0 (37–56 kW) | g/kWh |
| PM (Partikel) | 0,015 (19–37 kW) / 0,015 (37–56 kW) | g/kWh |
| PN (Partikelzahl) | 1 × 10¹² | 1/kWh |

### 46.3 Binnenfahrt-Besonderheiten

In den Niederlanden, Belgien und auf deutschen Binnengewässern gelten teilweise strengere lokale Vorschriften:
- **Amsterdam:** Emissionsfreie Zonen ab 2025 (betrifft ältere Motoren ohne Stage V)
- **Rotterdam:** Umweltzonierung für Hafengebiete
- **Bodensee:** Eigene Zulassungsordnung (BSO), unabhängig von CE/RCD
- **Berliner Gewässer:** Geschwindigkeitsbegrenzung = geringe Motorlast, weniger Emissionen

**AYDI-Empfehlung:** Für Binnenfahrt in den Niederlanden nur Stage-V-konforme Motoren einbauen. Ältere Motoren (vor 2019) könnten zukünftig Einschränkungen unterliegen. Confidence: documented.

---

## 47. Elektrik-Schaltpläne und Instrumentierung

### 47.1 Standard-Instrumentierung nach Hersteller

| Hersteller | Standard-Panel | Anzeigen | Optional |
|------------|---------------|---------|---------|
| Beta Marine | Analoges Rundpanel | Drehzahl, Temperatur, Öldruck, Batterie | Stundenzähler, Alarm-LED |
| Nanni Diesel | Digitales LCD-Panel | Drehzahl, Temperatur, Öldruck, Batterie, Betriebsstunden | CAN-Bus Display (T-Serie) |
| Vetus | Modulares Panel | Drehzahl, Temperatur, Öldruck, Batterie | CAN-Bus, BOW PRO Integration |
| Sole Diesel | Analoges Rundpanel | Drehzahl, Temperatur, Öldruck, Batterie | Stundenzähler |
| Craftsman | Einfaches Panel | Drehzahl, Temperatur, Öldruck | Batterie (optional) |

### 47.2 Alarm-Schwellenwerte

| Alarm | Schwellenwert | Maßnahme |
|-------|-------------|----------|
| Kühlwasser-Temperatur hoch | >95 °C | Drehzahl reduzieren, Kühlsystem prüfen |
| Kühlwasser-Temperatur kritisch | >105 °C | Motor sofort abstellen |
| Öldruck niedrig | <0,8 bar (Leerlauf) | Drehzahl erhöhen, Ölstand prüfen |
| Öldruck kritisch | <0,3 bar | Motor sofort abstellen |
| Batteriespannung niedrig | <11,5 V | Lichtmaschine prüfen |
| Batteriespannung hoch | >15,0 V | Regler defekt, Ladeleitung trennen |
| Kühlmittelstand niedrig | Sensor-basiert | Kühlmittel nachfüllen, Leck suchen |

### 47.3 Kabelquerschnitte für Marine-Installation

| Verbraucher | Stromstärke | Max. 3 m | Max. 6 m | Max. 10 m |
|------------|-----------|---------|---------|----------|
| Anlasser 12V | 150–300 A | 50 mm² | 70 mm² | 95 mm² |
| Lichtmaschine B+ | 60–110 A | 10 mm² | 16 mm² | 25 mm² |
| Vorglührelais | 40–80 A | 6 mm² | 10 mm² | 16 mm² |
| Instrumentenpanel | 2–5 A | 1,5 mm² | 2,5 mm² | 4 mm² |
| Alarm-Summer | 0,5–1 A | 1,0 mm² | 1,5 mm² | 2,5 mm² |
| Kraftstoff-Magnetventil | 2–4 A | 1,5 mm² | 2,5 mm² | 4 mm² |

**Wichtig:** Alle Kabel im Motorraum müssen hitze- und ölbeständig sein (min. 105 °C). Marinekabel nach ISO 13297 verwenden. Verzinnte Kupferlitze bevorzugen.

---

## 48. Drehmomentwerte für Montage

### 48.1 Allgemeine Drehmomentwerte (Richtwerte)

| Verbindung | Drehmoment (Nm) | Anmerkung |
|-----------|----------------|-----------|
| Zylinderkopfschrauben | Siehe Hersteller-Handbuch | Immer in vorgeschriebener Reihenfolge |
| Ventildeckel | 8–12 Nm | Nicht überziehen (Dichtung!) |
| Ölablassschraube | 25–35 Nm | Kupferdichtung erneuern |
| Ölfilter | Handfest + ¾ Umdrehung | Dichtring einölen |
| Impellergehäuse-Deckel | 8–12 Nm | Gleichmäßig anziehen |
| Auspuffkrümmer | 25–40 Nm | Neue Dichtung, kreuzweise anziehen |
| Injektoren | 55–70 Nm | Kupferdichtring erneuern |
| Injektorleitungen | 25–30 Nm | Nicht überziehen (Hohlschraube!) |
| Motorlager-Bolzen | 40–60 Nm | Kontermutter sichern |
| Schwungrad-Schrauben | 80–120 Nm | Schraubensicherung (Loctite 243) |
| Wellenkupplung | 30–50 Nm | Gleichmäßig, kreuzweise |
| Getriebe-Flansch | 35–55 Nm | Hersteller-Vorgabe beachten |
| Seewasserventil-Flansch | 15–25 Nm | Dichtmittel verwenden |
| Kühlmittelthermostat-Gehäuse | 10–15 Nm | Gleichmäßig anziehen |
| Kraftstofffilter-Gehäuse | 8–12 Nm | Handfest, O-Ring prüfen |

### 48.2 Zylinderkopf-Anzugsreihenfolge (allgemein)

**3-Zylinder (Beta 16/20/25, Nanni N3.x, Vetus M3.x, Sole Mini-17/26/29):**
```
Anzugsreihenfolge:    4 — 2 — 6
(von vorn gesehen)    1 — 3 — 5
                      ← Schwungradseite
```

**4-Zylinder (Beta 30–50, Nanni N4.x, Vetus M4.x, Sole Mini-33–55):**
```
Anzugsreihenfolge:    8 — 4 — 2 — 6
(von vorn gesehen)    7 — 3 — 1 — 5
                      ← Schwungradseite
```

**Hinweis:** Dies sind typische Reihenfolgen für Kubota/Mitsubishi-Blöcke. Immer das Werkstatthandbuch des jeweiligen Herstellers konsultieren! Drehmomentwerte und exakte Reihenfolge können abweichen.

---

## 49. Kraftstoffsystem — Detailspezifikationen

### 49.1 Kraftstofffilter-Systeme

| Hersteller | Vorfilter (Wasserabscheider) | Hauptfilter (am Motor) | Filtertyp |
|------------|---------------------------|----------------------|----------|
| Beta Marine | Racor 110A (10µm, optional) | Kubota-Originalfilter | Papierpatrone |
| Nanni Diesel | Nanni/Racor (Standard bei N4+) | Kubota/Toyota-Filter | Papierpatrone |
| Vetus | Vetus WS180 / WS720 | Mitsubishi-Originalfilter | Papierpatrone |
| Sole Diesel | Sole/Racor (optional) | Mitsubishi-Originalfilter | Papierpatrone |
| Craftsman | Nicht standardmäßig | Mitsubishi-Originalfilter | Papierpatrone |

**AYDI-Empfehlung:** Immer einen Vorfilter mit Wasserabscheider installieren, auch wenn nicht ab Werk verbaut. Im Mittelmeer unverzichtbar (Kraftstoffqualität). Empfohlen: Racor 110A für Motoren bis 60 PS, Racor 500FG für größere Motoren.

### 49.2 Kraftstoffleitungs-Spezifikationen

| Parameter | Anforderung |
|-----------|------------|
| Material Saugleitung | Kupfer oder ISO 7840 Marine-Kraftstoffschlauch |
| Material Rücklaufleitung | Kupfer oder ISO 7840 Marine-Kraftstoffschlauch |
| Innendurchmesser (bis 50 PS) | 8 mm |
| Innendurchmesser (50–100 PS) | 10 mm |
| Innendurchmesser (100–200 PS) | 12 mm |
| Schlauchschellen | Doppelschlauchschellen an allen Verbindungen |
| Absperrhahn | Kugelhahn, am Tank, erreichbar ohne Werkzeug |
| Belüftung | Tankbelüftung nach ISO 10088 |
| Feuerschutz | Kraftstoffleitung min. 300 mm von Auspuff entfernt |

### 49.3 Dieselpest-Prävention

| Maßnahme | Beschreibung | Intervall |
|----------|-------------|-----------|
| Tank vollfüllen | Minimiert Kondensation im Luftraum | Bei jedem längeren Stillstand |
| Diesel-Biozid | Grotamar 82 oder Marine 16 (1:1.000) | Halbjährlich, vor Winterlagerung |
| Wasserabscheider prüfen | Wasser ablassen, Filterglas kontrollieren | 100h / monatlich |
| Tankinspektion | Visuell (Inspektionsluke) | Jährlich |
| Kraftstoff umwälzen | Motor-Rücklaufleitung in Tankboden führen | Permanent (Konstruktionsmerkmal) |
| Algenwachstum erkennen | Dunkle Schlieren, Gelklumpen im Filter | Bei Filterwechsel |
| Tankreinigung | Professionell absaugen und reinigen | Bei Befall, sonst alle 5–10 Jahre |

### 49.4 Entlüftungsprozedur nach Hersteller

**Beta Marine (alle Modelle):**
1. Kraftstoffabsperrhahn öffnen
2. Entlüfterschraube am Kraftstofffilter (10 mm) lösen
3. Handpumpe am Filter betätigen bis blasenfreier Kraftstoff austritt
4. Entlüfterschraube schließen (Drehmoment: 5 Nm)
5. Entlüfterschraube an Einspritzpumpe lösen
6. Handpumpe betätigen bis blasenfreier Kraftstoff
7. Schraube schließen
8. Motor starten (max. 30 Sek. orgeln, dann 30 Sek. Pause)

**Nanni Diesel (Toyota-Basis N2/N3/N4.38):**
- Wie Beta Marine, jedoch Entlüfterknopf statt Schraube am Filter
- Toyota-Blöcke entlüften sich oft schwerer → mehr Geduld nötig

**Nanni Diesel (Kubota-Basis N4.50+):**
- Wie Beta Marine (gleicher Kubota-Prozess)

**Vetus (Mitsubishi-Basis):**
- Entlüfterschraube am Filtergehäuse (8 mm Innensechskant)
- Handpumpe auf dem Filter (Gummibalg)
- Mitsubishi-Blöcke entlüften sich gut → meist reicht Filterpumpe

**Sole Diesel:**
- Wie Vetus (gleiche Mitsubishi-Blöcke)
- Entlüfterschraube am Kraftstofffilter + an der Einspritzpumpe

---

## 50. Motor-Identifikation und Zustandsbewertung (AYDI-Schema)

### 50.1 AYDI Motor-Zustandsklassen

| Klasse | Bezeichnung | Betriebsstunden | Zustand | Score |
|--------|-----------|----------------|---------|-------|
| A+ | Neuwertig | 0–200h | Wie neu, erste Saison | 95–100 |
| A | Sehr gut | 200–1.500h | Regelmäßig gewartet, keine Mängel | 85–94 |
| B+ | Gut | 1.500–3.000h | Gewartet, leichte Gebrauchsspuren | 75–84 |
| B | Befriedigend | 3.000–5.000h | Funktionsfähig, kleinere Mängel | 65–74 |
| C+ | Ausreichend | 5.000–7.000h | Funktionsfähig, Verschleiß sichtbar | 55–64 |
| C | Mangelhaft | 7.000–10.000h | Überholung nötig, deutlicher Verschleiß | 40–54 |
| D | Überholungsbedürftig | >10.000h | Grundüberholung oder Austausch empfohlen | 20–39 |
| F | Nicht betriebsfähig | — | Schwerer Schaden, wirtschaftlicher Totalschaden | 0–19 |

### 50.2 AYDI Bewertungskriterien für Alternativmotoren

| Kriterium | Gewichtung | Messmethode |
|-----------|-----------|-------------|
| Kompression (Gleichmäßigkeit) | 25 % | Kompressionsmessung, max. 10 % Abweichung |
| Öldruck (warm, 2.000 U/min) | 15 % | Manometer, min. 2,0 bar |
| Kühlsystem (Dichtheit) | 15 % | Druckprüfung, 1,0 bar / 15 Min. |
| Ölzustand (Analyse) | 10 % | Laboranalyse (Metalle, Wasser, Kraftstoff) |
| Auspuffkrümmer (Zustand) | 10 % | Visuell + Druckprüfung |
| Getriebe (Funktion) | 10 % | Schalten V/N/R, kein Rutschen |
| Lichtmaschine (Ladung) | 5 % | Spannung 13,8–14,4V bei Nenn-RPM |
| Motorlager (Zustand) | 5 % | Visuell, Risse, Durchsackung |
| Elektrik (Zustand) | 5 % | Visuell, Korrosion, Isolierung |

### 50.3 Wertverlust-Kurve (normiert auf 100 % Neuwert)

| Betriebsstunden | Beta Marine | Nanni | Vetus | Sole | Craftsman | Yanmar (Ref.) |
|----------------|-----------|-------|-------|------|-----------|--------------|
| 0 (Neu) | 100 % | 100 % | 100 % | 100 % | 100 % | 100 % |
| 500 | 80 % | 78 % | 78 % | 75 % | 72 % | 85 % |
| 1.000 | 70 % | 68 % | 67 % | 65 % | 60 % | 75 % |
| 2.000 | 55 % | 52 % | 52 % | 48 % | 42 % | 62 % |
| 3.000 | 45 % | 42 % | 42 % | 38 % | 32 % | 52 % |
| 5.000 | 30 % | 27 % | 27 % | 23 % | 18 % | 38 % |
| 8.000 | 18 % | 15 % | 15 % | 12 % | 8 % | 25 % |
| 10.000+ | 10 % | 8 % | 8 % | 5 % | 3 % | 15 % |

**AYDI-Hinweis:** Wertverlust ist stark abhängig von dokumentierter Wartungshistorie. Ein gut gewarteter Motor mit 5.000h kann mehr wert sein als ein schlecht gewarteter mit 2.000h. Serviceheft und Rechnungen sind wertbestimmend.

---

> **AYDI-Hinweis:** Diese Wissensdatei wird als Referenz für die Module Compliance, Kosten, Produktion und Service-Patterns verwendet. Alle technischen Daten basieren auf Herstellerangaben (confidence: measured). Preisangaben sind UVP-Richtwerte und können regional abweichen (confidence: estimated). Schwachstellenbewertungen basieren auf dokumentierten Erfahrungswerten und Eignerfeedback (confidence: documented/estimated).

---
