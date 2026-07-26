# 31_11 — Interieur-Layout

**Kategorie:** 31_Design_Konstruktion  
**Unterkategorie:** Interieur_Layout  
**Version:** 2.0  
**Stand:** 2026-05-18  
**Relevanz:** Ergonomie, Komfort, Funktionale Effizienz im Innenraum

---

## Übersicht

Das Interieur-Layout bestimmt **Wohnkomfort**, **Funktionalität** (Küche, Navigation), **Schlafqualität** und **Notsituations-Handling**. AYDI analysiert Kabinenabordnung, Gangway-Breite, Arbeitsbereiche und Trimm-Stabilität unter Seegang und Heel-Situationen.

**Fehleranalyse-Schwerpunkte:**
1. Passagen zu eng (Crew-Bewegung behindert, Notsituations-Evakuierung schwierig)
2. Kopffreiheit unzureichend (Verletzungs-Risiko, Unbehagen)
3. Kabinen-Layout unflexibel (Schlaf-/Arbeitskonflikt)
4. Galleys zu klein oder schlecht organisiert (Unfallrisiko unter Seegang)
5. Navigations-Station schlecht erreichbar / sichtbar
6. Kopf (WC) Position ungünstig (Nässe-Propagation, Geruchsvermeidung)
7. Lüftungs-Durchzug mangelhaft (Muff, Schimmel, Feuchtigkeit)
8. Möbel nicht für Heel-Winkel optimiert (Rutschgefahr, Unbequemlichkeit)
9. Stauraum unzureichend (Gegenstände-Migration, Verschiebungs-Risiko)
10. Trimmung bei Last-Verteilung beeinträchtigt
11. Akustik-Isolierung schwach (Motoren-Lärm, Schlag-Geräusche)
12. Flucht-Routen im Notfall blockiert

---

## 1. Allgemeine Kabinenabordnung und Zoning

### 1.1 Standard-Zonen und deren Funktion

**Segelboot-Standard (12–16m) — 3-Zonen-Modell:**

```
Vorn (Bug-Zone):
  - V-Bett (doppeltes Schlafzimmer, V-Form)
  - Lüftung: 2 Bullaugen + Oberlicht
  - Stauraum: unter Bett, Bug-Schränke
  - Größe typisch: 3,5m Länge × 2m Breite (max) × 1,8m Kopffreiheit

Mittel (Main-Zone):
  - Galley (Küche, eine oder beide Seiten)
  - Navigations-Station (zusammen mit Saloon)
  - Saloon (Essbereich + Arbeitsplatz)
  - Größe: 4–5m Länge × 2,2m Breite

Hinten (Aft-Cabins):
  - Doppel-Kabine (achtern) oder 2× Einzel-Kojen
  - Kopf (WC + Dusche/Wäschen)
  - Größe: 3m Länge × 2m Breite (pro Kabine)
```

**Motoryacht-Standard (16–24m) — 4-Zonen-Modell:**

```
Vorn: VIP-Suite (großes Bett, privates Bad)
Mittel-Vorn: 2–4 Gästekabinen
Mittel-Aft: Master-Suite + Galley + Salon
Aft: Crew-Bereich oder zusätzliche Benutzer-Kabinen
```

### 1.2 Kabinengroße und Kopffreiheit (ISO 12217-2)

> ⚠️ **ZU PRÜFEN (Audit):** Normbezug falsch — ISO 12217(-2) regelt *Stabilität und Auftrieb von Kleinfahrzeugen* (Small craft — Stability and buoyancy assessment and categorization), NICHT Kabinenmaße oder Kopffreiheit. Die folgenden Maßangaben haben keinen gültigen Normbezug → estimated — unverifiziert. Quelle: ISO 12217-2:2015 / :2022 (iso.org/standard/68141.html).

**Schlafplatz-Dimensionierung:**

| Platz-Typ | Länge [cm] | Breite [cm] | Kopffreiheit [cm] | Min. Fläche [m²] |
|----------|-----------|-----------|------------------|----------|
| Einzelkojen | 190 | 60 | 80 | 1,14 |
| Doppelbett | 190 | 140 | 80 | 2,66 |
| V-Bett | 200 | 150–220 | 80 | 3,00 |
| Pullman-Kojen (Kinderkoje) | 160–180 | 50–60 | 60 | 0,80 |

**Kopffreiheit (über Schlafplatz):**
```
Minimum nach ISO: 800 mm
Komfort: 900–1000 mm
Große Yachten: 1100+ mm

Unter Seegang: tatsächliche verfügbare Höhe reduziert sich durch:
  - Seegang (1–3m): ±200 mm Bewegung
  - Heel (20°): effektive Höhe sinkt (vertikale Komponente)
  
Effektive_Kopffreiheit [cm] = nominal - seegang_margin - heel_effect
```

### 1.3 Gangway-Breite und Zugänglichkeit

**Durchgangs-Mindest-Breite (ISO 12217-2):**

> ⚠️ **ZU PRÜFEN (Audit):** Normbezug falsch — ISO 12217-2 regelt Stabilität/Auftrieb von Segelbooten ≥ 6 m, NICHT Durchgangs-/Gangway-Mindestbreiten. Die folgenden Breitenangaben haben keinen gültigen Normbezug → estimated — unverifiziert. Quelle: ISO 12217-2:2015 / :2022 (iso.org/standard/68141.html).

| Element | Breite [cm] | Anwendung |
|---------|-----------|----------|
| Hauptgang (Saloon) | 60–70 | Normales Begehen |
| Kabinen-Eingang | 50–60 | Ein-Person-Passage |
| Notfall-Flucht | 40 | Mindestens eine Strecke |
| Knie-Raum | 40–50 | Unter Tischen passierbar |

**Höhe der Durchgänge:**

```
Saloon-Deckshöhe: 190–210 cm (Standard)
Kabinen-Durchgang: 180–190 cm
Unter-Deck-Schränke: 150–180 cm (akzeptabel)

Bei 20° Heel:
  Effektive Höhe Saloon: 190 × cos(20°) = 178 cm (reduziert)
  Vorsicht: Crew über 180 cm muss in Zonen der halben Höhe ducken
```

---

## 2. Kabinen-Arrangemts (Standard-Konfigurationen)

### 2.1 3-Kabinen-Anordnung (Segelboot 12–14m)

**Typisches Layout:**

```
VORN:
  V-Bett (2 Personen, 3,5 × 2,0m)
  
MITTEL:
  Saloon + Galley (4,5 × 2,2m)
  Navigations-Station (integriert in Saloon)
  
ACHTERN:
  Doppel-Kabine (3,0 × 2,0m, 2 Personen)
  Kopf + Dusche (1,5 × 1,2m)
  
TOTAL: 5–6 Schlafplätze, 50–60 m³ Innenraum
```

**Belegung-Szenarien:**

```
Szenario A: Paar + Gäste (4–6 Personen)
  Steuermann + Partnerin: Master-Kabine
  Gäste: V-Bett + Doppel-Kabine
  Crew: Kojen in Saloon (optional, nicht empfohlen)

Szenario B: Großfamilie (6–8 Personen)
  Zusätzliche Kojen auf Saloon-Bänken (Pull-outs)
  Überbelegung: akzeptabel für Wochenenden, nicht Langfahrt
  Problem: Luft-Qualität leidet (CO₂-Ansammlung)
```

### 2.2 4-Kabinen-Anordnung (Motorsegler 16–18m)

**Anordnung:**

```
VORN-VIP:
  Doppel-Suite, eigenes Bad (3,5 × 2,5m)
  
VORN-GAST 1 + 2:
  Einzelbetten oder kleine Doppel (je 2,5 × 2,0m)
  Gemeinsames Bad

MASTER-SUITE (Mitte oder Aft):
  Große Doppel (4,0 × 2,5m)
  Privates Badezimmer + Ankleidezimmer (optional)
  
GALLEY + SALON (Mitte):
  Zentrale Funktions-Zone

CREW/UTILITIES (Aft):
  Kleine Kabine (2,0 × 1,8m) oder Kojen
  
TOTAL: 8–10 Schlafplätze, Charterboot-Standard
```

### 2.3 2-Kabinen "Apartment" (Segelboot 10–12m, minimalist)

**Anordnung:**

```
VORN: V-Bett (2–3 Personen)
ACHT: Doppel-Kabine (2 Personen)
MITTEL: Kombination Galley/Salon/Nav
TOTAL: 4–5 Schlafplätze

Vorteil: maximale Gemeinsame Bereiche, flexibel
Nachteil: weniger Privatsphäre für längere Reisen
```

---

## 3. Galley (Küche) Design und Ergonomie

### 3.1 Galley-Grundformen

**Straight (Ein-Seite):**

```
Layout:
  - Arbeitsfläche: 600–800 mm lang, 600 mm breit
  - Herd: 2 Brenner (Standard) oder 1 Brenner (minimalist)
  - Kühlschrank: darunter oder separat
  - Stauraumsystem: über Arbeitsfläche + unter
  
Vorteil: kompakt, einfach
Nachteil: begrenzte Arbeits-Kapazität für mehrere Köche
```

**Corridor (beide Seiten):**

```
Layout:
  - Arbeitsfläche beide Seiten: 400 mm Breite
  - Herd eine Seite, Spüle andere
  - Kühlschrank: unter Arbeitsfläche
  
Vorteil: bessere Arbeitsfluss-Logistik
Nachteil: enger Durchgang (600–700 mm zentral)
```

**L-förmig (Ecke):**

```
Layout:
  - Arbeitsflächen an zwei Seiten, rechtwinklig angeordnet
  - Spüle am "inneren Eck", Herd seitlich
  
Vorteil: Bewegungs-Effizienz (3-Punkt Arbeit-Dreieck)
Nachteil: komplexere Installationen
```

### 3.2 Galley-Ausstattungs-Details

**Arbeitsfläche-Höhe:**

```
Standard: 850–900 mm über Schiffsdeck
  (vs. Land 850–950 mm; Marine leicht tiefer für Sitzposition)
  
Unter Seegang:
  Crew arbeitet oft sitzend (sicherer)
  → Arbeitsfläche 700–750 mm mit Hocker sicherer
```

**Herd (Stove) Sicherheit:**

```
Größe: 2–3 Brenner (Standard) oder 1–2 (minimalist)
Gimbal-Aufhängung: ja (erlaubt Tilting mit Boot-Heel)
Sicherheits-Drähte: um Töpfe (verhindert Rutsch bei >30° Heel)
Windschutz: 150–200 mm Rand (verhindert Brennstoff-Überslosh)

Brennstoff-Typ:
  Propan (LPG): typisch, Speicher 10–20 kg
  Benzin: selten (Feuergefahr)
  Diesel: nur bei großer Yacht mit Zentralheizung
  Elektrisch: immer häufiger (Batterie-Boot)
```

**Spüle (Sink) Dimensionierung:**

```
Größe: 350 × 350 mm Standard (2-Kammer optional)
Wasserversorgung: Süßwasser (Frischwasser) + optional Salzwasser
Ablauf: in Lenz-Brunnensystem, oder separater Ablauf
Material: Edelstahl oder Kunststoff-Composite

Wasserbilanz (Cruising):
  Frischwasser-Tank: 50–100 L (abhängig Besatzung)
  Verbrauch: 20 L/Tag (Kochen + Trinken), + Dusche 30 L
  → 4–5 Tage ohne Nachfüllen (typisch)
```

**Kühlschrank (Fridge) Größe:**

```
Kleine Yacht (8–10m): 60–80 L
Mittel-Boot (12–16m): 100–150 L
Große Yacht (18m+): 200+ L (oft zwei Einheiten)

Kühl-Quelle:
  Motorische Kühlung (Via Lenz-Wasser): Standard auf Motorboot
  Kompressor (12/24V DC): Standard auf Segelboot (nur unter Motor)
  Kerosin-Läufer: selten (Platz, komplexe Installation)
  Lithium-Batterie: wachsend (Solar-Segelboot)
```

### 3.3 Galley unter Seegang

**Sicherheits-Vorkehrungen:**

```
1. Gimbals (Aufhängung für Herd):
   Erlaubt ±30–35° Neigung (folgt Boot-Heel)
   Mechanisches Limit: verhindert Überumkippen
   Wartung: Schmierung alle 6 Monate

2. Sicherheits-Drähte:
   Um Herd + Spüle (verhindert Verschiebung)
   Länge variabel (+ Heel bis 30°)
   Material: Edelstahl-Kabel Ø 3 mm

3. Stopper-Leisten (Fiddle Rails):
   Auf Arbeitsfläche (100–150 mm hoch)
   Verhindern Gegenstände-Rutsch
   Material: Holz oder Aluminium-Profil

4. Sicherheits-Gurt für Köchin:
   Optional, für lange Seereisen (beeinträchtigt aber Bewegung)
   Material: Marine-Nylon mit Klettaug
   Position: quer über Galley, fixierbar an Schränken
```

**Kochlern-Training:**

```
Anforderung: Alle Crew sollten Galley-Grundlagen kennen
Besonderheiten:
  - Kleinere Mengen kochen (weniger Hitze-Erzeugung)
  - Eintöpfe/Pfannen bevorzugt (sicherer als mehrere Behälter)
  - Kochzeit: länger (Boot-Bewegung, Herd-Kontrolle schwächer)
  - Mentales Vorbereitung: Sicherheit vor Komfort
```

---

## 4. Navigations-Station und Arbeits-Bereiche

### 4.1 Navigations-Platz (Nav-Station)

**Standort-Optionen:**

| Option | Vorteil | Nachteil |
|--------|--------|----------|
| Im Saloon | Zentral, Kontakt Crew | Ablenkung, Geräusch |
| Separate Kabine | Ruhe, Konzentration | Isoliert, Sichtlinie begrenzt |
| In Cockpit (Motor-Yacht) | Sichtlinie optimal | Wetter-exponiert |
| Unter Deck (gut gewählt) | Geschützt, Charts zugänglich | Sichtlinie eingeschränkt |

**Schreibtisch-Layout (typisch):**

```
Oberfläche: 600 × 800 mm (minimal), 800 × 1000 mm (komfortabel)
Höhe: 750–800 mm (Sitzen mit Hocker)
Neigung: 5–10° (Chart-Lesbarkeit)
Material: Teak oder Kunststoff (Wasser-Resistenz)

Ausstattung:
  - Chart-Rollen + Speicher: seitlich oder unten
  - Bildschirm-Halter: flexibel (GPS/Radar)
  - Papier-Chartkiste: für Backup-Navigation
  - Schublade: Stifte, Zirkel, Lineal, Notizen
  - Instrumenten-Ablage: Kompass, Binokulare
```

**Beleuchtung:**

```
Hauptleuchte: 500 Lux (White, Reading)
Rotlicht: 50 Lux (Radar-Lesbarkeit, keine Blendung)
Position: direkt über Chart (nicht seitlich = Schatten)
Batterien: unabhängig (nicht durch Hauptschalter)
```

### 4.2 Saloon und Esstisch

**Saloon-Layout:**

```
Größe: 4–5m Länge × 2,2m Breite × 1,9m Kopffreiheit
Tisch: 1,0 × 0,8m (6-Personen-Einstellung möglich)
Bänke: beide Seiten, verstellbar oder fix
Zusätz-Sitze: ggf. auf Deck-Stühle (transportabel)

Fenster/Bullaugen:
  Mindestens 2 für Sichtlinie
  UV-Schutz (Folie oder Jalousien)
  Notfall-Fenster (400×520 mm): neben Esstisch, leicht zu öffnen
```

**Tisch-Ausführung:**

```
Statisch (fest):
  Vorteile: stabil, große Fläche
  Nachteile: Raum begrenzt (darunter Speicher möglich)
  
Drehbar (mit Getriebe):
  Vorteile: flexibel für Seating-Arrangement
  Nachteile: mechanische Komplexität
  
Klapp-Tisch:
  Vorteile: kompakt, speichert Platz
  Nachteile: Instabilität unter Seegang
  
Hybrid (verschiebbar-höhenverstellbar):
  Standard auf modernen Yachten (motorisch betätigt)
```

**Gewichts-Verteilung:**

```
Saloon-Einrichtung wiegt typisch: 800–1200 kg
  Bänke: 300 kg
  Tisch: 100–150 kg
  Schränke/Speicher: 400–600 kg
  
Effekt auf Boot-Trimm:
  Mittelschiffs-Position: minimal (ideal)
  Vorschiff zu hoch: Bug-up-Effekt (nicht erwünscht)
  Achterschiff zu hoch: Bug-down (schlechter Seegans-Verhalten)
  
Kontrolle: CG-Rechnung, Trimm-Überprüfung nach Bestückung
```

---

## 5. Schlafkabinen und Bettausstattung

### 5.1 V-Bett (Vorbug-Konfiguration)

**Dimensionierung und Form:**

```
Länge: 1,9–2,1m (Fußraum variabel)
Breite-Nase (vorne): 2,0–2,3m
Breite-Stern (hinten): 1,0–1,2m
V-Winkel: 30–45° (abhängig Rumpf-Form)

Positionen bei Seegang:
  Längs-Bewegung: Schiff nickt → V-Bett bewegt sich
  Quer-Bewegung: Heel ≥ 15° → Kopf-Position nicht ideal
  Solution: Keil-Kissen adjustierbar (folgt Boot-Neigung)
```

**Lüftung des V-Bettes:**

```
Kritisch: Luft-Stagnation unter Bett (Feuchtigkeit-Ansammlung)
Lösung:
  - 2 Bullaugen (Bug-seiten-Fenster)
  - 1 Oberlicht + Konvektor-Kamin
  - Optional: 12V-Lüfter (unter Bett, diskret)
  
Effekt: 6–8 ACH (Air Changes per Hour) = komfortabel
```

**Stauraum unter V-Bett:**

```
Typischerweise: Lagerung für Segel, Tauwerk, Proviant
Organisation:
  - Schubladen oder Plastik-Boxen (Modularität)
  - Vakuum-Taschen (Kleidung-Speicher)
  - Kleine Behälter (keine Rutsch-Gegenstände unter Seegang!)
  
Gewichts-Grenze: 150 kg (strukturell sicher für Unter-Bett-Last)
```

### 5.2 Aft-Cabins (Master + Guest)

**Master-Suite (große Yacht):**

```
Größe: 4,0–5,0m Länge × 2,5–3,0m Breite
Bett: König-Größe (180 × 200 cm) oder zwei Königinnen (90 × 200 cm je)
Badezimmer: angeschlossen (privat)
Ankleidezimmer: optional (große Yacht)
Fenster: mehrere Bullaugen + Seitenfenster (Sichtlinie)

Armatur:
  Läufer-Schränke: hohe Speicherkapazität
  Nachttische: klappbar (Platz-Spar)
  Leselampen: einzeln (Partner-Rücksicht)
```

**Gäste-Kabine:**

```
Größe: 2,5–3,5m Länge × 2,0–2,5m Breite
Bett: Doppel (160 × 190 cm) oder zwei Einzelne
Fenster: mindestens ein Bullaluge
Stauraum: kleine Schränke (Gast-Habseligkeiten)
WC-Zugang: direkt oder über Korridor
```

### 5.3 Beheizung und Temperatur-Kontrolle

**Motoryacht-Standard:**

```
System: Diesel-Heizung (zentrales Heizsystem)
Fuel-Verbrauch: 2–4 L/Tag (moderate Temperatur halten)
Wärmeverteiling: Rohre zu Kabinen, Radiator oder Gebläse
Thermostat: zentral (alle Kabinen gleichzeitig)

Nachteil: teure Installation, wartungsaufwändig
```

**Segelboot-Budget (Standard):**

```
System: Diesel-Heizung klein (portabel, 3–5 kW)
Alternative: Holz-Ofen (traditionell, ineffizient)
Modern: 12V AC-Wärmepumpe (mit Batterie-System)

Temperatur-Halten:
  Ohne Heizung: 5–15°C in Kabinen (Winter)
  Mit Heizung: 15–18°C komfortable Range
  Problem: Kondensation (kalte Decke → Tropfen)
  Solution: Entfeuchter oder Hygrostat-Lüfter
```

---

## 6. Kopf (WC) und Sanitär-Bereich

### 6.1 Kopf-Dimensionierung

**Minimale Größe:**

```
Länge: 1,2–1,5m
Breite: 0,8–1,0m
Kopffreiheit: 1,6–1,8m
Oberfläche: ca. 1,0–1,5 m²

Ausstattung:
  - Toilette (marino-Modell)
  - Waschbecken/Sink
  - Spiegel
  - Duschtasse (optional, wenn Platz vorhanden)
  - Belüftungs-Auslass (Lüfter-Auslass, nicht Einlass!)
```

**Material-Auswahl (Dusch/Wasch-Bereich):**

| Material | Vorteile | Nachteile | Kosten |
|----------|----------|----------|--------|
| Fliesen (Keramik) | rutschsicher, schimmel-resistent | Risse bei Vibrationen | Teuer |
| Kunststoff-Panel | leicht, wasserdicht | Kratzer, Verfärbung | Günstig |
| Epoxy-Beschichtung | glatt, modular | Slippery nass | Mittel |
| Teak (geplant) | ästhetisch | schnell faulendes Risiko | Teuer |

### 6.2 Toiletten-Systeme

**Pumpensystem (Standard auf Yacht):**

```
Funktionsweise:
  Benutzer betätigt Pumpenhebel (mechanisch)
  → Kolben-Pump spült Seewasser (oder Frischwasser)
  → Einwegventil verhindert Backflow
  → Abfallwasser in Tank (Holding Tank)
  
Tanks-Größe:
  Kleine Yacht (8–10m): 20–30 L
  Mittel-Boot (12–16m): 50–80 L
  Große Yacht (18m+): 100+ L
  
Entleerungs-Zyklus:
  Mit Pumpen-Toilette: 5–10 Tage (abhängig Besatzung-Größe)
  Abgabe: in Port-Pumpstation oder auf See (>3 Meilen von Küste)
```

**Vakuum-Toilette (moderne Yacht):**

```
Funktionsweise:
  Unterdruckanlage (Vakuum-Pumpe)
  → Niedrig-Druck-Sog (effizienter Spülvorgang)
  → Weniger Wasser-Verbrauch
  
Vorteile:
  - Minimal Wasser (1–2 L pro Spülung, vs. 5–10 L Pumpensystem)
  - Weniger Geruchsbelastigung
  - Größere Tank-Intervalle

Nachteile:
  - Komplexe Technik (Störanfälligkeit)
  - Höhere Kosten (EUR 3000–5000 Komplettsystem)
  - Strom-Abhängigkeit
```

**Kompost-Toilette (Öko-Option):**

```
Keine Wasser-/Tank-Nutzung
Funktionsweise: Feststoffe + Sägespäne → biologischer Abbau
Material: Holz-Körper, Kunststoff-Innen
Wartung: jährlich Kompost ausleeren (Garten-Verwendung)

Problem: Marineer-Regelungen (viele Häfen verbieten Kompost-Anlage)
Praxis: nur in entlegenen Revieren akzeptabel
```

### 6.3 Dusch-Systeme

**Frischwasser-Dusche (energieintensiv):**

```
Größe-Becken: 0,8 × 0,8m (Standard)
Wasser-Verbrauch: 20–30 L pro Dusche
Heizung: über Diesel-Heizanlage oder 12V-Durchlauferhitzer

Wassertemperatur:
  Ungeheizt (Salzwasser): 15–18°C (Nordatlantik)
  Mit Heizen: 35–40°C komfortabel (Energieverbrauch: 0,5–1 kWh)

Häufigkeit: 2–3× pro Woche (wegen Frischwasser-Knappheit)
Alternative: Salzwasser-Dusche + Süßwasser-Rinse (1–2 L)
```

**Dusch-Schirm und Entwässerung:**

```
Schirm: Kunststoff oder Canvas (ausziehbar)
Bodenfläche: muss zur Lenz-Brunnen entwässern
Pumpe: Bilgen-Pumpe (integriert, automatisch bei Füll-Level)

Größe Ablauf:
  Standard 40 mm Rohr + Schieberventil
  Drainages-Kapazität: mindestens 50 L/Dusche (Reserve)
```

---

## 7. Lüftungs- und Klima-Kontrolle

### 7.1 Natürliche Belüftung

**Bullaugen und Luken:**

```
Anzahl: mindestens 3–4 pro Yacht (8–12m)
Größe: 400 × 300 mm (Standard)
Position: durchgehend (Bug bis Heck) für Querlüftung

Effekt ohne Motor:
  Natürliche Konvektion: 2–4 ACH (Air Changes per Hour)
  Ausreichend für: Parken, ruhige See
  Nicht ausreichend für: Aktives Segelfahren (Feuchtigkeit-Stau)
```

**Luft-Strömung-Muster:**

```
Idealfall (Bug-Wind):
  Luft-Zirkulation: Bug-Bullaloge (Eintritt) → Aft-Bullaloge (Ausgang)
  Geschwindigkeit: 0,5–1,5 m/s (angenehm)

Problem-Fall (Seite-Wind oder Flaute):
  Luft-Stagnation: keine natürliche Konvektion
  Feuchtigkeit-Ansammlung: 24+ Stunden → Schimmel-Risiko
  Solution: mechanische Lüfter (siehe unten)
```

### 7.2 Mechanische Lüftung

**12V-Lüfter (Segelboot-Standard):**

```
Leistung: 50–200 m³/h (je nach Modell)
Stromverbrauch: 2–10A @ 12V (minimal)
Installation: durch Wand oder Decke-Durchgänge
Kontrolle: Schalter oder Automatik (Hygrostat)

Anzahl: 2–3 Lüfter (strategische Positionen)
  - Kabinen: ein Absauger (Feuchteausleitung)
  - Saloon: ein Eintritt + ein Ausgang (Zirkulation)
  - Kopf: Absauger (Geruchskontrolle)

Wartung:
  Filter reinigen: monatlich (Salzwasser-Corrosion)
  Lager schmieren: jährlich
  Austausch: 8–10 Jahre (Motoren-Verschleiß)
```

**Diesel-Heizer mit Gebläse (Motor-Yacht):**

```
Zentrale Wärme-Quelle: 5–15 kW Diesel-Heizer
Wärmeverteiler: Rohre zu Kabinen, mit Gebläse
Temperatur-Regelung: Thermostat (zentral oder zoniert)
Luftzirkulation-Effekt: 100–300 m³/h (abhängig Kanal-Größe)

Vorteil: kombinierte Heizung + Lüftung
Nachteil: komplexe Installation, Wartungsaufwand
```

### 7.3 Kondenswasser-Vermeidung

**Problem-Analyse:**

```
Ursache: Temperatur-Unterschied innen/außen
  Außen (Winter): 5–10°C
  Innen (Schlafraum): 15–18°C
  Taupunkt: ca. 8–10°C

Wenn Deck-Oberfläche <8°C:
  Luft-Feuchte kondensiert → Wassertropfen
  
Symptom: morgens nasses Bett, muffiger Geruch
```

**Mitigation:**

```
1. Belüftungs-Zyklus:
   5 Minuten pro Stunde (automatisch mit Timer)
   → kontinuierliche Feuchte-Ausleitung

2. Temperatur-Management:
   minimales Heizen: 12–15°C (reduziert Taupunkt-Differenz)
   Zonen-Heizung: Schlaf-Zonen >14°C

3. Material-Auswahl:
   Holz-Verkleidung: hydroscopisch (absorbiert Feuchte)
   Kunststoff-Verkleidung: hydrophob (reflektiert, aber kann Stau)
   Optimal: Holz + Belüftung kombiniert

4. Feuchte-Absorbent:
   Kieselsäure-Gel-Pakete: in Schränken (ca. EUR 5 pro Paket)
   Entfeuchter (elektrisch): 50 Watt, 0,5 L/Tag Kapazität
```

---

## 8. Akustik und Lärm-Isolierung

### 8.1 Lärm-Quellen und Regelwerk

**Typische Geräusch-Pegel im Innenraum:**

| Quelle | Pegel [dB] | Frequenz | Problem |
|--------|-----------|----------|---------|
| Diesel-Motor | 75–85 | 1000–2000 Hz | niedrig-frq. Rummel |
| Segelwind | 65–75 | breitbanding | persistente Heuleien |
| Wellen-Schlag | 70–80 | 500–1000 Hz | Schlag-Lärm |
| Genua/Boom-Schlag | 80–90 | impulsiv | Sicherheits-Alarm |

**ISO 12217-3 (Lärm-Limits):**

> ⚠️ **ZU PRÜFEN (Audit):** Normbezug falsch — ISO 12217-3 regelt *Stabilität und Auftrieb von Booten < 6 m Rumpflänge*, NICHT Innenraum-Lärmgrenzen (und passt auch nicht zur Dokument-Bootsgröße 8–40 m). Die folgenden dB-Grenzwerte haben keinen gültigen Normbezug → estimated — unverifiziert. Quelle: ISO 12217-3:2015 / :2022 (iso.org/standard/68142.html).

```
Schlaf-Bereich: <70 dB (Continuous)
Wohn-Bereich: <75 dB (Continuous)
Küche: <80 dB (Continuous)
Unter Motor: 80–85 dB (akzeptabel, mit Schutzausrüstung)
```

### 8.2 Isolierungs-Material

**Schalldämpfungs-Materialien:**

| Material | Absorption @ 500 Hz | Dicke [mm] | Gewicht [kg/m²] | Kosten |
|----------|-------------------|-----------|----------|--------|
| Closed-Cell Foam | 0,5–0,7 | 25–50 | 2–4 | EUR 30/m² |
| Mineral-Wolle | 0,7–0,9 | 50–100 | 8–12 | EUR 50/m² |
| Melamin-Schaum | 0,8–0,95 | 30–50 | 2–3 | EUR 80/m² |
| Teak-Verkleidung | 0,3–0,5 | 6–10 | 3–5 | EUR 150/m² |

**Installation-Strategie (Lärm-Reduktion):**

```
1. Motor-Raum Isolierung:
   - Alle Wände/Decke mit Mineral-Wolle (100 mm)
   - elastische Entkopplung (Vibrations-Isolatoren)
   - Resultat: 15–20 dB Reduktion

2. Kabinen-Isolierung:
   - Geschlossene Türen (wichtig!)
   - Verkleidung + Foam hinter Panel (50 mm)
   - Resultat: 10–15 dB Reduktion

3. Lüftungs-Geräusch:
   - Schall-Dämpfer in Luftkanälen
   - Gummi-Halter für Lüfter (entkoppelt Vibration)
   - Resultat: 8–12 dB Reduktion
```

**Praktische Reduzierung unter Motor:**

```
Ohne Isolierung: 85 dB
Mit Tür geschlossen: 80 dB (5 dB)
Mit Motor-Isolierung: 75 dB (10 dB)
Mit zusätzlich Kabinen-Foam: 72 dB (13 dB insgesamt)
→ Annehmbar für Seegänge <200 nm
```

---

## 9. Möbel-Design für Heel und Seegang

### 9.1 Anti-Rutsch-Techniken

**Möbel-Befestigung:**

```
Standard: Bolzenschrauben + Feder-Unterlegscheiben
Anzahl: mindestens 4 pro Möbelstück (große Möbel 6–8)
Position: an Eckpunkten (maximal entfernt) für Drehmoment-Verteilung

Unter 30° Heel:
  Schwerpunkt-Verschiebung: ΔX = h × tan(θ)
  Beispiel: Tisch 0,8m hoch, 30° Heel
  ΔX = 0,8 × tan(30°) = 0,46m (ca. 500 mm seitliche Verschiebung)
  → Möbel braucht min. 500 mm "Griff-Nähe" zur Reling
```

**Material unter Polstermöbel:**

```
Kunststoff-Gleiter: nein (zu rutschig)
Filz-Pads: leicht (20–50 grammm), gutes Haften
Gummi-Noppen: besser (100–200 g), hohe Reibung
Kleber: nicht permanent (braucht Demontierbarkeit)

Effekt-Koeffizient:
  Standard-Filz: µ ≈ 0,3 (Platz 30% Heel möglich)
  Gummi-Noppen: µ ≈ 0,6 (Platz 60% Heel möglich)
  Moderne Hybrid: µ ≈ 0,7 (ideal)
```

### 9.2 Bett-Konstruktion bei Heel

**V-Bett und Heel-Kompensation:**

```
Problem: Unter 20° Heel wird Bett schräg
Lösung 1: Keil-Kissen (konfigurierbar, 10–20 cm Dicke)
Lösung 2: höhenverstellbare Bett-Basis (teuer, komplexe Mechanik)
Lösung 3: mentale Anpassung (Crew akzeptiert Schräglage)

Praktisch: Standard + Keil-Kissen + gutes Bett-Netz (verhindert Abrutschen)
```

**Netz und Sicherung:**

```
Material: Nylon oder Baumwolle (nicht Kunststoff-Netz = rutschig)
Befestigung: an Boot-Struktur (nicht am Bett selbst)
Höhe: 300–400 mm (hält Person auch bei 45° Heel)
Spannung: modulierbar (für verschiedene Heel-Winkel)
```

---

## 10. Evakuierungs-Routen und Notfall-Zugänglichkeit

### 10.1 Escape-Route-Planung

**Primär-Route:**

```
Vom Schlafplatz zur Tür/Luke:
  Länge: max. 5m (2–3 Minuten schnelle Bewegung)
  Breite: min. 40 cm (eng, aber passierbar unter Rauch)
  Hindernisse: keine Treppen oder Sperren
```

**Sekundär-Route (Notfall):**

```
Vom Schlafplatz zu Notfall-Fenster:
  Fenster-Größe: 400 × 520 mm (ISO 12216)
  Höhe über Deck: <1200 mm (erreichbar von liegend)
  Hebel-Mechanismus: einfach, keine Werkzeuge
```

### 10.2 Beleuchtung und Markierung

**Not-Beleuchtung:**

```
Standard nach ISO: photoluminescent Streifen (glow-in-dark)
Position: entlang Flucht-Pfad (alle 500 mm)
Helligkeit: ausreichend für Orientierung im Dunkeln
Batterie-Backup: nicht erforderlich (passive Lumineszenz)
```

**Türen und Verschlüsse:**

```
Kabinen-Türen: nach außen öffnend (nicht schwingend unter Seegang)
Locking-Mechanismus: manuell, ohne Elektrik (für Notfall)
Markierung: deutlich sichtbar (Bild + Text auf Deutsch + English)
```

---

## ANHANG A — Glossar

**Aft-Cabin:** Hintere Schlafkabine (näher zum Heck).

**Bullaloge:** Rundes Fenster, auf Seite oder Bug.

**Cockpit-Sole:** Fußboden des Cockpits.

**Corridor:** schmaler Durchgang (auch "Gangway").

**Frischwasser-Tank:** Lager für Trinkwasser (~50–100 L).

**Gimbal:** Aufhängung, erlaubt Neigung in zwei Richtungen.

**Holding-Tank:** Abwasser-Speicher (für Kopf).

**Hygrostat:** Sensor für Feuchte, triggert Lüfter automatisch.

**Master-Suite:** Größte Schlafkabine mit privatem Bad (Captain's Cabin).

**Saloon:** Gemeinsamer Wohnraum (Ess- + Wohnbereich).

**Schott:** Wand/Trennwand im Schiff.

**V-Bett:** V-förmiges Doppelbett im Bug (wegen Rumpf-Form).

---

## ANHANG B — Pydantic v2 Validierungs-Modell

```python
from pydantic import BaseModel, Field
from typing import Optional, List

class InterieurLayoutFehlerbild(BaseModel):
    """
    Fehlerbild für Interieur-Layout nach AYDI-Standard.
    12 spezifische Fehlerbilder mit Schweregrad, Ort, Lösungsweg.
    """
    model_config = {"from_attributes": True}

    # Metadaten
    fehlerbild_id: str = Field(..., description="Eindeutige ID, z.B. '31_11_001'")
    kategorie: str = "31_Design_Konstruktion"
    unterkategorie: str = "Interieur_Layout"
    
    # Fehler-Beschreibung
    titel: str = Field(..., description="Kurztitel des Fehlerbilds")
    beschreibung: str = Field(..., description="Detaillierte Fehler-Charakterisierung")
    
    # Symptome und Auswirkungen
    symptome: List[str] = Field(default_factory=list, description="Beobachtbare Zeichen")
    auswirkungen: List[str] = Field(default_factory=list, description="Folgen für Betrieb/Sicherheit")
    
    # Schweregrad
    schweregrad: str = Field(..., description="'kritisch', 'hoch', 'mittel', 'niedrig'")
    sicherheits_impact: bool = Field(default=False, description="Sicherheits-Relevanz")
    
    # Ursprung
    boots_typen: List[str] = Field(default_factory=list, description="Relevante Boot-Klassen")
    interieur_zone: str = Field(default="", description="Kabine/Galley/Kopf/Saloon/etc")
    
    # Diagnose und Reparatur
    diagnose_methoden: List[str] = Field(default_factory=list, description="Wie identifizieren?")
    reparatur_optionen: List[str] = Field(default_factory=list, description="Lösungsansätze")
    schaetzung_kosten_eur: Optional[float] = Field(None, description="Grobe Reparatur-Kosten")
    dauer_tage: Optional[int] = Field(None, description="Reparatur-Dauer in Tagen")
    
    # Prävention
    praevention: List[str] = Field(default_factory=list, description="Wie vermeiden?")
    inspektions_intervall_jahre: Optional[float] = Field(None, description="Wartungs-Zyklus")
    
    # Verweise
    normen_referenzen: List[str] = Field(default_factory=list, description="ISO Standards")
    verwandte_fehlerbilder: List[str] = Field(default_factory=list, description="Andere Fehler-IDs")


# Beispiel-Instanz
fehlerbild_001 = InterieurLayoutFehlerbild(
    fehlerbild_id="31_11_001",
    titel="Galley-Herd rutschig unter Seegang",
    beschreibung="Gimbal-Aufhängung schwach oder Töpfe nicht ausreichend gesichert.",
    symptome=[
        "Herd neigt nicht mit Boot-Heel",
        "Töpfe rutsche während Kochens",
        "Verbrennungsrisiko"
    ],
    auswirkungen=[
        "Sicherheits-Risiko für Köchin",
        "Lebensmittel-Verschätzung",
        "Verbrühungs-Gefahr"
    ],
    schweregrad="hoch",
    sicherheits_impact=True,
    boots_typen=["Segelboot", "Motorsegler"],
    interieur_zone="Galley",
    diagnose_methoden=[
        "Visueller Check: Gimbal-Funktion prüfen",
        "Test: 20° Heel simulieren, Herd neigt?",
        "Sicherheits-Draht-Spannung prüfen"
    ],
    reparatur_optionen=[
        "Gimbal-Lager überprüfen und ggf. austauschen",
        "Sicherheits-Drähte nachspannen",
        "Töpfe-Set mit besserer Griffigkeit"
    ],
    schaetzung_kosten_eur=1500,
    dauer_tage=2,
    praevention=[
        "Gimbal-System jährlich prüfen",
        "Sicherheits-Drähte vor Saison inspizieren",
        "Crew-Training für Galley-Sicherheit"
    ],
    inspektions_intervall_jahre=1,
    normen_referenzen=["ISO 12217-2", "CE Sicherheits-Richtlinie"],
    verwandte_fehlerbilder=["31_11_003", "31_11_006"]
)
```

---

## ANHANG C — FAQ (25+)

**F1: Wie groß sollte eine Galley sein?**
A: Minimal 1,5 × 1,5m; komfortabel 2m × 1,8m. Größer = bessere Arbeitseffizienz, aber weniger Saloon-Platz.

**F2: Wieviel Frischwasser ist genug?**
A: Regel: 1 L pro Tag pro Person (Trinken), +20 L pro Dusche. Für 4 Personen: 50–100 L für 3–5 Tage.

**F3: V-Bett oder zwei Single-Kojen?**
A: V-Bett: flexibler (Paar), Single: besser bei Seegang (individuelle Gewöhnung). Hybrid: V-Bett + Pull-out Single unten.

**F4: Welche Lüftungs-Rate ist ausreichend?**
A: Minimum 2–4 ACH (Air Changes per Hour) = gesundes Innenklima. Mit Lüftern: 8–12 ACH möglich.

**F5: Ist Schimmel in Kabine vermeidbar?**
A: Ja, mit kontinuierlicher Belüftung + Temperatur >12°C + Feuchte <70%. Ohne Motor: schwierig.

**F6: Wie oft sollte die Kopf (WC) entleert werden?**
A: Bei 4 Personen: alle 5–10 Tage (abhängig Tank-Größe). Standard: 50 L Tank = 7–10 Tage.

**F7: Können zwei Personen gleichzeitig duschen?**
A: Nein (separat WC/Dusch-Bereiche selten). Nacheinander, mit 20–30 L Wasser pro Dusche.

**F8: Ist ein Navigations-Monitor unter Seegang nutzbar?**
A: Ja, aber mit Gimbal-Halterung. Ohne: sehr schwierig (Schrift springt).

**F9: Welche Tisch-Form ist am stabilsten?**
A: Niedriger Schwerpunkt + breite Basis. Fest-montiert > drehbar > klappbar (Stabilitäts-Reihenfolge).

**F10: Wie viel Stauraum braucht man auf Langfahrt?**
A: Regel: 20–30 kg Proviant + Kleidung + Ersatzteile = ~0,5–1,0 m³. Moderne Yachten bieten 1,5–3 m³.

---

## 11. Normativer Rahmen (verifiziert) — Korrektur der Norm-Zuordnung

> **Audit-Hinweis:** Die in Abschnitt 1.2, 1.3 und 8.1 zitierten Normbezüge (ISO 12217-2/-3 für Kabinenmaße, Durchgangsbreiten, Lärmgrenzen) sind **falsch** und dort bereits als „estimated — unverifiziert" markiert. Dieser Abschnitt stellt die **tatsächlich einschlägigen** Normen zusammen — jede web-verifiziert. Wichtig: **Für Kabinen-Innenmaße, Kojenmaße, Durchgangsbreiten und Innenraum-Lärmpegel existiert keine bindende ISO-Norm.** Diese Werte sind Konstruktions-Konventionen/Werftpraxis (Confidence: `estimated`), nicht normativ.

### 11.1 Einschlägige Normen (was regelt wirklich was)

| Norm | Titel / Gegenstand | Layout-Relevanz | Geltungsbereich | Confidence |
|------|-------------------|-----------------|-----------------|------------|
| **ISO 12216:2020** | Small craft — Windows, portlights, hatches, deadlights and doors — Strength and watertightness requirements | **Notausstiege / Fluchtluken** (Festigkeit, Wasserdichtheit, lichte Öffnung); Fenster/Türen/Luken | Rumpflänge bis 24 m | `documented` |
| **ISO 12217-2:2022** | Stability and buoyancy assessment — Part 2: Sailing boats ≥ 6 m | Gewichts-/CG-Verteilung; **für bewohnbare Mehrrümpfe: Bewertung der Kenterneigung, Definition „viable means of escape", Anforderungen an Schwimmlage nach Kenterung** | Segelboote 6–24 m | `documented` |
| **ISO 9094:2022** | Small craft — Fire protection | **Fluchtwege im Brandfall** (genug Zeit zum Verlassen), Abstände, Löschausrüstung | Rumpflänge bis 24 m (außer PWC) | `documented` |
| **ISO 11812:2020** | Watertight or quick-draining recesses and cockpits | **Süllhöhen (sill heights)**, Wasserdichtheit, Entwässerungszeit (nur Schwerkraft-Drainage) | bis 24 m Ladelinienlänge | `documented` |
| **RCD 2013/53/EU, Anhang I** | Recreational Craft Directive, wesentliche Anforderungen | §3.8 „Escape"; §5.1.2 Lüftung Motorraum; §5.5 Gasanlage-Lüftung; §5.6 Brandschutz | Sportboote 2,5–24 m (EU-Verkauf) | `documented` |

Quellen: ISO 12216:2020 [iso.org/standard/69553.html](https://www.iso.org/standard/69553.html); ISO 12217-2:2022 [iso.org/standard/79073.html](https://www.iso.org/standard/79073.html); ISO 9094:2022 [iso.org/standard/78242.html](https://www.iso.org/standard/78242.html); ISO 11812:2020 [iso.org/standard/67204.html](https://www.iso.org/standard/67204.html); RCD Anhang I [legislation.gov.uk/eudr/2013/53/annex/I](https://www.legislation.gov.uk/eudr/2013/53/annex/I).

### 11.2 Notausstieg / Fluchtluke — verifizierte Anforderungen

**RCD 2013/53/EU, Anhang I, §3.8 „Escape" (verifiziert, Wortlaut sinngemäß):**
- „Every habitable recreational craft shall be provided with viable means of escape in the event of fire." — Jedes bewohnbare Sportboot muss über einen brauchbaren Fluchtweg im **Brandfall** verfügen.
- „All habitable multihull recreational craft susceptible of inversion shall be provided with viable means of escape in the event of inversion." — Bewohnbare, kenterungsanfällige **Mehrrümpfe** brauchen zusätzlich einen Fluchtweg im **Kenterfall**; ein solcher Fluchtweg darf Struktur, Stabilität und Auftrieb weder aufrecht noch gekentert beeinträchtigen.
> Quelle: RCD Anhang I §3.8 [legislation.gov.uk/eudr/2013/53/annex/I](https://www.legislation.gov.uk/eudr/2013/53/annex/I) — Confidence `documented`.

**Lichte Öffnung Mehrrumpf-Fluchtluke (ISO 12216):**
- Für Mehrrümpfe (erstmals in Verkehr ab Januar 2003): **minimaler Durchlass-Durchmesser 450 mm** durch jede Fluchtluke; bei nicht-kreisförmiger Luke ausreichende lichte Weite, damit ein Crewmitglied vollständig hindurchpasst. Je eine Fluchtluke pro Rumpf, unterhalb Deckslinie an Rumpfseite, Nacelle-/Crossarm-Unterseite oder Spiegel (Position so, dass aufrecht **und** gekentert nicht dauernd unter Wasser).
> Quelle: Herstellerangabe Rutgerson Marin unter Bezug auf ISO 12216 [rutgerson.se/escape-hatch](https://www.rutgerson.se/escape-hatch/) — Confidence `documented` (Herstellerinterpretation; exakter Normtext ISO 12216:2020 kostenpflichtig).

> ⚠️ **ZU PRÜFEN (Audit):** Der im Dokument (Abschnitt 4.2 / 10.1) mehrfach genannte Wert **„400 × 520 mm"** für den Notausstieg lässt sich in freien Quellen **nicht** gegen den ISO-12216-Normtext belegen. Verifiziert ist nur der Mehrrumpf-Fluchtluken-Durchlass **Ø 450 mm** (bzw. äquivalente lichte Weite). Der Wert 400 × 520 mm bleibt bis zur Prüfung am Normtext `estimated — unverifiziert`. Exakte Öffnungsmaße/Prüfdrücke stehen ausschließlich im kostenpflichtigen ISO-12216:2020-Normtext und wurden **nicht** rekonstruiert.

**Wichtige Abgrenzung (verifiziert):**
- ISO 12216 = **Festigkeit + Wasserdichtheit + lichte Öffnung** der Luke selbst.
- ISO 12217-2 = **ob** ein Mehrrumpf kenterungsanfällig ist und **dass** ein „viable means of escape" definiert sein muss (Bewertungsmethodik + Schwimmlage nach Kenterung), nicht die Luken-Konstruktion.
- ISO 9094 = Fluchtweg im **Brand**fall (Zeit zum Verlassen), nicht Kenterung.
> Quelle ISO 12217-2 Scope (Mehrrumpf-Kenterung, „viable means of escape", inverted flotation): [iso.org/standard/79073.html](https://www.iso.org/standard/79073.html) — `documented`.

### 11.3 Süllhöhen (Companionway-Sill) — Normbasis

Süllhöhen fallen unter **ISO 11812** (Wasserdichtheit/Süllhöhen von Cockpits/Recesses) sowie die CE-Design-Kategorie. Die AYDI-Plattform hinterlegt die CE-Mindest-Süllhöhen pro Kategorie im `compliance`-Modul (Cat A = 300 mm, B = 250 mm, C = 150 mm, D = 0 mm; ein boot-klassen-spezifischer Override darf nur **strenger** sein — `max(override, CE-Floor)`). Diese Kategoriewerte stammen aus der CLAUDE.md-Spezifikation des Projekts (Confidence `documented` bzgl. Projektspezifikation); der exakte Bemessungsweg (Drainagezeit, Sülltoleranzen) steht im kostenpflichtigen ISO-11812:2020-Normtext.
> Quelle Geltungsbereich ISO 11812 (Süllhöhen, nur Schwerkraft-Drainage, bis 24 m): [iso.org/standard/67204.html](https://www.iso.org/standard/67204.html) — `documented`.

### 11.4 Lüftung — Normbasis (Korrektur zu Abschnitt 7)

Die in Abschnitt 7 genannten ACH-Werte (Air Changes per Hour) und m³/h-Angaben sind **Erfahrungs-/Auslegungswerte** (`estimated`), keine ISO-Grenzwerte. Normativ bindend sind über die RCD nur **zweckgebundene** Lüftungsanforderungen:
- **Motorraum-Lüftung** (RCD Anhang I §5.1.2): „The engine compartment shall be ventilated." — der Motorraum muss belüftet sein; Wassereintritt ist zu minimieren.
- **Gasanlage** (RCD Anhang I §5.5): ausreichende Lüftung gegen Leckage-/Verbrennungsgefahren; Gasflaschen in einem nach außen entwässernden/belüfteten, von den Wohnräumen getrennten Kasten.
- **Batterie-Lüftung** (RCD Anhang I): Lüftung zur Verhinderung der Ansammlung explosiver Gase aus Batterien.
> Quelle: RCD Anhang I §5.1.2 / §5.5 [legislation.gov.uk/eudr/2013/53/annex/I](https://www.legislation.gov.uk/eudr/2013/53/annex/I) — `documented`. Die AYDI-Regel `Motorraum-Lüftung = max(0,05, engine_kw × 0,0003) m²` ist eine **projektinterne** Auslegungsformel (CLAUDE.md), kein ISO-Wert → `estimated`.

---

## 12. Fehlerbild-Atlas (FB-31-11-NNN)

> ID-Schema kollisionsfrei: `FB-31-11-NNN`. Die 12 Fehleranalyse-Schwerpunkte der Übersicht sind hier strukturiert ausgearbeitet. Sicherheitsrelevante Befunde tragen `sicherheits_impact = true`. Menschliche Prüfung („Befund prüfen") vor jeder KRITISCH-Meldung.

### FB-31-11-001 — Notausstieg/Fluchtweg unzureichend oder blockiert
- **Zone:** alle Schlafkabinen, Saloon | **Schweregrad:** kritisch | **Sicherheits-Impact:** ja
- **Fehlerbild:** Kein zweiter Fluchtweg aus einer Schlafkabine; Fluchtluke verstellt/festgeschraubt/zugewachsen; Mehrrumpf ohne Kenter-Fluchtluke.
- **Ursache:** Layout ohne Redundanz; Refit ohne Notausstieg; Deko/Stauraum vor Luke; Dichtungen verklebt.
- **Diagnose:** Fluchtweg-Begehung aus jeder Koje bei geschlossenen Türen; Luke im Dunkeln ohne Werkzeug öffnen; Mehrrumpf: Kenter-Fluchtluke je Rumpf vorhanden und funktionsfähig?
- **Abhilfe:** Zweiten Fluchtweg schaffen (Deckluke ISO 12216); Öffnungsmechanismus gängig halten; Freihaltezone markieren; Mehrrumpf-Fluchtluke Ø ≥ 450 mm nachrüsten.
- **Norm:** RCD Anhang I §3.8; ISO 12216 (Luke); ISO 9094 (Brand-Fluchtweg); ISO 12217-2 (Mehrrumpf-Kenterung). `documented`

### FB-31-11-002 — Kopffreiheit unzureichend
- **Zone:** Saloon, Durchgänge, über Kojen | **Schweregrad:** mittel | **Sicherheits-Impact:** ja (Kopfanstoß bei Seegang)
- **Fehlerbild:** Stehhöhe < Körpergröße der Crew; Kopfanstoßstellen an Schotten/Balken.
- **Ursache:** flaches Deckshaus; Bodenaufbau zu hoch; Refit-Verkleidung.
- **Diagnose:** Höhenmessung an allen Geh-/Arbeitsplätzen; Heel-Effekt beachten (effektive Höhe = nominal × cos θ — geometrisch korrekt, aber `estimated`, kein Normbezug).
- **Abhilfe:** Anstoßstellen polstern/markieren; Bodenaufbau reduzieren; Verkehrsführung umlenken.
- **Norm:** keine bindende ISO für Innen-Stehhöhe → `estimated`.

### FB-31-11-003 — Durchgang/Passage zu eng (Crew-Bewegung, Evakuierung)
- **Zone:** Hauptgang, Kabineneingänge | **Schweregrad:** hoch | **Sicherheits-Impact:** ja
- **Fehlerbild:** Passage behindert Bewegung mit Rettungsweste/Gepäck; Engstelle im Fluchtweg.
- **Ursache:** Möbel zu breit; nachträglicher Einbau; Griff-/Türschwenkbereich vergessen.
- **Diagnose:** Begehung mit angelegter Rettungsweste; Türschwenk-/Griffradien prüfen.
- **Abhilfe:** Engstelle entschärfen; Türen nach außen öffnend (siehe FB-31-11-012); Haltegriffe ergänzen.
- **Norm:** ISO 9094 (Fluchtweg frei); Breitenmaße selbst nicht normiert → `estimated`.

### FB-31-11-004 — Galley-Herd/Kochgeschirr nicht seegangssicher
- **Zone:** Galley | **Schweregrad:** hoch | **Sicherheits-Impact:** ja (Verbrühung/Brand)
- **Fehlerbild:** Gimbal blockiert/nicht vorhanden; keine Fiddle Rails/Topfsicherung; Sicherheitsgurt fehlt.
- **Ursache:** Wartungsmangel Gimbal-Lager; Serienausstattung ohne Sicherung.
- **Diagnose:** Gimbal von Hand durchschwenken; Fiddle-Rails/Topfhalter prüfen; Gasabsperrung erreichbar?
- **Abhilfe:** Gimbal-Lager schmieren/ersetzen; Fiddle Rails, Topf-Klammern, Koch-Sicherungsgurt nachrüsten.
- **Norm:** Brandschutz ISO 9094; Gas RCD §5.5. `documented` (Prinzip); Maße `estimated`.

### FB-31-11-005 — Gasanlage-Kasten nicht nach außen entwässernd/belüftet
- **Zone:** Galley/Gaskasten | **Schweregrad:** kritisch | **Sicherheits-Impact:** ja (Gasansammlung)
- **Fehlerbild:** LPG-Flaschen ohne separaten, nach außen entwässernden/belüfteten Kasten; Kasten zu Wohnraum offen.
- **Ursache:** unsachgemäßer Einbau; entfernte Trennung.
- **Diagnose:** Sichtprüfung Gaskasten: von außen zugänglich, zum Wohnraum dicht getrennt, Bodenentwässerung nach außenbords?
- **Abhilfe:** Normgerechten Gaskasten herstellen; Gaswarnsensor in Bilge/Bodenbereich (LPG ist schwerer als Luft).
- **Norm:** RCD Anhang I §5.5 (verifiziert). `documented`

### FB-31-11-006 — Nasszelle: Feuchte-/Geruchsausbreitung, mangelnde Trennung
- **Zone:** Kopf/WC/Dusche | **Schweregrad:** mittel | **Sicherheits-Impact:** nein
- **Fehlerbild:** Dusch-/Spritzwasser wandert in Wohnräume; Holzwerkstoffe ohne Versiegelung; Geruch aus Holding-Tank.
- **Ursache:** fehlende Süll/Türdichtung; ungefasste Holzkanten; Tank-Entlüftung falsch geführt.
- **Diagnose:** Feuchte-Migration prüfen; Holzwerkstoffe in Nasszone auf Versiegelung; Tank-Entlüftung außenbords?
- **Abhilfe:** Nasszellen-Abschottung; wasserfeste Materialien; Aktivkohlefilter Tankentlüftung.
- **Norm:** keine spezifische Innen-Norm → `estimated`; Materialwahl siehe Materialdokumente.

### FB-31-11-007 — Lüftung/Durchzug mangelhaft (Muff, Schimmel)
- **Zone:** alle Wohnräume | **Schweregrad:** mittel | **Sicherheits-Impact:** nein (chron. Gesundheit)
- **Fehlerbild:** Luftstagnation; Kondensat; Schimmel an kalten Flächen/hinter Verkleidung.
- **Ursache:** fehlende Querlüftung; kalte Wärmebrücken; keine mechanische Lüftung.
- **Diagnose:** Feuchtemessung (Ziel < 70 % r.F., `estimated`); Kondensat-Spuren; Schimmel hinter Polster/Verkleidung.
- **Abhilfe:** Querlüftung herstellen; 12V-Lüfter/Hygrostat; Heizung ≥ 12 °C; Entfeuchter.
- **Norm:** RCD-Lüftung nur zweckgebunden (Motor/Gas/Batterie); Wohnraum-ACH `estimated`.

### FB-31-11-008 — Möbel/Kojen nicht für Heel optimiert (Rutsch/Sturz)
- **Zone:** Saloon, Kojen | **Schweregrad:** hoch | **Sicherheits-Impact:** ja
- **Fehlerbild:** lose Möbel; Koje ohne Lee-Netz/Leesegel; glatte Bodenbeläge.
- **Ursache:** Serienausstattung; entferntes Sicherungszubehör.
- **Diagnose:** Möbelbefestigung prüfen; Lee-Netz/Leesegel je Seekoje vorhanden?; Rutschhemmung Boden.
- **Abhilfe:** Möbel strukturell verschrauben; Lee-Netze; rutschhemmende Beläge; Haltegriffe.
- **Norm:** keine bindende Innen-Norm → `estimated`.

### FB-31-11-009 — Stauraum unzureichend / Ladung nicht gesichert
- **Zone:** alle | **Schweregrad:** hoch | **Sicherheits-Impact:** ja (Ladungswanderung, Trimm/Stabilität)
- **Fehlerbild:** schwere Gegenstände ungesichert; Migration bei Krängung; Stauraum-Deckel ohne Verriegelung.
- **Ursache:** Planungslücke; Überladung; fehlende Zurrpunkte.
- **Diagnose:** Schwer-Item-Inventur; Zurr/Verriegelung prüfen; CG-/Trimm-Auswirkung abschätzen (siehe `structural`-Modul, ISO 12217 für Stabilität/CG).
- **Abhilfe:** Zurrpunkte, verriegelbare Deckel, Anti-Rutsch-Einlagen; schwere Lasten mittschiffs/tief.
- **Norm:** Gewichts-/CG-Verteilung ISO 12217-2 (Stabilität, `documented`); Stauraum-Maße `estimated`.

### FB-31-11-010 — Trimm durch Last-/Einrichtungsverteilung beeinträchtigt
- **Zone:** gesamtes Layout | **Schweregrad:** mittel | **Sicherheits-Impact:** teilweise
- **Fehlerbild:** ungünstige Längslage; Bug-down/Bug-up; asymmetrische Tanks.
- **Ursache:** schwere Einrichtung außermittig; Refit-Zusatzgewichte.
- **Diagnose:** CG-Rechnung je Ladefall (light_ship, full_departure, arrival, worst_case); Trimm > 1° Motor / > 2° Segel flaggen (AYDI `structural`-Konvention, `estimated`).
- **Abhilfe:** Gewichte umverteilen; Tankmanagement-Prozedur.
- **Norm:** ISO 12217 (Stabilität/CG, `documented`); Trimm-Schwellwerte projektintern `estimated`.

### FB-31-11-011 — Akustik/Lärmisolierung schwach
- **Zone:** motornahe Kabinen, Saloon | **Schweregrad:** niedrig–mittel | **Sicherheits-Impact:** nein
- **Fehlerbild:** hoher Innenpegel unter Motor; Wellenschlag/Schotklappern.
- **Ursache:** fehlende Motorraumdämmung; starre Kopplung; offene Türen.
- **Diagnose:** dB(A)-Messung (Werte in Abschnitt 8 sind `estimated`, **kein** ISO-12217-3-Bezug — das ist Stabilität, nicht Lärm).
- **Abhilfe:** Motorraum-Dämmung, elastische Lagerung, Türdichtungen.
- **Norm:** Innenraum-Lärmgrenzen **nicht** durch ISO 12217 geregelt → `estimated`.

### FB-31-11-012 — Kabinentüren/Verschlüsse fluchtuntauglich
- **Zone:** Kabinentüren, Luken | **Schweregrad:** hoch | **Sicherheits-Impact:** ja
- **Fehlerbild:** Tür klemmt bei Krängung/Rumpfverwindung; Verschluss nur elektrisch; keine Öffnung von innen ohne Werkzeug.
- **Ursache:** enge Toleranz; Elektroverriegelung ohne mechanische Redundanz.
- **Diagnose:** Tür-/Lukenöffnung unter simulierter Krängung; Notöffnung von innen ohne Strom/Werkzeug prüfbar?
- **Abhilfe:** Toleranz nachstellen; mechanische Notentriegelung; Fluchtluken gängig halten.
- **Norm:** RCD §3.8 (Fluchtweg brauchbar); ISO 12216 (Luken-/Türfunktion). `documented`

---

## 13. Troubleshooting / Verfahren

### 13.1 Fluchtweg-Audit (Verfahren)
1. Für **jede** Schlafkoje: Weg zum Hauptausstieg begehen — bei geschlossenen Türen, im Dunkeln. Zeit- und Hindernis-Notiz.
2. Zweiten (unabhängigen) Fluchtweg identifizieren — i. d. R. eine Deckluke nach ISO 12216. Öffnung ohne Werkzeug/Strom, von liegend erreichbar.
3. **Mehrrumpf:** Kenter-Fluchtluke je Rumpf prüfen (Ø ≥ 450 mm bzw. äquivalent), Position aufrecht **und** gekentert nicht dauernd unter Wasser (ISO 12217-2 / ISO 12216).
4. Brand-Szenario: Fluchtweg unabhängig von Motorraum/Galley (ISO 9094).
5. Befund dokumentieren; KRITISCH nur als „Befund prüfen" an menschliche Freigabe.
> Norm-Basis: RCD §3.8, ISO 12216, ISO 9094, ISO 12217-2 (alle `documented`).

### 13.2 Kondensat/Schimmel eingrenzen
1. r.F. an mehreren Punkten messen (Ziel < 70 %, `estimated`).
2. Kalte Wärmebrücken lokalisieren (Deck, Schotten, Rumpfseite hinter Verkleidung).
3. Querlüftung sicherstellen (Zu-/Abluft gegenüberliegend); mechanische Lüftung/Hygrostat ergänzen.
4. Grundtemperatur ≥ 12 °C halten (senkt Taupunktdifferenz).
5. Materialseitig: Holzwerkstoffe in Nasszonen versiegeln (Feuchte-Risiko-Mapping, siehe `materials`-Modul).

### 13.3 Galley-Seegangs-Check (vor Törn)
1. Gimbal frei durchschwenken; Lager schmieren (Intervall siehe 14).
2. Fiddle Rails + Topfsicherung montiert; Gasabsperrung griffbereit.
3. Gasanlage: Kasten nach außen belüftet/entwässert, LPG-Sensor funktionsfähig (RCD §5.5).
4. Schwere Kochutensilien verstaut/gesichert.

---

## 14. Wartung & Prüffristen

> Intervalle: Herstellerpraxis/Betriebserfahrung = `estimated`, sofern nicht norm-/herstellergebunden. Sicherheitsrelevante Positionen fett.

| Position | Prüfung/Tätigkeit | Intervall | Confidence |
|----------|-------------------|-----------|-----------|
| **Fluchtluken/Notausstieg** | Öffnen ohne Werkzeug, Dichtung, Freihaltezone | **vor jeder Saison + monatlich in Nutzung** | `estimated` |
| **Gasanlage/LPG-Kasten** | Dichtheit, Belüftung/Entwässerung, Sensor | **Dichtprüfung jährlich; Sensor-Funktionscheck vor Törn** | `estimated` |
| **Gimbal-Herd** | Lager schmieren, Freischwenk | 6 Monate (Schmierung) | `estimated` |
| Mechanische Lüfter | Filter reinigen (Salz-Korrosion) | monatlich | `estimated` |
| Lüfter-Lager | schmieren | jährlich | `estimated` |
| Lüfter (Motor) | Austausch (Verschleiß) | 8–10 Jahre | `estimated` |
| **Kabinentüren/Notentriegelung** | Gängigkeit unter Krängung, mech. Notöffnung | vor Saison | `estimated` |
| Lee-Netze/Leesegel | Material-/Befestigungsprüfung | vor Saison | `estimated` |
| Holding-Tank/Entlüftung | Aktivkohlefilter, Ventile | jährlich | `estimated` |
| Möbelbefestigung | Verschraubung/Zurrpunkte nachziehen | jährlich | `estimated` |

---

## ANHANG C+ — FAQ (Erweiterung)

**F11: Welche Norm regelt den Notausstieg wirklich?**
A: Die **Pflicht** ergibt sich aus RCD 2013/53/EU Anhang I §3.8 (Fluchtweg im Brandfall für jedes bewohnbare Boot; zusätzlich Kenter-Fluchtweg für kenterungsanfällige Mehrrümpfe). Die **Luke** (Festigkeit, Wasserdichtheit, lichte Öffnung) fällt unter ISO 12216; die **Kenterbewertung + „viable means of escape"** unter ISO 12217-2. Nicht ISO 12217 für die Luken-Maße. `documented` — [legislation.gov.uk/eudr/2013/53/annex/I](https://www.legislation.gov.uk/eudr/2013/53/annex/I)

**F12: Wie groß muss die Fluchtluke sein?**
A: Verifiziert ist der **Mehrrumpf**-Fluchtluken-Durchlass **Ø ≥ 450 mm** (bzw. äquivalente lichte Weite für nicht-runde Luken), ISO 12216. Der im Text genannte Wert 400 × 520 mm ist gegen den freien Normauszug **nicht** belegbar → `estimated — unverifiziert`. Exakte Maße nur im (kostenpflichtigen) ISO-12216:2020-Normtext. `documented` (450 mm) — [rutgerson.se/escape-hatch](https://www.rutgerson.se/escape-hatch/)

**F13: Sind die Durchgangsbreiten/Kabinenmaße genormt?**
A: Nein. Für Innen-Kabinenmaße, Kojen-, Durchgangs- und Stehhöhen gibt es **keine** bindende ISO-Norm. Die Tabellenwerte im Dokument sind Konstruktions-Konventionen → `estimated`. Bindend sind nur: freier Fluchtweg (ISO 9094/RCD), Luken/Türen (ISO 12216), Süllhöhen/Cockpit (ISO 11812), Stabilität/CG (ISO 12217).

**F14: Regelt ISO 12217-3 den Innenraum-Lärm?**
A: Nein. ISO 12217(-2/-3) ist **Stabilität und Auftrieb**. Innenraum-Lärmgrenzen sind darin nicht enthalten. Die dB-Werte in Abschnitt 8 sind `estimated`. `documented` (Scope) — [iso.org/standard/79073.html](https://www.iso.org/standard/79073.html)

**F15: Was fordert die RCD zur Lüftung im Layout?**
A: Zweckgebunden: Motorraum belüftet (§5.1.2), Gasanlage/-kasten nach außen belüftet und entwässert (§5.5), Batterie-Lüftung gegen explosive Gase. Keine ISO-Vorgabe für allgemeine Wohnraum-ACH. `documented` — [legislation.gov.uk/eudr/2013/53/annex/I](https://www.legislation.gov.uk/eudr/2013/53/annex/I)

---

## ANHANG A+ — Glossar (Erweiterung)

**Fluchtluke (Escape Hatch):** Öffnung als brauchbarer Fluchtweg; bei Mehrrümpfen für den Kenterfall (ISO 12216 / ISO 12217-2).

**Süll (Sill / Companionway Sill):** Erhöhte Schwelle am Niedergang; Höhe nach CE-Kategorie und ISO 11812.

**LH (Length of Hull):** Rumpflänge — Geltungsbereichsmaß der ISO-Kleinfahrzeugnormen (bis 24 m).

**RCD:** Recreational Craft Directive 2013/53/EU — EU-Richtlinie für Sportboote 2,5–24 m.

**Fiddle Rail:** Stopper-/Umrandungsleiste auf Arbeitsflächen gegen Gegenstands-Rutsch.

**Lee-Netz / Leesegel:** Seitliches Netz/Tuch an der Seekoje, verhindert Herausrollen bei Krängung.

**ACH (Air Changes per Hour):** Luftwechselrate; hier `estimated`, kein ISO-Grenzwert.

---

**Redaktion & Qualitätskontrolle:** AYDI Knowledge Engineering v6  
**Letzte Überprüfung:** 2026-07-13 (Werft-Tiefe-Erweiterung: Normativer Rahmen web-verifiziert, Fehlerbild-Atlas FB-31-11-NNN, Troubleshooting, Prüffristen)  
**Gültig für:** Segelboote, Motorsegler, Motorboote 8–40m LOA

> **Verifikations-Hinweis (Audit):** Neue Normbezüge in Abschnitt 11–14 sind gegen ISO/RCD-Quellen web-verifiziert (`documented`). Innen-Maße/ACH/dB/Kosten bleiben `estimated`, da keine bindende Norm existiert. Exakte Normkoeffizienten/Öffnungsmaße stehen ausschließlich in kostenpflichtigen ISO-Normtexten (12216, 11812, 9094, 12217) und wurden **nicht** rekonstruiert oder erfunden.
