# 31_10 — Deck-Layout

**Kategorie:** 31_Design_Konstruktion  
**Unterkategorie:** Deck_Layout  
**Version:** 2.1  
**Stand:** 2026-07-13  
**Relevanz:** Sicherheit, Ergonomie, funktionale Effizienz an Deck

> **Hinweis zur Version 2.1 (Werft-Tiefe-Erweiterung):** Die Abschnitte 1–10 sind Bestand (v2.0) und unverändert erhalten. **Neu angefügt** sind die web-verifizierten Abschnitte **11 (Normativer Rahmen)**, **12 (Sichtlinien ISO 11591)**, **13 (Fanggeländer-Präzisierung ISO 15085:2024)**, **14 (Beschlag-/Winsch-/Klampen-Platzierung, ISO 15084)**, **15 (Cockpit-Entwässerung ISO 11812 — Korrektur)** sowie der **Fehlerbild-Atlas (FB-31-10-xxx)**. Wo Bestand v2.0 nachweislich von verifizierten Normwerten abweicht, steht in Abschnitt 11–15 ein ausdrücklicher **Korrekturhinweis** — der Originaltext bleibt zur Nachvollziehbarkeit stehen, ist aber gegenüber den verifizierten Werten nachrangig.

---

## Übersicht

Das Deck-Layout bestimmt **Sicherheit (Fanggeländer, Entwässerung)**, **Arbeitseffizienz (Segelhandling)** und **Komfort (Cockpit-Design)** fundamental. AYDI analysiert Cockpit-Dimensionierung, Arbeitsdecks, Foredeck-Sicherheit und Drainage-Systeme.

**Fehleranalyse-Schwerpunkte:**
1. Cockpit zu eng (Sicherheit und Bedienung beeinträchtigt)
2. Cockpit-Sole zu hoch (Auflaufen möglich, Selbstlenzung nicht optimal)
3. Fanggeländer zu niedrig oder unterbrochen (Überboard-Risiko)
4. Seitliche Decks zu schmal (Bewegungsfreiheit, crew-safety)
5. Foredeck-Belüftung schlecht (Segelbeutel-Nässe, Fäulnis)
6. Abflusssystem verstopft / Dimensionierung zu klein
7. Oberflächen-Rauhheit ungünstig (rutschig oder zu rau/zerstörerisch)
8. Hauptsegel-Winde ergonomisch ungünstig positioniert
9. Focksegel-Systeme überlastet (Führungs-Blockaden)
10. Dachhöhe zum Cockpit mangelhaft (Seewasser-Eindringung)
11. Achterdecks-Überladung (Trimm-Verschlimmerung)
12. Zu-Wasser-Rettungs-Ausrüstung schlecht erreichbar

---

## 1. Cockpit-Dimensionierung und Form

### 1.1 Cockpit-Volumen und Selbstlenzung

**ISO 11812 Standard (Cockpit-Drainage):**

```
Cockpit_Volume [m³] = Length × Width × Average_Depth

Drainge_Requirement:
  Cockpits müssen in ≤ 5 Sekunden 50% Wasser selbstlenzen
  Drain_Flow [m³/s] = 0.5 × Volume / 5 = 0.1 × Volume

Drain_Pipe_Diameter [mm]:
  Flow_Velocity = 1.5–2.0 m/s (Standard)
  A = Q / v → Pipe_Diameter = sqrt(4 × A / π)

Beispiel: 12m Segelboot, Cockpit 4m × 2m × 0,6m
  Volume = 4 × 2 × 0,6 = 4,8 m³
  Drain_Flow = 0.1 × 4,8 = 0,48 m³/s = 480 L/min
  Pipe_Diameter = sqrt(4 × (0,48 / 1,75) / 3,14159) = 0,588 m ≈ 588 mm (theoretisch — unrealistisch, siehe Abschnitt 3.1)
  → Praktisch: 2 × 40 mm Rohre oder 1 × 60 mm Rohr
```

**Cockpit-Tiefe Standard nach Boot-Klasse:**

| Boot-Klasse | Cockpit-Tiefe [mm] | Begründung |
|-------------|-------------------|-----------|
| Racing Dinghy | 150–250 | Minimal, schnell selbstlenzend, aber nass |
| Cruiser-Racer 8–12m | 300–500 | Balanced: Selbstlensung + Sitzkomfort |
| Comfortable Cruiser 12–20m | 500–700 | Tiefer, höheres Volumen, braucht große Drainage |
| Mega-Yacht 25m+ | 600–1000 | Sehr tief, mehrere separate Cockpits |

**Praktische Tiefe-Berechnung:**

```
Tiefe sollte so sein, dass Wasser über Reling kommt, 
aber nicht über Cockpit-Rand spritzt.

Typisch: Cockpit_Sole_Height = Wasserlinie + 400–600 mm
  → Wenn Boot Wellen schlägt (1–2m Höhe), bleibt meist trocken
  → Bei großem Seegang (3–5m) → Nassheit normal
```

### 1.2 Cockpit-Form und Funktionale Zonen

**Standard-Layout (Mittelmotorig / Mittelsegel):**

```
       Foredeck
     ___________
    |           |
    |   FORWARD COCKPIT (optional)
    |___________|
    |\         /|
    | \       / |
    |  \     /  | SIDE AREAS
    |   \   /   |
    |_______| HELM STATION
    |\ ~~~~~\|   
    | \STERN COCKPIT (Helm + 2-4 Crew)
    |_______|___
      Engine Hatch
```

**Zone 1: Helm Station (Steuern)**

```
Dimensionierung:
  Breite: 600–800 mm (für 1 Person komfortabel)
  Tiefe: 400–600 mm (Fußraum + Sitzhöhe 350–450 mm)
  Sichtlinie: nach vorn (mindestens 45° nach Backbord/Steuerbord)
  Winde-Position: 300–400 mm zu Backbord/Steuerbord (angewinkelte Arme)
  
Ergonomie:
  Sitzabstand Lenkrad: 500–600 mm (entspannt, aber Alert)
  Lenkrad-Ø: 500–700 mm (je nach Boot-Größe)
  Griff-Höhe: 100–150 mm über Sitzkante
```

**Zone 2: Crew-Platz (Sicherheit + Funktion)**

```
Mindestens 2–3 zusätzliche Plätze im hinteren Cockpit:
  Jeder Platz: 400–500 mm Breite, 300–400 mm Tiefe
  Höhenausgleich: Sitze leicht erhöht gegen Reling
  Haltegriffe: 2–3 Pro Platz (Stab + Reling)
  
Sitzerhöhung (Hiking-Position bei Segelbooten):
  Über Reling hinaus möglich (für Ballast bei Heel)
  Sicherheits-Gurt + Pad erforderlich
  Höhe: bis 300 mm über normales Reling
```

**Zone 3: Süd-Cockpit (größere Boote)**

```
Viele Motoryachten haben separate Cockpits:
  Vorderer Cockpit (Ankermanöver): kleine Fläche, Anker-Handgriff
  Mittlerer Cockpit (Fahren): Helm-Station
  Achteren Cockpit (Sonnen/Entspannung): größer, offener
```

### 1.3 Seitliche Decks und Gangway

**Seitendecks-Breite (ISO 15085):**

```
Minimum: 400 mm (eng, aber passiebar)
Komfort: 500–700 mm (für Bewegung freihändig)
Großer Yacht: 1000+ mm (promenade-artig)

Beziehung zu Reling-Höhe:
  Wenn Seitendeck 400 mm: Reling minimum 900–1000 mm hoch
  Wenn Seitendeck 600 mm: Reling 800 mm ausreichend
  → Verhältnis: je schmaler Deck, desto höher Reling
```

**Oberflächen-Belag (Rutschfestigkeit):**

| Material | Rutsch-Koeffizient | Haltbarkeit | Kosten (EUR/m²) |
|----------|-----------------|-----------|----------|
| Teak (ungeplant) | 0,6–0,8 | 15–20 Jahre | 150–250 |
| Gitterrost (FRP) | 0,8–0,9 | 20+ Jahre | 80–150 |
| Kunststoff-Fliese | 0,5–0,7 | 10–15 Jahre | 50–100 |
| Farbige Epoxy | 0,5–0,6 | 5–8 Jahre | 30–60 |
| Gelcoat (glatt) | 0,3–0,4 | 3–5 Jahre | 10–20 |

**Best Practice:** Teak im Cockpit, Gitterrost an Seiten (Wasser-Drainage).

### 1.4 Cockpit-Dach (Hard Top / Bimini)

**Funktionen:**
1. UV-Schutz (Crew + Material)
2. Regenschutz
3. Seewasser-Ablenkung (bei Dünung)

**Dimensionierung:**

```
Dach-Ausladung:
  Vorne (Schutz nach vorn): 500–800 mm nach Bug
  Hinten (Helm-Bereich): 1000–1500 mm
  Seiten: 300–500 mm über Reling

Durchgangs-Höhe:
  Mindestens 2000 mm (6'6") für stehende Crew
  Großer Yacht: 2200–2400 mm
  
Gewicht des Daches:
  Aluminiumrahmen + Canvas: 20–40 kg (für 12m Boot)
  → Einflusss auf CG negligible
```

**Wasser-Ableitung:**

```
Dach-Neigung: 3–5° (Selbstentleerung)
Fallrohr: 50–75 mm Ø, in Lenz-Brunnen direkt
Ablauf-Öffnungen: mehrere kleine (nicht ein großes → Vortex-Risiko)
```

---

## 2. Foredeck-Layout und Segelbeutel-Management

### 2.1 Foredeck-Breite und Arbeitsplatz

**Arbeitsfläche (Fokus Segelbeutel-Handling):**

```
Breite Foredeck (ideal): 2,5–3,5m für 12m Boot
  → Fokus-Segel auslegen, neu falten
  
Breite Foredeck (eng): 1,5–2,0m
  → Nur Handhaben möglich, Neufaltung schwierig
  
Länge Foredeck (nützlich): mindestens 4m
  → Genug Platz, zwei Segel gleichzeitig zu handhaben
```

### 2.2 Fock- und Fokus-Segel-Systeme

**Führungsschienen (Traveller Rail):**

```
Position: 300–500 mm inboard von Reling
Material: Aluminiums-Profil oder Kunststoff-Schiene
Läufer: Kugelgelagert, leichte Bewegung

Breite der Schiene:
  Für 12m Boot: 3–4m (Fokus und Fock)
  Für 18m Boot: 4–6m
  
Anzahl der Schienen:
  Minimum: 2 (Fokus + Fock)
  Mit Staysegel: 3 Schienen (Komplexität erhöht)
  
Block-Positionierung:
  Sollte ergonomisch erreichbar sein (nicht >2m über Deck)
  Deckblock unter Spannung: 45–60° ideal
```

**Windenanordnung:**

```
Fokus-Winde (Vordeck):
  Position: zentral auf Foredeck, leicht backbord
  Höhe: 600–800 mm über Deck (Handgriff)
  Übersetzung: 40:1 bis 60:1 (abhängig Segel-Größe)
  
Fock-Winde (parallel oder separate):
  Wenn elektrisch: separate, oft Fernbedienung vom Cockpit
  Wenn manuell: neben Fokus-Winde, aber Backbord
  
Notfall-Sicherung:
  Handgriff oder Notfall-Kurbel für elektr. Fehler
```

### 2.3 Befestigungs-Punkte und Sicherung

**Rollen und Blöcke (Rigging-Hardware):**

```
Material: Edelstahl 316L oder Aluminium-anodisiert
Tragfähigkeit: mindestens 2× die maximale Segel-Last
  Typisch: 30–50 kN pro Block

Wartung:
  Jährlich: Verschleiß prüfen (Rollen drehen frei?)
  Alle 3 Jahre: Lager austauschen (wenn nötig)
  Nach Beschädigungen: sofort kontrollieren
```

**Sicherungs-Ogen (Pad Eyes):**

```
Standard für Segelboot: 8–10 Pad Eyes auf Foredeck
  Positionen: Staysegel-Punkt, Fokus-Halse, Achterstag, etc.
  
Belastung: 10–20 kN pro Auge (abhängig Rigging)
Befestigung: 8–10 Bolzen pro Auge (verteilt auf 100×100 mm Fläche)
Material: Edelstahl 316L oder Federstahl

Kontrolle:
  Jährlich auf Lockerung prüfen (mit Magnet-Schlüssel)
  Nach Grounding oder Kenterung: sofort prüfen
```

### 2.4 Sicherheits-Linie und Handgriffe

**Sicherheits-Leinen (Lifelines/Jack Lines):**

```
Standard nach ISAF/IMS:
  Zwei Leitungen vom Cockpit zum Foredeck (Backbord + Steuerbord)
  Höhe: 600–800 mm über Deck
  Durchmesser Tau: 8–10 mm (Ø brauchbar für Sicherheits-Harness)
  Spannung: 2000–3000 N (fest, aber nicht zu straff)
  
Befestigung:
  Vorne: Staysegel-Punkt oder Ankerklampe
  Hinten: direkt am Cockpit-Reling (oder Poop-Deck)
  Mittenpunkte: 1–2 Umlenkrollen zur Stabilisierung
  
Inspektion:
  Visuell: auf Verschleiß, Fäden-Ausfransung
  Zugtest: 1000 N Zugkraft, darf nicht mehr als 5 cm durchhängen
  Austausch: alle 5–7 Jahre (UV-Degradation)
```

**Handgriffe (Deck-Handles):**

```
Positionen: Foredeck-Seiten + Mitte, Cockpit-Reling, Stufen
Material: Edelstahl oder Kunststoff-mit-Kern
Höhe: 100–150 mm über Oberfläche (komfortabel greifbar)
Abstände: max. 1m (schnelle Bewegung erfordert häufige Griffe)

Tragfähigkeit: mindestens 150 kg pro Griff (Sicherheitsfaktor 3)
```

---

## 3. Entwässerungs-Systeme

### 3.1 Cockpit-Drainage (Selbstlensung)

**Rohr-Layout:**

```
Standard für 12m Segelboot:

Cockpit-Sohle → Sammlung an tiefster Stelle (typ. hinten)
  ↓
Hahnblock (mit Schieberventil zum Abperren)
  ↓
Erste Etappe (40 mm Rohr, bis Wassergrenze)
  ↓
Seewasser-Einlaufystem (Hahnstock mit Schieberventil)
  ↓
Bilgenpumpe (Standard) oder direkt über Schiffsseite
  ↓
Durchführung Hull (mit Antrieb-Sicherung: Kugelsperrventil)

Alternative: Direkter Ablauf (wenn Cockpit-Sohle über Wasserlinie):
  Cockpit → Rohr → Hahnstock-Ventil → Durchführung
```

**Rohrdimensionierung (detailliert):**

```
Für Cockpit 4 m × 2 m × 0,6 m:
  Volume = 4,8 m³
  Drain Time Goal: 5 Sekunden (50% = 2,4 m³)
  Flow Rate = 2,4 m³ / 5s = 0,48 m³/s = 480 L/min

  Rohr-Ø Berechnung:
  Flow = v × A
  A = Flow / v = 0,48 m³/s / 1,75 m/s = 0,274 m²
  d = sqrt(4 × A / π) = sqrt(4 × 0,274 / 3,14159) = 0,588 m = 588 mm (!!)
  
  Das ist unrealistisch! Standard ist 2 Rohre:
  2 × A = 0,274 m² → A pro Rohr = 0,137 m²
  d = sqrt(4 × 0,137 / 3,14159) = 0,417 m = 417 mm (immer noch groß!)
  
  Praktisch: 2 × 50–60 mm Rohre zusammen genügen
  (mit leichten Turbulenzen/Verlängerung der Drain-Zeit)
```

**Hahnstock-Ventile (Seacock):**

```
Standard für Segelboot: Ball-Ventile, Edelstahl
Größe: DN40–DN50 (Rohr-Größe angepasst)

Position: unterhalb Wasserlinie (10–20 cm über Kiel)
Material: Bronze (Seacock) oder Kunststoff (nicht empfohlen Salzwasser)

Wartung:
  Jährlich: Ventil öffnen/schließen (Funktionsprüfung, Verhinderung Verkalkung)
  Alle 5 Jahre: Ventil-Zug überprüfen (darf nicht hart sein)
  Bei Festsitzen: Penetrol-Öl + sachte wenden (nicht erzwingen!)
```

### 3.2 Deck-Drainage (Regen + Spritzwasser)

**Außendeck-Ableitung:**

```
Principium: Wasser darf nicht auf Deck stagnieren
  Minest-Neigung: 1–2% (entspricht 10–20 mm pro Meter)
  
Cockpit-Sohle sollte leicht nach vorn/hinten geneigt sein:
  Typisch 50–100 mm Höhenunterschied über 4m Länge
  
Seitendeck-Drainage:
  Kleine Rinnen zwischen Reling + Hauptdeck
  Offene Öffnungen oder Gittersystem
  Loch-Größe: max. 5 mm (verhindert Tripping, lässt Wasser durch)
  
Foredeck-Drainage:
  Mittellinie mit leichtem Gefälle nach Cockpit
  Achter-Drainage über Cockpit-Sohle
```

**Regen-Entwässerung (Dauerhafte Systeme):**

```
Für Boote mit Dach/Canvas: Fallrohre erforderlich

Fallrohr-Größe: 50–75 mm Ø (abhängig Dach-Fläche)
Anzahl der Fallrohre: mindestens 2 (Backup, wenn einer blockiert)

Ablauf-Ziel: 
  Option A: Direkt in Lenz-Brunnen oder Cockpit-Drainage
  Option B: Über Seite über spezielles Rohr
  Option C: In separates Sammelbecken (für Trink-Wassersystem)
```

### 3.3 Blockade-Vermeidung und Wartung

**Häufige Verstopfungs-Ursachen:**

```
1. Laub / Algen-Wuchs: Filter-Sieb (5 mm) vor Hahnblock
2. Salz-Kristallisierung: regelmäßige Spülung mit Süßwasser
3. Mu schelwuchs: in Rohren (besonders in Warmen Meeren)
4. Sand / Schlamm: sedimentiert in gebogenen Rohren

Prävention:
  Jährlich: komplette Drainage-Spülung mit Süßwasser
  Vor Winterlagerung: Drainage-Ventile öffnen, trocknen lassen
  Bei längerer Inaktivität: Ventile abwechselnd öffnen (Belüftung)
```

**Inspektions-Checkliste:**

```
Vor Saison-Start:
  ☐ Hahnblock öffnen/schließen prüfen (Ventil darf nicht fest sein)
  ☐ Rohre auf Risse / Verformung prüfen
  ☐ Filter-Sieb sichtprüfen (sauber?)
  ☐ Testlauf: kleine Menge Wasser eingeben, Ablauf prüfen

Während Saison:
  ☐ Nach Regen: Drainage-Funktion prüfen
  ☐ Wöchentlich (bei Salzwasser): kurze Spülung Süßwasser
  ☐ Monatlich: Sichtprüfung Hahnblock-Ventil auf Verschleiß
```

---

## 4. Reling und Fanggeländer (ISO 15085)

### 4.1 Höhe und Material

**ISO 15085 Vorschrift:**

```
Mindesthöhe (über Deck): 900 mm
Empfohlen (Komfort): 1000–1100 mm
Große Yacht/Sicherheit: 1100–1200 mm

Höhe über Wasserlinie (bei maximaler Last):
  Sollte mindestens 500–600 mm über Wasserlinie sein
  → verhindert Übergang-Nass-Werden bei Schlägen
```

**Material-Optionen:**

| Material | Festigkeit | Gewicht | Kosten | Wartung | Haltbarkeit |
|----------|-----------|--------|--------|---------|-----------|
| Edelstahl 316L | Sehr hoch | Mittel | EUR 150–200/m | Jährlich (Salz) | 20+ Jahre |
| Aluminum 6061 | Hoch | Niedrig | EUR 100–150/m | Jährlich (oxidation) | 15–20 Jahre |
| Kunststoff (Polyurethan) | Niedrig | Sehr niedrig | EUR 50–100/m | Minimal | 8–12 Jahre |
| Teak-Handlauf | Moderat | Mittel | EUR 200–300/m | Jährlich (Öl) | 15–20 Jahre |

**Best-Practice: Edelstahl mit Kunststoff-Inlay** (rutschsicher, robust).

### 4.2 Reling-Ausführungs-Details

**Querstützen (Stanchions):**

```
Abstand: 1,5–2,0m (nicht >2m nach ISO)
Höhe: 100–150 mm über Reling-Rohr
Material: Edelstahl 316L Rohr oder solid bar

Befestigung:
  Unten: Weld oder Bolzen (für Deck-Durchführung)
  Oben: Reling-Klemmung (nicht Schweißung, erlaubt Demontage)
  
Querschnitts-Größe:
  Minimal: Ø 20 mm (bei nahem Abstand)
  Standard: Ø 25–32 mm (bei 1,5–2m Abstand)
```

**Oberkaente (Top Rail):**

```
Durchmesser: 30–40 mm (komfortabel zu greifen)
Oberfläche: rau (20–40 µm Ra) für Rutsch-Sicherheit
Material: Edelstahl oder Kunststoff-beschichtetes Aluminum

Verbindungs-Details:
  Nicht direkt schweißen (ermüdet Material)
  Mit Klemmblöcken + Bolzen (erlaubt Spannungs-Relief)
```

**Zwischen-Drähte / Netze:**

```
Für sichere Reling: optionale zusätzliche Drähte zwischen Stanchions
  Material: rostfreier Stahldraht Ø 4–6 mm
  Spannung: 200–400 N pro Draht
  Höhe-Abstände: 300 mm (oben, mitte, unten)

Vorteil: verhindert durchschlupf von Personen/Gegenständen
Nachteil: Komplexität, Wartungsaufwand
```

### 4.3 Reling-Unterbrechungen (Eingangsöffnungen)

**Standardöffnungen:**

```
Typ A: Sprossen (removable stanchions)
  Für Zugang zu Seite-Decks
  Breite: 600–800 mm (komfortabel für Person)
  Anzahl: 2–4 (eine pro Seite, eine vorne, eine hinten)
  
Typ B: Flip-up Reling (klappbar)
  An Heck für Nachtanker-Platz oder Badeleiter
  Material: leicht zu öffnen/schließen
  
Typ C: Drehtür (selten, für Mega-Yachten)
  Vollständig zu öffnen für Zugang
  Muss automatisch rückspulen (Sicherheit)
```

**Zugangs-Kriterium:**

```
Öffnungsbreite sollte:
  ≥ 60 cm (Schulterbreite für schnelle Evakuierung)
  Leicht zu öffnen (manuell, ohne Werkzeug)
  Mit Stopper (verhindert unbeabsichtigtes Öffnen bei Seegang)
```

---

## 5. Sicherheits-Features und Notfall-Ausrüstung

### 5.1 Überboard-Rettungs-Ausrüstung

**Überboard-Ballen (Person Overboard Equipment):**

```
Standard nach SOLAS/ISAF:
  Schwimmender Rettungsballen (Ø 250–300 mm)
  Befestigung: Heck oder Seite (schnell erreichbar)
  Mit Beleuchtung (LED Blitz, 12–24h Batterie)
  Mit Rauch (kalter Rauch, weiß, nicht giftig)
  Mit Wassersack (Ankersack, bremst Drift)

Position:
  Heck-Reling (beste Sichtbarkeit, schnelle Auslösung)
  NICHT im Cockpit (Blockade bei Crash)
  NICHT zu schwer (max. 20 kg, schnelle Auslösung)
```

**Überboard-Heißstelle:**

```
Standard für Motor-Yacht:
  Einschalt-Knopf (roter Pilz, deutlich gekennzeichnet)
  Position: im Cockpit (Steuermann erreichbar, sofort)
  
Aktion:
  Drücken → Rettungsballen automatisch auslösen
  + Motor(en) neutralisieren (optional, je nach Einstellung)
  + Alarm + Signal an Crew
  
Wartung:
  Jährlich: Test-Funktion prüfen (ohne Auslösen)
  Nach Auslösung: sofort Ballen ersetzen
```

### 5.2 Notfall-Lücken im Reling (Reparatur-Fähigkeit)

**Szenario: Stanchion beschädigt, Reling unterbrochen**

```
Provisorische Sicherung:
  1. Beschädigten Stanchion aus Klemmung nehmen (wenn möglich)
  2. Tauwerk um benachbarte Stanchions spannen (Übergangs-Schutz)
  3. Notfall-Stanchion einbauen (sollte an Bord sein)
  4. Oder: Starkes Tauwerk (Ø 8–10 mm) um Reling spannen
  
Sicherheits-Maßnahme während Reparatur:
  - Betroffene Deck-Seite meiden
  - Zusätzliche Aufsicht bei Crew-Bewegung
  - Sicherheits-Harness tragen (wenn möglich)
```

---

## 6. Arbeitsdecks und funktionale Zonen

### 6.1 Hauptsegel-Baum und Gabelbereich

**Boom-Höhe und Clearance:**

```
Durchgangs-Höhe unter Baum (beim Manöver):
  Mindestens 1900–2000 mm freier Kopfraum
  Für sicheres Kreuzen unter dem Baum
  
Boom-Position bei verschiedenen Kursen:
  Anluven (Closehauled): 10–15° zur Mittellinie
  Halsen (Run): 30–45° zur Kante
  Tiefwind: 20–30° zur Mittellinie
  
Boom-Ende (Hals-Position):
  Min. 500 mm von Heck-Reling (Platz für Baum-Schwenkbereich)
  Min. 1000 mm über Wasserlinie (Tiefgang + Sicherheit)
```

**Baum-Beschleunigung (Sicherheits-Bedenken):**

```
Baum-Gewicht: typisch 30–50 kg für 12m Boot
Bei plötzlicher Halse: Auswirkungs-Kraft > Boot-Gewicht möglich!
  Impact-Force ≈ Baum_Mass × Swing_Velocity
  Typisch: 500–2000 N (Kopfwunde-Risiko!)
  
Mitigation:
  1. Ausladungs-Schützer (gepolsterte Abdeckung Baum-Ende)
  2. Schnelle Gabelblock (reduziert Wirbel-Ausstieg)
  3. Automatische Gabelhalter (Carriage-lock bei Halse)
  4. Crew-Training (schnelle Ausweich-Reflex)
```

### 6.2 Decksbelag und Material-Eigenschaften

**Teak vs. Alternative:**

| Material | Rutsch-Beiwert | Haltbarkeit | Temperatur-Komfort | Kosten | Wartung |
|----------|---------------|-----------|------------------|--------|---------|
| Teak (geplant) | 0,7–0,8 | 15–20 Jahre | Warm im Sommer | EUR 200–300/m² | Jährlich ölen |
| Teak (ungeplant) | 0,6–0,7 | 8–12 Jahre | Rutschig nass | EUR 150–200/m² | 2x/Jahr ölen |
| Gitterrost FRP | 0,8–0,9 | 20+ Jahre | Kühl (Metal-Effekt) | EUR 80–150/m² | Minimal |
| Kunststoff Antirutsch | 0,5–0,7 | 10–15 Jahre | Neutral | EUR 50–100/m² | Jährlich |
| Epoxy + Körnung | 0,5–0,6 | 5–8 Jahre | Neutral | EUR 30–60/m² | 2-3 Jahre Refresh |

**Best-Practice:** Teak im Cockpit (Wärmekomfort), Gitterrost an Seiten und Foredeck (Drainage + Sicherheit).

---

## 7. Cockpit-Möbel und Polsterung

### 7.1 Sitz-Ergonomie

**Sitzhöhe und Neigung:**

```
Sitzhöhe über Deck: 300–400 mm
Rückenlehnen-Neigung: 10–20° (nicht senkrecht)
Sitztiefe (vorne bis hinten): 400–500 mm

Polsterung:
  Material: Marine-Leder oder UV-beständiger Kunststoff
  Dicke: 40–60 mm (Komfort + Wärmeisolation)
  Drainage-Loch: Entwässerung nach unten
```

**Kopfstützen (Rückenstütze):**

```
Für lange Fahrten: optional Kopfstütze 100–150 mm hoch
Material: schwach gepolstert (nicht zu soft = Halsflattern)
Befestigung: abnehmbar (einfachere Reinigung)
```

### 7.2 Polster-Schutz

**Material-Auswahl:**

```
Für Salzwasser-Umgebung:
  Nur marine-grade UV-beständiger Kunststoff oder Leder
  Nicht standard-Baumwolle (faulen schnell)
  
Wartung:
  Jährlich: Polyester-Reinigung (1% Seife, Süßwasser)
  2-jährlich: UV-Schutz-Schicht auftragen
  Bei Verschleiß: Bezug austauschbar (auf Rahmen gespannt)
```

---

## 8. Spezielle Decks für Motorboote

### 8.1 Flybridge / Upper Deck

**Nutzung und Layout:**

```
Für Motor-Yacht (16m+):
  Zweites Deck über Hauptcockpit
  Helm-Station mit freiem Blick rundherum
  Lounge/Sun-Deck mit Stühlen + Tisch
  
Größe: 3m × 5m (typisch 16m Boot)
Reling: 1000–1100 mm (gleich wie Hauptdeck)
Treppen: 2–3 Stufen, breit und rutschsicher
```

**Überlade-Warnung:**

```
Gewicht-Limit pro m²: 250–500 kg (abhängig Struktur)
Typisch Flybridge (15 m²): max. 3000–4000 kg
  Inklusive: Möbel, Crew (8 Personen × 80 kg = 640 kg), Wasser (500 kg)
  
Warnung: Overload verursacht:
  - Stabilitäts-Verschlechterung (höheres CG)
  - Struktur-Überlastung (Nieten/Bolzen schwach)
  - Trimm-Verschlechterung (Bug zu tief)
```

---

## 9. Notfall-Deckss und Evakuierung

### 9.1 Escape-Luken (Notfall-Ausstieg)

**ISO 12216 Anforderung:**

```
Mindestens 2 Evakuerungs-Punkte pro Kabine:
  Größe: 400 × 520 mm (Standard Notfall-Fenster)
  Position: von Schlafplatz erreichbar (max. 1,5m Kriechen)
  
Decks-Ausstieg:
  Leicht zu öffnen (nicht verschraubt)
  Mit Halte-Griff außen (für Rettungs-Zugang)
  Mit Dichtgummi (verhindert Wasser-Eindringung)
```

**Notfall-Schlauchboot-Position:**

```
Standard: an Seite + Heck befestigt
Erreichbarkeit: nicht >30 Sekunden zur Auslösung
Gewicht: max. 35 kg (schnelle Handhabung)
Übung: mindestens 1× pro Jahr (Crew-Training)
```

---

## 10. Wartung und Inspektions-Intervalle

### 10.1 Jährliche Kontrollen

```
Vor Saison:
  ☐ Reling: alle Stanchions fest? Keine Risse?
  ☐ Handgriffe: rostig? Lose Bolzen?
  ☐ Drainage: Hahnblock öffnen/schließen Test
  ☐ Segelblöcke: leicht drehend? Verschleiß sichtbar?
  ☐ Teak: Öl nachfüllen (bei unbeplantes Teak jährlich)
  ☐ Sicherheits-Ausrüstung: Überboard-Ballen Beleuchtung prüfen

Nach Saison:
  ☐ Gründliche Spülung Süßwasser (Salzwasser Boote)
  ☐ Drainage System: komplette Kontrolle
  ☐ Sicherheits-Leinen: Verschleiß prüfen
  ☐ Polster: UV-Schaden überprüfen
```

### 10.2 5-Jahres-Inspektionen

```
Alle 5 Jahre:
  ☐ Reling-Stanchions: Schweißnähte prüfen (Risse?)
  ☐ Bolzen: alle anziehen, Korrosions-Check
  ☐ Decksbeschichtung: Risse/Abblätterung? → Reparatur
  ☐ Hahnblock-Ventile: Demontage + Reinigung
  ☐ Sicherheits-Leinen: ggf. Austausch
```

---

## ANHANG A — Glossar

**Antrirungs-Schützer:** Gepolsterte Abdeckung am Baum-Ende (Kopfschutz).

**Boom:** Horizontal-Balken, trägt Hauptsegel-Unterkante.

**Cockpit-Sole:** Boden des Cockpits (unter Sitzbereichen).

**Drainage:** Wasser-Ablauf-System.

**Flybridge:** Oberes Deck auf Motoryacht.

**Foredeck:** Vorderes Arbeitsdeck (Segment-Handhabung).

**Hahnblock:** Absperrventil für Seewasser-Einlass.

**Handgriffe (Deck-Handles):** Befestigung für Crew-Sicherheit.

**Hintern-Cockpit:** Steuerbord-Cockpit (Helm-Station).

**Leinen (Jack Lines):** Sicherheits-Tauwerk vom Bug bis Heck.

**Reling:** Sicherheits-Umzäunung (Höhe 900+ mm).

**Selbstlensung:** Natürliche Wasser-Ableitung aus Cockpit (ohne Pumpe).

**Seitendeck:** Schmale Laufroute entlang Rumpfseiten.

**Stanchion:** Vertikale Stütze für Reling.

**Traveller Rail:** Führungs-Schiene für Segelblock-Position-Anpassung.

**Winde:** Mechanisch angetriebene Seil-Rolle (Segel-Handling).

---

## ANHANG B — Pydantic v2 Validierungs-Modell

```python
from pydantic import BaseModel, Field
from typing import Optional, List

class DeckLayoutFehlerbild(BaseModel):
    """
    Fehlerbild für Deck-Layout nach AYDI-Standard.
    12 spezifische Fehlerbilder mit Schweregrad, Ort, Lösungsweg.
    """
    model_config = {"from_attributes": True}

    # Metadaten
    fehlerbild_id: str = Field(..., description="Eindeutige ID, z.B. '31_10_001'")
    kategorie: str = "31_Design_Konstruktion"
    unterkategorie: str = "Deck_Layout"
    
    # Fehler-Beschreibung
    titel: str = Field(..., description="Kurztitel des Fehlerbilds")
    beschreibung: str = Field(..., description="Detaillierte Fehler-Charakterisierung")
    
    # Symptome und Auswirkungen
    symptome: List[str] = Field(default_factory=list, description="Beobachtbare Zeichen")
    auswirkungen: List[str] = Field(default_factory=list, description="Folgen für Sicherheit/Betrieb")
    
    # Schweregrad
    schweregrad: str = Field(..., description="'kritisch', 'hoch', 'mittel', 'niedrig'")
    sicherheits_impact: bool = Field(default=False, description="Sicherheits-Relevanz")
    
    # Ursprung
    boots_typen: List[str] = Field(default_factory=list, description="Relevante Boot-Klassen")
    deckbereich: str = Field(default="", description="Cockpit/Foredeck/Seitendeck/etc")
    
    # Diagnose und Reparatur
    diagnose_methoden: List[str] = Field(default_factory=list, description="Wie identifizieren?")
    reparatur_optionen: List[str] = Field(default_factory=list, description="Lösungsansätze")
    schaetzung_kosten_eur: Optional[float] = Field(None, description="Grobe Reparatur-Kosten")
    dauer_tage: Optional[int] = Field(None, description="Reparatur-Dauer in Tagen")
    
    # Prävention
    praevention: List[str] = Field(default_factory=list, description="Wie vermeiden?")
    inspektions_intervall_jahre: Optional[float] = Field(None, description="Wartungs-Zyklus")
    
    # Verweise
    normen_referenzen: List[str] = Field(default_factory=list, description="ISO, CE Kategorien")
    verwandte_fehlerbilder: List[str] = Field(default_factory=list, description="Andere Fehler-IDs")


# Beispiel-Instanz
fehlerbild_001 = DeckLayoutFehlerbild(
    fehlerbild_id="31_10_001",
    titel="Cockpit-Volumen zu gering für Selbstlensung",
    beschreibung="Drainage-Fläche / Rohre nicht für Wasser-Volumen dimensioniert.",
    symptome=[
        "Wasser staut sich im Cockpit",
        "Selbstlensung dauert >10 Sekunden",
        "Stagnationswasser nach Regen/Seegang"
    ],
    auswirkungen=[
        "Sicherheit: Boot lädt Wasser, höhere Sinke-Gefahr",
        "Komfort: nasse Cockpit-Sohle → Rutsch-Risiko",
        "Struktur: längere Wasser-Belastung → Delaminierung"
    ],
    schweregrad="hoch",
    sicherheits_impact=True,
    boots_typen=["Segelboot", "Motorsegler"],
    deckbereich="Cockpit",
    diagnose_methoden=[
        "Wasser-Volumen-Messung (Cockpit)",
        "Drainage-Rate Test (5L/min Test)",
        "Rohrdurchmesser Prüfung"
    ],
    reparatur_optionen=[
        "Drainage-Rohre vergrößern (DN40 → DN50)",
        "Zusätzliche Entwässerungs-Öffnung",
        "Bilgenpumpe-Kapazität erhöhen"
    ],
    schaetzung_kosten_eur=3500,
    dauer_tage=5,
    praevention=[
        "ISO 11812 Standard beachten",
        "Cockpit-Volumen berechnen vor Design",
        "Rohrdurchmesser für Flow-Rate prüfen"
    ],
    inspektions_intervall_jahre=3,
    normen_referenzen=["ISO 11812", "CE 2013/53/EU"],
    verwandte_fehlerbilder=["31_10_002", "31_10_005"]
)
```

---

## ANHANG C — FAQ (25+)

**F1: Wie groß sollte das Cockpit-Volumen sein?**
A: Typisch 5–10% des Rumpf-Volumens. Größer = komfortabler, aber schwerer zu entwässern. Standard: 4–8 m³ für 12m Boot.

**F2: Wie oft sollte die Drainage-Anlage gewartet werden?**
A: Visuell jährlich; Funktionsprüfung vor/nach Saison; komplettes Durchspülen alle 2 Jahre.

**F3: Sind zwei Ablauf-Rohre oder ein großes ausreichend?**
A: Zwei kleinere robuster (Redundanz, weniger Verstopfungs-Risiko). Ein großes funktioniert, aber bei Blockade gestranded.

**F4: Wie hoch müssen Sicherheits-Leinen gespannt sein?**
A: Fest, aber nicht straff. Durchhang <5 cm unter Gewicht (z.B. Harness-Zug 100 kg). Zu straff = Spannung-Versagen.

**F5: Kann man Teak mit anderen Hölzern mischen?**
A: Nein, optisch/Wartungs-weiser problematisch. Entweder ganz Teak oder Kunststoff-Gitterrost.

**F6: Wie lange hält eine Reling-Beschichtung?**
A: Edelstahl 316L: 20+ Jahre (mit Pflege). Aluminum-anodisiert: 15 Jahre. Kunststoff: 8–12 Jahre.

**F7: Ist eine Foredeck-Sicherheits-Linie erforderlich?**
A: Ja, nach ISO 15085 + CE-Regel für Boot >8m. Mindestens eine (Backbord + Steuerbord empfohlen).

**F8: Was bedeutet "Selbstlensung"?**
A: Wasser fließt natürlich aus dem Cockpit (durch Drainage), ohne Pumpe. Erfolgt in <5 Sekunden (50% Volumen).

**F9: Kann man Überboard-Ballen täglich benutzen?**
A: Nein, nur Notfall. Batterie begrenzt (~12–24h). Nach Auslösung: sofort ersetzen.

**F10: Wie breit sollten Seitendeck sein?**
A: Mindestens 400 mm (eng), 500–700 mm komfortabel. Breiter = höher Sicherheit aber weniger Deck-Fläche.

---

## 11. Normativer Rahmen (web-verifiziert)

> **Regel:** Jede Norm-Angabe unten ist an der Ausgabestelle (ISO/CEN) geprüft. Titel und Geltungsbereich sind `documented`. **Exakte Zahlenwerte, Koeffizienten und Prüfformeln stehen im kostenpflichtigen Normtext und wurden NICHT rekonstruiert** — wo eine Zahl unten steht, ist ihre Quelle genannt; wo keine steht, gilt sie als "nur im Normtext" und wird hier bewusst nicht erfunden.

### 11.1 Kern-Normen für das Deck-Layout

| Norm | Titel (Geltungsbereich) | Deck-Layout-Bezug | Confidence |
|------|-------------------------|-------------------|-----------|
| **ISO 11591** | *Small craft — Field of vision from the steering position* (Ausgabe 2000/2011/2019, aktuell **2020**; früher "engine-driven", ab 2019 allg. "steering position") | Sichtlinien vom Steuerstand, vorwärts (horizontal+vertikal) und achtern; Boote bis 24 m LH | `documented` |
| **ISO 15085** | *Small craft — Protection from falling overboard and means of reboarding* (1. Ausg. **2003** + Amd 1:2009 + Amd 2:2017; **2. Ausg. 2024** ersetzt diese) | Fanggeländer/Reling, Stützen, Fußleisten, Wiedereinstieg; Boote bis 24 m LH | `documented` |
| **ISO 11812** | *Small craft — Watertight or quick-draining recesses and cockpits* (2001; aktuell **2020** + Amd 1:2024) | Cockpit-Wasserdichtheit, Selbstlenz-Zeit, Süllhöhen; Boote bis 24 m Wasserlinienlänge | `documented` |
| **ISO 15084** | *Small craft — Anchoring, mooring and towing — Strong points* (**2003**; EN-Fassung 2018) | Klampen, Poller, Belegpunkte, Ankerbeschlag — horizontale Auslegungslast $P_n$ | `documented` |
| **ISO 12216** | *Small craft — Windows, portlights, hatches, deadlights and doors — Strength and watertightness requirements* (2020) | Notausstiegs-/Escape-Luken, Fenster an Deck | `documented` |
| **ISO 12217** | *Small craft — Stability and buoyancy assessment and categorization* | Gewichts-/CG-Verteilung an Deck (Flybridge-Überladung, Achterdeck-Trimm) — **Stabilität, NICHT Struktur** | `documented` |
| **ISO 12215** (Teile 1–9) | *Small craft — Hull construction and scantlings* | Beschlag-Unterbau, Verstärkungen unter Winschen/Klampen/Stützen (Scantlings) | `documented` |

> Quelle (Titel/Ausgaben/Scope): iso.org Katalogeinträge zu ISO 11591 (std/80914, std/67210, std/46211), ISO 15085 (std/78010, std/26408), ISO 11812 (std/67204, std/32251), ISO 15084 (std/26407); CEN-CENELEC-Mitteilung zu EN ISO 15085:2024 (cencenelec.eu, 2024-11-18). Abgerufen 2026-07.

### 11.2 Racing- vs. CE-Regelwerk — nicht verwechseln

- **CE / RCD 2013/53/EU** verweist über harmonisierte EN-ISO-Normen (u. a. EN ISO 15085, EN ISO 11812, EN ISO 11591) auf die **Mindestanforderungen für den Verkauf** in der EU. Das ist der gesetzliche Boden.
- **World Sailing Offshore Special Regulations (OSR)** (früher "ISAF OSR") sind ein **Wettfahrt-Regelwerk** für Hochsee-Regatten — strenger und detaillierter als CE, aber **nicht gesetzlich** für Fahrtenyachten. Viele im Bestand (Abschnitt 2.4, 4.x) genannten Zahlen entsprechen OSR-Praxis, nicht CE-Pflicht.

> **Korrekturhinweis zu Bestand Abschnitt 2.4:** Die Referenz "ISAF/IMS" für Jack Lines ist unpräzise — maßgeblich ist heute **World Sailing OSR** (der Nachfolger von ISAF-OSR); "IMS" ist eine Vermessungsformel und regelt keine Sicherheitsleinen. `documented`

---

## 12. Sichtlinien vom Steuerstand (ISO 11591) — NEU

> Dieses Themenfeld fehlte im Bestand v2.0 vollständig und ist für die AYDI-Ergonomie-/Compliance-Module load-bearing.

### 12.1 Grundprinzip

ISO 11591 legt das **Sichtfeld von der Steuerposition** fest — vorwärts (horizontal und vertikal) und achtern — für Kleinfahrzeuge bis **24 m Rumpflänge (LH)**. Ziel ist die Vermeidung von Kollisionen durch tote Winkel. Die Norm unterscheidet Risiko-Bewertungen für motor- und segelgetriebene Fahrzeuge wegen ihrer unterschiedlichen Geschwindigkeitsbereiche.

> Quelle: ISO 11591 Scope, iso.org std/80914 (2020) und std/46211 (2011). `documented`

**Verifizierte Kernanforderung (horizontales Vorwärts-Sichtfeld):**

> Das vorwärtige horizontale Sichtfeld muss von der Augenposition des Rudergängers **mindestens 112,5° nach Steuerbord und 112,5° nach Backbord** umfassen (zusammen 225° vorderer Sektor), **ohne dass der Bediener die Steuerposition verlassen muss**.

> Quelle: Zusammenfassung ISO 11591 (iso.org / GlobalSpec std/13271659). Der Wert 112,5° entspricht dem seitlichen Grenzwinkel der KVR/COLREG-Bugsektor-Definition (Seitenlichter: je 112,5°). `documented`

> ⚠️ ZU PRÜFEN (Audit): Die **vertikalen** Sichtwinkel, die zulässige **Blindsektor-Breite direkt voraus** (Bugwelle/tote Zone auf der Wasseroberfläche) und die Mess-Augenpunkte (Höhe/Position) sind **quantitativ nur im Normtext** definiert und wurden hier NICHT rekonstruiert — nicht erfinden.

### 12.2 Trimm-/Verdrängungsübergang (verifiziert, qualitativ)

ISO 11591 stellt ausdrücklich fest, dass schnelle motorgetriebene Boote bei bestimmten Geschwindigkeiten Trimmwinkel erreichen, bei denen die **Vorwärtssicht vorübergehend verdeckt** wird, und dass die Norm eine Bedienung **ohne** zeitweisen Sichtverlust im **Übergang von Verdrängungs- zu Gleitfahrt** nicht garantieren kann. Für tillergesteuerte Boote mit Höchstgeschwindigkeit **< 10 kn** sowie reine Segelboote galt die Ausgabe 2011 nicht; ab 2019/2020 ist der Titel auf "steering position" verallgemeinert.

> Quelle: ISO 11591 Scope-Text (iso.org std/46211, 2011). `documented`

**Konstruktive Konsequenz fürs Deck-Layout:**
- Steuerstand/Flybridge-Höhe so wählen, dass der tote Sektor voraus im Gleitübergang begrenzt bleibt (Sitz-/Steh-Augpunkt erhöhen).
- Aufbauten, Sprayhood, Bimini-Rahmen, Ankergalgen und gestapelte Segelbeutel **nicht in den 225°-Vorwärtssektor** stellen.
- Der Owner's Manual muss laut Norm auf Sicht-Einschränkungen und -Warnungen hinweisen (dokumentationspflichtig). `documented`

---

## 13. Fanggeländer / Reling — Präzisierung nach ISO 15085:2024

> Dieser Abschnitt **präzisiert und korrigiert** Bestand Abschnitt 4 mit verifizierten Werten der 2. Ausgabe (2024).

### 13.1 Verifizierte Kernwerte ISO 15085:2024

| Element | Verifizierter Wert | Quelle | Confidence |
|---------|--------------------|--------|-----------|
| **Niedrige** Überbord-Barriere (low barrier), Mindesthöhe | **450 mm** | CEN-CENELEC 2024-11-18; ISO 15085:2024 Zusammenfassung | `documented` |
| **Hohe** Überbord-Barriere (high barrier), Mindesthöhe | **600 mm** | CEN-CENELEC 2024-11-18 | `documented` |
| Fußleiste (footrail/toe rail), Segelboot | ≥ **25 mm** | CEN-CENELEC 2024-11-18 | `documented` |
| Fußleiste (footrail/toe rail), Motorboot | ≥ **20 mm** | CEN-CENELEC 2024-11-18 | `documented` |
| Deck-Zonen | **Z1 / Z2 / Z3** (nach Absturzrisiko gestaffelt); rutschhemmende Oberfläche in allen begangenen Bereichen | CEN-CENELEC 2024-11-18 | `documented` |
| Schnellboote > **25 kn** | zusätzliche Körperstützen und Handgriffe; verschärfte Sitz-Festigkeit | CEN-CENELEC 2024-11-18 | `documented` |
| Wiedereinstieg (reboarding) | ohne fremde Hilfe möglich; Leiter (starr/flexibel) muss Last + Lastwechsel standhalten | CEN-CENELEC 2024-11-18 | `documented` |

> **Wichtige Einordnung:** Die Barrierehöhen 450 mm / 600 mm sind **abgestufte Mindesthöhen der Norm** (je nach Zone/Bootstyp), NICHT die im Bestand Abschnitt 4.1 genannten "900 mm". Der 900-mm-Wert entspricht eher einer **Komfort-/Landgeländer-Höhe** und ist keine ISO-15085-Mindesthöhe. Konkrete Zuordnung Höhe↔Zone↔Bootskategorie steht im Normtext.

> ⚠️ ZU PRÜFEN (Audit): Welche Barrierehöhe (450 vs. 600 mm) für welche **Zone/Design-Kategorie/Bootstyp** gilt, sowie exakte **Stützenabstände** und **Festigkeits-/Prüflasten** stehen quantitativ nur im ISO-15085-Normtext. Bestand-Werte in 4.2 (Stützenabstand 1,5–2,0 m) und die OSR-Werte in 13.2 sind als **Richtwert `estimated`** zu behandeln, nicht als ISO-15085-Zitat.

### 13.2 World-Sailing-OSR-Vergleichswerte (Regatta-Regelwerk, nicht CE)

Diese Werte stammen aus den **World Sailing Offshore Special Regulations** und sind für Fahrtenyachten **kein Pflichtmaßstab**, aber gute Best-Practice-Orientierung:

| OSR-Anforderung | Wert | Confidence |
|------------------|------|-----------|
| Max. vertikale Öffnung im Geländer-System | **560 mm (22 in)** | `documented` |
| Stützen-Neigung: innerhalb erste 50 mm über Deck kein Versatz > 10 mm; darüber max. **10°** aus der Vertikalen | s. links | `documented` |
| Stützenabstand (Auflager der Lifeline) | ca. **2,13 m (84 in)** max. | `documented` |
| Einzel-Lifeline-Höhe (kleine Altboote < 8,5 m, Registrierung vor 1992) | ≥ **450 mm (18 in)** über Arbeitsdeck | `documented` |
| Lifeline-Höhe Boote ≥ 8,5 m (28 ft) | ≥ **610 mm (24 in)** | `documented` |

> Quelle: World Sailing / ISAF OSR (sailing.org OSR-Dokumente 2008–2014; SPSC-Bericht Stanchions/Pulpits/Lifelines). `documented`

> **Konsistenz-Notiz:** OSR-Lifeline ≥ 600 mm und ISO-15085-"high barrier" ≥ 600 mm stimmen größenordnungsmäßig überein — das stützt 600 mm als robusten Planungswert für die **obere** Fanggeländer-Leine oberhalb Deck.

---

## 14. Beschlag-Platzierung: Klampen, Winschen, Strong Points

> Neuer Kern-Abschnitt zum Thema (Winsch-/Klampen-/Beschlag-Platzierung). Formeln nur, wo dokumentiert; Einheiten explizit.

### 14.1 Belegpunkte / Klampen — ISO 15084

ISO 15084:2003 legt **Belegpunkte (strong points)** zum Ankern, Vertäuen und Schleppen für Boote bis 24 m LH fest. Kernprinzip (verifiziert):

- Jeder Belegpunkt muss eine **horizontale Last $P_n$ [kN]** aufnehmen, **ohne Versagen des Beschlags oder der umgebenden Struktur**, an die er angeschlossen ist.
- Die geforderte Bruchlast eines Belegpunkts muss **nicht höher** sein als die Last, die die **Masse des voll ausgerüsteten, einsatzbereiten Bootes** repräsentiert.
- Erfasste Beschläge: Poller, Klampen, Samson-Posten, Mastfuß, Bugauge (Trailerboote), Winschen, Ankerwinden, Spills.

> Quelle: ISO 15084:2003 Scope (iso.org std/26407). `documented`

> ⚠️ ZU PRÜFEN (Audit): Die **Tabelle der $P_n$-Werte** nach Bootslänge/-masse und die zugehörigen Sicherheitsfaktoren stehen quantitativ nur im Normtext. Bestand Abschnitt 2.3 nennt "10–20 kN pro Auge / 30–50 kN pro Block" — diese Werte sind **`estimated`**, kein ISO-15084-Zitat.

**Konstruktive Grundregeln (dokumentierte Praxis):**
- Klampe/Poller braucht einen **strukturellen Unterbau** (Backing Plate) nach ISO 12215-Logik — Punktlast in Laminat/Deck verteilen, nie nur Gelcoat/Sandwich-Deckhaut verschrauben.
- Zuglinie der Leine soll **flach zur Klampe** verlaufen; hoher Aufwärtszug (z. B. über Klampe hinweg) erzeugt Hebel und Ausriss-Moment.
- Klampen **frei anströmbar** platzieren (Fender-/Leinenführung), nicht hinter Relingfuß/Süll verdeckt.

### 14.2 Klampen-Dimensionierung (dokumentierte Faustregel)

**Regel:** Klampenlänge ≈ **1 in (25,4 mm) Klampenlänge je 1/16 in (1,6 mm) Leinendurchmesser**.
Beispiel (konsistent gerechnet): 3/8-in-Leine (≈ 9,5 mm) = 6 × 1/16 in → **6-in-Klampe (≈ 150 mm)**.

> Quelle: BoatUS-Foundation-Faustregel, zit. n. mehreren Beschlag-Ratgebern (fisheriessupply, havendock, betterboat). `documented`
> Hinweis: In einer Quelle war ein Rechenbeispiel ("1/2 in → 6 in") intern widersprüchlich; hier ist die **Regelform** maßgeblich, das Beispiel oben ist regelkonform nachgerechnet.

**Vertäu-Leinen-Durchmesser nach Bootslänge (verifizierte Richttabelle):**

| Bootslänge | Leinen-Ø | 
|------------|----------|
| bis 27 ft (≈ 8,2 m) | 3/8 in (9,5 mm) |
| 28–31 ft (≈ 8,5–9,4 m) | 1/2 in (12,7 mm) |
| 32–36 ft (≈ 9,8–11 m) | 5/8 in (15,9 mm) |
| 37–45 ft (≈ 11,3–13,7 m) | 3/4 in (19,1 mm) |
| 46–54 ft (≈ 14–16,5 m) | 7/8 in (22,2 mm) |
| 55–63 ft (≈ 16,8–19,2 m) | 1 in (25,4 mm) |

> Quelle: betterboat.com Dock-Line-Size-Chart. `documented`
> **Wichtig:** Verdrängung (Bootsgewicht) zählt mehr als Länge allein — schwere Yacht eine Stufe größer wählen. `documented`

### 14.3 Winsch-Platzierung und -Leistung

**Ergonomie / Platzierung (dokumentierte Praxis):**
- Winsch so setzen, dass der **Kurbelkreis frei** dreht (keine Kollision mit Süll, Sprayhood, Nachbarwinsch, Traveller) — Radius = Kurbellänge + Handknöchel.
- Der einlaufende Leinenwinkel zur Trommel soll **leicht aufwärts (ca. 5–8°)** sein, damit sich die Törns nicht übereinanderlegen (Override) — Umlenkblock/Leadblock entsprechend setzen.
- Self-Tailing-Winschen sind heute für die meisten Funktionen erste Wahl (Zweihand-/Solo-Betrieb).

> Quelle: Harken/West-Marine/Jimmy-Green Winsch-Auswahl-Ratgeber. `documented`

**Power Ratio (dokumentierte Definition):**

$$\text{Power Ratio} = \frac{\text{Kurbellänge}}{\text{Trommelradius}} \times \text{Getriebeübersetzung}$$

Beispiel (dokumentiert, Harken): Kurbel 10 in, Trommel-Ø 5 in (Radius 2,5 in), Getriebe 6:1 → (10 / 2,5) × 6 = **24:1**.

> Quelle: Harken "Choosing Winch Power" (zit. n. Suchindex). `documented`
> Faustregel Kurbellänge: **Trommelradius × 4** (z. B. Radius 2,5 in → 10-in-Kurbel; 3 in → 12-in-Kurbel). `documented`

**Genua-Schotlast (dokumentierte Industrieformel, imperial):**

$$\text{Schotlast [lbs]} = SA \times V^2 \times 0{,}00431$$

mit **SA** = Segelfläche [sq ft], **V** = (scheinbare) Windgeschwindigkeit [kn]. Da $V$ quadratisch eingeht, dominiert die Windgeschwindigkeit die Last.

> Quelle: Harken Genoa-System-Loading-Formel, unabhängig bestätigt (Sailing-Anarchy-Rigging-Thread; l-36.com Jibsheet-Load-Calculator). `documented`
> ⚠️ Einheiten beachten: Ergebnis in **lbs**, Eingaben imperial. Für SI mit Faktor umrechnen (1 lbf ≈ 4,448 N). Coefficient 0,00431 ist empirisch (Industrie), **keine ISO-Formel** — als `documented` (Herstellerpraxis), nicht `measured` behandeln.

---

## 15. Cockpit-Entwässerung (ISO 11812) — Korrektur zu Abschnitt 1.1 / 3.1

> **Korrekturhinweis (wichtig):** Die im Bestand (Abschnitte 1.1 und 3.1) durchgerechneten Rohrdurchmesser von **417–588 mm** sind **physikalisch unplausibel** und beruhen auf einer fehlerhaften Anwendung von $A=Q/v$ (die "5-Sekunden/50 %"-Annahme ist keine ISO-11812-Vorgabe). Der Bestandstext erkennt dies selbst ("unrealistisch"). Diese Rechenbeispiele sind **nicht als Bemessungsgrundlage zu verwenden.**

**Verifizierter Rahmen ISO 11812:2020:**
ISO 11812:2020 spezifiziert **Wasserdichtheit, Entwässerungszeit (draining time) und Süllhöhen** für wasserdichte bzw. schnell lenzende Vertiefungen und Cockpits bei Booten bis 24 m Wasserlinienlänge. Betrachtet wird **ausschließlich Schwerkraft-Entwässerung** (kein Pumpen).

> Quelle: ISO 11812:2020 Scope (iso.org std/67204). `documented`

> ⚠️ ZU PRÜFEN (Audit): Die **konkrete zulässige Entwässerungszeit**, die **Mindest-Abflussquerschnitte/Rohrzahl** und die **Süllhöhen je Design-Kategorie (A/B/C/D)** sind quantitativ **nur im Normtext** von ISO 11812:2020 definiert und wurden hier NICHT rekonstruiert oder erfunden. Die im AYDI-`compliance`-Modul hinterlegten Süllhöhen (Cat A=300 / B=250 / C=150 / D=0 mm) sind **AYDI-interne Spec-Werte** (CLAUDE.md) und als solche `documented (AYDI-intern)`, nicht als wörtliches ISO-11812-Zitat, zu führen.

**Dokumentierte qualitative Bemessungsprinzipien (statt der falschen Rechnung):**
- Cockpit-Sole so hoch wie möglich über der Wasserlinie (statischer Abstand), damit Selbstlenzung überhaupt durch Schwerkraft funktioniert.
- Mindestens **zwei** Abläufe (Redundanz bei Verstopfung; Bestand Abschnitt 3.1/FAQ F3 korrekt).
- Abläufe an der **tiefsten Stelle** der Sole, Sole mit Gefälle dorthin.
- Seeventile (Seacocks) unter Wasserlinie in **Bronze** oder normgerechtem Verbundwerkstoff; Kunststoff nur, wenn ausdrücklich seewasser-/feuertauglich zugelassen.

---

## 16. Fehlerbild-Atlas (FB-31-10-xxx)

> **ID-Schema:** `FB-31-10-NNN`, fortlaufend, **kollisionsfrei** zu den Bestand-Bezeichnern ("Fehleranalyse-Schwerpunkte 1–12" in der Übersicht und der Pydantic-ID `31_10_001`). Jede Faktenzeile ist auf Abschnitt 11–15 verifiziert oder als `estimated` gekennzeichnet.

### FB-31-10-001 — Toter Sektor voraus am Steuerstand (ISO 11591)
- **Symptom:** Rudergänger sieht Wasseroberfläche voraus erst in großem Abstand; Aufbau/Bimini/Ankergalgen verdeckt Bugsektor; im Gleitübergang zeitweise "blind".
- **Norm:** ISO 11591 (Vorwärts-Sektor ≥ 112,5° je Seite; Owner's-Manual-Warnpflicht). `documented`
- **Ursache:** Steuerstand zu tief/zu weit achtern; Sprayhood/Beschläge im Sichtsektor; Trimm im Verdrängungs-Gleit-Übergang.
- **Lösung:** Augpunkt erhöhen (Sitz/Podest); Sichtsektor freiräumen; Trimmklappen/Interceptor; Kamera/Blindzonen-Assistenz. **Schweregrad: hoch (Kollisionsrisiko).**

### FB-31-10-002 — Fanggeländer unter ISO-15085-Mindesthöhe
- **Symptom:** Obere Leine/Barriere unterschreitet die abgestufte Mindesthöhe (450/600 mm je Zone); Absturzschutz unzureichend.
- **Norm:** ISO 15085:2024 (low 450 mm / high 600 mm). `documented`
- **Lösung:** Stützen erhöhen / Barrierehöhe anheben; Fußleiste ≥ 25 mm (Segel) / 20 mm (Motor) ergänzen. **Schweregrad: hoch (Überbord).**

### FB-31-10-003 — Zu große vertikale Öffnung im Geländer
- **Symptom:** Person/Gegenstand kann zwischen den Leinen durchrutschen.
- **Best-Practice (OSR):** vertikale Öffnung max. **560 mm**. `documented` (OSR, nicht CE)
- **Lösung:** Zwischenleine/-draht einziehen; Netz im Bugbereich (Kinder/Segelbeutel). **Schweregrad: mittel–hoch.**

### FB-31-10-004 — Stützenabstand zu groß / Stütze zu schräg
- **Symptom:** Geländer federt/gibt nach; Stütze biegt bei Belastung aus.
- **Best-Practice (OSR):** Auflagerabstand ≤ **2,13 m**; Neigung ≤ **10°** über 50 mm Deckhöhe. `documented` (OSR)
- **Hinweis:** Exakte ISO-15085-Prüflasten nur im Normtext (`estimated` für Zwischenwerte).
- **Lösung:** Zusatzstütze; steiferer Stützenfuß mit Backing Plate. **Schweregrad: mittel.**

### FB-31-10-005 — Klampe/Belegpunkt reißt Struktur aus (ISO 15084)
- **Symptom:** Klampe/Poller lockert sich, Gelcoat-Risse sternförmig, Deck delaminiert unter Zug.
- **Norm:** ISO 15084 ($P_n$ ohne Versagen von Beschlag **oder umgebender Struktur**). `documented`
- **Ursache:** fehlende Backing Plate; Verschraubung nur in Sandwich-Deckhaut; zu kleine Klampe.
- **Lösung:** Backing Plate / Kompressionsrohr im Kern; Klampe nach 1-in-je-1/16-in-Regel dimensionieren; Zuglinie flach. **Schweregrad: hoch (Vertäuen/Schleppen/Anker).**

### FB-31-10-006 — Winsch-Override durch falschen Einlaufwinkel
- **Symptom:** Törns legen sich übereinander (Override), Schot klemmt unter Last.
- **Ursache:** Leinen-Einlauf horizontal/abwärts statt leicht aufwärts (≈ 5–8°); Leadblock falsch positioniert.
- **Lösung:** Umlenkblock höher/tiefer setzen; Winsch leicht kippen. `documented` (Herstellerpraxis) **Schweregrad: mittel (Handling/Sicherheit unter Last).**

### FB-31-10-007 — Winsch unterdimensioniert (Power Ratio zu klein)
- **Symptom:** Genua/Groß lässt sich bei Frischwind nicht mehr dichtholen; Crew überfordert.
- **Methode:** Schotlast $= SA \times V^2 \times 0{,}00431$ [lbs] gegen Winsch-Power-Ratio prüfen. `documented`
- **Lösung:** größere/Self-Tailing-Winsch, korrekte Kurbellänge (Radius × 4), ggf. elektrisch. **Schweregrad: mittel.**

### FB-31-10-008 — Winsch-Kurbelkreis kollidiert mit Umgebung
- **Symptom:** Kurbel schlägt an Süll/Sprayhood/Nachbarwinsch; Vollkreis nicht möglich.
- **Lösung:** Winsch versetzen; Abstand = Kurbellänge + Knöchelfreiraum rundum. `documented` **Schweregrad: mittel.**

### FB-31-10-009 — Laufweg zu schmal / Handlauf-Lücke
- **Symptom:** Seitendeck < 400 mm ohne durchgehenden Handlauf; Crew balanciert am Aufbau.
- **Bezug:** ISO 15085 (Zonen Z1–Z3, rutschhemmende Fläche, Handhalte-Kontinuität). `documented`
- **Lösung:** durchgehende Handläufe (max. Griffabstand so, dass immer ein Griff erreichbar), rutschhemmende Beläge, Jackstay-Anschlagpunkte. **Schweregrad: hoch (Überbord).**

### FB-31-10-010 — Jackstay/Sorgleine falsch geführt oder verschlissen
- **Symptom:** Sorgleine erlaubt Überbordgehen (zu weit außen geführt), oder UV-/Scheuerschaden.
- **Bezug:** World Sailing OSR (Jackstays); ISO 15085 (Anschlagpunkte). `documented`
- **Ursache:** Jackstay zu nah an Deckskante; Gurtband UV-degradiert.
- **Lösung:** Jackstay **mittig/innen** führen (Lifeline-Länge so, dass Crew inboard bleibt); Gurtband nach Herstellerfrist tauschen (UV). **Schweregrad: hoch.**

### FB-31-10-011 — Escape-Luke blockiert/unterdimensioniert (ISO 12216)
- **Symptom:** Notausstieg klemmt, verstellt oder zu klein.
- **Bezug:** ISO 12216 (Festigkeit/Dichtheit); AYDI-`compliance`: Escape-Luke min. **400 × 520 mm** (CLAUDE.md-Spec). `documented (AYDI-intern)`
- **Lösung:** Luke freihalten, gängig halten, Dichtung prüfen. **Schweregrad: kritisch (Evakuierung).**

### FB-31-10-012 — Flybridge/Achterdeck überladen → Trimm/Stabilität (ISO 12217)
- **Symptom:** hohes CG, Trimm bug-/hecklastig, verschlechterte Stabilität.
- **Bezug:** ISO 12217 (Stabilität/CG) — **nicht** ISO 12215 (Struktur). `documented`
- **Lösung:** Gewichtslimit pro Fläche einhalten (Bestand 8.2 nennt Richtwerte `estimated`), schwere Ausrüstung tiefer/mittiger. **Schweregrad: hoch (Stabilität).**

> **Verweistabelle Bestand ↔ Atlas:** Bestand-Schwerpunkt 3 (Fanggeländer) → FB-002/003/004; Schwerpunkt 4 (schmale Decks) → FB-009; Schwerpunkt 8 (Winsch-Position) → FB-006/007/008; Schwerpunkt 11 (Achterdeck-Überladung) → FB-012; Schwerpunkt 6 (Abflussdimensionierung) → siehe Korrektur Abschnitt 15.

---

## 17. Ergänzende FAQ (verifiziert)

**F11: Welche Norm regelt die Sicht vom Steuerstand?**
A: **ISO 11591** (aktuell 2020). Vorwärtssektor ≥ 112,5° je Seite ohne Verlassen der Steuerposition; bei schnellen Motorbooten ist im Gleitübergang zeitweiser Sichtverlust möglich (Warnpflicht im Handbuch). `documented`

**F12: Wie hoch muss das Fanggeländer nach aktueller ISO wirklich sein?**
A: ISO 15085:2024 nennt **abgestufte Mindesthöhen 450 mm (low) / 600 mm (high)** je Zone/Bootstyp — nicht pauschal 900 mm. Welche Höhe wo gilt, steht im Normtext. `documented`

**F13: Was ist der Unterschied zwischen CE-Pflicht und World-Sailing-OSR-Werten?**
A: CE (RCD 2013/53/EU über harmonisierte EN-ISO) ist gesetzlicher Verkaufs-Mindeststandard; OSR ist ein strengeres **Regatta**-Regelwerk und für Fahrtenyachten nicht verbindlich. Viele Reling-Zahlen im Umlauf stammen aus OSR. `documented`

**F14: Welche Norm regelt Klampen/Poller?**
A: **ISO 15084** (Belegpunkte für Ankern/Vertäuen/Schleppen). Sie fordert Aufnahme einer horizontalen Last $P_n$ ohne Versagen von Beschlag **oder** Struktur; Zahlenwerte nur im Normtext. `documented`

**F15: Wie groß muss eine Klampe für meine Vertäuleine sein?**
A: Faustregel **1 in Klampenlänge je 1/16 in Leinen-Ø**; z. B. 3/8-in-Leine → 6-in-Klampe. Leinen-Ø nach Bootslänge (Tabelle 14.2), im Zweifel eine Stufe größer bei schwerem Boot. `documented`

**F16: Wie prüfe ich, ob meine Genua-Winsch stark genug ist?**
A: Schotlast $= SA \times V^2 \times 0{,}00431$ [lbs] abschätzen (SA in sq ft, V in kn) und gegen die Winsch-Power-Ratio = (Kurbellänge/Trommelradius) × Getriebe stellen. `documented` (Herstellerformel, imperial).

**F17: Stimmt die 588-mm-Ablaufrohr-Rechnung aus Abschnitt 1.1/3.1?**
A: **Nein.** Sie beruht auf einer nicht-normgerechten Annahme und ist unplausibel (siehe Korrektur Abschnitt 15). Maßgeblich sind die im ISO-11812:2020-Normtext definierten Entwässerungszeiten/-querschnitte; mindestens zwei Abläufe (Redundanz). `documented`

---

**Redaktion & Qualitätskontrolle:** AYDI Knowledge Engineering v6  
**Letzte Überprüfung:** 2026-07-13 (v2.1 — web-verifizierte Erweiterung: ISO 11591, ISO 15085:2024, ISO 15084, ISO 11812:2020; Fehlerbild-Atlas)  
**Gültig für:** Segelboote, Motorsegler, Motorboote 8–40m LOA

**Verifikations-Quellen (Abschnitte 11–17):**
- ISO-Katalog: 11591 (std/80914, std/67210, std/46211), 15085 (std/78010, std/26408), 11812 (std/67204, std/32251), 15084 (std/26407) — iso.org
- CEN-CENELEC: "Stay on board — revised Safety Standard EN ISO 15085:2024" (cencenelec.eu, 2024-11-18)
- World Sailing / ISAF Offshore Special Regulations 2008–2014 (sailing.org); SPSC-Bericht Stanchions/Pulpits/Lifelines
- Winsch/Schotlast: Harken "Choosing Winch Power" / Genoa System Loading; unabhängig bestätigt (Sailing Anarchy Rigging-Thread, l-36.com)
- Klampen/Leinen: BoatUS-Foundation-Faustregel; betterboat.com Dock-Line-Size-Chart
> Alle faktischen Neu-Angaben sind `documented`; nicht zweifelsfrei aus autoritativer Quelle belegbare Zahlen sind als `estimated` oder "⚠️ ZU PRÜFEN (Audit) — nur im Normtext" markiert und wurden NICHT erfunden.
