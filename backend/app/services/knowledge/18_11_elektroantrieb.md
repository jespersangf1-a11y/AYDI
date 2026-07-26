---
titel: "Elektro- und Hybridantrieb"
kategorie: "Motoren und Antrieb"
unterkategorie: "Elektroantrieb"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 18_11 — Elektro- und Hybridantrieb

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Grundlagen der elektrischen Antriebstechnik](#2-grundlagen-der-elektrischen-antriebstechnik)
3. [Rein-elektrische Antriebssysteme](#3-rein-elektrische-antriebssysteme)
4. [Hybrid-Antriebssysteme](#4-hybrid-antriebssysteme)
5. [Batteriesysteme und Energiespeicher](#5-batteriesysteme-und-energiespeicher)
6. [Batterie-Management-Systeme (BMS)](#6-batterie-management-systeme-bms)
7. [Reichweite und Energieberechnung](#7-reichweite-und-energieberechnung)
8. [Ladeinfrastruktur und Energiequellen](#8-ladeinfrastruktur-und-energiequellen)
9. [Leistungselektronik und Steuerung](#9-leistungselektronik-und-steuerung)
10. [Installation und Integration](#10-installation-und-integration)
11. [Normen und Vorschriften](#11-normen-und-vorschriften)
12. [Kosten und TCO-Analyse](#12-kosten-und-tco-analyse)
13. [Umrüstung Diesel auf Elektro](#13-umrüstung-diesel-auf-elektro)
14. [Fehlerbild-Atlas](#14-fehlerbild-atlas)
15. [Troubleshooting](#15-troubleshooting)
16. [FAQ — Häufige Fragen](#16-faq--häufige-fragen)
17. [Glossar](#17-glossar)
18. [Schnell-Referenz](#18-schnell-referenz)
19. [ANHANG A–H: Fallstudien](#19-anhang-ah-fallstudien)
20. [ANHANG I–R: Pydantic v2 Datenmodelle](#20-anhang-ir-pydantic-v2-datenmodelle)

---
---

## 1. Einführung

### 1.1 Bedeutung des elektrischen Antriebs im modernen Yachtbau

Der elektrische Antrieb hat sich von einer Nischenlösung für kleine
Binnenboote zu einer ernstzunehmenden Alternative für Yachten aller
Größenklassen entwickelt. Die Kombination aus steigendem Umweltbewusstsein,
regulatorischem Druck (Emissionszonen in europäischen Binnengewässern,
Nationalparks, Naturschutzgebiete), technologischem Fortschritt bei
Batterien und Leistungselektronik sowie sinkenden Kosten treibt
die Elektrifizierung der Sportschifffahrt voran.

Für Yachtdesigner und -eigner ergeben sich fundamentale Veränderungen:

- **Gewichtsverteilung**: Batterien sind schwerer als Dieseltanks bei
  gleicher Energiemenge, aber die Positionierung ist flexibler.
- **Platzgewinn**: Elektromotoren sind kompakter als Dieselaggregate.
  Der wegfallende Abgasstrang, Kraftstofftank und Kühlwasserkreislauf
  schafft zusätzlichen Raum.
- **Geräuschkomfort**: Elektromotoren arbeiten praktisch lautlos —
  ein Paradigmenwechsel für den Bordkomfort.
- **Wartungsreduktion**: Deutlich weniger bewegliche Teile, kein
  Ölwechsel, kein Impellertausch, keine Zinkanoden am Motor.
- **Neue Designfreiheiten**: Pod-Antriebe, Doppelmotoren, flexible
  Einbauorte ohne Abgasführung.

### 1.2 Marktentwicklung und Trends (2020–2026)

| Jahr | Marktvolumen (EU) | Wachstum | Treiber |
|------|-------------------|----------|---------|
| 2020 | ~120 Mio. EUR | Basis | Torqeedo-Dominanz, Nischenmarkt |
| 2021 | ~160 Mio. EUR | +33 % | Corona-Boom, Outdoortrend |
| 2022 | ~220 Mio. EUR | +38 % | ePropulsion-Markteintritt EU |
| 2023 | ~310 Mio. EUR | +41 % | LiFePO4-Preisverfall, neue OEM-Angebote |
| 2024 | ~420 Mio. EUR | +35 % | Emissionszonen Amsterdam, Bodensee |
| 2025 | ~550 Mio. EUR | +31 % | Hybrid-Lösungen für Motoryachten |
| 2026 | ~700 Mio. EUR | +27 % | Superyacht-Segment, Feststoffbatterien |

### 1.3 Vergleich: Diesel vs. Elektro vs. Hybrid

| Kriterium | Diesel | Rein-Elektrisch | Parallel-Hybrid | Seriell-Hybrid |
|-----------|--------|----------------|-----------------|----------------|
| Energiedichte (Wh/kg) | ~12.000 (Diesel) | 90–200 (LiFePO4/NMC) | Kombiniert | Kombiniert |
| Reichweite (typ. 12m Yacht) | 500–1.500 sm | 20–80 sm | 300–800 sm | 200–600 sm |
| Geräusch (dB bei 5 kn) | 65–85 dB | 30–45 dB | 30–85 dB | 50–75 dB |
| Wartungskosten/Jahr | 800–3.000 EUR | 100–400 EUR | 600–2.500 EUR | 500–2.000 EUR |
| Anschaffung (10m Boot) | 15.000–40.000 EUR | 12.000–60.000 EUR | 35.000–80.000 EUR | 40.000–90.000 EUR |
| CO₂-Emission (pro sm) | 5–15 kg | 0 (lokal) | 2–10 kg | 3–12 kg |
| Lebensdauer Motor | 5.000–15.000 h | 15.000–30.000 h | Kombiniert | Kombiniert |
| Tankzeit/Ladezeit | 5–10 min | 4–12 h (Landstrom) | Selbstladend | Selbstladend |

### 1.4 Einsatzszenarien nach Bootsklasse

| Bootsklasse | Empfohlene Technologie | Begründung |
|------------|----------------------|------------|
| Jolle/Dinghy (< 5 m) | Rein-elektrisch | Geringe Leistung, kurze Strecken, ideal für E-Außenborder |
| Segelboot 7–10 m | Rein-elektrisch | Motor nur als Hilfsantrieb, Hydro-Regeneration möglich |
| Segelboot 10–15 m | Elektrisch oder Hybrid | Längere Hafenmanöver, Hydro-Regen auf Langfahrt |
| Motoryacht 8–12 m | Parallel-Hybrid | Manöver elektrisch, Überfahrten mit Diesel |
| Motoryacht 12–18 m | Parallel-/Seriell-Hybrid | Emissionszone + Langstrecke |
| Motoryacht 18–24 m | Seriell-Hybrid | Diesel-Generator + E-Motoren, optimale Effizienz |
| Superyacht 24 m+ | Seriell-Hybrid / Diesel-Elektrisch | Hotellasten, dynamische Positionierung |
| Katamaran 10–15 m | Rein-elektrisch (Doppel) | Zwei E-Motoren, großes Solardach, Reichweite ausreichend |

### 1.5 Physikalische Grundbeziehungen

Die folgenden Formeln bestimmen die Auslegung jedes elektrischen
Bootsantriebs:

**Widerstandsleistung (Savitsky vereinfacht):**
```
P_widerstand = (0,5 × ρ_wasser × v² × C_w × A_benetzt) / η_propeller

Dabei:
  ρ_wasser  = 1.025 kg/m³ (Salzwasser) / 1.000 kg/m³ (Süßwasser)
  v         = Geschwindigkeit in m/s
  C_w       = Widerstandsbeiwert (0,003–0,008 je nach Rumpfform)
  A_benetzt = Benetzte Fläche in m²
  η_propeller = Propellerwirkungsgrad (0,40–0,65)
```

**Rumpfgeschwindigkeit (Verdränger):**
```
v_max = 1,34 × √(LWL_ft)  [in Knoten]
v_max = 2,43 × √(LWL_m)   [in Knoten]
```

**Energiebedarf pro Seemeile:**
```
E_sm = P_antrieb / v_knoten  [in kWh/sm]
```

**Faustregel für Verdränger:**
```
P_minimalfahrt ≈ 2–4 kW pro Tonne Verdrängung (bei v_hull × 0,5)
P_rumpfgeschwindigkeit ≈ 5–8 kW pro Tonne (bei v_hull × 1,0)
```

---
---

## 2. Grundlagen der elektrischen Antriebstechnik

### 2.1 Motortypen für den Marinebereich

#### 2.1.1 Permanentmagnet-Synchronmotor (PMSM)

Der PMSM ist der dominante Motortyp im marinen Elektroantrieb:

- **Funktionsprinzip**: Rotor mit Permanentmagneten (NdFeB), Stator mit
  Drehfeld-Wicklung. Drehmoment durch magnetische Anziehung/Abstoßung.
- **Vorteile**: Höchster Wirkungsgrad (92–97 %), kompakt, leicht,
  hohes Drehmoment bei niedrigen Drehzahlen, wartungsfrei.
- **Nachteile**: Teure Magnete (Neodym), empfindlich gegen Überhitzung
  (Entmagnetisierung > 150 °C), keine Feldschwächung ohne Regler.
- **Hersteller marine**: Torqeedo, Oceanvolt, Bellmarine, Fischer Panda.
- **Typische Daten (10 kW)**: Ø 200–280 mm, Länge 180–250 mm,
  Gewicht 15–35 kg, η = 94–96 %.

#### 2.1.2 Asynchronmotor (ASM / Induktionsmotor)

- **Funktionsprinzip**: Rotor mit Kurzschlussläufer (Käfigläufer),
  kein Magnet. Drehmoment durch Induktion.
- **Vorteile**: Robust, preiswert, überlastfähig, keine Seltenen Erden.
- **Nachteile**: Geringerer Wirkungsgrad (88–94 %), schwerer, Schlupf.
- **Einsatz marine**: Größere Systeme (> 20 kW), Hybrid-Antriebe,
  ältere Installationen.
- **Typische Daten (10 kW)**: Ø 250–320 mm, Länge 250–350 mm,
  Gewicht 30–60 kg, η = 90–93 %.

#### 2.1.3 Bürstenloser Gleichstrommotor (BLDC)

- **Funktionsprinzip**: Variante des PMSM mit trapezförmiger
  Kommutierung statt sinusförmig.
- **Vorteile**: Einfache Steuerung, preiswert, guter Wirkungsgrad.
- **Nachteile**: Drehmomentwelligkeit, Geräusche bei Niedrigdrehzahl.
- **Einsatz marine**: Außenborder (ePropulsion, Torqeedo Travel),
  kleine Innenborder bis 5 kW.

#### 2.1.4 Gleichstrommotor mit Bürsten (DC)

- **Funktionsprinzip**: Mechanischer Kommutator, Kohlebürsten.
- **Vorteile**: Einfach, robust, lineares Drehmoment-Drehzahl-Verhalten.
- **Nachteile**: Bürstenverschleiß, Funkenbildung (Ex-Gefahr!),
  geringerer Wirkungsgrad (80–88 %).
- **Einsatz marine**: Nur noch Legacy-Systeme, Bugstrahler,
  Ankerwinden. Nicht für Hauptantrieb empfohlen.

### 2.2 Wirkungsgradkette

Die Gesamteffizienz des elektrischen Antriebsstrangs:

```
η_gesamt = η_batterie × η_regler × η_motor × η_getriebe × η_propeller

Typische Werte:
  η_batterie   = 0,95 (Lade-/Entlade-Verluste)
  η_regler     = 0,97 (Frequenzumrichter/Controller)
  η_motor      = 0,94 (PMSM)
  η_getriebe   = 0,98 (Planetengetriebe) oder 1,00 (Direktantrieb)
  η_propeller  = 0,55 (Festpropeller) bis 0,65 (Verstellpropeller)

η_gesamt_typisch = 0,95 × 0,97 × 0,94 × 0,98 × 0,60 = 0,509 ≈ 51 %

Zum Vergleich: Dieselantrieb
  η_diesel × η_getriebe × η_propeller = 0,35 × 0,96 × 0,55 = 0,185 ≈ 19 %
```

Der elektrische Antrieb ist also bei der Energieumwandlung an Bord
ca. 2,7× effizienter als der Dieselantrieb. Aber: Die Energiedichte
von Diesel (~12.000 Wh/kg) ist ~80× höher als LiFePO4 (~150 Wh/kg).

### 2.3 Drehmoment-Drehzahl-Charakteristik

| Eigenschaft | E-Motor | Dieselmotor |
|------------|---------|-------------|
| Max. Drehmoment bei | 0 U/min | 2.000–3.000 U/min |
| Drehzahlbereich | 0–5.000 U/min | 800–4.000 U/min |
| Drehmomentkurve | Flach (konstant) | Buckel bei Nenndrehzahl |
| Leerlaufdrehzahl | 0 U/min | 600–900 U/min |
| Getriebe nötig? | Oft nicht (Direktantrieb) | Immer (Untersetzung) |

Der flache Drehmomentverlauf des E-Motors ist ideal für den
Propellerantrieb: Hohes Drehmoment beim Anfahren (Manöver),
konstante Leistung über breiten Drehzahlbereich.

### 2.4 Kühlungskonzepte

#### Luftkühlung
- Einsatz: Kleine Motoren bis 5 kW
- Ventilator am Motor oder passive Konvektion
- Einfach, aber begrenzte Dauerleistung

#### Wasserkühlung (geschlossener Kreislauf)
- Einsatz: Motoren ab 5 kW, hohe Dauerbelastung
- Kühlmittel: Glykol/Wasser-Gemisch, Wärmetauscher am Rumpf
- Höhere Dauerleistung, kompaktere Bauweise

#### Seewasserkühlung (offener Kreislauf)
- Einsatz: Integrierte Systeme (Saildrive-E-Motor)
- Einfach und effektiv, aber Korrosions-/Bewuchsrisiko
- Oceanvolt ServoProp nutzt dieses Prinzip

#### Ölkühlung (geschlossener Kreislauf)
- Einsatz: Hochleistungsmotoren, integrierte Getriebe
- Öl als Kühl- und Schmiermittel
- Sehr hohe Dauerleistung, komplex

### 2.5 Spannungsebenen im Marinebereich

| Spannungsebene | Typische Spannung | Einsatz | Vorteile | Nachteile |
|---------------|-------------------|---------|----------|-----------|
| Niederspannung | 12 V / 24 V | Außenborder < 3 kW | Einfach, sicher | Hohe Ströme, dicke Kabel |
| Mittelspannung | 48 V | Außen-/Innenborder 3–10 kW | Guter Kompromiss | Standard-Batterien |
| Hochspannung | 300–400 V | Innenborder 10–100 kW | Dünne Kabel, effizient | Berührungsschutz! |
| Hochspannung+ | 600–800 V | Superyacht > 100 kW | Maximale Effizienz | Spezialisten erforderlich |

**Sicherheitshinweis**: Ab 48 V DC bzw. 60 V AC gelten verschärfte
Vorschriften (IEC 60092, ISO 16315). Ab 120 V DC besteht Lebensgefahr.
Hochvolt-Systeme (> 60 V) erfordern geschultes Fachpersonal, isolierte
Werkzeuge und Berührungsschutz gemäß IP2X.

### 2.6 Kabelquerschnitte und Verluste

Dimensionierungstabelle für Gleichstromleitungen (Kupfer, 3 % Verlust):

| Strom (A) | 12 V (mm²) | 24 V (mm²) | 48 V (mm²) | 400 V (mm²) |
|-----------|-----------|-----------|-----------|------------|
| 10 | 6 | 4 | 2,5 | 0,75 |
| 25 | 16 | 10 | 6 | 1,5 |
| 50 | 35 | 16 | 10 | 2,5 |
| 100 | 70 | 35 | 16 | 4 |
| 200 | 150 | 70 | 35 | 10 |
| 400 | — | 150 | 70 | 16 |

Kabelgewicht bei 5 m Leitungslänge (hin + zurück = 10 m):

| Querschnitt | Gewicht/m | 10 m gesamt |
|------------|----------|------------|
| 6 mm² | 0,06 kg | 0,6 kg |
| 16 mm² | 0,16 kg | 1,6 kg |
| 35 mm² | 0,35 kg | 3,5 kg |
| 70 mm² | 0,70 kg | 7,0 kg |
| 150 mm² | 1,50 kg | 15,0 kg |

Hochvolt-Systeme (400 V) sparen massiv Kabelgewicht und -querschnitt.

---
---

## 3. Rein-elektrische Antriebssysteme

### 3.1 Torqeedo — Marktführer marine Elektroantriebe

#### 3.1.1 Torqeedo Cruise-Serie (Innenborder/Pod)

| Modell | Leistung | Äquivalent (Diesel) | Spannung | Gewicht Motor | Preis (EUR) |
|--------|---------|---------------------|----------|-------------|------------|
| Cruise 2.0 | 2,0 kW | ~5 PS | 24/48 V | 10,2 kg | 3.800–4.200 |
| Cruise 3.0 | 3,0 kW | ~8 PS | 24/48 V | 11,5 kg | 4.400–4.900 |
| Cruise 4.0 | 4,0 kW | ~10 PS | 48 V | 13,8 kg | 5.200–5.800 |
| Cruise 6.0 | 6,0 kW | ~15 PS | 48 V | 16,2 kg | 6.800–7.500 |
| Cruise 10.0 | 10,0 kW | ~25 PS | 48 V | 26,0 kg | 9.500–10.500 |
| Cruise 10.0 FP | 10,0 kW (Faltprop) | ~25 PS | 48 V | 28,5 kg | 11.000–12.000 |

**Technische Daten Cruise-Serie:**
- Motortyp: PMSM (Permanentmagnet-Synchron)
- Schutzklasse: IPX8 (dauerhaft untertaucht)
- Kühlung: Seewasser (direkt am Unterwasserteil)
- Steuerung: Torqeedo TorqLink (CAN-Bus)
- Kompatible Batterien: Torqeedo Power 24-3500/48-5000, BMW i3-Module
- Fernbedienung: Throttle-Hebel (optional), Torqeedo-App (Bluetooth)
- GPS-Geschwindigkeitsanzeige: Serienmäßig (Reichweitenanzeige)
- Garantie: 3 Jahre Motor, 5 Jahre Batterie (> 80 % Kapazität)

#### 3.1.2 Torqeedo Deep Blue-Serie (Hochleistung)

| Modell | Leistung | Äquivalent | Spannung | Gewicht | Preis (EUR) |
|--------|---------|-----------|----------|---------|------------|
| Deep Blue 25i | 25 kW | ~50 PS | 345 V | 47 kg | 18.000–20.000 |
| Deep Blue 40i | 40 kW | ~80 PS | 345 V | 62 kg | 24.000–27.000 |
| Deep Blue 50i | 50 kW | ~100 PS | 345 V | 78 kg | 30.000–34.000 |
| Deep Blue 100i | 100 kW | ~200 PS | 360 V | 135 kg | 55.000–62.000 |

**Technische Details Deep Blue:**
- Motortyp: Wassergekühlter PMSM
- Batterie: BMW i3-Hochvoltmodule (33,4 kWh netto pro Pack)
- Maximale Batterie-Konfiguration: 6 Packs = 200,4 kWh
- Onboard-Charger: 22 kW (3-phasig) optional
- CAN-Bus: NMEA 2000 kompatibel
- Monitoring: Torqeedo-App mit Live-Daten
- Zertifizierung: CE, ABYC E-11, ISO 16315

#### 3.1.3 Torqeedo Preise Batterien

| Modell | Kapazität | Spannung | Chemie | Gewicht | Preis (EUR) |
|--------|----------|---------|--------|---------|------------|
| Power 24-3500 | 3,5 kWh | 25,9 V | LiFePO4 | 28 kg | 3.400–3.800 |
| Power 48-5000 | 5,0 kWh | 51,2 V | LiFePO4 | 39 kg | 4.800–5.400 |
| Deep Blue i3 Pack | 33,4 kWh | 345 V | NMC (Li-Ion) | 256 kg | 22.000–25.000 |

### 3.2 ePropulsion — Preis-Leistungs-Alternative

#### 3.2.1 ePropulsion Navy-Serie (Innenborder)

| Modell | Leistung | Äquivalent | Spannung | Gewicht Motor | Preis (EUR) |
|--------|---------|-----------|----------|-------------|------------|
| Navy 3.0 Evo | 3,0 kW | ~8 PS | 48 V | 12,0 kg | 2.900–3.400 |
| Navy 6.0 Evo | 6,0 kW | ~15 PS | 48 V | 18,5 kg | 4.200–4.800 |
| Navy 10.0 Evo | 10,0 kW | ~25 PS | 48 V | 28,0 kg | 6.500–7.200 |

**Technische Daten Navy-Serie:**
- Motortyp: PMSM
- Schutzklasse: IP67 (Motor), IPX8 (Unterwasserteil)
- Kühlung: Seewasser (Unterwasserteil), Luft (Controller)
- Steuerung: ePropulsion EPC (CAN-Bus)
- Kompatible Batterien: ePropulsion E-Serie, Drittanbieter (48 V, CAN)
- Display: 5" Touchscreen mit GPS, Reichweite, Verbrauch
- Garantie: 5 Jahre Motor, 3 Jahre Batterie (>70 % Kapazität)

#### 3.2.2 ePropulsion Batterien

| Modell | Kapazität | Spannung | Chemie | Gewicht | Preis (EUR) |
|--------|----------|---------|--------|---------|------------|
| E40 | 4,0 kWh | 51,2 V | LiFePO4 | 32 kg | 2.800–3.200 |
| E80 | 8,0 kWh | 51,2 V | LiFePO4 | 58 kg | 5.200–5.800 |
| E175 | 17,5 kWh | 51,2 V | LiFePO4 | 118 kg | 10.500–11.800 |

#### 3.2.3 Preisvergleich ePropulsion vs. Torqeedo (10 kW Konfiguration)

| Komponente | ePropulsion | Torqeedo | Differenz |
|-----------|------------|---------|----------|
| Motor 10 kW | 6.850 EUR | 10.000 EUR | −3.150 EUR (−32 %) |
| Batterie ~17 kWh | 10.500 EUR | 14.400 EUR (3× P48-5000) | −3.900 EUR (−27 %) |
| Controller/Display | inklusive | inklusive | 0 |
| Kabelbaum | 350 EUR | 450 EUR | −100 EUR |
| **Gesamt** | **17.700 EUR** | **24.850 EUR** | **−7.150 EUR (−29 %)** |

### 3.3 Oceanvolt — Segelyacht-Spezialist

#### 3.3.1 Oceanvolt ServoProp-Serie

| Modell | Leistung | Äquivalent | Spannung | Besonderheit | Preis (EUR) |
|--------|---------|-----------|----------|-------------|------------|
| ServoProp 5 | 5 kW | ~12 PS | 48 V | Saildrive-Ersatz | 8.500–9.500 |
| ServoProp 10 | 10 kW | ~25 PS | 48 V | Saildrive-Ersatz | 12.000–13.500 |
| ServoProp 15 | 15 kW | ~35 PS | 48 V | Saildrive-Ersatz | 16.500–18.500 |
| ServoProp 20 | 20 kW | ~45 PS | 48 V | Saildrive-Ersatz | 21.000–24.000 |

**Besonderheit ServoProp:**
- Integrierter Saildrive mit Faltpropeller
- Direkte Montage am Saildrive-Ausschnitt (Yanmar SD20/SD25/SD50 kompatibel)
- **Hydro-Regeneration**: Der Propeller treibt unter Segeln den Generator an.
  Typische Regenerationsleistung: 0,5–1,5 kW bei 6–8 Knoten Fahrt.
- Stufenlose Drehzahlregelung, vorwärts/rückwärts
- Kühlung: Seewasser (direkt)
- Gewicht: 22–45 kg (je nach Modell, deutlich leichter als Diesel-Saildrive)

#### 3.3.2 Oceanvolt AXC-Serie (Wellenantrieb)

| Modell | Leistung | Äquivalent | Spannung | Preis (EUR) |
|--------|---------|-----------|----------|------------|
| AXC 6 | 6 kW | ~15 PS | 48 V | 7.500–8.500 |
| AXC 10 | 10 kW | ~25 PS | 48 V | 10.000–11.500 |
| AXC 15 | 15 kW | ~35 PS | 48 V | 13.500–15.000 |
| AXC 20 | 20 kW | ~45 PS | 48 V | 17.000–19.000 |

**AXC-Details:**
- Flanschmontage an bestehende Wellenanlage (SAE-Standard-Flansch)
- Ideal für Umrüstungen: Diesel raus, AXC rein
- Optionales Planetengetriebe (2:1 oder 3:1 Untersetzung)
- Hydro-Regeneration möglich (bei Wellenantrieb durch freien Propeller)

### 3.4 Bellmarine — Niederländischer Spezialist

#### 3.4.1 Bellmarine DriveMaster-Serie

| Modell | Leistung | Äquivalent | Spannung | Gewicht | Preis (EUR) |
|--------|---------|-----------|----------|---------|------------|
| DriveMaster 3.5 | 3,5 kW | ~9 PS | 48 V | 14 kg | 4.200–4.800 |
| DriveMaster 5.0 | 5,0 kW | ~12 PS | 48 V | 18 kg | 5.500–6.200 |
| DriveMaster 7.5 | 7,5 kW | ~18 PS | 48 V | 24 kg | 7.000–7.800 |
| DriveMaster 10.0 | 10,0 kW | ~25 PS | 48 V | 32 kg | 8.500–9.500 |
| DriveMaster Ultimate 12 | 12,0 kW | ~30 PS | 48 V | 38 kg | 10.500–11.800 |
| DriveMaster Ultimate 15 | 15,0 kW | ~35 PS | 48 V | 45 kg | 12.000–13.500 |

**Bellmarine-Besonderheiten:**
- Alle Modelle mit integriertem Planetengetriebe (Untersetzung wählbar)
- SAE-Flansch-Montage (direkter Dieselersatz)
- Kühlwassermantel (geschlossener Kreislauf oder Seewasser)
- Kompatibel mit allen 48 V LiFePO4-Batterien
- Dutch Marine Quality (strenge niederländische Binnenfahrt-Zulassung)
- Besonders stark im Grachtenboot-Segment und Charter

#### 3.4.2 Bellmarine EcoPower Saildrive

| Modell | Leistung | Besonderheit | Preis (EUR) |
|--------|---------|-------------|------------|
| EcoPower SD 5 | 5 kW | Volvo/Yanmar SD-kompatibel | 9.000–10.000 |
| EcoPower SD 10 | 10 kW | Volvo/Yanmar SD-kompatibel | 13.000–14.500 |
| EcoPower SD 15 | 15 kW | Volvo/Yanmar SD-kompatibel | 17.000–19.000 |

### 3.5 Fischer Panda E-Drive

| Modell | Leistung | Spannung | Besonderheit | Preis (EUR) |
|--------|---------|----------|-------------|------------|
| E-Drive 5 | 5 kW | 48 V | Wellenantrieb | 6.500–7.500 |
| E-Drive 10 | 10 kW | 48 V | Wellenantrieb | 9.000–10.500 |
| E-Drive 20 | 20 kW | 48/360 V | Wellenantrieb | 16.000–18.000 |
| E-Drive 40 | 40 kW | 360 V | Wellenantrieb | 28.000–32.000 |
| E-Drive 80 | 80 kW | 360/700 V | Wellenantrieb | 52.000–60.000 |

**Fischer Panda Besonderheit:**
- Deutscher Hersteller (Paderborn), bekannt für Generatoren
- Hybrid-Kopplung: E-Drive + Fischer Panda Diesel-Generator = Seriell-Hybrid
- Integrierte Systemlösung: Motor + Generator + Batterie + Management
- Marinisierte Industriequalität, ABYC/CE zertifiziert

### 3.6 Weitere Hersteller (Übersicht)

| Hersteller | Herkunft | Leistungsbereich | Besonderheit | Preisbereich (EUR) |
|-----------|---------|-----------------|-------------|-------------------|
| Elco Motor Yachts | USA | 5–100 kW | Historische Marke (seit 1893) | 8.000–80.000 |
| Aqua Watt | Österreich | 3–20 kW | Grachtenbootspezialist | 4.000–18.000 |
| Kräutler | Österreich | 2–25 kW | Bodensee-Tradition | 3.500–22.000 |
| Electric Yacht | USA | 5–30 kW | Umrüst-Spezialist | 6.000–28.000 |
| Lynch Motor | UK | 2–20 kW | Bürstenlose DC-Motoren | 2.500–15.000 |
| Combi Marine | Niederlande | 5–50 kW | Hybrid-Systeme | 8.000–45.000 |
| ZF Marine (eGear) | Deutschland | 25–500 kW | Superyacht-Hybrid | 30.000–300.000 |
| Danfoss Editron | Finnland | 50–2.000 kW | Schwerlast, Fähren | 40.000–500.000+ |

### 3.7 Außenborder (rein-elektrisch)

| Modell | Leistung | Äquivalent | Batterie | Gewicht | Preis (EUR) |
|--------|---------|-----------|---------|---------|------------|
| Torqeedo Travel 603 | 600 W | ~2 PS | integriert (530 Wh) | 8,9 kg | 1.800–2.100 |
| Torqeedo Travel 1103 | 1,1 kW | ~3 PS | integriert (915 Wh) | 13,9 kg | 2.400–2.800 |
| Torqeedo Cruise 2.0 R | 2,0 kW | ~5 PS | extern | 14,0 kg | 3.800–4.200 |
| ePropulsion Spirit 1.0 Plus | 1,0 kW | ~3 PS | integriert (1,3 kWh) | 10,5 kg | 1.400–1.600 |
| ePropulsion Navy 3.0 AB | 3,0 kW | ~8 PS | extern | 24,0 kg | 3.200–3.600 |
| ePropulsion X20 | 3,0 kW | ~6 PS | extern | 18,0 kg | 2.800–3.200 |
| ePropulsion X40 | 6,0 kW | ~10 PS | extern | 28,0 kg | 4.500–5.000 |
| Mercury Avator 7.5e | 750 W | ~2,5 PS | integriert | 11,3 kg | 2.200–2.500 |
| Pure Watercraft | 20 kW | ~50 PS | integriert (12 kWh) | 58 kg | 12.000–14.000 |
| Evoy Storm | 120 kW | ~300 PS | extern (63–126 kWh) | 185 kg | 65.000–85.000 |

---
---

## 4. Hybrid-Antriebssysteme

### 4.1 Hybrid-Architekturen im Vergleich

#### 4.1.1 Parallel-Hybrid

```
                    ┌───────────┐
                    │  Batterie │
                    └─────┬─────┘
                          │
┌──────────┐    ┌─────────┴────────┐    ┌──────────┐    ┌───────────┐
│  Diesel  ├────┤  Kupplung/PTI    ├────┤ Getriebe ├────┤ Propeller │
│  Motor   │    │  (E-Motor integ.)│    │          │    │           │
└──────────┘    └──────────────────┘    └──────────┘    └───────────┘
```

**Funktionsprinzip:**
- Diesel und E-Motor sitzen auf derselben Wellenachse
- Kupplung trennt/verbindet Diesel mechanisch
- Drei Betriebsmodi:
  1. **Diesel only**: E-Motor entkoppelt, klassischer Betrieb
  2. **Elektrisch only**: Diesel entkoppelt, leises Manövrieren
  3. **Boost**: Beide Motoren treiben gleichzeitig (maximale Leistung)
  4. **Laden**: Diesel treibt Propeller + Generator (E-Motor als Generator)

**Vorteile:**
- Diesel-Reichweite bleibt erhalten
- Elektrisches Manövrieren in Häfen/Emissionszonen
- Boost-Modus für Notsituationen
- Diesel kann Batterien laden (unterwegs)

**Nachteile:**
- Komplexes Kupplungssystem
- Diesel muss trotzdem gewartet werden
- Gewichtszunahme (beide Systeme an Bord)
- Eingeschränkte Aufstellungsfreiheit (koaxial)

#### 4.1.2 Seriell-Hybrid (Diesel-Elektrisch)

```
┌──────────┐    ┌───────────┐    ┌───────────┐
│  Diesel  ├────┤ Generator ├────┤  Batterie │
│  Motor   │    │           │    │           │
└──────────┘    └─────┬─────┘    └─────┬─────┘
                      │                │
                      └──────┬─────────┘
                             │
                      ┌──────┴──────┐    ┌───────────┐
                      │  Controller ├────┤ E-Motor   │
                      │  (Inverter) │    │ + Propell. │
                      └─────────────┘    └───────────┘
```

**Funktionsprinzip:**
- Diesel treibt nur den Generator an (keine mechanische Kopplung
  zum Propeller)
- Generator lädt Batterien und/oder speist E-Motor direkt
- E-Motor treibt den Propeller an
- Betriebsmodi:
  1. **Batterie only**: Lautloser Betrieb, begrenzte Reichweite
  2. **Generator only**: Diesel-Generator läuft bei optimalem
     Wirkungsgrad-Punkt (konstante Drehzahl)
  3. **Gemischt**: Generator + Batterie für Spitzenleistung

**Vorteile:**
- Diesel läuft immer im optimalen Betriebspunkt (Verbrauch −15–25 %)
- Volle Designfreiheit: Generator kann überall platziert werden
- E-Motor-Vorteile (Drehmoment, Laufruhe)
- Einfache Doppelmotorisierung (zwei E-Motoren, ein Generator)
- Ideal für Superyachten mit hoher Hotellast

**Nachteile:**
- Doppelte Energieumwandlung (Diesel→Generator→Batterie→Motor)
- Gesamtwirkungsgrad im Generator-Betrieb geringer als Parallel
- Höhere Anschaffungskosten
- Mehr Elektronik = mehr potenzielle Fehlerquellen

### 4.2 Volvo Penta Hybrid-Systeme

#### 4.2.1 Volvo Penta D4/D6 Hybrid (IPS mit Parallel-Hybrid)

| Parameter | D4-320 Hybrid | D6-440 Hybrid |
|-----------|-------------|-------------|
| Dieselleistung | 235 kW (320 PS) | 324 kW (440 PS) |
| E-Motor-Leistung | 20 kW | 30 kW |
| Batterie | 11,5 kWh (LiFePO4) | 23 kWh (LiFePO4) |
| Elektrische Reichweite | ~3 sm (Manöver) | ~5 sm (Manöver) |
| Boost-Leistung | 255 kW (347 PS) | 354 kW (481 PS) |
| Systemgewicht (Mehrgewicht) | +180 kg | +310 kg |
| Preis (Aufpreis zu Standard) | ~25.000 EUR | ~38.000 EUR |

**Integration:**
- Nahtlos in Volvo IPS-System integriert
- Joystick-Manövrierung auch rein-elektrisch
- Automatisches Laden während Diesel-Betrieb
- Dynamic Positioning System (DPS) unterstützt
- EVC (Electronic Vessel Control) steuert alle Modi

#### 4.2.2 Volvo Penta Hybrid-Modi

| Modus | Diesel | E-Motor | Batterie | Anwendung |
|-------|--------|---------|----------|-----------|
| Pure Electric | Aus | Antrieb | Entlädt | Hafen, Emissionszone |
| Diesel | An (optimal) | Aus | — | Langstrecke |
| Hybrid | An | Generator | Lädt | Cruising + Laden |
| Boost | An (Vollgas) | Antrieb | Entlädt | Beschleunigung, Not |
| Hotel | Aus | — | Versorgt | Ankern, Bordnetz |

### 4.3 ZF Marine Hybrid-Getriebe

#### 4.3.1 ZF Parallel-Hybrid-Module

| Modell | E-Motor-Leistung | Max. Diesel-Leistung | Untersetzung | Preis (EUR) |
|--------|-----------------|---------------------|-------------|------------|
| ZF 3000 PTI | 25 kW | 250 kW | 1,5:1–3:1 | 18.000–22.000 |
| ZF 5000 PTI | 50 kW | 500 kW | 1,5:1–3:1 | 28.000–35.000 |
| ZF 9000 PTI | 100 kW | 1.000 kW | 1,5:1–3:1 | 48.000–58.000 |

**PTI = Power Take-In:** E-Motor speist Leistung ins Getriebe ein.
**PTO = Power Take-Off:** Dieselmotor treibt Generator über Getriebe an.

ZF-Getriebe ermöglichen PTI und PTO gleichzeitig:
- Während der Diesel läuft: Laden über PTO
- Im Hafen: Antrieb über PTI (rein-elektrisch)
- Auf See: Boost über PTI + Diesel

#### 4.3.2 ZF eGear-System (Vollelektrisch)

| Modell | Leistung | Drehmoment | Spannung | Preis (EUR) |
|--------|---------|-----------|----------|------------|
| eGear 1500 | 25 kW | 450 Nm | 360 V | 22.000–26.000 |
| eGear 3000 | 50 kW | 900 Nm | 360 V | 35.000–42.000 |
| eGear 6000 | 100 kW | 1.800 Nm | 360/700 V | 55.000–65.000 |

### 4.4 Hybrid-System-Auslegung nach Bootsklasse

| Bootsklasse | Hybrid-Typ | Diesel | E-Motor | Batterie | Budget (EUR) |
|------------|-----------|--------|---------|----------|-------------|
| Motoryacht 10–12 m | Parallel | 100–150 kW | 10–15 kW | 10–20 kWh | 35.000–55.000 |
| Motoryacht 12–16 m | Parallel | 150–250 kW | 15–25 kW | 20–40 kWh | 55.000–90.000 |
| Motoryacht 16–20 m | Seriell | 100–200 kW Gen | 50–100 kW | 50–100 kWh | 120.000–200.000 |
| Motoryacht 20–24 m | Seriell | 150–300 kW Gen | 100–200 kW | 100–200 kWh | 200.000–400.000 |
| Superyacht 24–35 m | Seriell | 200–500 kW Gen | 200–500 kW | 200–500 kWh | 400.000–1.200.000 |
| Superyacht 35 m+ | Diesel-Elek. | 500+ kW Gen | 500+ kW | 500+ kWh | 1.000.000+ |

### 4.5 Regeneration und Energierückgewinnung

#### 4.5.1 Hydro-Regeneration (Segelboote)

Beim Segeln treibt der freidrehende Propeller den E-Motor als Generator an:

| Fahrt (Knoten) | Typische Regeneration | Bemerkung |
|---------------|---------------------|-----------|
| 4 | 50–150 W | Kaum nutzbar |
| 5 | 150–400 W | Grundversorgung Bordnetz |
| 6 | 300–800 W | Sinnvoll |
| 7 | 500–1.200 W | Gut |
| 8 | 800–1.800 W | Sehr gut |
| 10+ | 1.200–2.500 W | Maximal |

**Formel Hydro-Regeneration (überschlägig):**
```
P_regen = 0,5 × ρ × A_prop × v³ × η_prop × η_gen × C_regen

Dabei:
  ρ        = 1.025 kg/m³
  A_prop   = Propellerkreisfläche (m²)
  v        = Fahrt (m/s)
  η_prop   = 0,30–0,50 (als Turbine geringer als als Propeller)
  η_gen    = 0,90–0,95
  C_regen  = 0,25–0,40 (Korrekturfaktor für Wellenleitung)
```

**Praxiswerte Oceanvolt ServoProp (Hydro-Regen):**
| Modell | bei 5 kn | bei 6 kn | bei 7 kn | bei 8 kn |
|--------|---------|---------|---------|---------|
| ServoProp 5 | 120 W | 280 W | 500 W | 750 W |
| ServoProp 10 | 180 W | 400 W | 750 W | 1.200 W |
| ServoProp 15 | 250 W | 550 W | 1.000 W | 1.600 W |
| ServoProp 20 | 300 W | 700 W | 1.300 W | 2.000 W |

**Praxisbeispiel**: Segelboot 12 m, ServoProp 10, Atlantik-Überquerung:
- Durchschnittliche Segelfahrt: 6,5 Knoten
- Durchschnittliche Regeneration: ~550 W
- Tagesertrag: 550 W × 24 h = 13,2 kWh
- Bordverbrauch: ~3–5 kWh/Tag (Autopilot, Navigation, Kühlschrank)
- Netto-Überschuss: ~8 kWh/Tag → Batterie immer voll

#### 4.5.2 Diesel-Regeneration (Hybrid-Betrieb)

Im Parallel-Hybrid kann der Diesel die Batterie laden:

| Diesel-Last | Wirkungsgrad Diesel | Überschuss für Laden | Lade-Leistung |
|------------|-------------------|---------------------|--------------|
| 50 % Last | ~32 % | Wenig Überschuss | 5–10 % der Nennleistung |
| 75 % Last | ~36 % (optimal) | Mäßig | 10–15 % der Nennleistung |
| 100 % Last | ~34 % | Überlastet | Nicht empfohlen |

**Empfehlung**: Diesel bei 70–80 % Last betreiben, 10–15 % der
Leistung zum Laden nutzen. Ein 150 kW Diesel lädt dann mit ca.
15–22 kW die Batterie.

#### 4.5.3 Bremsenergie-Rückgewinnung (Motoryachten)

Bei Geschwindigkeitsreduzierung und Rückwärtsfahrt kann der E-Motor
als Generator arbeiten. Typische Rückgewinnung: 3–8 % der
Gesamtenergie pro Fahrt (gering, da Boote selten bremsen).

---
---

## 5. Batteriesysteme und Energiespeicher

### 5.1 Batterie-Chemie im Vergleich

| Eigenschaft | LiFePO4 (LFP) | NMC (Li-Ion) | Blei-Säure (AGM) | LTO |
|------------|---------------|-------------|------------------|-----|
| Nennspannung/Zelle | 3,2 V | 3,7 V | 2,0 V | 2,3 V |
| Energiedichte (Wh/kg) | 130–170 | 180–260 | 30–45 | 70–90 |
| Energiedichte (Wh/L) | 250–350 | 400–700 | 80–120 | 130–180 |
| Zyklenlebensdauer | 3.000–5.000 | 1.000–2.000 | 300–600 | 10.000–20.000 |
| Selbstentladung (%/Monat) | 1–3 % | 2–5 % | 3–5 % | 2–4 % |
| Thermische Stabilität | Sehr hoch (270 °C) | Mittel (150–200 °C) | Hoch | Sehr hoch (250+ °C) |
| Thermal Runaway Risiko | Sehr gering | Vorhanden | Nein | Nein |
| Tiefentlade-Toleranz | Gut (bis 10 % SoC) | Schlecht (min 20 %) | Schlecht (max 50 %) | Sehr gut (bis 0 %) |
| Ladegeschwindigkeit | 1C Standard | 0,5–1C | 0,2C | 5–10C möglich |
| Temperaturbereich | −20 bis +60 °C | −10 bis +45 °C | −20 bis +50 °C | −40 bis +55 °C |
| Preis (EUR/kWh, 2026) | 250–400 | 200–350 | 100–180 | 500–800 |
| Marineeignung | ★★★★★ | ★★★★☆ | ★★☆☆☆ | ★★★★☆ |

**Empfehlung für Yachtantrieb:**
- **LiFePO4**: Standard-Empfehlung. Sicherste Lithium-Chemie,
  hervorragende Zyklenfestigkeit, robust gegen Missbrauch.
- **NMC**: Für Hochleistungsanwendungen (Torqeedo Deep Blue).
  Höhere Energiedichte, aber Thermal-Runaway-Risiko erfordert
  besseres BMS und Brandschutz.
- **Blei-Säure**: Nur für Niedrigleistungs-Anwendungen (< 2 kW)
  oder als Starterbatterie. Für Antriebsbatterien nicht empfohlen.
- **LTO (Lithium-Titanat)**: Premium-Lösung für Fähren und
  kommerzielle Schiffe. Extrem zyklenfest, schnellladefähig,
  aber teuer und geringe Energiedichte.

### 5.2 Victron Energy LiFePO4 Batterien

| Modell | Kapazität | Spannung | Energie | Gewicht | Zyklen | Preis (EUR) |
|--------|----------|---------|---------|---------|--------|------------|
| Smart Lithium 12,8V/100Ah | 100 Ah | 12,8 V | 1,28 kWh | 12 kg | 2.500 | 950–1.100 |
| Smart Lithium 12,8V/200Ah | 200 Ah | 12,8 V | 2,56 kWh | 22 kg | 2.500 | 1.800–2.100 |
| Smart Lithium 12,8V/330Ah | 330 Ah | 12,8 V | 4,22 kWh | 37 kg | 2.500 | 2.800–3.200 |
| Lynx Smart BMS 500 | — | 12/24/48 V | — | — | — | 480–550 |

**Victron 48 V Konfiguration (4S Parallel):**
- 4 × Smart Lithium 12,8V/200Ah in Serie = 51,2 V / 200 Ah = 10,24 kWh
- Gewicht: 4 × 22 kg = 88 kg
- Preis: 4 × 1.950 EUR + BMS = ~8.300 EUR
- Zyklen: 2.500 bei 80 % DoD
- Gesamtenergie über Lebensdauer: 10,24 × 2.500 × 0,8 = 20.480 kWh

**Victron-System-Vorteile:**
- Bluetooth-Monitoring (VictronConnect App)
- VE.Bus/VE.Can Vernetzung mit Ladegeräten, Wechselrichtern
- GX-Gerät (Cerbo GX) als zentrale Steuerung
- VRM-Portal: Cloud-Monitoring aller Batteriedaten
- Große Installationsbasis → viele Fachbetriebe

### 5.3 Mastervolt MLI-Serie

| Modell | Kapazität | Spannung | Energie | Gewicht | Zyklen | Preis (EUR) |
|--------|----------|---------|---------|---------|--------|------------|
| MLI Ultra 12/1250 | 100 Ah | 12 V | 1,25 kWh | 11 kg | 3.500 | 1.400–1.600 |
| MLI Ultra 12/2750 | 220 Ah | 12 V | 2,75 kWh | 22 kg | 3.500 | 2.800–3.200 |
| MLI Ultra 12/5500 | 440 Ah | 12 V | 5,50 kWh | 42 kg | 3.500 | 5.200–5.800 |
| MLI Ultra 24/1250 | 50 Ah | 24 V | 1,25 kWh | 12 kg | 3.500 | 1.500–1.700 |
| MLI Ultra 24/2750 | 110 Ah | 24 V | 2,75 kWh | 23 kg | 3.500 | 3.000–3.400 |
| MLI Ultra 24/5500 | 220 Ah | 24 V | 5,50 kWh | 43 kg | 3.500 | 5.500–6.200 |

**Mastervolt-Besonderheiten:**
- Integriertes BMS (kein externes BMS nötig)
- MasterBus-Vernetzung
- IP65-Schutzklasse (spritzwassergeschützt)
- Stapelbar (modular erweiterbar)
- CZone-kompatibel (Mastervolt-Steuerungssystem)
- 3.500 Zyklen bei 80 % DoD (Premium-Zellen)

### 5.4 Weitere Batterie-Hersteller (marine-zertifiziert)

| Hersteller | Modellreihe | Chemie | kWh-Bereich | Preis/kWh (EUR) | Besonderheit |
|-----------|------------|--------|------------|----------------|-------------|
| Lithionics | NeverDie | LiFePO4 | 1–40 kWh | 350–500 | US-Marine-Standard |
| RELiON | InSight | LiFePO4 | 1–6 kWh | 300–450 | Drop-In-Ersatz |
| Super B | Epsilon | LiFePO4 | 1–8 kWh | 350–500 | Racing/Marine |
| MG Energy | HE/HP Serie | LiFePO4/NMC | 5–50 kWh | 280–400 | Niederländisch |
| Pylontech | US-Serie | LiFePO4 | 2,5–5 kWh | 200–280 | Budget (nicht marinisiert!) |
| BYD | LVS/LVL | LiFePO4 | 4–64 kWh | 180–250 | Budget (nicht marinisiert!) |
| Torqeedo | Power/DB | LiFePO4/NMC | 3,5–33 kWh | 700–900 | Proprietär, teuer |
| Oceanvolt | Aqua | LiFePO4 | 10–30 kWh | 400–550 | Abgestimmt auf Oceanvolt |

**Warnung**: Pylontech und BYD Batterien sind NICHT marinisiert!
Sie haben keine IP65/67-Schutzklasse, kein Salzwasser-taugliches
Gehäuse und keine Marine-Zertifizierung. Einsatz auf Booten auf
eigenes Risiko und meist nicht versicherbar. Trotzdem werden sie
aufgrund des niedrigen Preises häufig verbaut — besonders in der
Binnenfahrt (Grachtenboote, Hausboote).

### 5.5 Batterie-Dimensionierung (kWh-Sizing)

#### 5.5.1 Bestimmung des Energiebedarfs

**Schritt 1: Antriebsenergie berechnen**

| Bootstyp (Verdränger) | Leistung bei 5 kn | Leistung bei 6 kn | Leistung bei 7 kn |
|-----------------------|-------------------|-------------------|-------------------|
| Segelboot 8 m (3 t) | 0,8 kW | 1,5 kW | 3,0 kW |
| Segelboot 10 m (5 t) | 1,2 kW | 2,5 kW | 5,0 kW |
| Segelboot 12 m (8 t) | 2,0 kW | 4,0 kW | 8,0 kW |
| Segelboot 14 m (12 t) | 3,0 kW | 6,0 kW | 12,0 kW |
| Motoryacht 10 m (6 t) | 1,5 kW | 3,0 kW | 6,5 kW |
| Motoryacht 12 m (10 t) | 2,5 kW | 5,0 kW | 10,0 kW |
| Motoryacht 14 m (15 t) | 3,5 kW | 7,0 kW | 15,0 kW |
| Katamaran 12 m (8 t) | 1,5 kW | 3,0 kW | 6,0 kW |

**Schritt 2: Bordverbrauch addieren**

| Verbraucher | Typische Leistung | Nutzungsdauer/Tag | Energie/Tag |
|------------|-------------------|------------------|------------|
| Autopilot | 30–80 W | 8–24 h | 0,5–1,5 kWh |
| Navigation/Plotter | 15–40 W | 8–16 h | 0,2–0,5 kWh |
| Kühlschrank | 40–80 W | 24 h (Zyklus ~40 %) | 0,4–0,8 kWh |
| LED-Beleuchtung | 20–60 W | 4–8 h | 0,1–0,4 kWh |
| Ankerwinde | 800–1.500 W | 0,1 h | 0,1–0,2 kWh |
| Bugstrahler | 2.000–5.000 W | 0,05 h | 0,1–0,3 kWh |
| Heizung (Webasto) | 300–1.000 W | 8 h (Winter) | 2,4–8,0 kWh |
| Klimaanlage | 1.500–3.000 W | 8 h (Sommer) | 12–24 kWh |
| Inverter-Grundlast | 15–30 W | 24 h | 0,4–0,7 kWh |
| Laptop/Laden | 50–100 W | 4 h | 0,2–0,4 kWh |
| **Summe (Segelboot)** | — | — | **2–6 kWh/Tag** |
| **Summe (Motoryacht)** | — | — | **5–35 kWh/Tag** |

**Schritt 3: Batterie-Sizing-Formel**

```
kWh_brutto = (P_antrieb × t_stunden + E_bord_tag) / DoD_max / η_system

Dabei:
  P_antrieb  = Antriebsleistung (kW) bei gewünschter Geschwindigkeit
  t_stunden  = Gewünschte Motorlaufzeit (h)
  E_bord_tag = Täglicher Bordverbrauch (kWh)
  DoD_max    = Maximale Entladetiefe (0,80 für LiFePO4, 0,70 für NMC)
  η_system   = Systemwirkungsgrad (0,90)
```

#### 5.5.2 Praxisbeispiele Batterie-Sizing

**Beispiel 1: Segelboot 10 m, rein-elektrisch**
- Anforderung: 2 h Motorbetrieb bei 5 kn + 1 Tag Bordverbrauch
- Antriebsenergie: 1,2 kW × 2 h = 2,4 kWh
- Bordverbrauch: 3,0 kWh
- kWh_brutto = (2,4 + 3,0) / 0,80 / 0,90 = 7,5 kWh
- **Empfehlung: 8–10 kWh (z.B. 2 × Victron 12,8V/200Ah in Serie = 51,2V/200Ah = 10,24 kWh → falsch, 4S nötig für 48V)**
- **Korrektur: 4 × Victron 12,8V/100Ah in Serie = 51,2V/100Ah = 5,12 kWh (zu wenig)**
- **Richtig: 4S2P = 8 × Victron 12,8V/100Ah = 51,2V/200Ah = 10,24 kWh → 8.800 EUR**

**Beispiel 2: Motoryacht 12 m, Parallel-Hybrid (elektrisch für 1 h Manöver)**
- Anforderung: 1 h bei 4 kn + 0,5 h Bugstrahlmanöver
- Antriebsenergie: 3,0 kW × 1 h = 3,0 kWh
- Bugstrahler: 3,0 kW × 0,5 h = 1,5 kWh
- Bordverbrauch (1 h): 0,3 kWh
- kWh_brutto = (3,0 + 1,5 + 0,3) / 0,80 / 0,90 = 6,7 kWh
- **Empfehlung: 8–10 kWh**

**Beispiel 3: Katamaran 12 m, rein-elektrisch (Langfahrt)**
- Anforderung: 8 h Motorbetrieb bei 5 kn (2 × Motoren)
- Antriebsenergie: 2 × 1,2 kW × 8 h = 19,2 kWh
- Bordverbrauch: 5,0 kWh
- kWh_brutto = (19,2 + 5,0) / 0,80 / 0,90 = 33,6 kWh
- **Empfehlung: 35–40 kWh (z.B. 2 × ePropulsion E175 = 35 kWh → 21.000 EUR)**

### 5.6 Batterie-Platzierung und Gewichtsverteilung

| Position | Vorteile | Nachteile | Empfehlung |
|---------|----------|-----------|-----------|
| Bilge (mittschiffs) | Tiefer Schwerpunkt, keine Trimänderung | Feuchtigkeit, Zugang schwer | ★★★★★ Ideal für Segelboote |
| Unter Salon-Sole | Zentraler Schwerpunkt | Zugang bei Wartung | ★★★★☆ Gut für Motoryachten |
| Motorraum | Kurze Kabelwege | Hitze, Vibration | ★★★☆☆ Nur wenn thermisch isoliert |
| Achterpiek | Einfache Installation | Hecklastig, Trimprobleme | ★★☆☆☆ Nur mit Trimmberechnung |
| Vorpiek | — | Buglastig, Seeschlagrisiko | ★☆☆☆☆ Nicht empfohlen |
| Kiel (Segelboot) | Tiefster Schwerpunkt | Spezial-Kiel nötig | ★★★★★ Premium (Oceanvolt) |

**Gewichtsfaustregeln:**
- LiFePO4: ~7 kg/kWh (inkl. Gehäuse und BMS)
- NMC: ~5 kg/kWh (inkl. Gehäuse und BMS)
- Blei-Säure: ~28 kg/kWh

**Trimmkritische Grenze:**
- Asymmetrische Batterieplatzierung max. 5 % der Gesamtverdrängung
- Trimänderung durch Batterie max. 0,5° (Segelboot) / 0,3° (Motoryacht)

### 5.7 Batterie-Sicherheit und Brandschutz

#### 5.7.1 Thermal Runaway — Risikobewertung

| Chemie | Thermal Runaway Temperatur | Gasfreisetzung | Brandrisiko | Marine-Eignung |
|--------|---------------------------|---------------|-------------|---------------|
| LiFePO4 | > 270 °C | Gering | Sehr gering | Empfohlen |
| NMC | > 150–200 °C | Hoch (HF, CO) | Mittel–Hoch | Nur mit Schutz |
| NCA | > 130–150 °C | Sehr hoch | Hoch | Nicht empfohlen |
| LTO | > 250 °C | Gering | Sehr gering | Empfohlen |

#### 5.7.2 Schutzmaßnahmen (obligatorisch)

1. **Belüftung**: Batterieraum muss belüftet sein (ISO 10133, ABYC E-13).
   Mindestens 2 × Querschnitt der Kabeleinführung als Lüftungsöffnung.
2. **Temperatursensor**: BMS muss Zelltemperatur überwachen.
   Abschaltung bei > 60 °C (LiFePO4) bzw. > 45 °C (NMC).
3. **Sicherung**: Jeder Batteriestrang mit ANL-/MEGA-Sicherung.
   Auslösezeit < 10 ms bei Kurzschluss.
4. **Trennschalter**: Manueller Not-Aus in Reichweite des Rudergängers.
5. **Brandschutz**: Feuerlöscher (CO₂ oder Lithiumbatterie-Löscher)
   in Batterienähe. Kein Wasser auf Lithium-Brände!
6. **Gasdetektor**: Bei NMC-Batterien Gasdetektor für Fluorwasserstoff
   (HF) empfohlen. Bei LiFePO4 nicht zwingend.
7. **Isolationswächter**: Bei Hochvolt-Systemen (> 60 V) obligatorisch
   gemäß ISO 16315.

---
---

## 6. Batterie-Management-Systeme (BMS)

### 6.1 Aufgaben des BMS

Das BMS ist das „Gehirn" des Batteriespeichers:

| Funktion | Beschreibung | Kritikalität |
|---------|-------------|-------------|
| Zellspannungs-Überwachung | Jede Zelle einzeln messen (3,0–3,65 V bei LFP) | Kritisch |
| Zellbalancing | Spannungsunterschiede ausgleichen (passiv/aktiv) | Wichtig |
| Strom-Überwachung | Lade-/Entladestrom messen, begrenzen | Kritisch |
| Temperatur-Überwachung | Zelltemperatur messen (min. 2 Sensoren/Pack) | Kritisch |
| SoC-Berechnung | State of Charge (Ladezustand) berechnen | Wichtig |
| SoH-Tracking | State of Health (Gesundheitszustand) über Lebensdauer | Nützlich |
| Über-/Unterspannungsschutz | Abschaltung bei Grenzwerten | Kritisch |
| Überstromschutz | Abschaltung bei zu hohem Strom | Kritisch |
| Kurzschlussschutz | Sofortige Abschaltung (< 1 ms) | Kritisch |
| Kommunikation | CAN-Bus, Bluetooth, VE.Can, Modbus | Nützlich |
| Logging | Lade-/Entladezyklen, Fehler protokollieren | Nützlich |
| Heizungssteuerung | Batterieheizung bei < 5 °C aktivieren | Wichtig (Winter) |

### 6.2 BMS-Topologien

#### Zentrales BMS
- Ein Steuergerät, Kabel zu jeder Zelle
- Vorteile: Einfach, preiswert
- Nachteile: Viele Kabel, Einzelpunktversagen
- Beispiel: Victron Lynx Smart BMS

#### Verteiltes BMS
- Slave-Module an jedem Zellpack, Master als Zentrale
- Vorteile: Modularer Aufbau, kurze Sensorleitungen
- Nachteile: Mehr Elektronik, teurer
- Beispiel: Mastervolt MLI (integriert)

#### Integriertes BMS
- BMS direkt in Batterie integriert
- Vorteile: Plug-and-Play, kein externer Verdrahtungsaufwand
- Nachteile: Nicht aufrüstbar, proprietär
- Beispiel: ePropulsion E-Serie, Torqeedo Power

### 6.3 BMS-Parameter für LiFePO4 (48 V / 16S Konfiguration)

| Parameter | Wert | Hysterese | Aktion |
|-----------|------|----------|--------|
| Zellspannung max. (Ladeschluss) | 3,65 V | −0,05 V | Laden stoppen |
| Zellspannung min. (Entladeschluss) | 2,80 V | +0,10 V | Entladen stoppen |
| Zell-Differenzspannung max. | 0,05 V | — | Balancing aktivieren |
| Packspannung max. (16S) | 58,4 V | −0,8 V | Laden stoppen |
| Packspannung min. (16S) | 44,8 V | +1,6 V | Entladen stoppen |
| Max. Ladestrom | 1C (z.B. 200 A bei 200 Ah) | — | Laden begrenzen |
| Max. Entladestrom | 2C (z.B. 400 A bei 200 Ah) | — | Entladen begrenzen |
| Max. Kurzschlussstrom | 10C (z.B. 2.000 A) | < 1 ms | Sofort trennen |
| Temperatur max. (Entladen) | 60 °C | −5 °C | Entladen stoppen |
| Temperatur max. (Laden) | 45 °C | −5 °C | Laden stoppen |
| Temperatur min. (Laden) | 0 °C | +5 °C | Laden stoppen (Lithium-Plating!) |
| Temperatur min. (Entladen) | −20 °C | +5 °C | Entladen stoppen |

**Kritisch: Laden unter 0 °C**
LiFePO4-Zellen dürfen NICHT unter 0 °C geladen werden! Lithium-Ionen
lagern sich als metallisches Lithium ab (Lithium-Plating), was die
Kapazität irreversibel reduziert und im Extremfall zu Kurzschlüssen
führt. Ein gutes BMS sperrt den Ladeeingang bei < 0 °C Zelltemperatur
und aktiviert optional eine Batterieheizung.

### 6.4 SoC-Bestimmung (State of Charge)

| Methode | Genauigkeit | Beschreibung |
|---------|-----------|-------------|
| Coulomb-Counting | ±2–5 % | Integration des Stroms über Zeit |
| Spannungsmessung (OCV) | ±5–10 % | Ruhespannung → SoC-Kennlinie (bei LFP sehr flach!) |
| Impedanzmessung (EIS) | ±1–3 % | Innenwiderstandsmessung (aufwändig) |
| Kalman-Filter | ±1–3 % | Kombination aus Strom + Spannung + Modell |
| Neuronales Netz | ±1–2 % | KI-basiert, trainiert auf Zelltyp |

**Problem bei LiFePO4:**
Die Spannungskurve von LiFePO4 ist zwischen 20 % und 80 % SoC extrem
flach (~3,2–3,3 V). Spannungsbasierte SoC-Schätzung ist daher
ungenau. Coulomb-Counting mit regelmäßiger Kalibrierung (bei 100 %
und 0 %) ist Standard.

### 6.5 Kommunikationsschnittstellen

| Protokoll | Geschwindigkeit | Verbreitung (Marine) | Anwendung |
|----------|----------------|---------------------|-----------|
| CAN-Bus (NMEA 2000) | 250 kbit/s | Hoch | Motorsteuerung, BMS ↔ Charger |
| VE.Can (Victron) | 250 kbit/s | Hoch (Victron) | BMS ↔ Ladegerät ↔ Inverter |
| VE.Direct (Victron) | 19.200 baud | Hoch (Victron) | MPPT ↔ GX-Gerät |
| MasterBus (Mastervolt) | 250 kbit/s | Mittel | Mastervolt-Ökosystem |
| Modbus TCP/RTU | Variabel | Mittel | Industrie-Integration |
| Bluetooth (BLE) | 1 Mbit/s | Hoch (Monitoring) | App-Verbindung |
| Wi-Fi | 54+ Mbit/s | Mittel | Cloud-Upload, Remote |
| RS485 | 9.600–115.200 | Gering | Legacy-Systeme |

---
---

## 7. Reichweite und Energieberechnung

### 7.1 Reichweiten-Berechnungsformel

```
Reichweite (sm) = (E_batterie × DoD × η_system) / (P_antrieb / v_knoten + P_bord / v_knoten)

Vereinfacht:
Reichweite (sm) = E_nutzbar / E_pro_sm

Dabei:
  E_nutzbar   = kWh_brutto × DoD × η_system
  E_pro_sm    = P_antrieb / v_knoten  [kWh/sm]
  P_bord      = Bordverbraucher [kW] (ca. 0,1–0,5 kW)
```

### 7.2 Reichweiten-Tabelle (Verdränger, LiFePO4, 80 % DoD)

#### Segelboot 10 m (5 t Verdrängung)

| Geschwindigkeit | Leistung | kWh/sm | 10 kWh Batterie | 20 kWh Batterie | 30 kWh Batterie |
|----------------|---------|--------|----------------|----------------|----------------|
| 3 kn (Minimal) | 0,5 kW | 0,17 | 47 sm | 94 sm | 141 sm |
| 4 kn (Spazier) | 0,8 kW | 0,20 | 40 sm | 80 sm | 120 sm |
| 5 kn (Normal) | 1,2 kW | 0,24 | 33 sm | 67 sm | 100 sm |
| 6 kn (Schnell) | 2,5 kW | 0,42 | 19 sm | 38 sm | 57 sm |
| 7 kn (Rumpf) | 5,0 kW | 0,71 | 11 sm | 22 sm | 34 sm |

#### Motoryacht 12 m (10 t Verdrängung)

| Geschwindigkeit | Leistung | kWh/sm | 20 kWh Batterie | 40 kWh Batterie | 80 kWh Batterie |
|----------------|---------|--------|----------------|----------------|----------------|
| 4 kn (Minimal) | 1,5 kW | 0,38 | 42 sm | 84 sm | 168 sm |
| 5 kn (Spazier) | 2,5 kW | 0,50 | 32 sm | 64 sm | 128 sm |
| 6 kn (Normal) | 5,0 kW | 0,83 | 19 sm | 38 sm | 77 sm |
| 7 kn (Schnell) | 10,0 kW | 1,43 | 11 sm | 22 sm | 45 sm |
| 7,5 kn (Rumpf) | 15,0 kW | 2,00 | 8 sm | 16 sm | 32 sm |

#### Katamaran 12 m (8 t Verdrängung, 2 × Motoren)

| Geschwindigkeit | Leistung (2×) | kWh/sm | 20 kWh | 40 kWh | 60 kWh |
|----------------|-------------|--------|--------|--------|--------|
| 4 kn | 1,2 kW | 0,30 | 53 sm | 107 sm | 160 sm |
| 5 kn | 2,0 kW | 0,40 | 40 sm | 80 sm | 120 sm |
| 6 kn | 3,5 kW | 0,58 | 28 sm | 55 sm | 83 sm |
| 7 kn | 6,0 kW | 0,86 | 19 sm | 37 sm | 56 sm |
| 8 kn | 10,0 kW | 1,25 | 13 sm | 26 sm | 38 sm |

### 7.3 Geschwindigkeitsreduktion als Reichweitenhebel

Die Antriebsleistung steigt mit der dritten Potenz der Geschwindigkeit
(bei Verdrängerfahrt):

```
P₂/P₁ = (v₂/v₁)³
```

Das bedeutet: **10 % langsamer = 27 % weniger Leistungsbedarf = 23 % mehr Reichweite!**

| Geschwindigkeitsreduktion | Leistungsersparnis | Reichweitengewinn |
|--------------------------|-------------------|-------------------|
| −5 % | −14 % | +11 % |
| −10 % | −27 % | +23 % |
| −15 % | −39 % | +38 % |
| −20 % | −49 % | +56 % |
| −25 % | −58 % | +78 % |
| −30 % | −66 % | +104 % |
| −50 % | −88 % | +300 % |

**Praxis-Empfehlung**: Bei knapper Batteriekapazität die Geschwindigkeit
um 15–20 % reduzieren. Das erhöht die Reichweite um rund 40–55 %
(die Betriebsdauer nähert sich dabei der Verdopplung).

> ✅ Aufgeloest (Audit): Reichweitengewinn ∝ 1/v² (nicht 1/v³) bei P ∝ v³ — Reichweite = v · t mit t = E/P ∝ 1/v³, also Reichweite ∝ 1/v². Spalte korrigiert (−10 % ⇒ +23 %, −20 % ⇒ +56 %, −50 % ⇒ +300 %); die ursprünglichen Werte waren der Betriebsdauergewinn (∝ 1/v³). Quelle: „Cube law"/Propeller-Gesetz für Verdrängerrümpfe (Widerstandsleistung P ∝ v³), en.wikipedia.org/wiki/Hull_speed; boatdesign.net.

### 7.4 Einflussfaktoren auf die Reichweite

| Faktor | Einfluss | Typische Abweichung |
|--------|---------|-------------------|
| Gegenwind (20 kn) | Erhöhter Widerstand | −15 bis −30 % |
| Gegenstrom (1 kn) | Reduzierte Grundgeschwindigkeit | −15 bis −25 % |
| Bewuchs am Rumpf | Erhöhter Reibungswiderstand | −5 bis −20 % |
| Seegang (1 m Wellenhöhe) | Wellenwiderstands-Zuschlag | −10 bis −25 % |
| Beladung (+20 %) | Erhöhte Verdrängung | −5 bis −10 % |
| Kalte Batterie (< 10 °C) | Reduzierte Kapazität | −10 bis −20 % |
| Alte Batterie (80 % SoH) | Reduzierte Kapazität | −20 % |
| Propellerzustand (schlecht) | Wirkungsgradverlust | −5 bis −15 % |

### 7.5 Notreserve und Sicherheitspuffer

**Empfohlene Mindestreserve:**

| Einsatzgebiet | Reserve (% der Kapazität) | Begründung |
|-------------|-------------------------|-----------|
| Binnengewässer (Fluss, See) | 10 % | Nothafen in der Nähe |
| Küstenfahrt (< 5 sm von Land) | 15 % | Wind-/Strömungszuschlag |
| Küstenfahrt (5–20 sm) | 20 % | Wetteränderung möglich |
| Offshore (> 20 sm) | 25 % | Sicherheitskritisch |

**Empfehlung**: In der Reichweitenanzeige des Antriebssystems die
Reserve berücksichtigen. Torqeedo und ePropulsion zeigen GPS-basierte
Restreichweite an — diese Systeme berücksichtigen Wind und Strom
NICHT automatisch. Angezeigte Werte sind optimistisch.

---
---

## 8. Ladeinfrastruktur und Energiequellen

### 8.1 Landstrom (Shore Power)

#### 8.1.1 Ladegeräte für LiFePO4-Antriebsbatterien

| Ladegerät | Leistung | Eingang | Ausgang | Preis (EUR) |
|----------|---------|--------|---------|------------|
| Victron Centaur 24/60 | 1,44 kW | 230 V AC | 24 V / 60 A | 400–480 |
| Victron Centaur 24/100 | 2,40 kW | 230 V AC | 24 V / 100 A | 550–650 |
| Victron Skylla-IP65 24/35 | 0,84 kW | 230 V AC | 24 V / 35 A | 480–560 |
| Victron Skylla-IP44 48/50 | 2,40 kW | 230 V AC | 48 V / 50 A | 650–750 |
| Victron Skylla-IP44 48/100 | 4,80 kW | 230 V AC | 48 V / 100 A | 1.200–1.400 |
| Mastervolt ChargeMaster Plus 24/80 | 1,92 kW | 230 V AC | 24 V / 80 A | 800–950 |
| Mastervolt ChargeMaster Plus 48/50 | 2,40 kW | 230 V AC | 48 V / 50 A | 1.000–1.200 |
| Torqeedo Fast Charger 48V | 3,50 kW | 230 V AC | 48 V / 70 A | 1.800–2.200 |
| Torqeedo Deep Blue Charger | 22,0 kW | 400 V 3ph AC | 345 V DC | 5.500–6.500 |

#### 8.1.2 Ladezeiten (typisch)

| Batterie-Kapazität | 1 kW Lader | 2,5 kW Lader | 5 kW Lader | 22 kW Lader |
|-------------------|-----------|-------------|-----------|------------|
| 5 kWh | 5 h | 2 h | 1 h | 15 min |
| 10 kWh | 10 h | 4 h | 2 h | 30 min |
| 20 kWh | 20 h | 8 h | 4 h | 1 h |
| 40 kWh | 40 h | 16 h | 8 h | 2 h |
| 100 kWh | 100 h | 40 h | 20 h | 5 h |

**Praxis**: Die meisten Yachten laden über Nacht am Steg mit
1–5 kW Landstrom. Für 10–20 kWh Batterien reicht eine Nacht (8–12 h).
Schnellladen (22 kW, 3-phasig) erfordert einen CEE-32A-Anschluss,
der in vielen Marinas verfügbar ist.

### 8.2 Solarenergie

#### 8.2.1 Solarpanel-Technologien für Boote

| Technologie | Wirkungsgrad | Flexibel? | Salzwasser-tauglich? | Preis (EUR/Wp) |
|------------|-----------|----------|---------------------|---------------|
| Monokristallin (starr) | 20–23 % | Nein | Ja (Alu-Rahmen) | 0,50–0,80 |
| Monokristallin (semi-flex) | 18–22 % | Ja (< 30°) | Bedingt (Laminierung) | 1,00–1,50 |
| Monokristallin (flexibel) | 15–19 % | Ja (< 60°) | Bedingt | 1,50–2,50 |
| Dünnschicht (CIGS) | 12–16 % | Ja | Bedingt | 1,80–3,00 |
| Perowskit (emerging) | 15–20 % | Ja | In Entwicklung | Noch nicht verfügbar |

#### 8.2.2 Solarertrag nach Bootstyp und Fläche

| Boot | Verfügbare Fläche | Installiert (Wp) | Tagesertrag (kWh)* | Jahresertrag (kWh)* |
|------|-------------------|------------------|--------------------|--------------------|
| Segelboot 10 m (Bimini) | 2–3 m² | 400–600 Wp | 1,5–2,5 kWh | 500–800 kWh |
| Segelboot 12 m (Arch) | 3–5 m² | 600–1.000 Wp | 2,5–4,0 kWh | 800–1.300 kWh |
| Katamaran 12 m (Dach) | 8–15 m² | 1.600–3.000 Wp | 6,0–12,0 kWh | 2.000–4.000 kWh |
| Motoryacht 12 m (Flybridge) | 5–10 m² | 1.000–2.000 Wp | 4,0–8,0 kWh | 1.300–2.600 kWh |
| Motoryacht 18 m (Dach) | 10–20 m² | 2.000–4.000 Wp | 8,0–16,0 kWh | 2.600–5.200 kWh |

*Mittelmeer/Karibik, Jahresmittel ~4,5 Sonnenstunden/Tag.

#### 8.2.3 MPPT-Laderegler

| Regler | Max. PV-Leistung | Batteriespannung | Preis (EUR) |
|--------|-----------------|-----------------|------------|
| Victron SmartSolar 100/30 | 440 W (12V) | 12/24/48 V | 180–220 |
| Victron SmartSolar 150/45 | 650 W (12V) | 12/24/48 V | 280–340 |
| Victron SmartSolar 250/100 | 1.450 W (12V) | 12/24/48 V | 550–650 |
| Victron SmartSolar RS 450/100 | 6.500 W | 48 V | 650–750 |
| Victron SmartSolar RS 450/200 | 13.000 W | 48 V | 1.100–1.300 |
| Mastervolt SCM60 | 900 W (12V) | 12/24 V | 350–420 |

### 8.3 Hydro-Regeneration

Hydro-Regeneration ist die Energierückgewinnung durch den freidrehenden
Propeller beim Segeln oder bei Strömung. Siehe Kapitel 4.5.1 für
detaillierte Daten.

**Zusammenfassung Hydro-Regeneration:**
- Nur bei Segelbooten sinnvoll (lange Segelstrecken)
- Typische Leistung: 0,3–2,0 kW bei 5–8 Knoten
- Tagesertrag: 5–15 kWh (bei gutem Wind)
- Deckt auf Langfahrt den Bordverbrauch vollständig
- Oceanvolt ServoProp hat die beste Hydro-Regen-Effizienz
- Nachteil: Bremseffekt (~0,3–0,8 Knoten Geschwindigkeitsverlust)

### 8.4 Windgeneratoren (ergänzende Energiequelle)

| Modell | Leistung (Nenn) | Windstärke | Ertrag/Tag (20 kn) | Preis (EUR) |
|--------|---------------|-----------|-------------------|------------|
| Superwind 350 | 350 W | ab 3 Bft | 3–5 kWh | 1.800–2.200 |
| Silentwind 400+ | 420 W | ab 3 Bft | 4–6 kWh | 2.000–2.500 |
| Rutland 1200 | 500 W | ab 3 Bft | 5–8 kWh | 1.500–1.800 |
| Leading Edge LE-300 | 300 W | ab 3 Bft | 2–4 kWh | 1.200–1.500 |

### 8.5 Diesel-Generator (Range Extender)

Für Hybrid-Systeme und als Notfall-Ladequelle:

| Generator | Leistung | Gewicht | Verbrauch | Preis (EUR) |
|----------|---------|---------|----------|------------|
| Fischer Panda iSeries 4000i | 3,5 kW | 62 kg | 1,2 L/h | 8.500–9.500 |
| Fischer Panda iSeries 8000i | 7,0 kW | 85 kg | 2,1 L/h | 12.000–13.500 |
| Fischer Panda iSeries 15000i | 13,0 kW | 145 kg | 3,5 L/h | 18.000–20.000 |
| Whisper Power GV4 | 3,5 kW | 58 kg | 1,1 L/h | 7.500–8.500 |
| Onan/Cummins MDKBU 5 | 5,0 kW | 120 kg | 1,8 L/h | 9.000–10.500 |
| Mastervolt Alpha Pro 3 | 3,0 kW | 55 kg | 1,0 L/h | 6.500–7.500 |

**Auslegung Range Extender:**
- Generator-Leistung ≥ Durchschnittliche Antriebsleistung (für unbegrenzte Reichweite)
- Generator-Leistung < Antriebsleistung → Batterie als Puffer nutzen
- Dieselverbrauch: ~0,3 L/kWh (Generator) vs. ~0,25 L/kWh (Direktantrieb)
- Vorteil: Generator läuft bei konstantem, optimalem Lastpunkt

### 8.6 Brennstoffzelle (Zukunftstechnologie)

| Hersteller | Modell | Leistung | Brennstoff | Gewicht | Preis (EUR) |
|-----------|--------|---------|-----------|---------|------------|
| EFOY | Pro 2800 | 125 W | Methanol | 8 kg | 4.500–5.500 |
| EFOY | Hydrogen 2.5 | 2,5 kW | Wasserstoff | 25 kg | 25.000–30.000 |
| Toyota (marine) | FC-Modul | 80 kW | Wasserstoff | 250 kg | In Erprobung |
| PowerCell | PS-5 | 5 kW | Wasserstoff | 40 kg | 35.000–45.000 |

**Status 2026**: Methanol-Brennstoffzellen (EFOY) sind etabliert als
Bordstromversorgung (Segelboote, Wohnmobile). Wasserstoff-BZ für
den Hauptantrieb sind noch in der Demonstrationsphase. Infrastruktur
(Wasserstoff-Tankstellen in Marinas) fehlt weitgehend.

### 8.7 Energiebilanz-Szenarien (Tagesbetrachtung)

#### Szenario 1: Segelboot 12 m, Mittelmeer-Sommertag

| Energiequelle / Verbraucher | Eingang (kWh) | Ausgang (kWh) |
|----------------------------|-------------|-------------|
| Solar (600 Wp, 5 h Sonne) | +3,0 | — |
| Hydro-Regen (6 kn, 6 h Segeln) | +2,4 | — |
| Motorfahrt (1 h Ein-/Auslaufen, 5 kn) | — | −1,3 |
| Kühlschrank (24 h) | — | −0,6 |
| Navigation + Autopilot (8 h) | — | −0,5 |
| LED-Beleuchtung (4 h) | — | −0,2 |
| Laden Geräte (Handy, Laptop) | — | −0,3 |
| **Tagesbilanz** | **+5,4** | **−2,9** |
| **Netto** | **+2,5 kWh** | |

Ergebnis: Batterie wird voller → Energieautarkie erreicht.

#### Szenario 2: Motoryacht 12 m, Binnenkanal-Tagestour

| Energiequelle / Verbraucher | Eingang (kWh) | Ausgang (kWh) |
|----------------------------|-------------|-------------|
| Solar (1.200 Wp, 4 h Sonne) | +4,8 | — |
| Motorfahrt (6 h bei 6 kn, 5 kW) | — | −30,0 |
| Klimaanlage (8 h) | — | −12,0 |
| Kühlschrank + Sonstiges | — | −2,0 |
| **Tagesbilanz** | **+4,8** | **−44,0** |
| **Netto** | **−39,2 kWh** | |

Ergebnis: 40 kWh Batterie reicht nicht für einen vollen Tag.
Lösung: Hybrid-Modus oder Reichweite/Geschwindigkeit reduzieren.

#### Szenario 3: Katamaran 12 m, Karibik-Ankertag

| Energiequelle / Verbraucher | Eingang (kWh) | Ausgang (kWh) |
|----------------------------|-------------|-------------|
| Solar (2.400 Wp, 6 h Sonne) | +14,4 | — |
| Kein Motorfahrt | — | 0 |
| Kühlschrank + Tiefkühler | — | −1,5 |
| Watermaker (2 h) | — | −1,2 |
| Klimaanlage (6 h Nacht) | — | −6,0 |
| Navigation, Ankeralarme, Laden | — | −1,0 |
| **Tagesbilanz** | **+14,4** | **−9,7** |
| **Netto** | **+4,7 kWh** | |

Ergebnis: Überschuss → Batterie auf 100 %. Genug Reserve für
nächsten Motorfahrt-Tag.

---
---

## 9. Leistungselektronik und Steuerung

### 9.1 Frequenzumrichter / Motor-Controller

Der Controller wandelt DC-Batteriespannung in die AC-Phasenspannung
für den E-Motor um:

| Parameter | 48 V System | 360 V System |
|-----------|-----------|-------------|
| Eingang | 40–58 V DC | 280–420 V DC |
| Ausgang | 3-Phasen AC (variable Frequenz) | 3-Phasen AC |
| Schaltfrequenz | 8–20 kHz | 8–20 kHz |
| Wirkungsgrad | 96–98 % | 97–99 % |
| Kühlung | Wasser oder Luft | Wasser |
| Schutzklasse | IP54–IP67 | IP54–IP67 |

### 9.2 DC/DC-Wandler

Zur Versorgung des 12/24 V Bordnetzes aus dem Antriebsbatteriepack:

| Modell | Eingang | Ausgang | Leistung | Preis (EUR) |
|--------|--------|--------|---------|------------|
| Victron Orion-Tr 48/12-30 | 48 V | 12 V / 30 A | 360 W | 120–150 |
| Victron Orion-Tr 48/24-16 | 48 V | 24 V / 16 A | 380 W | 130–160 |
| Victron Orion-Tr 48/12-110 | 48 V | 12 V / 110 A | 1.320 W | 350–420 |
| Mastervolt DC Master 48/12-20 | 48 V | 12 V / 20 A | 240 W | 200–250 |
| Mastervolt DC Master 48/12-60 | 48 V | 12 V / 60 A | 720 W | 450–550 |

**Wichtig**: Ein rein-elektrisches Boot hat typischerweise nur EIN
Batteriesystem (z.B. 48 V LiFePO4). Das 12/24 V Bordnetz wird über
DC/DC-Wandler gespeist. Keine separate Starterbatterie nötig (E-Motor
braucht keinen Anlasser).

### 9.3 Wechselrichter (Inverter)

Für 230 V AC Verbraucher an Bord (Bordsteckdosen, Klimaanlage):

| Modell | Leistung | Eingang | Ausgang | Preis (EUR) |
|--------|---------|--------|--------|------------|
| Victron MultiPlus-II 48/3000 | 3.000 VA | 48 V DC | 230 V AC | 1.200–1.400 |
| Victron MultiPlus-II 48/5000 | 5.000 VA | 48 V DC | 230 V AC | 1.800–2.100 |
| Victron Quattro-II 48/10000 | 10.000 VA | 48 V DC | 230 V AC | 3.500–4.000 |
| Mastervolt Mass Combi Ultra 48/3500 | 3.500 VA | 48 V DC | 230 V AC | 2.800–3.200 |

### 9.4 Systemintegration (Victron-Beispiel)

```
┌──────────────┐    ┌─────────────┐    ┌──────────────┐
│  Solarpanels ├────┤ MPPT-Regler ├────┤              │
│              │    │ SmartSolar  │    │              │
└──────────────┘    └─────────────┘    │              │
                                       │   LiFePO4    │
┌──────────────┐    ┌─────────────┐    │   Batterie   │
│  Landstrom   ├────┤ MultiPlus   ├────┤   48 V       │
│  230 V AC    │    │ (Charger +  │    │              │
└──────────────┘    │  Inverter)  │    │              │
                    └──────┬──────┘    └──────┬───────┘
                           │                  │
                    ┌──────┴──────┐    ┌──────┴───────┐
                    │ 230 V AC    │    │ E-Motor      │
                    │ Bordnetz    │    │ Controller   │
                    └─────────────┘    └──────┬───────┘
                                              │
┌──────────────┐    ┌─────────────┐    ┌──────┴───────┐
│  Cerbo GX    ├────┤ Lynx Smart  ├────┤ E-Motor      │
│  (Monitor)   │    │ BMS         │    │ (PMSM)       │
└──────┬───────┘    └─────────────┘    └──────────────┘
       │
┌──────┴───────┐    ┌─────────────┐
│  VRM Portal  │    │ DC/DC 48→12 │→→→ 12 V Bordnetz
│  (Cloud)     │    └─────────────┘
└──────────────┘
```

### 9.5 NMEA 2000 Integration

Elektrische Antriebssysteme sollten in das NMEA 2000 Netzwerk
integriert werden:

| PGN | Beschreibung | Quelle |
|-----|-------------|--------|
| 127488 | Engine Parameters, Rapid Update | E-Motor Controller |
| 127489 | Engine Parameters, Dynamic | E-Motor Controller |
| 127505 | Fluid Level (Batterie als „Tank") | BMS |
| 127506 | DC Detailed Status | BMS |
| 127508 | Battery Status | BMS |
| 130312 | Temperature | BMS (Zelltemperatur) |
| 65280–65535 | Proprietäre PGNs | Herstellerspezifisch |

---
---

## 10. Installation und Integration

### 10.1 Vorplanung und Systemdesign

#### 10.1.1 Checkliste Vorplanung

| Schritt | Detail | Ergebnis |
|---------|--------|---------|
| 1. Bootsdaten | LWL, Breite, Verdrängung, Rumpfform | Basisdaten |
| 2. Einsatzprofil | Revier, Strecken, Geschwindigkeiten, Nutzungsdauer | Anforderungsprofil |
| 3. Energiebedarf | Antrieb + Bord (kWh/Tag) | Batterie-Sizing |
| 4. Platzverhältnisse | Motorraum, Batteriefach, Kabelwege | Einbau-Machbarkeit |
| 5. Gewicht | Motor + Batterie + Kabel vs. alter Diesel + Tank | Trimmberechnung |
| 6. Spannungsebene | 12/24/48/HV — abhängig von Leistung | Systemarchitektur |
| 7. Lademöglichkeiten | Landstrom, Solar, Hydro, Generator | Ladestrategie |
| 8. Budget | Gesamt incl. Installation | Komponentenwahl |
| 9. Normen | CE, ISO 16315, ABYC E-11 | Prüfpflichten |
| 10. Versicherung | E-Antrieb muss gemeldet werden | Versicherungsanpassung |

#### 10.1.2 Gewichtsvergleich Diesel vs. Elektro

| Komponente | Diesel (10 kW / 27 PS) | Elektro (10 kW) |
|-----------|----------------------|----------------|
| Motor | 120–180 kg (Yanmar 3YM30) | 25–35 kg (E-Motor) |
| Getriebe | 25–40 kg | 0–10 kg (Planetar, optional) |
| Kraftstofftank (100 L) | 80–90 kg (voll) | — |
| Abgasanlage | 10–20 kg | — |
| Kühlwassersystem | 5–10 kg | — |
| Batterie (20 kWh LiFePO4) | — | 140–160 kg |
| Controller/Elektronik | — | 5–10 kg |
| Kabel (48V) | 2–5 kg | 5–15 kg |
| Landstrom-Ladegerät | — | 5–10 kg |
| **Gesamt** | **240–345 kg** | **180–240 kg** |

**Ergebnis**: Ein 10 kW Elektroantrieb mit 20 kWh Batterie ist
typischerweise 60–100 kg leichter als ein vergleichbarer Dieselantrieb
mit 100 L Tank. Allerdings sinkt dieser Vorteil mit steigender
Batteriekapazität.

### 10.2 Elektrische Installation

#### 10.2.1 Kabelführung und Anschluss

**Grundregeln:**
1. Kabel so kurz wie möglich (Batterie → Controller → Motor)
2. Plus- und Minusleitung zusammen führen (EMV-Reduktion)
3. Kabel gegen Scheuerung schützen (Wellrohr, Kabeldurchführungen)
4. Alle Verbindungen gecrimpt oder verschraubt (kein Löten bei Hochstrom!)
5. Marine-Kabel verwenden: verzinntes Kupfer, Gummi-/Silikonmantel
6. Biegeradius: min. 6 × Kabeldurchmesser
7. Kabelkennzeichnung: Plus (rot), Minus (schwarz/blau), Erdung (grün/gelb)
8. Durchführungen: IP67 Kabelverschraubungen (keine offenen Löcher)

#### 10.2.2 Sicherungskonzept

```
Batterie (+)
    │
    ├── ANL-Sicherung (z.B. 400 A bei 48V/10kW)
    │
    ├── Not-Trennschalter (zugänglich vom Steuerstand)
    │
    ├── Shunt (Strommessung für BMS/Monitor)
    │
    └── Controller (Frequenzumrichter)
            │
            └── E-Motor (3-Phasen)

Batterie (−)
    │
    └── direkt zum Controller (über Shunt)
```

**Sicherungsdimensionierung:**
```
I_sicherung = P_motor_max / (V_batterie_min × η_controller) × 1,25 (Sicherheitsfaktor)

Beispiel 10 kW / 48 V:
I_sicherung = 10.000 / (44,8 × 0,97) × 1,25 = 288 A → 300 A ANL-Sicherung
```

> ⚠️ **ZU PRÜFEN (Audit):** Für den identischen Fall 48 V / 10 kW nennt das Dokument drei unterschiedliche ANL-Sicherungswerte: **400 A** (Kap. 10.2.2, Sicherungs-Skizze oben), **300 A** (Formel hier: 288 A → 300 A) und **250 A** (Kap. 10.5.1, Tabelle). Bei ~208–230 A Dauerstrom und 70 mm² Kabel ist 400 A überdimensioniert (Kabelschutz gegen Überstrom/Brand nicht mehr sichergestellt). Wert vereinheitlichen — das Formelergebnis (≈ 300 A) ist plausibel; Richtung des korrekten Einzelwerts nicht zweifelsfrei, daher nicht automatisch korrigiert.

### 10.3 Mechanische Installation

#### 10.3.1 Motoreinbau

**Wellenantrieb (Bellmarine, Fischer Panda, Oceanvolt AXC):**
- SAE-Flansch-Montage auf bestehendem Motorfundament
- Alignment: gleiche Anforderungen wie Diesel (±0,05 mm)
- Vorteil: E-Motor ist kürzer → ggf. Fundamentanpassung nötig
- Motorlager: weichere Shore-Härte möglich (weniger Vibration)

**Saildrive-Ersatz (Oceanvolt ServoProp, Bellmarine EcoPower SD):**
- Bestehenden Saildrive-Ausschnitt nutzen
- Manschette und Dichtung erneuern
- Deutlich leichter als Diesel-Saildrive (~20 kg vs. ~80 kg)
- Alignment entfällt (integrierte Einheit)

**Pod-Antrieb (Torqeedo Cruise Pod):**
- Montage am Spiegel oder unter dem Rumpf
- Kein Stevenrohr, keine Wellenanlage nötig
- Steuern durch Drehen des Pods (360°)
- Ideal für Neubauten und Umrüstungen ohne Wellenanlage

#### 10.3.2 Batterie-Einbau

| Anforderung | Detail |
|------------|--------|
| Fundament | Steif, vibrationsfest, GFK-Wanne oder Stahlrahmen |
| Befestigung | Batterien MÜSSEN gegen Verrutschen gesichert sein (Spanngurte, Halterungen) |
| Belüftung | Mindestens 2 Öffnungen (oben und unten im Batteriefach) |
| Zugang | Für Wartung und Notfall-Abschaltung zugänglich |
| Temperatur | 10–35 °C ideal, nicht direkt an Motorraum-Schott |
| Feuchtigkeit | Kein stehendes Wasser, Entwässerung des Fachs |
| Isolation | Thermische Isolation wenn nahe Wärmequellen |
| Kabeleinführung | IP67 Durchführungen, Zugentlastung |

### 10.4 Inbetriebnahme-Checkliste

| # | Prüfpunkt | Methode | OK-Kriterium |
|---|----------|---------|-------------|
| 1 | Batteriespannung | Multimeter | ±2 % Nennwert |
| 2 | Zellbalance | BMS-Anzeige | Δ < 50 mV |
| 3 | Isolationswiderstand | Isolationsmessgerät (500 V DC) | > 1 MΩ (48V), > 10 MΩ (HV) |
| 4 | Kabelanschlüsse | Sichtprüfung + Drehmoment | Alle fest, kein Grünspan |
| 5 | Sicherungen | Sichtprüfung | Korrekte Werte, keine Korrosion |
| 6 | Not-Trennschalter | Funktionstest | Trennt sofort, zugänglich |
| 7 | Propeller | Drehen von Hand | Frei, kein Schleifen |
| 8 | Alignment (Welle) | Messuhr/Laser | ±0,05 mm |
| 9 | Controller-Parametrierung | Herstellersoftware | Motortyp, Batterie, Grenzen |
| 10 | Probelauf (trocken) | Motor ohne Last kurz laufen | Drehrichtung, Geräusche |
| 11 | Probelauf (Wasser) | Stegmanöver, vorwärts/rückwärts | Schub, Vibrationen |
| 12 | Notfalltest | Not-Aus betätigen | Sofortiger Stopp |
| 13 | BMS-Grenzwerttest | Simuliert (wenn möglich) | Abschaltung funktioniert |
| 14 | Dokumentation | Fotos, Protokoll | Vollständig, unterschrieben |

### 10.5 Typische Installationsfehler und Vermeidung

#### 10.5.1 Fehler: Falsche Kabelquerschnitte

Ein häufiger und gefährlicher Fehler ist die Unterdimensionierung
der DC-Hauptkabel. Anders als bei 230 V Landstrom fließen bei
48 V Systemen erhebliche Ströme:

| Leistung | Strom bei 48 V | Min. Querschnitt (3 % Verlust, 3 m) | Sicherung |
|---------|-------------|-------------------------------------|----------|
| 3 kW | 63 A | 16 mm² | 80 A |
| 5 kW | 104 A | 25 mm² | 125 A |
| 10 kW | 208 A | 70 mm² | 250 A |
| 15 kW | 313 A | 95 mm² | 400 A |
| 20 kW | 417 A | 150 mm² | 500 A |

**Folgen bei zu dünnem Kabel:**
- Spannungsabfall > 5 % → Leistungsverlust, Controller-Fehler
- Kabelerwärmung > 70 °C → Isolationsschmelze, Brandgefahr
- Im Extremfall: Kabelbrand bei Dauerlast

**Vermeidung:**
- IMMER nach ABYC E-11 / ISO 10133 dimensionieren
- Temperaturzuschlag bei Kabelbündeln (+15–25 %)
- Marine-Kabel verwenden (verzinntes Kupfer, höhere Temperaturklasse)
- Kabelquerschnitt im Zweifelsfall eine Stufe größer wählen

#### 10.5.2 Fehler: Unzureichende Batterie-Befestigung

Auf See wirken erhebliche Kräfte auf die Batterien:
- 30° Krängung (Segelboot): Seitenkraft = sin(30°) × Gewicht = 50 %
- Seeschlag (3 g Beschleunigung): 3× Batteriegewicht als Stoßbelastung
- 20 kWh LiFePO4 = ~140 kg → bis zu 420 kg Stoßkraft!

**Anforderungen an die Befestigung (nach ISO 10133, Anhang):**
| Ausrichtung | Beschleunigung | Sicherungskraft (20 kWh = 140 kg) |
|------------|---------------|----------------------------------|
| Vertikal (aufwärts) | 2 g | 2.744 N (280 kgf) |
| Horizontal (seitlich) | 3 g | 4.116 N (420 kgf) |
| Horizontal (längs) | 4 g | 5.488 N (560 kgf) |

**Empfohlene Befestigungsmethoden:**
1. Edelstahl-Gewindestangen durch GFK-Fundament (M10/M12)
2. Spanngurte (Zugfestigkeit > 2.000 daN) über Batterie
3. Alu-Rahmen mit Klemmleisten (verschraubt)
4. GFK-Wanne mit seitlichen Anschlägen und Deckel
5. NICHT: Holzbrettchen, Klettband, Kabelbinder!

#### 10.5.3 Fehler: Fehlende galvanische Trennung bei Landstrom

Das Anlegen an Landstrom ohne galvanische Trennung kann massive
Elektrolyse verursachen:

**Problem:** Das Bordnetz wird über den Schutzleiter (PE) des
Landstromkabels mit dem Marinastromnetz verbunden. Über das Wasser
fließen Ausgleichsströme zwischen benachbarten Booten und der
Landinstallation. Besonders E-Boote mit hoher Ladeleistung (5+ kW)
erzeugen größere Leckströme.

**Lösung:**
| Maßnahme | Schutzwirkung | Preis (EUR) |
|---------|-------------|------------|
| Galvanischer Isolator (Diodenblock) | Gut (unterbricht DC, lässt AC-Fehlstrom durch) | 80–200 |
| Trenntrafo (1:1) | Sehr gut (vollständige galvanische Trennung) | 500–2.000 |
| Isolationsüberwachungsrelais | Detektiert, schützt nicht | 200–400 |

**Empfehlung:** Trenntrafo bei allen E-Booten, die regelmäßig am
Landstrom laden. Galvanischer Isolator als Minimum.

#### 10.5.4 Fehler: Propeller nicht an E-Motor angepasst

Ein Dieselmotor dreht typischerweise 2.500–3.500 U/min am Propeller
(nach Getriebe). Ein E-Motor im Direktantrieb dreht 1.000–2.500 U/min.
Der alte Diesel-Propeller ist für die höhere Drehzahl ausgelegt und
passt NICHT zum E-Motor.

**Konsequenzen eines falschen Propellers:**
- Zu hohe Steigung → Motor überlastet bei niedriger Drehzahl
- Zu kleiner Durchmesser → Wirkungsgrad schlecht
- Festpropeller statt Faltpropeller → Widerstand unter Segeln

**Empfohlene Propeller für E-Antrieb:**
| Antriebsart | Propeller-Typ | Durchmesser | Steigung | Hersteller |
|------------|-------------|-----------|---------|-----------|
| Saildrive E-Motor | 3-Blatt Faltpropeller | 14"–17" | Variabel (selbsteinstellend) | Gori, Flexofold |
| Wellenantrieb E-Motor | 3-Blatt Festpropeller | 15"–20" | Niedrig (P/D 0,6–0,9) | Vetus, Sole |
| Pod-Antrieb | Integriert (Herstellerpropeller) | — | — | Torqeedo, ePropulsion |

**Faustregel:** Bei Umrüstung Diesel→Elektro mit Direktantrieb:
Propeller eine Nummer größer, Steigung ~30 % reduzieren.

#### 10.5.5 Fehler: Kein Isolationswächter bei Hochvolt-Systemen

Systeme über 60 V DC (z.B. Torqeedo Deep Blue mit 345 V) erfordern
gemäß ISO 16315 einen Isolationswächter (Insulation Monitoring Device,
IMD). Dieser überwacht den Isolationswiderstand zwischen den
spannungsführenden Leitern und dem Bootskörper/Erde.

**Anforderungen:**
- Messbereich: 0–10 MΩ
- Alarmgrenze: < 500 Ω/V (bei 345 V: < 172 kΩ)
- Reaktionszeit: < 5 s
- Anzeige: Deutlich sichtbar am Steuerstand
- Aktion bei Unterschreitung: Warnung (optisch/akustisch),
  ggf. automatische Abschaltung

**Empfohlene Isolationswächter:**
| Modell | Spannungsbereich | Preis (EUR) |
|--------|-----------------|------------|
| Bender ISOMETER iso685-D | Bis 690 V DC | 800–1.000 |
| Littelfuse SE-601 | Bis 500 V DC | 400–550 |
| Torqeedo IMD (Deep Blue) | 345 V DC (integriert) | Im System enthalten |

### 10.6 Systemdiagnose und Monitoring

#### 10.6.1 Regelmäßige Prüfungen

| Prüfung | Intervall | Werkzeug | OK-Kriterium |
|---------|----------|---------|-------------|
| SoC / SoH der Batterie | Monatlich | BMS-App | SoH > 80 % |
| Zellbalance | Monatlich | BMS-App | Δ < 50 mV |
| Isolationswiderstand | Jährlich | Isolationsmessgerät | > 1 MΩ (48V), > 10 MΩ (HV) |
| Kabelverbindungen | Jährlich | Sichtprüfung + Drehmoment | Keine Korrosion, fest |
| Propeller-Zustand | Halbjährlich | Taucher / Kran | Kein Bewuchs, keine Schäden |
| Zinkanoden | Halbjährlich | Sichtprüfung | > 50 % Substanz |
| Motor-Lager | Alle 5.000 h | Vibrationsmessung | Keine Geräusche, kein Spiel |
| Not-Aus-Funktion | Vor jeder Saison | Funktionstest | Trennt sofort |
| Sicherungen | Vor jeder Saison | Sichtprüfung | Keine Korrosion |
| BMS-Firmware | Vor jeder Saison | Hersteller-Website | Aktuellste Version |

#### 10.6.2 Monitoring-Systeme

| System | Hersteller | Funktionen | Preis (EUR) |
|--------|-----------|-----------|------------|
| Cerbo GX + VRM | Victron | Batterie, Solar, Ladung, Remote | 350 + kostenlos |
| CZone Digital Switching | Mastervolt | Bordnetz-Steuerung + Monitoring | 800–3.000 |
| Torqeedo TorqTrac | Torqeedo | Motor + Batterie, GPS, Reichweite | Im System |
| ePropulsion App | ePropulsion | Motor + Batterie, Bluetooth | Kostenlos |
| Oceanvolt Panel | Oceanvolt | Motordaten + Regeneration | Im System |
| SignalK (Open Source) | Community | Universell, NMEA 2000 Integration | 100–300 (Hardware) |

**Empfehlung:** Victron VRM-Portal ist der De-facto-Standard für
das Remote-Monitoring von Batterie- und Solarsystemen auf Yachten.
Daten werden alle 15 Minuten in die Cloud gesendet und sind von
überall abrufbar (auch für den Winterschlaf-Check der Batterie).

---
---

## 11. Normen und Vorschriften

### 11.1 Relevante Normen für elektrische Bootsantriebe

| Norm | Titel | Inhalt (Kurzfassung) |
|------|-------|---------------------|
| ISO 16315:2016 | Small craft — Electric propulsion system | Hauptnorm für E-Antrieb auf Booten |
| IEC 60092-507 | Electrical installations in ships — Small vessels | Elektrische Installationen auf Schiffen |
| ISO 10133:2012 | Small craft — Extra-low-voltage DC installations | 12/24 V DC Installationen |
| ISO 13297:2021 | Small craft — AC installations | 230 V AC Installationen |
| IEC 62619:2022 | Secondary lithium cells for industrial applications | Batterie-Sicherheit |
| IEC 62660-3:2022 | Secondary lithium-ion cells for EVs — Safety | Batterie-Sicherheitstests |
| UN 38.3 | Transport of dangerous goods — Lithium batteries | Transportvorschrift Lithium-Batterien |
| ABYC E-11 | AC and DC electrical systems on boats | US-Standard (oft referenziert) |
| ABYC E-2 | Cathodic protection | Korrosionsschutz |
| ABYC E-30 (ehem. TE-30) | Electric propulsion systems | US-Standard E-Antrieb |
| EN 50620 | Cables for EV charging systems | Ladekabel-Norm |
| ISO 12217 | Small craft — Stability | Stabilitätsberechnung (Batteriegewicht!) |

### 11.2 ISO 16315 im Detail

Die ISO 16315 ist die zentrale Norm für elektrische Bootsantriebe:

**Geltungsbereich:**
- Boote bis 24 m LH (Rumpflänge)
- Elektrische Antriebe ab 48 V DC / 50 V AC
- Batterien, Ladegeräte, Controller, Motoren, Kabel

**Wesentliche Anforderungen:**

| Bereich | Anforderung |
|---------|-----------|
| Isolation | Min. 500 Ω/V (bei 48 V: min. 24 kΩ) |
| Berührungsschutz | IP2X für alle spannungsführenden Teile > 48 V DC |
| Not-Aus | Roter Pilz-Taster am Steuerstand, trennt Antriebsbatterie |
| Fehlerstromschutz | RCD 30 mA für AC-Ladekreis |
| EMV | CE-konform, keine Störung von Navigation/Funk |
| Temperatur | Max. 90 °C Kabeloberfläche, max. 60 °C Gehäuse (berührbar) |
| Kurzschlussschutz | Max. Abschaltzeit 5 s (> 48 V DC) |
| Dokumentation | Systemschaltplan, Batterie-Datenblatt, Betriebsanleitung |
| Kennzeichnung | Warnschilder „Hochspannung" bei > 48 V DC |

### 11.3 Klassifizierungsgesellschaften und E-Antrieb

Für gewerbliche Schiffe und Superyachten sind Klassifizierungsregeln
relevant:

| Klassifikation | Regelwerk E-Antrieb | Anwendung |
|---------------|-------------------|-----------|
| DNV GL | Rules for Classification — Pt. 4 Ch. 8 Sec. 4 | Elektrische Antriebe auf klassifizierten Schiffen |
| Lloyd's Register | Rules for Naval Ships, Vol. 2, Part 5 | Marineschiffe und Superyachten |
| Bureau Veritas | NR 206 (Marine Electrical Systems) | Allgemein, Fähren |
| RINA | Rules for Classification of Yachts | Italienische Klassifikation |
| ABS | Guide for Hybrid Electric Power Systems | US-Fokus |

**DNV GL Batterie-Regeln (Zusammenfassung):**
- Batterieraum: Eigener Raum mit A-60-Brandschott (NMC) oder A-0 (LFP)
- Belüftung: Mechanisch, 6-facher Luftwechsel/h bei Laden
- Feuermelder: Rauchdetektor + Gasmelder im Batterieraum
- Löschanlage: Automatische CO₂- oder Aerosol-Löschanlage (NMC)
- BMS: Redundante Abschaltung (2 unabhängige Trenneinrichtungen)
- Dokumentation: Failure Mode Effect Analysis (FMEA) des Gesamtsystems
- Testlauf: 72 h Dauerlast-Test vor Inbetriebnahme

**Kosten Klassifizierung:**
| Bootsgröße | Erstklassifizierung | Jährliche Umfrage |
|-----------|-------------------|------------------|
| 18–24 m | 15.000–30.000 EUR | 3.000–5.000 EUR |
| 24–35 m | 25.000–50.000 EUR | 5.000–10.000 EUR |
| 35–50 m | 40.000–80.000 EUR | 8.000–15.000 EUR |
| 50 m+ | 60.000–150.000 EUR | 12.000–25.000 EUR |

### 11.4 Emissionszonen und Regulierung

| Region/Gewässer | Regulierung | Ab wann | Betroffene Boote |
|----------------|-----------|---------|-----------------|
| Amsterdam Grachten | Emissionsfrei | 2025 | Alle Motorboote |
| Bodensee | < 10 kW E-Motor ohne Zulassung | Bestehend | Alle |
| Berliner Gewässer | Tempo 6–12 km/h (de facto E-Antrieb) | Bestehend | Alle in Schutzgebieten |
| Norwegische Fjorde | Emissionsfrei (Geirangerfjord) | 2026 | Alle inkl. Kreuzfahrt |
| Balearen (Cala) | Ankerverbot mit Motorlärm | 2024 | Motoryachten |
| Schweizer Seen | E-Motor bis 6 kW erlaubt | Bestehend | Alle |
| Oberbayerische Seen | Nur E-Motor (z.B. Starnberger See) | Bestehend | Alle |
| EU (allgemein) | RCD 2013/53/EU (CE) | Bestehend | Neubauten/Import |

### 11.5 Vorschriften für Batterietransport

Der Transport von Lithium-Batterien unterliegt strengen Vorschriften:

| Transportweg | Regelwerk | Klasse | UN-Nummer | Verpackung |
|-------------|----------|--------|-----------|-----------|
| Straße (EU) | ADR 2023 | 9 | UN3480 (ohne Gerät) | P903 |
| Straße (EU) | ADR 2023 | 9 | UN3481 (mit Gerät) | P903/P906 |
| Seefracht | IMDG Code | 9 | UN3480/3481 | P903/LP903 |
| Luftfracht (Cargo) | IATA DGR | 9 | UN3480 | PI965/PI966 |
| Luftfracht (Passagier) | IATA DGR | 9 | UN3481 | Max. 160 Wh Einzelbatterie |

**Praxis bei Yacht-Batterien:**
- Einzelne Antriebsbatterien (> 1 kWh): Nur per Straße oder Seefracht
- Beschädigte/defekte Batterien: Sonder-Verpackung (UN-zugelassener
  Container), Brandschutzmatte, SoC < 30 %
- Spedition für Gefahrgut-Transport beauftragen (Kosten: 200–800 EUR
  je nach Entfernung und Gewicht)
- Hinweis: Yachten mit eingebauten Batterien unterliegen bei
  Yachttransporten (per Tieflader, Containerschiff) ebenfalls den
  Gefahrgutvorschriften → Transporteur informieren!

### 11.6 Versicherung und Zulassung

**Meldepflicht bei Umrüstung:**
1. Versicherung informieren (Antriebsänderung = wesentliche Änderung)
2. Sportboot-Führerschein: Leistungsgrenzen beachten (z.B. 15 PS/11 kW
   führerscheinfrei auf Binnenwasserstraßen in DE)
3. CE-Konformität: Bei Umrüstung ist der Umrüster für CE verantwortlich
4. Bodensee: Schifffahrtsamt muss E-Motor genehmigen (aber einfacher als Diesel)
5. Flaggenstaatliche Vorschriften beachten (Seeschifffahrt)

---
---

## 12. Kosten und TCO-Analyse

### 12.1 Total Cost of Ownership (TCO) — 10-Jahres-Vergleich

#### 12.1.1 Segelboot 10 m — Diesel vs. Elektrisch

| Kostenposition | Diesel (13 PS Yanmar) | Elektrisch (5 kW) |
|---------------|---------------------|-------------------|
| **Anschaffung** | | |
| Motor | 6.500 EUR | 5.500 EUR (Bellmarine DM5) |
| Batterie (10 kWh) | — | 8.000 EUR (Victron LiFePO4) |
| Tank (50 L) + Leitungen | 800 EUR | — |
| Abgasanlage | 600 EUR | — |
| Ladegerät + MPPT | — | 1.200 EUR |
| Solar (400 Wp) | — | 800 EUR |
| Installation | 2.500 EUR | 1.800 EUR |
| **Summe Anschaffung** | **10.400 EUR** | **17.300 EUR** |
| | | |
| **Jährliche Kosten** | | |
| Diesel (~150 L/Jahr) | 270 EUR | — |
| Strom (~500 kWh/Jahr) | — | 175 EUR |
| Ölwechsel | 80 EUR | — |
| Impellertausch (alle 2 J) | 40 EUR/Jahr | — |
| Zinkanode Motor | 30 EUR | — |
| Motorservice (alle 2 J) | 200 EUR/Jahr | — |
| BMS/Elektronik-Check | — | 50 EUR |
| Batterietausch (anteilig, nach 10 J) | — | 400 EUR/Jahr |
| **Summe jährlich** | **620 EUR** | **625 EUR** |
| | | |
| **10-Jahres-TCO** | **16.600 EUR** | **23.550 EUR** |
| **15-Jahres-TCO** | **19.700 EUR** | **26.675 EUR** |

**Fazit**: Rein ökonomisch ist der Dieselantrieb bei Segelbooten
noch günstiger. Der Elektroantrieb lohnt sich wirtschaftlich erst bei
hohen Motorlaufzeiten (> 300 h/Jahr) oder wenn die Batterie auch
als Bordstromspeicher genutzt wird (Einsparung separater Servicebatterie).

#### 12.1.2 Motoryacht 12 m — Diesel vs. Parallel-Hybrid

| Kostenposition | Diesel (40 PS) | Parallel-Hybrid |
|---------------|---------------|----------------|
| **Anschaffung** | | |
| Diesel-Motor | 18.000 EUR | 18.000 EUR |
| E-Motor + PTI | — | 15.000 EUR |
| Batterie (20 kWh) | — | 14.000 EUR |
| Controller/Elektronik | — | 3.000 EUR |
| Installation Diesel | 4.000 EUR | 4.000 EUR |
| Installation E-Antrieb | — | 5.000 EUR |
| **Summe Anschaffung** | **22.000 EUR** | **59.000 EUR** |
| | | |
| **Jährliche Kosten** | | |
| Diesel (~600 L/Jahr) | 1.080 EUR | 650 EUR (−40 % weniger Diesel) |
| Strom (Landstrom) | — | 250 EUR |
| Motorwartung | 500 EUR | 500 EUR |
| E-Antrieb-Wartung | — | 100 EUR |
| Batterie (anteilig) | — | 700 EUR |
| **Summe jährlich** | **1.580 EUR** | **2.200 EUR** |
| | | |
| **10-Jahres-TCO** | **37.800 EUR** | **81.000 EUR** |

**Fazit**: Ein Parallel-Hybrid ist bei Motoryachten primär ein
Komfort- und Umwelt-Feature, kein Sparmodell. Der wirtschaftliche
Vorteil ergibt sich nur bei:
- Emissionszonen-Pflicht (Amsterdam, Geirangerfjord)
- Sehr hohen Dieselpreisen (> 2,50 EUR/L)
- Hohem Liegegeld in ruhigen Buchten (Geräuschreduktion)
- Wiederverkaufswert-Steigerung (zunehmend relevant)

### 12.2 Förderprogramme (Stand 2026)

| Land | Programm | Förderung | Bedingung |
|------|---------|----------|----------|
| Deutschland | KfW-Umweltprogramm | Bis 30 % der Umrüstkosten | Emissionsfreier Antrieb |
| Niederlande | VAMIL/MIA | Steuerliche Abschreibung | Gewerbliche Nutzung |
| Norwegen | Enova | Bis 40 % der Mehrkosten | Hybrid/Elektro |
| Österreich | Umweltförderung | Bis 30 % (max. 20.000 EUR) | Boot < 24 m |
| Schweiz | Bodensee-Kantone | 2.000–5.000 CHF | E-Motor-Umrüstung |
| EU | Horizon Europe | Projektfinanzierung | Innovations-/Demoprojekte |

### 12.3 Detaillierte Betriebskostenanalyse

#### 12.3.1 Energiekosten im Detail

**Diesel-Betriebskosten (Motorisierung 10 kW / 27 PS):**
| Parameter | Wert |
|-----------|------|
| Spezifischer Verbrauch | 0,28–0,35 L/kWh (am Propeller) |
| Verbrauch bei 5 kn (1,2 kW) | 0,42 L/h |
| Verbrauch bei Rumpfgeschwindigkeit (5 kW) | 1,75 L/h |
| Dieselpreis (DE, 2026) | 1,75–1,90 EUR/L |
| Kosten pro Stunde (5 kn) | 0,74 EUR/h |
| Kosten pro Stunde (Rumpfgeschw.) | 3,06 EUR/h |
| Kosten pro Seemeile (5 kn) | 0,15 EUR/sm |
| Kosten pro Seemeile (Rumpfgeschw.) | 0,44 EUR/sm |

**Elektro-Betriebskosten (gleiche Leistung):**
| Parameter | Wert |
|-----------|------|
| Systemwirkungsgrad | 0,90 (Batterie→Propeller) |
| Verbrauch bei 5 kn (1,2 kW) | 1,33 kWh/h (an der Batterie) |
| Verbrauch bei Rumpfgeschw. (5 kW) | 5,56 kWh/h |
| Strompreis Marina (DE, 2026) | 0,35–0,45 EUR/kWh |
| Strompreis Solar (eigene Panels) | 0,00 EUR/kWh |
| Kosten pro Stunde (5 kn, Marina) | 0,47 EUR/h |
| Kosten pro Stunde (5 kn, Solar) | 0,00 EUR/h |
| Kosten pro Stunde (Rumpfgeschw., Marina) | 1,94 EUR/h |
| Kosten pro Seemeile (5 kn, Marina) | 0,09 EUR/sm |
| Kosten pro Seemeile (5 kn, Solar) | 0,00 EUR/sm |
| Kosten pro Seemeile (Rumpfgeschw., Marina) | 0,28 EUR/sm |

**Fazit:** Pro Seemeile ist der E-Antrieb am Landstrom ~40 % günstiger
als Diesel. Mit Solar sinken die Betriebskosten auf nahezu null.

#### 12.3.2 Wartungskosten im Detail

**Diesel-Wartung (typisch pro Jahr):**
| Wartung | Intervall | Kosten/Durchgang | Jährlich |
|---------|----------|-----------------|---------|
| Ölwechsel (3 L Öl + Filter) | 200 h oder jährlich | 45 EUR | 45 EUR |
| Kraftstofffilter | 200 h oder jährlich | 20 EUR | 20 EUR |
| Impellertausch | 400 h oder alle 2 Jahre | 35 EUR | 18 EUR |
| Zinkanode Motor (Saildrive) | Jährlich | 25 EUR | 25 EUR |
| Zinkanode Propellerwelle | Jährlich | 15 EUR | 15 EUR |
| Keilriemen | Alle 3 Jahre | 20 EUR | 7 EUR |
| Kühlwasser (Mischung) | Alle 2 Jahre | 30 EUR | 15 EUR |
| Motorservice (Werkstatt, alle 2 J) | 500 h oder 2 Jahre | 350 EUR | 175 EUR |
| Ventilspiel-Einstellung (alle 5 J) | 1.000 h oder 5 Jahre | 250 EUR | 50 EUR |
| **Summe Diesel-Wartung** | | | **370 EUR/Jahr** |

**Elektro-Wartung (typisch pro Jahr):**
| Wartung | Intervall | Kosten/Durchgang | Jährlich |
|---------|----------|-----------------|---------|
| Propeller-Antifouling | Jährlich | 30 EUR | 30 EUR |
| Zinkanode (Saildrive/Welle) | Jährlich | 25 EUR | 25 EUR |
| Wellendichtung (Inspektion) | Alle 2 Jahre | 20 EUR | 10 EUR |
| BMS-Firmware-Update | Jährlich | 0 EUR (kostenlos) | 0 EUR |
| Kabelverbindungen prüfen | Jährlich | 0 EUR (Eigenleistung) | 0 EUR |
| Isolationsmessung (HV-Systeme) | Jährlich | 50 EUR (Fachmann) | 50 EUR |
| **Summe Elektro-Wartung** | | | **115 EUR/Jahr** |

**Einsparung:** ~255 EUR/Jahr bei E-Antrieb = ~70 % weniger Wartungskosten.

#### 12.3.3 Batterie-Lebenszyklus-Kosten

Die Batterie ist der größte Kostenfaktor und muss über die Lebensdauer
amortisiert werden:

| Parameter | LiFePO4 (10 kWh) | NMC (10 kWh) |
|-----------|-----------------|-------------|
| Anschaffungspreis | 3.500 EUR | 2.800 EUR |
| Zyklenlebensdauer | 4.000 Zyklen | 1.500 Zyklen |
| Nutzbare Energie pro Zyklus | 8 kWh (80 % DoD) | 7 kWh (70 % DoD) |
| Gesamtenergie über Lebensdauer | 32.000 kWh | 10.500 kWh |
| Kosten pro kWh (Lifecycle) | 0,11 EUR/kWh | 0,27 EUR/kWh |
| Kalendarische Lebensdauer | 12–15 Jahre | 8–10 Jahre |
| Zyklen/Jahr (typ. Yacht) | 150–200 | 150–200 |
| Berechnete Lebensdauer | 20–27 Jahre | 7–10 Jahre |
| Begrenzender Faktor | Kalendarisch | Zyklisch + Kalendarisch |
| **Amortisationskosten/Jahr** | **~250–290 EUR** | **~280–350 EUR** |

**Fazit:** LiFePO4 ist langfristig ~30 % günstiger als NMC trotz
höherem Anschaffungspreis.

### 12.4 Wiederverkaufswert

| Antriebsart | Wertverlust/Jahr (Tendenz 2026) | Begründung |
|------------|-------------------------------|-----------|
| Diesel (konventionell) | 6–8 % | Standard, aber Emissionsregel-Risiko |
| Diesel (Euro Stage V) | 5–7 % | Zukunftssicherer |
| Rein-Elektrisch | 5–8 % | Batterie-Alterung als Risiko |
| Parallel-Hybrid | 4–6 % | Flexible Technologie, gefragt |
| Seriell-Hybrid | 4–6 % | Premium-Segment |

### 12.5 Versicherungskosten

| Versicherer | E-Antrieb-Aufschlag | Bedingungen | Bemerkung |
|-----------|-------------------|------------|----------|
| PANTAENIUS | 0–5 % | CE-konforme Installation | Progressiver Versicherer |
| Allianz Marine | 5–10 % | Fachgerechte Installation | Standard |
| HUK Yacht | 5–15 % | Zertifizierung erforderlich | Konservativ |
| Yacht-Pool | 0–8 % | LiFePO4 bevorzugt | Spezialversicherer |
| Lloyds Marine | Individuell | Umfangreiche Dokumentation | Superyachten |

**Einspar-Potenzial:**
- Einige Versicherer geben Rabatte für emissionsfreie Antriebe
- Reduziertes Brandrisiko (kein Diesel, kein Abgas) → niedrigere Prämie
- Geringere Umwelthaftung (kein Dieselaustritt bei Leck)

### 12.6 Strompreise in europäischen Marinas (2026)

| Region | Preis/kWh (EUR) | Abrechnung | Bemerkung |
|--------|----------------|-----------|----------|
| Deutschland (Nord) | 0,35–0,50 | Prepaid-Karte / Münze | Teils Pauschal/Tag |
| Deutschland (Süd) | 0,30–0,45 | Prepaid-Karte | Bodensee günstiger |
| Niederlande | 0,30–0,40 | Stegmeister/App | Grachten oft Pauschale |
| Frankreich | 0,25–0,35 | Stegmeister | Günstiger als DE |
| Italien | 0,25–0,40 | Stegmeister / Coin | Starkes Nord-Süd-Gefälle |
| Spanien | 0,20–0,35 | Stegmeister | Südeuropa günstiger |
| Griechenland | 0,20–0,30 | Stegmeister | Am günstigsten |
| Kroatien | 0,22–0,35 | ACI-Marina-Karte | Standardisiert |
| Schweden | 0,25–0,35 | App / Prepaid | Hoher Ökostrom-Anteil |
| Norwegen | 0,15–0,25 | App / Prepaid | Wasserkraft = günstig |
| UK | 0,35–0,55 GBP | Prepaid/Meter | Nach Brexit teurer |
| Türkei | 0,10–0,20 | Stegmeister | Sehr günstig |
| Karibik | 0,30–0,60 USD | Generator oder Steg | Sehr variabel |

**Tipp:** In norwegischen und schwedischen Marinas ist der Strom
am günstigsten und stammt zu > 90 % aus erneuerbaren Quellen
(Wasserkraft). Ideal für E-Boot-Tourismus.

---
---

## 13. Umrüstung Diesel auf Elektro

### 13.1 Umrüst-Eignung nach Bootstyp

| Bootstyp | Eignung | Aufwand | Bemerkung |
|---------|---------|---------|----------|
| Segelboot mit Saildrive | ★★★★★ | Gering | Oceanvolt ServoProp = Plug-and-Play |
| Segelboot mit Wellenantrieb | ★★★★☆ | Mittel | Bellmarine/AXC an bestehende Welle |
| Motoryacht (Verdränger) | ★★★☆☆ | Mittel–Hoch | Batterie-Platz und -Gewicht kritisch |
| Motoryacht (Gleiter) | ★☆☆☆☆ | Sehr hoch | Unrealistisch (Energiebedarf zu hoch) |
| Katamaran | ★★★★★ | Mittel | Platz für Batterien + Solar |
| Daycruiser | ★★★★☆ | Gering | Kurze Strecken, reicht oft |
| Grachtenboot | ★★★★★ | Gering | Perfektes E-Boot-Revier |

### 13.2 Umrüst-Prozess Schritt für Schritt

#### Phase 1: Planung (2–4 Wochen)
1. Bootvermessung (Motorraum, Batteriefach, Kabelwege)
2. Energiebedarfsberechnung (siehe Kapitel 7)
3. Komponentenwahl (Motor, Batterie, Controller, Ladung)
4. Gewichts- und Trimmberechnung
5. Kostenkalkulation und Angebot

#### Phase 2: Demontage (1–3 Tage)
1. Diesel ablassen (Kraftstoff und Öl fachgerecht entsorgen!)
2. Abgasanlage demontieren
3. Kühlwasserleitungen entfernen
4. Motor lösen (Motorlager, Flanschkupplung)
5. Motor ausheben (Kran, typisch 150–300 kg)
6. Kraftstofftank ausbauen
7. Motorraum reinigen

#### Phase 3: Einbau Elektro (3–7 Tage)
1. Motorfundament anpassen (wenn nötig)
2. E-Motor einsetzen und ausrichten
3. Batterie-Fundament einbauen
4. Batterien montieren und sichern
5. Controller montieren
6. Verkabelung (DC-Hauptkabel, Steuerleitungen, BMS)
7. Ladegerät installieren
8. DC/DC-Wandler für Bordnetz
9. Not-Trennschalter und Sicherungen
10. MPPT + Solar (wenn gewünscht)

#### Phase 4: Inbetriebnahme (1–2 Tage)
1. Elektrische Prüfungen (siehe Kapitel 10.4)
2. Probelauf (Steg, langsame Fahrt)
3. Belastungstest (Vollgas, Manöver)
4. Einweisung des Eigners
5. Dokumentation und Übergabe

### 13.3 Typische Umrüstkosten

| Bootstyp | Leistung | Batterie | Material | Arbeit | Gesamt (EUR) |
|---------|---------|---------|---------|--------|-------------|
| Segelboot 8 m (SD→ServoProp) | 5 kW | 10 kWh | 14.000 | 3.000 | 17.000 |
| Segelboot 10 m (Welle→AXC) | 10 kW | 15 kWh | 20.000 | 4.000 | 24.000 |
| Segelboot 12 m (SD→ServoProp) | 10 kW | 20 kWh | 24.000 | 4.500 | 28.500 |
| Katamaran 12 m (2×Welle) | 2×6 kW | 30 kWh | 32.000 | 6.000 | 38.000 |
| Motoryacht 10 m (Verdränger) | 10 kW | 30 kWh | 28.000 | 5.000 | 33.000 |
| Grachtenboot 8 m | 5 kW | 10 kWh | 12.000 | 2.500 | 14.500 |

### 13.4 Häufige Umrüst-Fehler

| Fehler | Konsequenz | Vermeidung |
|--------|-----------|-----------|
| Batterie zu klein dimensioniert | Reichweitenangst, Tiefentladung | Korrekte Berechnung + 20 % Reserve |
| Kabel zu dünn | Spannungsabfall, Überhitzung, Brand | Dimensionierung nach Kapitel 2.6 |
| Batterie nicht fixiert | Verrutschen bei Seegang → Kurzschluss | Sturmsichere Befestigung (30° Krängung) |
| Keine Belüftung Batteriefach | Gasansammlung, Überhitzung | 2 Öffnungen, oben und unten |
| Kein Not-Trennschalter | Keine Notabschaltung möglich | Pflicht gem. ISO 16315 |
| Falscher Propeller | Wirkungsgrad schlecht | E-Motor-Drehzahl ≠ Diesel → Propeller anpassen |
| BMS nicht konfiguriert | Tiefentladung, Überladung | Fachmann parametriert BMS |
| Versicherung nicht informiert | Kein Versicherungsschutz | VOR Umrüstung melden |
| Kein Erdungssystem | Galvanische Korrosion | Potenzialausgleich nach ABYC |
| Schwerpunkt verändert | Trimprobleme, Stabilitätsverlust | Trimmberechnung vor Einbau |

---
---

## 14. Fehlerbild-Atlas

### Fehlerbild 1: Motor dreht nicht (kein Anlauf)

**Symptom**: Gashebel vorwärts, keine Reaktion des Motors.

**Mögliche Ursachen:**
| # | Ursache | Wahrscheinlichkeit | Prüfung |
|---|--------|-------------------|---------|
| 1 | Not-Aus-Schalter ausgelöst | Hoch | Stellung prüfen |
| 2 | BMS hat Batterie getrennt | Hoch | BMS-Status prüfen (LED/App) |
| 3 | Hauptsicherung (ANL/MEGA) durchgebrannt | Mittel | Sicherung prüfen |
| 4 | Controller-Fehler (Error-Code) | Mittel | Display/Diagnose-LED |
| 5 | Kabelbruch/lose Verbindung | Mittel | Spannung am Controller messen |
| 6 | Kill-Switch (Lanyard) | Gering | Position prüfen |
| 7 | Controller defekt | Gering | Tauschreparatur |
| 8 | Motor blockiert (Propeller) | Gering | Propeller von Hand drehen |

**AYDI-Bewertung**: Score 0 (Antrieb nicht verfügbar), Confidence: measured/visual_high.

### Fehlerbild 2: Motor läuft, aber kein/wenig Schub

**Symptom**: Motor dreht, Boot bewegt sich kaum.

**Mögliche Ursachen:**
| # | Ursache | Wahrscheinlichkeit | Prüfung |
|---|--------|-------------------|---------|
| 1 | Propeller bewachsen (Muscheln, Algen) | Hoch | Taucher/Spiegel |
| 2 | Leine im Propeller | Hoch | Motor aus, inspizieren |
| 3 | Faltpropeller öffnet nicht | Mittel | Unter Wasser prüfen |
| 4 | Falsche Drehrichtung | Gering | Vorwärts/Rückwärts vertauscht |
| 5 | Controller-Leistungsbegrenzung (Überhitzung) | Mittel | Temperatur prüfen |
| 6 | Getriebe defekt (Schlupf) | Gering | Drehzahl Motor vs. Propeller |

**AYDI-Bewertung**: Score 20–40, abhängig von Ursache.

### Fehlerbild 3: Batterie entlädt sich schneller als erwartet

**Symptom**: Reichweite deutlich unter Berechnung.

**Mögliche Ursachen:**
| # | Ursache | Wahrscheinlichkeit | Prüfung |
|---|--------|-------------------|---------|
| 1 | Bewuchs am Rumpf | Hoch | Rumpfzustand prüfen |
| 2 | Gegen Wind/Strom gefahren | Hoch | GPS-Geschwindigkeit vs. Fahrt durch Wasser |
| 3 | Batterie gealtert (SoH < 80 %) | Mittel | BMS: SoH-Wert prüfen |
| 4 | SoC-Anzeige falsch kalibriert | Mittel | Volle Ladung + Kalibrierfahrt |
| 5 | Parasitärer Verbrauch (Leck) | Gering | Ruhestromverbrauch messen (< 50 mA) |
| 6 | Zelldisbalance | Mittel | BMS: Zellspannungen vergleichen |
| 7 | Zu hohe Geschwindigkeit | Häufig | Leistung vs. Geschwindigkeit prüfen |

**AYDI-Bewertung**: Score 40–70, Confidence: calculated/documented.

### Fehlerbild 4: BMS löst häufig aus (Batterie-Abschaltung)

**Symptom**: Batterie trennt sich während der Fahrt, Motor stoppt.

**Mögliche Ursachen:**
| # | Ursache | Wahrscheinlichkeit | Prüfung |
|---|--------|-------------------|---------|
| 1 | Unterspannung (Batterie leer) | Hoch | SoC und Zellspannungen |
| 2 | Überstrom (Motor zieht zu viel) | Mittel | Stromaufnahme bei Vollgas |
| 3 | Zelldisbalance (eine Zelle schwach) | Mittel | Zellspannungen vergleichen |
| 4 | Übertemperatur | Mittel | BMS-Temperatursensoren |
| 5 | BMS-Kabel lose/korrodiert | Gering | Sensorleitungen prüfen |
| 6 | BMS-Firmware-Bug | Gering | Firmware-Update |
| 7 | Defekte Zelle (intern) | Gering | Einzelzellen-Kapazitätstest |

**AYDI-Bewertung**: Score 20–50 (sicherheitsrelevant), Confidence: measured.

### Fehlerbild 5: Ungewöhnliche Geräusche vom E-Motor

**Symptom**: Pfeifen, Summen, Rattern oder Schleifen im E-Motor.

**Mögliche Ursachen:**
| # | Ursache | Wahrscheinlichkeit | Prüfung |
|---|--------|-------------------|---------|
| 1 | Lagerverschleiß (Kugellager) | Mittel | Motor entkoppeln, von Hand drehen |
| 2 | PWM-Frequenz hörbar (Controller) | Häufig | Normal bei manchen Drehzahlen |
| 3 | Fremdkörper im Propeller | Mittel | Propeller inspizieren |
| 4 | Alignment-Fehler (Welle) | Gering | Alignment prüfen |
| 5 | Magnetische Geräusche (Magnetostriktion) | Gering | Lastabhängig, normal |
| 6 | Getriebe-Verschleiß | Gering | Getriebespiel prüfen |

**AYDI-Bewertung**: Score 50–80 je nach Ursache.

### Fehlerbild 6: Ladegerät lädt nicht / langsam

**Symptom**: Batterie wird am Landstrom nicht (voll) geladen.

**Mögliche Ursachen:**
| # | Ursache | Wahrscheinlichkeit | Prüfung |
|---|--------|-------------------|---------|
| 1 | Landstrom nicht eingesteckt/eingeschaltet | Hoch | Sicherung Marina prüfen |
| 2 | Ladegerät auf falsche Batterie-Chemie eingestellt | Mittel | Einstellung prüfen (LiFePO4!) |
| 3 | BMS sperrt Laden (Temperatur < 0 °C) | Mittel | Batterietemperatur |
| 4 | BMS sperrt Laden (Zelle voll: > 3,65 V) | Normal | Balancing-Phase |
| 5 | Ladegerät defekt | Gering | Ausgangsspannung messen |
| 6 | Kabel korrodiert (Kontaktwiderstand) | Gering | Spannungsabfall messen |
| 7 | CEE-Stecker feucht/korrodiert | Mittel | Stecker inspizieren |

**AYDI-Bewertung**: Score 50–80.

### Fehlerbild 7: Überhitzung des Controllers

**Symptom**: Controller geht in Leistungsreduktion (Derating) oder schaltet ab.

**Mögliche Ursachen:**
| # | Ursache | Wahrscheinlichkeit | Prüfung |
|---|--------|-------------------|---------|
| 1 | Kühlwasserpumpe defekt/blockiert | Mittel | Wasserfluss prüfen |
| 2 | Umgebungstemperatur zu hoch (Motorraum) | Häufig | Motorraum-Belüftung |
| 3 | Dauerlast über Nennleistung | Mittel | Geschwindigkeit reduzieren |
| 4 | Kühlkörper verschmutzt (Luft) | Mittel | Reinigen |
| 5 | Kabelquerschnitt zu gering | Gering | Kabel prüfen (warm?) |

**AYDI-Bewertung**: Score 40–60.

### Fehlerbild 8: Galvanische Korrosion (Elektrolyse)

**Symptom**: Schnelle Korrosion an Metallteilen unter Wasser nach E-Antrieb-Einbau.

**Mögliche Ursachen:**
| # | Ursache | Wahrscheinlichkeit | Prüfung |
|---|--------|-------------------|---------|
| 1 | Fehlender Potenzialausgleich | Hoch | Erdungsleitungen prüfen |
| 2 | Leckstrom durch Motor ins Wasser | Mittel | Isolationsmessung Motor |
| 3 | Fehlende/verbrauchte Zinkanoden | Mittel | Anoden inspizieren |
| 4 | Landstrom-Fehlstrom (Marina) | Häufig | Trenntrafo einsetzen |
| 5 | Ungleichartige Metalle in Kontakt | Mittel | Material-Check |

**AYDI-Bewertung**: Score 20–40 (strukturkritisch!).

### Fehlerbild 9: Hydro-Regeneration funktioniert nicht

**Symptom**: Unter Segeln wird keine Energie regeneriert.

**Mögliche Ursachen:**
| # | Ursache | Wahrscheinlichkeit | Prüfung |
|---|--------|-------------------|---------|
| 1 | Regeneration im Controller nicht aktiviert | Häufig | Einstellung prüfen |
| 2 | Propeller arretiert (Faltpropeller geschlossen) | Häufig | Propeller muss frei drehen |
| 3 | Geschwindigkeit zu gering (< 4 kn) | Mittel | Erst ab 4–5 kn sinnvoll |
| 4 | BMS sperrt Laden (Batterie voll) | Normal | SoC prüfen |
| 5 | Kabelverbindung Motor → Controller unterbrochen | Gering | Verkabelung prüfen |

**AYDI-Bewertung**: Score 60–80 (Komfortproblem, nicht sicherheitsrelevant).

### Fehlerbild 10: Zellbalancing-Problem

**Symptom**: Eine oder mehrere Zellen weichen stark von den anderen ab.

**Mögliche Ursachen:**
| # | Ursache | Wahrscheinlichkeit | Prüfung |
|---|--------|-------------------|---------|
| 1 | Defekte Zelle (intern) | Mittel | Einzelzellen-Kapazitätstest |
| 2 | BMS-Balancing defekt | Gering | BMS-Diagnose |
| 3 | Temperaturgradient im Batteriefach | Mittel | Temperatur aller Zellen |
| 4 | Ungleiche Alterung (partieller Ersatz) | Mittel | Zellen gleichen Alters? |
| 5 | Sensorleitung lose/korrodiert | Gering | Kabel prüfen |

**AYDI-Bewertung**: Score 30–60.

### Fehlerbild 11: Erdschluss / Isolationsfehler (Hochvolt)

**Symptom**: Isolationswächter meldet Fehler, System schaltet ab.

**Mögliche Ursachen:**
| # | Ursache | Wahrscheinlichkeit | Prüfung |
|---|--------|-------------------|---------|
| 1 | Feuchtigkeit in Kabelverbindung | Hoch | Stecker inspizieren, trocknen |
| 2 | Kabelisolierung beschädigt (Scheuerung) | Mittel | Kabel visuell prüfen |
| 3 | Salzwasser im Batteriefach | Mittel | Batteriefach inspizieren |
| 4 | Motor-Isolierung geschwächt (Feuchtigkeit) | Gering | Isolationsmessung Motor |
| 5 | Controller-Kondensator defekt | Gering | Fachwerkstatt |

**AYDI-Bewertung**: Score 10–30 (sicherheitskritisch!).

### Fehlerbild 12: Elektromagnetische Störungen (EMV)

**Symptom**: Störungen an Funkgeräten, Plotter, AIS oder Autopilot
bei laufendem E-Motor.

**Mögliche Ursachen:**
| # | Ursache | Wahrscheinlichkeit | Prüfung |
|---|--------|-------------------|---------|
| 1 | Controller-PWM strahlt | Mittel | Abstand Controller ↔ Antenne |
| 2 | Ungeschirmte DC-Kabel | Häufig | Plus + Minus parallel führen |
| 3 | Fehlender EMV-Filter | Mittel | Filter nachrüsten |
| 4 | Erdungsproblem | Mittel | Potenzialausgleich prüfen |
| 5 | Billig-Controller (kein CE) | Gering | CE-konformen Controller verwenden |

**AYDI-Bewertung**: Score 40–70 (Navigations-Sicherheit!).

---
---

## 15. Troubleshooting

### Troubleshooting 1: Systematische Fehlersuche „Motor startet nicht"

```
START: Motor reagiert nicht auf Gashebel
  │
  ├── Not-Aus-Schalter in Stellung „EIN"?
  │     ├── NEIN → Not-Aus einschalten → LÖSUNG
  │     └── JA ↓
  │
  ├── BMS-Status: Batterie aktiv? (LED grün / App-Status)
  │     ├── NEIN → BMS-Reset (Aus/Ein), Zellspannungen prüfen
  │     │          Batterie leer? → Laden
  │     │          BMS-Fehler? → Fehlercode lesen
  │     └── JA ↓
  │
  ├── Spannung am Controller-Eingang messen
  │     ├── 0 V → Hauptsicherung prüfen, Kabel prüfen
  │     ├── < 44 V (48V-System) → Batterie zu leer, BMS sollte trennen
  │     └── > 44 V ↓
  │
  ├── Controller-Display/LED: Fehlercode?
  │     ├── JA → Fehlercode im Handbuch nachschlagen
  │     │         Typisch: Übertemperatur, Überstrom, Motor-Fehler
  │     └── NEIN (kein Display, keine LED) → Controller defekt? Stromversorgung?
  │
  ├── Gashebel-Signal prüfen (0–5V analog oder CAN-Bus)
  │     ├── Kein Signal → Gashebel-Kabel, Potentiometer, CAN-Verbindung
  │     └── Signal vorhanden ↓
  │
  ├── Motor-Phasen prüfen (3 Kabel zum Motor)
  │     ├── Widerstand: sollte 0,1–2 Ω zwischen je 2 Phasen sein
  │     ├── Unendlich → Kabelbruch oder Motor-Wicklung defekt
  │     └── Normal → Controller defekt (Endstufe)
  │
  └── ERGEBNIS: Controller-Tausch oder Fachwerkstatt
```

### Troubleshooting 2: „Batterie lädt nicht vollständig"

```
START: Batterie erreicht nicht 100 % SoC
  │
  ├── Ladegerät aktiv? (LED, Display)
  │     ├── NEIN → Landstrom prüfen, Sicherung, CEE-Stecker
  │     └── JA ↓
  │
  ├── Ladestrom > 0 A?
  │     ├── NEIN → BMS sperrt Laden
  │     │         Temperatur < 0 °C? → Heizung, warten
  │     │         Zelle > 3,65 V? → Balancing-Phase (normal, dauert!)
  │     │         BMS-Fehler? → Reset, Fehlercode
  │     └── JA ↓
  │
  ├── Ladestrom sinkt auf nahe 0 A, aber SoC < 95 %?
  │     ├── JA → Zelldisbalance: eine Zelle ist voll, andere nicht
  │     │         Lösung: BMS balancieren lassen (kann 12–48 h dauern!)
  │     │         Wenn Balance > 100 mV: defekte Zelle wahrscheinlich
  │     └── NEIN ↓
  │
  ├── Ladestrom normal, aber SoC-Anzeige „hängt"?
  │     ├── JA → SoC-Kalibrierung: Batterie einmal komplett laden (3,65 V/Zelle)
  │     │         und dann entladen (bis BMS trennt), dann wieder voll laden.
  │     └── NEIN → Kapazitätsverlust (SoH < 80 %): Batterie-Test durchführen
  │
  └── ERGEBNIS: Batterie-Health-Check oder Zelltausch
```

### Troubleshooting 3: „Reichweite deutlich unter Erwartung"

```
START: Tatsächliche Reichweite < 70 % der berechneten
  │
  ├── Geschwindigkeit korrekt? (GPS vs. Berechnung)
  │     ├── Schneller als geplant → P steigt mit v³!
  │     │     10 % schneller = 37 % weniger Reichweite
  │     └── Korrekt ↓
  │
  ├── Rumpfzustand prüfen (Bewuchs?)
  │     ├── Bewuchs vorhanden → Rumpf reinigen (−10 bis −30 % Widerstand)
  │     └── Sauber ↓
  │
  ├── Wind/Strömung?
  │     ├── Gegenwind > 15 kn → Normaler Mehrverbrauch (−15 bis −30 %)
  │     ├── Gegenstrom > 0,5 kn → Normaler Mehrverbrauch
  │     └── Ruhig ↓
  │
  ├── Batterie SoH prüfen (BMS)
  │     ├── SoH < 80 % → Batterie ersetzen oder Kapazität akzeptieren
  │     └── SoH > 80 % ↓
  │
  ├── Bordverbrauch messen (alle Verbraucher aus, nur Antrieb)
  │     ├── Leistung passt → Bordverbraucher optimieren
  │     └── Leistung zu hoch ↓
  │
  ├── Propeller-Zustand und -Typ prüfen
  │     ├── Falsche Steigung/Durchmesser → Propeller anpassen
  │     ├── Beschädigt → Propeller reparieren/ersetzen
  │     └── OK → Rumpfform/Beladung/Trim prüfen
  │
  └── ERGEBNIS: Ursache identifiziert, Maßnahme einleiten
```

### Troubleshooting 4: „Galvanische Korrosion nach E-Umrüstung"

```
START: Korrosion an Metallteilen unter Wasser verstärkt nach E-Umrüstung
  │
  ├── Isolationsmessung Motor → Rumpf durchführen
  │     ├── < 1 MΩ → Leckstrom! Motor oder Kabel defekt/feucht
  │     │         Reparatur erforderlich (Motorwicklung, Kabel ersetzen)
  │     └── > 1 MΩ ↓
  │
  ├── Potenzialausgleich vorhanden?
  │     ├── NEIN → Potenzialausgleichsschiene installieren
  │     │         Alle Metallteile (Motor, Welle, Stevenrohr, Durchbrüche)
  │     │         mit 6–16 mm² Kupferkabel verbinden
  │     └── JA ↓
  │
  ├── Zinkanoden vorhanden und intakt?
  │     ├── NEIN / verbraucht → Neue Zinkanoden montieren
  │     └── JA ↓
  │
  ├── Landstrom-Fehlstrom?
  │     ├── Stecker ziehen: Korrosion stoppt → Trenntrafo einbauen!
  │     └── Korrosion auch ohne Landstrom ↓
  │
  ├── Galvanisches Element identifizieren
  │     ├── Unterschiedliche Metalle in Kontakt → Isolieren oder angleichen
  │     └── Kein offensichtlicher Kontakt → Fachwerkstatt (Unterwassermessung)
  │
  └── ERGEBNIS: Potenzialausgleich, Trenntrafo, Zinkanoden, Motorprüfung
```

### Troubleshooting 5: „EMV-Störungen bei laufendem E-Motor"

```
START: Funkstörungen / Plotterstörungen bei E-Motor-Betrieb
  │
  ├── Welche Geräte gestört? (VHF, AIS, Plotter, Autopilot)
  │     ├── VHF → EMV-Strahlung in VHF-Band (156 MHz)
  │     ├── AIS → EMV-Strahlung
  │     ├── Plotter → Leitungsgebundene Störung
  │     └── Autopilot → Magnetfeld-Störung durch Motormagnete
  │
  ├── Antennenkabel und -anschlüsse prüfen
  │     ├── Defekt/korrodiert → Reparieren (oft die eigentliche Ursache)
  │     └── OK ↓
  │
  ├── Abstand Controller/DC-Kabel → Antenne messen
  │     ├── < 1 m → Kabel/Controller verlegen (min. 1–2 m Abstand)
  │     └── > 1 m ↓
  │
  ├── DC-Kabel parallel geführt (Plus + Minus)?
  │     ├── NEIN → Kabel zusammenführen (Verdrillen wenn möglich)
  │     └── JA ↓
  │
  ├── EMV-Filter am Controller-Eingang?
  │     ├── NEIN → EMV-Filterdrossel nachrüsten (~50–200 EUR)
  │     └── JA ↓
  │
  ├── Potenzialausgleich korrekt? (alle Geräte-Masse verbunden)
  │     ├── NEIN → Potenzialausgleichsschiene
  │     └── JA → Controller-Hersteller kontaktieren (Firmware/Schaltfrequenz)
  │
  └── ERGEBNIS: Abstand, Kabelführung, Filter, Erdung
```

---
---

## 16. FAQ — Häufige Fragen

### FAQ 1: Wie lange hält eine LiFePO4-Antriebsbatterie?

**Antwort:** LiFePO4-Batterien halten typisch 3.000–5.000 Vollzyklen
(80 % DoD). Bei typischem Yacht-Einsatz (100–200 Zyklen/Jahr) sind
das 15–25+ Jahre. Der begrenzende Faktor ist oft die kalendarische
Alterung (~15 Jahre bei guter Pflege) und nicht die Zyklenlebensdauer.
Praktisch erreichen die meisten Marinebatterien 10–15 Jahre.

### FAQ 2: Kann ich meine Blei-Batterien einfach durch LiFePO4 ersetzen?

**Antwort:** Nicht direkt als „Drop-In-Replacement". LiFePO4 hat eine
andere Ladekennlinie (CC/CV bei 3,65 V/Zelle statt 2,40 V/Zelle).
Der Laderegler muss auf LiFePO4-Profil umgestellt werden. Außerdem
ist ein BMS zwingend erforderlich. Viele LiFePO4-Batterien haben ein
integriertes BMS (z.B. Victron Smart, Mastervolt MLI), das den Tausch
vereinfacht. Die Ladegeräte müssen trotzdem kompatibel sein.

### FAQ 3: Ist ein Elektroantrieb wirklich wartungsfrei?

**Antwort:** Fast, aber nicht ganz. Kein Ölwechsel, kein Impeller,
keine Zinkanoden am Motor. Aber: Propeller-Antifouling, Wellendichtung
(bei Wellenantrieb), Korrosionsschutz, BMS-Firmware-Updates,
Batterie-SoH-Check alle 2 Jahre. Aufwand: ~2 h/Jahr vs. ~8 h/Jahr
beim Diesel.

### FAQ 4: Wie sicher sind Lithium-Batterien auf Booten?

**Antwort:** LiFePO4 ist die sicherste Lithium-Chemie und für den
Marineeinsatz empfohlen. Die thermische Stabilität ist deutlich höher
als bei NMC oder NCA. Dennoch: Ein gutes BMS, korrekte Verkabelung,
Sicherungen und Belüftung sind unerlässlich. Die meisten
Batterie-Brände auf Booten entstehen durch unsachgemäße Installation,
nicht durch die Batterie selbst.

### FAQ 5: Kann ich mit einem Elektroboot den Atlantik überqueren?

**Antwort:** Rein elektrisch unter Motor: nein (viel zu wenig Energie).
Aber: Ein elektrisch angetriebenes Segelboot mit Hydro-Regeneration
kann den Atlantik problemlos überqueren. Die Regeneration unter Segeln
deckt den Bordverbrauch und hält die Batterie für Hafenmanöver geladen.
Mehrere Segler haben dies mit Oceanvolt-Systemen erfolgreich gemacht.

### FAQ 6: Was passiert, wenn die Batterie auf See leer ist?

**Antwort:** Das Boot schwimmt weiter — es ist ja kein Leck. Bei
Segelbooten: Segel setzen. Bei Motoryachten: Notsituation, Hilfe
rufen (VHF Kanal 16). Deshalb ist die Reichweiten-Reserveplanung
so wichtig (siehe Kapitel 7.5). Bei Hybrid-Systemen springt der
Diesel automatisch an. Einige Systeme (Torqeedo) warnen rechtzeitig
per App/Display.

### FAQ 7: Wie laut ist ein Elektroantrieb wirklich?

**Antwort:** Messungen an typischen Installationen:
| Situation | Diesel (dB(A) am Steuerstand) | Elektro (dB(A)) | Differenz |
|----------|------------------------------|-----------------|----------|
| Leerlauf | 55–65 | 25–35 | −30 dB |
| 3 Knoten | 60–70 | 30–40 | −30 dB |
| 5 Knoten | 65–75 | 35–45 | −30 dB |
| 7 Knoten (Rumpf) | 72–85 | 40–55 | −30 dB |

30 dB weniger bedeutet: Der E-Motor ist ~1.000× leiser (dB ist
logarithmisch). In der Praxis hört man bei einem E-Boot vor allem
das Wasserrauschen am Rumpf.

### FAQ 8: Kann ich Solar alleine als Energiequelle für den Antrieb nutzen?

**Antwort:** Für den Dauerbetrieb: nur bei langsamer Fahrt und großer
Solardachfläche (Katamaran). Beispiel: 3 kWp Solar auf Katamaran-Dach
liefert ~1,5 kW Durchschnittsleistung → ausreichend für 3–4 Knoten
Dauerfahrt. Für schnellere Fahrt oder kürzere Strecken: Solar lädt
die Batterie, die den Motor versorgt. Auf einem typischen Segelboot
(400–600 Wp) reicht Solar nur für den Bordverbrauch, nicht den Antrieb.

### FAQ 9: Welchen Propeller brauche ich für einen E-Motor?

**Antwort:** E-Motoren drehen typischerweise langsamer als Dieselmotoren
(oder über Getriebe). Für Direktantrieb: großer Propeller, geringe
Steigung (Segelboot: 3-Blatt Festpropeller oder Faltpropeller).
Für Getriebeantrieb: Standard-Propeller wie beim Diesel, aber
Steigung ggf. anpassen. Faltpropeller empfohlen für Segelboote
(weniger Widerstand, Hydro-Regen-tauglich).

### FAQ 10: Brauche ich einen Führerschein für ein Elektroboot?

**Antwort:** In Deutschland:
- Seeschifffahrt: Ab 11,03 kW (15 PS) Motorleistung → SBF See
- Binnenschifffahrt: Ab 11,03 kW (15 PS) → SBF Binnen
- Unter 11,03 kW: Kein Führerschein (aber empfohlen)
- Bodensee: E-Motor bis 6 kW ohne Zulassung und Führerschein
- Niederlande: Kein Führerschein für Boote < 15 m und < 20 km/h

### FAQ 11: Kann ich eine Tesla-Batterie für mein Boot verwenden?

**Antwort:** Technisch möglich, aber nicht empfohlen. Tesla verwendet
NMC-Zellen (Thermal-Runaway-Risiko), die Batteriepacks sind für
Automobile konzipiert (nicht marinisiert), das BMS ist proprietär
und nicht für Marine-Einsatz ausgelegt. Keine Marine-Zertifizierung,
keine Versicherungsdeckung. Torqeedo nutzt BMW i3-Module mit
eigenem Marine-BMS — das ist die einzige seriöse
Automotive-zu-Marine-Lösung.

### FAQ 12: Wie entsorge ich Lithium-Antriebsbatterien?

**Antwort:** Lithium-Batterien sind Sondermüll und dürfen NICHT im
Hausmüll entsorgt werden. Rückgabe an den Hersteller oder über
zertifizierte Recycling-Unternehmen (z.B. Remondis, Accurec).
Transportvorschrift: UN 38.3 (Gefahrgut Klasse 9). Defekte Batterien
mit SoC < 30 % transportieren. Second-Life-Nutzung (stationärer
Speicher) ist ökologisch sinnvoll und wirtschaftlich attraktiv.

### FAQ 13: Was kostet eine Kilowattstunde „Bootsfahren"?

**Antwort:**
| Energiequelle | Kosten/kWh (2026) | Kosten pro Seemeile (5 kn, 10m Segelboot) |
|-------------|------------------|----------------------------------------|
| Landstrom (Marina DE) | 0,35 EUR/kWh | 0,08 EUR/sm |
| Solar (eigene Panels) | 0,00 EUR/kWh | 0,00 EUR/sm (nach Amortisation) |
| Diesel (1,80 EUR/L) | ~0,60 EUR/kWh (am Propeller) | 0,30 EUR/sm |
| Diesel-Generator | ~0,50 EUR/kWh | 0,25 EUR/sm |
| Hydro-Regeneration | 0,00 EUR/kWh | 0,00 EUR/sm |

Elektrisch fahren ist 3–4× günstiger pro Seemeile als Diesel.

### FAQ 14: Kann ich mein Boot mit einer Wallbox wie ein E-Auto laden?

**Antwort:** Wallboxen liefern AC (1-phasig 3,7 kW oder 3-phasig 11/22 kW).
Boote laden typischerweise über ein Bordladegerät, das AC in DC umwandelt.
Eine Wallbox mit CEE- oder Typ-2-Stecker kann als Energiequelle dienen,
wenn das Bordladegerät kompatibel ist. Torqeedo Deep Blue hat einen
integrierten 22 kW Onboard-Charger für Typ-2-Anschluss.
Standard-48V-Systeme nutzen CEE-Stecker → Steckdose, keine Wallbox nötig.

### FAQ 15: Wie verhält sich ein E-Motor bei Seegang?

**Antwort:** Besser als ein Diesel! E-Motoren haben kein Problem mit
Schräglage (kein Ölsumpf, keine Kühlwasser-Probleme). Sogar bei
Kenterung besteht kein Risiko von Wassereinbruch in den Motor
(IPX8-Motoren wie Torqeedo). Die Batterie muss allerdings fest
montiert sein (sturmfeste Halterung, 30° Krängung).

### FAQ 16: Kann ich Rückenwind-Energie per Propeller gewinnen (segelndes Motorboot)?

**Antwort:** Technisch möglich bei Motoryachten, die unter Notsegel
fahren. Praktisch kaum relevant, da Motoryachten selten segeln und
die Regenerationsleistung bei niedriger Geschwindigkeit minimal ist.
Bei Segelbooten ist Hydro-Regeneration dagegen ein Standardfeature.

### FAQ 17: Wie beeinflusst Kälte die Batterieleistung?

**Antwort:** Bei 0 °C hat eine LiFePO4-Batterie nur noch ~80 % der
Nennkapazität. Bei −10 °C noch ~60 %. Zusätzlich sperrt das BMS
das Laden unter 0 °C (Lithium-Plating-Schutz). Maßnahmen:
Batterieheizung (Heizfolie, ~50–100 W), isoliertes Batteriefach,
vor dem Laden auf > 5 °C erwärmen. In skandinavischen Gewässern
ist Batterie-Isolierung Standard.

### FAQ 18: Kann ich Brennstoffzelle und Batterie kombinieren?

**Antwort:** Ja, das ist der Range-Extender-Ansatz. EFOY Pro liefert
~100–125 W Dauerleistung (Methanol) → deckt den Bordverbrauch und
lädt die Antriebsbatterie langsam nach. Für den Hauptantrieb reicht
die Leistung nicht. Wasserstoff-Brennstoffzellen (2,5–80 kW) könnten
das ändern, sind aber 2026 noch nicht marktreif für Yachten.

### FAQ 19: Wie sieht die CO₂-Bilanz von E-Booten wirklich aus?

**Antwort:** Abhängig vom Strommix:
| Stromquelle | CO₂ pro kWh | CO₂ pro sm (10m Segelboot) |
|------------|------------|--------------------------|
| Solar (eigen) | 0 g | 0 g |
| Ökostrom (Marina) | ~25 g | 6 g |
| Deutscher Strommix | ~380 g | 91 g |
| Diesel (direkt) | ~600 g | 300 g |

Selbst mit deutschem Strommix ist das E-Boot ~70 % sauberer als
der Dieselantrieb. Mit Solar oder Ökostrom nahezu emissionsfrei.

### FAQ 20: Wie schwer ist die Umstellung von Diesel auf Elektro beim Fahren?

**Antwort:** Sehr einfach. Der Gashebel funktioniert gleich.
Unterschiede: Kein Motorstartvorgang (einfach Hebel bewegen),
kein Leerlauf-Geräusch (irritiert anfangs), sofortiges Drehmoment
beim Gasgeben, kein „Warmlaufen" nötig, Rückwärtsgang ist nur
Umpolen (sofort, kein Getriebeknacken). Die meisten Umsteiger
berichten: „Ich will nie wieder Diesel."

### FAQ 21: Gibt es Lademöglichkeiten in Marinas?

**Antwort:** Fast jede europäische Marina hat Landstromanschlüsse
(CEE 16A, 230V = 3,7 kW). Viele haben auch CEE 32A (7,4 kW).
3-Phasig (CEE 32A rot, 22 kW) ist seltener, aber im Superyacht-Bereich
Standard. Spezielle E-Boot-Ladestationen (Typ 2, DC-Schnelllader)
gibt es erst vereinzelt (Amsterdam, Bodensee, Berliner Seen).
Die vorhandene Landstrom-Infrastruktur reicht für Über-Nacht-Laden aus.

### FAQ 22: Ist ein Elektroboot versicherbar?

**Antwort:** Ja, aber die Versicherung muss informiert werden.
Einige Versicherer verlangen:
- CE-konforme Installation (ISO 16315)
- BMS mit Sicherheitsfunktionen
- Fachgerechte Installation (Zertifikat der Werft)
- LiFePO4 bevorzugt (geringere Brandrisiko-Einstufung als NMC)
Aufpreis: 0–15 % gegenüber Diesel, teilweise günstiger bei PANTAENIUS
(Progressive Versicherer).

### FAQ 23: Kann ich einen Generator nachrüsten, wenn die Batterie nicht reicht?

**Antwort:** Ja, das ist der „Range Extender"-Ansatz. Ein kleiner
Diesel-Generator (3–5 kW) als Notfall-/Ladegerät. Installation:
Generator → Ladegerät → Batterie. Oder: Seriell-Hybrid mit
permanentem Generator. Kosten: 8.000–15.000 EUR für Generator +
Installation. Viele E-Boot-Eigner rüsten nach der ersten Saison
nach, wenn sie merken, dass die Reichweite nicht reicht.

### FAQ 24: Wie schnell degradiert eine Antriebsbatterie bei Nichtnutzung?

**Antwort:** LiFePO4 bei 50 % SoC gelagert: < 3 % Kapazitätsverlust
pro Jahr. Bei 100 % SoC: ~5 % pro Jahr. Empfehlung: Im Winterlager
auf 50–70 % SoC bringen, BMS aktiv lassen (Standby-Verbrauch ~5 mA).
Alle 3 Monate SoC prüfen, nachlade wenn < 30 %. Nicht tiefentladen
(< 10 %) über Monate stehen lassen!

### FAQ 25: Kann ich Batterie und Motor verschiedener Hersteller kombinieren?

**Antwort:** Grundsätzlich ja, wenn die Spannungsebenen passen und
die Kommunikation (CAN-Bus) kompatibel ist. Standard-48V-Systeme
sind weitgehend herstellerunabhängig. Hochvolt-Systeme (Torqeedo
Deep Blue, 345 V) sind proprietärer. Empfehlung: System-Lösung
eines Herstellers bevorzugen (Garantie, Support), aber 48V-LiFePO4-
Batterien sind universell einsetzbar.

### FAQ 26: Wie verhält sich ein Elektroboot bei Gewitter?

**Antwort:** Grundsätzlich gleich wie ein Dieselboot — das
Blitzschlagrisiko hängt vom Mast und der Bootshöhe ab, nicht
vom Antrieb. Zusätzliche Vorsichtsmaßnahmen für E-Boote:
- Überspannungsschutz am Landstrom-Eingang (Varistor / SPD)
- Batterie-Trennschalter aktivieren wenn möglich
- BMS schützt gegen Überspannung an den Zellen
- Blitzableiter (bei Segelbooten: Kette vom Mastfuß ins Wasser)
  schützt die gesamte Elektronik
- Nach Blitzeinschlag: ALLE Elektronik prüfen, insbesondere BMS,
  Controller und MPPT-Regler

### FAQ 27: Wie wirkt sich die Wellenhöhe auf den Energieverbrauch aus?

**Antwort:** Seegang erhöht den Energieverbrauch erheblich:
| Wellenhöhe (signifikant) | Mehrverbrauch (Verdränger) | Reichweiten-Reduktion |
|-------------------------|--------------------------|---------------------|
| 0,0–0,3 m (glatt) | Referenz (0 %) | 0 % |
| 0,3–0,5 m (leicht) | +5–10 % | −5 bis −10 % |
| 0,5–1,0 m (mäßig) | +10–25 % | −10 bis −20 % |
| 1,0–1,5 m (rauh) | +20–40 % | −17 bis −29 % |
| 1,5–2,5 m (grob) | +35–60 % | −26 bis −38 % |
| > 2,5 m (schwer) | +50–100 % | −33 bis −50 % |

Ursache: Wellenreiten (Pitching) erhöht den Formwiderstand und
verursacht Propellerbelüftung. Kürzere Boote sind stärker betroffen.
Empfehlung: Geschwindigkeit reduzieren (Energieeinsparung überwiegt).

### FAQ 28: Kann ich einen E-Außenborder auf ein beliebiges Boot montieren?

**Antwort:** E-Außenborder bis 3 kW (z.B. Torqeedo Travel, ePropulsion
Spirit) sind universell einsetzbar — gleiche Montage wie
Benzin-Außenborder (Spiegelbefestigung). Größere E-Außenborder
(6–20 kW) erfordern eine stabile Spiegelkonstruktion und entsprechende
Kabelführung für die externe Batterie. Gewicht beachten: Ein
20 kW E-Außenborder + Batterie wiegt ~60+ kg am Spiegel.

### FAQ 29: Was passiert, wenn Seewasser in die Batterie eindringt?

**Antwort:** Salzwasser ist hochleitfähig und verursacht Kurzschlüsse
zwischen Zellen. Folgen: Sofortige Entladung, Wärmeentwicklung, im
schlimmsten Fall Thermal Runaway (bei NMC). Maßnahmen:
1. Sofort Not-Aus betätigen
2. Batteriefach nicht berühren (Kurzschluss!)
3. Batterie NICHT ins Wasser werfen (verschlimmert die Situation)
4. Feuerlöscher bereithalten
5. Professionelle Entsorgung der kontaminierten Batterie
6. Ursache beseitigen (Leck im Batteriefach, Bilge-Entwässerung)

**Prävention:** Batteriefach wasserdicht (IP67), Bilgenpumpe aktiv,
Wassermelder im Batteriefach.

### FAQ 30: Gibt es Schnellladestationen speziell für Boote?

**Antwort:** Stand 2026 gibt es erste dedizierte Marine-Schnellladestationen:
- **Aqua superPower** (UK): CCS-basierte DC-Schnelllader für Boote
  (50–150 kW), installiert in ausgewählten UK-Marinas
- **Kempower** (FI): Mobile Marine-Lader (bis 300 kW),
  Pilotprojekte in Skandinavien
- **Greenline**: Eigene Ladestationen in Partnermarinas (22 kW AC)
- **Torqeedo**: DC-Schnelllade-Standard in Entwicklung

Die meisten Boote laden jedoch weiterhin über Standard-CEE-Anschlüsse.
Das DC-Schnellladen für Boote ist noch nicht standardisiert
(kein CCS/CHAdeMO-Äquivalent für Marine).

### FAQ 31: Wie berechne ich die optimale Propellergröße für einen E-Motor?

**Antwort:** Die Propeller-Auslegung für E-Motoren unterscheidet sich
vom Diesel:
- E-Motoren drehen typischerweise 1.000–3.000 U/min (Diesel: 2.500–4.000)
- Niedrigere Drehzahl → größerer Propeller, geringere Steigung
- Optimaler Propellerwirkungsgrad bei niedrigeren Drehzahlen
- Formel (Näherung Direktantrieb):
  ```
  D_prop ≈ K × (P_motor / n_motor)^(1/3)
  K = 16–20 (je nach Rumpfform)
  D_prop in mm, P_motor in kW, n_motor in U/min
  ```
- Empfehlung: Propellerhersteller konsultieren (Gori, Flexofold, Volvo)
  mit Motor-Drehzahl-Drehmomentkurve

### FAQ 32: Kann ich den alten Dieseltank als Ballast beibehalten?

**Antwort:** Möglich, aber nicht empfohlen. Leerer Tank korrodiert
innen (Kondenswasser), alte Dieselreste verharzen. Bessere Optionen:
- Tank entfernen, Gewicht durch Batterie ersetzen
- Tank als Wassertank umwidmen (nach Reinigung)
- Ballastgewichte (Blei/Stahl) an gleicher Stelle für Trimmausgleich
- Wenn Tank bleibt: vollständig reinigen, mit Konservierungsmittel
  füllen, Leitungen blind setzen

### FAQ 33: Welche Wartung braucht ein E-Antrieb nach dem Saisonende?

**Antwort:** Winterlager-Checkliste für E-Antriebe:
1. Batterie auf 50–70 % SoC bringen (nicht voll, nicht leer)
2. Haupttrennschalter AUS (Standby-Verbrauch minimieren)
3. BMS aktiv lassen (verbraucht ~5 mA für Balancing/Schutz)
4. Alle 3 Monate SoC prüfen, nachladen wenn < 30 %
5. Propeller reinigen und Antifouling erneuern
6. Wellendichtung prüfen (bei Wellenantrieb)
7. Zinkanoden inspizieren und ggf. ersetzen
8. Kabelverbindungen auf Korrosion prüfen
9. Batteriefach trocknen, Silica-Gel einlegen
10. Landstrom-Stecker abziehen (Frostschutz für Ladegerät)

Gesamtaufwand: ~1–2 Stunden (vs. ~4–6 Stunden beim Diesel).

### FAQ 34: Kann ein Elektroboot rückwärts genauso gut fahren wie vorwärts?

**Antwort:** Ja — sogar besser als ein Dieselboot! Ein E-Motor dreht
vorwärts und rückwärts mit exakt gleicher Leistung (kein
Getriebe-Schlupf, kein Diesel-Rucken beim Einlegen des Rückwärtsgangs).
Das Drehmoment steht sofort zur Verfügung. Nachteil: Festpropeller
haben rückwärts einen ~10–15 % geringeren Wirkungsgrad (asymmetrisches
Blatt). Faltpropeller (Gori, Flexofold) haben vorwärts und rückwärts
annähernd gleiche Leistung.

### FAQ 35: Wie beeinflussen die Gezeiten meine Reichweitenplanung?

**Antwort:** Gezeitenströme können 1–4 Knoten betragen (Ärmelkanal,
Britische Inseln, Wattenmeer). Bei 5 kn Fahrt und 2 kn Gegenstrom:
- Grundgeschwindigkeit: nur 3 kn
- Leistung: bleibt bei 5 kn durch das Wasser
- Reichweite: −40 % (Energie pro sm Grundweg verdoppelt sich fast)
- Empfehlung: MIT dem Gezeitenstrom fahren, Wartezeiten einplanen.
  Bei E-Antrieb ist die Reichweite der limitierende Faktor — umso
  wichtiger ist Gezeitenplanung.

### FAQ 36: Gibt es eine Möglichkeit, Lithium-Batterien im Flugzeug als Ersatz mitzunehmen?

**Antwort:** Extrem eingeschränkt. Gemäß IATA/UN 38.3:
- Batterien > 100 Wh: Nur im Handgepäck, max. 2 Stück (bis 160 Wh)
- Batterien > 160 Wh: Verboten im Passagierflugzeug
- Antriebsbatterien (> 1.000 Wh): Nur als Gefahrgut-Frachtgut
  (Klasse 9, UN3480/3481) → Spedition beauftragen
- Praktisch: Batterie am Zielort kaufen oder per Frachtschiff senden

### FAQ 37: Wie zuverlässig sind E-Antriebe im Vergleich zu Diesel?

**Antwort:** Statistisch zuverlässiger. Ein E-Motor hat nur 1
bewegliches Teil (Rotor), ein Dieselmotor hat hunderte (Kolben,
Ventile, Zahnräder, Pumpen, Lager...). Häufigste Ausfallursachen:
- E-Antrieb: BMS-Abschaltung (meist Bedienfehler), Kabelkorrosion,
  Propellerverstopfung → alles vor Ort behebbar
- Diesel: Impellerversagen, verstopfter Filter, Anlasserdefekt,
  Kühlwasserleck → oft Werftaufenthalt nötig
- Caveat: E-Antrieb-Elektronik ist empfindlicher gegen Feuchtigkeit
  und Spannungsspitzen. Sorgfältige Installation ist entscheidend.

### FAQ 38: Was ist der Unterschied zwischen kW und PS bei Bootsmotoren?

**Antwort:** 1 kW = 1,36 PS (genauer: 1,35962). In der E-Boots-Welt
wird immer in kW angegeben. Achtung: Die „Diesel-Äquivalent"-Angaben
der Hersteller sind Marketing und nicht direkt vergleichbar, da der
E-Motor ein deutlich höheres Drehmoment bei niedriger Drehzahl hat.
Ein 10 kW E-Motor fühlt sich beim Manövrieren an wie ein 20–25 PS
Diesel, obwohl er rechnerisch nur 13,6 PS hat.

### FAQ 39: Lohnt sich ein Elektroantrieb für ein Boot, das wenig genutzt wird?

**Antwort:** Paradoxerweise besonders! Vorteile bei Wenignutzung:
- Kein Diesel, der in Leitungen und Tank altert (Dieselpest)
- Kein „Motor muss regelmäßig laufen" (Diesel braucht Belastung)
- Keine Ölwechsel bei Nichtnutzung
- Batterie bei 50 % SoC lagern → degradiert minimal
- Kein Winterdiesel, keine Frostschutz-Probleme
- Sofort startbereit nach Monaten der Nichtnutzung
Nachteil: Höhere Anschaffungskosten amortisieren sich langsamer.

### FAQ 40: Wie sieht die Zukunft des elektrischen Bootsantriebs aus?

**Antwort:** Trends und Prognosen (2026–2035):
- **Feststoffbatterien** (ab ~2028): 2× Energiedichte, sicherer,
  schneller ladbar → Reichweite verdoppelt sich
- **Natrium-Ionen** (ab ~2027): Billig, kein Lithium → Budget-Segment
- **Standardisierte Schnellladung** (ab ~2028): CCS-Marine-Standard
- **Emissionszonen** ausgeweitet: Mittelmeer-Naturschutzgebiete,
  weitere Binnengwässer, karibische Nationalparks
- **Induktionsladen** am Steg (ab ~2030): Kabellos laden
- **Hydrogen-Brennstoffzelle** als Range Extender (ab ~2030):
  1 kg H₂ = 33 kWh (vs. 1 L Diesel = 10 kWh)
- **Autonome E-Boote** für Charter und Verleih
- **Preisentwicklung**: Parität E-Antrieb ↔ Diesel erwartet ~2030

---
---

## 17. Glossar

| Begriff | Erklärung |
|---------|----------|
| **AC** | Wechselstrom (Alternating Current) — 230 V Bordnetz, Landstrom |
| **AGM** | Absorbent Glass Mat — auslaufsichere Blei-Säure-Batterie |
| **AIS** | Automatic Identification System — Schiffsidentifikation/Ortung |
| **Amperestunde (Ah)** | Maß für die elektrische Ladung einer Batterie (Kapazität) |
| **ANL-Sicherung** | Großformat-Sicherung für hohe Ströme (Typ ANL/MEGA) |
| **ABYC** | American Boat & Yacht Council — US-Bootsstandard-Organisation |
| **BLE** | Bluetooth Low Energy — drahtlose Kommunikation (Monitoring) |
| **BLDC** | Brushless DC Motor — bürstenloser Gleichstrommotor |
| **BMS** | Batterie-Management-System — Überwachung und Schutz der Batterie |
| **Boost-Modus** | Hybrid: Diesel + E-Motor treiben gleichzeitig an (Spitzenleistung) |
| **C-Rate** | Lade-/Entladerate relativ zur Kapazität (1C = volle Kapazität in 1 h) |
| **CAN-Bus** | Controller Area Network — Datenbus für Motorsteuerung/BMS |
| **CC/CV** | Constant Current / Constant Voltage — Standard-Ladeverfahren für Li-Ion |
| **CE** | Conformité Européenne — europäisches Konformitätskennzeichen |
| **CEE-Stecker** | Industrie-Rundsteckverbinder für Landstrom (blau=230V, rot=400V 3ph) |
| **Controller** | Frequenzumrichter / Motor-Controller — wandelt DC→AC für E-Motor |
| **Coulomb-Counting** | SoC-Bestimmung durch Integration des Stroms über Zeit |
| **DC** | Gleichstrom (Direct Current) — Batteriestrom |
| **DC/DC-Wandler** | Spannungswandler (z.B. 48V → 12V) für Bordnetzversorgung |
| **Derating** | Leistungsreduzierung durch den Controller bei Überhitzung |
| **Direktantrieb** | E-Motor direkt auf der Propellerwelle, ohne Getriebe |
| **DoD** | Depth of Discharge — Entladetiefe in % der Nennkapazität |
| **EMV** | Elektromagnetische Verträglichkeit — Störfreiheit elektronischer Geräte |
| **EPC** | Electronic Power Controller — ePropulsion-Steuereinheit |
| **EPDM** | Ethylen-Propylen-Dien-Kautschuk — Dichtungsmaterial |
| **Erdschluss** | Ungewollte Verbindung eines Leiters mit dem Bootskörper/Erde |
| **Faltpropeller** | Propeller, dessen Blätter sich beim Segeln zusammenklappen |
| **Galvanische Korrosion** | Elektrochemische Korrosion durch unterschiedliche Metalle |
| **Hydro-Regeneration** | Energierückgewinnung durch den Propeller beim Segeln |
| **IEC** | International Electrotechnical Commission — Normungsorganisation |
| **Inverter** | Wechselrichter — wandelt DC (Batterie) → AC (230 V Bordnetz) |
| **IP-Schutzklasse** | International Protection Rating (z.B. IP67 = staubdicht + untertauchbar) |
| **Isolationswächter** | Überwacht den Isolationswiderstand bei HV-Systemen |
| **kWh** | Kilowattstunde — Energieeinheit (1 kWh = 3,6 MJ) |
| **LFP** | Lithium-Eisenphosphat (LiFePO4) — sichere Lithium-Batterie-Chemie |
| **Lithium-Plating** | Abscheidung metallischen Lithiums beim Laden unter 0 °C |
| **LTO** | Lithium-Titanat-Oxid — extrem zyklenfeste Batteriechemie |
| **MEGA-Sicherung** | Großformat-Sicherung (ähnlich ANL, anderer Formfaktor) |
| **MPPT** | Maximum Power Point Tracker — Solarladeregler |
| **NdFeB** | Neodym-Eisen-Bor — Permanentmagnet-Material (stärkste Dauermagnete) |
| **NMC** | Nickel-Mangan-Kobalt — Lithium-Batterie-Chemie (hohe Energiedichte) |
| **NMEA 2000** | Marine-Datenbus-Standard (CAN-basiert) |
| **Not-Aus** | Roter Pilz-Taster zur sofortigen Systemabschaltung |
| **OCV** | Open Circuit Voltage — Leerlaufspannung (Batterie ohne Last) |
| **Parallel-Hybrid** | Diesel + E-Motor auf derselben Welle (mechanisch gekoppelt) |
| **PGN** | Parameter Group Number — NMEA-2000-Datentelegramm-ID |
| **PMSM** | Permanentmagnet-Synchronmotor — effizientester E-Motor-Typ |
| **Pod-Antrieb** | Außenborder- oder Unterwasser-E-Motor als kompakte Einheit |
| **Potenzialausgleich** | Verbindung aller Metallteile zur Vermeidung galvanischer Korrosion |
| **PTI** | Power Take-In — E-Motor speist ins Getriebe ein (Hybrid) |
| **PTO** | Power Take-Off — Diesel treibt Generator über Getriebe an |
| **PWM** | Pulsweitenmodulation — Steuerverfahren für E-Motoren |
| **Range Extender** | Zusatzmotor/Generator zur Reichweitenverlängerung |
| **RCD** | Residual Current Device — Fehlerstromschutzschalter |
| **Regeneration** | Energierückgewinnung (Hydro, Bremsen, Diesel-Laden) |
| **Saildrive** | Antriebseinheit durch den Rumpfboden (statt Wellenanlage) |
| **Seriell-Hybrid** | Diesel treibt nur Generator an, E-Motor treibt Propeller an |
| **SoC** | State of Charge — Ladezustand der Batterie (0–100 %) |
| **SoH** | State of Health — Gesundheitszustand der Batterie (% der Nennkapazität) |
| **Thermal Runaway** | Unkontrollierte Selbsterhitzung einer Lithium-Zelle (Brand/Explosion) |
| **Trenntrafo** | Galvanische Trennung des Bordnetzes vom Landstrom |
| **Typ-2-Stecker** | Standard-Ladestecker für E-Autos (auch marine einsetzbar) |
| **VE.Can** | Victron Energy CAN-Bus-Protokoll |
| **VE.Direct** | Victron Energy serielles Kommunikationsprotokoll |
| **VRM** | Victron Remote Management — Cloud-Monitoring-Portal |
| **Zinkanode** | Opferanode zum Korrosionsschutz (Zink wird geopfert statt Stahl/Alu) |

---
---

## 18. Schnell-Referenz

### 18.1 Leistungs-Äquivalenz E-Motor ↔ Diesel

| E-Motor (kW) | Diesel-Äquivalent (PS) | Typischer Einsatz |
|-------------|----------------------|-----------------|
| 1 | ~2–3 | Beiboot, Dinghy |
| 2 | ~5 | Jolle, kleines Segelboot |
| 3 | ~8 | Segelboot 7–8 m |
| 5 | ~12 | Segelboot 8–10 m |
| 6 | ~15 | Segelboot 9–11 m |
| 10 | ~25 | Segelboot 10–13 m, MY 8–10 m |
| 15 | ~35 | Segelboot 13–15 m, MY 10–12 m |
| 20 | ~45 | Segelboot 14–16 m, MY 11–13 m |
| 25 | ~50–60 | MY 12–15 m |
| 40 | ~80–100 | MY 14–18 m |
| 50 | ~100–120 | MY 16–20 m |
| 100 | ~200 | MY 18–24 m |

### 18.2 Batterie-Faustregeln

| Fastregel | Wert |
|----------|------|
| LiFePO4 Gewicht pro kWh | ~7 kg |
| LiFePO4 Preis pro kWh (2026) | 250–500 EUR |
| LiFePO4 Zyklen (80% DoD) | 3.000–5.000 |
| Max. nutzbare Kapazität (DoD) | 80 % |
| Laden unter 0°C | VERBOTEN |
| Lagerung ideal (SoC) | 50–70 % |
| Spannungsbereich 48V Pack (16S) | 44,8–58,4 V |
| Nennspannung 48V Pack | 51,2 V |

### 18.3 Energieverbrauch Faustregeln (Verdränger)

| Bootstyp | kWh pro Seemeile (5 kn) | kWh pro Seemeile (Rumpfgeschw.) |
|---------|------------------------|-------------------------------|
| Segelboot 8 m | 0,15 | 0,50 |
| Segelboot 10 m | 0,24 | 0,71 |
| Segelboot 12 m | 0,40 | 1,14 |
| Motoryacht 10 m | 0,30 | 0,93 |
| Motoryacht 12 m | 0,50 | 1,43 |
| Katamaran 12 m | 0,40 | 1,00 |

### 18.4 Sicherheits-Checkliste (Kurzform)

- [ ] Not-Aus-Schalter: Zugänglich vom Steuerstand?
- [ ] Hauptsicherung: Korrekt dimensioniert?
- [ ] BMS: Aktiv, keine Fehlermeldung?
- [ ] Batterie: Befestigt, belüftet, kein Wasser?
- [ ] Kabel: Keine Scheuerung, fest angeschlossen?
- [ ] Erdung: Potenzialausgleich vorhanden?
- [ ] Feuerlöscher: In Batterienähe?
- [ ] Isolationswiderstand: > 1 MΩ (HV-Systeme)?

---
---

## 19. ANHANG A–H: Fallstudien

### ANHANG A — Fallstudie: Segelboot Bavaria 34, Diesel→Elektro Umrüstung

**Ausgangslage:**
- Boot: Bavaria 34 (2008), 10,4 m LWL, 5,8 t Verdrängung
- Alter Antrieb: Volvo Penta D1-30 (30 PS), Saildrive 120S
- Motor: 8.200 Betriebsstunden, Ölverbrauch erhöht, Impellergehäuse korrodiert
- Eigner: Segler, 200 h Motor/Jahr, Revier Mittelmeer + Atlantik-Pläne

**Gewählte Lösung:**
- Motor: Oceanvolt ServoProp 10 (10 kW, direkt am SD120-Ausschnitt)
- Batterie: 4 × Victron Smart Lithium 12,8V/200Ah = 10,24 kWh (48V)
- BMS: Victron Lynx Smart BMS 500
- Solar: 4 × 100 Wp Solara semi-flex auf Bimini = 400 Wp
- MPPT: Victron SmartSolar 150/45
- Ladegerät: Victron Skylla-IP44 48/50 (2,4 kW)
- DC/DC: Victron Orion-Tr 48/12-30 für Bordnetz
- Monitoring: Cerbo GX + Touch 50

**Kosten:**
| Position | EUR |
|---------|------|
| Oceanvolt ServoProp 10 | 12.500 |
| 4 × Victron Smart LiFePO4 12,8V/200Ah | 7.800 |
| Lynx Smart BMS 500 | 520 |
| 4 × Solara 100 Wp | 1.200 |
| SmartSolar 150/45 | 310 |
| Skylla-IP44 48/50 | 700 |
| Orion-Tr 48/12-30 | 140 |
| Cerbo GX + Touch 50 | 650 |
| Kabel, Sicherungen, Kleinteile | 800 |
| Demontage Diesel + Installation E-Antrieb (Werft) | 4.500 |
| **Gesamt** | **29.120 EUR** |

**Ergebnisse nach 2 Saisons:**
- Motorlaufzeit: ~180 h/Jahr (Hafenmanöver, Flauten)
- Typische Fahrt: 2–3 h Motor bei 5 kn (Ein-/Auslaufen)
- Batterie reicht: 6–8 h bei 5 kn (10 kWh bei 1,2 kW = 8,3 h)
- Hydro-Regeneration: Ø 450 W bei Segelfahrt (6 kn Durchschnitt)
- Auf Überführung Kanaren→Kapverden: Batterie war nie < 60 % SoC
- Bordverbrauch wird komplett durch Solar + Hydro-Regen gedeckt
- Gewichtseinsparung: ~90 kg (Diesel-Motor+Tank vs. E-Motor+Batterie)
- Lautstärke: „Totenstille im Hafen — die Nachbarlieger sind neidisch"

**AYDI-Bewertung:** Score 92/100, Confidence: documented.

### ANHANG B — Fallstudie: Motoryacht Linssen 36.9 AC, Parallel-Hybrid-Nachrüstung

**Ausgangslage:**
- Boot: Linssen Grand Sturdy 36.9 AC (2015), 11,1 m, 9,5 t
- Antrieb: Volvo Penta D2-75 (75 PS), Saildrive
- Eigner: Binnenschifffahrt NL/DE, 400 h/Jahr, Amsterdam-Emissionszone
- Problem: Ab 2025 emissionsfreie Pflicht in Amsterdamer Grachten

**Gewählte Lösung:**
- Hybrid-Modul: ZF 3000 PTI (25 kW E-Motor, integriert ins ZF-Getriebe)
- Batterie: 4 × MG Energy HE 12,8V/200Ah = 10,24 kWh (48V)
  + 4 × MG Energy HE 12,8V/200Ah = 10,24 kWh (48V) → 20,48 kWh gesamt
- BMS: MG Energy Master LV
- Ladegerät: Victron Skylla-IP44 48/100 (4,8 kW)
- Solar: 6 × 200 Wp auf Flybridge-Dach = 1.200 Wp
- DC/DC: 2 × Victron Orion-Tr 48/12-30

**Kosten:**
| Position | EUR |
|---------|------|
| ZF 3000 PTI + Installation | 22.000 |
| 8 × MG Energy HE 12,8V/200Ah | 14.400 |
| MG Energy Master LV BMS | 1.200 |
| Skylla-IP44 48/100 | 1.300 |
| 6 × 200 Wp Solarpanels | 1.800 |
| MPPT SmartSolar 250/100 | 600 |
| DC/DC-Wandler + Kleinteile | 800 |
| Installation Werft (elektrisch + mechanisch) | 8.000 |
| **Gesamt** | **50.100 EUR** |

**Ergebnisse nach 1 Saison:**
- Elektrische Reichweite: ~12 sm bei 5 kn (reicht für Amsterdam-Grachten)
- Diesel-Einsparung: ~35 % (E-Betrieb im Hafen + langsame Kanalfahrt)
- Hybrid-Modus auf Langstrecke: Diesel bei 75 % Last + 15 % Laden
- Dieselverbrauch gesamt: von 8 L/h auf 5,2 L/h gesenkt
- Komfort: „Einfahrt in Amsterdam ist jetzt ein Genuss statt Dieselgestank"

**AYDI-Bewertung:** Score 85/100, Confidence: documented.

### ANHANG C — Fallstudie: Katamaran Lagoon 42, Vollelektrisch mit Solar

**Ausgangslage:**
- Boot: Lagoon 42 (2020), 12,8 m, 7,2 t (Leichtversion)
- Alter Antrieb: 2 × Yanmar 3YM30 (je 30 PS), Saildrive
- Eigner: Liveaboard-Paar, Langfahrt Mittelmeer→Karibik
- Ziel: Energieautarkie, kein Diesel mehr an Bord

**Gewählte Lösung:**
- 2 × Oceanvolt ServoProp 15 (je 15 kW)
- Batterie: 40 kWh Oceanvolt Aqua (LiFePO4, 2 × 20 kWh)
- Solar: 12 × 200 Wp (2.400 Wp) auf Dach und Bimini
- MPPT: 2 × Victron SmartSolar RS 450/100
- Hydro-Regeneration: Integriert in ServoProp
- Windgenerator: Superwind 350
- DC/DC + Inverter: Victron MultiPlus-II 48/5000

**Kosten:**
| Position | EUR |
|---------|------|
| 2 × Oceanvolt ServoProp 15 | 35.000 |
| Oceanvolt Aqua 40 kWh | 24.000 |
| 12 × 200 Wp Solarpanels + Montage | 5.500 |
| 2 × SmartSolar RS 450/100 | 1.400 |
| Superwind 350 | 2.100 |
| MultiPlus-II 48/5000 | 2.000 |
| DC/DC, BMS, Cerbo GX, Kabel | 3.500 |
| Demontage 2× Diesel + Installation | 12.000 |
| **Gesamt** | **85.500 EUR** |

**Ergebnisse nach 3 Saisons:**
- Energieautarkie erreicht: kein Diesel in 3 Jahren
- Solar liefert Ø 8–12 kWh/Tag (Mittelmeer/Karibik)
- Hydro-Regen liefert Ø 5–8 kWh/Tag (auf See)
- Windgenerator: Ø 2–4 kWh/Tag
- Gesamtversorgung: 15–24 kWh/Tag → deckt Bordverbrauch (8–12 kWh)
  + Antrieb für 2–3 h/Tag (Ankerplatzwechsel)
- Motorstunden: ~150 h/Jahr (Hafen, Flaute, Ankerplatz-Hüpfen)
- Batterie SoH nach 3 Jahren: 96 % (minimal degradiert)
- Gewichtsbilanz: +120 kg gesamt (2× Diesel −380 kg, Batterie+Solar +500 kg)
- Geschwindigkeit unter Motor: max. 7,5 kn (Rumpfgeschwindigkeit)

**AYDI-Bewertung:** Score 95/100, Confidence: documented.

### ANHANG D — Fallstudie: Grachtenboot 8 m, Neubau vollelektrisch

**Ausgangslage:**
- Boot: Neubau Grachtenboot (Sloep) 8 m, Stahl, 2,5 t
- Einsatz: Vermietung Amsterdam, 8 h/Tag Saison (Apr–Okt)
- Anforderung: Emissionsfrei (Amsterdam-Pflicht), leise, robust

**Gewählte Lösung:**
- Motor: Bellmarine DriveMaster 5.0 (5 kW, 48V)
- Batterie: 2 × ePropulsion E80 (je 8 kWh) = 16 kWh
- Ladegerät: 48V/80A (3,8 kW) → Nachtladung (8 h → voll)
- Solar: 2 × 200 Wp auf Sonnendach = 400 Wp

**Kosten:**
| Position | EUR |
|---------|------|
| Bellmarine DriveMaster 5.0 | 5.700 |
| 2 × ePropulsion E80 | 11.000 |
| Ladegerät 48V/80A | 750 |
| Solar 400 Wp + MPPT | 900 |
| Installation | 2.500 |
| **Gesamt** | **20.850 EUR** |

**Ergebnisse nach 2 Saisons:**
- 8 h Betrieb bei 5 km/h (Grachten-Tempo): Verbrauch ~10 kWh/Tag
- Batterie reicht: 16 kWh × 0,8 DoD = 12,8 kWh nutzbar → 8+ Stunden
- Solar liefert ~1,5 kWh/Tag (Teilbeschattung Grachten)
- Nachtladung: 10 kWh / 3,8 kW = 2,6 h (vor Mitternacht voll)
- Stromkosten: ~1.050 kWh × 0,35 EUR = 368 EUR/Saison
- Dieselkosten wären: ~450 L × 1,80 EUR = 810 EUR/Saison
- Kein Ölgestank, kein Dieselfleck am Heck, Kunden begeistert
- ROI: Aufpreis E-Antrieb amortisiert nach ~7 Jahren

**AYDI-Bewertung:** Score 90/100, Confidence: documented.

### ANHANG E — Fallstudie: Superyacht 28 m, Seriell-Hybrid

**Ausgangslage:**
- Boot: Custom Motoryacht 28 m (Aluminium), 95 t, 2023
- Bisherig: 2 × MAN D2676 (je 588 kW), ZF-Getriebe
- Problem: Hoher Verbrauch (~180 L/h bei 18 kn), Lärm, Emissionen
- Ziel: Emissionsfreies Manövrieren, Ankerruhe, -30% Verbrauch

**Gewählte Lösung:**
- Seriell-Hybrid: 2 × Fischer Panda E-Drive 80 (je 80 kW)
- Generator: 2 × Fischer Panda iSeries 65i (je 65 kW)
- Batterie: 200 kWh NMC (Torqeedo Deep Blue, 6 × 33,4 kWh)
- Hotellast: Vollständig aus Batterie/Generator
- Dynamic Positioning: Über E-Motoren

**Kosten:**
| Position | EUR |
|---------|------|
| 2 × E-Drive 80 (160 kW gesamt) | 115.000 |
| 2 × Fischer Panda 65i Generator | 82.000 |
| 6 × Torqeedo Deep Blue i3 Pack (200 kWh) | 140.000 |
| Leistungselektronik + BMS | 45.000 |
| Verkabelung (HV) | 28.000 |
| Systemintegration + Inbetriebnahme | 65.000 |
| Klassifizierung (DNV) | 35.000 |
| **Gesamt** | **510.000 EUR** |

**Ergebnisse:**
- Elektrische Reichweite (Manöver): ~15 sm bei 6 kn (200 kWh)
- Generator-Betrieb (12 kn Reise): Verbrauch 38 L/h (−40 % vs. Diesel-Direkt)
- Ankerruhe: 48+ h aus Batterie (Hotellast ~4 kW)
- Schallpegel (Anker): < 40 dB(A) vs. 55 dB(A) mit laufendem Generator
- DPS für Positionshalt in der Bucht ohne Anker
- Crew-Zufriedenheit: „Wie ein anderes Boot — endlich Ruhe"

**AYDI-Bewertung:** Score 88/100, Confidence: documented.

### ANHANG F — Fallstudie: Torqeedo Deep Blue 50i auf Motoryacht 14 m

**Ausgangslage:**
- Boot: Greenline 40 (2021), 12,8 m, 8,5 t (Verdränger/Semi-Gleiter)
- Werksantrieb: Volvo D3-220 (220 PS, Diesel) + optional Hybrid
- Eigner: Bodensee, 200 h/Jahr, umweltbewusst

**Gewählte Lösung:**
- Motor: Torqeedo Deep Blue 50i (50 kW)
- Batterie: 3 × Deep Blue i3 Pack = 100 kWh
- Charger: Torqeedo Deep Blue Charger 22 kW (3-phasig)
- Solar: 1.600 Wp auf Flybridge

**Kosten:**
| Position | EUR |
|---------|------|
| Torqeedo Deep Blue 50i | 32.000 |
| 3 × i3 Pack (100 kWh) | 72.000 |
| Deep Blue Charger 22 kW | 6.000 |
| Solar 1.600 Wp + MPPT | 4.500 |
| Installation | 15.000 |
| **Gesamt** | **129.500 EUR** |

**Ergebnisse nach 1 Saison:**
- Rumpfgeschwindigkeit (7,5 kn): 35 sm Reichweite (100 kWh)
- Sparfahrt (5 kn): 80 sm Reichweite
- Bodensee-Überquerung (Konstanz→Bregenz, 30 sm): machbar bei 6 kn
- Laden am CEE 32A (22 kW): 5 h für Vollladung
- Solar-Ertrag: ~6 kWh/Tag (Sommer) → 15 sm Bonus-Reichweite bei 5 kn
- Betriebskosten: ~0,15 EUR/sm (Strom) vs. ~1,20 EUR/sm (Diesel)

**AYDI-Bewertung:** Score 82/100, Confidence: documented.

### ANHANG G — Fallstudie: ePropulsion Navy 6.0 auf Segelboot 9 m

**Ausgangslage:**
- Boot: Dehler 30 OD (2019), 9,1 m, 3,8 t, Saildrive (SD20)
- Alter Motor: Yanmar 1GM10 (10 PS), 3.200 Betriebsstunden
- Eigner: Regattasegler + Wochenend-Cruiser, Ostsee

**Gewählte Lösung:**
- Motor: ePropulsion Navy 6.0 Evo (6 kW, mit Saildrive-Adapter)
- Batterie: 2 × ePropulsion E40 (je 4 kWh) = 8 kWh
- Ladegerät: ePropulsion-Ladegerät 48V/20A (960 W)
- Kein Solar (Regattaboot, Gewicht sparen)

**Kosten:**
| Position | EUR |
|---------|------|
| ePropulsion Navy 6.0 Evo | 4.500 |
| Saildrive-Adapter SD20 | 800 |
| 2 × ePropulsion E40 (8 kWh) | 5.800 |
| Ladegerät + Kabel | 600 |
| Installation (Werft) | 3.000 |
| **Gesamt** | **14.700 EUR** |

**Ergebnisse nach 1 Saison:**
- Gewichtsersparnis: 45 kg (alter Diesel+Tank vs. E-Motor+Batterie)
- Reichweite bei 5 kn: ~25 sm (ausreichend für Ostsee-Revierfahrten)
- Regatta: Faltpropeller minimiert Widerstand, kein Diesel-Startproblem
- Hafenmanöver: Sofortiges Drehmoment, exakte Steuerung
- Lautstärke: „Man hört nur das Plätschern — unfassbar"
- Nachteil: Keine Hydro-Regen (Faltpropeller + kein ServoProp-Konzept)

**AYDI-Bewertung:** Score 88/100, Confidence: documented.

### ANHANG H — Fallstudie: Fehlgeschlagene Umrüstung — Motoryacht 15 m Gleiter

**Ausgangslage:**
- Boot: Cranchi Endurance 44 (2017), 14,5 m, 12 t, Gleiter
- Alter Antrieb: 2 × Volvo D6-370 (je 370 PS = 272 kW)
- Eigner wollte rein-elektrisch umrüsten

**Fehlberechnung:**
- Gleitfahrt bei 25 kn: 2 × 250 kW = 500 kW Antriebsleistung
- Für 2 h Fahrt: 500 kW × 2 h = 1.000 kWh Energie nötig
- In LiFePO4: 1.000 kWh / 150 Wh/kg = ~6.700 kg Batterien
- Boot wiegt 12 t, Batterien alleine 6,7 t → unmöglich!

**Was tatsächlich passierte:**
- Eigner installierte 100 kWh Batterie (unrealistisch klein)
- Reichweite: ~8 sm bei 7 kn (Verdrängerfahrt, kein Gleiten)
- Oder: ~2 sm bei 15 kn (Semi-Gleiten, dann leer)
- Boot war unbrauchbar für den gewünschten Einsatz
- Rückbau auf Diesel nach 6 Monaten

**Lehren:**
1. Gleiter und rein-elektrisch sind 2026 inkompatibel
2. Energiedichte von Batterien ist ~80× geringer als Diesel
3. Gleitboote benötigen hohe Leistung → hoher Energieverbrauch
4. Nur Verdränger und langsame Semiverdränger sind E-tauglich
5. IMMER zuerst rechnen, dann kaufen

**AYDI-Bewertung:** Score 15/100 (Fehlplanung), Confidence: documented.

---
---

## 20. ANHANG I–R: Pydantic v2 Datenmodelle

### ANHANG I — Elektroantrieb-Datenmodell

```python
"""
AYDI Elektroantrieb-Datenmodelle — Pydantic v2
Alle Modelle verwenden model_config = {"from_attributes": True}
"""

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import date


class PropulsionType(str, Enum):
    """Antriebstyp."""
    PURE_ELECTRIC = "pure_electric"
    PARALLEL_HYBRID = "parallel_hybrid"
    SERIAL_HYBRID = "serial_hybrid"
    DIESEL_ELECTRIC = "diesel_electric"


class ElectricMotorType(str, Enum):
    """Typ des Elektromotors."""
    PMSM = "pmsm"
    ASM = "asm"
    BLDC = "bldc"
    DC_BRUSHED = "dc_brushed"


class MountingType(str, Enum):
    """Einbauart."""
    SHAFT_DRIVE = "shaft_drive"
    SAILDRIVE = "saildrive"
    POD_DRIVE = "pod_drive"
    OUTBOARD = "outboard"


class CoolingType(str, Enum):
    """Kühlungskonzept."""
    AIR = "air"
    SEAWATER_DIRECT = "seawater_direct"
    CLOSED_LOOP_WATER = "closed_loop_water"
    OIL = "oil"


class MotorCondition(str, Enum):
    """Zustand des Elektromotors."""
    NEW = "new"
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    DEFECTIVE = "defective"


class ConfidenceLevel(str, Enum):
    """AYDI Confidence Level."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class ElectricMotorSpec(BaseModel):
    """Spezifikation eines Elektromotors."""
    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller (z.B. Torqeedo, Oceanvolt)")
    model: str = Field(..., description="Modellbezeichnung")
    motor_type: ElectricMotorType = Field(..., description="Motortyp")
    mounting_type: MountingType = Field(..., description="Einbauart")
    nominal_power_kw: float = Field(..., ge=0, description="Nennleistung (kW)")
    peak_power_kw: Optional[float] = Field(None, ge=0, description="Spitzenleistung (kW)")
    voltage_v: float = Field(..., ge=0, description="Nennspannung (V)")
    max_rpm: int = Field(..., ge=0, description="Maximale Drehzahl (U/min)")
    efficiency_pct: float = Field(..., ge=0, le=100, description="Wirkungsgrad (%)")
    cooling: CoolingType = Field(..., description="Kühlungskonzept")
    weight_kg: float = Field(..., ge=0, description="Motorgewicht (kg)")
    ip_rating: str = Field(default="IP67", description="Schutzklasse (z.B. IP67, IPX8)")
    has_regeneration: bool = Field(default=False, description="Hydro-Regeneration möglich")
    max_regen_power_w: Optional[float] = Field(None, ge=0, description="Max. Regenerationsleistung (W)")
    price_eur: Optional[float] = Field(None, ge=0, description="Listenpreis (EUR)")
    diesel_equivalent_hp: Optional[int] = Field(None, ge=0, description="Diesel-Äquivalent (PS)")
```

### ANHANG J — Batterie-Datenmodell

```python
class BatteryChemistry(str, Enum):
    """Batterie-Chemie."""
    LIFEPO4 = "lifepo4"
    NMC = "nmc"
    NCA = "nca"
    LTO = "lto"
    LEAD_ACID_AGM = "lead_acid_agm"
    LEAD_ACID_GEL = "lead_acid_gel"


class BatteryCondition(str, Enum):
    """Zustand der Batterie."""
    NEW = "new"
    EXCELLENT = "excellent"
    GOOD = "good"
    DEGRADED = "degraded"
    END_OF_LIFE = "end_of_life"
    DEFECTIVE = "defective"


class MarineBatterySpec(BaseModel):
    """Spezifikation einer Marine-Antriebsbatterie."""
    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    chemistry: BatteryChemistry = Field(..., description="Batterie-Chemie")
    nominal_voltage_v: float = Field(..., ge=0, description="Nennspannung (V)")
    capacity_ah: float = Field(..., ge=0, description="Kapazität (Ah)")
    energy_kwh: float = Field(..., ge=0, description="Energie (kWh)")
    weight_kg: float = Field(..., ge=0, description="Gewicht (kg)")
    cycle_life: int = Field(..., ge=0, description="Zyklenlebensdauer (bei 80 % DoD)")
    max_charge_rate_c: float = Field(default=1.0, ge=0, description="Max. Laderate (C)")
    max_discharge_rate_c: float = Field(default=2.0, ge=0, description="Max. Entladerate (C)")
    max_dod_pct: float = Field(default=80.0, ge=0, le=100, description="Max. Entladetiefe (%)")
    ip_rating: str = Field(default="IP54", description="Schutzklasse")
    bms_integrated: bool = Field(default=False, description="BMS integriert")
    marine_certified: bool = Field(default=False, description="Marine-zertifiziert (CE/ABYC)")
    price_eur: Optional[float] = Field(None, ge=0, description="Listenpreis (EUR)")
    min_charge_temp_c: float = Field(default=0.0, description="Min. Ladetemperatur (°C)")
    max_charge_temp_c: float = Field(default=45.0, description="Max. Ladetemperatur (°C)")
    min_discharge_temp_c: float = Field(default=-20.0, description="Min. Entladetemperatur (°C)")
    max_discharge_temp_c: float = Field(default=60.0, description="Max. Entladetemperatur (°C)")


class BatteryConditionReport(BaseModel):
    """Zustandsbericht einer eingebauten Antriebsbatterie."""
    model_config = {"from_attributes": True}

    battery_spec: Optional[MarineBatterySpec] = Field(None, description="Batterie-Spezifikation")
    installation_date: Optional[date] = Field(None, description="Einbaudatum")
    cycles_used: Optional[int] = Field(None, ge=0, description="Verbrauchte Zyklen")
    soh_pct: Optional[float] = Field(None, ge=0, le=100, description="State of Health (%)")
    last_soc_pct: Optional[float] = Field(None, ge=0, le=100, description="Letzter SoC (%)")
    cell_balance_mv: Optional[float] = Field(None, ge=0, description="Max. Zelldifferenz (mV)")
    condition: BatteryCondition = Field(..., description="Zustandsbewertung")
    has_swelling: bool = Field(default=False, description="Aufblähung festgestellt")
    has_corrosion: bool = Field(default=False, description="Korrosion an Terminals")
    has_moisture: bool = Field(default=False, description="Feuchtigkeit im Batteriefach")
    ventilation_adequate: bool = Field(default=True, description="Belüftung ausreichend")
    bms_errors: list[str] = Field(default_factory=list, description="BMS-Fehlermeldungen")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level")
    score: int = Field(..., ge=0, le=100, description="AYDI-Score (0–100)")
    findings: list[str] = Field(default_factory=list, description="Befunde (deutsch)")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen (deutsch)")
```

### ANHANG K — Hybrid-System-Datenmodell

```python
class HybridMode(str, Enum):
    """Betriebsmodus Hybrid-System."""
    PURE_ELECTRIC = "pure_electric"
    DIESEL_ONLY = "diesel_only"
    HYBRID_CHARGE = "hybrid_charge"
    BOOST = "boost"
    HOTEL = "hotel"
    REGENERATION = "regeneration"


class HybridSystemSpec(BaseModel):
    """Spezifikation eines Hybrid-Antriebssystems."""
    model_config = {"from_attributes": True}

    propulsion_type: PropulsionType = Field(..., description="Antriebskonzept")
    electric_motor: ElectricMotorSpec = Field(..., description="Elektromotor")
    diesel_power_kw: Optional[float] = Field(None, ge=0, description="Diesel-Leistung (kW)")
    diesel_manufacturer: Optional[str] = Field(None, description="Diesel-Hersteller")
    diesel_model: Optional[str] = Field(None, description="Diesel-Modell")
    generator_power_kw: Optional[float] = Field(None, ge=0, description="Generator-Leistung (kW)")
    battery_total_kwh: float = Field(..., ge=0, description="Gesamte Batteriekapazität (kWh)")
    available_modes: list[HybridMode] = Field(..., description="Verfügbare Betriebsmodi")
    electric_range_nm: Optional[float] = Field(None, ge=0, description="Elektrische Reichweite (sm)")
    electric_range_speed_kn: Optional[float] = Field(None, ge=0, description="Geschwindigkeit für E-Reichweite (kn)")
    total_system_weight_kg: float = Field(..., ge=0, description="Gesamtgewicht System (kg)")
    price_total_eur: Optional[float] = Field(None, ge=0, description="Gesamtpreis System (EUR)")
```

### ANHANG L — Reichweiten-Berechnungsmodell

```python
class RangeCalculationInput(BaseModel):
    """Eingabewerte für die Reichweitenberechnung."""
    model_config = {"from_attributes": True}

    displacement_kg: float = Field(..., ge=0, description="Verdrängung (kg)")
    lwl_m: float = Field(..., ge=0, description="Wasserlinienlänge (m)")
    beam_m: float = Field(..., ge=0, description="Breite (m)")
    motor_power_kw: float = Field(..., ge=0, description="Motorleistung (kW)")
    battery_kwh: float = Field(..., ge=0, description="Batteriekapazität (kWh)")
    max_dod_pct: float = Field(default=80.0, ge=0, le=100, description="Max. DoD (%)")
    system_efficiency: float = Field(default=0.90, ge=0, le=1.0, description="Systemwirkungsgrad")
    target_speed_kn: float = Field(..., ge=0, description="Zielgeschwindigkeit (kn)")
    hotel_load_kw: float = Field(default=0.2, ge=0, description="Bordverbrauch (kW)")
    wind_speed_kn: float = Field(default=0.0, ge=0, description="Windgeschwindigkeit (kn, Gegenwind)")
    current_kn: float = Field(default=0.0, description="Strom (kn, negativ = Gegenstrom)")
    hull_fouling_pct: float = Field(default=0.0, ge=0, le=50, description="Bewuchs-Zuschlag (%)")
    battery_soh_pct: float = Field(default=100.0, ge=0, le=100, description="Batterie SoH (%)")
    water_temp_c: float = Field(default=20.0, description="Wassertemperatur (°C)")
    reserve_pct: float = Field(default=15.0, ge=0, le=50, description="Sicherheitsreserve (%)")


class RangeCalculationResult(BaseModel):
    """Ergebnis der Reichweitenberechnung."""
    model_config = {"from_attributes": True}

    usable_energy_kwh: float = Field(..., ge=0, description="Nutzbare Energie (kWh)")
    power_at_speed_kw: float = Field(..., ge=0, description="Leistung bei Zielgeschwindigkeit (kW)")
    energy_per_nm_kwh: float = Field(..., ge=0, description="Energieverbrauch (kWh/sm)")
    range_nm: float = Field(..., ge=0, description="Reichweite (sm)")
    range_with_reserve_nm: float = Field(..., ge=0, description="Reichweite mit Reserve (sm)")
    endurance_hours: float = Field(..., ge=0, description="Fahrzeit (h)")
    hull_speed_kn: float = Field(..., ge=0, description="Rumpfgeschwindigkeit (kn)")
    speed_vs_hull_speed_pct: float = Field(..., ge=0, description="Zielgeschw. / Rumpfgeschw. (%)")
    warnings: list[str] = Field(default_factory=list, description="Warnungen (deutsch)")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level")
```

### ANHANG M — Ladeinfrastruktur-Datenmodell

```python
class ChargingSource(str, Enum):
    """Energiequelle für Laden."""
    SHORE_POWER = "shore_power"
    SOLAR = "solar"
    HYDRO_REGENERATION = "hydro_regeneration"
    WIND_GENERATOR = "wind_generator"
    DIESEL_GENERATOR = "diesel_generator"
    FUEL_CELL = "fuel_cell"


class ChargingSystemSpec(BaseModel):
    """Spezifikation der Ladeinfrastruktur an Bord."""
    model_config = {"from_attributes": True}

    sources: list[ChargingSource] = Field(..., description="Verfügbare Energiequellen")
    shore_charger_kw: Optional[float] = Field(None, ge=0, description="Landstrom-Ladegerät (kW)")
    shore_charger_phases: Optional[int] = Field(None, ge=1, le=3, description="Phasen (1 oder 3)")
    solar_wp: Optional[float] = Field(None, ge=0, description="Solar installiert (Wp)")
    solar_daily_kwh: Optional[float] = Field(None, ge=0, description="Solar Tagesertrag (kWh, Durchschnitt)")
    hydro_regen_max_w: Optional[float] = Field(None, ge=0, description="Hydro-Regen max. (W)")
    wind_gen_rated_w: Optional[float] = Field(None, ge=0, description="Windgenerator Nennleistung (W)")
    diesel_gen_kw: Optional[float] = Field(None, ge=0, description="Diesel-Generator (kW)")
    fuel_cell_w: Optional[float] = Field(None, ge=0, description="Brennstoffzelle (W)")
    daily_energy_budget_kwh: float = Field(default=0.0, ge=0, description="Tages-Energiebudget gesamt (kWh)")
    time_to_full_charge_h: Optional[float] = Field(None, ge=0, description="Zeit bis Vollladung (h, Landstrom)")
```

### ANHANG N — Galvanische Korrosion-Datenmodell

```python
class CorrosionRiskLevel(str, Enum):
    """Korrosionsrisiko-Stufe."""
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class CorrosionProtectionType(str, Enum):
    """Korrosionsschutz-Maßnahme."""
    ZINC_ANODES = "zinc_anodes"
    ALUMINUM_ANODES = "aluminum_anodes"
    MAGNESIUM_ANODES = "magnesium_anodes"
    GALVANIC_ISOLATOR = "galvanic_isolator"
    ISOLATION_TRANSFORMER = "isolation_transformer"
    POTENTIAL_EQUALIZATION = "potential_equalization"
    ICCP = "iccp"


class GalvanicCorrosionAssessment(BaseModel):
    """Bewertung des galvanischen Korrosionsrisikos bei E-Antrieb."""
    model_config = {"from_attributes": True}

    motor_isolation_mohm: Optional[float] = Field(None, ge=0, description="Motor-Isolationswiderstand (MΩ)")
    potential_equalization: bool = Field(default=False, description="Potenzialausgleich vorhanden")
    anode_type: Optional[CorrosionProtectionType] = Field(None, description="Anodentyp")
    anode_condition_pct: Optional[float] = Field(None, ge=0, le=100, description="Anodenzustand (%)")
    shore_power_isolator: bool = Field(default=False, description="Trenntrafo / Galvanischer Isolator")
    leak_current_ma: Optional[float] = Field(None, ge=0, description="Leckstrom gemessen (mA)")
    risk_level: CorrosionRiskLevel = Field(..., description="Korrosionsrisiko")
    protection_measures: list[CorrosionProtectionType] = Field(
        default_factory=list, description="Vorhandene Schutzmaßnahmen"
    )
    confidence: ConfidenceLevel = Field(..., description="Confidence Level")
    score: int = Field(..., ge=0, le=100, description="AYDI-Score (0–100)")
    findings: list[str] = Field(default_factory=list, description="Befunde (deutsch)")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen (deutsch)")
```

### ANHANG O — Umrüstungs-Datenmodell

```python
class ConversionStatus(str, Enum):
    """Status der Umrüstung."""
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"


class DieselToElectricConversion(BaseModel):
    """Dokumentation einer Diesel→Elektro Umrüstung."""
    model_config = {"from_attributes": True}

    boat_name: str = Field(..., description="Bootsname")
    boat_type: str = Field(..., description="Bootstyp und Modell")
    boat_length_m: float = Field(..., ge=0, description="Bootslänge (m)")
    displacement_kg: float = Field(..., ge=0, description="Verdrängung (kg)")
    old_engine: str = Field(..., description="Alter Dieselmotor (Hersteller/Modell)")
    old_engine_hp: float = Field(..., ge=0, description="Alte Motorleistung (PS)")
    old_engine_hours: Optional[int] = Field(None, ge=0, description="Betriebsstunden alter Motor")
    new_motor: ElectricMotorSpec = Field(..., description="Neuer Elektromotor")
    battery_spec: MarineBatterySpec = Field(..., description="Batterie-Spezifikation")
    battery_count: int = Field(default=1, ge=1, description="Anzahl Batterie-Module")
    total_battery_kwh: float = Field(..., ge=0, description="Gesamte Batteriekapazität (kWh)")
    charging: ChargingSystemSpec = Field(..., description="Ladeinfrastruktur")
    weight_change_kg: float = Field(..., description="Gewichtsänderung (+ schwerer, − leichter)")
    trim_change_deg: Optional[float] = Field(None, description="Trimänderung (°)")
    conversion_date: Optional[date] = Field(None, description="Umrüstungsdatum")
    conversion_yard: Optional[str] = Field(None, description="Ausführende Werft")
    cost_material_eur: float = Field(default=0, ge=0, description="Materialkosten (EUR)")
    cost_labor_eur: float = Field(default=0, ge=0, description="Arbeitskosten (EUR)")
    cost_total_eur: float = Field(default=0, ge=0, description="Gesamtkosten (EUR)")
    status: ConversionStatus = Field(default=ConversionStatus.PLANNED, description="Status")
    ce_conformity: bool = Field(default=False, description="CE-Konformität bestätigt")
    insurance_notified: bool = Field(default=False, description="Versicherung informiert")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level")
    score: int = Field(..., ge=0, le=100, description="AYDI-Score (0–100)")
    findings: list[str] = Field(default_factory=list, description="Befunde (deutsch)")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen (deutsch)")
```

### ANHANG P — TCO-Vergleichsmodell

```python
class TCOScenario(str, Enum):
    """TCO-Vergleichsszenario."""
    DIESEL = "diesel"
    PURE_ELECTRIC = "pure_electric"
    PARALLEL_HYBRID = "parallel_hybrid"
    SERIAL_HYBRID = "serial_hybrid"


class TCOCalculation(BaseModel):
    """Total Cost of Ownership Berechnung."""
    model_config = {"from_attributes": True}

    scenario: TCOScenario = Field(..., description="Szenario")
    analysis_period_years: int = Field(default=10, ge=1, le=30, description="Betrachtungszeitraum (Jahre)")
    acquisition_cost_eur: float = Field(..., ge=0, description="Anschaffungskosten (EUR)")
    annual_fuel_cost_eur: float = Field(default=0, ge=0, description="Jährliche Kraftstoffkosten (EUR)")
    annual_electricity_cost_eur: float = Field(default=0, ge=0, description="Jährliche Stromkosten (EUR)")
    annual_maintenance_eur: float = Field(default=0, ge=0, description="Jährliche Wartungskosten (EUR)")
    battery_replacement_eur: float = Field(default=0, ge=0, description="Batterietausch (anteilig/Jahr)")
    annual_insurance_delta_eur: float = Field(default=0, description="Versicherungs-Differenz (EUR/Jahr)")
    residual_value_pct: float = Field(default=20.0, ge=0, le=100, description="Restwert nach Periode (%)")
    tco_total_eur: float = Field(..., description="TCO gesamt (EUR)")
    tco_per_year_eur: float = Field(..., ge=0, description="TCO pro Jahr (EUR)")
    tco_per_operating_hour_eur: Optional[float] = Field(None, ge=0, description="TCO pro Betriebsstunde (EUR)")
    co2_total_kg: Optional[float] = Field(None, ge=0, description="CO₂ gesamt (kg)")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level")
```

### ANHANG Q — Elektro-Antrieb Gesamtbewertung

```python
class ElectricPropulsionAssessment(BaseModel):
    """AYDI-Gesamtbewertung eines elektrischen Antriebssystems."""
    model_config = {"from_attributes": True}

    propulsion_type: PropulsionType = Field(..., description="Antriebskonzept")
    motor_assessment: Optional[dict] = Field(None, description="Motor-Bewertung")
    battery_assessment: Optional[BatteryConditionReport] = Field(None, description="Batterie-Bewertung")
    corrosion_assessment: Optional[GalvanicCorrosionAssessment] = Field(None, description="Korrosions-Bewertung")
    charging_spec: Optional[ChargingSystemSpec] = Field(None, description="Ladeinfrastruktur")
    range_calculation: Optional[RangeCalculationResult] = Field(None, description="Reichweitenberechnung")
    tco_comparison: Optional[list[TCOCalculation]] = Field(None, description="TCO-Vergleich")
    overall_score: int = Field(..., ge=0, le=100, description="Gesamtscore (0–100)")
    motor_score: int = Field(default=0, ge=0, le=100, description="Motor-Score")
    battery_score: int = Field(default=0, ge=0, le=100, description="Batterie-Score")
    charging_score: int = Field(default=0, ge=0, le=100, description="Lade-Score")
    safety_score: int = Field(default=0, ge=0, le=100, description="Sicherheits-Score")
    installation_score: int = Field(default=0, ge=0, le=100, description="Installations-Score")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level")
    findings: list[str] = Field(default_factory=list, description="Befunde (deutsch)")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen (deutsch)")
    warnings: list[str] = Field(default_factory=list, description="Warnungen (deutsch)")
```

### ANHANG R — EMV-Bewertungsmodell

```python
class EMVSeverity(str, Enum):
    """Schweregrad der EMV-Störung."""
    NONE = "none"
    MINOR = "minor"
    MODERATE = "moderate"
    SEVERE = "severe"


class EMVAssessment(BaseModel):
    """Bewertung elektromagnetischer Verträglichkeit."""
    model_config = {"from_attributes": True}

    controller_ce_certified: bool = Field(default=True, description="Controller CE-zertifiziert")
    cable_routing_parallel: bool = Field(default=False, description="DC-Kabel parallel geführt")
    emv_filter_installed: bool = Field(default=False, description="EMV-Filter installiert")
    min_distance_antenna_cm: Optional[float] = Field(None, ge=0, description="Min. Abstand Antenne↔Controller (cm)")
    vhf_interference: EMVSeverity = Field(default=EMVSeverity.NONE, description="VHF-Störung")
    ais_interference: EMVSeverity = Field(default=EMVSeverity.NONE, description="AIS-Störung")
    gps_interference: EMVSeverity = Field(default=EMVSeverity.NONE, description="GPS-Störung")
    autopilot_interference: EMVSeverity = Field(default=EMVSeverity.NONE, description="Autopilot-Störung")
    potential_equalization: bool = Field(default=False, description="Potenzialausgleich vorhanden")
    overall_severity: EMVSeverity = Field(..., description="Gesamtbewertung EMV")
    confidence: ConfidenceLevel = Field(..., description="Confidence Level")
    score: int = Field(..., ge=0, le=100, description="AYDI-Score (0–100)")
    findings: list[str] = Field(default_factory=list, description="Befunde (deutsch)")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen (deutsch)")
```

---

---
---

## 21. Hersteller-Kontakte und Service-Netzwerk

### 21.1 Hersteller-Kontakt für Notfälle

| Hersteller | Hotline | E-Mail | Reaktionszeit |
|-----------|---------|--------|-------------|
| Torqeedo | +49 8151 2646-0 | support@torqeedo.com | 24 h (Mo–Fr) |
| ePropulsion | +31 20 2621 895 | support@epropulsion.com | 48 h |
| Oceanvolt | +358 40 824 3550 | support@oceanvolt.com | 24 h (Mo–Fr) |
| Bellmarine | +31 111 670 510 | info@bellmarine.nl | 48 h |
| Fischer Panda | +49 5251 24100-0 | info@fischerpanda.de | 24 h |
| Victron Energy | +31 36 535 97 00 | service@victronenergy.com | 24–48 h |
| Mastervolt | +31 20 342 21 00 | service@mastervolt.com | 24–48 h |

### 21.2 Autorisierte Service-Partner (Auswahl Europa)

| Region | Service-Partner | Hersteller | Adresse |
|--------|---------------|-----------|---------|
| Ostsee (DE) | SVB Yacht-Technik | Alle | Bremen |
| Nordsee (DE) | Busse Yachtshop | Torqeedo, Victron | Flensburg |
| Bodensee | Yachtservice Ultramarin | Torqeedo, Oceanvolt | Kressbronn |
| Mittelmeer (IT) | PanatEra Marine | Oceanvolt, ePropulsion | La Spezia |
| Frankreich (Atlantik) | Breizh Marine Elec | Torqeedo, Victron | La Rochelle |
| Niederlande | Mastervolt Servicedesk | Mastervolt, Bellmarine | Amsterdam |
| Schweden | Marinelektro AB | Oceanvolt, Torqeedo | Göteborg |
| Kroatien | E-Marine Adriatic | ePropulsion, Victron | Split |
| Griechenland | Hellas Marine Tech | Torqeedo, Victron | Athen |
| Karibik (BVI) | Caribbean Marine Elec | Torqeedo | Road Town |
| Mallorca | Astilleros de Mallorca E-Team | Diverse | Palma |

### 21.3 Ersatzteil-Verfügbarkeit

| Komponente | Lieferzeit (Europa) | Notfall-Workaround |
|-----------|-------------------|-------------------|
| E-Motor (komplett) | 2–6 Wochen | Kein Workaround — Segeln/Schleppen |
| Controller | 1–4 Wochen | Kein Workaround |
| Batteriepack | 1–3 Wochen | Alternativbatterie (gleiche Spannung) |
| BMS-Platine | 1–2 Wochen | Batterie direkt (ohne Schutz — NUR Notfall!) |
| Ladegerät | 1–2 Wochen | Alternatives Ladegerät (48 V LiFePO4-Profil) |
| Sicherung (ANL/MEGA) | Sofort (Schiffsausrüster) | — |
| DC-Kabel | Sofort (Schiffsausrüster) | — |
| MPPT-Regler | 1–2 Wochen | Direkt an Batterie (bei < 60 V Panelspannung) |
| Propeller | 1–4 Wochen | Notpropeller (wenn vorhanden) |

**Empfehlung:** Auf Langfahrt folgende Ersatzteile mitführen:
- 2 × ANL-Sicherung (passende Größe)
- 1 × Satz Crimpverbinder (35–70 mm²)
- Isolierband + Schrumpfschlauch
- Multimeter
- BMS-Handbuch (Fehlercodes)
- Controller-Handbuch (Fehlercodes + Reset-Anleitung)
- Kabel (1 m in passender Stärke)

---

*Ende der Wissensdatei 18_11 — Elektro- und Hybridantrieb*
*AYDI Maritime Knowledge Base v2.0 — Stand April 2026*