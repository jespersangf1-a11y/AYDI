# 22.03 — Kabel und Leitungen im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 22.03** — Kategorie 22: Elektrik und Verkabelung
> **Confidence-Quelle:** measured (Hersteller-TDS, ABYC E-11, ISO 13297), documented (Hersteller-Kataloge, Forum-Konsens), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-05-03

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien und Spezifikationen](#4-produktlinien-und-spezifikationen)
5. [Hersteller-Datenbank](#5-hersteller-datenbank)
6. [Fehlerbild-Atlas](#6-fehlerbild-atlas)
7. [Troubleshooting-Entscheidungsbäume](#7-troubleshooting-entscheidungsbäume)
8. [FAQ — Häufige Fragen](#8-faq--häufige-fragen)
9. [Glossar](#9-glossar)
10. [Schnell-Referenz](#10-schnell-referenz)
11. [ANHANG A–H — Fallstudien](#anhang-a--fallstudien)
12. [ANHANG I–R — AYDI-Integration (Pydantic v2 Modelle)](#anhang-i--aydi-integration-pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Kabel als Schwachstelle Nr. 1

Kabel und Leitungen bilden das Nervensystem einer jeden Yacht. Statistisch gesehen sind fehlerhafte oder unsachgemäß installierte Kabel die **häufigste Ursache für Bordelektrik-Ausfälle** und — in schwerwiegenden Fällen — für Brände an Bord. Die BoatUS Marine Insurance Schadensstatistik weist seit Jahren elektrische Defekte als **Top-3-Brandursache** auf Sportbooten und Yachten aus. Die ABYC (American Boat and Yacht Council) dokumentierte in ihrem 2024-Bericht, dass über 60% aller elektrischen Mängel bei Gebrauchtbooten auf folgende Kabel-Probleme zurückzuführen sind:

- **Falsche Querschnitte** (Spannungsabfall >10%, Überhitzung)
- **Nicht-verzinntes Kupfer** in Salzwasserumgebung (Korrosion, Grünspan, erhöhter Widerstand)
- **Mangelhafte Verbindungen** (lose Klemmen, kalte Lötstellen, offene Crimpungen)
- **Fehlende oder beschädigte Isolierung** (Kurzschluss, Erdschluss)
- **Unzureichende Zugentlastung** (Kabelbruch durch Vibration)
- **Ungeeignete Kabeltypen** (Automobil-Kabel statt Marine-Grade)

**Confidence:** documented — basierend auf BoatUS Claims Data, ABYC Technical Reports, Pantaenius Schadensberichte.

### 1.2 ABYC E-11 — Die Bibel der Marine-Elektrik

Der ABYC Standard E-11 „AC and DC Electrical Systems on Boats" ist der maßgebliche Industriestandard für die Planung, Installation und Wartung elektrischer Systeme auf Booten. Er wird von der US Coast Guard referenziert und ist de facto weltweit anerkannt. Zentrale Grundsätze:

**Grundprinzip 1: Spannungsabfall minimieren**
- Maximal **3%** Spannungsabfall für kritische Verbraucher (Navigation, Bilgenpumpe, Funk)
- Maximal **10%** Spannungsabfall für nicht-kritische Verbraucher (Beleuchtung, Steckdosen)
- Berechnung über Kabellänge (Hin- UND Rückleiter!), Querschnitt und Stromstärke

**Grundprinzip 2: Strombelastbarkeit (Ampacity)**
- Jedes Kabel muss den maximal möglichen Dauerstrom ohne Überhitzung führen können
- Umgebungstemperatur, Bündelungsfaktor und Verlegeart bestimmen die Belastbarkeit
- Absicherung muss kleiner sein als die Kabelbelastbarkeit

**Grundprinzip 3: Marine-Eignung**
- Nur verzinntes Kupfer (tinned copper) für alle Verbindungen
- Nur Isolierungsmaterialien, die für den Marineeinsatz zugelassen sind
- Alle Verbindungen müssen gegen Feuchtigkeit geschützt sein
- Kabel müssen gegen mechanische Beschädigung, Vibration und UV-Strahlung geschützt werden

**Grundprinzip 4: Farbcodierung**
- DC-Positiv (ungeschaltet): Rot
- DC-Negativ/Masse: Schwarz oder Gelb
- AC-Phase (L): Schwarz (USA) / Braun (EU/IEC)
- AC-Neutral (N): Weiß (USA) / Blau (EU/IEC)
- Schutzleiter (PE): Grün oder Grün/Gelb

### 1.3 Europäische Normung: ISO 13297

Für Boote, die in der EU verkauft werden, ist **ISO 13297** „Elektrische Systeme — Wechselstrom-Installationen" maßgeblich. In Verbindung mit **ISO 10133** (Gleichstromsysteme) bilden diese Standards das europäische Pendant zum ABYC E-11. Wesentliche Unterschiede:

| Aspekt | ABYC E-11 (USA) | ISO 13297/10133 (EU) |
|--------|-----------------|---------------------|
| Querschnittsangabe | AWG (American Wire Gauge) | mm² |
| Max. Spannungsabfall (kritisch) | 3% | 3% (identisch) |
| Max. Spannungsabfall (nicht-kritisch) | 10% | 10% (identisch) |
| Farbcode DC-Positiv | Rot | Rot |
| Farbcode DC-Negativ | Schwarz oder Gelb | Schwarz |
| Farbcode AC | Schwarz/Weiß/Grün (USA) | Braun/Blau/Grün-Gelb (IEC) |
| Erdungssystem | Grün | Grün-Gelb |
| Kabeltyp-Anforderung | UL-listed marine | CE-konform |
| Prüfzeichen | UL, ABYC | CE, VDE, LPCB |

### 1.4 Weitere relevante Standards

| Standard | Thema | Relevanz |
|----------|-------|----------|
| ISO 10133:2012 | DC-Systeme auf Booten | Gleichstrom-Verkabelung |
| ISO 13297:2014 | AC-Systeme auf Booten | Wechselstrom-Verkabelung |
| IEC 60529 | Schutzarten durch Gehäuse (IP-Code) | IP-Schutzklassen |
| IEC 60092 | Elektrische Anlagen auf Schiffen | Referenzstandard für Yachten >24m |
| ABYC E-11 | AC/DC Electrical Systems | US-Industriestandard |
| ABYC E-2 | Cathodic Protection | Korrosionsschutz-Erdung, Bonding |
| NMEA 0183 | Serielles Datenprotokoll | Kabelanforderungen für Seekarten/GPS |
| NMEA 2000 | CAN-Bus Netzwerk | Spezifische Kabel (DeviceNet Micro-C) |
| DIN VDE 0100-706 | Leitende Bereiche mit begrenzter Bewegungsfreiheit | Elektrische Anlagen in engen Räumen |
| GL/DNV Rules | Klassifikationsgesellschaften | Yachten >24m, Superyachten |

### 1.5 Kabel im Kontext der Yachtklassen

Die Anforderungen an Kabel und Leitungen variieren erheblich je nach Bootsklasse:

**Produktions-Segelboot (8–14m, 80.000–300.000 EUR):**
- Kabelmenge: 300–800m gesamt
- DC-System: 12V (kleine Boote) oder 12V/24V (>12m)
- AC-System: 230V Landstrom, selten Generator
- Typische Verbraucher: Navigation, Beleuchtung, Kühlschrank, Ankerwinde, Autopilot
- Kabelqualität: Marine-Grade Minimum, verzinntes Kupfer Standard
- Budget für Verkabelung: 3–5% des Gesamtpreises

**Semi-Custom Cruiser (12–20m, 300.000–1.500.000 EUR):**
- Kabelmenge: 1.500–4.000m gesamt
- DC-System: 12V + 24V, oft Lithium-Batterien
- AC-System: 230V Landstrom + Generator (6–12 kW), Inverter
- Typische Verbraucher: Klimaanlage, Wassermacher, Bugstrahlruder, umfangreiche Elektronik
- Kabelqualität: Marine-Grade Premium, alle Verbindungen gecrimpt mit doppelter Wandstärke
- Budget für Verkabelung: 4–7% des Gesamtpreises

**Custom/Superyacht (18m+, 1.500.000+ EUR):**
- Kabelmenge: 5.000–50.000m gesamt
- DC-System: 24V + 48V, Lithium mit BMS
- AC-System: 230V/400V, mehrere Generatoren (20–200 kW), Shore-Power-Konverter
- Typische Verbraucher: Vollklimatisierung, Stabilisatoren, Tender-Kran, Entertainment-Systeme
- Kabelqualität: Lloyd's/DNV-zertifiziert, alle Kabel flammenresistent (IEC 60332)
- Budget für Verkabelung: 5–10% des Gesamtpreises

### 1.6 Überblick der Schwachstellen-Zonen

Bestimmte Bereiche auf einer Yacht sind für Kabelschäden besonders anfällig:

| Zone | Belastungsfaktoren | Typische Ausfälle | Risiko |
|------|-------------------|-------------------|--------|
| Masttop | UV, Vibration, Feuchtigkeit, Wind | Kabelbruch, Isolationsriss, Stecker-Korrosion | KRITISCH |
| Mastfuß-Durchführung | Biegung, Wasser, Kompression | Kabelbruch, Kurzschluss, Kriechstrom | KRITISCH |
| Motorraum | Hitze, Vibration, Öl, Kraftstoffdämpfe | Isolationsversprödung, lose Klemmen | HOCH |
| Bilge | Wasser, Feuchtigkeit, Salz | Korrosion, Erdschluss, Grünspan | HOCH |
| Ruderschaft-Bereich | Feuchtigkeit, Biegung | Korrosion, Kabelbruch | MITTEL |
| Ankerkette-Kasten | Wasser, Schlag, Salzaerosol | Korrosion, mechanische Beschädigung | MITTEL |
| Decksdurchführungen | UV, Wasser, Biegung | Leckage, Isolationsschaden, Kabelbruch | HOCH |
| Cockpit-Konsole | UV, Spritzwasser, Vibration | Stecker-Korrosion, Ermüdungsbruch | MITTEL |
| Backskiste | Feuchtigkeit, Salzwasser | Korrosion, Kurzschluss | MITTEL |
| Salon-Bereich | Trocken, wenig Belastung | Selten — günstigste Zone | GERING |

---

## 2. Grundlagen und Theorie

### 2.1 Querschnittsberechnung — Spannungsabfall

Die korrekte Dimensionierung von Kabelquerschnitten ist die fundamentalste Aufgabe bei der Planung einer Yacht-Elektrik. Zwei Kriterien bestimmen den Mindestquerschnitt:

1. **Maximal zulässiger Spannungsabfall** (voltage drop)
2. **Maximal zulässige Strombelastbarkeit** (ampacity)

Der größere der beiden berechneten Querschnitte wird gewählt.

#### 2.1.1 Spannungsabfall-Formel

```
A = (2 × L × I × ρ) / (U_nenn × %V_drop / 100)
```

Wobei:
- **A** = erforderlicher Querschnitt in mm²
- **L** = einfache Kabellänge in Metern (Hin-Weg)
- **I** = Strom in Ampere
- **ρ** = spezifischer Widerstand des Leiters (Kupfer bei 20°C: 0,0175 Ω·mm²/m)
- **U_nenn** = Nennspannung des Systems in Volt
- **%V_drop** = maximal zulässiger Spannungsabfall in Prozent

**Faktor 2**: Der Spannungsabfall entsteht auf Hin- UND Rückleiter. Daher die Verdopplung der Kabellänge in der Formel. Bei negativer Rückleitung über den Bootskörper (z.B. Stahlboote mit Masseverbindung) entfällt der Faktor 2 — **aber dies ist auf GFK/Holzbooten NICHT zulässig!**

#### 2.1.2 Berechnungsbeispiel 12V-System

**Szenario:** Ankerwinde, 80A bei Volllast, 12V-System, 12m Kabelweg (einfach), max. 3% Spannungsabfall (kritischer Verbraucher)

```
A = (2 × 12m × 80A × 0,0175) / (12V × 0,03)
A = 33,6 / 0,36
A = 93,3 mm²
→ Nächster Standardquerschnitt: 95 mm²
```

**Gegenprobe Spannungsabfall:**
```
V_drop = (2 × 12m × 80A × 0,0175) / 95 mm²
V_drop = 33,6 / 95
V_drop = 0,354 V
%V_drop = 0,354 / 12 × 100 = 2,95% ✓ (unter 3%)
```

#### 2.1.3 Berechnungsbeispiel 24V-System

**Szenario:** Bugstrahlruder, 200A bei Volllast, 24V-System, 15m Kabelweg, max. 3% Spannungsabfall

```
A = (2 × 15m × 200A × 0,0175) / (24V × 0,03)
A = 105 / 0,72
A = 145,8 mm²
→ Nächster Standardquerschnitt: 150 mm² (oder 2× 95 mm² parallel)
```

#### 2.1.4 Spannungsabfall-Tabelle für 12V-Systeme (3% max.)

| Strom (A) | 3m | 5m | 8m | 10m | 12m | 15m | 20m |
|-----------|------|------|------|------|------|------|------|
| 5 | 1,5 | 2,5 | 4 | 4 | 6 | 6 | 10 |
| 10 | 2,5 | 4 | 6 | 10 | 10 | 16 | 16 |
| 15 | 4 | 6 | 10 | 16 | 16 | 25 | 25 |
| 20 | 6 | 10 | 16 | 16 | 25 | 25 | 35 |
| 25 | 6 | 10 | 16 | 25 | 25 | 35 | 50 |
| 30 | 10 | 16 | 25 | 25 | 35 | 50 | 50 |
| 40 | 10 | 16 | 25 | 35 | 50 | 50 | 70 |
| 50 | 16 | 25 | 35 | 50 | 50 | 70 | 95 |
| 60 | 16 | 25 | 50 | 50 | 70 | 70 | 95 |
| 80 | 25 | 35 | 50 | 70 | 95 | 95 | 120 |
| 100 | 25 | 50 | 70 | 95 | 95 | 120 | 150 |
| 120 | 35 | 50 | 70 | 95 | 120 | 150 | 185 |
| 150 | 35 | 70 | 95 | 120 | 150 | 185 | 240 |
| 200 | 50 | 95 | 120 | 150 | 185 | 240 | 2×150 |

*Werte in mm² — aufgerundet auf nächsten Standardquerschnitt (1,5 / 2,5 / 4 / 6 / 10 / 16 / 25 / 35 / 50 / 70 / 95 / 120 / 150 / 185 / 240)*

#### 2.1.5 Spannungsabfall-Tabelle für 24V-Systeme (3% max.)

| Strom (A) | 3m | 5m | 8m | 10m | 12m | 15m | 20m |
|-----------|------|------|------|------|------|------|------|
| 5 | 1,5 | 1,5 | 1,5 | 2,5 | 2,5 | 4 | 4 |
| 10 | 1,5 | 2,5 | 4 | 4 | 6 | 6 | 10 |
| 15 | 2,5 | 2,5 | 4 | 6 | 6 | 10 | 10 |
| 20 | 2,5 | 4 | 6 | 6 | 10 | 10 | 16 |
| 25 | 4 | 4 | 6 | 10 | 10 | 16 | 16 |
| 30 | 4 | 6 | 10 | 10 | 16 | 16 | 25 |
| 40 | 6 | 10 | 10 | 16 | 16 | 25 | 25 |
| 50 | 6 | 10 | 16 | 16 | 25 | 25 | 35 |
| 80 | 10 | 16 | 25 | 25 | 35 | 50 | 50 |
| 100 | 16 | 25 | 25 | 35 | 50 | 50 | 70 |
| 150 | 16 | 25 | 50 | 50 | 70 | 70 | 95 |
| 200 | 25 | 35 | 50 | 70 | 95 | 95 | 120 |

> ⚠️ **ZU PRÜFEN (Audit):** Widerspruch zum Rechenbeispiel 2.1.3 — dort ergibt 200 A / 15 m / 24 V nach der Formel aus 2.1.1 **150 mm²**, diese Tabelle nennt für dieselbe Kombination **95 mm²**. Bei 95 mm² beträgt der Spannungsabfall ≈4,6 % und überschreitet damit das für diese Tabelle angegebene 3-%-Kriterium. Die 200-A-Zeile (und einzelne Zellen der 12-V-Tabelle in 2.1.4, z. B. 200 A / 15 m = 240 mm² statt rechnerisch ~300 mm²) erscheinen gegenüber der dokumenteigenen Formel unterdimensioniert. Diese Tabellenwerte für hohe Ströme sind **estimated — unverifiziert** und vor sicherheitsrelevanter Verwendung mit der Formel aus 2.1.1 nachzurechnen. Maßgeblich ist im Zweifel die Formel/das Rechenbeispiel.

### 2.2 Strombelastbarkeit (Ampacity)

Die Strombelastbarkeit eines Kabels wird durch die maximale Leitertemperatur begrenzt, die das Isolationsmaterial verträgt, ohne zu degradieren. Die zulässige Stromstärke hängt ab von:

- **Leiterquerschnitt** — größerer Querschnitt = geringerer Widerstand = weniger Erwärmung
- **Isolationsmaterial** — PVC (70°C), PE (90°C), XLPE (90°C), Silikon (180°C)
- **Umgebungstemperatur** — höhere Umgebungstemperatur reduziert die Belastbarkeit
- **Bündelungsfaktor** — gebündelte Kabel können Wärme schlechter abführen
- **Verlegeart** — in freier Luft vs. in Kabelkanal vs. in Rohr

#### 2.2.1 Strombelastbarkeit bei 30°C Umgebungstemperatur (Einzelverlegung, PVC-Isolation)

| Querschnitt (mm²) | AWG Äquivalent | Dauerstrom (A) | Kurzzeitstrom 30min (A) |
|--------------------|---------------|----------------|------------------------|
| 0,75 | 18 | 6 | 8 |
| 1,0 | 16 | 10 | 13 |
| 1,5 | 16 | 15 | 20 |
| 2,5 | 14 | 20 | 27 |
| 4 | 12 | 27 | 36 |
| 6 | 10 | 35 | 47 |
| 10 | 8 | 50 | 67 |
| 16 | 6 | 65 | 87 |
| 25 | 4 | 85 | 114 |
| 35 | 2 | 105 | 140 |
| 50 | 1/0 | 130 | 174 |
| 70 | 2/0 | 165 | 220 |
| 95 | 3/0 | 200 | 267 |
| 120 | 4/0 | 230 | 307 |
| 150 | 300 MCM | 260 | 347 |
| 185 | 350 MCM | 300 | 400 |
| 240 | 500 MCM | 350 | 467 |

#### 2.2.2 Bündelungsfaktor (Derating)

Wenn mehrere Kabel gebündelt verlegt werden, reduziert sich die zulässige Strombelastbarkeit:

| Anzahl Kabel im Bündel | Bündelungsfaktor |
|-------------------------|-----------------|
| 1–3 | 1,00 |
| 4–6 | 0,80 |
| 7–9 | 0,70 |
| 10–12 | 0,65 |
| 13–16 | 0,60 |
| 17–20 | 0,57 |
| >20 | 0,50 |

**Berechnung:**
```
I_zulässig = I_Tabelle × Bündelungsfaktor
```

**Beispiel:** 10 mm² Kabel (50A Tabellenwert), 8 Kabel im Bündel:
```
I_zulässig = 50A × 0,70 = 35A
```

#### 2.2.3 Temperaturkorrektur

Die Tabellenwerte gelten für 30°C Umgebungstemperatur. Im Motorraum einer Yacht können 50–70°C herrschen:

| Umgebungstemperatur | Korrekturfaktor PVC (70°C) | Korrekturfaktor XLPE (90°C) | Korrekturfaktor Silikon (180°C) |
|--------------------|---------------------------|----------------------------|-------------------------------|
| 25°C | 1,06 | 1,04 | 1,01 |
| 30°C | 1,00 | 1,00 | 1,00 |
| 35°C | 0,94 | 0,96 | 0,99 |
| 40°C | 0,87 | 0,91 | 0,98 |
| 45°C | 0,79 | 0,87 | 0,97 |
| 50°C | 0,71 | 0,82 | 0,96 |
| 55°C | 0,61 | 0,76 | 0,95 |
| 60°C | 0,50 | 0,71 | 0,94 |
| 65°C | — | 0,65 | 0,93 |
| 70°C | — | 0,58 | 0,92 |
| 80°C | — | 0,41 | 0,90 |

**Beispiel Motorraum:** 10 mm² Kabel (50A Tabellenwert), PVC-Isolation, 55°C Motorraum, 6 Kabel im Bündel:
```
I_zulässig = 50A × 0,61 (Temperatur) × 0,80 (Bündelung) = 24,4A
```

→ Das Kabel kann im Motorraum nur noch 24,4A statt 50A tragen!

### 2.3 AWG vs. mm² — Umrechnungstabelle

Das amerikanische AWG-System (American Wire Gauge) ist kontraintuitiv: **höhere AWG-Zahl = kleinerer Querschnitt**. Im europäischen Yachtbau wird in mm² gerechnet, aber viele Komponenten und Dokumentationen verwenden AWG.

| AWG | mm² (exakt) | mm² (Standardwert) | Durchmesser (mm) | Widerstand (Ω/km bei 20°C) |
|-----|------------|--------------------|-----------------|-----------------------------|
| 22 | 0,326 | 0,34 | 0,644 | 52,96 |
| 20 | 0,518 | 0,50 | 0,812 | 33,31 |
| 18 | 0,823 | 0,75 | 1,024 | 20,95 |
| 16 | 1,309 | 1,5 | 1,291 | 13,18 |
| 14 | 2,081 | 2,5 | 1,628 | 8,286 |
| 12 | 3,309 | 4 | 2,053 | 5,211 |
| 10 | 5,261 | 6 | 2,588 | 3,277 |
| 8 | 8,366 | 10 | 3,264 | 2,061 |
| 6 | 13,30 | 16 | 4,115 | 1,296 |
| 4 | 21,15 | 25 | 5,189 | 0,8152 |
| 2 | 33,62 | 35 | 6,544 | 0,5127 |
| 1 | 42,41 | 50 | 7,348 | 0,4066 |
| 1/0 | 53,49 | 50 | 8,252 | 0,3225 |
| 2/0 | 67,43 | 70 | 9,266 | 0,2557 |
| 3/0 | 85,03 | 95 | 10,40 | 0,2028 |
| 4/0 | 107,2 | 120 | 11,68 | 0,1608 |

**Wichtiger Hinweis:** Die mm²-Standardwerte sind die nächstliegenden metrischen Handelsgrößen, NICHT exakte Umrechnungen. Ein AWG 10 hat exakt 5,26 mm², wird aber in der Praxis durch 6 mm² ersetzt. Dies bedeutet, dass metrische Kabel bei gleichem „Äquivalent" oft etwas großzügiger dimensioniert sind — ein Sicherheitsvorteil.

### 2.4 Marine-Grade: Verzinntes Kupfer

**Das wichtigste Merkmal eines Marine-Kabels ist die Verzinnung der Kupferlitzen.** Jede einzelne Litze wird galvanisch mit einer dünnen Zinnschicht (2–5 µm) überzogen, BEVOR das Kabel zusammengeführt und isoliert wird.

**Warum verzinntes Kupfer zwingend ist:**

| Eigenschaft | Blankes Kupfer | Verzinntes Kupfer |
|-------------|---------------|-------------------|
| Korrosionsbeständigkeit Salzluft | 2–5 Jahre | 15–25+ Jahre |
| Grünspan-Bildung (Cu₂(OH)₂CO₃) | Innerhalb Monaten | Keine |
| Übergangswiderstand nach 5 Jahren | +40–200% | +0–5% |
| Lötbarkeit nach 10 Jahren | Schlecht bis unmöglich | Gut |
| Crimpverbindungs-Haltbarkeit | Degradiert durch Oxidschicht | Bleibt stabil |
| Preis-Aufschlag | Basis | +15–25% |

**Erkennungsmerkmale:**
- Verzinntes Kupfer: silbrig-weiße Litzen
- Blankes Kupfer: rötlich-goldene Litzen (neu) → grünlich-schwarz (korrodiert)

**Marine-Grade Kabel erkennen:**
- UL 1426 (USA) — „Boat Cable" Zertifizierung
- Feindrähtig (Klasse 5 nach IEC 60228) — typisch 19–65 Einzeldrähte pro Litze
- Alle Einzeldrähte verzinnt
- Hochwertiges Isolationsmaterial (oft PVC/Nylon-Doppelmantel)
- Temperaturbeständig mindestens -40°C bis +75°C

### 2.5 Isolationsmaterialien

| Material | Kurzbezeichnung | Temp.-Bereich | UV-Beständigkeit | Öl/Kraftstoff | Flexibilität | Marine-Eignung |
|----------|----------------|--------------|-----------------|--------------|-------------|---------------|
| PVC (Polyvinylchlorid) | V, Y | -20 bis +70°C | Mittel | Gering | Gut | Standard |
| PVC/Nylon Doppelmantel | — | -40 bis +75°C | Gut | Mittel | Gut | Empfohlen |
| PE (Polyethylen) | — | -60 bis +80°C | Gut | Gering | Mäßig | Koaxialkabel |
| XLPE (Vernetztes PE) | X | -40 bis +90°C | Gut | Gut | Mäßig | Empfohlen |
| EPR (Ethylen-Propylen) | G | -40 bis +90°C | Sehr gut | Gut | Sehr gut | Premium |
| Silikon | S | -60 bis +180°C | Sehr gut | Gering | Hervorragend | Motorraum |
| PTFE (Teflon) | — | -200 bis +260°C | Hervorragend | Hervorragend | Mäßig | Spezial, teuer |
| TPE (Thermoplast. Elastomer) | — | -40 bis +105°C | Gut | Gut | Hervorragend | Premium |
| Gummi (CR/CSP) | — | -30 bis +80°C | Mäßig | Schlecht | Sehr gut | Veraltet |

**Empfehlung nach Einsatzzone:**
- **Motorraum:** Silikon oder XLPE (mindestens 90°C)
- **Mast:** XLPE oder EPR (UV, Vibration)
- **Bilge:** PVC/Nylon oder XLPE (Feuchtigkeit)
- **Deck/Cockpit:** PVC/Nylon oder TPE (UV, Flexibilität)
- **Salon/Kabine:** PVC Standard ausreichend

### 2.6 Farbcodes

#### 2.6.1 DC-Farbcode nach ABYC E-11

| Farbe | Funktion |
|-------|----------|
| Rot | DC-Positiv, ungeschaltet (Batterie-Hauptleitung) |
| Gelb/Rot | DC-Positiv, geschaltet (Zündung) |
| Schwarz | DC-Negativ (Masse) |
| Gelb | DC-Negativ (alternative Kennzeichnung) |
| Braun | Generator-Ladeleitung |
| Orange | Zubehör-Versorgung |
| Dunkelblau | Beleuchtung (Kabine) |
| Hellblau | Öldruckschalter |
| Grau | Tachometer |
| Dunkelgrün | Bonding/Erdung |
| Grün | Trimmklappen (Steuerbord) |
| Violett/Lila | Instrumenten-Versorgung, Zündung |
| Rosa | Kraftstoffgeber |
| Weiß | — |
| Weiß/Rot | — |
| Tan (Hellbraun) | Wassertemperatur |

#### 2.6.2 AC-Farbcode nach IEC (EU-Standard)

| Farbe | Funktion |
|-------|----------|
| Braun | Phase L1 |
| Schwarz | Phase L2 |
| Grau | Phase L3 |
| Blau (Hellblau) | Neutralleiter N |
| Grün-Gelb | Schutzleiter PE |

#### 2.6.3 NMEA 2000 Farbcode

| Farbe | Funktion |
|-------|----------|
| Rot | +12V Versorgung (Netzwerk-Strom) |
| Schwarz | Masse |
| Weiß | CAN_H (High) |
| Blau | CAN_L (Low) |
| Schirm (blankes Geflecht) | Abschirmung/Drain |

### 2.7 Leitermaterial und Aufbau

#### 2.7.1 Leiterklassen nach IEC 60228

| Klasse | Bezeichnung | Aufbau | Marine-Eignung |
|--------|------------|--------|---------------|
| Klasse 1 | Massiv (RE) | Eindrähtig | NEIN — bricht bei Vibration |
| Klasse 2 | Mehrdrahtig (RM) | 7–19 Drähte | Bedingt — nur starre Verlegung |
| Klasse 5 | Feindrähtig (RU) | 19–65+ Drähte | JA — Standard Marine |
| Klasse 6 | Feinstdrähtig (RD) | 100+ Drähte | JA — Premium, hoch-flexibel |

**Für den Marineeinsatz sind ausschließlich Klasse 5 oder Klasse 6 Leiter geeignet.** Die hohe Litzenzahl gewährleistet:
- Vibrationsfestigkeit (einzelne gebrochene Drähte beeinträchtigen das Kabel nicht sofort)
- Flexibilität für enge Radien und wiederholte Biegung
- Bessere Crimpverbindungen (mehr Kontaktfläche)

#### 2.7.2 Leiteraufbau nach Querschnitt (Klasse 5)

| Querschnitt (mm²) | Minimale Drahtanzahl | Einzeldraht-Ø (mm) |
|--------------------|---------------------|---------------------|
| 0,75 | 24 | 0,21 |
| 1,5 | 30 | 0,26 |
| 2,5 | 50 | 0,26 |
| 4 | 56 | 0,31 |
| 6 | 84 | 0,31 |
| 10 | 80 | 0,41 |
| 16 | 126 | 0,41 |
| 25 | 196 | 0,41 |
| 35 | 276 | 0,41 |
| 50 | 396 | 0,41 |
| 70 | 360 | 0,51 |
| 95 | 475 | 0,51 |
| 120 | 608 | 0,51 |

### 2.8 Biegeradien

Der minimale Biegeradius verhindert Beschädigung der Isolierung und Bruch einzelner Litzen:

| Kabeltyp | Minimaler Biegeradius (fest verlegt) | Minimaler Biegeradius (wiederholt gebogen) |
|----------|--------------------------------------|-------------------------------------------|
| Einadrig, PVC | 4× Außendurchmesser | 8× Außendurchmesser |
| Einadrig, XLPE | 6× Außendurchmesser | 12× Außendurchmesser |
| Mehradrig, PVC | 6× Außendurchmesser | 12× Außendurchmesser |
| Koaxial | 6× Außendurchmesser | 10× Außendurchmesser |
| Datenkabel (NMEA 2000) | 25 mm Mindestradius | 50 mm Mindestradius |
| Batteriekabel >50mm² | 6× Außendurchmesser | Nicht vorgesehen |

---

## 3. Typenübersicht

### 3.1 Einzeladerkabel (Einzelleiter)

#### 3.1.1 H07V-K (Marine-Version)

**Beschreibung:** Einadrige, feindrähtige Leitung mit PVC-Isolierung. Die Marine-Version verwendet verzinntes Kupfer und hochwertigeres PVC mit UV-Stabilisatoren.

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, verzinnt, Klasse 5 |
| Isolierung | PVC (TI2) |
| Temperaturbereich | -30°C bis +70°C (kurzzeitig +80°C) |
| Nennspannung | 450/750V |
| Prüfspannung | 2.500V AC |
| Querschnitte | 1,5 – 240 mm² |
| Farben | Rot, Schwarz, Blau, Braun, Gelb/Grün, Weiß, Grau |
| Zulassungen | VDE, CE, UL (variiert nach Hersteller) |
| Einsatz | DC-Hauptverkabelung, AC-Festverlegung, Schaltschrank |

#### 3.1.2 H05V-K / H05V-U

**Beschreibung:** Dünnere Einzeladerleitung für Steuerleitungen und Niederstrom-Anwendungen. H05V-U ist eindrahtig und daher NICHT für Marine geeignet.

| Eigenschaft | H05V-K (geeignet) | H05V-U (NICHT geeignet) |
|-------------|-------------------|------------------------|
| Leiter | Klasse 5, feindrähtig | Klasse 1, eindrahtig |
| Querschnitte | 0,5 – 1,0 mm² | 0,5 – 1,0 mm² |
| Vibrationsfest | Ja | NEIN |
| Marine-Eignung | Bedingt (nur Innenbereich) | NEIN |

#### 3.1.3 Silikonkabel (ÖLFLEX HEAT)

**Beschreibung:** Einzeladerleitung mit Silikonkautschuk-Isolierung für Hochtemperatur-Bereiche.

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, verzinnt, Klasse 5 |
| Isolierung | Silikonkautschuk (SiR) |
| Temperaturbereich | -60°C bis +180°C |
| Nennspannung | 300/500V |
| Querschnitte | 0,5 – 120 mm² |
| Besonderheit | Extrem flexibel, selbstverlöschend |
| Einsatz | Motorraum, Abgaskrümmer-Nähe, Generator |
| Nachteil | Mechanisch weniger robust, teuer |

### 3.2 Mehraderkabel (Mantelleitung)

#### 3.2.1 NYM-J / NYM-O (Marine-Variante)

**Beschreibung:** Mantelleitung mit PVC-Innen- und Außenmantel. Im stationären Bereich eines Bootes für AC-Verkabelung einsetzbar.

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, verzinnt (Marine-Version), Klasse 1 oder 5 |
| Isolierung | PVC-Aderumhüllung + PVC-Mantel |
| Temperaturbereich | -5°C bis +70°C |
| Nennspannung | 300/500V |
| Querschnitte | 3×1,5 – 5×16 mm² |
| Farben Adern | Braun, Blau, Grün/Gelb (+ Schwarz, Grau bei 4/5-adrig) |
| Einsatz | AC-Festverlegung im Schiff, Landstromleitung intern |

**Achtung:** Standard-NYM-J vom Baumarkt ist NICHT marine-tauglich — der Leiter ist nicht verzinnt und die Ummantelung ist für dauerhaft feuchte Umgebung nicht ausgelegt.

#### 3.2.2 ÖLFLEX CLASSIC 110 / 110 BK

**Beschreibung:** Steuer- und Anschlussleitung, häufig für Schaltschrank-Verdrahtung und Sensorik auf Yachten verwendet.

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, blank oder verzinnt |
| Isolierung | PVC-Aderumhüllung, PVC-Mantel |
| Temperaturbereich | -15°C bis +70°C (fest) / +5°C bis +70°C (bewegt) |
| Nennspannung | 300/500V |
| Aderzahl | 2–65 |
| Querschnitte | 0,5 – 4 mm² |
| Farben Adern | Nummeriert, Grün/Gelb-PE |
| Besonderheit | Ölbeständig (Mantel) |
| Einsatz | Motor-Steuerung, Alarmanlage, Sensorik |

#### 3.2.3 Marinekabel geschirmt

**Beschreibung:** Mehraderkabel mit Abschirmgeflecht für störungsempfindliche Anwendungen.

| Eigenschaft | Wert |
|-------------|------|
| Abschirmung | Kupfergeflecht, verzinnt (Bedeckung ≥85%) |
| Drain-Wire | Ja (für einfachen Erdungsanschluss) |
| EMV-Schutz | Ja — für UKW-Funk, AIS, GPS, Radar |
| Querschnitte | 2×0,5 – 4×2,5 mm² |
| Einsatz | Funkgeräte, Navigationselektronik, Sensoren |

### 3.3 Batteriekabel

#### 3.3.1 Anforderungen an Batteriekabel

Batteriekabel verbinden Batterien mit Hauptschaltern, Ladesystemen und Hochstromverbrauchern. Sie unterliegen den höchsten Anforderungen:

- **Querschnitte:** 16 – 240 mm² (typisch 35–95 mm² für 12V, 25–70 mm² für 24V)
- **Isolation:** PVC/Nylon Doppelmantel oder XLPE, mindestens 105°C-bewertet
- **Leiter:** Verzinntes Kupfer, Klasse 5, oft hochflexibel (Klasse 6)
- **Farbcodierung:** Rot (Positiv), Schwarz (Negativ)
- **Endbehandlung:** Rohrkabelschuhe, geschraubt, nicht gelötet

#### 3.3.2 Querschnitts-Richtwerte Batteriekabel

| Anwendung | 12V-System | 24V-System |
|-----------|-----------|-----------|
| Starter (Diesel bis 50 PS) | 35 mm² | 25 mm² |
| Starter (Diesel 50–150 PS) | 50 mm² | 35 mm² |
| Starter (Diesel >150 PS) | 70–95 mm² | 50 mm² |
| Lichtmaschine (60–120A) | 16–25 mm² | 10–16 mm² |
| Batterie-Sammelschiene | 50–95 mm² | 35–70 mm² |
| Ankerwinde (bis 1.500W) | 25–35 mm² | 16–25 mm² |
| Ankerwinde (1.500–3.000W) | 50–70 mm² | 35–50 mm² |
| Bugstrahlruder (5 kW) | 70 mm² | 50 mm² |
| Bugstrahlruder (10 kW) | 120 mm² | 95 mm² |
| Inverter (2.000W) | 35 mm² | 16 mm² |
| Inverter (3.000W) | 50 mm² | 25 mm² |

### 3.4 Koaxialkabel

#### 3.4.1 RG-58/U

| Eigenschaft | Wert |
|-------------|------|
| Impedanz | 50 Ω |
| Innenleiter | 0,9 mm Cu (blank oder verzinnt) |
| Dielektrikum | PE (Polyethylen) |
| Schirmung | Kupfergeflecht, 95% Bedeckung |
| Mantel | PVC, schwarz |
| Außen-Ø | 5,0 mm |
| Dämpfung bei 156 MHz | 12,1 dB/100m |
| Einsatz | UKW-Funk (Kurzstrecke), AIS, GPS |
| Max. Kabellänge UKW | 10–15m empfohlen |

#### 3.4.2 RG-213/U

| Eigenschaft | Wert |
|-------------|------|
| Impedanz | 50 Ω |
| Innenleiter | 2,26 mm Cu |
| Dielektrikum | PE |
| Schirmung | Kupfergeflecht, 97% Bedeckung |
| Mantel | PVC, schwarz |
| Außen-Ø | 10,3 mm |
| Dämpfung bei 156 MHz | 5,5 dB/100m |
| Einsatz | UKW-Funk (Langstrecke), SSB-Funk |
| Max. Kabellänge UKW | 25–30m empfohlen |

#### 3.4.3 RG-8X

| Eigenschaft | Wert |
|-------------|------|
| Impedanz | 50 Ω |
| Innenleiter | 1,0 mm Cu |
| Dielektrikum | PE-Schaum |
| Schirmung | Doppelschirmung (Geflecht + Folie) |
| Mantel | PVC, schwarz |
| Außen-Ø | 6,1 mm |
| Dämpfung bei 156 MHz | 9,8 dB/100m |
| Einsatz | UKW-Funk, AIS — guter Kompromiss Durchmesser/Dämpfung |

#### 3.4.4 RG-6/U

| Eigenschaft | Wert |
|-------------|------|
| Impedanz | 75 Ω |
| Innenleiter | 1,0 mm Cu-Stahl |
| Dielektrikum | PE-Schaum |
| Schirmung | Folie + Geflecht |
| Mantel | PVC, weiß oder schwarz |
| Außen-Ø | 6,9 mm |
| Einsatz | TV-Antenne, Sat-Empfang, Kamera-Systeme |

**Achtung:** 50-Ω- und 75-Ω-Kabel sind NICHT austauschbar! Ein 75-Ω-Kabel am UKW-Funk führt zu erhöhtem SWR und kann den Sender beschädigen.

#### 3.4.5 Koaxialkabel — Vergleichstabelle Dämpfung

| Kabeltyp | 30 MHz (dB/100m) | 156 MHz (dB/100m) | 450 MHz (dB/100m) | 1 GHz (dB/100m) |
|----------|------------------|--------------------|--------------------|--------------------|
| RG-58/U | 5,3 | 12,1 | 21,3 | 34,0 |
| RG-8X | 4,3 | 9,8 | 17,1 | 28,0 |
| RG-213/U | 2,5 | 5,5 | 9,8 | 16,0 |
| Aircell 7 | 2,2 | 4,8 | 8,3 | 13,5 |
| LMR-400 | 1,3 | 3,0 | 5,4 | 8,8 |

### 3.5 Datenkabel

#### 3.5.1 NMEA 2000 Backbone-Kabel (DeviceNet Micro-C)

| Eigenschaft | Wert |
|-------------|------|
| Standard | IEC 61918, DeviceNet Micro |
| Adern | 5 (2× Daten CAN_H/CAN_L, 2× Versorgung +12V/GND, 1× Schirm/Drain) |
| Impedanz | 120 Ω ± 10% (charakteristisch) |
| Querschnitt Daten | 2× 0,34 mm² (AWG 22), verdrillt |
| Querschnitt Versorgung | 2× 0,82 mm² (AWG 18) |
| Schirmung | Alufolie + Drain-Draht |
| Mantel | PVC oder PUR, UV-beständig |
| Stecker | 5-polige Micro-C Rundstecker (M12) |
| Max. Backbone-Länge | 100m (ohne Repeater) |
| Max. Stichleitungslänge | 6m |
| Terminierung | 120 Ω an beiden Enden |

**Wichtig:** NMEA 2000 Kabel dürfen NICHT durch Standard-Steuerleitungen ersetzt werden. Die Impedanzanpassung (120 Ω) ist für fehlerfreie CAN-Bus-Kommunikation zwingend.

#### 3.5.2 NMEA 0183 Kabel

| Eigenschaft | Wert |
|-------------|------|
| Protokoll | RS-422/RS-232 seriell |
| Adern | 2 (TX+/TX-) pro Sender/Empfänger-Paar + Masse |
| Querschnitt | 0,34–0,5 mm² (AWG 22–20) |
| Schirmung | Empfohlen (geschirmte Zweidrahtleitung) |
| Max. Kabellänge | ca. 500m (RS-422) / 15m (RS-232) |
| Einsatz | GPS, Echolot, Windmesser, Autopilot (ältere Geräte) |

#### 3.5.3 Ethernet-Kabel (Marine-Grade)

| Eigenschaft | Cat5e Marine | Cat6 Marine | Cat6a Marine |
|-------------|-------------|------------|-------------|
| Übertragungsrate | 1 Gbit/s | 1 Gbit/s | 10 Gbit/s |
| Frequenz | 100 MHz | 250 MHz | 500 MHz |
| Leiter | Cu verzinnt, feindrähtig | Cu verzinnt, feindrähtig | Cu verzinnt, feindrähtig |
| Schirmung | UTP oder STP | STP empfohlen | STP (geschirmt) |
| Mantel | PVC marine oder PUR | PVC marine oder PUR | PUR |
| UV-beständig | Ja (marine-Version) | Ja | Ja |
| Einsatz | MFD-Vernetzung, Router, IP-Kameras | Radar, Sonar, Chartplotter | AV-Systeme, Superyachten |

#### 3.5.4 USB-Kabel (Marine-Grade)

Für den Marineeinsatz existieren wasserdichte USB-Durchführungen und -Kabel:

| Typ | Einsatz | Bemerkung |
|-----|---------|-----------|
| USB-A zu USB-B | Chartplotter-Verbindung, Updates | Standardmäßig nicht wasserdicht |
| USB-C | Moderne MFDs, Ladeanschlüsse | Zunehmend verbreitet |
| Wasserdichte USB-Buchse (IP67) | Cockpit, Steuerstand | Spezielle Einbausteckdosen |

### 3.6 Spezialkabel

#### 3.6.1 Unterwasserkabel

**Einsatz:** Unterwasser-Beleuchtung, Echolot-Geber, Log/Lot-Geber, Bootsheizung (Unterwasser-Wärmetauscher)

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, verzinnt, Klasse 5 |
| Isolierung | XLPE oder PUR |
| Mantel | PUR (Polyurethan), schwarz, UV- und meerwasserbeständig |
| Schutzart | Mindestens IP68 (dauerhaft untergetaucht) |
| Biegeradius | ≥8× Außendurchmesser |
| Besonderheit | Keine Spleißstellen unter der Wasserlinie! |

**Regeln für Unterwasserkabel:**
1. Kabel muss von der Durchführung bis zum Verbraucher DURCHGEHEND sein — keine Verbindungsstellen unter Wasser
2. Decksdurchführung mit vergossenem Kabeleintritt oder Kompressionspassung
3. Kabel muss mechanisch gegen Scheuern am Rumpf geschützt werden
4. Jede Beschädigung → Kabel komplett tauschen, nicht reparieren

#### 3.6.2 Mastkabel

**Einsatz:** Positionslichter, Ankerlicht, Windex, UKW-Antenne, Radarreflektor, Windmessanlage, Scheinwerfer

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, verzinnt, Klasse 5/6 (hochflexibel!) |
| Isolierung | PVC/Nylon oder PUR |
| Mantel | PUR bevorzugt — UV-beständig, abriebfest |
| Querschnitte | 1,5–4 mm² (Licht/Signale), RG-8X/RG-213 (UKW) |
| Verlängerung | Nicht im Mast — durchgängig von Mastfuß zu Verbraucher |
| Zugentlastung | Am Mastfuß und Masttop zwingend |
| Bündelung | Max. 6 Kabel im Mastprofil |

**Kritische Problemzone Mastfuß-Durchführung:**
Der Mastfuß ist die Schwachstelle Nr. 1 bei Mastverkabelung. Beim Segelsetzen und durch Seegang biegt sich das Kabel an dieser Stelle tausende Male pro Saison. Lösungen:
- **Kabelschlaufe (Drip Loop):** 15–20 cm Schlaufe unterhalb der Mastdurchführung ermöglicht Biegung ohne Knickbelastung
- **Flexible Kabel (Klasse 6):** Minimiert Bruchgefahr
- **Spiral-Kabelschutz:** PVC-Spirale oder Geflechtschlauch als Knickschutz
- **Regelmäßige Inspektion:** Jährlich bei der Mastabnahme alle Kabel am Mastfuß prüfen

#### 3.6.3 Solar-Kabel (PV-Kabel)

| Eigenschaft | Wert |
|-------------|------|
| Standard | EN 50618 / TÜV Rheinland |
| Leiter | Kupfer, verzinnt, Klasse 5 |
| Isolierung | Doppelt (Elektronenstrahl-vernetztes Polymer) |
| Temperaturbereich | -40°C bis +90°C (am Leiter +120°C) |
| Nennspannung | 1.000/1.500V DC |
| UV-Beständigkeit | EN 50396 — hervorragend |
| Querschnitte | 4 – 10 mm² (typisch 6 mm²) |
| Stecker | MC4 (IP67/IP68) |
| Einsatz | Solar-Panel auf Bimini/Davits zum MPPT-Regler |

#### 3.6.4 Steuerkabel für Hydraulik-Systeme

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, verzinnt |
| Aderzahl | 2–7 |
| Querschnitte | 0,5–2,5 mm² |
| Schirmung | Optional (empfohlen bei Proportionalventilen) |
| Mantel | PUR, ölbeständig |
| Einsatz | Autopilot-Hydraulik, Bugstrahlruder, Gangschaltung |

#### 3.6.5 Heizungskabel (Selbstregulierende Heizbänder)

| Eigenschaft | Wert |
|-------------|------|
| Funktion | Frostschutz für Leitungen, Tank-Beheizung |
| Typ | Selbstregulierend (PTC-Effekt) |
| Leistung | 10–40 W/m (temperaturabhängig) |
| Max. Temperatur | 65–110°C (je nach Typ) |
| Mantel | Fluorpolymer oder PVC |
| Einsatz | Frischwasserleitungen, Dieseltanks (Winterbetrieb) |

---

## 4. Produktlinien und Spezifikationen

### 4.1 Ancor Marine Grade

**Hersteller:** Ancor (USA) — eine Marke der Marinco-Gruppe (Actuant/Enerpac)
**Position:** Marktführer für Marine-Kabel in den USA, weit verbreitet auch in Europa

#### 4.1.1 Ancor Marine Grade Einzeladerkabel

| Eigenschaft | Wert |
|-------------|------|
| Bezeichnung | Ancor Marine Grade Primary Wire |
| Leiter | Verzinntes Kupfer, Klasse 5 (ASTM B-174) |
| Isolierung | PVC/Nylon Doppelmantel |
| Temperaturbereich | -40°C bis +75°C |
| Nennspannung | 600V |
| Zulassung | UL 1426 „Boat Cable", SAE J1128 |
| Querschnitte | AWG 18 (0,75 mm²) bis AWG 4/0 (120 mm²) |
| Farben | 12 Standardfarben |
| Verpackung | 8m, 30m, 75m, 300m Rollen |

**Preisbereich (2025/2026):**
| AWG | mm² ca. | EUR/m (ca.) |
|-----|--------|------------|
| 16 | 1,5 | 0,90–1,20 |
| 14 | 2,5 | 1,10–1,50 |
| 12 | 4 | 1,40–1,90 |
| 10 | 6 | 2,00–2,60 |
| 8 | 10 | 3,20–4,00 |
| 6 | 16 | 4,50–5,50 |
| 4 | 25 | 6,50–8,00 |
| 2 | 35 | 9,00–11,00 |
| 1/0 | 50 | 14,00–17,00 |
| 2/0 | 70 | 18,00–22,00 |
| 4/0 | 120 | 28,00–35,00 |

#### 4.1.2 Ancor Duplex-Kabel

| Eigenschaft | Wert |
|-------------|------|
| Bezeichnung | Ancor Marine Grade Duplex Wire |
| Aufbau | 2 Adern (Rot + Schwarz) parallel, gemeinsamer Mantel |
| Leiter | Verzinntes Kupfer, Klasse 5 |
| Isolierung | PVC/Nylon/PVC Dreifachmantel |
| Querschnitte | AWG 16 (1,5 mm²) bis AWG 6 (16 mm²) |
| Einsatz | Bilgenpumpe, Navigationslichter, Zubehör |

#### 4.1.3 Ancor Triplex-Kabel

| Eigenschaft | Wert |
|-------------|------|
| Aufbau | 3 Adern (Schwarz + Weiß/Grau + Grün/Grün-Gelb) |
| Einsatz | AC-Verkabelung Bord, Landstrom-Anschluss |
| Querschnitte | AWG 16 bis AWG 6 |

#### 4.1.4 Ancor Batteriekabel

| Eigenschaft | Wert |
|-------------|------|
| Bezeichnung | Ancor Battery Cable |
| Leiter | Verzinntes Kupfer, hochflexibel (>600 Litzen) |
| Isolierung | PVC, Doppelwand |
| Querschnitte | AWG 8 (10 mm²) bis AWG 4/0 (120 mm²) |
| Farben | Rot, Schwarz, Gelb |
| Besonderheit | Extrem flexibel für enge Motorräume |

### 4.2 Lapp ÖLFLEX

**Hersteller:** Lapp GmbH (Stuttgart, Deutschland) — Weltmarktführer für Industriekabel
**Position:** Premium-Industriekabel, viele Typen für Marine geeignet

#### 4.2.1 ÖLFLEX CLASSIC 110 BK

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer blank, Klasse 5 (verzinnt optional) |
| Isolierung | PVC-Aderumhüllung |
| Mantel | PVC, schwarz, ölbeständig |
| Temperaturbereich | -15°C bis +70°C (fest), +5°C bis +70°C (bewegt) |
| Nennspannung | 300/500V |
| Aderzahl | 2–65 |
| Querschnitte | 0,5–4 mm² |
| Zulassung | VDE, UL/CSA, CE |
| Einsatz | Steuerverkabelung, Schaltschrank, Alarmanlage |

#### 4.2.2 ÖLFLEX HEAT 180 SiF

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, verzinnt, Klasse 5 |
| Isolierung | Silikonkautschuk |
| Temperaturbereich | -60°C bis +180°C |
| Nennspannung | 300/500V |
| Querschnitte | 0,25–240 mm² |
| Zulassung | VDE, UL |
| Einsatz | Motorraum, Generator, Auspuffnähe |

#### 4.2.3 ÖLFLEX ROBUST 215 C

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, verzinnt |
| Isolierung | TPE |
| Mantel | PUR-basiert, UV-beständig |
| Temperaturbereich | -40°C bis +80°C |
| Besonderheit | Extrem robust, ölbeständig, UV-beständig |
| Einsatz | Deck-Verkabelung, Außenbereich, Davit-Kabel |

#### 4.2.4 ÖLFLEX CHAIN 809 CY

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, verzinnt |
| Schirmung | Kupfergeflecht verzinnt, ≥85% Bedeckung |
| Mantel | PVC, grau |
| Temperaturbereich | -15°C bis +70°C |
| Besonderheit | Für Schleppketten geeignet → sehr biegefest |
| Einsatz | Geschirmte Steuerleitung, EMV-kritische Verbindungen |

### 4.3 SAB Bröckskes

**Hersteller:** SAB Bröckskes GmbH & Co. KG (Viersen, Deutschland)
**Position:** Spezialkabelhersteller, breites Marine-Portfolio

#### 4.3.1 SAB SABIX A 812 XL

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, verzinnt, Klasse 6 (feinstdrähtig) |
| Isolierung | XLPE |
| Mantel | PUR, schwarz, UV-beständig |
| Temperaturbereich | -40°C bis +90°C |
| Nennspannung | 0,6/1 kV |
| Schirmung | Kupfergeflecht verzinnt (optional) |
| Zulassung | GL (Germanischer Lloyd), VDE, CE |
| Besonderheit | GL-Marine-Zulassung, halogenfrei optional |
| Einsatz | Hauptverkabelung Superyachten, Lloyd's-Register-Boote |

#### 4.3.2 SAB SABIX D 315 FRNC MARITIME

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, verzinnt |
| Isolierung | Halogenfreier Compound |
| Mantel | FRNC (Flame Retardant Non Corrosive) |
| Flammenresistenz | IEC 60332-1, IEC 60332-3 |
| Rauchentwicklung | Gering (IEC 61034) |
| Zulassung | GL, DNV, Bureau Veritas |
| Einsatz | Superyachten >24m, Klassifizierte Schiffe |

### 4.4 Helukabel

**Hersteller:** Helukabel GmbH (Hemmingen, Deutschland)
**Position:** Breites Sortiment an Industrie- und Marine-Kabeln

#### 4.4.1 HELUKABEL HELUPOWER MARINE

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, verzinnt, Klasse 5 |
| Isolierung | EPR (Ethylen-Propylen-Kautschuk) |
| Mantel | CSP (Chlorsulfonyl-Polyethylen), schwarz |
| Temperaturbereich | -30°C bis +85°C |
| Nennspannung | 0,6/1 kV |
| Flammenresistenz | IEC 60332-1 |
| Zulassung | GL, DNV, BV, LR |
| Einsatz | Hauptverteilung auf Yachten >24m |

#### 4.4.2 HELUKABEL HELUSIGNAL 120

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, verzinnt |
| Impedanz | 120 Ω ± 10% |
| Aderzahl | 2 Datenpaare + 2 Versorgungsadern + Drain |
| Mantel | PVC, blau |
| Einsatz | NMEA 2000 kompatibles Backbone-Kabel |

### 4.5 Nexans

**Hersteller:** Nexans S.A. (Paris, Frankreich) — einer der größten Kabelhersteller weltweit
**Position:** Premium-Marine-Kabel, besonders für Superyachten und kommerzielle Schifffahrt

#### 4.5.1 Nexans TITANEX H07RN-F

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, blank (verzinnt auf Anfrage) |
| Isolierung | EPR (Ethylen-Propylen) |
| Mantel | CR (Chloropren-Kautschuk), schwarz |
| Temperaturbereich | -25°C bis +60°C (am Leiter +85°C) |
| Nennspannung | 450/750V |
| Querschnitte | 1,5–240 mm² |
| Besonderheit | Extrem robust, für raueste Bedingungen |
| Zulassung | VDE, CE, HAR |
| Einsatz | Landstromanschluss, Generator-Anschluss, Werftkabel |

#### 4.5.2 Nexans ALSECURE Marine

| Eigenschaft | Wert |
|-------------|------|
| Leiter | Kupfer, verzinnt |
| Isolierung | XLPE |
| Mantel | HFFR (Halogen Free Flame Retardant) |
| Flammenresistenz | IEC 60332-3 Cat. A |
| Rauchentwicklung | Sehr gering |
| Toxizität | Gering (halogenfrei) |
| Zulassung | DNV-GL, BV, LR |
| Einsatz | Superyachten >24m, Passagierschiffe, Megayachten |

### 4.6 Glomex (Koaxialkabel)

**Hersteller:** Glomex S.r.l. (Ravenna, Italien)
**Position:** Spezialist für Marine-Antennen und zugehörige Koaxialkabel

#### 4.6.1 Glomex RA352

| Eigenschaft | Wert |
|-------------|------|
| Typ | RG-8X äquivalent |
| Impedanz | 50 Ω |
| Innenleiter | CuBe verzinnt |
| Schirmung | Doppelschirmung (Folie + Geflecht) |
| Mantel | PVC, weiß, UV-beständig |
| Außen-Ø | 6,1 mm |
| Stecker | PL-259 vormontiert (verschiedene Längen) |
| Längen | 3m, 6m, 12m, 18m |
| Einsatz | UKW-Antennenanschluss |

#### 4.6.2 Glomex RA355

| Eigenschaft | Wert |
|-------------|------|
| Typ | RG-213 äquivalent |
| Impedanz | 50 Ω |
| Innenleiter | Cu-Vollleiter, verzinnt |
| Schirmung | Doppelschirmung |
| Mantel | PVC, schwarz, UV-beständig |
| Außen-Ø | 10,3 mm |
| Einsatz | SSB-Funk, lange UKW-Antennenverbindungen |

---

## 5. Hersteller-Datenbank

### 5.1 Ancor (USA)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Ancor Marine Grade Wire Products |
| Muttergesellschaft | Marinco (Enerpac Tool Group) |
| Hauptsitz | Menomonee Falls, Wisconsin, USA |
| Gegründet | 1985 |
| Marine-Fokus | 100% Marine-Kabel und Zubehör |
| Hauptprodukte | Einzeladerkabel, Duplex/Triplex, Batteriekabel, Steckverbinder, Kabelschuhe |
| Zulassungen | UL 1426, SAE J1128, ABYC E-11 konform |
| Vertrieb Europa | SVB (D), Compass24 (D), MarinePool, Budget Marine |
| Preisniveau | Mittel-Premium (USA-Importware in EU) |
| Stärken | Vollständiges Sortiment, bewährte Qualität, gute Verfügbarkeit |
| Schwächen | In Europa teurer als lokale Alternativen, AWG-Angaben erfordern Umrechnung |
| Website | ancorproducts.com |

### 5.2 Lapp (Deutschland)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Lapp GmbH (U.I. Lapp GmbH) |
| Hauptsitz | Stuttgart, Deutschland |
| Gegründet | 1957 |
| Marine-Fokus | ca. 5% des Umsatzes, aber breites Portfolio nutzbar |
| Hauptprodukte | ÖLFLEX-Serie (Steuer-/Anschlussleitungen), Silikonkabel, geschirmte Kabel |
| Zulassungen | VDE, UL, CSA, GL, CE |
| Vertrieb | Elektro-Großhandel, Online (lappkabel.de), Industrievertrieb |
| Preisniveau | Premium (Industriequalität) |
| Stärken | Hervorragende Qualität, deutsche Produktion, umfassende Zertifizierungen |
| Schwächen | Nicht alle Typen in verzinnter Ausführung, primär Industriekabel |
| Website | lapp.com |

### 5.3 SAB Bröckskes (Deutschland)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | SAB Bröckskes GmbH & Co. KG |
| Hauptsitz | Viersen, Deutschland |
| Gegründet | 1947 |
| Marine-Fokus | Eigene Marine-Sparte mit GL/DNV-zertifizierten Kabeln |
| Hauptprodukte | SABIX Marine-Serie, Spezialkabel, hochflexible Kabel |
| Zulassungen | GL, DNV, BV, LR, VDE, UL |
| Vertrieb | Direkt, Industrievertrieb, Werftbelieferung |
| Preisniveau | Premium-Hoch (Spezialkabel-Niveau) |
| Stärken | Marine-Zulassungen, Sonderlösungen, hohe Qualität |
| Schwächen | Wenig Einzelhandels-Verfügbarkeit, primär B2B |
| Website | sab-cable.com |

### 5.4 Helukabel (Deutschland)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Helukabel GmbH |
| Hauptsitz | Hemmingen, Deutschland |
| Gegründet | 1978 |
| Marine-Fokus | HELUPOWER MARINE Serie, breites Marine-Portfolio |
| Hauptprodukte | Marine-Energiekabel, Steuerleitungen, Datenkabel, NMEA-Kabel |
| Zulassungen | GL, DNV, BV, LR, VDE, UL |
| Vertrieb | Elektro-Großhandel, Online-Shop, Werftbelieferung |
| Preisniveau | Mittel-Premium |
| Stärken | Gutes Preis-Leistungs-Verhältnis, breite Verfügbarkeit, Marine-Serien |
| Schwächen | Weniger bekannt als Ancor im Yacht-Bereich |
| Website | helukabel.com |

### 5.5 Nexans (Frankreich)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Nexans S.A. |
| Hauptsitz | Paris, Frankreich |
| Gegründet | 2000 (Ausgliederung aus Alcatel) |
| Marine-Fokus | Eigene Marine-Division für Schiffbau und Offshore |
| Hauptprodukte | ALSECURE Marine, TITANEX, Seekabel, Marine-Energiekabel |
| Zulassungen | DNV-GL, BV, LR, RINA, VDE |
| Vertrieb | Direkt an Werften, Elektro-Großhandel |
| Preisniveau | Premium-Hoch |
| Stärken | Weltweit führend bei Seekabeln, höchste Zertifizierungen |
| Schwächen | Primär Großkunden/Werften, für Einzelbootseigner schwer verfügbar |
| Website | nexans.com |

### 5.6 Glomex (Italien)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Glomex S.r.l. |
| Hauptsitz | Ravenna, Italien |
| Gegründet | 1984 |
| Marine-Fokus | 100% Marine (Antennen und Koaxialkabel) |
| Hauptprodukte | VHF/UKW-Antennen, Koaxialkabel, TV-Antennen, Splitter |
| Zulassungen | CE, FCC, IC |
| Vertrieb | Marine-Fachhandel weltweit |
| Preisniveau | Mittel |
| Stärken | Auf Marine-Antennenanschlüsse spezialisiert, vorkonfektionierte Kabel |
| Schwächen | Begrenztes Sortiment (nur Koaxial/Antenne) |
| Website | glomex.it |

### 5.7 Weitere Hersteller (Kurzübersicht)

| Hersteller | Land | Spezialität | Bemerkung |
|-----------|------|------------|-----------|
| Pacer Group | USA | Marine-Kabel, Steckverbinder | Gute Alternative zu Ancor |
| Philippi | Deutschland | Marine-Elektrik komplett | Eigenes Kabel-Sortiment |
| Blue Sea Systems | USA | Marine-Elektrik, Sicherungen | Empfiehlt Ancor-Kabel |
| Mastervolt | Niederlande | Marine-Elektrik | Kabel im System-Angebot |
| Victron Energy | Niederlande | Batterie-Systeme | Eigene Batteriekabel |
| Leoni | Deutschland | Spezialkabel | Marine-Sparte |
| Prysmian | Italien | Kabel (alle Bereiche) | Marine-Division |
| Belden | USA | Signal-/Datenkabel | Marinekabel-Serie |

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild: Grünspan an Klemmen und Verbindungen

**Beschreibung:** Grüne bis blaugrüne kristalline Ablagerungen (Kupfer(II)-carbonat-hydroxid, Cu₂(OH)₂CO₃) an Kabelverbindungen, Klemmen, Sicherungshaltern und Schaltern.

**Ursache:** Nicht-verzinntes Kupfer oder beschädigte Verzinnung in Kontakt mit Feuchtigkeit und Salz. Auch an verzinntem Kupfer möglich, wenn die Verzinnung durch Crimpen oder Biegen beschädigt wurde und Feuchtigkeit eindringt.

**Auswirkungen:**
- Erhöhter Übergangswiderstand an der Verbindungsstelle
- Spannungsabfall steigt → Verbraucher funktioniert schlecht oder gar nicht
- Wärmeentwicklung an der Verbindung → Brandgefahr
- Korrosion frisst sich tiefer in den Leiter → eventueller Leitungsbruch

**Diagnose:**
- Visuell: grüne Verfärbung sichtbar
- Multimeter: Übergangswiderstand an der Klemme >0,1 Ω
- Infrarot-Thermometer: Hot-Spot an der Verbindung unter Last

**Behebung:**
1. Stromkreis freischalten
2. Verbindung lösen
3. Korrodiertes Kabelende großzügig (5–10 cm) abschneiden
4. Neues Kabelende abisolieren, verzinnten Kabelschuh aufcrimpen
5. Verbindung mit korrosionsschutzmittel (z.B. Caig DeoxIT, Loctite Felt Pad) behandeln
6. Schrumpfschlauch mit Kleber über der Verbindung
7. Wenn Klemme ebenfalls korrodiert: Klemme ersetzen

**AYDI-Bewertung:**
- Confidence: visual_high (gut sichtbar auf Fotos)
- Severity: HOCH (Brandgefahr)
- Repair urgency: 1–4 Wochen

### 6.2 Fehlerbild: Kabelbruch durch Vibration

**Beschreibung:** Einzelne oder alle Litzen im Kabel brechen durch wiederholte mechanische Beanspruchung (Vibration, Biegung). Das Kabel sieht äußerlich oft intakt aus, zeigt aber intermittierende Ausfälle.

**Ursache:**
- Fehlende Zugentlastung
- Starre Verlegung an vibrierende Komponenten (Motor, Winsch, Ruderanlage)
- Falsche Kabelklasse (Klasse 1/2 statt 5/6)
- Zu enger Biegeradius
- Scharfe Kanten am Kabeldurchgang

**Typische Stellen:**
- Mastfuß-Durchführung (Nr. 1 Problemstelle)
- Motor-Anschlüsse (Lichtmaschine, Starter, Sensoren)
- Ruder-Servo/Autopilot-Pumpe
- Ankerwinden-Anschluss (Vibration beim Ankern)
- Navigationslichter am Mast

**Diagnose:**
- Multimeter: Widerstandsmessung bei gleichzeitigem Bewegen des Kabels — springender Wert zeigt Bruchstelle
- Visuell: Kabel an der Bruchstelle oft steifer oder dicker (gebrochene Litzen verschieben sich)
- Kabel biegen: an der Bruchstelle knickt das Kabel leichter ein

**Behebung:**
1. Betroffenen Kabelabschnitt identifizieren
2. Kabel beidseitig der Bruchstelle mind. 15 cm großzügig abschneiden
3. Neue Verbindung mit Crimpverbinder (wasserdicht) oder durchgängiges neues Kabel verlegen
4. Zugentlastung montieren
5. Vibrationsschutz: Kabel mit Spiralschlauch oder Geflechtschlauch schützen
6. Biegeradius prüfen und korrigieren

**AYDI-Bewertung:**
- Confidence: visual_low (äußerlich oft nicht sichtbar)
- Severity: MITTEL bis HOCH (abhängig vom Stromkreis)
- Repair urgency: Sofort bei sicherheitsrelevanten Stromkreisen

### 6.3 Fehlerbild: Isolationsschaden durch UV-Strahlung

**Beschreibung:** Die Kabelisolierung wird durch UV-Strahlung spröde, rissig und bröckelig. Besonders betroffen: Deckskabel, Mastkabel, Kabel an Davits und auf dem Bimini.

**Ursache:**
- PVC ohne UV-Stabilisatoren (Standard-Industriekabel)
- Langjährige direkte Sonneneinstrahlung
- Falsche Kabelwahl für den Außenbereich

**Erscheinungsbild:**
- Isolierung verfärbt sich (weiß → gelblich/grau, schwarz → grau/rissig)
- Mikrorisse an der Oberfläche
- Isolierung bröckelt beim Biegen
- Leiter stellenweise sichtbar

**Diagnose:**
- Visuell: Verfärbung und Risse erkennbar
- Tastprobe: Isolierung fühlt sich hart und spröde an (statt flexibel)
- Biegetest: Kabel an verdächtiger Stelle biegen — rissige Isolierung bricht sichtbar auf

**Behebung:**
1. Betroffene Kabel komplett ersetzen (Reparatur nicht sinnvoll)
2. Neues Kabel mit UV-beständiger Isolierung (PUR, XLPE, Silikon oder markiertes „UV-resistant")
3. Alternativ: Kabel in UV-beständigem Kabelkanal oder Geflechtschlauch verlegen
4. Keine provisorische Reparatur mit Isolierband — hält nicht dauerhaft

**AYDI-Bewertung:**
- Confidence: visual_high (gut sichtbar auf Fotos)
- Severity: HOCH (Kurzschlussgefahr, Erdschluss)
- Repair urgency: Vor nächster Fahrt

### 6.4 Fehlerbild: Falscher Querschnitt (Unterdimensionierung)

**Beschreibung:** Kabel zu dünn für den fließenden Strom. Führt zu übermäßigem Spannungsabfall, Erwärmung und — im schlimmsten Fall — Kabelbrand.

**Ursache:**
- Laieninstallation ohne Berechnung
- Nachträglicher Einbau stärkerer Verbraucher ohne Kabel-Upgrade
- Verwechslung von AWG und mm² (AWG 10 ≠ 10 mm²!)
- Spannungsabfall nicht berücksichtigt (nur Ampacity gerechnet)

**Symptome:**
- Verbraucher arbeitet schwach (Ankerwinde zieht langsam, Licht dimmt)
- Kabel wird warm/heiß unter Last
- Sicherung löst (selten — meist sind Sicherungen zu groß gewählt)
- Spannungsabfall >10% messbar

**Diagnose:**
1. Querschnitt des installierten Kabels bestimmen (Aufdruck oder Messung)
2. Tatsächlichen Stromverbrauch messen (Zangenamperemeter)
3. Kabellänge (Hin + Rück) bestimmen
4. Soll-Querschnitt berechnen
5. Vergleich: Ist < Soll? → Unterdimensioniert

**Behebung:**
1. Kabel durch korrekt dimensioniertes ersetzen
2. Alternativ: zweites Kabel parallel verlegen (Querschnitt addiert sich)
3. Sicherung anpassen (kleiner als die Belastbarkeit des NEUEN Kabels)
4. Bei Gelegenheit: alle Kabel im betroffenen Bereich prüfen (Dominoeffekt)

**AYDI-Bewertung:**
- Confidence: measured (berechenbar) oder visual_medium (Kabel sichtbar, Querschnitt abschätzbar)
- Severity: KRITISCH (Brandgefahr!)
- Repair urgency: Sofort

### 6.5 Fehlerbild: Nicht-verzinntes Kupfer in Salzwasserumgebung

**Beschreibung:** Standard-Automobil- oder Industriekabel mit blanken Kupferlitzen in einer Yacht verbaut. Die Korrosion beginnt an den Enden und kriecht entlang der Litzen unter die Isolierung.

**Ursache:**
- Unwissenheit des Installateurs
- Kosteneinsparung (Marine-Kabel kosten 15–25% mehr)
- Verfügbarkeit (Marine-Kabel nicht vorrätig, Automobil-Kabel sofort verfügbar)
- KFZ-Werkstatt hat Bordelektrik repariert

**Erscheinungsbild:**
- An den Kabelenden: Kupfer verfärbt sich schwarz, dann grün
- Unter der Isolierung: bei Abziehen der Isolierung zeigt sich schwarzes, sprödes Kupfer
- Widerstand steigt progressiv über 2–5 Jahre
- Kontaktprobleme häufen sich

**Diagnose:**
- Kabelende prüfen: Blanke Litzen = rötlich-gold (blankes Kupfer) statt silbrig-weiß (verzinnt)
- Mit Messer an einer Litze kratzen: silbrig = verzinnt, kupferfarben = blank
- Widerstandsmessung: erhöhter Widerstand gegenüber Nennwert zeigt Korrosion

**Behebung:**
1. **Langfristig:** Alle nicht-verzinnten Kabel systematisch durch Marine-Grade ersetzen
2. **Kurzfristig:** Kabelenden großzügig abschneiden (korrodierter Bereich + 10 cm)
3. Neue Kabelschuhe/Crimpverbinder aufbringen
4. Verbindungen mit Schrumpfschlauch + Kleber versiegeln
5. Alle 6 Monate inspizieren bis Kabel getauscht sind

**AYDI-Bewertung:**
- Confidence: visual_medium (an Kabelenden erkennbar)
- Severity: MITTEL (langfristiger Schaden)
- Repair urgency: Saisonende (systematische Erneuerung planen)

### 6.6 Fehlerbild: Kalte Lötstelle

**Beschreibung:** Eine Lötstelle, bei der das Lötzinn nicht vollständig mit dem Leiter verschmolzen ist. Die Oberfläche erscheint matt und körnig statt glatt und glänzend.

**Ursache:**
- Lötkolben zu kalt oder zu kurze Lötzeit
- Leiter oder Kabelschuh nicht vorgewärmt
- Flussmittel verbraucht bevor Lötzinn floss
- Bewegung während der Abkühlung
- Verschmutzte/korrodierte Oberfläche

**Wichtig:** ABYC E-11 erlaubt Löten als alleinige mechanische Verbindung NICHT. Gelötet werden darf nur als zusätzliche Versiegelung einer mechanischen Verbindung (Crimp oder Schraube). Grund: Lot hat geringen Schmelzpunkt, eine rein gelötete Verbindung kann unter thermischer Belastung brechen.

**Diagnose:**
- Visuell: matte, körnige, klumpige Lötstelle (statt glatt und glänzend)
- Zugtest: kalte Lötstelle lässt sich oft mit wenig Kraft lösen
- Widerstandsmessung: erhöhter Übergangswiderstand

**Behebung:**
1. Lötstelle entfernen
2. Verbindung als Crimp-Verbindung neu herstellen (ABYC-konform)
3. Wenn Löten gewünscht: Korrekt mit geeignetem Flussmittel und ausreichend Temperatur nachlöten, nur als Zusatz zur mechanischen Verbindung

**AYDI-Bewertung:**
- Confidence: visual_medium (unter Schrumpfschlauch nicht sichtbar)
- Severity: MITTEL (Übergangswiderstand, potenziell Ausfall)
- Repair urgency: Bei nächster Wartung

### 6.7 Fehlerbild: Elektrolyse/Galvanische Korrosion an Kabelverbindungen

**Beschreibung:** Unterschiedliche Metalle in einer Verbindung (z.B. Kupferkabel an Edelstahl-Klemme, Aluminiumgehäuse an Messing-Kabelschuh) erzeugen bei Feuchtigkeitspräsenz eine galvanische Zelle. Das unedlere Metall korrodiert beschleunigt.

**Ursache:**
- Mischung von Metallen verschiedener Stellung in der galvanischen Spannungsreihe
- Feuchtigkeit (Elektrolyt) an der Verbindungsstelle
- Fehlende Isolierung zwischen ungleichen Metallen
- Häufig: Kupferkabel an Aluminium-Gehäuse ohne Übergangsverbinder

**Diagnose:**
- Visuell: weißes/graues Pulver (Aluminium-Korrosion) oder grüne Ablagerungen (Kupfer-Korrosion) an der Verbindungsstelle
- Verbindung löst sich bei leichtem Zug
- Widerstand steigt

**Behebung:**
1. Verbindung trennen
2. Korrosion mechanisch entfernen (Drahtbürste)
3. Übergangsverbinder verwenden (z.B. Kupfer-Aluminium-Bimetall-Kabelschuh)
4. Korrosionsschutzpaste auftragen (z.B. Burndy Penetrox, Alu-Kontaktfett)
5. Verbindung mit Schrumpfschlauch versiegeln
6. Alternativ: gleiche Materialien verwenden

**AYDI-Bewertung:**
- Confidence: visual_high (weiße/grüne Ablagerungen sichtbar)
- Severity: MITTEL
- Repair urgency: 2–4 Wochen

### 6.8 Fehlerbild: Wassereinbruch in Kabelkanal

**Beschreibung:** Wasser sammelt sich in Kabelkanälen, Rohren oder Leerrohren und führt zur großflächigen Korrosion aller enthaltenen Kabel.

**Ursache:**
- Undichte Decksdurchführung
- Kondensation in nicht belüfteten Kabelkanälen
- Fehlende Tropfschleifen (Drip Loops)
- Kabelkanal ohne Drainage

**Diagnose:**
- Visuell: Wasser/Feuchtigkeit im Kabelkanal sichtbar
- Kabel fühlen sich feucht an
- Isolierungsmessung: reduzierter Isolationswiderstand (Megger-Test <1 MΩ)

**Behebung:**
1. Wasserquelle identifizieren und abdichten
2. Kabelkanal trocknen (Druckluft, Trockenmittel)
3. Alle Kabel im Kanal auf Korrosion prüfen
4. Korrodierte Kabel ersetzen
5. Drainage-Bohrung im tiefsten Punkt des Kabelkanals
6. Tropfschleifen an Decksdurchführungen nachrüsten

**AYDI-Bewertung:**
- Confidence: visual_medium (oft versteckt in Verkleidungen)
- Severity: HOCH (großflächiger Schaden möglich)
- Repair urgency: 1–2 Wochen

### 6.9 Fehlerbild: Scheuerstelle durch falsche Verlegung

**Beschreibung:** Kabel reibt an einer scharfen Kante, einem Schott-Durchbruch oder einem beweglichen Teil. Über die Zeit scheuert die Isolierung durch, es entsteht ein Kurzschluss oder Erdschluss.

**Ursache:**
- Fehlende Kantenschutz-Tüllen an Schott-Durchbrüchen
- Kabel nicht fixiert, scheuert an Ecken/Kanten
- Kabel an beweglichen Teilen entlanggeführt (Schublade, Tür, Motorhalterung)
- Falsche Kabelschellen (Metall auf Kabel statt Gummi-beschichtete Schellen)

**Diagnose:**
- Visuell: abgescheuerter Mantel/Isolierung
- Auf durchscheuerungsgefährdete Stellen systematisch absuchen
- Isolierungsmessung: reduzierter Isolationswiderstand

**Behebung:**
1. Schadstelle lokalisieren
2. Beschädigtes Kabel ersetzen (nicht reparieren!)
3. Kantenschutz-Tülle (PVC oder Gummi) am Durchbruch montieren
4. Kabelschellen mit Gummieinsatz verwenden (Edelstahl-Bügelschellen mit Gummipolster)
5. Kabel in Schutzschlauch verlegen (Spiralschlauch, Wellrohr)
6. Kabel mit Kabelbinder fixieren (UV-beständig, schwarz)

**AYDI-Bewertung:**
- Confidence: visual_high (sichtbar bei Inspektion)
- Severity: HOCH (Kurzschluss-/Brandgefahr)
- Repair urgency: Sofort

### 6.10 Fehlerbild: Überhitzte Crimpverbindung

**Beschreibung:** Crimpverbindung verfärbt sich bräunlich/schwarz, Isolierung in der Nähe schmilzt oder wird weich. Brandgeruch möglich.

**Ursache:**
- Falscher Querschnitt des Crimpverbinders (zu groß → Kontaktfläche zu klein)
- Unzureichende Verpressung (Crimpzange nicht korrekt eingestellt)
- Oxidierter/korrodierter Leiter vor dem Crimpen nicht gereinigt
- Zu hoher Strom für die Verbindung

**Diagnose:**
- Visuell: Verfärbung, geschmolzene Isolierung
- Infrarot-Thermometer: Hot-Spot >80°C unter Last
- Berührung: Verbindung warm/heiß unter Last (Achtung: Verbrennungsgefahr!)

**Behebung:**
1. Stromkreis sofort freischalten
2. Verbindung trennen
3. Kabelende frisch abisolieren (min. 10 cm ab Schadstelle)
4. Passenden Crimpverbinder (Querschnitt muss exakt passen)
5. Professionelle Crimpzange verwenden (Ratschentyp mit korrektem Einsatz)
6. Nach dem Crimpen: Zug-Test (>5 kg Zugkraft muss halten)
7. Mit Schrumpfschlauch versiegeln

**AYDI-Bewertung:**
- Confidence: visual_high (Verfärbung sichtbar)
- Severity: KRITISCH (Brandgefahr!)
- Repair urgency: SOFORT

### 6.11 Fehlerbild: Falsch abgesicherte Leitung

**Beschreibung:** Sicherung (oder Automaten-Schutzschalter) ist größer dimensioniert als die Kabelbelastbarkeit erlaubt. Bei Kurzschluss oder Überlast schmilzt die Sicherung nicht rechtzeitig — das Kabel überhitzt zuerst.

**Ursache:**
- Unwissenheit: „Die 10A-Sicherung flog immer, also habe ich 25A eingesetzt"
- Verwechslung: Sicherung schützt NICHT den Verbraucher, sondern das KABEL
- Laieninstallation: Verbraucher hinzugefügt, Sicherung vergrößert, Kabel aber nicht

**Diagnose:**
1. Sicherungswert ablesen
2. Kabelquerschnitt bestimmen
3. Vergleich: Sicherung > Kabelbelastbarkeit? → Fehlerhaft

**Beispiel:**
- Kabel: 1,5 mm² (15A Belastbarkeit bei 30°C)
- Sicherung: 25A
- → Kabel kann bei 20A schmelzen, Sicherung greift erst bei 25A → BRANDGEFAHR

**Behebung:**
1. Sicherung auf Kabelbelastbarkeit absenken
2. Wenn Verbraucher mehr Strom benötigt: Kabel vergrößern UND dann Sicherung anpassen
3. Regel: Sicherung ≤ 80% der Kabelbelastbarkeit (Dauerbetrieb)

**AYDI-Bewertung:**
- Confidence: measured (Querschnitt + Sicherungswert = Berechnung)
- Severity: KRITISCH (Brandgefahr!)
- Repair urgency: SOFORT

### 6.12 Fehlerbild: Salzwasser-Kriechstrom (Earth Leakage)

**Beschreibung:** Salzwasser auf Kabel- oder Steckverbinder-Oberflächen bildet einen leitenden Film, der Kriechströme zwischen Leitern oder zwischen Leiter und Masse ermöglicht. Führt zu Batterie-Entladung, Fehlfunktionen und beschleunigter Korrosion.

**Ursache:**
- Unzureichende Isolierung von Verbindungen im Spritzwasserbereich
- Salzablagerungen in Schalttafeln und Sicherungskästen
- Kondensation in nicht-belüfteten Elektro-Gehäusen
- Salzaerosol (Sea Spray) dringt in offene Verbindungen ein

**Symptome:**
- Batterie entlädt sich über Nacht ohne erkennbaren Verbraucher
- Sicherung löst ohne erkennbare Ursache
- Kompass zeigt Abweichung (Magnetfeld durch Kriechstrom)
- Korrosionsspuren an Kabelverbindern im Spritzwasserbereich

**Diagnose:**
1. Alle Verbraucher ausschalten, Hauptschalter aus
2. Amperemeter in Serie mit Batterie: Ruhestrom messen
3. >50 mA Ruhestrom deutet auf Kriechstrom hin
4. Sicherungen einzeln ziehen und Ruhestrom beobachten → Stromkreis lokalisieren
5. Isolationswiderstand mit Megger (500V) messen: <1 MΩ = problematisch

**Behebung:**
1. Betroffene Verbindungen reinigen (Süßwasser + Kontaktreiniger)
2. Trocknen (Druckluft)
3. Verbindungen mit Schrumpfschlauch + Kleber versiegeln
4. Schaltkasten mit Trockenmittel bestücken
5. Alle Verbindungen im Spritzwasserbereich mit Korrosionsschutz (z.B. CRC Marine, Boeshield T-9) einsprühen
6. Langfristig: wasserdichte Gehäuse (IP65+) für alle Verteiler im Außenbereich

**AYDI-Bewertung:**
- Confidence: measured (Kriechstrom messbar) oder visual_low (optisch schwer erkennbar)
- Severity: MITTEL (Batterieproblem, Funktionsstörung) bis HOCH (beschleunigte Korrosion)
- Repair urgency: 1–2 Wochen

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Verbraucher funktioniert nicht

```
START: Verbraucher funktioniert nicht
│
├─ Sicherung prüfen
│  ├─ Sicherung durchgebrannt?
│  │  ├─ JA → Warum?
│  │  │  ├─ Kurzschluss im Verbraucher?
│  │  │  │  ├─ Verbraucher abklemmen, neue Sicherung → hält?
│  │  │  │  │  ├─ JA → Verbraucher defekt → Reparatur/Tausch
│  │  │  │  │  └─ NEIN → Kurzschluss in der Leitung
│  │  │  │  │     ├─ Kabelisolierung prüfen (Scheuerstellen?)
│  │  │  │  │     ├─ Verbindungen prüfen (lose Klemmen?)
│  │  │  │  │     └─ Kabel durchgängig auf Beschädigungen prüfen
│  │  │  ├─ Überlast?
│  │  │  │  ├─ Strom messen (Zangenamperemeter)
│  │  │  │  ├─ Strom > Sicherungswert? → Verbraucher defekt oder falsche Sicherung
│  │  │  │  └─ Strom < Sicherungswert → Sicherung ermüdet → neue Sicherung
│  │  │  └─ Falsche Sicherung (zu klein)?
│  │  │     └─ Sicherung gegen korrekte Größe tauschen (≤ Kabelbelastbarkeit)
│  │  └─ NEIN → Sicherung OK
│  │     ├─ Spannung am Verbraucher messen
│  │     │  ├─ 0V → Leitungsunterbrechung
│  │     │  │  ├─ Kabel durchgangsprüfen (Multimeter Durchgangsprüfer)
│  │     │  │  ├─ Schalter prüfen (Kontakt?)
│  │     │  │  ├─ Steckverbinder prüfen
│  │     │  │  └─ Kabelbruch (→ Fehlerbild 6.2)
│  │     │  ├─ Spannung vorhanden aber zu niedrig
│  │     │  │  ├─ Spannungsabfall in Leitung messen
│  │     │  │  │  ├─ Spannungsabfall >3% → Kabel zu dünn oder zu lang (→ 6.4)
│  │     │  │  │  └─ Spannungsabfall >10% → korrodierte Verbindung (→ 6.1)
│  │     │  │  └─ Batteriespannung prüfen
│  │     │  │     └─ Batterie schwach? → Laden oder tauschen
│  │     │  └─ Spannung korrekt → Verbraucher selbst defekt
│  │     └─ Masse-Rückleitung prüfen
│  │        ├─ Masseverbindung korrodiert? → Reinigen/erneuern
│  │        └─ Masseband unterbrochen? → Neu verlegen
│  └─ Sicherungshalter korrodiert?
│     └─ JA → Sicherungshalter ersetzen, Verbindungen reinigen
│
└─ ENDE
```

### 7.2 Entscheidungsbaum: Batterie entlädt sich über Nacht

```
START: Batterie entlädt sich ohne erkennbaren Verbraucher
│
├─ Ruhestrom messen
│  ├─ Alle Verbraucher aus, Hauptschalter EIN
│  ├─ Amperemeter zwischen Batterie-Pol und Kabel
│  ├─ Ruhestrom <50 mA?
│  │  └─ JA → Normal (Uhren, Speicher, CO-Melder)
│  │     └─ Batterie prüfen (Alter, Kapazität, Innenwiderstand)
│  └─ Ruhestrom >50 mA?
│     ├─ Sicherungen einzeln ziehen
│     │  ├─ Ruhestrom sinkt beim Ziehen einer Sicherung?
│     │  │  └─ JA → Verbraucher in diesem Stromkreis identifizieren
│     │  │     ├─ Verbraucher an? → Ausschalten
│     │  │     ├─ Verbraucher aus, trotzdem Strom? → Defekter Schalter oder Kriechstrom
│     │  │     ├─ Relais hängt? → Relais tauschen
│     │  │     └─ Kriechstrom durch Feuchtigkeit? (→ 6.12)
│     │  └─ NEIN → Ruhestrom unverändert nach allen Sicherungen?
│     │     ├─ Verbraucher vor den Sicherungen prüfen
│     │     │  ├─ Bilgenpumpe (oft direkt an Batterie)?
│     │     │  ├─ Batterieladegerät?
│     │     │  └─ Nicht dokumentierte Abzweigung?
│     │     └─ Kriechstrom über Kabeloberfläche (Salz)? → Reinigen
│     └─ Ruhestrom >1A?
│        ├─ ACHTUNG: Erheblicher Verbraucher aktiv
│        ├─ Kühlschrank vergessen?
│        ├─ Inverter auf Stand-by?
│        ├─ Bilgenpumpe läuft dauerhaft (Leck im Rumpf!)?
│        └─ Kurzschluss in Leitung?
│
└─ ENDE
```

### 7.3 Entscheidungsbaum: Spannungsabfall am Verbraucher

```
START: Verbraucher arbeitet schwach (Licht dim, Motor langsam)
│
├─ Batteriespannung unter Last messen
│  ├─ Batteriespannung OK (12V: >12,4V; 24V: >24,8V)?
│  │  ├─ JA → Problem in der Leitung
│  │  │  ├─ Spannung am Verbraucher messen
│  │  │  │  ├─ Differenz = Spannungsabfall in Hinleitung + Rückleitung
│  │  │  │  ├─ >3% bei kritischem Verbraucher? → Leitung prüfen
│  │  │  │  └─ >10% bei nicht-kritischem Verbraucher? → Leitung prüfen
│  │  │  ├─ Schrittweise Spannung an Verbindungspunkten messen
│  │  │  │  ├─ Großer Spannungsabfall an einer Klemme?
│  │  │  │  │  └─ Korrodierte/lose Verbindung (→ 6.1, 6.7, 6.10)
│  │  │  │  ├─ Gleichmäßiger Spannungsabfall über Kabellänge?
│  │  │  │  │  └─ Kabel unterdimensioniert (→ 6.4) oder zu lang
│  │  │  │  └─ Spannungsabfall in Rückleitung?
│  │  │  │     └─ Masseverbindung prüfen (Bonding, Masseband)
│  │  │  └─ Kabelquerschnitt prüfen → Soll-Ist-Vergleich
│  │  └─ NEIN → Batterieproblem
│  │     ├─ Batterie laden und erneut testen
│  │     ├─ Innenwiderstand messen (Batterietester)
│  │     ├─ Batterie alt (>5 Jahre Blei-Säure, >8 Jahre AGM)?
│  │     └─ Batterie defekt → Tausch
│  └─ Batteriespannung bricht unter Last stark ein?
│     └─ → Batterie defekt oder Ladegerät-Problem
│
└─ ENDE
```

### 7.4 Entscheidungsbaum: UKW-Funkgerät — Schlechte Reichweite

```
START: UKW-Funk hat geringe Reichweite oder hohen SWR
│
├─ SWR am Funkgerät ablesen (falls Anzeige vorhanden)
│  ├─ SWR >3:1?
│  │  ├─ JA → Antennen- oder Kabeldefekt
│  │  │  ├─ Koaxialkabel prüfen
│  │  │  │  ├─ Kabeltyp korrekt (50 Ω)?
│  │  │  │  │  └─ NEIN (z.B. 75 Ω TV-Kabel) → Kabel ersetzen
│  │  │  │  ├─ Stecker korrekt montiert?
│  │  │  │  │  ├─ PL-259 Innenleiter korrekt gelötet?
│  │  │  │  │  ├─ Schirmung nicht auf Innenleiter?
│  │  │  │  │  └─ Stecker oxidiert/korrodiert? → Neu konfektionieren
│  │  │  │  ├─ Kabel geknickt oder gequetscht?
│  │  │  │  │  └─ JA → Kabel ersetzen (reparieren nicht möglich)
│  │  │  │  ├─ Wasser im Kabel (Kapillareffekt)?
│  │  │  │  │  └─ JA → Kabel ersetzen
│  │  │  │  └─ Kabellänge korrekt? Dämpfung berechnen
│  │  │  │     └─ Zu lang? → Kürzeres/besseres Kabel (RG-213 statt RG-58)
│  │  │  ├─ Antenne prüfen
│  │  │  │  ├─ Antennenstab intakt?
│  │  │  │  ├─ Antennenanschluss trocken?
│  │  │  │  ├─ Antennenmontage korrekt (Grundplatte/Erdungsebene)?
│  │  │  │  └─ Antenne gealtert (>10 Jahre)? → Tausch erwägen
│  │  │  └─ Verbindung Antenne ↔ Kabel
│  │  │     ├─ Korrosion am Stecker?
│  │  │     └─ Wasser an der Verbindung?
│  │  └─ NEIN (SWR <3:1 aber Reichweite trotzdem gering)
│  │     ├─ Antennenhöhe?
│  │     │  └─ UKW ist Sichtverbindung — Höhe = Reichweite
│  │     ├─ Sendeleistung korrekt eingestellt (25W High)?
│  │     ├─ Kabeldämpfung zu hoch? (→ Vergleichstabelle 3.4.5)
│  │     └─ Funkgerät defekt? → Service/Austausch
│  └─ SWR <1.5:1 → Antennensystem in Ordnung, Reichweite physikalisch bedingt
│
└─ ENDE
```

### 7.5 Entscheidungsbaum: NMEA 2000 Netzwerk — Gerät nicht erkannt

```
START: NMEA 2000 Gerät wird im Netzwerk nicht angezeigt
│
├─ Versorgungsspannung am Netzwerk prüfen
│  ├─ Spannung am T-Stück des betroffenen Geräts messen
│  │  ├─ 0V → Netzwerk ohne Strom
│  │  │  ├─ Sicherung des NMEA 2000 Netzwerks prüfen
│  │  │  ├─ Versorgungskabel (Power-T) prüfen
│  │  │  └─ Backbone-Kabel-Unterbrechung?
│  │  ├─ <9V → Spannungsabfall zu hoch
│  │  │  ├─ Zu viele Geräte am Netzwerk? (Max. 50 Geräte, max. 3A)
│  │  │  ├─ Versorgungskabel zu dünn?
│  │  │  └─ Zu wenige/falsche Power-T-Stücke?
│  │  └─ 9–16V → Versorgung OK
│  │     ├─ Terminierung prüfen
│  │     │  ├─ Genau 2 Terminatoren (120 Ω) am Backbone?
│  │     │  │  ├─ 0 oder 1 Terminator → Terminator ergänzen
│  │     │  │  ├─ 3+ Terminatoren → Überschüssige entfernen
│  │     │  │  └─ 2 Terminatoren → OK, weiter prüfen
│  │     │  └─ Gesamtwiderstand Backbone messen: soll ~60 Ω sein
│  │     ├─ Stichleitung prüfen
│  │     │  ├─ Stichleitung >6m? → Verkürzen auf ≤6m
│  │     │  ├─ Stichleitung beschädigt? → Ersetzen
│  │     │  └─ Stecker am Gerät korrekt? (Klick-Verriegelung prüfen)
│  │     ├─ Backbone prüfen
│  │     │  ├─ Backbone >100m? → Repeater einsetzen oder kürzen
│  │     │  ├─ Backbone-Kabel korrekt (DeviceNet Micro-C, 120 Ω)?
│  │     │  │  └─ NEIN (z.B. normales Steuerkabel) → Backbone-Kabel ersetzen
│  │     │  └─ T-Stücke korrekt verriegelt?
│  │     ├─ Gerät selbst prüfen
│  │     │  ├─ Gerät einzeln am Netzwerk testen (nur Gerät + 2 Terminatoren)
│  │     │  │  ├─ Funktioniert? → Problem am Hauptnetzwerk (Position, Kabel)
│  │     │  │  └─ Funktioniert nicht → Gerät defekt
│  │     │  └─ Firmware-Update des Geräts prüfen
│  │     └─ EMV-Problem?
│  │        ├─ Backbone neben Stromkabeln verlegt? → Trennen (min. 10 cm)
│  │        └─ Motor-Störungen? → Entstörfilter am Power-T
│
└─ ENDE
```

---

## 8. FAQ — Häufige Fragen

### 8.1 Grundlagen

**F1: Warum darf ich kein Automobil-Kabel auf meinem Boot verwenden?**
Automobil-Kabel (z.B. FLRY, FLY) verwenden blankes Kupfer, nicht verzinntes. In der Salzwasserumgebung korrodieren die Litzen innerhalb weniger Jahre, der Übergangswiderstand steigt, und im schlimmsten Fall entsteht ein Kabelbrand. Zudem sind die Isolierungsmaterialien nicht für die hohe Luftfeuchtigkeit und UV-Belastung an Bord ausgelegt.

**F2: Was bedeutet "Marine Grade"?**
Marine-Grade-Kabel zeichnen sich durch drei Merkmale aus: (1) Alle Kupferlitzen sind galvanisch verzinnt. (2) Die Isolierung ist für erhöhte Feuchtigkeit, UV und Temperaturwechsel geeignet. (3) Der Leiter ist feindrähtig (Klasse 5 oder 6 nach IEC 60228) für Vibrationsfestigkeit. In den USA ist UL 1426 "Boat Cable" der offizielle Standard.

**F3: Muss auf einem Binnenboot ebenfalls verzinntes Kupfer verwendet werden?**
Streng genommen: Süßwasser ist weniger aggressiv als Salzwasser. Faktisch: Auch Binnenboote erleben Kondensation, Spritzwasser und hohe Luftfeuchtigkeit. Die Empfehlung ist eindeutig: Ja, auch auf Binnenbooten Marine-Grade verwenden. Der Preisaufschlag von 15–25% rechnet sich über die Lebensdauer.

**F4: Wie erkenne ich, ob mein Kabel verzinnt ist?**
Abisolieren und die Litzen betrachten: Silbrig-weiße Litzen = verzinnt. Rötlich-goldene Litzen = blankes Kupfer. Im Zweifelsfall mit einem Messer an einer Litze kratzen — unter der Oberfläche kupferfarben = blankes Kupfer.

**F5: Warum ist der Faktor 2 in der Spannungsabfall-Formel?**
Strom fließt von der Batterie zum Verbraucher (Hinleitung) und vom Verbraucher zurück zur Batterie (Rückleitung). Auf BEIDEN Leitungen entsteht Spannungsabfall. Die effektive Kabellänge ist daher doppelt so lang wie der Abstand Batterie–Verbraucher.

### 8.2 Querschnittswahl

**F6: Nach welchem Kriterium dimensioniere ich den Kabelquerschnitt — Spannungsabfall oder Strombelastbarkeit?**
Immer nach BEIDEN Kriterien berechnen, der größere Querschnitt gewinnt. In der Praxis ist bei langen Kabelwegen im 12V-System fast immer der Spannungsabfall das bestimmende Kriterium. Bei kurzen, hochbelasteten Leitungen (z.B. Batterie–Sicherungskasten) bestimmt die Strombelastbarkeit.

**F7: Was ist besser — einen Querschnitt größer nehmen oder exakt berechnen?**
Immer eine Stufe größer als berechnet wählen. Es gibt keinen Nachteil durch einen etwas größeren Querschnitt (außer Gewicht und Kosten), aber erhebliche Risiken bei Unterdimensionierung.

**F8: Ich habe ein 24V-System. Brauche ich nur halb so dicke Kabel wie bei 12V?**
Theoretisch ja — bei gleicher Leistung fließt bei 24V nur der halbe Strom, und der Spannungsabfall in Prozent ist bei gleicher absoluter Differenz nur halb so groß. In der Praxis sind die Einsparungen etwas geringer, weil bei 24V-Systemen oft auch leistungsstärkere Verbraucher installiert werden.

**F9: Kann ich zwei dünnere Kabel parallel verwenden statt eines dicken?**
Ja, das ist zulässig und manchmal sogar vorteilhaft (z.B. wenn das dicke Kabel nicht durch eine Durchführung passt). Die Querschnitte addieren sich: 2× 35 mm² = 70 mm². Beide Kabel müssen identischen Querschnitt haben, gleich lang sein und JEDES Kabel einzeln abgesichert werden.

**F10: Gilt der maximal zulässige Spannungsabfall von 3% auch für LED-Beleuchtung?**
LED-Beleuchtung ist ein nicht-kritischer Verbraucher, daher sind bis zu 10% zulässig. ABER: LEDs reagieren empfindlicher auf Spannungsschwankungen als Glühbirnen — bei starkem Spannungsabfall kann das Dimm-Verhalten leiden. Empfehlung: 5% als praxisnahen Kompromiss ansetzen.

### 8.3 Verbindungstechnik

**F11: Löten oder Crimpen — was ist besser auf einem Boot?**
Crimpen. Die ABYC E-11 erlaubt Löten nur als Ergänzung zu einer mechanischen Verbindung, nicht als alleinige Verbindungsmethode. Gründe: (1) Lot kann bei Vibration brechen. (2) Lot schmilzt bei Überlast, bevor die Sicherung auslöst. (3) Lötzinn erzeugt eine starre Zone im flexiblen Kabel → Bruchstelle. Eine korrekte Crimpverbindung ist gasdicht und hat eine Lebensdauer >20 Jahre.

**F12: Welche Crimpzange brauche ich?**
Eine Ratschenzange mit austauschbaren Einsätzen für den jeweiligen Verbinder-Typ. Billige Quetschzangen erzeugen keine reproduzierbaren, gasdichten Verbindungen. Empfehlung: Knipex 97 52 (mit passenden Einsätzen) oder Ancor Professional Crimper. Budget: 60–150 EUR.

**F13: Wie teste ich, ob eine Crimpverbindung gut ist?**
Zugtest: mindestens 5 kg Zugkraft muss die Verbindung aushalten, ohne sich zu lösen. Visuell: Der Crimp muss symmetrisch sein, die Isolierung des Verbinders darf nicht aufgerissen sein, und der Leiter muss durch das Sichtfenster (falls vorhanden) sichtbar sein. Elektrisch: Übergangswiderstand <0,01 Ω.

**F14: Was ist ein Schrumpfschlauch mit Kleber und wann brauche ich ihn?**
Ein doppelwandiger Schrumpfschlauch mit einer inneren Schicht aus Schmelzkleber. Beim Erwärmen schmilzt der Kleber und dichtet die Verbindung wasserdicht ab. Auf einem Boot: IMMER den Typ mit Kleber verwenden. Ohne Kleber kriecht Feuchtigkeit unter den Schrumpfschlauch.

**F15: Darf ich Wago-Klemmen auf einem Boot verwenden?**
Nein. Wago-Klemmen (Federklemmen) sind für die feste Gebäudeinstallation konzipiert, nicht für die Vibrationsumgebung eines Bootes. Durch Schläge und Vibrationen können sich die Kontakte lockern. Verwenden Sie stattdessen Crimpverbinder, Reihenklemmen (Phoenix Contact, Weidmüller) oder Schraubklemmen (mit Federring gesichert).

### 8.4 Verlegung

**F16: Wie befestige ich Kabel korrekt?**
Kabel alle 30–50 cm mit Kabelschellen (Edelstahl mit Gummieinsatz) oder UV-beständigen Kabelbindern fixieren. NIEMALS Kabel lose verlegen — Vibrationen verursachen Scheuerstellen. An Schott-Durchbrüchen immer Kantenschutztüllen verwenden.

**F17: Dürfen Strom- und Datenkabel zusammen verlegt werden?**
Nicht ideal. Stromkabel (besonders DC-Hochstrom und AC) können elektromagnetische Störungen in Datenkabel einkoppeln. Empfehlung: Mindestens 10 cm Abstand zwischen Strom- und Datenkabeln. NMEA 2000 und Ethernet-Kabel separat von Batteriekabeln verlegen. Kreuzen sich die Kabel, dann im 90°-Winkel.

**F18: Wie führe ich Kabel durch Schotten?**
Bohrung im Schott mit Durchmesser Kabelbündel + 10 mm. Gummi-Kabeldurchführung (Kabeltülle) einsetzen. Wenn wasserdicht erforderlich: IP67-Kabelverschraubung verwenden. NIEMALS Kabel durch scharfkantige Bohrungen ohne Tülle führen.

**F19: Was ist eine Tropfschleife (Drip Loop)?**
Eine U-förmige Schlaufe im Kabel, deren tiefster Punkt unterhalb der Durchführung liegt. Wasser, das am Kabel entlang läuft, tropft am tiefsten Punkt der Schlaufe ab, statt durch die Durchführung in das Bootsinnere zu gelangen. Pflicht an jeder Decksdurchführung.

**F20: Wie schütze ich Kabel im Motorraum?**
(1) Silikonkabel oder XLPE-Kabel verwenden (≥90°C). (2) Mindestabstand 5 cm zum Auspuffkrümmer, 3 cm zum Motor. (3) Kabel in Wellrohr oder Schutzschlauch (Silikon-beschichtet). (4) Regelmäßig auf Ölkontamination prüfen — PVC wird durch Dieselöl angegriffen.

### 8.5 Spezielle Anwendungen

**F21: Welches Koaxialkabel brauche ich für mein UKW-Funkgerät?**
Abhängig von der Kabellänge: Bis 10m ist RG-58 oder RG-8X ausreichend. Über 10m empfiehlt sich RG-8X (geringere Dämpfung als RG-58). Über 20m oder bei SSB-Funk: RG-213. Immer 50 Ω Impedanz! Niemals 75-Ω-TV-Kabel verwenden.

**F22: Kann ich NMEA 2000 Kabel durch normales geschirmtes Kabel ersetzen?**
Nein. NMEA 2000 erfordert Kabel mit 120 Ω charakteristischer Impedanz. Standard-Steuerleitungen haben eine andere Impedanz, was zu Signalreflexionen und Kommunikationsfehlern führt. Verwenden Sie nur zertifiziertes NMEA 2000 / DeviceNet Micro-C Kabel.

**F23: Wie verlege ich Kabel im Mast?**
Vor dem Mastsetzen alle Kabel einziehen (mit Führungsleine). Kabel nicht frei im Mastprofil baumeln lassen — mit Schaumstoff-Abstandshaltern alle 2m fixieren, um Klappergeräusche und Scheuern zu verhindern. Am Mastfuß Tropfschleife und Zugentlastung. Mastkabel müssen hochflexibel sein (Klasse 6).

**F24: Wie dimensioniere ich die Verkabelung für eine Lithium-Batterie?**
Lithium-Batterien können deutlich höhere Ströme liefern als Blei-Batterien. Das BMS begrenzt den Strom, aber die Kabel müssen für den maximalen BMS-Ausgangsstrom dimensioniert sein. Zudem: Lithium-Systeme erfordern oft ein separates Lade-/Entlade-Kabel. Immer die Herstellervorgaben des BMS beachten.

**F25: Brauche ich für Solarpanels spezielle Kabel?**
Ja, PV-Kabel nach EN 50618 mit doppelter Isolierung und MC4-Steckern. Die höhere Spannung von Solarpanels (oft >50V bei Reihenschaltung) erfordert Kabel mit höherer Spannungsfestigkeit als Standard-12V-Bordkabel.

### 8.6 Wartung und Inspektion

**F26: Wie oft sollte ich die Bordelektrik inspizieren?**
Visuell: vor jeder Saison (Frühjahr). Elektrisch (Spannungsabfall, Isolationswiderstand): alle 2 Jahre. Vollständige Überprüfung durch Fachmann: alle 5 Jahre oder bei Besitzerwechsel. Zusätzlich: nach jedem schweren Sturm und nach jedem Mastlegen die Mastkabel prüfen.

**F27: Wie messe ich den Isolationswiderstand?**
Mit einem Isolationstester (Megger) bei 500V DC. Kabel beidseitig abklemmen. Tester zwischen Leiter und Masse/Erde anschließen. Messwert >100 MΩ: einwandfrei. 10–100 MΩ: akzeptabel, beobachten. 1–10 MΩ: auffällig, Ursache suchen. <1 MΩ: Isolationsfehler, Kabel ersetzen.

**F28: Kann ich korrodierte Kabelenden einfach abschneiden und neu anschließen?**
Ja, vorausgesetzt: (1) Das Kabel ist lang genug (Reserve-Schlaufe vorhanden). (2) Die Korrosion hat sich nicht unter die Isolierung weiter ins Kabel hinein gefressen. (3) Das verbleibende Kabel ist sichtbar verzinnt/unbeschädigt. Wenn die Korrosion unter der Isolierung sichtbar ist: gesamtes Kabel ersetzen.

**F29: Was gehört in die Bordapotheke für Kabel?**
Empfohlenes Kabel-Reparatur-Set für Blauwasser-Segler:
- Crimpzange (Ratschentyp) + Crimpverbinder sortiert (1,5–6 mm²)
- Kabelschuhe sortiert (Ringkabelschuhe, Flachstecker)
- Schrumpfschlauch mit Kleber, sortierte Durchmesser
- Marine-Kabel: je 10m in 1,5 / 2,5 / 4 mm² (Rot + Schwarz)
- Multimeter
- Isolierband (Scotch Super 33+)
- Kontaktreiniger (DeoxIT)
- Abisolierzange
- Kabelbinder UV-beständig (Beutel)
- Sicherungen (Ersatzset passend zur Bordanlage)

**F30: Was kostet eine vollständige Neuverkabelung?**
Richtwerte für die Kabelkosten (Material, ohne Arbeit):
- 10m-Segelboot: 2.000–4.000 EUR
- 12m-Segelboot: 4.000–8.000 EUR
- 15m-Motoryacht: 6.000–12.000 EUR
- 20m-Motoryacht: 10.000–25.000 EUR
Arbeitszeit (Profi-Werft): 200–800 EUR/Tag. Neuverkabelung eines 12m-Segelboots: typisch 2–4 Wochen = 15.000–40.000 EUR gesamt.

---

## 9. Glossar

| Nr. | Begriff | Erklärung |
|-----|---------|-----------|
| 1 | **ABYC E-11** | Standard der American Boat and Yacht Council für AC/DC-Systeme auf Booten |
| 2 | **Ampacity** | Maximale Dauerstrombelastbarkeit eines Kabels in Ampere |
| 3 | **AWG** | American Wire Gauge — US-Drahtmaßsystem, größere Zahl = dünnerer Draht |
| 4 | **Backbone** | Hauptstrang eines NMEA 2000 Netzwerks |
| 5 | **Biegeradius** | Minimaler Krümmungsradius, bis zu dem ein Kabel gebogen werden darf |
| 6 | **Bonding** | Verbindung aller metallischen Teile zur Potenzialausgleichsschiene |
| 7 | **Bündelungsfaktor** | Reduktionsfaktor für die Strombelastbarkeit bei gebündelter Verlegung |
| 8 | **CAN-Bus** | Controller Area Network — Datenbus-Protokoll, Basis für NMEA 2000 |
| 9 | **Crimpverbindung** | Mechanische Kabelverbindung durch Verpressen |
| 10 | **DeoxIT** | Markenname eines Kontaktreinigers/Korrosionsschutzmittels (Caig) |
| 11 | **DeviceNet Micro-C** | Kabel-/Steckerspezifikation für NMEA 2000 |
| 12 | **Drain Wire** | Ableitdraht in geschirmten Kabeln für den Erdungsanschluss |
| 13 | **Drip Loop** | Tropfschleife — U-förmige Kabelschlaufe als Wasserablauf |
| 14 | **EMV** | Elektromagnetische Verträglichkeit — Störfestigkeit und Störaussendung |
| 15 | **EPR** | Ethylen-Propylen-Kautschuk — hochwertige Kabelisolierung |
| 16 | **Erdschluss** | Unbeabsichtigter Strompfad zwischen Leiter und Erde/Masse |
| 17 | **FRNC** | Flame Retardant Non Corrosive — halogenfreier, flammwidriger Kabelmantel |
| 18 | **Galvanische Korrosion** | Korrosion durch Kontakt unterschiedlicher Metalle in einem Elektrolyten |
| 19 | **Grünspan** | Kupfer(II)-carbonat-hydroxid — grüne Korrosionsprodukte an Kupfer |
| 20 | **H07V-K** | Harmonisierte Einzeladerleitung, PVC-isoliert, feindrähtig |
| 21 | **HFFR** | Halogen Free Flame Retardant — halogenfreier flammwidriger Kabelmantel |
| 22 | **IP-Schutzart** | Ingress Protection — Schutzgrad gegen Fremdkörper und Wasser (z.B. IP67) |
| 23 | **Isolationswiderstand** | Widerstand zwischen Leiter und Erde — Maß für Isolationsqualität |
| 24 | **Kabelschelle** | Befestigungselement zur Fixierung von Kabeln an Oberflächen |
| 25 | **Kabelschuh** | Endstück am Kabel für die Verbindung mit Klemmen oder Bolzen |
| 26 | **Kabelkanal** | Kunststoff- oder Metallprofil zur geordneten Kabelverlegung |
| 27 | **Kriechstrom** | Ungewollter Stromfluss über Oberflächen (durch Feuchtigkeit/Verschmutzung) |
| 28 | **Litze** | Einzelner Draht innerhalb eines Kabelleiters |
| 29 | **Megger** | Isolationstester (Markenname, wird generisch verwendet) |
| 30 | **NMEA 0183** | Serielles Datenprotokoll für Navigationselektronik (älter) |
| 31 | **NMEA 2000** | CAN-Bus-basiertes Netzwerkprotokoll für marine Elektronik |
| 32 | **PUR** | Polyurethan — hochwertiger Kabelmantel, UV- und abriebfest |
| 33 | **PVC** | Polyvinylchlorid — Standard-Kabelisolierung |
| 34 | **Querschnitt** | Leiterfläche in mm² — bestimmt Strombelastbarkeit und Widerstand |
| 35 | **Ratschenzange** | Crimpzange mit Ratschenmechanismus für reproduzierbare Crimpkraft |
| 36 | **Rohrkabelschuh** | Kabelschuh für große Querschnitte (>10 mm²), wird auf das Kabel gepresst |
| 37 | **Schrumpfschlauch** | Kunststoffschlauch, der bei Erwärmung schrumpft und die Verbindung isoliert |
| 38 | **SWR** | Standing Wave Ratio — Stehwellenverhältnis, Maß für Antennenanpassung |
| 39 | **Terminierung** | 120-Ω-Abschlusswiderstand an NMEA 2000 Backbone-Enden |
| 40 | **Tropfschleife** | Siehe Drip Loop |
| 41 | **UL 1426** | US-Zertifizierung für Marine-Kabel ("Boat Cable") |
| 42 | **Verzinntes Kupfer** | Kupferlitzen mit galvanischer Zinnbeschichtung gegen Korrosion |
| 43 | **Wellrohr** | Gewelltes Kunststoffrohr als mechanischer Kabelschutz |
| 44 | **XLPE** | Vernetztes Polyethylen — hochwertige Kabelisolierung (90°C) |
| 45 | **Zugentlastung** | Mechanische Vorrichtung zur Aufnahme von Zugkräften am Kabelende |

---

## 10. Schnell-Referenz

### 10.1 Kabelquerschnitt-Schnellwahl (12V, 3% Spannungsabfall)

```
┌─────────────────────────────────────────────────────────┐
│  SCHNELLWAHL KABELQUERSCHNITT (12V, 3% max.)           │
│                                                         │
│  Strom × Kabelweg (einfach) → mm²                      │
│                                                         │
│  5A  × 5m  = 2,5 mm²    │  30A × 5m  = 16 mm²        │
│  5A  × 10m = 4 mm²      │  30A × 10m = 25 mm²        │
│  5A  × 15m = 6 mm²      │  30A × 15m = 50 mm²        │
│  10A × 5m  = 4 mm²      │  50A × 5m  = 25 mm²        │
│  10A × 10m = 10 mm²     │  50A × 10m = 50 mm²        │
│  10A × 15m = 16 mm²     │  50A × 15m = 70 mm²        │
│  20A × 5m  = 10 mm²     │  80A × 5m  = 35 mm²        │
│  20A × 10m = 16 mm²     │  80A × 10m = 70 mm²        │
│  20A × 15m = 25 mm²     │  80A × 15m = 95 mm²        │
│                                                         │
│  REGEL: Im Zweifel EINE Stufe größer!                   │
└─────────────────────────────────────────────────────────┘
```

### 10.2 Sicherungszuordnung (Maximal-Sicherung für Querschnitt)

```
┌──────────────────────────────────────────┐
│  MAXIMALE SICHERUNG je QUERSCHNITT       │
│                                          │
│  1,5 mm²  →  max. 15A                   │
│  2,5 mm²  →  max. 20A                   │
│  4 mm²    →  max. 25A                   │
│  6 mm²    →  max. 35A                   │
│  10 mm²   →  max. 50A                   │
│  16 mm²   →  max. 65A                   │
│  25 mm²   →  max. 85A                   │
│  35 mm²   →  max. 100A                  │
│  50 mm²   →  max. 125A                  │
│  70 mm²   →  max. 160A                  │
│  95 mm²   →  max. 200A                  │
│                                          │
│  (Einzelverlegung, 30°C, PVC-Isolation)  │
│  Bündelung/Temperatur → reduzieren!      │
└──────────────────────────────────────────┘
```

### 10.3 Checkliste: Marine-Kabel erkennen

```
┌──────────────────────────────────────────────┐
│  IST DAS KABEL MARINE-TAUGLICH?              │
│                                              │
│  ☐ Litzen silbrig-weiß (verzinnt)?          │
│  ☐ Feindrähtig (viele Einzellitzen)?         │
│  ☐ PVC/Nylon oder XLPE Isolierung?           │
│  ☐ Flexibel (lässt sich eng biegen)?         │
│  ☐ UL 1426, VDE oder GL-Kennzeichnung?       │
│  ☐ Temperaturbereich ≥ -20 bis +70°C?        │
│                                              │
│  < 4 Haken = NICHT für Marine geeignet       │
│  ≥ 4 Haken = Marine-tauglich                 │
│  6 Haken = Premium Marine                    │
└──────────────────────────────────────────────┘
```

### 10.4 Koaxialkabel-Schnellwahl

```
┌──────────────────────────────────────────────────────┐
│  KOAXIALKABEL SCHNELLWAHL                            │
│                                                      │
│  UKW-Funk, bis 10m Kabelweg:     RG-58 oder RG-8X   │
│  UKW-Funk, 10–20m Kabelweg:      RG-8X              │
│  UKW-Funk, >20m Kabelweg:        RG-213             │
│  SSB-Funk:                        RG-213 oder LMR-400│
│  AIS:                             RG-58 oder RG-8X   │
│  GPS-Antenne:                     RG-58              │
│  TV-Antenne, SAT:                 RG-6 (75 Ω!)      │
│                                                      │
│  ACHTUNG: Funk = 50 Ω  /  TV/SAT = 75 Ω            │
│  NIEMALS verwechseln!                                │
└──────────────────────────────────────────────────────┘
```

### 10.5 Farbcode-Schnellreferenz

```
┌──────────────────────────────────────────────┐
│  DC-FARBCODE (ABYC/ISO)                      │
│                                              │
│  ROT     = DC + (Batterie-Positiv)           │
│  SCHWARZ = DC - (Masse/Negativ)              │
│  GELB    = DC - (Alternative)                │
│  GRÜN    = Bonding/Erdung                    │
│                                              │
│  AC-FARBCODE (IEC / EU)                      │
│                                              │
│  BRAUN     = Phase L1                        │
│  SCHWARZ   = Phase L2                        │
│  GRAU      = Phase L3                        │
│  BLAU      = Neutral N                       │
│  GRÜN-GELB = Schutzleiter PE                 │
│                                              │
│  NMEA 2000                                   │
│                                              │
│  WEISS = CAN_H  │  BLAU = CAN_L             │
│  ROT   = +12V   │  SCHWARZ = GND            │
└──────────────────────────────────────────────┘
```

---

## ANHANG A — Fallstudie: Neuverkabelung Bavaria 37 (2004)

### A.1 Ausgangssituation

**Boot:** Bavaria 37 Cruiser, Baujahr 2004, 11,35m LOA
**Eigner:** Charterflotte → Privat, 18 Jahre alt bei Übernahme
**Problem:** Sporadische Ausfälle der Navigationsbeleuchtung, dimme Ankerwinsche, Batterien entladen sich schnell

### A.2 Diagnose

Befundaufnahme durch AYDI-Analyse (Level 2):

| Zone | Befund | Severity |
|------|--------|----------|
| Hauptschalttafel | 60% der Verbindungen nicht verzinnt (Bavaria-Standard 2004) | HOCH |
| Motorraum | PVC-Kabel spröde (Hitze), Isolierung rissig am Lichtmaschinenausgang | KRITISCH |
| Mastfuß | 3 von 8 Kabeln gebrochen (Positionslicht, Windex, Decksfluter) | HOCH |
| Bilge | Korrosion an allen Masseverbindungen, Grünspan | HOCH |
| Bugbereich | Ankerwinsche: 16 mm² statt 35 mm² (Spannungsabfall 8,7%) | MITTEL |
| NMEA-Netzwerk | Standard-Steuerkabel statt DeviceNet → Datenfehler | MITTEL |

### A.3 Maßnahmen

1. **Komplette Neuverkabelung DC-System** mit Ancor Marine Grade
2. **Neue Verteilertafel** (Philippi STV 632) mit korrekter Absicherung
3. **Batteriekabel** 50 mm² zu Ankerwinde (statt 16 mm²)
4. **Mastkabel** komplett neu (SAB Marine, Klasse 6)
5. **NMEA 2000 Netzwerk** mit zertifiziertem Backbone-Kabel
6. **Motorraum-Kabel** ersetzt durch Silikonkabel (ÖLFLEX HEAT 180)

### A.4 Ergebnis

| Kennzahl | Vorher | Nachher |
|----------|--------|---------|
| Spannungsabfall Ankerwinde | 8,7% | 2,1% |
| Ruhestrom | 320 mA | 45 mA |
| Isolationswiderstand (min.) | 0,8 MΩ | >500 MΩ |
| Gesamtkosten Material | — | 4.800 EUR |
| Arbeitszeit | — | 120 Stunden |
| Gesamtkosten | — | 14.200 EUR |

**AYDI-Score Elektrik:** 28/100 → 92/100

---

## ANHANG B — Fallstudie: Mastverkabelung Hallberg-Rassy 40 (2012)

### B.1 Ausgangssituation

**Boot:** Hallberg-Rassy 40 MkII, Baujahr 2012, 12,20m LOA
**Problem:** Intermittierendes Versagen des Masttoplichts und der Windmessanlage, besonders bei Seegang

### B.2 Diagnose

Mastabnahme und Inspektion ergab:
- Kabelbruch an 4 Positionen am Mastfuß (fehlende Tropfschleifen, enger Biegeradius)
- Korrosion an den Mastfuß-Steckverbindern (Standard-DIN-Stecker, nicht wasserdicht)
- Kabel im Mastprofil lose, Scheuerstellen an internen Verstärkungen

### B.3 Maßnahmen

1. Alle Mastkabel ersetzt durch SAB SABIX Klasse 6 (feinstdrähtig)
2. Mastfuß: 20 cm Tropfschleife + flexible PUR-Schutzschläuche
3. Steckverbinder ersetzt durch Tyco Deutsch DT-Serie (IP68, vibrationsgesichert)
4. Kabel im Mast alle 2m mit Schaumstoff-Abstandshaltern fixiert
5. Koaxialkabel (UKW) ersetzt durch Aircell 7 (geringere Dämpfung)

### B.4 Ergebnis

| Kennzahl | Vorher | Nachher |
|----------|--------|---------|
| Zuverlässigkeit Masttoplicht | ~60% | 100% |
| UKW-Reichweite (geschätzt) | 15 nm | 25 nm |
| Gesamtkosten | — | 3.200 EUR |

---

## ANHANG C — Fallstudie: Lithium-Umbau Catana 471 (2008)

### C.1 Ausgangssituation

**Boot:** Catana 471, Baujahr 2008, 14,27m LOA (Katamaran)
**Vorhaben:** Umrüstung von AGM-Batteriebank (4× 220Ah = 880Ah, 12V pro Rumpf) auf LiFePO4 (2× 200Ah = 400Ah, 24V pro Rumpf, Victron Smart Lithium)

### C.2 Kabel-Herausforderungen

- Umstellung von 12V auf 24V erfordert Anpassung vieler Verbraucher
- Lithium-BMS begrenzt Lade-/Entladestrom auf 200A → Kabel müssen diesen Strom führen
- Bestehende Kabelwege zwischen Rümpfen (Brücke) müssen geprüft werden
- Neue DC/DC-Wandler für 12V-Verbraucher benötigen eigene Verkabelung

### C.3 Maßnahmen

| Kabelstrecke | Alt | Neu | Grund |
|-------------|-----|-----|-------|
| Batterie → Hauptschalter | 70 mm², 12V | 50 mm², 24V | Halber Strom bei 24V |
| Hauptschalter → Verteiler | 50 mm², 12V | 35 mm², 24V | Halber Strom |
| Batterie → Inverter 3kW | 95 mm², 12V | 50 mm², 24V | Halber Strom |
| BMS-Kommunikation | — | Cat5e STP | Neu (Victron GX-System) |
| DC/DC 24V→12V | — | 25 mm² (Ein/Aus) | Neu |
| Rumpf-zu-Rumpf | 50 mm², 12V | 35 mm², 24V | Upgrade Stecker |

### C.4 Ergebnis

| Kennzahl | Vorher (12V AGM) | Nachher (24V LiFePO4) |
|----------|-------------------|----------------------|
| Gesamtkabelgewicht | ~85 kg | ~55 kg |
| Batteriegewicht | 260 kg | 52 kg |
| Nutzbare Kapazität | ~440 Ah (50% DOD) | ~360 Ah (90% DOD) |
| Spannungsabfall Inverter | 4,2% | 1,8% |
| Gesamtkosten Kabel | — | 2.800 EUR |

---

## ANHANG D — Fallstudie: Korrosionsschaden durch nicht-verzinntes Kabel (Jeanneau Sun Odyssey 42i)

### D.1 Ausgangssituation

**Boot:** Jeanneau Sun Odyssey 42i, Baujahr 2010, Mittelmeer (Griechenland)
**Problem:** Nach 12 Jahren: Vielzahl von Fehlfunktionen — Navigationslicht flackert, Bilgenpumpe läuft langsam, Kompass zeigt Deviation, Batterie-Lebensdauer drastisch reduziert

### D.2 Diagnose

Systematische Inspektion ergab:
- 70% der DC-Kabel waren Standard-Industriekabel (nicht verzinnt) — Jeanneau-Werftstandard 2010
- Fortgeschrittene Korrosion an allen Kabelenden, besonders im Bugbereich und Bilge
- Übergangswiderstand an Klemmen: 0,5–2,5 Ω (statt <0,01 Ω)
- Gesamter Ruhestrom: 1,2A (Kriechströme durch Korrosion)
- Geschätzter Leistungsverlust durch Korrosion: 15–20%

### D.3 Kostenbewertung: Sofort-Tausch vs. Abwarten

| Option | Kosten jetzt | Folgekosten (5 Jahre) | Risiko |
|--------|-------------|----------------------|--------|
| Komplette Neuverkabelung | 22.000 EUR | 0 EUR | Minimal |
| Nur kritische Kabel | 8.000 EUR | ~8.000 EUR (weitere Ausfälle) | Mittel |
| Abwarten | 0 EUR | >30.000 EUR (Schäden, Brandgefahr) | HOCH |

### D.4 Durchgeführte Maßnahme

Entscheidung: Komplette Neuverkabelung mit Ancor Marine Grade und Philippi-Verteilersystem.

**Ergebnis:** Ruhestrom von 1,2A auf 38 mA reduziert. AYDI-Score Elektrik: 22/100 → 95/100.

---

## ANHANG E — Fallstudie: NMEA 2000 Netzwerk-Fehler (Beneteau Oceanis 46.1)

### E.1 Ausgangssituation

**Boot:** Beneteau Oceanis 46.1, Baujahr 2020, 14,09m LOA
**Problem:** Sporadische Ausfälle einzelner NMEA 2000 Geräte (Windmessanlage, Autopilot-Heading-Sensor), Fehlermeldungen auf dem MFD

### E.2 Diagnose

1. Backbone-Kabel geprüft: Beneteau hatte teilweise Standard-Steuerkabel (LIYCY 2×0,5 mm²) statt DeviceNet Micro-C verbaut
2. Impedanzmessung: 85 Ω statt 120 Ω → Signalreflexionen
3. Terminierung: nur ein Terminator statt zwei
4. Stichleitung zum Masttop-Sensor: 9m (max. erlaubt: 6m)

### E.3 Maßnahmen

1. Backbone komplett durch zertifiziertes NMEA 2000 Kabel (Helukabel HELUSIGNAL 120) ersetzt
2. Zweiten Terminatorwiderstand installiert
3. Masttop-Stichleitung auf 5,5m verkürzt (Sensor tiefer montiert)
4. Alle T-Stücke auf korrekte Verriegelung geprüft

### E.4 Ergebnis

- Keine Kommunikationsfehler mehr seit Umbau (18 Monate Betrieb)
- Autopilot-Heading stabil, Windmessanlage zuverlässig
- Kosten: 650 EUR (Material) + 8 Stunden Arbeit

---

## ANHANG F — Fallstudie: Brandschaden durch Überbrückung der Sicherung (Charter-Yacht)

### F.1 Ausgangssituation

**Boot:** Bavaria 46 Cruiser, Baujahr 2016, Charterbetrieb
**Vorfall:** Brand im Bereich der Schalttafel während einer Charter. Keine Personenschäden, erheblicher Sachschaden.

### F.2 Ursachenkette

1. Chartergast bemerkte, dass die Kühlschranksicherung (10A) wiederholt auslöste
2. Gast überbrückte die Sicherung mit Alufolie
3. Kühlschrankkompressor hatte einen Windungsschluss → Strom stieg auf ~25A
4. Kabel (2,5 mm², 20A Belastbarkeit) erhitzte sich auf >150°C
5. PVC-Isolierung schmolz, Kurzschluss zu benachbarten Leitungen
6. Brand in der Schalttafel

### F.3 Lehren

- **Sicherungen NIEMALS überbrücken** — sie schützen das KABEL, nicht den Verbraucher
- **Charterbriefing** muss Elektrik-Grundlagen enthalten
- **Schalttafel-Design** sollte Manipulationssicherheit bieten
- **Rauchmelder** im Bereich der Schalttafel sind Pflicht

### F.4 AYDI-Relevanz

- Fehlerbild 6.11 (falsch abgesicherte Leitung) als Grundursache
- Automatische Prüfung: Sicherungswert ≤ Kabelbelastbarkeit für jeden Stromkreis
- Confidence: measured (Sicherungswert und Querschnitt berechenbar)

---

## ANHANG G — Fallstudie: Solar-Verkabelung Langfahrt-Yacht (Ovni 435)

### G.1 Ausgangssituation

**Boot:** Ovni 435, Aluminium-Segelboot, 13,25m LOA
**Vorhaben:** Installation von 1.200 Wp Solaranlage (4× 300Wp Panels auf Bimini/Arch)

### G.2 Kabel-Planung

| Strecke | Spannung | Strom (max.) | Länge | Querschnitt |
|---------|----------|-------------|-------|-------------|
| Panel → Junction Box | ~40V (Vmpp) | 10A (Impp pro Panel) | 2m | 6 mm² PV-Kabel |
| Junction Box → MPPT #1 | ~80V (2S Reihenschaltung) | 10A | 8m | 6 mm² PV-Kabel |
| Junction Box → MPPT #2 | ~80V (2S Reihenschaltung) | 10A | 8m | 6 mm² PV-Kabel |
| MPPT → Batterie | 24V | 40A (max. pro Regler) | 3m | 10 mm² Marine |
| MPPT → Batterie | 24V | 40A | 3m | 10 mm² Marine |

### G.3 Besonderheiten Aluminium-Boot

- **ACHTUNG:** Bei Aluminium-Booten ist galvanische Korrosion zwischen Kupferkabel und Aluminium-Struktur ein kritisches Thema
- Alle Kabeldurchführungen durch Aluminium-Schotten müssen mit Kunststoff-Tüllen isoliert sein
- Kein direkter Kontakt Kupfer–Aluminium an Masseverbindungen → Bimetall-Kabelschuhe verwenden
- Alle Kabelschellen: Kunststoff oder Edelstahl mit Kunststoffeinsatz, NICHT Aluminium

### G.4 Ergebnis

- Solarertrag: ~5–6 kWh/Tag (Mittelmeer, Sommer)
- Gesamtkosten Verkabelung: 480 EUR
- Spannungsabfall Panel–Batterie: <2%

---

## ANHANG H — Fallstudie: Superyacht DC-Bus-System (50m, 24V/48V)

### H.1 Ausgangssituation

**Boot:** Custom Motor-Yacht, 50m LOA, Baujahr 2024
**Architektur:** 48V DC-Bus für Antrieb + 24V DC-Bordnetz + 230V/400V AC

### H.2 Kabel-Dimensionen

| System | Spannung | Max. Strom | Querschnitt | Kabeltyp | Gesamtlänge |
|--------|----------|-----------|-------------|----------|-------------|
| DC-Bus (Antrieb) | 48V DC | 600A | 4× 240 mm² | SAB SABIX D 315 FRNC | 200m |
| Batterie-Bank | 48V DC | 400A | 2× 185 mm² | Nexans ALSECURE | 80m |
| Generator → Ladegerät | 400V AC | 200A | 3× 95 mm² | Nexans ALSECURE | 150m |
| Bordnetz DC | 24V DC | div. | 2,5–50 mm² | Helukabel HELUPOWER | 8.000m |
| Bordnetz AC | 230V AC | div. | 2,5–16 mm² | Nexans ALSECURE | 4.000m |
| Entertainment | Cat6a STP | — | — | Belden Marine | 2.000m |
| NMEA 2000 | — | — | DeviceNet | Helukabel | 300m |
| Sicherheitssysteme | 24V DC | div. | 1,5–4 mm² | SAB SABIX FRNC | 3.000m |

### H.3 Gesamtkabelgewicht und -kosten

| Parameter | Wert |
|-----------|------|
| Gesamtkabellänge | ~18.000m |
| Gesamtgewicht Kabel | ~2.800 kg |
| Materialkosten Kabel | ~180.000 EUR |
| Installationskosten | ~250.000 EUR |
| Anteil am Gesamtpreis (15 Mio.) | ~2,9% |

### H.4 Besondere Anforderungen

- Alle Kabel FRNC (Flame Retardant Non Corrosive) nach IEC 60332-3
- Rauchentwicklung nach IEC 61034 (geringe Rauchgasdichte)
- DNV-GL und Lloyd's Register Zertifizierung
- Redundante Verkabelung für alle sicherheitskritischen Systeme
- Kabelschottdurchführungen feuerfest (30 Minuten Feuerwiderstand)

---

## ANHANG I — AYDI-Integration: Pydantic v2 Basismodelle

```python
"""
AYDI Wissensmodul 22.03 — Kabel und Leitungen
Pydantic v2 Modelle für die Integration in die AYDI-Analyse-Engine.

WICHTIG: Pydantic v2 mit model_config = {"from_attributes": True}
         NIEMALS class Config verwenden!
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# ── Enums ────────────────────────────────────────────────────────

class CableGrade(str, Enum):
    """Kabel-Qualitätsstufe."""
    MARINE_PREMIUM = "marine_premium"
    MARINE_STANDARD = "marine_standard"
    INDUSTRIAL = "industrial"
    AUTOMOTIVE = "automotive"
    UNKNOWN = "unknown"


class InsulationMaterial(str, Enum):
    """Isolationsmaterial."""
    PVC = "pvc"
    PVC_NYLON = "pvc_nylon"
    XLPE = "xlpe"
    EPR = "epr"
    SILICONE = "silicone"
    PTFE = "ptfe"
    TPE = "tpe"
    PUR = "pur"
    FRNC = "frnc"
    UNKNOWN = "unknown"


class ConductorType(str, Enum):
    """Leitertyp."""
    TINNED_COPPER = "tinned_copper"
    BARE_COPPER = "bare_copper"
    COPPER_CLAD_ALUMINIUM = "copper_clad_aluminium"
    UNKNOWN = "unknown"


class ConductorClass(str, Enum):
    """Leiterklasse nach IEC 60228."""
    CLASS_1_SOLID = "class_1"
    CLASS_2_STRANDED = "class_2"
    CLASS_5_FLEXIBLE = "class_5"
    CLASS_6_EXTRA_FLEXIBLE = "class_6"
    UNKNOWN = "unknown"


class WireColorCode(str, Enum):
    """Farbcodes."""
    RED = "red"
    BLACK = "black"
    YELLOW = "yellow"
    BLUE = "blue"
    BROWN = "brown"
    GREEN = "green"
    GREEN_YELLOW = "green_yellow"
    WHITE = "white"
    GREY = "grey"
    ORANGE = "orange"
    VIOLET = "violet"
    PINK = "pink"
    TAN = "tan"
    OTHER = "other"


class CableCategory(str, Enum):
    """Kabelkategorie."""
    SINGLE_CORE = "single_core"
    MULTI_CORE = "multi_core"
    BATTERY = "battery"
    COAXIAL = "coaxial"
    DATA_NMEA2000 = "data_nmea2000"
    DATA_NMEA0183 = "data_nmea0183"
    DATA_ETHERNET = "data_ethernet"
    SOLAR_PV = "solar_pv"
    UNDERWATER = "underwater"
    MAST = "mast"
    CONTROL = "control"
    HEATING = "heating"
    UNKNOWN = "unknown"


class FaultSeverity(str, Enum):
    """Fehlerschwere."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"


class RepairUrgency(str, Enum):
    """Reparaturdringlichkeit."""
    IMMEDIATE = "immediate"
    BEFORE_NEXT_TRIP = "before_next_trip"
    WITHIN_2_WEEKS = "within_2_weeks"
    WITHIN_4_WEEKS = "within_4_weeks"
    SEASONAL = "seasonal"
    NEXT_REFIT = "next_refit"


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


class VoltageSystem(str, Enum):
    """Spannungssystem."""
    DC_12V = "dc_12v"
    DC_24V = "dc_24v"
    DC_48V = "dc_48v"
    AC_230V = "ac_230v"
    AC_400V = "ac_400v"
    AC_120V = "ac_120v"


class BoatZone(str, Enum):
    """Bootszone für Kabelverlegung."""
    MAST_TOP = "mast_top"
    MAST_FOOT = "mast_foot"
    ENGINE_ROOM = "engine_room"
    BILGE = "bilge"
    RUDDER_AREA = "rudder_area"
    ANCHOR_LOCKER = "anchor_locker"
    DECK_PENETRATION = "deck_penetration"
    COCKPIT = "cockpit"
    LOCKER = "locker"
    SALON = "salon"
    CABIN = "cabin"
    HEAD = "head"
    GALLEY = "galley"
    FOREPEAK = "forepeak"
    LAZARETTE = "lazarette"
    UNDERWATER = "underwater"
    BIMINI_ARCH = "bimini_arch"


# ── Basismodelle ─────────────────────────────────────────────────

class CableSpec(BaseModel):
    """Spezifikation eines Kabels."""
    model_config = {"from_attributes": True}

    category: CableCategory
    designation: str = Field(..., description="Handelsbezeichnung (z.B. 'Ancor Marine Grade Primary Wire')")
    manufacturer: Optional[str] = None
    cross_section_mm2: float = Field(..., gt=0, description="Leiterquerschnitt in mm²")
    awg_equivalent: Optional[str] = Field(None, description="AWG Äquivalent (z.B. '10', '4/0')")
    num_cores: int = Field(1, ge=1, description="Aderzahl")
    conductor_type: ConductorType = ConductorType.UNKNOWN
    conductor_class: ConductorClass = ConductorClass.UNKNOWN
    insulation: InsulationMaterial = InsulationMaterial.UNKNOWN
    outer_sheath: Optional[InsulationMaterial] = None
    temperature_min_c: float = Field(-20, description="Min. Betriebstemperatur in °C")
    temperature_max_c: float = Field(70, description="Max. Betriebstemperatur in °C")
    voltage_rating_v: int = Field(600, description="Nennspannung in V")
    shielded: bool = False
    uv_resistant: bool = False
    oil_resistant: bool = False
    halogen_free: bool = False
    flame_retardant: bool = False
    outer_diameter_mm: Optional[float] = Field(None, gt=0)
    color: Optional[WireColorCode] = None
    certifications: list[str] = Field(default_factory=list, description="z.B. ['UL 1426', 'VDE', 'GL']")
    marine_grade: CableGrade = CableGrade.UNKNOWN
    price_per_meter_eur: Optional[float] = Field(None, ge=0)


class CableAmpacity(BaseModel):
    """Strombelastbarkeit eines Kabelquerschnitts."""
    model_config = {"from_attributes": True}

    cross_section_mm2: float = Field(..., gt=0)
    insulation: InsulationMaterial
    ambient_temp_c: float = Field(30, description="Umgebungstemperatur")
    continuous_amps: float = Field(..., gt=0, description="Dauerstrom in A")
    short_term_30min_amps: Optional[float] = Field(None, gt=0)
    bundle_count: int = Field(1, ge=1, description="Anzahl Kabel im Bündel")
    derating_factor: float = Field(1.0, ge=0, le=1.0)
    effective_amps: Optional[float] = Field(None, description="Effektive Belastbarkeit nach Derating")
```

---

## ANHANG J — AYDI-Integration: Querschnittsberechnung

```python
"""
AYDI Wissensmodul 22.03 — Kabelquerschnittsberechnung
"""

from __future__ import annotations

import math
from typing import Optional

from pydantic import BaseModel, Field, field_validator

from .cable_base_models import (
    BoatZone,
    CableGrade,
    ConfidenceLevel,
    InsulationMaterial,
    VoltageSystem,
)


# ── Konstanten ───────────────────────────────────────────────────

COPPER_RESISTIVITY_OHM_MM2_PER_M = 0.0175  # bei 20°C

STANDARD_CROSS_SECTIONS_MM2 = [
    0.5, 0.75, 1.0, 1.5, 2.5, 4, 6, 10, 16, 25, 35, 50, 70, 95, 120, 150, 185, 240,
]

# Bündelungsfaktoren nach ABYC E-11 / VDE
BUNDLE_DERATING = {
    (1, 3): 1.00,
    (4, 6): 0.80,
    (7, 9): 0.70,
    (10, 12): 0.65,
    (13, 16): 0.60,
    (17, 20): 0.57,
    (21, 999): 0.50,
}

# Temperatur-Korrekturfaktoren (PVC 70°C Leiter)
TEMP_DERATING_PVC = {
    25: 1.06, 30: 1.00, 35: 0.94, 40: 0.87, 45: 0.79,
    50: 0.71, 55: 0.61, 60: 0.50,
}

TEMP_DERATING_XLPE = {
    25: 1.04, 30: 1.00, 35: 0.96, 40: 0.91, 45: 0.87,
    50: 0.82, 55: 0.76, 60: 0.71, 65: 0.65, 70: 0.58, 80: 0.41,
}

TEMP_DERATING_SILICONE = {
    25: 1.01, 30: 1.00, 35: 0.99, 40: 0.98, 45: 0.97,
    50: 0.96, 55: 0.95, 60: 0.94, 65: 0.93, 70: 0.92, 80: 0.90,
}

# Maximal zulässiger Spannungsabfall (%)
MAX_VOLTAGE_DROP_CRITICAL = 3.0
MAX_VOLTAGE_DROP_NON_CRITICAL = 10.0


class CrossSectionInput(BaseModel):
    """Eingabe für die Querschnittsberechnung."""
    model_config = {"from_attributes": True}

    voltage_system: VoltageSystem
    current_amps: float = Field(..., gt=0, description="Maximaler Dauerstrom in A")
    cable_length_m: float = Field(..., gt=0, description="Einfache Kabellänge in Metern (Hinweg)")
    is_critical: bool = Field(True, description="Kritischer Verbraucher (Navigation, Bilgenpumpe)?")
    max_voltage_drop_pct: Optional[float] = Field(
        None, description="Benutzerdefinierter max. Spannungsabfall in %"
    )
    ambient_temp_c: float = Field(30, description="Umgebungstemperatur in °C")
    bundle_count: int = Field(1, ge=1, description="Anzahl Kabel im Bündel")
    insulation: InsulationMaterial = InsulationMaterial.PVC
    zone: Optional[BoatZone] = None
    return_via_hull: bool = Field(
        False,
        description="Rückleitung über Stahlrumpf (kein Faktor 2)? NUR bei Stahl-/Alu-Booten!",
    )

    @field_validator("max_voltage_drop_pct")
    @classmethod
    def validate_voltage_drop(cls, v: Optional[float]) -> Optional[float]:
        if v is not None and (v <= 0 or v > 25):
            msg = "Spannungsabfall muss zwischen 0 und 25% liegen"
            raise ValueError(msg)
        return v


class CrossSectionResult(BaseModel):
    """Ergebnis der Querschnittsberechnung."""
    model_config = {"from_attributes": True}

    # Eingabedaten (Echo)
    voltage_system: VoltageSystem
    current_amps: float
    cable_length_m: float
    is_critical: bool

    # Berechnungsergebnisse
    voltage_drop_required_mm2: float = Field(
        ..., description="Mindestquerschnitt nach Spannungsabfall"
    )
    ampacity_required_mm2: float = Field(
        ..., description="Mindestquerschnitt nach Strombelastbarkeit"
    )
    recommended_mm2: float = Field(
        ..., description="Empfohlener Querschnitt (nächster Standard nach oben)"
    )
    next_larger_mm2: Optional[float] = Field(
        None, description="Eine Stufe größer (Sicherheitsempfehlung)"
    )

    # Nachprüfung
    actual_voltage_drop_v: float
    actual_voltage_drop_pct: float
    max_allowed_drop_pct: float

    # Metadaten
    confidence: ConfidenceLevel = ConfidenceLevel.CALCULATED
    warnings: list[str] = Field(default_factory=list)
    notes: list[str] = Field(default_factory=list)


def _get_system_voltage(system: VoltageSystem) -> float:
    """Nennspannung aus dem System-Enum."""
    voltage_map = {
        VoltageSystem.DC_12V: 12.0,
        VoltageSystem.DC_24V: 24.0,
        VoltageSystem.DC_48V: 48.0,
        VoltageSystem.AC_230V: 230.0,
        VoltageSystem.AC_400V: 400.0,
        VoltageSystem.AC_120V: 120.0,
    }
    return voltage_map[system]


def _next_standard_cross_section(required_mm2: float) -> float:
    """Nächsten Standard-Querschnitt nach oben finden."""
    for cs in STANDARD_CROSS_SECTIONS_MM2:
        if cs >= required_mm2:
            return cs
    return STANDARD_CROSS_SECTIONS_MM2[-1]


def _get_next_larger(mm2: float) -> Optional[float]:
    """Eine Stufe größer als der gegebene Querschnitt."""
    for i, cs in enumerate(STANDARD_CROSS_SECTIONS_MM2):
        if cs == mm2 and i + 1 < len(STANDARD_CROSS_SECTIONS_MM2):
            return STANDARD_CROSS_SECTIONS_MM2[i + 1]
    return None


def _get_bundle_factor(count: int) -> float:
    """Bündelungsfaktor ermitteln."""
    for (low, high), factor in BUNDLE_DERATING.items():
        if low <= count <= high:
            return factor
    return 0.50


def _get_temp_factor(temp_c: float, insulation: InsulationMaterial) -> float:
    """Temperatur-Korrekturfaktor ermitteln."""
    if insulation in (InsulationMaterial.SILICONE,):
        table = TEMP_DERATING_SILICONE
    elif insulation in (InsulationMaterial.XLPE, InsulationMaterial.EPR):
        table = TEMP_DERATING_XLPE
    else:
        table = TEMP_DERATING_PVC

    # Nächstliegenden Wert in der Tabelle finden
    temps = sorted(table.keys())
    if temp_c <= temps[0]:
        return table[temps[0]]
    if temp_c >= temps[-1]:
        return table[temps[-1]]

    # Linear interpolieren
    for i in range(len(temps) - 1):
        if temps[i] <= temp_c <= temps[i + 1]:
            t1, t2 = temps[i], temps[i + 1]
            f1, f2 = table[t1], table[t2]
            return f1 + (f2 - f1) * (temp_c - t1) / (t2 - t1)
    return 1.0


def calculate_cable_cross_section(inp: CrossSectionInput) -> CrossSectionResult:
    """
    Berechnet den erforderlichen Kabelquerschnitt nach ABYC E-11 / ISO 13297.

    Berücksichtigt:
    - Spannungsabfall
    - Strombelastbarkeit mit Bündelungs- und Temperaturfaktor
    """
    warnings: list[str] = []
    notes: list[str] = []

    u_nenn = _get_system_voltage(inp.voltage_system)

    # Max. Spannungsabfall bestimmen
    if inp.max_voltage_drop_pct is not None:
        max_drop_pct = inp.max_voltage_drop_pct
    elif inp.is_critical:
        max_drop_pct = MAX_VOLTAGE_DROP_CRITICAL
    else:
        max_drop_pct = MAX_VOLTAGE_DROP_NON_CRITICAL

    # Faktor: Hin- und Rückleiter
    length_factor = 1.0 if inp.return_via_hull else 2.0

    if inp.return_via_hull:
        notes.append(
            "Rückleitung über Rumpf (Faktor 1). "
            "NUR zulässig bei Stahl-/Alu-Booten mit fachgerechtem Masseband."
        )

    # 1. Querschnitt nach Spannungsabfall
    a_vdrop = (
        length_factor * inp.cable_length_m * inp.current_amps * COPPER_RESISTIVITY_OHM_MM2_PER_M
    ) / (u_nenn * max_drop_pct / 100)

    # 2. Querschnitt nach Strombelastbarkeit (vereinfacht, Tabellenwerte)
    # Vereinfachte Faustformel: A = I / Stromdichte (5-8 A/mm² für Marine)
    stromdichte = 6.0  # A/mm² konservativ
    bundle_factor = _get_bundle_factor(inp.bundle_count)
    temp_factor = _get_temp_factor(inp.ambient_temp_c, inp.insulation)
    effective_stromdichte = stromdichte * bundle_factor * temp_factor
    a_ampacity = inp.current_amps / effective_stromdichte

    if bundle_factor < 1.0:
        notes.append(
            f"Bündelungsfaktor {bundle_factor:.2f} angewandt ({inp.bundle_count} Kabel im Bündel)."
        )
    if temp_factor < 1.0:
        notes.append(
            f"Temperaturfaktor {temp_factor:.2f} angewandt ({inp.ambient_temp_c}°C Umgebung)."
        )

    # Maßgebender Querschnitt
    required_mm2 = max(a_vdrop, a_ampacity)
    recommended = _next_standard_cross_section(required_mm2)
    next_larger = _get_next_larger(recommended)

    # Gegenprobe Spannungsabfall
    actual_vdrop_v = (
        length_factor * inp.cable_length_m * inp.current_amps * COPPER_RESISTIVITY_OHM_MM2_PER_M
    ) / recommended
    actual_vdrop_pct = (actual_vdrop_v / u_nenn) * 100

    # Warnungen
    if a_vdrop > a_ampacity:
        notes.append(
            "Spannungsabfall ist das bestimmende Kriterium (typisch für 12V-Systeme)."
        )
    else:
        notes.append("Strombelastbarkeit ist das bestimmende Kriterium.")

    if inp.zone == BoatZone.ENGINE_ROOM and inp.insulation == InsulationMaterial.PVC:
        warnings.append(
            "PVC-Isolierung im Motorraum: Max. 70°C Leitertemperatur. "
            "Silikon- oder XLPE-Kabel empfohlen."
        )

    if inp.zone == BoatZone.MAST_TOP or inp.zone == BoatZone.MAST_FOOT:
        warnings.append(
            "Mastverkabelung: Hochflexibles Kabel (Klasse 6) mit UV-Schutz empfohlen."
        )

    if recommended >= 95:
        notes.append(
            f"Großer Querschnitt ({recommended} mm²). "
            "Parallelverlegung von 2 Kabeln als Alternative prüfen."
        )

    return CrossSectionResult(
        voltage_system=inp.voltage_system,
        current_amps=inp.current_amps,
        cable_length_m=inp.cable_length_m,
        is_critical=inp.is_critical,
        voltage_drop_required_mm2=round(a_vdrop, 2),
        ampacity_required_mm2=round(a_ampacity, 2),
        recommended_mm2=recommended,
        next_larger_mm2=next_larger,
        actual_voltage_drop_v=round(actual_vdrop_v, 3),
        actual_voltage_drop_pct=round(actual_vdrop_pct, 2),
        max_allowed_drop_pct=max_drop_pct,
        confidence=ConfidenceLevel.CALCULATED,
        warnings=warnings,
        notes=notes,
    )
```

---

## ANHANG K — AYDI-Integration: Fehlerbild-Modelle

```python
"""
AYDI Wissensmodul 22.03 — Fehlerbild-Modelle für Kabel und Leitungen
"""

from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

from .cable_base_models import (
    BoatZone,
    CableGrade,
    ConfidenceLevel,
    FaultSeverity,
    RepairUrgency,
)


class CableFaultPattern(BaseModel):
    """Fehlerbild für Kabel und Leitungen."""
    model_config = {"from_attributes": True}

    fault_id: str = Field(..., description="Eindeutige ID (z.B. 'CABLE_FAULT_001')")
    fault_name_de: str = Field(..., description="Deutscher Fehlername")
    fault_name_en: str = Field(..., description="Englischer Fehlername")
    description_de: str = Field(..., description="Beschreibung des Fehlerbildes")
    typical_zones: list[BoatZone] = Field(
        default_factory=list, description="Typische Zonen, in denen dieser Fehler auftritt"
    )
    causes: list[str] = Field(default_factory=list, description="Mögliche Ursachen")
    symptoms: list[str] = Field(default_factory=list, description="Erkennbare Symptome")
    diagnosis_steps: list[str] = Field(
        default_factory=list, description="Diagnoseschritte"
    )
    repair_steps: list[str] = Field(default_factory=list, description="Reparaturschritte")
    severity: FaultSeverity
    repair_urgency: RepairUrgency
    visual_detectability: ConfidenceLevel = Field(
        ..., description="Wie gut kann dieser Fehler visuell (Foto) erkannt werden?"
    )
    estimated_repair_cost_eur_min: Optional[float] = None
    estimated_repair_cost_eur_max: Optional[float] = None
    estimated_repair_hours_min: Optional[float] = None
    estimated_repair_hours_max: Optional[float] = None
    prevention_measures: list[str] = Field(default_factory=list)
    related_faults: list[str] = Field(
        default_factory=list, description="IDs verwandter Fehlerbilder"
    )


class CableFaultFinding(BaseModel):
    """Konkreter Befund bei einer Inspektion."""
    model_config = {"from_attributes": True}

    finding_id: str
    fault_pattern_id: str = Field(..., description="Referenz auf CableFaultPattern.fault_id")
    zone: BoatZone
    location_description_de: str = Field(
        ..., description="Genauer Fundort (z.B. 'Hauptschalttafel, Klemme 14')"
    )
    severity_override: Optional[FaultSeverity] = Field(
        None, description="Abweichende Severity für diesen spezifischen Befund"
    )
    confidence: ConfidenceLevel
    evidence_type: str = Field(
        ..., description="Art des Nachweises (z.B. 'photo', 'measurement', 'visual')"
    )
    measurement_value: Optional[str] = Field(
        None, description="Messwert (z.B. '2,3 Ω Übergangswiderstand')"
    )
    photo_reference: Optional[str] = Field(None, description="Referenz zum Foto")
    recommendation_de: str = Field(..., description="Handlungsempfehlung auf Deutsch")
    estimated_cost_eur: Optional[float] = None
    inspection_date: Optional[date] = None
    inspector: Optional[str] = None


class CableFaultAtlas(BaseModel):
    """Vollständiger Fehlerbild-Atlas."""
    model_config = {"from_attributes": True}

    version: str = Field(default="1.0.0")
    last_updated: date
    fault_patterns: list[CableFaultPattern] = Field(default_factory=list)
    total_patterns: int = Field(0)

    def get_faults_by_zone(self, zone: BoatZone) -> list[CableFaultPattern]:
        """Alle Fehlerbilder für eine bestimmte Zone zurückgeben."""
        return [fp for fp in self.fault_patterns if zone in fp.typical_zones]

    def get_critical_faults(self) -> list[CableFaultPattern]:
        """Alle Fehlerbilder mit Severity CRITICAL zurückgeben."""
        return [
            fp for fp in self.fault_patterns if fp.severity == FaultSeverity.CRITICAL
        ]
```

---

## ANHANG L — AYDI-Integration: Kabel-Inspektion und Bewertung

```python
"""
AYDI Wissensmodul 22.03 — Kabel-Inspektions- und Bewertungsmodelle
"""

from __future__ import annotations

from datetime import date
from typing import Optional

from pydantic import BaseModel, Field

from .cable_base_models import (
    BoatZone,
    CableCategory,
    CableGrade,
    ConductorClass,
    ConductorType,
    ConfidenceLevel,
    InsulationMaterial,
    VoltageSystem,
)


class CableRun(BaseModel):
    """Ein einzelner Kabelstrang (Kabelweg) auf dem Boot."""
    model_config = {"from_attributes": True}

    run_id: str = Field(..., description="Eindeutige ID des Kabelstrangs")
    circuit_name: str = Field(..., description="Stromkreis-Bezeichnung")
    voltage_system: VoltageSystem
    cable_category: CableCategory
    cross_section_mm2: float = Field(..., gt=0)
    length_m: float = Field(..., gt=0, description="Einfache Kabellänge in m")
    conductor_type: ConductorType
    conductor_class: ConductorClass
    insulation: InsulationMaterial
    marine_grade: CableGrade
    zones_traversed: list[BoatZone] = Field(
        default_factory=list, description="Alle Zonen, die das Kabel durchläuft"
    )
    max_current_a: float = Field(..., gt=0, description="Maximaler Dauerstrom")
    fuse_rating_a: Optional[float] = Field(None, gt=0, description="Sicherungswert in A")
    year_installed: Optional[int] = None
    manufacturer: Optional[str] = None
    condition_score: Optional[int] = Field(
        None, ge=0, le=100, description="Zustandsbewertung 0–100"
    )
    notes: list[str] = Field(default_factory=list)


class CableInspectionResult(BaseModel):
    """Ergebnis einer Kabelinspektion für einen Strang."""
    model_config = {"from_attributes": True}

    run: CableRun
    voltage_drop_calculated_pct: float
    voltage_drop_within_limits: bool
    fuse_correctly_sized: Optional[bool] = Field(
        None, description="None wenn Sicherungswert unbekannt"
    )
    conductor_tinned: bool
    insulation_condition: str = Field(
        ..., description="gut / akzeptabel / auffällig / mangelhaft"
    )
    connections_condition: str = Field(
        ..., description="gut / akzeptabel / auffällig / mangelhaft"
    )
    findings: list[str] = Field(
        default_factory=list, description="Liste der Befunde"
    )
    overall_score: int = Field(..., ge=0, le=100)
    confidence: ConfidenceLevel
    recommendations: list[str] = Field(default_factory=list)


class ElectricalSystemAssessment(BaseModel):
    """Gesamtbewertung des elektrischen Systems (Kabelbereich)."""
    model_config = {"from_attributes": True}

    boat_name: Optional[str] = None
    boat_type: Optional[str] = None
    boat_year: Optional[int] = None
    inspection_date: date
    inspector: Optional[str] = None

    total_cable_runs_inspected: int = Field(0, ge=0)
    cable_runs: list[CableInspectionResult] = Field(default_factory=list)

    # Bewertungsfelder
    overall_score: int = Field(..., ge=0, le=100)
    marine_grade_percentage: float = Field(
        ..., ge=0, le=100, description="Anteil Marine-Grade-Kabel in %"
    )
    tinned_copper_percentage: float = Field(
        ..., ge=0, le=100, description="Anteil verzinntes Kupfer in %"
    )
    correctly_fused_percentage: Optional[float] = Field(
        None, ge=0, le=100, description="Anteil korrekt abgesichert in %"
    )
    voltage_drop_compliant_percentage: float = Field(
        ..., ge=0, le=100, description="Anteil Spannungsabfall-konform in %"
    )

    critical_findings: list[str] = Field(default_factory=list)
    high_findings: list[str] = Field(default_factory=list)
    medium_findings: list[str] = Field(default_factory=list)

    estimated_rewiring_cost_eur: Optional[float] = None
    estimated_rewiring_hours: Optional[float] = None

    confidence: ConfidenceLevel
    recommendations_prioritized: list[str] = Field(default_factory=list)
```

---

## ANHANG M — AYDI-Integration: Hersteller-Datenbank-Modell

```python
"""
AYDI Wissensmodul 22.03 — Hersteller-Datenbank für Kabel und Leitungen
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, HttpUrl


class CableManufacturer(BaseModel):
    """Hersteller von Marine-Kabeln."""
    model_config = {"from_attributes": True}

    manufacturer_id: str
    name: str
    full_legal_name: Optional[str] = None
    country: str
    city: Optional[str] = None
    founded_year: Optional[int] = None
    parent_company: Optional[str] = None
    marine_focus_pct: Optional[float] = Field(
        None, ge=0, le=100, description="Anteil Marine am Gesamtumsatz in %"
    )
    website: Optional[str] = None
    product_lines: list[str] = Field(default_factory=list)
    certifications: list[str] = Field(default_factory=list)
    distribution_eu: list[str] = Field(
        default_factory=list, description="Vertriebskanäle in Europa"
    )
    price_level: str = Field(
        "mittel", description="niedrig / mittel / mittel-premium / premium / premium-hoch"
    )
    strengths: list[str] = Field(default_factory=list)
    weaknesses: list[str] = Field(default_factory=list)
    recommended_for: list[str] = Field(
        default_factory=list,
        description="Empfohlen für (z.B. 'Produktionssegelboot', 'Superyacht')",
    )
    notes: list[str] = Field(default_factory=list)


class CableProduct(BaseModel):
    """Einzelnes Kabelprodukt in der Datenbank."""
    model_config = {"from_attributes": True}

    product_id: str
    manufacturer_id: str
    product_name: str
    product_line: Optional[str] = None
    description_de: str
    cable_category: str
    cross_sections_available: list[float] = Field(
        default_factory=list, description="Verfügbare Querschnitte in mm²"
    )
    num_cores_options: list[int] = Field(default_factory=list)
    colors_available: list[str] = Field(default_factory=list)
    conductor_type: str
    insulation_material: str
    outer_sheath_material: Optional[str] = None
    temperature_range: str = Field(
        ..., description="z.B. '-40°C bis +90°C'"
    )
    voltage_rating: str = Field(..., description="z.B. '0,6/1 kV'")
    shielded: bool = False
    uv_resistant: bool = False
    oil_resistant: bool = False
    halogen_free: bool = False
    flame_retardant: bool = False
    marine_certifications: list[str] = Field(default_factory=list)
    price_range_eur_per_m: Optional[str] = Field(
        None, description="z.B. '2,50–4,00'"
    )
    typical_applications: list[str] = Field(default_factory=list)
    order_information: Optional[str] = None


class CableManufacturerDatabase(BaseModel):
    """Hersteller-Datenbank."""
    model_config = {"from_attributes": True}

    version: str = Field(default="1.0.0")
    manufacturers: list[CableManufacturer] = Field(default_factory=list)
    products: list[CableProduct] = Field(default_factory=list)

    def get_manufacturer(self, manufacturer_id: str) -> Optional[CableManufacturer]:
        """Hersteller nach ID suchen."""
        for m in self.manufacturers:
            if m.manufacturer_id == manufacturer_id:
                return m
        return None

    def get_products_by_manufacturer(self, manufacturer_id: str) -> list[CableProduct]:
        """Alle Produkte eines Herstellers."""
        return [p for p in self.products if p.manufacturer_id == manufacturer_id]

    def search_products(
        self,
        *,
        category: Optional[str] = None,
        min_cross_section: Optional[float] = None,
        halogen_free: Optional[bool] = None,
        marine_cert_required: bool = False,
    ) -> list[CableProduct]:
        """Produkte nach Kriterien suchen."""
        results = self.products
        if category:
            results = [p for p in results if p.cable_category == category]
        if min_cross_section is not None:
            results = [
                p for p in results
                if any(cs >= min_cross_section for cs in p.cross_sections_available)
            ]
        if halogen_free is not None:
            results = [p for p in results if p.halogen_free == halogen_free]
        if marine_cert_required:
            results = [p for p in results if len(p.marine_certifications) > 0]
        return results
```

---

## ANHANG N — AYDI-Integration: Koaxialkabel-Modelle

```python
"""
AYDI Wissensmodul 22.03 — Koaxialkabel-spezifische Modelle
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class CoaxialCableSpec(BaseModel):
    """Spezifikation eines Koaxialkabels."""
    model_config = {"from_attributes": True}

    cable_type: str = Field(..., description="z.B. 'RG-58/U', 'RG-213/U', 'Aircell 7'")
    impedance_ohm: int = Field(..., description="Wellenwiderstand in Ω (50 oder 75)")
    inner_conductor_mm: float = Field(..., gt=0)
    inner_conductor_material: str = Field(default="Cu verzinnt")
    dielectric: str = Field(default="PE")
    shield_type: str = Field(..., description="z.B. 'Kupfergeflecht 95%'")
    outer_diameter_mm: float = Field(..., gt=0)
    attenuation_30mhz_db_per_100m: Optional[float] = None
    attenuation_156mhz_db_per_100m: Optional[float] = None
    attenuation_450mhz_db_per_100m: Optional[float] = None
    attenuation_1ghz_db_per_100m: Optional[float] = None
    max_recommended_length_vhf_m: Optional[float] = Field(
        None, description="Max. empfohlene Kabellänge für UKW-Funk"
    )
    suitable_for: list[str] = Field(
        default_factory=list,
        description="z.B. ['VHF', 'AIS', 'GPS', 'SSB', 'TV', 'SAT']",
    )
    connector_type: str = Field(default="PL-259 / SO-239")
    min_bend_radius_mm: Optional[float] = None
    price_per_meter_eur: Optional[float] = None


class CoaxialLossCalculation(BaseModel):
    """Berechnung der Koaxialkabeldämpfung."""
    model_config = {"from_attributes": True}

    cable_type: str
    frequency_mhz: float = Field(..., gt=0)
    cable_length_m: float = Field(..., gt=0)
    attenuation_per_100m_db: float = Field(..., description="Dämpfung bei gegebener Frequenz")
    total_attenuation_db: float = Field(..., description="Gesamtdämpfung")
    power_loss_pct: float = Field(
        ..., ge=0, le=100, description="Leistungsverlust in %"
    )
    connector_loss_db: float = Field(
        0.5, description="Geschätzte Steckerdämpfung pro Verbindung"
    )
    num_connectors: int = Field(2, ge=2)
    total_loss_db: float
    acceptable: bool = Field(
        ..., description="Ist die Gesamtdämpfung für den Einsatzzweck akzeptabel?"
    )
    recommendation: Optional[str] = None


def calculate_coax_loss(
    cable_type: str,
    attenuation_per_100m_db: float,
    cable_length_m: float,
    frequency_mhz: float,
    num_connectors: int = 2,
    connector_loss_db: float = 0.5,
    max_acceptable_loss_db: float = 10.0,
) -> CoaxialLossCalculation:
    """
    Berechnet die Gesamtdämpfung eines Koaxialkabels.
    """
    cable_loss = attenuation_per_100m_db * cable_length_m / 100
    total_connector_loss = num_connectors * connector_loss_db
    total_loss = cable_loss + total_connector_loss
    power_loss_pct = (1 - 10 ** (-total_loss / 10)) * 100

    acceptable = total_loss <= max_acceptable_loss_db

    recommendation = None
    if not acceptable:
        recommendation = (
            f"Gesamtdämpfung {total_loss:.1f} dB überschreitet Grenzwert "
            f"{max_acceptable_loss_db:.1f} dB. Kürzeres Kabel oder dämpfungsärmeren "
            f"Typ (z.B. RG-213 oder LMR-400) verwenden."
        )

    return CoaxialLossCalculation(
        cable_type=cable_type,
        frequency_mhz=frequency_mhz,
        cable_length_m=cable_length_m,
        attenuation_per_100m_db=attenuation_per_100m_db,
        total_attenuation_db=round(cable_loss, 2),
        power_loss_pct=round(power_loss_pct, 1),
        connector_loss_db=connector_loss_db,
        num_connectors=num_connectors,
        total_loss_db=round(total_loss, 2),
        acceptable=acceptable,
        recommendation=recommendation,
    )
```

---

## ANHANG O — AYDI-Integration: Kabelverlegungs-Bewertung

```python
"""
AYDI Wissensmodul 22.03 — Bewertungsmodell für Kabelverlegung
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .cable_base_models import BoatZone, ConfidenceLevel


class CableRoutingAssessment(BaseModel):
    """Bewertung der Kabelverlegung in einer Zone."""
    model_config = {"from_attributes": True}

    zone: BoatZone
    zone_name_de: str

    # Einzelbewertungen (0-100)
    cable_fixation_score: int = Field(
        ..., ge=0, le=100,
        description="Befestigung: Kabelschellen, Kabelbinder, Abstände",
    )
    bend_radius_score: int = Field(
        ..., ge=0, le=100,
        description="Biegeradien eingehalten?",
    )
    separation_score: int = Field(
        ..., ge=0, le=100,
        description="Trennung Strom-/Datenkabel",
    )
    protection_score: int = Field(
        ..., ge=0, le=100,
        description="Mechanischer Schutz (Tüllen, Wellrohr, Kantenschutz)",
    )
    drip_loop_score: int = Field(
        ..., ge=0, le=100,
        description="Tropfschleifen an Durchführungen",
    )
    labeling_score: int = Field(
        ..., ge=0, le=100,
        description="Beschriftung / Identifizierung der Kabel",
    )
    accessibility_score: int = Field(
        ..., ge=0, le=100,
        description="Zugänglichkeit für Wartung und Inspektion",
    )
    overall_routing_score: int = Field(
        ..., ge=0, le=100,
        description="Gesamtbewertung Verlegung",
    )

    findings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    confidence: ConfidenceLevel


class CableConnectionAssessment(BaseModel):
    """Bewertung der Kabelverbindungen in einer Zone."""
    model_config = {"from_attributes": True}

    zone: BoatZone
    total_connections_inspected: int = Field(0, ge=0)

    # Statistiken
    crimped_pct: float = Field(0, ge=0, le=100, description="Anteil gecrimpte Verbindungen")
    soldered_pct: float = Field(0, ge=0, le=100, description="Anteil gelötete Verbindungen")
    screw_terminal_pct: float = Field(0, ge=0, le=100, description="Anteil Schraubklemmen")
    wago_pct: float = Field(0, ge=0, le=100, description="Anteil Federklemmen (WAGO)")
    other_pct: float = Field(0, ge=0, le=100, description="Anteil sonstige")

    heat_shrink_with_glue_pct: float = Field(
        0, ge=0, le=100, description="Anteil mit Klebe-Schrumpfschlauch gesichert"
    )
    corrosion_found_pct: float = Field(
        0, ge=0, le=100, description="Anteil mit sichtbarer Korrosion"
    )
    loose_connections_found: int = Field(0, ge=0)

    overall_connection_score: int = Field(..., ge=0, le=100)
    confidence: ConfidenceLevel
    findings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
```

---

## ANHANG P — AYDI-Integration: Visuelle Analyse von Kabeln

```python
"""
AYDI Wissensmodul 22.03 — Visuelle Analyse-Prompts für Kabel und Leitungen
Für Claude Vision API Integration.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from .cable_base_models import BoatZone, ConfidenceLevel


CABLE_VISUAL_ANALYSIS_PROMPT_DE = """
Du bist ein erfahrener Marine-Elektriker und analysierst ein Foto
der Kabelinstallation auf einer Yacht.

Bewerte folgende Aspekte (Score 0-100, Confidence-Level angeben):

1. KABELQUALITÄT
   - Sind die Kabel marine-tauglich (verzinntes Kupfer)?
   - Sichtbare Korrosion an Kabelenden?
   - Isolierungszustand (spröde, rissig, verfärbt)?
   - Kabeltyp angemessen für die Zone?

2. VERLEGUNG
   - Kabel sauber geführt oder chaotisch?
   - Biegeradien eingehalten?
   - Kabel fixiert (Schellen, Kabelbinder)?
   - Tropfschleifen an Durchführungen?
   - Trennung von Strom- und Datenkabeln?

3. VERBINDUNGEN
   - Verbindungstyp erkennbar (Crimp, Löt, Schraubklemme)?
   - Schrumpfschlauch vorhanden?
   - Korrosion/Grünspan an Verbindungen?
   - Kabelschuhe passend zum Querschnitt?

4. SICHERHEIT
   - Offene/blanke Leiter sichtbar?
   - Scheuerstellen erkennbar?
   - Überhitzungsspuren (verfärbte Isolierung)?
   - Feuchtigkeit/Wasser in der Nähe von Verbindungen?

5. ABSICHERUNG (falls Sicherungskasten/Verteiler sichtbar)
   - Sicherungen beschriftet?
   - Sicherungstyp erkennbar (Blade, ANL, Glasrohr)?
   - Korrosion an Sicherungshaltern?

Antworte auf Deutsch. Verwende das AYDI-Confidence-System:
- visual_high: Eindeutig erkennbar
- visual_medium: Erkennbar, aber Unsicherheit
- visual_low: Schwer zu beurteilen
- visual_insufficient: Nicht beurteilbar

Sage "nicht beurteilbar" wenn du dir nicht sicher bist.
Jeden Befund mit Schweregrad (KRITISCH/HOCH/MITTEL/GERING) versehen.
"""


class CableVisualAnalysisRequest(BaseModel):
    """Anfrage für visuelle Kabelanalyse."""
    model_config = {"from_attributes": True}

    image_path: str = Field(..., description="Pfad zum Bild")
    zone: Optional[BoatZone] = Field(
        None, description="Zone, falls bekannt (verbessert Kontext)"
    )
    boat_type: Optional[str] = None
    boat_year: Optional[int] = None
    additional_context: Optional[str] = None


class CableVisualFinding(BaseModel):
    """Einzelbefund aus visueller Analyse."""
    model_config = {"from_attributes": True}

    finding_de: str = Field(..., description="Befund auf Deutsch")
    severity: str = Field(..., description="KRITISCH / HOCH / MITTEL / GERING")
    confidence: ConfidenceLevel
    location_in_image: Optional[str] = Field(
        None, description="Beschreibung der Position im Bild"
    )
    recommendation_de: Optional[str] = None


class CableVisualAnalysisResult(BaseModel):
    """Ergebnis der visuellen Kabelanalyse."""
    model_config = {"from_attributes": True}

    zone: Optional[BoatZone] = None
    overall_score: int = Field(..., ge=0, le=100)
    quality_score: int = Field(..., ge=0, le=100, description="Kabelqualität")
    routing_score: int = Field(..., ge=0, le=100, description="Verlegung")
    connection_score: int = Field(..., ge=0, le=100, description="Verbindungen")
    safety_score: int = Field(..., ge=0, le=100, description="Sicherheit")
    findings: list[CableVisualFinding] = Field(default_factory=list)
    confidence: ConfidenceLevel
    summary_de: str = Field(..., description="Zusammenfassung auf Deutsch")
```

---

## ANHANG Q — AYDI-Integration: NMEA 2000 Netzwerk-Modell

```python
"""
AYDI Wissensmodul 22.03 — NMEA 2000 Netzwerk-Diagnose-Modelle
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .cable_base_models import ConfidenceLevel


class NMEA2000Device(BaseModel):
    """Ein Gerät im NMEA 2000 Netzwerk."""
    model_config = {"from_attributes": True}

    device_name: str
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    pgn_list: list[int] = Field(
        default_factory=list, description="Liste der empfangenen/gesendeten PGNs"
    )
    drop_cable_length_m: float = Field(
        ..., gt=0, le=10,
        description="Stichleitungslänge in m (max. 6m empfohlen)",
    )
    current_draw_ma: Optional[float] = Field(
        None, gt=0, description="Stromaufnahme vom Netzwerk in mA"
    )
    is_functional: bool = True
    notes: list[str] = Field(default_factory=list)


class NMEA2000NetworkAssessment(BaseModel):
    """Bewertung eines NMEA 2000 Netzwerks."""
    model_config = {"from_attributes": True}

    backbone_length_m: float = Field(..., gt=0, description="Backbone-Länge in m")
    backbone_cable_type: str = Field(
        ..., description="z.B. 'DeviceNet Micro-C' oder 'Standard-Steuerleitung'"
    )
    backbone_impedance_correct: Optional[bool] = Field(
        None, description="120 Ω ± 10%?"
    )
    num_terminators: int = Field(..., ge=0, le=10)
    measured_total_resistance_ohm: Optional[float] = Field(
        None, description="Gemessener Gesamtwiderstand (soll ~60 Ω bei 2 Terminatoren)"
    )
    supply_voltage_v: Optional[float] = Field(None, description="Versorgungsspannung am Backbone")
    total_current_draw_ma: Optional[float] = Field(
        None, description="Gesamtstromaufnahme aller Geräte"
    )
    devices: list[NMEA2000Device] = Field(default_factory=list)
    num_devices: int = Field(0, ge=0)

    # Bewertung
    overall_score: int = Field(..., ge=0, le=100)
    backbone_score: int = Field(..., ge=0, le=100)
    termination_score: int = Field(..., ge=0, le=100)
    drop_cable_score: int = Field(..., ge=0, le=100)
    power_score: int = Field(..., ge=0, le=100)

    findings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    confidence: ConfidenceLevel


def assess_nmea2000_network(
    backbone_length_m: float,
    backbone_cable_type: str,
    num_terminators: int,
    devices: list[NMEA2000Device],
    supply_voltage_v: Optional[float] = None,
    measured_resistance_ohm: Optional[float] = None,
) -> NMEA2000NetworkAssessment:
    """
    Bewertet ein NMEA 2000 Netzwerk und gibt Empfehlungen.
    """
    findings: list[str] = []
    recommendations: list[str] = []

    # Backbone-Bewertung
    backbone_score = 100
    impedance_correct = None

    if "devicenet" in backbone_cable_type.lower() or "nmea" in backbone_cable_type.lower():
        impedance_correct = True
    elif "steuer" in backbone_cable_type.lower() or "liycy" in backbone_cable_type.lower():
        impedance_correct = False
        backbone_score -= 50
        findings.append("KRITISCH: Standard-Steuerkabel statt DeviceNet Micro-C als Backbone.")
        recommendations.append("Backbone durch zertifiziertes NMEA 2000 Kabel ersetzen.")

    if backbone_length_m > 100:
        backbone_score -= 30
        findings.append(f"Backbone-Länge {backbone_length_m}m überschreitet 100m Maximum.")
        recommendations.append("Repeater einsetzen oder Backbone-Layout optimieren.")
    elif backbone_length_m > 80:
        backbone_score -= 10
        findings.append(f"Backbone-Länge {backbone_length_m}m nähert sich dem 100m-Limit.")

    # Terminierung
    termination_score = 100
    if num_terminators != 2:
        termination_score = 20
        findings.append(
            f"{num_terminators} Terminator(en) statt 2. "
            "Exakt 2 Terminatoren (120 Ω) an den Backbone-Enden erforderlich."
        )
        recommendations.append(
            "Terminierung korrigieren: genau 2× 120 Ω an den Backbone-Enden."
        )

    if measured_resistance_ohm is not None:
        if 55 <= measured_resistance_ohm <= 65:
            pass  # OK
        elif 110 <= measured_resistance_ohm <= 130:
            termination_score -= 40
            findings.append("Gesamtwiderstand ~120 Ω → vermutlich nur 1 Terminator.")
        else:
            termination_score -= 60
            findings.append(
                f"Gesamtwiderstand {measured_resistance_ohm} Ω — "
                "Terminierung fehlerhaft oder Backbone unterbrochen."
            )

    # Stichleitungen
    drop_cable_score = 100
    for device in devices:
        if device.drop_cable_length_m > 6:
            drop_cable_score -= 20
            findings.append(
                f"Gerät '{device.device_name}': Stichleitung {device.drop_cable_length_m}m "
                "> 6m Maximum."
            )
            recommendations.append(
                f"Stichleitung von '{device.device_name}' auf ≤6m kürzen."
            )

    # Versorgung
    power_score = 100
    if supply_voltage_v is not None:
        if supply_voltage_v < 9:
            power_score = 20
            findings.append(f"Versorgungsspannung {supply_voltage_v}V < 9V Minimum.")
        elif supply_voltage_v < 10:
            power_score -= 30
            findings.append(f"Versorgungsspannung {supply_voltage_v}V niedrig (Grenzbereich).")

    num_devices = len(devices)
    if num_devices > 50:
        power_score -= 30
        findings.append(f"{num_devices} Geräte überschreiten das 50-Geräte-Limit.")

    # Gesamtbewertung
    overall_score = int(
        backbone_score * 0.35
        + termination_score * 0.25
        + drop_cable_score * 0.20
        + power_score * 0.20
    )

    return NMEA2000NetworkAssessment(
        backbone_length_m=backbone_length_m,
        backbone_cable_type=backbone_cable_type,
        backbone_impedance_correct=impedance_correct,
        num_terminators=num_terminators,
        measured_total_resistance_ohm=measured_resistance_ohm,
        supply_voltage_v=supply_voltage_v,
        total_current_draw_ma=None,
        devices=devices,
        num_devices=num_devices,
        overall_score=max(0, min(100, overall_score)),
        backbone_score=max(0, backbone_score),
        termination_score=max(0, termination_score),
        drop_cable_score=max(0, drop_cable_score),
        power_score=max(0, power_score),
        findings=findings,
        recommendations=recommendations,
        confidence=ConfidenceLevel.CALCULATED if measured_resistance_ohm else ConfidenceLevel.ESTIMATED,
    )
```

---

## ANHANG R — AYDI-Integration: Scoring-Fusion Kabelmodul

```python
"""
AYDI Wissensmodul 22.03 — Score-Fusion für das Kabelmodul
Kombiniert strukturelle und visuelle Analyse.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field

from .cable_base_models import ConfidenceLevel


class CableModuleStructuredScore(BaseModel):
    """Strukturelle Bewertung (Pipeline A) des Kabelmoduls."""
    model_config = {"from_attributes": True}

    marine_grade_score: int = Field(..., ge=0, le=100)
    voltage_drop_score: int = Field(..., ge=0, le=100)
    fuse_sizing_score: int = Field(..., ge=0, le=100)
    conductor_tinning_score: int = Field(..., ge=0, le=100)
    insulation_appropriateness_score: int = Field(..., ge=0, le=100)
    nmea_network_score: Optional[int] = Field(None, ge=0, le=100)

    overall_structured_score: int = Field(..., ge=0, le=100)
    confidence: ConfidenceLevel


class CableModuleVisualScore(BaseModel):
    """Visuelle Bewertung (Pipeline B) des Kabelmoduls."""
    model_config = {"from_attributes": True}

    routing_visual_score: int = Field(..., ge=0, le=100)
    connection_visual_score: int = Field(..., ge=0, le=100)
    safety_visual_score: int = Field(..., ge=0, le=100)
    labeling_visual_score: int = Field(..., ge=0, le=100)

    overall_visual_score: int = Field(..., ge=0, le=100)
    confidence: ConfidenceLevel


class CableModuleFusedScore(BaseModel):
    """Fusionierter Score für das Kabelmodul."""
    model_config = {"from_attributes": True}

    structured_score: Optional[CableModuleStructuredScore] = None
    visual_score: Optional[CableModuleVisualScore] = None

    # Fusionsgewichte (aus CLAUDE.md Score Fusion Weights)
    # Kabel fällt unter "compliance" oder eigene Gewichtung
    structured_weight: float = Field(default=0.70)
    visual_weight: float = Field(default=0.30)

    fused_score: int = Field(..., ge=0, le=100)
    confidence: ConfidenceLevel

    critical_findings_count: int = Field(0, ge=0)
    high_findings_count: int = Field(0, ge=0)
    medium_findings_count: int = Field(0, ge=0)

    summary_de: str = Field(..., description="Zusammenfassung auf Deutsch")
    top_recommendations: list[str] = Field(
        default_factory=list, description="Top-3 Empfehlungen, priorisiert"
    )


def fuse_cable_scores(
    structured: Optional[CableModuleStructuredScore],
    visual: Optional[CableModuleVisualScore],
    structured_weight: float = 0.70,
    visual_weight: float = 0.30,
) -> CableModuleFusedScore:
    """
    Fusioniert strukturelle und visuelle Bewertung des Kabelmoduls.

    Wenn nur eine Quelle vorliegt, wird diese mit 100% gewichtet.
    Wenn keine vorliegt, wird Score 0 mit visual_insufficient zurückgegeben.
    """
    if structured is None and visual is None:
        return CableModuleFusedScore(
            structured_score=None,
            visual_score=None,
            structured_weight=structured_weight,
            visual_weight=visual_weight,
            fused_score=0,
            confidence=ConfidenceLevel.VISUAL_INSUFFICIENT,
            summary_de="Keine Daten für Kabelbewertung vorhanden.",
            top_recommendations=["Kabelinspektion durchführen (strukturell und/oder visuell)."],
        )

    if structured is not None and visual is not None:
        fused = int(
            structured.overall_structured_score * structured_weight
            + visual.overall_visual_score * visual_weight
        )
        # Confidence: niedrigere der beiden Quellen
        conf = _lower_confidence(structured.confidence, visual.confidence)
    elif structured is not None:
        fused = structured.overall_structured_score
        conf = structured.confidence
    else:
        assert visual is not None
        fused = visual.overall_visual_score
        conf = visual.confidence

    # Zusammenfassung generieren
    if fused >= 80:
        summary = "Kabelinstallation in gutem Zustand. Keine kritischen Mängel."
    elif fused >= 60:
        summary = "Kabelinstallation akzeptabel, einige Verbesserungen empfohlen."
    elif fused >= 40:
        summary = "Kabelinstallation weist erhebliche Mängel auf. Sanierung empfohlen."
    else:
        summary = "Kabelinstallation in schlechtem Zustand. Dringende Sanierung erforderlich."

    return CableModuleFusedScore(
        structured_score=structured,
        visual_score=visual,
        structured_weight=structured_weight,
        visual_weight=visual_weight,
        fused_score=max(0, min(100, fused)),
        confidence=conf,
        summary_de=summary,
        top_recommendations=[],
    )


def _lower_confidence(a: ConfidenceLevel, b: ConfidenceLevel) -> ConfidenceLevel:
    """Gibt das niedrigere Confidence-Level zurück."""
    order = [
        ConfidenceLevel.MEASURED,
        ConfidenceLevel.CALCULATED,
        ConfidenceLevel.DOCUMENTED,
        ConfidenceLevel.VISUAL_HIGH,
        ConfidenceLevel.VISUAL_MEDIUM,
        ConfidenceLevel.ESTIMATED,
        ConfidenceLevel.BENCHMARK,
        ConfidenceLevel.VISUAL_LOW,
        ConfidenceLevel.VISUAL_INSUFFICIENT,
    ]
    idx_a = order.index(a) if a in order else len(order) - 1
    idx_b = order.index(b) if b in order else len(order) - 1
    return order[max(idx_a, idx_b)]
```

---

> **Ende der AYDI Wissensdatei 22.03 — Kabel und Leitungen**
> **Confidence-Mapping:** Alle Herstellerangaben basieren auf öffentlich verfügbaren Datenblättern (documented). Berechnungsformeln sind nach ABYC E-11 / ISO 13297 (measured). Erfahrungswerte und Preise sind estimated. Pydantic-Modelle sind als calculated markiert, da sie aus den Wissensinhalten algorithmisch abgeleitet werden.
