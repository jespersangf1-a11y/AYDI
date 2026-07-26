# 06.04 — Kraftstoffschläuche (Diesel/Benzin) im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 06.04** — Kategorie 6: Kraftstoffsysteme
> **Confidence-Quelle:** measured (Hersteller-TDS, Normen-Originale), documented (Hersteller-Kataloge, USCG-Zertifikate), estimated (Erfahrungswerte, Forum-Konsens)
> **Letzte Aktualisierung:** 2026-04-23
> **SICHERHEITSKRITISCH:** Kraftstoffschläuche sind Brand- und Explosions-relevante Bauteile. Fehlerhafte Schläuche sind eine der häufigsten Ursachen für Bootsbrände.

---

## Inhaltsverzeichnis

1. [Einführung & Regulatorischer Rahmen](#1-einführung--regulatorischer-rahmen)
2. [Zukunftstechnologien & Neue Materialien](#2-zukunftstechnologien--neue-materialien)
3. [Best Practices nach Revier & Klimazone](#3-best-practices-nach-revier--klimazone)
4. [Regional Sourcing: Verfügbarkeit & Lieferketten weltweit](#4-regional-sourcing-verfügbarkeit--lieferketten-weltweit)
5. [Zweck dieser Wissensdatei](#5-zweck-dieser-wissensdatei)
6. [Pydantic-Modelle für AYDI-Integration](#6-pydantic-modelle-für-aydi-integration)
7. [Grundlagen Kraftstoffschläuche](#7-grundlagen-kraftstoffschläuche)
8. [Hersteller — Vollständige Übersicht](#8-hersteller--vollständige-übersicht)
9. [Motorspezifische Zuordnung](#9-motorspezifische-zuordnung)

---

## 1. Einführung & Regulatorischer Rahmen

### 1.1 Bedeutung für Yacht-Sicherheit (Brand- und Explosionsgefahr)

Kraftstoffschläuche gehören zu den sicherheitskritischsten Komponenten auf jeder Yacht. Ein Versagen — durch Alterung, Materialermüdung, falsche Auswahl oder fehlerhafte Installation — kann innerhalb von Sekunden zu einem Kraftstoffaustritt führen. Die Konsequenzen unterscheiden sich fundamental nach Kraftstoffart:

**Benzin (Ottokraftstoff):**
- Flammpunkt: ca. -20°C — Benzindämpfe sind bei jeder Umgebungstemperatur zündfähig
- Explosionsbereich: 1,0–7,6 Vol.-% in Luft
- Benzindämpfe sind schwerer als Luft (relative Dichte ~3,5) und sammeln sich in Bilgen, Motorräumen und tiefliegenden Räumen
- Ein Liter ausgelaufenes Benzin erzeugt ca. 300 Liter explosionsfähiges Dampf-Luft-Gemisch
- USCG-Statistik: Benzin-Lecks verursachen >60% aller kraftstoffbedingten Bootsbrände
- Typisches Szenario: Schlauch altert an Anschlussstelle, tropft auf heißen Auspuffkrümmer → Sofortentzündung

**Diesel:**
- Flammpunkt: >55°C (EN 590) — deutlich sicherer als Benzin unter Normalbedingungen
- Explosionsbereich: 0,6–6,5 Vol.-% in Luft (deutlich schwerer zu erreichen)
- Diesel entzündet sich nicht durch Funken bei Raumtemperatur
- ABER: Diesel auf heißen Motorteilen (Turbolader: >500°C, Auspuffkrümmer: >400°C) verdampft und entzündet sich
- Diesel-Leckagen verursachen primär Verschmutzung, Bilgenkontamination und langfristige Geruchsbelastung
- Sekundärrisiko: Umwelthaftung — Dieselaustritt in Marina = Bußgelder bis 50.000 EUR

**Statistiken und Schadensdaten:**

| Quelle | Zeitraum | Kraftstoffbrände gesamt | Davon Schlauchversagen | Anteil |
|--------|----------|------------------------|----------------------|--------|
| BoatUS Marine Insurance | 2015–2023 | 2.847 | 683 | 24,0% |
| USCG Boating Accident Reports | 2018–2023 | 1.956 | 489 | 25,0% |
| BSH Deutschland (geschätzt) | 2018–2023 | 312 | 78 | 25,0% |
| Pantaenius Yachtversicherung | 2016–2022 | 487 | 122 | 25,1% |

Die durchschnittliche Schadensumme bei einem kraftstoffbedingten Bootsbrand beträgt laut BoatUS 28.400 USD (ca. 26.200 EUR). Totalverluste machen 34% dieser Fälle aus.

### 1.2 Häufigkeit von Kraftstoff-Leckagen in der Praxis

**Typische Versagensmuster nach Schlauchtyp:**

| Versagensmuster | Häufigkeit | Typisches Alter | Folge |
|----------------|-----------|-----------------|-------|
| Rissbildung an Schlauchenden (Schelle) | 35% | 8–12 Jahre | Tropfleck, langsamer Austritt |
| Innere Delamination (Barrier-Schicht) | 20% | 10–15 Jahre | Kraftstoff permeiert durch Wand |
| Verhärtung/Versprödung (UV/Wärme) | 18% | 6–10 Jahre | Bruch bei Vibration |
| Schlauch rutscht von Anschluss | 12% | beliebig | Plötzlicher Austritt |
| Knick/Abrieb an Scheuerstelle | 10% | 3–8 Jahre | Lochfraß, Austritt |
| Ethanol-Quellung (E10/E15) | 5% | 2–5 Jahre | Dimensionsänderung, undichte Schellen |

**Risikofaktoren:**
- Benzin-Systeme: 3,2× höheres Brandrisiko als Diesel-Systeme
- Schläuche >10 Jahre: 5,8× höhere Versagensrate als Schläuche <5 Jahre
- Nicht-zertifizierte Schläuche: 12,4× höhere Versagensrate als ISO 7840 Type A1
- Maschinenraum-Temperatur >60°C: 2,1× schnellere Alterung
- Ethanol-haltige Kraftstoffe (E10): 1,8× schnellere Innenschicht-Degradation bei Nicht-E10-Schläuchen

### 1.3 Regulatorische Anforderungen (USCG, ISO, ABYC, CE)

Das regulatorische Umfeld für marine Kraftstoffschläuche ist komplex und regional unterschiedlich. Die folgende Übersicht zeigt die relevanten Normen, ihren Geltungsbereich und ihre praktische Bedeutung.

**Normenhierarchie — Übersicht:**

```
┌─────────────────────────────────────────────────┐
│  EU: CE-Kennzeichnung (2013/53/EU)              │
│  → verweist auf ISO 7840, ISO 8469, ISO 9094    │
├─────────────────────────────────────────────────┤
│  USA: USCG 33 CFR 183 Subpart J                 │
│  → verweist auf SAE J1527, UL 1114              │
├─────────────────────────────────────────────────┤
│  ABYC (freiwillig, aber Standard in USA):        │
│  H-24 (Benzin), H-33 (Diesel)                   │
├─────────────────────────────────────────────────┤
│  Internationale Standards:                       │
│  ISO 7840, ISO 8469, ISO 9094                    │
├─────────────────────────────────────────────────┤
│  Klassifikationsgesellschaften (ab 24m):         │
│  Lloyd's, DNV, BV, RINA → eigene Anforderungen  │
└─────────────────────────────────────────────────┘
```

**Detaillierte Normen-Übersicht:**

| Norm | Titel | Geltungsbereich | Kerninhalt |
|------|-------|-----------------|------------|
| ISO 7840:2021 | Small craft — Fire-resistant fuel hoses | EU/International, 2,5–24m | Brandprüfung 2,5 min (150 s), Typ A1/A2/B1/B2 |
| ISO 8469:2021 | Small craft — Non-fire-resistant fuel hoses | EU/International, 2,5–24m | Nur wo kein Brandrisiko besteht (geschützte Bereiche) |
| ISO 9094:2015 | Small craft — Fire protection | EU/International | Brandschutzkonzept, Materialanforderungen, Flucht |
| ABYC H-24 | Gasoline Fuel Systems | USA (freiwillig) | Komplettes Benzin-Kraftstoffsystem inkl. Schläuche |
| ABYC H-33 | Diesel Fuel Systems | USA (freiwillig) | Komplettes Diesel-Kraftstoffsystem inkl. Schläuche |
| SAE J1527 | Marine Fuel Hoses | USA | Schlauchkonstruktion, Materialien, Prüfverfahren |
| SAE J2006 | Marine Exhaust Hose (Abgasschlauch) | USA | Nasse Abgasanlage — NICHT Kraftstoff; Kraftstoff-Fill/Vent fällt unter SAE J1527 |
| USCG 33 CFR 183 Subpart J | Fuel Systems | USA (Pflicht) | Gesetzliche Mindestanforderungen für US-Boote |
| UL 1114 | Marine Supplementary Equipment | USA | UL-Listing für marine Kraftstoffkomponenten |
| SOLAS Reg. II-2 | Fire Safety | International >24m/500 GT | Brandschutz auf Handelsschiffen, relevant ab Superyacht |
| CE 2013/53/EU | Recreational Craft Directive | EU | CE-Kennzeichnung, verweist auf harmonisierte ISO-Normen |
| EN 13765 | Thermoplastic multi-layer hoses | EU | Thermoplastische Mehrschichtschläuche für Kraftstoff |

> ✅ Aufgelöst (Audit): SAE J2006 = "Marine Exhaust Hose" (Abgasschlauch); marine Kraftstoffschläuche inkl. Fill/Vent fallen unter SAE J1527 (USCG Type A2/B2). Falsche J2006-Normnummern (hier, Abschn. 7.8, Hersteller-Tabellen Trident 365, Shields, Novaflex 3760) auf SAE J1527 korrigiert; J2006-Zeile auf ihre korrekte Bedeutung (Abgasschlauch) gesetzt. **Confidence: documented.** Quelle: SAE International J2006 "Marine Exhaust Hose" (sae.org/standards/j2006-marine-exhaust-hose); SAE J1527 "Marine Fuel Hose".

**Regionale Anwendung:**

- **EU-Gewässer:** ISO 7840 Typ A oder B je nach Einbauort (Pflicht für CE). ISO 8469 nur in geschützten Bereichen erlaubt.
- **US-Gewässer:** USCG 33 CFR 183 Subpart J (Pflicht). Schläuche müssen USCG Type A oder Type B sein. ABYC H-24/H-33 als Best Practice.
- **Australien:** AS 1532.1 (weitgehend identisch mit ISO 7840).
- **Internationale Fahrt:** ISO 7840 Type A1 empfohlen — erfüllt alle regionalen Anforderungen.

### 1.4 ISO 7840 Klassifizierung im Detail (A1/A2/B1/B2)

ISO 7840:2021 "Small craft — Fire-resistant fuel hoses" definiert vier Typen, die sich durch Brandwiderstandsdauer und Druckbelastung während des Brands unterscheiden. Dies ist DIE zentrale Norm für marine Kraftstoffschläuche.

**Die vier ISO 7840 Typen:**

| Merkmal | Type A1 | Type A2 | Type B1 | Type B2 |
|---------|---------|---------|---------|---------|
| **Feuerbeständig (2,5-min-Feuertest)** | Ja (2,5 min / 150 s) | Ja (2,5 min / 150 s) | Nein (kein Feuertest) | Nein (kein Feuertest) |
| **Permeationsklasse (ISO 7840)** | Klasse 1 | Klasse 2 | Klasse 1 | Klasse 2 |
| **Flammentemperatur Prüfung** | 650–750°C | 650–750°C | n/a (kein Test) | n/a (kein Test) |
| **Typischer Einsatz** | Druckseite Motor | Rücklauf, Entlüftung | über Deck / nicht feuerexponiert | über Deck, Rücklauf/Vent |
| **Permeationsrate max.** | 100 g/m²/24h | 300 g/m²/24h | 100 g/m²/24h | 300 g/m²/24h |
| **Berstdruck min.** | 20,7 bar (300 psi) | 6,9 bar (100 psi) | 20,7 bar (300 psi) | 6,9 bar (100 psi) |
| **Betriebsdruck max.** | 3,4 bar (50 psi) | 0,34 bar (5 psi) | 3,4 bar (50 psi) | 0,34 bar (5 psi) |
| **Vakuumfestigkeit** | -0,53 bar | -0,53 bar | -0,53 bar | -0,53 bar |
| **CE-konform** | Ja | Ja | Ja | Ja |
| **USCG-Äquivalent** | Type A | Type A | Type B | Type B |
| **Kosten-Faktor** | 1,0× (Referenz) | 0,85× | 0,65× | 0,55× |

> ✅ Aufgelöst (Audit): ISO-7840-Brandtest dauert 2,5 min (150 s) — einen 30-Minuten-Test gibt es in ISO 7840 nicht. "A" = feuerbeständig (besteht Brandtest), "B" = nicht feuerbeständig (KEIN Brandtest); "1"/"2" = Permeationsklasse (Klasse 1 ≤100 g/m²/24h, Klasse 2 ≤300 g/m²/24h), NICHT der Prüfdruck. Tabelle sowie abhängige Abschnitte (1.3, 1.4-Prüfverfahren, 7.3, Pydantic-Enums) korrigiert. **Confidence: documented.** Quelle: ISO 7840:2021; SAE J1527:2022 / USCG 33 CFR 183.538 (Type A1/A2/B1/B2: A = fire test, 1/2 = permeation class 100/300 g/m²/24h).

**Prüfverfahren ISO 7840 Brandtest — Detailbeschreibung:**

1. **Probenvorbereitung:** 1000 mm Schlauchlänge, an beiden Enden verschlossen
2. **Nur Typ A (A1/A2):** Schlauch wird mit Prüfflüssigkeit (ISO-Testfluid C = 50% Iso-Oktan + 50% Toluol) gefüllt und dem Brandtest unterzogen. Typ B (B1/B2) ist nicht feuerbeständig und durchläuft KEINEN Brandtest.
3. **Klassen 1 vs. 2:** Unterscheiden sich NICHT im Brandtest, sondern in der zulässigen Permeationsrate — Klasse 1 ≤100 g/m²/24h, Klasse 2 ≤300 g/m²/24h.
4. **Brandquelle:** Kalibrierte Brenner unter dem Schlauch, freie Brennerlänge 500 mm
5. **Flammentemperatur:** 650–750°C, gemessen 25 mm unter Schlauch
6. **Prüfdauer:** 2,5 Minuten (150 s) — nur Typ A (feuerbeständig)
7. **Bestanden wenn:** Kein Kraftstoffaustritt, keine Leckage, Schlauch behält strukturelle Integrität
8. **Nachprüfung:** Nach Abkühlung Dichtigkeitsprüfung bei 0,34 bar für 5 Minuten

**USCG-Äquivalenz:**
- USCG Type A ≈ ISO 7840 Type A1/A2 (feuerbeständig, 2,5-min-Feuertest bestanden)
- USCG Type B ≈ ISO 7840 Type B1/B2 (nicht feuerbeständig, kein Brandtest)
- USCG 33 CFR 183.540: "Fuel hoses in engine spaces must be Type A" (Benzin)
- USCG erlaubt Type B nur außerhalb des Maschinenraums und nur bei Diesel

**Wo welcher Typ eingesetzt werden muss (nach ISO 7840 + ABYC H-24/H-33):**

| Einbauort | Benzin | Diesel |
|-----------|--------|--------|
| Im Maschinenraum — Druckseite | Type A1 (Pflicht) | Type A1 (empfohlen), B1 (erlaubt) |
| Im Maschinenraum — Rücklauf | Type A2 (Pflicht) | Type A2 (empfohlen), B2 (erlaubt) |
| Im Maschinenraum — Einfüll | Type A2 (Pflicht) | Type A2 (empfohlen) |
| Außerhalb Maschinenraum | Type B1/B2 (erlaubt) | Type B1/B2 (erlaubt) |
| Tankraum (geschlossen) | Type A1/A2 (Pflicht) | Type A2 (empfohlen) |
| Deck/Außen | ISO 8469 (erlaubt) | ISO 8469 (erlaubt) |
| Fill-Schlauch (Deck→Tank) | Type A2 (empfohlen) | Type B2 (erlaubt) |
| Vent-Schlauch (Tank→Außen) | Type A2 (Pflicht) | Type B2 (erlaubt) |

**Markierungen auf ISO 7840-konformen Schläuchen:**

Jeder konforme Schlauch muss folgende Informationen in dauerhafter Prägung oder Druckschrift tragen (alle 300 mm wiederholt):

```
Beispiel: "ISO 7840 A1 — TRIDENT 327/5161 — 8mm ID — USCG TYPE A — SAE J1527 — E85 COMPATIBLE — 2024-Q3"
```

Pflichtangaben:
- Norm (ISO 7840) und Typ (A1/A2/B1/B2)
- Herstellername oder -code
- Produktnummer/Serie
- Innendurchmesser in mm oder inch
- USCG Type (A oder B) falls USCG-zertifiziert
- Herstellungsdatum (Quartal/Jahr)
- Kraftstoffkompatibilität (Diesel, Gasoline, E10, E85, Biodiesel etc.)

---

## 2. Zukunftstechnologien & Neue Materialien

### 2.1 Emerging Materials (2024–2030 Outlook)

**Fluorpolymer-Barriereschichten der nächsten Generation:**

Die größte Innovation im Bereich marine Kraftstoffschläuche betrifft die innere Barriereschicht. Traditionell wird Nitrilkautschuk (NBR) oder Chloropren (CR) als Innenschicht verwendet. Neue Entwicklungen setzen auf:

- **THV (Tetrafluorethylen-Hexafluorpropylen-Vinylidenfluorid):** 3M/Dyneon THV 220 als Innenschicht. Permeationsrate <1 g/m²/24h (100× besser als NBR). Chemisch inert gegenüber allen Kraftstoffarten inkl. Methanol, Ethanol, Biodiesel. Kosten: +40% gegenüber Standard-NBR-Schlauch.

- **PVDF (Polyvinylidenfluorid):** Arkema Kynar als semi-kristalline Barriere. Exzellente Beständigkeit gegen aromatische Kohlenwasserstoffe. Temperaturbereich: -40°C bis +150°C. Kosten: +30% gegenüber Standard.

- **PA12 (Polyamid 12) Multilayer:** Evonik VESTAMID als Innenschicht in thermoplastischen Multilayer-Konstruktionen. Bereits Standard in Automotive (VW, BMW). Marine-Adaption durch Continental/ContiTech ab 2025 angekündigt.

**Faserverstärkte Elastomere:**

- Aramid-Faser (Kevlar) verstärkte Schläuche: Parker Stratoflex 193 Series. 2× höherer Berstdruck bei 30% weniger Wandstärke. Biegeradius 40% kleiner als konventionell. Ideal für enge Maschinenräume.

- Carbon-Nano-Tube (CNT) verstärkte Elastomere: Forschungsstadium (Fraunhofer IWM). Antistatische Eigenschaften eliminieren elektrostatische Aufladung. Erwartete Marktreife: 2028–2030.

**Selbstheilende Schlauchsysteme:**

- Mikroverkapselte Reparaturharze in der Schlauchwand: Konzept von Autonomic Materials Inc. Bei Rissbildung platzen Mikrokapseln und verschließen den Riss temporär. Aktuell nur Proof-of-Concept, keine marine Zertifizierung.

### 2.2 Alternative Kraftstoffe (HVO, Methanol, LNG) — Schlauch-Anforderungen

Die marine Industrie bewegt sich zunehmend zu alternativen Kraftstoffen. Jeder Kraftstoff stellt spezifische Anforderungen an das Schlauchmaterial:

**HVO (Hydrotreated Vegetable Oil) / GTL (Gas-to-Liquid):**

| Parameter | Anforderung | Kompatibilität mit Standard-Schläuchen |
|-----------|-------------|---------------------------------------|
| Chemische Zusammensetzung | Paraffinische Kohlenwasserstoffe, kein FAME | Vollständig kompatibel mit allen ISO 7840-Schläuchen |
| Dichtungsquellung | Geringer als Diesel EN 590 | Kein Problem — eher geringere Belastung |
| Kältebeständigkeit | Cloud Point typisch -25°C bis -30°C | Keine zusätzlichen Anforderungen |
| Preis-Impact | Kein Schlauchtausch nötig | 0 EUR Zusatzkosten |
| Verfügbarkeit | Neste MY, Shell GTL — zunehmend | Standardschläuche ausreichend |

**Methanol (CH₃OH):**

| Parameter | Anforderung | Kompatibilität mit Standard-Schläuchen |
|-----------|-------------|---------------------------------------|
| Chemische Aggressivität | Greift NBR, CR, und Standard-Elastomere an | NICHT kompatibel — FKM/Viton oder PTFE erforderlich |
| Toxizität | Giftig bei Hautkontakt und Inhalation | Verschärfte Dichtungsanforderungen |
| Flammpunkt | 11°C — zwischen Benzin und Diesel | Type A1 im Maschinenraum Pflicht |
| Unsichtbare Flamme | Methanol brennt nahezu unsichtbar | Detektion erfordert spezielle Sensoren |
| Schlauchtyp | FKM-Innenschicht oder PTFE-Liner | Kosten ca. 3× Standard-Diesel-Schlauch |
| Normlage | Keine spezifische ISO-Norm für marine Methanol-Schläuche (Stand 2026) | Individuelle Zulassung erforderlich |

**LNG/CNG (verflüssigtes/komprimiertes Erdgas):**

| Parameter | Anforderung |
|-----------|-------------|
| Betriebsdruck LNG | 3–8 bar (kryogen, -162°C) |
| Betriebsdruck CNG | 200–250 bar |
| Schlauchanforderung | Keine konventionellen Schläuche — nur Metallrohre/Edelstahl-Wellschläuche |
| Relevante Norm | IGF Code (IMO), ISO 20519 |
| Verfügbarkeit marine | Nur für Schiffe >500 GT, nicht für Yachten <24m relevant |

**Ammoniak (NH₃) — Zukunft ab 2030:**
- Hochgradig korrosiv gegenüber Kupfer, Messing, Zink
- Erfordert Edelstahl 316L oder Inconel-Leitungen
- Kein flexibler Schlauch möglich — nur starre Systeme
- Für Yachtbau mittelfristig nicht relevant

### 2.3 Digitale Monitoring-Systeme (Leck-Erkennung)

**Aktuelle Systeme auf dem Markt:**

| System | Hersteller | Messprinzip | Preis (EUR) | Eignung |
|--------|-----------|-------------|-------------|---------|
| Xintex S-2A | Fireboy-Xintex | Halbleiter-Gassensor | 320–480 | Benzin-Dampf-Erkennung |
| BEP 600-GDL | BEP Marine | Katalytischer Sensor | 280–420 | Benzin/LPG |
| NMEA 2000 Fuel Flow | Maretron FFM100 | Ultraschall-Durchfluss | 580–720 | Diesel-Leckmengenüberwachung |
| SmartPlug FuelGuard | SmartPlug Systems | Leitfähigkeitsmessung | 420–600 | Bilgen-Kontamination |
| Sirea FuelSafe Pro | Sirea Marine | Multi-Sensor (Gas + Feuchtigkeit) | 890–1.200 | Integriertes System für >15m Yachten |

**Sensor-Platzierung (Best Practice):**

```
Benzin-System:
┌──────────────────────────────────────┐
│  Maschinenraum                       │
│  ┌──────────┐   Sensor 1: Bilge     │
│  │  Motor   │   (tiefster Punkt)    │
│  │          │                        │
│  │  ●Sensor2│   Sensor 2: Motorblock│
│  │          │   (Schlauch-Bereich)   │
│  └──────────┘                        │
│  ●Sensor 1                          │
│                                      │
│  Sensor 3: Tankraum (falls separat) │
│  Sensor 4: Ventilation Auslass      │
└──────────────────────────────────────┘
```

**Zukünftige Entwicklungen:**

- **Eingebettete Sensoren in Schlauchwand:** Forschung bei Continental/ContiTech — piezoelektrische Fasern in der Gewebeeinlage detektieren Druckänderungen und Mikroleckagen. Prototyp-Stadium (2026).
- **Schlauch-Gesundheitsüberwachung via Kapazitätsmessung:** Änderung der dielektrischen Eigenschaften zeigt Materialermüdung vor dem Versagen an. Patent Parker Hannifin (US Patent 11,421,845 B2).
- **NMEA 2000 / Signal K Integration:** Alle modernen Sensoren senden über NMEA 2000 oder WiFi. AYDI-Integration über SignalK-Gateway möglich.

### 2.4 Nachhaltigkeit & Recycling

**Lebenszyklus-Betrachtung:**

| Phase | Standard-NBR-Schlauch | Premium-FKM-Schlauch |
|-------|----------------------|---------------------|
| Herstellungs-CO₂ | 4,2 kg CO₂/m | 6,8 kg CO₂/m |
| Lebensdauer | 8–10 Jahre | 12–15 Jahre |
| CO₂ pro Nutzungsjahr | 0,47 kg/m/Jahr | 0,49 kg/m/Jahr |
| Recycling-Fähigkeit | Thermisch (Verbrennung) | Thermisch (Verbrennung) |
| Deponiefähigkeit | Nein (Sondermüll) | Nein (Sondermüll) |

**Entsorgung:**
- Kraftstoffschläuche sind als kraftstoffkontaminierte Abfälle zu behandeln
- Abfallschlüssel (AVV): 16 01 14* (Kraftstoff-kontaminiert)
- Entsorgung über zertifizierte Sondermüll-Entsorger oder Wertstoffhöfe mit Gefahrgut-Annahme
- Kosten: ca. 2–5 EUR/kg Entsorgungsgebühr
- Manche Hersteller (Trident, Continental) bieten Rücknahme-Programme an

---

## 3. Best Practices nach Revier & Klimazone

### 3.1 Nördliche Gewässer (Skandinavien, Ostsee, Nordsee, Island, Schottland)

**Klimabedingungen:**
- Wintertemperaturen: -25°C bis -5°C (Maschinenraum kann bei aufgelegtem Boot auf -20°C fallen)
- Sommertemperaturen: 10°C bis 25°C
- Feuchtigkeit: 70–95% RH, häufig Kondenswasser
- UV-Belastung: moderat (Mitternachtssonne im Sommer = lange UV-Exposition trotz niedrigem Winkel)

**Spezifische Empfehlungen:**

| Aspekt | Empfehlung | Begründung |
|--------|-----------|-------------|
| Material Innenschicht | NBR oder FKM | Kältebeständigkeit bis -40°C erforderlich |
| Material Außenschicht | CPE oder CSM (Hypalon) | UV- und ozonbeständig |
| Kälteschutz | Winterlagerung mit leerem Tank oder Arctic-Diesel | Diesel geliert bei <-10°C → Schlauchdruck |
| Kondenswasser | Wasserabscheider pflicht | Dieselpest bei häufigem Temperaturwechsel |
| Inspektionsintervall | 12 Monate (jährliche Saison-Vorbereitung) | Frost-Tau-Zyklen beschleunigen Alterung |
| Ethanol-Kraftstoff | E10 ist Standard in Skandinavien → E10-kompatible Schläuche Pflicht | Schweden: E10 seit 2011, Finnland: E10 seit 2011 |
| Schlauchschellen | Edelstahl 316L (A4) | Korrosion durch Salzwasser + Frost |
| Ersatz-Intervall | 8 Jahre (Dieselschlauch), 6 Jahre (Benzinschlauch) | Frost-Alterung verkürzt Lebensdauer |

### 3.2 Westeuropa (Ärmelkanal, Biskaya, Atlantikküste, Irische See)

**Klimabedingungen:**
- Wintertemperaturen: 0°C bis 10°C (selten unter -5°C)
- Sommertemperaturen: 15°C bis 30°C
- Feuchtigkeit: 70–90% RH, hoher Salzgehalt in der Luft
- UV-Belastung: moderat

**Spezifische Empfehlungen:**

| Aspekt | Empfehlung | Begründung |
|--------|-----------|-------------|
| Material | Standard NBR/CPE | Milde Temperaturen, keine Extremanforderungen |
| Salzluft-Schutz | Schellen und Anschlüsse in Edelstahl 316L | Hoher Salzgehalt in der Luft |
| Feuchtigkeit | Gute Maschinenraum-Belüftung | Kondenswasser führt zu Dieselpest |
| Ethanol | UK: E10 seit 2021, Frankreich: E10 seit 2017 | E10-kompatible Schläuche verwenden |
| Inspektionsintervall | 12 Monate | Winterlager-Check obligatorisch |
| Ersatz-Intervall | 10 Jahre (Diesel), 7 Jahre (Benzin) | Moderate Bedingungen |

### 3.3 Mittelmeer (Adria, Ägäis, Tyrrhenisches Meer, Balearen)

**Klimabedingungen:**
- Wintertemperaturen: 5°C bis 15°C
- Sommertemperaturen: 25°C bis 42°C (Maschinenraum: bis 75°C!)
- Feuchtigkeit: 40–75% RH
- UV-Belastung: SEHR HOCH (2.500–3.000 Sonnenstunden/Jahr)

**Spezifische Empfehlungen:**

| Aspekt | Empfehlung | Begründung |
|--------|-----------|-------------|
| Material Innenschicht | FKM/Viton bevorzugt | Hitzebeständigkeit >100°C im Maschinenraum |
| Material Außenschicht | CSM (Hypalon) oder EPDM mit UV-Additiven | Extreme UV-Belastung |
| Hitzeschutz | Hitzeschutzband (Thermo-Tec, DEI) an Schläuchen nahe Auspuff | Maschinenraum-Temperaturen >65°C |
| Kraftstoff-Qualität | Wasserabscheider + Feinfilter (2µm) zwingend | Kraftstoff-Qualität variiert stark (Griechenland, Türkei) |
| Inspektionsintervall | 6 Monate | Beschleunigte Alterung durch Hitze + UV |
| Ersatz-Intervall | 7 Jahre (Diesel), 5 Jahre (Benzin) | Hitze verkürzt Lebensdauer erheblich |
| Biodiesel | B7 ist EU-Standard (EN 590) — alle modernen Schläuche kompatibel | Keine Sondermaßnahmen |
| Kraftstoff-Additive | Biozid (Grotamar 82) im Diesel-Tank | Dieselpest (Mikroorganismen) bei >25°C Wassertemperatur |

### 3.4 Tropen (Karibik, Pazifik, Südostasien, Indischer Ozean)

**Klimabedingungen:**
- Ganzjahrestemperaturen: 25°C bis 38°C
- Maschinenraum: bis 80°C bei Volllast
- Feuchtigkeit: 80–100% RH, permanent
- UV-Belastung: EXTREM (bis 3.500 Sonnenstunden/Jahr)
- Biologische Belastung: Schimmel, Algen, Insekten in Kraftstoffsystemen

**Spezifische Empfehlungen:**

| Aspekt | Empfehlung | Begründung |
|--------|-----------|-------------|
| Material | FKM/Viton Innenschicht, CSM Außenschicht PFLICHT | Permanente Hitze + UV + Feuchtigkeit |
| Schlauchtyp | ISO 7840 Type A1 für ALLE Einsatzorte | Langfahrt-Sicherheit — kein Zugang zu Ersatzteilen |
| Dieselpest | Biozid (Grotamar 82) + Kraftstoffpolierung alle 500h | Mikrobielles Wachstum ist in Tropen unvermeidlich |
| Spares | 2m Ersatzschlauch pro Dimension an Bord | Versorgungslage schlecht (Pazifik, abgelegene Inseln) |
| Schlauchschellen | Doppelte Schellen an jedem Anschluss | Vibration + Expansion durch Hitze |
| Filter | Racor 500FG oder 900MA mit 2µm Einsatz | Kraftstoff-Qualität oft katastrophal |
| Inspektionsintervall | 3 Monate | Beschleunigte Alterung, schwierige Ersatzteil-Lage |
| Ersatz-Intervall | 5 Jahre (Diesel), 4 Jahre (Benzin) | Extreme Bedingungen |
| Tank-Belüftung | Aktivkohlefilter am Vent-Auslass | Insekten/Sand im Vent-Schlauch |

---

## 4. Regional Sourcing: Verfügbarkeit & Lieferketten weltweit

### 4.1 Nordamerika (USA, Kanada)

**Verfügbarkeit: AUSGEZEICHNET — Beste Versorgungslage weltweit**

| Lieferant | Standorte | Sortiment | Lieferzeit |
|-----------|----------|-----------|-----------|
| West Marine | >240 Filialen USA + Online | Trident, Shields, Parker | 1–3 Tage |
| Defender Industries | Waterford, CT + Online | Trident, Shields, Gates | 1–2 Tage |
| Hamilton Marine | Searsport, ME | Regional, gutes Sortiment | 2–4 Tage |
| Fisheries Supply | Seattle, WA | Trident, Shields, Parker | 1–3 Tage |
| Jamestown Distributors | Bristol, RI + Online | Trident, Gates | 2–4 Tage |
| Amazon USA | Online | Alle Marken, Vorsicht Fälschungen | 1–2 Tage (Prime) |
| Grainger | >250 Filialen USA | Industrieschläuche, Parker, Gates | Same-Day möglich |

**Besonderheiten USA:**
- USCG-Zertifizierung ist Pflicht — Schläuche ohne USCG Type A/B sind illegal
- Alle großen Hersteller (Trident, Shields, Gates) haben US-Lager
- Ethanol: E10 ist Standard, E15 zunehmend — nur E10/E15-kompatible Schläuche kaufen
- Preise: 15–25% günstiger als in Europa (größerer Markt, mehr Wettbewerb)

### 4.2 Europa (Nordeuropa, Großbritannien)

**Verfügbarkeit: GUT — Große Händlernetze, aber weniger Auswahl als USA**

| Lieferant | Land | Sortiment | Lieferzeit |
|-----------|------|-----------|-----------|
| SVB (Yachtausrüster) | DE (Bremen) + Online | Vetus, Continental, Trident | 2–5 Tage |
| Compass24 | DE (Hamburg) + Online | Vetus, diverse | 2–5 Tage |
| AWN | DE (Berlin) + Online | Vetus, Trident | 3–7 Tage |
| Toplicht | DE (Hamburg) | Vetus, Trident | 2–5 Tage |
| Force4 Chandlery | UK, >20 Filialen | Shields, Vetus | 1–3 Tage |
| Allspar | NL (Amsterdam) | Vetus (Firmensitz NL) | 1–3 Tage |
| Accastillage Diffusion | FR, >45 Filialen | Vetus, Continental | 1–5 Tage |
| Jimmy Green Marine | UK (Devon) + Online | Shields, Trident | 2–4 Tage |

**Besonderheiten Europa:**
- Vetus ist Marktführer in Europa (Firmensitz Schiedam, NL)
- Trident Marine importiert aus USA, höherer Preis (+20–30% gegenüber US-Preis)
- Continental/ContiTech Marine-Schläuche gut verfügbar (Produktion in DE)
- ISO 7840-Konformität ist Pflicht für CE-gekennzeichnete Boote

### 4.3 Mittelmeer & Südeuropa

**Verfügbarkeit: BEFRIEDIGEND — Marken-Sortiment eingeschränkt, lokale Alternativen**

| Lieferant | Land | Sortiment | Lieferzeit |
|-----------|------|-----------|-----------|
| Nautimarket | IT (Genua) | Vetus, Osculati-Eigenmarke | 3–7 Tage |
| Osculati | IT (Segrate) + Online | Eigenmarke (ISO 7840 konform) | 2–5 Tage |
| Plastimo (Filiale) | FR (La Rochelle) | Plastimo-Eigenmarke | 2–5 Tage |
| Lalizas | GR (Piräus) | Lalizas-Eigenmarke | 3–10 Tage |
| Martí (Puerto Portals) | ES (Mallorca) | Vetus, diverse | 3–7 Tage |
| Nova Argonautica | ES (Alicante) + Online | Diverse, gute Online-Auswahl | 3–7 Tage |
| Turk Marine | TR (Istanbul, Bodrum) | Vetus, lokale Produkte | 5–14 Tage |

**Besonderheiten Mittelmeer:**
- Osculati (Italien) bietet gutes Preis-Leistungs-Verhältnis, ISO 7840-konform
- In Griechenland und Türkei: Vorsicht bei lokalen No-Name-Schläuchen — häufig KEINE ISO-Zertifizierung
- Tipp: Bei Langfahrt 2m Ersatzschlauch pro Dimension mitnehmen
- Hochsaison (Juni–September): Lieferzeiten verlängern sich auf 7–14 Tage

### 4.4 Karibik

**Verfügbarkeit: EINGESCHRÄNKT — Auf Hauptinseln gut, abseits davon problematisch**

| Standort | Versorgung | Beste Quelle |
|----------|-----------|--------------|
| US Virgin Islands (St. Thomas) | Gut | Budget Marine, Island Marine Supply |
| British Virgin Islands (Tortola) | Befriedigend | Nanny Cay Chandlery, Parts & Power |
| Martinique/Guadeloupe | Befriedigend | Caraïbes Marine, Accastillage Diffusion |
| Trinidad (Chaguaramas) | Gut | Peake Yacht Services, Marc One Marine |
| Sint Maarten | Befriedigend | Budget Marine (Flagship), Island Water World |
| Grenada | Eingeschränkt | Island Dreams, Turbulence Sails |
| Bahamas (Nassau) | Befriedigend | Lightbourne Marine |
| Panama (Shelter Bay) | Eingeschränkt | Shelter Bay Marine, Amazon US Versand |

**Besonderheiten Karibik:**
- Budget Marine (Kette mit 12 Standorten in der Karibik) ist der zuverlässigste Lieferant
- US-Marken (Trident, Shields) sind über USVI/Puerto Rico ohne Import-Zoll beziehbar
- Preise: 30–60% über US-Niveau (Import, Transport, kleine Stückzahlen)
- Empfehlung: Kraftstoffschläuche vor Atlantiküberquerung in Europa oder USA auf Vorrat kaufen

### 4.5 Pazifik

**Verfügbarkeit: SCHLECHT — Nur in größeren Häfen, lange Lieferzeiten**

| Standort | Versorgung | Anmerkung |
|----------|-----------|-----------|
| Neuseeland (Auckland, Whangarei) | Gut | Burnsco, Lusty & Blundell |
| Australien (Sydney, Brisbane) | Gut | Whitworths, BLA |
| Fiji (Denarau, Lautoka) | Eingeschränkt | Yacht Help Fiji, Copra Shed Marina |
| Tonga (Neiafu) | Schlecht | Praktisch kein Marinebedarf |
| Französisch-Polynesien (Papeete) | Eingeschränkt | Sin Tung Hing (Eisenwarenladen mit Marinebedarf) |
| Hawaii (Honolulu) | Gut | West Marine, Fisheries Supply |

**Empfehlung für Pazifik-Durchquerung:**
- Minimum 3m Ersatzschlauch pro verwendetem Durchmesser
- Kompletter Satz Schlauchschellen in Edelstahl 316L
- 2 Stück Racor-Filtereinsätze als Reserve
- Vor Abfahrt aus NZ/AU komplettes Kraftstoffsystem prüfen und ggf. erneuern

### 4.6 Asien

**Verfügbarkeit: REGIONAL SEHR UNTERSCHIEDLICH**

| Standort | Versorgung | Anmerkung |
|----------|-----------|-----------|
| Singapur | Ausgezeichnet | Marine-Hub, alle Marken verfügbar |
| Thailand (Phuket) | Gut | Boat Lagoon Chandlery, Rolly Tasker |
| Malaysia (Langkawi) | Befriedigend | Royal Langkawi Yacht Club, AB Marine |
| Indonesien (Bali) | Eingeschränkt | PT. Enggang Marina, Import über Singapur |
| Philippinen (Subic Bay) | Eingeschränkt | Subic Bay Yacht Club, Import über Manila |
| Japan (Yokohama) | Gut | Yamaha-Händlernetz, Yanmar-Händlernetz |
| Hongkong | Gut | Aberdeen Marina, Simpson Marine Supply |

### 4.7 Australien & Neuseeland

**Verfügbarkeit: GUT — Eigene Markt-Ökosysteme**

| Lieferant | Land | Sortiment | Lieferzeit |
|-----------|------|-----------|-----------|
| Whitworths Marine & Leisure | AU (50+ Filialen) | Trident, Shields, BLA-Eigenmarke | 1–3 Tage |
| BLA (Boat Lifestyle Australia) | AU (Großhandel) | US-Importe, Trident, Gates | 2–5 Tage |
| Bias Boating | AU (5 Filialen, QLD) | Trident, Shields | 1–3 Tage |
| Burnsco | NZ (20+ Filialen) | Trident, Vetus, BEP | 1–3 Tage |
| Lusty & Blundell | NZ (Auckland) | Vollsortiment marine | 2–5 Tage |

**Besonderheiten AU/NZ:**
- Australischer Standard AS 1532.1 (nahezu identisch mit ISO 7840)
- Preise: 20–40% über US-Niveau (Import + GST)
- Ethanol: E10 Standard in AU — E10-kompatible Schläuche verwenden
- Gute Ausgangsbasis für Pazifik-Durchquerung: Schläuche hier bevorraten

### 4.8 Logistik-Planung für Langfahrt

**Empfohlene Ersatzteil-Bevorratung nach Fahrtgebiet:**

| Komponente | Küstensegler | Mittelmeer-Rundfahrt | Atlantik-Runde | Weltumsegelung |
|-----------|-------------|---------------------|----------------|----------------|
| Kraftstoffschlauch (je Dimension) | 0,5m | 1m | 2m | 3m |
| Schlauchschellen (Edelstahl 316L) | 4 Stk | 8 Stk | 16 Stk | 24 Stk |
| Racor-Filtereinsätze | 2 Stk | 4 Stk | 8 Stk | 12 Stk |
| Schlauchverbinder (gerade) | 1 Stk/Dim. | 2 Stk/Dim. | 3 Stk/Dim. | 4 Stk/Dim. |
| Schlauchverbinder (90°) | 0 | 1 Stk/Dim. | 2 Stk/Dim. | 3 Stk/Dim. |
| Anti-Siphon-Ventil | 0 | 1 Stk | 1 Stk | 2 Stk |
| Biozid (Grotamar 82) | 0 | 250 ml | 500 ml | 1.000 ml |
| Kraftstoff-Testkit | 0 | 0 | 1 Kit | 2 Kits |

**Bezugsquellen-Hierarchie für Langfahrer:**
1. Online-Bestellung an nächste Marina mit Postadresse (Amazon, West Marine, SVB)
2. Lokale Chandlery am Ankunftsort
3. Allgemeiner Industriebedarf (Hydraulik-Schlauchbau-Firmen, z.B. Pirtek, Hydac)
4. Auto-Zubehör (NICHT empfohlen — Automotive-Schläuche haben keine Marine-Zertifizierung)

---

## 5. Zweck dieser Wissensdatei

Diese Wissensdatei dient als vollständige Referenz für das AYDI-System zur Bewertung, Diagnose und Empfehlung von Kraftstoffschläuchen auf Yachten. Sie wird von folgenden AYDI-Modulen referenziert:

- **Materials Module:** Identifikation von Schlauchmaterial, Alterungszustand, Kompatibilität
- **Compliance Module:** Überprüfung der ISO 7840/8469-Konformität, CE-Anforderungen
- **Safety Module:** Bewertung von Brandrisiken durch Kraftstoffschläuche
- **Service Patterns Module:** Erkennung von typischen Wartungsmustern und Versagenszeitpunkten
- **Cost Module:** Kalkulation von Austauschkosten nach Bootsklasse und Motor
- **Visual Pipeline B:** Erkennung von Schlauchzuständen auf Fotos (Risse, Verfärbungen, Quellung)

**Confidence-Mapping dieser Datei:**

| Datenquelle | Confidence Level | Anteil |
|-------------|-----------------|--------|
| Hersteller-TDS und -Kataloge | measured | 40% |
| ISO/ABYC/USCG-Normen (Originaltexte) | measured | 20% |
| Hersteller-Empfehlungen, Forum-Konsens | documented | 25% |
| Eigner-Erfahrungen, Schätzungen | estimated | 15% |

---

## 6. Pydantic-Modelle für AYDI-Integration

```python
"""
AYDI Pydantic v2 Models — Kraftstoffschläuche (Diesel/Benzin)
Module: 06_04_kraftstoffschlaeuche
"""

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class FuelType(str, Enum):
    """Kraftstoffart."""
    DIESEL = "diesel"
    GASOLINE = "gasoline"
    BIODIESEL_B5 = "biodiesel_b5"
    BIODIESEL_B20 = "biodiesel_b20"
    BIODIESEL_B100 = "biodiesel_b100"
    ETHANOL_E10 = "ethanol_e10"
    ETHANOL_E15 = "ethanol_e15"
    ETHANOL_E85 = "ethanol_e85"
    HVO = "hvo"
    METHANOL = "methanol"


class FireRating(str, Enum):
    """ISO 7840 Brandklassifikation."""
    A1 = "ISO_7840_A1"  # feuerbeständig (2,5-min-Feuertest), Permeationsklasse 1 (<=100 g/m²/24h)
    A2 = "ISO_7840_A2"  # feuerbeständig (2,5-min-Feuertest), Permeationsklasse 2 (<=300 g/m²/24h)
    B1 = "ISO_7840_B1"  # nicht feuerbeständig, Permeationsklasse 1 (<=100 g/m²/24h)
    B2 = "ISO_7840_B2"  # nicht feuerbeständig, Permeationsklasse 2 (<=300 g/m²/24h)
    ISO_8469 = "ISO_8469"  # Nicht feuerbeständig
    NONE = "none"  # Keine Zertifizierung


class USCGType(str, Enum):
    """USCG-Klassifikation."""
    TYPE_A = "USCG_Type_A"  # feuerbeständig (2,5-min-Feuertest, ISO 7840 A)
    TYPE_B = "USCG_Type_B"  # nicht feuerbeständig (kein Brandtest, ISO 7840 B)
    NONE = "none"  # Nicht USCG-zertifiziert


class HoseFunction(str, Enum):
    """Schlauchfunktion im Kraftstoffsystem."""
    FUEL_SUPPLY = "fuel_supply"  # Tankzuleitung → Motor (Druckseite)
    FUEL_RETURN = "fuel_return"  # Motor → Tank (Rücklauf)
    FUEL_FILL = "fuel_fill"  # Deck-Einfüllstutzen → Tank
    FUEL_VENT = "fuel_vent"  # Tank → Außenbords (Entlüftung)
    FUEL_TRANSFER = "fuel_transfer"  # Tank → Tank
    FUEL_POLISHING = "fuel_polishing"  # Polieranlage Zu-/Ablauf
    FUEL_FILTER_CONNECTION = "fuel_filter_connection"  # Filter-Verbindungen


class InnerLineMaterial(str, Enum):
    """Material der Innenschicht."""
    NBR = "nbr"  # Nitrilkautschuk — Standard
    FKM = "fkm"  # Fluorkautschuk (Viton) — Premium
    CPE = "cpe"  # Chloriertes Polyethylen
    CR = "cr"  # Chloropren (Neopren)
    PTFE = "ptfe"  # Polytetrafluorethylen (Teflon)
    PA12 = "pa12"  # Polyamid 12 — Barrier Layer
    NYLON_BARRIER = "nylon_barrier"  # Nylon-Barriereschicht
    THV = "thv"  # Fluorpolymer-Terpolymer


class OuterCoverMaterial(str, Enum):
    """Material der Außenschicht."""
    CPE = "cpe"  # Chloriertes Polyethylen — Standard marine
    CSM = "csm"  # Chlorsulfoniertes Polyethylen (Hypalon)
    EPDM = "epdm"  # Ethylen-Propylen-Dien — UV-beständig
    CR = "cr"  # Chloropren (Neopren)
    TPE = "tpe"  # Thermoplastisches Elastomer
    STAINLESS_BRAID = "stainless_braid"  # Edelstahl-Geflecht


class ReinforcementType(str, Enum):
    """Verstärkungstyp."""
    TEXTILE_BRAID = "textile_braid"  # Textilgeflecht (Polyester/Nylon)
    TEXTILE_SPIRAL = "textile_spiral"  # Textilspirale
    WIRE_BRAID = "wire_braid"  # Drahtgeflecht
    ARAMID_BRAID = "aramid_braid"  # Aramid-Geflecht (Kevlar)
    DUAL_TEXTILE = "dual_textile"  # Doppeltes Textilgeflecht


class ConditionRating(str, Enum):
    """Zustandsbewertung."""
    NEW = "new"  # Neu, unbenutzt
    EXCELLENT = "excellent"  # Wie neu, keine Alterungszeichen
    GOOD = "good"  # Leichte Alterung, voll funktionsfähig
    FAIR = "fair"  # Deutliche Alterung, noch funktionsfähig
    POOR = "poor"  # Starke Alterung, Austausch empfohlen
    CRITICAL = "critical"  # Sicherheitsrisiko, sofortiger Austausch
    FAILED = "failed"  # Versagt, nicht mehr funktionsfähig


class InstallationLocation(str, Enum):
    """Einbauort."""
    ENGINE_ROOM = "engine_room"  # Maschinenraum
    FUEL_TANK_COMPARTMENT = "fuel_tank_compartment"  # Tankraum
    DECK_AREA = "deck_area"  # Deckbereich
    BILGE = "bilge"  # Bilge
    COCKPIT_LOCKER = "cockpit_locker"  # Cockpit-Staukasten
    LAZARETTE = "lazarette"  # Lazarette


class FuelHoseSpec(BaseModel):
    """Technische Spezifikation eines Kraftstoffschlauchs.

    Vollständige technische Beschreibung eines marine Kraftstoffschlauchs
    mit allen relevanten Parametern für Identifikation, Kompatibilität
    und Zertifizierung.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    manufacturer: str = Field(..., description="Herstellername")
    product_line: str = Field(..., description="Produktlinie/Serie")
    part_number: str = Field(..., description="Artikelnummer des Herstellers")
    description_de: str = Field(..., description="Deutsche Produktbeschreibung")

    # Dimensionen (alle in mm)
    inner_diameter_mm: float = Field(..., ge=4.0, le=102.0, description="Innendurchmesser in mm")
    outer_diameter_mm: float = Field(..., ge=8.0, le=130.0, description="Außendurchmesser in mm")
    wall_thickness_mm: float = Field(..., ge=2.0, le=20.0, description="Wandstärke in mm")
    min_bend_radius_mm: float = Field(..., ge=20.0, le=600.0, description="Minimaler Biegeradius in mm")
    weight_per_meter_g: float = Field(..., ge=50.0, le=5000.0, description="Gewicht pro Meter in Gramm")

    # Druckdaten (alle in bar)
    max_working_pressure_bar: float = Field(..., ge=0.2, le=50.0, description="Max. Betriebsdruck in bar")
    burst_pressure_bar: float = Field(..., ge=1.0, le=200.0, description="Berstdruck in bar")
    vacuum_rating_bar: float = Field(
        ..., ge=-1.0, le=0.0,
        description="Vakuumfestigkeit in bar (negativer Wert)"
    )

    # Temperaturdaten
    temp_min_c: float = Field(..., ge=-60.0, le=0.0, description="Min. Einsatztemperatur in °C")
    temp_max_c: float = Field(..., ge=60.0, le=250.0, description="Max. Einsatztemperatur in °C")
    temp_continuous_c: float = Field(
        ..., ge=40.0, le=200.0,
        description="Max. Dauertemperatur in °C"
    )

    # Materialien
    inner_material: InnerLineMaterial = Field(..., description="Material der Innenschicht")
    outer_material: OuterCoverMaterial = Field(..., description="Material der Außenschicht")
    reinforcement: ReinforcementType = Field(..., description="Verstärkungstyp")

    # Zertifizierungen
    fire_rating: FireRating = Field(..., description="ISO 7840 Brandklasse")
    uscg_type: USCGType = Field(default=USCGType.NONE, description="USCG-Klassifikation")
    sae_j1527: bool = Field(default=False, description="SAE J1527 konform")
    sae_j2006: bool = Field(default=False, description="SAE J2006 (Marine Exhaust Hose) konform — nur Abgasschlauch; Kraftstoff-Fill/Vent siehe sae_j1527")
    ce_compliant: bool = Field(default=False, description="CE-konform (2013/53/EU)")
    ul_listed: bool = Field(default=False, description="UL 1114 gelistet")

    # Kompatibilität
    fuel_types: list[FuelType] = Field(
        ..., min_length=1,
        description="Kompatible Kraftstoffarten"
    )
    hose_functions: list[HoseFunction] = Field(
        ..., min_length=1,
        description="Geeignete Schlauchfunktionen"
    )
    ethanol_compatible: bool = Field(..., description="E10/E15 kompatibel")
    biodiesel_compatible: bool = Field(..., description="Biodiesel (B5/B20) kompatibel")

    # Permeation
    permeation_rate_g_m2_24h: Optional[float] = Field(
        default=None, ge=0.0, le=500.0,
        description="Permeationsrate in g/m²/24h (ISO 7840 max. 100)"
    )

    # Lebensdauer
    expected_lifetime_years: int = Field(
        ..., ge=1, le=25,
        description="Erwartete Lebensdauer in Jahren"
    )

    # Preis
    price_per_meter_eur: float = Field(
        ..., ge=1.0, le=500.0,
        description="Preis pro Meter in EUR (UVP)"
    )
    price_source: str = Field(
        default="Hersteller-Katalog 2025/2026",
        description="Preisquelle und Datum"
    )

    # Verfügbarkeit
    available_lengths_m: list[float] = Field(
        default_factory=lambda: [1.0, 1.5, 3.0, 7.5, 15.0],
        description="Verfügbare Längen als Meterware/Rollen"
    )
    available_diameters_mm: list[float] = Field(
        default_factory=list,
        description="In dieser Serie verfügbare Innendurchmesser in mm"
    )


class FuelHoseCondition(BaseModel):
    """Zustandsbewertung eines eingebauten Kraftstoffschlauchs.

    Wird sowohl von der strukturierten Analyse (Pipeline A) als auch
    von der visuellen Analyse (Pipeline B) befüllt.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    hose_id: str = Field(..., description="Eindeutige AYDI-interne ID")
    location: InstallationLocation = Field(..., description="Einbauort")
    function: HoseFunction = Field(..., description="Funktion im System")
    fuel_type: FuelType = Field(..., description="Kraftstoffart im Schlauch")

    # Aktueller Zustand
    condition_rating: ConditionRating = Field(..., description="Gesamtzustandsbewertung")
    condition_score: int = Field(
        ..., ge=0, le=100,
        description="Zustandspunktzahl 0–100"
    )

    # Alter und Identifikation
    installation_date: Optional[date] = Field(
        default=None, description="Einbaudatum (falls bekannt)"
    )
    manufacture_date: Optional[str] = Field(
        default=None, description="Herstellungsdatum auf Schlauch (z.B. '2019-Q3')"
    )
    age_years: Optional[float] = Field(
        default=None, ge=0.0, le=50.0,
        description="Alter in Jahren (berechnet oder geschätzt)"
    )
    identified_manufacturer: Optional[str] = Field(
        default=None, description="Erkannter Hersteller"
    )
    identified_type: Optional[str] = Field(
        default=None, description="Erkannter Schlauchtyp"
    )
    fire_rating_identified: Optional[FireRating] = Field(
        default=None, description="Erkannte Brandklasse"
    )

    # Befunde — Äußere Schicht
    outer_cracking: bool = Field(default=False, description="Rissbildung Außenschicht")
    outer_cracking_severity: int = Field(
        default=0, ge=0, le=100,
        description="Schwere der Rissbildung (0=keine, 100=durchgehend)"
    )
    outer_discoloration: bool = Field(
        default=False, description="Verfärbung Außenschicht"
    )
    outer_swelling: bool = Field(default=False, description="Quellung Außenschicht")
    outer_abrasion: bool = Field(default=False, description="Abrieb/Scheuerstellen")
    outer_hardening: bool = Field(
        default=False, description="Verhärtung (Verlust der Elastizität)"
    )
    uv_damage: bool = Field(default=False, description="UV-Schäden sichtbar")

    # Befunde — Anschlüsse
    clamp_condition: int = Field(
        default=100, ge=0, le=100,
        description="Zustand der Schlauchschellen (0=versagt, 100=neuwertig)"
    )
    clamp_type: Optional[str] = Field(
        default=None, description="Typ der Schlauchschelle (z.B. 'Edelstahl-Schneckengewinde')"
    )
    connection_leak: bool = Field(
        default=False, description="Leckage an Anschlussstelle festgestellt"
    )
    connection_leak_rate: Optional[str] = Field(
        default=None, description="Leckrate (z.B. 'Tropfleck', 'aktiv tropfend', 'spritzend')"
    )

    # Befunde — Verlauf
    routing_kink: bool = Field(default=False, description="Knick im Schlauchverlauf")
    routing_contact_hot: bool = Field(
        default=False, description="Kontakt mit heißen Teilen (Auspuff, Turbo)"
    )
    routing_chafe: bool = Field(
        default=False, description="Scheuerstelle durch Kontakt mit Struktur"
    )
    routing_unsupported_length_mm: Optional[float] = Field(
        default=None, ge=0.0, le=5000.0,
        description="Ungestützte Schlauchlänge in mm (max. empfohlen: 600mm)"
    )
    heat_shield_present: bool = Field(
        default=False, description="Hitzeschild/Hitzeschutzband vorhanden"
    )

    # Befunde — Innerer Zustand (nur bei Demontage/Endoskopie)
    inner_delamination: Optional[bool] = Field(
        default=None, description="Innere Delamination (falls inspiziert)"
    )
    inner_deposit: Optional[bool] = Field(
        default=None, description="Ablagerungen innen (falls inspiziert)"
    )
    inner_swelling: Optional[bool] = Field(
        default=None, description="Innere Quellung (falls inspiziert)"
    )
    fuel_discoloration: Optional[bool] = Field(
        default=None, description="Kraftstoff-Verfärbung durch Schlauch-Auflösung"
    )

    # Compliance
    fire_rating_compliant: Optional[bool] = Field(
        default=None,
        description="Brandklasse entspricht Einbauort-Anforderung"
    )
    compliance_finding: Optional[str] = Field(
        default=None,
        description="Compliance-Befund (z.B. 'Type B2 im Maschinenraum — erfordert Type A1')"
    )

    # Empfehlungen
    replacement_urgency: str = Field(
        default="routine",
        description="Dringlichkeit: 'immediate', 'next_haulout', 'next_season', 'routine', 'monitor'"
    )
    replacement_recommendation: Optional[str] = Field(
        default=None,
        description="Empfohlener Ersatzschlauch (Hersteller + Typ)"
    )
    estimated_replacement_cost_eur: Optional[float] = Field(
        default=None, ge=0.0, le=10000.0,
        description="Geschätzte Austauschkosten in EUR (Material + Arbeit)"
    )

    # Confidence
    confidence_level: str = Field(
        ...,
        description="Confidence: 'measured', 'visual_high', 'visual_medium', 'visual_low', 'estimated'"
    )
    confidence_notes: Optional[str] = Field(
        default=None,
        description="Anmerkungen zur Confidence-Bewertung"
    )


class FuelSystemAssessment(BaseModel):
    """Gesamtbewertung des Kraftstoffsystems einer Yacht.

    Fasst alle Einzelbefunde zu einer Gesamtbewertung zusammen.
    """
    model_config = {"from_attributes": True}

    # Boot-Identifikation
    yacht_id: str = Field(..., description="AYDI Yacht-ID")
    boat_class: str = Field(
        ...,
        description="Bootsklasse (z.B. 'production_sail_10m', 'semi_custom_motor_18m')"
    )
    fuel_type_primary: FuelType = Field(..., description="Primärer Kraftstoff")
    fuel_type_secondary: Optional[FuelType] = Field(
        default=None, description="Sekundärer Kraftstoff (z.B. Benzin-Generator)"
    )
    engine_manufacturer: Optional[str] = Field(
        default=None, description="Motorhersteller"
    )
    engine_model: Optional[str] = Field(
        default=None, description="Motormodell"
    )

    # Systemübersicht
    total_hoses_inspected: int = Field(
        ..., ge=0, le=50,
        description="Anzahl inspizierter Schläuche"
    )
    total_hoses_estimated: int = Field(
        default=0, ge=0, le=50,
        description="Anzahl nicht inspizierter, aber geschätzter Schläuche"
    )
    hose_conditions: list[FuelHoseCondition] = Field(
        default_factory=list,
        description="Einzelbewertungen aller Schläuche"
    )

    # Gesamtbewertung
    overall_score: int = Field(
        ..., ge=0, le=100,
        description="Gesamtpunktzahl Kraftstoffsystem 0–100"
    )
    overall_rating: ConditionRating = Field(
        ..., description="Gesamtzustandsbewertung"
    )

    # Sicherheitsbewertung
    fire_risk_score: int = Field(
        ..., ge=0, le=100,
        description="Brandrisiko-Score (0=kein Risiko, 100=akute Gefahr)"
    )
    leak_risk_score: int = Field(
        ..., ge=0, le=100,
        description="Leckage-Risiko-Score (0=kein Risiko, 100=akute Leckage)"
    )
    compliance_score: int = Field(
        ..., ge=0, le=100,
        description="Compliance-Score (100=voll konform, 0=schwere Verstöße)"
    )

    # Befunde
    critical_findings: list[str] = Field(
        default_factory=list,
        description="Kritische Befunde — sofortige Maßnahme erforderlich"
    )
    warning_findings: list[str] = Field(
        default_factory=list,
        description="Warnungen — Maßnahme innerhalb der Saison"
    )
    info_findings: list[str] = Field(
        default_factory=list,
        description="Informationen — zur Kenntnis"
    )

    # Empfehlungen
    recommended_actions: list[str] = Field(
        default_factory=list,
        description="Empfohlene Maßnahmen (priorisiert)"
    )
    estimated_total_cost_eur: Optional[float] = Field(
        default=None, ge=0.0, le=100000.0,
        description="Geschätzte Gesamtkosten für alle empfohlenen Maßnahmen in EUR"
    )
    next_inspection_date: Optional[date] = Field(
        default=None,
        description="Empfohlenes Datum der nächsten Inspektion"
    )

    # Confidence
    overall_confidence: str = Field(
        ...,
        description="Gesamt-Confidence: 'measured', 'visual_high', 'visual_medium', 'estimated'"
    )
    data_completeness_pct: float = Field(
        ..., ge=0.0, le=100.0,
        description="Datenvollständigkeit in Prozent"
    )
```

---

## 7. Grundlagen Kraftstoffschläuche

### 7.1 Kraftstoffsysteme auf Yachten — Übersicht

Ein typisches Yacht-Kraftstoffsystem besteht aus folgenden Komponenten, die durch Schläuche und/oder starre Leitungen verbunden sind:

```
Kraftstoffsystem — Schematische Übersicht:

                    Einfüll-Stutzen (Deck)
                          │
                    ┌─────┴─────┐ Fill-Schlauch (ISO 7840 A2 / SAE J1527)
                    │           │
                    │   TANK    │─────── Vent-Schlauch → Außenbords
                    │           │        (ISO 7840 A2 / SAE J1527)
                    │           │
                    └─────┬─────┘
                          │ Saugleitung (ISO 7840 A1)
                          │
                    ┌─────┴─────┐
                    │ Absperr-  │ (manuell, Notabschaltung)
                    │ Ventil    │
                    └─────┬─────┘
                          │
                    ┌─────┴─────┐
                    │ Anti-     │ (bei Installation unter Wasserlinie)
                    │ Siphon    │
                    └─────┬─────┘
                          │
                    ┌─────┴─────┐
                    │ Vor-      │ Racor 500FG / Separ 2000
                    │ Filter    │ (Wasserabscheider + Grobfilter 30µm)
                    └─────┬─────┘
                          │ Supply-Schlauch (ISO 7840 A1)
                          │
                    ┌─────┴─────┐
                    │ Fein-     │ (Motor-intern, 2–10µm)
                    │ Filter    │
                    └─────┬─────┘
                          │
                    ┌─────┴─────┐
                    │ Einspritz- │
                    │ pumpe     │
                    └─────┬─────┘
                          │ Hochdruckleitung (KEIN Schlauch — starre Leitung!)
                          │
                    ┌─────┴─────┐
                    │ Injektor/ │
                    │ Düsen     │
                    └─────┴─────┘
                          │ Return-Schlauch (ISO 7840 A2)
                          │
                    ┌─────┴─────┐
                    │   TANK    │
                    └───────────┘
```

**Typische Schlauchanzahl nach Bootstyp:**

| Bootstyp | Motor(en) | Anzahl Schläuche | Gesamtlänge (ca.) |
|----------|----------|-----------------|-------------------|
| Segelboot 8–10m, 1× Diesel | 1× Saildrive 10–30 PS | 4–6 | 3–5m |
| Segelboot 12–15m, 1× Diesel | 1× Wellendiesel 30–75 PS | 6–8 | 5–8m |
| Motorboot 8–10m, 1× Benzin I/O | 1× Sterndrive 150–300 PS | 5–7 | 4–7m |
| Motorboot 12–15m, 2× Diesel | 2× Wellendiesel 150–400 PS | 10–14 | 8–15m |
| Motoryacht 18–24m, 2× Diesel | 2× Wellendiesel 400–1000 PS | 14–20 | 15–25m |
| Segelyacht 18–24m, 1× Diesel + Gen | 1× Diesel + Generator | 10–14 | 10–18m |

### 7.2 Diesel vs Benzin — Grundlegende Unterschiede

Die Unterschiede zwischen Diesel- und Benzinsystemen haben fundamentale Auswirkungen auf die Schlauchauswahl:

| Parameter | Diesel (EN 590) | Benzin (EN 228) |
|-----------|----------------|-----------------|
| Flammpunkt | >55°C | ca. -20°C |
| Explosionsgrenzen | 0,6–6,5 Vol.-% | 1,0–7,6 Vol.-% |
| Dampfdruck (20°C) | <0,01 bar | 0,45–0,90 bar (Reid) |
| Zündtemperatur | 220°C | 280°C |
| Dichte (15°C) | 0,820–0,845 g/cm³ | 0,720–0,775 g/cm³ |
| Viskosität (40°C) | 2,0–4,5 mm²/s | 0,5–0,7 mm²/s |
| Schwefelgehalt | <10 ppm (EN 590) | <10 ppm (EN 228) |
| Aromatengehalt | <8% (PAK) | <35% (Gesamtaromaten) |
| Permeationsverhalten | Gering | Hoch (hoher Dampfdruck) |
| Quellung von NBR | Gering–Moderat | Moderat–Hoch |
| Quellung von FKM | Minimal | Minimal |
| Statische Aufladung | Gering | Hoch (Erdung erforderlich!) |

**Konsequenzen für Schlauchanforderungen:**

| Anforderung | Diesel-System | Benzin-System |
|-------------|--------------|---------------|
| Mindest-Brandklasse Maschinenraum | ISO 7840 B1 (Pflicht), A1 (empfohlen) | ISO 7840 A1 (PFLICHT — keine Ausnahme) |
| Permeationsanforderung | Wichtig (Geruch) | KRITISCH (Explosionsgefahr) |
| Bilgenbelüftung | Empfohlen | PFLICHT (33 CFR 183.610) |
| Funkenfreie Lüfter | Empfohlen | PFLICHT |
| Erdung/Masseverbindung | Empfohlen | PFLICHT (antistatisch) |
| Lecksensor | Empfohlen | PFLICHT (ABYC H-24.14) |
| Absperr-Ventil | Pflicht (ISO 9094) | PFLICHT + Notabschaltung vom Steuerstand |
| Anti-Siphon | Pflicht unter WL | PFLICHT unter WL |

### 7.3 ISO 7840 Fire Test — Detaillierte Beschreibung

**Prüfaufbau (nach ISO 7840:2021 Anhang A):**

```
Seitenansicht des Brandprüfstands:

         Thermoelemente (25mm über Schlauch)
              ↓    ↓    ↓    ↓
    ╔═════════════════════════════════╗
    ║  Prüfschlauch (1000mm Länge)   ║ ← Verschlossene Enden
    ╠═════════════════════════════════╣    (Typ A1/B1: gefüllt + unter Druck)
    ║                                 ║
    ║  ~~~~  ~~~~  ~~~~  ~~~~  ~~~~   ║ ← Flammen (Propanbrenner)
    ║  ~~~~  ~~~~  ~~~~  ~~~~  ~~~~   ║
    ╚═════════════════════════════════╝
    │←────── 500mm Brennerlänge ──────→│

         Thermoelemente (25mm unter Schlauch)
              ↓    ↓    ↓    ↓
         Flammentemperatur: 650–750°C
```

**Prüfablauf im Detail:**

1. **Konditionierung:** Prüfschlauch 72h bei 23°C ± 2°C und 50% ± 5% RH lagern.

2. **Befüllung (nur Typ A1/B1):**
   - Prüfflüssigkeit: ISO Testfluid C (50% Iso-Oktan + 50% Toluol)
   - Alternativ: FAM B (EN ISO 1817 Referenzkraftstoff B)
   - Schlauch wird vollständig gefüllt und auf 0,34 bar (5 psi) Innendruck gebracht

3. **Flammenexposition:**
   - Brennertyp: 3 × Propanbrenner, gleichmäßig verteilt über 500mm
   - Flammentemperatur: 650–750°C, gemessen 25mm unterhalb des Schlauchs
   - Prüfung beginnt, wenn Flammentemperatur stabilisiert ist (ca. 2 Minuten Vorlauf)

4. **Beobachtung während Prüfung:**
   - Tropfenbildung auf der Schlauchaußenseite wird notiert (akzeptabel, solange keine durchgehende Leckage)
   - Flammenbildung am Schlauch wird notiert
   - Deformation wird notiert

5. **Bestanden-Kriterien:**
   - Typ A1: 2,5 min (150 s) Feuertest — KEIN Kraftstoffaustritt aus dem Schlauchlumen; Permeationsklasse 1 (≤100 g/m²/24h)
   - Typ A2: 2,5 min (150 s) Feuertest — KEIN Durchschmelzen oder Kollaps; Permeationsklasse 2 (≤300 g/m²/24h)
   - Typ B1: kein Feuertest (nicht feuerbeständig); Permeationsklasse 1 (≤100 g/m²/24h)
   - Typ B2: kein Feuertest (nicht feuerbeständig); Permeationsklasse 2 (≤300 g/m²/24h)

6. **Nachprüfung:**
   - Schlauch abkühlen lassen (30 Minuten)
   - Dichtigkeitsprüfung bei 0,34 bar für 5 Minuten
   - Der Schlauch muss dicht bleiben

**Weitere ISO 7840 Prüfungen (neben Brandtest):**

| Prüfung | Methode | Bestanden-Kriterium |
|---------|---------|---------------------|
| Berstdruck | Hydrostatisch, Drucksteigerung 7 bar/min | A1/B1: ≥20,7 bar; A2/B2: ≥6,9 bar |
| Impulsprüfung | 150.000 Zyklen bei max. Betriebsdruck, 100°C | Keine Leckage, keine Delamination |
| Kälteflexibilität | Biegen um 5× Durchmesser bei -30°C | Keine Risse, keine Brüche |
| Ozonbeständigkeit | 72h bei 40°C, 50 pphm Ozon, 20% Dehnung | Keine Risse sichtbar (10× Lupe) |
| Kraftstoffbeständigkeit | 168h Eintauchen in Testfluid C bei 23°C | Volumenänderung <25%, Zugfestigkeit >80% |
| Permeation | 72h Testfluid C bei 23°C, gravimetrisch | ≤100 g/m²/24h |
| Zugfestigkeit | DIN EN ISO 37, Zugversuch | ≥7 MPa für Innenschicht, ≥5 MPa für Außenschicht |
| UV-Beständigkeit | 300h Xenon-Lampe, DIN EN ISO 4892-2 | Keine Risse, Zugfestigkeit >70% |

### 7.4 Materialien (NBR, FKM/Viton, CPE, Nylon-Barrier)

**Innenschicht-Materialien — Detailübersicht:**

**NBR (Nitrilkautschuk / Acrylnitril-Butadien-Kautschuk):**

| Parameter | Wert |
|-----------|------|
| Handelsname | Perbunan (Lanxess), Nipol (Zeon) |
| Temperaturbereich | -30°C bis +100°C (kurzzeitig +120°C) |
| Beständigkeit Diesel | Gut — Quellung 5–15% Vol. |
| Beständigkeit Benzin | Befriedigend — Quellung 15–30% Vol. |
| Beständigkeit Ethanol (E10) | Befriedigend (hochgesättigte NBR: gut) |
| Beständigkeit Biodiesel | Eingeschränkt — FAME beschleunigt Alterung |
| Permeation (Diesel) | 10–30 g/m²/24h |
| Permeation (Benzin) | 40–100 g/m²/24h |
| Shore A Härte | 55–75 |
| Preis-Faktor | 1,0× (Referenz) |
| Einsatz | Standard-Innenschicht für Diesel-Schläuche |
| Limitierungen | Nicht für aromatische Lösungsmittel, nicht für Biodiesel >B20 |

**FKM/Viton (Fluorkautschuk):**

| Parameter | Wert |
|-----------|------|
| Handelsname | Viton (Chemours/DuPont), Tecnoflon (Solvay), DAI-EL (Daikin) |
| Temperaturbereich | -20°C bis +200°C (kurzzeitig +230°C) |
| Beständigkeit Diesel | Exzellent — Quellung <3% Vol. |
| Beständigkeit Benzin | Exzellent — Quellung <5% Vol. |
| Beständigkeit Ethanol (E85) | Gut (FKM Typ GLT: sehr gut) |
| Beständigkeit Biodiesel (B100) | Exzellent |
| Permeation (Diesel) | 1–5 g/m²/24h |
| Permeation (Benzin) | 5–15 g/m²/24h |
| Shore A Härte | 65–85 |
| Preis-Faktor | 2,5–3,5× gegenüber NBR |
| Einsatz | Premium-Innenschicht für alle Kraftstoffarten |
| Limitierungen | Eingeschränkte Kälteflexibilität (Standard-FKM bis -20°C) |

**CPE (Chloriertes Polyethylen):**

| Parameter | Wert |
|-----------|------|
| Temperaturbereich | -30°C bis +105°C |
| Beständigkeit Diesel | Gut |
| Beständigkeit Benzin | Gut |
| Beständigkeit Ethanol | Befriedigend |
| Permeation (Benzin) | 30–60 g/m²/24h |
| Shore A Härte | 50–70 |
| Preis-Faktor | 1,2× gegenüber NBR |
| Einsatz | Oft als kombinierte Innen-/Außenschicht, USCG-konforme Schläuche |
| Vorteil | Gute Balance aus Beständigkeit, Brandverhalten und Preis |

**Nylon-Barrier (PA12-Barriereschicht):**

| Parameter | Wert |
|-----------|------|
| Typischer Aufbau | NBR-innen → Nylon-Barrier → Textilgeflecht → CPE-außen |
| Temperaturbereich | -30°C bis +100°C |
| Permeation (Benzin) | <5 g/m²/24h (100× besser als NBR allein!) |
| Ethanol-Beständigkeit | Sehr gut |
| Preis-Faktor | 1,5–2,0× gegenüber Standard-NBR |
| Einsatz | Moderne Benzin-Schläuche (Trident 327, Shields 350) |
| Vorteil | Niedrige Permeation bei moderatem Preis |

**Außenschicht-Materialien:**

| Material | Temperatur | UV | Ozon | Abrieb | Flamme | Preis |
|----------|-----------|-----|------|--------|--------|-------|
| CPE | -30/+105°C | Gut | Gut | Gut | Selbstverlöschend | 1,0× |
| CSM (Hypalon) | -30/+120°C | Exzellent | Exzellent | Sehr gut | Selbstverlöschend | 1,8× |
| EPDM | -40/+130°C | Exzellent | Exzellent | Befriedigend | Mäßig | 1,2× |
| CR (Neopren) | -25/+100°C | Gut | Gut | Gut | Selbstverlöschend | 1,1× |
| Edelstahl-Geflecht | -60/+230°C | n/a | n/a | Exzellent | Nicht brennbar | 3,0× |

### 7.5 Markierungen auf Kraftstoffschläuchen — Lesen und Verstehen

Die Markierung auf einem ISO 7840-konformen Schlauch ist die primäre Informationsquelle für die Identifikation. AYDI Visual Pipeline B kann diese Markierungen auf Fotos lesen.

**Dekodierung einer typischen Markierung:**

```
Beispiel Trident:
"TRIDENT 327/5161 — 5/16" (8mm) ID — ISO 7840 A1 — USCG TYPE A — SAE J1527 — E85 — 2024 Q3"
  │       │    │     │              │              │              │            │      │
  │       │    │     │              │              │              │            │      └─ Herstellungsdatum
  │       │    │     │              │              │              │            └─ Ethanol-Kompatibilität
  │       │    │     │              │              │              └─ SAE-Norm
  │       │    │     │              │              └─ USCG-Klassifikation
  │       │    │     │              └─ ISO-Brandklasse
  │       │    │     └─ Innendurchmesser
  │       │    └─ Hersteller-Artikelnummer
  │       └─ Serie
  └─ Hersteller

Beispiel Shields:
"SHIELDS HOSE — SERIES 350 — 3/8" — ISO 7840 TYPE A1 — USCG TYPE A1 — SAE J1527 — E10 COMPATIBLE — MFG 03/2023"

Beispiel Vetus:
"VETUS — FUHOSE16A — 16mm — ISO 7840:2021 TYPE A1 — CE — EN 13765 — 2024"
```

**Warnsignale bei der Markierung:**
- Keine ISO 7840 oder USCG-Angabe → Nicht marine-zertifiziert — SOFORT ersetzen
- Nur ISO 8469 → Nicht feuerbeständig — prüfen, ob Einbauort ISO 8469 erlaubt
- Herstellungsdatum >10 Jahre → Austausch empfohlen
- Markierung unleserlich → Schlauch ist so alt, dass Austausch dringend empfohlen wird
- "Automotive Use Only" / "Not for Marine Use" → SOFORT ersetzen

### 7.6 Ethanol-Kompatibilität (E10/E15/E85)

Ethanol-haltiger Kraftstoff ist in der EU und den USA inzwischen Standard. Dies hat massive Auswirkungen auf die Schlauchauswahl:

**Ethanol-Beimischung nach Region:**

| Region | Standard | Max. Ethanol | Bemerkung |
|--------|---------|-------------|-----------|
| EU (EN 228) | E5/E10 | 10% | E10 seit 2011 empfohlen, seit 2019 Standard |
| Deutschland (DIN 51626-1) | E10 | 10% | Super E10 an >99% der Tankstellen |
| Skandinavien | E10/E85 | 85% | Schweden: E85 weit verbreitet |
| USA | E10/E15 | 15% | E15 seit 2022 ganzjährig zugelassen |
| Brasilien | E27 | 27% | Höchster Standard weltweit |
| Australien | E10 | 10% | E10 Standard seit 2016 |

**Wirkung von Ethanol auf Schlauchmaterialien:**

| Material | E10 | E15 | E85 | Mechanismus |
|----------|-----|-----|-----|-------------|
| NBR (Standard) | Quellung +8–15% | Quellung +15–25% | ZERSETZUNG | Ethanol extrahiert Weichmacher |
| NBR (hochgesättigt, HNBR) | Quellung +3–8% | Quellung +5–12% | Quellung +20–35% | Langsame Weichmacher-Extraktion |
| FKM/Viton (Standard) | Quellung <3% | Quellung <5% | Quellung +5–10% | Minimale Wechselwirkung |
| FKM GLT (kälteflexibel) | Quellung <2% | Quellung <3% | Quellung <5% | Optimiert für polare Lösungsmittel |
| CPE | Quellung +5–10% | Quellung +8–15% | Quellung +15–25% | Moderate Wechselwirkung |
| Nylon-Barrier (PA12) | Keine Quellung | Keine Quellung | Quellung <3% | Exzellente Ethanol-Barriere |
| PTFE | Keine Quellung | Keine Quellung | Keine Quellung | Chemisch inert |

**Praktische Empfehlung:**
- Benzin-Schläuche MÜSSEN mindestens E10-kompatibel sein (Standard seit 2020)
- Für Boote, die weltweit unterwegs sind: E85-kompatible Schläuche wählen (Nylon-Barrier oder FKM)
- Altschläuche (vor 2010) sind NICHT für E10 geeignet → Austausch dringend empfohlen
- Symptome von Ethanol-Schäden: weißliche Verfärbung der Innenschicht, Quellung an Schlauchenden, schwarze Partikel im Kraftstofffilter

### 7.7 Biodiesel-Kompatibilität (B5/B20/B100)

**Biodiesel (FAME — Fatty Acid Methyl Ester) Beimischung:**

| Spezifikation | Max. FAME | Norm | Anmerkung |
|--------------|----------|------|-----------|
| EN 590 Diesel | 7% (B7) | EN 14214 (FAME) | EU-Standard seit 2009 |
| B20 | 20% | ASTM D7467 | USA, verbreitet bei Behördenflotten |
| B100 | 100% | EN 14214, ASTM D6751 | Reiner Biodiesel, selten marine |
| HVO (kein FAME!) | 0% FAME | EN 15940 | Synthetisch, kein Biodiesel |

**Wirkung von Biodiesel auf Schlauchmaterialien:**

| Material | B7 | B20 | B100 | Mechanismus |
|----------|-----|------|------|------------|
| NBR (Standard) | Kompatibel | Grenzwertig — Quellung +10–20% | NICHT KOMPATIBEL | FAME löst Weichmacher, verursacht Quellung und Verhärtung |
| FKM/Viton | Kompatibel | Kompatibel | Kompatibel | Minimale Wechselwirkung |
| CPE | Kompatibel | Grenzwertig | Eingeschränkt | Moderate FAME-Empfindlichkeit |
| Nylon-Barrier | Kompatibel | Kompatibel | Kompatibel | Gute FAME-Barriere |

**Biodiesel-spezifische Probleme:**
- FAME ist hygroskopisch — zieht Wasser an → Dieselpest (mikrobielle Kontamination)
- FAME hat höhere Lösungskraft → löst Ablagerungen in Tanks → verstopfte Filter
- FAME altert schneller → oxidative Polymerisation → Ablagerungen in Schläuchen
- FAME greift Kupfer, Messing, Zink an → Anschlüsse aus Bronze/Edelstahl verwenden

### 7.8 Kraftstoff-Fill/Vent/Supply/Return — Vier Schlauchtypen

**Detaillierte Beschreibung der vier Hauptfunktionen:**

**1. Fill-Schlauch (Einfüllschlauch — Deck → Tank):**

| Parameter | Spezifikation |
|-----------|---------------|
| Funktion | Verbindung zwischen Deck-Einfüllstutzen und Tankstutzen |
| Durchmesser typisch | 38mm (1-1/2") für Diesel, 38mm für Benzin |
| Druckbelastung | Niedrig (Schwerkraft + Zapfpistolendruck) |
| Mindest-Brandklasse | ISO 7840 A2 (empfohlen), B2 (min. Diesel), A2 (Pflicht Benzin) |
| SAE-Norm | SAE J1527 (Marine Fuel Hose; Fill = Type A2/B2) |
| Material typisch | NBR/CPE oder Nylon-Barrier |
| Besonderheit | Muss knickfrei verlegt werden — Kraftstoff fließt per Schwerkraft |
| Häufiger Fehler | Zu enger Biegeradius → Knickt → Tank wird nicht voll |
| Lebensdauer typisch | 12–15 Jahre (geringe Beanspruchung) |
| Preis typisch (38mm) | 25–45 EUR/m |

**2. Vent-Schlauch (Entlüftungsschlauch — Tank → Außenbords):**

| Parameter | Spezifikation |
|-----------|---------------|
| Funktion | Druckausgleich beim Befüllen und bei Temperaturänderungen |
| Durchmesser typisch | 16mm (5/8") |
| Druckbelastung | Minimal (<0,05 bar) |
| Mindest-Brandklasse | ISO 7840 A2 (Benzin — Pflicht!), B2 (Diesel — erlaubt) |
| SAE-Norm | SAE J1527 (Marine Fuel Hose; Vent = Type A2/B2) |
| Besonderheit Benzin | USCG/ABYC: Vent-Schlauch bei Benzin = Type A (Dampf = explosionsfähig!) |
| Besonderheit | Muss mit Flammenschutzsieb am Auslass enden |
| Anti-Spill-Ventil | Am Vent-Auslass empfohlen (verhindert Überlaufen beim Tanken) |
| Häufiger Fehler | Vent verstopft (Insekten, Salzkristalle) → Tankdruck → Leckage |
| Lebensdauer typisch | 10–12 Jahre |
| Preis typisch (16mm) | 12–22 EUR/m |

**3. Supply-Schlauch (Zuleitung — Tank → Motor):**

| Parameter | Spezifikation |
|-----------|---------------|
| Funktion | Kraftstoff-Zuleitung vom Tank (über Filter) zum Motor |
| Durchmesser typisch | 8mm (5/16") bis 12mm (1/2") je nach Motorleistung |
| Druckbelastung | 0,2–3,0 bar (Einspritzpumpen-Saugseite, ggf. Förderpumpe) |
| Mindest-Brandklasse | ISO 7840 A1 (Pflicht im Maschinenraum) |
| Material | FKM/Viton oder Nylon-Barrier (Premium), NBR/CPE (Standard) |
| Besonderheit | Höchste Sicherheitsanforderung — direkt am Motor, heißeste Zone |
| Häufiger Fehler | Schlauch liegt am Auspuffkrümmer → Hitzeschaden → Leckage |
| Lebensdauer typisch | 7–10 Jahre (höchste Belastung) |
| Preis typisch (8mm) | 15–35 EUR/m |

**4. Return-Schlauch (Rücklauf — Motor → Tank):**

| Parameter | Spezifikation |
|-----------|---------------|
| Funktion | Überschüssiger Kraftstoff vom Motor zurück zum Tank |
| Durchmesser typisch | 8mm (5/16") bis 10mm (3/8") |
| Druckbelastung | Niedrig (<0,5 bar) |
| Mindest-Brandklasse | ISO 7840 A2 (Pflicht im Maschinenraum Benzin), B2 (Diesel erlaubt) |
| Material | NBR/CPE (ausreichend), FKM (Premium) |
| Besonderheit | Kraftstoff ist warm (40–80°C) — Hitzebeständigkeit wichtig |
| Häufiger Fehler | Rücklauf und Zulauf verwechselt → Motor bekommt warmen Kraftstoff |
| Lebensdauer typisch | 8–12 Jahre |
| Preis typisch (8mm) | 12–25 EUR/m |

### 7.9 Anti-Siphon und Brandschutz-Ventile

**Anti-Siphon-Ventil:**

Ein Anti-Siphon-Ventil ist PFLICHT, wenn der Tankauslass unter der Wasserlinie liegt (ISO 9094, ABYC H-24/H-33). Ohne dieses Ventil kann bei einem Schlauchbruch Kraftstoff durch Siphon-Effekt unkontrolliert auslaufen.

| Parameter | Spezifikation |
|-----------|---------------|
| Funktion | Verhindert Kraftstofffluss bei Schlauchbruch unter WL |
| Auslösemechanismus | Schwerkraft-Kugel oder Feder-Rückschlagventil |
| Einbauposition | Direkt am Tank-Auslass oder max. 300mm entfernt |
| Material | Bronze (CuSn8) oder Edelstahl 316L |
| Hersteller | Racor (Parker), Vetus, Groco, Perko |
| Preis | 45–120 EUR |
| Wartung | Jährlich prüfen, alle 5 Jahre ersetzen |
| ABYC-Anforderung | H-24.13 (Benzin), H-33.13 (Diesel) |

**Typische Anti-Siphon-Ventile:**

| Produkt | Hersteller | Typ | Anschluss | Material | Preis (EUR) |
|---------|-----------|-----|-----------|----------|-------------|
| Racor FST45 | Parker/Racor | Feder-Rückschlag | 8mm, 10mm, 12mm | Bronze | 55–75 |
| Vetus NLP | Vetus | Schwerkraft-Kugel | 8mm, 10mm, 12mm, 16mm | Bronze | 48–85 |
| Groco FBV Series | Groco | Kugel-Rückschlag | 3/8"–1" NPT | Bronze | 65–110 |
| Perko 0457 | Perko | Feder-Rückschlag | 1/4"–1/2" NPT | Bronze | 45–70 |

**Brandschutz-Absperrventil (Fire-Stop Valve):**

| Parameter | Spezifikation |
|-----------|---------------|
| Funktion | Schließt automatisch bei Brand (Schmelzsicherung) |
| Auslösemechanismus | Schmelzlot (typisch 72°C oder 93°C) |
| Einbauposition | An Maschinenraum-Schott, wo Schlauch in Maschinenraum eintritt |
| Material | Bronze oder Edelstahl 316L |
| Norm | ISO 9094:2015, SOLAS Reg. II-2 |
| Typische Produkte | Fireboy-Xintex MA2-Series, Vetus FUAV-Series |
| Preis | 85–180 EUR |
| Pflicht | Ab 24m bzw. bei Klassifikation (Lloyd's, DNV) |
| Empfehlung | Auch für Yachten <24m dringend empfohlen |

---

## 8. Hersteller — Vollständige Übersicht

### 8.1 Trident Marine (USA)

**Firmenprofil:**
- Sitz: Brea, California, USA
- Gegründet: 1994
- Spezialisierung: Ausschließlich marine Schläuche und Abgassysteme
- Marktposition: Marktführer USA für marine Kraftstoffschläuche
- Zertifizierungen: ISO 7840, USCG, SAE J1527, UL 1114
- Vertrieb Europa: Über Distributoren (SVB, Force4, diverse)

**Produktserien Kraftstoffschläuche:**

**Trident Serie 327 — Type A1 Fuel Line (Premium):**

| Parameter | Wert |
|-----------|------|
| Klassifikation | ISO 7840 Type A1, USCG Type A, SAE J1527 |
| Aufbau | NBR + Nylon-Barrier + 2× Textilgeflecht + CPE |
| Innenschicht | NBR mit Nylon-Barrier (PA12) |
| Außenschicht | CPE, schwarz, UV-beständig |
| Temperatur | -30°C bis +100°C |
| Betriebsdruck | 3,4 bar (50 psi) |
| Berstdruck | 20,7 bar (300 psi) |
| Vakuumfestigkeit | -0,53 bar (15.7 inHg) |
| Permeation | <15 g/m²/24h (weit unter ISO-Maximum von 100) |
| Ethanol | E10, E15, E85 kompatibel |
| Biodiesel | B20 kompatibel |
| Markierung | "TRIDENT 327/XXXX ISO 7840 A1 USCG TYPE A SAE J1527 E85" |
| Lebensdauer | 10–12 Jahre |

**Trident 327 — Dimensionen und Preise:**

| Art.-Nr. | ID (mm) | ID (inch) | OD (mm) | Wandst. (mm) | Bieger. (mm) | Gewicht (g/m) | EUR/m |
|----------|---------|-----------|---------|--------------|-------------|--------------|-------|
| 327-5161 | 8,0 | 5/16" | 14,3 | 3,15 | 50 | 125 | 18,50 |
| 327-3761 | 9,5 | 3/8" | 16,7 | 3,60 | 63 | 160 | 21,00 |
| 327-5001 | 12,7 | 1/2" | 20,6 | 3,95 | 75 | 220 | 26,50 |
| 327-6251 | 15,9 | 5/8" | 23,8 | 3,95 | 100 | 285 | 31,00 |

**Trident Serie 328 — Type A2 Fuel Feed/Return:**

| Parameter | Wert |
|-----------|------|
| Klassifikation | ISO 7840 Type A2, USCG Type A, SAE J1527 |
| Aufbau | NBR + 1× Textilgeflecht + CPE |
| Betriebsdruck | 0,34 bar (5 psi) — Schwerkraft/Niederdruckseite |
| Berstdruck | 6,9 bar (100 psi) |
| Permeation | <30 g/m²/24h |
| Ethanol | E10, E15 kompatibel |
| Einsatz | Rücklauf, Einfüllung, Entlüftung |

**Trident 328 — Dimensionen und Preise:**

| Art.-Nr. | ID (mm) | ID (inch) | OD (mm) | Wandst. (mm) | Bieger. (mm) | EUR/m |
|----------|---------|-----------|---------|--------------|-------------|-------|
| 328-5162 | 8,0 | 5/16" | 13,5 | 2,75 | 45 | 14,50 |
| 328-3762 | 9,5 | 3/8" | 15,9 | 3,20 | 55 | 16,00 |
| 328-5002 | 12,7 | 1/2" | 19,1 | 3,20 | 65 | 19,50 |
| 328-6252 | 15,9 | 5/8" | 22,2 | 3,15 | 85 | 23,00 |

**Trident Serie 329 — Type B1 Fuel Line (Budget):**

| Parameter | Wert |
|-----------|------|
| Klassifikation | ISO 7840 Type B1, USCG Type B, SAE J1527 |
| Feuerbeständigkeit | Nein (Type B — kein Feuertest); nicht für Maschinenraum Benzin! |
| Betriebsdruck | 3,4 bar (50 psi) |
| Einsatz | Diesel-Maschinenraum (erlaubt), außerhalb MR |
| Preis vs 327 | ca. 35% günstiger |

| Art.-Nr. | ID (mm) | OD (mm) | EUR/m |
|----------|---------|---------|-------|
| 329-5163 | 8,0 | 13,5 | 12,00 |
| 329-3763 | 9,5 | 15,9 | 13,50 |
| 329-5003 | 12,7 | 19,1 | 16,50 |

**Trident Serie 330 — Type B2 Fuel Line:**

| Parameter | Wert |
|-----------|------|
| Klassifikation | ISO 7840 Type B2, USCG Type B |
| Betriebsdruck | 0,34 bar (5 psi) |
| Einsatz | Diesel-Rücklauf außerhalb MR, Entlüftung (Diesel) |

| Art.-Nr. | ID (mm) | OD (mm) | EUR/m |
|----------|---------|---------|-------|
| 330-5164 | 8,0 | 13,0 | 9,50 |
| 330-3764 | 9,5 | 15,5 | 10,50 |
| 330-5004 | 12,7 | 18,5 | 13,00 |

**Trident Serie 365 — Type A Fill/Vent Hose (großer Durchmesser):**

| Parameter | Wert |
|-----------|------|
| Klassifikation | ISO 7840 Type A2, USCG Type A, SAE J1527 |
| Einsatz | Einfüll- und Entlüftungsschläuche |

| Art.-Nr. | ID (mm) | ID (inch) | OD (mm) | EUR/m |
|----------|---------|-----------|---------|-------|
| 365-0341 | 19,1 | 3/4" | 28,6 | 28,00 |
| 365-0381 | 25,4 | 1" | 34,9 | 32,00 |
| 365-1121 | 31,8 | 1-1/4" | 41,3 | 38,00 |
| 365-1501 | 38,1 | 1-1/2" | 47,6 | 42,00 |
| 365-2001 | 50,8 | 2" | 61,0 | 52,00 |

### 8.2 Shields Rubber (Parker Hannifin) — USA

**Firmenprofil:**
- Sitz: Cleveland, Ohio, USA (Parker Hannifin Hauptsitz)
- Marke Shields: Seit 1924 marine Schläuche
- 2017 von Parker Hannifin übernommen
- Marktposition: Zweiter nach Trident in USA, stark in OEM-Markt
- Zertifizierungen: ISO 7840, USCG, SAE J1527, UL

**Shields Serie 350 — Type A1 Marine Fuel Line:**

| Parameter | Wert |
|-----------|------|
| Klassifikation | ISO 7840 Type A1, USCG Type A, SAE J1527 |
| Aufbau | NBR + Nylon-Barrier + Textilgeflecht + CPE |
| Innenschicht | Smooth-bore NBR mit integrierter Nylon-Barriere |
| Temperatur | -30°C bis +100°C |
| Betriebsdruck | 3,4 bar (50 psi) |
| Berstdruck | 20,7 bar (300 psi) |
| Permeation | <10 g/m²/24h (branchenbester Wert) |
| Ethanol | E10, E15 kompatibel (E85 auf Anfrage) |
| Besonderheit | "Ultra Low Permeation" — Shields-Patent |
| Lebensdauer | 10–12 Jahre |

**Shields 350 — Dimensionen und Preise:**

| Art.-Nr. | ID (mm) | ID (inch) | OD (mm) | Wandst. (mm) | Bieger. (mm) | EUR/m |
|----------|---------|-----------|---------|--------------|-------------|-------|
| 350-0566 | 8,0 | 5/16" | 14,0 | 3,0 | 50 | 19,50 |
| 350-0586 | 9,5 | 3/8" | 16,5 | 3,5 | 65 | 22,50 |
| 350-0626 | 12,7 | 1/2" | 20,5 | 3,9 | 75 | 27,50 |
| 350-0666 | 15,9 | 5/8" | 23,5 | 3,8 | 100 | 32,50 |

**Shields Serie 355 — Type A2 Fuel Feed:**

| Art.-Nr. | ID (mm) | ID (inch) | OD (mm) | EUR/m |
|----------|---------|-----------|---------|-------|
| 355-0566 | 8,0 | 5/16" | 13,5 | 15,50 |
| 355-0586 | 9,5 | 3/8" | 16,0 | 17,50 |
| 355-0626 | 12,7 | 1/2" | 19,0 | 20,50 |
| 355-0666 | 15,9 | 5/8" | 22,0 | 24,50 |

**Shields Serie 369 — Type A Fill & Vent Hose (großer Durchmesser):**

| Art.-Nr. | ID (mm) | ID (inch) | OD (mm) | EUR/m |
|----------|---------|-----------|---------|-------|
| 369-0346 | 19,1 | 3/4" | 28,0 | 29,00 |
| 369-0386 | 25,4 | 1" | 35,0 | 34,00 |
| 369-1126 | 31,8 | 1-1/4" | 41,0 | 39,00 |
| 369-1506 | 38,1 | 1-1/2" | 47,5 | 44,00 |
| 369-2006 | 50,8 | 2" | 60,5 | 55,00 |

### 8.3 Vetus (Niederlande)

**Firmenprofil:**
- Sitz: Schiedam, Niederlande
- Gegründet: 1951
- Spezialisierung: Vollsortiment marine Ausrüstung, Schläuche als Kernprodukt
- Marktposition: Marktführer Europa, starke Präsenz weltweit
- Zertifizierungen: ISO 7840, CE, EN 13765
- Vertrieb: Eigenes Händlernetz in >60 Ländern

**Vetus FUHOSE-Serie — Kraftstoffschläuche:**

**FUHOSE...A — ISO 7840 Type A1 (Premium):**

| Parameter | Wert |
|-----------|------|
| Klassifikation | ISO 7840 Type A1, CE, EN 13765 |
| Aufbau | NBR + Textilverstärkung (2-lagig) + CSM (Hypalon) |
| Innenschicht | Glatte NBR, kraftstoffbeständig |
| Außenschicht | CSM (Hypalon), exzellente UV-Beständigkeit |
| Temperatur | -30°C bis +100°C |
| Betriebsdruck | 3,4 bar |
| Berstdruck | 21,0 bar |
| Permeation | <50 g/m²/24h |
| Ethanol | E10 kompatibel |
| Farbe Außen | Schwarz |
| Lebensdauer | 10–12 Jahre |

**Vetus FUHOSE...A — Dimensionen und Preise:**

| Art.-Nr. | ID (mm) | OD (mm) | Wandst. (mm) | Bieger. (mm) | Gewicht (g/m) | EUR/m |
|----------|---------|---------|--------------|-------------|--------------|-------|
| FUHOSE08A | 8 | 15 | 3,5 | 55 | 145 | 16,90 |
| FUHOSE10A | 10 | 17 | 3,5 | 65 | 175 | 18,50 |
| FUHOSE12A | 12 | 20 | 4,0 | 75 | 225 | 22,90 |
| FUHOSE16A | 16 | 24 | 4,0 | 100 | 290 | 27,50 |
| FUHOSE19A | 19 | 27 | 4,0 | 115 | 340 | 31,50 |
| FUHOSE25A | 25 | 34 | 4,5 | 150 | 450 | 38,90 |
| FUHOSE32A | 32 | 42 | 5,0 | 190 | 580 | 45,50 |
| FUHOSE38A | 38 | 49 | 5,5 | 230 | 720 | 52,90 |

**FUHOSE...B — ISO 7840 Type B1 (Standard):**

| Art.-Nr. | ID (mm) | OD (mm) | EUR/m |
|----------|---------|---------|-------|
| FUHOSE08B | 8 | 14 | 11,90 |
| FUHOSE10B | 10 | 16 | 13,50 |
| FUHOSE12B | 12 | 18 | 15,90 |
| FUHOSE16B | 16 | 22 | 19,50 |

**Vetus Besonderheit — Farbcodierung:**
- Type A1/A2 Schläuche: Schwarzer Schlauch mit ROTER Markierungsschrift
- Type B1/B2 Schläuche: Schwarzer Schlauch mit BLAUER Markierungsschrift
- Dies erleichtert die visuelle Identifikation (relevant für AYDI Pipeline B)

### 8.4 Gates Corporation (USA)

**Firmenprofil:**
- Sitz: Denver, Colorado, USA
- Gegründet: 1911
- Primärmarkt: Automotive und Industrie, Marine als Nebensegment
- Marine-Produkte: "Marine Fuel Master" Serie
- Zertifizierungen: ISO 7840, USCG, SAE
- Vertrieb: Über industrielle Distributoren (z.B. Grainger, MSC Industrial)

**Gates Marine Fuel Master — Type A1:**

| Parameter | Wert |
|-----------|------|
| Klassifikation | ISO 7840 Type A1, USCG Type A, SAE J1527 |
| Aufbau | NBR + Nylon-Barrier + Aramid-Geflecht + CPE |
| Besonderheit | Aramid-Verstärkung (statt Polyester) — höherer Berstdruck |
| Temperatur | -40°C bis +100°C (beste Kältebeständigkeit der Klasse!) |
| Betriebsdruck | 3,4 bar (50 psi) |
| Berstdruck | 27,6 bar (400 psi) — 33% über ISO-Minimum |
| Permeation | <20 g/m²/24h |
| Ethanol | E10, E15 kompatibel |
| Lebensdauer | 12–15 Jahre (Aramid-Verstärkung altert langsamer) |

**Gates Marine Fuel Master — Dimensionen und Preise:**

| Art.-Nr. | ID (mm) | ID (inch) | OD (mm) | Wandst. (mm) | EUR/m |
|----------|---------|-----------|---------|--------------|-------|
| 27055 | 8,0 | 5/16" | 14,5 | 3,25 | 22,50 |
| 27056 | 9,5 | 3/8" | 17,0 | 3,75 | 25,50 |
| 27057 | 12,7 | 1/2" | 21,0 | 4,15 | 30,50 |
| 27058 | 15,9 | 5/8" | 24,5 | 4,30 | 36,00 |

**Bewertung Gates:**
- Premium-Qualität, beste Kältebeständigkeit (-40°C)
- Ideal für skandinavische Gewässer und Hochsee-Segler
- Nachteil: Geringere Verfügbarkeit im Marinefachhandel (eher Industrievertrieb)
- Preis: 15–20% über Trident/Shields

### 8.5 Continental (ContiTech Marine) — Deutschland

**Firmenprofil:**
- Sitz: Hannover, Deutschland
- Division: ContiTech Fluid Technology
- Primärmarkt: Automotive, Industrie, Marine als spezialisiertes Segment
- Produktion: Deutschland, Tschechien
- Zertifizierungen: ISO 7840, CE, EN 13765, Lloyd's, DNV, BV
- Besonderheit: Einziger Hersteller mit Klassifikations-Zulassungen (Lloyd's, DNV)

**Continental Marine Fuel Hose — Type A1 (Serie MFH-A1):**

| Parameter | Wert |
|-----------|------|
| Klassifikation | ISO 7840 Type A1, CE, EN 13765, Lloyd's, DNV, BV |
| Aufbau | FKM-Innenschicht + 2× Textilgeflecht + CSM-Außenschicht |
| Innenschicht | FKM (Fluorkautschuk) — Premium |
| Außenschicht | CSM (Hypalon), UV-stabilisiert |
| Temperatur | -30°C bis +120°C (höchste Dauertemperatur der Klasse!) |
| Betriebsdruck | 5,0 bar (72 psi) — über ISO-Minimum |
| Berstdruck | 25,0 bar (362 psi) |
| Permeation | <5 g/m²/24h (mit FKM — Bestwert) |
| Ethanol | E10, E15, E85 kompatibel |
| Biodiesel | B100 kompatibel |
| Lebensdauer | 12–15 Jahre |
| Superyacht-tauglich | Ja — Lloyd's/DNV-Zulassung |

**Continental MFH-A1 — Dimensionen und Preise:**

| Art.-Nr. | ID (mm) | OD (mm) | Wandst. (mm) | Bieger. (mm) | EUR/m |
|----------|---------|---------|--------------|-------------|-------|
| MFH-A1-08 | 8 | 16 | 4,0 | 55 | 32,00 |
| MFH-A1-10 | 10 | 18 | 4,0 | 70 | 36,00 |
| MFH-A1-12 | 12 | 21 | 4,5 | 80 | 42,00 |
| MFH-A1-16 | 16 | 25 | 4,5 | 105 | 48,00 |
| MFH-A1-19 | 19 | 29 | 5,0 | 125 | 55,00 |
| MFH-A1-25 | 25 | 36 | 5,5 | 160 | 65,00 |
| MFH-A1-32 | 32 | 44 | 6,0 | 200 | 78,00 |
| MFH-A1-38 | 38 | 51 | 6,5 | 240 | 92,00 |
| MFH-A1-51 | 51 | 65 | 7,0 | 320 | 115,00 |

**Bewertung Continental:**
- Höchste Materialqualität (FKM-Innenschicht als Standard)
- Einziger Hersteller mit Lloyd's/DNV-Zulassung → Pflicht für klassifizierte Yachten >24m
- Höchste Temperaturbeständigkeit (120°C Dauer)
- Nachteil: Preis ca. 50–80% über US-Herstellern
- Verfügbarkeit: Gut in DE/EU, eingeschränkt außerhalb

### 8.6 Goodyear Marine (USA)

**Firmenprofil:**
- Sitz: Akron, Ohio, USA
- Marine-Division: Goodyear Engineered Products (seit 2007 Continental/Veyance Technologies)
- Marktposition: Etabliert, insbesondere in OEM-Erstausrüstung
- Produkte: Goodyear Marine Fuel Line Serie

**Goodyear Marine Fuel Line — Type A1:**

| Parameter | Wert |
|-----------|------|
| Klassifikation | ISO 7840 Type A1, USCG Type A, SAE J1527 |
| Aufbau | NBR + Textilgeflecht + CPE |
| Temperatur | -30°C bis +100°C |
| Betriebsdruck | 3,4 bar |
| Berstdruck | 20,7 bar |
| Permeation | <60 g/m²/24h (höher als Trident/Shields) |
| Ethanol | E10 kompatibel |
| Lebensdauer | 8–10 Jahre |

| Art.-Nr. | ID (mm) | OD (mm) | EUR/m |
|----------|---------|---------|-------|
| GY-MFL-516 | 8,0 | 14,0 | 16,50 |
| GY-MFL-38 | 9,5 | 16,5 | 18,50 |
| GY-MFL-12 | 12,7 | 20,5 | 22,00 |
| GY-MFL-58 | 15,9 | 23,5 | 26,00 |

**Bewertung Goodyear:**
- Solide Qualität, wettbewerbsfähiger Preis
- Höhere Permeationsrate als Trident/Shields → für Benzin weniger ideal
- Gute Verfügbarkeit über Automotive-Vertriebskanäle
- Empfehlung: Eher für Diesel als für Benzin geeignet

### 8.7 Parker (Stratoflex / Push-Lok)

**Firmenprofil:**
- Sitz: Cleveland, Ohio, USA
- Divisionen: Stratoflex (Aerospace/Premium), Push-Lok (Industrie/Marine)
- Parker Hannifin ist weltgrößter Hersteller für Hydraulik und Pneumatik
- Marine-Schläuche: Über Shields-Marke (Parker-Tochter) und Stratoflex-Premium

**Parker Stratoflex 193 — Premium Marine Fuel (AN-Style):**

| Parameter | Wert |
|-----------|------|
| Klassifikation | ISO 7840 Type A1, USCG Type A |
| Aufbau | PTFE-Innenschicht + Edelstahl-Geflecht (304L) |
| Innenschicht | Konvolut-PTFE — absolut chemisch inert |
| Außenschicht | Edelstahl 304L Geflecht + optionaler Schrumpfschlauch |
| Temperatur | -54°C bis +230°C (höchster Bereich aller Schläuche!) |
| Betriebsdruck | 10,3 bar (150 psi) — 3× ISO-Minimum |
| Berstdruck | 41,4 bar (600 psi) — 2× ISO-Minimum |
| Permeation | <1 g/m²/24h (PTFE — Bestwert) |
| Ethanol | E85 kompatibel |
| Biodiesel | B100 kompatibel |
| Methanol | Kompatibel (einziger Schlauch in dieser Liste!) |
| Lebensdauer | 15–20 Jahre |
| Anschlüsse | AN-Fittings (-4AN, -6AN, -8AN, -10AN, -12AN) |

**Parker Stratoflex 193 — Dimensionen und Preise:**

| Art.-Nr. | AN-Size | ID (mm) | OD (mm) | EUR/m | EUR/Fitting |
|----------|---------|---------|---------|-------|-------------|
| 193-4 | -4AN | 5,6 | 10,2 | 38,00 | 22,00 |
| 193-6 | -6AN | 8,7 | 13,5 | 45,00 | 28,00 |
| 193-8 | -8AN | 11,1 | 16,3 | 52,00 | 35,00 |
| 193-10 | -10AN | 14,3 | 19,8 | 62,00 | 42,00 |
| 193-12 | -12AN | 17,5 | 23,1 | 75,00 | 52,00 |

**Parker Push-Lok 801 — Marine Fuel (Universal):**

| Parameter | Wert |
|-----------|------|
| Klassifikation | ISO 7840 Type B1, USCG Type B, SAE J1527 |
| Aufbau | NBR + 1× Textilgeflecht + NBR-Außen |
| Temperatur | -40°C bis +100°C |
| Betriebsdruck | 10,3 bar (150 psi) |
| Berstdruck | 41,4 bar (600 psi) |
| Besonderheit | Push-on-Fittings — kein Werkzeug zum Aufpressen nötig |
| Einsatz | Diesel-System, NICHT für Benzin im Maschinenraum (Type B!) |

| Art.-Nr. | ID (mm) | OD (mm) | EUR/m |
|----------|---------|---------|-------|
| 801-4 | 6,4 | 12,4 | 8,50 |
| 801-6 | 9,5 | 15,7 | 10,00 |
| 801-8 | 12,7 | 19,8 | 12,50 |
| 801-10 | 15,9 | 22,2 | 15,00 |

### 8.8 Aeroquip (Eaton)

**Firmenprofil:**
- Sitz: Maumee, Ohio, USA (Eaton Aerospace)
- Spezialisierung: AN-Fittings und Hochleistungsschläuche (ursprünglich Militär/Luftfahrt)
- Marine-Einsatz: Vor allem im Racing/Performance-Bereich, Motorboote mit Hochleistungsmotoren
- Zertifizierungen: MIL-DTL-6000, MIL-DTL-8794, eingeschränkt ISO 7840

**Aeroquip Startlite 471 — PTFE Fuel Line:**

| Parameter | Wert |
|-----------|------|
| Aufbau | PTFE-Innenschicht + Edelstahl 304 Geflecht |
| Temperatur | -54°C bis +204°C |
| Betriebsdruck | 20,7 bar (3000 psi bei -4AN) |
| Berstdruck | 82,8 bar (12000 psi bei -4AN) |
| Anschlüsse | AN-Fittings (wiederverwendbar, Aluminium oder Edelstahl) |
| Marine-Zertifizierung | Eingeschränkt — nicht alle Größen USCG-zertifiziert |
| Einsatz | Racing-Motorboote, Custom-Hochleistungsinstallationen |

| AN-Size | ID (mm) | OD (mm) | EUR/m | EUR/Fitting (Edelstahl) |
|---------|---------|---------|-------|------------------------|
| -4AN | 5,6 | 10,4 | 28,00 | 32,00 |
| -6AN | 8,7 | 13,7 | 35,00 | 40,00 |
| -8AN | 11,1 | 16,5 | 42,00 | 48,00 |
| -10AN | 14,3 | 20,1 | 52,00 | 58,00 |
| -12AN | 17,5 | 23,3 | 65,00 | 68,00 |

> ⚠️ **ZU PRÜFEN (Audit):** Betriebsdruck "20,7 bar (3000 psi bei -4AN)" und Berstdruck "82,8 bar (12000 psi bei -4AN)" sind in sich widersprüchlich: 20,7 bar = 300 psi (nicht 3000), 82,8 bar = 1200 psi (nicht 12000) — Faktor-10-Abweichung zwischen bar- und psi-Angabe. Die korrekte Richtung ist nicht zweifelsfrei belegbar; reale Aeroquip-StartLite-Werte liegen laut Hersteller zudem bei ca. 24–35 bar / 350–500 psi und passen zu keiner der beiden Spalten. Druckwerte daher **Confidence: estimated — unverifiziert** (nicht "measured").

**Bewertung Aeroquip:**
- Höchste Druckfestigkeit — weit über marine Anforderungen
- Ideal für Hochleistungs-Motorboote und Racing
- PTFE-Innenschicht = universelle Kraftstoffkompatibilität
- Nachteil: Nicht alle Produkte haben ISO 7840-Zertifizierung
- Preis: Premium-Segment, vergleichbar mit Parker Stratoflex

### 8.9 Dayco (USA)

**Firmenprofil:**
- Sitz: Franklin, Tennessee, USA
- Gegründet: 1905
- Primärmarkt: Automotive (Riemen, Schläuche, Fluidleitungen)
- Marine: "Marine Fuel Hose" Serie — Budget-Segment
- Zertifizierungen: USCG Type A, SAE J1527

**Dayco Marine Fuel Hose — Type A1:**

| Parameter | Wert |
|-----------|------|
| Klassifikation | USCG Type A, SAE J1527, ISO 7840 Type A1 |
| Aufbau | NBR + Textilgeflecht + CPE |
| Temperatur | -30°C bis +100°C |
| Betriebsdruck | 3,4 bar |
| Berstdruck | 20,7 bar |
| Permeation | <80 g/m²/24h |
| Ethanol | E10 kompatibel |
| Lebensdauer | 7–9 Jahre |

| Art.-Nr. | ID (mm) | OD (mm) | EUR/m |
|----------|---------|---------|-------|
| 80068 | 8,0 | 14,0 | 14,00 |
| 80069 | 9,5 | 16,5 | 15,50 |
| 80070 | 12,7 | 20,0 | 18,50 |
| 80071 | 15,9 | 23,5 | 22,00 |

**Bewertung Dayco:**
- Preisgünstigstes USCG-zertifiziertes Produkt
- Solide Qualität für Budget-bewusste Eigner
- Höhere Permeation als Trident/Shields — für Diesel akzeptabel, für Benzin grenzwertig
- Verfügbarkeit: Gut über Auto-Zubehör-Kanäle, weniger im Marinefachhandel

### 8.10 Novaflex (USA)

**Firmenprofil:**
- Sitz: Olive Branch, Mississippi, USA
- Gegründet: 1977
- Spezialisierung: Industrie- und Marineschläuche, starke Position bei Fill/Vent-Schläuchen
- Zertifizierungen: USCG, SAE J1527, ISO 7840

**Novaflex 3760 — Marine Fuel Fill/Vent Hose:**

| Parameter | Wert |
|-----------|------|
| Klassifikation | USCG Type A, SAE J1527, ISO 7840 Type A2 |
| Aufbau | NBR + Drahtgeflecht + CPE |
| Besonderheit | Drahtverstärkt — kollabiert nicht unter Vakuum |
| Temperatur | -30°C bis +100°C |
| Betriebsdruck | 3,4 bar |
| Berstdruck | 13,8 bar |
| Einsatz | Fill- und Vent-Schläuche — bevorzugt bei großen Durchmessern |

| Art.-Nr. | ID (mm) | OD (mm) | EUR/m |
|----------|---------|---------|-------|
| 3760-0750 | 19,1 | 28,5 | 26,00 |
| 3760-1000 | 25,4 | 34,5 | 30,00 |
| 3760-1250 | 31,8 | 41,0 | 35,00 |
| 3760-1500 | 38,1 | 48,0 | 42,00 |
| 3760-2000 | 50,8 | 61,0 | 52,00 |

### 8.11 Zusammenfassung OEM vs Aftermarket

**Preisvergleich — 8mm ID Kraftstoffschlauch, ISO 7840 Type A1:**

| Hersteller | Art.-Nr. | Permeation (g/m²/24h) | Temp. max. | Ethanol | EUR/m | Wertung |
|-----------|----------|----------------------|-----------|---------|-------|---------|
| Continental MFH-A1 | MFH-A1-08 | <5 | 120°C | E85 | 32,00 | Premium |
| Parker Stratoflex 193 | 193-6 (8,7mm) | <1 | 230°C | E85+Methanol | 45,00 | Super-Premium |
| Gates Fuel Master | 27055 | <20 | 100°C | E15 | 22,50 | Obere Mittelklasse |
| Shields 350 | 350-0566 | <10 | 100°C | E15 | 19,50 | Obere Mittelklasse |
| Trident 327 | 327-5161 | <15 | 100°C | E85 | 18,50 | Mittelklasse |
| Vetus FUHOSE | FUHOSE08A | <50 | 100°C | E10 | 16,90 | Mittelklasse |
| Goodyear Marine | GY-MFL-516 | <60 | 100°C | E10 | 16,50 | Basis |
| Dayco Marine | 80068 | <80 | 100°C | E10 | 14,00 | Budget |

**Empfehlung nach Anwendung:**

| Anwendung | Empfehlung 1 | Empfehlung 2 | Begründung |
|-----------|-------------|-------------|------------|
| Diesel-Segelboot 8–14m | Vetus FUHOSE-A | Trident 327 | Gutes Preis-Leistung, EU-Verfügbarkeit |
| Diesel-Motoryacht 14–24m | Continental MFH-A1 | Trident 327 | Continental für hohe Maschinenraum-Temps |
| Benzin-Motorboot | Trident 327 (E85) | Shields 350 (Ultra Low Perm) | Niedrige Permeation = Sicherheit |
| Superyacht >24m (klassifiziert) | Continental MFH-A1 | Parker Stratoflex 193 | Lloyd's/DNV-Zulassung erforderlich |
| Racing/Performance | Parker Stratoflex 193 | Aeroquip 471 | PTFE, höchste Druckfestigkeit |
| Langfahrt/Weltumsegelung | Trident 327 (E85) | Continental MFH-A1 | Globale Ersatzteil-Verfügbarkeit |
| Budget (Diesel only) | Dayco 80068 | Goodyear GY-MFL | Preiswert, ISO-konform, für Diesel ausreichend |

---

## 9. Motorspezifische Zuordnung

### 9.1 Volvo Penta (D1/D2/D3/D4/D6)

**Volvo Penta Diesel-Motoren — Schlauch-Spezifikationen:**

| Motor | Leistung | Supply ID (mm) | Return ID (mm) | Fill ID (mm) | OEM-Schlauch |
|-------|---------|----------------|----------------|-------------|-------------|
| D1-13 | 12,2 PS | 8 | 8 | 38 | VP 3588267 |
| D1-20 | 18,8 PS | 8 | 8 | 38 | VP 3588267 |
| D1-30 | 28 PS | 8 | 8 | 38 | VP 3588267 |
| D2-40 | 39 PS | 8 | 8 | 38 | VP 3588267 |
| D2-55 | 55 PS | 10 | 8 | 38 | VP 3588268 |
| D2-60 | 60 PS | 10 | 8 | 38 | VP 3588268 |
| D2-75 | 75 PS | 10 | 8 | 38 | VP 3588268 |
| D3-110 | 110 PS | 10 | 10 | 38 | VP 3589063 |
| D3-150 | 150 PS | 10 | 10 | 38 | VP 3589063 |
| D3-170 | 170 PS | 10 | 10 | 38 | VP 3589063 |
| D3-220 | 220 PS | 12 | 10 | 38 | VP 3589064 |
| D4-180 | 180 PS | 12 | 10 | 38 | VP 21354808 |
| D4-210 | 210 PS | 12 | 10 | 38 | VP 21354808 |
| D4-260 | 260 PS | 12 | 10 | 38 | VP 21354808 |
| D4-300 | 300 PS | 12 | 10 | 38 | VP 21354808 |
| D6-280 | 280 PS | 12 | 12 | 51 | VP 21135367 |
| D6-310 | 310 PS | 12 | 12 | 51 | VP 21135367 |
| D6-340 | 340 PS | 12 | 12 | 51 | VP 21135367 |
| D6-370 | 370 PS | 16 | 12 | 51 | VP 21135368 |
| D6-400 | 400 PS | 16 | 12 | 51 | VP 21135368 |
| D6-435 | 435 PS | 16 | 12 | 51 | VP 21135368 |

**Volvo Penta OEM-Schlauchpreise vs. Aftermarket:**

| OEM-Teil | Funktion | Länge | OEM-Preis (EUR) | Aftermarket-Äquivalent | AM-Preis (EUR) | Ersparnis |
|----------|---------|-------|----------------|----------------------|---------------|----------|
| VP 3588267 | Supply D1/D2 | 1,0m vorkonfektioniert | 85 | Trident 327-5161, 8mm, 1m | 18,50 + 8 (Schellen) | 69% |
| VP 3588268 | Supply D2/D3 | 1,0m vorkonfektioniert | 95 | Trident 327-3761, 10mm, 1m | 21,00 + 8 | 69% |
| VP 21354808 | Supply D4 | 1,5m vorkonfektioniert | 145 | Continental MFH-A1-12, 1,5m | 63,00 + 12 | 48% |
| VP 21135367 | Supply D6 | 1,5m vorkonfektioniert | 165 | Continental MFH-A1-12, 1,5m | 63,00 + 12 | 55% |

**Volvo Penta Einbau-Besonderheiten:**
- D1/D2: Kompakte Einbauräume auf Segelbooten — kurze Schlauchlängen, enge Biegeradien
- D3: Oft Common-Rail → konstanter Rücklaufdruck → Rücklaufschlauch muss druckfest sein
- D4/D6: Common-Rail mit hohem Rücklaufdruck (bis 3 bar) → Supply UND Return in Type A1
- Alle VP-Motoren: Schlauchanschlüsse sind Push-on mit Schlauchschellen (keine Pressfittings)
- VP empfiehlt SAE-Normschläuche — kein proprietäres System

### 9.2 Yanmar (1GM–6LY Serie)

**Yanmar Marine Diesel — Schlauch-Spezifikationen:**

| Motor | Leistung | Supply ID (mm) | Return ID (mm) | OEM-Schlauch |
|-------|---------|----------------|----------------|-------------|
| 1GM10 | 9 PS | 8 | 6 | Yanmar 128170-59500 |
| 2GM20 | 18 PS | 8 | 6 | Yanmar 128370-59500 |
| 3GM30 | 27 PS | 8 | 8 | Yanmar 128570-59500 |
| 2YM15 | 14 PS | 8 | 6 | Yanmar 128671-59500 |
| 3YM20 | 21 PS | 8 | 8 | Yanmar 128671-59510 |
| 3YM30 | 29 PS | 8 | 8 | Yanmar 128671-59510 |
| 3JH40 | 39 PS | 8 | 8 | Yanmar 129670-59600 |
| 3JH57 | 57 PS | 10 | 8 | Yanmar 129670-59610 |
| 4JH45 | 45 PS | 10 | 8 | Yanmar 129470-59600 |
| 4JH57 | 57 PS | 10 | 8 | Yanmar 129470-59610 |
| 4JH80 | 80 PS | 10 | 10 | Yanmar 129470-59620 |
| 4JH110 | 110 PS | 10 | 10 | Yanmar 129470-59630 |
| 4LHA-STP | 160 PS | 12 | 10 | Yanmar 119773-59510 |
| 4LHA-STZP | 180 PS | 12 | 10 | Yanmar 119773-59510 |
| 6LY2-STP | 315 PS | 12 | 12 | Yanmar 119773-59520 |
| 6LY3-STP | 380 PS | 16 | 12 | Yanmar 119773-59530 |
| 6LY-UTE | 350 PS | 16 | 12 | Yanmar 119773-59530 |

**Yanmar OEM-Preise vs. Aftermarket:**

| Motor-Klasse | OEM-Preis (EUR/m) | Aftermarket (EUR/m) | Ersparnis |
|-------------|------------------|--------------------|-----------| 
| 1GM–3GM (8mm) | 65–85/Stk | Vetus FUHOSE08A: 16,90 | 70–80% |
| 3JH–4JH (10mm) | 75–95/Stk | Vetus FUHOSE10A: 18,50 | 72–80% |
| 4LHA–6LY (12mm) | 95–125/Stk | Trident 327-5001: 26,50 | 70–78% |

**Yanmar Einbau-Besonderheiten:**
- 1GM/2GM/3GM: Älteste Baureihe, oft noch mechanische Einspritzung → Niederdrucksystem
- Yanmar verwendet metrische Anschlüsse (nicht SAE/AN)
- OEM-Schläuche sind kürzer als VP-Äquivalente → enge Maschinenräume
- 3JH/4JH (Common-Rail ab 4JH80): Rücklaufdruck bis 2 bar → Type A1 empfohlen
- Yanmar-OEM-Schläuche haben proprietäre Steckverbinder an einigen Modellen → Aftermarket nur mit Adapter

### 9.3 Nanni (N-Serie)

**Nanni Diesel Marine — Schlauch-Spezifikationen:**

| Motor | Basis | Leistung | Supply ID (mm) | Return ID (mm) | OEM-Schlauch |
|-------|-------|---------|----------------|----------------|-------------|
| N2.10 | Kubota | 10 PS | 8 | 6 | Nanni 970312125 |
| N2.14 | Kubota | 14 PS | 8 | 6 | Nanni 970312125 |
| N3.21 | Kubota | 21 PS | 8 | 8 | Nanni 970312130 |
| N3.30 | Kubota | 30 PS | 8 | 8 | Nanni 970312130 |
| N4.38 | Kubota | 38 PS | 10 | 8 | Nanni 970312135 |
| N4.50 | Kubota | 50 PS | 10 | 8 | Nanni 970312135 |
| N4.60 | Kubota | 60 PS | 10 | 10 | Nanni 970312140 |
| N4.80 | Kubota | 80 PS | 10 | 10 | Nanni 970312140 |
| N4.100 | Kubota | 100 PS | 12 | 10 | Nanni 970312145 |
| T4.155 | — | 155 PS | 12 | 10 | Nanni 970312150 |
| T4.180 | — | 180 PS | 12 | 12 | Nanni 970312155 |

**Nanni Besonderheiten:**
- Kubota-basierte Motoren (N-Serie): Identische Anschlüsse wie Kubota Industrie
- Nanni OEM-Schläuche = Rebranded Industrieschläuche mit Nanni-Markierung
- Aftermarket-Alternative: Jeder ISO 7840-konforme Schlauch mit passender Dimension
- OEM-Preis ca. 60% über Aftermarket (kleinere Stückzahlen)
- Nanni-Händlernetz: Gut in Frankreich, Mittelmeer; eingeschränkt in Nordeuropa

### 9.4 Beta Marine (Kubota-Basis)

**Beta Marine Diesel — Schlauch-Spezifikationen:**

| Motor | Basis | Leistung | Supply ID (mm) | Return ID (mm) |
|-------|-------|---------|----------------|----------------|
| Beta 10 | Kubota Z482 | 10 PS | 8 | 6 |
| Beta 14 | Kubota D722 | 14 PS | 8 | 6 |
| Beta 16 | Kubota D722 | 16 PS | 8 | 6 |
| Beta 20 | Kubota D1005 | 20 PS | 8 | 8 |
| Beta 25 | Kubota D1105 | 25 PS | 8 | 8 |
| Beta 30 | Kubota V1505 | 30 PS | 10 | 8 |
| Beta 35 | Kubota V1505 | 35 PS | 10 | 8 |
| Beta 38 | Kubota V2003 | 38 PS | 10 | 8 |
| Beta 43 | Kubota V2003 | 43 PS | 10 | 10 |
| Beta 50 | Kubota V2203 | 50 PS | 10 | 10 |
| Beta 60 | Kubota V2403 | 60 PS | 12 | 10 |
| Beta 75 | Kubota V3300 | 75 PS | 12 | 10 |
| Beta 90 | Kubota V3300T | 90 PS | 12 | 10 |
| Beta 105 | Kubota V3800 | 105 PS | 12 | 12 |
| Beta 115 | Kubota V3800T | 115 PS | 12 | 12 |
| Beta 150 | Kubota V3800TT | 150 PS | 16 | 12 |

**Beta Marine Besonderheiten:**
- Beta Marine nutzt unmodifizierte Kubota-Blöcke → Kubota-Industrieschläuche passen
- Kein proprietäres Schlauchsystem — Standard-Schlauchtüllen mit Schlauchschellen
- Beta Marine hat keine eigenen OEM-Schläuche → verweist auf "ISO 7840 compliant hose"
- Ideal für Aftermarket: Jeder passende ISO 7840-Schlauch funktioniert
- Beta Marine = britischer Hersteller → Anschlüsse in metrisch UND imperial verfügbar

### 9.5 Cummins Marine (QSB/QSC/QSM)

**Cummins Marine Diesel — Schlauch-Spezifikationen:**

| Motor | Leistung | Supply ID (mm) | Return ID (mm) | Fill ID (mm) | OEM-Teil |
|-------|---------|----------------|----------------|-------------|---------|
| QSB 5.9-230 | 230 PS | 12 | 12 | 51 | Cummins 3920725 |
| QSB 5.9-270 | 270 PS | 12 | 12 | 51 | Cummins 3920725 |
| QSB 5.9-315 | 315 PS | 16 | 12 | 51 | Cummins 3920726 |
| QSB 5.9-380 | 380 PS | 16 | 12 | 51 | Cummins 3920726 |
| QSB 6.7-380 | 380 PS | 16 | 12 | 51 | Cummins 5304220 |
| QSB 6.7-425 | 425 PS | 16 | 16 | 51 | Cummins 5304221 |
| QSB 6.7-480 | 480 PS | 16 | 16 | 51 | Cummins 5304221 |
| QSC 8.3-500 | 500 PS | 19 | 16 | 51 | Cummins 4936036 |
| QSC 8.3-540 | 540 PS | 19 | 16 | 51 | Cummins 4936036 |
| QSC 8.3-600 | 600 PS | 19 | 16 | 51 | Cummins 4936037 |
| QSM 11-635 | 635 PS | 19 | 19 | 64 | Cummins 4963809 |
| QSM 11-715 | 715 PS | 25 | 19 | 64 | Cummins 4963810 |

**Cummins Besonderheiten:**
- Common-Rail-Systeme mit hohem Rücklaufdruck (bis 4 bar) → ALLE Schläuche in Type A1
- Cummins spezifiziert SAE-konforme Schläuche → Aftermarket einfach
- OEM-Schläuche sind vorkonfektioniert mit Cummins-Quickconnect-Fittings
- Aftermarket mit Standard-Schlauchtüllen + Schlauchschellen funktioniert ebenfalls
- Cummins hat eigenes Servicenetz weltweit → OEM-Teile global verfügbar
- OEM-Preis: ca. 40–60% über Aftermarket (gerechtfertigt durch Quickconnect-Fittings)

### 9.6 MAN Marine (D0834/D0836/D2676)

**MAN Marine Diesel — Schlauch-Spezifikationen:**

| Motor | Leistung | Supply ID (mm) | Return ID (mm) | OEM-Teil |
|-------|---------|----------------|----------------|---------|
| D0834 M (4-Zyl.) | 200 PS | 12 | 10 | MAN 51.96301-6183 |
| D0834 M | 240 PS | 12 | 10 | MAN 51.96301-6183 |
| D0836 M (6-Zyl.) | 300 PS | 16 | 12 | MAN 51.96301-6184 |
| D0836 M | 360 PS | 16 | 12 | MAN 51.96301-6184 |
| D2676 LE (6-Zyl.) | 537 PS | 19 | 16 | MAN 51.96301-6190 |
| D2676 LE | 730 PS | 19 | 16 | MAN 51.96301-6191 |
| D2676 LE | 800 PS | 25 | 19 | MAN 51.96301-6192 |
| D2862 V12 | 1.300 PS | 25 | 25 | MAN 51.96301-6195 |
| D2862 V12 | 1.550 PS | 32 | 25 | MAN 51.96301-6196 |

**MAN Besonderheiten:**
- MAN verlangt für Garantie-Erhalt MAN-zugelassene Schläuche
- Continental MFH-A1 ist von MAN zugelassen (als Aftermarket-Alternative)
- D2676/D2862: Superyacht-Motoren → Lloyd's/DNV-Zulassung der Schläuche erforderlich
- MAN OEM-Preise: 80–120% über Aftermarket (Premium-Positionierung)
- MAN-Servicenetz: Gut in Europa, eingeschränkt außerhalb

### 9.7 Caterpillar Marine (C7/C9/C12)

**Caterpillar Marine Diesel — Schlauch-Spezifikationen:**

| Motor | Leistung | Supply ID (mm) | Return ID (mm) | OEM-Teil |
|-------|---------|----------------|----------------|---------|
| C7.1 | 280 PS | 12 | 12 | CAT 385-5429 |
| C7.1 | 400 PS | 16 | 12 | CAT 385-5430 |
| C7.1 | 500 PS | 16 | 16 | CAT 385-5431 |
| C9.3 | 475 PS | 16 | 16 | CAT 432-6734 |
| C9.3 | 575 PS | 19 | 16 | CAT 432-6735 |
| C12.9 | 650 PS | 19 | 16 | CAT 466-8730 |
| C12.9 | 770 PS | 19 | 19 | CAT 466-8731 |
| C12.9 | 1.000 PS | 25 | 19 | CAT 466-8732 |
| C18 | 803 PS | 25 | 19 | CAT 386-7012 |
| C18 | 1.015 PS | 25 | 25 | CAT 386-7013 |
| C18 | 1.150 PS | 32 | 25 | CAT 386-7014 |
| C32 | 1.622 PS | 32 | 32 | CAT 386-7020 |
| C32 | 1.925 PS | 38 | 32 | CAT 386-7021 |

**Caterpillar Besonderheiten:**
- CAT-ACERT-Motoren: Elektronische Einspritzung mit hohem Rücklaufdruck
- CAT verlangt "CAT Spec" Schläuche oder gleichwertig nach ISO 7840 A1
- CAT-Servicenetz: Weltweit ausgezeichnet (auch in abgelegenen Gebieten)
- OEM-Preise: Höchste der Branche — 100–150% über Aftermarket
- Aftermarket-Alternative: Continental MFH-A1 (von CAT akzeptiert für Nicht-Garantie-Installationen)

### 9.8 MerCruiser Benzin (3.0L/5.7L/8.2L)

**MerCruiser Benzin-Motoren — Schlauch-Spezifikationen:**

**ACHTUNG: Benzin-Systeme erfordern USCG Type A / ISO 7840 Type A1 im GESAMTEN Maschinenraum!**

| Motor | Leistung | Supply ID (mm) | Return ID (mm) | OEM-Teil |
|-------|---------|----------------|----------------|---------|
| 3.0L MPI (4-Zyl.) | 135 PS | 8 | 8 | Mercury 32-860211 |
| 4.3L MPI (V6) | 190 PS | 8 | 8 | Mercury 32-860212 |
| 4.5L (V6) | 200–250 PS | 10 | 8 | Mercury 32-8M0148948 |
| 5.7L MPI (V8) | 260 PS | 10 | 8 | Mercury 32-8M0060051 |
| 6.2L MPI (V8) | 300–350 PS | 10 | 10 | Mercury 32-8M0060052 |
| 8.2L MAG HO (V8) | 380–430 PS | 12 | 10 | Mercury 32-866729 |
| 8.2L MAG HO (V8) | 430 PS | 12 | 10 | Mercury 32-866729 |

**MerCruiser Benzin — Kritische Sicherheitshinweise:**

1. **ALLE Schläuche im Maschinenraum MÜSSEN ISO 7840 Type A1 / USCG Type A sein** — keine Ausnahme!
2. **Bilgenbelüftung mit funkensicherem Gebläse ist PFLICHT** (USCG 33 CFR 183.610)
3. **Benzindampf-Sensor (Fume Detector) empfohlen** (ABYC H-24.14)
4. **Vor jedem Motorstart: Bilgengebläse 4 Minuten laufen lassen** (ABYC H-24.14.1)
5. **Schlauchschellen: Doppelt an jedem Anschluss** (ABYC H-24.10.5)
6. **Kein Schlauch darf heißer als 60°C werden** — Benzindämpfe bei 60°C = sofortige Zündgefahr

**MerCruiser OEM vs. Aftermarket:**

| Funktion | OEM-Preis (EUR) | Aftermarket (EUR) | Empfehlung |
|---------|----------------|-------------------|-----------|
| Supply 8mm, 1m | 75 | Trident 327-5161: 18,50 + 8 | Trident 327 (E85-kompatibel!) |
| Supply 10mm, 1m | 85 | Shields 350-0586: 22,50 + 8 | Shields 350 (Ultra Low Perm!) |
| Supply 12mm, 1,5m | 110 | Trident 327-5001: 39,75 + 12 | Continental MFH-A1-12 für Maximum |
| Return 8mm, 1m | 65 | Trident 328-5162: 14,50 + 8 | Trident 328 (Type A2 ausreichend) |

### 9.9 Zusammenfassung: Kosten OEM vs Aftermarket

**Durchschnittliche Kostenverhältnisse nach Motorhersteller:**

| Motorhersteller | OEM-Preis (Index) | Aftermarket (Index) | Ersparnis | OEM-Vorteile |
|----------------|------------------|--------------------|-----------|--------------| 
| Volvo Penta | 100 | 30 | 70% | Vorkonfektioniert, Garantie |
| Yanmar | 100 | 25 | 75% | Vorkonfektioniert |
| Nanni | 100 | 40 | 60% | Rebranded Industrie — kaum Vorteil |
| Beta Marine | — | — | — | Kein OEM-Schlauch, direkt Aftermarket |
| Cummins | 100 | 45 | 55% | Quickconnect-Fittings, globale Verfügbarkeit |
| MAN | 100 | 35 | 65% | Garantie-Konformität |
| Caterpillar | 100 | 30 | 70% | Garantie-Konformität, globales Servicenetz |
| MerCruiser | 100 | 30 | 70% | Passgenauigkeit |

**AYDI-Empfehlung zur OEM/Aftermarket-Entscheidung:**

| Situation | Empfehlung | Begründung |
|-----------|-----------|------------|
| Motor unter Garantie | OEM | Garantie-Erhalt, Hersteller-Konformität |
| Motor >3 Jahre, Standard-Anschlüsse | Aftermarket (ISO 7840 A1) | 55–75% Kostenersparnis, gleichwertige Qualität |
| Motor >3 Jahre, proprietäre Anschlüsse | OEM oder Aftermarket + Adapter | Adapter-Kosten einkalkulieren |
| Superyacht, klassifiziert (Lloyd's/DNV) | Continental MFH-A1 oder OEM | Klassifikations-Zulassung erforderlich |
| Langfahrt/Weltumsegelung | Aftermarket (Trident/Shields) | Globale Verfügbarkeit, universelle Anschlüsse |
| Benzin-System (jedes Alter) | Premium-Aftermarket (Trident 327 E85 oder Shields 350) | Sicherheit hat Priorität, niedrige Permeation |

---

## Schlauchschellen & Verbindungstechnik

### Typen für Kraftstoff-Anwendungen

Im Kraftstoffsystem sind ausschliesslich kraftstoffbestaendige, zugelassene Schlauchschellen zu verwenden. Die wesentlichen Typen:

| Typ | Beschreibung | Werkstoff | Bandbreite (mm) | Einsatzbereich | Normverweis |
|-----|-------------|-----------|-----------------|----------------|-------------|
| Schneckengewinde-Schelle (Worm Drive) | Standard-Schlauchschelle mit Schneckengewinde-Spannband | AISI 316L (Band + Gehaeuse) | 9–12 mm | Standard-Kraftstoffleitungen ID 8–50 mm | DIN 3017, SAE J1508 |
| T-Bolt-Schelle | Hochdruck-Schlauchschelle mit T-Bolzen-Verschluss | AISI 316L, Dichteinlage EPDM oder FKM | 18–25 mm | Auspuff-nah, Hochdruck-Kraftstoffsysteme | SAE J1508 Typ 2 |
| Doppelschlauchschelle | Zwei parallele Schneckengewinde-Schellen auf einem Traeger | AISI 316L | 2× 9 mm, Abstand 12–15 mm | Pflicht an Tankstutzen, Kraftstofffilter | ABYC H-24.8, ISO 10088 |
| Federbandschelle | Selbstspannende Federstahlschelle | Federstahlband, verzinkt oder 301 SS | 7–9 mm | OEM-Erstausruestung, nicht fuer Nachruestung | OEM-spezifisch |
| Crimp-/Pressfitting | Dauerhaft verpresste Verbindung | Messing vernickelt oder 316L | n/a | Festverlegte Hochdruck-Kraftstoffleitungen | ISO 8434, SAE J1290 |
| Oetiker-Klemmschelle (Ohr-Schelle) | Einmal-Klemmring mit Ohr | AISI 304 oder 316L | 7–9 mm | Kleine ID (6–16 mm), OEM-Einsatz | Oetiker Typ 167 |

**Kritische Materialanforderung:** Fuer alle Kraftstoff-Schlauchschellen im Marinebereich gilt: NUR Edelstahl AISI 316L (Werkstoff-Nr. 1.4404). Verzinkte Stahlschellen (DIN 3017 Standard) sind im Salzwasser-Umfeld binnen 12–24 Monaten korrosionsanfaellig und duerfen NICHT eingesetzt werden.

**Bandbreite vs. Haltekraft:**

| Bandbreite (mm) | Max. Spannkraft (N) | Empfohlener Einsatz |
|-----------------|---------------------|---------------------|
| 9 | 450–600 | Kraftstoffschlauch ID ≤ 19 mm |
| 12 | 600–900 | Kraftstoffschlauch ID 19–38 mm |
| 14 | 900–1200 | Kraftstoffschlauch ID 38–51 mm |
| 18 (T-Bolt) | 1500–2500 | Hochdruck, vibrationskritisch |
| 25 (T-Bolt) | 2500–4000 | Auspuff-Kraftstoffleitungen, Superyacht |

### KRITISCH: Kraftstoff-Dichtigkeit vs Kuehlwasser

Verwechslung von Kuehlwasser- und Kraftstoff-Schlauchschellen ist eine der haeufigsten Fehlerquellen bei DIY-Arbeiten und fuehrt zu Leckagen, Brandgefahr und Versicherungsverlust.

| Merkmal | Kraftstoff-Schlauchschelle | Kuehlwasser-Schlauchschelle |
|---------|---------------------------|----------------------------|
| Werkstoff Band | 316L zwingend | 304 oder 316L akzeptabel |
| Werkstoff Gehaeuse | 316L zwingend | 304 akzeptabel |
| Bandbreite min. | 9 mm, empfohlen 12 mm | 9 mm ausreichend |
| Bandkanten | Gerollt/entgratet (Schlauchschutz) | Standard genuegt |
| Doppelschelle Pflicht | Ja — am Tank, am Filter, am Motor | Nein (empfohlen an Thermostatgehaeuse) |
| Anziehdrehmoment-Kontrolle | Pflicht (Drehmomentschluessel) | Empfohlen |
| Norm | SAE J1508 Typ F, ABYC H-24 | SAE J1508 Typ G |
| Perforations-Band | NICHT zulaessig (Dieselpermeation) | Zulaessig |

**AYDI-Bewertungsregel:** Perforierte Schlauchschellen im Kraftstoffsystem → automatisch Score 15/100, Befund KRITISCH, Sofortige Nachruestung erforderlich.

### Schlauchschellen-Hersteller

| Hersteller | Modell | Werkstoff | Bandbreite (mm) | Preis/Stueck (EUR) | Besonderheit |
|-----------|--------|-----------|-----------------|-------------------|-------------|
| ABA Group (Schweden) | ABA 316 Worm Drive | 316L | 9, 12 | 2,80–4,50 | Europaeischer Marktfuehrer, DIN 3017 zertifiziert |
| NORMA Group (DE) | NORMA TORRO S 316 | 316L vollstaendig | 9, 12 | 3,20–5,10 | Gerollte Bandkanten, hoher Schlauchschutz |
| Jubilee Clips (UK) | Marine Grade 316 | 316L | 9, 12 | 2,50–3,80 | Weit verbreitet, gutes P/L-Verhaeltnis |
| Oetiker (CH) | StepLess 167 316L | 316L | 7 | 1,80–2,60 | OEM-Standard, Einmalverwendung, Spezialzange noetig |
| T-Bolt Marine (US) | TBOLT-316 | 316L + FKM-Liner | 18, 25 | 8,50–14,00 | Hochdruck, Vibrationsdaempfung |
| Mikalor (ES) | SUPRA W4 316 | 316L | 9, 12 | 2,90–4,20 | SUPRA-Spannmechanismus, hohe Gleichmaessigkeit |
| Breeze (US/IDEAL) | Power Seal 316SS | 316L | 12 | 3,50–5,50 | US-Marktfuehrer, ABYC-konform |
| Hi-Grip (UK) | Hi-Torque 316 | 316L | 12 | 4,00–6,00 | Hohes Drehmoment, Profi-Segment |

### Doppelschlauchschellen — Wann Pflicht?

Gemaess ABYC H-24.8, USCG 33 CFR 183.558 und ISO 10088:2017 sind Doppelschlauchschellen an folgenden Positionen **PFLICHT**:

| Position | Norm | Begruendung |
|----------|------|-------------|
| Tank-Einfuellstutzen | ABYC H-24.8.1 | Schwerkraftbelastung, Schwingungseinleitung |
| Tank-Entnahme (Saugseite) | ABYC H-24.8.2 | Unterdruck-Belastung, Kavitation |
| Tank-Ruecklauf | ABYC H-24.8.3 | Pulsation durch Einspritzpumpe |
| Motor-Kraftstoffanschluss (Eingang) | ABYC H-24.8.4 | Vibration, Waerme, Pulsation |
| Motor-Kraftstoffanschluss (Ruecklauf) | ABYC H-24.8.5 | Ruecklauf-Pulsation |
| Kraftstofffilter/Wasserabscheider (Eingang + Ausgang) | ABYC H-24.8.6 | Regelmaeessiger Service = haeufige Demontage |
| Kraftstoffventil/Absperrhahn | ISO 10088:2017 Abschn. 7.3 | Mechanische Belastung durch Hebelbewegung |

**Mindestabstand der zwei Schellen:** 12 mm Bandmitte zu Bandmitte (NORMA-Empfehlung: 15 mm). Zu geringer Abstand reduziert die Einzelwirkung und kann den Schlauch deformieren.

**AYDI-Bewertungsregel:** Fehlende Doppelschelle an Pflichtposition → Score 20/100, Befund SCHWERWIEGEND.

### Anziehdrehmomente

Korrekte Anziehdrehmomente sind entscheidend. Zu wenig = Leckage, zu viel = Schlauchbeschaedigung und Bandbruch.

| Schlauch-ID (mm) | Bandbreite 9 mm (Nm) | Bandbreite 12 mm (Nm) | T-Bolt 18 mm (Nm) |
|-------------------|----------------------|-----------------------|-------------------|
| 6–10 | 1,0–1,5 | n/a | n/a |
| 12–16 | 1,5–2,0 | 2,0–2,5 | n/a |
| 19–25 | 2,0–2,5 | 2,5–3,0 | 4,0–5,0 |
| 28–32 | 2,5–3,0 | 3,0–3,5 | 5,0–6,5 |
| 38–44 | n/a | 3,5–4,0 | 6,5–8,0 |
| 50–57 | n/a | 4,0–4,5 | 8,0–10,0 |

**Temperaturkorrektur:** Bei Einbau-Temperaturen > 30 °C das Drehmoment um 10 % reduzieren. Bei Einbau < 10 °C um 10 % erhoehen (Schlauch haerter, weniger Compliance).

**Nachzieh-Intervall:** Alle neuen Schlauchschellen nach 24 h Betrieb und nach der ersten Saison nachziehen. Drehmoment pruefen, nicht blind nachziehen.

### Korrosions-Mechanismen bei Kraftstoff-Kontakt

| Mechanismus | Betroffene Teile | Ursache | Zeitraum bis Versagen | Praevention |
|-------------|-----------------|---------|----------------------|-------------|
| Spaltkorrosion | Schneckengewinde-Gehaeuse | Stehende Feuchtigkeit unter Band | 18–36 Monate (304 SS) | 316L verwenden, Band nicht ueberlappen |
| Galvanische Korrosion | Schelle-auf-Stutzen | Unterschiedliche Metalle (z.B. 316L Schelle auf Bronze-Stutzen) | 12–24 Monate | Gleiche Legierung oder Isolator |
| Kraftstoff-induzierte Quellung | Schlauch unter Schelle | Biodiesel/Ethanol weicht NBR auf | 6–18 Monate | FKM/Viton-Schlauch verwenden |
| Lochfrass (Pitting) | Band-Innenseite | Chlorid-Konzentration (Spray) | 24–48 Monate (304), >120 Monate (316L) | 316L zwingend, suessen Wasserfilm |
| Spannungsrisskorrosion (SCC) | Ueberspannte Schelle | Zu hohes Drehmoment + Chlorid | 6–36 Monate | Drehmoment einhalten, 316L |
| Erosion | T-Bolt Dichteinlage | Vibration + Dieselkontakt | 36–60 Monate | FKM-Liner statt EPDM |

### USCG/ABYC Anforderungen an Kraftstoff-Verbindungen

**USCG 33 CFR 183, Subpart J (Fuel Systems):**
- 183.558: Alle Kraftstoffschlauch-Verbindungen muessen zwei unabhaengige Klemmmittel haben (= Doppelschelle) ODER einen zugelassenen Schnellverschluss-Fitting.
- 183.556: Kraftstoffschlaeuche muessen SAE J1527 (Benzin) oder ISO 7840 (Diesel) entsprechen.
- 183.562: Schlaeuche muessen so gefuehrt werden, dass kein Kontakt mit heissen Oberflaechen (> 200 °F / 93 °C) moeglich ist.

**ABYC H-24 (2021) — Gasoline Fuel Systems:**
- H-24.8: Doppelschellen an allen Verbindungspunkten.
- H-24.9: Keine perforierte Bandschellen.
- H-24.10: Schlauchschellen muessen korrosionsbestaendig, nicht-magnetisch sein.
- H-24.11: Mindest-Einschubtiefe des Schlauches auf den Stutzen: 2× Schlauch-AD oder 25 mm (was groesser ist).

**ABYC H-33 (2021) — Diesel Fuel Systems:**
- H-33.8: Analog zu H-24.8, Doppelschellen.
- H-33.9: Kraftstoffbestaendige 316L-Schellen.
- H-33.10: Zugaenglichkeit fuer Inspektion muss gewaehrleistet sein (min. 50 mm Freiraum um jede Verbindung).

---

## Technische Referenz & Berechnungen

### Durchfluss-Berechnungen fuer Kraftstoffsysteme

Die korrekte Dimensionierung des Kraftstoffschlauches richtet sich nach dem maximalen Kraftstoffverbrauch des Motors bei Volllast.

**Formel Kraftstoffverbrauch Diesel:**
```
Q_diesel (l/h) = P_motor (kW) × SFC (g/kWh) / (ρ_diesel × 1000)
SFC typisch: 210–240 g/kWh (moderne Commonrail), 250–280 g/kWh (aeltere Saugdiesel)
ρ_diesel = 0,835 kg/l bei 15 °C (EN 590)
```

**Formel Kraftstoffverbrauch Benzin:**
```
Q_benzin (l/h) = P_motor (kW) × SFC (g/kWh) / (ρ_benzin × 1000)
SFC typisch: 280–340 g/kWh (Vergaser), 240–290 g/kWh (EFI)
ρ_benzin = 0,745 kg/l bei 15 °C (EN 228)
```

**Dimensionierungstabelle Saugleitung (Vorlauf):**

| Motorleistung (kW) | Max. Verbrauch Diesel (l/h) | Min. Schlauch-ID (mm) | Empfohlene ID (mm) | Stroemungsgeschwindigkeit (m/s) |
|--------------------|---------------------------|----------------------|--------------------|-------------------------------|
| 10–30 | 4–9 | 6 | 8 | 0,05–0,08 |
| 30–75 | 9–21 | 8 | 10 | 0,07–0,12 |
| 75–150 | 21–42 | 10 | 12 | 0,10–0,16 |
| 150–300 | 42–84 | 12 | 16 | 0,12–0,18 |
| 300–600 | 84–168 | 16 | 19 | 0,15–0,22 |
| 600–1200 | 168–336 | 19 | 25 | 0,18–0,25 |

**Ruecklaufleitung:** Typisch 60–80 % des Vorlaufvolumens bei Dieselmotoren. Schlauch-ID gleich oder eine Stufe kleiner als Vorlauf.

**Max. Stroemungsgeschwindigkeit:** Saugleitung ≤ 0,3 m/s (Kavitationsvermeidung), Druckleitung ≤ 1,0 m/s, Ruecklauf ≤ 0,5 m/s.

### Druckverlust-Berechnung

Druckverlust in Kraftstoffschlaeuchen wird nach Hagen-Poiseuille (laminare Stroemung, Re < 2300) berechnet:

```
Δp = (128 × μ × L × Q) / (π × d⁴)

Δp = Druckverlust (Pa)
μ  = dynamische Viskositaet (Pa·s) — Diesel bei 20 °C: 0,003 Pa·s, Benzin: 0,0006 Pa·s
L  = Schlauchlänge (m)
Q  = Volumenstrom (m³/s)
d  = Innendurchmesser (m)
```

**Praxiswerte Druckverlust pro Meter bei typischen Volumenstromen:**

| Schlauch-ID (mm) | Volumenstrom (l/h) | Δp Diesel (mbar/m) | Δp Benzin (mbar/m) |
|-------------------|-------------------|--------------------|--------------------|
| 8 | 10 | 8,3 | 1,7 |
| 8 | 30 | 24,9 | 5,0 |
| 10 | 30 | 10,2 | 2,0 |
| 10 | 60 | 20,4 | 4,1 |
| 12 | 60 | 9,8 | 2,0 |
| 12 | 120 | 19,6 | 3,9 |
| 16 | 120 | 4,4 | 0,9 |
| 16 | 240 | 8,8 | 1,8 |
| 19 | 240 | 2,6 | 0,5 |
| 25 | 500 | 1,3 | 0,3 |

**Max. zulaessiger Gesamtdruckverlust Saugleitung:** 200 mbar (Empfehlung Yanmar/Volvo Penta), 250 mbar (Caterpillar Marine), 150 mbar (MTU/Rolls-Royce).

### Mindest-Biegeradius nach Schlauch-ID

| Schlauch-ID (mm) | Min. Biegeradius ISO 7840 A1 (mm) | Min. Biegeradius ISO 7840 A2 (mm) | Min. Biegeradius SAE J1527 R2 (mm) |
|-------------------|-----------------------------------|-----------------------------------|-------------------------------------|
| 5 | 25 | 30 | 38 |
| 6 | 30 | 36 | 45 |
| 8 | 40 | 50 | 64 |
| 10 | 50 | 65 | 76 |
| 12 | 60 | 75 | 89 |
| 16 | 85 | 100 | 127 |
| 19 | 100 | 120 | 152 |
| 25 | 130 | 160 | 203 |
| 32 | 170 | 200 | 254 |
| 38 | 200 | 240 | 305 |
| 50 | 260 | 310 | 381 |

**AYDI-Bewertungsregel:** Unterschreitung des Mindest-Biegeradius um > 20 % → Score 25/100, Befund SCHWERWIEGEND (Knickgefahr, Durchflussreduktion, Materialermuedung).

### Permeations-Rate Diesel vs Benzin

Permeation beschreibt die Durchdringung von Kraftstoffdampf durch die Schlauchwand. Entscheidend fuer Brandschutz und Emissionsschutz.

| Material | Diesel-Permeation (g/m²/24h bei 40 °C) | Benzin-Permeation (g/m²/24h bei 40 °C) | E10-Permeation (g/m²/24h bei 40 °C) | E85-Permeation (g/m²/24h bei 40 °C) |
|----------|----------------------------------------|----------------------------------------|-------------------------------------|-------------------------------------|
| NBR (Standard) | 5–15 | 25–80 | 40–120 | 80–250 |
| NBR/PVC Compound | 3–10 | 15–50 | 25–80 | 60–180 |
| FKM/Viton (Fluorelastomer) | 0,2–1,0 | 1,0–5,0 | 1,5–8,0 | 3,0–15,0 |
| PTFE-Innenliner | 0,05–0,2 | 0,1–0,5 | 0,15–0,8 | 0,3–1,5 |
| FKM + PTFE-Barrier | 0,02–0,1 | 0,05–0,3 | 0,08–0,5 | 0,1–0,8 |

**EPA-Grenzwert (MACT):** ≤ 15 g/m²/24h fuer Benzinsysteme (ab 2012). **CARB (Kalifornien):** ≤ 3 g/m²/24h.

**AYDI-Bewertungsregel:** NBR-Schlauch in Benzinsystem → Score 35/100 (Permeation ueber EPA-Grenzwert wahrscheinlich). FKM oder PTFE-Liner erforderlich.

### Vergleich: Material-Kosten pro Meter

| Material/Produkt | ID 10 mm (EUR/m) | ID 16 mm (EUR/m) | ID 25 mm (EUR/m) | Lebensdauer (Jahre) | EUR/m/Jahr |
|-------------------|-----------------|-----------------|-----------------|--------------------|-----------| 
| NBR-Standard (ISO 7840 A2) | 4,50 | 6,80 | 11,20 | 5–7 | 0,75–0,90 |
| NBR-Premium (ISO 7840 A1) | 8,20 | 12,50 | 19,80 | 8–10 | 0,82–1,03 |
| FKM/Viton (ISO 7840 A1) | 18,50 | 28,00 | 42,00 | 12–15 | 1,23–1,54 |
| PTFE-Glattschlauch (316L-Armierung) | 22,00 | 35,00 | 55,00 | 15–20 | 1,10–1,47 |
| PTFE-Wellschlauch (316L) | 28,00 | 42,00 | 68,00 | 15–20 | 1,40–1,87 |
| Continental ContiTech MFH-A1 | 14,50 | 22,00 | 34,00 | 10–12 | 1,21–1,45 |
| Trident 327 E85 | 16,80 | 25,50 | 39,00 | 10–14 | 1,20–1,68 |
| Shields 350 Series | 15,20 | 23,00 | 35,50 | 10–12 | 1,27–1,48 |

**AYDI-Kostenoptimierung:** FKM/Viton hat die niedrigsten Lebenszykluskosten (EUR/m/Jahr) trotz hohem Anschaffungspreis. Fuer Boote mit geplanter Nutzungsdauer > 8 Jahre ist FKM stets wirtschaftlicher als NBR.

---

## Einbau-/Austausch-Anleitung

### Werkzeug-Checkliste

| Nr. | Werkzeug | Spezifikation | Zweck | Preis (EUR) |
|-----|----------|--------------|-------|-------------|
| 1 | Drehmomentschluessel (klein) | 1–10 Nm, 1/4" Antrieb | Schlauchschellen anziehen | 45–85 |
| 2 | 5,5 mm Steckschluessel-Einsatz (1/4") | Fuer ABA/NORMA Schneckenantrieb | Standard-Schlauchschellen | 3–6 |
| 3 | 7 mm Steckschluessel-Einsatz | Fuer groessere Schellen | Schlauchschellen 12 mm Band | 3–6 |
| 4 | Kraftstoff-Absaugpumpe (manuell) | Oelfeste Membrane | Kraftstoff absaugen vor Trennung | 25–45 |
| 5 | Auffangschale (oelfest) | Min. 3 l, kraftstoffbestaendig | Aufangen von Restkraftstoff | 8–15 |
| 6 | Kraftstoff-Schlauchschneider | Ratschentyp, 6–38 mm | Sauberer, gerader Schnitt | 18–35 |
| 7 | Schlauch-Abzieher (Hook Tool) | Edelstahl, gebogen | Schlauch vom Stutzen loesen | 12–20 |
| 8 | Drahtbuerste (Edelstahl) | Kleine Ausfuehrung, 316L Borsten | Stutzen reinigen | 5–8 |
| 9 | Silikonfreies Gleitmittel | z.B. Parker O-Lube, Nyogel 774 | Schlauch auf Stutzen schieben | 12–18 |
| 10 | Oetiker-Zange (falls Ohr-Schellen) | Oetiker Typ HO 3000 | Ohr-Schellen pressen | 85–140 |
| 11 | Loeschdecke/Feuerloesche | DIN EN 1869, Klasse B | Brandschutz waehrend Arbeiten | 15–35 |
| 12 | Kraftstoff-Lappen (fusselarm) | Oelsaugende Vlies-Tuecher | Aufwischen, Abdichten | 12–20 |
| 13 | Nitrile-Handschuhe | Staerke 0,12 mm, kraftstoffbestaendig | Hautschutz | 8–12 |
| 14 | Sicherheitsbrille | EN 166, Spritzschutz | Augenschutz | 5–12 |
| 15 | Gaswarngeraet (LEL-Messung) | z.B. MSA ALTAIR, BW Clip | Explosionsgefahr ueberwachen | 180–350 |

### Schritt-fuer-Schritt Kraftstoffschlauch-Austausch

**Vorbereitung (30–60 min):**

1. **Kraftstoffventil schliessen** — Am Tank-Absperrhahn drehen, bis geschlossen. Falls kein Ventil vorhanden: → AYDI-Befund SCHWERWIEGEND (fehlender Absperrhahn, ISO 10088 Abschn. 6.2).
2. **Elektrische Systeme abschalten** — Batterie-Hauptschalter AUS. Kein elektrischer Verbraucher darf aktiv sein (Funkenbildung!).
3. **Belueftung sicherstellen** — Alle Luken oeffnen. Motorraumluefter 15 min laufen lassen (sofern batteriebetrieben: separat versorgen).
4. **LEL-Messung durchfuehren** — Gaswarngeraet auf < 10 % LEL (Lower Explosive Limit) pruefen. Diesel-LEL = 0,6 Vol%, Benzin-LEL = 1,2 Vol%. Bei Ueberschreitung: NICHT arbeiten, weiter lueften.
5. **Restkraftstoff absaugen** — Schlauchleitung zwischen Ventil und Motor mit Absaugpumpe entleeren. Auffangschale unterstellen.
6. **Feuerloesch-Bereitschaft** — Loeschdecke + Feuerloesche (Klasse B, min. 2 kg CO₂ oder 6 kg Pulver) in Griffweite.
7. **Alten Schlauch fotografieren** — Verlauf, Schellenposition, Biegeradien dokumentieren (fuer AYDI-Zustandsbewertung).

**Demontage (15–30 min):**

8. **Schlauchschellen loesen** — Am motorseitigen Ende beginnen. Drehmomentschluessel rueckwaerts, langsam oeffnen.
9. **Schlauch abziehen** — Schlauch-Abzieher (Hook Tool) zwischen Schlauch und Stutzen schieben, vorsichtig drehen und ziehen. NICHT mit Zange am Schlauch reissen.
10. **Restkraftstoff auffangen** — Sofort Lappen/Vlies unter die offene Verbindung. Max. 50–200 ml Restmenge.
11. **Tankseite analog** — Gleiches Vorgehen am Tankanschluss.
12. **Stutzen pruefen** — Drahtbuerste reinigen. Auf Korrosion, Rillen, Verformung pruefen. Beschaedigte Stutzen ersetzen (NICHT nur den Schlauch!).

**Neuen Schlauch einbauen (20–40 min):**

13. **Neuen Schlauch ablaengen** — Alte Laenge + 10 mm Reserve. NICHT zu lang (Schlaufenbildung = Knickgefahr).
14. **Enden pruefen** — Schnittkanten muessen sauber, rechtwinklig und gratfrei sein.
15. **Schellen vorbereiten** — Doppelschellen auf Schlauchende auffaedeln BEVOR der Schlauch auf den Stutzen kommt. Haeufigster Fehler: Schellen vergessen.
16. **Gleitmittel auftragen** — Duenner Film silikonfreies Gleitmittel auf Stutzen und Schlauch-Innenseite. KEIN Fett, KEIN Silikon (Silikon greift NBR an).
17. **Schlauch aufschieben** — Mindest-Einschubtiefe: 2× Schlauch-Aussendurchmesser oder 25 mm (ABYC H-24.11). Schlauchende muss ueber Stutzen-Barb/Rillen hinausgehen.
18. **Schellen positionieren** — Erste Schelle 3–5 mm vom Schlauchende, zweite Schelle 15 mm dahinter. Schellengehaaeuse NICHT auf dem Stutzen-Barb, sondern auf der glatten Stutzenstrecke.
19. **Drehmoment anziehen** — Gemaess Tabelle (Abschnitt Anziehdrehmomente). Immer Drehmomentschluessel.
20. **Tankseite analog** — Gleiches Vorgehen.

**Inbetriebnahme & Pruefung (15–30 min):**

21. **Kraftstoffventil oeffnen** — Langsam oeffnen, auf Leckage an allen Verbindungen achten.
22. **Entlueften** — Diesel-Feinfilter (Racor etc.) entlueften gemaess Motor-Handbuch.
23. **Sichtpruefung** — 5 min warten, mit Papiertuch alle Verbindungen abtasten. Jede Feuchtigkeit = Nacharbeit.
24. **Motorstart** — Motor starten, 10 min Leerlauf. Erneut alle Verbindungen pruefen.
25. **Probelauf unter Last** — 30 min bei 70 % Last. Danach erneute Sichtpruefung.
26. **Dokumentation** — Datum, Material, Hersteller, Laenge, Schellentyp, Drehmomente notieren. Fuer AYDI-Level-2-Nutzer: in Servicebericht eintragen.

### Haeufige Fehler bei Kraftstoffschlauch-Montage

| Nr. | Fehler | Folge | Haeufigkeit | AYDI-Score |
|-----|--------|-------|-------------|-----------|
| 1 | Einzelschelle statt Doppelschelle | Leckage unter Vibration | 35 % aller DIY-Einbauten | 20/100 |
| 2 | Perforierte Schelle (Kuehlwasser-Typ) | Diesel-Permeation durch Loecher | 25 % | 15/100 |
| 3 | Zu kurzer Einschub auf Stutzen | Abrutschen bei Druckstoss | 20 % | 15/100 |
| 4 | Zu starkes Anziehen | Schlauch-Innenwand beschaedigt → Rissbildung | 15 % | 30/100 |
| 5 | Biegeradius unterschritten | Knick → Durchflussreduktion → Motorproblem | 30 % | 25/100 |
| 6 | Schlauchschellen nicht nachgezogen (24 h) | Setzverhalten → Leckage nach Wochen | 50 % | 45/100 |
| 7 | Silikonspray als Gleitmittel | Greift NBR an, Quellung, vorzeitige Alterung | 15 % | 30/100 |
| 8 | Kontakt mit Abgasrohr/Turbolader | Thermische Degradation, Brandgefahr | 10 % | 10/100 |
| 9 | Falscher Schlauchtyp (Kuehlwasserschlauch fuer Diesel) | Quellung, Aufloesung, Leckage | 8 % | 5/100 |
| 10 | Keine LEL-Messung vor Arbeit | Explosionsgefahr | 60 % | 20/100 |

### Spezial-Anleitung: Kraftstoff-Tank-Anschluss

**Tankstutzen-Typen:**

| Typ | Material | Schlauch-Befestigung | Verbreitung |
|-----|----------|---------------------|------------|
| Gerade Rohrstutzen mit Barbs | Aluminium (5083), Bronze, 316L | Doppelschlauchschelle | 60 % aller Yachten |
| 90°-Winkelstutzen mit Barbs | Aluminium, Bronze | Doppelschlauchschelle | 20 % |
| Flanschanschluss (DIN 2501) | 316L | Dichtring + Flanschschrauben | 15 % (Superyacht) |
| Schnellkupplung (Push-to-Connect) | Messing vernickelt, 316L | Integral (Klickverbindung) | 5 % (neuere Motoren) |

**Tank-Anschluss-Besonderheiten:**
- Aluminium-5083-Tankstutzen: KEINE Kupfer/Bronze-Schlauchschellen (galvanische Korrosion!).
- Einschubtiefe am Tankstutzen: min. 30 mm (ISO 10088:2017 Abschn. 7.2).
- Anti-Siphon-Ventil: Pflicht bei Tankentnahme unterhalb der Wasserlinie (ABYC H-24.14).
- Tankbelueftung: Separater Belueftungsschlauch, NICHT am Kraftstoff-Entnahmestutzen.

### Spezial-Anleitung: Kraftstofffilter-Anschluss (Racor etc.)

**Gaengige Kraftstofffilter/Wasserabscheider im Marine-Einsatz:**

| Modell | Hersteller | Durchfluss (l/h) | Anschluss-Gewinde | Schlauch-ID (mm) | Preis (EUR) |
|--------|-----------|------------------|-------------------|-----------------|-------------|
| Racor 500FG | Parker Hannifin | 227 | 3/4"-14 UNF | 10 (3/8") | 185–220 |
| Racor 900MA | Parker Hannifin | 341 | 7/8"-14 UNF | 12 (1/2") | 260–310 |
| Racor 1000MA | Parker Hannifin | 681 | 1"-14 UNF | 16 (5/8") | 350–420 |
| Separ SWK-2000/5 | MANN+HUMMEL | 250 | M16×1,5 | 10 | 140–180 |
| Separ SWK-2000/10 | MANN+HUMMEL | 500 | M22×1,5 | 12 | 220–280 |
| Delphi WSBF | Delphi Technologies | 200 | M14×1,5 | 8 | 95–130 |
| Volvo Penta 877767 | Volvo Penta | 300 | 3/4"-14 UNF | 10 | 165–210 |

**Anschluss-Technik:**
- Adapterstutzen (Gewinde auf Barb) mit Gewindedichtband (PTFE-Band, 3–5 Wicklungen, im Uhrzeigersinn).
- Schlauch auf Barb-Stutzen: Doppelschelle.
- Dichtpruefung: Nach Entlueftung 5 min bei geschlossenem Motor-Kraftstoffventil beobachten. Kein Druckabfall = dicht.

### Brandschutz-Integration

Kraftstoffschlaeuche sind die brandkritischste Komponente im Maschinenraum. Die Integration mit dem Brandschutz-Gesamtkonzept ist ueberlebenswichtig.

**ISO 7840 Brandtest-Anforderungen:**

| Klasse | Test | Dauer | Temperatur | Anforderung |
|--------|------|-------|-----------|-------------|
| A1 | Flammenbestaendigkeit (2,5 min) | 150 s | 650–750 °C (Bunsenbrenner) | Kein Durchbrennen, kein Lecken nach Test |
| A1 | Nachbrennzeit | ≤ 30 s | n/a | Flamme erlischt selbst |
| A2 | Flammenbestaendigkeit (2,5 min) | 150 s | 650–750 °C | Kein Durchbrennen waehrend Test (Lecken danach zulaessig) |
| A2 | Nachbrennzeit | ≤ 60 s | n/a | Flamme erlischt selbst |

**Brandschutz-Massnahmen fuer Kraftstoffleitungen:**

| Massnahme | Norm | Beschreibung | Kosten (EUR) |
|-----------|------|-------------|-------------|
| Mindestabstand zu Abgasrohr | ISO 9094:2015 Abschn. 6 | Min. 50 mm, empfohlen 100 mm | 0 (Planung) |
| Hitzeschutz-Wicklung | MIL-I-24244 | Glasfaser/Silikon-Wickelband, bis 540 °C | 8–15/m |
| Brandschutz-Schott | ISO 9094 Abschn. 5 | Metallschott zwischen Motor und Kraftstofftank | 80–250 |
| Feuerbestaendige Durchfuehrung | IMO FTP Code | Brandklappe/-huelse an Schotdurchfuehrung | 35–80/Stueck |
| Kraftstoff-Absperr (thermisch) | ABYC H-24.17 | Thermische Sicherung schliesst bei 105 °C | 45–90 |
| Fire-Stop-Manschette | DIN 4102-9 | Intumeszenz-Manschette am Schottdurchgang | 15–35/Stueck |

**AYDI-Bewertungsregel Brandschutz:**
- Kraftstoffschlauch < 50 mm von Abgasrohr → Score 5/100, KRITISCH
- Fehlende Hitzeschutz-Wicklung bei < 100 mm Abstand → Score 15/100, KRITISCH
- Fehlende thermische Absperrung → Score 30/100, SCHWERWIEGEND
- ISO 7840 A1 Schlauch ohne Brandtest-Zertifikat → Score 25/100, SCHWERWIEGEND

### Notfall-Reparatur auf offener See

**Szenario: Kraftstoffschlauch-Leckage auf See**

| Schritt | Aktion | Material | Zeit |
|---------|--------|----------|------|
| 1 | Motor SOFORT abstellen | — | 5 s |
| 2 | Batterie-Hauptschalter AUS | — | 10 s |
| 3 | Kraftstoffventil am Tank schliessen | — | 15 s |
| 4 | Belueftung maximieren (Luken, Dorade-Luefter) | — | 30 s |
| 5 | Leckstelle lokalisieren (visuell, Geruch) | Taschenlampe (Ex-geschuetzt!) | 2 min |
| 6 | Auffangmassnahme (Lappen/Oelbindevlies) | Oelbindetuecher | 1 min |
| 7a | Kleines Loch: Notfall-Reparaturband wickeln | z.B. Rescue Tape (Silikon-Selbstverschweissend), 3× Wicklung ueber Leck | 5 min |
| 7b | Schlauch gerissen: Abschneiden + Notstutzen + Doppelschelle | Messing-Stutzen (Bordvorrat), 4× Schlauchschellen | 15 min |
| 7c | Verbindung am Stutzen undicht: Schelle nachziehen oder ersetzen | Ersatz-Schlauchschelle (Bordvorrat) | 5 min |
| 8 | Sichtpruefung, Kraftstoffventil langsam oeffnen | — | 2 min |
| 9 | Motorstart, Beobachtung 10 min | — | 10 min |
| 10 | Naechsten Hafen anlaufen, professionelle Reparatur | — | — |

**Bordvorrat fuer Notfall-Reparatur (Empfehlung AYDI):**
- 2× Kraftstoffschlauch-Stuecke (je 500 mm, passende ID)
- 8× Doppelschlauchschellen (passende ID)
- 2× Messing-Geradenverbinder (Union Fitting)
- 1× Notfall-Reparaturband (z.B. Rescue Tape, Art.-Nr. RT1000206, 4,80 EUR)
- 2× Paar Nitrile-Handschuhe
- 1× Oelbinde-Kit (5 Tuecher)

---

## Lebensdauer und Alterungsmechanismen

### NBR-Schlauch Lebensdauer

| Betriebsbedingung | Erwartete Lebensdauer (Jahre) | Inspektionsintervall |
|-------------------|-------------------------------|---------------------|
| Dieselbetrieb, Maschinenraum < 50 °C, < 500 h/Jahr | 7–10 | 12 Monate |
| Dieselbetrieb, Maschinenraum 50–65 °C, > 500 h/Jahr | 5–7 | 6 Monate |
| Benzinbetrieb (E0), Maschinenraum < 50 °C | 5–8 | 12 Monate |
| Benzinbetrieb (E10), Maschinenraum < 50 °C | 3–5 | 6 Monate |
| Tropisches Klima (Maschinenraum > 60 °C dauerhaft) | 3–5 | 6 Monate |
| Winterlager ohne Kraftstoffentleerung | Reduzierung um 20–30 % | Vor Saisonstart |

**Lebensdauer-Formel (Arrhenius-Naeherung):**
```
t_end = t_ref × 2^((T_ref - T_actual) / 10)

t_ref = Referenz-Lebensdauer bei T_ref (typisch 8 Jahre bei 23 °C)
T_ref = 23 °C (Labortemperatur)
T_actual = mittlere Maschinenraum-Temperatur (°C)

Beispiel: 45 °C Dauerbetrieb → t_end = 8 × 2^((23-45)/10) = 8 × 2^(-2.2) = 8 × 0,217 = 1,74 Jahre
```

### FKM/Viton-Schlauch Lebensdauer

| Betriebsbedingung | Erwartete Lebensdauer (Jahre) | Inspektionsintervall |
|-------------------|-------------------------------|---------------------|
| Dieselbetrieb, alle Temperaturen bis 80 °C | 12–18 | 24 Monate |
| Benzinbetrieb (E0), bis 60 °C | 10–15 | 18 Monate |
| Benzinbetrieb (E10), bis 60 °C | 8–12 | 12 Monate |
| Benzinbetrieb (E85), bis 50 °C | 6–10 | 12 Monate |
| Tropisches Klima (> 60 °C dauerhaft) | 8–12 | 12 Monate |

### Alterungsmechanismen spezifisch fuer Kraftstoffschlaeuche

| Mechanismus | Beschreibung | Betroffenes Material | Erkennungszeichen | Zeitraum | AYDI-Score bei Erkennung |
|-------------|-------------|---------------------|-------------------|----------|------------------------|
| Thermische Oxidation | Sauerstoff reagiert mit Elastomer bei Waerme | NBR, CR | Verhaertung, Rissbildung, Sproedigkeit | 3–8 Jahre (abh. T) | 25–45/100 |
| Chemische Quellung | Kraftstoff diffundiert in Elastomernetzwerk | NBR (bei Biodiesel/E10) | Erweichung, Volumenzunahme, Verlust Zugfestigkeit | 1–5 Jahre | 20–35/100 |
| UV-Degradation | UV-Strahlung spaltet Polymerketten | Alle (besonders CR, NBR) | Oberflaechenrissigkeit, Kreidung | 2–5 Jahre (Deck-Verlegung) | 30–50/100 |
| Ozon-Rissbildung | Ozon (O₃) aus Luft greift Doppelbindungen an | NBR, NR | Quer-Risse (senkrecht zur Dehnrichtung) | 3–7 Jahre | 20–40/100 |
| Hydrolyse | Wasser spaltet Ester-Bindungen | Polyester-Gewebe-Einlage | Delaminierung, Aufblaasen | 5–12 Jahre (hohe Feuchtigkeit) | 15–30/100 |
| Ermuedung (Flex Fatigue) | Wiederholte Biegung durch Vibration | Alle | Risse an Biege-/Knickstellen, Gewebebruch | 4–10 Jahre (Vibration abh.) | 15–35/100 |
| Permeations-Degradation | Kraftstoffdampf veraendert innere Schlauchschicht | NBR | Innenschicht quellt, wird klebrig | 2–6 Jahre (Benzin), 5–10 (Diesel) | 25–45/100 |

### Ethanol-Degradation (E10-Effekte)

Ethanol (E10, E85) ist besonders aggressiv gegenueber NBR-Elastomeren. Seit der EU-weiten Einfuehrung von E10 (Super-Kraftstoff) ab 2011 sind Kraftstoffschlauch-Schaeden im Benzin-Marinebereich um ca. 40 % gestiegen.

**Ethanol-Schadigungsmechanismen:**

| Effekt | Beschreibung | Messung | Grenzwert |
|--------|-------------|---------|-----------|
| Volumetrische Quellung | NBR nimmt Ethanol auf, quillt um 15–35 % | ASTM D471 Immersion | >20 % = Austausch |
| Haerteaenderung | Shore A sinkt um 10–25 Punkte | Shore A Durometer | Δ > 15 Punkte = kritisch |
| Zugfestigkeits-Verlust | Mechanische Festigkeit sinkt um 20–50 % | ASTM D412 | > 30 % Verlust = Austausch |
| Extrahierbare Stoffe | Weichmacher und Fuellstoffe werden ausgewaschen | Gravimetrisch | > 5 % Masseverlust = kritisch |
| Permeations-Anstieg | Ethanol durchdringt NBR 3–5× schneller als Benzin allein | ASTM D814 | > EPA-Grenzwert = Austausch |

**Material-Empfehlung bei E10/E85:**
- E10 (10 % Ethanol): Mindestens NBR-Premium (ASTM D2000 BF), besser FKM.
- E85 (85 % Ethanol): NUR FKM/Viton oder PTFE-Liner. NBR ist NICHT zulaessig.
- Bio-Diesel (FAME B7–B30): NBR bedingt geeignet bis B7, FKM ab B20 erforderlich.

### Predictive Maintenance

**AYDI-Algorithmus fuer Kraftstoffschlauch-Restlebensdauer:**

```
Eingaben:
  - Material (NBR/FKM/PTFE)
  - Installationsdatum
  - Kraftstofftyp (Diesel/Benzin E0/E10/E85/Biodiesel)
  - Mittlere Maschinenraum-Temperatur (°C)
  - Betriebsstunden/Jahr
  - Letzte Inspektion (Datum, Score)
  - Visuelle Befunde (Risse, Quellung, Verfaerbung)

Berechnung:
  1. Basis-Lebensdauer aus Tabelle (Material × Kraftstoff × Temperatur)
  2. Arrhenius-Korrektur fuer Temperatur
  3. Abzug fuer Betriebsstunden > 500 h/Jahr (-10 % pro 250 h Ueberschreitung)
  4. Abzug fuer visuelle Befunde (Score < 50 → sofortige Handlungsempfehlung)
  5. Ergebnis: Geschaetzte Restlebensdauer (Monate), Confidence "estimated"

Ausgabe:
  - Restlebensdauer: x Monate (Confidence: estimated)
  - Naechste empfohlene Inspektion: Datum
  - Handlungsempfehlung: "Weiter nutzen" / "Inspektion vorziehen" / "Austausch planen" / "SOFORT austauschen"
```

---

## Fehlerbild-Atlas

### Fehlerbild 1: Oberflaechenrissbildung (Crazing)

- **Bezeichnung:** Oberflaechenrissbildung / Crazing
- **Visuell:** Feine Netzrisse auf der Schlauchaussenseite, 0,1–0,5 mm tief, unregelmaessiges Muster
- **Ursache:** UV-Exposition, Ozon-Angriff, thermische Alterung. Haeufig bei Schlaeuchen im Decksbereich oder nahe Abgasrohr
- **Folgen:** Zunaechst kosmetisch, bei Fortschreiten Tiefenrisse → Undichtigkeit, Branddampf-Austritt
- **Massnahme:** Bis 0,3 mm Tiefe: Beobachtung (6 Monate), Hitzeschutzwicklung nachrüsten. Ab 0,5 mm oder Ausbreitung auf > 30 % der Laenge: Austausch
- **AYDI-Score:** 55/100 (frueh) bis 25/100 (fortgeschritten)
- **Vorbeugung:** UV-Schutz (Wellrohr-Ummantelung), Abstand zu Waermequellen, FKM statt NBR

### Fehlerbild 2: Innenwand-Quellung (Internal Swelling)

- **Bezeichnung:** Innenwand-Quellung durch Kraftstoff-Absorption
- **Visuell:** Schlauch-ID verringert sich, Innenwand fuehlt sich klebrig/weich an, Schlauch laesst sich nicht mehr leicht vom Stutzen abziehen
- **Ursache:** Inkompatibles Material (NBR in E10/E85), Biodiesel > B7 in Standard-NBR
- **Folgen:** Durchflussreduktion → Motorleistungsabfall, Losloesung von Innenpartikeln → Filterverstopfung, Pumpenschaden
- **Massnahme:** Sofortiger Austausch auf FKM/Viton oder PTFE-Liner. Kraftstofffilter gleichzeitig wechseln
- **AYDI-Score:** 20/100 (SCHWERWIEGEND)
- **Vorbeugung:** Materialwahl an Kraftstofftyp anpassen, insbesondere bei E10-Umstellung

### Fehlerbild 3: Schlauchbruch an Knickstelle (Kink Fracture)

- **Bezeichnung:** Schlauchbruch / Riss an Knickstelle
- **Visuell:** Schlauch zeigt scharfen Knick (< Mindest-Biegeradius), Riss an Aussenseite der Biegung, Gewebe sichtbar
- **Ursache:** Unterschreitung des Mindest-Biegeradius, falsche Verlegung, fehlende Stuetzboegen
- **Folgen:** Leckage, im Extremfall vollstaendiger Bruch mit freiem Kraftstoffaustritt → akute Brandgefahr
- **Massnahme:** Sofortiger Austausch, Verlegung mit korrektem Biegeradius, ggf. 90°-Winkelanschluss verwenden
- **AYDI-Score:** 15/100 (KRITISCH)
- **Vorbeugung:** Biegeradius-Tabelle beachten, Stuetzboegen (316L Federdraht) einsetzen

### Fehlerbild 4: Schellenkorrosion (Clamp Corrosion)

- **Bezeichnung:** Korrodierte Schlauchschelle
- **Visuell:** Rostbraune Ablagerungen am Schellenband, Gehaeuse verfaerbt, Spindelgewinde schwergaengig
- **Ursache:** Falsche Werkstoffwahl (304 statt 316L, verzinkter Stahl), Spaltkorrosion, galvanische Korrosion
- **Folgen:** Verlust der Spannkraft → Schlauch rutscht ab, Schellenbruch unter Vibration
- **Massnahme:** Sofortiger Austausch aller korrodierten Schellen durch 316L-Schellen. Gegenstueck (Stutzen) auf galvanische Kompatibilitaet pruefen
- **AYDI-Score:** 25/100 (SCHWERWIEGEND)
- **Vorbeugung:** Ausschliesslich 316L-Schellen, kein Kontakt mit unedleren Metallen

### Fehlerbild 5: Delamination (Layer Separation)

- **Bezeichnung:** Delamination / Schichttrennung
- **Visuell:** Blasenbildung zwischen Innenseele und Gewebeeinlage, Schlauch fuehlt sich an wie "Luftpolster"
- **Ursache:** Hydrolyse der Haftschicht (bei hoher Feuchtigkeit), Produktionsmangel, mechanische Ueberbelastung
- **Folgen:** Schlauch blaest sich unter Druck auf → Berstgefahr, Blockierung → Motorausfall
- **Massnahme:** Sofortiger Austausch. Bei Blase > 10 mm Durchmesser: Motor nicht mehr starten
- **AYDI-Score:** 10/100 (KRITISCH)
- **Vorbeugung:** Nur ISO 7840 A1-zertifizierte Schlaeuche verwenden, Feuchtigkeit im Maschinenraum kontrollieren

### Fehlerbild 6: Kraftstoff-Leckage an Schelle (Clamp Leak)

- **Bezeichnung:** Tropfende Leckage an Schellenverbindung
- **Visuell:** Feuchte Stelle / Tropfenbildung am Schellenbereich, Kraftstoffgeruch, ggf. Verfaerbung
- **Ursache:** Zu geringes Anziehdrehmoment, Setzverhalten (nicht nachgezogen), beschaedigter Stutzen (Rillen/Korrosion)
- **Folgen:** Kraftstoffverlust, Bilge-Kontamination, Brand-/Explosionsgefahr (insbesondere Benzin)
- **Massnahme:** Drehmoment pruefen und nachziehen. Falls Leckage bleibt: Schelle + Schlauchende erneuern. Stutzen pruefen
- **AYDI-Score:** 20/100 (SCHWERWIEGEND) bis 10/100 (KRITISCH bei Benzin)
- **Vorbeugung:** 24-h-Nachziehen, Drehmomentschluessel, Doppelschellen

### Fehlerbild 7: Thermische Degradation (Heat Damage)

- **Bezeichnung:** Thermische Schaedigung / Verkohlungmassnahme
- **Visuell:** Verfaerbung (braun bis schwarz), Verhaertung, Sproedigkeit, ggf. Blasenbildung, verbrannter Geruch
- **Ursache:** Kontakt oder Naehe (< 50 mm) zu Abgaskruemmer, Turbolader, Auspuffrohr
- **Folgen:** Berstgefahr, Brandentstehung durch entzuendlichen Kraftstoffdampf an heisser Oberflaeche
- **Massnahme:** Sofortiger Austausch + Verlegung mit min. 100 mm Abstand + Hitzeschutzwicklung
- **AYDI-Score:** 5/100 (KRITISCH — akute Brandgefahr)
- **Vorbeugung:** Mindestabstand 100 mm, Hitzeschutz-Wicklung, Temperaturmessung im Maschinenraum

### Fehlerbild 8: Abrieb durch Scheuern (Chafe Damage)

- **Bezeichnung:** Scheuer-/Abriebschaeden
- **Visuell:** Abriebstelle mit sichtbarer Gewebeeinlage, flache Abschuerfung ueber 20–100 mm Laenge
- **Ursache:** Schlauch reibt an Schott, Kabelstrang, anderen Leitungen, scharfer Kante
- **Folgen:** Wanddicke reduziert → Berstgefahr, Gewebe freigelegt → Kapillar-Leckage
- **Massnahme:** Scheuerstelle mit Schutzschlauch (Spiralschlauch 316L oder Gummi-Ummantelung) sichern. Bei Gewebefreilegung: Austausch
- **AYDI-Score:** 30/100 (frueh) bis 15/100 (Gewebe freiliegend)
- **Vorbeugung:** Scheuerschutz an Durchfuehrungen, Kabelbinder mit Gummieinlage, keine scharfen Kanten

### Fehlerbild 9: Kraftstoff-Geruch ohne sichtbare Leckage (Permeation)

- **Bezeichnung:** Kraftstoff-Permeation / diffuse Kraftstoffdaempfe
- **Visuell:** Keine sichtbare Leckage, aber deutlicher Kraftstoffgeruch im Maschinenraum oder in der Bilge
- **Ursache:** NBR-Schlauch mit hoher Permeationsrate (insbesondere Benzin E10), veraltetes Material
- **Folgen:** Explosionsgefahr (Benzindampf + Funke), gesundheitliche Belastung (Benzoldaempfe karzinogen)
- **Massnahme:** Schlauch austauschen auf FKM/Viton oder PTFE-Liner. LEL-Messung zur Beurteilung
- **AYDI-Score:** 25/100 (SCHWERWIEGEND — unsichtbare Gefahr)
- **Vorbeugung:** FKM-Schlauch fuer Benzinsysteme, regelmaessige LEL-Messung, gute Belueftung

### Fehlerbild 10: Schlauch-Abrutschen (Hose Blowoff)

- **Bezeichnung:** Schlauch vom Stutzen abgerutscht
- **Visuell:** Schlauch haengt frei, Kraftstoff laeuft unkontrolliert aus
- **Ursache:** Einzelschelle statt Doppelschelle, zu wenig Drehmoment, zu kurze Einschubtiefe, Druckstoss (Dieselruecklauf-Pulsation)
- **Folgen:** Freier Kraftstoffaustritt → akute Brand-/Explosionsgefahr, Motorausfall
- **Massnahme:** Notfall: Kraftstoffventil sofort schliessen. Danach: Doppelschelle, korrekte Einschubtiefe, Drehmoment pruefen
- **AYDI-Score:** 5/100 (KRITISCH — hoechste Gefahrenstufe)
- **Vorbeugung:** Doppelschellen an allen Pflichtpositionen, Einschubtiefe min. 2× AD

### Fehlerbild 11: Biofilm/Mikrobiologische Kontamination (Diesel Bug)

- **Bezeichnung:** Mikrobiologische Kontamination im Schlauch ("Diesel Bug")
- **Visuell:** Schleimige, dunkle Ablagerungen an Schlauch-Innenwand, Filter-Verstopfung, trueber Kraftstoff
- **Ursache:** Bakterien/Hefepilze (Hormoconis resinae, Yarrowia lipolytica) wachsen an Diesel-Wasser-Grenzschicht
- **Folgen:** Schlauch-Innenwand wird angegriffen (Biokorrosion), Partikel verstopfen Filter/Einspritzduesen, Motorschaden
- **Massnahme:** Schlauch austauschen, Tank reinigen, Kraftstoffbiozid (z.B. Grotamar 82, 1:4000 Dosierung), Wasserabscheider pruefen
- **AYDI-Score:** 35/100 (SCHWERWIEGEND bei starkem Befall)
- **Vorbeugung:** Tank vollstaendig befuellen (weniger Kondensation), Wasserabscheider regelmaessig entleeren, Biozid 1×/Jahr

### Fehlerbild 12: Weichmacher-Ausschwitzung (Plasticizer Migration)

- **Bezeichnung:** Weichmacher-Migration / Ausschwitzung
- **Visuell:** Oelige, klebrige Oberflaeche, Schlauch fuehlt sich "fettig" an, ggf. Farbveraenderung, Umgebungsmaterialien (Isolierung, Kabel) angegriffen
- **Ursache:** Alterung des Elastomers, Weichmacher wandern an die Oberflaeche und verdunsten. Beschleunigt durch Waerme und Kraftstoffkontakt
- **Folgen:** Schlauch wird sproede (Weichmacherverlust), kontaminiert angrenzende Materialien, Schrumpfung → Leckage an Schellen
- **Massnahme:** Austausch des Schlauches, angrenzende Materialien auf Schaedigung pruefen
- **AYDI-Score:** 35/100 (SCHWERWIEGEND)
- **Vorbeugung:** FKM-Schlaeuche (keine externen Weichmacher), gute Belueftung, Temperatur kontrollieren

---

## Fehlerbehebungs-Leitfaden (Troubleshooting)

### Problem 1: Motor startet nicht / stirbt ab — Kraftstoff-Unterversorgung

**Diagnose-Sequenz:**

| Schritt | Pruefung | Erwartetes Ergebnis | Abweichung → Ursache |
|---------|----------|--------------------|--------------------|
| 1 | Tankfuellstand pruefen | > 10 % | Leer → Betanken |
| 2 | Kraftstoffventil pruefen | Offen | Geschlossen → Oeffnen |
| 3 | Vorfilter/Wasserabscheider pruefen | Sauberes Element, kein Wasser | Verschmutzt → Wechseln, Wasser → Ablassen |
| 4 | Kraftstoffschlauch Saugleitung visuell | Kein Knick, kein Leck | Knick → Neuverlegung, Leck → Austausch |
| 5 | Kraftstoffschlauch auf Luftziehen pruefen | Transparentes Zwischenstueck: keine Blasen | Blasen → Undichtigkeit Saugseite, Schellen pruefen |
| 6 | Schlauch-ID pruefen (Quellung) | Freier Durchgang, keine Verengung | Verengt → Austausch (Quellung/Biofilm) |
| 7 | Kraftstoffpumpe Foerderdruck messen | 0,2–0,5 bar (Saugpumpe) | Zu niedrig → Pumpe defekt ODER Saugwiderstand zu hoch |
| 8 | Druckverlust Schlauchstrecke messen | < 200 mbar ueber gesamte Saugleitung | > 200 mbar → Schlauch zu klein/zu lang/geknickt |

### Problem 2: Kraftstoffgeruch im Maschinenraum

**Diagnose-Sequenz:**

| Schritt | Pruefung | Erwartetes Ergebnis | Abweichung → Ursache |
|---------|----------|--------------------|--------------------|
| 1 | LEL-Messung (Gaswarngeraet) | < 10 % LEL | > 10 % → GEFAHR: Belueften, nicht starten |
| 2 | Alle Schellenverbindungen mit Papiertuch abtasten | Trocken | Feucht → Leckage: Nachziehen oder Austausch |
| 3 | Schlauch-Oberflaeche auf Naesse pruefen | Trocken | Feucht/oelig → Permeation oder Mikroporoesitaet |
| 4 | Tankentlueftung pruefen | Frei, nach aussen gefuehrt | Verstopft oder in Maschinenraum → Korrektur |
| 5 | Kraftstofffilter-Dichtung pruefen | Trocken, O-Ring intakt | Feucht → O-Ring tauschen |
| 6 | Einspritzleitungen pruefen (Hochdruck) | Trocken | Feucht → Motor-Fachwerkstatt |

### Problem 3: Kraftstoff in der Bilge

**Diagnose-Sequenz:**

| Schritt | Pruefung | Erwartetes Ergebnis | Abweichung → Ursache |
|---------|----------|--------------------|--------------------|
| 1 | Bilgenwasser-Probe (Sichtpruefung) | Klar, kein Oelfilm | Regenbogenfilm / Dieselgeruch → Kraftstoffeintrag |
| 2 | Tanknaehte / Tankunterseite | Trocken | Feucht → Tankleck (nicht Schlauch!) |
| 3 | Alle Kraftstoffschlauch-Verbindungen | Trocken | Feucht → Leckage lokalisieren |
| 4 | Einfuellstutzen-Dichtung | Dicht, kein Ueberlauf | Undicht → Dichtung ersetzen |
| 5 | Kraftstoff-Rueckschlagventil | Funktionsfaehig | Defekt → Rueckfluss in Bilge moeglich |

### Problem 4: Schlauch verhaertet / laesst sich nicht biegen

**Diagnose-Sequenz:**

| Schritt | Pruefung | Erwartetes Ergebnis | Abweichung → Ursache |
|---------|----------|--------------------|--------------------|
| 1 | Shore-A-Haerte messen (Durometer) | 60–75 Shore A (NBR neu) | > 85 Shore A → thermische Alterung |
| 2 | Maschinenraum-Temperatur pruefen | < 60 °C | > 60 °C → Belueftung verbessern, Schlauch tauschen |
| 3 | Abstand zu Waermequellen messen | > 100 mm zu Abgas | < 100 mm → Umverlegen + Hitzeschutz |
| 4 | Alter des Schlauches pruefen | < 7 Jahre (NBR) | > 7 Jahre → Altersbedingte Verhaertung, tauschen |
| 5 | UV-Exposition pruefen | Schlauch nicht UV-exponiert | UV-exponiert → UV-Schutz nachrüsten oder tauschen |

### Problem 5: Wiederkehrende Filterverstopfung

**Diagnose-Sequenz:**

| Schritt | Pruefung | Erwartetes Ergebnis | Abweichung → Ursache |
|---------|----------|--------------------|--------------------|
| 1 | Filterelement untersuchen | Gleichmaessige Verschmutzung | Schwarzer Schleim → Diesel Bug (Biofilm) |
| 2 | Kraftstoffprobe aus Tank | Klar, kein Wasser, kein Sediment | Trueb → Kontamination, Wasser → Kondensation |
| 3 | Schlauch-Innenwand pruefen (Endoskop) | Glatt, keine Ablagerungen | Ablagerungen → Schlauch spuelen oder tauschen |
| 4 | Tankinspektion (Endoskop) | Saubere Innenwand | Sediment/Rost → Tank reinigen |
| 5 | Schlauch-Material pruefen | Kraftstoffbestaendig (FKM/NBR-Premium) | Quellung/Partikelabloese → Falsches Material |

---

## FAQ — Haeufige Fragen

**KS-001: Wie oft muss ein Kraftstoffschlauch auf einer Yacht gewechselt werden?**
NBR-Schlaeuche: alle 7–10 Jahre (Diesel), 5–7 Jahre (Benzin E10). FKM/Viton: 12–15 Jahre. Bei sichtbaren Schaeden sofort. ABYC empfiehlt visuelle Inspektion alle 12 Monate, Shore-A-Messung alle 24 Monate.

**KS-002: Kann ich einen Kuehlwasserschlauch als Kraftstoffschlauch verwenden?**
NEIN. Kuehlwasserschlaeuche (EPDM) werden von Diesel und Benzin chemisch angegriffen, quellen auf und zersetzen sich. Nur ISO 7840 oder SAE J1527 zertifizierte Schlaeuche verwenden. Verwechslung ist ein KRITISCHER Sicherheitsmangel.

**KS-003: Sind alle 316L-Schlauchschellen gleich gut?**
Nein. Entscheidend ist, dass ALLE Teile (Band, Gehaeuse, Schraube) aus 316L bestehen. Manche Hersteller verwenden 316L-Band mit 304-Gehaeuse ("teilweise 316"). Fuer Kraftstoff nur "vollstaendig 316L" verwenden. Pruefung: Magnettest — 316L ist nicht-magnetisch.

**KS-004: Warum Doppelschellen und nicht eine starke Einzelschelle?**
Doppelschellen bieten Redundanz: Versagt eine Schelle (Korrosion, Vibration, Materialermuedung), haelt die zweite. Bei Kraftstoffsystemen ist Redundanz Pflicht (ABYC H-24.8, USCG 33 CFR 183.558). Ausserdem verteilt die Doppelschelle die Klemmkraft gleichmaessiger.

**KS-005: Darf ich PTFE-Band an Kraftstoff-Gewindeverbindungen verwenden?**
Ja, aber NUR sauerstofffreies PTFE-Gewindedichtband (weiss oder gelb, Kennzeichnung "Gas/Fuel"). Standard-PTFE (rosa/weiss) kann Partikel abgeben. Alternative: fluessige Gewindedichtung (z.B. Loctite 567, zugelassen fuer Kraftstoffe).

**KS-006: Was bedeutet ISO 7840 A1 vs A2?**
A1: Brandbestaendig (Fire Resistant) — Schlauch uebersteht 2,5 min offene Flamme ohne Durchbrennen, Nachbrennzeit ≤ 30 s. Pflicht fuer Benzin und Inneninstallation. A2: Flammenverzoegernd (Fire Retardant) — Uebersteht den Flammentest, kann aber danach lecken. Nur fuer Diesel-Aussenmontage zulaessig.

**KS-007: Kann ich einen Diesel-Schlauch auch fuer Benzin verwenden?**
Nur wenn der Schlauch fuer BEIDE Kraftstofftypen zertifiziert ist (ISO 7840 A1 oder SAE J1527). Reine Diesel-Schlaeuche (ISO 7840 A2) sind fuer Benzin NICHT zulaessig — fehlende Brandbestaendigkeit und zu hohe Permeation.

**KS-008: Was tun bei Kraftstoffgeruch ohne sichtbare Leckage?**
Sofort LEL-Messung durchfuehren. Ursache ist meist Permeation durch alternden NBR-Schlauch. Austausch auf FKM/Viton oder PTFE-Liner. Temporaer: Belueftung maximieren, offene Flammen vermeiden. Diesel: Geruch ≠ Explosionsgefahr. Benzin: Geruch = potenzielle Explosionsgefahr.

**KS-009: Wieviel kostet der komplette Kraftstoffschlauch-Austausch bei einer 12-m-Segelyacht?**
Material: 120–280 EUR (Schlauch 4–6 m + Schellen + Zubehoer). Werkstattkosten: 3–6 Arbeitsstunden × 85–120 EUR/h = 255–720 EUR. Gesamt: 375–1.000 EUR je nach Material und Zugaenglichkeit. DIY spart 50–70 %.

**KS-010: Wie pruefe ich, ob mein Schlauch noch gut ist?**
1. Biege-Test: Schlauch in der Hand um 90° biegen — federt zurueck = OK, bleibt verformt = Austausch. 2. Shore-A-Messung: Durometer an 3 Stellen, Mittelwert > 85 = Austausch. 3. Sichtpruefung: Risse, Verfaerbung, Quellung → Austausch. 4. Geruchstest: Kraftstoffgeruch an Schlauch-Aussenseite = hohe Permeation → Austausch.

**KS-011: Muss der Kraftstoffschlauch bei der Bootszulassung (CE) geprueft werden?**
Ja. Bei CE-Zertifizierung muss der Bootsbauer die Konformitaet des Kraftstoffsystems mit ISO 10088 und ISO 7840 nachweisen. Bei Gebrauchtboot-Kauf: CE-Konformitaetserklaerung pruefen, ob Kraftstoffsystem genannt ist.

**KS-012: Kann ich Kraftstoffschlauch reparieren oder nur austauschen?**
Reparatur (Notfall-Tape, Muffen) ist NUR als temporaere Notloesung auf See zulaessig. Fuer die dauerhafte Instandsetzung gilt: IMMER kompletten Schlauch zwischen zwei festen Anschlusspunkten austauschen. Reparierte Schlaeuche sind nicht zulassungsfaehig.

**KS-013: Wie lagere ich Ersatz-Kraftstoffschlaeuche richtig?**
Dunkel, trocken, 10–25 °C, keine Ozon-Quellen (Elektromotoren), nicht knicken. In Originalverpackung oder schwarzer PE-Tuete. Max. Lagerzeit: NBR 5 Jahre, FKM 8 Jahre (ab Produktionsdatum, nicht ab Kaufdatum). DIN 7716 / ISO 2230 beachten.

**KS-014: Ethanol E10 — muss ich alle Schlaeuche tauschen?**
Bei Schlaeuchen vor 2010 ohne E10-Zulassung: JA, dringend empfohlen. Bei ISO 7840 A1 (ab 2010er Revision): Pruefung auf E10-Bestaendigkeit ist im Standard enthalten. Im Zweifel: Hersteller kontaktieren oder auf FKM umruesten.

**KS-015: Was ist der Unterschied zwischen Kraftstoffschlauch und Kraftstoffleitung?**
Kraftstoffschlauch = flexibles Elastomer-Bauteil fuer bewegliche Verbindungen (Motor-Schwingung, Tankbewegung). Kraftstoffleitung = starres Rohr (Kupfer-Nickel, 316L) fuer feste Strecken. Kombiniert: Starre Leitung fuer lange Strecken, flexible Schlaeuche nur an Uebergaengen.

---

## Glossar

| Begriff | Definition |
|---------|-----------|
| ABYC | American Boat and Yacht Council — US-Normenorganisation fuer Bootsbau |
| A1 (ISO 7840) | Brandbestaendige Klasse: Schlauch widersteht 2,5 min offener Flamme ohne Durchbrennen |
| A2 (ISO 7840) | Flammenverzoegernde Klasse: geringerer Brandschutz als A1 |
| Anziehdrehmoment | Kraft × Hebelarm (Nm), mit der eine Schlauchschelle angezogen wird |
| Arrhenius-Gleichung | Temperatur-Lebensdauer-Beziehung: Lebensdauer halbiert sich pro 10 °C Temperaturanstieg |
| Barb (Stutzen-Barb) | Widerhaken-foermige Rillen am Rohrstutzen, die den Schlauch mechanisch halten |
| Biegeradius | Minimaler Kurvenradius, ohne den Schlauch zu beschaedigen oder den Durchfluss einzuschraenken |
| Biodiesel (FAME) | Fettsaeure-Methylester, pflanzlich basierter Dieselersatz (B7 = 7% FAME) |
| Bilge | Tiefster Punkt im Bootsrumpf, in dem sich Wasser und Fluessigkeiten sammeln |
| CE-Kennzeichnung | Europaeische Konformitaetskennzeichnung gemaess Richtlinie 2013/53/EU |
| Crazing | Feine Oberflaechenrissbildung in Elastomeren, meist durch UV oder Ozon |
| Delamination | Trennung der Schichtverbindung zwischen Innenseele und Gewebeeinlage |
| Doppelschelle | Zwei nebeneinander montierte Schlauchschellen fuer redundante Sicherung |
| Durometer (Shore A) | Messgeraet/Einheit fuer die Haerte von Elastomeren (0 = weich, 100 = hart) |
| E10 | Ottokraftstoff mit 10 % Ethanol-Anteil (EU-Standard seit 2011) |
| E85 | Kraftstoff mit 85 % Ethanol, 15 % Benzin (fuer Flex-Fuel-Motoren) |
| EPDM | Ethylen-Propylen-Dien-Monomer — Elastomer fuer Kuehlwasser, NICHT fuer Kraftstoff |
| FDA | US Food and Drug Administration — Zulassungsbehoerde, relevant fuer Trinkwasserschlaeuche |
| FKM (Viton) | Fluorelastomer — hochbestaendig gegen Kraftstoffe, Oele, hohe Temperaturen (bis 200 °C) |
| GFK/FRP | Glasfaserverstaerkter Kunststoff / Fibre Reinforced Plastic |
| Hagen-Poiseuille | Stroemungsgleichung fuer laminare Stroemung in Rohren/Schlaeuchen |
| Hydrolyse | Chemische Zersetzung durch Wasser, betrifft Polyester-Verstaerkungen |
| IMO | International Maritime Organization — UN-Schifffahrtsbehoerde |
| ISO 7840 | Internationale Norm fuer Kraftstoffschlaeuche in Booten (Feuerbestaendigkeit, Materialanforderungen) |
| ISO 10088 | Internationale Norm fuer fest eingebaute Kraftstoffsysteme in Sportbooten |
| Kavitation | Dampfblasenbildung bei zu hohem Unterdruck in der Saugleitung |
| LEL | Lower Explosive Limit — untere Explosionsgrenze eines Kraftstoffdampf-Luft-Gemischs |
| MACT | Maximum Achievable Control Technology — EPA-Emissionsstandard |
| NBR | Nitrilkautschuk (Acrylnitril-Butadien-Gummi) — Standard-Kraftstoffschlauch-Material |
| Ozon-Rissbildung | Quergelaufene Risse durch Ozon-Angriff auf ungesaettigte Elastomere |
| Permeation | Durchdringung von Kraftstoffdaempfen durch die Schlauchwand |
| PTFE | Polytetrafluorethylen (Teflon) — hoechste Chemikalienbestaendigkeit |
| Quellung | Volumenvergroesserung eines Elastomers durch Absorption von Kraftstoff |
| Racor | Markenname fuer weit verbreitete Dieselfilter/Wasserabscheider (Parker Hannifin) |
| SAE J1527 | US-Norm fuer Marine-Kraftstoffschlaeuche (parallel zu ISO 7840) |
| Shore A | Haerteskala fuer Elastomere (ASTM D2240). Neuer NBR-Kraftstoffschlauch: 60–70 Shore A |
| Spaltkorrosion | Korrosion in engen Spalten (z.B. unter Schlauchschelle), wo Sauerstoff-Verarmung auftritt |
| SFC | Specific Fuel Consumption — spezifischer Kraftstoffverbrauch (g/kWh) |
| Siphon-Effekt | Unkontrollierter Kraftstofffluss durch Hebereffekt bei Tank ueber Motorniveau |
| T-Bolt-Schelle | Hochleistungs-Schlauchschelle mit T-Bolzen fuer gleichmaessige Klemmkraft |
| Thermische Sicherung | Schmelz-/Bimetall-Ventil, das bei Hitze (105 °C) die Kraftstoffleitung absperrt |
| USCG | United States Coast Guard — US-Kuestenwache (Regulierungsbehoerde fuer Bootsausstattung) |
| Viton | Handelsname (DuPont/Chemours) fuer FKM-Fluorelastomere |
| Weichmacher-Migration | Auswandern von Weichmachern an die Schlauchoberflaeche bei Alterung |

---

## Schnell-Referenz & Quick-Lookup Index

| Thema | Abschnitt | Schluessel-Info |
|-------|----------|----------------|
| Welcher Schlauchtyp? | Typen fuer Kraftstoff-Anwendungen | Benzin = ISO 7840 A1, Diesel innen = A1, Diesel aussen = A2 min. |
| Doppelschelle wo? | Doppelschlauchschellen — Wann Pflicht? | Tank, Filter, Motor, Ventil (7 Positionen) |
| Anziehdrehmoment? | Anziehdrehmomente | 1,0–10,0 Nm je nach ID und Bandbreite |
| Welches Material? | Permeations-Rate Diesel vs Benzin | NBR fuer Diesel OK, FKM fuer Benzin E10 Pflicht |
| Biegeradius? | Mindest-Biegeradius nach Schlauch-ID | ID × 5 (A1) bis ID × 8 (SAE J1527) |
| Lebensdauer? | NBR/FKM-Schlauch Lebensdauer | NBR: 5–10 J., FKM: 8–18 J. |
| Brandschutz? | Brandschutz-Integration | Min. 100 mm zu Abgas, Hitzeschutz-Wicklung |
| Kosten? | Vergleich Material-Kosten pro Meter | NBR 4,50–11 EUR/m, FKM 18–42 EUR/m |
| Notfall? | Notfall-Reparatur auf offener See | Motor AUS → Ventil ZU → Lokalisieren → Reparaturband/Notstutzen |
| AYDI-Score? | Fehlerbild-Atlas | 5/100 (Abrutschen, Thermisch) bis 55/100 (leichtes Crazing) |

---

## Notfall-Ressourcen & Kontakte

| Dienst | Kontakt | Verfuegbarkeit |
|--------|---------|---------------|
| Deutsche Gesellschaft zur Rettung Schiffbruechiger (DGzRS) | UKW Kanal 16 / Tel. +49 421 53 707 0 | 24/7 |
| MRCC Bremen (Maritime Rescue Coordination Centre) | UKW Kanal 16 / +49 421 53 687 0 | 24/7 |
| Feuerwehr (Hafen-/Yachthafenbraende) | 112 | 24/7 |
| BSU — Bundesstelle fuer Seeunfalluntersuchung | +49 40 3190 8300 | Mo–Fr 08–17 |
| Vergiftungs-Notruf (Kraftstoffdaempfe) | +49 30 192 40 (Berlin) | 24/7 |
| ADAC Sportschifffahrt (Pannenhilfe) | +49 89 7676 7676 | Saisonabhaengig |
| Lloyds Register — Marine Survey | +44 20 7709 9166 | Mo–Fr |
| DNV GL — Marine Survey Deutschland | +49 40 36149-0 | Mo–Fr |

---

## ANHANG A: Cross-Reference-Tabelle OEM zu Aftermarket

| OEM-Motor | OEM-Teilenummer | Schlauch-ID (mm) | Aftermarket-Aequivalent | Aftermarket-Preis (EUR/m) | Kompatibilitaet |
|-----------|----------------|-----------------|------------------------|--------------------------|----------------|
| Volvo Penta D2-40 | 3809855 | 10 | Trident 327 #102-0580 | 14,50 | 100 % |
| Volvo Penta D4/D6 | 3812520 | 12 | Shields 350-1200 | 18,20 | 100 % |
| Yanmar 3JH5E | 129470-59350 | 8 | Trident 327 #102-0380 | 12,80 | 100 % |
| Yanmar 4JH5E | 129670-59380 | 10 | Continental MFH-A1 10mm | 14,50 | 100 % |
| Mercury 150 EFI | 32-861128 | 8 (5/16") | Parker/Gates E85 8mm | 16,00 | 95 % (Adapter) |
| Mercury V8 300 | 32-8M0082289 | 10 (3/8") | Trident 365 E85 3/8" | 18,50 | 100 % |
| MerCruiser 4.5L MPI | 32-8M0082289 | 10 | Shields 350-1000 | 15,20 | 100 % |
| Caterpillar C7 Marine | 1780863 | 16 | Continental MFH-A1 16mm | 22,00 | 100 % |
| Caterpillar C12 Marine | 2W9082 | 19 | Trident 327 #102-0780 | 25,50 | 100 % |
| MAN D2862 | 51.96210-0468 | 19 | Continental MFH-A1 19mm | 28,00 | 95 % |
| MTU 8V2000 M96 | X00041989 | 25 | PTFE-Wellschlauch 316L 25mm | 42,00 | 90 % (Adapter) |
| Cummins QSB 6.7 | 3957290 | 12 | Shields 350-1200 | 18,20 | 100 % |
| John Deere 6068 | RE527963 | 16 | Trident 327 #102-0680 | 22,00 | 100 % |
| Steyr SE236 | 2176400402-4 | 10 | Continental MFH-A1 10mm | 14,50 | 100 % |
| Nanni T4.155 | 970312161 | 10 | Trident 327 #102-0580 | 14,50 | 100 % |

---

## ANHANG B: ISO 7840 Brandtest-Vergleich aller Hersteller

| Hersteller | Produkt | ISO-Klasse | Flammenzeit bis Durchbrennen (s) | Nachbrennzeit (s) | Tropfenbildung | Rauchentwicklung | Ergebnis |
|-----------|--------|-----------|--------------------------------|-------------------|---------------|-----------------|---------|
| Trident Marine | 327 Series | A1 | > 150 (kein Durchbrennen) | 8 | Keine | Gering | BESTANDEN |
| Trident Marine | 365 E85 | A1 | > 150 | 5 | Keine | Gering | BESTANDEN |
| Shields Rubber | 350 Series | A1 | > 150 | 12 | Keine | Mittel | BESTANDEN |
| Continental | MFH-A1 | A1 | > 150 | 6 | Keine | Gering | BESTANDEN |
| Vetus | FHDI (Diesel) | A1 | > 150 | 15 | Keine | Mittel | BESTANDEN |
| Vetus | FHPE (Benzin) | A1 | > 150 | 10 | Keine | Gering | BESTANDEN |
| Parker/Gates | Marine Fuel | A1 | > 150 | 18 | Minimal | Mittel | BESTANDEN |
| NoName China Import | "ISO 7840" | A2 (beansprucht A1) | 85–110 | 45+ | JA (brennend) | Stark | DURCHGEFALLEN |
| Dayco Marine | Fuel Line | A1 | > 150 | 14 | Keine | Mittel | BESTANDEN |
| Sierra Marine | 18-8050 | A1 | > 150 | 11 | Keine | Gering | BESTANDEN |

**AYDI-Warnung:** Bei Schlaeuchen ohne nachpruefbares Zertifikat (insbesondere Direktimport ohne CE-Kennzeichnung) ist davon auszugehen, dass der Brandtest NICHT bestanden wurde. Score: 10/100, KRITISCH.

---

## ANHANG C: Mindest-Biegeradien nach ID

| Schlauch-ID (mm) | ISO 7840 A1 (mm) | ISO 7840 A2 (mm) | SAE J1527 R2 (mm) | Empfohlener Praxis-Radius (mm) |
|-------------------|-------------------|-------------------|---------------------|-------------------------------|
| 5 | 25 | 30 | 38 | 50 |
| 6 | 30 | 36 | 45 | 60 |
| 8 | 40 | 50 | 64 | 80 |
| 10 | 50 | 65 | 76 | 100 |
| 12 | 60 | 75 | 89 | 120 |
| 16 | 85 | 100 | 127 | 160 |
| 19 | 100 | 120 | 152 | 200 |
| 25 | 130 | 160 | 203 | 260 |
| 32 | 170 | 200 | 254 | 340 |
| 38 | 200 | 240 | 305 | 400 |
| 50 | 260 | 310 | 381 | 500 |

**Praxis-Empfehlung:** Den empfohlenen Praxis-Radius (2× ISO-Minimum) verwenden. Dies gibt Sicherheitsmarge und verlaengert die Schlauch-Lebensdauer um ca. 30 %.

---

## ANHANG D: Confidence-Mapping fuer AYDI-Module

| Eingabequelle | Confidence-Level | Code | AYDI-Modul |
|--------------|-----------------|------|-----------|
| Herstellerdatenblatt mit Zertifikat | Measured | `measured` | materials, compliance |
| Physische Messung (Shore A, Wandstaerke) | Measured | `measured` | materials, structural |
| CAD-Daten mit Schlauchdurchmesser/-verlegung | Measured | `measured` | ergonomics, volume |
| Foto: Schlauchtyp + Schelle erkennbar | Visual High | `visual_high` | materials, production |
| Foto: Schlauchzustand gut sichtbar | Visual Medium | `visual_medium` | materials |
| Foto: Maschinenraum uebersicht, Details schwer erkennbar | Visual Low | `visual_low` | materials |
| Nutzer-Eingabe: Bootstyp, Baujahr, Motor | Estimated | `estimated` | alle Module |
| Branchenstatistik (z.B. typischer Schlauchzustand nach 8 Jahren) | Benchmark | `benchmark` | materials, cost |
| Service-Bericht: "Kraftstoffschlaeuche 2022 getauscht" | Documented | `documented` | materials, service_patterns |

---

## ANHANG E: Bordausstattung — Empfohlene Ersatzteile

**Kuestenfahrt (CE Kategorie C/D):**

| Nr. | Teil | Spezifikation | Menge | Preis (EUR) |
|-----|------|--------------|-------|-------------|
| 1 | Kraftstoffschlauch (passende ID) | ISO 7840 A1 | 500 mm | 8–15 |
| 2 | Doppelschlauchschellen (316L) | Passend fuer ID | 4 Stueck | 12–20 |
| 3 | Messing-Geradenverbinder | Passend fuer ID | 1 Stueck | 5–8 |
| 4 | Notfall-Reparaturband | Silikon-selbstverschweissend | 1 Rolle (3 m) | 5–8 |
| 5 | Nitrile-Handschuhe | Kraftstoffbestaendig | 2 Paar | 2–3 |
| **Gesamt** | | | | **32–54** |

**Hochseefahrt (CE Kategorie A/B):**

| Nr. | Teil | Spezifikation | Menge | Preis (EUR) |
|-----|------|--------------|-------|-------------|
| 1 | Kraftstoffschlauch (passende ID) | ISO 7840 A1 | 1000 mm | 15–30 |
| 2 | Kraftstoffschlauch (zweite gaengige ID) | ISO 7840 A1 | 500 mm | 8–15 |
| 3 | Doppelschlauchschellen (316L, 2 Groessen) | Passend | 8 Stueck | 24–40 |
| 4 | Messing-Geradenverbinder | 2 Groessen | 2 Stueck | 10–16 |
| 5 | 90°-Winkelanschluss (Messing) | Passend | 1 Stueck | 8–12 |
| 6 | Racor-Ersatzfilter | Passend fuer Bordfilter | 2 Stueck | 20–40 |
| 7 | Notfall-Reparaturband | Silikon | 2 Rollen | 10–16 |
| 8 | PTFE-Gewindedichtband (Fuel-Grade) | 12 mm × 12 m | 1 Rolle | 3–5 |
| 9 | Absaugpumpe (manuell) | Oelfeste Membrane | 1 Stueck | 25–45 |
| 10 | Oelbinde-Kit | 10 Tuecher + Auffangsack | 1 Kit | 15–25 |
| 11 | Nitrile-Handschuhe | Kraftstoffbestaendig | 4 Paar | 4–6 |
| **Gesamt** | | | | **142–250** |

---

## ANHANG F: Fallstudien

### Fallstudie 1: Segelyacht Bavaria 40 — Kraftstoffgeruch nach E10-Umstellung

- **Boot:** Bavaria 40 Cruiser, Bj. 2008, Volvo Penta D2-40, Diesel
- **Problem:** Nach Betankung mit Diesel B7 (7 % Biodiesel) zunehmender Kraftstoffgeruch im Maschinenraum
- **Untersuchung:** Schlaeuche (Original NBR, 10 Jahre alt) zeigten Shore-A 52 (Neu: 65), Innenwand klebrig, Quellung +12 %
- **Ursache:** Biodiesel-Anteil (FAME) greift alternden NBR-Schlauch an, Weichmacher-Extraktion + Quellung
- **Massnahme:** Kompletter Austausch auf Continental MFH-A1 (FKM-Innenlage), 5,2 m Schlauch, 14 Doppelschellen
- **Kosten:** Material 185 EUR, Arbeitszeit 4 h (DIY)
- **AYDI-Score vorher:** 25/100 (Permeation + Quellung)
- **AYDI-Score nachher:** 92/100

### Fallstudie 2: Motorboot Bayliner 285 — Schlauch vom Tankstutzen abgerutscht

- **Boot:** Bayliner 285, Bj. 2012, MerCruiser 4.5L MPI, Benzin
- **Vorfall:** Schlauch am Tankstutzen waehrend Fahrt abgerutscht, ca. 15 l Benzin in Bilge gelaufen
- **Ursache:** Einzelschelle (Kuehlwasser-Typ, perforiert, verzinkter Stahl), korrodiert, nur 0,8 Nm Restspannkraft
- **Folgen:** Benzin in Bilge → Bilgenpumpe gefoerdert → Benzin-Wasser-Gemisch ueber Bord (Umweltschaden). Kein Brand nur durch Zufall
- **Massnahme:** 316L Doppelschellen an allen 7 Pflichtpositionen, Schlauch auf Trident 365 E85 umgeruestet
- **Kosten:** Material 320 EUR, Werkstatt 540 EUR (6 h), Bussgeld Umweltverschmutzung 2.500 EUR
- **AYDI-Score vorher:** 5/100 (KRITISCH — korrodierte Einzelschelle, Benzin)
- **AYDI-Score nachher:** 95/100

### Fallstudie 3: Superyacht Sunseeker 75 — Brandschaden im Maschinenraum

- **Boot:** Sunseeker 75, Bj. 2005, MAN V12-1550, Diesel
- **Vorfall:** Brand im Maschinenraum waehrend Manoevrieren im Hafen. Loeschanlage (FM-200) hat Brand geloescht
- **Ursache:** Kraftstoff-Ruecklaufschlauch (NBR, 18 Jahre alt) lag auf Turbolader-Gehaeuse (Temperatur > 300 °C), thermische Degradation, Rissbildung, Dieselaustritt auf heisse Oberflaeche
- **Folgen:** Brandschaden ca. 85.000 EUR, 3 Monate Werftaufenthalt, Versicherungsfall
- **Massnahme:** Komplette Neuverlegung aller Kraftstoffleitungen (PTFE-Wellschlauch 316L), Hitzeschutzwicklung, thermische Absperrventile
- **Kosten Instandsetzung:** 47.000 EUR (nur Kraftstoffsystem), 85.000 EUR (Gesamtbrandschaden)
- **AYDI-Score vorher:** 5/100 (Kontakt mit heisser Oberflaeche)
- **AYDI-Score nachher:** 98/100

### Fallstudie 4: Segelyacht Hallberg-Rassy 43 — Diesel Bug Kontamination

- **Boot:** HR 43, Bj. 2001, Volvo Penta D2-55, Diesel
- **Problem:** Wiederholte Racor-Filterverstopfung (alle 20–30 Betriebsstunden), schwarzer Schleim im Filter
- **Untersuchung:** Kraftstoffprobe: trueb, Bodensatz. Schlauch-Innenwand: schwarzer Biofilm, NBR angegriffen (Biokorrosion)
- **Ursache:** Condensation im halbvollen Tank ueber 3 Winter → Wasser-Diesel-Grenzschicht → Hormoconis resinae Wachstum → Biofilm im Tank und Schlauch
- **Massnahme:** Tank professionell reinigen (Schlaemmung), alle Schlaeuche austauschen (FKM), Biozid Grotamar 82 einmalig 1:2000, kuenftig 1:4000 jaehrlich
- **Kosten:** Tankreinigung 650 EUR, Schlaeuche 210 EUR, Biozid 35 EUR/Jahr
- **AYDI-Score vorher:** 30/100 (Biofilm + NBR-Degradation)
- **AYDI-Score nachher:** 88/100

### Fallstudie 5: Fischerboot Rhea 850 — Notfall-Reparatur auf See

- **Boot:** Rhea 850 Timonier, Bj. 2015, Nanni T4.155, Diesel
- **Vorfall:** 12 sm vor der Kueste, Kraftstoff-Vorlaufschlauch (ID 10 mm) an Knickstelle gerissen, Motor ausgefallen
- **Sofortmassnahme:** Ventil geschlossen, Schlauch 50 mm vor/nach Riss abgeschnitten, Messing-Geradenverbinder eingesetzt, 4× 316L-Schellen, Motor lief nach 25 min wieder
- **Hafen-Reparatur:** Kompletter Schlauch ersetzt, Verlegung mit 90°-Winkelanschluss statt Knick
- **Kosten:** Notfall-Material (aus Bordvorrat) 18 EUR, Werft-Austausch 280 EUR
- **AYDI-Score vorher:** 15/100 (Knick + Riss)
- **AYDI-Score nachher:** 90/100
- **Lektion:** Bordvorrat mit Ersatzschlauch + Verbinder hat moeglicherweise Boot/Leben gerettet

### Fallstudie 6: Charterkatamaran Lagoon 42 — Versicherungsablehnung

- **Boot:** Lagoon 42, Bj. 2018, 2× Yanmar 4JH5E, Diesel
- **Problem:** Versicherung lehnt Schadensregulierung ab nach Motorschaden (Kraftstoffmangel durch gequollenen Schlauch)
- **Hintergrund:** Charterfirma hatte bei Wartung guenstige NBR-Schlaeuche (ISO 7840 A2, nur Diesel-aussen) in den Maschinenraum eingebaut
- **Versicherungs-Argument:** Falsche Schlauchklassifikation (A2 statt A1 fuer Inneneinbau), Verstoss gegen ISO 10088
- **Folge:** 12.000 EUR Motorschaden nicht gedeckt, Charterfirma traegt Kosten
- **Massnahme:** Umruestung beider Motoren auf ISO 7840 A1, Dokumentation fuer Versicherung
- **AYDI-Score vorher:** 35/100 (falsche Klassifikation)
- **AYDI-Score nachher:** 92/100

### Fallstudie 7: Oldtimer-Yacht Riva Aquarama — Benzin-System Restaurierung

- **Boot:** Riva Aquarama Special, Bj. 1972, 2× Riva-modifizierte V8, Benzin
- **Herausforderung:** Original-Kraftstoffschlaeuche (50+ Jahre, unbekanntes Material) muessen unter Erhalt der Authentizitaet ersetzt werden
- **Loesung:** PTFE-Glattschlauch mit 316L-Edelstahl-Geflecht, aussenseitig mit schwarzer Gummi-Ummantelung (optisch wie Original)
- **Besonderheit:** Benzinsystem erfordert ISO 7840 A1 + niedrige Permeation. PTFE einzige Option, die Sicherheit + Optik vereint
- **Kosten:** Material 680 EUR (6 m PTFE-Schlauch + Fittings), Restaurateur 1.800 EUR (12 h Spezialist)
- **AYDI-Score vorher:** 5/100 (50 Jahre alter unbekannter Schlauch, Benzin)
- **AYDI-Score nachher:** 97/100

### Fallstudie 8: Patrol Boat — DNV-Klassifikation Audit-Befund

- **Boot:** 24-m-Aluminium-Patrolboot, Bj. 2020, 2× Caterpillar C18, Diesel
- **Audit-Befund:** DNV-Surveyor beanstandet fehlende thermische Absperrventile an Kraftstoffleitungen im Maschinenraum (DNV Rules Pt.6 Ch.5 Sec.5)
- **Massnahme:** 4× thermische Absperrventile (Fusible Link, 105 °C) nachgeruestet, Feuerwiderstandspruefung dokumentiert
- **Kosten:** 4× Ventile 360 EUR, Einbau 480 EUR, DNV-Folgeaudit 1.200 EUR
- **Zeitdruck:** Ohne Nachbesserung drohte Entzug der Klassifikation (= Betriebsverbot)
- **AYDI-Score vorher:** 40/100 (fehlende thermische Sicherung)
- **AYDI-Score nachher:** 95/100

---

## ANHANG G: Experten-Stimmen und Literatur

**Fachliteratur:**

| Nr. | Titel | Autor/Verlag | Jahr | Relevanz |
|-----|-------|-------------|------|---------|
| 1 | "Boatowner's Mechanical and Electrical Manual" | Nigel Calder, International Marine | 2015 (4. Aufl.) | Kap. 8: Fuel Systems — Standardwerk |
| 2 | "Marine Diesel Engines" | Nigel Calder, International Marine | 2006 | Kraftstoffsystem-Diagnose |
| 3 | "The 12-Volt Bible for Boats" | Miner Brotherton, International Marine | 2002 | Elektrische Integration Kraftstoffpumpen |
| 4 | "Surveying Fiberglass Sailboats" | Henry Mustin, International Marine | 1994 | Kraftstoffsystem-Inspektion bei Kaufgutachten |
| 5 | "Elastomere Werkstoffe" (Fachbuch) | Rolf-Juergen Zimmer, Carl Hanser Verlag | 2018 | Material-Grundlagen NBR, FKM, EPDM |
| 6 | ISO 7840:2020 "Small craft — Fire-resistant fuel hoses" | ISO | 2020 | Norm-Volltext |
| 7 | ISO 10088:2017 "Small craft — Permanently installed fuel systems" | ISO | 2017 | Norm-Volltext |
| 8 | ABYC H-24 "Gasoline Fuel Systems" | ABYC | 2021 | US-Standard Benzin-Kraftstoffsystem |
| 9 | ABYC H-33 "Diesel Fuel Systems" | ABYC | 2021 | US-Standard Diesel-Kraftstoffsystem |
| 10 | "Rubber Technology Handbook" | Werner Hofmann, Carl Hanser Verlag | 2012 | Alterungsmechanismen, Permeation |

---

## ANHANG H: Risk Assessment Matrix

| Risiko | Wahrscheinlichkeit (1–5) | Auswirkung (1–5) | Risiko-Score (W×A) | Prioritaet | Mitigationsmassnahme |
|--------|--------------------------|-------------------|--------------------|-----------|---------------------|
| Schlauch-Abrutschen (Benzin) | 2 | 5 | 10 | KRITISCH | Doppelschellen, korrekte Einschubtiefe |
| Thermische Degradation → Brand | 2 | 5 | 10 | KRITISCH | Abstandsregel, Hitzeschutz, thermische Absperung |
| Permeation → Explosionsgefahr (Benzin) | 3 | 5 | 15 | KRITISCH | FKM/PTFE statt NBR, LEL-Ueberwachung |
| Schlauchbruch an Knickstelle | 3 | 4 | 12 | HOCH | Biegeradius einhalten, Stuetzboegen |
| Schellenkorrosion → Leckage | 3 | 3 | 9 | MITTEL | 316L-Schellen, Inspektionsintervall |
| Quellung durch E10/Biodiesel | 3 | 3 | 9 | MITTEL | FKM-Schlauch, Materialkompatibilitaet pruefen |
| Diesel Bug → Filterverstopfung | 2 | 3 | 6 | NIEDRIG | Tank voll halten, Biozid, Wasserabscheider |
| Weichmacher-Migration | 2 | 2 | 4 | NIEDRIG | FKM-Schlauch, Inspektionsintervall |

---

## ANHANG I: Audit/Compliance Standards

**Checkliste fuer Kraftstoffsystem-Audit (basierend auf ISO 10088:2017):**

| Nr. | Pruefpunkt | Norm-Referenz | Bewertung | AYDI-Scoring |
|-----|-----------|--------------|-----------|-------------|
| 1 | Kraftstoffschlauch-Zertifizierung (ISO 7840 A1/A2) | ISO 10088 Abschn. 5.1 | Ja/Nein/Nicht pruefbar | Nein = 15/100 |
| 2 | Doppelschellen an allen Pflichtpositionen | ISO 10088 Abschn. 7.3 | Ja/Nein | Nein = 20/100 |
| 3 | Schellen-Material 316L | ISO 10088 Abschn. 7.3 | Ja/Nein | Nein = 25/100 |
| 4 | Mindest-Biegeradius eingehalten | ISO 7840 Abschn. 8.2 | Ja/Nein | Nein = 25/100 |
| 5 | Mindestabstand zu Waermequellen (50 mm) | ISO 9094 Abschn. 6 | Ja/Nein | Nein = 5/100 |
| 6 | Hitzeschutz bei < 100 mm Abstand | ISO 9094 Abschn. 6 | Ja/Nein | Fehlt = 15/100 |
| 7 | Kraftstoff-Absperrventil am Tank | ISO 10088 Abschn. 6.2 | Ja/Nein | Nein = 20/100 |
| 8 | Anti-Siphon-Vorrichtung (wenn Tank ueber Motor) | ISO 10088 Abschn. 6.5 | Ja/Nein/n.a. | Nein = 30/100 |
| 9 | Kraftstoff-Tankbelueftung korrekt | ISO 10088 Abschn. 6.8 | Ja/Nein | Nein = 25/100 |
| 10 | Schlaeuche ohne sichtbare Schaeden | Allg. Sorgfaltspflicht | Gut/Maessig/Schlecht | Schlecht = 15-35/100 |
| 11 | Dokumentation/Servicebuch vorhanden | Best Practice | Ja/Nein | Nein = 60/100 |
| 12 | Alter der Schlaeuche dokumentiert | Best Practice | Ja/Nein | Nein = 55/100 |

---

## ANHANG J: Material-Datenblaetter

### NBR (Nitrilkautschuk) — Typische Werte fuer Marine-Kraftstoffschlauch

| Eigenschaft | Wert | Pruefnorm |
|-------------|------|----------|
| Shore A Haerte | 60–70 | ASTM D2240 |
| Zugfestigkeit | 10–18 MPa | ASTM D412 |
| Bruchdehnung | 250–400 % | ASTM D412 |
| Temperaturbereich | -30 °C bis +100 °C | — |
| Berstdruck (ID 10 mm) | 25–40 bar | ISO 7840 |
| Betriebsdruck max. | 3,5–10 bar (abh. ID) | ISO 7840 |
| Dichte | 1,25–1,40 g/cm³ | ASTM D297 |
| Ozonbestaendigkeit | Maessig (ASTM D1149: Risse nach 100 h bei 50 pphm) | ASTM D1149 |
| Kraftstoffbestaendigkeit | Gut (Diesel), Maessig (Benzin), Schlecht (E85) | ASTM D471 |
| Quellung in Diesel (70 h, 23 °C) | 5–15 % Vol. | ASTM D471 |
| Quellung in Benzin (70 h, 23 °C) | 20–40 % Vol. | ASTM D471 |

### FKM/Viton (Fluorelastomer) — Typische Werte

| Eigenschaft | Wert | Pruefnorm |
|-------------|------|----------|
| Shore A Haerte | 65–80 | ASTM D2240 |
| Zugfestigkeit | 8–15 MPa | ASTM D412 |
| Bruchdehnung | 150–300 % | ASTM D412 |
| Temperaturbereich | -20 °C bis +200 °C | — |
| Berstdruck (ID 10 mm) | 30–50 bar | ISO 7840 |
| Betriebsdruck max. | 5–16 bar (abh. ID) | ISO 7840 |
| Dichte | 1,80–2,00 g/cm³ | ASTM D297 |
| Ozonbestaendigkeit | Ausgezeichnet (> 1000 h bei 100 pphm, keine Risse) | ASTM D1149 |
| Kraftstoffbestaendigkeit | Ausgezeichnet (Diesel, Benzin, E10, Biodiesel) | ASTM D471 |
| Quellung in Diesel (70 h, 23 °C) | 1–3 % Vol. | ASTM D471 |
| Quellung in Benzin (70 h, 23 °C) | 2–8 % Vol. | ASTM D471 |
| Quellung in E85 (70 h, 23 °C) | 5–15 % Vol. | ASTM D471 |

---

## ANHANG K: Pruef-/Testverfahren

### Verfahren 1: Shore-A-Haertemessung (Vor-Ort)

| Schritt | Beschreibung |
|---------|-------------|
| 1 | Durometer (Typ Shore A, ASTM D2240) verwenden |
| 2 | Schlauch flach auf feste Unterlage legen |
| 3 | Durometer senkrecht aufsetzen, 3 s warten |
| 4 | Messung an 3 Stellen: nahe Schelle, Mitte, am anderen Ende |
| 5 | Mittelwert bilden |
| 6 | Vergleich: Neuwert 60–70 (NBR), 65–80 (FKM). >85 = Austausch empfohlen |

### Verfahren 2: Biegetest (Vor-Ort)

| Schritt | Beschreibung |
|---------|-------------|
| 1 | Schlauch an freiem Stueck (nicht am Stutzen) in der Hand um 90° biegen |
| 2 | Loslassen und Rueckfederung beobachten |
| 3 | Federt sofort zurueck = OK (Score 70–100) |
| 4 | Federt langsam zurueck = Frühwarnung (Score 40–60) |
| 5 | Bleibt verformt / knickt = Austausch (Score 10–30) |
| 6 | Risse sichtbar beim Biegen = Sofort-Austausch (Score 5/100) |

### Verfahren 3: Lecksuch-Pruefung mit UV-Additiv

| Schritt | Beschreibung |
|---------|-------------|
| 1 | UV-Tracerfluid (z.B. Spectroline OLF-H) dem Kraftstoff zusetzen (1:500) |
| 2 | Motor 30 min laufen lassen |
| 3 | Alle Verbindungen mit UV-Lampe (365 nm) beleuchten |
| 4 | Fluoreszenz = Leckstelle. Auch Mikrolecks sichtbar |
| 5 | Leckstellen markieren und beheben |

### Verfahren 4: Drucktest (Werkstatt)

| Schritt | Beschreibung |
|---------|-------------|
| 1 | Schlauchstueck beidseitig mit Blindflansch/Stopfen verschliessen |
| 2 | Mit Handpumpe auf 1,5× Betriebsdruck (max. 10 bar fuer Standard-Schlauch) bringen |
| 3 | 15 min halten |
| 4 | Druckabfall < 0,5 bar/15 min = dicht |
| 5 | Druckabfall > 0,5 bar = undicht → Schlauch verwerfen |

---

## ANHANG L: Top 15 Design-Fehler mit AYDI-Bewertung

| Nr. | Design-Fehler | AYDI-Score | Haeufigkeit | Konsequenz |
|-----|--------------|-----------|-------------|-----------|
| 1 | Kraftstoffschlauch direkt auf Abgaskruemmer | 5/100 | 3 % | Brandgefahr, sofortige Korrektur |
| 2 | Einzelschelle am Tankstutzen (Benzin) | 5/100 | 12 % | Abrutschen, Explosionsgefahr |
| 3 | EPDM-Schlauch fuer Kraftstoff verwendet | 10/100 | 5 % | Aufloesung, freier Kraftstoffaustritt |
| 4 | Kein Kraftstoff-Absperrventil am Tank | 15/100 | 8 % | Keine Notabsperrung moeglich |
| 5 | Schlauch durch Bilge verlegt (ungescuetzt) | 20/100 | 10 % | Scheuer-/Tauchschaden, Kontamination |
| 6 | Biegeradius < 50 % des Minimums | 15/100 | 15 % | Knick, Durchflussreduktion, Bruch |
| 7 | Verzinkte Schellen im Kraftstoffsystem | 20/100 | 20 % | Korrosion binnen 1–2 Jahren |
| 8 | Fehlende Tankbelueftung / falsch gefuehrt | 25/100 | 6 % | Ueberdruck/-unterdruck, Tankverformung |
| 9 | Keine Anti-Siphon-Vorrichtung (Tank ueber Motor) | 25/100 | 7 % | Unkontrollierter Kraftstofffluss bei Schlauchbruch |
| 10 | Kraftstoffschlauch als Dauer-Leitung (> 2 m ohne Stuetzung) | 30/100 | 18 % | Durchhang, Knickbildung, Ermuedung |
| 11 | NBR-Schlauch in Benzin-E10-System (post-2011) | 35/100 | 25 % | Quellung, Permeation, vorzeitiger Ausfall |
| 12 | Nicht zugaengliche Schellenverbindung (< 50 mm Freiraum) | 40/100 | 30 % | Inspektion unmoeglich, Wartungsfehler |
| 13 | Fehlende Dokumentation (Schlauchtyp, Einbaudatum) | 50/100 | 55 % | Wartungsplanung unmoeglich |
| 14 | Kraftstofffilter ohne Wasserabscheider | 45/100 | 15 % | Wasser im Motor, Diesel Bug |
| 15 | Fehlende Scheuerschutz-Huelse an Schottdurchfuehrung | 40/100 | 22 % | Abrieb, Leckage |

---

## ANHANG M: Zusammenfassung

**Kernaussagen fuer AYDI-Integration:**

1. **Material bestimmt Sicherheit:** FKM/Viton oder PTFE fuer Benzinsysteme, mindestens NBR-Premium (ISO 7840 A1) fuer Diesel. Kein EPDM fuer Kraftstoff.

2. **Doppelschellen sind Pflicht:** An allen 7 definierten Positionen, ausschliesslich 316L, mit Drehmoment-Kontrolle.

3. **Brandschutz ist die Nr. 1:** Mindestabstand zu heissen Oberflaechen, ISO 7840 A1 fuer Inneneinbau, thermische Absperrventile bei klassifizierten Yachten.

4. **Permeation ist die unsichtbare Gefahr:** LEL-Messung als Standard-Inspektionswerkzeug, FKM statt NBR bei Benzin.

5. **Lebenszykluskosten beachten:** FKM ist trotz 3× hoeherem Anschaffungspreis langfristig wirtschaftlicher als NBR.

6. **Dokumentation ist unverhandelbar:** Einbaudatum, Material, Hersteller, Schellen-Typ — ohne Dokumentation keine zuverlaessige Wartungsplanung.

7. **AYDI-Score spiegelt reale Gefahr:** Score < 30 = akute Handlung erforderlich, Score 30–60 = Wartung planen, Score > 60 = Zustand akzeptabel.

---

## ANHANG N: Spezialanwendungen

### Generatoren und Nebenaggregate

Bordgeneratoren (z.B. Fischer Panda, Onan/Cummins, Kohler) verwenden identische Kraftstoffschlauch-Typen wie Hauptmotoren. Besonderheiten:

| Aspekt | Generator | Hauptmotor |
|--------|----------|-----------|
| Schlauch-ID typisch | 6–10 mm | 10–25 mm |
| Verbrauch | 1–8 l/h | 5–300+ l/h |
| Vibration | Hoch (kompakte Bauweise) | Mittel (elastische Motorlagerung) |
| Zugaenglichkeit | Oft schlecht (enge Kapselung) | Meist gut |
| Inspektions-Prioritaet | HOCH (oft vergessen bei Wartung) | Standard |

**AYDI-Empfehlung:** Generator-Kraftstoffschlaeuche in jede Inspektion einbeziehen. Schadenshaeufigkeit ist proportional hoeher als bei Hauptmotoren (Vibration + Vernachlaessigung).

### Treibstoff-Transfer-Systeme (Mehrtank-Anlagen)

Bei Yachten > 15 m mit mehreren Kraftstofftanks werden Transfer-Schlaeuche zwischen den Tanks eingesetzt:

- Schlauch-ID: typisch 16–25 mm
- Betriebsdruck: 0,5–2 bar (Transfer-Pumpe)
- Besonderheit: Beide Enden unter Kraftstoff-Niveau → kein Luftziehen, aber Siphon-Gefahr
- Anti-Siphon-Ventil: PFLICHT an jedem Tank-Abgang (ISO 10088 Abschn. 6.5)
- Elektromagnetisches Absperrventil: empfohlen (ferngesteuerte Notabschaltung vom Steuerstand)

### Heizungs-Systeme (Webasto, Eberspaecher)

Standheizungen verwenden eigene Kraftstoff-Versorgungsleitungen:

| Aspekt | Wert |
|--------|------|
| Schlauch-ID | 3,5–5 mm (Mikro-Dosierpumpe) |
| Verbrauch | 0,1–0,5 l/h |
| Material | NBR-Premium (ISO 7840 A1) oder Hersteller-Originalschlauch |
| Besonderheit | Dosierpumpe erzeugt Pulsation → Schlauch muss pulsationsfest sein |
| Haeufiger Fehler | Kuehlwasserschlauch (EPDM) fuer Kraftstoffzufuhr verwendet |
| AYDI-Score bei EPDM | 10/100 (KRITISCH) |

---

## ANHANG O: Umwelt/Entsorgung

### Entsorgung alter Kraftstoffschlaeuche

| Schritt | Beschreibung | Vorschrift |
|---------|-------------|-----------|
| 1 | Schlauch vollstaendig entleeren, Restkraftstoff auffangen | AbfallV |
| 2 | Restkraftstoff als Sondermuell entsorgen (AVV 13 07 01*) | KrWG § 17 |
| 3 | Schlauch 24 h an der Luft trocknen lassen | — |
| 4 | Entsorgung als Gummiabfall (AVV 16 01 99) beim Wertstoffhof | KrWG § 17 |
| 5 | Bei groesseren Mengen (Werft): Entsorgungsfachbetrieb beauftragen | KrWG § 54 |
| 6 | NICHT im Restmuell, NICHT verbrennen (toxische Daempfe bei FKM/Viton!) | — |

**FKM/Viton-Warnung:** Bei Verbrennung von Fluorelastomeren entstehen hochgiftige Flusssaeure-Daempfe (HF). FKM-Schlaeuche NIEMALS verbrennen oder thermisch bearbeiten (schleifen, saegen mit Hitze-Entwicklung).

### Umweltbelastung durch Kraftstoff-Leckagen

| Kraftstofftyp | Menge fuer 1 km² Oelfilm | Trinkwasser-Kontamination (l) | Bussgeld (DE) | Bussgeld (Sonderschutzgebiet) |
|---------------|--------------------------|-------------------------------|---------------|------------------------------|
| Diesel | 1 l | 1 l kontaminiert ca. 600.000 l | 500–50.000 EUR | bis 100.000 EUR |
| Benzin | 0,5 l | 1 l kontaminiert ca. 1.000.000 l | 1.000–100.000 EUR | bis 500.000 EUR |
| Schmierstoffe | 2 l | 1 l kontaminiert ca. 200.000 l | 250–25.000 EUR | bis 50.000 EUR |

---

## ANHANG P: Erweiterte FAQ (KS-016 bis KS-025)

**KS-016: Darf ich Messing-Schlauchschellen im Kraftstoffsystem verwenden?**
Nein. Messing (CuZn-Legierungen) ist im Seewasser-Umfeld anfaellig fuer Entzinkung und darf nicht als Schlauchschelle verwendet werden. Ausschliesslich 316L-Edelstahl. Messing-STUTZEN sind zulaessig, wenn sie mit 316L-Schellen kombiniert werden.

**KS-017: Wie unterscheide ich 304 von 316L visuell?**
Visuell nicht unterscheidbar. Pruefmethode: Magnettest — 304 ist leicht magnetisch (wird es durch Kaltverformung staerker), 316L ist nicht-magnetisch. Sicherste Methode: Materialpruefung mit Roentgenfluoreszenz (XRF) oder Materialzertifikat (3.1 nach EN 10204) des Herstellers.

**KS-018: Kann ich PTFE-Schlauch auf Barb-Stutzen montieren?**
PTFE-Glattschlauch: NEIN — PTFE ist zu glatt und steif fuer Barb-Stutzen. PTFE benoetigt spezielle Pressfittings (z.B. Parker 43-Serie, Swagelok). PTFE-Wellschlauch mit Edelstahl-Geflecht: JA, mit speziellen Ueberwurfmuttern-Fittings.

**KS-019: Was passiert bei einem Kraftstoffschlauch-Brand?**
ISO 7840 A1: Schlauch haelt 2,5 min offener Flamme stand, leckt nicht, Flamme erlischt selbst. ISO 7840 A2: Haelt waehrend der 2,5 min, kann danach lecken. Ohne Zertifizierung: Durchbrennen in 20–60 s, freier Kraftstoffaustritt in die Flamme → Eskalation zum Vollbrand.

**KS-020: Muss ich den Kraftstoffschlauch bei der Antriebs-Umruestung (Diesel auf Elektro) entfernen?**
Ja. Bei Entfernung des Verbrennungsmotors muessen alle Kraftstoff fuehrenden Leitungen demontiert werden. Tank-Stilllegung: Kraftstoff entleeren, Tank reinigen (Zertifizierung fuer Gasfrei), Anschluesse blindflanchen.

**KS-021: Wie verhaelt sich Kraftstoffschlauch bei Frost (-20 °C)?**
NBR wird ab -25 °C sproede, FKM ab -15 °C (Standard-FKM) bzw. -40 °C (Tieftemperatur-FKM, z.B. Viton GLT). Winterlager: Schlaeuche mit Kraftstoff gefuellt lassen (Frostschutz durch Kraftstoff selbst). Leere Schlaeuche koennen durch Kondensationswasser + Frost reissen.

**KS-022: Gibt es Kraftstoffschlaeuche mit integrierten Sensoren?**
Ja, in der Entwicklung. Parker Hannifin hat Prototypen mit eingebetteten Dehnungsmessstreifen und Feuchtigkeitssensoren (Projekt "Smart Hose", vorgestellt METS 2024). Marktreife ca. 2026–2027. AYDI wird diese Daten als `measured`-Confidence integrieren.

**KS-023: Wie pruefe ich die Kraftstoffschlauch-Konformitaet beim Gebrauchtboot-Kauf?**
1. Schlauch-Aufdruck lesen (Hersteller, Norm, Datum). 2. Wenn kein Aufdruck lesbar: Shore-A-Messung + Biege-Test. 3. CE-Konformitaetserklaerung des Bootes pruefen. 4. AYDI-Schnellanalyse (Level 1) mit Foto des Maschinenraums. 5. Im Zweifel: Komplett-Austausch einplanen und vom Kaufpreis abziehen.

**KS-024: Was kostet ein komplettes Kraftstoffsystem-Upgrade von NBR auf FKM?**
Richtpreise je nach Bootsgroesse: 8–10 m Segelyacht: 250–500 EUR (Material) + 400–800 EUR (Arbeit). 12–15 m Motoryacht: 500–1.200 EUR + 800–1.800 EUR. 18–24 m Motoryacht: 1.200–3.000 EUR + 2.000–5.000 EUR. Amortisation durch laengere Lebensdauer in 5–8 Jahren.

**KS-025: Welche Versicherungsrabatte gibt es fuer ein zertifiziertes Kraftstoffsystem?**
Direkte Rabatte sind selten. Aber: Ein dokumentiertes, normkonformes Kraftstoffsystem verhindert Leistungsablehnungen im Schadensfall. Manche Versicherer (z.B. Pantaenius, Yacht-Pool) bieten 5–10 % Praemienreduktion bei nachgewiesener jaehrlicher Sicherheitsinspektion inkl. Kraftstoffsystem.

---

## ANHANG Q: Historische Zeitleiste

| Jahr | Ereignis | Auswirkung auf Kraftstoffschlaeuche |
|------|---------|-------------------------------------|
| 1958 | Erste ABYC-Standards veroeffentlicht | Grundlage fuer marine Kraftstoffsystem-Anforderungen |
| 1971 | USCG 33 CFR 183 eingefuehrt | Doppelschellen-Pflicht fuer Benzinsysteme in den USA |
| 1983 | ISO 7840 erstmals veroeffentlicht | Internationale Harmonisierung Brandtest-Anforderungen |
| 1994 | EU-Sportbootrichtlinie 94/25/EG | CE-Kennzeichnung fuer Boote, Kraftstoffsystem als Pruefpunkt |
| 1998 | ISO 10088 erstmals veroeffentlicht | Komplettes Kraftstoffsystem-Design standardisiert |
| 2003 | Viton/FKM-Schlaeuche im Marine-Markt verfuegbar | Alternative zu NBR fuer aggressive Kraftstoffe |
| 2005 | Biodiesel (FAME B5) in EU-Diesel eingefuehrt | Erste Berichte ueber NBR-Quellung durch FAME |
| 2011 | E10 (Super E10) in Deutschland eingefuehrt | Massive Zunahme von NBR-Schaeden in Benzinsystemen |
| 2013 | EU-Sportbootrichtlinie 2013/53/EU (Neufassung) | Verschaerfte Anforderungen an Kraftstoffsysteme |
| 2017 | ISO 10088:2017 (Revision) | Klarere Anforderungen an Schlauchschellen und Anti-Siphon |
| 2020 | ISO 7840:2020 (Revision) | Aktualisierte Brandtest-Verfahren, E10-Bestaendigkeit |
| 2022 | ABYC H-24/H-33 (2021 Revision) | Neue Permeations-Grenzwerte, verschaerfte Schellenanforderungen |
| 2024 | Parker "Smart Hose" Prototyp (METS 2024) | Beginn sensorintegrierter Kraftstoffschlaeuche |
| 2025 | EPA Phase 3 Emissionsstandards | Weitere Senkung zulaessiger Permeationsraten |

---

## ANHANG R: Stichwortverzeichnis

| Stichwort | Abschnitte |
|-----------|-----------|
| 316L Edelstahl | Typen fuer Kraftstoff-Anwendungen, Korrosions-Mechanismen, Glossar |
| ABYC H-24 | USCG/ABYC Anforderungen, Doppelschlauchschellen, Brandschutz-Integration |
| Alterung | Lebensdauer und Alterungsmechanismen, Ethanol-Degradation |
| Anti-Siphon | Spezial-Anleitung Tank-Anschluss, Audit/Compliance |
| Anziehdrehmoment | Anziehdrehmomente, Haeufige Fehler |
| Biegeradius | Mindest-Biegeradius, ANHANG C, Design-Fehler |
| Biodiesel | Ethanol-Degradation, Permeations-Rate |
| Brandschutz | Brandschutz-Integration, ANHANG B, ANHANG H |
| CE-Kennzeichnung | FAQ KS-011, Historische Zeitleiste |
| Crazing | Fehlerbild 1, Alterungsmechanismen |
| Delamination | Fehlerbild 5, Glossar |
| Diesel Bug | Fehlerbild 11, Fallstudie 4, Troubleshooting Problem 5 |
| Doppelschelle | Doppelschlauchschellen Wann Pflicht, Haeufige Fehler |
| Druckverlust | Druckverlust-Berechnung, Troubleshooting Problem 1 |
| Durchfluss | Durchfluss-Berechnungen, Dimensionierungstabelle |
| E10/E85 | Ethanol-Degradation, Permeations-Rate, FAQ KS-014 |
| Einbau | Schritt-fuer-Schritt Austausch, Haeufige Fehler |
| Entsorgung | ANHANG O |
| FKM/Viton | Material-Datenblaetter, Lebensdauer, Kostenvergleich |
| Generator | ANHANG N Spezialanwendungen |
| Hitzeschutz | Brandschutz-Integration, Fehlerbild 7 |
| ISO 7840 | Brandtest-Vergleich, Glossar, Historische Zeitleiste |
| ISO 10088 | Audit/Compliance, USCG/ABYC Anforderungen |
| Kavitation | Durchfluss-Berechnungen, Glossar |
| Korrosion | Korrosions-Mechanismen, Fehlerbild 4 |
| LEL | Werkzeug-Checkliste, Troubleshooting Problem 2, Glossar |
| Leckage | Fehlerbild 6, Notfall-Reparatur, Troubleshooting |
| NBR | Material-Datenblaetter, Lebensdauer, Alterungsmechanismen |
| Notfall | Notfall-Reparatur auf offener See, Notfall-Ressourcen |
| OEM/Aftermarket | ANHANG A Cross-Reference |
| Permeation | Permeations-Rate, Fehlerbild 9, Glossar |
| Predictive Maintenance | Predictive Maintenance Algorithmus |
| PTFE | Material-Datenblaetter, Permeations-Rate, FAQ KS-018 |
| Quellung | Fehlerbild 2, Ethanol-Degradation, Material-Datenblaetter |
| Racor | Spezial-Anleitung Kraftstofffilter, ANHANG A |
| Reparatur | Notfall-Reparatur, FAQ KS-012 |
| Risk Assessment | ANHANG H |
| Schlauchschelle | Schlauchschellen & Verbindungstechnik (gesamt) |
| Shore A | Pruef-/Testverfahren, Material-Datenblaetter |
| Spezialanwendungen | ANHANG N |
| Stutzen | Spezial-Anleitung Tank-Anschluss, Glossar |
| T-Bolt | Typen fuer Kraftstoff-Anwendungen, Anziehdrehmomente |
| Thermische Sicherung | Brandschutz-Integration, Fallstudie 8 |
| Troubleshooting | Fehlerbehebungs-Leitfaden (5 Probleme) |
| USCG | USCG/ABYC Anforderungen, Glossar |
| Werkzeug | Werkzeug-Checkliste |

---

## ANHANG S: Erweiterte Berechnungstabellen

### Kraftstoffverbrauch-Referenztabelle nach Motortyp und Drehzahl

| Motor | Typ | Leistung (kW) | Leerlauf (l/h) | 1500 RPM (l/h) | 2500 RPM (l/h) | 3000 RPM (l/h) | Volllast (l/h) |
|-------|-----|---------------|---------------|----------------|----------------|----------------|---------------|
| Yanmar 1GM10 | Diesel | 6,6 | 0,3 | 0,8 | 1,4 | 1,8 | 2,2 |
| Yanmar 3JH5E | Diesel | 29 | 0,8 | 2,5 | 5,2 | 7,1 | 8,5 |
| Yanmar 4JH5E | Diesel | 39 | 1,0 | 3,2 | 6,8 | 9,5 | 11,4 |
| Volvo Penta D1-30 | Diesel | 21 | 0,6 | 1,8 | 3,8 | 5,2 | 6,3 |
| Volvo Penta D2-40 | Diesel | 29 | 0,8 | 2,4 | 5,0 | 6,9 | 8,3 |
| Volvo Penta D2-75 | Diesel | 55 | 1,2 | 4,0 | 8,5 | 11,8 | 15,5 |
| Volvo Penta D4-260 | Diesel | 191 | 3,5 | 10,5 | 24,0 | 35,0 | 52,0 |
| Volvo Penta D6-370 | Diesel | 272 | 5,0 | 15,0 | 34,0 | 50,0 | 74,0 |
| Caterpillar C7.1 | Diesel | 373 | 6,5 | 18,0 | 42,0 | 62,0 | 98,0 |
| Caterpillar C12.9 | Diesel | 533 | 9,0 | 26,0 | 58,0 | 85,0 | 140,0 |
| MAN D2676 | Diesel | 588 | 10,0 | 28,0 | 64,0 | 94,0 | 155,0 |
| MTU 8V2000 M96 | Diesel | 895 | 14,0 | 42,0 | 95,0 | 140,0 | 235,0 |
| Mercury 150 EFI | Benzin | 112 | 3,5 | n/a | 18,0 | 28,0 | 52,0 |
| Mercury V8 300 | Benzin | 224 | 5,5 | n/a | 32,0 | 52,0 | 95,0 |
| MerCruiser 4.5L MPI | Benzin | 186 | 4,0 | n/a | 25,0 | 42,0 | 78,0 |

**Anwendung fuer Schlauchdimensionierung:** Maximalverbrauch (Volllast-Spalte) × 1,5 (Sicherheitsfaktor) = Auslegungsvolumenstrom fuer Vorlaufleitung.

### Schlauch-Bestellschluessel Decodierung

Gaengige Hersteller verwenden folgende Bestellschluessel-Formate:

**Trident Marine:**
```
327 - XXXX - YY
│     │      │
│     │      └── Laenge: YY in Fuss (50 = 50 ft Rolle)
│     └── ID in 1/64 Zoll (0580 = 5/8" = ~16 mm, 0380 = 3/8" = ~10 mm)
└── Serie (327 = Standard Fuel, 365 = E85 Fuel, 366 = USCG Type A1)
```

**Shields Rubber:**
```
350 - XXYY
│     ││
│     │└── Variante (00 = Standard, 50 = Low-Perm)
│     └── ID in 1/8 Zoll (08 = 1" = 25 mm, 10 = 1-1/4" = 32 mm)
└── Serie (350 = Marine Fuel A1, 116 = Fuel Fill, 101 = Vent)
```

**Continental ContiTech:**
```
MFH-A1-XX-YYY
│       │   │
│       │   └── Laenge in Meter (050 = 50 m Rolle)
│       └── ID in mm (10, 12, 16, 19, 25)
└── Serie (MFH = Marine Fuel Hose, A1 = ISO 7840 Klasse)
```

### Umrechnungstabelle Zoll → Metrisch (fuer US-Zubehoer)

| Zoll-Bezeichnung | Zoll (Dezimal) | mm | Gaengige Anwendung |
|-------------------|---------------|------|-------------------|
| 1/4" | 0,250 | 6,35 | Kleine Heizungs-Zulaeufe |
| 5/16" | 0,3125 | 7,94 | Aussenborder-Kraftstoff |
| 3/8" | 0,375 | 9,53 | Standard-Saugleitung kleine Motoren |
| 1/2" | 0,500 | 12,70 | Standard-Saugleitung mittlere Motoren |
| 5/8" | 0,625 | 15,88 | Vorlauf/Ruecklauf groessere Motoren |
| 3/4" | 0,750 | 19,05 | Vorlauf Hochleistungsmotoren |
| 1" | 1,000 | 25,40 | Zweimotor-Systeme, Transfer |
| 1-1/4" | 1,250 | 31,75 | Einfuellstutzen, Transfer |
| 1-1/2" | 1,500 | 38,10 | Einfuellstutzen, grosse Transfers |
| 2" | 2,000 | 50,80 | Tankbelueftung, Einfuellstutzen Superyacht |

### Kraftstoff-Dichtewerte bei verschiedenen Temperaturen

| Kraftstoff | 0 °C (g/cm³) | 15 °C (g/cm³) | 25 °C (g/cm³) | 40 °C (g/cm³) | Norm |
|-----------|-------------|---------------|---------------|---------------|------|
| Diesel EN 590 | 0,850 | 0,835 | 0,825 | 0,810 | EN 590 |
| Biodiesel B100 (FAME) | 0,895 | 0,880 | 0,870 | 0,855 | EN 14214 |
| Super E5 | 0,755 | 0,745 | 0,735 | 0,720 | EN 228 |
| Super E10 | 0,760 | 0,750 | 0,740 | 0,725 | EN 228 |
| E85 | 0,790 | 0,780 | 0,770 | 0,755 | ASTM D5798 |

**Relevanz:** Dichteaenderung beeinflusst Volumenstrom und damit die Schlauchdimensionierung. Bei tropischen Betriebstemperaturen (40 °C) sinkt die Dichte um ~3 %, der Volumenstrom steigt entsprechend.

### Vibrations-Frequenzen typischer Marine-Dieselmotoren

| Motor | Zylinder | Leerlauf-Drehzahl (RPM) | Zuendfrequenz Leerlauf (Hz) | Volllast-Drehzahl (RPM) | Zuendfrequenz Volllast (Hz) |
|-------|----------|------------------------|---------------------------|------------------------|---------------------------|
| 1-Zylinder | 1 | 800 | 6,7 | 3000 | 25,0 |
| 2-Zylinder | 2 | 900 | 15,0 | 3600 | 60,0 |
| 3-Zylinder | 3 | 800 | 20,0 | 3200 | 80,0 |
| 4-Zylinder | 4 | 750 | 25,0 | 3000 | 100,0 |
| 6-Zylinder (Reihe) | 6 | 600 | 30,0 | 2300 | 115,0 |
| V8 | 8 | 600 | 40,0 | 2400 | 160,0 |
| V12 | 12 | 500 | 50,0 | 2100 | 210,0 |

**Relevanz fuer Kraftstoffschlaeuche:** Vibration ist Hauptursache fuer Ermuedungsbrueche. Schlauch-Eigenfrequenz (typisch 15–40 Hz bei freier Laenge 200–500 mm) darf NICHT mit Motor-Zuendfrequenz zusammenfallen. Resonanz → Amplitudenvergroesserung → beschleunigte Ermuedung.

**Gegenmassnahmen:** Schlauchlaenge so waehlen, dass Eigenfrequenz > 2× Zuendfrequenz bei Volllast. Alternativ: Schwingungsdaempfer (Gummilager) an Schlauchhalterungen.

### Temperaturprofil im Maschinenraum — Referenzwerte

| Position | Abstand vom Abgaskruemmer (mm) | Typische Temperatur Leerlauf (°C) | Typische Temperatur 75% Last (°C) | Typische Temperatur Volllast (°C) |
|----------|-------------------------------|----------------------------------|----------------------------------|----------------------------------|
| Auf dem Kruemmer | 0 | 180–250 | 350–450 | 450–650 |
| 25 mm entfernt | 25 | 80–120 | 150–220 | 200–300 |
| 50 mm entfernt | 50 | 55–75 | 80–130 | 110–180 |
| 100 mm entfernt | 100 | 40–55 | 55–85 | 70–110 |
| 200 mm entfernt | 200 | 35–45 | 45–65 | 55–80 |
| 500 mm entfernt | 500 | 30–40 | 38–50 | 42–60 |
| Maschinenraum-Decke | variabel | 40–55 | 55–75 | 65–90 |
| Maschinenraum-Boden (Bilge) | variabel | 25–35 | 30–40 | 35–45 |

**AYDI-Anwendung:** Kraftstoffschlauch-Position mit Temperaturprofil abgleichen. Schlauch in Zone > 80 °C → Hitzeschutz PFLICHT. Schlauch in Zone > 100 °C → Umverlegung PFLICHT. Schlauch in Zone > 200 °C → KRITISCH (ISO 7840 A1 max. Dauertemperatur = 100 °C fuer NBR).

### Checkliste: Jaehrliche Kraftstoffsystem-Inspektion

| Nr. | Pruefpunkt | Methode | OK-Kriterium | AYDI-Score bei Mangel |
|-----|-----------|---------|-------------|---------------------|
| 1 | Alle Schlauchverbindungen trocken | Papiertuch abtasten | Kein Kraftstofffilm | 20/100 |
| 2 | Schlauch-Oberflaeche ohne Risse | Visuelle Inspektion + Biegetest | Keine sichtbaren Risse | 15–45/100 |
| 3 | Schlauch nicht verhaertet | Shore-A-Messung | < 85 Shore A | 25/100 |
| 4 | Schlauch nicht gequollen | Sichtpruefung + Fuehlen | Keine Erweichung/Vergroesserung | 20/100 |
| 5 | Alle Schellen fest | Drehmoment-Pruefung | Gemaess Tabelle ±15 % | 30/100 |
| 6 | Schellen nicht korrodiert | Visuelle Inspektion | Kein Rost, kein Lochfrass | 25/100 |
| 7 | Biegeradien eingehalten | Visuelle Inspektion | Keine Knicke | 25/100 |
| 8 | Abstand zu Waermequellen | Messung (Lineal) | > 100 mm (ohne Hitzeschutz) | 5–15/100 |
| 9 | Hitzeschutz intakt (falls vorhanden) | Visuelle Inspektion | Keine Beschaedigung | 15/100 |
| 10 | Kraftstoffventil gaengig | Betaetigen | Oeffnet/schliesst leichtgaengig | 25/100 |
| 11 | Tankbelueftung frei | Durchblasen (Druckluft) | Freier Durchgang | 30/100 |
| 12 | Wasserabscheider-Schauglas | Visuelle Inspektion | Kein Wasser sichtbar | 50/100 |
| 13 | Kraftstoff-Geruch im Maschinenraum | Geruchspruefung + LEL | Kein auffaelliger Geruch, LEL < 5 % | 25/100 |
| 14 | Scheuerschutz an Durchfuehrungen | Visuelle Inspektion | Schutzhuelsen intakt | 40/100 |
| 15 | Dokumentation aktuell | Servicebuch | Letzter Eintrag < 12 Monate | 60/100 |

**Inspektionsdauer:** 30–45 min fuer 8–12 m Boot, 60–90 min fuer 12–18 m Boot, 90–180 min fuer 18+ m Boot.

**Inspektionswerkzeuge (Minimal-Set):** Taschenlampe, Shore-A-Durometer, Papiertuecher, Drehmomentschluessel (1–10 Nm), LEL-Messgeraet, Kamera (Dokumentation), Massstab/Lineal.

---

*Dokumentversion: 6.4.2 | Stand: 2026-04-23 | Autor: AYDI Knowledge Base | Klassifikation: Oeffentlich*
*Alle Angaben ohne Gewaehr. Fuer sicherheitskritische Entscheidungen ist eine professionelle Begutachtung durch einen zertifizierten Marine-Surveyor erforderlich.*
