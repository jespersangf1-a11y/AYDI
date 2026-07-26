# Kat 31.04 — Rigg-Dimensionierung

**Kategorie:** 31_Design_Konstruktion  
**Unterkategorie:** Rigg_Dimensionierung  
**Gültig ab:** 2025-01  
**Version:** 1.0  
**Sprache:** German (Inhalte), English (Code)

---

## 1. Grundlagen Rigg-Design

### 1.1 Funktion des Mastes und der Segelanlage

Ein Segler-Rigg hat mehrere Aufgaben:
- **Segel-Träger:** Mast und Baum halten Segelfläche
- **Last-Übertragung:** Segeldruck → Rumpf (über Mastschuh und Wanten/Stagen)
- **Trimmung:** Wanten und Laufende Takelage ermöglichen Segelverstellung
- **Sicherheit:** Struktur muss haltbar sein, darf nicht brechen/fallen

### 1.2 Klassische Rigg-Typen

**Sloop (eine Vorsegel, ein Großsegel):**
- Vereinfachte Takelage, niedrig Kosten
- Standard für kleine bis mittlere Cruiser
- Gutes Balance-Verhältnis

**Cutter (zwei Vorsegel, ein Großsegel):**
- Höhere Modularität (mehrere Vorsegel für verschiedene Wind)
- Großes Segelplan-Spektrum
- Klassisch für Cruising-Yachten

**Ketch/Yawl (Großsegel + Foresail + Mizzensegel):**
- Zwei Masten, kompliziertere Takelage
- Exzellent für lange Fahrten (besseres Balance bei Selbststeuerung)
- Höhere Instandhaltung

---

## 2. Mast-Dimensionierung

### 2.1 Mast-Profil und Material

**Übliche Profil-Geometrien:**

```
Rechteck (Box-Section):
  H × W × t (Höhe × Breite × Wanddicke)
  Typisch: 80×60 mm bis 150×100 mm für Cruiser
  Vorteil: Hohe Torsionssteifigkeit
  Nachteil: Höheres Gewicht

Kanal (Channel):
  Symmetrisch oder asymmetrisch
  Typisch: 80×35 mm bis 150×50 mm
  Vorteil: Leichter, aero-optimiert
  Nachteil: Niedrigere Torsionssteifigkeit

I-Profil:
  Selten, aber existiert (z.B. Superyacht)
  Hohe Biegungssteifigkeit
  Schwach in Torsion
```

**Material-Wahl:**

| Material | Dichte | E-Modul | Kosten | Korrosion | Anwendung |
|----------|--------|---------|--------|-----------|-----------|
| Aluminium 6061-T6 | 2.70 g/cm³ | 69 GPa | Mittel | Oxydation (wird weißlich) | Standard |
| Aluminium 7075-T73 | 2.81 g/cm³ | 72 GPa | Hoch | Salzwasser-geeignet | Hochleistung |
| Carbonfiber (Epoxy) | 1.60 g/cm³ | 230 GPa | Sehr hoch | Keine | Racing, Superyacht |
| Holz (Sitka Spruce) | 0.45 g/cm³ | 11 GPa | Mittel | Fäulnis-Risiko | Klassisch (selten modern) |

### 2.2 Mast-Länge und Aspekt-Verhältnis

**Mast-Länge (Höhe über Deck):**
```
h_mast ≈ 1.15 bis 1.35 × LWL  (abhängig Rigg-Typ und Klasse)
Beispiel: 12m LWL → h_mast ≈ 14–16m
```

**Segelplan-Aspekt-Verhältnis:**
```
AR_sail = h_luff² / Segelgebiet  (in m²)
Beispiel: Luff 15m, Segelgebiet 60 m² → AR ≈ 3.75

Hochleistungs-Segler: AR > 4.0 (schmale tiefe Segel)
Cruising-Standard: AR = 3.0–3.5
```

### 2.3 Mast-Analyse — Kritische Lastfälle

**Lastfall 1: Halse (Run vor dem Wind, Segelwechsel):**
```
Seitliche Kraft auf Mast ≈ 0.5 × Wind-Druck × Segelgebiet
Typisch: 2–5 kN laterale Kraft
Belastung: Beugung in Richtung quer-Schiff
```

**Lastfall 2: Tieft-Lauf (Luvsegler-Positionen, hohem Wind):**
```
Laterale Kraft ≈ Wind-Druck × (Segelgebiet × sin(Heel-Winkel))
Typisch: 5–15 kN (je nach Segelplan-Größe und Wind)
```

**Lastfall 3: Anluvende Manöver (Wende):**
```
Dynamische Spike = 1.5–2.0 × statische Last (Beschleunigungseffekt)
Kritisch bei Segel-Wechsel
```

---

## 3. Wanten und Stagen

### 3.1 Oberwanten (Upper Shrouds)

Vertikale (oder leicht schräge) Kabel von Mastspitze zu Mastfüßen auf Rumpf.

**Funktion:** Laterale Stabilisierung des Mastes gegen Seitenkräfte

**Dimensionierung:**
```
Spannung_zul = Zugfestigkeit / Safety_Factor
              = 1770 MPa (Stahl) / 2.5 = 708 MPa typisch

Erforderliche Querschnittsfläche:
A_required = Lastfall_Kraft / Spannung_zul

Beispiel: 10 kN Last, 2 Wanten
  10000 N / 2 / 708 MPa = 7.1 mm² pro Wante
  → Üblicher 6 mm Stahl-Draht oder ähnlich
```

**Typische Anordnung:**
```
Oberwanten: 2 oder 4 (paarweise Stb/Bb)
Abstand auf Mast-Kopf: 1–3m unter Mastspitze
Winkel zur Vertikal: 10–20°
```

**Material:**
- **Stahldraht (Edelstahl 316):** Preiswert, schwer (~8 g/m × 6mm)
- **Dyneema (HMPE):** Leicht (~0.15 g/m), teuer, kriechen-anfällig
- **Carbon-Draht:** Selten, sehr teuer, bruchanfällig

### 3.2 Unteren Wanten (Lower Shrouds)

Vorderward und nach-unten geneigt (oft mit Spreizern für Breite).

**Funktion:** Zusätzliche laterale Unterstützung, reduzieren Mast-Durchbiegung

**Typische Anordnung:**
```
Unten-Wanten: 2–4 pro Seite (abhängig Mast-Länge)
Winkel zur Vertikal: 25–40° (stärker geneigt als Oberwanten)
Spreizer (Spreader): Erhöhen effektive Breite der Wanten-Befestigung
  Spreizer-Abstand: 0.3–0.5 × Mast-Höhe von oben
  Spreizer-Länge: 1.0–2.5m (dient als Hebel)
```

### 3.3 Forestay (Vorliegende Stag)

Kabel von Mastspitze zu Bug-Bügel, hält Segel (Foresail/Jib).

**Span-Kraft:**
```
Spannung_Forestay ≈ 1.5 × Segel-Zug
Typisch: 2–8 kN für Cruising-Segler
```

**Bauweise:**
- **Starre Stag (Rod):** Carbon oder Stahl, höhere Präzision für Race-Boote
- **Draht-Stag:** Klassisch, einfacher einzustellen
- **Laufende Stag (Running Backstay):** Optional, reduziert Mast-Durchbiegung

### 3.4 Backstay (Achterliche Stag)

Kabel von Mastspitze zum Heck-Bügel, stabilisiert Mast gegen Vorwärtskräfte.

**Span-Kraft:**
```
Spannung ≈ 0.8–1.5 × Forestay-Spannung
Typisch: 2–10 kN
```

**Bauweise:**
- **Einfach Backstay:** Fest gespannt
- **Laufend Backstay:** Doppelte Kabel, oberster ist einstellbar (Race-Feature)

---

## 4. Mastschuh und Takelage-Befestigung

### 4.1 Mastschuh (Mast-Step)

Struktur, welche Mast zu Rumpf verbindet. Überträgt alle Kräfte (vertikal, lateral, Torsion).

**Design-Anforderungen:**
```
Basis-Fläche ≥ Mast-Querschnitt × 3  (typisch 150–200 mm Durchmesser Ring)
Höhe (Tiefe) ≥ Mast-Höhe / 50  (typisch 150–300 mm)
Material: Aluminium (wenn Rumpf FRP), verstärkte FRP Sandwich, oder Edelstahl
Verankerung: Min. 4 Bolzen M10 oder äquivalent, in verstärkte Zone des Rumpfes
```

**Belastungen auf Mastschuh:**
```
Vertikal (Gewicht): 200–500 kg (abhängig Mast-Material und Länge)
Lateral (Wind): 5–20 kN (abhängig Segelplan)
Torsion: 2–10 kN·m (abhängig Baumstöße und Manöver)
```

### 4.2 Kettenplatte (Chainplates) für Wanten

Befestigungspunkte für Wanten auf der Rumpfseite.

**Anordnung:**
```
Obere Kettenplatte: ~1–2m unter Mastspitze, seitlich Rumpf
Untere Kettenplatte: ~2–4m tiefer, etwas outboard (Spreizer)
Abstände zwischen Platten: ≥ 500–800 mm (abhängig Mast-Länge)
```

**Belastung pro Kettenplatte:**
```
Typisch: 3–10 kN (abhängig Wanten-Spannung und Anzahl)
Befestigung: 4 Bolzen M8–M10 in Rumpf-Verstärkungszone
```

**Material:**
- **Edelstahl (316):** Korrosionsresistent, Standard
- **Aluminium:** Leichter, schnellere Korrosion (galvanische Isolierung erforderlich)
- **Bronze:** Klassisch, kostspielig, selten modern

---

## 5. Baum und Gäbelbaum

### 5.1 Baum (Boom)

Spendet Großsegel von unten. Üblicher Material: Aluminium (Box-Sektion) oder Carbon.

**Dimensionen:**
```
Länge: 0.8–1.0 × Lauf-Länge des Großsegels
Profil: Ähnlich Mast (Box-Section oder Channel)
Typisch: 60×40 mm bis 100×60 mm Querschnitt
```

**Belastungen:**
```
Vertikales Moment (Segelgewicht + Druck): 1–5 kN
Laterale Torsion (Boom-Bewegung): 1–3 kN·m
```

**Baum-Befestigung:**
```
Gooseneck (Mast-Verbindung): Metallisches Gelenk mit Stift oder Kugellager
Achterliche Brille (Aft-End Fitting): Kann Booms-Bremsvorrichtung oder Sensor halten
```

### 5.2 Gäbelbaum (Boom-Vang oder Kicker)

Kabel oder Stab von Mast zu Baum-Ende, verhindert Baum-Hochlauf bei tiefem Wind.

**Bauweise:**
- **Hydraulisch:** Kompakt, einfach zu bedienen, kostspielig
- **Mechanisch (Flaschenzug):** Preiswert, langwierig zu bedienen
- **Starre Stab (Rod Vang):** Für Race-Boote

---

## 6. Fehleranalyse — 12 Fehlermuster

### 6.1 [F6.1] Zu dünner Mast-Querschnitt (Biegeversagen)

**Symptom:**
- Mast biegt sich deutlich unter Wind (z.B. 300–500 mm Durchbiegung bei 12m Mast)
- Sichtbar: Mast ist gebogen, nicht gerade
- Spannungen in Wanten erhöht

**Ursache:**
- Zu niedriges Mast-Profil dimensioniert (Gewichtsersparnis)
- Keine ausreichende Steifigkeits-Analyse durchgeführt
- Material-Wahl zu leicht (z.B. zu dünnes Aluminium)

**Folgen:**
```
Durchbiegung_Mast = (Wind-Kraft × h_Mast³) / (3 × E × I)
Zu große Durchbiegung führt zu:
  − Segelform verschlechtert (Segel-Leistung sinkt ~5–15%)
  − Spannungen in Wanten und Maststschuh erhöht
  − Größere Biegespannungen im Mast selber
  − Ermüdungsfestigkeit reduziert
  − Vibrationen und Rattling möglich
```

**Empforlicht Korrektion:**
```
Ziel-Durchbiegung: ≤ 1/150 × Mast-Höhe
  Beispiel: 15m Mast → Durchbiegung ≤ 100 mm

Vergrößerung Trägheitsmoment I:
  − Größeres Profil (z.B. 80×60 statt 70×50)
  − Dickere Wände (z.B. 2.5 mm statt 2.0 mm)
  − Carbon-Mast (E ≈ 230 GPa vs. Alu ≈ 70 GPa)

Oder: Zusätzliche Wanten/Spreizer zur Unterstützung
```

**Prüfkriterium:** Mast-Durchbiegung > L/100 unter Design-Wind → Überprüfung

---

### 6.2 [F6.2] Ungenügende Wanten-Spannung (Mast fällt zur Seite)

**Symptom:**
- Mast-Neigung zur Seite unter Wind (nicht vertikal)
- Wanten sind schlaff (keine Vorbeanspruchung)
- Mast kann in leichtem Wind bereits wackeln

**Ursache:**
- Wanten zu dünn dimensioniert
- Wanten-Spannung nicht korrekt eingestellt
- Zu wenige Wanten (nur 2 statt 4 z.B.)

**Folgen:**
- Mast-Stabilität verloren
- Höhere Biegespannungen im Mast (nicht mehr "dreieckig" gestützt)
- Bruchrisiko erhöht
- Sicherheit: Mast-Bruch oder -Fall möglich

**Empforlicht Korrektion:**
```
Wanten-Spannung Ziel:
  Vorbeanspruchung ≈ 5–15% der Mast-Höhe-Last
  Beispiel: 15m Mast, Wind-Last 15 kN → Vorbeanspruchung 0.75–2.25 kN

Wanten-Dicke:
  Pro Wante ≈ Gesamt-Last / Anzahl-Wanten / Zugfestigkeit

Überprüfung: Wanten sollten immer unter Spannung sein
             Auch im leichten Wind sollte keine "Slappage" sichtbar sein
```

**Prüfkriterium:** Wanten-Vorspannung < 0.5 kN → Überprüfung/Nachspannung

---

### 6.3 [F6.3] Falscher Spreizer-Winkel (Wanten-Geometrie fehlerhaft)

**Symptom:**
- Spreizer-Position: zu nah am Mast (Winkel < 15°) oder zu weit (> 45°)
- Wanten beißen unkontrolliert in Spreizer ein
- Unausgewogene Laterale Kräfte

**Ursache:**
- Spreizer nicht nach Rigg-Geometrie dimensioniert
- CAD-Fehler in Spreizer-Abstand oder -Winkel

**Folgen:**
- Ineffiziente Spreizer-Funktion (sollte Wanten auseinander drücken)
- Höhere Spannungen im Spreizer
- Spreizer-Bruch möglich
- Mast-Stabilität beeinträchtigt

**Empforlicht Korrektion:**
```
Zielwinkel Spreizer-Wanten-Winkel: 30–40°
  (Winkel zwischen Obere-Wante und Spreizer zur Seite)

Spreizer-Länge ≈ 1.0–2.0m (abhängig Mast-Breite)
Spreizer-Abstand vom Mast-Kopf ≈ 0.3–0.5 × Mast-Höhe

Überprüfung: Spreizer sollte "auseinander drücken", nicht "schieben"
```

**Prüfkriterium:** Spreizer-Winkel < 20° oder > 50° → Überprüfung

---

### 6.4 [F6.4] Mastschuh zu schwach ausgelegt (Befestigung unzureichend)

**Symptom:**
- Rumpf um Mastschuh: Risse oder Eindellung
- Mastschuh "wandert" oder lockert sich
- Wasser-Leckage um Mastschuh

**Ursache:**
- Mastschuh-Verankerung nur 2–3 Bolzen statt 4+
- Mastschuh-Ring zu klein
- Rumpf-Verstärkung unzureichend

**Folgen:**
- Strukturelles Versagen möglich
- Mast kann ausfallen (Sicherheit-Katastrophe)
- Rumpf-Risse kritisch

**Empforlicht Korrektion:**
```
Mastschuh-Basis-Größe:
  Durchmesser ≥ Mast-Breite × 2.5–3.0
  Beispiel: 80mm Mast → ~200–240mm Ring-Durchmesser

Verankerung:
  Min. 4 Bolzen M10 oder äquivalent (je nach Material)
  In verstärkte Zone: Sandwich oder extra-Laminat um Bolzenlöcher
  Sicherheitsfaktor ≥ 3.0 auf Bolzen-Scherfestigkeit

Dichtung: Wasserdichter Übergang (Silikon oder Mastschuh-Ring mit Dichtung)
```

**Prüfkriterium:** Mastschuh mit < 4 Bolzen oder Ring-Durchmesser < 150mm → Fehler

---

### 6.5 [F6.5] Kettenplatte falsch positioniert (zu nah oder zu weit Außenbord)

**Symptom:**
- Wanten-Winkel zu steil oder zu flach
- Unausgewogene Kraft-Komponenten in Rumpf
- Rumpf-Verformung neben Kettenplatte

**Ursache:**
- Kettenplatte nicht nach Rigg-Geometrie dimensioniert
- Outboard-Abstand nicht beachtet

**Folgen:**
```
Wenn Wante zu flach (Kettenplatte zu nah an Mittellinie):
  − Weniger laterale Stabilisierung des Mastes
  − Mehr vertikale Last auf Rumpf
  
Wenn Wante zu steil (Kettenplatte zu weit außenbord):
  − Höhere laterale Kräfte
  − Rumpf-Verspreizung möglich
  − Spannungs-Konzentration
```

**Empforlicht Korrektion:**
```
Ziel-Winkel Wante zur Vertikal:
  Obere Wanten: 10–20° von Vertikal
  Untere Wanten: 25–40° von Vertikal

Outboard-Abstand:
  Min. 300–500 mm von Schiffsmittellinie
  Typisch: 0.4–0.6 × Rumpf-Breite

Überprüfung: Wanten sollte glattes V-Muster bilden, nicht zu spitz
```

**Prüfkriterium:** Wante-Winkel < 8° oder > 45° → Überprüfung

---

### 6.6 [F6.6] Forestay-Spannung zu hoch (Bugbügel belastet übermäßig)

**Symptom:**
- Bugbügel hat Risse oder Verformung
- Forestay ist steif (kann nicht eingestellt werden)
- Mast biegt sich rückwärts (bow-aft)

**Ursache:**
- Forestay zu dünn → zu hohe Spannung notwendig für Starrheit
- Zu aggressive Wind-Vorhersage
- Mast-Material zu schwach (zu dünn)

**Folgen:**
- Bugbügel-Bruch möglich (Mast-Fall-Risiko)
- Mast excessive rearward-bending
- Segelform schlecht (Segel zu flat)

**Empforlicht Korrektion:**
```
Forestay-Spannung Ziel:
  Vorbeanspruchung ≈ 2–5 kN typisch für 12m Cruiser
  Maximum: 8–10 kN (abhängig Material und Durchmesser)

Forestay-Material:
  Dicke: 6–8 mm Edelstahl oder 5–6 mm Carbon-Rod

Mast-Längs-Durchbiegung Ziel:
  ≤ 1/150 × Mast-Höhe (ähnlich laterale)
  Zu viel Rückwärts-Biegung (>100mm) schwächt Segelform
```

**Prüfkriterium:** Forestay-Spannung > 10 kN mit üblichem 6mm Draht → Überprüfung

---

### 6.7 [F6.7] Backstay-Spannungs-Unausgewogenheit (nicht symmetrisch)

**Symptom:**
- Mast neigt sich zur Seite (nicht nur vertikal)
- Backstay Stb hat andere Spannung als Bb
- Mast sichtbar windschief

**Ursache:**
- Backstay nicht symmetrisch befestigt
- Unterschiedliche Draht-Länge oder Durchmesser
- Heck-Struktur unsymmetrisch

**Folgen:**
- Mast-Neigung → höhere Spannungen asymmetrisch
- Segelform verzerrt (Segel sucht asymmetrisches Gleichgewicht)
- Struktur-Überlastung einseitig
- Sicherheit: Bruch auf Seite mit höherer Spannung möglich

**Empforlicht Korrektion:**
```
Backstay-Spannung überprüfen:
  Beide Seiten sollten gleich gespannt sein (±0.5 kN Toleranz)
  
Längen überprüfen:
  Steuerbord und Backbord Backstay sollten identisch sein
  (Wenn unterschiedlich: Verkürzung oder Längung notwendig)

Symmetrie-Check:
  Mast sollte vertikal stehen (mit Lot überprüfen)
  Keine Neigung zur Seite akzeptabel
```

**Prüfkriterium:** Mast-Neigung > 50 mm zur Seite oder Spannungs-Diff > 2 kN → Überprüfung

---

### 6.8 [F6.8] Mastschuh-Befestigung zu eng oder zu locker (Verdrehung möglich)

**Symptom:**
- Mast dreht sich in Mastschuh (rotiert um Längsmittellinie)
- Mastschuh wirkt "locker" oder rattert
- Segel-Trim nicht stabil (Mast rollt herum)

**Ursache:**
- Mastschuh-Nut (wenn eingerastet) zu locker
- Befestigung zu locker oder nicht durchgehend angezogen
- Mastschuh-Durchmesser nicht angepasst (zu groß)

**Folgen:**
- Mast-Rotation unter Wind-Last
- Segel-Form variabel und instabil
- Mastschuh-Verschleiß erhöht
- Vibrationen und Rattling

**Empforlicht Korrektion:**
```
Mastschuh-Überprüfung:
  − Alle Befestigung-Bolzen überprüfen und nachziehen (torque spec.)
  − Nut oder Ring-Fit sollte <2mm Spiel haben
  − Mast sollte fest sein, keine Verdrehung unter Hand-Kraft

Wenn Mastschuh zu locker:
  − Neue Buchsen/Shims erforderlich (Abstände erhöhen)
  − Oder: Mastschuh-Durchmesser überprüfen und ggf. Mast tauschen

Oder: Rotierende Mastschuh (mit Kugellager) verwenden (kostspielig aber elegant)
```

**Prüfkriterium:** Mast-Drehung > 2–3° unter Hand-Druck → Überprüfung

---

### 6.9 [F6.9] Wantensplitter oder Verschleiß (Draht-Bruch möglich)

**Symptom:**
- Visuelle Inspekt: einzelne Drähte aus Wante herausstehend
- Wante-Länge scheint zu ändern
- Verlust Vorbeanspruchung (Wante wird locker)

**Ursache:**
- Wante-Material degradiert (Rost, Korrosion)
- Überlast oder Schlag auf Wante
- Material-Fehler oder schlechte Installation

**Folgen:**
- Wante-Bruch möglich (komplett oder teilweise)
- Mast-Stabilität reduziert
- Wenn Wante reißt: Mast fällt zu dieser Seite

**Empforlicht Korrektion:**
```
Prävention:
  − Wanten aus Edelstahl 316 verwenden (nicht niedrig-Kosten-Material)
  − Regelmäßige Inspekt (jährlich)
  − Splitter abschleifen/verwenden Korrosions-Inhibitor

Reparatur/Ersatz:
  − Sichtbare Splitter: komplett Wante tauschen (nur tauschen, nicht reparieren)
  − Abstand bei Inspektion überprüfen (sollte stabil sein)

Material-Spezifikation:
  Edelstahl 1×19 (19 Drähte pro Laye) oder 7×19 (7 Lagen × 19 Drähte)
  Zugfestigkeit: ≥ 1770 MPa für Segler
```

**Prüfkriterium:** Sichtbare Splitter oder Korrosion → Ersatz erforderlich

---

### 6.10 [F6.10] Baum-Befestigung locker (Gooseneck-Spiel)

**Symptom:**
- Baum hat Spiel in Gooseneck (kann vertikald hochgezogen werden)
- Baum-Position nicht stabil (wandert herum)
- Knarren oder Klicken Geräusche beim Segel-Trim

**Ursache:**
- Gooseneck-Stift oder Kugellager verschlissen
- Befestigung nicht angezogen
- Gooseneck-Design zu locker

**Folgen:**
- Segel-Trim schwierig (Baum bewegt sich mit Mast-Bewegung)
- Verschleiß am Gooseneck erhöht
- Strukturelles Risiko (Baum kann aufheben unter bestimmten Bewegungen)

**Empforlicht Korrektion:**
```
Gooseneck-Überprüfung:
  − Alle Bolzen nachziehen (4–6 Nm typisch)
  − Spiel sollte < 2–3 mm sein in alle Richtungen
  − Kugellager (wenn vorhanden) sollte glatt drehen, kein Rattern

Wenn Verschleiß zu groß:
  − Gooseneck-Stift tauschen (kleine Komponente, einfach)
  − Kugellager ggf. tauschen
  − Oder: Kompletter Gooseneck-Montage erneuern
```

**Prüfkriterium:** Gooseneck-Spiel > 5 mm → Überprüfung/Reparatur

---

### 6.11 [F6.11] Spreizer-Bruch oder Verbiegung (unerwartete Last)

**Symptom:**
- Spreizer-Ende hängend oder verbogen
- Spreizer-Winkel nicht mehr symmetrisch
- Wanten-Position verschoben

**Ursache:**
- Spreizer-Material zu schwach
- Crash oder Schlag (z.B. Baum-Jibe gegen Spreizer)
- Laster-Fahrt oder Hängenbleiben am Dock

**Folgen:**
- Spreizer-Funktion verloren (Wanten nicht mehr auseinandergedrückt)
- Mast-Stabilität reduziert
- Höhere Spannungen im Mast
- Wanten können überlastet werden

**Empforlicht Korrektion:**
```
Spreizer-Material Ziel:
  Aluminium 6061-T6 oder Carbon-Faser
  Durchmesser: 25–40 mm (abhängig Länge und Mast-Kraft)

Bruch-Sicherung:
  − Spreizer sollte mit Schnappkarabiner oder Sicherheits-Lein befestigt sein
  − Wenn Spreizer bricht: sollte nicht vollständig ausfallen

Reparatur/Ersatz:
  − Spreizer-Bruch: Vollständig tauschen (Reparatur nicht empfohlen)
  − Neuer Spreizer sollte identische Länge und Winkel haben
```

**Prüfkriterium:** Spreizer verbogen oder gebrochen → Ersatz erforderlich

---

### 6.12 [F6.12] Mast-Profil nicht quellbeständig oder optimiert (falsche Querschnitts-Wahl)

**Symptom:**
- Mast beugt sich oder dellt ein leicht
- Profile zeigt Dellen oder Verformungen nach Seaseason
- Torsionssteifigkeit variabel

**Ursache:**
- Box-Profil zu dünn (2.0 mm statt 2.5 mm Wanddicke)
- Nicht quellbeständiger Alu-Legierung (z.B. 5083 statt 6061-T6)
- Zu viel Wasser eindrang (Hohlraum nicht versiegelt)

**Folgen:**
- Mast-Beule oder Dellen (visuelle Probleme)
- Dellen können Stress-Konzentration sein (Riss-Initiierung möglich)
- Steifigkeit reduziert
- Lebensdauer verkürzt

**Empforlicht Korrektion:**
```
Mast-Profil-Spezifikation:
  − Material: Aluminium 6061-T6 (Seewasser-geeignet)
  − Wanddicke: Min. 2.5 mm (typisch 2.5–3.0 mm für Cruiser)
  − Box-Profil: H × W × t mindestens 80×60×2.5 für 12m Segler

Versiegelung:
  − Mast-Hohlraum sollte versiegelt sein (nicht offen für Wasser)
  − Drainagelöcher unten zum Ablassen von Wasser
  − Oder: Vollständig versiegeltes Profil (Carbon ideal)

Überprüfung nach Saison:
  − Visuell auf Dellen inspizieren
  − Risse um Dellen überprüfen
  − Torsions-Test durchführen (sollte steif sein)
```

**Prüfkriterium:** Dellen oder Einbiegungen sichtbar → Inspektion auf Risse, ggf. Mast-Tausch

---

## 7. Rigg-Tuning und Wartung

### 7.1 Vor-Saison-Überprüfung

- [ ] Alle Wanten auf Spannung überprüfen (ggf. nachspannen)
- [ ] Forestay und Backstay auf Verschleiß inspizieren
- [ ] Mastschuh-Bolzen nachziehen
- [ ] Kettenketten auf Risse überprüfen
- [ ] Gooseneck auf Spiel überprüfen
- [ ] Spreizer auf Verformung inspizieren
- [ ] Baum-Befestigung überprüfen

### 7.2 Laufende Wartung

- Nach Stürmen: Überprüfung auf Schäden
- Jährlich: Korrosions-Inhibitor auf Stahl-Wanten anwenden
- Regelmäßig: Rigg-Spannung überprüfen (beim Aufrigg)

---

## 8. Normen und Standards

### 8.1 ISO 12216 (Fenster und Luken)

Nicht direkt Rigg, aber regelt Öffnungen in Segelkonstruktion (z.B. Fenster in Großsegel-Fach)

### 8.2 ABS / DNV-GL Rules für Segelschiffe

Optionale Class-Anforderungen für professionelle Yachten

---

## 9. ANHANG — Pydantic v2 Model

```python
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from enum import Enum
from datetime import datetime

class RiggTypeEnum(str, Enum):
    SLOOP = "sloop"
    CUTTER = "cutter"
    KETCH = "ketch"
    YAWL = "yawl"
    CATBOAT = "catboat"

class MastMaterialEnum(str, Enum):
    ALUMINIUM_6061 = "alu_6061"
    ALUMINIUM_7075 = "alu_7075"
    CARBON_FIBER = "carbon"
    STAINLESS_STEEL = "stainless_steel"
    WOOD_SPRUCE = "wood_spruce"

class WireTypeEnum(str, Enum):
    STAINLESS_316 = "ss_316"
    DYNEEMA = "dyneema"
    CARBON_WIRE = "carbon_wire"
    STAINLESS_ROPE = "ss_rope"

class MastSpecification(BaseModel):
    """Mast-Spezifikation und Dimensionen"""
    model_config = {"from_attributes": True}
    
    mast_id: str = Field(..., description="Unique mast identifier")
    material: MastMaterialEnum = Field(..., description="Mast material")
    length_mm: float = Field(..., gt=0, description="Mast length (mm)")
    
    # Profile Dimensionen
    section_height_mm: float = Field(..., description="Profile height (mm)")
    section_width_mm: float = Field(..., description="Profile width (mm)")
    wall_thickness_mm: float = Field(..., description="Wall thickness (mm)")
    
    # Steifigkeits-Parameter
    bending_modulus_gpa: Optional[float] = Field(None, description="Bending modulus (GPa)")
    moment_of_inertia_mm4: Optional[float] = Field(None, description="Moment of inertia (mm⁴)")
    
    # Gewicht
    weight_kg: Optional[float] = Field(None, description="Mast weight (kg)")
    
    # Belastungen
    max_bending_stress_mpa: Optional[float] = Field(None, description="Max bending stress (MPa)")
    max_deflection_mm: Optional[float] = Field(None, description="Max deflection (mm)")

class StaySpecification(BaseModel):
    """Stag und Wanten-Spezifikation"""
    model_config = {"from_attributes": True}
    
    stay_id: str = Field(..., description="Stay identifier (e.g., 'Upper_Shroud_Port')")
    stay_type: str = Field(..., description="Type (Upper_Shroud, Lower_Shroud, Forestay, Backstay)")
    
    wire_material: WireTypeEnum = Field(..., description="Wire material")
    wire_diameter_mm: float = Field(..., gt=0, description="Wire diameter (mm)")
    length_mm: Optional[float] = Field(None, description="Stay length (mm)")
    
    # Spannungen
    pre_tension_kn: Optional[float] = Field(None, description="Pre-tension (kN)")
    working_load_kn: Optional[float] = Field(None, description="Working load (kN)")
    
    # Befestigung
    upper_attachment: str = Field(..., description="Upper attachment point (e.g., 'Mast_Top')")
    lower_attachment: str = Field(..., description="Lower attachment point (e.g., 'Chainplate_Port')")
    angle_to_vertical_deg: Optional[float] = Field(None, description="Angle to vertical (deg)")

class RiggingSystem(BaseModel):
    """Komplettes Rigging-System"""
    model_config = {"from_attributes": True}
    
    vessel_name: str = Field(..., description="Yacht name")
    rigging_type: RiggTypeEnum = Field(..., description="Rigging type")
    
    # Mast(e)
    main_mast: MastSpecification = Field(..., description="Main mast")
    jib_mast: Optional[MastSpecification] = Field(None, description="Fore mast (Cutter/Ketch)")
    mizzen_mast: Optional[MastSpecification] = Field(None, description="Mizzen mast (Ketch/Yawl)")
    
    # Boom
    main_boom: Optional[MastSpecification] = Field(None, description="Main boom (similar to mast in structure)")
    jib_boom: Optional[MastSpecification] = Field(None, description="Jib boom")
    
    # Stays and Shrouds
    stays: List[StaySpecification] = Field(default_factory=list, description="All stays and shrouds")
    
    # Spreader
    spreader_length_mm: Optional[float] = Field(None, description="Spreader length (mm)")
    spreader_angle_deg: Optional[float] = Field(None, description="Spreader angle (deg)")
    
    # Segelplan
    mainsail_area_m2: Optional[float] = Field(None, description="Mainsail area (m²)")
    jib_area_m2: Optional[float] = Field(None, description="Jib area (m²)")
    total_sail_area_m2: Optional[float] = Field(None, description="Total sail area (m²)")
    
    # Analyse
    analysis_date: datetime = Field(default_factory=datetime.now)
    condition_notes: List[str] = Field(default_factory=list, description="Notes on condition")
    maintenance_required: List[str] = Field(default_factory=list, description="Required maintenance items")

def calculate_mast_deflection(
    wind_load_kn: float,
    mast_length_mm: float,
    moment_of_inertia_mm4: float,
    bending_modulus_gpa: float
) -> dict:
    """Berechne Mast-Durchbiegung unter Wind-Last"""
    E = bending_modulus_gpa * 1000  # Convert to MPa
    I = moment_of_inertia_mm4
    L = mast_length_mm
    F = wind_load_kn * 1000  # Convert to N
    
    # Simplified: assuming point load at mast head
    deflection_mm = (F * (L ** 3)) / (3 * E * I)
    
    limit_mm = L / 150  # Target: L/150
    
    return {
        "deflection_mm": round(deflection_mm, 1),
        "limit_mm": round(limit_mm, 1),
        "acceptable": deflection_mm <= limit_mm,
        "margin_percent": ((limit_mm - deflection_mm) / limit_mm * 100) if limit_mm > 0 else 0
    }

def calculate_wire_area_required(
    load_kn: float,
    num_wires: int,
    material: str,
    safety_factor: float = 2.5
) -> dict:
    """Berechne erforderliche Draht-Querschnittsfläche"""
    
    material_strength = {
        "ss_316": 1770,  # MPa
        "dyneema": 2800,  # MPa
        "carbon": 2500,  # MPa
    }
    
    strength_mpa = material_strength.get(material, 1770)
    allowable_stress = strength_mpa / safety_factor
    
    total_force_n = load_kn * 1000
    per_wire_n = total_force_n / num_wires
    area_per_wire_mm2 = per_wire_n / allowable_stress
    
    # Common wire diameters and areas
    diameters = {
        4: 12.6,
        5: 19.6,
        6: 28.3,
        8: 50.3,
        10: 78.5,
    }
    
    suitable_diameter = None
    for d_mm, a_mm2 in diameters.items():
        if a_mm2 >= area_per_wire_mm2:
            suitable_diameter = d_mm
            break
    
    return {
        "required_area_mm2": round(area_per_wire_mm2, 1),
        "recommended_diameter_mm": suitable_diameter,
        "safety_factor_applied": safety_factor,
        "allowable_stress_mpa": round(allowable_stress, 1)
    }
```

---

# TEIL II — WERFT-TIEFE (web-verifizierte Erweiterung)

> **Status dieser Erweiterung:** Version 2.0 (2026-07). Alle faktischen Angaben in Teil II
> (Normen, Bruchlasten, Verfahren) sind an autoritativer Quelle verifiziert und inline
> belegt (Confidence `documented`). Rein unit-basierte Umrechnungen (kg → kN, lbs → kN)
> sind als solche gekennzeichnet.
>
> **⚠️ Wichtiger Hinweis zu Teil I (Abschnitte 1–9):** Die in Teil I genannten Zahlenbereiche,
> Formeln und Koeffizienten (z. B. `h_mast ≈ 1.15–1.35 × LWL`, `Spannung_Forestay ≈ 1.5 × Segel-Zug`,
> Safety-Factor 2.5, die Punktlast-Durchbiegungsformel) sind **Legacy-Schätzwerte
> (`estimated — unverifiziert`)** aus der ursprünglichen Fassung und **nicht** aus Normtext
> abgeleitet. Sie dienen der Orientierung, ersetzen **keine** Bemessung nach ISO 12215-10.
> Für lastrelevante Auslegung gilt ausschließlich der Normtext bzw. eine qualifizierte
> Rigg-Berechnung. Teil II liefert den verifizierten Rahmen dazu.

---

## 10. Normativer Rahmen

### 10.1 ISO 12215-10 — Rigglasten und Rigg-Anbindung (Leitnorm)

**ISO 12215-10:2020** *„Small craft — Hull construction and scantlings — Part 10: Rig loads
and rig attachment in sailing craft"* ist die **maßgebliche Norm** für die Dimensionierung
der Rigg-Anbindung an Segelfahrzeugen.

**Verifizierter Geltungsbereich (Scope):**
- Legt Verfahren fest zur Bestimmung von **Design-Lasten und Design-Spannungen an Rigg-Elementen**
  sowie der Lasten und Scantlings von **Rigg-Anbindungen, Mastschuh/Pütting und Mastspur/Stützen**
  an Einrumpf- und Mehrrumpf-Segelfahrzeugen.
- Anwendbar auf Fahrzeuge bis **Rumpflänge L_H = 24 m** (bzw. bis 24 m Wasserlinienlänge).
- Primär für **Sportboote inkl. Charterfahrzeuge**. **Nicht** anwendbar auf reine
  Profi-Rennyachten.
- Enthält in Annexen „established practices" (etablierte Praxis) zur Bewertung von
  **Mastspur/Stütze und Püttingen (chainplates)**.
- Betrachtet **ausschließlich Lasten beim Segeln** — andere Lastsituationen (z. B. Transport,
  Kranung) sind nicht abgedeckt.
- Ist **gemeinsam** mit ISO 12215-8 (Ruder) und ISO 12215-9 (Anhänge/Kiel von Segelyachten)
  anzuwenden, um vollständige Scantlings zu erhalten.

Quelle: ISO 12215-10:2020 (iso.org/standard/67294.html); NF EN ISO 12215-10 (afnor). Confidence `documented`.

> **⚠️ ZU PRÜFEN / bewusst NICHT rekonstruiert:** Die konkreten Berechnungs­koeffizienten,
> Design-Faktoren und Formeln von ISO 12215-10 (Rigg-Kraft aus Krängungs-/Aufrichtmoment,
> Anbindungs-Nachweise) stehen **nur im kostenpflichtigen Normtext**. Sie werden hier
> **nicht** aus Sekundärquellen „nachgebaut". Wer nach Norm auslegt, benötigt den Originaltext
> bzw. eine anerkannte Rigg-Berechnungssoftware. Die in Abschnitt 12 genannten Verfahren sind
> **klassische, publizierte Methoden** (nicht ISO) und ausdrücklich als solche gekennzeichnet.

### 10.2 Verwandte Normen im Rigg-/Struktur-Kontext

| Norm | Titel / Gegenstand | Bezug zum Rigg |
|------|--------------------|----------------|
| ISO 12215-10:2020 | Rig loads and rig attachment in sailing craft | **Leitnorm** — Rigglasten, Anbindung, Mastschuh, Pütting |
| ISO 12215-8 | Rudders | Ruderkraft/Ruderschaft — gemeinsam anzuwenden |
| ISO 12215-9 | Appendages of sailing craft | Kiel-/Anhang-Anbindung, Ballast-Befestigung |
| ISO 12215-5:2019 | Design pressures for monohulls, design stresses, scantlings | Rumpf-Scantlings — Basis für Verstärkungszonen um Mastschuh/Pütting |
| ISO 12217 | Stability and buoyancy assessment | Aufrichtmoment (Eingangsgröße für Rigglast) — **Stabilität, nicht Struktur** |

Quelle: ISO 12215-10:2020 Scope-Verweis auf -8/-9; iso.org. Confidence `documented`.

> **Norm-Abgrenzung (häufige Verwechslung):** ISO **12217** ist *Stabilität* und liefert das
> Aufrichtmoment (RM) als **Eingangsgröße** der Rigglast. Die *strukturelle* Rigg-Bemessung
> erfolgt nach ISO **12215-10**. Nicht 12217 für Scantlings zitieren.

---

## 11. Werkstoffe des stehenden Guts — verifizierte Bruchlasten

### 11.1 1×19 Edelstahldraht (Standard-Konstruktion)

**1×19** (ein Bündel aus 19 Einzeldrähten) ist die **meistverwendete** Konstruktion für
stehendes Gut: größter metallischer Querschnitt und dickere Einzeldrähte als 7×7 oder 7×19,
daher **stärkster, aber steifster** der gängigen Aufbauten.
Quelle: Fisheries Supply / S3i Produktbeschreibungen 1×19 316. Confidence `documented`.

**Werkstoff:** AISI **316** / EN **1.4401** (molybdänlegierter austenitischer Edelstahl).
Standard für Segelyacht-Rigg wegen guter Chlorid-Beständigkeit.
Quelle: martinleaning.co.uk (europäischer 1×19-Draht aus 1.4401); Senmit 304-vs-316. Confidence `documented`.

**Mindestbruchlast (MBL) 1×19 AISI 316** — verifizierte Herstellertabelle (Premium Ropes):

| Ø (mm) | MBL (kg) | MBL (kN)¹ | Gewicht (kg/100 m) |
|--------|----------|-----------|--------------------|
| 2.5 | 525 | ~5.15 | 3.10 |
| 3 | 757 | ~7.43 | 4.46 |
| 4 | 1 350 | ~13.2 | 7.93 |
| 5 | 2 100 | ~20.6 | 12.40 |
| 6 | 3 028 | ~29.7 | 17.85 |
| 7 | 3 850 | ~37.8 | 24.30 |
| 8 | 5 040 | ~49.4 | 31.70 |
| 10 | 7 870 | ~77.2 | 49.70 |
| 12 | 10 600 | ~104.0 | 71.30 |
| 14 | 13 400 | ~131.5 | 97.10 |
| 16 | 17 940 | ~176.0 | 127.00 |

¹ kN-Spalte = reine Umrechnung MBL(kg) × 9.81 m/s² / 1000 (`calculated`). MBL(kg) verifiziert.
Quelle: premiumropes.com/1x19 (AISI 316). Confidence `documented` (kg-Werte).

> **Wichtig:** MBL ist die **Mindestbruchlast**, nicht die zulässige Arbeitslast. Zulässige
> Vorspannung/Arbeitslast liegt deutlich darunter (siehe Abschnitt 12.3). Herstellerwerte
> variieren geringfügig (± wenige %) je nach Draht-Lieferant — immer Datenblatt des konkreten
> Herstellers verwenden.

### 11.2 Compact-Strand / Dyform 1×19

**Verdichteter Draht** (compacted strand, Markenname u. a. *Dyform*): Die Einzeldrähte werden
gezogen/verdichtet, dadurch **höhere Bruchlast und geringere Dehnung** bei gleichem Durchmesser.

- Bruchlast **rund 30 % höher** als konventioneller 1×19-Draht gleichen Durchmessers.
- E-Modul (Steifigkeit) **~30 % höher** → weniger Reck, strafferes Vorstag.
- Werkstoff ebenfalls AISI **316 / 1.4401**.
- Beispielwerte (Hersteller, zur Illustration): 6 mm compact ≈ 2 880–3 700 kg MBL;
  10 mm compact ≈ 10 250 kg MBL (herstellerabhängig).

Quelle: jimmygreen.com/508-compacted-strand; s3i.co.uk Dyform. Confidence `documented`.

> Anwendung: Wo geringeres Reck / straffes Vorstag gewünscht ist, ohne auf Rod zu wechseln —
> häufig Performance-Cruiser. Terminals müssen für Compact-Strand freigegeben sein
> (spezielle Keile, siehe 13.2).

### 11.3 Rod-Rigg (Nitronic 50)

**Rod** = massiver, kaltgezogener Rundstab statt Litze. Werkstoff **Nitronic 50**
(hochfester, dehnungsarmer, korrosionsbeständiger Edelstahl, ~200 000 psi ≈ **1 380 MPa**
Zugfestigkeit), speziell für Yacht-Rigg entwickelt. **Deutlich korrosionsbeständiger** als
316-Litze; geringstes Reck; höchste aerodynamische Güte. Nachteil: Punkt-Ermüdung an
Umlenkungen (Kopf/Spreizerenden), nicht feld-reparierbar.

**Navtec R505 Nitronic-50-Rod** — verifizierte Größen/Bruchlasten:

| Rod-Größe | Ø (Zoll) | Ø (mm)² | Äquiv. Draht | Min. Bruchlast (lbs) | Bruchlast (kN)² |
|-----------|----------|---------|--------------|----------------------|-----------------|
| −4 | .172 | ~4.4 | 3/16"+ | 4 700 | ~20.9 |
| −6 | .198 | ~5.0 | 6 mm | 6 300 | ~28.0 |
| −8 | .225 | ~5.7 | 9/32"+ | 8 200 | ~36.5 |
| −10 | .250 | ~6.4 | 5/16" | 10 300 | ~45.8 |
| −12 | .281 | ~7.1 | 5/16"+ | 12 500 | ~55.6 |
| −15 | .296 | ~7.5 | 3/8" | 14 250 | ~63.4 |
| −17 | .330 | ~8.4 | 10 mm+ | 17 500 | ~77.8 |
| −22 | .375 | ~9.5 | 7/16"+ | 22 500 | ~100.1 |
| −30 | .437 | ~11.1 | 9/16"− | 30 000 | ~133.4 |
| −40 | .500 | ~12.7 | 5/8"− | 38 000 | ~169.0 |
| −48 | .562 | ~14.3 | 3/4" | 48 000 | ~213.5 |
| −60 | .660 | ~16.8 | 7/8"− | 60 000 | ~266.9 |
| −76 | .705 | ~17.9 | 1"− | 76 000 | ~338.0 |

² Ø(mm) = Zoll × 25.4; kN = lbs × 0.0044482 (`calculated`, reine Umrechnung). lbs-/Zoll-Werte verifiziert.
Merkregel: Rod-Nummer ≈ Bruchlast in Hundert lbs (−22 ≈ 22 500 lbs).
Quelle: rigrite.com Rod Rigging (Navtec R505); Hayn R505; Wichard/Navtec-Katalog. Confidence `documented` (lbs/Zoll).

### 11.4 Duplex 1.4462 (2205) als Alternativwerkstoff

Für besonders krevikorrosions-kritische Anwendungen (Litze bildet zwangsläufig Spalten) wird
**Duplex 2205 / EN 1.4462** eingesetzt:
- Streckgrenze **~450 MPa** — nahezu doppelt so hoch wie 304/316.
- Deutlich höhere Beständigkeit gegen **Loch-, Spalt- und Chlorid-Spannungsrisskorrosion**.
- 316 gilt „mit den für Drahtseil typischen Spalten an seiner Grenze"; daher wird 2205 dort
  bevorzugt.
- **Tea-Staining** (bräunlicher Oberflächen­film): 316 (Mo-legiert) widersteht **besser**;
  Tea-Staining ist jedoch **kosmetisch**, keine Struktur-Korrosion — Passivschicht bleibt
  intakt, entfernbar mit verdünnter Oxalsäure.

Quelle: MFG Shop 1.4462; ASSDA/worldstainless Duplex; Suncor Marine-Korrosion. Confidence `documented`.

---

## 12. Dimensionierungs-Methodik (publizierte Verfahren, NICHT ISO)

> **Abgrenzung:** Die folgenden Verfahren sind **klassische Fachliteratur-Methoden**
> (Nordic Boat Standard, Skene, Phillips-Birt, Gerr). Sie sind **nicht** ISO 12215-10 und
> liefern **Näherungen** für Vorauslegung/Plausibilisierung. Die normkonforme Bemessung
> erfolgt nach ISO 12215-10 (Koeffizienten nur im Normtext). Alle Zahlen unten sind an der
> zitierten Fachquelle belegt.

### 12.1 Aufrichtmoment-Methode (Nordic Boat Standard, NBS)

Grundgedanke: Die **quer wirkenden Wantenlasten** werden aus dem **Aufrichtmoment (RM)** bei
einem Design-Krängungswinkel abgeleitet.

- Design-Krängung **30°** (entspricht kräftigem Wind bei noch voll ziehenden Segeln).
- Korrektur für Crew-Gewichtsverteilung; zwei Lastfälle: **volles Arbeitsvorsegel** ODER
  **gerefftes Groß**.
- Lastaufteilung auf Masttopp, Hounds (Salingshöhe) und Lümmelbeschlag.
- **Wantenlasten × 2.5 bis 3** (Sicherheits-/Dynamikfaktor).
- **Mastdruck × 1.5** zur Abdeckung dynamischer Faktoren.

Quelle: classic-marine.co.uk „Rigging Loads" (Nordic Boat Standard). Confidence `documented`.

### 12.2 Weitere publizierte Näherungen

| Verfahren | Kernaussage (verifiziert) | Quelle |
|-----------|---------------------------|--------|
| **Skene „Short Method"** | Max. Mastdruck = **2.78 × Moment ÷ halbe Breite**; +50 % für decksgestepte Masten; SF 1.5–3 je Drahttyp | classic-marine.co.uk |
| **Skene „Long Method"** | Winddruck-Annahme **1 lb/ft² Segelfläche**, gleichmäßig verteilt; SF **4**; Endfaktor 2.7–4 | classic-marine.co.uk |
| **Phillips-Birt** (empirisch) | Mast-Scantling-Kriterium ∝ B + M + H + 2cos⁴A (B=Ballastanteil, M∝Metazentrum, H=Vorsegelhöhe, A=Wantenwinkel) | classic-marine.co.uk |
| **Gerr / „The Nature of Boats"** (Verdrängungs-Regel) | Summe der MBL aller Wanten **einer** Seite ≥ **1.0 ×** Verdrängung (Racer), **1.1 ×** (Küsten-Cruiser), **1.2 ×** (Blauwasser-Cruiser) | Gerr, zit. n. Suchergebnis |

Quelle: classic-marine.co.uk; Dave Gerr *The Nature of Boats*. Confidence `documented`.

> **⚠️ ZU PRÜFEN:** Formel-Terme (z. B. Phillips-Birt `2cos⁴A`, Skene `2.78`) sind hier als
> **Zitat** der Sekundärquelle wiedergegeben, nicht selbst hergeleitet. Vor produktiver
> Anwendung am Original (Skene's *Elements of Yacht Design*, Phillips-Birt) verifizieren.

### 12.3 Sicherheitsfaktoren und zulässige Spannung (Faustregeln)

- **Arbeitsvorspannung Wanten:** nicht über **25 % der Bruchlast** (MBL) — Faustregel
  unabhängig vom Durchmesser.
- **Vorstag-Vorspannung:** typisch **~15 % der Bruchlast**.
- Allgemeine Rigging-Sicherheitsfaktoren (Hebe-/Lastindustrie): meist **4:1**, Spanne 4:1–7:1
  — im Yacht-Rigg wird über die Bruchlast-Reserve gearbeitet (Wanten-MBL ≫ Arbeitslast).

Quelle: YBW Forum / eltlift.com WLL vs BL; classic-marine.co.uk. Confidence `documented`.

> Der in Teil I genannte Safety-Factor **2.5** in `calculate_wire_area_required()` ist ein
> **Legacy-Wert** und deckt sich zufällig mit dem NBS-Lastmultiplikator 2.5–3, ist aber
> **nicht** dasselbe (Lastmultiplikator vs. Materialsicherheit). Nicht vermischen.

---

## 13. Terminals und Anschlüsse

### 13.1 Gepresste Terminals (Swage)

- Hydraulische Presshülse bildet „Kaltverschweißung" um den Draht; **niedriges Profil**.
- **Nicht feld-reparierbar**, nicht zerstörungsfrei innen inspizierbar.
- Versagen kann **plötzlich** eintreten (innere Spaltkorrosion, Haarrisse an der Hülse).
- Wirkungsgrad: bricht **knapp oberhalb** der Nenn-Bruchlast des Drahtes (Test).

Quelle: Practical Sailor „Screw-on Rigging Terminals"; SailNet. Confidence `documented`.

### 13.2 Mechanische (schraubbare) Terminals — Sta-Lok / Norseman / Suncor

- **Zerlegbar, wiederverwendbar, feld-montierbar, innen inspizierbar** — ideal für
  Blauwasser.
- **Wirkungsgrad (Practical-Sailor-Test):** Swage, **Sta-Lok** und **Suncor** brachen jeweils
  **etwas oberhalb** der Nenn-Bruchlast des Drahtes; der getestete **Norseman** versagte bei
  **69 %** der Nenn-Bruchlast.
- Vorteil beim 10-Jahres-Wechsel: Fittings wiederverwendbar → geringere Ersatzkosten.
- Für **Compact-Strand/Dyform** spezielle Keile (wedges) erforderlich.

Quelle: Practical Sailor Terminal-Test; stalok.com Dyform-Keile. Confidence `documented`.

> **Auslegungsregel:** Terminal-Wirkungsgrad in die Kette einrechnen. Wenn ein Terminal nur
> ~69 % der Draht-MBL hält, ist **das Terminal** das schwächste Glied — nicht der Draht.
> Nur freigegebene Draht/Terminal-Kombinationen verwenden.

---

## 14. Fehlerbild-Atlas (kollisionsfrei, Schema FB-31-04-NNN)

> Ergänzt die Legacy-Fehlermuster **[F6.1]–[F6.12]** aus Teil I (dortige IDs bleiben gültig).
> Neue IDs im projektweiten Schema `FB-<Kat>-<Unterkat>-<lfd>`, hier **FB-31-04-001 ff.**,
> kollisionsfrei zu den `[F6.x]`.

### FB-31-04-001 — Terminal als schwächstes Glied (Norseman-Effekt)
- **Fehlerbild:** Draht korrekt dimensioniert, aber Terminal-Wirkungsgrad < 100 % → Bruch am
  Terminal unter Nenn-MBL.
- **Ursache:** falsch montiertes/nicht freigegebenes Schraubterminal; im Test versagte ein
  Norseman-Terminal bei **69 %** der Draht-MBL (Practical Sailor).
- **Diagnose:** Terminal-Datenblatt-Wirkungsgrad prüfen; Kette „Draht → Terminal → Pütting"
  auf schwächstes Glied durchrechnen.
- **Abhilfe:** Nur freigegebene Draht/Terminal-Paarung; Montage nach Herstellervorgabe;
  bei Compact-Strand passende Keile.
- Quelle: Practical Sailor Terminal-Test. Confidence `documented`.

### FB-31-04-002 — Swage-Terminal: verdeckte Spaltkorrosion
- **Fehlerbild:** Von außen intakte Presshülse, innen Spaltkorrosion/Haarrisse → plötzlicher
  Bruch ohne Vorwarnung.
- **Ursache:** Chlorid + Sauerstoffarmut im Spalt Hülse/Draht; 316 „an der Grenze" bei
  Drahtseil-typischen Spalten.
- **Diagnose:** Risslupe an Hülsenmündung, Verfärbung/rostige Fahnen; ggf. Wirbelstrom-/
  Rissprüfung durch Rigger.
- **Abhilfe:** Bei Rissindikation Terminal/Draht ersetzen; für kritische Fahrt schraubbare,
  inspizierbare Terminals bevorzugen; Werkstoff-Upgrade auf Duplex 1.4462 erwägen.
- Quelle: Practical Sailor; ASSDA/worldstainless Duplex-Spaltkorrosion. Confidence `documented`.

### FB-31-04-003 — Überspannung > 25 % MBL (Reck, Dauerbruch)
- **Fehlerbild:** Draht dauerhaft über 25 % MBL gespannt → bleibendes Reck, beschleunigte
  Ermüdung.
- **Ursache:** Über-Tuning (zu straffes Rigg), fehlende Spannungsmessung.
- **Diagnose:** Wanten-Spannungsmesser (Loos-Gauge o. ä.); Ziel: Vorspannung ≤ 25 % MBL,
  Vorstag ~15 % MBL.
- **Abhilfe:** Nach Herstellervorgabe/Rigg-Tuning-Tabelle nachspannen; nicht über 25 % MBL.
- Quelle: YBW Forum Standing-Rigging-Tension; classic-marine.co.uk. Confidence `documented`.

### FB-31-04-004 — Falscher Werkstoff bei Spaltkorrosions-Risiko
- **Fehlerbild:** 316-Litze in Dauer-Salzwasser mit stehenden Spalten → Loch-/Spaltkorrosion,
  frühzeitiges Versagen.
- **Ursache:** 316 an seiner Beständigkeitsgrenze in Spaltgeometrie.
- **Diagnose:** Werkstoffnachweis (1.4401 vs 1.4462); Betriebsumgebung (tropisch/Dauerliege).
- **Abhilfe:** Für kritische Fälle Duplex **2205 / 1.4462** (höhere Loch-/Spalt-/CSCC-
  Beständigkeit, ~450 MPa Streckgrenze).
- Quelle: MFG Shop 1.4462; ASSDA. Confidence `documented`.

### FB-31-04-005 — Rod-Punktermüdung an Umlenkung
- **Fehlerbild:** Rod-Rigg bricht an Masttopp-Terminal oder Spreizerende (Biegewechsel-
  Ermüdung), nicht auf freier Länge.
- **Ursache:** Zyklische Biegung an Umlenkpunkten; Rod ist dehnungsarm, aber punktermüdungs-
  empfindlich; nicht feld-reparierbar.
- **Diagnose:** Rissprüfung an Rod-Köpfen/Umlenkungen durch Rigger; Rod-Rigg nach
  Herstellerintervall zerlegen und prüfen.
- **Abhilfe:** Terminals/Kopfstücke tauschen; Rod bei Rissindikation ersetzen; Umlenk-
  radien beachten.
- Quelle: rigrite.com / Annapolis Rigging Rod-Rigging (Nitronic 50, Punktermüdung). Confidence `documented`.

### FB-31-04-006 — Überalterung / abgelaufenes Wechselintervall
- **Fehlerbild:** Optisch „gutes" Rigg jenseits Lebensdauer → statistisch stark erhöhtes
  Bruchrisiko; ggf. Deckungsverlust der Versicherung.
- **Ursache:** Nichteinhaltung des ~10-Jahres-Wechselintervalls.
- **Diagnose:** Rigg-Alter/Seemeilen dokumentieren; Terminals elektronisch prüfen lassen.
- **Abhilfe:** Stehendes Gut ~alle **10 Jahre** (bzw. **50 000–80 000 sm** offshore) ersetzen,
  unabhängig vom Aussehen (siehe 15.1).
- Quelle: SailMagazine; YBW Rigging-Renewal. Confidence `documented`.

---

## 15. Wartung, Prüf- und Wechselfristen

### 15.1 Wechselintervall stehendes Gut (verifiziert)

- **Ersatz ~alle 10 Jahre**, unabhängig vom äußeren Zustand; offshore-Richtwert
  **50 000–80 000 sm**.
- **Versicherungen** verlangen häufig (nicht immer) den 10-Jahres-Wechsel; teils längere
  Frist bei **professioneller Inspektion**, insbesondere **elektronischer Terminal-Prüfung**.
- Mechanische (schraubbare) Terminals erlauben Wiederverwendung der Fittings beim Draht-
  Wechsel → geringere Kosten.

Quelle: SailMagazine „Inspecting… Standing Rigging"; YBW Rigging-Renewal; Practical Sailor. Confidence `documented`.

### 15.2 Inspektions-Checkliste (ergänzend zu 7.1)

- [ ] Terminal-Mündungen mit Risslupe prüfen (Haarrisse, rostige Fahnen) — FB-31-04-002
- [ ] Wantenspannung mit Messgerät prüfen: Vorspannung ≤ 25 % MBL, Vorstag ~15 % MBL — FB-31-04-003
- [ ] Rod-Köpfe/Umlenkungen auf Punktermüdung prüfen (bei Rod-Rigg) — FB-31-04-005
- [ ] Rigg-Alter/Seemeilen gegen 10-Jahres-/50 000–80 000-sm-Grenze abgleichen — FB-31-04-006
- [ ] Werkstoff/Umgebung: bei Dauer-Salzwasser + Spalten Werkstoff-Upgrade prüfen — FB-31-04-004
- [ ] Draht/Terminal-Freigabe (Compact-Strand → passende Keile) prüfen — FB-31-04-001

---

## 16. FAQ und Glossar

### 16.1 FAQ

**Welche Norm gilt für die Rigg-Dimensionierung?**
ISO **12215-10:2020** (Rigglasten und Rigg-Anbindung), gemeinsam mit ISO 12215-8 (Ruder) und
-9 (Anhänge). Für Fahrzeuge bis 24 m, nicht für reine Profi-Rennyachten.
Quelle: ISO 12215-10:2020 Scope. Confidence `documented`.

**Warum steht hier keine fertige ISO-Formel für die Wantenlast?**
Weil die Koeffizienten von ISO 12215-10 nur im **kostenpflichtigen Normtext** stehen. Wir
rekonstruieren sie **nicht** (Kernregel: nichts Unverifiziertes als Fakt). Für Näherungen
siehe die publizierten Verfahren in Abschnitt 12 (klar als Nicht-ISO gekennzeichnet).

**Wie straff darf ich Wanten spannen?**
Faustregel: **≤ 25 % der Bruchlast**; Vorstag **~15 %**. Über 25 % → Reck/Ermüdung (FB-31-04-003).
Quelle: YBW; classic-marine.co.uk. Confidence `documented`.

**Draht, Compact-Strand oder Rod?**
Draht 1×19 (316): Standard, gut einstellbar. Compact/Dyform: ~30 % höhere Bruchlast & Steifigkeit
bei gleichem Ø. Rod (Nitronic 50): geringstes Reck, höchste Korrosionsbeständigkeit, aber
punktermüdungs-empfindlich und nicht feld-reparierbar.
Quelle: jimmygreen.com; rigrite.com. Confidence `documented`.

**Wann muss stehendes Gut getauscht werden?**
~Alle **10 Jahre** bzw. **50 000–80 000 sm**, unabhängig vom Aussehen.
Quelle: SailMagazine; YBW. Confidence `documented`.

### 16.2 Glossar

| Begriff | Bedeutung |
|---------|-----------|
| **Stehendes Gut** (standing rigging) | Feste Verstagung: Wanten, Vor-/Achterstag |
| **Laufendes Gut** (running rigging) | Bewegliche Leinen: Fallen, Schoten |
| **1×19** | Draht-Konstruktion: 1 Bündel aus 19 Einzeldrähten; stärkster/steifster Standard-Aufbau |
| **Compact-Strand / Dyform** | Verdichteter Draht; ~30 % höhere Bruchlast & Steifigkeit |
| **Rod** | Massiver kaltgezogener Rundstab (Nitronic 50); dehnungsarm |
| **MBL** | Minimum Breaking Load / Mindestbruchlast |
| **WLL** | Working Load Limit / zulässige Arbeitslast (= MBL ÷ Sicherheitsfaktor) |
| **Swage** | Gepresstes Terminal (Presshülse) |
| **Sta-Lok / Norseman** | Schraubbare, zerlegbare, wiederverwendbare Terminals |
| **Pütting** (chainplate) | Rumpfseitiger Anschlagpunkt der Wanten |
| **Hounds** | Salings-/Wantenanschlaghöhe am Mast |
| **RM** | Righting Moment / Aufrichtmoment (Eingangsgröße der Rigglast, aus ISO 12217) |
| **Nitronic 50** | Hochfester Rigg-Edelstahl (~1 380 MPa), korrosionsbeständiger als 316 |
| **Duplex 2205 / 1.4462** | Duplex-Edelstahl, ~450 MPa Streckgrenze, hohe Spaltkorrosions-Beständigkeit |

---

## Quellen (Teil II)

- ISO 12215-10:2020 — iso.org/standard/67294.html ; NF EN ISO 12215-10 (afnor.org) — Scope, Anwendbarkeit, Verweis auf -8/-9
- ISO 12215-5:2019, -8, -9 — iso.org (Struktur-/Ruder-/Anhang-Bezug)
- premiumropes.com/1x19 — 1×19 AISI 316 Bruchlast-Tabelle (kg)
- jimmygreen.com/508-compacted-strand ; s3i.co.uk — Compact-Strand/Dyform (+30 %)
- rigrite.com Rod Rigging ; hayn.com R505 ; Wichard/Navtec-Katalog — Nitronic-50-Rod-Tabelle
- MFG Shop 1.4462 ; ASSDA/worldstainless ; Suncor Stainless — Duplex 2205, Korrosion, Tea-Staining
- classic-marine.co.uk „Rigging Loads" — NBS, Skene, Phillips-Birt, Gerr (publizierte Verfahren)
- Practical Sailor „Screw-on Rigging Terminals" — Terminal-Wirkungsgrade (Swage/Sta-Lok/Suncor/Norseman)
- SailMagazine ; YBW Forum — Wechselintervall 10 Jahre / 50 000–80 000 sm; Versicherungspraxis

---

**Datei abgeschlossen.**  
Kat 31.04 Rigg-Dimensionierung — Version 2.0 (Teil II Werft-Tiefe ergänzt) — 2026-07  
Teil I (Version 1.0, 2025-01) unverändert erhalten.
