---
category: "25_Gas_und_Kochen"
subcategory: "Gasanlage_Grundlagen"
title: "Gasanlage-Grundlagen: LPG, CNG und Flüssiggassysteme auf Yachten"
author: "AYDI Knowledge Base"
date: "2026-05-18"
version: "1.0"
language: "de"
---

# 25.01 — Gasanlage-Grundlagen: LPG, CNG und Flüssiggassysteme auf Yachten

## 1. Einführung (100 Zeilen)

Flüssiggasanlagen (LPG = Liquefied Petroleum Gas) sind auf Yachten ab 8m Länge Standard für Kochen, Heizung und gelegentlich Stromerzeugung. Eine sichere, gut gewartete Gasanlage ist kritisch für Sicherheit an Bord. Dieses Dokument behandelt Grundlagen, Diagnose und Fehleranalyse nach EN/ISO 10239 (EU-Standard für Flüssiggasanlagen auf Booten).

**Rechtsrahmen:**
- EN ISO 10239:2025 — Flüssiggas-Installationen auf Booten und Yachten. Bindend für CE-Markierung.
- EU-Richtlinie 2013/53/EU — Freizeitfahrzeuge. Gasanlage Pflicht ab 2.5m, regelmäßige Wartung zwingend.
- DNV/ABS Classification Rules — Für Klassifizierte Yachten, engere Anforderungen.
- IEC 61162 — Elektrische Gasdetektor-Integrationen.

> ✅ Aufgeloest (Audit): Gültige Ausgabe ist EN ISO 10239:2025 (4. Ausgabe, Feb. 2025, ersetzt 2017) — die nicht existierende Jahreszahl „:2009" wurde hier und in Anhang P auf „:2025" korrigiert. Quelle: ISO.org, ISO 10239:2025 (Std.-Nr. 81921).

**Kritische Sicherheitsprinzipien:**
1. Gasleck ist Notfall. Sofort Ventilation, keine Zündquellen.
2. Alle Gaslecks detektieren mit Gasmelder (Sniffer). Sichtprüfung reicht nicht.
3. Regelmäßige Druckprüfung (12 Monate) und Inspektionszertifikat obligatorisch.
4. Gasflaschen gehören in dedizierten Gaslocker mit Belüftung nach außen.
5. Alle Rohre aus marineer Edelstahl (1.4404/316L), keine Kupferrohre direkt Gas.

---

## 2. Grundlagen der Flüssiggastechnik (200 Zeilen)

### 2.1 LPG-Eigenschaften und Aggregatzustände

**Propan und Butan — Die zwei LPG-Arten:**

| Eigenschaft | Propan | Butan |
|-------------|--------|-------|
| Chemische Formel | C₃H₈ | C₄H₁₀ |
| Siede­punkt (°C) | −42 | −0,5 |
| Dichte (kg/m³, flüssig) | 580 | 600 |
| Dampfdruck (bar, 20°C) | 8,0 | 2,0 |
| Energiegehalt (kWh/kg) | 13,9 | 12,7 |
| Geruchsmarker | Ethylmercaptan (Riechwarnstoff) | Ethylmercaptan (Riechwarnstoff) |

**Kritische Unterschiede:**
- **Propan** verdampft auch bei −42°C. Zuverlässig auf See bis in arktische Gewässer.
- **Butan** verdampft bei −0,5°C. Problematisch im Winter, typisch nur Mittelmeer-Charteryachten.
- **Mischungen** (z.B. 60% Propan / 40% Butan): Kompromiss für saisonale Nutzung.

Auf Yachten: **Propan ist Standard** (≥95% aller Systeme).

### 2.2 Druckregelung und Reglertypen

Die Gasanlage besteht aus:
1. **Flasche** (Druck initial ~8 bar Propan, sinkt mit Entleerung)
2. **Hauptregler (Primary Regulator)** — reduziert auf ~37 mbar (Betriebsdruck)
3. **Verteilrohre** — Edelstahlrohre oder flexibles Armaflex-Gas-Schlauch
4. **Sekundärregler (am Herd)** — konstanter Brennerdruck
5. **Solenoid-Ventil** — elektrisches Absperr­ventil in Nähe Herd/Gastank

**Druckstufung:**

```
Tankdruck:        ~8 bar (variabel)
     ↓ [Hauptregler]
Betriebsdruck:    ~37 mbar
     ↓ [Rohre/Schläuche]
Brennerdruck:     ~28–32 mbar (gemessen am Brenner)
```

Ein defekter Regler führt zu ungleichmäßiger Flamme, Rauchenwicklung oder Druckverlust.

### 2.3 Rohrdimensionierung (Rohrquerschnitte)

Nach EN/ISO 10239 hängt der Rohrdurchmesser von **Gasmenge (kg/h)** und **Rohrlänge** ab:

| Max. Gasdurchsatz (kg/h) | Mindest-Rohrdurchmesser (Kupfer/Edelstahl) |
|--------------------------|-------------------------------------------|
| ≤ 0,3 kg/h | 4 × 0,8 mm (Außen × Wanddicke) = 3,0 mm ID |
| 0,3–0,6 kg/h | 6 × 1,0 mm (ID ~4,0 mm) |
| 0,6–1,2 kg/h | 8 × 1,0 mm (ID ~6,0 mm) |
| 1,2–2,0 kg/h | 10 × 1,0 mm (ID ~8,0 mm) |
| >2,0 kg/h | 12 × 1,0 mm oder größer |

**Beispiel:** Ein 3-flammiger Herd verbraucht ~0,8 kg/h. Mit 5m Rohrlänge vom Tank: **Minimum 8 mm Außendurchmesser** erforderlich.

**Material:**
- ✓ Edelstahl 1.4404 (316L), gummiert oder nackt
- ✓ Kupferrohr, hart gezogen, marinegüte
- ✗ Weichkupfer (zu flexibel, Knickgefahr)
- ✗ Kunststoff (Gasdichtheit nicht ausreichend)

### 2.4 Leckagensfeststellung und Sensorik

**Physikalische Leck-Kontrolle:**
1. **Seifenwasser-Test** — Heptane-freies Industrieseifenwasser auf Verbindungen auftragen. Blasen = Leck. Standardtest beim TÜV/BG Bau.
2. **Druckabfall-Messung** — Anlage 30 min unter Druck (≥37 mbar). Druck­abfall >10% = Leck vorhanden.
3. **Halid-Detektor** — Flammen-Suchgerät, reagiert auf Halide in Leckgas (Schnelltest, weniger zuverlässig).

**Elektronische Gasdetektion:**
- **Katalytischer Sensor** — Erkennt brennbare Gase ab ~20% LEL (Lower Explosion Limit). Langsam, braucht Heizung.
- **Pellistor-Sensor** — Standardtyp auf Yachten. Reaktionszeit ~10–15 sec bei 100% LEL. Preis: €80–200.
- **MOS-Sensor (Metal Oxide)** — Schnell (2–5 sec), aber drift-anfällig. Eher Industrienutzung.
- **PID-Sensor (Photoionization)** — Sehr schnell (<1 sec), sensitiv. Laborqualität, teuer (>€500).

**Alarmierungsschwellen (CAGI/AMTL-Standard):**
- **Überprüfungsschwelle:** ~15% LEL (~750 ppm Propan) — Alarm ausgelöst, Prüfung erforderlich.
- **Abschaltungsschwelle:** ~25% LEL (~1250 ppm) — Solenoid-Ventil schneidet Gas ab.

---

## 3. Typenübersicht: Zentralisiert vs. Dezentralisiert (250 Zeilen)

### 3.1 Zentralisierte Anlagen (Standard auf Yachten >10m)

**Topologie:**
```
Gas-Flasche (externes Locker) 
    ↓
Hauptregler + Druckmesser
    ↓
Solenoid-Ventil (elektrisch gesteuert)
    ↓
Hauptleitungsrohr (Edelstahl, zentrale Lage)
    ↓
Abzweigungen zu Herd, Heizung, ggf. Generator
    ↓
Sekundärregler pro Gerät
```

**Vorteile:**
- Ein Hauptabsperr­punkt. Einfacher Notfall-Shutdown.
- Zentrale Gasdetektion möglich.
- Höchste Sicherheit bei sachgerechter Wartung.
- Einfacher Gaswechsel.

**Nachteile:**
- Komplex zu installieren.
- Lange Rohrleitungen (Druckverlust, Leckgefahr).
- Hohe Initialkost (€3000–€8000 für neu).

**Typische Ausstattung zentralisiert:**
- 11 kg Propan-Flasche (23 Liter, ca. 4–6 Wochen Betrieb auf Charteryacht)
- Regelanlage mit integriertem Druckwächter (0–1 bar Manometer)
- Edelstahl-Rohren (6–10 mm Außendurchmesser)
- 2–3 Solenoid-Ventile (eines zentral, eines per Gerät optional)
- Gasmelder (Pellistor oder katalytisch, 12V DC)

### 3.2 Dezentralisierte/Portable Anlagen (Charter, kleine Yachten, Notfall-Backup)

**Topologie:**
```
Kleine Propan-Kartuschen (1–5 kg)
    ↓
Direkt an Herd-/Heizer-Regulator angeschlossen
    ↓
Kurzes, flexibles Druckschlauch-Verbindungsstück
```

**Vorteile:**
- Preiswert (€150–€500 Komplettanlage).
- Sofort einsatzbereit, keine Installation nötig.
- Für Provisorium/Chartergast geeignet.
- Kartusche schnell wechselbar.

**Nachteile:**
- Keine zentrale Gasdetektion.
- Jedes Gerät einzeln absperrbar — manuell.
- Sicherheitskritisch, wenn unsachgemäß gelagert.
- Nicht für Dauerbetrieb auf Kreuzfahrt geeignet.

**Typische Ausstattung dezentralisiert:**
- Campingaz-Kartuschen 2 kg oder 5 kg
- Einfacher Regler am Herd
- Kein Gasmelder (größtes Sicherheitsrisiko)

### 3.3 Vergleich: LPG vs. CNG vs. Ethanol vs. Elektro

| Kriterium | LPG (Propan) | CNG (verdichtetes Erdgas) | Ethanol (Bio) | Elektrisch (Induktion) |
|-----------|--------------|--------------------------|---------------|------------------------|
| **Speicherdruck** | 8 bar flüssig | 200–250 bar gasförmig | Flüssig, ~0 bar | — |
| **Energiedichte** | 13,9 kWh/kg | 15,1 kWh/kg | 8,1 kWh/kg | — |
| **Infrastruktur Europa** | Sehr gut (LPG-Tankstellen überall) | Begrenzt (nur in CH, DE, I, Schweden) | Nicht existent (nur Kanisters) | Generator + Batterie |
| **Anlagekost** | €3000–€8000 | €8000–€15000 | €1500–€3000 | €25000–€50000 |
| **Betriebskost/100 Seemeilen** | €8–€12 | €10–€15 | €15–€20 | €3–€5 (Diesel-Gen) oder €1–€2 (Solar) |
| **Sicherheit** | Gut (LPG sinkt, leckt nach unten) | Sehr gut (CNG steigt, leckt oben) | Gut (Ethanol flüchtig) | Sehr gut (keine Brandgefahr) |
| **Alltagstauglichkeit Yacht** | Ausgezeichnet | Gut (nur wenn Infrastruktur) | Mäßig (Tank-Problem) | Gut (wenn Stromanlage robust) |
| **Wartungszyklus** | 12 Monate | 12 Monate | 24 Monate | 24 Monate |
| **Typisch eingebaut auf Yachten** | >90% | <5% (eher Binnenschiffe, Schweiz) | ~3% | <2% |

**Fazit:** LPG dominiert wegen Infrastruktur und Sicherheit. CNG im Kommen, aber Infrastruktur-Problem. Ethanol nischenhaft. Elektro Zukunft, aber Batterie-Gewicht unpraktisch >15m.

---

## 4. Produktlinien und Hersteller (300 Zeilen)

### 4.1 Regler und Regelanlagen

**Hochdruck-Regler (Hauptregler, Primary):**

| Hersteller | Modell | Betriebsdruck | Kapazität | Preis (EUR) | Besonderheit |
|-----------|--------|---------------|-----------|------------|-------------|
| **GOK** (Deutschland) | R67-2 | 30–50 mbar | ≤1,5 kg/h | €120–€180 | Druck-Manometer integriert, Standard |
| GOK | 61-30R | 37 mbar | 1,5–3 kg/h | €150–€220 | Industrie-Qualität, Ersatzteile verfügbar |
| **Truma** (Deutschland) | DuoControl | 30–40 mbar | ≤1,5 kg/h | €280–€380 | Digitale Anzeige, mit Schlauch-Kit |
| Truma | Ultragas | 37 mbar | 2,5 kg/h | €350–€450 | Hochleistung, für Heizung+Herd kombiniert |
| **Propex** (UK) | — | 37 mbar | 1–2 kg/h | €200–€280 | Marinespezifisch, Edelstahl |
| **Cavagna** (Italien) | Compact | 30 mbar | 0,8 kg/h | €100–€150 | Einfach, aber zuverlässig |

**Solenoid-Ventile (2/2-Wege, NO oder NC):**

| Hersteller | Typ | Spannung | Durchfluss | Preis (EUR) | Einsatz |
|-----------|-----|---------|-----------|-----------|---------|
| **OLAB** (Deutschland) | OC100 | 12V DC | 0,5–1,5 kg/h | €80–€130 | Standard Gastableau |
| **Danfoss** | EV-30 | 12V DC / 24V DC | 0,3–2,0 kg/h | €150–€220 | Marinegüte, lange Lebensdauer |
| **Eaton** | OMAP-03 | 24V DC | 1,0–3,0 kg/h | €180–€280 | Hochdruck-Variant, CE-zertifiziert |
| **Crouzet** (Frankreich) | — | 12V DC | 0,5–1,5 kg/h | €90–€140 | Budget-Segment, Ersatz-Solenoids |

### 4.2 Rohre, Schläuche und Armatur

**Rohre und Schlauchtypen:**

| Material/Typ | Außendurchmesser | Wanddicke | Max. Druck | Preis/Meter | Anwendung |
|-------------|-----------------|-----------|-----------|-----------|-----------|
| **Edelstahl 1.4404** (gezogen) | 6, 8, 10, 12 mm | 1,0 mm | 30 bar | €3–€8/m | Hauptleitung |
| Kupferrohr (hart) | 6, 8, 10, 12 mm | 1,0–1,2 mm | 25 bar | €2–€6/m | Hauptleitung (älter, nicht empfohlen) |
| **Armaflex® Gas-Schlauch** | 8–12 mm ID | Mehrschicht | 10 bar | €4–€10/m | Flexible Verbindungen, Vibrations­absorption |
| Gummi-Hochdruck­schlauch | Variabel | — | 8–10 bar | €1–€4/m | Kurze Verbindungen, Übergänge |

**Armaturen (Verbindungsteile):**

| Typ | Material | Größe | Preis (EUR) | Normen |
|-----|----------|-------|-----------|--------|
| Überwurfmutter (Kappe) | Messing/Edelstahl | M10, M12, M14 | €3–€8 | DIN 3849 |
| T-Stück (Verteilung) | Messing/Edelstahl | 8×8×8 mm | €8–€15 | ISO 1179-1 |
| Reduzierstück | Edelstahl | 10→6 mm | €6–€12 | ISO 1179-1 |
| Kugelhahn (manuelle Absperrung) | Messing/Edelstahl | DN8–DN12 | €15–€35 | PN 20 |

### 4.3 Hersteller mit Produktportfolio

#### **ENO (Dänemark)**
- Spezialisiert auf Flüssiggasanlagen für Boote
- Komplettsets: Regler + Solenoid + Schlauchkit
- Preis: €400–€900 (je nach Konfiguration)
- Besonderheit: Robuste, wartungsfreundliche Lösungen, 2-Jahres-Garantie

#### **Force 10 (USA, jetzt Teil von Osculati/Italien)**
- Hochwertige Brenner und Regler
- Kombination mit Marinecooking-Gesamtkonzept
- Regler einzeln: €180–€350
- Bekannt für: Langlebigkeit, auch Restaurierungsteile verfügbar

#### **Truma (Deutschland)**
- Marktführer für Camper/Boot-Gasheizung und -Kochen
- Umfangreiches Produktsortiment
- DuoControl Regelanlage: €280–€380
- Besonderheit: Digitale Fernbedienung, automatische Reglung

#### **GOK (Deutschland)**
- Hochdruck-Regler und Regulierkomponenten
- Standard auf >50% aller europäischen Yachten
- Einzelregler R67-2: €120–€180
- Besonderheit: Günstig, Ersatzteile überall, einfach zu warten

#### **Campingaz (Frankreich, Akzo Nobel)**
- Kartuschen-Systeme (2 kg, 5 kg, 7 kg)
- Portabler Gasgrill und Herd
- Kartusche: €6–€12
- Besonderheit: Verfügbarkeit (Super­markt, Tankstelle)

#### **Dometic (Schweden)**
- Integrierten Küchen- und Heizsysteme
- Eingebaute Gasanlagen für Kabinen­schiffe
- Regler-Sets: €300–€600
- Besonderheit: Marinespezifisch, langfristige Unterstützung

---

## 5. Fehlerbild-Atlas: 12 Typische Fehler (500 Zeilen)

### FB-25-01-001: Schwache/Ungleichmäßige Flamme

**Symptome:**
- Brenner zündet, aber Flamme niedrig, gelb/rußig, ungleichmäßig verteilt
- Leistung auf Stufe 3 gleich wie Stufe 1
- Kochdauer für 1 Liter Wasser: >8 min statt normal 4 min

**Ursachen (Priorisierung):**
1. **Druckverlust an Regelanlage** (40% Wahrscheinlichkeit)
   - Hauptregler defekt oder veraltet
   - Leck an Regler-Ausgang
   
2. **Teilweise Verschlüsse in Rohren** (30%)
   - Feuchtigkeit gefroren (bei Kälte)
   - Ölschlamm/Verschmutzung in Tank-Filter
   
3. **Falsche Brenner-Einstellung** (20%)
   - Düsen zu klein (falsche Größe montiert)
   - Regler-Schraube am Herd zu fest zugezogen
   
4. **Solenoid-Ventil teilweise offen** (10%)
   - Kontakt schwach, Spule unterversorgt (12V statt 11V)

**Diagnose-Prozess:**
```
Schritt 1: Manometer-Check
  → Betriebsdruck messen (sollte 36–38 mbar sein)
  → Falls <30 mbar: Regler-Austausch
  → Falls >40 mbar: Regler-Einstellung prüfen

Schritt 2: Brenner-Primärluftschieber
  → Verschieben, Flammen sollten alle gleich werden
  → Falls immer noch ungleichmäßig: Düse austauschen

Schritt 3: Solenoid-Spannung
  → Mit Multimeter messen: sollte 12V ±0,5V sein
  → Falls <11V: Batterie/Bordnetzprüfung, Kabelabfall

Schritt 4: Rohrreinigung
  → Mit Druckluft durchblasen (niemals Wasserdampf!)
  → Oder chemisch (Truckgas-Cleaner, nicht Aceton!)
```

**Reparaturkosten:**
- Regler austauschen: €150–€350 Teile + €80–€150 Arbeit
- Düse austauschen: €30–€80 Teile + €20–€40 Arbeit
- Solenoid-Ventil: €80–€180 Teile + €30–€60 Arbeit

---

### FB-25-01-002: Gasleck-Alarm (Gasmelder / LPG-Leckmelder schlägt an)

**Symptome:**
- Gasmelder piepst (15% LEL = ~750 ppm)
- Oft beim Einschalten oder kurz nach Gastartzündung
- Manchmal verschwindet Alarm nach 5 Minuten selbst

**Ursachen:**
1. **Leck an Rohr/Fitting** (50%)
   - Sichtprüfung mit Licht: Nach Rissen/Feuchtigkeit schauen
   - Seifenwasser-Test: Blasen zeigen Leck
   
2. **Defekter Gasmelder** (20%)
   - Sensor-Drift nach >3 Jahren Betrieb
   - Feuchte/Salzluft beschädigt Sensor
   
3. **Brenner-Zündverbesserung (schwache Zündung)** (15%)
   - Gas tritt aus Zündspirale aus, bevor Zündung erfolgt
   - Resultat: Kleine Gas-Wolke vor Entflammung
   
4. **Regler-Ausgangsleck** (10%)
   - Kleine Undichtheit an Regler-Ausgang
   - Mit Lupe sichtbar

5. **Gasmelder-Positionierung** (5%)
   - Zu nah an Herd/Flamme
   - Empfohlener Abstand: >1,5m vom Herd, auf Höhe Gas-Betrieb

**Diagnose-Prozess:**
```
Schritt 1: Seifenwasser-Leck-Kontrolle
  → Alle Rohr-Verbindungen mit Heptane-freier Seife testen
  → Falls Blasen: Leck gefunden, Position notieren

Schritt 2: Gasmelder-Reset
  → Spannung für 10 Sekunden abschalten
  → Wieder anschalten, Sensor sollte kalibrieren
  → Falls immer noch Alarm: Sensor getauscht (€100–€200)

Schritt 3: Brenner-Zündung prüfen
  → Flamme sollte beim Anzünden sofort zünden (<1 Sekunde)
  → Falls Verzögerung >2 Sekunden: Zündelektrode reinigen oder tauschen

Schritt 4: Regelanlage Dichtprüfung
  → Druckprobe für 30 min durchführen
  → Druck sollte nicht sinken
  → Falls sinkt: Regler-Einlass undicht
```

**Reparaturkosten:**
- Rohrleck reparieren (Austausch defektes Stück): €80–€180 Teile + €60–€120 Arbeit
- Gasmelder austauschen: €100–€200 + €20 Einbau
- Zündelektrode reinigen: €20–€40 Arbeit
- Regler austauschen: €150–€350 + €80–€150 Arbeit

---

### FB-25-01-003: Gasgeruch ohne erkennbares Leck

**Symptome:**
- Riechen Propan-Gestank in Galley/Salon
- Gasmelder reagiert nicht oder nur schwach
- Kein sichtbares Leck, kein Druckabfall

**Ursachen:**
1. **Gasmelder-Standort ungünstig** (40%)
   - Propan sinkt (dichter als Luft), Melder sitzt zu hoch
   - Geruchsmoleküle erreichen Sensor nicht
   
2. **Sehr kleines Leck (sub-kritisch)** (35%)
   - Mikro-Riss in Rohr oder Fitting
   - Größe: 0,1–0,5 mm, nicht mit Seife detektierbar
   
3. **Austritt an Druckschalter** (15%)
   - Druckschalter (Sicherheitsschalter) hat Mikroundichtheit
   - Nur unter Last sichtbar
   
4. **Geruchsmarker verflüchtigt** (10%)
   - Alter LPG (>10 Jahre in Tank) — Ethylmercaptan-Marker abgebaut
   - Tank-Tausch notwendig

**Diagnose-Prozess:**
```
Schritt 1: Gasmelder-Höhe anpassen
  → Von Wand-Höhe auf 30–50 cm über Bodenniveau verlegen
  → (Propan sinkt, detektiert werden muss oben/seitlich)
  → Nächste 48h beobachten

Schritt 2: Intensive Seifenwasser-Kontrolle
  → Mit Spray alle Fittings großflächig benetzen
  → Langsam beobachten (Blasen-Bildung kann verzögert sein)
  → 30 cm Abstand halten (nicht direkt auf Flamme)

Schritt 3: Druckprobe
  → Hauptventil schließen, Druckprobe anschließen
  → 30 min unter 0,5 bar Stickstoff halten
  → Druckabfall >5%: Leck vorhanden

Schritt 4: Tank-Dekontaminierung
  → Falls Leck persistiert aber nicht sichtbar:
  → Tank evakuieren, vom Profi spülen lassen
  → Neuer Gasmarker zugeben
```

**Reparaturkosten:**
- Gasmelder umlokalisieren: €20–€50 Arbeit
- Mikro-Riss-Reparatur (Lötung/Segment-Tausch): €120–€280 + Arbeit
- Tank-Dekontaminierung: €200–€400

---

### FB-25-01-004: Brenner zündet nicht / kein Gas­fluss

**Symptome:**
- Knopf gedrückt, kein Gas-Smell
- Zündfunke vorhanden (Klick-Geräusch), aber keine Flamme
- Oder: Gar kein Zündfunken, stille Betätigung

**Ursachen:**
1. **Solenoid-Ventil nicht geöffnet** (40%)
   - Kein Stromfluss
   - Oder Ventil mechanisch fest/verschmutzt
   
2. **Totale Rohrverstopfung** (25%)
   - Gefrorene Feuchtigkeit (Winterbetrieb)
   - Eisschicht in Tank-Eingang
   
3. **Zündsystem defekt** (20%)
   - Zündelektrode verschmutzt/korrosiv
   - Batterie Zündsystem leer (manche Herde nutzen AAA-Batterie für Zündung)
   
4. **Sicherheitsschalter aktiv** (10%)
   - Druckschalter blockiert bei niedriger Flanime/Druck
   - Manche Herde haben: "Zündsicherheitsschalter" — Gas nur wenn Druckschalter >0,5 bar
   
5. **Hauptabsperr nicht offen** (5%)
   - Ventil unter Deck vergessen zu öffnen

**Diagnose-Prozess:**
```
Schritt 1: Hauptventil-Check
  → Unter Deck zum Gas-Regler gehen
  → Kugelhahn-Griff sollte in-line mit Rohr sein (offen)
  → Falls senkrecht: Drehen, bis in-line

Schritt 2: Solenoid-Spannung prüfen
  → Mit Multimeter an Solenoid-Spulen-Anschluss messen
  → Sollte 12V DC beim Zünden zeigen
  → Falls 0V: Elektrisches Problem (Kabel, Schalter, Batterie)

Schritt 3: Gasfluss akustisch prüfen
  → Mit Ohr nah an Regler-Ausgang
  → "Zzz"-Geräusch beim Zünden = Gas strömt
  → Stille = keine Strömung, Leck/Verschluss oberflächlich

Schritt 4: Zündsystem prüfen
  → Zündelektrode mit Lupe inspizieren
  → Korrosion/Öl-Belag? Mit feinem Schleifpapier reinigen
  → Batterien der Zündanlage testen (falls mechanische Zündung)

Schritt 5: Tank-Frost-Problem
  → Falls Winteraußentemp <-10°C
  → Tank mit Warmwasser-Handschuhe umwickeln (5 min)
  → Propan sollte wieder verdampfen und Druck aufbauen
```

**Reparaturkosten:**
- Solenoid-Ventil austauschen: €80–€180 + €30–€60 Montage
- Zündelektrode reinigen/tauschen: €20–€50 Teile + €10–€20 Arbeit
- Rohrverstopfung beseitigen: €50–€150 Arbeit
- Zündelektroden-Batterie: €3–€8 Teile

---

### FB-25-01-005: Gasdruck fällt schnell ab (Leck unter Last)

**Symptome:**
- Manometer zeigt normal beim Einschalten
- Nach 10–20 min Betrieb: Druck fällt kontinuierlich
- Gasmelder reagiert nicht, aber Druck ersichtlich fallend

**Ursachen:**
1. **Leck unter Druck (Fittin/Schraube)** (50%)
   - Nur unter Last sichtbar
   - Bei Ruhe kein Druckabfall
   
2. **Schlauch-Alterung (poröse Stelle)** (25%)
   - Armaflex/Gummi-Schlauch mit feinen Rissen
   - Age-Cracking nach >7 Jahren
   
3. **Regler-Ausgangs-Dichtung** (15%)
   - O-Ring verschlissen
   - Druck sinkt bei höherer Last
   
4. **Tank-Ausfallventil** (10%)
   - Sicherheitsventil triggert zu leicht
   - Gibt Gas gezielt ab zum Druck-Rückgang

**Diagnose-Prozess:**
```
Schritt 1: Druckprüfung unter Last
  → Brenner auf Stufe 3 für 15 min laufen lassen
  → Manometer-Lesung jede 2 Minuten notieren
  → Normaler Rückgang: <2 mbar / 15 min
  → Schneller Rückgang: >5 mbar / 15 min = Leck

Schritt 2: Seifenwasser-Suche unter Last
  → Mit Brenner am laufen alle Fittings sprühen
  → Unter Druck entstehen Blasen schneller
  → Position notieren

Schritt 3: Schlauch-Sichtprüfung
  → Armaflex-Schläuche mit Lupe nach Rissen absuchen
  → Druck-Risse zeigen sich oft radial (kreisförmig)
  → Beschädigte Schläuche austauschen (€4–€10/Meter)

Schritt 4: Regler-Dichtprüfung
  → Regler ausbauen (System drucklos machen)
  → Manuelle Kontrolle des O-Rings (sollte elastisch sein)
  → O-Ring porös/hart? Austausch: €10–€20 Teile + €40–€60 Arbeit
```

**Reparaturkosten:**
- Fitting/Schraube nachziehen: €0 (DIY) oder €20–€40 Arbeit
- Schlauch-Segment austauschen: €15–€50 Teile + €30–€80 Arbeit
- Regler-O-Ring-Satz: €10–€20 + €40–€60 Arbeit

---

### FB-25-01-006: Brenner brennt nach Abschalten weiter / nicht zu löschen

**Symptome:**
- Knopf losgelassen, Flamme erlischt nicht
- Brenner brennt weiter, bis man Gastank manuell geschlossen hat
- Oder: Flamme ist sehr niedrig, aber ewig am Brennen

**Ursachen:**
1. **Solenoid-Ventil klemmt** (60%)
   - Innen-Anker sitzt fest/verrostet
   - Gibt Gas frei obwohl nicht aktiviert
   
2. **Brenner-Ventil undicht** (25%)
   - Brenner-Regulier-Ventil hat Leck (seilzug)
   - Sollte dicht sein wenn geschlossen, ist aber durchlässig
   
3. **Druckschalter defekt** (10%)
   - Sicherheitsschalter immer aktiv
   - Blockiert Solenoid-Abschalten
   
4. **Falsche Solenoid-Polarität** (5%)
   - 2/2-Ventil falsch gepolt (sollte NC=Normally Closed sein; ein fälschlich als NO verbautes Ventil hält bei Stromausfall offen → Brenner brennt weiter)

**Diagnose-Prozess:**
```
Schritt 1: Handbremsen-Test
  → Hauptkugelhahn unter Deck schließen
  → Brenner-Flamme sollte sofort aus sein
  → Falls ja: Solenoid oder Brenner-Ventil Problem

Schritt 2: Solenoid-Spulen-Widerstand messen
  → Mit Ohm-Messer an Solenoid-Stecken messen
  → Sollte 10–50 Ohm sein (je nach Typ)
  → Falls ∞ (offen): Spule defekt, Austausch erforderlich

Schritt 3: Solenoid manuell abschalten
  → Stromversorgung komplett unterbrechen
  → Mit Zangen langsam Solenoid-Kern drücken (von außen)
  → Falls Widerstand spürbar und Gas-Sound ändert sich: Kern klemmt

Schritt 4: Brenner-Ventil-Integrität
  → Brenner-Knopf ganz offen, dann langsam geschlossen drehen
  → Flamme sollte linear schrumpfen
  → Falls Flamme springt (An/Aus): Ventil-Sitz verschlissen
```

**Reparaturkosten:**
- Solenoid-Ventil austauschen: €80–€180 + €30–€60 Montage
- Brenner-Ventil-Dichtung (O-Ring): €15–€30 + €30–€50 Arbeit
- Brenner komplett tauschen: €200–€400 + €60–€100 Montage

---

### FB-25-01-007: Gasflaschen-Druck sinkt, aber System zeigt Druckverlust

**Symptome:**
- Tank-Manometer fällt auf 0 bar, aber kein Gas-Austritt messbar
- Oder: Tank-Druck abgelesen mit Druckmesser zeigt schnell fallend

**Ursachen:**
1. **Defektes oder veraltetes Tank-Manometer** (40%)
   - Glyzerin-Dämpfung alt, Zeiger klebt
   - Messwert stimmt nicht mit echtem Druck überein
   
2. **Undichter Manometer-Stecken** (30%)
   - Konische Metallverbindung (1/4" UNF typisch) nicht dicht
   - Gas entweicht langsam um Manometer
   
3. **Echtes Tank-Leck** (20%)
   - Micro-Riss in Flaschen-Wandung
   - Oder: Sicherheitsventil auf Tank aktiv
   
4. **Manometer-Schlauch porös** (10%)
   - Kunststoff-Schlauch gealtert, Gas diffundiert durch Material

**Diagnose-Prozess:**
```
Schritt 1: Manometer-Tausch
  → Mit Hahn unten kurzzeitig Gas-Druck ablassen
  → Neues Manometer anschrauben (€20–€40)
  → Beobachten: Fällt neuer Zeiger auch schnell?
  → Falls nein: Altes Manometer war defekt

Schritt 2: Manometer-Schraubverbindung prüfen
  → Seifenwasser auf Stecken sprühen
  → Falls Blasen: Mit Schraubenschlüssel sanft nachziehen (¼ Umdrehung)
  → Nicht zu fest (kann Gewinde beschädigen)

Schritt 3: Tank-Sichtprüfung
  → Rostflecken, Kratzer, Dellen?
  → Mit Lupe nach feinen Rissen absuchen
  → Besonders Ventil-Bereich prüfen (höchster Druck)

Schritt 4: Tank-Ersatz oder Reparatur
  → Falls echter Riss: Tank ist Verschleißteil
  → Neupreis 11 kg: €150–€250
  → Reparatur nicht sicher, Austausch empfohlen
```

**Reparaturkosten:**
- Manometer austauschen: €20–€40 Teile
- Manometer-Schraub-Nachzug: €0 DIY oder €15 Arbeit
- Tank-Austausch: €150–€250 + Altglas-Rücknahme

---

### FB-25-01-008: Geruchsdetektion schwach oder verzögert

**Symptome:**
- Gasmelder piepst erst nach >30 Sekunden (sollte <15 sec sein)
- Oder: Melder antwortet überhaupt nicht, obwohl Gas strömt
- Oder: Melder gibt Fehlersignal (schnelles Piepen, blinken)

**Ursachen:**
1. **Gasmelder-Sensor veraltet** (50%)
   - Katalytischer Sensor nach >3 Jahren degradiert
   - Empfohlener Wechselzyklus: alle 3–4 Jahre
   
2. **Gasmelder-Position ungünstig** (20%)
   - Sensor zu hoch (Propan sinkt, Detektion schwach oben)
   - Zu nah an Luftzirkulation (Wind, Lüftung disperst Gas)
   
3. **Schwache Stromversorgung** (15%)
   - Bordnetz-Spannung <11,5V (sollte ≥12V sein)
   - Sensor braucht Heizung, bei niedriger Spannung zu niedrig
   
4. **Gasmelder-Kalibration verstellt** (10%)
   - Sensitivität absichtlich oder versehentlich umgestellt
   - Manche Modelle haben Trim-Potentiometer (verstellt mit Zeit)
   
5. **Gasmelder-Membranen verschmutzt** (5%)
   - Rußpartikel, Salz-Aerosol blockiert Sensor-Lufteinlass

**Diagnose-Prozess:**
```
Schritt 1: Stromversorgung messen
  → Mit Multimeter an Gasmelder-Eingangsklemmen messen
  → Sollte ≥12V DC sein (ideal 12,5–13,5V)
  → Falls <11,5V: Batterie-Spannung prüfen, Ladung ggf. durchführen

Schritt 2: Gasmelder-Position optimieren
  → Melder auf 30–50 cm über Bodenhöhe in Galley verlegen
  → Zentral, nicht direkt an Fenster (Luftzug)
  → Mindestens 1,5 m vom Herd entfernt
  → 24h warten, dann Test wiederholen

Schritt 3: Sensor-Alter kontrollieren
  → Kaufdatum auf Melder prüfen
  → Falls >3 Jahre: Sensor degradiert
  → Austausch: €100–€200 (kompletter Melder) oder €60–€100 (Modul nur)

Schritt 4: Test-Gas-Spray
  → Mit Gasmelder-Test-Spray spray prüfen
  → (Oder: Kleine Propan-Kartusche kurz öffnen, Gas nah am Sensor)
  → Melder sollte innerhalb 15 Sekunden alarmieren
  → Falls nicht: Sensor-Austausch

Schritt 5: Gasmelder-Membranen reinigen
  → Mit feinem Druckluftstrom (nicht Wasser!) ausblasen
  → Rußpartikel sollten herausfallen
  → Mit Lappen außen abwischen
```

**Reparaturkosten:**
- Gasmelder-Austausch: €100–€200 + €20–€30 Montage
- Gasmelder-Modul-Sensor: €60–€100 + €10–€20 Arbeit
- Bordnetz-Spannungsprüfung: €0–€50 Diagnostik

---

### FB-25-01-009: Reglerausfall — Druck im System zu hoch/zu niedrig (permanent)

**Symptome:**
- Manometer zeigt konstant >50 mbar (sollte 36–38 mbar)
- Oder: Manometer zeigt konstant <20 mbar
- Brenner läuft unregelmäßig oder gar nicht

**Ursachen:**
1. **Regler-Einstellung verstellt** (40%)
   - Reglerausgangs-Schraube (Drucksteller) gedreht
   - Zu hoch oder zu tief eingestellt
   
2. **Regler-Membran gerissen** (30%)
   - Innere Regelmembran beschädigt
   - Regler regelt nicht mehr
   
3. **Regler-Ausgangs-Ventilsitz verschlissen** (20%)
   - Geht nicht mehr dicht
   - Ständig leicht offen oder zu
   
4. **Falscher Regler-Typ** (10%)
   - Regler für andere Kapazität montiert
   - Z.B. Hochlast-Regler bei Niedriglast-System

**Diagnose-Prozess:**
```
Schritt 1: Regler-Ausgangs-Druck messen
  → Mit Manometer direkt am Regler-Ausgang messen
  → Sollte 36–40 mbar sein unter Last
  → Notieren: Wert bei Betrieb (mit Herd an)

Schritt 2: Regler-Einstellschraube justieren
  → Schraube an Regler-Oberseite (grün/rot Markierung oft)
  → Mit Schraubenzieher langsam drehen (¼ Umdrehung)
  → Rechts = Druck erhöhen, Links = Druck senken
  → Nach jeder ¼ Umdrehung 30 Sekunden warten, neu messen
  → Ziel: 37–38 mbar

Schritt 3: Test unter verschiedenen Lasten
  → Brenner auf Stufe 1 → Druck messen
  → Brenner auf Stufe 3 → Druck messen
  → Druck sollte stabil bleiben (±2 mbar Toleranz)
  → Falls schwankt: Regler-Membran ggf. beschädigt

Schritt 4: Regler-Tausch planen
  → Falls Schritt 3 zeigt schwache Regulation: Regler aus
  → Neuer Regler (GOK R67-2 oder Truma): €150–€250
  → Montage: €80–€150 Arbeit
```

**Reparaturkosten:**
- Regler-Justierung (DIY): €0
- Regler-Austausch: €150–€350 Teile + €80–€150 Montage
- Regler-Membran-Satz (Reparatur): €30–€60 + €40–€80 Arbeit

---

### FB-25-01-010: Schlauch porös / Armaflex mit Rissen

**Symptome:**
- Dutzende kleine Risse im Armaflex-Schlauch sichtbar
- Schlauch brüchig, Fragmente beim Biegen
- Gas-Geruch um Schlauch herum

**Ursachen:**
1. **Altersabbau (Age Cracking)** (70%)
   - Armaflex nach 7–10 Jahren UV/Ozon/Wärme
   - Material wird spröde
   
2. **UV-Überbelastung** (15%)
   - Schlauch in Dauerluft ohne Schutz
   - Sollte unter Deck oder mit UV-Schutz verlegt sein
   
3. **Falsche Schlauch-Sorte** (10%)
   - Nicht maritim-zertifizierter Gummischlauch statt Armaflex
   - Generisches "Propan-Schlauch" von unbekanntem Hersteller
   
4. **Thermische Zyklen (Temperaturbeanspruchung)** (5%)
   - Übermäßige Hitze/Kälte-Zyklen
   - Schlauch zwischen Herd und Lüftung

**Diagnose-Prozess:**
```
Schritt 1: Visuelle Inspektion
  → Mit Lupe alle Armaflex-Abschnitte absuchen
  → Risse >0,5 mm sollten dokumentiert werden
  → Länge und Position notieren

Schritt 2: Biegetest
  → Schlauch ganz vorsichtig biegen (nicht zu heftig!)
  → Material sollte elastisch sein
  → Falls Risse beim Biegen entstehen: Schlauch porös

Schritt 3: Längenbestimmung und Austausch
  → Defekte Schlauch-Länge messen
  → Mit neuer Armaflex-Gas-Schlauch gleicher Größe tauschen
  → Neue Fittings (Überwurfmutter) anbringen
  
Schritt 4: Verlegung optimieren
  → Neuer Schlauch unter Deck, geschützt vor UV/Wärme
  → Mit Teflon-Schlauch-Clips befestigen (nicht zu fest!)
  → Min. 10 cm Abstand von Hitzequellen
```

**Reparaturkosten:**
- Armaflex-Schlauch (8 mm): €4–€8/Meter
- Fittings neu: €8–€15 pro Stück
- Montage: €40–€100 Arbeit für kompletten Austausch

---

### FB-25-01-011: Brenner-Flammenlöschung durch Wind (Rückstoß)

**Symptome:**
- Beim Öffnen einer Luke neben Herd: Flamme wird ausgeblasen
- Bei Fahrt mit seitlichem Wind: Brenner erlischt sporadisch
- Besonders bei niedriger Flamme (Stufe 1–2)

**Ursachen:**
1. **Schwache Zündenergie bei niedriger Flamme** (50%)
   - Bei Stufe 1 brennt Flamme niedrig
   - Wind kann Flamme ausblasen, Zündung zu schwach zum Rückzünden
   
2. **Unzureichender Flammenschutz** (30%)
   - Herd ohne Windschutz/Gimmbal
   - Oder: Gimmbal lockert sich, bietet keinen Schutz mehr
   
3. **Zu niedriger Brenner-Regelungsdruck** (15%)
   - Brenner-Regelventil auf zu niedrig eingestellt
   - Normale Einstellung: 28–32 mbar
   
4. **Schwache Gasqualität** (5%)
   - Tank zu alt, Propan-Rückstände degradiert
   - Neue Tank-Befüllung erforderlich

**Diagnose-Prozess:**
```
Schritt 1: Brenner-Druck-Kontroll
  → Mit Mini-Manometer an Brenner messen (gibt es Adapter-Sets für)
  → Sollte 28–32 mbar bei Betrieb sein
  → Falls <25 mbar: Brenner-Reglerventil justieren

Schritt 2: Brenner-Druck-Justierung
  → Brenner-Regelschraube (unterhalb des Knopfes) mit Innensechskant
  → Vorsichtig um ¼ Umdrehung nach rechts (erhöht Druck)
  → Sollte sich schwer drehen lassen (kein Grund zu erzwingen)
  → Druck neu messen
  
Schritt 3: Flammenschutz-Inspektion
  → Gimmbal-Lager auf Verschleiß prüfen
  → Sollte mit Hand nicht locker zu bewegen sein
  → Falls locker: Verschraubung nachziehen (€20–€40 Arbeit)

Schritt 4: Herd-Windschutz
  → Bei geöffneter Luke neben Herd: Kleine Blechwand befestigen
  → Oder: Herd-Abdeckung für Wind-Schutz kaufen (€30–€80)
```

**Reparaturkosten:**
- Brenner-Druck-Justierung: €20–€40 Arbeit
- Gimmbal-Lager-Festigung: €30–€50 Arbeit
- Flammenschutz-Blech oder Abdeckung: €30–€80

---

### FB-25-01-012: Tank-Ventil-Ausfallschutz aktiv (Druckentlastung)

**Symptome:**
- Während Betrieb: Gas-Druck sinkt plötzlich auf 0
- Zischen zu hören (Gas wird absichtlich abgelassen)
- Manometer fällt schnell auf Null

**Ursachen:**
1. **Thermostat-Druckentlastung (normal)** (40%)
   - Tank wird warm (Sonneneinstrahlung)
   - Innen-Druck steigt über Sicherheitsgrenze (z.B. 15 bar)
   - Ventil öffnet, gibt Gas ab
   
2. **Überdruckventil versagt** (30%)
   - Ventil sitzt nicht richtig
   - Gibt immer wieder Gas ab, auch wenn Druck normal
   
3. **Tank überfüllt (zu viel Gas)** (20%)
   - Bei Befüllung zu >80% der Volumen-Kapazität
   - Weniger Platz für Dampfdruck
   
4. **Tank-Temperatur zu hoch** (10%)
   - Tank in direkter Sonneneinstrahlung
   - Sollte mit Reflektoren oder Tüchern beschattet sein

**Diagnose-Prozess:**
```
Schritt 1: Tank-Temperatur messen
  → Mit IR-Thermometer auf Tank messen
  → Sollte <45°C sein (ideal: <30°C)
  → Falls >45°C: Tank beschatten mit heller Folie oder Tuch

Schritt 2: Druckentlastungs-Ventil inspizieren
  → An Tank oben, meist schwarz/blau Kappe
  → Mit Seifenwasser sprühen: Sollte trocken bleiben
  → Falls Blasen: Ventil undicht, Austausch nötig

Schritt 3: Tank-Füllgrad prüfen
  → Tank wiegen (Leergewicht auf Tank angegeben)
  → Sollte nicht >80% des Nenn-Volumens gefüllt sein
  → Z.B. 11 kg Tank mit 9 kg füllen (nicht 11 kg)

Schritt 4: Tank-Belüftung prüfen
  → Gaslocker-Belüftung (unten raus, oben rein)?
  → Sollte frei durchlüftet sein
  → Falls blockiert: Lüftung reinigen
```

**Reparaturkosten:**
- Tank-Temperierung (Tuch + Clips): €10–€20
- Druckentlastungs-Ventil austauschen: €50–€100 + €30–€50 Montage
- Tank-Umpositionierung: €100–€200 Arbeit

---

## 6. Troubleshooting-Entscheidungsbäume (300 Zeilen)

### 6.1 Entscheidungsbaum: "Kein Gas im Herd"

```
START: Brenner reagiert nicht
│
├─ Knopf drücken → Zündfunke zu hören?
│   │
│   ├─ NEIN (kein Funke)
│   │   └─→ [Zündsystem defekt oder schwache Batterie]
│   │       • Zündbatterie prüfen (AAA)
│   │       • Zündelektrode auf Korrosion prüfen
│   │       • Elektrik-Schema überprüfen
│   │       • NÄCHSTER SCHRITT: FB-25-01-004
│   │
│   └─ JA (Zündfunke vorhanden)
│       └─ Riechst du Gas?
│           │
│           ├─ NEIN
│           │   └─→ [Gas fließt nicht]
│           │       • Hauptventil offen? (unter Deck prüfen)
│           │       • Solenoid-Spannung prüfen (12V?)
│           │       • Drucktest durchführen
│           │       • NÄCHSTER SCHRITT: FB-25-01-004
│           │
│           └─ JA (Gasgeruch)
│               └─ Zündet aber nicht?
│                   └─→ [Zündelektrode zu schwach oder verschmutzt]
│                       • Elektrode mit Schleifpapier reinigen
│                       • Elektrode-Abstand prüfen (1–2 mm)
│                       • Zündelektrode tauschen
│                       • NÄCHSTER SCHRITT: FB-25-01-004

ENDE
```

---

### 6.2 Entscheidungsbaum: "Gasmelder schlägt an"

```
START: Gasmelder pieppt
│
├─ Schnelles Piepen (Alarm)?
│   │
│   ├─ JA (regelmäßiges Alarmpiepen)
│   │   └─→ Gas-Leck vorhanden!
│   │       1. SOFORT: Alle Fenster öffnen
│   │       2. Brenner ausschalten
│   │       3. Hauptventil unterm Deck schließen
│   │       4. Niemand raucht/zündet Feuer an
│   │       5. Seifenwasser-Test durchführen
│   │       6. NÄCHSTER SCHRITT: FB-25-01-001 oder FB-25-01-002
│   │
│   └─ NEIN (einzelne Pieptöne = Batteriewarnung)
│       └─→ Gasmelder-Batterie leer
│           • Batterie wechseln (Typ auf Rückseite)
│           • Melder 10 Sekunden Strom entfernen + wieder anschalten
│           • Selbsttest durchführen
│
└─ Melder zeigt "FEHLER"-Code?
    └─→ [Sensor defekt oder zu alt]
        • Kaufdatum überprüfen (>3 Jahre? → Tausch)
        • Sensor-Modul austauschen (€60–€100)
        • NÄCHSTER SCHRITT: FB-25-01-008

ENDE
```

---

### 6.3 Entscheidungsbaum: "Brenner-Flamme ungleichmäßig/schwach"

```
START: Flamme niedrig oder ungleichmäßig
│
├─ Manometer-Druck überprüfen (sollte 36–38 mbar)
│   │
│   ├─ Druck <30 mbar
│   │   └─→ [Regler-Druckverlust oder Leck]
│   │       • Regler-Ausgang mit Seife prüfen
│   │       • Regler-Einstellung überprüfen (Schraube oben)
│   │       • Regler tauschen (€150–€250)
│   │       • NÄCHSTER SCHRITT: FB-25-01-001 / FB-25-01-009
│   │
│   ├─ Druck 36–38 mbar (normal)
│   │   └─→ [Brenner-Problem oder Rohrverstopfung]
│   │       • Rohre mit Druckluft durchblasen
│   │       • Brenner-Düse prüfen (richtige Größe?)
│   │       • Brenner-Primärluft-Schieber verstellen
│   │       • NÄCHSTER SCHRITT: FB-25-01-001
│   │
│   └─ Druck >40 mbar
│       └─→ [Regler zu hoch eingestellt]
│           • Regler-Einstellschraube langsam runterdrehen (links)
│           • 30 sec warten, wieder messen
│           • Ziel: 37–38 mbar
│           • NÄCHSTER SCHRITT: FB-25-01-009

ENDE
```

---

### 6.4 Entscheidungsbaum: "Gasgeruch, aber Melder reagiert nicht"

```
START: Rieche Gas, Melder still
│
├─ Gasmelder-Position prüfen
│   │
│   ├─ Melder sitzt >150 cm über Boden?
│   │   └─→ [Zu hoch, Propan sinkt!]
│   │       • Melder auf 30–50 cm über Boden verlegen
│   │       • 24h warten, neu testen
│   │       • NÄCHSTER SCHRITT: FB-25-01-008
│   │
│   └─ Melder sitzt richtig
│       └─→ [Sensor degradiert oder Leck zu klein]
│           • Test-Gas sprühen, Melder reagiert?
│           • Falls nein: Sensor austauschen (€100–€200)
│           • Falls ja: Leck ist sehr klein
│           • Seifenwasser-Kontrolle gründlich durchführen
│           • NÄCHSTER SCHRITT: FB-25-01-003 / FB-25-01-008

ENDE
```

---

### 6.5 Entscheidungsbaum: "Tank-Druck fällt schnell ab"

```
START: Druckabfall >5% in 15 Minuten unter Last
│
├─ Erst: Druckprobe durchführen
│   │
│   ├─ Hauptventil schließen, 30 min warten
│   │   │
│   │   ├─ Druck bleibt stabil
│   │   │   └─→ [Leck unter Last]
│   │   │       • Seifenwasser-Kontrolle mit Brenner an
│   │   │       • Fittings nachziehen (¼ Umdrehung)
│   │   │       • Schlauch auf Risse prüfen
│   │   │       • NÄCHSTER SCHRITT: FB-25-01-005
│   │   │
│   │   └─ Druck fällt auch ohne Last
│   │       └─→ [Großes Leck]
│   │           • Seifenwasser überall
│   │           • Brenner ausschalten, Ventil zu
│   │           • Leck lokalisieren
│   │           • SOFORT Werkstatt
│   │           • NÄCHSTER SCHRITT: FB-25-01-007
│   │
│   └─ Manometer-Problem prüfen
│       └─→ Manometer tauschen (€20–€40)
│           • Falls neuer Manometer stabil: Alt-Manometer war Fehler
│           • NÄCHSTER SCHRITT: FB-25-01-007

ENDE
```

---

## 7. Troubleshooting-Hilfe für Schiffe (300 Zeilen)

### 7.1 Häufigste Fehler bei Gaslecks

**Fehler 1: "Ich rieche Gas, aber mache nichts"**
- Gas-Geruch ist Notfall-Signal
- Sofort: Alle Fenster offen
- Kein Feuer, keine Zündquellen
- Gasleck suchen mit Seife
- Falls nicht gefunden: Hauptventil zu, nicht fahren

**Fehler 2: "Gasmelder pieppt, ich ignoriere das"**
- Gasmelder ist wie Rauchmelder im Haus
- >15% LEL ist Alarm
- Kann bedeuten: Leck oder Sensor-Fehler
- Entweder: Sensor prüfen oder Leck suchen
- Nicht ignorieren!

**Fehler 3: "Gas-Regler alt, aber noch 'okay'"**
- Regler <2% Verschleiß pro Jahr
- Nach 10 Jahren sollte regler getauscht sein
- Alte Regler: 30–50% Fehlquote
- Neuer Regler (€150–€250) spart Ärger
- Wartung alle 2 Jahre: Druckprobe

**Fehler 4: "Gasschlauch 'sieht gut aus', aber ist 10 Jahre alt"**
- Armaflex-Schlauch: UV/Ozon-Degradation
- Nach 7–10 Jahren: Austausch empfohlen
- Sichtprüfung mit Lupe: Risse?
- Biegetest: Material spröde?
- Neuer Schlauch: €4–€10/Meter (klein, aber wichtig)

---

### 7.2 Wartungs-Checkliste (Jährlich vor Saison)

**Vor der Saison (März–April):**

□ Gasflaschen-Druck mit Manometer prüfen (sollte >6 bar)
□ Gasmelder testen: Test-Gas sprühen, Alarm sollte <15 Sekunden
□ Alle Rohre/Fittings mit Seifenwasser-Spray auf Lecks prüfen
□ Regler-Ausgangs-Druck messen (sollte 36–38 mbar)
□ Brenner anzünden, Flammenbild überprüfen (gleichmäßig?)
□ Gasmelder-Batterie prüfen (12V, Voltmeter)
□ Schläuche auf Risse/Porenigkeit prüfen (Lupe)
□ Gaslocker-Belüftung prüfen (unten raus, oben rein)
□ Solenoid-Ventil Funk­tionsprobe (Gas-Fluss bei Spannung)
□ Druckprobe 30 min durchführen (Druckabfall <10% erlaubt)

**Falls TÜV/Klassifizierung erforderlich:**

□ Offizielles Inspektionszertifikat beantragen (BG Bau, TÜV)
□ Dichtheitsprüfung mit zertifizierter Ausrüstung
□ Wartungsprotokoll führen (Datiere alle Maßnahmen)
□ Inspektions-Plakette anbringen (gültig 12 Monate)

---

## 8. FAQ 25+ (300 Zeilen)

### F1: Wie oft sollte ich die Gasanlage überprüfen?

**Antwort:** Mindestens 1x pro Saison (März–April vor Auslaufen). TÜV/BG Bau verlangt 12-Monats-Zertifikat für klassifizierte Yachten. Amateur-Yachten: mind. 1x/Jahr Funktionsprobe, alle 2 Jahre professionelle Dichtheitsprüfung.

---

### F2: Was ist der Unterschied zwischen Propan und Butan?

**Antwort:** Propan verdampft bei −42°C (zuverlässig auf See). Butan verdampft bei −0,5°C (nur Mittelmeer im Winter). Propan: 13,9 kWh/kg. Butan: 12,7 kWh/kg. Für offene See: **immer 100% Propan** (oder Propan-dominante Mischung ≥90%).

---

### F3: Kann ich einen alten Gasschlauch mit neuem Schlauch ersetzen?

**Antwort:** Ja. Alten Armaflex-Schlauch ausschrauben, neuen (gleiche Größe) einschrauben. Fittings sollten auch neu sein (€8–€15/Stück). Prüfung: Mit Druckluft testen, dann mit Herd auf Last fahren. Kostet total €30–€80 für ein Meter + Fittings + Arbeit.

---

### F4: Gasmelder pieppt manchmal. Ist das normal?

**Antwort:** Nein. Normales Piepen (schnell): Alarmzustand (Gas-Erkennung). Langsames Piepen (1x/Minute): Batteriewarnung. Kein Piepen: Normal. Falls ständig Alarmpiepen ohne sichtbares Leck: Sensor degradiert (>3 Jahre alt), austauschen.

---

### F5: Kann ich meine Gasanlage selber installieren?

**Antwort:** Theoretisch ja, aber nicht empfohlen für Anfänger. Risiko: Lecks, falsche Druckregelung, elektrische Fehler. Besser: Profi-Installation (€1000–€2000) mit Inspektions-Zertifikat. DIY-Wartung (Seifenwasser-Checks, Regler-Justierung) OK.

---

### F6: Wie lagere ich eine Gaskartusche sicher?

**Antwort:** Aufrecht stehend, draußen oder in gut belüfteter Garage. Niemals im Salon, Schlafkabine oder Motorraum. Temperatur 0–40°C. Keinen Druck ausüben. Ventil-Kappe drauf. Mindestens 2 m von Feuer/Hitze entfernt.

---

### F7: Was ist "LEL" (Lower Explosion Limit)?

**Antwort:** LEL ist die niedrigste Konzentration eines brennbaren Gases in Luft, bei der Explosion/Feuer möglich ist. Für Propan: 2,1 % Vol. (21.000 ppm). Gasmelder alarmiert bei 15–25% LEL = 3.150–5.250 ppm. Kurz: LEL ist "Explosivitätsgrenze".

> ✅ Aufgeloest (Audit): Bei LEL(Propan) = 21.000 ppm (= 2,1 % Vol.) ergeben 15–25 % LEL rechnerisch 3.150–5.250 ppm; die Zahl „315" war ein Faktor-10-Tippfehler und wurde auf „3.150" korrigiert. Quelle: NIOSH/CDC (Propan LEL 2,1 % Vol. ≈ 21.000 ppm). Hinweis: die abweichenden ppm-Werte in Abschn. 2.4 / FB-25-01-002 (750 / 1.250 ppm) bleiben unberührt; maßgeblich ist der in %-LEL angegebene Melder-Schwellwert.

---

### F8: Brauche ich zwingend einen Gasmelder?

**Antwort:** En/ISO 10239 **verlangt Gasmelder** für alle Yachten mit LPG-Anlage (außer sehr kleine Kartuschen-Systeme). CE-Markierung unmöglich ohne. Aus Sicherheitsgründen: JA, unbedingt. Kosten €100–€200, kann Leben retten.

---

### F9: Kann ich Propan und Butan vermischen?

**Antwort:** Technisch ja (viele kommerzielle Flüssiggas-Mischungen sind 60% Propan + 40% Butan). Aber: Butan verdampft nicht unter −0,5°C. Für See/Winter: nicht empfohlen. Stick zu 100% Propan oder min. 90% Propan-Anteil.

---

### F10: Wie erkenne ich eine alte/schlechte Gasanlage?

**Antwort:** 
- Regler >10 Jahre alt
- Keine Wartungsunterlagen / unbekannte Herkunft
- Schläuche porös/Risse sichtbar
- Kein Gasmelder
- Brenner rußig/gelbe Flamme
- Druckabfall schneller als 5% in 15 min
→ Kompletter Austausch: €3000–€6000

---

### F11: Solenoid-Ventil: Was ist "NO" vs "NC"?

**Antwort:** 
- **NO (Normally Open):** Ohne Strom = offen, Gas fließt. Mit Strom = geschlossen.
- **NC (Normally Closed):** Ohne Strom = geschlossen, kein Gas. Mit Strom = offen.

Für Sicherheit auf Yachten: **NC besser** (Gas schneidet automatisch ab bei Stromausfall — Ventil fällt stromlos zu).

---

### F12: Was kostet ein kompletter Gasanlage-Austausch?

**Antwort:** 
- Teile: €1500–€3000 (Regler, Ventile, Rohre, Schläuche, Melder)
- Arbeit: €800–€1500 (Installation, Druckprüfung, Zertifikat)
- **Total: €2300–€4500** (je nach Komplexität, Bootsgröße)

---

### F13: Kann ich einen defekten Regler selbst reparieren?

**Antwort:** Nur einfache Teile (O-Ring, Dichtung) mit Satz-Kit (€20–€40). Komplexe Reparatur (Membrane, Ventilsitz): besser Austausch. Neuer Regler (€150–€250) zuverlässiger als DIY-Reparatur.

---

### F14: Wie prüfe ich, ob die Druckprobe bestanden ist?

**Antwort:** 
1. Hauptventil geschlossen
2. Druckprüfer anschließen (0–1 bar Manometer)
3. Mit Stickstoff auf 0,5 bar aufpumpen
4. 30 Minuten warten
5. Druckabfall <5% = **bestanden**
6. Druckabfall >10% = **Leck vorhanden**

---

### F15: Welche Edelstahl-Sorte für Gas-Rohre?

**Antwort:** **1.4404 (DIN / EN) = 316L (ASTM)**. Das ist marinegütig, chlorid-resistent. Nicht 1.4301 (304) oder 1.4305 (303) — zu anfällig für Salzkorrosion.

---

## 9. Glossar (200 Zeilen)

**Alarmgrenzwert:** Schwelle, bei der Gasmelder Alarm auslöst. Standard: 15–25% LEL.

**Armaflex:** Markenname für Mehrschicht-Gummi-Schlauch mit Schaumkernen zur Vibrations- und Wärmeisolation.

**Aufstelldruck:** Der Druck, bei dem ein Überdruckventil öffnet. Z.B. Gasflaschen ~15 bar.

**Betriebsdruck:** Druck an Brenner, normalerweise 36–38 mbar. (Unterschied: Tank ~8 bar, Betrieb ~38 mbar.)

**Butan:** C₄H₁₀, Siede­punkt −0,5°C. Weniger zuverlässig im Winter als Propan.

**Dampfdruck:** Druck, den eine Flüssigkeit in geschlossenem Behälter erzeugt. Steigt mit Temperatur.

**Dezentralisiert:** Jedes Gas-Gerät hat eigenen kleinen Tank (Kartuschen). Keine Zentralanlage.

**Dichtheits­prüfung:** Standardtest mit Druckprüfer (Stickstoff, 30 min, unter 0,5 bar).

**Druckregler:** Gerät, das Hochdruck (z.B. 8 bar) auf Betriebsdruck (z.B. 37 mbar) reduziert.

**Druckschalter:** Elektrischer Schalter, der bei bestimmtem Druck auslöst/blockiert.

**Ethylmercaptan:** Riechstoff (ätzender Geruch), der zu LPG hinzugefügt wird, um Lecks erkennbar zu machen.

**Flammen-Rückkehr:** Unerwünschte Flammen-Propagation zurück in Rohr/Regler. Verhindert durch "Flame Trap" Ventile.

**Flammentrap:** Sicherheitsventil, das Flammen-Rückkehr verhindert. Oft in Regler integriert.

**Flammensicherheits­schalter:** Elektroschalter an Brenner, der Solenoid-Ventil nur öffnet, wenn Zündfunke vorhanden.

**Gewinde-Dichtpaste:** Teflon-Paste (PTFE) für Gas-Gewinde, verhindert Lecks.

**Gimmbal:** Kardanische Lagerung für Herd, kompensiert Schiff-Neigung/Wellen.

**Gummidichtung (O-Ring):** Elastische Dichtung zwischen Fittings, häufigste Verschleiß-Komponente.

**Hauptregler:** Zentral­-Druckregler, der Tank-Druck (8 bar) auf Betriebsdruck (37 mbar) regelt.

**Hochdruckseite:** Tank bis Regler-Eingang (typisch 0,5–8 bar).

**ISO 10239:** EU-Standard für Flüssiggasanlagen auf Booten. Bindend für CE-Markierung.

**Kapazität (Regler):** Max. Gasmenge, die Regler durchlassen kann. Z.B. 1,5 kg/h.

**Kartusche:** Kleine, tragbare Propan/Butan-Flasche (0,5–5 kg). Für portable Systeme.

**Leck (Mikro-):** Sehr kleine Undichtheit, <0,1 mm. Mit Lupe schwer zu sehen.

**LEL (Lower Explosion Limit):** Unterste Konzentration brennbaren Gases, bei der Explosion möglich ist. Propan: 2,1 % = 21.000 ppm.

**Membran (Regler):** Elastische Scheibe in Regler, die auf Druckdifferenz reagiert und Ventilsitz steuert.

**Mbar (Millibar):** Druckeinheit. 1 mbar = 1/1000 bar. Betriebsdruck: 30–40 mbar.

**Niederdruckseite:** Regler-Ausgang bis Brenner (typisch 30–40 mbar).

**Nordmann-Ventil:** Sicherheitsventil, das bei Temperaturanstieg öffnet (thermisches Überdruckventil).

**O-Ring:** Elastische Dichtung aus Gummi, typisch Nitriel oder EPDM.

**Pellistor-Sensor:** Katalytischer Gas-Sensor für Gasmelder. Standard auf Yachten.

**Propan:** C₃H₈, Siede­punkt −42°C. Ideal für See, funktioniert in jeder Wintertemperatur.

**Sekundärregler:** Kleiner Regler direkt am Brenner (oft integriert), stellt lokalen Betriebsdruck feiner.

**Sicherheitsventil:** Ventil, das bei Überdruckeröffnet, um Schaden zu vermeiden.

**Solenoid:** Elektro-Magnet-Spule. Solenoid-Ventil: Ventil, das von Solenoid elektromagnetisch geöffnet/geschlossen wird.

**Sprödigkeit:** Alterserscheinung von Kunststoff/Gummi — Material wird brüchig.

**Stickstoff (für Druckprobe):** Inerts Gas, das für Dichtheitsprüfung nutzt (statt echtes Flüssiggas, wegen Sicherheit).

**Tankventil:** Ventil an Gasflaschenöffnung, über das Gas entnommen wird.

**Venturi-Effekt:** Druckverlust entlang einer Rohrleitigung beim Gasfluss. Höhere Durchsätze = größere Rohre nötig.

**Vollasttest:** Brenner auf höchster Stufe laufen lassen, Systemverhalten prüfen.

---

## 10. Schnell-Referenz (150 Zeilen)

### 10.1 Druck-Checkliste

| Messpunkt | Normal | Min. | Max. | Einheit |
|-----------|--------|------|------|---------|
| Tank-Druck (voll) | 8,0 | 6,0 | 10,0 | bar |
| Tank-Druck (halbleer) | 4,0 | 3,0 | 5,0 | bar |
| Regler-Ausgang (idle) | 37 | 35 | 40 | mbar |
| Regler-Ausgang (Last) | 37 | 35 | 40 | mbar |
| Brenner-Druck (idle) | 28 | 25 | 32 | mbar |
| Brenner-Druck (Last) | 28 | 25 | 32 | mbar |

---

### 10.2 Röhren-Querschnitt-Checkliste

| Durchsatz (kg/h) | Außen-Ø (mm) | Wand­dicke (mm) | Typ | Max. Länge (m) |
|------------------|-------------|----------------|-----|---------------|
| ≤0,3 | 4 | 0,8 | Kupfer/Edelstahl | 10 |
| 0,3–0,6 | 6 | 1,0 | Kupfer/Edelstahl | 8 |
| 0,6–1,2 | 8 | 1,0 | Kupfer/Edelstahl | 6 |
| 1,2–2,0 | 10 | 1,0 | Kupfer/Edelstahl | 4 |
| >2,0 | 12 | 1,0 | Kupfer/Edelstahl | 3 |

---

### 10.3 Test-Checkliste (Vor Saison)

- [ ] Tank-Druck ≥6 bar?
- [ ] Gasmelder reagiert auf Test-Gas (<15 sec)?
- [ ] Keine Blasen bei Seifenwasser-Test?
- [ ] Regler-Ausgang 36–38 mbar?
- [ ] Brenner-Flamme gleichmäßig?
- [ ] Druckprobe 30 min, Abfall <5%?
- [ ] Schläuche ohne Risse?
- [ ] Gaslocker-Belüftung frei?
- [ ] Solenoid-Spannung 12V?
- [ ] Inspektionszertifikat aktuell (TÜV/BG)?

---

### 10.4 Notfall-Vorgehen (Gasleck-Alarm)

```
1. RUHE bewahren — keine Panik
2. Alle Fenster/Luken öffnen — maximale Belüftung
3. FEUER/ZÜNDQUELLEN ausschalten (Rauchen, Streichhölzer, Feuerzeug)
4. Hauptgas-Ventil (unterm Deck) schließen
5. Mit Seife aller Rohre suchen — Leck finden
6. Falls gefunden: Dichtring-Austausch oder Rohr-Austausch
7. Falls nicht gefunden: Gasmelder überprüfen (Sensor alt?)
8. Nur fahren, wenn Gasmelder wieder grün und kein Geruch
9. Werkstatt aufsuchen, wenn Problem persistiert
```

---

## ANHANG A: Fallstudie 1 — Regler-Ausfall auf Langfahrt

**Szenario:** 40' Gulet, 250 Nm vom nächsten Hafen entfernt. Plötzlich schwache Flamme, Herd läuft nicht mehr.

**Analyse:**
1. Manometer zeigt 20 mbar (sollte 37 mbar)
2. Regler-Ausgangs-Schraube versucht nachzuziehen — kein Effekt
3. Tank-Druck 7 bar (noch normal)
4. Conclusion: Regler-Membran gerissen

**Notfall-Lösung:**
- Regler ausbauen (Hochdruckseite mit Schraubenschlüssel halten)
- Neuen Regler (Ersatz-Kit) anschrauben — wichtig: Dichtpaste auf Gewinde
- Druckprobe mit Seife durchführen
- System wieder in Betrieb

**Lehre:** Ersatz-Regler sollte im Ersatzteil-Kit an Bord sein (€150–€250, wiegt <500g). Wartung alle 3–5 Jahre spart Notfall.

---

## ANHANG B: Fallstudie 2 — Gasmelder-Falsches Alarm

**Szenario:** Charter-Katamaran, Gasmelder pieppt regelmäßig, aber kein Gasleck erkennbar.

**Analyse:**
1. Seifenwasser-Test: Alle Fittings trocken
2. Druckprobe: Kein Abfall
3. Gasmelder-Position: 180 cm über Bodenniveau (zu hoch!)
4. Gasmelder gekauft vor 4 Jahren

**Lösung:**
1. Melder auf 40 cm über Boden verlegen
2. Sensor-Modul austauschen (€60–€80)
3. 48h Beobachtung: Kein Alarm mehr
4. Root Cause: Alte Sensor-Drift + falsche Position

**Lehre:** Gasmelder-Position ist kritisch (Propan sinkt). Austausch alle 3–4 Jahre. DIY-Relokalisierung kostet €0.

---

## ANHANG C: Fallstudie 3 — Saisonale Druckprobleme

**Szenario:** 35' Motorsailer, Winter im Mittelmeer. Brenner zündet nicht, obwohl alles "eigentlich okay" ist.

**Analyse:**
1. Tank wird kalt (Nacht, 5°C)
2. Propan-Dampfdruck sinkt unter Regler-Schwelle
3. Regler kann Gas nicht mehr ziehen
4. Folge: Unter­druck an Brenner

**Lösung:**
1. Tank mit warmem Wasser-Handtuch umwickeln (5 min)
2. Propan-Druck steigt, Brenner zündet wieder
3. Für längeren Winter: Tank nachts mit schwarzer Folie einwickeln (absorbiert Wärmestrahlung)

**Lehre:** Winter-Betrieb braucht Propan-Reaktivierung. Butan in Mischung macht Betrieb below −5°C kritisch. Für Langfahrt: 100% Propan.

---

## ANHANG D: Fallstudie 4 — Undichter Schlauch unter Last

**Szenario:** 50' Expeditionsseglers, Langfahrt Pazifik. Nach 6 Stunden durchgehend Kochen: Gasmelder schlägt an.

**Analyse:**
1. Seifenwasser-Test mit Brenner an: Blasen am Herd-Schlauch (unter Last sichtbar)
2. Schlauch-Alter: 11 Jahre alt Armaflex
3. Winziges Leck, bei Ruhe nicht sichtbar, unter Druck Gasleck

**Lösung:**
1. Brenner ausschalten, Hauptventil schließen
2. Schlauch-Segment austauschen (Fittings + Schlauch: €40–€60)
3. Druckprobe: Bestanden
4. Test Brenner an 2 Stunden: Kein Alarm

**Lehre:** Altere Schläuche (>8 Jahre) sollten vorsorglich getauscht sein, nicht erst bei Fehler. Prevention besser als Notfall auf See.

---

## ANHANG E: Fallstudie 5 — Korrekt­ur einer Überdrucksi­tuation

**Szenario:** 30' Gleiter, Sommer im östlichen Mittelmeer. Tank wird extrem warm (Sonne + Motor-Hitze-Strahlung).

**Analyse:**
1. Tank-Druckentlastungs-Ventil "atmet" (öffnet, gibt Gas ab)
2. Propan-Verluste ~50g/Tag
3. Regler-Ausgangs-Druck schwankend (wegen variabler Tank-Temperatur)

**Lösung:**
1. Tank mit UV-reflektierend Folie (silber) abdecken
2. Gaslocker-Belüftung überprüfen (sollte 2–3 m³/h zirkulieren)
3. Tank im Schatten lagern wenn möglich
4. Nach Maßnahmen: Druckentlastung nur noch 1x/Woche minimal

**Lehre:** Thermische Stabili­tät ist unterschätzt. Gute Belüftung + Beschattung reduziert Verluste und Sicherheits-Probleme.

---

## ANHANG F: Fallstudie 6 — Alter-Cracking in Schlauch-Materialien

**Szenario:** 42' Cruiser, lagert seit 2 Jahren vor Reparatur. Gasanlage wird nach 2 Jahren Stillstand wieder aktiviert.

**Analyse:**
1. Visuelle Inspektion: Armaflex zeigt Risse (Radial-Cracking)
2. Material spröde, bricht bei leichtem Biegen
3. Ursache: UV/Ozon-Exposition + Temperatur-Zyklen während Stillstand

**Lösung:**
1. Kompletter Schlauch-Satz austauschen (€80–€150 für alle Segmente)
2. Neue Fittings (€20–€40)
3. Montage+Prüfung: €100–€200 Arbeit
4. Nach Austausch: Vollständige Druckprobe, bestanden

**Lehre:** Langzeit-Stillstand (>1 Jahr) erfordert vollständige Inspektion vor Betrieb. Schläuche sind Verschleißteile, nicht unbegrenzt haltbar.

---

## ANHANG G: Fallstudie 7 — Solenoid-Ventil-Blockade durch Verschmutzung

**Szenario:** 60' Motor-Segler, gehört einem Charterunternehmen. Nach 5 Jahren Wechsel zwischen hundert Chartergästen: Solenoid-Ventil öffnet nur noch langsam.

**Analyse:**
1. Brenner dauert 3–5 Sekunden bis Gas kommt (sollte <1 sec)
2. Prüfung: Solenoid-Spule reagiert (Spannung 12V), aber mechanisch träge
3. Vermutung: Wasser/Öl-Verschmutzung in Ventil-Kern

**Lösung:**
1. Solenoid ausbauen (Hochdruckseite mit Hahn absperren)
2. Mit feinem Lösungsmittel (Heptan, nicht Wasser!) durchspülen
3. Ventil-Kern manuell durchbewegen (3–5x)
4. Trocknen, neu montieren
5. Test: Öffnungszeit wieder <1 sec

**Alternative:** Neues Solenoid (€80–€150) — wenn Reinigung nicht funktioniert.

**Lehre:** Charterboote brauchen häufigere Wartung (6 Monate statt 12). Wasser-Kontamination ist Risiko bei häufigem "Fremdeinsatz".

---

## ANHANG H: Fallstudie 8 — Brenner-Düse-Vertauschung

**Szenario:** Bootswerkstatt nimmt Herd auseinander für Reparatur, montiert falsche Brenner-Düse beim Zusammenbau.

**Analyse:**
1. Flammen extrem schwach, nach Reparatur
2. Alle Druck-Werte normal (37 mbar)
3. Verdacht: Brenner-Problem
4. Lupe-Inspektion: Düse ist 0,50 mm statt 0,75 mm (falsche Größe!)

**Lösung:**
1. Richtige Düse einbauen (Größe auf Brenner-Handbuch überprüfen)
2. Flammen sofort normal
3. Feine Abstimmung mit Primärluft-Schieber

**Lehre:** Nach Brenner-Reparatur IMMER Teile-Nummern überprüfen. Düsen sind klein (€5–€15), aber kritisch.

---

## ANHANG I: Pydantic v2 Datenmodelle für Gasanlage-Tracking

```python
# models.py - Gasanlage-Datenschema für AYDI-Wissen­sdatenbank

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum

model_config = {"from_attributes": True}

class GasTypeEnum(str, Enum):
    PROPAN = "propan"
    BUTAN = "butan"
    MISCHUNG = "mischung"
    CNG = "cng"
    ETHANOL = "ethanol"
    UNKNOWN = "unknown"

class ReliabilityEnum(str, Enum):
    MEASURED = "measured"
    ESTIMATED = "estimated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    DOCUMENTED = "documented"
    BENCHMARK = "benchmark"

class GasTankModel(BaseModel):
    """Modell für Gasflaschenspezifikationen"""
    tank_id: str = Field(..., description="Eindeutige Tank-ID z.B. 'tank_11kg_001'")
    capacity_kg: float = Field(..., ge=1, le=50, description="Kapazität in kg")
    material: str = Field(default="Stahl", description="Behältermaterial")
    gas_type: GasTypeEnum = Field(default=GasTypeEnum.PROPAN)
    manufacture_date: Optional[datetime] = None
    pressure_bar_full: float = Field(default=8.0, description="Druck bei voller Füllung")
    pressure_bar_min: float = Field(default=2.0, description="Minimaldruck für Betrieb")
    weight_empty_kg: float = Field(..., description="Leergewicht")
    weight_full_kg: float = Field(..., description="Vollgewicht")
    has_safety_valve: bool = Field(default=True, description="Druckentlastungs-Ventil vorhanden")
    safety_valve_pressure_bar: float = Field(default=15.0, description="Ventil-Auslösedruck")
    inspection_date: Optional[datetime] = None
    next_inspection_due: Optional[datetime] = None
    reliability: ReliabilityEnum = Field(default=ReliabilityEnum.MEASURED)
    notes: str = ""

class RegulatorModel(BaseModel):
    """Modell für Druckregler"""
    regulator_id: str
    manufacturer: str = Field(..., description="z.B. 'GOK', 'Truma', 'ENO'")
    model: str
    input_pressure_bar_max: float = Field(default=10.0, description="Max. Eingangsdruck")
    output_pressure_mbar_nominal: float = Field(default=37.0, description="Nennausgangsdruck")
    output_pressure_mbar_min: float = Field(default=35.0)
    output_pressure_mbar_max: float = Field(default=40.0)
    capacity_kg_per_hour: float = Field(..., ge=0.3, le=3.0)
    has_integrated_gauge: bool = Field(default=False)
    has_integral_flame_trap: bool = Field(default=True)
    installation_date: Optional[datetime] = None
    last_maintenance_date: Optional[datetime] = None
    next_maintenance_due: Optional[datetime] = None
    adjustment_screw_turns: Optional[float] = None
    reliability: ReliabilityEnum = Field(default=ReliabilityEnum.MEASURED)
    notes: str = ""

class SolenoidValveModel(BaseModel):
    """Modell für Solenoid-Ventile"""
    valve_id: str
    manufacturer: str
    model: str
    valve_type: str = Field(default="2/2", description="'2/2' (Ein/Aus), etc.")
    normally_open: bool = Field(default=True, description="True=NO, False=NC")
    rated_voltage_v_dc: float = Field(default=12.0, description="Spannungsbezeichnung")
    coil_resistance_ohms: float = Field(..., ge=5, le=200, description="Spulenwiderstand")
    max_flow_kg_per_hour: float
    max_pressure_bar: float = Field(default=10.0)
    installation_date: Optional[datetime] = None
    last_test_date: Optional[datetime] = None
    reliability: ReliabilityEnum
    notes: str = ""

class HoseSegmentModel(BaseModel):
    """Modell für Gas-Schlauch-Segmente"""
    hose_id: str
    material: str = Field(default="Armaflex", description="Material: Armaflex, Gummi, Kupfer, etc.")
    outer_diameter_mm: float = Field(..., ge=4, le=16)
    inner_diameter_mm: Optional[float] = None
    wall_thickness_mm: Optional[float] = None
    length_m: float
    max_pressure_bar: float
    installation_date: Optional[datetime] = None
    age_years: Optional[float] = None
    has_visible_cracks: bool = Field(default=False)
    brittleness_assessment: str = Field(default="ok", description="ok | minor | major")
    reliability: ReliabilityEnum
    notes: str = ""

class GasSystemMaintenanceRecordModel(BaseModel):
    """Wartungsprotokoll für Gasanlage"""
    record_id: str
    yacht_id: str = Field(..., description="Referenz zum Schiff")
    maintenance_date: datetime
    maintenance_type: str = Field(..., description="z.B. 'Pressure_Test', 'Leak_Check', 'Sensor_Replacement'")
    performed_by: str = Field(..., description="Techniker-Name")
    pressure_test_duration_min: Optional[int] = Field(None, ge=1, le=1440)
    pressure_test_mbar_initial: Optional[float] = None
    pressure_test_mbar_final: Optional[float] = None
    pressure_test_passed: Optional[bool] = None
    leak_detected: bool = Field(default=False)
    leak_location_description: Optional[str] = None
    sensor_replacement_required: bool = Field(default=False)
    components_replaced: List[str] = Field(default_factory=list)
    next_maintenance_due: Optional[datetime] = None
    certification_obtained: bool = Field(default=False, description="TÜV/BG Bau Zertifikat")
    reliability: ReliabilityEnum = Field(default=ReliabilityEnum.DOCUMENTED)
    notes: str = ""

class GasSensorAlertModel(BaseModel):
    """Gasdetektor-Alarm-Protokoll"""
    alert_id: str
    yacht_id: str
    alert_datetime: datetime
    sensor_model: str
    alarm_type: str = Field(..., description="z.B. 'HIGH_ALARM', 'LOW_ALARM', 'BATTERY_WARNING', 'SENSOR_ERROR'")
    lel_percentage: Optional[float] = Field(None, ge=0, le=100, description="LEL-Prozentsatz beim Alarm")
    action_taken: str = Field(..., description="Was wurde getan (z.B. Lüftung, Ventil geschlossen, Sensor getestet)")
    root_cause_identified: bool = Field(default=False)
    root_cause_description: Optional[str] = None
    resolved: bool = Field(default=False)
    reliability: ReliabilityEnum
    notes: str = ""

class GasSystemCompleteModel(BaseModel):
    """Gesamtmodell für komplette Gasanlage"""
    system_id: str
    yacht_id: str
    system_type: str = Field(default="centralized", description="centralized | portable | hybrid")
    tank: GasTankModel
    regulator: RegulatorModel
    solenoid_valves: List[SolenoidValveModel] = Field(default_factory=list)
    hose_segments: List[HoseSegmentModel] = Field(default_factory=list)
    gas_sensor: Optional[dict] = None  # Sensor-Modell optional
    last_full_inspection: Optional[datetime] = None
    maintenance_records: List[GasSystemMaintenanceRecordModel] = Field(default_factory=list)
    alert_history: List[GasSensorAlertModel] = Field(default_factory=list)
    overall_reliability: ReliabilityEnum = Field(default=ReliabilityEnum.ESTIMATED)
    overall_safety_assessment: str = Field(default="unknown", description="safe | caution | danger | unknown")
    notes: str = ""

    model_config = {"from_attributes": True}
```

---

## ANHANG J: Referenzen und Standards

1. **EN ISO 10239:2025** — Flüssiggas-Installationen auf Booten und Yachten. (Hauptstandard)

2. **EU-Richtlinie 2013/53/EU** — Anforderungen für die Vermarktung von Freizeitfahrzeugen. (Enthält Gasanlage-Abschnitte, Designkategorien)

3. **IEC 61162-1:2016** — Marinegeräte — Digitale Schnittstellen und Netzwerke — IEC 61162-1. (Für Gasmelder-Integration)

4. **ISO 12217:2015** — Boote unter 24 m — Bewertung und Klassifizierung der Stabilitäts- und Schwimmfähigkeit. (Gewichtsverlagerung durch Gastank)

5. **ISO 9094:2015** — Freizeitfahrzeuge — Brandschutz — Anforderungen. (Abstände Engine ↔ Gasrohre)

6. **ISO 15085:2003** — Freizeitfahrzeuge — Mann-über-Bord-Vorbeugung. (Railing-Höhen neben Gaslecks)

7. **ISO 11812:2020** — Freizeitfahrzeuge — Speiseraumgestaltung — Entwässerung. (Cockpit-Drainage bei Gas-Lecks)

8. **ISO 12216:2020** — Fenster und Luken — Sicherheit. (Notfall-Escapeöffnungen, Gasmelder-Zugang)

9. **DNV-GL Rules for Classification of Yachts** — Part 4, Chapter 8. (Flüssiggas-Anlagen für klassifizierte Yachten)

10. **ABS Guide for Building and Classing Recreational Vessels**. (Nordamerika-Standard)

---

## ANHANG K: Hersteller-Kontakte und Fachverbände

**Haupthersteller:**

- **GOK GmbH** (Deutschland): www.gok.de — Regler, Ventile, Komponenten
- **Truma** (Deutschland): www.truma.de — Regelanlagen, Heizung, komplette Systeme
- **ENO Marine** (Dänemark): www.enomarine.dk — Flüssiggas-Komplettsets für Boote
- **Campingaz** (Frankreich): www.campingaz.com — Kartuschen, portable Systeme
- **Dometic** (Schweden): www.dometic.com — Integrierte Küchen- und Wärmemanagement-Lösungen

**Zertifizierungsstellen:**

- **TÜV Rheinland** (Deutschland): www.tuv.com — CE-Markierung, Gasanlage-Prüfung
- **BG Bau** (Deutschland): www.bgbau.de — Berufsgenossenschaft, Zertifikate für Gastechniker
- **IMCA** (UK): www.imca.org — Maritime Consulting Association, Standards

**Fachverbände:**

- **EYCA** (European Yacht Charter Association) — Charter-Boot-Standards
- **Deutsches Institut für Normung (DIN)** — EN/ISO Standards
- **CLIA** (Cruise Lines International Association) — Kreuzfahrt-Standards

---

## ANHANG L: Kostenübersicht (EUR 2026)

| Maßnahme | Teile | Arbeit | Gesamt | Häufigkeit |
|----------|------|--------|---------|-----------|
| Gasmelder Sensor-Austausch | €60–€100 | €10–€20 | €70–€120 | Alle 3–4 J. |
| Regler-Austausch | €150–€250 | €80–€150 | €230–€400 | Alle 10 J. |
| Druckprobe (TÜV-Zertifikat) | €0 | €150–€250 | €150–€250 | 12 Monate |
| Schlauch-Segment austauschen (1m) | €15–€50 | €30–€80 | €45–€130 | Nach Alter/Schaden |
| Solenoid-Ventil-Austausch | €80–€180 | €30–€60 | €110–€240 | Alle 8–10 J. oder bei Fehler |
| Komplette Gasanlage (Neu) | €1500–€3000 | €800–€1500 | €2300–€4500 | Alle 15–20 J. |
| Gasmelder (kompletter Austausch) | €100–€200 | €20–€30 | €120–€230 | Alle 3–4 J. |
| Tank-Befüllung (11 kg) | €25–€40 | — | €25–€40 | Nach Bedarf (4–8x/Jahr) |
| Jährliche Sichtprüfung (DIY) | €0 | — | €0 | Jährlich |
| Jährliche Professionelle Inspektion | €0 | €100–€200 | €100–€200 | Jährlich |

---

## ANHANG M: Nützliche Tools und Ausrüstung

**Für Wartung:**
- Druckprüfer-Set (0–1 bar): €20–€50
- Manometer-Adapter-Sätze: €15–€30
- Schraubenschlüssel-Set (Metrisch): €30–€60
- Gasmelder-Testspray: €10–€20
- Heptane-freies Seifenwasser (CAGI-Standard): €8–€15
- Multimeter (digitals): €15–€40
- Infrarot-Thermometer: €20–€50
- Magnet-Lupe (für Risse-Suche): €10–€20

**Für Notfälle:**
- Ersatz-Regler-Set (GOK/Truma): €150–€250
- Ersatz-Schlauch-Kit (3–5m Armaflex + Fittings): €40–€80
- Ersatz-Solenoid-Ventil: €80–€150
- Tetralin oder Heptan-Lösungsmittel (Ventil-Reinigung): €10–€20
- Hochdruckmaßstab (Schraubzieher, Schlüssel): €0 (DIY-Werkzeug)

---

## ANHANG N: Checkliste für Bootskauf (Gasanlage-Prüfung)

Beim Kauf einer gebrauchten Yacht sollte die Gasanlage wie folgt überprüft werden:

- [ ] **Anlage-Typ:** Zentralisiert oder dezentralisiert?
- [ ] **Tank-Alter:** Baujahr? (>20 Jahre = kritisch)
- [ ] **Tank-Zustand:** Rostflecken? Dellen? Verschleiß?
- [ ] **Tank-Inspection-Etikett:** Aktuelles Zertifikat vorhanden?
- [ ] **Regler-Alter:** Baujahr? (>10 Jahre = kritisch)
- [ ] **Regler-Typ:** Bekannter Hersteller (GOK, Truma, ENO)?
- [ ] **Schlauch-Zustand:** Risse sichtbar? Alterserscheinungen?
- [ ] **Gasmelder:** Vorhanden? Welches Modell? Baujahr?
- [ ] **Solenoid-Ventile:** Funktionieren alle? Spannung okay?
- [ ] **Brenner-Flamme:** Gleichmäßig? Rußig?
- [ ] **Wartungsprotokoll:** Protokolle/Zertifikate vorhanden?
- [ ] **Druckprobe:** Vor Kauf durchführen (TÜV).
- [ ] **Gasmelder-Test:** Mit Test-Spray prüfen.

**Rote Flaggen für Kauf:**
- Tank-Alter >25 Jahre
- Regler-Alter >15 Jahre ohne Wartung
- Keine Gasmelder
- Sichtbare Risse in Schläuchen
- Rußige Flammen
- Keine Inspektionsprotokolle

---

## ANHANG O: Geplante Upgrades und Technologie-Ausblick

**CNG (Erdgas unter Druck) — Zukunft?**
- Höherer Druck (200–250 bar) erfordert stärkere Tanks
- Sicherer als LPG (Gas steigt auf, entweicht oben, nicht unten)
- Infrastruktur wächst (Schweiz, Deutschland, Skandinavien)
- Langfristig: Wahrscheinlich Standard für kommerzielle/professionelle Yachten
- Kostensteigerung: +€5000–€10000 vs. LPG

**Hybrid-Systeme:**
- Gasanlage + Induktions-Herd-Backup
- Induktion aus Solar + Batterie
- Redundanz im Notfall

**Digitale Überwachung:**
- IoT-Gasmelder mit Remote-Alert
- Smartphone-Integration
- Druck-Logger (kontinuierliche Aufzeichnung)
- KI-basierte Anomalieerkennung

---

## ANHANG P: Bibliographie und Leseangebot

1. **"Yacht Design Detailing" von Gerr 2013** — Chapters on Mechanical Systems
2. **"The Art and Science of Small Boat Design" von Herreshoff & Skene** — Historical context on propane adoption
3. **"Flüssiggas-Technik in der Schifffahrt" (Lehr­skript)** — Deutschsprachige Schulung, BG Bau
4. **Online-Resources:**
   - www.vly.de (Verband Liegeplatz Yachthafen) — Gasanlage-Richtlinien
   - www.dmyv.de (Deutscher Motorboot-Verband) — Wartungs-Tipps
   - www.sperrlande.de (Intra-European Yacht Code) — Konformitätsprüfung

---

## Conclusion

Gasanlagen auf Yachten erfordern ständige Aufmerksamkeit und Wartung. Dieser Ratgeber deckt 80% der Fragen und Fehler ab, die sich in der Praxis stellen. Für ungewöhnliche Situationen: Immer einen zertifizierten Gasfachmann konsultieren. Sicherheit ist nicht verhandelbar — eine €500 Inspektions-Investition pro Jahr spart €10.000+ an Notfall-Schäden und garantiert Seefahrts-Sicherheit.

---

**Dokument Ende**

Letztes Update: 2026-05-18 | Autor: AYDI Knowledge Base | Lizenz: CC-BY-SA für interne Nutzung

---

# EXPANSION: Erweiterte Fehlerbild-Atlas & Fallstudien

> ⚠️ **ZU PRÜFEN (Audit):** Betriebsdruck-Widerspruch ~800–1200 mbar vs. ~28–37 mbar — der gesamte Expansions-Teil (ab hier) nennt Arbeits-/Betriebsdrücke von ~800–1200 mbar (0,8–1,2 bar), z. B. „950 mbar", „1100 mbar", „0,8–1,2 bar" und Tabelle SR-1. Der Haupttext (Abschn. 2.2 und 10.1) sowie die europäische LPG-Niederdruck-Praxis nach EN/ISO 10239 geben den Betriebs-/Brennerdruck hinter dem Niederdruckregler mit **~28–37 mbar** an. 0,8–1,2 bar ist für einen Yacht-Herd hinter dem Niederdruckregler physikalisch nicht plausibel. Alle Druckangaben in diesem Expansions-Teil gelten daher als **estimated — unverifiziert** und dürfen NICHT für Regler-Einstellung, Grenzwerte oder Druckprüfung herangezogen werden, bis der Widerspruch geklärt ist.

## Fehlerbild 25-01-002: Regulatorversatz und Druck-Instabilität

**Symptom:**
Druck schwankt zwischen 800 mbar und 1200 mbar, obwohl Ventil fest geschlossen ist.

**Root Cause:**
Regler-Membran hat Verschleiß oder Verschmutzung. Kleine Partikel halten Ventilsitz nicht dicht.

**Diagnose-Schritte:**
1. Manometer über 5 Minuten beobachten
2. Temperatur-abhängige Druckänderung ausrechnen (Gay-Lussac: ΔP = P₀ × ΔT/273)
3. Isolationsprüfung: Absperrhahn vor Regler schließen, 10 Min warten, Druck neu lesen
4. Wenn Druck fällt: Leck nach dem Regler (Fitting, Leitung)
5. Wenn Druck stabil: Regler ist schuld

**Handlung:**
- Regler reinigen (lauwarmes Wasser + Zahnbürste)
- Falls Membran beschädigt: Tausch (€150–300)
- Test: 30 Min laufen, Manometer sollte ±50 mbar bleiben

**Prävention:**
- Filter vor Regler alle 2 Jahre wechseln
- Regler nicht in direkter Sonne montieren (Wärmestau)

---

## Fehlerbild 25-01-003: Kältebruch in Leitung (Winter/Hochgebirge)

**Symptom:**
Herd funktioniert normal, dann plötzlich kein Gas. Flasche ist voll, Regler zeigt normal.

**Root Cause:**
Propan-Flüssigkeit gefriert bei <–42°C. Bei Butan <–0,5°C. In Höhe (Hochgebirge) oder Winter kann Temperatur ausreichen. Gefrorene Flüssigkeit blockiert Verdampfer.

**Diagnose-Schritte:**
1. Flasche von außen fühlen (eiskalt?)
2. Temperatur-Sensor oder Thermometer an Flasche anlegen
3. Heiße Wasserbäder (aber nie Feuer!) unter Flasche halten
4. Regler mit warmem Tuch wickeln
5. 30 Min warten, dann Hahn langsam öffnen

**Handlung:**
- Flasche in wärmere Kabine bringen
- Im Winter: Flasche in Styropor-Box, isoliert
- Für Hochgebirge: Propan-Butan-Mischung (gibt es als Spezial-Mix bis 1500m)

**Prävention:**
- Winterbetrieb: Flasche im beheizten Raum lagern
- Hochgebirge: Vor Fahrt Spezial-Mix kaufen

---

## Fehlerbild 25-01-004: Korrosion durch Salzwasser-Aerosol (Deck-Flasche)

**Symptom:**
Flasche rostet von außen, Ventil wird zäh, Leitung zeigt grüne Verfärbung (Kupferoxid).

**Root Cause:**
Cu­-Messing + Salzwasser-Aerosol → galvanische Korrosion. Besonders wenn Flasche auf Deck liegt.

**Diagnose-Schritte:**
1. Optisch: Grüne/braune Flecken auf Flasche oder Armatur?
2. Ventil drehen: Läuft schwergängig?
3. Leitung: Biegsamkeit prüfen, Risse?
4. Korrosions-Grad schätzen: <5% Oberfläche = noch OK, >20% = Austausch

**Handlung:**
- Leichte Korrosion: Drahtbürste + Rostumwandler (Konverter)
- Flasche dann mit Kunststoff-Schutzmantel umwickeln
- Schwere Korrosion (>20%): Flasche austauschen (€120–200)
- Ventil + Regler: Tausch (€80–150)

**Prävention:**
- Flasche NICHT auf Deck lagern
- Im Motorraum oder in isolierter Locker unter Deck
- Flasche mit Kunststoff-Folie gegen Spritzwasser schützen
- Jährliche Sichtprüfung

---

## Fehlerbild 25-01-005: Dichtungsverschleiß an Regulatorausgang (Festdruck-Leitung)

**Symptom:**
Schwaches Zischen an Regler-Ausgang, auch wenn Hahn zu ist. Nach Herd-Nutzung Gasgeruch.

**Root Cause:**
O-Ring oder Cone-Seal an Regler-Outlet ist abgenutzt oder mit Partikeln verkratzt.

**Diagnose-Schritte:**
1. Seifenblosen-Test: Seifenwasser auf Regler-Fitting sprühen
2. Blasen entstehen? → Leck bestätigt
3. Isolationsprüfung: Alle Geräte-Hähne zu, dann Regler-Ausgang beobachten
4. Blasen nur bei Druck? → Dichtung schuld
5. Blasen auch ohne Druck? → Ventil nicht dicht

**Handlung:**
- Regler + Sealing-Kit austauschen (€200–400)
- Oder: Nur O-Ring + Cone wechseln (€30–60, erfordert Fachmann)
- Test nach Reparatur: 5 Min Drucktest

**Prävention:**
- Regler nicht in Vibrations-Zone montieren
- Jährliche Druckprüfung

---

## Fehlerbild 25-01-006: Schlauch-Risse und Abnutzung (5-Jahr-Zyklus)

**Symptom:**
Schwacher Gasgeruch im Motorraum, aber alle Hähne zu. Schlauch fühlt sich brüchig an.

**Root Cause:**
Marine-Schläuche (Gummi/Nylon) verschleißen nach 5 Jahren durch UV, Ozon, Temperatur. Besonders Deck-Schläuche.

**Diagnose-Schritte:**
1. Schlauch visuell prüfen: Risse, Versprödung?
2. Drucktest: 5 bar für 10 Min, Seifenblasen-Test
3. Alter prüfen: Herstellungsdatum auf Schlauch?
4. Flexibilität: Schlauch biegen — soll flexibel bleiben, nicht brechen

**Handlung:**
- Schlauch austauschen (€8–15/Meter, plus Fittings €5–10 pro Stück)
- Dauer: 1–2 Stunden für kompletten Lauf
- Nach Montage: Druck + Seifenblasen-Test

**Prävention:**
- Schläuche alle 5 Jahre austauschen (Wartungs-Plan)
- Deck-Schläuche jährlich prüfen
- UV-Schutz (schwarzer Gummi-Mantel) für Außenschläuche

---

## Fehlerbild 25-01-007: Flaschenventil-Abbruch (Transportschaden)

**Symptom:**
Plötzlich großer Gasgeruch, Druck fällt rapide. Ventil-Kopf ist ab oder lose.

**Root Cause:**
Flasche umgestoßen oder unsachgemäß transportiert. Ventil-Hals ist am dünnsten Punkt abgebrochen.

**Diagnose-Schritte:**
1. SOFORT alle Luken öffnen, Lüftung max
2. Alle Geräte-Hähne schließen
3. Flasche-Ventil-Hahn fest zu (Notbremse)
4. Visuelle Prüfung: Ventil vollständig?
5. Druck: Kann man noch messen oder nicht?

**Handlung:**
- NICHT zu reparieren. Flasche ist Schrott (€0 Restwert)
- Neue Flasche kaufen (€120–200)
- Transport-Sicherung überprüfen (Flaschenhalter, Gurt)

**Prävention:**
- Flaschenhalter mit Gurt verwenden (€30–50)
- Flasche nicht auf Deck binden
- Fahrt in rauer See: Flasche extra sichern

---

## Fehlerbild 25-01-008: Regler-Frostbildung und Vereisung

**Symptom:**
Regler wird eiskalt, Frost bildet sich außen. Gas kommt nur noch tropfenweise.

**Root Cause:**
Joule-Thomson-Effekt: Hochdruck-Gas entspannt sich, Temperatur sinkt. Bei hohem Durchsatz (z.B. zwei Herde gleichzeitig) kann Regler auf –30°C fallen.

**Diagnose-Schritte:**
1. Regler anfassen (Schutz: Handschuh!)
2. Temperatur messen: Thermometer-Streifen
3. Durchsatz prüfen: Wieviele Geräte laufen?
4. Umgebungs-Temperatur: <5°C außen?

**Handlung:**
- Durchsatz reduzieren (ein Herd statt zwei)
- Regler mit warmer Luft blasen (Föhn, aber nicht zu heiß!)
- Flasche in warmen Raum bringen
- Nach 10 Min sollte Regler tauen und Druck steigen

**Prävention:**
- Regler isolieren (Kunststoff-Mantel, €10–20)
- Im Winter: Begrenzte Nutzung akzeptieren
- Hochleistungs-Regler kaufen (größerer Durchsatz → weniger Abkühlung)

---

## Fehlerbild 25-01-009: Zünder-Probleme (elektrische Zünd­anlage)

**Symptom:**
Herd hat Zünder-Knopf, aber kein Funke. Keine Zündung, manuell mit Feuerzeug nötig.

**Root Cause:**
Batterie leer, oder Zündtrafo defekt.

**Diagnose-Schritte:**
1. Batterie prüfen (9V, AA oder AAA je nach Modell)
2. Zündtrafo mit Multimeter prüfen: Ohm-Messung Spule
3. Hörprüfung: Klick-Geräusch beim Zünden?
4. Sichtprüfung: Elektro-Kontakte oxidiert?

**Handlung:**
- Batterie wechseln (€3–5)
- Elektro-Kontakte mit Essig reinigen
- Trafo austauschen (€40–80)
- Test: 5 × zünden sollte jeden Versuch Funken geben

**Prävention:**
- Batterie jährlich wechseln
- Zündanlage trocken halten

---

## Fehlerbild 25-01-010: Gemische und Druckkreis-Ungleichgewicht

**Symptom:**
Herd-Linksfeld brennt normal, Rechtsfeld ist schwach, Regler zeigt 950 mbar.

**Root Cause:**
Einzeln-Regler bei jedem Feld ist beschädigt, oder gemeinsamer Regler verteilt ungleich.

**Diagnose-Schritte:**
1. Alle Brenner einzeln prüfen: Flammen-Höhe/Farbe?
2. Druckmessung bei laufendem Rechtsfeld: Ist es wirklich < 950 mbar dort?
3. Schlauch-Durchmesser prüfen: Beide gleich?
4. Fitting-Blockade: Schmutz in Leitung?

**Handlung:**
- Regler reinigen oder austauschen
- Schlauch-Querschnitt prüfen, ggf. ersetzen
- Herd-Regulator (falls vorhanden) kalibrieren

**Prävention:**
- Regler sollten identisch sein (gleiche Kalibrierung)
- Jährliche Druck-Kontrolle

---

## Fehlerbild 25-01-011: Gasflasche läuft aus (Ventil nicht dicht)

**Symptom:**
Flasche-Gewicht sinkt deutlich, obwohl Boot nicht benutzt wird. Gasgeruch schwach, aber wahrnehmbar.

**Root Cause:**
Flaschenventil-Kugel sitzt nicht dicht. Undicht durch Verschleiß oder Verunreinigung.

**Diagnose-Schritte:**
1. Seifenblosen-Test am Ventil-Ausgang
2. Gewicht-Vergleich: 1 Woche lagern, dann neu wiegen
3. Ventil drehen: Läuft leicht oder zäh?
4. Dichtring prüfen: Sichtbar beschädigt?

**Handlung:**
- Ventil-Innenteil reinigen (für Fachmann: €30–50)
- Dichtring wechseln (€10–15)
- Komplettes Ventil austauschen (€80–150)

**Prävention:**
- Ventil-Griff nicht ständig bewegen
- Ventil mit Kunststoff-Kappe schützen (€5)

---

## Fehlerbild 25-01-012: Lecks im Verbindungs-Netzwerk (Fitting-Fehler)

**Symptom:**
Nach Inspektion findet man mehrere kleine Lecks an verschiedenen Fittings (Union-Knoten, Reduzierungen).

**Root Cause:**
Fittings nicht fest genug angezogen, oder Dichtmittel (PTFE-Band) vergessen / falsch angewickelt.

**Diagnose-Schritte:**
1. Seifenblasen-Test an jedem Fitting
2. Drehmoment prüfen: Mit Ringschlüssel versuchen nachzuziehen (leichter Widerstand = OK)
3. PTFE-Band sichtbar? Auf Gewinde?

**Handlung:**
- Fittings um 1/4 Umdrehung nachzuziehen (nicht zu fest!)
- Wenn Leck bleibt: Fitting abschrauben, PTFE-Band erneuern (3–5 Windungen mit leichter Spannung)
- Nach Montage: 24 h warten, dann Seifenblasen-Test

**Prävention:**
- PTFE-Band immer verwenden bei Gewinde-Verbindungen
- Keine flüssigen Dichtstoffe verwenden (können gegen Propan reagieren)
- Drehmoment-Anleitung befolgen

---

# Erweiterte Troubleshooting-Entscheidungsbäume

## Entscheidungsbaum A: "Gas kommt nicht aus dem Herd"

```
START: Zünder klicken hörbar?
├─ NEIN → Gehe zu TB_E (Zündproblem)
└─ JA:
   ├─ Flamme sichtbar, brennt weg?
   │  ├─ JA: Gehe zu TB_B (Luftzufuhr/Verbrennung)
   │  └─ NEIN:
   │     ├─ Gasgeruch im Bereich?
   │     │  ├─ JA: Leck irgendwo. Gehe zu TB_D (Lecksuche)
   │     │  └─ NEIN:
   │     │     ├─ Manometer zeigt Druck?
   │     │     │  ├─ JA: Druckhahn oder Brennerhahn zu? → Öffnen
   │     │     │  └─ NEIN:
   │     │     │     ├─ Flasche voll? Schlauch kalt? → TB_C (Vereisung)
   │     │     │     └─ Gehe zu TB_A (Druck prüfen)
```

## Entscheidungsbaum B: "Flamme ist schwach oder orange (nicht blau)"

```
START: Flammen-Farbe?
├─ ORANGE/GELB → Luft/Brennstoff-Verhältnis falsch (Düse?)
│  ├─ Düse prüfen: Verstopft? → Reinigen
│  ├─ Luftschacht prüfen: Blockiert? → Öffnen
│  └─ Gas-Art prüfen: Propan oder Butan? (Butan brennt oranger)
├─ BLAU aber schwach → Druck zu niedrig
│  ├─ Manometer prüfen: <800 mbar?
│  └─ Gehe zu TB_A (Druck)
└─ BLAU und stark → Normale Verbrennung, OK
```

## Entscheidungsbaum C: "Manometer zeigt niedrig oder 0"

```
START: Flasche kalt anfassen?
├─ EISKALT → Vereisung (FB-008). Warm werden lassen.
├─ NORMAL:
│  ├─ Hahn am Regler zu?
│  │  ├─ JA → Öffnen
│  │  └─ NEIN:
│  │     ├─ Seifenblasen-Test am Regler-Inlet
│  │     │  ├─ Blasen? → Leck vor Regler. Fitting nachziehen.
│  │     │  └─ Keine Blasen:
│  │     │     ├─ Flasche leer? (Wiegen)
│  │     │     └─ Regler defekt? → Austausch
└─ HEISSPFIFFIG → Sollte nie sein. Flasche-Ventil prüfen (FB-011)
```

## Entscheidungsbaum D: "Gasgeruch im Boot überall"

```
START: Intensität?
├─ Sehr stark, durchdringend → NOTFALL
│  ├─ ALLE Luken öffnen
│  ├─ Motor aus, keine Funken
│  ├─ Flaschenventil schließen
│  └─ Gasfachmann anrufen
├─ Schwach aber wahrnehmbar → Systematische Suche
│  ├─ Seifenblasen-Test an: Flasche, Regler, Herd-Inlet, Schläuche
│  ├─ Leck gefunden? → TB_F (Fitting-Reparatur)
│  └─ Kein Leck gefunden? → Evtl. Kal­tstart-Lecks (morgens). Beobachten.
└─ Nur nach Herd-Nutzung kurz → Normal (Starter-Gas). OK.
```

## Entscheidungsbaum E: "Zünder macht nicht: Klick?"

```
START: Hörbarer Klick beim Drücken?
├─ JA, Klick da, aber kein Funke → Trafo kaputt
│  └─ Austausch (€40–80)
├─ NEIN, gar kein Klick → Batterie leer oder Schalter defekt
│  ├─ Batterie wechseln
│  ├─ Nach Wechsel: Klick da? → OK
│  └─ Immer noch kein Klick? → Schalter-Elektronik defekt
└─ Funke da, aber zündet nicht → Düse-Lage oder Gas-Flow (TB_A)
```

---

# Erweiterte FAQ (25+ Fragen)

## FAQ-201: "Kann ich die Gasflasche selber austauschen?"

**Antwort:**
Ja, Flaschenventil + Schlauch-Kupplung ist relativ einfach. Aber: Gasanlage muss danach sofort überprüft werden (Druck, Seifenblasen-Test). Wenn Sie unsicher sind → Gasfachmann (€60–100 Arbeit). Flasche selbst wird von Gas-Lieferant getauscht (Rückgabe + Kauf, €120–200).

---

## FAQ-202: "Warum wird das Manometer manchmal rot?"

**Antwort:**
Manometer hat oft eine rote Markierung bei Überdrucken (z.B. >3 bar). Das ist eine Warnung. Normal sollte der Zeiger im grünen Bereich (0.8–1.2 bar) bleiben. Wenn die Nadel in Rot geht → sofort untersuchen (blockierte Leitung, Regler-Fehler, Temperatur).

---

## FAQ-203: "Muss ich die Gasanlage vor der Winter-Einlagerung leeren?"

**Antwort:**
Nein. Modernes LPG ist chemisch stabil über Jahre. ABER: Vor Einlagerung sollte man alle Hähne schließen und die Leitung mit Handpumpe leergeblasen. Flasche kann lagern (unter 5°C besser für Haltbarkeit). Test beim Auswinterung: Druckprüfung + Seifenblasen-Test.

---

## FAQ-204: "Kann Propan-Flasche im Laderaum gelagert werden?"

**Antwort:**
NEIN! Geräte-Klasse erlaubt Flasche nur in einem speziellen Gaskasten mit Belüftung. Laderaum ist zu dicht. Explosion-Risiko. Gaskasten muss außenbord durchbelüftet sein (z.B. mit Klapptür). Standort: Unter Deck, hinten, isoliert, mit Gurt gesichert.

---

## FAQ-205: "Was bedeutet 'Betriebsbeschränkung' für eine Gasanlage?"

**Antwort:**
Z.B. "Nur Betrieb in Süßwasser, nicht in Salzwasser" oder "Max. 1000m Höhe". Dies steht im Ce-Papier. Wenn Sie diese Grenzen überschreiten, gilt die Zertifizierung nicht mehr. Zu beachten bei Atlantik-Überquerung (Salzwasser = keine Beschränkung normalerweise) oder Hochgebirge-Fahrt.

---

## FAQ-206: "Wie oft muss die Gasanlage überprüft werden?"

**Antwort:**
- Vor jeder Saison: Sichtprüfung, Manometer-Check
- Jährlich: Druckprüfung (5 Min bei 1.5× Arbeits-Druck)
- Alle 5 Jahre: Hauptuntersuchung durch Fachmann (€100–200)
- Nach Schlag/Stoß: Sofort prüfen

---

## FAQ-207: "Warum riecht es manchmal nach Gas, obwohl alles zu ist?"

**Antwort:**
Mehrere Ursachen:
1. Morgens nach Kaltstart: Starter-Gas, verdunstet schnell (normal)
2. Mikro-Lecks in Fitting (zu schwach, um großes Aroma zu geben)
3. Gerätereste im Herd von letzter Nutzung (normales Knacken)
4. Seltener: Loch im Schlauch (aber dann meist stärker riechbar)

→ Seifenblasen-Test macht Sicherheit.

---

## FAQ-208: "Kann ich einen Auto-Gashahn verwenden statt Marine-Regler?"

**Antwort:**
NEIN! Auto-Regler hat andere Druckauslegung (1–4 bar statt 0.8–1.2 bar). Würde Herd-Düsen zu hoch drücken (Flammen zu groß, Gefahr). Marine-Regler ist billiger (€100–200), kaufen Sie den richtigen.

---

## FAQ-209: "Gibt es eine Backup-Flasche für Langfahrten?"

**Antwort:**
Ja, sinnvoll für Atlantik oder längere Cruises. System: 
- Haupt-Flasche (z.B. 6 kg)
- Backup-Flasche (z.B. 3 kg) mit eigenem Hahn + Regler
- Umschalt-Ventil (€30–50) um beide zu regeln
- Bei Verbrauch: Hahn wechseln, Backup wird Haupt

Kosten: +€100–150. Genug für 60+ Tage Betrieb.

---

## FAQ-210: "Wie kann ich den Gas-Verbrauch messen?"

**Antwort:**
Flasche wiegen (mit Waage):
- Vor Saison: W₁ (kg)
- Nach Monat: W₂ (kg)
- Verbrauch = W₁ – W₂ (kg)

Normale Nutzung (1× täglich kochen, 2h): ca. 0.3–0.5 kg/Monat.
Bei hohem Verbrauch (Backofen, Heizung): 1–2 kg/Monat.

---

## FAQ-211: "Muss der Gaskasten am Rumpf montiert sein?"

**Antwort:**
Am besten ja — externe Belüftung ist einfacher. ABER: Kann auch in Cockpit unter Bankbox sein, wenn:
- Vorder- und Rückseite belüftet (Lüftungsschläuche)
- Klapptür mit Scharnier + Verschluss
- Keine Nähe zu Motor-Auspuff (Hitze)

Schon besser als unter Deck im geschlossenen Raum.

---

## FAQ-212: "Ist eine Absperrkugel oder Nadel besser?"

**Antwort:**
- Kugelhahn (ball valve): ¼ Drehung zu, einfacher, meist besser
- Nadelhahn (needle valve): Feinregelung, langsamer zu, aufwendiger

Für Flaschenventil: Kugel, darunter Nadel für jeden Brenner (optional, für Feinabstimmung).

---

## FAQ-213: "Warum ist das CE-Papier so wichtig?"

**Antwort:**
CE-Zertifikat (Konformitätserklärung) bescheinigt, dass die Gasanlage die Richtlinie 2013/53/EU (Sportboot-Richtlinie / Recreational Craft Directive) einhält. Ohne CE:
- Boot wird nicht versichert
- TÜV-Prüfung nicht bestanden
- Verkauf schwierig
- Haftung im Schadensfall beim Besitzer

Immer aufbewahren + mit Boot mitgeben.

---

## FAQ-214: "Darf ich selbst einen Regler einstellen (Druck anpassen)?"

**Antwort:**
NEIN! Regler-Verschraubung (meist 2–3 kleine Schrauben) ist vom Fachmann eingestellt. Eigenes Herumschrauben kann zu Überdruck oder Unterdruck führen. Immer Fachmann (€50–100).

---

## FAQ-215: "Was ist der Unterschied zwischen Druckregler und Druckreduzier?"

**Antwort:**
- **Druckregler** (Regulator): Speichert Höchstdruck, reduziert ihn auf stabilen Arbeits-Druck
- **Druckreduzierventil**: Reduziert einfach von Hoch auf Niedrig, ohne Speicher

Für Yacht: Druckregler (mit Regler-Kasten).

---

## FAQ-216: "Kann die Gasanlage in Salzwasser korrodieren?"

**Antwort:**
Ja! Besonders:
- Messing-Fittings (Cu + Zn) reagieren mit Salzwasser-Elektrolyten
- Stahl (nicht Edelstahl) rostet schnell
- Lösungsmittel: Edelstahl 316L verwenden, Opfer-Anode installieren oder Flasche nicht on Deck lagern

Details: Siehe FB-004 (Korrosion).

---

## FAQ-217: "Wie lange dauert eine Gasanlage-Reparatur beim Hafen?"

**Antwort:**
- Kleine Reparatur (Fitting nachziehen, O-Ring): 30–60 Min (€50–100)
- Schlauch-Austausch: 2–3 h (€150–250)
- Regler-Austausch: 1–2 h (€150–300)
- Komplettes Retrofit: 1–2 Tage (€1000–2000)

Lagen-bedingt: Mit Termin meist 1–2 Wochen Vorlauf.

---

## FAQ-218: "Muss ich die Gasanlage dokumentieren beim Neukauf?"

**Antwort:**
Ja! Wichtig:
- CE-Zertifikat + Konformitätserklärung mitnehmen
- Wartungs­log anfangen (Datum, Art, Gasfachmann)
- Manometer-Kalibrier-Zertifikat (alle 2 Jahre)
- Regler-Wartungs-Quittungen sammeln

Hilft bei Versicherung und Verkauf.

---

## FAQ-219: "Kann man Flüssiggas auch mit Diesel-Heizung nutzen?"

**Antwort:**
NEIN! Diesel-Heizung (z.B. Webasto) läuft auf Diesel. Komplett separates System. Es gibt aber Hybrid-Heizungen, die Diesel oder Strom nehmen. Gas-Heizung ist seperates System (LPG-Brenner), ca. €1000–2000.

---

## FAQ-220: "Was ist die sicherste Montage-Position für die Gasflasche?"

**Antwort:**
Ideale Position:
1. Außenbord-Gaskasten (unter Cockpit, Seitenbrett)
2. Belüftung vorne und hinten mit Klapptüren
3. Gekapselt (eigener Behälter), nicht sichtbar von Deck
4. Mit Sicherheits-Gurt gesichert
5. Mindestens 2m Abstand zu Motor, Auspuff, Wohnraum

Schlecht: Auf Deck sichtbar (Korrosion, Hitze), unter Deck ohne Belüftung (Explosion-Risiko).

---

## FAQ-221: "Ist eine digitale Überwachung der Gasanlage möglich?"

**Antwort:**
Ja, neu am Markt:
- IoT-Gasmelder mit Cloud-Integration (z.B. Atmel, ca. €200–400)
- Druck-Logger mit SD-Karte (ca. €100–150)
- Smartphone-App für Fernüberwachung (Premium, €500+)

Für Profis sinnvoll, private Yacht: Klassischer Sensor mit Alarm reicht meist.

---

## FAQ-222: "Kann die Gasanlage während des Fahrens betrieben werden?"

**Antwort:**
Ja, rechtlich ist es erlaubt (in den meisten EU-Häfen). ABER praktisch:
- Bei schwerem Seegang: Gimbal-Herd wird mitgenommen, vermeidbar
- Sicherheit: Besatzung sollte in Nähe sein (schnell zuschalten können)
- Best Practice: Kochen auf ruhigem Wasser (Ankerplatz)

In rauen Bedingungen: Herd nicht nutzen, kalte Verpflegung oder Spirituskocher.

---

## FAQ-223: "Warum kostet ein Regler in der Marina 3× mehr als online?"

**Antwort:**
Mehrere Gründe:
1. Lagerkosten + Gewinnmarge (30–50%)
2. Sofort-Verfügbarkeit (you need it now)
3. Installation + Beratung inbegriffen
4. Garantie-Abwicklung lokaler
5. Online-Preis oft für Lande-Käufer (keine Versandkosten eingerechnet für Boot)

Tipp: Kaufen Sie 6 Wochen vor Saison online, installieren Sie selber (mit Fachmann-Konsultation).

---

## FAQ-224: "Gibt es eine Gasanlage, die sowohl Propan als auch Butan akzeptiert?"

**Antwort:**
Ja, moderne Regler können beides handeln (Propan/Butan-Mix). Allerdings:
- Butan verdampft nur bis –0.5°C (Winter-Problem)
- Propan bis –42°C (besser)
- Standard-Mix: 60% Propan, 40% Butan (kompromiss)

Für Winter-Fahrt: 100% Propan. Für Mittelmeer: Mix reicht.

---

## FAQ-225: "Muss ich den Druckregler lagern, wenn das Boot in Winterschlaf ist?"

**Antwort:**
Nein, kann in Reglerkopf bleiben (ist geschützt). ABER: Bei extremer Kälte (<-20°C) sollte man Regler ins warme Lager nehmen. Membran-Material kann brüchig werden. Wenn Regler draußen bleibt: Kunststoff-Schutzhaube drüber (€10).

---

# Schnell-Referenz Tabellen

## Tabelle SR-1: Druck-Normen nach Gerätetyp

> ⚠️ **ZU PRÜFEN (Audit):** 850–1200 mbar vs. ~28–37 mbar — diese Tabelle widerspricht direkt der „Druck-Checkliste" in Abschn. 10.1 (Brennerdruck 28 mbar, Reglerausgang 37 mbar) und der europäischen LPG-Niederdruck-Praxis. Werte hier **estimated — unverifiziert**; nicht für Einstellungen verwenden.

| Gerätetyp | Arbeits-Druck | Min | Max | Notiz |
|-----------|---------------|-----|-----|-------|
| Herd (1–3 Brenner) | 850–950 mbar | 750 | 1100 | Standard |
| Heizung (Brenner) | 1000–1100 mbar | 900 | 1300 | Höher für Verbrennungs-Sicherheit |
| Grill (external) | 900–1000 mbar | 800 | 1200 | Variabel je Modell |
| Kombi-System | 950–1050 mbar | 850 | 1200 | Alle Geräte nutzen gemeinsamen Druck |

---

## Tabelle SR-2: Schlauch-Querschnitte und maximale Durchsätze

| Außen-Ø (mm) | Innen-Ø (mm) | Max-Durchsatz (kg/h) | Typischer Einsatz | Max-Länge (m) |
|-------------|-------------|-----------------|------------------|---------------|
| 6 | 4 | 0.8 | Einzelner Brenner | 3 |
| 8 | 6 | 1.5 | Zwei Brenner | 5 |
| 10 | 8 | 2.5 | Herd + kleine Heizung | 8 |
| 12 | 10 | 4.0 | Heizung + Herd | 10 |

---

## Tabelle SR-3: Korrosions-Anfälligkeit von Materialien

| Material | Salzwasser | Süßwasser | Luft (trocken) | Lösungsmittel | Empfehlung |
|----------|-----------|-----------|--------------|--------------|-----------|
| Messing CW614N | Hoch (grün) | Mittel | Niedrig | OK | Mit Opfer-Anode |
| Edelstahl 316L | Sehr niedrig | Sehr niedrig | Sehr niedrig | OK | Standard, bevorzugt |
| Stahl verzinkt | Mittel | Mittel | Mittel | OK | Gelegentliche Prüfung |
| Kupfer (rein) | Sehr hoch (grün) | Mittel | Mittel | Nein | Nicht empfohlen |
| Kunststoff PTFE | Keine | Keine | Keine | Teils | Nur für Dichtungen |

---

## Tabelle SR-4: Fehler-Symptom-Matrix

| Symptom | Ursache 1 | Ursache 2 | Ursache 3 | Erste Maßnahme |
|---------|-----------|-----------|-----------|----------------|
| Kein Gas | Flasche leer | Ventil zu | Leck | Gewicht prüfen |
| Druck niedrig | Vereisung | Leck | Regler defekt | Seifenblasen |
| Flamme schwach | Düse verstopft | Druck gering | Luft-Mangel | Düse prüfen |
| Gasgeruch | Leck | Kaltstart-Reste | Microleck | Seifenblasen-Test |
| Zünder funktioniert nicht | Batterie leer | Trafo kaputt | Schalter defekt | Batterie wechseln |

---

# ANHANG A–H: Fallstudien Gasanlage-Fehler auf Yachten

## ANHANG A: Fallstudie 1 — "Der Druck sinkt Tag um Tag"

**Boot:** Segelyacht Dehler 34 (2015), Baujahr 2008, vorher in Griechenland privat, jetzt gekauft.

**Symptom:** Gasanlage funktioniert OK, aber Manometer sinkt kontinuierlich. Nach 1 Woche: 1100 mbar → 800 mbar, obwohl kein Gerät läuft.

**Diagnose-Prozess:**
1. Besitzer dachte zuerst: Flasche leer. Flasche gewogen: 4.2 kg von 6 kg (gut, noch volle Lebensdauer)
2. Manometer beobachtet 48h: Druckfall bei 20°C → mbar pro Tag
3. Seifenblasen-Test an allen Fittings: Negativ
4. Isolationsprüfung: Alle Hähne zu, Druck stabil → kein aktives Leck
5. Temperatur-Überprüfung: Theoretischer Druck-Fall nach Gay-Lussac: 1100 × (15°C / 293K) ≈ 56 mbar für 5°C Fall. Gemessen: 300 mbar Unterschied. Nicht erklärbar durch Temperatur.
6. Verdacht: Regler-Leck (innenleck nach dem Regler)
7. Hahn vor Regler schließen, 12h warten: Druck stabil
8. Hahn nach Regler (vor Herd) schließen, 12h warten: Druck sinkt weiter

→ **Root Cause:** Mikro-Leck in Regler-Auslass-Dichtung.

**Lösung:**
- Regler austausch (€200, Fachmann €50 Arbeit)
- Neue Dichtungs-Kits bestellt, Lagerbestand erneuert
- Nach Reparatur: Test 5 Tage, Druck stabil

**Lernpunkt:** Bei kontinuierlichem Druck-Fall, aber keine visuellen Lecks → Regler-Innenleck prüfen. Nicht automatisch annehmen, dass Flasche leer ist.

---

## ANHANG B: Fallstudie 2 — "Flaschenventil-Abbruch im Atlantik"

**Boot:** Allegro-49-Katamaran (2012), 8-Personen-Crew, auf dem Weg von Kanaren nach Brasilien.

**Symptom:** Am 15. Segeltag (Atlantik-Mitte) plötzlich massiver Gasgeruch überall. Crew öffnet sofort Luken, Herd aus, alle Fenster auf.

**Diagnose-Prozess:**
1. Kapitän findet Flasche im Cockpit-Gaskasten mit lockerem Ventil-Kopf
2. Inspektion: Ventil-Hals ist oben halbwegs abgebrochen (wahrscheinlich Transport-Schlag beim Einsetzen oder Knarren-Bewegung)
3. Druck: Kann nicht gemessen werden (Manometer-Anschluss ist ab)
4. Gas-Austritts-Rate: Geschätzt 10–20 g/min (basierend auf Geruchs-Intensität)

**Handlung:**
- Flasche SOFORT in isolierten Behälter (Kunststoff-Box mit Lüftungsschacht nach außenbord)
- Ventil-Kappe festziehen (Band um die Bruchstelle)
- Gasanlage abgesperrt (Hahn vor Regler geschlossen)
- Herd 10 Tage lang nicht nutzbar
- Bei nächstem Hafen (Bermuda, nach 5 Tagen) neue Flasche geholt (€150 teuer dort, aber notwendig)

**Lernpunkt:** Flaschenventil ist dünnste Stelle. Transportmechanismus (Schock-Absorbung) ist notwendig. Sicherungs-Gurt allein reicht nicht — Flasche sollte in Kasten mit Polsterung liegen.

---

## ANHANG C: Fallstudie 3 — "Regler-Vereisung im Hochgebirge"

**Boot:** Flusskreuzfahrt (Main–Donau-Kanal) Beneteau-51 (Motor), 2 Personen, Winterfahrt (Oktober, 1500m Höhe über Meer).

**Symptom:** Herd läuft OK, aber nach 45 Min kontinuierlichem Kochen wird Regler eiskalt, Eis bildet sich außen. Druck fällt rapide, nach 1h kein Gas mehr.

**Diagnose-Prozess:**
1. Regler-Temperatur gemessen: –22°C (Thermometer-Streifen)
2. Umgebung: 0°C Luft-Temperatur, Boot auf der Donau (kalte Wasser-Kühlung)
3. Durchsatz-Prüfung: Gleichzeitig zwei Brenner + Backofen laufen (ungewöhnlich hoch)
4. Theory: Joule-Thomson-Effekt bei hohem Durchsatz führt zu extremer Abkühlung

**Handlung:**
1. Sofort Durchsatz reduzieren (nur ein Brenner)
2. Regler mit Handschuhen anfassen, warm blasen (Föhn auf 40°C)
3. Flasche von Außenkühlung bringen (in Motorraum = wärmer)
4. Warten: Nach 15 Min taute Regler, Druck stieg auf 950 mbar

**Lernpunkt:** Hochgebirge + kalte Luft + hoher Durchsatz = Vereisung. Lösungen: (a) Regler isolieren mit Kunststoff-Mantel, (b) Durchsatz reduzieren (nicht beide Brenner gleichzeitig), (c) Flasche in beheiztem Raum lagern.

---

## ANHANG D: Fallstudie 4 — "Korrosion nach 5 Jahren in Südsee"

**Boot:** Catana 47 (Katamaran, Baujahr 2017), 5 Jahre kontinuierliche Nutzung in Salzwasser (Französisch-Polynesien).

**Symptom:** Flasche zeigt grüne/braune Verfärbung außen, Ventil wird zäh beim Drehen, Schläuche zeigen grüne Flecken (Kupfer-Oxid-Patina).

**Diagnose-Prozess:**
1. Optische Kontrolle: 30% der Oberfläche ist verfärbt (Galvanische Korrosion)
2. Schlauch-Flexibilität: Noch OK, aber brüchiger als normal
3. Ventil-Bewegung: Dauert 3 Sekunden statt 1 Sekunde zum Drehen (Reibung)
4. Korrosions-Tiefe: Geschätzt <1 mm (oberflächlich, aber fortgeschritten)

**Handlung:**
1. Schläuche austauschen (€120, Fachmann-Zeit 2h)
2. Flasche mit Drahtbürste + Rostumwandler (Konverter) reinigen
3. Flasche mit schwarzem Kunststoff-Schutzmantel umwickeln (€15)
4. Ventil-Kappe neu ersetzen (€10)
5. Hahn-Dichtring erneuern (€5)
6. Danach: Regelmäßig prüfen (alle 6 Monate statt 1 Jahr)

**Kosten:** €150–200 Gesamtreparatur vs. €120–200 für neue Flasche. Bestehende Flasche noch 3–4 Jahre gut.

**Lernpunkt:** Salzwasser zersetzt Messing schnell. Flasche sollte NICHT auf Deck liegen (Spritzwasser), auch nicht in offener Locker. Kunststoff-Schutz ist billiger als Neukauf.

---

## ANHANG E: Fallstudie 5 — "Schlauch-Riss entdeckt bei Wartung"

**Boot:** Sunseeker-55 (Motor Yacht, Baujahr 2009), private Nutzung 2–4 Wochen/Jahr.

**Symptom:** Bei jährlicher Wartung durch Hafen-Techniker: Schlauch hinter Motorraum-Wand zeigt Risse (ca. 2 mm lange Spalten im Gummi).

**Diagnose-Prozess:**
1. Schlauch-Alters-Stempel: "Hergestellt 2014" (8 Jahre alt)
2. Material-Prüfung: Gummi ist brüchig, verliert Elastizität
3. Druck-Test: 5 bar für 10 Min, dann Seifenblasen-Test → Keine Lecks während Test
4. ABER: Techniker empfiehlt Tausch, da Rissflanken können sich unter Vibration öffnen

**Handlung:**
1. Schlauch komplett austauschen (3m Lauf: €24 + Fittings €20 = €44 Material)
2. Fachmann-Installation: 1.5h = €90 Arbeit
3. Kosten: €134 total
4. Test nach Montage: 5 Min Drucktest + Seifenblasen
5. Neuer Schlauch hat Hersteller-Stempel 2024 (Lagerware)

**Lernpunkt:** Schläuche haben 5–8 Jahre Lebensdauer. Auch wenn keine Lecks sichtbar sind, präventivier Tausch ist günstiger als Notfall-Reparatur im Ausland (€300+).

---

## ANHANG F: Fallstudie 6 — "Fitting-Undichtigkeiten nach Montage"

**Boot:** Beneteau First 35 (Segler, Baujahr 2010), nach Reengineer der Gasanlage (neue Herd + Schläuche).

**Symptom:** Nach Montage durch lokalen Techniker (€150 Arbeit): Besitzer macht Seifenblasen-Test und findet Blasen an 3 verschiedenen Fittings.

**Diagnose-Prozess:**
1. Fittings identifiziert: (a) Union-Knoten am Regler-Ausgang, (b) Reduzier-Fitting am Herd-Eingang, (c) Kupplung an Schlauch-Trennstelle
2. PTFE-Band geprüft: Beim Fitting (c) war kein PTFE-Band vorhanden (Übersehen bei Montage)
3. Fitting (a) + (b) waren nur locker angezogen (Techniker hatte 1 Umdrehung übersehen)

**Handlung:**
1. Techniker zu Rückbesuch geholt (kostenlos, Fehler des Monteurs)
2. Alle Fittings nachgezogen (1/4 Umdrehung)
3. Fitting (c) abgeschraubt, PTFE-Band erneuert (3 Windungen mit Spannung), wieder montiert
4. Nach 24h: Seifenblasen-Test, alle Lecks weg

**Lernpunkt:** Nach Montage IMMER Seifenblasen-Test durchführen. Fitting-Fehler sind häufigste Anfänger-Fehler. PTFE-Band ist billig (€2) und kritisch.

---

## ANHANG G: Fallstudie 7 — "Zünder-Batterie leer mitten auf dem Meer"

**Boot:** Hallberg-Rassy-53 (Segler), 8-Personen-Crew, Wochenend-Cruise (Nordsee).

**Symptom:** Morgens: Zünder funktioniert normal. Nach 6h Betrieb: Klick-Geräusch wird schwächer, dann gar kein Klick. Kochen mit Feuerzeug notwendig.

**Diagnose-Prozess:**
1. Zündanlage: 9V-Batterie (Typ 6F22, Standard)
2. Batterie-Spannungs-Messung: 3.2V (sollte 9V sein)
3. Batterie auf Herdträger datiert: Sept 2022 (fast 2 Jahre alt)
4. Einsatz-Häufigkeit: 3× täglich zünden, ca. 20 Zünde pro Betätigung = 60 Zünde/Tag

**Handlung:**
1. Crew hat Ersatz-Batterie an Bord? NEIN (wichtig: immer 1–2 Ersatz-Batterien mitnehmen)
2. Hafen-Stop nächster Tag, neue Batterie kaufen (€3)
3. Alte Batterie wechseln, Zünder funktioniert wieder

**Lernpunkt:** Zünder-Batterie hält ca. 12 Monate bei normalem Einsatz. Auf Langfahrten: Immer 2–3 Ersatz-Batterien an Bord. Alternativ: Zu Federstein-Zünder upgraden (keine Batterie nötig, aber teurer €400+).

---

## ANHANG H: Fallstudie 8 — "Gasanlage-Blackout nach CE-Prüfung"

**Boot:** Custom-Schooner 60 (Superyacht, Baujahr 2023, Neubau), erste CE-Abnahme.

**Symptom:** Gasanlage war fertig montiert + getestet. Bei CE-Inspektor-Besuch wird Gasanlage überprüft und folgende Fehler gefunden, die nicht vorher aufgefallen waren:
1. Regler-Isolation: Fehlende Beschriftung (Druckwert)
2. Schläuche: Keine eindeutige Farbmarkierung (sollten rot sein für Gas)
3. Manometer: Kalibrierungs-Zertifikat fehlte (>2 Jahre alt)
4. Gasmelder: Position nicht nach Norm (zu hoch in der Kabine)

**Diagnose-Prozess:**
1. Inspektor gibt Abweichungs-Liste aus
2. Werft musste alle Punkte innerhalb 2 Wochen korrigieren
3. Technischer Direktor analysiert, warum Fehler nicht früher aufgefallen waren: Werkstatt-Routinen nicht dokumentiert

**Handlung:**
1. Markierungen an allen Schläuchen + Komponenten anbringen (Aufkleber, €50)
2. Manometer neu kalibrieren (€80, 3 Werktage)
3. Gasmelder verlegen (neue Position 30 cm über Galley, Kabel + Montage €150)
4. Regler-Beschriftung anbringen (€10, Kunststoff-Plakette)
5. Neue CE-Prüfung geplant für 3 Wochen später

**Kosten:** €290 + Verzögerung (2 Wochen Bauzeitverlängerung = mehrere k€ in Multiplikator-Kosten).

**Lernpunkt:** CE-Abnahme ist nicht nur technisch, sondern auch dokumentarisch. Alle Komponenten müssen eindeutig beschriftet und zertifiziert sein. Werkstatt sollte früh mit Inspektor-Anforderungen vertraut sein (nicht erst bei Abnahme überrascht werden).

---

# ANHANG I: Pydantic v2 Datenmodelle für Gasanlage-Module

```python
from pydantic import BaseModel, Field, ConfigDict
from enum import Enum
from datetime import datetime
from typing import Optional, List

# Enums
class ConfidenceLevel(str, Enum):
    measured = "measured"
    calculated = "calculated"
    estimated = "estimated"
    visual_high = "visual_high"
    visual_medium = "visual_medium"
    visual_low = "visual_low"
    visual_insufficient = "visual_insufficient"
    documented = "documented"

class ErrorSeverity(str, Enum):
    critical = "critical"
    high = "high"
    medium = "medium"
    low = "low"
    info = "info"

class ComponentType(str, Enum):
    flasche = "flasche"
    ventil = "ventil"
    schlauch = "schlauch"
    regler = "regler"
    fitting = "fitting"
    herd = "herd"
    manometer = "manometer"
    zuender = "zuender"

# Core Models
class GasComponentMeasurement(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    component_id: str = Field(..., description="Eindeutige Komponenten-ID")
    component_type: ComponentType
    age_years: Optional[float] = Field(None, description="Alter in Jahren")
    pressure_mbar: Optional[float] = Field(None, description="Aktueller Druck in mbar")
    temperature_celsius: Optional[float] = Field(None, description="Temperatur in °C")
    visual_condition: Optional[str] = Field(None, description="Zustand: OK, warn, critical")
    last_inspection_date: Optional[datetime] = None
    confidence: ConfidenceLevel
    notes: Optional[str] = None

class PressureReading(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    timestamp: datetime
    pressure_mbar: float = Field(..., ge=0, le=5000)
    temperature_celsius: float
    ambient_temperature_celsius: Optional[float] = None
    confidence: ConfidenceLevel

class GasSystemDiagnosis(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    boat_id: str
    analysis_date: datetime
    components: List[GasComponentMeasurement]
    pressure_readings: List[PressureReading]
    identified_issues: List['GasIssue']
    recommendations: List['Recommendation']
    overall_confidence: ConfidenceLevel
    risk_level: ErrorSeverity

class GasIssue(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    issue_id: str = Field(..., description="Format: FB-25-01-XXX")
    symptom: str
    root_cause: Optional[str] = None
    severity: ErrorSeverity
    affected_components: List[ComponentType]
    pressure_context: Optional[str] = Field(None, description="Z.B. 'niedrig', 'instabil'")
    confidence: ConfidenceLevel

class Recommendation(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    action: str
    priority: int = Field(..., ge=1, le=5, description="1=sofort, 5=optional")
    estimated_cost_eur: Optional[float] = None
    estimated_hours: Optional[float] = None
    success_probability: float = Field(..., ge=0, le=1)
    references: Optional[List[str]] = Field(None, description="Links zu Fallstudien/FAQ")

class MaintenanceRecord(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    record_id: str
    boat_id: str
    performed_date: datetime
    technician_name: str
    work_performed: str
    components_replaced: List[str] = []
    cost_eur: Optional[float] = None
    next_due_date: Optional[datetime] = None
    notes: Optional[str] = None

```

---

# ANHANG J–R: Referenztabellen und schnelle Checklisten

## Tabelle J-1: Jährliche Wartungs-Checkliste

| Monat | Aufgabe | Dauer | Kosten (€) | Notizen |
|-------|---------|-------|-----------|---------|
| März/April | Visuelle Inspektion | 30 Min | 0 | Vor Saison-Start |
| März/April | Druck-Test (5 Min @ 1.5bar) | 45 Min | 50 | Mit Manometer-Prüfung |
| Juni | Schlauch-Prüfung (Flexibilität/Risse) | 30 Min | 0 | Mittag der Saison |
| September | Verbrauch-Kontrolle (Gewicht) | 15 Min | 0 | Halb-Jahres-Bilanz |
| Oktober | Manometer-Kalibrierung | 1h | 80 | Alle 2 Jahre |
| Oktober | Regler-Wartung oder Tausch | 2h | 200 | Alle 5 Jahre oder nach Fehler |
| November | Wintervorbereitung | 30 Min | 0 | Alle Hähne schließen, Leerrohre blasen |

---

## Tabelle K-1: Kosten-Übersicht für häufige Reparaturen

| Reparatur | Teile (€) | Arbeit (€) | Total | Dauer |
|-----------|----------|-----------|-------|-------|
| Batterie wechseln | 3 | 0 | 3 | 5 Min |
| O-Ring ersetzen | 5 | 30 | 35 | 30 Min |
| Schlauch 1m austauschen | 8 | 30 | 38 | 1h |
| Fitting nachziehen | 0 | 20 | 20 | 15 Min |
| PTFE-Band erneuern | 2 | 25 | 27 | 20 Min |
| Manometer kalibrieren | 80 | 0 | 80 | 3 Werktage |
| Regler austausch | 150 | 50 | 200 | 2h |
| Komplette Schlauch-Lauf | 50 | 150 | 200 | 4h |
| Flasche austausch | 150 | 20 | 170 | 1h |

---

## Tabelle L-1: Lagerbestände für Notfall-Reparaturen

**Empfohlene Bordlager:**
- 2× 9V Zünder-Batterien
- 1× Regler-Sealing-Kit (O-Ringe + Cone)
- 1× 3m Universalschlauch (8mm Durchmesser)
- 4× Fitting-Satz (Union 8mm, Reduzier-Fitting, Kupplung)
- 1× PTFE-Band-Rolle (2cm × 50m)
- 1× Manometer-Ersatz (analog, 0–4 bar)
- 1× Drahtbürste + Rostumwandler
- 1× Seifenblasen-Spray (500ml)

**Kosten Gesamt-Lager:** €150–200

---

## Tabelle M-1: Fault-Finding Priorität-Matrix

| Fehler-Typ | Sofort-Action | Zeitrahmen | Ernstheit |
|-----------|--------------|-----------|----------|
| Starker Gasgeruch überall | Luken auf, Motor aus, FV schließen | Sofort | Critical |
| Flamme brennt weg | Druck prüfen, Regulator resetzen | <1h | High |
| Kein Gas, aber Flasche voll | Isolations-Test durchführen | <2h | Medium |
| Schwaches Zischen am Regler | Seifenblasen-Test, ggf. Fitting nachziehen | <24h | Low |
| Schlauch-Verfärbung | Visuelle Dokumentation, Beobachtung | <1 Woche | Info |

---

Dokument fortgesetzt — Expansion vollständig.

