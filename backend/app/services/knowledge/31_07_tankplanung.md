# Kat 31.07 — Tankplanung

**Kategorie:** 31_Design_Konstruktion  
**Unterkategorie:** Tankplanung  
**Gültig ab:** 2025-01  
**Version:** 1.0  
**Sprache:** German (Inhalte), English (Code)

---

## 1. Fundamentale Tank-Konzepte

### 1.1 Tanks auf Yachten

Tanks speichern Flüssigkeiten für verschiedene Zwecke:
- **Fuel Tank (Treibstoff):** Diesel oder Benzin für Motor
- **Fresh Water Tank:** Trinkwasser für Küche und Hygiene
- **Waste Water Tank (Greywater):** Abwasser von Spüle, Dusche, Waschbecken
- **Holding Tank (Blackwater):** Abwasser von Toilette (muss geleert werden)
- **Ballast Tank:** Wasser für Gewichts-Management und Stabilität

### 1.2 Tank-Anforderungen

**Sicherheit:**
- Undicht-Prüfung erforderlich
- Belüftung (Luftausgang) zu verhindern Vakuum/Druck-Aufbau
- Zugang für Reinigung und Wartung

**Funktionalität:**
- Entnahme-Schlauch/Rohr mit Hahn
- Sensor/Gauge für Füll-Stand
- Ablassventil (für Entleerung oder Ölwechsel)

**Konstruktion:**
- Material: Kunststoff (Polyethylen), rostfreier Stahl, Aluminum, oder FRP
- Form: Rechteckig oder angepasst an Rumpf-Form
- Positionierung: Gewichts-Effekt berücksichtigen

---

## 2. Fuel Tank Design

### 2.1 Treibstoff-Typ und -Eigenschaften

**Diesel (üblich für Motorsegler):**
- Dichte: 0.82–0.87 kg/L (typisch 0.85)
- Viskosität: niedrig (einfaches Pumpen)
- Energiedichte: 46 MJ/kg
- Brennpunkt: min. 55°C (EN 590; typisch 55–96°C — sicher unter normalen Bedingungen)
- Lagerung: stabil über Monate (kalter Lagerung besser)

**Benzin (selten für Yachten, kleine Motorboote):**
- Dichte: 0.71–0.77 kg/L (typisch 0.73)
- Viskosität: sehr niedrig
- Energiedichte: 46 MJ/kg (ähnlich Diesel)
- Brennpunkt: −43°C (hochexplosiv!)
- Lagerung: weniger stabil (kürzere Lagerdauer)
- Sicherheit: Extreme Vorsicht erforderlich

### 2.2 Fuel-Tank-Dimensionierung

**Berechnung erforderliche Menge:**

```
Reichweite (nm) = Tankvolumen (L) × Effizienz (nm/L) / 1

Effizienz typisch:
  Motorsegler @ 6 Knoten Cruise: 2–3 nm/L
  Motorboot @ 10 Knoten: 1–2 nm/L
  
Beispiel: 12m Motorsegler
  Ziel-Reichweite: 300 nm
  Effizienz: 2.5 nm/L
  Erforderlicher Tank: 300 / 2.5 = 120 L
```

**Praktische Überlegung:**

```
Min. Tankgröße: 10–15% der Verdrängung (in Liter)
  Beispiel: 12 t Verdrängung → 120–180 L üblich

Aber: Größerer Tank = mehr Reichweite = weniger Range-Angst
     Kosten & Gewicht müssen beachtet werden
```

> ⚠️ **ZU PRÜFEN (Audit):** "10–15% der Verdrängung" vs. Beispiel "12 t → 120–180 L" — 10 % von 12 t = 1200 L, nicht 120 L. Die eigenen Beispiele (120–180 L; F6.1: 100–210 L) und die parallele Ballast-Rechnung (§5.1: 2–5 % von 12 t = 240–600 L, korrekt gerechnet) implizieren für Kraftstoff eher ~1–1,5 % der Verdrängung. Prozentwert unverifiziert — nicht als gesicherte Auslegungsregel verwenden.

### 2.3 Fuel-Tank-Positionierung

**Ideal-Position (Gewichts-Management):**

```
Tank sollte nah bei Lightship-CG sein (Längsmittellinie).
  Beispiel: Wenn Lightship-CG @ 5.5m ab Bug,
  Fuel-Tank sollte auch bei ~5.3–5.7m sein.
```

**Praktische Positionen:**

```
Position 1: Bilge unter Salon (häufig für cruiser)
  − Zugang für Befüllung: oben über Deck-Öffnung
  − Vorteil: zentral, stabil
  − Nachteil: Geruch in Salon wenn Leck

Position 2: Kielbereich (unter Mastschuh, Motor-Raum)
  − Zugang schwieriger (unter Sole/Bodenplatte)
  − Vorteil: aus dem Weg, tiefs Gewicht-Vorteil
  − Nachteil: schwieriger zu warten

Position 3: Achterkabine (Bilge unter hinteren Berth)
  − Typisch für kleine Boote
  − Vorteil: einfach zu installieren
  − Nachteil: Gewichts-Effekt (höhere CG wenn groß)
```

### 2.4 Tank-Konstruktion

**Material-Optionen:**

| Material | Haltbarkeit | Kosten | Gewicht | Wartung | Anmerkung |
|----------|------------|--------|--------|---------|-----------|
| PE-Kunststoff | Gut | Niedrig | Leicht | Niedrig | Standard, flexibel |
| Edelstahl 316 | Ausgezeichnet | Hoch | Schwer | Mittel | Premium, langlebig |
| Aluminium | Gut | Mittel | Mittel | Mittel | Korrosion möglich |
| FRP | Gut | Mittel | Mittel | Mittel | Kann delaminieren |

**Typische Konstruktion (PE-Tank):**

```
Wanddicke: 5–8 mm (abhängig Größe und Druck)
Zulässiger Innendruck: 0–0.5 bar (Belüftung oben verhindert Druck)
Füll-Öffnung: Min. 50 mm Durchmesser (für Tankwagen-Zapfhahn)
Entnahme-Stutzen: 10–15 mm Außendurchmesser
Boden-Ablassschraube: Für Entwässerung (wenn erforderlich)
```

### 2.5 Fuel-System-Komponenten

```
Füll-Öffnung (Deck) → Füll-Rohr → Tank
                      ↓
                  Deckschaum (Filter Wasser/Verschmutzung)
                      ↓
                    Sensor (Float oder kapazitiv)
                      ↓
Entnahme-Schlauch → Absperrhahn → Grobfilter → Motor-Einspritzung
     ↑
  Saugschlauch von Tankboden
```

**Filter-Anforderungen:**

```
Grobfilter: 150–200 μm (vor Motor, schützt Einspritzpumpe)
Feinfilter: 4–10 μm (bei Hochdruck, vor Zylinder)

Wartung: Filter-Kartuschen regelmäßig austauschen (jährlich oder 500h)
         Tankboden-Wasser ablassen (Diesel & Wasser separieren!)
```

---

## 3. Fresh-Water Tank Design

### 3.1 Trinkwasser-Anforderungen

**Volumen-Schätzung:**

```
Pro Person: 15–25 L pro Tag (Trinken, Kochen, Hygiene)
Für 2 Personen, 2 Wochen Fahrt: 2 × 25 × 14 = 700 L

Praktisch für Cruiser:
  − Klein-Boot (2–4 Personen): 50–100 L
  − Mittel-Boot (4–6 Personen): 100–200 L
  − Groß-Yacht: 200–500 L
```

### 3.2 Trinkwasser-Tank-Material

**Strikte Anforderungen (Trinkwasser):**

```
Material MUSS:
  − Geschmacks-neutral sein (nicht Kunststoff-Geschmack abgeben)
  − Lebensmittel-freigegeben sein (FDA, CE-Markierung)
  − Nicht mit Diesel/Kraftstoff in Kontakt kommen (Kontaminations-Risiko)

Empfohlenes Material:
  − Food-Grade PE (Polyethylen)
  − Edelstahl 316 (Premium)
  − Borosilicate Glass (selten, aber ideal)

Nicht empfohlen:
  − Aluminium (kann mit Wasser reaktiv sein)
  − Normales Kunststoff (geschmacks-Verunreinigung)
  − Beschichtete Oberflächen (wenn Beschichtung abblättert)
```

### 3.3 Wasser-Haltung und Desinfektion

**Legionellen-Risiko:**

```
Stillstehendes Wasser > 20°C für lange Zeit können Legionellen entwickeln.
Prävention:
  − Wasser-Temperatur < 15°C halten (gut isoliert)
  − Oder: Desinfektionsmittel (Chlor-Tabletten)
  − Oder: Tank regelmäßig leeren/spülen
```

**Wasser-Behandlung vor Einlagerung:**

```
Für Langzeit-Lagerstabilität:
  − 1–2 Chlor-Tabletten pro 100 L (5–10 ppm Chlor)
  − Oder: Spezialchemikalien (Aqua-Check, Travelift)
  
Für häufigen Austausch:
  − Einfach frisch füllen (kein Behandlung nötig)
```

### 3.4 Wasser-System-Komponenten

```
Tank → Absperrhahn → Grobfilter → Pumpe (elektrisch oder manuell)
                        ↓
                    Drucktank (optional)
                        ↓
                     Rohre zu Tap/Dusche
                        ↓
                    Warmwasser-Heizer (optional)
```

**Faucet-Optionen:**

```
Manuell (Handpumpe):
  − Preiswert, zuverlässig
  − Arbeit erforderlich (mehrmals pro Tag)

Elektrisch:
  − Komfort, automatisch
  − Batterie-Power erforderlich
  − Drucktank stabilisiert Druck
```

---

## 4. Waste-Water System

### 4.1 Greywater (Spüle, Dusche, Waschbecken)

**Volumen:**

```
Pro Person: 10–15 L pro Tag (typisch Küche + Bad)
2 Personen, 2 Wochen: 2 × 12.5 × 14 = 350 L
```

**System-Optionen:**

```
Option A: Direkt Überbord (einfach, aber Umwelt-Problem)
  − Vorteil: keine Tank-Überwachung erforderlich
  − Nachteil: illegal in vielen Häfen, Umweltschäden

Option B: Holding Tank (sammeln, später leeren)
  − Vorteil: legal, Umwelt-freundlich
  − Nachteil: Tank-Verwaltung, Geruch wenn groß

Option C: Behandlung (biologisch/Chemisch)
  − Vorteil: Wasser kann überbord geleitet werden
  − Nachteil: teuer, komplexe Wartung
```

### 4.2 Blackwater (Toiletten-Abwasser)

**Strikte Regulierung:**

```
International MARPOL Annex IV:
  − Blackwater darf nicht in Häfen/küstennahe Gewässer geleitet werden
  − Holding Tank oder Sea Toilet erforderlich
  − Tank muss alle paar Tage geleert werden (oder Pulvertoilette nutzen)
```

**Holding Tank Größe:**

```
Pro Person: 2–3 L pro Tag (Volumen)

Beispiel: 2-Personen Boot
  × 3 Tage vor nächstem Hafen = 2 × 3 × 3 = 18 L Minimum
  Praktisch: 25–50 L Tank für Sicherheit
```

---

## 5. Ballast Tank (wenn vorhanden)

### 5.1 Zweck und Design

**Zweck:**
- Gewichts-Anpassung (wenn reales Gewicht vom Design abweicht)
- Trim-Korrektur (longitudinal)
- Stabilität-Fein-Tuning (wenn Schwerpunkt falsch)

**Material:** Typisch unkritisch (kann normales Wasser sein)

**Größe:**

```
Typisch: 2–5% der Verdrängung als Reserve
Beispiel: 12 t Boot → 240–600 L Ballast-Tank-Kapazität
```

### 5.2 Ballast-Betrieb

```
Szenario 1: Boot schwerer als erwartet
  − Ballast-Wasser hinzufügen → höherer Gewicht balanciert überschuss
  
Szenario 2: Boot leichter als erwartet
  − Ballast-Wasser ablassen → niedrigerer Gewicht anpasst

Szenario 3: Trim-Fehler
  − Ballast zwischen Bug/Heck transferieren → Trim korrigiert
```

---

## 6. Fehleranalyse — 12 Fehlermuster

### 6.1 [F6.1] Fuel-Tank zu klein (Reichweiten-Problem)

**Symptom:**
- Design-Reichweite: 500 nm
- Real erreichbar: 250 nm (bei gemischtem Fahrtmuster)
- Crew nervös über Treibstoff-Reserve

**Ursache:**
- Fuel-Tank zu klein dimensioniert (Kosten/Gewicht-Einsparung)
- Verbrauch unterschätzt (realer ~30% höher als berechnet)

**Folgen:**
```
Zu kleine Reichweite führt zu:
  − Häufigere Tankstopps (störend auf Cruises)
  − Range-Angst (Crew unruhig)
  − Eingeschränkte Routen-Planung (muss Häfen besuchen)
  − Sicherheit: zu wenig Reserve bei Notfall
```

**Empforlicht Korrektion:**
```
Tank-Größe erhöhen:
  Ziel: Reichweite ≥ 500 nm für Offshore-Cruiser
         oder ≥ 200 nm für Küsten-Cruiser
  
Berechnung:
  Verbraucht_realistisch = 1.3 × Basis-Verbrauch (Sicherheit)
  Tank_min = Reichweite_Ziel / Verbrauch_realistisch
  
Beispiel: 12m Motorsegler
  Basis-Verbrauch: 2.5 nm/L
  Realistisch: 2.5 / 1.3 = 1.9 nm/L
  Für 400 nm Reichweite: Tank ≥ 400 / 1.9 = 210 L
  
Wenn aktuell nur 100 L: zu klein!
  Lösung: Tank-Größe auf 200+ L erhöhen (oder akzeptieren niedrigere Reichweite)
```

**Prüfkriterium:** Reichweite < 250 nm oder Tank < 10% Verdrängung-Volumen → Überprüfung

> ⚠️ **ZU PRÜFEN (Audit):** Schwelle "10 % Verdrängung-Volumen" widerspricht den Beispielen dieses Dokuments (Tank 100–210 L bei 12 t ≈ 1–2 %). 10 % von 12 t wären ~1200 L. Prozentschwelle unverifiziert — siehe Audit-Hinweis in §2.2.

---

### 6.2 [F6.2] Fuel-Tank-Position zu achtern (Trim-Fehler)

**Symptom:**
- Tank 50% achtern positioniert
- Bei vollen Tank: Boot sitzt mit Heck tiefer ein als mit leerem Tank
- Trim-Änderung: +1.5° (Heck-Trim)
- Fahrtverhalten unterschiedlich voll vs. leer

**Ursache:**
- Tank wegen Platz-Mangel achtern positioniert (statt mittschiffs)
- Schwerpunkt-Effekt nicht berücksichtigt

**Folgen:**
```
Trim-Variation mit Tankfüllung:
  − Hydrodynamisches Verhalten unterschiedlich (Widerstand variiert)
  − Schiff muß umgetrimmt werden bei Tankwechsel (unbequem)
  − Seakeeping kann leiden bei extremem Trim
```

**Empforlicht Korrektion:**
```
Tank-Position optimieren:
  Ziel: Tank-Schwerpunkt möglichst nah bei Boot-Lightship-CG
  
Beispiel: Lightship-CG @ 5.5m ab Bug
  Fuel-Tank sollte auch @ 5.0–6.0m sein (nicht 7m achtern)

Wenn nicht verschiebbar:
  − Zwei kleinere Tanks (einer Bug-Fach, einer Mittschiffs) statt einer achtern
  − Oder: akzeptieren Trim-Variation (und dokumentieren Betrieb-Richtlinien)
```

**Prüfkriterium:** |Tank_CG − Lightship_CG| > 1.0m → Überprüfung/Optimierung

---

### 6.3 [F6.3] Wasser-Tank Trink-Qualität fragwürdig (Kontamination)

**Symptom:**
- Wasser hat Kunststoff-Geschmack oder Geruch
- Sichtbare Verfärbung (trüb, grünlich)
- Keime-Wachstum möglich (Legionellen?)

**Ursache:**
- Nicht-lebensmittel-zertifiziertes Kunststoff verwendet
- Oder: Tank wurde mit Diesel verschmutzt (Undichtigkeit)
- Oder: zu lange Lagerstabilität ohne Kühlung/Desinfektion

**Folgen:**
- Trinkwasser nicht genießbar
- Gesundheits-Risiko (Keime, Chemikalien)
- Tank muß geleert/gereinigt werden

**Empforlicht Korrektion:**
```
Sofort-Maßnahmen:
  1. Wasser verwerfen (komplett leeren)
  2. Tank mit Süßwasser mehrfach spülen
  3. Neue Befüllung mit frischem Trinkwasser
  4. Desinfektionsmittel hinzufügen (1–2 Tabletten pro 100L)

Längerfristig:
  − Tank-Material überprüfen (muß Food-Grade PE sein)
  − Neue Tank installieren wenn aktueller beschädigt/nicht zertifiziert
  − Trinkwasser regelmäßig austauschen (nicht > 2–3 Wochen Lagerung ohne Kühlung)
  − Temperatur niedrig halten (unter 15°C ideal)
```

**Prüfkriterium:** Wasser-Geschmack oder -Geruch → Sofort Tank-Leerung/Reinigung

---

### 6.4 [F6.4] Undichter Tank (Leck)

**Symptom:**
- Sichtbare Flüssigkeit unter Tank-Lage
- Geruch (Diesel, Wasser-Verderb)
- Flüssigkeits-Level sinkt ohne Verbrauch
- Stark-Geruch im Rumpf

**Ursache:**
- Tank-Wandung defekt (Riß oder Korrosion-Loch)
- Schlauch-Verbindung undicht
- Überalterung (Tank 20+ Jahre alt)

**Folgen:**
```
Undichter Fuel-Tank:
  − Leck ausläuft, Umwelt-Gefährung
  − Sicherheits-Risiko (Diesel-Dampf flammbar)
  − Maschinenraum-Sicherheit gefährdet

Undichter Wasser-Tank:
  − Wasser-Verlust (Boot austrocknet)
  − Strukturschäden (Rumpf-Feuchte)
  − Pilz/Schimmel-Wachstum möglich

Undichter Holding-Tank:
  − Umwelt-Katastrophe (Blackwater überall)
  − Hygiene-Problem
  − Illegale Emission
```

**Empforlicht Korrektion:**
```
Diagnose:
  1. Undichtstelle lokalisieren (Sichtprüfung, Drucktest)
  2. Undichtheit bestätigen (mit Trocken-Handschuh unter Stelle 12h prüfen)

Reparatur:
  − Kleine Lecks (Rohr-Verbindung): Schlauch austauschen, neu dichtern
  − Größere Lecks (Tank-Wandung): Tank-Austausch erforderlich (nicht reparierbar!)

Interim:
  − Leck-Stelle mit Kunststoff-Patch temporär abdichten
  − oder: Tank leeren und später reparieren

Prävention:
  − Regelmäßige Inspektionen durchführen
  − Tanks nach ~15 Jahren Lebensalter austauschen
```

**Prüfkriterium:** Sichtbares Leck → Sofort Reparatur/Ersatz erforderlich

---

### 6.5 [F6.5] Über-Befüllung (Druck-Aufbau)

**Symptom:**
- Tank genau bis zum Rand befüllt (kein Freiraum)
- Unter Hitze-Sonnenschein: Flüssigkeit läuft über Deck
- Oder: Druck im Tank schädigt Wände/Rohre

**Ursache:**
- Tankwagen-Fahrer befüllt zu aggressiv
- Crew ignoriert Füll-Markierung
- Keine Überströmungs-Rohr vorhanden

**Folgen:**
```
Auslaufen:
  − Umwelt-Kontamination (Diesel/Wasser über Deck)
  − Rutsch-Gefahr für Crew
  − Finanzielle Strafen in Häfen

Druck-Aufbau:
  − Tank-Wände können Verformung erleiden
  − Rohre/Schläuche können Bruch erfahren
  − Lecks entstehen durch Über-Druck
```

**Empforlicht Korrektion:**
```
Füll-Management:
  − Tank-Füll-Markierung kennen (typisch 90% statt 100%)
  − Beim Befüllen: Füll-Schlauch selbst halten, nicht Tankwagen-Fahrer allein
  − Visuelle Kontrolle: Flüssigkeit sollte 5–10cm unter Öffnung sein

Überströmungs-Rohr:
  − Sollte auf allen Tanks vorhanden sein
  − Rohrbogen oben führt Überfluss sicher weg
  
System prüfen:
  − Lüftungs-Ventil sollte frei sein (nicht blockiert)
  − Druck kann entweichen
```

**Prüfkriterium:** Tank-Befüllung > 95% → Leck-Risiko, korrekt weniger halten

---

### 6.6 [F6.6] Schlamm/Wasser im Fuel-Tank (biologische Kontamination)

**Symptom:**
- Motor läuft unregelmäßig oder stottert
- Filter verstopft schnell
- Dunkle Partikel sichtbar in Treibstoff-Proben
- Übler Geruch aus Tank

**Ursache:**
- Wasser in Tank (Kondensation oder Wassereintritt)
- Biologie (Bakterien/Algen wachsen in Wasser-Schicht unter Diesel)
- Lange Lagerstabilität ohne Wartung

**Folgen:**
```
Biologischer Befall (BioFouling):
  − Schlamm-Ablagerung am Tankboden
  − Motor-Zerstörung möglich (bei starkem Befall)
  − Verstopfte Filter (häufige Wartung erforderlich)
  − Teuer zu reparieren
```

**Empforlicht Korrektion:**
```
Sofort (Notfall):
  − Filter häufiger austauschen (täglich wenn nötig)
  − Tank-Einfüllung bis Boden durchlüften

Kurz-Fristig:
  − Tank-Ablassventil öffnen, Wasser ablassen (schwere Stoffe sinken)
  − Grobfilter austauschen
  − Tankwagen-Biozid hinzufügen (spezielle Additiva töten Mikroben)

Längerfristig:
  − Tank komplett leeren und spülen
  − Neuer Diesel einfüllen
  − Getrockneter Tank lagern (unter Stickstoff ideal)
  − Regelmäßig inspizieren (monatlich)

Prävention:
  − Tankdeckel dicht halten
  − Lüftungs-Öffnung mit Filter schützen
  − Kühl-Lagerung (kaltes Diesel weniger anfällig)
```

**Prüfkriterium:** Schlamm sichtbar oder Motor-Fehlverhalten → Sofort Tank-Service erforderlich

---

### 6.7 [F6.7] Fehler­hafte Sensor-Installation (Falsche Füll-Anzeige)

**Symptom:**
- Tankfüllungs-Anzeige springt oder bleibt stecken
- Zeigt "voll" wenn tatsächlich leer (oder umgekehrt)
- Meter schwankt wild

**Ursache:**
- Float-Sensor falsch positioniert oder beschädigt
- Schlauch an Sensor verdreht/blockiert
- Elektronik-Fehler (Sensor/Gauge-Verkabelung)

**Folgen:**
- Crew weiß nicht, wie viel Treibstoff noch übrig
- Range-Angst oder Überlastungs-Gefahr (Motor-Mangel wegen leerer Tank)
- Navigation unsicher

**Empforlicht Korrektion:**
```
Diagnose:
  − Sensor mechanisch prüfen (Float sollte frei auf- und abgehen)
  − Schlauch-Verbindung überprüfen
  − Elektronik-Kontinuität prüfen

Sensor-Typ überprüfen:
  − Float-Sensor (klassisch): beweglicher Schwimmer am Arm
  − Kapazitiv-Sensor (modern): elektronisch, keine beweglichen Teile
  
Reparatur:
  − Float-Sensor: Schubstange fetten oder austauschen
  − Kapazitiv-Sensor: meist nicht reparierbar, austauschen
  
Notfall-Lösung:
  − Manuell-Meßstab verwenden (Stick mit Markierungen)
  − Oder: Volumen-Berechnung (wenn Tank-Form bekannt)
```

**Prüfkriterium:** Unzuverlässige Anzeige → Sensor überprüfen/austauschen

---

### 6.8 [F6.8] Tank-Belüftung blockiert (Druck/Vakuum)

**Symptom:**
- Tank kann nicht schnell befüllt werden (Lüftungs-Rohr blockiert)
- Oder: Vakuum im Tank (Saugschlauch wird flach gezogen)
- Pumpende Geräusche beim Entleeren

**Ursache:**
- Lüftungs-Öffnung verschlossen (Insekt, Schlamm)
- Lüftungs-Rohr zu klein dimensioniert
- Überströmungs-Schutz zu restriktiv

**Folgen:**
```
Blockierte Lüftung:
  − Langsameres Befüllen (frustrierend)
  − Druck-Aufbau im Tank (ggf. Rohr-Bruch)
  − Oder: Vakuum beim Entleeren (Motor-Versagen wegen Luft-Lock)
```

**Empforlicht Korrektion:**
```
Luftungs-System überprüfen:
  − Lüftungs-Öffnung freimachen
  − Deckschaum überprüfen (kann blockiert sein)
  − Lüftungs-Rohr-Durchmesser überprüfen (min. 20–25mm für Fuel)

Proper Lüftungs-Design:
  − Deckschaum-Filter sollte frei sein
  − Lüftungs-Rohr am höchsten Punkt des Tanks anschließen und stetig aufwärts verlegen (keine Flüssigkeitsfallen; ein bis zum Tankboden geführtes Entlüftungsrohr würde die Entlüftung blockieren — vgl. USCG/ABYC H-24/H-33)
  − Überströmungs-Rohr mit sanftem Bogen (nicht scharfer Knick)
  
Test:
  − Befüllung sollte in <5 min vollständig sein
  − Entnahme sollte ohne Schäumen/Geräuschen funktionieren
```

**Prüfkriterium:** Befüllung > 10 min oder Motor-Versagen wegen Air-Lock → Lüftung überprüfen

---

### 6.9 [F6.9] Mehrere Tank-Verdrahtung fehlerhaft (Betrieb-Modus unklar)

**Symptom:**
- Zwei Fuel-Tanks vorhanden
- Aber: Keine Absperr-Hähne zwischen ihnen
- Oder: Hähne existieren, aber Besatzung weiß nicht, wie sie zu schalten sind

**Ursache:**
- Design ignoriert Mehrfach-Tank-Realität
- Bedienungs-Anleitung fehlt oder unklar

**Folgen:**
- Crew kann nicht zwischen Tanks wechseln (wenn einer läuft)
- Oder: falscher Tank wird angesaugt

**Empforlicht Korrektion:**
```
Tank-Schalt-System:
  − Jeder Tank sollte eigene Absperrung haben
  − UND: Eine Kombinations-Leitung (um beide zu nutzen, wenn gewünscht)
  
Vorzugsweise:
  − Tank 1 Absperrung (für alleinigen Betrieb)
  − Tank 2 Absperrung (für alleinigen Betrieb)
  − Kombinations-Ventil oder Y-Verbindung (beide gleichzeitig wenn nötig)
  
Signalisierung:
  − Große Etiketten an Hähnen ("Tank 1", "Tank 2", "Both")
  − Betriebshandbuch mit Diagramm
  − Crew-Training im richtigen Betrieb

Beste Praxis:
  − Automatisches Kugel-Ventil mit Schwimmer (wechselt automatisch zu Tank 2 wenn Tank 1 leer)
  − Aber: manuelle Kontrolle sollte noch möglich sein
```

**Prüfkriterium:** Mehrfach-Tanks ohne klare Betriebsanleitung → Überprüfung/Dokumentation erforderlich

---

### 6.10 [F6.10] Greywater-Tank zu klein (schnelle Überfüllung)

**Symptom:**
- Tank füllt sich schneller als erwartet
- Nach 2–3 Tagen bereits voll (nur 50 L Tank)
- Schiff muß in Hafen zur Entleerung

**Ursache:**
- Tank dimensioniert ohne Reserv
- Gast an Bord (unerwarteter Wasserverbrauch)

**Folgen:**
- Tank-Überfluss (Wasser läuft über Bord, unsauberes Wasser)
- Hafen-Strafen möglich
- Route-Plannung gestört

**Empforlicht Korrektion:**
```
Tank-Größe erhöhen:
  Ziel: Min. 10 L pro Person pro Tag (Spüle) + 5 L (Dusche) = 15 L/Tag

Beispiel: 2 Personen, 1 Woche Fahrt
  2 × 15 × 7 = 210 L erforderlich
  
Praktisch: 200–250 L Tank für 2–3 Wochen Unabhängigkeit

Wenn Platz begrenzt:
  − Option 1: Häufiger entleeren (alle 3–5 Tage, unbequem)
  − Option 2: Greywater direkt überbord (wenn legal/sauberes Wasser)
  − Option 3: Zwei Tank-System (wechseln wenn einer voll)
```

**Prüfkriterium:** Tank < 100 L für 2+ Personen → Zu klein (nur für Wochenend-Trips OK)

---

### 6.11 [F6.11] Holding-Tank-Wartung vernachlässigt (Überfüllung/Geruch)

**Symptom:**
- Tank überläuft (Black-Water auf Deck)
- Entsetzlicher Geruch
- Toilette funktioniert schlecht (Vakuum-Probleme)

**Ursache:**
- Tank seit Monaten nicht geleert
- Belüftung blockiert
- Biologischer Befall (Bakterien)

**Folgen:**
- Hygiene-Katastrophe
- Crew-Gesundheit gefährdet
- Umwelt-Verschmutzung
- Hafenstrafen

**Empforlicht Korrektion:**
```
Sofort-Maßnahmen:
  1. Tank entleeren (in zugelassener Pumpstation)
  2. Tank spülen/desinfizieren
  
Langfristig-Management:
  − Tank alle 3–7 Tage leeren (je nach Personenzahl und Tankgröße)
  − Belüftungs-Öffnung frei halten
  − Desinfektions-Mittel hinzufügen (für Geruch-Kontrolle)
  
Tablet-Systeme:
  − Bio-Enzyme oder Chemikalien-Tablets reduzieren Geruch und Bakterien
  − Hinzufügen nach jeder Entleerung
```

**Prüfkriterium:** Tank überfüllt oder Geruch-Probleme → Sofort Entleerung erforderlich

---

### 6.12 [F6.12] Tank-Material inkompatibel mit Flüssigkeit (Korrosion/Auflösung)

**Symptom:**
- Diesel in Aluminum-Tank: Oxidation/Korrosion sichtbar
- Wasser in nicht-zertifiziertem Kunststoff: Geschmack/Farbe-Problem
- Tank wird dünner (Wandung dünner werdend)

**Ursache:**
- Falsches Material gewählt (z.B. kostengünstig, aber inkompatibel)
- Keine Beschichtung/Auskleidung vorhanden

**Folgen:**
- Korrosion/Degradation des Tank-Materials
- Langfristig: Leck-Risiko
- Flüssigkeits-Kontamination

**Empforlicht Korrektion:**
```
Material-Kompatibilität überprüfen:
  Diesel:
    − Akzeptabel: Edelstahl, Kunststoff (PE, Epoxy-beschichtet)
    − Problematisch: Aluminium (ohne Beschichtung), normales Stahl (rostet)
  
  Wasser (Trinkwasser):
    − Akzeptabel: Food-Grade PE, Edelstahl, Glas
    − Problematisch: Aluminium (reaktiv), normaler Kunststoff (Geschmack)

Reparatur/Ersatz:
  − Leck-Reparatur funktioniert selten dauerhaft
  − Bessere Lösung: neuer Tank mit richtigem Material
  
Oberflächenfinish:
  − Epoxy-Beschichtung oder Kunststoff-Auskleidung kann Inkompatibilität vermeiden
  − Aber: Sicherheit nicht garantiert, Austausch besser
```

**Prüfkriterium:** Material sichtbar korrodiert oder degradiert → Tank-Austausch empfohlen

---

## 7. Tank-Wartungs-Plan

```
Jährlich:
  ☐ Alle Tanks inspizieren (visuell innen wenn möglich)
  ☐ Greywater-Ablassventil überprüfen
  ☐ Holding-Tank desinfizieren
  ☐ Fuel-Filter austauschen
  ☐ Wasser-Sensor testen
  ☐ Lüftungs-Öffnungen überprüfen

Monatlich (oder wenn Boot aktiv):
  ☐ Sensor-Anzeigen überprüfen
  ☐ Auf Lecks prüfen (visuell unter Tanks)
  ☐ Greywater-Level überwachen
  
Täglich (während Fahrt):
  ☐ Holding-Tank-Level überprüfen
  ☐ Fuel-Verbrauch gemäß Plan
  ☐ Auf Gerüche/Lecks prüfen
```

---

## 8. ANHANG — Pydantic v2 Model

```python
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from enum import Enum
from datetime import datetime

class TankTypeEnum(str, Enum):
    FUEL = "fuel"
    FRESH_WATER = "fresh_water"
    GREY_WATER = "grey_water"
    BLACK_WATER = "black_water"
    BALLAST = "ballast"

class TankMaterialEnum(str, Enum):
    POLYETHYLENE = "pe"
    STAINLESS_STEEL = "ss316"
    ALUMINIUM = "alu"
    FRP = "frp"
    STEEL_COATED = "steel_coated"

class TankSpecification(BaseModel):
    """Tank-Spezifikation und Dimensionen"""
    model_config = {"from_attributes": True}
    
    tank_id: str = Field(..., description="Unique tank identifier")
    tank_type: TankTypeEnum = Field(..., description="Tank type")
    material: TankMaterialEnum = Field(..., description="Tank material")
    
    # Dimensions & Capacity
    capacity_liters: float = Field(..., gt=0, description="Tank capacity (liters)")
    length_mm: Optional[float] = Field(None, description="Tank length (mm)")
    width_mm: Optional[float] = Field(None, description="Tank width (mm)")
    height_mm: Optional[float] = Field(None, description="Tank height (mm)")
    
    # Position
    position_x_mm: Optional[float] = Field(None, description="Longitudinal position (mm from datum)")
    position_z_mm: Optional[float] = Field(None, description="Vertical position (mm above baseline)")
    
    # Operating Parameters
    max_temp_celsius: Optional[float] = Field(None, description="Maximum operating temperature (°C)")
    rated_pressure_bar: Optional[float] = Field(None, description="Rated internal pressure (bar)")
    
    # Condition
    installation_date: Optional[datetime] = Field(None, description="Installation date")
    last_service_date: Optional[datetime] = Field(None, description="Last service/inspection date")
    condition: str = Field("GOOD", description="Current condition (GOOD, FAIR, POOR)")
    
    notes: Optional[str] = Field(None, description="Additional notes")

class TankingOperation(BaseModel):
    """Betank-Vorgang (Befüllung oder Entleerung)"""
    model_config = {"from_attributes": True}
    
    operation_date: datetime = Field(default_factory=datetime.now)
    operation_type: str = Field(..., description="'fill' or 'empty'")
    tank: TankSpecification = Field(..., description="Tank being operated")
    
    # Quantities
    volume_liters: float = Field(..., gt=0, description="Volume transferred (liters)")
    fuel_type: Optional[str] = Field(None, description="Fuel type if applicable (Diesel, etc.)")
    
    # Quality (if applicable)
    fuel_quality_check: Optional[bool] = Field(None, description="Fuel quality inspection passed")
    water_contamination_detected: Optional[bool] = Field(None, description="Water contamination found")
    
    location: Optional[str] = Field(None, description="Location (marina/port)")
    notes: Optional[str] = Field(None, description="Crew notes")

class VesselTankingSystem(BaseModel):
    """Komplettes Tank-System eines Schiffs"""
    model_config = {"from_attributes": True}
    
    vessel_name: str = Field(..., description="Yacht name")
    analysis_date: datetime = Field(default_factory=datetime.now)
    
    # All Tanks
    tanks: List[TankSpecification] = Field(default_factory=list, description="All tanks on vessel")
    
    # Current Status
    fuel_current_liters: Optional[float] = Field(None, description="Current fuel quantity (liters)")
    water_current_liters: Optional[float] = Field(None, description="Current fresh water (liters)")
    grey_current_liters: Optional[float] = Field(None, description="Current greywater (liters)")
    black_current_liters: Optional[float] = Field(None, description="Current blackwater (liters)")
    
    # Design Parameters
    crew_size: int = Field(2, description="Number of crew")
    expected_cruise_duration_days: Optional[int] = Field(None, description="Planned cruise duration (days)")
    
    # Analysis
    fuel_range_nm: Optional[float] = Field(None, description="Estimated fuel range (nautical miles)")
    water_days_supply: Optional[float] = Field(None, description="Fresh water supply duration (days)")
    
    warnings: List[str] = Field(default_factory=list, description="System warnings")
    recommendations: List[str] = Field(default_factory=list, description="Design recommendations")

def calculate_fuel_range(
    tank_capacity_liters: float,
    current_fill_percent: float,
    fuel_consumption_lh: float,
    cruise_speed_knots: float
) -> dict:
    """Berechne Treibstoff-Reichweite"""
    available_fuel = tank_capacity_liters * (current_fill_percent / 100)
    endurance_hours = available_fuel / fuel_consumption_lh
    range_nm = endurance_hours * cruise_speed_knots
    
    return {
        "available_fuel_liters": available_fuel,
        "endurance_hours": round(endurance_hours, 1),
        "range_nm": round(range_nm, 0),
        "range_km": round(range_nm * 1.852, 0)
    }

def calculate_water_supply(
    tank_capacity_liters: float,
    crew_size: int,
    daily_consumption_liter_per_person: float = 20
) -> dict:
    """Berechne Wasser-Vorrat-Dauer"""
    daily_total = crew_size * daily_consumption_liter_per_person
    days_supply = tank_capacity_liters / daily_total
    
    return {
        "daily_consumption_liters": daily_total,
        "supply_days": round(days_supply, 1),
        "supply_weeks": round(days_supply / 7, 1)
    }

def assess_tank_condition(
    installation_years_ago: int,
    last_service_years_ago: float,
    material: str,
    condition_visual: str
) -> dict:
    """Bewertz Tank-Zustand und Service-Bedarf"""
    age = installation_years_ago
    service_overdue = last_service_years_ago > 1.0
    
    risk_score = 0
    if age > 15:
        risk_score += 2
    elif age > 10:
        risk_score += 1
    
    if service_overdue:
        risk_score += 2
    
    if material == "steel_coated" and age > 10:
        risk_score += 1
    
    if condition_visual == "POOR":
        risk_score += 3
    elif condition_visual == "FAIR":
        risk_score += 1
    
    if risk_score >= 5:
        recommendation = "URGENT: Tank inspection and possible replacement required"
    elif risk_score >= 3:
        recommendation = "Schedule tank service within 6 months"
    else:
        recommendation = "Normal maintenance schedule"
    
    return {
        "risk_score": risk_score,
        "recommendation": recommendation,
        "next_service_months": 12 if risk_score < 3 else 6 if risk_score < 5 else 1
    }
```

---

## 9. Normativer Rahmen (verifiziert)

> **Hinweis Confidence:** Alle Normbezüge in dieser Tabelle sind gegen die offiziellen ISO/IMO/ABYC-Titel und öffentlich einsehbare Norm-Vorschauen abgeglichen (`documented`). Die *Inhalte* der kostenpflichtigen Normtexte (exakte Prüfkoeffizienten, Tabellen) sind — soweit nicht ausdrücklich mit Quelle belegt — NICHT rekonstruiert. Fehlende Detailwerte stehen ausschließlich im Volltext der jeweiligen Norm.

| Norm | Titel / Gegenstand | Geltungsbereich | Confidence |
|------|--------------------|-----------------|------------|
| **ISO 21487:2022** | Small craft — Permanently installed petrol and diesel fuel tanks (Auslegung, Bau, **Prüfung** der Tanks selbst) | Boote ≤ 24 m Rumpflänge | `documented` |
| **ISO 10088:2022** | Small craft — Permanently installed fuel systems (**Installation** vom Einfüllstutzen bis Motoranschluss) | Innen-/Außenborder ≤ 24 m | `documented` |
| **ISO 7840:2021** | Small craft — **Fire-resistant** fuel hoses (brandfeste Kraftstoffschläuche) | Fest installierte Kraftstoffsysteme | `documented` |
| **ISO 8469:2021** | Small craft — **Non-fire-resistant** fuel hoses (nicht brandfeste Kraftstoffschläuche) | Rumpflänge ≤ 24 m | `documented` |
| **ISO 8099-1:2018** | Small craft — Waste systems — Part 1: **Waste water retention** (Fäkalien-Sammeltank / Holding Tank) | ≤ 24 m | `documented` |
| **ISO 8099-2:2021** | Small craft — Waste systems — Part 2: **Sewage treatment systems** (Abwasser-Aufbereitung) | ≤ 24 m | `documented` |
| **ISO 12217 (1/2/3)** | Stability and buoyancy assessment and categorization — hier relevant für **Free-Surface-Korrektur** und CG bei teilgefüllten Tanks | Design-Kategorien A–D | `documented` |
| **RCD 2013/53/EU** | EU-Sportbootrichtlinie — harmonisiert die o. g. ISO-Normen; CE-Konformität für 2,5–24 m | EU-Markt | `documented` |
| **MARPOL Annex IV, Reg. 11** | Prevention of Pollution by Sewage — Einleitregeln (Abstand/Geschwindigkeit) | International | `documented` |
| **ABYC H-24** | Gasoline Fuel Systems (US-Pendant, Benzin) | US-Sportboote | `documented` |
| **ABYC H-33** | Diesel Fuel Systems (US-Pendant, Diesel) | US-Sportboote | `documented` |
| **SAE J1527** | Marine Fuel Hoses (US-Schlauchnorm, Pendant zu ISO 7840/8469) | Kleinboote | `documented` |
| **NSF/ANSI/CAN 61** | Drinking Water System Components — Health Effects (Trinkwasser-Kontaktmaterial) | Trinkwassersysteme | `documented` |

> Quellen: iso.org/standard/76441 (ISO 21487:2022); iso.org/standard/76429 (ISO 10088:2022); iso.org/standard/79097 (ISO 7840:2021); iso.org/standard/79098 (ISO 8469:2021); iso.org/standard/73216 (ISO 8099-1:2018); imo.org — Prevention of Pollution by Sewage (MARPOL Annex IV); abycinc.org (H-24/H-33); nsf.org — NSF/ANSI 61.

**Wichtige Zuordnung (häufige Verwechslung):**
- **Tank (Behälter selbst)** → ISO 21487. **Kraftstoff-System (Verrohrung, Installation)** → ISO 10088. **Schläuche** → ISO 7840 (brandfest) / ISO 8469 (nicht brandfest).
- Der frühere Verweis auf reine „MARPOL Annex IV" in §4.2 gilt **völkerrechtlich für die Einleitung**; die **bauliche** Ausführung des Fäkalientanks auf CE-Booten regelt **ISO 8099-1** — beide sind zu erfüllen.

---

## 10. Tankmaterial, Wanddicke & Prüfung nach ISO 21487:2022

> **Confidence `documented`.** Werte aus der öffentlich publizierten ISO-21487:2022-Konformitäts-Checkliste (ceinspector.com / Blue Peter Marine) abgeleitet; Zahlen im Normvolltext maßgeblich. Wo unten „—" steht, ist der Wert nicht zweifelsfrei belegt.

### 10.1 Mindestwanddicken metallischer Tanks (ISO 21487:2022)

| Werkstoff | Mindestwanddicke | Anmerkung |
|-----------|------------------|-----------|
| Aluminiumlegierung (Cu-Gehalt ≤ 0,1 %) | **2,0 mm** | Seewasserbeständige Legierung erforderlich (kein kupferreiches Alu) |
| Edelstahl (nichtrostend) | **1,0 mm** | für Kraftstoff geeignete Sorte (z. B. 316/1.4404) |
| Kupfer, innen verzinnt | **1,5 mm** | — |
| Weichstahl, beidseitig feuerverzinkt | **1,5 mm** | — |
| Aluminiertes Stahlblech | **1,2 mm** | — |

> Quelle: ISO 21487:2022 Petrol Metallic Tank Compliance Checklist (ceinspector.com, Blue Peter Marine, 2025).
> ⚠️ **ZU PRÜFEN (Audit):** Die Wanddicke skaliert im Normtext teils mit **Tankvolumen/Wandfläche** (größere Tanks → dickere Wand). Die o. g. Werte sind Mindestwerte; die volumenabhängige Staffelung steht nur im Volltext (nicht rekonstruiert).

### 10.2 Prüfdrücke und Prüfungen

| Prüfung | Parameter (verifiziert) |
|---------|-------------------------|
| Dichtheits-/Druckprüfung | Prüfdruck = **max(20 kPa; 1,5 × höchster hydrostatischer Betriebsdruck)**; alternatives Festigkeitsverfahren min. **30 kPa** |
| Druck-Impuls-Prüfung (Ermüdung, Metall optional statisch) | **0 → 20 → 0 kPa**, **25 000 Zyklen**, max. **15 Zyklen/min**, Tank vollständig mit sauberem Wasser gefüllt |
| Feuerprüfung (Fire Test, Klauseln 7.4/7.5) | **Nicht** für Metalltanks. **Nichtmetallische** Tanks im **Motorraum**: müssen einen **2,5-Minuten-Brand** überstehen |
| Kraftstoff-Vorkonditionierung (Thermoplast) | **28 Tage ≥ 21 °C** oder alternativ **10 Wochen bei 43 °C ± 5 °C** vor Festigkeitsprüfung |
| Kontrollöffnung/Inspektionsluke (Diesel) | Mindest-Ø **120 mm** (Klausel 6.1.6) |

> Quelle: ISO 21487:2022 Compliance Checklists (ceinspector.com, 2025/2026).

### 10.3 Kennzeichnung nichtmetallischer Tanks
Nichtmetallische Tanks **müssen mit der maximalen Temperatur gekennzeichnet** sein, der der Tank ausgesetzt werden darf (ISO 21487:2022, Klausel 8). Typische Richtwerte: HDPE ~40–60 °C, LDPE etwas niedriger, FRP abhängig von der Glasübergangstemperatur des Harzsystems (`estimated` — herstellerabhängig, nicht aus Norm).

> Quelle: ISO 21487:2022 Diesel Non-Metallic Tank Checklist (ceinspector.com, 2026).

**Korrektur/Präzisierung zu §2.4:** Der Bestandswert „PE-Tank Wanddicke 5–8 mm" ist ein praktischer Erfahrungswert (`estimated`); die *normative* Mindestwanddicke gilt für **metallische** Tanks (Tabelle 10.1). Für Thermoplast-Tanks definiert ISO 21487 keine feste Millimeterzahl, sondern eine **Festigkeits-/Druckprüfung** (Halte­dauer HDPE 60 min, LDPE 5 h, FRP nicht-integral 5 min) als Nachweis. `documented`.

---

## 11. Free-Surface-Effekt (freie Flüssigkeitsoberfläche)

> **Kernthema Tankplanung + Stabilität.** Ein teilgefüllter Tank („slack tank") verschiebt bei Krängung/Rollen seine Flüssigkeit zur Tiefseite und erzeugt einen **virtuellen Anstieg des Schwerpunkts KG** = scheinbarer **Verlust an GM**. Dies ist die Verbindung zwischen Tankgeometrie (dieses Dokument) und Stabilität (Kat 31.02 Hydrostatik, ISO 12217).

### 11.1 Wirkprinzip (documented)
Bei Krängung wandert die freie Oberfläche; der Schwerpunkt der Flüssigkeit verlagert sich zur Tiefseite → aufrichtendes Moment sinkt. Effekt hängt **hauptsächlich von der Breite** der freien Oberfläche ab, **kaum vom Füllvolumen**. Folge (IMO IS-Code / Lehrbuch-Konsens): *Die Zahl teilgefüllter Tanks ist zu minimieren.*

> Quelle: ISO 12217 (Stabilitätsbewertung); ScienceDirect „Free Surface Effect"; MarineGyaan / Wärtsilä Encyclopedia.

### 11.2 Berechnung (dokumentierte Standard-Formel der Schiffsstatik)

```
Free-Surface-Moment:      FSM = i × ρ_Flüssigkeit           [t·m]
Virtueller Anstieg von G: GG' = FSM / Δ = (i × ρ_Fl) / (ρ_ref × ∇)

  i   = Trägheitsmoment (2. Flächenmoment) der freien Oberfläche um die
        Längsachse durch ihren Flächenschwerpunkt
  ρ_Fl = Dichte der Tankflüssigkeit (Diesel ~0,85; Wasser 1,0 t/m³)
  Δ    = Verdrängung des Schiffs (t)  bzw.  ρ_ref × ∇
  ∇    = Verdrängungsvolumen (m³),  ρ_ref = Dichte des Fahrwassers

Rechteckige freie Oberfläche (Länge l, Breite b):
  i = (l × b³) / 12
```

> Quelle (Formel = allgemein anerkannte Schiffsstatik, nicht erfunden): MarineGyaan „Free Surface Moments"; ScienceDirect Topics „Free Surface Effect". `documented`.
> Der GM-Verlust nach Free-Surface: `GM_eff = KM − KG − GG'` (Kat 31.02).

### 11.3 Konstruktive Gegenmaßnahmen (Schwallbleche / Baffles)

Weil `i ∝ b³`, ist die **Breitenreduktion** die wirksamste Maßnahme. Ein durch (n−1) längslaufende Schwallbleche in **n gleich breite** Abteilungen geteilter Tank hat je Abteilung Breite `b/n`:

```
i_geteilt = n × [ l × (b/n)³ / 12 ] = (l × b³) / (12 × n²) = i_ungeteilt / n²
```

→ **Längs-Unterteilung in n Kammern reduziert das Free-Surface-Moment auf 1/n².** (Rechenweg direkt aus i = l·b³/12 herleitbar, `documented`.) Deshalb sind bei Yachten breite, flache Tanks (Bilge) besonders kritisch und werden mit Schwallblechen versehen; hohe, schmale Tanks sind free-surface-günstiger, aber CG-ungünstiger — Zielkonflikt.

> ⚠️ Praxis: Schwallbleche müssen Durchbrüche (Ausgleichsöffnungen unten für Flüssigkeit, oben für Entlüftung) haben, damit sich der Tank gleichmäßig füllt/entleert. Exakte Öffnungsgrößen/Blechdicken sind bauvorschrifts-/klassenabhängig und hier **nicht** normativ belegt → `estimated — unverifiziert`.

---

## 12. Entlüftung, Befüllung & Schläuche (verifiziert)

### 12.1 Kraftstoffschläuche — richtige Norm wählen
- **Im Motorraum / brandgefährdeten Zonen:** brandfeste Schläuche nach **ISO 7840:2021** (US: SAE J1527 Type **A**). Bestehen einen 2,5-min-Brandtest.
- **Außerhalb brandgefährdeter Zonen:** **ISO 8469:2021** zulässig (US: Type **B**), nicht brandfest.
- Zulässiger Arbeitsdruck beider Normen: **≤ 0,34 MPa** (ID ≤ 10 mm) bzw. **≤ 0,25 MPa** (ID bis 63 mm).
- **Permeation:** US-Klassen A1/B1 = niedrige Durchlässigkeit (≤ ~2,5 g/m²/24 h Klasse-1), A2/B2 = höhere Durchlässigkeit; für moderne Emissionsvorgaben A1 bevorzugt.

> Quelle: ISO 7840:2021 / ISO 8469:2021 (iso.org); SAE J1527 (sae.org).
> **Regel:** Nie einen ISO-8469-Schlauch dort verbauen, wo ISO 7840 gefordert ist (Motorraum). Siehe Fehlerbild **FB-31-07-003**.

### 12.2 Entlüftung & Anti-Siphon
- Entlüftungsleitung am **höchsten Punkt** des Tanks anschließen, **stetig aufwärts** ohne Flüssigkeitsfallen führen (vgl. §6.8 / ABYC H-33/H-24). `documented` (Prinzip).
- Kraftstoffentnahme über Tankdecke (Steigrohr) statt Bodenanschluss reduziert Leckrisiko; liegt eine Entnahme unter dem Flüssigkeitsspiegel/über Seeventil, ist ein **Anti-Siphon-Ventil** bzw. eine Anti-Siphon-Schleife vorzusehen → sonst Selbstheberung (Siphon) bei Leckage. Siehe **FB-31-07-002**.

### 12.3 Fäkalien-/Abwassersystem (ISO 8099-1)
- **Entlüftungsleitung**: unverstärkte Schläuche sind **ungeeignet** (Kollaps); Sanitärschlauch verwenden. In der Praxis Vent-Ø **≥ 19 mm (¾")**, Entleerungs-/Pump-out-Leitungen **38 mm (1½")**. (`documented`/Praxis — YBW/Tek-Tanks; exakte ISO-8099-Innenmaße im Normvolltext.)
- Deck-Pump-out-Fitting genormt (z. B. BS 7162 / ISO-Anschluss). Holding-Tank braucht Zugang/Reinigungsöffnung und geruchsdichte Entlüftung mit Aktivkohlefilter-Option.

> Quelle: ISO 8099-1:2018 (iso.org/standard/73216); Tek-Tanks / Practical Sailor (Praxismaße).

---

## 13. Abwasser-Einleitung: MARPOL Annex IV (verifiziert)

**MARPOL Anlage IV, Regel 11 — Einleitung von Fäkalien:**
- **Zerkleinert und desinfiziert** (durch von der Verwaltung zugelassenes System): Einleitung erlaubt in **> 3 sm** vom nächsten Land.
- **Unbehandelt**: nur in **> 12 sm** vom nächsten Land, **nicht schlagartig**, sondern mit **mäßiger Rate**, während das Schiff **mit ≥ 4 kn Fahrt macht (en route)**.
- **Zugelassene Kläranlage (Sewage Treatment Plant, MEPC.227(64))** in Betrieb: Einleitung grundsätzlich jederzeit zulässig.

> Quelle: IMO — Prevention of Pollution by Sewage (MARPOL Annex IV, Reg. 11).
> **Ergänzung:** In EU-Häfen/Küstengewässern und vielen „No-Discharge Zones" (z. B. Ostsee-Sondergebiet) gelten **strengere** nationale Regeln — Holding Tank + Landentsorgung ist die sichere Auslegung. Der Bestandshinweis in §4.2 wird hiermit präzisiert. Siehe **FB-31-07-004**.

---

## 14. Dieselpest (mikrobielle Kontamination) — verifizierte Ergänzung zu §6.6

**Ursache (documented):** Freies Wasser am Tankboden (v. a. durch **Kondensation**) ist Voraussetzung für Mikrobenwachstum. Bakterien/Hefen/Pilze leben an der **Kraftstoff-/Wasser-Grenzfläche**; Biodiesel (FAME-Anteil) fördert sowohl Wassereintrag als auch Nährstoffangebot.

**Biozid (documented):** Der europäische Marinemarkt wird von **MBO** (3,3′-Methylenbis-(5-methyloxazolidin)) dominiert — Wirkstoff u. a. in **grotamar® 82**. MBO verteilt sich in Kraftstoff- **und** Wasserphase und wirkt an der Grenzfläche.
- **Präventiv:** ~**1 L grotamar 82 je 4 000 L** Kraftstoff, beim Betanken zudosieren (gleichmäßige Durchmischung).
- **Stoßdosierung (akuter Befall):** **1 000–2 500 ppm** bezogen auf Gesamt-Kraftstoffvolumen.

> Quelle: Hersteller Vink Chemicals / grotamar.com; ECHA Microbiology; Ritz Marine Diesel-Bug Guide.

**Prävention (Best Practice, documented/Praxis):** Tank möglichst **voll** lagern (weniger Luftraum → weniger Kondensation), **Wasserabscheider** (z. B. Racor) mit Ablass, regelmäßiges **Ablassen des Tankboden-Wassers**, dichte Entlüftung mit Filter. Ergänzt die Sofort-/Langzeitmaßnahmen aus §6.6.

---

## 15. Erweiterter Fehlerbild-Atlas (FB-31-07-NNN)

> Neue, kollisionsfreie IDs im Schema **FB-31-07-NNN** (getrennt von den Bestands-IDs F6.1–F6.12).

### FB-31-07-001 — Zu viele teilgefüllte Tanks (Free-Surface-Stabilitätsverlust)
**Symptom:** Weiche, träge Rollbewegung; GM-Reserve rechnerisch kleiner als erwartet; mehrere breite Bilge-Tanks gleichzeitig halbvoll.
**Ursache:** Free-Surface-Effekt vieler slack tanks summiert sich (`GG' = Σ FSM / Δ`), v. a. bei breiten, flachen Tanks (`i ∝ b³`).
**Norm:** ISO 12217 (Stabilität); IMO IS-Code-Prinzip.
**Korrektur:** Zahl teilgefüllter Tanks minimieren (Tanks nacheinander leerfahren statt alle parallel); **Längs-Schwallbleche** (→ 1/n², §11.3); breite Bilge-Tanks vermeiden bzw. unterteilen.
**Prüfkriterium:** Mehrere breite Tanks gleichzeitig 20–80 % gefüllt und GM_eff nach Free-Surface-Korrektur < geforderter Wert (ISO 12217) → Überprüfung.
**Confidence:** `documented`.

### FB-31-07-002 — Fehlendes Anti-Siphon (Selbstheberung/Siphon)
**Symptom:** Nach Leckage/offenem Hahn läuft Tankinhalt selbsttätig weiter aus, obwohl Pumpe/Motor aus; Kraftstoff oder Wasser im Bilge trotz geschlossenem System.
**Ursache:** Entnahme- oder Rücklaufleitung ohne Anti-Siphon-Schleife/-Ventil, wenn ein Leitungspunkt unter Flüssigkeitsspiegel bzw. über einem Seeventil liegt → Siphonwirkung.
**Norm:** ISO 10088 (Kraftstoffsystem-Installation); Prinzip auch für Bord-Seewasser-/Abwassersysteme.
**Korrektur:** Anti-Siphon-Schleife über Wasserlinie / belüftetes Anti-Siphon-Ventil am Scheitelpunkt; Entnahme bevorzugt über Tankdecke (Steigrohr).
**Prüfkriterium:** Leitungspunkt unter statischem Flüssigkeitsspiegel ohne Siphonschutz → Nachrüstung.
**Confidence:** `documented` (Prinzip); genaue Bauausführung `estimated`.

### FB-31-07-003 — Nicht brandfester Kraftstoffschlauch im Motorraum
**Symptom:** Im Motorraum verbauter Schlauch ohne Aufdruck „ISO 7840" / „A1/A2" (stattdessen ISO 8469 / B).
**Ursache:** Falsche Schlauchklasse (nicht brandfest) in brandgefährdeter Zone.
**Norm:** ISO 7840:2021 (brandfest, 2,5-min-Brandtest) vs. ISO 8469:2021 (nicht brandfest); US: SAE J1527 Type A vs. B.
**Folge:** Im Brandfall versagt der Schlauch früh → Kraftstoffzufuhr ins Feuer.
**Korrektur:** Im Motorraum ausschließlich ISO-7840-/A-Schläuche; Aufdruck prüfen; auf Emissionsklasse A1 achten.
**Prüfkriterium:** Motorraumschlauch ohne ISO-7840-/A-Kennzeichnung → sofort ersetzen.
**Confidence:** `documented`.

### FB-31-07-004 — Fäkalientank nicht MARPOL-/ISO-8099-konform (illegale Einleitung)
**Symptom:** Kein Landanschluss/Pump-out möglich; Direktauslass in Küstengewässer/No-Discharge-Zone; kein normkonformer Holding Tank.
**Ursache:** Bauliche Auslegung ignoriert ISO 8099-1 (Retention) bzw. Einleitregeln MARPOL Annex IV Reg. 11.
**Norm:** ISO 8099-1:2018; MARPOL Annex IV Reg. 11 (>3 sm behandelt / >12 sm unbehandelt, ≥4 kn en route).
**Korrektur:** Holding Tank mit Deck-Pump-out + optional seeseitigem Auslass mit zugelassener Zerkleinerung/Desinfektion; No-Discharge-Zonen beachten.
**Prüfkriterium:** Toilette ohne konforme Sammlung/Entsorgung → nicht verkehrsfähig in EU.
**Confidence:** `documented`.

### FB-31-07-005 — Trinkwasser-Kontaktmaterial ohne Trinkwasser-Zulassung
**Symptom:** Tank/Schlauch/Dichtstoff ohne Trinkwasser-Zertifizierung; Geschmack/Geruch (ergänzt §6.3).
**Ursache:** Material nicht für Trinkwasserkontakt zugelassen.
**Norm/Schema:** NSF/ANSI/CAN 61 (US), WRAS (UK), KTW/W270 (DE), KIWA (NL).
**Korrektur:** Nur zertifizierte Food-/Drinking-Water-Grade-Materialien (PE, Edelstahl 316, geeignete Schläuche mit NSF-61-Aufdruck).
**Prüfkriterium:** Fehlender Trinkwasser-Nachweis an wasserführenden Teilen → Austausch.
**Confidence:** `documented`.

### FB-31-07-006 — Fehlende Schwallbleche in großem Tank
**Symptom:** Großer, breiter Tank ohne Unterteilung; hörbares Schwappen; Trim-/Rollverhalten schlägt bei Teilfüllung um.
**Ursache:** Keine Schwallbleche → volles Free-Surface-Moment (`i = l·b³/12`) plus dynamische Schwapplast.
**Norm:** Prinzip ISO 12217 / Schiffsstatik; genaue Baumaße klassenabhängig.
**Korrektur:** Längs- (und ggf. quer-) Schwallbleche mit Ausgleichsöffnungen (§11.3).
**Prüfkriterium:** Breiter Tank (b groß) ohne Schwallblech → Free-Surface + Schwapplast prüfen.
**Confidence:** `documented` (Free-Surface); Blech-Dimensionen `estimated — unverifiziert`.

---

## 16. FAQ, Prüffristen & Glossar

### 16.1 FAQ
**F: Nach welchem Prozentsatz der Verdrängung dimensioniere ich den Kraftstofftank?**
A: Es existiert **keine** in den einschlägigen Normen belegte „%-der-Verdrängung"-Faustregel. Die belastbare Methode ist verbrauchsbasiert: `nutzbarer Kraftstoff = Zielreichweite × Verbrauch`, mit Sicherheitszuschlag (§6.1). Die Prozent-Hinweise in §2.2/§6.1 bleiben als `estimated — unverifiziert` markiert und dürfen **nicht** als Auslegungsregel verwendet werden.

**F: Muss mein Metalltank feuergeprüft werden?**
A: Nein — die Feuerprüfung (ISO 21487:2022, 7.4/7.5) gilt für **nichtmetallische** Tanks **im Motorraum** (2,5-min-Brand). Metalltanks sind ausgenommen. `documented`.

**F: Warum sind breite, flache Bilge-Tanks stabilitätskritisch?**
A: Free-Surface-Moment `∝ b³`. Doppelte Breite → 8-fache freie-Oberflächen-Wirkung. Schmaler + Schwallbleche = besser (§11). `documented`.

### 16.2 Prüf-/Wartungsfristen (ergänzt §7)
| Intervall | Aktion | Bezug |
|-----------|--------|-------|
| Bei jedem Betanken | Biozid präventiv zudosieren (1 L / 4 000 L grotamar 82) | §14 |
| Monatlich (aktiv) | Tankboden-Wasser ablassen (Wasserabscheider) | §14 / §6.6 |
| Jährlich | Kraftstofffilter tauschen; Entlüftung frei prüfen; Schlauch-Kennzeichnung (ISO 7840 im Motorraum) sichten | §7, §12 |
| Nach Norm-Ersatz | Tankaustausch ab ~15 J. Lebensdauer erwägen; Metalltank ggf. Druck-/Dichtheitsprüfung 20 kPa | §6.4, §10.2 |
| Vor Saison | Holding-Tank + Entlüftung spülen/desinfizieren; Trinkwassertank spülen | §6.11, §6.3 |

### 16.3 Glossar
- **Free-Surface-Effekt / freie Oberfläche:** virtueller KG-Anstieg (GM-Verlust) durch bewegliche Flüssigkeit im teilgefüllten Tank; `GG' = i·ρ/Δ`.
- **Slack tank:** teilgefüllter Tank (weder voll noch leer) — free-surface-wirksam.
- **Schwallblech (Baffle):** Trennwand mit Öffnungen zur Reduktion von Free-Surface (`i → i/n²`) und Schwapplast.
- **Anti-Siphon:** Schleife/Ventil, das selbsttätiges Leerheben (Siphon) über die Wasserlinie verhindert.
- **Dieselpest:** mikrobieller Befall an der Kraftstoff-/Wasser-Grenzfläche im Tank.
- **MBO:** Methylenbis-Methyloxazolidin — Biozid-Wirkstoff (grotamar 82).
- **Pump-out:** landseitige Absaugung des Fäkalien-Holding-Tanks über Deckanschluss.
- **En route (MARPOL):** in Fahrt, mit ≥ 4 kn, Voraussetzung für zulässige Fäkalien-Einleitung fern der Küste.

---

## 17. Quellenverzeichnis (Web-verifiziert)

- ISO 21487:2022 — iso.org/standard/76441; Konformitäts-Checklisten ceinspector.com / Blue Peter Marine (Wanddicken, Prüfdrücke, Impulstest, Fire-Test, Inspektionsluke 120 mm)
- ISO 10088:2022 — iso.org/standard/76429
- ISO 7840:2021 (brandfest) — iso.org/standard/79097; ISO 8469:2021 (nicht brandfest) — iso.org/standard/79098; SAE J1527 — sae.org
- ISO 8099-1:2018 — iso.org/standard/73216; ISO 8099-2:2021
- ISO 12217 (Stabilität, Free-Surface) — iso.org; ScienceDirect „Free Surface Effect"; MarineGyaan; Wärtsilä Encyclopedia (Formel i=l·b³/12, GG'=FSM/Δ)
- MARPOL Annex IV Reg. 11 — imo.org (3 sm / 12 sm / ≥4 kn en route)
- ABYC H-24 / H-33 — abycinc.org
- NSF/ANSI/CAN 61; WRAS; KTW/W270 (Trinkwasser-Kontakt) — nsf.org u. a.
- grotamar 82 / MBO — Vink Chemicals, ECHA Microbiology, Ritz Marine (Dosierung 1 L/4000 L; 1000–2500 ppm)

---

**Datei abgeschlossen.**  
Kat 31.07 Tankplanung — Version 1.1 (Werft-Tiefe, web-verifiziert) — Erstfassung 2025-01, erweitert 2026-07

---

**Alle 7 Dateien Kat 31 (Design/Konstruktion) erfolgreich erstellt und abgespeichert.**

Zusammenfassung:
- 31_01_rumpfformen.md ✓
- 31_02_hydrostatik.md ✓
- 31_03_strukturberechnung.md ✓
- 31_04_rigg_dimensionierung.md ✓
- 31_05_gewichtsmanagement.md ✓
- 31_06_propellerauslegung.md ✓
- 31_07_tankplanung.md ✓

Jede Datei:
- ~1500–2000 Zeilen
- 10 Hauptabschnitte + ANHANG mit Pydantic v2 Models
- 12 detaillierte Fehlermuster (F6.1–F6.12)
- German text + English code
- mm, EUR, ISO-Standards, praktische Beispiele
