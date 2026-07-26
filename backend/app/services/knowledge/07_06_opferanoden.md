# 07.06 — Opferanoden und Korrosionsschutz

> **AYDI Wissensdatei 07.06** — Kategorie 7: Korrosionsschutz und Unterwassertechnik
> **Confidence-Quelle:** measured (Hersteller-TDS, MIL-Specs), documented (ISO/DIN-Normen, Hersteller-Kataloge, Klassegesellschaften), estimated (Erfahrungswerte, Forum-Konsens)
> **Letzte Aktualisierung:** 2026-04-24

---

## Inhaltsverzeichnis

1. [Einführung & Regulatorischer Rahmen](#1-einführung--regulatorischer-rahmen)
2. [Zukunftstechnologien (ICCP, Smart Monitoring, neue Legierungen)](#2-zukunftstechnologien-iccp-smart-monitoring-neue-legierungen)
3. [Best Practices nach Revier](#3-best-practices-nach-revier)
4. [Regional Sourcing](#4-regional-sourcing)
5. [Zweck dieser Wissensdatei](#5-zweck-dieser-wissensdatei)
6. [Pydantic-Modelle](#6-pydantic-modelle)
7. [Grundlagen](#7-grundlagen)
8. [Hersteller — Vollständige Übersicht](#8-hersteller--vollständige-übersicht)
9. [Anlagen-spezifische Zuordnung](#9-anlagen-spezifische-zuordnung)

---

## 1. Einführung & Regulatorischer Rahmen

### 1.1 Warum Opferanoden überlebenswichtig sind

Galvanische Korrosion ist der häufigste und teuerste Schadensmechanismus an Unterwasser-Metallteilen von Yachten. Ohne funktionierenden kathodischen Schutz kann ein Bronzepropeller innerhalb einer Saison durchkorrodieren, ein Edelstahlwellenschaft Lochfraß zeigen, ein Ruderkoker bis zur Undichtigkeit angegriffen werden. Die Schadensummen beginnen bei wenigen hundert Euro für einen neuen Zinkanode-Satz und reichen bis zu fünfstelligen Beträgen für den Austausch eines Propellers, einer Welle oder eines Saildrives.

**Kernprinzip:** Eine Opferanode (Sacrificial Anode) ist ein Metallstück mit niedrigerem elektrochemischen Potenzial als die zu schützende Struktur. Die Anode korrodiert kontrolliert anstelle der wertvollen Unterwasserkomponenten. Sie „opfert" sich — daher der Name.

### 1.2 Relevante Normen und Standards

| Norm | Bezeichnung | Geltungsbereich | Relevanz für Yachtbau |
|------|-------------|-----------------|----------------------|
| **ISO 15589-2:2012** | Cathodic protection of pipeline transportation systems — Part 2: Offshore pipelines | Kathodischer Schutz von Offshore-Pipelines | Referenz für Schutzpotenziale; sinngemäß auf marine Strukturen übertragbar (nicht schiffsrumpf-spezifisch) |
| **DIN EN 12496:2013** | Galvanische Anoden für den kathodischen Korrosionsschutz in Seewasser und Meeresboden | Legierungszusammensetzung, elektrochemische Mindestleistung | Definiert Qualitätsanforderungen an Anodenlegierungen |
| **DIN EN 13174:2001** | Kathodischer Korrosionsschutz für Hafeninfrastrukturen | Ergänzend für Liegeplatz-Wechselwirkungen | Relevant bei Landstrom-Problemen |
| **ABYC E-2** | Cathodic Protection | Nordamerikanischer Standard | De-facto-Weltstandard für Yachten, sehr detailliert |
| **MIL-A-18001K** | Anodes, Corrosion Preventive, Zinc; Slab, Disc, and Rod Shaped | Militär-Spec für Zinkanoden | Definiert Legierungszusammensetzung für marine Zinkanoden |
| **MIL-DTL-24779C** | Anodes, Sacrificial, Aluminum Alloy | Militär-Spec für Aluminiumanoden | Definiert Al-Zn-In-Legierungsanforderungen |
| **NACE SP0176-2007** | Corrosion Control of Submerged Areas of Permanently Installed Steel Offshore Structures | Offshore-Kathodenschutz | Berechnungsgrundlagen für Anodenauslegung |
| **DNV-RP-B401:2021** | Cathodic Protection Design | Offshore-Kathodenschutz-Design | Industriestandard für Auslegungsberechnungen |
| **ISO 8044:2020** | Corrosion of metals and alloys — Basic terms and definitions | Korrosionsterminologie | Einheitliche Fachbegriffe |

### 1.3 Schutzpotenziale nach Normen

Die zentrale Größe ist das **Schutzpotenzial** (Protection Potential), gemessen gegen eine Ag/AgCl-Referenzelektrode in Seewasser:

| Werkstoff | Min. Schutzpotenzial (mV vs. Ag/AgCl) | Max. Schutzpotenzial (mV vs. Ag/AgCl) | Quelle |
|-----------|---------------------------------------|---------------------------------------|--------|
| Kohlenstoffstahl | −800 | −1100 | DNV-RP-B401 |
| Edelstahl 316L | −500 | −1100 | ABYC E-2 |
| Kupfer-Nickel (Cu-Ni 90/10) | −300 | −650 | ISO 15589-2 |
| Bronze (G-CuSn) | −300 | −650 | ISO 15589-2 |
| Aluminium (Rumpf) | −800 | −1100 | ABYC E-2 |

> **Achtung:** Überprotektion (zu negatives Potenzial) kann bei Aluminiumrümpfen zur Alkaliversprödung und bei beschichteten Flächen zur Enthaftung der Beschichtung führen. Das Maximum von −1100 mV vs. Ag/AgCl ist bei Aluminiumrümpfen strikt einzuhalten.

### 1.4 CE-Relevanz und Klassegesellschaften

Die EU-Sportbootrichtlinie 2013/53/EU schreibt keinen kathodischen Schutz explizit vor, referenziert jedoch die harmonisierten Normen. In der Praxis verlangen alle seriösen Werften und Gutachter einen funktionierenden Korrosionsschutz. Klassegesellschaften (DNV, Lloyd's Register, Bureau Veritas, RINA) fordern bei klasse-geführten Yachten:

- Nachweis des kathodischen Schutzsystems im Bauplan
- Jährliche Anodeninspektion bei Klasseerneuerung
- Dokumentation der Anodenwechsel im Logbuch
- Potenzial-Messprotokoll bei Werftaufenthalt

### 1.5 Haftungsaspekte

Ein fehlender oder verbrauchter kathodischer Schutz kann bei Versicherungsschäden (z.B. Wellenbruch durch Korrosion) als **Obliegenheitsverletzung** gewertet werden. Dokumentierte Anodenwechsel-Protokolle sind bei Schadensregulierung essenziell.

---

## 2. Zukunftstechnologien (ICCP, Smart Monitoring, neue Legierungen)

### 2.1 ICCP — Impressed Current Cathodic Protection

Statt sich verbrauchender Opferanoden nutzt ein ICCP-System eine externe Gleichstromquelle, um das Schutzpotenzial aktiv einzustellen. Die Anoden bestehen aus unlöslichem Material (Titan mit MMO-Beschichtung — Mixed Metal Oxide) und verbrauchen sich praktisch nicht.

**Funktionsprinzip:**
1. Referenzelektrode (Ag/AgCl oder Zn) misst das Rumpfpotenzial
2. Steuergerät vergleicht Ist- mit Soll-Potenzial (−800 bis −1100 mV)
3. Gleichrichter speist kontrollierten Strom über MMO-Titan-Anode ein
4. Feedback-Regelung hält Potenzial im Schutzbereich

**Vorteile gegenüber Opferanoden:**
- Keine regelmäßigen Anodenwechsel (Titananoden halten 15–20 Jahre)
- Exakte Potenzialregelung — kein Über- oder Unterschutz
- Geringerer hydrodynamischer Widerstand (flache Anoden)
- Für Aluminiumrümpfe besonders geeignet (Potenzialgrenze einhaltbar)

**Nachteile:**
- Hohe Anschaffungskosten: ab 2.500 EUR (< 12 m) bis 15.000+ EUR (> 20 m)
- Stromversorgung erforderlich (permanent 12/24 V DC)
- Bei Systemausfall kein Schutz — Backup-Opferanoden empfohlen
- Fachinstallation erforderlich
- Regelmäßige Kalibrierung der Referenzelektrode

**Hersteller von Marine-ICCP-Systemen:**

| Hersteller | System | Bootsgröße | Preis (EUR) | Besonderheit |
|-----------|--------|------------|-------------|-------------|
| **Cathelco** (UK) | ICCP Marine Series | 10–50+ m | 3.500–25.000 | Marktführer Superyacht, DNV-zugelassen |
| **Farwest Corrosion Control** (USA) | Mariner Series | 8–30 m | 2.500–12.000 | Robuste Yacht-Systeme |
| **Corrosion Control International** (AUS) | CCI Marine | 12–60 m | 4.000–20.000 | Erfahrung mit Aluminiumrümpfen |
| **CMP (Canada Metal Pacific)** | Guardian ICCP | 10–25 m | 2.800–8.000 | Retrofit-freundlich |
| **Sea Shield Marine** (USA) | AquaShield ICCP | 8–20 m | 2.200–6.500 | Einstiegssegment |
| **Anode Engineering** (AUS) | AE-ICCP | 15–50 m | 5.000–18.000 | Superyacht-Fokus |

### 2.2 Hybrid-Systeme (ICCP + Opferanoden)

Zunehmend verbreitet auf Yachten ab 15 m: Ein ICCP-System schützt den Rumpf, klassische Opferanoden sichern mechanische Komponenten (Propeller, Welle, Ruder) und dienen als Backup bei ICCP-Ausfall.

**Empfehlung nach Bootsgröße:**

| Bootsgröße | Empfohlenes System | Confidence |
|------------|-------------------|------------|
| < 10 m | Nur Opferanoden | measured |
| 10–15 m | Opferanoden, ICCP optional | documented |
| 15–25 m | Hybrid (ICCP Rumpf + Opferanoden Antrieb) | documented |
| > 25 m | ICCP primär + Backup-Opferanoden | documented |

### 2.3 Smart Monitoring — Korrosionsüberwachung

Moderne Systeme ermöglichen die ferngesteuerte Überwachung des kathodischen Schutzes:

**Verfügbare Systeme:**

| System | Hersteller | Funktion | Preis (EUR) | Konnektivität |
|--------|-----------|----------|-------------|---------------|
| **CorroWatch** | Cathelco | Potenzial-Logger + Alarm | 1.200–3.500 | WiFi/GSM |
| **Aqualink CP** | McMurdo/Orolia | Referenzelektrode + Cloud | 800–2.000 | LoRa/4G |
| **Corrosion Scout** | Boatwatch | DIY-Referenzmessung + App | 350–600 | Bluetooth |
| **ZM-100** | Martyr/Zineti | Anodenverbrauch-Sensor | 150–300 | Kabelgebunden |

**Funktionalität:**
- Permanente Potentialmessung am Rumpf (mV vs. Ag/AgCl)
- Alarm bei Unterschreitung des Schutzpotenzials (< −800 mV)
- Alarm bei Überschreitung (> −1100 mV, kritisch für Aluminium)
- Trendanalyse: Anodenverbrauchsrate, prognostiziertes Wechseldatum
- Streustromerkennung: ungewöhnliche Potenzialsprünge bei Landstrom

### 2.4 Neue Anodenlegierungen

**Aluminium-Zink-Indium-Gallium (Al-Zn-In-Ga):**
Die neueste Generation der Al-Anoden ersetzt Quecksilber durch Gallium als Aktivator. Vorteile: RoHS-konform, gleichmäßigere Auflösung, höhere Stromausbeute (bis 2.800 Ah/kg vs. 2.600 Ah/kg bei Al-Zn-In).

**Magnesium-Lithium-Legierungen (experimental):**
Für extreme Süßwasserbedingungen (< 500 µS/cm Leitfähigkeit). Höheres Treibpotenzial als Standard-Magnesium, aber noch nicht marine-qualifiziert.

**Nano-strukturierte Zinkanoden:**
Forschungsansatz: nano-kristalline Zinklegierungen mit höherer Kapazität (830+ Ah/kg vs. 780 Ah/kg Standard). Laborphase, 3–5 Jahre bis Marktreife.

---

## 3. Best Practices nach Revier

### 3.1 Salzwasser (> 20.000 µS/cm) — Nordsee, Mittelmeer, Karibik, Atlantik

**Empfohlenes Anodenmaterial:** Zink oder Aluminium

| Parameter | Zink (MIL-A-18001K) | Aluminium (MIL-DTL-24779C) |
|-----------|---------------------|---------------------------|
| Treibpotenzial vs. Ag/AgCl | −1.050 mV | −1.100 mV |
| Stromkapazität | 780 Ah/kg | 2.600 Ah/kg |
| Dichte | 7,1 g/cm³ | 2,7 g/cm³ |
| Gewicht für gleichen Schutz | 100% (Referenz) | ca. 30% |
| Preis pro kg | 8–12 EUR | 12–18 EUR |
| Preis pro Ah | 0,010–0,015 EUR | 0,005–0,007 EUR |
| Empfehlung | Standard, bewährt | Leichter, wirtschaftlicher, Zukunft |

**Spezifische Salzwasser-Regeln:**
- Mindestens 2× jährliche Sichtprüfung aller Anoden (Saisonstart + Mitte)
- Wechsel bei 50% Verbrauch — nicht warten bis zur vollständigen Auflösung
- Anoden nach Bewuchs frei kratzen — biologischer Bewuchs isoliert die Anode
- Antifouling niemals auf Anoden auftragen
- Tropische Gewässer (> 25°C): Korrosionsrate um 25–40% erhöht → kürzere Intervalle

**Salzwasser-Spezialfall Mittelmeer:**
- Höherer Salzgehalt (38–39 ‰ vs. 35 ‰ Atlantik) → leicht erhöhte Korrosionsrate
- Viele Häfen mit schlecht gewarteten Landstromanlagen → Streustromproblem
- Galvanischer Isolator am Landstromkabel obligatorisch
- Al-Anoden bevorzugt wegen besserer Langzeitleistung bei hohen Temperaturen

**Salzwasser-Spezialfall Tropen (Karibik, Südostasien):**
- Wassertemperaturen 27–32°C: Korrosionsrate doppelt so hoch wie in der Nordsee
- Biologischer Bewuchs extrem schnell → Anoden alle 4–6 Wochen reinigen
- Aluminium-Anoden bevorzugt (höhere Kapazität kompensiert schnelleren Verbrauch)
- ICCP-Systeme hier besonders wirtschaftlich (vermeidet häufige Tauchgänge)

### 3.2 Brackwasser (2.000–20.000 µS/cm) — Ostsee, Flussmündungen, Lagunen

**Empfohlenes Anodenmaterial:** Aluminium (bevorzugt) oder Magnesium

Brackwasser ist für den kathodischen Schutz besonders anspruchsvoll, da die Leitfähigkeit stark schwankt:

| Region | Salzgehalt (‰) | Leitfähigkeit (µS/cm) | Empfohlene Anode |
|--------|----------------|----------------------|-----------------|
| Ostsee (Kiel) | 15–18 | 12.000–15.000 | Aluminium |
| Ostsee (Stockholm) | 5–7 | 5.000–7.000 | Aluminium |
| Ostsee (Helsinki) | 3–5 | 3.000–5.000 | Aluminium oder Magnesium |
| Ostsee (Bottenwiek) | 1–3 | 1.000–3.000 | Magnesium |
| Flussmündung (Elbe) | 5–25 (tideabhängig) | variabel | Aluminium |
| IJsselmeer (NL) | 0,5–3 | 500–3.000 | Magnesium |

**Besonderheiten Brackwasser:**
- Zink funktioniert unter ~10.000 µS/cm nicht mehr zuverlässig (Passivierung)
- Aluminium bleibt bis ca. 3.000 µS/cm aktiv (dank Indium-Aktivierung)
- Magnesium notwendig unter 3.000 µS/cm
- Magnesium in Salzwasser NICHT verwenden (löst sich zu schnell auf, Überprotektion)

### 3.3 Süßwasser (< 2.000 µS/cm) — Binnenseen, Flüsse, Kanäle

**Empfohlenes Anodenmaterial:** Magnesium (einzige zuverlässige Option)

| Parameter | Magnesium (AZ-63/AZ-31) |
|-----------|--------------------------|
| Treibpotenzial vs. Ag/AgCl | −1.550 mV |
| Stromkapazität | 1.100–1.230 Ah/kg |
| Selbstkorrosionsrate | Hoch (Nachteil) |
| Stromausbeute | 50–55% (Rest = Selbstkorrosion) |
| Empfehlung | Einzige Option für Süßwasser |

**Süßwasser-Spezialregeln:**
- Zink und Aluminium sind in Süßwasser **wirkungslos** (passivieren sofort)
- Magnesium-Anoden verbrauchen sich auch ohne Schutzstrom (Selbstkorrosion ~50%)
- Größere Anoden einplanen als im Salzwasser-Äquivalent
- Wasserqualität prüfen: extrem weiches Wasser (< 200 µS/cm) kann selbst Magnesium passivieren → ICCP empfohlen
- Kalkhaltige Gewässer: Kalkablagerungen auf Anoden entfernen

### 3.4 Zusammenfassende Reviermatrix

| Revier | Leitfähigkeit | Zink | Aluminium | Magnesium | ICCP |
|--------|--------------|------|-----------|-----------|------|
| Hochsee / Atlantik | > 40.000 µS/cm | ✓✓✓ | ✓✓✓ | ✗ | ✓✓ |
| Mittelmeer | > 45.000 µS/cm | ✓✓ | ✓✓✓ | ✗ | ✓✓✓ |
| Tropen | > 45.000 µS/cm | ✓ | ✓✓✓ | ✗ | ✓✓✓ |
| Nordsee | 30.000–40.000 µS/cm | ✓✓✓ | ✓✓✓ | ✗ | ✓✓ |
| Ostsee West (Kiel) | 12.000–18.000 µS/cm | ✓ | ✓✓✓ | ✓ | ✓✓ |
| Ostsee Ost | 3.000–7.000 µS/cm | ✗ | ✓✓ | ✓✓ | ✓✓ |
| Brackwasser | 2.000–10.000 µS/cm | ✗ | ✓✓ | ✓✓ | ✓✓ |
| Süßwasser | 500–2.000 µS/cm | ✗ | ✗ | ✓✓✓ | ✓✓✓ |
| Weiches Süßwasser | < 500 µS/cm | ✗ | ✗ | ✓ | ✓✓✓ |

> Legende: ✓✓✓ = optimale Wahl, ✓✓ = geeignet, ✓ = bedingt geeignet, ✗ = ungeeignet
> Confidence: `documented` (basierend auf ABYC E-2, Herstellerempfehlungen, Praxiserfahrung)

---

## 4. Regional Sourcing

### 4.1 Europa — Bezugsquellen

| Händler / Distributor | Land | Sortiment | Online-Shop | Besonderheit |
|----------------------|------|-----------|-------------|-------------|
| **SVB (Sailing & Vinylester Bedarf)** | DE | Martyr, Tecnoseal, Camp, OEM | svb-marine.de | Größter deutscher Yachtzubehör-Versand |
| **Toplicht** | DE | Martyr, MG Duff, OEM | toplicht.de | Hamburger Traditionshändler |
| **AWN** | DE | Martyr, Camp, Vetus | awn.de | Breites Sortiment |
| **Compass24** | DE | Martyr, Tecnoseal, Camp | compass24.de | Gute OEM-Zuordnung |
| **Yachtausrüster Arlt** | DE | Martyr, Tecnoseal | arlt-maritim.de | Ostsee-Fokus |
| **ASAP Supplies** | UK | Martyr, MG Duff, Tecnoseal, CMP | asap-supplies.com | Riesiges Anodensortiment |
| **Seapower Marine** | UK | MG Duff, Martyr | seapowermarine.co.uk | Spezialist für UK-Markt |
| **Accastillage Diffusion** | FR | Tecnoseal, Camp | ad-europe.com | Frankreich + Mittelmeer |
| **Navimo / Plastimo** | FR | Camp, Tecnoseal | plastimo.com | Französischer Marktführer |
| **Forniture Nautiche Italiane (FNI)** | IT | Tecnoseal, Camp/Zineti | ffranceschetti.it | Direktimport Italien |
| **Allpa** | NL | Camp, Vetus, Martyr | allpa.nl | Benelux-Distributor |

### 4.2 Nordamerika — Bezugsquellen

| Händler / Distributor | Land | Sortiment | Online-Shop |
|----------------------|------|-----------|-------------|
| **Fisheries Supply** | USA | Martyr, Performance Metals, CMP | fisheriessupply.com |
| **West Marine** | USA | Martyr, CMP, OEM | westmarine.com |
| **Defender Industries** | USA | Martyr, Performance Metals, CMP | defender.com |
| **Hamilton Marine** | USA | Martyr, CMP | hamiltonmarine.com |
| **Canada Metal Pacific** | CAN | CMP (Hersteller + Direktvertrieb) | canadametal.com |

### 4.3 OEM-Anoden — Bezug über autorisierte Händler

Für Motor- und Antriebsanoden ist der Bezug über den OEM-Händler oft vorzuziehen:

| OEM | Typische Anode | OEM-Preis (EUR) | Aftermarket-Äquivalent | Aftermarket-Preis (EUR) |
|-----|---------------|----------------|----------------------|------------------------|
| Volvo Penta | 3888305 (Saildrive 120S) | 35–45 | Martyr CMV-18-6Z | 18–25 |
| Volvo Penta | 3858399 (Ruderblatt) | 45–60 | Tecnoseal 00702 | 22–32 |
| Yanmar | 27210-200300 (Saildrive SD20) | 40–55 | Camp 70-YSDR | 20–28 |
| Yanmar | 196420-02652 (Motorblock) | 15–22 | Martyr CM196420-02652Z | 8–14 |
| Mercury/MerCruiser | 97-826134Q | 30–40 | CMP MRC-M826134 | 15–22 |
| Mercury/MerCruiser | 97-821630Q1 (Alpha) | 25–35 | Martyr CM-821630Z | 12–18 |
| Mercury/MerCruiser | 97-821631Q1 (Bravo) | 28–38 | Martyr CM-821631Z | 14–20 |

> Confidence: `estimated` (Preise Stand 2025/2026, schwanken nach Zinkpreis und Lieferkette)

### 4.4 Preisindikation nach Bootsgröße — Kompletter Anodensatz

| Bootsgröße | Segelboot (Satz) | Motorboot (Satz) | Intervall |
|------------|-----------------|-----------------|-----------|
| 7–9 m | 80–150 EUR | 120–200 EUR | 12–24 Monate (Salzwasser) |
| 10–12 m | 150–280 EUR | 200–400 EUR | 12–18 Monate |
| 13–16 m | 280–500 EUR | 400–700 EUR | 12 Monate |
| 17–20 m | 500–900 EUR | 700–1.200 EUR | 12 Monate |
| 21–25 m | 900–1.500 EUR | 1.200–2.500 EUR | 6–12 Monate |
| > 25 m | 1.500–4.000 EUR | 2.500–8.000 EUR | 6–12 Monate + Taucher |

---

## 5. Zweck dieser Wissensdatei

### 5.1 Einordnung im AYDI-System

Diese Wissensdatei dient dem AYDI-Analysemodul als Referenz für:

1. **Materialmodul:** Bewertung des Korrosionsschutzzustands aller Unterwasser-Metallteile
2. **Strukturmodul:** Erkennung korrosionsbedingter Strukturschwächen (Wellenschaft, Ruderkoker, Kielbefestigung)
3. **Compliance-Modul:** Prüfung auf normgerechten kathodischen Schutz
4. **Kostenmodul:** Parametrische Kostenschätzung für Anodenwechsel und ICCP-Installation
5. **Service-Pattern-Modul:** Erkennung von Korrosionsmustern in Wartungsberichten
6. **Visuelles Modul:** Pipeline-B-Analyse von Unterwasserfotos (Anodenzustand, Korrosionsspuren)

### 5.2 Confidence-Zuordnung

| Datenquelle | Confidence-Level | Beispiel |
|-------------|-----------------|---------|
| MIL-Spec-Datenblatt | `measured` | Legierungszusammensetzung, Stromkapazität |
| Hersteller-TDS | `measured` | Produktabmessungen, Gewicht |
| ISO/DIN-Norm | `documented` | Schutzpotenziale, Prüfverfahren |
| Klassegesellschaft | `documented` | Inspektionsintervalle, Anforderungen |
| AYDI-Fotobewertung | `visual_high` bis `visual_insufficient` | Anoden-Verbrauchsgrad aus Foto |
| Forum-Konsens / Praxis | `estimated` | Wechselintervalle, Revierspezifika |
| Preisangaben | `estimated` | Tagespreisabhängig, Zinkbörse |

### 5.3 Integration in Pipeline B (Visuelle Analyse)

Typische Fotobefunde, die das visuelle Modul erkennen muss:

| Befund | Severity | Confidence-Anforderung | Nächster Schritt |
|--------|----------|----------------------|-----------------|
| Anode > 50% verbraucht | WARNING | `visual_medium` | Wechsel empfehlen |
| Anode komplett verbraucht / fehlend | CRITICAL | `visual_high` | Sofortiger Wechsel |
| Lochfraß an Propeller / Welle | CRITICAL | `visual_high` | Fachbetrieb einschalten |
| Galvanische Korrosion (Verfärbung) | WARNING | `visual_medium` | Ursachensuche empfehlen |
| Streustrommuster (lokalisierte Auflösung) | CRITICAL | `visual_high` | Elektrik prüfen lassen |
| Bewuchs auf Anoden | INFO | `visual_low` | Reinigung empfehlen |
| Falscher Anodentyp für Revier | WARNING | `visual_insufficient` | Revierdaten abfragen |

---

## 6. Pydantic-Modelle

```python
from __future__ import annotations
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


# ─── Enums ───────────────────────────────────────────────────────────

class AnodeMaterial(str, Enum):
    """Anodenwerkstoff nach Einsatzzweck."""
    ZINC = "zinc"                    # Seewasser, Standard
    ALUMINUM = "aluminum"            # Seewasser + Brackwasser
    MAGNESIUM = "magnesium"          # Süßwasser
    MMO_TITANIUM = "mmo_titanium"    # ICCP-Anoden (unlöslich)

class AnodeType(str, Enum):
    """Anodenform und Einsatzort."""
    HULL_BOLT_ON = "hull_bolt_on"
    HULL_WELD_ON = "hull_weld_on"
    SHAFT_COLLAR = "shaft_collar"
    SHAFT_DONUT = "shaft_donut"
    PROPELLER = "propeller"
    RUDDER = "rudder"
    TRIM_TAB = "trim_tab"
    SAILDRIVE = "saildrive"
    STERNDRIVE_ALPHA = "sterndrive_alpha"
    STERNDRIVE_BRAVO = "sterndrive_bravo"
    THROUGH_HULL = "through_hull"
    HEAT_EXCHANGER = "heat_exchanger"
    ENGINE_BLOCK = "engine_block"
    BOW_THRUSTER = "bow_thruster"
    KEEL = "keel"
    FLAT_HULL = "flat_hull"

class WaterType(str, Enum):
    """Fahrgebiet für Anodenwahl."""
    SALT = "salt"              # > 20.000 µS/cm
    BRACKISH = "brackish"      # 2.000–20.000 µS/cm
    FRESH = "fresh"            # < 2.000 µS/cm

class ProtectionSystem(str, Enum):
    """Art des kathodischen Schutzsystems."""
    PASSIVE_SACRIFICIAL = "passive_sacrificial"
    ICCP = "iccp"
    HYBRID = "hybrid"
    NONE = "none"

class AnodeConditionRating(str, Enum):
    """Zustandsbewertung einer Opferanode."""
    NEW = "new"                          # 0–10% verbraucht
    GOOD = "good"                        # 10–30% verbraucht
    SERVICEABLE = "serviceable"          # 30–50% verbraucht
    REPLACE_SOON = "replace_soon"        # 50–70% verbraucht
    CRITICAL = "critical"                # 70–90% verbraucht
    DEPLETED = "depleted"                # > 90% verbraucht oder fehlend
    NOT_ASSESSABLE = "not_assessable"    # Nicht beurteilbar

class CorrosionSeverity(str, Enum):
    """Korrosionsschweregrad an geschützten Komponenten."""
    NONE = "none"
    SURFACE = "surface"          # Oberflächliche Verfärbung
    MODERATE = "moderate"        # Sichtbare Materialabnahme
    SEVERE = "severe"            # Strukturrelevante Korrosion
    CRITICAL = "critical"        # Akute Versagensgefahr

class ConfidenceLevel(str, Enum):
    """AYDI-Confidence-Level für Befunde."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


# ─── Kernmodelle ─────────────────────────────────────────────────────

class AnodeSpec(BaseModel):
    """Technische Spezifikation einer Opferanode (Produktdaten)."""
    model_config = {"from_attributes": True}

    product_name: str = Field(..., description="Produktbezeichnung inkl. Hersteller-Artikelnummer")
    manufacturer: str
    manufacturer_part_number: str
    material: AnodeMaterial
    anode_type: AnodeType
    mil_spec: Optional[str] = Field(None, description="MIL-A-18001K / MIL-DTL-24779C / None")

    # Legierung
    alloy_zn_pct: Optional[float] = Field(None, ge=0, le=100)
    alloy_al_pct: Optional[float] = Field(None, ge=0, le=100)
    alloy_mg_pct: Optional[float] = Field(None, ge=0, le=100)
    alloy_in_pct: Optional[float] = Field(None, ge=0, le=1, description="Indium-Anteil in %")
    alloy_cd_pct: Optional[float] = Field(None, ge=0, le=1, description="Cadmium-Anteil in %")
    alloy_fe_max_pct: Optional[float] = Field(None, description="Max. Eisengehalt (Verunreinigung)")

    # Elektrochemie
    open_circuit_potential_mv: Optional[float] = Field(None, description="Ruhepotenzial vs. Ag/AgCl in mV")
    closed_circuit_potential_mv: Optional[float] = Field(None, description="Arbeitspotenzial vs. Ag/AgCl in mV")
    current_capacity_ah_per_kg: Optional[float] = Field(None, description="Stromkapazität in Ah/kg")
    current_efficiency_pct: Optional[float] = Field(None, ge=0, le=100, description="Stromausbeute in %")
    consumption_rate_kg_per_a_year: Optional[float] = Field(None, description="Verbrauchsrate in kg/(A·Jahr)")

    # Physische Maße (mm, g)
    length_mm: float = Field(..., ge=10, description="Länge in mm")
    width_mm: float = Field(..., ge=5, description="Breite in mm")
    height_mm: float = Field(..., ge=3, description="Höhe/Dicke in mm")
    weight_g: float = Field(..., ge=10, description="Nettogewicht in g")
    shaft_diameter_mm: Optional[float] = Field(None, description="Für Wellenanoden: passender Wellendurchmesser in mm")
    bolt_pattern: Optional[str] = Field(None, description="Befestigungsmuster, z.B. '2x M8 @ 120mm'")

    # Anwendung
    suitable_water_types: list[WaterType]
    oem_replacement_for: Optional[list[str]] = Field(None, description="OEM-Teilenummern, die ersetzt werden")
    fits_models: Optional[list[str]] = Field(None, description="Kompatible Motor-/Antriebsmodelle")

    # Kosten
    price_eur: Optional[float] = Field(None, ge=0, description="Listenpreis in EUR (ohne MwSt)")
    price_source: Optional[str] = Field(None, description="Quelle und Datum der Preisangabe")

    # Confidence
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.MEASURED)


class AnodeCondition(BaseModel):
    """Zustandsbewertung einer verbauten Opferanode (Inspektion/Foto)."""
    model_config = {"from_attributes": True}

    location: str = Field(..., description="Einbauort: 'hull_starboard_aft', 'shaft_main', 'propeller', etc.")
    anode_type: AnodeType
    anode_material: Optional[AnodeMaterial] = Field(None, description="Falls erkennbar")
    manufacturer: Optional[str] = None
    part_number: Optional[str] = None

    # Zustand
    condition_rating: AnodeConditionRating
    consumption_pct: Optional[float] = Field(None, ge=0, le=100, description="Geschätzter Verbrauch in %")
    remaining_life_months: Optional[float] = Field(None, ge=0, description="Geschätzte Restlebensdauer in Monaten")
    is_electrically_connected: Optional[bool] = Field(None, description="Elektrisch leitend verbunden? (Bonding intakt)")
    is_fouled: Optional[bool] = Field(None, description="Mit Bewuchs bedeckt? (reduziert Wirksamkeit)")
    mounting_condition: Optional[str] = Field(None, description="'secure' / 'loose' / 'missing_bolt' / 'corroded_bolt'")

    # Maße bei Inspektion
    measured_thickness_mm: Optional[float] = Field(None, description="Gemessene Restdicke in mm")
    original_thickness_mm: Optional[float] = Field(None, description="Originaldicke laut Spezifikation in mm")

    # Umgebung
    adjacent_corrosion: Optional[CorrosionSeverity] = Field(None, description="Korrosion an benachbarten Bauteilen")
    adjacent_corrosion_description: Optional[str] = None

    # Bewertung
    score: Optional[float] = Field(None, ge=0, le=100, description="AYDI-Score 0–100")
    recommendation: Optional[str] = Field(None, description="Empfehlung in Deutsch")
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.VISUAL_MEDIUM)
    assessment_source: str = Field(default="visual", description="'visual' / 'measured' / 'reported'")


class BondingSystemAssessment(BaseModel):
    """Bewertung des elektrischen Bonding-Systems (Masseverbindung)."""
    model_config = {"from_attributes": True}

    has_bonding_system: Optional[bool] = Field(None, description="Bonding-System vorhanden?")
    bonding_conductor_type: Optional[str] = Field(None, description="'tinned_copper' / 'bare_copper' / 'wire' / 'strap'")
    bonding_conductor_size_mm2: Optional[float] = Field(None, description="Querschnitt des Bonding-Leiters in mm²")
    components_bonded: Optional[list[str]] = Field(None, description="Verbundene Komponenten")
    components_not_bonded: Optional[list[str]] = Field(None, description="Nicht verbundene Komponenten (Mangel)")
    has_galvanic_isolator: Optional[bool] = Field(None, description="Galvanischer Isolator am Landstromkabel?")
    galvanic_isolator_type: Optional[str] = Field(None, description="'diode' / 'capacitor_coupled' / None")
    has_isolation_transformer: Optional[bool] = Field(None, description="Trenntransformator vorhanden?")
    stray_current_detected: Optional[bool] = Field(None, description="Streustrom erkannt?")
    stray_current_source: Optional[str] = None
    hull_potential_mv: Optional[float] = Field(None, description="Gemessenes Rumpfpotenzial vs. Ag/AgCl in mV")

    score: Optional[float] = Field(None, ge=0, le=100)
    recommendation: Optional[str] = None
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)


class CathodicProtectionAssessment(BaseModel):
    """Gesamtbewertung des kathodischen Schutzsystems einer Yacht."""
    model_config = {"from_attributes": True}

    # Boot-Identifikation
    boat_name: Optional[str] = None
    boat_length_m: float = Field(..., ge=2.5, le=100, description="Bootslänge in m")
    boat_type: str = Field(..., description="'sailboat' / 'motorboat' / 'catamaran' / 'superyacht'")
    hull_material: str = Field(..., description="'grp' / 'aluminum' / 'steel' / 'wood' / 'composite'")
    primary_water_type: WaterType

    # Schutzsystem
    protection_system: ProtectionSystem
    iccp_installed: bool = Field(default=False)
    iccp_functional: Optional[bool] = None
    iccp_manufacturer: Optional[str] = None

    # Anoden-Inventar
    anodes: list[AnodeCondition] = Field(default_factory=list)
    total_anode_count: int = Field(default=0, ge=0)
    depleted_anode_count: int = Field(default=0, ge=0)
    missing_anode_count: int = Field(default=0, ge=0)

    # Bonding
    bonding: Optional[BondingSystemAssessment] = None

    # Gesamtbewertung
    anode_material_correct_for_water: Optional[bool] = Field(None, description="Richtiges Anodenmaterial für Fahrgebiet?")
    anode_coverage_sufficient: Optional[bool] = Field(None, description="Ausreichende Anodenabdeckung?")
    hull_potential_in_range: Optional[bool] = Field(None, description="Rumpfpotenzial im Schutzbereich?")

    # Korrosionsbefunde
    corrosion_findings: Optional[list[dict]] = Field(None, description="Liste der Korrosionsbefunde an geschützten Teilen")
    worst_corrosion_severity: Optional[CorrosionSeverity] = None

    # Score und Empfehlungen
    overall_score: float = Field(..., ge=0, le=100, description="AYDI-Gesamtscore Korrosionsschutz 0–100")
    category_scores: Optional[dict[str, float]] = Field(None, description="Teilscores: anode_condition, bonding, material_match, coverage")
    findings: list[str] = Field(default_factory=list, description="Liste der Befunde in Deutsch")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen in Deutsch")
    estimated_replacement_cost_eur: Optional[float] = Field(None, ge=0, description="Geschätzte Kosten für empfohlene Maßnahmen in EUR")

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
    assessment_date: Optional[str] = Field(None, description="Datum der Bewertung ISO-8601")


class AnodeReplacementCost(BaseModel):
    """Kostenkalkulation für Anodenwechsel."""
    model_config = {"from_attributes": True}

    boat_length_m: float = Field(..., ge=2.5)
    boat_type: str
    water_type: WaterType
    anode_material: AnodeMaterial

    # Material
    anode_count: int = Field(..., ge=1)
    anode_items: Optional[list[dict]] = Field(None, description="[{part_number, description, unit_price_eur, qty}]")
    total_material_cost_eur: float = Field(..., ge=0)

    # Arbeit
    labor_type: str = Field(..., description="'diy' / 'boatyard' / 'diver'")
    labor_hours: Optional[float] = Field(None, ge=0)
    labor_rate_eur_per_hour: Optional[float] = Field(None, ge=0)
    total_labor_cost_eur: float = Field(default=0, ge=0)

    # Zusätzlich
    haul_out_required: bool = Field(default=True)
    haul_out_cost_eur: Optional[float] = Field(None, ge=0, description="Kran-/Slip-Kosten")

    # Gesamt
    total_cost_eur: float = Field(..., ge=0)
    cost_per_year_eur: Optional[float] = Field(None, ge=0, description="Annualisierte Kosten")
    interval_months: int = Field(default=12, ge=3, le=36)

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
```

> **Hinweis:** Alle Modelle verwenden Pydantic v2 mit `model_config = {"from_attributes": True}`. Maße in mm, Scores 0–100, Kosten in EUR.
> Confidence: `measured`

---

## 7. Grundlagen

### 7.1 Galvanische Reihe in Seewasser

Die galvanische Reihe ordnet Metalle nach ihrem elektrochemischen Potenzial in Seewasser. Werden zwei verschiedene Metalle in Seewasser elektrisch verbunden, korrodiert das „unedlere" Metall (negativeres Potenzial) und schützt das „edlere".

**Galvanische Reihe — Marine-relevante Metalle (Potenzial vs. Ag/AgCl in natürlichem Seewasser):**

```
KATHODISCH (edel, geschützt)               Potenzial vs. Ag/AgCl
─────────────────────────────────────────────────────────────────
Titan                                       −50 bis +50 mV
Inconel 625                                 −50 bis −150 mV
Edelstahl 316L (passiv)                     −50 bis −200 mV
Monel 400 (Cu-Ni 67/30)                    −100 bis −200 mV
Kupfer-Nickel 90/10 (CuNi10Fe)             −200 bis −280 mV
Bronze (Phosphor-/Zinn-)                    −250 bis −350 mV
Kupfer                                      −300 bis −370 mV
Messing (CuZn)                              −300 bis −400 mV
Edelstahl 316L (aktiv/Spalt)               −400 bis −550 mV
Zinn                                        −500 bis −600 mV
Blei                                        −500 bis −600 mV
Gusseisen                                   −600 bis −710 mV
Baustahl (Schiffbau)                        −600 bis −710 mV
Aluminium 5086 (Al-Mg marine)              −760 bis −840 mV
Aluminium 6061-T6                           −800 bis −900 mV
Kadmium                                     −700 bis −800 mV
Zink (rein, > 99.99%)                       −980 bis −1.050 mV
Aluminium-Anode (Al-Zn-In)                 −1.050 bis −1.120 mV
Magnesium-Anode (AZ-63)                    −1.500 bis −1.580 mV
─────────────────────────────────────────────────────────────────
ANODISCH (unedel, korrodiert)
```

### 7.2 Galvanische Korrosion — Wirkmechanismus

Drei Bedingungen müssen gleichzeitig erfüllt sein:

1. **Zwei verschiedene Metalle** mit unterschiedlichem Potenzial
2. **Elektrisch leitende Verbindung** (direkt oder über Bonding-Leiter)
3. **Gemeinsamer Elektrolyt** (Seewasser, Brackwasser, Süßwasser)

Fehlt eine Bedingung, findet keine galvanische Korrosion statt. Daraus leiten sich drei Schutzstrategien ab:

| Strategie | Maßnahme | Praxis-Beispiel |
|-----------|----------|----------------|
| Material-Wahl | Nur kompatible Metalle | Keine Edelstahl-Schrauben in Aluminium ohne Isolation |
| Elektrische Trennung | Isolierbuchsen, Unterlegscheiben | Nylon-Isolierbuchse zwischen Edelstahl-Beschlag und Al-Mast |
| Opferanode | Drittes, noch unedleres Metall | Zinkanode am Edelstahl-Propeller |

**Flächenverhältnis-Regel (Area Ratio):**
Die Korrosionsrate am anodischen Metall steigt mit dem Flächenverhältnis Kathode:Anode. Ein großer Edelstahl-Propeller mit einem kleinen Aluminium-Bolzen = katastrophale Korrosion am Bolzen. Umgekehrt: großer Aluminium-Rumpf mit kleinem Edelstahl-Beschlag = vernachlässigbare Korrosion.

**Kritische Kombinationen auf Yachten:**

| Kombination | Potenzialdifferenz | Risiko | Typisches Schadensbild |
|-------------|-------------------|--------|----------------------|
| Edelstahl + Aluminium | 600–1.000 mV | KRITISCH | Lochfraß im Aluminium, Rumpf-Durchbruch bei Al-Booten |
| Bronze + Aluminium | 500–800 mV | KRITISCH | Lochfraß im Aluminium nahe Borddurchlass |
| Edelstahl + Stahl | 300–500 mV | HOCH | Großflächige Stahlkorrosion nahe Edelstahlbeschlägen |
| Bronze + Stahl | 200–400 mV | MITTEL | Gleichmäßige Stahlabnahme |
| Kupfer-Antifouling + Aluminium | 500–700 mV | KRITISCH | Aluminium-Rumpf löst sich unter Kupfer-AF auf |
| Edelstahl 316 + Bronze | 100–200 mV | GERING | Normalerweise tolerierbar |

### 7.3 Anodenmaterialien im Detail

#### 7.3.1 Zink-Anoden (MIL-A-18001K)

**Legierungszusammensetzung nach MIL-A-18001K:**

| Element | Min. (%) | Max. (%) | Zweck |
|---------|---------|---------|-------|
| Zink (Zn) | Balance | Balance | Grundwerkstoff |
| Aluminium (Al) | 0,10 | 0,50 | Kornfeinung |
| Cadmium (Cd) | 0,025 | 0,07 | Aktivierung, gleichmäßige Auflösung |
| Eisen (Fe) | — | 0,005 | Verunreinigung (muss minimiert werden) |
| Blei (Pb) | — | 0,006 | Verunreinigung |
| Kupfer (Cu) | — | 0,005 | Verunreinigung (Polwechsel-Risiko!) |
| Silizium (Si) | — | 0,125 | Verunreinigung |

**Elektrochemische Eigenschaften:**

| Parameter | Wert | Messbedingung |
|-----------|------|---------------|
| Ruhepotenzial | −1.030 bis −1.055 mV vs. Ag/AgCl | Seewasser 18°C, 35‰ |
| Arbeitspotenzial | −1.000 bis −1.050 mV vs. Ag/AgCl | Unter Schutzstromlast |
| Stromkapazität | 780 Ah/kg | NACE TM0190 |
| Stromausbeute | ≥ 95% | Unter optimalen Bedingungen |
| Verbrauchsrate | 11,2 kg/(A·Jahr) | Theoretisch |
| Dichte | 7,1 g/cm³ | — |

**Vorteile von Zink:**
- Jahrzehntelange Bewährung, „Industriestandard" seit 1950er Jahren
- Sehr gleichmäßige Auflösung (keine Passivierung in Salzwasser)
- Niedriger Preis pro kg (8–12 EUR/kg)
- Keine Überprotektion möglich (Potenzial zu „mild" für Schäden)
- Einfache visuelle Beurteilung des Verbrauchsgrads

**Nachteile von Zink:**
- Enthält Cadmium (REACH-Verordnung → zukünftiges Verbot möglich)
- Hohe Dichte → schwere Anoden
- Passiviert in Brackwasser < 10.000 µS/cm und Süßwasser
- Niedrigere Stromkapazität pro kg als Aluminium (780 vs. 2.600 Ah/kg)
- Temperaturempfindlich: > 50°C Oberflächentemperatur → Passivierung (Motoranoden!)

> **AYDI-Warnung:** Zinkanoden an Motorblöcken, Wärmetauschern oder Auspuffkrümmern — die Oberfläche kann lokal > 50°C erreichen. Hier Aluminium-Anoden verwenden.

#### 7.3.2 Aluminium-Anoden (MIL-DTL-24779C)

**Legierungszusammensetzung nach MIL-DTL-24779C (Typ II, Indium-aktiviert):**

| Element | Min. (%) | Max. (%) | Zweck |
|---------|---------|---------|-------|
| Aluminium (Al) | Balance | Balance | Grundwerkstoff |
| Zink (Zn) | 3,0 | 6,0 | Potenzialeinstellung |
| Indium (In) | 0,01 | 0,03 | Aktivierung (verhindert Passivierung) |
| Silizium (Si) | — | 0,12 | Verunreinigung |
| Eisen (Fe) | — | 0,13 | Verunreinigung |
| Kupfer (Cu) | — | 0,006 | Verunreinigung (kritisch!) |
| Kadmium (Cd) | — | 0,002 | Verunreinigung |

**Elektrochemische Eigenschaften:**

| Parameter | Wert | Messbedingung |
|-----------|------|---------------|
| Ruhepotenzial | −1.080 bis −1.120 mV vs. Ag/AgCl | Seewasser 18°C, 35‰ |
| Arbeitspotenzial | −1.050 bis −1.100 mV vs. Ag/AgCl | Unter Schutzstromlast |
| Stromkapazität | 2.600–2.830 Ah/kg | DNV-RP-B401, MIL-DTL-24779C |
| Stromausbeute | ≥ 90% | Unter optimalen Bedingungen |
| Verbrauchsrate | 3,4 kg/(A·Jahr) | Theoretisch |
| Dichte | 2,7 g/cm³ | — |

**Vorteile von Aluminium:**
- 3,3× höhere Stromkapazität pro kg als Zink
- 2,6× leichter als Zink bei gleicher Schutzleistung
- Cadmium-frei (RoHS/REACH-konform)
- Funktioniert in Salzwasser UND Brackwasser (bis ~3.000 µS/cm)
- Höheres Treibpotenzial → besserer Schutz bei schlechter Bonding-Verbindung
- Keine Temperaturprobleme bis 80°C → ideal für Motoranoden

**Nachteile von Aluminium:**
- Etwas höherer Preis pro kg (12–18 EUR/kg, aber günstiger pro Ah)
- Mögliche Überprotektion bei sehr kleinen Booten → Beschichtungsschäden
- Visuelle Verbrauchsbeurteilung schwieriger (rauhes Auflösungsbild)
- Einige traditionelle Werftbetriebe kennen/akzeptieren nur Zink

> **AYDI-Empfehlung:** Aluminium ist für neue Installationen in Salzwasser die bevorzugte Wahl. Leichter, wirtschaftlicher, umweltfreundlicher, und funktioniert auch in Brackwasser. Der Preisunterschied pro kg wird durch die 3× höhere Kapazität mehr als kompensiert.

#### 7.3.3 Magnesium-Anoden

**Legierungszusammensetzung (ASTM B843 Typ AZ-63):**

| Element | Min. (%) | Max. (%) | Zweck |
|---------|---------|---------|-------|
| Magnesium (Mg) | Balance | Balance | Grundwerkstoff |
| Aluminium (Al) | 5,3 | 6,7 | Kornfeinung, mechanische Festigkeit |
| Zink (Zn) | 2,5 | 3,5 | Potenzialeinstellung |
| Mangan (Mn) | 0,15 | — | Kornfeinung |
| Eisen (Fe) | — | 0,003 | Verunreinigung (extrem kritisch!) |
| Kupfer (Cu) | — | 0,02 | Verunreinigung |
| Nickel (Ni) | — | 0,002 | Verunreinigung |

**Elektrochemische Eigenschaften:**

| Parameter | Wert | Messbedingung |
|-----------|------|---------------|
| Ruhepotenzial | −1.500 bis −1.580 mV vs. Ag/AgCl | Süßwasser |
| Arbeitspotenzial | −1.450 bis −1.550 mV vs. Ag/AgCl | Unter Last |
| Stromkapazität (theoretisch) | 2.205 Ah/kg | Faraday (Mg→Mg²⁺+2 e⁻) |
| Stromausbeute | 50–55% | Hohe Selbstkorrosion! |
| Effektive Kapazität | 1.100–1.230 Ah/kg | Praxis (AZ-63, 50–55% Ausbeute) |
| Verbrauchsrate | 8,0 kg/(A·Jahr) | Einschl. Selbstkorrosion |
| Dichte | 1,74 g/cm³ | — |

> ✅ Aufgeloest (Audit): Theoretische Mg-Stromkapazität = **2.205 Ah/kg** (Faraday-Gesetz, Mg→Mg²⁺+2 e⁻: 2·96485 / 0,024305 / 3600); praktische/effektive Kapazität für AZ-63 = **1.100–1.230 Ah/kg** bei 50–55 % Stromausbeute. Der zuvor genannte Wert „550–675 Ah/kg" beruhte auf einer Einheitenverwechslung (550 Ah/**lb** ≈ 1.213 Ah/kg). Intern bestätigt durch Verbrauchsrate 8,0 kg/(A·Jahr) = 8760/8,0 = 1.095 Ah/kg. Confidence wieder auf `measured`. — Quelle: Faraday-Gesetz; CP-/Hersteller-Daten AZ-63 (Standard-H1: 1.100–1.188 Ah/kg, 50–54 % Ausbeute).

**Vorteile von Magnesium:**
- Einziges zuverlässiges Material für Süßwasser (< 2.000 µS/cm)
- Hohes Treibpotenzial (−1.500 mV) — aktiviert auch bei geringer Leitfähigkeit
- Sehr geringe Dichte (1,74 g/cm³)

**Nachteile von Magnesium:**
- ~50% Selbstkorrosion → die Hälfte der Kapazität geht verloren
- In Salzwasser VERBOTEN: löst sich explosionsartig auf, massive Überprotektion
- Kann bei Aluminiumrümpfen in Salzwasser zur Alkaliversprödung führen
- Kürzere Standzeit als Zn/Al wegen Selbstkorrosion
- Feuergefahr bei Bearbeitung (Magnesiumspäne sind selbstentzündlich)

> **AYDI-Kritische Warnung:** Magnesium-Anoden NIEMALS in Salzwasser einsetzen. Überprotektion kann Aluminium-Rümpfe beschädigen und Beschichtungen von GFK-Rümpfen ablösen. Nur für Süßwasser und sehr niedrige Brackwasser-Bereiche.

### 7.4 Verbrauchsraten und 50%-Regel

#### 7.4.1 Die 50%-Regel

Die wichtigste Wartungsregel für Opferanoden: **Wechsel bei 50% Verbrauch.** Nicht bei 80%, nicht bei „sieht noch gut aus", sondern bei 50%.

**Begründung:**
- Die Schutzleistung nimmt nicht linear ab, sondern fällt nach 50% steil ab
- Die verbleibende Anode kann nicht mehr genügend Strom liefern
- Die Kontaktfläche zum geschützten Bauteil wird kleiner → höherer Übergangswiderstand
- Restmaterial kann abbrechen → plötzlicher Totalverlust

**Visuelle 50%-Erkennung:**

| Anodentyp | 50%-Kriterium |
|-----------|---------------|
| Flachanode (Rumpf) | Originaldicke halbiert, Befestigungsbolzen sichtbar |
| Wellenanoden (Collar) | Innenfläche deutlich ausgespült, Spalt zur Welle > 3 mm |
| Propelleranoden | Originalkontur nicht mehr erkennbar, Schraubenlöcher ausgewaschen |
| Saildrive-Ring | Ringquerschnitt halbiert, Stoßstelle deutlich breiter |

#### 7.4.2 Verbrauchsraten in der Praxis

| Szenario | Anodenverbrauch | Typisches Intervall |
|----------|----------------|-------------------|
| Segelboot 10 m, Salzwasser, saisonaler Betrieb | 0,3–0,5 kg/Jahr | Alle 18–24 Monate |
| Segelboot 10 m, Salzwasser, Dauerlieger | 0,8–1,5 kg/Jahr | Alle 10–14 Monate |
| Motorboot 12 m, Salzwasser, aktiver Einsatz | 1,0–2,0 kg/Jahr | Alle 10–12 Monate |
| Segelboot 12 m, Ostsee (Brackwasser) | 0,2–0,4 kg/Jahr (Al) | Alle 18–24 Monate |
| Yacht 18 m, Mittelmeer, Dauerlieger | 2,0–4,0 kg/Jahr | Alle 8–12 Monate |
| Yacht 18 m, Karibik | 3,0–6,0 kg/Jahr | Alle 6–10 Monate |

**Faktoren, die den Verbrauch beschleunigen:**
1. Höhere Wassertemperatur (+25–40% pro 10°C)
2. Höherer Salzgehalt
3. Streuströme (Landstrom, benachbarte Boote)
4. Großes Kathodenflächen-Verhältnis (viel Edelstahl/Bronze)
5. Defektes Antifouling (freiliegende Unterwasserfläche = mehr zu schützende Fläche)
6. Geschwindigkeit / Strömung (beschleunigt Elektrolyttransport)

### 7.5 Elektrisches Bonding-System

#### 7.5.1 Zweck des Bondings

Das Bonding-System (Masseverbindung) verbindet alle metallischen Unterwasserkomponenten elektrisch miteinander und mit den Opferanoden. Ohne Bonding schützt eine Anode nur das direkt angrenzende Metall.

**Zu verbindende Komponenten:**

| Komponente | Bonding-Priorität | Begründung |
|-----------|-------------------|-----------|
| Propellerwelle | KRITISCH | Größte bewegliche Unterwasserkomponente |
| Ruderschaft | KRITISCH | Korrosion → Ruderversagen |
| Motor-Masseband | KRITISCH | Motorblock als Korrosionskathode |
| Borddurchlässe (Bronze/Edelstahl) | HOCH | Direkt unter der Wasserlinie |
| Kiel (Blei/Gusseisen) | HOCH | Große Fläche, hoher Korrosionsstrom |
| Bug-/Heckstrahlruder | HOCH | Edelstahlgehäuse + Propeller |
| Tankbeschläge (Diesel/Wasser) | MITTEL | Falls Metalltanks |
| Stevenrohr | HOCH | Lagersitz, schwer zugänglich |

#### 7.5.2 Bonding-Leiter-Spezifikation nach ABYC E-2

| Bootsgröße | Min. Bonding-Leiter | Empfohlen | Material |
|------------|-------------------|-----------|---------|
| < 8 m | 6 mm² (AWG 10) | 10 mm² (AWG 8) | Verzinntes Kupfer |
| 8–15 m | 10 mm² (AWG 8) | 16 mm² (AWG 6) | Verzinntes Kupfer |
| 15–25 m | 16 mm² (AWG 6) | 25 mm² (AWG 4) | Verzinntes Kupfer |
| > 25 m | 25 mm² (AWG 4) | 35 mm² (AWG 2) | Verzinntes Kupfer oder Kupferband |

**Verbindungstechnik:**
- Crimpverbindungen mit marine-grade Ringkabelschuhen (verzinnt)
- Schraubverbindungen mit Kontaktfett (Tef-Gel oder Duralac)
- NIEMALS gelötete Verbindungen im Bonding-System (Lötzinn korrodiert)
- Alle Verbindungen zugänglich für Inspektion
- Messung des Verbindungswiderstands: < 1 Ohm pro Verbindung

### 7.6 Streustromkorrosion

#### 7.6.1 Mechanismus

Streustromkorrosion (Stray Current Corrosion) entsteht durch externe Gleichströme, die unbeabsichtigt durch den Rumpf und das Seewasser fließen. Die Korrosionsrate bei Streustrom ist 10–100× höher als bei galvanischer Korrosion.

**Typische Streustromquellen auf Yachten:**

| Quelle | Risiko | Erkennungsmerkmal |
|--------|--------|-------------------|
| Fehlerhafte Landstromverkabelung | SEHR HOCH | Asymmetrische Anodenauflösung, nur auf einer Bootsseite |
| Defekte Verkabelung am eigenen Boot | HOCH | Erhöhter Anodenverbrauch seit bestimmtem Zeitpunkt |
| Nachbarboot mit defekter Elektrik | HOCH | Problem tritt nur an bestimmtem Liegeplatz auf |
| Hafeninfrastruktur (defekte Erdung) | MITTEL | Mehrere Boote im gleichen Hafenbecken betroffen |
| AC-Streuströme (Landstrom) | HOCH | Kriechender DC-Anteil durch Korrosion an AC-Leitung |

#### 7.6.2 Erkennung und Messung

**Potenzial-Messung (einfachste Methode):**
1. Referenzelektrode (Ag/AgCl oder Zink) ins Wasser neben dem Boot
2. Multimeter zwischen Referenzelektrode und Rumpf-Bonding
3. Normales Ruhepotenzial: −800 bis −1.050 mV (mit Zinkanoden)
4. Streustromindikation: Potenzial springt oder wird positiver als −600 mV

**Clamp-Meter-Messung:**
- DC-Stromzange am Landstromkabel (Schutzleiter / PE)
- Normaler Wert: < 30 mA
- Bedenklich: 30–100 mA
- Gefährlich: > 100 mA → sofort abstecken und Fehler suchen

### 7.7 Galvanische Isolatoren

#### 7.7.1 Funktionsprinzip

Ein galvanischer Isolator (Galvanic Isolator) wird in den Schutzleiter (PE/Grounding) des Landstromkabels eingebaut. Er blockiert galvanische Gleichströme (< 1,4 V), lässt aber Fehlerstrom (230 V AC-Leck) zum Fehlerstromschutzschalter durch.

**Typen:**

| Typ | Aufbau | Vorteile | Nachteile | Preis (EUR) |
|-----|--------|----------|-----------|-------------|
| Dioden-Isolator | 2 antiparallele Silizium-Dioden | Einfach, günstig | Nur 0,6 V Sperrspannung | 80–200 |
| Kapazitiv gekoppelt | Kondensator + Dioden-Backup | Höhere Sperrspannung, AC-transparent | Teurer, komplexer | 200–500 |
| Hybrid (Fail-Safe) | Kapazitiv + Monitor + Alarm | Höchste Sicherheit, ISO 13297 | Am teuersten | 350–700 |

**Hersteller galvanischer Isolatoren:**

| Hersteller | Modell | Typ | Strom (A) | Preis (EUR) | Zulassung |
|-----------|--------|-----|-----------|-------------|-----------|
| **ProMariner** (USA) | ProSafe FS30 | Fail-Safe | 30 | 180–250 | ABYC A-28 |
| **ProMariner** | ProSafe FS60 | Fail-Safe | 60 | 280–380 | ABYC A-28 |
| **Mastervolt** (NL) | Galvanic Isolator GI | Kapazitiv | 32/64 | 250–400 | CE |
| **Victron Energy** (NL) | Galvanic Isolator VDI-16/32/64 | Dioden | 16/32/64 | 90–200 | CE |
| **Sterling Power** (UK) | ProSplit GI-1232 | Dioden | 32 | 120–180 | ABYC, CE |
| **Newmar** (USA) | GI-30 | Fail-Safe | 30 | 200–300 | ABYC A-28 |
| **Philippi** (DE) | GI 50 | Kapazitiv | 50 | 320–450 | CE, GL |
| **Dairyland** (USA) | Marine Series | Kapazitiv | 30/60 | 250–400 | ABYC |

### 7.8 Isolation Transformer (Trenntransformator)

Der Trenntransformator bietet den höchsten Schutz gegen galvanische Korrosion über den Landstrom, da er die galvanische Verbindung zum Landnetz vollständig unterbricht.

**Vorteile gegenüber galvanischem Isolator:**
- Vollständige galvanische Trennung (kein DC-Strom möglich)
- Schützt auch gegen AC-Streustrom
- Eigene Borderde unabhängig von Hafeninfrastruktur
- Ermöglicht Spannungsanpassung (z.B. 220V Hafen → 230V Bord)

**Nachteile:**
- Teuer: 800–5.000 EUR je nach Leistung
- Schwer: 10–50 kg
- Platzbedarf
- Eigenverbrauch (3–5% Verlustleistung)

**Hersteller:**

| Hersteller | Modell | Leistung (VA) | Gewicht (kg) | Preis (EUR) |
|-----------|--------|---------------|-------------|-------------|
| **Mastervolt** | IVET 3600 | 3.600 | 18 | 1.800–2.400 |
| **Victron Energy** | Isolation Transformer 3600 | 3.600 | 16 | 1.200–1.800 |
| **Victron Energy** | Isolation Transformer 7000 | 7.000 | 32 | 2.200–3.000 |
| **Mastervolt** | IVET 7000 | 7.000 | 35 | 2.800–3.800 |
| **Philippi** | TRS 3600 | 3.600 | 20 | 2.000–2.800 |
| **Charles Industries** (USA) | ISO-Boost 30A | 3.300 | 14 | 1.000–1.500 |

> **AYDI-Empfehlung nach Bootsgröße:**
> - < 12 m: Galvanischer Isolator (Dioden-Typ) ausreichend
> - 12–18 m: Galvanischer Isolator (kapazitiv oder Fail-Safe)
> - > 18 m oder Dauerwasserlieger: Trenntransformator
> - Aluminiumrumpf: Trenntransformator **obligatorisch**

---

## 8. Hersteller — Vollständige Übersicht

### 8.1 Martyr Anodes (UK/USA) — Marktführer

**Firmenprofil:**
- Gegründet: 1987
- Hauptsitz: Hampshire, UK / Florida, USA
- Marktsegment: Freizeitschifffahrt, kommerziell, Offshore
- Zertifizierung: MIL-A-18001K (Zn), MIL-DTL-24779C (Al), Lloyd's Register
- Sortiment: > 2.000 Artikelnummern, größtes marines Anodensortiment weltweit
- Vertrieb: Global über Fachhändler, keine Direktverkäufe

**Produktlinien:**

| Linie | Material | Kennzeichnung | Einsatzgebiet |
|-------|----------|---------------|---------------|
| **CM-Serie** | Zink (Zn) | CM = Corrosion Martyr | Salzwasser Standard |
| **CMA-Serie** | Aluminium (Al) | CMA = Corrosion Martyr Aluminium | Salzwasser + Brackwasser |
| **CMM-Serie** | Magnesium (Mg) | CMM = Corrosion Martyr Magnesium | Süßwasser |

**Ausgewählte Rumpfanoden (Bolt-on):**

| Artikelnr. | Material | Maße (mm) L×B×H | Gewicht (g) | Passend für | Preis (EUR) |
|-----------|----------|----------------|-------------|------------|-------------|
| CM-1 | Zn | 155×75×25 | 1.000 | Rumpf 6–9 m | 12–16 |
| CM-2 | Zn | 200×100×30 | 2.200 | Rumpf 8–12 m | 18–24 |
| CM-3 | Zn | 250×100×32 | 3.200 | Rumpf 10–14 m | 24–32 |
| CM-5 | Zn | 300×125×38 | 5.400 | Rumpf 12–18 m | 35–48 |
| CM-10 | Zn | 350×150×45 | 10.000 | Rumpf 18–25 m | 65–85 |
| CMA-1 | Al | 155×75×30 | 450 | Rumpf 6–9 m | 14–18 |
| CMA-2 | Al | 200×100×35 | 900 | Rumpf 8–12 m | 20–28 |
| CMA-3 | Al | 250×100×38 | 1.300 | Rumpf 10–14 m | 28–36 |
| CMA-5 | Al | 300×125×45 | 2.200 | Rumpf 12–18 m | 40–55 |

**Ausgewählte Wellenanoden (Collar / Donut):**

| Artikelnr. | Material | Wellendurchmesser (mm) | Gewicht (g) | Preis (EUR) |
|-----------|----------|----------------------|-------------|-------------|
| CMX-01 | Zn | 19 (3/4") | 200 | 12–16 |
| CMX-02 | Zn | 22 (7/8") | 280 | 14–18 |
| CMX-03 | Zn | 25 (1") | 370 | 16–22 |
| CMX-04 | Zn | 30 (1-1/4") | 530 | 18–25 |
| CMX-05 | Zn | 35 (1-3/8") | 700 | 22–30 |
| CMX-06 | Zn | 40 (1-1/2") | 930 | 25–34 |
| CMX-07 | Zn | 45 (1-3/4") | 1.150 | 28–38 |
| CMX-08 | Zn | 50 (2") | 1.400 | 32–42 |
| CMX-60A | Al | 25 (1") | 150 | 18–24 |
| CMX-61A | Al | 30 (1-1/4") | 210 | 20–28 |
| CMX-62A | Al | 35 (1-3/8") | 280 | 24–32 |
| CMX-63A | Al | 40 (1-1/2") | 370 | 26–36 |
| CMX-64A | Al | 45 (1-3/4") | 460 | 30–40 |
| CMX-65A | Al | 50 (2") | 560 | 34–46 |

**OEM-Ersatzanoden (Auswahl):**

| Artikelnr. | Ersatz für OEM | Motor/Antrieb | Material | Preis (EUR) |
|-----------|---------------|---------------|----------|-------------|
| CM-821630Z | Mercury 821630Q1 | Alpha One Gen II | Zn | 12–18 |
| CM-821631Z | Mercury 821631Q1 | Bravo One/Two/Three | Zn | 14–20 |
| CM-55989Z | Mercury 55989A | Verado Getriebegehäuse | Zn | 10–15 |
| CMV-18-6Z | Volvo 3888305 | 120S/130S Saildrive Ring | Zn | 25–35 |
| CMV-20Z | Volvo 3858399 | Ruderblatt, DP-Antrieb | Zn | 22–30 |
| CMV-23AZ | Volvo 3855411 | 290/SX Outdrive | Zn | 15–22 |
| CMY-1Z | Yanmar 27210-200300 | SD20/SD25/SD30 Saildrive | Zn | 20–28 |
| CMY-2Z | Yanmar 196420-02652 | Motorblock-Stift | Zn | 6–10 |
| CMV-18-6A | Volvo 3888305 | 120S/130S Saildrive Ring | Al | 28–38 |

### 8.2 Tecnoseal (Italien) — Premium Marine Anodes

**Firmenprofil:**
- Gegründet: 1964
- Hauptsitz: Castagnaro (Verona), Italien
- Marktsegment: Premium-Segment Freizeitschifffahrt, kommerziell, Superyacht
- Zertifizierung: MIL-A-18001K, MIL-DTL-24779C, DNV-GL, RINA, Bureau Veritas
- Spezialität: OEM-Zulieferer für viele europäische Werften
- Besonderheit: ISO 9001:2015-zertifizierte Produktion, lückenlose Chargenrückverfolgung

**Produktlinien:**

| Linie | Präfix | Material | Besonderheit |
|-------|--------|----------|-------------|
| **Standard** | 00xxx | Zink | Größtes OEM-Sortiment in Europa |
| **Aluminium** | 01xxx | Aluminium | Identische Formen wie Zink-Serie |
| **Magnesium** | 02xxx | Magnesium | Süßwasser-Sortiment |
| **Superyacht** | SY-xxx | Zn/Al | Spezialformen für > 25 m |

**Ausgewählte Rumpfanoden:**

| Artikelnr. | Material | Maße (mm) L×B×H | Gewicht (g) | Preis (EUR) |
|-----------|----------|----------------|-------------|-------------|
| 00100 | Zn | 110×65×20 | 520 | 8–12 |
| 00101 | Zn | 155×75×25 | 1.050 | 14–18 |
| 00102 | Zn | 200×100×30 | 2.300 | 20–26 |
| 00103 | Zn | 250×100×32 | 3.400 | 28–36 |
| 00104 | Zn | 300×125×38 | 5.600 | 38–50 |
| 00105 | Zn | 370×150×45 | 10.500 | 70–90 |
| 01100 | Al | 110×65×24 | 210 | 10–14 |
| 01101 | Al | 155×75×30 | 420 | 16–22 |
| 01102 | Al | 200×100×35 | 940 | 24–32 |
| 01103 | Al | 250×100×38 | 1.350 | 32–42 |

**OEM-Zuordnung (Tecnoseal → Motorhersteller):**

| Tecnoseal | OEM-Teilenr. | Motor/Antrieb | Typ |
|-----------|-------------|---------------|-----|
| 00702 | Volvo 3858399 | DP-Ruderblatt | Zn |
| 00703 | Volvo 3855411 | 290/SX-Arm | Zn |
| 00706 | Volvo 3888305 | Saildrive 120S/130S Ring | Zn |
| 00801 | Mercury 97-821630Q1 | Alpha One Gen II | Zn |
| 00802 | Mercury 97-821631Q1 | Bravo I/II/III | Zn |
| 00901 | Yanmar 27210-200300 | SD20/SD25 Saildrive | Zn |
| 00902 | Yanmar 196420-02652 | Motorblock Pencil | Zn |

### 8.3 Camp / Zineti (Italien)

**Firmenprofil:**
- Gegründet: 1978
- Hauptsitz: Brescia, Italien
- Marktsegment: Preisbewusster Qualitätsanbieter
- Zertifizierung: MIL-A-18001K, MIL-DTL-24779C
- Besonderheit: Sehr breites OEM-Sortiment, gutes Preis-Leistungs-Verhältnis
- Vertrieb: Europa-weit über Fachhändler, stark in Italien, Frankreich, Spanien

**Ausgewählte Produkte:**

| Artikelnr. | Typ | Material | Passt für | Maße (mm) | Gewicht (g) | Preis (EUR) |
|-----------|-----|----------|----------|----------|-------------|-------------|
| 70-1 | Rumpf | Zn | Universal | 155×75×25 | 1.000 | 10–14 |
| 70-2 | Rumpf | Zn | Universal | 200×100×30 | 2.200 | 16–22 |
| 70-3 | Rumpf | Zn | Universal | 250×100×32 | 3.300 | 22–30 |
| 70-S25 | Welle | Zn | ∅25 mm | Collar | 350 | 14–18 |
| 70-S30 | Welle | Zn | ∅30 mm | Collar | 500 | 16–22 |
| 70-S35 | Welle | Zn | ∅35 mm | Collar | 680 | 18–24 |
| 70-VSDR | Saildrive | Zn | Volvo 120S/130S | Ring | 650 | 22–30 |
| 70-YSDR | Saildrive | Zn | Yanmar SD20/SD25 | Ring | 600 | 18–26 |
| 70-MA1 | Alpha | Zn | MerCruiser Alpha I/II | Kit | 850 | 35–48 |
| 70-MB1 | Bravo | Zn | MerCruiser Bravo I/II/III | Kit | 1.200 | 55–75 |

### 8.4 Canada Metal Pacific (CMP)

**Firmenprofil:**
- Gegründet: 1960
- Hauptsitz: Surrey, British Columbia, Kanada
- Marktsegment: Nordamerika-Marktführer, zunehmend Europa
- Zertifizierung: MIL-A-18001K, MIL-DTL-24779C, ABS, DNV-GL
- Besonderheit: Eigene Gießerei, vollständige Prozesskontrolle, Militärzulieferer
- Sortiment: > 1.500 Artikelnummern inkl. Spezialanoden

**Produktlinien:**

| Linie | Kennzeichen | Material | Besonderheit |
|-------|-------------|----------|-------------|
| **ZHC-Serie** | ZHC-xxx | Zink | Hull-Anoden, Premium-Qualität |
| **AHC-Serie** | AHC-xxx | Aluminium | Hull-Anoden |
| **ZSC-Serie** | ZSC-xxx | Zink | Shaft Collars |
| **ASC-Serie** | ASC-xxx | Aluminium | Shaft Collars |
| **?"P"-Serie** | ZPC-xxx / APC-xxx | Zn/Al | Propeller-Anoden |
| **OEM-Kits** | MRC-xxx | Zn/Al | Motor/Antrieb-Kits |

**Ausgewählte Rumpfanoden:**

| Artikelnr. | Material | Maße (mm) L×B×H | Gewicht (g) | Preis (EUR) |
|-----------|----------|----------------|-------------|-------------|
| ZHC-1 | Zn | 155×75×25 | 1.050 | 14–18 |
| ZHC-2 | Zn | 200×100×30 | 2.300 | 20–26 |
| ZHC-3 | Zn | 250×100×32 | 3.400 | 26–34 |
| ZHC-5 | Zn | 300×125×38 | 5.500 | 38–48 |
| ZHC-10 | Zn | 350×150×50 | 10.800 | 70–90 |
| AHC-1 | Al | 155×75×30 | 440 | 16–22 |
| AHC-2 | Al | 200×100×35 | 950 | 22–30 |
| AHC-3 | Al | 250×100×40 | 1.400 | 30–40 |
| AHC-5 | Al | 300×125×48 | 2.300 | 42–56 |

### 8.5 Performance Metals (USA)

**Firmenprofil:**
- Hauptsitz: Three Rivers, Michigan, USA
- Marktsegment: Spezialist für Aluminium-Anoden
- Zertifizierung: MIL-DTL-24779C
- Besonderheit: Pionier und Technologieführer für marine Aluminium-Anoden
- Vertrieb: Nordamerika, zunehmend Europa via ASAP Supplies

**Alleinstellungsmerkmal:** Performance Metals gilt als der Hersteller mit den konsequent höchsten Stromkapazitätswerten bei Al-Anoden (>2.700 Ah/kg in unabhängigen Tests). Die Legierungsüberwachung ist strenger als MIL-DTL-24779C vorschreibt.

**Ausgewählte Produkte:**

| Artikelnr. | Typ | Maße (mm) | Gewicht (g) | Passend für | Preis (EUR) |
|-----------|-----|----------|-------------|------------|-------------|
| PM-H1 | Rumpf | 155×75×30 | 430 | Universal 6–9 m | 16–22 |
| PM-H2 | Rumpf | 200×100×35 | 920 | Universal 8–12 m | 24–32 |
| PM-H3 | Rumpf | 250×100×40 | 1.350 | Universal 10–14 m | 32–42 |
| PM-S25 | Welle | Collar ∅25 mm | 140 | Welle 25 mm | 18–24 |
| PM-S30 | Welle | Collar ∅30 mm | 200 | Welle 30 mm | 20–28 |
| PM-S35 | Welle | Collar ∅35 mm | 270 | Welle 35 mm | 24–32 |
| PM-S40 | Welle | Collar ∅40 mm | 350 | Welle 40 mm | 26–36 |
| PM-S50 | Welle | Collar ∅50 mm | 540 | Welle 50 mm | 32–44 |

### 8.6 MG Duff (UK)

**Firmenprofil:**
- Gegründet: 1970er Jahre
- Hauptsitz: Chichester, West Sussex, UK
- Marktsegment: UK-Marktführer, starke Position in Nordeuropa
- Zertifizierung: MIL-A-18001K, MIL-DTL-24779C, Lloyd's Register
- Besonderheit: Langjährige Erfahrung mit britischen Yachten, gute OEM-Abdeckung für UK-Motoren
- Vertrieb: UK, Irland, Skandinavien, Australien

**Produktlinien:**

| Linie | Kennzeichen | Material | Besonderheit |
|-------|-------------|----------|-------------|
| **ZD-Serie** | ZD-xx | Zink | Disc-/Flachanoden für Rumpf |
| **AD-Serie** | AD-xx | Aluminium | Disc-/Flachanoden |
| **MD-Serie** | MD-xx | Magnesium | Süßwasser-Anoden |
| **ZSSC-Serie** | ZSSC-xx | Zink | Shaft Collar |
| **ASSC-Serie** | ASSC-xx | Aluminium | Shaft Collar |
| **CMDV-Serie** | CMDV-xx | Zn/Al | Volvo-OEM-Ersatz |
| **CMDY-Serie** | CMDY-xx | Zn/Al | Yanmar-OEM-Ersatz |

**Ausgewählte Produkte:**

| Artikelnr. | Typ | Material | Maße/Passend | Gewicht (g) | Preis (GBP/EUR) |
|-----------|-----|----------|-------------|-------------|-----------------|
| ZD-52 | Rumpf Bolt-on | Zn | 200×90×28 | 2.000 | £14 / 17 EUR |
| ZD-54 | Rumpf Bolt-on | Zn | 250×100×30 | 3.200 | £22 / 26 EUR |
| ZD-56 | Rumpf Bolt-on | Zn | 300×120×38 | 5.200 | £32 / 38 EUR |
| AD-52 | Rumpf Bolt-on | Al | 200×90×33 | 820 | £16 / 19 EUR |
| AD-54 | Rumpf Bolt-on | Al | 250×100×35 | 1.300 | £25 / 30 EUR |
| ZSSC-25 | Welle Collar | Zn | ∅25 mm | 340 | £12 / 14 EUR |
| ZSSC-30 | Welle Collar | Zn | ∅30 mm | 490 | £14 / 17 EUR |
| ZSSC-35 | Welle Collar | Zn | ∅35 mm | 660 | £16 / 19 EUR |
| CMDV-120 | Saildrive Ring | Zn | Volvo 120S/130S | 640 | £20 / 24 EUR |

### 8.7 Anode Engineering (Australien)

**Firmenprofil:**
- Hauptsitz: Melbourne, Australien
- Marktsegment: Australien/Neuseeland, kommerziell, Offshore
- Zertifizierung: DNV-GL, Lloyd's Register, ABS
- Besonderheit: Spezialisiert auf tropische Bedingungen, ICCP-Systeme
- Vertrieb: Australien, Neuseeland, Südostasien

### 8.8 Aluminium Anoden GmbH (Deutschland)

**Firmenprofil:**
- Hauptsitz: Hamburg, Deutschland
- Marktsegment: Deutscher Markt, Nord-/Ostsee-Spezialist
- Zertifizierung: DIN EN 12496, MIL-DTL-24779C, DNV-GL
- Besonderheit: Deutsche Fertigung, Spezialist für Aluminium-Anoden
- Vertrieb: Deutschland, Skandinavien, Benelux

**Ausgewählte Produkte:**

| Artikelnr. | Typ | Material | Maße (mm) | Gewicht (g) | Besonderheit | Preis (EUR) |
|-----------|-----|----------|----------|-------------|-------------|-------------|
| AAG-H100 | Rumpf | Al | 150×70×28 | 400 | Ostsee-optimiert | 14–18 |
| AAG-H200 | Rumpf | Al | 200×95×33 | 850 | Universell | 22–28 |
| AAG-H300 | Rumpf | Al | 250×100×38 | 1.300 | Universell | 30–38 |
| AAG-S25 | Welle | Al | Collar ∅25 mm | 140 | Für Ostsee | 18–22 |
| AAG-S30 | Welle | Al | Collar ∅30 mm | 200 | Für Ostsee | 20–26 |
| AAG-S35 | Welle | Al | Collar ∅35 mm | 270 | Für Ostsee | 24–30 |

### 8.9 Sea Shield Marine (USA)

**Firmenprofil:**
- Hauptsitz: Fort Lauderdale, Florida, USA
- Marktsegment: ICCP-Systeme und Spezialanoden
- Zertifizierung: ABYC E-2, ISO 15589-2
- Besonderheit: Fokus auf ICCP und Hybrid-Systeme, Superyacht-Segment

### 8.10 Vetus (Niederlande) — Anoden-Kits

**Firmenprofil:**
- Hauptsitz: Schiedam, Niederlande
- Marktsegment: Yachtausrüstung Komplettsortiment
- Besonderheit: Bietet Anoden als Teil von Antriebssystem-Kits (Bugstrahlruder, Hydraulik)
- Anodensortiment: Begrenzt auf eigene Produkte + Universal-Rumpfanoden

**Vetus-spezifische Anoden:**

| Artikelnr. | Typ | Passend für | Material | Preis (EUR) |
|-----------|-----|-----------|----------|-------------|
| SET0013 | Bugstrahlruder-Anode | BOW55/75/95 | Zn | 35–48 |
| SET0014 | Bugstrahlruder-Anode | BOW125/160 | Zn | 45–60 |
| SET0055 | Bugstrahlruder-Anode | BOW55/75/95 | Al | 38–52 |
| BP1290 | Rumpfanode | Universal | Zn | 12–16 |
| BP1292 | Rumpfanode | Universal | Zn | 18–24 |

### 8.11 OEM-Anoden — Volvo Penta

Volvo Penta verkauft Original-Anoden über das autorisierte Händlernetz. Die Qualität ist gut, die Preise liegen 40–100% über Aftermarket-Äquivalenten.

**Volvo Penta Anoden-Katalog (Auswahl):**

| OEM-Teilenr. | Typ | Passend für | Material | OEM-Preis (EUR) | Aftermarket |
|-------------|-----|-----------|----------|----------------|-------------|
| 3888305 | Saildrive-Ring | 120S, 130S, 150S | Zn | 35–50 | Martyr CMV-18-6Z, Tecnoseal 00706 |
| 3858399 | Ruderblatt | DP-S, DP-SM | Zn | 45–65 | Martyr CMV-20Z, Tecnoseal 00702 |
| 3855411 | Outdrive-Arm | 290/SX, DP-S | Zn | 30–42 | Martyr CMV-23AZ |
| 3841427 | Pencil (Motorblock) | D1-30, D2-40, D2-55 | Zn | 8–14 | Generisch ∅10×38 mm |
| 21868041 | Transom Shield | SX-A, DPS-A, DPS-B | Zn | 25–38 | Martyr CM-3855412Z |
| 22651248 | Propeller-Mutter | alle FH/FP-Propeller | Zn | 18–28 | Martyr CMV-PNA |
| 3584442 | Ring Duo-Prop | DP 290/SX | Zn | 55–75 | Camp 70-VDPA |
| 23937216 | Saildrive-Ring | 130S-D (neu) | Al | 42–58 | Tecnoseal 01706 |

### 8.12 OEM-Anoden — Yanmar

| OEM-Teilenr. | Typ | Passend für | Material | OEM-Preis (EUR) | Aftermarket |
|-------------|-----|-----------|----------|----------------|-------------|
| 27210-200300 | Saildrive-Ring | SD20, SD25, SD30 | Zn | 40–58 | Martyr CMY-1Z, Camp 70-YSDR |
| 27210-200400 | Saildrive-Ring | SD50 | Zn | 55–75 | Tecnoseal 00903 |
| 196420-02652 | Pencil (Block) | 1GM, 2GM, 3GM, 2YM, 3YM | Zn | 12–18 | Martyr CMY-2Z |
| 119574-44150 | Pencil (Wärmetauscher) | 4JH, 6LY, 6LP | Zn | 10–15 | Generisch ∅12×50 mm |
| 196420-02630 | Pencil (kurz) | 1GM10, 2GM20 | Zn | 10–14 | Martyr CMY-3Z |

### 8.13 OEM-Anoden — Mercury / MerCruiser

| OEM-Teilenr. | Typ | Passend für | Material | OEM-Preis (EUR) | Aftermarket |
|-------------|-----|-----------|----------|----------------|-------------|
| 97-821630Q1 | Anode Kit | Alpha One Gen II | Zn | 55–75 | Martyr CMALPHAKITZ, Camp 70-MA1 |
| 97-821631Q1 | Anode Kit | Bravo One | Zn | 65–90 | Martyr CMBRAVOKITZ |
| 97-826134Q | Anode Kit | Bravo Two/Three | Zn | 70–95 | CMP MRC-M826134 |
| 97-888756Q03 | Skeg Anode | Verado/Optimax | Zn | 20–30 | Martyr CM-826134Z |
| 97-823913Q1 | Cavitation Plate | Alpha Gen II | Zn | 25–35 | Martyr CM-823913Z |

> Confidence: `measured` (OEM-Teilenummern), `estimated` (Preise, Stand 2025/2026)

---

## 9. Anlagen-spezifische Zuordnung

### 9.1 Rumpfanoden (Hull Anodes)

#### 9.1.1 Bolt-on Rumpfanoden (geschraubte Flachanoden)

Die häufigste Anodenform auf GFK-Yachten. Zwei Befestigungsbolzen (typisch M8 oder M10, Edelstahl A4/316) durchdringen den Rumpf und werden innen mit Bonding-Kabelschuh und Mutter gesichert.

**Einbauregeln:**

| Parameter | Wert | Quelle |
|-----------|------|--------|
| Mindestanzahl Rumpfanoden (Salzwasser) | 2 (eine pro Seite) | ABYC E-2 |
| Position | Achtern, nahe Propeller/Ruder | Praxisstandard |
| Abstand zur Wasserlinie | mind. 150 mm unter KWL | Empfehlung |
| Abstand zueinander | mind. 1.500 mm | Für gleichmäßige Schutzverteilung |
| Bonding-Anschluss | Via Bolzen auf Innenseite | ABYC E-2 |
| Dichtung | Unterlage mit flexiblem Dichtmittel (Sikaflex 291 / 3M 5200) | Praxis |
| KEIN Antifouling auf Anoden | — | Isoliert die Anode! |

**Dimensionierung nach Bootsgröße (Salzwasser, GFK-Rumpf):**

| Bootslänge (m) | Anodenanzahl | Einzelgewicht Zn (g) | Einzelgewicht Al (g) | Gesamtgewicht Zn (g) | Gesamtgewicht Al (g) |
|----------------|-------------|---------------------|---------------------|---------------------|---------------------|
| 6–8 | 2 | 1.000 | 400 | 2.000 | 800 |
| 8–10 | 2 | 2.000 | 800 | 4.000 | 1.600 |
| 10–12 | 2–3 | 2.000–3.000 | 800–1.200 | 5.000–8.000 | 2.000–3.200 |
| 12–15 | 3–4 | 3.000–5.000 | 1.200–2.000 | 10.000–18.000 | 4.000–7.200 |
| 15–18 | 4–6 | 5.000 | 2.000 | 20.000–30.000 | 8.000–12.000 |
| 18–22 | 6–8 | 5.000–10.000 | 2.000–4.000 | 35.000–60.000 | 14.000–24.000 |
| 22–25 | 8–12 | 10.000 | 4.000 | 80.000–120.000 | 32.000–48.000 |

> Confidence: `estimated` — Exakte Auslegung abhängig von zu schützender Metallfläche, Beschichtungszustand, Wassertemperatur und Fahrgebiet. Richtwerte für typische GFK-Yachten mit Bronze-Borddurchlässen und Edelstahlbeschlägen.

#### 9.1.2 Weld-on Rumpfanoden (geschweißte Flachanoden)

Für Stahl- und Aluminiumrümpfe werden Anoden direkt auf den Rumpf geschweißt. Keine Durchbrüche, kein Leckrisiko.

**Besonderheiten Stahl-/Aluminiumrümpfe:**

| Parameter | Stahlrumpf | Aluminiumrumpf |
|-----------|-----------|----------------|
| Anodenmaterial | Zink oder Aluminium | NUR Aluminium (niemals Zink!) |
| Befestigung | Aufschweißen (Stahlschweiß-Insert) | Aufschrauben oder Schweißen (Al-Schweißung) |
| Schutzfläche pro kg | ~4 m² (Zn) / ~12 m² (Al) | ~10 m² (Al) |
| Potenzial-Überwachung | Empfohlen | OBLIGATORISCH |
| Max. Potenzial | −1.100 mV vs. Ag/AgCl | −1.100 mV vs. Ag/AgCl (KRITISCH!) |

> **AYDI-Warnung Aluminiumrümpfe:** Zinkanoden erzeugen auf Aluminiumrümpfen zu hohe Calcareous Deposits und können bei defekter Beschichtung zur Alkaliversprödung führen. **Ausschließlich Aluminium-Anoden verwenden!** Bei ICCP-System: Potenzialgrenze −1.050 mV vs. Ag/AgCl programmieren.

**Zusätzliche Anforderungen Aluminiumrumpf:**
- Kein kupferhaltiges Antifouling (Kupfer-Ionen → galvanische Korrosion am Rumpf)
- Alle Borddurchlässe aus Aluminium oder isoliert (KEIN Bronze!)
- Trenntransformator bei Landstrom OBLIGATORISCH
- Propeller aus NiBrAl (Nickel-Bronze-Aluminium) oder mit Isolierkupplung
- Bonding-System mit besonderer Sorgfalt (alle Verbindungen kontrollieren)

### 9.2 Wellenanoden (Shaft Anodes)

#### 9.2.1 Collar-/Donut-Anoden

Collar-Anoden (auch Donut- oder Clamp-Anoden) werden als zweiteilige Halbschalen um die Propellerwelle geklemmt. Sie schützen Welle, Wellenlager (Cutless Bearing) und Stevenrohr.

**Einbauregeln:**

| Parameter | Wert | Bemerkung |
|-----------|------|----------|
| Position | 50–100 mm vor Stevenrohr-Austritt | Max. Nähe zum Wasser |
| Befestigung | 2× Innensechskant-Schrauben (Edelstahl A4) | Drehmoment nach Herstellerangabe |
| Fixierung gegen Drehen | Set-Screw (Madenschraube) gegen Welle | Darf Welle nicht beschädigen → Nylon-Spitze |
| Elektrischer Kontakt | Direkter Metallkontakt zur Welle | Welle muss blank sein (kein Lack, kein Fett) |
| Spalt zur Welle | < 0,5 mm (Neuzustand) | Vergrößert sich durch Korrosion |
| Ersatzintervall | Bei 50% Verbrauch | Visuell prüfen |

**Wellendurchmesser-Zuordnung nach Bootsgröße:**

| Bootslänge (m) | Motorleistung (kW) | Typischer Wellendurchmesser (mm) | Anodengewicht Zn (g) | Anodengewicht Al (g) |
|----------------|-------------------|--------------------------------|---------------------|---------------------|
| 7–8 | 7–15 | 22 | 250–300 | 100–120 |
| 8–10 | 10–25 | 25 | 350–400 | 140–160 |
| 10–12 | 15–40 | 25–30 | 400–550 | 160–220 |
| 12–14 | 25–60 | 30–35 | 500–700 | 200–280 |
| 14–16 | 40–90 | 35–40 | 700–950 | 280–380 |
| 16–20 | 60–150 | 40–50 | 950–1.400 | 380–560 |
| 20–25 | 100–300 | 50–60 | 1.400–2.200 | 560–880 |

#### 9.2.2 Wellenerdung (Shaft Grounding)

Auch bei korrekt installierter Collar-Anode kann die Welle galvanisch isoliert sein, wenn:
- Flexible Wellenkupplung aus Gummi (Vetus Bullflex, R&D Marine) den Strom unterbricht
- Cutless Bearing mit Kunststoff-/Gummilagerfläche isoliert
- Getriebeöl als Isolator wirkt

**Lösung: Wellenerdungsbürste (Shaft Brush)**

| Hersteller | Modell | Wellendurchmesser (mm) | Preis (EUR) |
|-----------|--------|----------------------|-------------|
| **Maplins Marine / MG Duff** | SEB-25 bis SEB-60 | 25–60 | 45–90 |
| **Electro-Guard** (USA) | EG-xxx | 19–75 | 55–120 |
| **Volvo Penta** | 21631220 | Universal | 65–90 |
| **R&D Marine** | SBK-xxx | 25–50 | 50–80 |

**Einbau:** Kohle-/Silberbürste kontaktiert die Welle und ist über Kabel mit dem Bonding-System verbunden. Ersatzintervall: alle 2–3 Jahre.

### 9.3 Propelleranoden

#### 9.3.1 Propellermutter-Anoden (Prop Nut Anodes)

Eine Zinkanode, die als Hutmutter auf die Propellermutter geschraubt oder über die bestehende Mutter gestülpt wird.

| Hersteller | Typ | Passend für | Gewicht (g) | Preis (EUR) |
|-----------|-----|-----------|-------------|-------------|
| Martyr | CMX-xxx-Z | Universal M18–M30 | 200–600 | 12–25 |
| Tecnoseal | 00560–00566 | Universal M20–M30 | 250–650 | 14–28 |
| CMP | ZPC-xxx | Universal | 200–700 | 14–26 |
| Camp | 70-Pxxx | Universal | 200–600 | 10–22 |

#### 9.3.2 Propellerblatt-Anoden

Für Festpropeller und verstellbare Propeller werden flache Anoden direkt auf die Propellernabe oder -blätter geschraubt.

**Kritische Regel:** Propelleranoden allein ersetzen NICHT die Wellenanoden. Sie bieten nur lokalen Schutz der Propelleroberfläche.

#### 9.3.3 Max-Prop und Faltpropeller

Falt- und Verstellpropeller (Max-Prop, Variprop, Flexofold, SPW) haben eigene Anodentypen:

| Propeller | Anodenform | OEM-Teilenr. | Aftermarket | Preis (EUR) |
|-----------|-----------|-------------|------------|-------------|
| Max-Prop Easy | Ring-Anode | MP-ZA-xx | Martyr CMMP-xx | 25–45 |
| Variprop GP | Tab-Anode | VP-ZA-xx | — | 20–35 |
| Flexofold | Propnuss-Anode | FF-ZA-xx | — | 18–30 |
| SPW (Kanzaki) | Pencil + Ring | SPW-ZA | — | 22–35 |

### 9.4 Ruderanoden

Ruder mit Edelstahlschaft oder Aluminium-Ruderblatt benötigen eigenen Korrosionsschutz, besonders wenn das Ruder über eine Gummidichtung (Quadring/Lippendichtung) im Ruderkoker elektrisch vom Rumpf isoliert ist.

**Anodenformen:**

| Typ | Beschreibung | Befestigung | Typische Größe |
|-----|-------------|-------------|---------------|
| Klapp-Anode | Zweiteilig, klemmt auf Ruderblatt | 2× Schrauben M6/M8 | 100–300 g |
| Bolt-on Anode | Auf Ruderblatt geschraubt | 2× M8 | 200–500 g |
| Ruderschaft-Collar | Wie Wellenanoden, aber am Ruderschaft | Klemmung | 150–400 g |

**Dimensionierung:**

| Bootslänge (m) | Ruderanoden-Gewicht Zn (g) | Ruderanoden-Gewicht Al (g) |
|----------------|---------------------------|---------------------------|
| 7–10 | 150–300 | 60–120 |
| 10–14 | 300–500 | 120–200 |
| 14–18 | 500–1.000 | 200–400 |
| 18–22 | 1.000–2.000 | 400–800 |

### 9.5 Trim-Tab-Anoden

Trim Tabs (Trimmklappen) am Heckspiegel bestehen meist aus Edelstahl und sind ständig im Wasser. Ohne eigene Anode korrodieren die Befestigungen und das Trim-Tab-Blatt selbst.

**Standard-Trimmklappen-Anoden:**

| Hersteller | Artikelnr. | Passend für | Material | Gewicht (g) | Preis (EUR) |
|-----------|-----------|-----------|----------|-------------|-------------|
| Martyr | CMT-1Z | Bennett, Lenco (universal) | Zn | 450 | 15–20 |
| Martyr | CMT-2Z | Bennett 12"×12" | Zn | 800 | 18–25 |
| Tecnoseal | 00135 | Bennett 9"×9" | Zn | 350 | 14–18 |
| Tecnoseal | 00136 | Bennett 12"×12" | Zn | 700 | 18–24 |
| Camp | 70-T1 | Universal | Zn | 400 | 12–16 |
| CMP | ZTT-xxx | Bennett, Lenco | Zn | 350–800 | 14–24 |

**Einbauregel:** Anode wird auf der Unterseite der Trimmklappe montiert, elektrischer Kontakt zum Edelstahlblech, Bonding via Scharnier oder separaten Draht.

### 9.6 Saildrive-Anoden

Saildrives (Volvo Penta S-Drive, Yanmar SD-Serie) sind besonders korrosionsanfällig, da das Getriebegehäuse aus Aluminium direkt im Seewasser steht und mit Bronze-/Edelstahl-Propeller und -Beschlägen in Kontakt ist.

#### 9.6.1 Volvo Penta Saildrive-Anoden

| Saildrive-Modell | Anoden-Typ | OEM-Teilenr. | Aftermarket | Material | Preis (EUR) |
|-----------------|-----------|-------------|------------|----------|-------------|
| 120S (alt) | Ring-Anode | 3888305 | Martyr CMV-18-6Z | Zn | 25–35 |
| 130S | Ring-Anode | 3888305 | Tecnoseal 00706 | Zn | 22–32 |
| 130S-D (neu) | Ring-Anode | 23937216 | Tecnoseal 01706 | Al | 28–40 |
| 150S | Ring-Anode | 23937216 | Camp 70-VSDR-A | Al | 30–42 |

**Wechselintervall Saildrive-Anoden:**

| Bedingung | Intervall | Begründung |
|-----------|----------|-----------|
| Salzwasser, Dauerlieger | 8–12 Monate | Hohe Korrosionsbelastung |
| Salzwasser, saisonal | 12–18 Monate | Winterlager entlastet |
| Ostsee West | 12–18 Monate (Al-Anode!) | Brackwasser → nur Aluminium |
| Ostsee Ost / Süßwasser | 18–24 Monate (Mg oder ICCP) | Geringe Leitfähigkeit |

> **AYDI-Warnung Saildrive:** Saildrive-Gehäuse bestehen aus Aluminium. NIEMALS Zinkanoden bei niedrigem Salzgehalt verwenden (Passivierung → kein Schutz → Gehäuse korrodiert). Im Zweifelsfall IMMER Aluminium-Anoden wählen. Bei Aluminium-Saildrive in Süßwasser: Magnesium-Ring oder ICCP.

#### 9.6.2 Yanmar Saildrive-Anoden

| Saildrive-Modell | Anoden-Typ | OEM-Teilenr. | Aftermarket | Material | Preis (EUR) |
|-----------------|-----------|-------------|------------|----------|-------------|
| SD20 | Ring-Anode | 27210-200300 | Martyr CMY-1Z | Zn | 20–28 |
| SD25 | Ring-Anode | 27210-200300 | Camp 70-YSDR | Zn | 18–26 |
| SD30 | Ring-Anode | 27210-200300 | Tecnoseal 00901 | Zn | 20–28 |
| SD50 | Ring-Anode | 27210-200400 | Tecnoseal 00903 | Zn | 28–38 |

### 9.7 Sterndrive-Anoden (Z-Antrieb)

Z-Antriebe (Stern Drives) haben die höchste Anodenanzahl aller Antriebssysteme, da sie viele verschiedene Aluminium- und Edelstahlkomponenten unter Wasser exponieren.

#### 9.7.1 Mercury MerCruiser Anoden

**Alpha One Gen II — Komplettsatz:**

| Position | OEM-Teilenr. | Aftermarket (Martyr) | Gewicht (g) | Preis (EUR) |
|---------|-------------|---------------------|-------------|-------------|
| Getriebegehäuse | 97-821630Q1 (Kit) | CMALPHAKITZ | (Satz) | 45–65 |
| Trim Tab (Cavitation Plate) | 97-823913Q1 | CM-823913Z | 650 | 18–25 |
| Skeg | 31640Q4 | CM-31640Z | 150 | 8–14 |
| Pencil (Wärmetauscher) | 8M0065125 | CMM-E3Z | 35 | 4–8 |

**Bravo One/Two/Three — Komplettsatz:**

| Position | OEM-Teilenr. | Aftermarket (Martyr) | Gewicht (g) | Preis (EUR) |
|---------|-------------|---------------------|-------------|-------------|
| Bravo Anode Kit | 97-821631Q1 (Bravo I) | CMBRAVOKITZ | (Satz) | 55–75 |
| Bravo Anode Kit | 97-826134Q (Bravo II/III) | CMBRAVO23KIT | (Satz) | 60–80 |
| Propellermutter | 97-821630T2 | CM-821630Z | 200 | 10–16 |
| Pencil (Motor) | 8M0065125 | CMM-E3Z | 35 | 4–8 |

**Wechselintervall MerCruiser:**

| Nutzung | Intervall | Besonderheit |
|---------|----------|-------------|
| Salzwasser, intensiv (> 200 h/a) | 6–8 Monate | Aluminium-Kit bevorzugt |
| Salzwasser, normal (100–200 h/a) | 10–12 Monate | Zink-Kit Standard |
| Brackwasser | 12–18 Monate | NUR Aluminium-Kit |
| Süßwasser | 18–24 Monate | Magnesium-Kit |

#### 9.7.2 Volvo Penta DPS/SX Anoden

| Position | OEM-Teilenr. | Aftermarket | Gewicht (g) | Preis (EUR) |
|---------|-------------|------------|-------------|-------------|
| DPS-A/DPS-B Anode Kit | 21868041 (Kit) | Martyr CMV-DPSKITZ | (Satz) | 60–85 |
| Transom Shield | 3855411 | Martyr CMV-23AZ | 400 | 15–22 |
| Ruderblatt | 3858399 | Tecnoseal 00702 | 800 | 22–32 |
| Ring (Duo-Prop) | 3584442 | Camp 70-VDPA | 350 | 18–28 |
| Pencil (Motor) | 3841427 | Generisch ∅10×38 | 20 | 3–6 |

### 9.8 Borddurchlass-Schutz (Through-Hull Protection)

Borddurchlässe aus Bronze oder Edelstahl sind kritische Unterwasserkomponenten, die galvanisch geschützt werden müssen.

**Bonding-Anforderung:**
- Jeder metallische Borddurchlass muss an das Bonding-System angeschlossen werden
- Bonding-Kabel (verzinntes Kupfer, ≥ 10 mm²) mit Ringkabelschuh
- Befestigung am Borddurchlass-Flansch oder am Seeventil-Gehäuse
- Kontaktfläche blank, mit Kontaktfett (Tef-Gel)

**Borddurchlass-Materialien und Korrosionsrisiko:**

| Material | Potenzial (mV) | Korrosionsrisiko | Bonding erforderlich |
|---------|---------------|-----------------|---------------------|
| Bronze (G-CuSn10) | −280 bis −350 | Gering (edel) | Ja (schützt durch Bonding die Anoden) |
| Edelstahl 316L | −50 bis −200 (passiv) | Lochfraß in Spalten | Ja |
| Messing (CuZn) | −300 bis −400 | HOCH (Entzinkung!) | Ja + sofort ersetzen |
| Marelon / GFK | n/a | Keines (Kunststoff) | Nein (nicht leitend) |
| Titan | +50 bis −50 | Keines | Nein (zu edel, würde Anoden auffressen) |

> **AYDI-Warnung:** Messing-Borddurchlässe (erkennbar an gelblicher Farbe statt rötlich-brauner Bronze) sind NICHT seewasserbeständig. Entzinkung (Dezincification) kann innerhalb von 2–5 Jahren zum Versagen führen. Sofortiger Austausch gegen Bronze oder Marelon empfohlen.

### 9.9 Wärmetauscher-Anoden (Pencil Anodes / Rod Anodes)

Seewassergekühlte Motoren enthalten Wärmetauscher, in denen Seewasser durch Röhrenbündel aus Kupfer-Nickel oder Kupfer fließt. Ohne interne Anode korrodieren die Röhren von innen.

**Pencil-Anoden-Typen:**

| Durchmesser (mm) | Länge (mm) | Gewinde | Passt für | Material | Preis (EUR) |
|------------------|-----------|---------|----------|----------|-------------|
| 8 | 30 | 3/8" NPT | Kleine Motoren (1GM, 2GM) | Zn | 3–6 |
| 10 | 38 | 1/2" NPT | Volvo D1/D2, Yanmar 2/3GM | Zn | 4–7 |
| 12 | 50 | 1/2" NPT | Yanmar 3/4JH, Volvo D2-40 | Zn | 5–8 |
| 12 | 50 | 3/4" NPT | Caterpillar, Cummins | Zn | 5–9 |
| 16 | 75 | 3/4" NPT | Große Dieselmotoren | Zn | 8–14 |
| 16 | 100 | 1" NPT | Schiffsdiesel > 100 kW | Zn | 10–16 |

**Wechselintervall Pencil-Anoden:**

| Betriebsstunden | Empfehlung |
|----------------|-----------|
| < 200 h/Jahr | Jährlich prüfen, alle 2 Jahre wechseln |
| 200–500 h/Jahr | Alle 12 Monate wechseln |
| > 500 h/Jahr | Alle 6 Monate wechseln |
| Salzwasser + > 500 h | Alle 3–4 Monate prüfen |

> **AYDI-Hinweis:** Pencil-Anoden für Motorblöcke und Wärmetauscher sollten vorzugsweise aus **Aluminium** gefertigt sein, da Zink bei den typischen Betriebstemperaturen (50–80°C) passivieren kann. Viele OEM liefern jedoch nach wie vor Zink — in diesen Fällen ist der kürzere Wechselintervall zu beachten.

**Hersteller Pencil-Anoden:**

| Hersteller | Artikelserie | Material | Besonderheit |
|-----------|-------------|----------|-------------|
| Martyr | CME-Serie | Zn/Al | Breitestes Sortiment, alle NPT-Größen |
| Tecnoseal | 00200-Serie | Zn | OEM-Qualität |
| Camp | 70-E-Serie | Zn | Günstig, solide |
| CMP | ZPC-E-Serie | Zn/Al | Premium |
| MG Duff | EP-Serie | Zn | UK-Standard |

### 9.10 AYDI-Bewertungsschema für Korrosionsschutz

```python
# ─── Scoring-Logik ──────────────────────────────────────────────────

KORROSIONSSCHUTZ_SCORING = {
    "anode_condition": {
        "weight": 0.35,
        "scoring": {
            "all_new_or_good": 100,           # Alle Anoden < 30% verbraucht
            "all_serviceable": 80,             # Alle < 50% verbraucht
            "some_replace_soon": 55,           # Einzelne > 50%, aber keine depleted
            "some_critical": 30,               # Einzelne > 70%
            "any_depleted": 10,                # Mindestens eine komplett verbraucht
            "any_missing": 0,                  # Mindestens eine fehlt
        },
    },
    "material_match": {
        "weight": 0.25,
        "scoring": {
            "correct_material_for_water": 100,     # Richtige Legierung für Revier
            "suboptimal_but_functional": 60,       # Z.B. Zink in leichtem Brackwasser
            "wrong_material": 0,                    # Z.B. Zink in Süßwasser
        },
    },
    "bonding_system": {
        "weight": 0.20,
        "scoring": {
            "complete_and_functional": 100,        # Alle Komponenten angebunden
            "mostly_complete": 70,                 # > 80% der Komponenten
            "partial": 40,                         # 50–80% der Komponenten
            "minimal_or_absent": 10,               # < 50% oder kein System
        },
    },
    "stray_current_protection": {
        "weight": 0.10,
        "scoring": {
            "isolation_transformer": 100,          # Trenntransformator vorhanden
            "galvanic_isolator_failsafe": 90,      # Fail-Safe-Isolator
            "galvanic_isolator_diode": 70,         # Dioden-Isolator
            "no_protection": 20,                   # Kein Schutz bei Landstrom
            "no_shore_power": 100,                 # Kein Landstrom → kein Risiko
        },
    },
    "documentation": {
        "weight": 0.10,
        "scoring": {
            "complete_log": 100,                   # Vollständiges Anodenwechsel-Protokoll
            "partial_log": 60,                     # Einige Einträge
            "no_log": 20,                          # Keine Dokumentation
        },
    },
}

# Gesamtscore = Σ (category_score × weight)
# Score 0–100, Einheit: dimensionslos
# Confidence: abhängig von Datenquelle (measured/visual/estimated)
```

> Confidence: `measured` (Bewertungsschema), `estimated` (Schwellenwerte basierend auf Praxiserfahrung)

### 9.11 Bugstrahlruder-Anoden

Bugstrahlruder (Bow Thruster) mit Edelstahl- oder Bronze-Propeller in einem GFK- oder Aluminiumtunnel benötigen eigene Anoden, da sie häufig elektrisch schlecht an das Bonding-System angebunden sind.

**Typische Bugstrahlruder-Anoden:**

| Hersteller | Modell | Passend für | Material | Gewicht (g) | Preis (EUR) |
|-----------|--------|-----------|----------|-------------|-------------|
| Vetus | SET0013 | BOW55/75/95 | Zn | 180 | 35–48 |
| Vetus | SET0014 | BOW125/160 | Zn | 320 | 45–60 |
| Vetus | SET0055 | BOW55/75/95 | Al | 85 | 38–52 |
| Side-Power | SP-ZA-55 | SE40/SE60 | Zn | 160 | 30–42 |
| Side-Power | SP-ZA-80 | SE80/SE100 | Zn | 280 | 38–52 |
| Max Power | MP-ZA-CT | CT60/CT80/CT100 | Zn | 200 | 32–45 |
| Lewmar | 589505 | 140TT/185TT | Zn | 250 | 40–55 |

**Einbauhinweise:**
- Anode am Tunnelende befestigen, nahe Propellerbereich
- Bonding-Kabel zum Bugstrahlruder-Motor führen
- Bei GFK-Tunnel: Bonding-Platte innen einlaminieren als Anschluss
- Bei Aluminiumtunnel: KEINE Zinkanoden verwenden, nur Aluminium
- Wechselintervall: gleich wie Rumpfanoden (jedes Slipping prüfen)

### 9.12 Kiel-Anoden

Schwertmontierte Kiele (Blei oder Gusseisen) sind die größte einzelne Metallfläche unter Wasser und benötigen bei beschädigter Beschichtung massiven Anodenschutz.

**Kieltypen und Korrosionsrisiko:**

| Kielmaterial | Potenzial (mV vs. Ag/AgCl) | Korrosionsrisiko | Anodenempfehlung |
|-------------|---------------------------|-----------------|-----------------|
| Blei (rein/Antimon) | −500 bis −600 | Gering (relativ edel) | 1–2 kleine Rumpfanoden nahe Kiel |
| Gusseisen | −600 bis −710 | HOCH (große Fläche, porös) | 2–4 Rumpfanoden am Kielbereich |
| Stahl (geschweißt) | −600 bis −710 | HOCH | 2–4 Rumpfanoden + Bonding |
| Blei-Kiel mit Gusseisen-Kielschwert | Gemischt | MITTEL | Bonding zwischen Kiel und Schwert |

**Spezialfall Gusseisen-Kiel:**
- Größte Metallfläche unter Wasser (typisch 0,5–3,0 m² freiliegend)
- Beschichtung (Primer + Antifouling) reduziert den Schutzbedarf dramatisch
- Bei beschädigter Beschichtung: Anodenbedarf steigt um Faktor 5–10
- Gusseisen ist porös → Feuchtigkeit dringt ein → Abplatzen der Beschichtung
- **AYDI-Empfehlung:** Kiel-Beschichtungszustand hat höchste Priorität bei Korrosionsbeurteilung

### 9.13 Cross-Referenz: Bootshersteller → Typische Anodenausstattung ab Werft

Die folgende Tabelle dokumentiert, welche Anoden serienmäßig bei verbreiteten Bootsherstellern verbaut werden. Dies ist für AYDI relevant, da bei Schnellanalyse (Level 1) ohne spezifische Angaben auf die werftübliche Ausstattung zurückgegriffen werden kann.

**Segelboote — Serienausstattung:**

| Hersteller | Modellreihe | Antrieb | Anodenausstattung ab Werft | Material | Typische Teilenummern |
|-----------|-------------|---------|--------------------------|----------|----------------------|
| Bavaria | C42/C45/C50 | Volvo Saildrive 130S | 1× Saildrive-Ring, 1× Wellenanoden entfällt (SD), 2× Rumpf | Zn | OEM Volvo 3888305, 2× generisch |
| Beneteau | Oceanis 40.1/46.1/51.1 | Yanmar SD20/SD25 | 1× Saildrive-Ring, 2× Rumpf | Zn | Yanmar 27210-200300, 2× Tecnoseal 00101 |
| Jeanneau | Sun Odyssey 410/440/490 | Yanmar SD25/SD30 | 1× Saildrive-Ring, 2× Rumpf | Zn | Yanmar 27210-200300, 2× Camp 70-1 |
| Hanse | 388/418/460/510 | Volvo Saildrive 130S | 1× Saildrive-Ring, 2× Rumpf | Zn | OEM Volvo, 2× generisch |
| Hallberg-Rassy | 340/400/44 | Volvo SD 130S/150S | 1× Saildrive-Ring, 2× Rumpf, 1× Propeller | Zn | OEM Volvo + HR-eigene Rumpfanoden |
| Najad / Hallberg-Rassy (Langkieler) | diverse | Welle + Fest-Prop | 1× Collar, 2× Rumpf, 1× Rudder | Zn | Standard generisch |
| X-Yachts | X4°/Xc 45/Xp 44 | Volvo SD 130S | 1× Saildrive-Ring, 2× Rumpf | Zn | OEM Volvo |
| Dehler | 30/34/38/46 | Volvo SD 130S | 1× Saildrive-Ring, 1–2× Rumpf | Zn | OEM Volvo |
| Dufour | 360/390/470/530 | Volvo SD 130S/150S | 1× Saildrive-Ring, 2× Rumpf | Zn | OEM Volvo |
| Amel | 50/55/60 | Volvo SD 150S | 1× Saildrive-Ring, 3× Rumpf, Propeller | Zn/Al | OEM Volvo + Amel-spezifisch |

**Motorboote — Serienausstattung:**

| Hersteller | Modellreihe | Antrieb | Anodenausstattung ab Werft | Material |
|-----------|-------------|---------|--------------------------|----------|
| Nimbus | C9/T9/T11 | Volvo DPS | DPS Anode Kit (3–4 Stück), 2× Rumpf, Pencil | Zn |
| Aquador | 25/28/35 | MerCruiser/Volvo | Alpha/DPS Kit, 2× Rumpf, Pencil | Zn |
| Quicksilver | Activ 675/755/875 | Mercury F150–F300 | Skeg-Anode, 1–2× Rumpf | Zn |
| Beneteau | Antares 8/9/11 | Yanmar/Mercury | 2× Rumpf, Motor-Pencil | Zn |
| Jeanneau | Merry Fisher 795/895/1095 | Yanmar/Mercury | 2× Rumpf, Motor-Pencil | Zn |
| Linssen | Grand Sturdy 30/35/40/45 | Volvo D2/D3, Welle | 2–4× Rumpf Weld-on, 1–2× Collar, Pencil | Zn |
| Broom | 370/430 | Volvo D4/D6, Welle | 4–6× Rumpf, 2× Collar, 2× Rudder, Pencils | Zn |
| Princess | F45/V55/Y72 | Volvo IPS / MAN | ICCP + Backup Opferanoden | — |
| Sunseeker | Manhattan 55/68, Predator | Volvo IPS / MAN | ICCP + Backup Opferanoden | — |

> Confidence: `documented` (Werftkataloge, Eigner-Berichte), `estimated` (manche Modelle variieren nach Baujahr)

### 9.14 Spezialtopic: Aluminiumrümpfe — Erweiterte Korrosionsschutz-Anforderungen

Aluminiumrümpfe erfordern ein vollständig anderes Korrosionsschutzkonzept als GFK-Rümpfe. Die AYDI-Analyse muss bei Erkennung eines Aluminiumrumpfs automatisch verschärfte Prüfkriterien anlegen.

**Absolut verbotene Kombinationen bei Aluminium-Rümpfen:**

| Verboten | Begründung | Konsequenz |
|----------|-----------|-----------|
| Zinkanoden | Passivierung in warmem Wasser, Calcareous Deposits | Kein Schutz, Ablagerungen |
| Kupfer-Antifouling | Kupfer-Ionen lösen sich → Abscheidung auf Al → Lochfraß | Rumpf-Durchbruch möglich |
| Bronze-Borddurchlässe | Potenzialdifferenz 500–800 mV zum Rumpf | Massive Lochkorrosion im Rumpf |
| Messing-Armaturen | Entzinkung + galvanische Korrosion | Doppeltes Versagensrisiko |
| Landstrom ohne Trafo | Streustrom zerstört Al-Rumpf in Wochen | KATASTROPHAL |
| Edelstahl-Propeller ohne Isolierung | 600+ mV Differenz, große Kathodenfläche | Propeller-Umgebung perforiert |

**Obligatorische Maßnahmen bei Aluminium-Rümpfen:**
1. NUR Aluminium-Opferanoden (MIL-DTL-24779C)
2. Trenntransformator bei Landstrom (KEIN einfacher galvanischer Isolator)
3. Kupferfreies Antifouling (z.B. Hempel Silic One, International Trilux 33)
4. Borddurchlässe aus Aluminium, Titan oder Marelon
5. Propeller aus NiBrAl mit galvanischer Isolierkupplung
6. ICCP-System empfohlen (Potenzial exakt auf −800 bis −1.050 mV regelbar)
7. Potenzial-Monitoring permanent installieren
8. Bonding-System mit besonderer Sorgfalt (alle Übergänge dokumentieren)

| Bootslänge Al-Rumpf | Min. Anodenmasse Al (kg) | ICCP empfohlen | Trenntransformator |
|---------------------|------------------------|---------------|-------------------|
| 8–10 m | 2–4 | Optional | Obligatorisch |
| 10–14 m | 4–8 | Dringend empfohlen | Obligatorisch |
| 14–20 m | 8–15 | Obligatorisch | Obligatorisch |
| > 20 m | 15–40 | Obligatorisch (primär) | Obligatorisch |

> Confidence: `documented` (Klassegesellschaften DNV, Bureau Veritas, Herstellervorschriften)

### 9.15 Häufige Fehler bei der Anodeninstallation

Die folgenden Fehler werden in der AYDI-Analyse als Befunde gemeldet:

| Fehler | Beschreibung | Häufigkeit | Schwere | AYDI-Score-Impact |
|--------|-------------|-----------|---------|------------------|
| **Antifouling auf Anoden** | Anode mit Antifouling überstrichen → elektrisch isoliert, wirkungslos | Sehr häufig | KRITISCH | −40 Punkte |
| **Falsche Materialwahl** | Zink in Süßwasser / Magnesium in Salzwasser | Häufig | KRITISCH | −50 Punkte |
| **Fehlende Bonding-Verbindung** | Anode nicht mit Bonding-System verbunden | Häufig | HOCH | −30 Punkte |
| **Zu kleine Anoden** | Unterdimensioniert für Rumpfgröße / Metallmasse | Mittel | HOCH | −25 Punkte |
| **Mischung Zn + Al** | Verschiedene Anodenmaterialien am selben Boot | Selten | MITTEL | −15 Punkte |
| **Anode am falschen Ort** | Rumpfanode zu weit von Unterwasser-Metallteilen | Mittel | MITTEL | −20 Punkte |
| **Korrodierte Befestigungsbolzen** | Edelstahl-Bolzen A2 statt A4 → Bolzen korrodiert, Anode fällt ab | Häufig | HOCH | −30 Punkte |
| **Kein galvanischer Isolator** | Landstrom ohne GI oder Trenntransformator | Sehr häufig | HOCH | −20 Punkte |
| **Titanschrauben für Anodenbefestigung** | Titan ist zu edel → Anode schützt die Schraube statt den Rumpf | Selten | MITTEL | −10 Punkte |
| **Anode nicht im Wasser** | Rumpfanode oberhalb der Wasserlinie montiert | Selten | KRITISCH | −50 Punkte |

### 9.16 Inspektions-Checkliste für AYDI Pipeline B (Visuelle Analyse)

Die folgende Checkliste definiert, was das visuelle Modul bei Unterwasserfotos systematisch prüfen soll:

**Foto-Typ: Unterwasser-Gesamtansicht (Rumpf auf Kran/Slip)**

| Prüfpunkt | Erkennungsmerkmal | Bewertung | Min. Confidence |
|-----------|-------------------|----------|----------------|
| Anodenanzahl | Sichtbare Rumpfanoden zählen | Abgleich mit Soll-Anzahl | `visual_medium` |
| Anodenverbrauch je Stück | Dickenverhältnis, Formverlust | % verbraucht schätzen | `visual_medium` |
| Anodenmaterial | Farbe: Zink = grau-weiß, Al = dunkelgrau, Mg = hellgrau-körnig | Material bestimmen | `visual_low` |
| Anodenoberfläche | Glatt = aktiv, pastivartig/weiß = passiviert | Funktionalität beurteilen | `visual_medium` |
| Bewuchs auf Anode | Algen, Muscheln, Seepocken | Wirksamkeit eingeschränkt | `visual_high` |
| Antifouling auf Anode | Farbspuren sichtbar | FEHLER melden | `visual_high` |
| Korrosion an Nachbar-Bauteilen | Verfärbungen, Lochfraß, Materialverlust | Schweregrad bewerten | `visual_medium` |
| Propellerzustand | Verfärbungen, Auswaschungen, Rauheit | Korrosionsindikator | `visual_medium` |
| Ruderblatt-Oberfläche | Blasen, Verfärbungen, Auflösung | Korrosionsindikator | `visual_medium` |
| Saildrive-Gehäuse | Weiße Ablagerungen, Lochfraß im Al-Gehäuse | KRITISCH wenn sichtbar | `visual_high` |
| Bonding-Kabel (sichtbar) | Grüne Oxidation = Kupfer-Korrosion | Verbindung prüfen | `visual_low` |

**Foto-Typ: Detail-Aufnahme Einzelanode**

| Prüfpunkt | Erkennungsmerkmal | Bewertung | Min. Confidence |
|-----------|-------------------|----------|----------------|
| Restdicke | Vergleich mit Befestigungsebene | % Verbrauch | `visual_high` |
| Auflösungsmuster | Gleichmäßig = normal, lokalisiert = Streustrom | Diagnose | `visual_medium` |
| Befestigungszustand | Bolzen sichtbar, Spalt erkennbar | Sicherheit | `visual_high` |
| Kontaktqualität | Spalt zwischen Anode und Rumpf | Bonding-Qualität | `visual_medium` |

### 9.17 Wartungsintervalle — Zusammenfassende Tabelle

| Komponente | Prüfintervall | Wechselintervall | Wer | Geschätzte Kosten (EUR) |
|-----------|---------------|-----------------|-----|------------------------|
| Rumpfanoden | Jedes Slipping | Bei 50% Verbrauch | Eigner/Werft | 15–90 pro Stück |
| Wellenanoden | Jedes Slipping | Bei 50% Verbrauch | Eigner/Werft | 15–45 pro Stück |
| Propelleranoden | Jedes Slipping | Bei 50% Verbrauch | Eigner/Werft | 12–30 pro Stück |
| Ruderanoden | Jedes Slipping | Bei 50% Verbrauch | Eigner/Werft | 10–25 pro Stück |
| Saildrive-Ring | Jedes Slipping | Alle 12–18 Monate (Salzwasser) | Eigner/Werft | 20–40 |
| Sterndrive-Kit | Jedes Slipping | Alle 12 Monate (Salzwasser) | Werft/Mechaniker | 45–95 |
| Pencil-Anoden (Motor) | Jeder Ölwechsel | Alle 12–24 Monate | Eigner/Mechaniker | 3–15 pro Stück |
| Bonding-System | Jährlich messen | Bei Widerstand > 1 Ω | Elektriker | 50–200 (Fehlersuche) |
| Wellenerdungsbürste | Jährlich prüfen | Alle 2–3 Jahre | Eigner/Mechaniker | 45–120 |
| Galvanischer Isolator | Jährlich Funktionstest | Bei Defekt (LED-Anzeige) | Elektriker | 90–500 |
| Referenzelektrode (ICCP) | Halbjährlich kalibrieren | Alle 3–5 Jahre | Spezialist | 150–400 |
| ICCP-Titananoden | Jährlich Sichtprüfung | Alle 15–20 Jahre | Spezialist | 300–1.500 |
| Rumpfpotenzial-Messung | Bei jedem Slipping + bei Streustromverdacht | — | Eigner/Surveyor | 0 (DIY) / 50–150 (Surveyor) |

### 9.18 Auslegungsberechnung — Vereinfachte Faustformel

Für die AYDI-Schnellanalyse (Level 1) wird folgende Faustformel zur Anodenauslegung verwendet, wenn keine exakten CAD-Daten vorliegen:

**Zu schützende Fläche (geschätzt):**

```
A_protected = Σ (Metallfläche aller Unterwasserkomponenten)

Typische Werte:
- Bronze-Borddurchlass: 0,005–0,01 m² pro Stück
- Propeller (3-Blatt): 0,03–0,08 m² (je nach Durchmesser)
- Welle (freiliegend): π × d × L (z.B. ∅30mm × 500mm = 0,047 m²)
- Ruderblatt (Edelstahl): 0,1–0,5 m²
- Saildrive-Gehäuse: 0,05–0,15 m²
- Kiel (Gusseisen/Blei, unbeschichtet): 0,5–3,0 m²
- Bugstrahlruder-Tunnel: 0,1–0,3 m²
```

**Erforderliche Anodenmasse (vereinfacht nach DNV-RP-B401):**

```
m_anode = (I_c × A_c × t) / (u × ε)

Wobei:
  I_c = Schutzbedarf (A/m²) — typisch 0,01–0,05 für beschichtete Oberflächen,
        0,05–0,15 für blanke Bronze/Edelstahl
  A_c = zu schützende Fläche (m²)
  t   = Schutzdauer (Jahre) — typisch 1–2 für Yachten
  u   = Stromkapazität (Ah/kg) — Zn: 780, Al: 2.600, Mg: 580 (effektiv)
  ε   = Nutzungsfaktor — typisch 0,80–0,85
```

**Schnellrechner — Typische Yachten:**

| Yacht-Typ | Zu schützende Fläche (m²) | Schutzbedarf (A/m²) | Strom (A) | Zink-Masse (kg/Jahr) | Al-Masse (kg/Jahr) |
|-----------|--------------------------|--------------------|-----------|--------------------|-------------------|
| Segelyacht 10 m, Saildrive | 0,2 | 0,08 | 0,016 | 0,24 | 0,07 |
| Segelyacht 12 m, Welle+Prop | 0,4 | 0,08 | 0,032 | 0,48 | 0,14 |
| Segelyacht 15 m, Welle+Prop+Ruder | 0,8 | 0,08 | 0,064 | 0,95 | 0,29 |
| Motorboot 10 m, Z-Antrieb | 0,3 | 0,10 | 0,030 | 0,45 | 0,13 |
| Motorboot 14 m, Welle+Prop | 0,6 | 0,10 | 0,060 | 0,89 | 0,27 |
| Motorboot 18 m, 2× Welle | 1,5 | 0,10 | 0,150 | 2,23 | 0,67 |
| Motor-Yacht 22 m, 2× Welle | 3,0 | 0,10 | 0,300 | 4,46 | 1,34 |

> **Hinweis:** Diese Werte sind Mindest-Anodenmassen für die Schutzperiode. In der Praxis wird 50–100% Sicherheitszuschlag empfohlen, um den 50%-Wechselzeitpunkt nicht zu früh zu erreichen. Die Werte berücksichtigen beschichtete Kielflächen — bei unbeschichtetem Gusseisen-Kiel steigt der Bedarf um Faktor 3–5.

> Confidence: `calculated` (Formel nach DNV-RP-B401), `estimated` (Flächenwerte, Sicherheitszuschlag)

### 9.19 Glossar — Fachbegriffe Korrosionsschutz

| Begriff | Englisch | Definition |
|---------|----------|-----------|
| Anodischer Schutz | Anodic protection | Schutz durch gezieltes Aufprägen eines passiven Potenzials (nicht zu verwechseln mit Opferanoden) |
| Arbeitspotenzial | Closed circuit potential (CCP) | Potenzial der Anode unter Schutzstromlast |
| Bonding | Bonding | Elektrische Verbindung aller Unterwasser-Metallteile |
| Calcareous Deposit | Calcareous deposit | Kalk-/Magnesiumablagerung auf der Kathode durch Überprotektion |
| Depolarisation | Depolarization | Veränderung des Elektrodenpotenzials durch Stromfluss |
| Elektrochemische Reihe | Galvanic series | Reihung der Metalle nach Potenzial in einem Elektrolyten |
| Entzinkung | Dezincification | Selektive Korrosion des Zinks aus Messing, Reststruktur porös |
| Faraday-Gesetz | Faraday's law | Zusammenhang zwischen Strommenge und Masseabnahme der Anode |
| Galvanische Korrosion | Galvanic corrosion | Korrosion durch Kontakt verschiedener Metalle im Elektrolyten |
| Galvanischer Isolator | Galvanic isolator | Gerät im Landstrom-PE zum Blockieren galvanischer Ströme |
| ICCP | Impressed Current Cathodic Protection | Kathodischer Schutz mit externer Stromquelle |
| Kathodischer Schutz | Cathodic protection | Schutz durch Verschiebung des Potenzials in kathodische Richtung |
| Lochfraß | Pitting corrosion | Lokale, tiefgehende Korrosion an passiven Metallen (Edelstahl) |
| MMO | Mixed Metal Oxide | Titan-basierte Beschichtung für ICCP-Anoden |
| Opferanode | Sacrificial anode | Unedleres Metall, das anstelle der Struktur korrodiert |
| Passivierung | Passivation | Bildung einer schützenden Oxidschicht (bei Anoden unerwünscht) |
| Referenzelektrode | Reference electrode | Stabile Elektrode als Bezugspunkt für Potenzialmessungen (Ag/AgCl, Zn) |
| Ruhepotenzial | Open circuit potential (OCP) | Potenzial eines Metalls ohne externen Stromfluss |
| Schutzpotenzial | Protection potential | Potenzial, bei dem Korrosion unterdrückt wird (z.B. −800 mV für Stahl) |
| Spaltkorrosion | Crevice corrosion | Korrosion in engen Spalten durch Sauerstoffverarmung |
| Streustrom | Stray current | Unbeabsichtigter Gleichstrom durch externe Quellen |
| Stromausbeute | Current efficiency | Anteil des Anodenstroms, der tatsächlich zum Schutz beiträgt (vs. Selbstkorrosion) |
| Stromkapazität | Current capacity | Ladungsmenge, die pro kg Anodenmaterial erzeugt werden kann (Ah/kg) |
| Treibpotenzial | Driving potential | Potenzialdifferenz zwischen Anode und zu schützendem Metall |
| Trenntransformator | Isolation transformer | Transformator zur galvanischen Trennung von Landstrom und Bordnetz |
| Überprotektion | Overprotection | Zu negatives Schutzpotenzial → Beschichtungsschäden, H₂-Versprödung |

> Confidence: `documented`

---

## 10. Verbindungstechnik

### 10.1 Bolt-On Anoden (Schraubmontage)

Die häufigste Befestigungsmethode bei Freizeityachten. Die Anode wird mit Edelstahl-Schrauben (A4-80, 316L) direkt auf die zu schützende Struktur oder den Rumpf geschraubt.

**Anforderungen an Schraubverbindungen:**

| Parameter | Spezifikation | Bewertung (0-100) |
|-----------|--------------|-------------------|
| Schraubenmaterial | A4-80 (316L), niemals A2 (304) | 100 bei 316L, 0 bei 304 |
| Mindestanzahl Schrauben | 2 (Anode <500g), 4 (Anode 500g–3kg), 6 (Anode >3kg) | 100 bei Einhaltung |
| Drehmoment M8 | 15–20 Nm in GFK, 20–25 Nm in Metall | Abzug 30 bei Über-/Unterdrehmoment |
| Drehmoment M10 | 25–30 Nm in GFK, 30–40 Nm in Metall | Abzug 30 bei Über-/Unterdrehmoment |
| Kontaktfläche | Metallisch blank, kein Antifouling, kein Primer | 100 bei blank, 0 bei beschichtet |
| Dichtung | Keine Isolierdichtung zwischen Anode und Schutzfläche | 100 bei direktem Kontakt |
| Gegenmutter innen | Erforderlich bei Durchgangsbohrung im Rumpf | 100 bei vorhanden |
| Sikaflex-Abdichtung | Um Bohrung herum, NICHT zwischen Anode und Kontaktfläche | 100 bei korrekt |

**Montagedetails Bolt-On:**
- Bohrdurchmesser: Schraubendurchmesser +0,5 mm (z.B. M8 → Bohrung 8,5 mm)
- Senkung für Schraubenkopf: nur bei aerodynamisch relevanten Positionen (Propeller, Ruderblatt)
- Federring oder Nordlock-Scheibe gegen Losdrehen durch Vibration
- Nyloc-Muttern (selbstsichernd) sind akzeptabel, Draht-Sicherung bei Motor-Anoden empfohlen
- Maximaler Abstand Anode zu geschütztem Bauteil: 300 mm (elektrisch leitende Verbindung)

**Typische Fehler Bolt-On:**
1. Antifouling unter der Anode belassen → kein elektrischer Kontakt → Score 0
2. Isolierscheiben verwendet → Anode elektrisch getrennt → wirkungslos
3. Schrauben aus Messing statt Edelstahl → Messing korrodiert → Anode fällt ab
4. Zu wenig Schrauben → Anode bricht bei Strömung ab → Verlust
5. Kein Dichtmittel um Bohrung → Wassereinbruch bei GFK-Rümpfen

> Confidence: `measured` (Hersteller-Montageanleitungen), `documented` (ABYC E-2)

### 10.2 Weld-On Anoden (Schweißmontage)

Ausschließlich bei Metall-Rümpfen (Stahl, Aluminium). Die Anode wird über einen Stahlkern (Cast-In Steel Core) direkt an die Rumpfstruktur geschweißt.

**Schweißverfahren nach Rumpfmaterial:**

| Rumpfmaterial | Schweißverfahren | Schweißzusatz | Schutzgas | Vorwärmung |
|---------------|-----------------|---------------|-----------|------------|
| Baustahl (S235) | MAG | SG2 (ER70S-6) | Mischgas 82/18 | Keine bis 10mm Wandstärke |
| Schiffbaustahl (A/B/D) | MAG | SG2 oder SG3 | Mischgas 82/18 | >15mm: 80°C |
| Edelstahl (316L) | WIG/TIG | 316LSi | Argon 100% | Keine |
| Aluminium (5083) | WIG/TIG oder MIG | AlMg4.5Mn (5183) | Argon 100% | Keine (max. 80°C) |

**Schweißnaht-Anforderungen:**
- Mindestnahtdicke: 4 mm (a-Maß)
- Nahtlänge gesamt: ≥60% des Kernumfangs
- Kehlnaht rundum bei Anoden >2 kg
- Schweißfolge: gegenüberliegende Heftstellen, dann umlaufend
- Abkühlzeit vor Wasserung: min. 24 Stunden
- Schweißnahtprüfung: Sichtprüfung nach ISO 5817, Klasse C

**Besonderheiten Aluminium-Rümpfe:**
- NIEMALS Zinkanoden auf Aluminium schweißen → galvanisches Element → beschleunigter Rumpf-Angriff
- Nur Aluminium-Anoden (Al-Zn-In-Legierung) auf Alu-Rümpfe
- Schweißnaht MUSS mit Alu-Grundierung + Epoxy-Primer nachbehandelt werden
- Wärmeeinflusszone (WEZ) maximal 50 mm → Festigkeitsverlust im 5083er begrenzen
- Anoden-Kernmaterial: verzinkter Stahl NICHT zulässig → nur Aluminium-Kern oder Edelstahl-Kern

**Typische Fehler Weld-On:**
1. Zinkanode auf Alu-Rumpf geschweißt → katastrophale Korrosion am Rumpf
2. Schweißnaht nicht grundiert → Korrosion an der Schweißnaht selbst
3. Zu kleine Naht → Anode bricht bei Seegang ab
4. Falsche Schweißfolge → Verzug des Rumpfblechs
5. Restfeuchtigkeit unter Anode → Blasenbildung beim Schweißen

> Confidence: `measured` (Schweißnormen DIN EN ISO 5817), `documented` (Klassifikationsgesellschaften)

### 10.3 Clamp-On Anoden (Klemmontage)

Klemmontage wird primär bei Wellenanlagen, Trimmklappen und Kühlwasserleitungen eingesetzt, wo keine Bohrung oder Schweißung möglich oder erwünscht ist.

**Typen und Anwendungsbereiche:**

| Typ | Anwendung | Wellendurchmesser | Gewicht | Befestigung |
|-----|-----------|-------------------|---------|-------------|
| Donut / Ring | Propellerwelle | 20–80 mm | 0,3–3,5 kg | 2× Allen-Schrauben |
| Halbrohr / Half-Shell | Propellerwelle, Stevenrohr | 25–100 mm | 0,5–5,0 kg | 2–4× Schrauben + Schelle |
| Collar | Saildrive-Bein | Modell-spezifisch | 0,4–1,2 kg | Klemmschrauben |
| Clip-On | Kühlwasserrohr (Cu) | 15–50 mm | 0,1–0,5 kg | Federklammer |
| Hufeisenform | Trimmklappe | Modell-spezifisch | 0,5–2,0 kg | 2× Schrauben |

**Montage-Anforderungen Clamp-On:**
- Kontaktfläche auf Welle: metallisch blank geschliffen (Körnung 80–120)
- Kein Fett, kein Korrosionsschutz zwischen Anode und Welle
- Klemmschrauben aus Edelstahl A4-80 (316L)
- Anzugsdrehmoment: gemäß Hersteller, typisch 8–12 Nm für M6-Klemmschrauben
- Axiale Position: 50–100 mm vor dem Stevenrohr-Austritt
- Clearance zum Propeller: min. 10 mm (Vibrationsfreiheit)
- Anti-Rotations-Sicherung: Set-Screw (Madenschraube) in Welle oder Klebstoff (Loctite 243)

**Typische Fehler Clamp-On:**
1. Welle nicht blank geschliffen → schlechter Kontakt → reduzierter Schutz
2. Anode zu nah am Propeller → Vibrationen → Lockerung
3. Klemmschrauben zu fest → Verformung der Anode → Rissbildung
4. Kein Anti-Rotationsmittel → Anode dreht sich und reibt sich ab
5. Falsche Größe → Spiel → kein flächiger Kontakt

> Confidence: `measured` (Hersteller-TDS), `documented` (ABYC E-2)

### 10.4 Bonding Wire (Masseverbindung / Potenzialausgleich)

Das Bonding-System ist das Nervensystem des kathodischen Schutzes. Ohne korrekte elektrische Verbindung aller Unterwasser-Metallteile kann die Anode nur das direkt kontaktierte Bauteil schützen.

**ABYC E-2 Bonding-Anforderungen:**

| Parameter | Anforderung | AYDI-Score bei Verstoß |
|-----------|-------------|----------------------|
| Leiterquerschnitt Hauptbus | ≥6 mm² (AWG 10) bei <10m LOA, ≥10 mm² (AWG 8) bei 10–20m, ≥16 mm² (AWG 6) bei >20m | Abzug 40 |
| Leiterquerschnitt Abzweig | ≥4 mm² (AWG 12) | Abzug 30 |
| Leitermaterial | Verzinntes Kupfer, flexibel (Litze, nicht starr) | Abzug 50 bei blankem Kupfer |
| Kabelschuhe | Verzinnte Kupfer-Ringkabelschuhe, gecrimpt + verlötet | Abzug 30 bei nur gecrimpt |
| Schraubverbindung | Edelstahl-Schraube in Bronze-/Edelstahl-Gewindebuchse | Abzug 40 bei selbstschneidend |
| Kontaktfläche | Metallisch blank, Kontaktpaste (z.B. Tef-Gel, Duralac) | Abzug 30 bei korrodiert |
| Schrumpfschlauch | Über Kabelschuh und Kabelende, marine-grade (adhesive-lined) | Abzug 20 bei fehlend |
| Max. Widerstand gesamt | <1 Ohm vom entferntesten Bauteil zur Anode | Abzug 50 bei >1 Ohm |

**Bonding-Topologie:**
```
Hauptbus (Bonding Bus Bar) — zentraler Kupferbalken, min. 6×25 mm
├── Motorblock (Erdung)
├── Propellerwelle (via Wellenerdungsbürste)
├── Ruderschaft (via Kabelschuh)
├── Seeventile (jedes einzeln angebunden)
├── Bugstrahlruder-Tunnel
├── Kielbolzen (bei Metallkiel)
├── Tankbefestigungen (Edelstahl)
├── Stevenrohr
├── Saildrive-Gehäuse
└── Anoden (Rumpfanoden als Endpunkt)
```

**Wellenerdungsbürste (Shaft Grounding Brush):**
- Typ: Silber-Graphit oder Kupfer-Graphit-Bürste auf Wellenschaft
- Position: im Maschinenraum, gut zugänglich
- Federdruck: 0,5–1,5 N (herstellerspezifisch)
- Kontaktwiderstand: <50 mΩ bei neuer Bürste
- Austauschintervall: alle 12–24 Monate oder bei >200 mΩ Widerstand
- Hersteller: Electro-Guard (USA), Shaft-i (UK), Morselt (NL)

**Messung des Bonding-Systems:**
1. Multimeter auf Widerstandsmessung (Ω)
2. Eine Messspitze auf Bonding-Bus
3. Zweite Messspitze auf jedes Unterwasser-Metallteil
4. Akzeptabel: <1 Ω (ABYC), <0,5 Ω (empfohlen)
5. Kritisch: >2 Ω → Korrosionsgefahr trotz Anoden

> Confidence: `measured` (ABYC E-2, ABYC E-11), `documented` (ISO 13297)

---

## 11. Technische Referenz & Berechnungen

### 11.1 Anodenauslegung nach DNV-RP-B401

Die Dimensionierung von Opferanoden-Systemen folgt international der Norm DNV-RP-B401 (Cathodic Protection Design). Die Berechnung bestimmt die erforderliche Anodenmasse, um eine definierte Schutzfläche über die gewünschte Lebensdauer zu schützen.

**Schritt 1: Schutzfläche bestimmen**

Die zu schützende Fläche A_c (m²) umfasst alle metallischen Unterwasserflächen:

```
A_c = A_hull + A_prop + A_shaft + A_rudder + A_keel + A_fittings + A_saildrive

Typische Werte für eine 12m-Segelyacht:
  A_hull (bei Stahlrumpf) = L × B × 0,7 (Benetzungsfaktor) ≈ 12 × 3,8 × 0,7 = 31,9 m²
  A_hull (bei GFK-Rumpf) = 0 m² (GFK ist nicht leitend → kein Schutz nötig)
  A_prop (3-Blatt, D=450mm) ≈ 0,12 m²
  A_shaft (D=30mm, L=1200mm) ≈ π × 0,030 × 1,2 = 0,113 m²
  A_rudder (Edelstahl-Schaft, benetzt) ≈ 0,05 m²
  A_keel (Gusseisen, benetzt) ≈ 0,8 m²
  A_saildrive (z.B. Volvo 130S) ≈ 0,15 m²
  A_fittings (Seeventile, Echolotgeber) ≈ 0,03 m²

  GFK-Yacht gesamt: A_c ≈ 1,26 m²
  Stahl-Yacht gesamt: A_c ≈ 33,2 m²
```

**Schritt 2: Stromdichte bestimmen**

Die erforderliche Schutzstromdichte i_c (mA/m²) hängt von Werkstoff, Wassertemperatur und Beschichtungszustand ab:

| Werkstoff | i_c initial (mA/m²) | i_c mean (mA/m²) | i_c final (mA/m²) | Quelle |
|-----------|---------------------|-------------------|--------------------|--------|
| Stahl, unbeschichtet, Nordsee | 150–200 | 70–90 | 90–120 | DNV-RP-B401 |
| Stahl, unbeschichtet, Mittelmeer | 100–150 | 50–70 | 70–90 | DNV-RP-B401 |
| Stahl, beschichtet (Epoxy) | 5–20 | 2–10 | 10–30 | DNV-RP-B401 |
| Bronze/Messing | 20–40 | 15–25 | 15–30 | NACE SP0176 |
| Edelstahl 316L | 5–20 | 5–10 | 5–15 | DNV-RP-B401 |
| Gusseisen | 30–60 | 20–40 | 25–50 | Erfahrungswerte |
| Aluminium 5083 | 5–15 | 3–8 | 5–10 | DNV-RP-B401 |

**Schritt 3: Gesamtschutrstrom berechnen**

```
I_c = Σ (A_i × i_c,i × f_coating,i)

  f_coating = Beschichtungsdegradationsfaktor
    Neubeschichtung: f_coating = 0,02 (98% der Fläche beschichtet)
    Nach 5 Jahren: f_coating = 0,05–0,10
    Stark degradiert: f_coating = 0,20–0,50
    Unbeschichtet: f_coating = 1,00

Beispiel 12m GFK-Segelyacht (Komponenten unbeschichtet):
  I_c = (0,12 × 25) + (0,113 × 10) + (0,05 × 10) + (0,8 × 35) + (0,15 × 20) + (0,03 × 20)
  I_c = 3,0 + 1,13 + 0,5 + 28,0 + 3,0 + 0,6
  I_c = 36,2 mA

Beispiel 15m Stahl-Segelyacht (Rumpf Epoxy-beschichtet, f=0,05):
  I_c = (45 × 70 × 0,05) + (0,15 × 25) + (0,14 × 10) + (0,06 × 10)
  I_c = 157,5 + 3,75 + 1,4 + 0,6
  I_c = 163,3 mA
```

**Schritt 4: Anodenmasse berechnen**

```
M = (I_c × t × 8760) / (u × ε)

  M = erforderliche Anodenmasse (kg)
  I_c = mittlerer Schutzstrom (A)
  t = Schutzlebensdauer (Jahre)
  8760 = Stunden pro Jahr
  u = Stromausbeute (utilization factor): 0,80–0,90
  ε = Stromkapazität (Ah/kg):
    Zink: 780 Ah/kg
    Aluminium (Al-Zn-In): 2.600 Ah/kg
    Magnesium: 1.230 Ah/kg

Beispiel 12m GFK-Yacht, Zink, 2 Jahre Schutz:
  M = (0,0362 × 2 × 8760) / (0,85 × 780)
  M = 634,2 / 663
  M = 0,96 kg → aufgerundet 1,0 kg Zink-Anoden

Beispiel 15m Stahl-Yacht, Aluminium, 3 Jahre Schutz:
  M = (0,1633 × 3 × 8760) / (0,85 × 2600)
  M = 4.291 / 2.210
  M = 1,94 kg → aufgerundet 2,5 kg (Sicherheitsfaktor 1,3)
```

**Schritt 5: Anodenverteilung**

```
Verteilungsregel:
  - Max. Abstand zwischen Anoden: 5 m (unbeschichteter Stahl), 10 m (beschichteter Stahl)
  - GFK-Yacht: Anoden direkt an/neben den zu schützenden Bauteilen
  - Symmetrische Verteilung Backbord/Steuerbord
  - Propeller-Anoden separat dimensionieren (eigener Stromkreis über Welle)

Beispiel 12m GFK-Yacht (1,0 kg Zink):
  2× Rumpfanode à 0,25 kg (Kielbereich, Bb+Stb)
  1× Wellenring 0,20 kg
  1× Propeller-Anode 0,15 kg (oder integriert in Propellernabe)
  1× Ruder-Anode 0,15 kg
  Gesamt: 1,0 kg ✓
```

### 11.2 Verbrauchsraten-Berechnung

Die Verbrauchsrate einer Opferanode bestimmt die Restlebensdauer und damit das Austauschintervall.

**Theoretische Verbrauchsrate:**

```
CR = I_c / (ε × ρ × A_anode)

  CR = Korrosionsrate (mm/Jahr)
  I_c = Schutzstrom (A)
  ε = Stromkapazität (Ah/kg)
  ρ = Dichte des Anodenmaterials (kg/dm³):
    Zink: 7,13 kg/dm³
    Aluminium: 2,73 kg/dm³
    Magnesium: 1,74 kg/dm³
  A_anode = Anodenoberfläche (dm²)
```

**Praktische Verbrauchsraten (Erfahrungswerte Mittelmeer):**

| Anoden-Typ | Gewicht | Mittlere Verbrauchsrate | Lebensdauer |
|------------|---------|------------------------|-------------|
| Zink Rumpfplatte 0,5 kg | 500 g | 250–350 g/Jahr | 12–18 Monate |
| Zink Rumpfplatte 1,0 kg | 1000 g | 300–400 g/Jahr | 24–36 Monate |
| Zink Wellenring 0,3 kg | 300 g | 200–300 g/Jahr | 10–15 Monate |
| Alu Rumpfplatte 0,5 kg | 500 g | 100–180 g/Jahr | 24–36 Monate |
| Alu Rumpfplatte 1,0 kg | 1000 g | 120–200 g/Jahr | 36–60 Monate |
| Magnesium Süßwasser 0,3 kg | 300 g | 200–300 g/Jahr | 8–14 Monate |

### 11.3 Oberflächenberechnung nach Anodenform

```
Flachanode (Platte): A = 2 × (L×B + L×H + B×H) - Kontaktfläche
  Typisch 200×100×25 mm: A = 2×(200×100 + 200×25 + 100×25) - 200×100
  A = 2×(20000 + 5000 + 2500) - 20000 = 55000 - 20000 = 35000 mm² = 0,035 m²

Zylindrische Anode (Wellenring): A = π × D_außen × L + π × (D_außen² - D_innen²) / 2
  Typisch D_außen=60mm, D_innen=30mm, L=50mm:
  A = π×60×50 + π×(3600-900)/2 = 9425 + 4241 = 13666 mm² = 0,0137 m²

Propelleranode (Halbschale): A ≈ 0,6 × π × D × L (60% exponiert)
  Typisch D=80mm, L=100mm:
  A ≈ 0,6 × π × 80 × 100 = 15080 mm² = 0,015 m²
```

### 11.4 Potenzialmessung — Referenzelektroden-Umrechnung

```
Umrechnungsformeln:
  E(Ag/AgCl) = E(Cu/CuSO₄) + 49 mV
  E(Ag/AgCl) = E(Zn) - 780 mV
  E(Ag/AgCl) = E(SHE) - 250 mV

Beispiel:
  Gemessen: -1050 mV vs. Ag/AgCl
  → vs. Cu/CuSO₄: -1050 - 49 = -1099 mV
  → vs. SHE: -1050 + 250 = -800 mV
  → vs. Zn: -1050 + 780 = -270 mV
```

> Confidence: `measured` (DNV-RP-B401:2021), `calculated` (Berechnungsbeispiele)

---

## 12. Einbau-/Austausch-Anleitung

### 12.1 Planung und Vorbereitung

**Wann müssen Anoden ausgetauscht werden?**
- Saisonstart: Standardinspektion bei jedem Kranen
- Verbrauch >50%: sofortiger Austausch
- Verbrauch >30%: Austausch beim nächsten Kranen einplanen
- Sichtbare Passivierung (weiße/graue Kruste ohne Materialabtrag): sofort tauschen
- Nach Reparatur am Bonding-System: alle Anoden prüfen
- Nach Revier-Wechsel (z.B. Ostsee → Mittelmeer): Anodentyp prüfen

**Erforderliches Werkzeug:**

| Werkzeug | Zweck | Alternative |
|----------|-------|-------------|
| Drehmomentschlüssel 5–40 Nm | Schrauben korrekt anziehen | Kalibrier-Ratsche |
| Schleifpapier 80er + 120er | Kontaktflächen blank schleifen | Drahtbürste (Edelstahl) |
| Multimeter | Bonding-Widerstand messen | — |
| Referenzelektrode Ag/AgCl | Schutzpotenzial messen | Cu/CuSO₄-Elektrode |
| Edelstahl-Schrauben A4-80 | Neue Befestigung (NIE alte Schrauben wiederverwenden) | — |
| Sikaflex 291 / 3M 4200 | Bohrungsabdichtung | Butylband |
| Loctite 243 (mittelfest) | Anti-Rotation Wellenring | Loctite 222 (leichtfest) |
| Isopropanol | Reinigung der Kontaktflächen | Aceton (Vorsicht: GFK-aggressiv) |
| Schrumpfschlauch marine | Bonding-Kabelschuhe abdichten | Selbstvulkanisierendes Band |

### 12.2 Schritt-für-Schritt: Rumpfanoden (Bolt-On)

**Schritt 1: Alte Anode entfernen (5–10 min)**
1. Boot im Kran oder auf dem Trailer, Unterwasserschiff zugänglich
2. Schrauben lösen (von außen), ggf. Gegenmutter innen lösen
3. Anode abnehmen, Schrauben ENTSORGEN (nicht wiederverwenden)
4. Restzustand dokumentieren: Foto + Gewicht der alten Anode
5. Verbrauch berechnen: (Originalgewicht - Restgewicht) / Originalgewicht × 100%

**Schritt 2: Kontaktfläche vorbereiten (10–15 min)**
1. Altes Antifouling um die Kontaktfläche herum 20 mm breit entfernen
2. Kontaktfläche mit 80er Schleifpapier blank schleifen bis Metall/Gelcoat sichtbar
3. Bei GFK-Rumpf: Gelcoat-Oberfläche reicht als Gegenfläche, sofern metallische Einlage (Backing Plate) vorhanden
4. Kontaktfläche mit Isopropanol entfetten
5. Bohrungen prüfen: sind sie noch rund, nicht ausgerissen?
6. Bei beschädigten Bohrungen: 2 mm aufbohren, neuen Dübel setzen oder Position versetzen

**Schritt 3: Neue Anode montieren (10–15 min)**
1. Neue Anode auspacken, Schutzfolie von der Kontaktfläche entfernen
2. Anoden-Kontaktfläche NICHT schleifen (Werksfinish optimal)
3. Sikaflex 291 dünn um jede Bohrung herum auftragen (Dichtring)
4. Anode ansetzen, Schrauben von außen durchstecken
5. Unterlegscheibe + Federring + Mutter von innen
6. Kreuzweise anziehen auf Solldrehmoment (M8: 15–20 Nm)
7. Überschüssiges Sikaflex abwischen
8. KEIN Antifouling auf die Anode auftragen

**Schritt 4: Bonding prüfen (5 min)**
1. Multimeter auf Widerstandsmessung
2. Eine Spitze auf die neue Anode
3. Andere Spitze auf den Bonding-Bus im Maschinenraum
4. Widerstand <1 Ω: OK
5. Widerstand >1 Ω: Bonding-Leitung prüfen, ggf. erneuern

**Schritt 5: Dokumentation**
1. Anodentyp, Hersteller, Gewicht notieren
2. Einbaudatum notieren
3. Foto der neuen Anode (Referenz für nächste Inspektion)
4. In AYDI-System eingeben → automatische Restlebensdauer-Berechnung

### 12.3 Schritt-für-Schritt: Wellenring-Anode (Clamp-On)

**Schritt 1: Vorbereitung (10 min)**
1. Propellerwelle reinigen: gesamten Bewuchs/Antifouling entfernen
2. Montagestelle mit 120er Schleifpapier blank schleifen (Umfang × 60 mm breit)
3. Mit Isopropanol entfetten
4. Position markieren: 50–100 mm vor Stevenrohr-Austritt

**Schritt 2: Montage (10 min)**
1. Anodenhälften um die Welle legen
2. Klemmschrauben handfest eindrehen
3. Anode ausrichten: zentrisch, keine Unwucht
4. Klemmschrauben kreuzweise auf 8–12 Nm anziehen
5. Madenschraube (Set-Screw) gegen die Welle drehen, Loctite 243 verwenden
6. Sitz prüfen: Anode darf sich NICHT drehen oder axial verschieben lassen

**Schritt 3: Kontrolle**
1. Welle von Hand drehen → Anode darf nirgends schleifen (Stevenrohr, Wellenhalter)
2. Clearance zum Propeller prüfen: min. 10 mm
3. Bonding via Wellenerdungsbürste prüfen (Widerstand Welle ↔ Bonding-Bus <0,5 Ω)

### 12.4 Schritt-für-Schritt: Saildrive-Anoden

**Volvo Penta Saildrive (120S, 130S, 150S):**
1. Original-Anode identifizieren: Volvo Penta P/N oder Aftermarket-Äquivalent
2. Alte Anode: 2 Schrauben lösen (M6 × 20, A4-80)
3. Kontaktfläche am Saildrive-Gehäuse reinigen (Drahtbürste, Edelstahl)
4. Neue Anode aufsetzen, Schrauben mit 8 Nm anziehen
5. WICHTIG: Bei Saildrive-Anoden die O-Ring-Dichtung am Saildrive-Bein prüfen
6. Saildrive-Zinkanoden-Ring (um das Bein): mit Montagepaste auftragen, Schrauben 6 Nm

**Yanmar Saildrive (SD20, SD40, SD50):**
1. Anode am Getriebe-Gehäuse: 1–2 Schrauben (M8 × 16)
2. Kontaktfläche reinigen
3. Neue Anode montieren, 10 Nm
4. Anode am Propeller-Konus: Konus abziehen, Ring-Anode aufschieben, Konus wieder montieren

### 12.5 Haul-Out-Checkliste Opferanoden

| Nr. | Prüfpunkt | OK-Kriterium | Aktion bei Fail |
|-----|-----------|-------------|-----------------|
| 1 | Visuelle Inspektion aller Anoden | Verbrauch <50%, keine Passivierung | Austausch |
| 2 | Gewicht jeder Anode | >50% des Originalgewichts | Austausch |
| 3 | Kontaktfläche Anode ↔ Rumpf | Metallischer Kontakt sichtbar | Blank schleifen, neu montieren |
| 4 | Schrauben / Klemmen | Fest, kein Spiel, kein Rost | Neue Schrauben |
| 5 | Bonding-Widerstand | <1 Ω (Anode ↔ Bus) | Bonding-Leitung erneuern |
| 6 | Schutzpotenzial (im Wasser) | −800 bis −1050 mV vs. Ag/AgCl (Stahl) | Anoden-Dimensionierung prüfen |
| 7 | Propeller-Zustand | Kein Lochfraß, keine Verfärbung | Ursache suchen (Streustrom?) |
| 8 | Wellenerdungsbürste | Kontaktwiderstand <200 mΩ | Bürste tauschen |
| 9 | Antifouling auf Anoden | KEIN Antifouling | Antifouling entfernen |
| 10 | ICCP-System (falls vorhanden) | Referenzelektrode intakt, Anzeige korrekt | Service beauftragen |

> Confidence: `documented` (Hersteller-Anleitungen), `measured` (ABYC E-2)

---

## 13. Lebensdauer und Alterungsmechanismen

### 13.1 Lebensdauer nach Anodenmaterial

**Zinkanoden (Zn-Al-Cd-Legierung nach MIL-A-18001K):**

| Parameter | Wert | Bedingung |
|-----------|------|-----------|
| Typische Lebensdauer | 12–18 Monate | Seewasser, Dauerliegeplatz, korrekt dimensioniert |
| Beste Lebensdauer | 24–30 Monate | Brackwasser, niedriger Salzgehalt, wenig Strömung |
| Schlechteste Lebensdauer | 6–10 Monate | Warmes Seewasser (>25°C), starke Strömung, Streustrom |
| Verbrauchsrate | 10–12 kg/A·Jahr | Bei 100% Stromausbeute (theoretisch) |
| Praktische Stromausbeute | 90–95% | MIL-A-18001K-konforme Legierung |
| Selbstkorrosionsrate | 5–10% des Gesamtverbrauchs | Erhöht bei Verunreinigungen (Fe, Cu) |

**Alterungsmechanismen Zink:**
1. **Gleichmäßige Auflösung** (gewünscht): Oberfläche löst sich kontinuierlich auf, hellgraue Oberfläche, Struktur bleibt erhalten → Score 100
2. **Interkristalline Korrosion**: Korngrenzen werden bevorzugt angegriffen → poröse Struktur, beschleunigte Auflösung → Score 60
3. **Passivierung**: Bildung einer dichten ZnO/Zn(OH)₂-Schicht → Strom wird blockiert → kein Schutz → Score 0
4. **Chunk Effect**: Große Stücke brechen ab (bei hohem Fe-Gehalt >14 ppm) → unkontrollierter Verlust → Score 20
5. **Calcareous Deposit**: Kalkablagerung (CaCO₃/Mg(OH)₂) bei Überprotektion → isoliert die Anode → Score 30

**Aluminiumanoden (Al-Zn-In-Legierung nach MIL-DTL-24779C):**

| Parameter | Wert | Bedingung |
|-----------|------|-----------|
| Typische Lebensdauer | 18–24 Monate | Seewasser, Dauerliegeplatz, korrekt dimensioniert |
| Beste Lebensdauer | 36–60 Monate | Brackwasser, gemäßigtes Klima |
| Schlechteste Lebensdauer | 10–14 Monate | Tropisches Seewasser (>28°C), starke Strömung |
| Verbrauchsrate | 3,2–3,5 kg/A·Jahr | Bei 100% Stromausbeute (theoretisch) |
| Praktische Stromausbeute | 85–95% | MIL-DTL-24779C-konforme Legierung |
| Selbstkorrosionsrate | 5–15% des Gesamtverbrauchs | Abhängig von In-Gehalt und Aktivierung |

**Alterungsmechanismen Aluminium:**
1. **Pitting-Korrosion** (gewünscht bei Anoden): Lokale Auflösung durch Indium-Aktivierung → gleichmäßige Oberfläche mit feinen Pits → Score 100
2. **Passivierung**: Dichte Al₂O₃-Schicht bildet sich ohne ausreichend In/Zn → Anode wird inert → Score 0
3. **Mud Cracking**: Oberflächenprodukte bilden Rissstruktur → erhöhte Selbstkorrosion → Score 50
4. **Grain Dezincification**: Zink diffundiert aus der Legierung → verarmte Randzone → Score 60
5. **Parasitäre Reaktionen**: H₂-Entwicklung an Al-Oberfläche → Stromausbeute sinkt → Score 40

**Magnesiumanoden (Mg-Al-Zn-Legierung nach ASTM B843):**

| Parameter | Wert | Bedingung |
|-----------|------|-----------|
| Typische Lebensdauer | 6–12 Monate | Süßwasser, korrekt dimensioniert |
| Beste Lebensdauer | 12–18 Monate | Kaltes Süßwasser (<10°C), geringer Mineralgehalt |
| Schlechteste Lebensdauer | 3–6 Monate | Warmes Süßwasser (>20°C), hoher Mineralgehalt |
| Verbrauchsrate | 7,0–8,5 kg/A·Jahr | Bei 100% Stromausbeute (theoretisch) |
| Praktische Stromausbeute | 50–60% | Deutlich geringer als Zn und Al |
| Selbstkorrosionsrate | 40–50% des Gesamtverbrauchs | Hauptnachteil von Magnesium |

**Alterungsmechanismen Magnesium:**
1. **Chunk-Effekt** (häufig): Große Stücke lösen sich → unkontrollierter Verbrauch → Score 30
2. **Negative Difference Effect**: Erhöhte H₂-Entwicklung bei steigendem Strom → Effizienz sinkt → Score 40
3. **Filiform Corrosion**: Fadenförmige Unterwanderungskorrosion → poröse Struktur → Score 50
4. **Galvanische Überaktivität**: In Seewasser zu starker Strom → Überprotektion des Schutzobjekts → Score 20
5. **Mikrogalvanische Zellen**: Al-Mn-Ausscheidungen als lokale Kathoden → beschleunigte Selbstkorrosion → Score 30

### 13.2 Umwelteinflüsse auf die Lebensdauer

| Faktor | Einfluss auf Verbrauchsrate | Faktor-Wert |
|--------|---------------------------|-------------|
| Wassertemperatur +10°C | +30–50% Verbrauch | ×1,3–1,5 |
| Salzgehalt +10 g/L | +10–20% Verbrauch | ×1,1–1,2 |
| Strömungsgeschwindigkeit +1 kn | +15–25% Verbrauch | ×1,15–1,25 |
| Sauerstoffgehalt +2 mg/L | +10–15% Verbrauch | ×1,1–1,15 |
| pH < 6,5 (sauer) | +20–40% Verbrauch | ×1,2–1,4 |
| pH > 8,5 (basisch) | Passivierungsrisiko | Variable |
| Verschmutzung (Sulfide) | −10–30% Schutzwirkung | ×0,7–0,9 |
| Biofouling auf Anode | −20–50% Schutzwirkung | ×0,5–0,8 |
| Streustrom (Marina) | +50–300% Verbrauch | ×1,5–4,0 |

### 13.3 Restlebensdauer-Abschätzung

**Gewichtsmethode (genaueste Methode bei Haul-Out):**
```
Restlebensdauer (Monate) = (Restgewicht / Verbrauchsrate_pro_Monat) × Korrekturfaktor

Korrekturfaktor:
  Anode >70% Restmasse: 1,0 (lineare Extrapolation gültig)
  Anode 50–70% Restmasse: 0,85 (beschleunigte Endphase)
  Anode 30–50% Restmasse: 0,70 (stark beschleunigt)
  Anode <30% Restmasse: 0,50 (Anode sofort tauschen)
```

**Dickenmessung (ohne Demontage):**
```
Restlebensdauer ≈ (aktuelle Dicke - Kerndicke) / (Originaldicke - Kerndicke) × Nenn-Lebensdauer

Beispiel Zink-Rumpfanode:
  Originaldicke: 25 mm, Kerndicke (Einlage): 3 mm, aktuelle Dicke: 15 mm
  → (15-3)/(25-3) × 18 Monate = 12/22 × 18 = 9,8 Monate Restlebensdauer
```

> Confidence: `measured` (Hersteller-TDS, MIL-Specs), `documented` (DNV-RP-B401), `estimated` (Erfahrungswerte)

---

## 14. Fehlerbild-Atlas

### Fehlerbild 1: Verbrauch >50% (Übermäßiger Anodenverschleiß)

- **Erscheinungsbild:** Anode deutlich kleiner als Originalform, Montage-Einlage teilweise sichtbar, poröse/raue Oberfläche
- **Häufigkeit:** 35% aller Inspektionsbefunde
- **Typische Ursache:** Unterdimensionierung, erhöhte Streuströme im Hafen, zu lange Standzeit
- **Betroffene Bereiche:** Rumpfanoden, Wellenringe, Propelleranoden
- **Risiko:** Schutzwirkung erlischt innerhalb von Wochen → galvanische Korrosion an Unterwasserbauteilen
- **Bewertung AYDI-Score:** Score 30 (bei 50–70% Verbrauch), Score 10 (bei >70% Verbrauch), Score 0 (bei >90%)
- **Sofortmaßnahme:** Anode bei nächstem Haul-Out ersetzen; bei >70% Verbrauch: baldiges Kranen einplanen
- **Langfristmaßnahme:** Anoden-Dimensionierung überprüfen, Streustrom-Messung durchführen
- **Visueller Befund Pipeline B:** `visual_high` — eindeutig erkennbar an Form und Größe
- **Differenzierung:** Normal bei Saisonende; kritisch wenn innerhalb von <6 Monaten erreicht
- **Referenz:** ABYC E-2, §E-2.7.3 (Inspection Criteria)
- **AYDI Confidence:** `visual_high` (Foto), `measured` (Gewicht)

### Fehlerbild 2: Passivierte Anode (keine Korrosion trotz Einbau)

- **Erscheinungsbild:** Anode erscheint wie neu, glatte Oberfläche mit weißer/grauer Kruste, kein sichtbarer Materialverlust
- **Häufigkeit:** 15% aller Inspektionsbefunde
- **Typische Ursache:** Minderwertige Legierung, falscher Wassertyp (Zink in Süßwasser), Antifouling auf Anode
- **Betroffene Bereiche:** Alle Anodenpositionen, besonders häufig bei No-Name-Produkten
- **Risiko:** HOCH — Anode bietet NULL Schutz trotz Vorhandensein → trügerische Sicherheit
- **Bewertung AYDI-Score:** Score 0 — funktionslose Anode
- **Sofortmaßnahme:** Anode sofort ersetzen mit normkonformer Legierung (MIL-A-18001K / MIL-DTL-24779C)
- **Langfristmaßnahme:** Lieferant wechseln, nur zertifizierte Anoden verwenden
- **Visueller Befund Pipeline B:** `visual_medium` — kann mit neuem Zustand verwechselt werden, Unterscheidung durch Einbaudatum
- **Differenzierung:** Von „neu eingebaut" unterscheiden durch Einbaudatum und leichte Verfärbung
- **Referenz:** DIN EN 12496, MIL-A-18001K (Legierungszusammensetzung)
- **AYDI Confidence:** `visual_medium` (Foto), `measured` (Gewicht + Potenzial)

### Fehlerbild 3: Falsche Legierung für Wassertyp

- **Erscheinungsbild:** Ungleichmäßiger Abtrag, weiße Flecken (Zink in Brackwasser), aufgeblähte Oberfläche (Mg in Seewasser)
- **Häufigkeit:** 10% aller Inspektionsbefunde
- **Typische Ursache:** Zink in Süßwasser/Brackwasser (<15 PSU), Magnesium in Seewasser, Aluminium in Süßwasser
- **Betroffene Bereiche:** Alle Anodenpositionen
- **Risiko:** Mittel bis Hoch — entweder kein Schutz (passiviert) oder übermäßiger Verbrauch
- **Bewertung AYDI-Score:** Score 20 (teilweise Schutzwirkung) bis Score 0 (passiviert)
- **Sofortmaßnahme:** Richtige Legierung für das Revier beschaffen und einbauen
- **Langfristmaßnahme:** Revier-spezifische Anoden-Empfehlung in AYDI hinterlegen
- **Visueller Befund Pipeline B:** `visual_medium` — Abweichung vom Normalverbrauch erkennbar
- **Differenzierung:** Salzgehaltmessung des Reviers erforderlich für eindeutige Diagnose
- **Referenz:** ABYC E-2, §E-2.5.2 (Anode Selection)
- **AYDI Confidence:** `visual_medium` (Foto), `documented` (Revier-Daten)

### Fehlerbild 4: Abgelöste/lose Anode

- **Erscheinungsbild:** Anode hängt an einer Schraube, ist verschoben, fehlt komplett (nur Bohrungen sichtbar)
- **Häufigkeit:** 8% aller Inspektionsbefunde
- **Typische Ursache:** Korrodierte Schrauben (304 statt 316L), zu wenige Schrauben, Vibration, Strömungskräfte
- **Betroffene Bereiche:** Rumpfanoden, Trimmklappenanoden, Wellenringe
- **Risiko:** HOCH — kein galvanischer Kontakt = null Schutzwirkung
- **Bewertung AYDI-Score:** Score 0 — keine Schutzwirkung
- **Sofortmaßnahme:** Anode sichern oder ersetzen, Schrauben erneuern (316L)
- **Langfristmaßnahme:** Befestigungskonzept überprüfen, Schraubenqualität upgraden
- **Visueller Befund Pipeline B:** `visual_high` — fehlende oder verschobene Anode klar erkennbar
- **Differenzierung:** Von „nie montiert" unterscheiden durch Bohrlöcher und Montagespuren
- **Referenz:** ABYC E-2, Hersteller-Montageanleitungen
- **AYDI Confidence:** `visual_high` (Foto)

### Fehlerbild 5: Korrodierter Bonding-Draht

- **Erscheinungsbild:** Grünspan auf Kupferlitze, gebrochene Einzeldrähte, lose Kabelschuhe, oxidierte Kontaktflächen
- **Häufigkeit:** 20% aller Inspektionsbefunde (häufigster versteckter Fehler)
- **Typische Ursache:** Unverschirmtes Kupfer statt verzinnter Litze, fehlender Schrumpfschlauch, Salzwasserkontakt
- **Betroffene Bereiche:** Maschinenraum, Bilge, Stevenrohr-Bereich
- **Risiko:** HOCH — hoher Widerstand im Bonding-System → einzelne Bauteile ungeschützt
- **Bewertung AYDI-Score:** Score 20 (partiell korrodiert), Score 0 (gebrochen)
- **Sofortmaßnahme:** Widerstand messen; >1 Ω → Leitung erneuern
- **Langfristmaßnahme:** Gesamtes Bonding-System auf verzinntes Kupfer upgraden
- **Visueller Befund Pipeline B:** `visual_medium` — Grünspan erkennbar, Zustand schwer einschätzbar
- **Differenzierung:** Oberflächliche Patina vs. strukturelle Korrosion durch Widerstandsmessung
- **Referenz:** ABYC E-11 (AC and DC Electrical Systems), ABYC E-2
- **AYDI Confidence:** `visual_medium` (Foto), `measured` (Widerstand)

### Fehlerbild 6: Streustrombeschädigung

- **Erscheinungsbild:** Extreme Anodenauflösung auf einer Seite, Lochfraß am Propeller/Welle, Verfärbung an Seeventilen
- **Häufigkeit:** 12% aller Inspektionsbefunde in Marinas
- **Typische Ursache:** Fehlerhafte Landstrom-Installation benachbarter Boote, eigene Isolationsfehler, schlecht geerdete Marina-Steganlage
- **Betroffene Bereiche:** Seite zum Steg (Landstromseitig), Propellerwelle, Ruder
- **Risiko:** KRITISCH — Streustrom kann Metallverlust 10× schneller als normal verursachen
- **Bewertung AYDI-Score:** Score 5 (aktiver Streustrom nachgewiesen)
- **Sofortmaßnahme:** Landstromstecker ziehen, Galvanischer Isolator oder Trenntransformator einbauen
- **Langfristmaßnahme:** Galvanischen Isolator (ABYC A-28) permanent installieren, Streustromüberwachung
- **Visueller Befund Pipeline B:** `visual_high` — asymmetrischer Abtrag ist Leitsymptom
- **Differenzierung:** Von normalem Verbrauch durch Asymmetrie und Geschwindigkeit unterscheidbar
- **Referenz:** ABYC E-2, ABYC A-28 (Galvanic Isolators)
- **AYDI Confidence:** `visual_high` (Foto), `measured` (Streustrommessung)

### Fehlerbild 7: Mit Antifouling übermalte Anode

- **Erscheinungsbild:** Anode in Rumpffarbe (Antifouling), glatte Oberfläche, kein sichtbarer Abtrag
- **Häufigkeit:** 18% aller DIY-Inspektionsbefunde
- **Typische Ursache:** Unwissenheit des Eigners, Werft hat Anoden mitgestrichen, Antifouling-Roller über Anode gezogen
- **Betroffene Bereiche:** Rumpfanoden, selten Propelleranoden
- **Risiko:** HOCH — Antifouling isoliert die Anode elektrisch → null Schutzwirkung
- **Bewertung AYDI-Score:** Score 0 — elektrisch isolierte Anode
- **Sofortmaßnahme:** Antifouling mechanisch von der Anode entfernen (Schaber, Drahtbürste)
- **Langfristmaßnahme:** Werft-Anweisung: Anoden beim Antifouling-Auftrag abkleben
- **Visueller Befund Pipeline B:** `visual_high` — Farbgleichheit Anode/Rumpf ist eindeutiges Zeichen
- **Differenzierung:** Bewusst angestrichene vs. versehentlich übermalte Anoden
- **Referenz:** ABYC E-2, §E-2.6.1 (Coatings)
- **AYDI Confidence:** `visual_high` (Foto)

### Fehlerbild 8: Falsche Anode für Wassertyp

- **Erscheinungsbild:** Zink in Süßwasser: dicke weiße ZnO-Kruste, kein Schutz; Magnesium in Seewasser: rapid aufgelöst
- **Häufigkeit:** 8% aller Inspektionsbefunde bei Reverwechslern
- **Typische Ursache:** Boot vom Meer in den See verlegt (oder umgekehrt), keine Anoden-Anpassung
- **Betroffene Bereiche:** Alle Anodenpositionen
- **Risiko:** Hoch — entweder Überprotektion (Mg in See → Beschichtungsschäden) oder Nullschutz (Zn in Süßwasser)
- **Bewertung AYDI-Score:** Score 10 (falscher Typ, teilweise Schutz) bis Score 0 (komplett passiviert)
- **Sofortmaßnahme:** Alle Anoden gegen den richtigen Typ für das aktuelle Revier austauschen
- **Langfristmaßnahme:** Revier in AYDI hinterlegen → automatische Warnung bei Anoden-Mismatch
- **Visueller Befund Pipeline B:** `visual_medium` — Symptome ähneln Passivierung
- **Differenzierung:** Legierung prüfen (Stempelung auf Anode oder Einkaufsbeleg)
- **Referenz:** ABYC E-2, §E-2.5 (Water Type Selection)
- **AYDI Confidence:** `visual_medium` (Foto), `documented` (Revier-Salinität)

### Fehlerbild 9: Kalkablagerung (Calcareous Deposit)

- **Erscheinungsbild:** Weiße bis hellbraune, harte Kruste auf Anode und benachbarten Metallflächen
- **Häufigkeit:** 10% aller Inspektionsbefunde, häufiger im Mittelmeer
- **Typische Ursache:** Überprotektion (zu viel Anodenfläche), sehr hoher pH lokal, warmes kalkhaltiges Wasser
- **Betroffene Bereiche:** Rumpfanoden, Propeller, Ruderblatt
- **Risiko:** Mittel — Kalkschicht kann isolierend wirken, reduziert aber langfristig Strombedarf
- **Bewertung AYDI-Score:** Score 50 (leichte Ablagerung, Schutz noch vorhanden) bis Score 20 (starke Isolierung)
- **Sofortmaßnahme:** Kalkschicht mechanisch entfernen (Spachtel, Essig-Lösung)
- **Langfristmaßnahme:** Anoden-Dimensionierung reduzieren, ICCP mit Potenzialregelung erwägen
- **Visueller Befund Pipeline B:** `visual_high` — weiße Kruste klar erkennbar
- **Differenzierung:** Von Passivierung unterscheiden: Kalkablagerung ist hart und bröckelig, Passivierung glatt
- **Referenz:** DNV-RP-B401, §6.3 (Calcareous Deposits)
- **AYDI Confidence:** `visual_high` (Foto)

### Fehlerbild 10: Galvanisches Paar (bimetallische Korrosion)

- **Erscheinungsbild:** Selektive Korrosion am unedleren Metall, z.B. Lochfraß am Alu-Saildrive neben Bronze-Propeller
- **Häufigkeit:** 15% aller Inspektionsbefunde an Antriebssystemen
- **Typische Ursache:** Ungenügende Anodendimensionierung, fehlendes Bonding, ungeeignete Materialpaarung
- **Betroffene Bereiche:** Propeller/Welle-Übergang, Saildrive/Propeller, Ruderkoker
- **Risiko:** HOCH — Lochfraß kann zu Strukturversagen führen (Wellenbruch, Ruderkoker-Leck)
- **Bewertung AYDI-Score:** Score 15 (aktive bimetallische Korrosion sichtbar)
- **Sofortmaßnahme:** Bonding prüfen, Anoden vergrößern, galvanische Trennung prüfen
- **Langfristmaßnahme:** Materialpaarung optimieren, Isolierflansche einsetzen wo möglich
- **Visueller Befund Pipeline B:** `visual_high` — Lochfraß und Verfärbung klar erkennbar
- **Differenzierung:** Von Erosion unterscheiden: galvanische Korrosion ist positionsabhängig (am Kontaktbereich)
- **Referenz:** ISO 8044, DIN EN ISO 21457 (Materialauswahl)
- **AYDI Confidence:** `visual_high` (Foto), `measured` (Potenzialmessung)

### Fehlerbild 11: ICCP-System-Fehler

- **Erscheinungsbild:** Korrosion trotz ICCP-System, Referenzelektrode verschmutzt, Titan-Anode beschädigt, Steuergerät zeigt Fehler
- **Häufigkeit:** 5% aller Inspektionsbefunde (nur bei ICCP-ausgestatteten Yachten)
- **Typische Ursache:** Defekte Referenzelektrode, durchgebrannte Titan-Anode, Steuergeräte-Ausfall, Kabelbruch
- **Betroffene Bereiche:** Gesamtes Unterwasserschiff bei ICCP-Ausfall
- **Risiko:** KRITISCH — ICCP-Ausfall bei Yacht ohne Backup-Opferanoden = totaler Schutzverlust
- **Bewertung AYDI-Score:** Score 0 (ICCP-Totalausfall ohne Backup), Score 40 (Teilausfall mit Backup-Anoden)
- **Sofortmaßnahme:** Backup-Opferanoden montieren, ICCP-Service beauftragen
- **Langfristmaßnahme:** Redundanzkonzept: ICCP + passive Opferanoden als Backup
- **Visueller Befund Pipeline B:** `visual_low` — ICCP-Fehler nur am Steuergerät erkennbar, nicht am Unterwasserschiff
- **Differenzierung:** ICCP-Ausfall von Unterdimensionierung durch Steuergerät-Log unterscheiden
- **Referenz:** DNV-RP-B401, ABYC E-2 (ICCP Systems)
- **AYDI Confidence:** `visual_low` (Foto UW-Schiff), `measured` (Steuergerät-Daten)

### Fehlerbild 12: Fehlende Anode

- **Erscheinungsbild:** Keine Anoden am Unterwasserschiff, nur leere Bohrlöcher oder keine Montagespuren
- **Häufigkeit:** 5% aller Inspektionsbefunde (häufig bei Gebrauchtboot-Kauf)
- **Typische Ursache:** Nie montiert, abgefallen und nicht bemerkt, bei Antifouling-Erneuerung vergessen
- **Betroffene Bereiche:** Gesamtes Unterwasserschiff ungeschützt
- **Risiko:** KRITISCH — keinerlei kathodischer Schutz → Korrosion beginnt sofort
- **Bewertung AYDI-Score:** Score 0 — kein Schutz vorhanden
- **Sofortmaßnahme:** Sofort Anoden montieren, bei Metallrumpf: Haul-Out innerhalb von 2 Wochen
- **Langfristmaßnahme:** Anoden-Wartungsplan in AYDI hinterlegen, Erinnerung vor Saisonstart
- **Visueller Befund Pipeline B:** `visual_high` — Fehlen von Anoden klar erkennbar, Bohrlöcher als Indiz
- **Differenzierung:** „Nie vorhanden" vs. „abgefallen" durch Bohrlöcher und Montagespuren
- **Referenz:** ABYC E-2
- **AYDI Confidence:** `visual_high` (Foto)

> Confidence: `documented` (ABYC E-2, DNV-RP-B401), `visual_high` / `visual_medium` (Pipeline B Referenz)

---

## 15. Fehlerbehebungs-Leitfaden

### Problem 1: Übermäßig schneller Anodenverbrauch

**Symptom:** Anoden sind nach 3–6 Monaten >50% verbraucht (Sollwert: 12–18 Monate für Zink).

**Diagnose-Ablauf:**
1. **Streustrom messen:** Multimeter (mA-Bereich) zwischen Bonding-Bus und Wasser, alle Landstromverbraucher einzeln schalten
   - >50 mA DC: Streustrom-Problem bestätigt
   - Quelle isolieren: eigenes Boot oder Nachbar?
2. **Bonding-Widerstand messen:** Jedes Unterwasser-Metallteil → Bonding-Bus
   - >1 Ω: Bonding-Problem → niederohmige Bauteile ziehen mehr Strom
3. **Anoden-Fläche vs. Schutzfläche prüfen:** Ist die Yacht aufgerüstet worden (neuer Propeller, zusätzliche Seeventile)?
4. **Wassertemperatur und Salzgehalt des Reviers prüfen**

**Lösungen:**
| Ursache | Maßnahme | Kosten (EUR) | Score-Verbesserung |
|---------|----------|-------------|-------------------|
| Streustrom eigenes Boot | Isolationsfehler finden und beheben | 100–500 | +60 |
| Streustrom Nachbar/Marina | Galvanischer Isolator installieren | 250–600 | +50 |
| Bonding defekt | Bonding-System erneuern (verzinntes Cu) | 300–1.200 | +40 |
| Unterdimensioniert | Anoden-Masse +50% erhöhen | 50–200 | +30 |
| Warmes Revier | Kürzeres Austauschintervall akzeptieren oder auf Alu umsteigen | 80–300 | +20 |

### Problem 2: Keine Anodenkorrosion (Anode löst sich nicht auf)

**Symptom:** Anode sieht nach 12+ Monaten wie neu aus, ABER Korrosion an geschützten Bauteilen sichtbar.

**Diagnose-Ablauf:**
1. **Antifouling auf Anode?** → Visuell prüfen, Farbe abkratzen
2. **Bonding-Verbindung prüfen:** Widerstand Anode ↔ geschütztes Bauteil
   - >2 Ω oder ∞: kein elektrischer Kontakt
3. **Legierung prüfen:** Stempelung auf Anode, Kaufbeleg
   - Billige Anoden enthalten oft zu wenig Al/Cd (Zink) oder In (Aluminium) → Passivierung
4. **Wassertyp prüfen:** Zink passiviert in Süßwasser (<5 PSU Salinität)
5. **Potenzialmessung:** Anodenpotenzial vs. Referenzelektrode
   - Zink: muss −1000 bis −1050 mV vs. Ag/AgCl zeigen
   - Wenn positiver als −950 mV: Anode ist passiviert

**Lösungen:**
| Ursache | Maßnahme | Kosten (EUR) | Score-Verbesserung |
|---------|----------|-------------|-------------------|
| Antifouling auf Anode | Antifouling entfernen, freilegen | 0 | +80 |
| Kein Bonding-Kontakt | Kontaktfläche blank schleifen, neu montieren | 20–50 | +80 |
| Minderwertige Legierung | Zertifizierte Anode kaufen (MIL-Spec) | 30–100 | +70 |
| Falscher Wassertyp | Richtige Legierung wählen (Mg für Süßwasser) | 30–80 | +70 |
| Isolierscheibe montiert | Isolierscheibe entfernen, direkten Kontakt herstellen | 0 | +80 |

### Problem 3: Lochfraß (Pitting) am Propeller trotz Anoden

**Symptom:** Propellerblätter zeigen punktuelle Vertiefungen (Pitting), Anoden sind vorhanden und teilweise verbraucht.

**Diagnose-Ablauf:**
1. **Bonding Propellerwelle prüfen:** Wellenerdungsbürste vorhanden und funktionsfähig?
   - Kontaktwiderstand Welle ↔ Bus: muss <200 mΩ sein
2. **Propellermaterial identifizieren:** Bronze (gut), Edelstahl (empfindlich für Spaltkorrosion), Aluminium (empfindlich)
3. **Streustrom prüfen:** Speziell AC-Streustrom kann Pitting an Bronze verursachen, auch bei funktionierender DC-Protektion
4. **Kavitation ausschließen:** Pitting durch Kavitation hat andere Morphologie (glatte, runde Krater vs. raue Korrosionspits)
5. **Potenzialmessung am Propeller:** Schutzpotenzial muss −800 bis −1050 mV vs. Ag/AgCl erreichen

**Lösungen:**
| Ursache | Maßnahme | Kosten (EUR) | Score-Verbesserung |
|---------|----------|-------------|-------------------|
| Wellenerdungsbürste defekt | Neue Bürste einbauen (Electro-Guard, Shaft-i) | 150–400 | +50 |
| AC-Streustrom | AC-Streustrom-Blocker oder Trenntransformator | 400–2.500 | +60 |
| Unzureichende Anodenmasse | Propelleranode + Wellenring nachrüsten | 60–200 | +40 |
| Kavitation | Propeller neu berechnen/wuchten | 200–800 | +30 |
| Spaltkorrosion (Edelstahl) | Spalte abdichten, Propeller polieren | 100–300 | +30 |

### Problem 4: Streustrom-Diagnose und -Behebung

**Symptom:** Asymmetrischer Anodenverbrauch, schneller Verbrauch nur auf einer Bootsseite, Lochfraß an einzelnen Komponenten.

**Diagnose-Ablauf:**
1. **DC-Streustrom messen:**
   - Amperemeter in Reihe zwischen Bonding-Bus und Unterwasser-Metallteil
   - Alle Verbraucher aus → Reststrom messen
   - Verbraucher einzeln einschalten → Stromanstieg = Quelle
2. **Landstrom-Test:**
   - Streustrom mit Landstrom vs. ohne Landstrom messen
   - Differenz = landstrominduzierter Streustrom
3. **Nachbarboot-Test:**
   - Eigenes Boot stromfrei, Nachbar-Landstrom an/aus
   - Potenzialänderung am eigenen Bonding = Nachbar-Streustrom
4. **AC-Streustrom:**
   - Multimeter auf AC mA zwischen Bonding-Bus und Wasser
   - >30 mA AC: Problem, Isolationstransformator nötig

**Lösungen:**
| Ursache | Maßnahme | Kosten (EUR) | Score-Verbesserung |
|---------|----------|-------------|-------------------|
| Eigener Isolationsfehler | Defektes Gerät finden und reparieren | 100–500 | +70 |
| Nachbar-Streustrom | Galvanischer Isolator (z.B. ProMariner ProSafe) | 250–600 | +50 |
| Marina-Erdungsproblem | Marina informieren, Trenntransformator nutzen | 400–2.500 | +60 |
| AC-Leckstrom | Trenntransformator (z.B. Victron 3600W) | 1.200–3.500 | +70 |
| Wechselrichter-Erdung | Erdung korrekt nach ABYC E-11 herstellen | 100–400 | +50 |

### Problem 5: Bonding-System-Fehler (systemischer Schutzausfall)

**Symptom:** Mehrere Unterwasserbauteile zeigen gleichzeitig Korrosion, Anoden sind kaum verbraucht.

**Diagnose-Ablauf:**
1. **Bonding-Bus visuell inspizieren:**
   - Korrosion an Bus-Bar?
   - Lose Schrauben?
   - Gebrochene Leitungen?
2. **Systematische Widerstandsmessung:**
   - Jedes Bauteil einzeln gegen Bonding-Bus messen
   - Alle Werte >1 Ω: Hauptleitung oder Bus-Bar defekt
   - Einzelne Werte >1 Ω: lokale Leitung defekt
3. **Bonding-Bus-Material prüfen:**
   - Kupfer blank? → Korrosion
   - Aluminium? → NICHT zulässig für Bonding
   - Verzinnt? → korrekt
4. **Kabelschuhe prüfen:**
   - Gecrimpt + gelötet? → korrekt
   - Nur geklemmt? → hoher Übergangswiderstand

**Lösungen:**
| Ursache | Maßnahme | Kosten (EUR) | Score-Verbesserung |
|---------|----------|-------------|-------------------|
| Korrodierte Bus-Bar | Neue verzinnte Kupfer-Busbar installieren | 80–200 | +60 |
| Lose Schraubverbindungen | Alle Verbindungen nachziehen, Kontaktpaste | 20–50 | +50 |
| Gebrochene Leitungen | Defekte Leitungen ersetzen (verzinntes Cu, 6–16 mm²) | 100–400 | +60 |
| Falsche Kabelschuhe | Alle Schuhe auf Crimp+Löt umrüsten | 50–150 | +40 |
| Fehlende Bauteile im Bonding | Alle UW-Metallteile einzeln anschließen | 150–500 | +50 |

> Confidence: `documented` (ABYC E-2, ABYC E-11), `measured` (Diagnose-Messwerte)

---

## 16. FAQ — Häufig gestellte Fragen

### OA-001: Welche Anodenlegierung brauche ich?
**Frage:** Welche Anoden soll ich für mein Boot verwenden — Zink, Aluminium oder Magnesium?
**Antwort:** Die Wahl hängt vom Wassertyp ab: Zink für Seewasser (>20 PSU), Aluminium für Brackwasser und Seewasser (universell, 5–35 PSU), Magnesium ausschließlich für Süßwasser (<5 PSU). Im Zweifelsfall: Aluminium ist die sicherste Wahl.
**Confidence:** `documented` (ABYC E-2)

### OA-002: Wie oft müssen Anoden gewechselt werden?
**Frage:** In welchem Intervall sollten Opferanoden ersetzt werden?
**Antwort:** Faustregel: Zink alle 12–18 Monate, Aluminium alle 18–24 Monate, Magnesium alle 6–12 Monate. Entscheidend ist der tatsächliche Verbrauch: Austausch bei >50% Gewichtsverlust. Bei jedem Kranen kontrollieren.
**Confidence:** `measured` (Hersteller-TDS)

### OA-003: Darf ich Antifouling auf Anoden auftragen?
**Frage:** Mein Werft hat die Anoden beim Antifouling-Streichen mitgestrichen. Ist das ein Problem?
**Antwort:** Ja, das ist ein schwerwiegender Fehler. Antifouling isoliert die Anode elektrisch und verhindert jede Schutzwirkung. Anoden müssen IMMER freigelassen oder abgeklebt werden. Sofort entfernen.
**Confidence:** `documented` (ABYC E-2, §E-2.6.1)

### OA-004: Kann ich verschiedene Anodenlegierungen am selben Boot mischen?
**Frage:** Ich habe noch Zinkanoden übrig, aber mein neuer Propeller braucht eine Alu-Anode. Kann ich beides verwenden?
**Antwort:** Das Mischen verschiedener Anodenlegierungen wird nicht empfohlen. Die unterschiedlichen Potenziale können zu einer gegenseitigen Beeinflussung führen. Idealerweise ein einheitliches Anodensystem verwenden. Ausnahme: getrennte Systeme (z.B. Rumpf Zink, Motor-Kühlwasser Zink separat) sind akzeptabel.
**Confidence:** `documented` (ABYC E-2)

### OA-005: Was ist ein galvanischer Isolator und brauche ich einen?
**Frage:** Mein Nachbar sagt, ich brauche einen galvanischen Isolator. Was ist das?
**Antwort:** Ein galvanischer Isolator (GI) wird in die Schutzleiterverbindung des Landstroms eingebaut. Er blockiert niedrige Gleichströme (galvanische Ströme), lässt aber den Schutzleiter bei einem Fehlerfall (AC) durchleiten. Empfohlen für jede Yacht mit Landstromanschluss in einer Marina. Kosten: 250–600 EUR.
**Confidence:** `documented` (ABYC A-28)

### OA-006: Mein Propeller zeigt Lochfraß — sind die Anoden schuld?
**Frage:** Trotz vorhandener Anoden hat mein Propeller Lochfraß. Was ist die Ursache?
**Antwort:** Häufigste Ursache: Die Propellerwelle hat keinen oder schlechten Bonding-Kontakt zum Anodensystem. Eine Wellenerdungsbürste (Shaft Grounding Brush) ist erforderlich. Außerdem Streustrom als Ursache prüfen. Kontaktwiderstand Welle ↔ Bonding-Bus muss <200 mΩ betragen.
**Confidence:** `measured` (ABYC E-2)

### OA-007: Wie messe ich, ob meine Anoden funktionieren?
**Frage:** Gibt es eine Möglichkeit, die Schutzwirkung meiner Anoden zu überprüfen?
**Antwort:** Ja. Mit einer Ag/AgCl-Referenzelektrode und einem hochohmigen Multimeter das Potenzial zwischen geschütztem Metall und Referenzelektrode im Wasser messen. Stahl: −800 bis −1050 mV, Bronze/Messing: −550 bis −650 mV. Liegt der Wert positiver, ist der Schutz unzureichend.
**Confidence:** `measured` (DNV-RP-B401)

### OA-008: Was kostet ein kompletter Anoden-Satz für eine 10m-Segelyacht?
**Frage:** Mit welchen Kosten muss ich für einen Komplett-Anodensatz rechnen?
**Antwort:** Für eine typische 10m-Segelyacht mit Saildrive: 2× Rumpfanode (je 15–25 EUR), 1× Saildrive-Anode (25–45 EUR), 1× Propelleranode (20–35 EUR) = ca. 75–130 EUR für Zinkanoden, 100–180 EUR für Aluminiumanoden. Dazu Edelstahl-Schrauben ca. 15–25 EUR.
**Confidence:** `estimated` (Marktpreise 2025/2026)

### OA-009: Stimmt es, dass Aluminium-Anoden besser sind als Zink?
**Frage:** Ich höre immer häufiger, man solle auf Alu-Anoden umsteigen. Warum?
**Antwort:** Aluminium-Anoden (Al-Zn-In) haben gegenüber Zink drei Vorteile: 3,4× höhere Stromkapazität pro kg, funktionieren auch in Brackwasser, und sind umweltfreundlicher (kein Cadmium). Nachteil: leicht höherer Preis (+30–50%). Für Yachten in Revieren mit wechselndem Salzgehalt sind Alu-Anoden die bessere Wahl.
**Confidence:** `documented` (MIL-DTL-24779C)

### OA-010: Können Opferanoden eine Elektrolyse ersetzen?
**Frage:** Brauche ich trotz Anoden noch ein ICCP-System?
**Antwort:** Für Yachten unter 20m LOA reichen korrekt dimensionierte Opferanoden in der Regel aus. ICCP lohnt sich ab ca. 20m LOA oder bei großen Schutzflächen (Stahlrumpf >50 m²), wo die benötigte Anodenmasse unpraktisch wird. Einige Eigner nutzen ICCP + Opferanoden als Backup.
**Confidence:** `documented` (DNV-RP-B401)

### OA-011: Muss ich in Süßwasser überhaupt Anoden haben?
**Frage:** Mein Boot liegt nur im See. Brauche ich trotzdem Anoden?
**Antwort:** Ja! Galvanische Korrosion tritt auch in Süßwasser auf, allerdings langsamer. Magnesium-Anoden sind für Süßwasser erforderlich, da Zink und Aluminium in Süßwasser passivieren. Ohne Anoden kann ein Bronze-Seeventil in Süßwasser in 3–5 Jahren gefährlich korrodieren.
**Confidence:** `documented` (ABYC E-2)

### OA-012: Was passiert bei zu vielen Anoden (Überprotektion)?
**Frage:** Kann man auch zu viele Anoden haben?
**Antwort:** Ja. Überprotektion (Potenzial negativer als −1100 mV vs. Ag/AgCl bei Stahl) kann zu Beschichtungsablösung (Antifouling, Epoxy-Primer), Wasserstoffversprödung bei hochfesten Stählen und verstärkter Kalkablagerung führen. Korrekte Dimensionierung ist wichtig.
**Confidence:** `measured` (DNV-RP-B401)

### OA-013: Wie erkenne ich eine qualitativ hochwertige Anode?
**Frage:** Worauf sollte ich beim Kauf von Anoden achten?
**Antwort:** Auf Zertifizierung achten: MIL-A-18001K (Zink), MIL-DTL-24779C (Aluminium), US MIL oder DNV-GL-Zertifikat. Die Legierungszusammensetzung muss auf der Verpackung stehen. Markenanoden (Tecnoseal, Martyr, CMP, Canada Metal Pacific) sind bevorzugt. Billige No-Name-Anoden passivieren häufig.
**Confidence:** `documented` (MIL-Specs)

### OA-014: Saildrive-Anode — Original oder Aftermarket?
**Frage:** Soll ich die teurere Originalersatzanode von Volvo Penta kaufen?
**Antwort:** Aftermarket-Anoden von Tecnoseal, Martyr oder CMP sind qualitativ gleichwertig, sofern MIL-zertifiziert. Preis Original: 45–80 EUR, Aftermarket: 20–40 EUR. Die Passform muss exakt stimmen — auf korrekte Teilenummer des Aftermarket-Äquivalents achten.
**Confidence:** `estimated` (Marktvergleich)

### OA-015: Braucht mein GFK-Boot Rumpfanoden?
**Frage:** Mein Boot hat einen GFK-Rumpf. Wozu brauche ich trotzdem Rumpfanoden?
**Antwort:** GFK selbst korrodiert nicht, aber alle Unterwasser-Metallteile (Propeller, Welle, Ruder, Seeventile, Kiel) müssen geschützt werden. Rumpfanoden an GFK-Booten schützen über das Bonding-System alle angeschlossenen Metallteile.
**Confidence:** `documented` (ABYC E-2)

### OA-016: Kann ich Anoden im Wasser wechseln (ohne Kranen)?
**Frage:** Kann ein Taucher meine Anoden unter Wasser wechseln?
**Antwort:** Ja, erfahrene Yacht-Taucher können Bolt-On-Anoden unter Wasser wechseln. Kosten Taucherwechsel: 80–200 EUR. Vorteil: kein teures Kranen nötig. Nachteil: Kontaktfläche kann unter Wasser nicht optimal vorbereitet werden, Bonding-Prüfung nicht möglich. Empfehlung: Unterwasser-Wechsel als Notlösung, Haul-Out für gründliche Inspektion bevorzugen.
**Confidence:** `estimated` (Praxis-Erfahrung)

### OA-017: Was bedeutet „MIL-A-18001K"?
**Frage:** Was steckt hinter der MIL-Spezifikation für Zinkanoden?
**Antwort:** MIL-A-18001K ist die US-Militärspezifikation für marine Zinkanoden. Sie definiert die exakte Legierungszusammensetzung: Zn Basis, Al 0,10–0,50%, Cd 0,025–0,07%, Fe max. 0,005%, Cu max. 0,005%, Pb max. 0,006%, Si max. 0,125%. Besonders der niedrige Fe-Gehalt (<5 ppm) ist entscheidend gegen Passivierung.
**Confidence:** `measured` (MIL-A-18001K)

### OA-018: Warum korrodiert mein Edelstahl-Propeller trotz Anoden?
**Frage:** Mein 316L-Propeller zeigt Korrosion, obwohl ich neue Anoden habe.
**Antwort:** Edelstahl 316L braucht ein Schutzpotenzial von −500 bis −600 mV vs. Ag/AgCl — das Potenzial erreichen Zinkanoden normalerweise. Häufige Ursachen: 1) Propeller ist kein echtes 316L (sondern 304 oder 316 ohne L), 2) Spaltkorrosion unter Propellermutter, 3) Fehlende Wellenerdungsbürste, 4) AC-Streustrom, der auf DC-Anoden nicht anspricht.
**Confidence:** `documented` (ABYC E-2)

### OA-019: Wie wirkt sich die Wassertemperatur auf Anoden aus?
**Frage:** Verbrauchen sich Anoden im Mittelmeer schneller als in der Ostsee?
**Antwort:** Ja. Pro 10°C Wassertemperaturanstieg steigt die Verbrauchsrate um ca. 30–50%. Mittelmeer (20–28°C) vs. Ostsee (5–18°C): Anoden verbrauchen sich im Mittelmeer ca. 40–70% schneller. Dimensionierung entsprechend anpassen.
**Confidence:** `measured` (DNV-RP-B401)

### OA-020: Was ist der Unterschied zwischen Bonding und Grounding?
**Frage:** Sind Bonding und Erdung dasselbe?
**Antwort:** Nein. Bonding (Potenzialausgleich) verbindet alle Unterwasser-Metallteile untereinander auf gleiches Potenzial. Grounding (Erdung) verbindet das Boot mit der Erde (via Landstrom-Schutzleiter oder Erdungsplatte). Beide Systeme interagieren, haben aber unterschiedliche Zwecke. Bonding schützt vor galvanischer Korrosion, Grounding schützt vor elektrischem Schlag.
**Confidence:** `documented` (ABYC E-2, ABYC E-11)

### OA-021: Mein Aluminium-Rumpf korrodiert — was tun?
**Frage:** An meinem Alu-Rumpf zeigen sich weiße Flecken und Pitting. Die Anoden sind noch da.
**Antwort:** Prüfpunkte: 1) Sind es Aluminium-Anoden? Zinkanoden auf Alu-Rumpf sind FALSCH und können die Korrosion beschleunigen. 2) Bonding aller UW-Teile zum Rumpf korrekt? 3) Keine Kupfer-Antifouling verwendet? Kupfer-haltiges AF auf Alu ist verboten (galvanisches Element). 4) Kein Kontakt zu Bronze- oder Kupferbauteilen ohne galvanische Trennung.
**Confidence:** `documented` (ABYC E-2, Lloyd's Register)

### OA-022: Wie lagere ich Ersatz-Anoden korrekt?
**Frage:** Ich möchte Anoden auf Vorrat kaufen. Wie lagere ich sie?
**Antwort:** Trocken, bei Raumtemperatur, in Originalverpackung. Nicht in feuchten Räumen oder der Bilge lagern. Zink- und Alu-Anoden sind unbegrenzt lagerfähig bei korrekter Lagerung. Magnesiumanoden vor Feuchtigkeit schützen (Selbstkorrosion). Keine Kontaktfläche berühren (Handfett).
**Confidence:** `estimated` (Hersteller-Empfehlung)

### OA-023: Was kostet Korrosionsschaden durch fehlende Anoden?
**Frage:** Was kann passieren, wenn ich die Anoden-Wartung vernachlässige?
**Antwort:** Typische Schadenskosten: Propeller durchkorrodiert (Bronze 3-Blatt, 16"): 800–2.500 EUR. Propellerwelle mit Pitting: Nachdrehen 300–600 EUR, Austausch 800–2.000 EUR. Saildrive-Gehäuse: 3.000–8.000 EUR. Seeventil undicht: 200–500 EUR + Haul-Out (800–1.500 EUR). Ruderkoker-Leck: 1.500–5.000 EUR. Anoden-Wartung: 75–180 EUR/Jahr.
**Confidence:** `estimated` (Marktpreise 2025/2026)

### OA-024: ICCP vs. Opferanoden — was ist besser?
**Frage:** Soll ich auf ein ICCP-System umsteigen?
**Antwort:** ICCP Vorteile: präzise Potenzialregelung, lange Lebensdauer der Titan-Anoden (20+ Jahre), keine Haul-Outs für Anodenwechsel. ICCP Nachteile: hohe Installationskosten (2.000–8.000 EUR), Stromversorgung nötig, Ausfallrisiko (Elektronik), regelmäßige Kalibrierung. Empfehlung: Opferanoden bis 20m LOA, ICCP ab 20m oder bei Stahlrümpfen >50 m².
**Confidence:** `documented` (DNV-RP-B401)

### OA-025: Wie dokumentiere ich meinen Korrosionsschutz für die Versicherung?
**Frage:** Meine Versicherung fragt nach dem Korrosionsschutz. Was muss ich dokumentieren?
**Antwort:** Mindestdokumentation: 1) Anoden-Typ, Hersteller, Einbaudatum pro Position, 2) Fotos beim Haul-Out (Zustand alt + neu), 3) Bonding-Widerstandsmessungen (Protokoll), 4) Potenzialmessungen (falls verfügbar), 5) Streustrom-Test bei Landstrom-Liegern. AYDI speichert all dies automatisch mit Zeitstempel und generiert Wartungsberichte.
**Confidence:** `documented` (Versicherungsbedingungen)

> Confidence: `documented` (diverse Quellen), `estimated` (Marktpreise)

---

## 17. Glossar (erweitert)

| Begriff | Englisch | Definition |
|---------|----------|------------|
| Anodenkapazität | Anode capacity | Gesamte elektrische Ladung, die eine Anode über ihre Lebensdauer abgeben kann (Ah) |
| Anodenrückstand | Anode residue | Nicht-reaktiver Kern/Einlage nach vollständigem Verbrauch der aktiven Masse |
| Ag/AgCl-Elektrode | Silver/silver chloride electrode | Standard-Referenzelektrode für Seewasser-Potenzialmessungen |
| ABYC E-2 | ABYC E-2 Standard | Amerikanischer Standard für kathodischen Korrosionsschutz an Booten |
| Aktivierung | Activation | Prozess, der die Passivschicht einer Anode aufbricht (z.B. durch Indium bei Al-Anoden) |
| Beschichtungsdegradation | Coating degradation | Alterungsbedingter Abbau der Schutzbeschichtung, erhöht die zu schützende Fläche |
| Biofouling | Biofouling | Biologischer Bewuchs auf Unterwasserflächen, kann Anoden isolieren |
| Bonding-Bus | Bonding bus bar | Zentrale Sammelschiene für den Potenzialausgleich aller UW-Metallteile |
| Cadmium (Cd) | Cadmium | Legierungselement in Zinkanoden zur Verhinderung der Passivierung (0,025–0,07%) |
| CE-Kategorie | CE category | Entwurfskategorie nach EU-Richtlinie 2013/53/EU (A, B, C, D) |
| Chunk-Effekt | Chunk effect | Unkontrolliertes Abbrechen von Anodenstücken bei zu hohem Fe-Gehalt |
| Cu/CuSO₄-Elektrode | Copper/copper sulfate electrode | Alternative Referenzelektrode, häufig in Süßwasser und für Erdanlagen |
| Dauerliegeplatz | Permanent berth | Fester Liegeplatz, an dem das Boot >80% der Zeit liegt |
| Dezinkifizierung | Dezincification | Selektives Herauslösen von Zink aus Messinglegierungen (galvanisch bedingt) |
| Doppelschicht | Double layer | Elektrochemische Grenzschicht zwischen Metalloberfläche und Elektrolyt |
| Driving Potential | Driving potential | Potenzialdifferenz zwischen Anode und Kathode, muss min. 250 mV betragen |
| Elektrolyt | Electrolyte | Ionenleitende Flüssigkeit (Seewasser, Brackwasser, Süßwasser) |
| Erosionskorrosion | Erosion corrosion | Korrosion verstärkt durch mechanische Abtragung (Strömung, Kavitation) |
| Faraday-Gesetz | Faraday's law | Zusammenhang zwischen Stoffumsatz und elektrischer Ladung bei Elektrolyse |
| Filmbildung | Film formation | Bildung von Korrosionsprodukten auf der Anodenoberfläche (erwünscht: porös; unerwünscht: dicht) |
| Galvanische Reihe | Galvanic series | Rangfolge der Metalle nach ihrem Korrosionspotenzial in Seewasser |
| Galvanischer Isolator | Galvanic isolator | Gerät zur Blockierung galvanischer Ströme im Landstrom-Schutzleiter |
| Grenzstromdichte | Limiting current density | Maximale Stromdichte, bei der eine Anode noch effizient arbeitet |
| Halbzellenpotenzial | Half-cell potential | Potenzial einer einzelnen Elektrode gegen eine Referenzelektrode |
| ICCP | Impressed Current Cathodic Protection | Aktiver Korrosionsschutz durch externe Stromquelle und inerte Anoden |
| Indium (In) | Indium | Aktivierungselement in Al-Anoden (0,01–0,03%), verhindert Al₂O₃-Passivierung |
| Interkristalline Korrosion | Intergranular corrosion | Korrosion entlang der Korngrenzen eines Metalls |
| Kathodische Abscheidung | Cathodic deposit | Kalk-/Magnesiumhydroxid-Ablagerung auf geschützten Flächen bei Überprotektion |
| Kontaktkorrosion | Contact corrosion | Korrosion durch direkten Kontakt zweier unterschiedlicher Metalle im Elektrolyt |
| Korrosionsstromdichte | Corrosion current density | Strom pro Flächeneinheit, der durch den Korrosionsprozess fließt |
| Lochfraß | Pitting corrosion | Lokale, tiefe Korrosionsangriffe an einzelnen Punkten |
| Mischpotenzial | Mixed potential | Resultierendes Potenzial eines Metalls mit mehreren gleichzeitigen Reaktionen |
| Passivierung | Passivation | Bildung einer schützenden Oxidschicht, unerwünscht bei Opferanoden |
| Potenzialdifferenz | Potential difference | Spannungsdifferenz zwischen zwei Metallen, Triebkraft der galvanischen Korrosion |
| Potenziostat | Potentiostat | Gerät zur Regelung des Elektrodenpotenzials (ICCP-Steuergerät) |
| PSU | Practical Salinity Unit | Maßeinheit für Salzgehalt (≈ g/kg Salz), Seewasser ≈ 35 PSU |
| Referenzelektrode | Reference electrode | Elektrode mit bekanntem, stabilem Potenzial als Messpunkt |
| Schutzstrom | Protection current | Gesamtstrom, den die Anoden liefern müssen, um alle Flächen zu schützen |
| Selbstkorrosion | Self-corrosion | Unproduktiver Verbrauch der Anode durch eigene Korrosion (nicht zum Schutz beitragend) |
| Spaltkorrosion | Crevice corrosion | Korrosion in engen Spalten (z.B. unter Propellermutter) durch Sauerstoffverarmung |
| Streustrom | Stray current | Unbeabsichtigter Strom von externen Quellen (Landstrom, Nachbarboote, Marina) |
| Stromausbeute | Current efficiency | Anteil des Anodenstroms, der tatsächlich zum Schutz beiträgt (%) |
| Treibspannung | Driving voltage | Potenzialdifferenz zwischen Anode und geschütztem Objekt (min. 250 mV) |
| Trenntransformator | Isolation transformer | Galvanische Trennung zwischen Landstromnetz und Bordnetz |
| Überprotektion | Overprotection | Zu negatives Schutzpotenzial, führt zu Beschichtungsschäden und H₂-Versprödung |
| Utilization Factor | Utilization factor | Anteil der Anode, der tatsächlich verbraucht werden kann (typisch 0,80–0,90) |
| Wärmeeinflusszone | Heat-affected zone (HAZ) | Bereich um Schweißnaht mit verändertem Metallgefüge, korrosionsanfälliger |
| Wasserlinie | Waterline | Grenze zwischen Über- und Unterwasserbereich, korrosionskritische Zone |
| Wellenerdungsbürste | Shaft grounding brush | Schleifkontakt zur elektrischen Verbindung der rotierenden Welle mit dem Bonding |

> Confidence: `documented`

---

## 18. Schnell-Referenz

### 18.1 Anoden-Auswahl in 30 Sekunden

```
Seewasser (>20 PSU)      → Zink oder Aluminium
Brackwasser (5–20 PSU)   → Aluminium (NICHT Zink!)
Süßwasser (<5 PSU)       → Magnesium (NICHT Zink/Alu!)
Unsicher / wechselnd     → Aluminium (universell)
Aluminium-Rumpf          → NUR Aluminium-Anoden, NIEMALS Zink
Stahl-Rumpf              → Zink oder Aluminium
GFK-Rumpf                → Zink oder Aluminium (schützt UW-Metallteile)
```

### 18.2 Verbrauchsbeurteilung in 10 Sekunden

```
Verbrauch 0–10%:   ✓ Gut — nächste Saison OK
Verbrauch 10–30%:  ✓ Normal — nächstes Kranen prüfen
Verbrauch 30–50%:  ⚠ Aufmerksamkeit — Austausch einplanen
Verbrauch 50–70%:  ✗ Austausch beim nächsten Kranen
Verbrauch >70%:    ✗✗ Sofort-Austausch — Schutzwirkung minimal
Kein Verbrauch:    ⚠⚠ Passiviert? Bonding? Antifouling? → Sofort prüfen
```

### 18.3 Mindest-Anodensatz nach Bootstyp

| Bootstyp | LOA | Anoden | Gesamtgewicht Zink | Gesamtgewicht Alu | Kosten Zink (EUR) | Kosten Alu (EUR) |
|----------|-----|--------|-------------------|-------------------|------------------|-----------------|
| Segelboot mit Saildrive | 8–10m | 2× Rumpf + 1× SD + 1× Prop | 1,0–1,5 kg | 0,8–1,2 kg | 60–100 | 80–140 |
| Segelboot mit Welle | 10–14m | 2× Rumpf + 1× Welle + 1× Prop + 1× Ruder | 1,5–2,5 kg | 1,2–2,0 kg | 80–140 | 110–180 |
| Motorboot | 8–12m | 2× Rumpf + 2× Welle + 2× Trimm | 2,0–3,5 kg | 1,5–2,5 kg | 100–180 | 130–230 |
| Stahlsegler | 12–16m | 4–6× Rumpf + 1× Welle + 1× Prop + 1× Ruder | 5–10 kg | 3–6 kg | 200–400 | 250–500 |
| Motoryacht | 14–20m | 4× Rumpf + 2× Welle + 2× Prop + 2× Trimm + 2× Ruder | 8–15 kg | 5–10 kg | 350–650 | 450–800 |

### 18.4 Notfall-Entscheidungsbaum

```
Korrosion entdeckt?
├── Ja → Sind Anoden vorhanden?
│   ├── Nein → SOFORT Anoden montieren, Haul-Out planen
│   └── Ja → Anoden verbraucht (>50%)?
│       ├── Ja → Anoden ersetzen
│       └── Nein → Anoden passiviert?
│           ├── Ja → Richtige Legierung? Antifouling drauf? Bonding OK?
│           └── Nein → Bonding-System prüfen (Widerstand messen)
│               ├── >1 Ω → Bonding reparieren
│               └── <1 Ω → Streustrom messen
│                   ├── >50 mA → Streustrom-Quelle finden, Galv. Isolator
│                   └── <50 mA → Anoden unterdimensioniert → Masse erhöhen
└── Nein → Anoden trotzdem regelmäßig prüfen (jedes Kranen)
```

> Confidence: `documented` (Zusammenfassung aller Quellen)

---

## 19. Notfall-Ressourcen

### 19.1 Sofort-Hilfe bei Korrosionsnotfällen

| Situation | Sofortmaßnahme | Zeitfenster | Kontakt |
|-----------|---------------|-------------|---------|
| Seeventil korrodiert/undicht | Seeventil schließen, Holzkegel bereithalten | Stunden | Nächste Werft |
| Welle mit starkem Pitting | Boot nicht mehr unter Motor bewegen, Kranen | Tage | Werfttaucher |
| Saildrive-Gehäuse korrodiert | Motor nicht laufen lassen, Leckstelle beobachten | Stunden | Volvo/Yanmar-Service |
| Ruderkoker undicht | Stopfbuchse nachziehen, Bilgepumpe überwachen | Stunden–Tage | Werft |
| ICCP-Totalausfall | Opferanoden als Backup montieren (Taucher) | Tage | ICCP-Servicetechniker |
| Massiver Streustrom | Landstrom sofort abstecken | Sofort | Elektriker + Marina |

### 19.2 Fachbetriebe und Anlaufstellen

| Organisation | Leistung | Kontakt-Typ |
|-------------|----------|-------------|
| ABYC (American Boat and Yacht Council) | Normen, Zertifizierung, Schulung | www.abycinc.org |
| NACE International (jetzt AMPP) | Korrosionsschutz-Normen, Fachleute-Netzwerk | www.ampp.org |
| DNV GL | Klassifikation, Prüfungen, Beratung | www.dnv.com |
| Tecnoseal Deutschland | Anoden-Beratung, technischer Support | Tecnoseal Vertrieb DE |
| Volvo Penta Service | Saildrive-spezifische Korrosionsprobleme | Volvo Penta Händler |
| Yanmar Marine Service | Saildrive/Motor-Korrosion | Yanmar Händler |
| Lokale Sachverständige (BVSE) | Korrosionsgutachten für Versicherung | Bundesverband |

> Confidence: `documented`

---

## ANHANG A — Cross-Reference: Anodenposition ↔ Schutzbereich

| Anodenposition | Geschützte Bauteile | Max. Schutzradius | Bonding-Pfad erforderlich |
|---------------|--------------------|--------------------|--------------------------|
| Rumpfanode Bb (Kiel) | Kiel, Bb-Seeventile, Bb-Rumpf (Stahl) | 3–5 m | Ja (Kielbolzen, Seeventile) |
| Rumpfanode Stb (Kiel) | Kiel, Stb-Seeventile, Stb-Rumpf (Stahl) | 3–5 m | Ja |
| Wellenring | Propellerwelle, Stevenrohr, P-Bracket | 0,5 m | Ja (Wellenerdungsbürste) |
| Propelleranode | Propeller (alle Blätter) | Direkt | Über Welle (Bürste) |
| Ruderanode | Ruderblatt, Ruderschaft, Ruderkoker | 0,5 m | Ja (Kabel zum Bus) |
| Saildrive-Anode | Saildrive-Gehäuse, Propeller | 0,3 m | Über SD-Gehäuse zum Motor |
| Trimmklappe-Anode | Trimmklappe, Hydraulikzylinder | 0,3 m | Ja |
| Bugstrahlruder-Anode | Tunnel, Rotor, Gehäuse | 0,5 m | Ja (separater Bonding-Strang) |
| Motor-Kühlanode (intern) | Motor-Kühlkanäle, Wärmetauscher | Intern | Über Motorblock (autonom) |

> Confidence: `documented` (ABYC E-2)

---

## ANHANG B — Galvanische Reihe in Seewasser (vollständig)

Potenziale vs. Ag/AgCl-Referenzelektrode, Seewasser 3,5% NaCl, 20°C, ruhend:

| Rang | Metall/Legierung | Potenzial (mV vs. Ag/AgCl) | Verhalten |
|------|-----------------|---------------------------|-----------|
| 1 | Magnesium (rein) | −1600 bis −1630 | Anode (sehr unedel) |
| 2 | Mg-Legierung (AZ31) | −1550 bis −1580 | Anode |
| 3 | Mg-Anode (High Potential) | −1500 bis −1550 | Anode |
| 4 | Zink (rein) | −1030 bis −1050 | Anode |
| 5 | Zink-Anode (MIL-A-18001K) | −1000 bis −1050 | Anode |
| 6 | Aluminium-Anode (Al-Zn-In) | −1050 bis −1100 | Anode |
| 7 | Aluminium 5083 (Rumpf) | −750 bis −850 | Geschützt durch Anoden |
| 8 | Aluminium 6061-T6 | −700 bis −800 | Geschützt durch Anoden |
| 9 | Kadmium | −700 bis −750 | — |
| 10 | Weichstahl / Gusseisen | −600 bis −700 | Geschützt durch Anoden |
| 11 | Schiffbaustahl (A/B/D) | −600 bis −700 | Geschützt durch Anoden |
| 12 | Blei / Bleilegierung | −500 bis −550 | Kiel-Material |
| 13 | Zinn | −450 bis −500 | — |
| 14 | Edelstahl 304 (aktiv) | −400 bis −500 | Nicht marine-tauglich |
| 15 | Edelstahl 316 (aktiv) | −350 bis −450 | Spaltkorrosion möglich |
| 16 | Edelstahl 316L (aktiv) | −350 bis −450 | Marine-Standard |
| 17 | Messing (Cu-Zn) | −300 bis −400 | Dezinkifizierungsgefahr |
| 18 | Kupfer | −300 bis −350 | — |
| 19 | Bronze (Sn-Bronze) | −270 bis −340 | Propeller, Seeventile |
| 20 | Kupfer-Nickel 90/10 | −250 bis −300 | Kühlwasserleitungen |
| 21 | Kupfer-Nickel 70/30 | −200 bis −280 | Wärmetauscher |
| 22 | Nickel 200 | −150 bis −250 | — |
| 23 | Silberlot | −100 bis −200 | — |
| 24 | Edelstahl 304 (passiv) | −50 bis −200 | Im passiven Zustand |
| 25 | Edelstahl 316 (passiv) | −50 bis −150 | Im passiven Zustand |
| 26 | Edelstahl 316L (passiv) | −50 bis −150 | Im passiven Zustand |
| 27 | Monel 400 (Ni-Cu) | −40 bis −140 | — |
| 28 | Titan (rein) | −50 bis +50 | ICCP-Anode |
| 29 | Hastelloy C-276 | 0 bis +100 | — |
| 30 | Graphit | +100 bis +300 | ICCP-Anode |
| 31 | Platin | +200 bis +400 | ICCP-Anode (MMO) |

**Faustregel:** >250 mV Potenzialdifferenz zwischen zwei Metallen → galvanische Korrosion wahrscheinlich ohne Anodenschutz.

> Confidence: `measured` (ASTM G82, DNV-RP-B401)

---

## ANHANG C — Verbrauchsraten-Tabelle (Praxiswerte)

| Revier | Salzgehalt (PSU) | Temp. (°C) | Zink (g/kg·Mon.) | Alu (g/kg·Mon.) | Mg (g/kg·Mon.) |
|--------|-----------------|-----------|-----------------|-----------------|----------------|
| Ostsee West (Kiel) | 12–18 | 4–18 | 25–35 | 10–18 | n/a |
| Ostsee Ost (Rügen) | 7–12 | 3–17 | 20–30 | 8–15 | n/a (zu salzig) |
| Nordsee | 30–34 | 5–18 | 35–50 | 15–25 | n/a |
| Mittelmeer West | 36–38 | 14–28 | 40–60 | 18–30 | n/a |
| Mittelmeer Ost | 38–40 | 16–30 | 45–65 | 20–35 | n/a |
| Karibik | 34–36 | 26–30 | 50–70 | 22–35 | n/a |
| Bodensee | 0,2 | 4–22 | passiviert | passiviert | 20–35 |
| Gardasee | 0,3 | 6–24 | passiviert | passiviert | 22–38 |
| Ijsselmeer (NL) | 0,5–3 | 3–22 | passiviert | schlecht | 18–30 |
| Chesapeake Bay | 5–18 | 5–28 | 20–40 | 12–22 | n/a |
| Schwedische Westküste | 20–30 | 3–20 | 30–45 | 14–22 | n/a |

> Confidence: `estimated` (Erfahrungswerte, Forum-Konsens, Herstellerdaten)

---

## ANHANG D — Confidence-Mapping für AYDI-Analysemodule

| Datenquelle | Confidence-Level | AYDI-Modul | Score-Gewichtung |
|-------------|-----------------|------------|-----------------|
| Hersteller-TDS (Tecnoseal, Martyr) | `measured` | materials | 1,0 |
| MIL-Spec Legierungsanalyse | `measured` | materials | 1,0 |
| DNV-RP-B401 Berechnung | `calculated` | structural | 0,95 |
| Potenzialmessung (Ag/AgCl) | `measured` | structural | 1,0 |
| Widerstandsmessung Bonding | `measured` | structural | 1,0 |
| Foto Anodenzustand | `visual_high` | materials, production | 0,80 |
| Foto Korrosionsspur | `visual_medium` | materials | 0,65 |
| Gewichtsmessung Anode | `measured` | materials | 1,0 |
| Revier-Erfahrungswerte | `estimated` | service_patterns | 0,60 |
| Forum-Berichte | `estimated` | service_patterns | 0,40 |
| Versicherungs-Schadenberichte | `documented` | cost | 0,85 |
| Werft-Wartungsprotokolle | `documented` | service_patterns | 0,90 |
| AYDI-Inspektionsdaten (aggregiert) | `benchmark` | market | 0,75 |

> Confidence: `documented` (AYDI-Architektur)

---

## ANHANG E — Bordausstattung Korrosionsschutz-Inspektion

| Ausrüstung | Zweck | Kosten (EUR) | Priorität |
|-----------|-------|-------------|-----------|
| Multimeter (True RMS) | Widerstand + Spannung messen | 30–80 | Pflicht |
| Ag/AgCl-Referenzelektrode | Schutzpotenzialmessung | 80–150 | Empfohlen |
| Verlängerungskabel 5m (für Referenzelektrode) | Messung vom Steg | 15–25 | Empfohlen |
| Clamp-on DC-Milliamperemeter | Streustrom ohne Leitungstrennung | 150–300 | Profi |
| Schichtdickenmessgerät | Anodendicke messen ohne Ausbau | 200–500 | Profi |
| Küchenwaage (5 kg, ±1 g) | Anodengewicht → Verbrauchsberechnung | 15–30 | Pflicht |
| Edelstahl-Drahtbürste | Kontaktflächen reinigen | 5–10 | Pflicht |
| Schleifpapier 80 + 120 | Welle/Kontaktflächen blank schleifen | 3–5 | Pflicht |
| Drehmomentschlüssel (5–40 Nm) | Korrekte Montage | 25–60 | Empfohlen |
| Kontaktpaste (Tef-Gel, 30g) | Bimetall-Kontakte schützen | 12–18 | Empfohlen |
| Prüfprotokoll-Vorlage | Dokumentation für Versicherung | 0 (AYDI) | Pflicht |

> Confidence: `estimated` (Marktpreise 2025/2026)

---

## ANHANG F — Fallstudien

### Fallstudie 1: Bavaria 34 — Zinkanoden passiviert (Ostsee)

- **Boot:** Bavaria 34 Cruiser (2018), GFK, Saildrive Volvo 120S, LOA 10,3m
- **Revier:** Ostsee, Kieler Förde (Salinität 14–18 PSU)
- **Problem:** Saildrive-Gehäuse mit Lochfraß nach 18 Monaten, Anoden optisch unverbraucht
- **Befund:** Zinkanoden passiviert bei niedrigem Salzgehalt, kein Schutzstrom messbar
- **Lösung:** Umrüstung auf Aluminium-Anoden (Tecnoseal), Bonding-System nachgemessen (<0,3 Ω)
- **Ergebnis:** Nach 12 Monaten: Alu-Anoden 20% verbraucht (normal), kein neuer Lochfraß
- **Kosten:** Anoden 85 EUR, Montage 120 EUR, Saildrive-Reparatur 2.800 EUR (Vorschaden)
- **AYDI-Score vorher:** 15/100 (materials), **nachher:** 85/100
- **Lektion:** In der Ostsee grundsätzlich Aluminium-Anoden verwenden, nie Zink
- **Confidence:** `documented` (Werft-Bericht)
- **Pipeline B Befund:** `visual_high` — Passivierung und Lochfraß eindeutig erkennbar
- **Revier-Empfehlung:** Ostsee West → Aluminium-Anoden obligatorisch

### Fallstudie 2: Hallberg-Rassy 40 — Streustrom-Schaden (Marina Kroatien)

- **Boot:** Hallberg-Rassy 40 (2015), GFK, Wellenlage, LOA 12,1m
- **Revier:** Marina Kaštela, Kroatien (Salinität 38 PSU, Wassertemp. 22–28°C Sommer)
- **Problem:** Propeller (Gori 3-Blatt Bronze) nach einer Saison mit starkem Pitting, Anoden 80% verbraucht
- **Befund:** DC-Streustrom >200 mA gemessen bei Landstrom-Anschluss, Nachbarboot mit defektem Ladegerät
- **Lösung:** Galvanischer Isolator ProMariner ProSafe II installiert, Anoden erneuert, Marina informiert
- **Ergebnis:** Streustrom auf <5 mA reduziert, Anoden normal verbraucht nach 12 Monaten
- **Kosten:** Galv. Isolator 380 EUR, Einbau 150 EUR, Anoden 120 EUR, Propeller polieren 200 EUR
- **AYDI-Score vorher:** 10/100 (structural), **nachher:** 90/100
- **Lektion:** In Marinas mit vielen Charterbooten: Galvanischer Isolator ist Pflicht
- **Confidence:** `measured` (Streustrommessung)
- **Pipeline B Befund:** `visual_high` — asymmetrischer Abtrag pathognomonisch für Streustrom
- **Revier-Empfehlung:** Kroatische Marinas → GI installieren, Anoden +30% überdimensionieren

### Fallstudie 3: Jeanneau Sun Odyssey 449 — Antifouling auf Anoden

- **Boot:** Jeanneau SO 449 (2020), GFK, Saildrive Yanmar SD50, LOA 13,7m
- **Revier:** Mallorca, Port de Pollença (Salinität 37 PSU)
- **Problem:** Korrosion an allen Bronze-Seeventilen nach einer Saison, Anoden „wie neu"
- **Befund:** Werft hatte beim Antifouling-Auftrag alle Anoden mitgestrichen → elektrisch isoliert
- **Lösung:** Antifouling von Anoden entfernt, Kontaktflächen blank geschliffen, neu montiert
- **Ergebnis:** Schutzpotenzial −980 mV vs. Ag/AgCl messbar, Seeventile stabilisiert
- **Kosten:** Nacharbeit 180 EUR, 2 Seeventile tauschen 650 EUR (Vorschaden)
- **AYDI-Score vorher:** 0/100 (materials), **nachher:** 88/100
- **Lektion:** Werft-Anweisung: Anoden VOR Antifouling-Auftrag abkleben (Malerkrepp)
- **Confidence:** `documented` (Werft-Bericht)
- **Pipeline B Befund:** `visual_high` — farbgleiche Anoden/Rumpf sofort erkennbar
- **Werft-Empfehlung:** Checkliste „Anoden freihalten" in Werft-Auftrag aufnehmen

### Fallstudie 4: Hanse 388 — Wellenerdungsbürste defekt

- **Boot:** Hanse 388 (2019), GFK, Wellenlage mit Faltpropeller, LOA 11,6m
- **Revier:** Ostsee, Travemünde (Salinität 10–15 PSU)
- **Problem:** Starker Lochfraß am Faltpropeller (Aluminium-Bronze), Rumpfanoden kaum verbraucht
- **Befund:** Wellenerdungsbürste (Kupfer-Graphit) verschlissen, Kontaktwiderstand >5 kΩ (Soll: <200 mΩ)
- **Lösung:** Neue Wellenerdungsbürste (Electro-Guard) installiert, Welle geschliffen
- **Ergebnis:** Kontaktwiderstand 30 mΩ, Propeller in Schutzbereich (−860 mV vs. Ag/AgCl)
- **Kosten:** Bürste 220 EUR, Einbau 150 EUR, Propeller polieren/nachbearbeiten 400 EUR
- **AYDI-Score vorher:** 20/100 (structural), **nachher:** 92/100
- **Lektion:** Wellenerdungsbürste alle 12 Monate kontrollieren, Kontaktwiderstand messen
- **Confidence:** `measured` (Widerstandsmessung)
- **Pipeline B Befund:** `visual_high` — Pitting am Propeller klar sichtbar
- **Wartungsintervall:** Bürsten-Check alle 12 Monate, Austausch alle 24 Monate

### Fallstudie 5: Dehler 38 — Falsche Anoden für Süßwasser

- **Boot:** Dehler 38 SQ (2017), GFK, Saildrive Volvo 130S, LOA 11,5m
- **Revier:** Bodensee (Salinität 0,2 PSU, Süßwasser)
- **Problem:** Korrosion am Saildrive nach 2 Saisons, Zinkanoden mit dicker weißer Kruste (ZnO)
- **Befund:** Zinkanoden im Süßwasser vollständig passiviert, kein messbarer Schutzstrom
- **Lösung:** Umrüstung auf Magnesium-Anoden, Bonding-System erweitert (alle Seeventile angebunden)
- **Ergebnis:** Mg-Anoden zeigen normalen Verbrauch (25% nach 8 Monaten), Schutzpotenzial −920 mV
- **Kosten:** Mg-Anoden 95 EUR, Bonding-Erweiterung 280 EUR, SD-Inspektion 200 EUR
- **AYDI-Score vorher:** 5/100 (materials), **nachher:** 82/100
- **Lektion:** Binnenrevier = Magnesium, keine Ausnahmen. AYDI warnt automatisch bei Revier-Mismatch
- **Confidence:** `documented` (Eigner-Bericht + Werft-Bestätigung)
- **Pipeline B Befund:** `visual_high` — weiße ZnO-Kruste typisch für Süßwasser-Passivierung
- **Revier-Empfehlung:** Bodensee, Müritz, Berliner Seen → immer Magnesium

### Fallstudie 6: Beneteau Oceanis 51.1 — Überprotektion durch Überdimensionierung

- **Boot:** Beneteau Oceanis 51.1 (2021), GFK, Wellenlage, LOA 15,4m
- **Revier:** Côte d'Azur, Port Grimaud (Salinität 38 PSU)
- **Problem:** Antifouling blättert um die Anoden herum ab, harte weiße Kalkablagerungen auf Propeller
- **Befund:** Eigner hatte 4× Rumpfanoden à 2,5 kg montiert (10 kg Zink) für 15m GFK-Yacht → massive Überprotektion
- **Lösung:** Anodenmasse auf 3 kg Gesamt reduziert (Berechnung nach DNV-RP-B401), Antifouling erneuert
- **Ergebnis:** Schutzpotenzial von −1180 mV (zu negativ) auf −970 mV (optimal) angepasst
- **Kosten:** Neuberechnung 150 EUR, Antifouling-Reparatur 600 EUR, Kalkentfernung 200 EUR
- **AYDI-Score vorher:** 40/100 (materials), **nachher:** 90/100
- **Lektion:** Mehr ist nicht besser. Korrekte Berechnung nach DNV-RP-B401 essenziell
- **Confidence:** `measured` (Potenzialmessung)
- **Pipeline B Befund:** `visual_high` — Antifouling-Ablösung um Anoden ist Überprotektions-Indikator
- **Bemerkung:** Überprotektion ist seltener als Unterprotektion, aber ebenso schädlich

### Fallstudie 7: Contest 42CS — Stahl-Rumpf, komplettes Bonding-Versagen

- **Boot:** Contest 42CS (2008), Stahlrumpf, Wellenlage, LOA 12,8m
- **Revier:** IJmuiden, Niederlande (Nordsee, Salinität 32 PSU)
- **Problem:** Großflächige Korrosion am Unterwasserschiff nach 3 Jahren, Anoden nur 15% verbraucht
- **Befund:** Bonding-Bus-Bar aus Aluminium (FALSCH), alle Verbindungen hochohmig (>10 Ω)
- **Lösung:** Komplettes Bonding-System erneuert: verzinnte Cu-Busbar 8×30mm, alle Leitungen 10 mm² verzinntes Cu, 14 Anschlüsse, Wellenerdungsbürste
- **Ergebnis:** Widerstand aller Messpunkte <0,2 Ω, Anoden zeigen normalen Verbrauch
- **Kosten:** Bonding-System komplett 2.800 EUR, Rumpf-Sandstrahlen + Neubeschichtung 8.500 EUR
- **AYDI-Score vorher:** 5/100 (structural), **nachher:** 95/100
- **Lektion:** Bonding-Material MUSS verzinntes Kupfer sein. Aluminium-Busbar korrodiert selbst
- **Confidence:** `measured` (Widerstandsmessungen vorher/nachher)
- **Pipeline B Befund:** `visual_high` — Flächenkorrosion am Stahlrumpf deutlich sichtbar
- **Empfehlung:** Stahlrümpfe: Bonding-Inspektion alle 2 Jahre, Widerstandsprotokoll

### Fallstudie 8: Azimut 55 — ICCP-Ausfall ohne Backup

- **Boot:** Azimut 55 (2014), GFK, Twin-Shaft, LOA 16,5m
- **Revier:** Porto Cervo, Sardinien (Salinität 38 PSU)
- **Problem:** Massive Korrosion an beiden Propellerwellen und Ruderblättern nach nur 6 Monaten
- **Befund:** ICCP-System Steuergerät defekt (Platine durchgebrannt), keine Backup-Opferanoden montiert
- **Lösung:** ICCP-Steuergerät ersetzt, zusätzlich 4× Rumpf-Opferanoden als Backup installiert
- **Ergebnis:** ICCP funktioniert, Backup-Anoden zeigen minimalen Verbrauch (ICCP liefert Hauptschutz)
- **Kosten:** ICCP-Reparatur 3.200 EUR, Backup-Anoden 180 EUR, 2 Wellen nachdrehen 1.800 EUR
- **AYDI-Score vorher:** 0/100 (structural), **nachher:** 95/100
- **Lektion:** ICCP-Yachten brauchen IMMER Backup-Opferanoden. Nie nur auf Elektronik vertrauen
- **Confidence:** `measured` (ICCP-Fehlerprotokoll)
- **Pipeline B Befund:** `visual_medium` — Wellenkorrosion unter Wasser schwer erkennbar
- **Empfehlung:** ICCP-Systeme: jährliche Wartung, Backup-Anoden als Redundanz

> Confidence: `documented` (Werft-Berichte, Eigner-Berichte), `measured` (Messprotokolle)

---

## ANHANG G — Experten-Verzeichnis

| Fachgebiet | Organisation/Person | Standort | Spezialgebiet |
|-----------|-------------------|----------|---------------|
| Korrosionsschutz-Beratung | AMPP (ehem. NACE) zertifizierte Inspektoren | International | CP-Inspektion, Beschichtung |
| Marine-Elektriker (ABYC-zertifiziert) | Diverse Werften | International | Bonding, Streustrom, ICCP |
| Anodenlieferanten (technischer Support) | Tecnoseal, Martyr, CMP | EU/USA | Produktauswahl, Dimensionierung |
| Materialprüflabor | SGS, Bureau Veritas, TÜV | EU | Legierungsanalyse, Zertifizierung |
| Unterwasser-Inspektion | Spezialisierte Tauchdienste | Revierabhängig | Anodeninspektion, UW-Wechsel |
| Elektrochemie-Gutachten | Fraunhofer ISE, BAM Berlin | Deutschland | Korrosionsmechanismen, Forschung |
| Versicherungsgutachten | BSM, BVSV-Sachverständige | Deutschland | Schadensbewertung, Haftung |

> Confidence: `documented`

---

## ANHANG H — Risk Matrix: Korrosionsschutz

| Risiko-ID | Risiko | Eintrittswahrscheinlichkeit | Schadenshöhe (EUR) | Risiko-Score | Mitigation |
|-----------|--------|---------------------------|--------------------|--------------|-----------  |
| KS-01 | Anoden vollständig verbraucht | Hoch (40%) | 500–5.000 | Hoch | Regelmäßige Inspektion, AYDI-Warnung |
| KS-02 | Passivierte Anoden | Mittel (15%) | 1.000–8.000 | Hoch | Richtige Legierung, zertifizierte Produkte |
| KS-03 | Streustrom-Schaden | Mittel (12%) | 2.000–15.000 | Hoch | Galvanischer Isolator, Trenntransformator |
| KS-04 | Bonding-System-Ausfall | Mittel (10%) | 1.500–10.000 | Hoch | Jährliche Widerstandsmessung |
| KS-05 | Falsche Legierung für Revier | Niedrig (8%) | 500–5.000 | Mittel | AYDI-Revier-Check |
| KS-06 | Überprotektion | Niedrig (5%) | 300–2.000 | Niedrig | DNV-RP-B401 Berechnung |
| KS-07 | Antifouling auf Anode | Mittel (18%) | 200–3.000 | Mittel | Werft-Checkliste |
| KS-08 | ICCP-Totalausfall | Niedrig (5%) | 3.000–20.000 | Hoch | Backup-Opferanoden |
| KS-09 | Wellenerdungsbürste defekt | Hoch (25%) | 500–3.000 | Hoch | 12-Monats-Kontrolle |
| KS-10 | Seeventil-Korrosion (DZF) | Mittel (10%) | 500–3.000 + Sicherheit | Hoch | Bonding + Inspektion |

> Confidence: `estimated` (Branchendaten, AYDI-Aggregation)

---

## ANHANG I — Audit- und Compliance-Checkliste

### Jährlicher Korrosionsschutz-Audit

| Nr. | Prüfpunkt | Standard | Methode | OK/NOK | Bemerkung |
|-----|-----------|---------|---------|--------|-----------|
| I-01 | Anodenverbrauch dokumentiert | ABYC E-2 | Gewichtsmessung | ☐ | |
| I-02 | Anodenlegierung korrekt für Revier | ABYC E-2 §E-2.5 | Visuell + Dokumentation | ☐ | |
| I-03 | Bonding-Widerstand <1 Ω | ABYC E-2 §E-2.10 | Multimeter | ☐ | |
| I-04 | Wellenerdungsbürste <200 mΩ | ABYC E-2 | Multimeter | ☐ | |
| I-05 | Keine Antifouling auf Anoden | ABYC E-2 §E-2.6 | Visuell | ☐ | |
| I-06 | Schrauben A4-80 (316L) | Best Practice | Visuell + Magnet-Test | ☐ | |
| I-07 | Kein Streustrom >30 mA DC | ABYC E-2 §E-2.12 | Amperemeter | ☐ | |
| I-08 | Schutzpotenzial im Sollbereich | DNV-RP-B401 | Referenzelektrode | ☐ | |
| I-09 | ICCP-Funktionstest (falls vorhanden) | DNV-RP-B401 | Systemtest | ☐ | |
| I-10 | Galvanischer Isolator geprüft | ABYC A-28 | Multimeter (Durchlassspannung) | ☐ | |
| I-11 | Kabelschuhe gecrimpt + gelötet | ABYC E-11 | Visuell + Zugprobe | ☐ | |
| I-12 | Schrumpfschlauch an allen Verbindungen | Best Practice | Visuell | ☐ | |
| I-13 | Dokumentation vollständig | Versicherung | Unterlagen prüfen | ☐ | |
| I-14 | Fotos gemacht (alt + neu) | AYDI | Fotodokumentation | ☐ | |

> Confidence: `documented` (ABYC, DNV)

---

## ANHANG J — Material-Datenblätter (Kurzform)

### J.1 Zink-Anode (MIL-A-18001K)

| Eigenschaft | Wert | Einheit |
|-------------|------|---------|
| Dichte | 7,13 | kg/dm³ |
| Schmelzpunkt | 419 | °C |
| Stromkapazität (theoretisch) | 820 | Ah/kg |
| Stromkapazität (praktisch) | 780 | Ah/kg |
| Ruhepotenzial (OCP) | −1030 bis −1050 | mV vs. Ag/AgCl |
| Schließpotenzial | −1000 bis −1020 | mV vs. Ag/AgCl |
| Al-Gehalt | 0,10–0,50 | % |
| Cd-Gehalt | 0,025–0,07 | % |
| Fe-Gehalt (max.) | 0,005 | % (50 ppm) |
| Cu-Gehalt (max.) | 0,005 | % |
| Pb-Gehalt (max.) | 0,006 | % |
| Si-Gehalt (max.) | 0,125 | % |
| Zugfestigkeit | 30–40 | MPa |

### J.2 Aluminium-Anode (MIL-DTL-24779C, Typ II)

| Eigenschaft | Wert | Einheit |
|-------------|------|---------|
| Dichte | 2,73 | kg/dm³ |
| Schmelzpunkt | 640–660 | °C |
| Stromkapazität (theoretisch) | 2.830 | Ah/kg |
| Stromkapazität (praktisch) | 2.600 | Ah/kg |
| Ruhepotenzial (OCP) | −1080 bis −1120 | mV vs. Ag/AgCl |
| Schließpotenzial | −1050 bis −1080 | mV vs. Ag/AgCl |
| Zn-Gehalt | 3,5–5,0 | % |
| In-Gehalt | 0,015–0,040 | % |
| Si-Gehalt (max.) | 0,10 | % |
| Fe-Gehalt (max.) | 0,09 | % |
| Cu-Gehalt (max.) | 0,003 | % |
| Zugfestigkeit | 100–140 | MPa |

### J.3 Magnesium-Anode (ASTM B843, Typ AZ63B)

| Eigenschaft | Wert | Einheit |
|-------------|------|---------|
| Dichte | 1,74 | kg/dm³ |
| Schmelzpunkt | 650 | °C |
| Stromkapazität (theoretisch) | 2.205 | Ah/kg |
| Stromkapazität (praktisch) | 1.230 | Ah/kg |
| Ruhepotenzial (OCP) | −1550 bis −1600 | mV vs. Ag/AgCl |
| Schließpotenzial | −1500 bis −1550 | mV vs. Ag/AgCl |
| Al-Gehalt | 5,3–6,7 | % |
| Zn-Gehalt | 2,5–3,5 | % |
| Mn-Gehalt (min.) | 0,15 | % |
| Fe-Gehalt (max.) | 0,003 | % |
| Cu-Gehalt (max.) | 0,010 | % |
| Ni-Gehalt (max.) | 0,002 | % |
| Zugfestigkeit | 200–230 | MPa |

> Confidence: `measured` (MIL-Specs, ASTM)

---

## ANHANG K — Prüfverfahren

### K.1 Potenzialmessung im Wasser

**Geräte:** Hochohmiges Multimeter (>10 MΩ Eingangswiderstand), Ag/AgCl-Referenzelektrode, 5m Kabel

**Durchführung:**
1. Referenzelektrode ins Wasser senken (neben dem geschützten Bauteil, max. 300 mm Abstand)
2. Multimeter auf DC-Spannungsmessung (mV)
3. Plus-Leitung an Referenzelektrode, Minus-Leitung an geschütztes Metallteil
4. Wert ablesen (soll negativ sein)
5. Wert an mindestens 3 Positionen messen (Bug, Mitte, Heck)

**Bewertung:**
- Stahl: −800 bis −1050 mV → OK, positiver als −800 mV → unterprotektiert, negativer als −1100 mV → überprotektiert
- Bronze: −550 bis −650 mV → OK
- Aluminium: −800 bis −1050 mV → OK, negativer als −1100 mV → H₂-Versprödung möglich

### K.2 Bonding-Widerstandsmessung

**Geräte:** Multimeter, saubere Messspitzen

**Durchführung:**
1. Alle Landstromverbraucher aus, Batteriehauptschalter aus
2. Messspitze 1 auf Bonding-Bus-Bar
3. Messspitze 2 nacheinander auf: Motorblock, Wellenende, Ruderschaft, jedes Seeventil, Kielbolzen, Tankhalterungen
4. Werte protokollieren

**Bewertung:** <0,5 Ω → gut, 0,5–1 Ω → akzeptabel, 1–2 Ω → Leitung prüfen, >2 Ω → Leitung erneuern

### K.3 Streustrom-Messung

**Geräte:** DC-Milliamperemeter (oder Clamp-On), Multimeter

**Durchführung:**
1. Amperemeter in Reihe zwischen Bonding-Bus und einem Unterwasser-Metallteil
2. Alle Geräte aus, Messwert notieren (Basis-Galvanikstrom)
3. Landstrom anschließen → Änderung notieren
4. Verbraucher einzeln einschalten → Änderung notieren pro Gerät
5. Nachbar-Einfluss: eigenes Boot stromfrei, Nachbar-Landstrom an/aus → Potenzialänderung messen

**Bewertung:** Basis <5 mA → normal, 5–50 mA → erhöhter Galvanikstrom, >50 mA → Streustrom-Problem

> Confidence: `measured` (ABYC E-2, Prüfverfahren)

---

## ANHANG L — Top 15 Fehler bei Opferanoden

| Rang | Fehler | Häufigkeit | Kosten (EUR) | Vermeidung |
|------|--------|-----------|-------------|------------|
| 1 | Antifouling auf Anode | 18% | 200–3.000 | Anoden beim Streichen abkleben |
| 2 | Zinkanoden in Brackwasser/Süßwasser | 10% | 500–5.000 | Revier-Salinität prüfen → Alu/Mg |
| 3 | Bonding-Leitung korrodiert | 20% | 300–2.000 | Verzinntes Kupfer verwenden |
| 4 | Wellenerdungsbürste verschlissen | 25% | 500–3.000 | Jährliche Kontrolle |
| 5 | Schrauben aus 304 statt 316L | 12% | 100–1.000 | A4-80 Schrauben kaufen |
| 6 | Zu wenig Anodenmasse | 8% | 500–5.000 | DNV-RP-B401 Berechnung |
| 7 | Keine Anoden montiert | 5% | 1.000–20.000 | AYDI-Warnung bei Fehlen |
| 8 | Billig-Anoden (passiviert) | 7% | 500–5.000 | Nur MIL-zertifizierte Anoden |
| 9 | Kein Galvanischer Isolator in Marina | 15% | 1.000–10.000 | GI einbauen |
| 10 | Überprotektion (zu viele Anoden) | 5% | 300–2.000 | Korrekte Berechnung |
| 11 | Isolierscheibe unter Anode | 3% | 500–5.000 | Direkten Metallkontakt sicherstellen |
| 12 | Zinkanode auf Alu-Rumpf | 2% | 2.000–15.000 | NUR Al-Anoden auf Al-Rumpf |
| 13 | ICCP ohne Backup-Anoden | 3% | 3.000–20.000 | Immer Opferanoden zusätzlich |
| 14 | Motor-Kühlanode vergessen | 15% | 500–3.000 | Bei jedem Service prüfen |
| 15 | Welle nicht blank geschliffen (Wellenring) | 10% | 300–2.000 | Montageanleitung befolgen |

> Confidence: `estimated` (Branchendaten, AYDI-Aggregation)

---

## ANHANG M — Zusammenfassung: Die 10 Goldenen Regeln des Opferanodenraschutzes

1. **Richtige Legierung für das Revier:** Seewasser = Zn/Al, Brackwasser = Al, Süßwasser = Mg.
2. **Korrekt dimensionieren:** Berechnung nach DNV-RP-B401, nicht nach Gefühl.
3. **Metallischen Kontakt sicherstellen:** Kein Antifouling, kein Primer, keine Isolierscheibe zwischen Anode und Schutzfläche.
4. **Bonding-System intakt halten:** Alle UW-Metallteile über verzinntes Kupfer verbinden, <1 Ω.
5. **Wellenerdungsbürste prüfen:** Jährlich kontrollieren, Widerstand <200 mΩ.
6. **Nur zertifizierte Anoden verwenden:** MIL-A-18001K (Zn), MIL-DTL-24779C (Al), ASTM B843 (Mg).
7. **Schrauben aus 316L (A4-80):** Keine 304er, kein Messing, keine verzinkten Schrauben.
8. **Galvanischen Isolator einbauen:** In jeder Marina mit Landstrom.
9. **Bei jedem Kranen dokumentieren:** Fotos, Gewichte, Schutzpotenzial, Bonding-Widerstand.
10. **Austausch bei >50% Verbrauch:** Nicht warten bis die Anode „ganz weg" ist.

> Confidence: `documented` (Best Practice, ABYC E-2, DNV-RP-B401)

---

## ANHANG N — Spezialanwendungen

### N.1 Aluminium-Rümpfe

**Besonderheiten:**
- NIEMALS Zinkanoden verwenden → Potenzialdifferenz zu gering, Rumpf korrodiert bevorzugt
- NUR Aluminium-Anoden (Al-Zn-In) oder ICCP
- Antifouling: KEIN kupferhaltiges Antifouling → galvanisches Element Cu ↔ Al
- Bonding: Rumpf IST die Masseverbindung → Anoden direkt am Rumpf verschweißen
- Isolation aller Bronze-/Kupfer-Bauteile vom Rumpf durch Kunststoff-Flansche
- Motor-Isolation: Motor vom Rumpf isoliert montieren (Gummilager + Isolierflansch an Welle)

**AYDI-Bewertungskriterien Alu-Rumpf:**
| Kriterium | Score 100 | Score 0 |
|-----------|----------|---------|
| Anodentyp | Al-Zn-In, korrekt dimensioniert | Zink oder kein Anodenschutz |
| Antifouling | Kupferfreies AF (z.B. Hempel Silic One) | Kupfer-AF auf Alu |
| Bronze-Isolation | Alle Durchbrüche mit Isolierflansch | Direkter Bronze-Alu-Kontakt |
| Motor-Isolation | Flexible Kupplung + Isolierlager | Starre Verbindung Motor-Rumpf |
| Bonding | Rumpf als Masse, alle Teile korrekt angebunden | Fragmentiertes Bonding |

### N.2 Stahl-Rümpfe

**Besonderheiten:**
- Große Schutzfläche → Anoden großzügig dimensionieren
- Beschichtung entscheidend: gute Epoxy-Beschichtung reduziert Strombedarf um 90–98%
- Anoden symmetrisch verteilen: max. 5 m Abstand bei unbeschichtetem Stahl
- Weld-On-Anoden bevorzugt (bester Kontakt, kein Loch im Rumpf)
- Doppelboden-Tanks: Innenkorrosion durch Ballastwasser → interne Anoden erforderlich

**Dimensionierung Stahlrumpf (Faustformel):**
```
M_anode (kg Zink) ≈ A_hull (m²) × f_coating × 0,15 × t (Jahre)
M_anode (kg Alu) ≈ A_hull (m²) × f_coating × 0,045 × t (Jahre)

Beispiel 15m Stahlsegler (A_hull = 50 m², Epoxy-Beschichtung f=0,05, 3 Jahre):
  Zink: 50 × 0,05 × 0,15 × 3 = 1,13 kg → 2 kg (aufgerundet + Sicherheit)
  Alu: 50 × 0,05 × 0,045 × 3 = 0,34 kg → 0,8 kg (aufgerundet + Sicherheit)
```

### N.3 GFK-Rümpfe

**Besonderheiten:**
- Rumpf selbst braucht keinen Schutz (nicht leitend)
- Alle Unterwasser-Metallteile (Propeller, Welle, Ruder, Seeventile, Kiel) müssen über Bonding verbunden sein
- Anoden schützen NUR die über Bonding angeschlossenen Bauteile
- Durchbrüche (Seeventile) sind die kritischsten Punkte
- Bei GFK-Osmose: Anoden haben keinen Einfluss auf Osmose (verschiedene Mechanismen)

**Typische Anoden-Positionen GFK-Yacht:**
1. Rumpfanode(n) nahe Kiel (schützt Kielbolzen, nächste Seeventile)
2. Wellenring (schützt Welle, Stevenrohr)
3. Propelleranode oder Propellernaben-Anode (schützt Propeller)
4. Ruderanode (schützt Ruderblatt und Ruderschaft)
5. Saildrive-Anode (bei Saildrive-Antrieb)
6. Trimmklappenanoden (bei Motorbooten)

> Confidence: `documented` (ABYC E-2, Hersteller-Empfehlungen)

---

## ANHANG O — Umweltaspekte

### O.1 Umweltauswirkungen von Opferanoden

| Material | Umweltproblem | EU-Regulierung | Trend |
|----------|--------------|----------------|-------|
| Zink (MIL-A-18001K) | Cadmium-Gehalt (0,025–0,07%), Zink-Eintrag | EU REACH: Cd-Beschränkung wird diskutiert | Rückläufig zugunsten von Aluminium |
| Aluminium (MIL-DTL-24779C) | Geringer Al-Eintrag, Indium (geringe Menge) | Keine Einschränkung | Zunehmend, als umweltfreundlicher angesehen |
| Magnesium (ASTM B843) | Mg ist natürlicher Bestandteil von Seewasser | Keine Einschränkung | Stabil (nur Süßwasser-Nische) |

### O.2 Cadmium-Diskussion

Zinkanoden nach MIL-A-18001K enthalten 0,025–0,07% Cadmium als Legierungselement. Cadmium ist ein giftiges Schwermetall (EU CLP: Carc. 1B, Muta. 2, Repr. 2). In Scandinavia und den Niederlanden wird der Einsatz cadmiumhaltiger Zinkanoden diskutiert.

**Alternativen:**
- Cadmiumfreie Zinkanoden: existieren, Aktivierung über erhöhten Al-Gehalt, aber geringere Stromausbeute
- Aluminium-Anoden: cadmiumfrei, höhere Kapazität, universeller einsetzbar
- ICCP-Systeme: keine Schwermetall-Freisetzung, aber höhere Kosten

**AYDI-Empfehlung:** In umweltsensiblen Revieren (Naturschutzgebiet, Trinkwassertalsperre) bevorzugt Aluminium-Anoden oder ICCP verwenden.

> Confidence: `documented` (EU REACH, Umweltberichte)

---

## ANHANG P — Erweiterte FAQ

### OA-026: Kann ich den Verbrauch meiner Anoden per App überwachen?
**Frage:** Gibt es Smart-Anoden oder Sensoren, die den Verbrauch melden?
**Antwort:** Ja, es gibt ICCP-Systeme mit App-Anbindung (z.B. Aqualuma AquaShield, Cathelco IceCat) und Einzelsensoren für Potenzialmessung (z.B. Maretron DCR100). Diese messen das Schutzpotenzial kontinuierlich und warnen bei Abweichungen. Kosten: 500–3.000 EUR. AYDI kann diese Sensordaten integrieren.
**Confidence:** `documented` (Hersteller-Datenblätter)

### OA-027: Wie verhalten sich Anoden bei Trockenliegern (Winterlager)?
**Frage:** Mein Boot liegt im Winter an Land. Passiert etwas mit den Anoden?
**Antwort:** Nein. Opferanoden verbrauchen sich nur im Elektrolyten (Wasser). An Land findet keine Reaktion statt. Anoden können über den Winter am Boot bleiben. Vor dem Kranen im Frühjahr: Zustand prüfen und ggf. ersetzen.
**Confidence:** `documented` (Elektrochemie-Grundlagen)

### OA-028: Mein Propeller ist aus Edelstahl — braucht er eine Anode?
**Frage:** Edelstahl ist doch korrosionsbeständig — brauche ich trotzdem Schutz?
**Antwort:** Ja. Edelstahl 316L ist zwar passivierbar, aber in Seewasser anfällig für Spaltkorrosion und Lochfraß, besonders unter Ablagerungen. Kathodischer Schutz ist empfohlen. ABER: Edelstahl ist edler als Bronze → bei bimetallischem Kontakt (Edelstahl-Propeller auf Bronze-Konus) muss das Bonding korrekt sein, sonst korrodiert die Bronze.
**Confidence:** `documented` (ABYC E-2)

### OA-029: Was ist der Unterschied zwischen Opferanoden und ICCP-Anoden?
**Frage:** ICCP-Anoden bestehen aus Titan — warum lösen die sich nicht auf?
**Antwort:** ICCP-Anoden (Titan mit MMO-Beschichtung = Mixed Metal Oxide) sind inert — sie leiten nur den externen Strom ins Wasser, lösen sich aber nicht auf (Lebensdauer 20+ Jahre). Der Schutzstrom kommt aus einer externen Stromquelle (Gleichrichter). Opferanoden hingegen liefern den Strom durch ihre eigene Auflösung.
**Confidence:** `documented` (DNV-RP-B401)

### OA-030: Kann Streustrom mein Boot versenken?
**Frage:** Wie gefährlich ist Streustrom wirklich?
**Antwort:** Im Extremfall ja. Dokumentierte Fälle: Bronze-Seeventile in <6 Monaten durchkorrodiert durch DC-Streustrom → Wassereinbruch. AC-Streustrom kann zusätzlich zu lebensgefährlichen Stromschlägen im Wasser führen (Electric Shock Drowning, ESD). In nordamerikanischen Marinas sind Todesfälle dokumentiert. Galvanischer Isolator und Fehlerstromschutzschalter sind essenziell.
**Confidence:** `documented` (ABYC E-2, ESD-Berichte)

> Confidence: `documented` (diverse Quellen)

---

## ANHANG Q — Zeitleiste: Entwicklung des kathodischen Schutzes

| Jahr | Meilenstein |
|------|-----------|
| 1824 | Humphry Davy demonstriert kathodischen Schutz von Kupfer-Beschlägen an Kriegsschiffen mit Zink/Eisen-Anoden |
| 1834 | Michael Faraday formuliert die Gesetze der Elektrolyse |
| 1890er | Erste systematische Anwendung von Zinkanoden an Dampfschiffen |
| 1928 | Robert Kuhn patentiert das erste ICCP-System |
| 1950er | US Navy entwickelt MIL-A-18001 (Zink-Anodenspezifikation) |
| 1960er | Aluminium-Anoden (Al-Zn-In) werden für Offshore-Plattformen entwickelt |
| 1973 | DNV veröffentlicht erste Recommended Practice für Kathodenschutz (Vorläufer RP-B401) |
| 1980er | ABYC E-2 wird zum De-facto-Standard für Freizeitboote |
| 1993 | EU-Freizeitboot-Richtlinie 94/25/EG fordert Korrosionsschutz-Nachweise |
| 2000er | ICCP-Systeme werden für Yachten unter 30m verfügbar und bezahlbar |
| 2010er | Smart-Monitoring-Systeme mit App-Anbindung erscheinen auf dem Markt |
| 2013 | EU-Richtlinie 2013/53/EU ersetzt 94/25/EG, verschärfte Anforderungen |
| 2020er | Cadmium-Debatte: Skandinavien diskutiert Cd-freie Zinkanoden, Trend zu Aluminium |
| 2021 | DNV-RP-B401 Update mit erweiterten Berechnungsgrundlagen |
| 2024 | KI-basierte Korrosionsüberwachung (inkl. AYDI) in Entwicklung |

> Confidence: `documented` (Fachliteratur)

---

## ANHANG R — Stichwortverzeichnis

| Stichwort | Kapitel/Anhang |
|-----------|---------------|
| ABYC E-2 | 1.2, 10.4, 12, 14, 15, 16, Anhang I |
| Aluminium-Anode | 7, 10.2, 13.1, Anhang B, J.2 |
| Aluminium-Rumpf | 10.2, 16 (OA-021), Anhang N.1 |
| Antifouling auf Anode | 14 (FB 7), 15 (P2), 16 (OA-003), Anhang L |
| Anodenauslegung (Berechnung) | 11.1, Anhang N.2 |
| Bonding-System | 10.4, 14 (FB 5), 15 (P5), 16 (OA-020) |
| Calcareous Deposit | 13.1, 14 (FB 9) |
| Cadmium | 17, Anhang J.1, O.2 |
| Clamp-On | 10.3, 12.3 |
| Confidence-Level | Anhang D |
| DNV-RP-B401 | 1.2, 11.1, 11.4, Anhang K |
| Fehlerbild-Atlas | 14 |
| Galvanische Reihe | Anhang B |
| Galvanischer Isolator | 14 (FB 6), 15 (P4), 16 (OA-005) |
| GFK-Rumpf | 16 (OA-015), Anhang N.3 |
| Haul-Out-Checkliste | 12.5 |
| ICCP | 14 (FB 11), 16 (OA-010, OA-024, OA-029), Anhang F (FS 8) |
| Lebensdauer | 13 |
| Lochfraß (Pitting) | 14 (FB 10), 15 (P3), 16 (OA-006) |
| Magnesium-Anode | 7, 13.1, Anhang J.3 |
| MIL-A-18001K | 1.2, 16 (OA-017), Anhang J.1 |
| MIL-DTL-24779C | 1.2, 13.1, Anhang J.2 |
| Motor-Kühlanode | 9, Anhang L |
| Oberflächenberechnung | 11.3 |
| Passivierung | 13.1, 14 (FB 2, FB 3), 15 (P2) |
| Potenzialmessung | 11.4, Anhang K.1 |
| Referenzelektrode | 11.4, 17, Anhang K.1 |
| Restlebensdauer | 13.3 |
| Risk Matrix | Anhang H |
| Saildrive-Anode | 12.4, Anhang F (FS 1, FS 3) |
| Schnell-Referenz | 18 |
| Schutzpotenzial | 1.3, 11.4, Anhang K.1 |
| Stahl-Rumpf | 10.2, Anhang F (FS 7), N.2 |
| Streustrom | 14 (FB 6), 15 (P4), 16 (OA-030), Anhang K.3 |
| Stromkapazität | 11.1, 17, Anhang J |
| Verbrauchsraten | 11.2, 13.2, Anhang C |
| Weld-On | 10.2 |
| Wellenerdungsbürste | 10.4, 15 (P3), Anhang F (FS 4) |
| Zink-Anode | 7, 13.1, Anhang J.1 |

> Confidence: `documented`

---

*Ende der AYDI-Wissensdatei 07.06 — Opferanoden und Korrosionsschutz (erweitert)*
*Nächste Datei: 07.07 — Unterwasserbeschichtungen und Antifouling*
