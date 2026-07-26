# 08.05 — Luken- und Fensterdichtungen: Vollständige Wissensreferenz

> **AYDI Wissensdatei 08.05** — Kategorie 8: Luken, Fenster und Dichtungssysteme
> **Confidence-Quelle:** measured (Hersteller-TDS), documented (Hersteller-Kataloge, ISO-Normen), estimated (Erfahrungswerte)
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

### 1.1 Bedeutung von Luken- und Fensterdichtungen

Luken- und Fensterdichtungen bilden die primäre Barriere gegen Wassereinbruch durch Decksöffnungen. Im Gegensatz zu strukturellen Verbindungen (Rumpf-Deck-Verbindung, Kiel-Rumpf-Verbindung) sind Dichtungen bewegliche Verschleißteile mit begrenzter Lebensdauer. Ihre Funktion unterliegt permanenter Degradation durch UV-Strahlung, Ozon, Kompression, Salzwasser und mechanische Belastung.

**Statistische Relevanz:**
- 38% aller Wassereinbrüche auf Yachten <15m gehen auf versagende Luken-/Fensterdichtungen zurück (Confidence: documented, Quelle: Pantaenius Schadensstatistik 2019–2023)
- 22% der Gewährleistungsfälle bei Neubooten betreffen undichte Luken oder Fenster in den ersten 24 Monaten (Confidence: estimated, Quelle: SVB Kundenservice-Auswertung)
- Durchschnittlicher Schadensbetrag bei Folgeschäden durch undichte Luken: EUR 2.800–8.500 (Confidence: estimated)
- Kosten für präventiven Dichtungstausch: EUR 15–180 pro Luke je nach Hersteller und Größe (Confidence: measured)

### 1.2 Abgrenzung zu verwandten Wissensdateien

| Wissensdatei | Thema | Abgrenzung zu 08.05 |
|-------------|-------|---------------------|
| 01.01 | Luken-Dichtungen (Dichtungsmaterial) | Fokus auf Dichtungsprofil-Material und -Eigenschaften |
| 01.02 | Fenster-Dichtungen | Fokus auf Fensterdichtungen als Bauteil |
| 01.04 | Niedergangs-Dichtungen | Dichtungen an Niedergang/Companionway |
| 02.01–02.08 | Dichtstoffe und Kleber | Vergussmassen, keine Profildichtungen |
| 08.01 | Decksluken | Luken als Gesamtbauteil inkl. Mechanik, Rahmen, Linse |
| 08.02 | Bullaugen | Bullaugen als Gesamtbauteil |
| 08.03 | Windschutzscheiben | Windschutzscheiben als Gesamtbauteil |
| **08.05** | **Luken- und Fensterdichtungen** | **Dichtungssystem als Ganzes: Profil + Nut + Anpressung + Austausch + Diagnose** |

Die vorliegende Datei 08.05 behandelt Dichtungen als **Systemkomponente** — also das Zusammenspiel von Dichtungsprofil, Nutgeometrie, Anpressmechanismus, Oberflächenbeschaffenheit der Dichtflächen und Einbauverfahren. Sie ergänzt die materialfokussierten Dateien 01.01 und 01.02 um die systemische Perspektive.

### 1.3 Regulatorischer Rahmen

#### 1.3.1 CE-Kennzeichnung und Recreational Craft Directive 2013/53/EU

Die CE-Richtlinie definiert keine expliziten Anforderungen an Dichtungsprofile, stellt aber Anforderungen an die **Dichtheit von Öffnungen** in Abhängigkeit der Entwurfskategorie:

| Kategorie | Anforderung Luken | Anforderung Fenster | Dichtungsbezug |
|-----------|-------------------|--------------------|--------------------|
| A (Hochsee) | Wasserdicht bei Übernahme von Grünwasser, Verschlüsse mit Sicherung | Festverglast oder druckwasserdicht | Dichtung muss dynamischen Wasserdrücken >50 kPa standhalten |
| B (Offshore) | Wasserdicht bei schwerer See | Spritzwasserdicht, bedingter Wellenschlag | Dichtung muss kurzzeitigen Druckbelastungen >20 kPa standhalten |
| C (Küste) | Spritzwasserdicht | Spritzwasserdicht | Standardkompression ausreichend |
| D (Geschützt) | Regendicht | Regendicht | Minimale Anforderungen |

#### 1.3.2 ISO-Normen mit Dichtungsbezug

**ISO 12216:2020 — Fenster, Bullaugen, Luken, Deckel und Türen — Festigkeits- und Wasserdichtigkeitsanforderungen**

Dies ist die zentrale Norm für Luken- und Fensterdichtungen. Sie definiert:

- **Druckprüfung:** Prüfdruck abhängig von Einbauhöhe über Wasserlinie und Entwurfskategorie
  - Luken auf Deck, Kat. A: mind. 6 kPa (entspricht ca. 0,6 m Wassersäule)
  - Luken auf Deck, Kat. B: mind. 4 kPa
  - Fenster im Rumpf, Kat. A: 10–25 kPa je nach Höhe unter Schottendeck
  - Windschutzscheiben: 8–15 kPa je nach Kategorie und Einbauwinkel
- **Schlagprüfung:** Widerstandsfähigkeit gegen mechanische Belastung (herabfallende Gegenstände, Mannüber-Bord-Szenarien)
- **Ermüdungsprüfung:** 20.000 Öffnungs-/Schließzyklen ohne Dichtigkeitsverlust
- **Notausstiegs-Luken:** Mindestmaß 400 mm × 520 mm lichte Weite (für Flucht)
- **Temperaturzyklus:** Dichtigkeitsnachweis nach Temperaturwechsel -20°C bis +60°C

**ISO 9094:2015 — Brandschutz**

- Dichtungsmaterialien im Maschinenraum müssen selbstverlöschend sein (Relevanz für Maschinenraumluken)
- EPDM ist selbstverlöschend nach ASTM D2000 (bei entsprechender Formulierung)
- Silikon hat inhärente Flammwidrigkeit (LOI 25–35%)

**ISO 11812:2020 — Cockpits**

- Cockpit-Luken und Staukästen: Dichtungen müssen das Cockpit-Volumen vor Eindringen von Grundwasser schützen
- Ablaufdimensionierung: cockpit_volume × 2 (Sekunden) Ablaufkapazität

**ISO 15085:2003 — Mann-über-Bord-Verhütung**

- Keine direkte Dichtungsanforderung, aber: Lukendeckel auf begehbaren Flächen müssen rutschhemmend sein — Dichtungen dürfen nicht über Decksniveau herausragen und Stolperfallen bilden

#### 1.3.3 Klassifikationsgesellschaften

Für Yachten >24m (Superyachts, Commercial Yachts) gelten zusätzliche Anforderungen:

| Gesellschaft | Regelwerk | Dichtungsanforderung |
|-------------|-----------|---------------------|
| Lloyd's Register | SSC (Special Service Craft) | Dichtungen auf Wetterdeck: EPDM oder Silikon, UV-stabilisiert, Shore A 40–70 |
| Bureau Veritas | NR 500 | Druckprüfung 1,5× Betriebsdruck, Ermüdung 50.000 Zyklen |
| DNV | HSLC / Yacht Rules | Dichtungsmaterial nach ISO 3302 Toleranzklasse M2 oder besser |
| RINA | Rules for Yachts | Referenz auf ISO 12216, zusätzlich Ozonresistenz nach ISO 1431 |
| ABS | Guide for Building & Classing Yachts | Dichtungen für Wetterdecksöffnungen: Druckprüfung gemäß Load Line Convention |

#### 1.3.4 Prüfnormen für Dichtungsmaterialien

| Norm | Gegenstand | Grenzwert Marine |
|------|-----------|-----------------|
| ISO 815-1:2019 | Druckverformungsrest (Compression Set) | <25% nach 72h/23°C (EPDM), <30% (Silikon) |
| ISO 48-4:2018 | Shore-Härte | Shore A 40–70 für Kompressionsprofile |
| ISO 37:2017 | Zugfestigkeit und Bruchdehnung | >8 MPa Zugfestigkeit, >300% Bruchdehnung (EPDM) |
| ISO 188:2023 | Wärmebeständige Alterung | <15% Härtezunahme nach 168h/100°C |
| ISO 1431-1:2022 | Ozonbeständigkeit | Keine Risse nach 72h bei 50 pphm Ozon, 40°C |
| ISO 4892-2:2013 | Künstliche Bewitterung (Xenon) | <20% Eigenschaftsänderung nach 2000h |
| ASTM D2000 | Standard-Klassifikation Gummi | Marine-Dichtungen: BC (EPDM), BE (Silikon), BF (FKM) |
| DIN 7715 | Gummiformteile/-profile Toleranzen | Klasse E2 (Standardtoleranzen) für marine Profile |

---

## 2. Zukunftstechnologien

### 2.1 Selbstheilende Dichtungsmaterialien

Aktuelle Forschung an Polymeren mit intrinsischer Selbstheilung durch Diels-Alder-Reaktionen oder supramolekulare Netzwerke. Potenzial für marine Anwendungen:

- **Supramolekulares EPDM:** Reversible Wasserstoffbrückenbindungen ermöglichen Reparatur kleiner Risse bei Erwärmung (50–80°C). Stand 2025: Laborstadium, TRL 3–4. Kein kommerzielles Produkt für marine Dichtungen verfügbar.
- **Mikroverkapselte Heilungsmittel:** In die Dichtungsmatrix eingebettete Kapseln mit reaktivem Harz. Bei Rissbildung platzen Kapseln und vernetzen den Riss. Stand 2025: TRL 4, Probleme mit Langzeitstabilität der Kapseln unter UV.
- **Prognose:** Frühestens 2028–2032 erste kommerzielle marine Anwendungen zu erwarten. Zunächst für statische Dichtungen (Fensterrahmen), später für dynamische Kompressionsprofile.

### 2.2 Sensorisch überwachte Dichtungen

- **Leitfähige Elastomere:** EPDM mit eingebetteten Carbon-Nanotubes oder leitfähigem Ruß. Änderung des elektrischen Widerstands zeigt Kompression, Alterung oder Rissbildung an. Firma: Cabot Corporation (Masterbatches), Parker Hannifin (Prototypen).
- **Faseroptische Sensoren:** In Dichtungsprofile eingebettete Glasfasern messen Druck und Temperatur. Superyacht-Segment: erste Pilotprojekte bei Lürssen und Feadship (2024–2025). Kosten: ca. EUR 500–2.000 pro überwachter Luke.
- **Kapazitive Feuchtesensoren:** Dünne Kupferfolien auf beiden Seiten der Dichtung messen Kapazitätsänderung bei Feuchtigkeitseintritt. Firma: Seatech (NL), Prototyp seit 2023. Kosten: ca. EUR 80 pro Luke.
- **AYDI-Integration:** Zustandsüberwachung via IoT könnte direkt in Pipeline A (structured data) einfließen — real-time Dichtungszustand als measured-Confidence.

### 2.3 Biobasierte Dichtungswerkstoffe

- **Bio-EPDM:** Ethylen aus Bioethanol (Braskem, Brasilien). Dien-Anteil weiterhin petrochemisch. CO2-Einsparung ca. 30–50%. Materialkosten: +15–25% gegenüber konventionellem EPDM. Erste Extrusionsprofile verfügbar (Metzeler, Trelleborg).
- **Bio-TPE:** Thermoplastische Elastomere auf Basis von Rizinusöl (Arkema Pebax Rnew). Shore A 40–65 erreichbar. UV-Stabilität noch nicht auf Niveau von Standard-EPDM.
- **Naturkautschuk-Blends:** NR/EPDM-Blends mit 30–50% NR-Anteil. Gute mechanische Eigenschaften, aber eingeschränkte Ozonresistenz. Nicht empfohlen für permanente UV-Exposition (Decksdichtungen).

### 2.4 Additive Fertigung (3D-Druck)

- **FDM/FFF mit TPU:** Für Prototypen und Notrepairen. Shore A 85–95 (zu hart für Kompressionsprofile). Materialien: NinjaTek NinjaFlex, Polymaker PolyFlex. Layerbinding begrenzt Dichtwirkung.
- **SLA/DLP mit Flexible Resin:** Formlabs Flexible 80A, Elastic 50A. Bessere Oberflächenqualität, aber UV-Alterung problematisch. Geeignet für Prototypen, nicht für Dauerbetrieb.
- **Silikon-3D-Druck:** ACEO (Wacker) und Spectroplast. Shore A 20–60 einstellbar. Beste Eignung für marine Einzelstücke, aber hohe Kosten (EUR 50–200 pro Meter Profil). Lieferzeit 5–10 Werktage.
- **Relevanz:** 3D-Druck ist 2025 eine Nischenlösung für Yachten mit nicht mehr lieferbaren OEM-Profilen (historische Boote, eingestellte Serien). Für Seriendichtungen unwirtschaftlich.

### 2.5 Nano-Beschichtungen für Dichtungsoberflächen

- **PTFE-Nanobeschichtung:** Reduziert Haftung des Dichtungsprofils an Acrylglas-Linsen. Produkt: Nanoproof Marine Seal Coat (DE). Applikation als Spray, Standzeit 12–18 Monate. EUR 24,90/100 ml.
- **TiO2-Photokatalytische Beschichtung:** Selbstreinigende Oberfläche, baut organische Ablagerungen (Algen, Schimmel) unter UV-Licht ab. Laborstadium für Elastomere.
- **Graphen-modifiziertes EPDM:** Verbesserte UV-Resistenz und mechanische Eigenschaften durch 0,5–2% Graphen-Zusatz. Firma: Directa Plus (IT). Erste Compound-Tests positiv, aber noch kein extrudiertes Profil für marine Anwendung am Markt.

---

## 3. Best Practices nach Revier

### 3.1 Mittelmeer (hohe UV, wenig Regen, moderate Salzbelastung)

**Hauptbelastung:** Extreme UV-Strahlung (UV-Index 8–11 im Sommer), hohe Oberflächentemperaturen (bis +85°C auf schwarzen Lukenrahmen), Ozon, seltene aber heftige Regenfälle.

**Empfehlungen:**
- **Dichtungsmaterial:** Silikon bevorzugt (überlegene UV-Beständigkeit), alternativ EPDM mit UV-Stabilisator (Carbon Black oder chemisch UV-stabilisiert)
- **Shore-Härte:** 50–60 Shore A (höhere Härte, da Wärmeausdehnung die Kompression erhöht)
- **Wartungsintervall:** Alle 12 Monate visuelle Inspektion, alle 6 Monate Silikonpflege (z.B. Lewmar Seal Care, Boeshield T-9)
- **Typische Lebensdauer:** EPDM 5–8 Jahre, Silikon 8–12 Jahre
- **Besonderheit:** Weiße oder hellgraue Dichtungen vermeiden — sie vergilben und werden spröde. Schwarzes EPDM mit Carbon-Black-Füllung ist hier überlegen.
- **Häufigster Fehler:** Luken bei Hafenaufenthalt dauerhaft geschlossen lassen. Die Kompression bei hohen Temperaturen beschleunigt den Compression Set. Empfehlung: Luken im Hafen leicht geöffnet lassen (Lüftungsstellung).

### 3.2 Nordeuropa / Ostsee / Nordsee (moderate UV, viel Regen, starke Temperaturschwankungen)

**Hauptbelastung:** Frost-Tau-Zyklen (bis -20°C), hohe Regenfrequenz, Salzsprühnebel (Nordsee), Algenbildung, Feuchtigkeit in Nutkanälen.

**Empfehlungen:**
- **Dichtungsmaterial:** EPDM (beste Frostflexibilität bis -45°C), Silikon ebenfalls gut
- **Shore-Härte:** 40–55 Shore A (weicher, da niedrige Temperaturen die Dichtung verhärten)
- **Wartungsintervall:** Alle 6 Monate Inspektion (Frühjahr und Herbst), Nutkanal reinigen und trocknen vor Winterlager
- **Typische Lebensdauer:** EPDM 7–10 Jahre, Silikon 10–15 Jahre (weniger UV-Belastung)
- **Besonderheit:** Schimmelbildung in Nutkanälen ist Hauptproblem. Empfehlung: Nutkanal mit verdünntem Essig (5%) reinigen, trocknen, Dichtung mit Silikonspray behandeln (z.B. WD-40 Specialist Silikon, Ballistol Silikon). Kein Fett oder Öl verwenden.
- **Winterlager:** Dichtungen vor dem Einwintern reinigen und mit Talkum oder Silikonspray behandeln. Luken in Lüftungsstellung arretieren. Persenning darf nicht direkt auf Dichtungen aufliegen (Kondenswasser).

### 3.3 Tropen / Karibik (extreme UV, hohe Feuchtigkeit, Regen, biologischer Bewuchs)

**Hauptbelastung:** Ganzjährig extreme UV (UV-Index 10–14), permanente Feuchtigkeit 70–95% rH, Schimmel- und Algenbefall, Insektenbefall in Nutkanälen, tropische Regenfälle.

**Empfehlungen:**
- **Dichtungsmaterial:** Silikon zwingend empfohlen (UV + Schimmelresistenz). EPDM nur mit Premium-UV-Schutz und Fungizid-Zusatz.
- **Shore-Härte:** 45–55 Shore A
- **Wartungsintervall:** Alle 3 Monate Inspektion und Reinigung, alle 6 Monate Silikonpflege
- **Typische Lebensdauer:** EPDM 3–5 Jahre, Silikon 6–10 Jahre
- **Besonderheit:** Fungizid-Zusätze in der Dichtungsmischung verlängern die Lebensdauer signifikant. Produkt: Lewmar mit Microban-Technologie (seit 2019 in der Ocean-Serie). Alternativ: regelmäßige Behandlung mit Star Brite Mildew Stain Remover (chlorfrei).
- **Insektenbefall:** In der Karibik nisten Wespen und Termiten in Hohlprofilen. Empfehlung: Offene Profilenden mit Silikon verschließen.

### 3.4 Hohe Breiten / Arktis / Antarktis (extreme Kälte, geringe UV, Eisbelastung)

**Hauptbelastung:** Dauerfrost (-30°C bis -50°C), mechanische Eisbelastung, geringe UV.

**Empfehlungen:**
- **Dichtungsmaterial:** Silikon (Tieftemperatur-Sorten bis -60°C, z.B. Wacker Elastosil R 401/60) oder Spezial-EPDM (tieftemperaturbeständig bis -50°C)
- **Shore-Härte:** 35–45 Shore A (möglichst weich, bleibt bei Kälte elastisch)
- **Besonderheit:** Standard-EPDM (bis -40°C) reicht oft nicht. Neopren (CR) ist unter -20°C ungeeignet (wird starr). NBR vollkommen ungeeignet.
- **Eisbildung:** Luken nie zufrieren lassen — die Eisbildung in der Dichtungsnut kann das Profil zerstören. Dichtungen vor dem Zufrieren mit Silikonspray behandeln, damit sich kein Eis in der Nut bildet.

### 3.5 Trockenmarina / Trailerbetrieb

**Hauptbelastung:** Straßenvibrationen, Staub, seltener Wasserkontakt, UV bei Freilagerung.

**Empfehlungen:**
- **Dichtungsmaterial:** EPDM oder TPE (kostengünstig, Staub/UV)
- **Wartungsintervall:** Alle 12 Monate vor dem Saisonstart
- **Besonderheit:** Staubablagerungen in Nutkanälen sind abrasiv — vor jedem Saisonstart mit feuchtem Tuch auswischen. Vibrationen lösen klebefixierte Dichtungen — press-fit bevorzugt.

---

## 4. Regional Sourcing

### 4.1 Deutschland / Österreich / Schweiz (DACH)

| Lieferant | Sortiment | Lieferzeit | Besonderheit |
|-----------|----------|-----------|-------------|
| SVB (Bremen) | Lewmar, Vetus, Gebo OEM-Dichtungen | 1–3 Werktage | Größtes Sortiment marine Dichtungen im DACH-Raum |
| Toplicht (Hamburg) | Lewmar, Goiot, Vetus | 2–4 Werktage | Gute Fachberatung |
| Compass24 (Kiel) | Lewmar, Vetus, Osculati | 1–3 Werktage | Preisaggressiv, breites Sortiment |
| AWN (Hamburg) | Lewmar, Vetus | 2–5 Werktage | Auch Meterware EPDM/Silikon |
| Peters Rubber (Viersen) | Custom EPDM-Profile | 5–15 Werktage | Individuelle Extrusion ab 50m Mindestmenge |
| Meyco (Rödermark) | EPDM-Standardprofile (Meterware) | 1–3 Werktage | Nicht marine-spezifisch, aber passende Profile |
| Deventer Profile (Berleburg) | TPE/EPDM-Profile | 2–5 Werktage | Architektur-Profile, teilw. marine-kompatibel |
| Schlegel (Rosenheim) | Bürstendichtungen, EPDM | 2–4 Werktage | Für Schiebefenster und -luken |
| Rehau (Rehau) | TPE-Systeme | 3–8 Werktage | Primär Automotive/Bau, Custom marine möglich |
| Dichtungsprofi24.de | Meterware D/P/E-Profile | 1–2 Werktage | Online-Konfigurator, schnelle Lieferung |

### 4.2 Großbritannien / Irland

| Lieferant | Sortiment | Lieferzeit | Besonderheit |
|-----------|----------|-----------|-------------|
| Lewmar (Havant, Hampshire) | OEM-Dichtungen alle Lewmar-Serien | 2–5 Werktage | Direkt vom Hersteller, auch Einzel-Dichtungen |
| Houdini Marine (Portsmouth) | OEM und Aftermarket | 3–7 Werktage | Spezialist für Luken und deren Dichtungen |
| Trend Marine (Plymouth) | Fensterdichtungen, Custom Profile | 5–10 Werktage | Schwerpunkt Fenster und Windschutzscheiben |
| Sea Teach / Force 4 | Lewmar, Goiot, Houdini | 1–3 Werktage | Online und Filialnetz |
| Offshore Marine (Hamble) | Lewmar OEM, Ersatzprofile | 2–5 Werktage | Reparaturservice |
| HF Rubber (Rugby) | Custom EPDM/Silikon-Extrusion | 5–15 Werktage | Klein- und Mittelserie, marine-erfahren |

### 4.3 Niederlande / Belgien

| Lieferant | Sortiment | Lieferzeit | Besonderheit |
|-----------|----------|-----------|-------------|
| Vetus (Schiedam) | Vetus OEM-Dichtungen | 2–5 Werktage | Direkt vom Hersteller |
| Allpa Marine (Middelburg) | Multi-Marke, Meterware | 1–3 Werktage | Guter Großhandel |
| WaveMarine (Amsterdam) | Lewmar, Goiot, Vetus | 2–4 Werktage | Spezialist für Refits |
| Raboesch (Oss) | Kunststoff-Profile | 2–5 Werktage | Spezialist für Kunststoff-Extrusionen |

### 4.4 Frankreich

| Lieferant | Sortiment | Lieferzeit | Besonderheit |
|-----------|----------|-----------|-------------|
| Goiot Systems (Nantes) | OEM Goiot-Dichtungen | 3–7 Werktage | Direkt vom Hersteller, OEM-Bénéteau |
| Plastimo (Lorient) | Plastimo und Aftermarket | 2–5 Werktage | Breites Sortiment |
| Accastillage Diffusion | Multi-Marke | 1–3 Werktage | Größter franz. Marine-Händler, Filialnetz |
| USHIP | Multi-Marke | 2–4 Werktage | Filialnetz Mittelmeer/Atlantik |

### 4.5 Skandinavien

| Lieferant | Sortiment | Lieferzeit | Besonderheit |
|-----------|----------|-----------|-------------|
| Seldén (Göteborg, SE) | Seldén Luken + Dichtungen | 3–7 Werktage | OEM für skandinavische Werften |
| Rutgerson (SE) | OEM Rutgerson-Dichtungen | 5–10 Werktage | Nischen-Hersteller |
| Maritim (NO, SE, DK, FI) | Multi-Marke | 2–5 Werktage | Skandinaviens größte Kette |

### 4.6 USA / Kanada

| Lieferant | Sortiment | Lieferzeit | Besonderheit |
|-----------|----------|-----------|-------------|
| Bomar / Pompanette (Charlevoix, MI) | OEM Bomar-Dichtungen | 3–8 Werktage | Direkt vom Hersteller |
| Lewmar USA (Guilford, CT) | Lewmar OEM | 2–5 Werktage | US-Lager |
| West Marine | Multi-Marke | 1–3 Werktage | 250+ Filialen USA |
| Defender Industries (Waterford, CT) | Multi-Marke | 1–3 Werktage | Online-Spezialist, breites Sortiment |
| McMaster-Carr | Industrielle Elastomer-Profile | 1–2 Werktage | Nicht marine-spezifisch, aber passende Meterware |

### 4.7 Internationaler Online-Versand

| Lieferant | Sortiment | Lieferzeit | Besonderheit |
|-----------|----------|-----------|-------------|
| Toplicht.de | Marine-Dichtungen, EU-Versand | 3–7 Werktage (EU) | Versand in alle EU-Länder |
| SVB.de | Marine-Dichtungen, weltweiter Versand | 5–15 Werktage (weltweit) | Versand weltweit |
| Amazon (diverse Seller) | Aftermarket-Profile, Meterware | 1–5 Werktage | Qualität stark schwankend, keine Beratung |
| eBay (diverse Seller) | Gebrauchte OEM-Teile, Aftermarket | 3–10 Werktage | Für eingestellte Serien nützlich |
| AliExpress | Aftermarket-EPDM, TPE | 15–40 Werktage | Extrem günstig, aber keine marine-zertifizierten Materialien. Nur als Notlösung. |

---

## 5. Zweck dieser Wissensdatei

### 5.1 AYDI-Integration

Diese Wissensdatei dient als **Referenzdatenbank** für die AYDI-Analyse-Engine. Sie wird in folgenden Pipelines und Modulen referenziert:

**Pipeline A (Structured Data):**
- Modul `materials`: Bewertung des Dichtungsmaterials nach Eignung für Bootklasse und Revier
- Modul `compliance`: Prüfung der Dichtungseigenschaften gegen ISO 12216 und CE-Anforderungen
- Modul `service_patterns`: Erkennung typischer Verschleißmuster und Wartungsintervalle
- Modul `cost`: Kostenabschätzung für Dichtungstausch

**Pipeline B (Visual Data):**
- Modul `materials`: Erkennung von Dichtungszustand aus Fotos (Risse, Verfärbungen, Quellungen, Ablösungen)
- Modul `production`: Bewertung der Einbauqualität (Stoßstellen, Eckverbindungen, Nut-Passung)

**Pipeline C (Text Data):**
- Modul `service_patterns`: Extraktion von Dichtungsproblemen aus Servicereports und Eigner-Berichten

### 5.2 Confidence-Mapping für Dichtungsbewertung

| Datenquelle | Confidence | Typisches Szenario |
|------------|------------|-------------------|
| OEM-Datenblatt mit Profilnummer | measured | Lewmar Ocean 60, Dichtungs-PN 19901060 |
| Hersteller-Katalog ohne spezifische Prüfdaten | documented | Vetus Katalog: "EPDM, Shore A 55" |
| Forum-Konsens (>5 Berichte) | documented | "Goiot-Dichtungen nach 5 Jahren spröde" |
| Foto: klarer Befund | visual_high | Sichtbar gerissene Dichtung, >50% Umfang |
| Foto: teilweise erkennbar | visual_medium | Dichtung sichtbar, Zustand nicht eindeutig |
| Foto: schlecht erkennbar | visual_low | Dichtung nur angeschnitten im Bild, verdeckt |
| Schätzung aus Bootklasse und Alter | estimated | "Boot Bj. 2008, vermutlich EPDM, vermutlich tauschbedürftig" |
| Service-Report mit Befund | documented | "Luke undicht, Dichtung getauscht 2024" |

### 5.3 Bewertungsziele

Die AYDI-Engine bewertet Dichtungssysteme anhand folgender Kriterien:

| Kriterium | Gewicht | Score-Bereich | Ideal |
|-----------|---------|-------------|-------|
| Dichtungsmaterial-Eignung | 0.20 | 0–100 | 90–100 (EPDM/Silikon, passend für Revier) |
| Profil-Nutpassung | 0.25 | 0–100 | 95–100 (OEM-Profil in OEM-Nut) |
| Kompressionsverhalten | 0.20 | 0–100 | 90–100 (20–35% Compression Ratio) |
| Alterszustand | 0.15 | 0–100 | 85–100 (<3 Jahre, keine sichtbaren Mängel) |
| Einbauqualität | 0.10 | 0–100 | 90–100 (saubere Ecken, keine Stoßstellen) |
| Wartungszustand | 0.10 | 0–100 | 80–100 (gepflegt, Silikonpflege erkennbar) |

---

## 6. Pydantic-Modelle

### 6.1 Enumerationen

```python
"""Pydantic-Modelle für Luken- und Fensterdichtungen.

AYDI Wissensdatei 08.05 — Kategorie 8: Luken, Fenster und Dichtungssysteme.
Alle Maße in mm, Scores 0-100, Preise in EUR.
"""

from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class SealProfileType(str, Enum):
    """Dichtungsprofil-Typen für marine Luken und Fenster."""

    D_PROFILE = "d_profile"              # D-Profil (halbrundes Hohlprofil)
    P_PROFILE = "p_profile"              # P-Profil (D mit versetztem Fuß)
    E_PROFILE = "e_profile"              # E-Profil (dreifache Dichtlippe)
    OMEGA_PROFILE = "omega_profile"      # Omega-Profil (Ω-Form, hohe Kompression)
    TORPEDO_PROFILE = "torpedo_profile"  # Torpedo-Profil (zylindrischer Kopf)
    BULB_PROFILE = "bulb_profile"        # Bulb-/Knollenprofil (verdickter Kopf)
    LIP_SEAL = "lip_seal"               # Lippendichtung (flexible Lippe)
    FLAT_GASKET = "flat_gasket"          # Flachdichtung (gepresster Ring)
    HOLLOW_SQUARE = "hollow_square"      # Hohlkastenprofil (rechteckig)
    WEDGE_PROFILE = "wedge_profile"      # Keilprofil (asymmetrisch)
    CUSTOM = "custom"                    # Sonderprofil (herstellerspezifisch)


class SealMaterial(str, Enum):
    """Dichtungsmaterial-Typen."""

    EPDM = "epdm"                        # Ethylen-Propylen-Dien-Kautschuk
    EPDM_UV = "epdm_uv"                  # EPDM mit UV-Stabilisator
    EPDM_PEROXIDE = "epdm_peroxide"      # EPDM peroxidvernetzt (Premium)
    SILICONE = "silicone"                # Silikonkautschuk (VMQ/MVQ)
    SILICONE_FLUORINATED = "silicone_f"  # Fluorsilikon (FVMQ)
    NEOPRENE_CR = "neoprene_cr"          # Chloropren-Kautschuk (Neopren)
    NITRILE_NBR = "nitrile_nbr"          # Nitrilkautschuk (Acrylnitril-Butadien)
    TPE = "tpe"                          # Thermoplastisches Elastomer
    TPE_V = "tpe_v"                      # Vulkanisat-TPE (dynamisch vernetzt)
    TPO = "tpo"                          # Thermoplastisches Olefin
    PVC_FLEXIBLE = "pvc_flexible"        # Weich-PVC (veraltet)
    FKM = "fkm"                          # Fluorkautschuk (Viton)
    POLYURETHANE = "polyurethane"         # Polyurethan-Elastomer
    BUTYL_IIR = "butyl_iir"             # Butylkautschuk


class SealMountType(str, Enum):
    """Befestigungsart der Dichtung in der Nut."""

    PRESS_FIT = "press_fit"              # Formschlüssig eingepresst (Feder/Nut)
    ADHESIVE_BACKED = "adhesive_backed"  # Selbstklebend (Klebeband-Rückseite)
    BONDED = "bonded"                    # Eingeklebt (Kontaktkleber/Silikonkleber)
    SLIDE_IN = "slide_in"               # Eingeschoben (Torpedo in Kanal)
    SNAP_FIT = "snap_fit"               # Eingerastet (Widerhaken/Pfeilprofil)
    MECHANICAL = "mechanical"            # Mechanisch fixiert (Klemmprofil/Schrauben)
    VULCANIZED = "vulcanized"            # Aufvulkanisiert (OEM-Fertigung)


class SealLocation(str, Enum):
    """Einbauort der Dichtung."""

    DECK_HATCH_FOREDECK = "deck_hatch_foredeck"          # Vordeckluke
    DECK_HATCH_MIDSHIPS = "deck_hatch_midships"          # Mittelschiffsluke
    DECK_HATCH_AFT = "deck_hatch_aft"                    # Achterluke
    DECK_HATCH_FLUSH = "deck_hatch_flush"                # Flush-Luke (bündig)
    PORTLIGHT_FIXED = "portlight_fixed"                  # Bullaugenfenster fest
    PORTLIGHT_OPENING = "portlight_opening"              # Bullaugenfenster öffnend
    WINDSHIELD_FIXED = "windshield_fixed"                # Windschutzscheibe fest
    WINDSHIELD_OPENING = "windshield_opening"            # Windschutzscheibe öffnend
    COMPANIONWAY = "companionway"                        # Niedergang
    ENGINE_ROOM_HATCH = "engine_room_hatch"              # Maschinenraumluke
    LAZARETTE = "lazarette"                              # Lazarette/Stauraum
    ANCHOR_LOCKER = "anchor_locker"                      # Ankerkastenluke
    ESCAPE_HATCH = "escape_hatch"                        # Fluchtluke
    SALON_WINDOW = "salon_window"                        # Salonfenster
    HULL_WINDOW = "hull_window"                          # Rumpffenster
    CABIN_WINDOW = "cabin_window"                        # Kabinenfenster
    SKYLIGHT = "skylight"                                # Oberlicht/Skylicht


class SealConditionCode(str, Enum):
    """Zustandsbewertung der Dichtung."""

    NEW = "new"                          # Neu / wie neu
    GOOD = "good"                        # Gut, volle Funktion
    FAIR = "fair"                        # Befriedigend, leichte Alterungszeichen
    WORN = "worn"                        # Verschlissen, eingeschränkte Funktion
    DAMAGED = "damaged"                  # Beschädigt, undicht
    FAILED = "failed"                    # Versagt, kein Dichteffekt
    MISSING = "missing"                  # Fehlend
    NOT_ASSESSABLE = "not_assessable"    # Nicht beurteilbar


class ConfidenceLevel(str, Enum):
    """AYDI Confidence-Level für Dichtungsbewertung."""

    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class BoatClass(str, Enum):
    """Bootklasse für Kalibrierung der Bewertungsmaßstäbe."""

    PRODUCTION_SAIL_SMALL = "production_sail_small"      # Serienboot Segel <10m
    PRODUCTION_SAIL_MEDIUM = "production_sail_medium"    # Serienboot Segel 10-14m
    PRODUCTION_MOTOR_SMALL = "production_motor_small"    # Serienboot Motor <10m
    PRODUCTION_MOTOR_MEDIUM = "production_motor_medium"  # Serienboot Motor 10-14m
    SEMICUSTOM_SAIL = "semicustom_sail"                  # Semi-Custom Segel 12-20m
    SEMICUSTOM_MOTOR = "semicustom_motor"                # Semi-Custom Motor 12-20m
    CUSTOM_SAIL = "custom_sail"                          # Custom Segel >18m
    CUSTOM_MOTOR = "custom_motor"                        # Custom Motor >18m
    SUPERYACHT = "superyacht"                            # Superyacht >24m
```

### 6.2 SealProfileSpec — Dichtungsprofilspezifikation

```python
class SealProfileSpec(BaseModel):
    """Vollständige Spezifikation eines Dichtungsprofils.

    Dient als Input für die AYDI-Analyse-Engine (Pipeline A).
    Alle Maße in mm, Gewichte in g/m, Preise in EUR/m.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    manufacturer: str = Field(
        ...,
        description="Dichtungshersteller (z.B. 'Lewmar', 'Goiot', 'Peters Rubber')"
    )
    product_name: str = Field(
        ...,
        description="Produktbezeichnung (z.B. 'Ocean Hatch Seal', 'Profile 219')"
    )
    part_number: Optional[str] = Field(
        None,
        description="Hersteller-Teilenummer (z.B. Lewmar '19901060')"
    )
    oem_cross_reference: Optional[list[str]] = Field(
        None,
        description="Cross-Referenz zu OEM-Nummern anderer Hersteller"
    )

    # Profilgeometrie
    profile_type: SealProfileType = Field(
        ...,
        description="Profiltyp (D, P, E, Omega, Torpedo, Bulb, Lippe, Flach)"
    )
    total_height_mm: float = Field(
        ...,
        ge=2.0,
        le=50.0,
        description="Gesamthöhe des Profils in mm (Fuß bis Kopf-Oberkante)"
    )
    total_width_mm: float = Field(
        ...,
        ge=2.0,
        le=50.0,
        description="Gesamtbreite des Profils in mm"
    )
    foot_width_mm: float = Field(
        ...,
        ge=1.0,
        le=30.0,
        description="Breite des Fußes (Einsteckmaß in Nut) in mm"
    )
    foot_height_mm: float = Field(
        ...,
        ge=1.0,
        le=20.0,
        description="Höhe des Fußes in mm"
    )
    head_height_mm: float = Field(
        ...,
        ge=1.0,
        le=35.0,
        description="Höhe des Dichtkopfes über Nutoberkante in mm"
    )
    wall_thickness_mm: Optional[float] = Field(
        None,
        ge=0.5,
        le=5.0,
        description="Wandstärke bei Hohlprofilen in mm"
    )
    hollow_inner_diameter_mm: Optional[float] = Field(
        None,
        ge=1.0,
        le=30.0,
        description="Innendurchmesser bei Hohlprofilen (D-Profil) in mm"
    )

    # Nutgeometrie (Empfehlung)
    groove_width_mm: float = Field(
        ...,
        ge=1.0,
        le=25.0,
        description="Empfohlene Nutbreite in mm"
    )
    groove_depth_mm: float = Field(
        ...,
        ge=1.0,
        le=20.0,
        description="Empfohlene Nuttiefe in mm"
    )
    groove_tolerance_mm: float = Field(
        0.2,
        ge=0.05,
        le=1.0,
        description="Toleranz der Nutmaße in mm (±)"
    )

    # Material
    material: SealMaterial = Field(
        ...,
        description="Werkstoff der Dichtung"
    )
    shore_hardness_a: int = Field(
        ...,
        ge=20,
        le=90,
        description="Shore-A-Härte (typisch 40-70 für marine Kompressionsprofile)"
    )
    color: str = Field(
        "schwarz",
        description="Farbe der Dichtung (schwarz, grau, weiß, transparent)"
    )
    uv_stabilized: bool = Field(
        True,
        description="UV-Stabilisator enthalten"
    )
    food_grade: bool = Field(
        False,
        description="Lebensmittelecht (relevant für Trinkwassertank-Luken)"
    )

    # Mechanische Eigenschaften
    compression_set_pct: Optional[float] = Field(
        None,
        ge=0.0,
        le=100.0,
        description="Druckverformungsrest in % (ISO 815-1, 72h/23°C)"
    )
    tensile_strength_mpa: Optional[float] = Field(
        None,
        ge=0.0,
        le=30.0,
        description="Zugfestigkeit in MPa (ISO 37)"
    )
    elongation_at_break_pct: Optional[float] = Field(
        None,
        ge=0.0,
        le=800.0,
        description="Bruchdehnung in % (ISO 37)"
    )
    temperature_min_c: float = Field(
        -40.0,
        ge=-80.0,
        le=0.0,
        description="Minimale Einsatztemperatur in °C"
    )
    temperature_max_c: float = Field(
        120.0,
        ge=50.0,
        le=300.0,
        description="Maximale Einsatztemperatur in °C"
    )

    # Kompatibilität
    compatible_hatch_series: Optional[list[str]] = Field(
        None,
        description="Kompatible Lukenserien (z.B. ['Lewmar Ocean 20-70', 'Goiot Cristal'])"
    )
    compatible_frame_materials: list[str] = Field(
        default_factory=lambda: ["aluminum_anodized", "aluminum_painted",
                                 "stainless_316", "grp"],
        description="Kompatible Rahmenmaterialien"
    )
    mount_type: SealMountType = Field(
        SealMountType.PRESS_FIT,
        description="Befestigungsart"
    )

    # Preis und Verfügbarkeit
    price_per_meter_eur: Optional[float] = Field(
        None,
        ge=0.0,
        description="Preis pro Meter in EUR (UVP exkl. MwSt.)"
    )
    min_order_length_m: float = Field(
        1.0,
        ge=0.1,
        description="Mindestbestelllänge in Metern"
    )
    lead_time_days: Optional[int] = Field(
        None,
        ge=0,
        description="Lieferzeit in Werktagen"
    )
    availability: str = Field(
        "standard",
        description="Verfügbarkeit: 'standard', 'auf_anfrage', 'eingestellt', 'nur_oem'"
    )

    # Lebensdauer
    expected_lifespan_years: Optional[float] = Field(
        None,
        ge=0.5,
        le=25.0,
        description="Erwartete Lebensdauer in Jahren (revierabhängig)"
    )
    recommended_replacement_interval_years: Optional[float] = Field(
        None,
        ge=0.5,
        le=15.0,
        description="Empfohlenes Austauschintervall in Jahren"
    )

    # Metadaten
    data_source: str = Field(
        ...,
        description="Datenquelle (z.B. 'Lewmar TDS 2024', 'Peters Rubber Katalog 2023')"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.DOCUMENTED,
        description="Vertrauensstufe der Daten"
    )
    notes: Optional[str] = Field(
        None,
        description="Zusätzliche Hinweise"
    )
```

### 6.3 SealCondition — Zustandsbewertung einer Dichtung

```python
class SealDefect(BaseModel):
    """Einzelner Defekt an einer Dichtung."""
    model_config = {"from_attributes": True}

    defect_type: str = Field(
        ...,
        description=(
            "Defekttyp: 'riss_laengs' (Längsriss), 'riss_quer' (Querriss), "
            "'sproed' (Versprödung), 'quellung' (Material gequollen), "
            "'abloesung' (aus Nut gelöst), 'compression_set' (permanent verformt), "
            "'schimmel' (Schimmelbefall), 'verfaerbung' (Farbänderung), "
            "'abrieb' (Abrieb/Verschleiß), 'stoss_offen' (Stoßstelle offen), "
            "'ecke_offen' (Eckverbindung offen), 'falsch_montiert' (Einbaufehler), "
            "'fehlend' (Dichtung fehlt teilweise)"
        )
    )
    location_on_seal: str = Field(
        ...,
        description="Position am Dichtungsumfang (z.B. 'oben', 'unten', 'links', 'rechts', 'ecke_vl', 'stoss_achtern', '120-180_grad')"
    )
    severity: int = Field(
        ...,
        ge=0,
        le=100,
        description="Schweregrad 0 (kosmetisch) bis 100 (totaler Funktionsverlust)"
    )
    length_mm: Optional[float] = Field(
        None,
        ge=0.0,
        description="Ausdehnung des Defekts in mm (bei Rissen, Ablösungen)"
    )
    affects_watertightness: bool = Field(
        ...,
        description="Beeinträchtigt die Wasserdichtigkeit"
    )
    photo_reference: Optional[str] = Field(
        None,
        description="Referenz auf Foto-ID aus Pipeline B"
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="Vertrauensstufe der Defektbewertung"
    )


class SealCondition(BaseModel):
    """Zustandsbewertung einer einzelnen Dichtung.

    Wird erzeugt durch Pipeline A (strukturierte Daten) und/oder Pipeline B
    (visuelle Analyse). Alle Scores 0-100, höher = besser.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    seal_id: str = Field(
        ...,
        description="Eindeutige Dichtungs-ID innerhalb des Projekts (z.B. 'seal_foredeck_hatch_1')"
    )
    location: SealLocation = Field(
        ...,
        description="Einbauort der Dichtung"
    )
    associated_component_id: Optional[str] = Field(
        None,
        description="ID der zugehörigen Luke/Fenster (Referenz auf 08.01/08.02/08.03)"
    )

    # Dichtungsinformation
    profile_spec: Optional[SealProfileSpec] = Field(
        None,
        description="Zugeordnete Profilspezifikation (wenn bekannt)"
    )
    estimated_material: Optional[SealMaterial] = Field(
        None,
        description="Geschätztes Material (wenn Profil nicht exakt identifiziert)"
    )
    estimated_age_years: Optional[float] = Field(
        None,
        ge=0.0,
        le=50.0,
        description="Geschätztes Alter in Jahren"
    )
    installation_date: Optional[str] = Field(
        None,
        description="Einbaudatum (ISO 8601, wenn bekannt)"
    )

    # Zustandsbewertung
    condition_code: SealConditionCode = Field(
        ...,
        description="Gesamtzustandscode"
    )
    overall_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Gesamtscore 0-100 (100 = wie neu)"
    )
    elasticity_score: Optional[int] = Field(
        None,
        ge=0,
        le=100,
        description="Elastizitätsbewertung (Rückfederung nach Kompression)"
    )
    surface_score: Optional[int] = Field(
        None,
        ge=0,
        le=100,
        description="Oberflächenzustand (Risse, Versprödung, Verfärbung)"
    )
    adhesion_score: Optional[int] = Field(
        None,
        ge=0,
        le=100,
        description="Haftung in der Nut (kein Herausrutschen)"
    )
    compression_set_score: Optional[int] = Field(
        None,
        ge=0,
        le=100,
        description="Druckverformungsrest-Bewertung (100 = kein bleibender Set)"
    )
    corner_joint_score: Optional[int] = Field(
        None,
        ge=0,
        le=100,
        description="Eckverbindungen-Bewertung (Vulkanisiert/Geklebt)"
    )

    # Defekte
    defects: list[SealDefect] = Field(
        default_factory=list,
        description="Liste der identifizierten Defekte"
    )

    # Wasserdichtigkeit
    watertight: Optional[bool] = Field(
        None,
        description="Wasserdicht (True/False/None = nicht geprüft)"
    )
    leak_test_method: Optional[str] = Field(
        None,
        description="Prüfmethode: 'visual', 'water_hose', 'pressure_test', 'ultrasonic', 'none'"
    )
    leak_test_pressure_kpa: Optional[float] = Field(
        None,
        ge=0.0,
        description="Prüfdruck in kPa (wenn Druckprüfung)"
    )

    # Empfehlungen
    action_required: str = Field(
        "keine",
        description=(
            "Empfohlene Maßnahme: 'keine', 'beobachten', 'pflegen', "
            "'nachspannen', 'teilweise_erneuern', 'komplett_erneuern', "
            "'sofort_erneuern'"
        )
    )
    urgency: str = Field(
        "niedrig",
        description="Dringlichkeit: 'niedrig', 'mittel', 'hoch', 'kritisch'"
    )
    replacement_seal_suggestion: Optional[str] = Field(
        None,
        description="Empfohlenes Ersatzprofil (Hersteller + Teilenummer)"
    )
    estimated_replacement_cost_eur: Optional[float] = Field(
        None,
        ge=0.0,
        description="Geschätzte Kosten für Dichtungstausch (Material + Arbeit) in EUR"
    )
    estimated_labor_hours: Optional[float] = Field(
        None,
        ge=0.0,
        description="Geschätzter Arbeitsaufwand in Stunden"
    )

    # Metadaten
    assessed_by: str = Field(
        "aydi_engine",
        description="Bewerter: 'aydi_engine', 'surveyor', 'owner', 'boatyard'"
    )
    assessment_date: str = Field(
        ...,
        description="Bewertungsdatum (ISO 8601)"
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="Vertrauensstufe der Gesamtbewertung"
    )
    notes: Optional[str] = Field(
        None,
        description="Zusätzliche Anmerkungen"
    )
```

### 6.4 SealSystemAssessment — Gesamtbewertung aller Dichtungen eines Bootes

```python
class SealZoneSummary(BaseModel):
    """Zusammenfassung der Dichtungsbewertung für eine Zone."""
    model_config = {"from_attributes": True}

    zone: str = Field(
        ...,
        description="Zone: 'deck_hatches', 'portlights', 'windshield', 'companionway', 'engine_room', 'storage'"
    )
    seal_count: int = Field(
        ...,
        ge=0,
        description="Anzahl Dichtungen in dieser Zone"
    )
    average_score: float = Field(
        ...,
        ge=0.0,
        le=100.0,
        description="Durchschnittsscore dieser Zone (0-100)"
    )
    worst_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Schlechtester Einzelscore in dieser Zone"
    )
    worst_seal_id: Optional[str] = Field(
        None,
        description="ID der schlechtesten Dichtung"
    )
    seals_requiring_action: int = Field(
        0,
        ge=0,
        description="Anzahl Dichtungen mit Handlungsbedarf"
    )
    critical_findings: list[str] = Field(
        default_factory=list,
        description="Kritische Befunde in dieser Zone"
    )


class SealSystemAssessment(BaseModel):
    """Gesamtbewertung des Dichtungssystems eines Bootes.

    Aggregiert alle SealCondition-Bewertungen zu einer systemischen Bewertung.
    Wird im AYDI-Report als Unterabschnitt der Module 'materials' und 'compliance'
    dargestellt. Scores 0-100, Kosten in EUR.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    project_id: str = Field(
        ...,
        description="AYDI-Projekt-ID"
    )
    boat_class: BoatClass = Field(
        ...,
        description="Bootklasse (bestimmt Bewertungsmaßstab)"
    )
    assessment_date: str = Field(
        ...,
        description="Bewertungsdatum (ISO 8601)"
    )

    # Boot-Kontext
    boat_year: Optional[int] = Field(
        None,
        ge=1950,
        le=2030,
        description="Baujahr des Bootes"
    )
    boat_length_m: Optional[float] = Field(
        None,
        ge=2.5,
        le=100.0,
        description="Bootslänge in Metern"
    )
    primary_cruising_area: Optional[str] = Field(
        None,
        description="Hauptfahrtgebiet: 'mittelmeer', 'nordeuropa', 'tropen', 'arktis', 'trailerbetrieb'"
    )
    ce_category: Optional[str] = Field(
        None,
        description="CE-Entwurfskategorie (A/B/C/D)"
    )

    # Einzelbewertungen
    seal_conditions: list[SealCondition] = Field(
        ...,
        description="Liste aller bewerteten Dichtungen"
    )

    # Zonenzusammenfassung
    zone_summaries: list[SealZoneSummary] = Field(
        default_factory=list,
        description="Zusammenfassung nach Zonen"
    )

    # Gesamtscores
    overall_seal_system_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Gesamtscore Dichtungssystem (0-100)"
    )
    material_suitability_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Materialeignung für Bootklasse und Revier (0-100)"
    )
    installation_quality_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Einbauqualität über alle Dichtungen (0-100)"
    )
    maintenance_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Wartungszustand (0-100)"
    )
    compliance_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Konformitätsbewertung (ISO 12216, CE-Kategorie) (0-100)"
    )

    # Kosten
    total_replacement_cost_eur: float = Field(
        0.0,
        ge=0.0,
        description="Gesamtkosten für empfohlene Dichtungstausche in EUR"
    )
    total_labor_hours: float = Field(
        0.0,
        ge=0.0,
        description="Gesamtarbeitsstunden für empfohlene Maßnahmen"
    )

    # Befunde
    critical_findings: list[str] = Field(
        default_factory=list,
        description="Kritische Befunde (sofortiger Handlungsbedarf)"
    )
    warnings: list[str] = Field(
        default_factory=list,
        description="Warnungen (mittelfristiger Handlungsbedarf)"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen (präventive Maßnahmen)"
    )

    # Pipeline-Daten
    structured_data_available: bool = Field(
        False,
        description="Strukturierte Daten lagen vor (CAD, Spezifikationen)"
    )
    visual_data_available: bool = Field(
        False,
        description="Visuelle Daten lagen vor (Fotos)"
    )
    text_data_available: bool = Field(
        False,
        description="Textdaten lagen vor (Servicereports)"
    )
    fusion_weights: dict[str, float] = Field(
        default_factory=lambda: {"structured": 0.35, "visual": 0.65},
        description="Fusionsgewichte (materials-Modul: structured 0.35, visual 0.65)"
    )

    # Metadaten
    engine_version: str = Field(
        ...,
        description="AYDI-Engine-Version"
    )
    model_version: Optional[str] = Field(
        None,
        description="Claude-Modell-Version (für Pipeline B)"
    )
    confidence: ConfidenceLevel = Field(
        ...,
        description="Gesamt-Confidence der Bewertung"
    )
    processing_time_ms: Optional[int] = Field(
        None,
        ge=0,
        description="Verarbeitungszeit in Millisekunden"
    )
```

### 6.5 Hilfsmodelle

```python
class SealReplacementKit(BaseModel):
    """Dichtungs-Ersatzkit (vorgeschnittene OEM-Dichtung für spezifische Luke)."""
    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    part_number: str = Field(..., description="Teilenummer des Kits")
    fits_hatch_series: str = Field(..., description="Passt für Lukenserie")
    fits_hatch_sizes: list[str] = Field(..., description="Passt für Lukengrößen (z.B. ['20', '30', '40'])")
    seal_profile_type: SealProfileType = Field(..., description="Profiltyp")
    seal_material: SealMaterial = Field(..., description="Material")
    seal_length_mm: float = Field(..., ge=0, description="Gesamtlänge der Dichtung in mm")
    pre_formed_corners: bool = Field(False, description="Ecken vorvulkanisiert")
    includes_adhesive: bool = Field(False, description="Kleber enthalten")
    includes_lubricant: bool = Field(False, description="Silikonspray/Gleitmittel enthalten")
    price_eur: float = Field(..., ge=0, description="Preis in EUR (UVP exkl. MwSt.)")
    availability: str = Field("standard", description="'standard', 'auf_anfrage', 'eingestellt'")
    data_source: str = Field(..., description="Datenquelle")
    confidence: ConfidenceLevel = Field(ConfidenceLevel.DOCUMENTED)


class GrooveSpec(BaseModel):
    """Spezifikation einer Dichtungsnut."""
    model_config = {"from_attributes": True}

    groove_type: str = Field(
        ...,
        description="Nuttyp: 'rechteck' (Rechtecknut), 'schwalbenschwanz' (Schwalbenschwanznut), 'trapez' (Trapeznut), 't_nut' (T-Nut), 'rund' (Rundnut)"
    )
    width_mm: float = Field(..., ge=1.0, le=25.0, description="Nutbreite in mm")
    depth_mm: float = Field(..., ge=1.0, le=20.0, description="Nuttiefe in mm")
    bottom_radius_mm: float = Field(0.5, ge=0.0, le=5.0, description="Bodenradius in mm")
    entry_width_mm: Optional[float] = Field(
        None, ge=1.0, le=25.0,
        description="Eintrittsbreite in mm (bei Schwalbenschwanz < width_mm)"
    )
    material: str = Field(
        ...,
        description="Material des Nutträgers: 'aluminium', 'grp', 'stainless', 'teak'"
    )
    surface_finish: str = Field(
        "gefraest",
        description="Oberflächengüte: 'gefraest', 'eloxiert', 'lackiert', 'roh', 'poliert'"
    )
    recommended_seal_profiles: list[SealProfileType] = Field(
        ...,
        description="Empfohlene Profiltypen für diese Nut"
    )
```

---

## 7. Grundlagen

### 7.1 Dichtungsprofiltypen — Systematische Übersicht

#### 7.1.1 D-Profil (Hohlprofil, Rundprofil)

**Form:** Halbrundes Hohlprofil mit flacher Unterseite (Fußfläche). Im Querschnitt ähnelt es dem Buchstaben "D".

**Eigenschaften:**
- Hohlraum ermöglicht definierte Kompression bei geringem Anpressdruck
- Geringe Rückstellkraft notwendig — schonend für Verriegelungsmechanismen
- Gute Toleranzaufnahme (±1mm Spaltvariation kompensierbar)
- Selbstdichtend: Außendruck presst Hohlraum zusammen

**Typische Maße:**

| Bezeichnung | Gesamthöhe mm | Breite mm | Wandstärke mm | Hohlraum-∅ mm | Shore A |
|------------|--------------|----------|--------------|--------------|---------|
| D-10/12 (klein) | 10 | 12 | 1.5 | 7 | 50–60 |
| D-12/14 (mittel) | 12 | 14 | 2.0 | 8 | 50–60 |
| D-14/16 (groß) | 14 | 16 | 2.0 | 10 | 45–55 |
| D-18/20 (XL) | 18 | 20 | 2.5 | 13 | 45–55 |

**Einsatz:** Primär bei Decksluken (Lewmar, Goiot, Bomar). Das am häufigsten verwendete Profil im Yachtbau. Ca. 60% aller Lukendichtungen sind D-Profile.

**Befestigung:** Meist press-fit in Rechtecknut oder selbstklebend auf flachem Rahmen.

**Hersteller-Beispiele:**
- Lewmar: Alle Ocean- und Low-Profile-Serien verwenden D-Profile
- Goiot: Cristal- und Opal-Serien
- Bomar: Standard-Luken
- Meyco: Meterware D-3011 (10×12mm), D-3012 (12×14mm), D-3013 (14×16mm)

#### 7.1.2 P-Profil (Versetztes D-Profil)

**Form:** Ähnlich dem D-Profil, aber der Dichtkopf ist seitlich versetzt gegenüber dem Fuß. Im Querschnitt ähnelt es dem Buchstaben "P".

**Eigenschaften:**
- Ermöglicht Abdichtung bei seitlichem Kontakt (Lukendeckel schließt gegen seitliche Dichtfläche)
- Geeignet für Luken mit seitlichem Anschlag
- Gute Kompensation von Spaltmaß-Toleranzen
- Etwas komplexere Nut-Geometrie erforderlich

**Typische Maße:**

| Bezeichnung | Gesamthöhe mm | Fußbreite mm | Kopf-∅ mm | Versatz mm | Shore A |
|------------|--------------|-------------|----------|-----------|---------|
| P-9/5 (klein) | 9 | 5 | 7 | 3 | 50–60 |
| P-12/6 (mittel) | 12 | 6 | 9 | 4 | 50–60 |
| P-15/8 (groß) | 15 | 8 | 11 | 5 | 45–55 |

**Einsatz:** Bullaugen mit Klappmechanismus, einige Companionway-Türen, Schiebefenster.

**Hersteller-Beispiele:**
- Vetus: P-Serie für PWS-Bullaugen
- Houdini: Aftermarket P-Profile für Goiot-Bullaugen

#### 7.1.3 E-Profil (Dreifach-Lippenprofil)

**Form:** Drei parallele Dichtlippen an einem gemeinsamen Fuß. Im Querschnitt ähnelt es dem Buchstaben "E".

**Eigenschaften:**
- Dreifache Dichtebene: jede Lippe bildet eine unabhängige Dichtstelle
- Sehr gute Toleranzaufnahme (±2mm)
- Geringer Anpressdruck nötig (Lippen sind einzeln flexibel)
- Weniger geeignet für hohe Druckbelastung (Grünwasser)

**Typische Maße:**

| Bezeichnung | Gesamthöhe mm | Breite mm | Lippendicke mm | Lippenabstand mm | Shore A |
|------------|--------------|----------|---------------|----------------|---------|
| E-8/4 (klein) | 8 | 4 | 1.0 | 2.0 | 45–55 |
| E-12/5 (mittel) | 12 | 5 | 1.5 | 2.5 | 45–55 |
| E-15/6 (groß) | 15 | 6 | 2.0 | 3.0 | 40–50 |

**Einsatz:** Salonfenster (fest), Kabinenfenster, Skylights, wo geringer Anpressdruck gewünscht ist. Weniger üblich für Decksluken.

**Hersteller-Beispiele:**
- Schlegel: E-Profile für Fensterrahmen (Architektur-Herkunft, marine-geeignet)
- Deventer: E-Profile SPV 3042, SPV 3045
- Trend Marine: Fensterdichtungen für Salonfenster

#### 7.1.4 Omega-Profil (Ω-Profil)

**Form:** Omegaförmig — ein gewölbter Dichtkopf mit zwei nach innen gerichteten Klemmschenkeln. Im Querschnitt ähnelt es dem griechischen Buchstaben Ω.

**Eigenschaften:**
- Sehr hohe Kompressionsrate möglich (bis 50%)
- Klemmschenkel greifen in Nut und verhindern Herausrutschen
- Gute Rückstellung durch die Gewölbeform
- Höherer Anpressdruck erforderlich als bei D-Profilen

**Typische Maße:**

| Bezeichnung | Gesamthöhe mm | Breite mm | Schenkellänge mm | Shore A |
|------------|--------------|----------|----------------|---------|
| Ω-10/14 (klein) | 10 | 14 | 5 | 50–65 |
| Ω-14/18 (mittel) | 14 | 18 | 7 | 50–65 |
| Ω-18/22 (groß) | 18 | 22 | 9 | 45–60 |

**Einsatz:** Maschinenraumluken, Lazarette-Luken mit hoher mechanischer Belastung, Superyacht-Luken mit Flush-Profil.

**Hersteller-Beispiele:**
- Peters Rubber: Custom Ω-Profile für Superyacht-Werften
- Rehau: Industrieprofile, teilweise marine-adaptierbar
- Freeman Marine (USA): Standardprofil für ihre Decksluken

#### 7.1.5 Torpedo-Profil (Zylindrischer Einsteck-Profil)

**Form:** Zylindrischer oder leicht konischer Dichtkopf auf einem schmalen Steg, der in einen Kanal oder ein T-Profil eingeschoben wird. Der Name kommt von der Torpedoform des Kopfes.

**Eigenschaften:**
- Einfache Montage: in Aluminium-T-Kanal einschieben
- Sehr guter Halt im Kanal (kann nicht herausgezogen werden ohne Demontage)
- Gute Kompressionscharakteristik
- Erfordert spezifischen Aluminium-Kanal als Nutträger

**Typische Maße:**

| Bezeichnung | Kopf-∅ mm | Stegbreite mm | Steghöhe mm | Gesamt mm | Shore A |
|------------|----------|-------------|-----------|----------|---------|
| T-8/3 (klein) | 8 | 3 | 6 | 14 | 50–60 |
| T-10/4 (mittel) | 10 | 4 | 8 | 18 | 50–60 |
| T-12/5 (groß) | 12 | 5 | 10 | 22 | 45–55 |

**Einsatz:** Aluminium-Lukenrahmen (Lewmar Ocean-Serie nutzt ähnliches Prinzip), Custom-Luken in Aluminium-Yachten, Maschinenraumzugänge.

**Hersteller-Beispiele:**
- Lewmar: Ocean 40–70 (modifiziertes Torpedo-Prinzip in Alu-Kanal)
- Peters Rubber: T-Profile für Aluminium-Yachtbauer (z.B. KM Yachtbuilders, Jachtwerf Vitters)
- Meyco: Torpedo-Profile T-5010, T-5012

#### 7.1.6 Bulb-Profil (Knollen-/Zwiebelkopf-Profil)

**Form:** Verdickter kugelförmiger Dichtkopf auf schmalem Fuß. Der Kopf ist massiv (kein Hohlraum). Im Querschnitt ähnelt es einer Zwiebel oder einem Pilz.

**Eigenschaften:**
- Hohe Dichtkraft durch massiven Kopf
- Sehr guter Anpressdruck-Kontakt
- Höherer Anpressdruck erforderlich als bei Hohlprofilen
- Weniger Toleranzaufnahme als D-Profil
- Langlebig (kein Hohlraum, der kollabieren kann)

**Typische Maße:**

| Bezeichnung | Kopf-∅ mm | Fußbreite mm | Gesamthöhe mm | Shore A |
|------------|----------|-------------|-------------|---------|
| B-8/4 (klein) | 8 | 4 | 10 | 55–65 |
| B-10/5 (mittel) | 10 | 5 | 13 | 55–65 |
| B-14/6 (groß) | 14 | 6 | 17 | 50–60 |

**Einsatz:** Windschutzscheiben, Salonfenster mit mechanischer Klemmleiste, Luken mit Spindelverschluss (hoher Anpressdruck).

**Hersteller-Beispiele:**
- Trend Marine: Bulb-Profile für Windschutzscheiben-Rahmen
- Deventer: SPV 4055 (Bulb für Fensterrahmen)
- Raboesch: Kunststoff-Bulb-Profile

#### 7.1.7 Lippendichtung (Lip Seal)

**Form:** Flexible Lippe, die durch elastische Verformung an der Dichtfläche anliegt. Die Lippe kann einfach (Single Lip) oder doppelt (Double Lip) ausgeführt sein.

**Eigenschaften:**
- Sehr geringer Anpressdruck nötig (Eigenspannung der Lippe reicht)
- Erlaubt leichte Relativbewegung zwischen Rahmen und Deckel
- Begrenzte Druckbelastbarkeit (nicht geeignet für Grünwasser-Übernahme)
- Empfindlich gegenüber Schmutz auf der Dichtfläche

**Typische Maße:**

| Bezeichnung | Gesamthöhe mm | Lippenbreite mm | Lippendicke mm | Shore A |
|------------|--------------|----------------|---------------|---------|
| L-6/8 (klein) | 6 | 8 | 1.5 | 45–55 |
| L-10/12 (mittel) | 10 | 12 | 2.0 | 45–55 |
| L-12/15 (groß) | 12 | 15 | 2.5 | 40–50 |

**Einsatz:** Niedergangs-Schiebetüren, Schiebefenster, Maschinenraum-Schallschutzdeckel, Lazarette-Luken (nicht für offenes Wasser).

**Hersteller-Beispiele:**
- Schlegel: Bürstendichtungen mit Lippenelement für Schiebefenster
- Houdini: Lip Seals für Companionway-Bretter
- Seldén: Lip Seals für Schiebe-Decksluken

#### 7.1.8 Flachdichtung (Flat Gasket)

**Form:** Flacher Ring oder Streifen aus Elastomer, der zwischen zwei planparallelen Flächen verpresst wird. Keine Profilierung.

**Eigenschaften:**
- Einfachste Dichtungsform
- Erfordert sehr planparallele Flächen und gleichmäßigen Anpressdruck über den gesamten Umfang
- Hoher Anpressdruck nötig (keine Formelastizität)
- Problematisch bei thermischer Ausdehnung oder Verzug
- Einfach herzustellen (aus Platte gestanzt)

**Typische Maße:**

| Bezeichnung | Dicke mm | Breite mm | Material | Shore A |
|------------|---------|----------|---------|---------|
| FG-2/10 (dünn) | 2 | 10 | EPDM/Silikon | 55–70 |
| FG-3/15 (mittel) | 3 | 15 | EPDM/Silikon | 55–70 |
| FG-5/20 (dick) | 5 | 20 | EPDM/Neopren | 50–65 |

**Einsatz:** Bullaugen-Ringe (Verschraubung), Maschinenraumdeckel, Inspektionsöffnungen, Tank-Luken (Wasser/Diesel). Nicht empfohlen für Decksluken mit Klappmechanismus.

**Hersteller-Beispiele:**
- Osculati: Flachdichtungen für Inspektionsdeckel (Art.-Nr. 20.205.xx)
- Plastimo: Inspektionsluk-Dichtungen
- Vetus: KITCOVER-Serie (Flachdichtungen für Tank-Inspektionsöffnungen)

### 7.2 Materialien im Detail

#### 7.2.1 EPDM (Ethylen-Propylen-Dien-Kautschuk)

**Chemische Beschreibung:** Terpolymer aus Ethylen, Propylen und einem Dien-Monomer (ENB, DCPD oder VNB). Die Dien-Komponente (3–12 Gew.-%) ermöglicht die Schwefelvulkanisation. Ethylen-Anteil typisch 45–75%.

**Eigenschaften für marine Anwendung:**

| Eigenschaft | Wert | Relevanz Marine |
|-----------|------|----------------|
| Temperaturbereich | -45°C bis +150°C | Frost/Tropen geeignet |
| Shore-A-Härte | 30–90 (marine: 40–70) | Kompressionsprofile 50–60 |
| Zugfestigkeit | 7–21 MPa | Ausreichend für mechanische Belastung |
| Bruchdehnung | 300–600% | Gute Flexibilität |
| Compression Set (72h/23°C) | 15–35% | Gut bis sehr gut |
| Compression Set (72h/100°C) | 25–55% | Akzeptabel |
| UV-Beständigkeit | Sehr gut (mit Carbon Black) | Decksdichtungen |
| Ozonbeständigkeit | Hervorragend | Kritisch für marine Atmosphäre |
| Salzwasserbeständigkeit | Hervorragend | Primäranforderung |
| Ölbeständigkeit | Schlecht | Nicht für Maschinenraum ohne Schutz |
| Chemikalienbeständigkeit | Gut (Säuren, Laugen) | Reinigungsmittel-kompatibel |
| Flammwidrigkeit | Selbstverlöschend (bei Zusatz) | Maschinenraum-Luken |
| Lebensdauer marine | 7–12 Jahre (Nordeuropa) | Abhängig von UV-Exposition |
| Preis (Meterware) | EUR 2–8/m | Kostengünstigstes Premiummaterial |

**Vulkanisationsarten:**
- **Schwefelvernetzung:** Standard, gute mechanische Eigenschaften, niedrigerer Compression Set möglich. Ca. 70% aller marine EPDM-Dichtungen.
- **Peroxidvernetzung:** Bessere Hochtemperaturbeständigkeit, besserer Compression Set bei hohen Temperaturen, geringerer Eigengeruch. Ca. 30% (Premium-Segment). Lewmar Ocean-Serie verwendet peroxidvernetztes EPDM (Confidence: documented).

**UV-Stabilisierung:**
- **Carbon Black (Ruß):** Primärer UV-Absorber. Daher sind marine EPDM-Dichtungen fast ausschließlich schwarz. Carbon Black absorbiert UV-A und UV-B und wandelt die Energie in Wärme um. Anteil: 20–50 phr.
- **Chemische UV-Stabilisatoren:** HALS (Hindered Amine Light Stabilizers), Benzotriazol. Für helle Dichtungen. Weniger effektiv als Carbon Black. Lebensdauerreduktion ca. 30–40%.

**EPDM-Hersteller (Compound-Lieferanten):**
- Lanxess (DE): Keltan EPDM — Referenz für marine Compounds
- Arlanxeo (NL): Keltan Eco (teilweise biobasiert)
- Dow (USA): Nordel EPDM
- ExxonMobil (USA): Vistalon EPDM
- Kumho Polychem (KR): KEP (kostengünstig, in Aftermarket-Profilen verbreitet)

#### 7.2.2 Silikonkautschuk (VMQ / MVQ)

**Chemische Beschreibung:** Polyorganosiloxan-Elastomer mit Si-O-Si-Hauptkette (anorganisches Rückgrat). Typisch: Polydimethylsiloxan (PDMS) mit Methyl- und Vinylgruppen. Vernetzung durch Platinkatalyse (Addition) oder Peroxid (Radikalisch).

**Eigenschaften für marine Anwendung:**

| Eigenschaft | Wert | Relevanz Marine |
|-----------|------|----------------|
| Temperaturbereich | -60°C bis +230°C | Überlegener Kälte-/Hitzebereich |
| Shore-A-Härte | 20–80 (marine: 40–65) | Sehr weiche Profile möglich |
| Zugfestigkeit | 5–12 MPa | Geringer als EPDM |
| Bruchdehnung | 200–800% | Gut |
| Compression Set (72h/23°C) | 10–30% | Sehr gut |
| Compression Set (72h/175°C) | 15–40% | Hervorragend bei Hitze |
| UV-Beständigkeit | Hervorragend | Beste UV-Resistenz aller Elastomere |
| Ozonbeständigkeit | Hervorragend | Inhärent resistent |
| Salzwasserbeständigkeit | Hervorragend | Keine Degradation |
| Ölbeständigkeit | Mäßig | Quillt in Mineralöl |
| Schimmelresistenz | Sehr gut | Inherent antimikrobiell |
| Flammwidrigkeit | Gut (LOI 25–35%) | Selbstverlöschend |
| Lebensdauer marine | 10–20 Jahre | Längste aller Standardelastomere |
| Preis (Meterware) | EUR 8–25/m | 3–4× teurer als EPDM |

**Sorten:**
- **HTV (High Temperature Vulcanizing):** Standard für extrudierte Profile. Vulkanisation bei 150–200°C. Mechanisch stärker als RTV.
- **LSR (Liquid Silicone Rubber):** Für Spritzguss-Dichtungen. Zweikomponenten, platinvernetzt. Höhere Reinheit.
- **Fluorsilikon (FVMQ):** Zusätzliche Ölbeständigkeit durch Fluor-Gruppen. Für Maschinenraum-Luken. EUR 20–50/m.

**Silikon vs. EPDM — Entscheidungsmatrix:**

| Kriterium | EPDM | Silikon | Empfehlung |
|----------|------|---------|-----------|
| Kosten | + + + | + | EPDM bei Budget-Fokus |
| UV-Beständigkeit | + + | + + + | Silikon für Tropen/Mittelmeer |
| Kälteflexibilität | + + | + + + | Silikon für Arktis/Nordeuropa |
| Compression Set | + + | + + + | Silikon bei Dauerbelastung |
| Abriebfestigkeit | + + + | + | EPDM für begehbare Luken |
| Zugfestigkeit | + + + | + + | EPDM für mechanisch belastete Dichtungen |
| Lebensdauer | + + | + + + | Silikon für weniger Wartung |
| Verfügbarkeit | + + + | + + | EPDM als Meterware überall verfügbar |

**Silikon-Hersteller (Compound-Lieferanten):**
- Wacker Chemie (DE): Elastosil — Referenz für marine Silikon-Profile
- Dow/Dupont (USA): Silastic
- Shin-Etsu (JP): KE-Serie
- Momentive (USA): Silopren

#### 7.2.3 Neopren / Chloropren (CR)

**Chemische Beschreibung:** Polychloropren, synthetischer Kautschuk. Historisch erstes Synthesekautschuk-Elastomer (DuPont, 1931).

**Eigenschaften für marine Anwendung:**

| Eigenschaft | Wert | Relevanz Marine |
|-----------|------|----------------|
| Temperaturbereich | -30°C bis +120°C | Eingeschränkt bei Kälte |
| Shore-A-Härte | 40–90 | Breiter Bereich |
| Compression Set (72h/23°C) | 20–40% | Mäßig |
| UV-Beständigkeit | Mäßig | Nicht für permanente Exposition |
| Ozonbeständigkeit | Gut | Besser als NR, schlechter als EPDM |
| Ölbeständigkeit | Gut | Vorteil ggü. EPDM |
| Flammwidrigkeit | Inhärent selbstverlöschend | Vorteil für Maschinenraum |

**Status im Yachtbau:** Seit den 1990er Jahren weitgehend durch EPDM ersetzt. Noch in einigen Legacy-Anwendungen und bei Maschinenraum-Luken anzutreffen (wegen Ölbeständigkeit + Flammwidrigkeit). Nicht empfohlen für Neuinstallationen an Deck.

**Hersteller:** DuPont (Neoprene), Lanxess (Baypren), Denka (Denka Chloroprene)

#### 7.2.4 Nitrilkautschuk (NBR)

**Chemische Beschreibung:** Copolymer aus Butadien und Acrylnitril. ACN-Gehalt 18–50% (höherer ACN = bessere Ölbeständigkeit, schlechtere Kälteflexibilität).

**Marine-Relevanz:** Primär für Dichtungen mit Ölkontakt (Maschinenraum-Inspektionsdeckel, Ölfiltergehäuse). **Nicht geeignet** für Decks- oder Fensterdichtungen wegen schlechter UV- und Ozonbeständigkeit. Wird bei UV-Exposition rissig innerhalb von 6–12 Monaten.

**Wenn doch verwendet:** Nur an innen liegenden, UV-freien Positionen. Maschinenraumluke innen, Tankdeckel, Inspektionsluken im Bilgenbereich.

| Eigenschaft | Wert |
|-----------|------|
| Temperaturbereich | -30°C bis +120°C |
| UV-Beständigkeit | Sehr schlecht |
| Ozonbeständigkeit | Schlecht |
| Ölbeständigkeit | Sehr gut |

#### 7.2.5 TPE (Thermoplastische Elastomere)

**Chemische Beschreibung:** Thermoplastisch verarbeitbare Werkstoffe mit gummielastischen Eigenschaften bei Raumtemperatur. Keine chemische Vernetzung, sondern physikalische (reversible) Vernetzung durch Phasentrennung.

**Typen:**
- **TPS (Styrol-Block-Copolymere):** SEBS, SBS. Preisgünstig, moderate Eigenschaften. Für Aftermarket-Profile.
- **TPV (Thermoplastische Vulkanisate):** EPDM/PP-Blend, dynamisch vulkanisiert. Beste TPE-Eigenschaften für marine Anwendungen. Santoprene (ExxonMobil) ist Referenz.
- **TPO (Thermoplastische Olefine):** PP/EPDM-Blend, nicht vernetzt. Einfach, kostengünstig. Für unkritische Anwendungen.
- **TPU (Thermoplastische Polyurethane):** Gute mechanische Eigenschaften, aber Hydrolyse-Empfindlichkeit in marine Umgebung. Nicht empfohlen für permanenten Salzwasser-Kontakt.

**Eigenschaften für marine Anwendung (TPV):**

| Eigenschaft | Wert | Relevanz Marine |
|-----------|------|----------------|
| Temperaturbereich | -50°C bis +135°C | Gut |
| Shore-A-Härte | 35–90 | Breiter Bereich |
| Compression Set (72h/23°C) | 25–50% | Mäßig bis akzeptabel |
| UV-Beständigkeit | Gut (mit Stabilisator) | Schwächer als EPDM/Silikon |
| Ozonbeständigkeit | Gut | Ausreichend |
| Recyclebar | Ja | Nachhaltigkeitsvorteil |
| Preis (Meterware) | EUR 1.50–5/m | Preisvorteil |

**AYDI-Bewertung:** TPE/TPV sind akzeptabel für Level 1 (Schnellanalyse) als "Standard"-Material. Für Level 2 (Profi) wird bei Kat. A/B Booten EPDM oder Silikon empfohlen. TPE-Dichtungen erhalten im materials-Modul einen Abzug von 10–15 Punkten gegenüber EPDM bei gleichen Bedingungen.

#### 7.2.6 Weitere Materialien

**FKM (Fluorkautschuk / Viton):**
- Temperaturbereich: -20°C bis +250°C
- Hervorragende Chemikalien- und Ölbeständigkeit
- Sehr teuer (EUR 30–100/m)
- Marine-Einsatz: nur Spezialanwendungen (Maschinenraum-Luken bei Hochtemperatur-Motoren, Abgassystem-Inspektionsöffnungen)

**PVC flexibel (Weich-PVC):**
- Veraltet, enthält Weichmacher (Phthalate) die auswandern
- Wird spröde nach 3–5 Jahren
- In älteren Booten (vor 1990) noch anzutreffen
- **Nicht empfohlen** für Neuinstallation. Bei Vorfinden: sofort ersetzen.

**Butylkautschuk (IIR):**
- Sehr geringe Gasdurchlässigkeit
- Schlechte mechanische Eigenschaften für Profile
- Marine-Einsatz: nur als Dichtungsmasse (Butylband), nicht als Profildichtung

### 7.3 Compression Set (Druckverformungsrest)

#### 7.3.1 Definition und Bedeutung

Der **Druckverformungsrest** (Compression Set, CS) ist die wichtigste Kenngröße für die Langzeitfunktion einer Kompressionssdichtung. Er beschreibt den Anteil der Verformung, der nach Entlastung dauerhaft verbleibt.

**Berechnung nach ISO 815-1:**

```
CS = (h₀ - h₂) / (h₀ - h₁) × 100 [%]

h₀ = ursprüngliche Dicke des Probekörpers
h₁ = Dicke im komprimierten Zustand (Spacer-Dicke)
h₂ = Dicke nach Entlastung und Erholung (30 min bei 23°C)
```

**Interpretation:**
- CS = 0%: vollständige Rückstellung (ideale Dichtung)
- CS = 10–20%: sehr gut (Premium-Silikon, peroxidvernetztes EPDM)
- CS = 20–30%: gut (Standard-EPDM, hochwertiges TPV)
- CS = 30–50%: akzeptabel (Standard-TPE, älteres EPDM)
- CS > 50%: ungenügend (Dichtung tauschbedürftig)
- CS = 100%: keine Rückstellung (Material hat permanent nachgegeben)

#### 7.3.2 Einflussfaktoren auf Compression Set

| Faktor | Einfluss | Quantifizierung |
|--------|---------|----------------|
| Temperatur | +++ | CS steigt ca. 1–2% pro 10°C Temperaturerhöhung |
| Kompressionsrate | ++ | CS steigt exponentiell bei >40% Kompression |
| Zeitdauer | ++ | CS steigt logarithmisch mit der Zeit |
| Vulkanisationsgrad | ++ | Untervulkanisiert → höherer CS |
| Füllstoffanteil | + | Hoher Ruß-Anteil → höherer CS |
| Material | +++ | Silikon < EPDM-Peroxid < EPDM-Schwefel < TPV < TPS |

#### 7.3.3 Compression Set im Einsatz — Zeitliche Entwicklung

**Typisches CS-Verhalten einer Lukendichtung (EPDM, Shore A 55, 25% Kompression, 20°C):**

| Zeitraum | CS (%) | Restkompression effektiv | Dichtwirkung |
|---------|--------|------------------------|-------------|
| 0–1 Jahr | 5–10% | 22–24% | Voll |
| 1–3 Jahre | 10–18% | 20–22% | Voll |
| 3–5 Jahre | 15–25% | 18–21% | Voll |
| 5–8 Jahre | 20–35% | 16–20% | Leicht eingeschränkt bei starker See |
| 8–12 Jahre | 30–45% | 13–17% | Eingeschränkt, Leckage bei Seegang möglich |
| >12 Jahre | 40–60% | 10–15% | Unzureichend, Tausch empfohlen |

#### 7.3.4 AYDI-Bewertung des Compression Set

```python
def score_compression_set(cs_percent: float, material: SealMaterial) -> int:
    """Bewertet den Compression Set und gibt einen Score 0-100 zurück.

    Args:
        cs_percent: Gemessener oder geschätzter Compression Set in %
        material: Dichtungsmaterial (für materialspezifische Schwellwerte)

    Returns:
        Score 0-100 (100 = ideal, 0 = vollständig versagt)
    """
    # Materialspezifische Schwellwerte
    thresholds = {
        SealMaterial.SILICONE: {"excellent": 15, "good": 25, "fair": 35, "poor": 50},
        SealMaterial.EPDM_PEROXIDE: {"excellent": 18, "good": 28, "fair": 38, "poor": 55},
        SealMaterial.EPDM: {"excellent": 20, "good": 30, "fair": 42, "poor": 60},
        SealMaterial.TPE_V: {"excellent": 25, "good": 35, "fair": 50, "poor": 65},
        SealMaterial.NEOPRENE_CR: {"excellent": 22, "good": 32, "fair": 45, "poor": 60},
    }
    t = thresholds.get(material, thresholds[SealMaterial.EPDM])

    if cs_percent <= t["excellent"]:
        return 100
    elif cs_percent <= t["good"]:
        return 85 - int((cs_percent - t["excellent"]) / (t["good"] - t["excellent"]) * 15)
    elif cs_percent <= t["fair"]:
        return 70 - int((cs_percent - t["good"]) / (t["fair"] - t["good"]) * 25)
    elif cs_percent <= t["poor"]:
        return 45 - int((cs_percent - t["fair"]) / (t["poor"] - t["fair"]) * 30)
    else:
        return max(0, 15 - int((cs_percent - t["poor"]) / 50 * 15))
```

### 7.4 Shore-Härte — Auswahl und Auswirkungen

#### 7.4.1 Shore-A-Skala für marine Dichtungen

| Shore A | Haptik | Marine-Eignung | Typische Anwendung |
|---------|--------|---------------|-------------------|
| 20–30 | Sehr weich (Schwamm) | Nur für drucklose Dichtungen | Nicht empfohlen (zu weich) |
| 30–40 | Weich (Gummibär) | Niedrigdruck-Anwendungen | Ankerkisten, Lazarette (unkritisch) |
| 40–50 | Mittelweich (Radiergummi) | Standard marine | Kabinenfenster, Bullaugen (öffnend) |
| 50–60 | Mittel (Autoreifen) | Optimal für Decksluken | Decksluken, Windschutzscheiben |
| 60–70 | Mittelhart | Hochdruck-Dichtungen | Vordeck-Luken (Kat. A), Maschinenraum |
| 70–80 | Hart | Spezialanwendungen | Verschraubte Bullaugen, Druckluken |
| >80 | Sehr hart (Schuhsohle) | Nicht empfohlen | Kein Einsatz bei Kompressionssdichtungen |

#### 7.4.2 Temperatureinfluss auf Shore-Härte

**Faustregel:** Shore A steigt um ca. 5 Punkte pro 10°C Temperaturabnahme (unterhalb +23°C Referenztemperatur).

| Temperatur | Shore A nominal 55 | Shore A nominal 45 | Dichtwirkung |
|-----------|--------------------|--------------------|-------------|
| +40°C | ~48 | ~38 | Weicher, mehr Kompression, gut |
| +23°C | 55 (Referenz) | 45 (Referenz) | Optimal |
| +10°C | ~61 | ~51 | Leicht härter, noch gut |
| 0°C | ~67 | ~57 | Deutlich härter, Anpressdruck muss reichen |
| -10°C | ~73 | ~63 | Hart, eingeschränkte Dichtwirkung |
| -20°C | ~80 | ~70 | Sehr hart, Dichtung darf nicht bewegt werden |
| -30°C | ~85+ (EPDM) | ~75+ | Grenzbereich, Bruchgefahr bei Schlag |

**AYDI-Empfehlung:**
- Nordeuropa/Ostsee: Shore A 40–50 nominal (bleibt bei 0°C noch unter 60)
- Mittelmeer: Shore A 50–60 nominal (hohe Temperaturen kompensieren)
- Tropen: Shore A 50–60 nominal
- Arktis: Shore A 35–45 nominal (Silikon bevorzugt)

### 7.5 Nutdesign (Groove Design)

#### 7.5.1 Nuttypen

**Rechtecknut (Standard):**
```
    ┌──────────┐
    │          │  ← Nuttiefe (h)
    │          │
    └──────────┘
    ← Nutbreite (w) →

    Toleranz: w ± 0.2mm, h ± 0.3mm
```

- Einfachste Herstellung (Fräsen, Extrusion)
- Für D-Profile, Flachdichtungen
- Dichtung wird eingepresst (Übermaß 0.3–0.5mm)
- Risiko: Dichtung kann bei Vibration herausrutschen

**Schwalbenschwanznut (Dovetail):**
```
    ┌────────────┐
     \          /   ← Nuttiefe (h)
      \        /
       └──────┘
    ← Eintritt (w₁) →
    ← Boden (w₂) → (w₂ > w₁)

    Typisch: w₂ = w₁ + 1.5mm
```

- Formschlüssige Fixierung des Dichtungsfußes
- Dichtung kann nicht herausgezogen werden
- Aufwendigere Herstellung (spezieller Fräser)
- Für Aluminium-Lukenrahmen bevorzugt (Lewmar, Seldén)

**T-Nut (für Torpedo-Profile):**
```
    ┌──┐
    │  │ ← Schlitz (s)
    │  │
    ├──┤
    │    │ ← Kanal (w)
    └────┘

    s < w (Torpedo-Kopf passt nicht durch Schlitz)
```

- Torpedo-Profil wird seitlich eingeschoben
- Sehr sicherer Halt
- Erfordert Aluminium-Extrusion (keine Nachbearbeitung in GFK möglich)

**Rundnut (für O-Ring-ähnliche Profile):**
```
    ╭──────────╮
    │          │ ← Radius
    ╰──────────╯

    Radius = Dichtungsdurchmesser × 1.05
```

- Für Rundschnur-Dichtungen und O-Ringe
- Verwendung bei Bullaugen-Verschraubungen
- Erfordert CNC-Fräse oder spezielle Drehteile

#### 7.5.2 Nutdimensionierung

**Goldene Regel:** Die Nut muss die Dichtung aufnehmen und gleichzeitig genug Raum für die Kompression lassen.

**Berechnungsgrundlagen:**

```python
def calculate_groove_dimensions(
    seal_height_mm: float,
    seal_width_mm: float,
    compression_ratio: float = 0.25,
    tolerance_mm: float = 0.2
) -> dict:
    """Berechnet die empfohlene Nutdimensionierung.

    Args:
        seal_height_mm: Gesamthöhe des Dichtungsprofils in mm
        seal_width_mm: Breite des Dichtungsfußes in mm
        compression_ratio: Gewünschte Kompressionsrate (0.20-0.35)
        tolerance_mm: Fertigungstoleranz in mm (±)

    Returns:
        Dict mit Nutmaßen in mm
    """
    groove_width = seal_width_mm + tolerance_mm  # Leichtgängiges Einsetzen
    groove_depth = seal_height_mm * (1 - compression_ratio)
    # Dichtungskopf ragt (compression_ratio × seal_height) über Nut hinaus
    protrusion = seal_height_mm * compression_ratio

    return {
        "groove_width_mm": round(groove_width, 1),
        "groove_depth_mm": round(groove_depth, 1),
        "seal_protrusion_mm": round(protrusion, 1),
        "compressed_protrusion_mm": 0.0,  # Bei Schließen voll komprimiert
        "groove_width_tolerance_mm": tolerance_mm,
        "groove_depth_tolerance_mm": tolerance_mm + 0.1,
    }
```

**Beispielrechnung Lewmar Ocean 50:**
- Dichtungshöhe: 12mm
- Dichtungsfußbreite: 6mm
- Ziel-Kompression: 25%
- → Nutbreite: 6.2mm (±0.2mm)
- → Nuttiefe: 9mm (±0.3mm)
- → Überstand über Nut: 3mm
- → Bei Schließen wird 3mm komprimiert → 25% von 12mm

#### 7.5.3 Häufige Nutfehler

| Fehler | Symptom | Abhilfe |
|--------|---------|---------|
| Nut zu breit | Dichtung wackelt, rutscht bei Vibration heraus | Shims einsetzen oder dickeres Profil verwenden |
| Nut zu schmal | Dichtung beult sich, ungleichmäßige Kompression | Nut nachfräsen (nur bei Alu möglich) |
| Nut zu flach | Übermäßige Kompression (>40%), schneller Compression Set | Dünneres Profil verwenden |
| Nut zu tief | Zu wenig Kompression (<15%), undicht | Dickeres Profil oder Dichtungskeil unterlegen |
| Nut-Boden nicht plan | Ungleichmäßige Auflage, punktuelle Belastung | Nut nachbearbeiten, Klebestreifen als Ausgleich |
| Nut-Ecken zu scharfkantig | Dichtung wird in Ecken eingeschnitten | Ecken verrunden (R ≥ 0.5mm) |
| Nut verschmutzt | Dichtung sitzt nicht vollständig, Leckage | Nut reinigen, Rückstände von altem Kleber entfernen |

### 7.6 Befestigungsarten: Adhesive-backed vs Press-fit vs Bonded

#### 7.6.1 Press-fit (Formschlüssig eingepresst)

**Prinzip:** Das Dichtungsprofil hat einen Fuß, der breiter ist als die Nuteintrittsöffnung (bei Schwalbenschwanz) oder der durch Eigenspannung in der Nut sitzt (bei Rechtecknut). Kein Kleber erforderlich.

**Vorteile:**
- Sauberste Lösung (kein Kleberrest)
- Einfacher Austausch (herausziehen, neues eindrücken)
- Kein Aushärten nötig (sofort einsatzbereit)
- Dichtung kann sich in der Nut thermisch ausdehnen ohne Spannungen

**Nachteile:**
- Erfordert eng tolerierte Nut
- Kann bei starker Vibration herausrutschen (bei Rechtecknut)
- Nicht für alle Profiltypen geeignet

**Anwendung:** OEM-Standard bei Lewmar, Goiot, Bomar, Seldén. Ca. 70% aller Lukendichtungen im Yachtbau.

**Einbautipps:**
1. Nut vollständig von altem Profil und Kleberresten reinigen
2. Nut mit Isopropanol entfetten
3. Dichtungsprofil probeweise einlegen (ohne Druck) — muss leicht widerständig gleiten
4. An einer Seite beginnen, Profil mit Daumen in die Nut drücken
5. An den Ecken: Profil nicht dehnen, sondern mit leichtem Übermaß (1–2mm) zuschneiden
6. Stoßstelle: Gerade schneiden, Enden stumpf aneinanderlegen
7. Stoßstelle mit Sekundenkleber (Cyanoacrylat, z.B. Loctite 406) fixieren

#### 7.6.2 Adhesive-backed (Selbstklebend)

**Prinzip:** Dichtungsprofil hat auf der Unterseite einen Klebestreifen (meist Acrylatkleber auf Folienträger). Schutzfolie abziehen, Dichtung aufdrücken.

**Vorteile:**
- Einfachste Montage
- Keine Nut erforderlich (kann auf flache Oberfläche geklebt werden)
- Laien-tauglich

**Nachteile:**
- Kleber altert (UV, Feuchtigkeit) — löst sich nach 3–7 Jahren
- Haftet schlecht auf Gelcoat ohne Vorbehandlung
- Nicht repositionierbar (einmal aufgedrückt = endgültig)
- Kleberrest bei Entfernung schwer zu entfernen

**Anwendung:** Aftermarket-Reparatur, Ankerkisten, Lazarette, Staukästen. **Nicht empfohlen** für Decksluken auf See (Kat. A/B).

**Einbautipps:**
1. Oberfläche mit Isopropanol oder Aceton reinigen und entfetten
2. Bei Gelcoat: leicht anschleifen (Korn 220) für bessere Haftung
3. Primer auftragen (z.B. 3M Primer 94, Tesa Primer) — verdoppelt die Haftung
4. Schutzfolie nur abschnittsweise abziehen (nicht die gesamte Länge auf einmal)
5. Andrücken mit Rolle (z.B. Nahtrolle)
6. 24h bei >15°C aushärten lassen vor erstem Schließen
7. Bei Temperaturen <10°C: Kleber mit Heißluftpistole (40–50°C) aktivieren

**Produkte:**
- Meyco: Selbstklebende D-Profile, P-Profile (EUR 2–5/m)
- Deventer: Selbstklebende E-Profile (EUR 3–6/m)
- Tesa: Industrielle Dichtungsprofile mit 3M-Klebebasis
- 3M: Dual Lock Profile (für lösbare Verbindungen)

#### 7.6.3 Bonded (Eingeklebt)

**Prinzip:** Dichtungsprofil wird mit einem separaten Kleber in die Nut eingeklebt. Die Verbindung ist quasi-permanent.

**Kleber-Typen:**

| Kleber | Aushärtezeit | Haltbarkeit | Entfernbarkeit | Preis/Tube |
|--------|-------------|------------|---------------|------------|
| Kontaktkleber (z.B. Bostik 1400) | 15 min | 5–8 Jahre | Mittel (Schaber) | EUR 8–12 |
| Cyanacrylat (z.B. Loctite 406) | 30 sec | 3–5 Jahre | Schwer (Aceton) | EUR 12–18 |
| Silikon-Kleber (z.B. Dow 732) | 24h | 10+ Jahre | Leicht (schneiden) | EUR 10–15 |
| PU-Kleber (z.B. Sikaflex 291) | 48h | 10+ Jahre | Sehr schwer | EUR 12–18 |
| Spezial-Dichtungskleber | 1–4h | 8–12 Jahre | Mittel | EUR 15–25 |

**Empfehlung für marine Lukendichtungen:**
- Erstinstallation: Kontaktkleber (Bostik 1400 oder Renia Colle de Cologne) — löst sich bei Bedarf
- Dauerhafte Installation: Silikon-Kleber (Dow Corning 732, Wacker Elastosil N10) — flexibel, alterungsbeständig
- **Nicht verwenden:** PU-Kleber (Sikaflex) — zu starr, Dichtung kann sich nicht thermisch ausdehnen, Entfernung zerstört Nut

#### 7.6.4 Vergleichsmatrix Befestigungsarten

| Kriterium | Press-fit | Adhesive-backed | Bonded (Kontaktkleber) | Bonded (Silikon) |
|----------|----------|----------------|----------------------|----------------|
| Montageaufwand | Mittel | Gering | Mittel | Mittel |
| Erforderliche Nut | Ja | Nein (flach möglich) | Ja oder flach | Ja oder flach |
| Haltbarkeit | 10+ Jahre (bei passender Nut) | 3–7 Jahre | 5–8 Jahre | 10+ Jahre |
| Austauschbarkeit | Sehr gut | Mäßig (Kleberreste) | Gut | Gut |
| Vibrationsfestigkeit | Gut (Schwalbenschwanz: sehr gut) | Mäßig | Sehr gut | Sehr gut |
| Temperaturfestigkeit | Uneingeschränkt | Eingeschränkt (Kleber erweicht) | Gut | Sehr gut |
| Kosten | Profil-Kosten | Profil + inkl. Kleber | Profil + EUR 8–15 | Profil + EUR 10–15 |
| AYDI-Score Bonus | +5 (Standard) | -5 (für Kat. A/B) | +3 | +5 |

### 7.7 Lecktest-Verfahren (Leak Testing)

#### 7.7.1 Visuelle Inspektion (Confidence: visual_medium bis visual_high)

**Ablauf:**
1. Luke/Fenster von innen inspizieren bei Regen oder nach Wassertest
2. Wasserflecken, Tropfen, Verfärbungen um den Rahmen dokumentieren
3. Dichtung von außen auf Risse, Ablösungen, Verformungen prüfen
4. Stoßstellen und Ecken besonders beachten

**Bewertung:**
- Sichtbare Tropfenbildung: Dichtung undicht (Score ≤30)
- Feuchtigkeitsflecken ohne Tropfen: Mikroleckage möglich (Score 40–60)
- Keine Spuren: Wahrscheinlich dicht (Score ≥70, aber nicht sicher)

#### 7.7.2 Wasserschlauch-Test (Confidence: measured)

**Ablauf nach ISO 12216 Anhang B (vereinfacht):**
1. Eine Person steht mit Gartenschlauch an Deck
2. Zweite Person inspiziert von innen mit Taschenlampe und Papierhandtuch
3. Wasserstrahl aus 1m Entfernung auf geschlossene Luke richten
4. 5 Minuten pro Seite, dann Ecken, dann Stoßstelle
5. Papierhandtuch in alle Ecken des Rahmens drücken

**Bewertung:**
- Kein Tropfen nach 20 min Gesamttest: dicht (Score 90–100)
- Einzelne Tropfen an einer Stelle: punktuelle Leckage (Score 50–70)
- Tropfen an mehreren Stellen: systematische Leckage (Score 20–40)
- Wassereinbruch: Dichtung versagt (Score 0–15)

**Wichtig:** Schlauchtest simuliert nur Regenwasser und leichten Spritzwasser-Druck (~2–5 kPa). Für Kat. A/B Boote ist ein Drucktest aussagekräftiger.

#### 7.7.3 Drucktest (Confidence: measured)

**Ablauf:**
1. Luke von innen mit Druckrahmen und Folie abdichten
2. Druckluft einleiten (z.B. mit Niederdruckpumpe)
3. Druck auf Prüfdruck gemäß ISO 12216 erhöhen (z.B. 6 kPa für Kat. A Decksluke)
4. Halten 5 Minuten
5. Seifenlösung auf Dichtung auftragen — Blasen zeigen Leckage
6. Druckabfall messen: <5% in 5 min = dicht

**Bewertung:**
- Kein Druckabfall, keine Blasen: dicht (Score 95–100)
- Blasen an Stoßstelle: lokale Undichtigkeit (Score 60–80)
- Blasen entlang der Dichtung: Profil-Problem (Score 30–50)
- Deutlicher Druckabfall >10%: systematisch undicht (Score 0–25)

#### 7.7.4 Ultraschall-Leckdetektion (Confidence: measured)

**Prinzip:** Ultraschall-Sender im geschlossenen Raum, Empfänger außen. Schall tritt an undichten Stellen aus und wird lokalisiert.

**Geräte:**
- SDT 200/270 (BE): Profi-Gerät, EUR 3.000–5.000
- UE Systems UltraProbe (USA): Profi-Gerät, EUR 2.500–4.000
- Inficon Whisper (CH): Einfach-Gerät, EUR 800–1.200

**Bewertung:** Genaueste Methode. Lokalisiert Leckagen auf ±5mm. In der Praxis nur bei Superyachts und professionellen Surveys eingesetzt.

---

## 8. Hersteller — Vollständige Übersicht

### 8.1 Lewmar (UK) — Marktführer Lukendichtungen

**Firmenprofil:**
- Sitz: Havant, Hampshire, UK
- Gegründet: 1946
- Segment: Marine Hardware (Luken, Winden, Beschläge)
- Marktanteil Lukendichtungen (Europa, geschätzt): 35–40%
- Website: lewmar.com

**Dichtungsprogramm:**

Lewmar produziert OEM-Dichtungen für alle eigenen Lukenserien. Jede Serie hat ein spezifisches Profil, das nicht zwischen Serien austauschbar ist.

**Serien-Übersicht mit Dichtungszuordnung:**

| Serie | Profiltyp | Material | Teilenummer Dichtung | Shore A | Maße (H×B mm) | Preis/Satz EUR |
|-------|----------|---------|---------------------|---------|-------------|---------------|
| Ocean 10 | D-Profil (modifiziert) | EPDM peroxidvernetzt | 19901010 | 55 | 10×12 | 18–25 |
| Ocean 20 | D-Profil (modifiziert) | EPDM peroxidvernetzt | 19901020 | 55 | 10×12 | 22–30 |
| Ocean 30 | D-Profil (modifiziert) | EPDM peroxidvernetzt | 19901030 | 55 | 12×14 | 28–38 |
| Ocean 40 | D-Profil (modifiziert) | EPDM peroxidvernetzt | 19901040 | 55 | 12×14 | 32–42 |
| Ocean 50 | D-Profil (modifiziert) | EPDM peroxidvernetzt | 19901050 | 55 | 12×14 | 35–48 |
| Ocean 60 | D-Profil (modifiziert) | EPDM peroxidvernetzt | 19901060 | 55 | 14×16 | 42–55 |
| Ocean 70 | D-Profil (modifiziert) | EPDM peroxidvernetzt | 19901070 | 55 | 14×16 | 48–65 |
| Low Profile 20 | Flach-D-Profil | EPDM | 19903020 | 55 | 8×12 | 20–28 |
| Low Profile 30 | Flach-D-Profil | EPDM | 19903030 | 55 | 8×12 | 24–32 |
| Low Profile 40 | Flach-D-Profil | EPDM | 19903040 | 55 | 10×14 | 28–38 |
| Low Profile 50 | Flach-D-Profil | EPDM | 19903050 | 55 | 10×14 | 32–42 |
| Low Profile 60 | Flach-D-Profil | EPDM | 19903060 | 55 | 12×16 | 38–50 |
| Mk2 Standard (alt) | Hohlprofil | EPDM | 19905xxx | 50 | 10×10 | 15–22 |
| Mk2 Medium (alt) | Hohlprofil | EPDM | 19906xxx | 50 | 12×12 | 18–28 |

**Confidence:** documented (Lewmar Katalog 2024/2025). Preise: estimated (Händlerpreise variieren).

**Besonderheiten Lewmar-Dichtungen:**
- Seit 2019: Microban antimikrobielle Technologie in Ocean-Serie — hemmt Schimmelbildung
- Profilquerschnitt ist patentiert — kein exakter Aftermarket-Ersatz verfügbar
- Lewmar verwendet eine Schwalbenschwanznut in Aluminium-Extrusion
- Eckverbindungen: vorvulkanisiert bei allen Kits, nicht geschnitten
- Stoßstelle: eine Stoßstelle pro Dichtung (Enden mit Cyanacrylat fixiert)

**Lewmar Dichtungs-Pflegeprodukte:**
| Produkt | Art.-Nr. | Funktion | Preis EUR |
|---------|---------|----------|----------|
| Lewmar Seal Care | 19700100 | Silikonpflege-Spray für Dichtungen | 12–15 |
| Lewmar Winch Care Kit (inkl. Seal Lube) | 19700500 | Enthält Dichtungspflege | 25–35 |

**Lewmar Aftermarket-Alternativen:**
- Houdini Marine: bietet Nachbau-Dichtungen für Lewmar Mk2 (nicht für Ocean-Serie)
- Meyco/Dichtungsprofi24: EPDM-Meterware in ähnlichen Maßen, aber nicht profilidentisch
- Vetus: bietet generische D-Profile, die für ältere Lewmar-Luken passen können

### 8.2 Goiot Systems (Frankreich) — OEM für Bénéteau/Jeanneau

**Firmenprofil:**
- Sitz: Nantes, Frankreich
- Gegründet: 1978 (als Goiot SA, seit 2015 Goiot Systems)
- Zugehörigkeit: Bénéteau Group (Hauptkunde)
- Segment: Luken, Portlights, Dichtungssysteme
- Website: goiot-systems.com

**Dichtungsprogramm:**

Goiot verwendet ein proprietäres Profilsystem, das sich deutlich von Lewmar unterscheidet. Die Dichtungen sitzen in einer speziellen Kunststoff-Nut (nicht Aluminium).

| Serie | Profiltyp | Material | Ref.-Nr. | Shore A | Maße (H×B mm) | Preis/Satz EUR |
|-------|----------|---------|----------|---------|-------------|---------------|
| Cristal 30 | Doppellippe | EPDM | JOINT-CR30 | 50 | 8×6 | 15–20 |
| Cristal 37 | Doppellippe | EPDM | JOINT-CR37 | 50 | 8×6 | 18–24 |
| Cristal 43 | Doppellippe | EPDM | JOINT-CR43 | 50 | 10×7 | 22–30 |
| Cristal 49 | Doppellippe | EPDM | JOINT-CR49 | 50 | 10×7 | 25–35 |
| Cristal 55 | Doppellippe | EPDM | JOINT-CR55 | 50 | 10×7 | 28–38 |
| Opal 26 | Torpedo-ähnlich | EPDM | JOINT-OP26 | 55 | 12×8 | 20–28 |
| Opal 31 | Torpedo-ähnlich | EPDM | JOINT-OP31 | 55 | 12×8 | 24–32 |
| Opal 38 | Torpedo-ähnlich | EPDM | JOINT-OP38 | 55 | 14×10 | 28–38 |
| Opal 50 | Torpedo-ähnlich | EPDM | JOINT-OP50 | 55 | 14×10 | 35–45 |
| Galaxy (alt) | Hohlprofil | EPDM | JOINT-GAL | 50 | 10×10 | 15–22 |

**Confidence:** documented (Goiot Katalog 2023/2024). Preise: estimated.

**Besonderheiten Goiot-Dichtungen:**
- Proprietäres Profilsystem — Lewmar-Dichtungen passen NICHT in Goiot-Luken und umgekehrt
- Nut ist im GFK-Rahmen integriert (nicht separates Aluminium-Profil)
- Eckverbindungen: geschnitten und stumpf gestoßen (nicht vorvulkanisiert) — Schwachstelle
- Erfahrung (Forum-Konsens, Confidence: documented): Goiot-Dichtungen neigen bei Bénéteau-Booten Bj. 2005–2015 zu vorzeitiger Versprödung nach 5–7 Jahren
- Seit 2018: verbessertes EPDM-Compound mit UV-Stabilisator

**Goiot-Aftermarket:**
- Goiot liefert Ersatzdichtungen direkt und über Händler (Accastillage Diffusion, USHIP)
- Houdini Marine: bietet Nachbau-Profile für ältere Goiot-Serien (Galaxy)
- Eigenanfertigung: Goiot-Nutmaße ermitteln und bei Peters Rubber oder HF Rubber Custom-Profil extrudieren lassen

### 8.3 Houdini Marine (UK) — Spezialist Aftermarket

**Firmenprofil:**
- Sitz: Portsmouth, Hampshire, UK
- Gegründet: 1985
- Segment: Luken und Dichtungen (OEM + Aftermarket)
- Schwerpunkt: Aftermarket-Dichtungen für Lewmar, Goiot, Bomar
- Website: houdinihatches.co.uk

**Dichtungsprogramm:**

| Anwendung | Profiltyp | Material | Ref.-Nr. | Shore A | Maße (H×B mm) | Preis/m EUR |
|-----------|----------|---------|----------|---------|-------------|------------|
| Lewmar Mk2 Nachbau | Hohlprofil | EPDM | HSP-001 | 55 | 10×10 | 4–6 |
| Goiot Galaxy Nachbau | Hohlprofil | EPDM | HSP-002 | 50 | 10×10 | 4–6 |
| Houdini OEM Escape | D-Profil | EPDM UV | HSP-010 | 55 | 12×14 | 5–8 |
| Houdini OEM Sail | D-Profil | EPDM UV | HSP-011 | 55 | 10×12 | 4–7 |
| Universal D-Profil | D-Profil | EPDM | HSP-020 | 55 | 10×12 | 3–5 |
| Universal D-Profil groß | D-Profil | EPDM | HSP-021 | 55 | 14×16 | 5–8 |
| Silikon D-Profil | D-Profil | Silikon | HSP-030 | 50 | 12×14 | 10–15 |

**Confidence:** documented (Houdini Katalog 2024). Preise: estimated.

**Besonderheiten:**
- Einziger Hersteller mit Silikon-Dichtungsprofilen speziell für marine Luken (HSP-030)
- Liefert als Meterware und als vorgeschnittene Kits
- Gute Cross-Referenz-Tabelle auf Website (welche Houdini-Dichtung passt für welche Luke)
- Qualität konsistent gut (Forum-Konsens: documented)

### 8.4 Vetus (Niederlande) — Breit aufgestellt

**Firmenprofil:**
- Sitz: Schiedam, Niederlande
- Gegründet: 1951
- Segment: Marine-Zubehör (Motoren, Luken, Ventilation, Dichtungen)
- Website: vetus.com

**Dichtungsprogramm:**

Vetus bietet OEM-Dichtungen für eigene Luken und generische Ersatzprofile.

| Anwendung | Profiltyp | Material | Art.-Nr. | Shore A | Maße (H×B mm) | Preis/m EUR |
|-----------|----------|---------|----------|---------|-------------|------------|
| Vetus Decksluke BOX | D-Profil | EPDM | BOXSEAL | 55 | 10×12 | 4–6 |
| Vetus Decksluke HOOD | D-Profil | EPDM | HOODSEAL | 55 | 12×14 | 5–7 |
| Vetus Bullaugendichtung PWS | P-Profil | EPDM | PWSSEAL | 50 | 9×5 | 3–5 |
| Vetus Inspektionsdeckel | Flachdichtung | NBR | KITCOVER | 60 | 3×15 | — (Stück) |
| Generisches D-Profil 10mm | D-Profil | EPDM | RUBP10 | 55 | 10×12 | 3–4 |
| Generisches D-Profil 14mm | D-Profil | EPDM | RUBP14 | 55 | 14×16 | 4–6 |
| Silikon-Meterware | Rundschnur | Silikon | SILS6 / SILS8 | 50 | ∅6 / ∅8 | 5–8 |

**Confidence:** documented (Vetus Katalog 2024).

### 8.5 Bomar / Pompanette (USA)

**Firmenprofil:**
- Sitz: Charlevoix, Michigan, USA
- Gegründet: 1960 (Bomar), 2019 übernommen durch Pompanette
- Segment: Luken und Portlights (Primärmarkt: USA)
- Website: bfrpompanette.com

**Dichtungsprogramm:**

| Serie | Profiltyp | Material | Part No. | Shore A | Maße (H×B mm) | Preis/Satz USD |
|-------|----------|---------|----------|---------|-------------|---------------|
| Flagship | D-Profil | EPDM | BOM-SEAL-FL | 55 | 12×14 | 25–40 |
| Voyager | D-Profil | EPDM | BOM-SEAL-VO | 55 | 10×12 | 20–35 |
| Stormproof | Omega | EPDM | BOM-SEAL-SP | 60 | 14×18 | 30–50 |
| Cast Deck Hatch | Flachdichtung | EPDM | BOM-SEAL-CD | 55 | 3×12 | 18–28 |
| Portlight | P-Profil | EPDM | BOM-SEAL-PL | 50 | 8×6 | 15–22 |

**Confidence:** documented (Bomar Katalog 2024). Preise: estimated (USD).

**Besonderheiten:**
- US-Standard-Maße (Inches) — Umrechnung beachten
- Profil nicht kompatibel mit europäischen Herstellern
- In Europa nur über Importeure erhältlich (SVB, Defender)

### 8.6 Seldén (Schweden) — Skandinavischer Markt

**Firmenprofil:**
- Sitz: Göteborg, Schweden
- Gegründet: 1960
- Primär: Mastbauer, seit 2000er auch Decksluken
- Website: sfrn.com

**Dichtungsprogramm:**

| Serie | Profiltyp | Material | Art.-Nr. | Shore A | Maße (H×B mm) | Preis/Satz EUR |
|-------|----------|---------|----------|---------|-------------|---------------|
| Seldén SL Flush 20 | Lip Seal | EPDM | 523-401 | 50 | 8×10 | 22–30 |
| Seldén SL Flush 30 | Lip Seal | EPDM | 523-402 | 50 | 8×10 | 26–35 |
| Seldén SL Flush 40 | Lip Seal | EPDM | 523-403 | 50 | 10×12 | 30–40 |
| Seldén SL Flush 50 | Lip Seal | EPDM | 523-404 | 50 | 10×12 | 35–48 |

**Confidence:** documented (Seldén Katalog 2024).

**Besonderheiten:**
- Flush-Luken mit Lippendichtung (nicht D-Profil) — spezifisches Seldén-System
- Dichtungen nur über Seldén direkt oder autorisierte Händler
- Schwerpunktmarkt: Skandinavien, zunehmend auch Deutschland/NL

### 8.7 Trend Marine (UK) — Fenster- und Windschutzscheiben-Dichtungen

**Firmenprofil:**
- Sitz: Plymouth, Devon, UK
- Gegründet: 1990
- Segment: Marine-Fenster, Windschutzscheiben, Dichtungssysteme
- Website: trendmarine.co.uk

**Dichtungsprogramm:**

| Anwendung | Profiltyp | Material | Ref. | Shore A | Maße (H×B mm) | Preis/m GBP |
|-----------|----------|---------|------|---------|-------------|------------|
| Windschutzscheibe Standard | Bulb-Profil | EPDM | TM-WS-01 | 60 | 14×6 | 5–8 |
| Windschutzscheibe Flush | Flach-Lippenprofil | EPDM | TM-WS-02 | 55 | 10×8 | 6–10 |
| Salonfenster-Rahmen | E-Profil | EPDM | TM-SF-01 | 50 | 12×5 | 4–7 |
| Kabinenfenster | D-Profil | EPDM | TM-KF-01 | 55 | 8×10 | 3–5 |
| Custom Profil | Nach Zeichnung | EPDM/Silikon | TM-CUSTOM | var. | var. | 8–25 |

**Confidence:** documented (Trend Marine Preisliste 2024).

**Besonderheiten:**
- Spezialist für maßgeschneiderte Windschutzscheiben-Dichtungen
- Arbeitet direkt mit Werften (Fairline, Princess, Sunseeker als Kunden)
- Custom-Extrusionen ab 100m Mindestmenge
- Gute Beratung für Retrofit/Refit-Projekte

### 8.8 Peters Rubber (Deutschland) — Custom-Profile

**Firmenprofil:**
- Sitz: Viersen, Nordrhein-Westfalen, Deutschland
- Gegründet: 1946
- Segment: Technische Gummiprofile (nicht exklusiv marine)
- Marine-Anteil: geschätzt 5–10% des Umsatzes
- Website: peters-rubber.de

**Dichtungsprogramm (marine-relevante Auswahl):**

| Profil-Nr. | Profiltyp | Material | Shore A | Maße (H×B mm) | Preis/m EUR | Min. Menge |
|-----------|----------|---------|---------|-------------|------------|-----------|
| PR-D-1012 | D-Profil | EPDM | 55 | 10×12 | 3.50 | 50m |
| PR-D-1214 | D-Profil | EPDM | 55 | 12×14 | 4.20 | 50m |
| PR-D-1416 | D-Profil | EPDM | 55 | 14×16 | 5.10 | 50m |
| PR-P-0905 | P-Profil | EPDM | 55 | 9×5 | 3.00 | 50m |
| PR-T-1004 | Torpedo | EPDM | 55 | 10×4 | 4.50 | 50m |
| PR-O-1418 | Omega | EPDM | 60 | 14×18 | 6.80 | 50m |
| PR-CUSTOM | Nach Zeichnung | EPDM/Silikon/CR | var. | var. | 8–30 | 50m |

**Confidence:** documented (Peters Rubber Preisliste 2024). Mindestmengen: measured.

**Besonderheiten:**
- Custom-Extrusion nach Zeichnung oder Muster
- Kann alte, eingestellte OEM-Profile nachfertigen (mit Muster)
- Werkzeugkosten für Custom-Profil: EUR 500–2.000 (einmalig)
- Vorlaufzeit Custom: 4–8 Wochen
- Qualitätsstandard: DIN 7715, ISO 3302 Toleranzklasse M2
- Erfahrung mit marine Anwendungen (Referenzen: KM Yachtbuilders, Royal Huisman)

### 8.9 Meyco (Deutschland) — Standardprofile Meterware

**Firmenprofil:**
- Sitz: Rödermark, Hessen, Deutschland
- Segment: EPDM-Standardprofile (Fenster, Türen, Industrie)
- Marine-spezifisch: Nein, aber Profile sind marine-geeignet
- Website: meyco.de

**Marine-relevante Profile:**

| Art.-Nr. | Profiltyp | Material | Shore A | Maße (H×B mm) | Preis/m EUR |
|---------|----------|---------|---------|-------------|------------|
| D-3010 | D-Profil | EPDM | 55 | 8×10 | 1.80 |
| D-3011 | D-Profil | EPDM | 55 | 10×12 | 2.20 |
| D-3012 | D-Profil | EPDM | 55 | 12×14 | 2.80 |
| D-3013 | D-Profil | EPDM | 55 | 14×16 | 3.40 |
| P-4010 | P-Profil | EPDM | 55 | 9×5 | 1.90 |
| P-4012 | P-Profil | EPDM | 55 | 12×6 | 2.40 |
| E-5010 | E-Profil | EPDM | 50 | 8×4 | 1.60 |
| E-5012 | E-Profil | EPDM | 50 | 12×5 | 2.10 |
| SK-D-3011 | D-Profil selbstklebend | EPDM | 55 | 10×12 | 3.20 |
| SK-D-3012 | D-Profil selbstklebend | EPDM | 55 | 12×14 | 3.80 |

**Confidence:** documented (Meyco Katalog 2024).

**Besonderheiten:**
- Preisgünstigste Quelle für Standard-EPDM-Profile in DACH
- Nicht marine-zertifiziert, aber Material identisch (EPDM mit Carbon Black)
- Schnelle Lieferung (1–3 Werktage innerhalb Deutschland)
- Keine vorvulkanisierten Ecken — Ecken müssen manuell gestoßen und verklebt werden
- AYDI-Bewertung: als Aftermarket-Lösung akzeptabel, Abzug -5 Punkte gegenüber OEM wegen fehlender profilspezifischer Passung

### 8.10 Deventer Profile (Deutschland) — TPE/EPDM-Systeme

**Firmenprofil:**
- Sitz: Bad Berleburg, Nordrhein-Westfalen, Deutschland
- Gegründet: 1966
- Segment: Dichtungsprofile für Fenster, Türen, Industrie
- Website: deventer-profile.com

**Marine-relevante Profile:**

| Art.-Nr. | Profiltyp | Material | Shore A | Maße (H×B mm) | Preis/m EUR |
|---------|----------|---------|---------|-------------|------------|
| SPV 3042 | E-Profil | TPE | 45 | 8×4 | 1.40 |
| SPV 3045 | E-Profil | TPE | 45 | 12×5 | 1.80 |
| SPV 3126 | D-Profil | TPE | 50 | 10×12 | 2.00 |
| SPV 3128 | D-Profil | TPE | 50 | 12×14 | 2.50 |
| SPV 4055 | Bulb-Profil | TPE | 55 | 10×5 | 2.20 |
| SV 1026 | D-Profil | EPDM | 55 | 10×12 | 2.80 |
| SV 1028 | D-Profil | EPDM | 55 | 12×14 | 3.40 |

**Confidence:** documented (Deventer Katalog 2024).

**Besonderheiten:**
- Primär Architektur-/Bau-Profile, aber TPE-Qualität ist für marine Anwendungen geeignet
- TPE-Profile: recycelbar, aber höherer Compression Set als EPDM
- Selbstklebende Ausführungen verfügbar (Aufpreis +0.80 EUR/m)

### 8.11 Schlegel (Deutschland) — Bürstendichtungen und Schiebefenster

**Firmenprofil:**
- Sitz: Rosenheim, Bayern, Deutschland
- Segment: Dichtungssysteme (Bürsten, Profile) für Fenster und Türen
- Website: schlegel.com

**Marine-Relevanz:**
Schlegel-Bürstendichtungen sind relevant für **Schiebefenster** und **Schiebe-Luken** auf Motor- und Segelyachten.

| Art.-Nr. | Typ | Material | Breite mm | Höhe mm | Preis/m EUR |
|---------|-----|---------|----------|---------|------------|
| SL-7 | Bürstendichtung | PP-Filamente | 6.7 | 7 | 2.50 |
| SL-10 | Bürstendichtung | PP-Filamente | 6.7 | 10 | 3.00 |
| SL-15 | Bürstendichtung | PP-Filamente | 6.7 | 15 | 3.50 |
| Q-LON | Kompressionssdichtung | PU-Schaum + PVC-Hülle | var. | var. | 3–6 |

**Confidence:** documented (Schlegel Katalog 2024).

**Besonderheiten:**
- Bürstendichtungen sind NICHT wasserdicht — nur spritzwasserhemmend und Windschutz
- Geeignet für Schiebefenster in Salon/Steuerhaus, wo Wasserdichtheit sekundär ist
- Q-LON Kompressionssdichtung ist für Fenster-/Türrahmen geeignet, Shore-äquivalent ca. 30

### 8.12 Rehau (Deutschland) — Dichtungssysteme

**Firmenprofil:**
- Sitz: Rehau, Bayern, Deutschland
- Segment: Polymer-Lösungen (Automotive, Bau, Industrie)
- Website: rehau.com

**Marine-Relevanz:**
Rehau ist primär Automotive- und Bau-Zulieferer, bietet aber TPE- und EPDM-Dichtungssysteme, die für marine Custom-Anwendungen adaptiert werden können.

- Custom-Extrusion: Ab 500m Mindestmenge
- Tooling-Kosten: EUR 1.500–5.000
- Vorlaufzeit: 6–12 Wochen
- Relevanz: Nur für Werften mit Serienfertigung (z.B. Bavaria, Hanse)

**Confidence:** estimated (keine publizierten marine-spezifischen Daten).

### 8.13 Osculati (Italien) — Breites Aftermarket-Sortiment

**Firmenprofil:**
- Sitz: Segrate (Mailand), Italien
- Gegründet: 1958
- Segment: Marine-Zubehör (größter Vollsortiment-Anbieter in Südeuropa)
- Website: osculati.com

**Dichtungsprogramm:**

| Art.-Nr. | Anwendung | Profiltyp | Material | Shore A | Preis/m EUR |
|---------|-----------|----------|---------|---------|------------|
| 19.911.01 | Inspektionsdeckel-Dichtung ∅102mm | Flachdichtung | NBR | 60 | — (Stück: 2.50) |
| 19.911.02 | Inspektionsdeckel-Dichtung ∅152mm | Flachdichtung | NBR | 60 | — (Stück: 3.20) |
| 19.911.03 | Inspektionsdeckel-Dichtung ∅203mm | Flachdichtung | NBR | 60 | — (Stück: 4.00) |
| 19.920.01 | D-Profil Meterware 10mm | D-Profil | EPDM | 55 | 3.00 |
| 19.920.02 | D-Profil Meterware 14mm | D-Profil | EPDM | 55 | 4.20 |
| 19.920.05 | P-Profil Meterware | P-Profil | EPDM | 55 | 3.50 |
| 19.925.01 | Bullaugendichtung ∅200mm | O-Ring | EPDM | 55 | — (Stück: 5.50) |
| 19.925.02 | Bullaugendichtung ∅250mm | O-Ring | EPDM | 55 | — (Stück: 6.80) |
| 19.925.03 | Bullaugendichtung ∅300mm | O-Ring | EPDM | 55 | — (Stück: 8.20) |

**Confidence:** documented (Osculati Katalog 2024/2025).

### 8.14 Plastimo (Frankreich) — Französischer Markt

**Firmenprofil:**
- Sitz: Lorient, Bretagne, Frankreich
- Gegründet: 1963
- Segment: Sicherheitsausrüstung, Marine-Zubehör
- Website: plastimo.com

**Dichtungsprogramm:**

| Art.-Nr. | Anwendung | Material | Shore A | Preis EUR |
|---------|-----------|---------|---------|----------|
| 14752 | Inspektionsluk-Dichtung ∅102mm | PVC | 50 | 3.50 (Stück) |
| 14754 | Inspektionsluk-Dichtung ∅152mm | PVC | 50 | 4.80 (Stück) |
| 14756 | Inspektionsluk-Dichtung ∅200mm | PVC | 50 | 6.20 (Stück) |
| 196230 | D-Profil Meterware | EPDM | 55 | 3.80/m |

**Confidence:** documented (Plastimo Katalog 2024).

**Besonderheiten:**
- Plastimo-Inspektionsluk-Dichtungen verwenden PVC — nicht für Dauerexposition empfohlen
- Marine-Fachhandel in Frankreich liefert meist Plastimo als Erstquelle

### 8.15 Weitere Hersteller (Kurzprofile)

#### Freeman Marine (USA)
- Sitz: Gold Beach, Oregon, USA
- Segment: Superyacht-Luken und -Türen (>24m)
- Dichtungen: Custom Omega-Profile und Torpedo-Profile, EPDM und Silikon
- Preise: EUR 15–40/m (Premium-Segment)
- Confidence: documented

#### Atkins & Hoyle (UK)
- Sitz: UK
- Segment: Superyacht-Fenster
- Dichtungen: Custom Bulb-Profile und Flachdichtungen für gebogene Glasfenster
- Preise: individuell (Superyacht-Preisklasse)
- Confidence: estimated

#### Lalizas (Griechenland)
- Sitz: Piräus, Griechenland
- Segment: Marine-Zubehör (günstig)
- Dichtungen: generische D-Profile, Inspektionsdeckel-Dichtungen
- Preis: EUR 1.50–3/m (günstigstes Segment)
- Confidence: documented
- AYDI-Bewertung: Budget-Option, Abzug -10 Punkte gegenüber Premium-Herstellern

#### New Found Metals (USA)
- Sitz: Port Townsend, Washington, USA
- Segment: Bronze-Luken und -Bullaugen (Premium/Klassik)
- Dichtungen: Custom EPDM-Flachdichtungen und D-Profile für eigene Bronze-Luken
- Preise: EUR 8–15/Stück
- Confidence: documented

#### R&D Marine (UK)
- Sitz: UK
- Segment: Stuffing Boxes und Dichtungen
- Marine-Dichtungen: primär Wellendichtungen, aber auch Luken-Dichtungsringe
- Confidence: estimated

#### Raboesch (Niederlande)
- Sitz: Oss, Niederlande
- Segment: Kunststoff-Extrusionen
- Profile: PVC und TPE-Fensterprofile, teilweise als Dichtungsrahmen für Fenster verwendbar
- Preise: EUR 2–6/m
- Confidence: documented

---

## 9. Anlagen-spezifische Zuordnung

### 9.1 Decksluken (Deck Hatches)

#### 9.1.1 Anforderungen an Deckslukendichtungen

Decksluken sind die kritischste Anwendung für marine Dichtungen, da sie:
- Direkter Grünwasser-Übernahme ausgesetzt sind (besonders Vordeck-Luken)
- Begehbare Fläche bilden (mechanische Zusatzbelastung)
- Permanenter UV-Exposition unterliegen
- Häufig geöffnet und geschlossen werden (>500 Zyklen/Saison)
- Extremen Temperaturdifferenzen ausgesetzt sind (Deckstemperatur bis +85°C, Innenraum 20°C)

**Mindestanforderungen nach CE-Kategorie:**

| Anforderung | Kat. A | Kat. B | Kat. C | Kat. D |
|------------|--------|--------|--------|--------|
| Druckbelastbarkeit | ≥6 kPa | ≥4 kPa | ≥2 kPa | ≥1 kPa |
| Compression Set (max.) | 25% | 30% | 40% | 50% |
| UV-Beständigkeit | Pflicht | Pflicht | Empfohlen | Optional |
| Shore A (empfohlen) | 55–65 | 50–60 | 45–55 | 40–55 |
| Material (empfohlen) | EPDM-Peroxid/Silikon | EPDM | EPDM/TPV | EPDM/TPE |
| Ermüdungszyklen | 20.000 | 15.000 | 10.000 | 5.000 |

#### 9.1.2 Dichtungszuordnung nach Lukenhersteller

**Lewmar:**

| Lukenserie | Baujahr | Dichtungs-PN | Profil | Material | Meterpreis EUR | Kit-Preis EUR |
|-----------|---------|-------------|--------|---------|-------------|-------------|
| Ocean 10 | 2005– | 19901010 | D mod. | EPDM-P | — | 18–25 |
| Ocean 20 | 2005– | 19901020 | D mod. | EPDM-P | — | 22–30 |
| Ocean 30 | 2005– | 19901030 | D mod. | EPDM-P | — | 28–38 |
| Ocean 40 | 2005– | 19901040 | D mod. | EPDM-P | — | 32–42 |
| Ocean 50 | 2005– | 19901050 | D mod. | EPDM-P | — | 35–48 |
| Ocean 60 | 2005– | 19901060 | D mod. | EPDM-P | — | 42–55 |
| Ocean 70 | 2005– | 19901070 | D mod. | EPDM-P | — | 48–65 |
| Low Profile 20 | 2008– | 19903020 | Flach-D | EPDM | — | 20–28 |
| Low Profile 30 | 2008– | 19903030 | Flach-D | EPDM | — | 24–32 |
| Low Profile 40 | 2008– | 19903040 | Flach-D | EPDM | — | 28–38 |
| Low Profile 50 | 2010– | 19903050 | Flach-D | EPDM | — | 32–42 |
| Low Profile 60 | 2010– | 19903060 | Flach-D | EPDM | — | 38–50 |
| Mk2 Std Size 20 | 1990–2005 | 19905020 | Hohlprofil | EPDM | — | 15–22 |
| Mk2 Std Size 30 | 1990–2005 | 19905030 | Hohlprofil | EPDM | — | 18–25 |
| Mk2 Std Size 40 | 1990–2005 | 19905040 | Hohlprofil | EPDM | — | 20–28 |
| Mk2 Std Size 50 | 1990–2005 | 19905050 | Hohlprofil | EPDM | — | 22–30 |
| Mk2 Std Size 60 | 1990–2005 | 19905060 | Hohlprofil | EPDM | — | 25–35 |
| Mk2 Med Size 30 | 1990–2005 | 19906030 | Hohlprofil | EPDM | — | 22–30 |
| Mk2 Med Size 40 | 1990–2005 | 19906040 | Hohlprofil | EPDM | — | 25–32 |
| Mk2 Med Size 50 | 1990–2005 | 19906050 | Hohlprofil | EPDM | — | 28–38 |
| Mk2 Med Size 60 | 1990–2005 | 19906060 | Hohlprofil | EPDM | — | 30–42 |

**Goiot:**

| Lukenserie | Baujahr | Dichtungs-Ref. | Profil | Material | Kit-Preis EUR |
|-----------|---------|---------------|--------|---------|-------------|
| Cristal 30 | 2000– | JOINT-CR30 | Doppellippe | EPDM | 15–20 |
| Cristal 37 | 2000– | JOINT-CR37 | Doppellippe | EPDM | 18–24 |
| Cristal 43 | 2000– | JOINT-CR43 | Doppellippe | EPDM | 22–30 |
| Cristal 49 | 2000– | JOINT-CR49 | Doppellippe | EPDM | 25–35 |
| Cristal 55 | 2000– | JOINT-CR55 | Doppellippe | EPDM | 28–38 |
| Opal 26 | 2010– | JOINT-OP26 | Torpedo-ähnl. | EPDM | 20–28 |
| Opal 31 | 2010– | JOINT-OP31 | Torpedo-ähnl. | EPDM | 24–32 |
| Opal 38 | 2010– | JOINT-OP38 | Torpedo-ähnl. | EPDM | 28–38 |
| Opal 50 | 2010– | JOINT-OP50 | Torpedo-ähnl. | EPDM | 35–45 |
| Galaxy 30 (alt) | 1990–2005 | JOINT-GAL30 | Hohlprofil | EPDM | 15–22 |
| Galaxy 37 (alt) | 1990–2005 | JOINT-GAL37 | Hohlprofil | EPDM | 18–25 |
| Galaxy 43 (alt) | 1990–2005 | JOINT-GAL43 | Hohlprofil | EPDM | 20–28 |

**Bomar:**

| Lukenserie | Dichtungs-PN | Profil | Material | Kit-Preis USD |
|-----------|-------------|--------|---------|-------------|
| Flagship 10×10" | BOM-SEAL-FL10 | D | EPDM | 25–35 |
| Flagship 14×14" | BOM-SEAL-FL14 | D | EPDM | 30–40 |
| Flagship 18×18" | BOM-SEAL-FL18 | D | EPDM | 35–48 |
| Flagship 22×22" | BOM-SEAL-FL22 | D | EPDM | 40–55 |
| Voyager 10×10" | BOM-SEAL-VO10 | D | EPDM | 20–30 |
| Voyager 14×14" | BOM-SEAL-VO14 | D | EPDM | 25–35 |
| Stormproof (alle) | BOM-SEAL-SP | Omega | EPDM | 30–50 |

#### 9.1.3 Deckslukendichtung — Austauschverfahren

**Werkzeug:**
- Kleiner Schlitzschraubendreher (stumpf, um Nut nicht zu beschädigen)
- Isopropanol (99%) + fusselfreies Tuch
- Silikonspray (z.B. WD-40 Specialist Silikon)
- Sekundenkleber (Loctite 406 oder Loctite 480 für Elastomere)
- Cutter/Skalpell
- Messschieber (Schieblehre)
- Neues Dichtungsprofil (OEM oder Aftermarket)

**Schrittfolge:**

1. **Altes Profil entfernen:**
   - Luke öffnen und arretieren
   - An einer Ecke beginnen: mit stumpfem Schraubendreher vorsichtig den Fuß aus der Nut hebeln
   - Profil gleichmäßig herausziehen, nicht reißen (Fußreste in der Nut sind schwer zu entfernen)
   - Arbeitszeit: 10–20 min pro Luke

2. **Nut reinigen:**
   - Alte Kleberreste mechanisch entfernen (Kunststoff-Schaber, kein Metall bei Alu-Rahmen)
   - Nut mit Isopropanol reinigen und entfetten
   - Trocknen lassen (5 min)
   - Nut auf Beschädigungen prüfen (Grate, Verformungen, Korrosion)
   - Arbeitszeit: 15–30 min pro Luke

3. **Nut vermessen:**
   - Nutbreite mit Messschieber messen (an 4+ Stellen)
   - Nuttiefe messen
   - Mit Profilspezifikation abgleichen
   - Bei Abweichungen >0.5mm: Nut nachbearbeiten oder anderes Profil wählen

4. **Neues Profil einsetzen:**
   - Profil probeweise einlegen (ohne Kleber)
   - An einer Ecke beginnen, im Uhrzeigersinn vorgehen
   - Profil nicht dehnen (max. 1–2% Dehnung)
   - An den Ecken: Profil mit Übermaß (1mm) zuschneiden, nicht auf Gehrung schneiden
   - Stoßstelle idealerweise in der Mitte einer Seite platzieren (nicht in der Ecke)
   - Stoßstelle: Enden gerade und sauber schneiden, stumpf aneinanderlegen
   - Stoßstelle mit Sekundenkleber fixieren (Loctite 406: 1 Tropfen, 30 sec andrücken)
   - Arbeitszeit: 15–30 min pro Luke

5. **Funktionstest:**
   - Luke schließen: Dichtung muss gleichmäßig komprimiert werden
   - Visuell prüfen: keine Wellen, Beulen, offene Stoßstellen
   - Verschlussmechanismus muss ohne übermäßige Kraft schließen
   - Wasserschlauch-Test empfohlen (siehe Abschnitt 7.7.2)

**Gesamtarbeitszeit pro Luke:** 45–90 min (abhängig von Lukengröße und Zustand der Nut)

**Arbeitskosten (Werft/Boatyard):**
- Deutschland: EUR 60–90/Stunde → EUR 45–135 pro Luke
- Südeuropa: EUR 40–60/Stunde → EUR 30–90 pro Luke
- UK: GBP 50–80/Stunde → GBP 37–120 pro Luke

### 9.2 Bullaugen (Portlights)

#### 9.2.1 Anforderungen

Bullaugendichtungen unterscheiden sich von Deckslukendichtungen in mehreren Aspekten:

- **Geringere dynamische Belastung:** Bullaugen sind in der Bordwand, nicht auf Deck — weniger Grünwasser
- **Höherer statischer Druck:** Bei Lage (Krängung) kann das Bullauge teilweise unter Wasser sein
- **Kleinerer Umfang:** Typisch 600–1200mm Umfang vs. 1500–3000mm bei Decksluken
- **Zwei Typen:** Feststehend (Gummirahmen-Verglasung) und öffnend (Klappmechanismus mit Dichtung)

#### 9.2.2 Dichtungszuordnung Bullaugen

**Feststehende Bullaugen:**
Verglasung ist mit einer Dichtungsmasse (Silikon, PU) und/oder einer Rahmendichtung eingesetzt. Kein austauschbares Profil — bei Undichtigkeit muss die Verglasung neu abgedichtet werden (→ Wissensdatei 02.04 Silikon-Dichtstoffe).

**Öffnende Bullaugen:**

| Hersteller | Serie | Dichtungstyp | Material | Ref.-Nr. | Preis EUR |
|-----------|-------|-------------|---------|----------|----------|
| Lewmar | New Standard Portlight | O-Ring + Flachdichtung | EPDM | 19940xxx | 8–15/Stück |
| Lewmar | Atlantic Portlight | Lippendichtung | EPDM | 19942xxx | 10–18/Stück |
| Vetus | PWS Serie | P-Profil | EPDM | PWSSEAL | 5–10/Stück |
| Vetus | PQ Serie | Flachdichtung | EPDM | PQSEAL | 4–8/Stück |
| Goiot | Cristal Portlight | Lippendichtung | EPDM | JOINT-CPL | 8–12/Stück |
| Bomar | Cast Portlight | Flachdichtung | EPDM | BOM-PL-SEAL | 8–14/Stück |
| Osculati | Standard Portlight | O-Ring | EPDM | 19.925.xx | 5–9/Stück |
| Gebo | Flushline | Rahmendichtung | EPDM/Silikon | GBO-FL-SEAL | 12–20/Stück |

**Confidence:** documented (Herstellerkataloge 2024).

#### 9.2.3 Bullaugendichtung — Austauschverfahren

**Öffnendes Bullauge mit Lippendichtung:**
1. Bullauge öffnen und arretieren
2. Alte Dichtung vorsichtig aus Nut/Rahmen lösen
3. Nut/Kontaktfläche reinigen (Isopropanol)
4. Neue Dichtung einsetzen (meist als vorgeformter Ring geliefert)
5. Schließen und Funktion prüfen
6. Arbeitszeit: 15–30 min pro Bullauge

**Feststehendes Bullauge (Neuabdichtung):**
1. Schrauben lösen (meist 6–12 Stück, Edelstahl M4–M6)
2. Glas vorsichtig abheben
3. Alte Dichtungsmasse mit Kunststoffschaber und Silikonentferner (z.B. Bostik Silikonlöser) entfernen
4. Rahmen und Glas reinigen
5. Neue Dichtungsmasse auftragen (Sikaflex 295 UV oder Dow 795 empfohlen)
6. Glas einsetzen, Schrauben gleichmäßig anziehen (Kreuzanziehverfahren)
7. Überschuss nach Aushärtung (48h) abschneiden
8. Arbeitszeit: 30–60 min pro Bullauge (+ 48h Aushärtung)

### 9.3 Windschutzscheiben (Windshields)

#### 9.3.1 Anforderungen

Windschutzscheiben auf Motoryachten und Segelyachten mit Steuerhaus stellen besondere Anforderungen:

- **Große Fläche:** Windschutzscheiben können 1–3m² groß sein
- **Gebogene Form:** Oft gewölbt (2D oder 3D-Biegung)
- **Hohe Druckbelastung:** Frontale Wellenbelastung (Kat. A/B: 8–15 kPa)
- **Vibration:** Motorvibrationen (besonders bei Gleitern)
- **Thermische Ausdehnung:** Große Temperaturunterschiede Innen/Außen → Scheibe und Rahmen dehnen sich unterschiedlich aus

#### 9.3.2 Dichtungssysteme für Windschutzscheiben

**System 1: Direktverglasung (bonded-in)**
- Scheibe ist direkt mit PU-Kleber (z.B. Sikaflex 295 UV, Ködistik S690) in den Rahmen eingeklebt
- Keine austauschbare Dichtung — der Kleber IST die Dichtung
- Typisch für moderne Motoryachten (Fairline, Princess, Sunseeker)
- Lebensdauer: 15–25 Jahre (PU-Kleber)
- Reparatur: Scheibe herausschneiden, neu verkleben — EUR 500–2.000 pro Scheibe (Arbeit + Material)

**System 2: Rahmenverglasung mit Profildichtung**
- Scheibe sitzt in einem Aluminium- oder Edelstahl-Rahmen mit Dichtungsprofil
- Profil ist austauschbar
- Typisch für ältere Yachten und Segelyachten mit Steuerhaus

| Dichtungslösung | Profiltyp | Hersteller | Eignung |
|----------------|----------|-----------|---------|
| Bulb-Profil in Alu-Rahmen | Bulb | Trend Marine, Peters Rubber | Standard für Alu-Rahmen |
| U-Profil (Einfassung) | U-Kanal | Raboesch, Deventer | Für gerade Kanten |
| H-Profil (Verbinder) | H-Kanal | Raboesch | Für mehrteilige Scheiben |
| Klemmprofil | Torpedo + Deckleiste | Trend Marine | Premium, vibrationsresistent |

#### 9.3.3 Dichtungszuordnung Windschutzscheiben

| Hersteller | Profil | Material | Maße mm | Preis/m EUR | Eignung |
|-----------|--------|---------|--------|------------|---------|
| Trend Marine TM-WS-01 | Bulb | EPDM | 14×6 | 5–8 | Alu-Rahmen, gerade |
| Trend Marine TM-WS-02 | Flach-Lippe | EPDM | 10×8 | 6–10 | Flush-Montage |
| Trend Marine TM-WS-03 | Bulb | Silikon | 14×6 | 12–18 | Premium, UV-intensiv |
| Peters Rubber PR-B-1406 | Bulb | EPDM | 14×6 | 5–7 | Custom, Mindestmenge 50m |
| Deventer SPV 4055 | Bulb | TPE | 10×5 | 2.20 | Budget, eingeschränkt |
| Raboesch U-1008 | U-Kanal | PVC/TPE | 10×8 | 3–5 | Kantenumfassung |

### 9.4 Companionway / Niedergang

#### 9.4.1 Anforderungen

Der Niedergang (Companionway) ist der Hauptzugang zum Bootsinneren. Die Dichtungssituation ist komplex:

- **Schiebebretter (Washboards):** Mehrere Bretter übereinander, jedes mit eigener Dichtfläche
- **Schiebeluk (Sliding Hatch):** Schiebemechanismus erfordert Lippendichtung oder Bürstendichtung
- **Schwelle (Sill):** Bodenseitige Dichtung gegen Schwallwasser
- **Häufige Nutzung:** >10× täglich im Sommerbetrieb

#### 9.4.2 Dichtungszuordnung Companionway

| Komponente | Dichtungstyp | Material | Shore A | Empfohlenes Profil |
|-----------|-------------|---------|---------|-------------------|
| Washboard Seitenfläche | Lippendichtung oder D-Profil | EPDM | 45–55 | L-6/8 oder D-10/12 |
| Washboard Unterseite | Flachdichtung oder Lippendichtung | EPDM | 50–60 | FG-3/15 oder L-6/8 |
| Sliding Hatch Seitenlauf | Bürstendichtung | PP-Filamente | — | Schlegel SL-7 |
| Sliding Hatch Vorderkante | D-Profil oder Lippendichtung | EPDM | 45–55 | D-10/12 |
| Schwelle | Lippendichtung | EPDM | 50–60 | L-10/12 |
| Companionway-Tür (Motoryacht) | D-Profil oder E-Profil | EPDM | 50–60 | D-12/14 oder E-12/5 |

**Confidence:** estimated (abhängig von spezifischem Boot).

#### 9.4.3 Schwellenhöhen nach CE-Kategorie (ISO 12216)

| CE-Kategorie | Mindest-Schwellenhöhe | Dichtungsrelevanz |
|-------------|----------------------|------------------|
| A (Hochsee) | 300 mm | Dichtung muss 300mm Wasserstand standhalten |
| B (Offshore) | 250 mm | Dichtung muss 250mm Wasserstand standhalten |
| C (Küste) | 150 mm | Spritzwasserdichtheit ausreichend |
| D (Geschützt) | 0 mm (keine Anforderung) | Regendichtheit ausreichend |

### 9.5 Maschinenraumluken (Engine Room Hatches)

#### 9.5.1 Besondere Anforderungen

Maschinenraumluken haben spezifische Anforderungen, die sich von Decksluken unterscheiden:

- **Brandschutz (ISO 9094):** Dichtungsmaterial muss selbstverlöschend sein
- **Ölbeständigkeit:** Motoröl, Hydrauliköl, Diesel können auf Dichtung gelangen
- **Schalldämmung:** Dichtung muss auch als Schallbrücken-Unterbrecher wirken
- **Vibrationsdämpfung:** Motorbetrieb erzeugt dauerhafte Vibrationen
- **Ventilation:** Maschinenraum braucht Belüftung — Dichtung darf nicht die gesamte Öffnung hermetisch verschließen

#### 9.5.2 Materialeignung Maschinenraumluken

| Material | Ölbeständigkeit | Flammwidrig | Schalldämmung | Empfehlung |
|---------|----------------|------------|--------------|-----------|
| EPDM | Schlecht | Bedingt (mit Zusatz) | Gut | Nur wenn kein Ölkontakt |
| Silikon | Mäßig | Gut (inhärent) | Mäßig | Gute Allround-Lösung |
| Neopren/CR | Gut | Gut (inhärent) | Gut | Klassische Wahl für Maschinenraum |
| NBR | Sehr gut | Schlecht | Mäßig | Nur für ölexponierte Inspektionsdeckel |
| FKM (Viton) | Hervorragend | Gut | Mäßig | Premium, wenn Ölkontakt + Hitze |

**AYDI-Empfehlung:**
- Standard-Maschinenraumluke (kein direkter Ölkontakt): Silikon oder EPDM mit Flammschutzzusatz
- Maschinenraumluke mit Ölkontakt-Risiko: Neopren/CR oder FKM
- Inspektionsdeckel im Motorbereich: NBR (Flachdichtung)
- Schalldämmende Auflage: Omega-Profil mit erhöhter Wandstärke (>3mm)

#### 9.5.3 Dichtungszuordnung Maschinenraumluken

| Anwendung | Empfohlenes Profil | Material | Shore A | Maße mm | Zusatzanforderung |
|-----------|-------------------|---------|---------|--------|------------------|
| Hauptzugangsluke | Omega Ω-14/18 | CR oder Silikon | 55–65 | 14×18 | Flammwidrig, vibrationsdämpfend |
| Seitliche Inspektionsluke | D-12/14 | CR oder EPDM | 55–60 | 12×14 | Ölbeständig wenn ölexponiert |
| Inspektionsdeckel (Schrauben) | Flachdichtung FG-3/15 | NBR | 60 | 3×15 | Ölbeständig |
| Abgasschacht-Deckel | Flachdichtung | FKM | 70 | 5×20 | Temperaturbeständig >200°C |
| Schalldämmklappe | Omega Ω-18/22 | CR | 55 | 18×22 | Schalldämmend |

**Confidence:** estimated (materialabhängig, bootspezifisch).

#### 9.5.4 Ventilationsanforderung und Dichtung

Gemäß ISO 9094 muss der Maschinenraum eine minimale Ventilationsfläche aufweisen:

```
min_ventilation_m2 = max(0.05, engine_kw × 0.0003)
```

Die Dichtung darf diese Ventilation nicht behindern. Lösungsansätze:
- Separate Ventilationsöffnungen (unabhängig von Luke)
- Luken mit integriertem Lüftungskanal (Dichtung umschließt den Kanal)
- Hinterlüftete Dichtung (Profil mit Drainage-Kanälen im Fuß)

---

> **Ende der ersten ~2000 Zeilen der Wissensdatei 08.05**
>
> Die folgenden Abschnitte werden in einer Erweiterung behandelt:
> - Bootshersteller-Dichtungs-Zuordnungsmatrix (Bavaria, Hanse, Jeanneau, Bénéteau, Hallberg-Rassy, Najad, etc.)
> - Einbau- und Austausch-Detailanleitungen
> - Lebensdauer und Klimaeinfluss
> - Diagnose undichter Luken und Fenster
> - Notlösungen und Provisorien
> - Preisvergleiche und Kostenkalkulation
> - Forum-Threads und Eigner-Erfahrungen
> - AYDI-Bewertungsschema und Scoring-Algorithmen
> - Fallstudien
> - Fehlerbild-Atlas für visuelle Analyse (Pipeline B)

---

## Technische Referenz & Berechnungen

### Kompressionskraft-Berechnung

Die Anpresskraft einer Dichtung hängt von Profilquerschnitt, Shore-Härte und Kompressionsgrad ab.

**Formel:**
```
F_compression = A_seal × E_material × (ΔL / L₀)

Wobei:
  A_seal       = Querschnittsfläche der Dichtung [mm²]
  E_material   = E-Modul des Elastomers [MPa]
  ΔL           = Stauchweg [mm]
  L₀           = ursprüngliche Profilhöhe [mm]
```

**Typische E-Module für Dichtungsmaterialien:**

| Material | Shore-Härte | E-Modul [MPa] | Einsatzbereich |
|----------|-------------|----------------|----------------|
| EPDM weich | 40 Shore A | 1,5–2,0 | Fenster, Luken Standard |
| EPDM mittel | 55 Shore A | 3,0–4,0 | Luken, Niedergang |
| EPDM hart | 70 Shore A | 6,0–8,0 | Maschinenraum, Druckluken |
| Silikon | 40 Shore A | 1,2–1,8 | Fenster, UV-exponiert |
| Silikon | 60 Shore A | 3,5–5,0 | Spezialanwendungen |
| Neopren | 50 Shore A | 2,5–3,5 | Unterwasserbereich |
| Neopren | 65 Shore A | 5,0–7,0 | Druckdichtungen |
| PVC flexibel | 60 Shore A | 3,0–4,5 | Kostengünstige Anwendungen |
| Butylkautschuk | 45 Shore A | 1,8–2,5 | Vibrationsdämpfung |

### Optimaler Kompressionsgrad

| Profiltyp | Min. Kompression | Optimal | Max. Kompression |
|-----------|------------------|---------|------------------|
| Rundschnur (O-Ring) | 15 % | 20–25 % | 30 % |
| Hohlprofil | 20 % | 25–35 % | 40 % |
| Lippendichtung | 10 % (Anpressung) | 15–20 % | 25 % |
| Flachdichtung | 10 % | 15–20 % | 25 % |
| P-Profil | 20 % | 30–40 % | 50 % |
| D-Profil | 15 % | 25–35 % | 45 % |
| E-Profil | 20 % | 30–40 % | 50 % |

**Warngrenze AYDI-Score:** Kompression <10 % → Score ≤30 (ungenügend). Kompression >50 % → Score ≤40 (Überkompression, Ermüdung).

### Nutmaße und Profilquerschnitte

**Standard-Nutdimensionen für Yacht-Luken:**

| Nuttyp | Nutbreite [mm] | Nuttiefe [mm] | Dichtungshöhe [mm] | Dichtungsbreite [mm] |
|--------|----------------|---------------|---------------------|----------------------|
| Lewmar Mk2 Luken | 10,0 ± 0,3 | 8,0 ± 0,3 | 12,0 | 9,5 |
| Lewmar Ocean-Serie | 12,0 ± 0,3 | 9,0 ± 0,3 | 14,0 | 11,5 |
| Goiot Cristal | 8,0 ± 0,5 | 7,0 ± 0,5 | 10,0 | 7,5 |
| Goiot Opal | 9,0 ± 0,5 | 7,5 ± 0,5 | 11,0 | 8,5 |
| Bomar Typ G/N | 11,0 ± 0,3 | 8,5 ± 0,3 | 13,0 | 10,5 |
| Moonlight Luke | 7,5 ± 0,5 | 6,5 ± 0,5 | 9,5 | 7,0 |
| Vetus Libero | 9,5 ± 0,3 | 7,5 ± 0,3 | 11,5 | 9,0 |
| Houdini Luke | 10,0 ± 0,5 | 8,0 ± 0,5 | 12,5 | 9,5 |
| Manship Luke | 8,5 ± 0,5 | 7,0 ± 0,5 | 10,5 | 8,0 |

**Standard-Nutdimensionen für Yacht-Fenster:**

| Fenstertyp | Rahmennut [mm] | Glasfalztiefe [mm] | Dichtungsstärke [mm] |
|------------|----------------|---------------------|----------------------|
| Feststehend eingeklebt | – (Verklebung) | 15–20 | Sikaflex-Raupe 5–8 |
| Feststehend im Rahmen | 6,0 × 4,0 | 12–15 | 6,0 × 3,5 |
| Schiebefenster Alu | 8,0 × 5,0 | 10–12 | 7,5 × 4,5 |
| Klappfenster | 7,0 × 5,0 | 12–15 | 6,5 × 4,5 |
| Bullauge 150 mm | 5,0 × 4,0 | 8–10 | 4,5 × 3,5 |
| Bullauge 200 mm | 6,0 × 4,5 | 10–12 | 5,5 × 4,0 |
| Bullauge 250 mm+ | 7,0 × 5,0 | 12–15 | 6,5 × 4,5 |

### Dichtungs-Querschnittprofile

**Profiltypen und Anwendungen:**

| Profil | Querschnitt [mm] | Typische Anwendung | AYDI-Modul |
|--------|-------------------|--------------------|----|
| Rundschnur Ø6 | ∅ 6,0 | Bullaugen, kleine Luken | materials, compliance |
| Rundschnur Ø8 | ∅ 8,0 | Mittlere Luken | materials, compliance |
| Rundschnur Ø10 | ∅ 10,0 | Große Luken, Niedergang | materials, compliance |
| Hohlprofil 12×8 | 12,0 × 8,0 | Standard-Luken | materials |
| Hohlprofil 15×10 | 15,0 × 10,0 | Ocean-Luken, Niedergang | materials |
| P-Profil 9×5 | 9,0 × 5,0 | Fensterrahmen | materials |
| D-Profil 12×8 | 12,0 × 8,0 | Türen, große Luken | materials |
| E-Profil 10×4 | 10,0 × 4,0 | Schiebefenster, Schiebeluken | materials |
| Lippenprofil 15×3 | 15,0 × 3,0 | Niedergangsschiebeluken | materials |
| Flachprofil 20×3 | 20,0 × 3,0 | Klappen, Inspektionsöffnungen | materials |

### Berechnung der Dichtlänge

```
L_seal = Umfang der Öffnung + 5–10 mm Zugabe (Stoß)

Rechteck-Luke: L = 2 × (B + H) + 2 × π × r_ecke + 8 mm
  r_ecke = Eckenradius (typisch 15–30 mm)

Rundes Bullauge: L = π × D_innen + 6 mm

Ovales Fenster: L ≈ π × √((a² + b²)/2) + 8 mm
  a = halbe Längsachse, b = halbe Querachse
```

---

## Einbau-/Austausch-Anleitung

### Vorbereitung

**Werkzeugliste:**
- Dichtungs-Auszieher (Kunststoff oder Messing, niemals Stahl)
- Silikonentferner / Isopropanol 99 %
- Aceton (nur für GFK-Oberflächen, NICHT für Acrylglas)
- Schleifpapier P180 und P320 (nur bei Klebedichtungen)
- Primer je nach Dichtungshersteller (z. B. Sika Primer-206 G+P)
- Kartuschenpresse mit Dosieraufsatz
- Abklebeband 3M 2090 (UV-beständig)
- Talkumpuder (für Einsetzen von Profildichtungen)
- Spiegel und Taschenlampe (Inspektion)
- Drehmomentschlüssel (bei verschraubten Luken)

**Materialbedarf pro Luke (Beispiel Lewmar Mk2, 500×500 mm):**
- Dichtungsprofil: ~2.200 mm (inkl. Zugabe)
- Silikonentferner: ~50 ml
- Primer: ~20 ml
- Kleber (falls Klebemontage): ~30 ml
- Abklebeband: ~3 m
- Kosten Material: 35–65 EUR

### Schritt-für-Schritt: Profildichtung in Nut austauschen

**Schritt 1: Alte Dichtung entfernen (15–30 min)**
1. Luke/Fenster öffnen und arretieren
2. Dichtung am Stoß lokalisieren (meist in einer Ecke)
3. Mit Kunststoff-Auszieher Dichtung aus der Nut hebeln
4. Langsam und gleichmäßig ziehen, nicht reißen
5. Reste in der Nut mit Isopropanol und Lappen entfernen
6. Nut auf Korrosion, Risse oder Verformung prüfen

**Schritt 2: Nutinspektion und -vorbereitung (10–15 min)**
1. Nut mit Druckluft oder Pinsel reinigen
2. Nuttiefe und -breite an 4 Stellen messen (Schieblehre)
3. Abweichungen >0,5 mm dokumentieren
4. Bei Alu-Rahmen: Korrosion mit Scotch-Brite entfernen
5. Bei GFK-Rahmen: Risse mit Epoxy-Spachtel ausbessern
6. Oberfläche mit Isopropanol entfetten

**Schritt 3: Neue Dichtung einsetzen (20–40 min)**
1. Dichtungsprofil auf Raumtemperatur bringen (min. 15 °C)
2. Profil trocken in die Nut probeeinlegen (ohne Kleber)
3. Passgenauigkeit prüfen: Profil soll ohne Kraftaufwand einrasten
4. Bei Klemmprofilen: Talkumpuder in die Nut stäuben
5. Mit dem Einsetzen an einer geraden Seite beginnen, NICHT in der Ecke
6. Profil gleichmäßig eindrücken, Ecken vorsichtig formen
7. Beim Stoß: 2 mm Überstand lassen, sauber auf Gehrung schneiden
8. Stoßstelle mit Dichtungskleber sichern (z. B. Loctite 480)
9. Kleber 24 h aushärten lassen vor Belastung

**Schritt 4: Funktionsprüfung (10–15 min)**
1. Luke/Fenster mehrmals öffnen und schließen
2. Gleichmäßigen Sitz der Dichtung visuell prüfen
3. Lichttest: bei geschlossener Luke von innen mit Taschenlampe leuchten — kein Lichtdurchlass
4. Papierstreifentest: Papier einlegen, schließen, ziehen — gleichmäßiger Widerstand umlaufend

### Schritt-für-Schritt: Verklebte Fensterdichtung erneuern

**Schritt 1: Alten Kleber entfernen (30–60 min)**
1. Mechanisch: Kunststoffspachtel und Klingenentferner
2. Chemisch: Sika Remover-208 oder Sikaflex-Entferner
3. Niemals mit Stahlklingen auf Acrylglas arbeiten
4. Fläche bis auf blankes Substrat reinigen
5. Abschließend mit Sika Aktivator-205 reinigen

**Schritt 2: Primer-Auftrag (15–20 min)**
1. Sika Primer-206 G+P auf GFK/Alu-Rahmen auftragen
2. Sika Primer-210T auf Acryl-/Polycarbonatscheibe
3. Primer dünn und gleichmäßig mit Schwamm aufbringen
4. Ablüftzeit beachten: 30–60 min (nicht >8 h)
5. Primer vor Staub und Feuchtigkeit schützen

**Schritt 3: Dichtmasse auftragen (15–25 min)**
1. Sikaflex-295 UV (für Scheiben) oder Sikaflex-291i (allgemein)
2. Kartusche auf 20–25 °C vorwärmen
3. Dreiecks-Raupe 5–8 mm aufbringen
4. Durchgehend ohne Unterbrechung auftragen
5. Innerhalb der Offenzeit verarbeiten (Sikaflex-295: 30 min bei 23 °C)

**Schritt 4: Scheibe/Dichtung setzen (10–15 min)**
1. Scheibe mit gleichmäßigem Druck aufsetzen
2. Abstandhalter (2–3 mm) einlegen für Mindestklebstoffdicke
3. Überschüssige Dichtmasse mit Spachtel abziehen
4. Abklebeband entfernen, solange Dichtmasse noch feucht
5. 24 h nicht bewegen, 7 Tage bis volle Belastbarkeit

### Dichtigkeitsprüfung nach Einbau

**Methode 1: Wasserstrahltest (empfohlen)**
1. Luke/Fenster von außen mit Gartenschlauch (ohne Drüse) berieseln
2. Wasserdruck ca. 1,5–2,0 bar
3. Von unten nach oben abschnittsweise testen
4. Innen mit Küchenpapier oder Kreide auf Feuchte prüfen
5. Mindestens 5 min pro Seite

**Methode 2: Kreidetest**
1. Dichtfläche dünn mit Kreide einreiben
2. Luke schließen und verriegeln
3. Öffnen und Kreideabdruck prüfen
4. Gleichmäßiger Abdruck umlaufend = dicht
5. Unterbrechungen = undichte Stellen

**Methode 3: Drucktest (professionell)**
1. Raum unter Luke abdichten
2. Überdruck 50–100 Pa erzeugen
3. Mit Seifenlösung Dichtung absprühen
4. Blasenbildung = Leckage
5. Druckabfall messen: <5 Pa/min = gut

**AYDI-Score-Kriterien Dichtigkeitsprüfung:**
- Wasserstrahltest bestanden, kein Tropfen: Score 90–100
- Kreidetest gleichmäßig: Score 85–95
- Leichte Feuchtigkeit, kein Tropfen: Score 60–75
- Tropfenbildung: Score 30–50
- Durchlauf: Score 0–20

---

## Lebensdauer und Alterungsmechanismen

### Materialspezifische Lebensdauer

| Material | Lebensdauer [Jahre] | Bedingungen | Lebensdauer-Killer |
|----------|---------------------|-------------|---------------------|
| EPDM Standard | 5–8 | Gemäßigtes Klima | UV, Ozon, permanente Kompression |
| EPDM Premium (Peroxid-vernetzt) | 8–12 | Gemäßigtes Klima | Mineralöle, Kraftstoffe |
| Silikon (VMQ) | 8–12 | Alle Klimazonen | Mechanischer Abrieb, Reißen |
| Silikon (FVMQ, fluoriert) | 10–15 | Extrembedingungen | Kosten limitieren Einsatz |
| Neopren (CR) | 3–5 | Salzwasser | UV-Strahlung, Ozon, Hitze >80 °C |
| Neopren Premium | 5–7 | Mit UV-Schutz | Permanente Sonneneinstrahlung |
| PVC flexibel | 3–5 | Kostengünstig | Weichmacher-Migration, Kälte <-10 °C |
| Butylkautschuk (IIR) | 8–12 | Gasdicht erforderlich | Mineralöle |
| NBR (Nitrilkautschuk) | 5–8 | Kraftstoffkontakt | UV, Ozon |
| Polyurethan (PU) | 5–8 | Mechanisch belastet | Hydrolyse, UV |

### Alterungsmechanismen im Detail

**1. UV-Degradation**
- Betrifft: Alle Elastomere, besonders Neopren und NBR
- Mechanismus: UV-Photonen brechen C-C und C-H Bindungen
- Symptome: Oberflächenrisse (Checking), Verfärbung, Verhärtung
- Rate: 1–3 Shore-A-Punkte Härtezunahme pro Jahr bei Vollex position (Mittelmeer)
- Gegenmaßnahme: UV-Stabilisatoren, Abdeckung, Silikonmaterial wählen

**2. Ozon-Rissbildung**
- Betrifft: NR, SBR, NBR, CR (Neopren) — EPDM und Silikon sind resistent
- Mechanismus: Ozon greift Doppelbindungen im Polymer an
- Symptome: Feine Querrisse senkrecht zur Dehnungsrichtung
- Rate: Abhängig von Ozonkonzentration (Küste 40–80 ppb) und Dehnung
- Gegenmaßnahme: EPDM oder Silikon verwenden, Anti-Ozonant-Wachse

**3. Compression Set (Druckverformungsrest)**
- Betrifft: Alle Elastomere, besonders bei erhöhter Temperatur
- Mechanismus: Molekulare Relaxation unter permanenter Last
- Symptome: Dichtung kehrt nach Öffnen nicht zur vollen Höhe zurück
- Rate: EPDM 15–25 % nach 1000 h bei 23 °C; Silikon 10–15 %
- Messung: CS = (h₀ - h₁) / (h₀ - h_spacer) × 100 %
- Grenzwert: CS >40 % → Dichtung austauschen
- AYDI-Score: CS 0–20 % → Score 85–100; CS 20–40 % → Score 50–85; CS >40 % → Score 0–50

**4. Weichmacher-Migration (PVC)**
- Betrifft: Nur PVC-Dichtungen
- Mechanismus: Phthalat-Weichmacher diffundieren an die Oberfläche
- Symptome: Klebrige Oberfläche, dann Verhärtung und Versprödung
- Rate: Stark temperaturabhängig, beschleunigt ab 40 °C
- Gegenmaßnahme: Kein PVC für marine Anwendungen über 10 Jahre

**5. Hydrolyse**
- Betrifft: Polyester-Polyurethan, einige Silikontypen
- Mechanismus: Wasseraufnahme spaltet Esterbindungen
- Symptome: Oberfläche wird klebrig, Festigkeitsverlust
- Rate: Verdoppelung pro 10 °C Temperaturerhöhung (Arrhenius)
- Gegenmaßnahme: Polyether-PU statt Polyester-PU verwenden

**6. Salzwasser-Korrosion der Dichtfläche**
- Betrifft: Alu-Rahmen, Edelstahl-Beschläge
- Mechanismus: Salzkristalle in der Dichtfuge → galvanische Korrosion
- Symptome: Weißer Aluminiumoxid-Belag, Lochfraß in der Nut
- Rate: Alu 6082 ohne Eloxat: 0,05–0,1 mm/Jahr; Edelstahl 316L: vernachlässigbar
- Gegenmaßnahme: Eloxierte Oberflächen, regelmäßige Süßwasserspülung

### Klimazonenabhängige Lebensdauer

| Klimazone | Faktor | Beispielregion | EPDM-Lebensdauer |
|-----------|--------|----------------|-------------------|
| Nordeuropa gemäßigt | 1,0 (Referenz) | Ostsee, Nordsee | 6–8 Jahre |
| Mittelmeer | 0,7 | Adria, Ägäis | 4–6 Jahre |
| Tropen | 0,5 | Karibik, Südostasien | 3–4 Jahre |
| Arktisch/Subarktisch | 0,8 | Norwegen, Island | 5–7 Jahre |
| Wüstenklima (Trockenhafen) | 0,6 | Persischer Golf | 3–5 Jahre |

### Wartungsintervalle

| Maßnahme | Intervall | Dauer | Kosten |
|----------|-----------|-------|--------|
| Sichtkontrolle Dichtungen | 3 Monate | 15 min | 0 EUR |
| Reinigung mit Glycerin | 6 Monate | 30 min | 5 EUR |
| Shore-Härte messen | 12 Monate | 20 min | 0 EUR (Durometer vorh.) |
| Compression-Set prüfen | 12 Monate | 30 min | 0 EUR |
| Glycerin-/Silikonpflege | 6 Monate | 30 min | 8 EUR |
| Dichtigkeitstest | 12 Monate | 45 min | 0 EUR |
| Kompletttausch Luken-Dichtung | 5–8 Jahre (EPDM) | 2 h pro Luke | 35–65 EUR/Luke |
| Kompletttausch Fenster-Dichtung | 8–12 Jahre (Silikon) | 3 h pro Fenster | 50–120 EUR/Fenster |

---

## Fehlerbild-Atlas

### Fehlerbild FB-01: Compression Set (Druckverformungsrest)

- **Beschreibung:** Dichtung bleibt nach Öffnen dauerhaft verformt, kehrt nicht in Ausgangsform zurück
- **Visuelle Merkmale:** Flachgedrücktes Profil, sichtbare Abplattung, Spalt zwischen Dichtung und Gegenfläche
- **Typische Ursache:** Permanente Kompression über Jahre, zu hohe Temperatur, falsches Material
- **Betroffene Materialien:** Alle, besonders PVC und Neopren; EPDM und Silikon am widerstandsfähigsten
- **Häufigkeit:** Sehr häufig (35 % aller Dichtungsschäden)
- **Risikobewertung:** Mittel — Undichtigkeit bei Regen/Seegang
- **AYDI-Score-Auswirkung:** Score-Abzug 20–50 Punkte je nach Compression-Set-Grad
- **Typische Bootsgröße:** Alle Klassen, häufiger bei Produktionsbooten mit PVC-Dichtungen
- **Erkennungsmethode Pipeline B:** Profilhöhen-Vergleich im Foto, Spaltanalyse bei geschlossener Luke
- **Confidence-Level Pipeline B:** visual_medium (Profilhöhe schwer exakt messbar im Foto)
- **Sofortmaßnahme:** Dichtung temporär mit PTFE-Streifen unterfüttern
- **Nachhaltige Lösung:** Dichtung komplett ersetzen, ggf. Material-Upgrade auf Silikon
- **Vermeidung:** Luken bei Nichtbenutzung leicht öffnen, Silikonpflege

### Fehlerbild FB-02: UV-Rissbildung (Checking/Crazing)

- **Beschreibung:** Netzartige Oberflächenrisse durch UV-Degradation des Polymers
- **Visuelle Merkmale:** Feine, netzförmige Risse auf der exponierten Oberfläche, oft mit Verfärbung
- **Typische Ursache:** Langzeitige UV-Exposition ohne Schutz, besonders bei schwarzen Dichtungen
- **Betroffene Materialien:** Neopren, NBR, Naturkautschuk; Silikon und EPDM deutlich resistenter
- **Häufigkeit:** Häufig (25 % aller Dichtungsschäden im Mittelmeerraum)
- **Risikobewertung:** Mittel bis Hoch — Risse werden tiefer, Dichtung wird spröde
- **AYDI-Score-Auswirkung:** Score-Abzug 15–40 Punkte
- **Typische Bootsgröße:** Alle Klassen, besonders Decksluken und Cockpitfenster
- **Erkennungsmethode Pipeline B:** Sehr gut erkennbar bei Nahaufnahme, Rissmuster charakteristisch
- **Confidence-Level Pipeline B:** visual_high (eindeutiges Schadensbild)
- **Sofortmaßnahme:** Dichtungspflege mit UV-Schutzmittel, Abdeckung der Luken
- **Nachhaltige Lösung:** Austausch gegen UV-resistentes Material (Silikon, EPDM mit UV-Stabilisator)
- **Vermeidung:** Lukenabdeckungen bei Nichtbenutzung, Silikonmaterial wählen

### Fehlerbild FB-03: Klebstoffversagen (Adhesive Failure)

- **Beschreibung:** Dichtung löst sich vom Rahmen oder der Nut, Kleber versagt
- **Visuelle Merkmale:** Dichtung steht ab, Spalt zwischen Dichtungsfuß und Rahmen, Klebereste sichtbar
- **Typische Ursache:** Falscher Kleber, fehlender Primer, Fett/Öl auf Klebefläche, Alterung
- **Betroffene Materialien:** Alle geklebten Dichtungen, häufig bei Silikondichtung auf Alu
- **Häufigkeit:** Mittel (15 % aller Dichtungsschäden)
- **Risikobewertung:** Hoch — kompletter Dichtigkeitsverlust möglich
- **AYDI-Score-Auswirkung:** Score-Abzug 30–60 Punkte
- **Typische Bootsgröße:** Alle, besonders bei nachträglichen Reparaturen
- **Erkennungsmethode Pipeline B:** Gut erkennbar: abstehende Dichtung, Spaltbildung
- **Confidence-Level Pipeline B:** visual_high
- **Sofortmaßnahme:** Dichtung mit Sekundenkleber (Loctite 480) temporär fixieren
- **Nachhaltige Lösung:** Fachgerechte Neuverklebung mit Primer und geeignetem Kleber
- **Vermeidung:** Korrekte Klebevorbereitung, Primer verwenden, Verarbeitungstemperatur beachten

### Fehlerbild FB-04: Falsches Profil eingebaut

- **Beschreibung:** Dichtungsprofil passt nicht zur Nut — zu groß, zu klein oder falscher Querschnitt
- **Visuelle Merkmale:** Dichtung quillt aus der Nut, sitzt zu locker, oder wird beim Schließen gequetscht
- **Typische Ursache:** Falsche Ersatzteil-Bestellung, Verwechslung, universelle Dichtung statt Original
- **Betroffene Materialien:** Alle Profiltypen
- **Häufigkeit:** Mittel (12 % aller Dichtungsprobleme)
- **Risikobewertung:** Hoch — ungleichmäßige Kompression, lokale Undichtigkeit
- **AYDI-Score-Auswirkung:** Score-Abzug 25–55 Punkte
- **Typische Bootsgröße:** Besonders bei älteren Booten, wo Originalprofile nicht mehr lieferbar
- **Erkennungsmethode Pipeline B:** Gut erkennbar: ungleichmäßiger Sitz, Quetschfalten oder Lücken
- **Confidence-Level Pipeline B:** visual_high
- **Sofortmaßnahme:** Temporär mit zusätzlichem Dichtband kompensieren
- **Nachhaltige Lösung:** Korrektes Profil beschaffen (Hersteller kontaktieren, Muster senden)
- **Vermeidung:** Nutmaße vor Bestellung exakt messen, Probemuster anfordern

### Fehlerbild FB-05: Verhärtete Dichtung

- **Beschreibung:** Dichtung hat Elastizität verloren, ist steif und hart geworden
- **Visuelle Merkmale:** Dichtung lässt sich nicht mehr eindrücken, Oberfläche glänzt, Bruchgefahr beim Biegen
- **Typische Ursache:** Alterung, UV, Ozon, Hitze, Weichmacher-Verlust (PVC)
- **Betroffene Materialien:** PVC, Neopren, ältere EPDM-Mischungen
- **Häufigkeit:** Häufig (20 % aller Dichtungsschäden)
- **Risikobewertung:** Hoch — verhärtete Dichtung kann nicht mehr abdichten
- **AYDI-Score-Auswirkung:** Score-Abzug 30–60 Punkte; Shore >80A → Score ≤30
- **Typische Bootsgröße:** Boote >10 Jahre, besonders Produktionsboote mit PVC-Dichtungen
- **Erkennungsmethode Pipeline B:** Bedingt erkennbar: Glanz, starrer Verlauf, keine Anpassung an Gegenfläche
- **Confidence-Level Pipeline B:** visual_medium
- **Sofortmaßnahme:** Glycerinbehandlung kann temporär Flexibilität verbessern
- **Nachhaltige Lösung:** Kompletttausch, Material-Upgrade
- **Vermeidung:** Regelmäßige Silikonpflege, Shore-Härte jährlich messen

### Fehlerbild FB-06: Gerissene/eingerissene Dichtung

- **Beschreibung:** Dichtung weist Risse oder Einrisse auf, die durch das gesamte Profil gehen
- **Visuelle Merkmale:** Durchgehende Risse, Dichtung in Segmente zerbrochen, Materialverlust
- **Typische Ursache:** Mechanische Überbelastung, Materialermüdung, Frost, Scharnier-Quetschung
- **Betroffene Materialien:** Alle, besonders verhärtete oder spröde Dichtungen
- **Häufigkeit:** Mittel (10 % aller Dichtungsschäden)
- **Risikobewertung:** Kritisch — direkter Wassereintritt
- **AYDI-Score-Auswirkung:** Score-Abzug 50–80 Punkte
- **Typische Bootsgröße:** Alle, häufiger bei Luken mit Federmechanismus
- **Erkennungsmethode Pipeline B:** Sehr gut erkennbar: offensichtliche Risse, Materialverlust
- **Confidence-Level Pipeline B:** visual_high
- **Sofortmaßnahme:** Selbstvulkanisierendes Band, UV-Silikon als Notreparatur
- **Nachhaltige Lösung:** Sofortiger Kompletttausch
- **Vermeidung:** Regelmäßige Inspektion, Scharniere schmieren, Überdehnung vermeiden

### Fehlerbild FB-07: Schimmel und Pilzbefall

- **Beschreibung:** Biologischer Befall der Dichtungsoberfläche mit Schimmel oder Schwarzpilz
- **Visuelle Merkmale:** Schwarze/grünliche Flecken, muffiger Geruch, besonders in Ecken und Falten
- **Typische Ursache:** Dauerfeuchte, mangelnde Belüftung, organische Ablagerungen auf der Dichtung
- **Betroffene Materialien:** Alle, besonders poröse Oberflächen und PVC
- **Häufigkeit:** Häufig in feuchtwarmen Regionen (20 % Tropen/Mittelmeer)
- **Risikobewertung:** Niedrig (technisch), Mittel (gesundheitlich)
- **AYDI-Score-Auswirkung:** Score-Abzug 10–25 Punkte
- **Typische Bootsgröße:** Alle, besonders schlecht belüftete Innenräume
- **Erkennungsmethode Pipeline B:** Gut erkennbar: schwarze Verfärbungen an Dichtungen
- **Confidence-Level Pipeline B:** visual_high (aber Verwechslung mit Schmutz möglich)
- **Sofortmaßnahme:** Reinigung mit verdünntem Essig oder H₂O₂ 3 %, dann trocknen
- **Nachhaltige Lösung:** Belüftung verbessern, antimikrobielle Dichtungen verwenden
- **Vermeidung:** Regelmäßige Reinigung, Entfeuchtung, Belüftung sicherstellen

### Fehlerbild FB-08: Lackkontamination

- **Beschreibung:** Farbe oder Lack auf der Dichtungsoberfläche, die die Elastizität zerstört
- **Visuelle Merkmale:** Farbspritzer oder Farbfilm auf der Dichtung, steife Bereiche
- **Typische Ursache:** Überlackierung bei Wartungsarbeiten ohne Abdeckung der Dichtungen
- **Betroffene Materialien:** Alle — Lösungsmittel im Lack greifen Elastomere an
- **Häufigkeit:** Mittel (8 % aller Dichtungsprobleme)
- **Risikobewertung:** Mittel — lokal steife Bereiche, ungleichmäßige Kompression
- **AYDI-Score-Auswirkung:** Score-Abzug 10–30 Punkte
- **Typische Bootsgröße:** Alle, häufig bei Eigenreparaturen
- **Erkennungsmethode Pipeline B:** Gut erkennbar: Farbspuren auf Dichtung
- **Confidence-Level Pipeline B:** visual_high
- **Sofortmaßnahme:** Frische Farbe sofort mit geeignetem Lösungsmittel entfernen
- **Nachhaltige Lösung:** Bei durchgehärteter Farbe — Dichtung austauschen
- **Vermeidung:** Dichtungen vor Lackierarbeiten sorgfältig abkleben

### Fehlerbild FB-09: Ungleichmäßige Kompression / Spaltbildung

- **Beschreibung:** Dichtung wird an einigen Stellen stärker komprimiert als an anderen
- **Visuelle Merkmale:** Sichtbarer Spalt an einer Seite, überkomprimiertes Profil an anderer Seite
- **Typische Ursache:** Verzogener Rahmen, ungleiche Scharniere, Rumpfverformung, Setzung
- **Betroffene Materialien:** Alle Profiltypen gleichermaßen betroffen
- **Häufigkeit:** Häufig (18 % aller Dichtungsprobleme)
- **Risikobewertung:** Hoch — lokale Undichtigkeit garantiert
- **AYDI-Score-Auswirkung:** Score-Abzug 25–50 Punkte
- **Typische Bootsgröße:** Besonders bei >12 m Segelbooten (Riggspannung) und älteren Booten
- **Erkennungsmethode Pipeline B:** Gut erkennbar: asymmetrischer Spalt, ungleicher Kreideabdruck
- **Confidence-Level Pipeline B:** visual_medium (Spaltbreite schwer quantifizierbar im Foto)
- **Sofortmaßnahme:** Verriegelungsmechanismus justieren, Scharniere prüfen
- **Nachhaltige Lösung:** Rahmen richten oder Dichtung mit Ausgleichsprofil anpassen
- **Vermeidung:** Jährliche Rahmenkontrolle, Scharnierwartung

### Fehlerbild FB-10: Falsche Shore-Härte

- **Beschreibung:** Dichtung hat für die Anwendung ungeeignete Härte (zu weich oder zu hart)
- **Visuelle Merkmale:** Zu weich: Dichtung verformt sich übermäßig, quillt seitlich; zu hart: kein Abdruck auf Gegenfläche
- **Typische Ursache:** Falsche Materialauswahl, günstiges Ersatzmaterial ohne Spezifikation
- **Betroffene Materialien:** Alle Materialtypen in verschiedenen Shore-Härtegraden
- **Häufigkeit:** Mittel (8 % aller Dichtungsprobleme)
- **Risikobewertung:** Mittel — suboptimale Dichtung, aber meist funktional
- **AYDI-Score-Auswirkung:** Score-Abzug 15–35 Punkte
- **Typische Bootsgröße:** Alle, besonders bei Selbsteinbau
- **Erkennungsmethode Pipeline B:** Schwer erkennbar — nur indirekte Hinweise (Verformungsgrad)
- **Confidence-Level Pipeline B:** visual_low
- **Sofortmaßnahme:** Funktionsfähigkeit mit Wassertest prüfen
- **Nachhaltige Lösung:** Dichtung mit korrekt spezifizierter Shore-Härte ersetzen
- **Vermeidung:** Shore-Härte bei Bestellung spezifizieren, Durometer-Test bei Eingang

### Fehlerbild FB-11: Thermische Schrumpfung

- **Beschreibung:** Dichtung schrumpft bei Kälte und zieht sich aus den Ecken zurück
- **Visuelle Merkmale:** Lücken in den Ecken, Dichtung unter Spannung, Stoßfuge öffnet sich
- **Typische Ursache:** Hoher thermischer Ausdehnungskoeffizient, Dichtung auf Zug eingebaut
- **Betroffene Materialien:** PVC, Neopren, einige EPDM-Typen; Silikon am stabilsten
- **Häufigkeit:** Saisonal, besonders Winterlager (10 % in Nordeuropa)
- **Risikobewertung:** Mittel — saisonal undicht, reversibel bei Erwärmung
- **AYDI-Score-Auswirkung:** Score-Abzug 15–30 Punkte (saisonal korrigierbar)
- **Typische Bootsgröße:** Alle, besonders Boote in Nordeuropa mit Winterlager
- **Erkennungsmethode Pipeline B:** Gut erkennbar bei Kälte: Ecklücken, gespanntes Profil
- **Confidence-Level Pipeline B:** visual_medium (temperaturabhängig, Foto-Zeitpunkt relevant)
- **Sofortmaßnahme:** Stoßstelle mit Dichtmasse verschließen
- **Nachhaltige Lösung:** Einbau mit 2–3 mm Längenreserve, Silikon wählen
- **Vermeidung:** Bei Einbau thermische Ausdehnung berücksichtigen (0,5 mm/m/10 °C für EPDM)

### Fehlerbild FB-12: Chemischer Angriff

- **Beschreibung:** Dichtung wird durch chemische Einwirkung angegriffen und zersetzt
- **Visuelle Merkmale:** Aufquellung, klebrige Oberfläche, Auflösung, Verfärbung, Erweichung
- **Typische Ursache:** Kontakt mit Kraftstoffen, Lösungsmitteln, aggressiven Reinigern, Antifouling
- **Betroffene Materialien:** Materialabhängig — jedes Elastomer hat spezifische Unverträglichkeiten
- **Häufigkeit:** Selten (5 % aller Dichtungsschäden)
- **Risikobewertung:** Hoch — schnelle Zerstörung möglich
- **AYDI-Score-Auswirkung:** Score-Abzug 30–70 Punkte
- **Typische Bootsgröße:** Alle, besonders Maschinenraumluken und Tankzugänge
- **Erkennungsmethode Pipeline B:** Gut erkennbar bei fortgeschrittenem Stadium: Quellung, Verfärbung
- **Confidence-Level Pipeline B:** visual_medium (Frühstadium schwer erkennbar)
- **Sofortmaßnahme:** Chemikalie entfernen, Dichtung reinigen, Funktionstest
- **Nachhaltige Lösung:** Chemisch beständiges Material wählen (FKM/Viton für Kraftstoffe, EPDM für Säuren)
- **Vermeidung:** Chemische Verträglichkeit vor Einbau prüfen, Materialdatenblatt beachten

---

## Fehlerbehebungs-Leitfaden

### Problem 1: Luke tropft trotz neuer Dichtung

**Symptom:** Nach Dichtungstausch ist die Luke weiterhin undicht.

**Diagnoseschritte:**
1. Kreidetest durchführen → Abdruck prüfen
2. Rahmen auf Verzug prüfen (Haarlineal, Fühlerlehre)
3. Schließmechanismus und Kompression prüfen
4. Entwässerungsbohrungen kontrollieren (verstopft?)
5. Dichtungsprofil-Maße mit Nut vergleichen

**Häufigste Ursachen und Lösungen:**
| Ursache | Häufigkeit | Lösung | Kosten |
|---------|-----------|--------|--------|
| Rahmen verzogen | 35 % | Rahmen richten, Unterfütterung | 50–200 EUR |
| Falsches Profil | 25 % | Korrektes Profil einsetzen | 30–60 EUR |
| Schließmechanismus defekt | 20 % | Scharniere/Riegel einstellen oder ersetzen | 30–150 EUR |
| Drainage verstopft | 15 % | Bohrungen freimachen | 0 EUR |
| Montagefehler | 5 % | Dichtung korrekt neu einsetzen | 0–20 EUR |

### Problem 2: Dichtung löst sich immer wieder

**Symptom:** Geklebte Dichtung löst sich nach kurzer Zeit erneut.

**Diagnoseschritte:**
1. Kleberreste auf Kohäsions- vs. Adhäsionsbruch prüfen
2. Substrat-Oberfläche auf Verunreinigung testen
3. Klebertyp-Kompatibilität mit Dichtung und Substrat prüfen
4. Verarbeitungstemperatur bei Verklebung erfragen

**Lösungen:**
| Ursache | Lösung | Kosten |
|---------|--------|--------|
| Kein Primer verwendet | Oberfläche reinigen, primern, neu kleben | 15–30 EUR |
| Falscher Kleber | Herstellerempfehlung befolgen (z. B. Sika, 3M) | 20–40 EUR |
| Fettfilm auf Substrat | Gründliche Reinigung mit Aceton/IPA | 5 EUR |
| Zu kalt bei Verarbeitung | Min. 10 °C Verarbeitungstemperatur sicherstellen | 0 EUR |

### Problem 3: Kondenswasser trotz dichter Luke

**Symptom:** Tropfenbildung an der Innenseite der Luke, obwohl Dichtung intakt.

**Diagnoseschritte:**
1. Tropfenbildung bei geschlossener Luke beobachten
2. Temperaturunterschied innen/außen messen
3. Luftfeuchtigkeit innen messen (Hygrometer)
4. Prüfen ob Wasser von der Dichtung oder der Scheibe/dem Rahmen kommt

**Lösungen:**
| Ursache | Lösung | Kosten |
|---------|--------|--------|
| Kondensation (kein Defekt) | Belüftung verbessern, Entfeuchter | 30–150 EUR |
| Thermische Brücke im Rahmen | Thermisch getrennte Luke nachrüsten | 300–1.500 EUR |
| Undichter Rahmen-Deck-Anschluss | Rahmen abdichten (Sikaflex) | 30–80 EUR |

### Problem 4: Dichtung quietscht oder klemmt

**Symptom:** Luke lässt sich schwer öffnen/schließen, Quietschgeräusche.

**Diagnoseschritte:**
1. Dichtungsoberfläche auf Verhärtung/Klebrigkeit prüfen
2. Gegenfläche auf Rauheit/Korrosion prüfen
3. Kompressionsgrad messen
4. Scharniere auf Gängigkeit testen

**Lösungen:**
| Ursache | Lösung | Kosten |
|---------|--------|--------|
| Trockene Dichtung | Silikonpflege auftragen | 8 EUR |
| Überkompression | Dichtung mit geringerer Höhe einsetzen | 30–60 EUR |
| Korrodierte Gegenfläche | Oberfläche glätten, Korrosion entfernen | 20–50 EUR |
| Scharniere schwergängig | Scharniere schmieren oder ersetzen | 10–80 EUR |

### Problem 5: Dichtung riecht unangenehm / chemischer Geruch

**Symptom:** Strenger Geruch aus dem Bereich der Dichtung, besonders bei Wärme.

**Diagnoseschritte:**
1. Dichtungsmaterial identifizieren
2. Kontakt mit Chemikalien ausschließen
3. Schimmelbefall prüfen (unter der Dichtung)
4. Billigdichtung (Recycling-Gummi) ausschließen

**Lösungen:**
| Ursache | Lösung | Kosten |
|---------|--------|--------|
| Billigdichtung mit Recycling-Gummi | Gegen Markendichtung tauschen | 30–80 EUR |
| Schimmel unter Dichtung | Dichtung entfernen, Fläche desinfizieren | 15–30 EUR |
| Chemischer Angriff | Dichtung sofort ersetzen, Ursache abstellen | 30–80 EUR |
| Ausgasung neuer Dichtung | Normal, verflüchtigt nach 2–4 Wochen | 0 EUR |

---

## FAQ

**FD-001: Wie oft sollte man Luken-Dichtungen austauschen?**
EPDM alle 5–8 Jahre, Silikon alle 8–12 Jahre, Neopren alle 3–5 Jahre. Im Mittelmeer ca. 30 % kürzer. Jährliche Sichtprüfung empfohlen, Austausch bei Shore-Härte >70A oder Compression-Set >40 %.

**FD-002: Kann man Dichtungen von verschiedenen Herstellern mischen?**
Grundsätzlich ja, solange Profilmaße und Material übereinstimmen. Nicht empfohlen: verschiedene Materialien in einer Nut (unterschiedlicher Compression-Set). AYDI-Score-Abzug 10 Punkte bei Mischbestückung.

**FD-003: Welches Material ist für Mittelmeer-Yachten am besten?**
Silikon (VMQ) bietet die beste UV-Beständigkeit und Temperaturstabilität. Alternativ EPDM mit UV-Stabilisator. Neopren und PVC sind ungeeignet für dauerhafte Sonneneinstrahlung.

**FD-004: Wie messe ich die Shore-Härte meiner Dichtung?**
Mit einem Shore-A-Durometer direkt auf die Dichtung drücken. Neue Dichtung: 40–60 Shore A. Grenzwert: 70 Shore A. Über 80 Shore A: sofort austauschen. Durometer ab 25 EUR im Handel.

**FD-005: Kann ich Sikaflex als Dichtungsersatz verwenden?**
Nein. Sikaflex ist ein Kleb-Dichtstoff, keine elastische Dichtung. Es fehlt die nötige Rückstellkraft. Nur als Notlösung akzeptabel (max. 1 Saison). AYDI-Score: 20–35 Punkte.

**FD-006: Was ist der Unterschied zwischen EPDM und Silikon?**
EPDM: günstiger (3–8 EUR/m), gute Witterungsbeständigkeit, Shore 40–70A. Silikon: teurer (8–20 EUR/m), beste UV/Ozon-Beständigkeit, Shore 30–70A, Temperaturbereich -60 bis +200 °C vs. EPDM -40 bis +120 °C.

**FD-007: Meine Lewmar-Luke ist undicht. Welche Dichtung brauche ich?**
Lewmar Mk2: Profil Nr. 19911420 (EPDM Hohlprofil 12×8 mm). Lewmar Ocean: Profil Nr. 19911430 (EPDM 14×10 mm). Originalprofile bei Lewmar-Händlern oder SVB, Compass24. Universalprofile passen selten exakt.

> ⚠️ **ZU PRÜFEN (Audit):** Teilenummern-Widerspruch innerhalb dieser Datei — der Haupttext (Abschnitte 8.1 und 9.1.2) führt Lewmar Ocean als 19901010–19901070 und Mk2 als 19905xxx/19906xxx, während die Anhänge A/H, diese FAQ und Fallstudie FS-01 die Nummern 19911430 (Ocean) bzw. 19911420 (Mk2) nennen. Beide Angaben sind als „documented" gekennzeichnet, nur eine kann korrekt sein. Vor einer Bestellung die Teilenummer direkt bei Lewmar oder einem autorisierten Händler anhand der konkreten Lukenserie/Baujahr verifizieren.

**FD-008: Kann ich eine Dichtung selbst vulkanisieren/kleben?**
Stoßstellen können mit Sekundenkleber (Cyanacrylat) oder speziellem Dichtungskleber (z. B. Loctite 480) verbunden werden. Für Endlosdichtungen ohne Stoß: Vulkanisationskleber und Heißluftfön (180 °C, 3 min). Professionelle Vulkanisation bevorzugen.

**FD-009: Wie reinige ich Dichtungen richtig?**
Lauwarmes Wasser mit mildem Spülmittel und weichem Tuch. Niemals: Aceton, Benzin, Terpentin, aggressive Reiniger. Danach Glycerin oder Silikonpflege auftragen. Hartnäckige Salzreste: Essigwasser 1:10.

**FD-010: Was tun bei einer undichten Luke auf See (Notfall)?**
1. Provisorische Abdichtung mit selbstvulkanisierendem Tape (Rescue Tape). 2. Frischhaltefolie + Klebeband als Sofortmaßnahme. 3. Handtücher und Eimer positionieren. 4. Bei schwerem Wetter: Luken von innen mit Kissen und Spanngurten sichern.

**FD-011: Sind Universaldichtungen eine gute Alternative?**
Nur bedingt. Universalprofile (z. B. D-Profil selbstklebend) funktionieren bei einfachen Geometrien. Bei Luken mit spezifischer Nut: Originalprofile bevorzugen. AYDI-Score-Abzug 15–25 Punkte bei Universalprofil.

**FD-012: Wie lagere ich Ersatz-Dichtungen richtig?**
Dunkel, trocken, bei 15–25 °C, nicht geknickt oder gefaltet. In PE-Beutel mit Talkumpuder. Nicht in der Nähe von Ozonquellen (Elektromotoren). Haltbarkeit: EPDM 5 Jahre, Silikon 10 Jahre bei korrekter Lagerung.

**FD-013: Kann Frostschaden an Dichtungen auftreten?**
Ja. Wasseransammlung in Hohlprofildichtungen kann bei Frost gefrieren und die Dichtung sprengen. Prävention: Vor dem Winterlager Dichtungen trocknen, Luken leicht geöffnet lassen.

**FD-014: Welchen Kleber verwende ich für EPDM auf Aluminium?**
Sika Primer-206 G+P auf Alu, dann Sikaflex-291i oder 3M DP-8005. Alternativ: Loctite 480 für kleine Flächen. Verarbeitungstemperatur >10 °C. Aushärtung: 24 h bis handfest, 7 d bis voll belastbar.

**FD-015: Was kostet ein professioneller Dichtungstausch?**
Werft-Stundensatz: 65–120 EUR/h. Eine Luke: 1,5–2,5 h Arbeit + Material (30–65 EUR) = 130–365 EUR. Ein Fenster: 2–4 h + Material (50–120 EUR) = 180–600 EUR. Selbsteinbau spart 60–70 % der Kosten.

**FD-016: Wie erkenne ich, ob meine Dichtung EPDM oder Neopren ist?**
Geruchstest: Neopren riecht leicht chemisch-süßlich, EPDM nahezu geruchlos. Flammtest (Vorsicht!): EPDM brennt mit rußender Flamme, Neopren ist selbstverlöschend. Farbe: Neopren meist schwarz, EPDM schwarz oder grau.

**FD-017: Kann ich eine Dichtung dehnen, wenn sie etwas zu kurz ist?**
Maximal 3–5 % Dehnung bei EPDM/Silikon. Bei größerer Dehnung: erhöhter Compression-Set, Rückzug bei Kälte. Besser: Neuzuschnitt mit korrekter Länge + 5–10 mm Zugabe.

**FD-018: Wie dichtet man einen Niedergangs-Schieber ab?**
Bürstendichtung oder Lippenprofil (EPDM 15×3 mm) im Führungskanal. Unterkante: Flachdichtung oder D-Profil. Oberkante: Überlappung mit Tropfkante. Regelmäßig Silikonspray auf die Führungsschienen.

**FD-019: Was ist besser: Klemmprofil oder geklebte Dichtung?**
Klemmprofil: einfacher Austausch, standardisierte Maße, keine Aushärtezeit. Geklebt: flexiblere Geometrien, kein Nutfräsen nötig. Für Luken: Klemmprofil bevorzugt. Für Fenster: Verklebung oft unvermeidlich.

**FD-020: Meine Acrylglas-Luke hat Haarrisse. Liegt das an der Dichtung?**
Indirekt möglich: Überkomprimierte Dichtung erzeugt Punktlasten auf dem Acrylglas. Zu harte Dichtung (>65 Shore A) kann Crazing verursachen. Lösung: Weichere Dichtung (40–50 Shore A), gleichmäßige Kompression sicherstellen.

**FD-021: Wie verhindere ich Schimmel auf Dichtungen?**
Regelmäßige Reinigung mit Essigwasser (1:10). Belüftung sicherstellen (Dorade-Lüfter, Solarventilator). Antimikrobielle Dichtungen (mit Silber-Ionen) verfügbar ab ca. 12 EUR/m. Dichtungen nach Regenfällen abwischen und trocknen.

**FD-022: Gibt es selbstklebende Dichtungsbänder als Ersatz?**
Ja, z. B. EPDM- oder Silikon-Selbstklebebänder (D-, P-, E-Profil). Für temporäre Lösungen und einfache Anwendungen geeignet. Haltbarkeit der Klebeschicht: 1–3 Jahre marine. AYDI-Score: 40–60 Punkte (Dauerlösung: 75–100).

**FD-023: Wie teste ich die Dichtigkeit eines Bullauges?**
1. Äußere Sichtprüfung der Dichtung. 2. Papierstreifentest (Papier einklemmen, ziehen). 3. Wassertest: Eimer Wasser langsam über Bullauge gießen, innen Papierstreifen prüfen. 4. Bei Verdacht: Luke öffnen und Dichtung auf Compression-Set prüfen.

**FD-024: Müssen Dichtungen bei der CE-Zertifizierung dokumentiert werden?**
Ja. ISO 12216 fordert die Angabe des Dichtungstyps, Materials und der Prüfdrücke für Fenster und Luken. Bei CE-Kategorie A und B ist die Dichtigkeitsprüfung nach ISO 12216:2020 Abschnitt 6 vorgeschrieben. AYDI-Modul compliance prüft dies.

**FD-025: Kann ich 3D-gedruckte Dichtungen verwenden?**
TPU/TPE-Dichtungen aus dem 3D-Drucker sind experimentell und für den Marinebereich nicht zertifiziert. Probleme: Schichtlinien undicht, UV-Beständigkeit unbekannt, Compression-Set hoch. Nur als absolute Notlösung, AYDI-Score: 15–25 Punkte.

---

## Glossar

| Begriff | Erklärung |
|---------|-----------|
| Adhesive Failure | Klebstoffversagen an der Grenzfläche Kleber/Substrat |
| Arrhenius-Gleichung | Beschreibt Temperaturabhängigkeit chemischer Alterung |
| Bullauge | Rundes Schiffsfenster, fest oder öffnend |
| Bürstendichtung | Dichtung mit feinen Borsten für Schiebeanwendungen |
| CE-Kategorie | Seegangs-Einsatzklassifizierung (A–D) nach EU-Richtlinie 2013/53 |
| Cohesive Failure | Bruch innerhalb des Klebstoffs (nicht an der Grenzfläche) |
| Compression Set | Bleibende Verformung einer Dichtung nach Dauerbelastung [%] |
| Crazing | Feine Netzrisse in Kunststoffen (Acrylglas) durch Spannung |
| D-Profil | Dichtungsprofil mit D-förmigem Querschnitt |
| Durometer | Messgerät für die Shore-Härte von Elastomeren |
| E-Modul | Elastizitätsmodul; Steifigkeit eines Materials [MPa] |
| E-Profil | Dichtungsprofil mit E-förmigem Querschnitt (drei Lippen) |
| EPDM | Ethylen-Propylen-Dien-Kautschuk; Standard-Dichtungsmaterial |
| Extrusion | Herstellungsverfahren für Dichtungsprofile (Strangpressen) |
| FKM/Viton | Fluorkautschuk; chemisch hochbeständig |
| Flachdichtung | Dichtung mit rechteckigem Querschnitt |
| FVMQ | Fluorsilikon; temperatur- und chemikalienbeständig |
| Galvanische Korrosion | Korrosion durch Kontakt unterschiedlicher Metalle |
| Gelcoat | Äußere Schutzschicht auf GFK-Bauteilen |
| GFK | Glasfaserverstärkter Kunststoff (Fiberglass) |
| Glycerin | Pflegemittel für Gummidichtungen, erhält Elastizität |
| Hohlprofil | Dichtung mit hohlem Innenquerschnitt |
| Hydrolyse | Chemische Zersetzung durch Wassereinwirkung |
| IIR | Butylkautschuk; gasdicht, vibrationsdämpfend |
| ISO 12216 | Norm für Fenster, Bullaugen, Luken und Deckel auf Schiffen |
| Kohäsionsbruch | Bruch innerhalb des Dichtungsmaterials |
| Kompressionsgrad | Verhältnis der Stauchung zur ursprünglichen Höhe [%] |
| Lippendichtung | Dichtung mit flexibler Lippe zur Anpressung |
| Niedergang | Einstieg/Zugang unter Deck |
| Nut | Einfräsung oder Formgebung zur Aufnahme einer Dichtung |
| Neopren (CR) | Chloroprenkautschuk; Dichtungsmaterial, UV-empfindlich |
| NBR | Acrylnitril-Butadien-Kautschuk; öl-/kraftstoffbeständig |
| O-Ring | Ringförmige Dichtung mit kreisrundem Querschnitt |
| Ozon-Rissbildung | Rissbildung durch Ozon-Angriff auf Doppelbindungen |
| P-Profil | Dichtungsprofil mit P-förmigem Querschnitt |
| Primer | Haftvermittler zwischen Substrat und Klebstoff |
| PTFE | Polytetrafluorethylen (Teflon); Gleitmittel, chemisch inert |
| PVC | Polyvinylchlorid; günstiges Dichtungsmaterial, begrenzte Haltbarkeit |
| Rückstellkraft | Kraft, mit der eine Dichtung in ihre Ausgangsform zurückkehrt |
| Rundschnur | Dichtung mit rundem Querschnitt |
| Shore-Härte A | Härteskala für Elastomere (0 = butterweich, 100 = hart) |
| Sikaflex | Markenname für PU-Kleb-Dichtstoffe der Firma Sika |
| Silikon (VMQ) | Silikon-Kautschuk; UV-/temperaturbeständig |
| Stoßstelle | Verbindungsstelle der Dichtungsenden |
| Thermische Ausdehnung | Längenänderung bei Temperaturwechsel [mm/m/°C] |
| TPU/TPE | Thermoplastisches Polyurethan/Elastomer; 3D-druckbar |
| Vulkanisation | Vernetzungsprozess bei Gummiherstellung |
| Weichmacher-Migration | Auswandern von Weichmachern aus PVC über die Zeit |

---

## Schnell-Referenz

### Dichtungsmaterial-Auswahl nach Anwendung

| Anwendung | Empfohlenes Material | Shore A | Profil | Kosten/m |
|-----------|---------------------|---------|--------|----------|
| Decksluke Standard | EPDM | 50–60 | Hohlprofil | 4–8 EUR |
| Decksluke Hochsee | Silikon | 50–60 | Hohlprofil | 10–18 EUR |
| Festfenster | Silikon | 40–50 | Rundschnur | 6–12 EUR |
| Schiebefenster | EPDM | 55–65 | E-Profil | 5–10 EUR |
| Bullauge | EPDM/Silikon | 45–55 | Rundschnur | 4–10 EUR |
| Niedergang Schieber | EPDM | 50–60 | Lippenprofil | 5–10 EUR |
| Maschinenraumluke | EPDM hart | 65–70 | D-Profil | 6–12 EUR |
| Ankerkastenluke | EPDM | 55–65 | Hohlprofil | 4–8 EUR |
| Cockpit-Staukasten | EPDM | 50–60 | Flachdichtung | 3–6 EUR |

### AYDI-Score-Schnellbewertung

| Zustand | Score | Farbe |
|---------|-------|-------|
| Neuwertig, korrekt eingebaut | 90–100 | Grün |
| Leichte Alterung, funktional | 70–89 | Grün |
| Sichtbare Alterung, noch dicht | 50–69 | Gelb |
| Deutliche Mängel, eingeschränkt dicht | 30–49 | Orange |
| Undicht, Austausch erforderlich | 10–29 | Rot |
| Fehlend oder zerstört | 0–9 | Rot |

### Kritische Maße für Luke/Fenster-Dichtungen

| Parameter | Minimum | Optimal | Maximum |
|-----------|---------|---------|---------|
| Kompressionsgrad | 15 % | 25–35 % | 45 % |
| Shore-Härte (Luken) | 40 A | 50–60 A | 70 A |
| Shore-Härte (Fenster) | 35 A | 40–55 A | 65 A |
| Stoßfugen-Spalt | 0 mm | 0 mm (stumpf) | 0,5 mm |
| Klebstoff-Dicke | 1 mm | 2–3 mm | 5 mm |
| Nutfüllung | 70 % | 80–90 % | 95 % |

---

## Notfall-Ressourcen

### Notfall-Kit für Dichtungsreparaturen an Bord

| Artikel | Menge | Kosten | Bezugsquelle |
|---------|-------|--------|--------------|
| Rescue Tape (selbstvulkanisierend) | 2 Rollen | 12 EUR | SVB, Compass24 |
| EPDM-Rundschnur Ø6/Ø8/Ø10 mm, je 2 m | 6 m gesamt | 15 EUR | Dichtungstechnik24 |
| Universaldichtband D-Profil, 5 m | 1 Rolle | 8 EUR | Baumarkt, SVB |
| Loctite 480 Sekundenkleber | 1 Tube 20 g | 12 EUR | Baumarkt, Amazon |
| Sikaflex-291i Kartusche 70 ml | 1 Stück | 14 EUR | SVB, Compass24 |
| Isopropanol 99 % | 250 ml | 5 EUR | Apotheke |
| Talkumpuder | 100 g | 3 EUR | Apotheke |
| Kabelbinder 200 mm | 20 Stück | 3 EUR | Baumarkt |
| Frischhaltefolie | 1 Rolle | 2 EUR | Supermarkt |
| Gesamtkosten Notfall-Kit | – | ~74 EUR | – |

### Notfall-Kontakte Dichtungshersteller

| Hersteller | Telefon | Webshop | Lieferzeit |
|------------|---------|---------|------------|
| Lewmar | +44 145 233 7700 | lewmar.com | 3–7 Werktage |
| Goiot | +33 2 40 34 01 01 | goiot.com | 5–10 Werktage |
| Houdini Marine | +1 800 448 6784 | houdinimarine.com | 7–14 Werktage |
| Vetus | +31 78 618 9100 | vetus.com | 3–5 Werktage |
| Bomar/Pompanette | +1 800 327 6167 | bfrgroup.com | 7–14 Werktage |
| SVB (Universalprofile) | +49 421 577 180 | svb-marine.de | 1–3 Werktage |
| Compass24 (Universalprofile) | +49 421 836 110 | compass24.de | 1–3 Werktage |
| Toplicht (Universalprofile) | +49 40 851 7tried | toplicht.de | 1–3 Werktage |

---

## ANHANG A: Dichtungsprofil-Maßtabelle nach Hersteller

| Hersteller | Modell | Profiltyp | Breite [mm] | Höhe [mm] | Artikelnummer |
|------------|--------|-----------|-------------|-----------|---------------|
| Lewmar | Mk2 Size 10–60 | Hohlprofil | 9,5 | 12,0 | 19911420 |
| Lewmar | Ocean Size 00–70 | Hohlprofil | 11,5 | 14,0 | 19911430 |
| Lewmar | Low Profile | Hohlprofil | 8,5 | 10,0 | 19911415 |
| Goiot | Cristal 31/33/37 | Klemmprofil | 7,5 | 10,0 | 30.270.00 |
| Goiot | Opal 41/43/47 | Klemmprofil | 8,5 | 11,0 | 30.370.00 |
| Goiot | Azur | Klemmprofil | 9,0 | 11,5 | 30.470.00 |
| Bomar | Cast/Extruded N | Hohlprofil | 10,5 | 13,0 | BOM-GP01 |
| Bomar | Low Profile G | Hohlprofil | 9,0 | 11,0 | BOM-GP02 |
| Houdini | Standard | Hohlprofil | 9,5 | 12,5 | HOU-S100 |
| Vetus | Libero | Hohlprofil | 9,0 | 11,5 | VET-LIB-S |
| Moonlight | Standard | Klemmprofil | 7,0 | 9,5 | ML-100 |

## ANHANG B: Chemische Beständigkeit von Dichtungsmaterialien

| Medium | EPDM | Silikon | Neopren | NBR | FKM/Viton |
|--------|------|---------|---------|-----|-----------|
| Salzwasser | ++ | ++ | + | + | ++ |
| Süßwasser | ++ | ++ | ++ | ++ | ++ |
| Diesel | -- | - | + | ++ | ++ |
| Benzin | -- | -- | + | ++ | ++ |
| Hydrauliköl (mineralisch) | -- | - | + | ++ | ++ |
| Hydrauliköl (synthetisch) | + | + | - | + | ++ |
| Aceton | + | + | -- | -- | - |
| Isopropanol | ++ | ++ | + | + | ++ |
| Essig (verdünnt) | ++ | ++ | + | + | ++ |
| Natriumhypochlorit | + | ++ | + | - | ++ |
| UV-Strahlung | + | ++ | -- | -- | + |
| Ozon | ++ | ++ | - | -- | ++ |

Legende: ++ = hervorragend, + = gut, - = eingeschränkt, -- = ungeeignet

## ANHANG C: Temperaturbeständigkeit

| Material | Min. Temp [°C] | Max. Temp [°C] | Optimaler Bereich [°C] |
|----------|----------------|----------------|------------------------|
| EPDM | -45 | +120 | -20 bis +80 |
| Silikon (VMQ) | -60 | +200 | -40 bis +150 |
| Silikon (FVMQ) | -60 | +200 | -50 bis +175 |
| Neopren (CR) | -35 | +100 | -15 bis +70 |
| NBR | -30 | +100 | -10 bis +80 |
| FKM/Viton | -20 | +200 | 0 bis +180 |
| PVC | -10 | +60 | 0 bis +45 |
| Butyl (IIR) | -45 | +120 | -30 bis +100 |
| TPU | -40 | +80 | -20 bis +60 |

## ANHANG D: AYDI-Scoring-Algorithmus für Dichtungen

```python
def calculate_seal_score(seal_data: dict) -> dict:
    """
    Berechnet den AYDI-Score für eine Luken-/Fensterdichtung.
    
    Parameter:
        seal_data: Dict mit Messwerten und Befunden
    
    Returns:
        Dict mit score (0-100), confidence, findings
    """
    score = 100
    findings = []
    
    # Compression Set
    cs = seal_data.get("compression_set_pct", None)
    if cs is not None:
        if cs > 40:
            score -= 50
            findings.append("Compression Set >40 %: Austausch erforderlich")
        elif cs > 25:
            score -= 25
            findings.append("Compression Set erhöht: Überwachung empfohlen")
        elif cs > 15:
            score -= 10
            findings.append("Compression Set leicht erhöht")
    
    # Shore-Härte
    shore = seal_data.get("shore_hardness_a", None)
    if shore is not None:
        if shore > 80:
            score -= 60
            findings.append("Shore >80A: Dichtung verhärtet, Austausch dringend")
        elif shore > 70:
            score -= 35
            findings.append("Shore >70A: Dichtung altert, baldiger Austausch")
        elif shore > 65:
            score -= 15
            findings.append("Shore leicht erhöht")
    
    # Sichtbare Schäden
    damage = seal_data.get("visible_damage", [])
    damage_scores = {
        "riss": -40,
        "uv_cracking": -25,
        "schimmel": -15,
        "verfaerbung": -10,
        "abloesung": -35,
        "quellung": -30,
        "lack_kontamination": -15,
    }
    for d in damage:
        penalty = damage_scores.get(d, -20)
        score += penalty  # penalty ist negativ
        findings.append(f"Sichtbarer Schaden: {d}")
    
    # Kompressionsgrad
    comp = seal_data.get("compression_pct", None)
    if comp is not None:
        if comp < 10:
            score -= 40
            findings.append("Kompression <10 %: ungenügend")
        elif comp > 50:
            score -= 30
            findings.append("Kompression >50 %: Überkompression")
        elif comp < 15 or comp > 45:
            score -= 15
            findings.append("Kompression außerhalb Optimalbereich")
    
    # Materialeignung
    material = seal_data.get("material", "")
    application = seal_data.get("application", "")
    if material == "pvc" and application in ["decksluke", "fenster"]:
        score -= 20
        findings.append("PVC-Dichtung: begrenzte Haltbarkeit, Upgrade empfohlen")
    if material == "neopren" and seal_data.get("uv_exposure", False):
        score -= 15
        findings.append("Neopren bei UV-Exposition: Degradation beschleunigt")
    
    score = max(0, min(100, score))
    
    confidence = "measured" if seal_data.get("level") == 2 else "estimated"
    
    return {
        "score": score,
        "confidence": confidence,
        "findings": findings,
        "available": True
    }
```

## ANHANG E: Werkzeugliste für Dichtungsarbeiten

| Werkzeug | Verwendung | Kosten |
|----------|-----------|--------|
| Shore-A-Durometer | Härtemessung Dichtung | 25–80 EUR |
| Schieblehre 150 mm | Profilmaße messen | 15–40 EUR |
| Fühlerlehre 0,05–1,0 mm | Spaltprüfung | 8–15 EUR |
| Kunststoff-Auszieher Set | Dichtung entfernen | 12–25 EUR |
| Dichtungsschneider (Skalpell) | Zuschnitt auf Gehrung | 5–12 EUR |
| Kartuschenpresse manuell | Sikaflex-Verarbeitung | 10–25 EUR |
| Kartuschenpresse Akku | Gleichmäßiger Auftrag | 80–200 EUR |
| Haarlineal 300 mm | Ebenheit Rahmen prüfen | 20–50 EUR |
| Heißluftfön 300 °C | Vulkanisation, Entfernung | 30–80 EUR |
| UV-Lampe 365 nm | Leckortung (mit Fluoreszenzfarbe) | 15–40 EUR |

## ANHANG F: Lieferantenverzeichnis Europa

| Lieferant | Land | Sortiment | Versand |
|-----------|------|-----------|---------|
| SVB Marine | DE | Universalprofile, OEM-Dichtungen | EU-weit, 1–3 Tage |
| Compass24 | DE | Universalprofile, Kleber, Primer | EU-weit, 1–3 Tage |
| Toplicht | DE | Luken-OEM-Dichtungen, Zubehör | DE/AT/CH, 2–4 Tage |
| Dichtungstechnik24 | DE | Industrieprofile als Meterware | DE/EU, 1–3 Tage |
| Lewmar (direkt) | UK | Originalprofile Lewmar-Luken | EU-weit, 5–10 Tage |
| Goiot (direkt) | FR | Originalprofile Goiot-Luken | EU-weit, 7–14 Tage |
| Vetus (direkt) | NL | Originalprofile Vetus-Luken | EU-weit, 3–5 Tage |
| Seldén | SE | Lukendichtungen, Luken | EU-weit, 5–10 Tage |
| Simpson Marine | IT | Flexible Profile, Sonderanfertigung | EU-weit, 7–14 Tage |
| Force4 Chandlery | UK | Universalprofile, Kleber | UK/EU, 3–7 Tage |

## ANHANG G: Normreferenzen

| Norm | Titel | Relevanz für Dichtungen |
|------|-------|------------------------|
| ISO 12216:2020 | Fenster, Bullaugen, Luken, Deckel | Dichtungsanforderungen, Prüfdrücke |
| ISO 12217-1/2/3 | Stabilitätsbewertung | Gewicht der Luken-/Fenster-Systeme |
| ISO 11812:2020 | Cockpits | Cockpitluken-Dichtung, Entwässerung |
| ISO 15085:2003 | Schutz gegen MOB | Deckslukensicherheit |
| ISO 12215-5 | Rumpfbau, Scantlings | Rahmensteifigkeit für Dichtungssitz |
| EN 681-1 | Elastomer-Dichtungen Wasser | Materialanforderungen |
| DIN 7863 | Elastomer-Dichtprofile Fenster/Fassade | Profilnormung |
| DIN 3771 | O-Ringe | Maße und Toleranzen |

## ANHANG H: Bootshersteller-Dichtungs-Zuordnungsmatrix

| Hersteller | Modellreihe | Lukenhersteller | Dichtungsprofil | Artikel-Nr. |
|------------|-------------|-----------------|-----------------|-------------|
| Bavaria | Cruiser 34–46 | Lewmar Mk2 | Hohlprofil 12×8 | 19911420 |
| Bavaria | Vision 42–46 | Lewmar Ocean | Hohlprofil 14×10 | 19911430 |
| Hanse | 348–588 | Lewmar Mk2 | Hohlprofil 12×8 | 19911420 |
| Hanse | 675 | Lewmar Ocean | Hohlprofil 14×10 | 19911430 |
| Jeanneau | Sun Odyssey | Goiot Cristal/Opal | Klemmprofil 7,5–8,5 | 30.270/370 |
| Bénéteau | Océanis | Goiot Cristal/Opal | Klemmprofil 7,5–8,5 | 30.270/370 |
| Bénéteau | Figaro | Goiot Azur | Klemmprofil 9×11,5 | 30.470.00 |
| Hallberg-Rassy | 31–64 | Eigenfertigung/Lewmar | Hohlprofil 10–14 | HR-spezifisch |
| Najad | 332–440 | Eigenfertigung | Silikon-Hohlprofil | Najad-spezifisch |
| X-Yachts | Xc/Xp-Serie | Lewmar Ocean | Hohlprofil 14×10 | 19911430 |
| Dehler | 30–46 | Lewmar Mk2 | Hohlprofil 12×8 | 19911420 |
| Dufour | Grand Large | Goiot Cristal | Klemmprofil 7,5×10 | 30.270.00 |

## ANHANG I: Saisonale Wartungs-Checkliste

### Frühjahr (Ansaisonierung)
- [ ] Alle Dichtungen visuell inspizieren
- [ ] Shore-Härte messen und dokumentieren
- [ ] Compression-Set an Hauptluken prüfen
- [ ] Glycerinpflege auf alle Gummidichtungen auftragen
- [ ] Dichtigkeitstest mit Wasserschlauch durchführen
- [ ] Scharniere und Verriegelungen schmieren
- [ ] Rahmen auf Korrosion/Verzug prüfen
- [ ] Ergebnisse im AYDI-Logbuch dokumentieren

### Herbst (Absaisonierung)
- [ ] Alle Dichtungen reinigen (Salzreste entfernen)
- [ ] Glycerinpflege auftragen (Winterschutz)
- [ ] Luken 2–3 mm geöffnet lassen (Belüftung)
- [ ] Bei Hohlprofildichtungen: Kondenswasser ausdrücken
- [ ] Lukenabdeckungen installieren (UV-Schutz)
- [ ] Defekte Dichtungen für Frühjahrstausch vorbestellen

## ANHANG J: Kostenvergleich Dichtungsmaterialien

| Material | Kosten/m | Lebensdauer | Kosten/m/Jahr | Gesamtkosten 20 J (10 m Boot, 8 Luken) |
|----------|----------|-------------|---------------|----------------------------------------|
| PVC | 2–4 EUR | 3–5 Jahre | 0,60–1,33 EUR | 640–1.060 EUR |
| Neopren | 4–8 EUR | 3–5 Jahre | 1,00–2,67 EUR | 1.280–2.130 EUR |
| EPDM Standard | 4–8 EUR | 5–8 Jahre | 0,63–1,60 EUR | 800–1.280 EUR |
| EPDM Premium | 6–12 EUR | 8–12 Jahre | 0,60–1,50 EUR | 640–960 EUR |
| Silikon | 8–18 EUR | 8–12 Jahre | 0,80–2,25 EUR | 960–1.440 EUR |
| Silikon Premium | 12–25 EUR | 10–15 Jahre | 0,93–2,50 EUR | 960–1.600 EUR |

Hinweis: Arbeitskosten bei Selbsteinbau nicht berücksichtigt. Bei Werfteinbau +100–250 EUR pro Tausch.

## ANHANG K: Fallstudien

### Fallstudie FS-01: Bavaria 40 Cruiser (Bj. 2012), Mittelmeer

- **Problem:** Alle 6 Decksluken undicht nach 8 Jahren, Wassereintritt bei Regen
- **Befund:** EPDM-Dichtungen (Lewmar Mk2) mit Compression-Set 45 %, Shore 72A
- **Ursache:** Permanente Kompression + Mittelmeer-UV ohne Lukenabdeckungen
- **Maßnahme:** Kompletttausch aller 6 Luken-Dichtungen auf EPDM Premium
- **Material:** 6 × 2,2 m Profil 19911420 = 13,2 m × 7 EUR = 92 EUR
- **Arbeitszeit:** 6 × 1,5 h = 9 h Selbsteinbau
- **Ergebnis:** Alle Luken dicht, Wasserstrahltest bestanden
- **AYDI-Score:** vorher 25, nachher 95
- **Empfehlung:** Lukenabdeckungen installieren, jährliche Glycerinpflege
- **Kosten gesamt:** 120 EUR (Material + Verbrauchsmaterial)
- **Vermiedene Folgekosten:** ~800 EUR Werft-Reparatur, ~2.000 EUR Feuchteschäden Innenausbau

### Fallstudie FS-02: Hallberg-Rassy 37 (Bj. 2005), Nordsee

- **Problem:** Niedergangs-Schieberluke klemmt und quietscht
- **Befund:** Original-Silikondichtung intakt, aber Alu-Führungsschiene korrodiert
- **Ursache:** Galvanische Korrosion zwischen Alu-Schiene und Edelstahl-Schrauben
- **Maßnahme:** Führungsschiene mit Scotch-Brite reinigen, isolieren, Dichtung erneuern
- **Material:** 3 m Lippenprofil EPDM + Alu-Schutzband = 45 EUR
- **Arbeitszeit:** 4 h
- **Ergebnis:** Schieber leichtgängig, kein Quietschen, dicht
- **AYDI-Score:** vorher 40, nachher 88
- **Empfehlung:** Alu-Schiene alle 2 Jahre mit Tef-Gel behandeln
- **Kosten gesamt:** 65 EUR
- **Lerneffekt:** Kontaktkorrosion als häufige Ursache für Klemmprobleme identifiziert

### Fallstudie FS-03: Jeanneau Sun Odyssey 440 (Bj. 2019), Karibik

- **Problem:** Vordere Bugluken nach 3 Jahren undicht, Neopren-Dichtung zerstört
- **Befund:** Goiot-Originaldichtung (Neopren CR) mit UV-Rissbildung und Shore 78A
- **Ursache:** Tropische UV-Strahlung zerstört Neopren in 2–3 Jahren
- **Maßnahme:** Austausch gegen Silikon-Profil (Sonderanfertigung, Goiot-kompatibel)
- **Material:** 4 × 1,8 m Silikonprofil = 7,2 m × 15 EUR = 108 EUR
- **Arbeitszeit:** 4 × 2 h = 8 h
- **Ergebnis:** Luken dicht, Silikon nach 2 weiteren Jahren ohne Befund
- **AYDI-Score:** vorher 15, nachher 92
- **Empfehlung:** In den Tropen grundsätzlich Silikon statt Neopren verwenden
- **Kosten gesamt:** 145 EUR (inkl. Primer und Versand Sonderprofil)
- **Vermiedene Folgekosten:** Jahresintervall Neopren-Tausch ~80 EUR/Jahr

### Fallstudie FS-04: Bénéteau Océanis 51.1 (Bj. 2018), Adria

- **Problem:** Panoramafenster im Salon undicht an Oberkante
- **Befund:** Sikaflex-295 UV Verklebung intakt, aber Dichtflansch-Spalt 3 mm oben
- **Ursache:** Thermische Ausdehnung des GFK-Decks bei 50 °C Oberflächentemperatur
- **Maßnahme:** Fenster nachverkleben mit dickerer Sikaflex-Raupe (8 mm statt 5 mm)
- **Material:** Sikaflex-295 UV 300 ml + Primer-206 G+P = 55 EUR
- **Arbeitszeit:** 6 h (inkl. Entfernung alter Dichtmasse)
- **Ergebnis:** Dicht, auch nach Sommer bei 45 °C Decktemperatur
- **AYDI-Score:** vorher 35, nachher 90
- **Empfehlung:** Bei dunklen Decks in Südeuropa Klebstoffdicke >6 mm wählen
- **Kosten gesamt:** 75 EUR
- **Vermiedene Folgekosten:** ~1.200 EUR für Polster-Ersatz bei Wasserschaden

### Fallstudie FS-05: Najad 440 (Bj. 2000), Schweden/Ostsee

- **Problem:** Original-Silikondichtungen nach 20 Jahren teilweise verhärtet
- **Befund:** Shore 58A (noch akzeptabel), Compression-Set 30 %, Stoßstellen leicht offen
- **Ursache:** Normaler Alterungsprozess, Silikon übertrifft EPDM-Lebensdauer deutlich
- **Maßnahme:** Nur Stoßstellen nachkleben, Kompletttausch auf nächste Saison verschieben
- **Material:** Loctite 480 + Silikonpflege = 20 EUR
- **Arbeitszeit:** 2 h
- **Ergebnis:** Stoßstellen dicht, Gesamtzustand für 1–2 weitere Saisons akzeptabel
- **AYDI-Score:** vorher 55, nachher 72
- **Empfehlung:** Kompletttausch in 1–2 Jahren planen
- **Kosten gesamt:** 20 EUR (Interim-Maßnahme)
- **Bemerkung:** Beleg für Silikon-Langlebigkeit: 20 Jahre bei Ostsee-Bedingungen

### Fallstudie FS-06: X-Yachts Xc 45 (Bj. 2015), Atlantik-Überquerung

- **Problem:** Cockpitluke (Steuerbordbord) undicht bei schwerem Seegang (>6 Bft)
- **Befund:** Dichtung intakt (Score 82), aber Rahmen 1,5 mm verzogen durch Riggspannung
- **Ursache:** Asymmetrische Riggspannung verzieht Deck und Lukenrahmen
- **Maßnahme:** Kompensationsdichtung (Hohlprofil mit größerem Querschnitt) eingebaut
- **Material:** 2,5 m Lewmar Ocean Profil (14×10 statt 12×8) = 45 EUR
- **Arbeitszeit:** 2 h
- **Ergebnis:** Dicht bis 8 Bft, Kompensation der Rahmenbewegung durch größeres Profil
- **AYDI-Score:** vorher 65, nachher 85
- **Empfehlung:** Bei Segelbooten >12 m Riggspannung und Lukendichtigkeit korreliert prüfen
- **Kosten gesamt:** 50 EUR
- **Lerneffekt:** Rigg-Tuning beeinflusst Deckslukendichtigkeit bei Semi-Custom-Yachten

### Fallstudie FS-07: Hanse 505 (Bj. 2017), Winterlager Norddeutschland

- **Problem:** Frostschaden an 4 Decksluken nach Winter -18 °C
- **Befund:** EPDM-Hohlprofildichtungen gerissen, Wasser war in Hohlkammern gefroren
- **Ursache:** Luken fest verschlossen im Winterlager, Kondenswasser in Hohlprofilen
- **Maßnahme:** Alle 4 Dichtungen getauscht, Winterlager-Protokoll angepasst
- **Material:** 4 × 2,2 m EPDM Premium = 8,8 m × 8 EUR = 70 EUR
- **Arbeitszeit:** 4 × 1,5 h = 6 h
- **Ergebnis:** Neue Dichtungen dicht, Winterprotokoll enthält nun Luken-Lüftungsregel
- **AYDI-Score:** vorher 10, nachher 95
- **Empfehlung:** Im Winterlager Luken immer 2–3 mm offen lassen, Hohlprofildichtungen ausdrücken
- **Kosten gesamt:** 95 EUR
- **Vermiedene Folgekosten:** Rechtzeitige Erkennung verhinderte Schimmelbildung im Vorschiff

### Fallstudie FS-08: Bénéteau First 40.7 (Bj. 2003), Regattaeinsatz Mittelmeer

- **Problem:** Großluke (Vorschiff) undicht bei Halse/Wende unter Spinnaker
- **Befund:** Dichtung in Ordnung, aber Schließmechanismus durch Regatta-Belastung ausgeleiert
- **Ursache:** Wiederholte Stoßbelastung bei Manövern lockert Scharnierbolzen
- **Maßnahme:** Scharnierbolzen getauscht, Verriegelungshebel nachgestellt, Dichtung erneuert
- **Material:** 2 Scharnierbolzen Edelstahl 316L + Dichtung = 85 EUR
- **Arbeitszeit:** 3 h
- **Ergebnis:** Luke dicht auch unter Regattabedingungen bis 7 Bft
- **AYDI-Score:** vorher 30, nachher 90
- **Empfehlung:** Bei Regattabooten Scharnierbolzen jährlich prüfen und nachziehen
- **Kosten gesamt:** 85 EUR
- **Lerneffekt:** Dichtungsproblem war in Wirklichkeit ein Beschlagproblem — ganzheitliche Diagnose wichtig

## ANHANG L: Prüfprotokoll-Vorlage

```
DICHTUNGS-PRÜFPROTOKOLL
========================
Boot: _________________ Typ: _________________ Bj: _____
Eigner: _______________ Datum: ________________ Prüfer: __________

LUKE/FENSTER Nr: _____ Position: _______________
Hersteller: __________ Modell: _________________ Größe: ___________

DICHTUNG:
  Material: [ ] EPDM  [ ] Silikon  [ ] Neopren  [ ] PVC  [ ] Andere: ____
  Profiltyp: [ ] Hohlprofil  [ ] Rundschnur  [ ] D  [ ] P  [ ] E  [ ] Lippe  [ ] Flach
  Breite: _____ mm    Höhe: _____ mm    Hersteller: _______________
  Alter (geschätzt): _____ Jahre

MESSWERTE:
  Shore-Härte: _____ A  (Grenzwert: 70A)
  Compression Set: _____ %  (Grenzwert: 40 %)
  Kompressionsgrad: _____ %  (Optimal: 25–35 %)

SICHTPRÜFUNG:
  [ ] Risse     [ ] UV-Schäden   [ ] Verfärbung   [ ] Schimmel
  [ ] Ablösung  [ ] Quellung     [ ] Verhärtung    [ ] Fremdkörper
  Bemerkungen: ________________________________________________

DICHTIGKEITSTEST:
  [ ] Wasserstrahltest:  [ ] bestanden  [ ] nicht bestanden
  [ ] Kreidetest:        [ ] gleichmäßig  [ ] ungleichmäßig
  [ ] Papierstreifentest: [ ] gleichmäßig  [ ] ungleichmäßig
  Leckage-Position: ________________________________________________

BEWERTUNG:
  AYDI-Score: _____ / 100
  Empfehlung: [ ] i.O.  [ ] Überwachen  [ ] Austausch planen  [ ] Sofort tauschen
  Nächste Prüfung: ________________
```

## ANHANG M: Umrechnungstabellen

| Von | Nach | Faktor |
|-----|------|--------|
| mm | Zoll (inch) | × 0,03937 |
| Zoll (inch) | mm | × 25,4 |
| Shore A | Shore D (grob) | Shore D ≈ Shore A - 50 (ab 80A) |
| bar | PSI | × 14,504 |
| °C | °F | × 1,8 + 32 |
| N/mm | lbf/in | × 5,710 |
| EUR/m | EUR/ft | × 0,3048 |

## ANHANG N: Abkürzungsverzeichnis

| Abkürzung | Bedeutung |
|-----------|-----------|
| CS | Compression Set |
| CR | Chloroprenkautschuk (Neopren) |
| EPDM | Ethylen-Propylen-Dien-Monomer |
| FKM | Fluorkautschuk |
| FVMQ | Fluorsilikon |
| GFK | Glasfaserverstärkter Kunststoff |
| IIR | Isobuten-Isopren-Kautschuk (Butyl) |
| IPA | Isopropanol |
| MOB | Mann über Bord |
| NBR | Acrylnitril-Butadien-Kautschuk (Nitril) |
| NR | Naturkautschuk |
| PU | Polyurethan |
| PVC | Polyvinylchlorid |
| SBR | Styrol-Butadien-Kautschuk |
| TPE | Thermoplastisches Elastomer |
| TPU | Thermoplastisches Polyurethan |
| VMQ | Vinyl-Methyl-Polysiloxan (Silikon) |

## ANHANG O: Visuelle Analyse Pipeline B — Erkennungsparameter

| Fehlerbild | Erkennungsmerkmal | Min. Auflösung | Confidence |
|------------|-------------------|----------------|------------|
| FB-01 Compression Set | Profilhöhenvergleich | 0,5 mm/px | visual_medium |
| FB-02 UV-Risse | Rissmuster, Netzstruktur | 0,2 mm/px | visual_high |
| FB-03 Klebstoffversagen | Spalt, abstehend | 0,5 mm/px | visual_high |
| FB-04 Falsches Profil | Quetschfalten, Lücken | 0,5 mm/px | visual_high |
| FB-05 Verhärtung | Glanz, starrer Verlauf | 1,0 mm/px | visual_medium |
| FB-06 Riss/Einriss | Materialunterbrechung | 0,3 mm/px | visual_high |
| FB-07 Schimmel | Schwarze Flecken | 0,5 mm/px | visual_high |
| FB-08 Lackkontamination | Farbspuren | 0,5 mm/px | visual_high |
| FB-09 Ungleiche Kompression | Asymmetrischer Spalt | 1,0 mm/px | visual_medium |
| FB-10 Falsche Shore-Härte | Verformungsgrad | – | visual_low |
| FB-11 Thermische Schrumpfung | Ecklücken | 0,5 mm/px | visual_medium |
| FB-12 Chemischer Angriff | Quellung, Verfärbung | 0,5 mm/px | visual_medium |

## ANHANG P: Wartungskosten-Kalkulation 20 Jahre

**Beispiel: 12 m Segelboot, 6 Decksluken + 8 Fenster + 1 Niedergang**

| Position | EPDM-Szenario | Silikon-Szenario | PVC-Szenario |
|----------|---------------|------------------|--------------|
| Material Luken (6×) | 6×14 m × 6 EUR × 3 Tausche = 1.512 EUR | 6×14 m × 14 EUR × 2 Tausche = 2.352 EUR | 6×14 m × 3 EUR × 5 Tausche = 1.260 EUR |
| Material Fenster (8×) | 8×3 m × 6 EUR × 3 = 432 EUR | 8×3 m × 14 EUR × 2 = 672 EUR | 8×3 m × 3 EUR × 5 = 360 EUR |
| Material Niedergang | 4 m × 8 EUR × 3 = 96 EUR | 4 m × 16 EUR × 2 = 128 EUR | 4 m × 4 EUR × 5 = 80 EUR |
| Arbeitszeit Selbsteinbau | 3 × 16 h × 0 EUR = 0 EUR | 2 × 16 h × 0 EUR = 0 EUR | 5 × 16 h × 0 EUR = 0 EUR |
| Pflegemittel | 20 × 10 EUR = 200 EUR | 20 × 10 EUR = 200 EUR | 20 × 10 EUR = 200 EUR |
| **Gesamt (Selbsteinbau)** | **2.240 EUR** | **3.352 EUR** | **1.900 EUR** |
| Arbeitszeit Werft | 3 × 16 h × 90 EUR = 4.320 EUR | 2 × 16 h × 90 EUR = 2.880 EUR | 5 × 16 h × 90 EUR = 7.200 EUR |
| **Gesamt (Werft)** | **6.560 EUR** | **6.232 EUR** | **9.100 EUR** |

**Fazit:** Silikon ist bei Werfteinbau langfristig am günstigsten trotz höherer Materialkosten. PVC ist bei Werfteinbau das teuerste Material über 20 Jahre.

## ANHANG Q: AYDI-Modul-Integration

### Betroffene AYDI-Module

| Modul | Relevanz | Daten aus 08.05 |
|-------|----------|-----------------|
| materials | Primär | Dichtungsmaterial, Shore-Härte, Alterungszustand |
| compliance | Primär | ISO 12216 Konformität, CE-Anforderungen |
| production | Sekundär | Einbauqualität, Profilwahl |
| structural | Sekundär | Rahmenintegrität, Verzug |
| ergonomics | Tertiär | Bedienbarkeit der Luken |
| cost | Sekundär | Wartungskosten, Lifecycle-Kosten |
| service_patterns | Primär | Häufige Defektmuster, Wartungsintervalle |
| emotional | Tertiär | Sauberkeit, Geruch, optischer Eindruck |
| brand_dna | Sekundär | Herstellerspezifische Lösungen |

### Score-Fusion-Gewichte für Dichtungsbefunde

```python
SEAL_FUSION_WEIGHTS = {
    "materials": {"structured": 0.35, "visual": 0.65},
    "compliance": {"structured": 0.95, "visual": 0.05},
    "production": {"structured": 0.55, "visual": 0.45},
    "service_patterns": {"structured": 0.65, "visual": 0.35},
}
```

## ANHANG R: Quellenverzeichnis

| Nr. | Quelle | Typ | Relevanz |
|-----|--------|-----|----------|
| 1 | ISO 12216:2020 — Windows, portlights, hatches, deadlights | Norm | Primär |
| 2 | ISO 11812:2020 — Cockpits | Norm | Sekundär |
| 3 | EU Recreational Craft Directive 2013/53/EU | Richtlinie | Primär |
| 4 | Lewmar Technical Manual, Hatch Seals | Herstellerdoku | Primär |
| 5 | Goiot Installation Guide, Cristal/Opal Series | Herstellerdoku | Primär |
| 6 | Sika Marine Application Guide (2024) | Herstellerdoku | Primär |
| 7 | Parker O-Ring Handbook (2021) | Fachliteratur | Sekundär |
| 8 | Freudenberg Sealing Technologies: EPDM Datasheet | Datenblatt | Primär |
| 9 | Trelleborg Marine Profiles Catalogue | Katalog | Sekundär |
| 10 | Practical Sailor: Hatch Seal Replacement Guide (2023) | Fachzeitschrift | Sekundär |
| 11 | Yachtsurvey.org: Hatch and Window Inspection | Fachliteratur | Sekundär |
| 12 | DIN 7863: Elastomer-Dichtprofile für Fenster und Fassade | Norm | Sekundär |
| 13 | EN 681-1: Elastomerdichtungen — Werkstoffanforderungen | Norm | Sekundär |
| 14 | SVB Dichtungsratgeber (2024) | Händlerdoku | Tertiär |
| 15 | Compass24 Luken-Dichtungs-Finder (2024) | Händlerdoku | Tertiär |

---

> **Ende der Wissensdatei 08.05 — Luken- und Fensterdichtungen**
> Gesamtumfang: ~3.800 Zeilen
> Letzte Aktualisierung: 2026-04-25
> AYDI-Module: materials, compliance, production, service_patterns, structural, cost
