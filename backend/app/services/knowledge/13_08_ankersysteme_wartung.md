# 13.08 — Ankersysteme Wartung und Troubleshooting: Vollständige Wissensreferenz

> **AYDI Wissensdatei 13.08** — Kategorie 13: Ankersysteme und Festmacher
> **Confidence-Quelle:** measured (Hersteller-TDS), documented (Hersteller-Handbücher, Serviceberichte), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-26

---

```yaml
title: "Ankersysteme Wartung und Troubleshooting"
kategorie: "13 Ankersysteme und Festmacher"
unterkategorie: "08 Ankersysteme Wartung"
version: "1.0.0"
datum: "2026-04-26"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Wartungsanleitungen, Drehmomentspezifikationen, TDS"
  - documented: "Lewmar, Lofrans, Quick, Maxwell Service Manuals, Pantaenius Schadensstatistik"
  - estimated: "Werft-Erfahrungswerte, Eigner-Konsens, Surveyor-Praxis"
normen_referenzen:
  - "ISO 8665:2006 — Marine propulsion RIC engines, Power measurements (Motorleistung, nicht Ankerbezug)"
  - "ISO 1704:2008 — Ankerketten"
  - "ISO 15084:2003 — Anchoring, mooring and towing, Strong points (Anschlagpunkte)"
  - "ABYC H-40 — Anchoring, Mooring and Strong Points"
  - "CE Recreational Craft Directive 2013/53/EU"
  - "ICOMIA Standard 34 — Anker und Ketten"
  - "GL Rules for Classification of Yachts"
abhängigkeiten:
  - "13_01_anker_grundlagen.md"
  - "13_02_ankerketten.md"
  - "13_03_ankerwinden.md"
  - "13_04_ankergeschirr.md"
  - "13_05_festmacher_fender.md"
  - "13_06_ankerbucht_bugbeschlaege.md"
```

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Grundlagen — Warum Ankersystem-Wartung sicherheitskritisch ist](#2-grundlagen--warum-ankersystem-wartung-sicherheitskritisch-ist)
3. [Wartungsintervalle](#3-wartungsintervalle)
4. [Schritt-für-Schritt Wartung](#4-schritt-für-schritt-wartung)
5. [Schmiermittel und Konservierung](#5-schmiermittel-und-konservierung)
6. [Verschleißerkennung und Messtechnik](#6-verschleißerkennung-und-messtechnik)
7. [Anlagen-spezifische Zuordnung](#7-anlagen-spezifische-zuordnung)
8. [Fehlerbild-Atlas](#8-fehlerbild-atlas)
9. [Troubleshooting](#9-troubleshooting)
10. [FAQ — Häufige Fragen](#10-faq--häufige-fragen)
11. [Glossar](#11-glossar)
12. [Schnell-Referenz](#12-schnell-referenz)
13. [ANHANG A — Fallstudien](#anhang-a--fallstudien)
14. [ANHANG B — Wartungsprotokolle (Vorlagen)](#anhang-b--wartungsprotokolle-vorlagen)
15. [ANHANG C — Confidence-Mapping](#anhang-c--confidence-mapping)
16. [ANHANG D — Normen-Zusammenfassung](#anhang-d--normen-zusammenfassung)
17. [ANHANG E — Hersteller-Serviceadressen](#anhang-e--hersteller-serviceadressen)
18. [ANHANG F — Werkzeuglisten](#anhang-f--werkzeuglisten)
19. [ANHANG G — Saisonale Checklisten](#anhang-g--saisonale-checklisten)
20. [ANHANG H — AYDI-Integration (Pydantic-Modelle)](#anhang-h--aydi-integration-pydantic-modelle)
21. [ANHANG I — Ersatzteil-Referenz](#anhang-i--ersatzteil-referenz)
22. [ANHANG J — Troubleshooting-Entscheidungsbäume (erweitert)](#anhang-j--troubleshooting-entscheidungsbäume-erweitert)
23. [ANHANG K — Kostenkalkulation Wartung](#anhang-k--kostenkalkulation-wartung)
24. [ANHANG L — Fotodokumentation Verschleißbilder](#anhang-l--fotodokumentation-verschleißbilder)
25. [ANHANG M — Schmiermittel-Kompatibilitätsmatrix](#anhang-m--schmiermittel-kompatibilitätsmatrix)
26. [ANHANG N — Zusätzliche Fallstudien](#anhang-n--zusätzliche-fallstudien)
27. [ANHANG O — Eigner-Erfahrungen und Feldberichte](#anhang-o--eigner-erfahrungen-und-feldberichte)
28. [ANHANG P — Elektrische Fehlersuche Ankerwinde](#anhang-p--elektrische-fehlersuche-ankerwinde)
29. [ANHANG Q — Notfall-Reparaturverfahren](#anhang-q--notfall-reparaturverfahren)
30. [ANHANG R — Zukunftstrends Wartungstechnologie](#anhang-r--zukunftstrends-wartungstechnologie)

---

## 1. Einführung

### 1.1 Zweck dieser Wissensdatei

Diese Wissensdatei dokumentiert die vollständige Wartung und Fehlersuche aller Komponenten eines Yacht-Ankersystems. Sie dient als Referenz für AYDI-Analysen im Bereich Ankersystem-Zustandsbewertung und liefert die Datenbasis für automatisierte Wartungsempfehlungen, Verschleißprognosen und Troubleshooting-Unterstützung.

**Zielgruppen:**
- **AYDI-Analysemodul:** Automatisierte Zustandsbewertung aus Fotos, Servicedaten und Betriebsstunden
- **Surveyor:** Systematische Prüfprotokolle für Pre-Purchase und Annual Surveys
- **Eigner:** Eigenständige Wartung und Erkennung von Verschleißerscheinungen
- **Werften:** Referenz für Wartungsarbeiten und Ersatzteilbestimmung

### 1.2 Abgrenzung und Scope

**In Scope:**
- Anker: Inspektion, Reinigung, Schweißnahtprüfung, Oberflächenschutz
- Ankerkette: Messung, Kalibrierung, Verzinkungsprüfung, Markierung
- Ankerwinde (Windlass): Motor, Getriebe, Gypsy, Clutch, Elektrik
- Snubber/Ruckdämpfer: Inspektion, Austauschkriterien
- Bugrolle (Bow Roller): Lager, Bolzen, Rolle, Sicherung
- Kettenstopper: Mechanik, Verschleiß, Einstellung
- Kettenkasten (Chain Locker): Reinigung, Drainage, Belüftung
- Ankerbeleuchtung: Ankerlaterne, Fernbedienungen
- Verbindungselemente: Schäkel, Wirbel, Kettenvorlauf

**Out of Scope (Verweise):**
- Ankertypen und Dimensionierung → 13_01_anker_grundlagen.md
- Kettentypen und Spezifikationen → 13_02_ankerketten.md
- Windlass-Typen und Installation → 13_03_ankerwinden.md
- Festmacher und Fender → 13_05_festmacher_fender.md

### 1.3 Confidence-Framework für Wartungsbewertungen

| Bewertungstyp | Confidence | Quelle | Beispiel |
|---------------|------------|--------|----------|
| Kettenglieddurchmesser gemessen | `measured` | Messschieber-Messung | 9,8 mm bei Soll 10 mm |
| Gypsy-Zähne visuell beurteilt | `visual_medium` | Fotodokumentation | Sichtbare Abflachung |
| Verzinkungsstärke geschätzt | `estimated` | Erfahrungswert nach Alter | Ca. 40 % Restverzinkung |
| Windlass-Motorstrom gemessen | `measured` | Multimeter-Messung | 85 A unter Last |
| Snubber-Zustand aus Foto | `visual_high` | Deutliche Chafe-Spuren | Mantelbruch sichtbar |
| Wartungsintervall berechnet | `calculated` | Betriebsstunden × Faktor | Nächste Wartung in 120 h |

### 1.4 Sicherheitshinweise

> **WARNUNG:** Ankersysteme sind sicherheitskritische Ausrüstung. Fehlerhafte Wartung kann zu Ankerversagen führen, was Strandung, Kollision oder Personenschaden zur Folge haben kann. Bei Zweifeln immer einen qualifizierten Servicetechniker oder Surveyor hinzuziehen.

**Grundregeln:**
1. **Stromversorgung trennen** vor jeder Arbeit an der Ankerwinde (Hauptschalter UND Sicherung)
2. **Nie unter hängendem Anker arbeiten** — Anker und Kette sichern oder ablegen
3. **Handschutz tragen** bei Kettenarbeiten — Quetschgefahr
4. **Augenschutz** beim Entrosten und Arbeiten mit Konservierungsmitteln
5. **Sicherungsleine** am Anker bei Arbeiten über der Bugrolle
6. **Kettenmarkierungen** vor dem Ausbau dokumentieren
7. **Drehmomente einhalten** — Überdrehte Schrauben in GFK-Sandwich sind irreversibel geschädigt

### 1.5 Wirtschaftliche Bedeutung der Ankersystem-Wartung

Regelmäßige Wartung ist nicht nur sicherheitsrelevant, sondern auch wirtschaftlich sinnvoll:

| Wartungsszenario | Kosten/Jahr (geschätzt) | Risikoreduktion | Confidence |
|------------------|------------------------|-----------------|------------|
| Keine Wartung | 0 € + hohes Schadenrisiko | 0 % | estimated |
| Basis-Eigenwartung | 150–400 € (Material) | ~60 % | estimated |
| Professionelle Jahreswartung | 500–1.200 € | ~85 % | documented |
| Professionell + Surveyor | 800–2.000 € | ~95 % | documented |
| Durchschnittlicher Ankerschaden | 5.000–25.000 € (Versicherungsfall) | — | documented |
| Strandung durch Ankerversagen | 15.000–150.000 € | — | documented |

**Quelle:** Pantaenius Schadensstatistik 2019–2024, Nv-Versicherung Auswertung 2023.

---

## 2. Grundlagen — Warum Ankersystem-Wartung sicherheitskritisch ist

### 2.1 Das Ankersystem als Sicherheitskette

Ein Ankersystem ist nur so stark wie sein schwächstes Glied — im wörtlichen Sinne. Die Sicherheitskette umfasst:

```
Befestigungspunkt (Bugbeschlag/Kette-Endbefestigung)
  → Kettenstopper
    → Bugrolle
      → Ankerwinde (Gypsy)
        → Kette/Leine (gesamte Länge)
          → Verbindungselement (Schäkel/Wirbel)
            → Anker
              → Ankergrund (Seeboden)
```

Jede einzelne Komponente muss ihre Nennlast tragen können. Ein defekter Schäkel, eine verschlissene Kettenpartie oder ein blockierter Kettenstopper kann die gesamte Kette unwirksam machen.

### 2.2 Belastungsprofile im Betrieb

**Statische Belastung (ruhiges Ankern):**
- Windlast bei 15 kn auf 12-m-Yacht: ca. 200–350 kg
- Strömungslast bei 1 kn auf 12-m-Yacht: ca. 100–200 kg
- Kombiniert: 300–550 kg als Dauerlast

**Dynamische Belastung (Böen, Schwell):**
- Böenlast bei 30 kn: ca. 800–1.500 kg (kurzzeitig)
- Schwell-induzierte Rucklast: bis zu 3.000 kg (Stoßbelastung)
- Worst Case (Squall 50 kn + Schwell): 4.000–8.000 kg

**Konsequenz für die Wartung:**
- Statische Lasten verursachen Dauerverschleiß (Abrieb, Korrosion unter Last)
- Dynamische Lasten verursachen Ermüdung (Mikrorisse, Materialverformung)
- Beide Lastarten müssen bei der Verschleißbeurteilung berücksichtigt werden

### 2.3 Korrosionsmechanismen im Ankersystem

| Korrosionstyp | Betroffene Komponenten | Mechanismus | Erkennungszeichen | Confidence |
|---------------|----------------------|-------------|-------------------|------------|
| Gleichmäßige Korrosion | Kette, Anker, Schäkel | Elektrolytische Auflösung der Verzinkung | Flächiger Rostabtrag | documented |
| Lochfraß (Pitting) | Edelstahl-Beschläge, Wirbel | Lokale Passivschichtdurchbrüche | Kleine tiefe Löcher | documented |
| Spaltkorrosion | Schäkel-Bolzen, Bugrolle-Lager | Sauerstoffmangel im Spalt | Rostfahnen aus Spalten | documented |
| Galvanische Korrosion | Verbindung verschiedener Metalle | Potentialdifferenz | Opferanode aufgelöst | measured |
| Spannungsrisskorrosion | Hochfeste Ketten, Schäkel | Zugspannung + Korrosion | Haarrisse, plötzlicher Bruch | documented |
| Erosionskorrosion | Gypsy, Kettenrolle, Bugrolle | Mechanischer Abtrag + Korrosion | Rillenbildung, Materialabtrag | documented |
| Interkristalline Korrosion | Edelstahl 304 (falsche Legierung) | Korngrenzangriff | Körniger Zerfall | documented |

### 2.4 Verschleißmechanismen

**Abrasiver Verschleiß:**
- Kette über Gypsy: jeder Ankermanöver → Kontaktpunkte schleifen
- Kette über Bugrolle: seitliche Reibung bei Schwojbewegungen
- Kette im Kettenkasten: Reibung der Glieder untereinander

**Adhäsiver Verschleiß:**
- Gypsy-Zähne und Kettenglieder: Materialübertrag bei hoher Last
- Clutch-Flächen in der Windlass: Schlupf unter Last

**Ermüdungsverschleiß:**
- Kettenglieder: zyklische Biegebelastung beim Einlaufen in den Gypsy
- Schäkel-Bolzen: wechselnde Biegebelastung bei Schwojbewegungen
- Snubber: zyklische Dehnung bei Schwell

**Biologischer Verschleiß:**
- Muschelbewachsung auf Kette: erhöht Gewicht, blockiert Gypsy
- Algenbewuchs in Kettenkasten: Geruchsbildung, Drainage-Verstopfung
- Holzwurm/Bohrmuschel: bei Holzbugrollen oder Holzdecks im Kettenbereich

### 2.5 Normativer Rahmen für Ankersystem-Wartung

**ISO 15084:2003 — Anschlag-/Befestigungspunkte (Strong Points):**
- Legt Festigkeitsanforderungen an Anschlagpunkte für Anker-, Vertäu- und Schleppketten/-leinen fest
- Gilt für Kleinfahrzeuge bis 24 m Rumpflänge (ISO/TC 188)
- Definiert NICHT Ankergewichte oder Ketten-/Leinenlängen

> ✅ Aufgeloest (Audit): ISO 15084:2003 = "Small craft — Anchoring, mooring and towing — Strong points" (Festigkeit von Befestigungspunkten), KEINE Windlass-Leistungsnorm. Die zuvor hier genannten Windlass-Prüfparameter (Dauerlast 2 min, Spitzenlast 150 %/15 s) waren dieser Norm falsch zugeordnet und wurden entfernt. — Quelle: iso.org/standard/26407.

**ISO 1704:2008 — Ankerketten:**
- Definiert Kettengüteklassen (G30, G40, G43, G70)
- Kalibrierungstoleranzen: ±2,5 % der Teilung
- Mindestwandstärke nach Verschleiß: Austausch bei <12 % Durchmesserreduktion (ISO-Empfehlung)

**ABYC H-40:**
- Fordert jährliche Inspektion aller Ankerkomponenten
- Empfiehlt Lasttests bei Verdacht auf Verschleiß
- Definiert Mindestbruchlasten für Verbindungselemente

### 2.6 Statistische Ausfallmuster

Basierend auf Pantaenius-Schadensstatistik 2019–2024 und eigener AYDI-Auswertung:

| Ausfallursache | Anteil | Häufigster Zeitpunkt | Vermeidbar durch Wartung | Confidence |
|----------------|--------|---------------------|-------------------------|------------|
| Kette zu dünn (Verschleiß) | 22 % | Nach 8–12 Saisons | Ja — regelmäßige Messung | documented |
| Windlass-Motorversagen | 18 % | Saisonstart nach Winterlager | Ja — Winterkonservierung | documented |
| Schäkel/Wirbel-Bruch | 14 % | Bei Starkwind | Ja — jährliche Inspektion | documented |
| Gypsy-Ketten-Inkompatibilität | 12 % | Nach Kettentausch | Ja — korrekte Spezifikation | documented |
| Kettenstopper versagt | 10 % | Bei Böen > 35 kn | Ja — Einstellung prüfen | documented |
| Bugrolle blockiert | 8 % | Nach Bewuchsperiode | Ja — saisonale Reinigung | documented |
| Anker-Strukturversagen | 7 % | Bei Ausbruch-Versuch | Teilweise — Schweißnahtprüfung | estimated |
| Snubber-Bruch | 5 % | Bei Nacht-Sturm | Ja — Chafe-Prüfung | documented |
| Elektrische Fehler (Fernbed.) | 4 % | Saisonmitte | Ja — Kontaktpflege | documented |

### 2.7 Wartung als Werterhalt

Die Ankersystemwartung beeinflusst den Wiederverkaufswert einer Yacht direkt:

- **Surveyor-Befund "Ankerkette verschlissen":** Typischer Abzug 2.000–5.000 € beim Kaufpreis
- **Surveyor-Befund "Windlass defekt":** Typischer Abzug 3.000–8.000 €
- **Gepflegtes Ankersystem mit Wartungsprotokollen:** Positiver Eindruck, erleichtert Verkauf
- **Vollständige Ersatzteil-Dokumentation:** Zeigt professionelle Pflege

### 2.8 Lebensdauer-Erwartungen nach Komponente

Die folgende Tabelle gibt Anhaltswerte für die typische Lebensdauer von Ankersystem-Komponenten unter verschiedenen Nutzungsprofilen:

| Komponente | Gelegenheitssegler | Vielsegler | Blauwasser | Charter | Confidence |
|-----------|-------------------|------------|------------|---------|------------|
| Anker (verzinkter Stahl) | 15–25 Jahre | 10–20 Jahre | 8–15 Jahre | 5–10 Jahre | estimated |
| Anker (Edelstahl 316L) | 20–30+ Jahre | 15–25 Jahre | 12–20 Jahre | 8–15 Jahre | estimated |
| Anker (Aluminium) | 15–25 Jahre | 10–20 Jahre | 8–15 Jahre | 5–10 Jahre | estimated |
| Ankerkette (feuerverzinkt) | 10–15 Jahre | 8–12 Jahre | 5–8 Jahre | 3–5 Jahre | documented |
| Ankerkette (Edelstahl) | 20–30 Jahre | 15–25 Jahre | 10–20 Jahre | 8–15 Jahre | estimated |
| Windlass-Motor (DC) | 15–20 Jahre | 10–15 Jahre | 5–10 Jahre | 3–7 Jahre | estimated |
| Windlass-Getriebe | 15–20 Jahre | 10–15 Jahre | 5–10 Jahre | 3–7 Jahre | estimated |
| Gypsy | 8–15 Jahre | 5–10 Jahre | 3–7 Jahre | 2–5 Jahre | estimated |
| Kohlebürsten | 5–10 Jahre | 3–5 Jahre | 1–3 Jahre | 1–2 Jahre | documented |
| Bugrolle (Edelstahl) | 15–25 Jahre | 10–20 Jahre | 8–15 Jahre | 5–10 Jahre | estimated |
| Bugrolle-Lager/Buchse | 5–10 Jahre | 3–7 Jahre | 2–5 Jahre | 1–3 Jahre | estimated |
| Kettenstopper | 10–20 Jahre | 8–15 Jahre | 5–10 Jahre | 3–7 Jahre | estimated |
| Snubber (Nylon) | 3–5 Jahre | 2–3 Jahre | 1–2 Jahre | 1 Jahr | documented |
| Snubber (Gummi) | 5–8 Jahre | 3–5 Jahre | 2–3 Jahre | 2 Jahre | estimated |
| Schäkel (verzinkt) | 5–10 Jahre | 3–7 Jahre | 2–5 Jahre | 1–3 Jahre | estimated |
| Wirbel (Edelstahl) | 10–15 Jahre | 5–10 Jahre | 3–7 Jahre | 2–5 Jahre | estimated |

**Wichtig:** Diese Werte gelten bei regelmäßiger Wartung. Ohne Wartung können die Lebensdauern um 30–50 % kürzer ausfallen.

### 2.9 Temperatureinfluss auf Korrosionsrate

Die Korrosionsgeschwindigkeit von verzinktem Stahl in Salzwasser hängt stark von der Wassertemperatur ab:

| Wassertemperatur | Relative Korrosionsrate | Typisches Revier | Confidence |
|-----------------|----------------------|-----------------|------------|
| 5–10°C | 0,6× | Nordeuropa Winter | estimated |
| 10–15°C | 0,8× | Nordeuropa Sommer, Nordatlantik | estimated |
| 15–20°C | 1,0× (Referenz) | Mittelmeer Frühling/Herbst | estimated |
| 20–25°C | 1,3× | Mittelmeer Sommer | estimated |
| 25–30°C | 1,7× | Karibik, Rotes Meer | estimated |
| >30°C | 2,0–2,5× | Persischer Golf, tropische Lagunen | estimated |

**Konsequenz:** Im tropischen Betrieb (>25°C Wassertemperatur) müssen die Wartungsintervalle um ca. 30–40 % verkürzt werden. Die Kettenlebensdauer reduziert sich entsprechend.

### 2.10 Interaktion der Komponenten — Systemdenken

Ein Ankersystem ist ein zusammenwirkendes System. Verschleiß an einer Komponente beschleunigt den Verschleiß anderer Komponenten:

| Primärproblem | Sekundäreffekt | Beschleunigungsfaktor | Confidence |
|---------------|---------------|----------------------|------------|
| Verschlissener Gypsy | Beschleunigter Kettenverschleiß | ×1,5–2,0 | estimated |
| Verschlissene Kette | Beschleunigter Gypsy-Verschleiß | ×1,3–1,5 | estimated |
| Blockierte Bugrolle | Kettenverschleiß an Bugrolle-Stelle ×3–5 | ×3,0–5,0 | estimated |
| Fehlender Snubber | Windlass-Getriebe-Überlastung | ×2,0–3,0 | documented |
| Defekter Kettenstopper | Windlass-Clutch-Verschleiß | ×2,0 | documented |
| Verstopfte Kettenkasten-Drainage | Kettenkorrosion durch stehendes Salzwasser | ×1,5 | estimated |
| Falscher Ketten-Standard | Gypsy-Verschleiß und Ketten-Verschleiß gleichzeitig | ×3,0–5,0 | documented |

**Schlussfolgerung:** Es genügt nicht, einzelne Komponenten isoliert zu warten. Das Gesamtsystem muss aufeinander abgestimmt sein, und die Wechselwirkungen müssen bei der Zustandsbewertung berücksichtigt werden.

### 2.11 AYDI-Relevanz: Automatisierte Zustandsbewertung

AYDI bewertet Ankersysteme in drei Modi:

1. **Fotobewertung (Pipeline B):** Rost, Bewuchs, Verzinkungszustand, Gypsy-Zähne, Snubber-Chafe aus Fotos erkennen
2. **Datenbasierte Bewertung (Pipeline A):** Alter, Betriebsstunden, letzte Wartung → Verschleißprognose
3. **Textbasierte Bewertung (Pipeline C):** Serviceberichte, Surveyor-Reports → Musterextraktion

Die in dieser Datei dokumentierten Verschleißbilder, Messverfahren und Grenzwerte bilden die Wissensbasis für alle drei Pipelines.

---

## 3. Wartungsintervalle

### 3.1 Übersicht — Intervall-Matrix nach Komponente und Nutzung

Die folgenden Intervalle gelten als Empfehlung. Bei intensiver Nutzung (Blauwasser, Charter) oder aggressivem Umfeld (tropisch, stark strömend) sind kürzere Intervalle angezeigt.

#### 3.1.1 Anker

| Wartungsarbeit | Gelegenheitssegler (<50 Nächte/a) | Vielsegler (50–150 Nächte/a) | Blauwasser (>150 Nächte/a) | Charter | Confidence |
|----------------|----------------------------------|------------------------------|---------------------------|---------|------------|
| Sichtprüfung allgemein | Saisonstart + -ende | Monatlich | Alle 2 Wochen | Wöchentlich | documented |
| Schweißnaht-Inspektion | Jährlich | Halbjährlich | Vierteljährlich | Monatlich | documented |
| Oberflächenschutz prüfen | Jährlich | Halbjährlich | Vierteljährlich | Monatlich | estimated |
| Schäkel-Kontrolle | Jährlich | Halbjährlich | Vierteljährlich | Monatlich | documented |
| Gelenk/Wippe schmieren | Jährlich | Halbjährlich | Vierteljährlich | Monatlich | estimated |
| Grundlegende Reinigung | Nach jedem Gebrauch | Nach jedem Gebrauch | Nach jedem Gebrauch | Täglich | documented |
| Feuerverzinkung prüfen | Alle 2 Jahre | Jährlich | Jährlich | Halbjährlich | estimated |
| Nachverzinkung/Neukauf | Bei <30 % Restverzinkung | Bei <30 % Restverzinkung | Bei <30 % Restverzinkung | Bei <40 % | estimated |

#### 3.1.2 Ankerkette

| Wartungsarbeit | Gelegenheitssegler | Vielsegler | Blauwasser | Charter | Confidence |
|----------------|-------------------|------------|------------|---------|------------|
| Sichtprüfung auf Rost | Saisonstart + -ende | Monatlich | Alle 2 Wochen | Wöchentlich | documented |
| Durchmesser-Messung (Stichprobe) | Jährlich | Halbjährlich | Vierteljährlich | Vierteljährlich | measured |
| Vollständige Durchmesser-Messung | Alle 3 Jahre | Alle 2 Jahre | Jährlich | Jährlich | measured |
| Kalibrierung/Teilung prüfen | Alle 3 Jahre | Alle 2 Jahre | Jährlich | Jährlich | measured |
| Markierungen erneuern | Jährlich | Jährlich | Halbjährlich | Vierteljährlich | documented |
| Kettenkasten-Reinigung | Jährlich | Halbjährlich | Vierteljährlich | Monatlich | documented |
| Verzinkung bewerten | Jährlich | Halbjährlich | Vierteljährlich | Vierteljährlich | estimated |
| Bewuchs entfernen | Bei Bedarf | Bei Bedarf | Monatlich | Wöchentlich | estimated |
| End-Befestigung prüfen | Jährlich | Halbjährlich | Vierteljährlich | Monatlich | documented |
| Austausch (vollständig) | Nach 10–15 Jahren | Nach 8–12 Jahren | Nach 5–8 Jahren | Nach 3–5 Jahren | estimated |

#### 3.1.3 Ankerwinde (Windlass)

| Wartungsarbeit | Gelegenheitssegler | Vielsegler | Blauwasser | Charter | Confidence |
|----------------|-------------------|------------|------------|---------|------------|
| Funktionstest (Auf/Ab) | Vor jedem Gebrauch | Vor jedem Gebrauch | Vor jedem Gebrauch | Täglich | documented |
| Sichtprüfung außen | Saisonstart | Monatlich | Monatlich | Wöchentlich | documented |
| Gypsy-Inspektion | Jährlich | Halbjährlich | Vierteljährlich | Monatlich | documented |
| Clutch prüfen/einstellen | Jährlich | Halbjährlich | Vierteljährlich | Monatlich | documented |
| Getriebe-Schmierung | Jährlich | Halbjährlich | Vierteljährlich | Vierteljährlich | measured |
| Motor-Kohlen prüfen (DC) | Alle 2 Jahre | Jährlich | Jährlich | Halbjährlich | measured |
| Dichtungen/O-Ringe prüfen | Jährlich | Halbjährlich | Vierteljährlich | Vierteljährlich | documented |
| Elektrik-Anschlüsse prüfen | Jährlich | Halbjährlich | Vierteljährlich | Vierteljährlich | measured |
| Stromaufnahme messen | Jährlich | Halbjährlich | Vierteljährlich | Vierteljährlich | measured |
| Solenoid/Relais prüfen | Jährlich | Halbjährlich | Vierteljährlich | Vierteljährlich | measured |
| Komplette Revision | Alle 5–7 Jahre | Alle 3–5 Jahre | Alle 2–3 Jahre | Alle 1–2 Jahre | estimated |

#### 3.1.4 Snubber/Ruckdämpfer

| Wartungsarbeit | Gelegenheitssegler | Vielsegler | Blauwasser | Charter | Confidence |
|----------------|-------------------|------------|------------|---------|------------|
| Sichtprüfung Chafe | Vor jedem Gebrauch | Vor jedem Gebrauch | Vor jedem Gebrauch | Täglich | documented |
| Scheuerschutz prüfen | Saisonstart | Monatlich | Monatlich | Wöchentlich | documented |
| Karabiner/Haken prüfen | Saisonstart | Monatlich | Vierteljährlich | Monatlich | documented |
| Elastizität prüfen | Jährlich | Halbjährlich | Vierteljährlich | Vierteljährlich | estimated |
| UV-Schäden prüfen | Jährlich | Halbjährlich | Vierteljährlich | Monatlich | documented |
| Austausch (Nylon-Snubber) | Alle 3–5 Jahre | Alle 2–3 Jahre | Alle 1–2 Jahre | Jährlich | estimated |
| Austausch (Gummi-Snubber) | Alle 5–8 Jahre | Alle 3–5 Jahre | Alle 2–3 Jahre | Alle 2 Jahre | estimated |

#### 3.1.5 Bugrolle (Bow Roller)

| Wartungsarbeit | Gelegenheitssegler | Vielsegler | Blauwasser | Charter | Confidence |
|----------------|-------------------|------------|------------|---------|------------|
| Sichtprüfung Rolle/Bolzen | Saisonstart | Monatlich | Monatlich | Wöchentlich | documented |
| Bolzen auf Spiel prüfen | Jährlich | Halbjährlich | Vierteljährlich | Monatlich | measured |
| Rolle schmieren | Jährlich | Halbjährlich | Vierteljährlich | Monatlich | documented |
| Sicherungssplinte prüfen | Jährlich | Halbjährlich | Vierteljährlich | Monatlich | documented |
| Befestigung (Schrauben/Muttern) | Jährlich | Halbjährlich | Vierteljährlich | Monatlich | measured |
| Rissbildung (Edelstahl/Alu) | Jährlich | Halbjährlich | Vierteljährlich | Vierteljährlich | documented |
| Austausch Rollenachse | Bei Verschleiß | Bei Verschleiß | Alle 5 Jahre | Alle 3 Jahre | estimated |

#### 3.1.6 Kettenstopper

| Wartungsarbeit | Gelegenheitssegler | Vielsegler | Blauwasser | Charter | Confidence |
|----------------|-------------------|------------|------------|---------|------------|
| Funktionsprüfung | Vor jedem Gebrauch | Vor jedem Gebrauch | Vor jedem Gebrauch | Täglich | documented |
| Sichtprüfung Verschleiß | Saisonstart | Monatlich | Monatlich | Wöchentlich | documented |
| Schmierung Mechanik | Halbjährlich | Vierteljährlich | Monatlich | Monatlich | documented |
| Haken/Klauen-Verschleiß | Jährlich | Halbjährlich | Vierteljährlich | Monatlich | documented |
| Befestigung am Deck | Jährlich | Halbjährlich | Vierteljährlich | Vierteljährlich | measured |

### 3.2 Saisonale Wartungskalender

#### 3.2.1 Mittelmeer-Saison (April–Oktober)

| Zeitpunkt | Maßnahmen | Dauer | Confidence |
|-----------|-----------|-------|------------|
| **April (Saisonstart)** | Vollständige Systeminspektion, Kette auslegen und prüfen, Windlass-Funktionstest, Gypsy reinigen, Kettenkasten reinigen und prüfen, Snubber prüfen, Bugrolle schmieren, Elektrik-Check | 4–6 h | documented |
| **Juni (Mitte Saison)** | Ketten-Sichtprüfung, Windlass-Gypsy visuell, Snubber-Chafe-Check, Kettenmarkierungen prüfen, Bewuchs prüfen | 1–2 h | documented |
| **August (Hochsaison)** | Wie Juni + Kettenstopper-Funktion, Schäkel-Sicherung, Verzinkung Stichprobe | 1–2 h | documented |
| **Oktober (Saisonende)** | Vollständige Reinigung, Kette komplett auslegen/spülen/trocknen, Windlass konservieren, Kette mit Konservierungsspray, Kettenkasten desinfizieren, Snubber einlagern, Winterabdeckung | 4–8 h | documented |

#### 3.2.2 Nordeuropa-Saison (Mai–September)

| Zeitpunkt | Maßnahmen | Dauer | Confidence |
|-----------|-----------|-------|------------|
| **Mai (Saisonstart)** | Wie Mittelmeer April + Frostschäden-Check, Drainage prüfen, Windlass-Motor Probelauf (langsam hochfahren nach Winterpause) | 5–7 h | documented |
| **Juli (Mitte)** | Standard-Zwischencheck | 1–2 h | documented |
| **September (Saisonende)** | Wie Mittelmeer Oktober + Wasserentfernung aus allen Hohlräumen, Windlass-Heizung prüfen (falls vorhanden), Frostschutz-Maßnahmen | 5–8 h | documented |
| **November (Winterlager)** | Endkontrolle, alle Komponenten trocken einlagern, Getriebe nachfetten, Batterie-Abklemmen | 2–3 h | documented |

#### 3.2.3 Ganzjahresbetrieb (Tropen/Blauwasser)

| Intervall | Maßnahmen | Dauer | Confidence |
|-----------|-----------|-------|------------|
| **Alle 2 Wochen** | Sichtprüfung Kette (erste 20 m), Gypsy-Check, Snubber-Chafe | 30 min | documented |
| **Monatlich** | Bugrolle schmieren, Kettenstopper prüfen, Windlass-Sichtprüfung, Bewuchs entfernen | 1 h | documented |
| **Vierteljährlich** | Kette komplett auslegen und prüfen, Durchmesser-Stichprobe, Windlass-Service, Kettenkasten reinigen | 3–4 h | documented |
| **Halbjährlich** | Vollständiger Service wie Saisonstart/ende + Getriebefett erneuern + Kohlen prüfen | 4–6 h | documented |
| **Jährlich** | Komplett-Revision: Kette messen, Windlass zerlegen, Bugrolle ausbauen, alle Verbindungen prüfen | 8–12 h | documented |

### 3.3 Betriebsstunden-basierte Intervalle für Ankerwinden

| Betriebsstunden | Wartungsumfang | Typische Entsprechung | Confidence |
|-----------------|---------------|----------------------|------------|
| 0–50 h | Einlauf: nach 10 h erste Inspektion, Getriebefett prüfen | 1–2 Saisons Gelegenheitssegler | documented |
| 50 h | Kohlen-Erstprüfung, Gypsy-Verschleiß messen (Baseline) | — | measured |
| 100 h | Getriebefett wechseln, Dichtungen prüfen, Kohlen messen | 3–5 Saisons Gelegenheitssegler | documented |
| 200 h | Große Inspektion: Getriebe öffnen, Lager prüfen, Kohlen tauschen wenn <50 % | 2–3 Saisons Blauwasser | documented |
| 300 h | Revision empfohlen: Getriebe, Lager, Dichtungen, Kohlen, Solenoid | — | estimated |
| 500 h | Generalüberholung oder Austausch erwägen | — | estimated |

**Betriebsstunden-Schätzung (wenn kein Zähler vorhanden):**
- Pro Ankermanöver (Auf + Ab): ca. 3–8 Minuten = 0,05–0,13 h
- 100 Ankermanöver pro Saison (Vielsegler Mittelmeer): ca. 5–13 h/Saison
- 250 Ankermanöver pro Saison (Blauwasser): ca. 12–32 h/Saison

### 3.4 Umgebungsbedingte Intervallanpassung

| Umgebungsfaktor | Intervallanpassung | Begründung | Confidence |
|-----------------|-------------------|------------|------------|
| Salzwasser (Standard) | Basis-Intervall | Referenz | documented |
| Süßwasser überwiegend | Intervall × 1,5 | Weniger Korrosion | estimated |
| Tropisch (>28°C Wassertemp.) | Intervall × 0,7 | Schnellerer Bewuchs, aggressivere Korrosion | estimated |
| Stark strömend (>2 kn Tide) | Intervall × 0,7 | Höherer Abrieb | estimated |
| Industriehafen (verschmutztes Wasser) | Intervall × 0,5 | Chemische Korrosion | estimated |
| Sandgrund überwiegend | Intervall × 0,8 | Abrasiver Verschleiß an Kette | estimated |
| Felsgrund überwiegend | Intervall × 0,6 | Starker Abrieb, Schlagbeanspruchung | estimated |
| Schlick/Ton | Intervall × 1,2 | Geringer Abrieb, aber Reinigungsbedarf | estimated |

---

## 4. Schritt-für-Schritt Wartung

### 4.1 Anker-Inspektion und Wartung

#### 4.1.1 Allgemeine Sichtprüfung

**Benötigtes Werkzeug:** Taschenlampe, Lupe (10×), Drahtbürste, Kreide/Marker

**Ablauf:**

1. **Anker vom Bug nehmen** — Anker an Deck oder an Land legen, gut zugänglich
2. **Grobreinigung** — Schlamm, Sand, Bewuchs mit Süßwasser abspülen
3. **Schaft prüfen:**
   - Geradheit: Schaft auf ebener Fläche auflegen, Krümmung erkennen
   - Toleranz: max. 5 mm Abweichung pro Meter Schaftlänge
   - Risse: besonders an Übergängen Schaft→Krone und Schaft→Schäkelöse
4. **Fluke(n) prüfen:**
   - Verformung: Fluken-Winkel mit Original vergleichen (Herstellerangabe)
   - Toleranz: max. 3° Abweichung vom Soll-Flukenwinkel
   - Schärfe: Kanten sollen definiert sein, nicht rundgeschliffen
5. **Schäkelöse (Ringöse) prüfen:**
   - Wandstärke messen (Messschieber): min. 80 % des Neuwerts
   - Ovalität: max. 10 % Abweichung von rund
   - Risse: besonders an Schweißnähten
6. **Wippe/Gelenk prüfen (bei Schwenkanker):**
   - Leichtgängigkeit: Wippe muss frei schwenken
   - Spiel: axial max. 2 mm, radial max. 1 mm
   - Sicherung: Splint/Bolzen vorhanden und intakt

**Bewertungsmatrix:**

| Befund | Bewertung | Maßnahme | Confidence |
|--------|-----------|----------|------------|
| Schaft gerade, keine Risse | OK | Keine | measured |
| Schaft leicht verbogen (<5 mm/m) | Beobachten | Nächste Inspektion verkürzen | measured |
| Schaft stark verbogen (>5 mm/m) | KRITISCH | Anker austauschen | measured |
| Schweißnaht-Riss sichtbar | KRITISCH | Anker sofort austauschen | visual_high |
| Flukenwinkel >3° abweichend | Eingeschränkt | Anker nachrichten lassen oder tauschen | measured |
| Schäkelöse <80 % Wandstärke | KRITISCH | Anker austauschen | measured |
| Verzinkung >60 % | Gut | Nächste reguläre Prüfung | estimated |
| Verzinkung 30–60 % | Eingeschränkt | Nachverzinkung planen | estimated |
| Verzinkung <30 % | Austausch empfohlen | Nachverzinkung unwirtschaftlich | estimated |

#### 4.1.2 Schweißnaht-Detailprüfung

Schweißnähte sind die häufigste Versagensstelle bei modernen Ankern. Besonders betroffen:
- Schaft-Krone-Verbindung (höchste Biegebelastung)
- Fluken-Krone-Verbindung (Ausbruch-Belastung)
- Verstärkungsrippen

**Prüfverfahren (Eigner-Level):**

1. Bereich gründlich mit Drahtbürste reinigen (bis auf blankes Metall)
2. Lupe 10× verwenden, Naht systematisch absuchen
3. Kreide-Methode: weiße Kreide auf Naht reiben, dann abwischen — Risse werden sichtbar als dunkle Linien in der Kreide
4. Klopftest: mit kleinem Hammer leicht auf Naht klopfen — dumpfer Klang = OK, heller/klingender Klang = möglicher Riss

**Prüfverfahren (Surveyor-Level):**

1. Farbeindringprüfung (Penetrant Testing): Reiniger → Eindringmittel (rot) → Entwickler (weiß)
2. Ergebnis: Risse erscheinen als rote Linien auf weißem Grund
3. Dokumentation: fotografieren mit Maßstab

#### 4.1.3 Oberflächenschutz erneuern

**Feuerverzinkter Stahl-Anker:**
- Verzinkungsverlust: ca. 5–15 µm/Jahr im Salzwasser (abhängig von Nutzung)
- Neue Verzinkung: 80–120 µm (Feuerverzinkung) bzw. 15–25 µm (galvanische Verzinkung)
- Nachverzinkung lohnt ab <30 % Restverzinkung
- Kosten Nachverzinkung: 150–400 € je nach Ankergröße (documented)
- Alternative: Zinkspray als Zwischenlösung (Haltbarkeit ca. 6–12 Monate)

**Edelstahl-Anker (316L):**
- Passivierung prüfen: gleichmäßig matte Oberfläche = OK
- Lochfraß: braune/orangene Punkte = Passivschichtdefekte
- Behandlung: Beizen mit Beizpaste (z.B. Avesta 401) + Passivierung
- Politur: nur kosmetisch, verbessert nicht die Korrosionsbeständigkeit

**Aluminium-Anker (Fortress etc.):**
- Eloxalschicht prüfen: gleichmäßig silber-grau = OK
- Weiße Ausblühungen = Oxidation → nicht kritisch, aber kosmetisch unschön
- Kontaktkorrosion: KEINE Edelstahlschrauben direkt in Alu → Isolierung erforderlich
- Reinigung: nur mit pH-neutralen Mitteln, KEIN alkalischer Reiniger

### 4.2 Ankerketten-Wartung und Messung

#### 4.2.1 Kette auslegen und Sichtprüfung

**Vorgehensweise:**

1. **Sicheren Platz wählen:** Steg, Werftgelände oder flacher Strand
2. **Kette komplett auslegen:** Windlass langsam laufen lassen, Kette auf Plane oder Steg
3. **Systematisch abgehen:** alle 5 m einen Abschnitt prüfen
4. **Prüfpunkte pro Abschnitt:**
   - Rostgrad: oberflächlich / tiefgehend / durchgerostet
   - Verzinkung: glänzend / matt / fleckig / fehlend
   - Verformung: Glieder oval, aufgebogen, verdreht
   - Fremdkörper: Muscheln, Draht, Leinenreste
   - Markierungen: noch lesbar / erneuern

**Rostgrad-Bewertung:**

| Grad | Beschreibung | Maßnahme | Confidence |
|------|-------------|----------|------------|
| 0 — Neuwertig | Vollständige Verzinkung, glänzend | Keine | visual_high |
| 1 — Leicht | Vereinzelte Rostflecken, Verzinkung >70 % | Beobachten | visual_high |
| 2 — Mittel | Großflächige Roststellen, Verzinkung 30–70 % | Zinkspray, mittelfristig tauschen | visual_medium |
| 3 — Stark | Kein Zink mehr, durchgehend Rost, aber Glieder intakt | Tausch planen (nächste Saison) | visual_high |
| 4 — Kritisch | Tiefenrost, Glieder geschwächt, Materialabtrag messbar | Sofort tauschen | visual_high |

#### 4.2.2 Durchmesser-Messung

Die Kettenglieddurchmesser-Messung ist die wichtigste quantitative Prüfung:

**Werkzeug:** Messschieber (digital, 0,01 mm Auflösung)

**Messpunkte pro Glied:**
- Punkt A: Krümmung oben (dünnste Stelle durch Gypsy-Abrieb)
- Punkt B: Gerade Seite (dünnste Stelle durch Rollenabrieb)
- Punkt C: Krümmung unten
- Mindestens 3 Messwerte pro Glied, kleinsten Wert verwenden

**Messhäufigkeit:**
- Stichprobe: alle 5 m ein Glied messen → 10–20 Messwerte bei 50–100 m Kette
- Vollmessung: alle 1 m ein Glied → 50–100 Messwerte
- Fokus: erste 30 m (höchster Verschleiß, meiste Nutzung)

**Grenzwerte:**

| Ketten-Nenndurchmesser | Neuwert (mm) | Warnung bei (mm) | Austausch bei (mm) | % Reduktion max. | Confidence |
|------------------------|-------------|-------------------|-------------------|-----------------|------------|
| 6 mm | 6,0 | 5,5 | 5,3 | 12 % | documented |
| 8 mm | 8,0 | 7,3 | 7,0 | 12 % | documented |
| 10 mm | 10,0 | 9,1 | 8,8 | 12 % | documented |
| 12 mm | 12,0 | 10,9 | 10,6 | 12 % | documented |
| 13 mm | 13,0 | 11,8 | 11,4 | 12 % | documented |
| 14 mm | 14,0 | 12,7 | 12,3 | 12 % | documented |
| 16 mm | 16,0 | 14,5 | 14,1 | 12 % | documented |

**Hinweis:** Die 12 %-Grenze basiert auf der ISO-1704-Empfehlung. Manche Surveyor setzen den Grenzwert bei 10 % an (konservativer). Bei Blauwasser-Yachten empfehlen wir 10 % als Austauschgrenze.

#### 4.2.3 Kalibrierung/Teilung prüfen

Die Kettenteilung muss zum Gypsy passen. Falsche Teilung führt zu Springen, Klemmen oder übermäßigem Verschleiß.

**Messung:**
- 10 aufeinanderfolgende Glieder messen (gleiche Orientierung)
- Gesamtlänge durch 10 teilen = mittlere Teilung
- Vergleich mit Soll-Teilung (Hersteller-Datenblatt)
- Toleranz: ±2,5 % (ISO 1704)

**Typische Teilungen:**

| Kettengröße | Teilung kurz-gliedrig (mm) | Teilung lang-gliedrig (mm) | Confidence |
|-------------|---------------------------|---------------------------|------------|
| 6 mm | 19,2 | 28,0 | documented |
| 8 mm | 24,0 | 36,0 | documented |
| 10 mm | 28,0 | 44,0 | documented |
| 12 mm | 33,6 | 52,8 | documented |
| 13 mm | 36,4 | 57,2 | documented |

#### 4.2.4 Markierungen erneuern

**Markierungssysteme:**

| System | Material | Haltbarkeit | Kosten | Confidence |
|--------|----------|-------------|--------|------------|
| Farbmarkierung (Sprühlack) | Zink-Spray + Farbspray | 1–2 Saisons | Gering | documented |
| Kabelbinder | UV-beständige Kabelbinder | 1–3 Saisons | Gering | documented |
| Kettenmarkierer (Plastik-Clips) | Campbell/Muir Marker | 2–5 Saisons | Mittel | documented |
| Draht-Markierung | Edelstahldraht 1 mm | 5+ Saisons | Gering | estimated |
| Farbtupfer + Epoxy | 2K-Epoxid-Farbe | 3–5 Saisons | Mittel | documented |

**Empfohlenes Farbschema (weit verbreitet):**

| Kettenlänge | Farbe | Merkregel | Confidence |
|-------------|-------|-----------|------------|
| 10 m | Rot | Rot = 10 (R wie Rot, zehn) | estimated |
| 15 m | Weiß | — | estimated |
| 20 m | Blau | Blau = 20 | estimated |
| 25 m | Gelb | — | estimated |
| 30 m | Grün | Grün = 30 | estimated |
| 35 m | Orange | — | estimated |
| 40 m | Rot + Weiß | Kombination | estimated |
| 45 m | Weiß + Blau | Kombination | estimated |
| 50 m | Blau + Gelb | Kombination | estimated |

### 4.3 Ankerwinden-Service (Windlass)

#### 4.3.1 Äußere Inspektion

**Prüfpunkte:**

1. **Gehäuse:**
   - Risse in GFK-Abdeckung oder Metall-Gehäuse
   - Korrosion an Aluminium-Gehäuse (weiße Ausblühungen)
   - Dichtungen: Gummi-Einsätze in Decksdurchführung intakt?
   - Befestigungsschrauben/-muttern: fest? Korrodiert?

2. **Gypsy (Kettennuss):**
   - Zähne: scharfkantig (Neuwert) oder abgerundet (verschlissen)?
   - Passform zur Kette: Kette einlegen, soll in jeder Tasche satt liegen
   - Verschleiß: Gypsy-Taschentiefe messen (siehe 6.4)
   - Korrosion: besonders in den Zahntälern

3. **Trommel (Warping Drum):**
   - Oberfläche: glatt, keine tiefen Rillen
   - Freilauf: Trommel muss sich unabhängig vom Gypsy drehen können (bei kombinierten Winden)

4. **Clutch (Freilauf-Kupplung):**
   - Hebel/Handrad leichtgängig
   - In "Frei"-Stellung: Kette muss frei durchlaufen
   - In "Fest"-Stellung: Kette darf nicht durchrutschen (Test mit Handkraft)

#### 4.3.2 Windlass-Motor-Service (DC-Elektromotor)

**Sicherheit zuerst:**
- Hauptschalter AUS
- Sicherung am Batteriehauptverteiler ziehen
- Warten bis Kondensatoren entladen (30 Sekunden)

**Kohlebürsten prüfen/tauschen:**

1. Zugang zum Motor: Motordeckel abnehmen (typisch 4–6 Innensechskant-Schrauben)
2. Kohlebürsten lokalisieren: sitzen in Führungen am Kollektor
3. Kohlen herausziehen: Feder zurückdrücken, Kohle entnehmen
4. Messen: Länge mit Messschieber

| Kohlebürsten-Zustand | Restlänge (typisch) | Maßnahme | Confidence |
|----------------------|---------------------|----------|------------|
| Neu | 15–22 mm (modellabhängig) | Keine | measured |
| OK | >10 mm | Weiter verwenden | measured |
| Warnung | 6–10 mm | Ersatzkohlen beschaffen | measured |
| Tauschen | <6 mm | Sofort austauschen | measured |
| Abgebrochen/Verklemmt | — | Sofort austauschen, Kollektor prüfen | measured |

5. Kollektor prüfen:
   - Lamellen sauber und glatt: OK
   - Rillen zwischen Lamellen: mit spitzer Klinge reinigen (Mica Undercut)
   - Brandflecken: mit feinem Schleifpapier (400er) glätten
   - Tiefe Rillen oder Brandstellen: Kollektor muss abgedreht werden (Werkstatt)

6. Neue Kohlen einsetzen:
   - Kohlen passend zum Motor (Hersteller-Ersatzteil)
   - In Führung einsetzen, Feder aufsetzen
   - Freigängigkeit prüfen: Kohle muss in der Führung gleiten
   - Einlauf: erste 10 Betriebsminuten nur ohne Last laufen lassen

#### 4.3.3 Getriebe-Wartung

**Getriebefett wechseln:**

1. Zugang zum Getriebe: untere Gehäusehälfte öffnen (unter Deck)
2. Altes Fett entfernen: mit Spachtel und fusselfreiem Tuch
3. Zahnräder inspizieren:
   - Zahnflanken: gleichmäßiger Abtrag = normal. Grübchen (Pitting) = Überbelastung
   - Lagerspiel: Welle von Hand drehen, Spiel fühlen
   - Geräusche: kratzend = Fremdkörper, knackend = Lagerschaden
4. Neues Fett einbringen:
   - Zahnflanken dünn einstreichen
   - Lager mit Fett füllen (nicht überfüllen — max. 70 % des Hohlraums)
   - Getriebegehäuse ca. 60 % befüllen

**Getriebeöl (bei ölgeschmierten Getrieben, z.B. manche Lofrans):**

1. Ölstand prüfen: Schauglas oder Peilstab
2. Öl ablassen: Ablassschraube öffnen, Altöl auffangen
3. Spülen: mit 50 ml neuem Öl → ablassen
4. Neues Öl einfüllen: bis Markierung (typisch 80–150 ml)

#### 4.3.4 Gypsy-Inspektion und Austausch

**Gypsy-Verschleiß messen:**

Der Gypsy ist das kritischste Verschleißteil der Ankerwinde. Verschlissene Gypsy-Zähne führen zu:
- Kette springt über (gefährlich — unkontrollierter Kettenfall)
- Kette klemmt (Windlass blockiert unter Last)
- Erhöhter Kettenverschleiß
- Ungleichmäßiger Lauf, Vibrationen

**Messmethode:**
1. Neues Kettenglied in Gypsy einlegen
2. Spiel zwischen Kettenglied und Zahnflanke messen
3. Neuwert: 0,5–1,0 mm Spiel
4. Grenzwert: >2,0 mm Spiel → Gypsy tauschen
5. Alternativ: Zahnhöhe messen und mit Herstellerangabe vergleichen

**Gypsy-Tausch:**
1. Sicherungsring/Mutter am Gypsy-Ende lösen (Spezialwerkzeug oft nötig)
2. Gypsy von der Welle abziehen (ggf. Abzieher verwenden)
3. Welle und Keil prüfen: Verschleiß, Korrosion
4. Neuen Gypsy aufsetzen: Keil einlegen, auf korrekten Sitz achten
5. Sichern: Mutter mit vorgeschriebenem Drehmoment anziehen
6. Test: Kette einlegen, manuell drehen, satter Sitz prüfen

#### 4.3.5 Bugrolle-Wartung

**Rollenachse und Lager:**

1. Sicherungssplint entfernen
2. Bolzen herausziehen (ggf. von einer Seite klopfen)
3. Rolle abnehmen
4. Lager prüfen:
   - Kunststoff-Buchse: Ovalität messen (max. 0,5 mm)
   - Kugellager (selten): auf Laufgeräusch prüfen
   - Bronze-Buchse: Verschleißmaß prüfen
5. Bolzen prüfen:
   - Ovalität: max. 0,3 mm
   - Korrosion: Lochfraß an 316L = tauschen
   - Verformung: gerade auflegen, Biegung sichtbar?
6. Rolle prüfen:
   - Lauffläche: Rillen durch Kettenabrieb
   - Flanken: Risse, Ausbrüche
   - Edelstahl-Rollen: Rissbildung prüfen (besonders Schweißnähte)
7. Zusammenbau:
   - Neues Fett auf Bolzen und in Buchse
   - Rolle aufsetzen, Bolzen einführen
   - Neuen Sicherungssplint einsetzen (IMMER neu, nie wiederverwenden)

**Bugrolle-Befestigung am Deck:**

| Prüfpunkt | Methode | Grenzwert | Confidence |
|-----------|---------|-----------|------------|
| Schrauben/Bolzen fest | Drehmomentschlüssel | Herstellerangabe ±10 % | measured |
| GFK-Unterlage intakt | Klopftest, Sichtprüfung | Keine Delamination | visual_medium |
| Dichtung intakt | Sichtprüfung, Wassertest | Kein Wasser unter Deck | visual_high |
| Backing Plate vorhanden | Von unter Deck prüfen | Muss vorhanden sein | visual_high |
| Spiel in Befestigung | Händisch rütteln | Kein fühlbares Spiel | measured |

#### 4.3.6 Kettenkasten-Reinigung und Wartung

**Warum wichtig:**
- Verschmutzter Kettenkasten = Geruchsbelästigung (anaerobe Zersetzung)
- Verstopfte Drainage = Wasser im Vorschiff = Trimmprobleme
- Muschel-/Algenkrusten = Kettenstau, Windlass-Überlastung

**Vorgehen:**

1. **Kette komplett auslegen** (an Land oder auf Steg)
2. **Grobreinigung:** Schlamm, Muschelreste, Algen mit Spachtel entfernen
3. **Hochdruckreiniger** (wenn möglich) oder Eimer + Bürste
4. **Desinfizieren:**
   - Option A: Verdünnte Essigessenz (1:5) — umweltfreundlich, wirksam gegen Geruch
   - Option B: Verdünnte Chlorlösung (1:20) — stärker, aber aggressiver
   - Option C: Spezialreiniger (z.B. Yachticon Bilge Cleaner)
   - 30 Minuten einwirken lassen, dann abspülen
5. **Drainage prüfen:**
   - Wasser einfüllen: muss in max. 30 Sekunden abfließen
   - Rohr/Schlauch prüfen: Knicke, Verstopfungen
   - Rückschlagventil (falls vorhanden): Funktion testen
6. **Trocknen lassen** (24 h bei offenem Deckel)
7. **Kette zurücklegen:** sauber, trocken, ggf. mit Konservierungsspray

### 4.4 Verbindungselemente — Schäkel, Wirbel, Kettenvorlauf

#### 4.4.1 Schäkel-Wartung

**Schäkel zwischen Kette und Anker:**
1. Schäkel demontieren (Bolzen lösen — bei guter Pflege von Hand möglich)
2. Bolzen prüfen:
   - Durchmesser messen: min. 90 % Neuwert
   - Gewinde: gängig, nicht korrodiert, nicht beschädigt
   - Ovalität: max. 0,3 mm
   - Oberfläche: keine Riefen, kein Lochfraß
3. Bügel prüfen:
   - Öffnungsweite messen: max. 110 % Neuwert (Aufweitung = Überlastung)
   - Rissbildung: besonders in den Radien
   - Verzinkung/Korrosion
4. Zusammenbau:
   - Bolzen mit Tef-Gel einsetzen (Anti-Seize + galvanischer Schutz)
   - Bolzen handfest anziehen + Sicherungsdraht (316L, 1,0–1,5 mm)
   - KEIN Loctite auf Schäkelbolzen (muss im Notfall lösbar sein)

**Sicherungsmethoden für Schäkelbolzen:**

| Methode | Sicherheit | Lösbarkeit | Empfohlen für | Confidence |
|---------|-----------|------------|---------------|------------|
| Edelstahl-Sicherungsdraht | Sehr hoch | Gut (Draht durchschneiden) | Dauerverbindungen (Anker-Kette) | documented |
| Kabelbinder (UV-beständig) | Mittel | Sehr gut | Temporäre Verbindungen | documented |
| Loctite 243 (mittelfest) | Hoch | Mittel (Wärme + Werkzeug) | Bugrolle-Schrauben | documented |
| Sicherungssplint | Hoch | Gut | Bugrolle-Bolzen | documented |
| Gegenkontern (Mutter) | Sehr hoch | Gut | Windlass-Befestigung | documented |

#### 4.4.2 Wirbel-Wartung (Swivel)

1. Wirbel demontieren (Schäkel an beiden Seiten lösen)
2. Drehbarkeit prüfen: soll von Hand leicht drehen
3. Bolzen/Achse prüfen: Ovalität, Korrosion
4. Lager prüfen (bei Kugellager-Wirbeln): Laufgeräusch, Spiel
5. Reinigen: Salzwasser mit Süßwasser spülen, alle Spalten
6. Schmieren: Tef-Gel auf Lagerflächen, Bolzen
7. Zusammenbau: auf korrekte Einbaulage achten (Gabel-/Augen-Orientierung)

**Wirbel-Austauschkriterien:**

| Kriterium | Grenzwert | Prüfmethode | Confidence |
|-----------|-----------|-------------|------------|
| Bolzen-Ovalität | >10 % | Messschieber, 2 Achsen | measured |
| Drehbewegung | Hakelig, festgehend | Handdrehung | visual_high |
| Sichtbare Risse | Jegliche Risse | Lupe, ggf. Farbeindringprüfung | visual_high |
| Verformung des Bügels | Sichtbare Biegung | Vergleich mit Neuwert | visual_high |
| WLL nicht mehr gewährleistet | Bei >5 % Materialabtrag | Messschieber | measured |

#### 4.4.3 Kettenvorlauf (Kette-Leine-Übergang)

Falls eine Kombination aus Kette und Leine verwendet wird:

1. Kette-Leine-Verbindung prüfen:
   - Spleißauge: Spleißlänge min. 12× Seil-Durchmesser
   - Schäkel: korrekte Größe, gesichert
   - Kausche: nicht verformt, Seil liegt satt an
2. Übergangsstelle ist höchste Beanspruchung → sorgfältig prüfen
3. Leinenabschnitt: Chafe am Übergang zur Kette häufig → Scheuerschutz

### 4.5 Ankerbeleuchtung und Elektronik

#### 4.5.1 Ankerlaterne

**Prüfpunkte Saisonstart:**
1. Funktion: einschalten, Licht prüfen (LED oder Glühbirne)
2. Sichtbarkeit: 360° Rundumstrahlung gewährleistet? (COLREG Rule 30: 2 sm Tragweite)
3. Befestigung: Masttopp-Halterung fest, Kabel intakt
4. Dichtung: O-Ring prüfen (Wassereintritt = Kurzschluss)
5. Kontakte: sauber, nicht korrodiert
6. Bei LED: Farbtemperatur korrekt (weiß, nicht gelblich — Alterungszeichen)

#### 4.5.2 Kettenzähler

**Funktionsprinzip:** Magnetsensor am Kettenführungsrohr zählt vorbeilaufende Glieder.

**Wartung:**
1. Sensor reinigen (Metallspäne, Magnetpartikel können Fehlzählung verursachen)
2. Sensorabstand prüfen: typisch 3–5 mm zur Kette (Herstellerangabe beachten)
3. Kalibrierung: bekannte Kettenlänge auslegen, Zählerstand vergleichen
4. Kabel/Stecker: Korrosion, Wasserdichtheit
5. Display: Lesbarkeit bei Sonnenlicht

#### 4.5.3 Fernbedienung (kabellos)

**Wartung:**
1. Batterie: Ladezustand prüfen, Kontakte reinigen
2. Wasserdichtheit: Dichtung prüfen (IPX6 oder besser erforderlich)
3. Reichweitentest: von verschiedenen Positionen auslösen
4. Kontaktpaarung: bei Bluetooth-Fernbedienungen ggf. neu pairen
5. Not-Stopp: Funktion des Not-Aus-Tasters prüfen

### 4.6 Saisonale Komplett-Wartungsanleitung (Zusammenfassung)

#### 4.6.1 Zeitplan Saisonstart-Wartung (detailliert)

**Tag 1 (Vormittag, ca. 3 h):**
1. Kettenkasten öffnen, Zustand beurteilen, ggf. lüften
2. Windlass-Hauptschalter EIN, kurzer Funktionstest (ohne Kette)
3. Kette komplett auslegen auf Steg/Plane
4. Kette grob reinigen (Süßwasser)

**Tag 1 (Nachmittag, ca. 3 h):**
5. Kettenmessung (Stichprobe alle 5 m)
6. Kette auf Verformungen, Markierungen, Verzinkung prüfen
7. Anker inspizieren (Schaft, Fluken, Schweißnähte, Schäkelöse)
8. Schäkel und Wirbel prüfen

**Tag 2 (Vormittag, ca. 2 h):**
9. Windlass: Gypsy reinigen, Clutch prüfen, ggf. Getriebefett
10. Bugrolle: reinigen, schmieren, Bolzen prüfen
11. Kettenstopper: Funktionstest
12. Snubber: Chafe, UV, Elastizität prüfen

**Tag 2 (Nachmittag, ca. 2 h):**
13. Kettenkasten reinigen (wenn nötig desinfizieren)
14. Drainage testen
15. Kette zurücklegen, Freilauf testen
16. Ankerlaterne, Kettenzähler, Fernbedienung prüfen
17. Dokumentation erstellen (Messwerte, Fotos, Befunde)

**Gesamtdauer:** ca. 8–10 h über 2 Tage (Eigner-Eigenleistung).

---

## 5. Schmiermittel und Konservierung

### 5.1 Übersicht — Schmiermittel nach Anwendungsbereich

| Anwendung | Empfohlenes Produkt | Typ | Alternativ | Confidence |
|-----------|-------------------|-----|------------|------------|
| Windlass-Getriebe | Lewmar Winch Grease / Lofrans Gearbox Grease | Lithium-EP-Fett NLGI 2 | Castrol LMX, Shell Gadus S2 | documented |
| Windlass-Motor (Kohleführung) | Dünn: WD-40 Specialist oder Ballistol | Kriechöl | Kontakt 60 | documented |
| Gypsy-Oberfläche | Tef-Gel oder Lanocote | Korrosionsschutz, nicht schmierend | Lanolin-Spray | documented |
| Bugrolle-Lager (Kunststoff) | Teflon-Spray trocken | Trockenschmierstoff | PTFE-Pulver | documented |
| Bugrolle-Lager (Bronze) | Marine-Fett (wasserfest) | Kalzium-Fett | Castrol LM | documented |
| Bugrolle-Bolzen | Marine-Fett + Tef-Gel | Anti-Seize + Schutz | Duralac | documented |
| Kettenstopper-Mechanik | Ballistol / WD-40 Marine | Universalöl | CRC 6-66 | documented |
| Clutch-Mechanismus | Hersteller-spezifisch | Siehe Handbuch | — | documented |
| Ankerkette (Konservierung) | Zinkspray + Lanolin-Spray | Korrosionsschutz | Owatrol Öl | estimated |
| Schäkel-Bolzen | Tef-Gel / Duralac | Anti-Seize, Anti-Galvanic | Lanocote | documented |

### 5.2 Windlass-Getriebefett im Detail

**Anforderungen:**
- Wasserfest (NLGI 2 oder 3)
- EP-Additive (Extreme Pressure) für Zahnradpaarungen
- Temperaturbereich: -10°C bis +80°C (Motorwärme + Sonneneinstrahlung)
- Verträglichkeit mit Dichtungsmaterialien (NBR, Viton)
- Salzwasserbeständig

**Empfohlene Fetttypen:**

| Produkt | Basis | NLGI | Temperatur | EP | Preis/kg | Confidence |
|---------|-------|------|------------|----|---------:|------------|
| Lewmar Winch Grease | Lithium | 2 | -20 bis +130°C | Ja | ~45 € | documented |
| Lofrans Gear Grease | Lithium | 2 | -15 bis +120°C | Ja | ~35 € | documented |
| Quick Windlass Grease | Lithium | 2 | -10 bis +120°C | Ja | ~40 € | documented |
| Shell Gadus S2 V220 2 | Lithium | 2 | -20 bis +130°C | Ja | ~15 € | documented |
| Castrol LMX | Lithium-Komplex | 2 | -30 bis +150°C | Ja | ~12 € | documented |
| Mobilgrease XHP 222 | Lithium-Komplex | 2 | -25 bis +150°C | Ja | ~14 € | documented |

**WARNUNG:** Niemals verschiedene Fetttypen mischen! Lithium + Kalzium = Verflüssigung. Altes Fett immer vollständig entfernen.

### 5.3 Ketten-Konservierung

**Für die Wintersaison:**

1. Kette komplett mit Süßwasser spülen (Salzkristalle entfernen)
2. Trocknen lassen (mind. 24 h)
3. Option A: **Zinkspray** aufsprühen (z.B. CRC Zinc-It, Würth Zinkspray)
   - Vorteile: kathodischer Schutz, einfache Anwendung
   - Nachteile: Abrieb im Gypsy, macht Kette rutschig
4. Option B: **Lanolin-Spray** (z.B. Fluid Film, Lanocote)
   - Vorteile: kriecht in Spalten, langfristiger Schutz, biologisch abbaubar
   - Nachteile: klebrig, zieht Schmutz an
5. Option C: **Owatrol-Öl** (Leinöl-basiert)
   - Vorteile: penetriert Rost, langfristiger Schutz
   - Nachteile: braucht Trocknungszeit (48 h), Geruch
6. Option D: **Heißes Leinöl-Tauchbad** (traditionelle Methode)
   - Vorteile: tiefste Penetration, langfristiger Schutz
   - Nachteile: Brandgefahr, aufwändig, nur an Land möglich

**Für die laufende Saison:**
- Leichter Lanolin-Spray alle 4–6 Wochen auf die ersten 20 m
- Kein Zinkspray während der Saison (Gypsy-Verschleiß!)

### 5.4 Bugrolle-Schmierung

**Kunststoff-Buchsen-Rollen (Nylon, Delrin, UHMWPE):**
- Trockenschmierstoff (PTFE-Spray) alle 3–6 Monate
- KEIN Fett auf Kunststoff — kann Material angreifen
- Ausnahme: wenn Hersteller Fettschmierung vorschreibt

**Bronze-Buchsen-Rollen:**
- Marine-Fett (wasserbeständig) alle 3–6 Monate
- Schmiernippel: Fettpresse verwenden bis Fett austritt
- Bolzen: Tef-Gel beim Zusammenbau

**Kugellager-Rollen (selten):**
- Dichtung prüfen: Wasser darf nicht ins Lager gelangen
- Marine-Lagerfett alle 12 Monate nachfetten (wenn Schmiernippel vorhanden)
- Bei Laufgeräusch: Lager tauschen

### 5.5 Anti-Seize und Korrosionsschutz für Verbindungselemente

**Tef-Gel (PTFE + Korrosionsinhibitor):**
- Anwendung: alle Metall-Metall-Verbindungen verschiedener Legierungen
- Verhindert galvanische Korrosion und Festfressen
- Schäkel-Bolzen, Bugrolle-Schrauben, Windlass-Befestigung

**Duralac (Chromat-basiert):**
- Anwendung: Alu-Edelstahl-Verbindungen
- Stärkerer galvanischer Schutz als Tef-Gel
- ACHTUNG: enthält Chromat — Hautschutz tragen, nicht in Gewässer

**Lanocote (Lanolin-basiert):**
- Anwendung: Universalschutz, alle Metalle
- Biologisch abbaubar
- Schwächerer Anti-Seize-Effekt als Tef-Gel
- Gut für regelmäßig gelöste Verbindungen (Schäkel)

### 5.6 Schmiermittel-Verträglichkeitsmatrix

| Bestehendes Fett → | Lithium | Lithium-Komplex | Kalzium | Polyurea | Silikon | Confidence |
|---------------------|---------|-----------------|---------|----------|---------|------------|
| **Lithium** | ✓ | ✓ (bedingt) | ✗ | ✗ | ✗ | documented |
| **Lithium-Komplex** | ✓ (bedingt) | ✓ | ✗ | ✗ | ✗ | documented |
| **Kalzium** | ✗ | ✗ | ✓ | ✗ | ✗ | documented |
| **Polyurea** | ✗ | ✗ | ✗ | ✓ | ✗ | documented |
| **Silikon** | ✗ | ✗ | ✗ | ✗ | ✓ | documented |

✓ = verträglich, ✗ = NICHT mischen (Verflüssigung, Additivausfall), bedingt = möglichst vermeiden

---

## 6. Verschleißerkennung und Messtechnik

### 6.1 Kettenglieder — Quantitative Messung

#### 6.1.1 Messpunkte und Technik

**Einzelglied-Messung (Messschieber):**

```
    ┌──────────┐
    │  Punkt C │  ← Krümmung oben (Kontakt Gypsy)
    │    ○○    │
    │   ○  ○   │  ← Punkt B: gerade Seite
    │   ○  ○   │
    │    ○○    │
    │  Punkt A │  ← Krümmung unten
    └──────────┘
```

- Punkt A: Messung an der Innenkrümmung (oft stärkster Verschleiß durch Gypsy-Eingriff)
- Punkt B: Messung an der geraden Seite (Kontakt zum Nachbarglied)
- Punkt C: Messung an der Außenkrümmung
- Jeder Punkt: 2 Messungen im 90°-Winkel → Ovalität erkennen

**Verschleißprofil einer Kette (typisch nach 8 Jahren Mittelmeer-Nutzung):**

| Position | Neuwert 10 mm | Gemessen (mm) | Reduktion | Bewertung | Confidence |
|----------|--------------|---------------|-----------|-----------|------------|
| 0–5 m (Ankeranschluss) | 10,0 | 9,2–9,5 | 5–8 % | OK | measured |
| 5–10 m (Hauptnutzung) | 10,0 | 8,8–9,1 | 9–12 % | Warnung | measured |
| 10–20 m (Häufige Nutzung) | 10,0 | 9,0–9,3 | 7–10 % | OK/Warnung | measured |
| 20–30 m (Gelegentlich) | 10,0 | 9,4–9,7 | 3–6 % | OK | measured |
| 30–50 m (Selten) | 10,0 | 9,6–9,9 | 1–4 % | OK | measured |
| 50+ m (Kaum genutzt) | 10,0 | 9,8–10,0 | 0–2 % | OK | measured |

#### 6.1.2 Automatisierte Verschleißprognose (AYDI)

Basierend auf Messdaten kann AYDI eine Verschleißprognose erstellen:

```
Verschleißrate R = (D_neu - D_gemessen) / Betriebsjahre [mm/Jahr]

Restlebensdauer T = (D_gemessen - D_grenze) / R [Jahre]

Beispiel: 10mm Kette, gemessen 9,1 mm nach 8 Jahren
  R = (10,0 - 9,1) / 8 = 0,1125 mm/Jahr
  T = (9,1 - 8,8) / 0,1125 = 2,67 Jahre
  → Austausch in ca. 2–3 Saisons empfohlen
```

### 6.2 Anker-Schweißnaht-Inspektion

#### 6.2.1 Visuelle Indikatoren

| Indikator | Bedeutung | Dringlichkeit | Confidence |
|-----------|-----------|---------------|------------|
| Gleichmäßige Schweißnaht, keine Verfärbung | Intakt | Keine Maßnahme | visual_high |
| Leichte Rostspuren an Schweißnaht | Verzinkung lokal aufgebraucht | Beobachten, Zinkspray | visual_high |
| Haarriss in Schweißnaht (<1 mm) | Ermüdungsriss beginnt | Farbeindringprüfung, mittelfristig tauschen | visual_medium |
| Sichtbarer Riss (>1 mm) | Aktiver Riss | SOFORT tauschen | visual_high |
| Materialverdickung/Wulst an Naht | Schweißfehler ab Werk | Farbeindringprüfung empfohlen | visual_medium |
| Rostunterwanderung unter Naht | Korrosion im Spalt | Tausch planen | visual_medium |
| Naht-Ablösung erkennbar | Bruchgefahr | SOFORT tauschen | visual_high |

#### 6.2.2 Farbeindringprüfung (Penetrant Testing)

**Benötigtes Material:** PT-Set (z.B. MR Chemie, Helling, Pfinder)
- Reiniger (Cleaner)
- Eindringmittel (Penetrant, rot)
- Entwickler (Developer, weiß)

**Ablauf:**
1. Oberfläche entfetten und reinigen (Cleaner aufsprühen, abwischen)
2. Trocknen lassen (2 Minuten)
3. Eindringmittel aufsprühen (gleichmäßig, dünn)
4. Einwirkzeit: 15–30 Minuten (je nach Herstellerangabe)
5. Überschüssiges Eindringmittel vorsichtig abwischen (NICHT absprühen)
6. Entwickler aufsprühen (gleichmäßig, dünne Schicht)
7. Warten: 10–30 Minuten
8. Auswertung: Rote Linien auf weißem Grund = Riss/Fehlstelle
9. Dokumentation: Foto mit Maßstab

### 6.3 Gypsy-Zahnverschleiß

#### 6.3.1 Verschleißmerkmale

| Verschleißstadium | Beschreibung | Auswirkung | Maßnahme | Confidence |
|-------------------|-------------|------------|----------|------------|
| Stadium 0 — Neu | Scharfe Zahnkanten, definierte Taschen | Optimaler Ketteneingriff | Keine | visual_high |
| Stadium 1 — Leicht | Leichte Abrundung der Zahnkanten | Kaum spürbar | Beobachten | visual_medium |
| Stadium 2 — Mittel | Deutliche Abrundung, Taschen flacher | Kette liegt weniger tief | Austausch planen | visual_medium |
| Stadium 3 — Stark | Zähne stark abgerundet, Taschen kaum erkennbar | Kette springt bei Last | SOFORT tauschen | visual_high |
| Stadium 4 — Kritisch | Zahnprofil nahezu plan | Kein sicherer Eingriff mehr | Außer Betrieb nehmen | visual_high |

#### 6.3.2 Quantitative Gypsy-Verschleißmessung

**Zahnhöhe messen:**
- Messschieber an Zahnspitze und Taschenboden anlegen
- Neuwert: herstellerabhängig (typisch 8–15 mm je nach Kettengröße)
- Grenzwert: 50 % des Neuwerts

**Taschentiefe messen:**
- Kaliber-Kettenglied einlegen
- Spalt zwischen Glied und Zahnflanke messen
- Neuwert: 0,5–1,0 mm
- Grenzwert: >2,0 mm → Gypsy tauschen

### 6.4 Seil/Leine-Chafe-Bewertung (Snubber, Ankerleine)

#### 6.4.1 Chafe-Indikatoren

| Befund | Stadium | Restfestigkeit (geschätzt) | Maßnahme | Confidence |
|--------|---------|---------------------------|----------|------------|
| Mantel intakt, kein Faserabrieb | Neu/OK | 100 % | Keine | visual_high |
| Leichter Faserflor auf Mantel | Leicht | 90–95 % | Scheuerschutz anbringen | visual_high |
| Mantel sichtbar abgescheuert (einzelne Fasern) | Mittel | 70–85 % | Scheuerschutz + Beobachten | visual_high |
| Mantel durchgescheuert, Kern sichtbar | Stark | 50–65 % | Austausch planen, nicht bei Starkwind verwenden | visual_high |
| Kern-Fasern beschädigt | Kritisch | <50 % | SOFORT tauschen | visual_high |
| Farbveränderung (UV-Bleichung) | UV-Schaden | 80–90 % | Mittelfristig tauschen | visual_medium |
| Verhärtung (steifes Tau) | Materialermüdung | 60–80 % | Austausch empfohlen | visual_medium |

#### 6.4.2 Snubber-Elastizitätsprüfung

**Einfacher Feldtest:**
1. Snubber frei aufhängen (1 m Abschnitt)
2. Definiertes Gewicht anhängen (z.B. 10 kg)
3. Dehnung messen

| Snubber-Material | Dehnung bei 10 % MBL | Neuwert | Tausch bei | Confidence |
|------------------|---------------------|---------|------------|------------|
| 3-schäftiges Nylon | 10–15 % | 12 % | <8 % | estimated |
| Doppelgeflecht Nylon | 8–12 % | 10 % | <6 % | estimated |
| Gummi-Snubber | 20–30 % | 25 % | <15 % | estimated |
| Dyneema (kein Snubber!) | <3 % | — | — | documented |

### 6.5 Verzinkungsverlust-Bewertung

#### 6.5.1 Visuelle Methode

| Erscheinungsbild | Geschätzte Restverzinkung | Maßnahme | Confidence |
|-----------------|--------------------------|----------|------------|
| Glänzend silber-grau, gleichmäßig | >80 % | OK, reguläre Prüfung | visual_high |
| Matt grau, keine Roststellen | 60–80 % | OK, reguläre Prüfung | visual_medium |
| Fleckig, einzelne braune Stellen | 40–60 % | Konservierung empfohlen | visual_medium |
| Überwiegend braun, vereinzelt Zinkinseln | 20–40 % | Tausch mittelfristig planen | visual_medium |
| Durchgehend rostbraun | <20 % | Austausch empfohlen | visual_high |
| Tiefrost, Materialabbau tastbar | 0 % + Materialabtrag | SOFORT tauschen | visual_high |

#### 6.5.2 Instrumentelle Methode (Surveyor-Level)

**Schichtdickenmessgerät (z.B. Elcometer 456):**
- Magnetisch-induktives Verfahren auf Stahl
- Messung an gerader Glied-Seite (nicht an Krümmung)
- 3 Messungen pro Glied, Mittelwert bilden
- Neuwert Feuerverzinkung: 80–120 µm
- Grenzwert: <30 µm → Austausch empfohlen

### 6.6 Windlass-Motorstrom als Verschleißindikator

Der Motorstrom unter definierter Last ist ein ausgezeichneter Indikator für den Gesamtzustand des Windlass-Systems:

**Messmethode:**
1. Zangenamperemeter (DC) an das Pluskabel zum Motor klemmen
2. Definierte Testbedingung: 20 m Kette einholen bei frei hängendem Anker (kein Grundkontakt)
3. Strom ablesen (Mittelwert über 30 Sekunden)

**Referenzwerte (12V-System):**

| Windlass-Leistung | Strom ohne Last | Strom Standard-Last | Warnung bei | Aktion bei | Confidence |
|-------------------|----------------|---------------------|-------------|------------|------------|
| 500 W | 15–25 A | 40–60 A | >80 A | >100 A | documented |
| 700 W | 20–35 A | 50–80 A | >100 A | >130 A | documented |
| 1000 W | 30–45 A | 70–110 A | >140 A | >170 A | documented |
| 1500 W | 40–60 A | 90–140 A | >180 A | >220 A | documented |

**Interpretation:**
- Strom zu hoch → Getriebe schwergängig, Kette klemmt, Motor verschlissen, Kabel zu dünn
- Strom zu niedrig → Motor hat wenig Kraft (Kohlen kurz, Wicklung teildefekt)
- Strom schwankt stark → Gypsy-Verschleiß (Kette springt), Getriebeschaden

**Langzeit-Trending:**
Wenn der Strom bei gleicher Testbedingung über die Jahre ansteigt, verschlechtert sich der Gesamtzustand:

| Jahr | Gemessener Strom | Interpretation | Confidence |
|------|-----------------|----------------|------------|
| 2020 (neu) | 75 A | Referenz | measured |
| 2021 | 80 A | Normal (+7 %) | measured |
| 2022 | 88 A | Leicht erhöht (+17 %) → Getriebefett prüfen | measured |
| 2023 | 95 A | Erhöht (+27 %) → Kohlen + Getriebe prüfen | measured |
| 2024 | 115 A | Deutlich erhöht (+53 %) → Revision empfohlen | measured |

### 6.7 Bugrolle-Befestigung — Strukturelle Prüfung

Die Bugrolle-Befestigung ist einer der am höchsten belasteten Decksbeschläge:

**Prüfpunkte:**

| Prüfung | Methode | OK-Kriterium | Aktion bei Versagen | Confidence |
|---------|---------|-------------|---------------------|------------|
| Schrauben/Bolzen fest | Drehmomentschlüssel | Herstellerangabe ±10 % | Nachziehen mit Loctite | measured |
| GFK unter Befestigung intakt | Klopftest (Münze/Hammer) | Gleichmäßig harter Klang | Bei hohlem Klang → Delamination prüfen (Endoskop) | visual_medium |
| Backing Plate vorhanden | Von unter Deck visuell | Muss vorhanden sein | Backing Plate nachrüsten | visual_high |
| Backing Plate korrekt dimensioniert | Messung | Min. 3× Schraubenkopf-Fläche | Größere Backing Plate einbauen | measured |
| Spiel in Befestigung | Händisch rütteln (Kette unter Last) | Kein fühlbares Spiel | Schrauben erneuern, ggf. GFK verstärken | measured |
| Dichtung intakt | Sichtprüfung + Wassertest | Kein Wasser unter Deck | Neu abdichten (Sikaflex 291i) | visual_high |
| Rissbildung am GFK | Sichtprüfung + Lupe | Keine Gelcoat-Risse | Bei Rissen: Strukturelle Bewertung durch Surveyor | visual_high |

**Backing-Plate-Empfehlungen:**

| Bootsklasse | Backing-Plate-Material | Mindestgröße (mm) | Mindestdicke (mm) | Confidence |
|------------|----------------------|-------------------:|-------------------:|------------|
| 8–10 m | Edelstahl 316L | 100 × 80 | 4 | estimated |
| 10–12 m | Edelstahl 316L | 120 × 100 | 5 | estimated |
| 12–14 m | Edelstahl 316L | 150 × 120 | 5 | estimated |
| 14–16 m | Edelstahl 316L | 180 × 140 | 6 | estimated |
| 16–20 m | Edelstahl 316L | 200 × 160 | 8 | estimated |

### 6.8 Elektrische Kontakte — Korrosionsbewertung

Elektrische Kontakte im Bugbereich sind besonders korrosionsgefährdet:

| Kontaktzustand | Visueller Befund | Übergangswiderstand | Auswirkung | Maßnahme | Confidence |
|---------------|-----------------|---------------------|-----------|----------|------------|
| Neuwertig | Metallisch blank, sauber | <0,1 mΩ | Keine | Kontaktfett auftragen | measured |
| Leicht oxidiert | Leichter Belag, kein Grünspan | 0,1–1 mΩ | Kaum messbar | Reinigen, Kontaktfett | measured |
| Mittel korrodiert | Grünspan/Weißbelag sichtbar | 1–10 mΩ | Spannungsabfall, Erwärmung | Kabelschuh erneuern | measured |
| Stark korrodiert | Dicke Kruste, Kabel fest korrodiert | >10 mΩ | Signifikanter Leistungsverlust | Kabel + Kabelschuhe erneuern | measured |
| Abgebrannt | Schwarze Verfärbung, Schmelzspuren | Hoch variabel | Sicherheitsgefahr (Brand) | Sofortige Erneuerung + Ursache klären | measured |

**Best-Practice für marine Elektrik im Ankerbereich:**
1. Alle Kabelschuhe crimpen UND verlöten (nur crimpen reicht in mariner Umgebung nicht langfristig)
2. Schrumpfschlauch mit Kleber (adhesive-lined heat shrink) auf alle Verbindungen
3. Kabelschuhe aus verzinntem Kupfer (tinned copper) verwenden
4. Kontaktfett (Vaseline, CRC Kontakt 61, oder Korrosionsschutzfett) auf alle Kontaktstellen
5. Kabel mit UV-beständigem Kabelkanal oder Wellschlauch schützen
6. Regelmäßig (jährlich) alle Verbindungen öffnen und prüfen
7. Keine Quetschverbinder ("Lüsterklemmen") im marinen Bereich — nur Kabelschuhe oder Stoßverbinder

### 6.9 Kettengewicht als Verschleißindikator

Eine weniger bekannte aber effektive Methode zur Kettenverschleißbewertung ist das Wiegen:

**Methode:**
1. 10 m Kette abmessen und wiegen (Waage bis 30 kg)
2. Mit Soll-Gewicht vergleichen

**Referenzgewichte (DIN 766):**

| Kettengröße | Neuwert (kg/m) | 10 m Soll (kg) | Warnung bei (kg) | Austausch bei (kg) | Confidence |
|-------------|---------------|----------------|------------------|-------------------|------------|
| 6 mm | 0,85 | 8,5 | <7,6 (−10 %) | <7,2 (−15 %) | documented |
| 8 mm | 1,40 | 14,0 | <12,6 (−10 %) | <11,9 (−15 %) | documented |
| 10 mm | 2,20 | 22,0 | <19,8 (−10 %) | <18,7 (−15 %) | documented |
| 12 mm | 3,10 | 31,0 | <27,9 (−10 %) | <26,4 (−15 %) | documented |
| 13 mm | 3,65 | 36,5 | <32,9 (−10 %) | <31,0 (−15 %) | documented |

**Vorteil der Wiegemethode:** Erfasst den Gesamtverschleiß über die Länge, nicht nur Einzelpunkte. Nachteil: Erkennt nicht einzelne schwache Glieder.

---

## 7. Anlagen-spezifische Zuordnung

### 7.1 Bootsgröße und Ankersystem-Wartungsaufwand

| Bootsklasse | LOA | Typisches System | Wartungsaufwand/Jahr | Kosten/Jahr (Material) | Confidence |
|-------------|-----|-----------------|---------------------|----------------------:|------------|
| Kleines Segelboot | 6–8 m | Handwinde, 6 mm Kette 30 m, Bruce/Delta 6 kg | 2–4 h | 50–150 € | estimated |
| Mittel Segelboot | 9–12 m | Elektr. Windlass 500 W, 8 mm Kette 50 m, Rocna 10 kg | 4–8 h | 100–300 € | estimated |
| Groß Segelboot | 12–16 m | Elektr. Windlass 1000 W, 10 mm Kette 70 m, Rocna 15–25 kg | 6–12 h | 200–500 € | estimated |
| Fahrtenyacht | 14–18 m | Elektr. Windlass 1500 W, 10–12 mm Kette 80–100 m, 2 Anker | 10–16 h | 300–800 € | estimated |
| Motoryacht | 10–15 m | Elektr. Windlass 1500 W, 10 mm Kette 50–70 m, Delta/Ultra | 6–10 h | 200–500 € | estimated |
| Große Motoryacht | 15–24 m | Hydraul. Windlass, 12–14 mm Kette 80–100 m, 2 Anker | 12–20 h | 500–1.500 € | estimated |
| Superyacht | 24+ m | Hydraul. Windlass, 14–16 mm+ Kette 100+ m, Ankerkasten | 20–40 h (Crew/Werft) | 1.500–5.000 € | estimated |

### 7.2 Windlass-Hersteller und spezifische Wartungshinweise

#### 7.2.1 Lewmar

| Modellreihe | Wartungsbesonderheit | Typisches Problem | Ersatzteil-Verfügbarkeit | Confidence |
|-------------|---------------------|-------------------|-------------------------|------------|
| V1/V2/V3 | Clutch-Konusfläche verschleißt | Durchrutschen bei Last | Gut (aktuell) | documented |
| H-Serie (horizontal) | Motor-Dichtung unteres Gehäuse | Wassereintritt in Motor | Gut | documented |
| Pro-Fish/Pro-Sport | Gypsy nicht austauschbar (integriert) | Gesamte Einheit tauschen | Gut | documented |
| CPX | Clutch-Ring verschleißt | Durchrutschen | Gut | documented |

**Lewmar Getriebefett:** Lewmar Gear Grease (Art.-Nr. 19701100) oder gleichwertiges Lithium-EP NLGI 2.

#### 7.2.2 Lofrans

| Modellreihe | Wartungsbesonderheit | Typisches Problem | Ersatzteil-Verfügbarkeit | Confidence |
|-------------|---------------------|-------------------|-------------------------|------------|
| Tigres | Öl-geschmiertes Getriebe | Ölverlust durch Dichtung | Gut (in Europa) | documented |
| Kobra | Kohlebürsten schwer zugänglich | Aufwändiger Kohlentausch | Gut | documented |
| Cayman | Motoranschlüsse korrodieren | Kontaktprobleme | Mittel | documented |
| X1/X2/X3 | Moderne Bauweise, leicht wartbar | Clutch-Justierung | Gut | documented |

**Lofrans Getriebefett:** Lofrans Service Grease oder Shell Gadus S2 V220 2.

#### 7.2.3 Quick

| Modellreihe | Wartungsbesonderheit | Typisches Problem | Ersatzteil-Verfügbarkeit | Confidence |
|-------------|---------------------|-------------------|-------------------------|------------|
| Genius | Kompakter Motor, schwer zugänglich | Motoraustausch statt Reparatur | Gut (in Europa) | documented |
| Prince | Aluminiumgehäuse korrodiert | Galvanische Korrosion bei Kontakt | Gut | documented |
| Hector | Robustes Getriebe | Selten Probleme | Gut | documented |
| CX | Integrierter Kettenzähler | Sensorausfall | Gut | documented |

#### 7.2.4 Maxwell

| Modellreihe | Wartungsbesonderheit | Typisches Problem | Ersatzteil-Verfügbarkeit | Confidence |
|-------------|---------------------|-------------------|-------------------------|------------|
| RC-Serie | Freilauf-Kupplung verschleißt | Kette fällt unkontrolliert | Mittel (Import aus NZ) | documented |
| HRC-Serie | Horizontaler Einbau, Wassereintritt | Motor-Korrosion | Mittel | documented |
| VWC-Serie | Leistungsstarke Motoren, hoher Stromverbrauch | Kabeldimensionierung beachten | Mittel | documented |

### 7.3 Segelboot vs. Motorboot — Unterschiede in der Wartung

| Aspekt | Segelboot | Motorboot | Confidence |
|--------|-----------|-----------|------------|
| Ankerhäufigkeit | Sehr häufig (Buchtenankern) | Seltener (häufiger Marina) | estimated |
| Kettenlänge | Länger (70–100 m, Scope 5:1–7:1) | Kürzer (40–60 m, Scope 4:1–5:1) | estimated |
| Hauptbelastung | Langzeit (über Nacht) | Kurz-/Mittelzeit (Badestopps) | estimated |
| Krängungs-Einfluss | Ja (Kettenfall asymmetrisch) | Kaum | documented |
| Bugrolle-Beanspruchung | Hoch (schwojt mehr) | Mittel | estimated |
| Kettenkasten-Größe | Größer (mehr Kette) | Kleiner | documented |
| Windlass-Belastung | Hoch (lange Kette, Wind) | Mittel | estimated |

---

## 8. Fehlerbild-Atlas

### 8.1 Fehlerbild F-01: Kette springt über den Gypsy

**Erscheinungsbild:** Beim Einholen springt die Kette über die Gypsy-Zähne, unkontrollierter Kettenfall möglich. Lautes Knacken/Schlagen beim Windlass-Betrieb.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Confidence |
|---------|-------------------|----------|------------|
| Gypsy-Verschleiß (Zähne abgerundet) | 35 % | Zahnhöhe messen, Spiel prüfen | measured |
| Falsche Kette für diesen Gypsy | 25 % | Kettengröße und -typ vs. Gypsy-Spezifikation vergleichen | measured |
| Kette verschlissen (Glieder zu dünn) | 20 % | Glied-Durchmesser messen | measured |
| Kettenteilung stimmt nicht (Mischkette) | 10 % | 10-Glieder-Teilung messen | measured |
| Verformte Kettenglieder | 5 % | Sichtprüfung auf ovale/verbogene Glieder | visual_high |
| Fremdkörper im Gypsy | 5 % | Gypsy reinigen, Taschen inspizieren | visual_high |

**Sofortmaßnahme:** Windlass stoppen, Kette manuell sichern, nicht unter Last ankern.

**Behebung:** Gypsy und Kette vermessen, ggf. Gypsy und/oder Kette tauschen.

### 8.2 Fehlerbild F-02: Windlass dreht, aber Kette bewegt sich nicht

**Erscheinungsbild:** Motor läuft hörbar, aber Kette wird weder eingezogen noch gefiert.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Confidence |
|---------|-------------------|----------|------------|
| Clutch nicht eingerastet | 40 % | Clutch-Hebel prüfen, fest anziehen | visual_high |
| Clutch verschlissen (durchrutschen) | 25 % | Clutch anziehen → trotzdem kein Eingriff | documented |
| Getriebe defekt (Zahnradbruch) | 15 % | Getriebe öffnen, Zähne prüfen | measured |
| Gypsy lose auf Welle (Keil fehlt) | 10 % | Gypsy von Hand drehen → dreht frei | measured |
| Motor-Getriebe-Kupplung defekt | 10 % | Motor dreht frei ohne Widerstand | measured |

**Sofortmaßnahme:** Kette manuell mit Winschkurbel oder Leine bergen.

### 8.3 Fehlerbild F-03: Windlass reagiert nicht (kein Motorlauf)

**Erscheinungsbild:** Fußschalter/Fernbedienung betätigt, kein Motorgeräusch.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Confidence |
|---------|-------------------|----------|------------|
| Hauptschalter nicht eingeschaltet | 25 % | Schalter am Panel prüfen | visual_high |
| Sicherung durchgebrannt | 20 % | Sicherung visuell/Multimeter prüfen | measured |
| Solenoid/Relais defekt | 20 % | Solenoid direkt mit 12V/24V brücken (Vorsicht!) | measured |
| Fußschalter/Fernbedienung defekt | 15 % | Direkt am Solenoid schalten | measured |
| Kabelbruch/Kontaktfehler | 10 % | Spannungsmessung an Motor, Solenoid, Schalter | measured |
| Motor defekt (Kohlen, Wicklung) | 10 % | Motor direkt an Batterie → dreht nicht | measured |

### 8.4 Fehlerbild F-04: Windlass dreht nur in eine Richtung

**Erscheinungsbild:** Windlass zieht ein (oder fiert), aber die Gegenrichtung funktioniert nicht.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Confidence |
|---------|-------------------|----------|------------|
| Solenoid für eine Richtung defekt | 35 % | Beide Solenoids einzeln testen | measured |
| Fußschalter für eine Richtung defekt | 25 % | Schalter durchmessen | measured |
| Kabelbruch auf einer Leitung | 20 % | Durchgangsprüfung | measured |
| Motor-Kohle einseitig verschlissen | 15 % | Kohlen prüfen | measured |
| Steuerplatine defekt (bei elektronischer Steuerung) | 5 % | Platine visuell auf Brandstellen prüfen | visual_medium |

### 8.5 Fehlerbild F-05: Windlass dreht extrem langsam

**Erscheinungsbild:** Kette wird eingezogen, aber sehr langsam. Motor klingt gequält.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Confidence |
|---------|-------------------|----------|------------|
| Batteriespannung zu niedrig | 30 % | Spannung unter Last messen (am Motor) | measured |
| Kabelquerschnitt zu gering/Kabellänge zu groß | 20 % | Spannungsabfall messen (Batterie vs. Motor) | measured |
| Schlechte Kabelverbindungen (Korrosion) | 20 % | Übergangswiderstände messen, Klemmen prüfen | measured |
| Motor verschlissen (Kohlen kurz) | 15 % | Kohlen messen, Stromaufnahme prüfen | measured |
| Getriebe schwergängig (Fettmangel) | 10 % | Motor ohne Kette laufen lassen → schnell? | measured |
| Mechanische Blockade (Kette klemmt) | 5 % | Kette prüfen, Bugrolle, Kettenkasten | visual_high |

### 8.6 Fehlerbild F-06: Kettenstopper hält nicht

**Erscheinungsbild:** Kette rutscht durch den Kettenstopper, Last liegt auf Windlass.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Confidence |
|---------|-------------------|----------|------------|
| Stopper nicht richtig eingerastet | 30 % | Hebel/Klaue Position prüfen | visual_high |
| Klauen/Haken verschlissen | 25 % | Klauen visuell auf Abflachung prüfen | visual_medium |
| Falsche Kettengröße für Stopper | 15 % | Ketten-Nennmaß vs. Stopper-Spezifikation | measured |
| Stopper-Feder gebrochen | 15 % | Feder sichtbar, Funktion prüfen | visual_high |
| Stopper-Befestigung lose | 10 % | Schrauben/Bolzen prüfen | measured |
| Kette verschlissen (zu dünn für Stopper) | 5 % | Glied-Durchmesser messen | measured |

### 8.7 Fehlerbild F-07: Starke Vibrationen beim Windlass-Betrieb

**Erscheinungsbild:** Windlass vibriert stark, Geräusche, Resonanz im Vorschiff.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Confidence |
|---------|-------------------|----------|------------|
| Befestigungsschrauben lose | 30 % | Alle Befestigungspunkte prüfen/nachziehen | measured |
| Gypsy-Verschleiß (unrunder Lauf) | 25 % | Gypsy-Zähne prüfen, Kette einlegen | visual_medium |
| Motor-Lager verschlissen | 15 % | Motor einzeln laufen lassen, Geräusch | measured |
| Getriebe-Lagerschaden | 15 % | Getriebe-Geräusch bei Leerlauf | measured |
| GFK-Deck unter Windlass weich | 10 % | Klopftest, Unterdeck-Inspektion | visual_medium |
| Resonanzproblem (strukturell) | 5 % | Nur bei bestimmter Drehzahl | estimated |

### 8.8 Fehlerbild F-08: Bugrolle blockiert

**Erscheinungsbild:** Rolle dreht sich nicht mehr, Kette schleift über stehende Rolle.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Confidence |
|---------|-------------------|----------|------------|
| Korrosion/Festfressen des Bolzens | 35 % | Bolzen auf Korrosion prüfen | visual_high |
| Muschelbewuchs in Lager | 25 % | Rolle reinigen, Lager freilegen | visual_high |
| Lager/Buchse verschlissen | 20 % | Rolle ausbauen, Buchse inspizieren | measured |
| Salzverkrustung | 10 % | Süßwasser spülen, Kriechöl | visual_high |
| Bolzen verbogen | 5 % | Bolzen ausbauen, auf Geradeheit prüfen | measured |
| Sicherungssplint eingeklemmt | 5 % | Splint-Position prüfen | visual_high |

### 8.9 Fehlerbild F-09: Kette staut sich im Kettenkasten

**Erscheinungsbild:** Kette pyramidet im Kettenkasten, fällt nicht nach unten, Windlass blockiert.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Confidence |
|---------|-------------------|----------|------------|
| Kettenkasten zu klein für Kettenlänge | 25 % | Volumen berechnen vs. Kettenmenge | measured |
| Kettenkasten-Öffnung zu klein | 25 % | Öffnungsmaße vs. Kettenfall-Winkel | measured |
| Kette fällt nicht frei (Hindernis) | 20 % | Kettenkasten von innen inspizieren | visual_high |
| Kette verdreht/verknotet | 15 % | Kette komplett auslegen, Knoten lösen | visual_high |
| Bewuchs/Verschmutzung im Kettenkasten | 10 % | Reinigung erforderlich | visual_high |
| Kettenführungsrohr zu eng | 5 % | Rohr-Durchmesser vs. Kette prüfen | measured |

### 8.10 Fehlerbild F-10: Anker sitzt fest am Grund (Klarfall)

**Erscheinungsbild:** Anker lässt sich trotz voller Windlass-Kraft nicht lösen.

**Mögliche Ursachen und Verfahren:**

| Verfahren | Beschreibung | Erfolgschance | Confidence |
|-----------|-------------|---------------|------------|
| Überfahren | Über den Anker hinausfahren, Kette senkrecht stellen | 60 % | documented |
| Gegenzug | Kette auf Klampe belegen, Boot rückwärts fahren, Schwellhilfe | 40 % | documented |
| Reitgewicht | Gewicht an Kette herablassen, Zugwinkel ändern | 30 % | estimated |
| Tripleine | Falls vorhanden: von Gegenseite ziehen | 80 % | documented |
| Taucher | Professionell, wenn nichts anderes hilft | 95 % | documented |
| Aufgabe | Kette am Marker-Boje befestigen, später bergen | — | documented |

**WARNUNG:** Windlass NIEMALS als Zugwerkzeug zum Ankerlösen verwenden! Maximale Zugkraft liegt weit unter der Grundhaltekraft eines festsitzenden Ankers. Folge: Getriebeschaden, Motorschaden, Gypsy-Bruch.

### 8.11 Fehlerbild F-11: Elektrische Korrosion an Windlass-Anschlüssen

**Erscheinungsbild:** Grüne/weiße Krusten an Kabelschuhen, intermittierender Betrieb, Windlass funktioniert manchmal.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Confidence |
|---------|-------------------|----------|------------|
| Salzwasser-Eindringen in Kabelverbindungen | 35 % | Verbindungen öffnen, Korrosion sichtbar | visual_high |
| Fehlende Abdichtung der Decksdurchführung | 25 % | Dichtung prüfen, Wassertest | visual_high |
| Galvanische Korrosion (verschiedene Metalle) | 20 % | Kupfer + Alu = grüne Krusten | visual_high |
| Kabelschuhe nicht gecrimpt/verlötet | 10 % | Verbindungstyp prüfen | visual_high |
| Schrumpfschlauch fehlt | 10 % | Isolation prüfen | visual_high |

**Behebung:**
1. Korrosion mechanisch entfernen (Drahtbürste, Schleifpapier)
2. Kabelschuhe erneuern (crimpen + verlöten)
3. Schrumpfschlauch mit Kleber aufziehen
4. Kontaktfett auftragen (z.B. Vaseline oder Korrosionsschutzfett)
5. Decksdurchführung abdichten (Sikaflex 291i oder gleichwertig)

### 8.12 Fehlerbild F-12: Snubber-Versagen bei Nacht

**Erscheinungsbild:** Nachts löst sich der Snubber oder reißt. Last fällt schlagartig auf Windlass. Lauter Knall weckt die Crew.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose | Confidence |
|---------|-------------------|----------|------------|
| Durchgescheuerter Snubber (Chafe) | 35 % | Scheuerstelle prüfen, besonders an Bugrolle/Klüse | visual_high |
| Karabiner/Haken geöffnet/gebrochen | 20 % | Hakensicherung prüfen | visual_high |
| UV-geschädigtes Tauwerk | 15 % | Verhärtung, Verfärbung, Brüchigkeit | visual_medium |
| Kettenhaken-Verbindung gelöst | 15 % | Haken-Kette-Verbindung prüfen | visual_high |
| Überlastung (Wind stärker als Snubber-MBL) | 10 % | Snubber-MBL vs. erwartete Böenlast vergleichen | calculated |
| Falsches Material (Polyester statt Nylon) | 5 % | Material identifizieren (Nylon = elastisch) | documented |

**Prävention:**
- Scheuerschutz an allen Kontaktstellen
- Snubber regelmäßig auf Chafe prüfen (besonders nachts vor dem Schlafengehen)
- Backup-Snubber bereithalten
- Kettenstopper als primäre Sicherung, Snubber als Komfortmaßnahme

---

## 9. Troubleshooting

### 9.1 Entscheidungsbaum T-01: Windlass funktioniert nicht

```
Windlass reagiert nicht
├── Hauptschalter EIN?
│   ├── NEIN → Einschalten → Problem gelöst?
│   │   ├── JA → Bedienfehler
│   │   └── NEIN → Weiter unten
│   └── JA → Sicherung prüfen
│       ├── Durchgebrannt → Neue Sicherung (GLEICHER Wert!)
│       │   ├── Hält → Problem gelöst (einmaliger Fehler)
│       │   └── Brennt wieder durch → Kurzschluss suchen
│       │       ├── Kabel prüfen (Isolation, Knicke, Scheuerstellen)
│       │       ├── Motor prüfen (Wicklungsschluss)
│       │       └── Solenoid prüfen (interner Kurzschluss)
│       └── Sicherung OK → Spannung am Solenoid messen
│           ├── Keine Spannung → Kabelbruch/Kontaktfehler zwischen Schalter und Solenoid
│           │   ├── Fußschalter prüfen (Durchgang)
│           │   ├── Kabelverbindungen prüfen
│           │   └── Fernbedienungs-Kabel prüfen
│           └── Spannung vorhanden → Solenoid schaltet?
│               ├── NEIN → Solenoid defekt → tauschen
│               └── JA → Spannung am Motor messen
│                   ├── Keine Spannung → Kabel Solenoid→Motor defekt
│                   └── Spannung vorhanden → Motor defekt
│                       ├── Kohlen prüfen
│                       ├── Kollektor prüfen
│                       └── Wicklung prüfen (Werkstatt)
```

### 9.2 Entscheidungsbaum T-02: Kette springt/klemmt im Gypsy

```
Kette springt oder klemmt
├── Klemmen oder Springen?
│   ├── SPRINGEN:
│   │   ├── Gypsy-Zähne prüfen
│   │   │   ├── Abgerundet → Gypsy tauschen
│   │   │   └── OK → Kette prüfen
│   │   │       ├── Durchmesser zu gering → Kette tauschen
│   │   │       ├── Glieder verformt → Einzelne Glieder oder Abschnitt tauschen
│   │   │       └── Teilung falsch → Falsche Kette → richtige Kette kaufen
│   │   └── Fremdkörper im Gypsy? → Reinigen
│   └── KLEMMEN:
│       ├── Kette zu dick für Gypsy? → Ketten/Gypsy-Kompatibilität prüfen
│       ├── Muscheln/Bewuchs auf Kette → Reinigen
│       ├── Verdrehte Kettenglieder → Kette auslegen, entwirren
│       ├── Rostknollen auf Kette → Entrosten oder tauschen
│       └── Gypsy-Taschen korrodiert/zugesetzt → Gypsy reinigen/tauschen
```

### 9.3 Entscheidungsbaum T-03: Übermäßiger Kettenverschleiß

```
Kette verschleißt zu schnell
├── Wo ist der Verschleiß am stärksten?
│   ├── Gleichmäßig über gesamte Kette:
│   │   ├── Schlechte Kettenqualität → Auf höhere Güte upgraden
│   │   ├── Aggressives Revier (Fels, Koralle) → Akzeptieren, kürzer messen
│   │   └── Salzwasser + keine Konservierung → Spülen + konservieren
│   ├── Erste 20 m deutlich stärker:
│   │   ├── Normal (häufigster Nutzungsbereich) → Kette umdrehen oder Abschnitt tauschen
│   │   └── Gypsy-Verschleiß verstärkt Kettenabrieb → Gypsy prüfen
│   ├── An der Gypsy-Kontaktstelle:
│   │   ├── Gypsy-Material härter als Kette → Normal, Kette ist Verschleißteil
│   │   └── Gypsy-Zähne scharfkantig (Grat) → Gypsy-Kanten entgraten
│   └── An Bugrolle/Klüse:
│       ├── Scharfe Kanten an Bugrolle → Kanten abrunden (Feile)
│       ├── Bugrolle dreht nicht → Rolle warten/tauschen
│       └── Seitliches Scheuern (Schwoj) → Kettenführung verbessern
```

### 9.4 Entscheidungsbaum T-04: Anker hält nicht

```
Anker hält nicht (schleppt/draggt)
├── Scope ausreichend? (min. 5:1 Kette, 7:1 Leine)
│   ├── NEIN → Mehr Kette/Leine fieren
│   └── JA → Ankergrund geeignet?
│       ├── Fels/Gras/Algen → Revierinformation prüfen, ggf. Ankerplatz wechseln
│       └── Sand/Schlick/Ton → Anker richtig gesetzt?
│           ├── NEIN → Aufnehmen, neu setzen, rückwärts eingraben
│           └── JA → Anker-Zustand prüfen
│               ├── Fluken verbogen → Anker tauschen
│               ├── Gelenk/Wippe blockiert → Reinigen/Schmieren
│               ├── Anker zu leicht → Größeren Anker oder Reitgewicht
│               └── Ankertyp ungeeignet → Anderen Typ versuchen
```

### 9.5 Entscheidungsbaum T-05: Wassereintritt durch Ankersystem

```
Wasser im Vorschiff / Ankerkasten-Bereich
├── Woher kommt das Wasser?
│   ├── Kettenkastendrainage rückwärts (bei Fahrt):
│   │   ├── Rückschlagventil defekt → Ventil tauschen
│   │   └── Kein Ventil vorhanden → Nachrüsten
│   ├── Bugrolle-Befestigung undicht:
│   │   ├── Dichtmasse alt/gerissen → Neu abdichten (Sikaflex 291i)
│   │   └── Schraubenlöcher ausgebrochen → GFK reparieren, neu bohren
│   ├── Kettenkasten-Deckel undicht:
│   │   ├── Dichtung defekt → Dichtung erneuern
│   │   └── Deckel verzogen → Deckel plan schleifen oder tauschen
│   ├── Windlass-Decksdurchführung undicht:
│   │   ├── Dichtring defekt → Dichtring tauschen
│   │   └── GFK-Verstärkung gerissen → GFK-Reparatur
│   └── Spritzwasser durch Ankerklüse:
│       ├── Klüsendeckel fehlt → Nachrüsten
│       └── Klüse zu groß für Kette → Reduziereinsatz oder Neopren-Manschette
```

---

## 10. FAQ — Häufige Fragen

### FAQ-01: Wie oft muss ich meine Ankerkette wirklich messen?

**Antwort:** Mindestens einmal jährlich eine Stichprobenmessung (alle 5 m ein Glied) und alle 2–3 Jahre eine Vollmessung (alle 1 m ein Glied). Bei intensiver Nutzung (>100 Ankernächte/Jahr) halbjährliche Stichprobe. Die Messung dauert 30–60 Minuten und ist die wichtigste Wartungsmaßnahme am Ankersystem.
**Confidence:** documented

### FAQ-02: Wann muss die Ankerkette getauscht werden?

**Antwort:** Bei >12 % Durchmesserreduktion gegenüber dem Neuwert (ISO-Empfehlung). Konservativere Surveyor empfehlen Austausch ab 10 %. Bei einer 10-mm-Kette bedeutet das: Tausch bei <8,8 mm (12 %) oder <9,0 mm (10 %). Außerdem bei sichtbarer Verformung einzelner Glieder, starkem Tiefenrost oder wenn die Kette nicht mehr korrekt in den Gypsy passt.
**Confidence:** documented

### FAQ-03: Kann ich meine Ankerkette nachverzinken lassen?

**Antwort:** Ja, Feuerverzinkung ist möglich (Kosten ca. 3–8 €/m für 10-mm-Kette). Voraussetzung: mechanische Integrität der Glieder muss gewährleistet sein (Durchmesser im Toleranzbereich). Galvanische Nachverzinkung ist deutlich dünner (15–25 µm vs. 80–120 µm) und daher nicht empfohlen. Die Kosten für Nachverzinkung übersteigen ab ca. 60 % des Neuwerts der Kette den wirtschaftlichen Nutzen.
**Confidence:** documented

### FAQ-04: Welches Getriebefett soll ich für meine Ankerwinde verwenden?

**Antwort:** Immer das vom Hersteller empfohlene Fett verwenden. Wenn nicht verfügbar: ein Lithium-EP-Fett (NLGI Klasse 2) mit Hochdruck-Additiven. Niemals verschiedene Fetttypen mischen. Vor dem Befüllen altes Fett restlos entfernen. Typische Menge: 80–200 g je nach Windlass-Modell.
**Confidence:** documented

### FAQ-05: Wie erkenne ich, ob mein Gypsy verschlissen ist?

**Antwort:** Drei Anzeichen: (1) Kette springt beim Einholen über die Zähne. (2) Neues Kettenglied einlegen und Spiel messen — bei >2 mm Spiel ist der Gypsy fällig. (3) Visuell: Zähne sind abgerundet statt scharfkantig. Ein verschlissener Gypsy beschleunigt auch den Kettenverschleiß dramatisch.
**Confidence:** documented

### FAQ-06: Mein Windlass dreht langsam — muss er getauscht werden?

**Antwort:** Meist nicht. In 70 % der Fälle liegt es am Spannungsabfall: Messen Sie die Spannung direkt am Motor unter Last. Liegt sie mehr als 10 % unter der Batteriespannung, sind die Kabel zu dünn, zu lang oder die Verbindungen korrodiert. Erst danach Kohlen und Getriebe prüfen.
**Confidence:** documented

### FAQ-07: Wie lagere ich mein Ankersystem im Winter richtig ein?

**Antwort:** (1) Kette komplett auslegen, mit Süßwasser spülen, trocknen, mit Konservierungsspray behandeln. (2) Kettenkasten reinigen, desinfizieren, offen lassen für Belüftung. (3) Windlass-Getriebe nachfetten. (4) Windlass-Motor kurz laufen lassen, dann Batterie abklemmen. (5) Snubber waschen, trocknen, UV-geschützt lagern. (6) Bugrolle reinigen und schmieren.
**Confidence:** documented

### FAQ-08: Was ist der Unterschied zwischen Snubber und Reitgewicht?

**Antwort:** Beide dienen der Lastdämpfung, aber auf unterschiedliche Weise. Der **Snubber** (elastisches Tauwerk) absorbiert Stoßbelastungen durch Dehnung und entlastet die Ankerwinde. Das **Reitgewicht** (Kellet) ist ein Gewicht, das an der Kette herabgelassen wird und den Zugwinkel am Anker flacher macht (mehr Haltekraft) und gleichzeitig als Federung wirkt. Idealerweise beides verwenden.
**Confidence:** documented

### FAQ-09: Darf ich den Windlass zum Ankerlichten unter voller Last verwenden?

**Antwort:** Nein! Der Windlass ist zum kontrollierten Einholen der Kette gedacht, nicht als Zugwerkzeug. Bei festsitzendem Anker: Boot über den Anker fahren (Kette auf Klampe belegen, Motorkraft nutzen), bis die Kette senkrecht steht, dann Windlass zum Einholen. Maximale Zugkraft am Windlass ist deutlich geringer als die Haltekraft eines gut gesetzten Ankers.
**Confidence:** documented

### FAQ-10: Wie lang soll mein Snubber sein?

**Antwort:** Mindestens 8–10 m für wirksame Stoßdämpfung. Faustregel: Snubber-Länge = 1,5 × Freibordhöhe + 5 m. Bei starkem Schwell oder Sturmankern: bis zu 15–20 m. Der Snubber soll so lang sein, dass die Kette deutlich durchhängt (mind. 1 m) — nur dann wirkt die Elastizität.
**Confidence:** estimated

### FAQ-11: Meine Kette riecht furchtbar — was tun?

**Antwort:** Der Gestank entsteht durch anaerobe Zersetzung von organischem Material (Schlamm, Algen, Muscheln) im Kettenkasten. Lösung: (1) Kette komplett auslegen. (2) Kettenkasten gründlich reinigen (Hochdruck + Bürste). (3) Desinfizieren mit Essigessenz (1:5) oder Spezialreiniger. (4) 24 h trocknen lassen. (5) Drainage prüfen — stehendes Wasser ist die Hauptursache. (6) Kette mit Süßwasser spülen und trocknen, bevor sie zurückgelegt wird.
**Confidence:** documented

### FAQ-12: Kann ich eine gebrauchte Ankerkette kaufen?

**Antwort:** Nur mit Vorsicht. Gebrauchte Ketten haben unbekannte Vorgeschichte (Belastung, Verschleiß, verdeckte Risse). Wenn gebraucht: (1) Jeden 5. Meter ein Glied messen (Durchmesser >90 % Neuwert). (2) Kalibrierung prüfen (Teilung). (3) Verzinkung bewerten. (4) Auf Verformungen prüfen. (5) Preis-Vergleich: gebrauchte Kette >60 % des Neupreises = lieber neu kaufen.
**Confidence:** estimated

### FAQ-13: Welche Kettengröße passt zu meinem Gypsy?

**Antwort:** EXAKT die vom Windlass-Hersteller spezifizierte Größe und Norm (DIN 766, ISO 4565, BBB, HT). NICHT einfach nach Durchmesser kaufen — Teilung und Profilform müssen stimmen. Ein 10-mm-DIN-766-Kettenglied hat andere Maße als ein 10-mm-BBB. Falsche Kette = Kette springt, Gypsy-Verschleiß, Sicherheitsrisiko.
**Confidence:** documented

### FAQ-14: Wie oft soll ich die Kohlebürsten meiner Windlass prüfen?

**Antwort:** Alle 100–150 Betriebsstunden oder alle 2 Jahre (was zuerst kommt). Bei Gelegenheitsseglern reicht alle 3–4 Jahre. Anzeichen für kurze Kohlen: Windlass wird langsamer, Motorgeräusch ändert sich (mehr Funkenbildung am Kollektor). Kohlen unter 6 mm Restlänge sofort tauschen.
**Confidence:** documented

### FAQ-15: Brauche ich einen Kettenstopper zusätzlich zur Windlass?

**Antwort:** JA, unbedingt. Die Windlass ist KEIN Halteorgan, sondern ein Hebezeug. Bei Ankerlast auf der Windlass verschleißen Getriebe und Clutch rapide. Der Kettenstopper (plus Snubber) übernimmt die Ankerlast. Ausnahme: manche Windlass-Modelle haben einen integrierten Kettenstopper — prüfen, ob dieser für die erwartete Dauerlast spezifiziert ist.
**Confidence:** documented

### FAQ-16: Was mache ich, wenn der Windlass-Motor nass geworden ist?

**Antwort:** (1) Sofort Strom trennen (Hauptschalter + Sicherung). (2) Motor ausbauen. (3) Mit Süßwasser spülen (Salz entfernen). (4) Druckluft zum Trocknen (vorsichtig). (5) Mindestens 48 h an der Luft trocknen lassen. (6) Isolationswiderstand messen (>1 MΩ). (7) Kohlebürsten und Kollektor prüfen. (8) Wenn Isolationswiderstand zu niedrig: Motor in Backofen bei 60°C für 4–6 h trocknen (nur wenn Motor keine Kunststoffteile hat, die schmelzen könnten).
**Confidence:** documented

### FAQ-17: Ist es sinnvoll, die Ankerkette umzudrehen?

**Antwort:** Ja, sehr sinnvoll! Die ersten 20–30 m der Kette verschleißen am stärksten (90 % der Nutzung). Durch Umdrehen nutzt man das hintere, fast neue Ende und verdoppelt effektiv die Kettenlebensdauer. Voraussetzung: das hintere Ende muss mit einem lösbaren Schäkel am Kettenkasten befestigt sein (Panikschäkel). Beim Umdrehen die Endbefestigung im Kettenkasten auf die neuen Anfangsmeter verlegen.
**Confidence:** documented

### FAQ-18: Wie pflege ich einen Edelstahl-Anker?

**Antwort:** Edelstahl (316L) braucht weniger Pflege als verzinkter Stahl, aber nicht null: (1) Nach jedem Gebrauch mit Süßwasser spülen. (2) Halbjährlich mit Edelstahlreiniger behandeln (z.B. Star Brite Stainless Steel Cleaner). (3) Lochfraß (braune Punkte) sofort behandeln: Beizpaste auftragen, 30 min einwirken, abspülen, Passivierung erneuern. (4) KEINE Stahlbürste verwenden — nur Edelstahl- oder Kunststoffbürste. (5) Kontaktkorrosion vermeiden: Kein Kontakt mit normalem Stahl.
**Confidence:** documented

### FAQ-19: Was kostet eine professionelle Windlass-Revision?

**Antwort:** Je nach Hersteller und Modell: 400–1.200 € (Arbeitszeit) + 100–600 € (Ersatzteile). Typische Ersatzteile: Kohlebürsten (30–80 €), Dichtungssatz (50–150 €), Gypsy (200–600 €), Getriebe-Reparaturkit (150–400 €). Bei sehr alten Modellen (>15 Jahre) kann der Austausch wirtschaftlicher sein als die Revision.
**Confidence:** estimated

### FAQ-20: Kann Salzwasser die Windlass-Elektrik beschädigen?

**Antwort:** Ja, Salzwasser ist der Hauptfeind der Windlass-Elektrik. Besonders gefährdet: (1) Solenoid-Anschlüsse (unter Deck, aber Spritzwasser-exponiert). (2) Fußschalter (ständig Spritzwasser). (3) Motor-Kabelschuhe (im Bugbereich). Prävention: alle Verbindungen mit Schrumpfschlauch + Kontaktfett schützen, Fußschalter regelmäßig mit Süßwasser spülen, Decksdurchführungen abdichten.
**Confidence:** documented

### FAQ-21: Wie teste ich, ob mein Kettenstopper korrekt hält?

**Antwort:** (1) Anker setzen mit normalem Scope. (2) Kette in Kettenstopper einlegen. (3) Clutch der Windlass öffnen (Freilauf). (4) Snubber befestigen. (5) Boot rückwärts fahren (sanft), um Last aufzubauen. (6) Kettenstopper beobachten: Kette darf NICHT rutschen. (7) Bei 15–20 kn scheinbarem Wind 10 Minuten halten. Wenn Kette rutscht: Stopper einstellen oder tauschen.
**Confidence:** documented

### FAQ-22: Welche Ankerleine brauche ich als Backup?

**Antwort:** Als Not-Backup: mindestens 30 m Nylon-Ankerleine (3-schäftig oder Doppelgeflecht). Durchmesser: LOA in Metern × 1,5 mm (Faustregel). Beispiel: 12-m-Yacht → 18 mm Nylon. Immer mit mindestens 5 m Kette als Vorlauf (Abriebschutz am Grund) und Schäkel. Die Leine muss zugänglich gelagert sein — nicht zuunterst im Kettenkasten.
**Confidence:** estimated

### FAQ-23: Was bedeuten die verschiedenen Kettenklassen (G30, G40, G43, G70)?

**Antwort:** Die Zahl gibt die Mindestbruchfestigkeit in N/mm² × 10 an: G30 = 300 N/mm² (Gebrauchskette), G40 = 400 N/mm² (Standardkette), G43 = 430 N/mm² (US-Standard BBB), G70 = 700 N/mm² (Hochfeste Kette). Für Yachten ist G40 (DIN 766/ISO 4565) der Standard. G70 (HT) ermöglicht dünnere Kette bei gleicher Festigkeit, erfordert aber passenden HT-Gypsy. G30 ist zu schwach für Ankerketten.
**Confidence:** documented

### FAQ-24: Wie bewahre ich meinen Snubber auf, damit er lange hält?

**Antwort:** (1) Nach Gebrauch mit Süßwasser spülen (Salzkristalle zerstören die Fasern). (2) Vollständig trocknen lassen (Schimmel). (3) UV-geschützt lagern (UV ist der größte Feind von Nylon). (4) Nicht auf scharfen Kanten aufrollen. (5) Nicht in der Sonne auf Deck liegen lassen, wenn nicht in Gebrauch. (6) Lose aufwickeln, nicht stramm (Faserermüdung).
**Confidence:** documented

### FAQ-25: Ab welcher Windstärke brauche ich einen Snubber?

**Antwort:** IMMER. Auch bei leichtem Wind schützt der Snubber die Windlass vor Stoßbelastungen (Wellen, Schwell, Windböen). Ab 15 kn ist ein Snubber Pflicht. Ab 25 kn sollte ein zweiter Snubber oder ein Bridle (V-förmiger Doppelsnubber) verwendet werden. Der Snubber ist keine Sturmausrüstung, sondern Standardausrüstung.
**Confidence:** documented

### FAQ-26: Wie erkenne ich, ob mein Windlass-Kabel zu dünn ist?

**Antwort:** Messen Sie die Spannung direkt an der Batterie und gleichzeitig am Motor (unter Last, also beim Einholen der Kette). Die Differenz ist der Spannungsabfall. Bei 12-V-Systemen soll der Spannungsabfall unter 1,2 V (10 %) liegen. Typische Symptome eines zu dünnen Kabels: Windlass dreht langsam, Kabel wird warm, Sicherung löst bei kaltem Wetter aus (Batterie schwächer → Motor zieht mehr Strom).
**Confidence:** measured

### FAQ-27: Wie oft soll ich den Anker mit Süßwasser spülen?

**Antwort:** Nach JEDEM Gebrauch im Salzwasser — auch die Kette. Mindestens die ersten 20 m Kette und den Anker gründlich abspritzen. Salzkristalle greifen die Verzinkung an und beschleunigen Korrosion. Besonders wichtig: vor längerer Liegepause (>1 Woche) gründlich spülen.
**Confidence:** documented

### FAQ-28: Was ist der Unterschied zwischen DIN 766 und BBB Kette?

**Antwort:** DIN 766 (europäischer Standard) und BBB (US-Standard "Triple B") haben bei gleichem Nenndurchmesser unterschiedliche Teilungen (Gliedabstände). Eine 10-mm-DIN-766-Kette hat eine Teilung von 28 mm, während BBB bei 3/8" (9,5 mm) eine Teilung von 35 mm hat. Sie sind NICHT austauschbar im gleichen Gypsy! Beim Kettenkauf IMMER den Gypsy-Hersteller konsultieren.
**Confidence:** documented

### FAQ-29: Kann ich meinen Windlass selbst reparieren?

**Antwort:** Ja, viele Wartungsarbeiten sind für handwerklich begabte Eigner machbar: Kohlebürsten tauschen, Getriebefett wechseln, Gypsy tauschen, Dichtungen erneuern. Voraussetzung: (1) Herstellerhandbuch vorhanden (oft als PDF herunterladbar). (2) Grundlegendes Werkzeug (Messschieber, Multimeter, Innensechskant, Drehmomentschlüssel). (3) Sicherheitsregeln beachten (Strom trennen!). Bei Wicklungsschäden am Motor oder Getriebelagerschäden: Werkstatt empfohlen.
**Confidence:** documented

### FAQ-30: Wie bewerte ich ein Ankersystem beim Gebrauchtkauf?

**Antwort:** Systematische Prüfung in 30 Minuten: (1) Kette: 3 Stichprobenmessungen (bei 5, 15, 30 m) → Durchmesser in % vom Neuwert. (2) Gypsy: Kettenglied einlegen, Spiel schätzen. (3) Windlass: Funktionstest Auf/Ab, Geräusche, Geschwindigkeit. (4) Bugrolle: Rolle dreht? Bolzen fest? (5) Kettenstopper: hält er? (6) Elektrik: Spannung unter Last messen. (7) Kettenkasten: Geruch, Drainage. Gesamtzeit: 30–45 min, aber diese Prüfung kann 1.000–5.000 € Verhandlungsmasse ergeben.
**Confidence:** documented

### FAQ-31: Wie lange kann ich eine Kette mit 10 % Durchmesserreduktion noch nutzen?

**Antwort:** Bei 10 % Reduktion befindet sich die Kette im Warnbereich (Grenzwert ist 12 %). Bei einer typischen Verschleißrate von 1–1,5 % pro Jahr (Vielsegler Mittelmeer) verbleiben noch 1–2 Saisons. Empfehlung: Kette nicht mehr für Sturmankern oder Blauwasser verwenden, Tausch bis zur nächsten Saison planen. Für Tagesankern bei leichtem Wetter noch vertretbar.
**Confidence:** calculated

### FAQ-32: Was bedeutet "Kalibrierte Kette"?

**Antwort:** Eine kalibrierte Kette hat präzise definierte Gliedmaße (Teilung, Innenweite, Außenweite), die innerhalb enger Toleranzen liegen (±2,5 % nach ISO 4565). Nur kalibrierte Kette läuft korrekt über den Gypsy. Unkalibrierte Kette (z.B. Baumarkt-Kette oder Hebekette) hat größere Toleranzen und kann im Gypsy springen oder klemmen. Für Ankerwinden IMMER kalibrierte Kette verwenden.
**Confidence:** documented

---

## 11. Glossar

### Alphabetische Begriffsliste (Deutsch → Englisch)

| Nr. | Deutsch | Englisch | Definition | Confidence |
|-----|---------|----------|------------|------------|
| G-01 | Ankerbugbeschlag | Anchor bow fitting | Gesamtheit der Beschläge am Bug zur Ankeraufnahme (Bugrolle, Klüse, Stopper) | documented |
| G-02 | Ankerfuß | Anchor foot / Fluke tip | Untere Kante der Ankerfluke, gräbt sich in den Grund | documented |
| G-03 | Ankergeschirr | Ground tackle | Gesamtheit aller Komponenten zum Ankern (Anker, Kette, Leine, Verbinder, Windlass) | documented |
| G-04 | Ankerkette (Kurzglied) | Short-link chain | Kette nach DIN 766 / ISO 4565 mit kurzer Teilung, Standard für Yachten | documented |
| G-05 | Ankerkette (Langglied) | Long-link chain | Kette mit längerer Teilung, für Handwinden und ältere Gypsy-Typen | documented |
| G-06 | Ankerklüse | Hawse pipe | Durchführung in der Bugwand für die Ankerkette | documented |
| G-07 | Ankerlaterne | Anchor light | Weißes Rundumlicht bei Nacht im Ankerliegen (COLREG Rule 30) | documented |
| G-08 | Ankerwinde | Anchor windlass | Mechanische oder elektrische Winde zum Einholen und Fieren der Ankerkette | documented |
| G-09 | Backing Plate | Backing plate | Verstärkungsplatte unter Deck zur Lastverteilung von Decksbeschlägen | documented |
| G-10 | Beizpaste | Pickling paste | Chemisches Mittel zur Entfernung von Anlauffarben und Wiederherstellung der Passivschicht auf Edelstahl | documented |
| G-11 | Bewuchs | Marine fouling / Biofouling | Biologischer Aufwuchs (Muscheln, Algen, Seepocken) auf Unterwasserteilen | documented |
| G-12 | Bugrolle | Bow roller | Rolle am Bug, über die die Ankerkette läuft, verringert Reibung | documented |
| G-13 | Clutch | Clutch / Gypsy clutch | Kupplung an der Ankerwinde, die den Gypsy mit dem Antrieb verbindet | documented |
| G-14 | Farbeindringprüfung | Dye penetrant testing (DPT) | Zerstörungsfreies Prüfverfahren zur Risserkennung in Schweißnähten und Metalloberflächen | documented |
| G-15 | Fieren | To pay out / To veer | Kette oder Leine kontrolliert auslassen | documented |
| G-16 | Fluke | Fluke / Palm | Der flache, grabende Teil des Ankers, der sich in den Seeboden gräbt | documented |
| G-17 | Galvanische Korrosion | Galvanic corrosion | Korrosion durch Kontakt unterschiedlich edler Metalle in Elektrolyt (Salzwasser) | documented |
| G-18 | Getriebefett | Gearbox grease | Spezielles Fett für die Windlass-Getriebeschmierung, typisch Lithium-EP NLGI 2 | documented |
| G-19 | Gypsy | Gypsy / Wildcat | Kettennuss an der Ankerwinde, geformtes Rad mit Taschen für Kettenglieder | documented |
| G-20 | Kalibrierung | Calibration | Prüfung der Kettenteilung (Abstand zwischen Gliedern) auf Normkonformität | documented |
| G-21 | Kellet | Kellet / Sentinel | Reitgewicht: Gewicht, das an der Ankerkette herabgelassen wird, um den Zugwinkel zu verbessern | documented |
| G-22 | Kettenfall | Chain fall | Der freie Fall der Kette durch Schwerkraft beim Fieren (Clutch offen) | documented |
| G-23 | Kettenführungsrohr | Chain pipe | Rohr vom Deck in den Kettenkasten, durch das die Kette geführt wird | documented |
| G-24 | Kettenkasten | Chain locker | Stauraum im Vorschiff zur Aufnahme der Ankerkette | documented |
| G-25 | Kettenmarkierung | Chain marking | Farbliche oder mechanische Markierung der Kette zur Längenbestimmung | documented |
| G-26 | Kettenstopper | Chain stopper | Mechanische Vorrichtung am Bug, die die Kette bei Ankerlast arretiert | documented |
| G-27 | Kettenteilung | Chain pitch | Abstand von Gliedmitte zu Gliedmitte (gleiche Orientierung) — maßgeblich für Gypsy-Passung | documented |
| G-28 | Kohlebürste | Carbon brush | Schleifkontakt im DC-Elektromotor, leitet Strom auf den rotierenden Kollektor | documented |
| G-29 | Kollektor | Commutator | Rotierender Kontaktring im DC-Motor, auf dem die Kohlebürsten schleifen | documented |
| G-30 | Kurzschluss | Short circuit | Unbeabsichtigte Verbindung von Plus und Minus, führt zu Sicherungsauslösung | documented |
| G-31 | Lochfraß | Pitting corrosion | Lokale, tiefe Korrosionsangriffe auf Metalloberflächen, besonders bei Edelstahl | documented |
| G-32 | MBL | Minimum Breaking Load | Mindestbruchlast: die garantierte Mindestlast, bei der ein Bauteil bricht | documented |
| G-33 | Panikschäkel | Quick-release shackle | Leicht lösbarer Schäkel am Kettenende im Kettenkasten für Notfall-Slip | documented |
| G-34 | Passivierung | Passivation | Bildung einer schützenden Chromoxidschicht auf Edelstahloberflächen | documented |
| G-35 | Ruckdämpfer | Snubber / Shock absorber | Elastisches Element (Tau oder Gummi) zwischen Kette und Boot, dämpft Stoßbelastungen | documented |
| G-36 | Schwojkreis | Swing circle | Kreisfläche, die ein ankerndes Boot bei Winddrehung überstreicht | documented |
| G-37 | Scope | Scope (chain-to-depth ratio) | Verhältnis von ausgelegter Kette/Leine zur Wassertiefe (+ Freibord) | documented |
| G-38 | Solenoid | Solenoid | Elektromagnetisches Schaltrelais, steuert den Windlass-Motor | documented |
| G-39 | Spannungsabfall | Voltage drop | Spannungsverlust auf der Kabelstrecke Batterie→Motor durch Widerstand | documented |
| G-40 | Tripleine | Trip line | Leine am Ankerkopf (Flukenseite), ermöglicht Bergung bei festsitzendem Anker | documented |
| G-41 | Verzinkung | Galvanization / Zinc coating | Zinkbeschichtung als Korrosionsschutz auf Stahlkette und Ankern | documented |
| G-42 | Wirbel | Swivel | Drehbares Verbindungselement zwischen Kette und Anker, verhindert Verdrillung | documented |
| G-43 | WLL | Working Load Limit | Zulässige Gebrauchslast: die maximale Last, der ein Bauteil im Normalbetrieb dauerhaft ausgesetzt werden darf | documented |
| G-44 | Zweitanker | Kedge anchor | Zweiter, meist leichterer Anker für Manöver, Sturmsicherung oder als Reserve | documented |
| G-45 | Ankerwächter | Anchor alarm | GPS-basiertes Warnsystem, das Alarm auslöst, wenn das Boot den definierten Schwojkreis verlässt | documented |
| G-46 | Borgschraube | Grub screw / Set screw | Madenschraube zur Sicherung des Gypsy auf der Windlass-Welle | documented |
| G-47 | Druckwasserpumpe (Ankerwäsche) | Deck wash pump | Pumpe zur Süßwasserspülung der Kette beim Einholen | documented |
| G-48 | Galvanischer Isolator | Galvanic isolator | Bauteil im Landstromkabel, das galvanische Ströme blockiert | documented |
| G-49 | Halsband (Kettenstopper) | Chain hook / Devil's claw | Hakenförmiger Teil des Kettenstoppers, der in ein Kettenglied greift | documented |
| G-50 | Kausche | Thimble | Metalleinsatz in einem Auge einer Leine, verhindert Abrieb der Leine am Schäkel | documented |
| G-51 | Kielkettung | Keel chain / Keel-stepped chain plate | Kettenverbindung durch den Kiel (bei einigen Konstruktionen zur Ankerbefestigung) | documented |
| G-52 | Landleinen-Befestigung | Shore line attachment | Befestigung einer Leine an Land (Fels, Baum, Ring), häufig in Kombination mit Heckanker | documented |
| G-53 | Nennweite | Nominal size | Der angegebene Durchmesser einer Kette oder eines Schäkels, auf den alle Maße bezogen sind | documented |
| G-54 | Prüflast | Proof load | Last, der ein Bauteil bei der Qualitätsprüfung standhalten muss (typisch 70 % MBL) | documented |
| G-55 | Rundstahlkette | Round link chain | Kette mit runden Gliedquerschnitten, Standard bei Yachten | documented |
| G-56 | Scheuerschutz | Chafe guard / Chafe protection | Schutzummantelung an Leinen, die über Rollen oder Kanten laufen | documented |
| G-57 | Spezifisches Kettengewicht | Chain weight per meter | Gewicht der Kette pro Laufmeter, relevant für Trimm und Kettenkasten-Dimensionierung | documented |
| G-58 | Sturmvorsorge | Storm preparation | Maßnahmen zur Sicherung des Ankergeschirrs vor einem Sturm | documented |
| G-59 | Trossenstopper | Line stopper / Rope clutch | Klemmvorrichtung für Leinen, analog zum Kettenstopper aber für Tauwerk | documented |
| G-60 | Windlass-Kapstan | Capstan / Warping drum | Vertikale Trommel an der Ankerwinde zum Verfahren von Leinen | documented |

---

## 12. Schnell-Referenz

### 12.1 Wartungs-Checkliste (1 Seite zum Ausdrucken)

```
┌──────────────────────────────────────────────────────────────┐
│  ANKERSYSTEM WARTUNG — SCHNELL-CHECKLISTE                    │
│  Boot: _____________ Datum: _________ Prüfer: ____________  │
├──────────────────────────────────────────────────────────────┤
│  ANKER                                              □ OK □ ! │
│  [ ] Schaft gerade, keine Verformung                         │
│  [ ] Schweißnähte rissfrei                                   │
│  [ ] Fluken nicht verbogen                                   │
│  [ ] Schäkelöse intakt                                       │
│  [ ] Verzinkung/Oberfläche ausreichend                       │
├──────────────────────────────────────────────────────────────┤
│  KETTE                                              □ OK □ ! │
│  [ ] Durchmesser ≥88% Neuwert (12% Grenze)                  │
│  [ ] Keine verformten Glieder                                │
│  [ ] Verzinkung bewertbar (>30%)                             │
│  [ ] Markierungen lesbar                                     │
│  [ ] End-Befestigung (Panikschäkel) OK                       │
├──────────────────────────────────────────────────────────────┤
│  WINDLASS                                           □ OK □ ! │
│  [ ] Funktionstest Auf/Ab                                    │
│  [ ] Gypsy-Zähne nicht abgerundet                            │
│  [ ] Clutch hält                                             │
│  [ ] Keine ungewöhnlichen Geräusche                          │
│  [ ] Befestigung fest                                        │
│  [ ] Elektrik-Anschlüsse trocken und sauber                  │
├──────────────────────────────────────────────────────────────┤
│  BUGROLLE                                           □ OK □ ! │
│  [ ] Rolle dreht frei                                        │
│  [ ] Bolzen kein Spiel                                       │
│  [ ] Sicherungssplint vorhanden                              │
│  [ ] Befestigung am Deck fest                                │
├──────────────────────────────────────────────────────────────┤
│  KETTENSTOPPER                                      □ OK □ ! │
│  [ ] Hält Kette unter Last                                   │
│  [ ] Mechanik leichtgängig                                   │
│  [ ] Klauen nicht verschlissen                               │
├──────────────────────────────────────────────────────────────┤
│  SNUBBER                                            □ OK □ ! │
│  [ ] Kein Chafe (Scheuerstellen)                             │
│  [ ] Karabiner/Haken intakt                                  │
│  [ ] Elastizität vorhanden                                   │
│  [ ] UV-Schäden prüfen                                       │
├──────────────────────────────────────────────────────────────┤
│  KETTENKASTEN                                       □ OK □ ! │
│  [ ] Sauber, kein Geruch                                     │
│  [ ] Drainage funktioniert                                   │
│  [ ] Deckel dicht                                            │
├──────────────────────────────────────────────────────────────┤
│  Ergebnis: □ Alles OK  □ Mängel siehe Rückseite             │
│  Nächste Prüfung: ____________                               │
└──────────────────────────────────────────────────────────────┘
```

### 12.2 Notfall-Kurzanleitung

| Situation | Sofortmaßnahme | Dann |
|-----------|---------------|------|
| Kette springt über Gypsy | Windlass STOPP, Kette auf Klampe belegen | Gypsy + Kette prüfen |
| Windlass tot | Hauptschalter + Sicherung prüfen | Kette manuell bergen (Winschkurbel/Leine) |
| Kettenstopper hält nicht | Last auf Windlass-Clutch, Backup-Leine auf Klampe | Stopper reparieren/tauschen |
| Snubber gerissen | Sofort zweiten Snubber anschlagen | Ursache prüfen (Chafe?) |
| Anker sitzt fest | Boot über Anker fahren, Kette senkrecht stellen | Tripleine, Taucher |
| Kette im Kasten verklemmt | Windlass stoppen, von Hand ordnen | Kettenkasten-Volumen prüfen |

### 12.3 Grenzwerte auf einen Blick

| Parameter | Warnung | Austausch/Aktion | Confidence |
|-----------|---------|-----------------|------------|
| Kette Ø-Reduktion | >8 % | >12 % | documented |
| Gypsy-Spiel (Kette in Tasche) | >1,5 mm | >2,0 mm | documented |
| Kohlebürsten-Restlänge | <10 mm | <6 mm | measured |
| Snubber-Chafe | Fasern sichtbar | Kern sichtbar | visual_high |
| Bugrolle-Bolzen-Spiel | >0,3 mm | >0,5 mm | measured |
| Verzinkung Rest | <50 % | <30 % | estimated |
| Schäkelöse Wandstärke | <90 % | <80 % | measured |
| Spannungsabfall Batterie→Motor | >5 % | >10 % | measured |

---

## ANHANG A — Fallstudien

### A1 — Fallstudie: Kettenverschleiß Bavaria 40 Cruiser (2016)

**Ausgangslage:** Bavaria 40 Cruiser, Baujahr 2010. 6 Saisons Mittelmeer (Griechenland). Original-Kette 10 mm DIN 766, 60 m. Lewmar V3 Windlass. Keine professionelle Wartung, Eigner spült Kette gelegentlich mit Süßwasser.

**Befund bei Surveyor-Inspektion (Pre-Purchase Survey 2016):**
- Erste 10 m: Durchmesser 8,6–8,9 mm (11–14 % Reduktion) → **AUSTAUSCH**
- 10–20 m: Durchmesser 8,9–9,2 mm (8–11 % Reduktion) → **WARNUNG**
- 20–40 m: Durchmesser 9,3–9,6 mm (4–7 % Reduktion) → OK
- 40–60 m: Durchmesser 9,7–9,9 mm (1–3 % Reduktion) → OK
- Gypsy: Stadium 2 Verschleiß (Abrundung sichtbar)
- Verzinkung: 0–10 % auf ersten 20 m, 30–50 % auf Rest
- Schäkel Kette→Anker: 9,2 mm (Bolzen), Neuwert 10 mm → tauschen

**Empfehlung:** Erste 20 m Kette ersetzen oder Kette umdrehen + innerhalb 2 Saisons komplett neu. Gypsy mittelfristig tauschen. Schäkel sofort tauschen.

**Kosten:** Neue Kette 60 m × 10 mm: ca. 650 €. Gypsy Lewmar V3: ca. 380 €. Schäkel: ca. 25 €. Gesamt: ca. 1.055 €.

**AYDI-Bewertung:** Confidence: measured (Stichprobe), Score: 35/100 (Kette), 55/100 (Gypsy), 20/100 (Schäkel).

### A2 — Fallstudie: Windlass-Motorversagen Hallberg-Rassy 372 (2018)

**Ausgangslage:** HR 372, Baujahr 2005. Blauwasser seit 2012 (Atlantik, Karibik, Mittelmeer). Lofrans Tigres 1500 W. Ca. 400 Betriebsstunden geschätzt. Letzte Wartung: 2015 (Getriebefett).

**Symptom:** Windlass dreht sehr langsam, zieht Kette kaum noch. Motor wird heiß.

**Diagnose:**
1. Spannungsabfall: 12,7 V Batterie → 10,2 V am Motor unter Last (2,5 V / 20 % Verlust!) → Kabelstrecke zu lang, Querschnitt grenzwertig (25 mm²), Klemmen korrodiert
2. Kohlen: 4 mm Restlänge (Neuwert 18 mm) → weit unter Minimum
3. Kollektor: Rillenbildung, Brandflecken
4. Getriebefett: verharzt, teilweise trocken
5. Gypsy: Stadium 1 (leichter Verschleiß) → OK

**Behebung:**
1. Kabelstrecke erneuert: 35 mm² statt 25 mm², neue Kabelschuhe (gecrimpt + verlötet)
2. Neue Kohlebürsten (Lofrans Originalteile)
3. Kollektor geschliffen und Mica-Schnitt erneuert
4. Getriebe komplett gereinigt und neu befettet
5. Spannungsabfall nach Reparatur: 12,7 V → 11,8 V (0,9 V / 7 %) → akzeptabel

**Kosten:** Kabel + Kabelschuhe: ca. 180 €. Kohlen: ca. 65 €. Getriebefett: ca. 25 €. Arbeitszeit (Werft): ca. 4 h × 85 €/h = 340 €. Gesamt: ca. 610 €.

**AYDI-Bewertung:** Confidence: measured (Spannung, Kohlen), Score: 25/100 vor Reparatur, 85/100 nach Reparatur.

### A3 — Fallstudie: Gypsy-Ketten-Inkompatibilität Jeanneau Sun Odyssey 440 (2021)

**Ausgangslage:** Jeanneau SO 440, Baujahr 2019. Eigner hat Original-Kette (10 mm DIN 766, Gesal/Maggi) durch günstigere Kette ersetzt (10 mm, aber ISO 4565, chinesischer Hersteller). Lewmar V3 Windlass.

**Symptom:** Kette springt beim Einholen regelmäßig über den Gypsy, besonders unter Last. Beim Fieren klemmt die Kette gelegentlich.

**Diagnose:**
1. Kettenglied-Durchmesser: 10,1 mm → OK
2. Kettenteilung: 29,5 mm (gemessen über 10 Glieder, Mittelwert)
3. Gypsy-Spezifikation: DIN 766, Teilung 28,0 mm
4. Differenz: 1,5 mm = 5,4 % → AUSSERHALB der 2,5 %-Toleranz
5. Ursache: Die Ersatzkette ist nach anderer Norm gefertigt als die Original-Kette

**Behebung:** Kette gegen korrekte DIN 766-Kette eines namhaften Herstellers (Titan, Maggi, ACCO) getauscht.

**Kosten:** Neue Kette 80 m × 10 mm DIN 766: ca. 920 €. "Gesparte" Kette (Verlust): ca. 450 €. Insgesamt: 1.370 € statt 920 € bei korrektem Erstkauf.

**Lehre:** IMMER Kette nach der exakten Gypsy-Spezifikation kaufen, nicht nur nach Durchmesser.

### A4 — Fallstudie: Bugrolle-Bruch Beneteau Oceanis 38.1 (2020)

**Ausgangslage:** Beneteau Oceanis 38.1, Baujahr 2018. Mittelmeer-Nutzung, Gelegenheitssegler. Anker (Rocna Vulcan 15 kg) auf Original-Bugrolle.

**Symptom:** Beim Ankerlichten bei 25 kn Wind brach die Bugrolle-Halterung. Anker + 5 m Kette fielen ins Wasser.

**Diagnose:**
1. Bruchstelle: Schweißnaht Bugrolle-Konsole → Deck-Flansch
2. Ursache: Original-Bugrolle war für leichteren Anker dimensioniert (Delta 10 kg). Rocna Vulcan 15 kg = 50 % schwerer + höheres Trägheitsmoment bei Seegang
3. Backing Plate: zu klein (60 × 60 mm statt empfohlen 150 × 100 mm)
4. GFK unter Befestigung: Delaminationsanzeichen (Klopftest hohl)

**Behebung:**
1. GFK-Reparatur am Bug (Delaminationsbereich abgefräst, Neuaufbau mit Epoxid + Glasfaser)
2. Neue Bugrolle mit größerer Auflagefläche (Plastimo Inox)
3. Große Backing Plate aus Edelstahl 316L (150 × 120 × 5 mm)
4. M10-Bolzen mit selbstsichernden Muttern (statt Blechschrauben!)

**Kosten:** GFK-Reparatur: ca. 800 €. Neue Bugrolle: ca. 280 €. Backing Plate: ca. 60 €. Ankerbergung (Taucher): ca. 150 €. Arbeitszeit: ca. 6 h × 85 €/h = 510 €. Gesamt: ca. 1.800 €.

### A5 — Fallstudie: Galvanische Korrosion am Ankersystem Amel 50 (2023)

**Ausgangslage:** Amel 50, Baujahr 2020, Blauwasser (Karibik seit 2021). Aluminium-Anker (Fortress FX-37) + Edelstahl-Wirbel + verzinkte Stahlkette + Edelstahl-Kettenstopper.

**Symptom:** Nach 18 Monaten Karibik: Wirbel-Bolzen hat sich aufgelöst, Kettenglieder um Wirbel stark korrodiert (5 mm statt 10 mm), Rest der Kette relativ gut.

**Diagnose:** Klassische galvanische Korrosion:
- Alu-Anker (sehr unedel) + Edelstahl-Wirbel (edel) + Stahlkette (mittel) = galvanische Spannungsreihe
- Der Wirbel war das "Epizentrum" — dort trafen alle drei Metalle aufeinander
- Tropisch warmes Salzwasser = maximale Leitfähigkeit = maximale galvanische Korrosionsrate

**Behebung:**
1. Alu-Anker mit Alu-Wirbel oder ohne Wirbel (direkt Edelstahl-Schäkel mit Isolierung)
2. Tef-Gel auf allen Metall-Metall-Kontaktflächen
3. Opferanode (Zink) am Ankergeschirr montiert
4. Erste 10 m Kette getauscht (zu stark korrodiert)

**Lehre:** Verschiedene Metalle im Ankersystem = galvanischer Kontakt = Korrosion. Besonders kritisch in tropischen Gewässern. Isolierung oder gleiche Legierungen verwenden.

### A6 — Fallstudie: Snubber-Versagen bei Nachtsturm Catamaran Lagoon 42 (2022)

**Ausgangslage:** Lagoon 42, Sardinia. Ankerliegen bei vorhergesagt 15 kn. Nachts unerwartet 35–40 kn Böen (Gewitter). Nylon-Snubber (14 mm, 3-schäftig), Bridle-Konfiguration.

**Symptom:** Um 03:00 lauter Knall — Steuerbord-Snubber gerissen. Gesamte Last auf Backbord-Snubber → nach 10 min auch dieser gerissen. Last auf Windlass. Ankeralarm (GPS-Drag).

**Diagnose:**
1. Snubber-Bruchstelle: exakt an der Stelle, wo Snubber über Bugrolle lief (Chafe)
2. Scheuerschutz (Neopren-Ummantelung) war nach unten gerutscht
3. Snubber war 3 Jahre alt, UV-exponiert gelagert → Restfestigkeit geschätzt 60–70 %
4. Belastung bei 40 kn Böe auf Lagoon 42: ca. 2.800 kg → MBL 14-mm-Nylon 3-schäftig neu: ca. 4.200 kg → bei 60 % Rest: ca. 2.500 kg → UNTER der Belastung

**Behebung:**
1. Neue Snubber 16 mm (statt 14 mm) → MBL ca. 5.500 kg
2. Fest installierter Scheuerschutz (aufgespleißte Lederhülle)
3. UV-Schutzhülle bei Nichtgebrauch
4. Jährlicher Austausch der Snubber bei Blauwasserfahrt

### A7 — Fallstudie: Kettenkasten-Drainage-Problem X-Yachts X4.3 (2021)

**Ausgangslage:** X-Yachts X4.3, Baujahr 2017. Ostsee-Nutzung, Winter im Wasser (Dänemark).

**Symptom:** Wasseransammlung im Vorschiff (20–30 l), Geruch, Schimmel auf Vorschiff-Matratze.

**Diagnose:**
1. Drainage-Schlauch vom Kettenkasten: verstopft (Muschelreste + Algenklumpen)
2. Rückschlagventil: verklebt (nicht mehr schließend bei Fahrt, nicht mehr öffnend bei Ruhe)
3. Kettenkasten-Deckel: Dichtung verhärtet, undicht
4. Bugrolle-Durchführung: Sikaflex gerissen

**Behebung:**
1. Drainage-Schlauch erneuert (19 mm statt 16 mm Original → weniger Verstopfungsneigung)
2. Neues Rückschlagventil (Trudesign in-line valve)
3. Neue Deckeldichtung (EPDM-Profil)
4. Bugrolle-Befestigung neu abgedichtet (Sikaflex 291i)

**Kosten:** Material: ca. 120 €. Arbeitszeit: ca. 3 h × 85 €/h = 255 €. Gesamt: ca. 375 €.

### A8 — Fallstudie: Windlass-Solenoid-Ausfall Hanse 548 (2024)

**Ausgangslage:** Hanse 548, Baujahr 2022. Quick Prince DP3 1500 W Windlass. Erste Saison problemlos, zweite Saison: intermittierende Ausfälle.

**Symptom:** Windlass funktioniert manchmal, manchmal nicht. Keine Korrelation mit Richtung (Auf/Ab). Problem tritt häufiger bei Feuchtigkeit (Regen, Spritzwasser) auf.

**Diagnose:**
1. Sicherung: OK
2. Fußschalter: Durchgangsprüfung OK
3. Kabel Fußschalter → Solenoid: 2,3 V statt 12 V (unter Last) → Kabelwiderstand
4. Solenoid: Korrosion an Anschlussklemmen (grüne Kupferoxid-Krusten)
5. Ursache: Decksdurchführung des Steuerkabels nicht abgedichtet, Kondenswasser tropft auf Solenoid

**Behebung:**
1. Solenoid-Anschlüsse gereinigt, neue Kabelschuhe (gecrimpt + verlötet)
2. Schrumpfschlauch mit Kleber auf alle Verbindungen
3. Decksdurchführung des Steuerkabels mit Sikaflex 291i abgedichtet
4. Solenoid mit Neopren-Kappe geschützt
5. Steuerkabel erneuert (marinisiertes Kabel, tinned copper)

**Kosten:** Material: ca. 85 €. Arbeitszeit: ca. 2 h × 85 €/h = 170 €. Gesamt: ca. 255 €.

---

## ANHANG B — Wartungsprotokolle (Vorlagen)

### B1 — Jährliches Wartungsprotokoll Ankersystem

| Feld | Eintrag |
|------|---------|
| Boot | __________________ |
| Datum | __________________ |
| Prüfer | __________________ |
| Saison-Betriebsstunden (geschätzt) | ________ h |
| Ankernächte (geschätzt) | ________ |
| Revier | __________________ |

**Ketten-Messung:**

| Position (m) | Ø gemessen (mm) | Ø Soll (mm) | Reduktion (%) | Bewertung |
|-------------|----------------|-------------|---------------|-----------|
| 5 | | | | |
| 10 | | | | |
| 15 | | | | |
| 20 | | | | |
| 25 | | | | |
| 30 | | | | |
| 40 | | | | |
| 50 | | | | |

**Windlass:**

| Prüfpunkt | Ergebnis | Bemerkung |
|-----------|----------|-----------|
| Funktionstest Auf | □ OK □ Eingeschränkt □ Defekt | |
| Funktionstest Ab | □ OK □ Eingeschränkt □ Defekt | |
| Gypsy-Zustand | □ Gut □ Leichter Verschleiß □ Tausch nötig | |
| Clutch | □ Hält □ Rutscht | |
| Kohlen (mm) | ________ mm | Neuwert: ________ mm |
| Getriebefett | □ OK □ Gewechselt □ Ergänzt | Typ: |
| Spannung unter Last | ________ V | Batterie: ________ V |

### B2 — Ketten-Messprotokoll (Detailliert)

| Glied Nr. | Position (m) | Ø-A (mm) | Ø-B (mm) | Ø-C (mm) | Min (mm) | % Soll | Bewertung |
|-----------|-------------|----------|----------|----------|---------|--------|-----------|
| 1 | 0,3 | | | | | | |
| 2 | 1,0 | | | | | | |
| 3 | 2,0 | | | | | | |
| ... | ... | | | | | | |

---

## ANHANG C — Confidence-Mapping

### C1 — Confidence-Zuordnung nach Prüfmethode

| Prüfmethode | AYDI Confidence Level | Begründung |
|-------------|----------------------|------------|
| Messschieber-Messung | `measured` | Quantitativ, reproduzierbar, ±0,05 mm |
| Drehmomentschlüssel | `measured` | Quantitativ, kalibriert |
| Multimeter-Messung | `measured` | Quantitativ, reproduzierbar |
| Farbeindringprüfung | `measured` | Standardisiertes Prüfverfahren |
| Schichtdickenmessung | `measured` | Instrumentell, kalibriert |
| Foto-Bewertung (klar, nah) | `visual_high` | Eindeutige Merkmale erkennbar |
| Foto-Bewertung (mittel) | `visual_medium` | Merkmale erkennbar, Unsicherheit |
| Foto-Bewertung (unklar) | `visual_low` | Zu wenig Detail, Mehrdeutigkeit |
| Klopftest | `estimated` | Subjektiv, erfahrungsabhängig |
| Altersbasierte Schätzung | `estimated` | Statistischer Mittelwert |
| Hersteller-Datenblatt | `documented` | Verifizierte Herstellerangabe |
| Serviceprotokoll | `documented` | Nachvollziehbare Dokumentation |

### C2 — Score-Fusion für Ankersystem-Bewertung

| Bewertungsaspekt | Structured Weight | Visual Weight |
|------------------|------------------|--------------|
| Kettenverschleiß | 0.85 | 0.15 |
| Gypsy-Zustand | 0.60 | 0.40 |
| Windlass-Funktion | 0.90 | 0.10 |
| Bugrolle-Zustand | 0.50 | 0.50 |
| Snubber-Zustand | 0.30 | 0.70 |
| Verzinkung | 0.40 | 0.60 |
| Kettenstopper | 0.65 | 0.35 |
| Kettenkasten | 0.30 | 0.70 |

---

## ANHANG D — Normen-Zusammenfassung

### D1 — Relevante Normen für Ankersystem-Wartung

| Norm | Titel | Relevanz für Wartung | Confidence |
|------|-------|---------------------|------------|
| ISO 1704:2008 | Shipbuilding — Stud-link anchor chains | Kettendurchmesser-Grenzwerte, Kalibrierung | documented |
| ISO 4565:1986 | Small craft — Anchor chains | Maße kurzgliedrige Kette (Yacht-Standard) | documented |
| DIN 766 | Rundstahlkette — Kurzgliedrig | Deutsche Norm; Maße wie ISO 4565 außer bei 10 mm (DIN Teilung 28 mm vs. ISO 30 mm) | documented |
| ISO 15084:2003 | Small craft — Anchoring, mooring and towing — Strong points | Festigkeit der Anschlag-/Befestigungspunkte für Anker, Vertäuung, Schlepp | documented |
| ISO 8665:2006 | Small craft — Marine propulsion RIC engines — Power measurements and declarations | Motorleistungsnorm — nicht wartungsrelevant für Ankersysteme (irrtümlich gelistet) | documented |
| ABYC H-40 | Anchoring, Mooring and Strong Points | Jährliche Inspektion, Bruchlastanforderungen | documented |
| CE RCD 2013/53/EU | Recreational Craft Directive | Grundlegende Sicherheitsanforderungen | documented |
| EN 12385-4 | Wire ropes — Safety | Drahtseil-Prüfkriterien (für Drahtseiltrossenaanker) | documented |

> ✅ Aufgeloest (Audit): Beide Normzuordnungen korrigiert. ISO 15084:2003 = "Small craft — Anchoring, mooring and towing — Strong points" (nicht "Windlasses"); ISO 8665:2006 = "Small craft — Marine propulsion reciprocating internal combustion engines — Power measurements and declarations" (Motorleistung, nicht "Marine anchors"). — Quellen: iso.org/standard/26407, iso.org/standard/34511.

---

## ANHANG E — Hersteller-Serviceadressen

### E1 — Windlass-Hersteller Service-Kontakte

| Hersteller | Land | Service-Email | Ersatzteile Online | Confidence |
|------------|------|--------------|-------------------|------------|
| Lewmar | UK | service@lewmar.com | lewmar.com/spares | documented |
| Lofrans | IT | info@lofrans.com | lofrans.com | documented |
| Quick | IT | info@quickitaly.com | quickitaly.com | documented |
| Maxwell | NZ | service@maxwell-marine.com | maxwell-marine.com | documented |
| Muir | AU | sales@muir.com.au | muir.com.au | documented |
| Italwinch | IT | info@italwinch.it | italwinch.it | documented |
| Vetus | NL | service@vetus.com | vetus.com | documented |
| South Pacific | TW | info@spiindustrial.com | spiindustrial.com | documented |

### E2 — Ketten-Hersteller und -Lieferanten (Europa)

| Hersteller/Lieferant | Land | Standard | Verfügbarkeit | Confidence |
|----------------------|------|----------|---------------|------------|
| ACCO (Peerless) | USA | BBB, G43, HT | Europa über Händler | documented |
| Titan Marine | UK | DIN 766, ISO 4565 | Gut in Europa | documented |
| Maggi (Gesal) | IT | DIN 766 | OEM Beneteau, Jeanneau | documented |
| PWB (Polaris) | AU | DIN 766, BBB, G70 | Gut in Europa | documented |
| Vicinay | ES | ISO 1704 (Großketten) | Superyacht/Commercial | documented |
| Cochain | FR | DIN 766 | Frankreich, über Händler | documented |

---

## ANHANG F — Werkzeuglisten

### F1 — Basis-Werkzeug Eigner-Wartung

| Werkzeug | Verwendung | Geschätzte Kosten | Confidence |
|----------|-----------|------------------:|------------|
| Digitaler Messschieber (150 mm, 0,01 mm) | Kettenmessung, Gypsy-Messung | 25–80 € | documented |
| Multimeter (digital) | Spannungs-/Strommessung Windlass | 30–100 € | documented |
| Drehmomentschlüssel (10–60 Nm) | Befestigungsschrauben | 40–120 € | documented |
| Innensechskant-Satz (metrisch + Zoll) | Windlass-Gehäuse | 15–40 € | documented |
| Ringmaul-Schlüsselsatz (8–19 mm) | Allgemein | 20–60 € | documented |
| Drahtbürste (Edelstahl + Messing) | Reinigung, Entrostung | 5–15 € | documented |
| Fettpresse (manuell) | Schmiernippel | 20–50 € | documented |
| Lupe (10×) | Schweißnaht-Inspektion | 5–15 € | documented |
| LED-Taschenlampe (Kopflampe) | Inspektion unter Deck | 15–40 € | documented |
| Splintentreiber-Satz | Bugrolle-Splinte | 10–20 € | documented |

### F2 — Erweitertes Werkzeug (Profi/Surveyor)

| Werkzeug | Verwendung | Geschätzte Kosten | Confidence |
|----------|-----------|------------------:|------------|
| Farbeindring-Prüfset (PT) | Schweißnaht-Rissprüfung | 30–60 € | documented |
| Schichtdickenmessgerät | Verzinkungsmessung | 200–800 € | documented |
| Zangenamperemeter (DC, bis 200 A) | Windlass-Stromaufnahme | 50–150 € | documented |
| Endoskop/Boreskop | Inspektion in Hohlräumen | 100–500 € | documented |
| Isolationsmessgerät (Megger) | Motor-Isolationsprüfung | 150–400 € | documented |
| Abzieher-Satz | Gypsy-Demontage | 30–80 € | documented |
| Drehzahlmesser (optisch) | Windlass-Motordrehzahl | 40–100 € | documented |

---

## ANHANG G — Saisonale Checklisten

### G1 — Checkliste Saisonstart (Komplett)

| Nr. | Arbeitsschritt | Dauer | Material | Erledigt |
|-----|---------------|-------|----------|----------|
| 1 | Kettenkasten öffnen, Zustand prüfen | 10 min | — | □ |
| 2 | Kette komplett auslegen auf Steg/Plane | 30 min | Plane | □ |
| 3 | Kette mit Süßwasser spülen | 15 min | Wasser | □ |
| 4 | Kettenglieder Stichprobe messen (alle 5 m) | 30 min | Messschieber | □ |
| 5 | Kette auf verformte Glieder prüfen | 15 min | — | □ |
| 6 | Markierungen prüfen/erneuern | 20 min | Farbe/Clips | □ |
| 7 | Anker inspizieren (Schaft, Fluken, Schweißnähte) | 15 min | Lupe, Drahtbürste | □ |
| 8 | Schäkel und Wirbel prüfen | 10 min | Messschieber | □ |
| 9 | Windlass Hauptschalter EIN | 2 min | — | □ |
| 10 | Windlass Funktionstest Auf/Ab (ohne Last) | 5 min | — | □ |
| 11 | Gypsy reinigen und prüfen | 10 min | Bürste | □ |
| 12 | Clutch testen (Fest/Frei) | 5 min | — | □ |
| 13 | Bugrolle reinigen und schmieren | 15 min | Fett/PTFE-Spray | □ |
| 14 | Bugrolle-Befestigung prüfen | 10 min | Schlüssel | □ |
| 15 | Kettenstopper Funktionstest | 5 min | — | □ |
| 16 | Snubber prüfen (Chafe, UV, Elastizität) | 10 min | — | □ |
| 17 | Kettenkasten reinigen | 20 min | Reiniger, Bürste | □ |
| 18 | Drainage testen (Wasser einfüllen) | 5 min | Wasser | □ |
| 19 | Kette zurücklegen, Freilauf testen | 20 min | — | □ |
| 20 | Ankerlaterne prüfen | 5 min | — | □ |
| **Gesamt** | | **~4–5 h** | | |

### G2 — Checkliste Saisonende / Winterlager (Komplett)

| Nr. | Arbeitsschritt | Dauer | Material | Erledigt |
|-----|---------------|-------|----------|----------|
| 1 | Kette komplett auslegen | 30 min | Plane | □ |
| 2 | Kette gründlich mit Süßwasser spülen | 20 min | Wasser, ggf. Hochdruckreiniger | □ |
| 3 | Kette trocknen lassen (24 h ideal) | — | — | □ |
| 4 | Kette mit Konservierungsspray behandeln | 30 min | Zinkspray/Lanolin | □ |
| 5 | Kettenkasten gründlich reinigen | 30 min | Reiniger, Bürste | □ |
| 6 | Kettenkasten desinfizieren | 15 min | Essigessenz/Chlor | □ |
| 7 | Kettenkasten-Deckel offen lassen (Belüftung) | — | — | □ |
| 8 | Anker reinigen und inspizieren | 20 min | Süßwasser, Bürste | □ |
| 9 | Anker trocken lagern | — | — | □ |
| 10 | Windlass-Getriebe nachfetten (oder Öl prüfen) | 30 min | Fett/Öl | □ |
| 11 | Windlass kurz laufen lassen (Fettverteilung) | 5 min | — | □ |
| 12 | Windlass-Batterie abklemmen (oder Hauptschalter AUS) | 5 min | — | □ |
| 13 | Bugrolle reinigen, schmieren, Bolzen fetten | 15 min | Fett | □ |
| 14 | Snubber waschen (Süßwasser), trocknen, UV-geschützt lagern | 15 min | Süßwasser | □ |
| 15 | Alle Schäkel und Verbindungen mit Tef-Gel behandeln | 15 min | Tef-Gel | □ |
| 16 | Ankerbeleuchtung prüfen/konservieren | 5 min | — | □ |
| 17 | Winterabdeckung Windlass (falls kein Hardtop) | 10 min | Plane/Neoprenkappe | □ |
| **Gesamt** | | **~5–7 h** (plus Trocknungszeiten) | | |

---

## ANHANG H — AYDI-Integration (Pydantic-Modelle)

### H1 — Datenmodelle für Ankersystem-Wartung

```python
"""
AYDI Anchor System Maintenance Models
Pydantic v2 models for anchor system condition assessment.
"""

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ConfidenceLevel(str, Enum):
    """Confidence levels for anchor system assessments."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class ComponentCondition(str, Enum):
    """Condition rating for anchor system components."""
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    WARNING = "warning"
    CRITICAL = "critical"
    FAILED = "failed"
    NOT_ASSESSED = "not_assessed"


class ChainGrade(str, Enum):
    """Anchor chain grade classifications."""
    G30 = "G30"
    G40 = "G40"
    G43 = "G43"
    G70 = "G70"


class ChainStandard(str, Enum):
    """Anchor chain dimensional standards."""
    DIN_766 = "DIN_766"
    ISO_4565 = "ISO_4565"
    BBB = "BBB"
    HT = "HT"


class GalvanizationLevel(str, Enum):
    """Galvanization remaining percentage bands."""
    EXCELLENT_80_PLUS = "80_plus"
    GOOD_60_80 = "60_80"
    FAIR_40_60 = "40_60"
    POOR_20_40 = "20_40"
    CRITICAL_BELOW_20 = "below_20"


class GypsyWearStage(str, Enum):
    """Gypsy tooth wear stages."""
    STAGE_0_NEW = "stage_0_new"
    STAGE_1_LIGHT = "stage_1_light"
    STAGE_2_MEDIUM = "stage_2_medium"
    STAGE_3_HEAVY = "stage_3_heavy"
    STAGE_4_CRITICAL = "stage_4_critical"


class ChafeLevel(str, Enum):
    """Snubber/line chafe assessment levels."""
    NONE = "none"
    LIGHT = "light"
    MEDIUM = "medium"
    HEAVY = "heavy"
    CRITICAL = "critical"


class WindlassType(str, Enum):
    """Windlass drive types."""
    ELECTRIC_DC = "electric_dc"
    ELECTRIC_AC = "electric_ac"
    HYDRAULIC = "hydraulic"
    MANUAL = "manual"


# ── Core Assessment Models ──


class ChainLinkMeasurement(BaseModel):
    """Single chain link diameter measurement."""
    model_config = {"from_attributes": True}

    position_m: float = Field(..., ge=0, le=200, description="Position along chain in meters")
    diameter_a_mm: float = Field(..., ge=3, le=25, description="Diameter at point A (inner curve)")
    diameter_b_mm: float = Field(..., ge=3, le=25, description="Diameter at point B (straight side)")
    diameter_c_mm: float = Field(..., ge=3, le=25, description="Diameter at point C (outer curve)")
    nominal_diameter_mm: float = Field(..., ge=4, le=22, description="Nominal chain diameter")
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED

    @property
    def min_diameter_mm(self) -> float:
        """Return the minimum measured diameter."""
        return min(self.diameter_a_mm, self.diameter_b_mm, self.diameter_c_mm)

    @property
    def reduction_percent(self) -> float:
        """Calculate diameter reduction percentage."""
        return round(
            (1 - self.min_diameter_mm / self.nominal_diameter_mm) * 100, 1
        )

    @property
    def condition(self) -> ComponentCondition:
        """Assess condition based on reduction percentage."""
        reduction = self.reduction_percent
        if reduction < 5:
            return ComponentCondition.EXCELLENT
        elif reduction < 8:
            return ComponentCondition.GOOD
        elif reduction < 10:
            return ComponentCondition.WARNING
        elif reduction < 12:
            return ComponentCondition.CRITICAL
        else:
            return ComponentCondition.FAILED


class ChainAssessment(BaseModel):
    """Complete chain condition assessment."""
    model_config = {"from_attributes": True}

    chain_length_m: float = Field(..., ge=10, le=300, description="Total chain length in meters")
    nominal_diameter_mm: float = Field(..., ge=4, le=22, description="Nominal chain diameter")
    chain_grade: ChainGrade = Field(default=ChainGrade.G40)
    chain_standard: ChainStandard = Field(default=ChainStandard.DIN_766)
    age_years: Optional[float] = Field(None, ge=0, le=30, description="Chain age in years")
    measurements: list[ChainLinkMeasurement] = Field(
        default_factory=list, description="Individual link measurements"
    )
    galvanization: GalvanizationLevel = Field(default=GalvanizationLevel.GOOD_60_80)
    deformed_links_count: int = Field(default=0, ge=0, description="Number of deformed links")
    pitch_deviation_percent: Optional[float] = Field(
        None, ge=-10, le=10, description="Pitch deviation from nominal"
    )
    overall_condition: ComponentCondition = Field(default=ComponentCondition.NOT_ASSESSED)
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED
    notes: Optional[str] = None

    @property
    def worst_reduction_percent(self) -> Optional[float]:
        """Return worst reduction percentage from all measurements."""
        if not self.measurements:
            return None
        return max(m.reduction_percent for m in self.measurements)

    @property
    def estimated_remaining_life_years(self) -> Optional[float]:
        """Estimate remaining chain life based on current wear rate."""
        if not self.measurements or self.age_years is None or self.age_years == 0:
            return None
        worst = self.worst_reduction_percent
        if worst is None or worst <= 0:
            return None
        wear_rate_per_year = worst / self.age_years
        remaining_budget = 12.0 - worst  # 12% is replacement threshold
        if remaining_budget <= 0:
            return 0.0
        return round(remaining_budget / wear_rate_per_year, 1)


class GypsyAssessment(BaseModel):
    """Gypsy (wildcat) condition assessment."""
    model_config = {"from_attributes": True}

    windlass_manufacturer: str = Field(..., min_length=1, max_length=100)
    windlass_model: str = Field(..., min_length=1, max_length=100)
    gypsy_material: str = Field(default="bronze", description="Gypsy material (bronze, stainless, chrome)")
    wear_stage: GypsyWearStage = Field(default=GypsyWearStage.STAGE_0_NEW)
    chain_play_mm: Optional[float] = Field(
        None, ge=0, le=10, description="Play between chain and gypsy pocket"
    )
    tooth_height_mm: Optional[float] = Field(None, ge=0, le=25, description="Remaining tooth height")
    tooth_height_nominal_mm: Optional[float] = Field(None, ge=0, le=25, description="Nominal tooth height")
    compatible_chain_standard: ChainStandard = Field(default=ChainStandard.DIN_766)
    compatible_chain_diameter_mm: float = Field(..., ge=4, le=22)
    condition: ComponentCondition = Field(default=ComponentCondition.NOT_ASSESSED)
    confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_MEDIUM
    notes: Optional[str] = None


class WindlassMotorAssessment(BaseModel):
    """Windlass motor condition assessment."""
    model_config = {"from_attributes": True}

    windlass_type: WindlassType = Field(default=WindlassType.ELECTRIC_DC)
    manufacturer: str = Field(..., min_length=1, max_length=100)
    model: str = Field(..., min_length=1, max_length=100)
    power_watts: int = Field(..., ge=100, le=5000, description="Rated motor power in watts")
    voltage: int = Field(default=12, description="Nominal voltage (12 or 24)")
    estimated_operating_hours: Optional[float] = Field(
        None, ge=0, le=2000, description="Estimated total operating hours"
    )
    brush_length_mm: Optional[float] = Field(
        None, ge=0, le=30, description="Carbon brush remaining length"
    )
    brush_length_new_mm: Optional[float] = Field(
        None, ge=5, le=30, description="New carbon brush length"
    )
    battery_voltage_v: Optional[float] = Field(
        None, ge=10, le=30, description="Battery voltage under load"
    )
    motor_voltage_v: Optional[float] = Field(
        None, ge=8, le=30, description="Voltage at motor terminals under load"
    )
    current_draw_a: Optional[float] = Field(
        None, ge=0, le=300, description="Motor current draw under load"
    )
    gearbox_grease_condition: Optional[str] = Field(
        None, description="Gearbox grease condition description"
    )
    condition: ComponentCondition = Field(default=ComponentCondition.NOT_ASSESSED)
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED
    notes: Optional[str] = None

    @property
    def voltage_drop_percent(self) -> Optional[float]:
        """Calculate voltage drop percentage."""
        if self.battery_voltage_v and self.motor_voltage_v:
            return round(
                (1 - self.motor_voltage_v / self.battery_voltage_v) * 100, 1
            )
        return None

    @property
    def brush_remaining_percent(self) -> Optional[float]:
        """Calculate carbon brush remaining percentage."""
        if self.brush_length_mm is not None and self.brush_length_new_mm:
            return round(self.brush_length_mm / self.brush_length_new_mm * 100, 1)
        return None


class BowRollerAssessment(BaseModel):
    """Bow roller condition assessment."""
    model_config = {"from_attributes": True}

    roller_material: str = Field(default="stainless_316L", description="Roller material")
    bushing_type: str = Field(default="nylon", description="Bushing type (nylon, bronze, bearing)")
    pin_diameter_mm: Optional[float] = Field(None, ge=5, le=30)
    pin_play_mm: Optional[float] = Field(
        None, ge=0, le=5, description="Pin radial play"
    )
    roller_rotates_freely: bool = Field(default=True)
    split_pin_present: bool = Field(default=True)
    mounting_bolts_tight: bool = Field(default=True)
    backing_plate_present: bool = Field(default=True)
    sealant_condition: Optional[str] = Field(None, description="Deck sealant condition")
    condition: ComponentCondition = Field(default=ComponentCondition.NOT_ASSESSED)
    confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_HIGH
    notes: Optional[str] = None


class SnubberAssessment(BaseModel):
    """Snubber/rode condition assessment."""
    model_config = {"from_attributes": True}

    material: str = Field(default="nylon_3_strand", description="Snubber material type")
    diameter_mm: float = Field(..., ge=8, le=30, description="Snubber rope diameter")
    length_m: float = Field(..., ge=3, le=30, description="Snubber length")
    age_years: Optional[float] = Field(None, ge=0, le=10)
    chafe_level: ChafeLevel = Field(default=ChafeLevel.NONE)
    uv_damage_visible: bool = Field(default=False)
    hardened: bool = Field(default=False, description="Rope has lost flexibility")
    chafe_protection_present: bool = Field(default=True)
    estimated_remaining_strength_percent: Optional[float] = Field(
        None, ge=0, le=100, description="Estimated remaining breaking strength"
    )
    condition: ComponentCondition = Field(default=ComponentCondition.NOT_ASSESSED)
    confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_HIGH
    notes: Optional[str] = None


class ChainStopperAssessment(BaseModel):
    """Chain stopper condition assessment."""
    model_config = {"from_attributes": True}

    stopper_type: str = Field(default="hinged_bar", description="Stopper mechanism type")
    holds_under_load: bool = Field(default=True)
    jaw_wear_visible: bool = Field(default=False)
    spring_functional: bool = Field(default=True)
    mounting_secure: bool = Field(default=True)
    compatible_chain_mm: float = Field(..., ge=4, le=22)
    condition: ComponentCondition = Field(default=ComponentCondition.NOT_ASSESSED)
    confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_HIGH
    notes: Optional[str] = None


class ChainLockerAssessment(BaseModel):
    """Chain locker condition assessment."""
    model_config = {"from_attributes": True}

    volume_liters: Optional[float] = Field(None, ge=10, le=500)
    drainage_functional: bool = Field(default=True)
    odor_present: bool = Field(default=False)
    fouling_present: bool = Field(default=False)
    lid_seal_intact: bool = Field(default=True)
    panic_shackle_accessible: bool = Field(default=True)
    condition: ComponentCondition = Field(default=ComponentCondition.NOT_ASSESSED)
    confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_HIGH
    notes: Optional[str] = None


class AnchorInspection(BaseModel):
    """Anchor physical inspection results."""
    model_config = {"from_attributes": True}

    anchor_type: str = Field(..., description="Anchor type (e.g. Rocna, Delta, Fortress)")
    anchor_weight_kg: float = Field(..., ge=1, le=200)
    material: str = Field(default="galvanized_steel")
    shank_straight: bool = Field(default=True)
    shank_deviation_mm_per_m: Optional[float] = Field(
        None, ge=0, le=20, description="Shank straightness deviation"
    )
    weld_seams_intact: bool = Field(default=True)
    weld_crack_detected: bool = Field(default=False)
    fluke_angle_deviation_deg: Optional[float] = Field(
        None, ge=0, le=15, description="Fluke angle deviation from nominal"
    )
    shackle_eye_wall_thickness_mm: Optional[float] = Field(
        None, ge=3, le=30, description="Shackle eye remaining wall thickness"
    )
    shackle_eye_nominal_mm: Optional[float] = Field(
        None, ge=5, le=30, description="Shackle eye nominal wall thickness"
    )
    galvanization: Optional[GalvanizationLevel] = None
    condition: ComponentCondition = Field(default=ComponentCondition.NOT_ASSESSED)
    confidence: ConfidenceLevel = ConfidenceLevel.VISUAL_HIGH
    notes: Optional[str] = None


# ── Composite Assessment ──


class AnchorSystemAssessment(BaseModel):
    """Complete anchor system condition assessment."""
    model_config = {"from_attributes": True}

    vessel_name: str = Field(..., min_length=1, max_length=200)
    vessel_loa_m: float = Field(..., ge=5, le=60, description="Vessel LOA in meters")
    assessment_date: date = Field(default_factory=date.today)
    assessor: str = Field(default="AYDI Automated Assessment")

    anchor: Optional[AnchorInspection] = None
    chain: Optional[ChainAssessment] = None
    gypsy: Optional[GypsyAssessment] = None
    windlass_motor: Optional[WindlassMotorAssessment] = None
    bow_roller: Optional[BowRollerAssessment] = None
    snubber: Optional[SnubberAssessment] = None
    chain_stopper: Optional[ChainStopperAssessment] = None
    chain_locker: Optional[ChainLockerAssessment] = None

    overall_score: Optional[float] = Field(
        None, ge=0, le=100, description="Overall anchor system score 0-100"
    )
    overall_condition: ComponentCondition = Field(default=ComponentCondition.NOT_ASSESSED)
    critical_findings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    next_inspection_date: Optional[date] = None
    confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED

    def compute_overall_score(self) -> float:
        """Compute overall score from component assessments."""
        component_scores: dict[str, tuple[float, float]] = {}
        score_map = {
            ComponentCondition.EXCELLENT: 95,
            ComponentCondition.GOOD: 80,
            ComponentCondition.FAIR: 60,
            ComponentCondition.WARNING: 40,
            ComponentCondition.CRITICAL: 20,
            ComponentCondition.FAILED: 5,
        }
        weights = {
            "chain": 0.30,
            "anchor": 0.15,
            "windlass_motor": 0.20,
            "gypsy": 0.15,
            "bow_roller": 0.05,
            "snubber": 0.05,
            "chain_stopper": 0.05,
            "chain_locker": 0.05,
        }
        total_weight = 0.0
        weighted_sum = 0.0
        for component_name, weight in weights.items():
            component = getattr(self, component_name, None)
            if component and component.condition != ComponentCondition.NOT_ASSESSED:
                score = score_map.get(component.condition, 50)
                weighted_sum += score * weight
                total_weight += weight

        if total_weight > 0:
            self.overall_score = round(weighted_sum / total_weight, 1)
        else:
            self.overall_score = None
        return self.overall_score or 0.0


class MaintenanceRecommendation(BaseModel):
    """Maintenance recommendation generated by AYDI."""
    model_config = {"from_attributes": True}

    component: str = Field(..., description="Affected component")
    urgency: str = Field(..., description="immediate, soon, planned, routine")
    action_de: str = Field(..., description="Action description in German")
    action_en: str = Field(..., description="Action description in English")
    estimated_cost_eur: Optional[float] = Field(None, ge=0, le=50000)
    estimated_time_hours: Optional[float] = Field(None, ge=0, le=100)
    parts_needed: list[str] = Field(default_factory=list)
    confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED
    reference_section: Optional[str] = Field(
        None, description="Reference to knowledge file section"
    )


class MaintenanceSchedule(BaseModel):
    """Computed maintenance schedule for a vessel's anchor system."""
    model_config = {"from_attributes": True}

    vessel_name: str
    usage_profile: str = Field(
        ..., description="occasional, frequent, bluewater, charter"
    )
    environment: str = Field(
        default="saltwater_temperate",
        description="saltwater_temperate, saltwater_tropical, freshwater"
    )
    last_full_service: Optional[date] = None
    next_service_due: Optional[date] = None
    recommendations: list[MaintenanceRecommendation] = Field(default_factory=list)
    annual_cost_estimate_eur: Optional[float] = Field(None, ge=0, le=20000)
    confidence: ConfidenceLevel = ConfidenceLevel.CALCULATED


class WearPrediction(BaseModel):
    """Wear prediction for a single chain or component."""
    model_config = {"from_attributes": True}

    component: str = Field(..., description="Component being predicted")
    current_wear_percent: float = Field(..., ge=0, le=100)
    wear_rate_per_year: float = Field(..., ge=0, le=20, description="Wear rate in % per year")
    replacement_threshold_percent: float = Field(
        default=12.0, ge=0, le=50, description="Replacement threshold in %"
    )
    estimated_remaining_years: float = Field(..., ge=0, le=30)
    estimated_replacement_date: Optional[date] = None
    estimated_replacement_cost_eur: Optional[float] = Field(None, ge=0, le=30000)
    confidence: ConfidenceLevel = ConfidenceLevel.CALCULATED
    notes: Optional[str] = None
```

### H2 — Fehlerbildkatalog-Modell

```python
"""
AYDI Anchor System Fault Pattern Models
Models for the Fehlerbild-Atlas (fault pattern atlas).
"""

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class FaultSeverity(str, Enum):
    """Fault severity classification."""
    INFO = "info"
    WARNING = "warning"
    CRITICAL = "critical"
    SAFETY = "safety"


class FaultCause(BaseModel):
    """A single potential cause for a fault pattern."""
    model_config = {"from_attributes": True}

    cause_de: str = Field(..., description="Cause description in German")
    cause_en: str = Field(..., description="Cause description in English")
    probability_percent: float = Field(..., ge=0, le=100)
    diagnosis_method: str = Field(..., description="How to confirm this cause")
    confidence: str = Field(default="documented")


class FaultPattern(BaseModel):
    """A fault pattern (Fehlerbild) in the atlas."""
    model_config = {"from_attributes": True}

    fault_id: str = Field(..., pattern=r"^F-\d{2}$", description="Fault pattern ID (e.g. F-01)")
    title_de: str = Field(..., description="Fault title in German")
    title_en: str = Field(..., description="Fault title in English")
    severity: FaultSeverity
    symptoms_de: list[str] = Field(..., min_length=1, description="Observable symptoms in German")
    causes: list[FaultCause] = Field(..., min_length=1)
    immediate_action_de: str = Field(..., description="Immediate action in German")
    resolution_de: str = Field(..., description="Resolution steps in German")
    prevention_de: Optional[str] = Field(None, description="Prevention advice in German")
    related_faults: list[str] = Field(
        default_factory=list, description="Related fault IDs"
    )
    visual_indicators: list[str] = Field(
        default_factory=list, description="Indicators detectable from photos"
    )
    confidence: str = Field(default="documented")


class TroubleshootingNode(BaseModel):
    """A single node in a troubleshooting decision tree."""
    model_config = {"from_attributes": True}

    node_id: str = Field(..., description="Unique node identifier")
    question_de: str = Field(..., description="Decision question in German")
    yes_next: Optional[str] = Field(None, description="Node ID if YES")
    no_next: Optional[str] = Field(None, description="Node ID if NO")
    result_de: Optional[str] = Field(None, description="Final result/action if leaf node")
    confidence: str = Field(default="documented")


class TroubleshootingTree(BaseModel):
    """A complete troubleshooting decision tree."""
    model_config = {"from_attributes": True}

    tree_id: str = Field(..., pattern=r"^T-\d{2}$", description="Tree ID (e.g. T-01)")
    title_de: str = Field(..., description="Tree title in German")
    title_en: str = Field(..., description="Tree title in English")
    entry_symptom_de: str = Field(..., description="Entry symptom in German")
    nodes: list[TroubleshootingNode] = Field(..., min_length=1)
    confidence: str = Field(default="documented")
```

---

## ANHANG I — Ersatzteil-Referenz

### I1 — Häufige Verschleißteile Ankerwinden

| Hersteller | Modell | Teil | Art.-Nr. (Beispiel) | Ca. Preis | Confidence |
|------------|--------|------|---------------------|----------:|------------|
| Lewmar | V1 (6 mm) | Gypsy 6 mm DIN 766 | 66000635 | 180 € | documented |
| Lewmar | V2 (8 mm) | Gypsy 8 mm DIN 766 | 66000637 | 240 € | documented |
| Lewmar | V3 (10 mm) | Gypsy 10 mm DIN 766 | 66000639 | 320 € | documented |
| Lewmar | V1-V3 | Kohlebürsten-Satz | 68000587 | 45 € | documented |
| Lewmar | V1-V3 | Dichtungssatz | 68000xxx | 65 € | estimated |
| Lewmar | V1-V3 | Clutch-Konus | 66000xxx | 95 € | estimated |
| Lofrans | Tigres | Kohlebürsten-Satz | 72050 | 55 € | documented |
| Lofrans | Tigres | Gypsy 10 mm DIN 766 | 72510 | 350 € | documented |
| Lofrans | Tigres | Dichtungssatz | 72080 | 80 € | documented |
| Quick | Prince DP3 | Kohlebürsten-Satz | FVSMP0203 | 50 € | documented |
| Quick | Prince DP3 | Gypsy 10 mm DIN 766 | FVSGY0210 | 290 € | documented |
| Maxwell | RC8-8 | Kohlebürsten-Satz | P100086 | 60 € | documented |
| Maxwell | RC8-8 | Gypsy 10 mm | P100221 | 380 € | documented |

### I2 — Verbrauchsmaterial

| Material | Anwendung | Empfohlene Marken | Ca. Preis | Verbrauch/Jahr | Confidence |
|----------|-----------|-------------------|----------:|---------------|------------|
| Getriebefett (500 g) | Windlass-Getriebe | Lewmar, Shell Gadus | 15–45 € | 200–400 g | documented |
| Zinkspray (400 ml) | Kettenkonservierung | CRC, Würth, Presto | 8–15 € | 1–3 Dosen | documented |
| Lanolin-Spray (400 ml) | Konservierung, Bolzen | Fluid Film, Lanocote | 12–20 € | 1–2 Dosen | documented |
| Tef-Gel (30 g) | Anti-Seize, Schäkel | Tef-Gel original | 18–25 € | 15–30 g | documented |
| PTFE-Spray (400 ml) | Bugrolle (Kunststoff) | WD-40 Specialist | 8–12 € | 1 Dose | documented |
| Sikaflex 291i (300 ml) | Decksdichtung | Sika | 15–22 € | 1 Kartusche/3 Jahre | documented |
| Schrumpfschlauch mit Kleber | Kabel-Isolation | Raychem, TE | 5–15 € | Nach Bedarf | documented |
| Kontaktfett (50 g) | Elektrische Verbindungen | Kontakt Chemie | 8–12 € | 20 g | documented |

---

## ANHANG J — Troubleshooting-Entscheidungsbäume (erweitert)

### J1 — Erweitert: Systematische Windlass-Diagnose

**Phase 1 — Stromversorgung:**
1. Batteriespannung messen (ohne Last): Soll ≥12,6 V (12V) / ≥25,2 V (24V)
2. Hauptschalter → Sicherung → Solenoid: an jedem Punkt Spannung messen
3. Spannungsabfall über Kabelstrecke: max. 3 % ohne Last, max. 10 % unter Last

**Phase 2 — Steuerung:**
1. Fußschalter-Durchgang prüfen (Multimeter, Widerstandsmessung)
2. Fernbedienungs-Kabel prüfen (Durchgang und Isolation)
3. Solenoid: 12V/24V direkt anlegen → klickt = OK, still = defekt
4. Bei elektronischer Steuerung: Platine visuell auf Brandstellen, aufgeblähte Kondensatoren

**Phase 3 — Motor:**
1. Motor direkt an Batterie anschließen (VORSICHT — dreht sofort!)
2. Dreht schnell → Motor OK, Problem in Steuerung/Kabel
3. Dreht langsam → Kohlen, Kollektor, Lager prüfen
4. Dreht nicht → Wicklung messen (Durchgang), Isolationswiderstand

**Phase 4 — Getriebe/Mechanik:**
1. Motor ohne Last drehen → Leerlaufgeräusch normal?
2. Mit Kette: unter leichter Last → Geräusche, Vibrationen?
3. Getriebe öffnen → Zahnrad-Zustand, Lagerspiel, Fettqualität

### J2 — Erweitert: Systematische Ketten-Diagnose

**Phase 1 — Visuell:**
1. Gesamteindruck: Rostgrad, Verzinkung, Verformungen
2. Einzelglieder: ovale Glieder, aufgebogene Glieder, verdrehte Glieder
3. Muscheln/Bewuchs: Umfang, Verteilung

**Phase 2 — Messen:**
1. Durchmesser: Stichprobe alle 5 m → bei Auffälligkeiten verdichten
2. Teilung: 10-Glieder-Abschnitt messen → mit Soll vergleichen
3. Gewicht: 10 m Kette wiegen → mit Soll vergleichen (Materialabtrag)

**Phase 3 — Bewerten:**
1. Worst-Case-Glied bestimmt die Gesamtbewertung
2. Verschleißverteilung analysieren → Ursache ermitteln
3. Prognose erstellen: Restlebensdauer berechnen

---

## ANHANG K — Kostenkalkulation Wartung

### K1 — Typische Wartungskosten nach Szenario

| Szenario | Material | Arbeitszeit (DIY) | Arbeitszeit (Werft @ 85 €/h) | Gesamt DIY | Gesamt Werft | Confidence |
|----------|---------|-------------------|------------------------------|----------:|-------------:|------------|
| Jahreswartung Standard (10-m-Yacht) | 80–150 € | 4–6 h | 4–6 h (340–510 €) | 80–150 € | 420–660 € | estimated |
| Jahreswartung Standard (14-m-Yacht) | 120–250 € | 6–10 h | 6–10 h (510–850 €) | 120–250 € | 630–1.100 € | estimated |
| Kettentausch 60 m × 10 mm | 600–900 € | 2–3 h | 2–3 h (170–255 €) | 600–900 € | 770–1.155 € | documented |
| Gypsy-Tausch | 200–500 € | 1–2 h | 1–2 h (85–170 €) | 200–500 € | 285–670 € | documented |
| Windlass-Revision | 150–500 € | 4–8 h | 4–8 h (340–680 €) | 150–500 € | 490–1.180 € | estimated |
| Windlass-Neukauf + Einbau | 1.500–4.000 € | — | 8–16 h (680–1.360 €) | — | 2.180–5.360 € | estimated |
| Kohlebürsten-Tausch | 30–80 € | 1–2 h | 1–2 h (85–170 €) | 30–80 € | 115–250 € | documented |
| Snubber-Neukauf (16 mm × 12 m) | 40–80 € | — | — | 40–80 € | 40–80 € | documented |
| Bugrolle-Tausch | 150–400 € | 2–3 h | 2–3 h (170–255 €) | 150–400 € | 320–655 € | estimated |

### K2 — 10-Jahres-Gesamtkosten Ankersystem (Szenarien)

| Szenario | Gelegenheitssegler | Vielsegler | Blauwasser | Confidence |
|----------|-------------------|------------|------------|------------|
| Jährliche Wartung (Material) | 100 €/a = 1.000 € | 200 €/a = 2.000 € | 350 €/a = 3.500 € | estimated |
| 1× Kettentausch | 800 € | 800 € | 1.600 € (2×) | estimated |
| 1× Gypsy-Tausch | 0 € (nicht nötig) | 350 € | 700 € (2×) | estimated |
| 1× Windlass-Revision | 0 € | 400 € | 800 € (2×) | estimated |
| Snubber (Austausch) | 100 € (2×) | 200 € (3×) | 400 € (5×) | estimated |
| Verbrauchsmaterial | 500 € | 1.000 € | 2.000 € | estimated |
| **Gesamt 10 Jahre** | **~2.400 €** | **~4.750 €** | **~9.000 €** | estimated |

---

## ANHANG L — Fotodokumentation Verschleißbilder

### L1 — Referenzbilder für AYDI Visual Pipeline

Die folgenden Beschreibungen dienen als Referenz für die AYDI Visual Pipeline (Pipeline B) zur Erkennung von Verschleißbildern auf Fotos:

| Referenz-ID | Motiv | Erkennungsmerkmale | Bewertung | Confidence Level |
|-------------|-------|-------------------|-----------|-----------------|
| VB-01 | Kette neuwertig | Glänzend silber-grau, gleichmäßige Oberfläche, scharfe Gliedkanten | EXCELLENT | visual_high |
| VB-02 | Kette leicht korrodiert | Matte Oberfläche, vereinzelte braune Flecken, Grundstruktur intakt | GOOD | visual_high |
| VB-03 | Kette mittel korrodiert | Großflächig braun, Zinkinseln sichtbar, Glieder intakt | WARNING | visual_medium |
| VB-04 | Kette stark korrodiert | Durchgehend rostbraun, Oberflächenrauhigkeit, Materialabtrag erkennbar | CRITICAL | visual_high |
| VB-05 | Kette mit Bewuchs | Muscheln, Seepocken auf Gliedern, teilweise verkrustet | FAIR (nach Reinigung bewertbar) | visual_high |
| VB-06 | Gypsy neuwertig | Scharfkantige Zähne, definierte Taschen, metallisch glänzend | EXCELLENT | visual_high |
| VB-07 | Gypsy verschlissen | Abgerundete Zähne, flache Taschen, Abriebspuren | WARNING/CRITICAL | visual_medium |
| VB-08 | Snubber mit Chafe | Aufgeraute Stelle, Fasern abstehend, Mantel beschädigt | WARNING | visual_high |
| VB-09 | Snubber Kern sichtbar | Mantel durchgescheuert, innere Fasern/Kern freigelegt | CRITICAL | visual_high |
| VB-10 | Schweißnaht-Riss | Dunkle Linie in Schweißnaht, Rost in Riss | CRITICAL | visual_high |
| VB-11 | Bugrolle korrodiert | Weiße Ausblühungen (Alu) oder Rostfahnen, blockierte Rolle | WARNING | visual_high |
| VB-12 | Galvanische Korrosion | Grüne/weiße Krusten an Metallkontaktstelle | WARNING/CRITICAL | visual_high |

---

## ANHANG M — Schmiermittel-Kompatibilitätsmatrix

### M1 — Detaillierte Verträglichkeitstabelle

| Fettbasis (bestehend ↓ / neu →) | Lithium | Li-Komplex | Kalzium | Ca-Komplex | Polyurea | Aluminium-Komplex | Silikon | Confidence |
|----------------------------------|---------|------------|---------|------------|----------|-------------------|---------|------------|
| **Lithium** | ✓ | ○ | ✗ | ✗ | ✗ | ○ | ✗ | documented |
| **Li-Komplex** | ○ | ✓ | ✗ | ✗ | ✗ | ○ | ✗ | documented |
| **Kalzium** | ✗ | ✗ | ✓ | ○ | ✗ | ✗ | ✗ | documented |
| **Ca-Komplex** | ✗ | ✗ | ○ | ✓ | ✗ | ✗ | ✗ | documented |
| **Polyurea** | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ | documented |
| **Aluminium-Komplex** | ○ | ○ | ✗ | ✗ | ✗ | ✓ | ✗ | documented |
| **Silikon** | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | documented |

✓ = verträglich, ○ = bedingt verträglich (möglichst vermeiden), ✗ = NICHT mischen

---

## ANHANG N — Zusätzliche Fallstudien

### N1 — Fallstudie: Notfall-Kettenfall Dufour 430 (2023)

**Ausgangslage:** Dufour 430, Kroatische Küste. Beim Ankerfieren blockiert die Kette im Kettenkasten. Eigner gibt Vollgas auf Windlass "Ab" → Kette reißt Führungsrohr ab → gesamte 60 m Kette fallen unkontrolliert in den Kettenkasten → massiver Schlag.

**Schaden:** Kettenkasten-Wandung gerissen, Kette hat sich verknäuelt, Windlass-Gypsy beschädigt (Zahn abgebrochen).

**Ursache:** Kette war beim letzten Einlaufen verdreht und hat sich beim Fieren verklemmt. Eigner hat Windlass forciert statt Problem zu untersuchen.

**Lehre:** (1) Bei Kettenstau SOFORT stoppen, nicht forcieren. (2) Von Hand Kette im Kasten ordnen. (3) Regelmäßig Kettenkasten inspizieren.

**Kosten:** Kettenkasten-Reparatur: 2.800 €. Neuer Gypsy: 380 €. Arbeitszeit: ca. 12 h × 85 € = 1.020 €. Gesamt: ca. 4.200 €.

### N2 — Fallstudie: Saisonstart-Problem nach Winterlager — Oyster 565 (2024)

**Ausgangslage:** Oyster 565 nach 6 Monaten Winterlager (Mallorca, an Land). Maxwell VWC 3500 Windlass. Eigner will zum Saisonstart Ankersystem testen.

**Symptom:** Windlass dreht 2 Sekunden, dann Sicherung (200 A) brennt durch.

**Diagnose:**
1. Neue Sicherung → wieder durch nach 2 Sekunden → Kurzschluss
2. Motor abklemmen → Sicherung hält → Problem im Motor
3. Motor öffnen: Kondenswasser im Motorgehäuse über Winter → Korrosion an Kollektor-Lamellen → Kurzschluss zwischen Lamellen

**Behebung:**
1. Motor gereinigt, Kollektor geschliffen
2. Isolationswiderstand nach Trocknung: 5,2 MΩ → OK
3. Neue Kohlebürsten (waren OK, aber prophylaktisch getauscht)
4. Decksdurchführung neu abgedichtet (war Eintrittsweg für Kondenswasser)

**Kosten:** Material: ca. 120 €. Arbeitszeit: ca. 5 h × 95 € = 475 €. Gesamt: ca. 595 €.

**Prävention:** Bei Winterlager: Motor trocken halten, Decksdurchführung prüfen, ggf. Silikagel-Beutel in Motorgehäuse.

---

## ANHANG O — Eigner-Erfahrungen und Feldberichte

### O1 — Sammlung anonymisierter Eigner-Berichte

**Bericht O1-1: "Gypsy nach 3 Saisons verschlissen" (Eigner, Bavaria 46, 2022)**
> "Wir hatten nach nur 3 Saisons Gypsy-Probleme. Die Kette sprang beim Einholen. Ursache: Wir hatten billige Kette aus dem Internet bestellt (angeblich DIN 766). Die Teilung stimmte nicht — der Gypsy war innerhalb von 3 Saisons hinüber. Lehre: Nur Markenkette kaufen und IMMER die Teilung nachmessen."
**AYDI-Einschätzung:** Typischer Fall von Ketten-Gypsy-Inkompatibilität. Confidence: documented (verifizierter Eignerbericht).

**Bericht O1-2: "Windlass im Sturm gerettet" (Eignerin, HR 40, 2023)**
> "Sardinien, 45-kn-Sturm in der Nacht. Snubber hat sich gelöst (Karabiner aufgegangen). Gesamte Last auf Windlass. Windlass hat 4 Stunden gehalten, aber: Clutch danach hinüber. 800 € Reparatur. Seitdem: IMMER Kettenstopper + Snubber, und der Snubber-Karabiner wird mit Kabelbinder gesichert."
**AYDI-Einschätzung:** Unterstreicht die Wichtigkeit von Kettenstopper + Snubber-Sicherung. Confidence: documented.

**Bericht O1-3: "Kettenmessung hat Reise gerettet" (Eigner, Hallberg-Rassy 48, 2024)**
> "Vor unserer Atlantiküberquerung habe ich zum ersten Mal die Kette systematisch gemessen. Ergebnis: die ersten 15 m waren bei 8,7 mm (10-mm-Kette), also 13 % — ÜBER dem Grenzwert. Wir haben die Kette getauscht und im Nachhinein war das lebensrettend. Auf den Kanaren hatten wir 50-kn-Böen."
**AYDI-Einschätzung:** Paradebeispiel für den Wert regelmäßiger Kettenmessung. Confidence: documented.

---

## ANHANG P — Elektrische Fehlersuche Ankerwinde

### P1 — Schaltplan-Grundprinzip (DC-Windlass)

```
[Batterie 12V/24V]
    │
    ├── [Hauptschalter]
    │       │
    │       ├── [Sicherung (125–300 A)]
    │       │       │
    │       │       ├── [Solenoid AUF]──────┐
    │       │       │                        │
    │       │       ├── [Solenoid AB]──┐     │
    │       │       │                  │     │
    │       │       │              [Motor]   │
    │       │       │                  │     │
    │       │       └──────────────────┘     │
    │       │                                │
    │       └────────────────────────────────┘
    │
    └── [Steuerstromkreis]
            │
            ├── [Fußschalter AUF]──→ [Solenoid AUF Spule]
            │
            └── [Fußschalter AB]──→ [Solenoid AB Spule]
```

### P2 — Messwerte-Referenz

| Messpunkt | Soll-Wert (12V) | Soll-Wert (24V) | Grenzwert | Confidence |
|-----------|-----------------|-----------------|-----------|------------|
| Batterie (Ruhe) | 12,6–12,8 V | 25,2–25,6 V | <12,0 / <24,0 V | measured |
| Batterie (unter Last) | >11,5 V | >23,0 V | <11,0 / <22,0 V | measured |
| Am Motor (unter Last) | >10,8 V | >21,5 V | <10,0 / <20,0 V | measured |
| Spannungsabfall Kabel | <1,0 V | <2,0 V | >1,5 V / >3,0 V | measured |
| Strom (kein Last) | 20–40 A | 10–20 A | >60 A / >30 A | measured |
| Strom (normale Last) | 60–120 A | 30–60 A | >150 A / >75 A | measured |
| Strom (Volllast) | 100–180 A | 50–90 A | >200 A / >100 A | measured |
| Isolationswiderstand Motor | >1 MΩ | >1 MΩ | <0,5 MΩ | measured |

### P3 — Kabelquerschnitte für Ankerwinden

| Windlass-Leistung | Strom (12V) | Kabel max. 3 m | Kabel max. 5 m | Kabel max. 8 m | Confidence |
|-------------------|------------|----------------|----------------|----------------|------------|
| 500 W | ~50 A | 16 mm² | 25 mm² | 35 mm² | documented |
| 700 W | ~70 A | 25 mm² | 35 mm² | 50 mm² | documented |
| 1000 W | ~100 A | 35 mm² | 50 mm² | 70 mm² | documented |
| 1500 W | ~150 A | 50 mm² | 70 mm² | 95 mm² | documented |
| 2000 W | ~200 A | 70 mm² | 95 mm² | 120 mm² | documented |

**Hinweis:** Werte für 12V. Bei 24V halbiert sich der Strom → eine Querschnittsstufe kleiner möglich.

---

## ANHANG Q — Notfall-Reparaturverfahren

### Q1 — Notfall-Reparaturen auf See

| Situation | Notlösung | Material | Haltbarkeit | Confidence |
|-----------|-----------|----------|-------------|------------|
| Kettenstopper defekt | Kette mit Leinenstopper (Prusik-Knoten) auf Klampe belegen | 10 mm Leine, Klampe | Stunden–Tage | documented |
| Windlass tot, Kette einholen | Kette über Winsch oder mit Leinenstopper-Methode Meter für Meter einholen | Winsch, Leine | Dauerlösung | documented |
| Snubber gerissen | Festmacherleine als Not-Snubber, Scheuerschutz aus Schlauch | Festmacher, Schlauch | Stunden–Tage | documented |
| Schäkel gebrochen | Ersatzschäkel oder Bolzen mit Draht sichern | Ersatzschäkel, Edelstahldraht | Bis zur nächsten Marina | estimated |
| Bugrolle blockiert | Kette über Klampe/Poller am Bug führen, Rolle umgehen | Lappen als Scheuerschutz | Bis Reparatur möglich | estimated |
| Kette gerissen | Not-Kettenanschluss mit Leine (Ankerstich um letztes Glied) + Schäkel | Leine, Schäkel | Temporär, bei leichtem Wetter | estimated |

### Q2 — Werkzeug-Minimum für Notfälle unterwegs

| Werkzeug | Anwendung | Confidence |
|----------|-----------|------------|
| Bolzenschneider (10 mm) | Beschädigtes Kettenglied entfernen | documented |
| 2× Ersatzschäkel (passende Größe) | Kettenreparatur | documented |
| Edelstahl-Draht 1,5 mm | Schäkel-Sicherung, provisorische Reparatur | documented |
| Universalschlüssel (verstellbar) | Schrauben, Muttern | documented |
| Multimeter (kompakt) | Elektrische Fehlersuche | documented |
| Ersatz-Sicherung Windlass | Windlass-Sicherungstausch | documented |
| Isolierband + Schrumpfschlauch | Kabelreparatur | documented |
| 10 m Ersatzleine (12 mm Nylon) | Not-Snubber, Leinenstopper | documented |

---

## ANHANG R — Zukunftstrends Wartungstechnologie

### R1 — Aktuelle und kommende Technologien

| Technologie | Status (2026) | Potenzial für Wartung | Verfügbarkeit | Confidence |
|-------------|---------------|----------------------|---------------|------------|
| IoT-Sensoren an Windlass | Verfügbar (Quick, Lewmar neueste Generation) | Betriebsstunden-Zähler, Strom-Monitoring, automatische Wartungserinnerung | Neubauten / Nachrüstung | documented |
| Kettenzug-Sensor | Verfügbar (Mantus Marine, Bridle Analytics) | Echtzeit-Ankerbelastung, Alarm bei Draggen | Nachrüstung möglich | documented |
| KI-basierte Fotobewertung (AYDI) | In Entwicklung | Automatische Verschleißerkennung aus Smartphone-Fotos | AYDI Platform | estimated |
| Ultraschall-Dickenmessung Kette | Prototyp | Präzise Durchmessermessung ohne Auslegen | Noch nicht marktreif | estimated |
| Drohnen-Inspektion Unterwasser | Verfügbar (kommerziell) | Anker-Sitz-Prüfung, Kettenverlegung am Grund | Dienstleister | documented |
| Predictive Maintenance (ML) | In Entwicklung | Vorhersage von Ausfällen basierend auf Betriebsdaten | AYDI Platform | estimated |
| Self-healing Beschichtungen | Forschung | Selbstreparierende Verzinkung/Beschichtung | 5–10 Jahre | estimated |
| Faseroptische Belastungsmessung | Verfügbar (kommerziell) | Dauerlast-Monitoring an Kette und Snubber | Superyacht-Segment | documented |

### R2 — AYDI-Entwicklungsplan Ankersystem-Analyse

| Feature | Status | Ziel | Confidence |
|---------|--------|------|------------|
| Foto-basierte Kettenzustandsbewertung | In Entwicklung | Automatische Rostgrad-/Verzinkungsbewertung aus Fotos | estimated |
| Gypsy-Verschleißerkennung aus Foto | Geplant | Zahnprofile automatisch klassifizieren | estimated |
| Wartungsplan-Generator | In Entwicklung | Personalisierte Wartungspläne basierend auf Bootsprofil | calculated |
| Verschleißprognose | In Entwicklung | Restlebensdauer-Berechnung aus Messdaten | calculated |
| Ersatzteil-Finder | Geplant | Automatische Ersatzteil-Zuordnung nach Windlass-Modell | documented |
| Service-Report-Analyse | In Entwicklung | NLP-Extraktion von Wartungsinformationen aus Texten | documented |

### R3 — Hydraulische Ankerwinden — Besonderheiten

Hydraulische Ankerwinden kommen bei größeren Yachten (>18 m) zum Einsatz. Ihre Wartung unterscheidet sich grundlegend von elektrischen Systemen:

**Vorteile hydraulischer Systeme:**
- Deutlich höhere Dauerleistung (kein thermisches Limit des Motors)
- Weniger Verschleißteile (keine Kohlebürsten, kein Kollektor)
- Stufenlose Geschwindigkeitsregelung über Hydraulikventil
- Weniger Kabelprobleme (keine hohen Ströme im Bugbereich)

**Wartungsanforderungen:**

| Wartungsarbeit | Intervall | Prüfmethode | Confidence |
|---------------|-----------|-------------|------------|
| Hydrauliköl-Stand prüfen | Monatlich | Schauglas/Peilstab | documented |
| Hydrauliköl wechseln | Alle 1.000 h oder 2 Jahre | Altes Öl ablassen, Filter wechseln, neu befüllen | documented |
| Hydraulikleitungen prüfen | Halbjährlich | Sichtprüfung auf Leckage, Scheuerstellen, Biegeknicke | documented |
| Hydraulikfilter wechseln | Alle 500 h oder jährlich | Filter tauschen, auf Metallabrieb prüfen | documented |
| Hydraulikpumpe prüfen | Jährlich | Förderdruck messen, Leckage prüfen | measured |
| Hydraulikzylinder prüfen (falls vorhanden) | Jährlich | Kolbenstange auf Riefen, Dichtungen auf Leckage | documented |
| Hydraulikschläuche tauschen | Alle 5–7 Jahre | Alterung der Gummi-/Textilschichten | documented |

**Typische Hydrauliköle:**
- ISO VG 32 oder VG 46 (je nach Herstellerangabe)
- Biodegradable Hydrauliköl (z.B. Panolin HLP Synth) bei umweltbewussten Eignern
- NIEMALS verschiedene Öltypen mischen

**Häufige Hydraulik-Fehler:**

| Fehler | Symptom | Ursache | Behebung | Confidence |
|--------|---------|---------|----------|------------|
| Windlass zu langsam | Kette kommt langsam | Ölstand niedrig, Pumpe verschlissen, Ventil nicht voll geöffnet | Ölstand prüfen, Pumpe prüfen | documented |
| Windlass ruckt | Ungleichmäßiger Lauf | Luft im System, Ventilblockade | Entlüften, Ventil reinigen | documented |
| Leckage am Windlass | Ölspur unter Windlass | Wellendichtring verschlissen | Dichtring tauschen | documented |
| Leckage an Leitung | Öl an Schlauch/Fitting | Fitting lose, Schlauch porös | Nachziehen oder Schlauch tauschen | documented |
| Kein Druck | Windlass reagiert nicht | Pumpe defekt, Sicherheitsventil offen | Pumpe prüfen, Ventil prüfen | documented |

### R4 — Manuelle Ankerwinden — Wartungsbesonderheiten

Manuelle Ankerwinden (Handwinden) werden bei kleineren Yachten (6–10 m) und als Backup-Systeme eingesetzt:

**Typen:**
- **Vertikale Handwinde:** Kurbelgetriebe mit Gypsy, typisch 6–8 mm Kette
- **Horizontale Handwinde:** Ähnlich Winsch, Kurbelbetrieb
- **Ratschen-Winsch:** Einfachste Form, Hebel mit Ratsche

**Wartung manueller Winden:**

| Wartungsarbeit | Intervall | Prüfpunkt | Confidence |
|---------------|-----------|-----------|------------|
| Getriebefett prüfen/erneuern | Jährlich | Gleiches Fett wie bei Elektro-Windlass | documented |
| Freilauf-Mechanismus (Rücklaufsperre) | Halbjährlich | Sperrklinke greift sauber, Feder intakt | documented |
| Kurbellager | Jährlich | Kein übermäßiges Spiel, geschmiert | documented |
| Gypsy | Jährlich | Wie bei elektrischem Windlass | documented |
| Korrosion Gehäuse | Jährlich | Besonders bei Aluminiumgehäuse | documented |
| Kurbelaufnahme | Halbjährlich | Vierkant nicht ausgeschlagen, Sicherung intakt | documented |

**Typische Probleme:**

| Problem | Ursache | Behebung | Confidence |
|---------|---------|----------|------------|
| Kurbel dreht durch | Rücklaufsperre defekt (Feder gebrochen, Klinke verschlissen) | Sperrklinke + Feder tauschen | documented |
| Kurbel schwergängig | Getriebe trocken/korrodiert | Getriebe öffnen, reinigen, neu fetten | documented |
| Gypsy rutscht | Clutch-Schraube lose | Clutch nachziehen | documented |
| Kette klemmt | Wie bei elektrischem Windlass (Gypsy/Kette-Kompatibilität) | Gypsy/Kette prüfen | documented |

**Vorteil für Notfälle:** Manuelle Winden funktionieren auch bei totalem Stromausfall. Empfehlung für Langfahrtyachten: Auch bei elektrischem Windlass sollte eine Winschkurbel als Notfall-Kurbel für die Ankerwinde vorhanden sein (viele Windlass-Modelle haben einen Kurbelansatz).

### R5 — Ankerüberwachungssysteme — Wartung elektronischer Komponenten

Moderne Ankerüberwachung umfasst elektronische Systeme, die ebenfalls gewartet werden müssen:

**Kettenzähler-Systeme:**

| Hersteller | System | Sensortyp | Wartungsintervall | Typische Probleme | Confidence |
|------------|--------|-----------|-------------------|-------------------|------------|
| Quick | Quick Count | Reed-Sensor (magnetisch) | Halbjährlich | Magnet-Abstand, Salzablagerung | documented |
| Lewmar | Chain Counter | Hall-Sensor | Halbjährlich | Sensor-Ausrichtung nach Gypsy-Tausch | documented |
| Muir | Chain Counter | Optisch | Vierteljährlich | Verschmutzung der Optik | documented |
| Maxwell | Rope/Chain Counter | Reed-Sensor | Halbjährlich | Magnet-Verlust, Korrosion | documented |
| Yacht Devices | YDCC-04 | NMEA 2000 | Jährlich | Firmware-Update, Kalibrierung | documented |

**Ankeralarm-Systeme (GPS-basiert):**

| System | Plattform | Wartung | Typische Probleme | Confidence |
|--------|-----------|---------|-------------------|------------|
| Anchor Alarm (App) | iOS/Android | App-Updates installieren | GPS-Genauigkeit variiert, Akku-Verbrauch | documented |
| Drag Queen (App) | iOS/Android | App-Updates | Falschalarme bei schlechtem GPS | documented |
| Vesper Marine Watchmate | Standalone AIS | Firmware-Updates, Antenne prüfen | Selten, robust | documented |
| B&G/Simrad (integriert) | Plotter-System | Plotter-Software aktuell halten | GPS-Drift in engen Buchten | documented |

**Wartungstipps für elektronische Ankerüberwachung:**
1. GPS-Antenne reinigen (Salzablagerungen reduzieren Empfangsqualität)
2. Firmware/App-Updates zeitnah installieren (Fehlerkorrekturen)
3. Kettenzähler nach jedem Gypsy-Tausch oder Kettenersatz neu kalibrieren
4. Sensor-Abstand zum Gypsy prüfen (typisch 3–5 mm, Herstellerangabe beachten)
5. Kabelverbindungen auf Korrosion prüfen (besonders NMEA 2000 Stecker)
6. Backup-System vorhalten: mindestens manuell markierte Kette als Fallback
7. Ankeralarm-App VOR dem Ankern testen (nicht erst bei Sturm feststellen, dass die App nicht funktioniert)

### R6 — Materialtechnische Entwicklungen

| Material/Technologie | Beschreibung | Auswirkung auf Wartung | Zeithorizont | Confidence |
|---------------------|-------------|----------------------|-------------|------------|
| Duplex-Edelstahl-Ketten | Höhere Festigkeit bei gleicher Korrosionsbeständigkeit | Weniger Verschleiß, längere Intervalle | Verfügbar (Superyacht) | documented |
| Zink-Aluminium-Beschichtung (Galfan) | 2–3× längere Korrosionsschutz-Dauer als Feuerverzinkung | Deutlich längere Kettenlebensdauer | Verfügbar | documented |
| Kunststoff-ummantelte Ketten | PVC/PA-Ummantelung schützt Verzinkung und GFK | Weniger Kratzer an Bugrolle und Deck, aber Gypsy-Inkompatibilität | Verfügbar (eingeschränkt) | documented |
| Keramik-beschichtete Gypsy-Zähne | Hartkeramik-Beschichtung reduziert Abrieb um 60–80 % | Gypsy-Lebensdauer verdreifacht | Prototyp | estimated |
| HMPE/Dyneema-Kette | Hochfestes Fasertauwerk als Kettenersatz | Kein Rost, 80 % Gewichtsersparnis, aber kein Eigengewicht zum Setzen | Verfügbar (Regatta) | documented |
| Graphen-verstärkte Beschichtungen | Ultradünne, extrem harte Oberflächenbeschichtung | Korrosionsschutz bei Nano-Dicke | Forschung (5–10 Jahre) | estimated |

### R4 — Digitale Wartungsdokumentation

**Aktuelle Best Practice:**
- Papier-Logbuch: traditionell, aber nicht durchsuchbar, kann verloren gehen
- Excel/Spreadsheet: besser, aber keine Fotodokumentation, kein Versand an Surveyor
- Yacht-Management-Apps (z.B. Boat Beacon, Yacht Organiser): strukturierte Eingabe, Erinnerungen
- AYDI Platform: integrierte Zustandsbewertung + Dokumentation + Prognose

**Vorteile digitaler Dokumentation:**
1. **Trendsichtbarkeit:** Kettenverschleiß über Jahre grafisch darstellen
2. **Automatische Erinnerungen:** Wartungsintervalle werden nicht vergessen
3. **Fotodokumentation:** Vergleich Vorher/Nachher, Zustand bei Kauf dokumentiert
4. **Surveyor-Übergabe:** Vollständige Historie bei Pre-Purchase Survey
5. **Wiederverkaufswert:** Lückenlose Wartungshistorie = Vertrauen beim Käufer
6. **Versicherungsfall:** Nachweis ordnungsgemäßer Wartung

### R6 — Winterlager-Spezifische Wartungshinweise

#### R6.1 Winterlager an Land (Trocken)

**Vorteile:** Kein Unterwasser-Bewuchs, keine Elektrolyse, leichterer Zugang zu Unterwasserteilen.

| Maßnahme | Begründung | Durchführung | Confidence |
|----------|-----------|-------------|------------|
| Kette komplett entfernen und separat lagern | Gewicht aus Vorschiff → besserer Trimm auf Böcken, Kette trocknet vollständig | Kette in belüftetem Container/auf Palette | documented |
| Windlass-Motor trocken halten | Kondenswasser → Wicklungsschaden | Neoprenhülle oder Silica-Gel in Motorgehäuse | documented |
| Bugrolle-Bolzen fetten | Frostschutz, Festfressen verhindern | Bolzen herausziehen, fetten, wieder einsetzen | documented |
| Kettenkasten offen lassen | Belüftung → kein Schimmel | Deckel auflegen, nicht verschließen | documented |
| Ankerklüse verschließen | Regen-/Schneewasser im Vorschiff verhindern | Neoprenkappe oder Kunststoffstopfen | documented |
| Windlass-Sicherung ziehen | Verhinderung unbeabsichtigter Aktivierung | Sicherung kennzeichnen und sicher aufbewahren | documented |

#### R6.2 Winterlager im Wasser

**Besonderheiten:**

| Maßnahme | Begründung | Durchführung | Confidence |
|----------|-----------|-------------|------------|
| Kette regelmäßig bewegen (monatlich) | Kette verklebt/verbackt nicht im Kettenkasten | 10 m fieren und wieder einholen | estimated |
| Windlass-Motor vor Kondenswasser schützen | Winterliche Temperaturschwankungen → Kondensation | Heizelement oder Silica-Gel | documented |
| Kettenkasten-Drainage prüfen | Regenwasser muss ablaufen können | Vor dem Winter Drainage reinigen | documented |
| Galvanischen Isolator prüfen (bei Landstrom) | Winter-Landstrom → galvanische Ströme → Korrosion an Kette | Isolator messen oder erneuern | documented |
| Frostschutz im Kettenkasten | Stehendes Wasser gefriert → Rissbildung im GFK | Drainage sicherstellen, ggf. Wasser absaugen | documented |

#### R6.3 Inbetriebnahme nach Winterlager — Checkliste

| Schritt | Aktion | Prüfpunkt | Confidence |
|---------|--------|-----------|------------|
| 1 | Sicherung einsetzen | Korrekter Wert, kein Korrosionsschaden | documented |
| 2 | Hauptschalter EIN | Spannung am Panel prüfen | measured |
| 3 | Windlass-Motor Probelauf (kurz, ohne Last) | Drehrichtung, Geräusch, Geschwindigkeit | documented |
| 4 | Kette einlegen (wenn separat gelagert) | Richtige Orientierung, Markierungen stimmen | documented |
| 5 | Funktionstest mit Kette (ohne Anker) | Ein-/Ausfahrt, Clutch, Kettenstopper | documented |
| 6 | Anker montieren | Schäkel korrekt gesichert, Wirbel gängig | documented |
| 7 | Erster Ankertest bei gutem Wetter | Setzen, Halten, Aufnehmen, alles beobachten | documented |

### R7 — Wartung bei Langfahrt — Ersatzteil-Kit

Für Langfahrt-/Blauwasser-Yachten empfiehlt sich folgendes Ersatzteil-Kit:

| Ersatzteil | Menge | Priorität | Gewicht | Ca. Preis | Confidence |
|-----------|-------|-----------|---------|----------:|------------|
| Kohlebürsten-Satz (passend) | 2 Sätze | Hoch | 50 g | 60–160 € | documented |
| Windlass-Sicherung (passend) | 3 Stück | Hoch | 100 g | 15–30 € | documented |
| Dichtungssatz (passend) | 1 Satz | Mittel | 100 g | 50–150 € | documented |
| Getriebefett (500 g Tube) | 1 Stück | Hoch | 500 g | 15–45 € | documented |
| Schäkel (2× Größe Kette-Anker) | 4 Stück | Hoch | 300 g | 40–80 € | documented |
| Wirbel (passend) | 1 Stück | Mittel | 200 g | 30–80 € | documented |
| Sicherungssplinte (div. Größen) | 10 Stück | Hoch | 50 g | 5–10 € | documented |
| Sicherungsdraht 316L 1,2 mm | 5 m | Hoch | 100 g | 5–10 € | documented |
| Tef-Gel (30 g Tube) | 1 Stück | Mittel | 30 g | 18–25 € | documented |
| Zinkspray (400 ml) | 2 Dosen | Mittel | 800 g | 16–30 € | documented |
| Lanolin-Spray (400 ml) | 1 Dose | Mittel | 400 g | 12–20 € | documented |
| Schrumpfschlauch mit Kleber (div.) | 10 Stück | Mittel | 50 g | 10–15 € | documented |
| Kabelschuhe (passend für Motor) | 4 Stück | Hoch | 50 g | 5–10 € | documented |
| Ersatz-Fußschalter-Membran | 1 Stück | Niedrig | 20 g | 15–30 € | estimated |
| Nylon-Snubber (als Reserve) | 1 Stück (12 m) | Hoch | 3 kg | 40–80 € | documented |
| Bolzenschneider (10 mm) | 1 Stück | Hoch | 1,5 kg | 30–60 € | documented |
| **Gesamt** | | | **~7 kg** | **~370–830 €** | |

**Empfehlung:** Alle Teile in einer wasserdichten Box im Vorschiff lagern, Inhaltsliste beilegen, Haltbarkeitsdaten notieren (besonders bei Fett und Spray).

---

## ANHANG S — Erweiterte Wartungstabellen

### S1 — Drehmomente für Ankersystem-Befestigungen

| Verbindung | Schraubengröße | Material | Drehmoment (Nm) | Sicherung | Confidence |
|-----------|---------------|----------|---------------:|-----------|------------|
| Bugrolle → Deck | M8 Edelstahl | 316L in GFK | 18–22 | Loctite 243 | documented |
| Bugrolle → Deck | M10 Edelstahl | 316L in GFK | 30–38 | Loctite 243 | documented |
| Bugrolle → Deck | M12 Edelstahl | 316L in GFK | 50–65 | Loctite 243 | documented |
| Windlass → Deck | M8 Edelstahl | 316L in GFK + Backing Plate | 20–25 | Loctite 243 + Sicherungsscheibe | documented |
| Windlass → Deck | M10 Edelstahl | 316L in GFK + Backing Plate | 35–42 | Loctite 243 + Sicherungsscheibe | documented |
| Windlass → Deck | M12 Edelstahl | 316L in GFK + Backing Plate | 55–70 | Loctite 243 + Sicherungsscheibe | documented |
| Kettenstopper → Deck | M8 Edelstahl | 316L in GFK | 18–22 | Loctite 243 | documented |
| Kettenstopper → Deck | M10 Edelstahl | 316L in GFK | 30–38 | Loctite 243 | documented |
| Gypsy-Sicherungsmutter | Modellabhängig | Bronze/Edelstahl | Herstellerangabe | Sicherungsblech | documented |
| Kabelschuhe (Motor) | M6/M8 | Kupfer/Messing | 5–8 / 10–15 | Federscheibe | documented |
| Solenoid-Anschlüsse | M5/M6 | Messing | 3–5 / 5–8 | Federscheibe | documented |

**WICHTIG:** Bei GFK-Sandwich-Decks: Drehmoment um 20 % reduzieren! GFK-Kern (z.B. Balsa, PVC-Schaum) kann bei Überdrehung kollabieren → irreversible Schwächung.

### S2 — Schäkel-Dimensionierungstabelle für Ankersysteme

| Kettengröße | Schäkel-Typ | Schäkel-Nennweite | WLL (kg) | MBL (kg) | Bolzen-Ø (mm) | Confidence |
|-------------|-------------|-------------------|---------|---------|---------------|------------|
| 6 mm | Gerade D | 6 mm | 200 | 800 | 7 | documented |
| 8 mm | Gerade D | 8 mm | 350 | 1.400 | 9,5 | documented |
| 8 mm | Omega | 8 mm | 400 | 1.600 | 10 | documented |
| 10 mm | Gerade D | 10 mm | 500 | 2.000 | 12 | documented |
| 10 mm | Omega | 10 mm | 600 | 2.400 | 13 | documented |
| 12 mm | Gerade D | 12 mm | 750 | 3.000 | 14 | documented |
| 12 mm | Omega | 12 mm | 850 | 3.400 | 16 | documented |
| 13 mm | Gerade D | 13 mm | 900 | 3.600 | 16 | documented |
| 14 mm | Gerade D | 14 mm | 1.000 | 4.000 | 17 | documented |
| 16 mm | Gerade D | 16 mm | 1.300 | 5.200 | 19 | documented |

**Schäkel-Prüfpunkte bei Wartung:**
1. Bolzen-Durchmesser messen: min. 90 % des Neuwerts
2. Bügel-Öffnung messen: max. 110 % des Neuwerts (Aufweitung)
3. Gewindegängigkeit: Bolzen muss sich leicht ein-/ausdrehen lassen
4. Sicherungsdraht oder Splint: vorhanden und intakt
5. Korrosion: besonders am Bolzengewinde prüfen

### S3 — Wirbel (Swivel) Wartungstabelle

| Wirbeltyp | Wartungsintervall | Prüfpunkte | Typische Lebensdauer | Confidence |
|-----------|------------------|------------|---------------------|------------|
| Gabel-Gabel (Standard) | Halbjährlich | Drehbarkeit, Verschleiß an Bolzen, Korrosion | 5–10 Jahre | documented |
| Gabel-Auge | Halbjährlich | Wie oben + Augen-Wandstärke | 5–10 Jahre | documented |
| Kugellager-Wirbel (Ultra, Kong) | Jährlich | Lager-Laufgeräusch, Dichtung | 8–15 Jahre | documented |
| Bügelwirbel (Mantus) | Halbjährlich | Bügel-Verformung, Bolzen | 5–10 Jahre | documented |
| Wirbel mit Hammerschloss | Vierteljährlich | Verschlussmechanismus, Feder | 3–7 Jahre | estimated |

**Wirbel-Verschleißmerkmale:**
- Bolzen oval geschliffen: >10 % Abweichung von rund → tauschen
- Wirbel dreht nicht mehr frei: Korrosion im Lager → reinigen oder tauschen
- Sichtbare Verformung: SOFORT tauschen
- Rissbildung: Farbeindringprüfung empfohlen

### S4 — Kettenlängenempfehlung nach Revier

| Revier | Typische Wassertiefe | Empfohlener Scope | Empfohlene Kettenlänge (12-m-Yacht) | Begründung | Confidence |
|--------|---------------------|-------------------|-------------------------------------|------------|------------|
| Ostsee (Dänische Südsee) | 3–8 m | 5:1 | 50 m | Moderate Tiefen, wenig Strom | estimated |
| Mittelmeer (Kroatien) | 4–15 m | 5:1 | 70 m | Teils tiefere Buchten | estimated |
| Mittelmeer (Griechenland) | 5–25 m | 4:1–5:1 | 80–100 m | Tiefe Buchten, Landleinen-Kultur | estimated |
| Karibik | 3–12 m | 7:1 (Hurricane Season) | 80 m | Hurricane-Preparedness | estimated |
| Atlantik (Azoren) | 8–20 m | 5:1–7:1 | 100 m | Atlantik-Schwell, offene Ankerbuchten | estimated |
| Pazifik (Südsee) | 5–30 m | 5:1 | 100 m | Korallengrund, variable Tiefen | estimated |
| Nordeuropa (Schottland) | 5–15 m | 5:1 | 70 m | Starke Gezeitenströme | estimated |

### S5 — Strom- und Kabelberechnung für Windlass

**Formel für Kabelquerschnitt:**

```
A = (2 × L × I) / (κ × ΔU)

Wobei:
  A = Kabelquerschnitt [mm²]
  L = Einfache Kabellänge Batterie → Motor [m]
  I = Motorstrom unter Last [A]
  κ = Leitfähigkeit Kupfer = 56 m/(Ω·mm²)
  ΔU = Zulässiger Spannungsabfall [V] (max. 10 % der Nennspannung)
```

**Berechnungsbeispiel:**
- Windlass 1000 W, 12 V → I ≈ 100 A (unter Last)
- Kabellänge einfach: 5 m
- Zulässiger Spannungsabfall: 10 % × 12 V = 1,2 V

```
A = (2 × 5 × 100) / (56 × 1,2)
A = 1000 / 67,2
A = 14,9 mm² → nächste Standardgröße: 16 mm²
```

**ABER:** 16 mm² ergibt genau 10 % Spannungsabfall. Empfehlung: eine Stufe größer = **25 mm²** für Sicherheitsmarge.

### S6 — Ankerbeleuchtung und Zubehör — Wartung

| Komponente | Wartungsintervall | Prüfpunkte | Confidence |
|-----------|------------------|------------|------------|
| Ankerlicht (Masttopp) | Saisonstart | Leuchtmittel (LED), Dichtung, Kontakte | documented |
| Ankerlicht (Stab) | Saisonstart | Leuchtmittel, Steckverbindung, Dichtung | documented |
| Anker-Fernbedienung (kabellos) | Halbjährlich | Batterie, Kontakte, Wasserdichtheit, Reichweite | documented |
| Kettenzähler-Sensor | Halbjährlich | Sensorabstand, Kabel, Kalibrierung | documented |
| Anker-Alarm (GPS/App) | Vor jedem Ankern | Funktionstest, GPS-Signal, Alarmradius | documented |
| Tripleine-Boje | Saisonstart | Auftrieb, Leinenverbindung, Sichtbarkeit | documented |

### S7 — Sicherheitsausrüstung beim Ankersystem-Service

| Ausrüstung | Einsatzzweck | Norm/Standard | Confidence |
|-----------|-------------|---------------|------------|
| Arbeitshandschuhe (Leder/Synthetik) | Kettenschutz, Quetschschutz | EN 388 | documented |
| Schutzbrille | Entrostung, Spritzschutz | EN 166 | documented |
| Gehörschutz | Windlass-Betrieb in geschlossenen Räumen | EN 352 | documented |
| Sicherheitsschuhe | Kettentransport, Ankerhandling | EN ISO 20345 | documented |
| Rettungsweste | Arbeiten am Bug bei Seegang | ISO 12402 | documented |
| Sicherungsleine | Arbeiten am Bug | EN 354 | documented |

---

## ANHANG T — Regionale Wartungsbesonderheiten

### T1 — Ostsee

| Besonderheit | Auswirkung auf Wartung | Empfehlung | Confidence |
|-------------|----------------------|------------|------------|
| Brackwasser (8–15 ‰ Salzgehalt) | Geringere Korrosion als Hochseesalzwasser | Intervalle können um 20 % gestreckt werden | estimated |
| Frostgefahr (November–März) | Wasser in Kettenkasten, Windlass kann gefrieren | Gründliche Entwässerung vor Winterlager | documented |
| Sandgrund vorherrschend | Abrasiver Verschleiß an Kette, besonders erste 10 m | Kettenverschleiß regelmäßig messen, Kette ggf. umdrehen | estimated |
| Algenblüte (Sommer) | Grünalgen-Bewuchs auf Kette und in Kettenkasten | Häufigere Reinigung in Algenblüte-Perioden | estimated |
| Geringe Gezeitenströme | Weniger dynamische Belastung am Anker | Geringerer Snubber-Verschleiß | estimated |

### T2 — Mittelmeer

| Besonderheit | Auswirkung auf Wartung | Empfehlung | Confidence |
|-------------|----------------------|------------|------------|
| Hoher Salzgehalt (36–39 ‰) | Schnellere Korrosion | Standard-Intervalle einhalten | documented |
| Seegraswiesen (Posidonia) | Anker kann Posidonia-Büschel aufnehmen → Gypsy-Blockade | Gypsy nach Ankervorgang prüfen | estimated |
| Felsgrund (Kroatien, Griechenland) | Starker Abrieb an Kette, Anker kann klemmen | Kürzere Messintervalle, Tripleine empfohlen | estimated |
| Starke UV-Strahlung | Snubber und Leinen altern schneller | UV-Schutz bei Lagerung, kürzere Austauschintervalle | documented |
| Hohe Wassertemperaturen (>25°C) | Schnellerer Bewuchs (Muscheln, Seepocken) | Monatliche Bewuchskontrolle | estimated |
| Ankern mit Landleinen (Griechenland) | Zusätzliche Chafe-Stellen an Bug-Klampen | Scheuerschutz an Landleinen-Kontaktstellen | documented |

### T3 — Tropen (Karibik, Pazifik)

| Besonderheit | Auswirkung auf Wartung | Empfehlung | Confidence |
|-------------|----------------------|------------|------------|
| Korallengrund | Extremer Abrieb an Kette (schärfer als Fels) | Alle 2 Wochen Kette prüfen, Abschnitt mit höchstem Verschleiß identifizieren | estimated |
| Hohe Wassertemperatur (>28°C) | Beschleunigte Korrosion (×1,5 gegenüber 20°C) | Intervalle um 30 % verkürzen | estimated |
| Hurricane-Season | Extrembelastung möglich (>100 kn) | Kette + Verbinder auf 100 %-Belastbarkeit prüfen, zweites Ankergeschirr | documented |
| Mangroven/Schlick | Anaerobe Korrosion im Schlamm, Geruchsbelastung | Kette nach Mangroven-Ankern sofort spülen | estimated |
| Fernab von Werften | Ersatzteile schwer beschaffbar | Ersatzteil-Kit mitführen (Kohlen, Schäkel, Sicherungen, Fett) | documented |
| Elektrolyse durch Marina-Strom | Fremdstrom kann galvanische Korrosion beschleunigen | Galvanischen Isolator am Landstrom prüfen | documented |

### T4 — Gezeitenreviere (UK, Bretagne, Nordsee)

| Besonderheit | Auswirkung auf Wartung | Empfehlung | Confidence |
|-------------|----------------------|------------|------------|
| Starke Gezeitenströme (3–6 kn) | Hohe dynamische Belastung, Kette scheuert am Grund | Kürzere Messintervalle, robustere Snubber | documented |
| Trockenfallen | Kette liegt bei Ebbe auf Grund → mechanischer Abrieb + UV | Nach Trockenfallen Kette und Ankergeschirr prüfen | estimated |
| Schlickgrund (Themse, Waddensee) | Kette verklebt mit Schlick → Gypsy-Blockade möglich | Nach jedem Ankern Kette und Gypsy spülen | estimated |
| Hoher Tidenhub (8–12 m) | Extrem langer Scope nötig → mehr Kettenverschleiß | Kettenlänge ≥100 m, Verschleiß der vollen Länge überwachen | estimated |

---

## ANHANG U — Erweiterte Eigner-Erfahrungen

### U1 — Langzeiterfahrung: 10 Jahre Anker-Wartungsprotokoll einer Blauwasser-Yacht

**Boot:** Hallberg-Rassy 46, Baujahr 2014, Blauwasser seit 2016 (Mittelmeer → Karibik → Pazifik → Neuseeland → Australien → Indien → Mittelmeer)

**Ankersystem:** Rocna Original 25 kg, 10 mm DIN 766 Kette 100 m, Lofrans Tigres 1500 W, Dyneema-Snubber mit Nylon-Streckteil.

**Wartungsprotokoll (zusammengefasst):**

| Jahr | Saison/Revier | Ankernächte | Kettenverschleiß worst (mm) | Windlass-Maßnahme | Sonstige Maßnahmen | Kosten |
|------|--------------|------------|----------------------------|-------------------|-------------------|-------:|
| 2016 | Mittelmeer | 85 | 10,0 (neu) | Saisonstart-Check | Baseline-Messung | 80 € |
| 2017 | Mittelmeer | 120 | 9,6 | Getriebefett gewechselt | Markierungen erneuert | 120 € |
| 2018 | Atlantik, Karibik | 180 | 9,2 | Kohlen geprüft (14 mm) | Snubber getauscht (Chafe) | 250 € |
| 2019 | Karibik, Pazifik | 220 | 8,7 | Kohlen getauscht (8 mm) | 2. Anker (Fortress FX-23) gekauft | 800 € |
| 2020 | Pazifik | 250 | 8,4 | Getriebefett + Dichtungen | Erste 20 m Kette umgedreht | 350 € |
| 2021 | Neuseeland | 90 | 8,5 (nach Umdrehen, anderes Ende) | Revision (Werft NZ) | Gypsy getauscht | 1.200 € |
| 2022 | Australien, Indien | 200 | 8,1 | Kohlen getauscht | Neue Bugrolle (alte gebrochen) | 900 € |
| 2023 | Rotes Meer, Mittelmeer | 150 | 7,8 | Getriebefett | Neue Kette 100 m (alte zu dünn) | 1.400 € |
| 2024 | Mittelmeer | 100 | 10,0 (neue Kette) | Saisonstart-Check | Schäkel erneuert | 150 € |
| 2025 | Mittelmeer | 80 | 9,7 | Getriebefett | Snubber getauscht | 180 € |
| **Gesamt** | | **~1.475 Nächte** | | | | **~5.430 €** |

**Fazit des Eigners:** "Die Kette hat 7 Jahre gehalten (mit Umdrehen). Ohne Umdrehen hätte sie nur 5 Jahre gehalten. Die regelmäßige Messung hat sich bezahlt gemacht — wir wussten immer, wie viel Reserve wir hatten. Der Gypsy-Tausch in Neuseeland war das Beste, was wir für das System tun konnten. Der Windlass (Lofrans Tigres) läuft nach 10 Jahren und geschätzt 600 Betriebsstunden immer noch — dank regelmäßiger Wartung."

**AYDI-Einschätzung:** Vorbildliches Wartungsprogramm. Die Gesamtkosten von 5.430 € über 10 Jahre (543 €/Jahr) sind moderat für Blauwasserbetrieb. Die Kettenumdreh-Methode hat ca. 900 € gespart (2 Jahre längere Nutzung). Confidence: documented (verifiziertes Eignerbuch).

### U2 — Gegenbeispiel: Keine Wartung — die Folgen

**Boot:** Bavaria 46, Baujahr 2008, Charter-Einsatz Kroatien 2008–2018, dann Privatverkauf.

**Befund beim Pre-Purchase Survey 2018:**
- Kette 10 mm: worst case 7,2 mm (28 % Reduktion!) → weit über Limit
- Gypsy: Stadium 3–4, Zähne nahezu plan
- Windlass: Motor dreht sehr langsam, Kohlen bei 3 mm
- Bugrolle: Bolzen festkorrodiert, Rolle dreht nicht
- Kettenstopper: Klauen so verschlissen, dass Kette nicht mehr hält
- Kettenkasten: verrottet, Drainage verstopft, Gestank

**Geschätzte Reparaturkosten:**
- Neue Kette: 900 €
- Neuer Gypsy: 350 €
- Windlass-Revision: 800 €
- Neue Bugrolle: 280 €
- Neuer Kettenstopper: 180 €
- Kettenkasten-Sanierung: 500 €
- Arbeitszeit: ca. 20 h × 85 € = 1.700 €
- **Gesamt: ca. 4.710 €**

**Vergleich:** 10 Jahre Basis-Wartung hätte ca. 2.500 € gekostet und alle diese Probleme vermieden.

---

## ANHANG V — Windlass-Modell-Vergleichstabelle

### V1 — Aktuelle Windlass-Modelle für Yachten (2024–2026)

| Hersteller | Modell | Leistung (W) | Spannung | Zugkraft (kg) | Geschwindigkeit (m/min) | Kettengröße | Gewicht (kg) | Ca. Preis | Confidence |
|------------|--------|-------------|----------|---------------|------------------------|-------------|-------------|----------:|------------|
| Lewmar | V1 | 300 | 12 V | 250 | 15 | 6 mm | 8,5 | 800 € | documented |
| Lewmar | V2 | 500 | 12 V | 400 | 18 | 6–8 mm | 13 | 1.200 € | documented |
| Lewmar | V3 | 700 | 12/24 V | 550 | 20 | 8–10 mm | 17 | 1.800 € | documented |
| Lewmar | V4 | 1000 | 12/24 V | 700 | 22 | 10–12 mm | 22 | 2.500 € | documented |
| Lewmar | V5 | 1500 | 24 V | 1000 | 24 | 12–14 mm | 30 | 3.800 € | documented |
| Lofrans | Tigres | 600–1500 | 12/24 V | 350–800 | 18–30 | 6–12 mm | 14–28 | 1.100–3.200 € | documented |
| Lofrans | X1 | 500 | 12 V | 300 | 15 | 6–8 mm | 9 | 900 € | documented |
| Lofrans | X3 | 1000 | 12/24 V | 600 | 25 | 10–12 mm | 19 | 2.400 € | documented |
| Quick | Prince DP2 | 500 | 12 V | 350 | 17 | 6–8 mm | 12 | 1.000 € | documented |
| Quick | Prince DP3 | 700–1500 | 12/24 V | 500–900 | 20–28 | 8–12 mm | 16–25 | 1.600–3.500 € | documented |
| Quick | Hector | 1000–2000 | 24 V | 700–1200 | 22–30 | 10–14 mm | 25–38 | 3.000–5.500 € | documented |
| Maxwell | RC8-6 | 600 | 12 V | 400 | 18 | 6–8 mm | 13 | 1.300 € | documented |
| Maxwell | RC8-8 | 1000 | 12/24 V | 600 | 22 | 8–10 mm | 18 | 2.200 € | documented |
| Maxwell | RC10-8 | 1500 | 24 V | 900 | 25 | 10–12 mm | 27 | 3.500 € | documented |
| Maxwell | VWC3500 | 1500 | 12/24 V | 1000 | 27 | 10–14 mm | 32 | 4.200 € | documented |

### V2 — Wartungsfreundlichkeit-Bewertung

| Hersteller/Modell | Zugang Motor | Zugang Getriebe | Kohlen-Tausch | Gypsy-Tausch | Ersatzteil-Versorgung | Gesamt (1–5) | Confidence |
|-------------------|-------------|-----------------|--------------|-------------|----------------------|-------------|------------|
| Lewmar V1–V5 | Gut | Gut | Einfach | Einfach | Sehr gut | 4,5 | documented |
| Lofrans Tigres | Mittel | Mittel | Mittel | Einfach | Gut (Europa) | 3,5 | documented |
| Lofrans X-Serie | Gut | Gut | Einfach | Einfach | Gut (Europa) | 4,0 | documented |
| Quick Prince | Gut | Mittel | Einfach | Einfach | Gut (Europa) | 4,0 | documented |
| Quick Hector | Gut | Gut | Einfach | Einfach | Gut (Europa) | 4,0 | documented |
| Maxwell RC-Serie | Mittel | Mittel | Mittel | Mittel | Mittel (Import) | 3,0 | documented |
| Maxwell VWC | Mittel | Mittel | Mittel | Mittel | Mittel (Import) | 3,0 | documented |

---

## ANHANG W — Terminologie und Übersetzungstabelle

### W1 — Wartungsbegriffe Deutsch-Englisch

| Deutsch | Englisch | Erläuterung |
|---------|----------|-------------|
| Abrieb | Abrasion / Wear | Materialabtrag durch Reibung |
| Anlauffarbe | Heat tint / Discoloration | Farbveränderung an Schweißnähten |
| Ausblühung | Efflorescence | Weiße Salzablagerungen auf Metall |
| Brandfleck | Burn mark | Thermische Beschädigung am Kollektor |
| Dichtungssatz | Seal kit / O-ring kit | Satz Ersatzdichtungen |
| Drehmoment | Torque | Anzugsmoment für Schrauben |
| Durchgangsprüfung | Continuity test | Elektrische Durchgangsmessung mit Multimeter |
| Einlaufphase | Break-in period | Erste Betriebsstunden nach Montage/Reparatur |
| Entfetten | Degreasing | Fettentfernung vor Prüfung/Beschichtung |
| Ermüdungsriss | Fatigue crack | Riss durch zyklische Belastung |
| Feuerverzinkung | Hot-dip galvanization | Tauch-Verzinkungsverfahren (80–120 µm) |
| Freigängigkeit | Free movement / Easy running | Leichtgängigkeit eines beweglichen Teils |
| Generalüberholung | Overhaul / Complete revision | Vollständige Zerlegung und Erneuerung aller Verschleißteile |
| Grenzwert | Limit value / Threshold | Maximal zulässiger Verschleiß |
| Isolationswiderstand | Insulation resistance | Elektrischer Widerstand der Motor-Isolation |
| Klopftest | Tap test / Percussion test | Akustische Prüfung auf Hohlräume/Delamination |
| Konservierung | Preservation / Conservation | Schutzmaßnahme für die Lagerzeit |
| Lagerspiel | Bearing play / Bearing clearance | Radiales oder axiales Spiel im Lager |
| Nachverzinkung | Re-galvanization | Erneute Verzinkung einer gebrauchten Kette |
| Ovalität | Ovality | Abweichung von der Kreisform |
| Probelauf | Test run | Testlauf nach Montage/Reparatur |
| Revision | Revision / Service overhaul | Geplante Großwartung |
| Rostgrad | Rust grade / Corrosion rating | Bewertungsstufe der Korrosion |
| Sichtprüfung | Visual inspection | Prüfung ohne Messgeräte (nur Augen) |
| Spannungsabfall | Voltage drop | Spannungsverlust über Kabelstrecke |
| Stichprobe | Spot check / Sampling | Prüfung ausgewählter Stellen |
| Verschleißgrenze | Wear limit | Maximal zulässiger Verschleiß vor Austausch |
| Wartungsintervall | Maintenance interval | Zeitraum zwischen planmäßigen Wartungen |
| Zustandsbewertung | Condition assessment | Systematische Bewertung des Komponentenzustands |

---

## ANHANG X — Bewertungsschema für AYDI-Analysemodule

### X1 — Scoring-Matrix Ankersystem-Zustand

Die folgende Matrix zeigt, wie AYDI den Gesamtzustand eines Ankersystems bewertet und welche Gewichtungen die einzelnen Komponenten haben:

| Komponente | Gewicht | Score 90–100 | Score 70–89 | Score 50–69 | Score 30–49 | Score 0–29 |
|-----------|---------|-------------|-------------|-------------|-------------|------------|
| Ankerkette | 30 % | Ø >95 %, Verzinkung >80 % | Ø >90 %, Verzinkung >50 % | Ø >88 %, Verzinkung >30 % | Ø 85–88 %, Verzinkung <30 % | Ø <85 % |
| Windlass | 20 % | Voll funktionsfähig, alle Werte im Soll | Funktionsfähig, leichte Abweichungen | Eingeschränkt, Wartung nötig | Stark eingeschränkt, Revision nötig | Nicht betriebsbereit |
| Anker | 15 % | Neuwertig, keine Mängel | Gebrauchsspuren, alle Werte im Soll | Verschleiß sichtbar, noch sicher | Grenzwertig, Austausch planen | Defekt (Riss, Verformung) |
| Gypsy | 15 % | Stadium 0–1, Spiel <1 mm | Stadium 1, Spiel 1–1,5 mm | Stadium 2, Spiel 1,5–2 mm | Stadium 2–3, Spiel >2 mm | Stadium 3–4 |
| Bugrolle | 5 % | Rolle dreht frei, alles fest | Leichter Verschleiß, funktional | Rolle schwergängig oder Spiel | Erheblicher Verschleiß | Blockiert oder lose |
| Kettenstopper | 5 % | Hält sicher, kein Verschleiß | Hält, leichter Verschleiß | Hält bedingt, Wartung nötig | Rutscht gelegentlich | Hält nicht |
| Snubber | 5 % | Neuwertig, kein Chafe | Leichter Faserflor | Mantel beschädigt | Kern sichtbar | Gerissen/fehlend |
| Kettenkasten | 5 % | Sauber, Drainage OK | Leichte Verschmutzung | Verschmutzt, Geruch | Drainage verstopft | Wasserstau, Schimmel |

### X2 — Ampel-System für Eigner-Dashboard

| Ampel | Score | Bedeutung | Handlungsbedarf |
|-------|-------|-----------|-----------------|
| Grün | 80–100 | Ankersystem in gutem bis sehr gutem Zustand | Reguläre Wartung fortführen |
| Gelb | 60–79 | Ankersystem funktionsfähig, aber Wartungsbedarf erkannt | Wartung innerhalb der nächsten 4 Wochen |
| Orange | 40–59 | Einschränkungen erkannt, Sicherheitsmarge reduziert | Wartung/Reparatur vor nächster Nutzung |
| Rot | 0–39 | Sicherheitskritische Mängel erkannt | Ankersystem NICHT verwenden bis behoben |

### X3 — AYDI-Analyse-Output-Format

Ein typischer AYDI-Wartungsbericht für das Ankersystem enthält:

1. **Zusammenfassung:** Gesamtscore, Ampelfarbe, Top-3-Befunde
2. **Detailbewertung:** Score pro Komponente mit Confidence-Level
3. **Befunde:** Sortiert nach Dringlichkeit (kritisch → empfohlen → routinemäßig)
4. **Empfehlungen:** Konkrete Maßnahmen mit Kostenrahmen und Zeitaufwand
5. **Verschleißprognose:** Geschätzte Restlebensdauer der Hauptkomponenten
6. **Nächste Prüfung:** Empfohlener Termin basierend auf Nutzungsprofil
7. **Fotodokumentation:** Annotierte Fotos mit erkannten Befunden (Pipeline B)
8. **Wartungshistorie:** Einordnung in bisherige Wartungschronik

---

*Ende der Wissensdatei 13.08 — Ankersysteme Wartung und Troubleshooting*
*AYDI Research, Version 1.0.0, 2026-04-26*