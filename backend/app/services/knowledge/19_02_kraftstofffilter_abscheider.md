# 19.02 — Kraftstofffilter und Wasserabscheider im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 19.02** — Kategorie 19: Kraftstoffsystem und Kraftstoffaufbereitung
> **Confidence-Quelle:** measured (Hersteller-TDS, ISO-Normen), documented (Hersteller-Kataloge, Servicedokumentation), estimated (Erfahrungswerte Werft/Eigner)
> **Letzte Aktualisierung:** 2026-05-02

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien und Spezifikationen](#4-produktlinien-und-spezifikationen)
5. [Hersteller-Datenbank](#5-hersteller-datenbank)
6. [Filtereinsätze und Wechselintervalle](#6-filtereinsätze-und-wechselintervalle)
7. [Einbau und Installation](#7-einbau-und-installation)
8. [Wartung und Instandhaltung](#8-wartung-und-instandhaltung)
9. [Dieselpest — Mikrobiologische Kontamination](#9-dieselpest--mikrobiologische-kontamination)
10. [Fehlerbild-Atlas](#10-fehlerbild-atlas)
11. [Troubleshooting-Entscheidungsbäume](#11-troubleshooting-entscheidungsbäume)
12. [Normen und Vorschriften](#12-normen-und-vorschriften)
13. [Kraftstoffqualität und Additive](#13-kraftstoffqualität-und-additive)
14. [Dimensionierung und Auslegung](#14-dimensionierung-und-auslegung)
15. [Forum-Erfahrungen und Praxisberichte](#15-forum-erfahrungen-und-praxisberichte)
16. [FAQ — Häufig gestellte Fragen](#16-faq--häufig-gestellte-fragen)
17. [Glossar](#17-glossar)
18. [Schnell-Referenz](#18-schnell-referenz)
19. [ANHANG A — Fallstudie: Segelyacht 38ft, Racor 500FG verstopft nach Tropentörn](#anhang-a)
20. [ANHANG B — Fallstudie: Motoryacht 45ft, Dieselpest im Mittelmeer](#anhang-b)
21. [ANHANG C — Fallstudie: Blauwasseryacht 52ft, Dual-Racor-System](#anhang-c)
22. [ANHANG D — Fallstudie: Charteryacht, Separ SWK-2000 Erstinstallation](#anhang-d)
23. [ANHANG E — Fallstudie: Fischereifahrzeug 12m, Fleetguard-Upgrade](#anhang-e)
24. [ANHANG F — Fallstudie: Superyacht 28m, zentrale Kraftstoffaufbereitung](#anhang-f)
25. [ANHANG G — Fallstudie: Langfahrt-Katamaran, Vakuum-Entgasung](#anhang-g)
26. [ANHANG H — Fallstudie: Regattayacht, Gewichtsoptimiertes Filtersystem](#anhang-h)
27. [ANHANG I — Pydantic v2 Modelle: FuelFilterAssessment](#anhang-i)
28. [ANHANG J — Pydantic v2 Modelle: WaterSeparatorDiagnosis](#anhang-j)
29. [ANHANG K — Pydantic v2 Modelle: DieselPestAssessment](#anhang-k)
30. [ANHANG L — Pydantic v2 Modelle: FilterMaintenanceRecord](#anhang-l)
31. [ANHANG M — Pydantic v2 Modelle: FuelSystemConfiguration](#anhang-m)
32. [ANHANG N — Pydantic v2 Modelle: FilterElementSpecification](#anhang-n)
33. [ANHANG O — Pydantic v2 Modelle: FuelQualityTest](#anhang-o)
34. [ANHANG P — Pydantic v2 Modelle: TroubleshootingResult](#anhang-p)
35. [ANHANG Q — Pydantic v2 Modelle: FilterCostEstimate](#anhang-q)
36. [ANHANG R — AYDI Bewertungsschema für Kraftstofffiltersysteme](#anhang-r)

---

## 1. Einführung und Übersicht

### 1.1 Bedeutung der Kraftstofffiltration im maritimen Bereich

Kraftstofffilter und Wasserabscheider sind die kritischste Schutzbarriere zwischen dem Tankinhalt und der Einspritzanlage eines Schiffsdieselmotors. Die Konsequenzen eines Filterversagens sind unmittelbar und potenziell gefährlich: Leistungsverlust, Motorausfall, beschädigte Einspritzdüsen — und im schlimmsten Fall ein manövrierunfähiges Schiff in schwerem Wetter.

Die maritime Umgebung stellt besondere Anforderungen an die Kraftstoffaufbereitung:
- **Kondensation**: Temperaturwechsel zwischen Tag und Nacht erzeugen Wasser im Tank
- **Seegangsbewegung**: Aufwirbeln von Sedimenten und Verunreinigungen vom Tankboden
- **Lange Standzeiten**: Dieselkraftstoff steht wochen- oder monatelang im Tank
- **Biologische Kontamination**: Die Grenzschicht Diesel/Wasser ist Nährboden für Mikroorganismen
- **Qualitätsschwankungen**: Betankung in verschiedenen Häfen und Ländern mit unterschiedlicher Dieselqualität
- **Biodiesel-Anteil**: Moderner Diesel enthält bis zu 7% Biodiesel (B7), der hygroskopisch wirkt

### 1.2 Schadenspotenzial unzureichender Filtration

**Einspritzsystem-Schäden:**
- Common-Rail-Systeme (>1.600 bar): Partikel >4µm verursachen Verschleiß an Injektoren
- Kosten einer Injektorüberholung: €800–€2.500 pro Stück (4–6 Injektoren typisch)
- Einspritzpumpen-Überholung: €3.000–€8.000
- Totalausfall Einspritzanlage: €8.000–€25.000 je nach Motor

**Wasser im Kraftstoff:**
- Korrosion in Einspritzpumpe und Injektoren
- Kavitation an Hochdruckkomponenten
- Mikrobiologisches Wachstum (Dieselpest)
- Verringerter Heizwert → Leistungsverlust
- Ab 200 ppm freies Wasser: messbare Schäden bei Common-Rail

**Biologische Kontamination:**
- Verstopfte Filter (schnellster sichtbarer Effekt)
- Korrosive Metaboliten der Mikroorganismen (organische Säuren)
- Tankwandkorrosion durch Biofilm
- Vollständige Systemkontamination erfordert Tank-Sanierung (€2.000–€10.000+)

### 1.3 Scope dieser Wissensdatei

Diese Datei behandelt:
- Alle Kraftstofffilter und Wasserabscheider für Dieselmotoren im Yachtbau
- Primärfilter (Vorfilter/Wasserabscheider vor dem Motor)
- Sekundärfilter (motormontierte Feinfilter)
- Kraftstoffaufbereitungssysteme (Polier-/Umwälzsysteme)
- Produktlinien: Racor (Parker Hannifin), Separ, Vetus, Fleetguard (Cummins), Mann+Hummel, Delphi, CAV, Bosch
- Filtereinsätze, Wartungsintervalle, Diagnose und Fehlerbehebung
- Dimensionierung für verschiedene Motorleistungen und Bootsklassen

**Nicht behandelt:**
- Benzinfilter (→ separate Wissensdatei 19.03)
- Ölfilter (→ Wissensdatei 19.04)
- Luftfilter (→ Wissensdatei 19.05)
- Tankbau und Tanksanierung (→ Wissensdatei 19.01)

### 1.4 Bootsklassen-Kalibrierung

| Bootsklasse | Typische Motorleistung | Filterdurchfluss | Typisches System |
|---|---|---|---|
| Segelyacht 8–12m | 15–40 PS | 60–150 l/h | Racor 110A oder Separ SWK-2000/5 |
| Segelyacht 12–16m | 40–80 PS | 150–300 l/h | Racor 500FG oder Vetus WS180 |
| Motoryacht 8–12m | 100–250 PS | 300–500 l/h | Racor 500FG oder Separ SWK-2000/10 |
| Motoryacht 12–18m | 250–600 PS (2×) | 500–1.000 l/h | Racor 900FG oder Separ SWK-2000/18 |
| Motoryacht 18–24m | 500–1.200 PS (2×) | 800–2.000 l/h | Racor 1000FG oder Fleetguard |
| Superyacht 24m+ | 1.000+ PS (2×) | 2.000+ l/h | Racor 75900 oder zentrale Aufbereitung |

---

## 2. Grundlagen und Theorie

### 2.1 Filtrationsmechanismen

Kraftstofffilter nutzen verschiedene physikalische Prinzipien — häufig in Kombination:

#### 2.1.1 Oberflächenfiltration (Siebwirkung)

Das grundlegendste Prinzip: Partikel, die größer als die Porenöffnung sind, werden an der Filteroberfläche zurückgehalten.

- **Vorteile**: Definierte Abscheidegrenze, hoher Wirkungsgrad bei der Nennporengröße
- **Nachteile**: Schnelle Zusetzen bei hoher Schmutzlast, keine Tiefenwirkung
- **Typische Anwendung**: Metallsiebe als Vorfilter (100–300µm)
- **Maritime Relevanz**: Saugkorb im Tank (Mesh 60–100), Siebfilter in Leitungsarmaturen

#### 2.1.2 Tiefenfiltration (Absorption)

Partikel werden nicht nur an der Oberfläche, sondern im gesamten Filtervolumen zurückgehalten. Das Filtermedium besteht aus mehreren Schichten mit abnehmender Porengröße.

- **Vorteile**: Hohe Schmutzaufnahmekapazität, lange Standzeit
- **Nachteile**: Kein scharfer Cutoff — Abscheidegrad steigt graduell
- **Typische Anwendung**: Zellulose- und Synthetik-Filtereinsätze (2–30µm)
- **Maritime Relevanz**: Racor-Filtereinsätze (2µm, 10µm, 30µm Varianten)

**Filterfeinheit und Beta-Wert:**
Der Beta-Wert (βx) gibt das Verhältnis von Partikeln vor und nach dem Filter bei einer bestimmten Größe x an:
- β10 = 200 bedeutet: Von 200 Partikeln ≥10µm passiert 1 den Filter (99,5% Effizienz)
- β10 = 1000 bedeutet: 99,9% Effizienz bei 10µm
- Für Common-Rail-Motoren: β4(c) ≥ 200 empfohlen

#### 2.1.3 Koaleszenz (Wasserabscheidung)

Winzige Wassertröpfchen (Emulsion) werden beim Durchgang durch ein hydrophobes Filtermedium zusammengeführt (koalesziert) zu größeren Tropfen, die dann durch Schwerkraft nach unten sinken.

**Funktionsprinzip:**
1. Kraftstoff-Wasser-Gemisch tritt ein
2. Winzige Wassertröpfchen (1–50µm) treffen auf hydrophobe Fasern
3. Tröpfchen vereinigen sich an den Fasern zu größeren Tropfen (100–500µm)
4. Große Tropfen lösen sich von den Fasern
5. Schwerkraft zieht die Tropfen nach unten in den Sammelbecher

**Koaleszenz-Effizienz:**
- Neue Einsätze: >95% Wasserabscheidung
- Gealterte Einsätze (>500 Betriebsstunden): 60–80%
- Verschmutzte/kontaminierte Einsätze: <50% — Austausch erforderlich

#### 2.1.4 Schwerkraftabscheidung (Sedimentation)

Wasser (Dichte 1,0 g/cm³) ist schwerer als Diesel (Dichte 0,82–0,86 g/cm³). In einem Beruhigungsraum sinkt freies Wasser nach unten.

**Effektivität:**
- Freies Wasser (>500µm Tropfen): >99% Abscheidung
- Gebundenes Wasser (Emulsion, <50µm): <10% — erfordert Koaleszenz
- Kritischer Faktor: Verweilzeit im Abscheider
- Seegang reduziert die Effizienz erheblich (Aufwirbeln)

#### 2.1.5 Zentrifugalabscheidung

Durch Rotation oder Strömungsumlenkung werden schwerere Partikel und Wasser nach außen geschleudert.

- **Vorteile**: Kein Filtermedium, das verstopft; hoher Durchfluss
- **Nachteile**: Weniger effektiv bei kleinen Partikeln (<10µm), teuer
- **Maritime Anwendung**: Spinner II (Racor), Alfa Laval Separatoren (Großyachten)

### 2.2 Partikelgrößen und Schadwirkung

| Partikelgröße | Beispiel | Schadwirkung am Motor |
|---|---|---|
| >100µm | Rost, Tankschuppen, Dichtungsreste | Ventile blockiert, Leitungen verstopft |
| 30–100µm | Grober Sand, Lackpartikel | Abrasion Einspritzpumpe, Filter verstopft |
| 10–30µm | Feiner Staub, oxidierter Diesel | Verschleiß Injektordüsen, Pumpenventile |
| 4–10µm | Feinstaub, biologische Partikel | Erosion Common-Rail-Injektoren |
| 2–4µm | Submikron-Partikel | Langzeitverschleiß Hochdruckkomponenten |
| <2µm | Kolloidale Partikel | Minimal bei mechanischen Systemen |

**Kritische Grenze für moderne Dieselmotoren:**
- Mechanische Einspritzung (Vorkammer, Wirbelkammer): 10–30µm ausreichend
- Direkteinspritzung (konventionell): 10µm empfohlen
- Common-Rail (<1.600 bar): 5µm empfohlen
- Common-Rail (>1.600 bar): 2–4µm erforderlich

### 2.3 Wassergehalt im Dieselkraftstoff

**Formen von Wasser im Diesel:**
- **Gelöstes Wasser**: 50–80 ppm bei 20°C (unsichtbar, nicht schädlich)
- **Emulgiertes Wasser**: Feine Tröpfchen, trübt den Kraftstoff (milchig)
- **Freies Wasser**: Sichtbare Phase am Tankboden (extrem schädlich)

**Sättigungspunkt:**
- Diesel bei 20°C: ca. 60–80 ppm gelöstes Wasser
- Bei Temperaturabfall um 10°C: ca. 30 ppm kondensieren aus
- Ein 500-Liter-Tank kann über eine Saison 5–15 Liter freies Wasser ansammeln

**Wasser-Grenzwerte:**
| Norm/Hersteller | Max. Wassergehalt | Messmethode |
|---|---|---|
| EN 590 (Tankstelle) | 200 ppm | Karl-Fischer |
| ISO 4406 | Kodiert | Partikelzählung |
| Volvo Penta | <200 ppm | Am Einspritzpumpeneingang |
| Yanmar | <200 ppm | Am Motoreingang |
| Caterpillar | <200 ppm frei, <500 ppm gesamt | Karl-Fischer |
| Common-Rail (generisch) | <200 ppm | Karl-Fischer |

### 2.4 Dieselpest — Mikrobiologische Kontamination

#### 2.4.1 Was ist Dieselpest?

„Dieselpest" (engl. Diesel Bug) bezeichnet das unkontrollierte Wachstum von Mikroorganismen im Kraftstoffsystem. Diese Organismen leben an der Grenzschicht zwischen Wasser und Diesel:

**Beteiligte Organismen:**
- **Bakterien**: Pseudomonas aeruginosa, Desulfovibrio (sulfatreduzierende Bakterien → Schwefelwasserstoff, Korrosion)
- **Hefen**: Candida-Arten (bilden dickflüssigen Biofilm)
- **Pilze**: Hormoconis resinae (früher Cladosporium resinae) — der „Klassiker" der Dieselpest, bildet dichte Myzelmatten, besonders aggressiv bei Kerosin/Diesel

#### 2.4.2 Wachstumsbedingungen

| Faktor | Optimal für Wachstum | Hemmend |
|---|---|---|
| Wasser | >500 ppm freies Wasser | <100 ppm |
| Temperatur | 25–35°C (Mittelmeer-Sommer ideal) | <10°C, >60°C |
| Nährstoffe | Biodiesel-Anteil (FAME) | Reiner Diesel (selten verfügbar) |
| Standzeit | >4 Wochen ohne Bewegung | Regelmäßiger Betrieb |
| Tank | Nicht beschichteter Stahltank | Sauberer Edelstahl/Aluminium |

#### 2.4.3 Erkennung und Stadien

**Stadium 1 — Früh (unsichtbar):**
- Leicht trüber Kraftstoff
- Filterstandzeit noch normal
- Nur durch Labortest (Dip-Slides, ATP-Test) nachweisbar
- <10³ CFU/ml (colony forming units)

**Stadium 2 — Mittel:**
- Schmieriger Belag auf Filtereinsätzen
- Verkürzte Filterstandzeit (50% der Normalzeit)
- Leichter „fauliger" Geruch beim Tanköffnen
- 10³–10⁵ CFU/ml

**Stadium 3 — Schwer:**
- Schwarze/braune Schleim-Klumpen im Filter und Tank
- Filter verstopft innerhalb von Stunden nach Wechsel
- Deutlicher Schwefelwasserstoff-Geruch (faule Eier)
- Motorstottern, Leistungsverlust
- >10⁵ CFU/ml

**Stadium 4 — Kritisch:**
- Tank komplett kontaminiert, Biofilm an Tankwänden
- Korrosion unter Biofilm (MIC — Microbiologically Influenced Corrosion)
- Komplette Systemreinigung erforderlich
- >10⁷ CFU/ml

### 2.5 Filterfeinheit und Durchflussraten

#### 2.5.1 Nenn-Filterfeinheit vs. Absolut-Filterfeinheit

- **Nenn-Filterfeinheit (Nominal Rating)**: Der Filter hält einen bestimmten Prozentsatz der Partikel dieser Größe zurück (typisch 95%)
- **Absolut-Filterfeinheit (Absolute Rating)**: Der Filter hält 99,9%+ der Partikel dieser Größe zurück

**Praxisbeispiel:**
Ein „10µm nominal" Filter lässt möglicherweise 5% der 10µm-Partikel durch. Ein „10µm absolut" Filter lässt praktisch keine durch. Für maritime Anwendung stets Absolutwerte bevorzugen oder Beta-Werte prüfen.

#### 2.5.2 Durchflussraten

Die Dimensionierung erfolgt nach der maximalen Kraftstoffdurchflussmenge des Motors plus Sicherheitsfaktor:

**Berechnung:**
```
Durchfluss_Motor [l/h] = Motorleistung [kW] × spez. Verbrauch [g/kWh] / Dichte_Diesel [g/l]
Durchfluss_Filter [l/h] = Durchfluss_Motor × Sicherheitsfaktor (1,5–2,0)
```

**Typische spezifische Verbräuche:**
- Saugdiesel (Vorkammer): 250–280 g/kWh
- Direkteinspritzer (mechanisch): 220–250 g/kWh
- Common-Rail: 195–230 g/kWh

**Beispielrechnung:**
Motor: 100 kW (136 PS) Common-Rail
Spez. Verbrauch: 220 g/kWh
Diesel-Dichte: 840 g/l
Durchfluss_Motor = 100 × 220 / 840 = 26,2 l/h
Durchfluss_Filter = 26,2 × 2,0 = 52,4 l/h → Racor 500FG (227 l/h) wäre ausreichend

**Wichtig**: Die Rücklaufmenge bei Common-Rail-Systemen ist erheblich (bis zu 80% des geförderten Kraftstoffs fließen zurück). Der Filter muss den gesamten Förderstrom der Kraftstoffpumpe bewältigen können, nicht nur den Verbrauch.

### 2.6 Druckverlust und Strömungswiderstand

**Sauberer Filter:**
- Vorfilter/Wasserabscheider: 0,5–2,0 kPa (5–20 mbar)
- Feiner Motorfilter: 5–15 kPa (50–150 mbar)

**Verschmutzter Filter (Wechselgrenze):**
- Vorfilter: 15–25 kPa (150–250 mbar)
- Motorfilter: 30–50 kPa (300–500 mbar)

**Vakuumgrenze (Motor saugt Luft):**
- Typisch: -30 bis -50 kPa (je nach Motor)
- Manche Motoren haben Vakuum-Schalter: Warnung bei -20 kPa

**Höhenunterschied Tank → Motor:**
- 1m Höhendifferenz = ca. 6,5 kPa zusätzlicher Saugwiderstand
- Tank unter Motor: erschwerter Betrieb, stärkere Förderpumpe erforderlich
- Tank über Motor: erleichterter Betrieb, Schwerkraftzufuhr möglich

---

## 3. Typenübersicht

### 3.1 Vorfilter / Grobfilter

**Funktion**: Erste Verteidigungslinie, entfernt grobe Verunreinigungen und separiert freies Wasser. Sitzt zwischen Tank und Motor, in der Saugleitung.

**Merkmale:**
- Filterfeinheit: 10–30µm
- Integrierter Wassersammelbecher (transparent oder mit Sensor)
- Handbetätigte Wasserablass-Schraube (Drain)
- Oft mit Vakuummeter-Anschluss
- Wechselbarer Einsatz (Element)

**Typische Vertreter:**
- Racor Turbine Serie (500FG, 900FH, 1000FH)
- Separ SWK-2000 Serie
- Vetus WS-Serie
- Griffin GS-Serie
- Delphi/CAV Primer-Serie

**Einbauort:**
- Gut zugänglich im Motorraum
- Möglichst tief (Schwerkraft-Wasserabscheidung)
- Vor der Kraftstoff-Förderpumpe
- Vibrationsfrei montiert

### 3.2 Feinfilter (Sekundärfilter)

**Funktion**: Letzte Filtration vor der Einspritzanlage. Meist motormontiert und vom Motorhersteller spezifiziert.

**Merkmale:**
- Filterfeinheit: 2–10µm (abhängig vom Einspritzsystem)
- Spin-On-Patrone (aufschraubbar) oder Einsatzfilter
- Meist ohne Wassersammelbecher (Wasser sollte bereits entfernt sein)
- Wechsel gemäß Motorhersteller-Intervall

**Typische Vertreter:**
- Volvo Penta OEM-Filter (3840335, 3825133, 21718912)
- Yanmar OEM-Filter (119773-55510, 129470-55703)
- Caterpillar OEM-Filter (1R-0749, 1R-0751)
- Fleetguard FS-Serie (Cummins-Motoren)
- Mann+Hummel WK-Serie (Universal)

### 3.3 Wasserabscheider (dediziert)

**Funktion**: Primär auf Wasserentfernung ausgelegt, sekundär auf Partikelfiltration.

**Merkmale:**
- Großer Beruhigungsraum für Schwerkraftabscheidung
- Koaleszenz-Element zur Emulsionsbrechung
- Transparenter Sammelbecher mit Wasserstandsanzeige
- Manuelles oder automatisches Drainventil
- Teilweise mit Wasserstandssensor (Alarm)

**Unterschied zum Vorfilter:**
Während viele Vorfilter kombinierte Filter/Wasserabscheider sind, gibt es auch reine Wasserabscheider ohne Filterfunktion — sinnvoll als erste Stufe bei stark wasserhaltigem Kraftstoff.

### 3.4 Kombinationssysteme (Filter + Wasserabscheider)

Die häufigste Bauform im Yachtbau vereint beides in einem Gehäuse:

**Aufbau typisch (Racor-Prinzip):**
1. Kraftstoff tritt oben ein
2. Erste Schwerkraftabscheidung im konischen Becher (freies Wasser sinkt)
3. Koaleszenz-Filterelement (Wasseremulsion wird gebrochen)
4. Partikel-Filtration durch Zellulose-/Synthetik-Medium
5. Sauberer Kraftstoff tritt oben aus
6. Wasser sammelt sich unten im transparenten Becher

**Vorteile:**
- Kompakter Einbau
- Nur ein Wechsel-Element
- Standardisierte Einsätze

**Nachteile:**
- Kompromiss zwischen Filtration und Wasserabscheidung
- Bei schwerem Wasserbefall schnell überfordert
- Einzelnes Element für zwei Aufgaben

### 3.5 Zentrifugalabscheider / Spinner

**Funktion**: Nutzt Zentrifugalkraft zur Partikel- und Wasserentfernung. Keine Filtermedien, die verstopfen.

**Merkmale:**
- Eingangsstutzen tangential → Wirbelströmung
- Schwere Partikel und Wasser nach außen/unten
- Sauberer Kraftstoff aus dem Zentrum nach oben
- Kein Druckverlust-Anstieg über die Zeit
- Begrenzte Effizienz bei kleinen Partikeln (<10µm)

**Typische Vertreter:**
- Racor Spinner II
- Alfa Laval PureNOx / ALCAP (Großyachten)
- GEA Westfalia (kommerzielle Schiffe)

**Einsatz im Yachtbau:**
- Selten bei Yachten <20m (Overkill, teuer)
- Ab 24m als Kraftstoff-Polier-System (24/7-Umwälzung)
- Superyachten: Standard im Maschinenraum

### 3.6 Kraftstoff-Poliersysteme

**Funktion**: Permanente Umwälzung des Tankinhalts durch Filtersystem, auch bei stehendem Motor.

**Aufbau:**
- Kleine Elektro-Umwälzpumpe (12V/24V)
- Eigener Filtersatz (Partikel + Wasser)
- Ansaugung vom Tankboden, Rückführung oben
- Timer-gesteuert oder dauerbetrieb
- Optional mit Heizung (Paraffin-Ausscheidung verhindern)

**Produkte:**
- Racor FBO-Serie (Fuel Biocide/Oxidation)
- KTI-Plersch Kraftstoffaufbereitung
- FPS (Fuel Polishing Systems) verschiedener Hersteller
- Eigenbau aus Racor-Filter + Jabsco-Pumpe (verbreitet)

**Empfehlung nach Bootsklasse:**
- Segelyacht <14m: nicht nötig, regelmäßiger Filterwechsel reicht
- Motoryacht >14m mit großen Tanks: empfohlen
- Blauwasseryacht: stark empfohlen (lange Standzeiten, Tanken in Entwicklungsländern)
- Superyacht: Standard

---

## 4. Produktlinien und Spezifikationen

### 4.1 Racor (Parker Hannifin) — Turbine-Serie

Racor ist der De-facto-Standard im Yachtbau. Die Turbine-Serie nutzt ein patentiertes Zentrifugal-Vorabscheider-Prinzip: Der Kraftstoff wird beim Eintritt in Rotation versetzt (daher „Turbine"), schwere Partikel und Wasser werden nach außen geschleudert, bevor der Kraftstoff das Filterelement erreicht.

#### 4.1.1 Racor 110A / 120A (Kleinste Baugröße)

**Spezifikationen:**
- Max. Durchfluss: 110A: 57 l/h (15 GPH), 120A: 114 l/h (30 GPH)
- Filterfeinheit: 10µm oder 30µm (je nach Einsatz)
- Wasserabscheidung: >95% freies Wasser
- Anschlüsse: 3/8"-14 NPTF
- Gewicht: 0,8 kg (leer)
- Einsätze: R12T (10µm), R12P (30µm), R12S (2µm)
- Transparenter Becher: Standard (Option Metallbecher für Motorraum)
- Betriebsdruck: max. 2,4 bar
- Montage: 2 Bolzen

**Einsatzbereich:**
- Segelyachten 7–10m mit Einzylinder-Diesel 8–20 PS
- Typisch: Yanmar 1GM10, 2GM20, Volvo Penta D1-13/20

**Preise (Stand 2025/26):**
- 120A Komplettgehäuse: €95–€130
- Filtereinsatz R12T (10µm): €12–€18
- Filtereinsatz R12S (2µm): €18–€25
- Becherkit klar: €25–€35

#### 4.1.2 Racor 200 Serie (Mittlere Baugröße)

**Modelle:**
- 215R: 57 l/h, Reihenfilter
- 230R: 114 l/h, Reihenfilter
- 245R: 170 l/h, Reihenfilter

**Einsätze:**
- R20T (10µm), R20P (30µm), R20S (2µm)

**Einsatzbereich:**
- Segelyachten 9–13m, Motoryachten 7–10m
- Typisch: Yanmar 3JH-Serie, Volvo Penta D1-30/D2-40

#### 4.1.3 Racor 500FG / 500FH (Bestseller im Yachtbau)

Die Racor 500FG ist der meistverkaufte marine Kraftstofffilter/Wasserabscheider weltweit. „FG" steht für „Fuel/Gas" (Diesel), „FH" für „Fuel/Heater" (Heizöl).

**Spezifikationen:**
- Max. Durchfluss: 227 l/h (60 GPH)
- Filterfeinheit: 2µm, 10µm oder 30µm (je nach Einsatz)
- Wasserabscheidung: >99% freies Wasser bei Nenndurchfluss
- Anschlüsse: 3/4"-16 UNF (Standard), optional M14×1,5
- Höhe (gesamt): ca. 280 mm
- Durchmesser (Becher): ca. 95 mm
- Gewicht: 1,5 kg (leer)
- Betriebsdruck: max. 3,4 bar (0,5 bar Saugseite)
- Betriebstemperatur: -30°C bis +80°C

**Filtereinsätze für 500FG:**
| Teilenummer | Feinheit | Material | Einsatzbereich |
|---|---|---|---|
| 2010TM-OR | 10µm | Zellulose | Standard, mechanische Einspritzung |
| 2010SM-OR | 2µm | Zellulose | Common-Rail, höchste Reinheit |
| 2010PM-OR | 30µm | Zellulose | Vorfilter, stark verschmutzter Diesel |
| 2010N-10 | 10µm | Nylon-Sieb | Wiederverwendbar, Notfall-Backup |
| 2010TM-OR-K | 10µm + Wasserabsorber | Zellulose + Polymer | Emulgiertes Wasser (Biodiesel) |

**Hinweis zu -OR Suffix**: „OR" = O-Ring im Einsatz enthalten. Immer bevorzugen.

**Einbauoptionen:**
- 500FGSS: Edelstahlkopf (empfohlen für Salzwasserumgebung)
- 500FG: Aluminium-Druckguss-Kopf (Standard)
- 500FH: Identisch, aber für Heizöl-Anwendung zertifiziert

**Zubehör:**
- RK11-1606-1: Vakuummeter-Kit (Zeigt Verschmutzungsgrad)
- RK21069: Wasserstandssensor-Kit (12V oder 24V, Alarmsignal)
- T-Handle: Schnellwechsel-Handgriff für Einsatz
- Bowl Shield: Metallschutz für den transparenten Becher

**Preise (Stand 2025/26):**
- 500FG Komplettgehäuse mit Einsatz: €220–€320
- 500FGSS (Edelstahl): €350–€450
- Filtereinsatz 2010TM-OR (10µm): €22–€32
- Filtereinsatz 2010SM-OR (2µm): €28–€38
- Vakuummeter-Kit: €45–€65
- Wasserstandssensor: €55–€85

#### 4.1.4 Racor 900 Serie (Hoher Durchfluss)

**Modelle:**
- 900FG: Max. 340 l/h (90 GPH)
- 900FH: Identisch, Heizöl-Anwendung
- 900MA: Eingang/Ausgang oben (space-saving)

**Spezifikationen:**
- Filterfeinheit: 2µm, 10µm, 30µm
- Anschlüsse: 1"-14 UNS
- Höhe: ca. 340 mm
- Durchmesser: ca. 115 mm
- Gewicht: 2,1 kg (leer)

**Filtereinsätze:**
| Teilenummer | Feinheit | Material |
|---|---|---|
| 2040TM-OR | 10µm | Zellulose |
| 2040SM-OR | 2µm | Zellulose |
| 2040PM-OR | 30µm | Zellulose |
| 2040N-10 | 10µm | Nylon (wiederverwendbar) |
| 2040TM-OR-K | 10µm + Wasserabsorber | Zellulose + Polymer |

**Einsatzbereich:**
- Motoryachten 12–18m, Twin-Engines mittlerer Leistung
- Typisch: Volvo Penta D4/D6, Yanmar 6LY-Serie, Cummins QSB 5.9

**Preise (Stand 2025/26):**
- 900FG Gehäuse: €350–€450
- Einsatz 2040TM-OR: €32–€45
- Einsatz 2040SM-OR: €38–€52

#### 4.1.5 Racor 1000 Serie (Hochleistung)

**Modelle:**
- 1000FG: Max. 681 l/h (180 GPH)
- 1000FH: Heizöl-Anwendung
- 1000MA: Top-In/Top-Out

**Spezifikationen:**
- Filterfeinheit: 2µm, 10µm, 30µm
- Anschlüsse: 1"-14 UNS
- Höhe: ca. 410 mm
- Durchmesser: ca. 140 mm
- Gewicht: 3,2 kg (leer)

**Filtereinsätze:**
| Teilenummer | Feinheit | Material |
|---|---|---|
| 2020TM-OR | 10µm | Zellulose |
| 2020SM-OR | 2µm | Zellulose |
| 2020PM-OR | 30µm | Zellulose |
| 2020N-10 | 10µm | Nylon (wiederverwendbar) |

**Einsatzbereich:**
- Motoryachten 16–24m, leistungsstarke Motoren
- Typisch: Caterpillar C7/C9, MAN D2676, Volvo Penta D11/D13, MTU 8V/10V

**Preise (Stand 2025/26):**
- 1000FG Gehäuse: €480–€620
- Einsatz 2020TM-OR: €42–€58
- Einsatz 2020SM-OR: €52–€68

#### 4.1.6 Racor 75900 / 731000 (Superyacht-Klasse)

**Spezifikationen:**
- 75900: Max. 1.135 l/h (300 GPH)
- 731000: Max. 1.893 l/h (500 GPH)
- Doppelfilter-Ausführung (Umschaltbar, Wechsel unter Last)
- Edelstahl-Gehäuse
- Integriertes Differential-Druckmanometer

**Einsatzbereich:**
- Superyachten 24m+, großvolumige Motoren
- Typisch: MTU 12V/16V, Caterpillar C12/C18/C32

**Preise:** €2.500–€6.000 (Doppelgehäuse)

#### 4.1.7 Racor Dual-Manifold-Systeme

Für unterbrechungsfreien Betrieb: Zwei Filter parallel mit Umschaltventil.

**Modelle:**
- 75500MAX: 2× 500FG mit Manifold, max. 454 l/h
- 75900MAX: 2× 900FG mit Manifold, max. 681 l/h
- 731000MAX: 2× 1000FG mit Manifold, max. 1.362 l/h

**Vorteile:**
- Filterwechsel bei laufendem Motor möglich
- Notfall-Reserve bei plötzlicher Filterverstopfung
- Verdoppelte Filterstandzeit pro Seite
- Pflicht für Kategorie-A-Yachten (ozeangehend) laut vielen Versicherern

**Preise:** €700–€1.800 (nur Manifold-Kit, ohne Filter)

### 4.2 Separ — SWK-2000 Serie

Separ (SEPAR Filter GmbH, Deutschland) ist besonders in Europa verbreitet und bekannt für die SWK-2000-Serie, die durch ein einzigartiges Doppel-Koaleszenz-Prinzip arbeitet.

#### 4.2.1 Funktionsprinzip SWK-2000

1. **Vorfilter-Sieb**: 100µm Metallsieb am Eingang
2. **Erste Koaleszenz-Stufe**: Hydrophobes Medium bricht Emulsion
3. **Schwerkraft-Beruhigungszone**: Wasser sinkt ab
4. **Zweite Filtrationsstufe**: Feinfilter-Element (10µm oder 30µm)
5. **Transparenter Sammelbecher**: Wasserstand sichtbar

#### 4.2.2 Modellreihe SWK-2000

| Modell | Max. Durchfluss | Anschluss | Einsatzbereich |
|---|---|---|---|
| SWK-2000/5 | 75 l/h | 3/8" BSP | Segelyacht 8–12m, 15–30 PS |
| SWK-2000/5/50 | 125 l/h | 1/2" BSP | Segelyacht 10–14m, 30–50 PS |
| SWK-2000/10 | 250 l/h | 3/4" BSP | Motoryacht 8–14m, 50–150 PS |
| SWK-2000/18 | 450 l/h | 1" BSP | Motoryacht 14–20m, 150–400 PS |
| SWK-2000/40 | 1.000 l/h | 1 1/4" BSP | Motoryacht 20m+, 400+ PS |
| SWK-2000/130 | 3.250 l/h | 2" BSP | Superyacht/Kommerziell |

**Filtereinsätze SWK-2000:**
| Teilenummer | Feinheit | Passend für |
|---|---|---|
| 01030 | 30µm | SWK-2000/5 |
| 01010 | 10µm | SWK-2000/5 |
| 01050 | 30µm | SWK-2000/5/50 |
| 01051 | 10µm | SWK-2000/5/50 |
| 02030 | 30µm | SWK-2000/10 |
| 02010 | 10µm | SWK-2000/10 |
| 02018-30 | 30µm | SWK-2000/18 |
| 02018-10 | 10µm | SWK-2000/18 |
| 02040-30 | 30µm | SWK-2000/40 |
| 02040-10 | 10µm | SWK-2000/40 |

**Vorteile Separ:**
- Hervorragende Wasserabscheidung (Doppel-Koaleszenz)
- Robuste Bauweise (Aluminium-Druckguss, marinisiert)
- Gute Verfügbarkeit in Europa
- Deutsches Produkt, kurze Lieferwege

**Nachteile:**
- Filtereinsätze teurer als Racor-Äquivalente
- Geringere Modellvielfalt als Racor
- Keine 2µm-Option ab Werk
- Weniger Zubehör (kein Vakuummeter-Kit ab Werk)

**Preise (Stand 2025/26):**
- SWK-2000/5 Gehäuse: €150–€200
- SWK-2000/10 Gehäuse: €250–€350
- SWK-2000/18 Gehäuse: €400–€520
- Filtereinsatz 01010 (10µm, /5): €18–€26
- Filtereinsatz 02010 (10µm, /10): €25–€35
- Filtereinsatz 02018-10 (10µm, /18): €35–€50

### 4.3 Vetus — WS-Serie

Vetus (Niederlande) bietet eine kompakte Reihe von Kraftstofffiltern/Wasserabscheidern, die besonders bei europäischen Bootsbauern beliebt sind.

#### 4.3.1 Modellreihe

| Modell | Max. Durchfluss | Anschluss | Motor-PS |
|---|---|---|---|
| WS180 | 180 l/h | 3/8" BSP | bis 60 PS |
| WS360 | 360 l/h | 1/2" BSP | bis 120 PS |
| WS720 | 720 l/h | 3/4" BSP | bis 240 PS |
| WS750 | 750 l/h | 1" BSP | bis 260 PS |

#### 4.3.2 Filtereinsätze Vetus

| Teilenummer | Feinheit | Passend für |
|---|---|---|
| VT2606 | 10µm | WS180 |
| VT2611 | 30µm | WS180 |
| VT2606-360 | 10µm | WS360 |
| VT2611-360 | 30µm | WS360 |
| VT2606-720 | 10µm | WS720 |
| VT2611-720 | 30µm | WS720 |

**Besonderheiten Vetus:**
- Kompakte Bauform, ideal für enge Motorräume
- Aluminium-Gehäuse mit Epoxidbeschichtung
- Transparenter Becher mit Wasserstandsmarkierung
- Drain-Ventil mit Schlauchstutzen (sauberes Ablassen)
- Nicht-leitender Becher (keine galvanische Korrosion)

**Preise (Stand 2025/26):**
- WS180 Gehäuse: €120–€170
- WS720 Gehäuse: €250–€340
- Filtereinsatz VT2606 (10µm): €16–€24
- Dichtungssatz: €8–€12

### 4.4 Fleetguard (Cummins Filtration)

Fleetguard ist die Filtermarke von Cummins und Standard-OEM-Lieferant für Cummins-Motoren (QSB, QSC, QSM, QSL-Serie). Auch als Nachrüst-Option für andere Motoren geeignet.

#### 4.4.1 Relevante Modelle für Yachtbau

| Modell | Typ | Durchfluss | Feinheit | OEM für |
|---|---|---|---|---|
| FS1212 | Spin-On, mit Wasserabscheider | 170 l/h | 10µm | Cummins 4BT, 6BT |
| FS1242 | Spin-On, mit Wasserabscheider | 280 l/h | 10µm | Cummins QSB 5.9 |
| FS19816 | Spin-On, mit Wasserabscheider | 420 l/h | 5µm | Cummins QSC 8.3 |
| FS19732 | Spin-On, mit Wasserabscheider | 380 l/h | 5µm | Cummins QSB 6.7 |
| FS19765 | Spin-On, mit Wasserabscheider | 500 l/h | 5µm | Cummins QSM 11 |
| FS36259 | Spin-On, Common-Rail | 350 l/h | 2µm | Cummins QSB 6.7 CR |

**Besonderheiten:**
- Stratapore-Technologie: Mehrschichtiges Filtermedium
- AquaBlock: Wasserblock-Technologie (Element wird wasserabweisend bei Kontakt)
- NanoNet: Synthetisches Medium für 2µm-Filtration
- Integrierte Wasserstandssensoren bei vielen Modellen

**Preise (Stand 2025/26):**
- FS1242: €35–€50
- FS19816: €45–€65
- FS36259 (NanoNet): €65–€90

### 4.5 Mann+Hummel

Mann+Hummel (Deutschland) ist einer der weltweit größten Filterhersteller und liefert OEM an zahlreiche Motorhersteller.

#### 4.5.1 Relevante Serien

**WK-Serie (Wechselfilter Kraftstoff):**
| Modell | Typ | Passend für |
|---|---|---|
| WK 842/2 | Spin-On | Viele europäische Dieselmotoren |
| WK 854/6 | Einsatzfilter | Volvo Penta TAD, D-Serie |
| WK 940/5 | Spin-On mit Wasserabscheider | Universal marine |
| WK 1060/5 x | Einsatzfilter mit Wasserabscheider | Common-Rail-Anwendungen |
| WK 11 001 x | Einsatzfilter, Hochleistung | Moderne Common-Rail |

**PreLine-Serie (Vorfilter/Wasserabscheider):**
| Modell | Durchfluss | Feinheit |
|---|---|---|
| PreLine 150 | 150 l/h | 30µm + Wasserabscheidung |
| PreLine 270 | 270 l/h | 30µm + Wasserabscheidung |
| PreLine 420 | 420 l/h | 30µm + Wasserabscheidung |

**Preise (Stand 2025/26):**
- WK 842/2: €12–€18
- WK 940/5: €22–€32
- PreLine 270 Gehäuse: €180–€260
- PreLine 270 Einsatz: €20–€30

### 4.6 Delphi / CAV / Lucas

Historisch wichtig: CAV (Clayton-Abell-Vakuum) war über Jahrzehnte Standard bei britischen und französischen Bootsmotoren (Perkins, Ford/Lehman, BMC). Heute unter Delphi Technologies weitergeführt.

#### 4.6.1 CAV/Delphi Filter im Yachtbau

| Modell | Typ | Verbreitung |
|---|---|---|
| CAV 296 | Glas-Becher, Spin-On | Perkins 4.108, Ford Lehman |
| CAV 596 | Metall-Becher, Spin-On | Perkins 6.354, Range 4 |
| Delphi HDF296 | Nachfolger CAV 296 | Ersatzteilmarkt |
| Delphi HDF596 | Nachfolger CAV 596 | Ersatzteilmarkt |

**Historische Bedeutung:**
Tausende älterer Yachten (Baujahr 1970–2000) haben noch CAV-basierte Filtersysteme. Die Einsätze sind weiterhin verfügbar, aber ein Upgrade auf Racor/Separ wird bei Grundüberholung empfohlen.

### 4.7 Bosch

Bosch liefert primär Sekundärfilter (motormontiert) als OEM für viele Motorhersteller.

| Modell | Typ | OEM für |
|---|---|---|
| F 026 402 007 | Einsatzfilter | Diverse |
| F 026 402 016 | Spin-On | Diverse |
| N 2048 | Spin-On mit Wasserabscheider | Marine-Anwendungen |
| N 4438 | Einsatzfilter | Common-Rail |

### 4.8 OEM-Motorfilter (Sekundärfilter) — Wichtige Teilenummern

#### 4.8.1 Volvo Penta

| Motor | OEM-Filtereinsatz | Feinheit | Typ | Preis |
|---|---|---|---|---|
| D1-13 / D1-20 | 3840335 | 10µm | Spin-On | €18–€25 |
| D1-30 / D2-40 | 3840335 | 10µm | Spin-On | €18–€25 |
| D2-55 / D2-75 | 21718912 (ersetzt 3825133) | 5µm | Einsatz | €28–€40 |
| D3-110 / D3-150 | 21718912 | 5µm | Einsatz | €28–€40 |
| D4-225 / D4-260 / D4-300 | 21380475 (ersetzt 3583443) | 2µm | Einsatz | €35–€50 |
| D6-310 / D6-370 / D6-435 | 21380475 | 2µm | Einsatz | €35–€50 |
| D11 / D13 | 22988765 | 2µm | Einsatz | €45–€65 |

#### 4.8.2 Yanmar

| Motor | OEM-Filtereinsatz | Feinheit | Typ | Preis |
|---|---|---|---|---|
| 1GM10 / 2GM20 | 104500-55710 | 10µm | Spin-On | €15–€22 |
| 3GM30 / 3JH-Serie | 129470-55703 | 10µm | Spin-On | €15–€22 |
| 3JH5E | 129470-55703 | 10µm | Spin-On | €15–€22 |
| 4JH-Serie | 129470-55810 | 10µm | Spin-On | €18–€26 |
| 4LHA-Serie | 119773-55510 | 10µm | Spin-On | €22–€32 |
| 6LY-Serie | 119773-55510 | 10µm | Spin-On | €22–€32 |
| 6LPA-Serie | 119773-55510 | 10µm | Spin-On | €22–€32 |

#### 4.8.3 Caterpillar

| Motor | OEM-Filtereinsatz | Feinheit | Typ | Preis |
|---|---|---|---|---|
| C7.1 ACERT | 1R-0749 | 2µm | Spin-On | €35–€50 |
| C9.3 ACERT | 1R-0751 | 2µm | Spin-On | €38–€55 |
| C12.9 | 1R-0762 | 2µm | Spin-On | €42–€60 |
| C18 ACERT | 1R-0762 | 2µm | Spin-On | €42–€60 |
| C32 ACERT | 1R-1808 | 2µm | Spin-On | €55–€80 |

#### 4.8.4 MAN

| Motor | OEM-Filtereinsatz | Feinheit | Typ | Preis |
|---|---|---|---|---|
| D0834 / D0836 | 51.12503-0063 | 5µm | Einsatz | €30–€45 |
| D2676 | 51.12503-0086 | 2µm | Einsatz | €40–€60 |
| D2862 (V12) | 51.12503-0098 | 2µm | Einsatz | €50–€75 |

#### 4.8.5 Cummins

| Motor | OEM-Filtereinsatz (Fleetguard) | Feinheit | Typ | Preis |
|---|---|---|---|---|
| QSB 5.9 | FS1242 | 10µm | Spin-On | €35–€50 |
| QSB 6.7 | FS19732 / FS36259 (CR) | 5µm / 2µm | Spin-On | €45–€90 |
| QSC 8.3 | FS19816 | 5µm | Spin-On | €45–€65 |
| QSM 11 | FS19765 | 5µm | Spin-On | €50–€70 |
| QSK 19 | FS20007 | 2µm | Spin-On | €65–€95 |

#### 4.8.6 MTU (Rolls-Royce Power Systems)

| Motor | OEM-Filtereinsatz | Feinheit | Typ | Preis |
|---|---|---|---|---|
| 8V/10V 2000 | X00042421 | 2µm | Einsatz | €55–€80 |
| 12V/16V 2000 | X00042421 | 2µm | Einsatz | €55–€80 |
| 12V/16V 4000 | X00059893 | 2µm | Einsatz | €75–€120 |

---

## 5. Hersteller-Datenbank

### 5.1 Racor (Parker Hannifin — Filtration Division)

| Feld | Information |
|---|---|
| **Vollständiger Name** | Parker Hannifin Corporation, Racor Division |
| **Hauptsitz** | Modesto, California, USA |
| **Europazentrale** | Parker Hannifin Manufacturing Ltd, Hemel Hempstead, UK |
| **Website** | www.parker.com/racor |
| **Technischer Support Europa** | +44 (0) 1onal-Nummer siehe Website |
| **Gründung** | 1969 (Racor Industries), 1988 von Parker übernommen |
| **Marktposition** | Weltmarktführer marine Kraftstofffilter |
| **Modellreihen (Marine)** | Turbine-Serie (110A–731000), Spin-On (R-Serie), FBO (Polishing), Spinner II |
| **Preisbereich** | €80–€6.000 (Gehäuse), €12–€90 (Einsätze) |
| **Verfügbarkeit** | Weltweit, nahezu jeder Marine-Händler |
| **Stärken** | Breiteste Produktpalette, höchste Verfügbarkeit, Standard-Referenz |
| **Schwächen** | Premium-Preis, Aluminium-Gehäuse korrodiert in Salzluft ohne Pflege |

**Deutsche Händler:**
- SVB (Yacht-Zubehör): www.svb-marine.de
- Toplicht: www.toplicht.de
- Compass24: www.compass24.de
- AWN: www.awn.de
- Bukh-Bremen (Motorhersteller/Händler): www.bukh-bremen.de

### 5.2 SEPAR Filter GmbH

| Feld | Information |
|---|---|
| **Vollständiger Name** | SEPAR Filter GmbH |
| **Sitz** | Weyhe bei Bremen, Deutschland |
| **Website** | www.separ-filter.de |
| **Telefon** | +49 (0) 4203 4300-0 |
| **Gründung** | 1986 |
| **Marktposition** | Stark in Europa, besonders D/A/CH und Skandinavien |
| **Modellreihen** | SWK-2000 Serie (5 bis 130), SWK-2000/5U (Untertisch), Heizölfilter |
| **Preisbereich** | €120–€800 (Gehäuse), €15–€60 (Einsätze) |
| **Stärken** | Exzellente Wasserabscheidung, robuste deutsche Qualität, guter Service |
| **Schwächen** | Weniger international verfügbar, keine 2µm-Einsätze |

### 5.3 Vetus (Vetus Maxwell Group)

| Feld | Information |
|---|---|
| **Vollständiger Name** | Vetus Maxwell Group B.V. |
| **Sitz** | Schiedam, Niederlande |
| **Website** | www.vetus.com |
| **Telefon** | +31 (0) 10 2018920 |
| **Gründung** | 1951 |
| **Marktposition** | Breit aufgestellter Marine-Zulieferer, Filter als Teil des Sortiments |
| **Modellreihen** | WS-Serie (180–750), Inline-Filter |
| **Preisbereich** | €100–€400 (Gehäuse), €12–€30 (Einsätze) |
| **Stärken** | Kompakte Bauform, gutes Preis-Leistungs-Verhältnis, breites Händlernetz |
| **Schwächen** | Weniger spezialisiert als Racor/Separ, kleinere Auswahl |

### 5.4 Fleetguard (Cummins Filtration)

| Feld | Information |
|---|---|
| **Vollständiger Name** | Cummins Filtration (Marke: Fleetguard) |
| **Sitz** | Nashville, Tennessee, USA |
| **Website** | www.cumminsfiltration.com |
| **Marktposition** | OEM für Cummins-Motoren, stark im kommerziellen Bereich |
| **Modellreihen** | FS-Serie (Spin-On), Davco (Vorfilter), Fuel Pro |
| **Preisbereich** | €25–€150 (Spin-On-Elemente) |
| **Stärken** | Perfekte Abstimmung auf Cummins, NanoNet-Technologie, gute Forschung |
| **Schwächen** | Primär Spin-On, wenig eigenständige Gehäusesysteme für Nachrüstung |

### 5.5 Mann+Hummel

| Feld | Information |
|---|---|
| **Vollständiger Name** | MANN+HUMMEL GmbH |
| **Sitz** | Ludwigsburg, Deutschland |
| **Website** | www.mann-hummel.com |
| **Telefon** | +49 (0) 7141 98-0 |
| **Gründung** | 1941 |
| **Marktposition** | Einer der größten Filterhersteller weltweit, OEM für viele Motorhersteller |
| **Modellreihen** | WK-Serie, PreLine-Serie, PL-Serie |
| **Preisbereich** | €10–€300 (je nach System) |
| **Stärken** | Exzellente Filtermedien, breite OEM-Abdeckung, deutsche Qualität |
| **Schwächen** | Wenig marine-spezifische Gehäuse, primär Automotive/Truck adaptiert |

### 5.6 Delphi Technologies (ehem. CAV/Lucas)

| Feld | Information |
|---|---|
| **Vollständiger Name** | Delphi Technologies (seit 2023: BorgWarner Inc.) |
| **Sitz** | Auburn Hills, Michigan, USA |
| **Website** | www.delphiaftermarket.com |
| **Marktposition** | Historisch dominant bei britischen Motoren, Aftermarket |
| **Modellreihen** | HDF-Serie, Ersatz für CAV 296/596 |
| **Preisbereich** | €15–€80 |
| **Stärken** | Direkte Kompatibilität mit CAV-Altbestand, breite Verfügbarkeit |
| **Schwächen** | Technologisch nicht mehr führend, wird zunehmend durch Racor ersetzt |

### 5.7 Griffin (GS-Serie)

| Feld | Information |
|---|---|
| **Vollständiger Name** | Griffin Filters (Teil von Universal Silencer / CLARCOR, jetzt Parker) |
| **Marktposition** | Budget-Alternative zu Racor, in USA verbreitet |
| **Modellreihen** | GS078 (wie Racor 120A), GS178 (wie Racor 500FG), GS278 (wie Racor 1000FG) |
| **Preisbereich** | 20–30% günstiger als Racor-Äquivalente |
| **Besonderheit** | Einsätze sind kompatibel mit Racor-Gehäusen (und umgekehrt) |

### 5.8 Solas Marine (Spin-On-Adapter)

| Feld | Information |
|---|---|
| **Marktposition** | Spin-On-Adapter-Systeme als Racor-Alternative |
| **Stärken** | Günstig, universelle Spin-On-Kartuschen |
| **Schwächen** | Weniger Wasserabscheidung als Turbine-Systeme |

---

## 6. Filtereinsätze und Wechselintervalle

### 6.1 Materialien der Filtereinsätze

#### 6.1.1 Zellulose (Standard)

- **Aufbau**: Naturfasern (Zellstoff), imprägniert mit Phenolharz
- **Filterfeinheit**: Typisch 2–30µm (je nach Ausführung)
- **Wasserabscheidung**: Gut bei freiem Wasser, mäßig bei Emulsion
- **Lebensdauer**: 200–500 Betriebsstunden oder 12 Monate
- **Kosten**: €12–€40 je nach Größe
- **Nachteil**: Quillt bei starkem Wasserkontakt → Durchflusswiderstand steigt, kann Fasern freisetzen

#### 6.1.2 Synthetik (Hochleistung)

- **Aufbau**: Glasfaser oder Polyester, mehrschichtig
- **Filterfeinheit**: 2–10µm (schärferer Cutoff als Zellulose)
- **Wasserabscheidung**: Gut, definierte Hydrophobie
- **Lebensdauer**: 500–1.000 Betriebsstunden
- **Kosten**: €30–€90 je nach Größe
- **Vorteil**: Dimensionsstabil bei Wasserkontakt, höhere Beta-Werte

#### 6.1.3 Nylon-Sieb (wiederverwendbar)

- **Aufbau**: Feines Nylongewebe in Rahmen
- **Filterfeinheit**: 10µm (fest)
- **Wasserabscheidung**: Gering (nur mechanische Abscheidung)
- **Lebensdauer**: Unbegrenzt (reinigbar)
- **Kosten**: €25–€50 (einmalig)
- **Einsatz**: Notfall-Backup, extrem verschmutzter Diesel (häufiges Reinigen möglich)

#### 6.1.4 Zellulose + Wasserabsorber (Polymer)

- **Aufbau**: Zellulose-Medium mit eingebettetem Superabsorber-Polymer
- **Filterfeinheit**: 10µm
- **Wasserabscheidung**: Exzellent — absorbiert auch emulgiertes Wasser
- **Lebensdauer**: Kürzer als Standard-Zellulose (Absorber sättigt sich)
- **Kosten**: €25–€45
- **Einsatz**: Biodiesel (B7+), tropische Gewässer, bekannte Wasserproblematik

### 6.2 Wechselintervalle

#### 6.2.1 Empfohlene Intervalle (Hersteller)

| Filterhersteller | Einsatztyp | Intervall Stunden | Intervall Zeit |
|---|---|---|---|
| Racor | Zellulose (Turbine) | 250–500 h | 12 Monate |
| Racor | Synthetik (Turbine) | 500–1.000 h | 24 Monate |
| Separ | Standard-Einsatz | 250–500 h | 12 Monate |
| Vetus | Standard-Einsatz | 250 h | 12 Monate |
| Fleetguard | FS-Serie | Per Motorhersteller | 12 Monate |
| Motor-Feinfilter | OEM | 200–500 h | 12 Monate |

#### 6.2.2 Angepasste Intervalle nach Betriebsbedingungen

| Betriebsbedingung | Intervall-Multiplikator |
|---|---|
| Sauberer Diesel, Nordeuropa | ×1,0 (Standard) |
| Mittelmeer, moderate Qualität | ×0,75 |
| Tropen, variable Qualität | ×0,5 |
| Entwicklungsländer, fragliche Qualität | ×0,25–0,5 |
| Biodiesel >B7 | ×0,5 |
| Bekannte Dieselpest-Historie | ×0,25 |
| Tank mit Wasserbodenbelag | Sofort wechseln + Tank reinigen |

#### 6.2.3 Visuelle Indikatoren für Wechsel

| Indikator | Bedeutung | Aktion |
|---|---|---|
| Vakuummeter im gelben Bereich | Filter 50–70% zugesetzt | Wechsel planen (nächster Hafen) |
| Vakuummeter im roten Bereich | Filter >80% zugesetzt | Sofort wechseln |
| Wasser im Becher >1/3 | Wasserabscheider-Kapazität erschöpft | Wasser ablassen |
| Wasser im Becher dunkel/trüb | Möglicherweise Dieselpest | Wasser ablassen, Einsatz prüfen, ggf. Tank testen |
| Einsatz beim Ausbau schwarz | Normale Verschmutzung | Standard-Wechsel |
| Einsatz beim Ausbau schleimig | Biologische Kontamination | Einsatz + Gehäuse reinigen, Biozid in Tank |
| Einsatz beim Ausbau aufgequollen | Wassersättigung | Ursache Wasserquelle suchen |

### 6.3 Cross-Referenz: Filtereinsätze

| Racor | Separ (äquivalent) | Vetus (äquivalent) | Fleetguard | Feinheit |
|---|---|---|---|---|
| R12T | — | — | — | 10µm (110A/120A) |
| 2010TM-OR | 01010 (annähernd) | VT2606 (annähernd) | — | 10µm (500FG) |
| 2010SM-OR | — | — | — | 2µm (500FG) |
| 2040TM-OR | 02010 (annähernd) | — | — | 10µm (900FG) |
| 2020TM-OR | 02040-10 (annähernd) | — | — | 10µm (1000FG) |

**Wichtiger Hinweis:** Separ- und Vetus-Einsätze sind NICHT direkt kompatibel mit Racor-Gehäusen und umgekehrt. Die Tabelle zeigt funktionale Äquivalente (ähnliche Leistungsdaten), keine Austauschbarkeit.

---

## 7. Einbau und Installation

### 7.1 Systemanordnung

**Korrekte Reihenfolge im Kraftstoffsystem:**

```
Tank
  → Tankabsperrventil (manuell, feuerbeständig)
    → Saugkorb/Tankfilter (100µm Mesh)
      → Kraftstoffleitung (Kupfer oder CE-zugelassener Schlauch)
        → VORFILTER/WASSERABSCHEIDER (Racor/Separ/Vetus)
          → Kraftstoff-Förderpumpe (mechanisch oder elektrisch)
            → FEINFILTER (motormontiert, 2–10µm)
              → Einspritzpumpe / Common-Rail-Pumpe
                → Injektoren
                  → Rücklaufleitung → Tank
```

### 7.2 Einbaurichtlinien

#### 7.2.1 Position

- **Zugänglichkeit**: Einsatzwechsel muss ohne Werkzeug-Akrobatik möglich sein
- **Senkrecht**: Filter/Abscheider muss senkrecht montiert sein (Schwerkraft-Wasserabscheidung)
- **Toleranz**: Maximal 5° Neigung, besser <2°
- **Höhe**: Idealerweise unterhalb der Tankunterkante (Schwerkraftzufuhr)
- **Abstand zum Motor**: Mindestens 300 mm (Vibration, Hitze)
- **Spritzwasserschutz**: Kein direkter Kontakt mit Bilgenwasser
- **Beleuchtung**: Transparenter Becher muss inspizierbar sein

#### 7.2.2 Leitungsführung

- **Material Saugseite**: Kupfer (15mm od. 3/8"), Stahlrohr, oder CE-zugelassener Kraftstoffschlauch (ISO 7840 A1)
- **NICHT verwenden**: PVC-Schlauch, Gartenschlauch, nicht-zugelassene Kunststoffe
- **Durchmesser**: Nie kleiner als Filteranschluss (Druckverlust!)
- **Bögen**: Sanft, keine Knicke (Kavitationsgefahr auf der Saugseite)
- **Verbindungen**: Minimieren — jede Verbindung ist eine potenzielle Leckstelle

#### 7.2.3 Entlüftung

Nach jedem Filterwechsel muss das System entlüftet werden:
1. Neuen Einsatz einsetzen, Gehäuse schließen
2. Entlüftungsschraube am Filtergehäuse öffnen (falls vorhanden)
3. Handpumpe betätigen (Racor T-Handle, Motor-Handpumpe, oder elektrische Pumpe)
4. Pumpen bis blasenfreier Kraftstoff aus der Entlüftungsschraube tritt
5. Entlüftungsschraube schließen
6. Entlüftungsschraube am Feinfilter öffnen, pumpen bis blasenfrei
7. Entlüftungsschraube am Einspritzpumpen-Eingang öffnen (falls vorhanden)
8. Motor starten — kurzes Stottern ist normal
9. Nach 30 Sekunden: Filterverschraubungen auf Dichtheit prüfen

**Bei Common-Rail-Motoren:**
Viele moderne Common-Rail-Systeme haben eine automatische Entlüftung (Self-Bleeding). Trotzdem Racor/Vorfilter manuell entlüften, um Lufteintrag in die Hochdruckpumpe zu minimieren.

### 7.3 Dual-Filter-Installation

**Für Blauwasser- und Kategorie-A-Yachten empfohlen:**

```
Tank
  → Y-Ventil oder 3-Wege-Ventil
    ↙         ↘
  Filter A    Filter B
    ↘         ↙
  Y-Ventil oder 3-Wege-Ventil
    → Motor
```

**Umschaltventile:**
- Racor 75500MAX Manifold (empfohlen): Kugelventile in Edelstahl
- Eigenbau: Zwei 3-Wege-Ventile (Kugelhähne, Messing oder Edelstahl)
- **ACHTUNG**: Umschalten nie bei Volllast — kurz Gas wegnehmen, umschalten, wieder Gas geben

### 7.4 Elektrische Installation (Wasserstandssensor)

**Racor RK21069 Wasserstandssensor:**
- Gewindeanschluss am Becherboden
- Reed-Kontakt schließt bei Wasserstand
- Verkabelung: Signal → Alarmgeber (Summer/LED) → Masse
- Betriebsspannung: 12V oder 24V (je nach Version)
- Stromaufnahme: <100 mA

**Empfohlene Verdrahtung:**
- Kabelquerschnitt: 0,75 mm² (marine-Litze, verzinnt)
- Sicherung: 1A (Masse-seitig)
- Alarmgeber: LED-Warnleuchte am Steuerstand, optional Summer
- Farbe Kabel: Braun (Signal), Schwarz (Masse) — nach ISO 10133

### 7.5 Typische Einbaufehler

| Fehler | Folge | Vermeidung |
|---|---|---|
| Filter waagerecht montiert | Keine Wasserabscheidung | Immer senkrecht montieren |
| Zu kleine Leitungsquerschnitte | Kavitation, Luftziehen | Min. ¾" für Motoren >50 PS |
| Starre Verrohrung ohne Flexstück | Vibrationsbruch, Leck | Flexschlauch vor/nach Filter |
| Filter direkt am Motor (Vibration) | Lockere Verschraubungen | Auf Schott montieren, vibrationsfrei |
| Transparenter Becher nicht inspizierbar | Wasser wird nicht erkannt | Freie Sicht auf Becher sicherstellen |
| Sammelbecher-Drain über Bilge geleitet | Diesel in der Bilge | Auffangbehälter verwenden |
| Kein Absperrventil vor dem Filter | Diesel läuft beim Wechsel aus | Ventil nachrüsten |
| Kupferleitung direkt am Alu-Gehäuse | Galvanische Korrosion | Messingadapter verwenden |
| Entlüftungsschraube nicht zugänglich | Entlüftung erschwert | Zugang freihalten |
| Vakuummeter-Anschluss nicht genutzt | Verschmutzung nicht erkennbar | Vakuummeter nachrüsten (€50) |

### 7.6 Werkzeug für Installation und Wartung

**Grundwerkzeug:**
- Gabelschlüssel-Satz (metrisch + Zoll für Racor-Anschlüsse)
- Rohrzangen (für BSP-Gewinde bei Separ/Vetus)
- Bandschlüssel oder Filterschlüssel (Racor-spezifisch)
- PTFE-Band (Gewindedichtung)
- Rohrschneider (Kupfer)
- Bördelwerkzeug (Kupferleitungen)
- Schlauchschellen-Zange (für Messing-Schlauchschellen)

**Verbrauchsmaterial für Installation:**
- Kraftstoffschlauch ISO 7840 A1 (Meterware)
- Kupferrohr 10mm oder 12mm (marine-spezifisch)
- Messing-Verschraubungen (Reduzierstücke, Winkel, Schottdurchführungen)
- Schlauchschellen (Edelstahl, Doppelschellen für Kraftstoff)
- Auffangwanne (Kunststoff, säurebeständig)
- Öl-Bindevlies (für den Motorraum)

### 7.7 Prüfung nach Installation

**Checkliste Erstinstallation:**
```
□ Filtergehäuse senkrecht? (Wasserwaage)
□ Alle Verschraubungen handfest + ¼ Umdrehung?
□ O-Ringe korrekt eingelegt?
□ Keine Kupfer-Aluminium-Direktverbindung?
□ Tankventil funktioniert?
□ Saugleitung stetig fallend zum Tank (keine Hochpunkte)?
□ Druckleitung zum Motor ohne Knicke?
□ Vakuummeter angeschlossen (falls vorhanden)?
□ Wasserstandssensor verkabelt (falls vorhanden)?
□ System entlüftet?
□ Motor gestartet — kein Stottern?
□ 5 Minuten Lauf — keine Tropfen an Verschraubungen?
□ Vakuummeter zeigt <5 kPa bei Leerlauf?
□ Sammelbecher klar — kein Wasser sichtbar?
```

---

## 8. Wartung und Instandhaltung

### 8.1 Regelmäßige Wartung

#### 8.1.1 Tägliche Kontrolle (bei Betrieb)

- Transparenten Becher auf Wasserstand kontrollieren
- Vakuummeter ablesen (falls installiert)
- Kraftstoffleitungen auf Feuchtigkeit/Tropfen kontrollieren
- Bei Motor-Unregelmäßigkeiten: Filter zuerst prüfen

#### 8.1.2 Wöchentliche Wartung

- Wasser aus dem Sammelbecher ablassen (Drain-Ventil öffnen bis klarer Diesel kommt)
- Abgelassenes Wasser in Auffangbehälter (Entsorgung an Land!)
- Becher auf Verfärbung prüfen (Dieselpest-Früherkennung)
- Montageschrauben auf Festsitz prüfen

#### 8.1.3 Filterwechsel (alle 200–500 h oder jährlich)

**Werkzeug:**
- Filterschlüssel passend zum Gehäuse (Racor: großer Bandschlüssel oder spezifisch)
- Auffangschale (min. 1 Liter Fassungsvermögen)
- Lappen, Öl-Bindevlies
- Neuer Einsatz (korrekte Teilenummer!)
- Neuer O-Ring (im Einsatz-Kit -OR enthalten, sonst separat)
- Vaseline oder Diesel für O-Ring-Schmierung
- Optional: Handschuhe (Nitrile)

**Ablauf Racor Turbine-Serie:**
1. Tankventil schließen
2. Auffangschale unter Filter platzieren
3. T-Handle oder Becherverschraubung lösen
4. Becher absenken — Diesel läuft aus
5. Alten Einsatz herausziehen, in Tüte entsorgen
6. Becher reinigen (Diesel + Lappen, bei Biofilm: Bürste + Biozid)
7. O-Ring-Sitz am Gehäuse reinigen
8. Neuen O-Ring leicht mit Diesel einreiben
9. Neuen Einsatz einsetzen (auf korrekte Orientierung achten!)
10. Becher aufsetzen und festziehen (handfest + 1/4 Umdrehung, NICHT überdrehen)
11. Tankventil öffnen
12. System entlüften (siehe 7.2.3)
13. Motor starten, Dichtheit prüfen
14. Alten Einsatz und abgelassenes Dieselwasser fachgerecht entsorgen

### 8.2 Saisonale Wartung

#### 8.2.1 Einwinterung (Saisonende)

1. Tank randvoll füllen (minimiert Kondensation über Winter)
2. Biozid hinzufügen (z.B. Grotamar 82, Dosierung: 1:4000 = 250 ml auf 1.000 Liter)
3. Motor laufen lassen, damit behandelter Diesel das System durchflutet (15 Min.)
4. Neuen Filtereinsatz einsetzen (sauberer Filter über Winter = weniger Bakteriennährboden)
5. Wasser aus Sammelbecher ablassen

#### 8.2.2 Auswinterung (Saisonbeginn)

1. Wasser aus Sammelbecher ablassen
2. Kraftstoff visuell prüfen (Tankprobe: klar? Geruch?)
3. Filtereinsatz kontrollieren (wenn bei Einwinterung gewechselt: OK lassen)
4. System entlüften
5. Motor starten, 15 Minuten laufen lassen
6. Filter auf Dichtheit kontrollieren

### 8.3 Gehäuse-Wartung

#### 8.3.1 Aluminium-Gehäuse (Racor Standard, Separ)

- **Jährlich**: Äußere Oberfläche mit Korrosionsschutz behandeln (Lanocote, CorrosionX)
- **Alle 3 Jahre**: O-Ring-Sitze prüfen, beschädigte O-Ringe ersetzen
- **Alle 5 Jahre**: Gewinde prüfen, Gehäuse auf Korrosion inspizieren
- **Salzwasser**: Häufiger kontrollieren, Aluminium korrodiert galvanisch!

#### 8.3.2 Edelstahl-Gehäuse (Racor SS-Serie)

- **Jährlich**: Oberfläche reinigen, auf Lochfraß (Pitting) prüfen
- **Geringerer Wartungsaufwand** als Aluminium
- **Empfehlung**: 316L-Edelstahl für Salzwasserumgebung

#### 8.3.3 Transparenter Becher

- **Material**: Polycarbonat oder Nylon
- **Empfindlich gegen**: Diesel-Additive, Lösungsmittel, UV-Strahlung
- **Lebensdauer**: 5–8 Jahre, dann spröde (Bruchgefahr!)
- **Austausch**: Bei Vergilbung, Trübung, Mikrorissen → sofort tauschen
- **Alternativ**: Metallbecher für Motorraum-Montage (sicherer, aber nicht inspizierbar)

### 8.4 Troubleshooting Entlüftungsprobleme

| Problem | Ursache | Lösung |
|---|---|---|
| System lässt sich nicht entlüften | Tankventil geschlossen | Ventil öffnen |
| Luft kommt ständig nach | Leck in Saugleitung | Alle Verbindungen prüfen, abdichten |
| Luft im Becher nach Filterwechsel | O-Ring nicht korrekt sitzend | O-Ring prüfen, ggf. ersetzen |
| Diesel tritt am Gehäuse aus | Becher nicht fest, O-Ring defekt | Anziehen oder O-Ring tauschen |
| Motor springt nach Wechsel nicht an | Luft im System | Komplettes System entlüften |

---

## 9. Dieselpest — Mikrobiologische Kontamination

### 9.1 Ursachen und Begünstigende Faktoren

#### 9.1.1 Der Biodiesel-Faktor

Seit der EU-Norm EN 590 enthält handelsüblicher Diesel bis zu 7% FAME (Fatty Acid Methyl Esters = Biodiesel). Dieser Biodiesel-Anteil:
- Ist **hygroskopisch** (zieht Wasser an)
- Bietet **Nährstoffe** für Mikroorganismen (Fettsäuren)
- Hat eine **geringere Lagerstabilität** als Mineralöl-Diesel
- Führt zu **schnellerem Wachstum** der Dieselpest

**Zeitlicher Zusammenhang:**
- Vor 2000 (B0, kein Biodiesel): Dieselpest selten, primär Langfahrer in den Tropen
- 2005–2010 (B5, 5% Biodiesel): Zunahme der Fälle
- Ab 2010 (B7, 7% Biodiesel): Dieselpest ist ein Standardproblem geworden
- Künftig geplant (B10, B20): Problem wird sich verschärfen

#### 9.1.2 Der Temperatur-Faktor

- Mittelmeer-Sommer: Motorraum 40–60°C, Tank 30–45°C → ideal für Wachstum
- Nordeuropa-Winter: <10°C → Wachstum verlangsamt, aber nicht gestoppt
- Tropen: Ganzjährig 25–35°C → Dauerproblem

#### 9.1.3 Der Standzeit-Faktor

- Wochenendsegeln (5 Tage Standzeit): Geringes Risiko
- Monatliche Nutzung: Mittleres Risiko
- Winterlager (5–7 Monate): Hohes Risiko ohne Biozid
- Yacht am Liegeplatz, selten bewegt: Sehr hohes Risiko

### 9.2 Diagnose

#### 9.2.1 Schnelltest (Bordmittel)

1. **Tankprobe entnehmen** (vom Tankboden, über Drain oder Absaugen)
2. **Visuell beurteilen**: Klar = OK, trüb = Wasser/Emulsion, Flocken/Schleim = Dieselpest
3. **Geruchstest**: Faulig, schweflig, „Kanalisation" = fortgeschrittene Kontamination
4. **Filtereinsatz inspizieren**: Schwarzer/brauner Schleim = biologisch

#### 9.2.2 Labortest (professionell)

**Dip-Slide-Test (Eintauchnährboden):**
- Kosten: €15–€25 pro Test
- Durchführung: Nährboden in Kraftstoff tauchen, 48–72h bei Raumtemperatur inkubieren
- Auswertung: Koloniedichte mit Referenzskala vergleichen
- Produkte: Easicult TTC + Combi, Liqui-Cult, Microb-Check
- Genauigkeit: Ordnungsgrößen-Schätzung (10², 10⁴, 10⁶ CFU/ml)

**ATP-Test (Adenosintriphosphat-Lumineszenz):**
- Kosten: €30–€50 pro Test
- Durchführung: Probe in Messgerät, Ergebnis in Sekunden
- Genauigkeit: Quantitativ (RLU = Relative Light Units)
- Geräte: Hygiena SystemSURE, 3M Clean-Trace
- Vorteil: Sofortergebnis, objektiv

**Laboranalyse (IP 385 / ASTM D6469):**
- Kosten: €80–€200 pro Probe
- Durchführung: Einschicken an Labor (z.B. SGS, Bureau Veritas, Intertek)
- Ergebnis: CFU/ml, Artbestimmung, Empfehlung
- Dauer: 5–10 Arbeitstage

### 9.3 Bekämpfung

#### 9.3.1 Biozide (chemische Behandlung)

| Produkt | Wirkstoff | Dosierung (Schock) | Dosierung (Erhaltung) | Preis |
|---|---|---|---|---|
| Grotamar 82 | MBO + CMIT | 1:1.000 (1 ml/l) | 1:4.000 (0,25 ml/l) | €35–€50 / 500ml |
| Biobor JF | 2,2-Dioxo-1,3-dioxolan | 1:2.700 (0,37 ml/l) | 1:5.400 (0,19 ml/l) | €40–€60 / 473ml |
| MarineLine DFC | Quaternäre Amine | 1:1.000 | 1:2.000 | €30–€45 / 500ml |
| Liqui Moly Diesel-Schutz | CMIT/MIT | 1:1.000 | 1:2.000 | €12–€18 / 150ml |
| Star Tron Enzyme | Enzym-basiert | Per Herstellerangabe | Per Herstellerangabe | €20–€30 / 473ml |

**Anwendung Schockbehandlung:**
1. Biozid in Tankstutzen geben (VOR dem Tanken)
2. Diesel nachtanken (Durchmischung)
3. Motor 30 Minuten laufen lassen (Verteilung im System)
4. 24 Stunden wirken lassen
5. Filtereinsatz wechseln (abgetötete Biomasse verstopft den Filter!)
6. Ggf. zweite Wechsel nach 50 Betriebsstunden

**ACHTUNG**: Biozide sind umweltgefährdend! Abgelassenes Dieselwasser NIEMALS über Bord — immer fachgerecht entsorgen.

#### 9.3.2 Mechanische Reinigung (schwere Fälle)

Bei Stadium 3–4 reicht Biozid allein nicht aus:

1. **Tank entleeren** (Absaugen, nicht über Leitungen — Biofilm-Verstopfungsgefahr)
2. **Tank öffnen** (Inspektionsluke oder Mannloch)
3. **Biofilm mechanisch entfernen** (Hochdruckreiniger, Bürsten)
4. **Mit Biozid-Lösung ausspülen** (hohe Konzentration)
5. **Trocknen lassen** (belüften, ggf. Heizlüfter)
6. **Tankbeschichtung prüfen** (MIC-Korrosion?)
7. **Alle Filter und Leitungen erneuern**
8. **Sauberen Diesel einfüllen** mit Erhaltungsdosierung Biozid
9. **Dip-Slide-Test** nach 2 Wochen wiederholen

**Kosten Tanksanierung:**
- Segelyacht (200–400 l Tank): €500–€2.000
- Motoryacht (1.000–5.000 l Tank): €2.000–€8.000
- Superyacht (10.000+ l): €5.000–€25.000

### 9.3.3 UV-Behandlung (alternative Methode)

UV-C-Behandlung des Kraftstoffs als biozidfreie Alternative:

**Funktionsprinzip:**
- UV-C-Strahlung (254 nm) zerstört die DNA der Mikroorganismen
- Kraftstoff wird durch eine UV-Kammer gepumpt
- Kein chemischer Rückstand im Diesel

**Produkte:**
- BioGuard Marine UV-System: €1.200–€2.500
- Durchfluss: 50–200 l/h (Poliersystem-Integration)
- Energiebedarf: 15–40W (12V/24V)

**Vorteile:**
- Kein chemischer Eingriff in den Kraftstoff
- Keine Dosierungsprobleme
- Dauerhafte Wirkung bei permanentem Betrieb
- Umweltfreundlicher als Biozide

**Nachteile:**
- Hohe Anschaffungskosten
- UV-Lampe muss alle 8.000–10.000 h getauscht werden (€80–€150)
- Wirkt nur auf durchfließenden Kraftstoff (nicht im stehenden Tank)
- Trüber Kraftstoff reduziert die UV-Penetration (Vorfilter erforderlich)
- Im Yachtbau noch wenig verbreitet

**Empfehlung:** Sinnvoll als Ergänzung zum Poliersystem auf Langfahrt-Yachten. Ersetzt aber nicht die Biozid-Erstbehandlung bei bestehender Kontamination.

### 9.3.4 Thermische Behandlung

Erhitzen des Kraftstoffs auf >60°C tötet die meisten Dieselpest-Organismen ab:

**Methode:**
- Kraftstoff über Wärmetauscher (Motor-Kühlwasser) aufheizen
- Integration in Poliersystem
- Temperatur muss >60°C für >30 Minuten gehalten werden

**Limitierungen:**
- Hitze beschleunigt die Diesel-Oxidation (Alterung)
- Nicht alle Organismen sterben bei 60°C (thermophile Bakterien überleben bis 80°C)
- Sporen (Pilze) überleben auch höhere Temperaturen
- Nur als Ergänzung, nicht als alleinige Maßnahme

### 9.3.5 Enzymatische Behandlung

Neuerer Ansatz mit Enzym-basierten Produkten:

**Produkte:**
- Star Tron Enzyme Fuel Treatment: Enzyme spalten Biomasse in brennbare Bestandteile
- SOD (Sludge & Odor Destroyer): Ähnliches Prinzip

**Vorteile:**
- Kein toxisches Biozid
- Biomasse wird in brennbare Substanzen umgewandelt (nicht nur abgetötet)
- Kein Filterverstoßungsrisiko durch abgetötete Biomasse

**Nachteile:**
- Geringere Nachweisbasis als klassische Biozide
- Wirksamkeit bei schwerem Befall fraglich
- Teurer als konventionelle Biozide

**Empfehlung:** Als Ergänzung zu Bioziden oder für leichte Fälle. Bei schwerem Befall: Klassisches Biozid bevorzugen.

### 9.4 Prävention

**Goldene Regeln gegen Dieselpest:**
1. **Tank immer voll halten** (wenig Luftraum = wenig Kondensation)
2. **Biozid prophylaktisch** (Erhaltungsdosierung bei jeder Betankung)
3. **Wasser regelmäßig ablassen** (wöchentlich Sammelbecher, monatlich Tankdrain)
4. **Filter rechtzeitig wechseln** (nicht überreizen)
5. **Kraftstoff umwälzen** (Poliersystem oder regelmäßiger Motorbetrieb)
6. **Tanken an seriösen Stellen** (große Marinas, bekannte Lieferanten)
7. **Tankprobe testen** (Dip-Slide 2× jährlich)
8. **Belüftung Kraftstoffanlage** (Entlüftungsfilter am Tank gegen Feuchtigkeitseintrag)

---

## 10. Fehlerbild-Atlas

### 10.1 Fehlerbild F-01: Verstopfter Filtereinsatz (normal)

**Erscheinungsbild:**
- Einsatz gleichmäßig dunkelbraun bis schwarz gefärbt
- Keine Schleimbildung, keine Klumpen
- Vakuummeter zeigt erhöhten Unterdruck

**Ursache:**
- Normale Verschmutzung durch Diesel-Verunreinigungen
- Oxidationsprodukte, Rost, Feinstaub

**Bewertung:** Normal, Routinewechsel

**Maßnahme:**
- Einsatz wechseln
- Intervall beibehalten oder leicht verkürzen

**AYDI-Confidence:** documented

### 10.2 Fehlerbild F-02: Biologisch kontaminierter Einsatz (Dieselpest)

**Erscheinungsbild:**
- Einsatz mit schwarzem/braunem Schleim überzogen
- Schleimige Konsistenz beim Anfassen
- Fauliger Geruch
- Sammelbecher-Wasser dunkelbraun/schwarz, ggf. Flocken

**Ursache:**
- Mikrobiologisches Wachstum (Hormoconis resinae, Bakterien)
- Zu viel Wasser im System, lange Standzeiten

**Bewertung:** Ernsthaft, Handlungsbedarf

**Maßnahme:**
1. Einsatz wechseln
2. Gehäuse gründlich reinigen
3. Dip-Slide-Test des Tanks
4. Biozid-Schockbehandlung
5. Nach 50h erneut Einsatz prüfen
6. Bei schwerem Befall: Tank-Sanierung

**AYDI-Confidence:** documented

### 10.3 Fehlerbild F-03: Wasserdurchbruch

**Erscheinungsbild:**
- Sammelbecher randvoll Wasser
- Wasser hat Filterelement erreicht
- Einsatz aufgequollen, verformt
- Motor stottert oder stirbt ab

**Ursache:**
- Große Wassermenge im Tank (undichter Einfüllstutzen, Kondensation)
- Sammelbecher wurde nicht regelmäßig entleert
- Defekter Wasserstandssensor (kein Alarm)

**Bewertung:** Kritisch, Motorgefährdung

**Maßnahme:**
1. Motor sofort abstellen
2. Sammelbecher leeren
3. Einsatz sofort wechseln (aufgequollener Einsatz ist wirkungslos)
4. Tank auf Wasserquelle untersuchen
5. Tankwasser ablassen
6. System komplett entlüften
7. Bei Common-Rail: Wasserfreiheit am Motorfilter-Eingang bestätigen

**AYDI-Confidence:** documented

### 10.4 Fehlerbild F-04: Luftziehen am Filter

**Erscheinungsbild:**
- Blasen im Sammelbecher sichtbar
- Motor stottert unter Last
- Unregelmäßiger Leerlauf
- Vakuummeter zeigt schwankende Werte

**Ursache:**
- Undichter O-Ring am Gehäuse
- Lockere Becherverbindung
- Porös gewordener Kraftstoffschlauch auf der Saugseite
- Undichte Anschlussverschraubung

**Bewertung:** Ernsthaft, beeinträchtigt Motorzuverlässigkeit

**Maßnahme:**
1. Alle Verschraubungen am Filtergehäuse nachziehen
2. O-Ring prüfen, ggf. ersetzen
3. Saugleitungen Stück für Stück prüfen (Seifenwasser-Test oder Schlauchklemmen-Test)
4. Transparenter Becher auf Risse prüfen
5. Dichtheitstest: Handpumpe betätigen, Vakuum beobachten (muss halten)

**AYDI-Confidence:** documented

### 10.5 Fehlerbild F-05: Dichtungsleck am Filtergehäuse

**Erscheinungsbild:**
- Dieseltropfen oder -film am Gehäuse
- Geruch nach Diesel im Motorraum
- Möglicherweise Diesel in der Bilge

**Ursache:**
- O-Ring alt, verhärtet, eingerissen
- Becher nicht korrekt angezogen
- Gewinde am Gehäuse beschädigt
- Transparenter Becher verzogen (Hitze, UV, Alter)

**Bewertung:** Ernsthaft bis kritisch (Brandgefahr!)

**Maßnahme:**
1. Tankventil schließen
2. Leck lokalisieren
3. O-Ring ersetzen
4. Becher auf Verformung prüfen, ggf. ersetzen
5. Gewinde prüfen, ggf. Gewindedichtband (PTFE) verwenden
6. Dieselreste im Motorraum aufnehmen (Brandschutz!)

**AYDI-Confidence:** documented

### 10.6 Fehlerbild F-06: Falsche Filtergröße / falscher Einsatz

**Erscheinungsbild:**
- Einsatz sitzt nicht korrekt im Gehäuse
- Spaltmaße zwischen Einsatz und Gehäuse
- Bypass-Strömung um den Filter herum
- Trotz neuem Filter: Verschmutzung am Motorfilter

**Ursache:**
- Falscher Einsatz bestellt (z.B. 2010 statt 2020)
- Nachbau-Einsatz mit abweichenden Maßen
- Fehlende oder falsche Dichtung im Einsatz

**Bewertung:** Ernsthaft (kein Filterschutz!)

**Maßnahme:**
1. Teilenummer prüfen (Gehäuse-Etikett → korrekte Einsatz-Nummer)
2. Korrekten Einsatz beschaffen
3. Bei Nachbauten: Maße mit Original vergleichen
4. Motor-Feinfilter überprüfen (Bypass-Schmutz könnte dort gelandet sein)

**AYDI-Confidence:** documented

### 10.7 Fehlerbild F-07: Schnelle Wiederverstopfung nach Wechsel

**Erscheinungsbild:**
- Neuer Einsatz verstopft innerhalb von Stunden oder wenigen Betriebsstunden
- Vakuummeter steigt rapide
- Motorleistung fällt schnell ab

**Ursache:**
- Massive Tankverschmutzung (aufgewühlte Sedimente)
- Akute Dieselpest
- Rost/Schuppen vom Tank (Tankkorrosion)
- Defekte Tankbeschichtung (Abblätterung)
- Falsche Filterfeinheit (zu fein für den Verschmutzungsgrad)

**Bewertung:** Kritisch — systemisches Problem, nicht nur Filterproblem

**Maßnahme:**
1. Zunächst gröberen Einsatz verwenden (30µm statt 10µm)
2. Tankprobe entnehmen und analysieren
3. Tank auf Korrosion/Beschichtungsschäden inspizieren
4. Bei Dieselpest: Biozid-Schockbehandlung
5. Ggf. Tank professionell reinigen lassen
6. Kraftstoff-Poliersystem erwägen

**AYDI-Confidence:** documented

### 10.8 Fehlerbild F-08: Paraffin-Ausscheidung (Winterdiesel-Problem)

**Erscheinungsbild:**
- Weißliche, wachsartige Ablagerungen auf dem Filtereinsatz
- Filter verstopft bei niedrigen Temperaturen
- Motor springt nicht an bei Kälte

**Ursache:**
- Sommerdiesel bei Temperaturen unter seinem Cloud Point (ca. -6 bis -10°C)
- Unzureichender Kälteschutz des Diesels
- Kein beheizter Kraftstofffilter

**Bewertung:** Saisonal bedingt, vorhersehbar

**Maßnahme:**
1. Winterdiesel tanken (Cloud Point ca. -22°C)
2. Diesel-Fließverbesserer (Cold Flow Improver) zugeben
3. Beheizten Filterkopf nachrüsten (Racor Option)
4. Motorraum-Heizung installieren
5. Paraffin-Ablagerungen im Filter lösen sich bei Erwärmung auf

**AYDI-Confidence:** estimated

### 10.9 Fehlerbild F-09: Galvanische Korrosion am Filtergehäuse

**Erscheinungsbild:**
- Weiße, pulvrige Korrosion am Aluminium-Gehäuse
- Korrosion besonders an der Verbindung zu Kupferleitungen
- Gehäuse wird porös

**Ursache:**
- Kontakt von Aluminium (Gehäuse) mit Kupfer (Leitung) + Elektrolyt (Kondenswasser, Bilgenwasser)
- Salzluft im Motorraum
- Fehlende Isolierung zwischen ungleichen Metallen

**Bewertung:** Langfristig, Gehäuseversagen möglich

**Maßnahme:**
1. Messingadapter zwischen Aluminium und Kupfer verwenden
2. Gehäuse mit Korrosionsschutz behandeln (CorrosionX, Lanocote)
3. Bei schwerem Befall: Gehäuse ersetzen (Edelstahl-Version empfohlen)
4. Bilgenwasserstand kontrollieren (Gehäuse darf nicht im Wasser stehen)

**AYDI-Confidence:** documented

### 10.10 Fehlerbild F-10: Vakuummeter zeigt dauerhaft hohen Unterdruck

**Erscheinungsbild:**
- Vakuummeter im roten Bereich trotz neuem Filter
- Motor hat Leistungsverlust
- Ggf. Luft im System

**Ursache:**
- Verstopfter Tankansaugkorb (100µm Sieb im Tank)
- Abgeknickte oder verstopfte Saugleitung
- Zu kleine Leitungsquerschnitte
- Tankentlüftung blockiert (Tank zieht Vakuum)
- Defektes Vakuummeter

**Bewertung:** Ernsthaft — Problem liegt vor dem Filter

**Maßnahme:**
1. Vakuummeter kalibrieren / tauschen (Ausschluss)
2. Tankentlüftung prüfen (Einfüllstutzen öffnen, Vakuum beobachten)
3. Saugleitung durchblasen (Druckluft)
4. Tankansaugkorb reinigen (erfordert ggf. Tankzugang)
5. Leitungsquerschnitte prüfen (min. ¾" für Motoren >50 PS)

**AYDI-Confidence:** documented

### 10.11 Fehlerbild F-11: Diesel-Schaum im Sammelbecher

**Erscheinungsbild:**
- Schaumbildung im transparenten Becher
- Diesel erscheint milchig-schaumig
- Möglicherweise Überdosierung von Additiven erkennbar

**Ursache:**
- Überdosierung von Diesel-Additiven (Biozid, Fließverbesserer)
- Tensid-Verunreinigung (Reinigungsmittel im Tank)
- Starkes Emulgieren von Wasser durch Seegang bei Biodiesel
- Kavitation an der Saugseite (Luft wird eingezogen und emulgiert)

**Bewertung:** Mäßig bis ernsthaft (je nach Ursache)

**Maßnahme:**
1. Additiv-Dosierung überprüfen
2. Tankhistorie klären (Reinigungsmittel verwendet?)
3. Bei Kavitation: Saugseite auf Luftlecks prüfen
4. Diesel absitzen lassen (Schaum löst sich)
5. Bei Tensid-Verunreinigung: Tank spülen

**AYDI-Confidence:** estimated

### 10.12 Fehlerbild F-12: Kraftstoffleck an Filterverschraubungen unter Vibration

**Erscheinungsbild:**
- Intermittierendes Tropfen bei laufendem Motor
- Leitungsverschraubungen am Filterein-/ausgang arbeiten sich locker
- Vibrationsmarkierungen an Rohrverbindungen

**Ursache:**
- Filter nicht schwingungsfrei montiert
- Starre Verrohrung ohne Flexibilitätskompensation
- Nicht gesicherte Verschraubungen

**Bewertung:** Ernsthaft (Brandgefahr, Dieselverlust)

**Maßnahme:**
1. Flexible Kraftstoffschlauch-Stücke zwischen starrer Leitung und Filter einsetzen
2. Filter auf Gummipuffer montieren (schwingungsdämpfend)
3. Verschraubungen mit Schraubensicherung (Loctite 577 oder PTFE-Paste) sichern
4. Schlauchschellen durch Doppelschellen ersetzen
5. Regelmäßige Sichtprüfung bei laufendem Motor

**AYDI-Confidence:** documented

---

## 11. Troubleshooting-Entscheidungsbäume

### 11.1 Entscheidungsbaum: Motorleistungsverlust

```
MOTOR HAT LEISTUNGSVERLUST
│
├─ Vakuummeter vorhanden?
│   ├─ JA → Vakuummeter prüfen
│   │   ├─ Wert ERHÖHT (>15 kPa Unterdruck)
│   │   │   ├─ Neuer Filter (<50h)?
│   │   │   │   ├─ JA → Problem VOR dem Filter
│   │   │   │   │   ├─ Tankentlüftung prüfen (Unterdruck im Tank?)
│   │   │   │   │   ├─ Tankansaugkorb verstopft?
│   │   │   │   │   └─ Saugleitung geknickt/verstopft?
│   │   │   │   └─ NEIN → Filter verstopft
│   │   │   │       ├─ Wann zuletzt gewechselt?
│   │   │   │       │   ├─ <200h → Ursache klären (Dieselpest? Tank-Sediment?)
│   │   │   │       │   └─ >200h → Normaler Verschleiß, wechseln
│   │   │   │       └─ Einsatz inspizieren:
│   │   │   │           ├─ Schleimig → Dieselpest → Biozid + Tankcheck
│   │   │   │           ├─ Rostig/sandig → Tankkontamination → Tank reinigen
│   │   │   │           └─ Wachsartig → Paraffin → Winterdiesel/Heizung
│   │   │   └─ Wert NORMAL (<5 kPa)
│   │   │       ├─ Problem liegt NICHT am Vorfilter
│   │   │       ├─ Motor-Feinfilter prüfen
│   │   │       ├─ Kraftstoffleitungen prüfen (Knicke, Luftblasen)
│   │   │       └─ Einspritzanlage prüfen (Werkstatt)
│   └─ NEIN → Filtereinsatz manuell prüfen
│       ├─ Wasser im Sammelbecher?
│       │   ├─ JA → Wasser ablassen, ggf. Einsatz wechseln
│       │   └─ NEIN → Weiter prüfen
│       ├─ Einsatz dunkel/verstopft?
│       │   ├─ JA → Einsatz wechseln
│       │   └─ NEIN → Problem nicht am Vorfilter
│       └─ Letzte Wartung >12 Monate?
│           ├─ JA → Vorsorglich wechseln
│           └─ NEIN → Motor-Feinfilter + Einspritzanlage prüfen
```

### 11.2 Entscheidungsbaum: Schwarzer Rauch aus dem Auspuff

```
SCHWARZER RAUCH AUS DEM AUSPUFF
│
├─ Tritt bei allen Drehzahlen auf?
│   ├─ JA → Systemisches Problem
│   │   ├─ Luftfilter verstopft?
│   │   │   ├─ JA → Luftfilter wechseln
│   │   │   └─ NEIN → Weiter
│   │   ├─ Kraftstofffilter (Vorfilter + Motorfilter) verstopft?
│   │   │   ├─ JA → Filter wechseln → Rauch weg?
│   │   │   │   ├─ JA → Gelöst, Intervall anpassen
│   │   │   │   └─ NEIN → Einspritzanlage defekt (Werkstatt)
│   │   │   └─ NEIN → Einspritzanlage, Turbolader, Ventilspiel prüfen
│   │   └─ Falscher Kraftstoff? (Heizöl statt Diesel, verunreinigt)
│   │       ├─ JA → Tank leeren, sauberen Diesel tanken
│   │       └─ NEIN → Motor-Mechanik (Werkstatt)
│   └─ NEIN → Nur bei hoher Drehzahl/Last
│       ├─ Kraftstoff-Zufuhr eingeschränkt?
│       │   ├─ Vakuummeter prüfen (erhöhter Unterdruck unter Last)
│       │   │   ├─ JA → Filter/Saugleitung ist der Engpass
│       │   │   └─ NEIN → Nicht die Filter
│       │   └─ Durchflussrate des Filters ausreichend dimensioniert?
│       │       ├─ NEIN → Größeren Filter installieren
│       │       └─ JA → Problem nicht am Filter
│       └─ Turbolader defekt (Schaufeln, Lager)?
│           └─ Werkstatt
```

### 11.3 Entscheidungsbaum: Filterverfärbung ungewöhnlich

```
FILTEREINSATZ HAT UNGEWÖHNLICHE FARBE
│
├─ Farbe?
│   ├─ Schwarz, gleichmäßig
│   │   └─ Normal, Standardverschmutzung
│   ├─ Schwarz mit Schleim/Klumpen
│   │   └─ Dieselpest → Biozid-Behandlung, ggf. Tanksanierung
│   ├─ Rostbraun/orange
│   │   └─ Rostpartikel → Tank auf Korrosion prüfen
│   │       ├─ Stahltank → Innenbeschichtung prüfen
│   │       └─ Anderer Tank → Kraftstoff-Herkunft prüfen
│   ├─ Grünlich
│   │   └─ Algenbildung (selten bei Diesel, eher bei B7+)
│   │       ├─ Wassergehalt im Tank reduzieren
│   │       └─ Biozid einsetzen
│   ├─ Weiß/wachsartig
│   │   └─ Paraffin → Kälteproblematik
│   │       ├─ Winterdiesel verwenden
│   │       └─ Fließverbesserer zugeben
│   ├─ Heller als erwartet (wenig Verfärbung)
│   │   └─ Filter hat nicht gearbeitet (Bypass?)
│   │       ├─ Einsatz korrekt eingesetzt?
│   │       └─ O-Ring dicht?
│   └─ Metallisch glänzend (Partikel)
│       └─ Metallabrieb → schwerwiegendes Problem
│           ├─ Quelle identifizieren (Pumpe? Injektoren? Tank?)
│           └─ Motor sofort abstellen, Werkstatt
```

### 11.4 Entscheidungsbaum: Wasser im Wasserabscheider

```
WASSER IM SAMMELBECHER FESTGESTELLT
│
├─ Menge?
│   ├─ Wenig (<1/4 Becher)
│   │   └─ Normal (Kondensation)
│   │       ├─ Wasser ablassen
│   │       └─ Intervall beibehalten
│   ├─ Mittel (1/4–3/4 Becher)
│   │   └─ Erhöhte Wasserlast
│   │       ├─ Wasser ablassen
│   │       ├─ Wassereintrittsquelle suchen:
│   │       │   ├─ Einfüllstutzen dicht?
│   │       │   ├─ Tankentlüftung mit Wasserabscheider?
│   │       │   ├─ Tanken bei Regen?
│   │       │   └─ Große Temperaturschwankungen (Kondensation)?
│   │       └─ Kontrollintervall verkürzen (täglich)
│   └─ Voll (>3/4 Becher oder Becher übergelaufen)
│       └─ KRITISCH — Wasserflut
│           ├─ Motor SOFORT abstellen
│           ├─ Tankinhalt prüfen (Wasserphase am Boden?)
│           ├─ Tankwasser ablassen
│           ├─ Filtereinsatz wechseln (wassergesättigt)
│           ├─ Motorfilter prüfen (Wasser durchgebrochen?)
│           └─ Ursache eliminieren (Tank abdichten, Einfüllstutzen)
│
├─ Farbe des Wassers?
│   ├─ Klar
│   │   └─ Kondenswasser → normal
│   ├─ Milchig/emulsionsartig
│   │   └─ Wasser-Diesel-Emulsion → Biodiesel-Problem oder Tensid
│   ├─ Braun/schwarz
│   │   └─ Dieselpest → Biozid + Tankcheck
│   ├─ Rostig
│   │   └─ Tankkorrosion → Tank inspizieren
│   └─ Salzig (Geschmackstest NUR mit Teststreifen!)
│       └─ Seewasser-Eintritt → Tankdurchführung, Einfüllstutzen, Deckdurchführung
```

### 11.5 Entscheidungsbaum: Kraftstoffgeruch im Boot

```
KRAFTSTOFFGERUCH IM BOOT
│
├─ Wo am stärksten?
│   ├─ Motorraum
│   │   ├─ Sichtbare Tropfen/Film?
│   │   │   ├─ JA → Leck lokalisieren
│   │   │   │   ├─ Am Filtergehäuse → O-Ring, Becher prüfen
│   │   │   │   ├─ An Leitungsverschraubungen → Nachziehen, ggf. PTFE
│   │   │   │   ├─ Am Motorfilter → Filterverschraubung prüfen
│   │   │   │   ├─ An Einspritzleitungen → Werkstatt (Hochdruck!)
│   │   │   │   └─ An Rücklaufleitung → Schlauch/Anschluss prüfen
│   │   │   └─ NEIN → Verdunstung
│   │   │       ├─ Filterwechsel vor Kurzem? → Dieselrest verdunstet
│   │   │       ├─ Tankentlüftung im Motorraum? → Umleiten nach außen
│   │   │       └─ Überfüllung beim Tanken? → Überlauf-System prüfen
│   │   └─ Brandgefahr bewerten:
│   │       ├─ Diesel in Bilge → SOFORT reinigen
│   │       ├─ Diesel auf heißen Flächen → Motor abstellen, reinigen
│   │       └─ Nur leichter Geruch → Beobachten, Quelle suchen
│   ├─ Salon/Kabinen
│   │   ├─ Tankentlüftung geht durch Innenraum?
│   │   │   ├─ JA → Umleiten nach außen (über Bord)
│   │   │   └─ NEIN → Weiter
│   │   ├─ Undichter Tank oder Tankdurchführung?
│   │   │   ├─ Tank inspizieren
│   │   │   └─ Durchführungen prüfen
│   │   └─ Bilge-Diesel unter Boden?
│   │       └─ Reinigen, Quelle finden
│   └─ Cockpit/Außen
│       ├─ Auspuffgeruch (unverbrannter Diesel)?
│       │   └─ Motor läuft fett → Filter? Einspritzung?
│       └─ Tankentlüftung im Cockpit?
│           └─ Umleiten
```

---

## 11.6 Entscheidungsbaum: Motor springt nicht an (Kaltstart)

```
MOTOR SPRINGT NICHT AN (KALTSTART)
│
├─ Anlasser dreht?
│   ├─ JA → Kraftstoffversorgung oder Glühkerzen
│   │   ├─ Glühkerzen-Kontrolleuchte leuchtet normal?
│   │   │   ├─ JA → Glühkerzen wahrscheinlich OK
│   │   │   └─ NEIN → Glühkerzen-Sicherung, Relais, Kerzen prüfen
│   │   ├─ Tankventil offen?
│   │   │   ├─ JA → Weiter
│   │   │   └─ NEIN → Öffnen! (häufigster Fehler nach Wartung)
│   │   ├─ Filterwechsel vor Kurzem durchgeführt?
│   │   │   ├─ JA → Luft im System
│   │   │   │   ├─ Entlüftung korrekt durchgeführt?
│   │   │   │   │   ├─ JA → Erneut entlüften, O-Ring prüfen
│   │   │   │   │   └─ NEIN → Komplett entlüften (alle Stufen)
│   │   │   │   └─ Einsatz korrekt eingesetzt? O-Ring vorhanden?
│   │   │   │       ├─ Prüfen → ggf. korrigieren
│   │   │   │       └─ Erneut entlüften
│   │   │   └─ NEIN → Kein kürzlicher Wechsel
│   │   │       ├─ Sammelbecher prüfen → Wasser? Verstopfung?
│   │   │       ├─ Vakuummeter → Unterdruck erhöht?
│   │   │       ├─ Tank leer?
│   │   │       └─ Temperatur <0°C? → Paraffin-Problem
│   │   │           ├─ JA → Winterdiesel? Fließverbesserer?
│   │   │           │   ├─ Motorraum erwärmen (Heizlüfter, 30 Min.)
│   │   │           │   └─ Beheizten Filterkopf erwägen
│   │   │           └─ NEIN → Andere Ursache
│   │   └─ Luft hörbar (Zischen beim Starten)?
│   │       ├─ JA → Luftleck Saugseite
│   │       │   ├─ Filtergehäuse-O-Ring
│   │       │   ├─ Transparenter Becher (Risse?)
│   │       │   ├─ Saugleitungs-Verschraubungen
│   │       │   └─ Kraftstoffschlauch porös?
│   │       └─ NEIN → Förderpumpe defekt?
│   │           └─ Handpumpe betätigen — Widerstand spürbar?
│   │               ├─ JA → Pumpe OK, Blockade weiter unten
│   │               └─ NEIN → Pumpe/Ventile defekt → Werkstatt
│   └─ NEIN → Batterie/Starter-Problem (nicht filterbezogen)
```

### 11.7 Entscheidungsbaum: Ungewöhnliche Motorgeräusche (Klopfen/Nageln)

```
MOTOR KLOPFT ODER NAGELT UNGEWÖHNLICH
│
├─ Klopfen nur bei kaltem Motor?
│   ├─ JA → Normal bei Diesel (besonders Wirbelkammer/Vorkammer)
│   │   └─ Reduziert sich nach Warmfahren?
│   │       ├─ JA → Normal, kein Handlungsbedarf
│   │       └─ NEIN → Weiter prüfen
│   └─ NEIN → Auch bei warmem Motor
│       ├─ Unter Last verstärkt?
│       │   ├─ JA → Einspritzzeitpunkt oder Kraftstoffqualität
│       │   │   ├─ Kraftstoff gewechselt kürzlich? (Billigtanke?)
│       │   │   │   ├─ JA → Niedrige Cetanzahl, Cetanverbesserer zugeben
│       │   │   │   └─ NEIN → Einspritzzeitpunkt prüfen (Werkstatt)
│       │   │   ├─ Wasser im Kraftstoff?
│       │   │   │   ├─ Sammelbecher prüfen
│       │   │   │   └─ Wasser → Klopfen (ungleichmäßige Verbrennung)
│       │   │   └─ Filter verstopft? (ungleichmäßige Versorgung)
│       │   │       └─ Vakuummeter prüfen
│       │   └─ NEIN → Konstant bei allen Drehzahlen
│       │       └─ Mechanisches Problem (Lager, Kolben, Ventile) → Werkstatt
│       └─ Metallisches Klappern?
│           └─ Injektordüse defekt? → Werkstatt (Düsenprüfung)
```

---

## 11.8 Erweiterte Diagnose-Matrix

| Symptom | Filter verstopft | Wasser im System | Dieselpest | Luft im System | Paraffin | Falscher Einsatz |
|---|---|---|---|---|---|---|
| Leistungsverlust | ✓✓✓ | ✓ | ✓✓ | ✓✓ | ✓✓✓ | ✓ |
| Motorstottern | ✓✓ | ✓✓ | ✓✓ | ✓✓✓ | ✓ | ✓ |
| Motor stirbt ab | ✓✓✓ | ✓✓✓ | ✓✓✓ | ✓✓ | ✓✓✓ | — |
| Schwarzer Rauch | ✓✓ | — | — | — | — | — |
| Weißer Rauch | — | ✓✓✓ | — | ✓ | — | — |
| Schlechter Start | ✓ | ✓ | ✓ | ✓✓✓ | ✓✓✓ | — |
| Klopfen/Nageln | — | ✓✓ | — | ✓ | — | — |
| Hoher Verbrauch | ✓ | — | — | ✓ | ✓ | — |
| Dieselgeruch | — | — | — | — | — | — |
| Vakuum hoch | ✓✓✓ | — | ✓✓✓ | — | ✓✓✓ | — |
| Vakuum schwankt | — | — | — | ✓✓✓ | — | — |
| Wasser im Becher | — | ✓✓✓ | ✓✓ | — | — | — |
| Schleim am Filter | — | — | ✓✓✓ | — | — | — |

Legende: ✓ = möglich, ✓✓ = wahrscheinlich, ✓✓✓ = sehr wahrscheinlich, — = unwahrscheinlich

---

## 12. Normen und Vorschriften

### 12.1 ISO-Normen

| Norm | Titel | Relevanz für Kraftstofffilter |
|---|---|---|
| ISO 4020 | Road vehicles — Fuel filters — Test methods | Prüfmethoden Durchfluss, Effizienz, Druckverlust |
| ISO 4548 | Methods of test for full-flow lubricant filters | Analoge Methoden, adaptiert für Kraftstofffilter |
| ISO 16332 | Diesel fuel and petrol filters — Water separation efficiency | Wasserabscheide-Effizienz-Prüfung |
| ISO 19438 | Test method for filtration rating and efficiency | Beta-Wert-Bestimmung |
| ISO 4406 | Hydraulic fluid power — Fluids — Method for coding the level of contamination by solid particles | Partikelzählung und Reinheitsklasse |
| ISO 12216 | Small craft — Windows, portlights, hatches, deadlights and doors | CE-Relevanz allgemein |

### 12.2 CE-Relevanz (Recreational Craft Directive 2013/53/EU)

Die RCD schreibt keine spezifischen Kraftstofffilter vor, aber:
- **ISO 10088**: Fest eingebaute Kraftstoffsysteme — fordert Filter im System
- **ISO 7840**: Feuerbeständige Kraftstoffschläuche — Anforderungen an Leitungen
- **ISO 8469**: Nicht-feuerbeständige Kraftstoffschläuche — Anforderungen
- Filtration als Teil des sicheren Kraftstoffsystems implizit gefordert

### 12.3 Klassifikationsgesellschaften

| Gesellschaft | Anforderung |
|---|---|
| Lloyd's Register | Duplex-Filter (umschaltbar) für Hauptmotoren |
| Bureau Veritas | Primärfilter + Sekundärfilter für alle Motoren >100 kW |
| DNV GL | Duplex-Filter, Wasserstandsalarm, Druckdifferenz-Alarm |
| RINA | Duplex-Filter für Motoren >75 kW |
| ABS | Primärfilter mit Wasserabscheider |

### 12.4 Versicherungsanforderungen

Viele Yacht-Versicherer (besonders für Kategorie A — ozeangehend) fordern:
- Mindestens Duplex-Vorfilter für Hauptmotoren
- Wasserstandsalarm
- Ersatzfiltereinsätze an Bord (mindestens 2 pro Filtergehäuse)
- Dokumentierte Wartung (Logbuch)

---

## 13. Kraftstoffqualität und Additive

### 13.1 Dieselqualität nach Betankungsort

| Region | Qualität (Tendenz) | Risiken | Empfehlung |
|---|---|---|---|
| Nordeuropa (D/NL/UK/Skandinavien) | Gut (EN 590 B7) | Biodiesel-Anteil, Kondensation | Standard-Intervalle |
| Westliches Mittelmeer (F/ES/IT) | Gut bis mäßig | Höherer Schwefel, variable Qualität | Intervall ×0,75 |
| Östliches Mittelmeer (GR/TR/HR) | Mäßig | Wasser, Sediment, unklarer Biodiesel-Anteil | Intervall ×0,5–0,75 |
| Karibik | Mäßig bis schlecht | Wasser, Verunreinigungen, hohe Temperaturen | Intervall ×0,5, immer filtern |
| Westafrika | Schlecht | Stark verunreinigt, Wasser, Sand | 30µm Vorfilter + 10µm, Intervall ×0,25 |
| Südostasien | Variable | Wasser, Biodiesel-Anteil unklar, Pilz | Intervall ×0,5, Biozid prophylaktisch |
| Pazifik (Inseln) | Schlecht bis mäßig | Alte Bestände, Kondensation | Tragbarer Filterkanister beim Tanken |

### 13.2 Additive (empfohlene und bewährte)

#### 13.2.1 Biozide (gegen Dieselpest)

Siehe Abschnitt 9.3.1 — detaillierte Auflistung.

#### 13.2.2 Fließverbesserer (Cold Flow Improver)

| Produkt | Dosierung | Wirkung | Preis |
|---|---|---|---|
| Liqui Moly Diesel-Fließfit | 1:1.000 | CFPP ca. -15°C verbessern | €10–€15 / 150ml |
| ADDINOL Winterprotect | 1:1.000 | CFPP ca. -20°C verbessern | €12–€18 / 250ml |
| Stanadyne Performance Formula | 1:3.800 | +12°C CFPP-Verbesserung | €25–€35 / 473ml |

#### 13.2.3 Stabilisatoren (Lagerung)

| Produkt | Dosierung | Wirkung | Preis |
|---|---|---|---|
| Liqui Moly Diesel-Additiv | 1:1.000 | Oxidationsschutz, Reinigung | €8–€12 / 250ml |
| Stanadyne Lubricity Formula | 1:3.800 | Schmierung, Stabilisierung | €18–€25 / 473ml |
| ValvTect Diesel Guard | 1:1.280 | Multifunktional | €15–€22 / 946ml |

#### 13.2.4 Cetanzahlverbesserer

| Produkt | Dosierung | Wirkung | Preis |
|---|---|---|---|
| Liqui Moly Super Diesel Additiv | 1:1.000 | +3–5 Cetanzahl, Reinigung | €10–€15 / 250ml |
| Power Service Diesel Kleen | 1:1.500 | +3–6 Cetanzahl | €12–€18 / 946ml |

### 13.3 Tragbare Filterung beim Tanken

**Burt's Bottle (Racor FBO-10):**
- Tragbarer Filter-/Wasserabscheider für den Einfüllschlauch
- Durchfluss: bis 75 l/min
- Filtert Diesel BEIM Tanken (vor dem Tank)
- Besonders wertvoll in Regionen mit schlechter Dieselqualität
- Preis: €350–€500

**Mr. Funnel (Provisionell):**
- Trichter mit feinem Sieb + Wasser-Blockierfolie
- Einfach, robust, kostengünstig
- Durchfluss: ca. 15 l/min
- Preis: €25–€45

---

## 14. Dimensionierung und Auslegung

### 14.1 Auslegungsformel

```
Durchfluss_erforderlich [l/h] = (P_max [kW] × BSFC [g/kWh]) / (ρ_Diesel [g/l]) × SF

Wobei:
  P_max    = Max. Motorleistung in kW
  BSFC     = Brake Specific Fuel Consumption (spez. Kraftstoffverbrauch)
             - Saugdiesel: 260 g/kWh
             - Turbo-DI: 230 g/kWh
             - Common-Rail: 210 g/kWh
  ρ_Diesel = Dichte Diesel = 840 g/l
  SF       = Sicherheitsfaktor
             - Saugleitung (Filter vor Förderpumpe): 2,0
             - Druckleitung (Filter nach Förderpumpe): 1,5
             - Rücklauf-basiert (Common-Rail-Förderstrom): 3,0
```

### 14.2 Dimensionierungstabelle

| Motorleistung | Durchfluss berechnet (SF=2,0) | Empfohlener Racor | Empfohlener Separ | Empfohlener Vetus |
|---|---|---|---|---|
| 10 kW (14 PS) | 6 l/h → 12 l/h | 110A (57 l/h) | SWK-2000/5 (75 l/h) | — |
| 20 kW (27 PS) | 11 l/h → 22 l/h | 120A (114 l/h) | SWK-2000/5 (75 l/h) | WS180 (180 l/h) |
| 40 kW (54 PS) | 22 l/h → 44 l/h | 500FG (227 l/h) | SWK-2000/5/50 (125 l/h) | WS180 (180 l/h) |
| 75 kW (102 PS) | 41 l/h → 82 l/h | 500FG (227 l/h) | SWK-2000/10 (250 l/h) | WS360 (360 l/h) |
| 150 kW (204 PS) | 82 l/h → 164 l/h | 500FG (227 l/h) | SWK-2000/10 (250 l/h) | WS720 (720 l/h) |
| 300 kW (408 PS) | 164 l/h → 328 l/h | 900FG (340 l/h) | SWK-2000/18 (450 l/h) | WS750 (750 l/h) |
| 500 kW (680 PS) | 274 l/h → 548 l/h | 1000FG (681 l/h) | SWK-2000/40 (1.000 l/h) | — |
| 750 kW (1.020 PS) | 411 l/h → 822 l/h | 75900 (1.135 l/h) | SWK-2000/40 (1.000 l/h) | — |
| 1.000 kW (1.360 PS) | 548 l/h → 1.096 l/h | 731000 (1.893 l/h) | SWK-2000/130 (3.250 l/h) | — |

### 14.3 Zweistufige Filtration — Empfohlene Kombinationen

| Stufe 1 (Vorfilter) | Stufe 2 (Motorfilter) | Gesamtfiltration | Empfohlen für |
|---|---|---|---|
| 30µm Vorfilter | 10µm Motor-OEM | 30µm → 10µm | Mechanische Einspritzung |
| 10µm Vorfilter | 5µm Motor-OEM | 10µm → 5µm | Common-Rail (Standard) |
| 10µm Vorfilter | 2µm Motor-OEM | 10µm → 2µm | Common-Rail (Hochdruck) |
| 2µm Vorfilter | 2µm Motor-OEM | 2µm → 2µm | Kritische Anwendung |

**Hinweis:** Zwei identische Feinheiten in Serie verdoppeln nicht die Filtration, aber die Schmutzaufnahmekapazität. Das verlängert die Standzeit des teureren Motorfilters.

### 14.4 Common-Rail-Besonderheiten

Moderne Common-Rail-Dieselmotoren stellen besondere Anforderungen:

1. **Höhere Filterfeinheit**: 2–5µm statt 10µm
2. **Geringere Wassertoleranz**: <200 ppm statt <500 ppm
3. **Rücklaufmenge**: Die Hochdruckpumpe fördert mehr Kraftstoff als die Injektoren verbrauchen — der Überschuss fließt zurück. Dieser Rücklauf ist heiß (60–80°C) und kann beim Rückfluss in den Tank:
   - Wasserausscheidung im Tank begünstigen (Temperaturschock)
   - Oxidation des Diesels beschleunigen
   - Biologisches Wachstum begünstigen (warmes Diesel-Wasser-Gemisch)
4. **Selbstentlüftung**: Viele Common-Rail-Systeme haben automatische Entlüftung
5. **Sensoren**: OEM-Wasserstandssensoren im Motorfilter (Werkstatt-Diagnose)

### 14.5 Sonderfälle der Dimensionierung

#### 14.5.1 Twin-Engine-Yachten

Bei Twin-Engine-Installationen gilt:
- **Separate Filter pro Motor** (Standardlösung): Jeder Motor hat seinen eigenen Vorfilter, dimensioniert auf die jeweilige Motorleistung
- **Gemeinsamer Vorfilter** (Budgetlösung): Ein großer Filter für beide Motoren — NUR wenn der Durchfluss für beide gleichzeitig reicht
- **Empfehlung:** Separate Filter. Grund: Bei einem Filterproblem ist nur ein Motor betroffen

**Beispiel:** 2× Volvo Penta D4-300 (je 221 kW)
- Pro Motor: 221 kW × 210 g/kWh / 840 g/l × 2,0 = 110 l/h → Racor 500FG (227 l/h) reicht
- Gemeinsam: 220 l/h → Racor 900FG (340 l/h) nötig, aber: kein Redundanz-Gewinn!

#### 14.5.2 Generator-Diesel

Auch der Generator braucht sauberen Kraftstoff:
- Kleine Generatoren (<10 kW): Oft nur Motor-OEM-Filter, ausreichend wenn Tank sauber
- Mittlere Generatoren (10–30 kW): Racor 120A als Vorfilter empfohlen
- Große Generatoren (>30 kW): Racor 500FG als Vorfilter empfohlen
- Generator hat oft eigenen Tankansaug (nah am Tankboden) → mehr Sediment als Hauptmotor

#### 14.5.3 Heizungsysteme (Webasto, Eberspächer)

Diesel-Standheizungen (Webasto Thermo Top, Eberspächer Hydronic):
- Sehr geringer Verbrauch (0,3–1,0 l/h)
- Empfindlich gegen Wasser und Partikel
- Eigener Inline-Filter am Gerät (Wechselintervall nach Hersteller)
- Kein zusätzlicher Vorfilter nötig, wenn Haupt-Vorfilter im System sitzt
- ABER: Heizungsansaugleitung muss NACH dem Vorfilter abzweigen, nicht direkt vom Tank

---

## 15. Forum-Erfahrungen und Praxisberichte

### 15.1 Häufig diskutierte Themen in Yachtforen

#### 15.1.1 „Racor vs. Separ" (Dauerbrenner)

**Konsens:**
- Racor: Breiter verfügbar, mehr Ersatzteil-Quellen, Standard-Referenz weltweit
- Separ: Bessere Wasserabscheidung, robustere Bauweise, deutscher Service
- Beide Systeme sind zuverlässig und bewährt
- Entscheidung oft nach vorhandener Installation (was bereits an Bord ist)

#### 15.1.2 „2µm oder 10µm?" (Häufige Frage)

**Konsens:**
- Ältere Motoren (mechanische Einspritzung): 10µm ausreichend, 2µm verstopft zu schnell
- Moderne Motoren (Common-Rail): 2µm empfohlen, mindestens 10µm als Vorfilter
- Kompromiss: 10µm Vorfilter + Motor-OEM-Feinfilter (2–5µm)
- In Regionen mit schlechtem Diesel: 30µm Vorfilter + 10µm Hauptfilter

#### 15.1.3 „Dual-Racor-System — lohnt es sich?"

**Konsens:**
- Für Blauwasser und Ozeanpassagen: unbedingt
- Für Wochenendsegler im Mittelmeer: Nice-to-have, kein Muss
- Kosten-Nutzen: €600–€1.500 für ein Dual-System vs. Motorreparatur >€5.000
- Praktischer Tipp: Ein Filter reicht, wenn immer 2 Ersatzeinsätze an Bord sind und der Wechsel in 10 Minuten möglich ist

#### 15.1.4 „Nachrüst-Erfahrungen Kraftstoff-Poliersystem"

**Konsens:**
- Bei großen Tanks (>500 l) und langen Standzeiten: sehr sinnvoll
- Eigenbau aus Racor + Jabsco-Impellerpumpe + Timer: bewährt, €300–€500
- Fertigsysteme: komfortabler, aber deutlich teurer (€800–€2.000)
- Timer: 4 Stunden pro Tag reicht für die meisten Tanks

#### 15.1.5 „Grotamar vs. Biobor — welches Biozid?"

**Konsens:**
- Grotamar 82 (Schülke & Mayr): In Europa Standard, sehr wirksam, breites Wirkungsspektrum
- Biobor JF: In USA Standard, ebenso wirksam, leicht andere Wirkstoffe
- Beide sind zugelassen und bewährt — Verfügbarkeit am Tankort entscheidet oft
- NICHT mischen — ein Produkt konsequent verwenden
- Beide angreifen die meisten Dichtungsmaterialien NICHT (bei korrekter Dosierung)

#### 15.1.6 „Wie baue ich ein Poliersystem selbst?"

**Häufig empfohlener Aufbau:**
1. Jabsco 23870 Impellerpumpe (12V, selbstansaugend, 35 l/min)
2. Racor 120A als Polierfilter (10µm-Einsatz)
3. 12mm-Kupferleitung oder CE-Schlauch
4. Ansaugung: Tankboden (separater Ansaugstutzen oder T-Stück am bestehenden)
5. Rücklauf: Tankoberseite (Rücklaufdüse oder separater Stutzen)
6. Timer-Relais: 4 Stunden pro Tag (z.B. Finder 80-Serie)
7. Absicherung: 5A auf der Plusleitung

**Kosten Eigenbau:** €300–€500
**Kosten Fertigsystem:** €800–€2.000

#### 15.1.7 „Vakuummeter — welches und wo?"

**Konsens:**
- Racor RK11-1606-1 ist das Standard-Kit für Racor-Gehäuse
- Alternativ: Jedes Vakuummeter mit 1/8" NPT-Anschluss (0 bis -70 kPa)
- Montage: Direkt am Filtergehäuse (Racor hat Anschlussstutzen)
- Ablesung: Am besten sichtbar vom Steuerstand oder vom Motorraum-Eingang
- Fernablesung: Möglich mit elektrischem Drucksensor + Anzeige (Aufwand aber groß)
- Grünbereich: 0 bis -10 kPa
- Gelbbereich: -10 bis -20 kPa (Wechsel planen)
- Rotbereich: >-20 kPa (sofort wechseln)

### 15.2 Typische Eigner-Fehler

| Fehler | Häufigkeit | Konsequenz |
|---|---|---|
| Filter nie gewechselt (seit Jahren) | Sehr häufig (Charteryachten) | Motorausfall, Injektorschaden |
| Wasser im Becher ignoriert | Häufig | Dieselpest, Korrosion |
| Falschen Einsatz eingebaut | Gelegentlich | Bypass-Filtration (kein Schutz) |
| Becher nicht richtig angezogen | Gelegentlich | Luft zieht, Dieselleck |
| Tank nicht voll gelagert (Winter) | Häufig | Kondensation → Dieselpest |
| Biozid-Überdosierung | Selten | Schaumbildung, Dichtungsschäden |
| Billig-Einsätze (No-Name) | Gelegentlich | Schlechtere Filtration, Faserlösung |

---

## 16. FAQ — Häufig gestellte Fragen

### F-01: Wie oft muss ich den Kraftstofffilter wechseln?

**Antwort:** Alle 200–500 Betriebsstunden oder mindestens einmal jährlich — je nachdem, was zuerst eintritt. Bei verschmutztem Diesel oder nach langer Standzeit deutlich häufiger. Ein Vakuummeter am Filter ist die beste Investition für die richtige Wechselentscheidung.

### F-02: Was ist der Unterschied zwischen Vorfilter und Motorfilter?

**Antwort:** Der Vorfilter (Racor, Separ, Vetus) sitzt zwischen Tank und Motor, filtert grob (10–30µm) und scheidet Wasser ab. Der Motorfilter sitzt direkt am Motor, filtert fein (2–10µm) und ist vom Motorhersteller spezifiziert. Beide zusammen bilden ein zweistufiges System.

### F-03: Mein Motor stottert — ist der Filter schuld?

**Antwort:** Möglicherweise. Prüfen Sie: (1) Vakuummeter — erhöhter Unterdruck = verstopfter Filter. (2) Sammelbecher — Wasser oder Verschmutzung sichtbar? (3) Luftblasen im Becher — undichter O-Ring? Wenn alles OK: Problem liegt woanders (Einspritzanlage, Luftfilter, Motorelektrik).

### F-04: Kann ich den Filtereinsatz reinigen und wiederverwenden?

**Antwort:** Zellulose-Einsätze: NEIN, niemals. Nylon-Siebeinsätze (z.B. Racor 2010N-10): JA, mit Diesel ausspülen und trocknen. Generell: Zellulose-Einsätze sind Verbrauchsmaterial und kosten €15–€40. Der Motor ist €10.000–€50.000 wert. Sparen Sie nicht am Filter.

### F-05: Brauche ich einen Wasserstandssensor?

**Antwort:** Dringend empfohlen für: (a) Motoryachten, die viel laufen, (b) Yachten in tropischen Gewässern, (c) Yachten mit Tank >500 l, (d) jede Blauwasseryacht. Für eine Segelyacht, die wöchentlich segelt und regelmäßig den Becher kontrolliert — Nice-to-have, kein Muss.

### F-06: Was ist Dieselpest und wie erkenne ich sie?

**Antwort:** Dieselpest ist mikrobiologisches Wachstum (Bakterien, Pilze) an der Wasser-Diesel-Grenzschicht im Tank. Erkennung: Schwarzer/brauner Schleim auf dem Filtereinsatz, fauliger Geruch, schnell verstopfende Filter. Nachweis: Dip-Slide-Test (€15–€25). Gegenmaßnahme: Biozid (Grotamar 82, Biobor JF), bei schwerem Befall Tanksanierung.

### F-07: Welchen Biozid-Hersteller empfehlen Sie?

**Antwort:** Grotamar 82 und Biobor JF sind die beiden meistverwendeten und bewährtesten Produkte im Yachtbau. Grotamar 82 ist in Europa am verbreitetsten, Biobor JF in den USA. Beide sind wirksam und zugelassen. Dosierung exakt einhalten!

### F-08: Mein Racor 500FG-Gehäuse hat weiße Korrosion — was tun?

**Antwort:** Das Standardgehäuse ist Aluminium-Druckguss und korrodiert in Salzluft-Umgebung. Sofortmaßnahme: Korrosion abbürsten, mit CorrosionX oder Lanocote behandeln. Langfristig: Edelstahl-Version (500FGSS) kaufen — €100–€150 Aufpreis, aber keine Korrosion. Überprüfen Sie auch, ob Aluminium-Gehäuse und Kupferleitungen direkten Kontakt haben (galvanische Korrosion).

### F-09: Kann ich statt dem Original auch einen Nachbau-Einsatz verwenden?

**Antwort:** Es gibt qualitativ hochwertige Nachbauten (z.B. von Parker/Racor selbst produzierte OEM-Einsätze für andere Marken) und billige No-Name-Kopien. Empfehlung: Original oder bekannte Marken (Griffin, Mann+Hummel). Billige Nachbauten können minderwertige Filtermedien, schlechte O-Ringe und falsche Maße haben. Bei Common-Rail-Motoren: NUR Originaleinsätze oder explizit zertifizierte Alternativen.

### F-10: Wie entlüfte ich nach dem Filterwechsel?

**Antwort:** (1) Tankventil öffnen. (2) Entlüftungsschraube am Vorfilter öffnen. (3) Handpumpe betätigen bis blasenfreier Diesel austritt. (4) Entlüftungsschraube schließen. (5) Dasselbe am Motorfilter wiederholen. (6) Motor starten — kurzes Stottern normal. Bei Common-Rail: Viele Motoren haben Selbstentlüftung, aber den Vorfilter trotzdem manuell entlüften.

### F-11: Mein Motor springt nach dem Filterwechsel nicht an — was habe ich falsch gemacht?

**Antwort:** Luft im System. Häufigste Fehler: (a) Entlüftung vergessen oder unvollständig. (b) O-Ring vergessen oder falsch eingelegt. (c) Einsatz nicht korrekt sitzend. Lösung: Nochmals komplett entlüften. Wenn das nicht hilft: Alle Verschraubungen auf Dichtheit prüfen, O-Ring-Sitz kontrollieren. Notfall: Einspritzleitungen an den Injektoren leicht lösen, Motor anlassen, bis Diesel austritt, festziehen.

### F-12: Wie lagere ich Ersatz-Filtereinsätze an Bord richtig?

**Antwort:** In der Originalverpackung, trocken, vor Sonneneinstrahlung geschützt. Zellulose-Einsätze sind hygroskopisch — Feuchtigkeit verschlechtert die Filtrationsleistung. Nicht in der Bilge lagern. Empfehlung: In einem verschlossenen Plastikbeutel mit Trockenmittel-Beutel.

### F-13: Dual-Filter oder einzelner Filter mit Ersatzeinsatz — was ist besser?

**Antwort:** Dual-Filter ist bequemer und sicherer (Umschalten ohne Motorunterbrechung). Aber teurer (Manifold + zweites Gehäuse). Ein einzelner Filter reicht, wenn Sie den Wechsel schnell (<15 Minuten) durchführen können und immer Ersatzeinsätze haben. Für Blauwasser und Kategorie-A-Yachten: Dual-Filter empfohlen. Für Küstensegler: Einzelfilter + 2 Ersatzeinsätze reicht.

### F-14: Mein Bootsbauer hat einen Filter eingebaut, den ich nicht kenne — wie finde ich den richtigen Einsatz?

**Antwort:** (1) Gehäuse-Etikett fotografieren (Hersteller, Modell, Teilenummer). (2) Teilenummer googeln oder beim Marine-Händler nachfragen. (3) Gehäuse vermessen (Höhe, Durchmesser, Anschlussgewinde) und mit Katalogen vergleichen. (4) Im Zweifelsfall: Gehäuse ersetzen durch einen Standard (Racor 500FG) — langfristig besser als unbekannte Einsätze zu suchen.

### F-15: Muss der Filter wirklich senkrecht montiert sein?

**Antwort:** JA. Die Wasserabscheidung funktioniert durch Schwerkraft — Wasser muss nach unten in den Sammelbecher sinken. Bei schräger Montage (>5°) ist die Wasserabscheidung signifikant reduziert. Bei waagerechter Montage funktioniert sie praktisch nicht. Einzige Ausnahme: Reihenfilter (z.B. Racor 200-Serie) ohne Wasserabscheider-Funktion.

### F-16: Kann ich einen Benzinfilter für Diesel verwenden?

**Antwort:** NEIN! Benzinfilter haben andere Materialien (Diesel löst manche Kunststoffe/Dichtungen), andere Druckwerte und keine Wasserabscheidung. Außerdem: Benzinfilter sind für Überdruck-Systeme (Benzin wird gepumpt), Diesel-Vorfilter arbeiten auf der Saugseite (Unterdruck). Falscher Filter = Motorschaden + Sicherheitsrisiko.

### F-17: Wie erkenne ich, ob mein Diesel noch gut ist?

**Antwort:** Einfacher Test: Probe in ein Glasgefäß füllen, gegen Licht halten. Klar und bernsteinfarben = OK. Trüb = Wasser (emulgiert). Flocken/Schlieren = Dieselpest oder Oxidation. Dunkler als erwartet = Alterung. Fauliger Geruch = biologische Kontamination. Professionell: Dip-Slide-Test (Biologie), Karl-Fischer-Titration (Wasser, Labor).

### F-18: Was kostet ein komplett neues Filtersystem (Nachrüstung)?

**Antwort:** Abhängig von der Motorgröße: (a) Segelyacht 30–40 PS, Racor 500FG: Material €250–€350, Einbau €200–€400. (b) Motoryacht 150–300 PS, Racor 900FG oder 1000FG: Material €400–€700, Einbau €300–€600. (c) Dual-System: Material + 50%, Einbau + 30%. (d) Poliersystem: zusätzlich €500–€1.500.

### F-19: Was ist der Unterschied zwischen FG und FH bei Racor?

**Antwort:** FG = Fuel/Gasoline (eigentlich: Fuel Grade, für Diesel und Benzin). FH = Fuel/Heating (für Heizöl). Technisch sind die Gehäuse und Einsätze identisch. Der Unterschied liegt in der Zertifizierung. Für marine Diesel: FG kaufen.

### F-20: Wie oft muss ich den Sammelbecher leeren?

**Antwort:** Wöchentlich kontrollieren, bei Wasser sofort ablassen. In der Praxis: Bei jedem Motorbetrieb kurz nachschauen (transparenter Becher). Nach jedem Starkwind-Segeln oder Schlechtwetter-Fahrt: prüfen (Seegang wirbelt Tank auf). Bei langer Standzeit: vor dem Starten prüfen.

### F-21: Mein Vakuummeter zeigt immer 0 — ist es defekt?

**Antwort:** Möglicherweise: (a) Anschlussschlauch undicht oder abgerutscht. (b) Vakuummeter defekt. (c) Filter ist tatsächlich sauber UND die Saugleitung hat keinen Widerstand (unwahrscheinlich bei laufendem Motor). Test: Bei laufendem Motor muss ein minimaler Unterdruck vorhanden sein (2–5 kPa). Wenn 0: Schlauch und Anschluss prüfen.

### F-22: Kann Diesel ablaufen?

**Antwort:** Diesel hat kein offizielles Ablaufdatum, aber eine begrenzte Lagerstabilität. Ohne Additive: 6–12 Monate bei guten Bedingungen. Mit Stabilisator-Additiv: 12–24 Monate. Biodiesel (B7): kürzer als reiner Mineraldiesel. Anzeichen von gealtertem Diesel: Dunkle Farbe, Geruch nach Lack/Lösemittel, Sedimentbildung.

### F-23: Soll ich den Filter vor oder nach der Förderpumpe einbauen?

**Antwort:** Den Vorfilter/Wasserabscheider VOR der Förderpumpe (Saugseite). So schützt er auch die Pumpe. Der motormontierte Feinfilter sitzt NACH der Förderpumpe (Druckseite). Wichtig: Ein Filter auf der Saugseite darf keinen zu hohen Druckverlust erzeugen (sonst Kavitation). Deshalb den Vorfilter großzügig dimensionieren.

### F-24: Was bedeuten die Farben der Racor-Filtereinsätze?

**Antwort:** Racor codiert die Feinheit farblich: (a) Braun/Beige = 30µm (PM-Serie). (b) Gelb = 10µm (TM-Serie). (c) Weiß = 2µm (SM-Serie). Diese Farbcodierung gilt für die Turbine-Serie (500, 900, 1000). Immer die Teilenummer prüfen, nicht nur die Farbe.

### F-25: Ist ein Kraftstoff-Poliersystem wirklich nötig?

**Antwort:** Für die meisten Küstensegler: nein. Der regelmäßige Motorbetrieb und jährlicher Filterwechsel reichen. Für Blauwasserfahrer mit großen Tanks (>500 l), langen Standzeiten und Betankung in fraglichen Regionen: ja, eine der besten Investitionen. Für Motoryachten mit >2.000 l Tankvolumen: Standard, da die Kraftstoffmenge groß genug für signifikante Kondensation und biologisches Wachstum ist.

### F-26: Welche Ersatzteile sollte ich immer an Bord haben?

**Antwort:**
- 2–3 Filtereinsätze (Vorfilter)
- 1–2 Filtereinsätze (Motorfilter)
- O-Ring-Satz für Filtergehäuse
- Entlüftungsschlüssel / Handpumpen-Ersatzteile
- 1 Flasche Biozid (Grotamar 82 oder Biobor JF)
- 1 Dip-Slide-Test
- Vakuummeter (falls nicht fest installiert)
- Auffangschale und Lappen

### F-27: Mein transparenter Becher ist gelb/milchig geworden — muss ich ihn tauschen?

**Antwort:** Gelb/milchig = UV-Alterung oder Kontakt mit aggressiven Additiven. Funktional ist der Becher noch OK, solange er nicht rissig oder spröde ist. ABER: Die Inspektion des Wasserstands ist erschwert. Empfehlung: Becher alle 5–7 Jahre prophylaktisch ersetzen. Ein geplatzter Polycarbonat-Becher bei laufendem Motor = Dieselaustritt im Motorraum = Brandgefahr.

### F-28: Kann ich einen Racor-Einsatz in ein Separ-Gehäuse einsetzen (oder umgekehrt)?

**Antwort:** NEIN. Die Einsätze sind nicht austauschbar. Racor und Separ verwenden unterschiedliche Abmessungen, Dichtungssysteme und Befestigungsmechanismen. Ein falscher Einsatz kann Bypass-Strömung erzeugen (kein Filterschutz) oder undicht sein. Immer den vom Gehäusehersteller spezifizierten Einsatz verwenden.

### F-29: Wie erkenne ich, ob mein Tankansaugkorb verstopft ist?

**Antwort:** Symptome: (1) Vakuummeter zeigt hohen Unterdruck trotz neuem Filtereinsatz. (2) Motorleistung fällt besonders bei hoher Last ab. (3) Problem tritt plötzlich auf (Rost-/Schuppenablösung im Tank). Diagnose: Tankansaugkorb inspizieren — erfordert Zugang zum Tank (Inspektionsluke). Bei Stahltanks >15 Jahre: Ansaugkorb-Reinigung/Austausch in die regelmäßige Wartung aufnehmen.

### F-30: Mein Motor hat Common-Rail — brauche ich wirklich einen 2µm-Vorfilter?

**Antwort:** Der Motorhersteller spezifiziert den Feinfilter am Motor bereits auf 2–5µm. Der Vorfilter muss nicht identisch fein sein — er dient als Schutz für den Motorfilter und die Förderpumpe. Ein 10µm-Vorfilter + 2µm-Motorfilter ist eine bewährte und sinnvolle zweistufige Kombination. Ein 2µm-Vorfilter würde in verschmutzten Gewässern zu schnell verstopfen. Empfehlung für Common-Rail: 10µm-Vorfilter (Racor 500FG/900FG) + Motor-OEM-Feinfilter.

### F-31: Was kostet es, wenn ich den Filterwechsel ignoriere?

**Antwort:** Kalkulation am Beispiel eines Volvo Penta D6 (Common-Rail):
- Filterwechsel Vorfilter + Motorfilter: €80–€120/Jahr
- Einspritzdüsen-Satz (6 Stück): €6.000–€12.000
- Hochdruckpumpe: €4.000–€8.000
- Motorüberholung nach Wasser-/Schmutzschaden: €15.000–€30.000
- Abschleppen in der Marina nach Motorausfall: €500–€2.000
- Der Filterwechsel ist die günstigste Versicherung, die es gibt.

### F-32: Wie schnell wächst Dieselpest?

**Antwort:** Unter optimalen Bedingungen (25–35°C, freies Wasser, Biodiesel) kann die Bakterienpopulation sich alle 20–30 Minuten verdoppeln. Von 100 Organismen auf 10 Millionen in weniger als 2 Wochen. In der Praxis (suboptimale Bedingungen) dauert es typisch 4–8 Wochen von Stadium 1 zu Stadium 3. Kälte (<15°C) verlangsamt das Wachstum drastisch, stoppt es aber nicht vollständig.

### F-33: Kann ich HVO/GTL-Diesel tanken und hat das Auswirkungen auf den Filter?

**Antwort:** HVO (Hydrotreated Vegetable Oil) und GTL (Gas-to-Liquid) sind synthetische Dieselkraftstoffe mit hervorragenden Eigenschaften: praktisch kein Wasser, kein Biodiesel-Anteil, sehr hohe Cetanzahl (>70), keine Paraffin-Probleme. Auswirkung auf Filter: (1) Deutlich längere Filterstandzeiten. (2) Kein Dieselpest-Risiko (kein Wasser, keine Bio-Nährstoffe). (3) Keine Paraffin-Probleme bei Kälte. Nachteil: Begrenzte Verfügbarkeit, ca. 20–40% teurer als EN 590-Diesel.

### F-34: Wie lagere ich Diesel langfristig im Tank (Yacht im Winterlager)?

**Antwort:** (1) Tank zu 95% füllen (minimiert Luft/Kondensation, nicht 100% wegen Ausdehnung). (2) Biozid zugeben (Erhaltungsdosierung). (3) Stabilisator-Additiv zugeben (Oxidationsschutz). (4) Motor 15–20 Min. laufen lassen (behandelter Diesel im ganzen System). (5) Neuen Filtereinsatz einsetzen. (6) Im Frühjahr: Sammelbecher prüfen, Tankprobe testen, ggf. Einsatz wechseln.

### F-35: Mein Segelboot hat nur einen kleinen 10-PS-Motor — brauche ich überhaupt einen separaten Vorfilter?

**Antwort:** Ein separater Vorfilter ist auch bei kleinen Motoren sinnvoll, wenn: (a) Das Boot längere Zeit steht (Dieselpest-Risiko). (b) In verschiedenen Häfen/Ländern getankt wird. (c) Der Tank älter als 15 Jahre ist. Ein Racor 120A oder Separ SWK-2000/5 kostet €100–€200 und kann einen Motorausfall im ungünstigsten Moment verhindern. Für ein Boot, das ausschließlich in Nordeuropa fährt und regelmäßig bewegt wird: Der Motor-OEM-Filter reicht — aber ein Vorfilter ist trotzdem eine gute Versicherung.

---

## 17. Glossar

| Begriff | Erklärung |
|---|---|
| **Absolutfiltration** | Filtrationsgrad ≥99,9% bei angegebener Partikelgröße |
| **AquaBlock** | Fleetguard-Technologie: Filterelement blockiert bei Wasserkontakt den Durchfluss |
| **BSFC** | Brake Specific Fuel Consumption — spezifischer Kraftstoffverbrauch [g/kWh] |
| **Beta-Wert (βx)** | Verhältnis Partikelzahl vor/nach Filter bei Größe x µm. β10=200 → 99,5% Effizienz |
| **Biozid** | Chemische Substanz zur Abtötung von Mikroorganismen im Kraftstoff |
| **Bypass** | Unerwünschter Kraftstofffluss um das Filterelement herum |
| **CAV** | Clayton, Abell & Vakuum — historischer britischer Filterhersteller (jetzt Delphi) |
| **CE-Kategorie** | Einstufung der Seetüchtigkeit nach EU Recreational Craft Directive (A–D) |
| **CFPP** | Cold Filter Plugging Point — Temperatur, bei der Diesel den Filter verstopft |
| **CFU** | Colony Forming Units — Maßeinheit für Mikroorganismen pro ml |
| **Cloud Point** | Temperatur, bei der Paraffinkristalle im Diesel sichtbar werden |
| **Common-Rail** | Hochdruck-Einspritzsystem (1.600–2.500 bar) mit gemeinsamer Druckleitung |
| **Dieselpest** | Mikrobiologische Kontamination des Kraftstoffs (Diesel Bug) |
| **Drain** | Ablassventil am Sammelbecher des Wasserabscheiders |
| **Duplex-Filter** | Zwei parallel montierte Filter mit Umschaltventil (Wechsel unter Last) |
| **Emulsion** | Feine Verteilung von Wasser in Diesel (oder umgekehrt), milchig trüb |
| **EN 590** | Europäische Norm für Dieselkraftstoffqualität |
| **FAME** | Fatty Acid Methyl Ester — Biodiesel-Komponente |
| **FBO** | Fuel Biocide/Oxidation — Racor-Kraftstoffaufbereitungssystem |
| **FG** | Fuel Grade — Racor-Bezeichnung für Diesel-/Benzinfilter |
| **FH** | Fuel/Heating — Racor-Bezeichnung für Heizölfilter |
| **Fließverbesserer** | Additiv zur Senkung des CFPP (Cold Flow Improver) |
| **Hormoconis resinae** | Pilzart, Hauptverursacher der Dieselpest |
| **Hydrophob** | Wasserabweisend — Eigenschaft des Koaleszenz-Filtermediums |
| **Injektoren** | Einspritzdüsen am Motor |
| **ISO 7840** | Norm für fest installierte Kraftstoffschläuche (marine) |
| **ISO 10088** | Norm für fest eingebaute Kraftstoffsysteme (Sportboote) |
| **Karl-Fischer-Titration** | Präzise Labormethode zur Bestimmung des Wassergehalts |
| **Kavitation** | Blasenbildung in Flüssigkeit durch Unterdruck — schädlich für Pumpen |
| **Koaleszenz** | Zusammenführen kleiner Tröpfchen zu größeren durch hydrophobe Fasern |
| **MIC** | Microbiologically Influenced Corrosion — Korrosion unter Biofilm |
| **Manifold** | Verteiler-/Sammelstück für Dual-Filter-Systeme |
| **NanoNet** | Fleetguard-Synthetik-Filtermedium für ≤2µm Filtration |
| **Nominalfiltration** | Filtrationsgrad 95–98% bei angegebener Partikelgröße |
| **O-Ring** | Ringförmige Elastomer-Dichtung zwischen Filtergehäuse und Becher/Einsatz |
| **Paraffin** | Langkettige Kohlenwasserstoffe im Diesel, kristallisieren bei Kälte |
| **Poliersystem** | Kraftstoff-Umwälzsystem zur permanenten Reinigung des Tankinhalts |
| **ppm** | Parts per million — Konzentrationseinheit (mg/kg oder ml/m³) |
| **Racor** | Parker Hannifin Racor Division — Marktführer marine Kraftstofffilter |
| **RCD** | Recreational Craft Directive 2013/53/EU — EU-Sportbootrichtlinie |
| **Sedimentation** | Absinken schwerer Partikel/Wasser durch Schwerkraft |
| **Separ** | SEPAR Filter GmbH — deutscher Hersteller von Kraftstofffiltern |
| **Spin-On** | Aufschraubbarer Filterpatrone (wie PKW-Ölfilter) |
| **Stratapore** | Fleetguard-Mehrschicht-Filtermedium-Technologie |
| **SWK** | SchmutzWasserKraftstoff — Separ-Filterbezeichnung |
| **T-Handle** | Racor-Schnellwechselgriff zum Lösen des Filterbechers |
| **Turbine** | Racor-Zentrifugal-Vorabscheider-Prinzip im Filtergehäuse |
| **Vakuummeter** | Unterdruckmessgerät am Filtergehäuse (Verschmutzungsanzeige) |
| **Wasserabscheider** | Gerät zur Trennung von Wasser aus Kraftstoff |
| **Zellulose** | Naturfaser-Filtermedium (Standard für die meisten Filtereinsätze) |

---

## 18. Schnell-Referenz

### 18.1 Racor Turbine-Serie — Übersicht

| Modell | Durchfluss (l/h) | Einsatz 10µm | Einsatz 2µm | Einsatz 30µm | Preis Gehäuse |
|---|---|---|---|---|---|
| 110A | 57 | R12T | R12S | R12P | €95–€130 |
| 120A | 114 | R12T | R12S | R12P | €95–€130 |
| 500FG | 227 | 2010TM-OR | 2010SM-OR | 2010PM-OR | €220–€320 |
| 900FG | 340 | 2040TM-OR | 2040SM-OR | 2040PM-OR | €350–€450 |
| 1000FG | 681 | 2020TM-OR | 2020SM-OR | 2020PM-OR | €480–€620 |
| 75900 | 1.135 | — | — | — | €2.500–€4.000 |

### 18.2 Separ SWK-2000 — Übersicht

| Modell | Durchfluss (l/h) | Einsatz 10µm | Einsatz 30µm | Preis Gehäuse |
|---|---|---|---|---|
| SWK-2000/5 | 75 | 01010 | 01030 | €150–€200 |
| SWK-2000/5/50 | 125 | 01051 | 01050 | €180–€240 |
| SWK-2000/10 | 250 | 02010 | 02030 | €250–€350 |
| SWK-2000/18 | 450 | 02018-10 | 02018-30 | €400–€520 |
| SWK-2000/40 | 1.000 | 02040-10 | 02040-30 | €600–€800 |

### 18.3 Empfehlung nach Bootsklasse

| Bootsklasse | Motor | Empfohlener Vorfilter | Feinheit | Duplex? |
|---|---|---|---|---|
| Segelyacht 8–10m | 10–20 PS | Racor 120A | 10µm | Nein |
| Segelyacht 10–14m | 20–50 PS | Racor 500FG | 10µm | Optional |
| Segelyacht 14–18m | 50–100 PS | Racor 500FG | 10µm | Empfohlen (Blauwasser) |
| Motoryacht 8–12m | 100–200 PS | Racor 500FG oder 900FG | 10µm | Optional |
| Motoryacht 12–18m | 200–500 PS (2×) | Racor 900FG (je Motor) | 10µm | Empfohlen |
| Motoryacht 18–24m | 500–1.000 PS (2×) | Racor 1000FG (je Motor) | 10µm/2µm | Ja |
| Superyacht 24m+ | 1.000+ PS (2×) | Racor 75900 oder zentral | 2µm | Pflicht |

### 18.4 Wartungsintervall-Schnellreferenz

| Komponente | Intervall Stunden | Intervall Zeit | Aktion |
|---|---|---|---|
| Sammelbecher | — | Wöchentlich | Kontrollieren, ggf. Wasser ablassen |
| Vorfilter-Einsatz | 200–500 h | 12 Monate | Wechseln |
| Motor-Feinfilter | Per Motorhersteller | 12 Monate | Wechseln |
| O-Ringe | Beim Einsatzwechsel | 12 Monate | Prüfen, ggf. tauschen |
| Vakuummeter | — | 24 Monate | Kalibrierung prüfen |
| Transparenter Becher | — | 5–7 Jahre | Auf Sprödigkeit prüfen, tauschen |
| Gehäuse (Aluminium) | — | Jährlich | Korrosionsschutz auftragen |
| Biozid (prophylaktisch) | — | Bei jeder Betankung | Erhaltungsdosierung zugeben |
| Dip-Slide-Test | — | 2× jährlich | Biologische Kontrolle |

### 18.5 Biozid-Dosierungs-Schnellreferenz

| Produkt | Erhaltungsdosis (pro Liter Diesel) | Schockdosis (pro Liter Diesel) | Häufigkeit Erhaltung |
|---|---|---|---|
| Grotamar 82 | 0,25 ml/l (1:4.000) | 1,0 ml/l (1:1.000) | Bei jeder Betankung |
| Biobor JF | 0,19 ml/l (1:5.400) | 0,37 ml/l (1:2.700) | Bei jeder Betankung |
| MarineLine DFC | 0,5 ml/l (1:2.000) | 1,0 ml/l (1:1.000) | Bei jeder Betankung |

### 18.6 Anschlussgewinde-Schnellreferenz

| Filtermodell | Eingangs-/Ausgangsgewinde | Adapter benötigt für |
|---|---|---|
| Racor 110A/120A | 3/8"-14 NPTF | Metrisch: M14×1,5 Adapter |
| Racor 500FG | 3/4"-16 UNF | Metrisch: M16×1,5 oder M18×1,5 Adapter |
| Racor 900FG | 1"-14 UNS | Metrisch: M22×1,5 Adapter |
| Racor 1000FG | 1"-14 UNS | Metrisch: M22×1,5 Adapter |
| Separ SWK-2000/5 | 3/8" BSP | Zoll: 3/8" NPT Adapter |
| Separ SWK-2000/10 | 3/4" BSP | Zoll: 3/4" NPT Adapter |
| Separ SWK-2000/18 | 1" BSP | Zoll: 1" NPT Adapter |
| Vetus WS180 | 3/8" BSP | Zoll: 3/8" NPT Adapter |
| Vetus WS720 | 3/4" BSP | Zoll: 3/4" NPT Adapter |

**Hinweis:** BSP (British Standard Pipe) und NPT (National Pipe Thread) sind NICHT kompatibel! BSP hat 55°-Flankenwinkel, NPT hat 60°. Immer passenden Adapter verwenden.

### 18.7 Notfall-Checkliste: Motor stirbt auf See ab

```
□ Ruhe bewahren — Diesel-Motorausfall ist fast immer Kraftstoffversorgung
□ Tankventil offen?
□ Sammelbecher prüfen — Wasser? → Ablassen
□ Vakuummeter — roter Bereich? → Einsatz wechseln
□ Einsatz wechseln (Ersatz an Bord!)
□ System entlüften (Handpumpe)
□ Motor starten
□ Wenn Problem bleibt: Motorfilter wechseln
□ Wenn Problem bleibt: Saugleitung auf Luft prüfen
□ Wenn Problem bleibt: Hilfe anfordern
```

---

## ANHANG A — Fallstudie: Segelyacht 38ft, Racor 500FG verstopft nach Tropentörn {#anhang-a}

### A.1 Ausgangslage

**Boot:** Bavaria 38 Cruiser, Baujahr 2014
**Motor:** Volvo Penta D2-40 (40 PS), mechanische Einspritzung
**Filtersystem:** Racor 500FG mit 2010TM-OR (10µm), seit 3 Jahren unverändert
**Vorgeschichte:** Transatlantik-Passage ARC (Las Palmas → St. Lucia), anschließend 6 Monate Karibik

### A.2 Symptome

- Motorleistung nahm über 3 Wochen graduell ab
- Beim Manövrieren im Hafen von Martinique: Motor starb ab
- Neustart gelang nach 2 Minuten, aber nur im Leerlauf stabil
- Vakuummeter (nachträglich installiert) zeigte 22 kPa (roter Bereich)

### A.3 Diagnose

1. **Filtereinsatz inspiziert:** Dunkelbraun bis schwarz, schleimiger Belag, deutlicher Geruch
2. **Sammelbecher:** 4 cm braunes, trübes Wasser mit Flocken
3. **Dip-Slide-Test:** >10⁵ CFU/ml — schwere Dieselpest
4. **Tankprobe (vom Boden):** Schwarze Schlieren, fauliger Geruch

### A.4 Ursache

- Diesel in Martinique/Guadeloupe von unbekannter Qualität getankt
- 6 Wochen Standzeit bei 35°C Außentemperatur (Motorraum >45°C)
- Tank war bei Standzeit nur zu 30% gefüllt (viel Luftraum = viel Kondensation)
- Kein Biozid prophylaktisch verwendet
- Biodiesel-Anteil des französischen Diesels (B7) begünstigte Wachstum

### A.5 Maßnahmen

1. Neuen Filtereinsatz eingesetzt (30µm zunächst, da 10µm sofort zusetzte)
2. Biozid-Schockbehandlung: Grotamar 82, 1:1.000
3. Motor 30 Min. laufen lassen
4. 30µm-Einsatz nach 8 Stunden Fahrt gewechselt (bereits stark verschmutzt)
5. Erneut 30µm-Einsatz, diesmal 40 Stunden Standzeit
6. Dann 10µm-Einsatz — hielt normal
7. Tankrückstand (unterste 50 Liter) abgepumpt und entsorgt
8. Dip-Slide-Test nach 4 Wochen: <10³ CFU/ml — kontrolliert

### A.6 Kosten

| Position | Betrag |
|---|---|
| 3× Filtereinsatz 2010TM-OR | €75 |
| 1× Filtereinsatz 2010PM-OR (30µm) | €22 |
| Grotamar 82, 500 ml | €45 |
| 2× Dip-Slide-Test | €40 |
| Diesel entsorgt (50 l) | €25 |
| **Gesamt** | **€207** |

### A.7 Lessons Learned

- **Biozid ist Pflicht in den Tropen** — €45 hätte das gesamte Problem verhindert
- **Tank voll halten** bei Standzeiten
- **Wöchentlich Sammelbecher kontrollieren** — auch bei stehendem Motor
- **Ersatzeinsätze verschiedener Feinheiten** mitführen (30µm für Notfälle)

**AYDI-Confidence:** documented (Eignerbericht, Fotos der Filtereinsätze)

---

## ANHANG B — Fallstudie: Motoryacht 45ft, Dieselpest im Mittelmeer {#anhang-b}

### B.1 Ausgangslage

**Boot:** Princess 45, Baujahr 2018
**Motoren:** 2× Volvo Penta D6-370 (370 PS), Common-Rail
**Filtersystem:** 2× Racor 900FG mit 2040TM-OR (10µm)
**Vorgeschichte:** Yacht lag 14 Monate in der Marina von Palma de Mallorca ohne Betrieb

### B.2 Symptome

- Beide Motoren sprangen nach Winterpause an, aber instabiler Leerlauf
- Unter Last (Hafenausfahrt): Steuerbord-Motor stotterte schwer
- Backbord-Motor: leichte Leistungsschwäche
- Alarmanlage: Wasserstandssensor Steuerbord ausgelöst

### B.3 Diagnose

1. **Steuerbord-Filter:** Einsatz komplett zugesetzt, Sammelbecher randvoll braunes Wasser + Schlamm
2. **Backbord-Filter:** Einsatz 60% zugesetzt, Sammelbecher halb Wasser
3. **Tankproben:** Beide Tanks kontaminiert, Steuerbord-Tank schlimmer (weniger gefüllt gewesen)
4. **Dip-Slide:** Steuerbord >10⁶, Backbord >10⁴ CFU/ml
5. **Motor-OEM-Filter:** Steuerbord bereits leicht verfärbt (Wasser/Biomasse hat Vorfilter passiert)

### B.4 Maßnahmen

1. Beide Filtereinsätze gewechselt (30µm zunächst)
2. Motor-OEM-Filter beider Motoren gewechselt (Vorsicht: Common-Rail)
3. Biozid in beide Tanks (Biobor JF, Schockdosierung)
4. Tanksammelbecher/Drains beider Tanks geöffnet — je ca. 5 Liter Wasser/Schlamm
5. Motoren 2 Stunden im Hafen laufen lassen (niedrige Drehzahl)
6. Nach 2 Wochen: 30µm gegen 10µm getauscht
7. Kraftstoff-Polier-System nachgerüstet (Jabsco-Pumpe + Racor 120A + Timer)
8. Injektoren-Check bei Volvo-Werkstatt: OK, keine Schäden

### B.5 Kosten

| Position | Betrag |
|---|---|
| 4× Racor 2040TM-OR + 4× 2040PM-OR | €308 |
| 2× Volvo Penta OEM-Filter D6 | €180 |
| Biobor JF, 2× 473ml | €120 |
| Tankdrainage (Marina-Service) | €150 |
| Kraftstoff-Poliersystem (Eigenbau) | €450 |
| Volvo-Werkstatt Injektoren-Check | €350 |
| 4× Dip-Slide-Tests | €80 |
| **Gesamt** | **€1.638** |

### B.6 Lessons Learned

- **14 Monate Standzeit ohne Vorbereitung** ist ein Garantie-Rezept für Dieselpest
- **Common-Rail-Motoren** sind anfälliger für Folgeschäden durch Wasser und Biomasse
- **Poliersystem nachrüsten** war die richtige Entscheidung — Timer läuft nun 4h/Tag
- **Wasserstandssensor** hat rechtzeitig gewarnt (Steuerbord)
- **Ergebnis:** Kein bleibender Motorschaden, aber €1.638 statt €45 für prophylaktisches Biozid

**AYDI-Confidence:** documented (Werftbericht Palma, Volvo-Service-Protokoll)

---

## ANHANG C — Fallstudie: Blauwasseryacht 52ft, Dual-Racor-System {#anhang-c}

### C.1 Ausgangslage

**Boot:** Hallberg-Rassy 52, Baujahr 2020
**Motor:** Volvo Penta D3-150 (150 PS), Common-Rail
**Filtersystem:** Racor 75500MAX (Dual-500FG-System), ab Werft
**Route:** Weltumsegelung, aktuell Pazifik (Tonga → Fiji → Neuseeland)

### C.2 Erfahrungsbericht (24 Monate, 2.800 Motorstunden)

| Filterwechsel-Nr. | Stunden | Ort | Befund | Einsatz |
|---|---|---|---|---|
| 1 | 350 | Las Palmas | Normal, leicht braun | 2010TM-OR (10µm) |
| 2 | 320 | Barbados | Mehr Verschmutzung als erwartet | 2010TM-OR |
| 3 | 180 | Panama | Stark verschmutzt, Diesel aus Colón | 2010TM-OR |
| 4 | 220 | Galapagos | Moderat, Diesel OK | 2010TM-OR |
| 5 | 400 | Marquesas | Sauber, wenig Motorbetrieb | 2010TM-OR |
| 6 | 350 | Tahiti | Normal | 2010TM-OR |
| 7 | 280 | Tonga | Leichte Biologische Spuren | 2010TM-OR |

### C.3 Dual-System Bewertung

**Umschaltvorgänge:** 3× in 24 Monaten (jeweils beim Filterwechsel der aktiven Seite)
**Echter Notfall-Umschaltvorgang:** 1× (Panama → Galapagos, Filter verstopfte nach schlechtem Diesel in Colón)

**Eigner-Zitat:** „Das Dual-System hat sich in Panama bezahlt gemacht. Mitten auf dem Pazifik, 700 Meilen von Land entfernt, den Motor wegen eines verstopften Filters zu verlieren — das will niemand. Die Umschaltung dauerte 3 Sekunden. Danke, Racor."

### C.4 Empfehlung des Eigners

- Dual-System ist für Blauwasser unverzichtbar
- 10µm-Einsätze für den Vorfilter reichen (D3-150 hat eigenen Feinfilter)
- 6 Ersatzeinsätze für den Vorfilter an Bord (immer!)
- 3 Ersatz-Motorfilter an Bord
- Biozid (Grotamar 82) nach jedem Tanken in fraglichen Gewässern
- Vakuummeter als Frühwarnung unbezahlbar

**AYDI-Confidence:** documented (Eignerbericht, Bordlogbuch)

---

## ANHANG D — Fallstudie: Charteryacht, Separ SWK-2000 Erstinstallation {#anhang-d}

### D.1 Ausgangslage

**Boot:** Jeanneau Sun Odyssey 440, Baujahr 2019
**Motor:** Yanmar 3JH5E (39 PS), mechanische Einspritzung
**Filtersystem:** Nur OEM-Yanmar-Spin-On-Filter (kein separater Vorfilter/Wasserabscheider)
**Problem:** Charterflotte in Kroatien, häufige Filterverstopfungen, 3 Motorausfälle in einer Saison

### D.2 Analyse

- Kein Vorfilter = gesamte Filtrationslast auf dem kleinen Motor-Spin-On
- Chartergäste tanken an verschiedenen Stellen (Qualität variiert)
- Kein Wasserabscheider = Wasser erreicht Motor direkt
- Motorraum-Zugang bei Spin-On-Wechsel umständlich

### D.3 Lösung

Installation eines Separ SWK-2000/5 als Vorfilter:
- Montage an der Motorraum-Schottseite (gut zugänglich)
- 3/8"-BSP-Anschlüsse in bestehende Leitung eingesetzt
- Transparenter Becher mit Drain-Schlauch in die Bilge
- 10µm-Einsatz (01010)
- Vakuummeter nachgerüstet

### D.4 Ergebnis

| Kennzahl | Vorher (1 Saison) | Nachher (2 Saisons) |
|---|---|---|
| Motorausfälle wegen Filter | 3 | 0 |
| Yanmar-OEM-Filterwechsel | 8 | 2 (regulär) |
| Beschwerden Chartergäste | 5 | 0 |
| Kosten Filter/Reparatur | €1.200 | €180 (Separ-Einsätze + Yanmar-Filter) |

### D.5 Investition

| Position | Betrag |
|---|---|
| Separ SWK-2000/5 Gehäuse | €165 |
| Einbau (Werft, 2 Std.) | €180 |
| Vakuummeter-Kit | €55 |
| Schläuche, Adapter, Schellen | €45 |
| **Gesamt** | **€445** |

**Amortisation:** Innerhalb einer halben Charter-Saison (keine Ausfälle = keine Entschädigung an Gäste)

**AYDI-Confidence:** documented (Charterfirma-Bericht, Werft-Rechnung)

---

## ANHANG E — Fallstudie: Fischereifahrzeug 12m, Fleetguard-Upgrade {#anhang-e}

### E.1 Ausgangslage

**Boot:** Fischereifahrzeug, GFK, 12m, Baujahr 2001
**Motor:** Cummins 6BTA 5.9 (250 PS), mechanische Einspritzung
**Filtersystem:** Original Fleetguard FS1242 (Spin-On), kein separater Vorfilter
**Einsatzgebiet:** Nordsee, 1.200 Betriebsstunden/Jahr

### E.2 Problem

- Filterlebensdauer nur 80–120 Stunden (statt 250+)
- Häufiges Motorstottern bei rauer See (Aufwirbeln von Sediment)
- 2× Injektor-Überholung in 3 Jahren (Abrasion durch Partikel)

### E.3 Lösung

1. Racor 1000FG als Vorfilter nachgerüstet (30µm-Einsatz)
2. Fleetguard FS1242 als Motorfilter beibehalten (10µm)
3. Tank professionell gereinigt (nach 23 Jahren erstmals!)
4. Tankansaugkorb erneuert (altes Sieb war korrodiert und hatte Löcher)

### E.4 Ergebnis

| Kennzahl | Vorher | Nachher |
|---|---|---|
| FS1242 Standzeit | 80–120 h | 350+ h |
| Racor 1000FG Standzeit | — | 200–250 h (30µm) |
| Motorstottern | 2–3× pro Woche | Eliminiert |
| Injektor-Überholung | Alle 1.500 h | >4.000 h (und laufend) |

### E.5 Kosten-Nutzen

| Position | Betrag |
|---|---|
| Racor 1000FG + Einbau | €850 |
| Tankreinigung | €800 |
| Neuer Ansaugkorb | €120 |
| **Investition gesamt** | **€1.770** |
| **Einsparung Jahr 1** (weniger Filter, keine Injektor-Überholung) | **€3.200** |

**AYDI-Confidence:** documented (Werftprotokoll, Motoren-Service-Buch)

---

## ANHANG F — Fallstudie: Superyacht 28m, zentrale Kraftstoffaufbereitung {#anhang-f}

### F.1 Ausgangslage

**Boot:** Custom Motoryacht 28m, Aluminium, Baujahr 2022
**Motoren:** 2× MAN D2676 LE433 (730 PS), Common-Rail
**Generator:** 1× Onan 27 kW Diesel
**Tankvolumen:** 2× 5.000 Liter Diesel (10.000 l gesamt)
**Filtersystem:** Zentrale Kraftstoffaufbereitung durch Klassenanforderung (RINA)

### F.2 Systemaufbau

```
Tanks (2× 5.000 l)
  → Zentrale Poliereinheit (24/7)
      - Alfa Laval Centrifuge MAB 103
      - Heizung (40°C konstant)
      - Partikelzähler ISO 4406
      - Wassergehalt-Sensor (ppm)
  → Duplex-Vorfilter (Racor 75900MAX je Motor)
      - 2µm Einsätze
      - Diff-Druckmanometer
      - Automatischer Wasseralarm
  → Motor-OEM-Filter (MAN)
  → Motoren
  → Rücklauf → Tanks
```

### F.3 Betriebserfahrung (3 Jahre)

| Kennzahl | Wert |
|---|---|
| Gesamtbetriebsstunden (Motoren) | 4.200 h |
| Vorfilter-Einsatzwechsel | 6× (alle 700 h) |
| Motor-OEM-Filterwechsel | 4× (alle 1.000 h) |
| Wasser abgeschieden (gesamt) | ca. 45 Liter |
| Dieselpest-Vorfälle | 0 |
| Injektoren-Probleme | 0 |
| Partikelzähler stets im Bereich | ISO 4406: 15/13/10 (gut) |

### F.4 Kosten (3 Jahre)

| Position | Betrag |
|---|---|
| Zentrale Poliereinheit (Installation) | €35.000 |
| Duplex-Vorfilter 2× (Installation) | €12.000 |
| Verbrauchsmaterial 3 Jahre | €2.400 |
| Wartung Zentrifuge (jährlich Service) | €4.500 |
| **Gesamt 3 Jahre** | **€53.900** |
| **Pro Jahr** | **€17.967** |
| **Pro Betriebsstunde** | **€12,83** |

### F.5 Bewertung

Für eine 28m-Yacht mit MAN-Motoren (Injektor-Satz: €18.000, Hochdruckpumpe: €12.000) ist die zentrale Aufbereitung eine Versicherung. Die Kosten von €13/h sind im Kontext der Gesamtbetriebskosten (€200–€400/h) marginal.

**AYDI-Confidence:** measured (RINA-Klassifikation, Service-Protokolle, Partikelzähler-Daten)

---

## ANHANG G — Fallstudie: Langfahrt-Katamaran, Vakuum-Entgasung {#anhang-g}

### G.1 Ausgangslage

**Boot:** Lagoon 450F, Baujahr 2017
**Motoren:** 2× Yanmar 4JH4-TE (54 PS), mechanische Einspritzung
**Tankvolumen:** 2× 300 Liter
**Problem:** Luftprobleme nach jedem Filterwechsel, Motor springt schlecht an

### G.2 Analyse

Der Lagoon 450F hat die Tanks seitlich in den Rümpfen, der Motorraum ist im Brückenbereich. Die Saugleitung ist lang (ca. 4m) und hat mehrere Bögen. Nach dem Filterwechsel:
- Lange Entlüftungsprozedur (15–20 Minuten pumpen)
- Restluft im System führt zu Startschwierigkeiten
- Bei Seegang: Luft wird an Hochpunkten der Leitung eingeschlossen

### G.3 Lösung

1. Elektrische Kraftstoff-Förderpumpe (Facet 40105) vor den Filter installiert
2. Entlüftungsventil am Filterkopf (Racor-Option)
3. Leitungsführung optimiert: Stetige Steigung, keine Hochpunkte
4. Absperrventile an beiden Seiten des Filters (für tropffreien Wechsel)

### G.4 Ergebnis

- Entlüftungszeit nach Filterwechsel: von 15–20 Min. auf 2–3 Min.
- Motorstart nach Filterwechsel: sofort, kein Stottern
- Elektrische Pumpe erleichtert auch die Kraftstoffversorgung bei niedrigem Tankstand

### G.5 Kosten

| Position | Betrag |
|---|---|
| Facet 40105 Kraftstoffpumpe | €85 |
| Einbau + Verkabelung | €200 |
| Entlüftungsventil | €25 |
| Absperrventile 2× | €40 |
| Leitungsänderung | €150 |
| **Gesamt** | **€500** |

**AYDI-Confidence:** documented (Eignerbericht, Installationsfotos)

---

## ANHANG H — Fallstudie: Regattayacht, Gewichtsoptimiertes Filtersystem {#anhang-h}

### H.1 Ausgangslage

**Boot:** J/121, Baujahr 2021
**Motor:** Yanmar 3YM30 (29 PS), mechanische Einspritzung
**Einsatz:** Offshore-Regatta (RORC, Fastnet) + Küstenregatten
**Anforderung:** Minimales Gewicht, maximale Zuverlässigkeit

### H.2 Analyse

- Standard-Racor 500FG: 1,5 kg leer, ca. 2,5 kg befüllt
- Für eine 12m-Regattayacht ist jedes Kilogramm relevant
- Motor läuft nur zum Manövrieren und Laden (50–100 h/Saison)
- Diesel-Qualität in Nordeuropa gut

### H.3 Lösung

- Racor 120A statt 500FG (Gewichtseinsparung: 1,0 kg befüllt)
- 10µm-Einsatz (R12T)
- Kein Vakuummeter (Gewicht/Komplexität)
- Kein Wasserstandssensor
- Einsatzwechsel 1× jährlich (niedrige Betriebsstunden)
- 1 Ersatzeinsatz an Bord (statt 2–3)

### H.4 Gewichtsvergleich

| System | Gewicht befüllt | Differenz |
|---|---|---|
| Racor 500FG + Vakuummeter + Sensor | 3,1 kg | Referenz |
| Racor 120A (minimiert) | 1,6 kg | -1,5 kg |
| Einsparung + 1 weniger Ersatzeinsatz | — | -1,7 kg gesamt |

### H.5 Bewertung

Für eine Regattayacht mit geringer Motornutzung, gutem Diesel und kurzen Distanzen ist die Minimallösung vertretbar. Für Offshore-Regatten (Fastnet, Sydney-Hobart): mindestens Racor 500FG empfohlen.

**AYDI-Confidence:** estimated (Eigner-Interview, keine Messdaten)

---

## ANHANG I — Pydantic v2 Modelle: FuelFilterAssessment {#anhang-i}

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class FilterCondition(str, Enum):
    """Condition assessment of a fuel filter element."""
    new = "new"
    good = "good"
    moderate = "moderate"
    contaminated = "contaminated"
    blocked = "blocked"
    not_assessable = "not_assessable"


class FilterType(str, Enum):
    """Type of fuel filter."""
    pre_filter_water_separator = "pre_filter_water_separator"
    secondary_engine_filter = "secondary_engine_filter"
    polishing_filter = "polishing_filter"
    centrifugal_separator = "centrifugal_separator"
    inline_filter = "inline_filter"


class FuelFilterAssessment(BaseModel):
    """Assessment of a fuel filter / water separator installation on a yacht."""
    model_config = {"from_attributes": True}

    boat_manufacturer: str = Field(..., description="Bootshersteller")
    boat_model: str = Field(..., description="Bootsmodell")
    boat_year: Optional[int] = Field(None, description="Baujahr")
    boat_length_m: float = Field(..., description="Bootslänge in Metern")

    engine_manufacturer: str = Field(..., description="Motorhersteller (Volvo Penta, Yanmar, Cummins, etc.)")
    engine_model: str = Field(..., description="Motormodell (z.B. D2-40, 3JH5E, QSB 5.9)")
    engine_power_kw: float = Field(..., description="Motorleistung in kW")
    engine_type: str = Field("diesel", description="Motortyp: diesel")
    injection_system: str = Field(..., description="Einspritzsystem: mechanical/common_rail")

    filter_manufacturer: str = Field(..., description="Filterhersteller (Racor, Separ, Vetus, etc.)")
    filter_model: str = Field(..., description="Filtermodell (z.B. 500FG, SWK-2000/10, WS720)")
    filter_type: FilterType = Field(..., description="Filtertyp")
    filter_element_part_number: Optional[str] = Field(None, description="Teilenummer des aktuellen Einsatzes")
    filter_element_micron: Optional[int] = Field(None, description="Filterfeinheit in µm (2, 10, 30)")
    filter_max_flow_lph: Optional[float] = Field(None, description="Maximaler Durchfluss in l/h")

    condition: FilterCondition = Field(..., description="Zustandsbewertung des Filtereinsatzes")
    element_age_hours: Optional[int] = Field(None, description="Betriebsstunden seit letztem Wechsel")
    element_age_months: Optional[int] = Field(None, description="Monate seit letztem Wechsel")
    water_in_bowl_ml: Optional[int] = Field(None, description="Geschätzte Wassermenge im Sammelbecher in ml")
    vacuum_gauge_installed: bool = Field(False, description="Vakuummeter installiert?")
    vacuum_reading_kpa: Optional[float] = Field(None, description="Aktuelle Vakuummeter-Anzeige in kPa")
    water_sensor_installed: bool = Field(False, description="Wasserstandssensor installiert?")
    dual_filter_system: bool = Field(False, description="Duplex-/Dual-Filtersystem?")
    polishing_system_installed: bool = Field(False, description="Kraftstoff-Poliersystem installiert?")

    diesel_pest_risk: str = Field("low", description="Dieselpest-Risiko: low/medium/high/active")
    biological_contamination_cfu: Optional[str] = Field(None, description="CFU/ml falls getestet (z.B. '<1000', '10^5')")

    score: Optional[int] = Field(None, ge=0, le=100, description="Gesamtbewertung 0-100")
    findings: List[str] = Field(default_factory=list, description="Liste der Befunde (deutsch)")
    recommendations: List[str] = Field(default_factory=list, description="Liste der Empfehlungen (deutsch)")
    confidence: str = Field("estimated", description="Confidence: measured/calculated/visual_high/visual_medium/estimated/documented")
```

---

## ANHANG J — Pydantic v2 Modelle: WaterSeparatorDiagnosis {#anhang-j}

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class WaterSource(str, Enum):
    """Identified or suspected source of water in the fuel system."""
    condensation = "condensation"
    fuel_quality = "fuel_quality"
    filler_cap_leak = "filler_cap_leak"
    tank_vent = "tank_vent"
    tank_corrosion = "tank_corrosion"
    deck_fitting_leak = "deck_fitting_leak"
    unknown = "unknown"


class WaterSeverity(str, Enum):
    """Severity of water contamination."""
    normal = "normal"
    elevated = "elevated"
    critical = "critical"
    emergency = "emergency"


class WaterSeparatorDiagnosis(BaseModel):
    """Diagnosis of water contamination in a yacht fuel system."""
    model_config = {"from_attributes": True}

    filter_model: str = Field(..., description="Filtermodell (z.B. 500FG, SWK-2000/10)")
    bowl_water_level_percent: int = Field(..., ge=0, le=100, description="Wasserstand im Sammelbecher in %")
    bowl_water_color: str = Field(..., description="Farbe des Wassers: clear/milky/brown/black/rusty")
    bowl_water_odor: str = Field("none", description="Geruch: none/slight/sulfurous/foul")
    water_volume_ml: Optional[int] = Field(None, description="Geschätztes Wasservolumen in ml")

    severity: WaterSeverity = Field(..., description="Schweregrad der Wasserkontamination")
    suspected_sources: List[WaterSource] = Field(default_factory=list, description="Verdächtige Wasserquellen")

    tank_volume_liters: Optional[int] = Field(None, description="Tankvolumen in Litern")
    tank_fill_level_percent: Optional[int] = Field(None, ge=0, le=100, description="Tankfüllstand in %")
    tank_material: Optional[str] = Field(None, description="Tankmaterial: steel/stainless/aluminum/grp/polyethylene")
    tank_age_years: Optional[int] = Field(None, description="Tankalter in Jahren")
    tank_last_cleaned: Optional[str] = Field(None, description="Letzte Tankreinigung (Datum oder 'never')")

    biocide_used: bool = Field(False, description="Biozid im Einsatz?")
    biocide_product: Optional[str] = Field(None, description="Biozid-Produkt (z.B. Grotamar 82)")
    dip_slide_result: Optional[str] = Field(None, description="Dip-Slide-Ergebnis (CFU/ml)")

    immediate_actions: List[str] = Field(default_factory=list, description="Sofortmaßnahmen (deutsch)")
    long_term_actions: List[str] = Field(default_factory=list, description="Langfristmaßnahmen (deutsch)")
    estimated_cost_eur: Optional[float] = Field(None, description="Geschätzte Kosten der Maßnahmen in EUR")
    confidence: str = Field("estimated", description="Confidence-Level")
```

---

## ANHANG K — Pydantic v2 Modelle: DieselPestAssessment {#anhang-k}

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


class DieselPestStage(str, Enum):
    """Stage of diesel pest contamination."""
    none = "none"
    early = "early"
    moderate = "moderate"
    severe = "severe"
    critical = "critical"


class DieselPestAssessment(BaseModel):
    """Assessment of microbiological contamination (Diesel Pest / Diesel Bug)."""
    model_config = {"from_attributes": True}

    stage: DieselPestStage = Field(..., description="Stadium der Dieselpest")
    cfu_per_ml: Optional[str] = Field(None, description="CFU/ml (z.B. '<1000', '10^4-10^5', '>10^6')")
    test_method: Optional[str] = Field(None, description="Testmethode: dip_slide/atp/laboratory/visual")
    organisms_identified: List[str] = Field(default_factory=list, description="Identifizierte Organismen")

    filter_slime_visible: bool = Field(False, description="Schleimbildung auf Filtereinsatz sichtbar?")
    foul_odor: bool = Field(False, description="Fauliger Geruch?")
    filter_blocked_rapidly: bool = Field(False, description="Filter verstopft schnell nach Wechsel?")
    dark_water_in_bowl: bool = Field(False, description="Dunkles Wasser im Sammelbecher?")

    tank_volume_liters: Optional[int] = Field(None, description="Tankvolumen in Litern")
    tank_water_content_estimated_liters: Optional[float] = Field(None, description="Geschätzter Wassergehalt im Tank in Litern")
    tank_standtime_weeks: Optional[int] = Field(None, description="Standzeit des Kraftstoffs in Wochen")
    biodiesel_percentage: Optional[float] = Field(None, description="Biodiesel-Anteil in % (z.B. 7.0 für B7)")
    climate_zone: str = Field("temperate", description="Klimazone: temperate/mediterranean/tropical/arctic")

    biocide_treatment_recommended: bool = Field(True, description="Biozid-Behandlung empfohlen?")
    biocide_product_recommended: Optional[str] = Field(None, description="Empfohlenes Biozid-Produkt")
    biocide_dosage_ml_per_liter: Optional[float] = Field(None, description="Empfohlene Dosierung ml pro Liter Diesel")
    tank_cleaning_required: bool = Field(False, description="Tankreinigung erforderlich?")
    estimated_remediation_cost_eur: Optional[float] = Field(None, description="Geschätzte Sanierungskosten in EUR")

    prevention_measures: List[str] = Field(default_factory=list, description="Empfohlene Präventionsmaßnahmen (deutsch)")
    confidence: str = Field("estimated", description="Confidence-Level")
```

---

## ANHANG L — Pydantic v2 Modelle: FilterMaintenanceRecord {#anhang-l}

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date


class FilterMaintenanceRecord(BaseModel):
    """Record of a fuel filter maintenance event."""
    model_config = {"from_attributes": True}

    maintenance_date: date = Field(..., description="Datum der Wartung")
    maintenance_type: str = Field(..., description="Art: element_change/water_drain/inspection/full_service")
    engine_hours: Optional[int] = Field(None, description="Betriebsstunden am Motor")

    filter_position: str = Field(..., description="Position: pre_filter_port/pre_filter_starboard/engine_filter_port/engine_filter_starboard/polishing")
    filter_model: str = Field(..., description="Filtermodell")
    old_element_part_number: Optional[str] = Field(None, description="Alte Einsatz-Teilenummer")
    new_element_part_number: Optional[str] = Field(None, description="Neue Einsatz-Teilenummer")
    old_element_condition: Optional[str] = Field(None, description="Zustand alt: clean/light/moderate/heavy/blocked/biological")

    water_drained_ml: Optional[int] = Field(None, description="Abgelassenes Wasser in ml")
    water_color: Optional[str] = Field(None, description="Wasserfarbe: clear/milky/brown/black/rusty")
    vacuum_reading_before_kpa: Optional[float] = Field(None, description="Vakuummeter vor Wechsel in kPa")
    vacuum_reading_after_kpa: Optional[float] = Field(None, description="Vakuummeter nach Wechsel in kPa")

    biocide_added: bool = Field(False, description="Biozid zugegeben?")
    biocide_product: Optional[str] = Field(None, description="Biozid-Produkt")
    biocide_amount_ml: Optional[int] = Field(None, description="Biozid-Menge in ml")

    o_ring_replaced: bool = Field(False, description="O-Ring ersetzt?")
    bowl_cleaned: bool = Field(False, description="Becher gereinigt?")
    air_bleeding_performed: bool = Field(True, description="Entlüftung durchgeführt?")
    air_bleeding_issues: bool = Field(False, description="Probleme bei der Entlüftung?")

    notes: Optional[str] = Field(None, description="Zusätzliche Anmerkungen")
    cost_eur: Optional[float] = Field(None, description="Kosten in EUR")
    performed_by: str = Field("owner", description="Durchgeführt von: owner/mechanic/yard")
    confidence: str = Field("documented", description="Confidence-Level")
```

---

## ANHANG M — Pydantic v2 Modelle: FuelSystemConfiguration {#anhang-m}

```python
from pydantic import BaseModel, Field
from typing import Optional, List


class FilterStage(BaseModel):
    """Single filter stage in a fuel system configuration."""
    model_config = {"from_attributes": True}

    position: str = Field(..., description="Position: pre_filter/engine_filter/polishing_filter")
    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modell")
    micron_rating: int = Field(..., description="Filterfeinheit in µm")
    max_flow_lph: float = Field(..., description="Max. Durchfluss in l/h")
    water_separator: bool = Field(True, description="Wasserabscheider integriert?")
    duplex: bool = Field(False, description="Duplex-System (2 Filter umschaltbar)?")
    vacuum_gauge: bool = Field(False, description="Vakuummeter installiert?")
    water_sensor: bool = Field(False, description="Wasserstandssensor installiert?")
    heated: bool = Field(False, description="Beheizter Filterkopf?")


class FuelSystemConfiguration(BaseModel):
    """Complete fuel system filter configuration for a yacht."""
    model_config = {"from_attributes": True}

    boat_manufacturer: str = Field(..., description="Bootshersteller")
    boat_model: str = Field(..., description="Bootsmodell")
    boat_year: Optional[int] = Field(None, description="Baujahr")
    boat_length_m: float = Field(..., description="Bootslänge in Metern")
    boat_type: str = Field(..., description="Bootstyp: sailboat/motorboat/catamaran/trawler/superyacht")

    engine_count: int = Field(1, description="Anzahl Hauptmotoren")
    engine_manufacturer: str = Field(..., description="Motorhersteller")
    engine_model: str = Field(..., description="Motormodell")
    engine_power_kw: float = Field(..., description="Leistung pro Motor in kW")
    injection_system: str = Field(..., description="Einspritzsystem: mechanical/common_rail")
    fuel_consumption_max_lph: Optional[float] = Field(None, description="Max. Verbrauch pro Motor in l/h")

    tank_count: int = Field(1, description="Anzahl Dieseltanks")
    tank_total_volume_liters: int = Field(..., description="Gesamtes Tankvolumen in Litern")
    tank_material: str = Field("stainless", description="Tankmaterial: steel/stainless/aluminum/grp/polyethylene")

    filter_stages: List[FilterStage] = Field(default_factory=list, description="Filtrationsstufen")
    polishing_system: bool = Field(False, description="Kraftstoff-Poliersystem installiert?")
    polishing_system_type: Optional[str] = Field(None, description="Typ: timer_pump/centrifuge/continuous")

    ce_category: Optional[str] = Field(None, description="CE-Kategorie: A/B/C/D")
    classification_society: Optional[str] = Field(None, description="Klassifikation: lloyds/rina/dnv/bv/abs/none")

    overall_score: Optional[int] = Field(None, ge=0, le=100, description="Gesamtbewertung 0-100")
    adequacy_assessment: Optional[str] = Field(None, description="Angemessenheit: excellent/adequate/marginal/insufficient")
    recommendations: List[str] = Field(default_factory=list, description="Empfehlungen (deutsch)")
    confidence: str = Field("estimated", description="Confidence-Level")
```

---

## ANHANG N — Pydantic v2 Modelle: FilterElementSpecification {#anhang-n}

```python
from pydantic import BaseModel, Field
from typing import Optional, List


class FilterElementSpecification(BaseModel):
    """Technical specification of a fuel filter element / cartridge."""
    model_config = {"from_attributes": True}

    part_number: str = Field(..., description="Teilenummer (z.B. 2010TM-OR, 01010, FS1242)")
    manufacturer: str = Field(..., description="Hersteller (Racor, Separ, Vetus, Fleetguard, etc.)")
    fits_housing: str = Field(..., description="Passend für Gehäuse (z.B. 500FG, SWK-2000/5)")

    media_type: str = Field(..., description="Filtermedium: cellulose/synthetic/nylon_screen/cellulose_polymer")
    micron_rating: int = Field(..., description="Filterfeinheit in µm")
    micron_type: str = Field("nominal", description="Filterfeinheit-Typ: nominal/absolute")
    beta_value: Optional[str] = Field(None, description="Beta-Wert (z.B. 'β10=200')")

    height_mm: Optional[float] = Field(None, description="Höhe in mm")
    outer_diameter_mm: Optional[float] = Field(None, description="Außendurchmesser in mm")
    inner_diameter_mm: Optional[float] = Field(None, description="Innendurchmesser in mm")

    o_ring_included: bool = Field(False, description="O-Ring im Lieferumfang?")
    o_ring_part_number: Optional[str] = Field(None, description="O-Ring Teilenummer (separat)")
    water_separation_efficiency_percent: Optional[float] = Field(None, description="Wasserabscheide-Effizienz in %")
    water_absorber: bool = Field(False, description="Wasserabsorber-Polymer enthalten?")
    reusable: bool = Field(False, description="Wiederverwendbar (reinigbar)?")

    price_eur_min: Optional[float] = Field(None, description="Mindestpreis in EUR")
    price_eur_max: Optional[float] = Field(None, description="Höchstpreis in EUR")

    service_life_hours: Optional[int] = Field(None, description="Empfohlene Standzeit in Betriebsstunden")
    service_life_months: Optional[int] = Field(None, description="Empfohlene Standzeit in Monaten")

    cross_reference: List[str] = Field(default_factory=list, description="Vergleichbare Teilenummern anderer Hersteller")
    notes: Optional[str] = Field(None, description="Zusätzliche Hinweise")
    confidence: str = Field("measured", description="Confidence-Level")
```

---

## ANHANG O — Pydantic v2 Modelle: FuelQualityTest {#anhang-o}

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import date


class FuelQualityTest(BaseModel):
    """Result of a fuel quality test / analysis."""
    model_config = {"from_attributes": True}

    test_date: date = Field(..., description="Testdatum")
    test_location: str = Field(..., description="Ort der Probenahme")
    sample_source: str = Field(..., description="Quelle: tank_bottom/tank_mid/filter_bowl/fuel_line/jerry_can")

    visual_clarity: str = Field(..., description="Visuelle Klarheit: clear/hazy/cloudy/opaque")
    visual_color: str = Field(..., description="Farbe: amber/dark_amber/brown/black")
    odor: str = Field("normal", description="Geruch: normal/stale/sulfurous/foul/solvent")
    particulate_visible: bool = Field(False, description="Sichtbare Partikel/Flocken?")

    water_content_ppm: Optional[int] = Field(None, description="Wassergehalt in ppm (Karl-Fischer oder Schnelltest)")
    free_water_present: bool = Field(False, description="Freie Wasserphase sichtbar?")
    free_water_volume_ml: Optional[int] = Field(None, description="Menge freies Wasser in ml (Probe)")

    biological_test_method: Optional[str] = Field(None, description="Bio-Testmethode: dip_slide/atp/laboratory/none")
    biological_cfu_per_ml: Optional[str] = Field(None, description="CFU/ml Ergebnis")
    biological_assessment: Optional[str] = Field(None, description="Bewertung: clean/low/moderate/high/critical")

    iso_4406_code: Optional[str] = Field(None, description="ISO 4406 Reinheitsklasse (z.B. '18/16/13')")
    cetane_number: Optional[float] = Field(None, description="Cetanzahl (falls gemessen)")
    sulfur_content_ppm: Optional[int] = Field(None, description="Schwefelgehalt in ppm")
    biodiesel_percent: Optional[float] = Field(None, description="Biodiesel-Anteil in %")

    overall_quality: str = Field(..., description="Gesamtqualität: good/acceptable/poor/unacceptable")
    actions_required: List[str] = Field(default_factory=list, description="Erforderliche Maßnahmen (deutsch)")
    confidence: str = Field("measured", description="Confidence-Level")
```

---

## ANHANG P — Pydantic v2 Modelle: TroubleshootingResult {#anhang-p}

```python
from pydantic import BaseModel, Field
from typing import Optional, List


class DiagnosticStep(BaseModel):
    """A single step in a troubleshooting diagnostic process."""
    model_config = {"from_attributes": True}

    step_number: int = Field(..., description="Schrittnummer")
    question: str = Field(..., description="Diagnosefrage (deutsch)")
    answer: Optional[str] = Field(None, description="Antwort: yes/no/unknown/value")
    conclusion: Optional[str] = Field(None, description="Schlussfolgerung aus diesem Schritt (deutsch)")
    next_step: Optional[int] = Field(None, description="Nächster Schritt basierend auf Antwort")


class TroubleshootingResult(BaseModel):
    """Result of a fuel system troubleshooting session."""
    model_config = {"from_attributes": True}

    symptom: str = Field(..., description="Ausgangssymptom (deutsch, z.B. 'Motorleistungsverlust')")
    symptom_category: str = Field(..., description="Kategorie: power_loss/stalling/smoke/odor/noise/starting/water")

    diagnostic_steps: List[DiagnosticStep] = Field(default_factory=list, description="Durchlaufene Diagnoseschritte")
    steps_completed: int = Field(0, description="Anzahl abgeschlossener Schritte")

    root_cause_identified: bool = Field(False, description="Grundursache identifiziert?")
    root_cause: Optional[str] = Field(None, description="Identifizierte Grundursache (deutsch)")
    root_cause_component: Optional[str] = Field(None, description="Betroffene Komponente: pre_filter/engine_filter/fuel_line/tank/injection/other")
    root_cause_severity: Optional[str] = Field(None, description="Schweregrad: minor/moderate/serious/critical")

    recommended_actions: List[str] = Field(default_factory=list, description="Empfohlene Maßnahmen (deutsch, priorisiert)")
    parts_needed: List[str] = Field(default_factory=list, description="Benötigte Teile (Teilenummern)")
    estimated_repair_time_minutes: Optional[int] = Field(None, description="Geschätzte Reparaturzeit in Minuten")
    estimated_cost_eur: Optional[float] = Field(None, description="Geschätzte Kosten in EUR")
    professional_required: bool = Field(False, description="Fachwerkstatt erforderlich?")

    confidence: str = Field("estimated", description="Confidence-Level")
```

---

## ANHANG Q — Pydantic v2 Modelle: FilterCostEstimate {#anhang-q}

```python
from pydantic import BaseModel, Field
from typing import Optional, List


class CostLineItem(BaseModel):
    """A single line item in a cost estimate."""
    model_config = {"from_attributes": True}

    category: str = Field(..., description="Kategorie: hardware/element/consumable/labor/disposal")
    description: str = Field(..., description="Beschreibung (deutsch)")
    part_number: Optional[str] = Field(None, description="Teilenummer (falls zutreffend)")
    quantity: int = Field(1, description="Menge")
    unit_price_eur: float = Field(..., description="Stückpreis in EUR")
    total_price_eur: float = Field(..., description="Gesamtpreis in EUR")
    recurring: bool = Field(False, description="Wiederkehrend (jährlich)?")
    recurring_interval_months: Optional[int] = Field(None, description="Wiederkehr-Intervall in Monaten")


class FilterCostEstimate(BaseModel):
    """Cost estimate for fuel filter system installation or upgrade."""
    model_config = {"from_attributes": True}

    estimate_type: str = Field(..., description="Typ: new_installation/upgrade/annual_maintenance/repair/tank_remediation")
    boat_model: str = Field(..., description="Bootsmodell")
    engine_model: str = Field(..., description="Motormodell")

    line_items: List[CostLineItem] = Field(default_factory=list, description="Kostenpositionen")
    total_one_time_eur: float = Field(0, description="Einmalige Gesamtkosten in EUR")
    total_annual_recurring_eur: float = Field(0, description="Jährlich wiederkehrende Kosten in EUR")
    total_5_year_cost_eur: Optional[float] = Field(None, description="5-Jahres-Gesamtkosten in EUR")

    comparison_notes: Optional[str] = Field(None, description="Vergleichshinweise (z.B. vs. Injektorreparatur)")
    cost_benefit_ratio: Optional[str] = Field(None, description="Kosten-Nutzen-Bewertung: excellent/good/moderate/poor")
    confidence: str = Field("estimated", description="Confidence-Level")
    price_date: str = Field("2025-2026", description="Preisstand")
```

---

## ANHANG R — AYDI Bewertungsschema für Kraftstofffiltersysteme {#anhang-r}

### R.1 Bewertungskriterien

| Kriterium | Gewichtung | 100 Punkte | 75 Punkte | 50 Punkte | 25 Punkte | 0 Punkte |
|---|---|---|---|---|---|---|
| **Filterfeinheit** | 15% | ≤2µm (Common-Rail angemessen) | 10µm (mechanisch OK) | 30µm (nur Vorfilter) | >30µm | Kein Filter |
| **Wasserabscheidung** | 15% | Koaleszenz + Sensor + Alarm | Koaleszenz ohne Sensor | Nur Schwerkraft | Minimal | Keine |
| **Durchfluss-Dimensionierung** | 15% | >2× Motorbedarf | 1,5–2× | 1,0–1,5× | 0,5–1,0× | <0,5× |
| **Duplex-System** | 10% | Duplex vorhanden | Einzelfilter + 3+ Ersatz | Einzelfilter + 1–2 Ersatz | Einzelfilter ohne Ersatz | — |
| **Vakuummeter** | 5% | Installiert, kalibriert | Installiert, unkalibriert | Nicht installiert | — | — |
| **Zugänglichkeit** | 10% | Werkzeugloser Wechsel <5 Min. | <10 Min. mit Werkzeug | <30 Min. | >30 Min. | Nicht zugänglich |
| **Montagequalität** | 10% | Senkrecht, schwingungsfrei, geschützt | Leichte Neigung, akzeptabel | Deutliche Neigung | Stark geneigt | Waagerecht |
| **Wartungszustand** | 10% | Aktuell gewartet, dokumentiert | Leicht überfällig | Deutlich überfällig | Stark überfällig | Nie gewartet |
| **Dieselpest-Prävention** | 5% | Biozid + Poliersystem + Test | Biozid regelmäßig | Biozid gelegentlich | Kein Biozid | Aktive Kontamination |
| **Ersatzteile an Bord** | 5% | Komplett (Einsätze, O-Ringe, Biozid) | Einsätze vorhanden | Nur 1 Einsatz | Keine | — |

### R.2 Gesamtbewertung

| Punktzahl | Bewertung | Darstellung |
|---|---|---|
| 90–100 | Ausgezeichnet — vorbildliche Installation | Grünes Badge |
| 75–89 | Gut — geringe Verbesserungsmöglichkeiten | Grünes Badge |
| 60–74 | Befriedigend — Verbesserungen empfohlen | Gelbes Badge |
| 40–59 | Mangelhaft — Handlungsbedarf | Oranges Badge |
| 20–39 | Ungenügend — dringender Handlungsbedarf | Rotes Badge |
| 0–19 | Kritisch — Motorgefährdung, sofortige Maßnahmen | Rotes Badge (blinkend) |

### R.3 Automatische Befund-Generierung

```python
from pydantic import BaseModel, Field
from typing import List, Optional


class FilterSystemScore(BaseModel):
    """Automated scoring result for a fuel filter system assessment."""
    model_config = {"from_attributes": True}

    filtration_score: int = Field(..., ge=0, le=100, description="Teilbewertung Filterfeinheit")
    water_separation_score: int = Field(..., ge=0, le=100, description="Teilbewertung Wasserabscheidung")
    flow_dimensioning_score: int = Field(..., ge=0, le=100, description="Teilbewertung Durchfluss")
    duplex_score: int = Field(..., ge=0, le=100, description="Teilbewertung Duplex/Ersatzteile")
    vacuum_gauge_score: int = Field(..., ge=0, le=100, description="Teilbewertung Vakuummeter")
    accessibility_score: int = Field(..., ge=0, le=100, description="Teilbewertung Zugänglichkeit")
    installation_quality_score: int = Field(..., ge=0, le=100, description="Teilbewertung Montagequalität")
    maintenance_score: int = Field(..., ge=0, le=100, description="Teilbewertung Wartungszustand")
    diesel_pest_prevention_score: int = Field(..., ge=0, le=100, description="Teilbewertung Dieselpest-Prävention")
    spare_parts_score: int = Field(..., ge=0, le=100, description="Teilbewertung Ersatzteile")

    overall_score: int = Field(..., ge=0, le=100, description="Gewichtete Gesamtbewertung")
    grade: str = Field(..., description="Bewertungsgrad: excellent/good/satisfactory/poor/insufficient/critical")
    badge_color: str = Field(..., description="Badge-Farbe: green/yellow/orange/red")

    critical_findings: List[str] = Field(default_factory=list, description="Kritische Befunde (deutsch)")
    warnings: List[str] = Field(default_factory=list, description="Warnungen (deutsch)")
    recommendations: List[str] = Field(default_factory=list, description="Empfehlungen (deutsch)")
    estimated_upgrade_cost_eur: Optional[float] = Field(None, description="Geschätzte Kosten für empfohlene Verbesserungen")

    structured_weight: float = Field(0.85, description="Gewichtung strukturierte Analyse")
    visual_weight: float = Field(0.15, description="Gewichtung visuelle Analyse")
    confidence: str = Field("estimated", description="Confidence-Level")
```

### R.4 Beispiel-Bewertungen nach Bootsklasse

**Segelyacht 12m, Yanmar 3JH5E, Racor 500FG (10µm), kein Duplex, kein Vakuummeter, gut gewartet:**
- Filterfeinheit: 75 (10µm für mechanische Einspritzung OK)
- Wasserabscheidung: 75 (Koaleszenz, kein Sensor)
- Durchfluss: 100 (500FG weit überdimensioniert für 39 PS)
- Duplex: 50 (kein Duplex, 2 Ersatz an Bord)
- Vakuummeter: 0 (nicht installiert)
- Zugänglichkeit: 75 (10 Minuten mit Werkzeug)
- Montagequalität: 100 (senkrecht, schwingungsfrei)
- Wartungszustand: 100 (aktuell, dokumentiert)
- Dieselpest-Prävention: 50 (Biozid gelegentlich)
- Ersatzteile: 75 (Einsätze + O-Ringe vorhanden)
- **Gewichtet: 75 — Gut**
- **Empfehlung:** Vakuummeter nachrüsten (€50), Biozid-Routine etablieren

**Motoryacht 18m, 2× Volvo D6-370 (Common-Rail), Racor 1000FG (10µm), Duplex, Vakuummeter, Wasserstandssensor:**
- Filterfeinheit: 75 (10µm — für Common-Rail besser 2µm)
- Wasserabscheidung: 100 (Koaleszenz + Sensor + Alarm)
- Durchfluss: 100 (1000FG für D6 ausreichend)
- Duplex: 100 (Duplex vorhanden)
- Vakuummeter: 100 (installiert und kalibriert)
- Zugänglichkeit: 100 (Maschinenraum, werkzeugloser Wechsel)
- Montagequalität: 100
- Wartungszustand: 100
- Dieselpest-Prävention: 75 (Biozid regelmäßig)
- Ersatzteile: 100 (komplett)
- **Gewichtet: 95 — Ausgezeichnet**
- **Empfehlung:** 2µm-Einsätze für optimalen Common-Rail-Schutz erwägen

---

### R.5 Empfohlene Verbesserungen nach Bewertung

| Aktuelle Bewertung | Empfohlene Maßnahmen | Geschätzte Kosten | Erwartete Verbesserung |
|---|---|---|---|
| 0–19 (Kritisch) | Vorfilter installieren (Racor 500FG), Tankinspektion | €400–€800 | +40–60 Punkte |
| 20–39 (Ungenügend) | Filtereinsatz wechseln, Vakuummeter nachrüsten | €100–€200 | +20–30 Punkte |
| 40–59 (Mangelhaft) | Ersatzeinsätze besorgen, Biozid-Routine etablieren | €80–€150 | +15–25 Punkte |
| 60–74 (Befriedigend) | Vakuummeter, Wasserstandssensor nachrüsten | €100–€200 | +10–15 Punkte |
| 75–89 (Gut) | Poliersystem erwägen, Duplex für Blauwasser | €500–€1.500 | +5–10 Punkte |
| 90–100 (Ausgezeichnet) | Wartungsintervalle beibehalten | €80–€150/Jahr | Niveau halten |

### R.6 Automatische Warnmeldungen (AYDI-Integration)

| Bedingung | Warnung (deutsch) | Priorität |
|---|---|---|
| Filterfeinheit >30µm bei Common-Rail | „Filterfeinheit unzureichend für Common-Rail-Motor. Mindestens 10µm erforderlich." | HOCH |
| Kein Wasserabscheider installiert | „Kein Wasserabscheider im Kraftstoffsystem erkannt. Risiko für Motorschäden." | HOCH |
| Filter waagerecht montiert | „Filter nicht senkrecht montiert. Wasserabscheidung stark eingeschränkt." | HOCH |
| Kein Duplex bei CE-Kategorie A | „Einfaches Filtersystem bei Ozean-Kategorie. Duplex-System empfohlen." | MITTEL |
| Vakuummeter fehlt | „Kein Vakuummeter installiert. Filterverschmutzung nicht erkennbar." | NIEDRIG |
| Transparenter Becher >5 Jahre | „Becher-Material möglicherweise spröde. Inspektion empfohlen." | NIEDRIG |
| Aluminium-Gehäuse + Kupferleitung | „Galvanische Korrosion möglich. Messingadapter empfohlen." | MITTEL |
| Keine Ersatzeinsätze an Bord | „Keine Ersatzfilter an Bord. Mindestens 2 Einsätze empfohlen." | MITTEL |

---

## ANHANG S — Saisonale Wartungsplanung für Kraftstofffiltersysteme

### S.1 Nordeuropa (Saison Mai–Oktober, Winterlager November–April)

| Zeitpunkt | Maßnahme | Dauer | Kosten |
|---|---|---|---|
| **Saisonstart (April/Mai)** | | | |
| | Sammelbecher kontrollieren und leeren | 5 Min. | €0 |
| | Tankprobe visuell beurteilen | 5 Min. | €0 |
| | Dip-Slide-Test durchführen | 5 Min. + 48h | €15–€25 |
| | Filtereinsatz prüfen (wenn bei Einwinterung gewechselt: OK) | 5 Min. | €0 |
| | Leitungen und Verschraubungen auf Dichtheit prüfen | 10 Min. | €0 |
| | System entlüften, Motor starten | 15 Min. | €0 |
| **Während der Saison (wöchentlich)** | | | |
| | Sammelbecher visuell prüfen | 1 Min. | €0 |
| | Vakuummeter ablesen | 1 Min. | €0 |
| | Wasser ablassen (bei Befund) | 3 Min. | €0 |
| **Mitte Saison (Juli/August)** | | | |
| | Sammelbecher leeren und reinigen | 10 Min. | €0 |
| | Tankprobe Sichtprüfung | 5 Min. | €0 |
| | Biozid nachfüllen (Erhaltungsdosierung) | 5 Min. | €5–€10 |
| **Saisonende (Oktober/November)** | | | |
| | Filtereinsatz wechseln | 20 Min. | €20–€45 |
| | Motor-OEM-Filter wechseln (wenn fällig) | 15 Min. | €20–€65 |
| | Tank randvoll füllen | — | Dieselkosten |
| | Biozid Schockdosierung (wenn Kontamination) oder Erhaltung | 5 Min. | €10–€25 |
| | Stabilisator-Additiv zugeben | 5 Min. | €5–€10 |
| | Motor 20 Min. laufen lassen | 20 Min. | €5 (Diesel) |
| | Sammelbecher leeren | 5 Min. | €0 |
| | Gehäuse mit Korrosionsschutz behandeln | 10 Min. | €5 |
| **Jährliche Gesamtkosten** | | ca. 3 Std. | **€85–€185** |

### S.2 Mittelmeer (Ganzjahresbetrieb, reduziert im Winter)

| Zeitpunkt | Maßnahme | Besonderheit |
|---|---|---|
| **Monatlich** | Sammelbecher leeren | Höhere Kondensation im Sommer |
| **Alle 3 Monate** | Dip-Slide-Test | Höheres Dieselpest-Risiko |
| **Alle 6 Monate** | Filtereinsatz wechseln | Kürzere Intervalle als Nordeuropa |
| **Jährlich** | Motor-OEM-Filter wechseln | Standard |
| **Jährlich** | Tankdrain öffnen und Bodenwasser ablassen | Wichtig bei Stahltanks |
| **Alle 2 Jahre** | Tank professionell inspizieren | Korrosion unter Biofilm |
| **Bei jeder Betankung** | Biozid Erhaltungsdosierung | Pflicht im Mittelmeer |

### S.3 Tropen (Ganzjahresbetrieb)

| Zeitpunkt | Maßnahme | Besonderheit |
|---|---|---|
| **Wöchentlich** | Sammelbecher leeren | Extreme Kondensation |
| **Monatlich** | Filtereinsatz inspizieren | Hohe biologische Last |
| **Alle 2–3 Monate** | Filtereinsatz wechseln | ×0,5 Standardintervall |
| **Alle 2–3 Monate** | Dip-Slide-Test | Permanente Überwachung |
| **Bei jeder Betankung** | Biozid Erhaltungsdosierung + filtern beim Tanken | Pflicht |
| **Alle 6 Monate** | Tank Bodenwasser ablassen | Pflicht |
| **Jährlich** | Tank professionell reinigen | Bei Langfahrt empfohlen |

---

## ANHANG T — Bezugsquellen und Online-Händler

### T.1 Deutschland

| Händler | Website | Spezialisierung | Lager |
|---|---|---|---|
| SVB Yacht-Zubehör | www.svb-marine.de | Marine-Vollsortiment | Bremen |
| Toplicht | www.toplicht.de | Marine-Vollsortiment | Hamburg |
| Compass24 | www.compass24.de | Marine-Vollsortiment | Kiel |
| AWN | www.awn.de | Marine-Vollsortiment | Bremen |
| Bukh-Bremen | www.bukh-bremen.de | Motoren + Filter | Bremen |
| Bootsbedarf | www.bootsbedarf.de | Marine-Vollsortiment | Diverse |
| Schiffsausrüster Wellsee | www.wellsee-schiffsausruester.de | Profibedarf | Kiel |

### T.2 International

| Händler | Website | Land | Stärke |
|---|---|---|---|
| Fisheries Supply | www.fisheriessupply.com | USA | Racor-Komplettsortiment |
| West Marine | www.westmarine.com | USA | Breitestes Sortiment USA |
| Marine Deals | www.marinedeals.co.nz | Neuseeland | Pazifik/Australien |
| Jimmy Green Marine | www.jimmygreen.com | UK | Segelbedarf UK |
| Force 4 Chandlery | www.force4.co.uk | UK | Marine-Vollsortiment UK |
| Nautic Markt | www.nautic-markt.ch | Schweiz | D-A-CH Markt |
| Accastillage Diffusion | www.accastillage-diffusion.com | Frankreich | Französischer Markt |

### T.3 Direkt beim Hersteller

| Hersteller | Direktbestellung möglich? | Mindestbestellwert |
|---|---|---|
| Racor (Parker) | Über Händlernetz, nicht direkt | — |
| Separ | Ja, telefonisch oder per E-Mail | €50 |
| Vetus | Über Händlernetz | — |
| Fleetguard | Über Cummins-Händler | — |
| Mann+Hummel | Über Fachhandel | — |

---

## ANHANG U — Confidence-Mapping für AYDI-Integration

### U.1 Datenquellen und Confidence-Level

| Datentyp | Quelle | Confidence |
|---|---|---|
| Technische Spezifikationen (Durchfluss, Feinheit) | Hersteller-Datenblätter | measured |
| Teilenummern und Kompatibilität | Hersteller-Kataloge | measured |
| Preise | Händler-Websites (2025/26) | documented |
| Wechselintervalle | Hersteller-Empfehlungen | measured |
| Wechselintervalle (Korrekturfaktoren) | Erfahrungswerte Werften | estimated |
| Fehlerbilder | Sammelauswertung Praxis + Foren | documented |
| Troubleshooting-Bäume | Fachkonsens Bootsmechaniker | documented |
| Dieselpest-Stadien | Wissenschaftliche Literatur + Praxis | documented |
| Biozid-Dosierungen | Hersteller-TDS | measured |
| Kosten Tanksanierung | Werft-Angebote (Spanne) | estimated |
| Forum-Konsens | Segelpressen, Kreuzer-Abteilung, YachtForum | estimated |
| Fallstudien A–H | Eignerberichte, Werftprotokolle | documented |
| Pydantic-Modelle | AYDI-Entwicklung | measured |

### U.2 Gewichtungsfaktoren für Score Fusion

Für die AYDI-Analyse des Kraftstofffiltersystems gelten folgende Gewichtungen:

| Analyse-Aspekt | Strukturiert (Pipeline A) | Visuell (Pipeline B) | Begründung |
|---|---|---|---|
| Filterfeinheit | 0,90 | 0,10 | Teilenummer aus Datenblatt, visuell kaum erkennbar |
| Wasserabscheidung | 0,70 | 0,30 | Systemkonfiguration aus Specs, Becher visuell prüfbar |
| Durchfluss-Dimensionierung | 1,00 | 0,00 | Rein rechnerisch, nicht visuell |
| Montagequalität | 0,30 | 0,70 | Visuell gut erkennbar (Neigung, Zugänglichkeit) |
| Wartungszustand | 0,40 | 0,60 | Visuell: Korrosion, Becher-Zustand, Tropfen |
| Dieselpest-Risiko | 0,80 | 0,20 | Primär aus Betriebsdaten, visuell nur bei geöffnetem Filter |
| Ersatzteile an Bord | 0,90 | 0,10 | Dokumentation/Inventar, visuell schwer zu beurteilen |
| Leitungsqualität | 0,40 | 0,60 | Visuell: Knicke, Material, Anschlüsse sichtbar |
| Gehäusekorrosion | 0,20 | 0,80 | Primär visuell erkennbar |
| Gesamtsystem-Konfiguration | 0,85 | 0,15 | Aus Bootsklasse und Motorspezifikation ableitbar |

### U.3 Visuelle Analyse — Erkennbare Merkmale

Für Pipeline B (Visual Analysis) sind folgende Merkmale an Kraftstofffiltern visuell erkennbar:

| Merkmal | Erkennbarkeit | Visual Confidence |
|---|---|---|
| Filtergehäuse-Hersteller (Logo) | Gut bei klarem Foto | visual_high |
| Filtermodell (Größe, Form) | Gut bei Vergleichsfoto | visual_high |
| Montagelage (senkrecht?) | Gut | visual_high |
| Sammelbecher-Zustand (Wasser, Trübung) | Gut bei klarem Becher | visual_medium |
| Gehäusekorrosion | Gut | visual_high |
| Vakuummeter vorhanden/Anzeige | Mittel (Größe/Auflösung) | visual_medium |
| Filtereinsatz-Zustand | Nur bei geöffnetem Filter | visual_medium |
| Leitungsqualität | Mittel (Detailansicht nötig) | visual_medium |
| Zugänglichkeit | Gut bei Übersichtsfoto | visual_medium |
| Dual-System | Gut | visual_high |
| Tropfen/Leck | Schwierig (nur bei aktivem Leck) | visual_low |

### U.4 Prompt-Hinweise für Pipeline B (Visual Analysis)

Wenn ein Foto des Kraftstofffiltersystems analysiert wird, sollte der Visual-Prompt folgende Aspekte abfragen:

1. **Identifikation:** Welcher Hersteller/welches Modell ist erkennbar? (Logo, Gehäuseform, Farbgebung)
2. **Montagelage:** Ist das Filtergehäuse senkrecht montiert? Neigungswinkel schätzen.
3. **Sammelbecher:** Ist der transparente Becher sichtbar? Wasserstand? Verfärbung? Trübung?
4. **Korrosion:** Zeigt das Gehäuse Anzeichen von Korrosion (weiße Ablagerungen bei Aluminium)?
5. **Vakuummeter:** Ist ein Vakuummeter installiert? Welchen Wert zeigt es (falls ablesbar)?
6. **Duplex-System:** Sind zwei Filter parallel erkennbar? Umschaltventil sichtbar?
7. **Leitungen:** Welches Material (Kupfer, Schlauch)? Knicke? Zustand der Schlauchschellen?
8. **Zugänglichkeit:** Kann der Filtereinsatz offensichtlich leicht gewechselt werden?
9. **Umgebung:** Motorraum-Zustand allgemein — sauber, Ölspuren, Dieselspuren?
10. **Poliersystem:** Ist eine zusätzliche Pumpe/Filter-Kombination erkennbar?

**Confidence-Regeln für visuelle Filteranalyse:**
- Klares Detailfoto, Marke/Modell lesbar: visual_high
- Übersichtsfoto, Gehäuse erkennbar aber Details unscharf: visual_medium
- Teilweise verdeckt, schlechte Beleuchtung: visual_low
- Nicht im Bild oder nicht identifizierbar: visual_insufficient → „nicht beurteilbar"

---

*Ende der Wissensdatei 19.02 — Kraftstofffilter und Wasserabscheider im Yachtbau*
