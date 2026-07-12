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

---
---

# TEIL II — WEB-VERIFIZIERTE WERFT-ERWEITERUNG (Audit 2026-07)

> **Lesehinweis / Confidence-Konvention dieses Teils.** Alle Angaben in Teil II sind
> gegen autoritative Quellen (ISO-Katalogeinträge, begutachtete Fachpublikation,
> Kielhersteller, MAIB-Unfalluntersuchungen, Surveyor-Praxis) geprüft und tragen
> ein Confidence-Tag: `documented` = wörtlich/sinngemäß aus benannter Quelle
> belegt; `estimated` = branchenübliche Größenordnung ohne zweifelsfreien
> Einzelbeleg. **Exakte Formel-Koeffizienten, Teilsicherheitsbeiwerte und die
> genauen Lastfall-Gleichungen von ISO 12215-9 stehen ausschließlich im
> kostenpflichtigen Normtext und wurden NICHT rekonstruiert** — sie werden hier
> qualitativ (Was/Warum/welche Norm) beschrieben, nicht als Zahlenrezept.
>
> **Verhältnis zu Teil I:** Teil I (v2.0) enthält zahlreiche Rechenbeispiele,
> Profil-L/D-Werte, Abriebsraten und Koeffizienten **ohne Quellenbeleg**. Diese sind
> als `estimated — unverifiziert` zu behandeln. Wo Teil I einer verifizierten
> Quelle widerspricht, gilt Teil II. Die wichtigsten Korrekturen sind in
> Abschnitt II-0 zusammengefasst.

---

## II-0. Normative Klarstellungen und Korrekturen (Vorrang vor Teil I)

| # | Aussage in Teil I | Korrektur (verifiziert) | Confidence |
|---|-------------------|-------------------------|------------|
| K1 | Abschnitt 1.1: „Dimensionierung nach **ISO 12217-1**" für Kielflächen/Scantlings | **Falsche Norm.** ISO 12217 behandelt ausschließlich **Stabilität und Auftrieb**, nicht Struktur. Kiel-/Anhangslasten und -Scantlings: **ISO 12215-9**; Rumpf-Bemessungsdrücke/-Spannungen: **ISO 12215-5**. Die Formel `Fin_Area = LOA × Beam / 12` ist in keiner Norm belegt → `estimated — unverifiziert`. | `documented` |
| K2 | Abschnitt 2.1 / 6 / FAQ F5: „Stainless **316L** (mindestens): erforderlich" als Fakt | **Zu stark.** 316/316L erleidet im anaeroben, feuchten Kielsumpf-Spalt **intensive Spaltkorrosion (crevice corrosion)** und ist für dauergetauchte kritische Kielbolzen nach Herstelleraussage *nicht* geeignet. Moderner Konsens: **Duplex 2205 / Super-Duplex 2507** (siehe II-3). | `documented` |
| K3 | Diverse Rechenbeispiele (2.2, 2.3, 5, 7) mit Impact-Faktoren, Peel-Stress, Pitch-Frequenz-Formel | Keine dieser Formeln/Koeffizienten ist aus ISO 12215-9 oder anderer Quelle belegbar. **Als Illustration behandeln, nicht für reale Dimensionierung verwenden.** Reale Lastfälle: siehe II-2. | `estimated — unverifiziert` |
| K4 | „ISO 12944 C5-M" als „Passivierungs-Norm" (Abschn. 6.3 / 9.1) | ISO 12944-Teile beschreiben **Korrosionsschutz durch Beschichtungssysteme** und die Korrosivitätskategorie **C5** (nicht „C5-M"; die Kategorie heißt seit ISO 12944-2:2017 schlicht **C5**, zusätzlich **CX** für offshore/extrem). Chemische **Passivierung** von Edelstahl ist dagegen **ASTM A967 / ISO 16048**-Thema. Beide Normbezüge in Teil I sind ungenau. | `documented` |

---

## II-1. Normativer Rahmen — ISO-12215-Familie (verifiziert)

Die Reihe **ISO 12215 „Small craft — Hull construction and scantlings"** ist die
Bemessungsgrundlage für Rumpf und Anhänge kleiner Wasserfahrzeuge bis **24 m
Rumpflänge L_H** (Längenmessung nach **ISO 8666**). Relevante Teile für die
Kielkonstruktion:

| Teil | Titel | Rolle für den Kiel | Confidence |
|------|-------|--------------------|------------|
| **ISO 12215-5** | Design pressures for monohulls, design stresses, scantlings determination | Bemessungsdrücke, Bemessungsspannungen und Scantling-Ermittlung des Rumpfs — u. a. der Rumpfschale **im Kielanschlussbereich** | `documented` |
| **ISO 12215-8** | Rudders | Ruder (Ruderkraft, Schaft) — nicht Kiel, aber gleiche Systematik | `documented` |
| **ISO 12215-9** | **Sailing craft appendages** | **Kern für Kiel:** Lasten & Scantlings von festen/kippbaren Kielen, Schwertern, Steckschwertern und **deren Befestigung am Rumpf** | `documented` |
| **ISO 12215-10** | Rig loads and rig attachment in sailing craft | Rigg-Lasten/-Anschluss (indirekt kielrelevant über Rumpfbelastung) | `documented` |

> Quelle: ISO-Katalog, ISO 12215-5:2019 (Std. 69552) und ISO 12215-9:2012 (Std. 55339);
> „For the complete scantlings of the craft, ISO 12215-5 is intended to be used with
> ISO 12215-8 for rudders, ISO 12215-9 for appendages and ISO 12215-10 for rig loads."
> — iso.org. Confidence `documented`.

### ISO 12215-9 — Zweck und Geltungsbereich (verifiziert)

- **Geltungsbereich:** Lasten und Scantlings der Anhänge von **einrümpfigen
  Segelfahrzeugen bis 24 m L_H**. Erfasst **feste und kippende (canting) Kiele,
  Schwerter (centreboards) und Steckschwerter (daggerboards) sowie ihre Befestigung
  am Rumpf**. (ISO 12215-9, Scope) — `documented`
- **Was die Norm liefert:** Bemessungsspannungen (design stresses), die zu
  bewertenden Strukturbauteile, **Lastfälle und Bemessungslasten** für Kiel/Schwert
  und deren Befestigung, Rechenmethoden und Modellierungshinweise sowie die Nachweis-
  /Konformitätswege. — `documented`
- **Sicherheitsbegründung (Zitat sinngemäß, ISO/AFNOR-Scope):** „The loss of a keel
  leading to craft capsize is one of the major casualty hazards on sailing craft and
  therefore the structural efficiency of all elements of the keel and its connection
  to the craft is paramount." → **Kielverlust = Kentern**; deshalb gilt der
  Kielanschluss als hochkritisches Strukturelement. — `documented`

> **Wichtig (bekräftigt CLAUDE.md):** Für Kiel-Scantlings gilt **ISO 12215-9**, für
> Rumpfscantlings **ISO 12215-5** — **nicht** ISO 12217 (das nur Stabilität/Auftrieb
> bewertet).

### Revision ISO 12215-9 (Fassung 2025/2026) — verifiziert

Die Norm wird überarbeitet (ISO-Projekt Std. 85208; nationale Übernahme z. B.
SRPS EN ISO 12215-9:2026 in Vorbereitung). Laut begutachteter Fachpublikation
*„Regulatory Developments in Structural Keel Design: A Revised ISO 12215-9"*
(Aston University Research Explorer / ResearchGate 2024) umfasst die Revision:

1. **Neuer Lastfall „lateral impact"** (seitlicher Stoß) — bisher nicht abgedeckt. — `documented`
2. **Verpflichtende, strengere Ermüdungsbewertung** (fatigue) der Kielstruktur. — `documented`
3. **Verbesserte konstruktive Ausführung von Bolzen und Backing Plates**
   (Unterlegplatten), inkl. Abwägung Einzelschalen-Rumpflaminat vs. Backing-Plate-
   Dicke im Kielbereich und Behandlung der **Kielbolzen-Vorspannung**. — `documented`
4. **Informative Leitlinien zur Kielmontage** (keel installation procedures). — `documented`

> Quelle: research.aston.ac.uk / researchgate.net Publikation 379120751. Confidence `documented`.
> Genaue neue Gleichungen/Beiwerte stehen nur im Normtext → hier nicht wiedergegeben.

---

## II-2. Lastfälle und Bemessungsmethodik (dokumentierte Struktur, ohne Koeffizienten)

ISO 12215-9:2012 betrachtet **mehrere Lastfälle** (in der Literatur mit **sechs**
Lastfällen angegeben). Zwei sind für die Kielbefestigung führend:

| Lastfall | Bezeichnung | Physik / Nachweisort | Confidence |
|----------|-------------|----------------------|------------|
| **LC 1** | **90°-Knockdown (fester Kiel)** | Definiert Kraft **F1** und Bemessungs-**Biegemoment M1** bei **90° Krängung**, angesetzt am **Kielwurzel-/Bolzenniveau** bzw. an der **neutralen Faser der Bodenwrange (floor neutral axis)**. Üblicherweise die **schwerste Querbiegung** für feste Ballastkiele. | `documented` |
| **LC 3** | **Vertikaler Stoß / Grundberührung** | Vertikale **Pounding-Kraft am Kielboden** [N] — deckt Trockenfallen/Aufsetzen bzw. rein **vertikale, aufwärts gerichtete Grundberührung** ab. | `documented` |

> Quelle: ISO 12215-9:2012 (iso.org / scribd 741899436) und Aston-Publikation.
> „Load case 1 … force F1 and design bending moment M1 at 90° heel … at its root/bolt
> level and floor neutral axis"; „Load case 3 considers a vertical impact load in
> relation to events of dry-docking or purely vertical and upwards grounding …
> vertical pounding force exerted at keel bottom." Confidence `documented`.

**Methodik-Prinzip (belegt, qualitativ):**
- Die Norm gibt **Bemessungsspannungen** vor und benennt die **zu bewertenden
  Bauteile** der Lastkette: **Kielbolzen → Backing Plate/Unterlegplatte →
  Bodenwrangen (floors)/Matrix → Rumpfschale**. Jedes Glied ist einzeln nachzuweisen
  (das schwächste bestimmt die Sicherheit). — `documented`
- Nachweis wahlweise über **normative Formeln** oder **FEM** (die Norm gibt
  Modellierungshinweise). — `documented`
- Die Revision macht **Ermüdung verpflichtend** und ergänzt **seitlichen Stoß** —
  d. h. der reine Grounding-Vertikalstoß (LC 3) allein genügt künftig nicht. — `documented`

> ⚠️ ZU PRÜFEN (Audit): Die **Zahlenwerte** von F1/M1/LC3 (z. B. angesetzte
> Impact-Faktoren, Momentarme, Teilsicherheiten) stehen nur im Normtext und sind
> hier **bewusst nicht** angegeben. Die Rechenbeispiele in Teil I §2.2/§5 sind
> **nicht** aus der Norm abgeleitet und dürfen nicht als Normwerte zitiert werden.

---

## II-3. Kielbolzen-Werkstoffe — dokumentierte Werftrealität

Dies korrigiert und vertieft Teil I §2.1/§6 und FAQ F5.

| Werkstoff | Seewasser-Eignung (getaucht, Kielspalt) | Belege / Hinweise | Confidence |
|-----------|------------------------------------------|-------------------|------------|
| **304 / 304L** | **Ungeeignet** für Seewasser | Korrodiert schnell; nur Süßwasser | `documented` |
| **316 / 316L** | **Kritisch** — trotz „marine grade"-Ruf | „316 Stainless Steel cannot be used for critical applications immersed in seawater … suffers intense localised corrosion (crevice corrosion)"; einzelne Kiele versagten „almost as fast as ordinary steel", wenn Seewasser in den Spalt eindrang. Versagt gerade im **anaeroben, sauerstoffarmen** Kielsumpf-Spalt, wo die Passivschicht nicht erhalten bleibt. | `documented` |
| **Duplex 2205** | **Bevorzugt** (moderner Konsens) | „the Duplex Stainless family of alloys have become the preferred alloys for use as Keel Bolts in seawater immersion applications" — hohe Festigkeit **und** bessere Spaltkorrosionsbeständigkeit als 316. | `documented` |
| **Super-Duplex 2507** | **Sehr gut** | Für Hochsalz/High-Load; höchste Korrosionsbeständigkeit der genannten. | `documented` |
| **17-4 PH** | Herstellerangebot (z. B. MarsKeel) | Ausscheidungsgehärtet, hohe Festigkeit; Korrosionsverhalten anwendungsabhängig prüfen. | `documented` |
| **Aqualoy 22** | Herstellerangebot (Wellenwerkstoff-Familie) | Von Kielherstellern als Option gelistet. | `documented` |
| **Silizium-Bronze** | Traditionell geeignet | In der Literatur als „only truly appropriate material … in most circumstances" bezeichnet; unkritisch gegen Spaltkorrosion, dafür geringere Festigkeit → größerer Ø. | `documented` |
| **Feuerverzinkter/verzinkter Baustahl** | Nur Serienbau/Süßwasser, Verschleißteil | Von Serienwerften (Beneteau/Jeanneau/Hunter u. a.) verbreitet; „cheap option" — muss **regelmäßig geprüft und ersetzt** werden. | `documented` |

> Quellen: anzor.com.au/blog/keel-bolts; marskeel.com/resources/keel-bolt-material.
>
> **Werft-Fazit (documented):** Für dauergetauchte, kritische Kielbolzen in Seewasser
> ist **Duplex 2205 (bzw. 2507)** der Stand der Technik; **316/316L nur mit vollem
> Bewusstsein des Spaltkorrosionsrisikos** und intaktem, dauerhaft trockenem
> Bolzenspalt. Die pauschale Aussage „316L genügt" aus Teil I ist zu relativieren.

**Warum der Spalt tödlich ist (Mechanismus, documented):** Edelstahl benötigt
**Sauerstoff**, um die Passivschicht aufrechtzuerhalten. Im dauerfeuchten,
sauerstoffarmen **Kielsumpf-/Bolzenspalt** (Sealant-Versagen, stehendes Bilgewasser)
kommt es zu **Spaltkorrosion**: „A bolt that looks perfectly sound at the nut in the
bilge can be severely wasted at the sheathed section" — d. h. der Bolzen kann an der
Mutter oben makellos aussehen und im laminierten/geschlossenen Abschnitt stark
abgezehrt sein. (marine-inspect.co.uk)

---

## II-4. Kielbolzen-Vorspannung / Anziehen — belegtes Prinzip

Ergänzt Teil I §9 (Drehmoment). **Belegtes Prinzip (documented):** Die
**Vorspannkraft** eines Kielbolzens hängt ab von **Betriebskraft, Werkstoff von
Schraube und Mutter sowie Reibungskoeffizient**; die **Reibung im Gewinde und unter
dem Schrauben-/Mutterkopf macht oft bis zu 90 % des Anziehdrehmoments aus**
(Aston-Publikation, sinngemäß zu ISO 12215-9). → Das in Teil I §9 genannte
`T = K · F · d` mit stark streuendem K (0,08–0,20 je nach Schmierung) ist damit
**prinzipiell korrekt**, aber die **absoluten N·m-Werte in Teil I sind
estimated/unverifiziert**.

> **Konsequenz:** Drehmoment ohne bekannten, kontrollierten Reibwert ist ein
> **unzuverlässiges** Maß der tatsächlichen Vorspannung. Werftpraxis: definierte
> Schmierung (Herstellerangabe), ggf. **Dehnungs-/Längenmessung** statt reiner
> Drehmomentkontrolle, und **Re-Torque nach Herstellerintervall** (siehe II-6).
> Genaue Ziel-Vorspannungen/Beiwerte: nur Normtext + Bolzenlieferant. `documented`/`estimated`.

---

## II-5. Fehlerbild-Atlas (verifiziert, kollisionsfreie IDs FB-31-08-xxx)

> IDs bewusst im Schema **FB-31-08-NNN** — kollisionsfrei zu den 12 nummerierten
> „Fehleranalyse-Schwerpunkten" und zu den Pydantic-`fehlerbild_id`-Werten
> (`31_08_00x`) aus Anhang B. Jedes Fehlerbild trägt Beleg + Confidence.

### FB-31-08-001 — Spaltkorrosion Kielbolzen im anaeroben Kielsumpf
- **Fehlerbild:** Bolzen oben (Mutter/Bilge) optisch intakt, im laminierten/getauchten
  Abschnitt stark abgezehrt; ausgehend von Sealant-Versagen + stehendem Bilgewasser.
- **Diagnose:** Verfärbtes/rostiges Wasser im Kielsumpf als **Frühindikator** (noch
  vor sichtbarer Bewegung); endgültiger Nachweis nur durch **Bolzenziehen**.
- **Norm/Quelle:** marine-inspect.co.uk; anzor.com.au. **Confidence `documented`.**
- **Gegenmaßnahme:** Duplex-Bolzen, dauerhaft trockener Spalt, Sealant-Erneuerung,
  Re-Torque-Intervall einhalten.

### FB-31-08-002 — „Smile Crack" (Grinsen) an der Kiel-Rumpf-Fuge
- **Fehlerbild:** Gebogener Riss entlang der Kiel-Rumpf-Trennfuge, oft durch
  Antifouling sichtbar — **der bedeutsamste visuelle Einzelindikator für
  Kielbewegung**.
- **Diagnose:** Sichtkontrolle rund um die Fuge; Feuchtemessung; Perkussion.
- **Quelle:** marine-inspect.co.uk. **Confidence `documented`.**

### FB-31-08-003 — Herstellungsabweichung von der Konstruktionszeichnung (Kielstruktur)
- **Fehlerbild:** Kiel **nicht gemäß Designer-Zeichnung** gefertigt; kritische innere
  Schweißnähte (Rahmen↔Topplatte) im Bleiguss **verborgen und nicht inspizierbar**.
- **Realfall:** **„Tyger of London"** (Charter-Yacht, 07.12.2017, La Gomera→Teneriffa):
  Kiel versagte ohne Vorwarnung, Yacht kenterte in Sekunden; MAIB stellte fest, dass
  die Bolzen-Anzugskontrolle **nicht** den wahren Zustand des inneren Kielrahmens
  anzeigt.
- **Quelle:** MAIB via iims.org.uk / safety4sea.com. **Confidence `documented`.**

### FB-31-08-004 — Ermüdungsriss Kielanschluss (bisher unterbewertet)
- **Fehlerbild:** Rissbildung durch wiederholte Wellen-/Segellast an Bolzen, Wrangen
  oder Laminatanschluss; in ISO 12215-9:2012 nur begrenzt erfasst → **Revision macht
  Ermüdungsnachweis verpflichtend und strenger**.
- **Quelle:** Aston-Publikation. **Confidence `documented`.**

### FB-31-08-005 — Seitlicher Stoß (lateral impact) ohne Nachweis
- **Fehlerbild:** Kiel für **vertikale** Grundberührung (LC 3) ausgelegt, aber nicht
  für **seitlichen** Stoß (Fels/Container quer). Revision führt **neuen Lastfall
  lateral impact** ein → Altkonstruktionen ohne diesen Nachweis sind exponiert.
- **Quelle:** Aston-Publikation. **Confidence `documented`.**

### FB-31-08-006 — Unzureichende Backing Plate / Bodenwrangen (Lastkette)
- **Fehlerbild:** Schwächstes Glied ist nicht der Bolzen, sondern **Unterlegplatte
  oder Bodenwrange/Matrix**; Rumpflaminat im Kielbereich zu dünn ggü. Backing-Plate-
  Dicke. Revision adressiert genau diese **Abwägung Einzelschale ↔ Backing-Plate**.
- **Norm:** ISO 12215-9 (Bauteilkette Bolzen→Backing Plate→Wrangen→Schale). **Confidence `documented`.**

### FB-31-08-007 — Matrix-/Wrangenanbindung löst sich (Sekundärbindung)
- **Fehlerbild:** Innenmatrix/Bodenwrangen sekundär eingeklebt; Ablösung überträgt
  Kiellast direkt in die Rumpfschale.
- **Kontext:** MAIB-Sicherheitswarnung zu Kielversagen auf Segelyachten mahnt
  Inspektion der Kiel-Rumpf-/Matrix-Sicherung an.
- **Quelle:** gov.uk MAIB safety warning. **Confidence `documented`** (Mechanismus),
  Detailmaße `estimated`.

### FB-31-08-008 — Fehlendes Re-Torque-Protokoll
- **Fehlerbild:** Hersteller nennt Re-Torque-Intervall, aber **kein Nachweis** liegt
  vor → Surveyor wertet dies als **„material finding"** (wesentlicher Mangel).
- **Quelle:** marine-inspect.co.uk. **Confidence `documented`.**

> **Referenz-Realfälle (documented):** „Cheeki Rafiki" (2014, Kielverlust,
> Besatzung verloren — iims.org.uk/study-keel) und die generelle **MAIB Safety
> Warning „keel failures on sailing yachts"** (gov.uk) unterstreichen: Kielversagen
> tritt oft **ohne Vorwarnung** ein; äußere Sichtprüfung allein ist unzureichend.

---

## II-6. Inspektion, Prüffristen und Survey (verifiziert)

Ergänzt Teil I §10.

| Prüfpunkt | Vorgehen (belegt) | Confidence |
|-----------|-------------------|------------|
| Kiel-Rumpf-Fuge | Auf **Smile Crack** prüfen (bedeutsamster Sichtindikator) | `documented` |
| Kielsumpf | **Verfärbtes/rostiges Wasser = Frühindikator** für Bolzenkorrosion, noch vor Bewegung | `documented` |
| Bolzenzustand | Mutter/Washer-Interface + freiliegender Abschnitt; **kritische Zone (durch Laminat) nur durch Ziehen inspizierbar** | `documented` |
| Feuchte/Laminat | Feuchtemessung gegen trockene Referenz, **Perkussionstest quadrantenweise**, Unzugängliches explizit dokumentieren | `documented` |
| Re-Torque | Hersteller-Intervall prüfen; **fehlender Nachweis = material finding**. Praxisintervall in der Literatur genannt: **alle 7–10 Jahre** | `documented` (Prinzip), `estimated` (7–10 J.) |

> Quelle: marine-inspect.co.uk; safety4sea.com. **Wichtig:** Ein oben makelloser Bolzen
> kann im getauchten Abschnitt schwer abgezehrt sein → **Drehmoment-/Sichtprüfung
> ersetzt keine periodische Bolzenprüfung durch Ziehen** bei Verdacht.

---

## II-7. FAQ-Ergänzungen (verifiziert)

**F11: Welche Norm gilt wirklich für Kiel und Kielbefestigung?**
A: **ISO 12215-9** (Sailing craft appendages) für Kiel/Schwert + Befestigung,
zusammen mit **ISO 12215-5** für die Rumpfschale. **Nicht** ISO 12217 (nur
Stabilität/Auftrieb). Confidence `documented`.

**F12: Ist 316L wirklich ausreichend für Kielbolzen?**
A: Mit Vorbehalt. 316/316L gilt als „marine grade", **versagt aber gerade im
anaeroben Kielspalt durch Spaltkorrosion**. Moderner Standard für dauergetauchte
Kielbolzen: **Duplex 2205 / Super-Duplex 2507**. Silizium-Bronze ist die klassische
korrosionssichere (aber weichere) Alternative. Confidence `documented`.

**F13: Was ist der maßgebende Lastfall für einen festen Ballastkiel?**
A: In ISO 12215-9:2012 üblicherweise der **90°-Knockdown (LC 1)** für die
Querbiegung an Bolzen/Wrangen; zusätzlich **vertikale Grundberührung (LC 3)**. Die
Revision ergänzt **seitlichen Stoß** und **verpflichtende Ermüdung**. Confidence
`documented`. Zahlenwerte nur im Normtext.

**F14: Reicht Drehmomentkontrolle, um die Vorspannung zu sichern?**
A: Nur bedingt — **bis zu 90 % des Drehmoments gehen in Reibung**; ohne bekannten
Reibwert ist die reale Vorspannung unsicher. Besser: definierte Schmierung +
ggf. Längen-/Dehnungsmessung, plus Re-Torque nach Herstellerintervall. Confidence
`documented`.

---

## II-8. Glossar-Ergänzungen

**Backing Plate (Unterlegplatte):** Lastverteilende Platte zwischen Kielbolzen-Mutter
und Rumpfstruktur; Teil der Lastkette Bolzen→Backing Plate→Wrangen→Schale. In der
ISO-12215-9-Revision explizit behandelt.

**Bodenwrange (Floor):** Quer-/Längsträger über dem Kielanschluss, der die Kiellast in
den Rumpf einleitet; in LC 1 wird das Moment an der **neutralen Faser der Wrange**
nachgewiesen.

**Canting Keel (Kippkiel):** Seitlich schwenkbarer Ballastkiel; von ISO 12215-9
ausdrücklich erfasst.

**Crevice Corrosion (Spaltkorrosion):** Lokalisierte Korrosion in engen, sauerstoff-
armen Spalten (Kielsumpf) — Hauptversagensmechanismus von Edelstahl-Kielbolzen.

**Knockdown (90°):** Krängung auf 90°; maßgebender Querbiege-Lastfall (LC 1) fester
Ballastkiele in ISO 12215-9.

**L_H (Rumpflänge):** Längenmaß nach ISO 8666; Geltungsgrenze der ISO-12215-Reihe = 24 m.

**Smile Crack:** Gebogener Riss entlang der Kiel-Rumpf-Fuge; wichtigster Sichtindikator
für Kielbewegung.

---

## II-9. Quellen (Teil II)

- ISO 12215-9:2012 (Katalog) — iso.org/standard/55339.html
- ISO 12215-9 Revision (Projekt) — iso.org/standard/85208.html
- ISO 12215-5:2019 (Katalog) — iso.org/standard/69552.html
- Regulatory Developments in Structural Keel Design: A Revised ISO 12215-9 —
  research.aston.ac.uk / researchgate.net/publication/379120751
- Keel Bolts – which Stainless is best? — anzor.com.au/blog/keel-bolts
- Keel Bolt Material — marskeel.com/resources/keel-bolt-material
- Keel Integrity in Pre-Purchase Surveys — marine-inspect.co.uk/blog/keel-integrity-pre-purchase-survey-documentation
- Tyger of London — MAIB report (via IIMS) — iims.org.uk/keel-failure-and-capsize-of-charter-yacht-tyger-of-london-maib-report-published
- Study of a keel failure / Cheeki Rafiki — iims.org.uk/study-keel
- MAIB Safety warning about keel failures on sailing yachts — gov.uk/maib-reports/safety-warning-about-keel-failures-on-sailing-yachts
- UK MAIB: Lessons learned after yacht keel failure — safety4sea.com/uk-maib-lessons-learned-after-yacht-keel-failure

**Redaktion Teil II:** AYDI Knowledge Engineering — Web-verifizierte Audit-Erweiterung  
**Erstellt:** 2026-07-13  
**Regel:** Kein unverifizierter Fakt; Norm-Koeffizienten bewusst nicht rekonstruiert.
