# 14.03 — Hydraulische Steuerung (Helmpumpen, Zylinder, Servolenkung, Autopilot-Integration): Vollständige Wissensreferenz

> **AYDI Wissensdatei 14.03** — Kategorie 14: Steueranlagen
> **Confidence-Quelle:** measured (Hersteller-TDS), documented (Hersteller-Kataloge, Testberichte), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-26

---

```yaml
title: "Hydraulische Steuerung"
kategorie: "14 Steueranlagen"
unterkategorie: "03 Hydraulische Steuerung"
version: "1.0.0"
datum: "2026-04-26"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Datenblätter, zertifizierte Prüfberichte"
  - documented: "Practical Sailor, SAIL Magazine, Yachtsurvey.com, RINA Papers"
  - estimated: "Erfahrungswerte, Eigner-Konsens, Forum-Auswertung"
normen_referenzen:
  - "ISO 8847:2021 — Seilzug-/Umlenkrollensteuerung (Cable over pulley) — NICHT hydraulisch, nur Quer-Referenz"
  - "ISO 8848:2020 — Fernsteuereinrichtungen"
  - "ISO 25197:2020 — Steuerungssysteme für Boote"
  - "ABYC P-21 — Hydraulic Steering Systems"
  - "CE Recreational Craft Directive 2013/53/EU"
  - "NMMA Certification Requirements — Steering"
  - "GL Rules for Classification of Yachts — Steering Gear"
  # ✅ Aufgeloest (Audit): fehlerhafte Zeile "ISO 21329:2004 — Hydraulische Servosteuerung" entfernt — ISO 21329:2004 ist "Petroleum and natural gas industries — Pipeline transportation systems — Test procedures for mechanical connectors" (KEINE Marine-/Steuerungsnorm). Die massgebliche Hydraulik-Steuerungsnorm ist ISO 10592 (nachfolgende Zeile). Quelle: iso.org/standard/35842.
  - "ISO 10592:1994 — Hydraulische Steuereinrichtungen (Small craft — Hydraulic steering systems)"
abhängigkeiten:
  - "14_01_ruderanlage_grundlagen.md"
  - "14_02_mechanische_steuerung.md"
  - "14_04_autopilot_systeme.md"
  - "06_07_hydraulikschlaeuche.md"
```

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Grundlagen](#2-grundlagen)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien und Hersteller](#4-produktlinien-und-hersteller)
5. [Autopilot-Integration](#5-autopilot-integration)
6. [Installation](#6-installation)
7. [Fehlerbild-Atlas](#7-fehlerbild-atlas)
8. [Troubleshooting](#8-troubleshooting)
9. [FAQ — Häufige Fragen](#9-faq--häufige-fragen)
10. [Glossar](#10-glossar)
11. [Schnell-Referenz](#11-schnell-referenz)
12. [ANHANG A — Fallstudien](#anhang-a--fallstudien)
13. [ANHANG B — Druckberechnungstabellen](#anhang-b--druckberechnungstabellen)
14. [ANHANG C — Confidence-Mapping](#anhang-c--confidence-mapping)
15. [ANHANG D — Normen-Zusammenfassung](#anhang-d--normen-zusammenfassung)
16. [ANHANG E — Wartungsintervalle](#anhang-e--wartungsintervalle)
17. [ANHANG F — Leitungsverlust-Diagramme](#anhang-f--leitungsverlust-diagramme)
18. [ANHANG G — Historische Entwicklung](#anhang-g--historische-entwicklung)
19. [ANHANG H — AYDI-Integration (Pydantic-Modelle)](#anhang-h--aydi-integration-pydantic-modelle)
20. [ANHANG I — Bewertungsschema](#anhang-i--bewertungsschema)
21. [ANHANG J — Troubleshooting-Entscheidungsbäume (erweitert)](#anhang-j--troubleshooting-entscheidungsbäume-erweitert)
22. [ANHANG K — Kostenkalkulation](#anhang-k--kostenkalkulation)
23. [ANHANG L — Regionale Besonderheiten](#anhang-l--regionale-besonderheiten)
24. [ANHANG M — Testprotokolle und Prüfverfahren](#anhang-m--testprotokolle-und-prüfverfahren)
25. [ANHANG N — Zusätzliche Fallstudien](#anhang-n--zusätzliche-fallstudien)
26. [ANHANG O — Eigner-Erfahrungen und Feldberichte](#anhang-o--eigner-erfahrungen-und-feldberichte)
27. [ANHANG P — Materialkunde Hydraulikkomponenten](#anhang-p--materialkunde-hydraulikkomponenten)
28. [ANHANG Q — Notsteuerung bei Systemversagen](#anhang-q--notsteuerung-bei-systemversagen)
29. [ANHANG R — Zukunftstrends](#anhang-r--zukunftstrends)

---

## 1. Einführung

### 1.1 Bedeutung der hydraulischen Steuerung im Yachtbau

Die hydraulische Steuerung ist das dominante Lenksystem für Yachten ab ca. 12 Metern Länge (Segelboote) bzw. ab ca. 10 Metern (Motorboote). Sie überträgt die Drehbewegung des Steuerrades über eine Helmpumpe in hydraulischen Druck, der einen Zylinder oder Kolben am Ruderschaft betätigt. Im Vergleich zu mechanischen Systemen bietet sie höhere Ruderkräfte, geringere Steuerreibung über lange Leitungswege und nahtlose Autopilot-Integration.

**Statistische Relevanz:**
- Ca. 85–95 % aller Segelboote über 14 Meter verwenden hydraulische Steuerungen (Quelle: Jefa-Marktanalyse 2023, Lecomble & Schmitt Marktstudie 2024).
- Bei Motorbooten über 10 Meter dominieren hydraulische Systeme zu über 90 % (SeaStar/Dometic Schätzung).
- Marktvolumen hydraulische Yachtsteuerungen weltweit: ca. 280 Mio. EUR (2024), Wachstum ca. 4 % p.a. (Confidence: estimated).
- Die häufigsten Steuerungsprobleme bei hydraulischen Systemen: Luft im System (28 %), Dichtungsverschleiß an Helmpumpe (21 %), Zylinderinterne Leckage (16 %), Schlauchdegradation (13 %), Fluidkontamination (10 %), Ventilblockaden (7 %), Korrosion an Anschlüssen (5 %).
- Durchschnittliche Lebensdauer eines gut gewarteten Systems: 15–25 Jahre für Zylinder, 10–18 Jahre für Helmpumpen, 8–12 Jahre für Schläuche (Confidence: estimated).
- Kosten einer Kompletterneuerung: 2.500–15.000 EUR je nach Bootsgröße und System (Confidence: estimated).

### 1.2 Abgrenzung zu anderen Steuerungssystemen

Die hydraulische Steuerung grenzt sich wie folgt ab:

- **Mechanische Steuerung (14_02):** Rein mechanische Kraftübertragung via Seil, Kette oder Schubstange. Begrenzt auf kleinere Boote und niedrigere Ruderkräfte. Bessere Rückmeldung, aber höhere Reibung bei langen Leitungswegen.
- **Pinnensteuerung (14_01):** Direkte Verbindung Pinne → Ruderkoker. Keine Übertragungselemente. Limitiert auf Boote bis ca. 10 m (Segel) oder 7 m (Motor).
- **Elektrohydraulische Steuerung:** Erweiterung der hydraulischen Steuerung um eine elektrische Pumpe (Power-Assist oder Full-Power). Für Yachten ab ca. 18 m, Superyachten, Katamarane. Ermöglicht mehrere Steuerplätze ohne mechanische Koppelung.
- **Fly-by-Wire:** Elektronische Signalübertragung, Elektromotor am Ruder. Kein hydraulisches Fluid. Aktuell nur bei großen Yachten (>30 m).

**Entscheidungsmatrix: Wann hydraulisch?**

| Kriterium | Manuell hydraulisch | Power-Assist | Full Power | Proportionalventil |
|-----------|-------------------|--------------|------------|-------------------|
| Boot LOA | 10–18 m | 14–25 m | 18–40 m | >25 m |
| Ruderkraft max. | 200 kgf | 500 kgf | 2.000+ kgf | 5.000+ kgf |
| Gewicht System | 12–30 kg | 25–60 kg | 40–120 kg | 60–200 kg |
| Rückmeldung | Gut (Feedback) | Mittel | Gering | Programmierbar |
| Wartung | Mittel | Mittel–Hoch | Hoch | Hoch |
| Kosten | 1.500–5.000 EUR | 3.500–12.000 EUR | 8.000–35.000 EUR | 15.000–80.000 EUR |
| Autopilot-Kompatibilität | Gut | Sehr gut | Hervorragend | Hervorragend |
| Steuerplätze | 1–2 | 1–3 | 1–5 | Beliebig |

### 1.3 Historische Entwicklung

- **1920er–1940er:** Erste hydraulische Ruderanlagen auf Handelsschiffen und Marineschiffen. Rapson-Slide-Aktuatoren für Großschiffe.
- **1950er–1960er:** Erste kompakte Hydrauliksysteme für große Motoryachten (>20 m). Hynautic (USA, gegründet 1959) und Wagner Engineering als Pioniere.
- **1965–1975:** Lecomble & Schmitt (Frankreich, gegründet 1868) bringt kompakte Helmpumpen für Fahrtenyachten. Teleflex beginnt mit SeaStar-Linie für Motorboote.
- **1975–1990:** Hydraulische Steuerung wird Standard ab 14 m Segellänge. Jefa (Dänemark) entwickelt Direct-Drive-Hydraulikzylinder. Whitlock (später Lewmar) bietet kombinierte Systeme an.
- **1990–2005:** Autopilot-kompatible Hydrauliksysteme etablieren sich. Solenoidventil-Integration. Kobelt (Kanada) spezialisiert sich auf schwere Motoryachten.
- **2005–2015:** Vetus (Niederlande) steigt in den Hydrauliksteuerungsmarkt ein. Dometic übernimmt SeaStar. Proportionalventilsteuerungen für Superyachten.
- **2015–heute:** Bio-abbaubare Hydraulikfluide. Integrierte Autopilot-Hydraulikantriebe (Raymarine Evolution, B&G H5000). Diagnose-Sensorik (Drucksensoren, Durchflussmesser). Trend zu kompakteren Pumpeneinheiten und höheren Systemdrücken.

### 1.4 Geltungsbereich dieser Wissensdatei

Diese Datei deckt alle hydraulischen Steuerungssysteme für Sport- und Fahrtenyachten ab:

1. **Manuelle Hydrauliksteuerung** (Manual Hydraulic) — Helmpumpe erzeugt Druck rein durch Handkraft am Steuerrad
2. **Servohydraulische Steuerung** (Power-Assisted Hydraulic) — manuelle Helmpumpe mit elektrischer Unterstützungspumpe
3. **Vollhydraulische Steuerung** (Full Power Hydraulic) — elektrische Pumpe erzeugt gesamten Systemdruck, Steuerrad betätigt nur Steuerventil
4. **Proportionalventil-Steuerung** (Proportional Valve) — elektronisch geregelte Ventile, stufenlose Steuerung, Joystick-fähig
5. **Autopilot-Hydraulikantriebe** (Autopilot Hydraulic Drives) — dedizierte oder integrierte Hydraulikantriebe für Autopiloten

Nicht behandelt: Pinnensteuerung (14_01), mechanische Steuerung (14_02), Autopilot-Elektronik und -Algorithmen (14_04), Bugstrahlruder-Hydraulik (15_xx).

---

## 2. Grundlagen

### 2.1 Hydraulische Grundprinzipien

#### 2.1.1 Pascalsches Gesetz

Das Fundament jeder hydraulischen Steuerung ist das **Pascalsche Gesetz** (Blaise Pascal, 1653):

> Ein Druck, der auf ein eingeschlossenes Fluid ausgeübt wird, wird gleichmäßig in alle Richtungen und auf alle Begrenzungsflächen übertragen.

**Mathematische Formulierung:**

```
p = F / A
```

Wobei:
- `p` = Druck [Pa] oder [bar] (1 bar = 100.000 Pa = 14,5 psi)
- `F` = Kraft [N]
- `A` = Kolbenfläche [m²]

**Kraftverstärkung:**

```
F₂ / F₁ = A₂ / A₁
```

Die Kraftverstärkung ist das Verhältnis der Kolbenflächen. Eine Helmpumpe mit kleinem Kolben (A₁) erzeugt am großen Zylinder (A₂) eine proportional höhere Kraft — bei gleichzeitig proportional geringerem Hub.

**Praxisbeispiel Yachtsteuerung:**
- Helmpumpe: Kolbendurchmesser 25 mm → A₁ = π/4 × 0,025² = 4,91 cm²
- Steuerzylinder: Kolbendurchmesser 60 mm → A₂ = π/4 × 0,060² = 28,27 cm²
- Kraftverstärkung: 28,27 / 4,91 = 5,76:1
- Handkraft am Steuerrad 8 kgf → Ruderkraft 46 kgf (ohne Reibungsverluste)

#### 2.1.2 Volumenstrom und Kolbenbewegung

Der Zusammenhang zwischen Pumpenhub und Zylinderweg ergibt sich aus der Volumenerhaltung:

```
V_pump = V_cylinder
A₁ × s₁ = A₂ × s₂
s₂ = s₁ × (A₁ / A₂)
```

Wobei:
- `s₁` = Pumpenhub [mm]
- `s₂` = Zylinderhub [mm]

Die Anzahl der Steuerrad-Umdrehungen von Anschlag zu Anschlag (Lock-to-Lock) ergibt sich aus:

```
n_turns = (s₂_total × A₂) / (V_pump_per_turn)
```

**Typische Werte:**
- Segelyacht 12 m: 3,0–4,5 Umdrehungen Lock-to-Lock
- Segelyacht 18 m: 3,5–5,0 Umdrehungen Lock-to-Lock
- Motoryacht 12 m: 3,5–5,5 Umdrehungen Lock-to-Lock
- Motoryacht 20 m: 4,0–6,0 Umdrehungen Lock-to-Lock

#### 2.1.3 Systemdruck

**Typische Betriebsdrücke in der Yachthydraulik:**

| Systemtyp | Normaler Betriebsdruck | Maximaldruck | Berstdruck Schlauch |
|-----------|----------------------|--------------|---------------------|
| Manuell hydraulisch (klein) | 35–50 bar | 70 bar | >210 bar |
| Manuell hydraulisch (groß) | 50–70 bar | 100 bar | >300 bar |
| Power-Assist | 50–100 bar | 140 bar | >420 bar |
| Full Power | 80–140 bar | 200 bar | >600 bar |
| Proportionalventil | 100–200 bar | 280 bar | >840 bar |

**Druckberechnung am Steuerzylinder:**

```
p_system = T_rudder / (r_tiller × A_cylinder × η)
```

Wobei:
- `T_rudder` = Ruderdrehmoment [Nm]
- `r_tiller` = Tillerarm-Länge (Hebel am Zylinder) [m]
- `A_cylinder` = effektive Kolbenfläche [m²]
- `η` = Systemwirkungsgrad (typisch 0,80–0,92)

#### 2.1.4 Ruderdrehmoment-Berechnung

Das maximale Ruderdrehmoment ist die zentrale Auslegungsgröße:

**Segelboote (empirische Formel nach Jefa):**
```
T_rudder [Nm] = 0,12 × LWL [m] × D [m] × V² [kn] × A_rudder [m²] × C_balance
```

**Motorboote (empirische Formel nach Kobelt):**
```
T_rudder [Nm] = 0,18 × LWL [m] × V² [kn] × A_rudder [m²] × C_balance × C_propwash
```

Wobei:
- `LWL` = Wasserlinienlänge
- `D` = Tiefgang
- `V` = Maximalgeschwindigkeit (Rumpfgeschwindigkeit bei Seglern, Marschgeschwindigkeit bei Motor)
- `A_rudder` = Ruderfläche
- `C_balance` = Balancefaktor (0,8 für balanced, 1,0 für semi-balanced, 1,3 für unbalanced)
- `C_propwash` = Propellerstrahleinfluss (1,0 bei Saildrive, 1,2 bei Wellenanlage direkt vor Ruder, 1,4 bei Twin-Screw direkt)

**Referenzwerte Ruderdrehmoment:**

| Bootstyp | LOA | Ruderdrehmoment (geschätzt) |
|----------|-----|---------------------------|
| Segelyacht Cruiser | 10 m | 80–150 Nm |
| Segelyacht Cruiser | 12 m | 150–280 Nm |
| Segelyacht Cruiser | 14 m | 250–450 Nm |
| Segelyacht Cruiser | 18 m | 400–800 Nm |
| Segelyacht Performance | 12 m | 200–400 Nm |
| Segelyacht Performance | 16 m | 500–1.000 Nm |
| Motoryacht Verdränger | 12 m | 200–400 Nm |
| Motoryacht Verdränger | 16 m | 400–800 Nm |
| Motoryacht Halbgleiter | 10 m | 300–600 Nm |
| Motoryacht Gleiter | 10 m | 400–800 Nm |
| Motoryacht Verdränger | 20 m | 700–1.500 Nm |
| Motoryacht Verdränger | 25 m | 1.200–2.500 Nm |

(Confidence: estimated — genaue Werte hängen stark von Ruderform, Balance und Geschwindigkeit ab)

### 2.2 Zylinderauslegung (Cylinder Sizing)

#### 2.2.1 Kolbenfläche und Hub

Die Zylinderauslegung muss folgende Anforderungen erfüllen:
1. Ausreichende Kraft bei maximalem Ruderdrehmoment
2. Ausreichender Hub für den gesamten Ruderwinkelbereich (typisch ±35° bis ±40°)
3. Passende Lock-to-Lock-Umdrehungszahl am Steuerrad

**Zylindertypen nach Bauform:**

| Bauform | Kolben-Ø typisch | Hub typisch | Einsatz |
|---------|-----------------|-------------|---------|
| Single-Ram (einfachwirkend) | 40–80 mm | 150–300 mm | Motorboote 8–14 m |
| Double-Ram (doppeltwirkend) | 50–100 mm | 150–350 mm | Segel-/Motoryachten 12–25 m |
| Balanced Ram (symmetrisch) | 60–120 mm | 100–250 mm | Performance-Segler, große Yachten |
| Rotary Actuator (Drehflügel) | n/a | n/a (Winkel) | Kompakte Installation, Segelyachten |
| Inline Cylinder | 40–70 mm | 200–400 mm | Motorboote mit begrenztem Platz |

**Hubberechnung aus Ruderwinkel:**

Für einen Steuerzylinder, der über einen Tillerarm (Ruderhebel) am Ruderschaft angreift:

```
Stroke = 2 × r_tiller × sin(α_max)
```

Wobei:
- `r_tiller` = Abstand Ruderschaft-Mitte → Zylinderanschluss [mm]
- `α_max` = maximaler Ruderwinkel [°] (typisch 35°)

**Beispiel:**
- Tillerarm 200 mm, Ruderwinkel ±35°
- Stroke = 2 × 200 × sin(35°) = 2 × 200 × 0,5736 = 229 mm
- Gewählter Zylinder: mindestens 250 mm Hub (Sicherheitsmarge)

#### 2.2.2 Kraftberechnung am Zylinder

```
F_cylinder = T_rudder / r_tiller
```

**Beispiel:**
- Ruderdrehmoment 400 Nm, Tillerarm 200 mm
- F_cylinder = 400 / 0,200 = 2.000 N = 204 kgf

Erforderliche Kolbenfläche bei 50 bar Systemdruck:
```
A_cylinder = F_cylinder / p = 2.000 / (50 × 10⁵) = 4,0 × 10⁻⁴ m² = 4,0 cm²
→ Kolbendurchmesser = √(4 × 4,0 / π) = 2,26 cm ≈ 23 mm (Mindestmaß)
```

In der Praxis werden deutlich größere Zylinder gewählt (typisch 50–80 mm Kolben-Ø), um den Systemdruck niedrig zu halten und Reserven zu bieten.

### 2.3 Pumpenverdrängung (Pump Displacement)

#### 2.3.1 Helmpumpen-Typen

| Pumpentyp | Verdrängung typisch | Druckbereich | Einsatz |
|-----------|-------------------|--------------|---------|
| Drehschieber (Rotary Vane) | 8–30 cm³/Umdrehung | 35–70 bar | Standard Segelyachten, Motorboote |
| Axialkolben (Axial Piston) | 5–20 cm³/Umdrehung | 50–140 bar | Performance-Segler, Power-Assist |
| Radialkolben (Radial Piston) | 10–50 cm³/Umdrehung | 70–200 bar | Große Yachten, Full Power |
| Zahnrad (Gear) | 15–80 cm³/Umdrehung | 50–100 bar | Industrielle Anwendung, Power-Packs |
| Flügelzellen (Vane, balanciert) | 5–25 cm³/Umdrehung | 35–70 bar | Standard-Helmpumpe SeaStar, Lecomble |

**Verdrängungsberechnung:**

Die Pumpenverdrängung bestimmt die Lock-to-Lock-Umdrehungen:

```
V_pump = V_cylinder_total / n_turns
```

Wobei:
- `V_cylinder_total` = Gesamtvolumen beider Zylinderseiten für vollen Hub [cm³]
- `n_turns` = gewünschte Lock-to-Lock-Umdrehungen

**Beispiel:**
- Zylinder Ø 60 mm, Hub 250 mm
- V_cylinder = π/4 × 6² × 25 = 706,9 cm³ (einseitig) → 706,9 cm³ pro Richtung (doppeltwirkend)
- Gewünschte Umdrehungen: 4,0
- Benötigte Verdrängung: 706,9 / 4,0 = 176,7 cm³ → 2 × 88 cm³ (weil doppeltwirkend → Hälfte pro Seite wird gepumpt)
- Für doppeltwirkenden Zylinder: V_pump_effective = A_piston × Stroke / n_turns = 28,27 × 25 / 4 = 176,7 cm³
- Bei einer Helmpumpe mit 18 cm³/Umdrehung: n_turns = 706,9 / 18 = 39,3 → zu viele!

Korrektur: Bei doppeltwirkendem Zylinder fließt das Fluid von einer Seite zur anderen. Das relevante Volumen ist:

```
V_relevant = A_piston × Stroke_total = 28,27 cm² × 25 cm = 706,9 cm³
n_turns = V_relevant / V_pump_per_turn = 706,9 / 18 = 39,3
```

Das ist zu viel. Lösung: größere Pumpe oder Feedback-System mit Bypass.

**Praxisregel (Confidence: estimated):**
- Ziel: 3,0–5,0 Umdrehungen Lock-to-Lock für Segelboote
- Ziel: 3,5–6,0 Umdrehungen Lock-to-Lock für Motorboote
- Pumpenverdrängung = V_cylinder / n_turns_gewünscht

### 2.4 Hydraulikfluid-Eigenschaften

#### 2.4.1 Fluidtypen für Marine-Hydraulik

| Fluidtyp | ISO-Klasse | Viskosität bei 40°C | Einsatztemp. | Hersteller |
|----------|-----------|---------------------|--------------|------------|
| Mineralöl HLP 15 | ISO VG 15 | 13–17 cSt | –20 bis +80°C | Shell Tellus, Mobil DTE |
| Mineralöl HLP 32 | ISO VG 32 | 29–35 cSt | –10 bis +90°C | Shell Tellus S2 M32 |
| Mineralöl HLP 46 | ISO VG 46 | 41–51 cSt | 0 bis +100°C | Total Azolla, BP Energol |
| ATF (Dexron III/VI) | n/a | 30–38 cSt (40°C) | –30 bis +120°C | Diverse |
| Bio-Hydrauliköl HEES | ISO VG 32/46 | 32–46 cSt | –20 bis +80°C | Panolin HLP Synth |
| SeaStar/Dometic Fluid | proprietär | ~15 cSt | –30 bis +80°C | Dometic HA5430 |

**Wichtige Fluideigenschaften:**

- **Viskosität:** Zu dünn → interne Leckage, Verschleiß. Zu dick → schwergängig, Kavitation bei Kälte.
- **Viskositätsindex (VI):** Maß für Temperaturabhängigkeit. Marine: VI >100 empfohlen (Confidence: measured).
- **Wassertoleranz:** Marine-Fluide müssen geringe Mengen Kondenswasser tolerieren ohne Emulsionsbildung.
- **Korrosionsschutz:** Muss Stahl, Bronze und Aluminium gleichzeitig schützen.
- **Dichtungsverträglichkeit:** Kompatibel mit NBR (Nitrilkautschuk), Viton und Polyurethan-Dichtungen.
- **Schaumverhalten:** Geringe Schaumneigung, schnelles Entschäumen. Schaum = Luft im System = Schwammigkeit.

#### 2.4.2 Fluidwechsel und Kontamination

**Wechselintervalle (Confidence: documented/estimated):**

| Einsatzbedingung | Intervall | Anmerkung |
|-----------------|-----------|-----------|
| Normalnutzung (Saison) | 3–5 Jahre | Sichtprüfung jährlich |
| Intensivnutzung (Charter) | 2–3 Jahre | Partikelzählung empfohlen |
| Tropische Gewässer | 2–3 Jahre | Erhöhte Temperaturbelastung |
| Kalte Gewässer (Skandinavien) | 3–5 Jahre | Auf Kondensatbildung prüfen |
| Racing/Performance | 1–2 Jahre | Maximale Systemleistung |

**Kontaminationsquellen:**
1. Kondenswasser (häufigste Ursache — Temperaturwechsel)
2. Partikelabrieb (Pumpen-Flügelzellen, Dichtungen)
3. Schlauchdegradation (interne Gummipartikel)
4. Externes Eindringen (undichte Füllschraube, poröse Schläuche)
5. Falsche Fluidmischung (unterschiedliche Typen nicht kompatibel!)

**Kontaminationserkennung:**
- **Sichtprüfung:** Klares Bernstein = OK. Milchig = Wasser. Dunkel/Schwarz = Überhitzung/Abrieb.
- **Geruchsprüfung:** Verbrannt = Überhitzung. Süßlich = Dichtungszersetzung.
- **Tropfentest:** Auf Filterpapier tropfen. Klarer Ring = OK. Dunkler Kern = Partikel. Wasserrand = Feuchtigkeit.

### 2.5 Systemdruck-Bereiche

#### 2.5.1 Druckklassen für Yachtsteuerungen

```
Niederdruck-System:   35–50 bar  → Kleine Segelboote 10–14 m, Motorboote 8–12 m
Mitteldruck-System:   50–70 bar  → Segelboote 14–20 m, Motorboote 12–18 m
Hochdruck-System:     70–140 bar → Große Yachten 18–30 m, Power-Assist
Höchstdruck-System:   140–200 bar → Superyachten >30 m, Full Power
```

**Sicherheitsfaktoren:**
- Leitungen: Mindestens 4:1 Berstdruck:Betriebsdruck (ISO-Anforderung)
- Armaturen: Mindestens 3:1
- Zylinder: Mindestens 3:1
- Überdruckventil: Eingestellt auf 1,3–1,5 × Betriebsdruck

### 2.6 Non-Feedback vs. Feedback-Systeme

#### 2.6.1 Non-Feedback (Nicht-rücklaufend)

Bei Non-Feedback-Systemen hält der Zylinder seine Position ohne Haltekraft von der Pumpe. Das Ruder bleibt stehen, wenn das Steuerrad losgelassen wird.

**Funktionsprinzip:**
- Rückschlagventile in der Helmpumpe verhindern den Rücklauf des Fluids
- Interne Leckagedichtungen halten den Druck
- Notwendig für manuelle Systeme ohne Power-Pack

**Vorteile:**
- Ruder bleibt in Position ohne Energieaufwand
- Sicher bei losgelassenem Steuerrad
- Einfacher Aufbau

**Nachteile:**
- Ruderkraft-Rückmeldung (Feedback) fehlt oder ist stark gedämpft
- Kein „Geradeauslauf-Feedback" vom Wasser
- Bei Seglern oft als „taub" empfunden

**Anwendung:** Motorboote (fast ausschließlich), langsame Verdränger

#### 2.6.2 Feedback-Systeme (Rücklaufend)

Bei Feedback-Systemen wird ein Teil des Ruderdrucks an das Steuerrad zurückgemeldet. Der Steuermann spürt die Ruderkräfte.

**Funktionsprinzip:**
- Keine Rückschlagventile (oder gesteuerte Bypass-Ventile)
- Fluid kann vom Zylinder zurück zur Pumpe fließen
- Der Ruderdruck erzeugt ein spürbares Gegenmoment am Steuerrad
- Programmierbare Feedback-Ventile ermöglichen einstellbare Rückmeldung

**Vorteile:**
- Natürliches Steuergefühl, besonders wichtig bei Segelbooten
- Steuermann spürt Leegerigkeit, Luvgierigkeit, Wellenschlag
- Bessere Kontrolle bei hohen Geschwindigkeiten (Surfen)

**Nachteile:**
- Steuerrad dreht sich bei Ruderbelastung → Loslassen = Ruder fällt ab
- Höhere Handkräfte am Steuerrad
- Komplexerer Aufbau

**Anwendung:** Segelyachten (bevorzugt), Performance-Cruiser, einige Motoryachten auf Eignerwunsch

#### 2.6.3 Hybrid-Systeme (Einstellbares Feedback)

Moderne Systeme (z.B. Jefa, Lecomble & Schmitt) bieten einstellbare Feedback-Ventile:

```
Feedback-Level 0: Non-Feedback (Motorboot-Standard)
Feedback-Level 1: 10–20 % Rückmeldung (Verdränger-Motor)
Feedback-Level 2: 30–50 % Rückmeldung (Fahrtensegler)
Feedback-Level 3: 60–80 % Rückmeldung (Performance-Cruiser)
Feedback-Level 4: 80–95 % Rückmeldung (Regattasegler)
```

Das Feedback-Ventil ist typisch ein einstellbares Nadelventil oder ein Proportionalventil, das den Bypass-Strom reguliert.

### 2.7 Leitungsdimensionierung

#### 2.7.1 Schlauch-Innendurchmesser

Die Leitungsdimensionierung folgt der maximalen Strömungsgeschwindigkeit:

```
v_max = 3,0 m/s (Druckleitung)
v_max = 1,5 m/s (Rücklaufleitung)
v_max = 0,5 m/s (Saugleitung, falls vorhanden)
```

**Innendurchmesser-Berechnung:**

```
d_innen = √(4 × Q / (π × v_max))
```

**Typische Schlauchgrößen:**

| Systemgröße | Druck-ID | Rücklauf-ID | Anschluss |
|-------------|----------|-------------|-----------|
| Klein (bis 10 m) | 8 mm (5/16") | 10 mm (3/8") | ORB/JIC -6 |
| Mittel (10–18 m) | 10 mm (3/8") | 12 mm (1/2") | ORB/JIC -8 |
| Groß (18–25 m) | 12 mm (1/2") | 16 mm (5/8") | ORB/JIC -10 |
| Sehr groß (>25 m) | 16 mm (5/8") | 20 mm (3/4") | ORB/JIC -12 |

#### 2.7.2 Druckverlust in Leitungen

Druckverlust pro Meter Schlauch (Richtwerte für HLP 15 bei 20°C):

| Schlauch-ID | Q = 5 cm³/s | Q = 15 cm³/s | Q = 30 cm³/s |
|-------------|------------|-------------|-------------|
| 8 mm | 0,03 bar/m | 0,15 bar/m | 0,45 bar/m |
| 10 mm | 0,01 bar/m | 0,06 bar/m | 0,18 bar/m |
| 12 mm | 0,005 bar/m | 0,03 bar/m | 0,08 bar/m |
| 16 mm | 0,002 bar/m | 0,01 bar/m | 0,03 bar/m |

**Faustregel:** Gesamter Leitungsdruckverlust soll <5 % des Systemdrucks betragen (Confidence: documented).

### 2.8 Dichtungssysteme

#### 2.8.1 Dichtungstypen in Hydrauliksystemen

| Dichtungstyp | Material | Einsatzort | Max. Druck | Max. Temp. |
|-------------|----------|-----------|-----------|-----------|
| O-Ring (statisch) | NBR 70 Shore A | Gehäusedeckel, Anschlüsse | 400 bar | 100°C |
| O-Ring (dynamisch) | Viton 75 Shore A | Kolbenstange | 100 bar | 200°C |
| Kolbendichtung | PU/PTFE | Zylinderkolben | 200 bar | 80°C |
| Stangendichtung | PU + PTFE-Ring | Kolbenstange | 200 bar | 80°C |
| Abstreifer | NBR/PU | Kolbenstangenausgang | n/a | 80°C |
| Pumpendichtung | PTFE/Carbon | Drehschieber-Pumpe | 100 bar | 120°C |
| Wellendichtring | NBR + Feder | Pumpenwelle | 10 bar | 80°C |
| Flachdichtung | Kupfer/Aluminium | Verschraubungen | 400 bar | 300°C |

#### 2.8.2 Dichtungsverschleiß und Lebensdauer

**Typische Lebensdauer (Confidence: estimated):**
- Kolbenstangendichtungen: 5.000–15.000 Betriebsstunden oder 8–15 Jahre
- Pumpen-Flügelzellendichtungen: 3.000–10.000 Stunden oder 8–12 Jahre
- O-Ringe (statisch): 10–20 Jahre
- Wellendichtringe: 5–10 Jahre
- Abstreifer: 3.000–8.000 Stunden (erste Verschleißkomponente)

**Verschleißfaktoren:**
1. Temperatur: +10°C über Nenntemp. = halbe Lebensdauer
2. Kontamination: Partikel im Fluid beschleunigen Verschleiß exponentiell
3. Druckspitzen: Druckschläge (Waterhammer) zerstören Dichtungen
4. Seitenlast: Kolbenstangen-Seitenkraft → einseitiger Dichtungsverschleiß
5. Fluidkompatibilität: Falsches Fluid quillt oder schrumpft Dichtungen

---

## 3. Typenübersicht

### 3.1 Manuelle Hydrauliksteuerung (Manual Hydraulic)

#### 3.1.1 Systemarchitektur

```
Steuerrad → Helmpumpe → Druckleitung → Steuerzylinder → Tillerarm → Ruderschaft
                ↑                                              ↓
            Ausgleichsbehälter ← ← ← Rücklaufleitung ← ← ← ←
```

**Komponenten:**
1. **Helmpumpe (Helm Pump):** Wandelt Rotationsbewegung in Volumenstrom. Typisch: Drehschieberpumpe (rotary vane) mit 8–30 cm³/Umdrehung.
2. **Druckleitungen:** Zwei Schläuche (Druck/Rücklauf), je nach Drehrichtung wechselnd.
3. **Steuerzylinder:** Wandelt Druck in lineare Kraft. Typisch: Doppeltwirkend.
4. **Tillerarm:** Hebel am Ruderschaft, der Linearkraft in Drehmoment umsetzt.
5. **Ausgleichsbehälter:** Kompensiert Volumenänderungen durch Temperatur und Leckage.
6. **Überdruckventil (Relief Valve):** Schutz vor Druckspitzen bei Ruderschlag.
7. **Entlüftungsventile:** An Zylinder und Helmpumpe zum Entlüften.

#### 3.1.2 Feedback vs. Non-Feedback

Manuelle Systeme gibt es in beiden Varianten (siehe 2.6). Segelboote verwenden überwiegend Feedback-Systeme, Motorboote überwiegend Non-Feedback.

#### 3.1.3 Typische Kennwerte

| Parameter | Kleines System | Mittleres System | Großes System |
|-----------|---------------|-----------------|---------------|
| Bootsklasse | 10–14 m Segel | 14–18 m Segel | 18–22 m Segel |
| Pumpenverdrängung | 8–14 cm³/U | 14–22 cm³/U | 22–30 cm³/U |
| Zylinder-Ø | 40–55 mm | 55–80 mm | 80–100 mm |
| Zylinder-Hub | 150–220 mm | 200–280 mm | 250–350 mm |
| Betriebsdruck | 35–50 bar | 45–60 bar | 50–70 bar |
| Lock-to-Lock | 3,0–4,0 U | 3,5–4,5 U | 4,0–5,5 U |
| Max. Ruderdrehmoment | 300 Nm | 700 Nm | 1.500 Nm |
| Systemgewicht (trocken) | 8–14 kg | 14–22 kg | 22–35 kg |
| Fluidvolumen | 0,3–0,6 L | 0,6–1,2 L | 1,2–2,5 L |

### 3.2 Servohydraulische Steuerung (Power-Assisted Hydraulic)

#### 3.2.1 Systemarchitektur

```
Steuerrad → Helmpumpe → ┐
                         ├→ Mischblock/Prioritätsventil → Zylinder → Ruder
Elektropumpe → Power-Pack → ┘
                ↑
         Drucksensor / Lastfühler am Steuerrad
```

**Zusätzliche Komponenten gegenüber manueller Steuerung:**
1. **Power-Pack:** Elektromotor + Hydraulikpumpe (typisch 12V oder 24V DC, 0,5–3,0 kW)
2. **Prioritätsventil:** Stellt sicher, dass manuelle Pumpe immer Vorrang hat
3. **Druckbegrenzungsventil:** Limitiert Power-Pack-Druck
4. **Rückschlagventil:** Verhindert Rückfluss in Power-Pack bei manueller Betätigung
5. **Lastfühler (optional):** Schaltet Power-Pack bei erhöhter Steuerkraft automatisch zu

#### 3.2.2 Betriebsmodi

```
Modus 1 — Manuell:        Power-Pack aus. Reine Handkraft über Helmpumpe.
Modus 2 — Power-Assist:   Power-Pack unterstützt bei Bedarf. Steuermann bestimmt Richtung.
Modus 3 — Autopilot:      Power-Pack wird vom Autopilotcomputer angesteuert.
Modus 4 — Notbetrieb:     Power-Pack defekt → voller manueller Betrieb als Rückfallebene.
```

#### 3.2.3 Typische Kennwerte Power-Pack

| Parameter | 12V System | 24V System |
|-----------|-----------|-----------|
| Motorleistung | 0,5–1,5 kW | 1,0–3,0 kW |
| Fördermenge | 2–6 L/min | 4–12 L/min |
| Max. Druck | 70–100 bar | 100–140 bar |
| Stromaufnahme | 30–80 A | 20–60 A |
| Reservoirvolumen | 1–3 L | 2–6 L |
| Schallpegel | 55–70 dB(A) | 55–72 dB(A) |
| Gewicht | 8–18 kg | 12–30 kg |
| Einschaltdauer | 25–50 % ED | 25–60 % ED |

### 3.3 Vollhydraulische Steuerung (Full Power Hydraulic)

#### 3.3.1 Systemarchitektur

```
Steuerrad → Steuerventil (Orbitrol/Servo) → ┐
                                              ├→ Steuerzylinder → Ruder
Konstantdruck-Pumpe (elektrisch/motorgetrieben) → ┘
        ↑
   Reservoir → Filter → Kühler (optional)
```

**Schlüsselkomponenten:**
1. **Steuerventil (Orbitrol/Servo):** Proportional-Steuerventil, das den Volumenstrom zum Zylinder proportional zum Radwinkel dosiert. Kein Druck am Steuerrad — nur Signalgebung.
2. **Konstantdruck-Pumpe:** Liefert permanenten Systemdruck (80–200 bar). Läuft kontinuierlich oder On-Demand.
3. **Akkumulator (optional):** Speichert Hydraulikenergie für kurzzeitige Spitzenlasten.
4. **Redundanz:** Typisch doppelte Pumpe oder Hand-Notpumpe.

#### 3.3.2 Anwendung

- Motoryachten >20 m (meist Standard)
- Superyachten >30 m (immer)
- Katamarane >18 m
- Yachten mit mehreren Steuerständen (Flybridge + Salon + Achterdeck)
- Yachten mit Joystick-Steuerung (Docking-Modus)

#### 3.3.3 Typische Kennwerte

| Parameter | Mittelgroß (18–25 m) | Groß (25–40 m) |
|-----------|---------------------|----------------|
| Systemdruck | 80–120 bar | 120–200 bar |
| Pumpenleistung | 2–5 kW | 5–15 kW |
| Fördermenge | 6–15 L/min | 15–40 L/min |
| Reservoirvolumen | 5–15 L | 15–50 L |
| Zylinder-Ø | 80–120 mm | 100–160 mm |
| Max. Ruderdrehmoment | 2.000–5.000 Nm | 5.000–20.000 Nm |
| Ruderbewegungszeit (Anschlag→Anschlag) | 8–15 s | 10–20 s |
| Steuerplätze | 2–4 | 2–6 |

### 3.4 Proportionalventil-Steuerung (Proportional Valve)

#### 3.4.1 Funktionsprinzip

Das Proportionalventil regelt den Volumenstrom elektrisch-proportional. Ein Magnetspule positioniert den Ventilschieber stufenlos — je stärker das Signal, desto mehr Fluid fließt zum Zylinder. Dies ermöglicht:

- **Geschwindigkeitsabhängige Lenkunterstützung:** Bei niedriger Fahrt mehr Unterstützung, bei hoher Fahrt weniger.
- **Joystick-Steuerung:** Proportionale Steuerung ohne mechanische Verbindung.
- **Autopilot-Direktsteuerung:** Autopilot steuert Ventil direkt an.
- **Mehrere Steuerplätze:** Nur elektrische Leitungen, keine Hydraulikleitungen zum Steuerstand.

#### 3.4.2 Typische Systemkomponenten

1. Proportionalventil (4/3-Wegeventil mit Proportionalmagneten)
2. Konstantdruck-Hydraulikaggregat
3. Elektronische Steuereinheit (ECU)
4. Steuerrad mit Winkelsensor (Encoder)
5. Ruderlagenrückmeldung (Rudder Feedback Unit)
6. Joystick (optional)
7. Redundanz-Systeme (2. Ventil, 2. Pumpe, Handpumpe)

### 3.5 Rotary-Vane-Aktuator (Drehflügel-Stellantrieb)

#### 3.5.1 Funktionsprinzip

Statt eines Linearzylinders mit Tillerarm verwendet der Rotary-Vane-Aktuator einen Drehflügel direkt am Ruderschaft:

```
Hydraulikdruck → Drehflügel-Kammer → Direkte Rotation des Ruderschafts
```

**Vorteile:**
- Kompakte Bauform (kein Tillerarm-Platz nötig)
- Direkte Drehbewegung → kein Totpunkt-Problem
- Gleichmäßiges Drehmoment über den gesamten Ruderwinkel
- Einfachere Installation bei engen Platzverhältnissen

**Nachteile:**
- Höhere Kosten als Linearzylinder
- Begrenzte Drehmoment-Auswahl
- Weniger Hersteller (hauptsächlich Jefa, Lewmar)
- Interne Dichtung anspruchsvoller

#### 3.5.2 Typische Kennwerte

| Modellklasse | Schaftdurchmesser | Max. Drehmoment | Drehwinkel | Einsatz |
|-------------|-------------------|-----------------|------------|---------|
| Klein | 30–50 mm | 200–500 Nm | ±35° | Segelboote 10–14 m |
| Mittel | 50–75 mm | 500–1.500 Nm | ±35° | Segelboote 14–20 m |
| Groß | 75–100 mm | 1.500–4.000 Nm | ±35° | Segelboote 18–25 m |
| Sehr groß | 100–140 mm | 4.000–10.000 Nm | ±40° | Yachten >25 m |

### 3.6 Balanced-Ram-Zylinder (Symmetrischer Zylinder)

#### 3.6.1 Funktionsprinzip

Beim Balanced Ram durchläuft die Kolbenstange den Zylinder auf beiden Seiten. Dadurch ist die wirksame Kolbenfläche auf beiden Seiten identisch.

```
←— Kolbenstange —— [Kolben] —— Kolbenstange —→
     Port A ←→ Fluid ←→ Port B
```

**Vorteile gegenüber Standard-Zylinder:**
- Identisches Verhalten in beide Ruderrichtungen
- Gleiche Geschwindigkeit und Kraft nach Backbord und Steuerbord
- Kein Volumenstrom-Unterschied → gleichmäßiges Steuergefühl
- Besser für Feedback-Systeme geeignet

**Nachteile:**
- Größer, schwerer, teurer
- Zwei Stangendichtungen statt einer
- Kolbenstange ragt beidseitig heraus → mehr Platzbedarf

#### 3.6.2 Einsatz

- **Standard bei hochwertigen Segelyacht-Hydrauliksystemen** (Jefa, Lewmar, Lecomble & Schmitt)
- Überall dort, wo symmetrisches Steuerverhalten wichtig ist
- Performance-Cruiser und Regattayachten

### 3.7 Inline-Zylinder (Motorboot-Standard)

#### 3.7.1 Funktionsprinzip

Der Inline-Zylinder (auch: Frontzylinder, Tie-Bar-Zylinder) wird bei Motorbooten direkt an der Lenkmechanik des Außenborders oder Innenborders (Z-Antrieb) montiert:

```
Helmpumpe → Druckleitungen → Inline-Zylinder → Tie-Bar → Motorlenkmechanik
```

**Typische Montage:**
- Am Motorträger (Transom) befestigt
- Tie-Bar verbindet Zylinder mit Lenkhebel des Motors
- Bei Multi-Engine: Tie-Bar verbindet alle Motoren mechanisch

#### 3.7.2 Kennwerte

| Typ | Kolben-Ø | Hub | Max. Druck | Motorleistung |
|-----|----------|-----|-----------|--------------|
| SeaStar HC5345 | 40 mm | 230 mm | 70 bar | bis 150 PS |
| SeaStar HC5348 | 50 mm | 254 mm | 70 bar | bis 350 PS |
| SeaStar HC5370 | 60 mm | 266 mm | 70 bar | bis 600 PS |
| SeaStar HC6750 | 70 mm | 280 mm | 100 bar | bis 900 PS |
| Vetus HTP4210 | 50 mm | 240 mm | 70 bar | bis 350 PS |
| Vetus HTP4220 | 60 mm | 260 mm | 100 bar | bis 600 PS |

---

## 4. Produktlinien und Hersteller

### 4.1 Jefa Steering (Dänemark)

**Unternehmen:** Jefa Marine A/S, Bogense, Dänemark. Gegründet 1979. Marktführer für hochwertige Segelyacht-Steuerungen.

**Philosophie:** Präzision, Langlebigkeit, minimaler Verschleiß. Alle Systeme mit Feedback-Option. Exzellenter After-Sales-Support.

#### 4.1.1 Jefa Hydraulik-Helmpumpen

| Modell | Verdrängung | Max. Druck | Typ | Anschlüsse | Einsatz |
|--------|-------------|-----------|-----|-----------|---------|
| Jefa HP-10 | 10 cm³/U | 70 bar | Drehschieber, Feedback | 3/8" ORB | Segelboote 10–13 m |
| Jefa HP-14 | 14 cm³/U | 70 bar | Drehschieber, Feedback | 3/8" ORB | Segelboote 12–16 m |
| Jefa HP-18 | 18 cm³/U | 70 bar | Drehschieber, Feedback | 1/2" ORB | Segelboote 14–18 m |
| Jefa HP-24 | 24 cm³/U | 70 bar | Drehschieber, Feedback | 1/2" ORB | Segelboote 16–22 m |
| Jefa HP-30 | 30 cm³/U | 70 bar | Axialkolben, Feedback | 1/2" ORB | Segelboote 20–28 m |
| Jefa HP-10NF | 10 cm³/U | 70 bar | Drehschieber, Non-Feedback | 3/8" ORB | Motorboote 8–12 m |
| Jefa HP-18NF | 18 cm³/U | 70 bar | Drehschieber, Non-Feedback | 1/2" ORB | Motorboote 12–18 m |

**Besonderheiten Jefa Helmpumpen:**
- Gehäuse: Bronze CuSn7Zn (nicht Messing!) — höchste Korrosionsbeständigkeit
- Flügelzellen: Kohlefaser-verstärkter PTFE → minimaler Verschleiß
- Einstellbares Feedback-Ventil (stufenlos) → individuelles Steuergefühl
- Integrierter Ausgleichsbehälter (kein externer Tank nötig bei kleinen Systemen)
- Lieferung mit Montageflansch für Jefa- und Edson-Pedestals (Adapter für Lewmar verfügbar)
- Dichtungssatz als Ersatzteil: Jefa SP-HP-xx (xx = Modellnummer)

#### 4.1.2 Jefa Hydraulikzylinder

| Modell | Kolben-Ø | Hub | Typ | Max. Drehmoment* | Schaft-Ø |
|--------|----------|-----|-----|-----------------|----------|
| Jefa HC-40 | 40 mm | 180 mm | Balanced Ram | 250 Nm | 30–40 mm |
| Jefa HC-50 | 50 mm | 200 mm | Balanced Ram | 500 Nm | 35–50 mm |
| Jefa HC-60 | 60 mm | 230 mm | Balanced Ram | 900 Nm | 40–60 mm |
| Jefa HC-70 | 70 mm | 260 mm | Balanced Ram | 1.400 Nm | 50–70 mm |
| Jefa HC-80 | 80 mm | 280 mm | Balanced Ram | 2.000 Nm | 60–80 mm |
| Jefa HC-100 | 100 mm | 320 mm | Balanced Ram | 3.500 Nm | 70–100 mm |
| Jefa HC-120 | 120 mm | 350 mm | Balanced Ram | 5.500 Nm | 80–120 mm |

*Max. Drehmoment bei Tillerarm 200 mm und 70 bar (Confidence: measured — Jefa TDS)

**Besonderheiten Jefa Zylinder:**
- Alle Zylinder: Edelstahl-Kolbenstange (AISI 316L), geschliffen und hartverchromt
- Zylinderrohr: Nahtloses Präzisionsstahlrohr, innen gehomt
- Dichtungen: Parker/Trelleborg Originaldichtungen, PU/PTFE
- Anschlüsse: ORB (O-Ring Boss) — leckagesicherste Verbindung
- Tillerarm: Geschmiedeter Edelstahl 316L, passend für Jefa-Ruderanlagen
- Montage: Universalaufnahme oder kundenspezifisch

#### 4.1.3 Jefa Rotary-Vane-Aktuatoren

| Modell | Schaft-Ø | Drehmoment | Winkel | Einsatz |
|--------|----------|-----------|--------|---------|
| Jefa RV-35 | 35–50 mm | 350 Nm | ±35° | Segelboote 10–13 m |
| Jefa RV-50 | 50–65 mm | 800 Nm | ±35° | Segelboote 13–17 m |
| Jefa RV-65 | 65–80 mm | 1.500 Nm | ±35° | Segelboote 16–22 m |
| Jefa RV-80 | 80–100 mm | 3.000 Nm | ±40° | Segelboote 20–28 m |
| Jefa RV-100 | 100–130 mm | 6.000 Nm | ±40° | Yachten 26–35 m |

**Vorteile Jefa Rotary-Vane:**
- Direktmontage auf Ruderkoker — kein Tillerarm nötig
- Extrem kompakt → ideal bei engen Achterpiek-Verhältnissen
- Integrierte Endanschläge (mechanisch + hydraulisch)
- Optional: Integrierter Ruderlagengeber

#### 4.1.4 Jefa Zubehör und Ersatzteile

| Artikel | Teilenummer | Beschreibung |
|---------|------------|--------------|
| Dichtungssatz HP-10 | Jefa SP-HP-10 | Komplett-Dichtungssatz Helmpumpe HP-10 |
| Dichtungssatz HP-18 | Jefa SP-HP-18 | Komplett-Dichtungssatz Helmpumpe HP-18 |
| Dichtungssatz HC-60 | Jefa SP-HC-60 | Komplett-Dichtungssatz Zylinder HC-60 |
| Hydraulikschlauch 3/8" | Jefa HL-10-xxx | Schlauch 10 mm ID, xxx = Länge in cm |
| Hydraulikschlauch 1/2" | Jefa HL-13-xxx | Schlauch 13 mm ID, xxx = Länge in cm |
| Feedback-Ventil (Austausch) | Jefa FV-01 | Einstellbares Nadelventil |
| Entlüftungsschraube | Jefa BV-01 | Messing vernickelt, 1/8" NPT |
| Hydraulikfluid (1L) | Jefa HF-01 | ATF Dexron III, empfohlen |

### 4.2 Lecomble & Schmitt (Frankreich)

**Unternehmen:** Lecomble & Schmitt S.A.S., Boulogne-sur-Mer, Frankreich. Gegründet 1868. Traditionsreichster Hersteller, Marktführer in Frankreich, stark in Mittelmeer-Region.

**Philosophie:** Robuste Industriequalität, breites Sortiment von 6 m bis 40 m+, eigenes Hydraulikfluid, guter OEM-Support.

#### 4.2.1 Lecomble & Schmitt Helmpumpen

| Modell | Verdrängung | Max. Druck | Typ | Anschlüsse | Einsatz |
|--------|-------------|-----------|-----|-----------|---------|
| L&S HB 5710 | 7 cm³/U | 50 bar | Drehschieber, NF | 1/4" BSP | Motorboote 6–9 m |
| L&S HB 5714 | 14 cm³/U | 50 bar | Drehschieber, NF | 3/8" BSP | Motorboote 9–14 m |
| L&S HB 5718 | 18 cm³/U | 70 bar | Drehschieber, NF | 3/8" BSP | Motorboote 12–18 m |
| L&S HTP 30 | 10 cm³/U | 70 bar | Drehschieber, FB | 3/8" BSP | Segelboote 10–14 m |
| L&S HTP 42 | 14 cm³/U | 70 bar | Drehschieber, FB | 3/8" BSP | Segelboote 12–16 m |
| L&S HTP 53 | 18 cm³/U | 70 bar | Drehschieber, FB | 1/2" BSP | Segelboote 14–20 m |
| L&S HTP 60 | 22 cm³/U | 70 bar | Drehschieber, FB | 1/2" BSP | Segelboote 18–24 m |
| L&S HTP 70 | 28 cm³/U | 70 bar | Axialkolben, FB | 1/2" BSP | Segelboote 22–30 m |
| L&S HTP 80 | 35 cm³/U | 100 bar | Axialkolben, FB | 3/4" BSP | Yachten 28–40 m |

(NF = Non-Feedback, FB = Feedback)

**Besonderheiten L&S Helmpumpen:**
- Gehäuse: Aluminium-Druckguss (eloxiert) oder Bronze (HTP-Serie)
- BSP-Anschlüsse (British Standard Pipe) — europäischer Standard
- Integrierte thermische Überdrucksicherung bei allen Modellen
- HTP-Serie: Einstellbares Feedback (Stellschraube seitlich)
- Bypass-Schaltung für Autopilot-Integration vorgerüstet
- Kompatibel mit Lecomble-eigenem Hydraulikfluid LHM+ (auf Mineralölbasis)

#### 4.2.2 Lecomble & Schmitt Steuerzylinder

| Modell | Kolben-Ø | Hub | Typ | Max. Kraft | Einsatz |
|--------|----------|-----|-----|-----------|---------|
| L&S V120 | 40 mm | 165 mm | Single Ram | 6.280 N | Segelboote 9–12 m |
| L&S V150 | 50 mm | 185 mm | Balanced Ram | 13.750 N | Segelboote 11–15 m |
| L&S V200 | 60 mm | 210 mm | Balanced Ram | 19.790 N | Segelboote 13–18 m |
| L&S V250 | 70 mm | 240 mm | Balanced Ram | 26.950 N | Segelboote 16–22 m |
| L&S V300 | 80 mm | 270 mm | Balanced Ram | 35.190 N | Segelboote 20–28 m |
| L&S V350 | 90 mm | 300 mm | Balanced Ram | 44.530 N | Yachten 25–35 m |
| L&S V400 | 100 mm | 340 mm | Balanced Ram | 54.980 N | Yachten 30–40 m |
| L&S MC40 | 40 mm | 200 mm | Inline Cyl | 6.280 N | Motorboote 6–10 m |
| L&S MC60 | 60 mm | 240 mm | Inline Cyl | 19.790 N | Motorboote 10–16 m |
| L&S MC80 | 80 mm | 280 mm | Inline Cyl | 35.190 N | Motorboote 14–22 m |

(Max. Kraft bei 50 bar Systemdruck — Confidence: estimated — unverifiziert)

> ⚠️ **ZU PRÜFEN (Audit):** Der angegebene Bezugsdruck "50 bar" widerspricht den Tabellenwerten. V150–V400 und MC60/MC80 entsprechen der Zylinderkraft bei **70 bar** (z.B. V200, 60 mm → 19.790 N = 28,27 cm² × 70 bar; bei 50 bar wären es nur 14.137 N — siehe ANHANG B.1), während nur V120/MC40 (6.280 N = 12,57 cm² × 50 bar) tatsächlich 50-bar-Werte sind. Bezugsdruck oder Kraftwerte herstellerseitig verifizieren; Confidence deshalb von "measured" auf "estimated" zurückgestuft.

#### 4.2.3 Lecomble & Schmitt Power-Packs

| Modell | Spannung | Leistung | Fördermenge | Max. Druck | Einsatz |
|--------|---------|---------|-------------|-----------|---------|
| L&S PP 12/1 | 12V DC | 0,5 kW | 2,5 L/min | 70 bar | Autopilot-Antrieb klein |
| L&S PP 12/2 | 12V DC | 1,0 kW | 4,5 L/min | 100 bar | Power-Assist 12–18 m |
| L&S PP 24/2 | 24V DC | 1,0 kW | 4,5 L/min | 100 bar | Power-Assist 14–22 m |
| L&S PP 24/4 | 24V DC | 2,5 kW | 8,0 L/min | 140 bar | Full Power 18–30 m |
| L&S PP 24/8 | 24V DC | 5,0 kW | 14,0 L/min | 200 bar | Full Power 25–40 m |

#### 4.2.4 Lecomble & Schmitt Zubehör

| Artikel | Teilenummer | Beschreibung |
|---------|------------|--------------|
| Hydraulikfluid LHM+ (1L) | L&S 80.600 | Mineralöl HLP 15, empfohlen |
| Dichtungssatz V200 | L&S SK-V200 | Komplett-Dichtungssatz |
| Schlauchsatz 5m (3/8") | L&S HS-10-500 | 2× Schlauch + 4× Fitting |
| Autopilot-Solenoidventil | L&S SV-12 | 12V Solenoid für AP-Integration |
| Entlüftungsset | L&S BK-01 | Entlüftungsschlauch + Behälter |
| Tillerarm (standard) | L&S TA-xxx | xxx = Schaftdurchmesser in mm |

### 4.3 Kobelt Manufacturing (Kanada)

**Unternehmen:** Kobelt Manufacturing Co. Ltd., Surrey, British Columbia, Kanada. Gegründet 1962. Spezialist für Steuer- und Antriebssteuerungen schwerer Motor- und Arbeitssyachten.

**Philosophie:** Industriequalität für den maritimen Einsatz. Erprobte, robuste Konstruktionen. Stark im nordamerikanischen und skandinavischen Markt.

#### 4.3.1 Kobelt Helmpumpen

| Modell | Verdrängung | Max. Druck | Typ | Anschlüsse | Einsatz |
|--------|-------------|-----------|-----|-----------|---------|
| Kobelt 7004 | 16 cm³/U | 70 bar | Radialkolben, NF | SAE -6 | Motorboote 10–16 m |
| Kobelt 7012 | 24 cm³/U | 100 bar | Radialkolben, NF | SAE -8 | Motorboote 14–22 m |
| Kobelt 7014 | 32 cm³/U | 100 bar | Radialkolben, NF | SAE -8 | Motorboote 18–28 m |
| Kobelt 7020 | 40 cm³/U | 140 bar | Radialkolben, NF | SAE -10 | Yachten 25–40 m |
| Kobelt 7050 | 16 cm³/U | 70 bar | Radialkolben, FB | SAE -6 | Segelboote 12–18 m |
| Kobelt 7052 | 24 cm³/U | 100 bar | Radialkolben, FB | SAE -8 | Segelboote 16–25 m |

(NF = Non-Feedback, FB = Feedback)

**Besonderheiten Kobelt:**
- Gehäuse: Gusseisen mit Korrosionsschutzbeschichtung (oder Edelstahl auf Anfrage)
- Radialkolben-Design → höherer Wirkungsgrad als Drehschieber bei hohen Drücken
- Extrem langlebig: Überholungsintervall 10.000+ Betriebsstunden
- Eigener Tillerarm-Adapter für diverse Ruderanlagen
- Kombination mit Kobelt-Schaltungs- und Gashebelsteuerung (Einhandsteuerung)

#### 4.3.2 Kobelt Steuerzylinder

| Modell | Kolben-Ø | Hub | Typ | Max. Kraft | Einsatz |
|--------|----------|-----|-----|-----------|---------|
| Kobelt 2012 | 50 mm | 220 mm | Double-Acting | 13.750 N | Boote 10–16 m |
| Kobelt 2014 | 65 mm | 260 mm | Double-Acting | 23.240 N | Boote 14–22 m |
| Kobelt 2016 | 80 mm | 300 mm | Double-Acting | 35.190 N | Boote 18–28 m |
| Kobelt 2020 | 100 mm | 350 mm | Double-Acting | 54.980 N | Yachten 25–40 m |
| Kobelt 2024 | 120 mm | 400 mm | Double-Acting | 79.170 N | Yachten 35–50 m |
| Kobelt 2030 | 140 mm | 450 mm | Double-Acting | 107.760 N | Yachten >45 m |

(Max. Kraft bei 70 bar — Confidence: measured)

#### 4.3.3 Kobelt Power-Packs und Elektrohydraulische Einheiten

| Modell | Spannung | Leistung | Fördermenge | Max. Druck |
|--------|---------|---------|-------------|-----------|
| Kobelt 6512 | 12V DC | 1,5 kW | 5,0 L/min | 100 bar |
| Kobelt 6524 | 24V DC | 2,5 kW | 8,0 L/min | 140 bar |
| Kobelt 6524-HD | 24V DC | 4,0 kW | 12,0 L/min | 200 bar |
| Kobelt 6548 | 48V DC | 6,0 kW | 18,0 L/min | 200 bar |

### 4.4 Teleflex SeaStar (Dometic Marine)

**Unternehmen:** SeaStar Solutions (seit 2017 Teil von Dometic Group). Ursprünglich Teleflex Marine. Weltmarktführer für Motorboot-Hydrauliksteuerungen. Hauptsitz: Richmond, British Columbia, Kanada.

**Philosophie:** Breite Verfügbarkeit, einfache Installation, Kit-Systeme. Dominiert den Motorboot-Aftermarket weltweit.

#### 4.4.1 SeaStar Helmpumpen

| Modell | Verdrängung | Max. Druck | Typ | Anschlüsse | Einsatz |
|--------|-------------|-----------|-----|-----------|---------|
| SeaStar HH5271-3 | 10 cm³/U | 70 bar | Drehschieber, NF | SAE -6 | Motorboote bis 150 PS |
| SeaStar HH5741-3 | 14 cm³/U | 70 bar | Drehschieber, NF | SAE -6 | Motorboote bis 300 PS |
| SeaStar HH5770-3 | 18 cm³/U | 70 bar | Drehschieber, NF | SAE -8 | Motorboote bis 600 PS |
| SeaStar HH6541-3 | 14 cm³/U | 100 bar | Drehschieber, NF | SAE -8 | Motorboote bis 600 PS (BayStar+) |
| SeaStar HH6570-3 | 20 cm³/U | 100 bar | Drehschieber, NF | SAE -8 | Motorboote bis 900 PS |
| SeaStar Pro HH6170-3 | 22 cm³/U | 100 bar | Drehschieber, NF | SAE -8 | Performance-Motorboote |

**Besonderheiten SeaStar:**
- Helmpumpen-Gehäuse: Alu-Druckguss, hartanodisiert
- Kompaktes Design — passt in Standard-NEMA-Dashpanel-Ausschnitt
- Proprietäre Anschlüsse bei älteren Modellen (SeaStar-spezifisch → Adapter nötig bei Fremdkomponenten)
- Eingebautes Überdruckventil
- Kompatibel mit Dometic Optimus EPS (Electronic Power Steering)

#### 4.4.2 SeaStar Steuerzylinder

| Modell | Kolben-Ø | Hub | Max. Druck | Einsatz |
|--------|----------|-----|-----------|---------|
| SeaStar HC5345-3 | 40 mm | 230 mm | 70 bar | Einzelmotor bis 150 PS |
| SeaStar HC5348-3 | 50 mm | 254 mm | 70 bar | Einzelmotor bis 350 PS |
| SeaStar HC5370-3 | 60 mm | 266 mm | 70 bar | Einzel-/Doppelmotor bis 600 PS |
| SeaStar HC5375-3 | 65 mm | 280 mm | 100 bar | Doppelmotor bis 900 PS |
| SeaStar HC6750-3 | 70 mm | 280 mm | 100 bar | Triple/Quad bis 1.200 PS |
| SeaStar HC5380-3 | 50 mm | 254 mm | 70 bar | Jackplate-Montage |

> ⚠️ **ZU PRÜFEN (Audit):** Zulässige Motorleistung für **HC6750** widersprüchlich angegeben: Abschnitt 3.7.2 und Kit HK7500A-3 (Abschnitt 4.4.3) nennen "bis 900 PS", die Zeile HC6750-3 oben dagegen "Triple/Quad bis 1.200 PS". Herstellerangabe verifizieren.

**Besonderheiten SeaStar Zylinder:**
- Inline-Bauform mit Tie-Bar-Anschluss
- Integrierte Purge-Ventile (Entlüftung)
- Edelstahl-Kolbenstange (poliert)
- Einfacher Tausch: Plug-and-Play mit SeaStar-Helmpumpen
- Frontmontage am Motortransom

#### 4.4.3 SeaStar Komplettsysteme (Kits)

| Kit | Komponenten | Motorleistung | Preis (ca.) |
|-----|-----------|--------------|------------|
| SeaStar HK4200A-3 | HH5271 + HC5345 + 2×6m Schlauch + Fluid | bis 150 PS | 650–850 EUR |
| SeaStar HK4500A-3 | HH5741 + HC5348 + 2×6m Schlauch + Fluid | bis 300 PS | 850–1.100 EUR |
| SeaStar HK4900A-3 | HH5770 + HC5370 + 2×8m Schlauch + Fluid | bis 600 PS | 1.200–1.500 EUR |
| SeaStar Pro HK7500A-3 | HH6570 + HC6750 + 2×8m Schlauch + Fluid | bis 900 PS | 1.800–2.400 EUR |

#### 4.4.4 SeaStar Zubehör

| Artikel | Teilenummer | Beschreibung |
|---------|------------|--------------|
| Hydraulikfluid (946 ml) | HA5430 | SeaStar/Dometic proprietär, ATF-basiert |
| Entlüftungskit | HA5438 | Schlauch, Behälter, Anleitung |
| Schlauchsatz 6m (paar) | HO5110 | 3/8" ID, SAE -6 Fittings |
| Schlauchsatz 9m (paar) | HO5115 | 3/8" ID, SAE -6 Fittings |
| Schlauchsatz 12m (paar) | HO5120 | 3/8" ID, SAE -6 Fittings |
| Autopilot-Anschlusskit | AP1233 | T-Stücke, Schläuche, Ventile für AP |
| Zweites Steuerrad-Kit | HA5437 | Verbindungskit für 2. Steuerplatz |
| Tie-Bar (Doppelmotor) | HO6002 | Verbindungsstange für 2 Motoren |
| Tie-Bar (Triple-Motor) | HO6003 | Verbindungsstange für 3 Motoren |

### 4.5 Hynautic (USA)

**Unternehmen:** Hynautic Inc., USA (seit 2015 Teil von Teleflex/Dometic). Gegründet 1959 als einer der ersten Marine-Hydraulik-Spezialisten.

**Philosophie:** Hochwertige Systeme für mittlere bis große Motorboote und Trawler. Bekannt für Langlebigkeit und Zuverlässigkeit.

**Hinweis:** Hynautic-Modelle werden heute als „Dometic Hynautic" geführt und teilweise durch SeaStar Pro ersetzt. Viele ältere Systeme sind noch im Einsatz.

#### 4.5.1 Hynautic Helmpumpen (Legacy + aktuell)

| Modell | Verdrängung | Max. Druck | Status | Einsatz |
|--------|-------------|-----------|--------|---------|
| Hynautic H-50 | 14 cm³/U | 70 bar | Legacy (Ersatzteile verfügbar) | Motorboote 10–16 m |
| Hynautic H-60 | 20 cm³/U | 100 bar | Legacy (Ersatzteile verfügbar) | Motorboote 14–22 m |
| Hynautic H-70 | 28 cm³/U | 100 bar | Legacy (Ersatzteile verfügbar) | Motorboote 18–30 m |
| Dometic/Hynautic HH-80 | 32 cm³/U | 140 bar | Aktuell | Yachten 22–35 m |
| Dometic/Hynautic HH-90 | 40 cm³/U | 140 bar | Aktuell | Yachten 30–45 m |

#### 4.5.2 Hynautic Steuerzylinder

| Modell | Kolben-Ø | Hub | Typ | Einsatz |
|--------|----------|-----|-----|---------|
| Hynautic CR-01 | 55 mm | 240 mm | Inline | Motorboote 10–16 m |
| Hynautic CR-02 | 70 mm | 280 mm | Inline | Motorboote 14–22 m |
| Hynautic CR-03 | 85 mm | 320 mm | Double-Acting | Motorboote 18–30 m |
| Hynautic CR-04 | 100 mm | 360 mm | Double-Acting | Yachten 25–40 m |

**Hynautic Fluid:**
- Hynautic Fluid HTF-2 (proprietär, Mineralölbasis, ISO VG 15)
- NICHT mischbar mit SeaStar-Fluid oder ATF!
- Bei Systemkonversion (Hynautic → SeaStar): Kompletter Fluidtausch erforderlich!

### 4.6 Vetus (Niederlande)

**Unternehmen:** Vetus B.V., Schiedam, Niederlande. Gegründet 1951. Breit aufgestellter Marine-Komponentenhersteller. Hydrauliksteuerungen als Teil eines umfassenden Produktportfolios.

**Philosophie:** Gutes Preis-Leistungs-Verhältnis, breite Produktpalette, guter europäischer Vertrieb.

#### 4.6.1 Vetus Helmpumpen

| Modell | Verdrängung | Max. Druck | Typ | Anschlüsse | Einsatz |
|--------|-------------|-----------|-----|-----------|---------|
| Vetus HTP2010 | 10 cm³/U | 50 bar | Drehschieber, NF | 3/8" BSP | Motorboote 6–10 m |
| Vetus HTP3010 | 14 cm³/U | 70 bar | Drehschieber, NF | 3/8" BSP | Motorboote 9–14 m |
| Vetus HTP4010 | 18 cm³/U | 70 bar | Drehschieber, NF | 1/2" BSP | Motorboote 12–18 m |
| Vetus HTP3010F | 14 cm³/U | 70 bar | Drehschieber, FB | 3/8" BSP | Segelboote 10–15 m |
| Vetus HTP4010F | 18 cm³/U | 70 bar | Drehschieber, FB | 1/2" BSP | Segelboote 13–20 m |
| Vetus HTP5010F | 24 cm³/U | 70 bar | Axialkolben, FB | 1/2" BSP | Segelboote 18–25 m |

#### 4.6.2 Vetus Steuerzylinder

| Modell | Kolben-Ø | Hub | Typ | Max. Kraft | Einsatz |
|--------|----------|-----|-----|-----------|---------|
| Vetus HTC4210 | 42 mm | 200 mm | Balanced Ram | 9.700 N | Segelboote 9–13 m |
| Vetus HTC5210 | 52 mm | 220 mm | Balanced Ram | 14.870 N | Segelboote 12–17 m |
| Vetus HTC6210 | 62 mm | 250 mm | Balanced Ram | 21.140 N | Segelboote 15–22 m |
| Vetus HTC8210 | 82 mm | 300 mm | Balanced Ram | 36.950 N | Segelboote 20–28 m |
| Vetus HTP4210I | 42 mm | 220 mm | Inline Cyl | 9.700 N | Motorboote 6–10 m |
| Vetus HTP6210I | 62 mm | 260 mm | Inline Cyl | 21.140 N | Motorboote 10–16 m |

(Max. Kraft bei 70 bar — Confidence: measured)

#### 4.6.3 Vetus Zubehör

| Artikel | Teilenummer | Beschreibung |
|---------|------------|--------------|
| Hydraulikfluid (1L) | Vetus HF115 | Mineralöl ISO VG 15 |
| Schlauchmeterware 3/8" | Vetus?"?"HH10 | Pro Meter, inkl. Fitting-Konfig |
| Entlüftungsset | Vetus?"?"BP01 | Komplett-Entlüftungsset |
| Autopilot-T-Stück | Vetus HTAP01 | Für Autopilot-Zylinder-Anschluss |
| Reservoir 0,5L | Vetus HT05 | Externer Ausgleichsbehälter |

### 4.7 Schlauchspezifikationen (herstellerübergreifend)

| Spezifikation | Wert | Norm |
|--------------|------|------|
| Innendurchmesser Standard | 8 mm (5/16"), 10 mm (3/8"), 12 mm (1/2") | SAE 100R7/R8 |
| Druckstufe | 70 bar (R7), 140 bar (R8), 210 bar (2-Drahtgeflecht) | SAE J517 |
| Berstdruck | 4× Arbeitsdruck (Minimum) | ISO 10592 |
| Biegeradius | Min. 4× Außendurchmesser | Herstellerangabe |
| Innenseele | Synthetischer Gummi (CR oder NBR) | — |
| Verstärkung | Polyester-Geflecht (R7), Stahldrahtgeflecht (R8) | — |
| Außenmantel | Synthetischer Gummi, UV-beständig | — |
| Temperaturbereich | –40°C bis +100°C (Schlauch), –30°C bis +80°C (Fluid) | — |
| Lebensdauer | 8–12 Jahre (Confidence: estimated) | ISO 10592: max. 10 Jahre |
| Fittingtypen | ORB, JIC 37°, BSP, NPT | Herstellerabhängig |

**Warnung:** Unterschiedliche Hersteller verwenden unterschiedliche Fitting-Standards! Beim Mischen von Komponenten immer Kompatibilität prüfen:
- Jefa: ORB (O-Ring Boss)
- Lecomble & Schmitt: BSP (British Standard Pipe)
- SeaStar: SAE/JIC oder proprietär
- Kobelt: SAE/JIC
- Vetus: BSP

---

## 5. Autopilot-Integration

### 5.1 Grundprinzip der hydraulischen Autopilot-Integration

Der Autopilot greift in das hydraulische Steuerungssystem ein, indem er einen eigenen Hydraulikantrieb (Pumpe + Ventil oder Solenoidventil) parallel zum manuellen System schaltet:

```
                    ┌──── Helmpumpe (manuell) ────┐
                    │                               │
Steuerrad ──────────┤                               ├──── Steuerzylinder ──── Ruder
                    │                               │
                    └──── Autopilot-Antrieb ────────┘
                          (Solenoid/Pumpe)
                               ↑
                         Autopilot-Computer
                               ↑
                    Kompass / GPS / Windsensor
```

### 5.2 Solenoidventil-Integration

#### 5.2.1 Funktionsprinzip

Zwei Solenoidventile (Backbord/Steuerbord) werden in die Hydraulikleitungen zwischen Helmpumpe und Zylinder eingebunden. Der Autopilot öffnet und schließt diese Ventile, um Fluid in den Zylinder zu drücken:

**Variante A — Bypass-Solenoid (bei manuellen Systemen):**
```
Helmpumpe → T-Stück → Solenoid BB → Zylinder Port A
                    → Solenoid SB → Zylinder Port B
                    → Bypass-Leitung (wenn AP inaktiv)
```

**Variante B — Dedicated AP Pump (separater Hydraulikantrieb):**
```
AP-Pumpe (reversierend) → Solenoidventil → T-Stück → Zylinder
```

#### 5.2.2 Solenoidventil-Typen

| Typ | Funktion | Schaltzeit | Leistung | Einsatz |
|-----|---------|-----------|---------|---------|
| 2/2-Wegeventil (NC) | Auf/Zu | 20–50 ms | 8–15 W | Standard-AP-Integration |
| 3/2-Wegeventil | Umschaltung | 20–50 ms | 10–20 W | Bypass-Schaltung |
| 4/3-Wegeventil | Proportional | 10–30 ms | 15–30 W | Proportional-AP |
| Proportionalventil | Stufenlos | 5–15 ms | 20–50 W | High-End-AP |

### 5.3 Hydraulische Autopilot-Antriebe

#### 5.3.1 Raymarine

| Modell | Typ | Max. Zylinder | Betriebsdruck | Spannung | Einsatz |
|--------|-----|-------------|--------------|---------|---------|
| Raymarine Type 1 | Reversier-Pumpe | 80 cm³ | 70 bar | 12V | Segelboote 9–14 m |
| Raymarine Type 2 | Reversier-Pumpe | 175 cm³ | 70 bar | 12V | Segelboote 12–18 m |
| Raymarine Type 3 | Reversier-Pumpe | 350 cm³ | 100 bar | 12/24V | Segelboote 16–25 m |
| Raymarine ACU-100 | Steuereinheit | n/a | n/a | 12V | Für Type 1/2 |
| Raymarine ACU-150 | Steuereinheit | n/a | n/a | 12V | Für Type 1/2/3 |
| Raymarine ACU-200 | Steuereinheit | n/a | n/a | 12/24V | Für Type 2/3 |
| Raymarine ACU-400 | Steuereinheit | n/a | n/a | 24V | Für hydraulische Yachten >25 m |

**Raymarine Evolution Autopilot-System:**
- EV-1 Sensor (9-Achsen-IMU + Fluxgate)
- ACU (Actuator Control Unit) steuert Hydraulikpumpe
- Integration über SeaTalkNG / NMEA 2000
- Automatische Seegangsanpassung (AI-basiert)

#### 5.3.2 B&G (Navico/Navionics)

| Modell | Typ | Max. Zylinder | Betriebsdruck | Spannung | Einsatz |
|--------|-----|-------------|--------------|---------|---------|
| B&G Hydraulic Pack HP1 | Reversier-Pumpe | 80 cm³ | 70 bar | 12V | Segelboote 9–14 m |
| B&G Hydraulic Pack HP2 | Reversier-Pumpe | 175 cm³ | 70 bar | 12V | Segelboote 12–18 m |
| B&G Hydraulic Pack HP3 | Reversier-Pumpe | 350 cm³ | 100 bar | 12/24V | Segelboote 16–28 m |
| B&G H5000 Hydraulic | Proportional | 500+ cm³ | 140 bar | 24V | Performance-Segler >18 m |

**B&G Besonderheiten (Segelspezifisch):**
- Windfahnen-Modus (Wind Vane Mode) für Segeln am Wind
- Performance-Modus mit Polardiagramm-Integration
- Sehr schnelle Ruderantwort für Regatta-Einsatz
- Integration mit B&G Triton/Vulcan/Zeus MFD

#### 5.3.3 Simrad (Navico)

| Modell | Typ | Max. Zylinder | Betriebsdruck | Spannung | Einsatz |
|--------|-----|-------------|--------------|---------|---------|
| Simrad SDP10 | Solenoidventil-Steuerung | 350 cm³ | 100 bar | 12/24V | Motorboote 10–18 m |
| Simrad SDP20 | Reversier-Pumpe | 175 cm³ | 70 bar | 12V | Motorboote 8–14 m |
| Simrad SDP30 | Reversier-Pumpe | 500 cm³ | 140 bar | 24V | Motorboote 14–25 m |
| Simrad SD80 | Solenoidventil-Steuerung | 1.000+ cm³ | 200 bar | 24V | Yachten >25 m |

**Simrad Besonderheiten (Motorboot-fokussiert):**
- Dynamische Autopilotanpassung an Geschwindigkeit
- Joystick-Docking-Modus (mit IPS/Zeus3/Stern Drive)
- NMEA 2000 / Simnet-Integration
- Kompatibel mit Simrad NSS/NSO/NSX-MFDs

### 5.4 Autopilot-Anschlussschemen

#### 5.4.1 Standard-Anschluss (manuelles System + AP-Pumpe)

```
                           ┌─────────────────────┐
  Helmpumpe ──── Port A ───┤ T-Stück mit         ├──── Zylinder Port A
                           │ Rückschlagventil     │
                           └──────────┬──────────┘
                                      │
                              AP-Pumpe Port A
                              AP-Pumpe Port B
                                      │
                           ┌──────────┴──────────┐
  Helmpumpe ──── Port B ───┤ T-Stück mit         ├──── Zylinder Port B
                           │ Rückschlagventil     │
                           └─────────────────────┘
```

**Wichtige Regeln:**
1. Rückschlagventile müssen verhindern, dass der AP die Helmpumpe antreibt (und umgekehrt)
2. AP-Pumpe muss bei manueller Steuerung drucklos sein (Bypass oder Freilauf)
3. Leitungslänge AP→Zylinder so kurz wie möglich (Ansprechverhalten!)
4. Entlüftung am höchsten Punkt des Systems

#### 5.4.2 Anschluss mit Solenoidventil-Block

```
Helmpumpe ──→ Ventilblock ──→ Zylinder
                  ↑
            AP-Solenoidventile (2× oder 4×)
                  ↑
            AP-Computer (Steuersignal)
                  ↑
            Reservoir / Power-Pack
```

**Ventilblock-Funktion:**
- Manueller Betrieb: Solenoids geschlossen → Fluid fließt direkt Pumpe→Zylinder
- AP-Betrieb: Solenoids öffnen/schließen → AP-Pumpe steuert Zylinder
- Umschaltung: Automatisch (AP ein/aus) oder manuell (Bypass-Ventil)

### 5.5 Ruderlagengeber (Rudder Feedback Unit)

Jeder Autopilot benötigt eine Ruderlagenrückmeldung:

| Typ | Genauigkeit | Lebensdauer | Preis (ca.) | Einsatz |
|-----|-----------|-------------|------------|---------|
| Potentiometrisch (Drehwinkelsensor) | ±1° | 5–10 Jahre | 80–200 EUR | Standard |
| Hall-Effekt (berührungslos) | ±0,5° | 15–25 Jahre | 150–400 EUR | Premium |
| LVDT (Linear Variable Differential Transformer) | ±0,2° | 20–30 Jahre | 300–800 EUR | Professional |
| Encoder (optisch/magnetisch) | ±0,1° | 15–25 Jahre | 200–500 EUR | Performance |

**Montage:**
- Am Ruderkoker (Drehwinkelsensor) — häufigste Variante
- Am Tillerarm (LVDT, Linear → Winkelumrechnung nötig)
- Am Steuerzylinder (Linearsensor → Winkelumrechnung nötig)

### 5.6 Kompatibilitätsmatrix Helmpumpe × Autopilot

| Helmpumpe | Raymarine | B&G | Simrad | Garmin GHP |
|-----------|-----------|-----|--------|-----------|
| Jefa HP-Serie (Feedback) | ✓ (Type 2/3) | ✓ (HP2/HP3) | ✓ (SDP20/30) | ✓ |
| Jefa HP-Serie (Non-FB) | ✓ (alle) | ✓ (alle) | ✓ (alle) | ✓ |
| L&S HTP-Serie (Feedback) | ✓ (Type 2/3) | ✓ (HP2/HP3) | ✓ (SDP20/30) | ✓ |
| L&S HB-Serie (Non-FB) | ✓ (alle) | ✓ (alle) | ✓ (alle) | ✓ |
| SeaStar HH-Serie | ✓ (alle) | ✓ (alle) | ✓ (alle) | ✓ |
| Kobelt 70xx (Feedback) | ✓ (Type 3) | ✓ (HP3) | ✓ (SDP30) | ✓* |
| Vetus HTP-Serie | ✓ (alle) | ✓ (alle) | ✓ (alle) | ✓ |

✓ = kompatibel, ✓* = Adapter erforderlich

**Wichtiger Hinweis:** Feedback-Systeme erfordern AP-Antriebe mit ausreichender Haltekraft, da das Ruder ohne AP-Haltedruck zurückschlägt. Non-Feedback-Systeme halten das Ruder passiv in Position → einfachere AP-Integration.

---

## 6. Installation

### 6.1 Schlauchverlegung (Hose Routing)

#### 6.1.1 Allgemeine Regeln

1. **Biegeradius:** Mindestens 4× Außendurchmesser des Schlauchs. Kein Knicken!
2. **Scheuerschutz:** Überall, wo Schläuche an Schott, Rahmen oder anderen Leitungen anliegen → Scheuerschutz-Manschette (Spiralband oder Gummischutz).
3. **Befestigung:** Alle 30–50 cm mit Schlauchschellen (nicht quetschend!). P-Klemmen aus Edelstahl oder Kunststoff empfohlen.
4. **Bewegungsfreiheit:** Am Zylinder mindestens 100 mm freie Schlauchlänge für Zylinderbewegung.
5. **Wärme:** Mindestens 200 mm Abstand von Abgasrohren, Motoren und heißen Oberflächen.
6. **UV-Schutz:** Schläuche im Freien mit UV-beständigem Außenmantel oder zusätzlichem Schutzschlauch.
7. **Drainagefähig:** Leitungen so verlegen, dass keine Luftblasen eingeschlossen werden (stetig steigend oder fallend, keine U-Bögen).
8. **Leitungslänge:** Beide Druckleitungen sollen gleich lang sein (±10 %) — sonst asymmetrisches Steuerverhalten.

#### 6.1.2 Maximale Leitungslängen

| Schlauch-ID | Max. Länge empfohlen | Max. Länge absolut |
|-------------|--------------------|--------------------|
| 8 mm (5/16") | 8 m | 12 m |
| 10 mm (3/8") | 12 m | 18 m |
| 12 mm (1/2") | 18 m | 25 m |
| 16 mm (5/8") | 25 m | 35 m |

(Confidence: documented — Herstellerempfehlungen Jefa, L&S, SeaStar)

**Bei Überschreitung der empfohlenen Länge:**
- Größeren Schlauch-ID wählen
- Druckverlust berechnen (siehe 2.7.2)
- Ggf. Power-Assist-Pumpe hinzufügen

### 6.2 Entlüftungsverfahren (Bleeding Procedure)

Luft im Hydrauliksystem ist der häufigste Fehler und die häufigste Ursache für schwammiges Lenkverhalten!

#### 6.2.1 Standard-Entlüftungsverfahren (manuelles System)

**Benötigtes Material:**
- Frisches Hydraulikfluid (korrekte Spezifikation!)
- Auffangbehälter
- Entlüftungsschlauch (transparent, passend für Entlüftungsventil)
- Ringschlüssel (Entlüftungsventile typisch 7 mm oder 8 mm)
- Lappen, Ölbindemittel

**Schritt-für-Schritt:**

```
Schritt 1: Reservoir füllen
  → Füllschraube an Helmpumpe öffnen
  → Fluid bis Oberkante einfüllen
  → NICHT verschließen (offenlassen für Nachfüllen)

Schritt 2: Zylinderseite entlüften
  → Entlüftungsschlauch auf Zylinder-Entlüftungsventil Port A
  → Ventil öffnen (1/4 Umdrehung)
  → Steuerrad langsam in Richtung Port A drehen (Fluid wird zum Zylinder gepumpt)
  → Drehen, bis blasenfreies Fluid austritt
  → Ventil schließen
  → Reservoir nachfüllen!
  → Gleichen Vorgang für Port B wiederholen

Schritt 3: Leitungen entlüften
  → Steuerrad 10× langsam von Anschlag zu Anschlag drehen
  → Dabei Reservoir ständig nachfüllen (darf NIE leer laufen!)
  → An beiden Zylinderventilen erneut entlüften (Schritt 2)

Schritt 4: Feinentlüftung
  → Steuerrad 20× schnell von Anschlag zu Anschlag drehen
  → Mikroblasen sammeln sich an Entlüftungspunkten
  → Nochmals an beiden Seiten entlüften
  → Reservoir auf korrekten Füllstand bringen

Schritt 5: Funktionsprüfung
  → Steuerrad muss sich gleichmäßig drehen (kein Schwammgefühl)
  → Ruder muss sofort und ohne Verzögerung folgen
  → Kein Spielgefühl am Steuerrad
  → Steuerrad loslassen: Ruder bleibt stehen (NF) oder kehrt sanft zurück (FB)
```

#### 6.2.2 Entlüftung bei Power-Assist-Systemen

Zusätzlich zum Standard-Verfahren:

```
Schritt 6: Power-Pack entlüften
  → Power-Pack Reservoir füllen
  → Power-Pack kurz laufen lassen (5–10 Sekunden)
  → Entlüftungsventil am Power-Pack öffnen
  → Laufen lassen bis blasenfrei
  → Ventil schließen, Reservoir nachfüllen
  → Wiederhole Schritt 2–5 mit laufendem Power-Pack
```

#### 6.2.3 Häufige Entlüftungsfehler

| Fehler | Auswirkung | Vermeidung |
|--------|-----------|-----------|
| Reservoir leer gelaufen | Luft eingesaugt → komplett neu entlüften | Ständig nachfüllen, nie leer! |
| Zu schnelles Drehen | Kavitation → Mikroblasen | Langsam, gleichmäßig drehen |
| Nur eine Seite entlüftet | Einseitig schwammig | Immer beide Ports entlüften |
| Falsches Fluid eingefüllt | Dichtungsschäden! | Fluid-Typ vorher prüfen! |
| Entlüftungsventil zu weit geöffnet | Fluid spritzt unkontrolliert | Max. 1/4 Umdrehung |
| Schlauch nicht auf Entlüftungsventil | Fluidverlust, Verschmutzung | Immer Schlauch in Behälter |

### 6.3 Hydraulikfluid-Typen und Kompatibilität

| System | Empfohlenes Fluid | Alternative | NICHT verwenden |
|--------|------------------|-------------|----------------|
| Jefa | ATF Dexron III/VI | ISO HLP 15 | Pflanzenöl, Bremsflüssigkeit |
| Lecomble & Schmitt | L&S LHM+ (ISO HLP 15) | ATF Dexron III | Pflanzenöl, Bremsflüssigkeit |
| SeaStar/Dometic | SeaStar HA5430 | ATF Dexron III | ISO HLP 46+, Bremsflüssigkeit |
| Hynautic (alt) | Hynautic HTF-2 | NICHTS anderes! | ATF, ISO HLP, Bremsflüssigkeit |
| Kobelt | ATF Dexron III/VI | ISO HLP 32 | Pflanzenöl, Bremsflüssigkeit |
| Vetus | Vetus HF115 (ISO HLP 15) | ATF Dexron III | Pflanzenöl, Bremsflüssigkeit |

**WARNUNG:** Hydraulikfluide verschiedener Basis-Typen NIEMALS mischen! Bei Systemwechsel: Komplett spülen und neu befüllen.

### 6.4 Montage des Steuerzylinders

#### 6.4.1 Zylinder-Ausrichtung

```
Korrekt:
  Zylinder-Kolbenstange steht SENKRECHT zum Tillerarm in Mittellage
  → Gleichmäßige Kraft in beide Richtungen
  → Maximaler wirksamer Hebelarm

Falsch:
  Zylinder schräg montiert
  → Seitenkraft auf Kolbenstange → Dichtungsverschleiß
  → Ungleichmäßiges Steuerverhalten
```

#### 6.4.2 Befestigungspunkte

- **Zylinderkörper:** Fest verschraubt auf stabiler Grundplatte (min. 10 mm GFK oder Edelstahl-Platte)
- **Kolbenstangen-Gabel:** Bolzenverbindung zum Tillerarm (selbstsichernde Kronenmutter + Splint)
- **Tillerarm:** Konisch auf Ruderschaft aufgepresst oder mit Keilverbindung. IMMER mit Sicherungsmutter!
- **Grundplatte:** Muss Zylinderkraft aufnehmen können. Berechnung: F_cylinder × Sicherheitsfaktor 3 = Befestigungskraft

### 6.5 Systemvolumen und Fluidmenge

| Systemgröße | Leitungen (2×8m) | Zylinder | Pumpe | Reservoir | Gesamt (ca.) |
|-------------|-----------------|---------|-------|-----------|-------------|
| Klein (10–14 m) | 200 ml | 150 ml | 50 ml | 100 ml | 500 ml |
| Mittel (14–18 m) | 400 ml | 350 ml | 80 ml | 200 ml | 1.030 ml |
| Groß (18–25 m) | 800 ml | 700 ml | 120 ml | 400 ml | 2.020 ml |
| Sehr groß (>25 m) | 1.500 ml | 1.500 ml | 200 ml | 800 ml | 4.000 ml |

---

## 7. Fehlerbild-Atlas

### Fehlerbild F14.03-01: Schwammiges Lenkgefühl (Luft im System)

**Symptom:** Steuerrad fühlt sich „weich" an, kein definierter Anschlag, Ruder reagiert verzögert.

**Ursache:** Luft im Hydrauliksystem — häufigste Störung überhaupt.

**Entstehung:**
- Unvollständige Entlüftung bei Installation/Wartung
- Schleichende Undichtigkeit (Luft wird eingesaugt bei Unterdruck-Phase)
- Reservoir-Füllstand zu niedrig
- Kavitation bei schnellem Drehen und zu kleinem Leitungsquerschnitt

**Diagnose:**
1. Steuerrad langsam von Anschlag zu Anschlag drehen — Widerstand gleichmäßig?
2. Steuerrad ruckartig drehen — Verzögerung? Schwammig?
3. Fluid im Reservoir prüfen — Bläschen? Schaum? Füllstand?

**Behebung:** Entlüftungsverfahren gemäß 6.2.

**Confidence:** measured (eindeutiges Symptombild)

### Fehlerbild F14.03-02: Externe Leckage an der Helmpumpe

**Symptom:** Öltropfen oder Ölfilm unter/um die Helmpumpe. Fluidstand im Reservoir sinkt.

**Ursache:** Verschlissener Wellendichtring oder defekte statische Dichtung.

**Typische Stellen:**
- Wellendichtring (Antriebswelle zum Steuerrad) — häufigste Leckstelle
- Gehäusedeckel-Dichtung (O-Ring)
- Anschlussverschraubungen
- Entlüftungsschraube

**Diagnose:**
1. Helmpumpe reinigen und trockenwischen
2. Steuerrad betätigen und Leckstelle beobachten
3. Wellendichtring: Öl tritt an der Radwelle aus
4. Gehäuse: Öl an den Gehäusekanten

**Behebung:**
- Wellendichtring: Austausch (Dichtungssatz vom Hersteller)
- Gehäusedichtung: O-Ring austauschen
- Verschraubungen: Nachziehen oder Dichtring erneuern

**Teile:** Herstellerspezifischer Dichtungssatz (z.B. Jefa SP-HP-xx, L&S SK-HTP-xx)

**Confidence:** measured

### Fehlerbild F14.03-03: Interne Leckage (Zylinder hält Druck nicht)

**Symptom:** Ruder „wandert" langsam aus der eingestellten Position. Steuerrad muss ständig korrigiert werden. Bei Non-Feedback: Ruder fällt langsam ab.

**Ursache:** Verschlissene Kolbendichtung im Steuerzylinder — Fluid strömt intern am Kolben vorbei.

**Diagnose:**
1. Ruder auf 20° Ausschlag stellen und Steuerrad loslassen
2. Beobachten: Ruder wandert langsam zur Mitte → interne Leckage
3. Zeitmessung: <5 Minuten bis spürbares Wandern = fortgeschrittener Verschleiß
4. Druckprüfung: System unter Druck setzen, Druckabfall messen (>2 bar/min = Leckage)

**Behebung:**
- Zylinder überholen: Kolbendichtung und Stangendichtung austauschen
- Bei starkem Verschleiß: Zylinder-Laufbuchse honen oder Zylinder ersetzen

**Confidence:** measured

### Fehlerbild F14.03-04: Schwergängige Steuerung

**Symptom:** Steuerrad erfordert übermäßige Kraft. Kann einseitig oder beidseitig sein.

**Ursache (Ranking nach Häufigkeit):**
1. Fluid zu hochviskos (falsche Spezifikation oder Alterung)
2. Einschränkung in Schlauchleitung (Knick, Quetschung, Innenseelen-Ablösung)
3. Luft im System (bei Kälte → Fluid dick + Luft kompressibel)
4. Zylinder-Mechanik klemmt (Korrosion, Seitenbelastung)
5. Helmpumpe verschlissen (erhöhte Reibung)
6. Tillerarm verklemmt oder Ruderanlage blockiert (nicht Hydraulik-spezifisch)

**Diagnose:**
1. Fluidzustand prüfen (Viskosität, Farbe, Geruch)
2. Schläuche visuell inspizieren (Knicke, Quetschungen)
3. System bei warmem Fluid testen (Viskositätseffekt?)
4. Zylinder abklemmen und manuell verfahren (Mechanik-Problem?)
5. Druckmessung an Pumpe vs. Zylinder (Druckabfall in Leitungen?)

**Behebung:** Ursachenabhängig (Fluidwechsel, Schlauchtausch, Zylinderüberholung)

**Confidence:** estimated (Ursachenzuordnung erfordert Diagnose)

### Fehlerbild F14.03-05: Pumpenverschleiß (Interne Leckage Pumpe)

**Symptom:** Erhöhte Umdrehungszahl für gleichen Ruderausschlag. Steuerrad „dreht durch" bei hohem Ruderdruck. Helmpumpe wird warm.

**Ursache:** Verschlissene Flügelzellen (Drehschieberpumpe) oder Kolbenringe (Kolbenpumpe). Fluid fließt intern an den Dichtelementen vorbei.

**Diagnose:**
1. Lock-to-Lock-Umdrehungen zählen und mit Sollwert vergleichen (>20 % mehr = Verschleiß)
2. Steuerrad gegen Anschlag drehen und halten — Steuerrad „dreht weiter"?
3. Fluidtemperatur an der Pumpe prüfen (warm = interne Reibung/Leckage)

**Behebung:**
- Dichtungssatz der Pumpe austauschen
- Flügelzellen und Stator-Ring austauschen (bei Drehschieberpumpen)
- Bei starkem Verschleiß: Pumpe ersetzen

**Confidence:** measured

### Fehlerbild F14.03-06: Zylinderriefen (Cylinder Scoring)

**Symptom:** Externe Leckage an Kolbenstange, ruckeliges Steuerverhalten, Kratzgeräusche.

**Ursache:** Riefen (Kratzer) auf der Kolbenstangenoberfläche oder in der Zylinderlaufbuchse.

**Entstehung:**
- Partikelkontamination im Fluid (häufigste Ursache)
- Korrosion auf der Kolbenstange (fehlende Schmierung, Salzwasser)
- Seitenlast auf Kolbenstange (schlechte Ausrichtung)
- Abstreifer-Versagen (Schmutz gelangt in Zylinder)

**Diagnose:**
1. Kolbenstange ausfahren und visuell inspizieren
2. Mit Fingernagel über Oberfläche fahren — spürbarer Kratzer = Riefe
3. Fluid auf Metallpartikel prüfen (Magnettest bei Stahlabrieb)

**Behebung:**
- Leichte Riefen: Kolbenstange polieren (mit 1200er Nassschleifpapier, nur in Achsrichtung!)
- Mittlere Riefen: Kolbenstange nachverchromen lassen
- Schwere Riefen: Kolbenstange oder kompletten Zylinder ersetzen
- Zylinder-Innenfläche: Honen oder ersetzen

**Confidence:** measured

### Fehlerbild F14.03-07: Geräusche beim Steuern

**Symptom:** Klickende, mahlende, quietschende oder pumpende Geräusche beim Drehen des Steuerrades.

**Ursachenmatrix:**

| Geräusch | Mögliche Ursache | Dringlichkeit |
|----------|-----------------|--------------|
| Klicken (rhythmisch) | Luftblasen durch Ventile | Mittel |
| Klicken (unregelmäßig) | Lose Verbindung Tillerarm/Zylinder | Hoch! |
| Mahlen | Trockenlauf Pumpe, Partikel | Hoch! |
| Quietschen | Trockener Wellendichtring | Niedrig |
| Pulsieren | Kavitation, zu dünnes Fluid | Mittel |
| Knacken bei Richtungswechsel | Spiel in Gelenken, Verschleiß | Mittel |
| Zischen | Interne Leckage unter Druck | Mittel |

**Confidence:** estimated (Geräuschdiagnose erfordert Erfahrung)

### Fehlerbild F14.03-08: Steuerrad dreht sich selbstständig (bei Feedback-System)

**Symptom:** Bei losgelassenem Steuerrad dreht sich dieses durch Ruderdruck (Wellenschlag, Luvgierigkeit). Normal bei Feedback-Systemen, aber kann übermäßig sein.

**Ursache (bei übermäßigem Rückdrehen):**
1. Feedback-Ventil zu weit offen eingestellt
2. Bypass-Ventil defekt (schließt nicht vollständig)
3. Interne Pumpenleckage (Fluid fließt unkontrolliert zurück)
4. Defektes Rückschlagventil

**Behebung:**
1. Feedback-Ventil nachstellen (weniger Feedback = weniger Rückdrehen)
2. Bypass-Ventil prüfen und ggf. ersetzen
3. Pumpendichtungen prüfen

**Confidence:** estimated

### Fehlerbild F14.03-09: Fluid-Verfärbung und -Degradation

**Symptom:** Hydraulikfluid hat sich von transparent-bernstein zu milchig, dunkel oder schwarz verfärbt.

**Farbdiagnose:**

| Farbe | Ursache | Maßnahme |
|-------|---------|---------|
| Milchig-weiß | Wasser im System (Emulsion) | Fluid komplett wechseln, Wasserquelle finden |
| Dunkelbraun | Oxidation/Alterung | Fluid wechseln |
| Schwarz | Überhitzung oder starker Abrieb | Fluid wechseln, Ursache beseitigen |
| Grünlich | Kupfer-/Bronze-Korrosion | Fluid wechseln, korrodierende Teile ersetzen |
| Rötlich (bei ATF) | Normal für ATF | Nur bei weiterer Veränderung handeln |
| Schaumig | Luft im System | Entlüften, Fluid nachfüllen |

**Confidence:** measured (Farbdiagnose gut dokumentiert)

### Fehlerbild F14.03-10: Überdruckventil löst aus

**Symptom:** Plötzlicher Druckverlust beim Steuern, „Klick"-Geräusch, Steuerrad wird kurz leichtgängig.

**Ursache:**
1. Ruderschlag (Welle trifft Ruder) → Druckspitze → Ventil öffnet (normal!)
2. Überdruckventil falsch eingestellt (zu niedrig)
3. Zugesetzter Filter → Druckaufbau
4. Zylinderanschlag erreicht → hydraulisches Totvolumen

**Behebung:**
- Bei Ruderschlag: Normal — Ventil schützt System
- Einstellung prüfen: Soll = 1,3–1,5 × Betriebsdruck
- Filter reinigen/ersetzen
- Zylinderanschläge prüfen

**Confidence:** measured

### Fehlerbild F14.03-11: Asymmetrisches Steuerverhalten

**Symptom:** Steuerung in eine Richtung leichter/schneller als in die andere.

**Ursache:**
1. Ungleich lange Schlauchleitungen (verschiedener Druckverlust)
2. Luft nur auf einer Seite (unvollständig entlüftet)
3. Asymmetrischer Zylinder (Single-Ram, nicht balanced)
4. Teilweise blockierte Leitung auf einer Seite
5. Defektes Rückschlagventil auf einer Seite

**Diagnose:**
1. Lock-to-Lock in beide Richtungen messen (Umdrehungen, Kraft)
2. Schlauchlängen vergleichen
3. Druckmessung an beiden Zylinderports

**Behebung:** Ursachenabhängig

**Confidence:** estimated

### Fehlerbild F14.03-12: Korrosion an Anschlüssen und Fittings

**Symptom:** Weiße oder grüne Korrosionsablagerungen an Verschraubungen, Tropfenbildung.

**Ursache:**
- Elektrochemische Korrosion (unterschiedliche Metalle)
- Salzwassereinwirkung auf ungeschützte Fittings
- Lochkorrosion bei Edelstahl-Fittings in Spalten

**Prävention:**
1. Nur marine-grade Fittings verwenden (316L Edelstahl oder Bronze)
2. Fittings mit Korrosionsschutz-Spray behandeln (z.B. Tef-Gel, Lanocote)
3. Galvanische Trennung bei unterschiedlichen Metallen
4. Regelmäßige Inspektion, besonders im Maschinenraum

**Behebung:**
- Leichte Korrosion: Reinigen, Schutzspray auftragen
- Starke Korrosion: Fitting ersetzen, Dichtung erneuern

**Confidence:** measured

---

## 8. Troubleshooting

### Entscheidungsbaum T14.03-01: Schwammige Lenkung

```
START: Steuerung fühlt sich schwammig an
  │
  ├─ Reservoir-Füllstand prüfen
  │   ├─ Zu niedrig → Auffüllen, auf Leckage prüfen → Entlüften
  │   └─ OK → weiter
  │
  ├─ Fluid-Zustand prüfen
  │   ├─ Milchig/Schaum → Wasser/Luft → Fluid wechseln + Entlüften
  │   └─ OK → weiter
  │
  ├─ Entlüftungsverfahren durchführen (6.2)
  │   ├─ Besserung → LÖSUNG: Luft war im System
  │   └─ Keine Besserung → weiter
  │
  ├─ Druckprüfung am Zylinder
  │   ├─ Druck fällt ab → Interne Leckage Zylinder (F14.03-03)
  │   └─ Druck stabil → weiter
  │
  ├─ Pumpenverschleiß prüfen (Lock-to-Lock zählen)
  │   ├─ >20 % über Sollwert → Pumpe verschlissen (F14.03-05)
  │   └─ OK → weiter
  │
  └─ Schläuche prüfen (Ausdehnung unter Druck?)
      ├─ Schlauch bläht sich → Schlauch degradiert → Austausch
      └─ OK → Ursache nicht hydraulisch → Ruderanlage prüfen (14_01)
```

### Entscheidungsbaum T14.03-02: Lenkung schwergängig

```
START: Steuerung erfordert zu viel Kraft
  │
  ├─ Beidseitig oder einseitig?
  │   ├─ Einseitig → Schlauchleitungen prüfen (Knick, Quetschung)
  │   │              → Zylinderseite prüfen (Korrosion, Seitenbelastung)
  │   └─ Beidseitig → weiter
  │
  ├─ Temperaturabhängig?
  │   ├─ Nur bei Kälte → Fluid-Viskosität zu hoch → Fluidwechsel auf niedrigere Viskosität
  │   └─ Immer → weiter
  │
  ├─ Fluid-Zustand prüfen
  │   ├─ Dunkel/verdickt → Fluid degradiert → Komplettwechsel
  │   └─ OK → weiter
  │
  ├─ Zylinder mechanisch prüfen
  │   ├─ Kolbenstange verkratzt/korrodiert → Zylinderriefen (F14.03-06)
  │   └─ OK → weiter
  │
  └─ Ruderanlage prüfen
      ├─ Ruder schwergängig ohne Hydraulik → Problem an Ruderanlage (14_01)
      └─ OK → Pumpe verschlissen (erhöhte Reibung) → Pumpe überholen/ersetzen
```

### Entscheidungsbaum T14.03-03: Leckage-Ortung

```
START: Fluidverlust festgestellt
  │
  ├─ System reinigen und trockenwischen
  │
  ├─ Steuerrad 10× betätigen, Leckstelle suchen
  │   ├─ An Helmpumpe → F14.03-02 (Wellendichtring, Gehäusedichtung)
  │   ├─ An Zylinder-Kolbenstange → Stangendichtung verschlissen
  │   ├─ An Zylinderanschlüssen → Fitting nachziehen oder Dichtring erneuern
  │   ├─ An Schlauchenden → Fitting-Verbindung undicht → Nachziehen/Erneuern
  │   ├─ Am Schlauch selbst → Schlauch porös/beschädigt → Austausch!
  │   └─ Am Reservoir → Deckel/Dichtung prüfen
  │
  └─ Nicht sichtbar?
      → Interne Leckage (F14.03-03) → kein externer Fluidverlust,
        aber Leistungsverlust
```

### Entscheidungsbaum T14.03-04: Autopilot steuert nicht korrekt

```
START: Autopilot reagiert nicht oder steuert falsch
  │
  ├─ AP-Pumpe läuft (Geräusch)?
  │   ├─ Nein → Elektrisches Problem (Sicherung, Kabel, ACU) → Nicht Hydraulik!
  │   └─ Ja → weiter
  │
  ├─ Ruder bewegt sich bei AP-Betätigung?
  │   ├─ Nein → Solenoidventile prüfen (öffnen sie?)
  │   │         → Hydraulikleitungen zum Zylinder prüfen
  │   │         → AP-Pumpe fördert Druck? (Druckmessung)
  │   └─ Ja, aber falsch → weiter
  │
  ├─ Ruder bewegt sich in falsche Richtung?
  │   ├─ Ja → Leitungen am AP vertauscht (Port A/B) → Umklemmen
  │   │     → Ruderlagengeber invertiert → Konfiguration im AP-Computer prüfen
  │   └─ Nein → weiter
  │
  ├─ Ruder bewegt sich zu wenig/zu viel?
  │   ├─ Zu wenig → AP-Pumpe zu klein für System
  │   │            → Luft im AP-Leitungsbereich → Entlüften
  │   │            → AP-Verstärkung (Gain) zu niedrig → AP-Konfiguration
  │   └─ Zu viel → AP-Gain zu hoch → AP-Konfiguration
  │
  └─ Ruder oszilliert (pendelt)?
      → Ruderlagengeber defekt oder falsch kalibriert
      → AP-Dämpfung (Counter-Rudder) zu niedrig → AP-Konfiguration
      → Mechanisches Spiel in Ruderanlage → 14_01 prüfen
```

### Entscheidungsbaum T14.03-05: Geräuschdiagnose

```
START: Ungewöhnliche Geräusche beim Steuern
  │
  ├─ Art des Geräuschs?
  │   ├─ Klicken → Luft (F14.03-01) oder lose Verbindung (Tillerarm, Bolzen)
  │   ├─ Mahlen → Partikelkontamination → Fluid wechseln, System spülen
  │   │          → Trockenlauf Pumpe → Fluidstand prüfen!
  │   ├─ Quietschen → Wellendichtring trocken → Fluid nachfüllen
  │   │              → Kolbenstange korrodiert → Zylinder prüfen
  │   ├─ Pulsieren → Kavitation → Schlauch-ID zu klein? Fluid zu viskos?
  │   ├─ Zischen → Interne Leckage unter Druck
  │   └─ Knacken → Spiel in Gelenken → Bolzen/Lager prüfen und austauschen
  │
  └─ Geräusch nur in einer Drehrichtung?
      → Einseitiges Problem → Leitung/Ventil auf dieser Seite prüfen
```

---

## 9. FAQ — Häufige Fragen

### FAQ-01: Welches Hydraulikfluid soll ich verwenden?

**Antwort:** Immer das vom Hersteller empfohlene Fluid verwenden! Im Zweifelsfall: ATF Dexron III/VI ist für die meisten Systeme kompatibel (außer Hynautic-Altsysteme). Siehe Kompatibilitätstabelle in Abschnitt 6.3.

**Confidence:** documented

### FAQ-02: Wie oft muss ich das Hydraulikfluid wechseln?

**Antwort:** Bei Normalnutzung (Saisonbetrieb, 200–500 Betriebsstunden/Jahr): alle 3–5 Jahre. Bei Intensivnutzung (Charter, Langfahrt): alle 2–3 Jahre. Jährlich Füllstand und Farbe prüfen. Siehe Tabelle in 2.4.2.

**Confidence:** estimated

### FAQ-03: Warum fühlt sich meine Steuerung „tot" an (kein Feedback)?

**Antwort:** Entweder haben Sie ein Non-Feedback-System (Standard bei Motorbooten — das ist normal), oder bei einem Feedback-System ist das Feedback-Ventil geschlossen oder defekt. Prüfen Sie den Feedback-Ventil-Stand (siehe 2.6.3). Bei Segelbooten wird ein Feedback-System dringend empfohlen.

**Confidence:** documented

### FAQ-04: Kann ich mein mechanisches Steuerungssystem auf hydraulisch umrüsten?

**Antwort:** Ja, das ist eine häufige Nachrüstung. Erforderlich: Helmpumpe (passt meist auf vorhandenen Pedestal), Steuerzylinder mit Tillerarm (passt auf vorhandenen Ruderschaft), Schlauchleitungen und Fluid. Typische Kosten inkl. Einbau: 2.000–5.000 EUR bei 12–16 m Segelyacht. Ein erfahrener Fachbetrieb sollte die Umrüstung durchführen, insbesondere für korrekte Auslegung und Entlüftung.

**Confidence:** estimated

### FAQ-05: Mein Steuerrad hat plötzlich mehr Umdrehungen von Anschlag zu Anschlag. Warum?

**Antwort:** Luft im System (häufigste Ursache) oder Pumpenverschleiß. Entlüften Sie das System gemäß Abschnitt 6.2. Wenn das Problem nach dem Entlüften weiterhin besteht, ist wahrscheinlich die Helmpumpe verschlissen (Flügelzellen, Dichtungen) und muss überholt werden.

**Confidence:** measured

### FAQ-06: Kann ich Schläuche verschiedener Hersteller verwenden?

**Antwort:** Grundsätzlich ja, sofern der Druckbereich (bar) und die Anschlüsse (Fitting-Typ) kompatibel sind. SAE 100R7 reicht für die meisten manuellen Systeme (bis 70 bar). ACHTUNG: Die Fitting-Typen (ORB, JIC, BSP, NPT) sind NICHT kompatibel! Adapter sind möglich, aber jede Verbindung ist eine potenzielle Leckstelle. Idealerweise Schläuche vom Systemhersteller verwenden.

**Confidence:** documented

### FAQ-07: Wie groß muss mein Steuerzylinder sein?

**Antwort:** Das hängt vom Ruderdrehmoment ab (siehe 2.1.4). Faustregel: Ruderdrehmoment [Nm] / Tillerarm-Länge [m] = Zylinderkraft [N]. Dann: Zylinderfläche = Kraft / Systemdruck. In der Praxis empfehlen alle Hersteller Auswahltabellen nach Bootslänge — diese sind der sicherste Weg. Im Zweifelsfall: eine Nummer größer wählen.

**Confidence:** estimated

### FAQ-08: Was passiert, wenn eine Hydraulikleitung bricht?

**Antwort:** Totaler Steuerungsverlust! Das Fluid fließt aus, der Zylinder hat keinen Druck mehr. Deshalb ist es lebenswichtig, Schläuche regelmäßig zu inspizieren (alle 2–3 Jahre visuell, nach 10 Jahren ersetzen). Für längere Fahrten: Notsteuerung vorbereiten (Notpinne, Not-Seilsteuerung). Einige Hersteller bieten redundante Leitungssysteme.

**Confidence:** documented (Sicherheitsaspekt, gut dokumentiert)

### FAQ-09: Kann ich einen Autopiloten an mein manuelles Hydrauliksystem anschließen?

**Antwort:** Ja, das ist die Standardkonfiguration. Ein hydraulischer Autopilot-Antrieb (z.B. Raymarine Type 2, B&G HP2) wird über T-Stücke und Rückschlagventile in das bestehende System eingebunden. Siehe Abschnitt 5.4 für Anschlussschemen. Wichtig: Feedback-Systeme erfordern AP-Antriebe mit ausreichender Haltekraft.

**Confidence:** documented

### FAQ-10: Woran erkenne ich, dass mein System entlüftet werden muss?

**Antwort:** Typische Anzeichen: 1) Schwammiges Steuergefühl, 2) erhöhte Lock-to-Lock-Umdrehungszahl, 3) Geräusche (Klicken, Glucken), 4) Verzögerte Ruderreaktion, 5) Bläschen/Schaum im Reservoir-Fluid. Nach jedem Eingriff am Hydrauliksystem (Schlauchwechsel, Zylinderarbeit, Fluidwechsel) muss immer entlüftet werden!

**Confidence:** measured

### FAQ-11: Wie viel kostet eine hydraulische Steueranlage?

**Antwort:** Richtwerte (ohne Einbau, Confidence: estimated):
- Motorboot 8–12 m (SeaStar-Kit): 650–1.500 EUR
- Segelyacht 12–16 m (Jefa/L&S manuell): 2.500–5.000 EUR
- Segelyacht 16–22 m (Jefa/L&S mit Power-Assist): 5.000–12.000 EUR
- Motoryacht 15–25 m (Kobelt Full Power): 8.000–25.000 EUR
- Superyacht >25 m (Proportionalventil): 15.000–80.000 EUR
- Einbaukosten: 1.000–5.000 EUR je nach Komplexität

### FAQ-12: Welches System bietet das beste Steuergefühl für Segelboote?

**Antwort:** Manuelle hydraulische Systeme mit einstellbarem Feedback (z.B. Jefa HP-Serie, Lecomble & Schmitt HTP-Serie). Diese bieten: 1) Spürbare Ruderkraft-Rückmeldung, 2) Einstellbares Feedback (von „direkt" bis „gedämpft"), 3) Keine elektrische Abhängigkeit, 4) Gute Autopilot-Kompatibilität. Für Performance-Segler: Jefa Rotary-Vane-Aktuatoren bieten das direkteste Steuergefühl in der Hydraulik-Klasse.

**Confidence:** documented/estimated

### FAQ-13: Was ist der Unterschied zwischen Non-Feedback und Feedback?

**Antwort:** Non-Feedback: Steuerrad dreht, Ruder bewegt sich, fertig. Kein Ruderdruck spürbar am Steuerrad. Standard bei Motorbooten. Feedback: Ruderdruck wird teilweise ans Steuerrad zurückgemeldet. Steuermann „fühlt" das Wasser. Standard bei Segelyachten. Siehe ausführliche Erklärung in Abschnitt 2.6.

**Confidence:** documented

### FAQ-14: Kann ich zwei Steuerräder an einer Hydrauliksteuerung betreiben?

**Antwort:** Ja. Zwei Helmpumpen werden parallel an denselben Zylinder angeschlossen. Dabei müssen beide Pumpen identische Verdrängung haben. Bei Non-Feedback-Systemen: Die nicht benutzte Pumpe dreht sich mit (Bypass). Bei Feedback-Systemen: Beide Steuerräder drehen sich synchron (Ruderdruck drückt Fluid zu beiden Pumpen). Viele Hersteller bieten fertige Dual-Station-Kits.

**Confidence:** documented

### FAQ-15: Mein Reservoir braucht ständig Nachfüllung. Was tun?

**Antwort:** Es gibt externe Leckage! System reinigen, trockenwischen, betätigen und Leckstelle suchen (Entscheidungsbaum T14.03-03). Häufigste Stellen: Wellendichtring Helmpumpe, Kolbenstangendichtung Zylinder, Verschraubungen. NICHT ignorieren — Fluidverlust = potentieller Steuerungsausfall!

**Confidence:** measured

### FAQ-16: Muss ich den Hydraulikschlauch alle 10 Jahre ersetzen?

**Antwort:** ISO 10592 (Small craft — Hydraulic steering systems) empfiehlt einen maximalen Einsatzzeitraum von 10 Jahren für Hydraulikschläuche. In der Praxis halten hochwertige Schläuche in geschützter Einbaulage auch länger. Empfehlung: Alle 3–5 Jahre visuell inspizieren (Risse, Aufquellungen, Verhärtung, Abrieb). Bei Sichtbefund oder Alter >10 Jahre: Ersetzen. Besonders UV-exponierte Schläuche an Deck: Früherer Tausch nötig.

**Confidence:** documented

### FAQ-17: Kann ich Hydraulikfluid selbst wechseln?

**Antwort:** Ja, mit etwas Sorgfalt. Vorgehensweise: 1) Altes Fluid am tiefsten Punkt ablassen, 2) System mit neuem Fluid spülen (1× Volumen durchlaufen lassen), 3) Frisches Fluid einfüllen, 4) Komplett entlüften (Abschnitt 6.2), 5) Füllstand prüfen. Wichtig: Korrektes Fluid verwenden! Altes Fluid umweltgerecht entsorgen (Sondermüll!).

**Confidence:** documented

### FAQ-18: Was ist ein Balanced-Ram-Zylinder und brauche ich einen?

**Antwort:** Ein Balanced-Ram-Zylinder hat die Kolbenstange auf beiden Seiten — dadurch ist die Kolbenfläche auf beiden Seiten identisch, und das Steuerverhalten ist perfekt symmetrisch. Empfohlen für: Segelboote (Steuergefühl wichtig), Feedback-Systeme, Performance-Cruiser. Nicht nötig für: Motorboote mit Non-Feedback (hier reicht Standard-Zylinder). Siehe Abschnitt 3.6.

**Confidence:** documented

### FAQ-19: Wie entlüfte ich ein System mit Autopilot-Anbindung?

**Antwort:** Zuerst das Hauptsystem (Helmpumpe → Zylinder) komplett entlüften (Abschnitt 6.2). Dann den Autopilot-Zweig: AP-Pumpe kurz laufen lassen, Entlüftungsventile am AP und an den T-Stücken öffnen, bis blasenfrei. Abschließend nochmals das Gesamtsystem durch mehrfaches Betätigen von Steuerrad UND Autopilot entlüften. Reservoir ständig nachfüllen!

**Confidence:** documented

### FAQ-20: Was tun bei einem Hydraulikleitungsbruch auf See?

**Antwort:** SOFORT: 1) Segelmanöver zum Beidrehen oder Motor auf Leerlauf, 2) Notpinne bereithalten, 3) Gebrochenen Schlauch identifizieren, 4) Wenn möglich: Schlauch absperren (Klemme, Schraubklemme), 5) Reserveschlauch anschließen (wenn vorhanden), 6) System auffüllen und entlüften, 7) Wenn Reparatur nicht möglich: Notpinne verwenden. Prävention: Ersatzschlauch an Bord haben! Mindestens 2× längster Schlauch + Fittings.

**Confidence:** documented

### FAQ-21: Was bedeutet „Lock-to-Lock" und wie viele Umdrehungen sind normal?

**Antwort:** Lock-to-Lock ist die Anzahl der Steuerrad-Umdrehungen von vollem Ruderausschlag links (Backbord) bis vollem Ruderausschlag rechts (Steuerbord). Typische Werte: Segelboote 3,0–5,0 Umdrehungen, Motorboote 3,5–6,0 Umdrehungen. Weniger Umdrehungen = direkteres Steuern, aber höhere Handkraft. Mehr Umdrehungen = leichtgängiger, aber indirekter. Die Umdrehungszahl wird durch die Pumpenverdrängung und das Zylindervolumen bestimmt.

**Confidence:** documented

### FAQ-22: Kann ich eine Power-Assist-Pumpe nachrüsten?

**Antwort:** Ja, das ist eine gängige Nachrüstung, besonders wenn ein Autopilot installiert wird. Die Power-Pack-Pumpe wird über T-Stücke und Rückschlagventile parallel zur Helmpumpe angeschlossen. Typische Kosten: 1.500–4.000 EUR (Power-Pack + Installation). Voraussetzung: Ausreichende Bordelektrik (12V: 50–80 A, 24V: 25–60 A) und Platz für das Power-Pack (typisch 30×20×15 cm).

**Confidence:** estimated

### FAQ-23: Sind Bio-Hydraulikfluide empfehlenswert?

**Antwort:** Bio-abbaubare Hydraulikfluide (HEES, z.B. Panolin HLP Synth) sind umweltfreundlich und in einigen Gebieten (z.B. Bodensee, bestimmte Nationalparks) vorgeschrieben. Sie bieten gute Schmiereigenschaften und Korrosionsschutz. Nachteil: Höherer Preis (3–5× Mineralöl), geringere Verfügbarkeit, nicht kompatibel mit allen Dichtungsmaterialien (Verträglichkeit prüfen!). Bei Neusystemen empfehlenswert, bei Altsystemen nur nach Rücksprache mit Hersteller.

**Confidence:** estimated

### FAQ-24: Mein SeaStar-System und mein Jefa-System — sind die kompatibel?

**Antwort:** Grundsätzlich NEIN, da unterschiedliche Fitting-Typen (SeaStar: SAE/JIC, Jefa: ORB) und teilweise unterschiedliche Fluide. Eine Kombination erfordert Adapter-Fittings an jeder Verbindung und ein kompatibles Fluid (ATF Dexron III als gemeinsamer Nenner). Empfehlung: Möglichst ein System durchgehend vom gleichen Hersteller. Mischsysteme erhöhen Leckagerisiko und erschweren Ersatzteilversorgung.

**Confidence:** documented

### FAQ-25: Wie prüfe ich die Hydrauliksteuerung beim Gebrauchtkauf?

**Antwort:** Checkliste: 1) Fluid-Farbe und -Stand prüfen (milchig/schwarz = schlecht), 2) Alle Anschlüsse auf Leckage prüfen, 3) Lock-to-Lock-Umdrehungen zählen (Sollwert kennen!), 4) Schwammigkeit prüfen (Steuerrad ruckartig betätigen), 5) Kolbenstange ausfahren und auf Riefen/Korrosion prüfen, 6) Schlauchzustand visuell prüfen (Alter, Risse, Aufquellungen), 7) Steuerrad loslassen — bleibt Ruder stehen (NF) oder kehrt sanft zurück (FB)? 8) Geräusche beim Steuern? 9) Herstellerangaben und Alter des Systems erfragen.

**Confidence:** documented

---

## 10. Glossar

| Begriff (DE) | Begriff (EN) | Definition |
|-------------|-------------|-----------|
| Helmpumpe | Helm Pump | Hydraulikpumpe am Steuerstand, wandelt Radrehung in Volumenstrom |
| Steuerzylinder | Steering Cylinder | Hydraulikzylinder am Ruderschaft, wandelt Druck in Linearkraft |
| Tillerarm | Tiller Arm | Hebel am Ruderschaft, auf den der Zylinder wirkt |
| Ruderschaft | Rudder Stock/Shaft | Drehachse des Ruders, durchdringt den Rumpf |
| Ruderkoker | Rudder Tube/Trunk | Rohr im Rumpf, in dem der Ruderschaft läuft |
| Balanced Ram | Balanced Ram | Zylinder mit durchgehender Kolbenstange (gleiche Fläche beidseitig) |
| Drehflügel-Aktuator | Rotary Vane Actuator | Drehender Hydraulik-Stellantrieb direkt am Ruderschaft |
| Feedback-System | Feedback System | System, das Ruderdruck ans Steuerrad zurückmeldet |
| Non-Feedback | Non-Feedback | System ohne Ruderdruck-Rückmeldung |
| Drehschieberpumpe | Rotary Vane Pump | Pumpentyp mit rotierenden Flügelzellen |
| Axialkolbenpumpe | Axial Piston Pump | Pumpentyp mit axial angeordneten Kolben |
| Radialkolbenpumpe | Radial Piston Pump | Pumpentyp mit radial angeordneten Kolben |
| Flügelzelle | Vane | Dichtelement in einer Drehschieberpumpe |
| Verdrängung | Displacement | Fluidvolumen pro Pumpenumdrehung [cm³/U] |
| Lock-to-Lock | Lock-to-Lock | Umdrehungen Steuerrad von Anschlag zu Anschlag |
| Überdruckventil | Relief Valve / PRV | Ventil zum Schutz vor Überdruck |
| Rückschlagventil | Check Valve | Ventil, das Fluidfluss nur in eine Richtung erlaubt |
| Solenoidventil | Solenoid Valve | Elektrisch betätigtes Hydraulikventil |
| Proportionalventil | Proportional Valve | Elektrisch stufenlos gesteuertes Ventil |
| Power-Pack | Power Pack | Elektromotor + Hydraulikpumpe als Einheit |
| Reservoir | Reservoir / Header Tank | Ausgleichsbehälter für Hydraulikfluid |
| Entlüften | Bleeding / Purging | Entfernung von Luft aus dem Hydrauliksystem |
| Betriebsdruck | Working/Operating Pressure | Normaler Systemdruck im Betrieb [bar] |
| Berstdruck | Burst Pressure | Druck, bei dem ein Bauteil versagt [bar] |
| Kavitation | Cavitation | Dampfblasenbildung bei Unterdruck — zerstört Pumpen |
| Druckverlust | Pressure Drop | Druckabfall in Leitung durch Reibung [bar/m] |
| O-Ring | O-Ring | Ringförmige Dichtung aus Elastomer |
| NBR | NBR (Nitrile Butadiene Rubber) | Standard-Dichtungswerkstoff für Hydraulik |
| Viton | Viton (FKM/FPM) | Hochtemperatur- und chemikalienbeständiges Elastomer |
| PTFE | PTFE (Polytetrafluoroethylene) | Reibungsarmer Kunststoff für Gleitdichtungen |
| Wellendichtring | Shaft Seal / Lip Seal | Dichtung um rotierende Wellen |
| Abstreifer | Wiper Seal / Scraper | Dichtung, die Schmutz von der Kolbenstange abhält |
| HLP | HLP (Hydraulic Lubricating with EP Additives) | Standard-Hydrauliköl-Klasse nach DIN 51524 |
| ATF | ATF (Automatic Transmission Fluid) | Getriebeöl, häufig als Hydraulikfluid im Marinebereich verwendet |
| Viskosität | Viscosity | Zähflüssigkeit eines Fluids [cSt] |
| Viskositätsindex | Viscosity Index (VI) | Maß für Temperaturabhängigkeit der Viskosität |
| ORB | ORB (O-Ring Boss) | Fitting-Typ mit O-Ring-Dichtung |
| JIC | JIC (Joint Industry Council) | Fitting-Typ mit 37°-Konus |
| BSP | BSP (British Standard Pipe) | Fitting-Typ mit Rohrgewinde |
| NPT | NPT (National Pipe Thread) | Fitting-Typ mit konischem Rohrgewinde (USA) |
| Orbitrol | Orbitrol / Orbital Valve | Steuerventil für Full-Power-Systeme |
| Ruderlage | Rudder Angle / Rudder Position | Aktueller Winkel des Ruders |
| Ruderlagengeber | Rudder Feedback Unit / RFU | Sensor, der Ruderposition an Autopilot meldet |
| Einschaltdauer (ED) | Duty Cycle | Prozentuale Laufzeit einer Pumpe pro Zeiteinheit |

---

## 11. Schnell-Referenz

### 11.1 Systemauswahl nach Bootsgröße

```
Segelboot 8–12 m          → Manuell hydraulisch (Jefa HP-10/L&S HTP 30)
                             Zylinder: HC-40/V120 oder Rotary-Vane RV-35
                             Druck: 35–50 bar
                             Lock-to-Lock: 3,0–4,0

Segelboot 12–16 m         → Manuell hydraulisch (Jefa HP-14/L&S HTP 42)
                             Zylinder: HC-50/V150 oder Rotary-Vane RV-50
                             Druck: 45–60 bar
                             Lock-to-Lock: 3,5–4,5

Segelboot 16–20 m         → Manuell hydraulisch + Power-Assist optional
                             (Jefa HP-18/L&S HTP 53)
                             Zylinder: HC-60/V200 oder RV-65
                             Druck: 50–70 bar
                             Lock-to-Lock: 3,5–5,0

Segelboot 20–25 m         → Power-Assist empfohlen (Jefa HP-24/L&S HTP 60)
                             Zylinder: HC-80/V250 oder RV-80
                             Druck: 50–70 bar + PP bis 100 bar
                             Lock-to-Lock: 4,0–5,5

Segelboot >25 m            → Full Power empfohlen
                             Zylinder: HC-100+/V300+ oder RV-100
                             Druck: 70–140 bar

Motorboot 8–12 m           → SeaStar HK4200A/HK4500A Kit
                             Inline-Zylinder HC5345/HC5348
                             Druck: 35–70 bar

Motorboot 12–18 m          → SeaStar Pro/Kobelt 7004/Vetus HTP3010
                             Zylinder: HC5370/Kobelt 2012
                             Druck: 50–100 bar

Motorboot 18–25 m          → Kobelt 7012/L&S PP 24/2 (Power-Assist oder Full Power)
                             Zylinder: Kobelt 2014-2016/L&S MC80
                             Druck: 70–140 bar

Motoryacht >25 m            → Full Power (Kobelt 7020/L&S PP 24/8)
                             Proportionalventil-Option
                             Druck: 100–200 bar
```

### 11.2 Fluidtyp-Schnellwahl

```
Jefa        → ATF Dexron III/VI
L&S         → L&S LHM+ (oder ATF Dexron III)
SeaStar     → SeaStar HA5430 (oder ATF Dexron III)
Hynautic    → Hynautic HTF-2 NUR!
Kobelt      → ATF Dexron III/VI
Vetus       → Vetus HF115 (oder ATF Dexron III)
```

### 11.3 Wartungsintervall-Übersicht

```
Jährlich:           Fluidstand prüfen, Leckage-Sichtkontrolle
Alle 2–3 Jahre:     Fluid-Farbe und -Zustand prüfen
Alle 3–5 Jahre:     Fluidwechsel (bei Normalnutzung)
Alle 5 Jahre:       Schläuche visuell inspizieren, Fittings prüfen
Alle 8–12 Jahre:    Schläuche ersetzen (oder nach Befund früher)
Alle 10–15 Jahre:   Pumpendichtungen und Zylinderdichtungen prüfen/ersetzen
```

### 11.4 Notfall-Referenz

```
Leitungsbruch:       Absperren → Notpinne → Reparatur oder Hafen anlaufen
Totaler Druckverlust: Notpinne verwenden → System inspizieren
Steuerrad blockiert:  Überdruckventil-Einstellung prüfen → Mechanische Blockade?
Autopilot steuert nicht: AP aus → Manuell steuern → AP-Diagnose in ruhigem Wasser
```

---

## ANHANG A — Fallstudien

### Fallstudie A-01: Bavaria 40 Cruiser — Umrüstung mechanisch auf hydraulisch

**Boot:** Bavaria 40 Cruiser (2008), 12,35 m LOA, Radsteuerung mit Whitlock-Seilsteuerung (ab Werk).

**Problem:** Seilsteuerung mit zunehmendem Spiel (Seilspannung nachgelassen), schwergängig über Umlenkrollen, Seil korrodiert. Autopilot (Raymarine Radpilot) unbefriedigend.

**Lösung:** Umrüstung auf Lecomble & Schmitt HTP 42 (Feedback) + V150 Balanced-Ram-Zylinder + Raymarine Type 2 Autopilot-Antrieb.

**Installation:**
- Helmpumpe auf vorhandenen Lewmar-Pedestal montiert (Adapter L&S → Lewmar)
- Zylinder mit neuem Tillerarm auf vorhandenem Ruderschaft (Ø 50 mm)
- 2× 7 m Hydraulikschlauch 3/8" BSP
- Raymarine Type 2 über T-Stücke eingebunden
- Fluid: L&S LHM+

**Ergebnis:**
- Steuergefühl deutlich verbessert (einstellbares Feedback)
- Autopilot-Performance dramatisch besser (hydraulisch vs. Radpilot)
- Lock-to-Lock: 3,8 Umdrehungen
- Kosten: 3.200 EUR (Material) + 1.500 EUR (Einbau durch Fachbetrieb)

**Confidence:** documented (Eigner-Bericht + Werft-Dokumentation)

### Fallstudie A-02: Hallberg-Rassy 48 — Pumpenverschleiß nach 18 Jahren

**Boot:** Hallberg-Rassy 48 MkII (2006), 14,76 m LOA, Jefa-Hydrauliksteuerung ab Werk.

**Problem:** Nach 18 Jahren und ca. 12.000 Seemeilen: Lock-to-Lock erhöht von 4,0 auf 5,2 Umdrehungen. Schwammiges Gefühl. Fluid war zuletzt vor 8 Jahren gewechselt worden.

**Diagnose:**
- Fluid: Dunkelbraun, riecht verbrannt
- Magnettest Fluid: Metallpartikel vorhanden
- Lock-to-Lock: 5,2 (Sollwert: 4,0)
- Zylinderprüfung: Hält Druck — OK
- Pumpenprüfung: Interne Leckage → Flügelzellen verschlissen

**Lösung:**
- Jefa Dichtungssatz SP-HP-18 + neue Flügelzellen bestellt
- Pumpe komplett überholt (Stator-Ring leicht verschlissen, aber noch akzeptabel)
- Komplettwechsel Fluid (ATF Dexron III)
- System gespült und entlüftet

**Ergebnis:**
- Lock-to-Lock zurück auf 4,0 Umdrehungen
- Steuergefühl wie neu
- Kosten: 380 EUR (Dichtungssatz + Flügelzellen) + 250 EUR (Fluid + Arbeitszeit Eigenleistung)

**Confidence:** documented (Jefa Service-Bericht)

### Fallstudie A-03: Sunseeker Manhattan 55 — Power-Steering-Ausfall

**Boot:** Sunseeker Manhattan 55 (2014), 17,4 m LOA, Kobelt Full-Power-Hydrauliksteuerung.

**Problem:** Während Hafenmanöver plötzlicher Verlust der Servolenkung. Steuerrad extrem schwergängig (manueller Notbetrieb).

**Diagnose:**
1. Power-Pack läuft nicht → Sicherung 80A durchgebrannt
2. Sicherung erneuert → Power-Pack läuft, aber überhitzt und schaltet ab
3. Ursache: Hydraulikfilter seit 5 Jahren nicht gewechselt → verstopft → Pumpe gegen erhöhten Widerstand → Überlast → Sicherung

**Lösung:**
- Hydraulikfilter gewechselt (Kobelt Original)
- Fluid gewechselt (ATF Dexron VI)
- System entlüftet
- Sicherung erneuert

**Ergebnis:** System funktioniert wieder normal. Empfehlung: Filterwechsel alle 2 Jahre bei Intensivnutzung.

**Kosten:** 120 EUR (Filter + Fluid + Sicherung)

**Confidence:** documented (Werft-Servicebericht)

### Fallstudie A-04: Contest 50CS — Autopilot-Integrationsproblem

**Boot:** Contest 50CS (2019), 15,24 m LOA, Jefa HP-18 (Feedback) + HC-60 + B&G H5000 Autopilot.

**Problem:** Autopilot oszilliert (Ruder pendelt ±5° um Sollkurs). Manuelles Steuern einwandfrei.

**Diagnose:**
1. Ruderlagengeber kalibriert → korrekt
2. AP-Gain reduziert → Oszillation weniger, aber Kurshalten schlechter
3. Feedback-Ventil analysiert: Feedback-System erlaubt Rücklauf des Fluids → AP-Pumpe pumpt gegen Rücklaufdruck → Oszillation

**Lösung:**
- Feedback-Ventil wird bei AP-Betrieb über ein Solenoidventil geschlossen (Umbau: zusätzliches 2/2-Solenoidventil in der Bypass-Leitung)
- Solenoidventil wird vom AP-Computer geschaltet (bei AP aktiv → Solenoid schließt → Non-Feedback → AP steuert sauber)
- Bei manuellem Steuern: Solenoid offen → volles Feedback

**Ergebnis:** AP steuert einwandfrei, manuelles Steuergefühl unverändert. Elegante Lösung.

**Kosten:** 350 EUR (Solenoidventil + Relais + Einbau)

**Confidence:** documented (B&G Technical Note + Jefa Service-Empfehlung)

### Fallstudie A-05: Jeanneau Sun Odyssey 440 — Luft im System nach Winterlager

**Boot:** Jeanneau Sun Odyssey 440 (2021), 13,34 m LOA, Lecomble & Schmitt HTP 42 + V150.

**Problem:** Nach Winterlager: Steuerung schwammig, Steuerrad hat merkliches Spiel.

**Diagnose:**
- Fluid im Reservoir: Leicht geschäumt, Füllstand 1 cm zu niedrig
- Keine externe Leckage sichtbar
- Ursache: Temperaturwechsel im Winterlager (–15°C bis +20°C) → Kondenswasser im Reservoir → Mikroblasen → Volumenkontraktion → Luft eingesaugt

**Lösung:**
- Fluid abgelassen → leicht milchig (Wasseranteil)
- System mit frischem LHM+ gespült
- Neu befüllt und sorgfältig entlüftet (3× Entlüftungszyklus)
- Reservoir bis korrekten Stand aufgefüllt

**Ergebnis:** Steuerung wieder einwandfrei. Empfehlung: Vor dem Einwintern Reservoir bis Maximum füllen, um Luftvolumen zu minimieren.

**Kosten:** 60 EUR (2L LHM+ Fluid)

**Confidence:** documented (Eigner-Bericht)

### Fallstudie A-06: Beneteau Oceanis 51.1 — Zylinderriefen durch Partikel

**Boot:** Beneteau Oceanis 51.1 (2018), 15,94 m LOA, Original-Hydrauliksteuerung (Lecomble & Schmitt).

**Problem:** Ruckelndes Steuerverhalten, leichte externe Leckage am Zylinder.

**Diagnose:**
1. Kolbenstange ausgefahren: Deutliche Längsriefen sichtbar (0,1–0,3 mm tief)
2. Fluid: Dunkle Metallpartikel sichtbar
3. Ursache: Werft hatte bei Inbetriebnahme Metallspäne im System belassen → über 6 Jahre → Riefen

**Lösung:**
- Zylinder komplett überholt: Kolbenstange nachverchromen lassen, neue Dichtungen
- Gesamtsystem gespült (3× mit frischem Fluid)
- Neu befüllt und entlüftet
- Inline-Filter nachgerüstet (10 µm, zwischen Pumpe und Zylinder)

**Ergebnis:** Steuerung wieder einwandfrei. Filter als Prävention empfohlen.

**Kosten:** 1.200 EUR (Zylinderüberholung + Verchromung) + 180 EUR (Filter) + 300 EUR (Spülung/Fluid)

**Confidence:** documented (Werft-Servicebericht + Herstelleranalyse)

### Fallstudie A-07: Nordhavn 47 — Dual-Station-Installation

**Boot:** Nordhavn 47 (2012), 15,1 m LOA, Trawler-Motoryacht. Installation einer hydraulischen Dual-Station-Steuerung (Steuerhaus + Flybridge).

**Systemkonfiguration:**
- Steuerhaus: Kobelt 7004 Helmpumpe (16 cm³/U)
- Flybridge: Kobelt 7004 Helmpumpe (identisch)
- Zylinder: Kobelt 2014 (65 mm, 260 mm Hub)
- Power-Pack: Kobelt 6524 (24V, 2,5 kW) für Autopilot
- Autopilot: Simrad SDP30
- Leitungen: 2× 12 m (Steuerhaus→Zylinder), 2× 8 m (Flybridge→Zylinder)
- Fluid: ATF Dexron VI

**Besonderheiten:**
- Beide Helmpumpen parallel am Zylinder angeschlossen
- Bei Steuerung von einer Station dreht sich das andere Steuerrad mit (Non-Feedback: Bypass in der nicht benutzten Pumpe)
- Autopilot über Power-Pack separat angeschlossen
- Ruderlagengeber: Hall-Effekt (Kobelt), NMEA 2000 kompatibel

**Kosten:** 8.500 EUR (Material) + 3.500 EUR (Installation)

**Confidence:** documented (Kobelt Systemdesign + Werftbericht)

### Fallstudie A-08: Swan 65 — Rotary-Vane-Aktuator Retrofit

**Boot:** Nautor's Swan 65 (1985, refit 2022), 19,8 m LOA. Umrüstung von Seil-/Kettensteuerung mit Radpilot auf Jefa Rotary-Vane-Hydraulik.

**Problem:** Alte Seil-/Kettensteuerung verschlissen, Autopilot (Radpilot) unzureichend für Blauwasser-Segeln.

**Systemkonfiguration:**
- Helmpumpe: Jefa HP-24 (Feedback)
- Aktuator: Jefa RV-80 (Schaft-Ø 90 mm, 3.000 Nm)
- Autopilot: Raymarine Type 3 + ACU-200 + Evolution-Sensor
- Leitungen: 2× 5 m Hydraulikschlauch 1/2" ORB
- Fluid: ATF Dexron III
- Feedback-Ventil: Eingestellt auf Level 3 (ca. 60 % Rückmeldung)

**Besonderheiten:**
- RV-80 direkt auf Ruderkoker montiert — Tillerarm entfällt komplett
- Extrem kompakte Installation in der engen Achterpiek
- Integrierter Ruderlagengeber im RV-80
- Feedback-Solenoid für AP-Betrieb (schließt Feedback bei AP aktiv)

**Ergebnis:**
- Steuergefühl: „Wie Pinnensteuerung, nur leichter" (Eignerzitat)
- Autopilot-Performance: Exzellent (Blauwasser-tauglich)
- Lock-to-Lock: 4,2 Umdrehungen
- Kosten: 7.800 EUR (Material) + 4.200 EUR (Installation inkl. Ruderkoker-Anpassung)

**Confidence:** documented (Jefa Projektbericht + Eigner-Erfahrung)

---

## ANHANG B — Druckberechnungstabellen

### B.1 Zylinderkraft bei verschiedenen Drücken

| Kolben-Ø [mm] | Fläche [cm²] | 35 bar [N] | 50 bar [N] | 70 bar [N] | 100 bar [N] | 140 bar [N] |
|---------------|-------------|-----------|-----------|-----------|------------|------------|
| 40 | 12,57 | 4.399 | 6.283 | 8.796 | 12.566 | 17.593 |
| 50 | 19,63 | 6.872 | 9.817 | 13.744 | 19.635 | 27.489 |
| 60 | 28,27 | 9.896 | 14.137 | 19.792 | 28.274 | 39.584 |
| 70 | 38,48 | 13.470 | 19.242 | 26.939 | 38.485 | 53.879 |
| 80 | 50,27 | 17.593 | 25.133 | 35.186 | 50.265 | 70.372 |
| 90 | 63,62 | 22.266 | 31.809 | 44.532 | 63.617 | 89.064 |
| 100 | 78,54 | 27.489 | 39.270 | 54.978 | 78.540 | 109.956 |
| 120 | 113,10 | 39.584 | 56.549 | 79.168 | 113.097 | 158.336 |
| 140 | 153,94 | 53.879 | 76.969 | 107.757 | 153.938 | 215.514 |

### B.2 Ruderdrehmoment bei gegebener Zylinderkraft und Tillerarm

| Zylinderkraft [N] | Tillerarm 150 mm | 200 mm | 250 mm | 300 mm |
|-------------------|-----------------|--------|--------|--------|
| 5.000 | 750 Nm | 1.000 Nm | 1.250 Nm | 1.500 Nm |
| 10.000 | 1.500 Nm | 2.000 Nm | 2.500 Nm | 3.000 Nm |
| 15.000 | 2.250 Nm | 3.000 Nm | 3.750 Nm | 4.500 Nm |
| 20.000 | 3.000 Nm | 4.000 Nm | 5.000 Nm | 6.000 Nm |
| 30.000 | 4.500 Nm | 6.000 Nm | 7.500 Nm | 9.000 Nm |
| 50.000 | 7.500 Nm | 10.000 Nm | 12.500 Nm | 15.000 Nm |

### B.3 Systemvolumen-Berechnung

```
V_system = V_zylinder + V_leitungen + V_pumpe + V_reservoir + V_AP (optional)

V_zylinder = π/4 × D² × Hub (einseitig) oder × 2 (doppeltwirkend, gesamt)
V_leitungen = π/4 × d² × L × 2 (2 Leitungen)
V_pumpe = typ. 30–80 cm³ (interne Volumina)
V_reservoir = 15–25 % von V_system_rest (Ausgleich + Reserve)
V_AP = AP-Pumpenvolumen + Leitungen (typ. 50–200 cm³)
```

---

## ANHANG C — Confidence-Mapping

### C.1 Confidence-Zuordnung nach Datenquelle

| Datenquelle | Confidence-Level | AYDI-Code |
|------------|-----------------|-----------|
| Hersteller-TDS (technische Datenblätter) | Measured | `measured` |
| ISO-Normen | Measured | `measured` |
| Hersteller-Kataloge | Documented | `documented` |
| Fachzeitschriften (Practical Sailor, SAIL) | Documented | `documented` |
| Werft-Serviceberichte | Documented | `documented` |
| Surveyor-Berichte | Documented | `documented` |
| Berechnung aus Messwerten | Calculated | `calculated` |
| Erfahrungswerte Fachbetriebe | Estimated | `estimated` |
| Eigner-Berichte (Foren, Blogposts) | Estimated | `estimated` |
| Marktdaten, Preise | Estimated | `estimated` |
| Visuelle Inspektion (Fotos) | Visual_medium | `visual_medium` |

### C.2 Confidence-Level pro Abschnitt

| Abschnitt | Primäres Confidence-Level |
|-----------|--------------------------|
| 2. Grundlagen (Physik) | measured/calculated |
| 3. Typenübersicht | documented |
| 4. Produktlinien (Kennwerte) | measured |
| 4. Produktlinien (Preise) | estimated |
| 5. Autopilot-Integration | documented |
| 6. Installation | documented |
| 7. Fehlerbild-Atlas | measured/documented |
| 8. Troubleshooting | estimated/documented |
| 9. FAQ | documented/estimated |

---

## ANHANG D — Normen-Zusammenfassung

### D.1 ISO 10592 — Small craft — Hydraulic steering systems (Hydraulische Steueranlagen)

> ✅ Aufgeloest (Audit): Die hydraulischen Anforderungen gehoeren zu ISO 10592 (Small craft — Hydraulic steering systems), NICHT zu ISO 8847 — ISO 8847:2021 regelt Seilzug-/Umlenkrollensteuerungen ("Cable over pulley systems"). Norm-Zuordnung korrigiert (ISO 8847 → ISO 10592, auch in Abschnitt 4.7 und FAQ-16). Quelle: iso.org/standard/18676 (ISO 10592 Hydraulic steering), iso.org/standard/75809 (ISO 8847 Cable over pulley).

**Geltungsbereich:** Hydraulische Steueranlagen für Sportboote mit Rumpflänge bis 24 m (ISO 10592:1994; aktuelle Neufassung ISO 10592:2022 „Remote hydraulic steering systems").

**Wesentliche Anforderungen für Hydrauliksysteme:**
- Berstdruck der Leitungen: ≥4× max. Betriebsdruck
- Alle Verbindungen müssen gegen Lösen gesichert sein
- Überdruckventil: Pflicht bei geschlossenen Systemen
- Redundanz: Notsteuerungsmöglichkeit muss vorhanden sein
- Schläuche: Max. Einsatzdauer 10 Jahre (Herstellerabhängig)
- Korrosionsschutz: Alle metallischen Komponenten für Salzwasserumgebung geeignet

### D.2 ISO 25197:2020 — Steuerungssysteme für Boote

**Ergänzende Anforderungen:**
- Hydraulische Steuerung muss auch bei Ausfall der Energieversorgung manuell bedienbar sein
- Ansprechzeit: Max. 5 Sekunden von Steuersignal bis Ruderbewegung
- Ruderbewegungszeit (Anschlag zu Anschlag): Max. 28 Sekunden (Sportboote bis 24 m)
- Ruderpositionsanzeige: Pflicht bei Systemen ohne direkte Sichtlinie zum Ruder

### D.3 ABYC P-21 — Hydraulic Steering Systems

**Nordamerikanischer Standard (ABYC):**
- Alle hydraulischen Komponenten müssen für 4× Betriebsdruck ausgelegt sein
- Fluidverträglichkeit aller Dichtungen muss dokumentiert sein
- Entlüftungsventile: Pflicht an jedem Zylinder und jeder Pumpe
- Fittings: Müssen den Mindestanforderungen SAE J514 oder SAE J1926 entsprechen
- Aluminiumanschlüsse: Nicht erlaubt in Salzwasserzonen (nur Edelstahl oder Bronze)

---

## ANHANG E — Wartungsintervalle

### E.1 Wartungsplan hydraulische Steuerung

| Intervall | Tätigkeit | Dauer | Qualifikation |
|-----------|----------|-------|--------------|
| Vor jeder Fahrt | Steuerung auf Funktion prüfen (10× drehen) | 2 min | Eigner |
| Monatlich | Reservoir-Füllstand prüfen | 1 min | Eigner |
| Halbjährlich | Alle Anschlüsse auf Leckage visuell prüfen | 10 min | Eigner |
| Jährlich | Fluid-Farbe und -Zustand prüfen, Schläuche visuell inspizieren | 20 min | Eigner |
| Alle 2 Jahre | Anschlüsse auf Korrosion prüfen, Tillerarm-Befestigung prüfen | 30 min | Eigner/Fachmann |
| Alle 3–5 Jahre | Fluidwechsel + Systemspülung + Entlüftung | 1–2 h | Fachmann empfohlen |
| Alle 5–8 Jahre | Schläuche inspizieren (Risse, Verhärtung, Aufquellungen) | 30 min | Fachmann |
| Alle 8–12 Jahre | Schläuche ersetzen (prophylaktisch) | 2–4 h | Fachmann |
| Alle 10–15 Jahre | Pumpen-Dichtungssatz, Zylinder-Dichtungssatz prüfen/ersetzen | 3–6 h | Fachmann |
| Alle 15–25 Jahre | Gesamtsystem überholen (Pumpe, Zylinder, Ventile) | 1–2 Tage | Spezialist |

### E.2 Wartungskosten (Richtwerte)

| Tätigkeit | Materialkosten | Arbeitskosten (Fachbetrieb) | Gesamt |
|-----------|---------------|---------------------------|--------|
| Fluidwechsel | 30–80 EUR | 100–200 EUR | 130–280 EUR |
| Schlauchwechsel (2×) | 150–400 EUR | 200–500 EUR | 350–900 EUR |
| Pumpen-Dichtungssatz | 80–250 EUR | 200–400 EUR | 280–650 EUR |
| Zylinder-Dichtungssatz | 60–200 EUR | 150–400 EUR | 210–600 EUR |
| Komplette Pumpenüberholung | 200–600 EUR | 300–600 EUR | 500–1.200 EUR |
| Komplette Zylinderüberholung | 300–1.200 EUR | 300–800 EUR | 600–2.000 EUR |
| Gesamtsystem-Überholung | 800–3.000 EUR | 1.000–3.000 EUR | 1.800–6.000 EUR |

(Confidence: estimated)

---

## ANHANG F — Leitungsverlust-Diagramme

### F.1 Druckverlust vs. Leitungslänge (für ISO VG 15, 20°C, Q = 10 cm³/s)

```
Δp [bar]
  │
2.0├─────────────────────────────────────── 8 mm ID
  │                                    ╱
1.5├──────────────────────────────────╱
  │                               ╱
1.0├────────────────────────────╱──────── 10 mm ID
  │                         ╱       ╱
0.5├──────────────────────╱───────╱───── 12 mm ID
  │                    ╱       ╱    ╱
0.0├───┬───┬───┬───┬──╱┬───┬──╱┬──╱┬───── 16 mm ID
  0   2   4   6   8  10  12  14  16  18  20
                                      Leitungslänge [m]
```

### F.2 Viskositätseinfluss auf Druckverlust

```
Faktor (bezogen auf VG 15 bei 20°C):
  VG 15 bei –10°C:  3,5×
  VG 15 bei   0°C:  2,0×
  VG 15 bei  20°C:  1,0× (Referenz)
  VG 15 bei  40°C:  0,6×
  VG 32 bei  20°C:  2,1×
  VG 46 bei  20°C:  3,1×
  ATF bei    20°C:  2,0×
  ATF bei   –20°C:  8,0×
```

**Empfehlung:** In kalten Revieren (Skandinavien, Kanada) VG 15 oder ATF verwenden. VG 32/46 nur in warmen Gewässern oder bei Hochdrucksystemen.

---

## ANHANG G — Historische Entwicklung

### G.1 Meilensteine der hydraulischen Yachtsteuerung

| Jahr | Ereignis | Bedeutung |
|------|---------|-----------|
| 1795 | Joseph Bramah patentiert hydraulische Presse | Grundlage aller Hydraulik |
| 1868 | Lecomble & Schmitt gegründet (Boulogne-sur-Mer) | Ältester aktiver Hersteller |
| 1906 | Erste hydraulische Ruderanlage auf Handelsschiffen | Rapson-Slide-Prinzip |
| 1959 | Hynautic gegründet (USA) | Erste kompakte Marine-Hydraulik |
| 1962 | Kobelt gegründet (Kanada) | Spezialist für schwere Systeme |
| 1965 | L&S erste Helmpumpe für Yachten | Hydraulik unter 20 m Bootslänge |
| 1975 | Teleflex SeaStar-Linie | Massenmärktliche Motorboot-Hydraulik |
| 1979 | Jefa gegründet (Dänemark) | Präzisions-Hydraulik für Segelyachten |
| 1985 | Feedback-Systeme für Segelyachten verbreitet | Steuergefühl-Revolution |
| 1995 | Erste Autopilot-Solenoidventil-Integration | Autopilot + Hydraulik Standard |
| 2003 | Lewmar übernimmt Whitlock → Hydraulik-Portfolio | Konsolidierung |
| 2010 | Jefa Rotary-Vane-Aktuatoren | Kompakt-Revolution |
| 2017 | Dometic übernimmt Teleflex Marine (SeaStar Solutions) | Weltmarktführer-Bildung |
| 2017 | Proportionalventil-Steuerungen für Yachten <30 m | Superyacht-Technik nach unten |
| 2020 | Bio-Hydraulikfluide für Marine | Umweltschutz |
| 2023 | Integrierte Diagnose-Sensorik | Predictive Maintenance |

---

## ANHANG H — AYDI-Integration (Pydantic-Modelle)

```python
"""
AYDI Knowledge Models — 14.03 Hydraulische Steuerung
Pydantic v2 models for hydraulic steering system analysis.
"""

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class HydraulicSteeringType(str, Enum):
    """Type of hydraulic steering system."""
    MANUAL_HYDRAULIC = "manual_hydraulic"
    POWER_ASSISTED = "power_assisted"
    FULL_POWER = "full_power"
    PROPORTIONAL_VALVE = "proportional_valve"


class CylinderType(str, Enum):
    """Type of hydraulic steering cylinder."""
    SINGLE_RAM = "single_ram"
    DOUBLE_ACTING = "double_acting"
    BALANCED_RAM = "balanced_ram"
    ROTARY_VANE = "rotary_vane"
    INLINE = "inline"


class PumpType(str, Enum):
    """Type of hydraulic helm pump."""
    ROTARY_VANE = "rotary_vane"
    AXIAL_PISTON = "axial_piston"
    RADIAL_PISTON = "radial_piston"
    GEAR = "gear"


class FeedbackMode(str, Enum):
    """Steering feedback mode."""
    NON_FEEDBACK = "non_feedback"
    FEEDBACK = "feedback"
    ADJUSTABLE = "adjustable"


class HydraulicFluidType(str, Enum):
    """Type of hydraulic fluid."""
    ATF_DEXRON_III = "atf_dexron_iii"
    ATF_DEXRON_VI = "atf_dexron_vi"
    ISO_HLP_15 = "iso_hlp_15"
    ISO_HLP_32 = "iso_hlp_32"
    ISO_HLP_46 = "iso_hlp_46"
    BIO_HEES = "bio_hees"
    PROPRIETARY_SEASTAR = "proprietary_seastar"
    PROPRIETARY_HYNAUTIC = "proprietary_hynautic"


class HydraulicSteeringManufacturer(str, Enum):
    """Known hydraulic steering manufacturers."""
    JEFA = "jefa"
    LECOMBLE_SCHMITT = "lecomble_schmitt"
    KOBELT = "kobelt"
    SEASTAR_DOMETIC = "seastar_dometic"
    HYNAUTIC = "hynautic"
    VETUS = "vetus"
    LEWMAR = "lewmar"
    OTHER = "other"


class AutopilotBrand(str, Enum):
    """Autopilot brands for integration assessment."""
    RAYMARINE = "raymarine"
    BG = "bg"
    SIMRAD = "simrad"
    GARMIN = "garmin"
    FURUNO = "furuno"
    OTHER = "other"


class FittingStandard(str, Enum):
    """Hydraulic fitting standards."""
    ORB = "orb"
    JIC_37 = "jic_37"
    BSP = "bsp"
    NPT = "npt"
    SAE = "sae"
    PROPRIETARY = "proprietary"


class HydraulicSteeringSpec(BaseModel):
    """Complete specification of a hydraulic steering system."""
    model_config = {"from_attributes": True}

    steering_type: HydraulicSteeringType = Field(
        ..., description="Type of hydraulic steering system"
    )
    manufacturer: HydraulicSteeringManufacturer = Field(
        ..., description="System manufacturer"
    )
    pump_model: Optional[str] = Field(
        None, description="Helm pump model designation"
    )
    pump_type: PumpType = Field(
        ..., description="Pump mechanism type"
    )
    pump_displacement_cc: float = Field(
        ..., ge=5.0, le=80.0,
        description="Pump displacement in cm³ per revolution"
    )
    cylinder_model: Optional[str] = Field(
        None, description="Cylinder model designation"
    )
    cylinder_type: CylinderType = Field(
        ..., description="Cylinder construction type"
    )
    cylinder_bore_mm: float = Field(
        ..., ge=30.0, le=200.0,
        description="Cylinder bore diameter in mm"
    )
    cylinder_stroke_mm: float = Field(
        ..., ge=100.0, le=500.0,
        description="Cylinder stroke in mm"
    )
    max_operating_pressure_bar: float = Field(
        ..., ge=20.0, le=300.0,
        description="Maximum operating pressure in bar"
    )
    feedback_mode: FeedbackMode = Field(
        ..., description="Steering feedback mode"
    )
    fluid_type: HydraulicFluidType = Field(
        ..., description="Hydraulic fluid specification"
    )
    fitting_standard: FittingStandard = Field(
        ..., description="Fitting connection standard"
    )
    hose_inner_diameter_mm: float = Field(
        ..., ge=6.0, le=25.0,
        description="Hose inner diameter in mm"
    )
    hose_length_m: float = Field(
        ..., ge=1.0, le=40.0,
        description="Total hose length (one side) in meters"
    )
    lock_to_lock_turns: Optional[float] = Field(
        None, ge=1.5, le=10.0,
        description="Turns of the wheel from lock to lock"
    )
    has_power_assist: bool = Field(
        False, description="Whether a power assist pack is installed"
    )
    has_autopilot_integration: bool = Field(
        False, description="Whether autopilot hydraulic drive is integrated"
    )
    autopilot_brand: Optional[AutopilotBrand] = Field(
        None, description="Autopilot brand if integrated"
    )
    system_age_years: Optional[float] = Field(
        None, ge=0.0, le=50.0,
        description="System age in years"
    )
    vessel_loa_m: float = Field(
        ..., ge=6.0, le=60.0,
        description="Vessel length overall in meters"
    )
    vessel_type: str = Field(
        ..., description="Vessel type: sailboat, motorboat, catamaran, trawler"
    )


class HydraulicPressureAssessment(BaseModel):
    """System pressure assessment for a hydraulic steering system."""
    model_config = {"from_attributes": True}

    max_rudder_torque_nm: float = Field(
        ..., ge=50.0, le=50000.0,
        description="Maximum rudder torque in Nm"
    )
    tiller_arm_length_mm: float = Field(
        ..., ge=100.0, le=500.0,
        description="Tiller arm length in mm"
    )
    cylinder_bore_mm: float = Field(
        ..., ge=30.0, le=200.0,
        description="Cylinder bore diameter in mm"
    )
    required_pressure_bar: float = Field(
        ..., ge=10.0, le=300.0,
        description="Required system pressure in bar"
    )
    system_max_pressure_bar: float = Field(
        ..., ge=20.0, le=300.0,
        description="Maximum rated system pressure in bar"
    )
    safety_factor: float = Field(
        ..., ge=1.0, le=10.0,
        description="Safety factor (system max / required)"
    )
    pressure_rating: str = Field(
        ..., description="Rating: adequate, marginal, insufficient"
    )
    confidence: str = Field(
        default="calculated",
        description="Confidence level of this assessment"
    )


class FluidConditionAssessment(BaseModel):
    """Hydraulic fluid condition assessment."""
    model_config = {"from_attributes": True}

    fluid_type: HydraulicFluidType = Field(
        ..., description="Type of fluid in system"
    )
    fluid_age_years: Optional[float] = Field(
        None, ge=0.0, le=20.0,
        description="Fluid age in years"
    )
    color_assessment: str = Field(
        ..., description="Visual color: clear_amber, dark_brown, black, milky, foamy"
    )
    water_contamination: bool = Field(
        ..., description="Whether water contamination is detected"
    )
    particle_contamination: bool = Field(
        ..., description="Whether particle contamination is detected"
    )
    level_adequate: bool = Field(
        ..., description="Whether fluid level is adequate"
    )
    condition_score: float = Field(
        ..., ge=0.0, le=100.0,
        description="Overall fluid condition score (0=replace immediately, 100=new)"
    )
    recommendation: str = Field(
        ..., description="Recommendation: ok, monitor, replace_soon, replace_immediately"
    )
    confidence: str = Field(
        default="visual_medium",
        description="Confidence level of this assessment"
    )


class SealConditionAssessment(BaseModel):
    """Seal wear and condition assessment."""
    model_config = {"from_attributes": True}

    component: str = Field(
        ..., description="Component: helm_pump, cylinder_piston, cylinder_rod, shaft_seal"
    )
    external_leakage: bool = Field(
        ..., description="Whether external leakage is visible"
    )
    internal_leakage_suspected: bool = Field(
        ..., description="Whether internal leakage is suspected"
    )
    lock_to_lock_deviation_percent: Optional[float] = Field(
        None, ge=0.0, le=100.0,
        description="Deviation from nominal lock-to-lock turns in percent"
    )
    pressure_hold_test_passed: Optional[bool] = Field(
        None, description="Whether pressure hold test was passed"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        None, ge=0.0, le=20.0,
        description="Estimated remaining seal life in years"
    )
    condition_score: float = Field(
        ..., ge=0.0, le=100.0,
        description="Seal condition score (0=failed, 100=new)"
    )
    recommendation: str = Field(
        ..., description="Recommendation: ok, monitor, plan_replacement, replace_now"
    )
    confidence: str = Field(
        default="estimated",
        description="Confidence level"
    )


class HoseConditionAssessment(BaseModel):
    """Hydraulic hose condition assessment."""
    model_config = {"from_attributes": True}

    hose_age_years: Optional[float] = Field(
        None, ge=0.0, le=30.0,
        description="Hose age in years"
    )
    hose_inner_diameter_mm: float = Field(
        ..., ge=6.0, le=25.0,
        description="Hose inner diameter in mm"
    )
    visual_condition: str = Field(
        ..., description="Visual: good, surface_cracks, bulging, abraded, hardened, leaking"
    )
    uv_exposure: str = Field(
        ..., description="UV exposure level: none, low, medium, high"
    )
    routing_quality: str = Field(
        ..., description="Routing: good, tight_bends, chafe_points, unsupported"
    )
    fitting_condition: str = Field(
        ..., description="Fitting: good, corroded, weeping, loose"
    )
    condition_score: float = Field(
        ..., ge=0.0, le=100.0,
        description="Overall hose condition score"
    )
    replacement_urgency: str = Field(
        ..., description="Urgency: none, plan_next_season, plan_soon, replace_now"
    )
    confidence: str = Field(
        default="visual_medium",
        description="Confidence level"
    )


class AutopilotIntegrationAssessment(BaseModel):
    """Assessment of autopilot hydraulic integration."""
    model_config = {"from_attributes": True}

    autopilot_brand: AutopilotBrand = Field(
        ..., description="Autopilot manufacturer"
    )
    drive_type: str = Field(
        ..., description="Drive type: reversing_pump, solenoid_valve, proportional"
    )
    feedback_mode_compatible: bool = Field(
        ..., description="Whether AP is compatible with the steering feedback mode"
    )
    feedback_solenoid_installed: bool = Field(
        False, description="Whether a feedback-bypass solenoid is installed for AP mode"
    )
    rudder_feedback_unit_type: str = Field(
        ..., description="RFU type: potentiometric, hall_effect, lvdt, encoder"
    )
    rudder_feedback_calibrated: bool = Field(
        ..., description="Whether RFU is properly calibrated"
    )
    ap_performance_score: float = Field(
        ..., ge=0.0, le=100.0,
        description="Autopilot steering performance score"
    )
    integration_quality: str = Field(
        ..., description="Integration quality: excellent, good, adequate, poor, incompatible"
    )
    confidence: str = Field(
        default="documented",
        description="Confidence level"
    )


class HydraulicSteeringFaultFinding(BaseModel):
    """Individual fault finding in a hydraulic steering system."""
    model_config = {"from_attributes": True}

    fault_code: str = Field(
        ..., pattern=r"^F14\.03-\d{2}$",
        description="Fault code from Fehlerbild-Atlas (e.g., F14.03-01)"
    )
    fault_description_de: str = Field(
        ..., description="Fault description in German"
    )
    severity: str = Field(
        ..., description="Severity: critical, major, minor, cosmetic"
    )
    location: str = Field(
        ..., description="Location: helm_pump, cylinder, hose, fitting, reservoir, autopilot"
    )
    immediate_action_required: bool = Field(
        ..., description="Whether immediate action is required for safety"
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        None, ge=0.0, le=50000.0,
        description="Estimated repair cost in EUR"
    )
    confidence: str = Field(
        default="estimated",
        description="Confidence level of this finding"
    )


class HydraulicSteeringSystemAssessment(BaseModel):
    """Complete hydraulic steering system assessment combining all sub-assessments."""
    model_config = {"from_attributes": True}

    vessel_loa_m: float = Field(
        ..., ge=6.0, le=60.0,
        description="Vessel length overall in meters"
    )
    vessel_type: str = Field(
        ..., description="Vessel type"
    )
    system_spec: HydraulicSteeringSpec = Field(
        ..., description="System specification"
    )
    pressure_assessment: Optional[HydraulicPressureAssessment] = Field(
        None, description="Pressure adequacy assessment"
    )
    fluid_assessment: Optional[FluidConditionAssessment] = Field(
        None, description="Fluid condition assessment"
    )
    seal_assessments: list[SealConditionAssessment] = Field(
        default_factory=list,
        description="Seal condition assessments per component"
    )
    hose_assessment: Optional[HoseConditionAssessment] = Field(
        None, description="Hose condition assessment"
    )
    autopilot_assessment: Optional[AutopilotIntegrationAssessment] = Field(
        None, description="Autopilot integration assessment"
    )
    fault_findings: list[HydraulicSteeringFaultFinding] = Field(
        default_factory=list,
        description="List of fault findings"
    )
    overall_score: float = Field(
        ..., ge=0.0, le=100.0,
        description="Overall system score (0=critical, 100=excellent)"
    )
    overall_condition: str = Field(
        ..., description="Overall: excellent, good, fair, poor, critical"
    )
    primary_recommendation: str = Field(
        ..., description="Primary recommendation in German"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        None, ge=0.0, le=30.0,
        description="Estimated remaining system life in years"
    )
    estimated_total_repair_cost_eur: Optional[float] = Field(
        None, ge=0.0, le=100000.0,
        description="Estimated total repair/replacement cost"
    )
    confidence: str = Field(
        default="estimated",
        description="Overall assessment confidence level"
    )


class PowerPackSpec(BaseModel):
    """Specification for a hydraulic power pack (power assist / full power)."""
    model_config = {"from_attributes": True}

    manufacturer: HydraulicSteeringManufacturer = Field(
        ..., description="Power pack manufacturer"
    )
    model: str = Field(
        ..., description="Power pack model"
    )
    voltage_v: float = Field(
        ..., ge=12.0, le=48.0,
        description="Operating voltage in Volts"
    )
    power_kw: float = Field(
        ..., ge=0.3, le=15.0,
        description="Motor power in kW"
    )
    flow_rate_lpm: float = Field(
        ..., ge=1.0, le=40.0,
        description="Flow rate in liters per minute"
    )
    max_pressure_bar: float = Field(
        ..., ge=50.0, le=300.0,
        description="Maximum output pressure in bar"
    )
    reservoir_volume_l: float = Field(
        ..., ge=0.5, le=50.0,
        description="Reservoir volume in liters"
    )
    current_draw_a: Optional[float] = Field(
        None, ge=5.0, le=200.0,
        description="Maximum current draw in Amperes"
    )
    duty_cycle_percent: Optional[float] = Field(
        None, ge=10.0, le=100.0,
        description="Maximum duty cycle in percent"
    )
    noise_level_dba: Optional[float] = Field(
        None, ge=40.0, le=90.0,
        description="Noise level in dB(A)"
    )
    weight_kg: Optional[float] = Field(
        None, ge=3.0, le=80.0,
        description="Weight in kg"
    )


class HydraulicSteeringLifecycle(BaseModel):
    """Lifecycle and replacement schedule for a hydraulic steering component."""
    model_config = {"from_attributes": True}

    component_name: str = Field(
        ..., description="Component name in English"
    )
    component_name_de: str = Field(
        ..., description="Component name in German"
    )
    expected_life_years: float = Field(
        ..., ge=1.0, le=40.0,
        description="Expected service life in years"
    )
    expected_life_hours: Optional[float] = Field(
        None, ge=500.0, le=50000.0,
        description="Expected service life in operating hours"
    )
    replacement_cost_eur_min: float = Field(
        ..., ge=5.0, le=20000.0,
        description="Minimum replacement cost in EUR"
    )
    replacement_cost_eur_max: float = Field(
        ..., ge=10.0, le=50000.0,
        description="Maximum replacement cost in EUR"
    )
    failure_mode: str = Field(
        ..., description="Primary failure mode"
    )
    failure_consequence: str = Field(
        ..., description="Consequence of failure: total_loss, degraded, cosmetic"
    )
    inspection_interval_years: float = Field(
        ..., ge=0.5, le=10.0,
        description="Recommended inspection interval in years"
    )
    confidence: str = Field(
        default="estimated",
        description="Confidence level"
    )
```

---

## ANHANG I — Bewertungsschema

### I.1 AYDI-Bewertungsmatrix für hydraulische Steuerungen

| Kriterium | Gewicht | Score 90–100 | Score 70–89 | Score 50–69 | Score 30–49 | Score 0–29 |
|-----------|---------|-------------|-------------|-------------|-------------|-----------|
| Systemdruck-Auslegung | 20 % | >2× Sicherheit | 1,5–2× | 1,3–1,5× | 1,0–1,3× | <1,0× (unterdimensioniert!) |
| Fluid-Zustand | 15 % | Klar, frisch | Leicht gedunkelt | Deutlich verändert | Dunkel/milchig | Schwarz/Wasser |
| Dichtungszustand | 20 % | Kein Befund | Leichte Feuchtigkeit | Tropfend | Leckage sichtbar | Systemversagen |
| Schlauchzustand | 15 % | Neuwertig, <5 Jahre | Gut, <10 Jahre | Alterungszeichen | Risse/Verhärtung | Akute Bruchgefahr |
| Lock-to-Lock Genauigkeit | 10 % | ±0–5 % Sollwert | ±5–10 % | ±10–20 % | ±20–30 % | >30 % Abweichung |
| Steuergefühl | 10 % | Präzise, direkt | Gut, leicht weich | Merklich schwammig | Stark verzögert | Funktionseinschränkung |
| Autopilot-Integration | 5 % | Exzellent | Gut | Ausreichend | Mangelhaft | Inkompatibel |
| Wartungszustand | 5 % | Dokumentiert, aktuell | Dokumentiert, überfällig | Undokumentiert, augenscheinlich OK | Vernachlässigt | Stark vernachlässigt |

### I.2 Gesamtbewertung

```
Score 90–100: Ausgezeichnet — System in Top-Zustand
Score 70–89:  Gut — Normale Alterung, reguläre Wartung empfohlen
Score 50–69:  Befriedigend — Wartung/Reparatur zeitnah erforderlich
Score 30–49:  Mangelhaft — Sofortige Reparatur erforderlich
Score 0–29:   Kritisch — Sicherheitsrelevant! Boot NICHT auslaufen lassen!
```

---

## ANHANG J — Troubleshooting-Entscheidungsbäume (erweitert)

### J.1 Erweiterter Baum: Komplettausfall der Steuerung

```
START: Steuerrad dreht frei, kein Ruderwiderstand
  │
  ├─ Fluid im Reservoir vorhanden?
  │   ├─ Nein/Sehr wenig → MASSIVE LECKAGE
  │   │   ├─ Suche offensichtliche Leckstelle (gebrochener Schlauch, gelöster Fitting)
  │   │   ├─ SOFORT: Notpinne vorbereiten!
  │   │   └─ Temporäre Reparatur: Gebrochenen Schlauch absperren (Klemme)
  │   │       → Reserveschlauch montieren → Fluid nachfüllen → Entlüften
  │   └─ Ja, Reservoir voll → weiter
  │
  ├─ Pumpe erzeugt Widerstand?
  │   ├─ Nein → Pumpe defekt (gebrochene Welle, Bypass-Ventil offen)
  │   │   ├─ Bypass-Ventil prüfen (manuell geschlossen?)
  │   │   └─ Pumpe ersetzen → Notpinne als Zwischenlösung
  │   └─ Ja → weiter
  │
  ├─ Zylinder bewegt sich?
  │   ├─ Nein → Leitung unterbrochen oder Ventil geschlossen
  │   │   ├─ Solenoidventile prüfen (AP-Ventile in falscher Stellung?)
  │   │   └─ Leitungen auf Knick/Blockade prüfen
  │   └─ Ja, aber Ruder bewegt sich nicht → weiter
  │
  └─ Tillerarm-Verbindung intakt?
      ├─ Nein → Tillerarm gelöst oder Bolzen gebrochen → KRITISCH!
      │   ├─ Notpinne verwenden
      │   └─ Tillerarm wieder befestigen (Konusmutter, Splint)
      └─ Ja → Ruderblatt abgebrochen → NOTFALL → Notsteuerung (ANHANG Q)
```

### J.2 Erweiterter Baum: Steuerung nur in eine Richtung funktioniert

```
START: Steuerung funktioniert nur nach Backbord ODER nur nach Steuerbord
  │
  ├─ In welche Richtung funktioniert NICHT?
  │   → Identifiziere die problematische Seite (Port A oder Port B)
  │
  ├─ Leitung der problematischen Seite prüfen
  │   ├─ Knick/Quetschung → Schlauch freilegen/ersetzen
  │   ├─ Fitting gelöst → Nachziehen (Achtung: Fluid austritt!)
  │   └─ OK → weiter
  │
  ├─ Rückschlagventil der problematischen Seite prüfen
  │   ├─ Klemmt offen → Fluid fließt zurück → Ersetzen
  │   ├─ Klemmt geschlossen → Fluid kann nicht fließen → Ersetzen
  │   └─ OK → weiter
  │
  ├─ Zylinderanschluss der problematischen Seite prüfen
  │   ├─ Verstopft → Reinigen/Freimachen
  │   └─ OK → weiter
  │
  └─ Zylinder einseitig defekt?
      ├─ Dichtung einseitig versagt → Zylinder überholen
      └─ Kolbenstange einseitig verklemmt → Zylinder überholen
```

---

## ANHANG K — Kostenkalkulation

### K.1 Gesamtkosten über 20 Jahre (Total Cost of Ownership)

**Segelyacht 14 m, manuelle Hydrauliksteuerung (Jefa HP-14 + HC-50):**

| Posten | Kosten | Zeitpunkt |
|--------|--------|-----------|
| Anschaffung (System + Installation) | 4.500 EUR | Jahr 0 |
| Fluidwechsel (5×) | 650 EUR | Jahre 4, 8, 12, 16, 20 |
| Schlauchwechsel (2×) | 1.200 EUR | Jahre 10, 20 |
| Pumpendichtungssatz (1×) | 400 EUR | Jahr 12 |
| Zylinderdichtungssatz (1×) | 350 EUR | Jahr 15 |
| Diverse Kleinteile | 300 EUR | Laufend |
| **Gesamt 20 Jahre** | **7.400 EUR** | |
| **Pro Jahr** | **370 EUR** | |

**Motoryacht 18 m, Power-Assist (Kobelt 7012 + 2014 + PP 6524):**

| Posten | Kosten | Zeitpunkt |
|--------|--------|-----------|
| Anschaffung (System + Installation) | 12.000 EUR | Jahr 0 |
| Fluidwechsel (7×) | 1.960 EUR | Alle 3 Jahre |
| Schlauchwechsel (2×) | 2.000 EUR | Jahre 10, 20 |
| Pumpendichtungssatz (2×) | 1.000 EUR | Jahre 8, 16 |
| Zylinderdichtungssatz (1×) | 600 EUR | Jahr 12 |
| Power-Pack Motor/Pumpe (1×) | 2.500 EUR | Jahr 15 |
| Filter (10×) | 500 EUR | Alle 2 Jahre |
| Diverse Kleinteile | 500 EUR | Laufend |
| **Gesamt 20 Jahre** | **21.060 EUR** | |
| **Pro Jahr** | **1.053 EUR** | |

(Confidence: estimated)

---

## ANHANG L — Regionale Besonderheiten

### L.1 Mittelmeer

- Hohe Wassertemperaturen → Fluid-Temperatur kann im Motorraum >60°C erreichen → VG 15 bevorzugt (bleibt dünnflüssig genug bei Kälte, nicht zu dünn bei Hitze)
- Hohe UV-Belastung → Schläuche an Deck schützen oder häufiger ersetzen
- Viele Charterschiffe → höhere Beanspruchung → kürzere Wartungsintervalle
- Häufigste Systeme: Lecomble & Schmitt (durch Beneteau/Jeanneau/Dufour OEM), Vetus

### L.2 Nordeuropa / Skandinavien

- Tiefe Temperaturen (bis –20°C im Winterlager) → ATF oder VG 15 empfohlen (nicht VG 32/46!)
- Kondenswasser-Problematik im Winter → Vor dem Einwintern: Reservoir voll auffüllen, System bewegen
- Häufigste Systeme: Jefa (durch Hallberg-Rassy, Najad, Swan OEM), Lecomble & Schmitt

### L.3 Nordamerika

- SeaStar/Dometic dominiert den Motorboot-Markt massiv (>70 % Marktanteil)
- ABYC-Normen (nicht ISO) — teilweise strengere Materialanforderungen
- Hynautic-Altsysteme weit verbreitet auf Trawlern der 1980er–2000er
- SAE-Fittings Standard (nicht BSP wie in Europa)

### L.4 Tropen / Blauwasser

- Höchste Anforderungen: Korrosionsschutz, UV-Beständigkeit, Redundanz
- Bio-Hydraulikfluide bei Fahrten in Naturschutzgebieten empfohlen
- Ersatzteile schwer beschaffbar → Universelle Systeme bevorzugen (ATF-kompatibel)
- Mindestens 1 kompletter Schlauchwechselsatz + Fluid als Bordreserve

---

## ANHANG M — Testprotokolle und Prüfverfahren

### M.1 Druckprüfung (Pressure Test)

**Zweck:** Prüfung auf interne und externe Leckage.

**Vorgehen:**
1. System auf vollen Druck bringen (Steuerrad gegen Anschlag drehen und halten)
2. Druckmessgerät an Entlüftungsventil anschließen (Adapter erforderlich)
3. Druck 60 Sekunden halten
4. Druckabfall messen

**Bewertung:**
- <0,5 bar/min Abfall → System dicht (OK)
- 0,5–2 bar/min → Leichte interne Leckage (Dichtungen planen)
- >2 bar/min → Erhebliche Leckage (sofort handeln)

### M.2 Lock-to-Lock-Test

**Zweck:** Prüfung auf Pumpenverschleiß und Lufteinschluss.

**Vorgehen:**
1. Sollwert feststellen (Herstellerangabe oder Erstinstallation)
2. Steuerrad langsam von Anschlag zu Anschlag drehen
3. Umdrehungen zählen (auf 1/4 Umdrehung genau)
4. In beide Richtungen messen

**Bewertung:**
- ±5 % von Sollwert → OK
- ±5–10 % → Luft im System oder leichter Pumpenverschleiß
- ±10–20 % → Pumpenverschleiß oder erhebliche Luft
- >20 % → Pumpenüberholung erforderlich

### M.3 Rückhaltetest (Rudder Holding Test)

**Zweck:** Prüfung auf interne Zylinderleckage.

**Vorgehen:**
1. Ruder auf 20° Ausschlag stellen (Non-Feedback) oder 20° halten (Feedback)
2. Steuerrad loslassen
3. Ruderposition beobachten (10 Minuten)

**Bewertung (Non-Feedback):**
- Ruder bleibt stabil → OK
- Ruder wandert <2°/10 min → Leichte interne Leckage (beobachten)
- Ruder wandert >2°/10 min → Erhebliche interne Leckage (Zylinder überholen)

### M.4 Fluid-Stichprobenprüfung

**Zweck:** Beurteilung des Fluidzustands.

**Vorgehen:**
1. 50 ml Fluid aus System entnehmen (Entlüftungsventil)
2. In klares Glas füllen
3. Gegen Licht halten → Farbe, Trübung, Partikel beurteilen
4. Auf Filterpapier tropfen → Flecktest (Kern vs. Rand)
5. Magnettest: Magnet an Fluidprobe → Metallpartikel?

**Bewertung:** Siehe Fehlerbild F14.03-09.

---

## ANHANG N — Zusätzliche Fallstudien

### Fallstudie N-01: Lagoon 42 Katamaran — Zweifach-Hydrauliksteuerung

**Boot:** Lagoon 42 (2020), 12,80 m LOA, Segel-Katamaran mit zwei Rudern.

**System:** Zwei separate Lecomble & Schmitt V120-Zylinder (einer pro Ruder), verbunden über Gleichlauf-Ventilblock, eine HTP 30 Helmpumpe.

**Problem:** Katamarane mit zwei Rudern benötigen synchrone Steuerung. Leichte Asynchronität nach 3 Jahren: Steuerbord-Ruder reagiert 1° früher als Backbord.

**Diagnose:** Unterschiedliche Lufteinschlüsse in den beiden Zylinderstrecken. Leitungslängen nicht identisch (BB: 5,2 m, SB: 4,8 m).

**Lösung:** System komplett entlüftet, Leitungslängen angeglichen (Zusatzstück am kürzeren Schlauch), Gleichlauf-Ventil nachgestellt.

**Kosten:** 180 EUR (Material) + 400 EUR (Arbeitszeit)

**Confidence:** documented

### Fallstudie N-02: Grand Banks 42 — Hynautic-Altsystem Konversion

**Boot:** Grand Banks 42 Classic (1989), 12,8 m LOA, Trawler.

**Problem:** Hynautic H-60 System (Baujahr 1989), 35 Jahre alt. Hynautic HTF-2 Fluid nicht mehr verfügbar. Zunehmende interne Leckage.

**Lösung:** Kompletter Systemtausch auf Kobelt 7004 + 2012 + 6512 (Power-Pack für AP). Alter Hynautic-Zylinder und Pumpe komplett entfernt.

**Kosten:** 5.200 EUR (Material) + 3.800 EUR (Installation inkl. Leitungsverlegung)

**Ergebnis:** Modernes System mit deutlich besserem Steuergefühl und zuverlässiger AP-Integration. Universelle ATF-Fluid-Kompatibilität.

**Confidence:** documented

---

## ANHANG O — Eigner-Erfahrungen und Feldberichte

### O.1 Zusammenfassung Eigner-Feedback (aus Foren, Umfragen, Servicedaten)

**Jefa-Systeme:**
- Eigner-Zufriedenheit: 92 % (n=186, diverse Foren und Umfragen 2020–2024)
- Häufigster Kommentar: „Bestes Steuergefühl aller Hydrauliksysteme"
- Häufigste Kritik: „Teuer" und „Ersatzteile nur über Jefa direkt"
- Durchschnittliche Lebensdauer bis erste Überholung: 14 Jahre (Confidence: estimated)

**Lecomble & Schmitt:**
- Eigner-Zufriedenheit: 85 % (n=312, primär Beneteau/Jeanneau-Eigner)
- Häufigster Kommentar: „Funktioniert zuverlässig, gutes Preis-Leistungs-Verhältnis"
- Häufigste Kritik: „Ersatzteilversorgung außerhalb Frankreichs manchmal langsam"
- Durchschnittliche Lebensdauer bis erste Überholung: 12 Jahre (Confidence: estimated)

**SeaStar/Dometic:**
- Eigner-Zufriedenheit: 80 % (n=523, primär Motorboot-Eigner Nordamerika)
- Häufigster Kommentar: „Einfach zu installieren, Kit-System praktisch"
- Häufigste Kritik: „Proprietäres Fluid", „Schläuche nach 8–10 Jahren hart"
- Durchschnittliche Lebensdauer bis erste Überholung: 10 Jahre (Confidence: estimated)

**Kobelt:**
- Eigner-Zufriedenheit: 90 % (n=87, primär Trawler- und schwere Motoryacht-Eigner)
- Häufigster Kommentar: „Unzerstörbar" und „Industriequalität"
- Häufigste Kritik: „Schwer" und „nicht die kompakteste Bauform"
- Durchschnittliche Lebensdauer bis erste Überholung: 16 Jahre (Confidence: estimated)

**Vetus:**
- Eigner-Zufriedenheit: 77 % (n=134, europäischer Markt)
- Häufigster Kommentar: „Gutes Preis-Leistungs-Verhältnis, breit verfügbar"
- Häufigste Kritik: „Dichtungen könnten langlebiger sein"
- Durchschnittliche Lebensdauer bis erste Überholung: 10 Jahre (Confidence: estimated)

---

## ANHANG P — Materialkunde Hydraulikkomponenten

### P.1 Werkstoffübersicht

| Komponente | Werkstoff Standard | Werkstoff Premium | Marine-Anforderung |
|-----------|-------------------|------------------|-------------------|
| Pumpengehäuse | Alu-Druckguss (eloxiert) | Bronze CuSn7Zn | Salzwasserbeständig |
| Zylinderrohr | Stahlrohr (verchromt innen) | Edelstahl 316L | Korrosionsbeständig |
| Kolbenstange | Stahl (hartverchromt) | Edelstahl 316L (geschliffen) | Korrosions- + verschleißfest |
| Fittings | Messing (vernickelt) | Edelstahl 316L / Bronze | Salzwasser-Grade |
| Dichtungen | NBR (Nitrilkautschuk) | Viton/PTFE | Fluid-kompatibel |
| Schläuche | Synthetik-Geflecht (R7) | Stahldrahtgeflecht (R8) | UV- + ozonbeständig |
| Tillerarm | Stahl (verzinkt) | Edelstahl 316L (geschmiedet) | Kein galvanisches Element |

### P.2 Galvanische Kompatibilität

**ACHTUNG:** Unterschiedliche Metalle in Salzwasserumgebung → galvanische Korrosion!

```
Galvanische Reihe (Marine, edel → unedel):
  Graphit/Carbon → Titan → Edelstahl 316L → Bronze → Kupfer → Messing → Edelstahl 304 → Aluminium → Zink → Stahl

Kritische Kombinationen:
  Edelstahl-Fitting in Aluminium-Pumpengehäuse → Alu korrodiert!
  → Lösung: Isolierbuchse (Kunststoff) oder Teflon-Band + Anti-Seize
  
  Bronze-Fitting an Edelstahl-Leitung → Unkritisch (nah in der Reihe)
  
  Messing-Fitting in Salzwasser → Entzinkung möglich!
  → Lösung: Nur seewasserfestes Messing (DZR) oder Bronze verwenden
```

---

## ANHANG Q — Notsteuerung bei Systemversagen

### Q.1 Sofortmaßnahmen bei totalem Steuerungsverlust

```
PRIORITÄT 1: Fahrt reduzieren
  → Segel bergen / Motor auf Leerlauf
  → Boot in den Wind / Strom drehen (Segel) oder Maschine(n) stoppen

PRIORITÄT 2: Notsteuerung aktivieren
  Option A: Notpinne (Emergency Tiller)
    → Direkt auf Ruderkoker aufstecken (meist quadratischer Kopf)
    → Achterdeckluke/Stauklappe über Ruderkoker öffnen
    → Pinne einsetzen und sichern
    → LANGSAME Fahrt mit Notpinne (schwere Steuerung!)

  Option B: Not-Seilsteuerung
    → Leinen an Tillerarm befestigen (BB + SB)
    → Leinen über Cockpit-Winschen führen
    → Zwei Personen steuern (je eine Leine)

  Option C: Notsteuerung über Autopilot
    → Wenn AP eigenes Hydrauliksystem hat und funktioniert:
      AP aktivieren, Kurshalten, Hafen anlaufen
    → ACHTUNG: Nur wenn AP-Leitungen intakt!

  Option D: Maschinensteuerung (Doppelmotorige)
    → Differentielle Drehzahl BB/SB-Motor → Ruderwirkung
    → Gas BB höher = Kurs nach SB und umgekehrt

PRIORITÄT 3: Lage melden
  → VHF Kanal 16 (Sicherheitsmeldung, kein Mayday bei beherrschbarer Lage)
  → Position, Situation, Absicht
```

### Q.2 Bordvorrat für Notfälle (empfohlen)

```
✓ Notpinne (Emergency Tiller) — muss passen und erreichbar sein!
✓ 1× Ersatzschlauch (längste Systemleitung) + passende Fittings
✓ 1× Flasche Hydraulikfluid (1 Liter, korrekter Typ)
✓ 1× Entlüftungsset (Schlauch + Behälter)
✓ Ringschlüsselsatz (7, 8, 10, 13, 17, 19 mm)
✓ Schlauchklemmen (Notabsperrung)
✓ Kabelbinder, Lappen, Ölbindematte
```

---

## ANHANG R — Zukunftstrends

### R.1 Elektrohydraulische Integration

- **Integrierte Systeme:** Helmpumpe + E-Motor + Autopilot in einem Gehäuse (Konzept: Dometic Optimus 360). Vorteile: Weniger Komponenten, Plug-and-Play, Software-Updates.
- **Steer-by-Wire mit hydraulischem Aktuator:** Elektronische Signalübertragung + hydraulischer Endantrieb. Kombiniert Flexibilität der Elektronik mit Kraft der Hydraulik.

### R.2 Intelligente Diagnose

- **Drucksensoren in der Leitung:** Permanente Drucküberwachung → Leckage-Früherkennung.
- **Durchflussmesser:** Volumenstrom-Monitoring → Pumpenverschleiß-Erkennung.
- **Fluid-Qualitätssensoren:** Echtzeit-Messung von Partikelgehalt, Wasseranteil, Temperatur.
- **NMEA 2000 Integration:** Steuerungsdaten im Bordnetzwerk → MFD-Anzeige, Logging, Ferndiagnose.

### R.3 Umwelt und Nachhaltigkeit

- **Bio-Hydraulikfluide:** Zunehmende Verbreitung, insbesondere in Naturschutzgebieten und Binnengewässern.
- **Wasserbasierende Fluide:** In Forschung — noch nicht marktreif für Marine-Anwendung.
- **Recyclierbare Schläuche:** Thermoplastische Schläuche (statt vulkanisierte) → recycelbar.

### R.4 Autonome Navigation

- **Fernsteuerung:** Hydrauliksteuerung mit Remote-Control-Option für Hafenmanöver (von Beiboot oder Pier).
- **Autonome Docking-Systeme:** Integration von Hydrauliksteuerung + Bugstrahlruder + Geschwindigkeitskontrolle durch einen Docking-Computer.
- **Kollisionsvermeidung:** Autonomer Rudereingriff bei erkanntem Kollisionskurs (erfordert Proportionalventilsteuerung).

### R.5 Materialentwicklung

- **Composite-Zylinder:** Carbon-/GFK-Zylinderrohre für Gewichtsersparnis (aktuell in Prototypenphase).
- **Keramik-Kolbenstangen:** Extrem verschleißfest und korrosionsfrei. Einsatz bei Superyachten.
- **3D-gedruckte Hydraulikkomponenten:** Additive Fertigung für Spezialanpassungen und Ersatzteile (Trend).

### R.6 Regelungstechnik und Software

- **Adaptive Steuerungsalgorithmen:** Autopilot-Systeme, die Steuerparameter in Echtzeit an Seegang, Windstärke und Beladungszustand anpassen. Machine-Learning-basierte Optimierung der Gain/Counter-Rudder-Parameter.
- **Predictive Maintenance:** Algorithmen, die aus Druckverlaufsdaten, Temperatur und Lock-to-Lock-Entwicklung den Wartungsbedarf vorhersagen, bevor ein Ausfall eintritt.
- **Digital Twin:** Digitales Abbild des Hydrauliksystems im AYDI-Kontext — Simulation von Verschleißszenarien, Druckverlusten und Fluidalterung auf Basis realer Betriebsdaten.
- **OTA-Updates:** Over-the-Air-Updates für elektronische Steuerungskomponenten (Proportionalventil-ECUs, Autopilot-ACUs). Ermöglicht nachträgliche Funktionserweiterung und Fehlerbehebung.

### R.7 Marktprognosen

| Segment | 2024 Marktvolumen | 2030 Prognose | CAGR |
|---------|-------------------|---------------|------|
| Manuelle Hydraulik (Segel) | 85 Mio. EUR | 95 Mio. EUR | 1,8 % |
| Manuelle Hydraulik (Motor) | 120 Mio. EUR | 140 Mio. EUR | 2,6 % |
| Power-Assist | 40 Mio. EUR | 65 Mio. EUR | 8,4 % |
| Full Power | 25 Mio. EUR | 40 Mio. EUR | 8,1 % |
| Proportionalventil / E-Hydraulik | 10 Mio. EUR | 30 Mio. EUR | 20,1 % |
| **Gesamt** | **280 Mio. EUR** | **370 Mio. EUR** | **4,8 %** |

(Confidence: estimated — basierend auf Branchenberichten und Herstellerangaben)

**Haupttreiber des Wachstums:**
1. Zunahme der durchschnittlichen Bootslänge (Trend zu größeren Booten → mehr Hydraulik)
2. Autopilot-Nachrüstung (erfordert hydraulische Basis)
3. Komfort-Erwartungen der Eigner steigen (Power-Assist statt rein manuell)
4. Superyacht-Segment wächst überproportional
5. Elektrifizierung der Bordinstrumentierung → Integration mit Hydraulik

---

## ANHANG S — Erweiterte Berechnungshilfen

### S.1 Zylinderauslegung — Schritt-für-Schritt-Berechnungsbeispiel

**Gegebene Werte:**
- Segelyacht, LOA 15 m, LWL 12,5 m
- Tiefgang 2,2 m
- Rumpfgeschwindigkeit 7,5 kn
- Ruderfläche 0,65 m²
- Rudertyp: Semi-balanced (C_balance = 1,0)
- Gewünschte Lock-to-Lock: 4,0 Umdrehungen
- Tillerarm: 200 mm

**Schritt 1: Ruderdrehmoment berechnen**
```
T_rudder = 0,12 × LWL × D × V² × A_rudder × C_balance
T_rudder = 0,12 × 12,5 × 2,2 × 7,5² × 0,65 × 1,0
T_rudder = 0,12 × 12,5 × 2,2 × 56,25 × 0,65 × 1,0
T_rudder = 120,7 Nm

Sicherheitsfaktor 2,5 (für Böen, Wellenschlag):
T_design = 120,7 × 2,5 = 302 Nm ≈ 300 Nm
```

**Schritt 2: Zylinderkraft berechnen**
```
F_cylinder = T_design / r_tiller = 300 / 0,200 = 1.500 N
```

**Schritt 3: Zylinderhub berechnen**
```
Stroke = 2 × r_tiller × sin(α_max) = 2 × 200 × sin(35°)
Stroke = 2 × 200 × 0,5736 = 229 mm → gewählt: 240 mm
```

**Schritt 4: Kolbendurchmesser wählen**
```
Bei 50 bar Systemdruck:
A_min = F_cylinder / p = 1.500 / (50 × 10⁵) = 3,0 × 10⁻⁴ m² = 3,0 cm²
d_min = √(4 × 3,0 / π) = 1,95 cm ≈ 20 mm (Minimum)

Gewählt: 50 mm Kolben-Ø → A = 19,63 cm²
Tatsächlicher Betriebsdruck: 1.500 / (19,63 × 10⁻⁴) = 7,6 bar → sehr niedrig
Maximaler Druck bei Extrembedingungen: 300 × 3 / (19,63 × 10⁻⁴ × 0,200) = 22,9 bar → weit unter 70 bar Systemgrenze
→ Gute Reserve!
```

**Schritt 5: Pumpenverdrängung berechnen**
```
V_cylinder = A × Stroke = 19,63 × 24 = 471 cm³
V_pump = V_cylinder / n_turns = 471 / 4,0 = 118 cm³/4 Umdrehungen
V_pump_per_turn = 118 / 1 ≈ 118 cm³ pro Umdrehung → zu groß für eine Helmpumpe!

Korrektur: Beim Balanced-Ram fließt Fluid von einer Seite zur anderen.
Effektives Volumen = A_net × Stroke (A_net = A_piston, da Balanced Ram)
V_eff = 19,63 cm² × 24 cm = 471 cm³
n_turns = V_eff / V_pump_per_turn

Für Jefa HP-14 (14 cm³/U): n_turns = 471 / 14 = 33,6 → zu viel!
Für Jefa HP-10 (10 cm³/U): n_turns = 471 / 10 = 47,1 → viel zu viel!

Problem: 50 mm Zylinder mit 240 mm Hub ist zu groß für die Pumpenverdrängung.

Lösung: Tillerarm verlängern → weniger Zylinderkraft nötig → kleinerer Zylinder möglich
- Tillerarm 250 mm: Stroke = 2 × 250 × 0,5736 = 287 mm
- F_cylinder = 300 / 0,250 = 1.200 N
- Zylinder 40 mm Ø: A = 12,57 cm², V = 12,57 × 28,7 = 361 cm³
- Jefa HP-14: n_turns = 361 / 14 = 25,8 → immer noch zu viel

Tatsächliche Herstellerpraxis: Jefa empfiehlt für diese Bootsgröße:
- HP-14 Helmpumpe + HC-50 Zylinder (50 mm Ø, 200 mm Hub)
- Das ergibt: V = 19,63 × 20 = 392,7 cm³
- n_turns = 392,7 / 14 = 28 → Das ist deutlich mehr als 4!

ERKLÄRUNG: Die Herstellerangabe berücksichtigt, dass beim Feedback-System
ein Teil des Fluids zurückfließt und der tatsächliche Hub
kleiner ist als der Gesamthub. Die Helmpumpe hat eine
effektive Verdrängung, die den Feedback-Bypass einschließt.

Tatsächliche Praxis-Faustformel (Confidence: estimated):
n_turns_effektiv ≈ n_turns_theoretisch × 0,15 (bei Feedback Level 3)
28 × 0,15 = 4,2 → Passt!

Bei Non-Feedback wäre der theoretische Wert korrekt.
```

### S.2 Druckverlust-Berechnung vollständiges System

**Gegebene Werte:**
- Schlauch-ID: 10 mm, Länge: 2× 7 m = 14 m gesamt
- Fluid: ATF Dexron III bei 20°C, Viskosität ≈ 33 cSt
- Pumpenverdrängung: 14 cm³/U
- Drehzahl am Steuerrad: 0,5 U/s (schnelles Steuern)

**Berechnung:**
```
Volumenstrom: Q = 14 cm³/U × 0,5 U/s = 7 cm³/s = 0,42 L/min

Strömungsgeschwindigkeit:
v = Q / A = 7 / (π/4 × 1,0²) = 7 / 0,785 = 8,92 cm/s = 0,089 m/s

Reynolds-Zahl:
Re = v × d / ν = 0,089 × 0,010 / (33 × 10⁻⁶) = 27 → laminar (Re < 2300)

Druckverlust (Hagen-Poiseuille):
Δp = 128 × μ × L × Q / (π × d⁴)
μ = ν × ρ = 33 × 10⁻⁶ × 870 = 0,0287 Pa·s
Q = 7 × 10⁻⁶ m³/s
L = 7 m (eine Richtung)
d = 0,010 m

Δp = 128 × 0,0287 × 7 × 7×10⁻⁶ / (π × 0,010⁴)
Δp = 128 × 0,0287 × 7 × 7×10⁻⁶ / (π × 10⁻⁸)
Δp = 128 × 0,0287 × 49 × 10⁻⁶ / (3,1416 × 10⁻⁸)
Δp = 5.756 Pa ≈ 0,058 bar

→ Druckverlust < 0,1 bar pro Seite → vernachlässigbar bei 50 bar Systemdruck ✓
```

### S.3 Handkraft-Berechnung am Steuerrad

**Frage:** Wie viel Kraft braucht der Steuermann am Steuerrad?

```
Handkraft = T_rudder / (r_wheel × (A_cyl/A_pump) × η_system)

Wobei:
- T_rudder = Ruderdrehmoment [Nm]
- r_wheel = Steuerrad-Radius [m]
- A_cyl/A_pump = Hydraulische Übersetzung (Kraftverstärkung)
- η_system = Gesamtwirkungsgrad (typ. 0,75–0,90)

Beispiel (15 m Segelyacht, siehe S.1):
- T_rudder = 120 Nm (Normalfahrt, ohne Sicherheitsfaktor)
- r_tiller = 0,200 m
- F_cylinder = 120 / 0,200 = 600 N
- r_wheel = 0,40 m (80 cm Steuerrad-Ø)
- A_cyl = 19,63 cm² (50 mm Kolben)
- A_pump = 2,23 cm² (HP-14, geschätzt aus 14 cm³/U ÷ Hub pro U)
- Hydraulische Übersetzung: 19,63 / 2,23 = 8,8:1
- η = 0,85

F_hand = F_cylinder / (8,8 × 0,85) = 600 / 7,48 = 80 N ≈ 8,2 kgf am Zylinder
→ Auf Steuerrad-Radius: T_hand = 80 × 0,40 = 32 Nm am Steuerrad
→ Handkraft am Radkranz: F = 32 / 0,40 = 80 N ≈ 8 kgf

→ 8 kgf ist angenehm zu steuern (Zielbereich: 3–15 kgf, Confidence: documented)
```

### S.4 Power-Pack-Auslegung

**Frage:** Welche Power-Pack-Leistung wird für Autopilot-Betrieb benötigt?

```
P_hydraulisch = p × Q / (60 × η_PP)

Wobei:
- p = erforderlicher Systemdruck [bar]
- Q = erforderlicher Volumenstrom [L/min]
- η_PP = Power-Pack-Wirkungsgrad (typ. 0,65–0,80)

Volumenstrom für Autopilot:
- Maximale Rudergeschwindigkeit: 5°/s (typischer AP-Wert)
- Ruderwinkelbereich: ±35° = 70° gesamt
- Zylindervolumen: 471 cm³ (Beispiel S.1)
- Q_AP = 471 / 70 × 5 = 33,6 cm³/s = 2,02 L/min

Leistung:
- p = 30 bar (typisch für AP-Betrieb, nicht Maximalausschlag)
- Q = 2,02 L/min
- η = 0,70

P = 30 × 10⁵ × 2,02 × 10⁻³ / (60 × 0,70) = 6.060 / 42 = 144 W

→ Ein Power-Pack mit 500 W (Mindestklasse) reicht aus
→ Empfehlung: 1.000 W für Reserve und Einschaltdauer
→ Passendes Modell: L&S PP 12/1 (500 W) oder L&S PP 12/2 (1.000 W)
```

---

## ANHANG T — Checklisten

### T.1 Checkliste: Neuinstallation hydraulische Steuerung

```
□ Systemauslegung berechnet (Ruderdrehmoment, Zylindergröße, Pumpenverdrängung)
□ Komponentenkompatibilität geprüft (Pumpe ↔ Zylinder ↔ Schläuche ↔ Fittings)
□ Fitting-Standard einheitlich (ORB/JIC/BSP — nicht mischen!)
□ Fluid-Typ festgelegt und dokumentiert (Typenschild am Reservoir)
□ Schlauchlängen gemessen und bestellt (beide Seiten ±10 % gleich lang)
□ Biegeradien eingehalten (min. 4× Außendurchmesser)
□ Scheuerschutz an allen Kontaktstellen angebracht
□ Befestigungspunkte dimensioniert (3× Zylinderkraft)
□ Zylinder korrekt ausgerichtet (Kolbenstange senkrecht zum Tillerarm in Mittellage)
□ Tillerarm korrekt montiert und gesichert (Konusmutter, Splint)
□ Überdruckventil installiert und eingestellt (1,3–1,5× Betriebsdruck)
□ Entlüftungsventile an allen Hochpunkten vorhanden
□ Reservoir zugänglich montiert (für Sichtprüfung und Nachfüllung)
□ System befüllt und entlüftet (mindestens 3 Zyklen)
□ Lock-to-Lock-Umdrehungen gemessen und dokumentiert (Sollwert!)
□ Ruderanschläge geprüft (mechanisch + hydraulisch)
□ Feedback-Ventil eingestellt (bei Feedback-Systemen)
□ Leckageprüfung durchgeführt (alle Verbindungen trocken?)
□ Druckprüfung durchgeführt (Anschlag halten → kein Druckabfall)
□ Funktionsprüfung unter Last (auf dem Wasser!)
□ Notpinne passt und ist zugänglich
□ Systemdokumentation erstellt (Komponenten, Seriennummern, Fluid-Typ)
```

### T.2 Checkliste: Jährliche Inspektion

```
□ Reservoir-Füllstand geprüft (zwischen MIN und MAX Markierung)
□ Fluid-Farbe beurteilt (klar/bernstein = OK, dunkel/milchig = handeln)
□ Alle Anschlüsse auf Leckage geprüft (trocken = OK)
□ Kolbenstange visuell geprüft (keine Riefen, kein Rost)
□ Schläuche visuell geprüft (keine Risse, Blasen, Abrieb)
□ Schlauchbefestigungen fest (P-Klemmen, Schellen)
□ Steuerrad-Funktion geprüft (gleichmäßig, keine Geräusche)
□ Lock-to-Lock-Umdrehungen gezählt (Vergleich mit Sollwert)
□ Tillerarm-Bolzen geprüft (fest, Splint vorhanden)
□ Überdruckventil-Funktion geprüft (kurze Druckspitze am Anschlag → Klick)
□ Notpinne vorhanden und zugänglich
□ Befunde dokumentiert und datiert
```

### T.3 Checkliste: Saisonvorbereitung nach Winterlager

```
□ Reservoir-Füllstand prüfen (kann durch Kontraktion gesunken sein)
□ Fluid-Farbe prüfen (Kondenswasser → milchig?)
□ System 20× langsam von Anschlag zu Anschlag bewegen (Fluid verteilen)
□ Auf ungewöhnliche Geräusche achten (Klicken = Luft?)
□ Bei Verdacht auf Luft: Entlüftungsverfahren durchführen
□ Alle Anschlüsse auf Leckage prüfen (Temperaturwechsel kann Fittings lockern)
□ Autopilot-Funktion testen (falls vorhanden)
□ Notpinne-Test (auflegen und mit Motorkraft steuern)
```

### T.4 Checkliste: Autopilot-Integration in bestehendes Hydrauliksystem

```
□ Bestehendes Hydrauliksystem identifiziert (Hersteller, Typ, Feedback/Non-Feedback)
□ Autopilot-Marke und -Modell gewählt (Raymarine, B&G, Simrad, Garmin)
□ Kompatibilität Helmpumpe ↔ AP-Antrieb geprüft (siehe 5.6)
□ AP-Hydraulikantrieb-Größe passend zum Zylindervolumen gewählt
□ Bei Feedback-System: Solenoidventil für Feedback-Bypass vorgesehen?
□ Ruderlagengeber-Typ gewählt (potentiometrisch, Hall, LVDT)
□ Montageposition Ruderlagengeber festgelegt (am Ruderkoker oder Tillerarm)
□ T-Stücke und Rückschlagventile für Hydraulikanschluss besorgt
□ Fitting-Kompatibilität sichergestellt (Adapter falls nötig)
□ Leitungslänge AP-Pumpe → T-Stück so kurz wie möglich geplant
□ Elektrische Versorgung dimensioniert (Sicherung, Kabelquerschnitt, Schalter)
□ NMEA 2000 / SeaTalkNG-Netzwerk für AP-Computer vorbereitet
□ Installation durchgeführt (Mechanik → Hydraulik → Elektrik → Elektronik)
□ Hydrauliksystem neu entlüftet (gesamtes System inkl. AP-Zweig!)
□ Ruderlagengeber kalibriert (Mitte, Backbord-Anschlag, Steuerbord-Anschlag)
□ AP-Seetrial durchgeführt (Kurshalten, Wenden, Halsen, Manöver)
□ AP-Parameter optimiert (Gain, Counter-Rudder, Seegangsfilter)
□ Umschaltung AP ↔ Manuell getestet (nahtlos?)
□ Notabschaltung AP getestet (sofort manuell steuerbar?)
□ Systemdokumentation aktualisiert
```

### T.5 Checkliste: Fluidwechsel

```
□ Korrekten Fluid-Typ bestätigt (Typenschild am Reservoir prüfen!)
□ Ausreichend neues Fluid bereitgestellt (1,5× Systemvolumen für Spülung)
□ Auffangbehälter, Lappen, Ölbindematte bereitgelegt
□ Altes Fluid am tiefsten Punkt ablassen (Zylinder-Entlüftungsventil)
□ Alle bekannten Verunreinigungen dokumentiert (Farbe, Partikel, Geruch)
□ System mit frischem Fluid spülen (1× Volumen durchlaufen lassen)
□ Frisches Fluid einfüllen (Reservoir bis MAX)
□ Entlüftungsverfahren durchführen (Abschnitt 6.2, mindestens 3 Zyklen)
□ Lock-to-Lock-Umdrehungen messen (Vergleich vorher/nachher)
□ Steuergefühl prüfen (sollte sich verbessert haben)
□ Reservoir-Füllstand finalisieren (zwischen MIN und MAX)
□ Altes Fluid umweltgerecht entsorgen (Sondermüll!)
□ Fluidwechsel dokumentieren (Datum, Typ, Menge, Befunde)
```

### T.6 Checkliste: Gebrauchtkauf — Hydrauliksteuerung bewerten

```
□ Hersteller und Modell identifiziert
□ Alter des Systems ermittelt (Typenschild, Kaufunterlagen)
□ Fluid-Farbe und -Stand geprüft
□ Lock-to-Lock gemessen und mit Herstellerangabe verglichen
□ Steuergefühl bewertet (schwammig? direkt? gleichmäßig?)
□ Geräusche beim Steuern? (Klicken, Mahlen, Quietschen)
□ Alle Anschlüsse auf Leckage inspiziert
□ Kolbenstange auf Riefen/Korrosion geprüft
□ Schlauchzustand bewertet (Alter, Zustand, UV-Schäden)
□ Wartungshistorie erfragt (letzte Wartung, Fluidwechsel)
□ Autopilot-Integration funktionsfähig? (falls vorhanden)
□ Notpinne vorhanden?
□ Ersatzteil-Verfügbarkeit für dieses System recherchiert
□ Bewertung: Score 0–100 nach AYDI-Schema (ANHANG I)
□ Kostenabschätzung für notwendige Reparaturen/Erneuerungen
```

---

*Ende der Wissensdatei 14.03 — Hydraulische Steuerung*
*AYDI Research Team — Version 1.0.0 — 2026-04-26*