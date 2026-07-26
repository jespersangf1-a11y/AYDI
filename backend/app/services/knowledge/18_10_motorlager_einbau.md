---
titel: "Motorlager, Einbau und Ausrichtung"
kategorie: "Motoren und Antrieb"
unterkategorie: "Motorlager und Einbau"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 18_10 — Motorlager, Einbau und Ausrichtung

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Motorlager-Typen und Bauformen](#2-motorlager-typen-und-bauformen)
3. [Hersteller und Produktlinien](#3-hersteller-und-produktlinien)
4. [Motorlager-Dimensionierung](#4-motorlager-dimensionierung)
5. [Shore-Härte, Deflexion und Schwingungsverhalten](#5-shore-härte-deflexion-und-schwingungsverhalten)
6. [Motorfundament — Konstruktion und Materialien](#6-motorfundament--konstruktion-und-materialien)
7. [Motor-Alignment — Ausrichtung der Antriebsanlage](#7-motor-alignment--ausrichtung-der-antriebsanlage)
8. [Schallschutz und Vibrationsdämpfung](#8-schallschutz-und-vibrationsdämpfung)
9. [Motorraum-Belüftung](#9-motorraum-belüftung)
10. [Motorraum-Isolation](#10-motorraum-isolation)
11. [Motorraumzugang und Wartungsräume](#11-motorraumzugang-und-wartungsräume)
12. [Motorumrüstung (Repowering)](#12-motorumrüstung-repowering)
13. [Normen und Vorschriften](#13-normen-und-vorschriften)
14. [Fehlerbild-Atlas](#14-fehlerbild-atlas)
15. [Troubleshooting](#15-troubleshooting)
16. [FAQ — Häufige Fragen](#16-faq--häufige-fragen)
17. [Glossar](#17-glossar)
18. [Schnell-Referenz](#18-schnell-referenz)
19. [ANHANG A–H: Fallstudien](#19-anhang-ah-fallstudien)
20. [ANHANG I–R: Pydantic v2 Datenmodelle](#20-anhang-ir-pydantic-v2-datenmodelle)

---
---

## 1. Einführung

### 1.1 Bedeutung der Motorlagerung im Yachtbau

Die Motorlagerung ist eines der am meisten unterschätzten Systeme einer Yacht.
Ein korrekt gelagerter und ausgerichteter Motor läuft ruhig, vibrationsarm
und mit maximaler Lebensdauer. Ein fehlerhaft gelagerter Motor dagegen erzeugt
Vibrationen, die das gesamte Schiff durchdringen, Getriebeausgangsflansche
belasten, Wellenkupplungen beschädigen und den Wohnkomfort massiv
beeinträchtigen.

Die Motorlagerung erfüllt mehrere Funktionen gleichzeitig:

- **Tragfunktion**: Das Motorgewicht (typisch 80–2.500 kg bei Yachtmotoren)
  wird über die Lager auf das Fundament und von dort in die Rumpfstruktur
  übertragen.
- **Schwingungsisolation**: Motorbetriebsschwingungen (Zündfrequenz,
  Massenausgleich, Hilfsaggregate) werden vom Rumpf entkoppelt.
- **Ausrichtung**: Die Motor-Getriebe-Wellen-Achse muss mit der
  Stevenrohrachse auf 0,05 mm fluchten — die Motorlager ermöglichen
  die präzise Einstellung.
- **Schubübertragung**: Der Propellerschub wird über die Drucklager
  (im Getriebe integriert oder separat) und die Motorlager in den Rumpf
  eingeleitet.
- **Dynamische Entkopplung**: Seegangsbewegungen des Rumpfes dürfen
  nicht zu Verspannungen im Antriebsstrang führen.

### 1.2 Systemübersicht Antriebsstrang-Lagerung

```
Motor → Motorlager → Motorfundament → Stringerverband → Rumpf
  ↓
Getriebe → Flanschkupplung → Propellerwelle → Stevenrohr → Propeller
```

Jedes Element in dieser Kette muss korrekt dimensioniert und ausgerichtet sein.
Ein Fehler an einer Stelle wirkt sich auf die gesamte Kette aus:

| Fehler | Primäre Auswirkung | Sekundäre Folgen |
|--------|-------------------|-----------------|
| Weiches Motorlager | Motor sackt ab | Alignment verloren, Wellenvibrationen |
| Hartes Motorlager | Kein Schwingungsschutz | Rumpfvibrationen, Geräusche |
| Schlechtes Fundament | Lager kippen/rutschen | Alignment instabil, Risse |
| Fehl-Alignment | Kupplungsverschleiß | Getriebeschaden, Wellendichtung |
| Fehlende Belüftung | Überhitzung | Motorschaden, Brandgefahr |

### 1.3 Bootsklassen und typische Anforderungen

| Bootsklasse | Motorgewicht | Lagertyp | Alignment-Toleranz | Besonderheit |
|------------|-------------|---------|-------------------|-------------|
| Segelboot 7–10 m | 80–250 kg | Flex 40–55 Shore | ±0,05 mm | Enge Platzverhältnisse |
| Segelboot 10–15 m | 200–600 kg | Flex 45–60 Shore | ±0,05 mm | Saildrive oder Welle |
| Motoryacht 8–12 m | 200–500 kg | Flex 50–65 Shore | ±0,05 mm | Vibrationskomfort wichtig |
| Motoryacht 12–18 m | 400–1.200 kg | Flex 55–70 Shore | ±0,03 mm | Doppelmotorisierung |
| Motoryacht 18–24 m | 800–2.500 kg | Flex/Semi-rigid | ±0,03 mm | Hohe Leistung, Schub |
| Superyacht 24 m+ | 1.500–8.000 kg | Spezial-Systeme | ±0,02 mm | Lloyd's/DNV-Klasse |

### 1.4 Historische Entwicklung

- **1950er–1960er**: Starre Motorlagerung auf Holzfundamenten. Massive
  Vibrationsübertragung. Gummipuffer als erste Dämpfer.
- **1970er**: Einführung flexibler Motorlager (z.B. Vetus K-Serie).
  GFK-Fundamente mit eingelegten Stahlplatten.
- **1980er**: Professionelle Shore-Härte-Abstimmung. R&D Marine führt
  K-Prop-Serie ein. Laser-Alignment wird verfügbar.
- **1990er**: Poly-Flex-Systeme für hohe Lasten. Computer-gestützte
  Schwingungsberechnung. Schallschutzkapselungen werden Standard.
- **2000er**: Integrierte Lösungen (Motorlager + Schallschutz).
  Yanmar und Volvo bieten OEM-abgestimmte Lager.
- **2010er**: Aktive Vibrationsdämpfung bei Superyachten. Digitale
  Alignment-Systeme mit Bluetooth-Protokollierung.
- **2020er**: Nachhaltige Elastomere. 3D-gedruckte Montagehilfen.
  Elektromotoren erfordern neue Lagerkonzepte (weniger Vibration,
  andere Frequenzen).

---
---

## 2. Motorlager-Typen und Bauformen

### 2.1 Grundprinzipien der Schwingungsisolation

Ein Motorlager ist im Wesentlichen ein kalibriertes Elastomer-Element,
das zwischen der Motorlager-Schiene (engine foot) und dem Fundament sitzt.
Das Elastomer absorbiert Schwingungsenergie durch innere Reibung (Hysterese)
und wandelt sie in Wärme um.

**Schlüsselparameter:**

- **Statische Deflexion**: Einfederung unter Motorgewicht (mm)
- **Dynamische Steifigkeit**: Federkonstante unter Betriebsschwingungen (N/mm)
- **Shore-Härte**: Maß für die Elastomerhärte (Shore A)
- **Eigenfrequenz**: Resonanzfrequenz des Feder-Masse-Systems (Hz)
- **Isolationsgrad**: Reduktion der übertragenen Schwingung (%)
- **Druckverformungsrest**: Bleibende Verformung nach Belastung (%)

### 2.2 Zylindrische Motorlager (Standard-Typ)

Der häufigste Typ im Yachtbau. Zwei Metallplatten mit einem zylindrischen
Elastomerkörper dazwischen. Die Befestigungsbolzen gehen durch die obere
Platte (motorseits) und die untere Platte (fundamentseits).

**Merkmale:**
- Einfache Bauform, kostengünstig
- Höhenverstellung über Kontermuttern auf dem Befestigungsbolzen
- Typisch 4 Lager pro Motor (vorne links, vorne rechts, hinten links,
  hinten rechts)
- Standardgrößen: M10, M12, M16 Befestigungsbolzen

**Vorteile:**
- Einfacher Austausch
- Breite Verfügbarkeit
- Höheneinstellung für Alignment möglich

**Nachteile:**
- Begrenzte laterale Stabilität
- Keine axiale Schubaufnahme
- Setzung nach Einbau erfordert Nachjustierung

### 2.3 Konische Motorlager

Kegelförmiger Elastomerkörper, der sowohl vertikale als auch laterale
Kräfte aufnimmt. Der Konus verhindert seitliches Wandern des Motors.

**Merkmale:**
- Bessere Lateralstabilität als zylindrische Lager
- Geeignet für Hochleistungsmotoren mit hohem Drehmoment
- Typisch in Motoryachten ab 15 m
- Selbstzentrierend bei Montage

**Vorteile:**
- Verbesserte Stabilität in allen Achsen
- Geringere Verschiebung bei Schubreaktionen
- Längere Alignment-Stabilität

**Nachteile:**
- Komplexere Montage
- Höhere Kosten (ca. 40–60 % mehr als zylindrisch)
- Weniger Auswahl im Aftermarket

### 2.4 Doppelkonus-Motorlager (Sandwich-Typ)

Zwei gegenüberliegende konische Elastomerelemente in einem Gehäuse.
Bietet omnidirektionale Schwingungsisolation. Premium-Lösung für
komfortorientierte Yachten.

**Merkmale:**
- Symmetrische Isolation in Zug und Druck
- Motor kann nicht aus dem Lager „herausspringen"
- Typisch bei Custom-Yachten und Superyachten
- Aufwändige Montage mit Spezialwerkzeug

**Vorteile:**
- Beste Schwingungsisolation aller passiven Systeme
- Motor fixiert in alle Richtungen
- Kein Abheben bei Resonanz

**Nachteile:**
- Hohe Kosten (2–3× Standard)
- Aufwändiger Austausch
- Begrenzte Höhenverstellung

### 2.5 Metallgummi-Buchsen (Silentblöcke)

Zylindrische Gummibuchsen mit innerer Metallhülse. Werden in Bohrlöcher
eingepresst oder verschraubt. Typisch bei kleineren Motoren und als
sekundäre Lagerung.

**Merkmale:**
- Kompakte Bauform
- Hohe radiale Steifigkeit
- Geringe axiale Steifigkeit
- Typisch bei Innenbordmotoren bis 100 PS

**Vorteile:**
- Platzsparend
- Kostengünstig
- Einfache Integration in enge Motorräume

**Nachteile:**
- Geringe Höhenverstellbarkeit
- Schwieriges Alignment
- Begrenzte Lebensdauer in mariner Umgebung

### 2.6 Starre Motorlager (Rigid Mounts)

Metallblöcke oder Unterlegplatten ohne Elastomerelement. Der Motor ist
starr mit dem Fundament verbunden. Im modernen Yachtbau nur noch selten
verwendet.

**Anwendungsfälle:**
- Arbeitsboote, bei denen Komfort irrelevant ist
- Historische Restaurierungen
- Temporäre Montage bei Alignment-Problemen
- Testläufe ohne Elastomer

**Nachteile:**
- Massive Vibrationsübertragung (0 % Isolation)
- Beschleunigte Ermüdung der Rumpfstruktur
- Geräuschpegel unerträglich im Wohnbereich
- Getriebe-/Kupplungsverschleiß erhöht

### 2.7 Hydraulisch gedämpfte Motorlager

Elastomerkörper mit integrierter Hydraulikkammer. Die Flüssigkeit fließt
bei Schwingungen durch kalibrierte Kanäle und erzeugt zusätzliche Dämpfung.
Premium-Lösung für Superyachten.

**Merkmale:**
- Frequenzselektive Dämpfung
- Einstellbar über Ventil oder Kanalquerschnitt
- Typisch bei Motoren ab 500 PS
- Erfordert regelmäßige Inspektion der Hydraulikflüssigkeit

**Vorteile:**
- Breitbandige Schwingungsisolation
- Sehr gute Isolation bei niedrigen Frequenzen
- Einstellbar auf verschiedene Betriebszustände

**Nachteile:**
- Sehr hohe Kosten (5–10× Standard)
- Wartungsintensiv
- Leckage-Risiko der Hydraulikflüssigkeit
- Nur Spezialhersteller

### 2.8 Aktive Schwingungsisolation

Elektronisch geregelte Systeme mit Aktuatoren, die Gegenschwingungen
erzeugen. Prinzip: Sensor misst Vibration → Controller berechnet
Gegensignal → Aktuator erzeugt Gegenkraft.

**Merkmale:**
- Nur bei Superyachten (40 m+) wirtschaftlich sinnvoll
- Reduktion um 80–95 % im Frequenzbereich 5–200 Hz
- Erfordert Stromversorgung und Steuerungselektronik
- Hersteller: ARES (Anti-Resonance-Engineered-Solutions),
  Mackay Marine, Vulkan Couplings

**Vorteile:**
- Maximale Schwingungsreduktion
- Adaptiv an Betriebszustand
- Reduziert auch strukturellen Körperschall

**Nachteile:**
- Kosten 50.000–200.000 € pro Motor
- Komplexe Installation und Inbetriebnahme
- Abhängig von Elektronik und Stromversorgung
- Rückfallebene (passive Lager) erforderlich

### 2.9 Vergleichsmatrix Motorlager-Typen

| Typ | Isolation | Stabilität | Kosten | Wartung | Einsatzbereich |
|-----|----------|-----------|--------|---------|---------------|
| Zylindrisch | ★★★☆☆ | ★★☆☆☆ | € | Gering | Standard-Yachten |
| Konisch | ★★★★☆ | ★★★★☆ | €€ | Gering | Motoryachten |
| Doppelkonus | ★★★★★ | ★★★★★ | €€€ | Mittel | Custom/Superyacht |
| Silentblock | ★★☆☆☆ | ★★★☆☆ | € | Gering | Kleinmotoren |
| Starr | ☆☆☆☆☆ | ★★★★★ | € | Keine | Arbeitsboote |
| Hydraulisch | ★★★★★ | ★★★★☆ | €€€€ | Hoch | Superyacht |
| Aktiv | ★★★★★+ | ★★★★★ | €€€€€ | Hoch | Megayacht |

---
---

## 3. Hersteller und Produktlinien

### 3.1 Vetus (Niederlande)

**Unternehmenshintergrund:**
Vetus ist einer der führenden Hersteller von Marine-Zubehör mit Sitz
in Schiedam, Niederlande. Gegründet 1968. Motorlager sind ein Kernprodukt
des Sortiments. Vertrieb weltweit über Fachhändler.

**K-Serie (Standard):**

| Modell | Max. Gewicht/Lager | Shore-Härte | Bolzen | Deflexion | Einsatz |
|--------|-------------------|------------|--------|----------|---------|
| K30 | 30 kg | 45 Shore A | M10 | 3,5 mm | Hilfsaggregate |
| K50 | 50 kg | 45 Shore A | M10 | 3,8 mm | Kleine Diesel 1-Zyl |
| K75 | 75 kg | 50 Shore A | M12 | 4,0 mm | Diesel 1–2 Zyl |
| K100 | 100 kg | 55 Shore A | M12 | 4,2 mm | Diesel 2–3 Zyl |
| K130 | 130 kg | 55 Shore A | M12 | 4,5 mm | Diesel 3 Zyl |
| K160 | 160 kg | 60 Shore A | M16 | 4,8 mm | Diesel 3–4 Zyl |
| K200 | 200 kg | 60 Shore A | M16 | 5,0 mm | Diesel 4 Zyl |
| K250 | 250 kg | 60 Shore A | M16 | 5,2 mm | Diesel 4–6 Zyl |
| K300 | 300 kg | 65 Shore A | M16 | 5,5 mm | Diesel 6 Zyl |
| K400 | 400 kg | 65 Shore A | M20 | 5,8 mm | Großdiesel |
| K500 | 500 kg | 70 Shore A | M20 | 6,0 mm | Großdiesel |
| K700 | 700 kg | 70 Shore A | M24 | 6,5 mm | Schwere Diesel |

**Vetus HY-Serie (Hochleistung):**

| Modell | Max. Gewicht/Lager | Shore-Härte | Besonderheit |
|--------|-------------------|------------|-------------|
| HY200 | 200 kg | 55 Shore A | Erhöhte Lateralsteifigkeit |
| HY350 | 350 kg | 60 Shore A | Doppel-Elastomer |
| HY500 | 500 kg | 65 Shore A | Für Schnelläufer |
| HY800 | 800 kg | 70 Shore A | Für Gleiter-Motoryachten |

**Vetus Preisliste (UVP 2025/2026):**

| Modell | Einzelpreis (€) | 4er-Set (€) |
|--------|----------------|------------|
| K50 | 28 | 95 |
| K75 | 32 | 110 |
| K100 | 38 | 130 |
| K130 | 42 | 145 |
| K160 | 55 | 190 |
| K200 | 65 | 225 |
| K250 | 78 | 270 |
| K300 | 95 | 330 |
| K400 | 125 | 435 |
| K500 | 165 | 575 |
| K700 | 220 | 765 |

### 3.2 R&D Marine (UK)

**Unternehmenshintergrund:**
R&D Marine Ltd, ansässig in Fareham, Hampshire, UK. Spezialist für
marine Antriebskomponenten seit 1978. Bekannt für die K-Prop-Serie
flexibler Kupplungen und hochwertige Motorlager. Lieferant für
zahlreiche OEM-Werften (Hallberg-Rassy, Najad, Oyster, Contest).

**Flexible Motorlager-Serie:**

| Modell | Max. Gewicht/Lager | Shore-Härte | Bolzen | Besonderheit |
|--------|-------------------|------------|--------|-------------|
| RDM-50 | 50 kg | 45 Shore A | M10 | Kompakt |
| RDM-100 | 100 kg | 50 Shore A | M12 | Standard |
| RDM-150 | 150 kg | 55 Shore A | M12 | Mittelklasse |
| RDM-200 | 200 kg | 55 Shore A | M16 | Beliebt bei 30–50 PS |
| RDM-300 | 300 kg | 60 Shore A | M16 | Mittelgroße Diesel |
| RDM-450 | 450 kg | 65 Shore A | M16 | Große Segelyachten |
| RDM-600 | 600 kg | 65 Shore A | M20 | Motoryachten |
| RDM-900 | 900 kg | 70 Shore A | M20 | Schwere Diesel |
| RDM-1200 | 1.200 kg | 70 Shore A | M24 | Superyacht-Klasse |

**R&D Marine Qualitätsmerkmale:**
- Alle Lager mit Edelstahl-316L-Befestigungsbolzen (nicht nur verzinktem Stahl)
- EPDM-Elastomer mit UV-Stabilisatoren
- Salzwasserfeste Grundplatte (Edelstahl oder eloxiertes Aluminium)
- Jedes Lager einzeln geprüft und zertifiziert
- 5 Jahre Garantie auf Elastomer-Defekte

### 3.3 Yanmar Original-Motorlager

**OEM-Lager für Yanmar-Motoren:**

Yanmar liefert für jeden Motortyp werkseitig abgestimmte Motorlager.
Diese sind auf die spezifischen Schwingungseigenschaften des jeweiligen
Motors kalibriert.

| Motortyp | OEM-Lager-Nr. | Gewicht/Lager | Shore-Härte | Preis (€) |
|----------|-------------|-------------|------------|----------|
| 1GM10 | 128170-08370 | 25 kg | 45 Shore A | 45 |
| 2GM20 | 128170-08440 | 45 kg | 50 Shore A | 52 |
| 3GM30 | 128170-08450 | 55 kg | 50 Shore A | 55 |
| 3JH40 | 129670-08310 | 70 kg | 55 Shore A | 68 |
| 3JH5E | 129670-08350 | 75 kg | 55 Shore A | 72 |
| 4JH45 | 129670-08321 | 90 kg | 55 Shore A | 78 |
| 4JH57 | 129670-08330 | 100 kg | 60 Shore A | 82 |
| 4JH80 | 129670-08340 | 115 kg | 60 Shore A | 88 |
| 4JH110 | 129670-08360 | 130 kg | 60 Shore A | 95 |
| 4LHA-STP | 129670-08500 | 250 kg | 65 Shore A | 145 |
| 6LY-STP | 129670-08510 | 350 kg | 65 Shore A | 185 |

**Hinweis zu Yanmar-OEM-Lagern:**
Die Yanmar-OEM-Lager sind exakt auf die Motor-Eigenfrequenzen abgestimmt.
Der Einsatz von Aftermarket-Lagern ist möglich, jedoch muss die
Shore-Härte und Tragfähigkeit exakt passen. Yanmar empfiehlt ausschließlich
Original-Lager — die Garantie kann bei Verwendung von Fremdlagern erlöschen.

### 3.4 Volvo Penta Original-Motorlager

**OEM-Lager für Volvo Penta Motoren:**

| Motortyp | OEM-Lager-Nr. | Gewicht/Lager | Shore-Härte | Preis (€) |
|----------|-------------|-------------|------------|----------|
| D1-13 | 3809200 | 30 kg | 45 Shore A | 55 |
| D1-20 | 3809200 | 35 kg | 45 Shore A | 55 |
| D1-30 | 3809201 | 45 kg | 50 Shore A | 62 |
| D2-40 | 3809201 | 55 kg | 50 Shore A | 62 |
| D2-55 | 3809202 | 70 kg | 55 Shore A | 72 |
| D2-60 | 3809202 | 75 kg | 55 Shore A | 72 |
| D2-75 | 3809203 | 90 kg | 55 Shore A | 82 |
| D3-110 | 3809300 | 130 kg | 60 Shore A | 98 |
| D3-150 | 3809301 | 155 kg | 60 Shore A | 105 |
| D3-170 | 3809302 | 170 kg | 65 Shore A | 115 |
| D4-210 | 3809400 | 210 kg | 65 Shore A | 135 |
| D4-260 | 3809401 | 240 kg | 65 Shore A | 145 |
| D6-310 | 3809500 | 350 kg | 70 Shore A | 195 |
| D6-380 | 3809501 | 400 kg | 70 Shore A | 215 |

**Volvo Penta Besonderheiten:**
- Saildrive-Motoren (D1/D2 mit 120S/130S) haben eine andere Lagergeometrie
  als Wellenantriebe
- IPS-Antriebe (D4/D6 mit IPS) verwenden ein komplett anderes Lagersystem
  mit integrierten Pod-Lagern
- Volvo Penta bietet ein spezielles Alignment-Kit für Servicewerkstätten

### 3.5 Poly-Flex (Deutschland/Niederlande)

**Unternehmenshintergrund:**
Poly-Flex Schwingungstechnik GmbH mit Sitz in Wuppertal. Spezialist für
industrielle und marine Schwingungsisolation. Lieferant für mehrere
europäische Werften (Bavaria, Hanse, Jeanneau).

**PF-Serie (Marine):**

| Modell | Max. Gewicht/Lager | Shore-Härte | Deflexion | Besonderheit |
|--------|-------------------|------------|----------|-------------|
| PF-M50 | 50 kg | 45 Shore A | 3,5 mm | Minimal |
| PF-M100 | 100 kg | 50 Shore A | 4,0 mm | Standard |
| PF-M150 | 150 kg | 55 Shore A | 4,5 mm | Beliebt |
| PF-M200 | 200 kg | 55 Shore A | 4,8 mm | Vielseitig |
| PF-M300 | 300 kg | 60 Shore A | 5,2 mm | Mittelgroß |
| PF-M500 | 500 kg | 65 Shore A | 5,8 mm | Groß |
| PF-M750 | 750 kg | 70 Shore A | 6,2 mm | Schwer |
| PF-M1000 | 1.000 kg | 70 Shore A | 6,5 mm | Extra-schwer |

**Poly-Flex Sondermerkmale:**
- Doppel-Elastomer-Option (zwei Shore-Härten in einem Lager)
- Edelstahl-Ausführung für Salzwasser (Aufpreis 35 %)
- Kundenspezifische Sonder-Shore-Härten auf Anfrage
- Technischer Support mit Schwingungsberechnung
- Lieferzeit: Standard 2 Wochen, Sonder 4–6 Wochen

### 3.6 Weitere Hersteller

**Barry Controls / Hutchinson (Frankreich/USA):**
- Globaler Anbieter industrieller Schwingungsisolation
- Marine-Linie für Superyachten und Marineschiffe
- Produkte: Staploc, Elastomeric Isolators, Active Mounts
- Preisbereich: 150–2.000 € pro Lager

**Trelleborg (Schweden):**
- Marine-Elastomer-Spezialist
- Produkte: Metalastik-Serie für Großdiesel
- Typisch bei Motoren ab 200 kW
- Zertifiziert nach Lloyd's, DNV, BV

**GMT (Gruppo Mescole Tecnopolimeri, Italien):**
- Italienischer Hersteller von Gummi-Metall-Elementen
- Marine-Serie für italienische Werften (Azimut, Ferretti, Sanlorenzo)
- Preisbereich: 80–600 € pro Lager

**Vulkan (Deutschland):**
- Vulkan Kupplungs- und Getriebebau, Herne
- Spezialist für flexible Kupplungen und Schwingungsisolation
- Marine-Motorlager für den professionellen Bereich
- Erfordert werksseitige Schwingungsanalyse

**Soundown (USA):**
- Spezialist für marine Schall- und Vibrationskontrolle
- Motorlager, Schallisolierung und Vibrationsdämpfer als Gesamtsystem
- Beliebt im US-Markt

**Allpa Marine (Niederlande):**
- Aftermarket-Lieferant
- Kompatible Lager zu Vetus, Volvo, Yanmar
- Preislich 20–40 % unter OEM
- Qualität: ausreichend für Freizeityachten

### 3.7 Cross-Referenz: Motor → Empfohlenes Lager

| Motor | OEM-Lager | Vetus-Äquivalent | R&D Marine | Poly-Flex |
|-------|----------|-----------------|-----------|----------|
| Yanmar 1GM10 | 128170-08370 | K50 | RDM-50 | PF-M50 |
| Yanmar 3JH40 | 129670-08310 | K130 | RDM-150 | PF-M150 |
| Yanmar 4JH57 | 129670-08330 | K200 | RDM-200 | PF-M200 |
| Yanmar 4JH80 | 129670-08340 | K250 | RDM-300 | PF-M300 |
| Volvo D1-30 | 3809201 | K75 | RDM-100 | PF-M100 |
| Volvo D2-55 | 3809202 | K130 | RDM-150 | PF-M150 |
| Volvo D2-75 | 3809203 | K160 | RDM-200 | PF-M200 |
| Volvo D3-110 | 3809300 | K250 | RDM-300 | PF-M300 |
| Volvo D4-260 | 3809401 | K400 | RDM-600 | PF-M500 |
| Beta 25 | — | K100 | RDM-100 | PF-M100 |
| Beta 43 | — | K160 | RDM-200 | PF-M200 |
| Nanni N4.65 | — | K200 | RDM-200 | PF-M200 |
| Nanni N4.100 | — | K300 | RDM-300 | PF-M300 |

---
---

## 4. Motorlager-Dimensionierung

### 4.1 Grundlagen der Lager-Berechnung

Die korrekte Dimensionierung eines Motorlagers erfordert die Kenntnis
von Motorgewicht, Schwerpunktlage, Betriebsdrehzahlen und der gewünschten
Isolationseffizienz.

**Schritt 1: Motorgewicht bestimmen**

Das Gesamtgewicht umfasst:
- Trockengewicht des Motors (laut Datenblatt)
- Getriebegewicht (sofern angebaut)
- Gewicht der Anbauteile (Lichtmaschine, Kompressor, Wärmetauscher,
  Auspuffkrümmer, Frischluftfilter)
- Betriebsmittel (Öl, Kühlmittel) — ca. 5–10 % des Trockengewichts
- Zusatzgewicht: Schallschutzkapsel, wenn vorhanden

**Rechenbeispiel:**
```
Yanmar 4JH57:
  Trockengewicht Motor:     218 kg
  Getriebe KM4A:             32 kg
  Anbauteile:                18 kg
  Betriebsmittel:            15 kg
  Schallschutzkapsel:        12 kg
  ─────────────────────────────
  Gesamtgewicht:            295 kg
```

**Schritt 2: Gewicht pro Lager berechnen**

Bei 4 Lagern und annähernd symmetrischer Schwerpunktlage:
```
Gewicht pro Lager = Gesamtgewicht / 4 = 295 / 4 = 73,75 kg
```

**Wichtig:** Der Motorschwerpunkt liegt nicht exakt mittig. Typisch liegt
er 55–60 % der Motorlänge von der Getriebeseite entfernt. Die vorderen
Lager tragen daher mehr Last als die hinteren.

**Korrekte Berechnung mit Schwerpunktlage:**
```
Annahmen:
  Lagerabstand längs (L):    580 mm
  Schwerpunkt ab Hinterachse: 320 mm (55 % von 580)

  Last hintere Lager (2×): (580 - 320) / 580 × 295 = 132,2 kg → 66,1 kg/Lager
  Last vordere Lager (2×): 320 / 580 × 295 = 162,8 kg → 81,4 kg/Lager
```

**Schritt 3: Sicherheitsfaktor anwenden**

Empfohlener Sicherheitsfaktor: 1,3–1,5 für Yachten, 1,5–2,0 für
Arbeitsboote und raue See.

```
Max. Lagerbelastung = 81,4 kg × 1,5 = 122,1 kg → Auswahl: Vetus K130
```

### 4.2 Eigenfrequenz-Berechnung

Die Eigenfrequenz (Resonanzfrequenz) des Motor-Lager-Systems muss deutlich
unter der niedrigsten Erregerfrequenz des Motors liegen, um effektive
Isolation zu gewährleisten.

**Erregerfrequenz berechnen:**
```
f_err = (Drehzahl × Zylinderzahl) / (2 × 60)  [für Viertakt]

Beispiel Yanmar 4JH57 bei Leerlauf (800 U/min):
  f_err = (800 × 4) / (2 × 60) = 26,7 Hz

Beispiel Yanmar 4JH57 bei Nenndrehzahl (3.200 U/min):
  f_err = (3.200 × 4) / (2 × 60) = 106,7 Hz
```

**Eigenfrequenz des Lagers:**
```
f_n = (1 / 2π) × √(k / m)

wobei:
  k = Federsteifigkeit des Lagers (N/mm)
  m = Masse pro Lager (kg)

Typisch für Vetus K130:
  k ≈ 1.200 N/mm
  m = 75 kg
  f_n = (1 / 6,283) × √(1.200.000 / 75) = (1 / 6,283) × 126,5 = 20,1 Hz
```

**Isolationsregel:**
- Verhältnis f_err / f_n > 1,4: Isolation beginnt
- Verhältnis f_err / f_n > 2,0: gute Isolation (~75 %)
- Verhältnis f_err / f_n > 3,0: sehr gute Isolation (~90 %)
- Verhältnis f_err / f_n > 4,0: exzellente Isolation (~95 %)

Im Beispiel bei Leerlauf: 26,7 / 20,1 = 1,33 — **grenzwertig!**
Dies erklärt, warum viele Motoren im Leerlauf stärker vibrieren als
bei höheren Drehzahlen.

### 4.3 Statische Deflexion und Setzverhalten

Nach der Erstmontage setzt sich jedes Elastomerlager. Die anfängliche
Deflexion vergrößert sich in den ersten 100–200 Betriebsstunden um
typisch 10–15 %.

**Typische Deflexionswerte nach Einlaufphase:**

| Shore-Härte | Anfangsdeflexion | Nach 200 h | Nach 1.000 h | Nach 5.000 h |
|------------|-----------------|-----------|-------------|-------------|
| 45 Shore A | 4,0 mm | 4,5 mm | 4,6 mm | 4,8 mm |
| 50 Shore A | 3,5 mm | 3,9 mm | 4,0 mm | 4,2 mm |
| 55 Shore A | 3,0 mm | 3,4 mm | 3,5 mm | 3,6 mm |
| 60 Shore A | 2,5 mm | 2,8 mm | 2,9 mm | 3,0 mm |
| 65 Shore A | 2,0 mm | 2,2 mm | 2,3 mm | 2,4 mm |
| 70 Shore A | 1,5 mm | 1,7 mm | 1,7 mm | 1,8 mm |

**Praxisregel:** Nach der Erstinstallation eines Motors das Alignment
nach 50 Betriebsstunden, nach 200 Betriebsstunden und dann alle
500 Betriebsstunden oder jährlich prüfen.

### 4.4 Dynamische Belastung durch Propellerschub

Zusätzlich zum statischen Motorgewicht müssen die Lager den Propellerschub
aufnehmen (sofern kein separates Drucklager vorhanden).

**Propellerschub-Abschätzung:**
```
F_schub ≈ P / (v × η_p)

wobei:
  P = Motorleistung (W)
  v = Bootsgeschwindigkeit (m/s)
  η_p = Propellerwirkungsgrad (0,4–0,6)

Beispiel: 57 PS = 42 kW, 7 kn = 3,6 m/s, η_p = 0,5
  F_schub ≈ 42.000 / (3,6 × 0,5) = 23.333 N ≈ 2.380 kg

Dieser Schub wird über 4 Lager verteilt: 595 kg pro Lager (axial)
```

**Wichtig:** Die meisten Getriebe haben ein integriertes Drucklager,
das den Großteil des Propellerschubs aufnimmt, bevor er in die Motorlager
gelangt. Dennoch wirkt eine axiale Restkomponente auf die Motorlager.

### 4.5 Dimensionierungs-Entscheidungsbaum

```
Motorgewicht bestimmen (inkl. Getriebe, Anbauteile, Betriebsmittel)
    ↓
Schwerpunktlage ermitteln (ab Getriebeseite: typisch 55–60 %)
    ↓
Last pro Lager berechnen (mit Schwerpunktverteilung)
    ↓
Sicherheitsfaktor anwenden (1,3 Küstenfahrt, 1,5 Seefahrt, 2,0 Arbeitsboot)
    ↓
Lagergröße wählen (nächsthöhere verfügbare Tragfähigkeit)
    ↓
Eigenfrequenz prüfen (f_n < 0,5 × f_err bei Leerlauf)
    ↓
Shore-Härte bewerten:
  - Komfort-Priorität: weichere Lager (45–55 Shore A)
  - Alignment-Stabilität: härtere Lager (55–65 Shore A)
  - Leistung/Schub: härteste Lager (65–70 Shore A)
    ↓
Lager bestellen, einbauen, Alignment prüfen, nach 50 h nachprüfen
```

---
---

## 5. Shore-Härte, Deflexion und Schwingungsverhalten

### 5.1 Shore-Härte-Skala im Kontext Motorlager

Die Shore-A-Härte ist das wichtigste Auswahlkriterium für marine
Motorlager. Sie bestimmt sowohl die Schwingungsisolation als auch
die Alignment-Stabilität.

**Shore-A-Werte für marine Motorlager:**

| Shore A | Charakteristik | Typischer Einsatz | Isolation | Stabilität |
|---------|---------------|------------------|----------|-----------|
| 35–40 | Sehr weich | Generatoren, Hilfsaggregate | Exzellent | Gering |
| 40–45 | Weich | Kleindiesel, Segelboote | Sehr gut | Mäßig |
| 45–50 | Mittelweich | Standard-Segelbootdiesel | Gut | Gut |
| 50–55 | Mittel | Allround, beliebtester Bereich | Gut | Gut |
| 55–60 | Mittelfest | Motoryachten, Saildrive | Mäßig | Sehr gut |
| 60–65 | Fest | Große Diesel, Gleiter | Mäßig | Sehr gut |
| 65–70 | Sehr fest | Hochleistungsmotoren | Ausreichend | Exzellent |
| 70–75 | Hart | Arbeitsboote, starrer Antrieb | Gering | Exzellent |

### 5.2 Deflexionsmessung in der Praxis

Die Deflexion (Einfederung) eines Motorlagers wird gemessen als
vertikale Verformung unter statischer Last. Sie ist der wichtigste
Indikator für den Zustand eines Lagers.

**Messmethode:**
1. Motor abstellen und abkühlen lassen
2. Referenzmaß zwischen Motoroberkante und festem Punkt am Rumpf messen
3. Motor anheben (Flaschenzug oder Hydraulikpresse)
4. Entlastetes Maß messen
5. Differenz = aktuelle Deflexion

**Zustandsbewertung:**

| Deflexion vs. Neuzustand | Zustand | Maßnahme |
|--------------------------|---------|----------|
| 0–10 % mehr | Neuwertig | Keine |
| 10–20 % mehr | Normal eingelaufen | Alignment prüfen |
| 20–35 % mehr | Gealtert | Alignment nachjustieren, Austausch planen |
| 35–50 % mehr | Verschlissen | Austausch dringend empfohlen |
| > 50 % mehr | Defekt | Sofortiger Austausch |
| Lager rissig/gebrochen | Ausgefallen | Motor nicht betreiben |

### 5.3 Schwingungsspektrum und Erregerfrequenzen

Marine-Dieselmotoren erzeugen ein komplexes Schwingungsspektrum:

**Primäre Erreger:**
- **1. Ordnung**: Drehzahl / 60 Hz — Unwucht, Schwungscheibe
- **Zündfrequenz**: (Drehzahl × Zylinderzahl) / (2 × 60) Hz —
  Verbrennungsdruck
- **2. Ordnung**: 2 × Drehzahl / 60 Hz — Kolbenmassenkräfte

**Sekundäre Erreger:**
- Ventiltrieb: diverse Harmonische
- Einspritzpumpe: (Drehzahl × Zylinder) / (2 × 60) Hz
- Lichtmaschine: 2–3× Drehzahl über Riementrieb
- Kühlwasserpumpe: Drehzahl × Flügelzahl
- Turbolader: 10.000–100.000 U/min → 167–1.667 Hz

**Typische Frequenzen für Yachtmotoren:**

| Motor | Leerlauf (Hz) | Reisedrehzahl (Hz) | Nenndrehzahl (Hz) |
|-------|--------------|-------------------|------------------|
| 1-Zyl 3.600 U/min | 10 Hz | 22 Hz | 30 Hz |
| 2-Zyl 3.600 U/min | 13 Hz | 30 Hz | 60 Hz |
| 3-Zyl 3.000 U/min | 15 Hz | 30 Hz | 75 Hz |
| 4-Zyl 3.200 U/min | 27 Hz | 75 Hz | 107 Hz |
| 6-Zyl 3.200 U/min | 40 Hz | 110 Hz | 160 Hz |

### 5.4 Isolationsgrad-Berechnung

Der Isolationsgrad beschreibt, wie viel Prozent der Schwingungsenergie
das Motorlager absorbiert.

```
Transmissibilität T = 1 / |1 - (f/f_n)²|

Isolationsgrad I = (1 - T) × 100 %
```

**Praxisbeispiel: 4-Zylinder bei verschiedenen Drehzahlen:**

| Drehzahl | f_err (Hz) | f_n (Hz) | f/f_n | T | Isolation |
|----------|----------|---------|------|---|----------|
| 800 (Leerlauf) | 26,7 | 20 | 1,33 | 1,27 | −27 % (Verstärkung!) |
| 1.000 | 33,3 | 20 | 1,67 | 0,56 | 44 % |
| 1.500 | 50,0 | 20 | 2,50 | 0,19 | 81 % |
| 2.000 | 66,7 | 20 | 3,33 | 0,10 | 90 % |
| 2.500 | 83,3 | 20 | 4,17 | 0,06 | 94 % |
| 3.200 | 106,7 | 20 | 5,33 | 0,04 | 96 % |

**Erkenntnis:** Bei Leerlauf (f/f_n = 1,33) tritt Resonanzverstärkung
auf — der Motor vibriert stärker als ohne Lager! Dies ist ein
physikalisches Grundprinzip und kein Defekt. Abhilfe: weichere Lager
(niedrigeres f_n) oder schnelleres Hochdrehen nach dem Start.

### 5.5 Temperatureinfluss auf Shore-Härte

Die Elastomersteifigkeit hängt stark von der Temperatur ab:

| Temperatur | Shore-Härte-Änderung | Auswirkung |
|-----------|---------------------|-----------|
| −20 °C | +15–20 Shore A | Lager steif wie Hartgummi |
| −10 °C | +10–15 Shore A | Deutlich härter |
| 0 °C | +5–8 Shore A | Merklich härter |
| +10 °C | +2–3 Shore A | Leicht härter |
| +20 °C | Referenzwert | Nennwert |
| +40 °C | −2–3 Shore A | Leicht weicher |
| +60 °C | −5–8 Shore A | Merklich weicher |
| +80 °C | −8–12 Shore A | Deutlich weicher, Grenzbereich |

**Praxis-Auswirkung:** In skandinavischen Gewässern mit Wassertemperaturen
nahe 0 °C und Motorräumen um 5 °C kann ein 50 Shore A Lager effektiv
58 Shore A haben — es vibriert mehr als erwartet. Umgekehrt werden
Lager in tropischen Gewässern bei 60 °C Motorraumtemperatur weicher.

---
---

## 6. Motorfundament — Konstruktion und Materialien

### 6.1 Funktionale Anforderungen

Das Motorfundament (Engine Bed) ist die strukturelle Verbindung zwischen
den Motorlagern und dem Rumpf. Es muss:

- Das Motorgewicht statisch und dynamisch tragen
- Die Lagerkräfte gleichmäßig in den Rumpf einleiten
- Formstabil bleiben (kein Verziehen, Biegen, Schwingen)
- Korrosionsbeständig sein (Bilgenwasser, Salzluft, Öl, Diesel)
- Präzise Auflageflächen für die Motorlager bieten
- Den Propellerschub in den Rumpf einleiten

### 6.2 GFK-Laminat-Fundamente

Die häufigste Bauform bei modernen GFK-Yachten. Die Motorstringer sind
integraler Bestandteil der Rumpfkonstruktion.

**Aufbau eines hochwertigen GFK-Motorfundaments:**

```
Schicht 1: Rumpf-Innenlaminat (Basis)
Schicht 2: Schaumkern oder Holzkern (Formgebung)
Schicht 3: GFK-Überlaminat (6–12 Lagen Roving + Matte, 8–15 mm)
Schicht 4: Eingelegte Stahlplatte oder Gewindebuchsen (Lagerbefestigung)
Schicht 5: Abschluss-Laminat (Versiegelung der Stahleinlage)
Schicht 6: Topcoat oder Bilgenfarbe (Schutz)
```

**Qualitätsmerkmale (gutes Fundament):**
- Stringer durchgehend vom Bug bis Achterschiff, nicht nur im Motorbereich
- Verbreiterung im Motorbereich auf mindestens 150 mm Oberkante
- Stahlplatten mindestens 10 mm dick, Edelstahl 316L oder verzinkter Stahl
- Laminat faltenfrei, ohne Lufteinschlüsse
- Oberfläche plan (Toleranz < 0,5 mm über Lagerlänge)
- Bilgenfarbe vollständig, keine blanken GFK-Flächen

**Qualitätsmerkmale (schlechtes Fundament):**
- Kurze Stringer, die nur unter dem Motor enden
- Dünnes Laminat (< 6 mm) mit sichtbaren Fasern
- Eingesetzte Sperrholzklötze statt Stahlplatten
- Risse an den Übergängen Stringer → Rumpf
- Öl- und Diesel-getränktes Laminat (osmotische Schäden)
- Lose oder korrodierte Einlegeteile

### 6.3 Stahl-Stringer-Fundamente

Bei Stahlyachten oder als Nachrüstung in GFK-Rümpfen. U-Profile oder
L-Profile, die auf den Rumpf geschweißt oder laminiert werden.

**Typische Profile:**

| Bootsklasse | Profilform | Abmessungen | Material |
|------------|----------|-----------|---------|
| Segelboot 8–12 m | U-Profil | 80×40×5 mm | V2A (1.4301) |
| Segelboot 12–16 m | U-Profil | 100×50×6 mm | V4A (1.4404) |
| Motoryacht 10–15 m | U-Profil | 100×60×6 mm | V4A (1.4404) |
| Motoryacht 15–20 m | I-Profil | 120×60×8 mm | V4A (1.4404) |
| Motoryacht 20–25 m | I-Profil | 150×80×10 mm | V4A (1.4404) |

**Befestigung am GFK-Rumpf:**
1. Flansch am Profilunterkante anschweißen (mindestens 100 mm breit)
2. Rumpf-Innenseite anschleifen (80er Korn)
3. Epoxid-Grundierung auftragen
4. Flansch mit Sikaflex 292i oder Plexus MA420 verkleben
5. Mindestens 4 Lagen Biax-Gelege über den Flansch laminieren
6. Bolzensicherung zusätzlich: M10 Edelstahl durch Rumpf (alle 200 mm)

**Vorteile:**
- Extrem steif und formstabil
- Motorlager-Schrauben direkt in Stahl
- Einfaches Alignment durch Planfräsen/Planschleifen
- Langlebig bei richtiger Oberflächenbehandlung

**Nachteile:**
- Korrosionsrisiko bei Kontakt GFK ↔ Stahl (galvanische Korrosion)
- Höheres Gewicht als reines GFK-Fundament
- Schwingungsbrücke zum Rumpf (verschlechtert Isolation)
- Aufwändige Nachrüstung

### 6.4 Aluminium-Fundamente

Bei Aluminiumyachten Standard, bei GFK-Yachten als hochwertige Option.

**Materialwahl:**
- AlMg4,5Mn (5083): Standardlegierung für marine Anwendungen
- AlMg3 (5754): günstiger, etwas geringere Festigkeit
- NICHT: AlCuMg (2024) oder AlZnMg (7075) — korrosionsanfällig in Salzwasser

**Typische Konstruktion:**
- Geschweißte Profilkonstruktion mit integrierten Auflageplatten
- Eloxierung (hart-anodisiert) oder Zweikomponenten-Grundierung
- Isolierschicht zwischen Aluminium und GFK (Sealux oder Teroson)
- Befestigung mit Edelstahl-Bolzen und Isolierbuchsen

**Vorteile:**
- Leicht (ca. 35 % weniger als Stahl bei gleicher Steifigkeit)
- Keine Korrosion bei richtiger Legierung und Beschichtung
- Gute Zerspanbarkeit (Planfräsen der Auflageflächen)
- Gute Wärmeableitung

**Nachteile:**
- Galvanische Korrosion bei Kontakt mit unedleren Metallen
- Schweißnahtqualität kritisch
- Teurer als Stahl-Standardprofile
- Empfindlich gegen Säuren (Bilgenwasser-pH prüfen)

### 6.5 Hartholz-Fundamente

Traditionelle Bauweise, heute noch bei Holzyachten und älteren GFK-Booten
anzutreffen. Auch als Shim-Material (Unterlage) bei der Alignment-
Feinjustierung verwendet.

**Geeignete Holzarten:**

| Holzart | Druckfestigkeit | Feuchteresistenz | Eignung |
|---------|----------------|-----------------|---------|
| Eiche | 52 N/mm² | Gut | Traditionell, bewährt |
| Iroko | 46 N/mm² | Sehr gut | Beste Alternative zu Teak |
| Teak | 55 N/mm² | Exzellent | Premium, teuer |
| Azobe | 105 N/mm² | Exzellent | Schwer zu bearbeiten |
| Mahagoni | 38 N/mm² | Mäßig | Nur mit Epoxid-Versiegelung |
| Multiplex (marine) | 35 N/mm² | Gut (BS 1088) | Für Shims/Unterlagen |

**Konstruktionsregeln für Holzfundamente:**
- Mindestquerschnitt: 60×60 mm (Segelboot), 80×80 mm (Motoryacht)
- Epoxid-versiegelt (alle 6 Seiten, 3× Anstrich)
- Bolzenlöcher mit Epoxid ausgegossen
- Keine Hirnholz-Kontaktflächen (Wasser-Dochtwirkung)
- Mindestens 300 mm über Bilgenwasserspiegel
- Regelmäßige Inspektion auf Fäulnis und Bewegung

### 6.6 Fundamentkonstruktion bei Saildrive-Motoren

Saildrive-Motoren (Volvo 120S/130S, Yanmar SD-Serie) haben eine
grundlegend andere Einbausituation. Der Motor hängt über dem
Saildrive-Durchbruch im Rumpfboden.

**Besonderheiten:**
- Motor sitzt auf einem Rahmen über der Saildrive-Öffnung
- Rahmen muss den Motor tragen UND den Saildrive gegen Herausdrücken
  sichern (Wasserdruck von außen)
- Saildrive-Dichtung (Gummimanschette) muss spannungsfrei sein
- Kein Alignment im klassischen Sinne (Saildrive ist starr mit Motor
  verbunden)
- Motorlager dämpfen nur Schwingungen, keine Schubkräfte

**Typischer Aufbau:**
```
Motor mit integriertem Saildrive
    ↓
4× Motorlager (typisch weicher, 40–50 Shore A)
    ↓
Stahlrahmen oder GFK-Rahmen (über Saildrive-Öffnung)
    ↓
Rumpflaminat mit Verstärkung um Durchbruch
```

### 6.7 Qualitätsbewertung Motorfundament — AYDI-Kriterien

| Kriterium | 0–20 Punkte | 21–50 Punkte | 51–80 Punkte | 81–100 Punkte |
|-----------|------------|-------------|-------------|--------------|
| Materialstärke | < 5 mm Laminat | 5–8 mm | 8–12 mm | > 12 mm oder Stahl |
| Oberfläche | Risse, Delamination | Wellen, uneben | Plan ±1 mm | Plan ±0,3 mm |
| Lagerbefestigung | Lose, korrodiert | Holzklötze | Stahlplatten | Edelstahlplatten |
| Stringeranbindung | Abgelöst | Nur Laminat, dünn | Laminat 6+ Lagen | Laminat + Bolzen |
| Korrosionsschutz | Keiner | Teilweise | Vollständig | Premium-System |
| Zugänglichkeit | Nicht erreichbar | Schwer, Demontage | Gut, Inspektionsluke | Exzellent, alle Seiten |

---
---

## 7. Motor-Alignment — Ausrichtung der Antriebsanlage

### 7.1 Warum Alignment kritisch ist

Die Ausrichtung (Alignment) der Motor-Getriebe-Wellen-Achse mit der
Stevenrohr-Achse ist der wichtigste Faktor für die Lebensdauer des
gesamten Antriebsstrangs. Fehl-Alignment von nur 0,1 mm verursacht:

- Kupplungsverschleiß (Lebensdauer halbiert)
- Getriebe-Lagerverschleiß
- Wellendichtungs-Leckage (Stopfbuchse oder Lippendichtung)
- Vibration des gesamten Antriebsstrangs
- Erhöhten Kraftstoffverbrauch (2–5 %)
- Geräuschentwicklung im Rumpf

**Alignment-Toleranzen:**

| Bootsklasse | Radiale Toleranz | Axiale Toleranz | Winkeltoleranz |
|------------|-----------------|----------------|---------------|
| Segelboot bis 12 m | ±0,05 mm | ±0,10 mm | ±0,05 mm/100 mm |
| Segelboot 12–18 m | ±0,05 mm | ±0,08 mm | ±0,04 mm/100 mm |
| Motoryacht bis 15 m | ±0,05 mm | ±0,08 mm | ±0,04 mm/100 mm |
| Motoryacht 15–24 m | ±0,03 mm | ±0,05 mm | ±0,03 mm/100 mm |
| Superyacht 24 m+ | ±0,02 mm | ±0,03 mm | ±0,02 mm/100 mm |

### 7.2 Alignment-Geometrie

Das Alignment beschreibt die Lage zweier Flansche zueinander:

**Radiales Alignment (Offset/Versatz):**
- Parallele Verschiebung der Achsen
- Gemessen als Abstand der Achsmittelpunkte
- Verursacht durch falsche Motorhöhe oder seitliche Verschiebung

**Axiales Alignment (Gap):**
- Abstand zwischen den Flanschflächen
- Muss gleichmäßig am gesamten Umfang sein
- Verursacht durch Motor-Längsverschiebung

**Winkel-Alignment (Angular):**
- Neigung der Achsen zueinander
- Gemessen als Flanschabstand-Differenz oben/unten bzw. links/rechts
- Verursacht durch ungleichmäßige Lagerhöhen

### 7.3 Messmethode 1: Fühlerblatt-Methode (Straight-Edge)

Die einfachste und am häufigsten verwendete Methode. Erfordert nur ein
Stahllineal (Straight-Edge) und Fühlerlehren.

**Werkzeug:**
- Stahllineal (Haarlineal), 300–500 mm, Genauigkeit 0,02 mm/m
- Fühlerlehren-Set 0,02–1,0 mm
- Permanentmarker
- Taschenlampe

**Durchführung:**

1. **Kupplung trennen:** Flanschschrauben lösen, Flansche ca. 5 mm
   auseinanderziehen.

2. **Referenzpunkte markieren:** 4 Punkte am Flanschumfang markieren:
   12 Uhr (oben), 3 Uhr (steuerbord), 6 Uhr (unten), 9 Uhr (backbord).

3. **Radiales Alignment messen:**
   - Stahllineal über beide Flansche legen (an 12 Uhr)
   - Fühlerlehre in den Spalt zwischen Lineal und jedem Flansch schieben
   - Differenz = radialer Versatz an dieser Stelle
   - An allen 4 Positionen wiederholen

4. **Axiales/Winkel-Alignment messen:**
   - Fühlerlehre zwischen die Flanschflächen schieben (an 12 Uhr)
   - Spaltmaß notieren
   - An allen 4 Positionen wiederholen
   - Differenz 12 Uhr vs. 6 Uhr = vertikaler Winkel
   - Differenz 3 Uhr vs. 9 Uhr = horizontaler Winkel

5. **Welle drehen und wiederholen:**
   - Propellerwelle um 90° drehen
   - Alle Messungen wiederholen
   - Unterschiede deuten auf Wellenschlag oder Flanschunrundheit hin

**Genauigkeit:** ±0,03 mm bei sorgfältiger Durchführung.

### 7.4 Messmethode 2: Messuhr-Methode (Dial Indicator)

Die präziseste klassische Methode. Standard bei professionellen
Alignment-Arbeiten.

**Werkzeug:**
- Messuhr (Dial Indicator), Auflösung 0,01 mm, Hub 10 mm
- Messuhr-Halter (Magnetfuß oder Klemme an Getriebeflansch)
- Messuhrverlängerungen (Tastspitzen)
- Drehvorrichtung für Propellerwelle

**Durchführung:**

1. **Messuhr montieren:**
   - Magnetfuß auf Getriebe-Flansch befestigen
   - Messuhr-Taster auf Propellerwellen-Flansch richten
   - Sicherstellen, dass Messuhr bei Drehung nicht anschlägt

2. **Radiales Alignment (Face Reading):**
   - Messuhr auf Flanschfläche (face) ausrichten
   - Nullen bei 12 Uhr
   - Propellerwelle langsam drehen: 3 Uhr → 6 Uhr → 9 Uhr → 12 Uhr
   - Werte notieren (TIR = Total Indicated Runout)
   - TIR / 2 = tatsächlicher Winkelversatz

3. **Radiales Alignment (Rim Reading):**
   - Messuhr auf Flanschaußendurchmesser (rim) umsetzen
   - Nullen bei 12 Uhr
   - Propellerwelle drehen, Werte notieren
   - TIR / 2 = tatsächlicher radialer Versatz

4. **Ergebnis-Interpretation:**

   ```
   Messwerte Rim (Beispiel):
     12 Uhr: 0,00 mm (Referenz)
      3 Uhr: +0,04 mm
      6 Uhr: +0,12 mm
      9 Uhr: +0,06 mm

   Radialer Versatz vertikal: (0,12 - 0,00) / 2 = 0,06 mm → Motor 0,06 mm zu tief
   Radialer Versatz horizontal: (0,06 - 0,04) / 2 = 0,01 mm → akzeptabel
   ```

5. **Korrektur durchführen:**
   - Motor über Lagerhöhenverstellung anheben/senken
   - Laterale Verschiebung durch seitliches Verstellen der Lagerbolzen
   - Nach jeder Korrektur erneut messen
   - Prozess iterativ wiederholen bis Toleranz erreicht

**Genauigkeit:** ±0,01 mm.

### 7.5 Messmethode 3: Laser-Alignment

Die modernste und schnellste Methode. Verwendet Laserstrahl und
Positionsdetektoren (PSD).

**Systeme:**
- Fixturlaser Shaft Series (Schweden): ~3.000–8.000 €
- Easy-Laser XT660 (Schweden): ~5.000–12.000 €
- Prüftechnik Optalign (Deutschland): ~4.000–10.000 €
- SKF TKSA Series (Schweden): ~2.000–6.000 €

**Vorteile gegenüber Messuhr:**
- Schneller (15–30 Minuten vs. 60–120 Minuten)
- Anzeige der erforderlichen Korrektur in Echtzeit
- Kompensation von thermischer Dehnung
- Bluetooth-Datenübertragung, Protokoll-Erstellung
- Kein Wellen-Drehen um volle 360° erforderlich (3 Punkte genügen)

**Nachteile:**
- Hohe Anschaffungskosten
- Empfindlich gegen Feuchtigkeit und Vibrationen
- Erfordert Schulung
- Batteriebetrieb, begrenzte Einsatzdauer

**Genauigkeit:** ±0,005 mm.

### 7.6 Messmethode 4: String-Methode (Provisorisch)

Die einfachste Methode für grobe Ausrichtung und Vorjustierung.
Nicht für Endkontrolle geeignet.

**Durchführung:**
1. Dünne Schnur (Maurerschnur 0,5 mm) durch Stevenrohr spannen
2. Schnur an Bug-Querschott befestigen und straff spannen
3. Motor grob nach Schnurverlauf ausrichten
4. Höhe und Seite der Wellenachse annähern
5. Anschließend Feinjustierung mit Messuhr oder Laser

**Genauigkeit:** ±1–2 mm — nur für Vorjustierung!

### 7.7 Alignment-Protokoll

Jede Alignment-Messung sollte dokumentiert werden:

```
═══════════════════════════════════════════════
MOTOR-ALIGNMENT PROTOKOLL
═══════════════════════════════════════════════
Datum: _______________
Boot: _______________  LüA: _____ m
Motor: _______________  SN: _______________
Getriebe: _______________  SN: _______________
Welle: ø ___ mm  Länge: ___ mm
Messmethode: □ Fühlerblatt  □ Messuhr  □ Laser
Messinstrument: _______________
Prüfer: _______________

RADIAL (Rim) — TIR:
  12 Uhr: _____ mm
   3 Uhr: _____ mm
   6 Uhr: _____ mm
   9 Uhr: _____ mm
  TIR: _____ mm  Versatz: _____ mm

AXIAL (Face) — TIR:
  12 Uhr: _____ mm
   3 Uhr: _____ mm
   6 Uhr: _____ mm
   9 Uhr: _____ mm
  TIR: _____ mm  Winkel: _____ mm/100mm

BEWERTUNG:
  □ Innerhalb Toleranz (±0,05 mm)
  □ Grenzwertig (±0,08 mm)
  □ Außerhalb Toleranz — Korrektur erforderlich
  □ Korrektur durchgeführt — Nachprüfung OK

ANMERKUNGEN:
_______________________________________________
═══════════════════════════════════════════════
```

### 7.8 Alignment-Einflussfaktoren

Mehrere Faktoren verändern das Alignment nach der Ersteinstellung:

| Faktor | Einfluss | Größenordnung | Gegenmaßnahme |
|--------|---------|--------------|--------------|
| Motorlager-Setzung | Motor sackt ab | 0,5–2,0 mm | Nachjustierung nach 50 h |
| Thermische Dehnung | Motor wächst bei Betrieb | 0,1–0,5 mm | Warm-Alignment oder Kompensation |
| Rumpfverformung (Kran) | Rumpf biegt durch am Kran | 0,5–5,0 mm | Alignment nur im Wasser |
| Beladung | Rumpfbiegung ändert sich | 0,2–1,0 mm | Alignment bei Reisebeladung |
| Saison-Effekte | Quellen/Schwinden Holzrumpf | 0,5–3,0 mm | Halbjährliche Prüfung |
| Grundberührung | Plötzliche Verformung | Undefiniert | Sofortige Prüfung |
| Antifouling-Arbeiten | Rumpf auf Kiel/Böcken | 1–5 mm | Alignment nach Ablassen prüfen |

### 7.9 Alignment-Prüfintervalle

| Situation | Prüfintervall |
|-----------|--------------|
| Neuer Motor / Repowering | Nach 25 h, 50 h, 200 h, dann jährlich |
| Neue Motorlager | Nach 50 h, 200 h, dann jährlich |
| Saisonale Wartung | Jährlich vor Saisonstart |
| Nach Grundberührung | Sofort |
| Nach Rumpfarbeiten am Kran | Vor Saisonstart |
| Vibration oder Geräusche | Sofort |
| Kupplungsverschleiß festgestellt | Sofort |
| Wellendichtung leckt verstärkt | Nach Ausschluss anderer Ursachen |

---
---

## 8. Schallschutz und Vibrationsdämpfung

### 8.1 Grundlagen der Schallübertragung

Schall vom Motor erreicht den Wohnbereich auf drei Wegen:

1. **Luftschall**: Motorgeräusch → Luft → Wände/Schotten → Wohnbereich
   - Abhilfe: Schallschutzkapselung, Schalldämmung der Wände
2. **Körperschall**: Motorvibrationen → Motorlager → Fundament → Rumpf
   → Wohnbereich
   - Abhilfe: Flexible Motorlager, flexible Auspuffverbindung,
     flexible Wellenkupplung
3. **Abgasschall**: Motorauspuff → Auspuffrohr → Auslassöffnung → Luft
   - Abhilfe: Wassergekühlter Auspuff, Schalldämpfer

### 8.2 Schallschutz-Materialien

**Soundown (USA) — Marine Schallschutz-Spezialist:**

| Produkt | Material | Dicke | dB-Reduktion | Preis/m² (€) |
|---------|---------|-------|-------------|-------------|
| Insul-Sheet | MLV + Schaum | 25 mm | 15–20 dB | 65 |
| Insul-Sheet HD | MLV + Schaum | 38 mm | 20–25 dB | 95 |
| Insul-Sheet Ultra | MLV + Schaum | 50 mm | 25–30 dB | 135 |
| Insul-Shield | Aluminium-Folie + Schaum | 25 mm | 12–15 dB | 45 |
| Vibration Pad | Viskoelastisch | 3 mm | Vibration | 25 |

**Isoflex (Deutschland):**

| Produkt | Material | Dicke | dB-Reduktion | Preis/m² (€) |
|---------|---------|-------|-------------|-------------|
| Isoflex FSH | PU-Schaum + Bleifolie | 30 mm | 18–22 dB | 75 |
| Isoflex FSH-S | PU-Schaum + Bleifolie | 50 mm | 24–28 dB | 120 |
| Isoflex TF | Textil-Faser | 20 mm | 10–14 dB | 35 |
| Isoflex Rapid | Selbstklebend | 25 mm | 14–18 dB | 55 |

**Mass Loaded Vinyl (MLV):**

| Variante | Flächengewicht | dB-Reduktion | Preis/m² (€) |
|---------|---------------|-------------|-------------|
| MLV 1 lb/ft² | 4,9 kg/m² | 15–18 dB | 25 |
| MLV 2 lb/ft² | 9,8 kg/m² | 20–24 dB | 45 |
| MLV + Foam 1" | 4,9 kg/m² + Schaum | 22–26 dB | 65 |
| MLV + Foam 2" | 9,8 kg/m² + Schaum | 28–32 dB | 95 |

**Lead Foam Composite (Bleischaum):**
- Bleifolien-Kern (1–3 mm) zwischen Schaumstofflagen
- Höchste Massebeladung pro Dicke
- dB-Reduktion: 25–35 dB
- Preis: 80–180 €/m²
- Achtung: Blei ist umweltbedenklich, in einigen EU-Ländern
  für Neubauten eingeschränkt

### 8.3 Schallschutzkapselung des Motors

Eine vollständige Motorkapselung reduziert den Luftschall um 15–30 dB,
abhängig von Material und Ausführung.

**Konstruktionsprinzipien:**

1. **Masse-Feder-Prinzip**: Schwere Außenhaut (MLV) + elastische
   Entkopplung vom Fundament + absorbierende Innenschicht (Schaum)
2. **Keine direkten Schallbrücken**: Kapsel darf nicht starr am
   Motor befestigt sein
3. **Luftspalt**: Mindestens 25 mm Abstand zwischen Motor und
   Kapsel-Innenseite
4. **Belüftung**: Kapsel darf die Motorbelüftung nicht behindern
5. **Wartungszugang**: Kapselteile müssen demontierbar sein
6. **Brandschutz**: Alle Materialien selbstverlöschend

**Typische dB-Werte:**

| Maßnahme | dB-Reduktion | Kosten (Boot 10 m) |
|---------|-------------|-------------------|
| Keine Kapsel | Referenz | — |
| Einfache Schaumstoff-Auskleidung | 8–12 dB | 200–400 € |
| MLV + Schaum-Auskleidung | 15–20 dB | 600–1.200 € |
| Professionelle Kapsel (Soundown) | 20–28 dB | 1.500–4.000 € |
| Custom-Kapsel mit Bleischaum | 25–35 dB | 3.000–8.000 € |

### 8.4 Flexible Verbindungen im Antriebsstrang

Jede starre Verbindung zwischen Motor und Rumpf ist eine Schallbrücke.
Folgende Verbindungen müssen flexibel ausgeführt sein:

| Verbindung | Flexibles Element | Hersteller |
|-----------|------------------|-----------|
| Motor → Fundament | Flexible Motorlager | Vetus, R&D Marine |
| Getriebe → Welle | Flexible Kupplung | R&D Marine K-Prop, Vetus Bullflex |
| Motor → Abgas | Flexibler Auspuffschlauch | Vetus, Halyard |
| Motor → Kühlwasser | Flexible Schläuche | Standard-Marineschläuche |
| Motor → Kraftstoff | Flexible Leitungen | Normflex |
| Motor → Elektrik | Flexible Kabel mit Durchhang | — |
| Motor → Bedenzüge | Flexible Bowdenzüge | — |

### 8.5 Vibrationsdämpfung im Rumpf

Zusätzlich zur Motorlagerung können Vibrationen im Rumpf durch
aufgeklebte Dämpfungsbeläge reduziert werden:

**Constrained Layer Damping (CLD):**
- Viskoelastische Folie zwischen zwei Metallplatten
- Auf Rumpf-Innenseite oder Schottflächen aufgeklebt
- Reduziert Rumpfplattenresonanz um 10–20 dB
- Material: ISODAMP C-1000, 3M SJ-2015
- Flächengewicht: 2–8 kg/m²
- Kosten: 40–120 €/m²

**Schwimmender Boden (Floating Floor):**
- Kabinenboden auf Elastomer-Pads oder Kork
- Entkoppelt Wohnbereich vom schwingenden Rumpf
- Reduktion: 10–15 dB
- Aufbauhöhe: 10–30 mm
- Kosten: 80–200 €/m²

### 8.6 Schallpegel-Referenzwerte

| Bereich | Motortyp | Akzeptabel (dB(A)) | Gut (dB(A)) | Exzellent (dB(A)) |
|---------|---------|-------------------|------------|------------------|
| Cockpit | Segelboot-Diesel | < 75 | < 70 | < 65 |
| Cockpit | Motoryacht | < 72 | < 68 | < 62 |
| Salon | Segelboot | < 70 | < 65 | < 58 |
| Salon | Motoryacht | < 68 | < 62 | < 55 |
| Eignerkabine | Segelboot | < 65 | < 58 | < 52 |
| Eignerkabine | Motoryacht | < 62 | < 55 | < 48 |
| Motorraum | Alle | 95–110 | — | — |

---
---

## 9. Motorraum-Belüftung

### 9.1 Grundlagen und Normen

Die Motorraum-Belüftung ist sicherheitskritisch und durch mehrere
Normen geregelt:

- **ISO 8178** — Emissionsmessungen, Luftzufuhr-Anforderungen
- **ISO 9094** — Brandschutz auf Booten
- **ISO 11105** — Belüftung von Benzinmotorräumen (für Diesel relevant
  als Referenz)
- **ABYC H-32** — Ventilation of Boats Using Diesel Fuel (US-Standard)

**Warum Belüftung kritisch ist:**
- Dieselmotoren benötigen 6–8 m³ Luft pro kW und Stunde für die Verbrennung
- Zusätzlich muss die Abwärme abgeführt werden (30–40 % der
  Verbrennungsenergie wird als Wärme abgegeben)
- Überhitzung des Motorraums führt zu:
  - Leistungsverlust (heißere Ansaugluft = weniger Dichte)
  - Beschleunigte Alterung aller Komponenten
  - Brandgefahr bei Kraftstoff-/Öl-Leckagen
  - Materialversagen bei Kunststoff- und Gummiteilen
  - Elektronikausfälle

### 9.2 Luftmengen-Berechnung

**Verbrennungsluft:**
```
Q_verbrennung = P × 7  [m³/h]

wobei P = Motorleistung in kW

Beispiel: Yanmar 4JH57 = 42 kW
  Q_verbrennung = 42 × 7 = 294 m³/h
```

**Kühlluft (Abwärmeabfuhr):**
```
Q_kuehlung = P × 0,4 × 3.600 / (ρ × cp × ΔT)  [m³/h]

wobei:
  P × 0,4 = Abwärmeleistung (40 % der Motorleistung)
  ρ = 1,2 kg/m³ (Luftdichte)
  cp = 1.005 J/(kg·K)
  ΔT = max. zulässige Temperaturerhöhung (15–20 K)

Beispiel:
  Q_kuehlung = 42.000 × 0,4 × 3.600 / (1,2 × 1.005 × 20) = 2.508 m³/h
```

**Gesamt-Luftbedarf:**
```
Q_gesamt = max(Q_verbrennung, Q_kuehlung)

Im Beispiel: max(294, 2.508) = 2.508 m³/h → die Kühlung bestimmt!
```

### 9.3 Belüftungsöffnungen

**Mindestquerschnitt der Zuluftöffnungen:**
```
A_zuluft = Q_gesamt / (v × 3.600)  [m²]

wobei v = Luftgeschwindigkeit (max. 5–8 m/s, um Geräusche zu begrenzen)

Beispiel:
  A_zuluft = 2.508 / (6 × 3.600) = 0,116 m² ≈ 1.160 cm²
```

Das entspricht z.B. 4 Lüftungsgittern à 290 cm² oder 2 Dorade-Boxen
mit je 580 cm² freiem Querschnitt.

**Abluft:**
Mindestens 50 % des Zuluftquerschnitts. Natürliche Konvektion (warm → oben)
unterstützt die Abfuhr.

### 9.4 Zwangsbelüftung (Forced Ventilation)

Wenn die natürliche Belüftung nicht ausreicht (typisch bei Motoryachten
mit geschlossenem Motorraum):

**Ventilator-Auswahl:**

| Motorleistung | Luftbedarf | Ventilator | Ø Kanal |
|--------------|-----------|-----------|---------|
| 10–20 kW | 500–1.200 m³/h | 1× Ø 100 mm | 100 mm |
| 20–40 kW | 1.200–2.500 m³/h | 1× Ø 150 mm | 150 mm |
| 40–80 kW | 2.500–5.000 m³/h | 2× Ø 150 mm | 2× 150 mm |
| 80–150 kW | 5.000–10.000 m³/h | 2× Ø 200 mm | 2× 200 mm |
| 150–300 kW | 10.000–20.000 m³/h | Spezialplanung | Spezial |

**Ventilator-Typen:**
- **Bilge Blower**: Standard-Marinelüfter, 12V/24V, IP67
- **In-Line-Ventilator**: im Lüftungskanal montiert
- **Zentrifugalventilator**: höherer Druck, für lange Kanäle
- **ATEX-Ventilator**: explosionsgeschützt (für Benzinmotoren Pflicht)

**Hersteller:**
- Vetus (BOW-Serie): 12V/24V, 100–350 m³/h, 45–180 €
- Sealand/Dometic: industrielle Marinelüfter
- Vent-Axia (UK): hochwertige In-Line-Ventilatoren
- Jabsco (Xylem): klassische Bilge Blower

### 9.5 Brandschutzklappen (Fire Dampers)

Bei Motorräumen mit Zwangsbelüftung müssen Brandschutzklappen
(Fire Dampers) in den Lüftungskanälen installiert werden.

**Anforderungen nach ISO 9094:**
- Automatisches Schließen bei Feuer (Schmelzlot bei 72 °C oder 79 °C)
- Manuelles Auslösen von außerhalb des Motorraums möglich
- Vollständiger Verschluss (keine Restöffnung)
- Feuerwiderstand: mindestens 30 Minuten
- Selbsthaltend in geschlossenem Zustand

**Hersteller:**
- Blakes (UK): Marine Fire Dampers, 75–400 mm
- Halyard (UK): Fire-rated Dampers mit ISO-Zertifikat
- Vetus: Integrierte Brandschutzklappen für BOW-Lüfter

### 9.6 Motorraum-Temperaturüberwachung

Empfohlene Temperaturgrenzen:

| Bereich | Normal (°C) | Warnung (°C) | Alarm (°C) |
|---------|-----------|-------------|-----------|
| Motorraum gesamt | 40–55 | 55–65 | > 65 |
| Nahe Auspuffkrümmer | 60–80 | 80–100 | > 100 |
| Kraftstofffilter-Bereich | 35–50 | 50–60 | > 60 |
| Batteriebereich | 20–35 | 35–45 | > 45 |
| Schallschutzmaterial | 40–60 | 60–80 | > 80 |

---
---

## 10. Motorraum-Isolation

### 10.1 Thermische Isolation

Motorräume müssen thermisch isoliert werden, um:
- Wärmeübertragung in den Wohnbereich zu minimieren
- Brandausbreitung zu verlangsamen
- Kondensation auf kalten Rumpfflächen zu vermeiden

**Materialien:**

| Material | Temp.-Beständigkeit | Brandklasse | Dicke | Preis/m² (€) |
|---------|-------------------|-----------|-------|-------------|
| Steinwolle (Rockwool Marine) | 700 °C | A1 (nicht brennbar) | 25–50 mm | 20–45 |
| Glaswolle (Isover Marine) | 500 °C | A1 | 25–50 mm | 15–35 |
| Keramikfaser | 1.260 °C | A1 | 10–25 mm | 40–80 |
| Melamin-Schaum (Basotect) | 200 °C | B1 (schwer entflammbar) | 20–50 mm | 35–60 |
| PU-Schaum (selbstverlöschend) | 150 °C | B1 | 20–40 mm | 25–45 |
| Aluminium-Sandwich | 600 °C | A1 | 10–30 mm | 50–100 |

### 10.2 Halyard Marine (UK)

Halyard Marine Products ist der Marktführer für marine Brandschutz-
und Isolationssysteme.

**Produkte:**

| Produkt | Beschreibung | Brandschutz | Einsatz |
|---------|-------------|-----------|--------|
| Fireshield 50 | Keramikfaser + Folie | 30 min (A-30) | Motorraum-Wände |
| Fireshield 100 | Keramikfaser + Folie | 60 min (A-60) | Superyacht-Standard |
| Sonemat | Schalldämmmatte | B1 | Motorraum-Auskleidung |
| Firetex | Brandschutzfarbe | 30–120 min | Stahlkonstruktionen |
| Damping Sheet | Viskoelastisch | — | Rumpfplatten |

### 10.3 Installation von Motorraum-Isolation

**Richtige Installation:**
1. Alle Oberflächen reinigen und entfetten
2. Isolationsmaterial zuschneiden (5 mm Übermaß)
3. Mit geeignetem Kleber oder Befestigungspins montieren
4. Stoßstellen überlappen (mind. 30 mm) oder mit Aluklebeband verschließen
5. Keine Hohlräume (Luftpolster verschlechtern die Wirkung)
6. Isolierung darf keine Motorteile berühren (Vibrationsabrieb)
7. Abstand zum Auspuff: mindestens 50 mm (oder hitzebeständiges Material)

**Häufige Fehler:**
- Schaumstoff direkt am Auspuffkrümmer → Brandgefahr!
- Nicht-selbstverlöschende Materialien → Brandgefahr!
- Öl-getränkte Isolierung nicht erneuert → Brandgefahr!
- Isolierung blockiert Belüftungsöffnungen → Überhitzung
- Isolierung nicht befestigt, hängt auf Motor → Vibration, Abrieb, Brand

---
---

## 11. Motorraumzugang und Wartungsräume

### 11.1 Grundsätzliche Anforderungen

Der Motorraumzugang bestimmt maßgeblich die Wartungsfreundlichkeit
einer Yacht und damit die langfristigen Betriebskosten.

**ISO-Anforderungen und Branchenstandards:**
- Zugang zu Ölablassschraube ohne Demontage anderer Teile
- Zugang zu Ölfilter mit max. 1 Handgriff Demontage
- Zugang zu Kraftstofffilter ohne Werkzeug-Demontage
- Zugang zu Keilriemen/Zahnriemen mit max. 2 Handgriffen
- Zugang zu Impeller-Deckel mit max. 1 Handgriff
- Sichtbarkeit des Motorölstands ohne Verrenkung
- Zugang zum Getriebe-Ölmessstab

### 11.2 Zugangsklassen (AYDI-Bewertung)

| Klasse | Beschreibung | Demontage | Punkte |
|--------|-------------|----------|--------|
| A — Exzellent | Motorraum begehbar, alle Seiten frei | Keine | 90–100 |
| B — Gut | Motor von 3 Seiten zugänglich, große Luke | 1 Panel | 70–89 |
| C — Ausreichend | Motor von 2 Seiten zugänglich | 2–3 Panels | 50–69 |
| D — Mangelhaft | Motor nur von oben/vorne zugänglich | 4+ Panels | 30–49 |
| E — Unzureichend | Motor-Wartung erfordert Spezialwerkzeug/Ausbau | Major | 0–29 |

### 11.3 Mindestabstände für Wartungsarbeiten

| Wartungsarbeit | Mindestabstand (mm) | Ideal (mm) |
|---------------|-------------------|-----------|
| Ölwechsel (Absaugpumpe) | 100 oben | 200 oben |
| Ölfilter-Wechsel | 100 seitlich | 200 seitlich |
| Impeller-Wechsel | 150 vorne | 250 vorne |
| Keilriemen-Wechsel | 100 seitlich | 200 seitlich |
| Kraftstofffilter | 80 seitlich | 150 seitlich |
| Kühlmittel-Kontrolle | 50 oben | 150 oben |
| Motorlager-Kontrolle | 100 unten/seitlich | 200 unten/seitlich |
| Alignment-Prüfung | 200 hinten | 400 hinten |
| Lichtmaschine | 100 seitlich | 200 seitlich |
| Anlasser | 150 seitlich | 250 seitlich |

### 11.4 Luken- und Paneel-Systeme

**Typen von Motorraumzugängen:**

| Typ | Beschreibung | Vor-/Nachteile |
|-----|-------------|---------------|
| Hebe-Luke | Salontisch oder Boden hebt sich hydraulisch | +Großer Zugang, −Teuer |
| Klapp-Luke | Bodenpanel klappt auf Scharnieren | +Einfach, −Begrenzt |
| Schiebe-Panels | Mehrere Platten schieben/herausnehmen | +Flexibel, −Langwierig |
| Niedergangs-Treppe | Treppe schwenkt/hebt sich | +Keine Extra-Luke, −Komplex |
| Cockpitboden | Gesamter Cockpitboden hebbar | +Voller Zugang, −Schwer |
| Seitenschotten | Schotte mit Schnellverschlüssen | +Seitlicher Zugang, −Schallbrücke |

### 11.5 Wartungsraumplanung bei Neubauten

Empfehlungen für den Entwurf:

- **Mindestens 400 mm** freier Raum über der Motoroberkante
- **Mindestens 200 mm** seitlich zu Rumpf/Fundament
- **Mindestens 300 mm** hinter dem Getriebe (für Alignment-Arbeiten)
- **Bilgenpumpe** nicht direkt unter dem Motor (Ölverschmutzung)
- **Beleuchtung** im Motorraum (12V LED, wasserdicht)
- **Ölwechsel-Leitung** fest installiert mit Absperrhahn
- **Werkzeughalterung** oder -tasche im Motorraum
- **Etiketten** an allen Wartungspunkten (Ölsorte, Filtergröße, etc.)

---
---

## 12. Motorumrüstung (Repowering)

### 12.1 Wann ist Repowering sinnvoll?

**Typische Auslöser:**
- Motor hat 8.000–15.000 Betriebsstunden erreicht
- Ersatzteile nicht mehr verfügbar (Abkündigung)
- Motorschaden (Kolbenfresser, Kurbelwellenschaden)
- Leistungsbedarf ändert sich (neuer Propeller, neues Nutzungsprofil)
- Emissionsvorschriften erfordern neueren Motor
- Umstieg auf Elektro-/Hybridantrieb
- Kraftstoffverbrauch zu hoch (ältere Motoren 10–30 % mehr)
- Lärm und Vibrationen nicht mehr akzeptabel

### 12.2 Motorauswahl bei Repowering

**Grundregel:** Den Motor so wählen, dass er auf die vorhandenen
Fundamente passt — oder das Budget für neue Fundamente einplanen.

**Kompatibilitäts-Matrix gängiger Ersatzmotoren:**

| Alter Motor | Direkter Ersatz | Fundament-Anpassung | Neues Fundament |
|------------|----------------|-------------------|----------------|
| Volvo MD2020 | Volvo D1-20 | — | — |
| Volvo MD2030 | Volvo D1-30 | — | — |
| Volvo MD2040 | Volvo D2-40 | — | — |
| Volvo 2003 | Volvo D2-55/D2-60 | Lagerabstand prüfen | Selten nötig |
| Yanmar 2GM20 | Yanmar 2YM15 | Minimale Anpassung | — |
| Yanmar 3GM30 | Yanmar 3JH40 | Lagerabstand prüfen | — |
| Yanmar 3JH2E | Yanmar 3JH40 | — | — |
| Yanmar 4JH2E | Yanmar 4JH57/4JH80 | Lagerabstand prüfen | — |
| Perkins 4.108 | Beta 43 / Nanni N4.50 | Neues Fundament | Adapter-Kit |
| Bukh DV36 | Beta 38 / Nanni N4.40 | Neues Fundament | — |
| Westerbeke 30B | Beta 30 / Yanmar 3JH40 | Neues Fundament | — |

### 12.3 Repowering-Ablauf

**Phase 1 — Planung (2–4 Wochen):**
1. Bestehenden Motor vermessen (LxBxH, Lagerabstände, Wellenachsenhöhe)
2. Neuen Motor auswählen und Einbaumaße vergleichen
3. Fundament-Kompatibilität prüfen
4. Wellenanlage prüfen (Wellenmaß, Stevenrohr, Propeller)
5. Kühlung, Abgas, Elektrik planen
6. Budget erstellen

**Phase 2 — Demontage (2–5 Tage):**
1. Motor konservieren oder entsorgen
2. Alle Anschlüsse dokumentieren und fotografieren
3. Motor mit Flaschenzug oder Kran ausbauen
4. Fundament inspizieren und ggf. reparieren
5. Bilge reinigen und beschichten

**Phase 3 — Fundament-Anpassung (1–5 Tage):**
1. Neue Lagerbolzenpositionen ermitteln
2. Stahlplatten/Gewindebuchsen einlaminieren oder schweißen
3. Aushärtung abwarten (Epoxid: 24–72 h bei 20 °C)
4. Oberfläche planschleifen oder -fräsen
5. Bilgenfarbe/Epoxid auftragen

**Phase 4 — Einbau (3–7 Tage):**
1. Motor auf Fundament setzen (Kran/Flaschenzug)
2. Motorlager montieren und vorjustieren
3. Wellenanlage/Kupplung anschließen
4. Grob-Alignment mit Stahllineal
5. Kühlwasser, Abgas, Kraftstoff anschließen
6. Elektrik verkabeln
7. Bedenzüge (Gas, Schaltung) montieren
8. Fein-Alignment mit Messuhr oder Laser

**Phase 5 — Inbetriebnahme (1–2 Tage):**
1. Alle Anschlüsse auf Dichtheit prüfen
2. Motoröl und Kühlmittel einfüllen
3. Kraftstoffsystem entlüften
4. Erststart und Warmlaufen im Stand
5. Probefahrt mit Temperatur-/Drehzahlüberwachung
6. Alignment nach Warmlauf erneut prüfen
7. Dokumentation erstellen

### 12.4 Kosten-Abschätzung Repowering

| Position | Segelboot 10 m | Segelboot 14 m | Motoryacht 12 m |
|---------|---------------|---------------|----------------|
| Neuer Motor (ink. Getriebe) | 8.000–15.000 € | 12.000–25.000 € | 15.000–40.000 € |
| Motorlager (4×) | 100–250 € | 150–400 € | 200–500 € |
| Fundament-Anpassung | 500–2.000 € | 1.000–4.000 € | 1.500–5.000 € |
| Wellenanlage/Kupplung | 300–1.000 € | 500–2.000 € | 800–3.000 € |
| Propeller (ggf. neu) | 400–1.500 € | 600–3.000 € | 1.000–5.000 € |
| Abgasanlage | 300–800 € | 500–1.500 € | 800–3.000 € |
| Kühlsystem | 200–600 € | 300–1.000 € | 500–2.000 € |
| Elektrik | 300–800 € | 500–1.500 € | 800–2.500 € |
| Schallisolierung | 300–800 € | 500–1.500 € | 800–3.000 € |
| Arbeitslohn (40–80 €/h) | 2.000–5.000 € | 3.000–8.000 € | 5.000–15.000 € |
| **Gesamt** | **12.400–27.750 €** | **18.550–47.400 €** | **26.400–79.000 €** |

### 12.5 Elektro-Repowering

Zunehmend relevant für Segelboote und Motoryachten im Küstenbereich:

**Komponenten:**
- Elektromotor (5–50 kW): Torqeedo, Oceanvolt, Bellmarine, Elco
- Batteriebank (LiFePO4): 5–60 kWh
- Ladegerät (Landstrom): 2–10 kW
- Solar-/Hydrogenerator: optional
- Motorcontroller/Inverter
- Display und Bedienelemente

**Besonderheiten bei Motorlagerung:**
- Elektromotoren vibrieren kaum → weichere Lager möglich (35–45 Shore A)
- Geringeres Gewicht → leichtere Lager, aber Batteriegewicht beachten
- Kein Alignment bei Pod-Antrieben (Saildrive-Äquivalent)
- Bei Wellenantrieb: identisches Alignment wie Diesel
- Kein Abgas, keine Motorraum-Belüftung für Verbrennung nötig
- Batterien benötigen eigene Belüftung (Entgasung bei Ladung)

### 12.6 Hybridantrieb-Integration

**Paralleler Hybrid (Motor + E-Motor auf einer Welle):**
- Zusätzliche Alignment-Herausforderung (3 Achsen müssen fluchten)
- Kupplungssystem zwischen Diesel und E-Motor
- Schwingungsisolation für zwei unterschiedliche Erregerfrequenzen
- Motorlager für höheres Gesamtgewicht dimensionieren

**Serieller Hybrid (Generator + E-Motor):**
- Generator-Lagerung wie Hilfsaggregat
- E-Motor-Lagerung am Propellerantrieb
- Einfacheres Alignment (nur E-Motor → Welle)
- Generator kann vibrationsoptimiert aufgestellt werden

---
---

## 13. Normen und Vorschriften

### 13.1 Relevante ISO-Normen

| Norm | Titel | Relevanz |
|------|-------|---------|
| ISO 8178 | Emissionen, Luftzufuhr | Motorraum-Belüftung |
| ISO 9094 | Brandschutz | Motorraum-Isolation, Brandklappen |
| ISO 11105 | Belüftung Motorräume | Belüftungsquerschnitte |
| ISO 12217 | Stabilität | Motorposition, Gewichtsverteilung |
| ISO 10133 | Elektrik DC | Kabelverlegung im Motorraum |
| ISO 13297 | Elektrik AC | Landstrom im Motorraum |
| ISO 15085 | Personensicherheit | Schutz vor heißen Oberflächen |
| ISO 8846 | Zündschutz Elektrik | Schalter/Relais im Motorraum |

> ⚠️ **ZU PRÜFEN (Audit):** Die Zeile „ISO 15085 | Personensicherheit | Schutz vor
> heißen Oberflächen" ist fehlerhaft: ISO 15085 regelt „Small craft — Man-overboard
> prevention and recovery" (Verhütung von Über-Bord-Fällen, Reling-/Wiedereinstieg),
> NICHT den Schutz vor heißen Oberflächen. Die Normnummer passt nicht zum angegebenen
> Scope. Die korrekte Norm für den Schutz von Personen vor heißen Motor-/Abgasflächen
> ist zu verifizieren (nicht ISO 15085) — bis dahin unverifiziert.
> Quelle: iso.org/standard/26408.html (ISO 15085:2003, Man-overboard prevention and recovery).

### 13.2 Klassifikationsgesellschaften

Für Yachten ab 24 m (Superyacht-Bereich) gelten zusätzlich die Regeln
der Klassifikationsgesellschaften:

| Gesellschaft | Standard | Motorlager-Anforderung |
|-------------|---------|----------------------|
| Lloyd's Register | SSC Rules | Typ-geprüfte Lager, Alignment-Protokoll |
| DNV | DNVGL-RU-HSLC | Schwingungsberechnung, Shore-Härte-Nachweis |
| Bureau Veritas | NR 500 | Materialzertifikat Elastomer, Alignment |
| RINA | Rules for Yachts | Motorlager-Zulassung, Probelauf-Protokoll |
| ABS | Guide for Yachts | Alignment-Toleranzen, Vibrationsmessung |

### 13.3 CE-Relevanz

Für Boote 2,5–24 m unter CE-Kennzeichnung:
- Motorinstallation nach EN ISO 8665 (Motorleistungsmessung)
- Abgasemissionen nach EU 2016/1628
- Geräuschemissionen nach ISO 14509
- Brandschutz nach ISO 9094
- Motorlager selbst sind nicht direkt durch CE geregelt, aber Teil
  des Gesamtsystems „Motorinstallation"

---
---

## 14. Fehlerbild-Atlas

### 14.1 Fehlerbild: Gerissenes Elastomer

**Beschreibung:** Sichtbare Risse im Gummikörper des Motorlagers.
Von Haarrissen bis zu Durchrissen.

**Ursachen:**
- Alterung (UV, Ozon, Hitze) — ab 7–10 Jahren wahrscheinlich
- Überlastung (Motor zu schwer für gewähltes Lager)
- Ölkontamination (Diesel/Motoröl löst EPDM-Weichmacher)
- Chemikalienbelastung (Bilgenreiniger, Lösungsmittel)
- Dauerhaft zu hohe Motorraum-Temperatur (> 70 °C)

**Diagnose:**
- Sichtprüfung: Risse an Oberfläche, besonders an Knickstellen
- Deflexionsmessung: > 35 % über Nennwert
- Hörprüfung: metallisches Klicken bei Gasstößen

**Maßnahme:**
- Austausch aller 4 Lager gleichzeitig (nie einzeln!)
- Alignment nach Austausch erforderlich
- Ursache der Kontamination beseitigen (Ölleck, Belüftung verbessern)

**Confidence:** measured (Sichtbefund) / visual_high (Foto-Diagnose)

### 14.2 Fehlerbild: Motor sackt ab (einseitig)

**Beschreibung:** Motor steht schief, ein oder zwei Lager sind stärker
eingedrückt als die anderen.

**Ursachen:**
- Ungleiche Lagerbelastung (falsche Shore-Härte-Kombination)
- Einseitiger Lagerverschleiß
- Fundament-Verformung oder -bruch unter einem Lager
- Motor-Schwerpunktverschiebung (schwerer Anbau einseitig)

**Diagnose:**
- Wasserwaage auf Motor-Ventildeckel
- Höhenmessung an allen 4 Lagerpunkten
- Alignment-Prüfung (Out-of-tolerance vertikal)

**Maßnahme:**
- Alle 4 Lager prüfen und ggf. tauschen
- Fundament unter dem betroffenen Lager inspizieren
- Alignment komplett neu einstellen
- Ursache der ungleichmäßigen Belastung beseitigen

**Confidence:** measured (Messuhr) / visual_medium (Foto bei deutlicher Schieflage)

### 14.3 Fehlerbild: Motorlager-Bolzen korrodiert

**Beschreibung:** Befestigungsbolzen der Motorlager zeigen starke
Korrosion, sind festgefressen oder gebrochen.

**Ursachen:**
- Falsches Material (verzinkter Stahl statt Edelstahl 316L)
- Galvanische Korrosion (Kontakt ungleicher Metalle)
- Salzwasser-Kontakt (Bilgenwasser, Kondensat)
- Fehlende Korrosionsschutz-Behandlung

**Diagnose:**
- Sichtprüfung: Rost, Lochfraß, Verfärbung
- Drehmoment-Prüfung: Mutter nicht lösbar oder dreht durch
- Klopfprüfung: hohler Klang bei stark korrodiertem Bolzen

**Maßnahme:**
- Bolzen ersetzen (Edelstahl 316L, ggf. A4-80)
- Kontaktkorrosion verhindern (Isolierbuchsen, Tef-Gel)
- Ursache des Wasserkontakts beseitigen
- Bilgenmanagement verbessern

**Confidence:** measured / visual_high

### 14.4 Fehlerbild: Fundament-Risse

**Beschreibung:** Risse im GFK-Laminat oder Holz des Motorfundaments,
typisch an Übergängen Stringer → Rumpf oder unter Lagerplatten.

**Ursachen:**
- Unterdimensioniertes Fundament
- Schlagbelastung (Grundberührung, harte See)
- Motorlager zu hart (Schwingungen direkt ins Fundament)
- Alterung/Ermüdung des GFK-Laminats
- Osmotische Schäden am GFK

**Diagnose:**
- Sichtprüfung: Haarrisse im Gelcoat/Laminat
- Klopfprüfung: hohler Klang bei Delamination
- Feuchtemessung: erhöhte Feuchtigkeit bei osmotischen Schäden
- Wackeltest: Motor seitlich drücken, Fundament beobachten

**Maßnahme:**
- GFK-Reparatur: anschleifen, trocknen, überlaminieren
- Bei Delamination: beschädigtes Laminat entfernen und neu aufbauen
- Fundament verstärken (zusätzliche Lagen, Stahlverstärkung)
- Alignment nach Reparatur komplett neu

**Confidence:** measured (Klopfprüfung, Feuchte) / visual_medium

### 14.5 Fehlerbild: Übermäßige Vibrationen bei Leerlauf

**Beschreibung:** Motor vibriert im Leerlauf deutlich stärker als
bei höheren Drehzahlen. Typisch bei Vierzylinder-Dieseln.

**Ursachen:**
- Resonanzfrequenz der Motorlager nahe der Leerlauf-Erregerfrequenz
- Motorlager zu steif (Shore-Härte zu hoch für den Motor)
- Ungleichlauf des Motors im Leerlauf (Einspritzung nicht gleichmäßig)
- Schwungscheiben-Unwucht

**Diagnose:**
- Frequenzanalyse: dominante Frequenz bei Leerlauf messen
- Eigenfrequenz der Lager berechnen und vergleichen
- Motor auf allen Zylindern gleichmäßig? (Abgastemperatur-Vergleich)

**Maßnahme:**
- Weichere Motorlager einbauen (Shore-Härte 5–10 Punkte niedriger)
- Leerlaufdrehzahl erhöhen (wenn Motor es erlaubt, +50–100 U/min)
- Einspritzung prüfen und einstellen
- Schwungscheibe auf Unwucht prüfen

**Confidence:** measured (Frequenzmessung) / estimated (Shore-Härte-Berechnung)

### 14.6 Fehlerbild: Kupplungsverschleiß durch Fehl-Alignment

**Beschreibung:** Übermäßiger Verschleiß an der flexiblen Wellenkupplung
(Gummi-Elemente ausgefranst, Metallflächen blank geschliffen).

**Ursachen:**
- Motor-Wellen-Alignment außerhalb Toleranz
- Motorlager gesetzt/verschlissen, Alignment verloren
- Fundament verformt
- Rumpfverformung durch Beladung oder Alterung

**Diagnose:**
- Kupplung inspizieren: Gummi-Elemente, Verschleißmarken
- Alignment-Messung durchführen
- Motorlager-Deflexion prüfen

**Maßnahme:**
- Kupplung erneuern
- Alignment korrigieren
- Motorlager prüfen und ggf. erneuern
- Alignment-Protokoll anlegen und regelmäßig prüfen

**Confidence:** measured (Alignment-Messung) / visual_high (Kupplungszustand)

### 14.7 Fehlerbild: Öl-kontaminierte Motorlager

**Beschreibung:** Motorlager-Elastomer ist mit Motoröl oder Diesel
getränkt. Gummi ist weich, aufgequollen und hat Tragfähigkeit verloren.

**Ursachen:**
- Motoröl-Leck (Ölwannendichtung, Ölfilter)
- Diesel-Leck (Kraftstoffleitung, Filtergehäuse)
- Hydrauliköl-Leck (Getriebe, Steueranlage)

**Diagnose:**
- Sichtprüfung: glänzende, ölige Oberfläche
- Tastprüfung: Gummi klebt, ist weich und formbar
- Shore-Härte-Messung: deutlich unter Nennwert

**Maßnahme:**
- Alle 4 Lager tauschen (ölkontaminiertes Elastomer regeneriert sich nicht)
- Ölleck reparieren
- Ölwanne unter Motor installieren
- Fundament reinigen und ggf. neu beschichten

**Confidence:** measured / visual_high

### 14.8 Fehlerbild: Motorraum-Überhitzung

**Beschreibung:** Motorraum-Temperatur über 65 °C, beschleunigte
Alterung aller Komponenten, Motorlager härten aus.

**Ursachen:**
- Unzureichende Belüftung (Zuluft/Abluft-Öffnungen zu klein)
- Verstopfte Lüftungsgitter (Laub, Insekten, Farbschichten)
- Defekter Motorraum-Lüfter
- Schallisolierung blockiert Luftzirkulation
- Kühlwasser-Austritt (Dampf erhöht Temperatur und Feuchtigkeit)

**Diagnose:**
- Temperaturmessung mit IR-Thermometer
- Luftstrom-Messung an Zuluft-Öffnungen (Anemometer)
- Visuelle Prüfung: Verfärbung von Kunststoff- und Gummiteilen
- Isolierung auf Blockade prüfen

**Maßnahme:**
- Lüftungsöffnungen vergrößern oder reinigen
- Zwangslüfter installieren oder ersetzen
- Isolierung korrekt verlegen (keine Blockade)
- Kühlwasser-Leck reparieren
- Hitze-reflektierende Folie an besonders exponierten Stellen

**Confidence:** measured (Thermometer) / visual_medium

### 14.9 Fehlerbild: Motorlager-Bolzen lose

**Beschreibung:** Befestigungsmuttern der Motorlager haben sich gelöst.
Motor hat Spiel und wandert bei Laständerung.

**Ursachen:**
- Fehlende Sicherung (kein Loctite, keine Kontermutter, kein Federnring)
- Vibration hat Schrauben gelöst
- Falsches Anzugsmoment (zu gering)
- Korrosion hat Vorspannkraft reduziert

**Diagnose:**
- Maulschlüssel-Test: Mutter mit Hand drehbar?
- Wackeltest: Motor seitlich bewegen, Spiel fühlbar?
- Sichtprüfung: Muttern sichtbar verdreht gegenüber Markierung?

**Maßnahme:**
- Alle Muttern lösen, reinigen, mit korrektem Drehmoment anziehen
- Loctite 243 (mittelfest) auf Gewinde
- Kontermutter zusätzlich
- Alignment nach Festziehen prüfen (Anzugsmoment verändert Höhe!)
- Nach 50 h Nachprüfung

**Confidence:** measured / visual_medium

### 14.10 Fehlerbild: Schallbrücke durch starren Kontakt

**Beschreibung:** Trotz flexibler Motorlager übertragen sich
Motorvibrationen stark in den Rumpf. Ein starrer Kontaktpunkt
umgeht die Schwingungsisolation.

**Ursachen:**
- Auspuffschlauch starr an Motor und Rumpf befestigt
- Kühlwasserschlauch zu kurz/steif (kein Durchhang)
- Gaszug oder Schaltzug zu straff
- Kabel ohne Durchhang
- Werkzeug oder Lappen zwischen Motor und Fundament eingeklemmt
- Motor berührt Schallisolierung

**Diagnose:**
- Stethoskop an Verdachtsstelle: Vibration lauter als am Motorlager?
- Systematisch alle Verbindungen prüfen (Motor laufen lassen, einzeln
  lösen/entfernen und Vibration beobachten)

**Maßnahme:**
- Alle starren Verbindungen identifizieren und eliminieren
- Flexible Auspuffverbindung prüfen/erneuern
- Kabel und Schläuche mit ausreichend Durchhang verlegen
- Isolierung mit Abstand zum Motor befestigen

**Confidence:** measured (Stethoskop) / visual_low (schwer fotografierbar)

### 14.11 Fehlerbild: Wellengeräusch (Brummen/Dröhnen)

**Beschreibung:** Tieffrequentes Brummen bei bestimmten Drehzahlen,
das sich durch den gesamten Rumpf ausbreitet.

**Ursachen:**
- Rumpfplatten-Resonanz (Plattenfrequenz = Erregerfrequenz)
- Wellen-Biegeschwingung
- Stevenrohr als Resonanzkörper
- Propeller-Resonanz (Flügelfrequenz = Rumpf-Eigenfrequenz)

**Diagnose:**
- Drehzahl, bei der Brummen auftritt, genau bestimmen
- Frequenz messen (App oder Messgerät)
- Rumpfplatten im Brummbereich abtasten (Resonanz spürbar?)
- Testfahrt: Gang einlegen vs. neutral bei gleicher Drehzahl

**Maßnahme:**
- Constrained Layer Damping (CLD) auf resonierenden Rumpfplatten
- Verstärkungsrippen auf Rumpf-Innenseite
- Propeller-Wechsel (andere Flügelzahl)
- Wellendrehzahl anpassen (Getriebeuntersetzung ändern)

**Confidence:** measured (Frequenzmessung) / estimated (Ursachenzuordnung)

### 14.12 Fehlerbild: Motorfundament-Ablösung

**Beschreibung:** Motorfundament (Stringer) löst sich vom Rumpf.
Sichtbarer Spalt zwischen Stringer-Fuß und Rumpf-Innenlaminat.

**Ursachen:**
- Unterdimensioniertes Laminat (zu wenige Lagen, zu schmaler Flansch)
- Grundberührung oder Aufsetzer
- Schwerewetter-Belastung (Rumpfbiegung)
- Osmotische Schäden am Rumpf unter dem Stringer
- Schlechte Erstlaminierung (Haftungsfehler, Lufteinschlüsse)

**Diagnose:**
- Sichtprüfung: Spalt zwischen Stringer und Rumpf
- Klopfprüfung: hohler Klang entlang des Stringers
- Belastungstest: Motor laufen lassen, Stringer beobachten
  (Bewegung sichtbar?)

**Maßnahme:**
- **Sofort**: Motor nicht betreiben (Bruchgefahr!)
- Spalt reinigen, trocknen, mit Epoxid verfüllen
- Zusätzliche Laminatlagen (6–10) über Stringerfuß und
  mindestens 100 mm auf Rumpf-Innenseite
- Strukturelle Berechnung durch Fachbetrieb empfohlen
- Alignment komplett neu nach Aushärtung

**Confidence:** measured (Sichtprüfung, Klopfprüfung) / visual_high

---
---

## 15. Troubleshooting

### 15.1 Troubleshooting-Entscheidungsbaum: Vibrationen

```
Vibration festgestellt
    ├── Bei welcher Drehzahl?
    │   ├── Nur Leerlauf → Resonanz (Kapitel 5.4)
    │   │   ├── Weichere Lager einbauen
    │   │   ├── Leerlaufdrehzahl erhöhen
    │   │   └── Einspritzung prüfen
    │   │
    │   ├── Bestimmte Drehzahl (nicht Leerlauf) → Rumpfresonanz
    │   │   ├── Frequenz messen
    │   │   ├── CLD auf resonierender Fläche
    │   │   └── Drehzahl meiden (Betriebsanweisung)
    │   │
    │   └── Alle Drehzahlen → Alignment oder Motordefekt
    │       ├── Alignment prüfen
    │       ├── Motorlager prüfen (Deflexion)
    │       ├── Kupplung prüfen
    │       └── Motor intern prüfen (Schwungscheibe, Einspritzung)
    │
    ├── Wo am stärksten spürbar?
    │   ├── Am Motor → Motorlager-Problem
    │   ├── Am Stevenrohr/Heck → Alignment/Wellen-Problem
    │   ├── Im Salon → Schallbrücke oder Rumpfresonanz
    │   └── Überall gleich → Fundamentales Problem
    │
    └── Seit wann?
        ├── Seit Einbau → Dimensionierung/Alignment
        ├── Plötzlich → Defekt (Lager, Kupplung, Fundament)
        └── Schleichend → Alterung (Lager, Setzung)
```

### 15.2 Troubleshooting-Entscheidungsbaum: Geräusche

```
Motorgeräusch zu laut
    ├── Motorraum-Schallpegel messen
    │   ├── > 110 dB(A) → Motor intern (Ventile, Einspritzung, Kolben)
    │   └── 95–110 dB(A) → Normal, Isolation verbessern
    │
    ├── Wohnbereich-Schallpegel messen
    │   ├── > 75 dB(A) → Massive Schallbrücke oder fehlende Isolation
    │   ├── 65–75 dB(A) → Isolation verbesserungsfähig
    │   └── < 65 dB(A) → Akzeptabel bis gut
    │
    ├── Geräuschtyp?
    │   ├── Metallisches Klicken → Motorlager-Bolzen lose, Kupplung
    │   ├── Tiefes Brummen → Rumpfresonanz, Wellenresonanz
    │   ├── Hochfrequentes Pfeifen → Turbo, Keilriemen, Lichtmaschine
    │   ├── Klopfen/Hämmern → Motor intern, Alignment, Propellerschlag
    │   └── Rauschen → Auspuff, Belüftung, Kühlwasser
    │
    └── Schallbrücke identifizieren
        ├── Stethoskop an allen Verbindungspunkten
        ├── Systematisch Verbindungen lösen
        └── Lautester Punkt = Schallbrücke
```

### 15.3 Troubleshooting-Entscheidungsbaum: Alignment-Verlust

```
Alignment außerhalb Toleranz
    ├── Alle 4 Motorlager-Deflexionen messen
    │   ├── Gleichmäßig erhöht → Alterung, alle tauschen
    │   ├── Ungleichmäßig → Schwerpunktproblem oder einzelne defekte Lager
    │   └── Normal → Fundament-Problem oder Rumpfverformung
    │
    ├── Fundament inspizieren
    │   ├── Risse sichtbar → Reparatur (Kapitel 14.4)
    │   ├── Ablösung → Reparatur (Kapitel 14.12)
    │   └── Intakt → Weiter prüfen
    │
    ├── Wann verloren?
    │   ├── Nach Kranvorgang → Normal, nach Ablassen prüfen
    │   ├── Nach Grundberührung → Rumpfverformung, Fundament prüfen
    │   ├── Saisonbeginn → Holzrumpf Quellung/Schwindung
    │   └── Schleichend → Lager-Setzung, jährlich nachstellen
    │
    └── Welche Achse?
        ├── Vertikal → Lagerhöhe anpassen
        ├── Horizontal → Lager seitlich verschieben
        └── Winkel → Vordere/hintere Lager ungleich, selektiv anpassen
```

### 15.4 Troubleshooting-Entscheidungsbaum: Motorraum-Temperatur

```
Motorraum zu heiß (> 65 °C)
    ├── Zuluft-Öffnungen prüfen
    │   ├── Verstopft → Reinigen
    │   ├── Zu klein → Vergrößern (Berechnung Kapitel 9.3)
    │   └── OK → Weiter
    │
    ├── Abluft prüfen
    │   ├── Kein Luftzug spürbar → Lüfter defekt oder fehlend
    │   ├── Brandklappe geschlossen → Öffnen/Reparieren
    │   └── OK → Weiter
    │
    ├── Isolierung prüfen
    │   ├── Blockiert Luftwege → Umlegen
    │   ├── Fehlt → Installieren (Wärmereflektion statt -aufnahme)
    │   └── OK → Weiter
    │
    └── Motor prüfen
        ├── Kühlwasser-Temperatur zu hoch → Kühlsystem-Problem
        ├── Auspuff-Leck im Motorraum → Reparieren (GEFAHR!)
        └── Normale Motortemperatur → Belüftung verbessern
```

### 15.5 Troubleshooting-Entscheidungsbaum: Wellendichtungs-Leckage

```
Stopfbuchse/PSS leckt verstärkt
    ├── Leckrate bestimmen
    │   ├── Tropfende Stopfbuchse (1 Tropfen/5 Sek) → Normal
    │   ├── Verstärktes Tropfen → Alignment prüfen
    │   └── Fließendes Wasser → Sofort-Maßnahme!
    │
    ├── Alignment prüfen
    │   ├── Außerhalb Toleranz → Alignment-Problem (Motorlager!)
    │   └── Innerhalb Toleranz → Stopfbuchse/PSS selbst
    │
    ├── Stopfbuchse:
    │   ├── Packung nachziehen (1/6 Umdrehung)
    │   ├── Packung erneuern
    │   └── Welle auf Riefen prüfen
    │
    └── PSS (dripless):
        ├── Balgzustand prüfen (Risse, Elastizität)
        ├── Kohle-/Edelstahl-Ring auf Verschleiß prüfen
        └── Alignment: PSS toleriert weniger Fehl-Alignment als Stopfbuchse!
```

---
---

## 16. FAQ — Häufige Fragen

### FAQ 1: Wie oft müssen Motorlager gewechselt werden?

**Antwort:** Die Lebensdauer hängt stark von den Betriebsbedingungen ab.
Richtwerte:
- Standardmäßig: 8–12 Jahre oder 5.000–8.000 Betriebsstunden
- Bei optimalen Bedingungen (trocken, kühl, sauber): 12–15 Jahre
- Bei ungünstigen Bedingungen (Öl, Hitze, Bilgenwasser): 4–6 Jahre
- **Prüfkriterium:** Deflexion > 35 % über Neuwert → Austausch empfohlen

### FAQ 2: Kann ich nur ein einzelnes Motorlager tauschen?

**Antwort:** Nein — grundsätzlich immer alle 4 Lager gleichzeitig tauschen.
Unterschiedliche Elastomer-Steifigkeiten führen zu Alignment-Problemen
und ungleicher Lastverteilung. Ausnahme: Ein offensichtlich defektes
Lager (gebrochen) kann als Notmaßnahme einzeln getauscht werden,
aber das komplette Set sollte bei nächster Gelegenheit folgen.

### FAQ 3: OEM-Lager oder Aftermarket?

**Antwort:** OEM-Lager sind auf den spezifischen Motor abgestimmt und
bieten die Sicherheit der Herstellergarantie. Aftermarket-Lager (z.B.
Vetus K-Serie) sind eine gute Alternative, wenn Tragfähigkeit und
Shore-Härte korrekt gewählt werden. Preisersparnis: 20–40 %.
**Wichtig:** Bei Motoren unter Garantie immer OEM-Lager verwenden.

### FAQ 4: Weichere oder härtere Lager gegen Vibrationen?

**Antwort:** Kontraintuitiv: *weichere* Lager isolieren besser, machen
aber das Alignment instabiler. Härtere Lager sind stabiler, aber
vibrieren bei niedrigen Drehzahlen stärker.
- Segelboote (selten Motorbetrieb): eher weich (45–55 Shore A)
- Motoryachten (Dauerbetrieb): eher mittel (55–65 Shore A)
- Gleiter (Hochleistung): eher fest (60–70 Shore A)

### FAQ 5: Muss das Alignment bei Saildrive-Motoren geprüft werden?

**Antwort:** Nein — bei Saildrive-Motoren (Volvo 120S/130S, Yanmar SD)
ist der Antriebsstrang starr mit dem Motor verbunden. Es gibt keine
Wellenkupplung und somit kein Alignment im klassischen Sinne.
Motorlager dienen nur der Schwingungsisolation. Die Lager müssen
aber trotzdem auf Verschleiß geprüft werden.

### FAQ 6: Wie erkenne ich, ob mein Motorlager defekt ist?

**Antwort:** Die häufigsten Anzeichen:
- Stärkere Vibrationen als gewohnt, besonders im Leerlauf
- Motor steht sichtbar schief (Wasserwaage prüfen)
- Metallisches Klicken bei Gas geben/wegnehmen
- Wellendichtung leckt plötzlich stärker
- Sichtbare Risse im Gummikörper
- Motor hat sichtbar mehr Spiel als früher
- Alignment-Werte verschlechtert

### FAQ 7: Kann ich die Shore-Härte selbst messen?

**Antwort:** Ja, mit einem Shore-A-Durometer (Handgerät). Kosten:
30–150 € für ein einfaches Gerät. Messung am eingebauten Lager ist
allerdings schwierig — besser am ausgebauten Lager oder Reservelager.
Die Messung erfordert eine plane Fläche, mindestens 6 mm Materialdicke
und 3 Sekunden Verweilzeit. Praxisrelevanz: eher gering, da die
Deflexionsmessung aussagekräftiger ist.

### FAQ 8: Was kostet ein Motorlager-Austausch komplett?

**Antwort:** Richtwerte (inkl. Material und Arbeit):
- 4 Motorlager + Alignment-Prüfung: 400–800 € (Segelboot)
- 4 Motorlager + Alignment + Kupplung: 800–1.500 € (Segelboot)
- 4 Motorlager + Alignment: 600–1.200 € (Motoryacht)
- Mit Fundament-Nacharbeit: +500–2.000 €
- **DIY-Material:** 100–350 € (nur Lager)

### FAQ 9: Kann ich das Alignment selbst machen?

**Antwort:** Ja, mit der Fühlerblatt-Methode (Kapitel 7.3). Benötigt
wird: Stahllineal, Fühlerlehren-Set (zusammen ca. 30–50 €), Geduld
und Sorgfalt. Empfehlung: beim ersten Mal von einem Fachmann begleiten
lassen. Für die Messuhr-Methode ist mehr Erfahrung und eine Investition
von ca. 80–200 € (Messuhr + Halter) erforderlich.

### FAQ 10: Warum vibriert mein Motor nur im Leerlauf?

**Antwort:** Im Leerlauf ist die Erregerfrequenz am niedrigsten und
liegt oft nahe der Eigenfrequenz der Motorlager (Resonanz). Oberhalb
der Resonanzfrequenz isolieren die Lager zunehmend besser. Abhilfe:
weichere Lager (senken die Eigenfrequenz), Leerlaufdrehzahl leicht
erhöhen, oder kürzere Leerlaufphasen.

### FAQ 11: Ist Laser-Alignment bei meinem 10-m-Segelboot sinnvoll?

**Antwort:** Die Investition in ein Laser-Alignment-System (2.000–8.000 €)
lohnt sich für einen einzelnen Bootsbesitzer nicht. Die Fühlerblatt-
oder Messuhr-Methode ist für Segelboote vollkommen ausreichend. Sinnvoll
ist Laser-Alignment bei: Werften, die regelmäßig Motoren einbauen;
Motoryachten ab 15 m; und Repowering-Projekten an teuren Yachten.

### FAQ 12: Was passiert bei Grundberührung mit dem Alignment?

**Antwort:** Eine Grundberührung kann den Rumpf verformen und damit
die Stevenrohr-Position verändern. Dadurch verschiebt sich die
Wellenachse relativ zum Motor. **Immer** nach einer Grundberührung
das Alignment prüfen! Zusätzlich: Fundament auf Risse inspizieren,
Wellendichtung auf Leckage prüfen, Propeller auf Schäden.

### FAQ 13: Muss ich nach dem Kranen das Alignment prüfen?

**Antwort:** Ja, unbedingt. Der Rumpf verformt sich auf dem Kran oder
auf Böcken anders als im Wasser. Typisch: 0,5–5 mm Alignment-Änderung
zwischen „auf Böcken" und „im Wasser". Daher: Alignment immer im
Wasser (oder kurz nach dem Ablassen) durchführen.

### FAQ 14: Welches Werkzeug brauche ich für den Motorlager-Tausch?

**Antwort:** Grundausstattung:
- Gabelschlüssel 13 mm, 17 mm, 19 mm (je nach Lagergröße)
- Drehmomentschlüssel 10–80 Nm
- Fühlerlehren-Set
- Stahllineal (Haarlineal) 300 mm
- Schraubensicherung Loctite 243
- Rostlöser (WD-40 oder Caramba)
- Taschenlampe
- Spiegel (Teleskopspiegel)
- Optional: Hydraulik-Wagenheber (klein) zum Motoranheben

### FAQ 15: Kann ich statt flexiblen Lagern starre Lager einbauen?

**Antwort:** Technisch ja, praktisch nein. Starre Lagerung überträgt
100 % der Motorvibrationen in den Rumpf. Der Lärmpegel im Wohnbereich
wird unerträglich, die Rumpfstruktur ermüdet schneller, und die
Kupplung verschleißt rapide. Starre Lagerung nur bei Arbeitsbooten
ohne Wohnfunktion, historischen Restaurierungen oder als Notlösung.

### FAQ 16: Wie lagere ich Ersatz-Motorlager korrekt?

**Antwort:** Motorlager mit Elastomerkörper sollten:
- Trocken und dunkel gelagert werden (UV-Schutz)
- Temperaturbereich: 5–30 °C (nie unter 0 °C)
- Nicht in der Nähe von Ozon-Quellen (Elektromotoren, Schweißgeräte)
- Nicht in Kontakt mit Ölen, Lösungsmitteln oder Kraftstoffen
- Nicht unter Last lagern (verformt das Elastomer)
- Maximal 5 Jahre Lagerzeit (danach Shore-Härte prüfen)

### FAQ 17: Welches Drehmoment für Motorlager-Bolzen?

**Antwort:** Abhängig von Bolzengröße und Material:
- M10 Edelstahl A4-70: 35 Nm
- M12 Edelstahl A4-70: 60 Nm
- M16 Edelstahl A4-70: 120 Nm
- M20 Edelstahl A4-70: 200 Nm
Immer Herstellerangaben beachten! Schraubensicherung (Loctite 243)
verwenden.

### FAQ 18: Was ist der Unterschied zwischen Alignment und Balancing?

**Antwort:** Alignment = Ausrichtung der Motor-Wellen-Achse (Motor
relativ zur Welle). Balancing = Auswuchten rotierender Teile
(Schwungscheibe, Kupplung, Propeller). Beides verursacht Vibrationen,
aber die Ursachen und Maßnahmen sind grundverschieden. Alignment
wird mit Fühlerblatt/Messuhr/Laser geprüft, Balancing mit
Vibrationsmessgerät und Unwucht-Kompensation.

### FAQ 19: Kann ich mein Motorfundament selbst reparieren?

**Antwort:** Kleine Reparaturen (Haarrisse überlaminieren, Lagerplatten
nachlaminieren) sind für erfahrene Eigner machbar. Voraussetzung:
Erfahrung mit Epoxid-Laminat, geeignetes Material (Biax-Gelege,
Epoxidharz, Härter), und gute Belüftung. Strukturelle Reparaturen
(Stringer-Ablösung, großflächige Delamination) gehören in die Werft.

### FAQ 20: Wie wirkt sich die Bootskränkung (Segelboot) auf die Motorlager aus?

**Antwort:** Bei Krängung ändert sich die Lastverteilung auf die Lager:
die leeseitigen Lager tragen mehr, die luvseitigen weniger. Bei 25°
Krängung kann die Lastverschiebung 30–40 % betragen. Die Lager müssen
diese zyklische Belastung aushalten. Konsequenz: Segelboot-Motorlager
dürfen nicht knapp dimensioniert sein.

### FAQ 21: Was kostet eine professionelle Alignment-Prüfung?

**Antwort:** Richtwerte (Deutschland, 2025/2026):
- Fühlerblatt-Methode (Werft): 80–150 €
- Messuhr-Methode (Werft): 120–250 €
- Laser-Alignment (Spezialist): 250–500 €
- Alignment-Korrektur (ink. Prüfung): 200–600 €
- Alignment + Motorlager-Tausch: 500–1.200 €

### FAQ 22: Brauche ich nach dem Motorlager-Tausch ein neues Alignment?

**Antwort:** Ja, immer! Neue Lager haben eine andere Deflexion als die
alten. Auch wenn die gleiche Marke und Größe eingebaut wird, muss das
Alignment nach dem Tausch geprüft und ggf. korrigiert werden. Zudem
nach 50 Betriebsstunden Nachprüfung wegen Setzung der neuen Lager.

### FAQ 23: Können Motorvibrationen die Rumpfstruktur beschädigen?

**Antwort:** Ja, langfristig. Vibrationen verursachen Ermüdung im
GFK-Laminat und können zu Haarrissen und Delamination führen.
Besonders gefährdet: Stringeranbindungen, Schottverbindungen, und
Tankbefestigungen. Korrekte Motorlager und Alignment sind daher
auch ein Strukturschutz-Maßnahme.

### FAQ 24: Was ist Maschinensprache im Kontext von Motorlagerung?

**Antwort:** „Maschinensprache" ist der Oberbegriff für alle
Motor-Rumpf-Verbindungselemente: Motorlager, Fundamente, Kupplung,
Stevenrohr-Lager und deren Zubehör. Im angelsächsischen Raum als
„engine installation hardware" bezeichnet.

### FAQ 25: Wie dokumentiere ich den Zustand meiner Motorlager für AYDI?

**Antwort:** Für die AYDI-Analyse sind folgende Informationen optimal:
- Fotos aller 4 Lager (seitlich, zeigen Elastomer-Zustand)
- Marke und Typ der Lager (wenn lesbar)
- Alter der Lager (Einbaujahr)
- Letzte Alignment-Prüfung (Datum und Ergebnis)
- Deflexionsmessung (wenn möglich)
- Vibrations-Eindruck (subjektiv: keine/leicht/mittel/stark)
- Motorstunden seit letztem Lagertausch

---
---

## 17. Glossar

| Begriff | Erklärung |
|---------|----------|
| **Alignment** | Ausrichtung der Motor-Getriebe-Wellenachse mit der Stevenrohrachse. Toleranz typisch ±0,05 mm. |
| **Axiale Deflexion** | Verformung eines Motorlagers in Richtung der Welle (Schubrichtung). |
| **Bilge** | Tiefster Punkt im Rumpfinneren, wo sich Wasser sammelt. Motorlager sollen nicht im Bilgenwasser stehen. |
| **Constrained Layer Damping (CLD)** | Vibrationsdämpfung durch aufgeklebte Sandwich-Schicht (Metall-Visko-Metall) auf Rumpfplatten. |
| **Compression Set** | Druckverformungsrest — bleibende Verformung eines Elastomers nach Entlastung (in %). |
| **Deflexion** | Einfederung eines Motorlagers unter statischer Last (in mm). |
| **Dial Indicator** | Messuhr mit Skale und Zeiger, Auflösung 0,01 mm, für Alignment-Messung. |
| **Drucklager (Thrust Bearing)** | Lager, das den axialen Propellerschub aufnimmt. Meist im Getriebe integriert. |
| **Eigenfrequenz (f_n)** | Resonanzfrequenz des Motor-Lager-Systems. Muss deutlich unter der Erregerfrequenz liegen. |
| **Elastomer** | Gummiartiger Werkstoff (EPDM, NR, NBR) im Motorlager, der Schwingungen absorbiert. |
| **Engine Bed** | Motorfundament — die strukturelle Verbindung zwischen Motorlagern und Rumpf. |
| **EPDM** | Ethylen-Propylen-Dien-Monomer — Standard-Elastomer für marine Motorlager. |
| **Erregerfrequenz** | Schwingungsfrequenz, die der Motor durch Verbrennung und rotierende Massen erzeugt. |
| **Face Reading** | Alignment-Messung an der Flanschfläche (Winkelversatz). |
| **Fühlerblatt** | Dünnes Stahlblatt (0,02–1,0 mm) zur Spaltmessung beim Alignment. |
| **Flanschkupplung** | Verbindung zwischen Getriebe-Ausgangswelle und Propellerwelle über zwei Flansche mit Schrauben. |
| **Flexible Kupplung** | Wellenkupplung mit Elastomerelement (z.B. R&D Marine K-Prop), entkoppelt Vibrationen. |
| **GFK** | Glasfaserverstärkter Kunststoff — Standardmaterial für Yachtrümpfe und Fundamente. |
| **Haarlineal** | Stahllineal mit sehr hoher Genauigkeit (0,02 mm/m), für Alignment-Prüfung. |
| **Isolationsgrad** | Prozentsatz der Schwingungsenergie, der vom Motorlager absorbiert wird. |
| **K-Prop** | Flexible Wellenkupplung von R&D Marine, Industriestandard im Yachtbau. |
| **Körperschall** | Schwingungen, die über feste Strukturen (Fundament, Rumpf) übertragen werden. |
| **Laser-Alignment** | Alignment-Messung mit Laserstrahl und Positionsdetektoren. Genauigkeit ±0,005 mm. |
| **Luftschall** | Schwingungen, die über die Luft übertragen werden (Motorgeräusch). |
| **Mass Loaded Vinyl (MLV)** | Schwere, flexible Folie zur Schalldämmung. |
| **Motorfuß (Engine Foot)** | Befestigungspunkt am Motor, an dem das Motorlager verschraubt wird. |
| **Motorstringer** | Längsträger im Rumpf, die als Motorfundament dienen. |
| **Offset** | Radialer Versatz beim Alignment (parallele Achsverschiebung). |
| **Propellerschub** | Axialkraft, die der Propeller auf die Welle und damit auf den Antriebsstrang überträgt. |
| **PSS (Packless Sealing System)** | Tropffreie Wellendichtung (z.B. PYI PSS), empfindlich gegen Fehl-Alignment. |
| **Repowering** | Austausch des alten Motors gegen einen neuen (Motorumrüstung). |
| **Resonanz** | Zustand, in dem Erregerfrequenz = Eigenfrequenz. Massive Schwingungsverstärkung. |
| **Rim Reading** | Alignment-Messung am Flanschaußendurchmesser (radialer Versatz). |
| **Saildrive** | Antriebssystem, bei dem Motor und Antriebseinheit (S-Drive) starr verbunden sind und durch den Rumpfboden reichen. |
| **Schallbrücke** | Starre Verbindung, die die Schwingungsisolation umgeht. |
| **Shore A** | Härte-Skala für Elastomere (EPDM, Gummi). Marine-Motorlager: 40–70 Shore A. |
| **Silentblock** | Zylindrische Gummi-Metall-Buchse zur Schwingungsisolation. |
| **Stevenrohr** | Rohr im Rumpf, durch das die Propellerwelle nach außen geführt wird. |
| **Stopfbuchse** | Klassische Wellendichtung mit Packungsringen (PTFE/GFO). Leckt immer leicht. |
| **TIR (Total Indicated Runout)** | Gesamtanzeige der Messuhr bei einer vollen Umdrehung. TIR/2 = tatsächlicher Versatz. |
| **Transmissibilität** | Verhältnis übertragener zu eingeleiteter Schwingung. T < 1 = Isolation, T > 1 = Verstärkung. |
| **Zwangsbelüftung** | Motorraum-Belüftung mit Ventilator (bei geschlossenem Motorraum erforderlich). |

---
---

## 18. Schnell-Referenz

### 18.1 Motorlager-Auswahl in 5 Schritten

```
1. Motorgewicht (inkl. Getriebe, Anbauteile, Betriebsmittel) → G
2. Schwerster Lagerpunkt → G_max = G × 0,3 (bei 4 Lagern)
3. Sicherheitsfaktor → G_auslegung = G_max × 1,5
4. Lagergröße wählen: nächsthöhere Tragfähigkeit
5. Shore-Härte: Segel=50, Motor=60, Gleiter=65
```

### 18.2 Alignment-Schnellprüfung

```
1. Kupplung trennen
2. Fühlerlehre in Flanschspalt: 12, 3, 6, 9 Uhr
3. Alle Werte innerhalb ±0,05 mm → OK
4. Differenz > 0,05 mm → Nachjustierung erforderlich
```

### 18.3 Motorlager-Zustandsprüfung

```
1. Sichtprüfung: Risse? Ölkontamination? Korrosion?
2. Wackeltest: Motor seitlich drücken — Spiel?
3. Wasserwaage auf Motor: Schieflage?
4. Deflexion messen: > 35 % über Nennwert → Tausch
```

### 18.4 Motorraum-Belüftung Faustformel

```
Zuluft-Querschnitt (cm²) = Motorleistung (kW) × 28
Beispiel: 42 kW → 1.176 cm² → 4× Lüftungsgitter 300 cm²
```

### 18.5 Schallschutz-Prioritäten

```
1. Motorlager: richtige Shore-Härte, kein Verschleiß
2. Schallbrücken eliminieren: Auspuff, Kabel, Schläuche
3. Motorraum-Auskleidung: MLV + Schaum
4. Rumpfdämpfung: CLD auf resonierenden Platten
5. Schwimmender Boden: Kabinenboden entkoppeln
```

---
---

## 19. ANHANG A–H: Fallstudien

### ANHANG A — Fallstudie 1: Segelboot Bavaria 37, Motorlager-Probleme

**Boot:** Bavaria 37 Cruiser, Bj. 2008
**Motor:** Volvo D2-40 (29 kW), 2.200 Betriebsstunden
**Problem:** Zunehmende Vibrationen im Salon, besonders bei 1.800–2.200 U/min

**Untersuchung:**
- Motorlager Deflexion gemessen: Vorne links +42 %, vorne rechts +38 %,
  hinten links +28 %, hinten rechts +25 % über Nennwert
- Alignment: vertikaler Versatz 0,14 mm (Toleranz ±0,05 mm)
- Kupplung: Gummielemente sichtbar verschlissen
- Fundament: intakt, keine Risse

**Diagnose:**
Vorderen Motorlager stärker verschlissen (höhere Last durch
Schwerpunktlage). Daraus resultierendes Fehl-Alignment belastet
Kupplung und überträgt Vibrationen in den Rumpf.

**Maßnahme:**
1. Alle 4 Motorlager getauscht (Vetus K100 → Original Volvo 3809201)
2. Kupplung erneuert (R&D Marine K-Prop 2-2)
3. Alignment mit Messuhr: 0,03 mm radial, 0,04 mm/100mm axial
4. Nachprüfung nach 50 h: stabil bei 0,04 mm

**Kosten:** 620 € Material, 480 € Arbeit = 1.100 € gesamt
**Ergebnis:** Vibrationen vollständig beseitigt, Boot ruhiger als je zuvor

**AYDI-Bewertung:** Motorlager vorher 35/100, nachher 92/100

---

### ANHANG B — Fallstudie 2: Motoryacht Princess V42, Motorraum-Überhitzung

**Boot:** Princess V42, Bj. 2005, Doppelmotorisierung
**Motoren:** 2× Volvo D6-310 (je 228 kW), 1.800 Betriebsstunden
**Problem:** Motorraum-Temperatur über 70 °C bei Reisefahrt (28 kn)

**Untersuchung:**
- Zuluft-Öffnungen: 2× 200 cm² = 400 cm² gesamt
- Erforderlich: 2× 228 kW × 28 = 12.768 cm² (!)
- Abluft-Ventilatoren: 2× 350 m³/h (viel zu wenig)
- Schallschutz-Matten blockieren teilweise Luftwege
- Original-Brandschutzklappen: eine fehlt, eine klemmt

**Diagnose:**
Massive Unterdimensionierung der Motorraum-Belüftung. Die Werft hat
den Motorraum für Komfort (Geräusch) optimiert, dabei die thermischen
Anforderungen vernachlässigt.

**Maßnahme:**
1. Zuluftöffnungen vergrößert: 4× 800 cm² mit Schalldämpfer-Gittern
2. Abluft-Ventilatoren getauscht: 2× Sealand 2.500 m³/h
3. Schallschutzmatten korrekt verlegt (keine Blockade)
4. Brandschutzklappen ersetzt und getestet
5. Temperatur-Überwachung nachgerüstet (4× Sensor + Display)

**Kosten:** 4.200 € Material, 3.800 € Arbeit = 8.000 € gesamt
**Ergebnis:** Motorraum-Temperatur bei Reisefahrt: 52 °C (vorher 72 °C)

**AYDI-Bewertung:** Motorraum-Belüftung vorher 15/100, nachher 78/100

---

### ANHANG C — Fallstudie 3: Hallberg-Rassy 40, Repowering

**Boot:** Hallberg-Rassy 40 MkII, Bj. 1998
**Alter Motor:** Volvo MD2040 (28 kW), 7.500 Betriebsstunden
**Problem:** Motor unwirtschaftlich, Ersatzteile schwer beschaffbar

**Motorwahl:** Volvo D2-40 (29 kW) — Direkter Nachfolger

**Einbau:**
1. Fundament: Passt mit minimaler Anpassung (2 Bohrungen neu)
2. Motorlager: Volvo OEM 3809201 (4 Stück)
3. Wellenanlage: Propellerwelle übernommen, neue Kupplung (R&D Marine)
4. Abgas: Neuer Wassersammler, Schlauch teilweise erneuert
5. Elektrik: Neuer Kabelbaum Motor → Instrumententafel
6. Alignment: Laser (Fixturlaser), 0,02 mm radial

**Kosten:**
- Motor + Getriebe: 14.800 €
- Installation: 5.200 €
- Zubehör: 2.400 €
- Gesamt: 22.400 €

**Ergebnis:** Leiser, 15 % weniger Verbrauch, moderne Diagnose-Elektronik

**AYDI-Bewertung:** Motorinstallation 94/100

---

### ANHANG D — Fallstudie 4: Jeanneau Sun Odyssey 45, Fundament-Schaden

**Boot:** Jeanneau Sun Odyssey 45, Bj. 2007
**Motor:** Yanmar 4JH80 (59 kW)
**Problem:** Stringer-Ablösung nach Grundberührung in Griechenland

**Untersuchung:**
- Backbord-Stringer 200 mm auf 600 mm Länge vom Rumpf gelöst
- Motorlager backbord hinten: kein festes Auflager mehr
- Alignment: 0,35 mm radialer Versatz (!)
- Kupplung: massive Verschleißspuren
- Wellendichtung (PSS): undicht

**Reparatur:**
1. Motor ausgebaut (Kran über Niedergang)
2. Stringer-Ablösung: altes Laminat entfernt, Rumpf angeschliffen
3. Neues Laminat: 10 Lagen Biax-Gelege + Epoxid, 150 mm Flansch
4. Aushärtung: 72 h bei 22 °C
5. Stahlplatte für Motorlager einlaminiert
6. Motor eingebaut, neue Lager (Vetus K250)
7. Neue Kupplung, neue PSS-Dichtung
8. Alignment: 0,04 mm (Messuhr)

**Kosten:** 2.800 € Material, 4.500 € Arbeit = 7.300 €
**Ergebnis:** Fundament stärker als original

**AYDI-Bewertung:** Fundament vorher 8/100, nachher 88/100

---

### ANHANG E — Fallstudie 5: Bénéteau Oceanis 38, Saildrive-Vibration

**Boot:** Bénéteau Oceanis 38, Bj. 2014
**Motor:** Yanmar 3JH5E mit Saildrive SD60, 900 Betriebsstunden
**Problem:** Brummen im Achterschiff bei 2.200–2.800 U/min

**Untersuchung:**
- Saildrive-Motorlager: Deflexion normal (+12 % über Nennwert)
- Alignment: nicht relevant (Saildrive)
- Frequenzmessung: 68 Hz dominant bei 2.400 U/min
- Rumpfplatten-Test: Achterschiff-Boden resoniert bei 65–70 Hz
- Propeller: Sealine 3-Blatt, 15×11, original

**Diagnose:**
Rumpfplatten-Resonanz im Achterschiff bei Propeller-Flügelfrequenz
(3 Blatt × 2.400/60 = 120 Hz → Subharmonische bei 60 Hz erregt
Rumpfplatte).

**Maßnahme:**
1. Constrained Layer Damping (3M SJ-2015) auf Achterschiff-Boden
   innen (4 m²)
2. Verstärkungsrippe (GFK-Profil) quer auf Rumpfplatte
3. Alternativ-Versuch: 4-Blatt-Propeller (verschiebt Flügelfrequenz)

**Kosten:** CLD: 480 € + 300 € Arbeit = 780 €
**Ergebnis:** Brummen um 14 dB reduziert, kaum noch wahrnehmbar

**AYDI-Bewertung:** Vibration vorher 42/100, nachher 81/100

---

### ANHANG F — Fallstudie 6: Contest 46, Elektro-Repowering

**Boot:** Contest 46, Bj. 2003
**Alter Motor:** Volvo D2-55 (41 kW), 6.800 Betriebsstunden
**Neuer Antrieb:** Oceanvolt AXC30 (30 kW) + 40 kWh LiFePO4

**Besonderheiten Motorlagerung:**
- Elektromotor: 68 kg (vs. 340 kg Diesel + Getriebe)
- Neue Motorlager: Vetus K50 (weich, 45 Shore A)
- Fundament: vorhandenes Stahl-Stringer-Fundament gekürzt
- Adapter-Platte: Aluminium, CNC-gefräst für Oceanvolt-Befestigung
- Alignment: Oceanvolt-Welle → Propellerwelle, Messuhr, 0,03 mm
- Vibration: praktisch null — E-Motor hat keinen Massenkraftausgleich-
  Bedarf

**Batterieinstallation:**
- 40 kWh in 4 Modulen (je 10 kWh, je 55 kg)
- Montage auf ehemaligem Motorraum-Boden + unter Salon-Boden
- Belüftung: 2× 100 mm Kanal für LiFePO4-Entgasung

**Kosten:** 78.000 € (Motor, Batterien, Installation, Propeller)
**Ergebnis:** Lautlos bei Elektrobetrieb, 40 sm Reichweite bei 5 kn

**AYDI-Bewertung:** Motorinstallation 96/100 (Abzug: Reichweite begrenzt)

---

### ANHANG G — Fallstudie 7: Azimut 50, Alignment-Problem bei Doppelmotorisierung

**Boot:** Azimut 50, Bj. 2010
**Motoren:** 2× Volvo D6-370 (je 272 kW), IPS500
**Problem:** Vibrationen bei 22–25 kn, nur auf Steuerbord

**Untersuchung:**
- IPS-Pods: mechanisch in Ordnung
- Steuerbord-Motor Alignment (Motor → IPS): 0,09 mm radial
- Backbord-Motor: 0,03 mm
- Motorlager Steuerbord: Deflexion +32 % (Grenzbereich)
- Fundament Steuerbord: Haarriss am vorderen Stringer-Übergang

**Diagnose:**
Steuerbord-Fundament hat Haarriss, Motorlager sind an der
Verschleißgrenze, daraus resultiert Alignment-Verschlechterung.

**Maßnahme:**
1. Fundamentriss repariert (Überlaminierung, 8 Lagen)
2. Alle 8 Motorlager getauscht (4 pro Motor, Volvo OEM)
3. Beide Motoren neu ausgerichtet (Laser, je 0,02 mm)
4. Probefahrt: vibrationsfrei bis 32 kn

**Kosten:** 6.400 € (Material + Arbeit für beide Motoren)
**AYDI-Bewertung:** vorher 48/100, nachher 91/100

---

### ANHANG H — Fallstudie 8: Nauticat 38, Schallschutz-Komplettsanierung

**Boot:** Nauticat 38, Bj. 1996 (Motorsailer)
**Motor:** Ford Lehman 120 (90 kW), 4.500 Betriebsstunden
**Problem:** Unerträglicher Motorlärm im Salon (78 dB(A))

**Untersuchung:**
- Keine Schallisolierung im Motorraum
- Starre Auspuffverbindung (Stahlrohr direkt in GFK-Durchführung)
- Motorlager: Original 1996, Shore-Härte auf 72 Shore A ausgehärtet
- Keine flexible Kupplung (starre Flanschkupplung)
- Motorraum-Schotten: 6 mm GFK ohne Dämpfung

**Maßnahme (Komplettsanierung):**
1. Motorlager: 4× neue Poly-Flex PF-M300 (60 Shore A)
2. Kupplung: R&D Marine K-Prop 3-3 (flexible Kupplung)
3. Auspuff: Flexibler Edelstahl-Balg + Gummikompensator
4. Motorraum-Auskleidung: Soundown Insul-Sheet HD (38 mm) — 12 m²
5. Schott-Dämpfung: CLD auf beide Seiten Motorraum-Schotte — 8 m²
6. Schwimmender Salonboden über Motorraum: Kork-Elastomer-Pads — 6 m²
7. Alignment: Messuhr, 0,04 mm

**Schallmessung vorher/nachher:**

| Bereich | Vorher dB(A) | Nachher dB(A) | Reduktion |
|---------|-------------|-------------|----------|
| Motorraum | 108 | 105 | −3 dB |
| Salon (direkt) | 78 | 58 | −20 dB |
| Eignerkabine | 72 | 52 | −20 dB |
| Cockpit | 74 | 62 | −12 dB |

**Kosten:** 4.800 € Material, 3.200 € Arbeit = 8.000 €
**Ergebnis:** Salon bei Motorfahrt jetzt komfortabel, Unterhaltung möglich

**AYDI-Bewertung:** Schallschutz vorher 18/100, nachher 82/100

---
---

## 20. ANHANG I–R: Pydantic v2 Datenmodelle

### ANHANG I — Motorlager-Datenmodell

```python
"""
AYDI Motorlager-Datenmodelle — Pydantic v2
Alle Modelle verwenden model_config = {"from_attributes": True}
"""

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import date


class MountType(str, Enum):
    """Motorlager-Typ."""
    CYLINDRICAL = "cylindrical"
    CONICAL = "conical"
    DOUBLE_CONICAL = "double_conical"
    SILENT_BLOCK = "silent_block"
    RIGID = "rigid"
    HYDRAULIC = "hydraulic"
    ACTIVE = "active"


class MountPosition(str, Enum):
    """Position des Motorlagers."""
    FRONT_PORT = "front_port"
    FRONT_STARBOARD = "front_starboard"
    REAR_PORT = "rear_port"
    REAR_STARBOARD = "rear_starboard"


class MountCondition(str, Enum):
    """Zustand des Motorlagers."""
    NEW = "new"
    GOOD = "good"
    WORN = "worn"
    DAMAGED = "damaged"
    FAILED = "failed"


class ConfidenceLevel(str, Enum):
    """AYDI Confidence Level."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class EngineMountSpec(BaseModel):
    """Spezifikation eines Motorlagers."""
    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller des Motorlagers")
    model: str = Field(..., description="Modellbezeichnung")
    mount_type: MountType = Field(..., description="Lager-Typ")
    max_weight_kg: float = Field(..., ge=0, description="Maximale Tragfähigkeit pro Lager (kg)")
    shore_hardness: int = Field(..., ge=20, le=90, description="Shore-A-Härte")
    bolt_size_mm: int = Field(..., description="Befestigungsbolzen-Gewinde (mm)")
    deflection_mm: float = Field(..., ge=0, description="Nenn-Deflexion bei Volllast (mm)")
    price_eur: Optional[float] = Field(None, ge=0, description="Einzelpreis (EUR)")
    material: str = Field(default="EPDM", description="Elastomer-Material")
    weight_kg: Optional[float] = Field(None, ge=0, description="Eigengewicht des Lagers (kg)")


class EngineMountConditionReport(BaseModel):
    """Zustandsbericht eines eingebauten Motorlagers."""
    model_config = {"from_attributes": True}

    position: MountPosition = Field(..., description="Einbauposition")
    mount_spec: Optional[EngineMountSpec] = Field(None, description="Lager-Spezifikation")
    condition: MountCondition = Field(..., description="Zustandsbewertung")
    deflection_current_mm: Optional[float] = Field(None, ge=0, description="Aktuelle Deflexion (mm)")
    deflection_increase_pct: Optional[float] = Field(None, description="Deflexions-Zunahme gegenüber Nennwert (%)")
    oil_contamination: bool = Field(default=False, description="Ölkontamination festgestellt")
    visible_cracks: bool = Field(default=False, description="Sichtbare Risse im Elastomer")
    bolt_corrosion: bool = Field(default=False, description="Bolzenkorrosion festgestellt")
    installation_date: Optional[date] = Field(None, description="Einbaudatum")
    operating_hours: Optional[int] = Field(None, ge=0, description="Betriebsstunden seit Einbau")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level der Bewertung")
    notes: Optional[str] = Field(None, description="Anmerkungen")
    score: int = Field(..., ge=0, le=100, description="AYDI-Score (0–100)")


class EngineMountSetAssessment(BaseModel):
    """Bewertung eines kompletten Motorlager-Satzes (4 Lager)."""
    model_config = {"from_attributes": True}

    mounts: list[EngineMountConditionReport] = Field(
        ..., min_length=2, max_length=8, description="Einzelne Lagerbewertungen"
    )
    overall_condition: MountCondition = Field(..., description="Gesamtzustand")
    alignment_required: bool = Field(..., description="Alignment-Prüfung erforderlich")
    replacement_recommended: bool = Field(..., description="Austausch empfohlen")
    overall_score: int = Field(..., ge=0, le=100, description="Gesamtscore (0–100)")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level")
    findings: list[str] = Field(default_factory=list, description="Befunde (deutsch)")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen (deutsch)")
```

### ANHANG J — Alignment-Datenmodell

```python
class AlignmentMethod(str, Enum):
    """Alignment-Messmethode."""
    FEELER_GAUGE = "feeler_gauge"
    DIAL_INDICATOR = "dial_indicator"
    LASER = "laser"
    STRING = "string"
    VISUAL = "visual"


class AlignmentStatus(str, Enum):
    """Alignment-Bewertung."""
    WITHIN_TOLERANCE = "within_tolerance"
    BORDERLINE = "borderline"
    OUT_OF_TOLERANCE = "out_of_tolerance"
    NOT_ASSESSED = "not_assessed"


class AlignmentReading(BaseModel):
    """Einzelne Alignment-Messung an einer Uhr-Position."""
    model_config = {"from_attributes": True}

    position_clock: int = Field(..., ge=0, le=12, description="Uhr-Position (3, 6, 9, 12)")
    rim_value_mm: Optional[float] = Field(None, description="Rim-Messwert (radial, mm)")
    face_value_mm: Optional[float] = Field(None, description="Face-Messwert (axial, mm)")


class AlignmentMeasurement(BaseModel):
    """Vollständige Alignment-Messung."""
    model_config = {"from_attributes": True}

    measurement_date: date = Field(..., description="Messdatum")
    method: AlignmentMethod = Field(..., description="Messmethode")
    instrument: Optional[str] = Field(None, description="Verwendetes Messinstrument")
    readings: list[AlignmentReading] = Field(
        ..., min_length=4, max_length=8, description="Messwerte an Uhr-Positionen"
    )
    radial_offset_mm: float = Field(..., description="Radialer Versatz (mm)")
    angular_offset_mm_per_100mm: float = Field(..., description="Winkelversatz (mm/100mm)")
    tolerance_radial_mm: float = Field(default=0.05, description="Toleranz radial (mm)")
    tolerance_angular_mm: float = Field(default=0.05, description="Toleranz angular (mm/100mm)")
    status: AlignmentStatus = Field(..., description="Bewertung")
    correction_performed: bool = Field(default=False, description="Korrektur durchgeführt")
    post_correction_radial_mm: Optional[float] = Field(None, description="Versatz nach Korrektur")
    post_correction_angular_mm: Optional[float] = Field(None, description="Winkel nach Korrektur")
    next_check_hours: Optional[int] = Field(None, description="Nächste Prüfung nach X Betriebsstunden")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level")
    score: int = Field(..., ge=0, le=100, description="AYDI-Score (0–100)")
```

### ANHANG K — Motorfundament-Datenmodell

```python
class FoundationType(str, Enum):
    """Typ des Motorfundaments."""
    GFK_STRINGER = "gfk_stringer"
    STEEL_STRINGER = "steel_stringer"
    ALUMINUM_BED = "aluminum_bed"
    HARDWOOD_BED = "hardwood_bed"
    COMPOSITE = "composite"
    SAILDRIVE_FRAME = "saildrive_frame"


class FoundationCondition(str, Enum):
    """Zustand des Motorfundaments."""
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"


class EngineFoundationAssessment(BaseModel):
    """Bewertung des Motorfundaments."""
    model_config = {"from_attributes": True}

    foundation_type: FoundationType = Field(..., description="Fundament-Typ")
    material_thickness_mm: Optional[float] = Field(None, ge=0, description="Materialstärke (mm)")
    surface_flatness_mm: Optional[float] = Field(None, ge=0, description="Ebenheit (mm Abweichung)")
    stringer_attachment: str = Field(..., description="Art der Stringer-Anbindung")
    corrosion_protection: str = Field(..., description="Korrosionsschutz")
    bolt_plate_material: Optional[str] = Field(None, description="Material der Lagerplatten")
    cracks_detected: bool = Field(default=False, description="Risse festgestellt")
    delamination_detected: bool = Field(default=False, description="Delamination festgestellt")
    moisture_ingress: bool = Field(default=False, description="Feuchtigkeitseintritt")
    condition: FoundationCondition = Field(..., description="Gesamtzustand")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level")
    score: int = Field(..., ge=0, le=100, description="AYDI-Score (0–100)")
    findings: list[str] = Field(default_factory=list, description="Befunde (deutsch)")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen (deutsch)")
```

### ANHANG L — Schallschutz-Datenmodell

```python
class SoundInsulationMaterial(BaseModel):
    """Schallisolationsmaterial."""
    model_config = {"from_attributes": True}

    product_name: str = Field(..., description="Produktname")
    manufacturer: str = Field(..., description="Hersteller")
    thickness_mm: float = Field(..., ge=0, description="Dicke (mm)")
    db_reduction: float = Field(..., ge=0, description="dB-Reduktion")
    fire_rating: str = Field(..., description="Brandklasse")
    price_per_sqm_eur: Optional[float] = Field(None, ge=0, description="Preis pro m² (EUR)")
    area_installed_sqm: Optional[float] = Field(None, ge=0, description="Installierte Fläche (m²)")


class SoundLevelMeasurement(BaseModel):
    """Schallpegelmessung."""
    model_config = {"from_attributes": True}

    location: str = Field(..., description="Messort (z.B. 'Salon', 'Eignerkabine')")
    engine_rpm: int = Field(..., ge=0, description="Motordrehzahl bei Messung")
    db_a: float = Field(..., description="Schallpegel dB(A)")
    measurement_device: Optional[str] = Field(None, description="Messgerät")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level")


class SoundInsulationAssessment(BaseModel):
    """Bewertung der Schallisolation."""
    model_config = {"from_attributes": True}

    materials_installed: list[SoundInsulationMaterial] = Field(
        default_factory=list, description="Installierte Materialien"
    )
    measurements: list[SoundLevelMeasurement] = Field(
        default_factory=list, description="Schallpegelmessungen"
    )
    sound_bridges_identified: list[str] = Field(
        default_factory=list, description="Identifizierte Schallbrücken"
    )
    overall_rating: str = Field(..., description="Gesamtbewertung (exzellent/gut/ausreichend/mangelhaft)")
    score: int = Field(..., ge=0, le=100, description="AYDI-Score (0–100)")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level")
    findings: list[str] = Field(default_factory=list, description="Befunde (deutsch)")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen (deutsch)")
```

### ANHANG M — Motorraum-Belüftung-Datenmodell

```python
class VentilationType(str, Enum):
    """Belüftungstyp."""
    NATURAL = "natural"
    FORCED = "forced"
    COMBINED = "combined"


class EngineRoomVentilationAssessment(BaseModel):
    """Bewertung der Motorraum-Belüftung."""
    model_config = {"from_attributes": True}

    engine_power_kw: float = Field(..., ge=0, description="Motorleistung (kW)")
    ventilation_type: VentilationType = Field(..., description="Belüftungstyp")
    intake_area_sqcm: float = Field(..., ge=0, description="Zuluft-Querschnitt (cm²)")
    intake_area_required_sqcm: float = Field(..., ge=0, description="Erforderlicher Zuluft-Querschnitt (cm²)")
    exhaust_area_sqcm: Optional[float] = Field(None, ge=0, description="Abluft-Querschnitt (cm²)")
    fan_capacity_m3h: Optional[float] = Field(None, ge=0, description="Lüfterleistung (m³/h)")
    fire_dampers_installed: bool = Field(default=False, description="Brandschutzklappen vorhanden")
    fire_dampers_functional: Optional[bool] = Field(None, description="Brandschutzklappen funktionsfähig")
    max_temperature_celsius: Optional[float] = Field(None, description="Maximal gemessene Temperatur (°C)")
    temperature_rating: str = Field(default="not_measured", description="Temperaturbewertung")
    ventilation_sufficient: bool = Field(..., description="Belüftung ausreichend")
    score: int = Field(..., ge=0, le=100, description="AYDI-Score (0–100)")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level")
    findings: list[str] = Field(default_factory=list, description="Befunde (deutsch)")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen (deutsch)")
```

### ANHANG N — Repowering-Datenmodell

```python
class RepoweringType(str, Enum):
    """Typ der Motorumrüstung."""
    DIESEL_TO_DIESEL = "diesel_to_diesel"
    DIESEL_TO_ELECTRIC = "diesel_to_electric"
    DIESEL_TO_HYBRID = "diesel_to_hybrid"
    GASOLINE_TO_DIESEL = "gasoline_to_diesel"
    OTHER = "other"


class RepoweringAssessment(BaseModel):
    """Bewertung einer Motorumrüstung."""
    model_config = {"from_attributes": True}

    repowering_type: RepoweringType = Field(..., description="Typ der Umrüstung")
    old_engine: str = Field(..., description="Alter Motor (Hersteller + Modell)")
    new_engine: str = Field(..., description="Neuer Motor (Hersteller + Modell)")
    foundation_compatible: bool = Field(..., description="Fundament kompatibel")
    foundation_modification_required: str = Field(
        default="none", description="Erforderliche Fundament-Anpassung"
    )
    shaft_compatible: bool = Field(..., description="Wellenanlage kompatibel")
    estimated_cost_eur: float = Field(..., ge=0, description="Geschätzte Gesamtkosten (EUR)")
    estimated_duration_days: int = Field(..., ge=1, description="Geschätzte Dauer (Tage)")
    complexity: str = Field(..., description="Komplexität (einfach/mittel/komplex)")
    score: int = Field(..., ge=0, le=100, description="AYDI-Score (Machbarkeit, 0–100)")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level")
    findings: list[str] = Field(default_factory=list, description="Befunde (deutsch)")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen (deutsch)")
```

### ANHANG O — Gesamtbewertung Motorinstallation

```python
class EngineInstallationAssessment(BaseModel):
    """Gesamtbewertung der Motorinstallation (AYDI-Hauptmodell)."""
    model_config = {"from_attributes": True}

    # Teilbewertungen
    mount_assessment: Optional[EngineMountSetAssessment] = Field(
        None, description="Motorlager-Bewertung"
    )
    alignment_assessment: Optional[AlignmentMeasurement] = Field(
        None, description="Alignment-Bewertung"
    )
    foundation_assessment: Optional[EngineFoundationAssessment] = Field(
        None, description="Fundament-Bewertung"
    )
    sound_assessment: Optional[SoundInsulationAssessment] = Field(
        None, description="Schallschutz-Bewertung"
    )
    ventilation_assessment: Optional[EngineRoomVentilationAssessment] = Field(
        None, description="Belüftungs-Bewertung"
    )

    # Gesamtergebnis
    overall_score: int = Field(..., ge=0, le=100, description="Gesamtscore (0–100)")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level (niedrigstes der Teilbewertungen)")
    critical_findings: list[str] = Field(
        default_factory=list, description="Kritische Befunde (deutsch)"
    )
    warnings: list[str] = Field(
        default_factory=list, description="Warnungen (deutsch)"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen, priorisiert (deutsch)"
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Reparaturkosten (EUR)"
    )

    # Score-Gewichtung
    score_weights: dict[str, float] = Field(
        default={
            "mounts": 0.25,
            "alignment": 0.25,
            "foundation": 0.20,
            "sound": 0.15,
            "ventilation": 0.15,
        },
        description="Gewichtung der Teilbewertungen"
    )
```

### ANHANG P — Visual-Analyse Motorlager-Prompt

```python
ENGINE_MOUNT_VISUAL_PROMPT = """
Analysiere das Foto eines Motorlagers in einer Yacht.

Prüfe folgende Aspekte:
1. ELASTOMER-ZUSTAND: Risse, Verformung, Ausquetschung, Ölkontamination
2. BOLZEN-ZUSTAND: Korrosion, Verfärbung, Gewindezustand
3. DEFLEXION: Ist der Motor sichtbar eingesunken?
4. FUNDAMENT: Sichtbare Risse, Delamination, Verschmutzung
5. SCHALLBRÜCKEN: Starre Verbindungen zwischen Motor und Rumpf

Antworte auf Deutsch.

Bewertung:
- Score 0-100 (100 = Neuzustand)
- Confidence: visual_high (klares Foto, eindeutig) / visual_medium
  (erkennbar, einige Unsicherheit) / visual_low (schlecht erkennbar)
  / visual_insufficient (nicht beurteilbar)

Wenn nicht beurteilbar: sage "nicht beurteilbar" und erkläre warum.

Format:
{
  "zustand": "gut/verschlissen/defekt/nicht_beurteilbar",
  "score": 0-100,
  "confidence": "visual_high/visual_medium/visual_low/visual_insufficient",
  "befunde": ["..."],
  "empfehlungen": ["..."]
}
"""
```

### ANHANG Q — Visual-Analyse Alignment-Prompt

```python
ENGINE_ALIGNMENT_VISUAL_PROMPT = """
Analysiere das Foto einer Motor-Wellen-Kupplung in einer Yacht.

Prüfe folgende Aspekte:
1. FLANSCH-AUSRICHTUNG: Sichtbarer Versatz oder Winkelfehler
2. KUPPLUNG-ZUSTAND: Gummielemente, Verschleißmarken, Beschädigungen
3. BOLZEN: Korrosion, Anzugsmarkierungen, fehlende Bolzen
4. WELLE: Sichtbarer Schlag, Korrosion, Beschädigungen
5. ALLGEMEINER EINDRUCK: Sauberkeit, Wartungszustand

Antworte auf Deutsch.

Bewertung:
- Score 0-100 (100 = perfekt ausgerichtet, neuwertig)
- Confidence: visual_high / visual_medium / visual_low / visual_insufficient

Wenn nicht beurteilbar: sage "nicht beurteilbar".

Format:
{
  "zustand": "gut/grenzwertig/schlecht/nicht_beurteilbar",
  "score": 0-100,
  "confidence": "...",
  "befunde": ["..."],
  "empfehlungen": ["..."]
}
"""
```

### ANHANG R — Confidence-Mapping für Motorinstallation

```python
ENGINE_INSTALLATION_CONFIDENCE_MAP = {
    "mounts": {
        "measured": [
            "Deflexion mit Messuhr gemessen",
            "Shore-Härte mit Durometer geprüft",
            "Alle 4 Lager einzeln gemessen und bewertet"
        ],
        "visual_high": [
            "Klares Foto, Elastomer-Zustand eindeutig erkennbar",
            "Risse, Ölkontamination, Korrosion sichtbar/ausgeschlossen"
        ],
        "visual_medium": [
            "Foto erkennbar, aber nicht alle Lager sichtbar",
            "Beleuchtung eingeschränkt, Winkel suboptimal"
        ],
        "estimated": [
            "Lager-Alter und Betriebsstunden geschätzt",
            "Zustand aus Motortyp und Bootsklasse abgeleitet"
        ]
    },
    "alignment": {
        "measured": [
            "Messuhr-Messung mit 0,01 mm Auflösung",
            "Laser-Alignment mit Protokoll"
        ],
        "visual_high": [
            "Flanschversatz visuell eindeutig erkennbar (> 0,5 mm)",
            "Kupplungsverschleiß eindeutig sichtbar"
        ],
        "estimated": [
            "Letzte Alignment-Prüfung > 2 Jahre",
            "Alignment-Status aus Vibrations-Symptomen geschätzt"
        ]
    },
    "foundation": {
        "measured": [
            "Klopfprüfung durchgeführt",
            "Feuchtemessung durchgeführt",
            "Oberflächen-Ebenheit gemessen"
        ],
        "visual_high": [
            "Klares Foto, Risse/Delamination eindeutig erkennbar",
            "Fundament von mehreren Seiten fotografiert"
        ],
        "estimated": [
            "Fundament-Typ aus Bootsmodell abgeleitet",
            "Zustand aus Baujahr und Klasse geschätzt"
        ]
    },
    "sound": {
        "measured": [
            "dB(A)-Messung mit kalibriertem Schallpegelmesser",
            "Messungen an mehreren Positionen und Drehzahlen"
        ],
        "visual_medium": [
            "Foto zeigt installierte Schallisolierung",
            "Material erkennbar, Flächenanteil schätzbar"
        ],
        "estimated": [
            "Schallschutz-Bewertung aus Motortyp und Bootsklasse",
            "Eigner-Angabe zu subjektivem Lärmpegel"
        ]
    },
    "ventilation": {
        "measured": [
            "Temperaturmessung mit IR-Thermometer",
            "Luftstrom-Messung mit Anemometer",
            "Querschnittsmessung der Öffnungen"
        ],
        "visual_high": [
            "Lüftungsöffnungen klar fotografiert",
            "Ventilator-Typ und -Zustand erkennbar"
        ],
        "estimated": [
            "Belüftung aus Motorleistung und Öffnungsanzahl geschätzt"
        ]
    }
}
```

---
---

## ANHANG S — Erweiterte Cross-Referenz: Bootshersteller → Motor → Lager

### S.1 Bavaria (Deutschland)

| Modell | Baujahr | Motor | OEM-Lager | Empfehlung Aftermarket |
|--------|---------|-------|----------|----------------------|
| Bavaria 34 | 2005–2012 | Volvo D1-30 | 3809201 | Vetus K75 |
| Bavaria 37 | 2006–2014 | Volvo D2-40 | 3809201 | Vetus K100 |
| Bavaria 40 | 2008–2016 | Volvo D2-55 | 3809202 | Vetus K130 |
| Bavaria 44 | 2005–2010 | Volvo D2-75 | 3809203 | Vetus K160 |
| Bavaria 46 | 2010–2018 | Volvo D2-75 | 3809203 | Vetus K160 |
| Bavaria 50 | 2007–2014 | Volvo D3-110 | 3809300 | Vetus K250 |
| Bavaria C42 | 2018– | Volvo D2-40 | 3809201 | Vetus K100 |
| Bavaria C45 | 2019– | Volvo D2-60 | 3809202 | Vetus K130 |
| Bavaria C57 | 2017– | Volvo D3-110 | 3809300 | Vetus K250 |

### S.2 Hanse (Deutschland)

| Modell | Baujahr | Motor | OEM-Lager | Empfehlung Aftermarket |
|--------|---------|-------|----------|----------------------|
| Hanse 315 | 2016– | Yanmar 3JH40 | 129670-08310 | Vetus K130 |
| Hanse 348 | 2017– | Yanmar 3JH40 | 129670-08310 | Vetus K130 |
| Hanse 388 | 2018– | Yanmar 3JH5E | 129670-08350 | Vetus K130 |
| Hanse 418 | 2018– | Yanmar 4JH57 | 129670-08330 | Vetus K200 |
| Hanse 458 | 2019– | Yanmar 4JH57 | 129670-08330 | Vetus K200 |
| Hanse 508 | 2018– | Yanmar 4JH80 | 129670-08340 | Vetus K250 |
| Hanse 548 | 2020– | Yanmar 4JH80 | 129670-08340 | Vetus K250 |
| Hanse 588 | 2020– | Yanmar 4JH110 | 129670-08360 | Vetus K300 |
| Hanse 675 | 2017– | Volvo D3-150 | 3809301 | Vetus K300 |

### S.3 Jeanneau (Frankreich)

| Modell | Baujahr | Motor | OEM-Lager | Empfehlung Aftermarket |
|--------|---------|-------|----------|----------------------|
| Sun Odyssey 319 | 2017– | Yanmar 3JH40 | 129670-08310 | Vetus K130 |
| Sun Odyssey 349 | 2015– | Yanmar 3JH40 | 129670-08310 | Vetus K130 |
| Sun Odyssey 380 | 2020– | Yanmar 3JH5E | 129670-08350 | Vetus K130 |
| Sun Odyssey 410 | 2019– | Yanmar 4JH45 | 129670-08321 | Vetus K160 |
| Sun Odyssey 440 | 2018– | Yanmar 4JH57 | 129670-08330 | Vetus K200 |
| Sun Odyssey 490 | 2018– | Yanmar 4JH80 | 129670-08340 | Vetus K250 |
| Sun Odyssey 519 | 2016– | Yanmar 4JH80 | 129670-08340 | Vetus K250 |

### S.4 Bénéteau (Frankreich)

| Modell | Baujahr | Motor | OEM-Lager | Empfehlung Aftermarket |
|--------|---------|-------|----------|----------------------|
| Océanis 30.1 | 2019– | Yanmar 3JH40 | 129670-08310 | Vetus K130 |
| Océanis 34.1 | 2020– | Yanmar 3JH40 | 129670-08310 | Vetus K130 |
| Océanis 38.1 | 2017– | Yanmar 3JH5E | 129670-08350 | Vetus K130 |
| Océanis 40.1 | 2019– | Yanmar 4JH45 | 129670-08321 | Vetus K160 |
| Océanis 46.1 | 2017– | Yanmar 4JH57 | 129670-08330 | Vetus K200 |
| Océanis 51.1 | 2017– | Yanmar 4JH80 | 129670-08340 | Vetus K250 |

### S.5 Hallberg-Rassy (Schweden)

| Modell | Baujahr | Motor | OEM-Lager | Empfehlung Aftermarket |
|--------|---------|-------|----------|----------------------|
| HR 310 | 2009– | Volvo D1-30 | 3809201 | R&D Marine RDM-100 |
| HR 340 | 2003– | Volvo D2-40 | 3809201 | R&D Marine RDM-150 |
| HR 372 | 2002– | Volvo D2-55 | 3809202 | R&D Marine RDM-150 |
| HR 400 | 2006– | Volvo D2-55 | 3809202 | R&D Marine RDM-200 |
| HR 412 | 2014– | Volvo D2-60 | 3809202 | R&D Marine RDM-200 |
| HR 44 | 2003– | Volvo D2-75 | 3809203 | R&D Marine RDM-200 |
| HR 48 MkII | 2008– | Volvo D3-110 | 3809300 | R&D Marine RDM-300 |
| HR 55 | 2006– | Volvo D3-150 | 3809301 | R&D Marine RDM-450 |
| HR 57 | 2012– | Volvo D3-150 | 3809301 | R&D Marine RDM-450 |
| HR 64 | 2009– | Volvo D3-170 | 3809302 | R&D Marine RDM-450 |

### S.6 Najad (Schweden)

| Modell | Baujahr | Motor | OEM-Lager | Empfehlung Aftermarket |
|--------|---------|-------|----------|----------------------|
| Najad 355 | 2004– | Volvo D2-40 | 3809201 | R&D Marine RDM-150 |
| Najad 395 | 2002– | Volvo D2-55 | 3809202 | R&D Marine RDM-200 |
| Najad 440 | 2005– | Volvo D2-75 | 3809203 | R&D Marine RDM-200 |
| Najad 505 | 2000– | Volvo D3-110 | 3809300 | R&D Marine RDM-300 |
| Najad 570 | 2003– | Volvo D3-150 | 3809301 | R&D Marine RDM-450 |

### S.7 Contest (Niederlande)

| Modell | Baujahr | Motor | OEM-Lager | Empfehlung Aftermarket |
|--------|---------|-------|----------|----------------------|
| Contest 36S | 2010– | Volvo D2-40 | 3809201 | Vetus K100 |
| Contest 42CS | 2008– | Volvo D2-55 | 3809202 | Vetus K130 |
| Contest 46CS | 2005– | Volvo D2-75 | 3809203 | Vetus K160 |
| Contest 50CS | 2007– | Volvo D3-110 | 3809300 | Vetus K250 |
| Contest 55CS | 2004– | Volvo D3-150 | 3809301 | Vetus K300 |
| Contest 62CS | 2009– | Volvo D3-170 | 3809302 | Vetus K300 |

### S.8 Oyster (UK)

| Modell | Baujahr | Motor | OEM-Lager | Empfehlung Aftermarket |
|--------|---------|-------|----------|----------------------|
| Oyster 475 | 2010– | Volvo D2-75 | 3809203 | R&D Marine RDM-200 |
| Oyster 545 | 2008– | Volvo D3-110 | 3809300 | R&D Marine RDM-300 |
| Oyster 565 | 2012– | Volvo D3-150 | 3809301 | R&D Marine RDM-450 |
| Oyster 595 | 2009– | Volvo D3-150 | 3809301 | R&D Marine RDM-450 |
| Oyster 675 | 2011– | Volvo D3-170 | 3809302 | R&D Marine RDM-600 |
| Oyster 745 | 2013– | Volvo D4-210 | 3809400 | R&D Marine RDM-600 |
| Oyster 885 | 2014– | Volvo D4-260 | 3809401 | R&D Marine RDM-900 |

---
---

## ANHANG T — Wartungsplanung Motorinstallation

### T.1 Saisonale Wartungscheckliste

**Vor Saisonstart (Frühling):**

| Nr. | Prüfpunkt | Methode | Dauer | Werkzeug |
|-----|-----------|---------|-------|----------|
| 1 | Motorlager Sichtprüfung | Visuell + Taschenlampe | 10 min | Lampe, Spiegel |
| 2 | Motorlager Wackeltest | Motor seitlich drücken | 5 min | Keines |
| 3 | Motor-Wasserwaage | Wasserwaage auf Ventildeckel | 2 min | Wasserwaage |
| 4 | Motorlager-Bolzen Anzug | Drehmoment-Prüfung | 15 min | Drehmomentschlüssel |
| 5 | Alignment Schnellprüfung | Fühlerblatt an Kupplung | 20 min | Fühlerlehren, Lineal |
| 6 | Kupplung Sichtprüfung | Visuell | 5 min | Lampe |
| 7 | Fundament Sichtprüfung | Visuell + Klopfen | 10 min | Lampe, kleiner Hammer |
| 8 | Schallschutz-Matten | Visuell, auf Ablösung/Öl | 5 min | Lampe |
| 9 | Motorraum-Belüftung | Lüftungsgitter frei? | 5 min | Keines |
| 10 | Brandschutzklappen | Funktion prüfen | 5 min | Keines |
| 11 | Motorraum-Temperatur | Probelauf, IR-Thermometer | 15 min | IR-Thermometer |
| 12 | Bilge unter Motor | Öl? Wasser? Korrosion? | 5 min | Lampe |

**Gesamtdauer:** ca. 100 Minuten für gewissenhaften Eigner

**Vor Winterlager (Herbst):**

| Nr. | Prüfpunkt | Methode | Anmerkung |
|-----|-----------|---------|----------|
| 1 | Motorlager Sichtprüfung | Visuell | Zustand dokumentieren (Foto) |
| 2 | Bilge unter Motor reinigen | Pumpe + Reiniger | Ölfilm entfernen |
| 3 | Motorraum trocknen | Lüften, Entfeuchter | Keine stehendes Wasser |
| 4 | Korrosionsschutz Bolzen | WD-40 oder LPS 3 | Dünn auftragen |
| 5 | Lüftungsöffnungen offen lassen | Dorade-Boxen offen | Kondensat vermeiden |
| 6 | Motorabdeckung (optional) | Stoffhülle | Nicht luftdicht! |

### T.2 Intervall-Wartung nach Betriebsstunden

| Betriebsstunden | Maßnahme | Wer |
|----------------|----------|-----|
| 50 (nach Erstmontage) | Alignment-Nachprüfung | Werft/Eigner |
| 200 (nach Erstmontage) | Alignment-Nachprüfung | Werft/Eigner |
| 500 (jährlich) | Motorlager Sichtprüfung + Alignment | Eigner |
| 1.000 | Deflexionsmessung alle 4 Lager | Werft/Eigner |
| 2.000 | Vollständige Inspektion Motorinstallation | Werft |
| 3.000 | Deflexionsmessung, ggf. Alignment-Korrektur | Werft |
| 5.000 | Motorlager-Tausch prüfen (Deflexion bewerten) | Werft |
| 5.000–8.000 | Motorlager-Tausch empfohlen | Werft |

### T.3 Ersatzteil-Empfehlung an Bord

Für Langfahrt-Segler und Offshore-Yachten:

| Teil | Anzahl | Begründung | Gewicht |
|------|--------|-----------|---------|
| Motorlager (Satz 4×) | 1 Satz | Lager kann plötzlich reißen | 2–8 kg |
| Befestigungsbolzen (M12/M16) | 4 Stück | Korrosion, Bruch | 0,5 kg |
| Muttern + Scheiben | 8 Stück | Für Bolzen | 0,2 kg |
| Loctite 243 | 1 Tube | Schraubensicherung | 0,05 kg |
| Fühlerlehren-Set | 1 Set | Alignment-Prüfung | 0,1 kg |
| Edelstahl-Unterlegscheiben | 8 Stück | Höhenanpassung, Shims | 0,1 kg |

**Gesamtgewicht:** ca. 3–9 kg — vertretbar für Langfahrt

---
---

## ANHANG U — Berechnungsformeln Zusammenfassung

### U.1 Motorlager-Dimensionierung

```
Gewicht pro Lager (symmetrisch):
  G_lager = G_gesamt / n_lager

Gewicht pro Lager (mit Schwerpunkt):
  G_vorne = (d_hinten / L_gesamt) × G_gesamt / 2
  G_hinten = (d_vorne / L_gesamt) × G_gesamt / 2

Auslegungsgewicht:
  G_auslegung = G_lager × SF
  (SF = 1,3 Küste, 1,5 See, 2,0 Arbeit)
```

### U.2 Eigenfrequenz und Isolation

```
Eigenfrequenz:
  f_n = (1 / 2π) × √(k / m)  [Hz]

Erregerfrequenz (Viertakt):
  f_err = (n × z) / (2 × 60)  [Hz]
  n = Drehzahl [U/min], z = Zylinderzahl

Transmissibilität:
  T = 1 / |1 − (f/f_n)²|

Isolationsgrad:
  I = (1 − T) × 100 %

Effektive Isolation nur wenn f/f_n > √2 ≈ 1,41
```

### U.3 Motorraum-Belüftung

```
Verbrennungsluft:
  Q_verb = P_kW × 7  [m³/h]

Kühlluft:
  Q_kühl = (P_kW × 0,4 × 3.600) / (1,2 × 1.005 × ΔT)  [m³/h]

Zuluft-Querschnitt:
  A = Q / (v × 3.600)  [m²]
  v = 5–8 m/s (Strömungsgeschwindigkeit)

Faustformel:
  A_cm² ≈ P_kW × 28
```

### U.4 Propellerschub

```
Schub:
  F = P / (v × η_p)  [N]
  P = Leistung [W]
  v = Geschwindigkeit [m/s]
  η_p = Propellerwirkungsgrad (0,4–0,6)
```

### U.5 Deflexions-Zustandsbewertung

```
Deflexions-Zunahme:
  Δ% = (d_aktuell − d_nenn) / d_nenn × 100

Bewertung:
  0–10 %:  Neuwertig
  10–20 %: Normal eingelaufen
  20–35 %: Gealtert
  35–50 %: Verschlissen → Austausch empfohlen
  > 50 %:  Defekt → Sofortiger Austausch
```

---
---

## ANHANG V — Bezugsquellen und Lieferanten

### V.1 Deutschland

| Händler | Ort | Sortiment | Webshop |
|---------|-----|----------|---------|
| SVB (Segelversand Berlin) | Bremen | Vetus, Allpa, OEM | svb24.de |
| Compass24 | Bremen | Vetus, Allpa, diverse | compass24.de |
| Toplicht | Hamburg | Vetus, R&D Marine | toplicht.de |
| Bukh Bremen | Bremen | Bukh, diverse | bukh-bremen.de |
| Volvo Penta Händlernetz | Bundesweit | Volvo OEM | volvopenta.com |
| Yanmar Marine Händlernetz | Bundesweit | Yanmar OEM | yanmarmarine.eu |
| Marineshop24 | Flensburg | Aftermarket, Vetus | marineshop24.de |

### V.2 Niederlande

| Händler | Ort | Sortiment | Webshop |
|---------|-----|----------|---------|
| Vetus Direct | Schiedam | Vetus komplett | vfrancais.vetus.com |
| Allpa Marine | Emmeloord | Allpa Eigenmarke | allpa.nl |
| Bootmaterialen.nl | Breda | Diverse Aftermarket | bootmaterialen.nl |

### V.3 UK

| Händler | Ort | Sortiment | Webshop |
|---------|-----|----------|---------|
| R&D Marine | Fareham | R&D Marine komplett | rdmarine.co.uk |
| Halyard Marine | Colchester | Schallschutz, Isolation | halyardmarine.com |
| Tek-Tanks/Beta Marine | Gloucester | Beta OEM-Lager | betamarine.co.uk |
| Marine Parts Direct | Southampton | Diverse OEM + Aftermarket | marinepartsdirect.co.uk |
| Soundown UK | — | Schallschutz komplett | soundown.com |

### V.4 Online-Spezialisten

| Anbieter | Spezialgebiet | Region |
|----------|-------------|--------|
| dfrancais.vfrancais.com | Vetus Vollsortiment | EU |
| boat-parts.de | OEM-Referenz Aftermarket | DE |
| marineparts.eu | Multi-Hersteller-Suche | EU |
| marinedieselparts.com | Motor-Ersatzteile | Weltweit |
| rbmarineelectrics.co.uk | Marine-Zubehör | UK |

---
---

## ANHANG W — Zusätzliche FAQ (26–40)

### FAQ 26: Gibt es Motorlager speziell für Aluminium-Yachten?

**Antwort:** Standardmäßig werden die gleichen Elastomerlager wie bei
GFK-Yachten verwendet. Der Unterschied liegt in der Befestigung:
Bei Aluminium-Yachten werden die Lager direkt auf die Aluminium-Stringer
geschraubt (Gewinde in Aluminium oder Durchgangsbolzen). Wichtig:
Isolierbuchsen zwischen Edelstahl-Bolzen und Aluminium verwenden
(galvanische Korrosion!). Tef-Gel oder Duralac auf alle Kontaktflächen.

### FAQ 27: Können Motorlager „zu weich" sein?

**Antwort:** Ja. Zu weiche Lager verursachen:
- Übermäßige Motorauslenkung bei Schubreaktionen
- Instabiles Alignment (Motor wandert)
- Gefahr des Aufschwingens bei Resonanz
- Kupplung und Wellendichtung leiden
Faustregel: Statische Deflexion sollte 6 mm nicht überschreiten.

### FAQ 28: Wie wirkt sich ein defektes Motorlager auf den Kraftstoffverbrauch aus?

**Antwort:** Indirekt. Ein defektes Lager verursacht Fehl-Alignment,
das wiederum Reibung in Kupplung und Wellendichtung erhöht. Der
Mehrverbrauch beträgt typisch 2–5 %. Zusätzlich kann Vibration den
Propellerwirkungsgrad verschlechtern (Kavitation durch Wellenvibrationen).

### FAQ 29: Was tun bei Motorlager-Schaden auf See?

**Notmaßnahmen:**
1. Drehzahl reduzieren (minimale Vibration)
2. Defektes Lager inspizieren (gebrochen? gelöst?)
3. Wenn möglich: Motor auf intakten Lagern weiterlaufen lassen
4. Provisorisch: Hartholzklotz oder Gummimatte unter Motor schieben
5. Nächsten Hafen anlaufen, Lager tauschen
6. NICHT mit stark defektem Alignment weiterfahren (Getriebeschaden!)

### FAQ 30: Wie messe ich Vibrationen ohne Spezialgerät?

**Einfache Methoden:**
- Smartphone-App (z.B. „Vibration Meter"): misst Beschleunigung in m/s²
- Wasserglas-Test: Glas Wasser auf Salon-Tisch, Wellenmuster beobachten
- Münz-Test: Münze hochkant auf Motor stellen — fällt sie um?
- Subjektiv: Handauflegen auf verschiedene Oberflächen, Stärke vergleichen

**Bewertung (Smartphone-Messung am Motorblock):**
- < 5 m/s²: gut
- 5–15 m/s²: akzeptabel
- 15–30 m/s²: erhöht, Ursache suchen
- > 30 m/s²: stark, Maßnahme erforderlich

### FAQ 31: Motorlager im Winter frostgefährdet?

**Antwort:** EPDM-Elastomere sind frostbeständig bis −40 °C. Das Lager
selbst nimmt keinen Schaden. Allerdings wird das Elastomer bei Frost
deutlich härter (siehe Kapitel 5.5), und der erste Motorstart nach
Frost erzeugt verstärkte Vibrationen, bis sich das Lager erwärmt hat.
Das ist normal und kein Zeichen für einen Defekt.

### FAQ 32: Können Ratten oder Mäuse Motorlager beschädigen?

**Antwort:** Ja, Nagetiere knabbern an Gummiteilen. EPDM ist zwar
kein bevorzugtes Material, aber bei Nahrungsknappheit (Winterlager)
werden auch Motorlager angefressen. Schutz: Motorraum-Zugänge im
Winterlager sichern (Stahlwolle in Öffnungen), Rattenfallen/-köder.

### FAQ 33: Wie beeinflusst die Motortemperatur das Alignment?

**Antwort:** Ein warmer Motor dehnt sich aus. Typisch: 0,1–0,3 mm
vertikale Verschiebung zwischen kalt und betriebswarm (80 °C). Bei
präzisionsempfindlichen Anlagen (Superyachten) wird das Alignment
im warmen Zustand gemessen. Für die meisten Yachten ist der Effekt
vernachlässigbar, da die Motorlager-Elastomere die thermische Dehnung
aufnehmen.

### FAQ 34: Kann ich Motorlager verschiedener Hersteller mischen?

**Antwort:** Grundsätzlich nein. Alle 4 Lager sollten vom gleichen
Hersteller und Typ sein, um gleichmäßige Steifigkeit und Setzverhalten
zu gewährleisten. Eine Ausnahme: Wenn vorne härtere Lager als hinten
eingesetzt werden (wegen der höheren Frontlast), aber dies muss
berechnet sein und ist eine Spezialanwendung.

### FAQ 35: Gibt es Motorlager mit integrierter Höhenverstellung?

**Antwort:** Ja, einige Systeme bieten Spindel-Höhenverstellung:
- Vetus MH-Serie: Spindelmechanismus unter dem Elastomer
- R&D Marine Adjustable Mount: Gewinde-Verstellung
- Custom-Lösungen: Scherenwagenheber-Prinzip
Vorteil: Alignment-Nachjustierung ohne Motorausbau. Nachteil: Komplexer,
teurer, und die Spindel kann korrodieren.

### FAQ 36: Wie dokumentiere ich den Motorlager-Tausch für die AYDI-Datenbank?

**Antwort:** Folgende Daten erfassen:
- Datum des Tauschs
- Alte Lager: Hersteller, Modell, Alter, Betriebsstunden
- Neue Lager: Hersteller, Modell, Shore-Härte, Tragfähigkeit
- Alignment vor Tausch (Messwerte)
- Alignment nach Tausch (Messwerte)
- Alignment-Methode (Fühlerblatt/Messuhr/Laser)
- Fotos (alte Lager, neue Lager eingebaut, Alignment-Flansch)
- Kosten (Material + Arbeit)

### FAQ 37: Was ist ein „soft foot" beim Alignment?

**Antwort:** „Soft foot" bezeichnet den Zustand, wenn einer der vier
Motorfüße nicht plan auf dem Fundament aufliegt. Beim Festziehen dieses
Fußes verziehen sich die anderen — das Alignment ändert sich. Ursache:
unebenes Fundament, verzogener Motorfuß, ungleiche Shims.
Prüfung: Alle 4 Bolzen festziehen, dann jeden einzeln lösen und mit
Fühlerlehre prüfen, ob sich ein Spalt öffnet (> 0,05 mm = soft foot).

### FAQ 38: Welche Auswirkung hat die Propellergröße auf die Motorlagerung?

**Antwort:** Ein größerer Propeller erzeugt mehr Schub und damit höhere
axiale Kräfte auf die Motorlager. Zusätzlich verändert sich die
Flügelfrequenz (die Drehzahl sinkt bei größerem Propeller), was die
Vibrations-Anregung verschiebt. Nach einem Propellerwechsel: Alignment
prüfen und Vibrationsverhalten beobachten.

### FAQ 39: Können Motorlager recycelt werden?

**Antwort:** Die Metallteile (Stahl, Edelstahl) können recycelt werden.
Das Elastomer (EPDM, Natur-Kautschuk) kann thermisch verwertet oder
zu Gummigranulat recycelt werden. Ölkontaminierte Lager sind
Sondermüll (Altölverordnung). In der Praxis: bei der Werft entsorgen
lassen, die kennt die lokalen Regelungen.

### FAQ 40: Gibt es eine App zur Motorlager-Diagnose?

**Antwort:** Smartphone-Apps können Vibrationen messen (Beschleunigungssensor)
und als erste Indikation dienen. Dedizierte Apps:
- Vibration Meter (iOS/Android): Grundlegende Vibrationsmessung
- SKF QuickCollect: Professionelle Vibrations-Analyse
- Fixturlaser Alignment App: Bluetooth-Kopplung mit Laser-System
- AYDI Schnellanalyse: Foto-Upload für visuelle Bewertung (Level 1)

Keine App ersetzt eine professionelle Alignment-Messung oder
Deflexionsprüfung. Apps sind gut für Trendbeobachtung und
Ersteinschätzung.

---

*Ende der Wissensdatei 18_10 — Motorlager, Einbau und Ausrichtung*
*AYDI Maritime Knowledge Base v2.0 — Stand April 2026*
*Confidence-Quelle: measured (Hersteller-TDS, Messdaten), documented (Normen, Fachliteratur), estimated (Erfahrungswerte, Branchendaten)*
