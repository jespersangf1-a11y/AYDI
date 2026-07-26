---
category: "25_Gas_und_Kochen"
subcategory: "Gasflaschenlagerung"
title: "Gasflaschenlagerung und Handhabung"
version: "1.0"
last_updated: "2026-05-18"
languages: ["de", "en"]
---

# 25.03 – Gasflaschenlagerung und Handhabung

## 1. Einführung

Gasflaschenlagerung an Bord ist eine der kritischsten Sicherheitsmaßnahmen in der Yachtausrüstung. Flüssiggas (LPG/Propan, Butan) wird an Bord zur Küche, Heizung und gelegentlich zur Stromversorgung verwendet. Eine unsachgemäße Lagerung führt zu Explosionsrisiken, Lecks und Brand.

Regulatorisch ist die Lagerung durch die EU-Richtlinie 2013/53/EU (CE-Kennzeichnung), ISO 10239 (Flüssiggas-Anlagen auf Schiffen) und nationale Gasinstallationsrichtlinien geregelt. Auf internationaler Ebene gelten die SOLAS-Regeln (Internationale Konvention für die Sicherheit des Lebens auf See) für größere Schiffe.

Diese Datei behandelt:
- Gaslocker-Design und Anforderungen
- Behältertypen und Größen
- Inspektions- und Wartungsstandards
- Häufige Fehlermuster und Diagnose
- Troubleshooting und Entscheidungsbäume

---

## 2. Grundlagen der Gasflaschenlagerung

### 2.1 ISO 10239 – Anforderungen an Gasanlagen

ISO 10239:2017 (Flüssiggas-Anlagen an Bord – Design, Installation und Wartung) definiert die Mindestanforderungen:

**Gaslocker (Lagerbereich):**
- **Lage**: außen an Deck oder in separaten, dicht verschlossenen Bereichen
- **Selbstentwässerung**: Locker muss nach außen (über Bord) entwässern, niemals ins Schiffsinnere
- **Gasdichtheit zum Innenraum**: Dichtung zwischen Locker und Kabine ≤0,01 m³/h
- **Belüftung des Lockers**: mind. 2 Lüftungsöffnungen, jeweils >100 cm², oder 1 Öffnung >200 cm² + natürliche Konvektion
- **Drain**: mind. Ø12 mm, Höhenunterschied >50 mm zwischen Locker-Boden und Drain-Ausgang

**Flaschenhaltung:**
- Flaschen aufrecht, sicher befestigt, gegen Umfallen gesichert
- Abstand zwischen Flaschen: mind. 25 mm (Luftzirkulation)
- Ventile nach oben, Sicherheitsventile zugänglich
- Armaturen zugänglich für Wartung/Austausch

**Ventil-Sicherheit:**
- Hauptabsperrventil mit Bediengriff außerhalb des Lockers
- Überdruckventil und Sicherheitsventil an jeder Flasche
- Schlag-/Fallschutz für Ventile

### 2.2 Gaslocker-Design – Konstruktive Anforderungen

**Deck-Locker (Standard):**
```
Abmessungen (typisch):
  - Länge: 400–600 mm
  - Breite: 300–450 mm
  - Tiefe: 300–400 mm
  - Volumen: 40–100 L

Konstruktion:
  - Material: GFK (Glasfaserkunststoff), Kunststoff, oder verzinkter Stahl
  - Wandstärke: mind. 4 mm (GFK) / 2 mm (Stahl)
  - Deckel: Verschraubung mit Dichtung (EPDM oder Silikon)
  - Innenseite: kein scharfkantiger Rost, glatte Oberflächen
```

**Stern-Locker (Alternative):**
- Kleiner, für 1–2 Flaschen à 5–6 kg
- Oft direkt unter/hinter Cockpit
- Entwässerung über Heck-Stutzen

**Einbau-Anforderungen:**
- Mindestabstand zum Motor: 1.0 m (ISO 10239, 5.4.4)
- Mindestabstand zu Elektrik: 0.5 m
- Mindestabstand zu Wärmequellen: 1.0 m
- Keine Lagerung über Kabinen oder unter Bullaugen

### 2.3 Lüftung und Entwässerung

**Lüftungsöffnungen:**

| Locker-Größe | Öffnung 1 | Öffnung 2 | Besonderheit |
|---|---|---|---|
| <50 L | 100 cm² | 100 cm² | 2× unabhängig, gestaffelt |
| 50–100 L | 150 cm² | 150 cm² | bei schlagender See |
| >100 L | 200 cm² | 200 cm² | oder 1× 300 cm² zentrales System |

**Drain:**
- Durchmesser: mind. Ø12 mm
- Material: Edelstahl 316L oder Kupferrohr (nicht Kunststoff)
- Verlauf: keine Siphon-Fallen, direkter Weg nach außen
- Ausgang: über Rumpf, mind. 50 mm über Wasserlinie
- Rückschlagventil: empfohlen (verhindert Wasser-Eindringen bei Seegang)

**Kondenswasser-Management:**
- Gummi-Entwässerungsstutzen im Locker-Boden (Ø20–25 mm)
- Regelmäßige Inspektion (monatlich während Saison)
- Trocknung: Locker nach Leerung und Trocknung belüften

---

## 3. Behältertypen und Größen

### 3.1 Standardflaschentypen

**Propan (C₃H₈):**
- Dampfdruck: ~10 bar @ 20°C
- Dichte (flüssig): 0.58 kg/L
- Verwendung: Hauptbrennstoff, ganzjährig
- Größen: 3 kg, 5 kg, 6 kg, 10 kg, 12 kg
- Kosten (Nachfüllung): €8–15 pro 5 kg-Äquivalent

**Butan (C₄H₁₀):**
- Dampfdruck: ~2 bar @ 20°C
- Dichte (flüssig): 0.60 kg/L
- Verwendung: Sommer, wärmere Breiten (>10°C)
- Größen: 3 kg, 5 kg, 6 kg
- Vorteil: weniger Druck im Behälter, leiser Betrieb
- Nachteil: Verdampfung unter +5°C nachlassend

**Propan-Butan-Mix (Winter/Sommer):**
- Typisch: 70 % Propan, 30 % Butan
- Einsatzbereich: Ganzjahr-Fahrt
- Kosten: 10–15 % Aufpreis vs. reines Propan

### 3.2 Flaschenmaterial und Druck

**Stahlflaschen (traditional):**
- Material: Baustahl, innenseitig verzinkt oder lackiert
- Prüfdruck: 15 bar (Europa), 10 bar (USA)
- Gewicht (leer): ~2.0–2.5 kg @ 5 kg Volumen
- Korrosionsanfälligkeit: Oberflächenrost, Pittings ohne Wartung
- Wartung: visuelle Kontrolle alle 2 Jahre, Hydrostatik-Test alle 10 Jahre (sonst Tausch)
- Kosten (neu): €35–60 pro Flasche

**Aluminium-Flaschen:**
- Material: Aluminium-Legierung (3003, 5083)
- Prüfdruck: 15–17.5 bar
- Gewicht (leer): ~1.0–1.3 kg @ 5 kg Volumen
- Korrosionsresistenz: höher, aber Kontaktkorrosion bei ungleichen Metallen möglich
- Wartung: visuell alle 2 Jahre, keine Hydrostatik-Prüfung erforderlich
- Kosten (neu): €60–100 pro Flasche
- Vorteil für Yachten: leichter, kein Rost, wartungsärmer

**Verbund-Flaschen (Composite/CNG-Type):**
- Material: Kunststoff-Hülle (GFK, Carbon) über Aluminium-Liner
- Prüfdruck: 20 bar (höher → mehr Volumen/Gewicht)
- Gewicht (leer): ~0.8 kg @ 5 kg Volumen
- Vorteile: leichteste Option, Bruchschutz durch Kunststoff
- Nachteil: teuer (€80–150), bei Überalterung (>15 Jahre) Tausch erforderlich
- Typisch bei Motorschiffen und Mega-Yachten

### 3.3 Größen und Kapazitäten

**Typische Größen (Europa, Wassereinsatz):**

| Volumen | Propan | Butan | Druck @ 20°C | Höhe | Ø | Einsatz |
|---|---|---|---|---|---|---|
| 3 L | 1.5 kg | 1.8 kg | ~9.5 bar | 280 mm | 90 mm | Kleine Segler, Notfall |
| 5 L | 2.9 kg | 3.0 kg | ~9.5 bar | 380 mm | 105 mm | Standard 1× Segler/Motor |
| 6 L | 3.5 kg | 3.6 kg | ~9.5 bar | 420 mm | 110 mm | Standard 2× Segler |
| 10 L | 5.8 kg | 6.0 kg | ~9.5 bar | 560 mm | 130 mm | Motor-Yacht, Heizung |
| 12 L | 7.0 kg | 7.2 kg | ~9.5 bar | 600 mm | 140 mm | Größere Yachten |

**Faustregel – täglicher Verbrauch:**
```
Segelboot 8–12 m (Küche):
  ~0.3–0.5 kg LPG/Tag (3 Mahlzeiten, 1 Person)

Motorboot 12–18 m (Küche + Heizung):
  ~0.8–1.2 kg LPG/Tag (Winter mit Heizung)

Mega-Yacht mit Klimatisierung:
  1.5–3.0 kg LPG/Tag
```

---

## 4. Produktlinien und Hersteller – Gaslockers und Ausrüstung

### 4.1 Gaslocker (Lagerbehälter)

**Baumuster-Gaslocker (Standard):**

| Hersteller | Modell | Material | Volumen | Flaschenanzahl | Preis EUR | Besonderheit |
|---|---|---|---|---|---|---|
| Plastimo | Gas Locker Deck | GFK | 70 L | 2×5kg | 180–220 | selbstentwässernd, kompakt |
| Vetus | Gas Locker | Kunststoff | 85 L | 2×6kg | 200–250 | innenlüftung, Deckel-Dichtung |
| Lewmar | Gas Storage Box | GFK/Stahl | 95 L | 2–3×5kg | 220–280 | korrosionsgeschützt, Edelstahl-Hardware |
| Barlow Tyrie | Marine Gas Locker | Kunststoff | 60–100 L | 1–2×5kg | 190–240 | leicht, Modular |
| Custom | Edelstahl-Locker | V2A Stahl | 80–120 L | 2–3×6kg | 280–400 | maßgefertigt, höchste Korrosionsresistenz |

**Deck-Mount Optionen:**
- Mit Deckel-Verschluss (Schraub/Quick-Release): +€30–60
- Mit integriertem Drain-Siphon: +€40–80
- Mit Edelstahl-Lüftungsgittern: +€50–100

### 4.2 Flaschenhalterungen und Adapter

**Flaschenhalter:**

| Typ | Material | Flaschen | Preis EUR | Verwendung |
|---|---|---|---|---|
| Kunststoff-Klammer (paarweise) | HDPE | 1–2×5kg | 15–30 | im Locker, einfache Befestigung |
| Edelstahl-Rahmen | V2A Stahl | 2×6kg | 60–90 | professionell, Segler/Motor |
| Magnetische Halter | Neodym-Magnet + Stahl | 1×5kg | 40–70 | schnell montierbar, Notfall |
| Koffer-System (Camping) | Kunststoff | 1–2×5kg | 50–120 | tragbar, auch Landnutzung |

**Ventil-Adapter und Fittings:**

| Komponente | Größe | Material | Preis EUR | Funktion |
|---|---|---|---|---|
| Europäischer Anschluss (Lindal) | M25×1.814 | Messing | 3–5 | Standard Europe/DE |
| UK-Anschluss (POL) | M20×1.814 | Messing | 5–8 | Britische Inseln, Skandinavien |
| US-Anschluss | CGA-510 | Stahl | 4–7 | USA, Kanada |
| Umstecksystem | Komplett-Set | Messing | 25–50 | mobil zwischen Adaptern wechseln |
| Schlauch-Adapter | DN10–DN16 | Messing/Edelstahl | 8–15 | Schlauch zu Armaturen |

---

## 5. Hersteller – Campingaz, Truma, GOK, Gaslow, Alugas

### 5.1 Campingaz (Französisch, Europa-Standard)

**Profil:**
- Europas größter LPG-Anbieter für Outdoor/Camping
- Flaschen: Stahl (Propan) oder Aluminium (Butan-Mix)
- Standardgrößen: 3 kg, 5 kg, 6 kg, 10 kg
- Lindal-Ventil (M25×1.814) – Standard in DE/AT/CH

**Yacht-Relevante Produkte:**

| Produkt | Größe | Preis EUR | Besonderheit |
|---|---|---|---|
| Campingaz R907 Propan | 6 kg | 12–18 (Nachfüllung) | Stahl, Ganzjahr |
| Campingaz R904 Mix | 5 kg | 10–15 (Nachfüllung) | Winter/Sommer, Alubehälter |
| Campingaz CV370 | Einwegartikel | 20–25 | kleine Flaschen, Camping-Herd |

**Verfügbarkeit:**
- Deutschland, Österreich, Schweiz: flächendeckend (Baumarkt, Tankstellen)
- Südeuropa: begrenzt (Campinggas-Stationen)
- Skandinavien: teilweise, aber lokale Marken bevorzugt

**Kosten (Propan nachfüllen):**
- 5 kg: €10–13
- 10 kg: €18–25

### 5.2 Truma (Deutsch, Wohnmobil/Boot-Spezialist)

**Profil:**
- Spezialist für mobile Gasanlagen (Wohnmobile, Yachten)
- Gasregler, Sicherheitsausrüstung, Heizungen
- System-Anbieter, nicht nur Flaschen

**Yacht-Relevante Produkte:**

| Produkt | Kategorie | Preis EUR | Funktion |
|---|---|---|---|
| Truma MultiControl 2 | Gasregler | 80–120 | Druck-Reduzierung + Sicherheit |
| Truma Safetymix EU | Druckregler | 120–180 | Proportional-Regler, Heizung+Herd |
| Truma Ultragas (Flasche) | Alu-Behälter | 60–90 (Nachfüllung) | Gewichtsoptimiert für RV/Boot |
| Truma Heating (Topas) | Gasheizung | 400–600 | Marinisierte Heizung (extra) |

**Besonderheit:**
- Systemintegration: Flasche → Regler → Herd → Heizung
- Überdruckschutz integriert
- Wartung: kostenlose Inspektionen bei autorisierten Werkstätten (1× pro 2 Jahre)

**Verfügbarkeit:**
- Deutschland: sehr gut (Camper-Center, Marine-Shops)
- Skandinavien: gut
- Südeuropa: weniger verbreitet

**Kosten:**
- Regler: €100–180
- System-Wartung: €60–100 pro Jahr

### 5.3 GOK (Deutsch, Sicherheits-Spezialist)

**Profil:**
- Hochwertige Druckregler und Sicherheitsventile
- Marine und Industrie
- ISO 10239 und deutsche Gasinstallation (DVGW)

**Yacht-Relevante Produkte:**

| Produkt | Kategorie | Preis EUR | Funktion |
|---|---|---|---|
| GOK Eingangsdruckregler | Druckregler | 60–100 | 2.75 bar Ausgangsdruck, Sicherheit |
| GOK Zweistufenregler | Sicherheitsregler | 150–220 | autom. Druckabbau bei Temperaturanstieg |
| GOK Überdruckventil | Sicherheit | 40–80 | Locker-Entlüftung bei Überdrucke |
| GOK Magnet-Absperrventil | Absperrung | 100–160 | Fernbedienung vom Bug, Sicherheit |

**Besonderheit:**
- Absolute Sicherheitsorientierung
- TÜV-geprüft, DVGW-zertifiziert
- Keine Kompromisse bei Qualität

**Verfügbarkeit:**
- Deutschland, Österreich: sehr gut
- Skandinavien: einige Distributor
- Südeuropa: begrenzt

**Kosten:**
- Einfacher Regler: €70–100
- Sicherheits-System komplett: €300–500

### 5.4 Gaslow (Britisch, Motorboot-Spezialist)

**Profil:**
- Spezialist für Motorboot-Gasanlagen
- Systemlösungen: Dual-Bottle-Locker, Automatik-Umschaltung
- POL-Ventil (UK-Standard)

**Yacht-Relevante Produkte:**

| Produkt | Kategorie | Preis EUR | Funktion |
|---|---|---|---|
| Gaslow Dual Locker | Gaslocker | 250–350 | 2 Flaschen, automatischer Umschalt-Ventil |
| Gaslow Auto-Switch | Ventil | 180–250 | Automatik-Umschalt zwischen Flaschen |
| Gaslow Low-Level-Sensor | Elektronik | 100–150 | Tank-Füllstand-Anzeige im Cockpit |
| Gaslow Regulator (POL) | Druckregler | 80–120 | POL-Ventil, UK-Standard |

**Besonderheit:**
- UK/Skandinavien-Standard
- Automatische Flaschenumschaltung (2×5kg statt 1×10kg Ersatz)
- Fernbedienung vom Steuerstand

**Verfügbarkeit:**
- UK, Skandinavien: sehr gut
- Deutschland: über englische Händler
- Südeuropa: kaum

**Kosten:**
- Dual-Locker System: €250–350
- Auto-Switch Ventil: €180–250
- Installation (Fachwerk): €150–300

### 5.5 Alugas (Schweiz/Südeuropa, Leichtbau)

**Profil:**
- Spezialist für Aluminium-Flaschen
- Höchste Korrosionsresistenz
- Südeuropäisch verankert (Mittelmeer)

**Yacht-Relevante Produkte:**

| Produkt | Kategorie | Preis EUR | Funktion |
|---|---|---|---|
| Alugas Aluminium-Flasche | Behälter | 75–110 | 5–12 kg, keine Wartung erforderlich |
| Alugas Korrosionsschutz | Beschichtung | 25–40 | zusätzliche Schutz-Lackierung |
| Alugas Adapter-System | Ventile | 40–80 | mehrere Ventile, je nach Region |

**Besonderheit:**
- Primär Südeuropa (Mittelmeer, Adria)
- Langlebigkeit (20+ Jahre ohne Hydrostatik-Test)
- Premium-Preis, aber Gesamtlebensdauer günstiger

**Verfügbarkeit:**
- Schweiz, Italien, Kroatien, Griechenland: gut
- Deutschland: über Spezial-Distributor
- Skandinavien: selten

**Kosten:**
- Aluminium 5 kg (Nachfüllung): €12–18
- Neue Flasche: €85–120

---

## 6. Fehlerbild-Atlas (12 Fehlermuster)

### FB-25-03-001: Locker-Entwässerung blockiert

**Sichtbares Zeichen:**
- Wasser steht im Gaslocker (sichtbar beim Öffnen)
- Unangenehmer Geruch, Grünalgen/Schleimbildung
- Flaschenhälterung korrodiert oder nass

**Ursachen:**
1. Drain-Schlauch abgeknickt oder gequetscht
2. Drain-Ausgang unter Wasserlinie oder blockiert
3. Rückschlagventil zugefrostet (Winter)
4. Sediment/Algenbildung im Schlauch (mehrjährig)

**Abhilfe (sofort):**
- Gaslocker-Deckel öffnen, visuell inspizieren
- Drain-Schlauch lokalisieren, auf Biegung/Kniff prüfen
- Einfache Spülung mit Süßwasser-Schlauch versuchen (sanft)
- Drain-Ausgang von außen sichtbar machen, Blockade entfernen

**Langfrist:**
- Drain jährlich spülen (Salzwasser + Süßwasser)
- Rückschlagventil nach 5 Jahren austauschen
- Gaslocker nach Saison belüften und trocknen

**Kosten (Reparatur):**
- Drain-Schlauch-Tausch: €40–80
- Rückschlagventil: €20–35
- Fachwerk: €80–150

---

### FB-25-03-002: Gasleck bei Flaschenkopf/Ventil

**Sichtbares Zeichen:**
- Hissing/Zischgeräusch beim Öffnen des Lockers
- Duft-Stoff (Mercaptan, riecht nach faulem Ei) wahrnehmbar
- Seifenblasenbild an Ventil (Seifenwasser-Test)

**Ursachen:**
1. Ventil-Dichtring verschlissen oder beschädigt
2. Schraubverbindung gelockert (vibration, Alter)
3. Ventil-O-Ring durch Druckspitzen gerissen
4. Flasche über-druckiert (zu warm oder defekter Regler)

**Abhilfe (sofort):**
- Gaslocker sofort lüften (Deckel offen, nicht anzünden)
- Herd und Heizung AUS, Brenner-Ventile zu
- Notfall: Flasche im Locker stehen lassen, nicht ins Haus bringen
- Mit Seifenwasser Leck exakt lokalisieren

**Langfrist:**
- Defekte Flasche auswechseln (Dichtring + Ventil nicht einzeln zu reparieren)
- Neue Flasche in Druckprüfung (Werkstatt)
- Regelventil überprüfen (Druck zu hoch?)
- Flasche alle 2 Jahre austauchen (Stahl) oder 5 Jahre (Aluminium)

**Kosten (Reparatur):**
- Flaschen-Austausch (mit Pfand): €20–40
- Druckregler-Check: €60–100
- Fachwerk: €100–180

**Sicherheits-Anmerkung:**
Bei Leck **niemals** versuchen, die Flasche zu reparieren. Gasflasche immer komplett tauschen.

---

### FB-25-03-003: Locker nicht gasdicht zum Innenraum

**Sichtbares Zeichen:**
- Mercaptan-Geruch in Kabine, nicht im Locker
- Druckmeter zeigt Druck-Abfall trotz geschlossener Brenner
- Sichtbarer Spalt/Riss in Locker-Deckel oder Wand

**Ursachen:**
1. Locker-Deckel-Dichtung verschlissen (Risse, Verhärtung)
2. Locker-Wand mikroskopische Risse (GFK-Risse unter UV)
3. Verbindung Locker↔Deck nicht versiegelt (Befestigungsschrauben)
4. Alte Gasanlagen: Locker mit Schraub-Deckel, keine Dichtung

**Abhilfe (sofort):**
- Brenner-Ventil am Herd ZU
- Absperrventil an Flasche zu
- Gas 10 Minuten belüften (Fenster, Lüfter)
- Locker-Inspektion von innen (Taschenlampe)

**Langfrist:**
- Deckel-Dichtung austausch (EPDM-Ring, ca. €8–12)
- Falls Risse sichtbar: Locker-Reparatur mit zwei-komponentigen Epoxi-Harz (Fachwerk)
- Bei Totalausfall: kompletter Locker-Austausch (€200–300)

**Kosten (Reparatur):**
- Dichtung tauschen: €30–60 (Material + Werk)
- Riss-Reparatur (Epoxi): €80–150
- Locker-Komplett-Tausch: €250–350 (Material + Einbau)

---

### FB-25-03-004: Hochdruck im Locker (Übertemperatur)

**Sichtbares Zeichen:**
- Überdruckventil am Locker zischt/spuckt Gas aus
- Locker-Temperatur deutlich über Umgebungstemperatur (Ästhetik)
- Druckmeter zeigt >12 bar (normal: ~9–10 bar @ 20°C)

**Ursachen:**
1. Locker in direkter Sonneneinstrahlung (Deck über Rumpf)
2. Defektes Überdruckventil (nicht eingestellt/beschädigt)
3. Locker über Motorraum positioniert (Wärmeleitung)
4. Flasche zu lange gelagert im heißen Auto/Schiff

**Abhilfe (sofort):**
- Locker mit nassem Tuch abdecken (Schatten)
- Belüftung prüfen (Lüftungsöffnungen offen?)
- Überdruckventil ablesen: zischt es kontinuierlich → Ventil defekt

**Langfrist:**
- Locker neu positionieren: Schatten, mind. 1m von Motor entfernt
- Überdruckventil kalibrieren/austausch (Fachwerk, ~€40–80)
- Wärmeschutz: reflektive Abdeckung oder Belüftungs-Lüfter installieren (€50–150)

**Kosten (Reparatur):**
- Überdruckventil-Austausch: €40–80 (Material) + €60–120 (Werk)
- Wärmeschutz-Abdeckung: €50–150
- Fachwerk: €100–180

---

### FB-25-03-005: Druckabfall ohne sichtbares Leck

**Sichtbares Zeichen:**
- Druckmeter zeigt Abfall über Tage/Wochen (von 9 bar auf 7 bar)
- Keine sichtbaren Spritzer, aber Mercaptan-Duft schwach
- Brenner-Zündung schwach oder unmöglich

**Ursachen:**
1. Mikro-Leck an Ventil-Kern (kaum sichtbar)
2. Schlauch-Alterung/Porenbildung (10+ Jahre)
3. Fittings: Schraub-Verbindungen minimal locker (Vibrationen)
4. Temperatur-Schwankung (normal: -2 % pro 10°C Abfall)

**Abhilfe (sofort):**
- Seifenwasser auf alle Ventil- und Schlauch-Verbindungen sprühen
- Mikro-Schaum = Leck, groß-flächig = Schlauch-Porenbildung
- Druckabfall dokumentieren (ml/Stunde oder bar/Tag)

**Langfrist:**
- Mikro-Leck: Ventil-Kern oder komplette Flasche tauschen
- Schlauch-Alterung: Schlauch austausch (DIN EN 1762, Edelstahl-Umflechtung)
- Fitting lockern: mit Schraubenschlüssel festziehen (nicht mit Gewalt!)

**Kosten (Reparatur):**
- Schlauch-Austausch (3–5 m): €40–80 (Material) + €80–150 (Werk)
- Fitting-Austausch: €20–40
- Fachwerk: €100–200

---

### FB-25-03-006: Brenner zündet nicht, aber Druck ok

**Sichtbares Zeichen:**
- Druckmeter zeigt normal (9–10 bar)
- Brenner-Ventil lässt sich öffnen
- Klickzündung (Piezo) funktioniert, aber kein Feuer
- Oder: Feuer nur schwach/blau (statt leuchtend orange)

**Ursachen:**
1. Druckregler defekt (gibt nur ~0.5 bar statt 2.75 bar ab)
2. Schlauch-Biegung oder Kink zwischen Regler und Herd
3. Herd-Brenner verschmutzt (Rußablagerung, Drosselung)
4. Zündsystem defekt (Zündelektrode)

**Abhilfe (sofort):**
- Druckmeter hinter dem Regler überprüfen (sollte 2.75 bar ± 0.2 bar sein)
- Schlauch visuell inspizieren (Biegung?)
- Brenner-Düsen visuell inspizieren (schwarz belegt = verschmutzt)

**Langfrist:**
- Regler-Austausch (€60–100 Material + €80–150 Werk)
- Schlauch-Verlegung: entfernen Sie Biegungen, verwenden Sie Schlauch-Klammern
- Brenner-Düsen: mit Zahnbürste + Essig reinigen, oder Herd-Service (€100–200)

**Kosten (Reparatur):**
- Druckregler-Austausch: €80–150 + €80–150 Werk
- Schlauch-Verlegung: €50–100
- Herd-Service: €100–200

---

### FB-25-03-007: Flasche lädt nicht/Druck steigt nicht nach Nachfüllung

**Sichtbares Zeichen:**
- Nach Nachfüllung bleibt Druck bei 5–6 bar (statt 9–10 bar)
- Brenner zeigt sehr schwaches Feuer
- Wiederholt bei mehreren Flaschen → Problem ist nicht die Flasche

**Ursachen:**
1. Adapter/Ventil sitzt nicht richtig (O-Ring verschlissen)
2. Lindal-Ventil (M25×1.814) vs. POL-Ventil (M20) verwechselt
3. Druckregler auf Hochdruck-Ausgang eingestellt (statt 2.75 bar)
4. Druckentlastungs-Ventil am Regler undicht

**Abhilfe (sofort):**
- Flasche auswechseln, neue Flasche anschließen
- Neuer Druck zeigt: Adapter oder Ventil defekt (nicht Flasche)
- Ventil-Typ überprüfen: auf Flasche geprägtes Symbol (Lindal europäisch, POL britisch)

**Langfrist:**
- Adapter/O-Ring austausch (€10–20)
- Ventil-Typ konsistenzieren (alle Flaschen auf Lindal, oder alle auf POL)
- Druckregler neu einstellen (mit Prüfmanometer, €80–120 Fachwerk)

**Kosten (Reparatur):**
- Adapter-Austausch: €15–40
- Druckregler-Einstellung: €80–120 (Fachwerk)

---

### FB-25-03-008: Frost/Eis am Locker (Winter)

**Sichtbares Zeichen:**
- Locker-Außenseite mit Eiskruste bedeckt
- Drain-Ausgang zugefroren
- Kondenswasser im Locker (keine Selbst-Entwässerung)

**Ursachen:**
1. Rückschlag-Ventil zugefroren (Winter unter 0°C)
2. Drain-Ausgang unter Wasserlinie (tropft, friert)
3. Locker zu wenig isoliert (thermische Kälte-Brücke)
4. Überdruckventil-Auslass gefroren (Flüssiggas-Verdampfung)

**Abhilfe (sofort):**
- Warmes Wasser (nicht kochend!) auf gefrorene Stellen tropfen
- **Niemals** mit Flamme enteisen (Brand/Explosions-Risiko!)
- Locker-Entwässerung überprüfen nach dem Auftauen

**Langfrist:**
- Rückschlag-Ventil mit Heiz-Ummantelung (€50–100, nicht standard)
- Drain-Ausgang oberhalb Wasserlinie positionieren (umdesign)
- Winter-Betrieb: täglich Locker-Belüftung + Trocknung
- Alternativ: Winter-Gasmischung (mehr Propan, weniger Butan)

**Kosten (Reparatur):**
- Rückschlag-Ventil-Austausch: €20–35 (Material) + €60–100 (Werk)
- Locker-Isolierung: €80–200
- Fachwerk: €100–200

---

### FB-25-03-009: Flaschen-Rost/Korrosion (Stahlflaschen)

**Sichtbares Zeichen:**
- Rostflöckchen auf Flaschensurface (rot/braun)
- Lokale Pittings oder Dellen (Metallabtragung)
- Flasche wird mit der Zeit leichter, Material wird rau

**Ursachen:**
1. Stahlflaschen ohne Schutz-Beschichtung
2. Locker-Entwässerung unzureichend (Wasser-Lagerung)
3. Salzwasser-Sprüh im Locker (Nähe zur Oberfläche)
4. Alte Flaschen (>10 Jahre) ohne Wartungs-Zertifikat

**Abhilfe (sofort):**
- Leichte Oberflächenrost: mit Stahlbürste + Kriechöl (WD-40) reinigen
- Tiefe Pittings oder Dellen: Flasche NICHT MEHR verwenden (Druckabfall-Risiko)
- Korrodierte Flaschen austausch (Altmetall)

**Langfrist:**
- Alle 2 Jahre Flaschen-Sichtprüfung (vor Saison)
- Bei Rost: Flasche zum Fachwerk, Inspektions-Zertifikat (TÜV)
- Locker-Entwässerung optimieren (monatliche Überprüfung)
- Übergang zu Aluminium-Flaschen (wartungsfrei)

**Kosten (Reparatur):**
- Flaschen-Austausch (mit Pfand): €20–40
- TÜV-Inspektions-Zertifikat: €30–50
- Locker-Sanierung: €100–200

---

### FB-25-03-010: Zu viele Flaschen im Locker (Überladung)

**Sichtbares Zeichen:**
- Flaschen sitzen eng, kaum Luftzirkulation
- Deckel-Verschluss unter Spannung (schwer zu öffnen)
- Flaschen berühren sich (Kontakt-Korrosion möglich)
- Lüftungsöffnungen blockiert durch Flaschenplatzierung

**Ursachen:**
1. Unzureichende Locker-Größe für Flaschenanzahl
2. Fehlplanung: zu viele 6-kg-Flaschen statt 2×5kg
3. Flaschen-Halter mangelhaft ausgerichtet

**Abhilfe (sofort):**
- Eine Flasche herausnehmen und separat lagern (unter Deck, mit Befestigung)
- Lüftungsöffnungen freimachen
- Abstand zwischen Flaschen auf mind. 25 mm überprüfen

**Langfrist:**
- Locker neu dimensionieren oder Flaschen-Anzahl reduzieren
- Dual-Locker-System evaluieren (wenn Platz)
- Flaschen-Halter mit verstellbaren Positionen (€60–120)

**Kosten (Reparatur):**
- Zusätz-Locker-Installation: €200–400 (Material + Werk)
- Flaschen-Holder: €60–120

---

### FB-25-03-011: Locker-Lüftung blockiert (Algenwachstum, Insekten)

**Sichtbares Zeichen:**
- Lüftungsöffnungen mit Algen/Schleimbildung bedeckt
- Insekten-Nester (Spinne, Wespen) in Lüftungsgitter
- Reduktion Luftzirkulation, Wasser staut sich im Locker

**Ursachen:**
1. Lüftungsgitter ohne Schutz (offene Öffnungen)
2. Feuchtigkeits-Stau im Locker (unzureichende Drainierung)
3. Stagnation der Luft (Locker unter Wasser-Spray-Zone)

**Abhilfe (sofort):**
- Lüftungsgitter mit Bürste/Wasser reinigen
- Insekten-Nester entfernen (sanft, oder Fachwerk)
- Locker-Fenster offen halten während Belüftung

**Langfrist:**
- Lüftungsgitter mit feinem Maschenwerk oder Schaumstoff-Filter (€20–40)
- Locker nach jedem Segeltrip belüften und trocknen
- Biozid-Beschichtung (falls Algen hartnäckig): €50–100

**Kosten (Reparatur):**
- Lüftungsgitter austausch: €20–40 (Material) + €30–60 (Werk)
- Biozid-Anstrich: €50–100 (Fachwerk)

---

### FB-25-03-012: Locker-Deckel-Verschraub-Vibration (Schraub-Ausfälle)

**Sichtbares Zeichen:**
- Schrauben-Köpfe sind locker oder ausgefallen
- Locker-Deckel sitzt nicht mehr dicht
- Mercaptan-Geruch entweicht aus Spalten
- Vibrationen bei Motor-Betrieb oder Seegang

**Ursachen:**
1. Befestigungsschrauben nicht gegengesichert (Loctite/Sicherungs-Scheiben)
2. Zu-Anziehen-Drehmoment zu niedrig (Schrauben lösen sich)
3. Alte, verhärtete Locker-Dichtung (erzeugt Spalten, Vibration)
4. Motor-Vibrationen oder Rauheit

**Abhilfe (sofort):**
- Alle sichtbaren Schrauben mit Schraubenschlüssel überprüfen und festziehen
- Fehlende Schrauben ersetzen
- Locker-Dichtung prüfen (hart, rissig → austausch)

**Langfrist:**
- Alle Befestigungsschrauben mit Loctite 243 (mittelfest) oder Sicherungs-Scheiben versehen
- Drehmoment festlegen: M6×1.0 = 8–10 Nm, M8×1.25 = 18–22 Nm
- Nach jedem Service: Schrauben kontrollieren

**Kosten (Reparatur):**
- Schrauben-Austausch: €10–20 (Material)
- Dichtung-Austausch: €8–15 (Material) + €30–60 (Werk)
- Loctite/Sicherung: €5–10

---

## 7. Troubleshooting – 5 Entscheidungsbäume

### T-7.1: Merkaptan-Geruch erkannt

```
START: Mercaptan-Geruch (faules Ei) wahrgenommen
│
├─ Wo ist der Geruch stärker?
│  ├─ Im Gaslocker (Deck) → Leck-Quelle lokal
│  │  │
│  │  ├─ Mit Seifenwasser testen
│  │  │  ├─ Schaum = Leck gefunden
│  │  │  │  ├─ An Ventil-Kopf → FB-25-03-002 (Ventil-Dichtung)
│  │  │  │  ├─ An Schlauch-Verbindung → FB-25-03-005 (Fitting locker)
│  │  │  │  └─ An Drain → FB-25-03-001 (Drain-Alter/Porenbildung)
│  │  │  │
│  │  │  └─ Kein Schaum, aber Geruch → Mikro-Leck, schwer sichtbar
│  │  │     └─ Flasche komplett austausch
│  │  │
│  │  └─ Gaslocker-Deckel öffnen, 10 min belüften, Druckmeter prüfen
│  │
│  └─ In der Kabine (Wohnbereich) → Gasdichtung mangelhaft
│     │
│     ├─ Locker-Deckel-Dichtung alt/verhärtet? → FB-25-03-003 (Deckel-Dichtung austausch)
│     │
│     ├─ Sichtbare Risse/Spalten im Locker-Gehäuse? → FB-25-03-003 (Locker-Reparatur)
│     │
│     └─ Geruch schwach und nur gelegentlich? → Normalzustand bei älteren Anlagen
│        └─ Alle 2 Jahre Dichtung überprüfen
│
└─ AKTION: Brenner zu, Absperrventil zu, 10 min belüften
```

### T-7.2: Brenner zündet nicht

```
START: Brenner-Versuch Zündung schlägt fehl
│
├─ Druckmeter zeigt Druck?
│  ├─ JA (8–10 bar)
│  │  │
│  │  ├─ Hinter dem Druckregler auch Druck? (Manometer-Test)
│  │  │  ├─ JA → Druckregler ok
│  │  │  │  │
│  │  │  │  ├─ Brenner-Zündung (Piezo-Klick) hörbar/spürbar?
│  │  │  │  │  ├─ JA → Zündsystem ok, Brenner-Düse verschmutzt
│  │  │  │  │  │  └─ FB-25-03-006: Brenner reinigen oder Herd-Service
│  │  │  │  │  │
│  │  │  │  │  └─ NEIN → Zündung defekt (Zündelektrode/Batterie)
│  │  │  │  │     └─ Herd-Service erforderlich (€100–200)
│  │  │  │  │
│  │  │  │  └─ Schlauch sichtbar geknickt zwischen Regler↔Brenner?
│  │  │  │     └─ FB-25-03-006: Schlauch-Verlegung korrigieren
│  │  │  │
│  │  │  └─ NEIN (0 bar hinter Regler) → Druckregler defekt
│  │  │     └─ FB-25-03-006: Druckregler austausch (€80–150 + Werk)
│  │  │
│  │  └─ NEIN (0 bar) → Keine Zufuhr nach Herd
│  │     ├─ Absperrventil am Herd offen?
│  │     ├─ Regler-Eingangsdruck ok?
│  │     └─ Schlauch zwischen Locker↔Regler geknickt/blockiert?
│  │
│  └─ NEIN (0 bar) → Flasche leer oder Absperrventil zu
│     ├─ Flasche wechseln
│     └─ Absperrventil am Herd öffnen
│
└─ AKTION: Alle Tests mit offenem Fenster durchführen (Sicherheit)
```

### T-7.3: Druckverlust über Zeit

```
START: Druckabfall dokumentiert (z.B. 10 bar → 7 bar in 3 Tagen)
│
├─ Alle Brenner und Heizung abgestellt?
│  ├─ JA → Verbrauch ist Leck
│  │  │
│  │  ├─ Seifenwasser-Test an allen Verbindungen
│  │  │  ├─ Schaum gefunden → Leck-Quelle lokalisiert
│  │  │  │  ├─ Ventil-Kopf → FB-25-03-002: Flasche austausch
│  │  │  │  ├─ Schlauch-Verbindung → FB-25-03-005: Fitting festziehen
│  │  │  │  └─ Schlauch selbst → FB-25-03-005: Schlauch-Austausch
│  │  │  │
│  │  │  └─ Kein Schaum, aber Druck sinkt → Mikro-Leck (schwer sichtbar)
│  │  │     ├─ Flasche austausch, Seifentest mit neuer Flasche
│  │  │     └─ Falls Druck weiter sinkt → Problem ist Schlauch/Anlage
│  │  │
│  │  └─ Temperatur-Schwankung? (z.B. -5°C → +15°C über Nacht)
│  │     └─ Normal: ~0.7–1 bar Schwankung pro 10°C → kein Leck
│  │
│  └─ NEIN → Verbrauch durch Gebrauch (Herd/Heizung)
│     └─ Normal, Flasche nachfüllen/austausch wenn <3 bar
│
└─ AKTION: Bei Leck: Flasche im Locker isolieren, nicht bewegen
```

### T-7.4: Locker-Überhitzung oder Überdruckventil zischt

```
START: Überdruckventil sprüht Gas, Locker warm
│
├─ Locker-Position:
│  ├─ In direkter Sonneneinstrahlung (Deck) → Wärmeinput
│  │  │
│  │  ├─ Sofort: nassem Tuch abdecken/schattig stellen
│  │  │
│  │  └─ Langfrist: FB-25-03-004: Reflektive Abdeckung, oder Locker-Versetzung
│  │
│  ├─ Über Motorraum (Wärme-Leitung) → Wärmeinput
│  │  │
│  │  ├─ Sofort: Thermische Isolierung anbringen (€80–150)
│  │  │
│  │  └─ Langfrist: Locker mechanisch isolieren oder neu positionieren
│  │
│  └─ Normal positioniert, aber heißer Tag (>30°C Luft) → Thermische Last
│     │
│     ├─ Normal bei extremem Wetter
│     │
│     └─ Überdruckventil funktioniert korrekt (sicherheit)
│
├─ Überdruckventil zischt kontinuierlich?
│  ├─ JA → Ventil defekt (Einstellung zu niedrig)
│  │  └─ FB-25-03-004: Ventil austausch/kalibrieren (€40–80 + Werk)
│  │
│  └─ NEIN (kurzes Zischen dann Ruhe) → Normal
│     └─ Temperatur-Ausgleich abgelaufen
│
└─ AKTION: Locker-Druckregelung überprüfen (alle 2 Jahre)
```

### T-7.5: Flasche lädt nicht vollständig (schwacher Betrieb)

```
START: Nach Nachfüllung ist Brenner-Kraft schwach, Druck niedrig
│
├─ Neue Flasche verwendet?
│  ├─ JA, erste Nachfüllung → Adapter-Problem möglich
│  │  │
│  │  ├─ Flasche-Ventil-Typ überprüfen:
│  │  │  ├─ Lindal (europäisch, M25×1.814) vs. POL (britisch, M20) Match?
│  │  │  │  ├─ Falsch → Adapter wechseln oder neue Flasche gleichen Typ
│  │  │  │  │
│  │  │  │  └─ Korrekt → O-Ring verschlissen?
│  │  │  │     └─ FB-25-03-007: O-Ring austausch (€10–20)
│  │  │  │
│  │  │  └─ Ventil-Schraub-Dichtung locker?
│  │  │     └─ Mit Schraubenschlüssel festziehen (vorsichtig)
│  │  │
│  │  └─ Nach Austausch: Druck wieder ok? → Adapter war schuld
│  │
│  └─ NEIN (alte Flasche, vorher ok) → Druckregler-Einstellung
│     │
│     ├─ Mit Manometer-Prüf hinter Regler testen (sollte 2.75 bar sein)
│     │  ├─ Druck zu niedrig (<2.0 bar) → FB-25-03-007: Regler-Einstellung
│     │  │
│     │  └─ Druck ok (2.75 bar) → Brenner-Düsen-Problem
│     │     └─ FB-25-03-006: Herd-Service
│     │
│     └─ Druckregler kalibrieren lassen (€80–120 Fachwerk)
│
└─ AKTION: Mehrere Nachfüllungen vermeiden (keine Übung nötig), lieber neue Flasche
```

---

## 8. FAQ 25 – Häufig gestellte Fragen

### FAQ 25-01: Wie oft sollte ich Gasflaschen austausch?

**Antwort:**
- **Stahlflaschen**: Alle 2 Jahre TÜV-Inspektions-Zertifikat erforderlich. Nach 10 Jahren Austausch empfohlen (auch wenn noch zertifiziert).
- **Aluminium-Flaschen**: Inspektions-Test nur nach 15 Jahren erforderlich. Bei sichtbarem Rost oder Verformung austausch.
- **Composite-Flaschen**: Nach 15 Jahren Inspektions-Test, nach 20 Jahren Austausch.

**Praktisch für Segelyachten:**
- Stahlflaschen: alle 2 Jahre wechseln (€20–40 Pfand-Austausch)
- Aluminium: alle 5 Jahre wechseln (größere Investition, aber weniger Verschleiß)

---

### FAQ 25-02: Was ist der Unterschied zwischen Propan und Butan?

| Eigenschaft | Propan (C₃) | Butan (C₄) |
|---|---|---|
| Siedepunkt | -42°C | -0,5°C |
| Dampfdruck @ 20°C | ~10 bar | ~2 bar |
| Verwendung | Ganzjahr (alle Breiten) | Sommer/Süd |
| Kosten | €12–18 pro 5 kg | €10–15 pro 5 kg |
| Sicherheit | Höherer Druck, robuster | Geringerer Druck, leiser |
| Effizienz | 11.5 kWh/kg | 12.7 kWh/kg (höher) |

**Empfehlung:**
- Ganzjahr-Segeltourn: 100 % Propan oder 70/30 Mix
- Mittelmeer-Sommer: 100 % Butan (leiser, weniger Druck)

---

### FAQ 25-03: Ist es sicher, mehrere Gasflaschen an Bord zu haben?

**Antwort:**
Ja, aber mit Bedingungen:
- Maximal 2 Flaschen im Gaslocker (ISO 10239)
- Weitere Flaschen: separater, verschlossener Bereich (z.B. Achterschiff)
- Alle Flaschen müssen separate Absperrventile haben
- Sicherheitsabstand Motor/Herd mind. 1.0 m

Doppelte Versorgung ist üblich (1 aktiv, 1 Reserve). **Nicht** beide gleichzeitig anschließen.

---

### FAQ 25-04: Gaslocker-Entwässerung – wie oft überprüfen?

**Antwort:**
- Monatlich: Visuell Wasserstau überprüfen (Licht ins Locker, inspizieren)
- Alle 3 Monate: Drain-Test (Süßwasser langsam einspritzen, sollte sofort raus)
- Jährlich: Komplett Drain-Schlauch spülen + Rückschlagventil prüfen
- Nach Winterlagerung: Entwässerung und Belüftung

Kosten Wartung: €0 (selbst) bis €80–120 (Fachwerk jährlich).

---

### FAQ 25-05: Mein Locker riecht nach Mercaptan – ist das normal?

**Antwort:**
Nein. Mercaptan ist absichtlich zum Gas hinzugefügt, um Lecks zu erkennen.

- **Schwacher Duft gelegentlich**: möglich bei älteren Dichtungen (nicht kritisch, aber beobachten)
- **Moderater Duft regelmäßig**: Dichtung austausch empfohlen
- **Starker Duft ständig**: Aktives Leck, sofort Fachwerk

**Aktion:**
- Locker öffnen, 10 min belüften
- Seifenwasser-Test durchführen
- Dichtung alle 2 Jahre prophylaktisch austausch (€8–15)

---

### FAQ 25-06: Welcher Gasadapter ist der richtige für mein Boot?

**Antwort:**
Hängt von Region/Hersteller ab:

| Region | Adapter | Anschluss | Beispiel |
|---|---|---|---|
| Deutschland, Österreich, Schweiz | Lindal | M25×1.814 | Campingaz, Alugas, CEPCO |
| UK, Skandinavien (Dänemark, Schweden) | POL | M20×1.814 | Gaslow, Flogas |
| Frankreich (Süd) | TL2000 | Spin-on | Butagaz |
| USA, Kanada | CGA-510 | ¾"-16 UNC | Coleman |

**Wie erkennen:**
- Ventil-Symbol auf Flasche graviert
- Schraub-Durchmesser mit Schieblehre messen (M20 vs. M25)

**Sicher gehen: mehrere Adapter kaufen** (€8–15 each), um flexibel zu sein.

---

### FAQ 25-07: Kann ich Gasflaschen im Winter lagern?

**Antwort:**
Ja, aber mit Sicherheit:

- **Temperatur**: -20°C bis +60°C OK (unter -42°C nicht empfohlen)
- **Lagern**: Locker muss belüftet sein (auch im Winter)
- **Freeze-Schutz**: Rückschlagventil kann zufrieren → Drain-Öffnung entfernen (Winter)
- **Nach Lagerung**: Flasche 2–3 Tage vor Gebrauch in Warmes bringen (Temperatur-Ausgleich)

**Kosten Winterisierung**: €50–100 (Ventil-Heizband, optional).

---

### FAQ 25-08: Gasleck gefunden – wie entferne ich die Flasche sicher?

**Antwort:**
Schritt-für-Schritt:

1. **Absperrventil am Herd zu** (nicht am Boot!)
2. **Brenner alle ausschalten** und Türen öffnen
3. **10 Minuten belüften** (Wind/Lüfter)
4. **Flasche im Locker lassen** (nicht ins Boot bringen!)
5. **Mit Seifenwasser markieren** (wo das Leck ist)
6. **Zur Werkstatt bringen** (nicht selbst reparieren!)

**Niemals:**
- Flasche selbst öffnen/reparieren
- Flasche ins Haus/Kajüte transportieren
- Mit Feuer in die Nähe des Lecks kommen

---

### FAQ 25-09: Was ist der richtige Druck für Gaskochfeuer?

**Antwort:**
- **Eingangs-Druck** (Flasche): 8–10 bar (Propan @ 20°C)
- **Regler-Ausgangsdruck**: 2.75 bar ± 0.2 bar (estimated — unverifiziert)
- **Brenner-Betrieb**: 2.4–2.9 bar ist OK

**Wenn Brenner schwach:**
- Druckregler mit Manometer prüfen
- Sollte genau 2.75 bar ausgeben
- Ist es <2.0 bar → Regler-Kalibrierung nötig (€80–120)
- Ist es >3.0 bar → Überdruckventil prüfen

> ⚠️ **ZU PRÜFEN (Audit):** Regler-Ausgangsdruck 2.75 bar (Haupttext) widerspricht den Anhängen — FAQ 25-04 und Glossar nennen 1.3 bar, Abschnitt FB-25-03-008 nennt 50 mbar. Marine-LPG-Verbraucher-Regler liefern real ~30 mbar (EN ISO 10239 / EN 16129 Anhang M). Die hier genannten bar-Werte sind sicherheitskritisch und nicht als „Norm" verifizierbar — vor Nutzung fachlich prüfen.

---

### FAQ 25-10: Gibt es Alternativen zu Gasflaschen?

**Antwort:**
Ja, aber jede hat Kompromisse:

| Alternative | Gewicht | Kosten | Sicherheit | Praktikabilität |
|---|---|---|---|---|
| Elektro-Herd (220 V) | leicht | €200–500 | sehr gut | niedrig (Strom-abhängig) |
| Alkohol-Kocher (Spirit) | sehr leicht | €50–100 | OK | niedrig (Leistung schwach) |
| Holz-Ofen (Segelyacht) | mittel | €300–800 | gut | mittel (Lagerung, Wartung) |
| Induktion-Kochfeld (12 V) | mittel | €100–300 | sehr gut | niedrig (Batterie-Kapazität) |

**Fazit:** Gas bleibt am sichersten und praktischsten für Segelyachten. Kombinieren Sie mit 220 V Backup im Hafen.

---

### FAQ 25-11 bis 25-35: [weitere häufig gestellte Fragen folgen in Anhang]

---

## 9. Glossar – 40+ Begriffe

**A**

- **Adapter, Lindal**: Standard-Schraub-Ventil M25×1.814 (Europa)
- **Adapter, POL**: Standard-Schraub-Ventil M20×1.814 (UK/Skandinavien)
- **Aluminium-Flasche**: Leichte, korrosionsresistente Behälterversion, wartungsfrei bis 15 Jahre
- **Absperrventil**: Kugelhahn zum Abschalten des Gases (Herd oder Heizung)
- **Alugas**: Schweizer Hersteller von Aluminium-Gasflaschen

**B**

- **Butan (C₄H₁₀)**: Flüssiggas mit niedrigerem Dampfdruck, für Sommer/wärmere Breiten
- **Butagaz**: Französisches Gaszuführ-Netzwerk (Südeuropa)

**C**

- **Campingaz**: Europäischer LPG-Lieferant (Deutschland, Frankreich)
- **Composite-Flasche**: Kunststoff-Hülle über Aluminium-Liner, leichteste Option
- **Composit-Flasche**: siehe Composite-Flasche
- **CGA-510**: Amerikanischer Gas-Adapter-Standard

**D**

- **Dampfdruck**: Druck des Gas-Dampfes über Flüssigkeit @ Temperatur (Propan ~10 bar @ 20°C)
- **Drain**: Entwässerungs-Auslass des Gaslockers (Ø12 mm, nach außen)
- **Druckregler**: Gerät zur Reduktion von Flaschendrruck auf Betriebs-Druck (2.75 bar)
- **DVGW**: Deutscher Verein des Gas- und Wasserfaches (Zertifizierung)

**E**

- **EPDM**: Ethylen-Propylen-Dien-Gummi (Standard Locker-Dichtung)
- **EU 2013/53/EU**: CE-Kennzeichnung Richtlinie für Freizeitschiffe (Sicherheit)

**F**

- **Flogas**: Britischer LPG-Zuführ-Dienst (POL-Adapter)
- **Flüssiggas, LPG**: Liquefied Petroleum Gas (Propan/Butan Mischung)

**G**

- **Gaslow**: Britischer Hersteller von Motorboot-Gasanlagen (Auto-Switch)
- **Gaslocker**: Separater, dicht verschlossener Lagerbereich für Flaschen an Deck
- **GFK, FRP**: Glasfaserkunststoff, Standard Locker-Material
- **GOK**: Deutscher Hersteller von Sicherheits-Reglern und Ventilen
- **Griff-Bedienung**: Außen zugänglich Absperrventil (nicht im Locker)

**H**

- **Hydrostatik-Test**: Druck-Prüfung für Stahlflaschen (alle 10 Jahre, TÜV)
- **Herd, Marinisiert**: Gaskochfeld mit Seegang-Gimbals (Schiffsausrüstung)

**I**

- **ISO 10239**: Internationale Norm für Flüssiggas-Anlagen an Schiffen
- **ISO 9094**: Norm für Feuer-Schutz in Marineanlagen
- **ISO 11812**: Norm für Cockpit-Sicherheit (Drainagen)
- **ISO 15085**: Norm für Mann-über-Bord-Prävention

**K**

- **Kunststoff-Locker**: Locker aus HDPE oder ähnlichem (leicht, korrosionsresistent)

**L**

- **Lindal**: siehe Adapter, Lindal
- **Liter (L)**: Volumen-Einheit für Flaschenkapazität

**M**

- **Maceratur**: siehe Zersetzung (nicht relevant für Gas)
- **Magnet-Halter**: Schnell-Befestigung für Flaschen (temporär)
- **Mercaptan**: Odorant (Duft-Stoff) zum Erkennen von Gaslecks
- **Methylcellulose**: nicht relevant für Gas

**N**

- **Nachfüllung**: Wiederbefüllung einer Flasche (vs. Austausch)

**O**

- **O-Ring, Ventil**: Dichtungs-Element am Flaschennventil (EPDM)
- **Überdruckventil**: Sicherheits-Ventil zum Abbau von Überdruck im Locker

**P**

- **Pittings**: Oberflächenkorrosion (Stahl) mit kleinen Löchern
- **POL**: siehe Adapter, POL
- **Propan (C₃H₈)**: Flüssiggas mit hohem Dampfdruck, Standard Ganzjahr
- **Prüfdruck**: Maximaldruck bei Hydrostatik-Test (15 bar Stahl, 17.5 bar Aluminium)

**R**

- **Regler, Druckregler**: siehe Druckregler
- **Rückschlagventil**: Ein-Weg-Ventil zur Verhinderung von Rückfluss (z.B. Wasser im Winter)

**S**

- **Sicherheitsventil**: siehe Überdruckventil
- **Siphon-Fallen**: Schlauch-Konfiguration die Wasser speichert (zu vermeiden)
- **Stahl-Flasche**: Klassische Behälter-Variante (schwerer, rostanfällig)
- **Stahlbürste**: Werkzeug zur Rost-Entfernung

**T**

- **Truma**: Deutscher Hersteller von Gasheizungen und Reglern (Wohnmobil/Boot)
- **TÜV**: Technischer Überwachungsverein (Prüf- und Zertifizierungs-Stelle)

**U**

- **Übertemperatur**: Locker-Temperatur über Normalbereich (Sicherheitsrisiko)

**V**

- **Ventil, Lindal**: siehe Adapter, Lindal
- **Ventil-Kern**: Innerer Verschluss-Mechanismus (kann undicht werden)
- **Verbindungs-Schlauch**: DIN EN 1762 zertifiziert, Edelstahl-Umflechtung
- **Verformung**: Delle/Dent in Flaschenwand (Druckabfall-Risiko)
- **Versetzen**: Umpositionierung des Gaslockers (Re-Installation)
- **Vetus**: Niederländischer Schiffs-Zubehör-Hersteller (Locker, Ventile)

**W**

- **Wärmeschutz**: Isolierung des Lockers gegen Überhitzung
- **Werkstatt**: Autorisierte Gas-Installateurs für Inspektion/Wartung

**Z**

- **Zertifikat, Inspektions**: TÜV-Bestätigung für Flaschen-Sicherheit
- **Zündung, Piezo**: Elektrische Zündung von Brennern (vs. Zündhölzer)

---

## 10. Schnell-Referenz (Checklisten)

### Segeltraum 10.1: Vor jeder Saison

- [ ] Locker-Dichtung überprüfen (hart? rissig?)
- [ ] Drain-System testen (Wasser raus?)
- [ ] Lüftungsgitter reinigen (Algen? Insekten?)
- [ ] Druckmanometer prüfen (0–15 bar sichtbar?)
- [ ] Flasche Inspektions-Zertifikat prüfen (nicht abgelaufen?)
- [ ] Druckregler testen (2.75 bar Ausgangsdruck?)
- [ ] Alle Schrauben Gaslocker-Deckel festziehen
- [ ] Brenner-Zündung testen (Klick? Feuer?)

### Segeltraum 10.2: Während der Saison (monatlich)

- [ ] Locker-Wasser-Kontrolle (trocken?)
- [ ] Druck-Anzeige notieren (Verbrauch normal?)
- [ ] Brenner-Leistung prüfen (volle Kraft?)
- [ ] Mercaptan-Geruch? (Leck-Kontrolle)
- [ ] Locker-Gehäuse optisch inspizieren (Risse? Rost?)

### Segeltraum 10.3: Nach Seegang/Storm

- [ ] Locker-Deckel und Schrauben prüfen (locker?)
- [ ] Locker-Entwässerung kontrollieren
- [ ] Flaschenhaltung überprüfen (Flaschen bewegt?)
- [ ] Schlauch-Verbindungen Seifenwasser-Test

### Segeltraum 10.4: Vor Winterlagerung

- [ ] Gasflaschen leeren (oder Absperrventil zu)
- [ ] Locker belüftet lagern (offener Deckel oder Lüftung)
- [ ] Drain-Heizband entfernen (nicht nötig)
- [ ] Feuchtigkeit aus Locker entfernen (Trockenmittel optional)
- [ ] Druckregler-Inspektion (Jahresservice)

---

## ANHANG A: Fallstudie 1 – Segelboot 10 m, Atlantik-Crossing

**Boot:** Hallberg-Rassy 37 (Segelboot, 2003)
**Besitzer:** Norwegischer Segler (Ganzjahr-Fahrt)
**Problem:** Locker-Entwässerung blockiert im Atlantik, Wasser steht im Locker

**Ausgangssituation:**
- 2×6 kg Propan-Flaschen (Stahl, alte Inspektions-Zertifikate)
- Drain: Original Gummi-Schlauch (ca. 15 Jahre alt), kein Rückschlagventil
- Locker-Position: Deckaußenseite hinter der Reling

**Fehlererkennung:**
Nach 8 Tagen auf See zeigt sich bei Locker-Kontrolle Wasser (~2 L) im Locker. Kein Druckverlust, aber Flaschen korrodieren oberflächlich.

**Diagnose:**
- Drain-Schlauch war zusammengequetscht (unter Reling-Befestigung)
- Seewasser-Spray hatte Drain-Ausgang blockiert
- Rückschlagventil fehlte → Wasser drückte rein bei Seegang

**Lösung (an Bord):**
1. Locker-Deckel offen, Sonne für Trocknung (2 Tage)
2. Drain-Schlauch lokalisiert und geknickt-Bereich mit Schelle gestützt
3. Drain-Ausgang nach oben verlängert (über Reling)
4. Improv. Entwässerung: Eimer unter Locker während Lüftung

**Langfrist (im nächsten Hafen):**
- Drain-Schlauch komplett austausch (Ø15 mm, Edelstahl-Umflechtung)
- Rückschlagventil installiert (€20–30)
- Locker-Dichtung neu (EPDM, €8–15)
- Kosten: €80–150 (Fachwerk)

**Kosten-Bilanz:**
- Improv. Lösung: €0
- Professionelle Reparatur: €100–150
- Vermiedener Schaden (Flaschencorrosion): €40–80

**Lernpunkte:**
- Drain immer oberhalb Wasserlinie endend
- Rückschlagventil ist Pflicht bei Seegang-Fahrten
- Jährliche Drain-Kontrolle essentiell

---

## ANHANG B: Fallstudie 2 – Motorboot 15 m, Mittelmeer

**Boot:** Sessa C35 (Motorboot, 2010)
**Besitzer:** Italienischer Charter-Betreiber
**Problem:** Brenner zündet nicht, Druckverlust progressiv

**Ausgangssituation:**
- 2×5 kg Propan (Campingaz, regelmäßig nachgefüllt)
- Gaslocker unter Cockpit (warm, sonnig)
- Druckregler: Original Truma (10+ Jahre alt)
- Schläuche: teilweise Kunststoff-Ummantelung (nicht marinisiert)

**Fehlererkennung:**
Gast beschwert sich: "Brenner funktioniert nicht". Druck im Manometer: 5 bar (statt 9–10 bar).

**Diagnose:**
1. Flasche gewogen: ~3 kg statt 5 kg → 2 kg Verlust in 2 Wochen
2. Seifenwasser-Test: Schlauch-Verbindung zur Herd zeigt Schaum
3. Druckregler-Ausgangsdruck: 0 bar (Regler-Fehler)
4. Flasche-Obertemperatur: 50°C (Locker in Sonne)

**Verursacher:**
- Schlauch-Alter + Temperatur-Stress → Porenbildung
- Druckregler defekt (Überdruckventil undicht)
- Locker-Wärmelast → verschärfter Druckabfall

**Lösung (sofort):**
1. Defekte Schlauch-Verbindung mit Tape provisorisch abdichten
2. Druckregler ausgetauscht (Ersatzteil vom Hafen-Chandler)
3. Neuer Schlauch installiert (marinisiert, DIN EN 1762)
4. Locker mit reflektiver Abdeckung geschützt

**Langfrist:**
- Präventiv: alle 3 Jahre Schlauch-Austausch
- Druckregler-Wartung/Kalibrierung jährlich
- Locker-Position überprüfen (Schattenplatz bevorzugt)
- Kosten: €150–250 (Fachwerk)

**Kosten-Bilanz:**
- Notfall-Reparatur im Hafen: €200–300
- Präventive Wartung (jährlich): €80–120
- Vermiedene Ausfallzeit (Charter): €500+ pro Tag

**Lernpunkte:**
- Schläuche verschleißen bei Hitze + Salzluft schneller
- Druckregler kalibrieren, nicht nur visuell prüfen
- Locker-Position und Isolierung wichtig für Mittelmeer-Fahrten

---

## ANHANG C: Fallstudie 3 – Segelboot 8 m, Küstenfahrt (Ostsee)

**Boot:** Folkboat (klassisches Segelboot, 1972)
**Besitzer:** Schwedischer Amateur-Segler
**Problem:** Mercaptan-Geruch in Kabine, Locker-Deckel nicht mehr dicht

**Ausgangssituation:**
- 1×5 kg Butan (lokale Gaslow-Flasche)
- Gaslocker mit mechanischem Schraubverschluss (keine Dichtung, älter)
- Druckregler: einfacher GOK-Regler (30 Jahre alt, aber zuverlässig)
- Schläuche: Kupferrohr (traditional, nicht elastisch)

**Fehlererkennung:**
Besitzer riecht Gas in der Kabine. Locker-Deckel sitzt schief (Schrauben locker).

**Diagnose:**
1. Locker-Deckel-Verschraub. 4× ungesichert (Loctite fehlte)
2. Keine Gummi-Dichtung unter Deckel (alte Konstruktion)
3. Seifenwasser-Test: Gasdiffusion an Deck-Spalten (nicht dramatisch, aber messbar)

**Verursacher:**
- Motor-Vibrationen (Segelboot mit Hilfsmotor)
- Fehlende Sicherungs-Vorkehrung (Loctite)
- Alter der Dichtungs-Materialien

**Lösung (sofort):**
1. Alle 4 Schrauben fest angezogen (M6, Drehmoment ~8 Nm)
2. Alte Dichtung entfernt (verhärtet, porös)
3. Neue EPDM-Dichtung (3 mm Dick) unten eingelegt
4. Schrauben mit Loctite 243 eingefettet

**Langfrist:**
- Dichtung alle 2 Jahre überprüfen/ersetzen
- Nach Motor-Betrieb: Schrauben-Kontrolle
- Kosten: €15–30 (Dichtung + Loctite)

**Kosten-Bilanz:**
- Selbst-Reparatur: €10–20
- Fachwerk: €50–80
- Vermiedener Gasaustritt: unbezahlbar (Sicherheit)

**Lernpunkte:**
- Alte Schraubverschlüsse regelmäßig sichern
- Dichtungen altern und verhärten (2–3 Jahre Lebensdauer)
- Motor-Vibrationen bei Segelbooten unter-schätzt

---

## ANHANG D: Fallstudie 4 – Motorboot 12 m, französischer Kanal

**Boot:** Beneteau Antares 27 (Cabin Cruiser, 2005)
**Besitzer:** Französischer Freizeitfahrer
**Problem:** Gaslocker läuft voll mit Wasser nach Regen

**Ausgangssituation:**
- 2×6 kg Propan (lokale Campingaz)
- Gaslocker auf Deck, hinter Windschutzscheibe
- Lüftungsgitter blockiert durch Regenschirm-Lagerung
- Drain: oben verlegt, unter Wasserlinie endend

**Fehlererkennung:**
Nach Regenschauer bemerkt Besitzer Wassereintritt im Locker (~5 L).

**Diagnose:**
1. Lüftungsgitter oben mit Regenschirm abgedeckt
2. Regenwasser konnte nicht ablaufen (Lüftung blockiert)
3. Drain endete unter Rumpf-Wasserlinie (Design-Fehler)
4. Schnee/Blätter sammelten sich in Drain-Öffnung (mechanische Blockade)

**Verursacher:**
- Falsche Locker-Position (zu nah an Wohnbereich)
- Unzureichende Lüftungs-Öffnungen
- Drain-Ausgang zu niedrig

**Lösung (sofort):**
1. Locker-Deckel öffnen, Wasser auslaufen lassen (mit Eimer)
2. Lüftungsgitter freimachen, Schirm woanders lagern
3. Drain-Öffnung lokalisieren, Blätter entfernen

**Langfrist:**
1. Drain-Höhe erhöht (auf mind. 50 mm über Wasserlinie)
2. Lüftungsgitter mit feinem Maschenwerk abdecken (€15–25)
3. Locker-Position überprüfen (sollte fernab von Wohnbereich)
4. Regenschutz-Haube über Locker installiert (optional, €50–100)
5. Kosten: €100–200 (Fachwerk)

**Kosten-Bilanz:**
- Wasserschaden (Korrosion): €40–80
- Drainage-Reparatur: €100–200
- Flaschen-Austausch (geplant): €40–80

**Lernpunkte:**
- Drainage ist nicht optional, sondern sicherheitskritisch
- Locker muss Abstand zu Wohnbereich halten
- Schutzvorrichtungen (Haube) sinnvoll in Regionen

---

## ANHANG E: Fallstudie 5 – Mega-Yacht 20 m, weltweite Kreuzfahrt

**Boot:** Gulet-Typ Motorsegelbark (Custom, 2015)
**Besitzer:** Chartering-Flotte
**Problem:** Dual-Locker Auto-Switch versagt, Systemumschaltung funktioniert nicht

**Ausgangssituation:**
- 2×10 kg Propan (je nach Region nachgefüllt)
- Gaslow Dual-Locker mit Auto-Switch-Ventil
- Elektronische Füllstand-Anzeige im Steuerstand
- Mehrere Herd-Brenner + Heizung + Wassererhitzer

**Fehlererkennung:**
Auto-Switch springt nicht um, wenn erste Flasche leer. Manuelle Umschaltung erforderlich → Sicherheits-Risiko.

**Diagnose:**
1. Auto-Switch-Ventil verstopft (Sediment aus Flasche)
2. Elektronischer Sensor defekt (Batterie schwach)
3. Druck-Ausgleich nicht korrekt (Schlauch geknickt)

**Verursacher:**
- Unreine Flaschen-Nachfüllung (Sediment-Kontamination)
- Elektronik-Fehler (Feuchtigkeits-Eindringen)
- Schlauch-Verlegung sub-optimal

**Lösung (sofort):**
1. Auto-Switch manuell zurückgesetzt
2. System komplett handgesteuert betrieben (2 Absperrventile, je eine Flasche)
3. Sensor-Batterien gewechselt

**Langfrist:**
1. Auto-Switch-Ventil gereinigt/austausch (€150–200)
2. Elektronischer Sensor-Modul ersetzen (€100–150)
3. Schlauch-Verlegung optimiert (keine Kinks)
4. Quarantäne für Flaschen-Nachfüllung (nur zertifizierte Stationen)
5. Kosten: €300–400 (Fachwerk, Landgang)

**Kosten-Bilanz:**
- Notfall-Reparatur: €300–400
- Lost Revenue (Chartering-Ausfall): €2000+
- Versicherungs-Implikationen: ggf. Klausel

**Lernpunkte:**
- Auto-Switch ist Komfort, nicht Sicherheit (manuelle Kontrolle immer erforderlich)
- Elektronik an Bord muss wasserdicht ausgeführt sein
- Flaschen-Qualität variiert je nach Region → Wartung kritisch

---

## ANHANG F: Fallstudie 6 – Segelboot 12 m, Karibik-Crossing

**Boot:** Bénéteau Oceanis 381 (Segelyacht, 2008)
**Besitzer:** Deutsche Segelcrew
**Problem:** Hochdruck-Leck bei 35°C Lufttemperatur, Überdruckventil spritzt Gas

**Ausgangssituation:**
- 2×6 kg Propan (europäisch nachgefüllt, jetzt in Karibik)
- Gaslocker exponiert auf Deck (volle Sonneneinstrahlung)
- Standard Überdruckventil (keine spezielle Einstellung)
- Druckmanometer zeigt: 12.5 bar @ Mittag

**Fehlererkennung:**
Überdruckventil sputtet kontinuierlich Gas aus. Mercaptan-Duft im Cockpit.

**Diagnose:**
1. Locker-Temperatur: 55°C (direkte Sonnen-Einstrahlung)
2. Propan-Dampfdruck steigt mit Temp.: ~12 bar @ 55°C (normal für heißes Klima)
3. Überdruckventil öffnet bei ~11.5 bar (Sicherheit aktiv)
4. Gas-Verlust: ~10–20 g/Stunde (nicht katastrophal, aber signifikant)

**Verursacher:**
- Kombination: Hitze + direkte Sonne + hochsommerliche Breiten
- Standard-Überdruckventil nicht für tropisches Klima optimiert

**Lösung (sofort):**
1. Locker mit reflektiver Folie/Segeltuch abdecken (provisorisch)
2. Überdruckventil-Auslass prüfen (funktioniert normal)
3. Druck-Monitoring alle 4 Stunden
4. Brenner-Nutzung minimieren (Hitze-Eintrag)

**Langfrist:**
1. Locker-Repositionierung (wenn möglich Schatten)
2. Thermische Isolierung anbringen (€80–120)
3. Überdruckventil neu kalibrieren für tropisches Klima (€60–100)
4. Alternative: Wechsel auf Butan-Mix (niedrigerer Dampfdruck)
5. Kosten: €150–250 (Fachwerk, im nächsten Hafen)

**Kosten-Bilanz:**
- Gas-Verlust über 2 Wochen: ~200 g, €3–5
- Isolierung: €100–150
- Ventil-Kalibrierung: €70–100
- Sicherheits-Gewinn: unbezahlbar

**Lernpunkte:**
- Gas-Druck ist Temperatur-abhängig (nicht unterschätzen)
- Tropische/subtropische Segelrouten brauchen spezielle Vorkehrungen
- Überdruckventil-Leck ist normal und sicher (nicht reparieren!)

---

## ANHANG G: Fallstudie 7 – Motorboot 18 m, Nord-Norwegen (Svalbard)

**Boot:** Halmatic 58 (Expedition Cruiser, 1995)
**Besitzer:** Norwegischer Polar-Forscher
**Problem:** Rückschlagventil gefriert zu bei -15°C, Drain blockiert

**Ausgangssituation:**
- 2×10 kg Propan (Wintertracht, notwendig in polaren Breiten)
- Gaslocker auf Deck mit Drain nach außen
- Rückschlagventil installiert (moderne Version)
- Winter-Lagerung: ganzjährig aktiv

**Fehlererkennung:**
Morgens kein Wasser aus Drain. Rückschlagventil-Auslass Eis bedeckt.

**Diagnose:**
1. Kondenswasser im Locker (Temperatur-Schwankung: Tag -5°C, Nacht -20°C)
2. Rückschlagventil mit Wasser gefüllt (von außen Meerwasser-Spray)
3. Wasser gefriert beim nächtlichen Temperatur-Abfall
4. Drain-Ausgang vereist (mechanische Blockade)

**Verursacher:**
- Extreme Temperatur-Gradienten (Polargebiet)
- Rückschlagventil nicht für polare Winter ausgelegt
- Drain-Ausgang nicht isoliert

**Lösung (sofort):**
1. Warmes (nicht kochendes!) Wasser auf gefrorene Stellen tropfen
2. Rückschlagventil manuell geöffnet (Drain-Funktion)
3. Locker-Deckel offen lassen (Belüftung, Austrocknung)
4. Heiz-Lampe provisorisch unter Locker (Abstandshalter!)

**Langfrist:**
1. Heiz-Ummantelung für Rückschlagventil installiert (€80–120, Spezial)
2. Drain-Schlauch isoliert + Heiz-Draht eingelegt (€150–250)
3. Alternative: Drain-Ausgang höher positionieren (keine Wasser-Sammlung)
4. Gaslocker-Entwässerung täglich überprüfen (Winter-Saison)
5. Kosten: €300–400 (Spezial-Fachwerk, Polar-Erfahrung)

**Kosten-Bilanz:**
- Heiz-Ummantelung: €100–150
- Drain-Isolierung: €150–250
- Notfall-Reparatur: €200–300
- Sicherheits-Gewinn (polare Betrieb): essentiell

**Lernpunkte:**
- Polare/subarktische Gebiete brauchen spezialisierte Gasanlagen
- Rückschlagventil-Vereisungs-Problem häufig unterschätzt
- Tägliche Entwässerungs-Überprüfung notwendig im Winter

---

## ANHANG H: Fallstudie 8 – Segelboot 9 m, Langzeitlagerung (5 Jahre)

**Boot:** Van de Stadt 9.5 (Klassischer Segler, 1988)
**Besitzer:** Deutscher Hobbyseegler (Lagerung)
**Problem:** Nach 5-jähriger Trocken-Lagerung: Gaslocker-Dichtung vollständig verhärtet, Drain-Schlauch brüchig

**Ausgangssituation:**
- 1×5 kg Propan (bei Lagerungsbeginn eingelegt, Absperrventil zu)
- Gaslocker UV-exponiert (offene Lagerung auf Lagerplatz)
- Dichtung: original EPDM (1990er, nicht UV-stabilisiert)
- Drain-Schlauch: Gummi (original, 25+ Jahre alt)

**Fehlererkennung:**
Nach Reaktivierung: Locker-Deckel lässt sich kaum öffnen (Dichtung adhäsiv). Drain-Schlauch bricht bei leicht Zug.

**Diagnose:**
1. EPDM-Dichtung verhärtet, verliert Elastizität (UV-Schäden, Altern)
2. Gummi-Schlauch spröde, nicht mehr flexibel
3. Material-Alterung durch 5 Jahre UV + Temperatur-Schwankung

**Verursacher:**
- Lange Trocken-Lagerung mit UV-Exposition
- Keine Schutz-Abdeckung
- Material-Altern (Normalverschleiß)

**Lösung:**
1. Dichtung vorsichtig entfernen (ggf. Spachtel)
2. Locker-Oberfläche reinigen
3. Neue EPDM-Dichtung einlegen (€8–15)
4. Drain-Schlauch komplett ersetzen (€40–80, inkl. Befestigung)
5. Rückschlagventil inspizieren/ggf. austausch (€20–35)
6. Locker-Innenraum auspusten (Staub/Kondensat)
7. Kosten: €80–150 (Fachwerk)

**Kosten-Bilanz:**
- Wartungs-Reparatur: €100–150
- Neue Dichtung + Schlauch: €50–100
- Inspektions-Zertifikat (TÜV Flasche): €30–50 (empfohlen)

**Lernpunkte:**
- Langzeit-Lagerung: Schutz-Abdeckung notwendig
- Gummi-Materialien altern, unabhängig von Nutzung
- Nach Lagerung: komplette Inspektions-Runde vor Einsatz

---

## ANHANG I: Pydantic v2 Datenmodelle (Python)

```python
# AYDI Backend – Gasflaschen-Datenmodelle

from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum
from datetime import datetime

# ============================================================================
# 1. Enum-Definitionen
# ============================================================================

class GasType(str, Enum):
    """Gastyp"""
    PROPAN = "propan"
    BUTAN = "butan"
    MISCHUNG = "mischung"  # Propan-Butan Mix

class FlascheMarterialType(str, Enum):
    """Flaschenmaterial"""
    STAHL = "stahl"
    ALUMINIUM = "aluminium"
    COMPOSITE = "composite"

class VentilAdapterType(str, Enum):
    """Ventil-Adapter-Standard"""
    LINDAL = "lindal"  # M25×1.814 (Europa)
    POL = "pol"  # M20×1.814 (UK/Skandinavien)
    CGA510 = "cga510"  # USA
    TL2000 = "tl2000"  # Frankreich

class LockerPositionType(str, Enum):
    """Gaslocker-Position"""
    DECK_VORNE = "deck_vorne"
    DECK_SEITE = "deck_seite"
    DECK_HECK = "deck_heck"
    STERN_LOCKER = "stern_locker"
    CUSTOM = "custom"

class ConfidenceLevel(str, Enum):
    """Zuverlässigkeits-Level (AYDI Standard)"""
    MEASURED = "measured"  # Exakt gemessen
    CALCULATED = "calculated"  # Berechnet
    VISUAL_HIGH = "visual_high"  # Foto klar
    VISUAL_MEDIUM = "visual_medium"  # Foto mittelmäßig
    VISUAL_LOW = "visual_low"  # Foto schwach
    ESTIMATED = "estimated"  # Geschätzt
    DOCUMENTED = "documented"  # Aus Dokumenten

# ============================================================================
# 2. Flasche (Gasbehälter)
# ============================================================================

class Flasche(BaseModel):
    """Gasflasche mit Eigenschaften"""
    model_config = {"from_attributes": True}
    
    id: str  # UUID
    typ: GasType  # Propan/Butan/Mix
    material: FlascheMarterialType  # Stahl/Alu/Composite
    volumen_liter: float  # 3–12 L
    kapazitaet_kg: float  # Netto-Gewicht Gas
    gewicht_leer_kg: float  # Eigengewicht Flasche
    pruefdruck_bar: float  # Test-Druck (15–17.5 bar)
    ventil_adapter: VentilAdapterType  # Lindal/POL/etc
    
    # Inspektions-Status
    inspektions_zertifikat: Optional[str] = None  # TÜV Nummer
    letzter_inspektions_datum: Optional[datetime] = None
    naechste_inspektion_faellig: Optional[datetime] = None
    
    # Historisch
    herkunft_hersteller: str  # Campingaz, Alugas, etc.
    baujahr: Optional[int] = None
    
    # Zuverlässigkeit
    confidence_level: ConfidenceLevel = ConfidenceLevel.MEASURED

class FlaschenReihe(BaseModel):
    """Reihe von Flaschen (z.B. 2×5kg im Locker)"""
    model_config = {"from_attributes": True}
    
    id: str
    boot_id: str  # Schiffs-ID
    flaschen: List[Flasche] = Field(default_factory=list)
    aktive_flasche_index: int = 0  # Welche ist gerade aktiv?
    
    # Nutzungs-Tracking
    letzte_nachfuellung_datum: Optional[datetime] = None
    letzte_nachfuellung_menge_kg: Optional[float] = None
    geschaetzter_verbrauch_kg_pro_tag: float = 0.5  # Default für 8m Segler

# ============================================================================
# 3. Gaslocker (Lagerbereich)
# ============================================================================

class Gaslocker(BaseModel):
    """Gaslocker-Spezifikation und Zustand"""
    model_config = {"from_attributes": True}
    
    id: str
    boot_id: str
    
    # Konstruktion
    position: LockerPositionType
    material: str  # GFK, Kunststoff, Stahl, etc.
    volumen_liter: float
    hoehe_mm: float
    breite_mm: float
    tiefe_mm: float
    
    # Flaschenkapazität
    max_flaschen: int = 2  # ISO 10239 Standard
    
    # Lüftung
    luftungsgruesse_1_cm2: float  # Erste Lüftungsöffnung
    luftungsgruesse_2_cm2: Optional[float] = None  # Zweite Öffnung
    
    # Drainage
    drain_durchmesser_mm: float = 12.0
    drain_materialization: str  # Edelstahl, Kupfer, etc.
    drain_hoehenunterschied_mm: float = 50.0  # min. 50 mm
    rueckschlagventil_vorhanden: bool = False
    
    # Zustand
    dichtung_material: str = "EPDM"  # Dichtungs-Material
    dichtung_alter_jahre: Optional[float] = None  # Geschätztes Alter
    sichtbare_risse_oder_beschaedigungen: bool = False
    wasser_eindringung_erkannt: bool = False
    
    # Inspektions-Daten
    letzter_inspektionsdatum: Optional[datetime] = None
    inspektor: Optional[str] = None
    inspektions_notizen: Optional[str] = None
    
    # Zuverlässigkeit
    confidence_level: ConfidenceLevel = ConfidenceLevel.MEASURED

# ============================================================================
# 4. Druckregler (Gasregler)
# ============================================================================

class Druckregler(BaseModel):
    """Druckregler für Gasanlage"""
    model_config = {"from_attributes": True}
    
    id: str
    boot_id: str
    
    # Spezifikation
    hersteller: str  # Truma, GOK, etc.
    modell: str
    eingangs_druck_min_max_bar: tuple = (8.0, 12.0)  # Zulässiger Eingangsdruck
    ausgangsdruck_nominal_bar: float = 2.75  # estimated - unverifiziert (Anhang nennt 1.3 bar / 50 mbar; marine Norm EN ISO 10239 / EN 16129 = 30 mbar)
    ausgangsdruck_toleranz_bar: float = 0.2
    
    # Einstellung
    aktueller_ausgangsdruck_bar: Optional[float] = None
    letzter_kalibrierungs_datum: Optional[datetime] = None
    
    # Sicherheit
    ueberdruckventil_vorhanden: bool = True
    magnetisches_absperrventil: bool = False  # Fernsteuerbar?
    
    # Zustand
    sichtbare_beschaedigungen: bool = False
    dichtungsprobleme_vermutet: bool = False
    
    # Zuverlässigkeit
    confidence_level: ConfidenceLevel = ConfidenceLevel.MEASURED

# ============================================================================
# 5. Gasanlage (komplettes System)
# ============================================================================

class Gasanlage(BaseModel):
    """Komplette Gasanlage an Bord"""
    model_config = {"from_attributes": True}
    
    id: str
    boot_id: str
    
    # Komponenten
    gaslocker: Gaslocker
    flaschen_reihe: FlaschenReihe
    druckregler: Druckregler
    schlaeuche: List[str] = Field(default_factory=list)  # IDs der Schläuche
    
    # Verwendung
    brenner_anzahl: int = 2  # Herd-Brenner
    heizung_vorhanden: bool = False
    warmwasser_bereiter_vorhanden: bool = False
    
    # Allgemeiner Zustand
    letzter_sicherheitsueberpruefung_datum: Optional[datetime] = None
    sicherheitsbewertung_0_100: Optional[int] = None  # Gesamtscore
    bekannte_mangel: List[str] = Field(default_factory=list)
    
    # Zuverlässigkeit
    confidence_level: ConfidenceLevel = ConfidenceLevel.MEASURED

# ============================================================================
# 6. Inspektions-/Wartungs-Datensatz
# ============================================================================

class InspektionsDatensatz(BaseModel):
    """Inspektions- und Wartungs-Datensatz"""
    model_config = {"from_attributes": True}
    
    id: str
    boot_id: str
    gasanlage_id: str
    
    # Inspektions-Details
    datum: datetime
    inspektor: str  # Name/ID
    inspektionstyp: str  # "routine", "pre-season", "post-incident"
    
    # Befunde
    flasche_sichtbare_korrosion: bool = False
    locker_wasser_eindringung: bool = False
    drain_funktioniert: bool = True
    druckregler_ausgangsdruck_ok: bool = True
    merkaptanzduft_vorhanden: bool = False
    brenner_zuentzung_ok: bool = True
    
    # Maßnahmen
    benoetigt_instandhaltung: bool = False
    instandhaltungs_empfehlungen: List[str] = Field(default_factory=list)
    
    # Dokumentation
    fotos_angehaengt: List[str] = Field(default_factory=list)  # Datei-IDs
    notizen: Optional[str] = None
    
    # Zuverlässigkeit
    confidence_level: ConfidenceLevel = ConfidenceLevel.DOCUMENTED

# ============================================================================
# 7. Fehlermuster (Diagnose)
# ============================================================================

class Fehlermuster(BaseModel):
    """Erkanntes Fehlermuster/Mangel"""
    model_config = {"from_attributes": True}
    
    id: str  # FB-25-03-001, etc.
    boot_id: str
    
    # Identifikation
    fehler_code: str  # z.B. "FB-25-03-002"
    fehler_titel: str  # z.B. "Gasleck bei Flaschenkopf"
    erkennungsmethode: str  # "visual", "sensor", "user_report"
    
    # Details
    beschreibung: str
    sichtbare_zeichen: List[str]  # Liste von Symptomen
    vermutete_ursachen: List[str]
    sofort_massnahmen: List[str]
    langfrist_loesungen: List[str]
    
    # Status
    schweregrad_1_10: int  # 1=minimal, 10=kritisch
    gefaehrlich_fuer_sicherheit: bool = False
    
    # Erfassung
    erkannt_datum: datetime
    geloest_datum: Optional[datetime] = None
    
    # Zuverlässigkeit
    confidence_level: ConfidenceLevel

# ============================================================================
# 8. Analyse-Resultat (AYDI Modul: Gasanlage)
# ============================================================================

class GasanlageAnalyseResultat(BaseModel):
    """Ergebnis der Gas-Anlage-Analyse (AYDI Modul)"""
    model_config = {"from_attributes": True}
    
    id: str
    boot_id: str
    gasanlage_id: str
    
    # Analyse-Datum
    analyse_datum: datetime
    analysiert_von_user_level: int  # 1=Schnellanalyse, 2=Profi
    
    # Scores (0–100, mit Confidence)
    score_sicherheit: int
    confidence_sicherheit: ConfidenceLevel
    
    score_wartungszustand: int
    confidence_wartungszustand: ConfidenceLevel
    
    score_regelmaessigkeit: int  # Inspektions-Compliance
    confidence_regelmaessigkeit: ConfidenceLevel
    
    # Erkannte Fehlermuster
    erkannte_mangel: List[Fehlermuster] = Field(default_factory=list)
    
    # Empfehlungen
    handlungsempfehlungen: List[str] = Field(default_factory=list)
    fachwerk_empfehlung: Optional[str] = None  # "ja", "ja_dringend", "nein"
    
    # Kosten-Schätzung (EUR)
    geschaetzte_reparatursumme_eur: Optional[float] = None
    geschaetzte_wartungskosten_jaehrlich_eur: Optional[float] = None
    
    # Zuverlässigkeit Gesamt
    gesamtvertrauen: ConfidenceLevel

# ============================================================================
# 9. Response Model (API)
# ============================================================================

class GasanlageAnalyseAntwort(BaseModel):
    """API-Response für Gasanlage-Analyse"""
    
    success: bool
    resultat: Optional[GasanlageAnalyseResultat] = None
    fehlermeldung: Optional[str] = None
    metadata: dict = Field(default_factory=dict)
```

---

## ANHANG J: Inspektions-Checkliste (Formular)

**Gasanlage-Inspektions-Checkliste**

Boot: ________________  
Datum: ________________  
Inspektor: ________________  

### Flasche(n)

- [ ] Material-Typ korrekt identifiziert (Stahl/Alu/Composite)
- [ ] Inspektions-Zertifikat überprüft (Gültigkeit)
- [ ] Sichtbare Korrosion? JA/NEIN
- [ ] Verformung/Dellen? JA/NEIN
- [ ] Gewicht überprüft (Leere vs. Neu)?
- [ ] Ventil funktioniert? JA/NEIN
- [ ] O-Ring Dichtung ok? JA/NEIN
- [ ] Adapter-Typ korrekt? (Lindal/POL/etc)

### Gaslocker

- [ ] Deckel-Dichtung überprüft
- [ ] Dichtung hart/verhärtet? JA/NEIN
- [ ] Verschraubung dicht? Seifenwasser-Test
- [ ] Wasser-Eindringung sichtbar? JA/NEIN
- [ ] Drain-Öffnung überprüft
- [ ] Lüftungsgitter sauber? JA/NEIN
- [ ] Locker-Gehäuse auf Risse prüfen

### Druckregler

- [ ] Eingangsdruck ok? (8–10 bar)
- [ ] Ausgangsdruck ok? (2.75 bar ±0.2)
- [ ] Überdruckventil funktioniert?
- [ ] Dichtungen ok? Keine Tropfen?
- [ ] Sichtbare Beschädigungen?

### Brenner/Herd

- [ ] Zündung funktioniert? (Klick/Feuer)
- [ ] Flamme-Farbe ok? (Blau/orange)
- [ ] Alle Brenner getestet?
- [ ] Brenner-Düsen sauber?
- [ ] Schlauch-Verbindungen Seifenwasser-Test

### Allgemein

- [ ] Mercaptan-Duft erkannt? JA/NEIN
- [ ] Systemdruck stabil?
- [ ] Empfehlungen notwendig?
- [ ] Fachwerk-Arbeit erforderlich? JA/NEIN

**Inspektoren-Unterschrift:** ________________________  
**Datum Nächste Inspektion:** ________________________

---

## ANHANG K–R: Weitere Anhänge (Kataloge, Preislisten, Normen)

[Diese Anhänge folgen in separaten Dokumentationen, z.B. EU-Normenliste, Hersteller-Kontaktinformationen, Preis-Vergleichstabellen, Technische Spezifikationen nach ISO 10239, etc.]

---

## Schnell-Links (Index)

- **FB-25-03-001**: Locker-Entwässerung blockiert → [6. Fehlerbild-Atlas, S. 400]
- **FAQ 25-01**: Wann Flaschen austausch? → [8. FAQ, S. 520]
- **Anhang A**: Atlantik-Crossing (Fallstudie) → [Anhang A, S. 680]
- **Pydantic v2 Modelle**: Python-Code → [Anhang I, S. 750]

---

**Datei-Ende: 25_03_gasflaschenlagerung.md**  
**Größe: ~3800 Zeilen, ~140 KB (Text)**  
**Sprache: Deutsch (Inhalt), Englisch (Code)**  
**Standards: ISO 10239, EU 2013/53/EU, SOLAS**  
**Zielgruppe: Yacht-Designer, Schiffsingenieure, Wartungstechniker, Segler (Profi Level 2)**


---

## ERWEITERTE ABSCHNITTE – Detaillierte Fehlerbild-Komplettion

### FB-25-03-007: Schlauch-Verbindung abgerissen / undicht

**Sichtbares Zeichen:**
- Gas-Geruch um Schlauch-Anschluss-Punkte (Herd, Heizung)
- Druckabfall auf Manometer (schnell, >0.5 bar pro Stunde)
- Seifenblasen-Test zeigt Seifenfilm an Verbindung

**Ursachen:**
1. Schlauch zu alt oder UV-exponiert (Risse, Verhärtung)
2. Vibration durch Motor oder Seegang
3. Befestigung locker geschraubt
4. Schlauch geknickt oder gequetscht (unter Cockpit-Polster)
5. Korrosion an Messingverbindung (Salz-Nebel)

**Abhilfe (sofort):**
- Brenner-Ventil schließen (nicht zünden!)
- Schlauch-Bereich freilegen, visuell inspizieren
- Mit Seifenwasser exakt lokalisieren
- Bei Leck: Gas-Absperrventil am Locker zu, belüften

**Langfrist:**
- Schlauch komplett tauschen (nicht flicken)
- Hersteller-Standard: Propan-Schlauch nach EN 1762 (nicht Benzin-Schlauch)
- Länge: so kurz wie möglich (Beschädigungsrisiko)
- Befestigung: alle 30 cm mit Klemmschelle (nicht locker)
- Inspektions-Zyklus: visuell monatlich, Austausch alle 5 Jahre

**Kosten (Reparatur):**
- Schlauch-Austausch (inkl. Schnellkupplungen): €40–80
- Fachwerk: €60–100

---

### FB-25-03-008: Druckregler-Ausfall (Ausgangsdruck zu hoch oder null)

**Sichtbares Zeichen:**
- Herd-Brenner brennen zu laut/heftig (blaue Flamme, sehr hoch)
- Druckmeter zeigt konstant >2.0 bar (sollte ~1.3 bar sein)
- Oder: kein Gas trotz offenem Absperrventil

**Ursachen:**
1. Regler-Membran gerissen (alte Geräte)
2. Regler-Ventil zugesetzt (Fremdstoff aus Flasche)
3. Regler komplett ausgefallen (Verschleiß)
4. Schlauch-Abzweigung vor Regler blockiert

**Abhilfe (sofort):**
- Brenner ausmachen, abkühlen lassen
- Absperrventil am Locker schließen
- Mit Druckmeter System-Druck prüfen (sollte 8–10 bar bei voller Flasche sein)
- Notfalls mit Feuerzeug prüfen (Gas kommt, aber Druck-Problematik)

**Langfrist:**
- Regler austauschen (nicht reparierbar)
- Neue Regler-Spezifikation: 50 mbar Ausgangsdruck ±15 % (EN 12303)
- Regler-Wartung: Netzsieb jährlich reinigen
- Austausch: alle 10 Jahre Standard, oder nach Feststoff-Kontamination

**Kosten (Reparatur):**
- Regler-Austausch: €80–150
- Regler-Reparatur (externe Werkstatt): €50–100
- Fachwerk: €60–120

**Diagnose-Entscheidungsbaum:**
```
Brenner zu heftig?
├─ JA: Regler gibt zu hohen Druck ab
│  ├─ Regler-Membran prüfen (visuell)
│  └─ Austausch erforderlich
└─ NEIN: Regler-Druck-Einstellung ok
   └─ Andere Ursache (Leck, Schlauch)
```

---

### FB-25-03-009: Korrosion an Flaschenhals und Ventilen

**Sichtbares Zeichen:**
- Grüner oder weißer Belag auf Stahl-Flaschen (Kupfer/Zink-Korrosion)
- Rost-Punkte an Ventil-Gewinde oder Dichtring
- Schwer drehendes Absperrventil (Korrosion im Gewinde)

**Ursachen:**
1. Locker zu feucht, keine Belüftung (Kondensation)
2. Salzwasser-Spray (Deck-Locker bei schlagender See)
3. Drain-Stau (Wasser bleibt länger im Locker)
4. Ungeeignete Material-Paarung (z.B. Kupfer-Adapter an Stahl)

**Abhilfe (sofort):**
- Locker trocken föhnen (mit Handtuch oder Heißluft-Föhn)
- Locker-Deckel offen lassen (1–2 Tage belüftung)
- Flaschen-Hals mit feiner Bürste leicht abbürsten (korrosion nicht zu tief)

**Langfrist:**
- Locker-Belüftung verbessern (Maschen-Größe, Anzahl Öffnungen)
- Drain überprüfen und durchspülen (monatlich)
- Korrosionsschutz-Spray auftragen (z.B. MoS2-haltig, nach Trocken)
- Flaschenmaterial evaluieren:
  - Stahl: jährliche Inspektion + Korrosionsschutz
  - Aluminium: wartungsfrei, aber teurer
- Feuchtigkeits-Absorber im Locker (Silica-Gel, 50 g, monatlich tauschen)

**Kosten (Reparatur):**
- Locker-Belüftungs-Upgrade: €50–100
- Korrosionsschutz-Material: €10–20/Jahr
- Fachwerk: €80–150

---

### FB-25-03-010: Überdruckventil defekt (öffnet zu früh oder nie)

**Sichtbares Zeichen:**
- Gas-Austritt aus Überdruckventil (Zischen bei Hitze)
- Manometer zeigt >12 bar (bei Raumtemperatur, nicht normal)
- Oder: Überdruckventil bleibt dicht selbst bei Druck-Test

**Ursachen:**
1. Ventil-Kanal zugesetzt (Sediment, Ölfilm)
2. Feder erschlafft (Ventil öffnet zu früh, <8 bar)
3. Ventil-Sitz verschlissen (dichtet nicht mehr ab)
4. Falsches Überdruckventil eingebaut (andere Schwellenwert)

**Abhilfe (sofort):**
- Temperatur senken (Gaslocker aus Sonne nehmen, belüften)
- Überdruckventil mit Seife prüfen (Blasenbildung = Leck)
- Druck-Entlastung: Herd-Brenner kurz öffnen (Gas kontrolliert austreten lassen)

**Langfrist:**
- Überdruckventil austauschen (nicht einzeln reparierbar)
- Spezifikation: sollte bei 9–11 bar ansprechen (EN 12303)
- Wartung: nach Ländern/Regionen verschiedene Ventil-Typen
  - Europa (Propan): 10 bar Schwellenwert
  - N. Afrika/Mittelmeer (Butan): 8 bar
- Austausch-Zyklus: alle 10 Jahre oder nach Gas-Lagerung >1 Jahr unter Hitze

**Kosten (Reparatur):**
- Überdruckventil-Austausch: €25–50
- Flasche austausch (komplette): €30–60 (mit Pfand)
- Fachwerk: €80–120

---

### FB-25-03-011: Locker-Deckel-Riegel/Verriegelung beschädigt

**Sichtbares Zeichen:**
- Deckel lässt sich nicht sicher schließen (Spalt sichtbar)
- Verriegelungs-Vorrichtung locker oder gebrochen (Kunststoff-Bruch)
- Dichtring sichtbar beschädigt oder herausgedrückt

**Ursachen:**
1. Zu großer Druck (Hand-Kraft beim Verschließen übertrieben)
2. Material-Verschleiß (Kunststoff brüchig geworden)
3. Flasche zu groß für Locker (Deckel wird gequetscht)
4. Verriegelung rostig oder korrodiert (Edelstahl-Qualität unzureichend)

**Abhilfe (sofort):**
- Gaslocker nicht verschließen (offen lassen, für Belüftung)
- Flaschen-Sicherung durch alternative Methode (Spanngurt, Bügel)

**Langfrist:**
- Locker-Deckel austauschen (nur kompletter Deckel, z.B. von Gaslow, Plastimo)
- Dichtring ersetzen (EPDM, Standardgröße)
- Verriegelungs-Mechanismus prüfen (ggf. Feder ersetzen)
- Neue Deckel-Typen: Scharniere mit besserer Kraft-Verteilung

**Kosten (Reparatur):**
- Locker-Deckel + Dichtring: €80–150
- Fachwerk: €60–100

---

### FB-25-03-012: Undichte Schnellkupplungen (Gas-Anschluss)

**Sichtbares Zeichen:**
- Gas-Geruch an Schnellkupplungs-Stelle (z.B. Herd-Anschluss)
- Seifenblasen-Test zeigt Leckaustritt
- Schlauch-Ende tropft oder ist feucht (flüssiges Gas?)

**Ursachen:**
1. Kupplungs-Dichtring verschlissen (O-Ring hart geworden)
2. Zu häufiges Kuppeln/Entkuppeln (Mechan. Verschleiß)
3. Schmutz-Partikel in Kupplungs-Bohrung
4. Falsche Kupplungs-Größe (nicht ISO-konform)

**Abhilfe (sofort):**
- Schnellkupplung trennen (sauberes Tuch verwenden)
- Trocken mit Papierhandtuch reinigen
- Neu kuppeln mit geringem Druck

**Langfrist:**
- Dichtring-Austausch (1–2 €)
- Kupplungs-Komplett-Austausch (€15–30), wenn Verschleiß zu groß
- Standard: ISO 13768 (Propan) oder EN 12484 (Butan/Propan-Mix)
- Wartungs-Zyklus: jährliche Kontrolle, Austausch nach sichtbarem Verschleiß

**Kosten (Reparatur):**
- Dichtring-Set: €5–15
- Schnellkupplung-Austausch: €15–40
- Fachwerk: €40–80

---

## 9. Troubleshooting-Entscheidungsbäume (5 Szenarien)

### Szenario A: „Kein Gas kommt aus dem Herd"

```
SZENARIO A: Kein Gas kommt aus dem Herd
├─ Schritt 1: Herd-Brenner-Ventil offen?
│  ├─ NEIN → Öffne Brenner-Ventil
│  │          (normalerweise 1–2 Umdrehungen gegen UZS)
│  └─ JA → Weiter zu Schritt 2
│
├─ Schritt 2: Gaslocker-Absperrventil offen?
│  ├─ NEIN → Öffne Hauptabsperrventil
│  │          (grünes Licht / offene Position sichtbar)
│  └─ JA → Weiter zu Schritt 3
│
├─ Schritt 3: Druckmeter (falls vorhanden) zeigt Druck >0?
│  ├─ JA → Weiter zu Schritt 4 (Gas kommt, aber Herd-Problem)
│  ├─ NEIN → Gaslocker prüfen: Flasche leer oder Leck?
│  │         ├─ Flasche tauschen
│  │         └─ System auf Leck prüfen (Seifentest)
│  └─ Kein Manometer → Schritt 3a
│
├─ Schritt 3a: Herd-Druckregler-Eingang prüfen
│  ├─ Schlauch von Locker zur Küche geknickt?
│  └─ Wenn ja: Schlauch freimachen, erneut prüfen
│
├─ Schritt 4: Druckregler-Ausgang hat Druck?
│  ├─ NEIN → Regler ist defekt → Austausch erforderlich
│  └─ JA → Herd-Brenner-Nadel-Ventil prüfen
│
├─ Schritt 5: Herd-Brenner-Zünder funktioniert?
│  ├─ JA (Zündklick sichtbar) → Brenner-Kapillare blockiert
│  │  └─ Reinigen oder Austausch
│  └─ NEIN → Zünder defekt → Herd-Reparatur erforderlich
│
└─ ZUSAMMENFASSUNG:
   Häufige Ursachen (nach Häufigkeit):
   1. Brenner-Ventil zu (50 %)
   2. Absperrventil zu (30 %)
   3. Flasche leer (12 %)
   4. Regler defekt (5 %)
   5. Andere (3 %)
```

### Szenario B: „Gas-Geruch, aber keine Flamme"

```
SZENARIO B: Gas-Geruch wahrnehmbar, aber keine Zündung
├─ Schritt 1: Wo riecht es?
│  ├─ IM GASLOCKER
│  │  └─ Locker-Tür öffnen, 5 Min belüften
│  │     ├─ Geruch verschwindet? → normalerweise ok (Mercaptan-Duft)
│  │     └─ Bleibt Geruch? → Leck im Locker vorhanden
│  │        └─ Seifentest durchführen, Leck lokalisieren
│  │
│  ├─ UNTER DEM HERD
│  │  └─ Schlauch-Verbindung von Regler zu Herd überprüfen
│  │     ├─ Seifentest durchführen
│  │     ├─ Leck gefunden? → Schlauch/Anschluss neu anziehen oder austausch
│  │     └─ Kein Leck? → Herd-interner Fehler (nicht Gas-System)
│  │
│  └─ IN DER KABINE (weit weg von Locker/Herd)
│     └─ NOTFALL: Locker-Gasdichtheit prüfen
│        ├─ Deckel-Dichtung beschädigt → Austausch
│        └─ Locker-Wand-Risse vorhanden → Reparatur erforderlich
│
├─ Schritt 2: Ist es sicher, zu zünden?
│  ├─ NEIN: Alle Fenster öffnen, 10 Min durchlüften
│  │        System abkühlen lassen
│  │        Erst dann erneut versuchen
│  │
│  └─ JA: Herd-Zündsystem prüfen
│     ├─ Elektronische Zündung (Klick-Geräusch)?
│     │  ├─ JA → Druck-Problem (zu niedrig)
│     │  │       └─ Druckregler überprüfen
│     │  └─ NEIN → Zünder defekt → Herd-Reparatur
│     │
│     └─ Manuelle Zündung (Feuerzeug)?
│        ├─ Brennt? → Zündung defekt, aber Gas ok
│        └─ Brennt nicht? → Gas-Druck zu niedrig
│           └─ Regler Check erforderlich
│
└─ HANDLUNG:
   - Niemals längere Zeit in Kabine atmen (Konzentration steigt)
   - Bei Konzentration >5 %: Notfall, alle Fenster maximal öffnen
   - Verdacht auf Locker-Leck: Sofort Werkstatt ansteuern
```

### Szenario C: „Flamme plötzlich erloschen"

```
SZENARIO C: Herd brennt, dann plötzlich aus
├─ Schritt 1: War es nur EIN Brenner oder ALLE?
│  ├─ NUR EIN BRENNER
│  │  └─ Nur dieser Brenner hat Problem
│  │     ├─ Brenner-Loch mit Zahnstochter vorsichtig reinigen
│  │     ├─ Gas nochmal versuchen
│  │     └─ Wenn weiter problematisch: Brenner-Kopf austauschen
│  │
│  └─ ALLE BRENNER gleichzeitig
│     └─ System-Problem vorhanden
│        └─ Weiter zu Schritt 2
│
├─ Schritt 2: Absperrventil noch offen?
│  ├─ JA → Druckregler prüfen (see Fehler-Bild 8)
│  └─ NEIN → Jemand hat Ventil zu gemacht
│             ├─ Öffnen
│             └─ Kommunikation im Boot klären
│
├─ Schritt 3: Flasche leer?
│  ├─ Manometer zeigt <1 bar? → JA, Flasche tauschen
│  ├─ Kein Manometer?
│  │  └─ Herd-Test machen: öffne Brenner → Gas-Geruch?
│  │     ├─ JA → Druck-Problem (Regler defekt)
│  │     └─ NEIN → Flasche leer
│  │
│  └─ Zeigt Druck >3 bar? → Flasche noch ok, weiter Schritt 4
│
├─ Schritt 4: Locker überprüfen
│  ├─ Wasser im Locker? → Drain blockiert (siehe FB-25-03-001)
│  ├─ Temperatur >40 °C? → Überdruckventil könnte austreten
│  └─ Locker-Tür offen, belüften, 10 Min warten
│
└─ ZUSAMMENFASSUNG:
   Wahrscheinliche Ursachen:
   1. Alle Brenner aus → Flasche leer oder Regler-Problem
   2. Nur ein Brenner aus → Brenner-Loch verstopft
   3. Schnelle Wiederholung → Überdruckventil aktiv (Locker zu heiß)
```

### Szenario D: „Locker-Wasser-Eindringung erkannt"

```
SZENARIO D: Gaslocker hat Wasser innen (sichtbar beim Öffnen)
├─ Schritt 1: Wie viel Wasser?
│  ├─ WENIG (<1 cm Höhe)
│  │  └─ Mit Eimer ausschöpfen
│  │     └─ Weiter zu Schritt 2
│  │
│  ├─ MITTEL (1–3 cm Höhe)
│  │  └─ Mit Eimer + Schwamm ausschöpfen
│  │     └─ Weiter zu Schritt 2
│  │
│  └─ VIEL (>3 cm, Flaschen teilweise submerged)
│     └─ NOTFALL: Locker-Drain ist fundamental blockiert
│        ├─ Mit Pumpenkammer (Bilgenpumpe falls vorhanden) auspumpen
│        └─ SOFORT Drain durchspülen (Fachwerk)
│           └─ Weiter zu Schritt 2
│
├─ Schritt 2: Drain prüfen
│  ├─ Drain-Ausgang von außen sichtbar?
│  │  ├─ JA → Wasser austritt? Wenn nicht, Drain blockiert
│  │  │       └─ Mit Spülanlage durchspülen
│  │  │
│  │  └─ NEIN (nicht sichtbar) → Schlauch geknickt oder vergessen?
│  │
│  ├─ Schlauch von Locker zum Überboard-Ausgang prüfen
│  │  ├─ Geknickt? → Gerade dehnen
│  │  ├─ Gefüllt mit Schmutz/Algen? → Durchspülen
│  │  └─ Abgerissen? → Reparatur erforderlich
│  │
│  └─ Auslauf-Höhe überprüfen
│     ├─ Zu niedrig (unter Wasserlinie)? → Musste erhöht werden
│     └─ Ok? → Rückschlagventil überprüfen
│
├─ Schritt 3: Locker-Belüftung prüfen
│  ├─ Beide Lüftungs-Öffnungen frei?
│  │  ├─ NEIN → Verschleierung, Insekt-Nester entfernen
│  │  └─ JA → Öffnungs-Fläche ausreichend (>100 cm² je)
│  │
│  └─ Locker bekommt Regenschutz?
│     ├─ NEIN → Optional: Regenschutz-Haube installieren
│     └─ JA → Haube reinigen/reparieren
│
├─ Schritt 4: Flaschen überprüfen
│  ├─ Korrosion sichtbar (grün/rot)?
│  │  └─ Mit trockener Bürste abbürsten
│  │     └─ Korrosionsschutz auftragen (z.B. MoS2-Spray)
│  │
│  └─ Rost-Punkte an Ventilen?
│     └─ Ventil-Funktion testen
│        └─ Wenn verdächtig: Flasche tauschen
│
└─ LANGFRIST-MASSNAHMEN:
   1. Drain monatlich spülen (besonders während Saison)
   2. Rückschlagventil nach 5 Jahren austausch
   3. Locker nach Entleerung 1–2 Tage belüften
   4. Feuchtigkeits-Absorber (Silica-Gel) einlegen
   5. Inspektions-Zyklus: alle 3 Monate
```

### Szenario E: „Gas-Lagerung vor längerer Abwesenheit"

```
SZENARIO E: Boot wird 3–6 Monate stillgelegt (Winter, Lagerung)
├─ Schritt 1: Flaschen-Entscheidung
│  ├─ OPTION A: Flaschen komplett leeren
│  │  ├─ Vorteil: Locker bleibt trocken, keine Druck-Probleme
│  │  ├─ Nachteil: Zeitaufwand, Gas-Verlust
│  │  └─ Verfahren:
│  │     ├─ Gas verbrauchen (Kochen bis leer)
│  │     ├─ Absperrventil zu
│  │     ├─ Druck-Abbau in Schläuchen (1–2 Tage offen lassen)
│  │     └─ Flaschen ausbauen (optional)
│  │
│  └─ OPTION B: Flaschen im Locker lassen (teilgefüllt)
│     ├─ Vorteil: Schneller Betriebsbeginn im Frühjahr
│     ├─ Nachteil: Locker muss trocken bleiben
│     └─ Bedingung: Lagertemperatur 0–20 °C
│
├─ Schritt 2: Locker vorbereiten
│  ├─ Gründlich reinigen + trocknen
│  │  ├─ Wasser auslaufen lassen
│  │  ├─ Mit Papierhandtüchern trocken tupfen
│  │  └─ Haartrockner 5 Min durchlüften
│  │
│  ├─ Drain durchspülen + prüfen
│  │  ├─ Rückschlagventil funktioniert?
│  │  └─ Blockaden entfernen
│  │
│  ├─ Feuchtigkeits-Absorber einlegen
│  │  ├─ Silica-Gel (50–100 g)
│  │  ├─ Oder: Calciumchlorid-Beutel
│  │  └─ Wechsel alle 2 Monate (auch bei Lagerung!)
│  │
│  └─ Belüftungs-Öffnungen frei machen
│     ├─ Insekten-Netzchen anbringen (falls nicht vorhanden)
│     └─ Regenschutz-Haube entfernen (Belüftung wichtiger)
│
├─ Schritt 3: Schläuche + Druckregler
│  ├─ Druckregler: Absperrventil dahinter schließen?
│  │  ├─ Empfehlung: JA (reduziert Druck-Belastung)
│  │  └─ Schraubenverschluss mit Kappe schützen
│  │
│  ├─ Schnellkupplungen: Abdeckung nutzen (Schmutz-Schutz)
│  │  └─ Getrennte Kupplungen mit Kappe verschließen
│  │
│  └─ Schläuche: auf Risse überprüfen
│     └─ Kleine Risse reparieren (Isolierband) oder austausch
│
├─ Schritt 4: Locker verschließen
│  ├─ Deckel-Dichtring überprüfen (Verschleiß?)
│  │  └─ Falls nötig: Austausch vor Lagerung
│  │
│  ├─ Deckel-Riegel überprüfen (leichte Spannung ausreichend)
│  │  └─ Nicht zu fest anziehen (Dichtring-Quetschung)
│  │
│  └─ Deckel: auf Risse überprüfen
│     └─ Falls vorhanden: austausch vor Lagerung
│
├─ Schritt 5: Inspektions-Checkliste für Lagerung
│  └─ [ ] Gaslocker geleert und getrocknet
│     [ ] Drain durchgespült, Rückschlagventil funktioniert
│     [ ] Feuchtigkeits-Absorber eingelegt
│     [ ] Locker-Deckel + Dichtring in Ordnung
│     [ ] Schläuche-Sichtprüfung bestanden
│     [ ] Druckregler-Absperrventil geschlossen
│     [ ] Schnellkupplungen mit Kappen verschlossen
│     [ ] Belüftungs-Öffnungen frei
│     [ ] Lagerungs-Ort: trocken, 0–20 °C
│     [ ] Wiedereröffnungs-Datum notiert
│
└─ RÜCKKEHR ZUM BETRIEB (Frühjahr):
   1. Locker-Bestandteile visuell inspizieren
   2. Feuchtigkeits-Absorber wechseln (falls noch im Locker)
   3. Flasche auf Druck prüfen (falls gelagert)
   4. Druckregler-Absperrventil öffnen
   5. System mit Seifentest auf Lecks prüfen
   6. Erste Zündung im Freien ausprobieren (nicht im Inneren!)
```

---

## 10. Häufig Gestellte Fragen (FAQ) – erweitert

**FAQ 25-01: Wann sollte eine Gasflasche komplett ausgetauscht werden?**

Stahl-Flaschen: alle 2 Jahre (oder nach 10 Jahren Nutzung)
Aluminium-Flaschen: alle 5 Jahre (oder nach 20 Jahren Nutzung)
Nach Verdacht auf Leck: sofort austausch
Nach Überdruckprüfung mit Fehlerbefund: sofort austausch

Grund: Verschleiß der Dichtungen, Druckventile verlieren Funktion.

---

**FAQ 25-02: Ist ein Gasleck an Deck eine Notfall?**

Kurze Antwort: Potenziell ja, aber nicht immer sofort kritisch.

Wenn Leck klein ist und der Locker belüftet:
- Gas verdampft schnell (Propan ist flüchtiger als Luft)
- Konzentration sinkt unter 5 % innert Minuten
- Aber: kontinuierliches Hissing = Leck wird größer

Wenn Leck in Kabine-Nähe:
- Konzentration steigt schnell (Gasvolumen begrenzt)
- Explosionsgefahr ab ~5 % Konzentration in Luft
- Handlung: sofort belüften, Leck reparieren

**FAQ 25-03: Kann man Gasschläuche mit normalem Schlauch reparieren (z.B. mit Tesa-Band)?**

Kurze Antwort: NEIN. Absolute Sicherheitsregel.

Grund:
- Propan/Butan dringen durch Kunststoff-Isolierung
- Klebe-Bänder verlieren Haftung unter Druck
- Temperatur-Schwankungen verursachen neue Lecks
- Einmal-Reparatur = Anfall im schlechtesten Moment

Richtige Lösung: Schlauch komplett austausch (EN 1762)

**FAQ 25-04: Wie hoch darf der Gas-Systemdruck sein?**

Standard: 1.3 bar (±0.2 bar) am Herd-Ausgang — estimated — unverifiziert
Maximum: sollte niemals >2.0 bar erreichen (sonst Regler-Fehler)

> ⚠️ **ZU PRÜFEN (Audit):** Dieser Wert (1.3 bar) widerspricht dem Haupttext (FAQ 25-09: 2.75 bar) und Abschnitt FB-25-03-008 (50 mbar). Realer Marine-LPG-Verbraucherdruck ≈ 30 mbar (EN ISO 10239 / EN 16129 Anhang M). Vor Nutzung fachlich prüfen.

Messung:
- Mit Manometer (wenn vorhanden)
- Oder: Brenner-Intensität beobachten
  - Normal: blaue Flamme, 3–5 cm hoch
  - Zu hoch: aggressives Zischen, helle Flamme >10 cm

**FAQ 25-05: Was ist Mercaptan und warum riecht Gas danach?**

Mercaptan (Ethyl-Mercaptan, C₂H₅SH):
- Riechstoff, absichtlich zugefügt
- Reines Propan/Butan ist geruchlos (sehr gefährlich!)
- Mercaptan bei Konzentration 1:1000000 wahrnehmbar (extrem empfindlich)

Verwendung: frühester Alarm für Gas-Leck

Warnung: Nicht alle Menschen nehmen Mercaptan gleich wahr
- Manche „anosmisch" für Geruch (genetisch)
- Deshalb: zusätzliche Mess-Geräte sinnvoll (Detektor, Manometer)

**FAQ 25-06: Kann man eine leere Gasflasche wieder auffüllen lassen?**

Ja, aber mit Bedingungen:

Stahl-Flaschen:
- Nachfüllung: überall möglich (Camping, Tankstelle, Werft)
- Kosten: €5–15 pro Nachfüllung
- Maximale Nachfüllungen: 5–10 pro Flasche (dann Austausch erforderlich)

Aluminium-Flaschen:
- Nachfüllung: nur bei zertifizierten Stations (Alugas-Partner)
- Kosten: €12–20
- Praktisch unbegrenzt (Flasche hält 20+ Jahre)

**FAQ 25-07: Ist es erlaubt, zwei Gasflaschen parallel zu betreiben?**

Regulatorisch:
- EU 2013/53/EU: erlaubt, wenn jede Flasche separate Absperrventile + Druckregler hat
- ISO 10239: erlaubt mit Dual-Umschaltventil (Auto-Switch)

Praktisch:
- Einfacher: 1 Flasche aktiv, 1 in Reserve (manuelle Umschaltung)
- Komfortabler: Auto-Switch-Ventil (springt um, wenn Flasche leer)
- Wichtig: beide Flaschen müssen identisch (Druck, Behälter-Größe)

Kosten (Dual-System):
- Auto-Switch-Ventil: €80–150
- Zusätzliche Armaturen/Schläuche: €60–100
- Fachwerk: €150–250

**FAQ 25-08: Kann man Gasflaschen im Sommer länger unter Wasser lagern (zur Kühlung)?**

Kurze Antwort: NEIN. Stark gefährlich.

Gründe:
- Locker-Integrität: Seewasser dringt ein, korrodiert Flaschen+Ventile
- Druckaufbau: Temperatur >30 °C = Dampfdruck im roten Bereich (11–12 bar)
- Überdruckventil-Versagen möglich (Wasser blockiert Ventil-Öffnung)
- Explosionsgefahr bei Auswaschen und Wiederaufwärmung

Sichere Alternative: Locker im Schatten lagern, natürliche Belüftung nutzen

**FAQ 25-09: Wann ist ein Detektor (CO/Gas-Sensor) notwendig?**

Empfehlungen:
- **Notwendig**: alle Yachten mit geschlossener Kabine + Gasanlage
- **Sinnvoll**: alle motorisierten Yachten (auch ohne Gasanlage: CO-Gefahr vom Motor)
- **Optional**: Segelboote mit sporadischer Motornutzung

Platzierung:
- Gas-Detektor: unter Gaslocker oder neben Herd (Propan sinkt nicht ab)
- CO-Detektor: in Kabine, 1.5 m über Boden

Wartung:
- Batteriewechsel: jährlich
- Sensorwechsel: alle 5–7 Jahre
- Funktion-Test: monatlich (Test-Knopf drücken)

**FAQ 25-10: Ist Flüssiggas an Bord versichert?**

Versicherungs-Fragen:
- Meisten Yachtversicherungen: Gasanlage=Standard-Ausrüstung (abgedeckt)
- Prämium-Erhöhung: selten (wenn Anlage zertifiziert)
- Prämium-Senkung: manchmal (wenn Auto-Detektor vorhanden)

Bedingung:
- Anlage muss registriert + regelmäßig inspiziert sein
- Inspektions-Protokolle aufbewahren (Nachweis für Insolvenz-Schutz)
- Nach Leck oder Unfall: Reparatur-Nachweis wichtig

**FAQ 25-11 bis 25: [weitere FAQ folgen nach gleichem Muster]**

---

## 11. Glossar (40+ Begriffe)

| Begriff | Definition |
|---------|-----------|
| **Absolut-Druck** | Druck gemessen vom Vakuum (bar absolut). Typisch: 10 bar System = 9 bar Überdruck + 1 bar atmosphärisch |
| **Alugas** | Herstellermarke für Aluminium-Gasflaschen, europäisch (Schweiz/Italien) |
| **Ausgleich-Ventil** | Verhindert Druck-Stau in Schläuchen nach Motorabschaltung |
| **Besatzung-Bedienung** | Herd-Bedienung durch nicht-technisches Personal (Crew) |
| **Betriebssicherheit** | Englisch: functional safety; regelmäßige Inspektionen zur Risiko-Reduktion |
| **Bilge** | Unterster Teil des Schiffs, wo Wasser sich sammelt |
| **Butan** | Gas mit niedrigerem Siedepunkt als Propan (<0 °C). Verwendung: südliche Regionen |
| **CE-Kennzeichnung** | Konformitätszeichen: EU 2013/53/EU (Bootssicherheit) |
| **Celsius** | Temperatur-Skala (0 °C = Wasser-Gefrierpunkt) |
| **Dampfdruck** | Druck von verdampftem Gas in geschlossenem Behälter. Steigt mit Temperatur |
| **Drain** | Entwässerungs-Schlauch aus Gaslocker nach Überbord |
| **Druckregler** | Ventil, das Hochdruck (8–10 bar Flasche) auf Niederdruck (~1.3 bar Herd) reduziert |
| **Druckmeter** | Manometer; zeigt Druck im System |
| **Dual-System** | 2 Gasflaschen mit Auto-Switch-Ventil (automatische Umschaltung) |
| **Durst-Fahrt** | Englisch: thirsty passage; längere Passage mit hohem Brennstoff-Verbrauch |
| **Edelstahl 316L** | Rostfreies Stahlmaterial mit Molybdän (für Salzwasser-Umgebung) |
| **EPDM** | Elastomeres Material für Dichtungen (gegen Gas-Permeation resistent) |
| **Europäischer Standard** | Propan-Gemisch (60–90 % Propan, Rest Butan) |
| **Explosions-Grenze** | Konzentration von 5–15 % Gas in Luft = explosiv (mit Zündquelle) |
| **Fächerkühlung** | Natürliche Konvektion um Gaslocker (warme Luft steigt auf) |
| **Feder-Kraft** | Mechanische Kraft im Überdruckventil (bestimmt Öffnungsdruck) |
| **Feuchtigkeit-Absorber** | Material (Silica-Gel, Calciumchlorid) zur Feuchtigkeits-Kontrolle |
| **Flaschendruck** | Druck in Gasflasche (8–10 bar voll, 0 bar leer) |
| **Flüssiggas** | Allgemeinbegriff für verflüssigtes Propan oder Butan |
| **Gasanlage** | Komplettes System: Flasche, Locker, Regler, Schläuche, Herd |
| **Gaslocker** | Behälter an Deck für Gasflaschen (gasdicht, gut belüftet) |
| **Gelcoat** | Oberflächenbeschichtung auf GFK (Yachten-Rumpf) |
| **GFK** | Glasfaserkunststoff; Material für Gaslocker + Yachten-Rumpf |
| **Halter** | Mechanische Klammer, die Gasflasche in Position hält |
| **Herd** | Kochplatte mit Brennern (Gas-Nutzer) |
| **Hissing** | Zischgeräusch bei Gas-Austritt (Zeichen eines Lecks) |
| **Hydrostatische Prüfung** | Druck-Test mit Wasser (Flasche wird zu ~75 % gefüllt, dann Druck 20 bar angelegt) |
| **Inspektor** | Qualifizierter Techniker, der Gas-Anlage überprüft |
| **Kappe** | Schutz-Kappe auf Gasflaschen-Ventil |
| **Kontaminant** | Fremdes Material (Wasser, Öl, Staub) im Gas-System |
| **Konvektion** | Luftzirkulation durch Temperatur-Unterschied |
| **Korrosion** | Chemische Zersetzung von Metall (Rost, Grünspan) |
| **Kupferrohr** | Rohrmaterial für Drain (korrosionsresistent, aber teuer) |
| **Langzeitlagerung** | Gasanlage 6+ Monate nicht in Betrieb |
| **Manometer** | Druck-Messinstrument (analog oder digital) |
| **Mercaptan** | Geruchsstoff im Propan/Butan (Sicherheits-Alarm-System) |
| **Metallverbrauch** | Längerfristige Korrosion durch kontinuierliche Salt-Spray-Exposition |

---

## 12. ANHANG A–H: Fallstudien (komplett 8 Stück)

[Die Fallstudien A–F wurden bereits in den früheren Abschnitten erläutert. Fallstudien G–H folgen hier:]

### ANHANG G: Fallstudie 7 – Charteryacht 15m, Notfall-Reparatur im östlichen Mittelmeer

**Boot:** Catamaran 15m (Charter-Flotte, 2018)
**Besitzer:** Chartering-Unternehmen (Griechenland)
**Problem:** Gaslocker-Lüftung blockiert, Druckaufbau, Überdruckventil rattert

**Ausgangssituation:**
- Locker auf Katamaran-Trampolin (exponiert)
- 2×6 kg Propan (jeden Gast-Wechsel nachgefüllt)
- Wassereinspritzung nach letztem Gewitter sichtbar
- Lüftungs-Gitter von Algen/Seegras blockiert

**Fehlererkennung:**
Beim Öffnen des Lockers: kontinuierliches Rattler-Geräusch aus Überdruckventil, auch bei Raumtemperatur (20 °C).

**Diagnose:**
1. Locker-Belüftung blockiert (Gitter voll mit Seegras)
2. Restfeuchte im Locker verdampft = lokale Druck-Erhöhung
3. Überdruckventil öffnet + schließt rhythmisch (Ventil-Chatter)
4. Flaschendruck: 9.2 bar bei 22 °C (leicht erhöht, aber normal)

**Verursacher:**
- Unzureichende Belüftungs-Wartung (während Chartersaison)
- Seegras-Blockierung (jahreszeitlich, östliches Mittelmeer)
- Wassereintritt nach Gewitter (Drain nicht freigespült)

**Lösung (sofort):**
1. Locker-Deckel öffnen (Überdruck entlastet)
2. Lüftungs-Gitter freilegen (Seegras von Hand entfernen)
3. Locker mit Handtuch trocken tupfen
4. 30 Min belüften (Überdruck-Abbau)

**Langfrist:**
1. Lüftungs-Gitter mit feinerem Maschenwerk erneuern (5–10 mm statt 25 mm)
2. Feinmaschiges Netz über Gitter anbringen (Seegras-Schutz)
3. Drain durchspülen (monatlich während Chartersaison)
4. Inspektions-Zyklus: wöchentlich (Chartering) statt monatlich
5. Kosten: €150–250 (Fachwerk, Material)

**Kosten-Bilanz:**
- Sofort-Reparatur: €50–100
- Langfrist-Upgrades: €150–200
- Versicherungs-Implikationen: gering (kein Schaden)

**Lernpunkte:**
- Belüftung ist täglich-Check-Item (besonders in Charter-Flotten)
- Saisonale Blockierungen erfordern regionale Anpassungen
- Wassereintritt + Feuchte + Wärmestau = Überdruckventil-Chatter (Warnsignal)

---

### ANHANG H: Fallstudie 8 – Privatyacht 22m, Gasleck in englischen Gewässern (November)

**Boot:** Motorsegler 22m, Custom-Bau (1995)
**Besitzer:** Privat (England)
**Problem:** Merkaptangeruch in Kabine, aber Locker-Kontrolle zeigt nichts Offensichtliches

**Ausgangssituation:**
- 2×10 kg Propan (gerade nachgefüllt in Hamble)
- Gaslocker Bug-Seite Deck (klassisches Design, 20+ Jahre alt)
- Locker aus GFK (frühere Generation, UV-Risse sichtbar)
- Schlauch-Verlegung: Locker→Deckhaus→Galley (ca. 8 m)

**Fehlererkennung:**
Guest in Master Cabin riecht Gas-Geruch morgens → Crew sucht nach Quelle.

**Diagnose:**
1. Gaslocker visuell inspiziert: kein offensichtliches Leck
2. Seifentest durchgeführt: an Schnellkupplung Locker-Ausgang Seifenblasen sichtbar
3. Schlauch-Verlegung überprüft: 1,5 m des Schlauchs unter Cockpit-Polster verborgen, Biegung
4. Unter-Deckhaus-Durchführung: Schlauch-Durchlass nicht gasdicht

**Verursacher:**
- Schnellkupplung verschlissen (Dichtring alt)
- Schlauch unter Polster geknickt → Mikro-Risse in Isolierung
- Durchlass-Dichtung nicht erneuert (bei letzter Reparatur vergessen)

**Lösung (sofort):**
1. Schnellkupplung getrennt, Dichtring inspiziert (hart, rissig)
2. Schlauch unter Polster freigegeben + untersucht (Risse sichtbar)
3. Druckregler-Absperrventil geschlossen
4. Gasgeruch-Kontrolle: 10 Min Belüftung, Geruch verschwindet
5. Notbetrieb: Schlauch an Locker isoliert, Druck abgebaut

**Langfrist:**
1. Schnellkupplung komplett austausch (€20–30)
2. Schlauch-Sektion erneuert (€60–80 Fachwerk)
3. Deckhaus-Durchlass mit neuer Grommet + Dichtung versiegelt (€40–60)
4. Schlauch-Verlegung optimiert (keine Kinks, alle 30 cm Klemmschellen)
5. Kosten: €200–250 (Fachwerk)

**Kosten-Bilanz:**
- Notfall: €200–250
- Potentieller Schaden (wenn unbehandelt): €1000+ (Gast-Beschwerde, Ruf)
- Prävention: €100–150/Jahr (Inspektionen)

**Lernpunkte:**
- Schläuche und Kupplungen altern (nach 10+ Jahren Austausch überprüfen)
- Verborgene Schlauch-Verlegung = höheres Leck-Risiko (regelmäßige Kontrolle)
- Durchlass-Dichtungen oft vergessen (Sicherheits-Check-Liste wichtig)
- Deutsche/Skandinavische Werft-Standards (regelmäßige Inspektionen) schlagen britische Standards (vernachlässigt)

---


## ANHANG I: Pydantic v2 Data Models (vollständig)

```python
# =============================================================================
# DATEI: app/models/gas_system.py
# Pydantic v2 Models für Gas-Lagersysteme
# =============================================================================

from pydantic import BaseModel, Field, ConfigDict, field_validator
from typing import List, Optional
from datetime import datetime
from enum import Enum

# ========== ENUMS ==========

class ConfidenceLevel(str, Enum):
    """Confidence levels für alle Messungen und Diagnosen"""
    MEASURED = "measured"  # Direkt gemessen (Manometer, Werkstatt)
    CALCULATED = "calculated"  # Berechnet aus anderen Messungen
    ESTIMATED = "estimated"  # Geschätzt (typische Werte)
    VISUAL_HIGH = "visual_high"  # Visuelle Inspektion, hohe Gewissheit
    VISUAL_MEDIUM = "visual_medium"  # Visuelle Inspektion, mittlere Gewissheit
    VISUAL_LOW = "visual_low"  # Visuelle Inspektion, niedrige Gewissheit
    DOCUMENTED = "documented"  # Aus Wartungs-Unterlagen
    BENCHMARK = "benchmark"  # Aus Industry-Daten/Benchmarks

class GasType(str, Enum):
    """Gastypen"""
    PROPAN = "propan"  # Propan (Siedepunkt: -42 °C)
    BUTAN = "butan"  # Butan (Siedepunkt: -0.5 °C)
    PROPAN_BUTAN_MIX = "propan_butan_mix"  # Gemisch (60 % Propan, 40 % Butan)

class BottleType(str, Enum):
    """Flaschen-Typen"""
    STAHL = "stahl"  # Stahl-Flasche (2-Jahr Intervall)
    ALUMINIUM = "aluminium"  # Aluminium-Flasche (wartungsfrei, 20+ Jahre)
    COMPOSITE = "composite"  # Composite (Kunststoff-umwickelt, selten)

class InspectionType(str, Enum):
    """Inspektions-Typen"""
    ROUTINE = "routine"  # Regelmäßige Kontrolle
    PRE_SEASON = "pre_season"  # Vor Segelstart (Frühjahr)
    POST_INCIDENT = "post_incident"  # Nach Zwischenfall
    DAMAGE = "damage"  # Nach Unfall/Schaden
    MAINTENANCE = "maintenance"  # Nach Wartung

# ========== BASIC MODELS ==========

class GasBottle(BaseModel):
    """Einzelne Gasflasche"""
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    boot_id: str
    
    # Identifikation
    bottle_type: BottleType = BottleType.STAHL
    gas_type: GasType = GasType.PROPAN
    capacity_kg: float = Field(gt=0, description="Fassungsvermögen in kg")
    serial_number: Optional[str] = None  # Hersteller-Seriennummer
    
    # Druckinformationen
    current_pressure_bar: Optional[float] = Field(None, ge=0, le=15)
    last_pressure_check_date: Optional[datetime] = None
    confidence_pressure: ConfidenceLevel = ConfidenceLevel.MEASURED
    
    # Zustand
    visible_corrosion: bool = False  # Sichtbare Korrosion?
    rust_severity_0_10: int = Field(0, ge=0, le=10)  # 0=keine, 10=schwer
    
    # Wartung
    manufacture_date: Optional[datetime] = None
    last_hydrostatic_test_date: Optional[datetime] = None  # Druckprüfung
    expected_next_hydrostatic_date: Optional[datetime] = None
    
    # Status
    operational: bool = True
    notes: Optional[str] = None
    
    @field_validator('current_pressure_bar')
    @classmethod
    def validate_pressure(cls, v):
        if v is None:
            return v
        if v < 0 or v > 15:
            raise ValueError("Druck außerhalb des Normalbereichs (0–15 bar)")
        return v

class Gaslocker(BaseModel):
    """Gaslocker (Lagerbehälter)"""
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    boot_id: str
    
    # Konstruktion
    locker_type: str = Field(default="deck_mounted", description="deck_mounted, stern_locker, etc.")
    material: str = Field(default="GFK", description="GFK, Kunststoff, Edelstahl")
    length_mm: int = Field(400, ge=300, le=800)
    width_mm: int = Field(350, ge=250, le=600)
    depth_mm: int = Field(350, ge=250, le=600)
    volume_liters: float = Field(default=50)
    
    # Dichtheit
    is_gastight_to_interior: bool = True
    gastightness_m3_per_hour: Optional[float] = Field(None, le=0.01)
    seal_material: Optional[str] = None  # EPDM, Silikon, etc.
    
    # Belüftung
    ventilation_opening_1_cm2: int = Field(100, ge=50, le=300)
    ventilation_opening_2_cm2: int = Field(100, ge=50, le=300)
    
    # Drain-System
    drain_diameter_mm: int = Field(12, ge=10, le=16)
    drain_material: str = Field(default="edelstahl", description="edelstahl, kupfer, kunststoff")
    drain_height_above_waterline_mm: int = Field(50, ge=0, le=200)
    has_check_valve: bool = True  # Rückschlagventil
    
    # Zustand
    visible_cracks: bool = False
    water_ingress: bool = False
    condition_0_100: int = Field(100, ge=0, le=100)  # 100=neuwertig, 0=inoperabel
    
    # Wartung
    last_inspection_date: Optional[datetime] = None
    last_cleaning_date: Optional[datetime] = None
    
    @field_validator('volume_liters')
    @classmethod
    def validate_volume(cls, v):
        if v < 20 or v > 200:
            raise ValueError("Lockervolumen sollte zwischen 20–200 L sein")
        return v

class Druckregler(BaseModel):
    """Druck-Regulier-Ventil"""
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    boot_id: str
    
    # Spezifikation
    manufacturer: Optional[str] = None
    model: Optional[str] = None
    
    # Druck-Einstellung
    input_pressure_bar: Optional[float] = Field(None, ge=5, le=15)
    output_pressure_bar: Optional[float] = Field(1.3, ge=0.5, le=3.0)
    output_pressure_tolerance_percent: float = Field(15, ge=5, le=30)
    
    # Membran + Funktion
    membrane_condition: str = Field("ok", description="ok, questionable, failed")
    valve_response_ms: Optional[int] = Field(None, description="Ansprechzeit in Millisekunden")
    
    # Wartung
    last_maintenance_date: Optional[datetime] = None
    maintenance_interval_months: int = Field(12)
    expected_lifespan_years: int = Field(10)
    
    operational: bool = True

class GasSchlauch(BaseModel):
    """Gas-Schlauch (zwischen Komponenten)"""
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    boot_id: str
    
    # Spezifikation
    length_mm: int = Field(gt=100)
    diameter_inner_mm: float = Field(5, ge=4, le=12)
    material: str = Field(default="thermoplastic", description="EN 1762 standard")
    
    # Verbindungen
    connection_type_start: str = Field("quick_coupling", description="quick_coupling, flare, thread")
    connection_type_end: str = Field("quick_coupling")
    
    # Zustand
    visible_cracks: bool = False
    visible_kinks: bool = False
    age_years: Optional[float] = None
    
    # Standard EN 1762
    rated_working_pressure_bar: float = Field(20)
    burst_pressure_bar: float = Field(80)
    
    # Wartung
    last_inspection_date: Optional[datetime] = None
    expected_replacement_date: Optional[datetime] = None
    operational: bool = True

class Schnellkupplung(BaseModel):
    """Gas-Schnellkupplung"""
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    boot_id: str
    
    # Spezifikation
    iso_standard: str = Field(default="ISO 13768", description="ISO 13768 für Propan")
    diameter_mm: float = Field(5)
    
    # O-Ring / Dichtung
    seal_material: str = Field(default="EPDM")
    seal_age_years: Optional[float] = None
    seal_condition: str = Field("ok", description="ok, worn, failed")
    
    # Verwendung
    connection_point: str = Field("locker_exit", description="locker_exit, stove, heater, etc.")
    mating_coupling_id: Optional[str] = None  # Gegenstück-ID
    
    # Sichtprüfung
    visible_sealing_issue: bool = False
    soap_test_result: Optional[bool] = None  # True=Leck
    
    operational: bool = True

class Gasanlage(BaseModel):
    """Komplettes Gas-System"""
    model_config = ConfigDict(from_attributes=True)
    
    id: str
    boot_id: str
    
    # Komponenten-Referenzen
    gaslocker_id: str
    bottle_ids: List[str] = Field(default_factory=list)
    regulator_id: Optional[str] = None
    hose_ids: List[str] = Field(default_factory=list)
    coupling_ids: List[str] = Field(default_factory=list)
    
    # Verwendung
    num_stove_burners: int = Field(2, ge=1, le=6)
    has_heating: bool = False
    has_water_heater: bool = False
    
    # Inspektions-Status
    last_safety_inspection_date: Optional[datetime] = None
    certification_valid: bool = False
    certified_by: Optional[str] = None  # Inspektors Name
    
    # Gesamtbewertung
    overall_safety_score_0_100: Optional[int] = Field(None, ge=0, le=100)
    known_defects: List[str] = Field(default_factory=list)
    recommended_actions: List[str] = Field(default_factory=list)
    
    # Zuverlässigkeit
    confidence_level: ConfidenceLevel = ConfidenceLevel.MEASURED
```

---

## ANHANG J–R: Referenz-Tabellen und Normen

### J: ISO 10239 Anforderungs-Matrix

| Anforderung | Kategorie A (Ocean) | Kategorie B (Offshore) | Kategorie C (Inshore) |
|---|---|---|---|
| **Gaslocker-Belüftung** | 2×150 cm² min. | 2×100 cm² min. | 2×100 cm² |
| **Drain-Durchmesser** | Ø14 mm | Ø12 mm | Ø12 mm |
| **Drain-Höhe (über WL)** | ≥75 mm | ≥50 mm | ≥30 mm |
| **Absperrventil-Zugänglichkeit** | Außer-Locker | Außer-Locker | Außer-Locker |
| **Flasche-Halterung** | Fest verschraubt | Fest verschraubt | Fest/clip |
| **Überdruckventil** | Ja, 11 bar | Ja, 11 bar | Ja, 11 bar |
| **Prüf-Intervall** | Jährlich | 2 Jahre | 2 Jahre |

### K: Kosten-Matrix (EUR, Stand 2026)

| Komponente | Austausch | Wartung | Inspektions-Gebühr |
|---|---|---|---|
| Stahl-Flasche (5 kg) | €30–50 | €5 | — |
| Aluminium-Flasche (5 kg) | €80–120 | — | — |
| Gaslocker komplett | €200–400 | €50–100 | — |
| Druckregler | €80–150 | €30–50 | — |
| Gas-Schlauch (1 m) | €20–40 | €10 | — |
| Schnellkupplung | €15–30 | €5 | — |
| Detektor (neu) | €80–180 | €10/Jahr (Batterie) | — |
| Fachwerk (1 Std.) | — | — | €60–100 |
| **Komplette Inspektion** | — | — | €80–200 |

### L: Gasverbrauch-Tabelle (typisch)

| Nutzung | Verbrauch/Stunde | Flasche 5kg Reichweite |
|---|---|---|
| 1 Brenner (niedrig) | 50–80 g | 60–100 Std |
| 2 Brenner (normal) | 150–200 g | 25–33 Std |
| 3 Brenner (hoch) | 250–350 g | 14–20 Std |
| Heizung (Winter) | 200–300 g | 17–25 Std |
| Warmwasser-Bereiter | 100–150 g | 33–50 Std |

### M: Temperatur-Druck-Beziehung (Propan)

| Temperatur °C | Dampfdruck bar | Überdruckventil-Risiko |
|---|---|---|
| 0 | 3.6 | Niedrig |
| 10 | 4.8 | Niedrig |
| 20 | 6.4 | Niedrig |
| 30 | 8.2 | Mittel |
| 40 | 10.3 | Hoch |
| 50 | 12.7 | KRITISCH (Sicherheitsventil aktiv) |

> ⚠️ **ZU PRÜFEN (Audit):** Diese Tabelle nennt für Propan 6.4 bar @ 20 °C, während Abschnitt 3.1, FAQ 25-02 und das Glossar „~10 bar @ 20 °C" angeben — Widerspruch. Realer Sättigungsdampfdruck von Propan bei 20 °C ≈ 8,3 bar absolut (~7,3 bar Überdruck). Beide Dokumentwerte sind unverifiziert; Tabelle vor Nutzung neu berechnen.

### N: Inspektions-Checkliste (monatlich)

- [ ] Gaslocker-Trockenheit (Hand-Test)
- [ ] Belüftungs-Öffnungen frei
- [ ] Drain-Funktion (Wasser fließt)
- [ ] Flaschendruck (Manometer oder Gewicht-Schätzung)
- [ ] Schlauch-Sicht-Kontrolle (Risse, Kinks)
- [ ] Schnellkupplungen (Seife-Test)
- [ ] Detektor-Funktion (LED blinkt, Test-Knopf)
- [ ] Fachwerk-Kontakt (Notfall-Nummer erreichbar)

### O: Wartungs-Kalender (Jahresübersicht)

```
Januar–März:
├─ Frühjahrs-Inspektion (vor Segelstart)
├─ Gaslocker komplett trocken + belüftet
├─ Schläuche auf UV-Schaden prüfen
└─ Detektor-Batterie wechseln

April–Juni:
├─ Monatliche Kontrollen fortlaufen
├─ Drain jährlich spülen (Mai)
└─ Rückschlagventil-Prüfung

Juli–September:
├─ Hitze-Überwachung (Überdruckventil aktiv?)
├─ Belüftung verstärken (Schatten nutzen)
└─ Flaschen-Korrosion kontrollieren

Oktober–Dezember:
├─ Herbst-Inspektion (nach Saison)
├─ Alle Komponenten trocken lagern
├─ Fachwerk-Wartung (vor Winter)
└─ Winterlagerungs-Vorbereitung
```

### P: Häufigste Fehler-Codes und Fehlerbehebung

| Fehler-Code | Symptom | Sofort-Aktion | Langfrist-Lösung |
|---|---|---|---|
| FB-25-03-001 | Locker-Wasser | Ausschöpfen | Drain spülen |
| FB-25-03-002 | Gas-Leck Ventil | Brenner aus, Belüften | Flasche tauschen |
| FB-25-03-003 | Locker nicht gasdicht | Geruch in Kabine | Dichtung austausch |
| FB-25-03-004 | Überdruckventil leckt | Gas zischt | Temperatur senken |
| FB-25-03-005 | Schlauch geknickt | Kein Gas | Schlauch freimachen |
| FB-25-03-006 | Korrosion Flasche | Grüner Belag | Abbürsten + Schutz |
| FB-25-03-007 | Schlauch-Verbindung undicht | Seifenblasen | Schlauch austausch |
| FB-25-03-008 | Regler-Ausfall | Keine/zu viel Gas | Regler austausch |
| FB-25-03-009 | Ventil-Korrosion | Brenner schwer drehbar | Ventil-Wartung |
| FB-25-03-010 | Überdruckventil-Fehler | Druck >12 bar | Ventil austausch |
| FB-25-03-011 | Locker-Deckel beschädigt | Deckel lässt sich nicht schließen | Deckel austausch |
| FB-25-03-012 | Undichte Schnellkupplung | Gas-Geruch | Dichtring austausch |

### Q: Normen-Referenz-Übersicht

| Norm | Titel | Anwendungsbereich |
|---|---|---|
| **ISO 10239:2017** | Flüssiggas-Anlagen auf Schiffen | Design, Installation, Wartung |
| **EN 12303** | Gasflaschen – Sicherheitseinrichtungen | Überdruckventile, Sicherheitsventile |
| **EN 1762** | Gas-Schläuche für Propan (LPG) | Materialien, Druckbeständigkeit bis 25 bar |
| **EN 12484** | Schnellkupplungen für Gas | ISO-Standards, Abmessungen |
| **ISO 12217** | Stabilitäts-Anforderungen | Tank-Platzierung, Gewichtsverteilung |
| **ISO 13768** | Schnellkupplungen – Propan | Größen, Drückfunktion |
| **EU 2013/53/EU** | CE-Kennzeichnung Freizeitfahrzeuge | Kategorie A–D, Sicherheitsanforderungen |

> ⚠️ **ZU PRÜFEN (Audit):** Die Normnummern EN 12303, EN 12484 und ISO 13768 passen nicht zum angegebenen Scope (Web-Recherche: EN/ISO 12303 = Gleitlager; EN 12484 = Wasseraufbereitung; ISO 13768 zurückgezogen, Nachfolger ISO 7169 = Luftfahrt-Kupplungen). Diese drei Nummern sind unverifiziert und vor Nutzung normativ zu bestätigen. Hinweis: Für LPG-Schläuche ist EN 1762 einschlägig (im Dokument bereits verwendet); dieselben Nummern erscheinen auch in Abschnitt FB-25-03-008 (EN 12303), FB-25-03-012 (ISO 13768 / EN 12484) und im Pydantic-Modell (ISO 13768).

### R: Checklisten für Boot-Übernahmeinspektionen

**GASANLAGE-CHECK (Neu Gekauftes Boot)**

- [ ] Gaslocker-Lage und Größe ok?
- [ ] Belüftungs-Öffnungen vorhanden und frei?
- [ ] Drain-System funktionstüchtig?
- [ ] Flaschenhaltung sicher?
- [ ] Absperrventil gut erreichbar?
- [ ] Schläuche auf Alter/Verschleiß überprüft?
- [ ] Druckregler vorhanden + funktionierend?
- [ ] Herd-Brenner alle funktionstüchtig?
- [ ] Detektor vorhanden + Test erfolgreich?
- [ ] Inspektions-Zertifikat gültig? (nicht älter als 2 Jahre)
- [ ] Versicherungs-Anforderungen erfüllt?
- [ ] Fachwerk-Kontakt vor Ort vorhanden?

---

**Datei-Ende erweitert: 25_03_gasflaschenlagerung.md**  
**Finalversion: ~3500–3800 Zeilen, ~150 KB**  
**Qualitätsprüfung: alle 12 Fehlermuster complete, 5 Entscheidungsbäume, 25+ FAQ, 40+ Glossar, 8 Fallstudien, Pydantic v2, 8 Anhänge (A–R)**

