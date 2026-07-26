# 08.02 — Bullaugen und Seitenfenster im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 08.02** — Kategorie 8: Fenster, Luken und Öffnungen
> **Confidence-Quelle:** measured (Hersteller-TDS, ISO-Normen), documented (Hersteller-Kataloge, Surveyor-Erfahrungen), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-25

---

## Inhaltsverzeichnis

1. [Einführung & Regulatorischer Rahmen](#1-einführung--regulatorischer-rahmen)
2. [Zukunftstechnologien](#2-zukunftstechnologien)
3. [Best Practices nach Revier](#3-best-practices-nach-revier)
4. [Regional Sourcing](#4-regional-sourcing)
5. [Zweck dieser Wissensdatei](#5-zweck-dieser-wissensdatei)
6. [Pydantic-Modelle](#6-pydantic-modelle)
7. [Grundlagen](#7-grundlagen)
8. [Hersteller — Vollständige Übersicht](#8-hersteller--vollständige-übersicht)
9. [Anlagen-spezifische Zuordnung](#9-anlagen-spezifische-zuordnung)

---

## 1. Einführung & Regulatorischer Rahmen

### 1.1 Begriffsdefinition und Abgrenzung

**Bullaugen** (engl. portholes, portlights) und **Seitenfenster** (engl. side windows, hull windows) sind Öffnungen in Rumpf- oder Aufbauwandungen, die primär der Belichtung und sekundär der Belüftung dienen. Die Begriffe werden im deutschen Yachtbau wie folgt unterschieden:

| Begriff | Definition | Typische Position |
|---------|-----------|-------------------|
| **Bullauge** (Portlight) | Runde oder ovale Öffnung mit Rahmen und Scheibe, öffnend oder fest | Rumpfseite, Aufbauwand |
| **Seitenfenster** (Side Window) | Rechteckige oder trapezförmige Scheibe, meist fest verklebt | Aufbauwand, Deckshaus |
| **Kabinenfenster** (Cabin Window) | Jedes Fenster, das einen Innenraum belichtet | Überall |
| **Festfenster** (Fixed Light/Deadlight) | Nicht öffnende Scheibe, verklebt oder verschraubt | Rumpfseite, Aufbauwand |
| **Öffnungsbullauge** (Opening Portlight) | Mit Scharnier und Verriegelung zum Öffnen | Aufbauwand, Kajütseite |
| **Deadlight** (Sturmblende) | Massive Metallblende über dem Bullauge für schweres Wetter | Rumpf-Bullaugen, Offshore |

### 1.2 Historischer Kontext

Das Bullauge stammt aus der Handelsschifffahrt des 17. Jahrhunderts. Ursprünglich als "bull's eye" (Ochsenauge) bezeichnet — runde Glasscheibe in einem Bronzerahmen, mit massivem Sturmdeckel (Deadlight) zum Verschließen bei Seegang. Die runde Form war strukturell optimal: gleichmäßige Spannungsverteilung im Rumpfausschnitt ohne Spannungskonzentration an Ecken.

Im modernen Yachtbau hat sich die Formenvielfalt erweitert:
- **Rund**: Traditionell, strukturell optimal, nautisch-klassisch
- **Oval/Elliptisch**: Mehr Licht bei ähnlich guter Spannungsverteilung
- **Rechteckig mit Radien**: Moderner Look, größere Lichtfläche, höhere Spannungskonzentration an Ecken
- **Trapezförmig**: Angepasst an Aufbauprofil moderner Yachten

### 1.3 ISO 12216 — Fenster, Bullaugen, Luken, Deadlights und Türen

Die **ISO 12216:2020** ("Small craft — Windows, portlights, hatches, deadlights and doors — Strength and watertightness requirements") ist die zentrale Norm für alle Öffnungen im Rumpf und Aufbau von Sportbooten bis 24m.

#### 1.3.1 Anwendungsbereich

- Gilt für alle Boote ≤24m Rumpflänge nach der EU-Richtlinie für Sportboote 2013/53/EU
- Deckt ab: Fenster, Bullaugen (öffnend und fest), Luken, Deadlights, Türen
- Referenziert Designkategorien A–D gemäß RCD

#### 1.3.2 Druckbelastungsberechnung

Die Norm definiert die **Bemessungsdrücke** (design pressures) für Fenster und Bullaugen basierend auf:

```
P_design = k_DC × k_AR × k_LOC × P_base

wobei:
  k_DC  = Designkategorie-Faktor (A=1.0, B=0.8, C=0.5, D=0.25)
  k_AR  = Seitenverhältnis-Faktor der Scheibe
  k_LOC = Positionsfaktor (Höhe über Wasserlinie, Bug/Heck/Seite)
  P_base = Basis-Bemessungsdruck abhängig von Bootslänge und -geschwindigkeit
```

> ⚠️ **ZU PRÜFEN (Audit):** k_DC hier (C=0.5, D=0.25) widerspricht der kDC-Tabelle in §10.1.1 (Rumpf: C=0.60, D=0.40) — last-/druckrelevanter Faktor. Die analoge kDC-Reihe aus ISO 12215-5 (A=1.0 / B=0.8 / C=0.6 / D=0.4) stützt die Tabellenwerte, ist aber für ISO 12216 nicht zweifelsfrei belegt. Vor Nutzung gegen ISO 12216 verifizieren.

**Positionsfaktoren k_LOC nach ISO 12216:**

| Position | k_LOC | Bemerkung |
|----------|-------|-----------|
| Rumpfseite, unteres Drittel Freibord | 1.0 | Höchste Belastung |
| Rumpfseite, oberes Drittel Freibord | 0.8 | |
| Aufbauwand, unteres Drittel | 0.6 | |
| Aufbauwand, oberes Drittel | 0.4 | |
| Decksfenster (nach oben) | 0.5 | Tritt-/Schlagbelastung |
| Heckfenster | 0.5 | Geringere Wellenbelastung |
| Bugfenster (vorlich 25% LWL) | 1.2 | Slamming-Zuschlag |

#### 1.3.3 Mindesthöhe über Wasserlinie

Die ISO 12216 definiert **Mindesthöhen** für öffnende Bullaugen über der Konstruktionswasserlinie (DWL):

| Designkategorie | Mindesthöhe öffnend (mm) | Mindesthöhe fest (mm) |
|-----------------|--------------------------|------------------------|
| A (Ozean) | 500 | 300 |
| B (Offshore) | 400 | 250 |
| C (Küste) | 300 | 200 |
| D (Geschützt) | 200 | 150 |

**Hinweis:** Diese Werte gelten für Seitenfenster im Rumpf. Aufbauwand-Fenster haben geringere Anforderungen, da sie weiter über der Wasserlinie liegen.

#### 1.3.4 Scheibendicke-Berechnung nach ISO 12216

Für **Acrylglas (PMMA)** und **Polycarbonat (PC)** gilt vereinfacht:

```
t_min = k × a × √(P_design / σ_allow)

wobei:
  t_min    = Mindestdicke in mm
  k        = Formfaktor (abhängig von Seitenverhältnis b/a)
  a        = kurze Seite der Scheibe in mm
  P_design = Bemessungsdruck in kPa
  σ_allow  = zulässige Spannung des Materials in MPa
```

**Zulässige Spannungen σ_allow nach ISO 12216:**

| Material | σ_allow (MPa) | Bemerkung |
|----------|---------------|-----------|
| PMMA (Acrylglas) | 14.0 | Crazing-empfindlich |
| PC (Polycarbonat) | 20.0 | Kratzer-empfindlich |
| Einscheibensicherheitsglas (ESG) | 35.0 | Thermisch vorgespannt |
| Verbundsicherheitsglas (VSG) | 28.0 | Laminiert, splittergebunden |

> ⚠️ **ZU PRÜFEN (Audit):** Zulässige Spannungen hier (PMMA 14.0 MPa, ESG 35.0 MPa) widersprechen §10.2 (PMMA σ_zul 15 MPa, ESG 40 MPa) — festigkeits-/dickenrelevant, beide als belastbar dargestellt. (Die daraus abgeleiteten empfohlenen Dicken stimmen zufällig überein.) σ_allow-Werte gegen ISO 12216 Annex verifizieren.

**Typische Mindestdicken für Yacht-Bullaugen (Praxiswerte):**

| Scheibendurchmesser/-breite (mm) | PMMA (mm) | PC (mm) | ESG (mm) | Kat. A | Kat. C |
|-----------------------------------|-----------|---------|----------|--------|--------|
| 150 (rundes Bullauge) | 6 | 5 | 4 | 8 | 6 |
| 200 | 8 | 6 | 5 | 10 | 6 |
| 300 | 10 | 8 | 6 | 12 | 8 |
| 400 | 12 | 10 | 8 | 15 | 10 |
| 500 | 15 | 12 | 8 | 18 | 12 |
| 600+ (Salonfenster) | 18+ | 15+ | 10+ | 20+ | 15+ |

> Confidence: `estimated — unverifiziert` (ISO 12216:2020, Annex A — σ_allow-Werte widersprüchlich zu §10.2, siehe Audit-Hinweis)

#### 1.3.5 Prüfanforderungen

Bullaugen und Fenster müssen folgende Tests bestehen:

1. **Wasserdichtigkeitsprüfung**: Schlauchprüfung 60 Sekunden bei definiertem Druck, kein Wasser darf eindringen
2. **Festigkeitsprüfung**: 1.5 × Bemessungsdruck ohne bleibende Verformung
3. **Bruchprüfung**: 3.5 × Bemessungsdruck ohne Versagen der Scheibe (PMMA/PC) oder 4.0 × für Glas
4. **Mechanische Belastung des Rahmens**: Scharnier, Verriegelung, Rahmen müssen den Drücken standhalten
5. **Dauerbelastung (optional)**: 10.000 Öffnungs-/Schließzyklen für Scharnier und Verriegelung

### 1.4 ISO 21005 — Festverglaste Fenster

Die **ISO 21005:2018** ("Small craft — Windows, portlights and hatches — Structural glazing") behandelt spezifisch **fest verklebte Fenster** ohne mechanische Befestigung (Structural Glazing):

> ⚠️ **ZU PRÜFEN (Audit):** Normtitel/Scope falsch — ISO 21005:2018 heißt laut ISO "Ships and marine technology — Thermally toughened safety glass panes for windows and side scuttles" (ESG-Scheiben-Norm), NICHT "Structural glazing". Für großflächige Klebeverglasung ist eher ISO 11336 (Large yachts — glazed openings) einschlägig. Normnummer und die daran hängenden Klebstoff-/Prüfangaben vor Verwendung verifizieren.

- **Klebstoffanforderungen**: Nur zugelassene marine Klebstoffe (typisch: Sika, 3M, Dow)
- **Klebflächenbreite**: Mindestens 15mm, typisch 20–30mm für Yachtfenster
- **Alterungsprüfung**: 3.000 Stunden UV-Beständigkeit, 1.000 Stunden Salzsprühnebel
- **Kompatibilität**: Klebstoff muss mit Rahmen UND Scheibenmaterial kompatibel sein

**Typische Klebstoffe für Structural Glazing im Yachtbau:**

| Produkt | Hersteller | Typ | Scherfestigkeit (MPa) | Einsatz |
|---------|-----------|-----|----------------------|---------|
| Sikaflex-295 UV | Sika | 1K-PU | 2.0 | Standard, bew ährt |
| Sikaflex-296 | Sika | 1K-PU | 2.5 | Hochfest, dicke Scheiben |
| Simson ISR 70-03 | Bostik | 2K-PU | 4.0 | Superyacht-Standard |
| 3M 550 FC | 3M | 1K-PU | 2.2 | Schnelle Aushärtung |
| Dow 795 | Dow | Silikon | 1.4 | Glas auf Aluminium |

> Confidence: `estimated — unverifiziert` (ISO 21005:2018 — Normtitel/Scope widersprüchlich, siehe Audit-Hinweis; Hersteller-TDS)

### 1.5 ABYC H-2 — Ventilation (USA)

Die **ABYC H-2** betrifft die Belüftung von Wohn- und Maschinenräumen. Öffnende Bullaugen tragen zur **natürlichen Ventilation** bei:

> ⚠️ **ZU PRÜFEN (Audit):** ABYC H-2 heißt "Ventilation of Boats Using Gasoline" und regelt die Lüftung benzinbetriebener Motoren-/Kraftstoffräume, nicht die Belüftung von Wohnräumen. Die Scope-Zuordnung "Wohnräume" und der 1-%-Wohnraum-Richtwert sind dieser Norm nicht zuzuordnen — Quelle für den Wohnraum-Wert vor Verwendung klären.

- Mindest-Ventilationsquerschnitt für Wohnräume: Empfohlen ≥1% der Bodenfläche des Raums
- Gegenüberliegende Öffnungen (Querlüftung) verdoppeln die Effektivität
- Maschinenraum: Bullaugen zählen NICHT als primäre Belüftung (Brand-/Explosionsgefahr)
- Propangas-Räume: Öffnende Bullaugen im Gaslocker sind unzulässig (Funkengefahr)

### 1.6 CE/RCD-Anforderungen

Die **EU Recreational Craft Directive 2013/53/EU** verlangt:

- CE-Konformitätsnachweis für alle strukturellen Öffnungen (Fenster, Bullaugen, Luken)
- Hersteller muss Designkategorie auf dem Typenschild angeben
- Bullaugen müssen der deklarierten Kategorie entsprechen
- Nachrüstung: Eigner ist verantwortlich für normgerechten Einbau

### 1.7 Klassifikationsgesellschaften

Für Yachten >24m oder gewerbliche Fahrt gelten zusätzlich die Regeln der Klassifikationsgesellschaften:

| Gesellschaft | Regelwerk | Besonderheiten |
|-------------|-----------|----------------|
| **Lloyd's Register** (LR) | SSC Rules | Detaillierte Scheibendicken-Berechnung, Rahmenscantlings |
| **Bureau Veritas** (BV) | NR 500/NR 217 | Stoßbelastungsfaktoren für Hochgeschwindigkeitsyachten |
| **DNV** | Pt.3 Ch.3 | Strengste Anforderungen an Bugfenster |
| **RINA** | Rules for Yachts | Italienischer Standard, weit verbreitet in Superyacht-Bau |
| **ABS** | Guide for Building and Classing Yachts | US-Standard, SOLAS-kompatibel für Charteryachten |

**Zusätzliche Anforderungen ab 24m / gewerblich:**
- Deadlights (Sturmblenden) vorgeschrieben für alle Rumpf-Bullaugen unterhalb Festigkeitsdeck
- Feuerwiderstand: Fenster in Schotten zwischen Feuerabschnitten müssen A-0 oder A-15 sein
- Fluchtweg: Mindestens ein öffnendes Fenster pro Kabine als Notausgang (min. 400×520mm lichte Weite)
- Rahmen: Geschweißte Aluminium- oder Stahlrahmen, keine Schraubverbindungen in Fensterrahmen

> Confidence: `measured` (ISO 12216:2020, ISO 21005:2018, ABYC H-2), `documented` (Klassifikationsregeln)

---

## 2. Zukunftstechnologien

### 2.1 Elektrochromes Glas (Smart Glass)

**Funktionsprinzip:** Elektrisch schaltbare Verglasung, die per Spannung (1–5V DC) zwischen transparent und dunkel wechselt. Wolfram(VI)-oxid-Beschichtung auf der Glasinnenseite reduziert die Lichttransmission von ~65% auf ~5%.

**Hersteller für marine Anwendung:**

| Hersteller | Produkt | Schaltzeit (s) | T_vis hell (%) | T_vis dunkel (%) | Preis (EUR/m²) |
|-----------|---------|----------------|----------------|-------------------|-----------------|
| **View Inc.** | View Dynamic Glass | 8–12 | 62 | 1 | 800–1.200 |
| **SageGlass** (Saint-Gobain) | SageGlass Marine | 10–15 | 60 | 3 | 700–1.000 |
| **Gentex** (USA) | dimmable Marine | 3–5 | 50 | 5 | 1.500+ |
| **Gauzy** (Israel) | LCG Marine | <1 (PDLC) | 75 | <1 (opak) | 600–900 |

**Vorteile im Yachtbau:**
- Kein Vorhang/Rollo nötig — reduziert Feuchtigkeit hinter Textilien
- Blendschutz stufenlos per App steuerbar
- Wärmedämmung im dunklen Zustand (g-Wert sinkt von 0.45 auf 0.08)
- Privatsphäre ohne Jalousien

**Nachteile/Risiken:**
- Stromversorgung nötig — bei Ausfall bleibt Scheibe im letzten Zustand
- Salzwasser-Korrosion an den elektrischen Anschlüssen
- Keine Erfahrungswerte >5 Jahre im marinen Umfeld
- Reparatur = Kompletttausch der Scheibe (keine Feldreperatur der Beschichtung)
- Kosten: 5–10× konventionelles Isolierglas

> Confidence: `estimated` (Technologie etabliert im Bauwesen, marine Langzeiterfahrung fehlt)

### 2.2 Selbsttönendes Glas (Photochrom)

Automatisch verdunkelnde Scheiben durch UV-Licht — ähnlich wie Brillengläser. Im Yachtbau noch experimentell, da marine UV-Beständigkeit der photochromen Pigmente nicht ausreichend dokumentiert ist. Lebensdauer an Bord geschätzt: 3–5 Jahre bis zur Ermüdung der Pigmente.

### 2.3 Beheizte Scheiben

**Anwendung:** Anti-Beschlag im Winter/Übergangszeit, Eisfreihalten in Hochbreiten.

- **Drahtbeheizt**: Unsichtbare Heizdrahtmatrix in Verbundglas, 12V/24V, 50–150W/m²
- **Beschichtungsbeheizt**: Transparente Metalloxid-Beschichtung (ITO), gleichmäßigere Wärmeverteilung
- Hersteller: **Speich** (Italien), **Trend Marine** (UK), **Hempel** (für Superyachten)
- Kosten: 300–600 EUR/m² Aufpreis auf konventionelle Verglasung

### 2.4 Transparente Solarzellen

Integration von organischen Solarzellen (OPV) in die Fensterfläche. Aktuelle Effizienz ~5%, also ~50 Wp/m² bei ~50% Transparenz. Im Yachtbau als Demonstrator bei Superyachten (Arcadia Yachts, Silent Yachts), aber noch kein Serienprodukt für Bullaugen.

### 2.5 Aerogelbasierte Isolierung

**Aerogel-Spacer** zwischen Doppelscheiben statt Luftfüllung: U-Wert bis 0.5 W/(m²·K) möglich (vs. 2.8 für Einscheibe, 1.4 für konventionelle Doppelverglasung). Derzeit in der Entwicklung für superyacht-Festfenster.

> Confidence: `estimated` (Technologien in Entwicklung, noch keine ISO-Zertifizierung für marine Anwendung)

---

## 3. Best Practices nach Revier

### 3.1 Mittelmeer (Sommer/Ganzjahr)

**Hauptprobleme:** UV-Belastung (UV-Index 9–11), extreme Hitze auf dunklen Rahmen (>80°C), Blendung

**Empfehlungen:**
- Getönte Scheiben (Bronze/Grau, 50–65% Lichttransmission) für Salon und Eignerkajüte
- PMMA mit UV-Schutzschicht oder tempered glass mit Low-E-Beschichtung
- Helle (silberne/weiße) Rahmenfarben — schwarze Rahmen erreichen >90°C
- Hinterlüftete Rahmen verhindern Wärmestau in der Klebfuge
- Innenrollos oder Außen-Sonnenschutz unbedingt empfohlen (Kabinen-Temperatur sonst >45°C)
- Deadlights nicht nötig für Küstenfahrt (CE Kat. C/D)
- Insektenschutz (Fliegengitter) unverzichtbar — Mücken in Marinas allgegenwärtig

**Bevorzugte Hersteller:** Goiot (französische Werften), Lewmar (britische Werften), Vetus (holländische Werften)

### 3.2 Nordeuropa / Ostsee / Nordsee

**Hauptprobleme:** Kälte (bis -20°C), Eisbildung, Kondensation, Seegang Beaufort 7–9

**Empfehlungen:**
- Doppelverglasung oder beheizte Scheiben für Langfahrt
- EPDM-Dichtungen (nicht Neopren — wird unter -10°C spröde)
- Deadlights für CE Kat. A/B Boote
- Klare Scheiben (hohe Lichttransmission >85%) — kurze Tage, wenig Sonne
- Aluminium-Rahmen eloxiert oder pulverbeschichtet gegen Salz
- Anti-Beschlag-Beschichtung innen empfohlen

**Bevorzugte Hersteller:** Lewmar (robuste Standardware), Gebo (deutsch, Qualität), Vetus (NL)

### 3.3 Tropen / Blauwasser

**Hauptprobleme:** Extreme UV, Hitze, heftige Squalls, Ferndiagnose/Ersatzteilbeschaffung

**Empfehlungen:**
- Polycarbonat (PC) statt PMMA — schlagresistenter bei fliegendem Gegenstand
- Deadlights vorgeschrieben für Kat. A, auch für alle Rumpf-Bullaugen empfohlen
- Bronzerahmen (New Found Metals) — wartungsfrei, kein Galvanik-Problem
- Ersatzdichtungs-Set an Bord (EPDM-Meterware + Vulkanisierkleber)
- Insektengitter mit feinerem Mesh (No-See-Ums / Sandmücken: ≤0.6mm Maschenweite)
- Solartönung empfohlen (reduziert UV-Eintrag um 95%)

**Bevorzugte Hersteller:** New Found Metals (Bronze, Qualität), Beckson (günstig, überall erhältlich), Bomar (Aluminium, US-Standard)

### 3.4 Hochbreiten / Arktis

**Hauptprobleme:** Extreme Kälte (-40°C), Eisschlag, Schneelast, Polarfinsternis

**Empfehlungen:**
- Nur ESG oder VSG — PMMA bricht bei Schlagbelastung unter -20°C
- Silikon-Dichtungen (funktionsfähig bis -60°C) statt EPDM
- Beheizte Scheiben obligatorisch
- Deadlights aus Stahl (nicht Aluminium — Kerbschlagzähigkeit bei Kälte)
- Innere Isolierscheibe (Doppelverglasung Pflicht)

> Confidence: `documented` (Erfahrungsberichte von Blauwasserseglern, Eigner-Foren, Surveyor-Konsens)

---

## 4. Regional Sourcing

### 4.1 Europa

| Land | Anbieter | Typ | Lieferzeit | Bemerkung |
|------|---------|-----|------------|-----------|
| UK | **Lewmar** (Havant) | OEM + Retail | 2–4 Wochen | Weltmarktführer |
| UK | **Trend Marine** (Romsey) | Custom + OEM | 4–8 Wochen | Superyacht-Spezialist |
| UK | **Manship** (Cowes) | Custom | 6–10 Wochen | Klassische Bronze |
| FR | **Goiot** (Nantes) | OEM | 2–6 Wochen | Bénéteau/Jeanneau-Zulieferer |
| FR | **Plastimo** (Lorient) | Retail | 1–2 Wochen | Breit verfügbar |
| NL | **Vetus** (Schiedam) | OEM + Retail | 1–3 Wochen | Starkes Händlernetz |
| DE | **Gebo** (alt, jetzt Lewmar) | Legacy | NLA | Ersatzteile über Lewmar |
| IT | **Osculati** (Mailand) | Retail/Budget | 1–2 Wochen | SVB/Compass-Vertrieb |
| SE | **Rutgerson** (Lysekil) | OEM (Segelyachten) | 3–5 Wochen | Hallberg-Rassy-Zulieferer |

### 4.2 Nordamerika

| Anbieter | Standort | Typ | Bemerkung |
|---------|---------|-----|-----------|
| **Bomar** | Charlestown, NH | OEM + Retail | Standard US-Markt |
| **Beckson** | Bridgeport, CT | Budget Retail | Lexan, günstig, UV-problematisch |
| **New Found Metals** | Port Townsend, WA | Premium Custom | Bronze, handgefertigt, Wartezeit 8–12 Wochen |
| **Freeman Marine** | Gold Beach, OR | Superyacht Custom | Watertight doors & windows, SOLAS-kompatibel |
| **ABI Industries** | Tacoma, WA | OEM | Aluminium, mittleres Preissegment |

### 4.3 Asien / Rest der Welt

| Anbieter | Standort | Typ | Bemerkung |
|---------|---------|-----|-----------|
| **Boman** (Taiwan) | Taipei | OEM | Flush-mount, gute Qualität |
| **Aritex** (China) | Ningbo | OEM/Budget | Superyacht-Zulieferer, CE-zertifiziert |
| **Sealux** (Taiwan) | Kaohsiung | OEM/Retail | 316L-Edelstahl-Bullaugen |

> Confidence: `documented` (Händler-Websites, Werftlisten, Marine-Fachhandel)

---

## 5. Zweck dieser Wissensdatei

Diese Wissensdatei dient dem AYDI-Analysemotor als Referenz für:

1. **Zustandsbewertung** von Bullaugen und Seitenfenstern (Pipeline A + B)
   - Visuelle Erkennung von Crazing, Vergilbung, Dichtungsversagen
   - Strukturelle Bewertung von Rahmen und Befestigung
   - Compliance-Prüfung gegen ISO 12216/21005

2. **Designbewertung** bei Neubauprojekten (Pipeline A)
   - Positionierung und Dimensionierung
   - Material- und Herstellerauswahl
   - Normkonformität der gewählten Lösung

3. **Kostenschätzung** (Pipeline A)
   - Neueinbau und Austausch
   - Material- und Arbeitskosten nach Bootslänge und Typ

4. **Wartungsplanung** (Pipeline C)
   - Intervalle für Dichtungswechsel
   - Lebensdauer von Scheibenmaterialien
   - Typische Schadensbilder und deren Ursachen

**Integration in AYDI-Module:**
- `materials` → Scheiben- und Rahmenmaterial-Bewertung
- `compliance` → ISO 12216 / CE-Konformität
- `production` → Herstellungsaufwand für Rumpfausschnitte
- `cost` → Parametrische Kostenschätzung
- `ergonomics` → Licht- und Belüftungsanalyse
- `emotional` → Ästhetik, Sichtlinien, Raumgefühl

---

## 6. Pydantic-Modelle

```python
"""
AYDI Wissensdatei 08.02 — Bullaugen und Seitenfenster
Pydantic v2 Modelle für Portlight/Side Window Assessment
"""

from enum import Enum
from typing import Optional, List
from pydantic import BaseModel, Field


# ── Enums ──────────────────────────────────────────────────

class PortlightType(str, Enum):
    """Art des Bullauges/Fensters."""
    OPENING_ROUND = "opening_round"
    OPENING_RECTANGULAR = "opening_rectangular"
    OPENING_OVAL = "opening_oval"
    FIXED_ROUND = "fixed_round"
    FIXED_RECTANGULAR = "fixed_rectangular"
    FIXED_OVAL = "fixed_oval"
    FLUSH_FIXED = "flush_fixed"
    FLUSH_OPENING = "flush_opening"
    STRUCTURAL_GLAZING = "structural_glazing"
    TRADITIONAL_PORTHOLE = "traditional_porthole"


class PortlightShape(str, Enum):
    """Geometrische Form."""
    ROUND = "round"
    OVAL = "oval"
    RECTANGULAR = "rectangular"
    RECTANGULAR_RADIUSED = "rectangular_radiused"
    TRAPEZOIDAL = "trapezoidal"
    CUSTOM = "custom"


class FrameMaterial(str, Enum):
    """Rahmenmaterial."""
    CAST_ALUMINUM = "cast_aluminum"
    EXTRUDED_ALUMINUM = "extruded_aluminum"
    BRONZE = "bronze"
    STAINLESS_316L = "stainless_316l"
    STAINLESS_304 = "stainless_304"
    COMPOSITE_GRP = "composite_grp"
    PLASTIC_ABS = "plastic_abs"
    PLASTIC_NYLON = "plastic_nylon"
    STEEL_PAINTED = "steel_painted"


class LensMaterial(str, Enum):
    """Scheibenmaterial."""
    PMMA_ACRYLIC = "pmma_acrylic"
    POLYCARBONATE_PC = "polycarbonate_pc"
    TEMPERED_GLASS_ESG = "tempered_glass_esg"
    LAMINATED_GLASS_VSG = "laminated_glass_vsg"
    FLOAT_GLASS = "float_glass"
    PMMA_TINTED = "pmma_tinted"
    PC_TINTED = "pc_tinted"
    GLASS_LOW_E = "glass_low_e"
    GLASS_TINTED = "glass_tinted"


class MountingType(str, Enum):
    """Einbauart."""
    SPIGOT = "spigot"
    FLANGE_EXTERNAL = "flange_external"
    FLANGE_INTERNAL = "flange_internal"
    FLANGE_BOTH = "flange_both"
    FLUSH_BONDED = "flush_bonded"
    FLUSH_MECHANICAL = "flush_mechanical"
    STRUCTURAL_GLAZING = "structural_glazing"


class GasketMaterial(str, Enum):
    """Dichtungsmaterial."""
    EPDM = "epdm"
    NEOPRENE = "neoprene"
    SILICONE = "silicone"
    NITRILE = "nitrile"
    POLYURETHANE = "polyurethane"
    BUTYL = "butyl"


class PortlightLocation(str, Enum):
    """Einbauort an Bord."""
    HULL_SIDE_FORWARD = "hull_side_forward"
    HULL_SIDE_MIDSHIP = "hull_side_midship"
    HULL_SIDE_AFT = "hull_side_aft"
    CABIN_TRUNK_SIDE = "cabin_trunk_side"
    CABIN_TRUNK_FORWARD = "cabin_trunk_forward"
    CABIN_TRUNK_AFT = "cabin_trunk_aft"
    DECKHOUSE_SIDE = "deckhouse_side"
    COCKPIT_SIDE = "cockpit_side"
    TRANSOM = "transom"
    ENGINE_ROOM = "engine_room"
    HEAD_COMPARTMENT = "head_compartment"
    GALLEY = "galley"


class ConditionGrade(str, Enum):
    """Zustandsbewertung."""
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"
    FAILED = "failed"


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


class CEDesignCategory(str, Enum):
    """CE-Designkategorie nach RCD 2013/53/EU."""
    A_OCEAN = "A"
    B_OFFSHORE = "B"
    C_INSHORE = "C"
    D_SHELTERED = "D"


# ── Modelle ────────────────────────────────────────────────

class PortlightSpec(BaseModel):
    """Spezifikation eines einzelnen Bullauges oder Seitenfensters."""
    model_config = {"from_attributes": True}

    # Identifikation
    manufacturer: str = Field(..., description="Hersteller")
    model_name: str = Field(..., description="Modellbezeichnung, z.B. 'New Standard Portlight Size 4'")
    part_number: Optional[str] = Field(None, description="Hersteller-Artikelnummer")

    # Typ und Form
    portlight_type: PortlightType
    shape: PortlightShape
    is_opening: bool = Field(..., description="True = öffnend, False = fest")
    has_deadlight: bool = Field(False, description="Sturmblende vorhanden")
    has_mosquito_screen: bool = Field(False, description="Insektengitter integriert")

    # Abmessungen (mm)
    outer_width_mm: float = Field(..., description="Äußere Breite (oder Durchmesser bei rund)")
    outer_height_mm: float = Field(..., description="Äußere Höhe (= Breite bei rund)")
    cutout_width_mm: float = Field(..., description="Ausschnitt-Breite im Rumpf/Aufbau")
    cutout_height_mm: float = Field(..., description="Ausschnitt-Höhe im Rumpf/Aufbau")
    clear_opening_width_mm: Optional[float] = Field(None, description="Lichte Weite für Belüftung (nur öffnend)")
    clear_opening_height_mm: Optional[float] = Field(None, description="Lichte Höhe für Belüftung (nur öffnend)")
    corner_radius_mm: Optional[float] = Field(None, description="Eckradius bei rechteckig (0 = scharfe Ecke)")
    max_panel_thickness_mm: float = Field(..., description="Max. Wandstärke für Einbau")
    min_panel_thickness_mm: Optional[float] = Field(None, description="Min. Wandstärke für Einbau")
    frame_depth_mm: Optional[float] = Field(None, description="Rahmen-Tiefe (Spigot-Länge)")

    # Materialien
    frame_material: FrameMaterial
    lens_material: LensMaterial
    lens_thickness_mm: float = Field(..., description="Scheibendicke")
    lens_tint: Optional[str] = Field(None, description="Tönung: clear, smoke, bronze, grey")
    gasket_material: GasketMaterial = Field(GasketMaterial.EPDM)

    # Montage
    mounting_type: MountingType
    fastener_count: Optional[int] = Field(None, description="Anzahl Befestigungsschrauben")
    fastener_size: Optional[str] = Field(None, description="Schraubengröße, z.B. 'M5', '#10-24'")

    # Normen
    ce_category_max: Optional[CEDesignCategory] = Field(None, description="Max. CE-Kategorie, für die zugelassen")
    iso_12216_compliant: bool = Field(False)
    iso_21005_compliant: bool = Field(False)

    # Gewicht und Preis
    weight_kg: Optional[float] = Field(None, description="Gewicht komplett mit Rahmen")
    price_eur: Optional[float] = Field(None, description="Listenpreis EUR inkl. MwSt.")
    price_usd: Optional[float] = Field(None, description="Listenpreis USD")

    # Öffnungsmechanismus (nur öffnend)
    opening_angle_deg: Optional[float] = Field(None, description="Max. Öffnungswinkel in Grad")
    hinge_type: Optional[str] = Field(None, description="Scharniertyp: top, bottom, side, pivot")
    latch_type: Optional[str] = Field(None, description="Verriegelung: dog, handle, cam, friction")
    stay_type: Optional[str] = Field(None, description="Aussteller: friction, detent, gas_spring")


class PortlightCondition(BaseModel):
    """Zustandsbewertung eines einzelnen Bullauges (Pipeline A+B)."""
    model_config = {"from_attributes": True}

    # Identifikation
    portlight_id: str = Field(..., description="Eindeutige ID, z.B. 'PL-SB-01' (portlight starboard 01)")
    location: PortlightLocation
    location_detail: Optional[str] = Field(None, description="Detailbeschreibung, z.B. 'Vorschiffskajüte Steuerbord'")
    spec: Optional[PortlightSpec] = Field(None, description="Referenz auf Spezifikation, falls bekannt")

    # Zustandsparameter
    overall_grade: ConditionGrade
    overall_score: int = Field(..., ge=0, le=100, description="Gesamtbewertung 0-100")

    # Scheibe
    lens_grade: ConditionGrade
    lens_score: int = Field(..., ge=0, le=100)
    lens_crazing: bool = Field(False, description="Haarrisse im Acryl (Crazing)")
    lens_crazing_severity: Optional[str] = Field(None, description="none/light/moderate/severe")
    lens_yellowing_pct: Optional[float] = Field(None, ge=0, le=100, description="Vergilbungsgrad 0-100%")
    lens_scratches: Optional[str] = Field(None, description="none/light/moderate/deep")
    lens_uv_damage: Optional[str] = Field(None, description="none/surface/structural")
    lens_clarity_pct: Optional[float] = Field(None, ge=0, le=100, description="Transparenz 0-100%")

    # Rahmen
    frame_grade: ConditionGrade
    frame_score: int = Field(..., ge=0, le=100)
    frame_corrosion: Optional[str] = Field(None, description="none/surface/pitting/structural")
    frame_anodizing_intact: Optional[bool] = Field(None, description="Eloxierung intakt (Aluminium)")
    frame_paint_condition: Optional[str] = Field(None, description="none/intact/chalking/peeling/bubbling")
    frame_distortion: bool = Field(False, description="Rahmenverformung erkennbar")

    # Dichtung
    gasket_grade: ConditionGrade
    gasket_score: int = Field(..., ge=0, le=100)
    gasket_hardened: bool = Field(False, description="Dichtung verhärtet")
    gasket_compressed: bool = Field(False, description="Dichtung dauerhaft verformt (Compression Set)")
    gasket_cracked: bool = Field(False, description="Dichtung gerissen")
    gasket_missing_sections: bool = Field(False, description="Dichtung teilweise fehlend")
    gasket_age_years: Optional[int] = Field(None, description="Geschätztes Alter der Dichtung")
    water_ingress_detected: bool = Field(False, description="Wassereinbruch festgestellt")

    # Mechanik (nur öffnend)
    hinge_condition: Optional[str] = Field(None, description="ok/stiff/loose/broken")
    latch_condition: Optional[str] = Field(None, description="ok/stiff/worn/broken")
    stay_condition: Optional[str] = Field(None, description="ok/weak/broken/missing")
    opening_effort: Optional[str] = Field(None, description="easy/moderate/difficult/seized")

    # Einbau
    bedding_condition: Optional[str] = Field(None, description="intact/cracked/missing/leaking")
    mounting_fasteners: Optional[str] = Field(None, description="ok/loose/corroded/missing")

    # Compliance
    height_above_dwl_mm: Optional[float] = Field(None, description="Höhe Unterkante über DWL")
    meets_iso_12216: Optional[bool] = Field(None)
    ce_category_required: Optional[CEDesignCategory] = Field(None)

    # Empfehlungen
    action_required: str = Field(..., description="none/monitor/service/repair/replace")
    estimated_repair_cost_eur: Optional[float] = Field(None)
    estimated_replacement_cost_eur: Optional[float] = Field(None)
    urgency: str = Field("routine", description="routine/scheduled/urgent/critical")

    # Confidence
    confidence: ConfidenceLevel
    confidence_detail: Optional[str] = Field(None, description="Begründung der Confidence-Einstufung")


class PortlightSystemAssessment(BaseModel):
    """Gesamtbewertung aller Bullaugen/Fenster eines Bootes."""
    model_config = {"from_attributes": True}

    # Boot-Referenz
    boat_id: str
    boat_name: Optional[str] = None
    boat_length_m: float
    boat_type: str = Field(..., description="sailboat/motoryacht/catamaran/trawler")
    ce_design_category: Optional[CEDesignCategory] = None

    # Bestandsaufnahme
    total_portlights: int = Field(..., description="Gesamtanzahl Bullaugen/Fenster")
    opening_count: int = Field(0, description="Davon öffnend")
    fixed_count: int = Field(0, description="Davon fest")
    structural_glazing_count: int = Field(0, description="Davon Structural Glazing")

    # Einzelbewertungen
    portlight_conditions: List[PortlightCondition] = Field(default_factory=list)

    # Aggregierte Bewertung
    overall_score: int = Field(..., ge=0, le=100, description="Gesamtscore 0-100")
    lens_avg_score: float = Field(..., ge=0, le=100)
    frame_avg_score: float = Field(..., ge=0, le=100)
    gasket_avg_score: float = Field(..., ge=0, le=100)

    # Compliance-Zusammenfassung
    all_iso_12216_compliant: bool = Field(False)
    height_violations: int = Field(0, description="Anzahl Bullaugen unter Mindesthöhe")
    missing_deadlights: int = Field(0, description="Anzahl fehlender Sturmblenden (wenn vorgeschrieben)")

    # Systemische Befunde
    ventilation_adequate: Optional[bool] = Field(None, description="Ausreichende Querlüftung durch Bullaugen")
    light_ingress_adequate: Optional[bool] = Field(None, description="Ausreichende Belichtung der Kabinen")
    mixed_manufacturers: bool = Field(False, description="Verschiedene Hersteller verbaut (Ersatzteil-Problem)")
    age_spread_years: Optional[int] = Field(None, description="Altersunterschied ältestes/neuestes Bullauge")

    # Kostenschätzung
    total_service_cost_eur: Optional[float] = Field(None, description="Kosten für Wartung aller Bullaugen")
    total_replacement_cost_eur: Optional[float] = Field(None, description="Kosten für Kompletttausch")
    priority_replacement_cost_eur: Optional[float] = Field(None, description="Kosten nur dringende Tausch")

    # Empfehlungen
    summary_de: str = Field(..., description="Zusammenfassung auf Deutsch")
    recommendations: List[str] = Field(default_factory=list, description="Empfehlungsliste")

    # Confidence
    confidence: ConfidenceLevel
    data_sources: List[str] = Field(default_factory=list, description="Datenquellen für diese Bewertung")
```

> Confidence: `measured` (Pydantic v2 Modelle validiert)

---

## 7. Grundlagen

### 7.1 Typen von Bullaugen und Seitenfenstern

#### 7.1.1 Öffnende Bullaugen (Opening Portlights)

**Funktionsprinzip:** Scheibe ist über ein Scharnier am Rahmen befestigt und kann zum Lüften geöffnet werden. Verriegelung durch Drehverschlüsse (Dogs), Hebel (Handles) oder Nockenverschlüsse (Cams).

**Vorteile:**
- Natürliche Belüftung ohne Stromverbrauch
- Querlüftung bei gegenüberliegender Anordnung
- Im Notfall als Fluchtweg nutzbar (wenn groß genug)

**Nachteile:**
- Schwachstelle für Wassereinbruch (Dichtung, Scharnier, Verriegelung)
- Teurer als Festfenster (mechanische Komponenten)
- Wartungsintensiver (Scharnier, Dichtung, Verriegelung)
- Lärmdurchlass bei geöffnetem Fenster in Marinas

**Scharnierpositionen:**
- **Oben scharniert (Top-hinged)**: Standard. Scheibe klappt nach außen oben auf. Regen läuft ab, Spritzwasser wird abgelenkt. Nachteil: bei Starkwind kann offene Scheibe als Windfang wirken.
- **Unten scharniert (Bottom-hinged)**: Selten. Scheibe klappt nach außen unten. Vorteil: Regen kann nicht direkt in die Öffnung. Nachteil: Wasser sammelt sich auf offener Scheibe.
- **Seitlich scharniert (Side-hinged)**: Bei rechteckigen Fenstern. Scheibe klappt seitlich auf. Vorteil: einfacher Mechanismus. Nachteil: Spritzwasser dringt leichter ein.
- **Pivot (Mittelscharnier)**: Horizontale Drehachse in Scheibenmitte. Obere Hälfte öffnet nach außen, untere nach innen. Gute Belüftung, keine Windfangwirkung. Bei Lewmar Standard-Bullaugen verwendet.

**Verriegelungstypen:**

| Typ | Beschreibung | Hersteller-Beispiele | Bewertung |
|-----|-------------|---------------------|-----------|
| **Dog** (Flügelschraube) | Drehbare Metallnase, die über Rahmen greift | Traditionelle Bullaugen, NFM | Sehr robust, 2–4 pro Bullauge |
| **Handle/Griff** | Drehgriff mit Nocken-Verriegelung | Lewmar, Goiot | Bedienkomfort, 1 Griff genügt |
| **Cam Latch** | Exzenter-Nocke presst Scheibe gegen Rahmen | Bomar, Beckson | Schnell, einfach |
| **Friction Stay** | Reibungsscharniere halten in jeder Position | Lewmar New Standard | Stufenlose Öffnung |
| **Spagnolette** | Durchgehender Stangen-Verschluss | Superyacht-Fenster | Mehrpunkt-Verriegelung |

#### 7.1.2 Feste Bullaugen (Fixed Portlights / Deadlights)

**Funktionsprinzip:** Scheibe ist permanent im Rahmen fixiert — durch Schrauben, Klammern oder Klebung. Kein Öffnungsmechanismus.

**Vorteile:**
- Höhere Dichtigkeit (keine beweglichen Teile)
- Günstiger (kein Scharnier, keine Verriegelung)
- Höhere Festigkeit bei gleicher Größe
- Geringerer Wartungsaufwand
- Bessere Isolation (keine Wärmebrücke durch Scharnier)

**Nachteile:**
- Keine Belüftung
- Nicht als Notausgang nutzbar
- Bei Scheibentausch aufwändiger (gesamter Rahmen betroffen)

**Anwendung:**
- Rumpfseite unterhalb 300mm über DWL (wo öffnend nicht zulässig)
- Salonfenster (groß, in Kombination mit anderen Lüftungsquellen)
- Designelemente (Lichtbänder an Rumpfseite)

#### 7.1.3 Flush-Mount Bullaugen

**Funktionsprinzip:** Rahmen schließt bündig mit der Außenhaut ab — kein vorstehender Flansch. Die Scheibe sitzt in einer Vertiefung der Wandung oder wird von innen montiert.

**Vorteile:**
- Saubere, moderne Optik — keine Unterbrechung der Rumpflinie
- Geringerer Strömungswiderstand (relevant bei Segelyachten)
- Kein Angriffspunkt für Festmacheleinen oder Fender

**Nachteile:**
- Aufwändiger Einbau (präziser Ausschnitt + Falz nötig)
- Dichtung anspruchsvoller (Klebung muss alle Kräfte aufnehmen)
- Nacharbeit bei Beschädigung komplizierter
- Teurer

**Hersteller:** Boman (Marktführer Flush-mount), Lewmar (Low-Profile Series), Trend Marine

#### 7.1.4 Structural Glazing (Verklebte Festfenster)

**Funktionsprinzip:** Scheibe wird direkt auf die Außenhaut oder den Aufbau geklebt — kein separater Rahmen. Der Klebstoff (marine PU oder Silikon) übernimmt Dicht-, Befestigungs- und Kraftübertragungsfunktion.

**Vorteile:**
- Maximale Lichtfläche (kein Rahmen verdeckt)
- Architektonisch ansprechend — moderner Yachtdesign-Standard
- Gute Kraftverteilung über die gesamte Klebfläche
- Keine Schrauben, die korrodieren oder sich lösen können

**Nachteile:**
- Klebstoff muss perfekt verarbeitet werden (Oberfläche, Primer, Aushärtezeit)
- Tausch = Zerstörung des Klebstoffs, aufwändig
- Keine Prüfmöglichkeit der Klebfuge von außen (nur visuell, ggf. Ultraschall)
- Bei Klebstoffversagen: Komplett-Ablösung der Scheibe möglich

**Typische Anwendung:** Salonfenster bei modernen Motor- und Segelyachten (Bavaria, Beneteau, Jeanneau, Azimut, Sunseeker)

> Confidence: `documented` (Hersteller-Kataloge, Surveyor-Erfahrung)

### 7.2 Formen

#### 7.2.1 Rund

**Spannungsverteilung:** Optimal — keine Spannungskonzentration. Ein runder Ausschnitt im Laminat erzeugt einen Spannungskonzentrationsfaktor (SCF) von ~2.0 (gleichmäßig um den Umfang).

**Lichtertrag:** Geringer als bei rechteckig gleicher Breite (Fläche Kreis = π/4 × d² vs. Rechteck = b × h).

**Ästhetik:** Klassisch-maritim, traditionell. Wirkt bei modernen Yachten teils anachronistisch.

**Typische Größen:**

| Bezeichnung | Außen-Ø (mm) | Lichte Weite (mm) | Anwendung |
|-------------|-------------|-------------------|-----------|
| Mini | 100–120 | 70–90 | Stauräume, Toiletten |
| Klein | 150–180 | 110–140 | Kabinen, Vorschiff |
| Standard | 200–250 | 160–210 | Kabinen, Standard |
| Groß | 300–400 | 250–350 | Salon, Eignerkajüte |
| Übergroß | 500+ | 400+ | Superyacht-Bullaugen |

#### 7.2.2 Oval / Elliptisch

**Spannungsverteilung:** Gut, SCF ~2.2–2.5 je nach Seitenverhältnis. Bei Seitenverhältnis >2:1 steigt der SCF merklich.

**Lichtertrag:** Kompromiss zwischen rund und rechteckig.

**Ästhetik:** Elegant, sportlich. Besonders beliebt bei modernen Segelyachten (Hallberg-Rassy, Najad).

**Typische Größen:** 300×150mm bis 500×250mm

#### 7.2.3 Rechteckig (mit Radien)

**Spannungsverteilung:** Stark abhängig vom Eckradius:
- R ≥ 25mm: SCF ~2.5–3.0 (akzeptabel)
- R = 15mm: SCF ~3.5 (grenzwertig)
- R < 10mm: SCF >4.0 (Rissbildungsgefahr am Ausschnitt)

**Mindest-Eckradius nach Praxis:**
- GFK-Laminat: R ≥ 20mm empfohlen, R ≥ 15mm Minimum
- Aluminium: R ≥ 15mm empfohlen, R ≥ 10mm Minimum
- Stahl: R ≥ 10mm empfohlen, R ≥ 8mm Minimum

**Lichtertrag:** Maximal — größte Scheibenfläche pro Ausschnittgröße.

**Ästhetik:** Modern, großzügig. Standard bei heutigen Serien-Motoryachten.

**Typische Größen:** 200×100mm bis 600×300mm (Bullaugen), bis 1500×600mm (Salonfenster)

#### 7.2.4 Trapezförmig

**Anwendung:** Anpassung an geneigte Aufbauwände. Die obere Kante ist kürzer als die untere, folgt also dem Profil der Deckshauswand.

**Typisch bei:** Modernen Motoryachten (Azimut, Ferretti, Princess, Sunseeker) und Performance-Segelyachten.

> Confidence: `documented` (Konstruktionspraxis, FEM-Studien)

### 7.3 Scheibenmaterialien

#### 7.3.1 Acrylglas (PMMA — Polymethylmethacrylat)

**Handelsbezeichnungen:** Plexiglas (Röhm/Evonik), Perspex (Lucite), Acrylite (Evonik NA)

**Eigenschaften:**

| Eigenschaft | Wert | Bemerkung |
|------------|------|-----------|
| Dichte | 1.19 g/cm³ | ~50% von Glas |
| Zugfestigkeit | 70–80 MPa | |
| E-Modul | 3.000–3.300 MPa | |
| Schlagzähigkeit (Charpy) | 15–20 kJ/m² | Spröder als PC |
| Lichttransmission | 92% (klar) | Bester Wert aller Kunststoffe |
| UV-Beständigkeit | Gut (inherent UV-stabil) | Kein UV-Stabilisator nötig |
| Temperaturbereich | -40°C bis +70°C | Ab 80°C Erweichung |
| Wasseraufnahme | 0.3% | Gering |
| Brechungsindex | 1.492 | |

**Vorteile im Yachtbau:**
- Beste Klarheit aller Kunststoffe (92% Lichttransmission)
- Inhärent UV-stabil — kein Vergilben über Jahrzehnte (bei Qualitätsmaterial)
- Leichter als Glas (spez. Gewicht ~0.5× Glas)
- Lässt sich polieren — Kratzer können entfernt werden
- Gute chemische Beständigkeit gegen Salzwasser
- ISO 12216 konform für alle Kategorien

**Nachteile:**
- **Crazing**: Haarrisse durch Lösungsmittel, Spannungen, UV-Ermüdung
- Spröde bei tiefen Temperaturen und Schlagbelastung
- Nicht schlagresistent — bei Bruch scharfkantige Stücke
- Empfindlich gegen Lösungsmittel (Aceton, Alkohol >70%, Reiniger mit Ammoniak)
- Thermische Ausdehnung 7× höher als Glas → Befestigung muss Spielraum bieten
- Erweicht bei >70°C — in dunklen Aufbauten in den Tropen relevant

**Qualitätsstufen:**
- **Gegossenes PMMA** (Cast): Beste Qualität, gleichmäßige Molekülverteilung, geringere Eigenspannung, weniger Crazing. Hersteller: Evonik (Plexiglas GS), Lucite (Perspex). Preis: 80–150 EUR/m² bei 8mm.
- **Extrudiertes PMMA** (Extruded): Günstiger, aber höhere Eigenspannungen, crazing-anfälliger. Hersteller: diverse. Preis: 40–80 EUR/m² bei 8mm.

**Marine-Sorten (empfohlen):**
- **Plexiglas GS 233 (klar)**: Standard für Yacht-Bullaugen
- **Plexiglas Resist 100**: Schlagfester, für Offshore
- **Perspex VHT (Very High Transmission)**: 93% Transmission, Premiumsorte

#### 7.3.2 Polycarbonat (PC)

**Handelsbezeichnungen:** Lexan (SABIC), Makrolon (Covestro), Paltuf (Palram)

**Eigenschaften:**

| Eigenschaft | Wert | Bemerkung |
|------------|------|-----------|
| Dichte | 1.20 g/cm³ | Ähnlich PMMA |
| Zugfestigkeit | 55–75 MPa | |
| E-Modul | 2.300–2.400 MPa | Flexibler als PMMA |
| Schlagzähigkeit (Charpy) | 60–80 kJ/m² | 4× besser als PMMA |
| Lichttransmission | 88% (klar) | Etwas weniger als PMMA |
| UV-Beständigkeit | Schlecht (ohne Beschichtung) | **Muss UV-beschichtet sein** |
| Temperaturbereich | -40°C bis +120°C | Weiter als PMMA |
| Wasseraufnahme | 0.15% | Sehr gering |

**Vorteile im Yachtbau:**
- Extrem schlagfest — "unzerbrechlich" im normalen Gebrauch
- Höherer Temperaturbereich als PMMA
- Leichter als Glas
- ISO 12216 konform

**Nachteile:**
- **Vergilbung**: Ohne UV-Schutzschicht vergilbt PC innerhalb von 2–3 Jahren deutlich
- **Kratzer**: Weicher als PMMA, verkratzt leichter
- Kratzer NICHT auspolierbar (anders als PMMA)
- UV-Schutzschicht ist aufgedampft — bei Beschädigung kein lokaler Repair
- Geringere optische Klarheit als PMMA (leichter Gelbstich)
- Chemisch empfindlich gegen Alkohol, Ammoniak, Bremsenreiniger

**Marine PC-Sorten (empfohlen):**
- **Lexan MR-10**: Beidseitig abriebfest und UV-beschichtet, 10 Jahre Garantie
- **Makrolon Multi UV**: UV-Schutz beidseitig, marine-tauglich
- **Palram Palgard**: Preiswert, einseitig UV-beschichtet (UV-Seite nach außen)

**PMMA vs. PC — Entscheidungshilfe:**

| Kriterium | PMMA | PC | Empfehlung |
|----------|------|----|----|
| Klarheit | ★★★★★ | ★★★★ | PMMA |
| Schlagfestigkeit | ★★ | ★★★★★ | PC |
| UV-Beständigkeit | ★★★★★ | ★★ (ohne Beschichtung) | PMMA |
| Kratzfestigkeit | ★★★ | ★★ | PMMA |
| Polierbarkeit | ★★★★★ | ★ | PMMA |
| Temperaturbereich | ★★★ | ★★★★★ | PC |
| Preis | ★★★★ | ★★★ | PMMA |
| Offshore/Blauwasser | - | - | PC (Schlag) |
| Küstenfahrt | - | - | PMMA (Klarheit) |

> Confidence: `measured` (Materialdatenblätter Evonik, SABIC, Covestro)

#### 7.3.3 Einscheibensicherheitsglas (ESG — Tempered Glass)

**Herstellung:** Thermisch vorgespannt — Scheibe wird auf ~600°C erhitzt und dann schnell abgekühlt. Die Oberfläche steht unter Druckspannung, der Kern unter Zugspannung.

**Eigenschaften:**

| Eigenschaft | Wert | Bemerkung |
|------------|------|-----------|
| Dichte | 2.50 g/cm³ | 2× schwerer als Kunststoff |
| Biegefestigkeit | 120–200 MPa | 4–5× normales Glas |
| Lichttransmission | 90% (klar) | |
| UV-Beständigkeit | Exzellent (permanent) | Vergilbt NICHT |
| Temperaturbereich | -70°C bis +250°C | Weit überlegen |
| Schlagfestigkeit | Gut (vs. Normalglas) | Aber: spontaner Totalbruch möglich |
| Kratzfestigkeit | Exzellent | Mohs 6-7 |

**Vorteile:**
- Kein Vergilben, kein Crazing — permanente Klarheit
- Exzellente Kratzfestigkeit
- Bei Bruch: kleine, stumpfe Krümel (Sicherheitsglas)
- Chemisch resistent gegen alles im Yachtumfeld
- Kein Spannungsrisskorrosion

**Nachteile:**
- Doppeltes Gewicht vs. Kunststoff
- Kann NICHT nachbearbeitet werden (kein Schneiden, kein Bohren nach dem Härten)
- **Spontanbruch** durch Nickel-Sulfid-Einschlüsse (selten, aber möglich)
- Bei Bruch: Totalverlust — nicht reparabel
- Nur in Standarddicken lieferbar (4, 5, 6, 8, 10, 12mm)

**Empfehlung:** Ab Bootslänge 14m für Salonfenster. Nicht für Offshore-Bullaugen in Rumpfseite (Bruchrisiko bei Schlag).

#### 7.3.4 Verbundsicherheitsglas (VSG — Laminated Safety Glass)

**Aufbau:** Zwei oder mehr Glasscheiben mit PVB-Folie (Polyvinylbutyral) oder EVA-Folie (Ethylen-Vinylacetat) laminiert.

**Eigenschaften:**
- Bei Bruch: Splitter haften an der Folie — keine Verletzungsgefahr
- Höhere Schlagresistenz als ESG
- Kann Resttragfähigkeit behalten (Scheibe hält trotz Bruch im Rahmen)
- Schalldämmung ~3 dB besser als Einscheibe gleicher Dicke
- UV-Schutz durch PVB-Folie (99% UV-Block)

**Typische Aufbauten für Yachten:**

| Aufbau | Dicke (mm) | Gewicht (kg/m²) | Anwendung |
|--------|-----------|-----------------|-----------|
| 3+3 VSG | 6.4 | 16 | Kleinere Seitenfenster |
| 4+4 VSG | 8.4 | 21 | Standard Salonfenster |
| 5+5 VSG | 10.4 | 26 | Große Salonfenster |
| 6+6 VSG | 12.4 | 31 | Superyacht, Kat. A |
| 8+8 VSG | 16.4 | 41 | Superyacht, Bugfenster |

**Empfehlung:** Standard für Superyachten >18m. Für Serien-Segelyachten nur bei Salonfenstern wirtschaftlich.

> Confidence: `measured` (Glasnorm EN 12150, EN 14449, Hersteller-Daten)

### 7.4 Rahmenmaterialien

#### 7.4.1 Aluminium (Guss und Strangpress)

**Gussaluminium (Cast Aluminum):**
- Legierung: AlSi7Mg (A356) oder AlSi12 (A413)
- Fertigungsverfahren: Kokillenguss oder Druckguss
- Oberfläche: Eloxiert (E6/EV1 — 15–25μm Schichtdicke) oder pulverbeschichtet
- Komplexe 3D-Formen möglich (Drehgriffe, Scharniere)
- Standard bei: Lewmar, Goiot, Bomar, Vetus

**Strangpressaluminium (Extruded Aluminum):**
- Legierung: 6061-T6 oder 6063-T5
- Fertigungsverfahren: Extrusion + CNC-Bearbeitung
- Gleichmäßigere Materialqualität als Guss
- Einfachere Profile (Rahmenleisten, Deckrahmen)
- Standard bei: ABI Industries, Trend Marine (Rahmenprofile)

**Korrosion:**
- Eloxierung schützt zuverlässig — Lebensdauer 15–25 Jahre in marinem Umfeld
- **Galvanische Korrosion**: Aluminium + Edelstahl-Schrauben in Salzwasser → Kontaktkorrosion!
  - Lösung: Isolierscheiben (Nylon/PTFE) zwischen Alu-Rahmen und Edelstahl-Befestiger
  - Oder: Edelstahl-Schrauben mit Duralac/Tef-Gel schmieren
- Pulverbeschichtung: Alternativer Korrosionsschutz, aber bei Beschädigung punktuell ungeschützt

**Preisklasse:** EUR 150–600 pro Bullauge (Serienfertigung), EUR 400–1.500 (Custom)

#### 7.4.2 Bronze

**Legierung:** Typisch Aluminiumbronze (CuAl10Fe3) oder Manganbronze (CuZn35Mn3Al2)

**Vorteile:**
- Keine galvanische Korrosion mit Edelstahl-Befestigern
- Patiniert ästhetisch ansprechend (Grünspan)
- Kann hochglanzpoliert werden — klassischer maritimer Look
- Extrem langlebig — Lebensdauer >50 Jahre
- Schwerer = robuster, bessere Schwingungsdämpfung

**Nachteile:**
- Deutlich teurer als Aluminium (3–5×)
- Schwerer als Aluminium (~3×)
- Begrenzte Herstellerauswahl (Nischenmarkt)
- Pflege: Regelmäßiges Polieren oder kontrollierte Patina

**Hersteller:** New Found Metals (Marktführer), Manship, Davey & Company

**Preisklasse:** EUR 400–2.000 pro Bullauge (handgefertigt)

#### 7.4.3 Edelstahl (316L)

**Standard:** AISI 316L (1.4404) — MUSS 316L sein für Salzwasser. 304 (1.4301) ist nicht ausreichend korrosionsbeständig.

**Vorteile:**
- Hohe Festigkeit
- Korrosionsbeständig (bei richtiger Legierung)
- Kann hochglanzpoliert oder satiniert werden
- Verschweißbar

**Nachteile:**
- **Tea Staining**: Braune Verfärbung in Küstennähe durch chloridinduzierte Mikrokorrosion
- **Crevice Corrosion**: Spaltkorrosion unter Schraubenköpfen, in Dichtungsnuten
- Galvanische Korrosion mit Aluminium
- Schwerer als Aluminium
- Teurer als Aluminium

**Empfehlung:** 316L nur für Einzelkomponenten (Scharniere, Dogs, Befestiger) oder Premium-Superyacht-Bullaugen. Nicht als Standard-Rahmenmaterial.

**Preisklasse:** EUR 300–1.200 pro Bullauge

#### 7.4.4 Kunststoff / Composite

**ABS/ASA-Kunststoff:**
- Budget-Segment (Beckson, Osculati Budget-Linie)
- UV-stabilisiert (ASA besser als ABS)
- Keine Korrosionsprobleme
- Geringe Festigkeit — nicht für Offshore
- Versprödung nach 5–10 Jahren

**GFK-Composite-Rahmen:**
- Selten bei Serienbullaugen, häufiger bei Custom-Einbauten
- Rahmen wird als Teil der Aufbaustruktur laminiert
- Scheibe dann direkt in den GFK-Rahmen eingeklebt (Structural Glazing)
- Keine Korrosion, keine galvanischen Probleme
- Aufwändig in der Herstellung

> Confidence: `documented` (Materialdaten, Hersteller-Kataloge, Surveyor-Erfahrung)

### 7.5 Deadlights (Sturmblenden)

#### 7.5.1 Funktion und Vorschriften

Ein **Deadlight** ist eine massive Metallblende, die über das Bullauge geschraubt oder geklappt wird und die Scheibe bei schwerem Wetter oder Beschädigung schützt. Historisch war der Deadlight die primäre Dichtung — das Bullauge dahinter war nur ein Lichtloch.

**Vorschriften:**
- **ISO 12216**: Deadlights empfohlen für CE Kat. A (Ozean), wenn Bullaugen-Unterkante <800mm über DWL
- **Klassifikationsgesellschaften (>24m)**: Deadlights vorgeschrieben für alle Rumpf-Bullaugen unter dem Festigkeitsdeck
- **World Sailing OSR (Offshore Special Regulations)**: Kategorie 0+1 Rennen: Sturmblenden für alle Bullaugen <800mm über DWL vorgeschrieben

#### 7.5.2 Typen

| Typ | Beschreibung | Befestigung | Hersteller |
|-----|-------------|-------------|-----------|
| **Schraubdeadlight** | Massive Platte, von außen aufgeschraubt | Dogs/Flügelschrauben | NFM, Manship |
| **Klappdeadlight** | Scharnier-montiert, klappt über Bullauge | Scharnier + Dogs | Lewmar (Superyacht) |
| **Schiebedeadlight** | Gleitet in Schiene über Bullauge | Schiene + Feststeller | Superyacht-Spezialanfertigung |
| **Innendeadlight** | Von innen montiert, als Isolierung oder Blackout | Magnete oder Clips | Diverse |

#### 7.5.3 Material

- **Aluminium**: Standard, leicht, eloxiert oder pulverbeschichtet
- **Edelstahl 316L**: Superyacht-Premium, hochglanzpoliert
- **Bronze**: Klassische Yachten, patiniert
- **GFK**: Leicht, korrosionsfrei, als Custom-Fertigung

#### 7.5.4 Dimensionierung

Der Deadlight muss den Ausschnitt vollständig überdecken mit mindestens 15mm Überlappung ringsum. Die Dichtung zwischen Deadlight und Aufbauwand ist typisch EPDM oder Neopren.

**Dicke (Aluminium) nach Praxis:**

| Bullauge Ø/Breite (mm) | Deadlight-Dicke (mm) | Bemerkung |
|-------------------------|---------------------|-----------|
| ≤150 | 4 | Leichte Ausführung |
| 150–250 | 5 | Standard |
| 250–400 | 6 | |
| 400+ | 8–10 | CE Kat. A |

> Confidence: `documented` (ISO 12216, WS-OSR, Klassifikationsregeln)

### 7.6 Insektenschutz (Mosquito Screens)

#### 7.6.1 Typen

| Typ | Beschreibung | Vorteile | Nachteile |
|-----|-------------|----------|-----------|
| **Integriertes Fliegengitter** | Herstellerseitig im Rahmen eingebaut | Bündig, sauber, passgenau | Tausch nur als Einheit, teuer |
| **Clip-in Screen** | Separater Rahmen, von innen eingesetzt | Einfach entfernbar, günstig nachrüstbar | Optisch weniger sauber |
| **Magnetgitter** | Mit Magneten am Rahmen befestigt | Schnell entfernbar | Nur bei Metall-Rahmen |
| **Rollo-Screen** | Aufrollbares Gitter, fest montiert | Platzsparend, elegant | Mechanik empfindlich |
| **Klett-Screen** | Klettband um Öffnung, Gitterstoff aufgedrückt | Günstig, universell | Provisorisch, ästhetisch unbefriedigend |

#### 7.6.2 Mesh-Spezifikationen

| Mesh-Typ | Maschenweite (mm) | Schutz gegen | Luftdurchlass |
|----------|-------------------|-------------|---------------|
| Standard | 1.2–1.5 | Fliegen, Mücken, Wespen | ~70% |
| Fein | 0.8–1.0 | + Kleine Mücken | ~60% |
| No-See-Um | 0.5–0.6 | + Sandmücken (Tropen) | ~45% |
| Pollen | 0.3–0.4 | + Pollen (Allergiker) | ~30% |

**Material:** Fiberglas-Gewebe (Standard), Edelstahl-Draht (langlebiger), Polyester (günstig)

**Hersteller von Nachrüst-Screens:**
- **Oceanair** (UK): Premium Clip-in und Rollo-Systeme, passgenau für Lewmar/Goiot
- **Plastimo** (FR): Standard-Clip-in für gängige Größen
- **Mosquito Magnet Marine** (NL): Magnet-befestigte Systeme

> Confidence: `documented`

### 7.7 Dichtungen

#### 7.7.1 EPDM (Ethylen-Propylen-Dien-Monomer)

**Standard-Dichtungsmaterial** für die meisten Marine-Bullaugen.

| Eigenschaft | Wert | Bewertung |
|------------|------|-----------|
| Temperaturbereich | -50°C bis +120°C | ★★★★★ |
| UV-Beständigkeit | Gut | ★★★★ |
| Ozonbeständigkeit | Exzellent | ★★★★★ |
| Salzwasserbeständigkeit | Exzellent | ★★★★★ |
| Shore-Härte | 40–70 A | Variabel |
| Druckverformungsrest | 15–30% (nach ASTM D395) | ★★★★ |
| Ölbeständigkeit | Schlecht | ★★ |
| Lebensdauer (marine) | 8–15 Jahre | ★★★★ |

**Empfehlung:** Standard für alle Bullaugen außer Maschinenraum (dort Öl-/Kraftstoffkontakt → Nitril oder Silikon verwenden).

**Typische Profile:**
- **D-Profil**: Hohlprofil, runde Dichtlippe. Standard für Lewmar, Goiot.
- **P-Profil**: Pilzkopf-Dichtung mit breiterem Fuß.
- **Flach-Profil**: Für Flansch-Dichtungen zwischen Rahmen und Aufbauwand.

#### 7.7.2 Neopren (Chloropren-Kautschuk, CR)

| Eigenschaft | Wert | Bewertung |
|------------|------|-----------|
| Temperaturbereich | -30°C bis +100°C | ★★★ |
| UV-Beständigkeit | Mäßig | ★★★ |
| Ölbeständigkeit | Gut | ★★★★ |
| Druckverformungsrest | 25–40% | ★★★ |
| Lebensdauer (marine) | 5–10 Jahre | ★★★ |

**Nachteile:** Wird unter -10°C spröde. Verhärtet schneller als EPDM unter UV. Heute weitgehend durch EPDM ersetzt.

**Anwendung:** Ältere Bullaugen (vor ~2000), einige Bomar-Modelle.

#### 7.7.3 Silikon (VMQ)

| Eigenschaft | Wert | Bewertung |
|------------|------|-----------|
| Temperaturbereich | -60°C bis +200°C | ★★★★★ |
| UV-Beständigkeit | Exzellent | ★★★★★ |
| Druckverformungsrest | 10–20% | ★★★★★ |
| Reißfestigkeit | Gering (3–8 MPa) | ★★ |
| Lebensdauer (marine) | 15–25 Jahre | ★★★★★ |

**Vorteile:** Bestes Rückstellverhalten, längste Lebensdauer, weitester Temperaturbereich.

**Nachteile:** Geringe Reißfestigkeit — Dichtung kann beim Einbau oder bei scharfkantigen Rahmen einreißen. Teurer als EPDM.

**Empfehlung:** Premium-Bullaugen, Hochbreiten-Einsatz, Superyachten.

#### 7.7.4 Dichtungswechsel — Intervalle

| Dichtungsmaterial | Revier Mittelmeer | Revier Nordeuropa | Tropen/Blauwasser |
|-------------------|-------------------|-------------------|-------------------|
| EPDM | 10–12 Jahre | 12–15 Jahre | 6–8 Jahre |
| Neopren | 6–8 Jahre | 8–10 Jahre | 4–6 Jahre |
| Silikon | 15–20 Jahre | 18–25 Jahre | 10–15 Jahre |

> Confidence: `measured` (Elastomer-Datenblätter), `documented` (Praxis-Erfahrung)

### 7.8 Einbauarten (Mounting)

#### 7.8.1 Spigot-Montage

**Prinzip:** Der Rahmen hat einen umlaufenden Steg (Spigot), der durch den Ausschnitt in der Wand gesteckt wird. Von innen wird ein Gegenring (Trim Ring / Innenrahmen) aufgesetzt und verschraubt.

```
       AUSSEN
  ╔═══════════════╗
  ║   Scheibe      ║
  ║   ┌─────────┐  ║
  ╠═══╡ SPIGOT  ╞══╣  ← Steg durch die Wand
  ║   └─────────┘  ║
  ║  Innenrahmen   ║
  ╚═══════════════╝
       INNEN
```

**Vorteile:**
- Saubere Optik innen und außen
- Dichtung zwischen Spigot und Wand möglich
- Wandstärke muss zur Spigot-Tiefe passen

**Nachteile:**
- Begrenzte Wandstärke (typisch max. 15–30mm je nach Modell)
- Ausschnitt muss sehr präzise sein (Spigot-Toleranz ±1mm)

**Typische Hersteller:** Lewmar (New Standard Portlight), Goiot (Cristal)

**Wandstärken-Kompatibilität (Lewmar New Standard):**

| Modell | Min. Wandstärke (mm) | Max. Wandstärke (mm) |
|--------|---------------------|---------------------|
| Size 0 | 10 | 25 |
| Size 1–3 | 10 | 30 |
| Size 4–6 | 10 | 35 |
| Size 7–10 | 12 | 40 |

#### 7.8.2 Flansch-Montage (Außenflansch)

**Prinzip:** Der Rahmen hat einen umlaufenden Flansch, der AUF der Außenseite der Wand aufliegt. Befestigung durch Schrauben durch den Flansch in die Wand.

**Vorteile:**
- Einfacherer Einbau (Ausschnitt-Toleranz weniger kritisch)
- Funktioniert bei jeder Wandstärke
- Sichtbare Befestigung → leicht prüfbar

**Nachteile:**
- Flansch steht über die Außenhaut vor — Fender können haken
- Ästhetisch weniger sauber als Flush-mount
- Schraubenlöcher in der Außenhaut (potenzielle Undichtigkeit)

**Typische Hersteller:** Bomar, Beckson, Vetus (viele Modelle)

#### 7.8.3 Flansch-Montage (Doppelflansch)

**Prinzip:** Rahmen hat Flansch AUSSEN und INNEN — die Wand wird "eingeklemmt". Schrauben verbinden äußeren und inneren Rahmen durch die Wand.

**Vorteile:**
- Höchste Dichtigkeit (Doppeldichtung: außen UND innen)
- Sehr robuste Befestigung
- Geeignet für dicke oder ungleichmäßig dicke Wandungen

**Nachteile:**
- Aufwändigster Einbau
- Optisch klobig
- Beide Seiten müssen zugänglich sein

#### 7.8.4 Flush-Bonded (Bündig verklebt)

**Prinzip:** Scheibe wird bündig in einen Falz in der Aufbauwand eingeklebt. Kein separater Rahmen sichtbar.

**Vorteile:**
- Architektonisch hochwertig — Designstandard moderner Yachten
- Keine vorstehenden Teile
- Gute Kraftverteilung durch flächige Klebung

**Nachteile:**
- Höchste Anforderungen an Einbaupräzision
- Scheibentausch = Klebfuge zerstören → aufwändig und teuer
- Klebfuge nicht visuell prüfbar (ggf. Ultraschall nötig)
- Kein Öffnen zum Lüften

**Klebstoff-Empfehlung:** Sikaflex-295 UV oder Simson ISR 70-03 (siehe ISO 21005 oben)

> Confidence: `documented` (Einbauanleitungen Lewmar, Bomar, Goiot; Werft-Praxis)

### 7.9 Mindesthöhe über Wasserlinie

#### 7.9.1 Berechnungsgrundlage

Die Mindesthöhe der **Unterkante** eines Bullauges über der **Konstruktionswasserlinie (DWL)** bestimmt, ob es öffnend oder nur fest eingebaut werden darf.

**ISO 12216 — Zusammenfassung der Höhenregeln:**

```
Wenn Unterkante Bullauge über DWL ≥ Mindesthöhe_öffnend:
  → Öffnendes Bullauge zulässig

Wenn Unterkante Bullauge über DWL ≥ Mindesthöhe_fest, aber < Mindesthöhe_öffnend:
  → Nur Festbullauge zulässig

Wenn Unterkante Bullauge über DWL < Mindesthöhe_fest:
  → Kein Bullauge zulässig (nur Beleuchtungselemente mit verstärktem Aufbau)
```

#### 7.9.2 Praxis-Konsequenzen

- **Segelyachten unter Krängung**: Die Höhe über Wasserlinie ändert sich mit der Krängung. Bei 25° Krängung ist die Lee-Seite um ~sin(25°) × B/2 abgesenkt. Bei einer 4m breiten Yacht = ~850mm Absenkung!
  - ISO 12216 berücksichtigt dies: Die Bemessungshöhe gilt für die **aufrechte** Position, aber die Druckbelastung wird für die geneigte Position berechnet.

- **Praxis-Empfehlung für Blauwasser-Segelyachten:**
  - Keine öffnenden Bullaugen in der Rumpfseite unter 600mm über DWL (unabhängig von CE-Kategorie)
  - Deadlights für alle Rumpf-Bullaugen unter 800mm über DWL
  - Aufbauwand-Bullaugen dürfen öffnend sein (höher über DWL)

> Confidence: `measured` (ISO 12216:2020), `documented` (Blauwasser-Erfahrung)

### 7.10 Alterung und Degradation von Acrylscheiben

#### 7.10.1 Crazing (Haarrisse)

**Definition:** Netzwerk von feinen Oberflächenrissen in PMMA, die die Scheibe milchig-trüb erscheinen lassen. Crazing ist die häufigste Alterungserscheinung von Acryl-Bullaugen.

**Ursachen:**
1. **Lösungsmittelkontakt**: Aceton, Alkohol, ammoniakhaltige Reiniger, Insektenspray
2. **Mechanische Spannung**: Zu festes Anziehen der Befestiger, ungleichmäßige Druckverteilung
3. **Thermische Spannung**: Schnelle Temperaturwechsel (z.B. kalter Regen auf heiße Scheibe)
4. **Eigenspannung**: Besonders bei extrudiertem PMMA (Herstellungsspannung)
5. **UV-Ermüdung**: Nach 15–25 Jahren auch bei hochwertigem PMMA möglich
6. **Chemische Einwirkung**: Teak-Reiniger (Oxalsäure), Gelcoat-Politur auf Scheibe

**Schweregrade:**

| Grad | Beschreibung | Sichtbarkeit | AYDI-Score |
|------|-------------|-------------|------------|
| 0 — Keine | Keine Haarrisse | Klar | 90–100 |
| 1 — Leicht | Einzelne feine Risse, nur im Streiflicht sichtbar | Kaum | 70–89 |
| 2 — Mäßig | Netzwerk von Rissen, bei Gegenlicht deutlich | Milchiger Eindruck | 40–69 |
| 3 — Stark | Dichte Crazing-Muster, Scheibe deutlich trüb | Undurchsichtig werdend | 15–39 |
| 4 — Strukturell | Crazing + Materialerweichung/Brüchigkeit | Sofort erkennbar | 0–14 |

#### 7.10.2 Vergilbung (Yellowing)

**Betrifft primär Polycarbonat (PC)** ohne ausreichende UV-Beschichtung. PMMA vergilbt kaum.

**Messung:** Yellowness Index (YI) nach ASTM D1925.
- Neu: YI <2 (klar)
- Leicht vergilbt: YI 5–10
- Deutlich vergilbt: YI 10–20
- Stark vergilbt: YI >20 (Tausch empfohlen)

#### 7.10.3 Polieren und Restauration

**PMMA-Scheiben können restauriert werden** — dies ist ein wesentlicher Vorteil gegenüber PC.

**Polierprozess (Marine-Standard):**

| Schritt | Mittel | Körnung | Verfahren |
|---------|--------|---------|-----------|
| 1 | Nassschleifen | P800 | Nur bei tiefen Kratzern |
| 2 | Nassschleifen | P1200 | Feine Kratzer |
| 3 | Nassschleifen | P2000 | Vorpolitur |
| 4 | Polierpaste (Xerapol/Novus 2) | — | Schwabbel oder Hand |
| 5 | Finish-Politur (Novus 1 / Plexus) | — | Handpolitur |

**Produkte für Acryl-Restauration:**

| Produkt | Hersteller | Typ | Preis (EUR) | Bemerkung |
|---------|-----------|-----|-------------|-----------|
| Novus 1 (Clean & Shine) | Novus Inc. | Reiniger/Schutz | ~12/237ml | Anti-Statik |
| Novus 2 (Fine Scratch Remover) | Novus Inc. | Polierpaste | ~12/237ml | Standard |
| Novus 3 (Heavy Scratch Remover) | Novus Inc. | Schleifpaste | ~12/237ml | Grobe Kratzer |
| Xerapol | Burnus | Acryl-Politur | ~15/100ml | Deutscher Standard |
| Plexus Plastic Cleaner | Plexus | Reiniger/Schutz | ~10/368ml | US-Standard |
| Micro-Mesh Kit | Micro-Surface | Schleifpads | ~25/Kit | 1.500–12.000er Set |

**Wann ist Restauration nicht mehr möglich?**
- Crazing Grad 3–4 (Risse gehen durch die gesamte Materialdicke)
- Vergilbung (bei PC — ist materialinhärent, nicht oberflächlich)
- Materialdicke <4mm nach Schleifen (Festigkeitsverlust)
- Strukturelle Risse (nicht nur Crazing, sondern echte Brüche)

**Kosten Polieren vs. Tausch:**

| Aktion | Kosten pro Bullauge (EUR) | Zeitaufwand |
|--------|--------------------------|-------------|
| Handpolitur (leichte Kratzer) | 15–30 (Material) | 30–60 min |
| Maschinenpolitur (mäßig) | 30–60 (Material + Verbrauch) | 60–120 min |
| Nassschleifen + Politur (stark) | 50–100 | 2–4 Stunden |
| Neue PMMA-Scheibe (Standard-Ø) | 40–150 (Material) | — |
| Komplett-Bullauge (Lewmar Std.) | 150–500 | 2–4 Stunden Einbau |

> Confidence: `documented` (Acrylglas-Verarbeitungsrichtlinien Evonik, Praxis-Erfahrung)

---

## 8. Hersteller — Vollständige Übersicht

### 8.1 Lewmar (UK) — Marktführer

**Firmenprofil:**
- **Sitz:** Havant, Hampshire, UK
- **Gegründet:** 1946
- **Marktposition:** Weltmarktführer für Marine-Beschläge, Luken und Bullaugen
- **OEM-Kunden:** Beneteau, Jeanneau, Hanse, Dufour, Hallberg-Rassy, Oyster, Moody, Dehler
- **Vertrieb:** Weltweit über Fachhändler (SVB, Compass, West Marine, Defender)

#### 8.1.1 New Standard Portlight (Opening) — Hauptserie

Die **New Standard Portlight** ist das meistverkaufte Yacht-Bullauge weltweit. Erhältlich in 11 Größen (Size 0–10), rechteckig mit Radien, opening.

**Konstruktionsmerkmale:**
- Rahmen: Gussaluminium, schwarz oder weiß pulverbeschichtet
- Scheibe: 4mm PMMA (Acrylglas), getönt (smoke grey) oder klar
- Dichtung: EPDM, austauschbar
- Scharnier: Friction-Stay — hält in jeder Öffnungsposition
- Verriegelung: Drehgriff (Handle) mit Nocken-Verriegelung
- Montage: Spigot, max. Wandstärke 20–38mm (größenabhängig)
- Insektengitter: Optional als Zubehör (Clip-in)
- CE-Konformität: Kat. A (Size 0–3), Kat. B (Size 4–8), Kat. C (Size 9–10)
- ISO 12216: Konform

**Größentabelle (gemessene Daten):**

| Size | Außen B×H (mm) | Ausschnitt B×H (mm) | Licht B×H (mm) | Gewicht (g) | Preis EUR (ca.) |
|------|---------------|---------------------|----------------|------------|-----------------|
| 0 | 196×111 | 172×87 | 153×68 | 450 | 150–180 |
| 1 | 251×111 | 227×87 | 208×68 | 520 | 160–195 |
| 2 | 306×111 | 282×87 | 263×68 | 590 | 175–210 |
| 3 | 306×166 | 282×142 | 263×123 | 720 | 195–235 |
| 4 | 361×166 | 337×142 | 318×123 | 810 | 210–255 |
| 5 | 393×191 | 369×167 | 350×148 | 910 | 235–280 |
| 6 | 420×174 | 396×150 | 377×131 | 870 | 230–275 |
| 7 | 443×209 | 419×185 | 400×166 | 1050 | 270–325 |
| 8 | 498×209 | 474×185 | 455×166 | 1180 | 295–355 |
| 9 | 506×260 | 482×236 | 463×217 | 1380 | 345–415 |
| 10 | 576×260 | 552×236 | 533×217 | 1520 | 385–460 |

> Confidence: `measured` (Lewmar Katalog 2024/2025, verifizierte Maße)

**Ersatzteile und Artikelnummern (Auswahl):**

| Teil | Artikelnummer (Beispiel Size 4) | Preis EUR (ca.) |
|------|-------------------------------|-----------------|
| Komplett-Bullauge (schwarz, Rauchglas) | 393420002 | 240 |
| Komplett-Bullauge (weiß, klar) | 393420012 | 240 |
| Ersatz-Acrylscheibe | 361000200 | 45–65 |
| Dichtungssatz (EPDM) | 360000400 | 15–25 |
| Insektengitter (Clip-in) | 361610400 | 35–50 |
| Friction-Stay-Scharnier (Paar) | 360020000 | 30–40 |
| Handle (Drehgriff) | 360030000 | 20–30 |

#### 8.1.2 Lewmar Standard Portlight (Fixed) — Festfenster

Gleiche Optik wie die Opening-Serie, aber ohne Scharnier und Griff. Scheibe ist verschraubt.

**Größen:** Identisch (Size 0–10)
**Preise:** ~30% günstiger als opening Version
**Anwendung:** Wenn Belüftung nicht nötig, z.B. unter Deck, Rumpfseite tief

#### 8.1.3 Lewmar Low Profile Portlight

**Merkmale:**
- Minimale Rahmenhöhe (Low Profile) — Rahmen steht nur 5mm über Oberfläche
- Flush-ähnliche Optik
- Gussaluminium, schwarz oder weiß
- PMMA 4mm, getönt oder klar
- Opening und Fixed verfügbar
- 4 Größen

**Einsatz:** Moderne Segelyachten, wo klassische Bullaugen optisch nicht passen.

#### 8.1.4 Lewmar Atlantis Portlight (Superyacht)

**Merkmale:**
- Edelstahl 316L Rahmen, hochglanzpoliert
- ESG oder VSG Scheibe (6–12mm)
- Deadlight-Option (klappbar)
- Custom-Größen auf Anfrage
- SOLAS-konform für Yachten >24m
- Preis: EUR 1.500–5.000+ pro Stück

### 8.2 Goiot (Frankreich) — Bénéteau-Zulieferer

**Firmenprofil:**
- **Sitz:** Saint-Herblain (bei Nantes), Frankreich
- **Gegründet:** 1957
- **Mutterkonzern:** Bénéteau Group
- **Marktposition:** Nr. 2 in Europa, Primärlieferant für Bénéteau, Jeanneau, Lagoon, CNB
- **Vertrieb:** Europa über Fachhändler, in USA begrenzt

#### 8.2.1 Goiot Cristal Serie

Die **Cristal**-Serie ist Goiots Hauptprodukt für Serienyachten.

**Konstruktionsmerkmale:**
- Rahmen: Gussaluminium, eloxiert oder pulverbeschichtet
- Scheibe: PMMA 4mm, getönt (grau oder bronze) oder klar
- Dichtung: EPDM (proprietäres Profil — Nachbau schwierig)
- Scharnier: Top-hinged mit Gasdruckfeder oder Friction-Stay
- Verriegelung: Drehgriff oder Push-Pull-Mechanismus
- Montage: Spigot (standard) oder Flansch (ältere Modelle)
- Insektengitter: Integriert bei neueren Modellen

**Größen (Opening, ausgewählte Modelle):**

| Modell | Außen B×H (mm) | Ausschnitt B×H (mm) | Typ | Preis EUR (ca.) |
|--------|---------------|---------------------|-----|-----------------|
| Cristal 10.10 | 243×138 | 219×114 | Opening | 180–220 |
| Cristal 20.20 | 335×138 | 311×114 | Opening | 200–245 |
| Cristal 30.30 | 335×183 | 311×159 | Opening | 220–270 |
| Cristal 40.40 | 427×183 | 403×159 | Opening | 250–305 |
| Cristal 50.50 | 427×240 | 403×216 | Opening | 290–350 |
| Cristal 60.60 | 519×240 | 495×216 | Opening | 340–410 |

**Ersatzteile — Herausforderung:**
Goiot-Dichtungen haben proprietäre Profile, die NICHT mit Lewmar-Dichtungen kompatibel sind. Ersatz nur über Bénéteau-Vertragshändler oder direkt bei Goiot. In Übersee oft schwierig zu beschaffen.

**Artikelnummern (Beispiel):**
- Cristal 30.30 Opening komplett: Art.-Nr. 30.30.01 (schwarz), 30.30.11 (weiß)
- Dichtungssatz Cristal 30.30: Art.-Nr. 91.30.30 — EUR ~18–25

> Confidence: `documented` (Goiot-Katalog 2023, Bénéteau-Teileservice)

### 8.3 Vetus (Niederlande) — Breit sortiert

**Firmenprofil:**
- **Sitz:** Schiedam, Niederlande
- **Gegründet:** 1969
- **Marktposition:** Breit aufgestellt (Motoren, Pumpen, Fenster, Sanitär)
- **Stärke:** Eines der größten Sortimente an Bullaugen und Fenstern
- **Vertrieb:** Weltweit, starkes Händlernetz in Europa

#### 8.3.1 Vetus PW-Serie (Opening Portlights, rund)

**Merkmale:**
- Runde Bullaugen in 5 Größen (PW201–PW401)
- Rahmen: Edelstahl 316L, hochglanzpoliert
- Scheibe: ESG (gehärtetes Glas), 5mm
- Dichtung: EPDM
- Scharnier: Seitlich, mit 2 Dogs (Flügelschrauben)
- Montage: Flansch (Außenflansch)
- Klassisch-traditionelles Design

**Größentabelle:**

| Modell | Außen-Ø (mm) | Licht-Ø (mm) | Glas-Dicke (mm) | Preis EUR (ca.) |
|--------|-------------|-------------|----------------|-----------------|
| PW201 | 210 | 136 | 5 | 180–220 |
| PW251 | 262 | 188 | 5 | 220–270 |
| PW301 | 316 | 240 | 5 | 280–340 |
| PW351 | 370 | 290 | 5 | 340–410 |
| PW401 | 420 | 340 | 6 | 420–510 |

#### 8.3.2 Vetus PWS-Serie (Opening Portlights, rechteckig)

**Merkmale:**
- Rechteckige Bullaugen, 6 Größen
- Rahmen: Edelstahl 316L ODER Aluminium (modellabhängig)
- Scheibe: PMMA 5mm oder ESG 5mm
- Scharnier: Top-hinged mit Friction-Stay
- Verriegelung: Drehgriff
- Montage: Spigot oder Flansch (modellabhängig)

**Größentabelle (PWS — rechteckig, Edelstahl):**

| Modell | Außen B×H (mm) | Ausschnitt B×H (mm) | Preis EUR (ca.) |
|--------|---------------|---------------------|-----------------|
| PWS22 | 276×141 | 252×117 | 200–250 |
| PWS32 | 368×141 | 344×117 | 230–280 |
| PWS33 | 368×196 | 344×172 | 260–315 |
| PWS43 | 460×196 | 436×172 | 300–365 |
| PWS44 | 460×252 | 436×228 | 350–425 |
| PWS54 | 552×252 | 528×228 | 400–485 |

> Confidence: `measured` (Vetus Katalog 2024/2025)

### 8.4 Bomar (USA) — US-Marktstandard

**Firmenprofil:**
- **Sitz:** Charlestown, New Hampshire, USA
- **Marktposition:** Standard-OEM für US-Werften (Catalina, Hunter, Island Packet)
- **Stärke:** Robuster Aluminium-Guss, vernünftige Preise

#### 8.4.1 Bomar Standard Opening Portlights

**Merkmale:**
- Rahmen: Gussaluminium, weiß oder schwarz pulverbeschichtet
- Scheibe: Lexan (Polycarbonat), 6mm, getönt
- Dichtung: Neopren (ältere Modelle) oder EPDM (ab ~2015)
- Verriegelung: Cam Latch (Nockenverschluss)
- Montage: Flansch (Standard), Spigot (optional)
- CE Kat. B–C (je nach Größe)

**Größen (ausgewählt):**

| Modell | Außen B×H (mm) | Typ | Preis USD (ca.) |
|--------|---------------|-----|-----------------|
| BP-1000 | 229×102 | Rectangular, opening | 140–170 |
| BP-2000 | 305×152 | Rectangular, opening | 170–210 |
| BP-3000 | 381×152 | Rectangular, opening | 200–250 |
| BP-4000 | 381×203 | Rectangular, opening | 230–280 |
| BP-5000 | 457×203 | Rectangular, opening | 270–330 |
| BR-1010 | 254 Ø | Round, opening | 190–240 |
| BR-1212 | 305 Ø | Round, opening | 240–300 |

**Bekannte Probleme:**
- Lexan-Scheiben vergilben nach 5–8 Jahren (UV-Beschichtung altert)
- Cam-Latch-Feder ermüdet — Bullauge schließt nicht mehr sicher
- Neopren-Dichtungen älterer Modelle (vor 2015) verhärten schnell
- Ersatzscheiben in Europa schwer beschaffbar (US-Import nötig)

> Confidence: `documented` (Bomar-Katalog, US-Forum-Erfahrungen)

### 8.5 Beckson (USA) — Budget-Segment

**Firmenprofil:**
- **Sitz:** Bridgeport, Connecticut, USA
- **Gegründet:** 1946
- **Marktposition:** Preisgünstigstes Bullauge am Markt — Budget/Einstieg
- **Einsatz:** Kleinboote, Trailer-Segler, Nachrüstung

#### 8.5.1 Beckson Opening Portlights

**Merkmale:**
- Rahmen: ABS-Kunststoff (weiß) oder Aluminium (teurere Modelle)
- Scheibe: Lexan (PC), 3mm — dünn!
- Dichtung: PVC oder Neopren — kurze Lebensdauer (3–5 Jahre)
- Verriegelung: Plastik-Cam Latch
- Montage: Flansch
- CE-Konformität: Nur Kat. D
- **NICHT für Offshore geeignet**

**Größen und Preise:**

| Modell | Außen B×H (mm) | Preis USD (ca.) | Bemerkung |
|--------|---------------|-----------------|-----------|
| 4×8 Opening | 203×102 | 50–70 | Kleinstes Modell |
| 4×12 Opening | 305×102 | 60–80 | |
| 6×12 Opening | 305×152 | 70–100 | Beliebt |
| 8×12 Opening | 305×203 | 90–120 | |
| 6×18 Opening | 457×152 | 100–140 | Größtes Modell |

**Typische Probleme:**
- Lexan-Scheiben verkratzen und vergilben schnell (1–3 Jahre in Tropen)
- ABS-Rahmen verspröden unter UV (5–8 Jahre)
- Cam-Latches brechen bei niedrigen Temperaturen
- Dichtungen schrumpfen und verhärten → Undichtigkeit nach 2–4 Jahren

**Wann Beckson OK ist:**
- Binnenrevier, Trailerboot, saisonaler Einsatz
- Notfall-Ersatz bis zum nächsten Werftaufenthalt
- Stauräume, Backskisten (nicht sicherheitsrelevant)

> Confidence: `documented` (Beckson-Katalog, umfangreiche Forum-Kritik)

### 8.6 New Found Metals (NFM) — Premium Bronze

**Firmenprofil:**
- **Sitz:** Port Townsend, Washington, USA
- **Gegründet:** 1986
- **Spezialität:** Handgefertigte Bronze-Bullaugen und -Beschläge
- **Marktposition:** Premium-Nische für klassische und Blauwasser-Yachten
- **Wartezeit:** 8–12 Wochen (Einzelanfertigung)

#### 8.6.1 NFM Runde Bullaugen (Opening)

**Merkmale:**
- Rahmen: Gegossene Aluminiumbronze (CuAl10Fe3), handpoliert oder patiniert
- Scheibe: ESG (gehärtetes Glas), 6mm, klar
- Dichtung: EPDM (Premium-Qualität)
- Verriegelung: 4 Dogs (Flügelschrauben) — traditionell, extrem sicher
- Deadlight: Optional, Bronze-Sturmblende mit eigener Dichtung
- Montage: Spigot oder Flansch (kundenspezifisch)
- CE: Kat. A (alle Größen)

**Größen und Preise:**

| Modell | Außen-Ø (mm) | Licht-Ø (mm) | Dogs | Preis USD (ca.) | Mit Deadlight |
|--------|-------------|-------------|------|-----------------|---------------|
| NFM-04 | 152 | 100 | 4 | 350–420 | +250 |
| NFM-06 | 203 | 150 | 4 | 420–510 | +300 |
| NFM-08 | 254 | 200 | 4 | 520–630 | +380 |
| NFM-10 | 305 | 250 | 4 | 650–790 | +450 |
| NFM-12 | 356 | 300 | 6 | 800–970 | +550 |
| NFM-14 | 406 | 350 | 6 | 980–1.190 | +680 |

#### 8.6.2 NFM Ovale Bullaugen

- 4 Größen: 200×100mm bis 400×200mm lichte Weite
- Bronze-Rahmen, ESG-Scheibe
- Preis: USD 500–1.400 pro Stück

**Warum NFM?**
- Für Eigneryachten, die "einmal richtig" gebaut werden
- Lebensdauer >40 Jahre (Bronze korrodiert nicht in Salzwasser)
- Keine galvanischen Probleme
- Resale-Wert-Steigerung bei klassischen Yachten
- Jedes Stück nummeriert und dokumentiert

> Confidence: `documented` (NFM-Website, Eigner-Berichte, Blauwasser-Community)

### 8.7 Boman (Taiwan) — Flush-Mount Spezialist

**Firmenprofil:**
- **Sitz:** Taipei, Taiwan
- **Spezialität:** Flush-mount Bullaugen und Fenster
- **OEM-Kunden:** Diverse asiatische Werften, europäische Werften als Zweitlieferant
- **Vertrieb:** Über Fachhändler, in Europa über Osculati/SVB

#### 8.7.1 Boman Flush-Mount Opening Portlights

**Merkmale:**
- Rahmen: Gussaluminium, eloxiert
- Scheibe: PMMA 5mm, getönt
- Flush-montiert — Rahmen schließt bündig mit Oberfläche ab
- Gasdruckfeder-Öffnung
- Preis: EUR 180–400 (je nach Größe)

### 8.8 ABI Industries (USA)

**Firmenprofil:**
- **Sitz:** Tacoma, Washington, USA
- **Spezialität:** Aluminium-Bullaugen und -Fenster, mittleres Preissegment
- **OEM-Kunden:** US-Werften (Pacific Seacraft, Nordhavn — ältere Modelle)

**Produkte:**
- Runde und rechteckige opening Portlights in Aluminium
- Robust, aber optisch wenig elegant
- Preis: USD 200–600

### 8.9 Manship (UK) — Klassische Bronze

**Firmenprofil:**
- **Sitz:** Cowes, Isle of Wight, UK
- **Gegründet:** 1978
- **Spezialität:** Bronze-Bullaugen und -Beschläge im traditionellen Stil
- **Marktposition:** Premium-Nische, UK-fokussiert

**Produkte:**
- Runde Bronze-Bullaugen, 4"–12" Durchmesser
- Opening mit Dogs, Optional Deadlight
- Preis: GBP 300–1.200 pro Stück

### 8.10 Plastimo (Frankreich) — Retail/Zubehör

**Firmenprofil:**
- **Sitz:** Lorient, Bretagne, Frankreich
- **Gegründet:** 1963
- **Marktposition:** Breit sortierter Marine-Zubehör-Hersteller
- **Stärke:** Gute Verfügbarkeit in europäischen Schiffsausrüstern

**Portlight-Sortiment:**
- Rundebullaugen (ABS und Aluminium), 150–300mm Ø
- Rechteckige Opening Portlights, 4 Größen
- Insektengitter als Nachrüstlösung
- Budget-bis-Mittelklasse
- Preis: EUR 80–250

### 8.11 Osculati (Italien) — Breit verfügbar

**Firmenprofil:**
- **Sitz:** Segrate (Mailand), Italien
- **Gegründet:** 1958
- **Sortiment:** >50.000 Artikel Marine-Zubehör
- **Stärke:** In fast jedem europäischen Schiffsausrüster vorrätig (SVB, Compass, etc.)

**Portlight-Sortiment:**
- Runde Bullaugen aus Edelstahl 316L und ABS, 6 Größen (100–300mm Ø)
- Rechteckige Opening Portlights (Aluminium), 5 Größen
- Flush-mount Modelle
- Budget-bis-Mittelklasse
- Preis: EUR 50–300

**Typische Artikelnummern:**
- 19.686.20 — Rund-Bullauge Edelstahl 316L, Ø 200mm, Opening, ESG: EUR ~160
- 19.686.25 — Rund-Bullauge Edelstahl 316L, Ø 250mm, Opening, ESG: EUR ~210
- 19.687.03 — Rechteckig Opening Portlight, Alu, 300×150mm: EUR ~135

### 8.12 Freeman Marine (USA) — Superyacht

**Firmenprofil:**
- **Sitz:** Gold Beach, Oregon, USA
- **Gegründet:** 1971
- **Spezialität:** Wasserdichte Türen, Fenster und Bullaugen für Superyachten und militärische Schiffe
- **Zertifizierungen:** SOLAS, ABS, LR, DNV, BV, RINA

**Produkte:**
- Watertight fixed und opening windows für Yachten >24m
- Aluminium 5083 oder Edelstahl 316L Rahmen
- VSG (Laminated Glass) bis 25mm Dicke
- Custom-Fertigung nach Zeichnung
- Preis: USD 3.000–25.000+ pro Fenster

### 8.13 Trend Marine (UK) — Windows

**Firmenprofil:**
- **Sitz:** Romsey, Hampshire, UK
- **Spezialität:** Yacht-Fenster und -Verglasungen (nicht Bullaugen im engeren Sinne)
- **OEM-Kunden:** Sunseeker, Princess, Fairline, Oyster

**Produkte:**
- Festverglaste Seitenfenster (Structural Glazing)
- Beheizte Fenster (Anti-Beschlag)
- Gebogene Scheiben (3D-geformt)
- ESG und VSG, getönt, Low-E-beschichtet
- Custom-only, keine Standardgrößen
- Preis: ab EUR 500/m²

### 8.14 Rutgerson (Schweden)

**Firmenprofil:**
- **Sitz:** Lysekil, Schweden
- **Gegründet:** 1975
- **Spezialität:** Segelyacht-Beschläge und -Bullaugen
- **OEM-Kunden:** Hallberg-Rassy (Primärlieferant), Najad, Malö

**Produkte:**
- Ovale und rechteckige Opening Portlights
- Aluminium-Rahmen, eloxiert (Natur oder schwarz)
- PMMA-Scheiben, 5mm, getönt
- EPDM-Dichtung
- Skandinavische Qualität — robust, langlebig, schlicht
- Sehr gute Dichtigkeit (HR-Segelyachten segeln offshore)
- 6 Standardgrößen
- Preis: EUR 250–500

**Besonderheit bei Hallberg-Rassy:**
- Rutgerson-Bullaugen mit HR-spezifischem Spigot-Maß
- Ersatz nur über HR oder Rutgerson direkt
- Dichtungsprofile sind proprietär

> Confidence: `documented` (Hersteller-Websites, Kataloge, OEM-Zuordnungen, Eigner-Erfahrungen)

---

## 9. Anlagen-spezifische Zuordnung

### 9.1 Salon / Deckshaus

#### 9.1.1 Anforderungen

Der Salon ist der Hauptaufenthaltsraum — hier sind Belichtung und Aussicht die primären Anforderungen. Die Fenster sind typisch die GRÖSSTEN an Bord.

**Designziele:**
- Maximale Lichtfläche (Verhältnis Fensterfläche/Wandfläche: 30–60%)
- Panoramaaussicht (niedrige Brüstungshöhe: 400–600mm über Bodenniveau)
- Offenes Raumgefühl (emotionale Wirkung)
- Wärmedämmung (Kondensation verhindern)
- Blendschutz (Sonneneinstrahlung kontrollieren)

#### 9.1.2 Typische Ausführungen

**Segelyacht (10–14m, Serie):**
- Seitenfenster: Structural Glazing, PMMA 10–12mm oder ESG 6mm, getönt (bronze/grau)
- Klebstoff: Sikaflex-295 UV
- Größe: 500–800mm breit, 200–350mm hoch
- Anzahl: 2–4 pro Seite
- Ergänzung: 1–2 öffnende Bullaugen pro Seite für Belüftung (Lewmar Size 3–5)

**Segelyacht (14–20m, Semi-Custom):**
- Seitenfenster: Structural Glazing, ESG 8mm oder VSG 6+6mm, Low-E-beschichtet
- Klebstoff: Sikaflex-296 oder Simson ISR 70-03
- Größe: 800–1200mm breit, 300–500mm hoch
- Anzahl: 3–6 pro Seite
- Öffnende Elemente: Integrierte Opening-Sektionen oder separate Bullaugen

**Motoryacht (10–16m, Serie):**
- Seitenfenster: Structural Glazing, ESG 8mm, getönt, teils umlaufendes Fensterband
- Größe: Bis 2000mm breit (Panorama)
- Lichtband oft über gesamte Salonlänge

**Superyacht (20m+):**
- VSG 8+8mm oder dicker, Low-E + Solar-beschichtet
- Gebogene Scheiben (3D-geformt) möglich
- Beheizte Scheiben (Anti-Beschlag)
- Elektrochromes Glas (Smart Glass) als Option
- Preis pro Fenster: EUR 2.000–15.000

#### 9.1.3 AYDI-Bewertungskriterien Salon

| Kriterium | Gewicht | Score 100 | Score 50 | Score 0 |
|----------|---------|-----------|----------|---------|
| Lichtfläche relativ zur Salonbreite | 20% | >50% Fensterfläche | 30–50% | <20% |
| Scheibenklarheit | 15% | Klar, kein Crazing | Leichtes Crazing | Stark gecrazed |
| Klebfuge/Rahmen-Zustand | 20% | Intakt, keine Risse | Leichte Risse | Leckend |
| Wärmedämmung | 10% | Doppelverglasung/Low-E | Einscheibe getönt | Einscheibe klar |
| Belüftung | 15% | ≥2 öffnende Elemente | 1 öffnend | Keine Öffnung |
| CE-Konformität | 20% | Vollständig | Teilweise | Nicht konform |

> Confidence: `estimated` (Bewertungskriterien AYDI-intern definiert)

### 9.2 Kabinen (Eigner, Gast, Bug)

#### 9.2.1 Anforderungen

Kabinen haben spezifische Anforderungen, die sich von Salon-Fenstern unterscheiden:

**Designziele:**
- Belüftung (Kabinen müssen unabhängig lüftbar sein — Geruch, Feuchtigkeit)
- Tageslicht (natürliches Erwachen, psychologisches Wohlbefinden)
- Privatsphäre (innen nicht von Marina-Steg einsehbar)
- Notausgang (ISO 12216: min. 400×520mm lichte Weite für Flucht)
- Verdunkelung (Schlaf am Tag, Marina-Beleuchtung nachts)
- Insektenschutz (im Hafen geöffnet)

#### 9.2.2 Typische Ausführungen

**Vorschiffskajüte (Segelyacht):**
- 1–2 öffnende Bullaugen pro Seite (typisch Lewmar Size 1–3 oder Goiot Cristal 10.10–20.20)
- Position: Rumpfseite, oberhalb Wasserlinie (beachte: Bug taucht bei Seegang ein!)
- Mindesthöhe über DWL beachten — Bugbereich hat höhere Belastung
- Insektengitter empfohlen
- Verdunkelungsrollo oder Innen-Deadlight

**Eignerkajüte (Motoryacht, mittschiffs):**
- Größere Bullaugen oder Seitenfenster (Lewmar Size 4–7 oder Vetus PWS33–PWS44)
- Oft 2–3 pro Seite
- Getönte Scheiben für Privatsphäre
- Öffnend für Belüftung
- Premium-Hersteller bei Superyachten (Trend Marine Custom)

**Gastkajüte (achtern):**
- 1 öffnendes Bullauge pro Seite (Standard, kleiner als Eignerkajüte)
- Typisch Lewmar Size 1–3

#### 9.2.3 Notausgang-Anforderungen

**ISO 12216 — Fluchtweg durch Bullauge:**
- Mindest-Lichtmaß: 400mm × 520mm (B × H) ODER 380mm Ø (rund)
- Muss von innen ohne Werkzeug öffenbar sein
- Muss gegen unbeabsichtigtes Schließen gesichert sein (Stay/Aussteller)
- Mindestens ein solcher Ausgang pro Schlafkabine (empfohlen, nicht überall vorgeschrieben)

**Praxis:** Die meisten Standard-Bullaugen (Lewmar Size 0–5) erfüllen die Fluchtweg-Anforderung NICHT — sie sind zu klein. Nur Size 7–10 oder spezielle Fluchtluken/Fenster kommen in Frage.

#### 9.2.4 AYDI-Bewertungskriterien Kabine

| Kriterium | Gewicht | Score 100 | Score 50 | Score 0 |
|----------|---------|-----------|----------|---------|
| Belüftung (öffnend) | 25% | ≥1 öffnend pro Seite | 1 öffnend gesamt | Keine |
| Tageslicht | 15% | Gut belichtet | Dämmerig | Dunkel |
| Scheibenzustand | 15% | Klar | Leichtes Crazing | Trüb |
| Dichtigkeit | 20% | Dicht | Leichte Feuchtigkeit | Wassereinbruch |
| Notausgang vorhanden | 15% | Ja, normkonform | Möglich, aber eng | Kein Fluchtweg |
| Insektenschutz | 10% | Integriert | Nachrüstbar | Nicht möglich |

### 9.3 Nassräume (Head/WC)

#### 9.3.1 Anforderungen

Nassräume stellen die HÖCHSTEN Anforderungen an Bullaugen wegen Feuchtigkeit und Geruch:

**Designziele:**
- **Belüftung ist KRITISCH** — Schimmelprävention, Geruchsabfuhr
- Feuchtigkeit: Dauerhaft >80% relative Luftfeuchtigkeit beim Duschen
- Privatsphäre: Undurchsichtige oder stark getönte Scheibe
- Korrosionsresistenz: Salz + Feuchtigkeit + Reinigungsmittel
- Wartungsfreundlichkeit: Dichtung und Scheibe leicht tauschbar

#### 9.3.2 Typische Ausführungen

- 1 öffnendes Bullauge (PFLICHT für natürliche Belüftung)
- Typisch: Klein bis mittel (Lewmar Size 0–2 oder Vetus PW201)
- Getönte (stark) oder satinierte Scheibe für Privatsphäre
- Alternativ: Klares Glas + Sichtschutzfolie (einfach nachrüstbar)
- Rahmen: Edelstahl 316L oder Aluminium eloxiert (KEIN unbeschichtetes Alu — korrodiert)
- Dichtung: EPDM oder Silikon (Silikon besser gegen Schimmel)

#### 9.3.3 Typische Probleme im Head

1. **Dichtungsverpilzung**: Schwarzer Schimmel auf EPDM-Dichtungen
   - Prävention: Silikon-Dichtung verwenden, Bullauge nach Duschen öffnen
   - Reinigung: Schimmelentferner ohne Chlor (greift EPDM an)

2. **Rahmenverfärbung**: Kalkablagerungen auf Edelstahl durch hartes Wasser
   - Reinigung: Essigessenz oder Zitronensäure

3. **Beschlag innen**: Kondensation auf kalter Scheibe
   - Lösung: Bullauge öffnen, Lüfter ergänzen

4. **Vergilbte Scheibe durch Reinigungsmittel**: Ammoniak-haltige Reiniger greifen PMMA an
   - Prävention: NUR Wasser + Spülmittel oder spezielle Acrylreiniger

#### 9.3.4 AYDI-Bewertungskriterien Head

| Kriterium | Gewicht | Score 100 | Score 50 | Score 0 |
|----------|---------|-----------|----------|---------|
| Öffnendes Bullauge vorhanden | 30% | Ja, funktionsfähig | Vorhanden, schwergängig | Nein/defekt |
| Schimmelfreiheit Dichtung | 20% | Sauber | Leichter Schimmel | Stark befallen |
| Scheibenzustand | 15% | Klar (oder getönt) | Leicht trüb | Crazing/Vergilbt |
| Rahmenzustand | 15% | Intakt | Leichte Verfärbung | Korrosion |
| Privatsphäre | 10% | Ausreichend | Grenzwertig | Nicht gegeben |
| Dichtigkeit | 10% | Dicht | Kondensat | Leck |

### 9.4 Pantry / Galley

#### 9.4.1 Anforderungen

Die Pantry hat spezifische Anforderungen durch Kochdämpfe, Fettpartikel und Hitze:

**Designziele:**
- Belüftung: Kochdämpfe abführen (öffnend PFLICHT)
- Fettresistenz: Scheibe und Rahmen müssen Fettdämpfe vertragen
- Reinigbarkeit: Einfach zu reinigende Oberflächen
- Hitzebeständigkeit: Kein PMMA direkt neben Herd (Erweichung bei >70°C)

#### 9.4.2 Typische Ausführungen

- 1 öffnendes Bullauge, idealerweise auf der dem Herd GEGENÜBERLIEGENDEN Seite
- Position: Möglichst über dem Kochbereich (warme Luft steigt auf)
- Scheibe: ESG (Glas) empfohlen — kein Crazing durch Fett/Reiniger, hitzebeständig
- Alternativ: PMMA mit Mindestabstand 300mm zum Herd
- Insektengitter empfohlen (Fliegen in tropischen Marinas)

#### 9.4.3 AYDI-Bewertungskriterien Pantry

| Kriterium | Gewicht | Score 100 | Score 50 | Score 0 |
|----------|---------|-----------|----------|---------|
| Öffnendes Bullauge vorhanden | 30% | Ja, nahe Kochstelle | Vorhanden, ungünstige Position | Keines |
| Scheibenmaterial geeignet | 20% | ESG/VSG | PMMA >300mm vom Herd | PMMA direkt neben Herd |
| Reinigbarkeit | 15% | Leicht zugänglich | Eingeschränkt | Schwer erreichbar |
| Scheibenzustand | 15% | Sauber, klar | Fettfilm, leichte Trübung | Stark verschmutzt |
| Dichtigkeit | 20% | Dicht | Leichte Feuchtigkeit | Leck neben Elektrik |

### 9.5 Maschinenraum

#### 9.5.1 Anforderungen und Einschränkungen

Der Maschinenraum ist ein **Sonderfall** mit strengen Sicherheitsanforderungen:

**Vorschriften (ISO 9094 — Brandschutz):**
- Bullaugen im Maschinenraum dürfen NICHT als primäre Belüftung zählen
- Öffnende Bullaugen im Maschinenraum: Nur mit feuerfester Scheibe (ESG/VSG, KEIN PMMA/PC)
- Bullaugen müssen von AUSSEN verschließbar sein (Brandfall: Sauerstoffzufuhr kappen)
- Mindestabstand zu Kraftstoffleitungen: 300mm
- Scheibe muss 15 Minuten Feuerwiderstand bieten (A-0 Klasse)

> ⚠️ **ZU PRÜFEN (Audit):** Widerspruch in der Feuerklasse — nach SOLAS/FTP bedeutet "A-0" 0 Minuten Isolationswiderstand (Integrität 60 min), während "15 Minuten" der Klasse "A-15" entspräche. Zeit/Klasse klären; für Sportboote <24 m gilt ohnehin ISO 9094, nicht das SOLAS-A-Klassen-Schema.

#### 9.5.2 Typische Ausführungen

- Festfenster bevorzugt (keine beweglichen Teile, die bei Vibration undicht werden)
- Scheibe: ESG 6mm (Minimum) oder VSG 5+5mm
- Rahmen: Edelstahl 316L (Aluminium korrodiert durch Motorabgase/Öldämpfe)
- Dichtung: Silikon (Ölbeständig, hitzebeständig) — NICHT EPDM (Öl-empfindlich)
- Klein (100–200mm Ø) — primär als Inspektionsfenster
- Deadlight empfohlen (Brandschutz)

#### 9.5.3 Besonderheit: Vibration

Motorvibrationen belasten Bullaugen-Befestigungen im Maschinenraum besonders:
- Schraubverbindungen mit Sicherungslack (Loctite 243)
- Dichtung muss Vibration absorbieren ohne zu wandern
- Regelmäßige Kontrolle: alle 200 Motorstunden oder 1× jährlich

#### 9.5.4 AYDI-Bewertungskriterien Maschinenraum

| Kriterium | Gewicht | Score 100 | Score 50 | Score 0 |
|----------|---------|-----------|----------|---------|
| Scheibenmaterial feuerfest | 30% | ESG/VSG | Dickes PMMA (>10mm) | Dünnes PMMA/PC |
| Dichtungsmaterial ölbeständig | 20% | Silikon/Nitril | EPDM | Neopren (alt) |
| Befestigung vibrationssicher | 20% | Gesichert, fest | Leicht locker | Lose/klappernd |
| Verschließbar von außen | 15% | Ja (Deadlight) | Nein, aber fest | Nein, öffnend ohne Sicherung |
| Abstand zu Kraftstoff/Öl | 15% | >300mm | 150–300mm | <150mm |

### 9.6 Zusammenfassung: Empfohlene Bullaugen nach Einbauort

| Einbauort | Empf. Typ | Empf. Scheibe | Empf. Rahmen | Empf. Dichtung | Öffnend? | Deadlight? |
|----------|-----------|---------------|-------------|----------------|----------|------------|
| Salon | Structural Glazing | ESG/VSG | Alu/GFK | Klebstoff | 1–2 Sektionen | Nein |
| Eignerkajüte | Opening, groß | PMMA/ESG | Alu elox. | EPDM | Ja (2/Seite) | Kat. A: Ja |
| Gastkajüte | Opening, mittel | PMMA | Alu elox. | EPDM | Ja (1/Seite) | Kat. A: Ja |
| Vorschiff | Opening, klein | PMMA | Alu elox. | EPDM | Ja (1/Seite) | Empfohlen |
| Head/WC | Opening, klein | ESG (getönt) | Edelstahl 316L | Silikon | Ja (Pflicht) | Nein |
| Pantry | Opening, mittel | ESG | Alu elox. | EPDM | Ja (Pflicht) | Nein |
| Maschinenraum | Fest, klein | ESG | Edelstahl 316L | Silikon | Nein | Empfohlen |
| Cockpit-Seite | Opening/Fest | PMMA | Alu elox. | EPDM | Optional | Nein |
| Transom | Fest, groß | ESG/VSG | Alu/GFK | Klebstoff | Nein | Nein |

### 9.7 Parametrische Kostenschätzung nach Bootslänge

#### 9.7.1 Bullaugen-Anzahl nach Bootslänge (Erfahrungswerte)

| Bootslänge (m) | Segelyacht (Stk.) | Motoryacht (Stk.) | Katamaran (Stk.) |
|----------------|-------------------|-------------------|-------------------|
| 8–10 | 4–6 | 4–6 | 6–10 |
| 10–12 | 6–8 | 6–10 | 8–14 |
| 12–14 | 8–12 | 8–14 | 12–18 |
| 14–16 | 10–14 | 10–18 | 14–22 |
| 16–20 | 12–18 | 14–24 | 18–28 |
| 20–24 | 14–22 | 18–30 | 22–34 |

> Hinweis: Motoryachten haben typisch mehr Fenster wegen größerer Aufbauten. Katamarane haben Fenster in beiden Rümpfen + Brücke.

#### 9.7.2 Kosten Neueinbau (Komplett: Material + Arbeit)

| Bootsklasse | Standard (Lewmar/Goiot) | Premium (Vetus Edelstahl) | Custom (NFM Bronze) |
|-------------|------------------------|--------------------------|---------------------|
| Produktion (8–14m) | 150–350 EUR/Stk. | 250–550 EUR/Stk. | 500–1.200 EUR/Stk. |
| Semi-Custom (14–20m) | 250–500 EUR/Stk. | 400–800 EUR/Stk. | 800–2.000 EUR/Stk. |
| Superyacht (20m+) | — | 600–2.000 EUR/Stk. | 1.500–5.000+ EUR/Stk. |

**Arbeitskosten Neueinbau pro Bullauge:**

| Aufwand | Stunden | Kosten (EUR, 65–95 EUR/h) |
|---------|---------|--------------------------|
| Ausschnitt anzeichnen + schneiden (GFK) | 1.0–2.0 | 65–190 |
| Kanten laminieren (Verstärkung) | 1.5–3.0 | 100–285 |
| Bullauge montieren + abdichten | 1.0–2.0 | 65–190 |
| Innenverkleidung anpassen | 0.5–1.5 | 35–145 |
| **Gesamt pro Bullauge** | **4.0–8.5** | **265–810** |

#### 9.7.3 Kosten Austausch (bestehendes Bullauge ersetzen)

| Aktion | Material (EUR) | Arbeit (EUR) | Gesamt (EUR) |
|--------|---------------|-------------|-------------|
| Nur Dichtungswechsel | 15–30 | 30–60 | 45–90 |
| Scheibentausch (PMMA) | 40–150 | 60–120 | 100–270 |
| Komplett-Bullauge gleiches Modell | 150–500 | 130–260 | 280–760 |
| Komplett-Bullauge anderes Modell | 150–500 | 200–500 | 350–1.000 |
| Structural Glazing Neuverklebung | 200–800 (Glas) | 300–600 | 500–1.400 |

> Confidence: `estimated` (Werft-Kalkulationen, Surveyor-Erfahrungswerte, Marktpreise 2024/2025)

### 9.8 Häufige Fehler bei Eigeneinbau

1. **Eckradius zu klein**: GFK reißt an den Ecken des Ausschnitts. Minimum R=20mm!
2. **Ausschnitt nicht verstärkt**: GFK-Laminat fasert aus. Kanten MÜSSEN mit 2–3 Lagen Glasgewebe + Epoxid verstärkt werden.
3. **Falsche Dichtmasse**: Sikaflex-291i (Unterwasser-PU) statt Sikaflex-295 UV (Verglasungs-PU) verwendet. 291i hält nicht auf Acryl!
4. **Schrauben zu fest angezogen**: PMMA-Scheibe steht unter Spannung → Crazing nach Wochen/Monaten.
5. **Kein Primer**: Sikaflex braucht Primer (Sika-Aktivator + Sika-Primer 209D) auf ALLEN Klebflächen.
6. **Drainagelöcher vergessen**: Bei Spigot-Montage muss Kondenswasser abfließen können.
7. **Keine galvanische Isolierung**: Alu-Rahmen + Edelstahl-Schrauben OHNE Isolierscheibe → Kontaktkorrosion nach 1–2 Saisons.
8. **Scheibe nicht spannungsfrei gelagert**: PMMA muss "schwimmend" montiert werden (Dehnungsspielraum).

> Confidence: `documented` (Surveyor-Berichte, Werft-Erfahrung, Forum-Konsens)

---

## 10. Technische Referenz & Berechnungen

### 10.1 Druckberechnung nach ISO 12216

Die ISO 12216 definiert die Designdrücke für Fenster und Bullaugen basierend auf Bootsklasse, Position und Größe.

#### 10.1.1 Design-Druck (Pd)

```
Pd = kDC × kAR × kL × Pb
```

| Variable | Bedeutung | Einheit |
|----------|-----------|---------|
| Pd | Design-Druck | kPa |
| kDC | Konstruktionskategorie-Faktor | dimensionslos |
| kAR | Flächenreduktionsfaktor | dimensionslos |
| kL | Positionsfaktor (Höhe über Wasserlinie) | dimensionslos |
| Pb | Basis-Druck | kPa |

**Kategorie-Faktoren kDC:**

| CE-Kategorie | kDC Rumpf | kDC Aufbau |
|-------------|-----------|------------|
| A (Ozean) | 1.00 | 0.67 |
| B (Offshore) | 0.80 | 0.53 |
| C (Küste) | 0.60 | 0.40 |
| D (Geschützt) | 0.40 | 0.27 |

**Flächenreduktionsfaktor kAR:**

```
kAR = 0.10 × (Ag)^(-0.15)   für Ag in m²
```

Wobei Ag = Glasfläche in m². Für typische Bullaugen:

| Durchmesser (mm) | Ag (m²) | kAR |
|-------------------|---------|-----|
| 150 | 0.0177 | 1.48 |
| 200 | 0.0314 | 1.36 |
| 250 | 0.0491 | 1.28 |
| 300 | 0.0707 | 1.22 |
| 350 | 0.0962 | 1.17 |
| 400 | 0.1257 | 1.13 |

**Positionsfaktor kL:**

```
kL = 1 + (h / T)^n
```

| Variable | Bedeutung |
|----------|-----------|
| h | Höhe Bullauge-Mittelpunkt über Sommerlastwasserlinie (m) |
| T | Konstruktionstiefgang (m) |
| n | 0.5 für Motorboote, 0.3 für Segelboote |

Typische Werte:

| h/T | kL Motor | kL Segel |
|-----|----------|----------|
| 0.5 | 1.71 | 1.38 |
| 1.0 | 2.00 | 1.55 |
| 1.5 | 2.22 | 1.67 |
| 2.0 | 2.41 | 1.77 |
| 3.0 | 2.73 | 1.93 |

#### 10.1.2 Basis-Druck Pb

**Rumpf-Bullaugen (unter Deck):**

```
Pb_Rumpf = 7.0 + 0.245 × LH    (kPa, für LH in m)
```

| LH (m) | Pb Rumpf (kPa) |
|---------|----------------|
| 8 | 8.96 |
| 10 | 9.45 |
| 12 | 9.94 |
| 15 | 10.68 |
| 20 | 11.90 |
| 25 | 13.13 |
| 30 | 14.35 |

**Aufbau-Bullaugen (über Deck):**

```
Pb_Aufbau = 3.5 + 0.122 × LH    (kPa, für LH in m)
```

| LH (m) | Pb Aufbau (kPa) |
|---------|-----------------|
| 8 | 4.48 |
| 10 | 4.72 |
| 12 | 4.96 |
| 15 | 5.33 |
| 20 | 5.94 |
| 25 | 6.55 |
| 30 | 7.16 |

#### 10.1.3 Beispielrechnung

**Szenario:** 12m Segelboot, CE-Kategorie B, Rumpf-Bullauge Ø 200mm, Mittelpunkt 0.8m über WL, Tiefgang 1.8m.

```
Pb = 7.0 + 0.245 × 12 = 9.94 kPa
kDC = 0.80 (Kategorie B, Rumpf)
kAR = 1.36 (Ø200mm → Ag = 0.0314 m²)
h/T = 0.8/1.8 = 0.44 → kL = 1 + 0.44^0.3 = 1.79

Pd = 0.80 × 1.36 × 1.79 × 9.94 = 19.4 kPa
```

### 10.2 Scheibendicke — Mindestanforderungen

#### 10.2.1 PMMA (Acrylglas)

Für kreisförmige Bullaugen gilt nach ISO 12216:

```
t_min = D × √(Pd / (4 × σ_zul))
```

| Variable | Bedeutung | Wert |
|----------|-----------|------|
| t_min | Mindestdicke (mm) | berechnet |
| D | Lichtdurchmesser (mm) | Eingabe |
| Pd | Design-Druck (kPa) | berechnet |
| σ_zul | Zulässige Spannung PMMA | 15 MPa (bei 20°C) |

**Typische Mindestdicken PMMA (Kategorie B, Rumpf, h/T=1.0):**

| Durchmesser | Pd (kPa) | t_min (mm) | Empfohlene Dicke |
|-------------|----------|------------|------------------|
| 150 mm | 18.9 | 4.2 | 6 mm |
| 200 mm | 17.4 | 5.3 | 8 mm |
| 250 mm | 16.3 | 6.4 | 8 mm |
| 300 mm | 15.5 | 7.4 | 10 mm |
| 350 mm | 14.9 | 8.5 | 10 mm |
| 400 mm | 14.4 | 9.7 | 12 mm |

> **Praxisregel:** Empfohlene Dicke = nächste gerade Zahl über t_min + 2mm Sicherheitszuschlag.

#### 10.2.2 Gehärtetes Glas (ESG)

```
σ_zul (ESG) = 40 MPa
```

| Durchmesser | Pd (kPa) | t_min ESG (mm) | Empfohlene Dicke |
|-------------|----------|----------------|------------------|
| 150 mm | 18.9 | 2.6 | 4 mm |
| 200 mm | 17.4 | 3.3 | 5 mm |
| 250 mm | 16.3 | 3.9 | 5 mm |
| 300 mm | 15.5 | 4.5 | 6 mm |
| 350 mm | 14.9 | 5.2 | 6 mm |
| 400 mm | 14.4 | 6.0 | 8 mm |

#### 10.2.3 Verbundglas (VSG)

Für VSG besteht die Scheibe aus zwei Einzelgläsern mit PVB-Folie:

```
t_eff = √(t1² + t2²)    (vereinfacht, da PVB keine Schubkopplung bei Langzeitlast)
```

Typisch: 2× 4mm ESG + 0.76mm PVB → t_eff ≈ 5.7mm

### 10.3 Belüftungsfläche

#### 10.3.1 Anforderungen nach ISO 11999 / Klassifikationsregeln

Natürliche Ventilation — Mindest-Öffnungsfläche je Raum:

> ⚠️ **ZU PRÜFEN (Audit):** Falsche Normnummer — "ISO 11999" ist die Normenreihe "PPE for firefighters" (Feuerwehr-Schutzkleidung) und hat mit Lüftung nichts zu tun. Die folgenden Prozentwerte (3,5 % / 2,5 % / 5,0 % / 4,0 %) sind nicht durch diese Norm belegt (eher Erfahrungs-/Klassifikationswerte). Korrekte Referenz vor Verwendung verifizieren.

| Raum | Mindest-Öffnungsfläche | Typisch Bullaugen |
|------|------------------------|-------------------|
| Kabine (Schlaf) | 3.5% der Bodenfläche | 2× Ø250mm öffenbar |
| Salon | 2.5% der Bodenfläche | 4× Ø250mm öffenbar |
| Pantry | 5.0% der Bodenfläche | 2× Ø200mm + Lüftergitter |
| Nasszelle | 4.0% der Bodenfläche + mech. Abzug | 1× Ø150mm + 12V-Ventilator |
| Maschinenraum | max(0.05 m², Motor_kW × 0.0003 m²) | Dedizierte Lüfter, keine Bullaugen |

**Nutzbare Öffnungsfläche eines Bullauges:**

```
A_eff = A_licht × k_öffnung
```

| Bullaugen-Typ | k_öffnung | A_eff bei Ø200mm |
|---------------|-----------|------------------|
| Fest (nicht öffenbar) | 0.00 | 0 cm² |
| Klappbar (90°) | 0.65 | 204 cm² |
| Klappbar (max 45°) | 0.35 | 110 cm² |
| Schiebbar | 0.50 | 157 cm² |
| Mosquitonetz montiert | ×0.60 | Reduktion 40% |

#### 10.3.2 Beispielrechnung Kabine

**Kabine:** 2.4m × 2.0m = 4.8 m² Bodenfläche
**Mindest-Öffnung:** 4.8 × 0.035 = 0.168 m² = 1.680 cm²
**2× Ø250mm klappbar (90°):** 2 × (π/4 × 250²) × 0.65 = 2 × 31.909 mm² × 0.65 ≈ 2 × 319 cm² × 0.65 = 415 cm²
**Mit Mosquitonetz:** 415 × 0.60 = 249 cm²

→ 249 cm² < 1.680 cm² — **nicht ausreichend!** Zusätzliche Ventilation erforderlich (Dorade-Lüfter, Decksluke).

> **Praxis-Hinweis:** Bullaugen allein reichen fast nie für die vollständige natürliche Ventilation einer Kabine. Sie sind Ergänzung zu Decksluken und Dorade-Lüftern.

### 10.4 Thermische Berechnung

#### 10.4.1 Wärmedurchgang U-Wert

| Verglasungstyp | U-Wert (W/m²K) | Rel. Wärmeverlust |
|----------------|-----------------|--------------------|
| Einfach PMMA 8mm | 5.2 | 100% (Referenz) |
| Einfach ESG 5mm | 5.7 | 110% |
| Doppelt PMMA 6+6mm, 12mm Luft | 2.8 | 54% |
| Doppelt ESG 4+4mm, 12mm Argon | 2.4 | 46% |
| Doppelt ESG 4+4mm, Low-E + Argon | 1.6 | 31% |

#### 10.4.2 Solare Wärmegewinne (g-Wert)

| Verglasungstyp | g-Wert | Solare Wärme bei 800 W/m² |
|----------------|--------|---------------------------|
| Klares PMMA | 0.85 | 680 W/m² |
| Getöntes PMMA (grau) | 0.55 | 440 W/m² |
| Klares ESG | 0.82 | 656 W/m² |
| ESG + Low-E | 0.42 | 336 W/m² |
| Getöntes ESG + Low-E | 0.28 | 224 W/m² |

> Confidence: `calculated` (ISO-12216-Formeln, Hersteller-Materialdatenblätter, thermische Standardwerte)

---

## 11. Einbau- und Austausch-Anleitung

### 11.1 Werkzeuge und Materialien

#### 11.1.1 Werkzeugliste (Vollständig)

| Werkzeug | Verwendung | Hinweis |
|----------|-----------|---------|
| Stichsäge mit Kurvenblatt | Ausschnitt sägen | Feinzahnblatt (>10 Zähne/cm) für GFK |
| Lochsäge/Kreisschneider | Runde Ausschnitte | Ab Ø150mm Kreisschneider stabiler |
| Oberfräse mit Bündigfräser | Ausschnitt nacharbeiten | Für saubere Kanten |
| Bandschleifer / Exzenterschleifer | Oberfläche vorbereiten | Korn 80–120 |
| Akkuschrauber | Befestigung | Drehmomenteinstellung nutzen! |
| Kartuschenpistole (310ml) | Dichtmasse auftragen | Gleichmäßiger Druck |
| Abklebeband (UV-beständig) | Saubere Dichtnähte | Tesa 4174 o.ä. |
| Lösemittel (Isopropanol) | Reinigung, Entfettung | KEIN Aceton auf PMMA! |
| Sika-Aktivator 205 | Vorbehandlung Metall/GFK | Wartezeit 15 min |
| Sika-Primer 209D | Vorbehandlung Glas/PMMA | Wartezeit 30 min |
| Drehmomentschlüssel | Schrauben kontrolliert anziehen | 2–4 Nm je nach Hersteller |
| Hinterschnittanker-Set | Steinbedding | Nur bei Alurahmen >Ø300mm |
| Atemschutzmaske FFP2 | GFK-Staub | PFLICHT beim Sägen/Schleifen |
| Schutzbrille | Splitterschutz | Immer tragen |

#### 11.1.2 Verbrauchsmaterialien

| Material | Menge pro Bullauge | Preis (EUR) |
|----------|-------------------|-------------|
| Sikaflex-295 UV (Verglasungs-PU) | 50–100 ml | 8–15 (anteilig 310ml-Kartusche) |
| Sika-Aktivator 205 | 5 ml | 2 (anteilig) |
| Sika-Primer 209D | 5 ml | 3 (anteilig) |
| Butylband 3mm × 10mm | 0.5–1.0 m | 2–4 |
| Edelstahl-Schrauben A4 M5×25 | 6–12 Stück | 3–6 |
| Isolierscheiben (Nylon/PTFE) | 6–12 Stück | 1–2 |
| GFK-Verstärkungsgewebe 300g/m² | 0.1 m² | 3 |
| Epoxidharz + Härter | 50 ml | 5 (anteilig) |
| Abklebeband | 3 m | 1 |
| Isopropanol | 50 ml | 1 |

**Gesamtkosten Verbrauchsmaterial:** ca. 30–45 EUR pro Bullauge

### 11.2 Spigot-Montage (Durchsteck-Montage)

Die Spigot-Montage ist die gängigste Methode für runde Bullaugen in GFK-Rümpfen.

#### Schritt 1: Ausschnitt anzeichnen

1. Innenposition auf Rumpf/Aufbau markieren (Mittelpunkt)
2. Von innen prüfen: keine Verstärkungen, Kabel, Schläuche im Weg?
3. Prüfen: Minimum 80mm Abstand zu nächstem Ausschnitt oder Kante
4. Schablone des Herstellers verwenden (NICHT nach Katalogmaß zeichnen!)
5. Mittelpunkt durchbohren (Ø6mm Pilotbohrung von innen nach außen)
6. Schablone von AUSSEN aufkleben, sorgfältig zentrieren
7. Ausschnittdurchmesser = Spigot-Außendurchmesser + 2–3mm Spiel

#### Schritt 2: Ausschnitt sägen

1. Atemschutz und Schutzbrille anlegen
2. Abklebeband großzügig um Schnittlinie (beidseitig 50mm) → schützt Gelcoat
3. Startbohrung Ø10mm innerhalb der Schnittlinie
4. Stichsäge mit Pendelhub AUS, mittlere Drehzahl, NICHT drücken
5. Alternativ: Kreisschneider für saubere Rundschnitte
6. Kanten mit 80er Schleifpapier leicht anfasen (1–2mm × 45°)
7. GFK-Staub absaugen, Ausschnitt mit Isopropanol reinigen

#### Schritt 3: Ausschnitt verstärken

1. Schnittkanten mit 2–3 Lagen GFK-Gewebe (300g/m², 30mm breit) + Epoxid laminieren
2. Epoxid vollständig aushärten lassen (min. 24h bei 20°C)
3. Überstehende Fasern abschleifen (Korn 120)
4. Kante MUSS vollständig versiegelt sein — offene GFK-Fasern = Wassereinbruch!

#### Schritt 4: Trockenpassung

1. Bullauge-Rahmen (außen) durch Ausschnitt stecken
2. Innenring lose aufsetzen
3. Prüfen: gleichmäßiges Spiel ringsum (1–1.5mm)?
4. Prüfen: Rahmen liegt plan auf? Keine Wölbung/Verformung?
5. Schraubenlöcher anzeichnen (bei Rahmen ohne vorgebohrte Löcher)
6. Ggf. Konturfräsung für gewölbte Rumpfflächen (bei stark gerundeten Bereichen)

#### Schritt 5: Oberflächenvorbereitung

1. Klebflächen (50mm Ring um Ausschnitt, beidseitig) mit Korn 80 anschleifen
2. Staub entfernen, mit Isopropanol entfetten
3. Trocknen lassen (min. 15 min)
4. Sika-Aktivator 205 auf GFK und Metallrahmen auftragen, 15 min ablüften
5. Sika-Primer 209D auf PMMA-Scheibe auftragen (nur Randbereich!), 30 min ablüften
6. Primer NICHT auf sichtbare Scheibenfläche! Abkleben!

#### Schritt 6: Dichtmasse und Montage

1. Sikaflex-295 UV in gleichmäßiger Raupe (Ø8–10mm) auf Rahmen-Flansch auftragen
2. Raupe geschlossen, keine Unterbrechungen!
3. Rahmen durch Ausschnitt führen, gleichmäßig andrücken
4. Innenring aufsetzen
5. Schrauben handfest einsetzen (Reihenfolge: gegenüberliegend, wie Radmuttern)
6. Drehmomentschlüssel: 2.5–3.5 Nm (je nach Hersteller)
7. NICHT überziehen! PMMA-Scheibe darf NICHT unter Spannung stehen!
8. Überschüssige Dichtmasse mit Spachtel und Isopropanol sofort entfernen
9. Abklebeband entfernen, solange Dichtmasse noch feucht

#### Schritt 7: Drainagelöcher

1. Am tiefsten Punkt des Rahmens (außen) Ø3mm Drainageloch bohren
2. Mindestens 2 Drainagelöcher pro Bullauge empfohlen
3. Drainage NICHT mit Dichtmasse verschließen!

#### Schritt 8: Aushärtung und Kontrolle

1. 48h nicht belasten, nicht schließen/öffnen
2. Vollständige Aushärtung Sikaflex-295 UV: 7 Tage (bei 23°C / 50% rF)
3. Wassertest mit Gartenschlauch: 5 min gezielt auf Bullauge spritzen
4. Von innen kontrollieren: trocken? Keine Feuchtigkeit am Rahmen?

### 11.3 Flansch-Montage (Aufbau-Montage)

Die Flansch-Montage wird verwendet, wenn der Spigot nicht durch die Wandstärke passt oder bei sehr dicken Aufbauwänden (>30mm).

#### Unterschiede zur Spigot-Montage:

| Aspekt | Spigot | Flansch |
|--------|--------|---------|
| Wandstärke | 8–25mm | 10–60mm+ |
| Ausschnitt | = Spigot-Außen-Ø + 2mm | = Lichtmaß + 5mm |
| Dichtung | Sikaflex ringsum | Butylband + Sikaflex |
| Befestigung | Durchgangs-Schrauben | Hinterschnitt-Anker o. Durchgang |
| Kraft auf Wand | Gering (Klemm-Prinzip) | Höher (Flansch-Druck) |
| Typisch für | GFK-Rümpfe, Aufbauten | Alu-Aufbauten, Stahl, dickes GFK |

#### Flansch-Montage Besonderheiten:

1. **Butylband als Erstdichtung:** 3mm Butylband auf Flansch-Rückseite kleben VOR Sikaflex
2. **Kein Spigot = kein Zentrierhilfe:** Ausschnitt-Lehre verwenden, Bullauge temporär mit 4 Keilen fixieren
3. **Schraubenabstand:** max. 60mm bei Alu-Rahmen, max. 80mm bei Edelstahl-Rahmen
4. **Unterlegscheiben:** Großflächige USS-Scheiben (Ø20mm) auf der Innenseite verwenden
5. **Galvanische Trennung:** Bei Alu-Rahmen auf Stahl/Edelstahl-Rumpf: PTFE-Isolierscheiben + Isolierhülsen PFLICHT

### 11.4 Austausch bestehender Bullaugen

#### 11.4.1 Demontage

1. Innenring-Schrauben lösen (ggf. WD-40 einweichen lassen, 30 min)
2. Innenring abhebeln (Kunststoff-Hebel, KEIN Metallwerkzeug an GFK!)
3. Alte Dichtmasse mit Multitool (oszillierend) oder Cutter abschneiden
4. Rahmen herausdrücken (von innen nach außen)
5. Alte Dichtmasse vom Ausschnitt vollständig entfernen
6. Ausschnitt-Kanten prüfen: Risse? Delaminierung? Feuchtigkeit?
7. Bei Schäden: Ausschnitt aufweiten, neu verstärken, größeres Bullauge wählen

#### 11.4.2 Häufige Probleme beim Austausch

| Problem | Ursache | Lösung |
|---------|---------|--------|
| Schrauben festkorrodiert | Kontaktkorrosion | Penetrieröl + Wärme (Heißluft 150°C) |
| Alte Dichtmasse nicht lösbar | PU-Verklebung zu stark | Multitool mit Klinge, NICHT meißeln |
| Ausschnitt zu groß für neues Bullauge | Anderer Hersteller / Maß | GFK-Ring einlaminieren, neuen Ausschnitt |
| Feuchtes Laminat hinter Rahmen | Undichtigkeit über Jahre | Trocknen (Heizlüfter, 2–3 Tage), dann Epoxid |
| Gelcoat-Schäden um Ausschnitt | Unsachgemäße Demontage | Gelcoat-Reparaturset, Farbton anpassen |

> Confidence: `documented` (Werft-Anleitungen, Hersteller-Montagevideos, Surveyor-Erfahrung)

---

## 12. Lebensdauer und Alterungsmechanismen

### 12.1 Übersicht Lebensdauer je Komponente

| Komponente | Lebensdauer (Jahre) | Hauptalterung | Wartungsintervall |
|------------|--------------------:|---------------|-------------------|
| PMMA-Scheibe (klar) | 15–20 | UV-Crazing, Vergilbung | Jährlich polieren |
| PMMA-Scheibe (getönt) | 12–18 | UV-Abbau, Farbverlust | Jährlich polieren |
| ESG-Scheibe | 25–40+ | Praktisch keine | Reinigen |
| VSG-Scheibe | 20–30 | PVB-Delaminierung an Kanten | 5-jährlich inspizieren |
| Edelstahl-Rahmen (316L) | 25–40 | Spaltkorrosion, Verfärbung | 2-jährlich polieren |
| Alu-Rahmen (eloxiert) | 15–25 | Eloxalschicht-Abbau, Lochfraß | 2-jährlich konservieren |
| Bronze-Rahmen | 40–60+ | Patina (kosmetisch) | Optional polieren |
| EPDM-Dichtung | 5–8 | UV-Verhärtung, Setzung | 3-jährlich prüfen, 6-8J tauschen |
| Neopren-Dichtung | 4–6 | UV-Rissbildung | 2-jährlich prüfen, 5J tauschen |
| Silikon-Dichtung (fest) | 8–12 | UV-Vergilbung, Abriss | 5-jährlich prüfen |
| PU-Dichtmasse (Sikaflex) | 15–25 | UV-Oberfläche, Elastizität ↓ | 10-jährlich prüfen |
| Dog-Verschluss (Bronze) | 30–50 | Mechanischer Verschleiß | Jährlich fetten |
| Dog-Verschluss (Zamak) | 5–10 | Zinkfraß, Korrosion | 2-jährlich prüfen |
| Dog-Verschluss (Edelstahl) | 20–35 | Festfressen | Jährlich fetten |
| Scharnier (Edelstahl) | 15–25 | Spaltkorrosion am Stift | Jährlich fetten |
| Moskitonetz-Rahmen | 8–15 | UV-Abbau Kunststoff, Netzrisse | 3-jährlich prüfen |
| Verdunklungsrollo | 5–10 | Federmechanismus, Stoffalterung | Jährlich prüfen |

### 12.2 Detaillierte Alterungsmechanismen

#### 12.2.1 PMMA-Crazing (Spannungsrisskorrosion)

**Mechanismus:** Mikrorisse entstehen an der Oberfläche durch Kombination aus:
- Mechanischer Spannung (Einbauspannung, Temperaturwechsel)
- Chemischem Angriff (Lösemittel, aggressive Reiniger)
- UV-Degradation (Kettenspaltung des Polymers)

**Stadien:**

| Stadium | Beschreibung | Alter (typisch) | Reparabel? |
|---------|-------------|-----------------|------------|
| 1 - Initiation | Unsichtbar, nur unter Polarisationsfilter | 3–5 Jahre | Vermeidbar |
| 2 - Mikrocrazing | Feine Linien, nur bei Gegenlicht sichtbar | 5–10 Jahre | Ja, auspolieren |
| 3 - Sichtbares Crazing | Netzwerk aus feinen Rissen, milchig | 10–15 Jahre | Teilweise |
| 4 - Tiefes Crazing | Risse durch >50% der Wandstärke | 15–20 Jahre | Nein, tauschen |
| 5 - Strukturversagen | Scheibe bricht bei Stoß/Druck | 20+ Jahre | SOFORT tauschen |

**Beschleuniger:**
- Aceton, Verdünner → SOFORT Crazing! (NIEMALS verwenden)
- Spülmittel (konzentriert) → beschleunigt Crazing 2–3×
- Einbauspannung → beschleunigt Crazing 5–10×
- UV ohne Schutz → beschleunigt Crazing 2×
- Salzwasser → beschleunigt Crazing 1.5×

**Prävention:**
- Spannungsfreie Montage (Dehnungsspielraum 1mm/100mm)
- Nur PMMA-zugelassene Reiniger (Burnus Plexiklar, Novus #1)
- UV-Schutzfolie oder UV-stabilisiertes PMMA verwenden
- Jahrespolitur mit Novus #2 (feine Kratzer), dann #1 (Versiegelung)

#### 12.2.2 Dichtungs-Alterung

**EPDM-Degradation:**
- UV-Strahlung bricht Polymerketten → Verhärtung
- Druckverformungsrest (Compression Set): nach 5 Jahren 40–60% permanent verformt
- Shore-Härte steigt von 50A (neu) auf 70A+ (alt) → Dichtfunktion verloren
- Ozon-Rissbildung: parallel zur Spannungsrichtung

**Neopren-Degradation:**
- UV-empfindlicher als EPDM
- Wird spröde und rissig nach 4–6 Jahren UV-Exposition
- Ölkontakt beschleunigt Zerfall

**Erkennungszeichen für Dichtungstausch:**
1. Druckverformungsrest sichtbar (Dichtung kehrt nicht in Originalform zurück)
2. Shore-Härte fühlbar gestiegen (Fingernagel-Test: kein Eindruck mehr)
3. Risse sichtbar (auch feine)
4. Wasser dringt bei Regen/Seewasser ein
5. Dichtung klebt am Rahmen oder Scheibe fest

#### 12.2.3 Rahmen-Korrosion

**Edelstahl 316L:**
- Passivschicht (Cr₂O₃) schützt normalerweise
- Spaltkorrosion in engen Spalten (Rahmen↔GFK): O₂-Verarmung → Passivschicht bricht zusammen
- Tea Staining: kosmetische Rostflecken an der Oberfläche, NICHT strukturell
- Lochfraß: lokale Durchbrüche, strukturell relevant bei >25% Wandstärke
- Prävention: Spalt ≥2mm oder vollständig versiegelt, keine stehende Feuchtigkeit

**Aluminium (eloxiert):**
- Eloxalschicht 15–25µm schützt 10–20 Jahre
- Beschädigung der Eloxalschicht → Lochfraßkorrosion beginnt sofort
- Kontaktkorrosion mit Edelstahl/Kupfer → Alu opfert sich
- Weißer Korrosionsbelag = Al₂O₃, strukturell noch OK
- Tiefe Gruben/Durchbrüche → Rahmen ersetzen

**Bronze:**
- Bildet natürliche Patina (Cu₂O → CuCO₃), schützt
- Entzinkung bei Messing (Zn-Anteil >15%): rötlich, porös → NUR Bronze, KEIN Messing verwenden!
- Galvanische Verträglichkeit mit Edelstahl: OK
- Galvanische Verträglichkeit mit Aluminium: NICHT OK (Bronze = kathodisch)

### 12.3 Wartungsplan

#### 12.3.1 Saisonale Wartung (Vor/Nach Saison)

| Maßnahme | Zeitaufwand | Material |
|----------|-------------|----------|
| Visuelle Inspektion aller Bullaugen | 15 min gesamt | Keine |
| Dichtungen auf Risse/Verhärtung prüfen | 5 min/Bullauge | Keine |
| Dogs/Verschlüsse fetten (Teflon-Fett) | 2 min/Bullauge | Teflon-Fett, 3 EUR |
| Scheiben reinigen + polieren | 5 min/Bullauge | Novus #1, 12 EUR/Fl. |
| Rahmen reinigen | 3 min/Bullauge | Edelstahl-Reiniger, 8 EUR |
| Drainagelöcher freihalten | 1 min/Bullauge | Draht Ø2mm |

#### 12.3.2 Mehrjahresplan

| Intervall | Maßnahme | Geschätzte Kosten |
|-----------|----------|-------------------|
| Jährlich | Saisonale Wartung (s.o.) | 30–50 EUR Material |
| 3 Jahre | Tiefeninspektion Dichtungen | 0 (Eigenleistung) |
| 5 Jahre | PMMA-Tiefenpolitur (Novus #3 → #2 → #1) | 40 EUR Material |
| 6–8 Jahre | Dichtungen ersetzen (alle Bullaugen gleichzeitig) | 15–30 EUR/Bullauge |
| 10 Jahre | PU-Dichtmasse Zustand prüfen | 0 (Eigenleistung) |
| 15 Jahre | PMMA-Scheiben prüfen, ggf. ersetzen | 50–200 EUR/Bullauge |
| 20 Jahre | Vollständige Überholung erwägen | 150–500 EUR/Bullauge |

> Confidence: `documented` (Hersteller-Wartungsanleitungen, Surveyor-Langzeitdaten, Material-Datenblätter)

---

## 13. Fehlerbild-Atlas

### Fehlerbild F-BA-01: Crazing (Spannungsrisskorrosion)

**Beschreibung:** Netzwerk aus feinen, spinnenwebartigen Mikrorissen auf der PMMA-Scheibenoberfläche. Bei Gegenlicht als milchiger Schleier sichtbar, bei Auflicht als feine weiße Linien.
**Betroffene Komponente:** PMMA-Scheibe
**Häufigkeit:** Sehr häufig (>60% aller Boote >10 Jahre)
**Schweregrad:** Mittel bis Hoch (Score 30–60/100)
**Typisches Alter:** 8–20 Jahre, beschleunigt durch falsche Reiniger
**Ursache:** UV-Degradation + mechanische Spannung + chemischer Angriff (Lösemittel, aggressive Reiniger)
**Folgen:** Sichtbehinderung, Festigkeitsverlust (bei tiefem Crazing >50% Wandstärke: SICHERHEITSRISIKO)
**Reparaturmöglichkeit:** Stadium 1–2: Auspolieren (Novus #3/#2/#1). Stadium 3: Teilweise polierbar. Stadium 4–5: Scheibe ersetzen.
**Prävention:** Spannungsfreier Einbau, nur PMMA-zugelassene Reiniger, UV-Schutzfolie, jährliche Politur.
**Diagnosemethode:** Gegenlicht-Inspektion, Polarisationsfilter (Frühstadium), Fingernagel-Kratztest (tiefes Crazing fühlt sich rau an).
**Bewertung (Score):** Stadium 1: 85/100, Stadium 2: 65/100, Stadium 3: 45/100, Stadium 4: 20/100, Stadium 5: 0/100 (sofortige Maßnahme erforderlich).
**Typische Reparaturkosten:** Politur 30–60 EUR, Scheibentausch 80–250 EUR + Einbau.
**Confidence:** `visual_high` — im Foto bei Gegenlicht eindeutig erkennbar.

### Fehlerbild F-BA-02: Vergilbung (Yellowing)

**Beschreibung:** Gelbliche bis bräunliche Verfärbung der PMMA-Scheibe, gleichmäßig oder stärker auf der Sonnenseite. Scheibe wirkt trüb und alt.
**Betroffene Komponente:** PMMA-Scheibe
**Häufigkeit:** Häufig (>40% aller PMMA-Bullaugen >12 Jahre)
**Schweregrad:** Gering bis Mittel (Score 50–75/100)
**Typisches Alter:** 10–20 Jahre, beschleunigt in Tropen/Mittelmeer
**Ursache:** UV-induzierte Photooxidation des PMMA-Polymers. Chromophore Gruppen entstehen durch Kettenabbau.
**Folgen:** Ästhetische Beeinträchtigung, leichte Lichtreduktion (10–30%), KEIN direktes Sicherheitsrisiko.
**Reparaturmöglichkeit:** Leichte Vergilbung: Tiefenpolitur kann Oberfläche aufhellen. Starke Vergilbung: Scheibe ersetzen — Verfärbung ist im Material.
**Prävention:** UV-stabilisiertes PMMA (Plexiglas GS 233), UV-Schutzfolie, Sonnenschutzabdeckungen im Hafen.
**Diagnosemethode:** Vergleich mit weißem Papier hinter Scheibe. Farbtemperaturmessung (App genügt).
**Bewertung (Score):** Leicht gelblich: 75/100, Deutlich gelb: 55/100, Stark braun-gelb: 35/100.
**Typische Reparaturkosten:** Politur 30–60 EUR, Scheibentausch 80–250 EUR + Einbau.
**Confidence:** `visual_medium` — Farbwiedergabe kameraabhängig, Weißabgleich beeinflusst Beurteilung.

### Fehlerbild F-BA-03: Dichtungsversagen (Gasket Failure)

**Beschreibung:** Dichtung ist verhärtet, gerissen, verformt oder fehlt teilweise. Wasser dringt bei Regen oder Seegang ein. Oft sichtbar als verfärbte oder zusammengedrückte Gummilippe.
**Betroffene Komponente:** EPDM-/Neopren-Dichtung
**Häufigkeit:** Sehr häufig (>70% aller Boote >8 Jahre zeigen Dichtungsverschleiß)
**Schweregrad:** Mittel bis Hoch (Score 25–55/100)
**Typisches Alter:** 5–8 Jahre (EPDM), 4–6 Jahre (Neopren)
**Ursache:** UV-Degradation, Druckverformungsrest (Compression Set), Ozon-Rissbildung, Alterung.
**Folgen:** Wassereinbruch → Innenraumschäden, Schimmelbildung, Elektronikschäden. Bei Seegang: Sicherheitsrisiko.
**Reparaturmöglichkeit:** Dichtung ersetzen. Meist als Meterware oder herstellerspezifisch erhältlich.
**Prävention:** Jährliche Sichtprüfung, Silikonfett auf Dichtung (1×/Jahr), UV-Schutz im Hafen.
**Diagnosemethode:** Fingernagel-Eindrucktest (Hart = schlecht), Rissinspektion, Wassertest mit Schlauch.
**Bewertung (Score):** Leicht verhärtet: 55/100, Rissig: 35/100, Teilweise fehlend: 15/100, Vollständig defekt: 0/100.
**Typische Reparaturkosten:** Dichtungs-Meterware 5–15 EUR/m, Einbau 30–60 min Eigenleistung.
**Confidence:** `visual_high` — Dichtungszustand auf Nahaufnahme gut erkennbar.

### Fehlerbild F-BA-04: Rahmenkorrosion (Frame Corrosion)

**Beschreibung:** Korrosionserscheinungen am Metallrahmen: Rostflecken (Edelstahl), weißer Belag/Lochfraß (Aluminium), grüne Patina (Bronze). Kann kosmetisch oder strukturell sein.
**Betroffene Komponente:** Rahmen (Edelstahl 316L, Aluminium eloxiert, Bronze)
**Häufigkeit:** Häufig bei Alu (>50% nach 10J), selten bei 316L (<15%), sehr selten bei Bronze (<5%)
**Schweregrad:** Gering (kosmetisch) bis Kritisch (strukturelle Korrosion) (Score 20–80/100)
**Typisches Alter:** Alu: 8–15 Jahre, Edelstahl: 15–25 Jahre, Bronze: 30+ Jahre
**Ursache:** Spaltkorrosion (316L), Lochfraß nach Eloxalschaden (Alu), galvanische Korrosion (falsches Materialpaar), Entzinkung (Messing).
**Folgen:** Kosmetisch → Ästhetik. Strukturell → Rahmen kann versagen, Scheibe löst sich. SICHERHEITSRISIKO bei fortgeschrittener Korrosion.
**Reparaturmöglichkeit:** Kosmetisch: Polieren, Passivierung. Strukturell: Rahmen ersetzen.
**Prävention:** Galvanische Isolierung, regelmäßiges Polieren/Konservieren, korrekte Materialwahl.
**Diagnosemethode:** Visuelle Inspektion, Magnettest (316L = nicht magnetisch), Klopftest (hohl = unterwandert).
**Bewertung (Score):** Tea Staining (kosmetisch): 80/100, Oberflächenkorrosion: 55/100, Lochfraß: 30/100, Strukturell: 10/100.
**Typische Reparaturkosten:** Polieren 20–40 EUR, Rahmen ersetzen 200–800 EUR + Einbau.
**Confidence:** `visual_high` — Korrosionsart und -grad auf Foto meist eindeutig.

### Fehlerbild F-BA-05: Dog-/Verschlussversagen (Dog/Latch Failure)

**Beschreibung:** Dog-Verschlüsse (Flügelschrauben) oder Hebelverschlüsse sind schwergängig, festkorrodiert, gebrochen oder fehlen. Bullauge lässt sich nicht mehr sicher verschließen.
**Betroffene Komponente:** Dog-Verschlüsse, Hebel, Gelenke
**Häufigkeit:** Häufig (>40% aller Boote >8 Jahre)
**Schweregrad:** Mittel bis Hoch (Score 25–55/100) — offenes Bullauge bei Seegang = GEFAHR
**Typisches Alter:** Zamak: 5–10 Jahre, Edelstahl: 15–25 Jahre (Festfressen), Bronze: 25–40 Jahre
**Ursache:** Korrosion (Zamak-Zinkfraß), Festfressen (Edelstahl auf Edelstahl), mechanischer Verschleiß, fehlende Schmierung.
**Folgen:** Bullauge nicht dicht verschließbar → Wassereinbruch bei Seegang. CE-Compliance verletzt.
**Reparaturmöglichkeit:** Schmieren (leichtgängig machen), Zamak durch Bronze/Edelstahl ersetzen, einzelne Dogs nachkaufen.
**Prävention:** Halbjährlich Teflon-Fett oder Lanolin auf Gewinde/Gelenke, Zamak-Dogs prophylaktisch ersetzen.
**Diagnosemethode:** Funktionsprüfung (öffnen/schließen), visuelle Inspektion auf Korrosion, Gewindegängigkeit prüfen.
**Bewertung (Score):** Schwergängig: 55/100, 1 Dog defekt: 35/100, Mehrere Dogs defekt: 15/100, Bullauge nicht verschließbar: 0/100.
**Typische Reparaturkosten:** Fetten 5 EUR, Ersatz-Dogs 15–60 EUR/Stück, komplett Satz 80–200 EUR.
**Confidence:** `visual_medium` — Zustand oft nur bei Funktionsprüfung beurteilbar, nicht nur optisch.

### Fehlerbild F-BA-06: Leckage (Leak)

**Beschreibung:** Wassereinbruch am Bullauge bei Regen, Spritzwasser oder Seegang. Sichtbar als Wasserflecken, -spuren oder aktiver Wasseraustritt am Innenring oder Rahmenrand.
**Betroffene Komponente:** Dichtungssystem (Dichtung + Dichtmasse + Rahmen)
**Häufigkeit:** Häufig (>35% aller Boote >10 Jahre haben mindestens ein undichtes Bullauge)
**Schweregrad:** Mittel bis Kritisch (Score 15–50/100)
**Typisches Alter:** Ab 8 Jahren (Dichtungen) bis laufend (Einbaufehler)
**Ursache:** Dichtungsverschleiß, Dichtmasse-Alterung, Rahmenkorrosion, Einbaufehler, fehlende Drainage.
**Folgen:** Feuchtigkeitsschäden, Schimmel, Holzfäule (Furniere/Schotten), Elektronikschäden, Osmose-Risiko.
**Reparaturmöglichkeit:** Dichtung tauschen, Dichtmasse erneuern, Drainage freimachen. Bei Rahmenkorrosion: Bullauge komplett ersetzen.
**Prävention:** Wartungsplan einhalten, Drainage regelmäßig prüfen, Wassertest nach Einwintern.
**Diagnosemethode:** Wassertest (Gartenschlauch 5 min), UV-Leckagesuche (Fluoreszenzfarbstoff), Feuchtigkeitsmessung Innenverkleidung.
**Bewertung (Score):** Sickern bei Starkregen: 50/100, Tropfen bei Regen: 30/100, Laufen bei Spritzwasser: 15/100, Laufen bei Fahrt: 0/100.
**Typische Reparaturkosten:** Dichtungstausch 50–100 EUR, Neuverdichtung 100–200 EUR, Kompletttausch 300–800 EUR.
**Confidence:** `visual_medium` — Wasserflecken sichtbar, Ursache erfordert Inspektion vor Ort.

### Fehlerbild F-BA-07: UV-Schaden (UV Damage)

**Beschreibung:** Kombination aus Vergilbung, Oberflächenmattierung und beginnender Materialversprödung durch UV-Strahlung. Scheibe wirkt milchig-matt, Oberfläche fühlt sich stumpf an.
**Betroffene Komponente:** PMMA-Scheibe, Kunststoff-Rahmenteile, Dichtungen
**Häufigkeit:** Häufig in Mittelmeer/Tropen (>50%), seltener in Nordeuropa (<20%)
**Schweregrad:** Gering bis Mittel (Score 45–70/100)
**Typisches Alter:** 5–10 Jahre (Tropen), 10–15 Jahre (gemäßigt)
**Ursache:** UV-A/UV-B-Strahlung spaltet Polymerketten, Photooxidation bildet chromophore Gruppen.
**Folgen:** Lichtdurchlässigkeit sinkt (bis zu 30%), Oberflächenhärte nimmt ab, Kratzempfindlichkeit steigt.
**Reparaturmöglichkeit:** Politur kann Oberfläche auffrischen (1–3 Jahre Gewinn). UV-Schutzfolie nachrüsten.
**Prävention:** UV-stabilisiertes PMMA, UV-Schutzfolie (3M, Llumar), Sonnenschutzabdeckungen im Hafen.
**Diagnosemethode:** Oberflächenglanz messen (Glossmeter), Lichtdurchlässigkeit messen, Vergleich mit neuem PMMA.
**Bewertung (Score):** Leicht matt: 70/100, Deutlich matt + leicht gelb: 55/100, Stark matt + gelb: 40/100.
**Typische Reparaturkosten:** Tiefenpolitur 30–80 EUR, UV-Folie nachrüsten 40–80 EUR/Bullauge, Scheibentausch 80–250 EUR.
**Confidence:** `visual_medium` — Mattierung auf Foto erkennbar, Schweregrad schwer quantifizierbar.

### Fehlerbild F-BA-08: Delaminierung (Delamination)

**Beschreibung:** Bei VSG-Scheiben (Verbundglas) oder laminiertem PMMA: Schichten trennen sich, sichtbar als milchige Flecken oder Blasen zwischen den Glasschichten, typisch beginnend an den Kanten.
**Betroffene Komponente:** VSG-Scheibe (PVB-Folie zwischen Glasschichten)
**Häufigkeit:** Selten (<10% der VSG-Bullaugen), häufiger in feuchtem Tropenklima
**Schweregrad:** Mittel bis Hoch (Score 25–50/100)
**Typisches Alter:** 10–20 Jahre, beschleunigt durch Kantenexposition zu Feuchtigkeit
**Ursache:** Feuchtigkeit dringt an Kanten in PVB-Folie ein → Hydrolyse → Adhäsionsverlust → Schichten trennen sich.
**Folgen:** Sichtbehinderung, Festigkeitsverlust (VSG verliert Splitterbindung), bei vollständiger Delaminierung: wie zwei Einzelscheiben.
**Reparaturmöglichkeit:** NICHT reparierbar. Scheibe muss ersetzt werden.
**Prävention:** Kanten vollständig versiegeln, Rahmen-Drainage funktionsfähig halten, Feuchtigkeitsstau vermeiden.
**Diagnosemethode:** Visuelle Inspektion (milchige Zonen an Kanten), Klopftest (delaminierte Bereiche klingen anders).
**Bewertung (Score):** Kantendelaminierung <10%: 50/100, 10–30%: 35/100, >30%: 20/100, Vollständig: 0/100.
**Typische Reparaturkosten:** VSG-Scheibe ersetzen 200–600 EUR + Einbau.
**Confidence:** `visual_high` — Delaminierung auf Foto meist eindeutig erkennbar.

### Fehlerbild F-BA-09: Gebrochener Rahmen (Cracked Frame)

**Beschreibung:** Riss oder Bruch im Metallrahmen, typisch an Scharnieranbindung, Dog-Aufnahme oder an der dünnsten Stelle des Profils. Kann durch Ermüdung, Korrosion oder Überlastung entstehen.
**Betroffene Komponente:** Rahmen (besonders Zamak-Guss, dünnes Alu-Profil)
**Häufigkeit:** Selten bei Qualitätsrahmen (<5%), häufig bei Zamak-Guss (>20% nach 10J)
**Schweregrad:** Hoch bis Kritisch (Score 5–25/100) — SICHERHEITSRISIKO
**Typisches Alter:** Zamak: 8–15 Jahre, Alu: 15–25 Jahre, Edelstahl/Bronze: >25 Jahre (selten)
**Ursache:** Zamak-Zinkfraß (interkristalline Korrosion), Ermüdung an Spannungskonzentrationen, Überlastung (zugeschlagen bei Seegang).
**Folgen:** Bullauge nicht mehr dicht, bei vollständigem Bruch: Scheibe kann sich lösen → SCHWERES SICHERHEITSRISIKO.
**Reparaturmöglichkeit:** Zamak/Alu: NICHT schweißbar → ersetzen. Edelstahl: WIG-Schweißung möglich (Fachbetrieb). Bronze: Löten/Schweißen möglich.
**Prävention:** Qualitätsrahmen wählen (kein Zamak), Überlastung vermeiden, regelmäßige Inspektion.
**Diagnosemethode:** Visuelle Inspektion, Klopftest, Farbeindringprüfung (PT) für feine Risse.
**Bewertung (Score):** Haarriss: 25/100, Sichtbarer Riss: 10/100, Durchgehender Bruch: 0/100 (SOFORT ersetzen).
**Typische Reparaturkosten:** Rahmen ersetzen 200–800 EUR + Einbau 200–500 EUR.
**Confidence:** `visual_high` — Risse auf Nahaufnahme sichtbar, Zamak-Zerfall typisches Erscheinungsbild.

### Fehlerbild F-BA-10: Fehlende Sturmblende (Missing Deadlight)

**Beschreibung:** Die innen montierbare Sturmblende (Deadlight) fehlt, ist beschädigt oder nicht mehr fixierbar. Bei Bullaugen unterhalb der Wasserlinie oder in der Aufbauseite CE-relevant.
**Betroffene Komponente:** Sturmblende (Deadlight), Befestigungsknebel
**Häufigkeit:** Häufig fehlend bei gebrauchten Booten (>30%)
**Schweregrad:** Mittel bis Kritisch (Score 20–50/100 je nach Position)
**Typisches Alter:** Unabhängig von Alter — oft bei Vorbesitzerwechsel verloren
**Ursache:** Sturmblende verloren, Knebel gebrochen, Gewinde ausgerissen, vom Vorbesitzer demontiert und nicht mitgegeben.
**Folgen:** CE-Non-Compliance bei Offshore-Yachten. Bei Scheibenbruch kein Notfall-Verschluss → Wassereinbruch.
**Reparaturmöglichkeit:** Sturmblende nachfertigen oder beim Hersteller bestellen. Universelle Sturmblenden als Notlösung.
**Prävention:** Sturmblende immer an Bord halten (in Nähe des Bullauges lagern), Befestigung jährlich prüfen.
**Diagnosemethode:** Vollständigkeitsprüfung: Sturmblende vorhanden? Passt sie? Lässt sie sich fixieren?
**Bewertung (Score):** Vorhanden & funktional: 100/100, Vorhanden aber schwergängig: 65/100, Fehlend (über WL): 40/100, Fehlend (unter WL): 15/100.
**Typische Reparaturkosten:** Nachkauf 80–300 EUR, Nachfertigung 150–500 EUR.
**Confidence:** `visual_high` — Vorhandensein/Fehlen auf Foto eindeutig.

### Fehlerbild F-BA-11: Beschlagene Doppelverglasung (Fogging Between Panes)

**Beschreibung:** Kondensat oder milchiger Film zwischen den Scheiben einer Doppelverglasung. Sichtbar als Tropfen, Nebel oder permanenter milchiger Schleier im Scheibenzwischenraum.
**Betroffene Komponente:** Doppelverglasungs-Einheit (IGU — Insulating Glass Unit)
**Häufigkeit:** Häufig bei marinen IGU >10 Jahre (>25%), sehr häufig bei nachgerüsteten IGU
**Schweregrad:** Mittel (Score 35–55/100)
**Typisches Alter:** 8–15 Jahre, beschleunigt durch Vibrationen und Temperaturwechsel
**Ursache:** Randverbund (Butyl + Polysulfid/Silikon) versagt → Feuchtigkeit dringt in Scheibenzwischenraum → Molekularsieb-Trockenmittel gesättigt → Kondensat bildet sich.
**Folgen:** Sichtbehinderung, Isolationswirkung reduziert (U-Wert steigt ~50%), ästhetische Beeinträchtigung.
**Reparaturmöglichkeit:** Theoretisch Nachtrocknung möglich (Spezialfirma), in Praxis meist Scheiben-Einheit ersetzen.
**Prävention:** Hochwertige IGU mit marinem Randverbund verwenden, mechanische Vibrationen dämpfen.
**Diagnosemethode:** Visuell eindeutig — Kondensat/Nebel zwischen Scheiben, verschwindet nicht beim Reinigen.
**Bewertung (Score):** Leichter Rand-Beschlag: 55/100, Deutlicher Nebel: 40/100, Permanenter dichter Schleier: 25/100.
**Typische Reparaturkosten:** IGU-Einheit ersetzen 300–800 EUR + Einbau.
**Confidence:** `visual_high` — auf Foto eindeutig erkennbar (Kondensat zwischen Scheiben).

### Fehlerbild F-BA-12: Spannungsriss (Stress Crack)

**Beschreibung:** Einzelner, oft gerader oder leicht gebogener Riss in der PMMA-Scheibe, ausgehend vom Rand oder einer Bohrung. Unterscheidet sich von Crazing durch Linearität und Tiefe.
**Betroffene Komponente:** PMMA-Scheibe (selten ESG — dort Totalbruch)
**Häufigkeit:** Gelegentlich (<15%), häufiger bei nachgerüsteten Bullaugen
**Schweregrad:** Hoch bis Kritisch (Score 5–30/100)
**Typisches Alter:** Kann jederzeit auftreten — oft Wochen/Monate nach Einbau (latente Spannung)
**Ursache:** Übermäßige Einbauspannung (Schrauben zu fest), thermische Spannung (Sonneneinstrahlung auf eingespannte Scheibe), Schlagbelastung, Bohrung zu nah am Rand (<2× Durchmesser).
**Folgen:** Scheibe kann bei Belastung vollständig brechen. Riss wächst unter Last weiter. SICHERHEITSRISIKO.
**Reparaturmöglichkeit:** NICHT reparierbar. Rissspitze bohren (Ø3mm) kann Wachstum stoppen (TEMPORÄR). Scheibe ersetzen.
**Prävention:** Spannungsfreie Montage, korrekte Drehmomente, Dehnungsspielraum, keine Bohrungen <2d vom Rand.
**Diagnosemethode:** Visuell eindeutig. Polarisationsfilter zeigt Spannungsfeld um Riss. Rissfortschritt markieren (Edding).
**Bewertung (Score):** Riss <30mm, nicht durch: 30/100, Riss >30mm oder durchgehend: 10/100, Riss + Vibrationen/Seegang: 0/100 (SOFORT handeln).
**Typische Reparaturkosten:** Scheibentausch 80–250 EUR + Einbau, ggf. Rahmenüberholung 100–200 EUR.
**Confidence:** `visual_high` — Risse auf Foto eindeutig, Ursachenanalyse erfordert Vor-Ort-Inspektion.

> Confidence: `documented` (Surveyor-Berichte, Hersteller-Dokumentation, ISO 12216)

---

## 14. Fehlerbehebungs-Leitfaden

### Problem 1: Bullauge leckt bei Regen

**Symptom:** Wassertropfen oder -film innen am Bullauge nach Regen.

**Diagnose-Ablauf:**

1. **Lokalisierung:** Wo genau tritt Wasser ein? Oben, unten, seitlich, überall?
   - Oben → Dichtung oder Dichtmasse oben defekt
   - Unten → Drainage verstopft, Wasser staut sich im Rahmen
   - Überall → Dichtmasse insgesamt versagt
   - Am Glas vorbei → Dichtung (Scheibe ↔ Rahmen)
   - Am Rahmen vorbei → Dichtmasse (Rahmen ↔ Rumpf)
2. **Wassertest mit Schlauch:** Gezielt einzelne Bereiche abspritzen, 2 min pro Bereich.
3. **Dichtungsprüfung:** Dichtung mit Fingernagel eindrücken. Hart / kein Rückfedern = ersetzen.
4. **Rahmenprüfung:** Rahmen bewegen (leicht drücken). Beweglich = Dichtmasse lose.
5. **Drainage prüfen:** Draht Ø2mm in Drainagelöcher → frei? Verstopft?

**Behebung:**

| Ursache | Maßnahme | Material | Zeitaufwand | Kosten |
|---------|----------|----------|-------------|--------|
| Dichtung verhärtet | Dichtung ersetzen | EPDM-Meterware | 30–60 min | 15–30 EUR |
| Drainage verstopft | Löcher freimachen | Draht, Druckluft | 10 min | 0 EUR |
| Dichtmasse lose (lokal) | Lokal nachsicken | Sikaflex-295 UV | 60 min + 48h Aushärtung | 20 EUR |
| Dichtmasse insgesamt versagt | Bullauge aus- und neu einbauen | Sikaflex-Set | 3–4h + 48h Aushärtung | 40–60 EUR |
| Scheibe gesprungen | Scheibe oder Bullauge ersetzen | Neue Scheibe/Bullauge | 2–4h | 80–500 EUR |

### Problem 2: PMMA-Scheibe trüb/milchig

**Symptom:** Sicht durch Bullauge eingeschränkt, Scheibe wirkt milchig oder matt.

**Diagnose-Ablauf:**

1. **Außenseite reinigen:** Mit PMMA-Reiniger und Mikrofasertuch reinigen. Besser? → Nur Verschmutzung.
2. **Gegenlicht-Test:** Von innen beleuchten und von außen betrachten. Netzwerk feiner Linien? → Crazing.
3. **Gleichmäßig trüb ohne Linien?** → UV-Mattierung oder chemischer Angriff.
4. **Trübung zwischen Scheiben (Doppelverglasung)?** → IGU-Versagen (Fogging).
5. **Gelbstich?** → UV-Vergilbung (s. Fehlerbild F-BA-02).

**Behebung:**

| Ursache | Maßnahme | Erfolgschance |
|---------|----------|---------------|
| Oberflächenverschmutzung | Reinigen + Politur | 100% |
| UV-Mattierung (leicht) | 3-Stufen-Politur (Novus #3→#2→#1) | 80% |
| UV-Mattierung (stark) | Maschinenpolitur + UV-Folie | 60% |
| Crazing Stadium 2 | Politur + UV-Folie | 50% (temporär) |
| Crazing Stadium 3+ | Scheibe ersetzen | 100% (neue Scheibe) |
| IGU-Fogging | IGU-Einheit ersetzen | 100% (neue IGU) |
| Chemischer Angriff | Scheibe ersetzen | 100% (neue Scheibe) |

**Politur-Anleitung (3-Stufen):**

1. **Novus #3 (Heavy Scratch Remover):** Mit weichem Baumwolltuch in kreisenden Bewegungen, 2–3 Durchgänge, leichter Druck. Milchige Rückstände sind normal.
2. **Novus #2 (Fine Scratch Remover):** Gleiches Tuch (saubere Stelle), kreisend, 2 Durchgänge. Oberfläche wird klarer.
3. **Novus #1 (Clean & Shine):** Neues Mikrofasertuch, leicht kreisend. Versiegelt Oberfläche.
4. **Ergebnis:** Oberfläche sollte klar und glänzend sein. Effekt hält 6–12 Monate.

### Problem 3: Dog-Verschluss festgefressen

**Symptom:** Dog-Verschluss (Flügelschraube) lässt sich nicht drehen, knirscht oder bricht beim Versuch.

**Diagnose-Ablauf:**

1. **Material identifizieren:** Zamak (silbrig-grau, leicht, oft gegossen), Edelstahl (schwer, glänzend), Bronze (gelblich-braun).
2. **Zamak + weißer Belag/Blasen?** → Zinkfraß (interkristalline Korrosion). NICHT mit Gewalt lösen — bricht!
3. **Edelstahl + festsitzend?** → Kaltverschweißung (Galling). Penetrieröl + Wärme.
4. **Bronze + grün?** → Patina. Meist lösbar mit Penetrieröl.

**Behebung:**

| Ursache | Maßnahme |
|---------|----------|
| Zamak-Zinkfraß | Dog ersetzen (Bronze oder 316L). Zamak-Reparatur NICHT möglich. |
| Edelstahl-Galling | 1. WD-40 / Kroil einwirken (24h). 2. Heißluft 150°C auf Mutter. 3. Vorsichtig lösen. 4. Gewinde mit Kupferpaste/Lanolin montieren. |
| Bronze-Patina | Essigsäure-Bad (10 min), dann Messing-Politur, fetten. |
| Mechanischer Verschleiß | Gewinde nachschneiden oder Dog ersetzen. |

**Prävention:** Halbjährlich alle Dogs öffnen, fetten (Teflon-Fett oder Lanolin), wieder schließen. NIEMALS Kupferpaste auf Zamak!

### Problem 4: Bullauge klappert bei Seegang

**Symptom:** Öffenbares Bullauge vibriert oder klappert im geschlossenen Zustand bei Welle/Motor.

**Diagnose-Ablauf:**

1. Alle Dogs vollständig angezogen? → Nachziehen.
2. Dichtung platt/verhärtet? → Scheibe hat Spiel im Rahmen.
3. Scharnier ausgeschlagen? → Laterales Spiel prüfen.
4. Rahmen lose in Ausschnitt? → Dichtmasse versagt.

**Behebung:**

| Ursache | Maßnahme | Kosten |
|---------|----------|--------|
| Dogs nicht fest | Nachziehen, Federscheiben unter Dogs | 5 EUR |
| Dichtung platt | Dichtung ersetzen (dickere wählen) | 15–30 EUR |
| Scharnier ausgeschlagen | Scharnierstift ersetzen, Buchse einsetzen | 20–50 EUR |
| Rahmen lose | Bullauge neu setzen (Sikaflex) | 40–80 EUR + 3h Arbeit |
| Scheibe locker im Rahmen | Scheibenklemmung prüfen, Puffer einlegen | 10–20 EUR |

### Problem 5: Kondenswasser innen am Bullauge

**Symptom:** Innen bilden sich Wassertropfen am Bullauge, besonders nachts und in der Übergangszeit. KEIN Leck — Wasser kommt von innen.

**Diagnose-Ablauf:**

1. **Leck vs. Kondensat unterscheiden:** Tropfen nur bei Temperaturunterschied innen/außen? → Kondensat. Auch bei gleichmäßiger Temperatur? → Leck (s. Problem 1).
2. **Einzelverglasung?** → Kondensat ist physikalisch unvermeidlich bei ΔT >5°C und >60% rF.
3. **Doppelverglasung beschlagen?** → Zwischen den Scheiben? IGU-Versagen. Innen? Kondensat.

**Behebung:**

| Maßnahme | Effektivität | Kosten |
|----------|-------------|--------|
| Lüften (Querlüftung herstellen) | Hoch | 0 EUR |
| Luftentfeuchter (12V, z.B. Meaco DD8L) | Hoch | 250–400 EUR |
| Anti-Kondensations-Folie auf Scheibe | Mittel | 15–30 EUR/Bullauge |
| Doppelverglasung nachrüsten | Sehr hoch | 300–800 EUR/Bullauge |
| Isoliermatte (nachts von innen) | Mittel | 20–40 EUR/Bullauge |

> Confidence: `documented` (Werft-Serviceberichte, Surveyor-Praxis, Herstellerempfehlungen)

---

## 15. FAQ — Häufig gestellte Fragen

### BA-001: Darf ich Bullaugen unter der Wasserlinie einbauen?
Ja, aber NUR mit Typzulassung (Lloyd's, DNV, BV), Sturmblende (Deadlight) PFLICHT, und das Bullauge muss als "Unterwasser-Fitting" klassifiziert sein. Für Sportboote unter CE ist dies in ISO 12216 geregelt. Ab Kategorie A/B sind Bullaugen unter der Wasserlinie ohne Sturmblende NICHT zulässig.

### BA-002: Wie oft muss ich die Dichtungen wechseln?
EPDM-Dichtungen halten 5–8 Jahre, Neopren 4–6 Jahre. Prüfen Sie jährlich mit dem Fingernagel-Eindrucktest: Wenn die Dichtung sich nicht mehr elastisch zurückformt, ist ein Wechsel fällig. Im Zweifelsfall: wechseln. Dichtungs-Meterware kostet 5–15 EUR/m.

### BA-003: Kann ich Aceton zum Reinigen von PMMA verwenden?
NEIN! NIEMALS Aceton, Verdünner, Benzin oder andere Lösemittel auf PMMA verwenden. Diese verursachen SOFORT Spannungsrisse (Crazing). Verwenden Sie ausschließlich PMMA-zugelassene Reiniger (Burnus Plexiklar, Novus #1) oder lauwarmes Wasser mit mildem Spülmittel (verdünnt!).

### BA-004: Was ist der Unterschied zwischen Bullauge und Portlight?
Im deutschen Sprachgebrauch: Bullauge = rund, Portlight = rechteckig/oval. Im englischen: Portlight/Porthole umfasst beides. Technisch unterscheiden sich die Dichtungssysteme: Bullaugen verwenden Ringdichtungen, Portlights verwenden umlaufende Profildichtungen. Die ISO 12216 unterscheidet nicht nach Form.

### BA-005: Zamak oder Bronze — was ist besser?
Bronze ist in JEDER Hinsicht überlegen: korrosionsbeständiger, langlebiger (40–60 vs. 5–10 Jahre), reparierbar. Zamak ist nur billiger in der Herstellung. Für Langfahrt oder Boote >10m ist Bronze DRINGEND empfohlen. Zamak-Bullaugen sind für Binnengewässer und Boote <10m akzeptabel.

### BA-006: Brauche ich eine Sturmblende (Deadlight)?
Für CE-Kategorie A und B: JA, für alle öffenbaren Bullaugen, die bei Krängung oder Seegang unter Wasser geraten können. Für Kategorie C/D: empfohlen, aber nicht zwingend. Unabhängig von CE: Für Langfahrt und Blauwasser ist eine Sturmblende eine essentielle Sicherheitseinrichtung.

### BA-007: Kann ich ein rundes Bullauge durch ein rechteckiges Portlight ersetzen?
Ja, aber der Ausschnitt muss vergrößert und NEU verstärkt werden. Rechteckige Ausschnitte erfordern Eckradien ≥20mm. Die strukturelle Integrität muss durch einen Fachbetrieb oder Sachverständigen beurteilt werden. Bei tragenden Strukturen (Rumpf unter WL) ist eine Neuberechnung der Festigkeit PFLICHT.

### BA-008: Wie teste ich, ob mein Bullauge dicht ist?
Wassertest mit Gartenschlauch: 5 Minuten gezielt auf das Bullauge spritzen, dabei von innen beobachten. Für präzisere Ergebnisse: Fluoreszenzfarbstoff ins Spritzwasser, mit UV-Lampe von innen suchen. NICHT mit Hochdruckreiniger testen — das entspricht nicht realen Bedingungen und kann Dichtungen beschädigen.

### BA-009: Mein Bullauge ist von innen beschlagen — ist es undicht?
Wahrscheinlich NICHT undicht, sondern Kondenswasser. Kondensat bildet sich, wenn warme, feuchte Kabinenluft auf die kältere Scheibe trifft. Abhilfe: Lüften, Entfeuchter, Isolierfolie. Bei Doppelverglasung: Kondensat ZWISCHEN den Scheiben = IGU-Versagen → Scheibe ersetzen.

### BA-010: Welches Drehmoment für die Befestigungsschrauben?
Typisch 2.5–3.5 Nm für M5-Schrauben in PMMA-Rahmen. IMMER Herstellerangabe befolgen! Zu fest = PMMA steht unter Spannung → Crazing. Zu locker = undicht. Drehmomentschlüssel ist PFLICHT, nicht "nach Gefühl".

### BA-011: Kann ich Bullaugen selbst einbauen?
Ja, mit handwerklichem Geschick und den richtigen Werkzeugen (s. Abschnitt 11). Kritische Punkte: Ausschnitt verstärken, spannungsfreie Montage, korrekte Dichtmasse (Sikaflex-295 UV). Für Bullaugen unter der Wasserlinie oder in tragenden Strukturen: Fachbetrieb beauftragen.

### BA-012: Was kostet ein Bullauge-Austausch beim Fachbetrieb?
Komplett (Material + Arbeit): 300–800 EUR pro Bullauge, je nach Größe, Material und Zugänglichkeit. Bei schwierigem Zugang (Innenverkleidung demontieren, Polster entfernen) können Zusatzkosten von 100–300 EUR anfallen. Satz von 6 Bullaugen: oft Mengenrabatt 10–15%.

### BA-013: Wie erkenne ich, ob mein Rahmen aus 316L oder 304 besteht?
Magnettest: 316L ist NICHT magnetisch (oder nur sehr schwach), 304 kann leicht magnetisch sein (nach Kaltverformung). Sicherer: Funkentest oder XRF-Analyse (Surveyor). Auf Prägung achten: "AISI 316" oder "A4" = 316. "A2" = 304. Im Zweifelsfall: Hersteller fragen.

### BA-014: Sind LED-Ringe um Bullaugen sinnvoll?
Ästhetisch optional, technisch unkritisch. LED-Ringe (12V, IP67) können als Ambientebeleuchtung eingebaut werden. ACHTUNG: Kabelführung muss wasserdicht sein, Kabel NICHT durch die Dichtungsebene führen. Stromversorgung über separaten Kanal.

### BA-015: Wie groß darf ein Bullauge maximal sein?
Theoretisch unbegrenzt, praktisch limitiert durch: Strukturfestigkeit (Ausschnitt schwächt Rumpf/Aufbau), Scheibendicke (steigt quadratisch mit Durchmesser), Gewicht, Kosten. Für GFK-Rümpfe: Ø400mm ist praktische Obergrenze für Rund-Bullaugen. Darüber: rechteckige Fenster mit Rahmenversteifung.

### BA-016: Was ist besser — PMMA oder Glas?
PMMA: leichter (50% Gewichtsersparnis), schlagfester, einfacher zu bearbeiten, günstiger. ABER: kratzempfindlich, UV-empfindlich, altert sichtbar. ESG: kratzfest, UV-beständig, altert nicht sichtbar. ABER: schwerer, teurer, bei Bruch Totalverlust (Scheibe zerfällt). Für Sportboote <15m: PMMA ist Standard. Ab 15m und Superyachts: ESG oder VSG.

### BA-017: Kann ich meine Bullaugen tönen?
Ja, drei Möglichkeiten: (1) Getöntes PMMA bestellen (Plexiglas GS 7C14, grau oder bronze), (2) Tönungsfolie aufkleben (3M FX-HP, marine-grade), (3) Polarisierende Folie. Option 1 ist die beste Lösung (dauerhaft, gleichmäßig). Folie kann sich lösen oder Blasen bilden. NIEMALS Auto-Tönungsfolie verwenden — nicht UV-stabil für Marine.

### BA-018: Wie dichte ich ein Bullauge temporär ab (Notfall auf See)?
Sturmblende einsetzen (wenn vorhanden). Sonst: von INNEN mit Sperrholzplatte + Sikaflex oder Butylband abdichten. Provisorium: Plastiktüte + Klebeband (hält nur Stunden). Für Langfahrt: Epoxy-Reparaturset + Sperrholz-Rohling in Bullauge-Größe mitführen.

### BA-019: Warum beschlagen meine neuen Doppelverglasungs-Bullaugen?
Wenn Kondensat ZWISCHEN den Scheiben: Produktionsfehler (defekter Randverbund) → Gewährleistung geltend machen. Wenn Kondensat INNEN: Normal bei hoher Luftfeuchtigkeit in der Kabine. Abhilfe: Besser lüften, Entfeuchter verwenden. Neue IGU können in den ersten Wochen leichten Innen-Beschlag zeigen — das ist kein Defekt.

### BA-020: Welche Versicherung deckt Bullaugen-Schäden?
Kaskoversicherung deckt: Bruch durch Seegang, Sturm, Kollision. NICHT gedeckt: Alterung, Verschleiß, Wartungsmängel, Crazing. Haftpflicht: nur Drittschäden. Bei Totalverlust (Sinken wegen defektem Bullauge): Kaskoversicherung kann Leistung kürzen, wenn Wartungsmangel nachgewiesen wird. Bullaugen-Zustand im Condition Survey dokumentieren!

### BA-021: Dürfen Bullaugen im Maschinenraum eingebaut werden?
Grundsätzlich ja, aber mit Einschränkungen: Bullauge MUSS fest (nicht öffenbar) sein, Feuerwiderstandsklasse beachten (ISO 9094), ESG oder VSG bevorzugt (Temperaturbeständigkeit), Mindestabstand zu Auspuff/heißen Teilen: 300mm. Bei Motorbooten >24m gelten SOLAS-Anforderungen.

### BA-022: Was bedeutet "A60" bei Bullaugen?
A60 ist eine Feuerwiderstandsklasse nach SOLAS/FTP-Code: 60 Minuten Widerstand gegen Standard-Feuereinwirkung bei maximal 180°C Temperaturanstieg auf der Abgewandten Seite. Relevant nur für kommerzielle Schiffe und Superyachts >24m (>500 GT). Für Sportboote unter CE NICHT erforderlich.

### BA-023: Wie transportiere ich Ersatz-Bullaugen sicher?
PMMA-Scheiben: Schutzfolie NICHT entfernen, in Schaumstoff einwickeln, hochkant lagern (NICHT flach stapeln mit Gewicht darauf). Komplette Bullaugen mit Rahmen: Dogs lösen, Scheibe öffnen und fixieren, Ecken mit Schaumstoff schützen. Bronzerahmen können ungeschützt transportiert werden.

### BA-024: Gibt es Bullaugen mit integrierter Lüftung?
Ja, einige Hersteller (Lewmar, Vetus) bieten Bullaugen mit integrierten Mosquitonetzen und Lüftungseinsätzen. Typisch: innerer Rahmen mit Netz-/Lüftungseinsatz, der bei geschlossenem Bullauge Luftzirkulation ermöglicht. Effektive Lüftungsfläche: ca. 30–40% der Scheibenfläche.

### BA-025: Wann sollte ein Sachverständiger die Bullaugen prüfen?
Bei Kauf eines Gebrauchtboots (IMMER — Bullaugen sind Teil der Condition Survey), nach Grundberührung oder Kollision, bei sichtbarer Korrosion an tragenden Rahmenteilen, bei Rissen in Scheiben, vor Langfahrt (Blauwasser), und alle 5 Jahre bei Booten >15m. Kosten für Bullaugen-Inspektion als Teil einer Condition Survey: 50–100 EUR (anteilig).

> Confidence: `documented` (ISO 12216, CE-Richtlinie 2013/53/EU, Surveyor-Praxis, Herstellerdokumentation)

---

## 16. Glossar

| Begriff | Definition |
|---------|-----------|
| **Acrylglas (PMMA)** | Polymethylmethacrylat, transparenter Kunststoff, Handelsname Plexiglas. Standard-Scheibenmaterial für Marine-Bullaugen. |
| **Aufbau** | Oberhalb des Decks liegende Struktur (Deckshaus, Kabinendach). Bullaugen im Aufbau unterliegen geringeren Druckanforderungen als Rumpf-Bullaugen. |
| **Blindflansch** | Nicht-transparenter Verschluss für einen Bullauge-Ausschnitt. Verwendet als temporärer oder permanenter Verschluss. |
| **Butylband** | Dauerelastisches Dichtband auf Butylkautschuk-Basis. Wird als Erstdichtung unter Flansch-Bullaugen verwendet. |
| **CE-Kategorie** | Konstruktionskategorie nach EU-Richtlinie 2013/53/EU (A=Ozean, B=Offshore, C=Küste, D=Geschützt). Bestimmt Anforderungen an Bullaugen. |
| **Compression Set** | Druckverformungsrest: permanente Verformung einer Dichtung nach langem Zusammenpressen. Maß für Dichtungsalterung (in %). |
| **Crazing** | Netzwerk aus feinen Oberflächenrissen in PMMA, verursacht durch UV + Spannung + chemischen Angriff. Häufigstes Fehlerbild. |
| **Deadlight** | Sturmblende: massive Metall- oder GFK-Platte, die von innen über ein Bullauge montiert wird. Notfall-Verschluss bei Scheibenbruch. |
| **Dog** | Flügelschraube oder Knebelgriff zum Verschließen öffenbarer Bullaugen. Typisch: 2–6 Dogs pro Bullauge. |
| **Doppelverglasung (IGU)** | Insulating Glass Unit: zwei Scheiben mit Luft-/Gasfüllung dazwischen. Verbessert Wärmedämmung und reduziert Kondensat. |
| **EPDM** | Ethylen-Propylen-Dien-Kautschuk. Standard-Dichtungsmaterial für Marine-Bullaugen. UV-beständiger als Neopren. |
| **Eloxierung** | Anodische Oxidation von Aluminium. Erzeugt schützende Oxidschicht (15–25µm). Standard-Oberflächenbehandlung für Alu-Bullaugen. |
| **ESG** | Einscheiben-Sicherheitsglas (gehärtet). Kratzfester und temperaturbeständiger als PMMA, aber schwerer und bei Bruch Totalverlust. |
| **Flansch-Montage** | Montageart, bei der das Bullauge mit einem breiten Flansch auf der Außenseite verschraubt wird. Für dicke Wände (>25mm). |
| **Galvanische Korrosion** | Elektrochemische Korrosion durch Kontakt zweier verschiedener Metalle in Elektrolyt (Salzwasser). Bronze + Alu = Problem! |
| **Gelcoat** | Polyester- oder Vinylester-Deckschicht auf GFK. Schützt Laminat vor UV und Wasser. Typische Dicke: 0.5–0.8mm. |
| **GFK** | Glasfaserverstärkter Kunststoff (Fiberglass Reinforced Plastic). Standard-Rumpfmaterial für Sportboote. |
| **Galling** | Kaltverschweißung: Edelstahl-Gewinde fressen bei Trockenreibung ohne Schmierung fest. Irreversibel. |
| **Hinterschnittanker** | Befestigungselement für dicke Wände, bei dem die Schraube hinter der Wand verankert wird. Für Flansch-Montage in Alu/Stahl. |
| **ISO 12216** | Internationale Norm für Fenster, Bullaugen, Luken und Deadlights auf Sportbooten. Definiert Druckanforderungen, Prüfverfahren und Materialstandards. |
| **Kontaktkorrosion** | = Galvanische Korrosion. Tritt auf, wenn ungleiche Metalle in Gegenwart von Salzwasser Kontakt haben. |
| **Lichtmaß** | Freier Durchlass-Durchmesser eines Bullauges (Innenmaß des Rahmens, durch den Licht fällt). |
| **Low-E** | Low-Emissivity-Beschichtung: hauchdünne Metalloxidschicht auf Glas, die Wärmestrahlung reflektiert. Reduziert U-Wert um 40–60%. |
| **Mosquitonetz** | Feines Netz (Mesh) im Innenrahmen eines öffenbaren Bullauges. Verhindert Insekteneintritt bei geöffnetem Bullauge. |
| **Neopren** | Chloropren-Kautschuk. Dichtungsmaterial, UV-empfindlicher als EPDM, aber ölbeständiger. |
| **Osmose** | Wasseraufnahme durch GFK-Laminat. Kann durch undichte Bullaugen-Ausschnitte beschleunigt werden. |
| **Passivierung** | Chemische Behandlung (Salpetersäure/Zitronensäure) von Edelstahl zur Wiederherstellung der schützenden Chromoxid-Schicht. |
| **Polarisationsfilter** | Optischer Filter zur Erkennung von Spannungen in transparenten Materialien. Diagnostik-Werkzeug für Crazing-Frühstadien. |
| **Portlight** | Rechteckiges oder ovales Fenster in Rumpf oder Aufbau. Im Englischen auch Synonym für Bullauge. |
| **PVB** | Polyvinylbutyral: Folie zwischen VSG-Scheiben, die bei Bruch die Splitter bindet. |
| **Randverbund** | Abdichtungssystem am Rand einer Doppelverglasungseinheit (Butyl + Polysulfid/Silikon). Versagen = Fogging. |
| **Shore-Härte** | Maß für die Härte von Elastomeren (Skala A für weiche Materialien). Neue EPDM-Dichtung: ~50A, alte: >70A. |
| **Sikaflex-295 UV** | PU-Dichtmasse speziell für Verglasungen. UV-beständig, elastisch, haftet auf PMMA (mit Primer). Standard für Bullauge-Montage. |
| **Spigot-Montage** | Montageart, bei der ein zylindrischer Ansatz (Spigot) des Rahmens durch den Ausschnitt gesteckt und von innen mit Gegenring verschraubt wird. Standard für GFK. |
| **Spannungsriss** | Einzelner linearer Riss in PMMA, verursacht durch mechanische Überlastung oder Einbauspannung. Nicht zu verwechseln mit Crazing (Netzwerk). |
| **Sturmblende** | = Deadlight. Massiver Innenverschluss für Notfälle (Scheibenbruch). CE-Pflicht für Kategorie A/B unter bestimmten Bedingungen. |
| **Tea Staining** | Bräunliche Verfärbung auf Edelstahl-Oberflächen in Meeresnähe. Kosmetisch, NICHT strukturell. Entfernbar durch Polieren. |
| **Toughened Glass** | = ESG (Einscheiben-Sicherheitsglas). Durch thermische Vorspannung gehärtet. |
| **VSG** | Verbund-Sicherheitsglas: zwei Glasscheiben mit PVB-Folie verklebt. Bei Bruch bleiben Splitter an der Folie haften. |
| **Zamak** | Zink-Aluminium-Legierung (Zinkdruckguss). Billig, aber korrosionsanfällig in Salzwasser. Für Marine-Anwendung minderwertig. |
| **Zinkfraß** | Interkristalline Korrosion von Zamak-Bauteilen. Material wird porös, quillt auf und zerfällt. Irreversibel. |

> Confidence: `documented` (ISO 12216, DIN-Normen, Fachliteratur Schiffbau)

---

## 17. Schnell-Referenz

### 17.1 Bullauge-Auswahl nach Bootsklasse

| Bootsklasse | Empfohlenes Material | Rahmenmaterial | Mindest-Ø | Dichtung |
|-------------|---------------------|----------------|-----------|----------|
| Jolle / Daysailer (<8m) | PMMA 6mm | Alu eloxiert | 100mm | EPDM |
| Fahrtensegler (8–12m) | PMMA 8mm | Edelstahl 316L | 150mm | EPDM |
| Blauwasser-Segler (10–15m) | PMMA 10mm / ESG 5mm | Edelstahl 316L / Bronze | 150mm | EPDM |
| Motor-Yacht (8–15m) | PMMA 8mm | Edelstahl 316L | 200mm | EPDM |
| Semi-Custom (15–20m) | ESG 6mm / VSG | Edelstahl 316L poliert | 200mm | EPDM Marine |
| Custom/Superyacht (20m+) | VSG (ESG+ESG+PVB) | Edelstahl 316L / Bronze gegossen | 250mm | EPDM Marine |

### 17.2 Kritische Maße auf einen Blick

| Parameter | Wert | Quelle |
|-----------|------|--------|
| Min. Eckradius Ausschnitt | R ≥ 20mm | Praxis |
| Min. Abstand zum nächsten Ausschnitt | ≥ 80mm (≥ 1× Ø) | ISO 12216 |
| Min. PMMA-Dicke (Ø200mm, Kat. B) | 8mm | ISO 12216 Berechnung |
| Drehmoment M5-Schrauben | 2.5–3.5 Nm | Herstellerempfehlung |
| Sikaflex-295 UV Aushärtung | 48h belastbar, 7 Tage voll | Sika Datenblatt |
| EPDM-Dichtung Lebensdauer | 5–8 Jahre | Erfahrungswert |
| Drainage Mindest-Ø | 3mm | Praxis |
| Sturmblende CE-Pflicht | Kat. A + B (unter WL) | ISO 12216 |
| Max. Bullauge-Ø (GFK-Rumpf) | ~400mm | Strukturelle Grenze |
| Spigot-Spiel im Ausschnitt | 1–1.5mm ringsum | Montagepraxis |

### 17.3 Dichtmassen-Schnellwahl

| Anwendung | Produkt | Primer | Aushärtung |
|-----------|---------|--------|------------|
| PMMA-Scheibe auf GFK | Sikaflex-295 UV | Sika-Primer 209D (auf PMMA) + Sika-Aktivator 205 (auf GFK) | 7 Tage |
| ESG-Scheibe auf GFK | Sikaflex-295 UV | Sika-Primer 209D (auf Glas) + Sika-Aktivator 205 (auf GFK) | 7 Tage |
| Rahmen auf GFK | Sikaflex-295 UV | Sika-Aktivator 205 (beidseitig) | 7 Tage |
| Rahmen auf Alu | Sikaflex-252 | Sika-Primer 209D | 5 Tage |
| Rahmen auf Stahl | Sikaflex-252 | Sika-Aktivator 205 | 5 Tage |
| Notfall-Abdichtung | Butylband 3mm | Keiner | Sofort |

---

## 18. Notfall-Ressourcen

### 18.1 Notfall: Scheibenbruch auf See

**Sofortmaßnahmen (Reihenfolge!):**

1. **Gefahr bannen:** Alle Personen aus Gefahrenbereich. Scherben sichern.
2. **Sturmblende einsetzen** (wenn vorhanden): Von innen über Öffnung, Dogs festziehen.
3. **Keine Sturmblende?** Sperrholzplatte (vorgeschnitten!) + Sikaflex oder Butylband von INNEN aufsetzen.
4. **Kein Sperrholz?** Schneidebrett, Bodenbrett, JEDE feste Platte + Klebeband/Spanngurte.
5. **Bilgenpumpe aktivieren**, falls Wasser eindringt.
6. **Kurs ändern:** Leck auf der Lee-Seite halten (Segler: Wende/Halse).
7. **Seenotmittel bereithalten**, wenn Leck nicht kontrollierbar.

**Vorbereitung (Langfahrt-Pflicht):**
- Sperrholz-Zuschnitte für alle Bullaugen-Größen mitführen
- Butylband (5m Rolle) im Notfall-Kit
- Sikaflex-Kartusche (klein, 50ml)
- Spanngurte oder Zurrbänder
- Sturmblenden IMMER an Bord (in Nähe der Bullaugen lagern)

### 18.2 Notfall: Wassereinbruch durch Bullauge bei Seegang

**Sofortmaßnahmen:**

1. **Bullauge schließen** (Dogs alle festziehen)
2. **Sturmblende einsetzen**
3. **Handtücher/Lappen** in Rahmen-Spalt stopfen (temporär)
4. **Bilgenpumpe kontrollieren**
5. **Bei anhaltendem Einbruch:** Butylband um Rahmen-Außenkante drücken (bei ruhiger See/im Hafen)

### 18.3 Wichtige Kontakte und Bezugsquellen

| Ressource | Kontakt/URL | Anmerkung |
|-----------|-------------|-----------|
| Lewmar (Hersteller) | lewmar.com | Ersatzteile direkt bestellbar |
| Vetus (Hersteller) | vetus.com | Breites Sortiment, DE-Händlernetz |
| Goiot (Hersteller) | goiot.com | Französisch, Top-Qualität |
| New Found Metals | newfoundmetals.com | Bronze-Spezialist (US, Versand EU) |
| Toplicht (Händler DE) | toplicht.de | Großes Marine-Sortiment |
| SVB (Händler DE) | svb-marine.de | Umfangreich, schneller Versand |
| Compass24 (Händler DE) | compass24.de | Preisvergleich |
| Sika Deutschland | sika.com/de | Technische Hotline für Dichtmassen |
| Evonik (Plexiglas) | plexiglas.de | PMMA-Platten in Sondermaßen |
| Lloyd's Register | lr.org | Typzulassung Marine-Bullaugen |
| DNV | dnv.com | Typzulassung, Surveyor-Netzwerk |
| BSH (Bundesamt) | bsh.de | CE-Konformität, Regulierung DE |

> Confidence: `documented` (Hersteller-Websites, Surveyor-Netzwerk, Eigene Recherche 2024/2025)

---

## ANHANG A: Normen und Regelwerke

| Norm | Titel | Relevanz für Bullaugen |
|------|-------|----------------------|
| ISO 12216:2020 | Windows, portlights, hatches, deadlights and doors — Strength and watertightness requirements | ZENTRAL — definiert alle Anforderungen |
| ISO 12217:2022 | Stability and buoyancy assessment | Gewicht und Position von Bullaugen beeinflussen Stabilität |
| ISO 11812:2020 | Watertight and quick-draining cockpits | Cockpit-Bullaugen/-Fenster |
| ISO 15085:2003 | Man-overboard prevention and recovery | Öffnungsgrößen, Handgriffe an Bullaugen |
| ISO 9094:2015 | Fire protection | Feuerwiderstand von Bullaugen-Materialien |
| EU 2013/53/EU | Recreational Craft Directive | CE-Markierung, Design-Kategorien |
| SOLAS Kap. II-2 | Fire protection, fire detection and fire extinction | Bullaugen auf Schiffen >24m / >500 GT |
| FTP Code | International Code for Fire Test Procedures | A60-Prüfung für Bullaugen |
| GL Rules | Germanischer Lloyd — Hull Structures | Strukturelle Anforderungen für Ausschnitte |

## ANHANG B: Hersteller-Vergleichstabelle

| Hersteller | Herkunft | Material Rahmen | Material Scheibe | Preisklasse | Qualität | Zielgruppe |
|------------|---------|-----------------|-----------------|-------------|----------|------------|
| Lewmar | UK | Edelstahl 316L | PMMA / ESG | Mittel–Hoch | Hoch | Fahrtensegler, Motoryachten |
| Vetus | NL | Edelstahl 316L, Alu | PMMA | Niedrig–Mittel | Mittel–Hoch | Breit, Einstieg–Mittelklasse |
| Goiot | FR | Edelstahl 316L | PMMA / ESG | Hoch | Sehr hoch | Segler, Blauwasser |
| Bomar | US | Edelstahl 316L, Alu | PMMA / ESG | Mittel | Hoch | US-Markt, Motoryachten |
| New Found Metals | US | Bronze (gegossen) | PMMA / ESG | Hoch | Sehr hoch | Blauwasser, Klassiker |
| Manship | TW | Edelstahl 316L, Bronze | PMMA / ESG | Niedrig–Mittel | Mittel | Preis-Leistung |
| Seaflo | CN | Alu, Edelstahl 304 | PMMA | Niedrig | Niedrig–Mittel | Binnenboote, Budget |
| Beckson | US | Kunststoff (ABS) | PMMA | Sehr niedrig | Niedrig | Kleine Boote, Nachrüstung |
| Freeman Marine | US | Edelstahl 316L, Alu | ESG / VSG | Sehr hoch | Premium | Superyachts, kommerziell |
| Bohamet | PL | Edelstahl 316L | ESG / VSG | Hoch | Sehr hoch | Superyachts, kommerziell |

> ⚠️ **ZU PRÜFEN (Audit):** Zeile "Manship | TW | … | Niedrig–Mittel | Preis-Leistung" widerspricht §8.9 (Manship = UK, Cowes, Premium-Bronze, GBP 300–1.200). Wahrscheinlich mit "Boman" (Taiwan, §8.7 — in dieser Tabelle sonst nicht gelistet) verwechselt. Herkunft/Positionierung nach Klärung korrigieren.

## ANHANG C: PMMA-Datenblatt (Plexiglas GS 233)

| Eigenschaft | Wert | Einheit | Prüfnorm |
|-------------|------|---------|----------|
| Dichte | 1.19 | g/cm³ | ISO 1183 |
| Zugfestigkeit | 72 | MPa | ISO 527 |
| Bruchdehnung | 4.5 | % | ISO 527 |
| E-Modul (Zug) | 3.300 | MPa | ISO 527 |
| Biegefestigkeit | 115 | MPa | ISO 178 |
| Schlagzähigkeit (Charpy) | 15 | kJ/m² | ISO 179 |
| Wärmeformbeständigkeit (HDT/B) | 100 | °C | ISO 75 |
| Lichtdurchlässigkeit | 92 | % | ISO 13468 |
| Brechungsindex | 1.49 | — | ISO 489 |
| Wasseraufnahme (24h) | 0.3 | % | ISO 62 |
| UV-Beständigkeit | Gut | — | Florida-Test |
| Brennbarkeit | B2 (normal entflammbar) | — | DIN 4102 |

## ANHANG D: Edelstahl 316L-Datenblatt

| Eigenschaft | Wert | Einheit |
|-------------|------|---------|
| Dichte | 8.0 | g/cm³ |
| Zugfestigkeit | 485 | MPa |
| Streckgrenze (0.2%) | 170 | MPa |
| Bruchdehnung | 40 | % |
| E-Modul | 193.000 | MPa |
| Härte | 217 | HB |
| Cr-Gehalt | 16.5–18.5 | % |
| Ni-Gehalt | 10.0–13.0 | % |
| Mo-Gehalt | 2.0–2.5 | % |
| C-Gehalt (max.) | 0.03 | % |
| Lochfraßbeständigkeit (PREN) | 24 | — |
| Magnetisch | Nein | — |

## ANHANG E: Dichtmassen-Vergleich

| Eigenschaft | Sikaflex-295 UV | Sikaflex-252 | Sikaflex-291i | 3M 5200 | Butylband |
|-------------|-----------------|-------------|---------------|---------|-----------|
| Typ | PU (1K) | PU (1K) | PU (1K) | PU (1K) | Butyl |
| Verwendung | Verglasung | Struktur | Unterwasser | Universal | Temporär/Erstdichtung |
| Auf PMMA? | JA (mit Primer) | NEIN | NEIN | NEIN | Bedingt |
| Auf Glas? | JA (mit Primer) | Bedingt | NEIN | Bedingt | Bedingt |
| UV-Beständigkeit | Sehr gut | Gut | Gut | Gut | Mittel |
| Elastizität | Hoch (±25%) | Mittel (±12.5%) | Hoch (±25%) | Gering (±5%) | Plastisch |
| Aushärtezeit (voll) | 7 Tage | 5 Tage | 7 Tage | 7 Tage | Sofort |
| Überlackierbar | Ja | Ja | Ja | Nein | Nein |
| Preis (310ml) | 18–25 EUR | 12–18 EUR | 14–20 EUR | 15–22 EUR | 5–8 EUR/5m |

## ANHANG F: Wartungs-Checkliste (zum Ausdrucken)

```
BULLAUGEN-WARTUNG — CHECKLISTE
Yacht: _____________ Datum: ___________
Durchgeführt von: _____________

□ Alle Bullaugen visuell inspiziert
  □ Scheiben klar, kein Crazing/Vergilbung?
  □ Dichtungen elastisch, keine Risse?
  □ Rahmen korrosionsfrei?
  □ Dogs/Verschlüsse gängig?
  □ Sturmblenden vorhanden und funktional?
  □ Drainage frei?

Einzelprüfung pro Bullauge:
Nr. | Position | Scheibe | Dichtung | Rahmen | Dogs | Dicht? | Aktion
 1  | ________ | _______ | ________ | ______ | ____ | ______ | ______
 2  | ________ | _______ | ________ | ______ | ____ | ______ | ______
 3  | ________ | _______ | ________ | ______ | ____ | ______ | ______
 4  | ________ | _______ | ________ | ______ | ____ | ______ | ______
 5  | ________ | _______ | ________ | ______ | ____ | ______ | ______
 6  | ________ | _______ | ________ | ______ | ____ | ______ | ______
 7  | ________ | _______ | ________ | ______ | ____ | ______ | ______
 8  | ________ | _______ | ________ | ______ | ____ | ______ | ______

Wassertest durchgeführt: □ Ja  □ Nein
Ergebnis: _______________________________

Nächste Wartung fällig: ___________

Unterschrift: _____________
```

## ANHANG G: Fallstudien

### Fallstudie 1: Bavaria 38 Cruiser (2008) — Crazing aller Bullaugen

**Boot:** Bavaria 38 Cruiser, Bj. 2008, 11.35m, GFK, Mittelmeer (Kroatien)
**Problem:** Alle 6 Rumpf-Bullaugen (Vetus, Edelstahl/PMMA, Ø200mm) zeigen Stadium-3-Crazing nach 14 Jahren.
**Ursache:** Einbauspannung (Schrauben zu fest, ab Werft) + intensive UV-Belastung Mittelmeer + Reinigung mit Spülmittel-Konzentrat.
**Diagnose:** Polarisationsfilter zeigt Spannungsfeld um Schraubenpunkte. Crazing-Netzwerk radiär von Schrauben ausgehend.
**Maßnahme:** Alle 6 PMMA-Scheiben getauscht (UV-stabilisiertes Plexiglas GS 233, 8mm), Drehmoment 3.0 Nm, Dehnungsspielraum 1mm.
**Kosten:** 6× Scheibe à 45 EUR + Dichtmasse 30 EUR + 8h Arbeit à 65 EUR = 820 EUR gesamt.
**Ergebnis:** Nach 3 Jahren kein erneutes Crazing. Jahrespolitur wird durchgeführt.
**Lesson Learned:** Werfteinbau ist NICHT automatisch spannungsfrei. Drehmomentschlüssel verwenden!
**Score vorher:** 40/100 | **Score nachher:** 95/100

### Fallstudie 2: Hallberg-Rassy 40 (1998) — Zamak-Zinkfraß

**Boot:** Hallberg-Rassy 40, Bj. 1998, 12.10m, GFK, Nordsee/Atlantik
**Problem:** 2 von 8 Dog-Verschlüssen (Zamak) nach 18 Jahren durch Zinkfraß zerstört. Bullaugen nicht mehr sicher verschließbar.
**Ursache:** Zamak-Druckguss in Salzwasser-Umgebung — interkristalline Korrosion (Zinkfraß). HR hat ab ca. 2005 auf Bronze umgestellt.
**Diagnose:** Dogs aufgequollen, weißer Belag, porös, beim Zudrehen abgebrochen. Spröder Bruch typisch für Zinkfraß.
**Maßnahme:** Alle 48 Dogs (8 Bullaugen × 6 Dogs) prophylaktisch durch Bronze-Dogs ersetzt (New Found Metals).
**Kosten:** 48× Bronze-Dog à 12 EUR = 576 EUR + Versand (US→DE) 85 EUR + 4h Arbeit Eigenleistung.
**Ergebnis:** Problem dauerhaft gelöst. Bronze-Dogs patinieren leicht, passen ästhetisch hervorragend zum Boot.
**Lesson Learned:** Zamak-Dogs auf Blauwasser-Booten IMMER prophylaktisch ersetzen, BEVOR sie versagen.
**Score vorher:** 25/100 | **Score nachher:** 95/100

### Fallstudie 3: Beneteau Oceanis 46.1 (2019) — Undichtes Bullauge ab Werft

**Boot:** Beneteau Oceanis 46.1, Bj. 2019, 14.09m, GFK, Ostsee
**Problem:** 1 Bullauge (Backbord, Achterkabine) tropft bei Regen ab Auslieferung.
**Ursache:** Werft-Einbaufehler: Sikaflex-Raupe unterbrochen (Luftblase), Drainage-Loch auf der Oberseite statt Unterseite.
**Diagnose:** Wassertest lokalisiert Leck auf 10-Uhr-Position. Demontage zeigt Lücke in Dichtmasse (ca. 15mm).
**Maßnahme:** Bullauge demontiert, alte Dichtmasse entfernt, neu eingesetzt mit geschlossener Sikaflex-Raupe, Drainage korrekt unten.
**Kosten:** Gewährleistung durch Werft — 0 EUR für Eigner. (Werft-intern: ca. 3h Arbeit = 195 EUR)
**Ergebnis:** Dicht. Keine weiteren Probleme nach 3 Saisons.
**Lesson Learned:** Auch bei Neubooten ALLE Bullaugen mit Wassertest prüfen VOR Abnahme.
**Score vorher:** 35/100 | **Score nachher:** 100/100

### Fallstudie 4: Oyster 56 (2005) — Bronze-Bullaugen nach 18 Jahren

**Boot:** Oyster 56, Bj. 2005, 17.09m, GFK, Blauwasser (Weltumsegelung)
**Problem:** Eigentlich kein Problem — Zustandsbericht nach 18 Jahren und 45.000 sm.
**Ursache:** N/A (keine Mängel)
**Diagnose:** Alle 10 Bullaugen (Goiot, Bronze/ESG, Ø250mm) in sehr gutem Zustand. Bronze-Patina gleichmäßig, ESG-Scheiben klar, Dichtungen 2× getauscht (2013, 2021), Dogs gängig (jährlich gefettet).
**Maßnahme:** Routine-Dichtungswechsel alle 8 Jahre, jährliche Dog-Schmierung, gelegentliche Bronze-Politur (Eigner bevorzugt Patina).
**Kosten:** 2× Dichtungswechsel à 200 EUR + jährlich 20 EUR Wartungsmaterial = 760 EUR über 18 Jahre = 42 EUR/Jahr.
**Ergebnis:** Bronze + ESG + regelmäßige Wartung = Bullaugen überleben das Boot.
**Lesson Learned:** Qualitätsmaterial (Bronze/ESG) + konsequente Wartung = niedrigste Lebenszykluskosten.
**Score vorher:** N/A | **Score aktuell:** 92/100

### Fallstudie 5: Jeanneau Sun Odyssey 440 (2020) — Doppelverglasung nachgerüstet

**Boot:** Jeanneau Sun Odyssey 440, Bj. 2020, 13.34m, GFK, Nordeuropa (Skandinavien)
**Problem:** Starkes Kondensat an allen 6 Bullaugen (Einzelverglasung PMMA) im Herbst/Winter bei Liveaboard.
**Ursache:** Einfachverglasung in kaltem Klima bei beheizter Kabine → Taupunkt auf Scheibenoberfläche.
**Diagnose:** Thermografie zeigt Oberflächentemperatur der Scheiben bei -5°C Außen / 18°C Innen: 4°C → deutlich unter Taupunkt (12°C bei 65% rF).
**Maßnahme:** 6 Bullaugen durch Doppelverglasungs-Einheiten ersetzt (2× PMMA 6mm + 12mm Luftspalt, Lewmar).
**Kosten:** 6× Doppel-Bullauge à 380 EUR + Einbau 6× 2h à 65 EUR = 3.060 EUR gesamt.
**Ergebnis:** Kondensat um 90% reduziert. Heizenergiebedarf sinkt messbar (ca. 15% Diesel-Einsparung).
**Lesson Learned:** Für Liveaboard in Nordeuropa ist Doppelverglasung keine Luxusoption, sondern notwendig.
**Score vorher:** 55/100 | **Score nachher:** 92/100

### Fallstudie 6: Swan 48 (2012) — Spannungsriss nach Eigeneinbau

**Boot:** Swan 48, Bj. 2012, 14.62m, GFK, Mittelmeer (Mallorca)
**Problem:** PMMA-Scheibe (Ø250mm, 10mm) nach Eigeneinbau innerhalb von 3 Monaten mit Spannungsriss.
**Ursache:** Eigner hat Schrauben "nach Gefühl" angezogen (ca. 6–8 Nm statt max. 3.5 Nm). Riss ausgehend von Schraubenloch, 45° zur Rahmenachse.
**Diagnose:** Polarisationsfilter zeigt extreme Spannungskonzentration um alle Schraubenpunkte. Riss durch Scheibe (80% Wandstärke).
**Maßnahme:** Neue PMMA-Scheibe eingebaut, Drehmomentschlüssel verwendet (3.0 Nm), PTFE-Unterlegscheiben unter Schrauben für gleichmäßige Kraftverteilung.
**Kosten:** Scheibe 65 EUR + Dichtmasse 20 EUR + Unterlegscheiben 5 EUR + 3h Arbeit Eigenleistung.
**Ergebnis:** Kein erneuter Riss nach 2 Jahren. Eigner hat Drehmomentschlüssel gekauft (30 EUR — beste Investition).
**Lesson Learned:** Drehmomentschlüssel ist PFLICHT bei PMMA-Montage. "Nach Gefühl" ist IMMER zu fest.
**Score vorher:** 10/100 | **Score nachher:** 95/100

### Fallstudie 7: Grand Banks 42 (1985) — Korrodierte Alu-Rahmen

**Boot:** Grand Banks 42, Bj. 1985, 12.80m, GFK, Karibik
**Problem:** 4 von 8 Alu-Rahmen (eloxiert) zeigen fortgeschrittene Lochfraß-Korrosion nach 35 Jahren in tropischem Klima.
**Ursache:** Eloxalschicht nach ~20 Jahren aufgebraucht, Salzwasser + UV + Wärme beschleunigen Korrosion. Kontaktkorrosion an Edelstahl-Schrauben (ohne Isolierung).
**Diagnose:** Weißer Korrosionsbelag mit tiefen Gruben (bis 2mm), Rahmenquerschnitt um 30% reduziert. Strukturell NICHT mehr tragfähig.
**Maßnahme:** Alle 8 Bullaugen durch neue ersetzt (Lewmar, Edelstahl 316L / ESG, Ø250mm). PTFE-Isolierscheiben an allen Schraubpunkten.
**Kosten:** 8× Bullauge à 320 EUR + Einbau 8× 3h à 55 EUR = 3.880 EUR gesamt.
**Ergebnis:** Boot optisch und technisch aufgewertet. ESG statt PMMA eliminiert Crazing-Risiko in Tropen.
**Lesson Learned:** Alu-Rahmen in Tropenklima IMMER mit Isolierscheiben montieren. Nach 20 Jahren: Austausch einplanen.
**Score vorher:** 15/100 | **Score nachher:** 98/100

### Fallstudie 8: Lagoon 42 (2021) — Fehlende Sturmblenden bei Überführung

**Boot:** Lagoon 42, Bj. 2021, 12.80m, GFK-Katamaran, Biskaya-Überführung
**Problem:** Bei der Überführung Frankreich → Deutschland (Biskaya, November) wurde entdeckt, dass keine Sturmblenden an Bord waren. CE-Kategorie A.
**Ursache:** Werft liefert Sturmblenden separat verpackt — bei Übergabe vergessen/nicht übergeben.
**Diagnose:** 6 öffenbare Bullaugen ohne Sturmblenden. CE-Non-Compliance für Kategorie A. Kein akuter Defekt, aber Risiko bei Scheibenbruch.
**Maßnahme:** Überführung verschoben bis Sturmblenden geliefert. Werft lieferte innerhalb 2 Wochen nach. Alle Sturmblenden getestet und Lagerplätze markiert.
**Kosten:** 0 EUR (Gewährleistung) + 2 Wochen Liegegebühr Marina 280 EUR.
**Ergebnis:** Vollständige CE-Compliance hergestellt. Sturmblenden griffbereit verstaut.
**Lesson Learned:** Bei Neuboot-Übernahme: Sturmblenden-Vollständigkeit in Abnahme-Checkliste! IMMER prüfen.
**Score vorher:** 40/100 | **Score nachher:** 100/100

> Confidence: `documented` (Reale Fälle, anonymisiert, Surveyor-Berichte 2020–2025)

## ANHANG H: Prüfprotokoll-Vorlage (ISO 12216)

```
BULLAUGE-PRÜFPROTOKOLL nach ISO 12216
========================================
Boot: _______________ Bau-Nr.: ___________
Prüfer: _____________ Datum: _____________
Bullauge-Nr.: _____ Position: _____________
Hersteller: _________ Modell: _____________
Typ: □ Fest  □ Öffenbar  □ Öffenbar + Deadlight

DRUCKPRÜFUNG:
  Design-Druck Pd: _______ kPa
  Prüfdruck (1.5 × Pd): _______ kPa
  Dauer: 5 min
  Ergebnis: □ Bestanden  □ Nicht bestanden
  Verformung: _______ mm (max. zulässig: D/250)
  Bleibende Verformung: _______ mm (max: 0)

DICHTHEITSPRÜFUNG:
  Wassertest: □ Bestanden  □ Nicht bestanden
  Lufttest (bei UW-Bullaugen): □ Bestanden  □ Nicht bestanden

MECHANISCHE PRÜFUNG:
  Dogs gängig: □ Ja  □ Nein
  Scharnier fest: □ Ja  □ Nein
  Deadlight montierbar: □ Ja  □ Nein  □ N/A
  Drehmoment Schrauben: _______ Nm

ZUSTANDSBEWERTUNG:
  Scheibe: ________________ Score: ___/100
  Dichtung: _______________ Score: ___/100
  Rahmen: _________________ Score: ___/100
  Verschlüsse: ____________ Score: ___/100
  Gesamt: _________________ Score: ___/100

Bemerkungen: ___________________________________
Nächste Prüfung fällig: ___________
Unterschrift: _____________
```

## ANHANG I: Gewichtsvergleich

| Bullauge-Typ (Ø200mm) | Gewicht komplett (g) | Gewicht Scheibe (g) | Gewicht Rahmen (g) |
|------------------------|---------------------:|--------------------:|-------------------:|
| Alu/PMMA 8mm (Vetus) | 680 | 95 | 520 |
| Edelstahl 316L/PMMA 8mm (Lewmar) | 1.250 | 95 | 1.080 |
| Bronze/PMMA 8mm (New Found Metals) | 1.850 | 95 | 1.680 |
| Edelstahl 316L/ESG 5mm (Lewmar) | 1.420 | 245 | 1.080 |
| Bronze/ESG 5mm (Goiot) | 2.050 | 245 | 1.680 |
| Kunststoff ABS/PMMA 6mm (Beckson) | 280 | 70 | 160 |

> Gewichtsdifferenz 6 Bullaugen: Alu/PMMA vs. Bronze/ESG = (2.050 - 680) × 6 = 8.220g ≈ 8.2 kg Mehrgewicht.

## ANHANG J: Temperaturbeständigkeit

| Material | Min. Temp. (°C) | Max. Temp. (°C) | Anmerkung |
|----------|:---------------:|:---------------:|-----------|
| PMMA (Plexiglas GS) | -40 | +70 | Ab +80°C: Verformung beginnt |
| ESG | -40 | +200 | Thermische Vorspannung bleibt bis 280°C |
| VSG (mit PVB) | -30 | +60 | PVB wird ab +70°C weich |
| EPDM-Dichtung | -50 | +120 | Optimal -30 bis +80°C |
| Neopren-Dichtung | -40 | +100 | Optimal -20 bis +70°C |
| Sikaflex-295 UV | -40 | +90 | Dauertemperatur max. +70°C |
| Butylband | -30 | +80 | Wird bei >60°C weich (fließt) |
| Edelstahl 316L | -200 | +800 | Für Bullaugen irrelevant |
| Bronze (CuSn) | -200 | +400 | Für Bullaugen irrelevant |
| Aluminium 6082 | -200 | +200 | Festigkeitsverlust ab 150°C |

## ANHANG K: Schrauben-Spezifikation

| Anwendung | Material | Größe | Drehmoment (Nm) | Anzahl (Ø200mm) | Anzahl (Ø300mm) |
|-----------|----------|-------|:---------------:|:---------------:|:---------------:|
| Spigot-Montage (Standard) | A4 (316) | M5×20 | 2.5–3.5 | 6 | 8 |
| Spigot-Montage (dicke Wand) | A4 (316) | M5×30 | 2.5–3.5 | 6 | 8 |
| Flansch-Montage (GFK) | A4 (316) | M6×25 | 4.0–5.0 | 8 | 12 |
| Flansch-Montage (Alu) | A4 (316) + PTFE-Hülse | M6×30 | 4.0–5.0 | 8 | 12 |
| Flansch-Montage (Stahl) | A4 (316) | M6×25 | 5.0–6.0 | 8 | 12 |
| Deadlight-Knebel | A4 (316) / Bronze | M8 | 6.0–8.0 | 2–4 | 2–4 |

> IMMER Isolierscheiben (PTFE oder Nylon) verwenden bei Alu-Rahmen mit Edelstahl-Schrauben!

## ANHANG L: Reinigungsmittel-Kompatibilität

| Reinigungsmittel | PMMA | ESG | Edelstahl | Alu (eloxiert) | Bronze | EPDM |
|-----------------|:----:|:---:|:---------:|:--------------:|:------:|:----:|
| Wasser + mildes Spülmittel | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Novus #1 (Clean & Shine) | ✓ | ✓ | — | — | — | — |
| Novus #2 (Fine Scratch) | ✓ | — | — | — | — | — |
| Novus #3 (Heavy Scratch) | ✓ | — | — | — | — | — |
| Isopropanol | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Aceton | ✗✗✗ | ✓ | ✓ | ✓ | ✓ | ✗ |
| Essig (5%) | ✗ | ✓ | ✗ | ✗ | ✓ | ✓ |
| Edelstahl-Reiniger | — | — | ✓ | ✗ | ✗ | — |
| Hochdruckreiniger | ✗ | ✓ | ✓ | ✓ | ✓ | ✗ |
| Salzsäure | ✗✗✗ | ✗ | ✗✗✗ | ✗✗✗ | ✗ | ✗ |

Legende: ✓ = geeignet, — = nicht relevant, ✗ = nicht empfohlen, ✗✗✗ = ZERSTÖREND

## ANHANG M: Öffnungswinkel und Lüftungseffizienz

| Öffnungsmechanismus | Max. Winkel | k_öffnung | Regenschutz | Einbruchschutz |
|---------------------|:----------:|:---------:|:-----------:|:--------------:|
| Klappbar nach außen (oben) | 90° | 0.65 | Gering | Gering |
| Klappbar nach außen (seitlich) | 90° | 0.65 | Mittel | Gering |
| Klappbar nach innen | 90° | 0.60 | Keiner | Mittel |
| Klappbar begrenzt | 45° | 0.35 | Gut | Gut |
| Schiebbar | 50% Fläche | 0.50 | Gut | Mittel |
| Festverglast | 0° | 0.00 | Perfekt | Perfekt |

## ANHANG N: CE-Kennzeichnungspflicht Bullaugen

| Kriterium | Pflicht? | Anmerkung |
|-----------|:--------:|-----------|
| Neubau Sportboot 2.5–24m (EU-Verkauf) | JA | EU-Richtlinie 2013/53/EU |
| Umbau/Nachrüstung (wesentliche Änderung) | JA | Wenn Struktur betroffen |
| Eigenimport aus Nicht-EU | JA | Importeur wird Hersteller |
| Gewerbliche Schiffe | NEIN | Andere Regelwerke (SOLAS, Flaggenstaatregeln) |
| Historische/klassische Boote (Bestand) | NEIN | Bestandsschutz |
| Binnengewässer-Fahrzeuge | BEDINGT | Je nach Flaggenstaat |

## ANHANG O: Bullauge-Positionen — Typische Anordnung

```
Segelboot 12m (Seitenansicht, Steuerbord):
                    _______________
                   /  Aufbau      \
        ┌────────/────────────────\────────┐
        │  ⊕   ⊕  │  ⊕   ⊕  │  ⊕   ⊕  │     ← Aufbau-Bullaugen (über Deck)
  ~~~~~~│═══════════════════════════════════│~~~~~~  Wasserlinie
        │     ◉        ◉        ◉        │     ← Rumpf-Bullaugen (unter Deck)
        └─────────────────────────────────┘

⊕ = Aufbau-Bullauge (Pd_Aufbau)
◉ = Rumpf-Bullauge (Pd_Rumpf, höhere Anforderungen)

Typische Zuordnung:
- Bugkabine: 2× ◉ Rumpf (Ø150–200mm)
- Salon: 4× ⊕ Aufbau (Ø200–250mm)
- Achterkabine: 2× ◉ Rumpf (Ø150–200mm)
- Nasszelle: 1× ⊕ Aufbau (Ø150mm, fest oder klappbar)
- Pantry: 1× ⊕ Aufbau (Ø200mm, klappbar empfohlen)
```

## ANHANG P: Kostenvergleich Lebenszyklus (20 Jahre)

| Variante | Anschaffung | Wartung (20J) | Ersatzteile (20J) | Gesamt (20J) | EUR/Jahr |
|----------|:----------:|:------------:|:-----------------:|:------------:|:--------:|
| Budget (Alu/PMMA, Seaflo) | 80 EUR | 200 EUR | 160 EUR (2× Scheibe) | 440 EUR | 22 EUR |
| Standard (Edelstahl/PMMA, Vetus) | 180 EUR | 300 EUR | 120 EUR (1× Scheibe, 2× Dichtung) | 600 EUR | 30 EUR |
| Premium (Edelstahl/ESG, Lewmar) | 350 EUR | 200 EUR | 60 EUR (2× Dichtung) | 610 EUR | 31 EUR |
| Top (Bronze/ESG, Goiot) | 550 EUR | 150 EUR | 60 EUR (2× Dichtung) | 760 EUR | 38 EUR |

> **Erkenntnis:** Die Lebenszykluskosten unterscheiden sich weniger als die Anschaffungskosten vermuten lassen. Budget-Bullaugen sind langfristig NICHT signifikant günstiger.

## ANHANG Q: Visueller Bewertungsleitfaden für AYDI-Vision

```
Für die automatische Bildanalyse (Pipeline B) gelten folgende Erkennungsregeln:

SCHEIBENZUSTAND:
- Klar, reflektierend → Score 90–100, Confidence visual_high
- Leicht matt, minimal Crazing → Score 65–80, Confidence visual_medium
- Deutlich trüb/gelb, sichtbares Crazing → Score 35–60, Confidence visual_high
- Stark beschädigt, Risse → Score 0–30, Confidence visual_high

RAHMENZUSTAND:
- Glänzend, gleichmäßig → Score 90–100, Confidence visual_high
- Leichte Verfärbung, minimale Korrosion → Score 65–80, Confidence visual_medium
- Deutliche Korrosion, Verfärbung → Score 35–60, Confidence visual_high
- Schwere Korrosion, strukturelle Schäden → Score 0–30, Confidence visual_high

DICHTUNGSZUSTAND (schwer visuell beurteilbar):
- Sichtbar intakt, gleichmäßig → Score 70–90, Confidence visual_low
- Sichtbar zusammengedrückt/verformt → Score 40–60, Confidence visual_medium
- Sichtbar rissig/fehlend → Score 0–30, Confidence visual_high

EINBAUQUALITÄT:
- Saubere Dichtnaht, symmetrisch → Score 85–100, Confidence visual_medium
- Unsaubere Dichtnaht, Überschuss → Score 50–70, Confidence visual_medium
- Fehlende Dichtnaht, Spalte sichtbar → Score 0–40, Confidence visual_high
```

## ANHANG R: Änderungshistorie

| Version | Datum | Änderung | Autor |
|---------|-------|----------|-------|
| 1.0 | 2025-01 | Erstfassung: Grundlagen, Typen, Materialien | AYDI-Team |
| 1.1 | 2025-02 | Ergänzung: Bewertungsmatrix, Herstellervergleich | AYDI-Team |
| 1.2 | 2025-03 | Ergänzung: Einbau-Anleitung, Fehlerbild-Atlas | AYDI-Team |
| 2.0 | 2025-04 | Vollständige Erweiterung: ISO-Berechnungen, FAQ, Glossar, Anhänge A–R | AYDI-Team |

> Confidence: `documented` (Zusammenstellung aus ISO-Normen, Hersteller-Dokumentation, Surveyor-Erfahrung, Fachliteratur)
