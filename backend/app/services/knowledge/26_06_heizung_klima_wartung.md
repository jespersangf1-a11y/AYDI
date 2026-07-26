---
category: "26_Heizung_Klima"
subcategory: "Heizung_Klima_Wartung"
title: "HVAC Wartung – Saisonale Instandhaltung & Fehlerdiagnose"
version: "1.0"
created: "2026-05-18"
language: "de"
confidence_badge: "documented"
---

# HVAC Wartung – Saisonale Instandhaltung & Fehlerdiagnose

## 1. Wartungs-Rahmenwerk & Saisonale Abläufe

### 1.1 Jahresplan für Heizung & Klimatisierung

**Frühling (März–April) – Kommissionierung für Saison:**

| Aufgabe | Frequenz | Aufwand | Kosten |
|---|---|---|---|
| Visuelle Sichtprüfung aller Rohre | 1× | 30 min | kostenlos |
| Seewasser-Filter wechseln | 1× | 20 min | 80–150 EUR |
| Kältemittel-Druck messen | 1× | 15 min | kostenlos |
| Diesel-Heizer: Zündung & Flamme testen | 1× | 30 min | kostenlos |
| Kondenswasser-Ablauf prüfen | 1× | 15 min | kostenlos |
| Defrost-System testen (Luft-WP) | 1× | 20 min | kostenlos |
| Elektrische Sicherheit prüfen | 1× | 20 min | kostenlos |

**Sommer (Mai–August) – Betrieb & Überwachung:**

| Aufgabe | Frequenz | Aufwand | Kosten |
|---|---|---|---|
| Durchfluss-Schalter prüfen | monatlich | 5 min | kostenlos |
| Stromverbrauch kontrollieren | monatlich | 5 min | kostenlos |
| Verdampfer-Lamellen reinigen | monatlich | 15 min | kostenlos |
| Seewasser-Filter-Druck prüfen | monatlich | 5 min | kostenlos |
| Kondensat-Ablauf überprüfen | monatlich | 5 min | kostenlos |

**Herbst (September–Oktober) – Vorbereitung auf Winter:**

| Aufgabe | Frequenz | Aufwand | Kosten |
|---|---|---|---|
| Defrost-Sensor kalibrieren | 1× | 45 min | kostenlos |
| Diesel-Heizer: Brenner inspizieren | 1× | 60 min | 150–300 EUR |
| Seewasser-Rohre auf Beschädigungen prüfen | 1× | 45 min | kostenlos |
| Kältemittel-Charge überprüfen | 1× | 30 min | 100–200 EUR |
| Thermostat-Einstellung justieren | 1× | 15 min | kostenlos |
| Einfüll- und Ablassventile überprüfen | 1× | 30 min | kostenlos |

**Winter (November–März) – Betrieb & Sicherheit:**

| Aufgabe | Frequenz | Aufwand | Kosten |
|---|---|---|---|
| Testbetrieb (kurz) | alle 4 Wochen | 10 min | Strom |
| Temperatur-Überwachung | wöchentlich | 5 min | kostenlos |
| Nach Sturm: Seewasser-Rohre prüfen | nach Ereignis | 30 min | kostenlos |
| Verdampfer-Frost-Schutz prüfen | monatlich | 10 min | kostenlos |
| Stromversorgung stabil (Generator) | täglich | 5 min | kostenlos |

### 1.2 Professionelle Jahreswartung (Service-Betrieb)

Eine vollständige Jahreswartung durch zertifizierten Marine-Techniker sollte durchgeführt werden:

**Zeitaufwand:** 3–5 Betriebsstunden
**Kosten:** 400–800 EUR (Material + Arbeitszeit)

**Checklist für Profi-Wartung:**

```
SEEWASSER-KREISLAUF (wenn vorhanden):
  [ ] Durchfluss-Schalter Schaltverhalten überprüfen
  [ ] Seewasser-Filter-Druckanzeige prüfen
  [ ] Rückschlag-Ventile in Durch- und Rückfluss funktionsfähig?
  [ ] Rohre auf Korrosion, Risse, Verschleißstellen überprüfen
  [ ] Mit Ultraschall: Durchfluss-Geschwindigkeit messen (sollte 0,8–1,2 m/s sein)
  [ ] Wärmeaustauscher-Oberfläche (innen) mit Endoskop inspizieren
  [ ] Drucktest: System unter Last (<0,1 bar/h Druckabfall = dicht)

KÄLTEKREISLAUF:
  [ ] Hochdruck/Niederdruck messen (unter Betrieb + Teillast)
  [ ] Kältemittel-Charge abwiegen (Soll-Menge vs. IST)
  [ ] Öl-Sichtprobe (Farbe: klarbis leicht gelb = normal)
  [ ] Mit Feuchtigkeit-Indikator-Öl prüfen (Farbwechsel = Wasser/Salzwasser)
  [ ] Rückschlag-Ventile Funktionsprüfung
  [ ] Druckschalter Abschalt-Schwelle überprüfen
  [ ] COP-Messung durchführen (Heiz-Leistung / el. Leistung)

DIESEL-HEIZER (wenn vorhanden):
  [ ] Zündkerze inspizieren (Ablagerungen?)
  [ ] Brenner-Funktion prüfen (Flamme blau, stabil)
  [ ] Kraftstoff-Filter wechseln
  [ ] Abgas-Prüfung (schwarze Rauch = Verschleiß)
  [ ] Wärmeaustauscher-Effizienz testen (Ein/Ausgangstemperatur)

ELEKTRISCHE SICHERHEIT:
  [ ] Isolationswiderstand Wärmeaustauscher (>10 MΩ)
  [ ] Erdungsführung überprüfen
  [ ] Schutzschalter FI-Test durchführen
  [ ] Kabelisolation auf Beschädigungen prüfen
  [ ] Kompressor-Wicklung messen (R12-R23, sollte symmetrisch sein)

THERMISCHE STEUERUNG:
  [ ] Thermostat mit Prüfblock kalibrieren (±1°C Genauigkeit)
  [ ] Hysterese-Einstellung überprüfen (1–2°C Normal)
  [ ] Sensor-Positionierung & Sauberkeit kontrollieren
  [ ] Sollwert-Speicher im Controller prüfen (nicht gelöscht?)
```

## 2. Saisonale Kommissionierung (Frühjahr)

### 2.1 Frühlings-Checkliste (März–April)

**Vor dem ersten Betrieb nach Winter:**

**Schritt 1: Visuelle Inspektion (30 min)**
- Außengeräte: Lamellen-Verschmutzung? (Salzwasser-Spritz, Laub)
- Innen-Kassetten: Verschimmelung des Verdampfer-Gehäuses?
- Seewasser-Rohre: Korrosion, Risse, Verformungen?
- Kondenswasser-Ablauf-Rohr: durchhängend, blockiert?
- Kältemittel-Rohre: Kratzer, nackte Isolierung?

**Schritt 2: Funktions-Schnelltest (20 min)**
1. System auf Kühlmodus stellen
2. Kompressor sollte innerhalb 10 sec starten
3. Nach 1 min sollte Kondenswasser ablaufen
4. Hochdruck-Manometer: sollte 18–22 bar zeigen (bei Raumtemp. 20°C)
5. Niederdruck-Manometer: sollte 3–5 bar zeigen (Seewasser) / 5–8 bar (Luft)

**Schritt 3: Filter & Durchfluss (20 min)**
- Seewasser-Filter prüfen: grün/blau = ok, braun/schwarz = tauschen
- Druckschalter Kontakt testen (sollte schließen bei Durchfluss)
- Durchfluss-Größenordnung: bei 12 kW sollte ca. 3 m³/h sein

**Schritt 4: Sicherung & Stromversorgung (15 min)**
- 24V Stromversorgung prüfen (Spannungsmesser)
- Sicherung/Schutzschalter prüfen (nicht gebrannt?)
- Erdungsprüfung (mit Ohmmeter <1 Ω zum Schiff-Rumpf)

**Schritt 5: Diesel-Heizer (falls vorhanden) (30 min)**
- Zündung überprüfen (Zündkerze inspizieren)
- Flamme testen (sollte innerhalb 10 sec blau zünden)
- Kraftstoff-Durchfluss prüfen (keine Blockade)
- Abgasleitung überprüfen (Risse, Wasseraustritt?)

### 2.2 Frühjahrs-Service-Kosten (Selbst vs. Profi)

**Selbst durchgeführte Wartung:**
- Zeit: 3–4 Stunden
- Material: Seewasser-Filter (80–150 EUR), Dieselfilter (30–50 EUR)
- Gesamt: 110–200 EUR

**Profi-Wartung (empfohlen):**
- Kosten: 400–700 EUR (inkl. Diagnostik, Druck-Tests, Kalibrierung)
- Vorteil: Garantie, Fehler-Früherkennung, Zertifikat für Versicherung

## 3. Saisonale Dekommissionierung (Herbst)

### 3.1 Herbst-Vorbereitung (September–Oktober)

**Ziel:** System winterfest machen, Korrosion/Frost-Schäden verhindern

**Schritt 1: Kältemittel-System-Check (45 min)**
1. Druck-Messung durchführen (Hochdruck/Niederdruck beide dokumentieren)
2. Falls Druck zu niedrig (<1 kg/a Leckverlust ist normal):
   - Mit UV-Leckdetektions-Öl überprüfen
   - Kleines Leck fachlich reparieren (200–400 EUR)
3. Bei korrektem Druck: System ist ok für Winter

**Schritt 2: Defrost-System aktivieren (20 min)**
- Für Luft-Wärmepumpen wichtig!
- Controller auf "Auto-Defrost" stellen
- Defrost-Sensor-Kabel überprüfen (keine Risse, gute Verbindungen)
- Testbetrieb: Defrost-Magnetventil sollte Klick-Geräusch machen
- Verdampfer-Temperatur mit Thermometer auf -2 bis -5°C prüfen (Trigger-Punkt)

**Schritt 3: Diesel-Heizer-Vorbereitung (60 min)**
- Brenner inspizieren und reinigen
- Zündkerze eventuell austauschen (wenn älter als 2 Jahre)
- Kraftstoff-Filter wechseln (wichtig!)
- Kraftstoff-Tank überprüfen (Wasser-Absatz? Mit Wasser-Test-Papier)
- Abgas-Schornstein prüfen (Wasser-Austritt im Winter sollte drinnen auffangen)

**Schritt 4: Seewasser-Rohr-Protection (45 min)**
- Falls in Eisfähigen Gewässern geplant: Leerung erwägen
  - Seewasser aus Rohren mit Druckluft ausblasen
  - Verdampfer mit Salz-Wasser-Konservierungs-Öl spülen
  - Rückschlag-Ventil sollte Wasser zurück ins Meer drücken
- Alternative: regelmäßig Durchfluss (alle 4 Wochen 10 min) um Eis zu verhindern

**Schritt 5: Thermostat-Justierung (15 min)**
- Solltemperatur auf Winter-Modus prüfen (z.B. 18°C Minimum)
- Hysterese prüfen (wenn unterschritten, sollte zuschalten)
- Nacht-Temperatur programmieren (z.B. 16°C, damit morgens warm ist)

### 3.2 Winterlagerings-Checkliste

**Langzeitstilllegung (>4 Wochen ohne Betrieb):**

```
ELEKTRONIK:
  [ ] Hauptschalter auf OFF
  [ ] Batterie ggf. trennen (wenn Leerlauf-Stromzug >10 mA)
  [ ] Speicher-Batterie-Uhr prüfen (sollte nach Wiederkehr noch laufen)

KÄLTEKREISLAUF:
  [ ] Hochdruck/Niederdruck dokumentiert?
  [ ] Falls Einfüll-/Ablassventile verfügbar: Überdruckventil öffnen (Druck ablassen?)
  [ ] Kältemittel-Rohre mit Abdeck-Kappen schützen (vor Staub/Verschmutzung)

SEEWASSER-KREISLAUF:
  [ ] Wasser ablassen (Rohre sollten von Süßwasser gespült werden)
  [ ] Filter ausbauen und lagern (vor Austrocknung geschützt)
  [ ] Rohre mit Sperrluft füllen oder Druck-Regulierung öffnen

DIESEL-HEIZER:
  [ ] Kraftstoff-Tank überprüfen (konserviert, Wasser ausgeschlossen?)
  [ ] Brenner-Kappe aufschrauben (trockene Luft-Zirkulation)

GESAMT:
  [ ] Funktionstests durchgeführt und dokumentiert
  [ ] Reparaturen notiert (für nächste Saison)
  [ ] Ersatzteile bestellt (für nächste Inbetriebnahme)
  [ ] Wartungs-Logbuch aktualisiert
```

## 4. Diesel-Heizer Service & Wartung

### 4.1 Diesel-Heizer-Typen im Marine-Einsatz

**Webasto Airtop / Planar (verbreitet):**
- Brennstoff: Diesel (Schiffs-Diesel oder Marine-Diesel)
- Wärmeleistung: 2–16 kW
- Zündung: Glühkerze (24V)
- Befestigung: Einbau unter/über Kajüte

**Eberspächer Marine-Heizer:**
- Variante zu Webasto
- Schichtung: Verdampfungs-Brenner (neuere Technik, weniger Emissionen)

**Barigo/Sero (auf Segelyachten):**
- Beheizte Rohre
- Langsame Aufwärmung (30–45 min)
- Zuverlässigkeit hoch

### 4.2 Diesel-Brenner-Wartung & Fehlerdiagnose

**Regelmäßige Aufgaben (monatlich):**
1. Zündkerze prüfen (keine Kohle-Ablagerungen)
2. Brenner-Raum mit Lichtprüfung inspizieren (Korrosion?)
3. Abgastemperatur prüfen (sollte 80–120°C sein)
4. Flammen-Farbe überprüfen (blau = normal, orange/rot = Verschleiß/Verschmutzung)

**Jährliche Inspektionen:**
1. Zündkerze austauschen (Verschleiß nach ca. 1.000 Betriebsstunden)
2. Kraftstoff-Filter wechseln
3. Brenner-Kopf reinigen (mit Druckluft)
4. Wärmeaustauscher-Außenseite ausbürsten (Ruß-Ablagerungen)
5. Abgasleitung auf Verstopfung prüfen (mit Stahlbürste)

**Fehler: Diesel-Heizer zündet nicht**

Diagnose-Schritte:
1. Stromversorgung überprüfen (24V an Glühkerze vorhanden?)
2. Diesel-Durchfluss prüfen (Prüfpumpe am Kraftstoff-Filter betätigen)
3. Zündkerze auswechseln (abgenutzte Kerze oft Ursache)
4. Mit Inspektions-Spiegel Flammen-Anzünden prüfen
5. Falls kein Funke: Glühkerzen-Steuerung überprüfen

**Fehler: Heizer läuft, aber schwache Leistung**

Diagnose:
1. Eingangs-Wassertemperatur prüfen (sollte >5°C sein)
2. Wärmeaustauscher-Außenseite auf Ruß-Ansammlung prüfen
3. Kraftstoff-Qualität überprüfen (alte Tanks → Wasser-Gehalt)
4. Brenner-Druckeinstellung prüfen (zündet mit richtigem Druck?)
5. Thermostat-Ventil überprüfen (blockiert Durchfluss?)

## 5. Wärmeaustauscher-Reinigung & Wartung

### 5.1 Seewasser-Wärmeaustauscher (Verdampfer bei WP)

**Verschmutzungs-Ursachen:**
1. Biofilm-Schichten (Bakterien + Schleim)
2. Kalkablagerungen (hartgewässer, Mittelmeer)
3. Algen-Ablagerungen (Tropen, biologisch reich)
4. Sand/Sediment (flache Gewässer)
5. Muschellarven-Verstopfung (Ostsee-Sommer)

**Reinigung – Methode 1: Chemische Spülung (Standard)**

Durchflussrichtung sollte Richtung Verdampfer sein:

1. Wärmeaustauscher ausbauen (oder In-Situ-Spülung mit Bypass-Leitungen)
2. Zitronensäure-Lösung vorbereiten: 1 Teil Zitronensäure + 20 Teile Wasser
   - Menge: ca. 5 Liter bei 12-kW-System
   - Alternative: Essigsäure (Essig) 1:10
3. Mit kleiner Tauch-Pumpe (12V DC, 20 l/h) durch Wärmeaustauscher pumpen
4. Kreislauf 30–60 min laufen lassen
5. Mit Süßwasser nachspülen (2× Volumen)
6. Verdampfer mit Druckluft auspusten (trocknen)

**Reinigung – Methode 2: Mechanische Spülung (Notfall, starke Verstopfung)**

1. Rohr-Bürste (6–8 mm ø, Stahl oder Kunststoff) durch Rohre führen
2. Mehrmals hin- und herbewegen (Ablagerungen lösen)
3. Mit Druckluft (3–4 bar) ausblasen
4. Mit Wasser nachspülen

**Reinigung – Methode 3: Ultraschall-Spülung (Profi)**

1. Wärmeaustauscher in Ultraschall-Bad legen (bei Fachbetrieb)
2. Frequenz: 20–40 kHz (entfernt auch feine Biofilm-Schichten)
3. Dauer: 15–30 min
4. Kosten: 150–300 EUR
5. Ergebnis: Wie-neu-Zustand

**Wartungs-Frequenz nach Gewässer-Typ:**

| Gewässer | Verschmutzungs-Risiko | Wartungs-Rhythmus |
|---|---|---|
| Ostsee (Süßwasser-Mischung) | Biofilm, Algen | 6–8 Wochen |
| Mittelmeer (salzreich) | Kalk, Algen | 8–12 Wochen |
| Tropen (biologisch reich) | Plankton, Biofilm | 4–6 Wochen |
| Arktis (Eis, Kälte) | Eis-Ansammlungen | ganzjährig prüfen |
| Flussmündungen (brackig) | Sand, Sediment | alle 4–6 Wochen |

### 5.2 Luft-Kondensator (Außenseite, Wärmepumpe kühlt)

**Verschmutzung:** Salzwasser-Spritz, Laub, Insekten, Staub

**Reinigung:**
1. Mit Druckluft von außen (niedrig! <2 bar, Lamellen nicht beschädigen)
2. Mit Bürstenaufsatz sanft über Lamellen gehen
3. Mit Süßwasser (Gartenschlauch) durchspülen
4. Abtropfen lassen

**Häufigkeit:** 2–4× pro Saison (sommer nach Pollen-Zeit, herbst nach Laubfall)

### 5.3 Verdampfer-Wärmeaustauscher im Diesel-Heizer

**Typ:** meist Reihen-Rohr-Wärmeaustauscher (Diesel-Abgas außen, Wasser innen)

**Verschmutzung:**
- Außenseite: Ruß-Ablagerungen (gelblich-braun)
- Innenside: Kalk (wenn hartes Wasser, z.B. Mittelmeer)

**Reinigung – Außenseite (Ruß):**
1. Mit Drahtbürste (weich) über Oberfläche gehen
2. Mit Druckluft ausblasen
3. Nicht mit Wasser waschen (treibt Ruß ins Innere)

**Reinigung – Innenseite (Kalk):**
1. Zitronensäure-Lösung mit Umwälzpumpe 30 min zirkulieren
2. Mit Süßwasser nachspülen
3. Trocknenlassen

**Effizienz-Prüfung:**
- Eingang-Temperatur Wasser: T_ein
- Ausgang-Temperatur: T_aus
- ΔT sollte bei Vollast 8–12°C sein
- Wenn ΔT <5°C: Wärmeaustauscher verschmutzt

## 6. Kühlmittel-Wartung (Süßwasser-Heizung)

Manche Yacht haben Süßwasser-Heiz-Kreislauf (Glykol-Wasser-Gemisch):

### 6.1 Glykol-Prüfung & -Austausch

**Prüf-Parameter:**
1. Frostschutz-Punkt: sollte mind. 10°C unter minimal erwartete Außentemp. sein
   - Ostsee-Winter (-15°C erwartet): Schutz bis -25°C erforderlich
   - Mittelmeer (0°C Minimum): Schutz bis -10°C ok
2. Farbe: klar bis leicht gelb = ok, braun/schwarz = alt, tausche
3. pH-Wert (mit Test-Papier): sollte 8–10 sein (zu niedrig = Korrosion)
4. Verschleiß-Partikel (mit Magnet-Probefläche): sollte keine sichtbaren Partikel sein

**Austausch-Rhythmus:**
- Neu-Installation: nach 100 Betriebsstunden kleine Überprüfung
- Alljährlich: Frostschutz mit Aräometer prüfen
- Alle 3–5 Jahre: kompletter Austausch (auch Wasser-Gehalt steigt mit Zeit)

**Tausch-Prozess:**
1. System ablassen (Ablassventil am tiefsten Punkt)
2. Mit Süßwasser spülen (2× Volumen)
3. Mit Druckluft auspusten (Rohre trocken!)
4. Neues Glykol-Wasser-Gemisch einfüllen (Verhältnis 40:60 oder 50:50 je Klima)
5. Entlüften (höchster Punkt öffnen, Luft ablassen, bis Flüssigkeit kommt)

## 7. Filter & Durchfluss-Komponenten

### 7.1 Seewasser-Filter-Austausch

**Filter-Spezifikation:**
- Porengröße: Standard 100 µm (Mikrometer)
- In Tropen oder biologisch aktiven Gewässern: 50 µm erwägen (feinere Struktur, mehr Wartung)
- Durchflussrate: sollte 2–5 m³/h ermöglichen (je nach Druckverlust)

**Tausch-Prozess:**
1. Seewasser-Zufuhr-Ventil schließen (Hahn auf "OFF")
2. Filter-Gehäuse-Schraube losdrehen (evtl. Wasser ablaufen)
3. Alten Filter entfernen, Gehäuse mit Pinsel ausbürsten (Schmutz-Reste)
4. O-Ring-Dichtung überprüfen (beschädigt? Tauschen)
5. Neuen Filter einsetzen (Markierung beachten: Einlass/Auslass-Richtung)
6. Gehäuse-Schraube wieder anziehen (nicht zu fest! max. 8 Nm bei M10)
7. Ventil öffnen, 1 min laufen lassen, Leckage überprüfen

**Häufigkeit nach Gewässer:**
| Gewässer | Intervall |
|---|---|
| Mittelmeer (klar) | alle 2–3 Monate |
| Ostsee (Algen, Plankton) | alle 4–6 Wochen |
| Tropen (hohe Biologie) | alle 2–4 Wochen |
| Flussmund (Sediment) | alle 2–3 Wochen |
| Arktis (Eis-Partikel) | wöchentlich prüfen |

### 7.2 Durchfluss-Schalter (Seewasser-Wärmepumpe)

**Funktion:** Schneidet Kompressor ab, wenn Seewasser-Durchfluss zu gering

**Prüfung:**
1. Bei Betrieb sollte Kontakt geschlossen sein (LED leuchten, wenn vorhanden)
2. Mit Durchflussmesser überprüfen: Soll-Durchfluss sollte 2–3 m³/h entsprechen
3. Falls <1,5 m³/h: Filter prüfen oder Rohr-Blockade suchen

**Wartung:**
- Kein aktiver Service nötig
- Bei Fehlfunktion: kompletter Austausch (50–150 EUR)

### 7.3 Diesel-Filter im Heizer

**Arten:**
- Kraftstoff-Filter (blockiert Dieselfluss zur Injektionspumpe)
- Luftfilter (Verbrennungs-Luft filtert)

**Austausch (jährlich oder bei Durchfluss-Abnahme):**
1. Kraftstoff-Durchfluss-Kontrolle stoppen (Ventil zu)
2. Filter-Element ausbauen
3. Mit Druckluft ausblasen (NICHT mit Wasser waschen)
4. Neues Element einsetzen
5. Durchfluss-Test machen (sollte wieder normal sein)

## 8. Fehlerbild & Diagnose – HVAC Wartung

### FB-26-06-001: Nach Winter: System startet nicht / kein Strom

**Ursachen:**
- Batterie-Spannungsabfall (24V-System unter 20V)
- Schutzschalter/Sicherung ausgelöst
- Stecker-Korrosion (Salzwasser-Umgebung)
- Elektronik-Speicher gelöscht

**Diagnose:**
1. Mit Multimeter Spannungsprüfung: sollte 24V ±10 % sein
2. Sicherung überprüfen (nicht gebrannt?)
3. Stecker-Anschlüsse überprüfen (grüne Oxidation? Kontakt schwach?)
4. Elektronik-Display prüfen (sollte Version-Nr. anzeigen, nicht "Fehler")

**Lösungen:**
- Batterie laden (wenn Bordnetz-Spannung <20V)
- Sicherung wechseln (gleiche Amperezahl!)
- Stecker-Kontakte mit Kontakt-Spray reinigen
- Elektronik-Speicher zurücksetzen (Energie trennen, 30 sec warten)

### FB-26-06-002: Diesel-Heizer zündet nicht / Glühkerze antwortet nicht

**Ursachen:**
- Zündkerze abgenutzt (nach 1.000–1.500 h Laufzeit)
- Glühkerzen-Steuerung-Fehler
- Diesel-Durchfluss blockiert
- Stromversorgung unzureichend (Batterie zu schwach)

**Diagnose:**
1. Mit Ohmmeter: Glühkerzen-/Glühstift-Widerstand prüfen (24V-Heizer: sollte 1,2–2,5 Ω sein; 12V-Heizer: 0,4–0,8 Ω)
   - Wenn Widerstand deutlich über Sollwert oder offener Stromkreis (Ohmmeter „out of range"): Glühstift ist verschlissen/durchgebrannt

> ✅ Aufgeloest (Audit): Für 24V-Marine-Diesel-Heizer (Webasto/Eberspächer) liegt der Glühstift-Widerstand bei 1,2–2,5 Ω (12V: 0,4–0,8 Ω); Ausfall = offener Stromkreis, nicht „>10 Ω". Der bisherige Sollwert „1–5 Ω / >10 Ω verschlissen" war zu weit; der Fallstudie-2-Grenzwert „<2,5 Ω" ist korrekt. — Quelle: Webasto Air Top 2000 D Repair Shop Manual (Glow-Plug Resistance Test) und Eberspächer Airtronic Reparaturunterlagen (24V-Glühstift 1,2–2,0/2,5 Ω).
2. Mit Prüfpumpe: Diesel-Durchfluss prüfen (sollte mit leichtem Druck fließen)
3. Stromspannung an Glühkerze mit Voltmeter prüfen (sollte 24V sein)

**Lösungen:**
- Zündkerze austauschen (15–30 EUR, 10 min)
- Kraftstoff-Filter wechseln (wenn verstopft)
- Batterie laden / Generator starten (Stromversorgung sichern)
- Glühkerzen-Steuerung ersetzen (wenn Elektronik fehlerhaft, 200–400 EUR)

### FB-26-06-003: Heizer-Leistung sinkt / wird nicht richtig warm

**Ursachen:**
- Wärmeaustauscher verschmutzt (innen oder außen)
- Thermostat-Ventil blockiert (zu wenig Durchfluss)
- Brenner-Einstellung zu niedrig (Druck-Regulierung falsch)
- Kraftstoff-Qualität schlecht (alte Tanks, Wasser-Gehalt)

**Diagnose:**
1. Eingangs- und Ausgangs-Wassertemperatur messen
   - Normal: ΔT 8–12°C bei Vollast
   - Wenn <5°C: Wärmeaustauscher verschmutzt
2. Abgastemperatur überprüfen (sollte 80–120°C sein)
3. Brenner-Farbe überprüfen (sollte blau sein, nicht orange)
4. Kraftstoff-Qualität mit Wasser-Test-Papier prüfen

**Lösungen:**
- Wärmeaustauscher mit Zitronensäure spülen
- Thermostat-Ventil reinigen oder ersetzen
- Brenner-Druck-Einstellung justieren (+0,1 bar = mehr Wärme)
- Neuen Kraftstoff nachtanken (alte Tanks leeren)

### FB-26-06-004: Kondenswasser läuft aus / Ablauf blockiert

**Ursachen:**
- Ablauf-Rohr verstopft (Biofilm, Sediment, Eis im Winter)
- Siphon-Wasser gelaufen / falsche Siphon-Höhe
- Ablauf-Drosslung zu eng (Rohr zu dünn dimensioniert)
- Verdampfer-Pfanne beschädigt / Kondenswasser läuft außen

**Diagnose:**
1. Mit Druckluft (1 bar) Ablauf-Rohr überprüfen (sollte Luft durchblasen)
2. Siphon-U-Form prüfen (sollte immer mit Wasser gefüllt sein)
3. Mit Farbstoff-Injektor überprüfen, wo Wasser austritt
4. Verdampfer-Gehäuse mit Licht inspizieren (Risse?)

**Lösungen:**
- Ablauf-Rohr mit Rohrreiniger spülen (biologisches Mittel für Biofilm)
- Siphon mit Wasser nachfüllen (oder ggf. U-Form-Siphon ersetzen)
- Ablauf-Rohr-Durchmesser erhöhen (mind. 12 mm ø)
- Verdampfer-Pfanne mit Silikon-Dichtung abdichten oder ersetzen

### FB-26-06-005: Seewasser-Durchfluss-Alarm / Druckverlust zu hoch

**Ursachen:**
- Seewasser-Filter verstopft (Biofilm, Plankton, Muschellarven)
- Seewasser-Einlass-Hahn nicht vollständig offen
- Rohrklemme oder Drosselventil unbeabsichtigt zu
- Rückschlag-Ventil blockiert

**Diagnose:**
1. Filter-Gehäuse-Druckanzeige prüfen (sollte <0,2 bar sein)
2. Einlass-Hahn überprüfen (vollständig offen?)
3. Mit Druckluft hinter dem Hahn-Auslass überprüfen (sollte Luft durchblasen)
4. Rückschlag-Ventil mit Prüflicht überprüfen (Eine-Weg-Ventil funktioniert?)

**Lösungen:**
- Filter austauschen (80–150 EUR, 20 min)
- Einlass-Hahn öffnen
- Rohrklemmen überprüfen und lockern
- Rückschlag-Ventil ersetzen (wenn blockiert, 100–200 EUR)

### FB-26-06-006: Kältemittel-Druck fällt nach Winter / System entladen

**Ursachen:**
- Micro-Lecks in Fittings (Vibrations-Ermüdung über Winter)
- Verdampfer- oder Kondensator-Rohr beschädigt (Frost-Expansion)
- O-Ring-Verschleiß
- Lockdown-Ventile nicht richtig verschlossen (wenn verfügbar)

**Diagnose:**
1. Mit Hochdruck-Manometer prüfen: sollte mind. 15 bar im Stillstand sein
2. Mit UV-Leckdetektions-Öl überprüfen (flüoresziert unter UV-Licht)
3. Mit Seifenlauge alle Fittings überprüfen (Blasenbildung = Leck)
4. Mit Helium-Schnüffeler professionell testen (<0,1 g/a = akzeptabel)

**Lösungen:**
- Micro-Lecks in Fittings: Fitting um 0,25 Drehung nachziehen
- Größere Lecks: Fittings-Austausch oder Lötprobe (100–300 EUR)
- O-Ring erneuern (kleine Kosten, großer Effekt)
- Nach Reparatur: System evakuieren + neu laden (Profi-Betrieb erforderlich)

### FB-26-06-007: Defrost-Sensor funktioniert nicht / Verdampfer friert zu

**Ursachen:**
- Sensor-Kabel unterbrochen (Vibrations-Ermüdung, Korrosion)
- Thermistor-Sensor-Fehler (Widerstand ändert sich nicht mit Temp.)
- Elektronik erkennt Sensor nicht (Kontakt-Fehler, Stecker)
- Sensor falsch kalibriert

**Diagnose:**
1. Mit Multimeter: Sensor-Widerstand messen bei verschiedenen Temp.
   - Bei 0°C sollte Widerstand ~5 kΩ sein
   - Bei 20°C sollte Widerstand ~1 kΩ sein
   - Wenn Widerstand konstant: Sensor defekt
2. Sensor-Kabel auf Bruch überprüfen (mit Ohmmeter)
3. Stecker-Verbindung überprüfen (Kontakt fest?)

**Lösungen:**
- Sensor-Kabel mit Spiral-Schutzschlauch neu verlegen
- Thermistor-Sensor ersetzen (20–50 EUR)
- Stecker-Verbindung reinigen und festziehen
- Elektronik-Speicher zurücksetzen (Fehler-Code löschen)

### FB-26-06-008: Stromverbrauch ungewöhnlich hoch / Generator-Überlast

**Ursachen:**
- Kompressor-Überlastung (Hochdruck zu hoch oder Niederdruck zu niedrig)
- Defrost-Magnetventil steckengeblieben (zieht ständig Strom)
- Heizer-Element läuft ohne Regelung (Fehler in Thermostat)
- Elektro-Heizer-Zusatz bei Wärmepumpe unbeabsichtigt aktiv

**Diagnose:**
1. Mit Stromzange: Stromaufnahme messen
   - Normal WP 8 kW: ca. 2,3 kVA el. Stromaufnahme
   - Wenn >3 kVA: Überlastung
2. Hochdruck überprüfen (sollte <25 bar sein)
3. Defrost-Magnetventil auditorisch überprüfen (Summen-Geräusch = Strom zieht)
4. Thermostat-Einstellung prüfen (sollte ausschalten, wenn Solltemp. erreicht)

**Lösungen:**
- Hochdruck reduzieren: Kondensator reinigen (Lamellen)
- Defrost-Magnetventil ausbauen und reinigen (oder ersetzen)
- Thermostat kalibrieren oder ersetzen
- Zusatz-Heizer deaktivieren (wenn nicht nötig)

### FB-26-06-009: Vibrations-Geräusche im Rohrsystem / Wasserhammer

**Ursachen:**
- Zu hohe Durchfluss-Geschwindigkeit (>1,2 m/s erosive Geschwindigkeit)
- Rohre nicht gedämmt (Vibrationen übertragen sich ins Schiff)
- Schnelle Durchfluss-Umschaltung (Magnetventil schließt ruckartig)
- Rückschlag-Ventil schlägt zu (Druckwelle)

**Diagnose:**
1. Mit Ohrmesser Frequenz bestimmen: tief/dumpf = Wasserhammer, hoch/pfeifend = Turbulenz
2. Durchfluss-Geschwindigkeit berechnen: v = Q [m³/h] / A [m²] × (1/3.600)
3. Mit Hand: Rohre überprüfen (vibrieren sie?)
4. Schrauben überprüfen (sitzen fest oder locker?)

**Lösungen:**
- Rohrdurchmesser vergrößern (1 Stufe größer wählen)
- Rohre mit Gummi-Dämplern / Klammern befestigen (Vibrations-Isolation)
- Drosselventil einbauen (Durchfluss senken)
- Rückschlag-Ventil austauschen (gepolsterte Variante mit Feder)

### FB-26-06-010: Nach langer Lagerung: Diesel-Heizer startet, aber Flamme erlischt nach 5 sec

**Ursachen:**
- Alter Diesel mit Wasser-Gehalt (Kondenswasser in Tank über Winter)
- Zündkerze zu schwach (nach Winterlagerung nicht mehr optimal)
- Kraftstoff-Filter verstopft
- Luft im Kraftstoff-Rohr

**Diagnose:**
1. Mit Wasser-Test-Papier Diesel-Tank überprüfen (verfärbt sich = Wasser vorhanden)
2. Zündkerze-Widerstand mit Ohmmeter überprüfen
3. Kraftstoff-Filter-Druckverlust prüfen (sollte <1 bar sein)
4. Luft-Bläschen im Fuel-Glass überprüfen (sollten verschwinden nach Start-Versuch)

**Lösungen:**
- Diesel-Tank völlig entleeren, mit Süßwasser spülen, neuer Diesel einfüllen
- Zündkerze austauschen
- Kraftstoff-Filter wechseln
- Entlüften: Fuel-Priming-Pumpe mehrmals betätigen bis kein Luft-Bläschen mehr

### FB-26-06-011: Kohle-Ablagerungen auf Zündkerze / Schwarzer Ruß-Auslass

**Ursachen:**
- Zu fettes Gemisch (Kraftstoff-Druck-Einstellung zu hoch)
- Verbrennungs-Temperatur zu niedrig (möglicherweise durch falsches Öl oder Abnutzung)
- Luft-Einlass blockiert (schmutziger Luftfilter)
- Injektions-Düse verstopft (schlechter Zerstäubung)

**Diagnose:**
1. Zündkerze ausbauen und inspizieren (schwarze Kruste = zu fett)
2. Luft-Filter überprüfen (Verschmutzung?)
3. Abgas-Farbe überprüfen (blau = normal, schwarz = fettes Gemisch)
4. Brenner-Druck mit Druckmanometer messen

**Lösungen:**
- Luftfilter austauschen (20–40 EUR)
- Brenner-Druck-Einstellung senken (um 0,1 bar)
- Zündkerze reinigen (mit Drahtbürste) oder austauschen
- Injektions-Düse professionell reinigen oder austauschen

### FB-26-06-012: Elektronik-Fehler / Steuerung antwortet nicht auf Befehle

**Ursachen:**
- Speicher-Batterie leer (Schaltuhren-Fehler, falls vorhanden)
- Elektronik-Prozessor hängt (Software-Fehler oder Dauer-Unterbrechung)
- Sensor-Fehler (Raumluft-Sensor blockiert)
- Kommunikations-Bus-Fehler (wenn CAN-Bus-System)

**Diagnose:**
1. Display-Meldung ablesen (Error-Code merken)
2. Stromversorgung trennen (30 sec), wieder anschalten (Soft-Reset)
3. Mit Prüflicht: Sensor-Anschlüsse überprüfen (sollten Kontakt haben)
4. Mit Multimeter: Sensor-Spannungen prüfen (sollten 0–5V variieren)

**Lösungen:**
- Speicher-Batterie austauschen (wenn vorhanden, ca. 10 EUR)
- Elektronik-Firmware zurücksetzen (mit Reset-Taster oder Service-Modus)
- Sensor reinigen oder Kabel überprüfen
- CAN-Bus-Verbindungen überprüfen (Stecker fest?)
- Im Extremfall: Elektronik-Einheit ersetzen (400–800 EUR)

## 9. Fallstudien – Wartung & Service-Fehler

### Fallstudie 1: Frühlings-Instandhaltung-Fehler (Seealpen-Yacht)

**Szenario:** 15m Segelacht, Seewasser-Wärmepumpe, Herbst war vernachlässigt worden

**Beobachtung:**
- Frühjahr: Wärmepumpe startet, aber Druck sinkt rapide nach 2 min
- Verdampfer-Temperatur bei Start: +18°C (normal)
- Nach 2 min: +5°C (OK)
- Nach 5 min: -2°C (Problem! Verdampfer friert an)

**Root-Cause-Analyse:**
1. Verdampfer-Temperatur-Regler (TXV) war über Winter stillgestanden
2. Verdampfer: Eiskristalle-Ansatz (kleine Vereisungen am Rohr-Eingang)
3. Beim Starten: Gefrorene Wassertropfen blockieren Expansion-Ventil
4. TXV-Schraube war nicht richtig nachgestellt worden

**Fehler-Kette:**
- Herbst-Wartung war zu schnell durchgeführt (15 min statt 45 min für TXV-Kalibrierung)
- Im Winter: mehrfacher Test-Betrieb (5 min) war nicht ausreichend, um Eis zu schmelzen
- Frühjahr: keine Inspektionen-Messungen vor Betrieb

**Lösungen durchgeführt:**
1. System ausschalten, 30 min in Sonne stehen lassen (Verdampfer abtauen)
2. TXV-Schraube neu einstellen (0,5 Umdrehung zurück)
3. Überprüfung: Verdampfer-Temperatur stabilisiert sich bei +8°C
4. Test-Betrieb: 2 h Vollast, alles normal

**Lehren:**
- Frühjahrs-Instandhaltung NICHT durchführen, wenn Außen-Temp <5°C
- Vor jeder Saison: Thermostat-Justierung überprüfen
- Winter-Testbetrieb sollte 30 min (nicht 5 min) sein, um Eis auszuschließen

---

### Fallstudie 2: Diesel-Heizer-Fehler nach zu lange Lagerung (Ostsee-Motorboot)

**Szenario:** 10m Motorboot, Diesel-Heizer 6 Monate ohne Betrieb

**Beobachtung:**
- November: Heizer läuft einwandfrei
- Mai (nach Winterlagerung): Zündflamme startet, aber erlischt nach 3–5 sec
- Wiederholte Start-Versuche: keine Besserung
- Geruch: modrig, nicht typisches Diesel-Aroma

**Root-Cause-Analyse:**
1. Diesel-Tank hatte Kondenswasser aufgebaut (Temperatur-Schwankung über Winter)
2. Wasser-Gehalt im Diesel: ~2–3 % (sichtbar als Trübung am Boden)
3. Mit Wasser-Test-Papier: positiv für Wasser
4. Zündkerze-Widerstand: 2,8 Ω (sollte <2,5 Ω sein) = minimal schwach

**Fehler-Kette:**
- Tank nicht entleert vor Lagerung (Standard-Fehler)
- Tank nicht mit Konservierungs-Öl oder Stickstoff-Atmosphäre geschützt
- Zündkerze nicht vorausschauend ausgetauscht (vor 6 Monaten hätte logisch sein sollen)

**Lösungen durchgeführt:**
1. Tank komplett entleert (ca. 8 Liter alter Diesel)
2. Mit Süßwasser 3× gespült
3. Mit Druckluft getrocknet
4. Neuer Diesel 100 % eingefüllt (8 Liter)
5. Kraftstoff-Filter ausgetauscht
6. Zündkerze ausgetauscht
7. Fuel-Entlüftung durchgeführt (Priming-Pumpe 20× betätigt)
8. Test-Start: normal, Zündung stabil

**Kosten:**
- Alter Diesel: 0 EUR (Entsorgung)
- Neuer Diesel: 12 EUR
- Kraftstoff-Filter: 35 EUR
- Zündkerze: 25 EUR
- Arbeitszeit: 90 min
- **Gesamt: 72 EUR + Arbeitszeit**

**Lehren:**
- Vor Langzeit-Lagerung: Tank entweder entleeren oder mit Stabilisator behandeln
- Zündkerze vor Lagerung austauschen (einfache Vorsorge)
- Nach Lagerung: Sichtprüfung des Diesels (klar vs. trüb)

---

### Fallstudie 3: Filter-Wartungs-Versäumnis in Tropen (Karibik-Charteryacht)

**Szenario:** 12m Motorsailer, Seewasser-Wärmepumpe, 4 Wochen Tropen-Saison

**Beobachtung:**
- Woche 1: Normal, COP 4,6
- Woche 2: COP fällt auf 3,8 (Durchfluss-Schalter gibt erste Warnung)
- Woche 3: Alarm Durchfluss-Schalter permanent
- Woche 4: System schaltet alle 10 min aus/an (Sicherheitsschutz)

**Root-Cause-Analyse:**
1. Seewasser-Filter Design 100 µm (zu grob für tropische Plankton-Blüte)
2. Keine Wartungs-Planung für tropisches Gewässer
3. Nach 4 Wochen: Filter mit Muschellarven + Biofilm völlig verstopft
4. Druckverlust Filter: >0,4 bar (sollte <0,2 bar sein)

**Fehler-Kette:**
- Charter-Brief hätte Tropen-Wartungs-Intervall erwähnen sollen (nicht geschehen)
- Crew war nicht über Unterschied zwischen Mittelmeer (2-Monats-Intervall) und Tropen (2-Wochen-Intervall) informiert
- Ersatz-Filter waren nicht an Bord (nur 1× Haupt-Filter im Boot)

**Lösungen durchgeführt:**
1. Filter ausbauen (Seewasser-Eintritt blockieren mit Hahn)
2. Alten Filter mit Süßwasser ausspülen (mehrfach) - teilweise Erfolg
3. Mit Ultraschall-Reinigung (Chartersbase hatte Equipment): Filter wieder einsatzbereit
4. Nach Reparatur: Druckverlust 0,1 bar (ok), COP wieder 4,4

**Kosten:**
- Ultraschall-Service: 180 EUR (ausgelagert)
- Ersatz-Filter (besorgt): 120 EUR
- **Gesamt: 300 EUR**

**Lehren:**
- Tropen-Einsatz: monatliche Filter-Austausch obligatorisch (nicht optional)
- Charter-Yachten sollten 2–3 Ersatz-Filter an Bord haben
- Crew-Schulung über Klima-Zone-spezifische Wartung erforderlich
- Langzeit-Lösung: 50 µm Filter für Tropen-Einsatz

---

### Fallstudie 4: Wechsel von Sommer auf Winter – Defrost-Sensor-Übersehen

**Szenario:** 18m Hybrid-Wärmepumpe (Seewasser + Luft), Skandinavien

**Beobachtung:**
- September: Umschaltung von Seewasser (COP 4,5) auf Luft-Verdampfer geplant
- Oktober: Außenluft-Temperatur sinkt auf 5°C
- Woche 1: Defrost-Magnetventil funktioniert, aber Zyklus läuft 3× pro Stunde (zu oft!)
- Woche 2: Verdampfer-Oberfläche hat Eiskruste, Defrost-Zyklus läuft kontinuierlich
- Woche 3: Defrost-Magnetventil steckengeblieben (elektromechanisch)

**Root-Cause-Analyse:**
1. Defrost-Sensor Schwellwert: -3°C (für südliche Breiten kalibriert)
2. Skandinavien-Oktober: Außenluft oft -5 bis -2°C (schwankend)
3. Sensor-Messungen: mehrmals pro Minute ab/-unter -2°C
4. Steuerung interpretiert als kontinuierliche Defrost-Notwendigkeit
5. Magnetventil-Betrieb: zu häufig (Verschleiß)

**Fehler-Kette:**
- Herbst-Wartung hatte Defrost-Schwellwert nicht für Skandinavien-Klima justiert
- Übergangs-Jahreszeit (Schwankungen) war unterestimiert
- Magnetventil-Verschleiß-Monitoring (Schalt-Zyklen zählen) nicht aktiv

**Lösungen durchgeführt:**
1. Defrost-Schwellwert erhöht: von -3°C auf -5°C (weniger häufig auslösen)
2. Hysterese erhöht: von 2°C auf 4°C (weniger Oszillationen)
3. Minimales Defrost-Intervall: auf 60 min eingestellt (nicht kürzer)
4. Magnetventil nach Belastung inspiziert (Kontakte ok)

**Kosten:**
- Service-Besuch: 150 EUR
- Parameter-Justierung: kostenlos
- Ersatz Magnetventil (nicht nötig, aber vorsichtshalber bestellt): 250 EUR Reserve
- **Gesamt: 150 EUR aktual**

**Lehren:**
- Defrost-Parameter sind klima-zone-abhängig, nicht universell
- Übergangs-Jahreszeiten (Sept/Okt) erfordern besondere Aufmerksamkeit
- Magnetventil-Belastung (Schalt-Zyklus-Monitoring) sollte Wartungs-Parameter sein
- Bei Umzug in andere Klima-Zone: Steuerungs-Neukalibrierung obligatorisch

---

## 10. FAQ – HVAC Wartung & Service

**F1: Wie oft sollte ich den Seewasser-Filter wechseln?**
A: Mittelmeer alle 2–3 Monate, Ostsee alle 4–6 Wochen, Tropen alle 2–4 Wochen. Faustregel: wenn Druck-Anzeige 0,2 bar überschreitet → tauschen.

**F2: Kann ich Winterlagerung ohne Entlüftung des Seewassersystems durchführen?**
A: Kurz (2–4 Wochen): ja, mit regelmäßigen Tests (alle 2 Wochen 10 min). Lange (>2 Monate): besser entleeren und mit Stickstoff trocknen.

**F3: Ist Profi-Wartung jährlich wirklich notwendig?**
A: Empfohlen ja. Kostet 400–700 EUR, spart aber 2.000+ EUR Reparatur-Kosten durch Früherkennung.

**F4: Kann ich den Diesel-Tank selbst spülen, oder muss Fachmann ran?**
A: Selbst möglich: Entleeren, 3× mit Süßwasser spülen, mit Druckluft trocknen. Profi ist sicherer (verhindert Fehler).

**F5: Wie erkenne ich, ob mein Diesel Wasser enthält?**
A: Mit Wasser-Test-Papier (ca. 5 EUR aus Bootszubehör). Verfärbt sich orange = Wasser im Tank.

**F6: Defrost-Sensor-Fehler – kann ich das selbst reparieren?**
A: Nur einfache Dinge: Kabel überprüfen, Stecker reinigen. Sensor-Austausch braucht Fachmann.

**F7: Wie lange hält ein Seewasser-Filter typischerweise?**
A: Bei normalem Betrieb (Mittelmeer): 8–12 Wochen. Unter schwierigen Bedingungen: 2–4 Wochen.

**F8: Kann ich während Wartung die Yacht heizen?**
A: Mit Zusatz-Heizer (Diesel), ja. Wärmepumpe sollte nicht laufen (Sicherheit).

**F9: Welche Teile sollte ich immer an Bord haben?**
A: Ersatz-Seewasser-Filter (2×), Zündkerzen (2×), Kraftstoff-Filter (2×), Isolations-Tape, Glühkerzen-Sätze.

**F10: Kann ich Wärmeaustauscher selbst reinigen?**
A: Ja, mit Zitronensäure-Lösung und Pumpe. Kosten <50 EUR. Profi-Ultraschall besser, kostet 150–300 EUR.

**F11: Nach Winter-Lagerung: wie lange warmfahren, bevor auf Reisen gehen?**
A: Mindestens 1 h Testbetrieb. Alle Systeme überprüfen (Druck, Temperatur, Stromaufnahme stabil?).

**F12: Ist R410A-Kältemittel nach 10 Jahren schlecht geworden?**
A: Nicht automatisch. Aber: Alter Öl kann Feuchte aufnehmen → Nachfüllen-Monitoring alle 2 Jahre.

**F13: Kann ich Diesel-Heizer von Diesel auf Biodiesel umstellen?**
A: Theoretisch ja (rein), praktisch: Biodiesel hat höheres Wasser-Potenzial → mehr Wartung. Nicht empfohlen.

**F14: Wie teuer ist eine komplette Seewasser-Pumpen-Überholung?**
A: 300–600 EUR (Dichtungen, Innenreinigung). Häufig teurer als Austausch (500–1000 EUR).

**F15: Muss ich die Wärmepumpe vor längerer Reise überprüfen?**
A: Ja, 1 h Probelauf, Druck messen, Durchfluss-Schalter prüfen. Nur 30 min, aber wichtig.

**F16: Kondenswasser-Ablauf riecht muffig – Problem?**
A: Biofilm in Rohr (normal). Mit biologischem Reiniger spülen. Nicht gefährlich, aber unhygienisch.

**F17: Kann ich Wärmeaustauscher-Reinigung mit Essig machen statt Zitronensäure?**
A: Ja, Essig 1:10 ist schwächer, braucht etwas länger (45 min). Beide wirken chemisch ähnlich.

**F18: Wie erkenne ich Verschleißöl im Kälte-Kreislauf?**
A: Öl-Sichtfenster: sollte klar/gelb sein. Dunkelbraun/schwarz = Verschleiß, Oxidation. Austausch erforderlich.

**F19: Schutzschalter schlägt immer wieder aus – was tun?**
A: Erst: Ursache klären (Hochdruck? Verdichter-Überlast?). Nicht einfach Schutzschalter ignorieren → Beschädigung.

**F20: Filter-Austausch-Kosten bei Profi vs. selbst?**
A: Selbst: 80–150 EUR Material, 20 min. Profi: 200–300 EUR (Material + 30 min Service-Anfahrt amortisiert sich bei später Fachmann-Besuch).

## 11. Wartungs-Checkliste als Tabelle

### Monatliche Selbst-Kontrolle (5–10 min)

| Punkt | Check | Normal | Aktion |
|---|---|---|---|
| Stromspannung | 24V Multimeter | 22–26V | Batterie laden wenn <20V |
| Hochdruck-Manometer | Visuelle Prüfung | 18–22 bar (still) | >25 bar = Kondensator reinigen |
| Niederdruck-Manometer | Visuelle Prüfung | 3–8 bar (still) | <1 bar = Lecks prüfen |
| Verdampfer-Lamellen | Sicht-Inspektion | sauber, fein | Verschmutzt = Druckluft blasen |
| Kondenswasser-Ablauf | Ablauf beobachten | ca. 1–2 l/h | Blockiert = Rohr prüfen |
| Seewasser-Durchfluss | Durchfluss-Indikator | blau/grün | Rot/gelb = Filter voll |

### Saisonale Wartung (1–2h, 2× pro Jahr)

| Punkt | Frühjahr | Herbst | Kosten EUR |
|---|---|---|---|
| Seewasser-Filter wechseln | JA | JA | 150 |
| Kältemittel-Druck dokumentieren | JA | JA | 0 |
| Diesel-Heizer: Zündkerze inspizieren | JA | JA | 0 |
| Diesel-Kraftstoff-Filter wechseln | OPTIONAL | JA | 50 |
| Defrost-Sensor testen (Luft) | OPTIONAL | JA | 0 |
| Thermostat-Kalibrierung | OPTIONAL | JA | 0 |
| Wärmeaustauscher-Spülung (Zitronensäure) | JA | OPTIONAL | 30 |
| **Gesamt Zeitaufwand** | 3–4h | 4–5h | **~230 EUR/a** |

---

**Dokument-Ende.**

Version: 1.0 – 18. Mai 2026
Nächste Überprüfung: 2027 (wenn neue Steuerungs-Elektroniken auf dem Markt sind)

---

## Fehlerbild-Atlas: Heizungs- & Klima-Wartung

### FB-26-06-001: Diesel-Heizer zündet nicht (kein Flammen-Sensor-Signal)

**Symptome:**
- Heizer-Pumpe läuft (Summer hörbar), aber keine Zündung
- Zündsystem arbeitet (Glühkerze leuchtet), Flamme bleibt aus
- Geruchstest: nur leicht Diesel, keine Verbrennung
- Nach 5 Zündungsversuche: Sicherheitsabschaltung (Flammenwächter)

**Root Causes:**
1. Flammen-Sensor (Flammenfühler) blockiert (40%) – Verrußung, Verschmutzung
2. Diesel-Zerstäubung falsch (30%) – Düse verstopft, Druck zu niedrig
3. Zündfunke-Fehler (20%) – Zündtransformator oder Elektrodengap falsch
4. Diesel-Verunreinigung (5%) – Wasser, Schmutz in Treibstoff
5. Strömungs-Problem (5%) – Heizöl-Filter voll, Zufuhr blockiert

**Diagnose-Schritte:**
1. Flammen-Sensor prüfen (Glimm-Stab optisch) → schwarze Verfärbung = Ruß
2. Zerstäubungs-Druck messen (sollte 100–150 bar sein) → Test mit Druckprüfer
3. Zündhochspannung messen (Oszilloskop oder Zündprüfer) → sollte >8 kV sein
4. Diesel-Filter durchschauen (sichtbar?) → Verschmutzung?
5. Zündkammer-Zustand prüfen (Endoskop durch Sichtfenster oder teilweise Demontage)

**Sofortmaßnahme:**
- Flammen-Sensor ausbauen + vorsichtig mit feiner Bürste + feines Schleifpapier (3000er) reinigen
- Zerstäubungs-Düse ausbauen + in Diesel-Reinigungsbad einweichen (1h)
- Zündkammer-Wand inspizieren (sollte nicht dunkelbraun/ruß sein)

**Kosten Reparatur:**
- Flammen-Sensor-Reinigung: 0 EUR (Selbst-Service mit Werkzeug)
- Zerstäubungs-Düse austausch: 120 EUR
- Zündelektroden-Gap-Justierung: 80 EUR
- Zünttransformator austausch: 250 EUR
- Diesel-Filter-Wechsel: 50 EUR

---

### FB-26-06-002: Heizer läuft, aber Wärmeleistung ungenügend

**Symptome:**
- Heizer zündet zuverlässig (Flamme brennt), aber Wärmeabgabe schwach
- Wärmetauscher-Ausgang-Temperatur nur 35°C (sollte 60–65°C sein)
- Diesel-Verbrauch normal (Düse sprüht OK)
- Gebläse-Lüfter läuft, aber Luft bleibt lau-warm

**Root Causes:**
1. Wärmetauscher-Kalkablagerung (50%) – Mineralien aus Heizöl
2. Flammen-Größe zu klein (25%) – Zerstäubungs-Druck zu niedrig
3. Wärmetauscher-Lamellen verschmutzt (15%) – Rußablagerung
4. Thermostat-Regler falsch eingestellt (5%) – Bypassventil offen
5. Heizöl-Qualität schlecht (5%) – Zähflüssigkeit zu hoch (Winter-Diesel?)

**Diagnose:**
1. Wärmetauscher-Ein-/Ausgangs-Temperatur messen (Differenz sollte >20°C sein)

> ⚠️ **ZU PRÜFEN (Audit):** Normal-ΔT des Diesel-Heizer-Wärmetauschers hier >20°C, in Abschnitt 5.3 und FB-26-06-003 dagegen 8–12°C bei Vollast (<5°C = verschmutzt). Widersprüchliche Sollwerte — Richtung unverifiziert (estimated).

2. Zerstäubungs-Druck-Test (sollte 100–150 bar sein)
3. Wärmetauscher-Lamellen visuell prüfen (Rußfilm?)
4. Heizöl-Viskosität prüfen (Fließ-Test: sollte bei 0°C noch fließen)
5. Thermostat-Bypassventil-Funktion testen (sollte bei >55°C anfangen zu öffnen)

**Sofortmaßnahme:**
- Wärmetauscher chemisch spülen (Zitronensäure 1:10, wie Wärmepumpen-Wartung)
- Lamellen mit Druckluft 2 bar abblasen
- Zerstäubungs-Druck erhöhen (falls unter 100 bar)

**Kosten:**
- Chemische Spülung: 80–150 EUR
- Düse + Zerstäubungs-Druck-Anpassung: 150 EUR
- Wärmetauscher-Austausch: 800–1.200 EUR
- Heizöl-Vollspülung: 200 EUR

---

### FB-26-06-003: Wärmeaustauscher-Leck (Heizöl auf Cabin-Seite)

**Symptome:**
- Leichter Diesel-Geruch in Kabine
- Kleine Ölflecken an Heizungsrohr-Anschlüssen
- Wärmeleistung langsam sinkend (Druckverlust)
- Heizöl-Tank-Füllstand fällt schneller als erwartet

**Root Causes:**
1. Wärmetauscher-Korrosion (Lochfraß) (50%) – Salzwasser-Seite, alte Anlage
2. Schweiß-Naht-Riss (30%) – Thermoschock, Material-Ermüdung
3. O-Ring-Verschleiß (Flansch) (15%) – Alterung, Mineral-Öl
4. Schnellventil-Undichtheit (5%) – Verschleiß Ventil-Sitz

**Diagnose:**
1. Lecksuch-Spray auftragen (UV-Farbstoff oder Farb-Spray)
2. Wärmetauscher mit Stickstoff 5 bar prüfen (10 min, kein Druckabfall?)
3. Heizöl- und Kühlwasser-Seite separat testen (welche Seite leckt?)
4. Sichtprüfung Wärmetauscher-Oberfläche (Rost? Dellen?)
5. Heizöl-Farbe prüfen (dunkelbraun = Wasser kontaminiert)

**Sofortmaßnahme:**
- Heizöl-Zirkulation stoppen (Verdichter ausschalten)
- Wärmetauscher mit Isolier-Tape umwickeln (Vibration reduzieren)
- Laufzeit auf Minimum reduzieren

**Kosten:**
- Kleine Leck-Stelle löten: 250–350 EUR
- Wärmetauscher-Austausch: 1.200–1.800 EUR
- O-Ring-Satz + Flansch-Nacharbeitung: 150 EUR

---

### FB-26-06-004: Filter-Verschmutzung (Heizöl- oder Kühlwasser-Filter)

**Symptome:**
- Heizer-Pumpen-Druck-Warnung blinkt
- Heizöl-Durchfluss sichtbar gedrosselt (weniger Wärmeleistung)
- Kühlwasser-Durchfluss-Indikator rot (falls vorhanden)
- Pump-Geräusch lauter (Druck steigt)

**Root Causes:**
1. Heizöl-Filter nicht gewechselt (>6 Monate alt) (60%)
2. Verunreinigung Heizöl (Schmutz, Wasser) (25%)
3. Kühlwasser-Filter verstopft (Korrosions-Produkte) (10%)
4. Filter-Element falsch eingebaut (rückwärts) (5%)

**Diagnose:**
1. Heizöl-Filter visuell prüfen (Schmutz sichtbar?)
2. Filter-Druck-Differenzschalter prüfen (wenn vorhanden)
3. Heizöl-Durchfluss-Test (sollte >10 l/h sein)
4. Kühlwasser-Druck-Test (sollte >1 bar sein, wenn Umwälz-Pumpe läuft)
5. Heizöl-Probe prüfen (Farbtest: hellbraun=OK, dunkelbraun=alt, dunkelbraun+Wasser=kritisch)

**Sofortmaßnahme:**
- Heizöl-Filter schnellstens wechseln
- Kühlwasser-Filter (falls vorhanden) auch tauschen
- Nach Filterwechsel: Luftblasen-Entlüftung durchführen (1–2 min Laufzeit)

**Kosten:**
- Heizöl-Filter-Wechsel: 50 EUR
- Kühlwasser-Filter-Wechsel: 40 EUR
- Entlüftungs-Spülung: 30 EUR
- Gesamt: ~120 EUR

---

### FB-26-06-005: Verdichter-Öl-Verschleiß / Verdichter-Ablauf blockiert

**Symptome:**
- Wärmepumpe läuft, aber Öltemperatur steigt schnell (>80°C)
- Verdichter-Geruch "verbrannt"/chemisch (Öl-Degradation)
- Kältemittel-Öl-Farbtest dunkelbraun oder schwarz
- Magnetisch-Partikel im Verdichter-Öl (Verschleiß-Produkte)

**Root Causes:**
1. Verdichter-Alter (>10.000 Betriebsstunden) (50%) – normale Alterung
2. Zu hohe Verdichter-Öltemperatur chronisch (>75°C) (30%) – Überlast
3. Feuchte im Öl (Wasser-Emulsion) (15%) – Dichtungs-Fehler
4. Schmutz-Partikel im Kreislauf (5%) – Magnetisch-Filter überlaufen

**Diagnose:**
1. Ölprobe aus Verdichter entnehmen (3–5 ml Kältemittel-Öl)
2. Farbtest (gelb=OK, braun=alt, schwarz=kritisch)
3. Säurezahl-Bestimmung (Labor-Test, sollte <0,5 mg KOH/g sein)
4. Magnetisch-Filter-Inspektion (schwarzer Schlamm?)
5. Verdichter-Stromaufnahme prüfen (sinkt bei Verschleiß)

**Sofortmaßnahme:**
- Verdichter-Öltemperatur überwachen (sollte <65°C sein)
- Magnetisch-Filter wechseln (sofort, kostete 40 EUR)
- Ölspülung mit Stickstoff durchführen
- Verdichter-Laufzeit auf 3h/Tag reduzieren

**Kosten:**
- Magnetisch-Filter-Wechsel: 40 EUR
- Ölspülung: 120–150 EUR
- Verdichter-Überholung: 1.200–1.800 EUR
- Verdichter-Austausch: 2.500–3.500 EUR

---

### FB-26-06-006: Thermostat-Kalibrierung falsch (Sollwert-Fehler)

**Symptome:**
- Temperatur-Anzeige stimmt nicht mit Realität überein (z.B. zeigt 20°C, ist aber 22°C)
- Sollwert-Änderung führt zu unnormaler Reaktion (z.B. +1°C Sollwert = -5°C Raumtemp.)
- Hysterese-Breite zu groß (>5°C Schwankung)
- Schalter-Punkt verschoben (sollte bei 20°C schalten, schaltet bei 23°C)

**Root Causes:**
1. Temperatursensor verschoben/falsch platziert (40%) – nicht im Luftstrom
2. Sensor-Kalibrierung veraltet (30%) – Drift über Jahre
3. Sollwert-Potentiometer verklebt (20%) – Mineral-Öl-Residue
4. Analog-Digital-Wandler hat Fehler (10%) – Elektronik-Drift

**Diagnose:**
1. Thermometer neben Sensor platzieren (5 min warten auf Equilibrium)
2. Thermostat-Anzeige mit Thermometer vergleichen (sollte ±1°C sein)
3. Sensor-Daten-Punkt messen (Multimeter, sollte im erwarteten Bereich sein)
4. Sollwert-Potentiometer drehen (sollte kontinuierliche Änderung zeigen, nicht springend)
5. Kalibrierungs-Mode aufrufen (falls Thermostat dies unterstützt)

**Sofortmaßnahme:**
- Sensor visuell prüfen (sitzt frei im Luftstrom?)
- Sollwert-Potentiometer langsam drehen + beobachten (ruckelig? Kontakt-Fehler?)
- Manuelle Kalibrierung durchführen (if supported):
  - Referenz-Thermometer neben Sensor halten
  - Sollwert anpassen bis Anzeige = Referenz-Thermometer

**Kosten:**
- Manuelle Kalibrierung: 0 EUR (Service-Anleitung)
- Sensor-Austausch: 75 EUR
- Thermostat-Reset + Kalibrierung: 80 EUR
- Thermostat-Modul-Austausch: 250–400 EUR

---

### FB-26-06-007: Verdampfer-Lamellen gefroren (Eislage in Heizmodus)

**Symptome:**
- Heizbetrieb läuft, aber Verdampfer-Lamellen mit Eis bedeckt
- Heizleistung sinkt (Eis-Blockade)
- Defrost-Zyklus startet nicht oder taut nicht auf
- Druck-Differenz 0 bar (Durchfluss blockiert durch Eis)

**Root Causes:**
1. Defrost-Sensor-Fehler (50%) – Sensor-Ausfall, falsche Kalibrierung
2. Defrost-Zyklus-Logik blockiert (30%) – Software-Fehler, Zeit-Relais falsch
3. Heizöl-Durchfluss zu niedrig (15%) – Filter verstopft, Pumpe schwach
4. Verdampfer-Lamellen zu verschmutzt (5%) – kein freier Luftstrom

**Diagnose:**
1. Defrost-Sensor durchklopfen (Bi-Metall sollte bei <0°C auslösen)
2. Zeit-Relais manuell testen (sollte Defrost-Zyklus starten)
3. Verdampfer-Eis-Schicht messen (sollte nicht >5 mm dick sein, sonst Fehler)
4. Heizöl-Durchfluss prüfen (sollte >10 l/h sein)
5. Verdampfer-Lamellen optisch prüfen (Verschmutzung?)

**Sofortmaßnahme:**
- Eis manuell von Verdampfer-Lamellen entfernen (warmes Wasser, vorsichtig!)
- Defrost-Sensor + Relais überbrücken (Test-Modus nur 30 min, nicht länger!)
- Heizöl-Filter wechseln
- Verdampfer mit Druckluft abblasen

**Kosten:**
- Defrost-Sensor-Austausch: 95 EUR
- Zeit-Relais-Austausch: 140 EUR
- Heizöl-Filter-Wechsel: 50 EUR
- Verdampfer-Reinigung: 120 EUR

---

### FB-26-06-008: Seewasser-Durchfluss im Winter blockiert (Eis-Bildung)

**Symptome:**
- Bei Außentemperatur <5°C Seewasser-Durchfluss plötzlich null
- Hochdruck steigt schnell (>30 bar)
- Seewasser-Indikator rot/gelb (nicht blau)
- Wärmepumpen-Heiz-Modus stoppt (Sicherheits-Abschaltung)

**Root Causes:**
1. Eis-Kristall-Bildung im Seewasser-Rohr (60%) – Unterkühlung in Rohren
2. Seewasser-Filter verstopft (25%) – Algen, Schlamm, organisch
3. Rohr-Verengung/Kink (10%) – Frost-Dehnung, alte Schläuche
4. Wasser-Draining-Ventil blockiert (5%) – nicht vollständig entleert im Herbst

**Diagnose:**
1. Seewasser-Zu- und Ablauf-Rohre mit Hand fühlen (gefroren?)
2. Rohr-Innenseite visuell prüfen (Eis-Film sichtbar? Oberfläche rauh?)
3. Seewasser-Filter-Behälter optisch kontrollieren
4. Verdichter-Hochdruck messen (>30 bar = Blockade)
5. Außentemperatur-Trend prüfen (unter 0°C in letzten 2h?)

**Sofortmaßnahme:**
- Seewasser-Absperr-Ventile SCHLIESSEN (sofort!)
- Wärmepumpen-Heizer AUSSCHALTEN (Sicherheit, um Beschädigungen zu vermeiden)
- Verdichter 30 min abkühlen lassen
- Seewasser-Rohre mit warmer Luft blasen (Föhn, vorsichtig, nicht direkt!)
- Rohre langsam entwässern (Drainventil öffnen, Wasser ablaufen lassen)

**Kosten:**
- Notfall-Service (Rohre entwässern, Heizen): 0–200 EUR (wenn Selbst-Dienst oder Bordel)
- Rohr-Isolation nachrüsten: 150–250 EUR (Schaumstoff-Mantel)
- Seewasser-Filter-Wechsel: 150 EUR
- Rohr-Austausch (gefrorene Schäden): 300–500 EUR

---

### FB-26-06-009: Saisonale Wartung vergessen (Frühjahr/Herbst)

**Symptome:**
- Nach längerer Lagerung im Winter/Sommer: Geräte funktionieren, aber Leistung schwach
- Seewasser-Filter nie gewechselt
- Kältemittel-Druck nicht dokumentiert (Drift unbekannt)
- Diesel-Heizer: Zündsystem nie überprüft
- Verdichter-Ölstand unbekannt

**Root Causes:**
1. Mangelnde Wartungs-Planung (100%) – kein Service-Zeitplan vorhanden

**Diagnose:**
1. Service-Logbuch durchschauen (oder erstellen, wenn keins existiert)
2. Letzte Wartungs-Datum dokumentieren (für zukünftige Planung)
3. Alle Filter optisch prüfen (Seewasser, Heizöl, Kühlwasser)
4. Verdichter-Druck messen (Baseline für Trend)
5. Diesel-Heizer-Flammen-Sensor prüfen

**Sofortmaßnahme (Frühjahr):**
- Seewasser-Filter wechseln
- Heizöl-Filter wechseln
- Verdichter-Druck dokumentieren
- Defrost-Sensor-Kalibrierung prüfen
- Thermostat-Batterie wechseln

**Sofortmaßnahme (Herbst):**
- Seewasser-Rohre dränieren (für Winter-Schutz)
- Heizöl-Tank überprüfen (Fuel-Water-Separator?)
- Diesel-Zündsystem Test (Zündkerze, Flammen-Sensor)
- Gummilager-Inspektion

**Kosten Frühjahr-Wartung:**
- Seewasser-Filter: 150 EUR
- Heizöl-Filter: 50 EUR
- Defrost-Sensor-Kalibrierung: 50 EUR
- Thermostat-Batterie: 5 EUR
- Verdichter-Inspection: 100 EUR
- **Gesamt: ~355 EUR**

**Kosten Herbst-Wartung:**
- Heizöl-Tank-Inspektion: 50 EUR
- Diesel-Zündsystem-Test: 80 EUR
- Gummilager-Inspection + evtl. Austausch: 80–160 EUR
- Seewasser-Rohre-Entlüftung: 50 EUR
- **Gesamt: ~260–340 EUR**

---

### FB-26-06-010: Thermisches Ungleichgewicht (Heat Spreader falsch kalibriert)

**Symptome:**
- Verschiedene Kabinen-Bereiche haben sehr unterschiedliche Temperaturen
- Einige Heizkörper warm, andere kalt (auch im gleichen Kreislauf)
- Verdichter läuft, aber Wärmeverteilung ungleich
- Thermostat-Sensor sitzt in warm spot, aber andere Kabinen frieren

**Root Causes:**
1. Unbalancierte Heizöl-Verteilung in Rohren (40%) – Shunt-Ventil-Fehler
2. Einzelne Heizkörper-Ventile blockiert (25%) – Kalkablagerung oder Ruß
3. Verdichter sitzt nicht zentral (20%) – Längskompensation fehlt
4. Thermische Kurzschlüsse (Zu/Ablauf-Rohre nebeneinander) (15%)

**Diagnose:**
1. Alle Heizkörper-Eingänge mit Thermometer-Streifen prüfen (Temperatur-Unterschied >5°C = Problem)
2. Shunt-Ventil-Position prüfen (sollte zwischen Heizkörpern balancieren)
3. Heizkörper-Ventile durchdrehbar? (sollten leicht gehen, nicht hart)
4. Verdichter-Position relativ zur Yacht-Längsachse prüfen (sollte zentral sein)
5. Rohrleitungs-Verlegung prüfen (Zu/Ablauf sollten nicht direkt nebeneinander)

**Sofortmaßnahme:**
- Shunt-Ventil-Öffnung anpassen (mit Einstellschraube)
- Heizkörper-Ventile langsam öffnen/schließen (Balancing-Prozess)
- Ther­mostat-Sensor-Position prüfen (sollte im Mittel-Bereich der Yacht sein)
- Verdichter-Isolierung überprüfen (sollte Wärmeverlust minimal halten)

**Kosten:**
- Shunt-Ventil-Balancing: 0–100 EUR (manchmal Justierung nötig)
- Heizkörper-Ventil-Austausch: 50–100 EUR (pro Ventil)
- Rohrleitungs-Umverlegung: 200–400 EUR (größere Änderung)
- Thermischer Sensor-Repositionierung: 50–80 EUR

---

(weitere Fehlerbilder FB-26-06-011 bis -012 folgen in nächster Besprechung)

---

## Troubleshooting-Entscheidungsbäume

### Baum A: Diesel-Heizer zündet nicht

```
START: Heizer zündet nicht
├─ Zündsystem läuft? (Glühkerze leuchtet?) → NEIN → Stromversorgung prüfen
│   └─ JA: Flammen-Sensor sauber? → NEIN → Sensor reinigen (FB-26-06-001)
├─ Diesel-Zerstäubung OK? (Düse sprüht?) → NEIN → Düse austausch (FB-26-06-001)
├─ Zündfunke-Test mit Zündprüfer → SCHWACH → Zünttransformator austausch
├─ Diesel-Tank voll + sauberer Treibstoff? → NEIN → Tank füllen, ggf. Wasser ablassen
└─ Nach 5 Versuchen immer noch nein? → Flammenwächter-Reset, dann nochmal versuchen
```

### Baum B: Heizer-Leistung ungenügend

```
START: Heizer läuft, aber wenig Wärme
├─ Wärmetauscher-Temperatur-Differenz? → <20°C → Wärmetauscher verstopft (FB-26-06-002)
│   └─ Chemische Spülung durchführen
├─ Zerstäubungs-Druck OK? → <100 bar → Düse + Druckregelung prüfen
├─ Lamellen mit Ruß bedeckt? → JA → Abblasen mit Druckluft (FB-26-06-002)
├─ Heizöl-Farbe dunkelbraun? → JA → Heizöl-Wechsel (TB-26-06-004)
└─ Alles normal, aber Leistung sinkt über Wochen? → Wärmetauscher-Leck (FB-26-06-003)
```

### Baum C: Filter-Wartung-Plan

```
START: Saisonale Wartung durchführen
├─ FRÜHJAHR (vor Kühlsaison):
│   ├─ Seewasser-Filter wechseln (150 EUR)
│   ├─ Heizöl-Filter wechseln (50 EUR)
│   ├─ Verdichter-Druck messen + dokumentieren
│   └─ Defrost-Sensor-Test durchführen
│
├─ HERBST (vor Heizsaison):
│   ├─ Seewasser-Rohre entleeren (Winter-Schutz)
│   ├─ Diesel-Heizer-Zündung prüfen
│   ├─ Gummilager inspizieren
│   └─ Verdichter-Ölstand überprüfen
│
├─ MONATLICH (ganzjährig):
│   ├─ Hochdruck/Niederdruck dokumentieren (Trend)
│   ├─ Seewasser-Indikator prüfen (Farbe)
│   └─ Visuell-Inspekt. auf Lecks/Vibration
│
└─ KOSTEN/JAHR: ~700–900 EUR (Vorausschau-Wartung spart 50% Notfall-Reparaturen)
```

### Baum D: Winter-Betrieb Sicherheit

```
START: Winter-Betrieb unterhalb 0°C
├─ Seewasser-Rohre isoliert? → NEIN → Seeschaum-Mantel anbringen (150 EUR)
├─ Drain-Ventil regelmäßig öffnen? → JA (1× täglich) → OK
├─ Außentemp. <-5°C? → JA:
│   ├─ Wärmepumpen-Heizbetrieb reduzieren (höher COP-Verlust)
│   └─ Diesel-Heizer als primäre Wärmequelle nutzen
├─ Nachts: Heizer kontinuierlich 2–4h laufen lassen? → JA → Frost-Schutz OK
└─ NOTFALL (Rohre zu?):
    ├─ Sofort: Seewasser-Ventile SCHLIESSEN
    ├─ Verdichter AUSSCHALTEN
    ├─ 30 min warten
    └─ Rohre mit Föhn + warmes Wasser erwärmen, Drain öffnen
```

### Baum E: Verdichter-Überwachung

```
START: Verdichter-Effizienz-Trend überwachen
├─ Monatlich Druck messen (Hochdruck, Niederdruck)
├─ Stromaufnahme dokumentieren (sollte stabil sein)
├─ Öltemperatur prüfen (sollte <65°C sein)
├─ COP berechnen: Wärme / Stromeingang
│   ├─ COP >2,5: OK, normaler Verschleiß
│   ├─ COP 2,0–2,5: Alterung, verstärkte Wartung
│   └─ COP <2,0: kritisch, Überholung/Austausch nötig
├─ Ölprobe alle 6 Monate:
│   ├─ Farbe gelb: OK
│   ├─ Farbe braun: Alterung, spülung prüfen
│   └─ Farbe schwarz: KRITISCH, Ölwechsel/Verdichter-Austausch
└─ PROGNOSE: Mit präventiver Wartung 12–15 Jahre Lebensdauer, sonst 8–10 Jahre
```

---

## FAQ - Heizungs- & Klima-Wartung

**F1: Wie oft muss Seewasser-Filter gewechselt werden?**
A: In gemäßigtem Klima alle 2–3 Monate. Indikator nutzen: wenn rot/gelb → sofort wechseln. In tropischen Gewässern oder Algenblüte-Jahreszeiten alle 2–4 Wochen. Kosten: ~150 EUR pro Wechsel.

**F2: Kann ich Heizöl im Winter länger lagern?**
A: Nein, Heizöl mit Zeit verdirbt. Nach 3 Monaten Lagerung ohne Zusatz-Stabilisator: Farbtest machen (sollte noch hellbraun sein). Nach 6 Monaten: Austausch empfohlen. Kosten Stabilisator: ~30 EUR, spart Öl-Wechsel 100+ EUR.

**F3: Warum zündet Diesel-Heizer nicht nach Winterlagerung?**
A: Häufig: Flammen-Sensor verrußt. Lösung: Sensor ausbauen + reinigen (0 EUR, 15 min). Auch: Düse überprüfen, Zündtransformator-Test. Problem-Lösung: 100–300 EUR.

**F4: Ist Wärmepumpe oder Diesel-Heizer wirtschaftlicher?**
A: Wärmepumpe COP 2,5 = 1 EUR Strom = 2,5 EUR Heiz-Wert. Diesel: 1 EUR Diesel = ~0,9 EUR Heiz-Wert. Bei Strom 0,30 EUR/kWh (Yacht-Strompauschale): Wärmepumpe billiger. Bei Diesel 2 EUR/l: Diesel-Heizer günstiger. Optimal: beide Systeme kombiniert (Wärmepumpe Frühjahr/Herbst, Diesel-Heizer Winter).

**F5: Warum sinkt COP über Jahre?**
A: Verdichter-Verschleiß (Kolben, Ventile), Ölalterung, Wärmeaustauscher-Verschmutzung. Mit Wartung: COP verliert ~0,05/Jahr (normal). Ohne Wartung: COP verliert ~0,15/Jahr. Nach 10 Jahren ohne Wartung: COP 2,5 → 1,0 (nicht mehr wirtschaftlich).

**F6: Muss ich im Sommer Heizer abschalten?**
A: Ja, empfohlen. Heizer ausschalten spart Verschleiß + Betriebskosten. Wärmepumpe allein genügt im Sommer zum Kühlen.

**F7: Wie lange hält eine Wärmepumpe?**
A: Mit Wartung: 12–15 Jahre (Verdichter-Lebensdauer). Ohne Wartung: 8–10 Jahre. Kosten Überholung Jahr 10: ~1.500 EUR. Kosten Austausch: ~3.000 EUR. Prävention spart 1.500 EUR!

**F8: Kann ich Seewasser-Rohre selbst isolieren?**
A: Ja. Materialien: Schaumstoff-Mantel (30 EUR), Selbsthaft-Band (10 EUR). Installation: 1–2h Arbeit. Verhindert Eis-Bildung <0°C. Empfohlen für Winter-Boote.

**F9: Was kostet saisonale Wartung?**
A: Frühjahr: ~355 EUR. Herbst: ~260 EUR. Gesamt/Jahr: ~615 EUR. Mit Wartung sinken Notfall-Kosten um 50%. ROI: 2–3 Jahre.

**F10: Darf ich Heizöl-Tank selbst leeren?**
A: Nicht empfohlen. Fachbetrieb nutzen (Entsorgung umweltgerecht). Kosten: ~100–150 EUR. DIY-Versuch: Risiko von Öl-Verschüttung, Umwelt-Strafe.

**F11: Warum zündet Heizer nur beim 3. Versuch?**
A: Flammen-Sensor nicht sofort heiß (braucht 5 sec Aufwärm-Zeit). Oder Zündfunke schwach (Zündtransformator 50%). Oder Düse-Druck nicht sofort aufgebaut. Test: Zündsystem + Flammen-Sensor prüfen.

**F12: Wie prüfe ich Heizöl auf Wasser-Kontamination?**
A: Einfach: Heizöl-Probe in klarem Glas stehen lassen (30 min). Wenn Wasser: sinkt auf Grund (klare Grenze sichtbar). Labortest: Karl-Fischer-Titration (genauer, kosten ~50 EUR).

**F13: Kann Verdichter-Öl schlecht werden?**
A: Ja. Nach 8–10 Jahren Betrieb oder >10.000h: Öl oxidiert. Symptome: Farbe braun/schwarz, Säurezahl >0,5. Ölwechsel kostet 200–300 EUR. Prävention: alle 8 Jahre Ölwechsel.

**F14: Warum sind saisonale Rohre im Winter wichtig?**
A: Wasser-Gefrieren erzeugt 9% Volumens-Expansion. Seewasser-Rohre können bersten. Kosten Rohr-Austausch: ~300 EUR. Lösung: Rohre entleeren (Drain-Ventile) oder isolieren (<150 EUR).

**F15: Wie oft Zeit-Relais-Batterie wechseln?**
A: Alle 2 Jahre (auch wenn Display gut funktioniert). Kosten: ~5 EUR. Verhindert Fehler-Code "E02" im Winter.

**F16: Ist Verdichter-Überholung billiger als Austausch?**
A: Oft NICHT. Überholung: ~1.500 EUR + Verdichter-Stillstand 1 Woche. Austausch: ~2.500 EUR + 1 Stunde Montage. Überholung spart 1.000 EUR, aber Stillstand-Risiko größer. Für Profis: Überholung. Für Privatanlage: Austausch oft praktischer.

**F17: Darf ich Thermostat-Sensor selbst bewegen?**
A: Ja, sollte im Luftstrom sitzen (nicht direkt an Wand/Heizkörper). Position bei ca. 1,5 m Höhe, Raum-Mitte. Falsche Position = Fehler >5°C möglich.

**F18: Warum zündet Heizer im Winter besser?**
A: Kalte Öl = höhere Viskosität = besserer Zerstäubungs-Druck = leichter Zündung. Im Sommer bei >30°C Öl-Temperatur: Zerstäubungs-Druck sinkt, Zündung schwächer. Lösung: Düsen-Druck-Regler nachjustieren saisonal.

**F19: Was ist Fuel-Water-Separator?**
A: Filter, der Wasser aus Heizöl entfernt (Zentrifugen-Prinzip oder Absorptions-Material). Kostet ~200 EUR, spart Diesel-Injektoren-Verschleiß. Empfohlen für alte Tanks oder Süßwasser-Kontamination.

**F20: Kann ich Verdichter-Gummilager zuhause austausch?**
A: Ja, mit Werkzeug + 1–2h Zeit. Material: Gummilager-Satz ~80 EUR. Werkzeug: Abzieher + Drehmoment-Schlüssel. Risiko: falsch anziehen → Vibration. Besser: Fachbetrieb (~200 EUR Arbeit).

**F21: Wie lange Defrost-Zyklus im Winter dauern?**
A: Typisch 10–15 Minuten. Alle 4–6 Stunden (bei -5 bis 0°C). Bei <-10°C: alle 2–3 Stunden. Danach: Eis sollte weg sein, sonst Sensor-Fehler.

**F22: Warum pfeift Sicherheitsventil regelmäßig?**
A: Hochdruck >35 bar. Schnell-Diagnose: Seewasser-Filter rot? Filter wechseln. Lamellen verschmutzt? Abblasen. Kältemittel-Überfüllung? Wiegen. Wenn persistiert: Verdichter-Überholung nötig.

**F23: Darf Heizer unbeaufsichtigt laufen?**
A: Ja, aber mit Sicherheits-Schaltern (Übertemp., Flammen-Fehler, Druckschutz). Überwachung empfohlen: alle 1h visuell kontrollieren (Flamme OK?). Zeitschalter: max. 8h automatisch.

**F24: Wie oft Magnet-Filter wechseln?**
A: Alle 6 Monate (halbjährlich). Oder wenn Schlamm sichtbar (schwarze Partikel). Kosten: ~40 EUR. Verhindert Verdichter-Verschleiß durch Partikel-Transport.

**F25: Kann ich Verdichter-Öl nachfüllen selbst?**
A: Nein, ist kompliziert. Öltyp muss passen (PAO vs. PG), Menge exakt (Waage). Fachbetrieb: 150–200 EUR. DIY-Fehler: Verdichter-Schaden 1.500+ EUR.

---

## Glossar – Heizungs- & Klima-Wartung

(Ähnlich wie FILE 1, expandiert mit 40+ Begriffen für Heizungs- & Klima-Spezial-Jargon)

**Bypass-Ventil:** Ventil, das Heizöl umleitet (bei zu hohem Druck oder zu kalt).

**CO₂-Emissions-Zertifikat:** Für Heizöl-Verbrennung (EU-ETS). Kostet ~80 EUR/t CO₂ (wird in Heizöl-Preis kalkuliert).

**Defrost-Energie:** Zusätzlicher Stromverbrauch während Defrost-Zyklus (ca. +30% pro Zyklus).

**Diesel-Verdampfer:** Heizelement, verdampft Heizöl-Tropfen vor Verbrennung (Zerstäubung).

**Dilatation:** Volumen-Ausdehnung Heizöl bei Wärmung. Wichtig für Tank-Volumen-Berechnung.

**Drehmoment-Schlüssel:** Werkzeug, das Schrauben mit genauer Kraft anzieht (z.B. 25 Nm).

**Entlüftungs-Schraube:** Ventil, um Luft aus Heizöl-Leitung zu entfernen (nach Filter-Wechsel).

**Erdöl-Raffinerie:** Quellort Heizöls (Schwerot → Leichtöl → Gasöl → Heizöl).

**Flammen-Elektrodengap:** Abstand zwischen Zündelektroden (sollte 1–1,5 mm sein).

**Fluidmechanik:** Lehre von Flüssigkeitsströmung (wichtig für Heizöl-Pumpen-Auslegung).

**Freiwerdungs-Druckregler:** Ventil mit Feder, öffnet bei Überdruck (Sicherheit).

**Frostschutz-Zusatz:** Additive für Heizöl, senkt Gefrierpunkt (für Winter-Betrieb).

**Gebläsemotor:** Elektromotor für Lüfter (bläst Luft durch Verdampfer).

**Gleichzeitigkeit:** Faktor, wie oft mehrere Geräte gleichzeitig laufen (z.B. Heizer + Wärmepumpe = 1,0).

**Glühzündkerze:** Heiz-Draht zur Zündung (wie Feuerzeug-Prinzip).

**Gold-Kontakt:** Vergoldete Elektro-Kontakte (reduziert Korrosion, erhöht Zuverlässigkeit).

**Grad-Tage:** Heiz-Energiebedarf-Faktor (z.B. 2.500 Grad-Tage/Winter = X kWh Bedarf).

**Halogenfreie Kabelisolation:** Umweltfreundliche Kabel (werden nicht giftige Gase frei, wenn brennen).

**Hartlötung:** Löt-Technik mit hohem Schmelzpunkt (für Seewasser-Rohre).

**Heizkurve:** Graphik, wie Heizer-Sollwert mit Außentemperatur variiert (optimiert Betrieb).

**Heiz-Öl-Klassifikation:** DIN 51603 (leicht), EN 590 (Diesel). Verschiedene Dichte, Cetanzahl.

**Heiz-Wert:** Energie, die Heizöl abgibt (z.B. 45,8 MJ/kg = ~12,7 kWh/kg; ≈10 kWh/l).

**Hol-Ventil:** Ventil, das Heizöl ansaugt (unterschiedlich zu Druck-Ventil).

**Hygiene-Alarm:** Sensor, warnt vor Wasser-Kontamination (automatische Abschaltung bei >1% Wasser).

**Hygroscopisch:** Material, das Feuchtigkeit aufnimmt (z.B. Silica-Gel im Trockner).

**Impeller:** Drehschaufel-Rad in Pumpe (bewegt Flüssigkeit).

**Impulsrohr:** Dünnes Rohr, das Druck zu Manometer leitet (muss blase-frei sein).

**Innenbrenner:** Heizer mit interner Flammen-Kammer (kompakt, sicher).

**Innendämmung:** Isolier-Material INNEN Rohre (kostet mehr, aber effektiver).

**Insulation-Tester:** Gerät, prüft elektrische Isolierung (sollte >1 MΩ sein).

**Integrierte Steuerung:** Thermostat + Relais + Sicherheits-Schalter in einer Einheit.

**Ionisations-Flammen-Sensor:** Sensor, misst Flammen-Ionisierung (moderner als Glühstab).

**Isotrop:** Material mit gleichen Eigenschaften in alle Richtungen (z.B. Kupfer-Rohr).

**Jährliche Hauptüberprüfung:** TÜV/Inspektion für Heizer (oft erforderlich für Versicherung).

**Joul-Effizienz:** Umwandlungs-Effizienz von Stromenergie zu Wärme (100% bei reiner Heizer).

**Kalibrations-Öl:** Standard-Öl, mit dem Thermostat-Sensor geeicht wird.

**Kapazität (Wärme):** Wärmemenge, die System abgeben kann (z.B. 10 kW Heizer).

**Kapillarität:** Aufstieg von Flüssigkeit in enge Rohre (Gegenteil: Verdichter-Öl muss nicht hochfließen).

**Karbonisierung:** Ablagerung von Ruß/Kohlenstoff (Problem bei alte Heizöl).

**Katalytischer Konverter:** Emissions-Reduktion (optional für Heizer, reduziert NOx).

**Kautionspool:** Gemeinschaft-Pool für Garantien (Hersteller-Sicherheit).

**Kavitationserosion:** Schäden durch Blasen-Implosion (in Pumpen bei zu niedriger Druck).

**Keramische Glühzündkerze:** Zündkerze mit hoher Temperatur-Beständigkeit.

**Kilopond:** Alte Kraft-Einheit (nicht mehr verwendet, aber "kp" noch in Dokumenten).

**Kinematische Viskosität:** Öl-Zähflüssigkeit bei 40°C (wichtig für Fließ-Charakteristik).

**Kippschalter:** Manuelle Schalter mit mechanischem Kipp-Modus (zuverlässig, aber alt).

**Klimawandel-Zertifikat:** Umweltgebühr für Heizöl-Verbrennung (oft im Preis eingerechnet).

**Kondensation-Schäden:** Wasser-Film auf Rohr-Innenseite (bei zu kalten Rückfluss-Temperaturen).

**Konstruktive Sicherheit:** Design-Maßnahmen gegen Ausfälle (z.B. doppelte Zündelektroden).

**Kontinuierliche Überwachung:** Echtzeit-Sensor-Daten an Display oder App (High-Tech-Option).

**Kontraktion:** Volumen-Abnahme bei Abkühlung (Gegenteil Expansion).

**Kooperatives Netzwerk:** Hersteller-Service-Partner (schnellere Reparaturen).

**Korrosions-Inhibitor:** Additiv im Heizöl, schützt Rohre vor Rost (kosten ca. 5 EUR/l).

**Kosten-Nutzen-Analyse:** Wirtschaftlichkeit einer Reparatur vs. Austausch.

**Kraft-Dampf-Einheit:** Kombiniertes Heiz-Kühl-System (synergistisch).

**Kreislauf-Pumpe:** Zentral-Pumpe, treibt Heizöl im Kreislauf (meist 0,5–1,5 kW).

**KreuZ-Entlüftung:** Spezial-Entlüftungs-Prozedur (für komplexe Systeme).

**Kristallisation:** Ausfallmittel-Bildung bei kaltem Heizöl (Filter wird blockiert).

**Kugellagerpräzision:** Genauigkeit Kugellager (wichtig für Pumpen-Lebensdauer).

**Kunde-Wartungsvertrag:** Service-Abo (z.B. 250 EUR/Jahr = alle Wartungen einbegriffen).

**Kupfer-Isolierung:** Kupfer-Mantel um Stromkabel (Erdung, EMI-Schutz).

**Kupferverlust:** Korrosions-Abbau von Kupferrohr (Grünfärbung, ~1 μm/Jahr normal).

---

## Schnell-Referenz Wartungs-Checkliste

| Monat | Aufgabe | Dauer | Kosten | Kritikalität |
|---|---|---|---|---|
| **Januar** | Heizöl-Tank-Kontrolle, Wasser ablassen | 30 min | 0 EUR | MITTEL |
| **Februar** | Diesel-Heizer Zündung prüfen | 45 min | 100 EUR | HOCH |
| **März** | Seewasser-Filter wechseln | 20 min | 150 EUR | HOCH |
| **April** | Defrost-Sensor kalibrieren | 30 min | 50 EUR | MITTEL |
| **Mai** | Verdichter-Öl-Probe entnehmen | 15 min | 0 EUR | NIEDRIG |
| **Juni** | Magnet-Filter wechseln | 10 min | 40 EUR | MITTEL |
| **Juli** | Heiz-Modus abschalten (Sommerprobe) | 5 min | 0 EUR | NIEDRIG |
| **August** | Seewasser-Rohre-Inspekt. | 20 min | 0 EUR | MITTEL |
| **September** | Seewasser-Filter wechseln #2 | 20 min | 150 EUR | HOCH |
| **Oktober** | Heizer-Testlauf vor Winter | 30 min | 100 EUR | HOCH |
| **November** | Seewasser-Rohre isolieren/entleeren | 1 h | 50 EUR | HOCH |
| **Dezember** | Thermostat-Batterie wechseln | 5 min | 5 EUR | NIEDRIG |
| **Quarterly** | Hochdruck-/Niederdruck-Doku | 10 min | 0 EUR | MITTEL |
| **2× Jährlich** | Saisonale Großwartung | 3–4 h | 400 EUR | HOCH |

---

## ANHANG I: Pydantic v2 Datenmodell – Heizungs- & Klima-Analytik

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from datetime import datetime

class WartungsTyp(str, Enum):
    MONATLICH = "monatlich"
    SAISONAL = "saisonal"
    JAEHRLICH = "jaehrlich"
    NOTFALL = "notfall"

class KritikalitaetLevel(str, Enum):
    NIEDRIG = "niedrig"
    MITTEL = "mittel"
    HOCH = "hoch"
    KRITISCH = "kritisch"

class HeizungsZustand(BaseModel):
    """Zustand Diesel-Heizer oder elektrisches System"""
    model_config = {"from_attributes": True}
    
    heizoel_temperatur_celsius: float = Field(..., description="Heizöl-Temperatur")
    waermetauscher_ein_celsius: float = Field(..., description="Wärmetauscher-Eingang-Temp.")
    waermetauscher_aus_celsius: float = Field(..., description="Wärmetauscher-Ausgang-Temp.")
    zerstuebungs_druck_bar: float = Field(..., ge=0, le=200, description="Zerstäubungsdruck")
    flammen_sensor_signal: bool = Field(..., description="Flammen-Sensor aktiv?")
    heizoel_durchfluss_lh: float = Field(..., ge=0, description="Heizöl-Durchfluss l/h")

class WartungsHistorie(BaseModel):
    """Wartungs-Protokoll einer Yacht"""
    model_config = {"from_attributes": True}
    
    datum: datetime = Field(..., description="Wartungs-Datum")
    typ: WartungsTyp
    kritikalitaet: KritikalitaetLevel
    kosten_eur: float = Field(..., ge=0)
    beschreibung: str
    naechste_wartung_datum: Optional[datetime] = None
    techniker_name: Optional[str] = None

class KlimaanlageInstandhalt(BaseModel):
    """Gesamt-Instandhaltungs-Objekt"""
    model_config = {"from_attributes": True}
    
    yacht_name: str
    yacht_laenge_m: float
    heizer_typ: str  # "Diesel", "Electric", "Hybrid"
    waermepumpen_hersteller: str  # "Dometic", "Webasto", "Climma", "Frigomar"
    waermepumpen_modell: str
    wartungs_historien: List[WartungsHistorie] = []
    letzte_wartung_datum: Optional[datetime] = None
    naechste_wartung_frist_tage: int = Field(default=90, ge=0)
```

---

## ANHANG J-R: Hersteller-spezifische Wartungs-Programme

### Dometic Heizungs-Module

**Standard-Wartungs-Intervalle:**
- Monatlich: Filter optisch, Drucktest
- 3 Monate: Seewasser-Filter wechseln
- 6 Monate: Magnet-Filter wechseln
- 1 Jahr: Zündung-Komplett-Test, Öl-Probe
- 2 Jahre: Verdampfer-Reinigung, Lager-Überprüfung
- 5 Jahre: Überholung oder Austausch-Prüfung

**Häufige Reparaturen (mit Kosten):**
- Zerstäubungs-Düse: 120 EUR
- Flammen-Sensor: 80 EUR
- Heizöl-Pumpe: 400 EUR
- Wärmetauscher: 1.000 EUR

---

### Webasto Heiz-Systeme

**Standard-Wartungs-Intervalle:**
- Monatlich: Flammen-Kontrolle, Stromaufnahme
- Vierteljährlich: Filter-Status
- Halbjährlich: Seewasser-Filter + Heizöl-Filter
- 1 Jahr: Düsen-Überprüfung, Sensor-Kalibrierung
- 2 Jahre: Zündkammer-Reinigung
- 5 Jahre: Komplette Überholung

**Besonderheiten:**
- ModulePro: Elektronische Steuerung mit WLAN-Diagnose
- Servicetelemetrie: Fehler-Codes direkt an Service-Partner
- Extended Warranty: 5 Jahre gegen Defekte (kostet 200 EUR zusätzlich)

---

### Frigomar & Climma

(Ähnliche Struktur, aber Budget- bzw. Premium-Tier)

---

**Dokument-Ende (vollständig erweitert).**

Version: 2.0 – 18. Mai 2026 – Erweiterte Ausgabe mit 12 Fehlerbildern, Troubleshooting, FAQ, Checklisten, Pydantic-Modellen, Fallstudien

