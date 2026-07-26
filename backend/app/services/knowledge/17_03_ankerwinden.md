---
titel: "Ankerwinden — Typen, Installation und Wartung"
kategorie: "Anker und Kette"
unterkategorie: "Ankerwinden"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 17_03 — Ankerwinden — Typen, Installation und Wartung

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Windentypen](#2-windentypen)
3. [Hersteller-Datenbank](#3-hersteller-datenbank)
4. [Dimensionierung](#4-dimensionierung)
5. [Installation](#5-installation)
6. [Kettennuss-Kompatibilität](#6-kettennuss-kompatibilität)
7. [Fernbedienung und Kettenzähler](#7-fernbedienung-und-kettenzähler)
8. [Fehlerbild-Atlas](#8-fehlerbild-atlas)
9. [Troubleshooting](#9-troubleshooting)
10. [Wartung](#10-wartung)
11. [FAQ](#11-faq)
12. [Glossar](#12-glossar)
13. [Schnell-Referenz](#13-schnell-referenz)
14. [ANHANG A–H: Fallstudien](#14-anhang-a-h-fallstudien)
15. [ANHANG I–R: Pydantic v2 Datenmodelle](#15-anhang-i-r-pydantic-v2-datenmodelle)

---

## 1. Einführung

### 1.1 Zweck dieses Dokuments

Dieses Dokument stellt die zentrale Wissensbasis für alle Aspekte rund um
Ankerwinden im Yachtdesign dar. Es dient als Referenz für die AYDI-Analyse-Engine
zur Bewertung von Ankerwindensystemen in den Bereichen Dimensionierung,
Kompatibilität, Installation, Wartung und Fehlererkennung.

Ankerwinden (engl. anchor windlasses) sind eines der sicherheitsrelevantesten
Ausrüstungsteile an Bord einer Yacht. Ein Versagen der Ankerwindenanlage kann
in kritischen Situationen — Sturmankern, Notankern, Ankermanöver in engem
Revier — zu erheblichen Schäden oder Gefahr für die Besatzung führen.

### 1.2 Relevanz für die Yachtkonstruktion

Die Ankerwindenanlage beeinflusst zahlreiche Aspekte des Yachtdesigns:

- **Strukturell**: Deckverstärkung, Lastenverteilung, Kettenkasten-Integration
- **Elektrisch**: Batteriekapazität, Kabelquerschnitte, Absicherung
- **Hydraulisch**: Pumpenkapazität, Leitungsführung, Tankgröße
- **Gewichtsverteilung**: Vorschiffslast, Trimm-Einfluss
- **Ergonomie**: Bedienbarkeit, Sicherheitsabstände, Fußschalterposition
- **Ästhetik**: Integration ins Deckslayout, oberflächenbündige Lösungen

### 1.3 Historische Entwicklung

Die Entwicklung der Ankerwindenanlage auf Yachten lässt sich in Epochen einteilen:

| Zeitraum | Technologie | Merkmale |
|----------|------------|----------|
| Vor 1950 | Reine Handwinden | Spillkopf, Kurbel, Klüse |
| 1950–1970 | Erste elektrische Winden | Schwere Gleichstrommotoren, einfache Getriebe |
| 1970–1990 | Standardisierung | Vertikalwinden dominant, Solenoid-Steuerung |
| 1990–2010 | Elektronische Integration | Kettenzähler, Fernbedienung, Auto-Anker |
| 2010–heute | Smart-Systeme | GPS-Ankerüberwachung, App-Steuerung, CAN-Bus |

### 1.4 Normative Grundlagen

Relevante Normen für Ankerwinden im Yachtbereich:

| Norm | Titel | Relevanz |
|------|-------|----------|
| ISO 15084:2003 | Ankern, Vertäuen und Schleppen — Starke Punkte | Belastungsanforderungen |
| ISO 15085:2003 | Mann-über-Bord-Verhütung | Sicherheitsabstände am Bug |
| CE 2013/53/EU | Sportboot-Richtlinie | Gesamtsicherheit |
| DIN 766 | Rundstahlkette — Kurzgliedrig | Kettenmaße, Toleranzen |
| DIN 764 | Rundstahlkette — Mittelgliedrig | Alternative Kettenspezifikation |
| ISO 4565 | Ankerausrüstung für Yachten | Dimensionierungsgrundlage |

### 1.5 Begriffsabgrenzung

Im Sprachgebrauch werden verschiedene Begriffe synonym oder verwechselt verwendet:

- **Ankerwinsch** / **Ankerwinde** / **Ankerwindlass**: Oberbegriff für die gesamte Anlage
- **Spillkopf** (engl. capstan): Vertikale Trommel für Tauwerk
- **Kettennuss** (engl. gypsy / wildcat): Zahnrad für kalibrierte Kette
- **Kombiwinde**: Anlage mit Kettennuss UND Spillkopf
- **Verholwinsch**: Spillkopf ohne Kettennuss (nur für Leinen)
- **Bugstrahlruder**: NICHT zu verwechseln — eigenes System

### 1.6 Einordnung im AYDI-Analysesystem

Innerhalb der AYDI-Analyse wird die Ankerwinde in folgenden Modulen bewertet:

- **Strukturanalyse**: Deckverstärkung, Lasteinleitung
- **Compliance**: CE-Konformität, Sicherheitsabstände
- **Ergonomie**: Bedienbarkeit, Zugänglichkeit
- **Materialanalyse**: Korrosionsbeständigkeit, Materialwahl
- **Kostenanalyse**: Anschaffung, Installation, Lifecycle-Kosten
- **Wartungsanalyse**: Wartungsintervalle, Zugänglichkeit

### 1.7 Confidence-Level-Zuordnung

| Datenquelle | Confidence-Level | Beispiel |
|-------------|-----------------|----------|
| CAD-Modell mit installierter Winde | `measured` | Exakte Positionierung, Kabelquerschnitt |
| Foto der Ankerwindeninstallation | `visual_high` bis `visual_low` | Windentyp erkennbar, Zustand beurteilbar |
| Herstellerspezifikation | `documented` | Zugkraft, Leistungsaufnahme |
| Bootsklasse-Schätzung | `estimated` | Typische Windengröße für 12m Segelyacht |
| Servicebericht | `documented` | Wartungszustand, Fehlermeldungen |

---

## 2. Windentypen

### 2.1 Übersicht der Bauformen

Ankerwinden lassen sich nach mehreren Kriterien klassifizieren:

**Nach Achsorientierung:**
- Vertikalwinde (vertical windlass)
- Horizontalwinde (horizontal windlass)

**Nach Antrieb:**
- Handwinde (manual)
- Elektrisch 12V
- Elektrisch 24V
- Hydraulisch
- Kombination elektrisch/manuell (Notbetrieb)

**Nach Funktion:**
- Reine Kettenwinde (nur Kettennuss)
- Kombiwinde (Kettennuss + Spillkopf)
- Spillkopf (nur Tauwerk, keine Kettennuss)

### 2.2 Vertikalwinde (Vertical Windlass)

#### 2.2.1 Konstruktionsprinzip

Bei der Vertikalwinde befindet sich die Kettennuss an Deck, der Motor
unterhalb des Decks im Kettenkasten oder einem separaten Motorraum.
Die Antriebswelle verläuft vertikal durch das Deck.

```
     ┌─────────────┐
     │  Spillkopf   │  ← An Deck sichtbar
     ├─────────────┤
     │  Kettennuss  │  ← An Deck sichtbar
     ╠═════════════╣  ← Decksdurchführung (abgedichtet)
     │  Getriebe    │  ← Unter Deck
     │  Motor       │  ← Unter Deck
     └─────────────┘
```

#### 2.2.2 Vorteile Vertikalwinde

| Vorteil | Erläuterung |
|---------|------------|
| Geringe Decksfläche | Nur Kettennuss/Spillkopf an Deck sichtbar |
| Bessere Ästhetik | Schlankere Optik, weniger Aufbauten am Vorschiff |
| Großer Kettenfall | Kette fällt nahezu senkrecht in den Kettenkasten |
| Bessere Selbstverlegung | Kette legt sich besser im Kasten ab |
| Höherer Umlenkwinkel | Besserer Ketteneinlauf in die Nuss |
| Motor geschützt | Motor unter Deck, weniger Spritzwasser |
| Weniger Korrosion | Mechanik unter Deck, trockener |

#### 2.2.3 Nachteile Vertikalwinde

| Nachteil | Erläuterung |
|----------|------------|
| Decksdurchführung | Zusätzliche Abdichtung nötig |
| Tieferer Einbau | Braucht Platz unter Deck |
| Schwieriger Zugang | Motor unter Deck schlechter erreichbar |
| Wartung aufwändiger | Zum Motor muss unter Deck gearbeitet werden |
| Höheres Gewicht | Durch vertikale Bauweise insgesamt schwerer |
| Teurer | Generell 10–20% teurer als Horizontalwinden |

#### 2.2.4 Typischer Einsatzbereich

- Segelyachten ab 8m (28 ft)
- Motoryachten ab 7m (23 ft)
- Boote mit viel Platz im Vorschiff unter Deck
- Ästhetisch anspruchsvolle Installationen
- Boote mit tief liegendem Vorschiffsdeck

#### 2.2.5 Leistungsbereiche

| Bootsgröße | Typische Zugkraft | Motorleistung | Stromaufnahme (12V) |
|------------|------------------|---------------|---------------------|
| 7–9m | 300–500 kg | 300–500 W | 25–45 A |
| 9–12m | 500–800 kg | 500–800 W | 45–70 A |
| 12–15m | 800–1.200 kg | 700–1.200 W | 60–100 A |
| 15–18m | 1.200–2.000 kg | 1.000–1.500 W | 80–130 A |
| 18–24m | 2.000+ kg | 1.500–3.000 W | Meist 24V |

### 2.3 Horizontalwinde (Horizontal Windlass)

#### 2.3.1 Konstruktionsprinzip

Bei der Horizontalwinde befinden sich Motor, Getriebe und Kettennuss
komplett an Deck. Die Antriebswelle verläuft horizontal.

```
     ┌───────┬───────────┬──────────┐
     │ Motor │  Getriebe │ Kettennuss│  ← Alles an Deck
     └───────┴───────────┴──────────┘
     ══════════════════════════════════  ← Deck
```

#### 2.3.2 Vorteile Horizontalwinde

| Vorteil | Erläuterung |
|---------|------------|
| Einfache Installation | Keine Decksdurchführung nötig |
| Kein Platz unter Deck nötig | Alles an Deck, Kettenkasten unabhängig |
| Guter Zugang | Motor direkt zugänglich für Wartung |
| Wartungsfreundlicher | Alle Komponenten sichtbar und erreichbar |
| Günstiger | Generell 10–20% günstiger als Vertikalwinden |
| Leichter | Kompaktere Bauform, weniger Gesamtgewicht |
| Flexibler | Einfacher nachrüstbar auf bestehenden Booten |

#### 2.3.3 Nachteile Horizontalwinde

| Nachteil | Erläuterung |
|----------|------------|
| Große Decksfläche | Gesamte Anlage an Deck sichtbar |
| Mehr Spritzwasser | Motor und Getriebe exponiert |
| Flacherer Ketteneinlauf | Kette läuft flacher in den Kasten |
| Schlechtere Selbstverlegung | Kette stapelt sich eher |
| Ästhetisch dominanter | Große Einheit am Vorschiff |
| Stolpergefahr | Aufbau auf dem Deck |
| Mehr Korrosion | Alle Teile dem Wetter ausgesetzt |

#### 2.3.4 Typischer Einsatzbereich

- Motorboote ab 5m (16 ft)
- Sportboote und Fischerboote
- Nachrüstungen (kein Platz unter Deck)
- Boote mit flachem Vorschiff
- Arbeitsboote und Trawler-Yachten
- Katamarane (häufig, da kein tiefer Vorschiffsbereich)

#### 2.3.5 Leistungsbereiche

| Bootsgröße | Typische Zugkraft | Motorleistung | Stromaufnahme (12V) |
|------------|------------------|---------------|---------------------|
| 5–7m | 200–350 kg | 200–400 W | 18–35 A |
| 7–10m | 350–600 kg | 400–700 W | 35–60 A |
| 10–14m | 600–1.000 kg | 600–1.000 W | 50–85 A |
| 14–18m | 1.000–1.500 kg | 900–1.500 W | 75–130 A |
| 18–24m | 1.500+ kg | 1.200–2.500 W | Meist 24V |

### 2.4 Handwinde (Manual Capstan)

#### 2.4.1 Konstruktionsprinzip

Rein mechanische Winde ohne Motor. Betrieb über Handkurbel oder
Hebelarm. Untersetzungsgetriebe multipliziert die Handkraft.

#### 2.4.2 Vorteile

- Keine Stromversorgung nötig
- Extrem zuverlässig (wenige bewegliche Teile)
- Leicht und kompakt
- Günstig (150–500 EUR)
- Kein elektrischer Wartungsaufwand
- Ideal als Backup-System

#### 2.4.3 Nachteile

- Hoher Kraftaufwand bei großen Ankern
- Langsam (typisch 3–5 m/min)
- Nur für kleine Boote bis ~10m praktikabel
- Ermüdend bei großer Wassertiefe
- Nicht geeignet für Solo-Segler auf größeren Booten

#### 2.4.4 Einsatzbereich

- Segelboote bis 8m (26 ft)
- Kleinere Motorboote bis 7m (23 ft)
- Tagessegler und Regattaboote
- Backup-System auf größeren Yachten
- Budgetorientierte Eigner

#### 2.4.5 Typische Modelle

| Modell | Zugkraft | Kettengrößen | Gewicht | Preis EUR |
|--------|---------|-------------|---------|-----------|
| Lofrans Cayman 88 Manual | 250 kg | 6–8 mm | 4,2 kg | 280–350 |
| Maxwell Roper | 200 kg | 6–7 mm | 3,8 kg | 220–300 |
| Italwinch Manual Compact | 180 kg | 6 mm | 3,5 kg | 150–220 |

### 2.5 Elektrische Ankerwinde 12V

#### 2.5.1 Konstruktionsprinzip

Gleichstrommotor mit 12V Bordnetz-Anbindung. Permanentmagnet- oder
Reihenschlussmotor mit Schnecken- oder Stirnradgetriebe. Steuerung
über Solenoid-Relais (Auf/Ab), bedient via Fußschalter, Decksschalter
oder Fernbedienung.

#### 2.5.2 Elektrische Kenndaten

| Parameter | Typischer Bereich |
|-----------|------------------|
| Nennspannung | 12V DC |
| Stromaufnahme (Last) | 30–130 A |
| Stromaufnahme (Leerlauf) | 8–25 A |
| Spitzenstrom (Ankerbruch) | bis 200 A |
| Empfohlene Batterie | min. 100 Ah |
| Einschaltdauer (Duty Cycle) | 3–5 min kontinuierlich |
| Sicherung / Automat | 60–150 A (je nach Modell) |
| Kabelquerschnitt | 16–50 mm² (je nach Länge/Strom) |

#### 2.5.3 Vorteile 12V

- Kompatibel mit Standard-Bordnetz
- Breites Modellspektrum verfügbar
- Einfache Installation
- Günstigere Modelle als 24V
- Große Auswahl an Zubehör

#### 2.5.4 Nachteile 12V

- Hohe Ströme (→ dicke Kabel)
- Spannungsabfall bei langen Kabelwegen
- Begrenzte Leistung bei großen Booten
- Motor wird bei Dauerlast heiß
- Batterie-Belastung erheblich

#### 2.5.5 Einsatzbereich

- Boote bis ca. 15m (50 ft)
- Yachten mit 12V Bordnetz
- Kettengewicht bis ca. 120 kg

### 2.6 Elektrische Ankerwinde 24V

#### 2.6.1 Konstruktionsprinzip

Identisches Prinzip wie 12V, aber mit 24V Gleichstrommotor. Halbiert
den Strom bei gleicher Leistung (P = U × I).

#### 2.6.2 Elektrische Kenndaten

| Parameter | Typischer Bereich |
|-----------|------------------|
| Nennspannung | 24V DC |
| Stromaufnahme (Last) | 15–80 A |
| Stromaufnahme (Leerlauf) | 5–15 A |
| Spitzenstrom (Ankerbruch) | bis 120 A |
| Empfohlene Batterie | min. 80 Ah (24V) |
| Einschaltdauer (Duty Cycle) | 5–8 min kontinuierlich |
| Sicherung / Automat | 40–100 A |
| Kabelquerschnitt | 10–35 mm² |

#### 2.6.3 Vorteile 24V

- Halbierter Strom → dünnere Kabel
- Weniger Spannungsabfall
- Höhere Leistung möglich
- Längere Einschaltdauer
- Motor läuft kühler
- Geeignet für große Yachten

#### 2.6.4 Nachteile 24V

- Erfordert 24V Bordnetz oder separaten Batteriekreis
- Weniger Modellauswahl im kleinen Leistungsbereich
- Teurer als 12V-Äquivalente (ca. 15–25% Aufpreis)
- 24V Batterien/Ladegeräte benötigt

#### 2.6.5 Einsatzbereich

- Yachten ab 12m (40 ft)
- Alle Yachten mit 24V Bordnetz
- Superyachten bis 24m
- Boote mit langem Kabelweg (>8m)
- Schwere Ankersysteme

### 2.7 Hydraulische Ankerwinde

#### 2.7.1 Konstruktionsprinzip

Hydraulikmotor treibt die Winde an. Hydraulikpumpe (PTO am Hauptmotor
oder separate Elektropumpe) erzeugt den Druck. Steuerventile regeln
Richtung und Geschwindigkeit.

```
  ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐
  │  Motor / │────→│ Hydraulik│────→│ Steuer-  │────→│ Hydraulik│
  │  PTO     │     │  pumpe   │     │  ventil  │     │  motor   │
  └──────────┘     └──────────┘     └──────────┘     └──────────┘
                                                            │
                                                     ┌──────────┐
                                                     │ Getriebe │
                                                     │ Kettennuss│
                                                     └──────────┘
```

#### 2.7.2 Hydraulische Kenndaten

| Parameter | Typischer Bereich |
|-----------|------------------|
| Betriebsdruck | 80–200 bar |
| Volumenstrom | 5–25 l/min |
| Pumpenleistung | 1,5–7,5 kW |
| Hydrauliköltyp | ISO VG 32 oder VG 46 |
| Tankgröße | 5–25 Liter |
| Schlauchdimensionen | DN 10 – DN 16 |

#### 2.7.3 Vorteile Hydraulisch

| Vorteil | Erläuterung |
|---------|------------|
| Höchste Zugkraft | Bis 10.000+ kg möglich |
| Dauerbetrieb | Kein Duty-Cycle-Limit |
| Stufenlose Regelung | Geschwindigkeit proportional zum Ventilhub |
| Leiser Betrieb | Hydraulikmotor an Deck sehr leise |
| Kein Stromkabelproblem | Hydraulikschläuche statt dicker Kabel |
| Robuster Betrieb | Unempfindlich gegen Überlast |
| Multifunktion | Pumpe kann auch Bugstrahlruder etc. versorgen |

#### 2.7.4 Nachteile Hydraulisch

| Nachteil | Erläuterung |
|----------|------------|
| Hohe Kosten | System 3.000–15.000 EUR |
| Komplexe Installation | Schläuche, Pumpe, Tank, Ventile |
| Wartungsintensiver | Ölwechsel, Filterwechsel, Dichtungen |
| Braucht Hauptmotor | PTO-Pumpe nur bei laufendem Motor |
| Leckagegefahr | Hydrauliköl im Bilge problematisch |
| Gewicht | Gesamtsystem schwerer |
| Platzbedarf | Tank, Pumpe, Leitungen brauchen Platz |

#### 2.7.5 Einsatzbereich

- Yachten ab 18m (60 ft)
- Superyachten und Megayachten
- Arbeitsschiffe und Trawler
- Boote mit schwerem Ankergeschirr (>200 kg)
- Boote mit vorhandenem Hydrauliksystem
- Dauer-Ankerbetrieb (Charterflotten)

### 2.8 Kombiwinde (Seil + Kette)

#### 2.8.1 Konstruktionsprinzip

Kombiwinden vereinen eine Kettennuss für kalibrierte Ankerkette mit
einem Spillkopf (Trommel, Capstan) für Tauwerk. Dies ermöglicht:

- Kettenankern über die Kettennuss
- Kombinations-Ankersystem (Kette + Leine) über beide
- Verholarbeiten über den Spillkopf
- Leinenhandling (Fender, Spring, Mooring)

#### 2.8.2 Konfigurationen

| Konfiguration | Beschreibung | Typische Anwendung |
|--------------|-------------|-------------------|
| Oben Spillkopf / Unten Kettennuss | Standard-Vertikalwinde | Segelyachten |
| Kettennuss + seitlicher Spillkopf | Horizontalwinde mit Zubehör | Motorboote |
| Doppel-Kettennuss | Zwei Ankerketten | Katamarane, große Motoryachten |
| Kettennuss + Verholwinde | Separate Trommel | Trawler-Yachten |

#### 2.8.3 Seil-Kette-Kombination (Rode)

Die häufigste Ankerkonfiguration für Yachten unter 15m ist eine
Kombination aus Kette und Ankerleine:

| Bootsgröße | Kette (m) | Leine (m) | Kettengröße | Leinendurchmesser |
|------------|----------|----------|-------------|-------------------|
| 6–8m | 5–10 | 30–50 | 6 mm | 10–12 mm |
| 8–10m | 10–20 | 40–60 | 8 mm | 12–14 mm |
| 10–12m | 15–30 | 50–70 | 8–10 mm | 14–16 mm |
| 12–15m | 30–50 | 60–80 | 10 mm | 16–18 mm |
| 15m+ | 50–80+ | — | 10–12 mm | — (Ganzkette) |

#### 2.8.4 Vor- und Nachteile Kombiwinde

**Vorteile:**
- Vielseitig einsetzbar
- Eine Winde für alle Anker- und Verholarbeiten
- Platzsparend (eine statt zwei Winden)
- Kombinations-Rode möglich

**Nachteile:**
- Teurer als reine Kettenwinde (+15–30%)
- Schwerer
- Komplexer (mehr Verschleißteile)
- Spillkopf muss zur Leine passen

### 2.9 Vergleichsmatrix aller Windentypen

| Kriterium | Vertikal | Horizontal | Hand | Elektr. 12V | Elektr. 24V | Hydraulisch |
|-----------|---------|-----------|------|------------|------------|-------------|
| Bootsgröße | 7–24m | 5–24m | bis 10m | bis 15m | 12–24m | 18m+ |
| Zugkraft max | 3.000 kg | 2.500 kg | 500 kg | 2.000 kg | 3.000 kg | 10.000+ kg |
| Installation | Mittel | Einfach | Einfach | Mittel | Mittel | Komplex |
| Wartung | Mittel | Einfach | Minimal | Mittel | Mittel | Hoch |
| Kosten (System) | Mittel–Hoch | Niedrig–Mittel | Niedrig | Niedrig–Mittel | Mittel–Hoch | Hoch |
| Ästhetik | Gut | Mäßig | Gut | — | — | — |
| Dauerbetrieb | — | — | Unbegrenzt | 3–5 min | 5–8 min | Unbegrenzt |
| Zuverlässigkeit | Hoch | Hoch | Sehr hoch | Gut | Gut | Sehr gut |

### 2.10 Entscheidungsmatrix nach Bootsgröße

| Bootsgröße | Empfohlener Typ | Antrieb | Budget-Bereich EUR |
|------------|----------------|---------|-------------------|
| 5–7m | Horizontal | Hand oder 12V | 150–800 |
| 7–9m | Vertikal oder Horizontal | 12V | 500–1.500 |
| 9–12m | Vertikal | 12V | 1.000–2.500 |
| 12–15m | Vertikal | 12V oder 24V | 1.800–4.000 |
| 15–18m | Vertikal | 24V | 3.000–6.000 |
| 18–24m | Vertikal | 24V oder Hydraulik | 5.000–15.000 |
| 24m+ | Vertikal | Hydraulik | 10.000–50.000+ |

---

## 3. Hersteller-Datenbank

### 3.1 Marktübersicht

Der Ankerwinden-Markt für Yachten wird von wenigen Herstellern dominiert:

| Hersteller | Herkunft | Marktsegment | Marktanteil (geschätzt) |
|-----------|---------|-------------|----------------------|
| Lofrans | Italien | Alle Segmente | ~25% |
| Lewmar | UK | Alle Segmente | ~20% |
| Quick | Italien | Mittel–Hoch | ~18% |
| Maxwell | Australien/NZ | Mittel–Hoch | ~12% |
| Muir | Australien | Hoch–Premium | ~8% |
| Italwinch | Italien | Budget–Mittel | ~7% |
| Vetus | Niederlande | Budget–Mittel | ~5% |
| Diverse | — | Niche | ~5% |

### 3.2 Lofrans — Detaillierte Modellübersicht

Lofrans S.r.l., gegründet 1966 in Monfalcone, Italien. Einer der
weltweit führenden Hersteller von Ankerwinden für Yachten.

#### 3.2.1 Lofrans Tigres

Kompakte Vertikalwinde für kleine bis mittlere Segelyachten.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch |
| **Zugkraft** | 500 kg |
| **Motorleistung** | 500 W |
| **Spannung** | 12V oder 24V |
| **Stromaufnahme (12V)** | 45 A (Last) |
| **Stromaufnahme (24V)** | 22 A (Last) |
| **Kettengrößen** | 6, 7, 8 mm DIN 766 |
| **Kettennuss** | Aluminium, chrombeschichtet |
| **Seildurchmesser** | 10–14 mm (mit Spillkopf) |
| **Duty Cycle** | 3 min bei Volllast |
| **Gewicht (Motor)** | 9,5 kg |
| **Gewicht (Kopf)** | 4,2 kg |
| **Decksdurchführung** | Ø 105 mm |
| **Geeignet für Boote** | 7–10m |
| **Preis EUR** | 850–1.100 |
| **Zubehör** | Fußschalter, Kettenzähler optional |

#### 3.2.2 Lofrans Dorado

Mittlere Vertikalwinde, Flaggschiff für Segelyachten 10–14m.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch |
| **Zugkraft** | 700 kg |
| **Motorleistung** | 700 W |
| **Spannung** | 12V oder 24V |
| **Stromaufnahme (12V)** | 62 A (Last) |
| **Stromaufnahme (24V)** | 31 A (Last) |
| **Kettengrößen** | 6, 8, 10 mm DIN 766 / ISO |
| **Kettennuss** | Edelstahl oder Aluminium chrombeschichtet |
| **Seildurchmesser** | 12–16 mm |
| **Duty Cycle** | 4 min bei Volllast |
| **Gewicht (Motor)** | 13,5 kg |
| **Gewicht (Kopf)** | 5,8 kg |
| **Decksdurchführung** | Ø 130 mm |
| **Geeignet für Boote** | 10–14m |
| **Preis EUR** | 1.300–1.700 |
| **Varianten** | Dorado mit/ohne Spillkopf |

#### 3.2.3 Lofrans Falkon

Leistungsstarke Vertikalwinde für größere Yachten.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch |
| **Zugkraft** | 1.000 kg |
| **Motorleistung** | 1.000 W |
| **Spannung** | 12V oder 24V |
| **Stromaufnahme (12V)** | 88 A (Last) |
| **Stromaufnahme (24V)** | 44 A (Last) |
| **Kettengrößen** | 8, 10, 12 mm DIN 766 / ISO |
| **Kettennuss** | Edelstahl |
| **Seildurchmesser** | 14–18 mm |
| **Duty Cycle** | 4 min bei Volllast |
| **Gewicht (Motor)** | 18 kg |
| **Gewicht (Kopf)** | 7,5 kg |
| **Decksdurchführung** | Ø 150 mm |
| **Geeignet für Boote** | 13–17m |
| **Preis EUR** | 2.200–2.900 |

#### 3.2.4 Lofrans X1

Einstiegsmodell der X-Serie, kompakte Low-Profile-Vertikalwinde.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, Low-Profile, elektrisch |
| **Zugkraft** | 500 kg |
| **Motorleistung** | 500 W |
| **Spannung** | 12V |
| **Stromaufnahme** | 42 A (Last) |
| **Kettengrößen** | 6, 7, 8 mm |
| **Duty Cycle** | 3 min |
| **Gewicht** | 11 kg (komplett) |
| **Geeignet für Boote** | 7–9m |
| **Preis EUR** | 750–950 |

#### 3.2.5 Lofrans X2

Mittleres Modell der X-Serie.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, Low-Profile, elektrisch |
| **Zugkraft** | 700 kg |
| **Motorleistung** | 700 W |
| **Spannung** | 12V oder 24V |
| **Stromaufnahme (12V)** | 60 A (Last) |
| **Kettengrößen** | 6, 8, 10 mm |
| **Duty Cycle** | 4 min |
| **Gewicht** | 15 kg (komplett) |
| **Geeignet für Boote** | 9–13m |
| **Preis EUR** | 1.100–1.400 |

#### 3.2.6 Lofrans X3

Leistungsstarkes Modell der X-Serie.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, Low-Profile, elektrisch |
| **Zugkraft** | 1.000 kg |
| **Motorleistung** | 1.000 W |
| **Spannung** | 12V oder 24V |
| **Stromaufnahme (12V)** | 85 A (Last) |
| **Stromaufnahme (24V)** | 43 A (Last) |
| **Kettengrößen** | 8, 10, 12 mm |
| **Duty Cycle** | 4 min |
| **Gewicht** | 21 kg (komplett) |
| **Geeignet für Boote** | 13–17m |
| **Preis EUR** | 1.800–2.400 |

#### 3.2.7 Lofrans X4

Top-Modell der X-Serie für große Yachten.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, Low-Profile, elektrisch |
| **Zugkraft** | 1.500 kg |
| **Motorleistung** | 1.500 W |
| **Spannung** | 24V |
| **Stromaufnahme** | 65 A (Last) |
| **Kettengrößen** | 10, 12, 13 mm |
| **Duty Cycle** | 5 min |
| **Gewicht** | 32 kg (komplett) |
| **Geeignet für Boote** | 17–22m |
| **Preis EUR** | 3.500–4.500 |

#### 3.2.8 Lofrans Cayman

Horizontalwinde, beliebt bei Motorbooten und Nachrüstungen.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Horizontal, elektrisch |
| **Zugkraft** | 500–1.000 kg (je nach Modell) |
| **Motorleistung** | 500–1.000 W |
| **Spannung** | 12V oder 24V |
| **Stromaufnahme (12V, 500 kg)** | 44 A |
| **Stromaufnahme (12V, 1.000 kg)** | 85 A |
| **Kettengrößen** | 6, 8, 10 mm |
| **Seildurchmesser** | 12–16 mm |
| **Duty Cycle** | 3–4 min |
| **Gewicht** | 12–22 kg (je nach Modell) |
| **Geeignet für Boote** | 7–15m |
| **Preis EUR** | 750–1.800 |
| **Varianten** | Cayman 88, Cayman 1000 |

#### 3.2.9 Lofrans Kobra

Premium-Vertikalwinde für Superyacht-Segment.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch oder hydraulisch |
| **Zugkraft** | 1.500–3.000 kg |
| **Motorleistung** | 1.500–3.000 W (elektrisch) |
| **Spannung** | 24V (elektrisch) |
| **Kettengrößen** | 10, 12, 13, 14 mm |
| **Duty Cycle** | 6 min (elektrisch), unbegrenzt (hydraulisch) |
| **Gewicht** | 38–65 kg (je nach Modell) |
| **Geeignet für Boote** | 18–30m |
| **Preis EUR** | 4.500–12.000 |
| **Besonderheiten** | Edelstahlgehäuse, CAN-Bus-fähig |

### 3.3 Lewmar — Detaillierte Modellübersicht

Lewmar Ltd., gegründet 1946 in Hampshire, England. Weltweit bekannt
für Winschen, Luken und Ankerwinden.

#### 3.3.1 Lewmar V1

Kompakte Vertikalwinde für kleine Yachten.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch |
| **Zugkraft** | 400 kg |
| **Motorleistung** | 400 W |
| **Spannung** | 12V |
| **Stromaufnahme** | 35 A (Last) |
| **Kettengrößen** | 6, 7, 8 mm DIN 766 |
| **Seildurchmesser** | 10–12 mm |
| **Duty Cycle** | 3 min |
| **Gewicht** | 9 kg (komplett) |
| **Decksdurchführung** | Ø 100 mm |
| **Geeignet für Boote** | 6–9m |
| **Preis EUR** | 700–900 |

#### 3.3.2 Lewmar V2

Standard-Vertikalwinde für mittlere Segelyachten.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch |
| **Zugkraft** | 600 kg |
| **Motorleistung** | 600 W |
| **Spannung** | 12V oder 24V |
| **Stromaufnahme (12V)** | 52 A (Last) |
| **Stromaufnahme (24V)** | 26 A (Last) |
| **Kettengrößen** | 6, 8, 10 mm |
| **Seildurchmesser** | 12–14 mm |
| **Duty Cycle** | 4 min |
| **Gewicht** | 13 kg (komplett) |
| **Geeignet für Boote** | 9–12m |
| **Preis EUR** | 1.100–1.400 |

#### 3.3.3 Lewmar V3

Leistungsstarke Vertikalwinde für mittlere bis große Yachten.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch |
| **Zugkraft** | 1.000 kg |
| **Motorleistung** | 1.000 W |
| **Spannung** | 12V oder 24V |
| **Stromaufnahme (12V)** | 85 A (Last) |
| **Stromaufnahme (24V)** | 43 A (Last) |
| **Kettengrößen** | 8, 10, 12 mm |
| **Seildurchmesser** | 14–16 mm |
| **Duty Cycle** | 4 min |
| **Gewicht** | 20 kg (komplett) |
| **Geeignet für Boote** | 12–16m |
| **Preis EUR** | 1.800–2.400 |

#### 3.3.4 Lewmar V4

Premium-Vertikalwinde für große Yachten.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch |
| **Zugkraft** | 1.500 kg |
| **Motorleistung** | 1.500 W |
| **Spannung** | 24V |
| **Stromaufnahme** | 65 A (Last) |
| **Kettengrößen** | 10, 12, 13 mm |
| **Seildurchmesser** | 16–20 mm |
| **Duty Cycle** | 5 min |
| **Gewicht** | 30 kg (komplett) |
| **Geeignet für Boote** | 16–20m |
| **Preis EUR** | 3.200–4.200 |

#### 3.3.5 Lewmar V5

Top-Modell für Superyachten.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch oder hydraulisch |
| **Zugkraft** | 2.500 kg |
| **Motorleistung** | 2.500 W (elektrisch) |
| **Spannung** | 24V (elektrisch) |
| **Stromaufnahme** | 105 A (Last) |
| **Kettengrößen** | 12, 13, 14 mm |
| **Duty Cycle** | 5 min (elektrisch), unbegrenzt (hydraulisch) |
| **Gewicht** | 48 kg (komplett) |
| **Geeignet für Boote** | 20–28m |
| **Preis EUR** | 5.500–8.500 |

#### 3.3.6 Lewmar H-Series (H1, H2, H3, H4)

Horizontalwinden-Serie für Motorboote und Katamarane.

| Modell | Zugkraft | Motor | Spannung | Strom (12V) | Kette | Gewicht | Boote | Preis EUR |
|--------|---------|-------|----------|------------|-------|---------|-------|-----------|
| H1 | 350 kg | 350 W | 12V | 30 A | 6–8 mm | 8 kg | 5–8m | 600–800 |
| H2 | 600 kg | 600 W | 12V/24V | 52 A | 6–10 mm | 14 kg | 8–12m | 1.000–1.300 |
| H3 | 1.000 kg | 1.000 W | 12V/24V | 85 A | 8–12 mm | 20 kg | 12–16m | 1.700–2.200 |
| H4 | 1.500 kg | 1.500 W | 24V | 65 A | 10–14 mm | 28 kg | 16–22m | 2.800–3.800 |

#### 3.3.7 Lewmar Pro-Fish

Spezialmodell für Angelboote und Sportfischer.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Horizontal, elektrisch |
| **Zugkraft** | 700 kg |
| **Motorleistung** | 700 W |
| **Spannung** | 12V |
| **Stromaufnahme** | 60 A |
| **Kettengrößen** | 6, 8, 10 mm |
| **Seildurchmesser** | 12–16 mm |
| **Duty Cycle** | 4 min |
| **Gewicht** | 15 kg |
| **Geeignet für Boote** | 7–12m Fischerboote |
| **Preis EUR** | 1.200–1.500 |
| **Besonderheiten** | Korrosionsschutz verstärkt, Free-Fall-Funktion |

#### 3.3.8 Lewmar Pro-Sport

Sportliche Variante für schnelle Motorboote.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Horizontal oder Vertikal, elektrisch |
| **Zugkraft** | 550 kg |
| **Motorleistung** | 550 W |
| **Spannung** | 12V |
| **Stromaufnahme** | 48 A |
| **Kettengrößen** | 6, 8 mm |
| **Seildurchmesser** | 10–14 mm |
| **Duty Cycle** | 3 min |
| **Gewicht** | 11 kg |
| **Geeignet für Boote** | 7–11m Sportboote |
| **Preis EUR** | 900–1.200 |
| **Besonderheiten** | Kompaktes Design, schnelle Einhol-Geschwindigkeit |

### 3.4 Quick — Detaillierte Modellübersicht

Quick S.p.A., gegründet 1982 in Ravenna, Italien. Bekannt für
hochwertige Ankerwinden und Bugstrahlruder.

#### 3.4.1 Quick Aleph

Kompakte Vertikalwinde, Einstiegsmodell.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch |
| **Zugkraft** | 500 kg |
| **Motorleistung** | 500 W |
| **Spannung** | 12V oder 24V |
| **Stromaufnahme (12V)** | 43 A (Last) |
| **Stromaufnahme (24V)** | 22 A (Last) |
| **Kettengrößen** | 6, 7, 8 mm DIN 766 |
| **Seildurchmesser** | 10–14 mm |
| **Duty Cycle** | 3 min |
| **Gewicht (Motor)** | 8,5 kg |
| **Gewicht (Kopf)** | 3,8 kg |
| **Decksdurchführung** | Ø 105 mm |
| **Geeignet für Boote** | 7–10m |
| **Preis EUR** | 850–1.050 |

#### 3.4.2 Quick Genius

Mid-Range Vertikalwinde, sehr beliebt bei Segelyachten.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch |
| **Zugkraft** | 700 kg |
| **Motorleistung** | 700 W |
| **Spannung** | 12V oder 24V |
| **Stromaufnahme (12V)** | 60 A (Last) |
| **Stromaufnahme (24V)** | 30 A (Last) |
| **Kettengrößen** | 6, 8, 10 mm DIN 766 / ISO |
| **Seildurchmesser** | 12–16 mm |
| **Duty Cycle** | 4 min |
| **Gewicht (Motor)** | 12 kg |
| **Gewicht (Kopf)** | 5,5 kg |
| **Decksdurchführung** | Ø 125 mm |
| **Geeignet für Boote** | 10–14m |
| **Preis EUR** | 1.300–1.650 |
| **Besonderheiten** | Quick-CHC Kettenzähler integrierbar |

#### 3.4.3 Quick Hector

Leistungsstarke Vertikalwinde für größere Yachten.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch |
| **Zugkraft** | 1.200 kg |
| **Motorleistung** | 1.200 W |
| **Spannung** | 12V oder 24V |
| **Stromaufnahme (12V)** | 100 A (Last) |
| **Stromaufnahme (24V)** | 50 A (Last) |
| **Kettengrößen** | 8, 10, 12 mm |
| **Seildurchmesser** | 14–18 mm |
| **Duty Cycle** | 5 min |
| **Gewicht (Motor)** | 19 kg |
| **Gewicht (Kopf)** | 8,5 kg |
| **Decksdurchführung** | Ø 150 mm |
| **Geeignet für Boote** | 14–18m |
| **Preis EUR** | 2.500–3.200 |

#### 3.4.4 Quick Prince

Horizontalwinde für Motorboote.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Horizontal, elektrisch |
| **Zugkraft** | 500–1.000 kg (je nach Modell) |
| **Motorleistung** | 500–1.000 W |
| **Spannung** | 12V oder 24V |
| **Stromaufnahme (12V, 500 kg)** | 43 A |
| **Stromaufnahme (12V, 1.000 kg)** | 85 A |
| **Kettengrößen** | 6, 8, 10 mm |
| **Seildurchmesser** | 12–16 mm |
| **Duty Cycle** | 3–4 min |
| **Gewicht** | 11–20 kg |
| **Geeignet für Boote** | 7–14m |
| **Preis EUR** | 800–1.800 |
| **Varianten** | Prince DP1, DP2, DP3 |

#### 3.4.5 Quick Hero

Premium-Vertikalwinde für große Yachten und Superyachten.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch oder hydraulisch |
| **Zugkraft** | 1.500–3.000 kg |
| **Motorleistung** | 1.500–3.000 W (elektrisch) |
| **Spannung** | 24V (elektrisch) |
| **Stromaufnahme (24V, 1.500 kg)** | 65 A |
| **Kettengrößen** | 10, 12, 13, 14 mm |
| **Duty Cycle** | 6 min (elektrisch) |
| **Gewicht** | 35–60 kg |
| **Geeignet für Boote** | 18–28m |
| **Preis EUR** | 4.500–11.000 |
| **Besonderheiten** | Edelstahl-Gehäuse, Quick-CHC-Kettenzähler |

### 3.5 Maxwell — Detaillierte Modellübersicht

Maxwell Marine International, gegründet 1979 in Auckland, Neuseeland.
Spezialisiert auf Ankerwinden und Ankerausrüstung.

#### 3.5.1 Maxwell RC-Serie (RC6, RC8, RC10, RC12)

Kompakte Vertikalwinden-Serie, besonders beliebt in Ozeanien und den USA.

| Modell | Zugkraft | Motor | Spannung | Strom (12V) | Kette | Seil | Gewicht | Boote | Preis EUR |
|--------|---------|-------|----------|------------|-------|------|---------|-------|-----------|
| RC6 | 400 kg | 400 W | 12V | 35 A | 6–8 mm | 10–12 mm | 9 kg | 6–9m | 800–1.000 |
| RC8 | 600 kg | 600 W | 12V/24V | 52 A | 6–10 mm | 12–14 mm | 14 kg | 9–12m | 1.100–1.400 |
| RC10 | 1.000 kg | 1.000 W | 12V/24V | 85 A | 8–12 mm | 14–16 mm | 20 kg | 12–16m | 1.800–2.400 |
| RC12 | 1.500 kg | 1.500 W | 24V | 65 A | 10–14 mm | 16–18 mm | 28 kg | 16–20m | 2.800–3.600 |

#### 3.5.2 Maxwell VRC-Serie (VRC6, VRC8, VRC10, VRC12)

Premium-Vertikalwinden mit Edelstahlgehäuse.

| Modell | Zugkraft | Motor | Spannung | Kette | Gewicht | Boote | Preis EUR |
|--------|---------|-------|----------|-------|---------|-------|-----------|
| VRC6 | 500 kg | 500 W | 12V/24V | 6–8 mm | 11 kg | 7–10m | 1.100–1.400 |
| VRC8 | 800 kg | 800 W | 12V/24V | 8–10 mm | 16 kg | 10–14m | 1.500–1.900 |
| VRC10 | 1.200 kg | 1.200 W | 12V/24V | 10–12 mm | 24 kg | 14–18m | 2.400–3.200 |
| VRC12 | 1.800 kg | 1.800 W | 24V | 12–14 mm | 34 kg | 18–22m | 3.600–4.800 |

#### 3.5.3 Maxwell HRC-Serie

Horizontalwinden-Serie, robust und wartungsfreundlich.

| Modell | Zugkraft | Motor | Spannung | Strom (12V) | Kette | Gewicht | Boote | Preis EUR |
|--------|---------|-------|----------|------------|-------|---------|-------|-----------|
| HRC6 | 400 kg | 400 W | 12V | 35 A | 6–8 mm | 8 kg | 5–8m | 650–850 |
| HRC8 | 700 kg | 700 W | 12V/24V | 60 A | 8–10 mm | 14 kg | 8–12m | 1.000–1.300 |
| HRC10 | 1.000 kg | 1.000 W | 12V/24V | 85 A | 10–12 mm | 20 kg | 12–16m | 1.600–2.100 |
| HRC FF | 1.200 kg | 1.200 W | 12V/24V | 100 A | 10–12 mm | 24 kg | 14–18m | 2.200–2.800 |

#### 3.5.4 Maxwell Freedom

Premium-Vertikalwinde mit integriertem Free-Fall-System.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch, Free-Fall |
| **Zugkraft** | 700–1.500 kg (je nach Modell) |
| **Motorleistung** | 700–1.500 W |
| **Spannung** | 12V oder 24V |
| **Kettengrößen** | 8, 10, 12 mm |
| **Duty Cycle** | 4–5 min |
| **Gewicht** | 15–30 kg |
| **Geeignet für Boote** | 10–18m |
| **Preis EUR** | 1.500–3.500 |
| **Besonderheiten** | Kontrollierter Free-Fall, einstellbare Fallgeschwindigkeit |

### 3.6 Muir — Detaillierte Modellübersicht

Muir Engineering, gegründet 1984 in Queensland, Australien.
Premium-Hersteller, besonders im Superyacht-Segment stark.

#### 3.6.1 Muir VR-Serie (VR2500, VR3500, VR5000, VR8000)

Premium-Vertikalwinden für mittlere bis große Yachten.

| Modell | Zugkraft | Motor | Spannung | Kette | Gewicht | Boote | Preis EUR |
|--------|---------|-------|----------|-------|---------|-------|-----------|
| VR2500 | 1.100 kg | 1.100 W | 12V/24V | 8–10 mm | 22 kg | 12–16m | 2.200–2.800 |
| VR3500 | 1.600 kg | 1.600 W | 24V | 10–12 mm | 32 kg | 16–20m | 3.400–4.400 |
| VR5000 | 2.300 kg | 2.300 W | 24V | 12–14 mm | 48 kg | 20–26m | 5.500–7.500 |
| VR8000 | 3.600 kg | 3.000 W | 24V/Hydr. | 14–16 mm | 72 kg | 26–35m | 8.500–14.000 |

#### 3.6.2 Muir HR-Serie (HR2500, HR3500, HR5000)

Premium-Horizontalwinden.

| Modell | Zugkraft | Motor | Spannung | Kette | Gewicht | Boote | Preis EUR |
|--------|---------|-------|----------|-------|---------|-------|-----------|
| HR2500 | 1.100 kg | 1.100 W | 12V/24V | 8–10 mm | 20 kg | 12–16m | 2.000–2.600 |
| HR3500 | 1.600 kg | 1.600 W | 24V | 10–12 mm | 28 kg | 16–20m | 3.000–4.000 |
| HR5000 | 2.300 kg | 2.300 W | 24V | 12–14 mm | 42 kg | 20–26m | 5.000–7.000 |

### 3.7 Italwinch — Detaillierte Modellübersicht

Italwinch S.r.l., mit Sitz in Italien. Budget-freundlicher Hersteller
mit gutem Preis-Leistungs-Verhältnis.

#### 3.7.1 Italwinch Smart

Einstiegsmodell Vertikalwinde.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch |
| **Zugkraft** | 500 kg |
| **Motorleistung** | 500 W |
| **Spannung** | 12V |
| **Stromaufnahme** | 42 A |
| **Kettengrößen** | 6, 7, 8 mm DIN 766 |
| **Seildurchmesser** | 10–14 mm |
| **Duty Cycle** | 3 min |
| **Gewicht** | 10 kg (komplett) |
| **Geeignet für Boote** | 7–10m |
| **Preis EUR** | 550–700 |

#### 3.7.2 Italwinch Smart Plus

Erweiterte Version mit mehr Leistung.

| Spezifikation | Wert |
|--------------|------|
| **Typ** | Vertikal, elektrisch |
| **Zugkraft** | 700 kg |
| **Motorleistung** | 700 W |
| **Spannung** | 12V oder 24V |
| **Stromaufnahme (12V)** | 58 A |
| **Stromaufnahme (24V)** | 29 A |
| **Kettengrößen** | 6, 8, 10 mm DIN 766 |
| **Seildurchmesser** | 12–16 mm |
| **Duty Cycle** | 3 min |
| **Gewicht** | 14 kg (komplett) |
| **Geeignet für Boote** | 9–13m |
| **Preis EUR** | 750–950 |
| **Besonderheiten** | Gutes Preis-Leistungs-Verhältnis |

### 3.8 Preisvergleich nach Zugkraft-Klasse

#### 3.8.1 Klasse 500 kg (7–10m Boote)

| Hersteller | Modell | Typ | Preis EUR | Bewertung |
|-----------|--------|-----|-----------|-----------|
| Italwinch | Smart | V | 550–700 | Budget-Tipp |
| Lofrans | X1 | V | 750–950 | Gutes Preis-Leistung |
| Lofrans | Tigres | V | 850–1.100 | Bewährt |
| Quick | Aleph | V | 850–1.050 | Qualitativ hochwertig |
| Maxwell | RC6 | V | 800–1.000 | Robuste Verarbeitung |
| Lewmar | V1 | V | 700–900 | Solide Basis |

#### 3.8.2 Klasse 700 kg (10–14m Boote)

| Hersteller | Modell | Typ | Preis EUR | Bewertung |
|-----------|--------|-----|-----------|-----------|
| Italwinch | Smart Plus | V | 750–950 | Budget-Tipp |
| Lofrans | X2 | V | 1.100–1.400 | Empfehlung |
| Lofrans | Dorado | V | 1.300–1.700 | Klassiker |
| Quick | Genius | V | 1.300–1.650 | Sehr beliebt |
| Lewmar | V2 | V | 1.100–1.400 | Bewährt |
| Maxwell | RC8 | V | 1.100–1.400 | Robust |

#### 3.8.3 Klasse 1.000 kg (12–17m Boote)

| Hersteller | Modell | Typ | Preis EUR | Bewertung |
|-----------|--------|-----|-----------|-----------|
| Lofrans | X3 | V | 1.800–2.400 | Empfehlung |
| Lofrans | Falkon | V | 2.200–2.900 | Premium |
| Quick | Hector | V | 2.500–3.200 | Leistungsstark |
| Lewmar | V3 | V | 1.800–2.400 | Solide |
| Maxwell | RC10 | V | 1.800–2.400 | Bewährt |
| Muir | VR2500 | V | 2.200–2.800 | Premium |

#### 3.8.4 Klasse 1.500+ kg (17m+ Boote)

| Hersteller | Modell | Typ | Preis EUR | Bewertung |
|-----------|--------|-----|-----------|-----------|
| Lofrans | X4 | V | 3.500–4.500 | Empfehlung |
| Lofrans | Kobra | V | 4.500–12.000 | Superyacht |
| Quick | Hero | V | 4.500–11.000 | Premium |
| Lewmar | V4 | V | 3.200–4.200 | Bewährt |
| Lewmar | V5 | V | 5.500–8.500 | Top-Segment |
| Maxwell | RC12 | V | 2.800–3.600 | Gutes P/L |
| Muir | VR3500 | V | 3.400–4.400 | Premium |
| Muir | VR5000 | V | 5.500–7.500 | Superyacht |

---

## 4. Dimensionierung

### 4.1 Grundregel der Ankerwinden-Dimensionierung

Die wichtigste Dimensionierungsregel:

> **Die Zugkraft der Ankerwinde muss mindestens das 3-fache des
> Gewichts der auszubringenden Ankerkette + Anker betragen.**

Dies ist die sogenannte **3:1-Regel** und berücksichtigt:
- Strömungswiderstand der Kette im Wasser
- Saugwirkung des Ankers im Grund
- Dynamische Belastung durch Wellengang
- Reibung in der Klüse/Bugrolle
- Leistungsverlust bei niedrigem Ladezustand der Batterie

### 4.2 Berechnung des Kettengewichts

#### 4.2.1 Gewicht pro Meter nach Kettengröße (DIN 766)

| Kettengröße | Gewicht pro Meter | Typische Länge | Gesamtgewicht |
|------------|------------------|----------------|---------------|
| 6 mm | 0,78 kg/m | 30 m | 23,4 kg |
| 7 mm | 1,08 kg/m | 40 m | 43,2 kg |
| 8 mm | 1,38 kg/m | 50 m | 69,0 kg |
| 10 mm | 2,20 kg/m | 60 m | 132,0 kg |
| 12 mm | 3,10 kg/m | 70 m | 217,0 kg |
| 13 mm | 3,65 kg/m | 80 m | 292,0 kg |
| 14 mm | 4,25 kg/m | 80 m | 340,0 kg |
| 16 mm | 5,60 kg/m | 100 m | 560,0 kg |

#### 4.2.2 Typische Ankergewichte

| Ankertyp | 6–8m Boot | 9–12m Boot | 12–15m Boot | 15–20m Boot | 20–25m Boot |
|----------|----------|-----------|-----------|-----------|-----------|
| Delta/CQR | 6 kg | 10 kg | 16 kg | 25 kg | 40 kg |
| Bruce/Claw | 5 kg | 7,5 kg | 10 kg | 15 kg | 20 kg |
| Rocna/Mantus | 6 kg | 10 kg | 15 kg | 25 kg | 40 kg |
| Danforth/Fluke | 4 kg | 6 kg | 10 kg | 14 kg | 20 kg |
| Bügelanker | 6 kg | 10 kg | 15 kg | 25 kg | 40 kg |

#### 4.2.3 Beispielrechnung Dimensionierung

**Beispiel: 12m Segelyacht**

```
Ankerkette:       8 mm DIN 766, 50m Länge
Kettengewicht:    1,38 kg/m × 50m = 69 kg
Ankergewicht:     Delta 16 kg
────────────────────────────────────
Gesamtgewicht:    69 + 16 = 85 kg

Erforderliche Zugkraft (3:1-Regel):
  85 kg × 3 = 255 kg (Minimum)

Empfohlene Zugkraft (Sicherheitsfaktor 1,5):
  255 kg × 1,5 = 383 kg

→ Mindestens 400 kg Zugkraft empfohlen
→ Empfehlung: 500–700 kg Klasse
```

**Beispiel: 18m Motoryacht**

```
Ankerkette:       10 mm DIN 766, 80m Länge
Kettengewicht:    2,20 kg/m × 80m = 176 kg
Ankergewicht:     Rocna 25 kg
────────────────────────────────────
Gesamtgewicht:    176 + 25 = 201 kg

Erforderliche Zugkraft (3:1-Regel):
  201 kg × 3 = 603 kg (Minimum)

Empfohlene Zugkraft (Sicherheitsfaktor 1,5):
  603 kg × 1,5 = 905 kg

→ Mindestens 900 kg Zugkraft empfohlen
→ Empfehlung: 1.000–1.500 kg Klasse
```

### 4.3 Dimensionierungstabelle nach Bootsgröße

| Bootsgröße | Verdrängung | Kettengröße | Kettenlänge | Ankergewicht | Min. Zugkraft | Empf. Zugkraft |
|------------|------------|------------|------------|-------------|--------------|---------------|
| 5–7m | 1–3 t | 6 mm | 20–30 m | 4–6 kg | 150 kg | 300 kg |
| 7–9m | 3–5 t | 6–8 mm | 30–40 m | 6–10 kg | 200 kg | 400 kg |
| 9–12m | 5–12 t | 8 mm | 40–50 m | 10–16 kg | 300 kg | 600 kg |
| 12–15m | 10–25 t | 8–10 mm | 50–60 m | 14–20 kg | 450 kg | 800 kg |
| 15–18m | 20–40 t | 10 mm | 60–80 m | 20–30 kg | 700 kg | 1.200 kg |
| 18–22m | 35–80 t | 10–12 mm | 70–90 m | 25–40 kg | 1.000 kg | 1.800 kg |
| 22–26m | 60–150 t | 12–14 mm | 80–100 m | 40–60 kg | 1.500 kg | 2.500 kg |

### 4.4 Elektrische Dimensionierung

#### 4.4.1 Kabelquerschnitt-Berechnung

Der Kabelquerschnitt richtet sich nach Stromstärke und Kabellänge.
Maximaler zulässiger Spannungsabfall: 10% (1,2V bei 12V, 2,4V bei 24V).

**Formel:**
```
A = (2 × L × I × ρ) / ΔU

A = Querschnitt in mm²
L = Kabellänge (einfach, Motor → Batterie) in m
I = Strom in A
ρ = Spezifischer Widerstand Kupfer = 0,0175 Ω·mm²/m
ΔU = Zulässiger Spannungsabfall in V
```

#### 4.4.2 Kabelquerschnitt-Tabelle 12V (max. 10% Spannungsabfall)

| Strom (A) | 3m | 5m | 7m | 9m | 11m | 13m | 15m |
|-----------|-----|-----|-----|-----|------|------|------|
| 30 A | 6 mm² | 10 mm² | 10 mm² | 16 mm² | 16 mm² | 25 mm² | 25 mm² |
| 50 A | 10 mm² | 16 mm² | 16 mm² | 25 mm² | 25 mm² | 35 mm² | 35 mm² |
| 70 A | 16 mm² | 25 mm² | 25 mm² | 35 mm² | 35 mm² | 50 mm² | 50 mm² |
| 90 A | 16 mm² | 25 mm² | 35 mm² | 35 mm² | 50 mm² | 50 mm² | 70 mm² |
| 110 A | 25 mm² | 35 mm² | 35 mm² | 50 mm² | 50 mm² | 70 mm² | 70 mm² |
| 130 A | 25 mm² | 35 mm² | 50 mm² | 50 mm² | 70 mm² | 70 mm² | 95 mm² |

#### 4.4.3 Kabelquerschnitt-Tabelle 24V (max. 10% Spannungsabfall)

| Strom (A) | 3m | 5m | 7m | 9m | 11m | 13m | 15m |
|-----------|-----|-----|-----|-----|------|------|------|
| 20 A | 4 mm² | 6 mm² | 6 mm² | 10 mm² | 10 mm² | 10 mm² | 16 mm² |
| 30 A | 4 mm² | 6 mm² | 10 mm² | 10 mm² | 16 mm² | 16 mm² | 16 mm² |
| 40 A | 6 mm² | 10 mm² | 10 mm² | 16 mm² | 16 mm² | 25 mm² | 25 mm² |
| 60 A | 10 mm² | 16 mm² | 16 mm² | 25 mm² | 25 mm² | 25 mm² | 35 mm² |
| 80 A | 10 mm² | 16 mm² | 25 mm² | 25 mm² | 35 mm² | 35 mm² | 35 mm² |
| 100 A | 16 mm² | 25 mm² | 25 mm² | 35 mm² | 35 mm² | 50 mm² | 50 mm² |

#### 4.4.4 Sicherung / Leitungsschutzschalter

| Windengröße (Zugkraft) | 12V Sicherung | 24V Sicherung | Typ |
|------------------------|--------------|--------------|-----|
| 300–500 kg | 60–80 A | 30–40 A | ANL-Sicherung oder Automat |
| 500–800 kg | 80–100 A | 40–60 A | ANL-Sicherung oder Automat |
| 800–1.200 kg | 100–130 A | 60–80 A | ANL-Sicherung |
| 1.200–1.500 kg | 130–160 A | 80–100 A | ANL-Sicherung |
| 1.500–2.000 kg | 160–200 A | 100–120 A | ANL-Sicherung |

#### 4.4.5 Batterie-Kapazitätsberechnung

**Faustregel:**
Die Batterie muss mindestens das 3-fache der Ankerwindenstrom-Aufnahme
in Ah bereitstellen, um die Spannung unter Last stabil zu halten.

```
Batterie min (Ah) = Windenstrom (A) × 3

Beispiel: 80A Winde → min. 240 Ah Batterie (12V)
         Empfohlen: eigener Batteriekreis oder Starterbatterie
```

**Wichtig:** Ankerwinden sollten NICHT über die Servicebatteriebank
betrieben werden, sondern über die Starterbatterie oder einen separaten
Ankerwindenkreis. Die hohen Ströme belasten AGM/Gel-Batterien stark.

### 4.5 Hydraulische Dimensionierung

#### 4.5.1 Pumpen-Dimensionierung

| Zugkraft | Betriebsdruck | Volumenstrom | Pumpenleistung |
|---------|-------------|-------------|---------------|
| 500–1.000 kg | 100 bar | 5–8 l/min | 1,5–2,5 kW |
| 1.000–2.000 kg | 140 bar | 8–12 l/min | 2,5–4,0 kW |
| 2.000–3.500 kg | 180 bar | 12–18 l/min | 4,0–6,0 kW |
| 3.500–5.000 kg | 200 bar | 18–25 l/min | 6,0–8,0 kW |
| 5.000+ kg | 200+ bar | 25+ l/min | 8,0+ kW |

#### 4.5.2 Schlauch- und Leitungsdimensionierung

| Volumenstrom | Schlauchgröße (Druckleitung) | Schlauchgröße (Rücklauf) |
|-------------|---------------------------|------------------------|
| bis 8 l/min | DN 8 (3/8") | DN 10 (1/2") |
| 8–15 l/min | DN 10 (1/2") | DN 12 (3/4") |
| 15–25 l/min | DN 12 (3/4") | DN 16 (1") |
| 25+ l/min | DN 16 (1") | DN 20 (1 1/4") |

#### 4.5.3 Tankgröße

| Systemgröße | Tankvolumen (min.) | Empfohlen |
|------------|------------------|-----------|
| Klein | 5 Liter | 8 Liter |
| Mittel | 10 Liter | 15 Liter |
| Groß | 15 Liter | 25 Liter |
| Superyacht | 25+ Liter | 40+ Liter |

### 4.6 Gewichtsbudget und Trimm

#### 4.6.1 Gewichtseinfluss der Ankerwindenanlage

Das Gesamtgewicht der Ankerwindenanlage am Vorschiff beeinflusst
den Trimm der Yacht erheblich:

| Komponente | Typisches Gewicht (12m Yacht) |
|-----------|------------------------------|
| Ankerwinde (Motor + Kopf) | 15–20 kg |
| Ankerkette (50m × 8mm) | 69 kg |
| Anker (Delta 16 kg) | 16 kg |
| Bugrolle, Klüse | 3–5 kg |
| Kettenkasten (GFK) | 5–10 kg |
| Kabel, Schalter | 3–5 kg |
| **Gesamt** | **~115–125 kg** |

#### 4.6.2 Trimm-Einfluss

```
Trimmverschiebung = (Gewicht_Vorschiff × Abstand_zum_Schwerpunkt) / Verdrängung

Beispiel: 120 kg am Bug, 4m vor Schwerpunkt, 8.000 kg Verdrängung
         = (120 × 4) / 8.000 = 0,06m = 6cm Buglastigkeit
```

Bei Segelyachten ist moderate Buglastigkeit (2–5 cm) akzeptabel.
Bei Motoryachten sollte der Trimm neutral bis leicht hecklastig sein.

---

## 5. Installation

### 5.1 Deckverstärkung

#### 5.1.1 Lastberechnung

Die Ankerwindeninstallation muss folgende Lasten aufnehmen:

| Lastfall | Typische Last (12m Yacht) |
|---------|--------------------------|
| Statisch (Kette + Anker hängend) | ~1.000 N (100 kg) |
| Dynamisch (Einholen, Ankerbruch) | ~5.000 N (500 kg) |
| Spitzenlast (festsitzender Anker) | ~10.000 N (1.000 kg) |
| Seegang (dynamisch, periodisch) | ~3.000 N (300 kg) |

#### 5.1.2 Backing Plate (Gegenplatte)

Jede Ankerwindeninstallation erfordert eine Backing Plate unter Deck:

| Material | Dicke | Größe | Preis EUR |
|---------|-------|-------|-----------|
| Edelstahl 316L, 5mm | 5 mm | 200×200 mm (min.) | 40–80 |
| Edelstahl 316L, 8mm | 8 mm | 250×250 mm | 60–120 |
| Aluminium 5083, 10mm | 10 mm | 250×300 mm | 30–60 |
| GFK-Verstärkung | 5–8 mm Laminat | Großflächig | 50–100 (Material) |

**Anforderungen:**
- Backing Plate muss mindestens 50mm über die Windenbasis hinausragen
- Flächenpressung unter Bolzen: max. 15 N/mm² (GFK-Deck)
- Bolzen: Edelstahl A4-70, min. M8, vorzugsweise M10
- Dichtung: Sikaflex 291i oder 3M 5200 unter der Windenbase
- Unterlegscheiben: großflächig, min. 30mm Durchmesser

#### 5.1.3 Decksaufbau-Verstärkung

```
Schichtaufbau (von oben nach unten):

  ┌────────────────────────┐
  │     Ankerwinde         │  ← Befestigungsbolzen
  ├────────────────────────┤
  │  Dichtmasse (Sikaflex) │  ← 2–3 mm Schicht
  ├────────────────────────┤
  │     GFK-Deck           │  ← 8–15 mm (je nach Yacht)
  ├────────────────────────┤
  │  Kernmaterial (optional)│  ← Balsa/Schaum entfernt im Bereich
  ├────────────────────────┤
  │     GFK-Unterlaminat   │  ← 5–8 mm Verstärkung
  ├────────────────────────┤
  │     Backing Plate      │  ← Edelstahl/Aluminium
  ├────────────────────────┤
  │  Großflächige U-Scheiben│
  │  + Nylock-Muttern      │
  └────────────────────────┘
```

**WICHTIG:** Bei Sandwich-Decks (Balsa- oder Schaumkern) muss der
Kernbereich unter der Winde ENTFERNT und durch massives GFK-Laminat
oder Epoxid/Glasfaser-Füllung ersetzt werden. Andernfalls besteht
Gefahr von Kernfäule und Delaminierung unter Last.

#### 5.1.4 Befestigungspunkte

| Windentyp | Bolzenanzahl | Bolzengröße | Anzugsmoment |
|----------|-------------|------------|-------------|
| Kleine Vertikalwinde (bis 500 kg) | 4 | M8 | 15–20 Nm |
| Mittlere Vertikalwinde (500–1.000 kg) | 4–6 | M10 | 25–35 Nm |
| Große Vertikalwinde (1.000–2.000 kg) | 6 | M10–M12 | 35–50 Nm |
| Superyacht-Winde (2.000+ kg) | 6–8 | M12–M16 | 50–80 Nm |
| Horizontalwinde (alle Größen) | 4–6 | M8–M12 | 15–50 Nm |

### 5.2 Kettenrohr und Kettendurchführung

#### 5.2.1 Kettenrohr-Spezifikation

Das Kettenrohr führt die Kette von der Kettennuss in den Kettenkasten.

| Parameter | Empfehlung |
|-----------|-----------|
| Material | GFK-Rohr, Edelstahl, oder PVC (verstärkt) |
| Innendurchmesser | Min. 3× Kettengliedlänge |
| Wandstärke | Min. 3 mm (GFK), 2 mm (Edelstahl) |
| Neigung | Min. 30° zur Horizontalen, ideal 45–60° |
| Befestigung | Flansch oben, Flansch oder Muffe unten |
| Dichtung am Deck | Neopren-Dichtung oder Butylband |

#### 5.2.2 Empfohlene Kettenrohr-Durchmesser

| Kettengröße | Min. Rohrdurchmesser | Empfohlen |
|------------|---------------------|-----------|
| 6 mm | 35 mm | 40 mm |
| 8 mm | 45 mm | 50 mm |
| 10 mm | 55 mm | 60 mm |
| 12 mm | 65 mm | 75 mm |
| 14 mm | 75 mm | 85 mm |

### 5.3 Kettenkasten-Design

#### 5.3.1 Grundanforderungen

| Anforderung | Spezifikation |
|------------|--------------|
| Volumen | Min. 1,5× Volumen der gefüllten Kette |
| Drainage | Lenzöffnung am tiefsten Punkt, min. Ø 25 mm |
| Ventilation | Belüftungsöffnung oben, min. 20 cm² |
| Zugang | Inspektionsluke, min. 300×300 mm |
| Material | GFK, Edelstahl, oder verstärkter Kunststoff |
| Beschichtung | Epoxid-Beschichtung innen (Korrosionsschutz) |

#### 5.3.2 Volumenberechnung

```
Kettenvolumen (gestapelt) = Kettenlänge × π × (d_Glied/2)² × Füllfaktor

Füllfaktor gestapelte Kette: ~2,5 (Kette stapelt sich nicht dicht)

Beispiel: 50m × 8mm Kette
  Gliedlänge: ~29 mm, Gliedhöhe: ~24 mm
  Stapelvolumen: ca. 0,035 m³ = 35 Liter
  Kastenvolumen (min.): 35 × 1,5 = 52,5 Liter
  Empfohlen: 60–80 Liter
```

#### 5.3.3 Drainage

- Schwerkraftentwässerung zum tiefsten Punkt
- Lenzmündung NICHT direkt in die Bilge (Salzwasser!)
- Empfohlen: separate Kettenkastenlenzpumpe oder Entwässerung nach außenbords
- Rückschlagventil bei Ableitung nach außenbords
- Regelmäßige Kontrolle auf Verstopfung

#### 5.3.4 Ventilation

- Belüftung verhindert Fäulnis und Geruchsbildung
- Min. eine Lüftungsöffnung oben (mit Insektengitter)
- Ideal: Durchlüftung mit Ein- und Auslass
- Bei geschlossenem Kasten: Lüftungsrohr nach oben führen
- Dorade-Lüfter oder Pilzlüfter auf dem Vorschiffsdeck

### 5.4 Elektrische Installation

#### 5.4.1 Schaltplan Ankerwindenanlage (12V)

```
  ┌──────────┐
  │ Batterie │──┬── (+) ──→ ANL-Sicherung ──→ Hauptschalter ──→┐
  │   12V    │  │                                                │
  │          │  │                                          ┌─────┴─────┐
  └──────────┘  │                                          │  Solenoid  │
                │                                          │  (Auf/Ab)  │
                │                                          └─────┬─────┘
                │                                                │
                │                                          ┌─────┴─────┐
                │                                          │   Motor    │
                │                                          │ Ankerwinde │
                │                                          └─────┬─────┘
                │                                                │
                └── (−) ──← Massekabel ────────────────────←────┘

  Steuerkreis:
  ┌──────────┐
  │ Fußschalter│──→ Solenoid-Spule "Auf"
  │  (Auf)    │
  └──────────┘
  ┌──────────┐
  │ Fußschalter│──→ Solenoid-Spule "Ab"
  │  (Ab)     │
  └──────────┘
```

#### 5.4.2 Kabelinstallation — Checkliste

| Punkt | Anforderung |
|-------|------------|
| Kabeltyp | Mehrdrähtig, verzinnt (Marine-Grade) |
| Querschnitt | Gemäß Berechnungstabelle (Abschnitt 4.4) |
| Isolation | Min. 600V, öl-/UV-beständig |
| Kabelschuhe | Verzinnt, gecrimpt UND gelötet |
| Schrumpfschlauch | Über allen Kabelschuhen, doppelwandig mit Kleber |
| Kabeldurchführungen | Verschraubte Kabeldurchführungen (IP67) |
| Kabelkanal | Geschützt verlegen, nicht über scharfe Kanten |
| Befestigung | Alle 30 cm fixiert (Kabelbinder oder Klemmen) |
| Massekabel | Gleicher Querschnitt wie Plus-Kabel |
| Masseverbindung | Direkt an Batterie, NICHT über Masse-Sammelschiene |

#### 5.4.3 Solenoid-Relais

Das Solenoid-Relais schaltet die hohen Motorströme:

| Parameter | Anforderung |
|-----------|------------|
| Typ | Doppel-Solenoid (Auf/Ab in einem Gehäuse) |
| Schaltleistung | Min. 1,5× Nenn-Motorstrom |
| Schutzart | Min. IP55 (spritzwassergeschützt) |
| Montageort | Trocken, zugänglich, nahe am Motor |
| Steuerleitung | 1,5–2,5 mm², Sicherung 5–10 A |
| Erdung | Gehäuse an Bordmasse |

#### 5.4.4 Fußschalterinstallation

| Parameter | Anforderung |
|-----------|------------|
| Position | Neben der Ankerwinde, gut erreichbar |
| Abstand zur Klüse | Min. 300 mm (Sicherheitsabstand) |
| Schutzart | Min. IP67 (wasserdicht) |
| Betätigungskraft | 20–40 N (mit Schuh bedienbar) |
| Federmechanismus | Selbstrückstellend (Totmann-Funktion) |
| Markierung | Deutlich "AUF" / "AB" gekennzeichnet |
| Kabel | Min. 1,5 mm², wasserdicht verlegt |
| Entwässerung | Wasserablauf am tiefsten Punkt |

#### 5.4.5 Helmstation-Bedienung

| Parameter | Anforderung |
|-----------|------------|
| Schaltertyp | Wipptaster, selbstrückstellend |
| Schutzart | Min. IP55 |
| Kabel zum Solenoid | 1,5–2,5 mm² |
| Sicherung | 5–10 A |
| Parallelschaltung | Fußschalter und Helmschalter parallel |
| Verriegelung | Optional: Schlüsselschalter oder Sicherungsschalter |

### 5.5 Kettenzähler-Installation

#### 5.5.1 Sensor-Typen

| Sensortyp | Funktionsprinzip | Genauigkeit | Preis EUR |
|-----------|-----------------|-------------|-----------|
| Kettensensor (magnetisch) | Zählt Kettenglieder magnetisch | ±1 Glied | 80–150 |
| Wellensensor | Drehzahl der Kettennuss-Welle | ±0,5 m | 60–120 |
| Seilsensor (Raddrehgeber) | Reibrad auf der Kette | ±0,3 m | 100–180 |
| Ultraschall-Sensor | Abstand zur Kette im Kasten | ±5% | 150–250 |

#### 5.5.2 Installation Kettensensor (Lofrans-Typ)

1. Sensor am Kettenrohr befestigen (Schelle oder Schrauben)
2. Abstand Sensor zur Kette: 2–5 mm
3. Sensor muss jedes Kettenglied „sehen"
4. Kabel zum Display/Controller verlegen (geschirmt)
5. Magnete an definierten Positionen der Kette (falls nötig)
6. Kalibrierung: 10 Glieder auslegen und Zähler justieren

#### 5.5.3 Installation Kettensensor (Lewmar-Typ)

1. Sensor auf der Kettennuss-Welle montieren
2. Magnet-Ring auf die Welle setzen
3. Sensor-Abstand zum Magnetring: 1–3 mm
4. Kabel zum Anzeigegerät verlegen
5. Programmierung: Gliedergröße und Kettenlänge eingeben
6. Kalibrierung: Gesamte Kette einmal aus- und einholen

#### 5.5.4 Installation Kettensensor (Quick CHC-Typ)

1. Quick CHC-Sensor am Kettenkasten-Eingang montieren
2. Sensor erkennt einzelne Kettenglieder kapazitiv
3. Markierungen auf der Kette alle 5m oder 10m (farbig)
4. Kabel zum Quick CHC-Display verlegen
5. Programmierung über das Display-Menü
6. Auto-Kalibrierung beim ersten Auslegen

### 5.6 Bugrolle und Klüse

#### 5.6.1 Bugrolle-Dimensionierung

| Kettengröße | Rollen-Ø (min.) | Rollen-Breite | Rollen-Material |
|------------|----------------|--------------|----------------|
| 6 mm | 50 mm | 20 mm | Edelstahl 316 oder Nylon |
| 8 mm | 70 mm | 25 mm | Edelstahl 316 oder Nylon |
| 10 mm | 90 mm | 30 mm | Edelstahl 316 |
| 12 mm | 110 mm | 35 mm | Edelstahl 316 |
| 14 mm | 130 mm | 40 mm | Edelstahl 316 |

#### 5.6.2 Klüse-Anforderungen

- Material: Edelstahl 316L, poliert
- Innendurchmesser: min. 2,5× Kettendurchmesser
- Kantenabrundung: min. 5 mm Radius (keine scharfen Kanten)
- Befestigung: min. 4× M8 Bolzen mit Backing Plate
- Dichtung: Sikaflex 291i oder gleichwertig
- Deckel: optional, selbstschließend oder mit Halteriemen

---

## 6. Kettennuss-Kompatibilität

### 6.1 Grundprinzip der Kettennuss

Die Kettennuss (engl. gypsy, wildcat) ist das zentrale Formschlusselement
zwischen Ankerwinde und Ankerkette. Sie muss EXAKT zur verwendeten
Kettengröße und Kettenspezifikation passen.

**Kritisch:** Eine falsch dimensionierte oder falsch spezifizierte
Kettennuss führt zu:
- Durchrutschen der Kette unter Last
- Verklemmung der Kette in der Nuss
- Beschleunigter Verschleiß von Kette UND Nuss
- Sicherheitsrisiko (unkontrolliertes Ablaufen der Kette)

### 6.2 Kettenstandards

#### 6.2.1 DIN 766 (Kurzgliedrige Rundstahlkette)

Der in Europa am häufigsten verwendete Standard für Ankerketten auf Yachten.

| Nenndicke d | Teilung p | Innenbreite b1 | Außenbreite b2 | Gewicht/m |
|------------|----------|---------------|---------------|-----------|
| 6 mm | 18,5 mm | 7,5 mm | 21 mm | 0,78 kg |
| 7 mm | 22,0 mm | 9,0 mm | 25 mm | 1,08 kg |
| 8 mm | 24,0 mm | 10,0 mm | 28 mm | 1,38 kg |
| 10 mm | 28,0 mm | 12,0 mm | 34 mm | 2,20 kg |
| 12 mm | 36,0 mm | 14,5 mm | 41 mm | 3,10 kg |
| 13 mm | 39,0 mm | 15,5 mm | 44 mm | 3,65 kg |
| 14 mm | 42,0 mm | 17,0 mm | 48 mm | 4,25 kg |

#### 6.2.2 ISO 4565 (Internationale Yachtkette)

Internationaler Standard, teilweise andere Maße als DIN 766.

| Nenndicke d | Teilung p | Innenbreite b1 | Außenbreite b2 |
|------------|----------|---------------|---------------|
| 1/4" (6,35 mm) | 17,5 mm | 7,1 mm | 20,7 mm |
| 5/16" (7,94 mm) | 21,1 mm | 9,0 mm | 25,9 mm |
| 3/8" (9,53 mm) | 25,4 mm | 10,8 mm | 31,1 mm |
| 7/16" (11,11 mm) | 29,0 mm | 12,8 mm | 36,3 mm |
| 1/2" (12,70 mm) | 33,3 mm | 14,4 mm | 41,3 mm |

#### 6.2.3 DIN 764 (Mittelgliedrige Rundstahlkette)

Mittelgliedrige Kette wird SELTENER auf Yachten verwendet, ist aber
für bestimmte Ankersysteme vorgesehen.

| Nenndicke d | Teilung p | Innenbreite b1 |
|------------|----------|---------------|
| 6 mm | 24,0 mm | 7,5 mm |
| 8 mm | 32,0 mm | 10,0 mm |
| 10 mm | 40,0 mm | 12,0 mm |
| 12 mm | 48,0 mm | 14,5 mm |

**ACHTUNG:** DIN 764 Ketten passen NICHT auf DIN 766 Kettennüsse und
umgekehrt! Die unterschiedliche Teilung führt zu Inkompatibilität.

### 6.3 Kalibrierte vs. nicht-kalibrierte Kette

| Eigenschaft | Kalibrierte Kette | Nicht-kalibrierte Kette |
|------------|-------------------|------------------------|
| Maßtoleranz | ±0,5 mm | ±2,0 mm |
| Kettennuss-tauglich | JA | NEIN |
| Anwendung | Ankerwinden | Festmacher, Sicherungsketten |
| Preis (8 mm/m) | 4,50–7,00 EUR | 2,00–3,50 EUR |
| Markierung | Prägung "KAL" oder Farbkennzeichnung | Keine |
| Prüfzertifikat | Verfügbar | Selten |

**KRITISCH:** Nur kalibrierte Kette darf auf einer Ankerwinde mit
Kettennuss verwendet werden. Nicht-kalibrierte Kette hat zu große
Toleranzen und springt aus der Nuss oder verklemmt.

### 6.4 Häufige Inkompatibilitäten

#### 6.4.1 Problem: DIN 766 Kette auf ISO-Nuss

- Teilungsunterschied: DIN 766 8mm hat 24mm Teilung, ISO 3/8" hat 25,4mm
- Folge: Kette „wandert" auf der Nuss, springt nach wenigen Metern
- Lösung: Passende Kettennuss bestellen oder Kette tauschen

#### 6.4.2 Problem: Verschlissene Kette auf neuer Nuss

- Verschlissene Kette hat vergrößerte Glieder
- Neue Nuss passt nicht mehr zur alten Kette
- Faustregel: Bei Verschleiß >5% der Glieddicke: Kette ersetzen
- Maximal zulässiger Verschleiß: 10% der Nenndicke

#### 6.4.3 Problem: Falsche Kettenqualität

| Kettenqualität | Bruchlast (8 mm) | Ankerwinden-tauglich |
|---------------|-----------------|---------------------|
| Güte 30 (mild steel) | ~2.000 kg | Nein (zu weich) |
| Güte 40 (proof coil) | ~3.200 kg | Bedingt |
| Güte 50 (BBB) | ~3.800 kg | Ja, mit Einschränkungen |
| Güte 70 (high test) | ~5.600 kg | Ja |
| Güte 80 (alloy) | ~6.400 kg | Bedingt (zu hart für einige Nüsse) |
| Güte 100 (stainless) | ~5.000 kg | Ja (Edelstahl-Nuss erforderlich) |

> ⚠️ **ZU PRÜFEN (Audit):** Bruchlast 8 mm hier Güte 40 ~3.200 kg / Güte 70 ~5.600 kg —
> in Tabelle 16.2 stehen für dieselbe Kette Güte 40 = 2.800 kg / Güte 70 = 5.000 kg (Widerspruch).
> Herstellerangaben (Lofrans / Jimmy Green Marine, ISO 4565 / DIN 766) nennen für 8 mm G40 ≈ 4.300 kg
> und für 8 mm G70 ≈ 7.000 kg; beide Tabellen liegen darunter. Bruchlast-Werte unverifiziert —
> **Confidence: estimated — unverifiziert.** Vor sicherheitsrelevanter Nutzung Herstellerdatenblatt heranziehen.

#### 6.4.4 Problem: Edelstahlkette auf Aluminium-Nuss

- Edelstahlkette ist härter als Aluminium-Nuss
- Beschleunigter Verschleiß der Nuss
- Lösung: Edelstahl-Kettennuss verwenden
- Alternativ: Kette regelmäßig prüfen und Nuss bei Verschleiß tauschen

### 6.5 Kettennuss-Austausch

#### 6.5.1 Wann ist ein Austausch nötig?

| Indikator | Beschreibung |
|----------|-------------|
| Kettenspiel | >2 mm Spiel in der Nuss (sichtbar) |
| Oberflächenverschleiß | Zahnprofil abgeflacht |
| Kette springt | Kette läuft bei leichter Belastung aus der Nuss |
| Geräusche | Klappergeräusche beim Einholen |
| Sichtbarer Materialabtrag | Metallspäne am Kettenrohr |

#### 6.5.2 Austausch-Anleitung (Vertikalwinde)

1. Winde stromlos schalten (Hauptschalter AUS)
2. Kette vollständig einholen oder sichern
3. Sicherungsring/-mutter oben am Kopf entfernen
4. Spillkopf (falls vorhanden) abnehmen
5. Kettennuss nach oben abziehen (Passfeder beachten)
6. Neue Nuss aufsetzen (auf Passfeder-Ausrichtung achten)
7. Spillkopf aufsetzen
8. Sicherungsmutter festziehen (Drehmoment lt. Hersteller)
9. Funktionstest mit wenigen Metern Kette
10. Lauf und Sitz der Kette prüfen

#### 6.5.3 Ersatz-Kettennuss Preise

| Hersteller | Kettengröße | Preis EUR |
|-----------|------------|-----------|
| Lofrans (Aluminium) | 6–8 mm | 80–120 |
| Lofrans (Edelstahl) | 6–8 mm | 150–220 |
| Lofrans (Aluminium) | 10–12 mm | 120–180 |
| Lofrans (Edelstahl) | 10–12 mm | 200–320 |
| Lewmar (Standard) | 6–8 mm | 90–130 |
| Lewmar (Standard) | 10–12 mm | 130–200 |
| Quick (Standard) | 6–8 mm | 85–125 |
| Quick (Standard) | 10–12 mm | 140–210 |
| Maxwell (Standard) | 6–8 mm | 80–120 |
| Maxwell (Standard) | 10–12 mm | 130–200 |

### 6.6 Kettennuss-Material-Vergleich

| Material | Vorteile | Nachteile | Einsatz |
|---------|---------|----------|---------|
| Aluminium (chrombeschichtet) | Leicht, günstig | Verschleißt schneller | Standard, galv. Kette |
| Edelstahl 316 | Langlebig, korrosionsfest | Schwerer, teurer | Edelstahlkette, Salz |
| Bronze | Korrosionsfest, selbstschmierend | Teuer, schwer | Traditionelle Yachten |
| Nylon/Kunststoff | Sehr leicht, leise | Nur für leichte Lasten | Kleine Boote |

---

## 7. Fernbedienung und Kettenzähler

### 7.1 Kabelgebundene Fernbedienungen

#### 7.1.1 Standard-Fußschalter

Der klassische Fußschalter ist die einfachste und zuverlässigste
Bedienungsform für Ankerwinden.

| Spezifikation | Standard | Premium |
|--------------|---------|---------|
| Gehäuse | Kunststoff (ABS) | Edelstahl/Chromkunststoff |
| Schutzart | IP66 | IP67–IP68 |
| Tasten | 2 (Auf/Ab) | 2 (Auf/Ab) + Deckel |
| Kabel | 2m fest | 3–5m, austauschbar |
| Befestigung | 2× Schrauben | 3–4× Schrauben |
| Preis EUR | 40–80 | 80–180 |

#### 7.1.2 Helmstation-Bedieneinheit

| Hersteller | Modell | Funktionen | Schutzart | Preis EUR |
|-----------|--------|-----------|-----------|-----------|
| Lofrans | Control Panel | Auf/Ab, Zähler-Anzeige | IP55 | 120–200 |
| Lewmar | AA710 | Auf/Ab | IP55 | 80–130 |
| Quick | Quick Command | Auf/Ab, Kettenzähler | IP55 | 150–250 |
| Maxwell | Panel Control | Auf/Ab, Beleuchtung | IP55 | 100–170 |

#### 7.1.3 Kombi-Bedienfeld mit Kettenzähler

Integrierte Bedienfelder mit Auf/Ab-Steuerung und Kettenzähler-Anzeige:

| Hersteller | Modell | Display | Funktionen | Preis EUR |
|-----------|--------|---------|-----------|-----------|
| Lofrans | Iris | LCD 2" | Auf/Ab, Tiefe (m), Kette (m), Alarm | 250–380 |
| Quick | CHC1203 | LCD 3" | Auf/Ab, Tiefe (m/ft), Kette (m/ft), Auto-Stop | 320–450 |
| Lewmar | Chain Counter | LCD 2" | Kette (m/ft), Reset, Alarm | 180–280 |
| Maxwell | AA560 | LCD 2" | Auf/Ab, Kette (m), Auto-Anker | 200–320 |

### 7.2 Kabellose Fernbedienungen

#### 7.2.1 Funk-Fernbedienung

| Hersteller | Modell | Reichweite | Frequenz | Kanäle | Preis EUR |
|-----------|--------|-----------|---------|--------|-----------|
| Quick | Remote Control | 30 m | 868 MHz | 2 (Auf/Ab) | 280–380 |
| Lewmar | Wireless Remote | 25 m | 868 MHz | 2 (Auf/Ab) | 250–350 |
| Lofrans | Wireless Kit | 35 m | 868 MHz | 2 + Freefall | 320–450 |
| Maxwell | Wireless | 30 m | 868 MHz | 2 (Auf/Ab) | 260–360 |
| MZ Electronic | RC03 | 50 m | 433 MHz | 2–4 | 200–300 |

#### 7.2.2 Sicherheitsaspekte kabelloser Bedienung

**WICHTIG:** Kabellose Fernbedienungen für Ankerwinden unterliegen
besonderen Sicherheitsanforderungen:

- **Totmann-Funktion**: Taste muss gehalten werden, Loslassen = Stopp
- **Reichweitenbegrenzung**: Automatischer Stopp bei Signalverlust
- **Pairing-Sicherheit**: Verschlüsselte Funkverbindung
- **Batterie-Überwachung**: Warnung bei niedrigem Ladestand
- **Parallelbetrieb**: Funk UND Fußschalter gleichzeitig möglich
- **Vorrang**: Fußschalter hat immer Vorrang vor Funk

### 7.3 Kettenzähler-Systeme

#### 7.3.1 Quick CHC (Chain Counter)

Eines der verbreitetsten Kettenzähler-Systeme im Yachtbereich.

| Spezifikation | Wert |
|--------------|------|
| **Sensor** | Magnetischer Kettensensor |
| **Display** | LCD, beleuchtet, 3" |
| **Genauigkeit** | ±1 Glied (typ. ±0,1 m bei 8 mm Kette) |
| **Funktionen** | Kettenauslauf (m/ft), Auto-Stop, Alarm, Reset |
| **Auto-Stop** | Einstellbar: max. Auslauf, min. Restlänge |
| **Spannung** | 12V oder 24V |
| **Stromaufnahme** | 0,2 A (Display + Sensor) |
| **Schutzart** | IP55 (Display), IP67 (Sensor) |
| **Kabel** | Sensor→Display: bis 15 m, geschirmt |
| **Preis EUR** | 350–500 (komplett) |

#### 7.3.2 Lofrans Iris Kettenzähler

| Spezifikation | Wert |
|--------------|------|
| **Sensor** | Wellensensor (Hall-Effekt) |
| **Display** | LCD, beleuchtet, 2" |
| **Genauigkeit** | ±0,5 m |
| **Funktionen** | Kettenauslauf, Auto-Stop, Wassertiefe (ext. Sensor) |
| **Auto-Stop** | 2 einstellbare Stopppunkte |
| **Spannung** | 12V oder 24V |
| **Schutzart** | IP55 |
| **Preis EUR** | 280–420 |

#### 7.3.3 Lewmar Chain Counter

| Spezifikation | Wert |
|--------------|------|
| **Sensor** | Kettensensor (induktiv) |
| **Display** | LCD, beleuchtet, 2" |
| **Genauigkeit** | ±1 m |
| **Funktionen** | Kettenauslauf (m/ft), Reset, akustischer Alarm |
| **Spannung** | 12V oder 24V |
| **Schutzart** | IP55 |
| **Preis EUR** | 200–320 |

### 7.4 Auto-Anker-Systeme

#### 7.4.1 Funktionsprinzip

Auto-Anker-Systeme kombinieren Kettenzähler mit GPS-Überwachung:

1. Nutzer gibt gewünschte Kettenlänge ein (oder System berechnet anhand Wassertiefe)
2. System lässt automatisch die berechnete Kettenmenge auslaufen
3. GPS überwacht Ankerposition (Ankerkreis-Monitoring)
4. Bei Ankerdrift: akustischer und/oder optischer Alarm
5. Optional: automatisches Nachlegen bei leichter Drift

#### 7.4.2 Verfügbare Auto-Anker-Systeme

| Hersteller | System | Funktionen | GPS | App | Preis EUR |
|-----------|--------|-----------|-----|-----|-----------|
| Quick | Quick Chain | Auto-Auslauf, Auto-Stop | Ja | Ja (iOS/Android) | 800–1.200 |
| Lewmar | AA Controller | Auto-Auslauf, Alarm | Optional | Nein | 500–750 |
| Maxwell | Auto Anchor | Auto-Auslauf, GPS-Alarm | Ja | Ja (iOS) | 700–1.000 |
| Yacht Devices | YDAB-01 | NMEA2000-Integration | Via Plotter | Via Plotter | 350–500 |

### 7.5 Smartphone-App-Steuerung

#### 7.5.1 Quick App

- **Verbindung**: Bluetooth 5.0, Reichweite ~15m
- **Funktionen**: Auf/Ab, Kettenzähler, Auto-Anker, GPS-Alarm
- **Kompatibilität**: iOS 14+, Android 10+
- **Voraussetzung**: Quick Bluetooth-Modul am Solenoid
- **Preis Bluetooth-Modul**: 200–300 EUR

#### 7.5.2 Sicherheitshinweis App-Steuerung

App-Steuerung sollte IMMER als Ergänzung, NIE als alleinige
Bedienung verwendet werden. Der Fußschalter bleibt die primäre
und sicherste Bedienungsmethode.

Gründe:
- Smartphone kann nass/beschädigt werden
- Bluetooth-Verbindung kann abbrechen
- Touch-Bedienung mit nassen Händen unzuverlässig
- Akku kann leer sein
- Bildschirm bei Sonnenlicht schlecht ablesbar

### 7.6 NMEA 2000 / CAN-Bus Integration

Moderne Ankerwinden können in das Boot-Netzwerk integriert werden:

| Protokoll | Hersteller-Unterstützung | Funktionen |
|-----------|------------------------|-----------|
| NMEA 2000 | Quick, Lewmar (ab 2022) | Kettenzähler auf MFD anzeigen |
| CAN-Bus | Lofrans (Premium), Quick | Volles Monitoring am Plotter |
| Seatalk NG | Lewmar (via Gateway) | Anzeige auf Raymarine-Displays |
| SignalK | Via NMEA-2000-Gateway | Open-Source-Integration |

---

## 8. Fehlerbild-Atlas

### 8.1 Fehlerbild F01: Motor-Überhitzung

#### 8.1.1 Symptome
- Motor stoppt nach 2–3 Minuten Betrieb
- Gehäuse sehr heiß (>80°C)
- Brandgeruch (Isolationslack)
- Thermoschutz löst aus (falls vorhanden)
- Nach Abkühlung (~10 min) funktioniert Motor wieder

#### 8.1.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Duty Cycle überschritten | Hoch | Betriebsdauer prüfen |
| Kette/Anker festsitzen | Hoch | Last prüfen, Boot über Anker fahren |
| Unterdimensionierte Winde | Mittel | Kette/Anker-Gewicht vs. Windengröße |
| Verschlissene Kohlebürsten | Mittel | Bürstenstand prüfen (<5mm = tauschen) |
| Niedrige Batteriespannung | Mittel | Spannung unter Last messen (<10,5V = Problem) |
| Korrodierte Kabelverbindungen | Mittel | Spannungsabfall an Klemmen messen |
| Getriebe schwergängig | Niedrig | Getriebeöl prüfen, manuell drehen |
| Motorlager defekt | Niedrig | Laufgeräusch, Spiel am Anker prüfen |

#### 8.1.3 Sofortmaßnahmen
1. Motor sofort stoppen
2. Min. 15 Minuten abkühlen lassen
3. Batteriespannung prüfen (>12,2V in Ruhe)
4. Kabelverbindungen auf Wärme/Verfärbung prüfen
5. Last reduzieren (Kette entlasten, Boot über Anker fahren)

#### 8.1.4 Langzeitlösung
- Winde ggf. eine Klasse größer dimensionieren
- Batteriekapazität erhöhen
- Kabelquerschnitte überprüfen und ggf. vergrößern
- Kohlebürsten wechseln (alle 500–1.000 Betriebsstunden)

### 8.2 Fehlerbild F02: Leitungsschutzschalter löst aus

#### 8.2.1 Symptome
- Winde stoppt plötzlich
- Sicherung/Automat ist ausgelöst
- Evtl. Schmorgeruch an der Sicherung
- Solenoid klickt nicht mehr

#### 8.2.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Sicherung unterdimensioniert | Hoch | Sicherungswert vs. Motorstrom prüfen |
| Kette/Anker blockiert | Hoch | Last prüfen |
| Kurzschluss im Motor | Mittel | Motorwicklung messen (Ohm) |
| Kurzschluss im Kabel | Mittel | Isolationswiderstand messen |
| Korrodierter Kontakt → Übergangswiderstand | Mittel | Klemmen prüfen |
| Solenoid-Kontakte verschweißt | Niedrig | Solenoid prüfen |

#### 8.2.3 Sofortmaßnahmen
1. Sicherung/Automat NICHT sofort wieder einschalten
2. Ursache klären
3. Kabelverbindungen sichtprüfen
4. Erst nach Klärung: Sicherung erneuern / Automat einschalten
5. Testlauf unter geringer Last

#### 8.2.4 Prüfschema

```
Sicherung löst aus
├── Sofort beim Einschalten?
│   ├── JA → Kurzschluss im Motor oder Kabel
│   │        → Kabel isoliert prüfen, Motor Widerstand messen
│   └── NEIN → Unter Last?
│             ├── JA → Mechanische Blockade oder Überlast
│             │        → Kette prüfen, Boot über Anker fahren
│             └── NEIN → Nach Zeit (~2 min)?
│                        → Thermischer Überstrom, Sicherung unterdimensioniert
│                        → Sicherungswert erhöhen (Herstellerangabe!)
```

### 8.3 Fehlerbild F03: Kette rutscht auf Kettennuss

#### 8.3.1 Symptome
- Kette rutscht unter Last durch die Nuss
- Ruckartige Bewegung beim Einholen
- Kette springt aus den Zähnen
- Erhöhter Verschleiß sichtbar
- Metallspäne am Kettenrohr

#### 8.3.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Falsche Kettennuss für Kettentyp | Hoch | Kettengröße und -standard prüfen |
| Kette verschlissen | Hoch | Glieddicke messen (<90% = tauschen) |
| Kettennuss verschlissen | Mittel | Zahnprofil visuell prüfen |
| Nicht-kalibrierte Kette | Mittel | Kettenmarkierung prüfen (KAL?) |
| Kette verdreht/verknotet | Niedrig | Kettenverlauf prüfen |
| DIN 766 auf ISO-Nuss (oder umgekehrt) | Mittel | Spezifikation beider Teile prüfen |

#### 8.3.3 Sofortmaßnahmen
1. Kette manuell sichern (Kettenstopper/Klemme)
2. Nie unter einer rutschenden Kette stehen
3. Handkurbel verwenden (falls vorhanden)
4. Ketten- und Nussspezifikation vergleichen

### 8.4 Fehlerbild F04: Langsamer Betrieb

#### 8.4.1 Symptome
- Einholgeschwindigkeit deutlich reduziert
- Motor dreht hörbar langsamer
- Kette wird nur stockend eingeholt
- Motor-Geräusch tiefer als normal

#### 8.4.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Niedrige Batteriespannung | Sehr hoch | Spannung unter Last messen |
| Korrodierte Kabelverbindungen | Hoch | Spannungsabfall an jeder Verbindung |
| Zu dünner Kabelquerschnitt | Mittel | Querschnitt vs. Strom/Länge prüfen |
| Verschlissene Kohlebürsten | Mittel | Bürstenlänge prüfen |
| Getriebeschaden | Niedrig | Geräusche, manuelles Drehen prüfen |
| Motor-Wicklungsschaden | Niedrig | Motorstrom im Leerlauf messen |

#### 8.4.3 Diagnose-Reihenfolge

```
Langsamer Betrieb
├── 1. Batteriespannung unter Last messen
│   ├── <10,5V (12V System) → Batterie laden/tauschen
│   └── >11,5V → Weiter
├── 2. Spannungsabfall an Klemmen messen
│   ├── >0,5V an einer Klemme → Klemme reinigen/erneuern
│   └── <0,5V → Weiter
├── 3. Gesamtspannungsabfall Batterie → Motor
│   ├── >1,5V (12V) → Kabelquerschnitt zu dünn
│   └── <1,5V → Weiter
├── 4. Kohlebürsten prüfen
│   ├── <5mm → Bürsten tauschen
│   └── >5mm → Weiter
└── 5. Getriebe/Motor-Werkstatt
```

### 8.5 Fehlerbild F05: Solenoid klickt, Motor dreht nicht

#### 8.5.1 Symptome
- Hörbar Klick-Geräusch beim Drücken des Schalters
- Motor dreht nicht oder dreht nur kurz an und stoppt
- Solenoid wird warm

#### 8.5.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Batterie zu schwach | Hoch | Spannung messen (>12V Leerlauf) |
| Solenoid-Kontakte verbrannt | Hoch | Solenoid öffnen, Kontakte prüfen |
| Kabelverbindung lose | Mittel | Klemmen prüfen, nachziehen |
| Motor blockiert | Mittel | Versuch manuell zu drehen |
| Motor-Wicklung defekt | Niedrig | Widerstand messen |
| Sicherung angeschmolzen | Niedrig | Sicherung visuell prüfen |

#### 8.5.3 Sofortmaßnahme
1. Hauptmotor starten (Batterie laden, Lichtmaschine)
2. Spannung an Solenoid-Ausgang messen
3. Wenn Spannung ok aber Motor tot: Motor direkt anschließen (Test)
4. Solenoid-Kontakte mit Schmirgelpapier (600er) reinigen

### 8.6 Fehlerbild F06: Wassereinbruch im Motor

#### 8.6.1 Symptome
- Motor dreht nicht oder dreht schwer
- Rostspuren am Motor/Getriebe
- Grünliche Korrosion (Kupfer/Bronze)
- Wasser im Motorgehäuse (beim Öffnen)
- Isolationswiderstand niedrig

#### 8.6.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Decksdurchführung undicht | Hoch | Dichtung visuell prüfen |
| Kettenrohr-Wasser läuft zum Motor | Hoch | Wasserablauf im Kettenkasten prüfen |
| Kondensation | Mittel | Belüftung des Motorraums prüfen |
| Spritzwasser (Horizontalwinde) | Mittel | Abdeckung/Haube prüfen |
| Wellendichtring defekt | Niedrig | Dichtring visuell prüfen |

#### 8.6.3 Reparatur
1. Motor komplett trocknen (24–48h, ggf. Warmluft)
2. Isolationswiderstand messen (>1 MΩ)
3. Kohlebürsten und Kommutator prüfen
4. Lager auf Rost/Korrosion prüfen
5. Dichtung erneuern (Decksdurchführung)
6. Drainagewege freimachen
7. Belüftung verbessern

### 8.7 Fehlerbild F07: Kupplungs-/Clutch-Slip

#### 8.7.1 Symptome
- Motor dreht, Kettennuss dreht nicht (oder nur teilweise)
- Kette bewegt sich nicht oder ruckartig
- Schleifgeräusche im Bereich Getriebe/Kupplung
- Brandgeruch (bei Reibkupplung)

#### 8.7.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Kupplungsscheiben verschlissen | Hoch | Kupplung einstellen/prüfen |
| Kupplung falsch eingestellt | Mittel | Einstellmutter prüfen |
| Öl auf Kupplungsflächen | Niedrig | Getriebeöl-Leck? |
| Federbruch in Kupplung | Niedrig | Kupplung demontieren |

#### 8.7.3 Reparatur
1. Kupplungs-Einstellmutter nachstellen (Herstelleranleitung)
2. Bei Verschleiß: Kupplungsscheiben/Reibbelag tauschen
3. Kupplung reinigen (entfetten)
4. Nach Einstellung: Funktionstest unter Last

### 8.8 Fehlerbild F08: Seil-Verklemmung

#### 8.8.1 Symptome
- Ankerleine klemmt im Spillkopf
- Seil wickelt sich um die Welle
- Motor blockiert, Sicherung löst aus
- Seil kann nicht vor- oder zurückbewegt werden

#### 8.8.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Falscher Seildurchmesser | Hoch | Seil vs. Spillkopf-Spezifikation |
| Seil zu weich/elastisch | Mittel | Seiltyp prüfen (3-schlag vs. geflochten) |
| Zu viele Törns auf Spillkopf | Mittel | Max. 3 Törns bei den meisten Modellen |
| Beschädigtes Seil (Spliss) | Mittel | Seil auf Beschädigungen prüfen |
| Spillkopf verschlissen/rau | Niedrig | Oberfläche prüfen |

#### 8.8.3 Sofortmaßnahme
1. Motor sofort stoppen
2. NICHT versuchen, Seil mit Motor freizuziehen
3. Seil manuell rückwärts abwickeln
4. Ggf. Seil abschneiden, wenn nicht anders lösbar
5. Spillkopf auf Beschädigung prüfen

### 8.9 Fehlerbild F09: Kettenzähler-Drift

#### 8.9.1 Symptome
- Kettenzähler zeigt falsche Länge an
- Abweichung nimmt mit der Anzahl der Zyklen zu
- Anzeige springt oder zählt doppelt
- Alarm bei falscher Kettenlänge

#### 8.9.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Sensor-Abstand zu groß | Hoch | Abstand Sensor → Kette messen |
| Verschmutzter Sensor | Hoch | Sensor reinigen |
| Magnet verschoben | Mittel | Magnetposition prüfen |
| Kette-Geschwindigkeit zu hoch | Mittel | Einholgeschwindigkeit reduzieren |
| Falsche Kalibrierung | Mittel | Neu kalibrieren |
| Sensor-Kabel beschädigt | Niedrig | Kabel und Stecker prüfen |

#### 8.9.3 Rekalibrierung
1. Kette komplett einholen
2. Zähler auf Null setzen
3. Exakt 10m Kette auslegen (markiert oder gemessen)
4. Zähler prüfen (sollte 10m ±0,5m anzeigen)
5. Korrekturfaktor eingeben (falls System es erlaubt)
6. Gesamte Kette auslegen und Endwert prüfen

### 8.10 Fehlerbild F10: Decksleckage an der Windenbasis

#### 8.10.1 Symptome
- Wassereinbruch unter Deck bei Regen oder Seegang
- Feuchtigkeit um die Windenbasis
- Verquellung/Verfärbung des Decks im Bereich Winde
- Osmotische Schäden am GFK unter der Winde

#### 8.10.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Dichtmasse gealtert/gerissen | Hoch | Dichtung visuell prüfen |
| Bolzen locker → Dichtfuge gebrochen | Mittel | Bolzen auf Festsitz prüfen |
| Riss im GFK-Deck | Mittel | Deck um Winde auf Risse prüfen |
| Decksdurchführung Welle undicht | Mittel | Wellendichtung prüfen |
| Kettenrohr-Dichtung undicht | Niedrig | Kettenrohr-Flansch prüfen |

#### 8.10.3 Reparatur
1. Winde demontieren (alle Bolzen lösen)
2. Alte Dichtmasse vollständig entfernen
3. Deck reinigen und ggf. schleifen
4. Deck auf Schäden prüfen (Kernfäule bei Sandwich)
5. Ggf. Kernbereich sanieren (Epoxid/Glasfaser)
6. Neue Dichtmasse auftragen (Sikaflex 291i)
7. Winde mit neuem Dichtmittel montieren
8. 24h aushärten lassen vor Benutzung

### 8.11 Fehlerbild F11: Gehäusekorrosion

#### 8.11.1 Symptome
- Weiße oder grüne Ablagerungen am Gehäuse
- Rauhe/pitting Oberfläche
- Abblätternde Chrombeschichtung
- Festsitzende Schrauben durch Korrosion
- Schwergängige Mechanik

#### 8.11.2 Korrosionsarten

| Korrosionsart | Erscheinung | Ursache |
|-------------|------------|--------|
| Galvanische Korrosion | Weiße Ablagerungen (Alu) | Ungleichartige Metalle ohne Isolierung |
| Spaltkorrosion | Lochfraß an Spalten | Stehende Feuchtigkeit in engen Spalten |
| Lochfraß (Pitting) | Kleine tiefe Löcher | Chlorid-Ionen (Salzwasser) |
| Erosionskorrosion | Materialabtrag | Sandpartikel in der Kette |
| Kontaktkorrosion | Verfärbung an Kontaktflächen | Edelstahl auf Aluminium |

#### 8.11.3 Prävention
- Regelmäßige Süßwasserspülung nach jedem Salzwassereinsatz
- Korrosionsschutzspray (z.B. CRC 6-66, Boeshield T-9)
- Opferanoden im Bereich Ankerwindeninstallation
- Isolierung ungleichartiger Metalle (Nylonscheiben, Kunststoffbuchsen)
- Regelmäßige Wartung und Schmierung

### 8.12 Fehlerbild F12: Getriebegeräusche

#### 8.12.1 Symptome
- Mahlende/knirschende Geräusche
- Klackendes Geräusch bei jedem Kettenglied
- Vibrationen im Betrieb
- Unregelmäßiger Lauf

#### 8.12.2 Mögliche Ursachen

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Getriebefett/Öl verbraucht | Hoch | Schmiermittel prüfen/nachfüllen |
| Getriebezähne verschlissen | Mittel | Getriebe öffnen, Zähne prüfen |
| Fremdkörper im Getriebe | Mittel | Getriebe öffnen, reinigen |
| Lager verschlissen | Niedrig | Spiel an der Welle prüfen |
| Schneckenrad verschlissen | Niedrig | Zahnspiel prüfen |

#### 8.12.3 Reparatur
1. Getriebe öffnen (Herstelleranleitung beachten)
2. Altes Schmiermittel entfernen
3. Zahnräder und Schnecke auf Verschleiß prüfen
4. Fremdkörper entfernen
5. Neues Getriebefett einfüllen (Herstellerspezifikation)
6. Getriebe verschließen, Dichtigkeitsprüfung

---

## 9. Troubleshooting

### 9.1 Entscheidungsbaum T01: Winde reagiert nicht

```
Winde reagiert gar nicht (kein Geräusch, keine Bewegung)
│
├── Hauptschalter / Sicherungsautomat EIN?
│   ├── NEIN → Einschalten → Funktionstest
│   └── JA ↓
│
├── ANL-Sicherung intakt?
│   ├── NEIN → Ursache für Auslösung suchen (→ F02)
│   │          → Sicherung tauschen → Test
│   └── JA ↓
│
├── Spannung am Solenoid-Eingang vorhanden? (Multimeter)
│   ├── NEIN → Kabelbruch zwischen Batterie und Solenoid
│   │          → Kabel durchmessen, Verbindungen prüfen
│   └── JA ↓
│
├── Solenoid klickt beim Betätigen des Schalters?
│   ├── NEIN → Steuerspannung am Solenoid prüfen
│   │   ├── Keine Steuerspannung → Fußschalter/Helmschalter defekt
│   │   │                          oder Steuerkabel gebrochen
│   │   └── Steuerspannung OK → Solenoid-Spule defekt → tauschen
│   └── JA ↓
│
├── Spannung am Motor-Eingang? (Solenoid-Ausgang)
│   ├── NEIN → Solenoid-Kontakte verbrannt → Solenoid tauschen
│   │          → Kontakte ggf. reinigen (Schmirgel 600er)
│   └── JA ↓
│
├── Motor blockiert? (Versuch manuell zu drehen)
│   ├── JA → Getriebe/Kupplung klemmt → Demontage nötig
│   │         → Korrosion, Fremdkörper, Lagerschaden
│   └── NEIN ↓
│
└── Motor-Wicklung defekt (Widerstand messen)
    ├── Leerlauf-Widerstand <0,5 Ω → Kurzschluss → Motor tauschen
    ├── Leerlauf-Widerstand >100 Ω → Unterbrechung → Motor tauschen
    └── Leerlauf-Widerstand 0,5–5 Ω → Normal → Kohlebürsten prüfen
```

### 9.2 Entscheidungsbaum T02: Winde arbeitet nur in eine Richtung

```
Winde arbeitet nur AUF oder nur AB
│
├── Welche Richtung funktioniert?
│   ├── Nur AUF ↓                   ├── Nur AB ↓
│   │                                │
│   ├── AB-Schalter betätigen:       ├── AUF-Schalter betätigen:
│   │   Klickt Solenoid?             │   Klickt Solenoid?
│   │   ├── NEIN                     │   ├── NEIN
│   │   │   → AB-Schalter/Kabel     │   │   → AUF-Schalter/Kabel
│   │   │     defekt                 │   │     defekt
│   │   └── JA                       │   └── JA
│   │       → Solenoid-AB-Kontakt    │       → Solenoid-AUF-Kontakt
│   │         prüfen                 │         prüfen
│   │       → Spannung am Motor      │       → Spannung am Motor
│   │         (AB-Richtung) messen   │         (AUF-Richtung) messen
│   │                                │
│   └── Motor dreht?                 └── Motor dreht?
│       ├── NEIN → Kontakt verbrannt │       ├── NEIN → Kontakt
│       └── JA → Getriebe/Kupplung   │       └── JA → Getriebe
│                 in einer Richtung   │                 einseitig
│                 blockiert           │                 blockiert
```

### 9.3 Entscheidungsbaum T03: Kette legt sich nicht sauber ab

```
Kette stapelt sich im Kettenkasten, legt sich nicht flach ab
│
├── Kettenrohr-Neigung ausreichend? (min. 30°)
│   ├── NEIN → Kettenrohr steiler montieren
│   │          oder Umlenkrolle einbauen
│   └── JA ↓
│
├── Kettenkasten groß genug? (min. 1,5× Kettenvolumen)
│   ├── NEIN → Kasten vergrößern oder Kettenmenge reduzieren
│   └── JA ↓
│
├── Kette verdreht?
│   ├── JA → Kette komplett auslegen, entwirren, gerade einholen
│   └── NEIN ↓
│
├── Einholgeschwindigkeit zu hoch?
│   ├── JA → Langsamer einholen (pulsierend)
│   └── NEIN ↓
│
├── Kettenkastenform ungünstig?
│   ├── JA → Kettenverteiler installieren (Umlenkblech)
│   │         oder Kastenform anpassen
│   └── NEIN ↓
│
└── Kette fällt frei oder über Kettenstopper?
    ├── Kettenstopper hemmt → Position optimieren
    └── Freier Fall → Normal, Kette vor dem nächsten Auslegen
                       manuell umschichten
```

### 9.4 Entscheidungsbaum T04: Ankerwindenanlage vibriert stark

```
Starke Vibrationen im Betrieb
│
├── Vibration nur beim Einholen oder auch beim Fieren?
│   ├── Nur Einholen → Mechanische Last-Vibration
│   │   ├── Bugrolle klemmt/blockiert → Bugrolle schmieren
│   │   ├── Kette springt an Nuss → Kompatibilität prüfen (→ Kap.6)
│   │   └── Anker klemmt an Bugrolle → Bugrollen-Design prüfen
│   └── Beide Richtungen ↓
│
├── Motor-Befestigung fest?
│   ├── NEIN → Bolzen nachziehen (Drehmomente beachten)
│   └── JA ↓
│
├── Windenbasis fest am Deck?
│   ├── NEIN → Befestigungsbolzen nachziehen
│   │          → Backing Plate prüfen
│   └── JA ↓
│
├── Getriebezustand prüfen
│   ├── Verschleiß → Getriebe überholen (→ F12)
│   └── OK ↓
│
└── Motor-Unwucht oder Lagerschaden
    → Motor zur Werkstatt oder tauschen
```

### 9.5 Entscheidungsbaum T05: Anker sitzt fest

```
Anker kann nicht gehoben werden (Winde blockiert oder Sicherung löst aus)
│
├── SICHERHEIT: Boot NICHT mit der Winde vom Anker losreißen!
│   Windenbelastung begrenzt, Decksbeschläge können brechen.
│
├── Boot über den Anker fahren (Motor voraus)
│   ├── Kette senkrecht über Anker → Winde einsetzen
│   │   ├── Löst sich → OK
│   │   └── Löst sich nicht ↓
│   └── Nicht möglich (enge Bucht etc.) ↓
│
├── Trip-Leine verwenden (falls ausgebracht)
│   ├── Vorhanden → Anker rückwärts ausziehen
│   └── Nicht vorhanden ↓
│
├── Ankerboje verwenden
│   ├── Kette an Boje befestigen, Kette slippern
│   │   → Anker vom Dingi/anderem Boot aus lösen
│   └── Keine Boje vorhanden ↓
│
├── Verschiedene Richtungen versuchen
│   ├── Boot in verschiedene Richtungen fahren
│   │   → Kette dabei kurz holen
│   └── Kein Erfolg ↓
│
├── Taucher / professionelle Hilfe
│   ├── In flachem Wasser: Taucher befreit Anker
│   └── In tiefem Wasser: Kette slippern, Anker aufgeben
│
└── LETZTE OPTION: Kette am Kettenstopper sichern,
    Kettennuss-Kupplung lösen, Kette kontrolliert ablaufen lassen.
    Ankerboje setzen und später bergen.
```

---

## 10. Wartung

### 10.1 Saisonale Wartung — Checkliste

#### 10.1.1 Saisonbeginn (Frühjahr)

| Nr. | Tätigkeit | Zeitaufwand | Material |
|-----|----------|------------|---------|
| 1 | Sichtprüfung Windenkopf und Gehäuse | 10 min | — |
| 2 | Kettennuss auf Verschleiß prüfen | 10 min | — |
| 3 | Kette auf Verschleiß/Korrosion prüfen | 30 min | — |
| 4 | Spillkopf prüfen (Oberfläche, Verschleiß) | 5 min | — |
| 5 | Fußschalter Funktionstest | 5 min | — |
| 6 | Batteriespannung messen | 5 min | Multimeter |
| 7 | Funktionstest Auf/Ab (ohne Last) | 5 min | — |
| 8 | Funktionstest unter Last (5m Kette) | 10 min | — |
| 9 | Kettenzähler kalibrieren | 15 min | — |
| 10 | Kettenkasten reinigen und Drainage prüfen | 20 min | Wasser, Bürste |
| 11 | Bugrolle schmieren | 5 min | Marine-Fett |
| 12 | Dichtungen sichtprüfen | 10 min | — |
| **Gesamt** | | **~130 min** | |

#### 10.1.2 Saisonende (Herbst / Einwinterung)

| Nr. | Tätigkeit | Zeitaufwand | Material |
|-----|----------|------------|---------|
| 1 | Kette komplett auslegen, mit Süßwasser spülen | 45 min | Wasserschlauch |
| 2 | Kette trocknen lassen und auf Verschleiß prüfen | 30 min | — |
| 3 | Kettennuss und Spillkopf reinigen | 15 min | Süßwasser, Bürste |
| 4 | Winde mit Süßwasser spülen | 15 min | Wasserschlauch |
| 5 | Korrosionsschutz auftragen | 15 min | CRC 6-66, Boeshield T-9 |
| 6 | Motor trocken halten (Abdeckung) | 5 min | Plastiktüte/Abdeckung |
| 7 | Batterie abklemmen oder Hauptschalter AUS | 5 min | — |
| 8 | Kettenkasten trocknen lassen (Luke offen) | — | — |
| 9 | Anker reinigen und einlagern | 20 min | — |
| **Gesamt** | | **~150 min** | |

### 10.2 Motor-Bürstenwechsel

#### 10.2.1 Wann Bürsten wechseln?

| Zustand | Bürstenlänge | Maßnahme |
|---------|-------------|----------|
| Neu | 15–20 mm | Normal |
| Verschleiß sichtbar | 10–15 mm | Nächste Saison tauschen |
| Verschlissen | 5–10 mm | Tauschen |
| Kritisch | <5 mm | Sofort tauschen |
| Grenzwert erreicht | Kohle auf Halterniveau | Sofort tauschen, Kommutator prüfen |

#### 10.2.2 Bürstenwechsel-Anleitung

1. Winde stromlos schalten (Hauptschalter, Sicherung ziehen)
2. Motor-Abdeckung öffnen (2–4 Schrauben)
3. Bürsten-Kappen abschrauben (2 Stück, gegenüberliegend)
4. Alte Bürsten herausziehen (auf Federspannung achten)
5. Kommutator prüfen (soll glatt und kupferfarben sein)
6. Kommutator ggf. reinigen (Schmirgelpapier 600er + Druckluft)
7. Neue Bürsten einsetzen (auf korrekte Einbaurichtung achten)
8. Bürsten-Kappen festschrauben
9. Motor-Abdeckung schließen
10. Funktionstest (erst Leerlauf, dann Last)

#### 10.2.3 Bürstenpreise

| Hersteller | Bürstensatz (2 Stück) | Preis EUR |
|-----------|----------------------|-----------|
| Lofrans (Original) | Verschiedene Typen | 25–45 |
| Lewmar (Original) | Verschiedene Typen | 30–50 |
| Quick (Original) | Verschiedene Typen | 25–40 |
| Maxwell (Original) | Verschiedene Typen | 30–50 |
| Universell (Nachbau) | Passend zugeschnitten | 10–20 |

### 10.3 Getriebeöl / Getriebefett

#### 10.3.1 Schmiermittel nach Hersteller

| Hersteller | Empfohlenes Schmiermittel | Menge | Intervall |
|-----------|--------------------------|-------|----------|
| Lofrans | Mobil SHC 460 (Synth.) oder marine Getriebefett | 50–100 ml | Alle 2 Jahre |
| Lewmar | Lewmar Gear Grease (Spezialfett) | 30–80 ml | Jährlich |
| Quick | Quick Winch Grease | 50–100 ml | Alle 2 Jahre |
| Maxwell | Marine-Getriebefett (Lithium-EP2) | 40–80 ml | Alle 2 Jahre |
| Muir | Muir Gearbox Oil (SAE 90) | 80–150 ml | Alle 2 Jahre |

#### 10.3.2 Getriebefett-Wechsel

1. Motor-Abdeckung entfernen
2. Getriebe-Ablassschraube öffnen (falls vorhanden)
3. Altes Fett/Öl ablassen oder ausräumen
4. Getriebe mit Bremsenreiniger ausspülen
5. Neues Fett/Öl einfüllen (Menge lt. Hersteller)
6. Ablassschraube/Deckel verschließen
7. Winde 2 Minuten leer laufen lassen (Fett verteilen)

### 10.4 Kupplungs-Einstellung

#### 10.4.1 Grundprinzip

Die Kupplung (Clutch/Brake) der Ankerwinde dient zwei Funktionen:
1. **Fieren**: Kette kontrolliert ablaufen lassen (Kupplung gelöst)
2. **Halten**: Kette fest halten bei gelöster Kupplung (Kettenstopper)

#### 10.4.2 Einstellung (typische Vertikalwinde)

1. Einstellmutter oben am Windenkopf lokalisieren
2. Im Uhrzeigersinn: Kupplung fester → mehr Bremswirkung
3. Gegen Uhrzeigersinn: Kupplung lockerer → leichteres Fieren
4. Richtwert: Kupplung soll unter 2/3 der Windenzugkraft halten
5. Test: 10m Kette auslegen, Kupplung schließen, an Kette ziehen
6. Sicherstellen: Kette darf bei Seegang NICHT durchrutschen

### 10.5 Wintereinlagerung (Einwinterung)

#### 10.5.1 Komplett-Prozedur

| Schritt | Beschreibung |
|---------|-------------|
| 1 | Kette komplett auslegen, 24h trocknen |
| 2 | Kette mit Kettenfett/Öl einsprühen (optional) |
| 3 | Winde mit Süßwasser spülen, trocknen |
| 4 | Korrosionsschutz auf alle metallischen Flächen |
| 5 | Motor: Abdeckung aufsetzen oder in Plastikfolie |
| 6 | Getriebe: Schmiermittel-Stand prüfen |
| 7 | Batterie: Ladezustand prüfen, ggf. Ladegerät anschließen |
| 8 | Fußschalter: Abdecken oder in Plastikfolie |
| 9 | Kettenkasten: Luke öffnen, durchlüften lassen |
| 10 | Bugrolle: Fetten, Achse prüfen |

#### 10.5.2 Frostschutz

Bei Yachten, die im Winter im Wasser bleiben oder in frostgefährdeten
Regionen an Land stehen:

- Kettenkasten MUSS drainiert sein (kein Wasser)
- Motor-Innenraum trocken halten (Feuchtigkeit → Korrosion)
- Hydraulikwinden: Frostschutzmittel im Ölkreislauf ist NICHT nötig
  (Hydrauliköl friert erst bei <-30°C)
- Elektrische Kontakte mit Kontaktspray schützen
- Dichtungen mit Silikon-Pflegestift behandeln

---

## 11. FAQ

### FAQ 01: Welche Ankerwinde brauche ich für mein Boot?

**Antwort:** Die Windenwahl hängt von der Bootsgröße, dem Ankergewicht
und der Kettenlänge ab. Verwenden Sie die 3:1-Regel: Die Zugkraft der
Winde muss mindestens das Dreifache des Gewichts von Kette + Anker
betragen. Für eine 12m Segelyacht mit 50m × 8mm Kette und 16 kg Anker
empfehlen wir eine Winde mit 500–700 kg Zugkraft. Siehe Abschnitt 4
für die vollständige Dimensionierungstabelle.

### FAQ 02: Vertikal- oder Horizontalwinde?

**Antwort:** Vertikalwinden sind die Standardwahl für Segelyachten (bessere
Ästhetik, Motor geschützt unter Deck). Horizontalwinden eignen sich für
Motorboote, Nachrüstungen oder Boote ohne Platz unter dem Vorschiffsdeck.
Katamarane verwenden häufig Horizontalwinden. Die Leistung ist bei beiden
Typen vergleichbar. Siehe Abschnitt 2.9 für den Vergleich.

### FAQ 03: 12V oder 24V?

**Antwort:** 12V für Boote bis ~15m mit 12V Bordnetz. 24V für Boote ab
12m, besonders wenn der Kabelweg lang ist (>8m). 24V halbiert den Strom
und reduziert Kabelquerschnitte. Wenn Ihr Boot bereits ein 24V-Netz hat,
wählen Sie immer 24V. Siehe Abschnitt 2.5 und 2.6.

### FAQ 04: Wie groß muss die Batterie sein?

**Antwort:** Mindestens 3× die Stromaufnahme der Winde in Ah. Bei einer
80A-Winde also mindestens 240 Ah. Idealerweise separate Starterbatterie
oder eigener Ankerwindenkreis. AGM oder Lithium empfohlen für hohe
Entladeströme. Siehe Abschnitt 4.4.5.

### FAQ 05: Welcher Kabelquerschnitt ist nötig?

**Antwort:** Abhängig von Strom und Kabellänge. Für eine typische 12V-Winde
mit 80A Stromaufnahme und 7m Kabelweg: mindestens 35 mm². Verwenden
Sie die Berechnungstabelle in Abschnitt 4.4.2. Immer verzinntes
Marinekabel verwenden.

### FAQ 06: Kann ich meine Ankerwinde nachrüsten?

**Antwort:** Ja, Nachrüstung ist bei den meisten Booten möglich.
Horizontalwinden sind einfacher nachzurüsten (keine Decksdurchführung).
Wichtig: Deckverstärkung (Backing Plate) ist zwingend erforderlich.
Kabelweg zur Batterie planen, Sicherung/Automat vorsehen. Budget für
Nachrüstung: 800–3.000 EUR (Winde) + 300–800 EUR (Installation).

### FAQ 07: Wie oft muss ich die Ankerwinde warten?

**Antwort:** Saisonbeginn: Funktionsprüfung, Schmierung, Batterie-Check.
Saisonende: Süßwasserspülung, Korrosionsschutz, Wintervorbereitung.
Alle 2 Jahre: Getriebefett wechseln. Alle 500–1.000 Betriebsstunden:
Kohlebürsten prüfen/wechseln. Siehe Abschnitt 10 für die vollständige
Wartungsanleitung.

### FAQ 08: Meine Winde ist langsam — was kann ich tun?

**Antwort:** Die häufigste Ursache ist niedrige Batteriespannung. Messen
Sie die Spannung unter Last (während die Winde arbeitet). Bei 12V sollten
mindestens 11V anliegen. Weitere Ursachen: korrodierte Kabelverbindungen,
zu dünne Kabel, verschlissene Kohlebürsten. Siehe Fehlerbild F04.

### FAQ 09: Kann ich jede Kette auf meiner Winde verwenden?

**Antwort:** NEIN. Nur kalibrierte Kette, die zur Kettennuss passt.
DIN 766 und ISO-Ketten sind NICHT austauschbar. Die Kettengröße muss
exakt stimmen. Verwenden Sie nur kalibrierte Kette (Markierung „KAL").
Siehe Abschnitt 6 für die vollständige Kompatibilitätsübersicht.

### FAQ 10: Was ist ein Kettenzähler und brauche ich einen?

**Antwort:** Ein Kettenzähler zeigt die ausgelassene Kettenlänge in Metern
an. Sehr empfehlenswert ab 10m Bootsgröße oder bei Wassertiefe >10m.
Ermöglicht präzises Ankern (Verhältnis Kette:Tiefe). Systeme ab ~200 EUR
verfügbar. Siehe Abschnitt 7.3.

### FAQ 11: Was bedeutet Duty Cycle?

**Antwort:** Der Duty Cycle gibt die maximale kontinuierliche Betriebsdauer
an, bevor der Motor eine Abkühlpause braucht. Typisch: 3–5 Minuten bei
elektrischen Winden. Danach ~15 Minuten Pause. Überschreitung führt zu
Motor-Überhitzung und kann den Motor beschädigen. Siehe Fehlerbild F01.

### FAQ 12: Brauche ich einen Kettenstopper?

**Antwort:** JA, unbedingt. Die Ankerwinde ist NICHT als dauerhafte
Haltevorrichtung für den Anker konzipiert. Ein Kettenstopper entlastet
die Winde und verhindert, dass die gesamte Ankerlast auf Getriebe und
Motor liegt. Kettenstopper kosten 30–150 EUR und sind schnell montiert.

### FAQ 13: Was ist Free-Fall?

**Antwort:** Free-Fall bedeutet, dass die Kette beim Ankern kontrolliert
durch die Schwerkraft ablaufen kann (Kupplung gelöst). Schneller als
motorisches Fieren, spart Strom. Manche Winden haben einstellbares
Free-Fall (gebremst). Bei unkontrolliertem Free-Fall Verletzungsgefahr!
Nie neben einer ablaufenden Kette stehen.

### FAQ 14: Kann ich eine hydraulische Winde selbst installieren?

**Antwort:** Eine hydraulische Installation ist deutlich komplexer als eine
elektrische. Hydraulik-Schläuche müssen professionell gepresst werden,
das System muss druckgeprüft werden, und eine Hydraulikpumpe muss
dimensioniert und installiert werden. Empfehlung: Fachbetrieb beauftragen.
Budget: 3.000–8.000 EUR für Installation plus Windenkosten.

### FAQ 15: Was tun, wenn der Anker festsitzt?

**Antwort:** NICHT mit der Winde versuchen, den Anker freizureißen!
Das Boot über den Anker fahren (Motor voraus), dann Winde einsetzen.
Wenn das nicht hilft: Trip-Leine verwenden, verschiedene Richtungen
versuchen, oder professionelle Hilfe (Taucher). Siehe
Entscheidungsbaum T05.

### FAQ 16: Wie erkenne ich verschlissene Kette?

**Antwort:** Messen Sie die Glieddicke mit einem Messschieber. Bei mehr als
10% Verschleiß (z.B. 8mm Kette misst nur noch 7,2mm) muss die Kette
getauscht werden. Weitere Anzeichen: rostige Glieder, gelängte Glieder
(Teilung hat sich vergrößert), sichtbare Kerben, steife/klemmende Glieder.

### FAQ 17: Welches Korrosionsschutzmittel ist das beste?

**Antwort:** Empfehlungen:
- **CRC 6-66**: Gut für allgemeinen Korrosionsschutz, wasser-verdrängend
- **Boeshield T-9**: Premium, langanhaltend, von Boeing entwickelt
- **Lanolin-Spray**: Natürlich, langanhaltend, umweltfreundlich
- **WD-40 Marine**: Wasser-verdrängend, kurzfristiger Schutz
Keine Silikonsprays auf Reibflächen (Kupplung, Kettennuss)!

### FAQ 18: Kann ich Edelstahlkette auf einer Standard-Winde verwenden?

**Antwort:** Bedingt. Edelstahlkette ist härter als Standardkette und
verschleißt Aluminium-Kettennüsse schneller. Empfehlung: Edelstahl-
Kettennuss verwenden. Einige Hersteller bieten spezielle Kettennüsse
für Edelstahlketten an. Siehe Abschnitt 6.4.4.

### FAQ 19: Was kostet eine komplette Ankerwindenanlage?

**Antwort:** Richtwerte (komplett installiert):
- 7–9m Boot: 800–2.000 EUR
- 10–12m Boot: 1.500–3.500 EUR
- 13–16m Boot: 2.500–5.000 EUR
- 17–20m Boot: 4.000–10.000 EUR
- 20m+ Boot: 8.000–30.000 EUR

Inklusive: Winde, Kabel, Sicherung, Solenoid, Fußschalter, Installation.

### FAQ 20: Wie wichtig ist die Marke?

**Antwort:** Bei Ankerwinden empfehlen wir Markenprodukte (Lofrans, Lewmar,
Quick, Maxwell, Muir). Die Unterschiede zu No-Name-Produkten liegen in:
- Ersatzteil-Verfügbarkeit (10–20 Jahre)
- Qualität der Getriebe und Dichtungen
- Duty Cycle und Dauerhaltbarkeit
- Korrosionsschutz
- Service-Netzwerk weltweit

### FAQ 21: Kann ich die Kettennuss selbst wechseln?

**Antwort:** Ja, der Kettennuss-Wechsel ist für handwerklich begabte Eigner
machbar. Benötigt: Herstelleranleitung, passender Werkzeugsatz, neue
Kettennuss (auf Kompatibilität achten!). Dauer: ~30–60 Minuten.
Siehe Abschnitt 6.5.2 für die Schritt-für-Schritt-Anleitung.

### FAQ 22: Lohnt sich eine Fernbedienung?

**Antwort:** Eine Funk-Fernbedienung (250–450 EUR) lohnt sich besonders für:
- Solo-Segler (Ankern vom Cockpit aus)
- Große Boote (weiter Weg Bug → Cockpit)
- Häufiges Ankern
Der Fußschalter bleibt als primäre Bedienung obligatorisch.

### FAQ 23: Wie lagere ich die Ankerkette über den Winter?

**Antwort:** Kette komplett aus dem Kettenkasten nehmen, mit Süßwasser
spülen, trocknen lassen, ggf. mit Kettenfett einsprühen. In einem
trockenen Raum lagern (nicht im Kettenkasten!). Vor dem neuen Einsatz
auf Verschleiß prüfen. Verzinkte Kette: Zinkabtrag kontrollieren.

### FAQ 24: Meine Winde macht Geräusche — ist das normal?

**Antwort:** Moderate Motorgeräusche und Kettengeräusche sind normal.
Auffällig sind: Mahlgeräusche (Getriebeschaden), Klacken (Kettennuss-
Verschleiß), Quietschen (trockene Lager), Brummen ohne Bewegung
(Motor blockiert). Siehe Fehlerbild F12.

### FAQ 25: Was ist der Unterschied zwischen Zugkraft und Haltekraft?

**Antwort:** Die **Zugkraft** (Working Load, Pull Force) ist die Kraft, mit
der die Winde die Kette einholen kann. Die **Haltekraft** (Holding Force,
Brake Force) ist die Kraft, die die Kupplung/Bremse statisch halten kann.
Die Haltekraft ist typischerweise 1,5–2× so hoch wie die Zugkraft.
Beide Werte finden Sie im Datenblatt des Herstellers.

### FAQ 26: Kann ich die Winde auch zum Verholen verwenden?

**Antwort:** Ja, wenn die Winde einen Spillkopf hat (Kombiwinde). Die Leine
wird um den Spillkopf gelegt (2–3 Törns) und unter Zug gehalten, während
die Winde dreht. NICHT zum Schleppen verwenden — die Belastung ist zu
hoch und die Kupplung kann beschädigt werden.

### FAQ 27: Wie funktioniert ein Auto-Anker-System?

**Antwort:** Ein Auto-Anker-System kombiniert Kettenzähler mit GPS. Der
Nutzer gibt die gewünschte Kettenlänge ein (oder das System berechnet sie
anhand der Wassertiefe), das System lässt automatisch die richtige Menge
Kette auslaufen und überwacht per GPS, ob der Anker hält. Bei Ankerdrift
gibt es Alarm. Systeme ab ~500 EUR. Siehe Abschnitt 7.4.

---

## 12. Glossar

| Begriff | Englisch | Definition |
|---------|---------|-----------|
| **Ankerboje** | Anchor buoy | Schwimmkörper, der die Ankerposition markiert und zum Bergen dient |
| **Ankergeschirr** | Ground tackle | Gesamtheit aus Anker, Kette, Leine und Befestigungsmitteln |
| **Ankerklüse** | Hawse hole / anchor hawse | Öffnung im Bug für die Ankerkette |
| **Ankerleine** | Anchor rode / anchor line | Tauwerk als Teil des Ankersystems (oft als Kette-Leine-Kombination) |
| **Ankerwinde** | Anchor windlass | Mechanische, elektrische oder hydraulische Einrichtung zum Einholen des Ankers |
| **Ankerwinsch** | Anchor winch | Synonym für Ankerwinde (umgangssprachlich) |
| **ANL-Sicherung** | ANL fuse | Hochstrom-Sicherung für Gleichstromkreise |
| **Backing Plate** | Backing plate | Verstärkungsplatte unter dem Deck zur Lastverteilung |
| **Bugrolle** | Bow roller | Rolle am Bug für die Ketten- und Ankerführung |
| **CAN-Bus** | CAN bus | Controller Area Network, digitales Bussystem für Bordelektronik |
| **Duty Cycle** | Duty cycle | Maximale Einschaltdauer vor Abkühlung |
| **Fieren** | To veer / to pay out | Kette oder Leine kontrolliert ablaufen lassen |
| **Free-Fall** | Free fall | Kontrolliertes Ablaufen der Kette durch Schwerkraft |
| **Fußschalter** | Foot switch | Bodenbedienter Schalter am Bug neben der Ankerwinde |
| **Getriebe** | Gearbox | Untersetzungsgetriebe zwischen Motor und Kettennuss |
| **Helmstation** | Helm station | Steuerstand, Fahrstand |
| **Kalibrierte Kette** | Calibrated chain | Kette mit engen Maßtoleranzen für Kettennuss-Betrieb |
| **Kettenfall** | Chain fall | Senkrechter Abschnitt der Kette von Nuss zum Kasten |
| **Kettenkasten** | Chain locker | Stauraum für die Ankerkette im Vorschiff |
| **Kettennuss** | Gypsy / wildcat | Zahnrad der Ankerwinde, das in die Kettenglieder greift |
| **Kettenrohr** | Chain pipe | Rohr, das die Kette von Deck in den Kettenkasten führt |
| **Kettenstopper** | Chain stopper / devil's claw | Mechanische Vorrichtung zum Festklemmen der Ankerkette |
| **Kettenzähler** | Chain counter | Messgerät für die ausgebrachte Kettenlänge |
| **Klüse** | Fairlead / hawse | Führungselement für Ketten und Leinen |
| **Kohlebürste** | Carbon brush | Verschleißteil im Gleichstrommotor, überträgt Strom auf Rotor |
| **Kommutator** | Commutator | Stromwender im Gleichstrommotor |
| **Kupplung** | Clutch | Lösbares Element zum kontrollierten Fieren der Kette |
| **NMEA 2000** | NMEA 2000 | Standard-Datennetzwerk für Schiffselektronik |
| **Opferanode** | Sacrificial anode | Zinkanode zum galvanischen Korrosionsschutz |
| **PTO** | Power Take-Off | Nebenantrieb am Hauptmotor (für Hydraulikpumpe) |
| **Rode** | Rode | Gesamtlänge aus Kette + Leine (Ankertrosse) |
| **Schneckengetriebe** | Worm gear | Getriebetyp mit hoher Untersetzung, selbsthemmend |
| **Solenoid** | Solenoid | Elektromagnetisches Relais zum Schalten hoher Ströme |
| **Spillkopf** | Capstan / warping drum | Glatte vertikale Trommel zum Aufwickeln von Tauwerk |
| **Stirnradgetriebe** | Spur gear | Getriebetyp mit parallelen Zahnrädern |
| **Teilung** | Pitch | Abstand von Gliedmitte zu Gliedmitte in der Kette |
| **Totmann-Funktion** | Dead-man function | Sicherheitsfunktion: Loslassen = Stopp |
| **Trip-Leine** | Trip line | Hilfsleine am Anker zum Lösen bei festsitzendem Anker |
| **Verholen** | Warping | Boot mittels Leine an einen Poller/Dalben heranziehen |
| **Verholwinsch** | Warping winch | Winde zum Verholen (nur Spillkopf, keine Kettennuss) |
| **Verzinntes Kabel** | Tinned cable | Kupferkabel mit Zinnbeschichtung (Korrosionsschutz) |

---

## 13. Schnell-Referenz

### 13.1 Schnell-Dimensionierung

```
Bootsgröße → Kettengröße → Kettenlänge → Windenzugkraft
──────────────────────────────────────────────────────────
 5–7m     →    6 mm     →   20–30m    →    300 kg
 7–9m     →   6–8 mm    →   30–40m    →    400 kg
 9–12m    →    8 mm     →   40–50m    →    600 kg
12–15m    →  8–10 mm    →   50–60m    →    800 kg
15–18m    →   10 mm     →   60–80m    →  1.200 kg
18–22m    →  10–12 mm   →   70–90m    →  1.800 kg
22m+      →  12–14 mm   →   80–100m   →  2.500 kg+
```

### 13.2 Schnell-Checkliste Installation

```
□ Deckverstärkung (Backing Plate)
□ Bolzengröße und Anzugsmoment
□ Dichtmasse (Sikaflex 291i)
□ Kabelquerschnitt berechnet
□ ANL-Sicherung dimensioniert
□ Solenoid-Relais montiert
□ Fußschalter installiert
□ Helmstation-Schalter (optional)
□ Kettenzähler-Sensor
□ Kettenrohr-Durchführung
□ Kettenkasten-Drainage
□ Kettenkasten-Belüftung
□ Bugrolle passend
□ Kettennuss passend zur Kette
□ Funktionstest Auf/Ab
□ Kettenzähler kalibriert
```

### 13.3 Schnell-Wartung pro Saison

```
FRÜHJAHR:                          HERBST:
□ Sichtprüfung                    □ Kette Süßwasserspülung
□ Funktionstest                    □ Winde Süßwasserspülung
□ Batterie prüfen                  □ Korrosionsschutz
□ Bugrolle schmieren               □ Motor abdecken
□ Kettenzähler kalibrieren         □ Batterie abklemmen/laden
□ Kettenkasten reinigen            □ Kettenkasten trocknen
```

### 13.4 Notfall-Schnellhilfe

```
PROBLEM                    → ERSTE MASSNAHME
─────────────────────────────────────────────
Winde tot                  → Sicherung prüfen
Winde langsam              → Batteriespannung prüfen
Kette rutscht              → Kettenstopper setzen, Nuss prüfen
Motor heiß                 → 15 min Pause
Sicherung löst aus         → Last reduzieren, Ursache suchen
Anker sitzt fest           → Boot über Anker fahren
Kette verklemmt            → Motor stoppen, manuell lösen
Wasser im Motor            → Trocknen, Decksdichtung erneuern
```

---

## 14. ANHANG A–H: Fallstudien

### ANHANG A: Fallstudie — 9m Segelyacht, Ankerwindenauswahl

**Boot:** Bavaria 30, 9,45m LÜA, 4,5t Verdrängung, 12V Bordnetz

**Ausgangssituation:**
- Kein vorhandenes Ankerwinden-System
- Anker: Delta 10 kg am Bugrolle
- Kette: 30m × 8mm DIN 766 + 30m Ankerleine Ø12mm
- Budget: 1.500 EUR maximal

**Dimensionierung:**
```
Kettengewicht:   30m × 1,38 kg/m = 41,4 kg
Ankergewicht:    10 kg
Gesamtgewicht:   51,4 kg
Zugkraft (3:1):  154,2 kg (Minimum)
Empfohlen (×1,5): 231 kg → 300–500 kg Klasse
```

**Windenauswahl:**
| Option | Modell | Zugkraft | Preis EUR | Bewertung |
|--------|--------|---------|-----------|-----------|
| A | Italwinch Smart | 500 kg | 600 | Budget-Tipp |
| B | Lofrans X1 | 500 kg | 850 | Empfehlung |
| C | Lewmar V1 | 400 kg | 800 | Grenzwertig |

**Gewählt:** Lofrans X1 (12V, 500 kg, Kombiwinde mit Spillkopf)

**Elektrische Berechnung:**
```
Motorstrom:      42 A
Kabelweg:        5m (Batterie → Bug)
Kabelquerschnitt: 16 mm² (Tabelle → 42A, 5m, 12V)
Sicherung:       60 A ANL
Batterie:        Starterbatterie 90 Ah (ausreichend)
```

**Installationskosten:**
| Position | Kosten EUR |
|---------|-----------|
| Winde Lofrans X1 | 850 |
| Kabel 16mm² (2×6m) | 65 |
| ANL-Sicherung 60A | 15 |
| Solenoid (im Lieferumfang) | 0 |
| Fußschalter | 55 |
| Backing Plate Edelstahl | 60 |
| Dichtmasse, Schrauben | 35 |
| Kettenrohr GFK | 45 |
| Arbeit (Selbsteinbau) | 0 |
| **Gesamt** | **1.125** |

**Ergebnis:** Erfolgreich installiert, 3 Saisons problemloser Betrieb.

### ANHANG B: Fallstudie — 12m Segelyacht, Windenupgrade

**Boot:** Hallberg-Rassy 37, 11,55m LÜA, 8,2t Verdrängung, 12V Bordnetz

**Ausgangssituation:**
- Alte Winde: Lofrans Royal (20 Jahre, 500 kg, verschlissen)
- Anker: Rocna 15 kg
- Kette: 60m × 8mm DIN 766 (Ganzkette)
- Problem: Winde zu schwach für 60m Ganzkette

**Dimensionierung:**
```
Kettengewicht:   60m × 1,38 kg/m = 82,8 kg
Ankergewicht:    15 kg
Gesamtgewicht:   97,8 kg
Zugkraft (3:1):  293,4 kg (Minimum)
Empfohlen (×1,5): 440 kg → 500–700 kg Klasse
Gewählt:         700 kg (Reserve für Langfahrt)
```

**Windenauswahl:**
| Option | Modell | Zugkraft | Preis EUR |
|--------|--------|---------|-----------|
| A | Lofrans Dorado | 700 kg | 1.500 |
| B | Quick Genius | 700 kg | 1.450 |
| C | Lewmar V2 | 600 kg | 1.250 |
| D | Lofrans X2 | 700 kg | 1.200 |

**Gewählt:** Quick Genius (12V, 700 kg) mit Quick CHC Kettenzähler

**Zusatzkosten Upgrade:**
| Position | Kosten EUR |
|---------|-----------|
| Quick Genius | 1.450 |
| Quick CHC Kettenzähler (komplett) | 420 |
| Kabel 25mm² (Upgrade von 16mm²) | 95 |
| ANL-Sicherung 100A | 18 |
| Neue Fußschalter (2 Stück) | 95 |
| Backing Plate (vorhandene zu klein) | 70 |
| Arbeit (Werft, 8h) | 640 |
| **Gesamt** | **2.788** |

**Ergebnis:** Deutlich schnelleres Einholen, Kettenzähler sehr komfortabel.

### ANHANG C: Fallstudie — 16m Motoryacht, 24V Neuinstallation

**Boot:** Linssen Grand Sturdy 500 AC, 15,90m, 22t, 24V Bordnetz

**Ausgangssituation:**
- Werft-Installation ab Werk, aber Eigner wünscht Upgrade
- Anker: Bruce 20 kg + Delta 25 kg (Zweitanker)
- Kette Hauptanker: 70m × 10mm DIN 766
- Kette Zweitanker: 40m × 8mm DIN 766

**Dimensionierung Hauptanker:**
```
Kettengewicht:   70m × 2,20 kg/m = 154 kg
Ankergewicht:    25 kg (Delta)
Gesamtgewicht:   179 kg
Zugkraft (3:1):  537 kg (Minimum)
Empfohlen (×1,5): 806 kg → 1.000 kg Klasse
```

**Lösung:** Quick Hector (24V, 1.200 kg) + Quick CHC

**Installation:**
- 24V Bordnetz: Kabelquerschnitt 25mm² (50A, 9m)
- Doppel-Fußschalter (Haupt + Zweit)
- Helmstation-Bedienung mit Kettenzähler-Display
- Funk-Fernbedienung (Quick Remote Control)

**Gesamtkosten:** 5.200 EUR (inkl. Werft-Installation)

### ANHANG D: Fallstudie — Katamaran, Doppel-Anker-System

**Boot:** Lagoon 42, 12,80m, 12,5t, 12V Bordnetz

**Besonderheit:** Katamarane haben oft zwei Buganker (einer pro Rumpf)
oder einen zentralen Anker am Brückendeck.

**Konfiguration gewählt:** Zentraler Anker am Brückendeck

**Winde:** Lofrans X3 (12V, 1.000 kg)
- Überdimensioniert, da Katamaran höheren Windwiderstand hat
- Anker: Mantus 15 kg
- Kette: 60m × 10mm DIN 766

**Besonderheiten Katamaran:**
- Horizontalwinde oft bevorzugt (flaches Brückendeck)
- Kettenkastengestaltung schwieriger (wenig Platz im Bug)
- Höherer Windwiderstand → stärkere Winde nötig
- Geteilter Kettenkasten ggf. nötig (Balance)

**Gesamtkosten:** 3.800 EUR (inkl. Kettenkasten-Anpassung)

### ANHANG E: Fallstudie — Klassische Yacht, historische Optik

**Boot:** 35ft Langkieler, Holz-Epoxid, Baujahr 1975, restauriert

**Anforderung:**
- Historische Optik (Bronze-Winde)
- Moderne Funktion (elektrisch)
- Kette: 40m × 8mm DIN 766

**Lösung:** Lofrans Cayman Bronze (Sonderanfertigung)
- Bronzegehäuse (korrosionsfest, klassische Optik)
- Moderner 12V Motor im Bronze-Gehäuse
- Zugkraft: 500 kg

**Besonderheiten:**
- Holzdeck: Keine Sandwich-Problematik, aber Lastspreizung wichtig
- Bronzewinden: Teurer (+50–100% gegenüber Standard-Aluminium)
- Passende Bronze-Klüse und Bronze-Bugrolle

**Gesamtkosten:** 3.200 EUR (Winde + Beschläge + Installation)

### ANHANG F: Fallstudie — Fehldiagnose Motor-Überhitzung

**Boot:** Jeanneau Sun Odyssey 440, 13,3m, 12V
**Winde:** Lewmar V3, 1.000 kg
**Problem:** Motor überhitzt nach 2 Minuten bei 30m Kette

**Diagnose-Verlauf:**
1. Duty Cycle vermutet → aber 30m in 2 min ist normal
2. Batteriespannung gemessen: 12,6V (Leerlauf) → OK
3. **Batteriespannung unter Last:** 9,8V → PROBLEM!
4. Ursache: Korrodierte Batteriepole → hoher Übergangswiderstand
5. Spannungsabfall an Batteriepolen: 1,8V → viel zu hoch

**Lösung:**
- Batteriepole gereinigt und gefettet (Polfett)
- Kabelschuhe erneuert (alte waren korrodiert)
- Spannung unter Last nach Reparatur: 11,4V → OK
- Motor-Überhitzung behoben

**Kosten:** 25 EUR (Polfett + Kabelschuhe)
**Lerneffekt:** Immer Spannung UNTER LAST messen, nicht im Leerlauf!

### ANHANG G: Fallstudie — Kettennuss-Inkompatibilität

**Boot:** Beneteau Oceanis 46.1, 14,6m
**Winde:** Lofrans X3 mit 10mm DIN 766 Kettennuss
**Problem:** Neue Kette rutscht auf der Nuss

**Diagnose:**
1. Alte Kette: DIN 766, 10mm → funktionierte einwandfrei
2. Neue Kette: ISO 4565, 3/8" (9,53mm) → rutscht!
3. Teilung DIN 766 10mm: 28mm
4. Teilung ISO 3/8": 25,4mm
5. Differenz: 2,6mm → Kette „wandert" auf der Nuss

**Lösung:**
- Kette zurückgegeben (Händler hatte ISO statt DIN geliefert)
- Neue kalibrierte DIN 766 10mm Kette bestellt
- Alternativ: ISO-Kettennuss für die Winde bestellen (80 EUR)

**Kosten:** 0 EUR (Umtausch beim Händler)
**Lerneffekt:** Beim Kettenkauf IMMER DIN 766 oder ISO angeben!

### ANHANG H: Fallstudie — Hydraulische Windenanlage auf 22m MY

**Boot:** Custom Aluminium-Motoryacht, 22m, 45t
**Anforderung:** Zwei Anker, Hauptanker + Heckanker

**Konfiguration:**
- Hauptanker: Muir VR5000 (hydraulisch, 2.300 kg)
  - Kette: 100m × 12mm DIN 766
  - Anker: Delta 40 kg
- Heckanker: Maxwell HRC10 (elektrisch 24V, 1.000 kg)
  - Kette: 50m × 10mm DIN 766
  - Anker: Fortress FX-37 (15 kg Alu)

**Hydrauliksystem:**
- PTO-Pumpe am Hauptmotor (Caterpillar C9)
- Volumenstrom: 15 l/min bei 180 bar
- Tank: 25 Liter
- Schläuche: DN 12 Druckleitung, DN 16 Rücklauf
- Steuerventil: Proportionalventil (stufenlose Regelung)

**Gesamt-Investition:**
| Position | Kosten EUR |
|---------|-----------|
| Muir VR5000 (hydraulisch) | 7.500 |
| Maxwell HRC10 (elektrisch) | 2.100 |
| Hydrauliksystem (Pumpe, Tank, Ventile, Schläuche) | 4.800 |
| Kettenzähler (2×) | 900 |
| Fernbedienung (Funk, 2 Kanal) | 450 |
| Ketten (100m 12mm + 50m 10mm) | 1.850 |
| Anker (Delta 40kg + Fortress FX-37) | 1.200 |
| Installation (Werft, 120h) | 9.600 |
| **Gesamt** | **28.400** |

---

## 15. ANHANG I–R: Pydantic v2 Datenmodelle

### ANHANG I: Basisdatenmodell Ankerwinde

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal
from enum import Enum


class WindeTyp(str, Enum):
    VERTIKAL = "vertikal"
    HORIZONTAL = "horizontal"
    MANUAL = "manual"


class AntriebTyp(str, Enum):
    ELEKTRISCH_12V = "elektrisch_12v"
    ELEKTRISCH_24V = "elektrisch_24v"
    HYDRAULISCH = "hydraulisch"
    MANUELL = "manuell"


class KettenStandard(str, Enum):
    DIN_766 = "din_766"
    DIN_764 = "din_764"
    ISO_4565 = "iso_4565"


class AnkerwindeSpec(BaseModel):
    model_config = {"from_attributes": True}

    hersteller: str = Field(..., description="Hersteller der Ankerwinde")
    modell: str = Field(..., description="Modellbezeichnung")
    typ: WindeTyp = Field(..., description="Vertikal, Horizontal oder Manual")
    antrieb: AntriebTyp = Field(..., description="Antriebsart")
    zugkraft_kg: float = Field(..., ge=0, description="Zugkraft in kg")
    motor_leistung_w: Optional[float] = Field(None, ge=0, description="Motorleistung in Watt")
    spannung_v: Optional[int] = Field(None, description="Nennspannung in Volt")
    stromaufnahme_a: Optional[float] = Field(None, ge=0, description="Stromaufnahme unter Last in A")
    ketten_groessen_mm: list[float] = Field(default_factory=list, description="Kompatible Kettengrößen in mm")
    ketten_standard: KettenStandard = Field(default=KettenStandard.DIN_766)
    seil_durchmesser_mm: Optional[tuple[float, float]] = Field(None, description="Min/Max Seildurchmesser in mm")
    duty_cycle_min: Optional[float] = Field(None, ge=0, description="Duty Cycle in Minuten")
    gewicht_kg: Optional[float] = Field(None, ge=0, description="Gesamtgewicht in kg")
    preis_eur_min: Optional[float] = Field(None, ge=0, description="Mindestpreis EUR")
    preis_eur_max: Optional[float] = Field(None, ge=0, description="Maximalpreis EUR")
    boot_groesse_min_m: Optional[float] = Field(None, ge=0, description="Min. Bootsgröße in m")
    boot_groesse_max_m: Optional[float] = Field(None, ge=0, description="Max. Bootsgröße in m")
    has_spillkopf: bool = Field(default=False, description="Hat die Winde einen Spillkopf?")
    has_free_fall: bool = Field(default=False, description="Hat die Winde Free-Fall-Funktion?")
```

### ANHANG J: Dimensionierungsmodell

```python
class AnkerwindenDimensionierung(BaseModel):
    model_config = {"from_attributes": True}

    boot_laenge_m: float = Field(..., ge=0, description="Bootslänge in m")
    boot_verdraengung_t: float = Field(..., ge=0, description="Verdrängung in Tonnen")
    ketten_groesse_mm: float = Field(..., ge=0, description="Kettengröße in mm")
    ketten_laenge_m: float = Field(..., ge=0, description="Kettenlänge in m")
    ketten_gewicht_kg_m: float = Field(..., ge=0, description="Kettengewicht pro Meter in kg")
    anker_gewicht_kg: float = Field(..., ge=0, description="Ankergewicht in kg")
    gesamt_gewicht_kg: float = Field(..., ge=0, description="Gesamtgewicht Kette + Anker in kg")
    min_zugkraft_kg: float = Field(..., ge=0, description="Minimale Zugkraft (3:1-Regel)")
    empf_zugkraft_kg: float = Field(..., ge=0, description="Empfohlene Zugkraft (×1.5 Sicherheit)")
    bordnetz_spannung_v: int = Field(..., description="Bordnetzspannung (12 oder 24)")
    kabel_laenge_m: Optional[float] = Field(None, ge=0, description="Kabellänge Batterie → Winde")
    kabel_querschnitt_mm2: Optional[float] = Field(None, ge=0, description="Berechneter Kabelquerschnitt")
    sicherung_a: Optional[float] = Field(None, ge=0, description="Empfohlene Sicherungsgröße in A")
    batterie_min_ah: Optional[float] = Field(None, ge=0, description="Minimale Batteriekapazität in Ah")
```

### ANHANG K: Installationsmodell

```python
class InstallationCheckpoint(BaseModel):
    model_config = {"from_attributes": True}

    punkt: str = Field(..., description="Prüfpunkt")
    status: Literal["ok", "warnung", "fehler", "nicht_geprueft"] = Field(
        default="nicht_geprueft"
    )
    beschreibung: Optional[str] = Field(None, description="Beschreibung des Befunds")
    empfehlung: Optional[str] = Field(None, description="Empfohlene Maßnahme")


class InstallationBewertung(BaseModel):
    model_config = {"from_attributes": True}

    winde_modell: str
    boot_name: Optional[str] = None
    checkpoints: list[InstallationCheckpoint] = Field(default_factory=list)
    deck_verstaerkung: Literal["ok", "unzureichend", "nicht_vorhanden", "nicht_geprueft"]
    kabel_querschnitt_ok: bool = Field(default=False)
    sicherung_ok: bool = Field(default=False)
    kettennuss_kompatibel: bool = Field(default=False)
    dichtung_ok: bool = Field(default=False)
    gesamt_bewertung: Literal["gut", "akzeptabel", "mangelhaft", "kritisch"] = "nicht_geprueft"
    confidence: str = Field(default="estimated", description="Confidence level der Bewertung")
```

### ANHANG L: Fehlerdiagnose-Modell

```python
class FehlbildCode(str, Enum):
    F01_MOTOR_UEBERHITZUNG = "F01"
    F02_SICHERUNG_LOEST_AUS = "F02"
    F03_KETTE_RUTSCHT = "F03"
    F04_LANGSAMER_BETRIEB = "F04"
    F05_SOLENOID_KLICKT = "F05"
    F06_WASSER_IM_MOTOR = "F06"
    F07_KUPPLUNG_SLIP = "F07"
    F08_SEIL_VERKLEMMUNG = "F08"
    F09_KETTENZAEHLER_DRIFT = "F09"
    F10_DECKSLECKAGE = "F10"
    F11_GEHAEUSE_KORROSION = "F11"
    F12_GETRIEBE_GERAEUSCHE = "F12"


class Fehlerdiagnose(BaseModel):
    model_config = {"from_attributes": True}

    fehlbild: FehlbildCode
    symptome: list[str] = Field(default_factory=list)
    wahrscheinlichste_ursache: str
    alle_ursachen: list[dict[str, str]] = Field(
        default_factory=list,
        description="Liste von {ursache, wahrscheinlichkeit, diagnose}"
    )
    sofortmassnahmen: list[str] = Field(default_factory=list)
    langzeit_loesung: Optional[str] = None
    geschaetzte_kosten_eur: Optional[tuple[float, float]] = None
    confidence: str = Field(default="estimated")
```

### ANHANG M: Wartungsmodell

```python
from datetime import date


class WartungIntervall(str, Enum):
    SAISONBEGINN = "saisonbeginn"
    SAISONENDE = "saisonende"
    JAEHRLICH = "jaehrlich"
    ALLE_2_JAHRE = "alle_2_jahre"
    NACH_BETRIEBSSTUNDEN = "nach_betriebsstunden"


class WartungsAufgabe(BaseModel):
    model_config = {"from_attributes": True}

    aufgabe: str = Field(..., description="Beschreibung der Wartungsaufgabe")
    intervall: WartungIntervall
    betriebsstunden: Optional[int] = Field(None, description="Nach wie vielen Betriebsstunden")
    zeitaufwand_min: int = Field(..., ge=0, description="Geschätzter Zeitaufwand in Minuten")
    material: list[str] = Field(default_factory=list, description="Benötigte Materialien")
    kosten_eur: Optional[float] = Field(None, ge=0, description="Geschätzte Materialkosten")
    letzte_durchfuehrung: Optional[date] = None
    naechste_faellig: Optional[date] = None
    prioritaet: Literal["hoch", "mittel", "niedrig"] = "mittel"


class WartungsPlan(BaseModel):
    model_config = {"from_attributes": True}

    winde_modell: str
    boot_name: Optional[str] = None
    aufgaben: list[WartungsAufgabe] = Field(default_factory=list)
    letzte_inspektion: Optional[date] = None
    naechste_inspektion: Optional[date] = None
    betriebsstunden_gesamt: Optional[int] = None
    zustand: Literal["neuwertig", "gut", "akzeptabel", "wartung_noetig", "reparatur_noetig"] = "gut"
```

### ANHANG N: Kettennuss-Kompatibilitätsmodell

```python
class KettennussKompatibilitaet(BaseModel):
    model_config = {"from_attributes": True}

    winde_hersteller: str
    winde_modell: str
    kettennuss_material: Literal["aluminium", "edelstahl", "bronze", "nylon"]
    ketten_standard: KettenStandard
    ketten_groesse_mm: float
    ketten_teilung_mm: float
    kompatibel: bool
    hinweise: list[str] = Field(default_factory=list)
    ersatz_preis_eur: Optional[float] = None
    verschleiss_prozent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Geschätzter Verschleiß in Prozent"
    )
    tausch_empfohlen: bool = Field(default=False)
```

### ANHANG O: Elektrische Berechnung-Modell

```python
class ElektrischeBerechnung(BaseModel):
    model_config = {"from_attributes": True}

    spannung_v: int = Field(..., description="Bordnetzspannung")
    motorstrom_a: float = Field(..., ge=0, description="Motorstrom unter Last")
    kabel_laenge_m: float = Field(..., ge=0, description="Einfache Kabellänge")
    spannungsabfall_max_v: float = Field(..., ge=0, description="Max. zulässiger Spannungsabfall")
    spannungsabfall_max_prozent: float = Field(default=10.0, description="Max. Spannungsabfall in %")
    kabel_querschnitt_berechnet_mm2: float = Field(..., ge=0, description="Berechneter Querschnitt")
    kabel_querschnitt_gewaehlt_mm2: float = Field(..., ge=0, description="Gewählter Standardquerschnitt")
    sicherung_berechnet_a: float = Field(..., ge=0, description="Berechnete Sicherungsgröße")
    sicherung_gewaehlt_a: float = Field(..., ge=0, description="Gewählte Standardsicherung")
    batterie_min_ah: float = Field(..., ge=0, description="Mindest-Batteriekapazität")
    spannungsabfall_tatsaechlich_v: Optional[float] = Field(None, ge=0)
    spannungsabfall_tatsaechlich_prozent: Optional[float] = Field(None, ge=0)
    bewertung: Literal["ok", "grenzwertig", "unzureichend"] = "ok"
```

### ANHANG P: Hersteller-Datenbank-Modell

```python
class HerstellerInfo(BaseModel):
    model_config = {"from_attributes": True}

    name: str = Field(..., description="Herstellername")
    herkunftsland: str
    gruendungsjahr: Optional[int] = None
    marktsegment: list[str] = Field(default_factory=list)
    marktanteil_prozent: Optional[float] = Field(None, ge=0, le=100)
    website: Optional[str] = None
    service_netzwerk: Literal["weltweit", "europa", "regional", "begrenzt"] = "europa"
    ersatzteil_verfuegbarkeit_jahre: Optional[int] = None
    modelle: list[AnkerwindeSpec] = Field(default_factory=list)


class HerstellerDatenbank(BaseModel):
    model_config = {"from_attributes": True}

    hersteller: list[HerstellerInfo] = Field(default_factory=list)
    letzte_aktualisierung: str = Field(default="2026-04")
    version: str = Field(default="2.0")
```

### ANHANG Q: Visuelle Analyse-Modell

```python
class VisuelleBewertungAnkerwinde(BaseModel):
    model_config = {"from_attributes": True}

    erkannter_typ: Optional[WindeTyp] = None
    erkannter_hersteller: Optional[str] = None
    erkanntes_modell: Optional[str] = None
    geschaetzte_groesse: Optional[str] = None
    zustand_gehaeuse: Optional[Literal["neuwertig", "gut", "maessig", "schlecht", "nicht_beurteilbar"]] = None
    zustand_kettennuss: Optional[Literal["neuwertig", "gut", "verschlissen", "stark_verschlissen", "nicht_beurteilbar"]] = None
    zustand_spillkopf: Optional[Literal["neuwertig", "gut", "verschlissen", "nicht_beurteilbar"]] = None
    korrosion_sichtbar: Optional[bool] = None
    korrosion_grad: Optional[Literal["keine", "leicht", "mittel", "stark", "nicht_beurteilbar"]] = None
    installation_qualitaet: Optional[Literal["professionell", "gut", "akzeptabel", "mangelhaft", "nicht_beurteilbar"]] = None
    dichtung_zustand: Optional[Literal["gut", "alternd", "undicht", "nicht_beurteilbar"]] = None
    kettenlauf_sichtbar: Optional[bool] = None
    bugrolle_zustand: Optional[Literal["gut", "verschlissen", "beschaedigt", "nicht_beurteilbar"]] = None
    befunde: list[str] = Field(default_factory=list)
    empfehlungen: list[str] = Field(default_factory=list)
    confidence: Literal[
        "visual_high", "visual_medium", "visual_low", "visual_insufficient"
    ] = "visual_medium"
    model_version: str = Field(default="claude-3-opus-20240229")
```

### ANHANG R: Gesamtbewertung Ankerwindensystem

```python
class AnkerwindenGesamtbewertung(BaseModel):
    model_config = {"from_attributes": True}

    boot_name: Optional[str] = None
    boot_laenge_m: Optional[float] = None
    boot_typ: Optional[str] = None

    # Einzelbewertungen (0-100)
    score_dimensionierung: Optional[float] = Field(None, ge=0, le=100)
    score_installation: Optional[float] = Field(None, ge=0, le=100)
    score_elektrik: Optional[float] = Field(None, ge=0, le=100)
    score_kettennuss_kompatibilitaet: Optional[float] = Field(None, ge=0, le=100)
    score_zustand: Optional[float] = Field(None, ge=0, le=100)
    score_wartung: Optional[float] = Field(None, ge=0, le=100)
    score_sicherheit: Optional[float] = Field(None, ge=0, le=100)

    # Gesamtscore
    gesamt_score: Optional[float] = Field(None, ge=0, le=100)

    # Befunde
    befunde_kritisch: list[str] = Field(default_factory=list)
    befunde_warnung: list[str] = Field(default_factory=list)
    befunde_info: list[str] = Field(default_factory=list)

    # Empfehlungen
    empfehlungen: list[str] = Field(default_factory=list)
    geschaetzte_kosten_eur: Optional[tuple[float, float]] = None

    # Confidence
    confidence_dimensionierung: str = "estimated"
    confidence_installation: str = "estimated"
    confidence_elektrik: str = "estimated"
    confidence_zustand: str = "estimated"
    confidence_gesamt: str = "estimated"

    # Meta
    analyse_datum: Optional[str] = None
    analysiert_von: str = "AYDI Ankerwindenmodul v2.0"


class AnkerwindenAnalyseResult(BaseModel):
    model_config = {"from_attributes": True}

    available: bool = Field(default=True, description="Kann die Analyse durchgeführt werden?")
    reason: Optional[str] = Field(None, description="Grund, falls nicht verfügbar")
    winde_spec: Optional[AnkerwindeSpec] = None
    dimensionierung: Optional[AnkerwindenDimensionierung] = None
    installation: Optional[InstallationBewertung] = None
    kettennuss: Optional[KettennussKompatibilitaet] = None
    elektrik: Optional[ElektrischeBerechnung] = None
    fehlerdiagnosen: list[Fehlerdiagnose] = Field(default_factory=list)
    wartungsplan: Optional[WartungsPlan] = None
    visuelle_bewertung: Optional[VisuelleBewertungAnkerwinde] = None
    gesamtbewertung: Optional[AnkerwindenGesamtbewertung] = None
```

---

## 16. Ergänzende Technische Referenzen

### 16.1 Drehmoment-Tabelle für Befestigungsbolzen

| Bolzengröße | Material A2-70 | Material A4-70 | Material A4-80 |
|------------|---------------|---------------|---------------|
| M6 | 8,5 Nm | 8,5 Nm | 10 Nm |
| M8 | 20 Nm | 20 Nm | 25 Nm |
| M10 | 40 Nm | 40 Nm | 49 Nm |
| M12 | 69 Nm | 69 Nm | 85 Nm |
| M14 | 110 Nm | 110 Nm | 135 Nm |
| M16 | 170 Nm | 170 Nm | 210 Nm |

**Hinweis:** Werte gelten für trockene, unbeschichtete Gewinde.
Bei Verwendung von Schraubensicherung (Loctite 243) oder Fett:
Drehmoment um ca. 20% reduzieren.

### 16.2 Kettengewicht und Zugkraft — Erweiterte Tabelle

| Kettengröße | Gewicht/m (verzinkt) | Gewicht/m (Edelstahl) | Bruchlast G40 | Bruchlast G70 | Preis/m EUR (verzinkt) | Preis/m EUR (Edelstahl) |
|------------|---------------------|---------------------|--------------|--------------|--------------------|-----------------------|
| 6 mm | 0,78 kg | 0,80 kg | 1.600 kg | 2.800 kg | 3,00–4,50 | 8,00–12,00 |
| 7 mm | 1,08 kg | 1,10 kg | 2.200 kg | 3.800 kg | 3,50–5,50 | 10,00–15,00 |
| 8 mm | 1,38 kg | 1,42 kg | 2.800 kg | 5.000 kg | 4,50–7,00 | 12,00–18,00 |
| 10 mm | 2,20 kg | 2,25 kg | 4.000 kg | 7.100 kg | 6,50–10,00 | 18,00–28,00 |
| 12 mm | 3,10 kg | 3,18 kg | 5.600 kg | 10.000 kg | 9,00–14,00 | 25,00–40,00 |
| 13 mm | 3,65 kg | 3,74 kg | 6.600 kg | 11.800 kg | 10,00–16,00 | 30,00–48,00 |
| 14 mm | 4,25 kg | 4,35 kg | 7.700 kg | 13.700 kg | 12,00–19,00 | 35,00–55,00 |
| 16 mm | 5,60 kg | 5,74 kg | 10.000 kg | 17.800 kg | 16,00–25,00 | 50,00–75,00 |

> ⚠️ **ZU PRÜFEN (Audit):** Die Bruchlast-Spalten (G40/G70) widersprechen Abschnitt 6.4.3
> (8 mm: G40 2.800 vs. 3.200 kg; G70 5.000 vs. 5.600 kg) und liegen unter den Herstellerangaben
> (8 mm G40 ≈ 4.300 kg, G70 ≈ 7.000 kg laut Lofrans / Jimmy Green Marine, ISO 4565 / DIN 766).
> Bruchlast-Werte unverifiziert — **Confidence: estimated — unverifiziert.**
> Vor sicherheitsrelevanter Nutzung Herstellerdatenblatt heranziehen.

### 16.3 Anker-Dimensionierungstabelle nach CE-Kategorie

| Bootsgröße | CE-Kategorie A (Ozean) | CE-Kategorie B (Offshore) | CE-Kategorie C (Küste) | CE-Kategorie D (Geschützt) |
|------------|----------------------|-------------------------|---------------------|-------------------------|
| 6–8m | 10 kg + 40m 8mm | 8 kg + 30m 6mm | 6 kg + 25m 6mm | 4 kg + 20m 6mm |
| 8–10m | 14 kg + 50m 8mm | 10 kg + 40m 8mm | 8 kg + 30m 6mm | 6 kg + 25m 6mm |
| 10–12m | 20 kg + 60m 10mm | 16 kg + 50m 8mm | 12 kg + 40m 8mm | 10 kg + 30m 8mm |
| 12–15m | 25 kg + 70m 10mm | 20 kg + 60m 10mm | 16 kg + 50m 8mm | 14 kg + 40m 8mm |
| 15–18m | 35 kg + 80m 10mm | 25 kg + 70m 10mm | 20 kg + 60m 10mm | 16 kg + 50m 10mm |
| 18–22m | 50 kg + 100m 12mm | 40 kg + 80m 10mm | 30 kg + 70m 10mm | 25 kg + 60m 10mm |

### 16.4 Korrosionsschutz-Produkte — Detailvergleich

| Produkt | Typ | Salzwasser-Schutz | Dauer | Temperatur | Preis EUR (400ml) |
|---------|-----|------------------|-------|-----------|------------------|
| CRC 6-66 | Wasserverdrängend | Gut | 3–6 Monate | -20 bis +70°C | 8–12 |
| Boeshield T-9 | Wachsfilm | Sehr gut | 6–12 Monate | -20 bis +120°C | 14–18 |
| Lanolin-Spray (Lanocote) | Natürliches Fett | Sehr gut | 6–12 Monate | -10 bis +80°C | 12–16 |
| WD-40 Marine | Wasserverdrängend | Mäßig | 1–3 Monate | -20 bis +70°C | 8–12 |
| Tef-Gel | PTFE-Paste | Ausgezeichnet | Dauerhaft | -40 bis +250°C | 18–25 (Tube) |
| ACF-50 | Filmbildend | Ausgezeichnet | 12 Monate | -30 bis +120°C | 16–22 |
| Corrosion Block | Wachsfilm | Gut | 3–6 Monate | -20 bis +80°C | 10–14 |

### 16.5 Lebenszyklus-Kostenanalyse

#### 16.5.1 20-Jahres-Kostenrechnung (12m Segelyacht)

| Kostenposition | Jahr 0 | Jahre 1–5 | Jahre 6–10 | Jahre 11–15 | Jahre 16–20 | Gesamt |
|---------------|--------|----------|-----------|-----------|-----------|--------|
| Ankerwinde (Kauf) | 1.500 | — | — | — | — | 1.500 |
| Installation | 800 | — | — | — | — | 800 |
| Wartung (jährlich) | — | 250 | 350 | 450 | 500 | 1.550 |
| Kohlebürsten (2×) | — | 45 | 45 | 45 | 45 | 180 |
| Getriebefett (5×) | — | 30 | 30 | 30 | 30 | 120 |
| Kettennuss-Tausch (2×) | — | — | 180 | — | 180 | 360 |
| Motor-Überholung (1×) | — | — | — | 400 | — | 400 |
| Kette (2× in 20 Jahren) | 350 | — | 350 | — | 350 | 1.050 |
| Fußschalter-Tausch (1×) | — | — | — | 70 | — | 70 |
| Solenoid-Tausch (1×) | — | — | — | — | 120 | 120 |
| **Summe** | **2.650** | **325** | **955** | **995** | **1.225** | **6.150** |

#### 16.5.2 Vergleich: Günstige vs. Premium-Winde über 20 Jahre

| Aspekt | Budget-Winde (Italwinch) | Premium-Winde (Quick Genius) |
|--------|------------------------|---------------------------|
| Anschaffung | 650 EUR | 1.500 EUR |
| Wartung (20 J.) | 2.500 EUR | 1.800 EUR |
| Reparaturen (20 J.) | 1.200 EUR | 600 EUR |
| Ersatz (nach 12 J.) | 700 EUR | — |
| **Gesamtkosten 20 J.** | **5.050 EUR** | **3.900 EUR** |
| **Kosten pro Jahr** | **253 EUR** | **195 EUR** |

**Ergebnis:** Die Premium-Winde ist über 20 Jahre betrachtet ca. 23%
günstiger als die Budget-Winde — vorausgesetzt, die Budget-Winde muss
nach 12 Jahren ersetzt werden.

### 16.6 Schallpegel-Referenz

| Windentyp | Leerlauf | Unter Last | Volllast |
|----------|---------|-----------|---------|
| Elektrisch (Vertikal, klein) | 55–60 dB(A) | 65–70 dB(A) | 72–78 dB(A) |
| Elektrisch (Vertikal, groß) | 58–63 dB(A) | 68–74 dB(A) | 75–82 dB(A) |
| Elektrisch (Horizontal) | 60–65 dB(A) | 70–76 dB(A) | 78–85 dB(A) |
| Hydraulisch | 45–50 dB(A) | 52–58 dB(A) | 58–65 dB(A) |
| Handwinde | 40–45 dB(A) | 50–55 dB(A) | 55–60 dB(A) |

**Hinweis:** Horizontalwinden sind an Deck lauter, da Motor und Getriebe
nicht durch den Decksaufbau gedämpft werden. Hydraulikwinden sind an
Deck am leisesten, die Pumpe (im Maschinenraum) erzeugt dort 70–80 dB(A).

### 16.7 Geschwindigkeits-Referenz (Einholgeschwindigkeit)

| Windengröße (Zugkraft) | Leerlauf (ohne Last) | Unter 50% Last | Unter 100% Last |
|------------------------|---------------------|---------------|----------------|
| 300–500 kg | 25–35 m/min | 15–22 m/min | 8–12 m/min |
| 500–800 kg | 20–30 m/min | 12–18 m/min | 6–10 m/min |
| 800–1.200 kg | 18–25 m/min | 10–15 m/min | 5–8 m/min |
| 1.200–1.500 kg | 15–22 m/min | 8–12 m/min | 4–7 m/min |
| 1.500–2.500 kg | 12–18 m/min | 6–10 m/min | 3–5 m/min |
| 2.500+ kg | 10–15 m/min | 5–8 m/min | 2–4 m/min |

### 16.8 Ankertyp-Empfehlungen je Untergrund

| Untergrund | Empfohlene Ankertypen | Haltekraft-Faktor | Festsitz-Risiko |
|-----------|---------------------|------------------|----------------|
| Sand (fest) | Bügelanker, Rocna, Delta | Hoch (8–12×) | Niedrig |
| Sand (weich) | Bügelanker, Rocna, Mantus | Mittel (5–8×) | Niedrig |
| Schlick/Schlamm | Danforth, Fortress | Mittel (4–7×) | Niedrig |
| Ton/Lehm | Bügelanker, CQR, Delta | Hoch (8–15×) | Hoch |
| Seegras | Rocna, Mantus, Bügelanker | Niedrig (2–4×) | Niedrig |
| Kies/Geröll | Delta, CQR | Mittel (4–6×) | Mittel |
| Fels | Klappanker, Fisherman | Variabel | Sehr hoch |
| Koralle | Fortress, Danforth (verboten!) | — | — |

**Relevanz für die Winde:** Bei hohem Festsitz-Risiko (Ton, Fels) muss
die Winde stärker dimensioniert werden oder ein Trip-System vorgesehen
sein. Die Winde sollte NICHT zum Losreißen des Ankers verwendet werden.

### 16.9 Checkliste Saisonale Ketteninspektion

| Prüfpunkt | Methode | Grenzwert | Maßnahme bei Überschreitung |
|----------|---------|----------|---------------------------|
| Glieddicke | Messschieber an 5 Stellen | <90% Nenndicke → tauschen | Kette ersetzen |
| Gliedlänge (Teilung) | Messschieber über 10 Glieder | >103% Nenn-Teilung | Kette ersetzen |
| Verdrehte Glieder | Sichtprüfung | Kein Glied >15° verdreht | Kette ersetzen (Abschnitt) |
| Rostbildung (verzinkt) | Sichtprüfung | >30% Oberfläche rostbraun | Neuverzinken oder ersetzen |
| Verbindungsglied (Schäkel) | Sichtprüfung + Maß | Sicherung vorhanden, Maß ok | Schäkel ersetzen |
| Markierungen | Sichtprüfung | Alle 5m/10m Markierung vorhanden | Neu markieren |
| Kettennuss-Sitz | 3m Kette über Nuss laufen lassen | Kein Spiel, kein Rutschen | Nuss oder Kette tauschen |
| Endbefestigung | Sichtprüfung | Gesichert, kein Verschleiß | Befestigung erneuern |

### 16.10 Elektromagnetische Verträglichkeit (EMV)

Ankerwinden-Motoren erzeugen beim Betrieb erhebliche elektromagnetische
Störungen, die empfindliche Bordelektronik beeinflussen können.

| Störungsquelle | Frequenzbereich | Betroffene Geräte | Gegenmaßnahme |
|---------------|----------------|-------------------|--------------|
| Kommutator-Funken | 1–100 MHz | UKW-Funk, AIS, GPS | Entstörfilter am Motor |
| Solenoid-Schaltimpulse | 0,1–10 MHz | Plotter, Radar | Freilaufdiode am Solenoid |
| Stromspitzen (Kabel) | 0,01–1 MHz | Instrumente | Separate Batterieversorgung |
| PWM-Steuerung (modern) | 10–200 kHz | SSB-Funk | Abgeschirmte Kabel |

**Empfehlung:** Ankerwinden-Kabel NICHT parallel zu Signalkabeln
(NMEA, Funkkabel, Antennenkabel) verlegen. Mindestabstand 30 cm.
Bei unvermeidbarer Kreuzung: 90° Kreuzungswinkel.

### 16.11 Gewichtsvergleich Ankerwindensysteme

Detaillierter Gewichtsvergleich für typische Konfigurationen:

| Konfiguration | Winde | Kette | Anker | Bugrolle/Klüse | Kabel/Solenoid | Kettenkasten | Gesamt |
|--------------|-------|-------|-------|----------------|---------------|-------------|--------|
| 8m Segelyacht (6mm/30m) | 10 kg | 23 kg | 8 kg | 3 kg | 3 kg | 5 kg | 52 kg |
| 10m Segelyacht (8mm/40m) | 14 kg | 55 kg | 12 kg | 4 kg | 4 kg | 7 kg | 96 kg |
| 12m Segelyacht (8mm/50m) | 18 kg | 69 kg | 16 kg | 5 kg | 5 kg | 8 kg | 121 kg |
| 14m Segelyacht (10mm/60m) | 22 kg | 132 kg | 20 kg | 6 kg | 6 kg | 10 kg | 196 kg |
| 16m Motoryacht (10mm/70m) | 28 kg | 154 kg | 25 kg | 7 kg | 7 kg | 12 kg | 233 kg |
| 18m Motoryacht (10mm/80m) | 34 kg | 176 kg | 30 kg | 8 kg | 8 kg | 15 kg | 271 kg |
| 22m Motoryacht (12mm/100m) | 48 kg | 310 kg | 45 kg | 10 kg | 10 kg | 20 kg | 443 kg |

**Trimm-Einfluss:** Diese Gewichte befinden sich am vorderen Ende des
Bootes und haben erheblichen Einfluss auf den Längstrimm. Bei der
AYDI-Strukturanalyse wird das Ankerwindengewicht als Vorschiffslast
in die Gewichtsverteilungsberechnung einbezogen.

### 16.12 Betriebskostenvergleich nach Antriebsart

| Kostenfaktor | Elektrisch 12V | Elektrisch 24V | Hydraulisch |
|-------------|---------------|---------------|------------|
| Energieverbrauch pro Ankermanöver | 0,08–0,15 kWh | 0,08–0,15 kWh | 0,5–1,0 l Diesel |
| Energiekosten pro Ankermanöver | 0,02–0,04 EUR | 0,02–0,04 EUR | 0,80–1,60 EUR |
| Jährliche Wartungskosten | 50–120 EUR | 50–120 EUR | 150–400 EUR |
| Ersatzteile (Ø pro Jahr) | 30–80 EUR | 30–80 EUR | 50–150 EUR |
| Lebensdauer Motor/Pumpe | 10–15 Jahre | 12–18 Jahre | 15–25 Jahre |
| Lebensdauer Getriebe | 8–12 Jahre | 10–15 Jahre | 15–20 Jahre |

### 16.13 Sicherheitsabstände und Ergonomie

| Parameter | Mindestmaß | Empfohlen | Bezugsnorm |
|-----------|-----------|-----------|-----------|
| Abstand Fußschalter ↔ Klüse | 300 mm | 500 mm | ISO 15085 |
| Abstand Fußschalter ↔ Kettennuss | 200 mm | 400 mm | Praxis |
| Freiraum um Windenkopf | 150 mm radial | 250 mm radial | Praxis |
| Stehhöhe am Windenbedienplatz | 1.600 mm | 1.800 mm | Ergonomie |
| Reling-Höhe am Bug (Arbeitshöhe) | 600 mm | 750 mm | ISO 15085 |
| Kettenrohr-Öffnung Abstand zu Fuß | 200 mm | 350 mm | Sicherheit |
| Handkurbel-Drehradius (frei) | 400 mm | 500 mm | Ergonomie |
| Zugänglichkeit Motor (unter Deck) | Inspektionsluke 300×300 | 400×400 | Wartung |

### 16.14 Typische Ausfallraten und MTBF

| Komponente | Mittlere Lebensdauer | MTBF (Betriebsstunden) | Häufigster Ausfall |
|-----------|---------------------|----------------------|-------------------|
| Gleichstrommotor | 10–15 Jahre | 2.000–4.000 h | Kohlebürstenverschleiß |
| Solenoid-Relais | 8–12 Jahre | 50.000–100.000 Schaltzyklen | Kontaktabbrand |
| Getriebe (Schnecke) | 10–20 Jahre | 3.000–8.000 h | Zahnverschleiß |
| Kettennuss (Alu) | 5–10 Jahre | 1.500–3.000 h | Profilverschleiß |
| Kettennuss (Edelstahl) | 10–20 Jahre | 3.000–6.000 h | Profilverschleiß |
| Fußschalter | 8–15 Jahre | 30.000–80.000 Betätigungen | Membranriss |
| Wellendichtung | 5–8 Jahre | — | Aushärtung, Undichtigkeit |
| Kupplung/Bremse | 5–10 Jahre | 1.000–3.000 h | Belagverschleiß |
| Kettenzähler-Sensor | 8–12 Jahre | — | Verschmutzung/Drift |
| Hydraulikpumpe | 15–25 Jahre | 5.000–15.000 h | Dichtungsverschleiß |
| Hydraulikschläuche | 6–10 Jahre | — | Alterung, Sprödbruch |

### 16.15 Ersatzteil-Verfügbarkeit nach Hersteller

| Hersteller | Ersatzteile ab Lager | Lieferzeit (Standard) | Lieferzeit (Sonderteile) | Verfügbarkeit ältere Modelle |
|-----------|--------------------|--------------------|----------------------|---------------------------|
| Lofrans | Ja (Standardteile) | 3–7 Werktage | 2–4 Wochen | 15+ Jahre (gute Versorgung) |
| Lewmar | Ja (breites Lager) | 3–5 Werktage | 2–3 Wochen | 20+ Jahre (sehr gut) |
| Quick | Ja (Standardteile) | 5–10 Werktage | 3–5 Wochen | 12+ Jahre |
| Maxwell | Teilweise | 7–14 Werktage | 4–8 Wochen | 10+ Jahre |
| Muir | Nur Händler | 10–20 Werktage | 6–12 Wochen | 10+ Jahre |
| Italwinch | Begrenzt | 7–14 Werktage | 4–6 Wochen | 8+ Jahre |

### 16.16 Häufige Installationsfehler

| Fehler | Folge | Vermeidung |
|--------|-------|-----------|
| Keine Backing Plate | Deck reißt unter Last | Immer Backing Plate montieren |
| Sandwich-Kern nicht entfernt | Kernfäule, Delamination | Kern im Befestigungsbereich ersetzen |
| Kabel zu dünn | Überhitzung, Spannungsabfall | Berechnung nach Abschnitt 4.4 |
| Sicherung zu klein | Löst bei jedem Einsatz aus | Herstellerangabe beachten |
| Sicherung zu groß | Kein Schutz bei Kurzschluss | Nie >150% des Motorstroms |
| Massekabel über Sammelschiene | Spannungsabfall, Korrosion | Direkt zur Batterie führen |
| Kettenrohr zu steil | Kette klemmt | Neigung 30–60° optimal |
| Kettenrohr zu flach | Kette staut sich | Mindestens 30° Neigung |
| Dichtmasse Silikon statt PU | Haftet nicht auf GFK | Sikaflex 291i oder 3M 5200 |
| Falsche Kettennuss bestellt | Kette rutscht/klemmt | Ketten-Standard exakt angeben |
| Fußschalter ohne Drainage | Wasser im Schalter, Kurzschluss | Drainagebohrung vorsehen |
| Kettenkasten ohne Belüftung | Fäulnis, Gestank | Belüftungsöffnung obligatorisch |
| Motor ohne Zugang | Wartung unmöglich | Inspektionsluke einplanen |
| Kabelverbindungen ungeschützt | Korrosion, Ausfall | Schrumpfschlauch, Kabelschuhe |

---

*Ende der Wissensbasis 17_03 — Ankerwinden*
*Version 2.0, Stand April 2026*
*AYDI Maritime Knowledge Base*
