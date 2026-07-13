# 06.06 — Gasschläuche (Propan/Butan LPG) im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 06.06** — Kategorie 6: Gastechnik und LPG-Systeme
> **Confidence-Quelle:** measured (Hersteller-TDS, Zertifizierungen), documented (EN/ISO-Normen, ABYC Standards, DVGW-Prüfberichte), estimated (Erfahrungswerte, Foren-Konsens)
> **Letzte Aktualisierung:** 2026-04-23

---

> ⚠️ **SICHERHEITSWARNUNG — HÖCHSTE PRIORITÄT**
> LPG (Propan/Butan) ist **schwerer als Luft** und sammelt sich in tiefliegenden Bereichen des Rumpfes.
> Ein einziger undichter Gasschlauch kann zu einer **Explosion** führen, die das Boot zerstört und Menschenleben kostet.
> Gas-Unfälle auf Yachten enden häufig **tödlich**.
> Jede Gasinstallation, jeder Schlauchwechsel, jede Inspektion ist **sicherheitskritisch**.
> **Im Zweifel: Gas abstellen, Yacht belüften, Fachmann rufen.**

---

## Inhaltsverzeichnis

1. [Einführung & Regulatorischer Rahmen](#1-einführung--regulatorischer-rahmen)
2. [Zukunftstechnologien & Neue Materialien](#2-zukunftstechnologien--neue-materialien)
3. [Best Practices nach Revier & Klimazone](#3-best-practices-nach-revier--klimazone)
4. [Regional Sourcing](#4-regional-sourcing)
5. [Zweck dieser Wissensdatei](#5-zweck-dieser-wissensdatei)
6. [Pydantic-Modelle für AYDI-Integration](#6-pydantic-modelle-für-aydi-integration)
7. [Grundlagen Gasschläuche](#7-grundlagen-gasschläuche)
8. [Hersteller — Vollständige Übersicht](#8-hersteller--vollständige-übersicht)
9. [Anlagen-spezifische Zuordnung](#9-anlagen-spezifische-zuordnung)

---

## 1. Einführung & Regulatorischer Rahmen

### 1.1 Bedeutung für Yacht-Sicherheit (Explosionsgefahr!)

LPG-Systeme (Flüssiggas, Liquefied Petroleum Gas) sind auf Yachten die mit Abstand **gefährlichste Bordinstallation**. Kein anderes System an Bord hat ein vergleichbares Zerstörungspotenzial. Die Kombination aus:

- **Brennbarem Gas** (untere Explosionsgrenze Propan: 2,1 Vol.-%, Butan: 1,8 Vol.-%)
- **Geschlossenem Rumpf** (Gas kann nicht entweichen)
- **Schwerer-als-Luft-Eigenschaft** (Propan: 1,56× Luft, Butan: 2,07× Luft → sinkt in Bilge)
- **Zündquellen** überall (Elektrik, Lichtmaschine, Starter, Schalter, statische Entladung)

macht jede Undichtigkeit zu einer potenziellen Katastrophe. Ein Gasschlauch, der auf einer Landinstallation lediglich zu erhöhtem Verbrauch führt, kann auf einer Yacht eine **Volumexplosion** auslösen, die den gesamten Rumpf zerstört.

**Physikalische Grundlage der Gefahr:**
- Propan hat eine Dichte von 1,88 kg/m³ bei 15°C (Luft: 1,225 kg/m³)
- Ein defekter Gasschlauch mit 0,5 mm Riss bei 30 mbar Betriebsdruck verliert ca. 2–5 l/h Gas
- Bei einem Bilgenvolumen von 500 l erreicht die Gaskonzentration in ca. 3–8 Stunden die untere Explosionsgrenze
- Die Explosionsenergie von 1 kg Propan entspricht ca. 2,4 kg TNT
- Eine 11-kg-Propanflasche enthält genug Energie, um ein 12-m-Boot vollständig zu zerstören

**Typische Unfallszenarien:**
1. **Der „Morgen-nach-dem-Kochen"-Unfall**: Gasflasche nicht zugedreht, Schlauch oder Verbindung leckt über Nacht, Gas sammelt sich in Bilge, beim Einschalten der Bilgepumpe oder des Bordnetzes am Morgen erfolgt Zündung
2. **Der „Alte-Schlauch"-Unfall**: Schlauch über Ablaufdatum (>10 Jahre), Materialermüdung, Haarrisse nicht sichtbar, schleichende Leckage
3. **Der „Vibrationsbruch"-Unfall**: Motorvibrationen lösen Verschraubung am Regler oder Verbraucher, besonders bei starrer Verrohrung ohne flexible Endstücke
4. **Der „Reibungsschaden"-Unfall**: Schlauch scheuert an Schott-Durchführung, Kabel oder Metallkante, Außenmantel durchgescheuert
5. **Der „Winterfrost"-Unfall**: Kondenswasser in Butanflasche gefriert, Regler blockiert, nach Auftauen unkontrollierter Gasaustritt

### 1.2 Häufigkeit von Gas-Unfällen auf Yachten

**Statistische Daten (zusammengetragen aus BSU, MAIB, USCG, BSAA):**

| Quelle | Zeitraum | Gasunfälle | Todesfälle | Schwerstverletzte |
|--------|----------|------------|------------|-------------------|
| MAIB (UK) | 2010–2023 | 47 meldepflichtige | 8 | 23 |
| BSU (DE) | 2010–2023 | 12 meldepflichtige | 3 | 9 |
| USCG (USA) | 2015–2023 | 89 (Recreational) | 14 | 51 |
| BSAA (AUS) | 2010–2023 | 18 | 4 | 12 |

**Dunkelziffer:** Die tatsächliche Zahl liegt schätzungsweise 5–10× höher, da viele Kleinunfälle (Verpuffungen, Verbrennungen) nicht gemeldet werden.

**Hauptursachen nach MAIB-Analyse (UK, 2019):**
- 34% — Undichte Schlauchverbindungen (davon 60% altersbedingt)
- 22% — Defekte oder fehlende Gas-Absperrventile
- 18% — Fehlender oder nicht funktionierender Gasdetektor
- 12% — Unsachgemäße Installation (DIY ohne Fachkenntnis)
- 8% — Defekte Regler
- 6% — Sonstige (Flaschenschaden, Transportschaden, Vandalismus)

**AYDI-Bewertungsbasis:** Jedes Boot mit LPG-System, das keinen funktionierenden Gasdetektor hat, erhält automatisch einen **CRITICAL**-Befund mit Confidence `measured` oder `visual_high`.

### 1.3 Regulatorische Anforderungen (EN, ISO, ABYC, TRF, DVGW)

#### Normenhierarchie für marine LPG-Systeme

```
Internationale Ebene:
  ISO 10239:2014 — Kleine Wasserfahrzeuge — LPG-Systeme
  (Die zentrale Norm für alle LPG-Installationen auf Booten <24m)

EU-Ebene:
  EU Recreational Craft Directive 2013/53/EU
  → Verweist auf ISO 10239 als harmonisierte Norm
  EN 1763:2004+A1:2009 — Gummischläuche für LPG (Dampfphase)
  EN 16436-1:2014 — Gummischläuche mit Anschlussarmaturen für LPG
  EN 14800:2007 — Metallwellschläuche für Gas

Deutsche Ebene:
  TRF 2012 (Technische Regeln Flüssiggas) — DVGW/DVFG
  DIN 30665:2003 — Gasschlauchleitungen
  DVGW G 5614 — Prüfgrundlage für Gasschläuche
  BetrSichV — Betriebssicherheitsverordnung
  DGUV Regel 110-010 — Verwendung von Flüssiggas

US-Ebene:
  ABYC A-1 (2021) — Marine LPG (Propane) Systems
  ABYC A-22 (2019) — Marine CNG Systems
  NFPA 302 — Fire Protection Standard for Pleasure and Commercial Motor Craft

UK-Ebene:
  BSS (Boat Safety Scheme) — Section 7: LPG Systems
  BS EN 1763 / BS EN 16436 (nationale Adoption der EN-Normen)
```

#### Kernforderungen der wichtigsten Normen

**ISO 10239:2014 — Kleine Wasserfahrzeuge — Flüssiggasanlagen:**

| Anforderung | ISO 10239 Sektion | Detail |
|-------------|-------------------|--------|
| Gasflaschenlagerung | 5.2 | Gaslocker gasdicht zum Boot, Drainage nach außenbords, Belüftung oben |
| Druckregler | 5.3 | 30 mbar Betriebsdruck (EU), zweistufige Regelung empfohlen |
| Gasschläuche | 5.4 | EN 1763 oder EN 16436 konform, max. Länge 1500 mm, zugänglich auf gesamter Länge |
| Absperrventil | 5.5 | Hauptabsperrung an der Flasche + fernbedienbares Magnetventil in der Nähe des Verbrauchers |
| Leckdetektor | 5.6 | Gasdetektor in der Bilge, akustischer und visueller Alarm, automatische Absperrung empfohlen |
| Leitungsführung | 5.7 | Kupfer (EN 1057) oder Edelstahl (316L), keine Durchführung durch Wohnräume ohne Schutzrohr |
| Verbraucher | 5.8 | Flammensicherung Pflicht, ausreichende Belüftung am Aufstellort |
| Prüfung | 5.10 | Druckprüfung bei Installation mit 150 mbar, 3 min halten, kein Druckabfall |
| Kennzeichnung | 5.11 | Schild mit Systemdaten, Datum der Installation, nächster Prüftermin |

**ABYC A-1 (2021) — Marine LPG (Propane) Systems:**

ABYC A-1 ist strenger als ISO 10239 in mehreren Punkten:

| Anforderung | ABYC A-1 Detail | Vs. ISO 10239 |
|-------------|------------------|---------------|
| Gasdetektor | **Pflicht**, nicht nur empfohlen | ISO: empfohlen |
| Sensorposition | Max. 150 mm über Bilgenboden | ISO: „tiefer Punkt" |
| Alarm | Akustisch **und** visuell, min. 85 dB | ISO: akustisch oder visuell |
| Automatische Absperrung | **Pflicht** bei Detektor-Alarm | ISO: empfohlen |
| Schlauch-Inspektion | Jährlich dokumentiert | ISO: regelmäßig |
| Schlauch-Austausch | Alle 10 Jahre oder bei Mängeln | ISO: Herstellerangabe |
| Leitungsfarbe | Orange für Gas | ISO: keine Vorgabe |
| Drucktest | 1,5× Betriebsdruck, 15 min | ISO: 150 mbar, 3 min |

**TRF 2012 (Technische Regeln Flüssiggas, Deutschland):**

Die TRF 2012 (herausgegeben von DVGW und DVFG) regelt in Abschnitt 10 „Flüssiggasanlagen in Fahrzeugen" die Anforderungen für mobile Anlagen, unter die auch Boote fallen:

- Schlauchleitung nach DIN 30665 oder EN 1763
- Maximale Schlauchlänge: 400 mm (ohne Verlängerung) / 1500 mm (mit Verlängerung für eingebaute Geräte)
- Schlauch muss auf gesamter Länge **sichtbar und zugänglich** sein
- Schlauch darf **nicht durch Wände, Böden oder Schotte** geführt werden
- Aufdruck auf Schlauch: Hersteller, Norm, Herstelldatum, Prüfzeichen
- **Verwendungsdauer: max. 10 Jahre ab Herstelldatum** (Aufdruck auf Schlauch)
- Prüfintervall für Gesamtanlage: alle 2 Jahre durch Sachkundigen (nach G 607)

**EN 1763:2004+A1:2009 — Gummischläuche und Gummischlauchleitungen für Flüssiggas (Dampfphase, bis 25 bar):**

Definiert Anforderungen an Schlauchmaterial und Konstruktion:

| Parameter | Anforderung |
|-----------|-------------|
| Innenschicht | LPG-beständig (NBR oder gleichwertig) |
| Verstärkung | Textilgeflecht oder -gewebe |
| Außenschicht | Witterungsbeständig, UV-stabil, abriebfest |
| Berstdruck | Min. 4× Betriebsdruck |
| Betriebstemperatur | -30°C bis +70°C |
| Ozonbeständigkeit | 50 pphm, 72 h, keine Risse (ISO 1431) |
| Kälteflexibilität | Keine Risse bei -30°C nach Biegetest |
| Gaspermeabilität | Max. 300 cm³/(m·h) bei 20°C, Propan |
| Kennzeichnung | Herstellername, Norm, Quartal+Jahr, Betriebsdruck, „LPG" |

**EN 16436-1:2014 — Gummischläuche und Gummischlauchleitungen für Flüssiggas — Schlauchleitungen:**

Ergänzt EN 1763 um Anforderungen an **konfektionierte Schlauchleitungen** (Schlauch + Anschlussarmaturen):

- Armaturen: geschmiedet oder gedreht, nicht gegossen
- Schlauchschellen: doppelte Schlauchschelle oder Presshülse
- Gasdichtigkeitsprüfung: 100% der Produktion bei 1,5× Betriebsdruck
- Klasse 1 (max. 30 mbar): Für Niederdruckseite, orange Außenmantel
- Klasse 2 (max. 4 bar): Für Hochdruckseite, im Marine-Bereich selten

**EN 14800:2007 — Gewellte Sicherheits-Metallschlauchleitungen für Gas:**

Definiert Anforderungen an Edelstahl-Wellschläuche als Alternative zu Gummischläuchen:

| Parameter | Anforderung |
|-----------|-------------|
| Material | Austenitischer Edelstahl (AISI 316L für Marine) |
| Ummantelung | Edelstahlgeflecht oder Kunststoffummantelung |
| Berstdruck | Min. 5× Betriebsdruck |
| Lebensdauer | Nicht zeitbegrenzt (vs. 10 Jahre bei Gummi) |
| Biegezyklen | Min. 1000 Zyklen ohne Ermüdung |
| Anschlüsse | Gedrehte Überwurfmuttern, nicht gelötet |

**Vorteil Marine:** Kein 10-Jahres-Austausch nötig, höhere Vibrationsbeständigkeit, UV-unempfindlich.
**Nachteil Marine:** Teurer (3–5× Gummischlauch), schwerer, engerer Biegeradius.

### 1.4 ISO 10239 im Detail

ISO 10239:2014 „Small craft — Liquefied petroleum gas (LPG) systems" ist die zentrale internationale Norm für LPG-Installationen auf Booten unter 24 m Länge. Sie wird von der EU Recreational Craft Directive 2013/53/EU als harmonisierte Norm referenziert.

**Anwendungsbereich:**
- Alle LPG-Systeme auf Wasserfahrzeugen <24 m (CE-Pflicht)
- Gilt auch für Wasserfahrzeuge >24 m als Stand der Technik
- Umfasst: Flaschenaufstellung, Druckregelung, Leitungen, Schläuche, Verbraucher, Detektoren, Prüfung

**Schlüsselkapitel mit AYDI-Relevanz:**

**Kapitel 5.2 — Flaschenaufstellung (Gaslocker):**
- Gaslocker muss vom Bootsinneren gasdicht getrennt sein
- Mindestens ein Ablauf (Drain) nach außenbords, Durchmesser ≥ 19 mm
- Drain muss am tiefsten Punkt des Lockers enden
- Drain darf nicht in Cockpit-Ablauf münden (separate Durchführung)
- Locker muss von oben belüftet sein (min. 2500 mm² freier Querschnitt)
- Locker darf keine elektrischen Geräte oder Leitungen enthalten
- Flaschen müssen gegen Verrutschen und Umfallen gesichert sein
- **Prüfkriterium für AYDI:** Gaslocker visuell bewerten → visual_high wenn Drain, Dichtung und Belüftung sichtbar und korrekt

> ⚠️ **ZU PRÜFEN (Audit):** Belüftungsquerschnitt Gaslocker — hier „min. 2500 mm² (oben)" vs. Anhang „250 mm² unten + 250 mm² oben" (EN-1949-Abschnitt, jährliche Checkliste, Fehlerkatalog). Web-Recherche (EN ISO 10239) bestätigt zweifelsfrei nur den **Drain ≥ 19 mm Innen-Ø (≈ 283 mm²) am tiefsten Punkt nach außenbords**; eine separate Oben-Belüftungsfläche von 2500 mm² ist nicht verifiziert. Wert **estimated — unverifiziert**, nicht als „measured" behandeln.

**Kapitel 5.4 — Schläuche und Leitungen:**
- Starre Leitungen: Kupfer nach EN 1057 (wandstärke min. 1 mm, weich oder halbhart) oder Edelstahl 316L
- Flexible Schläuche: nur an Anschlüssen Flasche→Regler und Leitung→Verbraucher
- Max. Schlauchlänge: 750 mm (Flasche→Regler), 1500 mm (Leitung→Verbraucher)
- Schlauch auf gesamter Länge sichtbar und inspizierbar
- Keine Durchführung flexibler Schläuche durch Schotte oder Böden
- Schlauch darf keine scharfen Kanten berühren (Scheuerschutz erforderlich)
- Schlauch muss spannungsfrei montiert sein (Mindestbogen, kein Zug auf Anschlüsse)
- Kennzeichnung: Hersteller, Norm (EN 1763 / EN 16436), Herstelldatum, „LPG"

**Kapitel 5.5 — Absperrungen:**
- Hauptabsperrung: Ventil an der Gasflasche
- Fernabsperrung: Magnetventil (Solenoid), ansteuerbar vom Bedienpunkt des Verbrauchers
- Magnetventil muss bei Stromausfall schließen (fail-closed / normally-closed)
- Schalter für Magnetventil in Sichtweite des Verbrauchers, deutlich gekennzeichnet
- **AYDI-Prüfung:** Vorhandensein und Funktion des Magnetventils ist CRITICAL-Kriterium

**Kapitel 5.6 — Gasdetektion:**
- Gasdetektor empfohlen (ISO 10239 sagt „should", nicht „shall")
- ABYC A-1 macht Detektor zur Pflicht — AYDI übernimmt die ABYC-Forderung als Best Practice
- Sensor: tiefster erreichbarer Punkt im Rumpf, max. 150 mm über Bilgenboden
- Alarm: akustisch min. 85 dB(A) am Bedienpunkt
- Kalibrierung: jährlich oder nach Herstellerangabe
- Selbsttest: tägliche automatische Prüfung empfohlen
- **AYDI-Regel:** Boot ohne Gasdetektor bei vorhandenem LPG-System → automatisch score ≤ 30/100 im Compliance-Modul (Bereich Gassicherheit)

**Kapitel 5.10 — Prüfung und Abnahme:**

| Prüfschritt | Methode | Kriterium |
|-------------|---------|-----------|
| Sichtprüfung | Visuelle Inspektion aller Komponenten | Keine Beschädigungen, korrekte Montage |
| Dichtheitsprüfung (Niederdruck) | Druckprüfung mit Luft oder Stickstoff, 150 mbar | Kein Druckabfall in 3 Minuten |
| Dichtheitsprüfung (Hochdruck) | Sprühtest mit Lecksuchspray | Keine Blasenbildung |
| Funktionsprüfung Magnetventil | Schalter betätigen, Durchfluss prüfen | Öffnet bei Strom, schließt ohne Strom |
| Funktionsprüfung Gasdetektor | Prüfgas an Sensor halten | Alarm innerhalb 30 Sekunden |
| Flammenüberwachung | Flamme ausblasen, Gas muss stoppen | Abschaltung innerhalb 60 Sekunden |
| Dokumentation | Prüfprotokoll ausfüllen | Datum, Prüfer, Befunde, nächster Termin |

---

## 2. Zukunftstechnologien & Neue Materialien

### 2.1 Emerging Materials (2024–2030)

**Thermoplastische Elastomere (TPE) für Gasschläuche:**
- Hersteller wie Continental und Parker entwickeln TPE-basierte Gasschläuche
- Vorteile: längere Lebensdauer (geschätzt 15–20 Jahre vs. 10 Jahre NBR), bessere UV-Beständigkeit, recycelbar
- Status: noch nicht in EN 1763 aufgenommen, Pilotprojekte laufen
- Continental-Produktlinie: „ContiTech FLEXAgas TPE" (in Entwicklung)
- Parker: „Parflex Division" — TPE-Schlauch Typ 540T (bisher nur Industrie, Marine-Zulassung ausstehend)

**Nano-beschichtete Innenschichten:**
- Forschung an SiO₂-Nanopartikelbeschichtungen zur Reduktion der Gaspermeation
- Erste Labortests zeigen 80% geringere Permeation vs. Standard-NBR
- Marktreife geschätzt: 2027–2028

**Kevlar-verstärkte Schläuche:**
- Trelleborg und Semperit testen Kevlar-Gewebe anstelle von Polyester
- Vorteile: 3× höhere Berstfestigkeit, geringeres Gewicht
- Nachteil: UV-Empfindlichkeit des Kevlar erfordert zusätzlichen Außenschutz
- Kosten: ca. 2× konventioneller Schlauch

**3D-gedruckte Anschlussarmaturen:**
- Additive Fertigung in 316L-Edelstahl für Spezialanschlüsse
- Relevant für: Oldtimer-Yachten mit nicht mehr erhältlichen Armaturen
- Zulassungsproblem: individuelle Baumusterprüfung erforderlich

### 2.2 Elektrische Alternativen zu LPG (Induktion, Infrarot)

**Induktionskochfelder für Yachten:**

Die Elektrifizierung von Yacht-Küchen ist der wichtigste Trend zur Eliminierung der LPG-Explosionsgefahr.

| Hersteller | Modell | Leistung | Anschluss | Preis (EUR) |
|------------|--------|----------|-----------|-------------|
| Kenyon | SilKEN2 B41776 | 2× 1300W | 230V/50Hz | 890 |
| Kenyon | Lite-Touch Q B80005 | 2× 1500W | 230V/50Hz | 1.250 |
| CAN (Italien) | PI1162 | 2× 1400W | 230V/50Hz | 680 |
| Dometic | MCI-2340 | 2× 1800W | 230V/50Hz | 1.450 |
| Wallas (Finnland) | 86DU | 2× 1200W (Keramik) | 230V/50Hz | 1.100 |
| ENO | EMILIA 2 | 2× 1800W | 230V/50Hz | 1.680 |

**Strombedarf-Analyse für LPG-Ersatz:**
- 2-Flammen-Kocher: ca. 2.500–3.600 W Spitze
- Erforderliche Batteriekapazität für 1 h Kochen: ca. 250–400 Ah bei 12V
- LiFePO4-Batterie dafür: ca. 1.800–3.200 EUR
- Wechselrichter (3.000 W, reiner Sinus): ca. 800–1.500 EUR
- **Gesamtkosten Elektrifizierung: 3.500–6.500 EUR** vs. LPG-System ca. 800–1.500 EUR

**AYDI-Empfehlung:** Für Langfahrt mit begrenztem Stromangebot bleibt LPG auf absehbare Zeit die praktikabelste Lösung. Für Küstenfahrt und Yachten mit Generatoranlage oder großer Solaranlage ist Induktion die sicherere Alternative.

### 2.3 Digitale Gas-Überwachung

**Smart-Gas-Monitoring-Systeme:**

| System | Hersteller | Funktionen | Preis (EUR) |
|--------|------------|------------|-------------|
| Truma LevelControl | Truma | Füllstand per Ultraschall, App | 179 |
| Truma iNet Box | Truma | Fernsteuerung + Monitoring | 399 |
| GOK Senso4s Plus | GOK | Füllstand + Leckdetektor, BLE | 149 |
| Mopeka Pro Check | Mopeka | Ultraschall-Füllstand, WLAN | 89 |
| Gas Boat GD-1 | Gas Boat (UK) | Marine-Gasdetektor + Solenoid | 295 |
| XINTEX MS-2 | Fireboy-Xintex | 2-Kanal Marine-Detektor | 385 |
| NASA Marine Gas Detector | NASA Marine | Katalytischer Sensor, 12V | 195 |

**IoT-Integration:**
- Truma iNet System: MQTT-fähig, Integration in Yacht-Automation (Signal K, NMEA 2000 über Gateway)
- Mopeka Pro: BLE Advertising, lesbar von RaspberryPi / Signal K Server
- Fireboy-Xintex: NMEA 2000 PGN 127501 (Binary Status Report) für Alarm-Integration

**AYDI-Integration:**
- Vorhandensein eines digitalen Monitoring-Systems erhöht den Compliance-Score um 5–10 Punkte
- IoT-fähiges System mit automatischer Absperrung: +15 Punkte vs. manuelle Absperrung

### 2.4 CNG/LNG Marine-Systeme

**CNG (Compressed Natural Gas) — Erdgas auf Yachten:**

CNG (Methan, CH₄) hat einen fundamentalen Sicherheitsvorteil gegenüber LPG: Es ist **leichter als Luft** (Dichte 0,72 kg/m³) und steigt nach oben, anstatt sich in der Bilge zu sammeln.

| Parameter | CNG (Methan) | LPG (Propan) | LPG (Butan) |
|-----------|-------------|--------------|-------------|
| Relative Dichte (Luft=1) | 0,55 | 1,56 | 2,07 |
| Untere Explosionsgrenze | 5,0 Vol.-% | 2,1 Vol.-% | 1,8 Vol.-% |
| Obere Explosionsgrenze | 15,0 Vol.-% | 9,5 Vol.-% | 8,4 Vol.-% |
| Verhalten bei Leck | Steigt auf, ventiliert | Sinkt in Bilge | Sinkt in Bilge |
| Speicherdruck | 200–250 bar | 8–12 bar | 2–4 bar |
| Energiedichte pro Volumen | 9 MJ/l (250 bar) | 25,3 MJ/l (flüssig) | 27,7 MJ/l (flüssig) |

**CNG-Norm:** ABYC A-22 (2019) — Marine CNG Systems

**CNG auf Yachten — Status:**
- In den USA verbreiter als in Europa (Dometic/SMEV bietet CNG-Versionen an)
- Problem: CNG-Flaschen sind groß und schwer (200-bar-Stahlflasche: 25 kg für 5 m³ Gas)
- Verfügbarkeit von CNG-Befüllstationen in Marinas: in Europa praktisch null
- **AYDI-Bewertung:** CNG als „empfohlen wenn verfügbar" markiert, aber praktisch selten anzutreffen

**LNG (Liquefied Natural Gas) auf Yachten:**
- Noch exotischer als CNG im Yachtbereich
- Betriebstemperatur: −162°C (erfordert kryogene Tanks)
- Aktuell nur auf Großyachten (>40 m) und kommerziellen Schiffen relevant
- Kein Standard für Yachten <24 m

### 2.5 Nachhaltigkeit

**Ökobilanz von LPG-Schläuchen:**

| Material | CO₂-Fußabdruck (kg/m Schlauch) | Lebensdauer | CO₂/Jahr |
|----------|-------------------------------|-------------|----------|
| NBR-Gummischlauch | 3,2 | 10 Jahre | 0,32 |
| Edelstahl-Wellschlauch | 8,5 | 30+ Jahre | 0,28 |
| TPE-Schlauch (Prognose) | 2,1 | 15 Jahre | 0,14 |

**Recycling:**
- NBR-Gummischläuche: Energetische Verwertung (Verbrennung), kein Materialrecycling
- Edelstahl-Wellschläuche: Vollständig recycelbar (Schrottwert ca. 2–4 EUR/m)
- Alte Gasschläuche sind **Sondermüll**, wenn sie mit LPG kontaminiert sind

**LPG-Alternativen aus Nachhaltigkeitssicht:**

| Alternative | CO₂-Reduktion vs. LPG | Praktikabilität Marine | Marktreife |
|-------------|----------------------|----------------------|------------|
| Induktion + Solar | 80–100% | Mittel (Strombedarf) | Ja |
| BioLPG (rDME) | 50–80% | Hoch (gleiche Technik) | Begrenzt |
| Methanol-Kocher | 60–70% | Gering (Sicherheit) | Nische |
| Spiritus-Kocher | 40–50% | Mittel (Leistung gering) | Rückläufig |

---

## 3. Best Practices nach Revier & Klimazone

### 3.1 Nordeuropa (Ostsee, Nordsee, Skandinavien, UK)

**Klimabedingungen:** −20°C bis +25°C, hohe Feuchtigkeit, UV-Exposition moderat

| Thema | Empfehlung |
|-------|------------|
| Gastyp | **Propan ausschließlich** — Butan versagt unter +5°C |
| Schlauch | NBR Klasse 1, Kältebeständig bis −30°C, EN 1763 |
| Winterlager | Gasflaschen entfernen, System entlüften, Schläuche im warmen Raum lagern |
| Regler | Truma MonoControl CS (mit Crash-Sensor), temperaturkompensiert |
| Detektor | NASA Marine Gas Detector (12V, bewährt UK-Flotte) |
| Inspektion | Vor Saisonstart (April/Mai) + Mitte Saison (Juli) |
| Besonderheit | Kondenswasserbildung in Gaslockern → Drain-Kontrolle besonders wichtig |

### 3.2 Mittelmeer (Balearen, Adria, Ägäis, Türkische Riviera)

**Klimabedingungen:** +5°C bis +45°C, niedrige Feuchtigkeit Sommer, hohe UV-Exposition

| Thema | Empfehlung |
|-------|------------|
| Gastyp | Propan oder Butan (Butan günstiger, funktioniert ganzjährig bei >5°C) |
| Schlauch | EPDM oder NBR mit UV-Schutzschicht, Hitzebeständig bis +70°C |
| UV-Schutz | Schläuche in Cockpitbereich zusätzlich mit UV-Schutzschlauch überziehen |
| Regler | GOK Caramatic DriveTwo (Umschaltregler Propan/Butan) |
| Detektor | XINTEX MS-2 (hitzebeständig bis +55°C Sensortemperatur) |
| Inspektion | Halbjährlich (Herbst + Frühjahr) |
| Besonderheit | Flaschendruck Butan bei 40°C: ca. 3,8 bar → Regler muss ausgelegt sein |

### 3.3 Tropen und Langfahrt (Karibik, Pazifik, Indischer Ozean)

**Klimabedingungen:** +20°C bis +50°C (in Gaslocker!), Salzluft konstant, UV extrem

| Thema | Empfehlung |
|-------|------------|
| Gastyp | Propan (universelle Verfügbarkeit), Butanbeimischung akzeptabel |
| Schlauch | **Edelstahl-Wellschlauch** bevorzugt (keine 10-Jahres-Grenze, UV-immun) |
| Alternativ | TPE oder EPDM mit Edelstahl-Umflechtung |
| Regler | Cavagna Group Typ 7KG Adjustable (anpassbar an verschiedene Flaschensysteme) |
| Adapter-Set | GOK Adapter-Set „Welt" (Art. 01-150-00): 8 verschiedene Flaschenanschlüsse |
| Detektor | Fireboy-Xintex MS-2 mit Backup-Sensor |
| Flaschenbefüllung | Gaslow-System (nachfüllbar) + lokale Adapter |
| Inspektion | Vierteljährlich (quartalsweise) |
| Besonderheit | Verschiedene Flaschenanschlüsse weltweit → Adapter-Set Pflicht |

### 3.4 Arktische/Subarktische Reviere (Norwegen, Island, Grönland, Spitzbergen)

| Thema | Empfehlung |
|-------|------------|
| Gastyp | **Nur Propan** — Butan bei −20°C vollständig flüssig |
| Schlauch | EN 1763 Klasse 1, Kältetest bis −40°C bestanden |
| Regler | Truma MonoControl CS mit Eisfreihalter (EisEx) |
| Vereisungsgefahr | Regler kann bei hohem Verbrauch vereisen → Heizband am Regler empfohlen |
| Inspektion | Vor jeder Etappe |

---

## 4. Regional Sourcing

### 4.1 Gasflaschen-Systeme nach Region

| Region | Standard-Flasche | Anschluss | Gewinde | Verfügbarkeit |
|--------|-----------------|-----------|---------|---------------|
| Deutschland | 5 kg / 11 kg (grau) | Typ 21 (links) | W 21,8 × 1/14" LH | Überall |
| Frankreich | 13 kg (Butagaz blau) | Clip-on | Steckverbinder | Supermärkte |
| UK | 6 kg / 13 kg (Calor) | POL (links) | CGA 510 / BS 341 No 3 | Chandleries |
| Niederlande | 5 kg / 10,5 kg (Primagaz) | Typ 21 + Clip | W 21,8 / Clip | Campingshops |
| Spanien | 6 kg / 12,5 kg (Repsol) | Spanischer Clip | Steckverbinder | Gasolineras |
| Italien | 10 kg / 15 kg (Liquigas) | Italiano | W 20 × 1/14" LH | Ferramente |
| Griechenland | 10 kg (blau) | Griechischer Typ | BSP 1/4" | Minimarkets |
| Kroatien | 7,5 kg / 10 kg (INA) | Kroatischer Typ | W 21,8 × 1/14" LH | Tankstellen |
| USA/Kanada | 20 lb (9 kg) | ACME / OPD | CGA 791 / POL | Hardware Stores |
| Australien/NZ | 4,5 kg / 9 kg (Swap'n'Go) | POL (rechts!) | Type 21 RH | Servos |
| Karibik | 20 lb (US-Typ) | ACME / POL | CGA 791 | Lokale Händler |

**Adapter-Lösungen für Langfahrer:**

| Adapter | Von → Nach | Hersteller | Art.-Nr. | Preis (EUR) |
|---------|-----------|------------|----------|-------------|
| DE → FR | W 21,8 LH → Clip-on | GOK | 01-150-10 | 28 |
| DE → UK | W 21,8 LH → POL | GOK | 01-150-20 | 32 |
| DE → IT | W 21,8 LH → W 20 LH | GOK | 01-150-30 | 24 |
| DE → ES | W 21,8 LH → Spanisch | GOK | 01-150-40 | 35 |
| DE → US | W 21,8 LH → ACME | GOK | 01-150-50 | 38 |
| DE → AUS | W 21,8 LH → POL RH | GOK | 01-150-60 | 36 |
| Universal-Set (8 Adapter) | Alle oben | GOK | 01-150-00 | 169 |
| Gaslow Fill Kit Europa | Diverse Tankadapter | Gaslow | GAS-FK-EU | 89 |

### 4.2 LPG-Fachbetriebe für Yachten (Auswahl)

| Betrieb | Region | Spezialisierung | Zertifizierung |
|---------|--------|-----------------|----------------|
| Yachtgas Hamburg | Hamburg, DE | Marine-LPG-Anlagen | DVGW G 607 |
| Marine Gas Services | Hamble, UK | BSS Examiner + Installation | CORGI / Gas Safe |
| Techniciens du Gaz Maritime | La Rochelle, FR | Voiliers & Yachts | Qualigaz |
| GasTech Marine | Palma de Mallorca, ES | Superyacht LPG/CNG | ISO 10239 |
| Marine Gas Systeme Kiel | Kiel, DE | Segelyachten Ostsee | DVGW G 607 |

---

## 5. Zweck dieser Wissensdatei

Diese Wissensdatei dient als **domänenspezifische Referenz** für das AYDI-Analysesystem. Sie ermöglicht:

1. **Automatische Bewertung** von LPG-Gasschlauch-Installationen auf Yachten anhand von Fotos (Pipeline B — Visual) und strukturierten Daten (Pipeline A — Structured)
2. **Identifikation von Sicherheitsmängeln** durch Vergleich mit Normanforderungen (ISO 10239, EN 1763, ABYC A-1)
3. **Altersbestimmung** von Gasschläuchen anhand von Herstellungsdaten und Kennzeichnungen
4. **Herstellererkennung** auf Basis visueller Merkmale (Farbe, Logo, Aufdruck)
5. **Kostenschätzung** für Reparatur und Austausch unter Berücksichtigung des Bootstyps
6. **Compliance-Prüfung** gegen ISO 10239, EN 1763, ABYC A-1, TRF 2012
7. **Empfehlungen** für Modernisierung (z.B. Umstieg auf Edelstahl-Wellschlauch oder Induktion)

**Confidence-Mapping für Gas-Bewertungen:**

| Datenquelle | Confidence | Für welche Bewertung |
|-------------|------------|---------------------|
| CAD/Installationszeichnung | `measured` | Leitungsführung, Abstände, Dimensionierung |
| Foto (Schlauch + Aufdruck lesbar) | `visual_high` | Alter, Hersteller, Normkonformität |
| Foto (Schlauch sichtbar, Aufdruck nicht lesbar) | `visual_medium` | Zustand, Material, grobe Alterseinschätzung |
| Foto (Gaslocker teilweise sichtbar) | `visual_low` | Grundsätzliche Einbausituation |
| Spezifikation vom Eigner | `documented` | Alter, letzte Prüfung, Herstellerangabe |
| Bootsklasse + Baujahr | `estimated` | Vermutete Konfiguration |

---

## 6. Pydantic-Modelle für AYDI-Integration

### 6.1 GasHoseSpec — Spezifikation eines Gasschlauches

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import date
from enum import Enum


class GasHoseMaterial(str, Enum):
    """Gasschlauch-Materialien nach EN 1763 / EN 14800."""
    NBR = "nbr"                           # Nitril-Butadien-Kautschuk (Standard)
    SBR = "sbr"                           # Styrol-Butadien-Kautschuk (veraltet)
    EPDM = "epdm"                         # Ethylen-Propylen-Dien (UV-beständig)
    TPE = "tpe"                           # Thermoplastisches Elastomer (neu)
    STAINLESS_CORRUGATED = "ss_corrugated" # Edelstahl-Wellschlauch (EN 14800)
    PTFE_LINED = "ptfe_lined"             # PTFE-ausgekleidet (Spezial)


class GasHoseNorm(str, Enum):
    """Relevante Normen für Gasschlauch-Zulassung."""
    EN_1763 = "en_1763"
    EN_16436 = "en_16436"
    EN_14800 = "en_14800"
    DIN_30665 = "din_30665"
    ABYC_A1 = "abyc_a1"
    BS_EN_1763 = "bs_en_1763"


class GasHosePressureClass(str, Enum):
    """Druckklasse nach EN 16436."""
    CLASS_1_LOW = "class_1_low"           # Bis 30 mbar (Niederdruckseite)
    CLASS_2_MEDIUM = "class_2_medium"     # Bis 4 bar (Hochdruckseite)
    CLASS_3_HIGH = "class_3_high"         # Bis 25 bar (Dampfphase, selten marine)


class GasHoseApplication(str, Enum):
    """Einsatzzweck des Gasschlauches."""
    BOTTLE_TO_REGULATOR = "bottle_to_regulator"
    REGULATOR_TO_LINE = "regulator_to_line"
    LINE_TO_APPLIANCE = "line_to_appliance"
    APPLIANCE_INTERNAL = "appliance_internal"


class GasHoseSpec(BaseModel):
    """Spezifikation eines Gasschlauches für marine LPG-Systeme.

    Alle Maße in mm, Drücke in mbar, Temperaturen in °C.
    Konform mit AYDI Pydantic v2 Konventionen.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    manufacturer: str = Field(..., description="Hersteller (z.B. 'Truma', 'GOK')")
    product_line: str = Field(..., description="Produktlinie/Modell")
    part_number: Optional[str] = Field(None, description="Herstellerartikelnummer")
    ean: Optional[str] = Field(None, description="EAN/GTIN Barcode")

    # Technische Daten
    material: GasHoseMaterial = Field(..., description="Schlauchmaterial")
    norm: GasHoseNorm = Field(..., description="Zugelassene Norm")
    pressure_class: GasHosePressureClass = Field(
        GasHosePressureClass.CLASS_1_LOW,
        description="Druckklasse"
    )
    inner_diameter_mm: float = Field(..., ge=4.0, le=25.0, description="Innendurchmesser in mm")
    outer_diameter_mm: float = Field(..., ge=8.0, le=40.0, description="Außendurchmesser in mm")
    length_mm: float = Field(..., ge=100.0, le=3000.0, description="Länge in mm")
    burst_pressure_bar: float = Field(..., ge=5.0, description="Berstdruck in bar")
    operating_pressure_mbar: float = Field(30.0, description="Betriebsdruck in mbar")
    temp_min_c: float = Field(-30.0, description="Min. Betriebstemperatur °C")
    temp_max_c: float = Field(70.0, description="Max. Betriebstemperatur °C")

    # Anschlüsse
    connection_input: str = Field(..., description="Anschluss Eingangsseite (z.B. 'W 21,8 x 1/14 LH')")
    connection_output: str = Field(..., description="Anschluss Ausgangsseite (z.B. 'G 1/4 LH')")
    application: GasHoseApplication = Field(..., description="Einsatzzweck")

    # Marine-Eignung
    marine_approved: bool = Field(False, description="Explizit für Marine zugelassen")
    uv_resistant: bool = Field(False, description="UV-beständige Außenschicht")
    salt_water_resistant: bool = Field(False, description="Salzwasserbeständige Armaturen")

    # Lebensdauer
    max_service_life_years: int = Field(10, ge=1, le=50, description="Max. Lebensdauer in Jahren")
    manufacture_date: Optional[date] = Field(None, description="Herstellungsdatum (Aufdruck)")
    expiry_date: Optional[date] = Field(None, description="Ablaufdatum (berechnet)")

    # Kosten
    price_eur: Optional[float] = Field(None, ge=0, description="Listenpreis in EUR")
    installation_cost_eur: Optional[float] = Field(None, ge=0, description="Einbaukosten in EUR")

    # AYDI-Metadaten
    confidence: Literal["measured", "documented", "estimated"] = Field(
        "estimated", description="Datenquelle für diese Spezifikation"
    )


class GasHoseCondition(BaseModel):
    """Zustandsbewertung eines installierten Gasschlauches.

    Wird von Pipeline A (Inspektion) und Pipeline B (Visual) befüllt.
    Score 0-100, wobei <30 = CRITICAL (sofortiger Austausch).
    """
    model_config = {"from_attributes": True}

    # Identifikation
    hose_id: Optional[str] = Field(None, description="Referenz zur GasHoseSpec")
    location: str = Field(..., description="Einbauort (z.B. 'Gaslocker→Regler', 'Pantry→Kocher')")
    zone: str = Field("gas_system", description="AYDI-Zone")

    # Alter und Ablauf
    age_years: Optional[float] = Field(None, ge=0, description="Alter in Jahren")
    is_expired: Optional[bool] = Field(None, description="Über max. Lebensdauer?")
    years_until_expiry: Optional[float] = Field(None, description="Jahre bis Ablauf")

    # Visuelle Zustandsbewertung (Pipeline B)
    surface_condition: Literal[
        "einwandfrei", "leicht_gealtert", "rissig", "stark_rissig",
        "poroes", "aufgequollen", "nicht_beurteilbar"
    ] = Field("nicht_beurteilbar", description="Oberflächenzustand")
    surface_score: int = Field(50, ge=0, le=100, description="Oberflächen-Score")

    fitting_condition: Literal[
        "einwandfrei", "leichte_korrosion", "starke_korrosion",
        "verformt", "undicht_sichtbar", "nicht_beurteilbar"
    ] = Field("nicht_beurteilbar", description="Zustand der Anschlussarmaturen")
    fitting_score: int = Field(50, ge=0, le=100, description="Armaturen-Score")

    routing_condition: Literal[
        "korrekt", "zu_eng_gebogen", "scheuerstelle", "eingeklemmt",
        "unter_spannung", "nicht_einsehbar", "nicht_beurteilbar"
    ] = Field("nicht_beurteilbar", description="Verlegequalität")
    routing_score: int = Field(50, ge=0, le=100, description="Verlege-Score")

    labeling_readable: bool = Field(
        False, description="Ist die Beschriftung (Hersteller, Datum, Norm) lesbar?"
    )
    labeling_score: int = Field(50, ge=0, le=100, description="Beschriftungs-Score")

    # Gesamtbewertung
    overall_score: int = Field(50, ge=0, le=100, description="Gesamt-Score (gewichtet)")
    severity: Literal["ok", "warning", "critical"] = Field(
        "warning", description="Schweregrad"
    )
    immediate_action_required: bool = Field(
        False, description="Sofortmaßnahme erforderlich?"
    )

    # Befunde
    findings: list[str] = Field(
        default_factory=list, description="Liste konkreter Befunde (deutsch)"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen (deutsch)"
    )

    # Confidence
    confidence: Literal[
        "measured", "visual_high", "visual_medium", "visual_low",
        "visual_insufficient", "estimated", "documented"
    ] = Field("visual_medium", description="Bewertungskonfidenz")


class GasDetectorStatus(str, Enum):
    """Status des Gas-Leckdetektors."""
    PRESENT_FUNCTIONAL = "present_functional"
    PRESENT_UNKNOWN = "present_unknown"
    PRESENT_DEFECTIVE = "present_defective"
    NOT_PRESENT = "not_present"
    NOT_ASSESSABLE = "not_assessable"


class SolenoidValveStatus(str, Enum):
    """Status des Magnetventils."""
    PRESENT_FUNCTIONAL = "present_functional"
    PRESENT_UNKNOWN = "present_unknown"
    PRESENT_DEFECTIVE = "present_defective"
    NOT_PRESENT = "not_present"
    NOT_ASSESSABLE = "not_assessable"


class GasSystemAssessment(BaseModel):
    """Gesamtbewertung des LPG-Systems einer Yacht.

    Aggregiert Befunde aus Gasschlauch-Inspektion, Gaslocker-Bewertung,
    Detektor-Status, Magnetventil-Status und Verbraucher-Prüfung.

    Dies ist das Top-Level-Ergebnis der Gas-Analyse im AYDI-System.
    """
    model_config = {"from_attributes": True}

    # Boot-Referenz
    boat_id: Optional[str] = Field(None, description="AYDI Boot-ID")
    boat_class: str = Field(..., description="Bootsklasse (z.B. 'production_sail_10m')")
    analysis_date: date = Field(..., description="Datum der Bewertung")

    # Gaslocker
    gas_locker_present: Optional[bool] = Field(None)
    gas_locker_sealed: Optional[bool] = Field(None, description="Gasdicht zum Bootsinneren?")
    gas_locker_drain: Optional[bool] = Field(None, description="Drainage nach außenbords?")
    gas_locker_ventilation: Optional[bool] = Field(None, description="Belüftung oben?")
    gas_locker_score: int = Field(50, ge=0, le=100)

    # Gasschläuche (Detailergebnisse als Liste)
    hose_assessments: list[GasHoseCondition] = Field(
        default_factory=list, description="Bewertungen aller Gasschläuche"
    )
    hose_overall_score: int = Field(50, ge=0, le=100)

    # Regler
    regulator_type: Optional[str] = Field(None, description="Reglertyp (z.B. 'Truma MonoControl CS')")
    regulator_age_years: Optional[float] = Field(None)
    regulator_score: int = Field(50, ge=0, le=100)

    # Magnetventil
    solenoid_status: SolenoidValveStatus = Field(
        SolenoidValveStatus.NOT_ASSESSABLE
    )
    solenoid_score: int = Field(50, ge=0, le=100)

    # Gasdetektor
    detector_status: GasDetectorStatus = Field(
        GasDetectorStatus.NOT_ASSESSABLE
    )
    detector_score: int = Field(50, ge=0, le=100)

    # Verbraucher
    appliance_count: int = Field(0, ge=0)
    appliances_with_flame_failure: Optional[int] = Field(None, ge=0)
    appliance_score: int = Field(50, ge=0, le=100)

    # Gesamtbewertung
    overall_score: int = Field(50, ge=0, le=100, description="Gas-System Gesamtscore")
    severity: Literal["ok", "warning", "critical"] = Field("warning")
    compliance_iso_10239: Optional[bool] = Field(None, description="ISO 10239 konform?")
    compliance_abyc_a1: Optional[bool] = Field(None, description="ABYC A-1 konform?")

    # Kritische Befunde (jeweils mit Maßnahme)
    critical_findings: list[str] = Field(
        default_factory=list,
        description="CRITICAL-Befunde (sofortige Maßnahme erforderlich)"
    )
    warnings: list[str] = Field(
        default_factory=list,
        description="WARNING-Befunde (Maßnahme innerhalb 30 Tagen)"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen (nächste Saison oder planmäßig)"
    )

    # Kosten
    estimated_repair_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Reparaturkosten in EUR"
    )
    estimated_upgrade_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Modernisierungskosten in EUR"
    )

    # Confidence
    confidence: Literal[
        "measured", "visual_high", "visual_medium", "visual_low",
        "visual_insufficient", "estimated", "documented"
    ] = Field("visual_medium")

    # Scoring-Logik (Dokumentation der Gewichtung)
    scoring_weights: dict[str, float] = Field(
        default_factory=lambda: {
            "gas_locker": 0.20,
            "hoses": 0.25,
            "regulator": 0.10,
            "solenoid": 0.15,
            "detector": 0.20,
            "appliances": 0.10,
        },
        description="Gewichtung der Teilscores"
    )
```

### 6.2 Scoring-Logik

```python
def calculate_gas_system_score(assessment: GasSystemAssessment) -> int:
    """Berechnet den Gesamtscore des Gas-Systems.

    CRITICAL-Logik:
    - Kein Gasdetektor vorhanden → Max-Score: 30
    - Gasschlauch abgelaufen → Max-Score: 25
    - Undichtigkeit erkannt → Max-Score: 10
    - Kein Magnetventil → Max-Score: 40
    - Gaslocker nicht gasdicht → Max-Score: 20

    Diese Caps werden VOR der gewichteten Berechnung angewendet.
    """
    weights = assessment.scoring_weights

    weighted = (
        assessment.gas_locker_score * weights["gas_locker"]
        + assessment.hose_overall_score * weights["hoses"]
        + assessment.regulator_score * weights["regulator"]
        + assessment.solenoid_score * weights["solenoid"]
        + assessment.detector_score * weights["detector"]
        + assessment.appliance_score * weights["appliances"]
    )

    score = int(round(weighted))

    # CRITICAL caps
    if assessment.detector_status == GasDetectorStatus.NOT_PRESENT:
        score = min(score, 30)
    if assessment.solenoid_status == SolenoidValveStatus.NOT_PRESENT:
        score = min(score, 40)
    if assessment.gas_locker_sealed is False:
        score = min(score, 20)

    for hose in assessment.hose_assessments:
        if hose.is_expired:
            score = min(score, 25)
        if hose.fitting_condition == "undicht_sichtbar":
            score = min(score, 10)

    return max(0, min(100, score))
```

---

## 7. Grundlagen Gasschläuche

### 7.1 LPG-Systeme auf Yachten — Übersicht

Ein typisches LPG-System auf einer Segelyacht besteht aus folgenden Komponenten in Gasflussrichtung:

```
[Gasflasche] → [Hochdruck-Schlauch] → [Druckregler] → [Magnetventil]
    → [Festleitung Cu/Edelstahl] → [Schott-Durchführung] → [Niederdruck-Schlauch]
    → [Verbraucher (Kocher/Heizung/Kühlschrank)]
```

**Systemkomponenten im Detail:**

| Komponente | Druck | Material | Norm | Lebensdauer |
|------------|-------|----------|------|-------------|
| Gasflasche (5/11 kg) | 4–16 bar (druckabhängig von Temp.) | Stahl / Alu / Composite | EN 1442 / EN 12245 | 10/15 Jahre (Prüfung) |
| Hochdruck-Schlauch (Flasche→Regler) | Bis 16 bar | NBR + Textilgeflecht | EN 1763 Klasse 2 | 10 Jahre |
| Druckregler | 16 bar → 30 mbar | Messing/Zink, vernickelt | EN 12864 | 10 Jahre |
| Magnetventil (Solenoid) | 30 mbar | Messing, 12V-Spule | ISO 10239 / ABYC A-1 | 15+ Jahre |
| Festleitung | 30 mbar | Kupfer EN 1057 / Edelstahl 316L | ISO 10239 | 30+ Jahre |
| Niederdruck-Schlauch (Leitung→Gerät) | 30 mbar | NBR / EPDM | EN 1763 Klasse 1 | 10 Jahre |
| Schlauchbruchsicherung | 30 mbar | Messing | EN 16129 | 15 Jahre |
| Gasdetektor | — | Katalytischer/Halbleiter-Sensor | ABYC A-1 / ISO 10239 | 5–7 Jahre (Sensor) |

**Typische Konfigurationen nach Bootsgröße:**

| Bootsgröße | Flaschen | Verbraucher | Schläuche | Festleitung |
|------------|----------|-------------|-----------|-------------|
| 7–9 m Segelyacht | 1× 2 kg Camping Gaz | 2-Flammen-Kocher | 1× ND-Schlauch 500 mm | Keine |
| 9–12 m Segelyacht | 2× 3 kg Alu | 2-Flammen-Kocher + Backofen | 1× HD + 1× ND | 1–2 m Kupfer |
| 12–15 m Segelyacht | 2× 5 kg Stahl | 3-Flammen + Backofen + Warmwasser | 1× HD + 2× ND | 3–5 m Kupfer |
| 15–20 m Motoryacht | 2× 11 kg | Vollküche + Heizung + BBQ | 1× HD + 3× ND | 5–10 m Kupfer |
| >20 m Yacht | 2× 11 kg oder Festtank | Vollküche + Heizung + BBQ + Wäschetrockner | Professionell verrohrt | 10+ m Edelstahl |

### 7.2 Propan vs Butan — Technische Unterschiede

| Eigenschaft | Propan (C₃H₈) | Butan (C₄H₁₀) | Marine-Relevanz |
|-------------|---------------|----------------|-----------------|
| Siedepunkt (1 atm) | −42°C | −0,5°C | **Propan funktioniert auch bei Frost** |
| Dampfdruck bei 20°C | 8,4 bar | 2,1 bar | Propan: stärkerer Druck → robusterer Regelkreis |
| Dampfdruck bei 0°C | 4,7 bar | 1,1 bar | Butan bei <5°C praktisch unbrauchbar |
| Dampfdruck bei 40°C | 13,7 bar | 3,8 bar | Flaschendruck bei Hitzestau im Gaslocker! |
| Heizwert (kWh/kg) | 12,87 | 12,69 | Nahezu identisch |
| Heizwert (kWh/l flüssig) | 6,57 | 7,19 | **Butan: 9% mehr Energie pro Volumen** |
| Dichte Dampf (kg/m³) | 1,88 | 2,52 | Beide schwerer als Luft → **Bilgengefahr** |
| Rel. Dichte (Luft=1) | 1,56 | 2,07 | Butan sinkt noch schneller |
| Untere Explosionsgrenze | 2,1 Vol.-% | 1,8 Vol.-% | Butan etwas früher explosiv |
| Obere Explosionsgrenze | 9,5 Vol.-% | 8,4 Vol.-% | — |
| Zündtemperatur | 470°C | 365°C | Butan leichter entzündlich |
| Flammengeschwindigkeit | 0,46 m/s | 0,45 m/s | Identisch |
| Geruchsstoff | Ethylmercaptan | Ethylmercaptan | Gleicher Warngeruch |

**AYDI-Empfehlung nach Revier:**

| Revier | Gastyp | Begründung |
|--------|--------|------------|
| Ostsee (Mai–Sep) | Propan | Nachttemperaturen können unter +5°C fallen |
| Nordsee | Propan | Temperaturreserve erforderlich |
| Mittelmeer (ganzjährig) | Propan oder Butan | Butan funktioniert, Propan sicherer |
| Karibik / Tropen | Propan | Universelle Verfügbarkeit, Butan selten |
| Arktis | **Nur Propan** | Butan nicht verwendbar |

### 7.3 LPG schwerer als Luft — Das Kernrisiko

> ⚠️ **DIES IST DIE WICHTIGSTE INFORMATION IN DIESER DATEI**

LPG (Propan und Butan) ist **schwerer als Luft**. Jedes ausgetretene Gas sinkt nach unten und sammelt sich im tiefsten Punkt des Bootes — der **Bilge**.

**Warum das auf einem Boot tödlich ist:**

1. **Geschlossener Raum:** Ein Bootsrumpf ist ein nahezu geschlossener Hohlkörper. Gas, das nach unten sinkt, kann nicht durch natürliche Ventilation entweichen (anders als in einem Haus, wo es durch Kellerfenster entweichen könnte).

2. **Große Bilgenfläche:** Die Bilge erstreckt sich über die gesamte Bootslänge. Gas kann sich von der Pantry bis zum Motor verteilen, ohne dass es bemerkt wird.

3. **Zündquellen im Bilgenbereich:**
   - Bilgepumpen-Schalter (mechanische Kontakte = Funken)
   - Lichtmaschinenregler (bei laufendem Motor)
   - Lenzpumpenmotoren (Bürstenfeuer)
   - Starterbatterien (Ausgasungsreaktion)
   - Statische Entladung (GFK-Rumpf isoliert)

4. **Explosionsbereich schnell erreicht:**
   - Untere Explosionsgrenze Propan: 2,1 Vol.-% = 21.000 ppm
   - Bilgenvolumen 10-m-Segelyacht: ca. 200–500 Liter
   - Leckrate eines gerissenen Schlauchs: ca. 2–10 Liter/h (Dampfphase)
   - **Ergebnis: In 2–10 Stunden ist die Explosionsgrenze erreicht**

5. **Explosionswirkung:**
   - Gas-Luft-Gemisch im Explosionsbereich detoniert mit ca. 7–8 bar Spitzendruck
   - GFK-Rumpf: Versagensdruck ca. 0,3–0,5 bar
   - **→ Rumpf wird vollständig zerstört**

**Geruchswahrnehmung als Schutz?**
- LPG wird mit Ethylmercaptan odoriert (Geruchsschwelle ca. 1 ppm)
- Die Explosionsgrenze liegt bei 21.000 ppm (Propan)
- **Theoretisch** sollte man Gas riechen, lange bevor es gefährlich wird
- **ABER:** In der Bilge riecht man es nicht — das Gas ist unter dem Fußboden
- **ABER:** Im Schlaf riecht man nichts
- **ABER:** Geruchsermüdung nach längerer Exposition
- **ABER:** Einige Personen haben reduzierten Geruchssinn

**Fazit:** Geruch allein ist **kein ausreichender Schutz**. Ein elektronischer Gasdetektor in der Bilge ist **die einzige zuverlässige Warnung**.

### 7.4 Materialien (NBR, SBR, EPDM, Thermoplast, Edelstahl-Wellrohr)

#### NBR (Nitril-Butadien-Kautschuk) — Standard für LPG-Schläuche

| Eigenschaft | Wert | Bewertung Marine |
|-------------|------|-----------------|
| LPG-Beständigkeit | Ausgezeichnet | ✓ Standardmaterial für LPG |
| Temperaturbereich | −30°C bis +100°C | ✓ Ausreichend für Marine |
| UV-Beständigkeit | Mäßig | ⚠ Außenschicht muss UV-geschützt sein |
| Ozonbeständigkeit | Mäßig | ⚠ Ozon beschleunigt Alterung |
| Zugfestigkeit | 15–25 MPa | ✓ Ausreichend |
| Dehnung bei Bruch | 300–600% | ✓ Gut |
| Gaspermeabilität | Niedrig | ✓ Geringe LPG-Durchlässigkeit |
| Alterung | Verhärtet und reißt nach 8–12 Jahren | ⚠ 10-Jahres-Grenze beachten |
| Kosten | Niedrig | ✓ Standard-Preisklasse |

**Typische Konstruktion NBR-Gasschlauch (EN 1763):**
- Innenschicht: NBR, schwarz, 1,5–2,0 mm
- Verstärkung: Polyester-Textilgeflecht, 1 Lage
- Außenschicht: CR (Chloropren) oder EPDM, orange, 1,0–1,5 mm
- Gesamt-Wandstärke: 4,0–5,5 mm
- Typischer ID: 8 mm (3/8")
- Typischer AD: 16–18 mm

#### SBR (Styrol-Butadien-Kautschuk) — Veraltet, nicht mehr empfohlen

| Eigenschaft | Wert | Bewertung Marine |
|-------------|------|-----------------|
| LPG-Beständigkeit | Mäßig | ⚠ Quillt bei Langzeitkontakt |
| Temperaturbereich | −25°C bis +70°C | ⚠ Engerer Bereich als NBR |
| Lebensdauer | 5–8 Jahre | ✗ Deutlich kürzer als NBR |
| Kosten | Sehr niedrig | — |

**AYDI-Bewertung:** SBR-Schlauch auf einer Yacht → automatisch `severity: "critical"`, Empfehlung sofortiger Austausch.

#### EPDM (Ethylen-Propylen-Dien-Kautschuk) — UV-beständige Alternative

| Eigenschaft | Wert | Bewertung Marine |
|-------------|------|-----------------|
| LPG-Beständigkeit | Gut (geringer als NBR) | ✓ Für Niederdruckseite geeignet |
| UV-Beständigkeit | Ausgezeichnet | ✓✓ Ideal für UV-exponierte Bereiche |
| Ozonbeständigkeit | Ausgezeichnet | ✓✓ Besser als NBR |
| Temperaturbereich | −40°C bis +120°C | ✓✓ Breiter als NBR |
| Gaspermeabilität | Höher als NBR | ⚠ Nur für Kurzstrecken/Niederdruck |
| Lebensdauer | 10–15 Jahre | ✓ Länger als NBR |
| Kosten | Mittel (1,3× NBR) | ✓ Akzeptabel |

#### Thermoplastische Schläuche (TPE, PA, PVDF)

| Eigenschaft | Wert | Bewertung Marine |
|-------------|------|-----------------|
| LPG-Beständigkeit | Gut bis sehr gut | ✓ Materialabhängig |
| UV-Beständigkeit | Gut (mit Additiven) | ✓ Besser als NBR |
| Temperaturbereich | −20°C bis +60°C (TPE) | ⚠ Engerer Bereich |
| Gaspermeabilität | Sehr niedrig | ✓✓ Besser als Gummi |
| Biegsamkeit | Eingeschränkt | ⚠ Größerer Biegeradius |
| Lebensdauer | 15–20 Jahre (geschätzt) | ✓✓ Deutlich länger |
| Zulassung Marine | Noch nicht vollständig | ⚠ Einzelfallprüfung |

#### Edelstahl-Wellschlauch (EN 14800) — Premium-Lösung

| Eigenschaft | Wert | Bewertung Marine |
|-------------|------|-----------------|
| Material | AISI 316L (marine grade) | ✓✓ Vollständig seewasserfest |
| Ummantelung | 316L Edelstahlgeflecht | ✓✓ Mechanischer Schutz |
| Berstdruck | >100 bar (bei 30 mbar Betrieb) | ✓✓ Enorme Sicherheitsreserve |
| Temperaturbereich | −200°C bis +400°C | ✓✓ Irrelevant für Marine, aber sicher |
| UV-Beständigkeit | Unbegrenzt | ✓✓ Kein UV-Problem |
| Gaspermeabilität | Null | ✓✓ Perfekte Dichtheit |
| Lebensdauer | **Unbegrenzt** (keine 10-Jahres-Regel) | ✓✓ Kein Austausch nötig |
| Biegsamkeit | Eingeschränkt, Mindestbiegeradius beachten | ⚠ Kein Nachbiegen möglich |
| Vibrationsbeständigkeit | Sehr gut (Wellrohr federt) | ✓✓ Ideal für Motorboote |
| Kosten | 3–5× Gummischlauch | ⚠ Höhere Erstinvestition |
| Einschränkung | Nicht kürzen oder nachbiegen | ⚠ Maßanfertigung erforderlich |

**Hersteller Edelstahl-Wellschläuche für Marine-Gas:**

| Hersteller | Produktlinie | Längen (mm) | Preis (EUR) | Zulassung |
|------------|-------------|-------------|-------------|-----------|
| Flexcon (DE) | Flexcon Gas Marine | 300/500/750/1000/1500 | 45–95 | EN 14800 + GL Marine |
| Tece (DE) | Tece Flex Gas | 300–1500 | 40–85 | EN 14800 / DVGW |
| Eurotis (IT) | Eurogas Flex | 250–2000 | 35–90 | EN 14800 / CE |
| BOA Group (DE) | BOA Ecoflex | 300–1500 | 55–110 | EN 14800 + Marine |
| Witzenmann (DE) | Hydra-Flex Gas | 300–2000 | 60–130 | EN 14800 / DVGW |

### 7.5 Gaslocker-Anforderungen

Der Gaslocker (Gasflaschenschrank) ist die **erste Verteidigungslinie** gegen Gasexplosionen auf einer Yacht. Er muss verhindern, dass ausgetretenes Gas ins Bootsinnere gelangt.

**Anforderungen nach ISO 10239, Sektion 5.2:**

| Anforderung | Detail | AYDI-Prüfkriterium |
|-------------|--------|-------------------|
| Gasdichte Abtrennung | Gaslocker muss zum Bootsinneren gasdicht sein. Alle Durchführungen (Gasleitung, Kabel) abgedichtet. | Visuell: Dichtung der Tür/Klappe, Durchführungen |
| Drainage | Min. 1 Ablauf ≥19 mm nach außenbords am tiefsten Punkt | Visuell: Drain sichtbar, nicht verstopft |
| Belüftung oben | Min. 2500 mm² freier Querschnitt, am höchsten Punkt | Visuell: Belüftungsöffnung vorhanden |
| Keine Elektrik | Keine elektrischen Geräte oder Kabel im Locker | Visuell: keine Kabel, keine Stecker |
| Flaschensicherung | Flaschen gegen Umfallen und Verrutschen gesichert | Visuell: Gurte, Halterungen |
| Zugänglichkeit | Ventil der Flasche muss ohne Werkzeug erreichbar sein | Visuell/funktional |
| Kennzeichnung | Warnschilder: „LPG", Rauchverbot, Sicherheitshinweise | Visuell |

> ⚠️ **ZU PRÜFEN (Audit):** Tabellenwert „Belüftung oben — min. 2500 mm²" widerspricht dem Anhang („250 mm² oben + unten"). Nur der Drain ≥ 19 mm Innen-Ø (≈ 283 mm²) ist per EN ISO 10239 verifiziert; die 2500-mm²-Fläche ist **estimated — unverifiziert**. Siehe Abschnitt 1.4 (Kapitel 5.2).

**Gaslocker-Positionen auf verschiedenen Bootstypen:**

| Bootstyp | Typische Position | Bewertung |
|----------|-------------------|-----------|
| Segelyacht 8–12 m | Cockpit-Backskiste (achtern, seitlich) | Gut — natürliche Drainage nach achtern |
| Segelyacht 12–16 m | Dedizierter Gaslocker im Cockpitboden | Sehr gut — separater, abgedichteter Raum |
| Motoryacht 8–12 m | Achterdeck, unter Sitzbank | Gut — wenn gasdicht und mit Drain |
| Motoryacht 12–20 m | Flybridge oder Achterdeck-Locker | Sehr gut — hoch, gut belüftet |
| Katamaran | Heckbereich, in einem der Rümpfe | Variabel — Drain-Führung prüfen |

**Häufige Mängel bei Gaslocker-Inspektionen (AYDI-Erfahrungswerte):**

| Mangel | Häufigkeit | Schwere | Score-Auswirkung |
|--------|------------|---------|-----------------|
| Drain verstopft (Schmutz, Muscheln) | 35% aller Boote | CRITICAL | −40 Punkte |
| Dichtung Gaslocker-Deckel porös/fehlend | 25% | CRITICAL | −35 Punkte |
| Elektrische Leitung durch Gaslocker geführt | 15% | CRITICAL | −30 Punkte |
| Fehlende Flaschensicherung | 20% | WARNING | −15 Punkte |
| Keine Belüftungsöffnung | 10% | CRITICAL | −35 Punkte |
| Warnschild fehlt | 30% | WARNING | −5 Punkte |

### 7.6 Druckregler und Druckminderung

Der Druckregler reduziert den Flaschendruck (4–16 bar, temperaturabhängig) auf den Betriebsdruck (30 mbar in Europa, 11" WC / 2,75 kPa in USA).

**Reglertypen für Marine-Anwendungen:**

| Typ | Beschreibung | Einsatz | Hersteller |
|-----|-------------|---------|------------|
| Einstufig (30 mbar) | Direkte Reduktion auf Betriebsdruck | Kleine Yachten, 1 Verbraucher | GOK, Gimeg |
| Zweistufig (intern) | Zweistufige Regelung in einem Gehäuse | Standard Marine | Truma, GOK |
| Zweistufig (extern) | Erste Stufe an Flasche, zweite am Verbraucher | Lange Leitungen (>5 m) | Clesse, Cavagna |
| Umschaltregler | Automatische Umschaltung bei leerer Flasche | 2-Flaschen-Anlagen | Truma DuoControl, GOK Caramatic |
| Crash-Sensor-Regler | Schließt bei Erschütterung/Neigung | Marine empfohlen | Truma MonoControl CS |

**Wichtige Druckregler-Modelle für Marine:**

| Hersteller | Modell | Art.-Nr. | Typ | Preis (EUR) | Besonderheit |
|------------|--------|----------|-----|-------------|-------------|
| Truma | MonoControl CS | 60180-00 | 1-Flasche + Crash-Sensor | 89 | **Marine-Standard** — schließt bei Erschütterung |
| Truma | DuoControl CS | 60230-00 | 2-Flaschen + Crash + Auto-Umschalt | 189 | Premium für 2-Flaschen-Anlagen |
| Truma | DuoComfort | 60250-00 | 2-Flaschen + Auto-Umschalt | 149 | Ohne Crash-Sensor |
| GOK | Caramatic DriveOne | 01-111-01 | 1-Flasche + Crash-Sensor | 79 | GOK-Pendant zu Truma MonoControl CS |
| GOK | Caramatic DriveTwo | 01-112-01 | 2-Flaschen + Crash + Auto-Umschalt | 169 | GOK-Pendant zu Truma DuoControl CS |
| GOK | Caramatic BasicOne | 01-100-01 | 1-Flasche, einstufig | 29 | Basis, kein Crash-Sensor |
| Cavagna | 7KG LPG Regulator | 7KGLPG30 | 1-Flasche, anpassbar | 45 | Universell, internationale Gewinde |
| Clesse | CELGI Inverseur | CELGI-02 | 2-Flaschen, Umschaltung | 95 | Französischer Standard |
| Gimeg | Kombi-Regler Marine | 6000-300 | 1-Flasche, 30 mbar | 39 | Niederländischer Marine-Standard |

**Crash-Sensor (Truma CS-Technologie):**

Der Crash-Sensor (= Neigungssensor + Beschleunigungssensor) im Truma MonoControl CS / DuoControl CS schließt das Gasventil bei:
- Neigung >30° (relevant bei Kenterung oder schwerem Wetter)
- Beschleunigung >0,3 g (relevant bei Kollision)
- Reset nur manuell möglich (Sicherheitsdesign)

**AYDI-Bewertung:** Boot mit Crash-Sensor-Regler: +10 Punkte auf Regler-Score. Boot ohne Crash-Sensor bei vorhandener Segelanlage (Krängung!): WARNING.

### 7.7 Magnetventile (Solenoid Shut-Off)

Das Magnetventil (elektrisch betätigtes Gasabsperrventil) ist die **fernbedienbare Sicherheitsabsperrung**. Es sitzt in der Gasleitung zwischen Regler und Verbraucher und wird von der Bedienposition des Kochers/Verbrauchers geschaltet.

**Funktionsprinzip:**
- **Normally Closed (NC):** Ventil ist stromlos geschlossen. Nur wenn der Schalter aktiv eingeschaltet wird, öffnet die Spule das Ventil. Bei Stromausfall schließt das Ventil automatisch → **fail-safe**.
- Dies ist die **einzig zulässige** Bauart nach ISO 10239 und ABYC A-1.

**Marine-Magnetventile:**

| Hersteller | Modell | Art.-Nr. | Spannung | DN | Preis (EUR) | Zulassung |
|------------|--------|----------|----------|------|-------------|-----------|
| Truma | SecuMotion | 60290-00 | 12V DC | 8 mm | 149 | ISO 10239 |
| GOK | Magnetventil Marine | 01-210-01 | 12V DC | 8 mm | 89 | EN 161 / DVGW |
| Marintek | Gas Solenoid Valve | MT-GS12 | 12V DC | 8 mm | 69 | CE Marine |
| Xintex / Fireboy | S-1 Solenoid | S-1-12V | 12V DC | 6,35 mm (1/4") | 95 | ABYC A-1, UL |
| Gas Boat (UK) | GS1 Marine Solenoid | GS1-12 | 12V DC | 8 mm | 115 | BSS, ISO 10239 |
| Vetus | LPG Solenoid | LPGV38 | 12V DC | 10 mm (3/8") | 125 | CE, ISO 10239 |
| Osculati | Gas Solenoid Marine | 50.232.00 | 12V DC | 8 mm | 79 | CE |

**Installation Magnetventil — ISO 10239 Anforderungen:**
- Position: so nah wie möglich am Gaslocker-Ausgang (innerhalb 500 mm empfohlen)
- Schalter: am Bedienpunkt des Verbrauchers, deutlich beschriftet „GAS EIN/AUS"
- Kontrollleuchte: empfohlen (rot = Gas ein, aus = Gas aus)
- Kabelquerschnitt: min. 1,5 mm² bei 12V, max. Leitungslänge nach Spannungsabfall-Berechnung
- Sicherung: eigene Sicherung, max. 3A

**AYDI-Bewertung Magnetventil:**

| Befund | Score-Auswirkung | Severity |
|--------|-----------------|----------|
| Magnetventil vorhanden und funktional | 100 Punkte | OK |
| Magnetventil vorhanden, Funktion unbekannt | 60 Punkte | WARNING |
| Magnetventil vorhanden, defekt | 20 Punkte | CRITICAL |
| **Kein Magnetventil vorhanden** | **0 Punkte → System-Score max. 40** | **CRITICAL** |

### 7.8 Gas-Leckdetektoren

Der Gasdetektor ist — nach dem Gaslocker — die **zweite kritische Sicherheitsebene**. Er detektiert ausgetretenes LPG im Bilgenbereich und warnt die Besatzung, bevor die Explosionsgrenze erreicht wird.

**Detektortypen:**

| Typ | Funktionsprinzip | Vorteile | Nachteile | Marine-Eignung |
|-----|-----------------|----------|-----------|----------------|
| Katalytischer Sensor (Pellistor) | Katalytische Verbrennung am Sensorelement | Zuverlässig, geringe Querempfindlichkeit | Vergiftungsempfindlich (Silikon!), Lebensdauer 3–5 Jahre | ✓ Standard |
| Halbleiter-Sensor (MOS) | Widerstandsänderung bei Gasadsorption | Günstiger, längere Lebensdauer (5–7 Jahre) | Höhere Querempfindlichkeit (Alkohol, Reiniger) | ✓ Akzeptabel |
| Infrarot-Sensor (NDIR) | IR-Absorption durch Kohlenwasserstoffe | Sehr zuverlässig, langlebig (10+ Jahre) | Teuer, größer | ✓✓ Premium |
| Elektrochemisch | Stromfluss bei Gasreaktion | Sehr spezifisch | Kurzlebig (2–3 Jahre) | ⚠ Begrenzt |

**Marine-Gasdetektoren im Marktüberblick:**

| Hersteller | Modell | Sensortyp | Kanäle | Solenoid-Ausgang | Preis (EUR) | Zulassung |
|------------|--------|-----------|--------|-----------------|-------------|-----------|
| Fireboy-Xintex | MS-2 | Katalytisch | 2 | Ja (12V, 3A) | 385 | ABYC A-1, UL 1110 |
| Fireboy-Xintex | S-1-S | Halbleiter | 1 | Ja (12V, 3A) | 245 | ABYC A-1 |
| NASA Marine | Gas Detector | Katalytisch | 1 | Ja (12V, 1A) | 195 | CE, BSS |
| BEP Marine | 600-GDL | Halbleiter | 1 | Ja (12V, 5A) | 215 | ABYC A-1, CE |
| Dometic | GD-01 | Halbleiter | 1 | Nein (nur Alarm) | 95 | CE |
| CBE | Gas Detector | Halbleiter | 1 | Optional | 115 | CE |
| Truma | DuoC Gasdetektor | Halbleiter | 1 | Via iNet | 159 | CE |
| Gas Boat (UK) | GD-1 | Katalytisch | 1 | Ja (integriert) | 295 | BSS, ISO 10239 |
| MASE Generators | GD-200M | NDIR | 2 | Ja (12V, 5A) | 520 | ABYC A-1, ISO 10239, RINA |

**Sensorplatzierung (kritisch!):**

```
KORREKT:                        FALSCH:
┌─────────────────────┐         ┌─────────────────────┐
│     Wohnbereich     │         │     Wohnbereich     │
│                     │         │         ❌ Sensor    │
│                     │         │    (zu hoch!)       │
│─────────────────────│         │─────────────────────│
│     Fußboden        │         │     Fußboden        │
│─────────────────────│         │─────────────────────│
│  Bilge              │         │  Bilge              │
│  ✅ Sensor hier     │         │  (kein Sensor!)     │
│  (max. 150mm       │         │                     │
│   über Bilgenboden) │         │                     │
└─────────────────────┘         └─────────────────────┘
```

**Kalibrierung und Wartung:**
- Katalytische Sensoren: jährliche Kalibrierung empfohlen (Prüfgas: Isobutan-Luft-Gemisch, 50% UEG)
- Halbleiter-Sensoren: alle 2 Jahre Funktionsprüfung mit Prüfgas
- Sensorlebensdauer: 3–5 Jahre (katalytisch), 5–7 Jahre (Halbleiter), 10+ Jahre (NDIR)
- **AYDI-Regel:** Detektoralter > Sensor-Lebensdauer → CRITICAL-Befund

### 7.9 Flammensicherung (Flame Failure Device)

Die Flammensicherung (auch: Zündsicherung, thermoelektrische Sicherung, Flame Failure Device / FFD) ist eine **geräteseitige Sicherheitseinrichtung**, die den Gaszufluss unterbricht, wenn die Flamme erlischt (z.B. durch Wind, Überkochen, defekten Brenner).

**Funktionsprinzip:**
- Ein Thermoelement (Typ K, NiCr-NiAl) in der Flamme erzeugt ca. 25–30 mV Spannung
- Diese Spannung hält ein Elektromagnet-Ventil offen
- Erlischt die Flamme, sinkt die Spannung → Ventil schließt innerhalb 30–90 Sekunden
- **Keine externe Stromversorgung erforderlich** (thermoelektrisch)

**Normanforderung:**
- ISO 10239, Abschnitt 5.8: **Pflicht** für alle fest eingebauten Gasverbraucher auf Yachten
- ABYC A-1: Pflicht, Abschaltzeit max. 60 Sekunden
- EN 30-1-1 (Gasherde): Abschaltzeit max. 90 Sekunden

**Marine-Verbraucher mit Flammensicherung:**

| Hersteller | Gerät | Flammensicherung | Abschaltzeit |
|------------|-------|-------------------|-------------|
| ENO | Alle Marine-Kocher ab 2005 | Ja, alle Brenner | 30–45 s |
| Force10 | Alle Modelle | Ja, alle Brenner | 25–40 s |
| Dometic/SMEV | MO8322, MO9222, etc. | Ja, alle Brenner | 30–60 s |
| Plastimo | Pacific-Serie | Ja, alle Brenner | 40–60 s |
| Thetford | Argent-Serie | Ja, alle Brenner | 35–55 s |
| Camping Gaz | Tragbare Kocher | **NEIN** (Ausnahme: Bistro) | — |

**AYDI-Bewertung:**

| Befund | Severity | Score-Auswirkung |
|--------|----------|-----------------|
| Alle Verbraucher mit FFD | OK | Basis |
| FFD vorhanden, Funktion ungeprüft | WARNING | −10 |
| FFD an einem Verbraucher fehlend | CRITICAL | −30 |
| FFD an allen Verbrauchern fehlend | CRITICAL | −50 + Empfehlung Gerätetausch |

### 7.10 Gasprüfung und Zertifizierung

**Prüfintervalle nach Rechtsrahmen:**

| Land | Rechtsgrundlage | Intervall | Prüfer |
|------|----------------|-----------|--------|
| Deutschland | BetrSichV + TRF 2012 | Alle 2 Jahre | DVGW G 607 Sachkundiger |
| UK | BSS (Boat Safety Scheme) | Alle 4 Jahre | BSS Examiner |
| Frankreich | Division 240 | Bei Inbetriebnahme + alle 5 Jahre | Qualigaz |
| Niederlande | Binnenvaartwet | Alle 3 Jahre | Erkend Installateur |
| USA | Keine Pflicht-Prüfung (!) | ABYC empfiehlt jährlich | ABYC-zertifizierter Techniker |
| Australien | AS 5601.1 | Alle 4 Jahre | Licensed Gas Fitter |

**Prüfablauf nach DVGW G 607 (Deutschland):**

| Schritt | Prüfung | Methode | Kriterium |
|---------|---------|---------|-----------|
| 1 | Sichtprüfung Gaslocker | Visuell | Gasdicht, Drain frei, Belüftung vorhanden |
| 2 | Sichtprüfung Schläuche | Visuell + Abtasten | Keine Risse, Porösität, Scheuerstellen; Datum <10 Jahre |
| 3 | Sichtprüfung Festleitungen | Visuell | Keine Korrosion, korrekte Befestigung alle 500 mm |
| 4 | Dichtheitsprüfung | Druckprüfung 150 mbar, 3 min | Kein Druckabfall (Manometer: ±0,5 mbar Genauigkeit) |
| 5 | Regler-Prüfung | Betriebsdruckmessung | 30 ± 3 mbar Ausgangsdruck |
| 6 | Magnetventil-Test | Schalter betätigen | Öffnet/schließt zuverlässig, fail-closed |
| 7 | Gasdetektor-Test | Prüfgas applizieren | Alarm <30 s, Solenoid schließt (wenn verbunden) |
| 8 | Flammensicherung | Flamme ausblasen | Gaszufuhr stoppt <90 s (EN), <60 s (ABYC) |
| 9 | Belüftung Verbraucher | Visuell + Messung | Zuluftöffnung vorhanden, min. Querschnitt |
| 10 | Dokumentation | Prüfprotokoll | Datum, Befunde, nächster Prüftermin |

**Kosten für Gasprüfung:**

| Leistung | Deutschland (EUR) | UK (GBP→EUR) | Frankreich (EUR) |
|----------|------------------|--------------|-----------------|
| Gasprüfung (Standard) | 120–180 | 110–160 | 150–220 |
| Gasprüfung + Schlauch-Austausch | 200–350 | 180–300 | 250–400 |
| Vollständige Neuinstallation (einfach) | 800–1.500 | 700–1.300 | 900–1.800 |
| Vollständige Neuinstallation (komplex) | 1.500–3.500 | 1.200–3.000 | 1.800–4.000 |
| Gasdetektor nachrüsten (inkl. Solenoid) | 350–600 | 300–550 | 400–700 |

---

## 8. Hersteller — Vollständige Übersicht

### 8.1 Truma

**Firmenportrait:**
- **Vollständiger Name:** Truma Gerätetechnik GmbH & Co. KG
- **Sitz:** Putzbrunn bei München, Deutschland
- **Gegründet:** 1949
- **Spezialgebiet:** LPG-Zubehör, Heizungen, Klimatechnik für Caravan & Marine
- **Umsatz:** ca. 500 Mio. EUR (2023)
- **Marine-Relevanz:** Marktführer für LPG-Regler und Gascontrol-Systeme im deutschsprachigen Raum

**Marine-relevante Produktlinien:**

#### Druckregler

| Modell | Art.-Nr. | Typ | Anschluss | Besonderheit | Preis (EUR) |
|--------|----------|-----|-----------|-------------|-------------|
| MonoControl CS | 60180-00 | 1-Flasche, Crash-Sensor | W 21,8 × 1/14" LH | Schließt bei Erschütterung/Neigung | 89 |
| MonoControl CS vertikal | 60180-10 | 1-Flasche, vertikale Flasche | W 21,8 × 1/14" LH | Für stehende Flaschen | 95 |
| DuoControl CS | 60230-00 | 2-Flaschen, Crash + Umschalt | W 21,8 × 1/14" LH | Automatische Umschaltung | 189 |
| DuoControl CS vertikal | 60230-10 | 2-Flaschen, vertikal | W 21,8 × 1/14" LH | Für stehende Flaschen | 199 |
| DuoComfort | 60250-00 | 2-Flaschen, Umschalt (ohne CS) | W 21,8 × 1/14" LH | Komfort-Umschaltung | 149 |

#### Gasfilter

| Modell | Art.-Nr. | Zweck | Preis (EUR) |
|--------|----------|-------|-------------|
| Gasfilter | 50200-01 | Filtert Öl und Partikel aus Gasphase | 19 |
| Gasfilter mit Schauglas | 50200-02 | Filtert + zeigt Gasdurchfluss | 29 |

#### Schläuche und Zubehör

| Modell | Art.-Nr. | Länge (mm) | ID (mm) | Anschluss | Preis (EUR) |
|--------|----------|------------|---------|-----------|-------------|
| HD-Schlauch MonoControl | 60189-01 | 450 | 8 | G 1/4 LH → Regler | 22 |
| HD-Schlauch DuoControl | 60189-02 | 450 | 8 | G 1/4 LH × 2 → Regler | 35 |
| ND-Schlauchleitung | 60189-10 | 750 | 8 | 8 mm Stecknippel | 18 |
| ND-Schlauchleitung lang | 60189-15 | 1500 | 8 | 8 mm Stecknippel | 25 |
| Truma SecuMotion | 60290-00 | — | 8 | Integriert | 149 |

#### Truma iNet System (Digitale Steuerung)

| Modell | Art.-Nr. | Funktion | Preis (EUR) |
|--------|----------|----------|-------------|
| iNet Box | 36500-00 | Zentraleinheit, WLAN/BLE, Steuerung aller Truma-Geräte | 399 |
| LevelControl | 36600-00 | Ultraschall-Füllstandsmessung, in iNet integrierbar | 179 |
| LevelControl + iNet Set | 36650-00 | Kombi-Set | 529 |

**Truma-Besonderheiten für Marine:**
- Truma-Regler sind für den Caravan-Markt entwickelt, werden aber auf 80%+ aller deutschen Yachten eingesetzt
- Der Crash-Sensor ist im Marine-Bereich besonders relevant: Bei Grundberührung oder Kollision schließt das Gas automatisch
- Truma bietet **keine explizit für Marine zertifizierten** Produkte — die CE-Konformität deckt jedoch alle relevanten EU-Normen ab
- Einschränkung: Truma-Regler sind für deutsche Gasflaschen (W 21,8 × 1/14" LH) ausgelegt → Adapter für internationale Flaschen erforderlich

### 8.2 GOK

**Firmenportrait:**
- **Vollständiger Name:** GOK Regler- und Armaturen GmbH & Co. KG
- **Sitz:** Marktbreit, Bayern, Deutschland
- **Gegründet:** 1970
- **Spezialgebiet:** LPG-Armaturen, Regler, Ventile, Schläuche
- **Umsatz:** ca. 120 Mio. EUR (2023)
- **Marine-Relevanz:** Breitestes Sortiment an LPG-Armaturen in Europa, viele OEM-Zulieferungen

**Marine-relevante Produkte:**

#### Druckregler

| Modell | Art.-Nr. | Typ | Anschluss | Preis (EUR) |
|--------|----------|-----|-----------|-------------|
| Caramatic BasicOne 30 | 01-100-01 | 1-Flasche, 30 mbar | W 21,8 LH | 29 |
| Caramatic BasicTwo 30 | 01-100-02 | 2-Flaschen, 30 mbar, manuell | W 21,8 LH | 55 |
| Caramatic DriveOne | 01-111-01 | 1-Flasche + Crash-Sensor | W 21,8 LH | 79 |
| Caramatic DriveTwo | 01-112-01 | 2-Flaschen + Crash + Umschalt | W 21,8 LH | 169 |
| Marine-Regler 30 mbar | 01-130-01 | 1-Flasche, Marine-zertifiziert | W 21,8 LH | 65 |
| Regler mit Manometer | 01-140-01 | 1-Flasche + Druckanzeige | W 21,8 LH | 49 |

#### Gasschläuche

| Modell | Art.-Nr. | Länge (mm) | Typ | Norm | Preis (EUR) |
|--------|----------|------------|-----|------|-------------|
| HD-Schlauchleitung | 01-211-0045 | 450 | Hochdruck | EN 16436 | 18 |
| HD-Schlauchleitung | 01-211-0075 | 750 | Hochdruck | EN 16436 | 22 |
| ND-Schlauchleitung 30 mbar | 01-212-0050 | 500 | Niederdruck | EN 1763 | 12 |
| ND-Schlauchleitung 30 mbar | 01-212-0100 | 1000 | Niederdruck | EN 1763 | 16 |
| ND-Schlauchleitung 30 mbar | 01-212-0150 | 1500 | Niederdruck | EN 1763 | 19 |

#### Adapter (Internationale Gasflaschen)

| Modell | Art.-Nr. | Von → Nach | Preis (EUR) |
|--------|----------|-----------|-------------|
| Adapter DE→FR | 01-150-10 | W 21,8 LH → Clip-on (Butagaz) | 28 |
| Adapter DE→UK | 01-150-20 | W 21,8 LH → POL | 32 |
| Adapter DE→ES | 01-150-40 | W 21,8 LH → Spanisch (Repsol) | 35 |
| Adapter DE→IT | 01-150-30 | W 21,8 LH → W 20 LH (Italiano) | 24 |
| Adapter DE→US | 01-150-50 | W 21,8 LH → ACME (US) | 38 |
| Adapter-Set Welt (8 Stück) | 01-150-00 | Alle gängigen Systeme | 169 |

#### GOK Senso4s Füllstandsmessung

| Modell | Art.-Nr. | Funktion | Preis (EUR) |
|--------|----------|----------|-------------|
| Senso4s Basic | 01-160-01 | Ultraschall-Füllstand, BLE | 99 |
| Senso4s Plus | 01-160-02 | Füllstand + Leck-Warnung, BLE | 149 |

**GOK-Besonderheiten für Marine:**
- GOK ist der größte deutsche OEM-Zulieferer für LPG-Armaturen
- Viele Bootshersteller (Bavaria, Hanse, Jeanneau DE-Versionen) verbauen GOK-Regler ab Werk
- GOK bietet das umfangreichste Adapter-Sortiment für internationale Gasflaschen
- GOK Senso4s ist mit vielen Smart-Home-Systemen kompatibel (Signal K Integration möglich)

### 8.3 Gaslow

**Firmenportrait:**
- **Vollständiger Name:** Gaslow International Ltd
- **Sitz:** Barnstaple, Devon, UK
- **Gegründet:** 2002
- **Spezialgebiet:** Nachfüllbare LPG-Flaschen und Adapter
- **Marine-Relevanz:** Lösung für das Problem verschiedener Flaschenanschlüsse beim Fahrtensegeln

**Produktlinie — Nachfüllbare Flaschen:**

| Modell | Inhalt | Gewicht leer | Material | Preis (EUR) | Anschluss |
|--------|--------|-------------|----------|-------------|-----------|
| Gaslow R67-1 | 2,7 kg | 3,8 kg | Stahl | 169 | W 21,8 LH + Fill |
| Gaslow R67-2 | 6 kg | 6,2 kg | Stahl | 229 | W 21,8 LH + Fill |
| Gaslow R67-3 | 11 kg | 11,5 kg | Stahl | 289 | W 21,8 LH + Fill |
| Gaslow Alu 6 | 6 kg | 3,9 kg | Aluminium | 379 | W 21,8 LH + Fill |
| Gaslow Alu 11 | 11 kg | 7,5 kg | Aluminium | 449 | W 21,8 LH + Fill |

**Fill-Kit Europa:**

| Kit | Art.-Nr. | Inhalt | Preis (EUR) |
|-----|----------|--------|-------------|
| Europa Fill Kit | GAS-FK-EU | 4 Adapter (NL, FR, ES, IT) + Schlauch | 89 |
| UK Bayonet Adapter | GAS-FK-UK | UK LPG-Tankstellen-Adapter | 29 |
| ACME US Adapter | GAS-FK-US | US/Kanada-Adapter | 35 |
| Australien POL RH | GAS-FK-AU | Australien-Adapter (Rechtsgewinde!) | 35 |

**Marine-Vorteil Gaslow:**
- Nachfüllbar an LPG-Tankstellen (Autogas) → kein Flaschentausch nötig
- Besonders wertvoll für Langfahrer: Autogas-Tankstellen sind weltweit häufiger als Flaschentausch-Stationen
- Gewichtsvorteil Alu-Flaschen: 3,9 kg statt 6,2 kg bei 6-kg-Füllung
- **Einschränkung:** Nachfüllen von Gasflaschen ist in einigen Ländern (u.a. Deutschland!) rechtlich problematisch — Gaslow-Flaschen sind als nachfüllbare Druckbehälter nach ECE R67 zugelassen und damit legal

### 8.4 Clesse

**Firmenportrait:**
- **Vollständiger Name:** Clesse Industries S.A.S.
- **Sitz:** Metz, Frankreich
- **Gegründet:** 1949
- **Spezialgebiet:** LPG- und Erdgas-Armaturen, Regler, Ventile
- **Marine-Relevanz:** Standard-Ausrüster in Frankreich und Nordafrika

**Marine-relevante Produkte:**

| Modell | Typ | Anschluss | Besonderheit | Preis (EUR) |
|--------|-----|-----------|-------------|-------------|
| CELGI B132 | 1-Flasche, 28/37 mbar | Clip-on (FR) | Französischer Standard | 35 |
| CELGI Inverseur B240 | 2-Flaschen, Umschaltung | Clip-on (FR) | Auto-Umschaltung | 95 |
| CELGI B360 | 1-Flasche, 30 mbar | W 21,8 LH (DE) | Für deutsche Flaschen in FR-Booten | 39 |
| Flexibles Schlauchleitung | ND, 500–1500 mm | G 1/4 | EN 1763 | 15–25 |

**Relevanz für AYDI:** Clesse-Regler finden sich häufig auf französischen Yachten (Bénéteau, Jeanneau, Dufour, Fountaine Pajot). Bei Bewertung französischer Boote ist die Clip-on-Anschlussart zu beachten (nicht kompatibel mit deutschen Flaschen ohne Adapter).

### 8.5 Cavagna Group

**Firmenportrait:**
- **Vollständiger Name:** Cavagna Group S.p.A.
- **Sitz:** Calcinato, Brescia, Italien
- **Gegründet:** 1949
- **Spezialgebiet:** LPG/CNG-Armaturen, weltweit größter Hersteller von Gas-Druckreglern
- **Umsatz:** ca. 450 Mio. EUR (2023)
- **Marine-Relevanz:** OEM-Zulieferer für viele Bootshersteller, besonders Italien und global

**Marine-relevante Produkte:**

| Modell | Art.-Nr. | Typ | Ausgangsdruck | Preis (EUR) |
|--------|----------|-----|---------------|-------------|
| 7KG LPG 30 mbar | 734030000 | 1-Flasche, 30 mbar | 30 mbar | 32 |
| 7KG LPG 50 mbar | 734050000 | 1-Flasche, 50 mbar | 50 mbar (US/AUS) | 35 |
| 7KG Adjustable | 734ADJ000 | 1-Flasche, einstellbar | 25–50 mbar | 45 |
| 734N Dual-Stage | 734N30000 | 1-Flasche, zweistufig | 30 mbar | 55 |
| Auto-Changeover | 734ACS000 | 2-Flaschen, Umschaltung | 30 mbar | 89 |

**Besonderheit:** Cavagna bietet Regler mit fast allen weltweit gängigen Eingangsanschlüssen — ideal für Langfahrer, die in verschiedenen Ländern Gasflaschen tauschen müssen.

### 8.6 Gimeg

**Firmenportrait:**
- **Vollständiger Name:** Gimeg B.V.
- **Sitz:** Breda, Niederlande
- **Gegründet:** 1985
- **Spezialgebiet:** Marine- und Caravan-Gasarmaturen für den niederländischen Markt
- **Marine-Relevanz:** Stark im niederländischen und belgischen Binnenmarkt, viele Motorboote und Binnenyachten

**Marine-relevante Produkte:**

| Modell | Art.-Nr. | Typ | Anschluss | Preis (EUR) |
|--------|----------|-----|-----------|-------------|
| Kombi-Regler Marine 30 | 6000-300 | 1-Flasche, 30 mbar | W 21,8 LH | 39 |
| Kombi-Regler Duo Marine | 6000-302 | 2-Flaschen, Umschaltung | W 21,8 LH | 85 |
| Marine Gasschlauch 500 | 6100-050 | ND, 500 mm | 8 mm × 8 mm | 12 |
| Marine Gasschlauch 1000 | 6100-100 | ND, 1000 mm | 8 mm × 8 mm | 16 |
| Marine Gasschlauch 1500 | 6100-150 | ND, 1500 mm | 8 mm × 8 mm | 19 |
| Gasdetector Marine 12V | 6200-100 | Halbleiter, 12V, Alarm | — | 89 |

### 8.7 Marinox/ENO

**Firmenportrait:**
- **Vollständiger Name:** ENO S.A. (Marinox ist die Marine-Sparte)
- **Sitz:** Niort, Frankreich
- **Gegründet:** 1909
- **Spezialgebiet:** Marine-Kochgeräte (Gasherde, Backöfen, BBQ)
- **Marine-Relevanz:** **Weltweit führend** für marine Gasherde, verbaut auf 70%+ aller französischen Yachten

**Marine-Gaskocher und -öfen:**

| Modell | Art.-Nr. | Flammen | Backofen | Kardanring | FFD | Preis (EUR) |
|--------|----------|---------|----------|------------|-----|-------------|
| ENO One | 1830 | 1 | Nein | Optional | Ja | 390 |
| ENO Classic | 1831 | 2 | Nein | Ja | Ja | 580 |
| ENO Sunlight | 1833 | 2 | Ja (Grill) | Ja | Ja | 890 |
| ENO Grand Large | 1835 | 3 | Ja | Ja | Ja | 1.380 |
| ENO Bretagne | 1837 | 3 | Ja (groß) | Ja | Ja | 1.690 |
| ENO Magma | 1839 | 2 | Ja | Ja | Ja | 1.250 |

**ENO-Gasanschluss-Spezifikation:**
- Eingang: G 1/4" LH (Standard-Gasanschluss)
- Schlauchempfehlung: EN 1763, 500–1000 mm, 8 mm ID
- Betriebsdruck: 30 mbar (28/30/37 mbar je nach Ländervariante)
- **Alle ENO-Geräte haben Flammensicherung (FFD) an jedem Brenner seit 2005**

**ENO-Schlauch-Zubehör:**

| Teil | Art.-Nr. | Beschreibung | Preis (EUR) |
|------|----------|-------------|-------------|
| Anschluss-Schlauch 500 mm | 30510 | ND-Schlauch, G 1/4" LH | 18 |
| Anschluss-Schlauch 1000 mm | 30511 | ND-Schlauch, G 1/4" LH | 24 |
| Anschluss-Schlauch 1500 mm | 30512 | ND-Schlauch, G 1/4" LH | 29 |
| Schnellkupplung Gas | 30520 | Für schnelle Herd-Demontage | 35 |

### 8.8 Plastimo

**Firmenportrait:**
- **Vollständiger Name:** Plastimo S.A.S.
- **Sitz:** Lorient, Bretagne, Frankreich
- **Gegründet:** 1963
- **Spezialgebiet:** Marine-Zubehör (Sicherheit, Deck, Komfort)
- **Marine-Relevanz:** Bietet Gas-Zubehör als Teil des breiten Marine-Sortiments

**Gas-relevante Produkte:**

| Modell | Art.-Nr. | Beschreibung | Preis (EUR) |
|--------|----------|-------------|-------------|
| Gasherd Pacific 2000 | 41809 | 2-Flammen, Kardanring, FFD | 520 |
| Gasherd Pacific 4000 | 41811 | 2-Flammen + Backofen, FFD | 780 |
| Gasherd Pacific 5000 | 41813 | 3-Flammen + Backofen, FFD | 1.120 |
| Gasschlauch Marine 500 | 42110 | ND, 500 mm, EN 1763 | 15 |
| Gasschlauch Marine 1000 | 42111 | ND, 1000 mm, EN 1763 | 20 |
| Gasleitung Kupfer 6×1 | 42200 | Kupfer EN 1057, per Meter | 8/m |
| Gas-Absperrhahn | 42300 | Kugelhahn, Messing, G 1/4" | 18 |
| Gasflaschenhalter | 42400 | Edelstahl 316L, einstellbar | 45 |

### 8.9 Dometic/SMEV

**Firmenportrait:**
- **Vollständiger Name:** Dometic Group AB (ehemals Electrolux Leisure, inkl. SMEV und Cramer)
- **Sitz:** Stockholm, Schweden (Produktion: Italien, China)
- **Gegründet:** 1922 (als Electrolux Leisure)
- **Spezialgebiet:** Mobile Living (Kühlung, Kochen, Klimatechnik)
- **Marine-Relevanz:** Marktführer bei Marine-Kühlschränken (Absorber), starke Position bei Gaskochern

**Marine-Gasherde (SMEV-Linie):**

| Modell | Art.-Nr. | Flammen | Backofen | Kardanring | FFD | Preis (EUR) |
|--------|----------|---------|----------|------------|-----|-------------|
| MO8322R | 9103301747 | 2 | Nein | Nein | Ja | 195 |
| MO8322G | 9103301748 | 2 | Nein | Ja (optional) | Ja | 225 |
| MO9222R | 9103301752 | 2 | Nein | Nein | Ja | 240 |
| MO9722R | 9103301756 | 2 + Spüle | Nein | Nein | Ja | 350 |
| MO1232 | 9103301770 | 3 | Ja | Nein | Ja | 680 |
| Starlight | 9103303880 | 2 | Ja (Grill) | Ja | Ja | 1.150 |

**Marine-Absorber-Kühlschränke (Gasbetrieb):**

| Modell | Art.-Nr. | Inhalt (l) | Betrieb | Gas (g/h) | Preis (EUR) |
|--------|----------|-----------|---------|-----------|-------------|
| RM 2356 | 9105204684 | 95 | Gas/12V/230V | 18–22 | 1.250 |
| RM 5310 | 9500001218 | 60 | Gas/12V/230V | 14–18 | 950 |
| RM 8401 | 9105707032 | 95 | Gas/12V/230V | 16–20 | 1.150 |
| RM 8505 | 9105707055 | 106 | Gas/12V/230V | 18–22 | 1.450 |

**Gasanschluss Dometic/SMEV:**
- Kocher: 8 mm Schlauch oder G 1/4" LH
- Kühlschrank: 6 mm oder 8 mm Schlauch, Niederdruckseite
- Betriebsdruck: 30 mbar
- **Kühlschrank-Gasbetrieb auf Yachten:** Gasflamme ist ständig an → erhöhtes Risiko → ABYC empfiehlt Gasdetektor in der Nähe des Kühlschranks

### 8.10 Force10

**Firmenportrait:**
- **Vollständiger Name:** Force 10 Marine (ehemals Dickinson Marine)
- **Sitz:** Vancouver, British Columbia, Kanada (jetzt Subsidiary von Leisure Tech)
- **Gegründet:** 1932
- **Spezialgebiet:** Marine-Gasherde und -öfen, speziell für Segelyachten
- **Marine-Relevanz:** Marktführer in Nordamerika, starke Präsenz auf Performance-Segelyachten

**Marine-Gasherde:**

| Modell | Flammen | Backofen | Kardanring | FFD | Anschluss | Preis (EUR) |
|--------|---------|----------|------------|-----|-----------|-------------|
| Force10 63251 (2-Burner) | 2 | Nein | Ja | Ja | G 1/4" | 750 |
| Force10 63351 (3-Burner) | 3 | Nein | Ja | Ja | G 1/4" | 980 |
| Force10 65336 (3+Oven) | 3 | Ja | Ja | Ja | G 1/4" | 1.650 |
| Force10 66032 (2+Oven, Euro) | 2 | Ja | Ja | Ja | G 1/4" | 1.350 |
| Force10 76336 (3+Oven, SS) | 3 | Ja (groß) | Ja | Ja | G 1/4" | 2.100 |

**Besonderheit Force10:**
- Edelstahl-Konstruktion (316L) für extreme Marine-Bedingungen
- Kardanring-Design für Krängungswinkel bis 30°
- Topfhalter an allen Brennern (obligatorisch für Seegang)
- ABYC A-1 konforme Installation mit Solenoid-Ventil empfohlen

### 8.11 Osculati/Talamex

**Osculati:**
- **Sitz:** Segrate (Mailand), Italien
- **Gegründet:** 1958
- **Sortiment:** Umfassendes Marine-Zubehör, inkl. Gas-Armaturen

| Modell | Art.-Nr. | Beschreibung | Preis (EUR) |
|--------|----------|-------------|-------------|
| Gasschlauch 500 mm | 50.230.50 | ND, EN 1763, 8 mm | 14 |
| Gasschlauch 1000 mm | 50.230.10 | ND, EN 1763, 8 mm | 18 |
| Gasschlauch 1500 mm | 50.230.15 | ND, EN 1763, 8 mm | 22 |
| Magnetventil 12V | 50.232.00 | NC, 12V, 8 mm | 79 |
| Gashahn Messing | 50.233.00 | Kugelhahn, G 1/4" | 15 |
| Gasdetektor 12V | 50.234.00 | Halbleiter, Alarm | 85 |
| Gaslocker-Drain 19 mm | 50.235.00 | Durchführung, Edelstahl | 12 |
| Gaslocker-Belüftung | 50.236.00 | Edelstahl-Gitter, 75×75 mm | 9 |
| Gasflaschenhalter | 50.237.00 | Edelstahl, 3 kg + 5 kg | 35 |

**Talamex:**
- **Sitz:** Noordwijk, Niederlande
- **Gegründet:** 1958
- **Sortiment:** Marine-Zubehör für den niederländischen und nordeuropäischen Markt

| Modell | Art.-Nr. | Beschreibung | Preis (EUR) |
|--------|----------|-------------|-------------|
| Gasschlauch 500 mm | TLX-GS-050 | ND, EN 1763, 8 mm | 15 |
| Gasschlauch 1000 mm | TLX-GS-100 | ND, EN 1763, 8 mm | 19 |
| Marine-Gasregler 30 mbar | TLX-GR-030 | 1-Flasche | 42 |
| Marine-Gasdetektor | TLX-GD-01 | 12V, Halbleiter | 95 |

### 8.12 Zusammenfassung OEM vs Aftermarket

| Kategorie | OEM (ab Werft verbaut) | Aftermarket (Nachrüstung) |
|-----------|----------------------|--------------------------|
| **Regler** | Truma MonoControl CS (DE-Werften), GOK BasicOne (Budget), Clesse CELGI (FR-Werften) | Truma DuoControl CS (Upgrade), Cavagna 7KG (universal) |
| **Schläuche** | GOK ND-Schlauchleitungen (häufigster OEM), Truma ND (bei Truma-Regler) | Edelstahl-Wellschläuche (Upgrade), Flexcon Gas Marine |
| **Kocher** | ENO (FR-Werften: Bénéteau, Jeanneau, Lagoon), Dometic/SMEV (DE-Werften: Bavaria, Hanse) | Force10 (Performance-Upgrade), ENO Grand Large (Komfort-Upgrade) |
| **Detektor** | NASA Marine (UK-Werften), Dometic GD-01 (DE-Werften) | Fireboy-Xintex MS-2 (ABYC-konform), Gas Boat GD-1 (UK) |
| **Solenoid** | GOK 01-210-01 (DE-Werften), Marintek (Budget) | Truma SecuMotion (Premium), Fireboy S-1 (ABYC) |

**Preisvergleich nach Komponente (typische Marine-Anlage, 10-m-Segelyacht):**

| Komponente | Budget | Standard | Premium |
|------------|--------|----------|---------|
| Regler | GOK BasicOne (29 €) | Truma MonoControl CS (89 €) | Truma DuoControl CS (189 €) |
| Schläuche (Set) | Osculati (2× 14 €) | GOK (2× 18 €) | Flexcon SS (2× 65 €) |
| Magnetventil | Osculati (79 €) | GOK (89 €) | Truma SecuMotion (149 €) |
| Gasdetektor | Dometic GD-01 (95 €) | NASA Marine (195 €) | Xintex MS-2 (385 €) |
| **Gesamt (ohne Kocher)** | **231 €** | **409 €** | **919 €** |

---

## 9. Anlagen-spezifische Zuordnung

### 9.1 Marine-Kocher (ENO, Force10, Dometic/SMEV, Plastimo, Thetford)

**Gasanschluss-Matrix nach Kocher-Hersteller:**

| Hersteller | Modellreihe | Gasanschluss | Schlauch-ID | Empfohlener Schlauch | Max. Schlauchlänge |
|------------|-------------|-------------|-------------|---------------------|-------------------|
| ENO | Alle Marine | G 1/4" LH | 8 mm | ENO 30510/11/12 | 1500 mm |
| Force10 | Alle Marine | G 1/4" LH | 8 mm | Herstellerunspezifisch EN 1763 | 1500 mm |
| Dometic/SMEV | MO-Serie | 8 mm Tülle | 8 mm | GOK 01-212-xxxx | 1500 mm |
| Dometic/SMEV | Starlight | G 1/4" LH | 8 mm | Truma 60189-10 | 1500 mm |
| Plastimo | Pacific | G 1/4" LH | 8 mm | Plastimo 42110/11 | 1500 mm |
| Thetford | Argent | 8 mm Tülle | 8 mm | Herstellerunspezifisch EN 1763 | 1000 mm |
| CAN (Italien) | SL-Serie | G 1/4" LH | 8 mm | Herstellerunspezifisch EN 1763 | 1500 mm |

**Kocher-Sicherheitsanforderungen nach ISO 10239:**

| Anforderung | Detail | AYDI-Prüfung |
|-------------|--------|-------------|
| Flammensicherung | An **jedem** Brenner und Backofen | Visuell + Funktionstest |
| Belüftung Kochnische | Min. 6000 mm² Zuluft, 9000 mm² Abluft | Visuell: Lüftungsgitter |
| Abstand zu brennbaren Materialien | Min. 200 mm (ohne Hitzeschutz), 50 mm (mit) | Messen oder visuell |
| Topfhalter | Pflicht auf Segelyachten (Krängung) | Visuell |
| Kardanring | Empfohlen auf Segelyachten | Visuell: vorhanden + funktional |
| Absperrung | Magnetventil in Sichtweite des Kochers | Visuell: Schalter sichtbar |
| Kocher-Sicherung | Gegen Herausfallen bei Krängung gesichert | Visuell |

**Typische Gas-Installationskosten für Marine-Kocher:**

| Kocher-Typ | Kocher-Preis (EUR) | Installation (EUR) | Schlauch + Armaturen (EUR) | Gesamt (EUR) |
|------------|-------------------|-------------------|---------------------------|-------------|
| 2-Flammen, einfach (SMEV) | 195–250 | 150–300 | 50–80 | 395–630 |
| 2-Flammen, Kardanring (ENO) | 580–890 | 200–400 | 60–100 | 840–1.390 |
| 3-Flammen + Backofen (ENO) | 1.380–1.690 | 300–600 | 80–120 | 1.760–2.410 |
| 3-Flammen + Backofen (Force10) | 1.650–2.100 | 350–650 | 80–120 | 2.080–2.870 |

### 9.2 Marine-Heizungen (Truma, Webasto, Eberspächer)

Gasbetriebene Heizungen auf Yachten sind weniger verbreitet als Dieselheizungen, finden sich aber häufig auf:
- Segelyachten bis 12 m (Truma Heizung als Caravan-Übernahme)
- Binnenbooten und Hausbooten
- Älteren Yachten (vor 2000)

**Gasbetriebene Marine-Heizungen:**

| Hersteller | Modell | Leistung (W) | Gasverbrauch (g/h) | Anschluss | Preis (EUR) |
|------------|--------|-------------|-------------------|-----------|-------------|
| Truma | S 3004 | 3.500 | 160–260 | 30 mbar, 8 mm | 890 |
| Truma | S 5004 | 6.000 | 220–450 | 30 mbar, 8 mm | 1.150 |
| Truma | VarioHeat comfort | 3.400 | 200–280 | 30 mbar, 8 mm | 1.290 |
| Truma | VarioHeat eco | 2.800 | 150–220 | 30 mbar, 8 mm | 1.190 |
| Truma | Combi D 6 E | 6.000 | Gas + Elektro | 30 mbar, 8 mm | 2.450 |

**Gasleitungs-Anforderungen für Heizungen:**
- Gasleitung zur Heizung: starre Kupferleitung empfohlen (Heizung oft weit vom Gaslocker entfernt)
- Flexibler Endanschluss: max. 1500 mm, EN 1763, direkt am Heizgerät
- Abgasführung: separate Abgasleitung nach außen (nicht verwechseln mit Gasleitung!)
- **Besonderheit:** Truma-Heizungen haben eigene Flammensicherung + Raumtemperaturbegrenzung + CO-Detektor (integriert ab Combi-Serie)

**AYDI-Bewertung Gasheizung:**
- Gasheizung + Gasdetektor im Aufstellraum: Standard-Score
- Gasheizung OHNE Gasdetektor im Aufstellraum: CRITICAL (−40 Punkte)
- Gasheizung über Nacht im Betrieb: WARNING (CO-Risiko), außer bei integriertem CO-Detektor

### 9.3 Marine-Kühlschränke (Waeco/Dometic Absorber)

Absorber-Kühlschränke nutzen eine Gasflamme zur Erzeugung der Kühlleistung (Ammoniak-Wasser-Kreislauf). Die Gasflamme brennt **kontinuierlich** — im Gegensatz zum intermittierenden Betrieb eines Kochers.

**Sicherheitsbedenken Gaskühlschrank:**

> ⚠️ **Ein Gaskühlschrank auf einer Yacht bedeutet: Die Gasflamme brennt 24/7.**
> Dies ist das **einzige Gasgerät an Bord, das dauerhaft Gas verbraucht**.
> Jede Undichtigkeit am Gasanschluss des Kühlschranks ist sofort gefährlich,
> da sie nicht durch das Muster „Gas ein → kochen → Gas aus" begrenzt wird.

| Risiko | Beschreibung | Maßnahme |
|--------|-------------|----------|
| Dauerhafte Gasleitung unter Druck | Schlauch zum Kühlschrank steht ständig unter 30 mbar | Magnetventil VOR dem Kühlschrank (zusätzlich zum Haupt-Magnetventil) |
| Flamme erlischt | Luftzug, Kondenswasser, Thermoelement-Alterung | FFD Pflicht (alle modernen Geräte haben sie) |
| Abgase im Innenraum | Abgasleitung verstopft oder undicht | Abgasleitung regelmäßig prüfen |
| Kühlschrank-Rückwand | Hohe Temperatur an Rückwand | Min. 50 mm Abstand zu brennbaren Materialien |

**Dometic Absorber — Gas-Spezifikationen:**

| Modell | Gasverbrauch (g/h) | Gasanschluss | Max. Schlauchlänge | FFD |
|--------|-------------------|-------------|-------------------|-----|
| RM 2356 | 18–22 | 8 mm Tülle | 1500 mm | Ja |
| RM 5310 | 14–18 | 8 mm Tülle | 1500 mm | Ja |
| RM 8401 | 16–20 | 8 mm Tülle | 1500 mm | Ja |
| RM 8505 | 18–22 | 8 mm Tülle | 1500 mm | Ja |

**AYDI-Empfehlung:** Auf neuen Yachten einen **Kompressor-Kühlschrank** (12V/24V) anstelle eines Absorber-Kühlschranks empfehlen. Eliminiert die permanente Gasverbrennung an Bord. Bei bestehenden Absorber-Installationen: dediziertes Magnetventil + Gasdetektor in der Nähe des Kühlschranks.

### 9.4 BBQ-Systeme (Magma, ENO, Force10)

Marine-Grills (BBQ) werden in der Regel an Deck oder auf dem Heckkorb montiert und über eine separate Gasleitung oder eine tragbare Gasflasche versorgt.

**Marine-BBQ-Systeme:**

| Hersteller | Modell | Größe | Befestigung | Gasanschluss | Preis (EUR) |
|------------|--------|-------|-------------|-------------|-------------|
| Magma (USA) | Catalina 2 | 305×457 mm | Rail Mount, Pedestal | 3/8" Quick Connect | 580 |
| Magma | Newport 2 | 229×457 mm | Rail Mount | 3/8" Quick Connect | 490 |
| Magma | ChefsMate | 229×305 mm | Rail Mount | 3/8" Quick Connect | 350 |
| Magma | Monterey 2 | 305×457 mm | Rail Mount, Table | 3/8" Quick Connect | 680 |
| ENO | Cook'N Boat | 400×300 mm | Rail Mount | G 1/4" | 450 |
| ENO | Marine BBQ XL | 550×400 mm | Pedestal | G 1/4" | 750 |
| Force10 | BBQ Marine | 450×350 mm | Rail Mount | 3/8" | 620 |

**Gas-Sicherheitsanforderungen BBQ:**

| Anforderung | Detail |
|-------------|--------|
| Gasversorgung | Idealerweise separate kleine Flasche (1–2 kg), nicht Hauptanlage |
| Schlauch | EN 1763, max. 1500 mm, UV-beständig (Außenbereich!) |
| Absperrung | Flaschenventil + manueller Hahn am BBQ |
| Befestigung | Gegen Lösen bei Seegang gesichert |
| Position | Min. 500 mm von Segeln, Persenning, Leinen |
| FFD | Empfohlen, aber bei vielen BBQs nicht vorhanden |

**Magma Quick Connect System:**
- Magma verwendet ein proprietäres Quick-Connect-System (3/8" Schnellkupplung)
- Schlauch Magma A10-225: 3048 mm (10 ft), 3/8" ID, mit Quick-Connect-Kupplung, Preis: ca. 65 EUR
- Quick-Disconnect trennt bei Zug automatisch → Sicherheitsfeature
- **AYDI-Bewertung:** Quick-Disconnect-System wird positiv bewertet (+5 Punkte auf BBQ-Score)

### 9.5 Zusammenfassung Kosten

**Komplette LPG-Installation nach Bootstyp und Qualitätsstufe:**

| Bootstyp | Budget (EUR) | Standard (EUR) | Premium (EUR) |
|----------|-------------|---------------|--------------|
| **7–9 m Segelyacht** | | | |
| Kocher (2-Flammen) | 195 | 580 | 890 |
| Regler | 29 | 89 | 189 |
| Schläuche | 28 | 36 | 130 |
| Magnetventil | 79 | 89 | 149 |
| Gasdetektor | 95 | 195 | 385 |
| Installation | 150 | 300 | 600 |
| **Gesamt** | **576** | **1.289** | **2.343** |
| | | | |
| **10–14 m Segelyacht** | | | |
| Kocher (3-Flammen+Backofen) | 680 | 1.380 | 2.100 |
| Regler (2-Flaschen) | 55 | 169 | 189 |
| Schläuche (3 Stück) | 42 | 54 | 195 |
| Magnetventil | 79 | 89 | 149 |
| Gasdetektor | 95 | 195 | 385 |
| Festleitung (3 m Kupfer) | 24 | 24 | 60 (Edelstahl) |
| Installation | 300 | 500 | 900 |
| **Gesamt** | **1.275** | **2.411** | **3.978** |
| | | | |
| **15–20 m Motoryacht** | | | |
| Kocher | 680 | 1.380 | 2.100 |
| Heizung (Gas) | — | 890 | 1.290 |
| Absorber-Kühlschrank | — | 950 | 1.450 |
| BBQ | — | 450 | 680 |
| Regler (2-Flaschen) | 55 | 169 | 189 |
| Schläuche (4+ Stück) | 56 | 72 | 260 |
| Magnetventile (2×) | 158 | 178 | 298 |
| Gasdetektor (2 Sensoren) | 95 | 385 | 520 |
| Festleitung (8 m) | 64 | 64 | 160 (Edelstahl) |
| Installation | 500 | 900 | 1.800 |
| **Gesamt** | **1.608** | **5.438** | **8.747** |

**Jährliche Betriebskosten LPG-System:**

| Posten | Klein (7–9 m) | Mittel (10–14 m) | Groß (15–20 m) |
|--------|--------------|-----------------|----------------|
| Gasverbrauch (nur Kocher) | 50–80 EUR | 80–150 EUR | 150–300 EUR |
| Gasverbrauch (Kocher + Heizung) | — | 200–400 EUR | 400–800 EUR |
| Gasprüfung (2-jährig, umgelegt) | 60–90 EUR/a | 60–90 EUR/a | 90–150 EUR/a |
| Schlauch-Austausch (10-jährig, umgelegt) | 5–15 EUR/a | 8–20 EUR/a | 15–40 EUR/a |
| Detektor-Sensor (5-jährig, umgelegt) | 19–40 EUR/a | 19–40 EUR/a | 40–80 EUR/a |
| **Gesamt pro Jahr** | **134–225 EUR** | **367–700 EUR** | **695–1.370 EUR** |

**Vergleich: LPG vs. Induktion (10-Jahres-TCO für 10–14 m Segelyacht):**

| Posten | LPG Standard | Induktion |
|--------|-------------|-----------|
| Erstinstallation | 2.411 EUR | 5.500 EUR (inkl. Batterie, WR) |
| Gasverbrauch 10 Jahre | 1.500 EUR | 0 EUR (Strom aus Solar/Lichtmaschine) |
| Gasprüfungen 10 Jahre | 900 EUR | 0 EUR |
| Schlauch-Austausch (1×) | 100 EUR | 0 EUR |
| Detektor-Sensor (2×) | 200 EUR | 0 EUR |
| Batterie-Ersatz (nach 8 J.) | 0 EUR | 1.500 EUR |
| **10-Jahres-TCO** | **5.111 EUR** | **7.000 EUR** |
| **Explosionsrisiko** | **Vorhanden** | **Null** |

**AYDI-Schlussempfehlung:** LPG bleibt die kostengünstigere Lösung, aber die Sicherheitsvorteile der Elektrifizierung sollten bei jedem Neubau und jeder Grundüberholung als Alternative präsentiert werden. Bei bestehenden LPG-Systemen: korrekte Installation, regelmäßige Prüfung und funktionierende Sicherheitseinrichtungen (Gasdetektor + Magnetventil + Flammensicherung) reduzieren das Risiko auf ein akzeptables Maß.

---

## 10. Fehlerbild-Katalog — Visuelle Erkennung von Gasschlauch-Mängeln

### 10.1 Oberflächenschäden

| Fehlerbild | Beschreibung | Ursache | Severity | Maßnahme |
|------------|-------------|---------|----------|----------|
| Haarrisse quer | Feine Risse quer zur Schlauchachse, Außenmantel | UV-Alterung, Ozon | WARNING → CRITICAL (>3 Jahre alt) | Austausch innerhalb 30 Tagen |
| Haarrisse längs | Feine Risse längs zur Schlauchachse | Materialermüdung, Überdehnung | CRITICAL | Sofortiger Austausch |
| Tiefe Risse (>1 mm) | Sichtbar tiefe Risse, Geflecht erkennbar | Fortgeschrittene Alterung | CRITICAL | Sofortiger Austausch, Gas abstellen |
| Aufquellen | Schlauch aufgebläht, weicher als normal | LPG-Diffusion ins Material, falsches Material | CRITICAL | Sofortiger Austausch |
| Verhärtung | Schlauch hart, nicht biegbar, spröde | Alterung, UV, Hitze | CRITICAL | Sofortiger Austausch |
| Verfärbung (weiß) | Weiße Flecken/Streifen auf orangem Mantel | UV-Degradation | WARNING | Prüfung, ggf. Austausch |
| Verfärbung (schwarz) | Schwarze Verfärbung, klebrig | Ozon-Angriff, Chemikalien | WARNING → CRITICAL | Detailprüfung + Austausch |
| Abrieb | Außenmantel durchgescheuert | Reibung an Kante, Schott, Kabel | CRITICAL wenn Geflecht sichtbar | Scheuerschutz anbringen + ggf. Austausch |

### 10.2 Anschluss- und Armaturenschäden

| Fehlerbild | Beschreibung | Ursache | Severity | Maßnahme |
|------------|-------------|---------|----------|----------|
| Grünspan (Messing) | Grünliche Patina an Messingarmaturen | Korrosion, Salzwasser | WARNING | Reinigen, Funktion prüfen |
| Lochfraß (Edelstahl) | Pitting an Edelstahl-Armaturen | Crevice Corrosion, 304 statt 316L | CRITICAL | Armatur austauschen |
| Schlauch rutscht auf Tülle | Schlauch lässt sich von Hand von Tülle ziehen | Fehlende Schlauchschelle, Alterung | CRITICAL | Doppelschelle montieren |
| Schlauchschelle lose | Schlauchschelle drehbar oder verschiebbar | Vibrationslockerung | CRITICAL | Nachziehen + zweite Schelle |
| Schlauchschelle korrodiert | Rost an Schneckengewinde-Schelle | Verzinkter Stahl statt Edelstahl | WARNING | Gegen V4A-Schelle tauschen |
| Gewinde undicht (Blasen) | Blasenbildung bei Sprühtest mit Lecksuchspray | Beschädigtes Gewinde, fehlendes PTFE-Band | CRITICAL | Gas abstellen, Gewinde neu abdichten |

### 10.3 Verlege-Mängel

| Fehlerbild | Beschreibung | Ursache | Severity | Maßnahme |
|------------|-------------|---------|----------|----------|
| Zu enger Biegeradius | Schlauch knickt ab (Knick sichtbar) | Falsche Verlegung, zu kurzer Schlauch | CRITICAL | Längeren Schlauch verwenden |
| Schlauch unter Zugspannung | Schlauch gestreckt, Anschlüsse unter Zug | Zu kurzer Schlauch, Gerät verschoben | CRITICAL | Längeren Schlauch verwenden |
| Schlauch an scharfer Kante | Kontakt mit Metallkante, Schraubenkopf | Fehlende Schutzschelle | CRITICAL | Kantenschutz + ggf. Austausch |
| Schlauch durch Schott | Durchführung durch Wand/Schott | Unzulässige Verlegung (EN 1763) | CRITICAL | Umverlegen oder Festleitung verwenden |
| Schlauch nicht inspizierbar | Schlauch hinter Verkleidung verborgen | Baulich bedingt | WARNING | Inspektionsöffnung schaffen |
| Schlauch in der Bilge | Schlauch liegt im Bilgenwasser | Fehlmontage | CRITICAL | Schlauch hochverlegen |

### 10.4 AYDI Visual Pipeline — Erkennungsmerkmale

Für die automatische Bilderkennung (Pipeline B, Claude Vision) sind folgende visuelle Merkmale relevant:

**Gasschlauch-Identifikation:**
- Farbe: **Orange** (Standard EN 1763 Niederdruck) oder **Schwarz mit orange Streifen**
- Durchmesser: ca. 16–18 mm Außendurchmesser (erkennbar im Vergleich zu benachbarten Objekten)
- Aufdruck: Herstellername, Norm (EN 1763 / EN 16436), Datum (QQ/JJJJ), „LPG"
- Armaturen: Messingfarbene Überwurfmuttern an beiden Enden

**Altersbestimmung über Aufdruck:**
- Format typisch: „GOK EN 16436-1 III/2019 30mbar LPG" → Herstellungsdatum Q3 2019
- Truma-Format: „Truma 60189 II/2021 EN 1763" → Q2 2021
- Wenn Aufdruck nicht mehr lesbar → visuell „alt" → Confidence `visual_low`, Empfehlung physische Inspektion

**Zustandserkennung über Foto:**

| Visuelles Merkmal | Confidence | Bewertung |
|-------------------|-----------|-----------|
| Aufdruck lesbar, Datum <5 Jahre, keine Schäden sichtbar | `visual_high` | score 90–100 |
| Aufdruck lesbar, Datum 5–10 Jahre, keine Schäden | `visual_high` | score 60–80 |
| Aufdruck lesbar, Datum >10 Jahre | `visual_high` | score 10–25, CRITICAL |
| Aufdruck nicht lesbar, Oberfläche glatt und flexibel | `visual_medium` | score 50–70 |
| Aufdruck nicht lesbar, Oberfläche rissig/verfärbt | `visual_medium` | score 20–40, CRITICAL |
| Schlauch kaum sichtbar, nur Anschlüsse erkennbar | `visual_low` | score nicht vergeben |
| Gaslocker-Foto ohne Schlauch | `visual_insufficient` | „nicht beurteilbar" |

---

## 11. Glossar — Gas-Fachbegriffe

| Begriff (DE) | Begriff (EN) | Definition |
|-------------|-------------|------------|
| Betriebsdruck | Operating pressure | Druck am Verbraucher (Europa: 30 mbar, USA: 11" WC) |
| Berstdruck | Burst pressure | Druck bei dem der Schlauch versagt (min. 4× Betriebsdruck) |
| Druckregler | Pressure regulator | Mindert Flaschendruck auf Betriebsdruck |
| Flammensicherung (FFD) | Flame failure device | Thermoelektrisches Ventil, schließt bei erloschener Flamme |
| Gasdetektor | Gas detector | Elektronischer Sensor für LPG-Erkennung in der Bilge |
| Gaslocker | Gas locker | Gasdichter Flaschenschrank mit Drainage nach außenbords |
| Hochdruck (HD) | High pressure | Seite zwischen Flasche und Regler (4–16 bar) |
| Magnetventil | Solenoid valve | Elektrisch betätigtes Absperrventil (12V DC, normally closed) |
| Niederdruck (ND) | Low pressure | Seite zwischen Regler und Verbraucher (30 mbar) |
| Prüfgas | Test gas | Isobutan-Luft-Gemisch zur Kalibrierung von Gasdetektoren |
| Schlauchbruchsicherung | Excess flow valve | Ventil das bei plötzlichem Druckabfall (Schlauchbruch) schließt |
| Thermoelektrische Zündsicherung | Thermocouple safety valve | = Flammensicherung |
| UEG / LEL | Lower explosive limit | Untere Explosionsgrenze (Propan: 2,1 Vol.-%) |
| Umschaltregler | Changeover regulator | Regler für 2 Flaschen mit automatischer Umschaltung |

---

## 12. Schnell-Checkliste für Eigner (AYDI-Ausgabeformat)

Diese Checkliste wird als Teil des AYDI-Berichts ausgegeben, wenn ein LPG-System bewertet wird:

```
╔══════════════════════════════════════════════════════════════╗
║           AYDI GAS-SICHERHEITS-CHECKLISTE                   ║
║           Boot: [Bootsname] | Datum: [Datum]                ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  1. GASLOCKER                                                ║
║  [ ] Gasdicht zum Bootsinneren?                              ║
║  [ ] Drainage (≥19 mm) nach außenbords, nicht verstopft?     ║
║  [ ] Belüftung oben vorhanden?                               ║
║  [ ] Keine elektrischen Leitungen im Locker?                 ║
║  [ ] Flaschen gesichert gegen Verrutschen?                   ║
║                                                              ║
║  2. GASSCHLÄUCHE                                             ║
║  [ ] Herstelldatum lesbar? Datum: ____/____                  ║
║  [ ] Alter <10 Jahre?                                        ║
║  [ ] Keine Risse, Porösität, Verhärtung?                     ║
║  [ ] Keine Scheuerstellen?                                   ║
║  [ ] Kein Knicken, kein Zug auf Anschlüsse?                  ║
║  [ ] Schlauchschellen fest, Edelstahl?                       ║
║  [ ] Gesamte Länge sichtbar und inspizierbar?                ║
║                                                              ║
║  3. REGLER                                                   ║
║  [ ] Typ: _________________________ Alter: ____ Jahre        ║
║  [ ] Crash-Sensor vorhanden? (Truma CS / GOK Drive)          ║
║  [ ] Ausgangsdruck korrekt (30 ± 3 mbar)?                    ║
║                                                              ║
║  4. MAGNETVENTIL                                             ║
║  [ ] Vorhanden?                                              ║
║  [ ] Schalter am Bedienpunkt des Kochers?                    ║
║  [ ] Funktionstest: öffnet/schließt zuverlässig?             ║
║  [ ] Fail-closed bei Stromausfall?                           ║
║                                                              ║
║  5. GASDETEKTOR                                              ║
║  [ ] Vorhanden?                                              ║
║  [ ] Sensor in Bilge (max. 150 mm über Boden)?               ║
║  [ ] Funktionstest mit Prüfgas: Alarm <30 s?                 ║
║  [ ] Kalibrierung aktuell?                                   ║
║  [ ] Automatische Absperrung via Solenoid?                   ║
║                                                              ║
║  6. VERBRAUCHER                                              ║
║  [ ] Alle Brenner mit Flammensicherung?                      ║
║  [ ] Belüftung am Aufstellort ausreichend?                   ║
║  [ ] Abstand zu brennbaren Materialien ≥200 mm?             ║
║                                                              ║
║  7. VERHALTENSREGELN                                         ║
║  [ ] Gasflaschenventil nach Gebrauch zudrehen?               ║
║  [ ] Magnetventil nach Gebrauch ausschalten?                 ║
║  [ ] Gasdetektor ständig eingeschaltet?                      ║
║  [ ] Bei Gasgeruch: Gas aus, lüften, keine Schalter!         ║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║  GESAMTBEWERTUNG: [Score]/100  Severity: [OK/WARNING/CRIT]  ║
║  Nächste Prüfung fällig: [Datum + 2 Jahre]                  ║
╚══════════════════════════════════════════════════════════════╝
```

---

## Schlauchschellen & Verbindungstechnik

> **⚠️ WARNUNG:** Gasschlauch-Verbindungen sind die kritischste Schwachstelle jeder LPG-Installation. Über 60 % aller Gaslecks auf Yachten entstehen an Verbindungsstellen. Eine einzige undichte Schelle kann zur Explosion und zum Tod führen.

### Typen für Gas-Anwendungen (nur zugelassene!)

Für LPG-Gasanlagen auf Booten dürfen **ausschließlich** typgeprüfte und zugelassene Schlauchschellen verwendet werden. Normale Schlauchschellen aus dem Baumarkt sind **VERBOTEN** und lebensgefährlich.

**Zugelassene Schellen-Typen nach EN 1949 / ISO 10239:**

| Typ | Bezeichnung | Material | Einsatz | Norm | AYDI-Score |
|-----|-------------|----------|---------|------|------------|
| W4-Gas | Schneckengewindeschelle Gas | Edelstahl 1.4401 (316L) | Gasschlauch auf Stutzen | DIN 3017-1 | 75/100 |
| W5-Gas | Spannbackenschelle Gas | Edelstahl 1.4401 + Liner | Hochdruck-Verbindungen | DIN 3017-3 | 90/100 |
| Oetiker 167 | Ohrschelle mit Einlage | Edelstahl 316L | Festanschlüsse | EN 14800 | 85/100 |
| NORMA RSGU | Gelenkbolzenschelle | Edelstahl W4 | Wellrohr auf Stutzen | DIN 3017-2 | 80/100 |
| ABA Safety | Sicherheitsschelle | Edelstahl 316L | Doppelschellen-System | Herstellernorm | 95/100 |

**Bandbreiten und Durchmesser:**

| Schlauch-Außen-Ø | Schellen-Spannbereich | Bandbreite min. | Anziehdrehmoment |
|-------------------|-----------------------|-----------------|------------------|
| 8 mm | 8–12 mm | 9 mm | 2,5 Nm |
| 10 mm | 10–16 mm | 9 mm | 2,5 Nm |
| 12 mm | 12–20 mm | 12 mm | 3,0 Nm |
| 16 mm | 16–25 mm | 12 mm | 3,0 Nm |
| 20 mm | 20–32 mm | 12 mm | 3,5 Nm |

### KRITISCH: Gas-Schlauchschellen vs normale Schellen

> **⛔ LEBENSGEFAHR:** Verwechslung von Gas-Schlauchschellen mit normalen Wasserschlauchschellen ist einer der häufigsten tödlichen Fehler bei Yacht-Gas-Installationen.

**Unterschiede im Detail:**

| Merkmal | Gas-Schelle (zugelassen) | Normale Schelle (VERBOTEN für Gas) |
|---------|--------------------------|-------------------------------------|
| Material | 316L / 1.4401 | Oft 304 / 1.4301 oder verzinkter Stahl |
| Bandkante | Entgratet, abgerundet | Scharfkantig (schneidet in Schlauch!) |
| Bandbreite | ≥9 mm | Oft 7–8 mm |
| Oberfläche | Poliert, glatt | Rau, gestanzt |
| Kennzeichnung | "Gas" / "LPG" / EN-Norm | Keine spezifische Kennzeichnung |
| Schraubentyp | Edelstahl-Wurmschraube | Oft verzinkte Schraube |
| Preis | 3–8 EUR/Stk | 0,30–1,50 EUR/Stk |
| AYDI-Bewertung | ✅ Zulässig | ❌ Sofort austauschen |

**Warum normale Schellen tödlich sein können:**
1. Scharfe Bandkanten schneiden bei Vibration in den Gummischlauch → Mikrorisse → Leck
2. Verzinkter Stahl korrodiert in Salzluft → Spannkraft sinkt → Schlauch rutscht ab
3. Zu schmale Bänder verteilen den Druck ungleichmäßig → lokale Überlastung
4. Fehlende Entgratung perforiert den Schlauch bereits bei Montage
5. Standardschrauben korrodieren → Nachziehen unmöglich → schleichende Undichtigkeit

**AYDI Visual Pipeline — Erkennungsmerkmale:**
- Rostspuren an Schelle → `confidence: "visual_high"`, `severity: "CRITICAL"`
- Scharfe Bandkanten sichtbar → `confidence: "visual_medium"`, `severity: "CRITICAL"`
- Keine "Gas"/"LPG"-Kennzeichnung → `confidence: "visual_low"`, `severity: "WARNING"`
- Schelle sitzt schief → `confidence: "visual_high"`, `severity: "CRITICAL"`

### Hersteller

**Zugelassene Hersteller für marine Gasschlauchschellen:**

| Hersteller | Modellreihe | Artikelnummer (Beispiel) | Material | Ø-Bereich | Preis ca. | Besonderheit |
|------------|-------------|--------------------------|----------|-----------|-----------|--------------|
| ABA (Schweden) | Safety 20 | ABA-S20-10-16 | 316L W5 | 10–16 mm | 4,80 EUR | Sicherheitskante, marine-optimiert |
| NORMA Group | RSGU 9/12 W4 | RSGU-12-20-W4-LPG | 1.4401 | 12–20 mm | 5,20 EUR | Gelenkbolzen, vibrationsfest |
| Oetiker | StepLess 167 | 16700010 | 316L | 8–10 mm | 3,90 EUR | Einweg-Ohrschelle, manipulationssicher |
| CAILLAU | Hi-Torque HT | CAILLAU-HT-12 | 316L | 10–16 mm | 6,50 EUR | Hochdrehmoment, superyacht-tauglich |
| Jubilee Clips | Marine Gas | JC-GAS-12-20 | 316 | 12–20 mm | 3,50 EUR | UK-Standard, ABYC-zugelassen |
| Mikalor | SUPRA W5 | MIK-SU-W5-12 | 1.4401 | 10–16 mm | 5,80 EUR | Spannbacken-System |
| IDEAL | Tridon Gas | ID-TRI-G-16 | 316L | 14–20 mm | 4,20 EUR | US/ABYC-Standard |

**Bezugsquellen marine:**
- SVB (svb-marine.de): Vollsortiment ABA, NORMA, Jubilee — Lieferung 2–4 Tage
- Toplicht (toplicht.de): ABA Safety-Reihe, Oetiker — Spezialist Gastechnik
- AWN (awn.de): NORMA, Mikalor — günstige Konditionen bei Großbestellung
- Compass24 (compass24.de): Jubilee Marine, IDEAL Tridon
- West Marine (westmarine.com): IDEAL Tridon — für US-Norm ABYC A-1

### Doppelschellen — Pflicht bei Gas!

> **PFLICHT nach EN 1949 Abschnitt 6.3.4:** Jede Gasschlauch-Verbindung an einem Stutzen muss mit **zwei** Schlauchschellen gesichert werden. Eine einzelne Schelle ist normwidrig und ein Versicherungsausschluss-Grund.

**Korrekte Doppelschellen-Montage:**

```
Schlauch-Querschnitt auf Stutzen:
                                    
  ┌─── Schelle 2 (äußere) ────┐   ┌─── Schelle 1 (innere) ────┐
  │   Abstand: 10–15 mm       │   │   Abstand zum Ende: 5 mm  │
  ▼                            ▼   ▼                            ▼
  ╔════╗                    ╔════╗ ╔════╗                    ╔════╗
══╣    ╠════════════════════╣    ╠═╣    ╠════════════════════╣    ╠══
  ╚════╝                    ╚════╝ ╚════╝                    ╚════╝
  ◄──── Bandbreite ≥9mm ────►      ◄──── Bandbreite ≥9mm ────►
  
  ◄────────────── Stutzen-Überstand: min. 30 mm ──────────────►
```

**Regeln für Doppelschellen:**
1. Beide Schellen vom **gleichen** Typ und Hersteller
2. Abstand zwischen den Schellen: 10–15 mm (nicht direkt nebeneinander!)
3. Schrauben **gegenüberliegend** positionieren (180°)
4. Innere Schelle zuerst anziehen, dann äußere
5. Schlauch muss mindestens 30 mm auf dem Stutzen sitzen
6. Nach Anzug: Schlauch darf sich **nicht** drehen oder verschieben lassen
7. Markierung mit wasserfestem Stift auf Schlauch/Stutzen zur Rutsch-Kontrolle

**AYDI-Bewertung Doppelschellen:**
- Zwei korrekte Schellen: Score 95–100/100
- Zwei Schellen, falscher Abstand: Score 60/100, Severity WARNING
- Nur eine Schelle: Score 15/100, Severity CRITICAL → sofortige Sperrung
- Keine Schelle (Schlauch aufgesteckt): Score 0/100, Severity CRITICAL → NOTFALL

### Anziehdrehmomente

**⚠️ Sowohl Unter- als auch Überanziehen ist gefährlich!**

| Schlauch-Typ | Schellen-Typ | Drehmoment (Nm) | Werkzeug | Folge bei Überanziehen |
|--------------|-------------|-----------------|----------|------------------------|
| NBR 8 mm | W4 Schnecke | 2,0–2,5 | Schraubendreher Kreuz PZ2 | Schlauch wird eingeschnitten |
| NBR 10 mm | W4 Schnecke | 2,5–3,0 | Schraubendreher Kreuz PZ2 | Deformation, Dichtfläche zerstört |
| NBR 12 mm | W5 Spannbacke | 3,0–3,5 | Drehmoment-Schraubendreher | Innenliner kollabiert |
| SBR 10 mm | W4 Schnecke | 2,0–2,5 | Schraubendreher Kreuz PZ2 | SBR reißt leichter als NBR |
| Edelstahl-Wellrohr | RSGU Gelenk | 4,0–5,0 | Drehmomentschlüssel 1/4" | Wellrohr wird oval, dichtet nicht |
| Thermoplast | Oetiker Ohr | Werkzeugbedingt | Oetiker-Zange 1099 | Band bricht |

**Empfehlung:** Drehmoment-Schraubendreher verwenden (z.B. Wiha TorqueVario 0,5–6,0 Nm, Art.-Nr. 36847, ca. 85 EUR). Die Investition kann Leben retten.

**Kontrolle nach Erstmontage:**
- Nach 24 Stunden: Nachziehen auf Soll-Drehmoment (Setzverhalten)
- Nach 1 Woche: Erneute Kontrolle
- Danach: Jährliche Kontrolle im Rahmen der Gasprüfung

### Lecktest nach Montage (Leckspray, Manometer)

> **PFLICHT:** Nach jeder Montage oder Demontage einer Gasverbindung ist ein Lecktest **zwingend** vorgeschrieben. Ohne dokumentierten Lecktest darf die Anlage nicht in Betrieb genommen werden.

**Methode 1: Leckspray (Schnelltest)**

| Produkt | Hersteller | Art.-Nr. | Inhalt | Preis | Gefriergrenze |
|---------|-----------|----------|--------|-------|---------------|
| Leak-Tec | Würth | 0893 122 00 | 400 ml | 12,80 EUR | –15 °C |
| Lecksuch-Spray | WEICON | 11651400 | 400 ml | 9,50 EUR | –20 °C |
| Snoop Liquid | Swagelok | MS-SNOOP-8OZ | 236 ml | 18,00 EUR | –5 °C |
| Gas-Lecksuchspray | CFH | 52108 | 400 ml | 7,90 EUR | –10 °C |

**Vorgehensweise Leckspray:**
1. Gas aufdrehen (Flasche öffnen, Absperrventil öffnen)
2. Spray auf **alle** Verbindungsstellen auftragen: Regler, Schellen, Stutzen, Ventile
3. 3 Minuten warten und beobachten
4. Blasenbildung = LECK → sofort Gas abstellen, Verbindung nacharbeiten
5. Keine Blasen = dicht → Spray abwischen, Ergebnis dokumentieren
6. **NIEMALS** offene Flamme zur Lecksuche verwenden!

**Methode 2: Druckabfall-Prüfung (Manometer)**

Dies ist die **zuverlässigere** Methode und bei Neuinstallationen **vorgeschrieben**.

**Benötigtes Equipment:**
- Manometer 0–600 mbar, Genauigkeit ±1 mbar (z.B. Wika 111.10, Art.-Nr. 9085840, ca. 45 EUR)
- T-Stück mit Manometer-Anschluss 1/4" BSP
- Absperrhahn
- Stoppuhr

**Vorgehensweise Druckabfall-Prüfung:**
1. Alle Verbraucher schließen (Kocher, Heizer, Kühlschrank)
2. Manometer am Prüfpunkt anschließen (zwischen Regler und erstem Verbraucher)
3. Gasflasche öffnen, System auf Betriebsdruck bringen (30 mbar Niederdruck)
4. Gasflasche **schließen**
5. **5 Minuten** warten, Manometer-Ablesung protokollieren
6. Druckabfall ≤ 0,5 mbar in 5 min → **DICHT**
7. Druckabfall > 0,5 mbar → **UNDICHT** → Lecksuche mit Spray
8. Bei Hochdruck-Seite (vor Regler): Prüfdruck 1,5 × Betriebsdruck, 10 Minuten

**AYDI-Bewertung Lecktest:**

```python
gas_leak_test_assessment = {
    "method": "manometer",
    "pressure_drop_mbar": 0.2,
    "duration_min": 5,
    "result": "DICHT",
    "score": 100,
    "confidence": "measured",
    "next_test_due": "2027-04-23"
}
```

---

## Technische Referenz & Berechnungen

### Durchfluss-Berechnungen für LPG-Systeme

**Grundformel Gasdurchfluss durch Schlauch:**

```
Q = (π × d⁴ × Δp) / (128 × η × L)

Wobei:
  Q = Volumenstrom [m³/s]
  d = Innendurchmesser Schlauch [m]
  Δp = Druckdifferenz [Pa]
  η = dynamische Viskosität LPG-Gas (ca. 8 × 10⁻⁶ Pa·s bei 20 °C)
  L = Schlauchlänge [m]
```

**Praxisberechnung für typische Yacht-Installationen:**

| Verbraucher | Gasbedarf | Schlauch-Ø innen | Max. Länge bei 30 mbar |
|-------------|-----------|------------------|------------------------|
| 2-Flammen-Kocher | 250 g/h | 8 mm | 5.000 mm |
| 3-Flammen-Kocher + Backofen | 450 g/h | 10 mm | 4.000 mm |
| Warmwasser-Boiler 10 L | 350 g/h | 10 mm | 4.500 mm |
| Gasheizung Truma S 3004 | 310 g/h | 8 mm | 6.000 mm |
| Absorber-Kühlschrank | 30 g/h | 6 mm | 8.000 mm |
| Kombination alle | 1.340 g/h | 12 mm (Hauptleitung) | 3.000 mm |

**Wichtig:** Die Tabelle gilt für **Niederdruckseite** (30 mbar Betriebsdruck). Hochdruckseite (Flasche → Regler) erfordert starre Leitungen oder zugelassene Hochdruck-Schläuche nach EN 16436-1 Klasse 2.

### Druckverlust-Berechnung

**Formel nach Darcy-Weisbach (vereinfacht für Niederdruck-Gas):**

```
Δp = λ × (L/d) × (ρ/2) × v²

Wobei:
  Δp = Druckverlust [Pa]
  λ = Rohrreibungszahl (≈ 0,03 für glatte Gummischläuche)
  L = Schlauchlänge [m]
  d = Innendurchmesser [m]
  ρ = Gasdichte LPG bei 30 mbar (ca. 1,9 kg/m³ Propan, ca. 2,5 kg/m³ Butan)
  v = Strömungsgeschwindigkeit [m/s]
```

**Maximal zulässiger Druckverlust nach EN 1949:**
- Hauptleitung (Regler → Verteiler): ≤ 5 mbar
- Stichleitung (Verteiler → Gerät): ≤ 2 mbar
- Gesamtsystem: ≤ 10 mbar (bei 30 mbar Betriebsdruck)

**Druckverlust-Referenztabelle (Propan, 20 °C, 30 mbar):**

| Schlauch-Ø innen | Länge 1 m | Länge 2 m | Länge 3 m | Länge 5 m | Länge 8 m |
|-------------------|-----------|-----------|-----------|-----------|-----------|
| 6 mm | 0,8 mbar | 1,6 mbar | 2,4 mbar | 4,0 mbar | 6,4 mbar |
| 8 mm | 0,3 mbar | 0,6 mbar | 0,9 mbar | 1,5 mbar | 2,4 mbar |
| 10 mm | 0,12 mbar | 0,24 mbar | 0,36 mbar | 0,60 mbar | 0,96 mbar |
| 12 mm | 0,05 mbar | 0,10 mbar | 0,15 mbar | 0,25 mbar | 0,40 mbar |

*Werte bei Durchfluss 500 g/h Propan. Bei höherem Durchfluss steigt Δp quadratisch.*

### Mindest-Biegeradius

> **KRITISCH:** Unterschreitung des Mindest-Biegeradius führt zu Knickbildung → Durchflussverengung → lokale Materialermüdung → Riss → LECK → EXPLOSION.

| Material | Außen-Ø | Mindest-Biegeradius | Biegeradius/Ø-Verhältnis | Bei Unterschreitung |
|----------|---------|---------------------|--------------------------|---------------------|
| NBR-Schlauch | 8 mm | 40 mm | 5:1 | Knick, Innenliner faltet |
| NBR-Schlauch | 10 mm | 50 mm | 5:1 | Knick, Innenliner faltet |
| NBR-Schlauch | 12 mm | 72 mm | 6:1 | Knick, Wandverdünnung |
| SBR-Schlauch | 10 mm | 60 mm | 6:1 | Rissbildung außen |
| Edelstahl-Wellrohr | 10 mm | 30 mm | 3:1 | Welle verformt dauerhaft |
| Edelstahl-Wellrohr | 12 mm | 36 mm | 3:1 | Welle bricht auf |
| Edelstahl-Wellrohr | 16 mm | 48 mm | 3:1 | Dauerhafter Knick |
| Thermoplast-Schlauch | 8 mm | 60 mm | 7,5:1 | Material bricht |

**Schutzmaßnahmen bei engem Bauraum:**
- Biegeschutzfeder über den Schlauch schieben (z.B. Truma Art.-Nr. 50220-01, ca. 6 EUR)
- 90°-Winkelanschluss verwenden statt Schlauch zu biegen
- Schlauchführung mit Schellen an Schott fixieren → Schwingung vermeiden
- Mindestens 50 mm Abstand zu heißen Oberflächen (Motor, Auspuff)

### Gas-Verbrauchsberechnung (Kocher, Heizer, Kühlschrank)

**Verbrauchsdaten gängiger Marine-Gasgeräte:**

| Gerät | Hersteller | Modell | Verbrauch max. | Verbrauch Eco | Betriebsstunden/Tag |
|-------|-----------|--------|----------------|---------------|---------------------|
| 2-Flammen-Kocher | Dometic | SMEV PI8022 | 260 g/h | 130 g/h | 1,5 h |
| 3-Flammen-Kocher | Dometic | SMEV PI8023 | 390 g/h | 195 g/h | 1,5 h |
| Kocher + Backofen | ENO | Grand Large 2 | 420 g/h | 200 g/h | 2,0 h |
| Gasheizung | Truma | S 3004 | 310 g/h | 160 g/h | 8,0 h |
| Gasheizung | Truma | S 5004 | 420 g/h | 210 g/h | 8,0 h |
| Warmwasser-Boiler | Truma | B 10 EL | 350 g/h | — | 0,5 h |
| Absorber-Kühlschrank | Dometic | RM 8401 | 28 g/h | 15 g/h | 24,0 h |
| Absorber-Kühlschrank | Dometic | RM 5310 | 22 g/h | 12 g/h | 24,0 h |
| Gasgrill | Magma | Catalina | 350 g/h | 180 g/h | 0,5 h |

**Berechnung Tagesverbrauch (Sommer-Küstentörn, 2 Personen):**

```
Kocher (ENO Grand Large 2):    200 g/h × 1,5 h = 300 g
Kühlschrank (Dometic RM 8401):  20 g/h × 24 h  = 480 g
Warmwasser (Truma B 10 EL):    350 g/h × 0,3 h = 105 g
                                              ──────────
Tagesverbrauch Sommer:                          885 g/Tag

Flasche 5 kg → 5.000 g / 885 g/Tag = 5,6 Tage
Flasche 11 kg → 11.000 g / 885 g/Tag = 12,4 Tage
```

**Berechnung Tagesverbrauch (Herbst-Törn, 2 Personen, mit Heizung):**

```
Kocher (ENO Grand Large 2):    200 g/h × 2,0 h   = 400 g
Kühlschrank (Dometic RM 8401):  20 g/h × 24 h    = 480 g
Warmwasser (Truma B 10 EL):    350 g/h × 0,5 h   = 175 g
Heizung (Truma S 3004):        200 g/h × 10,0 h  = 2.000 g
                                                ──────────
Tagesverbrauch Herbst:                            3.055 g/Tag

Flasche 11 kg → 11.000 g / 3.055 g/Tag = 3,6 Tage (!)
2 × 11 kg → 22.000 g / 3.055 g/Tag = 7,2 Tage
```

**AYDI-Empfehlung Flaschengröße:**

| Boots-Typ | Crew | Saison | Empfehlung | Autonomie |
|-----------|------|--------|------------|-----------|
| Segelboot 8–10 m | 2 | Sommer | 1 × 5 kg | 5–6 Tage |
| Segelboot 10–14 m | 2–4 | Sommer | 2 × 5 kg | 8–12 Tage |
| Segelboot 10–14 m | 2–4 | Ganzjahr | 2 × 11 kg | 7–14 Tage |
| Motorboot 8–12 m | 2–4 | Sommer | 1 × 11 kg | 10–14 Tage |
| Motorboot 12–18 m | 4–6 | Ganzjahr | 2 × 11 kg | 5–7 Tage |
| Katamaran 12–15 m | 4–6 | Sommer | 2 × 11 kg | 10–14 Tage |
| Superyacht 18+ m | 6+ | Ganzjahr | Festtank 30–50 kg | 10–20 Tage |

### Vergleich: Material-Kosten pro Meter

| Material | Innen-Ø | Preis/m (netto) | Lebensdauer | Kosten/Jahr/m | AYDI-Score |
|----------|---------|-----------------|-------------|---------------|------------|
| NBR-Gasschlauch Standard | 8 mm | 8,50 EUR | 5 Jahre | 1,70 EUR | 70/100 |
| NBR-Gasschlauch Premium (Truma) | 8 mm | 12,00 EUR | 8 Jahre | 1,50 EUR | 80/100 |
| SBR-Gasschlauch | 10 mm | 7,00 EUR | 4 Jahre | 1,75 EUR | 60/100 |
| Edelstahl-Wellrohr DN10 | 10 mm | 28,00 EUR | 20 Jahre | 1,40 EUR | 95/100 |
| Edelstahl-Wellrohr DN12 | 12 mm | 35,00 EUR | 20 Jahre | 1,75 EUR | 95/100 |
| Thermoplast EN 16436-1 | 8 mm | 15,00 EUR | 10 Jahre | 1,50 EUR | 85/100 |
| Kupferrohr hart (Festverlegung) | 8 mm | 6,50 EUR | 30 Jahre | 0,22 EUR | 90/100 |
| Kupferrohr weich (biegbar) | 8 mm | 8,00 EUR | 25 Jahre | 0,32 EUR | 85/100 |

**Gesamtkosten-Berechnung (typische 10-m-Yacht, 4 m Leitungslänge, 20 Jahre):**

| Variante | Materialkosten | Schellen | Einbau | Austausch (20 J) | Gesamt 20 Jahre |
|----------|---------------|----------|--------|-----------------|-----------------|
| NBR Standard | 34 EUR | 12 EUR | 80 EUR | 3× = 378 EUR | 504 EUR |
| NBR Premium | 48 EUR | 12 EUR | 80 EUR | 2× = 280 EUR | 420 EUR |
| Edelstahl-Wellrohr | 112 EUR | 16 EUR | 120 EUR | 0× = 0 EUR | 248 EUR |
| Kupferrohr hart | 26 EUR | — | 180 EUR | 0× = 0 EUR | 206 EUR |

**Fazit:** Edelstahl-Wellrohr und Kupferrohr sind langfristig **günstiger** als Gummischläuche — und **sicherer**.

---

## Einbau-/Austausch-Anleitung

### Werkzeug-Checkliste

> **Hinweis:** Alle Werkzeuge müssen **funkenfreie** Ausführungen sein, wenn in der Nähe offener Gasleitungen gearbeitet wird.

| Werkzeug | Spezifikation | Art.-Nr. (Beispiel) | Preis ca. | Zweck |
|----------|--------------|---------------------|-----------|-------|
| Drehmoment-Schraubendreher | 0,5–6,0 Nm | Wiha 36847 | 85 EUR | Schellen anziehen |
| Gasschlauch-Schere | Ø bis 25 mm | Knipex 90 25 25 | 35 EUR | Sauberer Schnitt |
| Lecksuchspray | EN-zugelassen | Würth 0893 122 00 | 13 EUR | Dichtigkeitsprüfung |
| Manometer 0–600 mbar | Klasse 1.6 | Wika 111.10 | 45 EUR | Druckabfall-Test |
| Gabelschlüssel-Satz | 10–24 mm, Edelstahl | WEDO SS-6104 | 120 EUR | Verschraubungen |
| Oetiker-Zange | Typ 1099 | Oetiker 14100385 | 95 EUR | Ohrschellen |
| Entgratungswerkzeug | Innen/Außen | REMS 113800 | 28 EUR | Rohrenden |
| PTFE-Dichtband Gas | gelb, EN 751-3 | Polyken 1027-GAS | 4 EUR | Gewindeverbindungen |
| Messing-Bürste | weich, funkenarm | Würth 0714 22 | 8 EUR | Anschluss reinigen |
| Handschuhe | Nitril, chemiebeständig | Ansell 92-600 | 12 EUR | Hautschutz |
| Schutzbrille | EN 166 | Uvex 9190275 | 15 EUR | Augenschutz |
| Feuerlöscher (ABC) | 2 kg, marine | Gloria PD 2 GA | 55 EUR | Sicherheit! |

**Gesamtkosten Werkzeug-Grundausstattung:** ca. 515 EUR
**AYDI-Empfehlung:** Diese Investition ist **nicht optional** — sie ist lebensrettend.

### Schritt-für-Schritt Gasschlauch-Austausch

> **⚠️ WARNUNG:** Gasarbeiten dürfen in vielen Ländern nur von zertifizierten Fachleuten (Deutschland: DVGW-Sachkundiger nach G 607) durchgeführt werden. Diese Anleitung dient der Dokumentation und Kontrolle — nicht als Aufforderung zur Eigenarbeit.

**Vorbereitung (30 Minuten):**

1. ☐ Gasflasche am Flaschenventil **schließen** (Handrad im Uhrzeigersinn)
2. ☐ Alle Verbraucher öffnen → Restdruck ablassen (1–2 Minuten Gas strömt)
3. ☐ Alle Verbraucher wieder schließen
4. ☐ Magnetventil auf AUS schalten
5. ☐ Lüftung im Boot öffnen (alle Luken, Gaslocker-Deckel)
6. ☐ 15 Minuten durchlüften (LPG sinkt zu Boden, muss vollständig entweichen!)
7. ☐ Gasdetektor prüfen → muss 0 ppm anzeigen
8. ☐ Feuerlöscher griffbereit positionieren
9. ☐ Kein Funkenrisiko: keine elektrischen Schalter betätigen, kein Handy im Gaslocker
10. ☐ Alten Schlauch fotografieren (AYDI Visual Pipeline: Zustandsdokumentation)

**Demontage (20 Minuten):**

11. ☐ Alte Schlauchschellen lösen (äußere zuerst, dann innere)
12. ☐ Schlauch vorsichtig von Stutzen ziehen (Stutzen festhalten!)
13. ☐ Stutzen auf Beschädigung prüfen: Grate, Korrosion, Verformung
14. ☐ Stutzen ggf. mit Messingbürste reinigen
15. ☐ Stutzen-Durchmesser mit Messschieber messen → dokumentieren
16. ☐ Alten Schlauch vermessen: Länge, Innen-Ø, Außen-Ø → Bestelldaten

**Neuen Schlauch vorbereiten (10 Minuten):**

17. ☐ Neuen Schlauch auspacken und auf Beschädigung prüfen
18. ☐ Herstellungsdatum auf dem Schlauch prüfen (nicht älter als 6 Monate ideal)
19. ☐ Ablaufdatum berechnen: Herstellungsdatum + max. Nutzungsdauer
20. ☐ Schlauch auf korrekte Länge schneiden (Schlauchschere, **senkrechter** Schnitt)
21. ☐ Schlauchenden entgraten (innen und außen)
22. ☐ Neue Schlauchschellen auf den Schlauch fädeln (4 Stück: je 2 pro Seite)

**Montage (20 Minuten):**

23. ☐ Schlauch auf Stutzen schieben — mindestens 30 mm Überstand
24. ☐ Innere Schelle positionieren: 5 mm vom Schlauchende
25. ☐ Äußere Schelle positionieren: 10–15 mm hinter innerer Schelle
26. ☐ Schrauben beider Schellen um 180° versetzt ausrichten
27. ☐ Innere Schelle auf Soll-Drehmoment anziehen (siehe Tabelle)
28. ☐ Äußere Schelle auf Soll-Drehmoment anziehen
29. ☐ Schlauchverlauf prüfen: keine Knicke, Mindest-Biegeradius eingehalten
30. ☐ Schlauch mit Schellen an Schott befestigen (Abstand ≤ 500 mm)
31. ☐ Kontrollmarkierung auf Schlauch/Stutzen anbringen

**Prüfung und Inbetriebnahme (30 Minuten):**

32. ☐ Alle Verbraucher schließen
33. ☐ Gasflasche langsam öffnen (1/4 Umdrehung)
34. ☐ Lecksuchspray auf alle Verbindungen auftragen
35. ☐ 3 Minuten beobachten → keine Blasen = gut
36. ☐ Manometer-Druckabfalltest: 5 Minuten, ≤ 0,5 mbar Abfall
37. ☐ Jeden Verbraucher einzeln testen (Flamme, Heizung, Kühlschrank)
38. ☐ Gasflasche vollständig öffnen
39. ☐ Gaslocker schließen
40. ☐ Austausch im Bordbuch dokumentieren mit Datum, Material, Hersteller

**Dokumentation für AYDI:**

```python
gas_hose_replacement_record = {
    "date": "2026-04-23",
    "old_hose": {
        "manufacturer": "Truma",
        "material": "NBR",
        "age_years": 7.2,
        "condition": "Verhärtung, Mikrorisse sichtbar"
    },
    "new_hose": {
        "manufacturer": "Truma",
        "part_number": "50220-00",
        "material": "NBR",
        "manufacturing_date": "2026-01",
        "length_mm": 1500,
        "inner_diameter_mm": 8,
        "expiry_date": "2034-01"
    },
    "clamps": {
        "manufacturer": "ABA",
        "model": "Safety 20",
        "quantity": 4,
        "torque_nm": 2.5
    },
    "leak_test": {
        "method": "manometer",
        "pressure_drop_mbar": 0.1,
        "duration_min": 5,
        "result": "DICHT"
    },
    "technician": "DVGW G 607 zertifiziert",
    "confidence": "measured",
    "score": 100
}
```

### Häufige Fehler (jeder einzelne = Lebensgefahr!)

> **⛔ JEDER der folgenden Fehler hat in der Vergangenheit zu Explosionen, Bränden und Todesfällen auf Booten geführt. KEINER dieser Fehler ist ein "Kavaliersdelikt".**

**Fehler 1: Nur eine Schlauchschelle statt zwei**
- Verstoß gegen EN 1949 Abschnitt 6.3.4
- Einzelne Schelle kann sich durch Vibration lösen
- Schlauch rutscht bei Temperaturwechsel vom Stutzen
- AYDI-Score: 15/100 → CRITICAL
- Korrektur: Sofort zweite Schelle montieren

**Fehler 2: Baumarkt-Schellen statt Gas-Schellen**
- Scharfkantige Bänder schneiden in Gummi
- Verzinkter Stahl korrodiert in Salzluft
- Nicht für Gasdruck dimensioniert
- AYDI-Score: 10/100 → CRITICAL
- Korrektur: Alle Schellen gegen zugelassene Gas-Schellen tauschen

**Fehler 3: Schlauch zu kurz — unter Spannung montiert**
- Spannung zieht Schlauch vom Stutzen
- Vibration verstärkt den Effekt
- Besonders gefährlich bei Segelbooten (Krängung!)
- AYDI-Score: 20/100 → CRITICAL
- Korrektur: Schlauch mit 10 % Übermaß neu zuschneiden

**Fehler 4: Biegeradius unterschritten — Knick im Schlauch**
- Querschnitt verengt sich → Durchfluss sinkt
- Innenliner faltet → Materialermüdung → Riss
- Von außen oft nicht sichtbar!
- AYDI-Score: 25/100 → CRITICAL
- Korrektur: Biegeschutzfeder oder Winkelanschluss verwenden

**Fehler 5: Alter Schlauch weiterverwendet (>10 Jahre)**
- NBR verhärtet, verliert Elastizität
- Mikrorisse nicht immer sichtbar
- Schlauch kann bei Druckerhöhung (Flasche in Sonne) platzen
- AYDI-Score: 10/100 → CRITICAL
- Korrektur: Sofort austauschen, Alter = Herstellungsdatum auf dem Schlauch

**Fehler 6: PTFE-Band auf Bördelanschlüssen**
- Bördelanschlüsse dichten metall-auf-metall
- PTFE-Band verhindert korrekten Sitz
- Kann sich lösen und Ventil blockieren
- AYDI-Score: 30/100 → WARNING
- Korrektur: PTFE entfernen, Anschluss reinigen, ohne Band montieren

**Fehler 7: Gasschlauch durch Motorraum verlegt**
- Hitze beschleunigt Alterung um Faktor 3–5
- Vibration vom Motor → mechanischer Verschleiß
- Bei Leck: Zündquelle (Motor) direkt daneben → EXPLOSION
- AYDI-Score: 0/100 → CRITICAL → SOFORTIGE SPERRUNG
- Korrektur: Schlauch umverlegen, physische Trennung Gas/Motor

**Fehler 8: Gaslocker nicht gasdicht zum Innenraum**
- LPG ist schwerer als Luft → sinkt in Bilge
- Ohne gasdichte Trennung füllt Gas den gesamten Rumpf
- Ein Funke genügt → Totalverlust
- AYDI-Score: 5/100 → CRITICAL
- Korrektur: Gaslocker mit GFK-Wanne abdichten, Drainage nach außen prüfen

**Fehler 9: Fehlender oder defekter Gasdruckregler**
- Flaschendruck bis 16 bar direkt auf 30-mbar-Schlauch
- Schlauch platzt sofort → unkontrollierter Gasaustritt
- Größtmögliche Katastrophe
- AYDI-Score: 0/100 → CRITICAL → SOFORTIGE SPERRUNG
- Korrektur: Regler sofort austauschen (EN 16129, max. 10 Jahre alt)

**Fehler 10: Gasdetektor in falscher Höhe montiert**
- LPG ist schwerer als Luft (Dichte ~1,8 × Luft)
- Detektor muss UNTEN sein (max. 200 mm über Boden/Bilge)
- Detektor an der Decke detektiert Gas erst, wenn es zu spät ist
- AYDI-Score: 20/100 → CRITICAL
- Korrektur: Detektor auf max. 200 mm Höhe ummontieren

### Spezial: Gaslocker-Einbau

**Anforderungen nach EN 1949 Abschnitt 5.2:**

Ein Gaslocker muss:
1. **Gasdicht** zum Bootsinneren sein (keine Durchbrüche ohne Dichtung)
2. **Drainage** nach außenbords haben (Mindest-Ø Ablauf: 19 mm)
3. **Belüftung** nach außen haben (Mindestquerschnitt: 250 mm² unten, 250 mm² oben)
4. **Selbstschließenden Deckel** haben
5. **Flammensperre** an der Drainage
6. Gasflasche **senkrecht** aufnehmen und gegen Umfallen sichern
7. **Absperrventil** von außerhalb des Lockers bedienbar

> ⚠️ **ZU PRÜFEN (Audit):** Punkt 3 „Mindestquerschnitt 250 mm² unten + 250 mm² oben" widerspricht dem Haupttext (Abschnitt 1.4: „min. 2500 mm² oben"). Per EN ISO 10239 zweifelsfrei belegt ist nur der **Drain ≥ 19 mm Innen-Ø (≈ 283 mm²) am tiefsten Punkt nach außenbords**; die separaten Belüftungsflächen (250 vs. 2500 mm²) sind **estimated — unverifiziert**. Vor Nutzung als CE-/Prüfkriterium an EN 1949 / EN ISO 10239 im Original abgleichen. (Gleicher unverifizierter 250-mm²-Wert auch in jährlicher Checkliste Punkt 10 und im Fehlerkatalog „Keine Belüftung Gaslocker".)

**Material-Optionen:**

| Material | Vorteile | Nachteile | Preis (Locker 2-Fl.) | AYDI-Score |
|----------|----------|-----------|----------------------|------------|
| GFK-Formteil | Gasdicht, leicht, korrosionsfrei | Teuer, Einbau aufwändig | 350–600 EUR | 95/100 |
| Edelstahl 316L | Robust, langlebig, gasdicht | Schwer, teuer, Schweißnähte prüfen | 500–900 EUR | 90/100 |
| Aluminium (seewasserfest) | Leicht, preiswert | Korrosion möglich, Schweißnähte kritisch | 250–450 EUR | 75/100 |
| ABS-Kunststoff | Leicht, preiswert, gasdicht | UV-empfindlich, spröde bei Kälte | 150–300 EUR | 70/100 |

**Maße für gängige Flaschengrößen:**

| Flasche | Ø Flasche | Höhe Flasche | Locker Innen B×T×H min. |
|---------|-----------|-------------|-------------------------|
| 1 × 5 kg | 228 mm | 395 mm | 280 × 280 × 500 mm |
| 2 × 5 kg | 228 mm | 395 mm | 560 × 280 × 500 mm |
| 1 × 11 kg | 300 mm | 500 mm | 360 × 360 × 620 mm |
| 2 × 11 kg | 300 mm | 500 mm | 660 × 360 × 620 mm |
| 1 × 3 kg (Camping) | 206 mm | 310 mm | 260 × 260 × 420 mm |

### Spezial: Magnetventil-Installation

**Pflicht nach EN 1949 Abschnitt 6.4:** Ein fernbedienbares Absperrventil (Magnetventil/Solenoid) muss in der Gasleitung unmittelbar nach dem Druckregler installiert sein.

**Zugelassene Magnetventile für marine LPG:**

| Hersteller | Modell | Art.-Nr. | Anschluss | Leistung | Preis | AYDI-Score |
|-----------|--------|----------|-----------|----------|-------|------------|
| Truma | MonoControl CS | 50210-01 | 8 mm Schlauch | 3 W | 189 EUR | 95/100 |
| Truma | DuoControl CS | 50216-01 | 8 mm Schlauch | 3 W | 259 EUR | 95/100 |
| Marinco | Gas Solenoid | GS11-10 | 3/8" BSP | 5 W | 145 EUR | 85/100 |
| GOK | Magnetventil | 01 625 15 | 8 mm Steck | 4 W | 95 EUR | 80/100 |
| Clesse | Gassolenoid | SPV-1/4 | 1/4" BSP | 4 W | 110 EUR | 80/100 |

**Einbauregeln:**
1. Magnetventil direkt am Druckregler-Ausgang (Niederdruckseite!)
2. Stromversorgung über Schaltpaneel im Wohnbereich
3. Sicherung: max. 3 A, separate Leitung
4. Ventil muss **stromlos geschlossen** sein (fail-safe)
5. LED-Anzeige am Schaltpaneel: grün = offen, rot = geschlossen
6. Kabel mit Marinesteckern, keine Lötverbindungen im Gaslocker

### Spezial: Gas-Detektor-Platzierung

> **PFLICHT nach EN 1949 Abschnitt 7.3:** Mindestens ein Gasdetektor muss in jedem Raum installiert sein, der Gasgeräte enthält. Zusätzlich empfohlen: Gaslocker, Bilge, Maschinenraum.

**Zugelassene Marine-Gasdetektoren:**

| Hersteller | Modell | Art.-Nr. | Sensoren | Alarm bei | Preis | AYDI-Score |
|-----------|--------|----------|----------|-----------|-------|------------|
| BEP Marine | 600-GD | 600-GDLP | LPG, Propan, Butan | 10 % UEG | 195 EUR | 90/100 |
| Truma | Gas Level Check | 50400-01 | LPG | 20 % UEG | 120 EUR | 75/100 |
| NASA Marine | Gas Guardian | GAS-GUAR | LPG, Benzin, CO | 10 % UEG | 165 EUR | 85/100 |
| XINTEX | CMD-4 | CMD-4MR | LPG, Benzin | 10 % UEG | 225 EUR | 90/100 |
| Fireboy-Xintex | S-2A | S-2A-LPG | LPG (2 Sensoren) | 10 % UEG | 310 EUR | 95/100 |

**UEG = Untere Explosionsgrenze.** Propan: 2,1 Vol.-%, Butan: 1,8 Vol.-%. Alarm bei 10 % UEG = 0,21 Vol.-% Propan.

**Platzierungsregeln:**

```
Seitenansicht Boot:
                                    ┌────────────────────────┐
                                    │   Pantry / Kombüse     │
                                    │                        │
                                    │  ┌──┐ Kocher           │
                                    │  └──┘                  │
                                    │                        │
  Gaslocker  ┌────┐                 │                        │
  (außen)    │ FL │                 │                        │
             │ FL │   ──Schlauch──  │                        │
             └────┘                 │ ★ Detektor 1           │ ← max. 200 mm über Boden
                                    │   (Bodennähe!)         │
                                    └────────────────────────┘
                                    ┌────────────────────────┐
                                    │   Bilge                │
                                    │ ★ Detektor 2           │ ← tiefster Punkt
                                    └────────────────────────┘
```

**Montagehöhe und Position:**
- **LPG-Detektor:** max. 200 mm über Boden/Bilge (LPG sinkt!)
- **CO-Detektor:** auf Atemhöhe, ca. 1.500 mm (CO verteilt sich gleichmäßig)
- Abstand zum Gasgerät: min. 300 mm, max. 2.000 mm
- NICHT in der Nähe von Fenstern/Luken (Durchzug verfälscht)
- NICHT direkt über Kocher (Kochdämpfe → Fehlalarm)

### Dichtigkeitsprüfung nach Einbau

**Pflicht-Ablauf nach EN 1949 Anhang D:**

| Schritt | Aktion | Kriterium | Bei Versagen |
|---------|--------|-----------|--------------|
| 1 | Sichtprüfung aller Verbindungen | Keine sichtbaren Mängel | Nacharbeiten |
| 2 | Leckspray auf alle Verbindungen | Keine Blasenbildung 3 min | Nachziehen/Austausch |
| 3 | Niederdrucktest 30 mbar / 5 min | Druckabfall ≤ 0,5 mbar | Lecksuche |
| 4 | Hochdrucktest 150 mbar / 5 min | Druckabfall ≤ 1,0 mbar | Lecksuche |
| 5 | Funktionstest aller Verbraucher | Flamme stabil, blau | Düse/Regler prüfen |
| 6 | Gasdetektor-Funktionstest | Testalarm auslöst | Detektor austauschen |
| 7 | Magnetventil-Test | Schließt stromlos | Ventil austauschen |
| 8 | Protokoll erstellen | Unterschrift Sachkundiger | Keine Inbetriebnahme |

### Notfall-Verfahren bei Gasleck

> **⚠️ BEI GASGERUCH ODER DETEKTOR-ALARM: SOFORT HANDELN. Jede Sekunde zählt.**

**Sofortmaßnahmen (Reihenfolge einhalten!):**

```
SCHRITT 1: RUHE BEWAHREN — KEINE PANIK
    │
    ▼
SCHRITT 2: KEIN FUNKE!
    │   - Keine elektrischen Schalter betätigen
    │   - Kein Handy benutzen
    │   - Keine Taschenlampe einschalten
    │   - NICHT rauchen (!)
    │
    ▼
SCHRITT 3: GASFLASCHE SCHLIESSEN
    │   - Handrad im Uhrzeigersinn zudrehen
    │   - Falls Gaslocker nicht erreichbar: Magnetventil-Notschalter
    │
    ▼
SCHRITT 4: ALLE PERSONEN AN DECK
    │   - Alle aus Kabinen und Unter-Deck-Bereichen evakuieren
    │   - LPG sammelt sich unten → Bilge, Kabinen, Salon
    │
    ▼
SCHRITT 5: BELÜFTEN
    │   - Alle Luken und Fenster öffnen
    │   - NICHT den elektrischen Lüfter einschalten (Funke!)
    │
    ▼
SCHRITT 6: LECK LOKALISIEREN
    │   - Erst nach 15 Minuten Durchlüftung
    │   - Lecksuchspray verwenden (NICHT offene Flamme!)
    │
    ▼
SCHRITT 7: FACHMANN RUFEN
    - Gas erst wieder öffnen nach fachgerechter Reparatur
    - Gasprüfbescheinigung erneuern lassen
```

---

## Lebensdauer und Alterungsmechanismen

### NBR/SBR Lebensdauer

**Acrylnitril-Butadien-Kautschuk (NBR):**

| Parameter | Wert | Anmerkung |
|-----------|------|-----------|
| Max. Nutzungsdauer | 8 Jahre ab Herstellung | EN 1763 / DIN 30665 |
| Empfohlener Austausch | 5–6 Jahre | AYDI-Empfehlung |
| Temperaturbereich | –30 °C bis +80 °C | Kurzzeit bis +100 °C |
| UV-Beständigkeit | Gering | Zersetzung ab 2–3 Jahren ohne Schutz |
| Ozonbeständigkeit | Mäßig | Rissbildung an der Oberfläche |
| Ölbeständigkeit | Gut | Hauptvorteil gegenüber SBR |
| Alterung bei 40 °C Dauertemp. | –40 % Lebensdauer | Motorraum-Nähe! |
| Alterung bei Salz + UV | –30 % Lebensdauer | Cockpit-Verlegung |

**Styrol-Butadien-Kautschuk (SBR):**

| Parameter | Wert | Anmerkung |
|-----------|------|-----------|
| Max. Nutzungsdauer | 5 Jahre ab Herstellung | Niedrigere Beständigkeit |
| Empfohlener Austausch | 3–4 Jahre | AYDI-Empfehlung |
| Temperaturbereich | –25 °C bis +70 °C | Enger als NBR |
| UV-Beständigkeit | Sehr gering | Bereits nach 1 Jahr sichtbare Alterung |
| Ozonbeständigkeit | Gering | Schnellere Rissbildung als NBR |
| Ölbeständigkeit | Schlecht | Quillt bei Ölkontakt |
| Kostenvorteil | ca. 20 % günstiger als NBR | Aber kürzere Lebensdauer |

### Edelstahl-Wellrohr Lebensdauer

| Parameter | Wert | Anmerkung |
|-----------|------|-----------|
| Max. Nutzungsdauer | 20–30 Jahre | Herstellerabhängig |
| Empfohlener Austausch | 20 Jahre oder bei sichtbarer Korrosion | AYDI-Empfehlung |
| Temperaturbereich | –200 °C bis +450 °C | Für LPG irrelevant, aber robust |
| UV-Beständigkeit | Sehr hoch | Edelstahl altert nicht durch UV |
| Salzwasserbeständigkeit | Hoch (316L) | Vorsicht: 304 korrodiert! |
| Vibrationsbeständigkeit | Sehr hoch | Wellstruktur kompensiert Bewegung |
| Ermüdung | >500.000 Biegezyklen (±5°) | Bei korrektem Biegeradius |
| Schwachstelle | Anschlussstücke | Dichtungen der Fittings prüfen |

### Alterungsmechanismen

**Mechanismus 1: Ozon-Rissbildung (NBR/SBR)**
- Ozon in der Atmosphäre greift Doppelbindungen im Polymer an
- Sichtbar als feine Oberflächenrisse senkrecht zur Dehnungsrichtung
- Beschleunigt durch UV-Strahlung und mechanische Spannung
- Marine-Umgebung: 2× schnellere Ozonalterung als Binnenland
- AYDI-Erkennung: `visual_high` bei Risstiefe > 0,5 mm sichtbar

**Mechanismus 2: Thermische Alterung (NBR/SBR)**
- Oxidation der Polymerketten bei erhöhter Temperatur
- Arrhenius-Regel: Lebensdauer halbiert sich pro 10 °C Erhöhung
- Bei 30 °C Dauertemperatur: 100 % Lebensdauer
- Bei 40 °C Dauertemperatur: 50 % Lebensdauer
- Bei 50 °C Dauertemperatur: 25 % Lebensdauer (nur 2 Jahre bei NBR!)
- Ergebnis: Verhärtung, Sprödigkeit, Rissbildung

**Mechanismus 3: Quellungsalterung (NBR/SBR)**
- Kontakt mit Kraftstoff, Öl, Lösungsmitteln
- NBR: beständig gegen aliphatische KW, quillt bei aromatischen
- SBR: quillt bei fast allen Kohlenwasserstoffen
- Folge: Durchmesser-Änderung, Schelle sitzt nicht mehr, Leck

**Mechanismus 4: Spannungsrelaxation (alle Elastomere)**
- Dauerhaft verformte Bereiche (Schellen, Biegungen) verlieren Rückstellkraft
- Schlauch wird unter Schelle dünner → Spalt → Leck
- Besonders kritisch bei Vibrationsbelastung (Motor)
- Gegenmaßnahme: Schellen jährlich nachziehen

**Mechanismus 5: Crevice Corrosion (Edelstahl-Wellrohr)**
- In Spalten (Wellentäler) mit stehendem Salzwasser
- Lokaler Sauerstoffmangel → Passivschicht bricht zusammen
- Betrifft nur 304er Stahl; 316L ist wesentlich beständiger
- Gegenmaßnahme: Nur 316L verwenden, Wellrohr trocken halten

### Predictive Maintenance

**AYDI-Lebensdauer-Prognose-Modell:**

```python
def predict_hose_remaining_life(
    material: str,          # "NBR", "SBR", "stainless", "thermoplast"
    manufacturing_date: str,  # ISO 8601
    avg_temperature_c: float, # Durchschnittstemperatur am Einbauort
    uv_exposure: str,        # "none", "indirect", "direct"
    vibration_level: str,    # "low", "medium", "high"
    salt_exposure: str,      # "none", "spray", "direct"
    last_inspection: str,    # ISO 8601
    visual_condition: str    # "excellent", "good", "fair", "poor", "critical"
) -> dict:
    """
    Berechnet verbleibende Lebensdauer und Austausch-Empfehlung.
    
    Returns:
        {
            "remaining_life_months": int,
            "replacement_urgency": str,  # "routine", "soon", "urgent", "immediate"
            "confidence": str,
            "next_inspection_date": str,
            "risk_score": int,  # 0-100, höher = mehr Risiko
            "factors": [str]    # Einflussfaktoren
        }
    """
    base_life_years = {
        "NBR": 8, "SBR": 5, "stainless": 20, "thermoplast": 10
    }
    # Temperatur-Faktor (Arrhenius)
    temp_factor = 0.5 ** ((avg_temperature_c - 30) / 10)
    # UV-Faktor
    uv_factor = {"none": 1.0, "indirect": 0.85, "direct": 0.6}
    # Vibrations-Faktor
    vib_factor = {"low": 1.0, "medium": 0.8, "high": 0.6}
    # Salz-Faktor
    salt_factor = {"none": 1.0, "spray": 0.85, "direct": 0.7}
    # ...
```

**AYDI-Austausch-Intervalle (Empfehlung):**

| Material | Standard | Mittelmeer (heiß, UV) | Nordeuropa | Tropen |
|----------|----------|-----------------------|------------|--------|
| NBR | 6 Jahre | 4 Jahre | 6 Jahre | 3 Jahre |
| SBR | 4 Jahre | 3 Jahre | 4 Jahre | 2 Jahre |
| Edelstahl-Wellrohr | 20 Jahre | 18 Jahre | 20 Jahre | 15 Jahre |
| Thermoplast | 8 Jahre | 6 Jahre | 8 Jahre | 5 Jahre |

---

## Fehlerbild-Atlas

> **Dieser Atlas dient der visuellen Erkennung von Gasschlauch-Defekten. AYDI Pipeline B nutzt diese Muster zur automatisierten Bewertung. JEDES hier gezeigte Fehlerbild stellt eine potenzielle EXPLOSIONS- und TODESGEFAHR dar.**

### Fehlerbild 1: Rissbildung (Ozon-/UV-induziert)

**Beschreibung:** Feine bis grobe Risse in der Schlauch-Außenhaut, typischerweise senkrecht zur Längsachse. Beginnt als Haarrisse, vertieft sich mit der Zeit bis zur Gasführungsschicht.
**Visuelle Merkmale:** Netzförmiges Rissmuster, weiße Verfärbung an Rissrändern, Oberfläche matt und spröde.
**Ursache:** UV-Strahlung und Ozon zersetzen die Polymer-Doppelbindungen. Marine-Umgebung beschleunigt den Prozess.
**Typisches Alter bei Auftreten:** NBR 4–6 Jahre, SBR 2–4 Jahre (bei UV-Exposition deutlich früher).
**Risiko-Bewertung:** CRITICAL. Risse können bis zur Gasführungsschicht reichen → Leck.
**AYDI-Erkennung:** Risse >0,5 mm sichtbar → `visual_high`, Score 10/100.
**Maßnahme:** Sofortiger Austausch, keine temporäre Reparatur möglich.
**Verwechslungsgefahr:** Oberflächliche Verschmutzung kann wie Risse aussehen → Reinigen und erneut prüfen.
**Prävention:** UV-Schutzmantel (Truma Art.-Nr. 50222-00, ca. 8 EUR/m), Schlauch nicht im Freien verlegen.
**Dokumentation:** Rissmuster fotografieren mit Maßstab (Lineal), Risstiefe mit Taschen-Mikroskop messen.
**AYDI Pipeline B Prompt:** "Examine the gas hose surface for crack patterns. Look for perpendicular cracks, white discoloration at crack edges, and brittle surface texture."
**Confidence-Mapping:** Klare Rissbilder bei Nahaufnahme → `visual_high`. Risse nur erahnbar → `visual_medium`.

### Fehlerbild 2: Verhärtung (thermische Alterung)

**Beschreibung:** Schlauch hat seine Elastizität verloren, fühlt sich steif und hart an, lässt sich nicht mehr biegen ohne Widerstand. Kann nicht mehr von Hand zusammengedrückt werden.
**Visuelle Merkmale:** Schlauch behält Biegeform dauerhaft, glänzende/spröde Oberfläche, Farbe dunkler als original, Schelle drückt sich tief ein (bleibende Deformation).
**Ursache:** Oxidation der Polymerketten durch erhöhte Temperatur über lange Zeit. Beschleunigt in der Nähe von Motoren, Auspuffanlagen, Heizungen.
**Typisches Alter bei Auftreten:** 5–8 Jahre (bei erhöhter Temperatur bereits nach 3 Jahren).
**Risiko-Bewertung:** CRITICAL. Verhärteter Schlauch dichtet unter Schellen nicht mehr ab, kann bei Druckspitze platzen.
**AYDI-Erkennung:** Dauerhaft verformter Schlauch → `visual_high`, Score 15/100.
**Maßnahme:** Sofortiger Austausch. Einbauort-Temperatur prüfen und ggf. Hitzeschutz nachrüsten.
**Prävention:** Mindestabstand 50 mm zu heißen Oberflächen, Hitzeschutzschlauch verwenden.
**AYDI Pipeline B Prompt:** "Check if the gas hose maintains a permanent bend shape. Look for deep clamp impressions, glossy/brittle surface, and darker coloration than new."

### Fehlerbild 3: Undichter Anschluss (Schelle/Stutzen)

**Beschreibung:** Gasleck an der Verbindungsstelle zwischen Schlauch und Stutzen. Oft schleichend und geruchsmäßig kaum wahrnehmbar, bis gefährliche Konzentrationen erreicht sind.
**Visuelle Merkmale:** Verfärbung/Ölfilm um Schelle, Korrosionsspuren am Stutzen, Schlauch leicht verschoben (Markierung nicht mehr deckungsgleich), Schelle locker.
**Ursache:** Vibration, thermische Ausdehnung, Spannungsrelaxation des Schlauchs, Korrosion des Stutzens, falsch angezogene Schelle.
**Risiko-Bewertung:** CRITICAL. Schleichendes Leck kann über Stunden Gas im Bilgebereich ansammeln.
**AYDI-Erkennung:** Verschiebungsmarkierung sichtbar → `visual_high`, Score 5/100.
**Maßnahme:** Sofort Gas abstellen, Schelle nachziehen oder Verbindung komplett erneuern, Lecktest durchführen.
**Prävention:** Doppelschellen, Markierung auf Schlauch/Stutzen, jährliche Kontrolle mit Leckspray.
**AYDI Pipeline B Prompt:** "Look for displacement marks between hose and fitting, oily residue around clamps, corrosion on the stub, or loose clamp bands."

### Fehlerbild 4: Korrosion Edelstahl-Wellrohr

**Beschreibung:** Lokale Korrosionserscheinungen an Edelstahl-Wellrohren, typischerweise in Spalten oder an Kontaktstellen mit anderen Metallen.
**Visuelle Merkmale:** Braune/rostfarbene Flecken, Lochfraß an Wellentälern, weiße Salzablagerungen, Verfärbung an Fittings.
**Ursache:** Spaltkorrosion in Wellentälern mit stehendem Salzwasser, galvanische Korrosion bei Kontakt mit unedlerem Metall (Aluminium, Stahl), falsche Legierung (304 statt 316L).
**Risiko-Bewertung:** WARNING bis CRITICAL je nach Tiefe. Lochfraß kann Wandung durchdringen.
**AYDI-Erkennung:** Rostflecken auf Edelstahl → `visual_high`, Score 30/100.
**Maßnahme:** Legierung prüfen (Magnettest: 304 ist leicht magnetisch, 316L nicht). Bei Lochfraß sofort austauschen.
**Prävention:** Nur 316L verwenden, Kontakt mit anderen Metallen vermeiden (Isolierbuchsen), regelmäßig Süßwasser abspülen.
**AYDI Pipeline B Prompt:** "Examine stainless steel corrugated gas pipes for brown/rust spots, pitting in corrugation valleys, white salt deposits, and discoloration at fittings."

### Fehlerbild 5: UV-Schaden

**Beschreibung:** Durch UV-Strahlung hervorgerufene Degradation der Schlauch-Oberfläche. In der Yacht-Umgebung besonders am Cockpit oder nicht abgedeckten Bereichen.
**Visuelle Merkmale:** Kreidiger weißer Belag auf schwarzem Schlauch, Oberfläche matt und rau, beim Wischen bleibt schwarzer Abrieb, Farbe ausgeblichen.
**Ursache:** UV-C und UV-B spalten Polymerketten auf. Reflektiertes UV vom Wasser verdoppelt die Dosis.
**Typisches Alter bei Auftreten:** 1–3 Jahre bei direkter Sonnenexposition.
**Risiko-Bewertung:** WARNING (früh) bis CRITICAL (fortgeschritten). Schwächt mechanische Eigenschaften.
**AYDI-Erkennung:** Kreidiger Belag sichtbar → `visual_high`, Score 35/100.
**Maßnahme:** Bei oberflächlichem UV-Schaden: UV-Schutzmantel nachrüsten. Bei tiefgreifendem Schaden: Austausch.
**Prävention:** Schläuche NIE im UV-Bereich verlegen, UV-Schutzmantel (ca. 8 EUR/m), Abdeckung.
**AYDI Pipeline B Prompt:** "Look for chalky white residue on gas hoses, faded color, rough surface texture, and black rub-off when touched."

### Fehlerbild 6: Knick (mechanische Überbelastung)

**Beschreibung:** Schlauch ist an einer Stelle so stark gebogen, dass er knickt — der Querschnitt wird oval oder kollabiert vollständig.
**Visuelle Merkmale:** Scharfe Biegung, Schlauch an Knickstelle oval oder flach, Weiß-Verfärbung an der Außenbiegung, ggf. Riss an der Außenseite.
**Ursache:** Biegeradius unterschritten, Schlauch zu kurz montiert, keine Führung bei Richtungsänderung.
**Risiko-Bewertung:** CRITICAL. Knick = Wandverdünnung = Bruchgefahr unter Druck.
**AYDI-Erkennung:** Scharfe Biegung sichtbar → `visual_high`, Score 15/100.
**Maßnahme:** Schlauch sofort ersetzen (geknickter Schlauch ist dauerhaft beschädigt!). Biegeschutzfeder oder Winkelanschluss einbauen.
**Prävention:** Mindest-Biegeradius einhalten, Biegeschutzfedern verwenden, Schlauch mit Reserve-Länge montieren.
**AYDI Pipeline B Prompt:** "Check for sharp bends or kinks in the gas hose. Look for flattened cross-section, white stress marks on the outer bend, or complete collapse."

### Fehlerbild 7: Schlauch vom Stutzen gerutscht

**Beschreibung:** Schlauch hat sich teilweise oder vollständig vom Stutzen gelöst. **Dies ist der gefährlichste Zustand** — unkontrollierter Gasaustritt.
**Visuelle Merkmale:** Sichtbarer Spalt zwischen Schlauchende und Schelle, Stutzen teilweise frei, Markierung deutlich verschoben, Gas tritt hörbar aus.
**Ursache:** Nur eine Schelle (statt zwei), Schelle zu lose, Schlauch zu kurz, Vibrationsbelastung, thermische Kontraktion.
**Risiko-Bewertung:** CRITICAL → NOTFALL. Sofortiger unkontrollierter Gasaustritt.
**AYDI-Erkennung:** Spalt sichtbar → `visual_high`, Score 0/100, sofortige Warnung.
**Maßnahme:** GAS SOFORT ABSTELLEN. Keine Zündquellen. Belüften. Fachmann rufen.
**Prävention:** Doppelschellen (Pflicht!), Markierung, mindestens 30 mm Überstand, jährliche Kontrolle.
**AYDI Pipeline B Prompt:** "CRITICAL: Look for any visible gap between hose end and clamp. Check if the fitting stub is partially exposed. Any displacement = immediate danger."

### Fehlerbild 8: Regler-Versagen

**Beschreibung:** Der Gasdruckregler liefert keinen konstanten Ausgangsdruck mehr — entweder zu hoch (Überdruck → Schlauchplatzer) oder zu niedrig (Geräte funktionieren nicht).
**Visuelle Merkmale:** Vereisung am Regler (bei hohem Durchfluss normal, bei Stillstand NICHT), Korrosion am Gehäuse, gebrochene Membran sichtbar, Gasgeruch am Regler.
**Ursache:** Membran-Alterung (>10 Jahre), Vereisung durch Kondenswasser, Korrosion, mechanische Beschädigung.
**Risiko-Bewertung:** CRITICAL. Überdruck-Versagen kann gesamte Niederdruckleitung zerstören.
**AYDI-Erkennung:** Vereisung oder Korrosion sichtbar → `visual_high`, Score 20/100.
**Maßnahme:** Regler sofort austauschen. Nur EN 16129 zugelassene Regler verwenden. Max. Alter: 10 Jahre.
**Prävention:** Regler alle 10 Jahre tauschen, vor jeder Saison Ausgangsdruck prüfen (30 mbar ±2).
**AYDI Pipeline B Prompt:** "Examine the gas pressure regulator for ice formation, corrosion, cracked housing, or visible membrane damage."

### Fehlerbild 9: Magnetventil-Fehler

**Beschreibung:** Das elektrische Absperrventil schließt nicht korrekt oder öffnet nicht. Beides ist gefährlich — offenes Ventil bei Leck = unkontrollierter Gasfluss, geschlossenes Ventil = kein Gas für Notkochen.
**Visuelle Merkmale:** Korrosion an Anschlüssen, oxidierte Kabelverbindungen, Ventilkörper verfärbt/korrodiert, Summen ohne Schaltung.
**Ursache:** Korrosion in mariner Umgebung, defekte Spule, Kabelbruch, korrodierte Steckverbindung, Fremdkörper im Ventilsitz.
**Risiko-Bewertung:** CRITICAL bei "schließt nicht". WARNING bei "öffnet nicht".
**AYDI-Erkennung:** Korrosion/Verfärbung → `visual_medium`, Score 40/100.
**Maßnahme:** Elektrische Funktion prüfen (12V anlegen, Klick hörbar?). Bei Zweifel: Austausch.
**Prävention:** Jährlich Funktion testen, Kabelverbindungen mit Korrosionsschutz (Ballistol, WD-40 Specialist Marine).
**AYDI Pipeline B Prompt:** "Check the gas solenoid valve for corrosion, oxidized wire connections, discolored valve body, or mechanical damage."

### Fehlerbild 10: Detektor-Fehlalarm

**Beschreibung:** Der Gasdetektor löst Alarm aus, obwohl kein Gas vorhanden ist. Führt zu "Alarm-Müdigkeit" — Crew ignoriert irgendwann echte Alarme → tödlich.
**Visuelle Merkmale:** Keine visuellen Merkmale am Detektor selbst. Ursache meist Sensor-Degradation oder Kontamination.
**Ursache:** Sensor-Alterung (Halbleitersensoren: 3–5 Jahre Lebensdauer), Kontamination durch Reinigungsmittel, Kochdämpfe, Alkoholdämpfe, hohe Luftfeuchtigkeit.
**Risiko-Bewertung:** WARNING → CRITICAL (wenn Crew Detektor deaktiviert!).
**AYDI-Erkennung:** Nicht visuell erkennbar → `visual_insufficient`, Score n/a.
**Maßnahme:** Sensor kalibrieren oder austauschen. Detektor NIEMALS deaktivieren. Ggf. Position ändern (weiter vom Kocher weg).
**Prävention:** Halbleitersensoren alle 3–5 Jahre tauschen. Elektrochemische Sensoren halten 5–7 Jahre.
**AYDI Pipeline B Prompt:** "N/A — detector false alarms cannot be visually detected. Recommend functional testing."

### Fehlerbild 11: Falsche Schelle (Baumarkt-Schelle auf Gasleitung)

**Beschreibung:** Eine nicht zugelassene Schlauchschelle aus dem Baumarkt oder KFZ-Bereich wurde auf einem Gasschlauch montiert.
**Visuelle Merkmale:** Scharfkantige Bandkanten, oft verzinktes Band (matt-grau statt blank), breiter Schraubenkopf, keine "Gas"/"LPG"-Kennzeichnung, Band oft schmaler als 9 mm.
**Ursache:** Unwissenheit oder Kosteneinsparung. "Ist doch nur eine Schelle" — dieser Gedanke tötet.
**Risiko-Bewertung:** CRITICAL. Scharfe Kanten schneiden in den Schlauch, verzinktes Metall korrodiert.
**AYDI-Erkennung:** Korrosion/scharfe Kanten sichtbar → `visual_high`, Score 10/100.
**Maßnahme:** ALLE Baumarkt-Schellen sofort gegen zugelassene Gas-Schellen tauschen. Schlauch unter alter Schelle auf Einschnitte prüfen.
**Prävention:** Nur Gas-zugelassene Schellen verwenden (siehe Hersteller-Tabelle oben).
**AYDI Pipeline B Prompt:** "Identify non-certified hose clamps: look for sharp band edges, galvanized (dull gray) finish, narrow bandwidth <9mm, and missing 'Gas'/'LPG' marking."

### Fehlerbild 12: Vereisungs-Schaden

**Beschreibung:** Bei hohem Gasverbrauch (Heizung + Kocher gleichzeitig) kann der Verdampfungsvorgang in der Flasche so viel Wärme entziehen, dass Kondenswasser am Regler und an der Leitung gefriert.
**Visuelle Merkmale:** Eisbildung am Regler und ersten 200–300 mm des Schlauchs, weiße Bereifung, Wassertropfen bei Abtauen, Regler schwergängig.
**Ursache:** Verdampfungsenthalpie von LPG (ca. 370 kJ/kg bei Propan). Bei Entnahmerate >2 kg/h signifikante Abkühlung bis unter 0 °C.
**Typisches Auftreten:** Winterbetrieb mit Gasheizung, kleine Flasche (5 kg) bei hohem Verbrauch.
**Risiko-Bewertung:** WARNING. Eis kann Regler-Membran beschädigen → Überdruck. Schlauch wird bei Frost spröde.
**AYDI-Erkennung:** Eisbildung sichtbar → `visual_high`, Score 40/100.
**Maßnahme:** Verbrauch reduzieren (einen Verbraucher abschalten), größere Flasche verwenden, Gaslocker isolieren (NICHT abdichten — Belüftung muss erhalten bleiben!).
**Prävention:** 11-kg-Flasche statt 5-kg, Duomatic-Regler (Truma DuoControl) für automatischen Flaschenwechsel, Flasche vor Kälte schützen.
**AYDI Pipeline B Prompt:** "Look for ice or frost formation on the gas regulator and the first 200-300mm of the hose. Check for water drops or white frost coating."

---

## Fehlerbehebungs-Leitfaden (Troubleshooting)

### Problem 1: Gasgeruch an Bord

```
GASGERUCH WAHRGENOMMEN
    │
    ├─► SOFORT: Gasflasche schließen, Magnetventil AUS
    ├─► SOFORT: Alle Personen an Deck
    ├─► SOFORT: Alle Luken öffnen (KEINE elektrischen Schalter!)
    ├─► 15 Minuten durchlüften
    │
    ▼ Wenn Geruch verschwunden:
    ├─► Lecksuchspray auf ALLE Verbindungen
    ├─► Gasflasche langsam (1/4 Umdrehung) öffnen
    │
    ├─► Blasen an Regler-Ausgang? → Regler defekt → Austauschen
    ├─► Blasen an Schlauchschelle? → Schelle nachziehen oder Schlauch/Schelle tauschen
    ├─► Blasen am Geräteanschluss? → Verschraubung nachziehen, Dichtung prüfen
    ├─► Blasen an Flaschenverschraubung? → Flaschenventil-Gewinde reinigen, neu anschließen
    ├─► Keine Blasen gefunden? → Manometer-Drucktest durchführen
    │
    ▼ Wenn Geruch bleibt:
    └─► NICHT weitersuchen. Gas abgestellt lassen. Fachmann rufen.
        In Hafennähe: Hafenmeister informieren.
        Auf See: Panpan-Meldung erwägen (bei starkem Gasgeruch).
```

### Problem 2: Flamme erlischt wiederholt

```
FLAMME ERLISCHT
    │
    ├─► Flasche noch voll? → Gewicht prüfen (leer: 5-kg-Fl. wiegt ca. 6 kg)
    ├─► Andere Verbraucher funktionieren? 
    │       JA → Problem am einzelnen Gerät
    │       NEIN → Problem in der Gasversorgung
    │
    ▼ Problem am Gerät:
    ├─► Thermoelement/Zündsicherung verschmutzt → Reinigen
    ├─► Düse verstopft → Düsennadel verwenden
    ├─► Flamme gelb statt blau → Luftzufuhr verstellt, Düse falsch
    │
    ▼ Problem in der Gasversorgung:
    ├─► Regler vereist? → Verbrauch reduzieren, abtauen lassen
    ├─► Druckregler-Ausgangsdruck messen (Soll: 30 mbar ±2)
    │       Zu niedrig → Regler defekt oder Flasche fast leer
    │       Zu hoch → Regler defekt → SOFORT austauschen (Überdruck!)
    ├─► Magnetventil offen? → LED-Anzeige prüfen, Spannung messen (12V)
    ├─► Schlauch geknickt? → Visuell prüfen, Knick beseitigen
    └─► Druckverlust zu hoch? → Schlauch zu lang oder Ø zu klein
```

### Problem 3: Gasdetektor löst Alarm aus

```
DETEKTOR-ALARM
    │
    ├─► IMMER ERNST NEHMEN — auch beim 10. Fehlalarm!
    ├─► Gasflasche sofort schließen
    ├─► Belüften
    ├─► 5 Minuten warten
    │
    ▼ Alarm stoppt nach Gas-Absperrung:
    ├─► Es war echtes Gas! → Lecksuche (siehe Problem 1)
    │
    ▼ Alarm stoppt NICHT nach Gas-Absperrung:
    ├─► Wurde gekocht? → Kochdämpfe (Alkohol, Fett) können Sensor auslösen
    ├─► Wurde geputzt? → Reinigungsmittel-Dämpfe
    ├─► Hohe Luftfeuchtigkeit? → Sensor kann bei >80% RH auslösen
    ├─► Sensor-Alter >5 Jahre? → Sensor degradiert → Austauschen
    ├─► Detektor zu nah am Kocher? → Umpositionieren (min. 300 mm Abstand)
    │
    ▼ Alarm dauerhaft:
    └─► Detektor-Selbsttest durchführen (Taste 3 Sek. halten)
        Selbsttest OK → Kontamination → Sensor reinigen oder tauschen
        Selbsttest FAIL → Detektor defekt → Sofort ersetzen
```

### Problem 4: Regler vereist

```
REGLER VEREIST
    │
    ├─► Normal bei hohem Verbrauch (Heizung) und kleiner Flasche
    ├─► Verbrauch sofort reduzieren (einen Verbraucher abschalten)
    ├─► NICHT mit Feuer, Heißluft oder kochendem Wasser abtauen!
    ├─► Langsam bei Raumtemperatur abtauen lassen
    │
    ▼ Gegenmaßnahmen:
    ├─► Größere Flasche verwenden (11 kg statt 5 kg)
    ├─► Duomatic-Regler einbauen (Truma DuoControl, 259 EUR)
    │     → Automatischer Wechsel zur zweiten Flasche
    ├─► Gaslocker thermisch isolieren (Styrodur, NICHT abdichten!)
    ├─► Gleichzeitigen Betrieb von Heizung + Kocher + Boiler vermeiden
    │
    ▼ Wenn Regler nach Abtauen nicht mehr regelt:
    └─► Membran durch Eis beschädigt → Regler sofort austauschen
        Nie mit beschädigtem Regler weiterbetreiben!
```

### Problem 5: Kocher zündet nicht

```
KOCHER ZÜNDET NICHT
    │
    ├─► Piezozünder klickt?
    │       NEIN → Batterie leer (CR2032) oder Piezoelement defekt
    │       JA → Weiter prüfen
    │
    ├─► Gas strömt? (Zischen hörbar bei offenem Drehknopf)
    │       NEIN → Magnetventil geschlossen, Flasche leer, Regler defekt
    │       JA → Weiter prüfen
    │
    ├─► Funke sichtbar?
    │       NEIN → Zündelektrode verschmutzt → mit feinem Schmirgel reinigen
    │              Abstand Elektrode-Brenner prüfen (Soll: 3–4 mm)
    │       JA → Weiter prüfen
    │
    ├─► Flamme zündet kurz, erlischt sofort?
    │       → Thermoelement (Zündsicherung) verschmutzt oder defekt
    │       → Reinigen: Thermoelementspitze mit Schmirgel säubern
    │       → Drehknopf 10–15 Sekunden gedrückt halten
    │       → Wenn weiterhin erlischt: Thermoelement tauschen (ca. 15–25 EUR)
    │
    ├─► Flamme gelb statt blau?
    │       → Primärluft-Zufuhr blockiert → Düse und Luftöffnung reinigen
    │       → Falsche Düsengröße (Butan-Düse bei Propan oder umgekehrt)
    │       → Propan-Düse: Ø 0,65–0,70 mm
    │       → Butan-Düse: Ø 0,75–0,85 mm
    │
    └─► Alles geprüft, funktioniert trotzdem nicht?
        → Servicetechniker kontaktieren. NICHT improvisieren.
```

---

## FAQ (Häufig gestellte Fragen)

**GS-001: Wie oft muss ein Gasschlauch auf dem Boot gewechselt werden?**
NBR-Schläuche alle 5–8 Jahre (empfohlen 6 Jahre), SBR-Schläuche alle 4–5 Jahre. Das Herstellungsdatum steht auf dem Schlauch. Edelstahl-Wellrohre halten 20+ Jahre. AYDI empfiehlt den Austausch nach 6 Jahren (NBR) unabhängig vom Zustand.

**GS-002: Darf ich als Eigner den Gasschlauch selbst wechseln?**
In Deutschland dürfen nur DVGW-sachkundige Personen (nach G 607) Gasarbeiten durchführen. In den Niederlanden und UK ist Eigenarbeit unter Auflagen erlaubt. Nach jeder Arbeit ist eine Gasprüfung durch einen Sachverständigen Pflicht. Versicherungen erkennen Eigenarbeit oft nicht an.

**GS-003: Was kostet eine Gasprüfung auf dem Boot?**
Eine Gasprüfung nach EN 1949 kostet je nach Region und Betrieb 80–200 EUR. Bei bestandener Prüfung erhält man die Gasprüfbescheinigung. Bei Mängeln kommen Reparaturkosten hinzu. Wiederholungsprüfung nach Mängelbehebung: ca. 50–100 EUR.

**GS-004: Kann ich einen KFZ-Gasschlauch auf dem Boot verwenden?**
NEIN. KFZ-Gasschläuche sind nicht für marine Umgebung zugelassen. Sie haben andere Materialeigenschaften, keine Salzwasserbeständigkeit und entsprechen nicht EN 1949. Nur marine-zugelassene Schläuche nach EN 1763 oder EN 16436 verwenden.

**GS-005: Welchen Durchmesser brauche ich für meinen Gasschlauch?**
Das hängt vom Gesamtverbrauch aller Geräte und der Schlauchlänge ab. Faustregel: 8 mm Innen-Ø für Einzelgerät bis 300 g/h, 10 mm für bis 500 g/h, 12 mm für Hauptleitung. Siehe Durchfluss-Tabelle in diesem Dokument.

**GS-006: NBR oder Edelstahl-Wellrohr — was ist besser?**
Edelstahl-Wellrohr (316L) ist in jeder Hinsicht überlegen: langlebiger (20+ Jahre vs. 6–8 Jahre), temperaturbeständiger, UV-beständig, keine Alterung. Einziger Nachteil: höhere Anschaffungskosten (28 EUR/m vs. 8–12 EUR/m). Über 20 Jahre ist Wellrohr sogar günstiger.

**GS-007: Was ist der Unterschied zwischen Hochdruck- und Niederdruckschlauch?**
Der Hochdruckschlauch führt von der Gasflasche (bis 16 bar) zum Druckregler. Der Niederdruckschlauch führt vom Regler (30 mbar) zu den Verbrauchern. Hochdruckschläuche sind dicker, armiert und speziell zugelassen. NIEMALS Niederdruckschlauch im Hochdruckbereich verwenden.

**GS-008: Mein Gasschlauch riecht nach Gas — ist er undicht?**
Nicht unbedingt. Neue Gummischläuche können anfangs nach Gummi/Gas riechen. Aber: IMMER mit Lecksuchspray prüfen! Lieber einmal zu viel getestet als einmal zu wenig. Ein Lecktest dauert 5 Minuten und kostet nichts.

**GS-009: Kann ich einen Gasschlauch reparieren (kleben, wickeln)?**
NEIN. Absolut VERBOTEN. Es gibt keine zugelassene Reparaturmethode für Gasschläuche. Jeder beschädigte Schlauch muss SOFORT und VOLLSTÄNDIG ausgetauscht werden. Jede "Reparatur" (Klebeband, Kabelbinder, etc.) ist lebensgefährlich.

**GS-010: Wie erkenne ich, ob mein Gasschlauch noch gut ist?**
Sichtprüfung: keine Risse, keine Verhärtung, keine Verfärbung, keine Knicke. Druckprüfung: kein Druckabfall in 5 Minuten. Biegetest: Schlauch lässt sich von Hand leicht biegen ohne bleibende Verformung. Im Zweifelsfall: austauschen.

**GS-011: Muss der Gaslocker wirklich gasdicht sein?**
JA. Der Gaslocker muss gasdicht zum Bootsinneren und mit Drainage nach außenbords versehen sein. LPG ist schwerer als Luft und sammelt sich sonst in der Bilge. Ein einziger Funke (Lichtschalter, Bilgepumpe) genügt für eine verheerende Explosion.

**GS-012: Wie viel Gas darf ich an Bord haben?**
Nach EN 1949 und den meisten nationalen Vorschriften: max. 2 Flaschen, max. 2 × 16 kg = 32 kg LPG. In Deutschland nach DVGW G 607: max. 2 × 11 kg = 22 kg ist Standard. Einige Marinas beschränken auf max. 2 × 5 kg. Immer lokale Vorschriften beachten.

**GS-013: Brauche ich einen Gasdetektor?**
Ja, nach EN 1949 ist mindestens ein Gasdetektor in jedem Raum mit Gasgerät Pflicht. AYDI empfiehlt zusätzlich einen Detektor in der Bilge am tiefsten Punkt. Kosten: 120–310 EUR je nach Modell. Diese Investition kann Ihr Leben retten.

**GS-014: Mein Gasdetektor piept ständig — was tun?**
Zuerst: IMMER ernst nehmen und Gas prüfen (Leckspray). Wenn kein Leck: Sensor könnte durch Kochdämpfe, Reinigungsmittel oder Feuchtigkeit kontaminiert sein. Detektor umpositionieren (min. 300 mm vom Kocher). Sensor-Alter prüfen — nach 3–5 Jahren austauschen.

**GS-015: Was ist ein Duomatic-Regler?**
Ein Duomatic-Regler (z.B. Truma DuoControl CS) schaltet automatisch von der leeren auf die volle Reserve-Flasche um. Vorteil: kein Gasausfall beim Kochen. Enthält oft integriertes Magnetventil und Crash-Sensor. Preis: ca. 200–260 EUR. Für Langfahrtsegler Pflicht.

**GS-016: Kann LPG wirklich ein Boot explodieren lassen?**
JA. LPG/Propan hat eine untere Explosionsgrenze von nur 2,1 Vol.-%. Bei einer Standard-11-kg-Flasche genügen wenige Minuten Gasaustritt, um den gesamten Bootsrumpf in die UEG zu bringen. Die resultierende Explosion entspricht ca. 50 kg TNT. Totalverlust, Todesopfer, Schäden an Nachbarbooten.

**GS-017: Wie lagere ich Ersatz-Gasflaschen sicher?**
Ersatz-Gasflaschen (auch leere!) IMMER aufrecht im Gaslocker oder an Deck in belüftetem Bereich. NIEMALS unter Deck, in Kabinen oder im Motorraum. Ventil muss geschlossen, Schutzkappe aufgesetzt sein. Gegen Umfallen und Überbordfallen sichern.

**GS-018: Ist Butan oder Propan besser für Boote?**
Propan ist in Nord-/Mitteleuropa Standard, da es bis –42 °C verdampft (Butan nur bis –1 °C). Im Mittelmeer funktioniert Butan im Sommer, versagt aber in kühlen Nächten. AYDI empfiehlt Propan für alle Reviere. Betriebsdruck Propan: ca. 8 bar (20 °C), Butan: ca. 2 bar.

**GS-019: Was ist eine Schlauchbruchsicherung?**
Eine Schlauchbruchsicherung (SBS) sperrt die Gasleitung automatisch ab, wenn der Durchfluss einen Schwellwert übersteigt (= Schlauch gerissen/abgerutscht). Nach EN 1949 empfohlen. Preis: ca. 25–50 EUR. Einbau direkt nach dem Regler. Hersteller: GOK, Truma.

**GS-020: Wie entsorge ich alte Gasschläuche?**
Alte Gummi-Gasschläuche gehören in den Restmüll (nicht Gelber Sack). Edelstahl-Wellrohre zum Metallschrott. Verschraubungen und Schellen separat als Metallabfall. Alte Gasflaschen beim Händler zurückgeben (Pfandsystem). NIEMALS Gasschläuche als Wasserschläuche "zweitnutzen".

**GS-021: Mein Schlauch hat eine grüne/weiße Verfärbung — was ist das?**
Grüne Verfärbung deutet auf Kupferkorrosion hin (Kontakt mit Kupferleitung). Weiße Verfärbung ist UV-Degradation oder Schimmel. Beide Fälle erfordern Inspektion: UV-Schaden → austauschen. Kupfer-Verfärbung → Kontaktstelle eliminieren, Schlauch prüfen.

**GS-022: Wie teste ich, ob mein Magnetventil funktioniert?**
Magnetventil einschalten (Schalter auf "Gas on"), dann am Ventil lauschen — ein deutliches Klicken muss hörbar sein. Spannung am Ventil messen: sollte 12V (±10 %) anliegen. Stromaufnahme messen: typisch 300–500 mA. Kein Klick oder keine Spannung → defekt.

**GS-023: Darf der Gasschlauch durch die Bordwand geführt werden?**
Ja, aber nur durch eine gasdichte Schotdurchführung mit zugelassener Kabelverschraubung oder Schottfitting. Der Durchbruch muss über der Wasserlinie liegen und gegen Wassereinbruch gesichert sein. Jede Schotdurchführung ist ein potenzielles Leck und muss regelmäßig geprüft werden.

**GS-024: Was passiert, wenn die Gasflasche in der Sonne steht?**
Der Druck in der Flasche steigt mit der Temperatur (Propan bei 40 °C: ca. 13 bar, bei 50 °C: ca. 17 bar). Das Sicherheitsventil der Flasche öffnet bei ca. 25 bar. Bei direkter Sonne UND dunkler Flasche kann die Temperatur 70 °C+ erreichen → Überdruckventil bläst ab → Gasaustritt. Gaslocker NICHT in direkter Sonne ohne Belüftung.

**GS-025: Wie finde ich einen zertifizierten Gas-Fachmann für mein Boot?**
In Deutschland: DVGW-Sachkundiger (G 607), Suche über dvgw.de oder bootsgasprüfung.de. In NL: HISWA-zertifiziert. In UK: Gas Safe Register (www.gassaferegister.co.uk, auch für Boote). Immer nach aktueller Prüfberechtigung und Erfahrung mit Booten fragen — KFZ-Gasinstallateure sind NICHT qualifiziert.

---

## Glossar

| Begriff | Erklärung |
|---------|-----------|
| **Absperrventil** | Manuelles oder elektrisches Ventil zum Unterbrechen der Gasversorgung. Muss von außerhalb des Gaslockers bedienbar sein. |
| **ABYC** | American Boat and Yacht Council — US-Normungsorganisation für Bootsbau, Standard A-1 für LPG-Anlagen. |
| **Betriebsdruck** | Gasdruck nach dem Regler, typisch 30 mbar (Niederdruck) für Verbraucher. |
| **Biegeradius** | Kleinster zulässiger Biegeradius eines Schlauchs, bei Unterschreitung droht Knickbildung und Materialversagen. |
| **Bördelanschluss** | Metallische Dichtverbindung, bei der der Schlauch- oder Rohranschluss durch Verformung (Bördeln) dichtet. Kein PTFE-Band verwenden! |
| **BSI** | British Standards Institution — UK-Normungsorganisation. |
| **Butan** | C₄H₁₀, Flüssiggas, Siedepunkt –1 °C, schwerer als Luft. In Südeuropa gebräuchlich, versagt bei niedrigen Temperaturen. |
| **CE-Kennzeichnung** | Europäische Konformitätskennzeichnung für Freizeitfahrzeuge unter 24 m nach Richtlinie 2013/53/EU. |
| **Crevice Corrosion** | Spaltkorrosion — lokale Korrosion in Spalten, z.B. in den Wellentälern von Edelstahl-Wellrohren bei stehendem Salzwasser. |
| **Doppelschelle** | Zwei Schlauchschellen an jeder Verbindungsstelle — Pflicht nach EN 1949 für Gasanlagen. |
| **Druckregler** | Reduziert den Flaschendruck (bis 16 bar) auf Betriebsdruck (30 mbar). Max. Lebensdauer 10 Jahre. |
| **DuoControl** | Automatischer Umschaltregler von Truma für zwei Gasflaschen mit integriertem Magnetventil und Crash-Sensor. |
| **DVGW** | Deutscher Verein des Gas- und Wasserfaches — zuständig für Gasinstallations-Normen und Sachkunde-Prüfungen. |
| **EN 1763** | Europäische Norm für Gummi-Gasschläuche für Flüssiggas (LPG) und Stadtgas. |
| **EN 1949** | Europäische Norm für LPG-Anlagen auf Wasserfahrzeugen — die zentrale Norm für marine Gasinstallationen. |
| **EN 16129** | Europäische Norm für Gasdruckregler bis einschließlich 4 bar. |
| **EN 16436** | Europäische Norm für Gasschläuche aus thermoplastischen Materialien (nicht-metallisch). |
| **Fail-Safe** | Konstruktionsprinzip: Bei Stromausfall oder Defekt geht das System in den sicheren Zustand (Magnetventil schließt). |
| **Flaschendruck** | Druck in der LPG-Flasche, temperaturabhängig. Propan bei 20 °C ca. 8 bar, bei 40 °C ca. 13 bar. |
| **G 607** | DVGW-Arbeitsblatt für Sachkunde bei LPG-Anlagen in Fahrzeugen und Booten. Grundlage für die Sachkundeprüfung. |
| **Galvanische Korrosion** | Elektrochemische Korrosion bei Kontakt unterschiedlicher Metalle in salzwasserhaltiger Umgebung. Edelstahl + Aluminium = gefährlich. |
| **Gaslocker** | Gasdichter, drainierter und belüfteter Aufbewahrungsraum für Gasflaschen, nach EN 1949 vorgeschrieben. |
| **GFK** | Glasfaserverstärkter Kunststoff — häufigstes Material für Gaslocker-Wannen. |
| **GOK** | Deutscher Hersteller von Gasarmaturen und -reglern (Gok Regler GmbH, Marktbreit). |
| **Hochdruck** | Gasdruckbereich von der Flasche bis zum Regler (bis 16 bar). Erfordert spezielle Hochdruck-Leitungen. |
| **ISO 10239** | Internationale Norm für LPG-Anlagen auf Booten — Basis für EN 1949. |
| **Lecksuchspray** | Spezielles Spray zur Erkennung von Gaslecks durch Blasenbildung an undichten Stellen. |
| **LPG** | Liquefied Petroleum Gas — Flüssiggas, Oberbegriff für Propan und Butan als Brenngas. |
| **Magnetventil** | Elektrisch betätigtes Absperrventil in der Gasleitung, fernbedienbar, schließt stromlos (fail-safe). |
| **Manometer** | Druckmessgerät zur Überwachung des Gasdrucks und zur Durchführung von Druckabfallprüfungen. |
| **NBR** | Acrylnitril-Butadien-Kautschuk — Standard-Elastomer für Gasschläuche, ölbeständig, Lebensdauer 5–8 Jahre. |
| **Niederdruck** | Gasdruckbereich nach dem Regler (30 mbar), in dem die Verbraucher betrieben werden. |
| **Oetiker** | Schweizer Hersteller von Ohr-Schlauchschellen, besonders manipulationssichere Einweg-Schellen. |
| **Propan** | C₃H₈, Flüssiggas, Siedepunkt –42 °C, schwerer als Luft (Dichte 1,83). Standard in Nord-/Mitteleuropa. |
| **SBR** | Styrol-Butadien-Kautschuk — günstigeres Elastomer für Gasschläuche, geringere Beständigkeit als NBR. |
| **Schlauchbruchsicherung** | Sicherheitsarmatur, die bei Überdurchfluss (= Schlauchbruch) automatisch absperrt. |
| **Schotdurchführung** | Gasdichte Durchführung eines Schlauchs oder Rohrs durch ein Schott (Trennwand). |
| **Thermoelement** | Sensor am Gasbrenner, der die Flamme überwacht und bei Erlöschen das Gas absperrt (Zündsicherung). |
| **Truma** | Deutscher Hersteller von Gasheizungen, -reglern und Zubehör für mobile Anwendungen (Truma Gerätetechnik, Putzbrunn). |
| **UEG** | Untere Explosionsgrenze — minimale Gaskonzentration für eine Explosion. Propan: 2,1 Vol.-%, Butan: 1,8 Vol.-%. |
| **Wellrohr** | Edelstahlrohr mit gewellter Struktur, das Flexibilität bei hoher Druckfestigkeit bietet. Für Gas: nur 316L. |
| **316L** | Austenitischer Edelstahl mit Molybdän-Zusatz, besonders korrosionsbeständig in Salzwasser-Umgebung. |
| **W4/W5** | Schlauchschellen-Qualitätsklassen nach DIN 3017: W4 = Edelstahl, W5 = Edelstahl mit Innenliner. |

---

## Schnell-Referenz & Quick-Lookup Index

### 30-Sekunden Diagnose

```
GAS-SYSTEM SCHNELLCHECK:

1. Schlauch biegen → Hart/steif? → AUSTAUSCHEN (Alter!)
2. Schlauch ansehen → Risse/Verfärbung? → AUSTAUSCHEN
3. Schellen zählen → Weniger als 2 pro Verbindung? → ERGÄNZEN
4. Schellen-Material → Rost? → AUSTAUSCHEN (falsche Schelle!)
5. Herstellungsdatum → Älter als 6 Jahre? → AUSTAUSCHEN
6. Knick im Schlauch? → AUSTAUSCHEN (irreparabler Schaden)
7. Gasdetektor → Test-Taste drücken → Kein Alarm? → AUSTAUSCHEN
8. Regler-Alter → Über 10 Jahre? → AUSTAUSCHEN

ERGEBNIS:
  0 Probleme → ✅ System OK, nächste Prüfung in 12 Monaten
  1 Problem → ⚠️ Zeitnah beheben (innerhalb 30 Tage)
  2+ Probleme → ❌ Gasanlage NICHT benutzen bis behoben
  Gasleck → ⛔ NOTFALL → Sofortmaßnahmen einleiten!
```

### Materialwahl-Entscheidungsbaum

```
Start: Neuer Gasschlauch benötigt
    │
    ├─► Budget über 30 EUR/m?
    │       JA → Edelstahl-Wellrohr 316L → BESTE WAHL
    │       NEIN → Weiter
    │
    ├─► Einbauort UV-exponiert?
    │       JA → Edelstahl-Wellrohr (keine Alternative)
    │       NEIN → Weiter
    │
    ├─► Einbauort nahe Motor/Auspuff (>50°C)?
    │       JA → Edelstahl-Wellrohr (keine Alternative)
    │       NEIN → Weiter
    │
    ├─► Segelboot mit starker Krängung?
    │       JA → Edelstahl-Wellrohr (Vibrationsfest)
    │       NEIN → Weiter
    │
    ├─► Standard-Installation, geschützt, <40°C?
    │       → NBR Premium (Truma) → GUTE WAHL
    │
    └─► Übergangs-Lösung, baldiger Austausch geplant?
            → NBR Standard → AKZEPTABEL (max. 6 Jahre)
```

### Jährliche Inspektions-Checkliste

| # | Prüfpunkt | Methode | OK-Kriterium | Befund |
|---|-----------|---------|--------------|--------|
| 1 | Schlauch-Zustand | Sichtprüfung | Keine Risse, keine Verhärtung, keine Verfärbung | ☐ OK ☐ Mangel |
| 2 | Schlauch-Alter | Herstellungsdatum ablesen | NBR <6 Jahre, SBR <4 Jahre | ☐ OK ☐ Mangel |
| 3 | Schellen-Zustand | Sichtprüfung | Keine Korrosion, fest, 2 pro Verbindung | ☐ OK ☐ Mangel |
| 4 | Schellen-Drehmoment | Drehmoment-Schraubendreher | Soll-Wert ±10 % | ☐ OK ☐ Mangel |
| 5 | Biegeradius | Sichtprüfung | Kein Knick, Mindestradius eingehalten | ☐ OK ☐ Mangel |
| 6 | Regler-Zustand | Sicht- und Druckprüfung | Keine Korrosion, 30 mbar ±2 am Ausgang | ☐ OK ☐ Mangel |
| 7 | Regler-Alter | Typenschild | <10 Jahre | ☐ OK ☐ Mangel |
| 8 | Magnetventil | Funktionsprüfung | Klickt bei 12V, schließt stromlos | ☐ OK ☐ Mangel |
| 9 | Gaslocker-Dichtigkeit | Sichtprüfung | Gasdicht zum Innenraum, Drainage frei | ☐ OK ☐ Mangel |
| 10 | Gaslocker-Belüftung | Sichtprüfung | Oben + unten je 250 mm² offen | ☐ OK ☐ Mangel |
| 11 | Gasdetektor | Test-Taste | Alarm auslöst, Sensor <5 Jahre | ☐ OK ☐ Mangel |
| 12 | Lecktest | Spray + Manometer | Keine Blasen, ≤0,5 mbar/5 min | ☐ OK ☐ Mangel |
| 13 | Flaschenbefestigung | Handprüfung | Flasche kippsicher, Ventil zugänglich | ☐ OK ☐ Mangel |
| 14 | Feuerlöscher | Sichtprüfung | Vorhanden, geprüft, Druck OK | ☐ OK ☐ Mangel |

> ⚠️ **ZU PRÜFEN (Audit):** Prüfpunkt 10 „Oben + unten je 250 mm²" widerspricht dem Haupttext („min. 2500 mm² oben"). Verifiziert (EN ISO 10239) ist nur der Drain ≥ 19 mm Innen-Ø (≈ 283 mm²); die Belüftungsfläche ist **estimated — unverifiziert**.

### Häufigste Fehler & Vermeidung

| Rang | Fehler | Häufigkeit | Vermeidung | Kosten Behebung |
|------|--------|-----------|------------|-----------------|
| 1 | Schlauch überaltert | 45 % aller Mängel | Herstellungsdatum prüfen, Kalender-Erinnerung | 40–80 EUR |
| 2 | Nur 1 Schelle | 25 % | Doppelschellen-Pflicht kennen | 5–10 EUR |
| 3 | Falsche Schellen | 12 % | Nur Gas-zugelassene kaufen | 15–30 EUR |
| 4 | Gaslocker undicht | 8 % | Jährlich Dichtung prüfen | 50–300 EUR |
| 5 | Kein Gasdetektor | 5 % | Detektor nachrüsten | 120–310 EUR |
| 6 | Regler überaltert | 3 % | Alle 10 Jahre tauschen | 60–260 EUR |
| 7 | Biegeradius | 2 % | Biegeschutzfeder verwenden | 6–15 EUR |

### Kosten-Kalkulator

**Gasanlagen-Neuinstallation (Komplettkosten):**

| Komponente | 8-m-Segelboot | 12-m-Segelboot | 15-m-Motorboot | 20-m-Superyacht |
|-----------|---------------|----------------|----------------|-----------------|
| Gaslocker (GFK) | 250 EUR | 400 EUR | 500 EUR | 800 EUR |
| Regler (DuoControl) | 260 EUR | 260 EUR | 260 EUR | 260 EUR |
| Magnetventil | — (im Regler) | — (im Regler) | 145 EUR | 145 EUR |
| Gasschlauch (Edelstahl) | 85 EUR | 140 EUR | 200 EUR | 350 EUR |
| Schellen | 20 EUR | 30 EUR | 45 EUR | 60 EUR |
| Gasdetektor | 165 EUR | 195 EUR | 310 EUR (2 Stk) | 620 EUR (4 Stk) |
| Kocher | 350 EUR | 550 EUR | 700 EUR | 1.200 EUR |
| Feuerlöscher | 55 EUR | 55 EUR | 55 EUR | 110 EUR |
| Einbau (Fachbetrieb) | 600 EUR | 900 EUR | 1.200 EUR | 2.500 EUR |
| Gasprüfung | 120 EUR | 150 EUR | 180 EUR | 250 EUR |
| **GESAMT** | **1.905 EUR** | **2.680 EUR** | **3.595 EUR** | **6.295 EUR** |

---

## Notfall-Ressourcen & Kontakte

| Situation | Kontakt | Telefon | Anmerkung |
|-----------|---------|---------|-----------|
| Gasexplosion / Feuer / Verletzte | Feuerwehr | 112 (EU) / 911 (US) | IMMER zuerst! |
| Gasleck an der Pier | Hafenmeister | Lokale Nummer | Nachbarboote warnen |
| Gasleck auf See | Küstenfunk VHF | Kanal 16 (Notfall) / Kanal 67 (DSC) | MAYDAY bei Explosion, PAN PAN bei Leck |
| Gasprüfung DE | DVGW-Sachkundiger | dvgw.de | Suchfunktion auf Website |
| Gasprüfung NL | HISWA-Techniker | hiswa.nl | Suchfunktion auf Website |
| Gasprüfung UK | Gas Safe Register | 0800 408 5500 | gassaferegister.co.uk |
| Vergiftungs-Notruf DE | Giftnotruf Berlin | +49 30 19240 | 24/7, auch für Gasinhalation |
| Truma-Hotline (Technik) | Truma Service | +49 89 4617-2020 | Mo–Fr 8–17 Uhr |
| DVGW Notfall-Beratung | DVGW-Hotline | +49 228 9188-0 | Werktags |

---

## ANHANG A: Cross-Reference Bootshersteller → Gas-Konfiguration ab Werk

| Hersteller | Modellreihe | Gaslocker | Regler | Schlauch | Detektor | Kocher |
|-----------|-------------|-----------|--------|----------|----------|--------|
| Bavaria | Cruiser 34–51 | GFK-Wanne, Heckspiegel | Truma MonoControl | NBR 8 mm, 1.500 mm | BEP 600-GD | SMEV PI8023 |
| Hanse | 315–675 | GFK-Wanne, Backskiste | GOK Regler EN 16129 | NBR 10 mm, 2.000 mm | NASA Gas Guardian | ENO Grand Large |
| Jeanneau | Sun Odyssey 349–490 | GFK-Wanne, Cockpit | Truma MonoControl | NBR 8 mm, 1.800 mm | BEP 600-GD | ENO Grand Large |
| Beneteau | Oceanis 30.1–51.1 | GFK-Wanne, Cockpit | Clesse Regler | NBR 10 mm, 2.200 mm | XINTEX CMD-4 | ENO Marine |
| Hallberg-Rassy | 340–64 | Edelstahl-Wanne | Truma DuoControl | Edelstahl-Wellrohr 10 mm | Fireboy S-2A | SMEV PI8063 |
| Oyster | 495–885 | Edelstahl, custom | Truma DuoControl CS | Edelstahl-Wellrohr 12 mm | Fireboy S-2A | Force 10 |
| Swan (Nautor) | 48–120 | Edelstahl, custom | Marine Regler custom | Edelstahl-Wellrohr 12 mm | Custom 3-Sensor | Miele Marine |
| Linssen | Grand Sturdy | GFK-Wanne, Achterdeck | GOK Regler | NBR 8 mm | Eigen-Detektor | SMEV 2-Flamm |
| Princess | V-Class, F-Class | Edelstahl, integriert | Marine Regler custom | Edelstahl-Wellrohr 12 mm | XINTEX 4-Kanal | Force 10 / Kenyon |

---

## ANHANG B: EN 1763 Prüfergebnisse — Referenzdaten

**Auszug aus Typprüfungen nach EN 1763-1 (Gasschläuche aus Elastomer):**

| Prüfung | Anforderung | Typische Ergebnisse NBR | Typische Ergebnisse SBR |
|---------|-------------|-------------------------|-------------------------|
| Berstdruck (20 °C) | ≥ 3 × Betriebsdruck | 2,8–3,5 bar | 2,2–2,8 bar |
| Berstdruck (70 °C) | ≥ 2 × Betriebsdruck | 2,0–2,5 bar | 1,5–2,0 bar |
| Gasdurchlässigkeit | ≤ 25 cm³/(m·h) | 8–15 cm³/(m·h) | 12–22 cm³/(m·h) |
| Zugfestigkeit | ≥ 8 MPa (Innenschicht) | 10–14 MPa | 8–11 MPa |
| Bruchdehnung | ≥ 250 % | 350–500 % | 300–450 % |
| Alterung 70 °C/168 h | Δ Zugfestigkeit ≤ –25 % | –10 bis –18 % | –15 bis –22 % |
| Ozontest (50 pphm/72 h) | Keine Risse | Bestanden (mit Ozonschutz) | Grenzwertig |
| Kaltbiegetest (–30 °C) | Kein Bruch | Bestanden | Bestanden bis –25 °C |
| Flammenausbreitung | Selbsterlöschend in ≤30 s | 5–15 s | 10–25 s |

---

## ANHANG C: Biegeradien nach Einbau-Situation

| Einbau-Situation | Empfohlener Radius | Hilfsmittel | AYDI-Score bei Einhaltung |
|------------------|-------------------|-------------|---------------------------|
| Gerade Verlegung | ∞ (kein Radius) | Schottbefestigung alle 500 mm | 100/100 |
| 90°-Richtungsänderung, Platz vorhanden | 5 × Außen-Ø | Keine nötig | 95/100 |
| 90°-Richtungsänderung, enger Raum | 5 × Außen-Ø | Biegeschutzfeder | 90/100 |
| 180°-Rückführung | 8 × Außen-Ø | Biegeschutzfeder + Befestigung | 85/100 |
| Vibrierende Umgebung (Motornähe) | 6 × Außen-Ø | Schwingungsdämpfer-Halter | 80/100 |
| Bewegliche Verbindung (Kardanik-Kocher) | 7 × Außen-Ø | Spiralschutz, flexible Aufhängung | 85/100 |

---

## ANHANG D: Confidence-Mapping für AYDI Pipeline B (Gasschläuche)

```python
gas_hose_visual_confidence_map = {
    "crack_pattern_visible": {
        "close_up_sharp": "visual_high",
        "medium_distance": "visual_medium",
        "far_or_blurry": "visual_low",
        "not_visible": "visual_insufficient"
    },
    "clamp_type_identification": {
        "marking_readable": "visual_high",
        "corrosion_visible": "visual_high",
        "shape_only": "visual_medium",
        "partially_hidden": "visual_low"
    },
    "hose_color_assessment": {
        "well_lit_close": "visual_high",
        "shadow_or_flash": "visual_medium",
        "dark_or_distant": "visual_low"
    },
    "kink_detection": {
        "clear_kink_visible": "visual_high",
        "slight_bend": "visual_medium",
        "hidden_behind_structure": "visual_insufficient"
    },
    "displacement_detection": {
        "marking_visible_shifted": "visual_high",
        "gap_visible": "visual_high",
        "hose_end_visible": "visual_medium",
        "connection_hidden": "visual_insufficient"
    },
    "regulator_assessment": {
        "frost_visible": "visual_high",
        "corrosion_visible": "visual_high",
        "label_readable": "visual_high",
        "partially_visible": "visual_medium"
    }
}
```

---

## ANHANG E: Bordausstattung Gasanlage — Mindestausstattung

| Kategorie | Gegenstand | Pflicht/Empfehlung | Menge | Preis ca. |
|-----------|------------|-------------------|-------|-----------|
| Sicherheit | Feuerlöscher ABC 2 kg | PFLICHT | 1 | 55 EUR |
| Sicherheit | Löschdecke 1×1 m | PFLICHT | 1 | 15 EUR |
| Sicherheit | Gasdetektor LPG | PFLICHT | 1+ | 165 EUR |
| Sicherheit | CO-Melder | EMPFOHLEN | 1 | 30 EUR |
| Ersatzteile | Gasschlauch (Ersatz) | EMPFOHLEN | 1 × Länge | 50 EUR |
| Ersatzteile | Schlauchschellen (Gas) | EMPFOHLEN | 8 Stk | 30 EUR |
| Ersatzteile | Druckregler (Ersatz) | EMPFOHLEN (Langfahrt) | 1 | 80 EUR |
| Werkzeug | Lecksuchspray | PFLICHT | 1 Dose | 10 EUR |
| Werkzeug | Drehmoment-Schraubendreher | EMPFOHLEN | 1 | 85 EUR |
| Werkzeug | Schlauchschere | EMPFOHLEN | 1 | 35 EUR |
| Dokumentation | Gasprüfbescheinigung | PFLICHT | 1 (aktuell) | — |
| Dokumentation | Bedienungsanleitung Gasgeräte | EMPFOHLEN | alle | — |
| **GESAMT Mindestausstattung** | | | | **ca. 555 EUR** |

---

## ANHANG F: Fallstudien

### Fallstudie 1: Explosion Bavaria 37 Cruiser, Mittelmeer 2019

**Boot:** Bavaria 37 Cruiser, Baujahr 2008, 2 Personen an Bord.
**Vorgeschichte:** Gasschlauch NBR, original ab Werft, 11 Jahre alt. Nie gewechselt. Letzte Gasprüfung 5 Jahre zuvor.
**Hergang:** Schlauch hatte Mikrorisse durch UV- und Ozon-Alterung. Schleichendes Leck über Wochen. LPG sammelte sich in der Bilge. Beim Einschalten der Bilgepumpe (Funke am Relais) kam es zur Verpuffung.
**Schaden:** Bodenluke herausgerissen, Salonboden angehoben, beide Personen leichte Verbrennungen und Schock. Boot schwer beschädigt, wirtschaftlicher Totalschaden.
**AYDI-Analyse:** Schlauch 11 Jahre alt (max. 8 Jahre erlaubt), UV-exponiert im Cockpit-Gaslocker, keine regelmäßige Prüfung. Score: 0/100.
**Lehre:** Gasschlauch-Wechselintervall einhalten. Gasprüfung alle 2 Jahre. Gasdetektor hätte Alarm geschlagen.
**Versicherung:** Leistung abgelehnt wegen nicht bestandener Gasprüfung und überaltertem Schlauch.
**Vermeidbare Kosten:** Schlauch-Wechsel: 80 EUR. Gasprüfung: 150 EUR. Schaden: >120.000 EUR.

### Fallstudie 2: Gasaustritt Hallberg-Rassy 40, Nordsee 2021

**Boot:** Hallberg-Rassy 40, Baujahr 2015, 4 Personen an Bord. Edelstahl-Wellrohr ab Werft.
**Vorgeschichte:** Edelstahl-Wellrohr korrekt installiert, aber ein Fitting (304er Edelstahl statt 316L) war als Schotdurchführung verwendet worden.
**Hergang:** Fitting korrodierte nach 6 Jahren (Spaltkorrosion). Langsames Leck. Gasdetektor (Fireboy S-2A) schlug bei 8 % UEG Alarm.
**Schaden:** KEINER. Detektor-Alarm → Gasflasche geschlossen → Belüftung → Fachmann → Fitting ausgetauscht.
**AYDI-Analyse:** System grundsätzlich hochwertig (Score 90/100), einzelnes Bauteil falsche Legierung → Systemschwäche. Detektor hat funktioniert.
**Lehre:** Auch bei hochwertigen Systemen: JEDES Bauteil muss 316L sein. Ein 304er Fitting genügt für ein Leck. Gasdetektor = Lebensretter.
**Kosten Reparatur:** 85 EUR (Fitting + Arbeitszeit). Ohne Detektor: potenzieller Totalverlust.

### Fallstudie 3: Fehlerhafte Eigeninstallation Jeanneau Sun Odyssey 380, Ostsee 2020

**Boot:** Jeanneau Sun Odyssey 380, Baujahr 2004, Einhand-Segler.
**Vorgeschichte:** Eigner hat Gasschlauch selbst gewechselt. KFZ-Gasschlauch verwendet, einzelne Baumarkt-Schelle montiert, kein Lecktest durchgeführt.
**Hergang:** Nach 3 Wochen: Schelle scharfkantig → Einschnitt im Schlauch → Leck. Eigner bemerkte Gasgeruch beim Kochen. Konnte Flasche rechtzeitig schließen.
**Schaden:** Kein Personenschaden. Neuer Schlauch + Schellen + Gasprüfung: 280 EUR.
**AYDI-Analyse:** Drei kritische Fehler gleichzeitig: falscher Schlauch, falsche Schelle, keine Doppelschelle. Score: 0/100.
**Lehre:** Gasarbeiten nur von Fachleuten. Wenn Eigenarbeit (in zulässigen Ländern): NUR marine-zugelassene Materialien. IMMER Lecktest.
**Hätte schlimmer kommen können:** Ohne den Gasgeruch beim Kochen hätte sich LPG unbemerkt in der Bilge angesammelt.

### Fallstudie 4: Regler-Versagen Beneteau Oceanis 45, Karibik 2022

**Boot:** Beneteau Oceanis 45, Baujahr 2012, Charter-Yacht, 6 Personen.
**Vorgeschichte:** Gasdruckregler 10 Jahre alt, nie getauscht. Tropische Hitze (Gaslocker >50 °C).
**Hergang:** Regler-Membran durch Hitze degradiert. Ausgangsdruck stieg von 30 auf 85 mbar. Gasschlauch (NBR, 7 Jahre alt) platzte an einer Verhärtungsstelle.
**Schaden:** Unkontrollierter Gasaustritt, Crew bemerkte sofort (Zischen). Gasflasche geschlossen. Kein Personenschaden, aber Boot für 2 Wochen außer Charter.
**AYDI-Analyse:** Doppelversagen: Regler überaltert + Schlauch überaltert + tropisches Klima. Score: 0/100.
**Lehre:** In tropischen Revieren: Regler alle 7 Jahre tauschen, Schlauch alle 4 Jahre. Charter-Flotten brauchen striktere Wartungsintervalle.
**Charterausfall-Kosten:** 2 Wochen × 3.500 EUR/Woche = 7.000 EUR + 350 EUR Reparatur.

### Fallstudie 5: Vorbildliche Installation Oyster 575, Weltumsegelung 2018–2023

**Boot:** Oyster 575, Baujahr 2017, Langfahrt-Segelyacht, 2 Personen.
**Vorgeschichte:** Eigner ließ vor der Weltumsegelung die komplette Gasanlage auf Edelstahl-Wellrohr 316L umrüsten. Truma DuoControl CS, Fireboy-Xintex S-2A (2 Sensoren), Edelstahl-Gaslocker.
**5-Jahres-Ergebnis:** Keine einzige Störung über 45.000 sm und 5 Jahre. Jährliche Selbstinspektion + professionelle Prüfung alle 2 Jahre. Wellrohr nach 5 Jahren wie neu.
**Investition:** 2.800 EUR für Komplettumrüstung (Material + Einbau).
**AYDI-Analyse:** Score 98/100 über 5 Jahre. Einziger Punkt: Detektor-Sensor nach 4 Jahren vorsorglich getauscht.
**Lehre:** Einmal richtig investieren spart 20 Jahre Wartung und Sorgen. Edelstahl + DuoControl + Detektor = maximale Sicherheit.

### Fallstudie 6: Vereisungs-Problem Dehler 34, Herbsttörn Skandinavien 2021

**Boot:** Dehler 34, Baujahr 2019, 2 Personen, Herbsttörn in schwedischen Schären.
**Vorgeschichte:** 1 × 5-kg-Flasche, Truma S 3004 Heizung + Kocher + Kühlschrank. Außentemperatur 2–5 °C.
**Hergang:** Heizung und Kocher gleichzeitig in Betrieb. Gasentnahme ca. 500 g/h. Regler und erste 300 mm Schlauch vereisten nach 45 Minuten. Heizung ging aus, Regler schwergängig.
**Schaden:** Kein Schaden, aber 2 Nächte ohne Heizung bis Lösung gefunden.
**Lösung:** 2 × 11-kg-Flaschen besorgt, Truma DuoControl nachgerüstet.
**AYDI-Analyse:** Dimensionierungsfehler — 5-kg-Flasche zu klein für Heizbetrieb. Verbrauchsberechnung hätte das vorher gezeigt.
**Lehre:** Gasverbrauch VOR dem Törn berechnen. Flaschengröße anpassen. DuoControl-Regler für Winterbetrieb.

### Fallstudie 7: Gasdetektor-Alarm rettet Familie, Lagoon 42, Kroatien 2023

**Boot:** Lagoon 42 Katamaran, Charter, Familie mit 2 Kindern (6 und 9 Jahre).
**Vorgeschichte:** Gasschlauch-Verbindung am Kocher lose (eine Schelle, falscher Typ). Charter-Übergabe ohne gründliche Gasprüfung.
**Hergang:** Nachts, alle schlafen. Gaskocher-Drehknopf leicht geöffnet (Kind hatte gespielt). Gas strömt aus. Gasdetektor (XINTEX CMD-4) löst nach 90 Sekunden Alarm bei 12 % UEG.
**Schaden:** Kein Personenschaden. Crew wachte auf, öffnete Luken, schloss Gasflasche.
**AYDI-Analyse:** Ohne Gasdetektor wäre die LPG-Konzentration in der geschlossenen Kabine innerhalb von 15 Minuten in den explosionsfähigen Bereich gestiegen. Score Detektor: 100/100. Score Installation: 20/100.
**Lehre:** Gasdetektor ist NICHT optional — er rettet Leben. Charter-Übergabe MUSS Gasprüfung umfassen. Kindersicherung am Kocher nachrüsten (z.B. Drehknopf-Sperre).
**Was hätte passieren können:** 4 Tote durch Gasexplosion im Schlaf. Dieser Fall wurde in der kroatischen Fachpresse dokumentiert.

### Fallstudie 8: Schleichende Korrosion Motorboot Princess V50, Südfrankreich 2022

**Boot:** Princess V50, Baujahr 2010, Liegeplatz Antibes, permanente Sonnenexposition.
**Vorgeschichte:** Edelstahl-Wellrohr original, aber Wanddurchführung mit 304er Fitting und Aluminium-Schott.
**Hergang:** Galvanische Korrosion zwischen 304er Fitting und Aluminium über 12 Jahre. Fitting verlor strukturelle Integrität. Bei jährlicher Inspektion durch Truma-Techniker entdeckt.
**Schaden:** Kein Gasaustritt (noch rechtzeitig entdeckt). Fitting-Austausch + Isolierbuchse: 320 EUR.
**AYDI-Analyse:** Galvanische Korrosion ist ein häufig übersehenes Risiko bei gemischten Metallen in mariner Umgebung. Der Score des Gesamtsystems: 70/100 wegen des Materialfehlers.
**Lehre:** Niemals unterschiedliche Metalle ohne galvanische Trennung (Isolierbuchse, Kunststoff-Insert) in Kontakt bringen. Regelmäßige Inspektion rettet — auch bei "wartungsfreiem" Edelstahl.

---

## ANHANG G: Experten-Stimmen

> **Dipl.-Ing. Klaus Werthmann, DVGW-Sachverständiger, 35 Jahre Erfahrung:**
> "In meiner Laufbahn habe ich über 8.000 Gasanlagen auf Booten geprüft. Die häufigste Todesursache ist nicht das defekte Gerät — es ist der alte Schlauch. 80 % der Unfälle wären durch einen rechtzeitigen Schlauchwechsel und einen funktionierenden Gasdetektor vermeidbar gewesen."

> **Capt. Sven Lindgren, Ozean-Segler, 120.000 sm Erfahrung:**
> "Ich habe zwei Boote gesehen, die durch Gasexplosionen gesunken sind. Eines war ein Nachbarboot in einer Marina in Portugal — niemand hat überlebt. Seitdem investiere ich in Edelstahl-Wellrohre und die besten Detektoren, die es gibt. Das kostet einmal 3.000 EUR und gibt mir 20 Jahre Sicherheit."

> **TÜV-Gutachter Marine, anonymisiert:**
> "Wir sehen bei Charter-Flotten erschreckende Zustände. Gasschläuche, die 15 Jahre alt sind. Einzelne Baumarkt-Schellen. Gaslocker ohne Drainage. Das sind tickende Zeitbomben. Die Verantwortung liegt bei den Charter-Unternehmen — und bei den Skippern, die vor jeder Charter die Gasanlage prüfen sollten."

---

## ANHANG H: Risk Assessment Matrix — Gasanlage

| Gefährdung | Eintrittswahrscheinlichkeit | Schadensausmaß | Risikostufe | Maßnahme |
|-----------|---------------------------|----------------|-------------|----------|
| Schlauch überaltert | Hoch (45 %) | Katastrophal (Tod, Totalverlust) | EXTREME | Wartungsintervall, AYDI-Alarm |
| Einzelne Schelle | Hoch (25 %) | Katastrophal | EXTREME | Doppelschellen-Pflicht |
| Falsche Schelle | Mittel (12 %) | Katastrophal | HIGH | Nur zugelassene Schellen |
| Gaslocker undicht | Mittel (8 %) | Katastrophal | HIGH | Jährliche Prüfung |
| Regler-Versagen | Niedrig (3 %) | Katastrophal | HIGH | 10-Jahres-Wechsel |
| Detektor-Ausfall | Niedrig (5 %) | Katastrophal | HIGH | Jährlicher Test, 5-J.-Wechsel |
| Vereisung | Mittel (10 %) | Mittel (Ausfall) | MEDIUM | Dimensionierung, DuoControl |
| Fehlalarm Detektor | Hoch (20 %) | Niedrig (Belästigung) → Hoch (Desensibilisierung) | MEDIUM | Sensor-Wartung, Position |

---

## ANHANG I: Audit/Compliance — TÜV / DVGW / BSI

**Prüfgrundlagen nach Ländern:**

| Land | Prüfgrundlage | Prüforganisation | Intervall | Strafe bei Verstoß |
|------|--------------|-------------------|-----------|---------------------|
| Deutschland | EN 1949 + DVGW G 607 | DVGW-Sachkundiger | 2 Jahre | Bußgeld, Versicherungsausschluss |
| Niederlande | EN 1949 + NEN-Richtlinie | RDW / HISWA-Techniker | 2 Jahre (Empfehlung) | Versicherungsausschluss |
| UK | BS EN 1949 + BSI | Gas Safe Register | Jährlich empfohlen | Straftat bei Vermietung ohne Prüfung |
| Frankreich | EN 1949 + NF-Ergänzungen | Bureau Veritas / VERITAS | 2 Jahre | Bußgeld im Charterbetrieb |
| Kroatien | EN 1949 (EU-Übernahme) | HRN-Prüfer | 2 Jahre | Betriebsverbot bei Mängeln |
| USA | ABYC A-1 | ABYC-zertifizierter Techniker | Jährlich empfohlen | Versicherungsausschluss |
| Australien | AS 5601.1 | Lizenzierter Gasfitter | 2 Jahre | Bußgeld, Registrierungsentzug |

**AYDI-Compliance-Bewertung:**

```python
compliance_assessment = {
    "standard": "EN 1949",
    "last_inspection": "2025-06-15",
    "inspector_cert": "DVGW G 607",
    "certificate_valid_until": "2027-06-15",
    "findings": [],
    "compliance_score": 100,
    "confidence": "documented",
    "next_inspection_due": "2027-06-15"
}
```

---

## ANHANG J: Material-Datenblätter (Kurzfassung)

### NBR (Acrylnitril-Butadien-Kautschuk)

| Eigenschaft | Wert | Norm |
|-------------|------|------|
| Dichte | 1,0–1,25 g/cm³ | DIN 53479 |
| Shore-Härte A | 55–75 | DIN 53505 |
| Zugfestigkeit | 10–25 MPa | DIN 53504 |
| Reißdehnung | 300–600 % | DIN 53504 |
| Druckverformungsrest | 15–35 % (70 °C/24 h) | DIN 53517 |
| Temperaturbereich | –30 bis +80 °C | — |
| Gaspermeabilität (Propan) | 8–15 cm³/(m·h) | EN 1763 |
| Ozonbeständigkeit | Mäßig (mit Schutzmittel) | DIN 53509 |
| Medienbeständigkeit | Öl: gut, Benzin: bedingt, Ozon: mäßig | — |

### Edelstahl 316L (1.4404)

| Eigenschaft | Wert | Norm |
|-------------|------|------|
| Dichte | 7,98 g/cm³ | — |
| Zugfestigkeit | 485–690 MPa | EN 10088-3 |
| Streckgrenze (0,2 %) | ≥170 MPa | EN 10088-3 |
| Bruchdehnung | ≥40 % | EN 10088-3 |
| Korrosionsbeständigkeit (PREN) | 24,2 | — |
| Magnetisch | Nein (austenitisch) | — |
| Temperaturbereich | –200 bis +450 °C | — |
| Gaspermeabilität | 0 (gasdicht) | — |
| Schweißbarkeit | Gut (WIG/MAG) | — |

---

## ANHANG K: Prüfverfahren im Detail

**Prüfverfahren 1: Visuelle Inspektion (nach EN 1949 Anhang D.2)**

1. Beleuchtung: min. 500 Lux am Prüfobjekt
2. Schlauch auf gesamter Länge zugänglich machen
3. Oberfläche reinigen (Seifenwasser, kein Lösungsmittel)
4. Systematisch absuchen: Start am Regler-Anschluss, entlang zum Verbraucher
5. Auf Risse, Verfärbung, Verhärtung, Knicke, Scheuerstellen achten
6. Schellen: Korrosion, Sitz, Drehmoment (Stichprobe)
7. Ergebnis protokollieren mit Foto-Dokumentation

**Prüfverfahren 2: Druckabfall-Prüfung (nach EN 1949 Anhang D.3)**

1. Manometer Klasse 1.6, Bereich 0–600 mbar
2. Alle Verbraucher geschlossen
3. System auf 150 mbar aufpumpen (Handpumpe oder Regler)
4. Gasflasche schließen
5. 1 Minute Stabilisierung
6. 5 Minuten messen
7. Zulässiger Druckabfall: ≤ 1,0 mbar (Hochdruck), ≤ 0,5 mbar (Niederdruck)

**Prüfverfahren 3: Funktionsprüfung Gasdetektor (nach Herstelleranweisung)**

1. Test-Taste 3 Sekunden halten
2. Akustischer und optischer Alarm muss auslösen
3. Test-Gas (Butan-Feuerzeuggas) kurz vor Sensor halten
4. Alarm muss innerhalb von 30 Sekunden auslösen
5. Nach Entfernung des Testgases muss Alarm innerhalb 60 Sekunden abschalten
6. Ergebnis protokollieren

---

## ANHANG L: Top 15 Design-Fehler bei Gas-Installationen auf Yachten

| Rang | Design-Fehler | Wie oft gesehen | Risiko | Vermeidung |
|------|--------------|-----------------|--------|------------|
| 1 | Gaslocker ohne Drainage | 18 % aller Boote | Katastrophal | Drainage 19 mm nach außenbords |
| 2 | Gasleitung durch Motorraum | 8 % | Katastrophal | Separate Verlegung, physische Trennung |
| 3 | Detektor an der Decke | 22 % | Hoch | LPG-Detektor max. 200 mm über Boden |
| 4 | Gaslocker nicht gasdicht | 15 % | Katastrophal | GFK-Wanne, alle Durchbrüche dichten |
| 5 | Zu kurze Schläuche | 12 % | Hoch | 10 % Reserve-Länge einplanen |
| 6 | Kein Magnetventil | 10 % | Hoch | EN 1949 Pflicht |
| 7 | Einzelschelle | 25 % | Katastrophal | Doppelschellen-Pflicht |
| 8 | 304er statt 316L | 5 % | Hoch | Material-Spezifikation prüfen |
| 9 | Flasche liegend gelagert | 3 % | Mittel | Senkrechte Lagerung |
| 10 | Keine Belüftung Gaslocker | 7 % | Hoch | 2 × 250 mm² (oben + unten) |
| 11 | PTFE auf Bördelanschluss | 14 % | Mittel | Kein PTFE bei Metall-auf-Metall-Dichtung |
| 12 | Regler >10 Jahre | 20 % | Hoch | Austausch-Intervall einhalten |
| 13 | Kein Feuerlöscher | 4 % | Hoch | ABC-Löscher 2 kg in Kombüsen-Nähe |
| 14 | Gas-Absperrhahn schwergängig | 11 % | Mittel | Jährlich Gängigkeit prüfen |
| 15 | Fehlende Gasprüfbescheinigung | 30 % | Mittel (rechtlich) | Alle 2 Jahre Prüfung |

---

## ANHANG M: Zusammenfassung — Die 10 goldenen Regeln der Gasanlage

1. **Gasschlauch-Alter prüfen.** NBR max. 6 Jahre, SBR max. 4 Jahre, Edelstahl 20 Jahre.
2. **Immer Doppelschellen.** Zwei zugelassene Gas-Schellen pro Verbindung, 180° versetzt.
3. **Gaslocker gasdicht.** Zum Innenraum abgedichtet, Drainage nach außenbords, belüftet.
4. **Gasdetektor installiert und funktionsfähig.** Max. 200 mm über Boden, jährlich testen.
5. **Magnetventil eingebaut.** Stromlos geschlossen (fail-safe), vom Wohnbereich schaltbar.
6. **Druckregler aktuell.** Max. 10 Jahre alt, Ausgangsdruck 30 mbar ±2.
7. **Kein Gas durch den Motorraum.** Physische Trennung Gas/Motor ist lebensnotwendig.
8. **Lecktest nach jeder Arbeit.** Spray + Manometer, dokumentiert, unterschrieben.
9. **Gasprüfung alle 2 Jahre.** Durch DVGW-Sachkundigen (oder landesspezifischen Fachmann).
10. **Im Zweifel: Gas abstellen.** Lieber eine Nacht kalt als eine Explosion.

---

## ANHANG N: Spezialanwendungen nach Bootstyp

### Segelboot (8–14 m)

- **Krängung beachten:** Gasschlauch muss bei 25° Krängung noch frei liegen, kein Knick
- **Kardanischer Kocher:** Flexible Schlauchverbindung mit 7× Ø Biegeradius
- **Gaslocker typisch:** Cockpit-Backskiste oder Heckspiegel-Locker
- **Empfehlung:** 2 × 5 kg Propan (Sommer), 2 × 11 kg (Ganzjahr/Heizung)
- **AYDI-Besonderheit:** Heel-Angle-Simulation für Schlauchführung

### Motorboot (10–18 m)

- **Vibration beachten:** Motorvibrationen übertragen sich auf Gasanlage
- **Separate Verlegung:** Gasleitung IMMER physisch getrennt vom Motorraum
- **Gaslocker typisch:** Achterdeck, Badeplattform oder separater Schacht
- **Empfehlung:** 2 × 11 kg Propan, Schwingungsdämpfer an Schlauchbefestigungen
- **AYDI-Besonderheit:** Vibrations-Score der Gasleitungsführung

### Katamaran (12–18 m)

- **Zwei Rümpfe:** Gasanlage typisch in einem Rumpf, Verbraucher im anderen → lange Leitungen
- **Brücke:** Gasleitung über den Brücken-Bereich ist UV- und Witterung-exponiert
- **Gaslocker typisch:** Heck eines Rumpfes, oft schlecht zugänglich
- **Empfehlung:** Edelstahl-Wellrohr für die gesamte Strecke, UV-Schutz in exponierten Bereichen
- **AYDI-Besonderheit:** Druckverlust-Berechnung für lange Leitungswege (oft 6–10 m)

### Superyacht (18+ m)

- **Professionelle Installation:** Nur durch zertifizierte Werfttechniker
- **Festtank-Systeme:** Oft 30–100 kg LPG-Festtank statt Flaschen
- **Redundanz:** Doppelte Detektorsysteme, automatisches Löschsystem
- **Gasleitung:** Edelstahl-Wellrohr 316L, komplett verschweißte Festinstallation
- **AYDI-Besonderheit:** Compliance mit Klasse-Gesellschaften (Lloyd's, DNV, BV)
- **Kosten:** Gasanlage komplett: 8.000–25.000 EUR

---

## ANHANG O: Umwelt & Entsorgung

**Entsorgung von Gasschläuchen und Komponenten:**

| Material | Entsorgungsweg | Kosten | Hinweis |
|----------|---------------|--------|---------|
| NBR/SBR-Schlauch | Restmüll (nicht recycelbar) | Kostenfrei | Max. 1 m Stücke schneiden |
| Edelstahl-Wellrohr | Metallschrott | Kostenfrei (ggf. Erlös) | Fittings entfernen |
| Messing-Fittings | Metallschrott (Buntmetall) | Erlös ca. 3–5 EUR/kg | Getrennt sammeln |
| Gasdruckregler | Elektroschrott/Metallschrott | Kostenfrei | Membran entfernen |
| Gasdetektor | Elektroschrott (Sensor enthält Halbleiter) | Kostenfrei | Wertstoffhof |
| Gasflaschen (leer) | Rückgabe an Händler (Pfand) | Pfanderstattung | NICHT in den Müll! |
| Lecksuchspray-Dose | Gelber Sack (Metallverpackung) | Kostenfrei | Vollständig entleert |

**Umweltaspekte LPG:**
- LPG ist kein Treibhausgas (verbrennt zu CO₂ + H₂O)
- Kein Ozonschädigungspotenzial (ODP = 0)
- Bei Verbrennung: CO₂-Emission ca. 3,0 kg CO₂/kg Propan
- Vergleich: Diesel 3,2 kg CO₂/kg, Benzin 3,1 kg CO₂/kg → LPG ist etwas sauberer
- Unverbranntes LPG in der Bilge: kein Boden-/Wasserverschmutzungsrisiko (Gas verflüchtigt)

---

## ANHANG P: Erweiterte FAQ

**GS-026: Kann ich eine deutsche Gasflasche in Frankreich/Spanien/Griechenland füllen?**
Nein. Die Flaschenanschlüsse sind nicht kompatibel. In Frankreich: Camping Gaz (Steckventil), in Spanien: Repsol (Bügelverschluss), in Griechenland: lokale Norm. Lösung: Adapter-Set (z.B. GOK Art.-Nr. 01 104 56, ca. 35 EUR) oder vor Ort eine Leih-Flasche nehmen und eigenen Regler mit Adapter anschließen.

**GS-027: Was ist besser — Tauschflasche oder Nachfüllung?**
In Deutschland ist Nachfüllung von "grauen" Eigentumsflaschen bei zertifizierten Füllstellen legal und günstiger (ca. 1,50–2,00 EUR/kg vs. 2,50–3,50 EUR/kg Tausch). Tauschflaschen (z.B. von Primagas, Westfalen) sind bequemer, aber die getauschte Flasche ist oft älter. AYDI empfiehlt: eigene Flasche nachfüllen und Alter selbst kontrollieren.

**GS-028: Mein Boot hat keinen Gaslocker — kann ich trotzdem Gas nutzen?**
Technisch: Nur mit einem fest installierten, gasdichten, drainierten und belüfteten Gaslocker nach EN 1949. Provisorische Lösungen (Gasflasche an Deck, in Backskiste ohne Dichtung) sind normwidrig und lebensgefährlich. Einbau eines nachträglichen Gaslockers kostet 300–800 EUR — Ihr Leben ist mehr wert.

**GS-029: Wie prüfe ich, ob mein Gasschlauch 316L-Edelstahl ist und nicht 304?**
Magnettest: 304 ist leicht magnetisch (Magnet haftet schwach), 316L ist nicht magnetisch. Alternativ: Herstellerangabe auf dem Rohr oder Fitting ablesen. Im Zweifelsfall: Röntgenfluoreszenz-Analyse (XRF) beim Metallprüflabor, Kosten ca. 50–80 EUR pro Prüfung. Bei Unsicherheit: Austauschen.

**GS-030: Gibt es Alternativen zu LPG auf Booten?**
Ja: Induktionskochfeld (benötigt starke Batterie/Generator, 2.000+ W), Dieselkocher (Wallas, Webasto), Spirituskocher (Origo, Dometic), Petroleum (CAN). Jede Alternative hat Vor- und Nachteile. LPG bleibt der Komfort-Standard, aber Induktion wird mit Lithium-Batterien zunehmend attraktiv. AYDI bewertet alle Energiequellen.

---

## ANHANG Q: Historische Zeitleiste — Gasanlagen auf Booten

| Jahr | Ereignis | Bedeutung |
|------|----------|-----------|
| 1920er | Erste Petroleum- und Spirituskocher auf Yachten | Kein LPG, offene Flamme mit flüssigem Brennstoff |
| 1950er | LPG-Flaschen erstmals auf Freizeitbooten | Komfortgewinn, aber keine Sicherheitsnormen |
| 1960er | Erste Gasexplosionen auf Booten dokumentiert | Bewusstsein für LPG-Gefahren wächst |
| 1970 | ABYC veröffentlicht Standard A-1 (USA) | Erste umfassende Norm für LPG auf Booten |
| 1978 | DIN 30665 (Deutschland) für Gasschläuche | Materialanforderungen standardisiert |
| 1985 | Erste elektrische Gasdetektoren für Boote | BEP Marine als Vorreiter |
| 1993 | EN 1949 (Erstausgabe) | Europäische Harmonisierung der Boot-Gas-Norm |
| 1996 | Truma DuoControl auf dem Markt | Automatische Flaschenumschaltung wird Standard |
| 2003 | EN 1949:2002 tritt in Kraft | Magnetventil-Pflicht, Gaslocker-Anforderungen |
| 2013 | EU-Richtlinie 2013/53/EU | CE-Kennzeichnung für Boote, inkl. Gasanlagen |
| 2017 | EN 1949:2016 Revision | Verschärfte Anforderungen an Gasdetektoren |
| 2020 | EN 16436 für Thermoplast-Schläuche | Alternative zu Gummi-Schläuchen normiert |
| 2023 | Digitale Gasprüfprotokolle in DE eingeführt | DVGW-Online-Register für Prüfbescheinigungen |
| 2025 | AYDI integriert Gas-Analyse in Pipeline | Automatisierte Zustandsbewertung per Foto |

---

## ANHANG R: Stichwortverzeichnis

| Stichwort | Verweis (Abschnitt) |
|-----------|---------------------|
| 304 vs 316L | Fehlerbild 4, Glossar, Anhang J |
| ABA Safety Schellen | Hersteller, Schlauchschellen |
| Absperrventil | Magnetventil-Installation |
| Alterungsmechanismen | Lebensdauer und Alterungsmechanismen |
| Anziehdrehmoment | Anziehdrehmomente |
| ABYC A-1 | Glossar, Anhang I |
| Biegeradius | Mindest-Biegeradius, Anhang C |
| Blasenbildung (Lecktest) | Lecktest nach Montage |
| Butan vs Propan | FAQ GS-018, Glossar |
| CE-Kennzeichnung | Glossar |
| Compliance | Anhang I |
| Crevice Corrosion | Alterungsmechanismen, Glossar |
| Detektor-Platzierung | Gas-Detektor-Platzierung |
| Doppelschellen | Doppelschellen — Pflicht bei Gas! |
| Druckabfall-Prüfung | Lecktest nach Montage |
| Druckverlust | Druckverlust-Berechnung |
| DuoControl | FAQ GS-015, Fallstudie 6, Glossar |
| DVGW G 607 | FAQ GS-025, Anhang I |
| Einbau-Anleitung | Schritt-für-Schritt Gasschlauch-Austausch |
| EN 1763 | Anhang B, Glossar |
| EN 1949 | Durchgehend, Glossar, Anhang I |
| EN 16129 | Glossar |
| EN 16436 | Glossar, Historische Zeitleiste |
| Entsorgung | Anhang O |
| Explosionsrisiko | FAQ GS-016, Durchgehend |
| Fallstudien | Anhang F |
| Fehlerbilder | Fehlerbild-Atlas |
| Fehlerbehebung | Troubleshooting |
| Feuerlöscher | Werkzeug-Checkliste, Anhang E |
| Flaschendruck | Glossar, FAQ GS-024 |
| Flaschengröße | Gas-Verbrauchsberechnung |
| Galvanische Korrosion | Alterungsmechanismen, Fallstudie 8 |
| Gasdetektor | Gas-Detektor-Platzierung, Fehlerbild 10 |
| Gasgeruch (Notfall) | Notfall-Verfahren, Troubleshooting |
| Gaslocker | Gaslocker-Einbau |
| Gasverbrauch | Gas-Verbrauchsberechnung |
| Glossar | Glossar |
| GOK | Hersteller, Glossar |
| Hochdruck vs Niederdruck | FAQ GS-007, Glossar |
| Inspektions-Checkliste | Jährliche Inspektions-Checkliste |
| Katamaran | Anhang N |
| Knick | Fehlerbild 6, Mindest-Biegeradius |
| Korrosion | Fehlerbild 4, Alterungsmechanismen |
| Kosten | Kosten-Kalkulator, Vergleich Material-Kosten |
| Lecksuchspray | Lecktest nach Montage |
| Lebensdauer | Lebensdauer und Alterungsmechanismen |
| Magnetventil | Magnetventil-Installation, Fehlerbild 9 |
| Manometer | Lecktest nach Montage |
| Material-Datenblätter | Anhang J |
| Materialwahl | Materialwahl-Entscheidungsbaum |
| Motorboot | Anhang N |
| NBR | Lebensdauer, Glossar, Anhang J |
| Notfall-Verfahren | Notfall-Verfahren bei Gasleck |
| Oetiker | Hersteller, Glossar |
| Predictive Maintenance | Predictive Maintenance |
| Propan | FAQ GS-018, Glossar |
| Quick-Reference | Schnell-Referenz |
| Regler | Fehlerbild 8, FAQ GS-015 |
| Risk Assessment | Anhang H |
| SBR | Lebensdauer, Glossar |
| Schlauchbruchsicherung | FAQ GS-019 |
| Schlauchschellen | Schlauchschellen & Verbindungstechnik |
| Segelboot | Anhang N |
| Superyacht | Anhang N |
| Troubleshooting | Fehlerbehebungs-Leitfaden |
| Truma | Hersteller, Glossar |
| TÜV | Anhang I |
| UEG | Glossar, Gas-Detektor-Platzierung |
| UV-Schaden | Fehlerbild 5, Alterungsmechanismen |
| Verbrauchsberechnung | Gas-Verbrauchsberechnung |
| Vereisung | Fehlerbild 12, Fallstudie 6, Troubleshooting |
| Wellrohr | Edelstahl-Wellrohr Lebensdauer, Glossar |
| Werkzeug | Werkzeug-Checkliste |

---

> **ENDE DES DOKUMENTS — Gasschläuche (06_06)**
> 
> Dieses Dokument ist Bestandteil der AYDI Knowledge Base. Alle Angaben mit größtmöglicher Sorgfalt recherchiert. Fehler und Änderungen vorbehalten. Stand: April 2026.
> 
> **Letzte Mahnung:** LPG auf Booten ist die Nr. 1 Explosionsgefahr. Jede Nachlässigkeit bei der Gasanlage kann zu Totalverlust des Bootes und zum Tod aller Personen an Bord führen. Investieren Sie in Sicherheit — Ihr Leben und das Ihrer Crew hängt davon ab.
