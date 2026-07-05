# 31_08 — Kielkonstruktion

**Kategorie:** 31_Design_Konstruktion  
**Unterkategorie:** Kielkonstruktion  
**Version:** 2.0  
**Stand:** 2026-05-18  
**Relevanz:** Kern-Konstruktionswissen für Segelschiffe und Motorsegler

---

## Übersicht

Die Kielbauart bestimmt Stabilität, Performance, Grounding-Widerstandsfähigkeit und Baukosten fundamental. AYDI analysiert die **Auswahl und Dimensionierung der Kielform** sowie **Befestigung und Lastverteilung**.

**Fehleranalyse-Schwerpunkte:**
1. Kielbolzen-Dimensionierung zu schwach
2. Grounding-Last nicht in FEM berücksichtigt
3. Korrosion an Kielbolzen (nicht 316L oder passiviert)
4. Auftriebsverlust durch schlechte Profilwahl
5. Trimmverhalten bei Volumenänderung
6. Risse im Kielschuh
7. Verschleiß Kielschuh-Grundierung
8. Laminate zu dünn um Kielansatz
9. Fehlende Entwässerung in Kielnische
10. Dynamische Resonanz bei Motorbooten
11. Fertigungstoleranzen Kielansatz
12. Grounding-Szenarien-Management

---

## 1. Kielformen und Auswahl

### 1.1 Fin Keel (Flossenkiel)

**Charakteristik:**
- Separate, stromlinienförmige Flosse
- Aspektverhältnis: typisch 2–3
- Tiefgang: 1,2–2,5m (je nach LOA)
- Performance: hohe Wendigkeit, effizient bis ca. 15° Heel

**Einsatz:**
- Segelfahrten, Cruiser bis Rennboote
- Boote 8–30m LOA
- CE-Kategorien A, B, C

**Dimensionierung nach ISO 12217-1:**

```
Fin_Area [m²] = LOA [m] × Beam [m] / 12  (Basis-Startwert)
Aspect_Ratio = Height² / Area
Chord_Root [mm] = Area [m²] × 1000 / Height [m]
Chord_Tip [mm] = Chord_Root × 0.4  (typisch taper = 0.4–0.6)
```

**Profil-Auswahl:**
- NACA 63412 oder 64415: hohe Auftriebseffektivität
- NACA 0012: symmetrisch, für moderne Racing
- Renndesign: maßgeschneiderte Laminar-Profile

**Vorteile:**
- Höchste induktive Effizienz (2D-Profil)
- Einfache Serienproduktion
- Modularer Austausch

**Nachteile:**
- Kein Flachwasser-Verhalten
- Grounding-anfällig
- Störung seitens Motorhöhe bei Diesel-Inboard

### 1.2 Bulb Keel (Kugel- oder Flügellastenkiel)

**Charakteristik:**
- Flosse mit Massenkonzentration in Tiefe
- Bulb-Volumen: 15–25% des Gesamt-Kielvolumens
- Bulb-Tiefe: 0,5–1,2m unter Kielschuh

**Physik:**
```
Moment_Arm [m] = Bulb_CG_Depth [m] − Hull_CG_Depth [m]
Righting_Moment [Nm] = Bulb_Mass [kg] × 9.81 × Moment_Arm [m]
```

**Werkstoffe für Bulb:**
- Gusseisen (ductile): typisch 7800 kg/m³, einfacher zu gießen
- Blei (Pb): 11340 kg/m³, compact, aber: Umweltrecht (REACH) kontrollieren
- Stahlbeton-Verbund: seltener, höhere Baukosten

**Einsatz:**
- Langstrecken-Cruiser, Rennboote
- Hochzeitige Segelboote
- Boote 10–40m, wo Stabilität kritisch

**Grounding-Verhalten:**
- Bulb trifft zuerst auf Grund
- Abfederungs-Wirkung durch Kompression der Bulb-Masse
- Rissrisiko: Verbindung Flosse-Bulb muss >2mm Filetradius haben

**Vorteile:**
- Maximum-Righting-Moment pro Masse
- Tiefgang-abhängige Stabilität
- Moderne Racing-Standard

**Nachteile:**
- Kostenaufschlag 35–50%
- Komplexe Fertigung (Guss + Laminate)
- Korrosion an Guss-Laminate-Kontakt
- Grounding-schaden schwer reparierbar

### 1.3 Wing Keel (Flügelkiel)

**Charakteristik:**
- Flosse mit seitlichen Flügel-Vorsprüngen
- Ähnlich Bulb, aber: Massekonzentration seitlich (nicht vertikal)
- Tiefgang-Reduktion: 30–40% Einsparung ohne Stabilitäts-Verlust

**Beispiel-Abmessungen:**
| LOA | Fin-Tiefgang | Wing-Tiefgang | Reduktion |
|-----|-------------|---------------|-----------|
| 12m | 1,8m | 1,2m | 33% |
| 18m | 2,2m | 1,5m | 32% |
| 24m | 2,5m | 1,7m | 32% |

**Aerodynamik-Effekt (negativ bei falscher Ausführung):**
- Seitliche Flügel erzeugen induzierte Wirbel
- Widerstandserhöhung: 5–8% wenn schlecht dimensioniert
- Moderne CAD-Optimierung reduziert auf <2%

**Einsatz:**
- Shoal-Draft-Cruiser
- Reviere mit flachem Wasser (Ostsee, Mittelmeer)
- Motoryachten mit höheren Propeller-Anforderungen

**Vorteile:**
- Flachwasser-Verhalten + Stabilität
- Gute Wendigkeit
- Reparatur einzelner Flügel möglich

**Nachteile:**
- Höhere Strömungsverluste
- Komplexe FEM-Analyse erforderlich
- Fertigungs-Toleranzen kritischer

### 1.4 Lifting Keel (Hubkiel)

**Charakteristik:**
- Versenkbar hydraulisch oder mechanisch
- Tiefgang: 0,3–2,2m (variabel)
- Kompartiment in Rumpf erforderlich

**Funktionsweise:**
```
Hubkeil_Volumen [m³] = Hubzylinder × Stroke [m]
Gewicht_Mechanik [kg] = 50–150 kg (je nach Größe)
Sealing-Aufwand = 4x höher als Festkiel
```

**Hydraulik-Dimensionierung:**
- Zylinder-Druck: 150–210 bar
- Hydriervolumen pro Hub-Zyklus: 2–15 Liter
- Betriebszeit Einfah r/Ausfahrt: 20–60 Sekunden

**Einsatz:**
- Flussfahrten (Rumpf-Tiefgang 0,3–0,8m)
- Revierkreuzer mit dual-Modus
- Spezial-Designs (Liveaboard Ästuare)

**Kritische Probleme:**
1. Undichtigkeiten nach 5–10 Jahren (Seal-Verschleiß)
2. Biasing-Korrosion (Elektrolyt-Eindringung)
3. Notfall-Entriegelung-Ventil kann verklemmen
4. Kolben-Festfressen bei Salzwasser

**Vorteile:**
- Flachwasser + Offshore kombinierbar
- Null-Tiefgang möglich (hochgefahren)

**Nachteile:**
- Wartungsaufwand hoch
- Ausfallrisiko beim Manöver
- Umwelt-Compliance (Hydraulik-Leckage)

### 1.5 Doppelkiele (Twin Bilge Keels)

**Charakteristik:**
- Zwei kleinere Kiele seitlich der Kielline
- Jeder Kiel: Tiefgang 0,6–1,2m
- Abstand Mittelschiff: 3–6m

**Stabilität-Rechnung:**
```
Stability_Combined [%] = Single_Fin × 0.85  (wegen Interferenz)
Leeway_Angle = +15–20% höher als Fin
Moment_Arm_2Keels = (Keel_Mass × 2) × (Moment_Arm_Center)
```

**Einsatz:**
- Traditionale Designs, Holzboote
- Flussfahrt + Tidenreviere
- Motor-Langstrecker, wo Stabilität < Preis

**Grounding-Verhalten:**
- Kontrolliert: ein Kiel berührt zuerst
- Schräglage im Grounding: 5–15° (asymmetrisch)
- Reparatur: ein Kiel austauschbar

**Nachteile:**
- Hydrodynamischer Widerstand +8–12%
- Komplexe Kiel-Bolzen-Anordnung
- Zentrale Laminate-Belastung

---

## 2. Kielbolzen-Dimensionierung und Berechnung

### 2.1 ISO 12215-9 Kielbolzen-Spezifikation

**Regelwerk:**
- ISO 12215-9: Small craft — Hull construction and scantlings, Part 9 (Sailing craft appendages) — Lastfälle und Scantlings für Kiel und Kielbolzen als kritisches Strukturelement (Kielverlust = Kentergefahr). NICHT ISO 12217 (die nur Stabilität/Auftrieb bewertet).
- Lloyd's Register, DNV, ABS bieten optional erweiterte Regelwerke

**Material:**
- Stainless 316L (mindestens): erforderlich
- Verzinkte Stahlbolzen: nur für Süßwasser akzeptabel
- Duplex-Stahl (SAF 2507): alternativ für Hochsalz-Regionen

**Abmaße-Tabelle (Fin-Kiel, typisch):**

| LOA [m] | Kieltiefe [m] | Bolzen-Ø [mm] | Anzahl | Material | Gewinde-Tiefe [mm] |
|---------|---------------|---------------|--------|----------|-------------------|
| 8–10 | 1,0–1,3 | M16 | 4 | 316L | 50 |
| 10–14 | 1,3–1,8 | M20 | 6 | 316L | 65 |
| 14–18 | 1,8–2,2 | M24 | 8 | 316L | 80 |
| 18–24 | 2,2–2,8 | M30 | 10 | 316L | 100 |
| 24–30 | 2,8–3,4 | M36 | 12 | 316L | 120 |

### 2.2 Belastungs-Rechnung

**Grounding-Last-Szenario:**

```
Grounding_Force [N] = Boat_Mass [kg] × 9.81 × Impact_Factor
Impact_Factor = 3–6 (abhängig Auffahrt-Geschwindigkeit)
Typical: 5 × Boat_Mass × g

Beispiel: 20-Tonnen-Boot, 5x-Faktor
Grounding_Force = 20000 × 9.81 × 5 = 981 kN

Verteilung auf N_Bolzen:
Force_per_Bolt [kN] = 981 / 8 ≈ 123 kN

Stress_Bolt [MPa] = Force [N] / (π × (d/2)² )
Zulässig: 60–70% des Yield-Strength (für Ductility)
316L Yield: ~200 MPa → 60% = 120 MPa zulässig
```

**Bolzen-Kontakt-Fläche (Laminat-Interface):**

```
Kontakt_Fläche [m²] = N_Bolzen × π × (d_hole/2)² × (t_laminate_affected)
Typisch: 50–80 mm Laminat-Dicke um Bolzenloch wird stärker belastet

Peel_Stress [MPa] = Grounding_Force / Kontakt_Fläche
Zulässig (Epoxy-Matrix): 30–45 MPa
```

**Beispiel-Rechnung (18m Segelkutter):**
```
Boot_Mass = 24 t
Grounding_Force = 24 × 9.81 × 5 = 1177 kN (worst case)
N_Bolzen = 8 × M30
Kraft_pro_Bolzen = 1177 / 8 = 147 kN

M30: Ø 30mm
Querschnitt = π × 15² = 707 mm²
Stress = 147000 N / 707 mm² = 208 MPa

316L Yield 200 MPa → 103% → KRITISCH!
→ Müssen auf 10 × M30 upgraden
Neue Stress = 147 / 10 × 1000 / 707 = 167 MPa ✓
```

### 2.3 Spannungs-Konzentration und Ermüdung

**Ermüdungs-Lastfall:**
- Wiederholte Wellen-Belastung: 10–50 Millionen Zyklen über 20 Jahre
- Stress-Amplitude: 10–30% des Grounding-Worst-Case

**Festigkeit-Reduktion durch Kerben-Effekt:**
```
Notch_Factor [k_t] = 1.5–2.0 (abhängig Fillet-Radius)
Fillet_Radius >= 1 × d_bolt (mindestens)

Ermüdungs-Spannungsverlauf:
S_mean = 50 MPa (Durchschnitt)
S_amplitude = ±20 MPa (Wellen-Zyklus)
S_max = 70 MPa (zulässig für Ductility)
```

**Korrosions-Ermüdung:**
- Salzwasser reduziert Ermüdungs-Grenze um 30–40%
- Passivierung (ISO 12944 C5-M) erforderlich für 316L
- Prüfung alle 5 Jahre empfohlen

---

## 3. Kielschuh (Keel Shoe) und Füllstoff

### 3.1 Kielschuh-Funktion

**Aufgaben:**
1. Grounding-Schutz (elastische Abfederung)
2. Verschleißschutz (Laminat-Oberfläche)
3. Stromlinien-Übergang (Hull-Kiel-Interface)

### 3.2 Materialauswahl

| Material | Dichte [kg/m³] | Druckfestigkeit [MPa] | Einsatz | Kosten-Index |
|----------|-------------|----------------------|--------|-------------|
| Epoxy-Paste | 1800–1900 | 60–80 | Standard, C-Boot | 1.0 |
| Kevlar-Epoxy | 1400–1500 | 120–150 | Rennboot | 2.5 |
| Graphit-Epoxy | 1950–2050 | 90–110 | Semi-Custom | 2.0 |
| Kupfer-Epoxy | 3200–3500 | 70–85 | Antifouling + Abrieb | 3.5 |
| Polyurethan-Elastomer | 1100–1200 | 30–40 | Federung, Marine Mammal | 1.8 |

**Standard-Wahl:** Epoxy-Paste mit Quarzfüller, 30–50 mm Dicke

### 3.3 Fertigungs-Prozess

**Nagel-auf-Kopf-Methode (nicht empfohlen):**
- Kielschuh wird separat modelliert, geklebt
- Adhesive-Versagen bei Grounding
- Delaminierung nach 3–5 Jahren

**Best-Practice (moderne Konstruktion):**
```
Laminate-Sequence (von außen nach innen):
—— Gelcoat 0,5 mm (UV-Schutz)
—— CSM 300 g/m² (1,5 mm)
—— Woven 400 g/m² (2,0 mm) — Haupt-Schicht
—— Kielschuh-Paste wird integrated während Wicklung
—— Woven 400 g/m² (2,0 mm) — oben drauf während Härtung
—— CSM 300 g/m² (1,5 mm)
—— ggf. zusätz. Kern (PVC, 30 mm) für Gewicht/Steifheit
```

### 3.4 Verschleiß-Verhalten

**Empirische Abriebsraten:**

```
Typical_Abrasion [mm/1000_nm] = 0,5–2,0 (je nach Material + Untergrund)
Sandboden < 0,5 mm/1000 nm
Kiesgrund 1,0–1,5 mm/1000 nm
Hartgestirn 2,0–4,0 mm/1000 nm

Lebensdauer (50 mm initial):
Sandy: 100000 nm
Gravel: 35000 nm
Rocky: 12500 nm
```

**Überprüfungs-Richtlinie:**
- Jährliche visuelle Kontrolle
- Schichtdicken-Messung mit Ultraschall alle 5 Jahre
- Austausch bei <15 mm restliche Dicke

---

## 4. Aerodynamische Profilwahl

### 4.1 Klassische NACA-Serien

**NACA 63-xxx Profil:**
```
Beispiel: NACA 63415
6 = Series (laminar)
3 = Null-Auftrieb-Lage (deprecated, modern ignore)
4 = Maximale Wölbung in 40% Chord
15 = 15% Dicke
```

**Charakteristiken:**
- Laminar-Bereich bis Cl = 0,7–0,9
- Übergangs-Punkt ca. 15–20% Chord (laminar → turbulent)
- Sehr effizient aber kritisch gegenüber Verschmutzung

**NACA 64-xxx:**
- Modifiziert für höhere Stabilität in Stall
- Breiter Laminar-Bereich
- Weniger Performance-Verlust durch Algen/Bewuchs

### 4.2 Moderne Profil-Optimierung

**Rennboot-Profile (z.B. IMS-Regel):**
- Maßgeschneidert für spezifische Heel-Winkel
- LES-Simulationen (Large Eddy Simulation) für optimale Transition
- Kosten: EUR 15000–40000 pro Profil

**Cruiser-Kompromiss:**
- Auslegung für 10–20° Heel (typischer Betrieb)
- Robustheit gegen Verschmutzung: +2–3% Widerstand akzeptabel
- Küstenfahrt-Profil vs. Offshore

**Beispiel-Vergleich:**

| Profil | L/D (Best) | Laminar-Range | Robust gegen Verschm. | Kosten |
|--------|-----------|----------------|-----------------------|--------|
| NACA 63-415 | 180 | ±5° | Nein | Standard |
| NACA 64-415 | 175 | ±8° | Ja | Standard |
| Modern IMS | 200 | ±6° | Mittel | EUR 25k |
| Custom Cruiser | 170 | ±12° | Sehr Ja | EUR 35k |

### 4.3 Profildicken-Auswahl

```
Dünne Profile (10–12% Dicke):
  → Höhere Gleitzahl (L/D)
  → Geringere Festigkeit (mehr Verstärkung nötig)
  → Grounding-anfälliger

Mittlere Profile (15–18% Dicke):
  → Guter Kompromiss Festigkeit/Performance
  → Typisch für Production-Kiele
  → Einfacher zu fertigen

Dicke Profile (20–25% Dicke):
  → Maximale Festigkeit, Massenkonzentration Bulb
  → Für Bulb-Kiele üblich
  → Etwas höherer Widerstand
```

---

## 5. Dynamische Effekte und Grounding-Szenarios

### 5.1 Grounding-Szenarien nach Boots-Typ

**Szenario A: Auffahrt auf Sandbank (v ≈ 3–5 kn)**
```
Impact_Duration: 0,5–2 Sekunden
Beschleunigung: 1–3 g
Beanspruchung: hauptsächlich Vertikal + Längskräfte
Laminat-Risiko: moderat (Energie-Abbau durch Deformation)
Strukturversagen: selten bei korrekter Dimensionierung
```

**Szenario B: Harten Aufprall auf Stein (v ≈ 6–10 kn)**
```
Impact_Duration: <0,5 Sekunden
Beschleunigung: 5–8 g
Beanspruchung: konzentriert auf Kielschuh-Kontaktfläche
Laminat-Risiko: hoch (Matrix-Cracking, Faser-Brechen)
Strukturversagen: Risse im Kielbolzen-Bereich wahrscheinlich
```

**Szenario C: Schrittweise Auffahrt (v ≈ 1–2 kn)**
```
Impact_Duration: kontinuierlich, 10–30 Minuten
Beschleunigung: <0,5 g
Beanspruchung: Scherkräfte, Verschleiß
Laminat-Risiko: niedrig (statische Last)
Strukturversagen: Verschleiß-dominant; Kielbolzen unter Dauerstress
```

### 5.2 Notfall-Grounding-Manöver

**Refloating-Lasten:**

```
Boot_Aufschwemmungs-Kraft = Buoyancy_Delta × 9.81
Typisch: 2–10 kN extra Auftrieb nötig für Refloating
Kielbolzen-Zusatzlast beim Refloating mit Kraft-Boot: bis 200 kN!

Empfehlung: Refloating-Kraft begrenzt auf 80% des zulässigen Maximal-Bolzen-Stress
→ Gefährliche Schnelligkeit vermeiden
→ Hydraulische Hubkraft regelbar
```

**Grounding-Management-Protokoll:**
1. Engine aus, Segel dichtnehmen
2. Tiefenmesser prüfen (Tiefgang? Tide-Trend?)
3. Gewichts-Verlagerung (Ballast raus, keine plötzlichen Hänge-Bewegungen)
4. Back-warp oder versetzen (seitliche Drift)
5. Wenn Refloating: sanft ankern, dann externe Kraft minimal

### 5.3 FEM-Analyse des Grounding

**Modellierungs-Anforderungen:**

```
CAD-Eingabe:
- Hull-Geometrie (Netz-Auflösung: 20 mm in Kielbereich)
- Kielschuh-Schichtaufbau (Gelcoat, Laminate, Füllstoff)
- Kielbolzen (3D Geometrie mit Gewinde-Kerbe)
- Laminat-Orientierung (ply-by-ply für Festigkeit)
- Material-Daten (E-Modul, Poisson-Zahl, Bruchfestigkeit)

Randbedingungen:
- Bottom-Contact: Kontakt mit Untergrund (Starrheit)
- Druck-Lastfall: 500 kPa über 0,5 m² Kielschuh-Fläche
- Dynamisch: Impuls-Dauer 0,5–2 s (Zeit-Integration)

Ergebnis:
- Stress-Verteilung auf Kielbolzen
- Matrix-Dehnung (>1% = Bruch-Risiko)
- Verschiebungen Kiel relativ Hull
- Rissinitiierungs-Orte (typ. Bolzenlöcher)
```

---

## 6. Korrosion und Passivierung

### 6.1 Biasing-Korrosion (Galvanisches Paar)

**Metallpaarung im Seewasser:**

| Paar | Potential-Differenz [mV] | Korrosions-Rate | Risiko |
|------|--------------------------|-----------------|--------|
| Stahl-Kupfer | 400 | Hoch | Sehr kritisch |
| 316L-Kupfer | 250 | Mittel | Kritisch |
| 316L-Bronze | 150 | Niedrig | Moderat |
| 316L-Edelstahl | <10 | Negligible | OK |
| Duplex-316L | <20 | Negligible | OK |

**Schutzmaßnahmen:**
1. Isolierschicht: Epoxy-Laminat um Bolzen (2–3 mm), unversehrt halten
2. Opfer-Anode (Zink oder Aluminium): 1 Anode pro 2 m Kielfläche
3. Kathoden-Schutz (CP System): <-900 mV (Ag/AgCl) für Stahl

### 6.2 Spannungs-Korrosions-Risse (SCC)

**Risiko-Faktoren:**
- Hohe Zugspannung (>50% Yield) UND
- Aggressive Chemie (Chlorid-Konzentration) UND
- Zeit (Monate bis Jahre)

**Beispiel: 316L M30 Bolzen unter Grounding-Last**
```
Residual_Stress_after_tightening = 60 MPa
Grounding_Transient_Stress = 180 MPa
Total = 240 MPa (120% des Yields!)
→ SCC-Rissform nach 2–3 Jahren möglich

Mitigation:
1. Stress-Relief bei Installation (kurz auf 120°C erhitzen)
2. Oder: Direkter Austausch nach großem Grounding
3. Inspektionen: alle 2 Jahre mit UT-Prüfung
```

### 6.3 Chlorid-Eindringung und Pitting

**Schutz-Strategie:**

```
Barriere-Schicht:
1. Epoxy-Grundierung (2-Komponenten, 100 µm)
2. Polyurethan-Topcoat (75 µm)
3. Gesamt-Film: 175 µm
→ Pitting-Schutz >15 Jahre

Überprüfung:
- Jährlich auf Kratzer kontrollieren
- Nach Grounding sofort reparieren
- Rost-Flecken = Laminat-Breche, Bolzen freigen
```

**Passivierungs-Norm:**
- ISO 12944 C5-M (Marine High): erforderlich
- Dauer: 30–40 Minuten in Salzsäure-Bad
- Afterwards: Spülen + schnelles Trocknen

---

## 7. Trimmverhalten und Gewichts-Einfluss

### 7.1 Längstrimm bei Kielvolumen-Änderung

**Scenario: Bulb-Kiel mit Auftriebsverlust (Algen, Eis)**

```
Initialer Zustand:
Boot_Mass = 25 t
CG (Longitudinal) = 45% von Heck
Kiel_Volume = 2,8 m³
Kiel_CG = 60% von Heck (tiefer)

Trimm_Moment = (Kiel_CG − Boat_CG) × Kiel_Buoyancy
             = (60 − 45)% LOA × 2,8m³ × 1000 kg/m³ × 9.81
             = 0.15 × LOA × 27468 N
             (positive Moment = Bug-down, wenn Kiel Bug-wärts)

Trimmänderung:
Δtrimm [°] = Moment / (Boat_Mass × g × Waterplane_Area [m²])
Typisch: 1–2° Bug-down pro 100 kg Kielgewichts-Änderung
```

**Konsequenzen für Design:**
- Bug-Seegang-Eindringung bei falscher Trimm
- Kursstabilität verloren (zu viel Bug-down)
- Geschwindigkeits-Verlust (erhöhter Trim-Widerstand)

### 7.2 Dynamisches Verhalten bei Wellen

**Toss-Freqenz (Pitch-Resonanz):**

```
Pitch_Frequency [Hz] = sqrt(GM [m] / (LOA/2)² [m²])
Typisch 8–14m Boot: 0,3–0,5 Hz
Wellen-Periode, die Resonanz anregt: 10–20 Sekunden
→ Schwerer Seegang (3–5m Wellen, 10s Periode) = Problem
```

**Dämpfung durch Kielform:**
- Fin-Kiel: marginale Dämpfung (<5%)
- Bulb-Kiel mit Flüssigkeits-Bewegung: +3–8% Dämpfung
- Externe Stabilisierungs-Flosse: +15–25% möglich

---

## 8. Fertigungs-Toleranzen und Qualitätskontrolle

### 8.1 CAD-Entwurfs-Toleranzen

**Kritische Abmessungen:**

| Element | Nominal | Toleranz | Prüfung-Methode |
|---------|---------|----------|-----------------|
| Kieltiefe | 2000 mm | ±5 mm | Messstab + Wasserwaage |
| Kielneigung | 10° | ±0,5° | Transit-Theodolite |
| Bolzenloch-Position | zentrisch | ±2 mm | Bohrlehre |
| Bolzenloch-Ø | M30 | ±0,1 mm | Messlehrdorn |
| Kielschuh-Dicke | 50 mm | ±3 mm | Ultraschall-Dickenmesser |

### 8.2 Inspektions-Checkliste vor Übergabe

```
Visuelle Kontrolle:
  ☐ Keine Risse in Laminat um Bolzenlöcher
  ☐ Kielschuh-Oberfläche: max. 2 mm Rauhheit
  ☐ Kielbolzen-Gewinde frei von Verschmutzung
  ☐ Epoxy-Klebstoff-Füllstoff homogen (keine Lufteinschlüsse)
  
Dimensionelle Prüfung:
  ☐ Kieltiefe (±5 mm)
  ☐ Bolzenloch-Positionen (±2 mm)
  ☐ Kielschuh-Dicke alle 500 mm (±3 mm)
  
Zerstörungsfreie Prüfung (je nach Boot-Klasse):
  ☐ Thermographie: Hohlräume um Bolzenlöcher
  ☐ Ultraschall: Delaminierung in Laminat-Schichten
  ☐ Röntgen: innere Fehler (optional für Premium)
  
Belastungs-Test (bei neuer Design):
  ☐ Grounding-Simulations-Test: 100% Betriebslast auf Kielschuh
  ☐ Überprüfung auf Risse nach Test
```

### 8.3 Häufige Fertigungs-Fehler

**Fehler 1: Harz-Verhältnis falsch (zu viel Harz)**
```
Problem: Schlechte Faser-Benetzung, schwache Matrix
Folge: Keilbruch bei Grounding, 30% Festigkeits-Verlust
Prävention: Harz-Gehalt prüfen (sollte 30–35% Gewicht sein)
Testung: Burn-off-Test nach ISO 1172
```

**Fehler 2: Laminat-Schichtfolge invertiert**
```
Problem: Wenn CSM außen (statt Woven), nicht robust
Folge: UV-Vergilbung, schneller Verschleiß
Prävention: Prozess-Dokumentation, Lagen-Markierung während Wicklung
```

**Fehler 3: Bolzenlöcher zu nah an Kanten (Stress-Konzentration)**
```
Problem: Laminat-Cracking um Bolzenloch-Peripherie
Folge: Risse wachsen unter Betriebslast, Wassereinbruch
Prävention: Mindestens 30 mm Abstand Loch zu Hull-Kante
Prüfung: CAD-Check vor Produktion
```

---

## 9. Installation und Verschraubungs-Protokoll

### 9.1 Montageschritte

**Phase 1: Vorbereitung des Laminat-Sockels**

```
Schritt 1a: Prüfung Laminat-Oberflächenqualität
  - Oberflächen-Rauhheit: Ra 10–20 µm
  - Feuchtigkeit: <2% (mit Feuchtemesser prüfen)
  - Ablage mindestens 24h bei 20°C vor Montage

Schritt 1b: Bolzenloch-Vorbereitung
  - Innenloch: Klasse IT7 (±0,025 mm für M30)
  - Konter-Senker: 90° Winkel, 3 × d/2 Tiefe
  - Entgraten: feines Schleifpapier (Körnung 320)
  - Entwässerungs-Loch daneben (Ø 5 mm, 5 mm tiefer als Gewindegrund)
```

**Phase 2: Bolzen-Vorbereitung**

```
Schritt 2a: Gewinde-Kontrolle
  - Pitch-Prüfung mit Gewinde-Lehrdorn
  - Oberflächenrauhheit: <0,4 µm Ra (poliert)
  
Schritt 2b: Passivierung
  - ISO 12944 C5-M Standard erforderlich
  - Nach Pasivierung: sofort trocknen, <4h Lagerung vorher
  - Oberflächenhautbildung kontrollieren (Fleckprobe)

Schritt 2c: Fettung
  - Molybdän-Disulfid-Paste (MoS₂) auf Gewinde auftragen
  - Reibungs-Koeffizient standardisieren (besser als trockenes Gewinde)
  - Spezifikation: DIN 6205 oder Molykote G-Rapid Plus
```

**Phase 3: Verschraubung (Final Assembly)**

```
Dreh-Momnte-Plan (M30 × 316L mit MoS₂-Paste):

Schritt 3a: Finger-Anziehen
  Alle Bolzen von Hand bis Widerstand, Kraft ca. 50 N·m
  → Zentriert alle Bolzen

Schritt 3b: Überkreuz-Spannen (Stern-Muster)
  Bolt 1 → 100 N·m
  Bolt 5 (gegenüber) → 100 N·m
  Bolt 3 → 100 N·m
  Bolt 7 (gegenüber) → 100 N·m
  (wiederholen bis Stern-Nummer 4)

Schritt 3c: Finale Spannungsprüfung
  Alle Bolzen in Folge: Drehmoment 250 N·m (90% von Spec)
  Prüfprotokoll ausgefüllt:
    - Bolzen-Nummer
    - Mess-Drehmoment
    - Zeit
    - Prüfer-Signatur

Schritt 3d: Entspannungs-Messung (optional, für hochwertige Boote)
  24h nach Montage:
  Jedem Bolzen erneut Drehmoment 250 N·m anwenden
  Liegt Moment bei 240–250 N·m → OK (keine Relaxation)
  Unter 230 N·m → Bolzen lockerer geworden, nachspannen

Schritt 3e: Abdichtung
  Kopf-Fläche + Kontermutter mit Epoxy-Sperrgel beschichten
  (verhindert Wasser-Eindringung, Salzablagerung)
```

**Drehmoment-Berechnung (allgemein):**

```
Kurzform (Reibbeiwert-/Nut-Factor-Methode):
T [N·m] = K × F [N] × d [m]
  K = dimensionsloser Anziehfaktor (bündelt Gewinde- und Kopfreibung):
      trocken ≈ 0,20 ; leicht geölt ≈ 0,15 ; MoS₂-Paste ≈ 0,10
  F = Vorspannkraft [N]
  d = Nenndurchmesser [m]  (voller Durchmesser, NICHT Radius)

Für M30 × 316L + MoS₂:
  d = 30 mm = 0,030 m
  Zielspannung = 60% von Yield (200 MPa) = 120 MPa
  F = 120 MPa × π × 15² mm² = 84823 N ≈ 85 kN
  K mit MoS₂ ≈ 0,10

T = 0,10 × 85000 N × 0,030 m = 255 N·m ≈ 250 N·m

→ Deckt sich mit der Standard-Tabelle für M30, 316L, MoS₂-Paste (≈ 250 N·m)
  und entspricht der Ziel-Vorspannung von ~60% Yield.
  Hinweis: K streut mit Paste/Oberfläche (MoS₂ ≈ 0,08–0,12) — im Zweifel
  Herstellerangabe des Schmierstoffs verwenden.

Normbasis: ISO 12215-9 (Sailing craft appendages), Anhang B — "established
practice" für Kielbolzen-Anzug und Kielbefestigung. ISO 12217 bewertet nur
Stabilität/Auftrieb, nicht die Bolzen-Dimensionierung.
```

### 9.2 Abdichtungs-Detail

**Wassereinbruch-Sperr-Systeme:**

```
Option A: Epoxy-Paste-Siegel
  Material: Zweikomponenten-Epoxy + Quarzfüller
  Aufbringung: 10 mm dicke Schicht um Bolzenkopf
  Aushärtung: 24h vor Wasserkontakt
  Haltbarkeit: 10–15 Jahre
  Kosten: EUR 2–5 pro Bolzen

Option B: PTFE-Tape (Teflon)
  Wicklung: 8–10 Umwicklungen um Bolzen-Gewinde
  Kompatibilität: mit allen Materialien OK
  Nachteil: nur oberflächlich, nicht tiefe Eindringung
  Kosten: EUR 0,50 pro Bolzen

Option C: Anaerobes Dicht-Mittel
  Produkt: Loctite 243 (mittelfest)
  Aufbringung: auf Gewinde vor Montage
  Aushärtung: 24h
  Vorteil: Chemikalien-Abdichtung auch innerhalb Gewinde
  Nachteil: Demontage schwierig
  Kosten: EUR 1–2 pro Bolzen

Empfehlung für Marine: Kombination B + A
  → Tape verhindert Sand/Salz-Eindringung
  → Epoxy-Kappe versiegelt oberflächlich
```

---

## 10. Wartung und Inspektions-Intervalle

### 10.1 Inspektions-Checkliste nach Saison

```
Nach jedem Grounding oder Kollision:
  ☐ Sichtprüfung Kielschuh (Kratzer, Vertiefungen)
  ☐ Ultraschall-Dickenmessung (falls >5 mm Beschädigung)
  ☐ Bolzen-Kopf-Kontrolle auf Rost-Flecken
  ☐ Wenn Beschädigung, sofort Reparatur-Maßnahme einleiten

Jährlich (vor/nach Saison):
  ☐ Alle Kielbolzen-Köpfe auf Durchrost prüfen
  ☐ Epoxy-Siegelkappe: Kratzer ausbessern
  ☐ Kielschuh-Oberfläche: Tiefgang abgemessen, Trend kontrollieren
  ☐ Wasserlecks (Bilgenwasser-Geruch) = Bolzen-Leck?

Alle 5 Jahre:
  ☐ Ultraschall-Kontrolle der Laminat-Schichten
  ☐ Röntgen der Bolzenlöcher (optional, für hochwertige Boote)
  ☐ ggf. Bolzen-Anzugs-Kontrolle (Drehmoment-Schlüssel)

Alle 10 Jahre oder nach großem Grounding:
  ☐ Visuelle Inspektionsbohrung: eine kleine Bohrung (Ø 2 mm)
      in Kielschuh machen, Laminate-Struktur mit Endoskop prüfen
  ☐ ggf. Bolzen-Austausch (Sicherheitsfaktor)
  ☐ Korrosions-Schutz-System überprüfen
```

### 10.2 Reparatur nach Grounding

**Stufe 1: Oberflächlicher Kratzer/Delle (< 5 mm Tiefe)**

```
Schritte:
1. Abtrag des beschädigten Kielschuh-Materials mit Schleifer
2. U-förmige Ausnehmung schneiden (minimale stress-Konzentration)
3. Mit Epoxy-Paste nachfüllen, glätten
4. Nach Aushärtung: Oberfläche schleifen (Ra 20 µm)
5. Ggf. Schutz-Anstrich auftragen

Dauer: 1–3 Tage
Kosten: EUR 500–1500
```

**Stufe 2: Tiefe Kerbe / Riss in Laminat (5–20 mm, keine Bolzen betroffen)**

```
Schritte:
1. Beschädigte Laminat-Fasern komplett entfernen
   → 50 mm × 50 mm Areal + 20 mm über Riss hinaus
2. Rauheit-Fläche vorbereiten (Schleifen auf CSM-Struktur sichtbar)
3. Laminat-Matte + Woven nachwickeln (2–3 Schichten)
   → Faser-Orientierung prüfen (sollte Original entsprechen)
4. Abdeckung mit Epoxy-Paste + Oberflächen-Finish
5. Härtung 48h, dann Oberflächenbearbeitung

Dauer: 3–5 Tage
Kosten: EUR 1500–3500
```

**Stufe 3: Struktur-Schaden / Bolzen-Bereich betroffen**

```
Dies erfordert professionelle Reparaturwerft:

1. Kiel muss möglicherweise entfernt werden
   Schritte: Ablösen des Kiels (Schneidern der Klebe-Fuge)
2. Laminat im Bolzen-Bereich erneuert
3. Kiel neuaufgeklebt oder Bolzen gelöst und nachbearbeitet

Dauer: 2–4 Wochen (wartet auf Ablöse-Werkstatt)
Kosten: EUR 5000–15000
```

---

## ANHANG A — Glossar

**Aspektverhältnis (Aspect Ratio):** Verhältnis Kieltiefe² zu Kielfläche. Höhere AR = bessere Induzierte-Effizienz.

**Bulb Keel:** Kiel mit konzentrierter Massenlast in der Tiefe, meist Blei oder Gusseisen.

**CE-Kategorien:** Einteilung Segelboote nach Seegebiet (A=Ozean bis D=Binnensee).

**Delaminierung:** Ablösung zwischen Laminat-Schichten, meist durch Feuchte oder Stoß.

**Entwässerung (Drainage):** Kleine Bohrungen in Kielschuh-Bereich, um Stauwasser zu vermeiden.

**Fin-Kiel:** Standardform mit geringem Aspektverhältnis, typisch für moderne Segler.

**Filet-Radius:** Rundung an Kanten-Übergängen, reduziert Stress-Konzentration.

**Galvanisches Paar:** Zwei unterschiedliche Metalle in leitendem Medium → Korrosion.

**Gelcoat:** Kunstharz-Schutzschicht auf Laminate-Oberfläche (0,3–0,8 mm).

**Gleitzahl (L/D):** Auftrieb geteilt durch Widerstand, Effizienzmaß.

**Grounding:** Auflaufen auf Grund, könnte auch Schädigung-Event sein.

**Keel Shoe:** Verschleiß-Schicht auf Kielbasis, elastischer als Laminat.

**Laminat:** Geschichtete Struktur aus Fasern + Harz (GFK/FRP).

**NACA-Profil:** Systematische Profilbezeichnung (National Advisory Committee Aeronautics).

**Notch-Effekt:** Spannungs-Erhöhung an Kerben/Löchern, Faktor 1,5–3×.

**Pitch-Frequenz:** Eigenfrequenz des Boots im Nicken (Kopf-zu-Schwanz-Wippen).

**SCC (Spannungs-Korrosions-Risse):** Risse durch gleichzeitige Spannung + Chemikalien.

**Sealing:** Abdichtung gegen Wasser-Eindringung.

**Stress-Relief:** Thermische Entspannung von Residual-Stress nach Montage.

**Trim:** Längseigung des Schiffes (Bug hoch/tief oder level).

**Ultraschall-Dickenmessung:** UT-Prüfung für Material-Dicke ohne Zerstörung.

**Wing Keel:** Kiel mit seitlichen Flügeln, reduzierter Tiefgang ohne Stabilitätsverlust.

**Yield Strength:** Fließgrenze, Spannung bei 0,2% plastischer Dehnung.

**Zweikomponenten-Epoxy:** Harz + Härter, wird hart nach Vermischung.

---

## ANHANG B — Pydantic v2 Validierungs-Modell

```python
from pydantic import BaseModel, Field
from typing import Optional, List

class KielkonstruktionFehlerbild(BaseModel):
    """
    Fehlerbild für Kielkonstruktion nach AYDI-Standard.
    12 spezifische Fehlerbilder mit Schweregrad, Ort, Lösungsweg.
    """
    model_config = {"from_attributes": True}

    # Metadaten
    fehlerbild_id: str = Field(..., description="Eindeutige ID, z.B. '31_08_001'")
    kategorie: str = "31_Design_Konstruktion"
    unterkategorie: str = "Kielkonstruktion"
    
    # Fehler-Beschreibung
    titel: str = Field(..., description="Kurztitel des Fehlerbilds")
    beschreibung: str = Field(..., description="Detaillierte Fehler-Charakterisierung")
    
    # Symptome und Auswirkungen
    symptome: List[str] = Field(default_factory=list, description="Beobachtbare Zeichen")
    auswirkungen: List[str] = Field(default_factory=list, description="Folgen für Boot/Betrieb")
    
    # Schweregrad
    schweregrad: str = Field(..., description="'kritisch', 'hoch', 'mittel', 'niedrig'")
    sicherheits_impact: bool = Field(default=False, description="Sicherheits-relevanz")
    
    # Ursprung / Kontext
    boots_typen: List[str] = Field(default_factory=list, description="Relevante Boot-Klassen")
    materialien: List[str] = Field(default_factory=list, description="Betroffene Materialien")
    
    # Diagnose und Reparatur
    diagnose_methoden: List[str] = Field(default_factory=list, description="Wie identifizieren?")
    reparatur_optionen: List[str] = Field(default_factory=list, description="Lösungsansätze")
    schaetzung_kosten_eur: Optional[float] = Field(None, description="Grobe Reparatur-Kosten")
    dauer_tage: Optional[int] = Field(None, description="Reparatur-Dauer in Tagen")
    
    # Prävention
    praevention: List[str] = Field(default_factory=list, description="Wie vermeiden?")
    inspektions_intervall_jahre: Optional[float] = Field(None, description="Wartungs-Zyklus")
    
    # Verweise und Quellen
    normen_referenzen: List[str] = Field(default_factory=list, description="ISO, CE, Lloyd's, etc.")
    verwandte_fehlerbilder: List[str] = Field(default_factory=list, description="Andere Fehler-IDs")


# Instanz: Beispiel Fehlerbild 1
fehlerbild_001 = KielkonstruktionFehlerbild(
    fehlerbild_id="31_08_001",
    titel="Kielbolzen-Dimensionierung zu schwach",
    beschreibung="Bolzen mit unzureichendem Durchmesser für erwartete Grounding-Lasten.",
    symptome=[
        "Deformation Kielbolzen nach Auflaufen",
        "Sichtbare Verschlingung der Bolzen-Gewindegänge",
        "Wassereintritt durch gelockerte Bolzen"
    ],
    auswirkungen=[
        "Strukturelle Sicherheit beeinträchtigt",
        "Kiel kann verrutschen, worst case: Ablösung",
        "Reparatur nur mit Bolzen-Austausch möglich"
    ],
    schweregrad="kritisch",
    sicherheits_impact=True,
    boots_typen=["Segelboot", "Motorsegler"],
    materialien=["Stainless 316L", "Epoxy-Laminat"],
    diagnose_methoden=[
        "Visuelles Grounding-Protokoll",
        "Drehmoment-Prüfung der Bolzen",
        "FEM-Rückwärts-Analyse"
    ],
    reparatur_optionen=[
        "Bolzen-Austausch auf größeren Durchmesser",
        "Erhöhung der Bolzen-Anzahl",
        "Nachrüstung mit Kiel-Verstärkung"
    ],
    schaetzung_kosten_eur=3500,
    dauer_tage=5,
    praevention=[
        "Dimensionierung nach ISO 12215-9",
        "FEM-Analyse für Grounding-Lasten",
        "Überprüfung bei Konstruktion-Review"
    ],
    inspektions_intervall_jahre=5,
    normen_referenzen=["ISO 12215-9", "CE 2013/53/EU", "DNV GL Rules"],
    verwandte_fehlerbilder=["31_08_002", "31_08_007"]
)
```

---

## ANHANG C — Häufig Gestellte Fragen (FAQ)

**F1: Wann ist eine Bulb-Kiel wirtschaftlich sinnvoll?**
A: Bei Segelbooten >12m LOA und Kreuzer-Gebrauch. Kostenzuschlag 35–50% amortisiert sich durch bessere Segelleistung (1–2 kn mehr Geschwindigkeit), besonders bei Langfahrten.

**F2: Wie oft müssen Kielbolzen kontrolliert werden?**
A: Nach jedem Grounding sofort; jährlich visuell; alle 5 Jahre mit Drehmoment-Prüfung; alle 10 Jahre UT-Prüfung oder Austausch.

**F3: Kann man einen Fin-Kiel durch eine Bulb ersetzen (Retrofit)?**
A: Technisch ja, aber Kosten (EUR 15000–25000) und Aufwand (Auftriebsverlust während Downtime). Empfohlen nur bei sehr hohem Performance-Anspruch.

**F4: Was kostet die Reparatur eines gerissenen Kiel-Laminat?**
A: EUR 1500–3500 für oberflächliche Risse; EUR 5000–15000 wenn Bolzen betroffen (Demontage).

**F5: Ist 316L zwingend erforderlich?**
A: Ja, für Salzwasser. 304er-Edelstahl korrodiert in 5–10 Jahren. Verzinkter Stahl nur für Binnengewässer.

**F6: Wie lange hält Kielschuh-Material?**
A: Typisch 35000–100000 nm (abhängig Untergrund). Bei 1000 nm/Jahr = 35–100 Jahre, aber Verschleiß ist nicht linear (schneller gegen Ende).

**F7: Kann man eine Kielform optimieren (CFD)?**
A: Ja, moderne CFD kostet EUR 8000–25000 pro Profil. ROI erst bei Serien >20 Boote oder Rennboot-Einsatz.

**F8: Was ist der Unterschied zwischen "Lift Keel" und "Drop Keel"?**
A: Lift (Hubkiel): fährt in Kompartiment ein/aus. Drop: externes Gewicht (selten modern). Lift ist Standard.

**F9: Sind Doppelkiele sicherer als Fin-Kiel?**
A: Nein, nicht sicherer, aber robuster. Grounding auf Twin-Bilge kontrollierter, aber Widerstand +8–12%.

**F10: Welche Inspektionsmethode ist am zuverlässigsten?**
A: Ultraschall-Prüfung (UT) für Delaminierung; Röntgen für innere Hohlräume (kostet aber EUR 1500–3000). Visuelle Prüfung + UT = Standard.

---

## ANHANG D — Materialien-Kennwerte Referenz-Tabelle

| Material | E-Modul [GPa] | Yield [MPa] | Dichte [kg/m³] | Korrosions-Resistenz (Salzwasser) |
|----------|--------------|-----------|---------------|---------------------------------|
| Stainless 316L | 193 | 200–220 | 8000 | Ausgezeichnet |
| Duplex SAF 2507 | 200 | 450–550 | 7800 | Sehr gut (höher als 316L) |
| Gusseisen (ductile) | 170 | 350–400 | 7100 | Moderat (braucht Schutz) |
| Blei (Pb) | 16 | 12–17 | 11340 | Sehr gut (inert) |
| Epoxy-Harz | 3–5 | 60–80 | 1100–1200 | Ausgezeichnet |
| Woven GFK | 18–25 (Fasern 70%) | 350–450 | 1850–1950 | Ausgezeichnet |
| CSM GFK | 8–12 | 150–200 | 1800–1900 | Ausgezeichnet |

---

## ANHANG E — Typische Kosten-Übersicht (2026 Preise, EUR)

| Leistung | Segelboot 12m | Motorsegler 18m | Rennboot 14m |
|----------|--------------|-----------------|-------------|
| Fin-Kiel Konstruktion | 4500–6500 | 8000–12000 | 6000–9000 |
| Bulb-Kiel Konstruktion | 7500–10000 | 15000–20000 | 12000–16000 |
| Kielbolzen-Set (inkl. Passivierung) | 800–1200 | 1500–2200 | 1200–1800 |
| Kielschuh-Fertigungs-Aufschlag | 500–1000 | 1000–2000 | 800–1500 |
| Inspektions-Paket (visuell + UT) | 600–1000 | 800–1500 | 700–1200 |
| Grounding-Reparatur (oberflächlich) | 1500–2500 | 2500–4000 | 2000–3500 |
| Kiel-Austausch (Demontage + Neukiel) | 12000–20000 | 25000–40000 | 20000–35000 |

---

**Redaktion & Qualitätskontrolle:** AYDI Knowledge Engineering v6  
**Letzte Überprüfung:** 2026-05-18  
**Gültig für:** Segelboote, Motorsegel, Rennboote 8–40m LOA
