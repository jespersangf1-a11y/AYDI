---
title: "Winschen Wartung und Troubleshooting"
kategorie: "09 Winschen"
unterkategorie: "07 Wartung und Troubleshooting"
version: "1.0.0"
datum: "2026-04-25"
autor: "AYDI Research"
status: "validated"
bereich: "Rigg & Deck"
confidence_quellen:
  - measured: "Hersteller-TDS, Werkstattmessungen"
  - documented: "Hersteller-Kataloge, Service-Bulletins, Werft-Dokumentation"
  - estimated: "Erfahrungswerte Rigger, Forum-Konsens"
  - benchmark: "Regatta-Teams, Charterflotten-Statistiken"
tags:
  - winschen
  - wartung
  - troubleshooting
  - harken
  - lewmar
  - andersen
  - antal
  - schmiermittel
  - verschleissteile
  - service
  - instandhaltung
  - fehlerdiagnose
cross_references:
  - "09_01_winschen_grundlagen.md"
  - "09_02_harken_winschen.md"
  - "09_03_lewmar_winschen.md"
  - "09_04_andersen_winschen.md"
  - "09_05_antal_winschen.md"
  - "09_06_elektrische_winschen.md"
---

# 09.07 — Winschen Wartung und Troubleshooting: Umfassende Cross-Brand-Referenz

> **AYDI Wissensdatei 09.07** — Kategorie 9: Winschen
> **Confidence-Quelle:** measured (Hersteller-TDS), documented (Hersteller-Kataloge, Service-Bulletins), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-25

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Wartungsintervalle und -pläne](#3-wartungsintervalle-und--pläne)
4. [Schritt-für-Schritt Wartungsanleitungen](#4-schritt-für-schritt-wartungsanleitungen)
5. [Schmiermittel und Reinigungsmittel](#5-schmiermittel-und-reinigungsmittel)
6. [Verschleißteile und Ersatzteilplanung](#6-verschleißteile-und-ersatzteilplanung)
7. [Anlagen-spezifische Zuordnung](#7-anlagen-spezifische-zuordnung)
8. [Fehlerbild-Atlas](#8-fehlerbild-atlas)
9. [Troubleshooting-Entscheidungsbaum](#9-troubleshooting-entscheidungsbaum)
10. [FAQ](#10-faq)
11. [Glossar](#11-glossar)
12. [Schnell-Referenz](#12-schnell-referenz)
13. [Anhänge A–R](#13-anhänge-ar)

---

## 1. Einführung und Übersicht

### 1.1 Bedeutung der Winsch-Wartung

Winschen gehören zu den am höchsten belasteten mechanischen Bauteilen an Bord einer Segelyacht. Sie wandeln manuelle Kraft in kontrollierte Seilzugkraft um und sind dabei extremen Umgebungsbedingungen ausgesetzt: Salzwasser, UV-Strahlung, mechanische Stoßbelastungen und thermische Zyklen. Eine regelmäßige, fachgerechte Wartung ist nicht nur eine Frage der Betriebssicherheit, sondern hat direkte Auswirkungen auf die Leistungsfähigkeit, Lebensdauer und den Wiederverkaufswert einer Yacht.

**Kernstatistiken zur Wartungsrelevanz (Confidence: benchmark):**

| Aspekt | Wert | Quelle |
|--------|------|--------|
| Leistungsverlust ohne Wartung (1 Saison) | 15–30 % | Harken Technical Bulletin TB-2024-03 |
| Leistungsverlust ohne Wartung (3 Saisons) | 40–65 % | Lewmar Service Data 2023 |
| Häufigste Ursache für Winsch-Ausfall | Mangelnde Schmierung (47 %) | Charterflotten-Analyse, 2.400 Fälle |
| Durchschnittliche Reparaturkosten (Totalausfall) | 800–2.500 EUR | Werft-Statistiken DACH 2024 |
| Durchschnittliche Wartungskosten (jährlich) | 45–120 EUR | AYDI Kalkulation |
| ROI einer jährlichen Wartung | 12:1 bis 28:1 | Lebensdauervergleich gewartete vs. ungewartete Winschen |

### 1.2 Kosten der Vernachlässigung

Die Kosten der Nichtbeachtung übersteigen die Wartungskosten um ein Vielfaches. Eine vernachlässigte Winsch durchläuft typischerweise folgende Degradationsstufen:

**Stufe 1 — Leistungsminderung (0–12 Monate ohne Wartung):**
- Erhöhte Kurbelbetätigung erforderlich
- Leichtes Knirschen oder Kratzen hörbar
- Self-Tailing-Mechanismus greift unzuverlässig
- Geschätzter Wertverlust: 5–10 % der Winsch

**Stufe 2 — Funktionseinschränkung (12–36 Monate ohne Wartung):**
- Sperrklinken greifen verzögert oder unregelmäßig
- Korrosion an Lager- und Achsflächen
- Federkraft der Pawl-Springs nachgelassen
- Geschätzter Wertverlust: 20–40 % der Winsch

**Stufe 3 — Teilausfall (36–60 Monate ohne Wartung):**
- Eine oder mehrere Geschwindigkeitsstufen funktionieren nicht
- Lagerfressen unter Last möglich
- Self-Tailing-Backen verschlissen, Schot rutscht
- Geschätzter Wertverlust: 50–75 % der Winsch

**Stufe 4 — Totalausfall (>60 Monate ohne Wartung):**
- Winsch blockiert unter Last oder dreht durch
- Korrosionsschäden an Trommel und Basis irreversibel
- Sicherheitsrisiko bei Manövern
- Geschätzter Wertverlust: 80–100 % der Winsch (Austausch notwendig)

### 1.3 Wartungsphilosophie

Die AYDI-Wartungsphilosophie basiert auf drei Grundprinzipien:

1. **Präventiv statt reaktiv:** Regelmäßige Wartung nach definierten Intervallen, nicht erst bei Symptomen.
2. **Herstellerspezifisch:** Jeder Hersteller hat eigene Spezifikationen für Schmiermittel, Drehmomente und Ersatzteile. Diese müssen eingehalten werden.
3. **Dokumentiert:** Jede Wartung wird protokolliert — für die Betriebssicherheit, den Wiederverkaufswert und die AYDI-Zustandsanalyse.

**Confidence-Bewertung dieses Abschnitts:**
- Statistiken: `benchmark` — aggregierte Branchendaten
- Degradationsstufen: `documented` — Hersteller-Service-Bulletins und Werft-Erfahrung
- Kostenangaben: `estimated` — AYDI-Kalkulation auf Basis von Marktpreisen 2024/2025

---

## 2. Grundlagen und Theorie

### 2.1 Tribologie-Grundlagen für Winschen

Die Tribologie — die Wissenschaft von Reibung, Verschleiß und Schmierung — ist das zentrale Wissensgebiet für das Verständnis der Winsch-Wartung. In einer Winsch treten mehrere tribologische Kontaktsituationen auf:

**Gleitkontakte:**
- Achse ↔ Buchse (Zentralachse/Trommel)
- Sperrklinke ↔ Zahnkranz (Pawl/Ratchet)
- Self-Tailing-Backen ↔ Schot (Jaw-Inserts/Rope)

**Wälzkontakte:**
- Nadellager ↔ Laufbahn
- Kugellager ↔ Laufring
- Rollenlager ↔ Achszapfen

**Mischkontakte:**
- Getriebezähne (Planetengetriebe)
- Federkontakte (Pawl-Springs)
- Dichtlippen ↔ Achse

#### 2.1.1 Reibungskoeffizienten in der Winsch

| Kontaktpaar | Trocken (μ) | Geschmiert (μ) | Reduktion |
|-------------|-------------|-----------------|-----------|
| Edelstahl/Bronze (Achse/Buchse) | 0.35–0.45 | 0.04–0.08 | 85–90 % |
| Edelstahl/Edelstahl (Pawl/Ratchet) | 0.55–0.70 | 0.08–0.12 | 80–85 % |
| Edelstahl/Delrin (Lager) | 0.20–0.30 | 0.05–0.10 | 65–75 % |
| Edelstahl/PTFE (Buchse) | 0.04–0.08 | 0.02–0.04 | 50 % |
| Aluminium/Bronze (eloxiert) | 0.40–0.55 | 0.06–0.10 | 82–85 % |

**Praktische Bedeutung:** Eine ungeschmierte Winsch erfordert bis zu 8-mal mehr Kraft für dieselbe Arbeit. Die Schmierung ist der einzelne wichtigste Wartungsfaktor.

#### 2.1.2 Verschleißmechanismen

In einer Winsch treten vier Haupt-Verschleißmechanismen auf:

**Adhäsiver Verschleiß (Fressen):**
- Entsteht bei Metall-Metall-Kontakt ohne ausreichende Schmierung
- Besonders kritisch: Achse ↔ Buchse unter hoher Last
- Erkennbar an Riefenbildung, Materialübertrag, erhöhtem Spiel
- Hauptursache: Fettmangel, falsches Schmiermittel

**Abrasiver Verschleiß (Abrieb):**
- Fremdpartikel (Salzkristalle, Sand, Korrosionsprodukte) wirken als Schleifmittel
- Besonders kritisch: Lagerflächen, Zahnflanken
- Erkennbar an Materialabtrag, Vergrößerung von Toleranzen
- Hauptursache: Mangelnde Reinigung, eindringendes Seewasser

**Oberflächenermüdung (Pitting):**
- Zyklische Belastung führt zu Mikrorissen unter der Oberfläche
- Besonders kritisch: Kugel-/Nadellager, Zahnkranz
- Erkennbar an kleinen Kratern (Pits) auf den Laufflächen
- Hauptursache: Überlasten, Schlagbelastungen, Alterung

**Korrosiver Verschleiß:**
- Elektrochemische Korrosion (galvanische Korrosion, Spaltkorrosion, Lochfraß)
- Besonders kritisch: Edelstahl in Salzwasser-Umgebung, Kontakt verschiedener Metalle
- Erkennbar an Verfärbungen, Lochfraß, Ablagerungen
- Hauptursache: Salzwasser-Einwirkung, fehlende Spülung

### 2.2 Korrosionsmechanismen in der Winsch

#### 2.2.1 Galvanische Korrosion

Die Kombination verschiedener Metalle in einer Winsch erzeugt galvanische Elemente:

| Materialpaarung | Potentialdifferenz (mV) | Korrosionsrisiko |
|-----------------|------------------------|------------------|
| Edelstahl 316 / Aluminium (eloxiert) | 550–750 | Hoch |
| Edelstahl 316 / Bronze | 50–100 | Gering |
| Edelstahl 316 / Delrin | 0 (kein Metall) | Keines |
| Aluminium / Bronze | 500–650 | Hoch |
| Edelstahl 304 / Edelstahl 316 | 20–50 | Minimal |

**Schutzmaßnahmen in modernen Winschen:**
- Kunststoffbuchsen als galvanische Isolation (Harken, Andersen)
- Eloxierung von Aluminium-Trommeln (alle Hersteller)
- Fettschicht als Barriere (wartungsabhängig)
- Opferanoden bei elektrischen Winschen (Lewmar, Harken)

#### 2.2.2 Spaltkorrosion (Crevice Corrosion)

Spaltkorrosion entsteht in engen Spalten, in denen Salzwasser stagniert und der Sauerstoffgehalt sinkt. In Winschen betrifft dies:

- Achse ↔ Buchse (enger Spalt, Wasser dringt kapillar ein)
- Schraubverbindungen (Trommel ↔ Basis)
- O-Ring-Nuten (wenn O-Ring defekt)
- Self-Tailing-Backen ↔ Halterung

**Schutz:** Regelmäßiges Süßwasser-Spülen, konservierendes Fett in allen Spalten, intakte Dichtungen.

#### 2.2.3 Lochfraß (Pitting)

Chlorid-Ionen im Seewasser durchbrechen die passive Oxidschicht von Edelstahl. Dies betrifft besonders:

- Edelstahl 304 (weniger Molybdän als 316) — häufig bei günstigen Winschen
- Stellen mit mechanischer Vorschädigung (Kratzer, Schlagspuren)
- Bereiche unter Dauerspannung (Spannungsrisskorrosion)

**Erkennung:** Braune/rostfarbene Punkte auf Edelstahloberflächen, die sich nicht wegwischen lassen.

### 2.3 Fettchemie für die Winsch-Wartung

#### 2.3.1 Aufbau von Schmierfetten

Ein Schmierfett besteht aus drei Komponenten:

1. **Grundöl (70–90 %):** Mineral- oder Syntheseöl, bestimmt Viskosität und Temperaturverhalten
2. **Verdicker (5–20 %):** Metallseife (Lithium, Calcium, Barium) oder Nicht-Seife (PTFE, Silica), bildet die Struktur
3. **Additive (1–10 %):** Korrosionsschutz, EP-Additive (Extreme Pressure), Verschleißschutz, Oxidationsstabilisatoren

#### 2.3.2 NLGI-Klassen

| NLGI-Klasse | Konsistenz | Winsch-Anwendung |
|-------------|-----------|------------------|
| 000 | Flüssig | Nicht für Winschen geeignet |
| 00 | Halbflüssig | Getriebezähne (bei Kälte) |
| 0 | Sehr weich | Interne Getriebe, Zahnräder |
| 1 | Weich | Achsen, Lager (Standard) |
| 2 | Mittel | Pawl-Springs, Allzweck |
| 3 | Fest | Nicht empfohlen (zu steif bei Kälte) |

#### 2.3.3 Spezifische Winsch-Fette im Vergleich

| Eigenschaft | Harken White Grease (BK4520) | Lewmar Winch Grease (19701500) | Andersen Service Grease | Winch-Mate |
|-------------|------------------------------|-------------------------------|------------------------|------------|
| Grundöl | PAO-Synthese | Mineralöl/Synthese-Blend | PAO-Synthese | Mineralöl |
| Verdicker | Lithium-Komplex | Lithium | Calcium-Sulfonat | Lithium |
| NLGI-Klasse | 1–2 | 2 | 1–2 | 2 |
| Temperaturbereich | –30 °C bis +150 °C | –20 °C bis +130 °C | –35 °C bis +160 °C | –15 °C bis +120 °C |
| Salzwasserbeständigkeit | Hervorragend | Gut | Hervorragend | Befriedigend |
| Farbe | Weiß | Bernstein | Weiß | Bernstein/Gelb |
| Tropfpunkt | >200 °C | >180 °C | >220 °C | >170 °C |
| EP-Additive | Ja | Ja | Ja | Nein |
| PTFE-Anteil | Ja | Nein | Ja | Nein |
| Biologisch abbaubar | Nein | Nein | Teilweise | Nein |
| Preis (ca.) | 18 EUR / 100 g | 12 EUR / 100 g | 22 EUR / 100 g | 9 EUR / 100 g |

#### 2.3.4 Winsch-Öl

Für die Schmierung von Pawl-Springs und feinmechanischen Teilen wird dünnflüssiges Öl benötigt:

| Produkt | Hersteller | Art.-Nr. | Viskosität | Anwendung |
|---------|-----------|----------|-----------|-----------|
| Harken Pawl Oil | Harken | BK4521 | ISO VG 32 | Sperrklinken-Federn, Achsen |
| Lewmar Winch Oil | Lewmar | 19701600 | ISO VG 46 | Sperrklinken, feinmechanische Teile |
| McLube OneDrop | McLube | 1600 | ISO VG 22 | Allzweck-Winschöl |
| Ballistol Universal | Ballistol | 21000 | ISO VG 68 | Notlösung, nicht ideal |

### 2.4 Verschleißmuster und Lebensdauerprognose

#### 2.4.1 Typische Verschleißkurve einer Winsch

```
Leistung (%)
100 ┤━━━━━━━━━┓
 90 ┤          ┗━━━━━┓
 80 ┤                 ┗━━━┓
 70 ┤                     ┗━━┓
 60 ┤                        ┗━━┓
 50 ┤                            ┗━┓
 40 ┤                               ┗━━┓
 30 ┤                                   ┗━━━┓
 20 ┤                                       ┗━━━━━
    ┼──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──┬──
    0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15
                    Jahre ohne Wartung

--- GEWARTET (jährlich): ~95 % Leistung nach 15 Jahren
━━━ UNGEWARTET: ~20 % Leistung nach 15 Jahren
```

#### 2.4.2 Lebensdauererwartung nach Bauteil

| Bauteil | Lebensdauer (gewartet) | Lebensdauer (ungewartet) | Faktor |
|---------|----------------------|------------------------|--------|
| Trommel (eloxiert) | 25–40 Jahre | 15–25 Jahre | 1.6x |
| Basis (Edelstahl/Alu) | 30–50 Jahre | 20–30 Jahre | 1.5x |
| Zentralachse | 20–35 Jahre | 8–15 Jahre | 2.3x |
| Lager (Nadel/Kugel) | 10–15 Jahre | 3–7 Jahre | 2.5x |
| Pawl-Springs | 3–5 Jahre | 1–3 Jahre | 2.0x |
| Sperrklinken (Pawls) | 8–15 Jahre | 3–8 Jahre | 2.0x |
| Zahnkranz (Ratchet) | 15–25 Jahre | 5–12 Jahre | 2.3x |
| Self-Tailing-Backen | 5–8 Jahre | 2–5 Jahre | 2.0x |
| O-Ringe/Dichtungen | 3–5 Jahre | 1–2 Jahre | 2.5x |
| Getriebezähne (Planeten) | 20–30 Jahre | 8–15 Jahre | 2.0x |

**Confidence:** `documented` — Hersteller-Servicehandbücher, Werft-Erfahrungswerte

---

## 3. Wartungsintervalle und -pläne

### 3.1 Allgemeines Wartungsschema

Die Wartungsintervalle richten sich nach Nutzungsintensität, Einsatzgebiet und Bootsklasse. Das folgende Schema gilt als Mindestanforderung:

#### 3.1.1 Nach jedem Einsatz (Pflicht bei Salzwasser)

| Maßnahme | Dauer | Werkzeug | Priorität |
|----------|-------|----------|-----------|
| Süßwasser-Spülung der Winschen | 2 min/Winsch | Gartenschlauch, Sprühflasche | Hoch |
| Trommel mit Süßwasser abwischen | 1 min/Winsch | Schwamm, Süßwasser | Hoch |
| Self-Tailing-Backen von Salzrückständen befreien | 1 min/Winsch | Weiche Bürste | Mittel |
| Sichtprüfung auf offensichtliche Schäden | 30 s/Winsch | Augen | Hoch |
| Winsch 2–3 Umdrehungen leer drehen | 30 s/Winsch | Hand/Kurbel | Mittel |
| Winschkurbel abziehen und verstauen | 10 s/Winsch | — | Hoch |

**Zeitaufwand bei 6 Winschen:** ca. 25 Minuten

**Hinweis:** Das reine Süßwasser-Abspülen der Winschen nach dem Segeln ist die einzelne wirksamste Maßnahme zur Verlängerung der Lebensdauer. Salzkristalle in den Lagern wirken wie Schleifmittel und beschleunigen den Verschleiß um den Faktor 3–5.

#### 3.1.2 Monatliche Wartung (bei regelmäßiger Nutzung)

| Maßnahme | Dauer | Werkzeug |
|----------|-------|----------|
| Funktionsprüfung aller Geschwindigkeitsstufen | 2 min/Winsch | Winschkurbel |
| Self-Tailing-Funktion mit Schot prüfen | 2 min/Winsch | Testtau (8–12 mm) |
| Sperrklinken-Klickgeräusch bewerten | 1 min/Winsch | Ohren |
| Leichtgängigkeit im Vergleich bewerten | 2 min/Winsch | Winschkurbel |
| Trommeloberfläche auf Korrosion prüfen | 1 min/Winsch | Augen, Lupe |
| Befestigungsschrauben auf festen Sitz prüfen | 1 min/Winsch | Hand |

**Zeitaufwand bei 6 Winschen:** ca. 50 Minuten

**Dokumentation:** Auffälligkeiten im Bordbuch notieren. AYDI-Zustandsprotokoll verwenden (siehe Anhang L).

#### 3.1.3 Saisonale Wartung (Frühjahr/Herbst)

**Frühjahr — Inbetriebnahme:**

| Schritt | Maßnahme | Werkzeug | Dauer |
|---------|----------|----------|-------|
| 1 | Visuelle Gesamtinspektion aller Winschen | Lupe, Taschenlampe | 20 min |
| 2 | Trommel abnehmen (wo ohne Demontage möglich) | Ggf. Ringschlüssel | 10 min/Winsch |
| 3 | Sperrklinken und Federn sichtprüfen | Taschenlampe | 5 min/Winsch |
| 4 | Oberflächenschmierung erneuern | Herstellerfett, Ölkännchen | 5 min/Winsch |
| 5 | Self-Tailing-Backen prüfen, ggf. tauschen | Schraubendreher | 5 min/Winsch |
| 6 | Funktionsprüfung unter leichter Last | Winschkurbel, Testtau | 3 min/Winsch |
| 7 | Befestigungsmomente prüfen | Drehmomentschlüssel | 3 min/Winsch |

**Zeitaufwand bei 6 Winschen:** ca. 4–5 Stunden

**Herbst — Einlagerung:**

| Schritt | Maßnahme | Werkzeug | Dauer |
|---------|----------|----------|-------|
| 1 | Gründliche Süßwasser-Reinigung | Schlauch, Eimer, Bürste | 15 min |
| 2 | Alle Winschen komplett demontieren | Winsch-Werkzeugsatz | 30 min/Winsch |
| 3 | Alle Teile in Petroleum/White Spirit reinigen | Wanne, Pinsel, Lappen | 20 min/Winsch |
| 4 | Alle Teile inspizieren und dokumentieren | Lupe, Checkliste | 15 min/Winsch |
| 5 | Defekte Teile identifizieren und bestellen | Ersatzteilkatalog | Variable |
| 6 | Neu fetten und zusammenbauen | Herstellerfett | 20 min/Winsch |
| 7 | Korrosionsschutz auf Trommeloberfläche | Sprühwachs oder Korrosionsschutzöl | 5 min/Winsch |
| 8 | Winschkurbel-Aufnahme abdecken | Kappe oder Klebeband | 1 min/Winsch |

**Zeitaufwand bei 6 Winschen:** ca. 8–10 Stunden (inkl. Reinigung)

#### 3.1.4 Jährliche Vollwartung

Die jährliche Vollwartung umfasst die komplette Demontage, Reinigung, Inspektion und Neufettung aller Winschen. Sie ist der Herbstwartung ähnlich, aber mit zusätzlichen Messprüfungen:

| Zusätzliche Maßnahmen | Werkzeug | Kriterium |
|----------------------|----------|-----------|
| Axialspiel der Zentralachse messen | Messuhr, Messschieber | <0.5 mm (Harken), <0.3 mm (Andersen) |
| Lagerspiel der Nadellager messen | Fühlerlehre | <0.1 mm |
| Zahnflankenverschleiß beurteilen | Lupe (10x), Referenzbild | Kein sichtbarer Materialabtrag |
| Federkraft der Pawl-Springs prüfen | Federwaage (optional) | >80 % der Nennkraft |
| Korrosionszustand der Basis bewerten | Visuell, Klopfprüfung | Keine Verfärbungen, kein Hohlklang |
| Self-Tailing-Profil messen | Messschieber | Profiltiefe >1.5 mm |
| O-Ringe / Dichtungen prüfen | Visuell, Drucktest | Kein Riss, elastisch |
| Gewindezustand der Befestigung prüfen | Gewindebohrer (M6/M8) | Leichtgängig, kein Ausreißer |

**Zeitaufwand bei 6 Winschen:** ca. 10–14 Stunden (voller Arbeitstag)

#### 3.1.5 5-Jahres-Generalüberholung

Alle 5 Jahre sollte eine professionelle Generalüberholung durchgeführt werden, idealerweise durch den Hersteller oder einen zertifizierten Servicepartner:

| Maßnahme | Beschreibung |
|----------|-------------|
| Komplette Demontage inkl. Basis | Alle Teile bis zur einzelnen Schraube |
| Ultraschallreinigung aller Metallteile | Professionelle Reinigung in Ultraschallbad |
| Maßkontrolle aller verschleißrelevanten Teile | Messprotokoll mit Soll/Ist-Vergleich |
| Austausch aller Verschleißteile | Pawl-Springs, O-Ringe, Jaw-Inserts, ggf. Lager |
| Oberflächenaufarbeitung der Trommel | Nachpolieren oder Neu-Eloxierung |
| Prüfung der Basis-Befestigung | Bolzen, Backing-Plate, Dichtung zur Decksfläche |
| Leistungsmessung nach Zusammenbau | Drehmomentmessung im Leerlauf vs. Referenzwert |
| Dokumentation und Zertifikat | Serviceprotokoll mit Seriennummer |

**Kosten (Schätzung):**

| Winschgröße | Material | Arbeit (Werft) | Arbeit (Eigenleistung) | Gesamt (Werft) |
|-------------|----------|----------------|----------------------|----------------|
| Klein (Size 16–20) | 80–120 EUR | 150–250 EUR | 4–6 h | 230–370 EUR |
| Mittel (Size 40–48) | 120–200 EUR | 250–400 EUR | 6–8 h | 370–600 EUR |
| Groß (Size 50–70) | 200–350 EUR | 400–650 EUR | 8–12 h | 600–1.000 EUR |
| Elektrisch (beliebig) | 300–800 EUR | 500–1.200 EUR | n/a (Werft) | 800–2.000 EUR |

### 3.2 Herstellerspezifische Wartungspläne

#### 3.2.1 Harken — Wartungsvorgaben

**Quelle:** Harken Technical Service Manual, Revision 2024

Harken empfiehlt ein abgestuftes Wartungsprogramm:

**Stufe A — Basiswartung (alle 3 Monate oder 100 Betriebsstunden):**
- Trommel abnehmen, Sperrklinken sichtprüfen
- Pawl-Springs ölen mit Harken Pawl Oil (BK4521)
- Self-Tailing-Backen reinigen
- Trommel wieder aufsetzen, Funktionsprüfung

**Stufe B — Standardwartung (jährlich oder 300 Betriebsstunden):**
- Komplette Demontage (Trommel, obere Getriebeplatte, Sperrklinken, Lager)
- Reinigung aller Teile in White Spirit (KEIN Aceton!)
- Inspektion aller Verschleißteile
- Neufettung mit Harken White Grease (BK4520)
- Pawl-Springs ölen mit Harken Pawl Oil (BK4521)
- Zusammenbau in umgekehrter Reihenfolge

**Stufe C — Generalüberholung (alle 5 Jahre oder 1.500 Betriebsstunden):**
- Komplette Demontage inkl. Basis und Zentralachse
- Austausch: alle Pawl-Springs, O-Ringe, ggf. Jaw-Inserts
- Maßkontrolle der Achse, Lager, Zahnräder
- Oberflächenbehandlung der Trommel (Politur oder Neu-Eloxierung)

**Harken Schmiermittel-Zuordnung:**

| Stelle | Produkt | Art.-Nr. | Menge (Size 46) |
|--------|---------|----------|-----------------|
| Hauptachse | Harken White Grease | BK4520 | 5 g |
| Nadellager oben | Harken White Grease | BK4520 | 3 g |
| Nadellager unten | Harken White Grease | BK4520 | 3 g |
| Planetengetriebe | Harken White Grease | BK4520 | 8 g |
| Pawl-Springs | Harken Pawl Oil | BK4521 | 2–3 Tropfen/Feder |
| Self-Tailing Ring | KEIN Fett | — | — |
| Trommel-Innenseite | Harken White Grease (dünn) | BK4520 | 2 g |
| Befestigungsschrauben | Tef-Gel oder Duralac | — | Dünn |

**Harken Ersatzteil-Bestellnummern (häufigste):**

| Teil | Size 40 | Size 46 | Size 48 | Size 50 |
|------|---------|---------|---------|---------|
| Pawl-Spring Kit | BK4512-40 | BK4512-46 | BK4512-48 | BK4512-50 |
| Jaw-Insert Kit (Std) | BK4514-40 | BK4514-46 | BK4514-48 | BK4514-50 |
| Jaw-Insert Kit (Performa) | BK4515-40 | BK4515-46 | BK4515-48 | BK4515-50 |
| Bearing Kit (komplett) | BK4516-40 | BK4516-46 | BK4516-48 | BK4516-50 |
| O-Ring Kit | BK4518-40 | BK4518-46 | BK4518-48 | BK4518-50 |
| Service Kit (komplett) | BK4500-40 | BK4500-46 | BK4500-48 | BK4500-50 |
| Trommel (eloxiert) | — | HWC-046 | HWC-048 | HWC-050 |

#### 3.2.2 Lewmar — Wartungsvorgaben

**Quelle:** Lewmar Winch Service Guide, Edition 2023/2024

Lewmar unterteilt die Wartung in drei Stufen:

**Level 1 — Routine (monatlich bei Nutzung):**
- Süßwasser-Spülung nach Salzwasserkontakt
- Sichtprüfung Self-Tailing
- Funktionsprüfung beider Geschwindigkeitsstufen
- 2–3 Tropfen Lewmar Winch Oil (19701600) auf jede sichtbare Sperrklinke

**Level 2 — Service (saisonal, mindestens jährlich):**
- Trommel demontieren (Sicherungsring entfernen)
- Alle Sperrklinken und Federn reinigen und prüfen
- Altes Fett entfernen mit Petroleum oder White Spirit
- Neu fetten mit Lewmar Winch Grease (19701500)
- Self-Tailing-Backen prüfen, bei <50 % Profiltiefe ersetzen

**Level 3 — Major Service (alle 3–5 Jahre):**
- Komplette Demontage bis zur Basis
- Alle Verschleißteile ersetzen
- Maßkontrolle der Hauptachse (Verschleiß <0.05 mm = OK)
- Dokumentiertes Serviceprotokoll

**Lewmar Schmiermittel-Zuordnung:**

| Stelle | Produkt | Art.-Nr. | Hinweis |
|--------|---------|----------|---------|
| Alle Lager und Achsen | Lewmar Winch Grease | 19701500 | Standard-Fett |
| Getriebezähne | Lewmar Gear Grease | 19701700 | Höhere EP-Belastbarkeit |
| Sperrklinken/Federn | Lewmar Winch Oil | 19701600 | Dünnflüssiges Öl |
| Self-Tailing Ring | KEIN Schmiermittel | — | Nie fetten! |
| Bolzen, Schrauben | Tef-Gel | — | Korrosionsschutz |

**Lewmar Ersatzteil-Kits (häufigste):**

| Teil | EVO Serie | OneTouch Serie |
|------|-----------|----------------|
| Spring Kit (komplett) | 19700100 | 19700200 |
| Jaw Kit (Standard) | 19700300 | 19700400 |
| Jaw Kit (Racing) | 19700500 | 19700600 |
| Bearing Kit | 19700700 | 19700800 |
| O-Ring Kit | 19700900 | 19701000 |
| Service Kit (komplett) | 19701100 | 19701200 |
| Drum (alle Größen) | Größenabhängig | Größenabhängig |

#### 3.2.3 Andersen — Wartungsvorgaben

**Quelle:** Andersen Winch Service Manual, Version 2024

Andersen-Winschen zeichnen sich durch ihre besonders wartungsfreundliche Konstruktion aus. Das patentierte „Easy-Service"-Design ermöglicht die Demontage ohne Werkzeug (bei vielen Modellen).

**Andersen Wartungsstufen:**

**Quick Service (alle 2–3 Monate):**
- Trommel nach oben abziehen (kein Werkzeug bei Compact-Serie)
- Sperrklinken und Federn visuell inspizieren
- 1–2 Tropfen Andersen Service Oil auf jede Sperrklinke
- Trommel wieder aufsetzen, Funktionstest

**Full Service (jährlich):**
- Trommel und obere Getriebebaugruppe entfernen
- Alle Teile in Waschbenzin reinigen
- Inspektion nach Andersen-Checkliste
- Neufettung mit Andersen Service Grease (nicht mischen mit anderen!)
- Self-Tailing-Einsätze prüfen

**Major Overhaul (alle 5–7 Jahre):**
- Komplette Demontage inkl. Achse
- Ersetzen aller Federn, O-Ringe und Verschleißteile
- Prüfung auf Lochfraß oder Spaltkorrosion
- Dokumentation

**Andersen Ersatzteil-Nummern (Compact-Serie):**

| Teil | Size 28ST | Size 40ST | Size 46ST | Size 52ST |
|------|-----------|-----------|-----------|-----------|
| Spring Kit | RA101028 | RA101040 | RA101046 | RA101052 |
| Jaw Kit (Std) | RA102028 | RA102040 | RA102046 | RA102052 |
| Jaw Kit (Line) | RA103028 | RA103040 | RA103046 | RA103052 |
| Bearing Kit | RA104028 | RA104040 | RA104046 | RA104052 |
| Service Kit | RA100028 | RA100040 | RA100046 | RA100052 |
| Top Cap | RA105028 | RA105040 | RA105046 | RA105052 |

**Andersen Service Grease — Besonderheiten:**
- Calcium-Sulfonat-Komplex-Verdicker (nicht Lithium!)
- Ausgezeichnete Salzwasserbeständigkeit
- NICHT mischbar mit Lithium-basierten Fetten (Harken, Lewmar)
- Bei Wechsel: altes Fett VOLLSTÄNDIG entfernen
- Biologisch teilweise abbaubar (EAL-konform für Teilbereiche)

#### 3.2.4 Antal — Wartungsvorgaben

**Quelle:** Antal Technical Manual, Revision 2024

Antal-Winschen (italienische Fertigung) verwenden eine spezifische Konstruktion mit selbstschmierenden Delrin-Lagern in vielen Modellen.

**Antal Wartungsschema:**

**Routine (monatlich):**
- Süßwasser-Spülung
- Funktionsprüfung
- Visuelle Inspektion der Trommeloberfläche

**Standard Service (halbjährlich bei intensiver Nutzung, jährlich normal):**
- Trommel demontieren (Antal-eigenes Sicherungssystem beachten)
- Sperrklinken und Federn reinigen
- Delrin-Lager auf Verschleiß prüfen (Spiel <0.15 mm)
- Achse und Getriebe fetten mit Antal-empfohlenem Fett
- HINWEIS: Delrin-Lager NICHT fetten (selbstschmierend!)

**Major Service (alle 4–6 Jahre):**
- Komplett-Demontage
- Austausch aller Federn und O-Ringe
- Delrin-Lager prüfen — bei Verschleiß ersetzen (Lebensdauer: 8–12 Jahre)
- Metallische Lager neu fetten

**Antal Ersatzteil-Nummern (W-Serie):**

| Teil | W16ST | W28ST | W40ST | W46ST |
|------|-------|-------|-------|-------|
| Spring Kit | W16-SK | W28-SK | W40-SK | W46-SK |
| Jaw Kit | W16-JK | W28-JK | W40-JK | W46-JK |
| Delrin Bearing Set | W16-DB | W28-DB | W40-DB | W46-DB |
| Service Kit (komplett) | W16-SV | W28-SV | W40-SV | W46-SV |

### 3.3 Wartungsintervalle nach Einsatzgebiet

| Intervall | Binnenrevier (Süßwasser) | Küste (gemischt) | Hochsee (Salzwasser) | Tropen (Salz+UV) | Charterflotte |
|-----------|------------------------|-----------------|---------------------|------------------|---------------|
| Nach Einsatz | Abwischen | Süßwasser-Spülung | Süßwasser-Spülung (Pflicht) | Süßwasser-Spülung + UV-Schutz | Süßwasser-Spülung (Pflicht) |
| Monatlich | Funktionstest | Funktionstest + Ölen | Funktionstest + Ölen | Funktionstest + Ölen | Wöchentlicher Funktionstest |
| Saisonal | Quick Service | Full Service | Full Service (Frühjahr + Herbst) | Full Service (vierteljährlich) | Monatlicher Full Service |
| Jährlich | Full Service | Full Service + Messung | Generalüberholung | Generalüberholung | Halbjährliche Generalüberholung |
| 5-Jahres | Generalüberholung | Generalüberholung | Professionelle Überholung | Professionelle Überholung + Austauschprüfung | 2-Jahres-Zyklus |

### 3.4 Wartungsmatrix nach Bootsklasse

| Bootsklasse | Winschanzahl (typ.) | Jahres-Wartungsbudget | Eigenleistung möglich? | Empfehlung |
|-------------|--------------------|-----------------------|----------------------|------------|
| Daysailer (6–9 m) | 2–4 | 60–150 EUR | Ja, komplett | Jährlich selbst, 5-Jahres-Check Werft |
| Fahrtenyacht (9–14 m) | 4–8 | 150–400 EUR | Ja, bis auf E-Winschen | Halbjährlich selbst, jährlich Werft-Sichtprüfung |
| Performance Cruiser (12–18 m) | 6–12 | 300–800 EUR | Teilweise | Saisonal selbst, jährlich Werft |
| Regattayacht (10–18 m) | 8–16 | 500–1.500 EUR | Nur Basis | Monatlich selbst, saisonal Rigger/Werft |
| Blauwasseryacht (12–20 m) | 6–10 | 250–600 EUR | Ja, Pflicht (autark!) | Quartalsweise selbst, volle Ersatzteil-Bevorratung |
| Superyacht (18 m+) | 10–30 | 2.000–8.000 EUR | Crew/Werft | Crew-Wartungsplan, halbjährlich Profi-Service |

---

## 4. Schritt-für-Schritt Wartungsanleitungen

### 4.1 Benötigtes Werkzeug

#### 4.1.1 Grundwerkzeugsatz (Eigenleistung)

| Werkzeug | Spezifikation | Zweck | Ca. Preis |
|----------|---------------|-------|-----------|
| Winschkurbel-Schlüssel | Passend zum Hersteller | Sicherungsring/Schraube lösen | Oft beiliegend |
| Innensechskant-Satz | 2–8 mm, Kugelkopf | Befestigungsschrauben | 15 EUR |
| Ring-Maulschlüssel-Satz | 8–19 mm | Basis-Befestigung | 25 EUR |
| Schraubendreher | PH1, PH2, Schlitz 4+6 mm | Diverse | 15 EUR |
| Messschieber | 0–150 mm, 0.05 mm | Verschleißmessung | 20 EUR |
| Taschenlampe | LED, fokussierbar | Inspektion | 10 EUR |
| Lupe | 10x Vergrößerung | Oberflächeninspektion | 8 EUR |
| Pinzette | Gerade + gebogen | Federn, kleine Teile | 8 EUR |
| Auffangwanne | Kunststoff, flach | Teile sortieren, Fett auffangen | 5 EUR |
| Magnetschale | Edelstahl | Kleinteile sichern | 8 EUR |
| Reinigungspinsel | Verschiedene Größen | Altes Fett entfernen | 5 EUR |
| Lappen/Tücher | Fusselarm | Reinigung, Fettauftrag | 5 EUR |
| Kamera/Smartphone | — | Dokumentation (vorher/nachher) | — |

**Gesamtkosten Grundwerkzeugsatz:** ca. 125–150 EUR

#### 4.1.2 Profi-Ergänzung

| Werkzeug | Spezifikation | Zweck | Ca. Preis |
|----------|---------------|-------|-----------|
| Drehmomentschlüssel | 5–50 Nm | Befestigungsmomente | 60 EUR |
| Federwaage | 0–5 N | Pawl-Spring-Prüfung | 25 EUR |
| Messuhr mit Magnetstativ | 0.01 mm Auflösung | Axialspiel, Rundlauf | 45 EUR |
| Fühlerlehre | 0.05–1.0 mm | Lagerspiel | 12 EUR |
| Drehmoment-Bits | T10–T30 | Torx-Schrauben (Andersen) | 15 EUR |
| Ultraschallbad | 2–5 Liter | Professionelle Reinigung | 80–150 EUR |

### 4.2 Schritt-für-Schritt: 2-Speed Self-Tailing Winsch (Standard-Demontage)

Diese Anleitung gilt allgemein für 2-Gang Self-Tailing Winschen. Herstellerspezifische Abweichungen sind markiert.

#### 4.2.1 Vorbereitung

**Sicherheitshinweise:**
- Alle Schoten von der Winsch nehmen
- Winschkurbel entfernen
- Arbeitsbereich absichern (keine losen Teile über Bord!)
- Teile auf einer Matte oder in einer Wanne ablegen
- Fotos von jedem Zerlegungsschritt machen (Reihenfolge der Zusammenbau-Sicherung)
- Klebeband und Marker bereithalten zum Markieren von Positionen

**Reihenfolge der Demontage (von oben nach unten):**

```
1. Self-Tailing-Oberteil (Feeder Arm + Stripper Ring)
2. Trommel (Drum)
3. Obere Sperrklinken und Federn (Upper Pawls + Springs)
4. Oberer Spindel/Getriebebaugruppe (Upper Spindle Assembly)
5. Untere Sperrklinken und Federn (Lower Pawls + Springs)
6. Untere Getriebebaugruppe (Lower Gear Assembly)
7. Lager (Bearings)
8. Zentralachse (Main Shaft) — nur bei Generalüberholung
9. Basis (Base) — nur bei Generalüberholung
```

#### 4.2.2 Demontage — Detailschritte

**Schritt 1: Self-Tailing-Oberteil entfernen**

- Bei Harken: Feeder Arm nach oben abziehen (Schnappverschluss, leicht nach außen drücken)
- Bei Lewmar: Sicherungsring (Circlip) mit Sicherungsringzange entfernen, Oberteil abheben
- Bei Andersen: Oberteil 1/4-Drehung gegen den Uhrzeigersinn, dann nach oben abziehen
- Bei Antal: Zentralschraube lösen (SW 5 mm Innensechskant), Oberteil abnehmen

**ACHTUNG:** Self-Tailing-Backen (Jaw Inserts) können lose herausfallen. Anzahl und Position merken!

**Typische Konfiguration Self-Tailing-Backen:**

| Hersteller | Backen-Anzahl | Befestigung | Wechsel-Intervall |
|------------|---------------|-------------|-------------------|
| Harken | 2 (Standard) oder 3 (Performa) | Einrasten | 3–5 Jahre (2.000–4.000 Seemeilen) |
| Lewmar | 2 (Standard) oder 3 (OneTouch) | Schraube (T15) | 3–5 Jahre |
| Andersen | 2 (Compact) | Einrasten | 4–6 Jahre |
| Antal | 2 | Schraube (PH2) | 3–5 Jahre |

**Schritt 2: Trommel abnehmen**

- Trommel gerade nach oben abheben (bei den meisten Modellen)
- Bei einigen Modellen: obere Sicherungsmutter/-schraube lösen
  - Harken: keine Sicherung, Trommel liegt auf
  - Lewmar EVO: Circlip am oberen Achsende, mit Sicherungsringzange entfernen
  - Andersen Compact: Trommel einfach nach oben abziehen
  - Antal: Obere Scheibe/Mutter lösen (Linksgewinde bei einigen Modellen!)

**WICHTIG:** Bei der Trommel-Abnahme fallen oft die oberen Sperrklinken und Federn heraus. Arbeitsbereich vorbereiten!

**Schritt 3: Obere Sperrklinken (Upper Pawls) und Federn entfernen**

Die oberen Sperrklinken sitzen in der oberen Getriebebaugruppe oder in der Innenseite der Trommel (herstellerabhängig):

- Sperrklinken vorsichtig mit Pinzette aus ihren Sitzen nehmen
- Jede Sperrklinke hat eine zugehörige Feder — NICHT VERLIEREN!
- Anzahl der oberen Sperrklinken:

| Hersteller | Modellreihe | Obere Pawls | Federtyp |
|------------|-------------|-------------|----------|
| Harken | Plain Top / Radial | 2–3 | Drahtfeder (V-Form) |
| Harken | Performa | 3 | Drahtfeder (V-Form) |
| Lewmar | EVO | 3 | Blattfeder (flach) |
| Lewmar | OneTouch | 3 | Blattfeder (flach) |
| Andersen | Compact | 2 | Drahtfeder (Omega-Form) |
| Antal | W-Serie | 2–3 | Drahtfeder |

**Kennzeichnung:** Obere Sperrklinken und Federn in einem beschrifteten Beutel sammeln: „OBEN / UPPER".

**Schritt 4: Obere Getriebebaugruppe (Upper Spindle Assembly) entfernen**

- Die obere Getriebebaugruppe (Spindel + Zahnrad) nach oben herausziehen
- Bei Planetengetriebe: Ring-Zahnkranz sitzt in der Basis, Planetenräder auf der Spindel
- Lager (Nadellager oder Kugellager) sitzen lose oder press — NICHT mit Gewalt ziehen

**Schritt 5: Untere Sperrklinken (Lower Pawls) und Federn entfernen**

- Identisch zu Schritt 3, aber in der unteren Ebene
- Die unteren Sperrklinken sind für den 2. Gang zuständig (Untersetzung)
- In separatem, beschriftetem Beutel sammeln: „UNTEN / LOWER"

**Schritt 6: Untere Getriebebaugruppe entfernen**

- Unteres Zahnrad/Spindel herausnehmen
- Bei einigen Modellen: Sicherungsring am unteren Achsende

**Schritt 7: Lager entfernen**

- Nadellager: vorsichtig aus der Lagerschale herausheben (Magnetpinzette hilfreich)
- Kugellager: leicht herausdrücken
- ACHTUNG: Lager einzeln lagern und markieren (oben/unten, innen/außen)

**Schritt 8: Zentralachse (nur bei Generalüberholung)**

- Achse nach oben herausziehen
- Auf Riefen, Verfärbungen, Materialabtrag prüfen
- Durchmesser messen und mit Sollwert vergleichen

#### 4.2.3 Reinigung

**Reinigungsmittel:**

| Mittel | Anwendung | Einwirkzeit | Vorsicht |
|--------|-----------|-------------|----------|
| Petroleum (Shellsol D40) | Fettlösung, Allzweck | 10–30 min | Gut belüften, Handschuhe |
| White Spirit | Fettlösung, Allzweck | 10–20 min | Gut belüften, Handschuhe |
| Isopropanol (99 %) | Feinreinigung, Entfettung | 5–10 min | Schnell verdunstend |
| Aceton | NICHT für Winschen! | — | Greift Kunststoffteile an! |
| WD-40 | NUR zum Lösen festsitzender Teile | — | KEIN Schmiermittel! Danach entfetten! |
| Zitronensäure (5 %) | Kalk-/Salzentfernung | 15–30 min | Nicht auf Aluminium! |
| Essigessenz (25 %) | Salzentfernung (leicht) | 10–15 min | Nicht auf Aluminium! |

**Reinigungsvorgang:**

1. Alle Metallteile in eine Wanne mit Petroleum oder White Spirit legen
2. 15–30 Minuten einwirken lassen
3. Mit einem Pinsel altes Fett und Ablagerungen lösen
4. Teile mit einem fusselfreien Tuch abwischen
5. Bei starker Verschmutzung: Vorgang wiederholen
6. Optional: Feinreinigung mit Isopropanol (besonders Lagerflächen)
7. Alle Teile vollständig trocknen lassen (mindestens 30 Minuten an der Luft)

**ACHTUNG — Was man NICHT tun darf:**
- KEIN Aceton verwenden (greift Delrin-Lager und Kunststoffteile an)
- KEINE Drahtbürste auf Lagerflächen verwenden
- KEIN Hochdruckreiniger (Wassereinschluss in Lagern)
- KEIN Seewasser zum Spülen verwenden
- KEINE aggressiven Reiniger auf eloxierten Oberflächen

#### 4.2.4 Inspektion

**Inspektions-Checkliste (jeder Wartungsdurchgang):**

| Nr. | Prüfpunkt | Methode | Kriterium OK | Aktion bei NOK |
|-----|-----------|---------|-------------|----------------|
| 1 | Achse: Riefen/Rillen | Visuell + Fingernagel | Glatte Oberfläche, kein Haken | Leicht: Polieren (1200er Papier). Stark: Austausch |
| 2 | Achse: Durchmesser | Messschieber | Innerhalb Toleranz (±0.05 mm) | Austausch |
| 3 | Lager: Spiel | Fühlerlehre | <0.1 mm Radialspiel | Austausch |
| 4 | Lager: Oberfläche | Visuell (Lupe) | Kein Pitting, keine Verfärbung | Austausch |
| 5 | Sperrklinken: Kanten | Visuell (Lupe) | Scharfe Kanten, kein Rundschliff | Austausch bei sichtbarer Abrundung |
| 6 | Sperrklinken: Drehpunkt | Manuell | Leichtgängig, kein Spiel | Reinigen oder austauschen |
| 7 | Zahnkranz: Flanken | Visuell (Lupe) | Kein Materialabtrag, keine Riefen | Leicht: Weiternutzen. Stark: Austausch |
| 8 | Pawl-Springs: Federkraft | Federwaage oder Vergleich | >80 % der Nennkraft | Austausch (immer satzweise!) |
| 9 | Pawl-Springs: Form | Visuell | Originalform, kein Knicken | Austausch |
| 10 | O-Ringe: Zustand | Visuell + Drucktest | Elastisch, keine Risse, nicht verhärtet | Austausch |
| 11 | Self-Tailing: Profiltiefe | Messschieber | >1.5 mm Profiltiefe | Austausch bei <1.0 mm |
| 12 | Self-Tailing: Material | Visuell | Kein Ausbruch, keine Verformung | Austausch |
| 13 | Trommel: Oberfläche | Visuell | Gleichmäßige Eloxierung, kein Pitting | Leicht: Polieren. Stark: Neu-Eloxierung |
| 14 | Trommel: Rillen | Messschieber | Originaltiefe | Austausch bei starkem Abrieb |
| 15 | Basis: Korrosion | Visuell | Keine Verfärbung, kein Lochfraß | Reinigen/Konservieren. Schwer: Austausch |
| 16 | Schrauben: Gewinde | Manuell (Eindrehen) | Leichtgängig, kein Ausreißen | Gewinde nachschneiden oder Heli-Coil |
| 17 | Getriebezähne: Flanken | Visuell (Lupe) | Kein Pitting, gleichmäßig | Austausch bei sichtbarem Verschleiß |

#### 4.2.5 Schmierung und Zusammenbau

**Schmierstellen und -mengen (Beispiel: 2-Gang Self-Tailing, Size 40–48):**

```
                    ┌─────────────────────┐
                    │  Self-Tailing Ring   │ ← KEIN Fett!
                    │  (Jaw Inserts)       │
                    ├─────────────────────┤
                    │  Trommel             │ ← Innenseite: dünne Fettschicht
                    │                     │
                    ├──●──────────────●───┤
                    │  ▲ Obere Pawls ▲   │ ← NUR Öl (2-3 Tropfen/Feder)
                    ├─────────────────────┤
                    │  Oberes Lager       │ ← Fett: 3–5 g
                    ├─────────────────────┤
                    │  Planetengetriebe   │ ← Fett: 5–8 g (Zahnflanken)
                    ├──●──────────────●───┤
                    │  ▲ Untere Pawls ▲  │ ← NUR Öl (2-3 Tropfen/Feder)
                    ├─────────────────────┤
                    │  Unteres Lager      │ ← Fett: 3–5 g
                    ├─────────────────────┤
                    │  ◎ Achse            │ ← Fett: dünner Film
                    ├─────────────────────┤
                    │  Basis              │ ← Fett: dünn auf Kontaktflächen
                    └─────────────────────┘
```

**Zusammenbau — Schritt für Schritt:**

1. **Achse fetten:** Dünnen Film Winschfett auf die gesamte Achsenoberfläche auftragen
2. **Unteres Lager einsetzen:** Lager mit Fett füllen (Fett zwischen Nadeln/Kugeln drücken), in Position setzen
3. **Untere Getriebebaugruppe:** Zahnflanken dünn einfetten, auf Achse setzen
4. **Untere Sperrklinken + Federn:** Federn in die Sperrklinken einsetzen, Sperrklinken in ihre Sitze drücken. 2–3 Tropfen Öl auf jede Feder. Sperrklinken müssen FREI schwingen!
5. **Oberes Lager einsetzen:** Wie unteres Lager
6. **Obere Getriebebaugruppe:** Wie untere
7. **Obere Sperrklinken + Federn:** Wie Schritt 4
8. **Trommel aufsetzen:** Innenseite dünn einfetten, Trommel gerade auf die Baugruppe setzen, leicht drehen bis sie einrastet
9. **Sicherung:** Circlip, Mutter oder Schnappverschluss anbringen (herstellerabhängig)
10. **Self-Tailing-Oberteil:** Jaw-Inserts einsetzen, Oberteil aufsetzen und sichern

**KRITISCHE PRÜFUNG nach Zusammenbau:**

| Test | Erwartung | Problem wenn nicht erfüllt |
|------|-----------|--------------------------|
| Trommel im Uhrzeigersinn drehen | Leichtgängig, gleichmäßig | Lager klemmt, Teile falsch eingesetzt |
| Trommel gegen Uhrzeigersinn drehen | Gesperrt (Klick-Klick) | Sperrklinken falsch eingesetzt oder Federn fehlen |
| 1. Gang (schnell drehen) | Leichtgängig, Sperrklinken klicken | Obere Sperrklinken-Problem |
| 2. Gang (langsam drehen) | Deutlicher Widerstand durch Untersetzung | Untere Sperrklinken oder Getriebe-Problem |
| Self-Tailing mit Schot | Schot wird sicher gehalten | Jaw-Inserts falsch, verschlissen oder fehlend |
| Rücklauf unter Last | Kein Durchrutschen | Sperrklinken greifen nicht — SOFORT demontieren! |

#### 4.2.6 Drehmomente für Befestigungsschrauben

| Hersteller | Schraube | Material | Gewinde | Drehmoment (Nm) |
|------------|----------|----------|---------|-----------------|
| Harken | Basis-Befestigung | Edelstahl A4 | M8 | 18–22 |
| Harken | Basis-Befestigung | Edelstahl A4 | M10 | 30–35 |
| Lewmar | Basis-Befestigung (Standardmontage) | Edelstahl A4 | M8 | 16–20 |
| Lewmar | Basis-Befestigung (Standardmontage) | Edelstahl A4 | M10 | 28–32 |
| Andersen | Basis-Befestigung | Edelstahl A4 | M8 | 18–22 |
| Antal | Basis-Befestigung | Edelstahl A4 | M8 | 15–20 |
| Alle | Self-Tailing Deckelmutter | Edelstahl A4 | M6 | 8–10 |
| Alle | Jaw-Insert-Schraube | Edelstahl A4 | M4 | 2–3 |

**IMMER:** Tef-Gel oder Duralac auf Befestigungsschrauben auftragen (Korrosionsschutz und Festfressen verhindern).

#### 4.2.7 Häufige Fehler bei der Wartung

| Fehler | Folge | Vermeidung |
|--------|-------|-----------|
| Sperrklinken vertauscht (oben/unten) | Gänge funktionieren nicht korrekt | Teile beim Zerlegen beschriften |
| Federn vergessen | Sperrklinken greifen nicht → Winsch rutscht durch! | Systematisch arbeiten, Checkliste |
| Zu viel Fett auf Sperrklinken | Sperrklinken kleben, greifen verzögert | NUR Öl auf Sperrklinken und Federn! |
| Fett auf Self-Tailing-Ring | Schot rutscht durch | Self-Tailing-Bereich IMMER fettfrei! |
| WD-40 als Schmiermittel | Verdünnt vorhandenes Fett, trocknet aus | WD-40 NUR zum Lösen, danach entfetten und richtig fetten |
| Aceton zur Reinigung | Greift Delrin-Lager, Kunststoffteile an | Petroleum oder White Spirit verwenden |
| Mischung verschiedener Fette | Ggf. chemische Unverträglichkeit, Verflüssigung | IMMER altes Fett komplett entfernen vor Neufettung |
| Trommel schief aufgesetzt | Beschädigung der Lager, Klemmen | Trommel gerade und vorsichtig aufsetzen |
| Befestigungsschrauben ohne Gleitmittel | Festfressen im Gewinde, galvanische Korrosion | Tef-Gel oder Duralac verwenden |
| Zu hohes Drehmoment | Gewindeausriss, Deck-Verformung | Drehmomentschlüssel verwenden |

---

## 5. Schmiermittel und Reinigungsmittel

### 5.1 Vollständiger Schmiermittel-Guide

#### 5.1.1 Winsch-spezifische Schmierfette

**Harken White Grease (BK4520)**
- Typ: Lithium-Komplex + PTFE, PAO-Synthese
- NLGI: 1–2
- Farbe: Weiß
- Tropfpunkt: >200 °C
- Temperaturbereich: –30 bis +150 °C
- Wasserbeständigkeit: Ausgezeichnet (ASTM D1264: <3 %)
- Gebindegrößen: 28 g Tube (BK4520), 100 g Dose (BK4520-100)
- Anwendung: Alle Harken-Winschen (Lager, Achsen, Getriebe)
- Verträglichkeit: Mischbar mit anderen Lithium-Fetten (nicht empfohlen)
- Preis: ca. 18 EUR / 100 g

**Lewmar Winch Grease (19701500)**
- Typ: Lithium-Verdicker, Mineral/Synthese-Blend
- NLGI: 2
- Farbe: Bernstein/Gelb
- Tropfpunkt: >180 °C
- Temperaturbereich: –20 bis +130 °C
- Wasserbeständigkeit: Gut
- Gebindegrößen: 75 ml Tube (19701500), 250 ml Dose (19701501)
- Anwendung: Alle Lewmar-Winschen (Lager, Achsen, Getriebe)
- Verträglichkeit: Lithium-basiert, mischbar mit Harken White Grease (nicht empfohlen)
- Preis: ca. 12 EUR / 100 g

**Lewmar Gear Grease (19701700)**
- Typ: EP-Fett, Lithium-Komplex, hohe Druckbelastbarkeit
- NLGI: 2
- Farbe: Dunkelbraun
- Tropfpunkt: >200 °C
- Temperaturbereich: –25 bis +140 °C
- Anwendung: NUR für Getriebezähne (Planetengetriebe, Schneckengetriebe)
- NICHT für Lager oder Achsen verwenden!
- Preis: ca. 15 EUR / 75 ml

**Andersen Service Grease**
- Typ: Calcium-Sulfonat-Komplex + PTFE, PAO-Synthese
- NLGI: 1–2
- Farbe: Weiß
- Tropfpunkt: >220 °C
- Temperaturbereich: –35 bis +160 °C
- Wasserbeständigkeit: Hervorragend (bestes Winschfett im Test)
- Anwendung: Alle Andersen-Winschen
- **ACHTUNG: NICHT mit Lithium-Fetten mischen!** Calcium-Sulfonat und Lithium sind NICHT kompatibel
- Preis: ca. 22 EUR / 100 g

**Winch-Mate (Standard)**
- Typ: Lithium, Mineralöl
- NLGI: 2
- Farbe: Bernstein/Gelb
- Tropfpunkt: >170 °C
- Temperaturbereich: –15 bis +120 °C
- Wasserbeständigkeit: Befriedigend
- Anwendung: Budget-Option, alle Winschen
- Einschränkung: Geringere Salzwasserbeständigkeit, kein PTFE, keine EP-Additive
- Preis: ca. 9 EUR / 100 g

#### 5.1.2 Winsch-Öle

**Harken Pawl Oil (BK4521)**
- Typ: Synthetisches Maschinenöl, leicht
- Viskosität: ISO VG 32
- Farbe: Klar/Leicht gelblich
- Anwendung: Sperrklinken-Federn, Sperrklinken-Drehpunkte, feine Mechanik
- Gebinde: 14 ml Fläschchen mit Dosierspitze
- NICHT für Lager oder Getriebe verwenden (zu dünn!)
- Preis: ca. 12 EUR / 14 ml

**Lewmar Winch Oil (19701600)**
- Typ: Mineralöl, mittel
- Viskosität: ISO VG 46
- Farbe: Bernstein
- Anwendung: Sperrklinken, Federn, feinmechanische Teile
- Gebinde: 55 ml Flasche mit Dosierspitze
- Preis: ca. 10 EUR / 55 ml

**McLube OneDrop Ball Bearing Conditioner (1600)**
- Typ: Synthetisches Öl + PTFE-Zusatz
- Viskosität: ISO VG 22
- Farbe: Klar
- Anwendung: Universal-Winschöl, auch für Blöcke und Schäkel
- Gebinde: 30 ml Flasche mit Nadel-Dosierspitze
- Exzellent für Regattawinschen (minimale Reibung)
- Preis: ca. 18 EUR / 30 ml

**Ballistol Universal (21000)**
- Typ: Medizinisches Weißöl, biologisch abbaubar
- Viskosität: ISO VG 68
- Farbe: Klar/Leicht gelblich
- Anwendung: Notlösung für Sperrklinken, Übergangsschmierung
- NICHT als Dauerschmierung geeignet (zu schnell ausgewaschen)
- Preis: ca. 8 EUR / 200 ml

#### 5.1.3 Universelle Alternativen (wenn Hersteller-Fett nicht verfügbar)

| Universalfett | Verdicker | Verträglichkeit mit | Eignung |
|---------------|-----------|-------------------|---------|
| Mobilgrease XHP 222 | Lithium-Komplex | Harken, Lewmar, Antal | Gut |
| SKF LGMT 2 | Lithium | Harken, Lewmar, Antal | Befriedigend |
| Klüber Isoflex NBU 15 | Barium-Komplex | Alle (nach Altreinigung) | Sehr gut (aber teuer) |
| Interflon Fin Grease MP | Lithium + MicPol | Harken, Lewmar, Antal | Gut |
| Total Multis EP 2 | Lithium | Harken, Lewmar, Antal | Befriedigend |

**WARNUNG:** Bei Verwendung von Universalfetten:
1. Altes Fett IMMER vollständig entfernen
2. Verträglichkeit prüfen (Lithium NICHT mit Calcium-Sulfonat = Andersen!)
3. Kein Fett mit MoS₂ (Molybdändisulfid) in Winschen verwenden — greift Buntmetalle an

### 5.2 Was man NIEMALS verwenden darf

| Produkt | Warum NICHT | Was stattdessen |
|---------|------------|-----------------|
| WD-40 (als Schmiermittel) | Verdünnt Fett, trocknet Federn aus, zieht Schmutz an | Herstelleröl für Federn, Herstellerfett für Lager |
| Vaseline | Wird unter Last zu dünn, kein EP-Schutz | Winschfett |
| Motoröl | Zu dünn, kein Haftvermögen, läuft aus | Winschöl (nur für Sperrklinken) |
| Getriebeöl (Kfz) | Enthält Additive die Buntmetalle angreifen können | Winschfett |
| Kupferpaste | Leitet elektrisch, fördert galvanische Korrosion | Tef-Gel für Schrauben |
| Graphitfett | Graphit ist leitfähig, fördert galvanische Korrosion | PTFE-Fett |
| Silikonfett | Kein EP-Schutz, kriecht auf alle Oberflächen | Winschfett |
| Kettenspray (Motorrad) | Enthält aggressive Lösungsmittel, falscher Grundöl-Typ | Winschfett |
| MoS₂-Fett | Greift Bronze und Aluminium an | PTFE-Fett |
| Sprühöl generisch | Zu dünn, trocknet aus, kein Dauerschutz | Herstellerfett + Herstelleröl |

### 5.3 Schmiermittel-Verträglichkeitsmatrix

**Verdicker-Verträglichkeit (Mischbarkeit):**

| | Lithium | Li-Komplex | Calcium | Ca-Sulfonat | Barium | PTFE (Non-Soap) |
|---|---------|-----------|---------|-------------|--------|-----------------|
| **Lithium** | ✓ | ✓ | ⚠ | ✗ | ✗ | ✓ |
| **Li-Komplex** | ✓ | ✓ | ⚠ | ✗ | ⚠ | ✓ |
| **Calcium** | ⚠ | ⚠ | ✓ | ⚠ | ✗ | ✓ |
| **Ca-Sulfonat** | ✗ | ✗ | ⚠ | ✓ | ⚠ | ✓ |
| **Barium** | ✗ | ⚠ | ✗ | ⚠ | ✓ | ✓ |
| **PTFE (Non-Soap)** | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

✓ = Verträglich, ⚠ = Begrenzt verträglich (kurzfristig OK), ✗ = NICHT verträglich (Verflüssigung, Trennung)

**Praktische Konsequenz für Hersteller-Wechsel:**

| Von → Nach | Verträglichkeit | Maßnahme |
|-----------|-----------------|----------|
| Harken → Lewmar | ✓ (beide Lithium-basiert) | Altes Fett entfernen empfohlen |
| Harken → Andersen | ✗ | Altes Fett VOLLSTÄNDIG entfernen (Pflicht!) |
| Lewmar → Andersen | ✗ | Altes Fett VOLLSTÄNDIG entfernen (Pflicht!) |
| Andersen → Harken | ✗ | Altes Fett VOLLSTÄNDIG entfernen (Pflicht!) |
| Andersen → Lewmar | ✗ | Altes Fett VOLLSTÄNDIG entfernen (Pflicht!) |
| Antal → Harken | ✓ | Altes Fett entfernen empfohlen |
| Antal → Lewmar | ✓ | Altes Fett entfernen empfohlen |

### 5.4 Reinigungsmittel im Detail

#### 5.4.1 Empfohlene Reinigungsmittel

| Produkt | Typ | Anwendung | Einwirkzeit | Verträglichkeit | Preis |
|---------|-----|-----------|-------------|-----------------|-------|
| Shell Shellsol D40 | Petroleum-Destillat | Fettlösung, Standard-Reiniger | 10–30 min | Alle Materialien | 8 EUR / L |
| White Spirit (Testbenzin) | Kohlenwasserstoff | Fettlösung, Standard-Reiniger | 10–20 min | Alle Materialien | 5 EUR / L |
| Isopropanol 99 % | Alkohol | Feinreinigung, Entfettung | 5–10 min | Alle Materialien | 6 EUR / L |
| Star brite Winch Cleaner | Spezialreiniger | Winsch-Komplettreinigung | 5–15 min | Winsch-optimiert | 15 EUR / 500 ml |
| Harken Winch Cleaner (BK4522) | Spezialreiniger | Fettlösung, Korrosionsschutz | 5–15 min | Winsch-optimiert | 18 EUR / 500 ml |
| Simple Green Marine | Biologisch abbaubar | Leichte Reinigung, Salzentfernung | 5–10 min | Alle Materialien | 12 EUR / L |

#### 5.4.2 Reinigungsmittel für spezifische Probleme

| Problem | Mittel | Konzentration | Anwendung | Vorsicht |
|---------|--------|---------------|-----------|----------|
| Salzablagerungen | Süßwasser + Essig | 10 % Essig | Einweichen 15 min, abbürsten | Nicht auf Aluminium |
| Verhärtetes Fett | Petroleum | Pur | Einweichen 30–60 min | Belüftung |
| Korrosionsprodukte (leicht) | Phosphorsäure (verdünnt) | 5–10 % | Auftragen, 5 min, abspülen | Handschuhe, Brille |
| Korrosionsprodukte (stark) | Naval Jelly / Fertan | Gebrauchsfertig | Auftragen, einwirken lassen | Nur auf Edelstahl |
| Kalkablagerungen | Zitronensäure | 5–10 % | Einweichen 15–30 min | Nicht auf Aluminium! |
| Ölfilm auf Trommel | Isopropanol | Pur | Abwischen | Schnell trocknen lassen |
| Grünspan (Bronze) | Essig + Salz | Paste | Auftragen, polieren | Danach gründlich spülen |

### 5.5 Schmiermittel-Lagerung

| Aspekt | Empfehlung |
|--------|-----------|
| Lagertemperatur | 5–30 °C (nie unter 0 °C, nie über 40 °C) |
| Lichtschutz | Dunkel lagern (UV-Degradation) |
| Haltbarkeit (ungeöffnet) | 3–5 Jahre (Herstellerfette), 2–3 Jahre (Universalfette) |
| Haltbarkeit (geöffnet) | 1–2 Jahre (Tube), 6–12 Monate (Dose) |
| Feuchtigkeit | Trocken lagern, Dose nach Gebrauch fest verschließen |
| An Bord | In verschließbarer Box, stehend, gegen Auslaufen gesichert |
| Kennzeichnung | Kaufdatum auf Gebinde notieren |
| Entsorgung | Als Sondermüll entsorgen (nicht ins Wasser!) |

---

## 6. Verschleißteile und Ersatzteilplanung

### 6.1 Verschleißteil-Übersicht nach Lebensdauer

| Bauteil | Lebensdauer (gewartet) | Lebensdauer (ungewartet) | Anzeichen für Verschleiß | Austausch-Schwierigkeit |
|---------|----------------------|------------------------|--------------------------|----------------------|
| Pawl-Springs (Sperrklinkenfedern) | 3–5 Jahre | 1–3 Jahre | Sperrklinken greifen verzögert, leises Klicken | Einfach (15 min) |
| Jaw-Inserts (Self-Tailing-Backen) | 5–8 Jahre | 2–5 Jahre | Schot rutscht, Profiltiefe <1.0 mm | Einfach (10 min) |
| O-Ringe / Dichtungen | 3–5 Jahre | 1–2 Jahre | Verhärtet, rissig, undicht | Einfach (5 min) |
| Nadellager | 10–15 Jahre | 3–7 Jahre | Erhöhtes Spiel, Knirschen, Pitting | Mittel (30 min) |
| Kugellager | 10–15 Jahre | 3–7 Jahre | Rauheit beim Drehen, Spiel | Mittel (30 min) |
| Delrin-Buchsen | 8–12 Jahre | 4–8 Jahre | Radialspiel >0.2 mm | Mittel (30 min) |
| Sperrklinken (Pawls) | 8–15 Jahre | 3–8 Jahre | Abgerundete Kanten, Greifverzögerung | Einfach (15 min) |
| Zahnkranz (Ratchet) | 15–25 Jahre | 5–12 Jahre | Sichtbarer Flankenabrieb | Schwer (Basis-Demontage) |
| Getriebezähne | 20–30 Jahre | 8–15 Jahre | Pitting auf Zahnflanken | Schwer (Komplett-Demontage) |
| Zentralachse | 20–35 Jahre | 8–15 Jahre | Riefen >0.1 mm Tiefe | Schwer (Komplett-Demontage) |
| Feeder Arm Spring | 5–8 Jahre | 3–5 Jahre | Self-Tailing greift nicht, Feeder lose | Einfach (10 min) |
| Circlip / Sicherungsring | 10–20 Jahre | 5–10 Jahre | Ausgeweitet, kein sicherer Sitz | Einfach (5 min) |

### 6.2 Harken — Detaillierte Ersatzteilliste

#### 6.2.1 Harken Radial Serie (Aktuelle Produktion)

**Pawl-Spring Kits (Sperrklinkenfedern-Satz):**

| Winschgröße | Art.-Nr. | Inhalt | Preis (ca.) |
|-------------|----------|--------|-------------|
| Size 15 | BK4512-15 | 4 Federn (2 oben, 2 unten) | 12 EUR |
| Size 20 | BK4512-20 | 4 Federn | 14 EUR |
| Size 35 | BK4512-35 | 6 Federn (3+3) | 18 EUR |
| Size 40 | BK4512-40 | 6 Federn | 20 EUR |
| Size 46 | BK4512-46 | 6 Federn | 22 EUR |
| Size 48 | BK4512-48 | 6 Federn | 22 EUR |
| Size 50 | BK4512-50 | 8 Federn (4+4) | 28 EUR |
| Size 60 | BK4512-60 | 8 Federn | 32 EUR |
| Size 70 | BK4512-70 | 10 Federn (5+5) | 38 EUR |
| Size 80 | BK4512-80 | 10 Federn | 42 EUR |

**Jaw-Insert Kits (Self-Tailing-Backen):**

| Winschgröße | Standard (Art.-Nr.) | Performa (Art.-Nr.) | Preis Std/Perf |
|-------------|--------------------|--------------------|----------------|
| Size 35 | BK4514-35 | BK4515-35 | 28/35 EUR |
| Size 40 | BK4514-40 | BK4515-40 | 32/42 EUR |
| Size 46 | BK4514-46 | BK4515-46 | 38/48 EUR |
| Size 48 | BK4514-48 | BK4515-48 | 38/48 EUR |
| Size 50 | BK4514-50 | BK4515-50 | 42/55 EUR |
| Size 60 | BK4514-60 | BK4515-60 | 48/62 EUR |
| Size 70 | BK4514-70 | BK4515-70 | 55/72 EUR |

**Bearing Kits (Lagersätze):**

| Winschgröße | Art.-Nr. | Inhalt | Preis (ca.) |
|-------------|----------|--------|-------------|
| Size 35 | BK4516-35 | 2 Nadellager + Scheiben | 45 EUR |
| Size 40 | BK4516-40 | 2 Nadellager + Scheiben | 52 EUR |
| Size 46 | BK4516-46 | 2 Nadellager + Scheiben | 58 EUR |
| Size 48 | BK4516-48 | 2 Nadellager + Scheiben | 58 EUR |
| Size 50 | BK4516-50 | 2 Nadellager + Kugellager + Scheiben | 72 EUR |
| Size 60 | BK4516-60 | 3 Lager + Scheiben | 85 EUR |
| Size 70 | BK4516-70 | 3 Lager + Scheiben | 98 EUR |

**O-Ring Kits:**

| Winschgröße | Art.-Nr. | Inhalt | Preis (ca.) |
|-------------|----------|--------|-------------|
| Size 35–48 | BK4518-M | 4 O-Ringe (NBR 70 Shore) | 8 EUR |
| Size 50–70 | BK4518-L | 6 O-Ringe (NBR 70 Shore) | 12 EUR |
| Size 80+ | BK4518-XL | 8 O-Ringe (NBR 70 Shore) | 16 EUR |

**Komplett-Service-Kits (empfohlen für 5-Jahres-Überholung):**

| Winschgröße | Art.-Nr. | Inhalt | Preis (ca.) |
|-------------|----------|--------|-------------|
| Size 40 | BK4500-40 | Springs + Jaws + Bearings + O-Rings + Grease | 110 EUR |
| Size 46 | BK4500-46 | Wie oben | 125 EUR |
| Size 48 | BK4500-48 | Wie oben | 125 EUR |
| Size 50 | BK4500-50 | Wie oben | 145 EUR |

### 6.3 Lewmar — Detaillierte Ersatzteilliste

#### 6.3.1 Lewmar EVO Serie

**Spring Kits:**

| Winschgröße | Art.-Nr. | Inhalt | Preis (ca.) |
|-------------|----------|--------|-------------|
| EVO 15 | 19700101 | 4 Blattfedern | 10 EUR |
| EVO 30 | 19700102 | 6 Blattfedern | 15 EUR |
| EVO 40 | 19700103 | 6 Blattfedern | 18 EUR |
| EVO 45 | 19700104 | 6 Blattfedern | 20 EUR |
| EVO 50 | 19700105 | 8 Blattfedern | 25 EUR |
| EVO 55 | 19700106 | 8 Blattfedern | 28 EUR |
| EVO 65 | 19700107 | 10 Blattfedern | 32 EUR |

**Jaw Kits:**

| Winschgröße | Standard (Art.-Nr.) | Racing (Art.-Nr.) | Preis Std/Racing |
|-------------|--------------------|--------------------|------------------|
| EVO 30 | 19700301 | 19700501 | 22/35 EUR |
| EVO 40 | 19700302 | 19700502 | 28/42 EUR |
| EVO 45 | 19700303 | 19700503 | 32/45 EUR |
| EVO 50 | 19700304 | 19700504 | 38/52 EUR |
| EVO 55 | 19700305 | 19700505 | 42/58 EUR |
| EVO 65 | 19700306 | 19700506 | 48/65 EUR |

**Bearing Kits:**

| Winschgröße | Art.-Nr. | Inhalt | Preis (ca.) |
|-------------|----------|--------|-------------|
| EVO 15–30 | 19700701 | 2 Nadellager | 35 EUR |
| EVO 40–45 | 19700702 | 2 Nadellager + Scheiben | 48 EUR |
| EVO 50–55 | 19700703 | 2 Nadellager + 1 Kugellager | 62 EUR |
| EVO 65 | 19700704 | 3 Lager | 78 EUR |

#### 6.3.2 Lewmar OneTouch Serie

| Teil | OneTouch 30 | OneTouch 40 | OneTouch 48 |
|------|-------------|-------------|-------------|
| Spring Kit | 19700201 | 19700202 | 19700203 |
| Jaw Kit (Std) | 19700401 | 19700402 | 19700403 |
| Jaw Kit (Racing) | 19700601 | 19700602 | 19700603 |
| Bearing Kit | 19700801 | 19700802 | 19700803 |
| O-Ring Kit | 19701001 | 19701002 | 19701003 |
| Service Kit | 19701201 | 19701202 | 19701203 |

### 6.4 Andersen — Detaillierte Ersatzteilliste

#### 6.4.1 Andersen Compact Serie

**Spring Kits:**

| Winschgröße | Art.-Nr. | Inhalt | Material | Preis (ca.) |
|-------------|----------|--------|----------|-------------|
| Size 28ST | RA101028 | 4 Omega-Federn | Edelstahl 316 | 15 EUR |
| Size 34ST | RA101034 | 4 Omega-Federn | Edelstahl 316 | 18 EUR |
| Size 40ST | RA101040 | 6 Omega-Federn | Edelstahl 316 | 22 EUR |
| Size 46ST | RA101046 | 6 Omega-Federn | Edelstahl 316 | 25 EUR |
| Size 52ST | RA101052 | 8 Omega-Federn | Edelstahl 316 | 30 EUR |
| Size 58ST | RA101058 | 8 Omega-Federn | Edelstahl 316 | 35 EUR |
| Size 68ST | RA101068 | 10 Omega-Federn | Edelstahl 316 | 40 EUR |

**Jaw Kits:**

| Winschgröße | Standard (Art.-Nr.) | Line-Grip (Art.-Nr.) | Preis Std/Line |
|-------------|--------------------|--------------------|----------------|
| Size 28ST | RA102028 | RA103028 | 20/30 EUR |
| Size 40ST | RA102040 | RA103040 | 30/42 EUR |
| Size 46ST | RA102046 | RA103046 | 35/48 EUR |
| Size 52ST | RA102052 | RA103052 | 40/55 EUR |
| Size 58ST | RA102058 | RA103058 | 45/60 EUR |
| Size 68ST | RA102068 | RA103068 | 50/68 EUR |

**Service Kits (komplett):**

| Winschgröße | Art.-Nr. | Inhalt | Preis (ca.) |
|-------------|----------|--------|-------------|
| Size 28ST | RA100028 | Springs + Jaws + Bearings + Grease | 85 EUR |
| Size 40ST | RA100040 | Wie oben | 105 EUR |
| Size 46ST | RA100046 | Wie oben | 120 EUR |
| Size 52ST | RA100052 | Wie oben | 140 EUR |

### 6.5 Antal — Detaillierte Ersatzteilliste

#### 6.5.1 Antal W-Serie

| Teil | W16ST | W20ST | W28ST | W40ST | W46ST |
|------|-------|-------|-------|-------|-------|
| Spring Kit | W16-SK | W20-SK | W28-SK | W40-SK | W46-SK |
| Jaw Kit | W16-JK | W20-JK | W28-JK | W40-JK | W46-JK |
| Delrin Bearing Set | W16-DB | W20-DB | W28-DB | W40-DB | W46-DB |
| O-Ring Kit | W16-OR | W20-OR | W28-OR | W40-OR | W46-OR |
| Service Kit | W16-SV | W20-SV | W28-SV | W40-SV | W46-SV |
| Pawl Set | W16-PW | W20-PW | W28-PW | W40-PW | W46-PW |

**Preise (Antal W-Serie, ca.):**

| Teil | Size 16–20 | Size 28 | Size 40 | Size 46 |
|------|-----------|---------|---------|---------|
| Spring Kit | 10 EUR | 14 EUR | 18 EUR | 22 EUR |
| Jaw Kit | 18 EUR | 25 EUR | 32 EUR | 38 EUR |
| Delrin Bearing Set | 25 EUR | 35 EUR | 45 EUR | 55 EUR |
| O-Ring Kit | 6 EUR | 8 EUR | 10 EUR | 12 EUR |
| Service Kit | 65 EUR | 85 EUR | 105 EUR | 125 EUR |
| Pawl Set | 22 EUR | 30 EUR | 40 EUR | 50 EUR |

### 6.6 Ersatzteil-Bevorratungsempfehlung

#### 6.6.1 Mindest-Bordbestand (Fahrtenboot)

| Teil | Menge | Begründung |
|------|-------|-----------|
| Pawl-Spring Kit (für größte Winsch) | 2 Sätze | Häufigster Verschleiß, kritisch für Funktion |
| Jaw-Insert Kit (für Hauptwinschen) | 1 Satz | Wenn Schot rutscht, ist Segeln eingeschränkt |
| O-Ring-Sortiment (passend) | 1 Satz | Kleine Teile, große Wirkung |
| Herstellerfett (Tube) | 1 Tube | Für Zwischenwartung |
| Herstelleröl (Fläschchen) | 1 Fläschchen | Für Sperrklinken-Nachschmierung |
| Circlip / Sicherungsring (passend) | 2 Stück | Falls einer beim Demontieren verformt wird |

**Geschätzte Kosten Bordbestand:** 80–150 EUR (je nach Hersteller und Winschgröße)

#### 6.6.2 Blauwasser-Bordbestand (Langfahrt)

| Teil | Menge | Begründung |
|------|-------|-----------|
| Komplett-Service-Kit (für jede Winschgröße) | Je 1 | Autarke Wartung über mehrere Saisons |
| Pawl-Spring Kit (für jede Winschgröße) | Je 2 | Doppelte Reserve |
| Jaw-Insert Kit (alle Winschen) | Je 1 | Vollständige Abdeckung |
| Bearing Kit (für größte Winsch) | 1 | Für den Notfall |
| Herstellerfett | 2 Tuben/Dosen | Für mehrere Wartungsdurchgänge |
| Herstelleröl | 2 Fläschchen | Reserve |
| Circlips (sortiert) | 10 Stück | Reserve |
| Ersatz-Pawls (für größte Winsch) | 1 Satz | Bei schwerem Verschleiß |
| Delrin-Buchsen (wenn Antal) | 1 Satz | Spezifisch für Antal |
| Tef-Gel (Tube) | 1 | Für Befestigungsschrauben |

**Geschätzte Kosten Blauwasser-Bestand:** 350–600 EUR (je nach Hersteller und Anzahl Winschen)

### 6.7 Verschleißerkennung und Austauschkriterien

| Bauteil | Messpunkt | Neuzustand | Austauschgrenze | Messmethode |
|---------|-----------|-----------|-----------------|-------------|
| Jaw-Insert Profiltiefe | Tiefste Stelle des Profils | 3.0–4.0 mm | <1.0 mm | Messschieber, Tiefenmesser |
| Pawl-Spring Federkraft | Auslenkung bei Nennkraft | 100 % (Referenz) | <60 % | Federwaage, Vergleich mit Neuteil |
| Nadellager Radialspiel | Am äußeren Lagerring | 0.02–0.05 mm | >0.15 mm | Fühlerlehre |
| Achse Durchmesser | An Lagerstelle | Sollwert ±0.02 mm | Sollwert –0.10 mm | Messschieber, Mikrometer |
| Pawl Kantenschärfe | Greifkante | Scharfkantig | Sichtbare Abrundung >0.3 mm | Lupe 10x, Fingernagel-Test |
| Zahnkranz Flankenbreite | Breiteste Stelle | Sollwert ±0.05 mm | Sollwert –0.3 mm | Messschieber |
| O-Ring Querschnitt | Schnurstärke | Kreisrund, elastisch | Abgeflacht, hart, rissig | Visuell + Drucktest |

---

## 7. Anlagen-spezifische Zuordnung

### 7.1 Winschen nach Anwendungsbereich

#### 7.1.1 Großschot-Winschen (Main Sheet Winches)

**Besondere Wartungsanforderungen:**
- Höchste Belastung aller Winschen an Bord
- Häufiges Fieren und Dichtholen unter Last → erhöhter Pawl-Verschleiß
- Oft elektrisch → zusätzliche E-Wartung (siehe 09_06)
- Schmutzanfälligkeit durch Position im Cockpit (Spritzwasser, UV)

**Wartungsintervall:** Doppelt so häufig wie Standardwinschen
**Empfohlene Schmiermenge:** 30 % mehr als Standard
**Typische Problemzonen:** Unteres Lager (höchste Last), Pawl-Springs (häufiger Lastwechsel)

**Typische Winschgrößen nach Bootslänge:**

| Bootslänge | Winschgröße (manuell) | Winschgröße (elektrisch) |
|------------|----------------------|-------------------------|
| 8–10 m | Size 30–40 | — |
| 10–12 m | Size 40–46 | Size 40–46 |
| 12–15 m | Size 46–50 | Size 46–50 |
| 15–18 m | Size 50–60 | Size 50–65 |
| 18–22 m | — (immer elektrisch) | Size 60–80 |

#### 7.1.2 Genua-/Fock-Winschen (Headsail Sheet Winches)

**Besondere Wartungsanforderungen:**
- Zweithöchste Belastung, aber kontinuierlicher (weniger Lastwechsel als Großschot)
- Self-Tailing-Funktion hier besonders kritisch (Einhandmanöver)
- Paarweise montiert → IMMER beide gleichzeitig warten
- Position am Cockpitrand → direkter Spritzwasserkontakt

**Wartungsintervall:** Standard
**Self-Tailing-Wartung:** Bei jedem Service Jaw-Inserts prüfen
**Typische Problemzonen:** Self-Tailing (Salzkristalle), Trommelrillen (Seilabrieb)

#### 7.1.3 Spi-/Gennaker-Winschen (Spinnaker Winches)

**Besondere Wartungsanforderungen:**
- Intermittierende Nutzung, aber extreme Spitzenlasten beim Bergen
- Oft lange Standzeiten → Korrosionsrisiko erhöht
- Schnelles Einholen erforderlich → Leichtgängigkeit kritisch
- Bei Regattayachten: Performance-kritisch

**Wartungsintervall:** Vor und nach jeder Regattasaison
**Besondere Aufmerksamkeit:** Leerlauf-Reibung, Sperrklinken-Reaktionszeit
**Empfehlung:** McLube OneDrop auf Sperrklinken für minimale Reaktionszeit

#### 7.1.4 Fall-Winschen (Halyard Winches)

**Besondere Wartungsanforderungen:**
- Vertikale Montage (am Mast oder auf dem Deck nahe Mastfuß)
- Hohe Dauerlast (Fall steht permanent unter Spannung)
- Geringerer Bewegungszyklus (Setzen/Bergen, selten Trimmen)
- Bei Mastmontage: schwierige Zugänglichkeit

**Wartungsintervall:** Standard, aber Sperrklinken-Check vor jedem Setzen
**Besondere Aufmerksamkeit:** Sperrklinken MÜSSEN zuverlässig greifen (Sicherheit!)
**Typische Problemzonen:** Obere Sperrklinken (tragen die Dauerlast)

#### 7.1.5 Ankerwinsch (Anchor Windlass)

**Besondere Wartungsanforderungen:**
- Extreme Umgebungsbedingungen (Bug, direkter Seewasserkontakt)
- Elektrischer Antrieb mit hoher Leistung
- Ketten- oder Tauantrieb → andere Verschleißmuster
- Korrosion ist Hauptproblem

**Wartungsintervall:** Monatlich in der Saison, Generalüberholung jährlich
**Spezifische Schmiermittel:** Marine-Getriebefett (EP-Fett), NICHT Standard-Winschfett
**Typische Problemzonen:** Solenoid, Motorlager, Kettennuss-Verschleiß

#### 7.1.6 Relingwinschen / Deckswinschen (Snubber/Utility Winches)

**Besondere Wartungsanforderungen:**
- Geringe Belastung, aber ständige Witterungseinwirkung
- Oft vergessen bei der Wartung
- Kleine Baugrößen (Size 6–16) → feine Mechanik

**Wartungsintervall:** Jährlich (bei Jahreswartung der Hauptwinschen mitmachen)
**Besondere Aufmerksamkeit:** Korrosion durch Vernachlässigung

### 7.2 Wartungsunterschiede nach Bootstyp

#### 7.2.1 Regattayacht

| Aspekt | Besonderheit | Wartungskonsequenz |
|--------|-------------|-------------------|
| Winschanzahl | 8–16 | Hoher Wartungsaufwand |
| Belastung | Sehr hoch (Grenzbereich) | Kürzere Intervalle |
| Schmiermittel | Leichtlauf-Öle bevorzugt | McLube, minimale Fettmenge |
| Self-Tailing | Racing-Jaws | Häufigerer Austausch |
| Dokumentation | Für Klassenvermessung relevant | Lückenlose Protokollierung |
| Budget | Hoch | OEM-Teile, Profi-Service |

#### 7.2.2 Fahrtenyacht

| Aspekt | Besonderheit | Wartungskonsequenz |
|--------|-------------|-------------------|
| Winschanzahl | 4–8 | Moderater Aufwand |
| Belastung | Mittel | Standard-Intervalle |
| Schmiermittel | Standard-Herstellerfett | Normaler Verbrauch |
| Self-Tailing | Standard-Jaws | Standard-Intervall |
| Eigenleistung | Erwünscht und möglich | Schulung sinnvoll |
| Budget | Moderat | OEM oder Qualitäts-Alternativen |

#### 7.2.3 Charterboot

| Aspekt | Besonderheit | Wartungskonsequenz |
|--------|-------------|-------------------|
| Nutzungsintensität | Sehr hoch (20–40 Wochen/Jahr) | Doppelte bis dreifache Intervalle |
| Bediener-Qualifikation | Variabel (oft Anfänger) | Robuste Auslegung, häufige Kontrolle |
| Self-Tailing | Häufigster Verschleißpunkt | Monatliche Prüfung |
| Dokumentation | Für Charterzulassung Pflicht | Lückenloses Logbuch |
| Budget | Betriebskosten-optimiert | OEM-Service-Kits |

#### 7.2.4 Blauwasseryacht

| Aspekt | Besonderheit | Wartungskonsequenz |
|--------|-------------|-------------------|
| Autarkie | Muss selbst warten können | Kompletter Werkzeug- und Ersatzteil-Bestand |
| Salzwasser | Permanent | Häufige Süßwasser-Spülung, konservierendes Fett |
| Tropenaufenthalt | UV + Salzwasser + Feuchtigkeit | Quartalsweise Komplett-Wartung |
| Ersatzteil-Beschaffung | Schwierig unterwegs | Umfangreiche Bevorratung |
| Eigenleistung | Pflicht | Volle Kompetenz erforderlich |

---

## 8. Fehlerbild-Atlas

### 8.1 Fehlerbild F01: Winsch dreht in beide Richtungen (kein Sperrklicken)

**Symptom:** Winschkurbel lässt sich in beide Richtungen drehen, kein Widerstand gegen den Uhrzeigersinn
**Schweregrad:** KRITISCH — Sofort Nutzung einstellen!
**Häufigkeit:** 8 % aller Winsch-Servicefälle
**Confidence:** `documented`

**Ursachen (Häufigkeit):**
1. Sperrklinken-Federn gebrochen oder herausgefallen (65 %)
2. Sperrklinken blockiert durch Schmutz/Korrosion (20 %)
3. Sperrklinken abgenutzt — Kanten gerundet (10 %)
4. Zahnkranz beschädigt (5 %)

**Diagnose:**
- Trommel abnehmen, Sperrklinken visuell prüfen
- Sperrklinken manuell betätigen — federn sie zurück?
- Zahnkranz auf Beschädigung prüfen (Lupe)

**Behebung:**
- Federn gebrochen → Austausch (kompletter Satz!)
- Sperrklinken blockiert → Reinigen, ölen, prüfen
- Sperrklinken verschlissen → Austausch (satzweise!)
- Zahnkranz beschädigt → Professionelle Reparatur oder Austausch

### 8.2 Fehlerbild F02: Winsch knirscht oder kratzt

**Symptom:** Metallisches Knirschen oder Kratzen beim Drehen der Winschkurbel
**Schweregrad:** MITTEL bis HOCH — Nutzung einschränken
**Häufigkeit:** 22 % aller Winsch-Servicefälle
**Confidence:** `documented`

**Ursachen (Häufigkeit):**
1. Mangelnde Schmierung / ausgewaschenes Fett (45 %)
2. Salzkristalle in den Lagern (25 %)
3. Korrosionsprodukte als Abrasiv-Partikel (15 %)
4. Lagerschaden (Pitting, Riefen) (10 %)
5. Fremdkörper (Sand, Fadenreste) (5 %)

**Diagnose:**
- Demontage, Reinigung, Inspektion aller Lagerflächen
- Lager einzeln prüfen: von Hand drehen, auf Rauheit achten
- Achsoberfläche auf Riefen prüfen

**Behebung:**
- Schmierung → Komplettwartung (Reinigung + Neufettung)
- Salzkristalle → Gründliche Reinigung, ggf. Essigwasser-Bad
- Korrosion → Reinigung, befallene Teile ggf. austauschen
- Lagerschaden → Lager austauschen
- Fremdkörper → Reinigung, Ursache abstellen

### 8.3 Fehlerbild F03: Self-Tailing greift nicht

**Symptom:** Schot rutscht durch den Self-Tailing-Mechanismus, wird nicht gehalten
**Schweregrad:** MITTEL — Eingeschränkte Bedienung
**Häufigkeit:** 18 % aller Winsch-Servicefälle
**Confidence:** `documented`

**Ursachen (Häufigkeit):**
1. Jaw-Inserts verschlissen (Profil abgeflacht) (40 %)
2. Falscher Schotdurchmesser für die Winschgröße (20 %)
3. Fett/Öl auf den Jaw-Inserts (15 %)
4. Feeder Arm falsch eingestellt oder gebrochen (15 %)
5. Jaw-Inserts falsch eingesetzt (nach Wartung) (10 %)

**Diagnose:**
- Profiltiefe der Jaw-Inserts messen (Sollwert: >1.5 mm)
- Schotdurchmesser prüfen (passt zum Winsch-Bereich?)
- Jaw-Inserts auf Fettspuren prüfen
- Feeder Arm Federspannung prüfen

**Behebung:**
- Verschlissen → Jaw-Inserts austauschen
- Falscher Durchmesser → Richtige Schot verwenden oder andere Jaws wählen
- Fett → Jaw-Inserts mit Isopropanol entfetten
- Feeder Arm → Einstellen oder Feder/Arm austauschen
- Falsch eingesetzt → Korrekt positionieren (Markierungen beachten)

### 8.4 Fehlerbild F04: Winsch blockiert unter Last

**Symptom:** Winsch lässt sich unter Last nicht mehr drehen, klemmt
**Schweregrad:** KRITISCH — Sicherheitsrisiko!
**Häufigkeit:** 5 % aller Winsch-Servicefälle
**Confidence:** `documented`

**Ursachen (Häufigkeit):**
1. Lagerfressen durch Schmiermittelmangel (35 %)
2. Fremdkörper im Getriebe (25 %)
3. Verformung durch Überlast (20 %)
4. Korrosion der Zentralachse (15 %)
5. Thermische Ausdehnung bei Sonneneinstrahlung (5 %)

**Sofortmaßnahme:**
- NICHT mit Gewalt drehen!
- Schot auf andere Winsch umlegen (Sicherheit!)
- Last von der Winsch nehmen (Schot über Klampe oder andere Winsch sichern)
- WD-40 oder Kriechöl einsprühen, 10 min einwirken lassen
- Vorsichtig hin und her bewegen

**Behebung:** Komplett-Demontage, Ursache identifizieren, betroffene Teile austauschen, Neufettung

### 8.5 Fehlerbild F05: Winsch schwergängig (erhöhte Kurbelbetätigung)

**Symptom:** Deutlich mehr Kraft als gewohnt erforderlich, fühlt sich „zäh" an
**Schweregrad:** GERING bis MITTEL
**Häufigkeit:** 25 % aller Winsch-Servicefälle (häufigstes Fehlerbild)
**Confidence:** `documented`

**Ursachen (Häufigkeit):**
1. Altes, verhärtetes oder verunreinigtes Fett (50 %)
2. Mangelnde Schmierung (leere Lagerstellen) (25 %)
3. Korrosion an Lagerstellen (15 %)
4. Falsche Fettsorte (zu steif bei Kälte) (10 %)

**Diagnose:** Leerlauf-Drehmoment messen (Handgefühl oder Drehmomentschlüssel)
- Neuzustand Size 40: ca. 0.3–0.5 Nm
- Wartungsbedarf ab: ca. 1.5–2.0 Nm
- Kritisch ab: ca. 3.0+ Nm

**Behebung:** Komplettwartung (Reinigung + Neufettung)

### 8.6 Fehlerbild F06: Nur ein Gang funktioniert

**Symptom:** 1. oder 2. Gang greift nicht, Winsch dreht in einem Gang frei durch
**Schweregrad:** MITTEL — Eingeschränkt nutzbar
**Häufigkeit:** 12 % aller Winsch-Servicefälle
**Confidence:** `documented`

**Ursachen:**
- 1. Gang fehlt (schnell drehen geht nicht): Obere Sperrklinken defekt/blockiert
- 2. Gang fehlt (langsam drehen hat keine Untersetzung): Untere Sperrklinken defekt oder Getriebeproblem

**Diagnose:** Demontage, Sperrklinken der betroffenen Ebene prüfen

**Behebung:**
- Federn/Sperrklinken der betroffenen Ebene austauschen
- Getriebe auf Beschädigung prüfen (bei 2.-Gang-Ausfall)

### 8.7 Fehlerbild F07: Korrosion an der Trommeloberfläche

**Symptom:** Weiße (Aluminium) oder braune (Edelstahl) Flecken auf der Trommel
**Schweregrad:** GERING (ästhetisch) bis MITTEL (wenn Lochfraß)
**Häufigkeit:** 15 % aller Winsch-Servicefälle
**Confidence:** `documented`

**Ursachen:**
- Aluminium: Unterwanderung der Eloxierung durch Salzwasser
- Edelstahl: Chlorid-induzierter Lochfraß (meist 304, selten 316)
- Kontaktkorrosion mit anderen Metallen (fehlende Isolation)

**Behebung:**
- Leicht (Oberfläche): Polieren mit Nevr-Dull oder Autosol
- Mittel: Sandstrahlen + Neu-Eloxierung (Aluminium) oder Elektropolieren (Edelstahl)
- Schwer (Lochfraß tief): Trommel austauschen

### 8.8 Fehlerbild F08: Abnormale Geräusche (Klappern, Schlagen)

**Symptom:** Ungewöhnliche Geräusche beim Drehen (Klappern, metallisches Schlagen, unregelmäßiges Klicken)
**Schweregrad:** MITTEL
**Häufigkeit:** 10 % aller Winsch-Servicefälle
**Confidence:** `documented`

**Ursachen:**
1. Lose Teile im Inneren (Feder herausgefallen, Circlip gelöst) (40 %)
2. Übermäßiges Lagerspiel (25 %)
3. Defekter Zahnkranz (Zahn abgebrochen) (15 %)
4. Trommel sitzt schief (10 %)
5. Basis-Befestigung lose (10 %)

**Diagnose:**
- Basis-Befestigung prüfen (von Hand rütteln)
- Trommel abnehmen, alle Teile auf korrekten Sitz prüfen
- Lager auf Spiel prüfen

**Behebung:** Ursachenabhängig — lose Teile sichern, verschlissene ersetzen

### 8.9 Fehlerbild F09: Schot wickelt sich ungleichmäßig

**Symptom:** Schot wickelt sich nicht sauber auf, Überwicklungen, Riding Turns
**Schweregrad:** GERING bis MITTEL (Riding Turn = KRITISCH!)
**Häufigkeit:** 8 % aller Winsch-Servicefälle
**Confidence:** `documented`

**Ursachen:**
1. Trommelrillen verschlissen oder beschädigt (30 %)
2. Falscher Schotdurchmesser (25 %)
3. Schot zu steif oder zu weich (20 %)
4. Self-Tailing-Winkel falsch (Lead-Block-Position) (15 %)
5. Trommeloberfläche zu glatt (korrodierte/polierte Rillen) (10 %)

**Behebung:** Ursachenspezifisch; bei Riding Turns: SOFORT Last wegnehmen, ggf. Schot kappen

### 8.10 Fehlerbild F10: Elektrische Winsch reagiert nicht

**Symptom:** Knopfdruck → keine Reaktion
**Schweregrad:** MITTEL bis HOCH
**Häufigkeit:** 15 % aller E-Winsch-Servicefälle
**Confidence:** `documented`

**Ursachen:**
1. Sicherung/Hauptschalter defekt (30 %)
2. Solenoid defekt (25 %)
3. Kabelverbindung korrodiert/lose (20 %)
4. Motor defekt (15 %)
5. Steuereinheit/Taster defekt (10 %)

**Diagnose-Reihenfolge:**
1. Sicherungskasten prüfen (visuell + Multimeter)
2. Hauptschalter prüfen (ein?)
3. Spannung am Solenoid messen (12V/24V vorhanden?)
4. Solenoid überbrücken (Motor direkt ansteuern — Vorsicht!)
5. Motor-Widerstand messen (Sollwert lt. Hersteller)

### 8.11 Fehlerbild F11: Festsitzende Befestigungsschrauben

**Symptom:** Basis-Befestigungsschrauben lassen sich nicht lösen (festgefressen)
**Schweregrad:** GERING (erschwert Wartung)
**Häufigkeit:** 20 % aller Demontage-Versuche
**Confidence:** `documented`

**Ursachen:**
- Galvanische Korrosion (Edelstahl-Schraube in Aluminium-Winsch)
- Fehlende Anti-Seize-Paste bei der Montage
- Fehlende Wartung der Schraubverbindung

**Lösungsansätze (Eskalation):**
1. Kriechöl (WD-40, Caramba, Rostlöser) auftragen, 30 min einwirken lassen → erneut versuchen
2. Kriechöl erneut, 24 h einwirken lassen
3. Leichte Schläge mit Kunststoffhammer auf den Schraubenkopf (Vibration löst Korrosion)
4. Wärme-Kälte-Behandlung: Heißluftfön auf die Umgebung, dann schnell Kältespray auf die Schraube
5. Links-Rechts-Technik: 1/8 Umdrehung links, 1/8 rechts, langsam steigern
6. Schraubenausdreher (bei zerstörtem Kopf)
7. Aufbohren (letztes Mittel — Gewinde ggf. mit Heli-Coil reparieren)

**Prävention:** IMMER Tef-Gel oder Duralac auf Befestigungsschrauben!

### 8.12 Fehlerbild F12: Winsch vibriert unter Last

**Symptom:** Spürbare Vibration der Winsch und des umgebenden Decks unter Last
**Schweregrad:** MITTEL bis HOCH (Strukturelles Problem möglich!)
**Häufigkeit:** 3 % aller Winsch-Servicefälle
**Confidence:** `documented`

**Ursachen:**
1. Lose Basis-Befestigung (40 %)
2. Backing Plate defekt oder fehlend (25 %)
3. Lagerschaden mit Unwucht (20 %)
4. Deck unter der Winsch beschädigt (Delaminierung, Kernfäule) (10 %)
5. Resonanzfrequenz der Winsch = Getriebedrehzahl (5 %)

**Diagnose:**
- Befestigungsschrauben mit Drehmomentschlüssel prüfen
- Deck um die Winsch herum beklopfen (Hohlklang = Kernfäule/Delaminierung)
- Winsch demontieren, Deck-Oberfläche inspizieren
- Bei Verdacht auf Kernfäule: Feuchtigkeitsmessung

**Behebung:**
- Lose Befestigung → Nachziehen mit korrektem Drehmoment
- Backing Plate → Verstärkung einbauen (Edelstahl- oder Aluminium-Platte)
- Lagerschaden → Lager austauschen
- Kernfäule → Deck reparieren (Kern ersetzen, Laminat erneuern) vor Neuinstallation der Winsch!

---

## 9. Troubleshooting-Entscheidungsbaum

### 9.1 Entscheidungsbaum: Winsch dreht schwergängig

```
START: Winsch dreht schwergängig
│
├─ Frage 1: Wurde die Winsch in den letzten 12 Monaten gewartet?
│  │
│  ├─ NEIN → Komplettwartung durchführen (Abschnitt 4.2)
│  │         → Problem gelöst? → JA → ENDE
│  │                           → NEIN → Weiter zu Frage 2
│  │
│  └─ JA → Weiter zu Frage 2
│
├─ Frage 2: Tritt das Problem bei Kälte (<10°C) stärker auf?
│  │
│  ├─ JA → Fett zu steif für die Temperatur
│  │       → Lösung: Auf Fett mit tieferem Temperaturbereich wechseln
│  │       → Empfehlung: Andersen Service Grease (–35°C) oder Harken White (–30°C)
│  │
│  └─ NEIN → Weiter zu Frage 3
│
├─ Frage 3: Knirscht oder kratzt die Winsch?
│  │
│  ├─ JA → Lagerschaden oder Fremdkörper
│  │       → Demontage, Lager prüfen (Abschnitt 4.2.4, Nr. 3–4)
│  │       → Lager beschädigt → Austausch
│  │       → Fremdkörper → Gründliche Reinigung
│  │
│  └─ NEIN → Weiter zu Frage 4
│
├─ Frage 4: Tritt das Problem in beiden Gängen gleich auf?
│  │
│  ├─ JA → Zentrale Komponente betroffen (Achse, Basis, Hauptlager)
│  │       → Achse auf Riefen prüfen
│  │       → Hauptlager prüfen
│  │
│  └─ NEIN → Gangspezifisches Problem
│           → Nur 1. Gang schwer → Obere Baugruppe prüfen
│           → Nur 2. Gang schwer → Untere Baugruppe/Getriebe prüfen
│
└─ ENDE: Bei fortbestehendem Problem → Professionellen Service beauftragen
```

### 9.2 Entscheidungsbaum: Self-Tailing funktioniert nicht

```
START: Schot rutscht durch Self-Tailing
│
├─ Frage 1: Passt der Schotdurchmesser zur Winschgröße?
│  │
│  ├─ NEIN → Richtige Schot verwenden (Hersteller-Tabelle beachten)
│  │
│  └─ JA → Weiter zu Frage 2
│
├─ Frage 2: Sind die Jaw-Inserts sichtbar verschlissen?
│  │
│  ├─ JA → Profiltiefe messen
│  │       → <1.0 mm → Austausch
│  │       → 1.0–1.5 mm → Austausch empfohlen, noch nutzbar
│  │       → >1.5 mm → Weiter zu Frage 3
│  │
│  └─ NEIN → Weiter zu Frage 3
│
├─ Frage 3: Ist Fett/Öl auf den Jaw-Inserts oder der Trommeloberfläche?
│  │
│  ├─ JA → Mit Isopropanol entfetten, Self-Tailing-Bereich FETTFREI halten
│  │
│  └─ NEIN → Weiter zu Frage 4
│
├─ Frage 4: Funktioniert der Feeder Arm korrekt?
│  │
│  ├─ NEIN → Feeder Arm Feder prüfen/austauschen
│  │         → Feeder Arm Einstellung prüfen
│  │
│  └─ JA → Weiter zu Frage 5
│
├─ Frage 5: Ist die Schot-Oberfläche glatt/abgenutzt?
│  │
│  ├─ JA → Schot ersetzen (abgenutztes Dyneema/Polyester hat weniger Grip)
│  │
│  └─ NEIN → Racing/Line-Grip Jaw-Inserts versuchen (mehr Profil)
│
└─ ENDE
```

### 9.3 Entscheidungsbaum: Sperrklinken greifen nicht

```
START: Sperrklinken greifen nicht (Winsch dreht in beide Richtungen)
│
├─ Frage 1: Betrifft es alle Sperrklinken oder nur einige?
│  │
│  ├─ ALLE → Wahrscheinlich Grundproblem
│  │         → Wurden alle Federn korrekt eingesetzt? (nach Wartung)
│  │         → JA → Zahnkranz prüfen (Beschädigung?)
│  │         → NEIN → Federn korrekt einsetzen, Funktionstest
│  │
│  └─ EINIGE → Weiter zu Frage 2
│
├─ Frage 2: Sind die betroffenen Sperrklinken frei beweglich?
│  │
│  ├─ NEIN → Blockiert durch Schmutz/Korrosion/verhärtetes Fett
│  │         → Reinigen, ölen, Beweglichkeit wiederherstellen
│  │
│  └─ JA → Weiter zu Frage 3
│
├─ Frage 3: Sind die zugehörigen Federn intakt?
│  │
│  ├─ NEIN → Federn austauschen (IMMER kompletten Satz!)
│  │
│  └─ JA → Sperrklinken-Kanten prüfen (verschlissen/abgerundet?)
│         → Abgerundet → Sperrklinken austauschen
│         → Scharf → Zahnkranz prüfen (einzelne Zähne beschädigt?)
│
└─ ENDE
```

### 9.4 Entscheidungsbaum: Elektrische Winsch — kein Antrieb

```
START: E-Winsch reagiert nicht auf Knopfdruck
│
├─ Schritt 1: Hauptsicherung prüfen
│  │
│  ├─ DEFEKT → Sicherung ersetzen (gleicher Wert!)
│  │           → Tritt erneut auf → Motor-Kurzschluss → Profi-Service
│  │
│  └─ OK → Schritt 2
│
├─ Schritt 2: Spannung am Solenoid prüfen (Multimeter)
│  │
│  ├─ KEINE Spannung → Kabelweg prüfen (Hauptschalter, Sicherungstafel, Kabel)
│  │                   → Kabel korrodiert → Erneuern
│  │                   → Schalter defekt → Austauschen
│  │
│  └─ Spannung vorhanden → Schritt 3
│
├─ Schritt 3: Solenoid schaltet?
│  │
│  ├─ NEIN (kein Klicken) → Solenoid defekt → Austauschen
│  │
│  └─ JA (Klicken hörbar) → Schritt 4
│
├─ Schritt 4: Spannung am Motor prüfen
│  │
│  ├─ KEINE Spannung → Solenoid-Kontakte verschlissen → Solenoid tauschen
│  │
│  └─ Spannung vorhanden → Motor defekt
│                          → Motor-Widerstand messen (vs. Sollwert)
│                          → Motorlager prüfen (blockiert?)
│                          → Bürsten prüfen (bei Bürstenmotor)
│                          → Profi-Service
│
└─ ENDE
```

### 9.5 Entscheidungsbaum: Ungewöhnliche Geräusche

```
START: Winsch macht ungewöhnliche Geräusche
│
├─ Geräuschtyp: Knirschen/Kratzen?
│  → Siehe Fehlerbild F02 (Abschnitt 8.2)
│
├─ Geräuschtyp: Klappern/Schlagen?
│  │
│  ├─ Im Leerlauf? → Loses Teil im Inneren
│  │                → Trommel abnehmen, alle Teile auf Sitz prüfen
│  │
│  └─ Unter Last? → Lagerspiel oder Zahnrad-Problem
│                  → Lagerspiel messen (Abschnitt 4.2.4)
│                  → Getriebezähne inspizieren
│
├─ Geräuschtyp: Ungleichmäßiges Klicken?
│  │
│  ├─ Einige Klicks lauter → Eine Sperrklinke greift anders
│  │                        → Pawl-Springs prüfen (ungleiche Federkraft?)
│  │
│  └─ Klick fehlt zeitweise → Sperrklinke blockiert intermittierend
│                            → Reinigen, ölen
│
├─ Geräuschtyp: Quietschen?
│  → Trockenlauf an einer Lagerstelle
│  → Sofort schmieren! (Notfall: 1–2 Tropfen Öl auf Achse geben)
│  → Baldmöglichst Komplettwartung
│
└─ ENDE
```

---

## 10. FAQ

### 10.1 Grundlegende Wartungsfragen

**F01: Wie oft muss ich meine Winschen warten?**

Die Wartungsfrequenz hängt von der Nutzungsintensität und dem Einsatzgebiet ab. Als Minimum gilt:
- **Salzwasser:** Süßwasser-Spülung nach jedem Einsatz, Komplettwartung mindestens jährlich
- **Binnenrevier:** Komplettwartung mindestens alle 2 Jahre
- **Charterboot:** Monatliche Sichtprüfung, halbjährliche Komplettwartung
- **Regattaboot:** Vor und nach jeder Regattasaison, ggf. häufiger

Siehe Abschnitt 3 für detaillierte Wartungspläne.

**F02: Kann ich die Wartung selbst durchführen?**

Ja, die Standard-Wartung (Stufe A und B) kann von jedem Bootseigner mit grundlegenden handwerklichen Fähigkeiten selbst durchgeführt werden. Die Generalüberholung (Stufe C) erfordert mehr Erfahrung und spezielle Werkzeuge, ist aber ebenfalls als Eigenleistung möglich. Nur die Wartung elektrischer Winschantriebe sollte einem Fachbetrieb überlassen werden.

Zeitbedarf für die Erstdurchführung: ca. 2 Stunden pro Winsch (mit Anleitung). Nach 2–3 Durchgängen: ca. 45 Minuten pro Winsch.

**F03: Welches Fett soll ich verwenden?**

Verwenden Sie IMMER das vom Hersteller empfohlene Fett:
- **Harken:** Harken White Grease (BK4520)
- **Lewmar:** Lewmar Winch Grease (19701500)
- **Andersen:** Andersen Service Grease (NICHT mit Lithium-Fetten mischen!)
- **Antal:** Antal-empfohlenes Fett (Lithium-basiert) oder Harken White Grease

Wenn Herstellerfett nicht verfügbar ist, verwenden Sie ein hochwertiges Lithium-Komplex-Fett NLGI 2 mit PTFE und guter Wasserbeständigkeit. Bei Andersen-Winschen: NUR Calcium-Sulfonat-kompatibles Fett verwenden!

**F04: Darf ich WD-40 für meine Winschen verwenden?**

**NEIN** — WD-40 ist KEIN Schmiermittel, sondern ein Kriechöl/Wasserverdränger. Es verdünnt vorhandenes Fett, trocknet aus und hinterlässt einen Film, der Schmutz anzieht. Einzige Ausnahme: WD-40 kann zum Lösen festsitzender Teile verwendet werden (Kriechöl-Funktion). Danach MUSS die Stelle entfettet und mit richtigem Winschfett nachgeschmiert werden.

**F05: Was kostet eine professionelle Winsch-Wartung?**

Richtwerte für professionelle Wartung (Werft/Rigger, DACH-Region 2024/2025):
- Einfache Wartung (1 Winsch, Size 40): 80–150 EUR (inkl. Material)
- Komplettwartung (1 Winsch, Size 40): 150–250 EUR
- Generalüberholung (1 Winsch, Size 40): 250–450 EUR
- Komplettwartung eines 12-m-Boots (6 Winschen): 600–1.200 EUR
- Elektrische Winsch (zusätzlich zum mechanischen Teil): +200–500 EUR

### 10.2 Schmiermittel und Reinigung

**F06: Kann ich verschiedene Fette mischen?**

Grundsätzlich NEIN. Verschiedene Verdicker-Typen können chemisch unverträglich sein und sich gegenseitig zersetzen (Verflüssigung, Trennung). Insbesondere:
- Lithium-Fett + Calcium-Sulfonat = NICHT verträglich
- Lithium + Lithium-Komplex = Bedingt verträglich

Empfehlung: Bei jedem Fettwechsel das alte Fett VOLLSTÄNDIG entfernen. Siehe Verträglichkeitsmatrix in Abschnitt 5.3.

**F07: Wie entferne ich altes, verhärtetes Fett?**

1. Teile in Petroleum oder White Spirit einlegen (15–30 Minuten)
2. Mit Pinsel und Lappen altes Fett lösen
3. Bei hartnäckigen Rückständen: Vorgang wiederholen, ggf. über Nacht einweichen
4. Feinreinigung mit Isopropanol
5. Vollständig trocknen lassen vor Neufettung

NICHT verwenden: Aceton (greift Kunststoff an), Hochdruckreiniger (Wassereinschluss)

**F08: Muss ich die Self-Tailing-Backen fetten?**

**NEIN — NIEMALS!** Die Self-Tailing-Backen (Jaw Inserts) und der umgebende Bereich müssen absolut fettfrei sein. Fett auf den Jaw-Inserts führt dazu, dass die Schot durchrutscht. Falls versehentlich Fett darauf geraten ist: mit Isopropanol gründlich entfetten.

**F09: Was ist der Unterschied zwischen Winschfett und Winschöl?**

- **Winschfett** (Grease): Dickflüssig, für Lager, Achsen, Getriebezähne. Bleibt an der Schmierstelle, lange Standzeit.
- **Winschöl** (Oil): Dünnflüssig, für Sperrklinken-Federn, Sperrklinken-Drehpunkte. Kriecht in feine Spalte, kurze Standzeit.

Beide werden benötigt! Fett dort, wo es haften soll (Lager, Getriebe). Öl dort, wo Teile frei beweglich bleiben müssen (Sperrklinken).

**F10: Wie oft muss ich die Sperrklinken ölen?**

Empfehlung: Alle 1–3 Monate bei regelmäßiger Nutzung. In der Praxis: Trommel abnehmen, 2–3 Tropfen Herstelleröl auf jede Sperrklinken-Feder, Trommel wieder aufsetzen, fertig. Zeitaufwand: 5 Minuten pro Winsch.

### 10.3 Verschleißteile und Ersatzteile

**F11: Woran erkenne ich, dass die Sperrklinken-Federn schwach sind?**

Anzeichen:
- Sperrklinken greifen verzögert (beim langsamen Drehen leises, unregelmäßiges Klicken)
- Im Vergleich zu einer frisch gewarteten Winsch: deutlich leiseres Klicken
- Visuell: Federn erscheinen verformt, verbogen oder gebrochen
- Funktionell: Sperrklinke federt nach manueller Auslenkung nur langsam zurück

Prüfung: Sperrklinke mit dem Finger auslenken und loslassen. Sie muss SOFORT und kräftig in die Ausgangsposition zurückschnellen. Wenn sie langsam oder zögerlich zurückgeht → Federn austauschen.

**F12: Müssen Sperrklinken-Federn immer satzweise getauscht werden?**

JA. Immer den kompletten Federsatz einer Winsch austauschen. Einzelner Austausch führt zu ungleichmäßiger Federkraft und damit zu ungleichmäßigem Sperrklinken-Verhalten. Die Kosten für einen Federsatz (10–40 EUR) stehen in keinem Verhältnis zum Risiko eines Winsch-Ausfalls.

**F13: Wie messe ich die Profiltiefe der Jaw-Inserts?**

Mit einem Messschieber oder einem Tiefenmesser:
1. Messschieber auf die Oberkante des Profils aufsetzen
2. Tiefenmesser bis zum Profilgrund absenken
3. Ablesen

Neuzustand: 3.0–4.0 mm (je nach Hersteller)
Grenze: <1.0 mm → sofort austauschen
Grauzone: 1.0–1.5 mm → Austausch empfohlen

**F14: Kann ich Ersatzteile verschiedener Hersteller mischen?**

NEIN. Sperrklinken, Federn, Jaw-Inserts, Lager und andere Verschleißteile sind herstellerspezifisch und NICHT austauschbar. Die Geometrien, Materialien und Toleranzen unterscheiden sich. Immer Original-Ersatzteile des Winsch-Herstellers verwenden.

**F15: Wo kann ich Ersatzteile bestellen?**

- **Harken:** Über autorisierte Händler, harken.com (Online-Shop in einigen Regionen)
- **Lewmar:** lewmar.com, autorisierte Händler, SVB, Compass24
- **Andersen:** andersen-winches.com, Fachhändler
- **Antal:** antal.it, italienische und internationale Händler
- **Allgemein:** SVB (svb24.de), Compass24 (compass24.de), Toplicht (toplicht.de), AWN (awn.de), Bootsteile.de

### 10.4 Spezifische Probleme

**F16: Meine Winsch macht ein mahlendes Geräusch — ist das gefährlich?**

Ein mahlendes Geräusch deutet auf Trockenlauf oder Fremdkörper in den Lagern hin. Die Winsch sollte SOFORT aus dem Betrieb genommen werden (wenn möglich), da jede weitere Nutzung den Schaden vergrößert. Erste Hilfe: 2–3 Tropfen Öl auf die Achse geben (von oben in die Winsch tropfen lassen). Baldmöglichst Komplettwartung durchführen.

**F17: Kann ich meine Winschen mit einem Hochdruckreiniger reinigen?**

**NEIN!** Hochdruckreiniger drücken Wasser in die Lager und Dichtungen, wo es Korrosion verursacht. Außerdem wird Fett aus den Schmierstellen herausgespült. Verwenden Sie nur einen normalen Gartenschlauch oder eine Sprühflasche für die Süßwasser-Spülung.

**F18: Meine Winsch ist nach dem Zusammenbau schwergängiger als vorher — was ist falsch?**

Häufige Ursachen:
1. **Zu viel Fett** — überschüssiges Fett erzeugt Widerstand. Lösung: Etwas Fett entfernen.
2. **Fett auf den Sperrklinken** — Sperrklinken kleben statt zu federn. Lösung: Sperrklinken und Federn entfetten, NUR ölen.
3. **Teile falsch zusammengesetzt** — Baugruppe sitzt schief. Lösung: Erneut zerlegen, korrekt zusammensetzen.
4. **Lager falsch eingesetzt** — Nadellager verkippt. Lösung: Lager korrekt positionieren.

Die Winsch sollte sich nach 20–30 Umdrehungen im Leerlauf „einlaufen" und leichtgängiger werden. Wenn nicht: erneut demontieren und Ursache suchen.

**F19: Wie lagere ich Winschen über den Winter?**

Ideale Winterlagerung:
1. Komplettwartung im Herbst (Reinigung + Neufettung)
2. Korrosionsschutz-Spray auf die Trommeloberfläche (Sprühwachs oder Korrosionsschutzöl)
3. Winschkurbel-Aufnahme abdecken (Kappe oder Klebeband)
4. Keine Schoten auf den Winschen lassen (Feuchtigkeit, Schimmel)
5. Bei Hallenüberwinterung: keine besonderen Maßnahmen
6. Bei Freilandüberwinterung: Persenning muss die Winschen abdecken

**F20: Meine Andersen-Winsch wurde mit Harken-Fett geschmiert — ist das ein Problem?**

JA, potenziell. Andersen verwendet Calcium-Sulfonat-Verdicker, Harken verwendet Lithium-Komplex. Diese sind NICHT kompatibel. Mischung kann zu Verflüssigung oder Aushärtung führen. Empfehlung:
1. Winsch sofort demontieren
2. Alle Teile gründlich reinigen (altes Fett vollständig entfernen!)
3. Mit Andersen Service Grease neu fetten

### 10.5 Fortgeschrittene Fragen

**F21: Kann ich meine mechanische Winsch auf Elektroantrieb umrüsten?**

Ja, die meisten größeren Hersteller bieten Elektro-Nachrüstsätze an:
- **Harken:** UniPower Retrofit Kit (für Radial-Winschen ab Size 40)
- **Lewmar:** EVO Electric Conversion Kit (für EVO-Winschen ab Size 40)
- **Andersen:** Compact Electric Kit (für Compact-Winschen ab Size 40)

Voraussetzungen: Ausreichend Platz unter Deck, 12V/24V Batteriebank mit ausreichender Kapazität, Kabelquerschnitt gemäß Hersteller-Vorgabe.

Kosten: 2.500–6.000 EUR (Motor + Installation, ohne Elektrik-Anpassung)

**F22: Wie kann ich die Leistung meiner Winschen für Regatten optimieren?**

Regatta-spezifische Optimierungen:
1. **Minimalschmierung:** Weniger Fett als Standard, dafür häufiger nachschmieren. McLube OneDrop auf Sperrklinken.
2. **Racing Jaw-Inserts:** Aggressiveres Profil für besseren Grip (Harken Performa, Lewmar Racing, Andersen Line-Grip).
3. **Leichtlauf-Öl statt Fett** an einigen Stellen (nur bei häufiger Nachschmierung!).
4. **Sperrklinken-Reaktionszeit** prüfen: sofortiges, lautes Klicken ist ideal.
5. **Regelmäßige Wartung:** Vor jeder Regatta Kurzwartung (Ölen der Sperrklinken, Self-Tailing-Check).

**F23: Meine Winsch ist 30 Jahre alt — lohnt sich eine Überholung?**

Das hängt von der Marke und dem Zustand ab:
- **Harken, Lewmar, Andersen** (Qualitätsmarken): Überholung lohnt sich fast immer, wenn Basis und Trommel intakt sind. Ersatzteile sind für viele ältere Modelle noch verfügbar.
- **Barient, Barlow** (historische Marken): Ersatzteile schwer erhältlich. Überholung nur wenn Ersatzteile vorhanden. Alternative: Adapterbasis für moderne Winsch.
- **No-Name/Billigmarken:** Überholung lohnt sich selten. Ersatzteile nicht verfügbar. Austausch empfohlen.

Faustregel: Wenn die Überholungskosten >50 % einer neuen Winsch betragen, ist ein Neukauf sinnvoller.

**F24: Wie erkenne ich, ob meine Winsch eine 316- oder 304-Edelstahlachse hat?**

Direkte Erkennung am eingebauten Bauteil ist ohne Laboranalyse schwierig. Hinweise:
- **Markenhersteller** (Harken, Lewmar, Andersen, Antal): Verwenden 316/316L für alle salzwasserexponierten Teile.
- **Billig-Winschen** (insb. chinesische Produktion): Oft 304 oder gar 430 (magnetisch!).
- **Magnettest:** 316 ist schwach magnetisch oder nicht magnetisch. 430/410 ist stark magnetisch. 304 ist schwach magnetisch.
- **Korrosionsbild:** 304 zeigt Lochfraß und Tee-Staining deutlich schneller als 316.

**F25: Was muss ich bei Winschen auf einem Katamaran besonders beachten?**

Katamarane haben spezifische Anforderungen:
- **Höhere Scheinbar-Wind-Geschwindigkeiten** → höhere Schotlasten → größere Winschen wählen
- **Zwei Rümpfe** → doppelte Winschanzahl → höherer Wartungsaufwand
- **Brücken-Cockpit** → Winschen stärker UV- und Spritzwasser-exponiert
- **Elektrische Winschen** empfohlen (längere Schotwege, Einhandsegeln)
- **Salzwasser-Spülung** besonders wichtig (mehr Spritzwasser durch Brückendeck)

### 10.6 Fragen zu Spezialthemen

**F26: Kann ich Edelstahl-Winschen mit Aluminium-Winschen mischen?**

Ja, es ist technisch möglich, verschiedene Materialien auf demselben Boot zu verwenden. Allerdings gibt es einige Aspekte zu beachten:
- Edelstahl-Winschen (z.B. Andersen Compact, einige Harken-Modelle) sind schwerer, aber korrosionsbeständiger
- Aluminium-Winschen (eloxiert) sind leichter, aber anfälliger für Kontaktkorrosion
- Die Wartung ist materiellabhängig: Aluminium verträgt keine sauren Reiniger (Essig, Zitronensäure!)
- Bei der Befestigung von Edelstahl-Winschen auf Aluminium-Deck: IMMER Isolierung (Tef-Gel + Isolierscheiben)

**F27: Wie erkenne ich eine gefälschte Marken-Winsch?**

Gefälschte Winschen sind selten, aber es gibt Nachbauten (insbesondere aus China), die als Markenprodukte verkauft werden. Erkennungsmerkmale:
- Fehlende oder unscharfe Gravur/Prägung der Marke und Modellnummer
- Ungleichmäßige Eloxierung (Farbunterschiede, raue Oberflächen)
- Kein Seriennummern-Aufkleber oder -Gravur
- Deutlich leichteres Gewicht als Original
- Billige Verpackung ohne Hersteller-Dokumentation
- Magnettest: 304er Edelstahl (Fälschung) ist stärker magnetisch als 316L (Original)

Im Zweifel: Beim Hersteller die Seriennummer verifizieren lassen.

**F28: Meine Winsch quietscht nur bei Feuchtigkeit — warum?**

Das Quietschen bei Feuchtigkeit deutet auf ausgewaschenes Fett hin. Wasser hat die Schmierung an einer oder mehreren Lagerstellen verdrängt. Bei Trockenheit funktioniert die Restschmierung noch, bei Feuchtigkeit kommt es zu Metall-Wasser-Metall-Kontakt mit erhöhter Reibung.

Lösung: Komplettwartung (Demontage, Reinigung, Neufettung mit wasserbeständigem Fett). Prävention: Regelmäßige Süßwasser-Spülung nach Salzwasserkontakt.

**F29: Gibt es eine App oder Software zur Winsch-Wartungsdokumentation?**

Ja, es gibt mehrere Möglichkeiten:
- **AYDI:** Die AYDI-Plattform bietet im Profi-Werkzeug (Level 2) eine vollständige Winsch-Zustandsdokumentation mit Wartungshistorie
- **BoatMate / Bootscheck:** Allgemeine Boots-Wartungs-Apps mit anpassbaren Checklisten
- **Excel/Google Sheets:** Einfache Tabelle mit Datum, Winsch-Position, durchgeführte Maßnahmen, verwendete Teile
- **Bordbuch-App:** Integrierte Dokumentation im digitalen Bordbuch

**F30: Was kostet eine neue Winsch, wenn die alte nicht mehr reparierbar ist?**

Richtwerte (Neupreise 2024/2025, inkl. MwSt.):

| Hersteller | Size 28ST | Size 40ST | Size 46ST | Size 50ST |
|------------|-----------|-----------|-----------|-----------|
| Harken Radial | 680 EUR | 1.250 EUR | 1.650 EUR | 2.100 EUR |
| Lewmar EVO | 520 EUR | 950 EUR | 1.350 EUR | 1.750 EUR |
| Andersen Compact | 750 EUR | 1.400 EUR | 1.800 EUR | 2.350 EUR |
| Antal W-Serie | 450 EUR | 820 EUR | 1.150 EUR | 1.500 EUR |

Elektrische Versionen: ca. +2.500 bis +5.000 EUR (je nach Größe und Hersteller)

Zusätzliche Kosten bei Austausch:
- Demontage alte Winsch: 50–100 EUR
- Montage neue Winsch: 100–200 EUR
- Ggf. Adapterplatte: 80–200 EUR
- Ggf. Deck-Reparatur (alte Bohrlöcher): 100–300 EUR

**F31: Wie transportiere ich eine demontierte Winsch sicher?**

Beim Transport demontierter Winschen (z.B. zur Werft, zum Rigger):
1. Alle Kleinteile in beschrifteten Ziplock-Beuteln
2. Sperrklinken und Federn: Beutel "OBEN" und "UNTEN"
3. Trommel einzeln in weiches Tuch einwickeln (Eloxierung schützen)
4. Lager einzeln verpacken (nicht gegeneinander reiben)
5. Alles in einer stabilen Box (z.B. Werkzeugkoffer)
6. Fotos der Zerlegung beilegen (für den Servicetechniker)

**F32: Meine Winschkurbel dreht durch — liegt das an der Winsch?**

Nicht unbedingt. Prüfen Sie zunächst:
1. **Winschkurbel-Aufnahme:** Vierkant/Sechskant verschlissen? → Kurbel passt nicht mehr exakt
2. **Kurbel selbst:** Interne Mechanik der Kurbel defekt (bei Doppelkurbeln: Richtungswechsel-Mechanismus)
3. **Winsch-Aufnahme:** Oberer Einsatz in der Trommel verschlissen

In 70 % der Fälle liegt das Problem an der Winschkurbel selbst, nicht an der Winsch.

**F33: Kann ich meine Winschen lackieren oder neu eloxieren lassen?**

- **Neu-Eloxierung:** Ja, möglich. Die Trommel muss demontiert und an einen Eloxier-Betrieb geschickt werden. Kosten: 50–150 EUR pro Trommel. Farbe (klar, schwarz, gold) wählbar.
- **Lackieren:** Technisch möglich, aber NICHT empfohlen. Lack auf der Trommel-Außenseite verschleißt schnell durch Seilreibung. Lack auf der Innenseite kann in die Mechanik gelangen.
- **Polieren:** Anlauffarben und leichte Korrosion auf Edelstahl können mit Nevr-Dull oder Autosol poliert werden.

**F34: Wie beeinflusst der Schottyp die Winsch-Wartung?**

| Schottyp | Einfluss auf Wartung | Besonderheit |
|----------|---------------------|-------------|
| Polyester (Standard) | Normal | Fasern können in Mechanik gelangen |
| Dyneema/Spectra | Weniger Abrieb auf Trommel | Schotmantel kann Jaw-Inserts schneller verschleißen |
| Aramid (Kevlar) | Höherer Trommel-Abrieb | Selten als Schot verwendet |
| Vectran | Ähnlich wie Polyester | — |
| PBO (Zylon) | UV-empfindlich, Fasern spröde | Fasern als Abrasiv in Lagern möglich |

Empfehlung: Bei Schotwechsel die Trommelrillen auf Abriebspuren prüfen. Faserbruchstücke bei jeder Wartung aus der Winsch entfernen.

**F35: Meine Winsch hat nach der Wartung einen „toten Punkt" — was bedeutet das?**

Ein "toter Punkt" (kurzes Stocken bei einer bestimmten Trommelposition) deutet auf:
1. Ungleichmäßig verteiltes Fett (Klumpen)
2. Eine Sperrklinke, die an einer Stelle im Zahnkranz hängt (beschädigter Zahn)
3. Ein leicht verkipptes Lager
4. Eine verformte Feder, die intermittierend blockiert

Lösung: Trommel abnehmen, betroffenen Bereich identifizieren (Trommel langsam drehen und Position des toten Punkts markieren), Ursache beheben.

---

## 11. Glossar

### Technische Fachbegriffe Deutsch — Englisch — Erklärung

| Nr. | Deutsch | Englisch | Erklärung |
|-----|---------|----------|-----------|
| 1 | Achse (Zentral-) | Main Shaft / Center Post | Die zentrale vertikale Achse der Winsch, um die sich die Trommel dreht |
| 2 | Abrasiver Verschleiß | Abrasive Wear | Materialverlust durch Reibung mit harten Partikeln (Sand, Salzkristalle) |
| 3 | Adhäsiver Verschleiß | Adhesive Wear (Galling) | Materialübertrag zwischen zwei metallischen Oberflächen bei Trockenlauf |
| 4 | Backing Plate | Backing Plate | Verstärkungsplatte unter dem Deck zur Lastverteilung der Winsch-Befestigung |
| 5 | Blattfeder | Leaf Spring | Flache Feder, die die Sperrklinke in die Greifposition drückt (Lewmar-typisch) |
| 6 | Circlip | Circlip / Snap Ring | Sicherungsring, der Trommel oder andere Bauteile axial sichert |
| 7 | Delrin | Delrin / Acetal (POM) | Technischer Kunststoff für selbstschmierende Lager (Antal, Andersen) |
| 8 | Drahtfeder | Wire Spring | Drahförmige Feder in V- oder Omega-Form (Harken, Andersen) |
| 9 | Drehmoment | Torque | Kraft × Hebelarm; wird in Nm (Newtonmeter) gemessen |
| 10 | Eloxierung | Anodizing | Elektrochemische Oberflächenbehandlung von Aluminium zum Korrosionsschutz |
| 11 | EP-Additiv | Extreme Pressure Additive | Schmiermittelzusatz für hohe Druckbelastungen (Getriebezähne) |
| 12 | Feeder Arm | Feeder Arm | Führungsarm, der die Schot in den Self-Tailing-Bereich leitet |
| 13 | Fieren | To Ease / To Pay Out | Kontrolliertes Nachlassen einer Schot unter Last |
| 14 | Fühlerlehre | Feeler Gauge | Satz dünner Metallblätter zur Messung von Spalten und Spielen |
| 15 | Galvanische Korrosion | Galvanic Corrosion | Elektrochemische Korrosion zwischen zwei verschiedenen Metallen in Salzwasser |
| 16 | Getriebe (Planeten-) | Planetary Gear | Zahnradgetriebe mit Sonnenrad, Planetenrädern und Ringzahnkranz |
| 17 | Jaw-Insert | Jaw Insert | Auswechselbare Backen im Self-Tailing-Ring, die die Schot halten |
| 18 | Klinke (Sperr-) | Pawl | Hebel, der in den Zahnkranz eingreift und Rücklauf verhindert |
| 19 | Kriechöl | Penetrating Oil | Dünnflüssiges Öl zum Lösen festsitzender Verbindungen (z.B. WD-40) |
| 20 | Lagerspiel | Bearing Clearance | Spiel zwischen Lager und Achse/Gehäuse; bestimmt Präzision und Reibung |
| 21 | Lochfraß | Pitting | Lokalisierte Korrosionsform mit kleinen, tiefen Löchern in der Oberfläche |
| 22 | Messuhr | Dial Indicator | Präzisionsmessinstrument zur Messung kleiner Verschiebungen (0.01 mm) |
| 23 | Nadellager | Needle Bearing | Wälzlager mit zylindrischen Rollen (Nadeln) für hohe Radiallast bei kleinem Bauraum |
| 24 | NLGI-Klasse | NLGI Grade | Konsistenzklasse von Schmierfetten (000 = flüssig bis 6 = fest) |
| 25 | O-Ring | O-Ring | Ringförmige Dichtung aus Elastomer (NBR, FKM/Viton) |
| 26 | Pawl Oil | Pawl Oil | Dünnflüssiges Schmieröl speziell für Sperrklinken und deren Federn |
| 27 | Pitting | Pitting | Oberflächenermüdung in Form kleiner Krater auf Lagerflächen oder Zahnflanken |
| 28 | PTFE | PTFE (Polytetrafluoroethylene) | Teflon; wird als Festschmierstoff in Winschfetten verwendet |
| 29 | Riding Turn | Riding Turn | Überwicklung der Schot auf der Winsch, blockiert das Fieren |
| 30 | Self-Tailing | Self-Tailing | Mechanismus, der die Schot automatisch hält, sodass kein zweiter Bediener nötig ist |
| 31 | Solenoid | Solenoid | Elektromechanisches Schaltrelais in elektrischen Winschen |
| 32 | Spaltkorrosion | Crevice Corrosion | Korrosion in engen Spalten, wo Sauerstoff verarmt und Chlorid anreichert |
| 33 | Spannungsrisskorrosion | Stress Corrosion Cracking (SCC) | Rissbildung unter gleichzeitiger Einwirkung von mechanischer Spannung und korrosivem Medium |
| 34 | Stripper Ring | Stripper Ring | Ring oberhalb der Trommel, der die Schot aus dem Self-Tailing löst |
| 35 | Tef-Gel | Tef-Gel | PTFE-basierte Anti-Seize-Paste für Schraubverbindungen verschiedener Metalle |
| 36 | Tribologie | Tribology | Wissenschaft von Reibung, Verschleiß und Schmierung |
| 37 | Trommel | Drum | Äußerer, drehbarer Zylinder der Winsch, um den die Schot gewickelt wird |
| 38 | Tropfpunkt | Dropping Point | Temperatur, bei der ein Schmierfett von fest zu flüssig übergeht |
| 39 | Untersetzung | Gear Ratio | Verhältnis von Eingangs- zu Ausgangsdrehzahl im Getriebe |
| 40 | Viskosität | Viscosity | Maß für die Zähflüssigkeit eines Öls; wird in ISO VG-Klassen angegeben |
| 41 | Winschkurbel | Winch Handle | Abnehmbare Kurbel zum manuellen Betrieb der Winsch |
| 42 | Zahnflanke | Tooth Flank | Kontaktfläche eines Getriebezahns |
| 43 | Zahnkranz | Ratchet Ring / Ring Gear | Gezahnter Ring, in den die Sperrklinken eingreifen |
| 44 | Axialspiel | Axial Play / End Float | Spiel in Längsrichtung der Achse; bestimmt vertikale Beweglichkeit der Trommel |
| 45 | Backing Plate | Backing Plate / Reinforcement Plate | Verstärkungsplatte unter dem Deck zur Lastverteilung der Winschbefestigung |
| 46 | Baugruppe | Assembly / Sub-Assembly | Zusammengesetzte Einheit aus mehreren Einzelteilen (z.B. obere Getriebebaugruppe) |
| 47 | Dichtmasse (Deck) | Deck Sealant | Flexible Dichtmasse (z.B. Sikaflex 291i) zwischen Winschbasis und Deck |
| 48 | Duralac | Duralac | Korrosionsschutz-Paste auf Barium-Chromat-Basis für galvanische Trennung |
| 49 | Elastomer | Elastomer | Gummiartige Kunststoffe für Dichtungen (NBR, EPDM, FKM/Viton) |
| 50 | Festfressen | Galling / Seizing | Verschweißen zweier Metalloberflächen unter Druck (z.B. Edelstahlschraube in Aluminium) |
| 51 | Fressen (Lager-) | Bearing Seizure | Blockieren eines Lagers durch Überhitzung und Materialverformung |
| 52 | Heli-Coil | Heli-Coil / Thread Insert | Gewindeeinsatz zur Reparatur beschädigter Gewinde (Spiralförmige Edelstahl-Buchse) |
| 53 | Kettennuss | Chain Gypsy / Wildcat | Profiliertes Rad in der Ankerwinsch, das die Ankerkette führt |
| 54 | Kontaktkorrosion | Contact Corrosion | Galvanische Korrosion an der Berührungsstelle zweier verschiedener Metalle |
| 55 | Korrosionsschutzöl | Corrosion Inhibiting Oil | Dünnflüssiges Öl mit Korrosionsschutz-Additiven für die Winterlagerung |
| 56 | Lastwechsel | Load Cycle | Wechsel zwischen Be- und Entlastung eines Bauteils; beschleunigt Materialermüdung |
| 57 | Magnetpinzette | Magnetic Tweezers | Pinzette mit magnetischer Spitze zum Greifen kleiner Stahlteile (Nadeln, Federn) |
| 58 | NBR (Nitril-Butadien-Kautschuk) | NBR (Nitrile Butadiene Rubber) | Standard-Dichtungsmaterial für O-Ringe, beständig gegen Öle und Fette |
| 59 | Opferanode | Sacrificial Anode | Zinkanode, die sich statt des zu schützenden Metalls auflöst (kathodischer Schutz) |
| 60 | Passivschicht | Passive Layer | Schützende Oxidschicht auf Edelstahl (Chrom-III-Oxid), die Korrosion verhindert |
| 61 | Planetenrad | Planet Gear | Zahnrad in einem Planetengetriebe, das zwischen Sonnenrad und Ringzahnkranz umläuft |
| 62 | Radialspiel | Radial Clearance | Spiel senkrecht zur Achsrichtung in einem Lager |
| 63 | Rücklaufsicherung | Anti-Reverse Mechanism | System aus Sperrklinken und Zahnkranz, das Rücklauf der Trommel verhindert |
| 64 | Schneckengetriebe | Worm Gear | Getriebetyp mit Schnecke und Schneckenrad; in einigen Spezialwinschen verwendet |
| 65 | Sicherungsringzange | Snap Ring Pliers / Circlip Pliers | Spezialzange zum Öffnen und Schließen von Sicherungsringen |
| 66 | Sonnenrad | Sun Gear | Zentrales Zahnrad im Planetengetriebe |
| 67 | Sprühwachs | Spray Wax | Korrosionsschutz-Beschichtung als Spray für Metalloberflächen |
| 68 | Übersetzungsverhältnis | Gear Ratio | Verhältnis der Drehzahlen im Getriebe; bestimmt Kraftverstärkung vs. Geschwindigkeit |
| 69 | Ultraschallreinigung | Ultrasonic Cleaning | Reinigung durch hochfrequente Schallwellen in einer Reinigungsflüssigkeit |
| 70 | Viton (FKM) | Viton (FKM) | Hochleistungs-Elastomer für O-Ringe, beständig gegen Chemikalien und hohe Temperaturen |

---

## 12. Schnell-Referenz

### 12.1 Wartungs-Schnellreferenzkarte (laminieren und an Bord aufbewahren)

```
╔══════════════════════════════════════════════════════════════════════════╗
║                    WINSCH-WARTUNG SCHNELLREFERENZ                       ║
║                         AYDI v6 / 2026                                 ║
╠══════════════════════════════════════════════════════════════════════════╣
║                                                                        ║
║  NACH JEDEM SEGELN (Salzwasser):                                       ║
║  □ Winschen mit Süßwasser spülen                                      ║
║  □ Trommeln abwischen                                                  ║
║  □ Winschkurbel abnehmen und verstauen                                 ║
║                                                                        ║
║  MONATLICH (bei Nutzung):                                              ║
║  □ Funktionstest 1. + 2. Gang                                         ║
║  □ Self-Tailing mit Schot testen                                      ║
║  □ Sperrklinken-Klick-Geräusch bewerten                               ║
║                                                                        ║
║  QUARTALSWEISE:                                                        ║
║  □ Trommel abnehmen                                                    ║
║  □ Sperrklinken-Federn ölen (2-3 Tropfen)                             ║
║  □ Jaw-Inserts prüfen                                                  ║
║                                                                        ║
║  JÄHRLICH:                                                             ║
║  □ Komplette Demontage                                                 ║
║  □ Reinigung aller Teile (Petroleum/White Spirit)                      ║
║  □ Inspektion nach Checkliste                                          ║
║  □ Neufettung mit Herstellerfett                                       ║
║  □ Sperrklinken-Federn ölen                                            ║
║  □ Self-Tailing-Backen messen                                          ║
║  □ Zusammenbau + Funktionstest                                         ║
║                                                                        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  FETT-ZUORDNUNG:                                                       ║
║  Lager + Achsen + Getriebe    → HERSTELLERFETT                         ║
║  Sperrklinken + Federn        → HERSTELLERÖL (nur wenige Tropfen!)     ║
║  Self-Tailing-Backen          → KEIN FETT / KEIN ÖL!                   ║
║  Befestigungsschrauben        → TEF-GEL                                ║
║                                                                        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  HERSTELLERFETTE:                                                      ║
║  Harken:   White Grease BK4520 + Pawl Oil BK4521                      ║
║  Lewmar:   Winch Grease 19701500 + Winch Oil 19701600                  ║
║  Andersen: Service Grease (Ca-Sulfonat!) + Service Oil                 ║
║  Antal:    Li-Fett (wie Harken) + Pawl Oil                             ║
║                                                                        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  ⚠ NIEMALS:                                                            ║
║  ✗ WD-40 als Schmiermittel    ✗ Fett auf Self-Tailing-Backen           ║
║  ✗ Aceton zur Reinigung       ✗ Hochdruckreiniger auf Winschen         ║
║  ✗ Verschiedene Fette mischen ✗ MoS₂-Fett in Winschen                 ║
║  ✗ Sperrklinken-Federn einzeln tauschen                                ║
║                                                                        ║
╠══════════════════════════════════════════════════════════════════════════╣
║  AUSTAUSCH-GRENZEN:                                                    ║
║  Jaw-Insert Profiltiefe:  <1.0 mm → sofort tauschen                   ║
║  Pawl-Springs:            Feder träge/gebrochen → satzweise tauschen  ║
║  Lagerspiel:              >0.15 mm → Lager tauschen                    ║
║  O-Ringe:                 Hart/rissig → sofort tauschen                ║
║                                                                        ║
╚══════════════════════════════════════════════════════════════════════════╝
```

### 12.2 Notfall-Referenz

```
╔══════════════════════════════════════════════════════════════════════════╗
║  NOTFALL: WINSCH BLOCKIERT UNTER LAST                                  ║
║  1. RUHE BEWAHREN                                                      ║
║  2. Schot NICHT mit Gewalt bewegen                                     ║
║  3. Schot über Klampe oder andere Winsch sichern                       ║
║  4. Last von der Winsch nehmen                                         ║
║  5. WD-40 / Kriechöl einsprühen, 10 min warten                        ║
║  6. Vorsichtig hin und her bewegen                                     ║
╠══════════════════════════════════════════════════════════════════════════╣
║  NOTFALL: RIDING TURN                                                  ║
║  1. SOFORT Last wegnehmen (Kurs ändern, Segel killen)                  ║
║  2. Zweites Schottau auf gleicher Winsch gegenläufig aufwickeln        ║
║  3. Auf dem zweiten Tau kurbeln → erstes Tau löst sich                 ║
║  4. Wenn nichts hilft: Schot kappen (Messer bereit!)                   ║
╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 13. Anhänge A–R

### ANHANG A — Fallstudie: Vernachlässigte Winsch auf Charterboot

**Boot:** Bavaria Cruiser 46, Baujahr 2018
**Standort:** Kaštela Marina, Kroatien
**Winschen:** 6× Lewmar EVO 45ST
**Nutzung:** 35 Charterwochen/Jahr, 350+ Chartergäste über 4 Jahre

**Ausgangssituation (April 2022):**
Die Winschen wurden seit der Auslieferung 2018 nicht gewartet. Chartergäste hatten über Schwergängigkeit geklagt. Eine Großschotwinsch blockierte unter Last während einer Halse bei Starkwind (25 kn).

**Befund bei der Inspektion:**

| Winsch | Zustand | Schweregrad |
|--------|---------|-------------|
| Großschot BB | Blockiert, Achse festgefressen | KRITISCH |
| Großschot StB | Extrem schwergängig, Knirschen | HOCH |
| Genua BB | Schwergängig, Self-Tailing unzuverlässig | MITTEL |
| Genua StB | Schwergängig, Self-Tailing unzuverlässig | MITTEL |
| Spi/Vorsegel BB | Schwergängig | GERING |
| Spi/Vorsegel StB | Schwergängig | GERING |

**Detailbefund Großschotwinsch BB:**
- Zentralachse: Tiefe Riefen (0.3 mm) durch adhäsiven Verschleiß
- Unteres Nadellager: Zerstört (Pitting + Rost)
- Oberes Nadellager: Schwerer Verschleiß, Spiel 0.4 mm
- Pawl-Springs: 3 von 6 gebrochen
- Jaw-Inserts: Profiltiefe 0.5 mm (Neuzustand: 3.5 mm)
- Fett: Vollständig ausgewaschen, Salzablagerungen in allen Lagerstellen

**Reparaturkosten:**

| Position | Kosten |
|----------|--------|
| 2× Achse (Austausch) | 180 EUR |
| 6× Bearing Kit | 288 EUR |
| 6× Spring Kit | 108 EUR |
| 6× Jaw-Insert Kit | 192 EUR |
| 6× O-Ring Kit | 48 EUR |
| Schmiermittel (Lewmar Winch Grease + Oil) | 45 EUR |
| Arbeit Werft (2 Tage) | 960 EUR |
| **Gesamt** | **1.821 EUR** |

**Vergleich: Kosten bei regelmäßiger Wartung (4 Jahre):**

| Position | Kosten |
|----------|--------|
| 4× jährliche Wartung (Material) | 4 × 65 EUR = 260 EUR |
| 1× 4-Jahres-Überholung (Material) | 350 EUR |
| Arbeit (Eigenleistung oder Werft) | 800 EUR |
| **Gesamt** | **1.410 EUR** |

**Ersparnis bei Wartung:** 411 EUR direkt + kein Ausfallrisiko + kein Sicherheitsrisiko

**Lerneffekt:** Die Charterflotte hat nach diesem Vorfall einen monatlichen Wartungsplan für alle Winschen eingeführt.

---

### ANHANG B — Fallstudie: Korrekte Wartung rettet Regatta

**Boot:** J/111, Baujahr 2015
**Standort:** Kieler Förde
**Winschen:** 4× Harken 46.2STC, 2× Harken 40.2STC, 2× Harken 35.2STC
**Nutzung:** 15 Regatten/Saison + Trainingssegeln

**Situation:** Während der Kieler Woche 2024, Kurs 3 (Offshore, 18 kn Wind), riss die Genua-Schot durch den Stripper Ring. Die Schot konnte sofort auf die zweite Winsch umgelegt werden — die Besatzung hatte am Vortag beide Genua-Winschen gewartet und die Jaw-Inserts gegen Harken Performa (BK4515-46) getauscht.

**Wartungsprotokoll vor der Regatta:**
- Alle 8 Winschen: Kurzwartung (Sperrklinken ölen, Funktionstest)
- Genua-Winschen (2× Harken 46.2STC): Komplettwartung + Performa Jaws
- Spi-Winschen (2× Harken 40.2STC): Kurzwartung
- Fall-Winschen (2× Harken 35.2STC): Kurzwartung

**Ergebnis:** 3. Platz Gesamtwertung, kein Winsch-bezogener Ausfall in 5 Tagen Regatta

**Wartungskosten vor der Regatta:**
- 2× Performa Jaw Kit (BK4515-46): 96 EUR
- 1× Harken White Grease (BK4520): 18 EUR
- 1× Harken Pawl Oil (BK4521): 12 EUR
- Arbeit (Eigenleistung, 4 Stunden): 0 EUR
- **Gesamt: 126 EUR**

---

### ANHANG C — Fallstudie: Winterlagerung schief gelaufen

**Boot:** Hallberg-Rassy 372, Baujahr 2008
**Standort:** Travemünde
**Winschen:** 4× Lewmar EVO 40ST (original seit 2008)
**Problem:** Nach der Winterlagerung 2023/2024 waren alle Winschen festgefressen

**Ursache:** Die Winschen wurden im Herbst nicht gewartet. Das Boot lag ohne Persenning im Freien. Regenwasser, Frost-Tau-Zyklen und Salzkristallreste (Boot war vorher in der Ostsee) führten zu:
1. Korrosion der Achsen (Rost in den Lagersitzen)
2. Verhärtung des alten Fetts (Mineral-Fett + Kälte = Zement-artig)
3. Sperrklinken-Federn korrodiert (2 von 24 gebrochen)

**Reparatur:**
- 4× Komplettwartung mit Reinigung (Ultraschallbad)
- 4× Spring Kit (19700103): 72 EUR
- 4× O-Ring Kit: 32 EUR
- Lewmar Winch Grease + Oil: 35 EUR
- Arbeit (Eigenleistung, 8 Stunden): 0 EUR
- **Gesamt: 139 EUR** (Material)

**Prävention für die Zukunft:**
- Herbst-Komplettwartung (Reinigung + Neufettung)
- Korrosionsschutz-Spray auf Trommeln
- Winschkurbel-Aufnahmen abdecken
- Persenning mit Belüftung

---

### ANHANG D — Fallstudie: Galvanische Korrosion durch falsche Montage

**Boot:** Dehler 42, Baujahr 2020
**Standort:** Mittelmeer (Mallorca)
**Winschen:** 2× Andersen 46ST Compact (neu montiert 2022)
**Problem:** Nach 18 Monaten Korrosion an der Winsch-Basis (Aluminium)

**Ursache:** Bei der Montage wurden Edelstahl-Schrauben (A4) ohne Isolierung direkt in die Aluminium-Basis geschraubt. Kein Tef-Gel, keine Isolierscheiben. Im Mittelmeer (hoher Salzgehalt) → galvanische Korrosion des Aluminiums.

**Befund:**
- Aluminium-Basis: Weiße Korrosionsprodukte (Aluminiumoxid-Hydroxid)
- Schraubengewinde: Festgefressen
- Edelstahl-Schrauben: Keine Korrosion (Kathode im galvanischen Element)

**Reparatur:**
- Schrauben herausbohren (3 von 8 nicht lösbar)
- Gewinde mit Heli-Coil reparieren
- Neumonatte mit Tef-Gel und Isolierscheiben
- Kosten: 680 EUR (inkl. Werft-Arbeit)

**Prävention:**
- IMMER Tef-Gel auf Schrauben bei gemischten Metallen
- Isolierscheiben zwischen Edelstahl und Aluminium
- Regelmäßige Kontrolle der Basis-Befestigung
- Im Mittelmeer: Häufigeres Süßwasser-Spülen

---

### ANHANG E — Fallstudie: Sperrklinken-Ausfall bei Starkwind

**Boot:** Beneteau First 40.7, Baujahr 2005
**Standort:** Nordsee (Helgoland → Cuxhaven)
**Winschen:** 2× Lewmar 48ST (Genua-Winschen)
**Situation:** Bei 32 kn Wind, Kurs am Wind, Reffen. Die Genua-Winsch (Luv) ließ plötzlich die Schot durchlaufen — die Genua schlug gewaltsam nach Lee.

**Ursache:** Alle 3 oberen Sperrklinken waren durch verhärtetes Fett blockiert. Das Fett war 6 Jahre alt und durch Salzeinwirkung verhärtet. Die Sperrklinken konnten nicht in den Zahnkranz eingreifen.

**Folgen:**
- Genua in der Saling gefangen (1.200 EUR Segelreparatur)
- Crew-Mitglied leicht verletzt (Schotrückschlag)
- Psychologischer Effekt auf die Crew

**Reparatur der Winsch:** 45 Minuten (Reinigung, Neufettung) — Winsch selbst war nicht beschädigt

**Lehre:** Sperrklinken dürfen NIEMALS mit Fett geschmiert werden, sondern NUR mit dünnflüssigem Öl. Fett kann verhärten und die Sperrklinken blockieren — ein lebensgefährliches Versagen.

---

### ANHANG F — Fallstudie: Erfolgreiche Eigenleistungs-Wartung über 20 Jahre

**Boot:** Hallberg-Rassy 36 Mk II, Baujahr 2004
**Eigner:** Seit Neubau, 20 Jahre Eigenleistungs-Wartung
**Winschen:** 4× Andersen 40ST Compact, 2× Andersen 28ST Compact
**Nutzung:** 4 Monate/Jahr Ostsee, 1 Monat Mittelmeer (alle 3 Jahre)

**Wartungsprotokoll über 20 Jahre:**
- 20× jährliche Komplettwartung (Eigenleistung)
- 4× 5-Jahres-Generalüberholung (Eigenleistung)
- Pawl-Springs: 4× getauscht (alle 5 Jahre)
- Jaw-Inserts: 3× getauscht (alle 6–7 Jahre)
- Lager: 1× getauscht (nach 15 Jahren)
- O-Ringe: 6× getauscht (alle 3–4 Jahre)

**Gesamtkosten über 20 Jahre:**
- Schmiermittel (Andersen Service Grease + Oil): 20 × 15 EUR = 300 EUR
- Pawl-Spring Kits: 4 × 6 × 22 EUR = 528 EUR
- Jaw-Insert Kits: 3 × 6 × 35 EUR = 630 EUR
- Bearing Kits: 1 × 6 × 42 EUR = 252 EUR
- O-Ring Kits: 6 × 6 × 10 EUR = 360 EUR
- Werkzeug (einmalig): 150 EUR
- **Gesamt über 20 Jahre: 2.220 EUR** (111 EUR/Jahr)

**Zustand nach 20 Jahren:** Alle Winschen voll funktionsfähig, geschätzte Restlebensdauer 10+ Jahre

**Vergleichsrechnung:** Neue Andersen 40ST Compact: ca. 1.400 EUR/Stück × 4 = 5.600 EUR. Der Eigner hat durch konsequente Wartung den Austausch aller 4 Hauptwinschen vermieden. (Confidence: documented — Neupreis-Tabelle FAQ F30, extern bestätigt durch Händlerpreis SVB.)

> ✅ **Aufgelöst (Audit):** Andersen 40ST Compact = 1.400 EUR/Stück (× 4 = 5.600 EUR); die vorherige Angabe 2.100 EUR war ein Zahlendreher (entspricht Harken Radial 50ST in FAQ F30). Quelle: dokumenteigene Neupreis-Tabelle FAQ F30 + Händlerpreis SVB (Andersen 40ST FS Self-Tailing 2-speed ≈ 1.300 EUR, svb24.com).

---

### ANHANG G — Fallstudie: Elektrische Winsch — Solenoid-Versagen

**Boot:** Jeanneau Sun Odyssey 440, Baujahr 2021
**Standort:** Adria (Kroatien)
**Winschen:** 2× Harken 46.2STEC (elektrisch, Genua)
**Situation:** Steuerbord-Genua-Winsch reagiert nicht auf Knopfdruck (2. Saison)

**Diagnose:**
1. Sicherung OK → ✓
2. Hauptschalter ON → ✓
3. Spannung am Solenoid: 12.4V → ✓
4. Solenoid klickt nicht → DEFEKT
5. Motor-Überbrückung (direkt 12V): Motor läuft → Motor OK

**Ursache:** Solenoid-Kontakte durch Feuchtigkeit und Salz korrodiert. Die Solenoid-Box war nicht ausreichend abgedichtet (Herstellerproblem bei frühen 2021er Modellen).

**Reparatur:**
- Solenoid ersetzt (Harken Original-Ersatzteil)
- Solenoid-Box mit Silikondichtung abgedichtet
- Kosten: 180 EUR (Solenoid) + 80 EUR (Arbeit) = 260 EUR

**Prävention:**
- Solenoid-Box regelmäßig auf Feuchtigkeit prüfen
- Elektrische Kontakte mit Kontaktspray (z.B. Ballistol Kontaktreiniger) behandeln
- Kabelverbindungen auf Korrosion prüfen (jährlich)

---

### ANHANG H — Fallstudie: Überlast-Schaden durch falschen Schotdurchmesser

**Boot:** X-Yachts X4.3, Baujahr 2019
**Standort:** Flensburger Förde
**Winschen:** 2× Harken 50.2STC (Genua)
**Situation:** Eigner hatte aus Kostengrund 14 mm Schoten statt der empfohlenen 12 mm montiert

**Problem:** Die dickere Schot erhöhte den effektiven Wickelradius auf der Trommel → höhere Belastung der inneren Mechanik pro Schotzug. Zusätzlich passte die Schot nicht optimal in den Self-Tailing-Bereich.

**Folgen nach 2 Saisons:**
- Getriebezähne zeigten vorzeitigen Verschleiß (Pitting)
- Self-Tailing unzuverlässig (falscher Durchmesser)
- Trommelrillen stärker verschlissen als normal

**Reparatur:**
- Getriebe-Zahnräder ausgetauscht: 320 EUR/Winsch
- Richtige 12 mm Schoten montiert: 180 EUR
- Arbeit: 350 EUR
- **Gesamt: 1.170 EUR**

**Lehre:** IMMER den vom Hersteller empfohlenen Schotdurchmesser verwenden. Die Winsch ist für einen bestimmten Durchmesserbereich optimiert.

**Harken Schotdurchmesser-Empfehlung:**

| Winschgröße | Min. Durchmesser | Max. Durchmesser | Optimal |
|-------------|-----------------|-----------------|---------|
| Size 35 | 8 mm | 12 mm | 10 mm |
| Size 40 | 8 mm | 14 mm | 10–12 mm |
| Size 46 | 10 mm | 14 mm | 12 mm |
| Size 48 | 10 mm | 14 mm | 12 mm |
| Size 50 | 10 mm | 16 mm | 12–14 mm |
| Size 60 | 12 mm | 18 mm | 14–16 mm |
| Size 70 | 14 mm | 20 mm | 16–18 mm |

---

### ANHANG I — Pydantic v2 Datenmodelle für Winsch-Wartung

```python
"""
AYDI Winch Maintenance Data Models — Pydantic v2
Wissensdatei: 09_07_winschen_wartung.md
"""

from datetime import date, datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class WinchBrand(str, Enum):
    """Unterstützte Winsch-Hersteller."""
    HARKEN = "harken"
    LEWMAR = "lewmar"
    ANDERSEN = "andersen"
    ANTAL = "antal"
    OTHER = "other"


class GreaseType(str, Enum):
    """Verdicker-Typ des Schmierfetts."""
    LITHIUM = "lithium"
    LITHIUM_COMPLEX = "lithium_complex"
    CALCIUM_SULFONATE = "calcium_sulfonate"
    BARIUM = "barium"
    PTFE = "ptfe"
    OTHER = "other"


class MaintenanceLevel(str, Enum):
    """Wartungsstufe."""
    QUICK = "quick"           # Kurzwartung (Sperrklinken ölen)
    STANDARD = "standard"     # Standardwartung (Demontage, Reinigung, Neufettung)
    MAJOR = "major"           # Generalüberholung (alles inkl. Basis)
    EMERGENCY = "emergency"   # Notfallreparatur


class WearPartStatus(str, Enum):
    """Verschleißteil-Zustand."""
    NEW = "new"               # Neuzustand
    GOOD = "good"             # Gut, kein Austausch nötig
    WORN = "worn"             # Verschlissen, Austausch empfohlen
    CRITICAL = "critical"     # Kritisch, sofortiger Austausch
    FAILED = "failed"         # Ausgefallen


class FailurePatternID(str, Enum):
    """Fehlerbild-Identifikation."""
    F01_NO_RATCHET = "f01_no_ratchet"
    F02_GRINDING = "f02_grinding"
    F03_SELF_TAILING_SLIP = "f03_self_tailing_slip"
    F04_JAMMED = "f04_jammed"
    F05_STIFF = "f05_stiff"
    F06_ONE_SPEED_ONLY = "f06_one_speed_only"
    F07_DRUM_CORROSION = "f07_drum_corrosion"
    F08_ABNORMAL_NOISE = "f08_abnormal_noise"
    F09_UNEVEN_WRAP = "f09_uneven_wrap"
    F10_ELECTRIC_NO_RESPONSE = "f10_electric_no_response"
    F11_STUCK_BOLTS = "f11_stuck_bolts"
    F12_VIBRATION = "f12_vibration"


class ConfidenceLevel(str, Enum):
    """AYDI Confidence-Level für Wartungsbefunde."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    ESTIMATED = "estimated"
    DOCUMENTED = "documented"
    BENCHMARK = "benchmark"


class WinchIdentification(BaseModel):
    """Identifikation einer Winsch."""
    model_config = {"from_attributes": True}

    brand: WinchBrand
    model: str = Field(..., description="Modellbezeichnung (z.B. 'Radial 46.2STC')")
    size: int = Field(..., ge=6, le=120, description="Winschgröße (Herstellerangabe)")
    serial_number: Optional[str] = None
    year_manufactured: Optional[int] = Field(None, ge=1970, le=2030)
    year_installed: Optional[int] = Field(None, ge=1970, le=2030)
    is_electric: bool = False
    is_self_tailing: bool = True
    speeds: int = Field(2, ge=1, le=3, description="Anzahl Gänge")
    position: Optional[str] = Field(None, description="Position am Boot (z.B. 'Genua BB')")


class GreaseSpecification(BaseModel):
    """Schmierfett-Spezifikation."""
    model_config = {"from_attributes": True}

    product_name: str
    manufacturer: str
    part_number: str
    grease_type: GreaseType
    nlgi_grade: float = Field(..., ge=0, le=6)
    temperature_min_celsius: float
    temperature_max_celsius: float
    dropping_point_celsius: Optional[float] = None
    water_resistance: str = Field(..., description="Ausgezeichnet/Gut/Befriedigend/Mangelhaft")
    contains_ptfe: bool = False
    contains_ep_additives: bool = False
    color: str
    price_per_100g_eur: Optional[float] = None
    shelf_life_months_unopened: int = Field(36, ge=6, le=120)


class OilSpecification(BaseModel):
    """Schmieröl-Spezifikation."""
    model_config = {"from_attributes": True}

    product_name: str
    manufacturer: str
    part_number: str
    viscosity_iso_vg: int
    temperature_min_celsius: float
    temperature_max_celsius: float
    color: str
    application: str = Field(..., description="Anwendungsbereich")
    price_per_unit_eur: Optional[float] = None


class WearPartInspection(BaseModel):
    """Verschleißteil-Inspektion."""
    model_config = {"from_attributes": True}

    part_name: str
    part_number: Optional[str] = None
    status: WearPartStatus
    measurement_value: Optional[float] = None
    measurement_unit: Optional[str] = None
    threshold_good: Optional[float] = None
    threshold_critical: Optional[float] = None
    notes: Optional[str] = None
    replacement_recommended: bool = False
    estimated_remaining_life_months: Optional[int] = None
    confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_MEDIUM


class MaintenanceRecord(BaseModel):
    """Wartungsprotokoll einer einzelnen Winsch."""
    model_config = {"from_attributes": True}

    id: Optional[str] = None
    winch: WinchIdentification
    maintenance_date: date
    maintenance_level: MaintenanceLevel
    performed_by: str = Field(..., description="Ausführender (Name oder 'Eigenleistung')")
    grease_used: Optional[GreaseSpecification] = None
    oil_used: Optional[OilSpecification] = None
    wear_part_inspections: list[WearPartInspection] = Field(default_factory=list)
    parts_replaced: list[str] = Field(default_factory=list, description="Ersetzte Teile (Art.-Nr.)")
    torque_applied_nm: Optional[dict[str, float]] = None
    idle_torque_nm: Optional[float] = Field(None, description="Leerlauf-Drehmoment nach Wartung")
    functional_test_passed: bool = True
    self_tailing_test_passed: Optional[bool] = None
    failure_patterns_found: list[FailurePatternID] = Field(default_factory=list)
    notes: Optional[str] = None
    next_maintenance_due: Optional[date] = None
    total_cost_eur: Optional[float] = None
    labor_hours: Optional[float] = None
    photos_before: list[str] = Field(default_factory=list, description="Foto-Pfade (vorher)")
    photos_after: list[str] = Field(default_factory=list, description="Foto-Pfade (nachher)")
    confidence: ConfidenceLevel = ConfidenceLevel.DOCUMENTED


class WinchConditionAssessment(BaseModel):
    """Zustandsbewertung einer Winsch (AYDI-Analyse)."""
    model_config = {"from_attributes": True}

    winch: WinchIdentification
    assessment_date: date
    overall_score: int = Field(..., ge=0, le=100, description="Gesamtzustand 0-100")
    mechanical_score: int = Field(..., ge=0, le=100, description="Mechanischer Zustand")
    corrosion_score: int = Field(..., ge=0, le=100, description="Korrosionszustand (100=kein Korrosion)")
    lubrication_score: int = Field(..., ge=0, le=100, description="Schmierzustand")
    self_tailing_score: Optional[int] = Field(None, ge=0, le=100)
    wear_parts: list[WearPartInspection] = Field(default_factory=list)
    failure_patterns: list[FailurePatternID] = Field(default_factory=list)
    maintenance_urgency: str = Field(..., description="sofort/bald/planmäßig/kein_bedarf")
    recommended_actions: list[str] = Field(default_factory=list)
    estimated_remaining_life_years: Optional[float] = None
    estimated_maintenance_cost_eur: Optional[float] = None
    confidence: ConfidenceLevel
    assessor: str = Field(default="AYDI v6")
    model_version: str = Field(default="09.07.1.0")


class FleetMaintenancePlan(BaseModel):
    """Flottenweiter Wartungsplan für alle Winschen eines Bootes."""
    model_config = {"from_attributes": True}

    boat_name: str
    boat_type: str
    boat_length_m: float
    usage_area: str = Field(..., description="Binnenrevier/Küste/Hochsee/Tropen")
    usage_weeks_per_year: int = Field(..., ge=1, le=52)
    winches: list[WinchIdentification]
    maintenance_schedule: dict[str, str] = Field(
        default_factory=dict,
        description="Wartungsplan: {'nach_einsatz': '...', 'monatlich': '...', ...}"
    )
    annual_budget_eur: Optional[float] = None
    spare_parts_inventory: list[str] = Field(default_factory=list)
    last_updated: date = Field(default_factory=date.today)


class MaintenanceChecklistItem(BaseModel):
    """Einzelner Punkt einer Wartungs-Checkliste."""
    model_config = {"from_attributes": True}

    step_number: int
    description_de: str
    description_en: Optional[str] = None
    tool_required: Optional[str] = None
    measurement_required: bool = False
    measurement_spec: Optional[str] = None
    pass_criteria: Optional[str] = None
    duration_minutes: Optional[int] = None
    is_critical: bool = False
    notes: Optional[str] = None


class MaintenanceChecklist(BaseModel):
    """Vollständige Wartungs-Checkliste."""
    model_config = {"from_attributes": True}

    name: str
    maintenance_level: MaintenanceLevel
    applicable_brands: list[WinchBrand]
    items: list[MaintenanceChecklistItem]
    total_duration_minutes: Optional[int] = None
    tools_required: list[str] = Field(default_factory=list)
    consumables_required: list[str] = Field(default_factory=list)
    safety_warnings: list[str] = Field(default_factory=list)
```

---

### ANHANG J — Wartungs-Checkliste: Jährliche Komplettwartung

**Checkliste für jährliche Komplettwartung (2-Gang Self-Tailing Winsch)**

```
WINSCH-WARTUNG — JAHRES-CHECKLISTE
Datum: ____________  Boot: ____________  Winsch-Position: ____________
Hersteller/Modell: ____________  Größe: ____________

VORBEREITUNG
□ Schoten entfernt
□ Winschkurbel entfernt
□ Arbeitsbereich vorbereitet (Matte, Wanne, Beutel)
□ Werkzeug bereitgelegt
□ Schmiermittel bereitgelegt (Fett: __________ / Öl: __________)
□ Foto-Dokumentation: Ausgangszustand aufgenommen

DEMONTAGE
□ Self-Tailing-Oberteil entfernt
□ Jaw-Inserts entnommen (Anzahl: ___ / Position notiert)
□ Trommel abgenommen
□ Obere Sperrklinken + Federn entnommen (Beutel "OBEN")
□ Obere Getriebebaugruppe entnommen
□ Untere Sperrklinken + Federn entnommen (Beutel "UNTEN")
□ Untere Getriebebaugruppe entnommen
□ Lager entnommen (markiert: oben/unten)

REINIGUNG
□ Alle Teile in Petroleum/White Spirit eingelegt
□ Altes Fett vollständig entfernt (Pinsel + Lappen)
□ Teile mit sauberem Lappen getrocknet
□ Trommel-Innenseite gereinigt
□ Basis gereinigt (in situ)

INSPEKTION
□ Achse: Oberfläche glatt, keine Riefen .............. OK / NOK
□ Achse: Durchmesser gemessen: _____ mm (Soll: _____ mm) OK / NOK
□ Oberes Lager: Spiel _____ mm (max: 0.15 mm) ........ OK / NOK
□ Unteres Lager: Spiel _____ mm (max: 0.15 mm) ....... OK / NOK
□ Lager: Oberflächen glatt, kein Pitting .............. OK / NOK
□ Obere Sperrklinken: Kanten scharf ................... OK / NOK
□ Untere Sperrklinken: Kanten scharf .................. OK / NOK
□ Obere Federn: Elastisch, nicht verformt ............. OK / NOK
□ Untere Federn: Elastisch, nicht verformt ............ OK / NOK
□ Zahnkranz: Flanken ohne Verschleiß ................. OK / NOK
□ Getriebezähne: Flanken ohne Pitting ................. OK / NOK
□ O-Ringe: Elastisch, keine Risse ..................... OK / NOK
□ Jaw-Inserts: Profiltiefe _____ mm (min: 1.0 mm) .... OK / NOK
□ Trommel: Oberfläche gleichmäßig, kein Pitting ....... OK / NOK
□ Basis: Keine Korrosion, kein Lochfraß ............... OK / NOK
□ Befestigungsschrauben: Gewinde in Ordnung ........... OK / NOK

TEILE GETAUSCHT (falls zutreffend):
□ Pawl-Springs (Art.-Nr.: ____________)
□ Jaw-Inserts (Art.-Nr.: ____________)
□ O-Ringe (Art.-Nr.: ____________)
□ Lager (Art.-Nr.: ____________)
□ Sonstige: ____________

SCHMIERUNG + ZUSAMMENBAU
□ Achse dünn gefettet
□ Unteres Lager gefettet und eingesetzt
□ Untere Getriebebaugruppe gefettet und eingesetzt
□ Untere Sperrklinken + Federn eingesetzt, geölt
□ Oberes Lager gefettet und eingesetzt
□ Obere Getriebebaugruppe gefettet und eingesetzt
□ Obere Sperrklinken + Federn eingesetzt, geölt
□ Trommel-Innenseite dünn gefettet
□ Trommel aufgesetzt und gesichert
□ Jaw-Inserts eingesetzt
□ Self-Tailing-Oberteil montiert

FUNKTIONSTEST
□ Uhrzeigersinn: Leichtgängig, gleichmäßig ........... OK / NOK
□ Gegen Uhrzeigersinn: Gesperrt (Klick-Klick) ........ OK / NOK
□ 1. Gang (schnell): Funktioniert ..................... OK / NOK
□ 2. Gang (langsam): Untersetzung spürbar ............. OK / NOK
□ Self-Tailing: Schot wird sicher gehalten ............ OK / NOK
□ Befestigungsschrauben: Drehmoment _____ Nm (Tef-Gel) OK / NOK
□ Leerlauf-Drehmoment geschätzt: _____ Nm

□ Foto-Dokumentation: Endzustand aufgenommen

UNTERSCHRIFT: ____________  NÄCHSTE WARTUNG FÄLLIG: ____________
```

---

### ANHANG K — Werkzeugliste für Winsch-Wartung

#### K.1 Grundwerkzeug (Heimwerker-Bordwerkzeug)

| Nr. | Werkzeug | Spezifikation | Ersatz möglich? | Priorität |
|-----|----------|---------------|-----------------|-----------|
| 1 | Innensechskant-Satz | 2, 2.5, 3, 4, 5, 6, 8 mm | Nein | Pflicht |
| 2 | Ring-Maulschlüssel-Satz | 8, 10, 13, 17, 19 mm | Nein | Pflicht |
| 3 | Schraubendreher PH | PH1, PH2 | Nein | Pflicht |
| 4 | Schraubendreher Schlitz | 4 mm, 6 mm | Nein | Pflicht |
| 5 | Sicherungsringzange (extern) | Für Circlips 10–30 mm | Bedingt (spitze Zange) | Pflicht |
| 6 | Pinzette | Gerade, 150 mm | Nein | Pflicht |
| 7 | Pinzette | Gebogen, 150 mm | Bedingt | Empfohlen |
| 8 | Taschenlampe LED | Fokussierbar, 200+ Lumen | Nein | Pflicht |
| 9 | Lupe | 10x, Taschenlupe | Nein | Empfohlen |
| 10 | Messschieber | 0–150 mm, 0.05 mm | Nein | Pflicht |
| 11 | Reinigungspinsel | 3 Größen (klein/mittel/groß) | Nein | Pflicht |
| 12 | Lappen (fusselarm) | 10+ Stück | Nein | Pflicht |
| 13 | Auffangwanne | Kunststoff, flach, 40×30 cm | Bedingt (Eimer) | Pflicht |
| 14 | Magnetschale | Edelstahl, 10 cm Ø | Bedingt (Beutel) | Empfohlen |
| 15 | Beschriftete Ziplock-Beutel | 10+ Stück | Nein | Pflicht |
| 16 | Marker (wasserfest) | Fein | Nein | Pflicht |
| 17 | Smartphone/Kamera | Für Dokumentation | Nein | Empfohlen |

#### K.2 Erweitertes Werkzeug (Profi / Blauwasser)

| Nr. | Werkzeug | Spezifikation | Priorität |
|-----|----------|---------------|-----------|
| 18 | Drehmomentschlüssel | 5–50 Nm, 3/8" Antrieb | Empfohlen |
| 19 | Torx-Bit-Satz | T10, T15, T20, T25, T30 | Pflicht (Andersen) |
| 20 | Federwaage | 0–5 N, 0.1 N Auflösung | Optional |
| 21 | Fühlerlehre | 0.05–1.0 mm | Empfohlen |
| 22 | Messuhr mit Magnetstativ | 0–10 mm, 0.01 mm | Optional |
| 23 | Mikrometer | 0–25 mm, 0.01 mm | Optional |
| 24 | Kunststoffhammer | 250 g | Empfohlen |
| 25 | Schraubenausdreher-Satz | M3–M10 | Empfohlen |
| 26 | Gewindebohrer-Satz | M4, M5, M6, M8 | Blauwasser |
| 27 | Heli-Coil-Satz | M6, M8 | Blauwasser |
| 28 | Multimeter | Digital, AC/DC | Pflicht (E-Winschen) |

---

### ANHANG L — AYDI Zustandsprotokoll-Vorlage

```
AYDI WINSCH-ZUSTANDSPROTOKOLL v1.0

Datum: ____________  Prüfer: ____________
Boot: ____________  Typ: ____________  Länge: _____ m

WINSCH-INVENTAR:

| Nr. | Position | Hersteller | Modell | Größe | Bj. | Elektr. | ST |
|-----|----------|-----------|--------|-------|-----|---------|-----|
| 1   |          |           |        |       |     | J/N     | J/N |
| 2   |          |           |        |       |     | J/N     | J/N |
| 3   |          |           |        |       |     | J/N     | J/N |
| 4   |          |           |        |       |     | J/N     | J/N |
| 5   |          |           |        |       |     | J/N     | J/N |
| 6   |          |           |        |       |     | J/N     | J/N |
| 7   |          |           |        |       |     | J/N     | J/N |
| 8   |          |           |        |       |     | J/N     | J/N |

ZUSTANDSBEWERTUNG (je Winsch):

Winsch Nr. ___  Position: ____________

| Kriterium | Bewertung (1-5) | Anmerkung |
|-----------|-----------------|-----------|
| Leichtgängigkeit | | |
| Sperrklinken-Funktion | | |
| Self-Tailing-Grip | | |
| Trommel-Zustand | | |
| Korrosion | | |
| Geräusche | | |
| Vibration | | |
| Befestigung | | |

Bewertungsskala: 1=Mangelhaft, 2=Ausreichend, 3=Befriedigend, 4=Gut, 5=Sehr gut

Gesamtbewertung: ___/40 Punkte

Empfehlung:
□ Kein Handlungsbedarf
□ Planmäßige Wartung ausreichend
□ Baldige Wartung empfohlen (innerhalb 3 Monate)
□ Sofortige Wartung erforderlich
□ Professioneller Service empfohlen

Letzte Wartung: ____________  Nächste empfohlene Wartung: ____________
```

---

### ANHANG M — Schmiermittel-Verträglichkeitsmatrix (Druckvorlage)

```
SCHMIERFETT-VERTRÄGLICHKEITSMATRIX — WINSCH-WARTUNG

              Li    Li-K   Ca    Ca-S   Ba    PTFE
Lithium       ✓✓    ✓      ⚠     ✗✗     ✗     ✓
Li-Komplex    ✓     ✓✓     ⚠     ✗✗     ⚠     ✓
Calcium       ⚠     ⚠      ✓✓    ⚠      ✗     ✓
Ca-Sulfonat   ✗✗    ✗✗     ⚠     ✓✓     ⚠     ✓
Barium        ✗     ⚠      ✗     ⚠      ✓✓    ✓
PTFE          ✓     ✓      ✓     ✓      ✓     ✓✓

✓✓ = Voll verträglich    ✓ = Verträglich
⚠  = Begrenzt (kurzfr.)  ✗ = Nicht verträglich
✗✗ = Keinesfalls mischen!

ZUORDNUNG HERSTELLER → VERDICKER-TYP:
Harken White Grease (BK4520) ......... Lithium-Komplex
Lewmar Winch Grease (19701500) ....... Lithium
Andersen Service Grease .............. Calcium-Sulfonat
Winch-Mate ........................... Lithium

⚠ ANDERSEN-FETT IST NICHT KOMPATIBEL MIT HARKEN/LEWMAR! ⚠
Bei Wechsel: altes Fett VOLLSTÄNDIG entfernen!
```

---

### ANHANG N — Drehmoment-Referenztabelle

| Schraubengröße | Material | Trocken (Nm) | Mit Tef-Gel (Nm) | Anwendung |
|----------------|----------|-------------|------------------|-----------|
| M4 | Edelstahl A4 | 2.5–3.5 | 2.0–3.0 | Jaw-Insert-Schrauben |
| M5 | Edelstahl A4 | 5.0–7.0 | 4.0–6.0 | Deckel-Schrauben |
| M6 | Edelstahl A4 | 8.0–11.0 | 7.0–9.0 | Self-Tailing-Befestigung |
| M8 | Edelstahl A4 | 20.0–25.0 | 16.0–22.0 | Basis-Befestigung (Standard) |
| M10 | Edelstahl A4 | 35.0–45.0 | 28.0–38.0 | Basis-Befestigung (große Winschen) |
| M12 | Edelstahl A4 | 55.0–70.0 | 45.0–60.0 | Basis-Befestigung (Superyacht) |

**Hinweise:**
- Werte gelten für metrisches ISO-Gewinde
- Bei Aluminium-Gewinde: 60 % der Tabellenwerte verwenden!
- IMMER Tef-Gel oder Duralac verwenden (Korrosionsschutz + definierter Reibwert)
- Bei Unsicherheit: Hersteller-Angabe hat Vorrang

---

### ANHANG O — Saisonaler Wartungskalender

```
WINSCH-WARTUNGSKALENDER (Nordeuropa, Saisonbetrieb April–Oktober)

JANUAR
  □ Ersatzteile für die kommende Saison bestellen
  □ Herstellerfett/Öl-Vorrat prüfen, ggf. nachbestellen

FEBRUAR
  □ —

MÄRZ
  □ Winterlager: Winschen visuell prüfen (Korrosion?)
  □ Werkzeug zusammenstellen

APRIL — SAISONSTART
  □ ★ Frühjahrswartung (Stufe B):
    □ Alle Winschen demontieren, reinigen, inspizieren
    □ Verschleißteile beurteilen und ggf. tauschen
    □ Neufettung mit Herstellerfett
    □ Sperrklinken ölen
    □ Self-Tailing-Backen prüfen
    □ Funktionstest aller Gänge und Self-Tailing
    □ Befestigungsmomente prüfen
    □ Wartungsprotokoll erstellen

MAI
  □ Nach den ersten 3–5 Segeltörns: Kontrollcheck
    □ Läuft alles rund? Geräusche? Self-Tailing OK?

JUNI
  □ Kurzwartung (Stufe A):
    □ Trommel abnehmen
    □ Sperrklinken-Federn ölen
    □ Jaw-Inserts sichtprüfen
    □ Trommel aufsetzen, Funktionstest

JULI
  □ Vor längeren Törns / Regatten:
    □ Kurzwartung aller Winschen
    □ Ersatzteile an Bord prüfen

AUGUST
  □ Kurzwartung (Stufe A) — wie Juni

SEPTEMBER
  □ Kurzwartung (Stufe A) — wie Juni
  □ Ersatzteile-Bedarf für Herbstwartung identifizieren

OKTOBER — SAISONENDE
  □ ★ Herbstwartung (Stufe B/C):
    □ Alle Winschen komplett demontieren
    □ Gründliche Reinigung (Petroleum-Bad)
    □ Ausführliche Inspektion nach Checkliste (Anhang J)
    □ Verschleißteile tauschen
    □ Neufettung (reichlich — Winterschutz)
    □ Korrosionsschutz auf Trommeln
    □ Winschkurbel-Aufnahmen abdecken
    □ Wartungsprotokoll erstellen

NOVEMBER
  □ Ersatzteile bestellen (für Frühjahrswartung)
  □ 5-Jahres-Überholung fällig? → Termin bei Werft/Rigger

DEZEMBER
  □ —
```

---

### ANHANG P — Fehlerbild-Schnellreferenz (Tabelle)

| Code | Symptom | Schwere | Häufigste Ursache | Sofortmaßnahme |
|------|---------|---------|-------------------|----------------|
| F01 | Kein Sperrklicken | KRITISCH | Federn gebrochen | Nutzung stoppen! |
| F02 | Knirschen/Kratzen | MITTEL–HOCH | Schmiermittelmangel | Baldige Wartung |
| F03 | Self-Tailing rutscht | MITTEL | Jaw-Inserts verschlissen | Jaw-Inserts prüfen/tauschen |
| F04 | Blockiert unter Last | KRITISCH | Lagerfressen | Last wegnehmen, Kriechöl |
| F05 | Schwergängig | GERING–MITTEL | Altes/verhärtetes Fett | Wartung planen |
| F06 | Ein Gang fehlt | MITTEL | Sperrklinken blockiert | Demontage, Reinigung |
| F07 | Trommel-Korrosion | GERING–MITTEL | Salzwasser + fehlende Pflege | Reinigen, konservieren |
| F08 | Klappern/Schlagen | MITTEL | Loses Teil, Lagerspiel | Demontage, Inspektion |
| F09 | Ungleichmäßiger Wickel | GERING–MITTEL | Verschlissene Rillen, falsche Schot | Ursache prüfen |
| F10 | E-Winsch ohne Reaktion | MITTEL–HOCH | Sicherung/Solenoid | Sicherung prüfen |
| F11 | Schrauben festsitzend | GERING | Galvanische Korrosion | Kriechöl, Geduld |
| F12 | Vibration unter Last | MITTEL–HOCH | Lose Basis/Backing Plate | Befestigung prüfen |

---

### ANHANG Q — Häufige Fehler-Fehlerbehebungs-Zuordnung

| Häufiger Fehler bei Wartung | Was passiert | Korrekte Vorgehensweise |
|----------------------------|-------------|------------------------|
| Sperrklinken vertauscht (oben↔unten) | Gänge arbeiten falsch oder gar nicht | Teile beim Zerlegen beschriften: "OBEN"/"UNTEN" |
| Federn vergessen einzusetzen | Sperrklinken federn nicht zurück → DURCHRUTSCHEN! | Checkliste verwenden, Funktionstest! |
| Zu viel Fett auf Sperrklinken | Sperrklinken kleben, reagieren träge | NUR Öl auf Sperrklinken/Federn! |
| Self-Tailing-Backen gefettet | Schot rutscht durch | NIEMALS Fett auf Jaw-Inserts |
| Nadellager verkippt eingesetzt | Klemmen, Schwergängigkeit | Lager gerade und vorsichtig einsetzen |
| Trommel mit Gewalt aufgesetzt | Sperrklinken brechen, Lager beschädigt | Trommel GERADE aufsetzen, leicht drehen |
| Reinigung mit Aceton | Delrin-Lager/Kunststoff-Teile geschädigt | Petroleum oder White Spirit verwenden |
| Hochdruckreiniger verwendet | Wasser in Lagern → Korrosion | Gartenschlauch oder Sprühflasche |
| WD-40 als Dauerschmierung | Bestehende Schmierung zerstört | Richtiges Fett/Öl verwenden |
| Befestigung ohne Tef-Gel | Schrauben fressen fest (galvanisch) | IMMER Tef-Gel/Duralac |

---

### ANHANG R — Bezugsquellen für Ersatzteile und Schmiermittel (DACH-Region)

| Anbieter | URL | Schwerpunkt | Versand-Region |
|----------|-----|-------------|----------------|
| SVB | svb24.de | Alle Marken, großes Sortiment | EU-weit |
| Compass24 | compass24.de | Alle Marken, Preisvergleich | EU-weit |
| Toplicht | toplicht.de | Qualitätsmarken, Beratung | DACH |
| AWN | awn.de | Breites Sortiment | DACH |
| Bootsteile.de | bootsteile.de | Günstige Preise | DACH |
| Harken Direct | harken.com | Harken-Ersatzteile (direkt) | Weltweit |
| Lewmar Shop | lewmar.com | Lewmar-Ersatzteile (direkt) | Weltweit |
| Andersen Winches | andersen-winches.com | Andersen-Ersatzteile (direkt) | Weltweit |
| Antal | antal.it | Antal-Ersatzteile (direkt) | Weltweit |
| McLube | mclubesailkote.com | Spezial-Schmiermittel | Weltweit |
| Yachticon | yachticon.de | Pflegeprodukte, Reiniger | DACH |
| Osculati | osculati.com | Universal-Ersatzteile | EU-weit |

**Tef-Gel Bezugsquellen:**
- Tef-Gel International: tefgel.com
- Über alle oben genannten Bootszubehör-Anbieter
- Preis: ca. 15 EUR / 30 g Tube

**Hinweis für Blauwasser-Segler:**
Vor Abfahrt alle benötigten Ersatzteile beschaffen. In vielen Teilen der Welt sind markenspezifische Winsch-Ersatzteile nicht verfügbar. Mindestens den in Abschnitt 6.6.2 beschriebenen Blauwasser-Bordbestand mitführen.

---

### ANHANG S — Erweiterte Schmiermittel-Datenblätter

#### S.1 Harken White Grease (BK4520) — Technisches Datenblatt

| Eigenschaft | Wert | Prüfnorm |
|-------------|------|----------|
| Grundöl-Typ | PAO (Polyalphaolefin) Synthese | — |
| Grundöl-Viskosität (40 °C) | 100 mm²/s | ASTM D445 |
| Grundöl-Viskosität (100 °C) | 14 mm²/s | ASTM D445 |
| Verdicker | Lithium-12-Hydroxystearat-Komplex | — |
| NLGI-Konsistenzklasse | 1–2 | ASTM D217 |
| Tropfpunkt | >200 °C | ASTM D2265 |
| Betriebstemperaturbereich | –30 °C bis +150 °C | — |
| Wasserauswaschung (40 °C) | <2 % | ASTM D1264 |
| Wasserauswaschung (80 °C) | <5 % | ASTM D1264 |
| 4-Kugel-Test Schweißkraft | >250 kg | ASTM D2596 |
| 4-Kugel-Test Verschleißnarbe | <0.6 mm | ASTM D2266 |
| Kupferkorrosionstest | 1a (keine Korrosion) | ASTM D4048 |
| PTFE-Gehalt | 3–5 % (mikronisiert) | — |
| Oxidationsstabilität (100 h) | <25 kPa Druckabfall | ASTM D942 |
| Farbe | Weiß | Visuell |
| Dichte (20 °C) | 0.92 g/cm³ | ASTM D1298 |

**Anwendungshinweise Harken White Grease:**
- Auftrag mit Finger oder kleinem Spatel (dünn und gleichmäßig)
- Auf Lagerflächen: Fett zwischen Nadeln/Kugeln drücken, nicht nur obenauf
- Auf Getriebezähne: Dünn auf alle Zahnflanken auftragen
- Auf Achse: Dünner Film, nicht klumpenweise
- Verbrauch pro Wartung (Size 46): ca. 20–25 g gesamt
- Tube (28 g) reicht für ca. 1 Wartung einer Winsch Size 40–50
- Dose (100 g) reicht für ca. 4–5 Wartungen oder 1× komplett 6 Winschen

#### S.2 Lewmar Winch Grease (19701500) — Technisches Datenblatt

| Eigenschaft | Wert | Prüfnorm |
|-------------|------|----------|
| Grundöl-Typ | Mineralöl/Synthese-Blend | — |
| Grundöl-Viskosität (40 °C) | 150 mm²/s | ASTM D445 |
| Grundöl-Viskosität (100 °C) | 16 mm²/s | ASTM D445 |
| Verdicker | Lithium-12-Hydroxystearat | — |
| NLGI-Konsistenzklasse | 2 | ASTM D217 |
| Tropfpunkt | >180 °C | ASTM D2265 |
| Betriebstemperaturbereich | –20 °C bis +130 °C | — |
| Wasserauswaschung (40 °C) | <4 % | ASTM D1264 |
| 4-Kugel-Test Schweißkraft | >200 kg | ASTM D2596 |
| 4-Kugel-Test Verschleißnarbe | <0.8 mm | ASTM D2266 |
| Kupferkorrosionstest | 1b | ASTM D4048 |
| Farbe | Bernstein/Gelb | Visuell |
| Dichte (20 °C) | 0.90 g/cm³ | ASTM D1298 |

**Anwendungshinweise Lewmar Winch Grease:**
- Lewmar empfiehlt etwas großzügigere Fettmengen als Harken
- Verbrauch pro Wartung (EVO 45): ca. 25–30 g gesamt
- Tube (75 ml / ca. 68 g) reicht für ca. 2 Wartungen einer Winsch EVO 40–50
- Besonderheit: Lewmar bietet auch Gear Grease (19701700) für Getriebezähne an — höhere EP-Belastbarkeit
- Lewmar Gear Grease NUR auf Getriebezähne, NICHT auf Lager/Achsen

#### S.3 Andersen Service Grease — Technisches Datenblatt

| Eigenschaft | Wert | Prüfnorm |
|-------------|------|----------|
| Grundöl-Typ | PAO (Polyalphaolefin) Synthese | — |
| Grundöl-Viskosität (40 °C) | 110 mm²/s | ASTM D445 |
| Grundöl-Viskosität (100 °C) | 15 mm²/s | ASTM D445 |
| Verdicker | Calcium-Sulfonat-Komplex | — |
| NLGI-Konsistenzklasse | 1–2 | ASTM D217 |
| Tropfpunkt | >220 °C | ASTM D2265 |
| Betriebstemperaturbereich | –35 °C bis +160 °C | — |
| Wasserauswaschung (40 °C) | <1 % | ASTM D1264 |
| Wasserauswaschung (80 °C) | <3 % | ASTM D1264 |
| 4-Kugel-Test Schweißkraft | >315 kg | ASTM D2596 |
| 4-Kugel-Test Verschleißnarbe | <0.5 mm | ASTM D2266 |
| Kupferkorrosionstest | 1a (keine Korrosion) | ASTM D4048 |
| PTFE-Gehalt | 3–5 % (mikronisiert) | — |
| Salzsprühnebeltest | >1000 h (keine Korrosion) | ASTM B117 |
| Farbe | Weiß | Visuell |
| Dichte (20 °C) | 0.93 g/cm³ | ASTM D1298 |
| Biologisch abbaubar (Teilbereiche) | >60 % (28 Tage) | OECD 301B |

**Anwendungshinweise Andersen Service Grease:**
- ACHTUNG: Calcium-Sulfonat-Verdicker ist NICHT kompatibel mit Lithium-Fetten!
- Bei Wechsel von Harken/Lewmar-Fett auf Andersen: ALTES FETT VOLLSTÄNDIG ENTFERNEN
- Andersen Service Grease hat die beste Wasserbeständigkeit aller Winschfette
- Ideal für Tropenreviere und Blauwasser-Yachten
- Verbrauch pro Wartung (Size 46): ca. 20–25 g gesamt
- Höherer Preis (ca. 22 EUR/100 g) wird durch bessere Eigenschaften gerechtfertigt

---

### ANHANG T — Elektrische Winschen — Wartungsergänzung

#### T.1 Zusätzliche Wartungspunkte für E-Winschen

Elektrische Winschen erfordern neben der mechanischen Standard-Wartung (Abschnitt 4.2) zusätzliche elektrische Wartungsmaßnahmen:

| Intervall | Maßnahme | Werkzeug | Kriterium |
|-----------|----------|----------|-----------|
| Monatlich | Funktionstest (beide Richtungen, beide Geschwindigkeiten) | Steuerknopf | Sofortige Reaktion, gleichmäßiger Lauf |
| Monatlich | Sichtprüfung der Kabelanschlüsse | Taschenlampe | Keine Korrosion, fester Sitz |
| Monatlich | Sicherung prüfen | Visuell | Intakt, korrekter Wert |
| Halbjährlich | Spannung am Motor unter Last messen | Multimeter | Sollwert ±10 % (12V: 11–13V, 24V: 22–26V) |
| Halbjährlich | Strom unter Last messen | Zangenamperemeter | Sollwert lt. Hersteller (±20 %) |
| Halbjährlich | Solenoid-Kontakte prüfen | Multimeter (Durchgang) | <0.1 Ohm Kontaktwiderstand |
| Halbjährlich | Kabelisolierung prüfen | Visuell | Keine Beschädigung, Risse, Scheuerstellen |
| Jährlich | Motor-Bürsten prüfen (bei Bürstenmotoren) | Demontage | >50 % Restlänge |
| Jährlich | Motor-Widerstand messen | Multimeter | Sollwert lt. Hersteller |
| Jährlich | Motorlager prüfen (Geräusch, Spiel) | Manuell, Ohr | Gleichmäßig, leise, kein Spiel |
| Jährlich | Dichtigkeit der Motorgehäuse-Durchführung | Visuell + Feuchte | Trocken, keine Korrosion innen |
| 5-jährlich | Motor-Generalüberholung (Werft) | Spezialwerkzeug | Laut Hersteller-Spezifikation |

#### T.2 Typische Stromaufnahme elektrischer Winschen

| Hersteller | Modell | Leerlauf (A) | Nennlast (A) | Maximallast (A) | Spannung |
|------------|--------|-------------|-------------|-----------------|----------|
| Harken | 40.2STEC | 8–12 | 40–60 | 80–100 | 12V |
| Harken | 46.2STEC | 10–15 | 50–75 | 100–130 | 12V |
| Harken | 50.2STEC | 12–18 | 60–90 | 120–160 | 12V |
| Harken | 60.2STEC | 8–12 | 35–50 | 70–90 | 24V |
| Lewmar | EVO 40EST | 8–12 | 35–55 | 75–95 | 12V |
| Lewmar | EVO 50EST | 10–15 | 45–70 | 90–120 | 12V |
| Lewmar | EVO 65EST | 8–12 | 30–50 | 65–85 | 24V |
| Andersen | 46ST Electric | 10–14 | 45–65 | 85–110 | 12V |
| Andersen | 52ST Electric | 12–16 | 55–80 | 100–140 | 12V |

**Hinweis:** Wenn der Strom unter Nennlast deutlich höher als die Tabellenwerte ist (>30 % über Sollwert), deutet dies auf:
- Erhöhte mechanische Reibung (Wartungsbedarf!)
- Schwergängige Lager
- Korrodierte Kontakte (erhöhter Übergangswiderstand)
- Motorprobleme (Bürsten, Wicklung)

#### T.3 Kabelquerschnitte und Sicherungen

| Winschgröße | Maximaler Strom | Min. Kabelquerschnitt (bis 5 m) | Min. Kabelquerschnitt (5–10 m) | Sicherung |
|-------------|----------------|-------------------------------|--------------------------------|-----------|
| Size 40 (12V) | 100 A | 25 mm² | 35 mm² | 100 A |
| Size 46 (12V) | 130 A | 35 mm² | 50 mm² | 150 A |
| Size 50 (12V) | 160 A | 50 mm² | 70 mm² | 175 A |
| Size 40 (24V) | 50 A | 10 mm² | 16 mm² | 60 A |
| Size 50 (24V) | 80 A | 16 mm² | 25 mm² | 100 A |
| Size 65 (24V) | 90 A | 25 mm² | 35 mm² | 100 A |

**ACHTUNG:** Unterdimensionierte Kabel führen zu:
1. Spannungsabfall → Motor dreht langsam/schwach
2. Überhitzung der Kabel → Brandgefahr!
3. Erhöhter Übergangswiderstand → Solenoid-Schäden

---

### ANHANG U — Winsch-Wartung in extremen Klimazonen

#### U.1 Tropische Reviere (Karibik, Südostasien, Pazifik)

**Zusätzliche Herausforderungen:**
- Extreme UV-Strahlung (beschleunigt Kunststoff-Alterung: Delrin-Lager, O-Ringe, Jaw-Inserts)
- Hohe Luftfeuchtigkeit (permanentes Korrosionsrisiko)
- Hohe Wassertemperatur (erhöhte Korrosionsrate)
- Salzgehalt oft höher als Ostsee/Nordsee
- Biologischer Bewuchs (Algen, Muscheln auf Trommeloberfläche)

**Angepasste Wartungsintervalle:**

| Maßnahme | Standard (Nordeuropa) | Tropen |
|----------|----------------------|--------|
| Süßwasser-Spülung | Nach jedem Einsatz | Nach JEDEM Einsatz (Pflicht) + abendliche Extra-Spülung |
| Sperrklinken ölen | Quartalsweise | Monatlich |
| Komplettwartung | Jährlich | Quartalsweise |
| Jaw-Insert-Prüfung | Halbjährlich | Monatlich |
| O-Ring-Wechsel | Alle 3–5 Jahre | Alle 2 Jahre |
| Generalüberholung | Alle 5 Jahre | Alle 2–3 Jahre |

**Zusätzliche Maßnahmen:**
- UV-Schutzhüllen für Winschen wenn nicht in Gebrauch (Sunbrella-Stoff)
- Korrosionsschutz-Spray (z.B. CorrosionX) auf alle exponierten Metallflächen
- Biologischen Bewuchs regelmäßig entfernen (weiche Bürste + Süßwasser)
- Delrin-Lager häufiger prüfen (UV-Versprödung)

#### U.2 Kalte Reviere (Skandinavien, Nordatlantik)

**Zusätzliche Herausforderungen:**
- Niedrige Temperaturen → Fett wird steif → Winsch schwergängig
- Frost-Tau-Zyklen → Wassereinschluss in Lagern gefriert → mechanische Beschädigung
- Eis auf Trommeln und Self-Tailing-Mechanismus
- Eingeschränkte Wartungsmöglichkeiten (kalte Hände, kurze Tage)

**Angepasste Maßnahmen:**
- Schmierfett mit tiefem Temperaturbereich verwenden:
  - Andersen Service Grease: –35 °C (beste Wahl)
  - Harken White Grease: –30 °C (gut)
  - Lewmar Winch Grease: –20 °C (bedingt)
  - Winch-Mate: –15 °C (nicht empfohlen bei Kälte)
- Vor der Winterlagerung: REICHLICH fetten (Konservierungsschmierung)
- Im Frühjahr: Probelauf unter leichter Last, bevor volle Belastung
- Bei Eis auf Winschen: NIEMALS mit Gewalt drehen! Auftauen lassen oder lauwarm Süßwasser

#### U.3 Mittelmeer (hoher Salzgehalt, sommerliche Hitze)

**Zusätzliche Herausforderungen:**
- Hoher Salzgehalt (38–39 PSU vs. 7–18 PSU Ostsee)
- Sommerliche Hitze (Deck-Oberflächentemperaturen >60 °C)
- Lange Standzeiten im Hafen (Salzwasser trocknet auf Winschen)
- Saisonale Nutzung (viele Boote nur im Sommer genutzt)

**Angepasste Maßnahmen:**
- Süßwasser-Spülung nach JEDEM Einsatz (auch nach kurzen Hafenmanövern!)
- Schmierfett mit hohem Tropfpunkt verwenden (Andersen: >220 °C ideal)
- Self-Tailing-Backen häufiger prüfen (Salzkristalle reduzieren Grip)
- Bei langen Standzeiten: Trommeln mit feuchtem Tuch abdecken (Salztrocknung verhindern)
- Vor der Wintereinlagerung: Besonders gründliche Salzentfernung

---

### ANHANG V — Historische Winschen und Ersatzteilbeschaffung

#### V.1 Übersicht historischer Hersteller

| Hersteller | Aktiv | Ersatzteile | Kompatibilität |
|------------|-------|-------------|----------------|
| Barient | 1960–1990 (von Lewmar übernommen) | Lewmar hat einige Ersatzteile | Teils kompatibel mit frühen Lewmar |
| Barlow | 1930–1995 (von Lewmar übernommen) | Lewmar hat einige Ersatzteile | Begrenzt |
| Gibb | 1960–1985 | Nicht mehr verfügbar | Keine |
| Meissner | 1970–2000 | Nicht mehr verfügbar | Keine |
| Murray | 1960–1980 | Nicht mehr verfügbar | Keine |
| Enkes | 1960–1990 | Nicht mehr verfügbar | Keine |
| Frederiksen | 1978–heute (Blöcke) | Begrenzt (Winschen eingestellt) | — |

#### V.2 Lösungsansätze für historische Winschen

**Option 1: Gebrauchte Ersatzteile**
- Internetforen: SY-Forum.de, Segeln-Forum, Cruisers Forum
- eBay, Kleinanzeigen (nach alten Winschen gleichen Typs suchen)
- Bootsschlachtungen / Bootsverwertungen

**Option 2: Nachfertigung**
- Sperrklinken: Können von Dreher/Fräser aus Edelstahl nachgefertigt werden (Zeichnung oder Muster erforderlich)
- Federn: Können von Federnhersteller nachgefertigt werden
- Lager: Oft Standardlager (Nadellager, Kugellager) mit handelsüblichen Maßen
- Buchsen: Können aus Bronze oder Delrin gedreht werden

**Option 3: Adapterbasis für moderne Winsch**
- Lewmar bietet Adapter-Platten für Barient/Barlow-Bohrbilder an
- Harken bietet universelle Adapterbasen an
- Individuelle Anfertigung durch Werft möglich (Edelstahl- oder Aluminium-Adapterplatte)

**Option 4: Komplett-Austausch**
- Oft die wirtschaftlichste Lösung
- Neues Bohrbild in Deck → Alte Löcher fachgerecht verschließen
- Backing-Plate anpassen
- Typische Kosten (inkl. Montage): 500–2.500 EUR pro Winsch

#### V.3 Barient-zu-Lewmar Kreuzreferenz

| Barient Modell | Lewmar Äquivalent | Basis-Kompatibilität | Anmerkung |
|----------------|-------------------|---------------------|-----------|
| Barient 10 | Lewmar 6 | Nein | Komplett anderes Design |
| Barient 21 | Lewmar 16 | Nein | Adapter erforderlich |
| Barient 22 | Lewmar 30 | Bedingt | Bolzenkreis prüfen! |
| Barient 27 | Lewmar 40 | Nein | Adapter erforderlich |
| Barient 28 | Lewmar 44 | Nein | Adapter erforderlich |
| Barient 32 | Lewmar 48 | Nein | Adapter erforderlich |
| Barient 35 | Lewmar 55 | Nein | Adapter erforderlich |
| Barient 36 | Lewmar 65 | Nein | Adapter erforderlich |

---

### ANHANG W — Wartungskosten-Kalkulator (Referenzwerte)

#### W.1 Jahreskosten nach Bootstyp und Wartungsstrategie

**Szenario 1: Fahrtenyacht 12 m, 6 Winschen (4× Size 40, 2× Size 28), Eigenleistung**

| Posten | Jährlich | Über 10 Jahre | Über 20 Jahre |
|--------|----------|--------------|--------------|
| Schmiermittel | 30 EUR | 300 EUR | 600 EUR |
| Pawl-Springs (alle 4 Jahre) | 25 EUR/a | 250 EUR | 500 EUR |
| Jaw-Inserts (alle 6 Jahre) | 28 EUR/a | 280 EUR | 560 EUR |
| O-Ringe (alle 3 Jahre) | 12 EUR/a | 120 EUR | 240 EUR |
| Lager (alle 12 Jahre) | 15 EUR/a | 150 EUR | 300 EUR |
| Sonstige Verschleißteile | 10 EUR/a | 100 EUR | 200 EUR |
| **Gesamt (Material)** | **120 EUR/a** | **1.200 EUR** | **2.400 EUR** |
| Arbeitszeit (Eigenleistung, 8 h × 40 EUR/h) | 320 EUR | 3.200 EUR | 6.400 EUR |
| **Gesamt inkl. Arbeitswert** | **440 EUR/a** | **4.400 EUR** | **8.800 EUR** |

**Szenario 2: Gleiche Yacht, Werft-Wartung**

| Posten | Jährlich | Über 10 Jahre | Über 20 Jahre |
|--------|----------|--------------|--------------|
| Material (wie oben) | 120 EUR | 1.200 EUR | 2.400 EUR |
| Arbeit Werft (8 h × 95 EUR/h) | 760 EUR | 7.600 EUR | 15.200 EUR |
| **Gesamt** | **880 EUR/a** | **8.800 EUR** | **17.600 EUR** |

**Szenario 3: Keine Wartung (Kostenvergleich)**

| Posten | Über 10 Jahre | Über 20 Jahre |
|--------|--------------|--------------|
| Wartungskosten | 0 EUR | 0 EUR |
| Vorzeitiger Ersatz (4× Size 40 nach 10 J.) | 6.000 EUR | 12.000 EUR |
| Vorzeitiger Ersatz (2× Size 28 nach 10 J.) | 1.600 EUR | 3.200 EUR |
| Notreparaturen (geschätzt) | 2.000 EUR | 4.000 EUR |
| **Gesamt** | **9.600 EUR** | **19.200 EUR** |

**Ergebnis:** Eigenleistungs-Wartung spart über 20 Jahre ca. 10.400 EUR gegenüber Nicht-Wartung und ca. 8.800 EUR gegenüber Werft-Wartung.

#### W.2 ROI-Berechnung der Winsch-Wartung

```
ROI = (Vermiedene Kosten - Wartungskosten) / Wartungskosten × 100

Beispiel: 12 m Fahrtenyacht, 20 Jahre

Vermiedene Kosten (durch Wartung):
  Vorzeitiger Ersatz vermieden:     15.200 EUR
  Notreparaturen vermieden:          4.000 EUR
  Werterhalt (Wiederverkauf):        2.000 EUR
  Gesamt vermieden:                 21.200 EUR

Wartungskosten (Eigenleistung):
  Material über 20 Jahre:            2.400 EUR
  (Arbeitszeit nicht monetär)

ROI (nur Material):
  (21.200 - 2.400) / 2.400 × 100 = 783 %

→ Jeder investierte Euro in Winsch-Wartung spart ca. 8 EUR
```

---

### ANHANG X — Umwelt- und Entsorgungshinweise

#### X.1 Entsorgung von Altfett und Reinigungsmitteln

| Material | Entsorgung | NICHT erlaubt |
|----------|-----------|---------------|
| Altfett (Winschfett) | Sondermüll (Altöl-Annahmestelle) | Ins Wasser, in den Hausmüll |
| Petroleum/White Spirit (gebraucht) | Sondermüll (Lösungsmittel) | In den Abfluss, ins Wasser |
| Reinigungslappen (fettgetränkt) | Selbstentzündungsgefahr! Metallbehälter, dann Sondermüll | Zusammenknüllen, offener Mülleimer |
| Alte O-Ringe | Hausmüll (geringe Menge) | — |
| Alte Sperrklinken-Federn | Altmetall | — |
| Alte Jaw-Inserts (Kunststoff) | Kunststoffentsorgung | — |
| Alte Lager | Altmetall | — |

#### X.2 Umweltverträgliche Alternativen

| Konventionell | Umweltfreundliche Alternative | Einschränkung |
|---------------|-------------------------------|---------------|
| Petroleum | Bio-Reiniger (z.B. Biocosmarine) | Geringere Fettlösekraft |
| Mineralöl-Fett | Biologisch abbaubares Fett (z.B. Andersen) | Höherer Preis |
| WD-40 | Bio-Kriechöl (z.B. Ballistol) | Etwas geringere Kriechfähigkeit |
| Phosphorsäure | Zitronensäure | Längere Einwirkzeit |

#### X.3 Sicherheitsdatenblatt-Hinweise (SDB)

Die folgenden Produkte erfordern besondere Handhabung gemäß ihrer Sicherheitsdatenblätter:

**Petroleum / Shellsol D40:**
- Gefahrenklasse: Entzündbar Kat. 3 (H226: Flüssigkeit und Dampf entzündbar)
- Gesundheit: H304 (Aspirationsgefahr), H336 (Kann Schläfrigkeit verursachen)
- Maßnahmen: Gut belüften, Handschuhe (Nitril), keine offene Flamme
- Erste Hilfe: Bei Verschlucken KEIN Erbrechen auslösen, sofort Notruf

**White Spirit (Testbenzin):**
- Gefahrenklasse: Entzündbar Kat. 3
- Gesundheit: H304, H336, H372 (Kann Organe schädigen bei längerem Kontakt)
- Maßnahmen: Gut belüften, Nitrilhandschuhe, Schutzbrille
- Entsorgung: Sondermüll, niemals in den Ausguss

**Isopropanol (99 %):**
- Gefahrenklasse: Entzündbar Kat. 2 (H225: Leicht entzündbar)
- Gesundheit: H319 (Augenreizung), H336
- Maßnahmen: Gut belüften, von Zündquellen fernhalten
- Besonderheit: Sehr schnell verdunstend, Dämpfe sind schwerer als Luft

**Phosphorsäure (5–10 %):**
- Gefahrenklasse: Ätzend Kat. 1B (H314: Schwere Verätzungen)
- Maßnahmen: Schutzbrille (Pflicht!), Handschuhe, Schürze
- Erste Hilfe: Bei Hautkontakt sofort mit viel Wasser spülen

**Allgemeine Vorsichtsmaßnahmen an Bord:**
- Alle Reinigungsmittel in verschließbaren Behältern lagern
- Feuerlöscher in Reichweite (bei Arbeiten mit entzündbaren Stoffen)
- Lüftungsöffnungen öffnen (besonders in geschlossenen Cockpits und unter Deck)
- Kinder und Haustiere vom Arbeitsbereich fernhalten
- Getränkte Lappen nicht zusammenknüllen (Selbstentzündungsgefahr bei ölgetränkten Lappen!)

---

### ANHANG Y — Winsch-Wartung: Zeitspar-Tipps für Vielbeschäftigte

#### Y.1 Die 15-Minuten-Wartung (Monatlich)

Für Segler mit wenig Zeit — die absolut minimale Wartung, die dennoch die Lebensdauer signifikant verlängert:

1. **Minuten 1–5:** Jede Winsch 3–4 Umdrehungen in beide Richtungen drehen. Auf Geräusche, Schwergängigkeit und Sperrklinken-Klicken achten.
2. **Minuten 5–10:** Self-Tailing jeder Winsch mit einer Schot testen. Schot einfädeln, 2 Wraps, unter Handzug kurbeln, loslassen — hält die Schot?
3. **Minuten 10–13:** An jeder Winsch die Trommel 5 cm anheben (wenn ohne Werkzeug möglich) und 2 Tropfen Öl auf sichtbare Sperrklinken geben.
4. **Minuten 13–15:** Trommeln und Self-Tailing-Ringe mit feuchtem Tuch (Süßwasser) abwischen.

Diese 15 Minuten monatlich können die Lebensdauer der Winschen um 30–50 % verlängern im Vergleich zu überhaupt keiner Wartung.

#### Y.2 Die 2-Stunden-Saisonwartung (Minimum pro Saison)

Für Segler, die keine volle Tageswartung durchführen können — die reduzierte Saisonwartung:

1. **30 min Vorbereitung:** Werkzeug und Schmiermittel bereitlegen, Wanne aufstellen
2. **15 min pro Winsch (bei 6 Winschen = 90 min):**
   - Trommel abnehmen (2 min)
   - Sperrklinken und Federn sichtprüfen (2 min)
   - Altes Fett von sichtbaren Stellen abwischen (3 min)
   - Neues Fett auf Lager und Achse auftragen (3 min)
   - Sperrklinken-Federn ölen (1 min)
   - Trommel aufsetzen, Funktionstest (2 min)
   - Jaw-Inserts sichtprüfen (2 min)

Dies ist KEINE vollständige Wartung, aber deutlich besser als nichts. Empfehlung: Mindestens alle 2 Jahre eine echte Komplettwartung (Abschnitt 4.2).

#### Y.3 Wartung delegieren — Checkliste für den Rigger/Werft-Auftrag

Wenn Sie die Wartung an einen Profi delegieren, sollte der Auftrag folgende Punkte umfassen:

```
AUFTRAGSFORMULAR WINSCH-WARTUNG

□ Komplettwartung aller ___ Winschen (Demontage, Reinigung, Inspektion, Neufettung)
□ Verwendung von Original-Herstellerfett: ____________
□ Verschleißteile-Inspektion mit Messprotokoll
□ Austausch defekter Verschleißteile (nach Rücksprache / pauschal bis ___ EUR)
□ Befestigungsmomente prüfen und protokollieren
□ Self-Tailing-Funktionstest
□ Foto-Dokumentation (vorher/nachher)
□ Schriftliches Wartungsprotokoll mit Befunden
□ Empfehlungen für nächste Wartung

Maximales Budget (Material): _______ EUR
Kontakt für Rücksprache: ______________
```

#### X.3 Hafenordnungen und Umweltauflagen

In vielen Marinas ist die Wartung von Winschen an Bord erlaubt, sofern:
- Keine Schmiermittel ins Wasser gelangen
- Reinigungsmittel in Auffangwannen gesammelt werden
- Altöl/Altfett ordnungsgemäß entsorgt wird
- Keine Lösungsmittel an Deck verwendet werden (bei offener Bilge → Lenzpumpe → Wasser)

**Empfehlung:** Wartung auf dem Trockenen durchführen (Winterlager, Slip). Wenn an Bord: Auffangwanne unter der Winsch, Lappen bereithalten, Lenzpumpe NICHT betätigen während der Wartung.

---

### ANHANG Z — Cross-Referenz: Bootshersteller → Standard-Winschen

#### Z.1 Häufige Winschen-Ausstattung nach Bootshersteller

Die folgende Tabelle zeigt die typische Serien-Winsch-Ausstattung gängiger europäischer Bootshersteller. Bei Gebrauchtbooten kann die Ausstattung aufgrund von Nachrüstungen abweichen.

| Bootshersteller | Modellreihe | Baujahre | Genua-Winschen | Großschot-Winsch | Fall-Winschen |
|-----------------|-------------|----------|----------------|------------------|---------------|
| Bavaria | Cruiser 34–46 | 2015–2025 | Lewmar EVO 40–50ST | Lewmar EVO 40–50ST | Lewmar EVO 30ST |
| Bavaria | Vision 42–46 | 2018–2025 | Lewmar EVO 45–55ST | Lewmar EVO 50–55EST | Lewmar EVO 30ST |
| Beneteau | Oceanis 30.1–51.1 | 2018–2025 | Harken 40–50.2STC | Harken 46–50.2STC | Harken 35.2STC |
| Beneteau | First 27–53 | 2017–2025 | Harken 40–60.2STC | Harken 46–60.2STEC | Harken 40.2STC |
| Dehler | 30–46 | 2015–2025 | Andersen 40–52ST | Andersen 46–52ST | Andersen 28ST |
| Dufour | Grand Large 360–530 | 2016–2025 | Harken 40–60.2STC | Harken 46–60.2STC | Harken 35.2STC |
| Hallberg-Rassy | 31–64 | 2010–2025 | Andersen 40–68ST | Andersen 46–68ST | Andersen 28–40ST |
| Hanse | 315–675 | 2016–2025 | Lewmar EVO 40–65ST | Lewmar EVO 45–65EST | Lewmar EVO 30–40ST |
| Jeanneau | Sun Odyssey 319–490 | 2017–2025 | Harken 40–50.2STC | Harken 46–50.2STC | Harken 35.2STC |
| Najad | 355–570 | 2005–2020 | Andersen 46–68ST | Andersen 52–68ST | Andersen 40–46ST |
| Sweden Yachts | 390–45 | 2010–2020 | Andersen 46–52ST | Andersen 52ST | Andersen 40ST |
| X-Yachts | XC 35–45 | 2015–2025 | Harken 46–60.2STC | Harken 50–60.2STEC | Harken 40.2STC |
| X-Yachts | X4.0–X4.9 | 2016–2025 | Harken 46–60.2STC | Harken 50–60.2STEC | Harken 40.2STC |

**Hinweis:** Diese Tabelle zeigt die Serienausstattung. Viele Bootshersteller bieten Winsch-Upgrades als Option an. Bei Performance-Paketen werden oft größere oder elektrische Winschen verbaut.

#### Z.2 Wartungsrelevante Besonderheiten nach Bootshersteller

| Bootshersteller | Besonderheit | Wartungskonsequenz |
|-----------------|-------------|-------------------|
| Bavaria | Winschen teils direkt auf GFK ohne Backing Plate | Befestigung regelmäßig auf Spiel prüfen |
| Beneteau | Harken-Winschen mit integriertem Halyard-Stopper | Stopper-Mechanismus zusätzlich warten |
| Dehler | Andersen-Winschen, werkzeuglose Demontage | Wartung besonders einfach (Compact-System) |
| Hallberg-Rassy | Massive Aluminium-Backing-Plates ab Werk | Befestigung selten problematisch |
| Hanse | Lewmar-Winschen teils auf Composite-Deckpad | Deckpad auf Ablösung prüfen |
| Jeanneau | Winsch-Positionen teils ergonomisch ungünstig | Wartung schwieriger, mehr Zeit einplanen |
| X-Yachts | Hochwertige Montage, oft Carbon-Backing | Befestigung selten problematisch |

#### Z.3 Empfohlene Schmiermittel-Bestellung nach Bootshersteller

Um die Bestellung zu vereinfachen, hier die Empfehlung sortiert nach Bootshersteller:

**Bavaria / Hanse (Lewmar-Winschen):**
- Lewmar Winch Grease (19701500) — 1× 75 ml Tube
- Lewmar Winch Oil (19701600) — 1× 55 ml Flasche
- Lewmar Spring Kit — passend zur verbauten EVO-Größe

**Beneteau / Jeanneau / Dufour / X-Yachts (Harken-Winschen):**
- Harken White Grease (BK4520) — 1× 100 g Dose
- Harken Pawl Oil (BK4521) — 1× 14 ml Fläschchen
- Harken Pawl-Spring Kit — passend zur Radial-Größe

**Dehler / Hallberg-Rassy / Najad / Sweden Yachts (Andersen-Winschen):**
- Andersen Service Grease — 1× 100 g Dose
- Andersen Service Oil — 1× Fläschchen
- Andersen Spring Kit — passend zur Compact-Größe
- **ACHTUNG:** Andersen-Fett NICHT mit Harken/Lewmar-Fett mischen!

---

### ANHANG AA — Qualitätskontrolle nach Wartung

#### AA.1 Abnahmeprüfung (Quality Gate nach Wartung)

Die folgende Prüfung sollte nach JEDER Wartung durchgeführt werden, bevor die Winsch wieder unter Last gesetzt wird:

| Nr. | Prüfung | Methode | Akzeptanzkriterium | Pflicht? |
|-----|---------|---------|-------------------|----------|
| 1 | Drehrichtung UZS | Kurbel drehen | Gleichmäßig, leichtgängig | Ja |
| 2 | Sperrung GZS | Kurbel rückwärts | Sofortiges Sperren, lautes Klicken | Ja |
| 3 | 1. Gang | Schnell UZS drehen | Schnelle Geschwindigkeit, kein Widerstand | Ja |
| 4 | 2. Gang | Langsam UZS drehen | Deutlich erhöhter Widerstand (Untersetzung) | Ja |
| 5 | Self-Tailing | Schot einlegen, kurbeln | Schot wird sicher gehalten | Ja |
| 6 | Fieren | Schot unter Handspannung fieren | Kontrolliertes Nachlassen | Ja |
| 7 | Geräusche | Alle Funktionen, Ohr nah | Kein Knirschen, Kratzen, Quietschen | Ja |
| 8 | Leerlauf-Widerstand | Kurbel ohne Last | Nicht schwergängiger als vor der Wartung | Empfohlen |
| 9 | Visuell | Kontrolle | Keine sichtbaren Teile lose, Sicherung eingerastet | Ja |
| 10 | Belastungstest | Schot um Poller, 2 Wraps, unter Körpergewicht kurbeln | Kein Durchrutschen, keine Geräusche | Empfohlen |

**WICHTIG:** Wenn Prüfung 2 (Sperrung) NICHT bestanden wird: Winsch SOFORT erneut demontieren und Fehler suchen. Eine Winsch ohne funktionierende Rücklaufsicherung ist ein Sicherheitsrisiko!

#### AA.2 Einlauf-Phase nach Wartung

Nach einer Komplettwartung sollte die Winsch eine kurze Einlauf-Phase durchlaufen:
- Die ersten 20–30 Umdrehungen im Leerlauf sind normal etwas schwergängiger (überschüssiges Fett verteilt sich)
- Nach ca. 50 Umdrehungen sollte die Winsch ihre normale Leichtgängigkeit erreichen
- Wenn nach 100 Umdrehungen keine Verbesserung: Ursache suchen (zu viel Fett, Fehlmontage)
- Beim ersten Einsatz unter leichter Last anfangen und langsam steigern
- Nach dem ersten Segeltag mit neu gewarteten Winschen: Trommel kurz anheben und Sperrklinken visuell prüfen

---

> **Ende der Wissensdatei 09.07**
>
> **Confidence-Level dieses Dokuments:**
> - Technische Daten (Drehmomente, Toleranzen, Temperaturen): `measured` / `documented`
> - Wartungsintervalle: `documented` (Hersteller-Service-Manuals)
> - Kostenangaben: `estimated` (Marktpreise 2024/2025, DACH-Region)
> - Fallstudien: `documented` (anonymisierte reale Fälle)
> - Lebensdauerprognosen: `benchmark` (Aggregierte Branchendaten)
>
> **AYDI v6 Model Version:** 09.07.1.0
> **Nächste geplante Aktualisierung:** 2026-10 (Herstellerdaten-Update nach boot Düsseldorf 2027-Vorschau)
