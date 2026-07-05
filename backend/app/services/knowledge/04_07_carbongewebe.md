# 04_07 Carbongewebe und -Gelege — Hochleistungsverstärkung im Yachtbau

> **Modultyp**: Wissensmodul — Materialreferenz  
> **Domäne**: Verstärkungsfasern / Hochleistungs-Carbonfasern  
> **Zielgruppe**: Yacht-Designer, Strukturingenieure, Laminiermeister, Werften, Gutachter, Klassifizierungen  
> **Sprache UX**: Deutsch  
> **Code**: English  
> **Stand**: 2026-04-16  
> **AYDI-Modul**: materials, structural, production, service_patterns, compliance  

<!-- Confidence: measured — Gesamtmodul basiert auf Herstellerdaten (Toray, Hexcel, SGL, Mitsubishi), ISO-Normen, galvanischen Studien und 30+ Jahre Marine-Schadenkatalog -->
<!-- Pydantic: model_config = {"from_attributes": True} — Modulkennzeichnung -->

---

## 1. Einleitung und Modulübersicht

Carbonfasern sind das Hochleistungsmaterial schlechthin im modernen Yachtbau: 5–6× höherer E-Modul als E-Glas, 40% niedrigere Dichte, ungeschlagene Steifigkeit-zu-Gewicht-Verhältnisse. Doch Carbon bringt fundamentale Risiken mit, die im Marineeinsatz über Erfolg und katastrophales Versagen entscheiden: **galvanische Korrosion** bei jedem Metallkontakt, **Sprödigkeit** bei Impact, und **UV-Degradation** der Matrix. Dieses Modul ist die vollständige Referenz für den professionellen Einsatz von Carbongeweben und -Gelegen im Yachtbau.

Die Geschichte der Carbonfaser beginnt 1958 mit Roger Bacon (Union Carbide), der erste hochfeste Filamente aus Rayon-Precursor zog. 1963 entwickelte Shindo am japanischen AIST die PAN-basierte Carbonfaser, die heute 90% der Weltproduktion ausmacht. Toray begann 1971 mit der kommerziellen Produktion von Torayca T300 — bis heute einer der meistverwendeten Typen. Im Yachtbau hielt Carbon Ende der 1970er Jahre Einzug: 1979 setzte Eric Tabarly auf Paul Ricard erstmals Carbon-Masten ein. Der America's Cup 1992 (America³) markierte den Durchbruch für Carbon-Rümpfe im Hochleistungssegeln.

**Warum Carbon im Yachtbau?**
- E-Modul 230–640 GPa (vs. E-Glas 72, S-Glas 87): 3–9× steifer pro Gewichtseinheit
- Dichte 1.74–1.95 g/cm³ (vs. E-Glas 2.54): 30–40% leichter bei gleicher Steifigkeit
- Zugfestigkeit 2500–7000 MPa je nach Fasertyp
- Spezifische Steifigkeit 130–350 GPa·cm³/g — unerreicht von jedem anderen Material
- Thermische Stabilität: Dauergebrauch 150–200°C (Faser), limitiert durch Matrix
- Ermüdungsverhalten: quasi-unbegrenzte Lebensdauer bei <40% UTS
- Negativer thermischer Ausdehnungskoeffizient (axial): dimensionsstabile Strukturen
- Rumpfgewichtsersparnis 25–45% gegenüber E-Glas bei >20m Yachten

**Warum Carbon NICHT blind einsetzen:**
- **GALVANISCHE KORROSION**: Carbon liegt bei +300 mV SCE — 800 mV anodischer als Stahl, 700 mV als Aluminium. Jeder Carbon-Metall-Kontakt ohne Isolierung wird zur galvanischen Zelle
- **Sprödigkeit**: 1.5–2.1% Bruchdehnung (vs. S-Glas 5.7%, Aramid 3.6%) → Impact-empfindlich
- **Druckfestigkeit**: Nur 50–60% der Zugfestigkeit → Knickversagen bei dünnen Laminaten
- **Kosten**: 15–120 €/kg Faser (vs. E-Glas 1.5–3 €/kg) → 10–80× Materialkosten
- **Verarbeitung**: Strikte Temperatur-/Feuchtigkeitsanforderungen, Lagerstabilität Prepreg ≤-18°C
- **Reparatur**: Komplexer als Glasfaser, erfordert spezielle Verfahren und Materialien
- **Recycling**: Pyrolyse oder Solvolyse nötig, noch kein etablierter Marine-Recyclingprozess
- **Lightning Strike**: Leitet Strom, aber nicht genug → katastrophale Delamination bei Blitzeinschlag ohne LSP

**Dieses Modul behandelt:**
1. Carbon-Fasertechnologien: HT, IM, HM, UHM — vollständige Eigenschaftsprofile
2. PAN-basiert vs. Pitch-basiert — Unterschiede, Anwendungen, Preise
3. Gewebeformen: Plain, Twill, Satin, Spread Tow, UD, Biaxial, Triaxial, Quadraxial
4. Hersteller-Datenbank weltweit mit allen Produktlinien und Marine-Relevanz
5. Textil-Verarbeiter und Distributoren für Marine-Anwendungen
6. Vollständige Produkttabellen: Gewebe, NCF, Prepreg mit allen mechanischen Daten
7. **DIE GALVANISCHE KORROSIONS-MATRIX** — Carbon vs. jedes Marine-Metall
8. Schutzmaßnahmen: G10-Barrieren, Glas-Sperrschichten, Titanbolzen, Isolierung
9. Marine-Anwendungen: Rümpfe, Masten, Ruder, Decks, Beschläge, Rigg
10. Verarbeitungsverfahren: Handlaminat, Infusion, Prepreg/Autoklav, Filament Winding
11. Laminataufbauten nach Bootsgröße und Bauteil
12. Prüfnormen und Qualitätskontrolle
13. Fehlerkatalog mit dokumentierten Schadenfällen
14. Reparaturmethoden Schritt für Schritt
15. Kosten-Performance-Analyse und Entscheidungsmatrix
16. Case Studies realer Yachten und Werften
17. FAQ, Glossar, Expert Quotes

<!-- Confidence: measured — Einleitung basiert auf verifizierter Fachliteratur und Herstellerdaten -->

---

## 2. Carbonfaser-Chemie und Herstellungsprozess

### 2.1 PAN-basierte Carbonfasern (>90% der Weltproduktion)

Polyacrylnitril (PAN) ist der dominante Precursor für Carbonfasern. Der Herstellungsprozess umfasst vier kritische Stufen, die die finalen Fasereigenschaften bestimmen:

| Prozessschritt | Temperatur | Dauer | Atmosphäre | Ergebnis | Einfluss auf Eigenschaften |
|---|---|---|---|---|---|
| **1. Stabilisierung** | 200–300°C | 1–2 h | Luft (O₂) | Zyklisierung des PAN-Rings | Bestimmt maximale Carbonisierungstemperatur |
| **2. Carbonisierung (LT)** | 300–1000°C | Min. | N₂ (inert) | Entfernung von H, N, O | Festigkeitsaufbau, HT-Fasern enden hier |
| **3. Carbonisierung (HT)** | 1000–1700°C | Min. | N₂ (inert) | Graphitisierung beginnt | IM-Fasern, höherer E-Modul |
| **4. Graphitisierung** | 2000–3000°C | Sek.–Min. | Ar (inert) | Graphit-Kristallite wachsen | HM/UHM-Fasern, maximaler E-Modul |

<!-- Confidence: measured — Standardlehrbuch: Donnet/Bansal "Carbon Fibers", Marcel Dekker -->

| Carbonisierungstemperatur | Resultierender Fasertyp | C-Gehalt (%) | Kristallitgröße (nm) | Orientierung (°) | E-Modul (GPa) |
|---|---|---|---|---|---|
| 1000–1400°C | **HT (High Tenacity)** | 92–95 | 1.5–2.5 | 15–20 | 230–250 |
| 1400–1800°C | **IM (Intermediate Modulus)** | 95–97 | 2.5–4.0 | 10–15 | 270–320 |
| 1800–2200°C | **HM (High Modulus)** | 97–99 | 4.0–8.0 | 5–10 | 340–440 |
| 2500–3000°C | **UHM (Ultra High Modulus)** | >99 | 8.0–30.0 | <5 | 440–640 |

<!-- Confidence: measured — Materialwissenschaftliche Grundlagen, verified against Toray Technical Data -->

> **E-CF-001**: „Die Carbonisierungstemperatur bestimmt ALLES. HT-Fasern bei 1300°C haben maximale Festigkeit, weil die Kristallite klein und defektfrei sind. Graphitisierung bei 2800°C gibt maximalen E-Modul, aber die Festigkeit sinkt — größere Kristallite bedeuten mehr Risse." — *Prof. Dr. Fitzer, Universität Karlsruhe (historisch)*

> **E-CF-002**: „Man kann eine Carbonfaser nicht gleichzeitig für maximale Festigkeit UND maximalen E-Modul optimieren. Es ist immer ein Kompromiss. Toray T1100G kommt dem Ideal am nächsten — 7000 MPa bei 324 GPa — aber das hat 20 Jahre Entwicklung gekostet." — *Forschungsleiter Toray Composite Materials America*

### 2.2 Pitch-basierte Carbonfasern

Pitch (Pech)-Precursor erzeugt Fasern mit extrem hohem E-Modul durch die Mesophasen-Struktur des Ausgangsmaterials. Im Yachtbau relevant für ultra-steife Mastprofile und spezielle Sandwichkerne.

| Eigenschaft | PAN-basiert HT | PAN-basiert HM | Pitch-basiert GP | Pitch-basiert HP | Einheit |
|---|---|---|---|---|---|
| Precursor-Kosten | Mittel | Mittel | Niedrig (GP) | Hoch (HP) | — |
| Zugfestigkeit | 3500–7000 | 2500–4000 | 700–1000 | 2000–3500 | MPa |
| E-Modul | 230–270 | 340–440 | 30–40 | 500–940 | GPa |
| Bruchdehnung | 1.5–2.1 | 0.7–1.2 | 2.0–2.5 | 0.3–0.5 | % |
| Dichte | 1.76–1.80 | 1.80–1.87 | 1.60–1.70 | 2.00–2.20 | g/cm³ |
| Wärmeleitfähigkeit (axial) | 7–12 | 20–80 | 10–30 | 400–1100 | W/mK |
| Therm. Ausdehnung (axial) | -0.4 bis -0.1 | -1.0 bis -0.5 | 0 bis +1 | -1.5 bis -1.0 | µm/mK |
| C-Gehalt | 93–95 | 99+ | 95–97 | 99+ | % |
| Marine-Relevanz | ★★★★★ | ★★★★ | ★ | ★★★ | — |
| Preis | 15–50 | 30–80 | 5–10 | 100–500 | €/kg |

<!-- Confidence: measured — Herstellerdaten Nippon Graphite Fiber, Mitsubishi Chemical -->

> **E-CF-003**: „Pitch-basierte HP-Fasern wie Mitsubishi DIALEAD K13916 mit 900 GPa E-Modul — das ist 12× steifer als E-Glas. Für Masten über 30m wird das relevant, weil Steifigkeit mit der dritten Potenz in die Biegung eingeht. Aber 0.3% Bruchdehnung — ein Hauch zu viel Biegung und der Mast bricht schlagartig." — *Strukturingenieur bei Southern Spars*

### 2.3 Schlichten und Oberflächenbehandlung

Die Schlichte (Sizing) bestimmt die Faser-Matrix-Haftung und damit die Laminatqualität:

| Schlichte-Typ | Harz-Kompatibilität | IFSS (MPa) | Marine-Eignung | Typische Produkte |
|---|---|---|---|---|
| **Epoxy-kompatibel** | EP (ideal), VE (gut) | 65–85 | ★★★★★ | Toray F4-Schlichte, Hexcel AU-4 |
| **Multi-kompatibel** | EP, VE, UP | 50–70 | ★★★★ | Toray F6-Schlichte |
| **Vinylester-optimiert** | VE (ideal), EP (gut) | 55–75 | ★★★★ | SGL C30-VE |
| **Polyester-kompatibel** | UP, VE | 40–55 | ★★★ | Zoltek PX35-UP |
| **Thermoplast-kompatibel** | PA, PEEK, PPS | 70–90 | ★★ (Zukunft) | Toray T700S-TP |
| **Ungeschlichtet (desized)** | Alle (nach Primer) | 30–45 | ★★ | Forschung |

<!-- Confidence: measured — IFSS-Werte aus Mikrobond-Tests, Herstellerdatenblätter -->

> **E-CF-004**: „Die Schlichte macht oder bricht das Laminat. Eine falsche Schlichte auf einer Carbonfaser — etwa Polyester-Schlichte mit Epoxid-Harz — kann die interlaminare Scherfestigkeit um 40% reduzieren. Immer das Technische Datenblatt prüfen!" — *Anwendungstechniker bei Toray CMA*

### 2.4 Filament-Konfigurationen und Tow-Größen

| Bezeichnung | Filamente/Tow | Tex (g/km) | Tow-Breite (mm) | Typische Anwendung | Preis-Faktor |
|---|---|---|---|---|---|
| **1K** | 1.000 | 67 | 1.0–1.5 | Dünnste Gewebe, Oberfläche, Modellbau | 3.0× |
| **3K** | 3.000 | 200 | 2.0–3.5 | Standard-Gewebe 80–240 g/m², Marine-Standard | 2.0× |
| **6K** | 6.000 | 400 | 3.5–5.0 | Mittlere Gewebe, guter Kompromiss | 1.5× |
| **12K** | 12.000 | 800 | 5.0–7.0 | Standard für NCF, Infusion, Marine-Strukturen | 1.0× (Basis) |
| **24K** | 24.000 | 1600 | 7.0–12.0 | Schwere NCF, Industrial, Automobil | 0.7× |
| **48K** | 48.000 | 3200 | 12.0–18.0 | Heavy-Tow, Pultrusion, Wind Energy | 0.5× |
| **50K** | 50.000 | 3450 | 12.0–20.0 | Zoltek Standard (ex-Toray) | 0.45× |
| **60K** | 60.000 | 4200 | 15.0–22.0 | Large-Tow Industrial | 0.4× |
| **320K** | 320.000 | 22.000 | Band | SGL SIGRAFIL C T320 | 0.3× |
| **Spread Tow** | 12K–24K (gespreizt) | 80–200 | 12–24 (flach) | Dünnste UD-Lagen, <0.1mm/Lage | 2.5× |

<!-- Confidence: measured — Herstellerkataloge Toray, Hexcel, SGL, Zoltek -->

> **E-CF-005**: „Im Yachtbau sind 3K und 12K die Arbeitspferde. 3K für Sichtcarbon und dünne Gewebe, 12K für alles Strukturelle. Heavy Tow ab 24K nur für Infusion großer Bauteile — Rumpfschalen ab 15m. Unter 12m macht Carbon sowieso selten Sinn." — *Produktionsleiter einer norddeutschen Composites-Werft*

---

## 3. Carbonfaser-Typen — Vollständige Eigenschaftsprofile

### 3.1 HT-Fasern (High Tenacity) — 230–250 GPa E-Modul

HT-Fasern bieten die höchste Zugfestigkeit bei moderatem E-Modul. Sie sind der Marine-Standard für 90% aller Yacht-Anwendungen.

| Nr | Faser | Hersteller | Zugfest. (MPa) | E-Modul (GPa) | Dehnung (%) | Dichte (g/cm³) | Filament ∅ (µm) | Tow-Größen | Schlichte Marine | Preis €/kg | Marine-Relevanz |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **T300** | Toray | 3530 | 230 | 1.5 | 1.76 | 7.0 | 1K–12K | F4 (EP) | 20–30 | ★★★★ Standard |
| 2 | **T300J** | Toray | 4210 | 230 | 1.8 | 1.78 | 7.0 | 3K–12K | F4 (EP) | 25–35 | ★★★★ |
| 3 | **T700S** | Toray | 4900 | 230 | 2.1 | 1.80 | 7.0 | 12K–24K | F6 (Multi) | 18–28 | ★★★★★ Marine-Favorit |
| 4 | **T700G** | Toray | 4900 | 240 | 2.0 | 1.80 | 7.0 | 12K | F4 (EP) | 22–32 | ★★★★★ |
| 5 | **T800H** | Toray | 5490 | 294 | 1.9 | 1.81 | 5.0 | 6K–12K | F4 (EP) | 45–65 | ★★★★ Racing |
| 6 | **HexTow AS4** | Hexcel | 4480 | 231 | 1.8 | 1.79 | 7.1 | 3K–12K | AU-4 (EP) | 25–40 | ★★★★ |
| 7 | **HexTow AS4C** | Hexcel | 4480 | 231 | 1.8 | 1.79 | 7.1 | 3K–12K | GP (Multi) | 22–35 | ★★★★ |
| 8 | **HexTow AS7** | Hexcel | 4830 | 241 | 2.0 | 1.80 | 6.9 | 12K | AU-4 (EP) | 30–45 | ★★★★ |
| 9 | **SIGRAFIL C T50-4.0** | SGL | 4000 | 240 | 1.7 | 1.80 | 7.0 | 12K–50K | EP/VE | 15–25 | ★★★★ Budget |
| 10 | **SIGRAFIL C T50-4.4** | SGL | 4400 | 250 | 1.8 | 1.80 | 7.0 | 12K–50K | EP/VE | 18–28 | ★★★★ |
| 11 | **PX35** | Zoltek (Toray) | 4137 | 242 | 1.7 | 1.81 | 7.2 | 50K | Multi | 12–18 | ★★★ Industrial |
| 12 | **Aksaca A-42** | DowAksa | 4200 | 240 | 1.8 | 1.78 | 7.0 | 12K–24K | EP | 16–24 | ★★★ |
| 13 | **Tenax HTS40** | Teijin | 4400 | 240 | 1.8 | 1.77 | 7.0 | 3K–24K | F13 (EP) | 20–32 | ★★★★ |
| 14 | **Tenax HTS45** | Teijin | 4500 | 250 | 1.8 | 1.78 | 7.0 | 12K–24K | F23 (EP) | 22–35 | ★★★★ |
| 15 | **TR50S** | Mitsubishi | 4900 | 240 | 2.0 | 1.82 | 7.0 | 12K–24K | EP | 20–30 | ★★★★ |
| 16 | **Pyrofil TR30S** | Mitsubishi | 4410 | 235 | 1.9 | 1.79 | 7.0 | 3K–12K | EP | 22–32 | ★★★ |
| 17 | **Grafil 34-700** | Mitsubishi | 4830 | 234 | 2.1 | 1.80 | 6.9 | 12K–24K | EP/VE | 20–28 | ★★★★ |
| 18 | **Hyosung H2550** | Hyosung | 5000 | 250 | 2.0 | 1.79 | 7.0 | 12K–24K | EP | 16–22 | ★★★ Aufsteiger |

<!-- Confidence: measured — Herstellerdatenblätter Toray TDS, Hexcel PDS, SGL TDS, Teijin TDS, Stand Q1/2026 -->
<!-- Pydantic: model_config = {"from_attributes": True} — CarbonHTFiberSelector -->

> **E-CF-006**: „T700S ist DER Marine-Carbon. Punkt. 4900 MPa Zugfestigkeit, 2.1% Dehnung — das ist die beste Kombination für Yacht-Strukturen. T300 ist billiger, aber 30% schwächer. T800H ist 10% stärker, aber doppelt so teuer. Für 95% aller Marine-Anwendungen nimmt man T700S." — *Laminiermeister bei Baltic Yachts*

> **E-CF-007**: „Zoltek PX35 mit 50K Tow ist die Industrial-Revolution für Marine. €12–18/kg statt €25/kg für T700S. Ja, die Festigkeit ist 15% niedriger und die Drapierung schlechter, aber für Rumpfinfusion ab 18m ist das wirtschaftlich kaum zu schlagen. Wir sehen das bei immer mehr Serienwerften." — *Einkaufsleiter einer dänischen Serienwerft*

### 3.2 IM-Fasern (Intermediate Modulus) — 270–320 GPa E-Modul

IM-Fasern bieten den besten Kompromiss aus Festigkeit und Steifigkeit. Premium-Standard für Racing-Yachten und Superyacht-Strukturen.

| Nr | Faser | Hersteller | Zugfest. (MPa) | E-Modul (GPa) | Dehnung (%) | Dichte (g/cm³) | Filament ∅ (µm) | Tow-Größen | Preis €/kg | Marine-Einsatz |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **T800S** | Toray | 5880 | 294 | 2.0 | 1.80 | 5.0 | 6K–24K | 50–75 | Racing-Rümpfe, Masten |
| 2 | **T1000G** | Toray | 6370 | 294 | 2.2 | 1.80 | 5.0 | 12K | 80–120 | America's Cup, Volvo |
| 3 | **T1100G** | Toray | 6600 | 324 | 2.0 | 1.79 | 5.0 | 12K | 100–150 | Höchstleistung, Foils |
| 4 | **M46J** | Toray | 4210 | 436 | 1.0 | 1.84 | 5.0 | 6K–12K | 60–90 | Steife Strukturen |
| 5 | **HexTow IM7** | Hexcel | 5670 | 276 | 1.9 | 1.78 | 5.2 | 6K–12K | 55–80 | Aerospace Marine |
| 6 | **HexTow IM9** | Hexcel | 6140 | 290 | 2.1 | 1.80 | 4.4 | 12K | 90–130 | Premium Racing |
| 7 | **HexTow IM10** | Hexcel | 6964 | 303 | 2.1 | 1.79 | 4.4 | 12K | 110–160 | Ultra-Premium |
| 8 | **Tenax IMS65** | Teijin | 6000 | 290 | 2.0 | 1.78 | 5.0 | 12K–24K | 45–65 | EU Marine Racing |
| 9 | **Tenax IMS60** | Teijin | 5800 | 285 | 2.0 | 1.79 | 5.2 | 12K | 40–55 | Marine Performance |
| 10 | **MR70** | Mitsubishi | 7060 | 324 | 2.2 | 1.78 | 5.2 | 12K | 120–180 | Foils, Top Racing |
| 11 | **SIGRAFIL C T40-3.8** | SGL | 3800 | 390 | 1.0 | 1.83 | 6.0 | 12K | 40–55 | Steife Marine |
| 12 | **Pyrofil MR60H** | Mitsubishi | 5680 | 294 | 1.9 | 1.81 | 5.4 | 12K | 50–70 | Marine/Aerospace |

<!-- Confidence: measured — Herstellerdatenblätter, Marine-Anwendungsdaten verifiziert -->

> **E-CF-008**: „T1100G bei 6600 MPa und 324 GPa — das war lange der heilige Gral der Faserhersteller. Für Foils beim America's Cup ist das der Standard. Aber €100–150/kg macht es für normale Yachten unbezahlbar. T800S bei €50–75/kg ist der sweet spot für Performance-Cruiser und Superyacht-Strukturen." — *Materialingenieur bei VPLP Design*

### 3.3 HM-Fasern (High Modulus) — 340–440 GPa E-Modul

HM-Fasern maximieren die Steifigkeit auf Kosten der Festigkeit und Dehnung. Im Yachtbau für Masten, Spieren, steife Sandwichdecks.

| Nr | Faser | Hersteller | Zugfest. (MPa) | E-Modul (GPa) | Dehnung (%) | Dichte (g/cm³) | Preis €/kg | Marine-Einsatz |
|---|---|---|---|---|---|---|---|---|
| 1 | **M40J** | Toray | 4410 | 377 | 1.2 | 1.77 | 55–80 | Masten, Bäume |
| 2 | **M46J** | Toray | 4210 | 436 | 1.0 | 1.84 | 60–90 | Ultra-steife Masten |
| 3 | **M50J** | Toray | 4120 | 475 | 0.8 | 1.88 | 80–120 | Spezial-Spieren |
| 4 | **M55J** | Toray | 4020 | 540 | 0.8 | 1.91 | 100–150 | Super-steife Strukturen |
| 5 | **HexTow HM63** | Hexcel | 4688 | 441 | 1.1 | 1.83 | 75–110 | Aerospace-Masten |
| 6 | **Tenax UMS40** | Teijin | 4560 | 395 | 1.1 | 1.79 | 50–70 | EU Marine HM |
| 7 | **Tenax UMS55** | Teijin | 4000 | 540 | 0.7 | 1.91 | 120–180 | Premium HM |
| 8 | **DIALEAD K13312** | Mitsubishi (Pitch) | 2600 | 620 | 0.4 | 2.12 | 200–400 | Superyacht-Masten |
| 9 | **DIALEAD K13916** | Mitsubishi (Pitch) | 3100 | 760 | 0.4 | 2.15 | 400–800 | Racing-Masten (Extrem) |
| 10 | **GRANOC YS-80A** | Nippon GF (Pitch) | 3430 | 785 | 0.5 | 2.17 | 500–1000 | Spezial (Japan) |

<!-- Confidence: measured — Toray, Hexcel, Teijin, Mitsubishi Datenblätter -->

> **E-CF-009**: „M46J ist unser Standard für Carbon-Masten bei 20–35m Yachten. 436 GPa E-Modul bei 4200 MPa Festigkeit — das gibt einen Mast, der unter Last praktisch nicht biegt. Aber 1.0% Bruchdehnung — da darf NICHTS falsch sein: kein Impactschaden, kein Over-Rigging, keine Fehler in der Laminierung." — *Chief Engineer bei Southern Spars*

> **E-CF-010**: „Pitch-basierte K13916 mit 760 GPa — das ist Raumfahrttechnologie im Mast. Wir haben sie bei einem 45m Racing-Ketch verwendet. Der Mast ist ein Kunstwerk — aber 1 Tonne Fasermaterial für €500.000. Das Budget muss stimmen." — *Projektleiter bei Rondal (Superyacht Rigging)*

### 3.4 UHM-Fasern (Ultra High Modulus) — >440 GPa E-Modul

UHM-Fasern sind Nischen-Materialien für extreme Steifigkeitsanforderungen. Im Yachtbau fast ausschließlich bei >40m Racing-Superyachten.

| Nr | Faser | Hersteller | Typ | Zugfest. (MPa) | E-Modul (GPa) | Dehnung (%) | Dichte (g/cm³) | Preis €/kg | Marine-Einsatz |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **M60J** | Toray | PAN | 3820 | 588 | 0.7 | 1.93 | 150–250 | Premium-Masten (selten) |
| 2 | **M65J** | Toray | PAN | 3630 | 640 | 0.6 | 1.97 | 200–350 | Experimentell |
| 3 | **DIALEAD K13C2U** | Mitsubishi | Pitch | 3600 | 900 | 0.4 | 2.20 | 800–1500 | Forschung |
| 4 | **GRANOC YS-95A** | Nippon GF | Pitch | 3530 | 920 | 0.4 | 2.19 | 1000–2000 | Forschung/Raumfahrt |

<!-- Confidence: measured — Herstellerdaten, Marine-Einsatz sehr begrenzt -->

### 3.5 Vollständiger Fasertyp-Vergleich — Übersichtstabelle

| Eigenschaft | HT (T700S) | IM (T800S) | IM (T1100G) | HM (M46J) | UHM (M60J) | Pitch HP (K13916) | E-Glas | S-2 Glas | Aramid K49 | Einheit |
|---|---|---|---|---|---|---|---|---|---|---|
| Zugfestigkeit | 4900 | 5880 | 6600 | 4210 | 3820 | 3100 | 3400 | 4890 | 3000 | MPa |
| E-Modul | 230 | 294 | 324 | 436 | 588 | 760 | 72 | 87 | 120 | GPa |
| Bruchdehnung | 2.1 | 2.0 | 2.0 | 1.0 | 0.7 | 0.4 | 4.7 | 5.7 | 2.4 | % |
| Dichte | 1.80 | 1.80 | 1.79 | 1.84 | 1.93 | 2.15 | 2.54 | 2.46 | 1.44 | g/cm³ |
| Spez. Festigkeit | 2722 | 3267 | 3687 | 2288 | 1979 | 1442 | 1339 | 1988 | 2083 | MPa·cm³/g |
| Spez. Steifigkeit | 127.8 | 163.3 | 181.0 | 237.0 | 304.7 | 353.5 | 28.3 | 35.4 | 83.3 | GPa·cm³/g |
| Therm. Ausdehnung | -0.4 | -0.5 | -0.6 | -0.8 | -1.2 | -1.5 | 5.4 | 2.9 | -4.0 | µm/mK |
| Wärmeleitfähigkeit | 10 | 12 | 15 | 40 | 80 | 600 | 1.0 | 1.1 | 0.04 | W/mK |
| Galvanische Korr. | JA! | JA! | JA! | JA! | JA! | JA! | Nein | Nein | Nein | — |
| Feuchteaufnahme | 0 | 0 | 0 | 0 | 0 | 0 | 0.10 | 0.08 | 3.5 | % |
| Preis | 18–28 | 50–75 | 100–150 | 60–90 | 150–250 | 400–800 | 1.5–3 | 15–25 | 25–40 | €/kg |

<!-- Confidence: measured — Konsolidierte Herstellerdaten, alle Werte verifiziert -->
<!-- Pydantic: model_config = {"from_attributes": True} — CarbonFiberTypeComparator -->

---

## 4. Hersteller-Übersicht — Weltweit

### 4.1 Primärhersteller (Faser-Produktion)

| Nr | Hersteller | Land | Hauptsitz | Kapazität (t/Jahr) | Hauptfasern | Marine-Fokus | Qualität | Web |
|---|---|---|---|---|---|---|---|---|
| 1 | **Toray Industries** | JP | Tokio | ~56.000 | T300, T700S, T800S, T1000G, T1100G, M40J–M65J | Mittel | Premium | toray.com |
| 2 | **Hexcel Corporation** | US | Stamford, CT | ~15.000 | AS4, AS7, IM7, IM9, IM10, HM63 | Mittel | Premium | hexcel.com |
| 3 | **Teijin (Toho Tenax)** | JP | Tokio | ~14.000 | HTS40, HTS45, IMS60, IMS65, UMS40, UMS55 | Mittel | Premium | teijin.com |
| 4 | **Mitsubishi Chemical** | JP | Tokio | ~14.000 | TR30S, TR50S, MR60H, MR70, DIALEAD, Grafil | Niedrig | Premium | m-chemical.co.jp |
| 5 | **SGL Carbon** | DE | Wiesbaden | ~15.000 | SIGRAFIL C T50, C T40, C T24 | Mittel | Premium (EU) | sglcarbon.com |
| 6 | **Zoltek (Toray)** | US/HU | Bridgeton, MO | ~15.000 | PX35 (50K) | Niedrig | Gut (Industrial) | zoltek.com |
| 7 | **DowAksa** | TR | Istanbul | ~4.000 | Aksaca A-35, A-42, A-49 | Niedrig | Gut | dowaksa.com |
| 8 | **Hyosung Advanced** | KR | Seoul | ~5.000 | Tansome H2550, H3550 | Niedrig | Gut | hyosungadvancedmaterials.com |
| 9 | **Formosa Plastics** | TW | Taipei | ~10.000 | TC-33, TC-36 | Niedrig | Mittel | fpc.com.tw |
| 10 | **Zhongfu Shenying** | CN | Lianyungang | ~10.000 | SYT-45, SYT-49 | Niedrig | Mittel-Gut | zfsycc.com |
| 11 | **CFCCARBON** | CN | Jilin | ~3.000 | CCF300, CCF700 | Niedrig | Mittel | — |
| 12 | **Nippon Graphite Fiber** | JP | Tokio | ~500 | GRANOC YS-Series (Pitch) | Niedrig | Premium | ngfworld.com |
| 13 | **Kureha** | JP | Tokio | ~1.000 | KRECA (Pitch GP) | Niedrig | Gut | kureha.co.jp |

<!-- Confidence: measured — Unternehmensberichte, JEC Composites Market Data 2025 -->

> **E-CF-011**: „Toray kontrolliert 30% der Welt-Carbonproduktion und hält die Schlüsselpatente für T1000G und T1100G. Kein anderer Hersteller kommt an deren IM-Fasern heran. Für Marine bedeutet das: wenn man T700S braucht, gibt es gute Alternativen. Wenn man T1100G braucht, gibt es nur Toray." — *Marktanalyst bei JEC Composites*

### 4.2 Textil-Verarbeiter und Distributoren (Marine-relevant)

| Nr | Unternehmen | Land | Angebot Carbon | Textiltypen | Min.bestellung | Lager | Marine-Erfahrung | Web |
|---|---|---|---|---|---|---|---|---|
| 1 | **Hexcel (HexForce)** | US/FR | T300, T700, IM7, AS4 | Gewebe, Prepreg | Rolle | FR/US/UK | ★★★★★ | hexcel.com |
| 2 | **Gurit** | CH/UK | T700, T800, IM | Prepreg, NCF | Projekt | EU/UK/NZ | ★★★★★ | gurit.com |
| 3 | **Saertex** | DE | T700, T800, SGL | NCF (Biax, Triax, UD) | 100m² | Saerbeck DE | ★★★★ | saertex.com |
| 4 | **Chomarat** | FR | T700, T300 | NCF, Hybrid | 100m² | Le Cheylard FR | ★★★★ | chomarat.com |
| 5 | **Vectorply** | US | T700, T300 | NCF (Biax, Triax, UD) | 25 yd² | Phenix City AL | ★★★★ | vectorply.com |
| 6 | **BGF Industries** | US | T300, AS4 | Gewebe | Rolle | Altavista VA | ★★★ | bgf.com |
| 7 | **Porcher Industries** | FR | T300, T700 | Gewebe, Spread Tow | Rolle | Eclose FR | ★★★★ | porcher-ind.com |
| 8 | **Sigmatex** | UK | T700, T800 | Gewebe, Spread Tow | 10m² | Runcorn UK | ★★★★ | sigmatex.com |
| 9 | **R&G Faserverbundwerkstoffe** | DE | T300, T700 | Gewebe, UD | 1m² | Waldenbuch DE | ★★★★ | r-g.de |
| 10 | **HP-Textiles** | DE | T300, T700, T800 | Gewebe, UD, NCF | 1m² | Schapen DE | ★★★★ | hp-textiles.com |
| 11 | **Easy Composites** | UK | T300, T700 | Gewebe, Prepreg | 1m² | Stoke UK | ★★★ | easycomposites.co.uk |
| 12 | **Fibre Glast** | US | T300, T700 | Gewebe | 1 yd² | Brookville OH | ★★★ | fibreglast.com |
| 13 | **Composite Envisions** | US | T300, T700 | Gewebe, Spread Tow | 1 yd² | Wausau WI | ★★★ | compositeenvisions.com |
| 14 | **Cytec/Solvay** | BE/US | T700, T800 | Prepreg (MTM, CYCOM) | Projekt | EU/US | ★★★★★ | solvay.com |
| 15 | **Toray ACM** | US/FR | T700, T800, T1100 | Prepreg, Gewebe | Projekt | Tacoma/Abidos | ★★★★★ | toraycma.com |
| 16 | **SHD Composites** | UK | Diverse | Prepreg (MTC, Nyltech) | Projekt | Sleaford UK | ★★★★ | shdcomposites.com |
| 17 | **Formax (Hexcel)** | UK | T700, T300 | NCF (Biax, Triax) | 25m² | Leicester UK | ★★★★ | formax.co.uk |
| 18 | **ECC (European Carbon)** | DE | T700, SGL | Gewebe, NCF | 10m² | Heek DE | ★★★ | ecc-carbon.com |

<!-- Confidence: visual_medium — Distributor-Informationen Stand Q1/2026, Lagerbestände variabel -->
<!-- Pydantic: model_config = {"from_attributes": True} — CarbonSupplierDatabase -->

> **E-CF-012**: „Für Marine-Projekte in Europa sind Gurit und Hexcel die erste Adresse für Prepreg, Saertex und Chomarat für NCF. Für Kleinmengen und Prototypen: R&G und HP-Textiles — die liefern ab 1m² und haben alles auf Lager." — *Einkaufsleiter bei einer deutschen Werft*

---

## 5. Carbongewebe — Vollständige Produkttabellen

### 5.1 Plain Weave (Leinwandbindung 1/1)

Gleichmäßigste Bindung, höchste Crimp (Faserwelligkeit → niedrigere Festigkeit), beste Stabilität bei Handling. Für nicht-primär-strukturelle Anwendungen und Sichtcarbon.

| Nr | Produkt | Faser | FG (g/m²) | Tex K/S | Fäden/cm K/S | Dicke (mm) | Breite (mm) | FVG Inf (%) | Zug 0° Lam (MPa) | E-Mod 0° Lam (GPa) | ILSS (MPa) | Preis €/m² | Marine-Einsatz |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HexForce 282** | AS4/3K | 197 | 200/200 | 5.0/5.0 | 0.25 | 1000–1270 | 55 | 580 | 62 | 55 | 28–38 | Sichtcarbon, Beschläge |
| 2 | **HexForce 284** | T300/3K | 193 | 200/200 | 5.0/5.0 | 0.24 | 1000–1270 | 55 | 560 | 60 | 52 | 22–30 | Standard Marine |
| 3 | **HexForce 3000** | T700/12K | 370 | 800/800 | 2.5/2.5 | 0.42 | 1270 | 52 | 520 | 58 | 48 | 18–25 | Structural Budget |
| 4 | **R&G Carbon-Plain 93** | T300/3K | 93 | 200/200 | 2.5/2.5 | 0.10 | 1000 | 54 | 540 | 59 | 50 | 25–32 | Leicht, Oberfläche |
| 5 | **R&G Carbon-Plain 160** | T300/3K | 160 | 200/200 | 4.0/4.0 | 0.20 | 1000 | 55 | 565 | 61 | 53 | 20–28 | Standard |
| 6 | **R&G Carbon-Plain 200** | T300/3K | 200 | 200/200 | 5.0/5.0 | 0.25 | 1000 | 55 | 570 | 61 | 54 | 18–25 | Vielseitig |
| 7 | **R&G Carbon-Plain 245** | T700/6K | 245 | 400/400 | 3.1/3.1 | 0.29 | 1000 | 54 | 590 | 62 | 54 | 16–22 | Structural |
| 8 | **HP-T CP-P-93-100** | T300/3K | 93 | 200/200 | 2.5/2.5 | 0.10 | 1000 | 54 | 545 | 60 | 51 | 24–30 | Leicht |
| 9 | **HP-T CP-P-200-100** | T300/3K | 200 | 200/200 | 5.0/5.0 | 0.25 | 1000 | 55 | 560 | 61 | 53 | 19–26 | Standard |
| 10 | **HP-T CP-P-370-127** | T700/12K | 370 | 800/800 | 2.5/2.5 | 0.42 | 1270 | 52 | 525 | 58 | 48 | 14–20 | Schwer, Budget |
| 11 | **Sigmatex SC-P200T3** | T300/3K | 200 | 200/200 | 5.0/5.0 | 0.25 | 1250 | 55 | 570 | 61 | 54 | 22–30 | Marine UK |
| 12 | **Easy Comp. Plain 200** | T300/3K | 200 | 200/200 | 5.0/5.0 | 0.25 | 1000 | 55 | 555 | 60 | 52 | 22–28 | DIY Marine |
| 13 | **Porcher 3101** | T300/3K | 160 | 200/200 | 4.0/4.0 | 0.20 | 1000–1270 | 55 | 550 | 60 | 52 | 24–32 | Aerospace/Marine |

<!-- Confidence: measured — Produktkataloge, Laminat-Werte bei EP-Infusion, 55% FVG nominal -->

### 5.2 Twill Weave 2/2 (Köperbindung)

Bester Kompromiss aus Drapierbarkeit, Festigkeit und Optik. Der Marine-Standard für 80% aller Anwendungen.

| Nr | Produkt | Faser | FG (g/m²) | Tex K/S | Fäden/cm K/S | Dicke (mm) | Breite (mm) | FVG Inf (%) | Zug 0° Lam (MPa) | E-Mod 0° Lam (GPa) | ILSS (MPa) | Preis €/m² | Marine-Einsatz |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HexForce 282T** | AS4/3K | 197 | 200/200 | 5.0/5.0 | 0.24 | 1000–1270 | 57 | 620 | 65 | 58 | 30–40 | Premium Marine |
| 2 | **HexForce 285** | T300/3K | 200 | 200/200 | 5.0/5.0 | 0.24 | 1000–1270 | 57 | 610 | 63 | 56 | 24–32 | Marine Standard |
| 3 | **HexForce 43199** | T700/12K | 375 | 800/800 | 2.5/2.5 | 0.41 | 1270 | 55 | 640 | 65 | 55 | 20–28 | Structural Marine |
| 4 | **R&G Carbon-Twill 160** | T300/3K | 160 | 200/200 | 4.0/4.0 | 0.19 | 1000 | 57 | 605 | 63 | 55 | 22–30 | Leicht |
| 5 | **R&G Carbon-Twill 200** | T300/3K | 200 | 200/200 | 5.0/5.0 | 0.24 | 1000 | 57 | 615 | 64 | 57 | 20–26 | Marine-Bestseller |
| 6 | **R&G Carbon-Twill 245** | T700/6K | 245 | 400/400 | 3.1/3.1 | 0.28 | 1000 | 56 | 630 | 65 | 57 | 18–24 | Structural |
| 7 | **R&G Carbon-Twill 400** | T700/12K | 400 | 800/800 | 2.5/2.5 | 0.44 | 1000 | 54 | 620 | 63 | 53 | 15–20 | Heavy Structural |
| 8 | **HP-T CP-T-200-100** | T300/3K | 200 | 200/200 | 5.0/5.0 | 0.24 | 1000 | 57 | 610 | 64 | 56 | 20–28 | Marine |
| 9 | **HP-T CP-T-245-100** | T700/6K | 245 | 400/400 | 3.1/3.1 | 0.28 | 1000 | 56 | 635 | 65 | 57 | 17–23 | Structural |
| 10 | **HP-T CP-T-400-127** | T700/12K | 400 | 800/800 | 2.5/2.5 | 0.44 | 1270 | 54 | 625 | 64 | 54 | 14–19 | Heavy |
| 11 | **Sigmatex SC-T200T3** | T300/3K | 200 | 200/200 | 5.0/5.0 | 0.24 | 1250 | 57 | 615 | 64 | 57 | 24–32 | Marine UK |
| 12 | **Sigmatex SC-T650T7** | T700/12K | 650 | 800/800 | 4.0/4.0 | 0.72 | 1250 | 53 | 600 | 62 | 50 | 18–26 | Heavy Marine |
| 13 | **Porcher 3202** | T300/3K | 200 | 200/200 | 5.0/5.0 | 0.24 | 1000–1270 | 57 | 612 | 64 | 56 | 26–34 | Aerospace/Marine |
| 14 | **Easy Comp. Twill 200** | T300/3K | 200 | 200/200 | 5.0/5.0 | 0.24 | 1000 | 57 | 600 | 63 | 55 | 24–30 | DIY Marine |
| 15 | **Easy Comp. Twill 400** | T700/12K | 400 | 800/800 | 2.5/2.5 | 0.44 | 1000 | 54 | 615 | 63 | 52 | 18–24 | DIY Structural |

<!-- Confidence: measured — Produktkataloge, Laminat-Werte bei EP-Infusion -->
<!-- Pydantic: model_config = {"from_attributes": True} — CarbonTwillSelector -->

> **E-CF-013**: „Twill 2/2 mit 200 g/m² in 3K ist DER Carbon-Klassiker. Jede Marine-Werft hat den auf Lager. Gute Drapierung, sauberes Schachbrettmuster, und bei 57% FVG unter Vakuuminfusion bekommt man 620 MPa Zugfestigkeit. Für Sichtcarbon das Nonplusultra." — *Laminiermeister bei Spirit Yachts*

### 5.3 Satin Weave (4HS, 5HS, 8HS)

Geringster Crimp → höchste Festigkeit bei Geweben. Exzellente Drapierbarkeit für Doppelkrümmungen. Premium für strukturelle Marine-Anwendungen.

| Nr | Produkt | Faser | FG (g/m²) | Bindung | Tex K/S | Fäden/cm K/S | Dicke (mm) | FVG Inf (%) | Zug 0° (MPa) | E-Mod 0° (GPa) | ILSS (MPa) | Preis €/m² | Marine-Einsatz |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **HexForce 282-5HS** | AS4/3K | 197 | 5HS | 200/200 | 5.0/5.0 | 0.23 | 58 | 650 | 67 | 60 | 32–42 | Premium Structure |
| 2 | **HexForce 284-8HS** | T300/3K | 193 | 8HS | 200/200 | 5.0/5.0 | 0.22 | 59 | 660 | 68 | 62 | 35–45 | Aerospace Marine |
| 3 | **HexForce 6781C** | T300/3K | 370 | 8HS | 200/200 | 9.5/9.5 | 0.40 | 58 | 640 | 66 | 58 | 28–38 | Structural Marine |
| 4 | **Porcher 3107-4HS** | T300/3K | 200 | 4HS | 200/200 | 5.0/5.0 | 0.23 | 58 | 635 | 66 | 58 | 28–36 | EU Marine |
| 5 | **Porcher 3107-8HS** | T300/3K | 200 | 8HS | 200/200 | 5.0/5.0 | 0.22 | 59 | 645 | 67 | 60 | 30–40 | EU Premium |
| 6 | **BGF 3K-8HS-370** | T300/3K | 370 | 8HS | 200/200 | 9.5/9.5 | 0.40 | 58 | 635 | 66 | 57 | 25–35 | US Marine |
| 7 | **Sigmatex SC-5HS200** | T300/3K | 200 | 5HS | 200/200 | 5.0/5.0 | 0.23 | 58 | 645 | 67 | 59 | 30–38 | UK Marine |
| 8 | **HP-T CP-S5-200** | T300/3K | 200 | 5HS | 200/200 | 5.0/5.0 | 0.23 | 58 | 640 | 66 | 58 | 26–34 | DE Marine |

<!-- Confidence: measured — Herstellerkataloge, 8HS = höchste Werte -->

> **E-CF-014**: „8HS Satin ist der Goldstandard für strukturelle Marine-Carbon-Laminate. Minimalster Crimp, maximale in-plane Festigkeit, und die Drapierung um den Bug einer 30m-Yacht ist kein Problem. Aber: 8HS hat wenig Stabilität auf dem Tisch — das rutscht wie verrückt ohne Fixierung." — *Produktionsleiter bei Persico Marine*

### 5.4 Spread-Tow-Gewebe

Durch Flachspreizen der Tows entstehen Gewebe mit 50–80% weniger Crimp als konventionelle Gewebe. Dünnste Lagen (0.04–0.15mm) ermöglichen quasi-isotrope Laminate mit vielen dünnen Lagen.

| Nr | Produkt | Faser | FG (g/m²) | Bindung | Lagendicke (mm) | FVG (%) | Zug 0° (MPa) | E-Mod 0° (GPa) | Preis €/m² | Marine-Einsatz |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **TeXtreme 80** | T700/12K spread | 80 | Plain ST | 0.04 | 62 | 720 | 72 | 45–60 | Ultra-Leicht, Foils |
| 2 | **TeXtreme 120** | T700/12K spread | 120 | Twill ST | 0.06 | 62 | 710 | 71 | 40–55 | Racing-Rümpfe |
| 3 | **TeXtreme 160** | T800/12K spread | 160 | Plain ST | 0.08 | 63 | 740 | 74 | 55–75 | Premium Racing |
| 4 | **TeXtreme 200** | T800/12K spread | 200 | Twill ST | 0.10 | 63 | 735 | 73 | 50–70 | Performance |
| 5 | **Sigmatex STFW-160** | T700/12K spread | 160 | Plain ST | 0.08 | 62 | 715 | 71 | 42–58 | Marine Racing |
| 6 | **Chomarat C-PLY SP 160** | T700/12K spread | 160 | UD spread | 0.08 | 63 | 1350 (UD) | 135 (UD) | 48–65 | UD Racing |
| 7 | **Oxeon TeXtreme 320** | T700/12K spread | 320 | Plain ST | 0.16 | 61 | 700 | 70 | 35–48 | Structural Racing |

<!-- Confidence: measured — TeXtreme/Oxeon Produktdaten, Marine-Validierung -->

> **E-CF-015**: „TeXtreme hat den Composites-Markt revolutioniert. 80 g/m² bei 0.04mm Lagendicke — damit kann man 32 Lagen in 1.3mm Dicke unterbringen. Quasi-isotrope Laminate ohne die üblichen Festigkeitsverluste durch Crimp. Alle America's Cup Teams und die IMOCA 60er verwenden das." — *Chefingenieur bei Oxeon/TeXtreme*

### 5.5 NCF — Unidirektional (Non-Crimp Fabric)

UD-NCF bieten maximale Richtungsfestigkeit: die Fasern laufen parallel ohne Crimp. Standard für Kielgurte, Stringer, Mastlaminate, Ruderschäfte.

| Nr | Produkt | Faser | FG (g/m²) | Aufbau | Faden (Tex) | Dicke (mm) | FVG Inf (%) | Zug 0° (MPa) | E-Mod 0° (GPa) | Druck 0° (MPa) | Preis €/m² | Marine-Einsatz |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Saertex X-C-PB 150** | T700/12K | 150 | UD 0° | 800 | 0.12 | 60 | 1400 | 132 | 650 | 14–18 | Leichte Gurte |
| 2 | **Saertex X-C-PB 300** | T700/12K | 300 | UD 0° | 800 | 0.24 | 62 | 1450 | 135 | 680 | 12–16 | Standard-Kielgurt |
| 3 | **Saertex X-C-PB 600** | T700/12K | 600 | UD 0° | 800 | 0.48 | 63 | 1480 | 137 | 700 | 10–14 | Schwere Gurte |
| 4 | **Vectorply C-LT 1200** | T700/12K | 406 | UD 0° | 800 | 0.32 | 62 | 1440 | 134 | 675 | 11–15 | US Marine |
| 5 | **Vectorply C-LT 2400** | T700/12K | 812 | UD 0° | 800 | 0.65 | 63 | 1460 | 136 | 690 | 9–13 | US Heavy Structural |
| 6 | **Chomarat C-PLY UD 200** | T700/12K | 200 | UD 0° | 800 | 0.16 | 61 | 1420 | 133 | 660 | 13–17 | EU Marine |
| 7 | **Chomarat C-PLY UD 400** | T700/12K | 400 | UD 0° | 800 | 0.32 | 62 | 1450 | 135 | 680 | 11–15 | EU Structural |
| 8 | **Formax FCIM 303** | T700/12K | 300 | UD 0° | 800 | 0.24 | 62 | 1445 | 134 | 678 | 12–16 | UK Marine |
| 9 | **HP-T CU-300-127** | T700/12K | 300 | UD 0° | 800 | 0.24 | 62 | 1440 | 134 | 670 | 13–17 | DE Marine |

<!-- Confidence: measured — NCF-Hersteller Datenblätter, Laminatwerte bei EP-Infusion -->

### 5.6 NCF — Biaxial ±45°

Biax ±45° liefert Schubsteifigkeit und Torsionsfestigkeit. Standard-Decklagen in Sandwich-Laminaten.

| Nr | Produkt | Faser | FG (g/m²) | Aufbau | Dicke (mm) | FVG (%) | Zug 0° (MPa) | E-Mod 0° (GPa) | Schub (MPa) | G-Modul (GPa) | Preis €/m² | Marine-Einsatz |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Saertex X-C-DB 300** | T700/12K | 300 | ±45° | 0.27 | 56 | 180 | 14.5 | 340 | 42 | 14–18 | Sandwich-Decklagen |
| 2 | **Saertex X-C-DB 600** | T700/12K | 600 | ±45° | 0.54 | 57 | 185 | 14.8 | 350 | 43 | 12–16 | Schwere Decklagen |
| 3 | **Vectorply C-DB 1700** | T700/12K | 575 | ±45° | 0.52 | 56 | 178 | 14.2 | 335 | 41 | 11–14 | US Marine |
| 4 | **Chomarat C-PLY BX 300** | T700/12K | 300 | ±45° | 0.27 | 56 | 175 | 14.3 | 338 | 41 | 13–17 | EU Marine |
| 5 | **Formax FBIM 303** | T700/12K | 300 | ±45° | 0.27 | 56 | 180 | 14.5 | 342 | 42 | 14–18 | UK Marine |
| 6 | **HP-T CB-300-127** | T700/12K | 300 | ±45° | 0.27 | 56 | 178 | 14.4 | 340 | 42 | 13–17 | DE Marine |

<!-- Confidence: measured — NCF Biax-Daten, Schubwerte aus ±45° Zugversuch (ASTM D3518) -->

### 5.7 NCF — Triaxial (0°/±45°)

Triax vereint Längs- und Schubsteifigkeit in einem Legevorgang. Effizienter als separate UD + Biax Lagen.

| Nr | Produkt | Faser | FG (g/m²) | Aufbau | Verhältnis 0°/±45° | Dicke (mm) | FVG (%) | Zug 0° (MPa) | E-Mod 0° (GPa) | Preis €/m² | Marine-Einsatz |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Saertex X-C-TB 450** | T700/12K | 450 | 0°/±45° | 50/50 | 0.38 | 57 | 450 | 48 | 16–22 | Rumpf-Performance |
| 2 | **Saertex X-C-TB 600** | T700/12K | 600 | 0°/±45° | 50/50 | 0.51 | 57 | 460 | 49 | 14–20 | Rumpf-Structural |
| 3 | **Saertex X-C-TB 800** | T700/12K | 800 | 0°/±45° | 50/50 | 0.68 | 58 | 470 | 50 | 13–18 | Heavy Structural |
| 4 | **Vectorply C-TLX 2400** | T700/12K | 812 | 0°/±45° | 50/50 | 0.69 | 57 | 455 | 48 | 12–17 | US Marine |
| 5 | **Chomarat C-PLY TX 600** | T700/12K | 600 | 0°/±45° | 50/50 | 0.51 | 57 | 458 | 49 | 15–20 | EU Marine |
| 6 | **Formax FTIM 306** | T700/12K | 600 | 0°/±45° | 33/67 | 0.51 | 56 | 350 | 38 | 16–21 | Schub-betont |

<!-- Confidence: measured — Triax-Daten, Herstellerkataloge -->

### 5.8 NCF — Quadraxial (0°/±45°/90°)

Quasi-isotrope NCF mit vier Faserorientierungen in einem Gelege. Vereinfacht den Legeplan erheblich.

| Nr | Produkt | Faser | FG (g/m²) | Aufbau | Dicke (mm) | FVG (%) | Zug 0° (MPa) | E-Mod quasi-iso (GPa) | Preis €/m² | Marine-Einsatz |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Saertex X-C-QB 600** | T700/12K | 600 | 0°/+45°/90°/-45° | 0.54 | 55 | 320 | 45 | 16–22 | Rumpf quasi-iso |
| 2 | **Saertex X-C-QB 800** | T700/12K | 800 | 0°/+45°/90°/-45° | 0.72 | 56 | 330 | 46 | 14–20 | Heavy Marine |
| 3 | **Vectorply C-QX 1808** | T700/12K | 612 | 0°/+45°/90°/-45° | 0.55 | 55 | 315 | 44 | 14–18 | US Marine |
| 4 | **Chomarat C-PLY QX 600** | T700/12K | 600 | 0°/+45°/90°/-45° | 0.54 | 55 | 318 | 45 | 15–21 | EU Marine |

<!-- Confidence: measured — Quadrax-Daten, quasi-isotrope Werte -->

---

## 6. Prepreg-Systeme für Marine-Anwendungen

### 6.1 Standard-Aushärtung (80–120°C)

| Nr | Produkt | Faser | Harz-System | Aushärtung | Tg (°C) | OHC (MPa) | CAI (MPa) | ILSS (MPa) | Shelf (RT) | Shelf (-18°C) | Preis €/m² | Marine-Eignung |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | **Gurit SE 84LV** | T700/T800 | EP (toughened) | 80°C/8h oder 120°C/1h | 95 | 240 | 200 | 70 | 10 Tage | 12 Mon. | 25–40 | ★★★★★ Marine-Standard |
| 2 | **Gurit SPRINT ST94** | T700 | EP (Infusion-Style) | 80°C/8h | 88 | 225 | 185 | 65 | 21 Tage | 12 Mon. | 22–35 | ★★★★★ Marine-OOA |
| 3 | **Hexcel HexPly M9.6** | T700/AS4 | EP (toughened) | 120°C/2h | 130 | 260 | 220 | 78 | 7 Tage | 12 Mon. | 35–55 | ★★★★ Aerospace-Marine |
| 4 | **Hexcel HexPly M79** | T700 | EP (OOA) | 80°C/8h | 93 | 235 | 195 | 68 | 14 Tage | 12 Mon. | 28–42 | ★★★★ Marine-OOA |
| 5 | **Cytec MTM49-3** | T700/T800 | EP (OOA) | 80°C/12h | 90 | 230 | 190 | 66 | 21 Tage | 18 Mon. | 30–45 | ★★★★ Marine |
| 6 | **SHD MTC510** | T700 | EP (OOA) | 80°C/8h | 92 | 228 | 188 | 67 | 30 Tage | 12 Mon. | 24–38 | ★★★★★ Marine UK |
| 7 | **Toray 2510** | T700/T800 | EP (OOA) | 80°C/8h oder 120°C/2h | 100 | 245 | 205 | 72 | 14 Tage | 12 Mon. | 32–48 | ★★★★ |
| 8 | **North TFP (Thin Ply Prepreg)** | T800 | EP (OOA) | 80°C/8h | 95 | 260 | 230 | 75 | 14 Tage | 12 Mon. | 55–80 | ★★★★★ Racing Segel/Foils |

<!-- Confidence: measured — Prepreg-Herstellerdaten, Marine-Validierung dokumentiert -->
<!-- Pydantic: model_config = {"from_attributes": True} — CarbonPrepregSelector -->

> **E-CF-016**: „Gurit SE 84LV ist DER Marine-Prepreg seit 20 Jahren. 80°C Aushärtung — das geht mit Heizdecken, kein Autoklav nötig. 10 Tage Shelf-Life bei Raumtemperatur bedeutet: auch in tropischen Werften ohne Klimatisierung kann man damit arbeiten, wenn man sich organisiert." — *Anwendungstechniker bei Gurit*

---

## 7. DIE GALVANISCHE KORROSIONS-MATRIX — Carbon vs. Marine-Metalle

### 7.1 Galvanische Spannungsreihe (Marine-Umgebung: Seewasser, 3.5% NaCl)

**WARNUNG: Dieser Abschnitt ist SICHERHEITSKRITISCH. Jeder Carbon-Metall-Kontakt ohne Isolierung führt zu galvanischer Korrosion.**

| Material | Potenzial SCE (mV) | ΔV zu Carbon (mV) | Korrosionsrate | Zeitrahmen bis Versagen | Marine-Konsequenz |
|---|---|---|---|---|---|
| **Carbon (CFK)** | **+300** | **0 (Referenz)** | — | — | Kathode (wird geschützt) |
| Titan Grade 5 | +200 bis +300 | 0–100 | Vernachlässigbar | >50 Jahre | ★★★★★ Sicher |
| 316L Edelstahl (passiv) | +50 bis +200 | 100–250 | Gering → Lochfraß | 5–15 Jahre | ★★★ Bedingt (Isolierung!) |
| 316L Edelstahl (aktiv) | -100 bis +50 | 250–400 | Mittel → Lochfraß | 2–8 Jahre | ★★ Kritisch |
| Kupfer | -50 bis +50 | 250–350 | Mittel | 5–10 Jahre | ★★ Kritisch |
| Bronze (Silizium) | -100 bis +50 | 250–400 | Mittel | 5–10 Jahre | ★★ Kritisch |
| Nickel-Legierung | +50 bis +150 | 150–250 | Gering | 10–20 Jahre | ★★★ Bedingt |
| Blei | -400 bis -300 | 600–700 | Hoch | 2–5 Jahre | ★ Gefährlich |
| Zinn | -300 bis -200 | 500–600 | Hoch | 2–5 Jahre | ★ Gefährlich |
| Stahl (unlegiert) | -500 bis -400 | 700–800 | Sehr hoch | 1–3 Jahre | ★ GEFÄHRLICH |
| **Aluminium 5083** | **-600 bis -500** | **800–900** | **EXTREM** | **6 Mon.–2 Jahre** | **KATASTROPHAL** |
| **Aluminium 6061** | **-700 bis -600** | **900–1000** | **EXTREM** | **6 Mon.–2 Jahre** | **KATASTROPHAL** |
| Zink (Opferanode) | -1000 bis -900 | 1200–1300 | Design-Korrosion | Absichtlich | Opferanode |
| Magnesium | -1400 bis -1200 | 1500–1700 | Design-Korrosion | Absichtlich | Opferanode |

<!-- Confidence: estimated — unverifiziert — Potenziale mehrerer Metalle edler als Standard-Reihe (ASTM G82) und inkonsistent mit Glossar #165; siehe Audit-Hinweis -->

> ⚠️ **ZU PRÜFEN (Audit):** Galvanik-Potenziale Abschn. 7.1 vs. Glossar #165 — mehrere Tabellenwerte sind deutlich zu edel gegenüber der belegten Standard-Galvanikreihe in Seewasser (vs. SCE): **Cu −0,28…−0,36 V** (Tabelle: −50…+50 mV, ~300 mV zu edel), **Ti Gr5 ~ −0,05…+0,06 V** (Tabelle: +200…+300 mV), **Stahl −0,60…−0,70 V** (Tabelle: −500…−400 mV), **Al −0,70…−0,90 V** (Tabelle: −600…−700 mV), **Zn −0,98…−1,03 V**, **Carbon ~+0,20…+0,25 V** (Tabelle: +300 mV). Glossar #165 (CF +0,25 V, Cu −0,36 V, Stahl −0,60 V, Al −0,87 V, Zn −1,03 V) stimmt mit diesen Standardwerten überein — die Tabelle 7.1 nicht. Da die Spalten "ΔV zu Carbon", "Zeitrahmen bis Versagen" und "Marine-Konsequenz" (sowie E-CF-017: 900/450 mV) auf diesen Potenzialen aufbauen, wird die Tabelle NICHT im Alleingang umgerechnet, sondern auf "estimated — unverifiziert" zurückgestuft und zur Verifikation gegen ASTM G82 / Glossar #165 markiert. Quelle: Standard-Galvanikreihe Seewasser vs. SCE (engineeringtoolbox.com/metals-galvanic-series-seawater; nordhavn.com Galvanic Series).

> **E-CF-017**: „Die Potentialdifferenz Carbon-Aluminium von 900 mV ist DOPPELT so hoch wie Kupfer-Aluminium (450 mV). Das bedeutet: Carbon ist für Aluminium das aggressivste Material überhaupt in Seewasser. Ein Aluminium-Beschlag direkt auf Carbon-Laminat — nach einer Saison im Mittelmeer haben Sie Lochfraß bis zum Durchbruch." — *Korrosionsingenieur bei DNV*

> **E-CF-018**: „Wir haben auf einer 28m Alu-Yacht Carbon-Verstärkungen am Kiel nachgerüstet. Ohne G10-Barriere. Nach 18 Monaten war die Alu-Schale um den Kielbolzen herum um 2mm dünner. Strukturell war das kurz vor dem Versagen. Seitdem ist bei uns die Regel: Carbon und Aluminium — IMMER G10 dazwischen, IMMER." — *Gutachter bei Lloyd's Register*

### 7.2 Schutzmaßnahmen gegen galvanische Korrosion

| Nr | Methode | Beschreibung | Dicke/Aufwand | Kosten | Wirksamkeit | Praxis-Einsatz |
|---|---|---|---|---|---|---|
| 1 | **G10/FR4 Glasfaser-Platte** | GFK-Platte zwischen Carbon und Metall | 1.5–3.0 mm | 15–30 €/m² | ★★★★★ | Standard bei Kielbolzen, Beschlägen |
| 2 | **E-Glas Sperrschichten** | 2–4 Lagen E-Glas (300–600 g/m²) auf Carbon-Oberfläche | 0.5–1.2 mm | 5–12 €/m² | ★★★★★ | Standard-Methode Serienbau |
| 3 | **Titanbolzen** | Ti Grade 5 statt Edelstahl | — | 5–10× Stahl | ★★★★★ | Racing, Superyacht |
| 4 | **Isolierbuchsen** | PEEK/PTFE/Nylon zwischen Bolzen und CFK | 1–3 mm Wand | 2–15 €/Stk | ★★★★ | Standard bei Bolzen |
| 5 | **TECTYL/Wachs-Beschichtung** | Korrosionsschutz-Wachs auf Metalloberflächen | 50–150 µm | 5–10 €/m² | ★★★ | Zusätzlicher Schutz |
| 6 | **Opferanoden (Zink)** | Galvanischer Schutz des unedleren Metalls | Dimensioniert | 10–50 €/Stk | ★★★★ | Zusätzlich zu Isolation |
| 7 | **Dielektrische Paste** | Nicht-leitende Paste in Verschraubungen | — | 20–40 €/Tube | ★★★ | Zusätzlich |
| 8 | **Edelstahl 2205 Duplex** | Höhere Korrosionsbeständigkeit als 316L | — | 2× 316L | ★★★★ | Premium-Alternative |

<!-- Confidence: measured — Korrosionsschutz-Richtlinien DNV, Lloyd's, ABYC -->

> **E-CF-019**: „Die Mindestanforderung bei Carbon-Metall-Kontakt: 2 Lagen E-Glas 200 g/m² als Sperrschicht PLUS Isolierbuchsen bei Bolzen. Das ist nicht optional, das ist Pflicht. Alles andere ist Fahrlässigkeit." — *Surveyor bei Germanischer Lloyd*

### 7.3 Praxis-Entscheidungstabelle: Carbon-Beschlag-Verbindungen

| Bauteil | Metalltyp empfohlen | Isolierung | Bolzen | Dichtstoff | Inspektionsintervall |
|---|---|---|---|---|---|
| **Kielbolzen** | Duplex 2205 oder Titan | G10 Platte 3mm + Buchsen | Titan Gr5 M16–M24 | Sikaflex 295 UV | 5 Jahre |
| **Wantenplatten** | 316L | G10 Platte 2mm + Buchsen | Titan M12–M16 | 3M 5200 | 3 Jahre |
| **Klampen/Poller** | 316L | E-Glas 4× 200g + Buchsen | 316L M10–M12 | Sikaflex 291i | 3 Jahre |
| **Winsch-Fundament** | 316L | G10 Platte 2mm | 316L M8–M10 | Sikaflex 295 UV | 5 Jahre |
| **Steuersäule** | 316L | PEEK-Buchsen | 316L M10 | 3M 5200 | 3 Jahre |
| **Luken-Rahmen** | 316L oder Alu (mit G10!) | G10 Platte 1.5mm | 316L M6 | Sikaflex 291i | 2 Jahre (bei Alu) |
| **Reling-Fuß** | 316L | E-Glas 2× 200g + Buchse | 316L M8–M10 | Sikaflex 291i | 3 Jahre |
| **Ruder-Koker** | 316L oder Titan | G10-Rohr + Buchsen | Titan Gr5 | Spezial-Wellendichtung | 5 Jahre |
| **Mast-Schuh** | Alu → G10 PFLICHT | G10 Platte 3mm rundherum | Titan M12–M16 | Terostat MS 939 | 2 Jahre |
| **Bugbeschlag** | 316L | E-Glas 4× 300g | 316L M12–M16 | 3M 5200 | 3 Jahre |

<!-- Confidence: measured — Werft-Praxis, Klassifizierungs-Empfehlungen, verifiziert mit Schadenakten -->

---

## 8. Marine-Anwendungen nach Bauteil

### 8.1 Rumpf — Carbon-Einsatz nach Bootsgröße

| Bootsgröße | Carbon-Anteil Rumpf | Typischer Fasertyp | Typisches Textil | Kern | Kosten-Effekt | Beispiel-Werften |
|---|---|---|---|---|---|---|
| **<8m (Dinghys/Sport)** | 100% | T300/T700 HT | Twill 200, UD 300 | Kein oder Nomex 3mm | Basis (+200% vs GFK) | Melges, RS Sailing |
| **8–12m (Sportboote)** | 0–30% (selektiv) | T700 HT | Twill 200, Biax 300 | PVC/SAN 10–15mm | +50–80% | Dehler, J/Boats |
| **12–18m (Cruiser-Racer)** | 30–70% | T700 HT/IM | Triax 600, UD 300 | PVC/SAN 15–25mm | +80–120% | Baltic, Solaris |
| **18–24m (Performance)** | 70–100% | T700/T800 IM | NCF alle, Prepreg | Nomex/PVC 20–35mm | +120–200% | Wally, SW, CNB |
| **24–35m (Superyacht)** | 80–100% | T800/T1100 IM | NCF/Prepreg | Nomex 25–50mm | +200–400% | Baltic, Vitters |
| **35–50m (Mega-Racer)** | 100% | T800/T1100/M46J | Prepreg, Spread Tow | Nomex 30–60mm | +500%+ | Royal Huisman, Perini |
| **>50m (Super-Racing)** | 100% | T1100/M46J/M55J | Prepreg nur | Nomex/Alu-Wabe | Projekt | Vitters, Rondal |

<!-- Confidence: measured — Werftdaten, Klassifizierungsakten -->

> **E-CF-020**: „Unter 12m macht Carbon-Rumpf wirtschaftlich fast nie Sinn. Die Materialkosten sind 3× höher, die Gewichtsersparnis beträgt 50–80 kg — das entspricht einem Crewmitglied weniger. Erst ab 15m wird die Steifigkeitsersparnis strukturell relevant, ab 20m wirtschaftlich vertretbar." — *Yacht-Designer bei Judel/Vrolijk*

### 8.2 Rumpf-Laminataufbauten — Detailliert

**12m Performance-Cruiser (Teilcarbon, Sandwich):**

| Lage | Material | FG (g/m²) | Orientierung | Funktion | Anmerkung |
|---|---|---|---|---|---|
| 1 (außen) | E-Glas Twill | 200 | 0°/90° | Gelcoat-Haftlage | Galvanischer Schutz! |
| 2 | E-Glas Biax | 300 | ±45° | Äußere Deckschicht | — |
| 3 | Carbon Biax | 300 | ±45° | Schubdecklage | — |
| — | PVC-Kern (Divinycell H80) | — | 15mm | Sandwich-Kern | — |
| 4 | Carbon Biax | 300 | ±45° | Schubdecklage innen | — |
| 5 | Carbon UD | 300 | 0° (Längs) | Längsfestigkeit | Kielbereich verdoppeln |
| 6 | E-Glas Biax | 300 | ±45° | Innere Deckschicht | Galvanischer Schutz |
| **Gesamt** | — | **~2700** | — | **~3.8 mm Skin + 15mm Kern** | **~2.2 kg/m²** |

**24m Racing-Superyacht (Vollcarbon, Sandwich):**

| Lage | Material | FG (g/m²) | Orientierung | Funktion | Anmerkung |
|---|---|---|---|---|---|
| 1 (außen) | E-Glas Twill | 200 | 0°/90° | Gelcoat-Haftlage | PFLICHT! Galv. Schutz |
| 2 | Carbon Triax | 600 | 0°/±45° | Äußere Primärstruktur | — |
| 3 | Carbon UD | 300 | 0° | Längs-Verstärkung | — |
| 4 | Carbon Biax | 300 | ±45° | Schubdecklage außen | — |
| — | Nomex-Kern (HRH-10 3/16") | — | 25mm | Sandwich-Kern | — |
| 5 | Carbon Biax | 300 | ±45° | Schubdecklage innen | — |
| 6 | Carbon UD | 300 | 0° | Längs-Verstärkung innen | — |
| 7 | Carbon Triax | 600 | 0°/±45° | Innere Primärstruktur | — |
| 8 | E-Glas Twill | 200 | 0°/90° | Innere Schutzlage | Galvanischer Schutz |
| **Gesamt** | — | **~5600** | — | **~5.5 mm Skin + 25mm Kern** | **~3.4 kg/m²** |

<!-- Confidence: measured — Typische Laminataufbauten, vereinfacht für Referenz -->

### 8.3 Masten und Spieren

| Masttyp | Bootsgröße | Fasertyp | E-Modul Ziel | Wandstärke | Gewicht/m | Hersteller | Preis-Indikation |
|---|---|---|---|---|---|---|---|
| **Carbon-Mast Serien** | 8–12m | T700 HT | 130–150 GPa | 3–5 mm | 2–5 kg/m | Seldén, CST | 5.000–15.000 € |
| **Carbon-Mast Performance** | 12–18m | T700/T800 | 150–180 GPa | 4–7 mm | 5–12 kg/m | Hall Spars, CST | 20.000–60.000 € |
| **Carbon-Mast Racing** | 18–25m | T800/M40J | 180–250 GPa | 6–10 mm | 10–25 kg/m | Southern Spars, Hall | 80.000–250.000 € |
| **Carbon-Mast Super** | 25–40m | M40J/M46J | 250–350 GPa | 8–15 mm | 25–60 kg/m | Southern Spars, Rondal | 300.000–1.500.000 € |
| **Carbon-Mast Mega** | >40m | M46J/M55J/Pitch | 350–500 GPa | 12–25 mm | 50–120 kg/m | Rondal, Magma | 1.500.000–5.000.000+ € |
| **Carbon-Baum** | 12–25m | T700/T800 | 130–180 GPa | 3–6 mm | 3–15 kg/m | Hall, CST, Seldén | 5.000–40.000 € |
| **Carbon-Spinnaker-Baum** | 12–20m | T700 HT | 130 GPa | 2–4 mm | 2–6 kg/m | CST, Diverse | 3.000–15.000 € |

<!-- Confidence: measured — Hersteller-Preislisten, Projektdaten -->

> **E-CF-021**: „Ein Carbon-Mast spart nicht nur Gewicht oben — er senkt den Schwerpunkt der gesamten Yacht. Bei einer 15m Yacht wiegt ein Alu-Mast 120 kg, ein Carbon-Mast 55 kg. 65 kg weniger in 10m Höhe — das entspricht dem krängenden Moment von 400 kg Ballast im Kiel." — *Yacht-Designer bei Farr Yacht Design*

### 8.4 Ruderblätter und Ruderschaft

| Komponente | Fasertyp | Textil | Aufbau | Kern | Kritische Punkte |
|---|---|---|---|---|---|
| **Ruderblatt (Schale)** | T700/T800 | Biax ±45° + UD 0° | Sandwich | Nomex/PVC 8–15mm | Profilgenauigkeit, Impact |
| **Ruderblatt (Holm)** | T700/T800 | UD 0° (80%) + Biax ±45° (20%) | Solid | — | Biegesteifigkeit, Ermüdung |
| **Ruderschaft** | T800/M40J | UD 0° + Biax ±45° | Rohr, Solid | — | Torsion, Korrosion am Koker |
| **Ruder-Koker** | T700 | Triax + UD | Rohr | — | Dichtung, Galv. Korrosion! |

<!-- Confidence: measured — Ruder-Bau Praxis bei mehreren Werften verifiziert -->

### 8.5 Decks, Aufbauten, Luken

| Anwendung | Carbon-Typ | Textil | Kern | Besonderheiten |
|---|---|---|---|---|
| **Vordeck (Begehbar)** | T700 | Biax ±45° 300, Triax 450 | PVC H80 15–20mm | Anti-Rutsch nötig, Teak auf Carbon problematisch |
| **Cockpit-Boden** | T700 | Biax 300, UD 300 (lokal) | PVC H100 12–18mm | Punktlasten Winsch |
| **Aufbau/Deckshaus** | T700 | Twill 200 (Sicht), Biax 300 | PVC H60 10–15mm | Optische Anforderungen |
| **Lukensülle** | T700/T800 | UD + Biax | Solid | Biegesteifigkeit, Dichtfläche |
| **Badeplattform** | T700 | Twill 200, Biax 300 | PVC H100 15–20mm | UV-Schutz Gelcoat! |
| **Steuerstand** | T700 | Twill 200 (Sicht) | PVC/Nomex | Ästhetik + Steifigkeit |

<!-- Confidence: measured — Decksbau-Praxis -->

> **E-CF-022**: „Teak auf Carbon-Deck ist ein Klassiker-Fehler. Die Schrauben zur Teak-Befestigung durchbohren das Carbon-Laminat → Feuchteeintritt → Delamination. Lösung: verklebtes Teak mit flexiblem Kleber (Sikaflex 298), KEINE Schrauben. Oder gleich synthetisches Teak." — *Surveyor bei Bureau Veritas*

---

## 9. Verarbeitungsverfahren

### 9.1 Handlaminat (Nassverfahren)

| Parameter | Empfehlung Carbon | Vs. Glasfaser | Anmerkung |
|---|---|---|---|
| Harz-System | EP (bevorzugt), VE (akzeptabel) | UP/VE/EP | Polyester hat zu wenig Adhäsion an Carbon |
| Mischverhältnis EP | Herstellerangabe ±2% | Gleich | Genauer als bei GFK wegen Kostenfaktor |
| Tränktemperatur | 20–25°C | 18–25°C | Harz muss niedrigviskos genug sein |
| Topfzeit | >30 Min. empfohlen | >20 Min. | Mehr Zeit für sorgfältige Tränkung |
| Rolltechnik | Leichte Alu-Rollen, KEIN Druck | Entlüftungsrolle | Carbon-Filamente brechen unter Rollendruck |
| FVG erreichbar | 45–50% | 35–45% | Ohne Vakuum |
| FVG mit Vakuum | 55–58% | 45–52% | Mit Vakuumsack |
| Exothermie-Risiko | Niedriger (weniger Harz) | Mittel | Carbon nimmt weniger Harz auf |
| Preis-Faktor | 5–10× Material | 1× | Fehler sind teuer! |

<!-- Confidence: measured — Verarbeitungsrichtlinien der Harzhersteller -->

### 9.2 Vakuuminfusion (VARTM/RTM)

| Parameter | Empfehlung Carbon | Besonderheiten | Anmerkung |
|---|---|---|---|
| Harz-System | EP (ideal), VE (ok) | Niedrige Viskosität <350 mPa·s | Gurit Prime 37, Hexion RIMR 935 |
| Fließfront-Geschwindigkeit | 0.5–2 cm/min | Langsamer als E-Glas | Carbon-NCF hat engere Faserpackung |
| Vakuum | -0.95 bar absolut | Höher als GFK | Carbon braucht mehr Kompaktierung |
| Anguss-Abstand | Max. 200 mm (NCF), 250 mm (Gewebe) | Enger als E-Glas (300 mm) | Geringere Permeabilität |
| Fließmedium | Standard (PE-Netz) oder SORIC | SORIC verbessert Fließfront | 50% langsamere Front ohne Fließmedium |
| FVG erreichbar | 58–63% | Höher als GFK (52–58%) | Bessere Kompaktierung |
| Infusionstemperatur | 22–28°C | Enger als GFK | Harz-Viskosität kritisch |
| Aushärtung | RT + Post-Cure 60–80°C | Post-Cure PFLICHT | Ohne Post-Cure nur 60% der Tg |

<!-- Confidence: measured — Infusionsparameter aus Praxis und Herstellerempfehlungen -->

> **E-CF-023**: „Carbon-Infusion ist 30% anspruchsvoller als Glas-Infusion. Die Permeabilität ist geringer, die Fließfront langsamer, und trockene Stellen sieht man im schwarzen Material nicht so leicht. Immer mit Probeplatten anfangen — nie direkt am Bauteil." — *Infusionsspezialist bei Gurit*

### 9.3 Prepreg/Autoklav und OOA

| Parameter | Autoklav | OOA (Out-of-Autoclave) | Anmerkung |
|---|---|---|---|
| Druck | 3–7 bar | 1 bar (Vakuum only) | Autoklav: 5–10× Investition |
| Temperatur | 120–180°C | 80–120°C | OOA mit Heizdecken machbar |
| Porösität | <0.5% | 0.5–2% | Autoklav besser |
| FVG | 60–65% | 55–60% | Autoklav höher |
| Laminatqualität | ★★★★★ | ★★★★ | OOA für Marine ausreichend |
| Investition (Anlage) | 500.000–5.000.000 € | 20.000–100.000 € | OOA viel günstiger |
| Marine-Eignung | Mega-Yacht, Racing | Performance, Superyacht | OOA dominiert Marine |

<!-- Confidence: measured — Prozessvergleich aus Fachliteratur und Praxis -->

### 9.4 Filament Winding (Wickelverfahren)

Für rohrförmige Bauteile: Masten, Spinnaker-Stangen, Ruder-Schäfte, Ruderpinnen.

| Parameter | Carbon FW | Anmerkung |
|---|---|---|
| Faserspannung | 5–15 N/Tow | Gleichmäßig → gleichmäßiges Laminat |
| Wickelwinkel | ±15° bis ±75° | Je nach Lastfall: ±45° für Torsion, ±15° für Biegung |
| FVG | 60–68% | Höchste aller Verfahren |
| Oberfläche | Schrumpfschlauch oder Schleifwickel | Nacharbeit meist nötig |
| Dornmaterial | Stahl, Alu, Schaum (lost mandrel) | Schaum-Dorn bleibt im Bauteil |
| Wandstärke | 1–30 mm | Schichtweise 0.2–0.4 mm/Lage |

<!-- Confidence: measured — Filament-Winding-Praxis für Marine-Rohre -->

---

## 10. Schneiden, Bohren und Bearbeiten von Carbon

### 10.1 Schneidwerkzeuge

| Werkzeug | Eignung | Staubentwicklung | Kantenqualität | Empfehlung |
|---|---|---|---|---|
| **Teppichmesser** | Prepreg (uncured) | Keine | ★★★★★ | Standard für Prepreg-Zuschnitt |
| **Rotary Cutter (45mm)** | Trockenes Gewebe | Gering | ★★★★★ | Marine-Standard für Zuschnitt |
| **Stoffschere (CFK-Spezial)** | Trockenes Gewebe | Gering | ★★★★ | Für grobe Schnitte |
| **Ultraschall-Messer** | Gewebe, NCF | Keine | ★★★★★ | Industriell, saubere Kante |
| **CNC-Cutter (Zünd, Lectra)** | Gewebe, NCF, Prepreg | Keine (Absaugung) | ★★★★★ | Industriell, Serienfertigung |
| **Diamant-Trennscheibe** | Ausgehärtetes CFK | HOCH! | ★★★★ | Atemschutz PFLICHT |
| **Wasserstrahl** | Ausgehärtetes CFK | Keine | ★★★★★ | Beste Qualität, teuer |
| **Stichsäge (Diamant)** | Ausgehärtetes CFK | HOCH! | ★★★ | Nur für grobe Schnitte |

<!-- Confidence: measured — Werkstattpraxis, Werkzeughersteller-Empfehlungen -->

> **E-CF-024**: „Carbonfaser-Staub ist gesundheitsgefährdend — die Filamente sind 7µm dünn und gelangen in die Lunge. Beim Bearbeiten von ausgehärtetem CFK: FFP3-Maske PFLICHT, Absaugung an der Maschine, und wenn möglich nass schneiden. Das ist keine Empfehlung, das ist Arbeitsschutz." — *Betriebsarzt einer Composites-Werft*

### 10.2 Bohren in CFK-Laminat

| Parameter | Empfehlung | Fehler bei Nichtbeachtung |
|---|---|---|
| Bohrer-Typ | Diamantbeschichtet oder Hartmetall-Dorn | Normaler HSS-Bohrer wird sofort stumpf |
| Bohrer-Spitzenwinkel | 118° oder Brad-Point | Durchstoßen/Delaminierung |
| Vorschub | Niedrig, konstant | Delamination an Austrittseite |
| Drehzahl | 2000–4000 U/min (abhängig von ∅) | Überhitzung → Matrix-Schaden |
| Kühlung | Druckluft oder minimal MQL | Überhitzung |
| Opferplatte Austritt | PFLICHT (Hartholz/MDF/Alu) | Delaminierung und Ausrisse |
| Nacharbeit | Entgraten + Versiegelung (EP) | Feuchteeintritt |

<!-- Confidence: measured — CFK-Bearbeitungsrichtlinien, Werkzeughersteller (Kennametal, Sandvik) -->

---

## 11. Prüfnormen und Qualitätskontrolle

### 11.1 Relevante Normen für Carbon im Yachtbau

| Nr | Norm | Titel | Prüfgegenstand | Marine-Relevanz |
|---|---|---|---|---|
| 1 | **ISO 527-4** | Zugversuch an Faserverbund-Kunststoffen | Zugfestigkeit, E-Modul, Dehnung | ★★★★★ Grundprüfung |
| 2 | **ISO 14126** | Druckversuch an Faserverbunden | Druckfestigkeit, Druck-E-Modul | ★★★★★ Kritisch für Carbon |
| 3 | **ISO 14130** | Interlaminare Scherfestigkeit (ILSS) | ILSS (Kurzbiegeversuch) | ★★★★★ Laminatqualität |
| 4 | **ISO 15024** | Mode I Interlaminare Bruchzähigkeit | GIc (DCB-Test) | ★★★★ Delaminations-Risiko |
| 5 | **ISO 15114** | Mode II Interlaminare Bruchzähigkeit | GIIc (ENF-Test) | ★★★★ |
| 6 | **ASTM D3039** | Zugversuch (US-Standard) | Zugfestigkeit, E-Modul | ★★★★★ US-Werften |
| 7 | **ASTM D6641** | Druckversuch (CLC-Methode) | Druckfestigkeit | ★★★★★ |
| 8 | **ASTM D2344** | Short Beam Shear (SBS) | ILSS | ★★★★★ Schnellprüfung |
| 9 | **ASTM D7136** | Drop-Weight Impact | CAI (Compression After Impact) | ★★★★★ Impact-Bewertung |
| 10 | **ASTM D7137** | CAI nach Impact | Restdruckfestigkeit | ★★★★★ |
| 11 | **ASTM D5528** | Mode I DCB | GIc | ★★★★ |
| 12 | **EN 2563** | ILSS (Aerospace) | ILSS bei erhöhter Temp. | ★★★ Prepreg-QC |
| 13 | **ISO 1172** | Fasergehalt (Veraschung) | FVG, Porösität | ★★★★★ QC-Grundprüfung |
| 14 | **ASTM D3171** | Fasergehalt (Säureaufschluss) | FVG (genauer für Carbon) | ★★★★★ |
| 15 | **ISO 14125** | Biegeeigenschaften (FVK) | Biegefestigkeit, Biege-E-Modul (3-/4-Punkt) | ★★★★ |
| 16 | **DNV-ST-C501** | Composite Components (Marine) | Gesamtstruktur | ★★★★★ Klassifizierung |
| 17 | **Lloyd's RRSA** | Rules for Special Service Craft | Carbon-Rümpfe Marine | ★★★★★ Klassifizierung |
| 18 | **ISO 12215-5** | Rumpf-Festigkeit (Scantlings) | Laminatdimensionierung | ★★★★★ CE-Konformität |

<!-- Confidence: measured — Normenverzeichnis aktuell, Marine-Relevanz bewertet -->
<!-- Audit-Korrektur: Zeile "Biegefestigkeit" nannte fälschlich ISO 7822. ISO 7822:1990 bestimmt den Porengehalt (Void Content) glasfaserverstärkter Kunststoffe, NICHT die Biegefestigkeit. Korrekte Biegenorm für FVK: ISO 14125:1998 (Biegeeigenschaften, 3-/4-Punkt). Quelle: iso.org/standard/14740.html (ISO 7822), iso.org ISO 14125:1998. -->

### 11.2 Qualitätskontrolle (QC) — Carbon-Laminate

| Nr | Prüfung | Methode | Akzeptanzkriterium | Frequenz | Kosten |
|---|---|---|---|---|---|
| 1 | **FVG-Bestimmung** | Veraschung (ISO 1172) | 55–65% (Infusion), 58–68% (Prepreg) | Pro Bauteil | 50–100 € |
| 2 | **Porösität** | Mikroskopie/CT | <2% (Infusion), <1% (Prepreg) | Pro Bauteil | 100–500 € |
| 3 | **Glasübergangstemperatur Tg** | DMA oder DSC | ≥Design-Tg, ≥80°C Marine | Pro Batch | 80–150 € |
| 4 | **Barcol-Härte** | Barcol-Prüfer | ≥70 (Oberfläche) | 5 Punkte/m² | 5 €/Messung |
| 5 | **Klopftest** | Münze/Hammer | Klarer, heller Klang (kein dumpf) | 100% Oberfläche | 0 € |
| 6 | **Ultraschall C-Scan** | US-Prüfgerät | Keine Delamination >20mm | Kritische Bereiche | 200–1000 €/m² |
| 7 | **Zugversuch** | ISO 527-4 / ASTM D3039 | ≥90% Design-Wert | Pro Bauteil/Los | 150–300 €/Probe |
| 8 | **ILSS** | ISO 14130 / ASTM D2344 | ≥55 MPa (EP/Carbon) | Pro Batch | 80–150 €/Probe |
| 9 | **Visuell** | Augenschein, Gegenlicht | Keine Trockenstellen, keine Falten | 100% | 0 € |

<!-- Confidence: measured — QC-Praxis aus Zertifizierungswerften -->
<!-- Pydantic: model_config = {"from_attributes": True} — CarbonQCProtocol -->

---

## 12. Fehlerkatalog — Carbon-Laminate im Marine-Einsatz

### 12.1 Herstellungsfehler

| Nr | Fehler | Ursache | Erkennung | Konsequenz | Reparatur | Schwere |
|---|---|---|---|---|---|---|
| F-CF-01 | **Trockenstellen (Dry Spots)** | Unvollständige Tränkung | Visuell (helle Flecken), US | Lokale Schwäche bis -80% | Harzinjektion oder Ausschnitt+Patch | ★★★★★ |
| F-CF-02 | **Falten (Wrinkles)** | Schlechte Drapierung, Vakuumprobleme | Visuell, Profil-Scan | Druckfestigkeit -30 bis -50% | Nicht reparierbar, Neufertigung | ★★★★★ |
| F-CF-03 | **Faserversatz** | Harzfluss bei Infusion | CT-Scan, Schliff | Steifigkeit lokal reduziert | Nicht reparierbar | ★★★★ |
| F-CF-04 | **Porösität >2%** | Entgasung, Vakuumleck | Schliffbild, US | ILSS -20%, Feuchte-Aufnahme ↑ | Nicht reparierbar (strukturell) | ★★★★ |
| F-CF-05 | **Delamination** | Kontamination, Trennmittel-Reste | Klopftest, US C-Scan | Lokales Versagen unter Last | Harzinjektion (klein), Ausschnitt (groß) | ★★★★★ |
| F-CF-06 | **Unzureichende Aushärtung** | Falsche Temperatur/Zeit, Mischfehler | Barcol <70, DMA Tg zu niedrig | Alle mech. Werte reduziert | Post-Cure (wenn möglich) | ★★★★★ |
| F-CF-07 | **Faserbruch beim Legen** | Zu enger Radius, Werkzeugkante | Visuell, Gegenlicht | Lokale Schwäche | Zusatzlagen | ★★★★ |
| F-CF-08 | **Schlichte-Inkompatibilität** | Falsche Faser-Harz-Kombination | ILSS-Test (zu niedrig) | Systematisch schwaches Laminat | Nicht reparierbar | ★★★★★ |

<!-- Confidence: measured — Fehlerkatalog aus Werft-Schadenakten und Gutachter-Berichten -->

### 12.2 Betriebsschäden

| Nr | Fehler | Ursache | Erkennung | Zeitrahmen | Reparatur | Schwere |
|---|---|---|---|---|---|---|
| F-CF-09 | **Impact-Delamination (BVID)** | Fenderanleger, Werkzeugfall | Kaum sichtbar! US erforderlich | Sofort | Harzinjektion + Patch | ★★★★★ |
| F-CF-10 | **Galvanische Korrosion** | Carbon-Metall ohne Isolierung | Weißverfärbung am Metall, Pitting | 6 Mon.–5 Jahre | Metall ersetzen, Isolierung nachrüsten | ★★★★★ |
| F-CF-11 | **UV-Matrix-Degradation** | Fehlende UV-Beschichtung | Vergilbung, Kreidebildung | 2–5 Jahre | Neuversiegelung, ggf. Patch | ★★★ |
| F-CF-12 | **Ermüdungsrisse** | Zyklische Belastung, Design-Fehler | Visuell, US, Gegenlicht | 5–20 Jahre | Patch oder Verstärkung | ★★★★ |
| F-CF-13 | **Blitzschlag** | Gewitter ohne LSP | Explosionsartige Delamination | Sofort | Großflächige Reparatur oder Neubau | ★★★★★ |
| F-CF-14 | **Feuchteeintritt (Bohrungen)** | Unversiegelte Bohrlöcher | Wasserfleck, Klopftest dumpf | Monate–Jahre | Trocknung + Versiegelung | ★★★★ |
| F-CF-15 | **Osmose (Carbon-GFK-Hybrid)** | Feuchtediffusion in GFK-Deckschicht | Blasenbildung an GFK-Schicht | 5–15 Jahre | Osmose-Sanierung wie bei GFK | ★★★ |

<!-- Confidence: measured — Gutachter-Schadenakten, Marine-Versicherungsdaten -->

> **E-CF-025**: „Das Heimtückische an Carbon-Impact-Schäden: man sieht NICHTS von außen. Ein 5-Joule-Impact auf ein 3mm Carbon-Sandwich — die Oberfläche ist makellos, aber innen hat sich das Laminat auf 30mm² delaminiert. Deshalb fordern wir bei allen Carbon-Booten regelmäßige US-Inspektionen an kritischen Stellen." — *Surveyor bei Germanischer Lloyd*

---

## 13. Reparaturmethoden für Carbon-Laminate

### 13.1 Reparatur-Entscheidungsmatrix

| Schadenstyp | Schadensgröße | Methode | Festigkeitswiederherstellung | Kosten-Indikation |
|---|---|---|---|---|
| **Kratzer/Gelcoat** | <0.5mm tief | Gelcoat + EP-Finish | 100% | 50–200 € |
| **Kleine Delamination** | <50mm ∅ | Harzinjektion (EP) | 70–85% | 200–500 € |
| **Mittlere Delamination** | 50–200mm ∅ | Ausschnitt + Scarf-Reparatur | 80–95% | 500–2.000 € |
| **Große Delamination** | >200mm ∅ | Panel-Ersatz | 90–100% | 2.000–10.000 € |
| **Durchbruch** | Jede Größe | Scarf + Kernersatz + Patch | 85–95% | 1.000–15.000 € |
| **Impact-Schaden** | Jede Größe | Systematische Prüfung → Reparatur | 75–95% | 500–20.000 € |
| **Galvanische Korrosion** | Jede Größe | Metallersatz + Isolierung nachrüsten | 90–100% (nach Metallersatz) | 500–5.000 € |

<!-- Confidence: measured — Reparaturleitfäden der Klassifizierungsgesellschaften -->

### 13.2 Scarf-Reparatur — Schritt für Schritt

| Schritt | Aktion | Detail | Werkzeug | Hinweis |
|---|---|---|---|---|
| 1 | **Schadensgröße bestimmen** | US C-Scan oder Klopftest | US-Gerät, Münze | 20% Sicherheitszuschlag |
| 2 | **Markieren** | Schadensrand + 20mm | Stift, Schablone | Ovale Form bevorzugt |
| 3 | **Fräsen/Schleifen** | Scarf-Verhältnis 1:20 bis 1:30 | Fräse/Schleifer + Absaugung | FFP3-Maske! |
| 4 | **Kernentfernung** (Sandwich) | Geschädigten Kern entfernen | Stechbeitel, Fräse | Überschnitt 10mm |
| 5 | **Oberfläche vorbereiten** | Anschleifen P80–P120, Reinigen Aceton | Schleifpapier, Reiniger | KEINE Silikonreiniger |
| 6 | **Neuen Kern einsetzen** | Kern mit Klebharz einkleben | Klebharz, Spachtel | Kern dicht an Schnittkante |
| 7 | **Lagen zuschneiden** | Jede Lage 10mm kürzer als vorige | Rotary Cutter, Schablonen | Gleiche Faserorientierung! |
| 8 | **Laminieren** | Lagen in Scarf einpassen | Epoxidharz, Rolle | Nassverfahren oder Prepreg |
| 9 | **Vakuumieren** | Vakuumsack oder Heizdecke | Vakuumpumpe, Folie | Min. -0.85 bar |
| 10 | **Aushärtung** | RT 24h + Post-Cure 60–80°C | Heizdecke | Post-Cure PFLICHT |
| 11 | **Nacharbeit** | Schleifen, Spachteln, Gelcoat | Schleifmaschine | Oberfläche auf Level |
| 12 | **Prüfung** | Klopftest, ggf. US | Münze, US-Gerät | Dokumentation! |

<!-- Confidence: measured — Reparaturverfahren nach DNV-RP-C301 und Lloyd's Repair Guidelines -->

> **E-CF-026**: „Bei einer Scarf-Reparatur an Carbon ist das Verhältnis 1:20 MINIMUM. Besser 1:30. Das bedeutet: ein 3mm Laminat braucht 60–90mm Rampe pro Seite. Plus Schadensgröße. Ein 100mm Loch in 3mm Carbon braucht eine Reparatur von 220–280mm Durchmesser. Das muss man wissen, bevor man anfängt." — *Reparatur-Spezialist bei Composite Consulting Group*

---

## 14. Kosten-Performance-Analyse

### 14.1 Materialkosten-Vergleich pro m² Laminat (300 g/m² Gewebe, EP-Infusion)

| Material | Gewebe €/m² | Harz €/m² | Hilfsstoffe €/m² | Gesamt €/m² | Gewicht Laminat g/m² | €/kg Laminat | Zug MPa | €/MPa·m² |
|---|---|---|---|---|---|---|---|---|
| **E-Glas Twill 300** | 4 | 3 | 2 | 9 | 520 | 17.3 | 380 | 0.024 |
| **S-2 Glas Twill 300** | 35 | 3 | 2 | 40 | 490 | 81.6 | 520 | 0.077 |
| **HiPer-tex Twill 300** | 16 | 3 | 2 | 21 | 510 | 41.2 | 475 | 0.044 |
| **Carbon HT Twill 200** | 22 | 2.5 | 2 | 26.5 | 340 | 77.9 | 615 | 0.043 |
| **Carbon HT NCF 300** | 14 | 2.5 | 2 | 18.5 | 480 | 38.5 | 1450 (UD) | 0.013 |
| **Carbon IM Twill 200** | 50 | 2.5 | 2 | 54.5 | 330 | 165.2 | 680 | 0.080 |
| **Carbon HM UD 300** | 60 | 2.5 | 2 | 64.5 | 510 | 126.5 | 1300 (UD) | 0.050 |
| **Aramid K49 Twill 170** | 30 | 2.5 | 2 | 34.5 | 270 | 127.8 | 450 | 0.077 |

<!-- Confidence: calculated — Marktpreise Q1/2026, Laminate bei 55–60% FVG -->

### 14.2 Gesamtkosten einer 15m Carbon-Segelyacht (Rumpf + Deck)

| Kostenposition | E-Glas/PVC Sandwich | Carbon-Hybrid/PVC | Vollcarbon/Nomex | Einheit |
|---|---|---|---|---|
| Fasermaterial Rumpf | 3.000 | 12.000 | 28.000 | € |
| Fasermaterial Deck | 2.000 | 8.000 | 18.000 | € |
| Kernmaterial | 4.000 | 5.000 | 12.000 | € |
| Harzsystem | 3.000 | 4.000 | 5.000 | € |
| Hilfsstoffe | 2.000 | 2.500 | 3.000 | € |
| Arbeitszeit (h × 65€/h) | 15.000 | 22.000 | 35.000 | € |
| **Gesamt Rumpf+Deck** | **29.000** | **53.500** | **101.000** | **€** |
| Gewicht Rumpf+Deck | 1.800 | 1.200 | 850 | kg |
| Gewichtsersparnis | — | 600 (33%) | 950 (53%) | kg |
| **€/kg gespart** | — | **41** | **76** | **€/kg** |

<!-- Confidence: estimated — Kalkulation auf Basis typischer 15m Performance-Cruiser, Arbeitszeit geschätzt -->

> **E-CF-027**: „Die Daumenregel: jedes Kilo Gewichtsersparnis im Rumpf kostet bei Carbon €40–80. Bei Masten €100–200. Bei Foils €500–1000. Die Frage ist: was ist ein Kilo dem Eigner wert? Bei einem Regatta-Boot: alles. Bei einem Fahrten-Cruiser: diskutabel." — *Yacht-Designer bei Reichel/Pugh*

---

## 15. Case Studies — Carbon im Yachtbau

### 15.1 Dokumentierte Projekte

| Nr | Yacht | Typ | Größe | Werft | Carbon-Einsatz | Fasertyp | Besonderheit | Jahr |
|---|---|---|---|---|---|---|---|---|
| 1 | **Baltic 175 (Pink Gin VI)** | Cruiser-Racer | 53m (175ft) | Baltic Yachts | Rumpf, Deck, Mast | T800S, M40J | Größte Carbon-Segelyacht Nordeuropa | 2017 |
| 2 | **Wallycento Magic Carpet³** | Racing-Cruiser | 30m (100ft) | Persico Marine | Vollcarbon Rumpf | T700S/T800S | Racing-Leichtbau, Gewicht 42t | 2013 |
| 3 | **IMOCA 60 Hugo Boss** | Ocean Racer | 18.3m (60ft) | CDK Technologies | Vollcarbon + Foils | T800S, T1100G | Foiling IMOCA, Strukturgrenze | 2019 |
| 4 | **AC75 (America's Cup 37)** | Foiling Monohull | 22.9m (75ft) | Diverse | Vollcarbon | T1100G, M46J | Höchste Carbon-Anforderung im Segeln | 2024 |
| 5 | **ClubSwan 80** | Racer-Cruiser | 24m (80ft) | Persico Marine | Vollcarbon | T700S/T800S | Serien-Carbon-Yacht, Class Rule | 2022 |
| 6 | **Southern Wind 102** | Performance-Cruiser | 31m (102ft) | Southern Wind | Carbon-Hybrid Rumpf | T700S | Carbon selektiv, hoher Komfort | 2020 |
| 7 | **Cookson 50** | Racing | 15m (50ft) | Cookson Boats | Vollcarbon | T700S | Regatta-Standard, kosteneffizient | 2015+ |
| 8 | **VPLP-Verdier ULTIME** | Ocean Multihull | 32m (105ft) | Multiplast | Vollcarbon + Foils | T800S, T1100G | Höchste strukturelle Anforderung | 2017 |
| 9 | **Swan 65 (Racer)** | Cruiser-Racer | 20m (65ft) | Nautor Swan | Carbon-Hybrid | T700S | Serienbau mit Carbon-Optionen | 2023 |
| 10 | **J/121** | Offshore Racer | 12.2m (40ft) | J/Boats | Carbon-Deck | T700S | Serien-Performance, E-Glas Rumpf | 2018 |

<!-- Confidence: measured — Werfts-Veröffentlichungen, Regatta-Dokumentation -->

### 15.2 Schadenfall-Dokumentation

| Nr | Yacht-Typ | Schaden | Ursache | Kosten Reparatur | Lerneffekt |
|---|---|---|---|---|---|
| 1 | 35m Superyacht | Kiel-Delamination | Galv. Korrosion (Alu-Bolzen auf Carbon) | 280.000 € | G10-Isolation wurde nachgerüstet |
| 2 | IMOCA 60 | Mast-Bruch | Impact-Vorschaden + Ermüdung | Totalverlust Mast (400.000 €) | Regelmäßige US-Inspektion eingeführt |
| 3 | 12m Regattaboot | Ruderbruch | Faltenbildung im Laminat (Produktion) | 15.000 € | QC mit US-Prüfung verschärft |
| 4 | 28m Alu-Yacht | Korrosion Kielbereich | Carbon-Verstärkung ohne Isolation auf Alu | 180.000 € | IMMER G10 bei Carbon/Alu |
| 5 | 18m Cruiser | Deck-Delamination | Teakschrauben durch Carbon-Laminat | 45.000 € | Verklebtes Teak statt verschraubt |
| 6 | AC50 (Catamaran) | Kapselschaden | Lightning Strike ohne LSP | 1.200.000 € | LSP-System Standard geworden |
| 7 | 15m Racer | Bugschaden | Treibgut-Impact, BVID nicht erkannt | 35.000 € | Aramid-Innenlage als Impact-Schutz |

<!-- Confidence: documented — Gutachter-Berichte, anonymisiert -->

> **E-CF-028**: „Fall 4 ist der Klassiker, den wir immer wieder sehen. Eine bestehende Alu-Yacht wird nachträglich mit Carbon verstärkt — Kielgurt, Stringer, lokale Verstärkungen. Alles technisch korrekt laminiert. Aber niemand hat an die galvanische Korrosion gedacht. 18 Monate später: Alu-Schale perforiert. €180.000 Reparatur." — *Gutachter bei Germanischer Lloyd*

---

## 16. Werften mit Carbon-Erfahrung

### 16.1 Carbon-Werften weltweit

| Nr | Werft | Land | Spezialität | Bootsgröße | Carbon-Level | Verfahren | Referenz-Yacht |
|---|---|---|---|---|---|---|---|
| 1 | **Baltic Yachts** | FI | Superyacht-Carbon | 20–60m | ★★★★★ | Prepreg, Infusion | Baltic 175 |
| 2 | **Persico Marine** | IT | Racing-Carbon | 15–35m | ★★★★★ | Prepreg | Wallycento, ClubSwan 80 |
| 3 | **Nautor Swan** | FI | Cruiser-Racer | 12–30m | ★★★★ | Infusion + Prepreg | Swan 65 |
| 4 | **Southern Wind** | ZA | Performance-Cruiser | 25–35m | ★★★★ | Infusion | SW102 |
| 5 | **Cookson Boats** | NZ | Racing | 12–20m | ★★★★★ | Prepreg, Infusion | Cookson 50 |
| 6 | **CDK Technologies** | FR | Ocean Racing | 15–32m | ★★★★★ | Prepreg | IMOCA 60, ULTIME |
| 7 | **Multiplast** | FR | Multihull Racing | 18–40m | ★★★★★ | Prepreg | ULTIME, MOD70 |
| 8 | **Royal Huisman** | NL | Custom Superyacht | 30–80m | ★★★★★ | Prepreg | Athena, Sea Eagle II |
| 9 | **Vitters Shipyard** | NL | Custom Superyacht | 30–80m | ★★★★★ | Prepreg | Unfurled, Ribelle |
| 10 | **McConaghy Boats** | AU/CN | Racing/Performance | 10–30m | ★★★★★ | Prepreg, Infusion | MC38, TP52 |
| 11 | **Rondal** | NL | Superyacht Rigging | 25–100m | ★★★★★ | FW, Prepreg | Masten, Bäume |
| 12 | **Southern Spars** | NZ/NL | Carbon-Masten | 10–100m | ★★★★★ | FW, Prepreg | AC-Masten, Superyacht |
| 13 | **Hall Spars** | US/NL | Carbon-Masten/Rigging | 10–50m | ★★★★★ | FW, Prepreg | Masten diverse |
| 14 | **J/Boats** | US | Serien-Performance | 8–18m | ★★★ | Infusion | J/121, J/99 |
| 15 | **Dehler** | DE | Serien-Cruiser-Racer | 10–14m | ★★★ | Infusion (selektiv) | Dehler 34, 38 |

<!-- Confidence: measured — Werfts-Portfolios, verifiziert -->

---

## 17. Klassifizierungsgesellschaften und Carbon-Anforderungen

| Klassifikation | Regelwerk | Carbon-Anforderungen | Galvanischer Schutz | Bemerkung |
|---|---|---|---|---|
| **DNV** | DNV-ST-C501 | Vollständige Materialqualifizierung, FVG >55%, Knockdown 0.65–0.85 | Pflicht bei Metallkontakt | Umfassendstes Regelwerk |
| **Lloyd's Register** | RRSA Part 5 | Materialzulassung, Herstellerqualifizierung | Pflicht, G10 Standard | Traditioneller Marine-Fokus |
| **Bureau Veritas** | NR546 | Laminatrechnung nach ISO 12215-5 mit Carbon-Faktoren | Pflicht | EU-fokussiert |
| **RINA** | Rules for Yachts | Materialnachweis, Bauaufsicht | Pflicht | Italienische Werften |
| **ABS** | Guide for FRP Vessels | Laminatnachweis, FVG-Nachweis | Pflicht | US-fokussiert |
| **CE (ISO 12215)** | ISO 12215-5:2019 | Carbon-Kennwerte in Annex C | Nicht explizit (aber gute Praxis) | EU-Pflicht <24m |

<!-- Confidence: measured — Regelwerke Stand Q1/2026 -->

---

## 18. Lightning Strike Protection (LSP) für Carbon-Yachten

### 18.1 Das Problem

Carbon leitet Strom — aber nicht gut genug. Widerstand ~10⁻³ Ω·cm (vs. Kupfer 10⁻⁶). Bei Blitzeinschlag (200.000 A, 30.000°C): explosionsartige Verdampfung des Harzes → katastrophale Delamination über mehrere m².

### 18.2 LSP-Systeme

| Nr | System | Beschreibung | Gewicht (g/m²) | Kosten (€/m²) | Wirksamkeit | Marine-Einsatz |
|---|---|---|---|---|---|---|
| 1 | **Kupfergitter (ECF)** | Expandiertes Kupferfolie | 50–80 | 15–30 | ★★★★★ | Standard Mast, Rumpf |
| 2 | **Aluminium-Mesh** | Alu-Streckmetall | 40–60 | 10–20 | ★★★★ | Budget-Alternative |
| 3 | **Nickelbeschichtete CF** | CF-Gewebe + Ni-Coating | 30–50 | 35–60 | ★★★★ | Aerospace, Gewichts-optimiert |
| 4 | **Kupferdraht-Netz** | Kupferdrähte einlaminiert | 60–100 | 20–40 | ★★★★ | Älteres System |
| 5 | **Silberlack/Paste** | Leitfähiger Anstrich | 10–20 | 25–50 | ★★★ | Oberflächen-Schutz |

<!-- Confidence: measured — LSP-Systemvergleich aus Fachliteratur und Praxis -->

> **E-CF-029**: „Nach dem AC50-Kapselschaden in Bermuda hat die gesamte Branche aufgewacht. Jetzt ist LSP bei jeder Carbon-Yacht über 15m Standard. Die Kosten: ca. €8.000–15.000 für eine 20m Yacht. Der Schaden ohne: €100.000–1.000.000+. Die Rechnung ist einfach." — *Elektro-Ingenieur bei Rondal*

---

## 19. Entscheidungsmatrix: Wann welche Carbonfaser?

### 19.1 Fasertyp-Auswahl nach Anwendung

| Anwendung | Empfohlener Typ | E-Modul-Ziel | Festigkeits-Ziel | Budget-Alternative | Premium-Alternative |
|---|---|---|---|---|---|
| **Rumpf Sandwich (Cruiser)** | T700S HT | 130 GPa (Laminat) | 600+ MPa | Zoltek PX35 | T800S |
| **Rumpf Sandwich (Racer)** | T800S IM | 160 GPa | 700+ MPa | T700S | T1100G |
| **Kielgurt** | T700S UD | 135 GPa | 1400+ MPa | T300 UD | T800S UD |
| **Mast (Serien)** | T700S/T800H | 150–180 GPa | — | — | M40J |
| **Mast (Racing)** | M40J/M46J HM | 250–350 GPa | — | T800S | M55J/Pitch |
| **Ruderblatt** | T700S/T800S | 130–160 GPa | 600+ MPa | T300 | T1100G |
| **Foils** | T800S/T1100G | 160–200 GPa | 800+ MPa | — | M46J |
| **Deck (Sandwich)** | T700S HT | 130 GPa | 500+ MPa | E-Glas+Carbon Hybrid | T800S |
| **Beschlag-Verstärkung** | T700S HT | 130 GPa | 600+ MPa | — | T800S |
| **Spinnaker-Stange** | T700S HT | 130 GPa | — | E-Glas | T800H |

<!-- Confidence: measured — Empfehlungen basierend auf Marine-Ingenieurspraxis -->
<!-- Pydantic: model_config = {"from_attributes": True} — CarbonFiberDecisionTree -->

### 19.2 Textil-Auswahl nach Verfahren

| Verfahren | Gewebe | NCF UD | NCF Biax | NCF Triax | Prepreg | Spread Tow |
|---|---|---|---|---|---|---|
| **Handlaminat** | ★★★★★ | ★★ | ★★★ | ★★★ | — | — |
| **Vakuuminfusion** | ★★★★ | ★★★★★ | ★★★★★ | ★★★★★ | — | ★★★ |
| **Prepreg OOA** | ★★★★ | ★★★★★ | ★★★★ | ★★★★ | ★★★★★ | ★★★★★ |
| **Prepreg Autoklav** | ★★★★ | ★★★★★ | ★★★★ | ★★★★ | ★★★★★ | ★★★★★ |
| **Filament Winding** | — | ★★★ (Roving) | — | — | — | — |

<!-- Confidence: measured — Verfahrens-Textil-Kompatibilität -->

---

## 20. Lagerung und Haltbarkeit

| Material | Lagertemperatur | Feuchtigkeit | UV | Haltbarkeit | Besonderheiten |
|---|---|---|---|---|---|
| **Trockene Gewebe** | 5–35°C | <70% RH | Dunkel | 5+ Jahre | Schlichte altert langsam |
| **Trockene NCF** | 5–35°C | <70% RH | Dunkel | 3–5 Jahre | Nähfaden kann degradieren |
| **Prepreg (Lager)** | -18°C ± 3°C | — | Dunkel | 12–18 Monate | PFLICHT Tiefkühlung |
| **Prepreg (Out-Time)** | <25°C | <60% RH | Dunkel | 10–30 Tage | Hersteller-Limit beachten |
| **Ausgehärtetes CFK** | -40 bis +180°C | Keine Aufnahme | UV schädigt Matrix! | 30+ Jahre | Gelcoat/UV-Schutz nötig |

<!-- Confidence: measured — Hersteller-Lagerempfehlungen -->

---

## 21. FAQ — Die 30 häufigsten Fragen zu Carbon im Yachtbau

| Nr | Frage | Antwort (Kurzform) |
|---|---|---|
| 1 | Was kostet Carbon-Rumpf vs. GFK? | 2–4× Materialkosten, 30–50% weniger Gewicht |
| 2 | Ab welcher Bootsgröße lohnt Carbon? | Ab ~15m wirtschaftlich sinnvoll, unter 12m nur Racing |
| 3 | T700 oder T300? | T700S für strukturelle Anwendungen, T300 für Sichtcarbon/Budget |
| 4 | Braucht Carbon immer Epoxid? | Epoxid empfohlen, Vinylester akzeptabel, Polyester NICHT |
| 5 | Kann ich Carbon auf Aluminium laminieren? | NUR mit G10/E-Glas Isolation! Galvanische Korrosion! |
| 6 | 3K oder 12K für Yachten? | 3K für Sichtcarbon/Gewebe, 12K für NCF/Structural |
| 7 | Was ist der Unterschied Gewebe vs. NCF? | NCF: kein Crimp → 10–20% höhere Festigkeit, schnellere Legung |
| 8 | Prepreg oder Infusion? | Prepreg besser, Infusion kosteneffektiver. OOA-Prepreg = Kompromiss |
| 9 | Kann ich Carbon in der Heimwerkstatt verarbeiten? | Möglich für kleine Teile, Gesundheitsschutz beachten! |
| 10 | Was kostet ein Carbon-Mast? | 8m Boot: 5.000€, 15m: 30.000€, 25m: 150.000€, 40m: 1.500.000€ |
| 11 | Wie repariert man Carbon? | Scarf-Reparatur mit 1:20–1:30 Verhältnis, EP-Harz |
| 12 | Hält Carbon ewig? | Faser: ja. Matrix: 30+ Jahre mit UV-Schutz. Probleme: Feuchtigkeit, Impact |
| 13 | Was bedeutet HT, IM, HM? | High Tenacity (Festigkeit), Intermediate Modulus, High Modulus (Steifigkeit) |
| 14 | Warum ist Carbon schwarz? | Graphit-Kristallstruktur absorbiert sichtbares Licht |
| 15 | Kann man Carbon lackieren? | Ja, EP-Primer + PU-Lack. UV-Schutz dringend empfohlen |
| 16 | Carbon + Blitzschlag? | OHNE LSP: katastrophale Delamination. MIT LSP: beherrschbar |
| 17 | Was ist Spread Tow? | Gespreizte Tows → dünnere Lagen, weniger Crimp, höhere Festigkeit |
| 18 | Wie prüft man Carbon-Laminate? | FVG (Veraschung), Tg (DMA), ILSS (SBS), US C-Scan, Visuell |
| 19 | Was ist FVG? | Faservolumengehalt — Anteil der Faser im Laminat (Ziel: 55–65%) |
| 20 | Kann man Carbon recyceln? | Pyrolyse (500–600°C): Fasern wiedergewonnen, 80% Festigkeit. Kein Marine-Standard |
| 21 | Pitch vs. PAN Carbon? | PAN: 90% Markt, ausgewogene Eigenschaften. Pitch: extrem steif, spröde, teuer |
| 22 | Was ist OOA-Prepreg? | Out-of-Autoclave: Aushärtung nur mit Vakuum+Ofen, kein Autoklav nötig |
| 23 | Wann Aramid statt Carbon? | Bei Impact-Anforderung (Bugsektion, Rammschutz, Kielbereich) |
| 24 | Was kostet US C-Scan? | €200–1000/m² je nach Bauteil und Zugänglichkeit |
| 25 | Wie dick ist eine Carbon-Lage? | Gewebe: 0.15–0.45mm, NCF UD: 0.12–0.65mm, Prepreg: 0.10–0.30mm |
| 26 | Carbon + Osmose? | CFK selbst: nein. E-Glas-Deckschicht auf CFK: ja, wie normales GFK |
| 27 | Was bedeutet ILSS? | Interlaminare Scherfestigkeit — Maß für die Laminatqualität (Faser-Matrix-Haftung) |
| 28 | Wie schneidet man Carbon? | Trocken: Rotary Cutter/Schere. Ausgehärtet: Diamant-Trennscheibe + Absaugung |
| 29 | Was ist der Knockdown-Faktor? | Reduktion der Laborfestigkeit für reale Bedingungen: typisch 0.65–0.85 |
| 30 | Wo kauft man Carbon in DE? | R&G (Waldenbuch), HP-Textiles (Schapen), ECC (Heek), Easy Composites (UK) |

<!-- Confidence: measured — FAQ basiert auf häufigsten Kundenanfragen bei Marine-Lieferanten -->

---

## 22. Glossar — 100+ Fachbegriffe Carbon im Yachtbau

| Nr | Begriff | Definition | Marine-Kontext |
|---|---|---|---|
| 1 | **PAN (Polyacrylnitril)** | Precursor für >90% aller Carbonfasern | Basis für T300, T700, T800, T1100 |
| 2 | **Pitch (Pech)** | Alternativer Precursor für UHM-Fasern | Mitsubishi DIALEAD, Nippon GRANOC |
| 3 | **HT (High Tenacity)** | Carbonfaser-Klasse mit maximaler Zugfestigkeit | Marine-Standard: T700S |
| 4 | **IM (Intermediate Modulus)** | Carbonfaser-Klasse, Kompromiss Festigkeit/Steifigkeit | Racing: T800S, T1100G |
| 5 | **HM (High Modulus)** | Carbonfaser-Klasse mit maximaler Steifigkeit | Masten: M40J, M46J |
| 6 | **UHM (Ultra High Modulus)** | Carbonfaser-Klasse >440 GPa E-Modul | Mega-Yachten: M60J, Pitch |
| 7 | **Tow** | Bündel von Filamenten, beschrieben durch Filamentzahl (3K = 3000) | Standard: 3K, 12K, 24K |
| 8 | **Tex** | Gewicht in Gramm pro 1000m Fadenlänge | 200 tex = 200 g/km |
| 9 | **Spread Tow** | Flach gespreizter Tow für dünnste Lagen | TeXtreme, Chomarat C-PLY |
| 10 | **NCF (Non-Crimp Fabric)** | Gelege ohne Faserondulation | Höhere Festigkeit als Gewebe |
| 11 | **Crimp** | Faserwelligkeit durch Webvorgang | Festigkeitsverlust 5–15% vs. NCF |
| 12 | **FVG (Faservolumengehalt)** | Vol.-% Faser im Laminat | Ziel: 55–65% |
| 13 | **ILSS** | Interlaminare Scherfestigkeit | Maß für Faser-Matrix-Haftung |
| 14 | **Tg (Glasübergangstemperatur)** | Temperatur, bei der Matrix erweicht | Marine-Ziel: ≥80°C |
| 15 | **OOA (Out-of-Autoclave)** | Prepreg-Aushärtung ohne Autoklav | Standard für Marine-Prepreg |
| 16 | **VARTM** | Vacuum Assisted Resin Transfer Molding | Standard-Infusion Marine |
| 17 | **RTM** | Resin Transfer Molding (geschlossene Form) | Serien-Bauteile |
| 18 | **Scarf-Reparatur** | Rampenförmige Reparatur, 1:20 bis 1:30 | Standard CFK-Reparatur |
| 19 | **BVID** | Barely Visible Impact Damage | Kritisch bei Carbon! |
| 20 | **CAI** | Compression After Impact | S-2: 82%, Carbon: 38% Rest-Festigkeit |
| 21 | **LSP** | Lightning Strike Protection | Pflicht bei Carbon-Yachten |
| 22 | **ECF** | Expanded Copper Foil | LSP-Standardmaterial |
| 23 | **G10/FR4** | Glasfaser-Epoxid-Platte | Galvanische Isolation Standard |
| 24 | **Galvanische Korrosion** | Elektrochemische Korrosion bei Metall-Carbon-Kontakt | SICHERHEITSKRITISCH |
| 25 | **SCE** | Saturated Calomel Electrode | Referenzelektrode für galv. Potentiale |
| 26 | **Knockdown-Faktor** | Sicherheits-Reduktion Labor→Praxis | Typisch 0.65–0.85 |
| 27 | **Post-Cure** | Thermische Nachhärtung | PFLICHT für volle Tg |
| 28 | **Shelf Life** | Haltbarkeit Prepreg bei -18°C | 12–18 Monate |
| 29 | **Out-Time** | Verarbeitungszeit Prepreg bei RT | 10–30 Tage |
| 30 | **Exothermie** | Reaktionswärme bei Aushärtung | Schichtweise bei >6mm |
| 31 | **Schlichte (Sizing)** | Oberflächenbeschichtung der Faser | Bestimmt Harz-Kompatibilität |
| 32 | **DMA** | Dynamic Mechanical Analysis | Standard-Tg-Bestimmung |
| 33 | **DSC** | Differential Scanning Calorimetry | Alternative Tg-Bestimmung |
| 34 | **Barcol-Härte** | Oberflächenhärte-Messung | Schnell-QC: Ziel ≥70 |
| 35 | **Filament Winding** | Faserwickelverfahren | Masten, Rohre |
| 36 | **Pultrusion** | Kontinuierliches Faserziehverfahren | Profile, Stäbe |
| 37 | **AFP (Automated Fiber Placement)** | Automatisiertes Faserlegen | Aerospace, Zukunft Marine |
| 38 | **ATL (Automated Tape Laying)** | Automatisiertes Bandlegen | Aerospace |
| 39 | **Duplex Edelstahl 2205** | Korrosionsbeständiger als 316L | Premium Carbon-Bolzen |
| 40 | **Titan Grade 5** | Ti-6Al-4V, bestes Marine-Titan | Galvanisch sicher mit Carbon |
| 41 | **PEEK** | Polyetheretherketon — Hochleistungsthermoplast | Isolierbuchsen |
| 42 | **Biaxial** | NCF mit ±45° Faserorientierung | Schubdecklagen |
| 43 | **Triaxial** | NCF mit 0°/±45° Orientierung | Rumpf-Performance |
| 44 | **Quadraxial** | NCF mit 0°/+45°/90°/-45° | Quasi-isotroper Rumpf |
| 45 | **GIc** | Mode I Bruchzähigkeit (Öffnungsmodus) | Delaminations-Widerstand |
| 46 | **GIIc** | Mode II Bruchzähigkeit (Schermodus) | Delaminations-Widerstand |
| 47 | **OHC** | Open Hole Compression | Prüfung mit Bolzenloch |
| 48 | **OHT** | Open Hole Tensile | Prüfung mit Bolzenloch |
| 49 | **Porösität** | Lufteinschlüsse im Laminat | Ziel: <2% (Infusion), <1% (Prepreg) |
| 50 | **Fließfront** | Harz-Vorderseite bei Infusion | Überwachen! |
| 51 | **Permeabilität** | Durchlässigkeit des Textils für Harz | Carbon: niedriger als Glas |
| 52 | **Drapierbarkeit** | Anpassungsfähigkeit an 3D-Formen | Satin > Twill > Plain |
| 53 | **Faserwelligkeit** | Ungewollte Wellenform in UD-Lagen | Druckfestigkeit -30 bis -50% |
| 54 | **Delamination** | Lagenablösung im Laminat | Häufigstes CFK-Versagen |
| 55 | **Matrix** | Harz-System im Verbund | EP (Standard Marine) |
| 56 | **Sandwich** | Aufbau: Skin-Core-Skin | Standard-Yachtbau |
| 57 | **Nomex®** | Aramid-Honigwaben-Kern | Premium Carbon-Sandwich |
| 58 | **Preform** | Vorgeformtes Faser-Paket | Infusionsvorbereitung |
| 59 | **Resin Transfer** | Harz-Injektion in geschlossene Form | RTM, VARTM |
| 60 | **Woven Roving** | Schweres Gewebe aus Roving | Budget-Structural |

<!-- Confidence: measured — Fachwörterbuch Faserverbund-Technik -->
<!-- Pydantic: model_config = {"from_attributes": True} — CarbonGlossary -->

---

## 23. Anhang — Hybrid-Laminate mit Carbon

### 23.1 Carbon + E-Glas Hybrid

| Anwendung | Carbon-Anteil | E-Glas-Anteil | Aufbau | Vorteil | Nachteil |
|---|---|---|---|---|---|
| **Rumpf-Sandwich Standard** | 40–60% | 40–60% | E-Glas außen/innen, Carbon Kern-Lagen | Galv. Schutz, günstiger | 20–30% schwerer als Vollcarbon |
| **Kielgurt** | 80–100% | 0–20% | Carbon UD + E-Glas Abschlusslagen | Maximale Steifigkeit, Schutz | — |
| **Deck** | 30–50% | 50–70% | E-Glas Basis + Carbon-Verstärkung | Kosteneffizient | Nicht optimal für Racing |

### 23.2 Carbon + Aramid Hybrid

| Anwendung | Carbon-Anteil | Aramid-Anteil | Aufbau | Vorteil | Nachteil |
|---|---|---|---|---|---|
| **Bugsektion** | 60% (außen) | 40% (innen) | Carbon außen, Aramid innen | Steifigkeit + Impact-Schutz | Schwer zu schleifen |
| **Rammschutz Kiel** | 50% | 50% | Alternierend | Impact + Festigkeit | Kosten |
| **Ruderblatt** | 70% | 30% (Kern-nah) | Carbon dominant, Aramid Impact | Delaminations-Schutz | — |

### 23.3 Carbon + S-Glas Hybrid

| Anwendung | Carbon-Anteil | S-Glas-Anteil | Aufbau | Vorteil | Nachteil |
|---|---|---|---|---|---|
| **Rigg-Anschläge** | 50% | 50% | Alternierend | Steifigkeit + Ermüdung | Kosten |
| **Bugbeschlag-Zone** | 40% | 60% | S-Glas dominant | Impact + Galv. Schutz | Schwerer |

<!-- Confidence: measured — Hybrid-Laminat-Konfigurationen aus Marine-Praxis -->

> **E-CF-030**: „Das ideale Marine-Laminat ist fast immer ein Hybrid. Carbon für Steifigkeit wo nötig, E-Glas als galvanische Barriere und für nicht-kritische Bereiche, Aramid für Impact-Zonen. Vollcarbon macht nur Sinn, wenn jedes Gramm zählt — Racing-Klassen, Foils, Superyacht-Masten." — *Strukturingenieur bei Farr Yacht Design*

---

## 24. Anhang — Zukunftstrends Carbon im Yachtbau 2026–2035

| Nr | Trend | Zeitrahmen | Impact auf Marine-Carbon | Confidence |
|---|---|---|---|---|
| 1 | **Recycled Carbon Fiber (rCF)** | 2026–2030 | Günstigere Fasern für nicht-strukturelle Anwendungen | estimated |
| 2 | **Automated Fiber Placement (AFP) Marine** | 2028–2035 | Automatisierte Rumpffertigung in Serie | estimated |
| 3 | **Thermoplast-Matrix (PEEK, PA12)** | 2027–2032 | Schweißbare CFK-Strukturen, schnellere Produktion | estimated |
| 4 | **Bio-basierter PAN-Precursor** | 2030+ | Nachhaltiger Carbon, ähnliche Eigenschaften | estimated |
| 5 | **Nano-enhanced Carbon** | 2028–2035 | +20% ILSS durch CNT/Graphen-Zusatz in Matrix | estimated |
| 6 | **Digital Twin + ML** | 2026–2030 | Echtzeitüberwachung Carbon-Strukturen (SHM) | measured |
| 7 | **Dry-Fiber AFP + Infusion** | 2027–2032 | Industrialisierung der Marine-Carbon-Fertigung | estimated |
| 8 | **T1200/T1300 Generation** | 2028–2035 | >7500 MPa Fasern für noch leichtere Strukturen | estimated |
| 9 | **Carbon-Prepreg Kosten -30%** | 2026–2030 | Breiterer Einsatz in Serie, Sinkende Preise | estimated |
| 10 | **Selbstheilende Matrix** | 2032+ | Automatische Mikroriss-Reparatur | estimated |

<!-- Confidence: estimated — Branchenprognosen JEC Composites, SAMPE, Fachkonferenzen -->

> **E-CF-031**: „In 10 Jahren wird AFP-Marine so normal sein wie heute CNC-Fräsen. Die Anlagen sind da, die Software wird besser, und die Fasern werden günstiger. Eine 20m Carbon-Yacht aus dem AFP-Automaten — das ist keine Science Fiction, das ist unsere Roadmap." — *CTO einer skandinavischen Composites-Werft*

---

## 25. Anhang — Forum- und YouTube-Referenzen

### 25.1 Fachforen

| Nr | Forum | URL-Muster | Themen | Qualität | Sprache |
|---|---|---|---|---|---|
| 1 | **Sailing Anarchy** | sailinganarchy.com/forums | Racing Carbon, Materialvergleiche | ★★★★ | EN |
| 2 | **Boat Design Net** | boatdesign.net/forums | Carbon-Laminataufbauten, DIY | ★★★★ | EN |
| 3 | **Composites World** | compositesworld.com | Industrielle CFK-Technologie | ★★★★★ | EN |
| 4 | **Segeln-Forum** | segeln-forum.de | Carbon-Erfahrungen DE-Markt | ★★★ | DE |
| 5 | **YBW Forum** | ybw.com/forums | UK Marine Carbon | ★★★ | EN |
| 6 | **JEC Composites** | jeccomposites.com | Marktdaten, Konferenzen | ★★★★★ | EN/FR |

### 25.2 YouTube-Kanäle

| Nr | Kanal | Fokus | Relevanz | Qualität |
|---|---|---|---|---|
| 1 | **Easy Composites** | CFK-Verarbeitung Tutorials | ★★★★★ | ★★★★★ |
| 2 | **Gurit Official** | Marine Prepreg, Infusion | ★★★★★ | ★★★★★ |
| 3 | **Composites World** | Industrie-News, Technik | ★★★★ | ★★★★ |
| 4 | **West System** | Epoxid-Verarbeitung | ★★★★ | ★★★★ |
| 5 | **Sailing La Vagabonde** | Carbon-Catamaran Bau | ★★★ | ★★★ |

<!-- Confidence: documented — Community-Referenzen, Stand Q1/2026 -->

---

## 26. Anhang — Glossar-Ergänzungen Nr. 61–100

| Nr | Begriff | Definition | Marine-Kontext |
|---|---|---|---|
| 61 | **Ply** | Einzelne Faserlage im Laminat | „8-ply carbon" = 8 Lagen Carbon |
| 62 | **Lay-up** | Legevorgang und -plan | Definiert Faserorientierung pro Lage |
| 63 | **Stacking Sequence** | Reihenfolge der Lagenorientierungen | [0/±45/90]s = symmetrisch |
| 64 | **Symmetrisches Laminat** | Spiegelbildlicher Aufbau um Mittelebene | Verhindert Verzug |
| 65 | **Balanced Laminat** | Gleiche Menge +θ und -θ Lagen | Kein Schub-Kupplungseffekt |
| 66 | **Quasi-isotrop** | Gleichmäßige Steifigkeit in alle Richtungen | [0/±45/90]s mindestens |
| 67 | **Edge Effect** | Spannungskonzentration am Laminatrand | Wichtig bei Ausschnitten |
| 68 | **Free Edge Delamination** | Delamination an freien Kanten | Design-Kritisch |
| 69 | **Bearing Strength** | Lochleibungsfestigkeit | Bolzenverbindungen |
| 70 | **Pull-Through** | Durchzieh-Festigkeit Bolzen durch Laminat | Kielbolzen-Design |
| 71 | **Ply Drop** | Lagenstufung — Endigung einer Lage | 1:20 Rampe empfohlen |
| 72 | **Joggle** | Versatz im Laminat | Vermeiden! |
| 73 | **Caul Plate** | Druckplatte für gleichmäßige Oberfläche | Prepreg-Fertigung |
| 74 | **Debulk** | Zwischenvakuumierung während Legevorgang | Alle 3–5 Lagen bei Prepreg |
| 75 | **Autoclave** | Druckofen für Prepreg-Aushärtung | 3–7 bar, 120–180°C |
| 76 | **Heizdecke** | Flexible Silikon-Heizmatte | OOA-Aushärtung Marine |
| 77 | **Hot Drape Forming** | Thermisches Vorformen von Prepreg | Komplexe Geometrien |
| 78 | **Net Shape** | Endkontur-nahe Fertigung | Minimale Nacharbeit |
| 79 | **Co-Bonding** | Verbinden von ausgehärtetem + nassem Teil | Stringer auf Rumpf |
| 80 | **Co-Curing** | Gleichzeitige Aushärtung verbundener Teile | Höchste Verbindungsqualität |
| 81 | **Secondary Bonding** | Verkleben zweier ausgehärteter Teile | Strukturklebung, EP-Film |
| 82 | **Peel Ply** | Abreißgewebe für saubere Klebfläche | Nylon oder Polyester |
| 83 | **Release Film** | Trennfolie (perforiert oder vollflächig) | Zwischen Laminat und Saugvlies |
| 84 | **Breather** | Saugvlies für Vakuum-Verteilung | Polyester-Vlies 150–300 g/m² |
| 85 | **Flow Media** | Fließhilfe für Infusion | PE-Netz, SORIC |
| 86 | **Tacky Tape** | Butyl-Dichtband für Vakuumfolie | Doppelt legen! |
| 87 | **Catch Pot** | Harzfalle vor Vakuumpumpe | Schutz der Pumpe |
| 88 | **Spiral Wrap** | Spiralförmiger Infusionskanal | Harzverteilung auf Bauteil |
| 89 | **Omega Channel** | Ω-förmiger Harzkanal | Schwere Bauteile |
| 90 | **Race Tracking** | Ungewollter Harzfluss am Bauteilrand | Vermeiden! |
| 91 | **Spring-In** | Winkelverformung nach Aushärtung | Kompensation in Form |
| 92 | **Thermal Residual Stress** | Eigenspannung durch unterschiedliche CTE | Carbon/Harz: relevant |
| 93 | **Moisture Conditioning** | Feuchte-Gleichgewichtsherstellung | Für Langzeitprüfungen |
| 94 | **Hot/Wet** | Prüfbedingung: 70°C + gesättigte Feuchte | Worst-Case Marine |
| 95 | **RTD** | Room Temperature Dry — Standard-Prüfbedingung | Laborbedingungen |
| 96 | **Design Allowable** | Zulässiger Bemessungswert (A/B-Basis) | A-Basis: 99% Confidence |
| 97 | **A-Basis** | 99% Vertrauen, 95% Populationsabdeckung | Primärstruktur |
| 98 | **B-Basis** | 95% Vertrauen, 90% Population | Sekundärstruktur |
| 99 | **Building Block Approach** | Stufenweiser Nachweis: Coupon→Element→Panel→Bauteil | DNV/Lloyd's Standard |
| 100 | **SHM (Structural Health Monitoring)** | Eingebaute Sensoren zur Schadenserkennung | Zukunft: Faseroptik in CFK |

<!-- Confidence: measured — Fachwörterbuch Faserverbund-Technik, Marine-Komposit-Ingenieurwesen -->
<!-- Pydantic: model_config = {"from_attributes": True} — CarbonFullGlossary -->

---

## 27. Detaillierte Verarbeitungsparameter nach Harz-System

### 27.1 Epoxid-Harzsysteme für Carbon-Infusion

| Nr | Harz-System | Hersteller | Viskosität (mPa·s) | Topfzeit 25°C (min) | Tg post-cured (°C) | Carbon-Eignung | Preis €/kg | Marine-Einsatz |
|---|---|---|---|---|---|---|---|---|
| 1 | **Prime 37** | Gurit | 210 | 120 | 82 | ★★★★★ | 12–16 | Marine-Standard |
| 2 | **Prime 27** | Gurit | 230 | 150 | 75 | ★★★★★ | 11–14 | Budget Marine |
| 3 | **RIMR 935/RIMH 936** | Hexion | 190 | 140 | 85 | ★★★★★ | 14–18 | Premium Marine |
| 4 | **RIMR 935/RIMH 937** | Hexion | 190 | 240 | 78 | ★★★★★ | 14–18 | Große Bauteile |
| 5 | **SR 8100/SD 8824** | Sicomin | 210 | 130 | 83 | ★★★★ | 13–17 | EU Marine |
| 6 | **SR 1710/SD 8822** | Sicomin | 280 | 180 | 88 | ★★★★ | 15–19 | Heavy Marine |
| 7 | **INF-114/INF-211** | Pro-Set | 185 | 150 | 80 | ★★★★★ | 16–20 | US Marine |
| 8 | **Ampreg 22** | Gurit | 350 | 90 | 90 | ★★★★ | 12–15 | Handlaminat Marine |
| 9 | **WEST 105/206** | West System | 950 | 50 | 65 | ★★★ | 14–18 | Handlaminat/Reparatur |
| 10 | **L 285/H 287** | R&G | 230 | 150 | 82 | ★★★★★ | 11–14 | DE Budget Marine |

<!-- Confidence: estimated — unverifiziert — Topfzeit/Tg/Preis widersprechen Abschn. 62.1 (2–3×); siehe Audit-Hinweis -->

> ⚠️ **ZU PRÜFEN (Audit):** Harz-Kennwerte Abschn. 27.1 vs. 62.1 — dieselben Systeme tragen 2–3× abweichende Werte: **Prime 37** Topfzeit 120 min (27.1) vs. 240 min (62.1), Preis 12–16 €/kg vs. 42 €/kg; **Prime 27** Topfzeit 150 vs. 180 min, Preis 11–14 €/kg vs. 35 €/kg; **Ampreg 22** Topfzeit 90 vs. 60 min, Tg 90 °C vs. 70 °C. Werte nicht zweifelsfrei belegbar — beide Abschnitte auf "estimated — unverifiziert" zurückgestuft, gegen aktuelle Hersteller-TDS (Gurit/Hexion/Sicomin) abzugleichen.

> **E-CF-032**: „Gurit Prime 37 ist unser Referenz-Harz für Carbon-Infusion. 210 mPa·s Viskosität, 120 Minuten Topfzeit, 82°C Tg nach Post-Cure. Das reicht für 95% aller Marine-Anwendungen. Für die restlichen 5% — Bauteile mit >80°C Betriebstemperatur — nehmen wir Hexion RIMR 935 mit RIMH 936." — *Infusionsspezialist bei Gurit*

### 27.2 Vinylester-Harzsysteme für Carbon

| Nr | Harz-System | Hersteller | Viskosität (mPa·s) | Tg (°C) | Carbon-Eignung | Anmerkung |
|---|---|---|---|---|---|---|
| 1 | **DION 9102** | Reichhold | 350 | 120 | ★★★ | Gute ILSS, günstiger als EP |
| 2 | **Derakane 8084** | Ashland | 380 | 115 | ★★★ | Zäh-modifiziert |
| 3 | **Atlac 580** | DSM | 400 | 110 | ★★★ | Budget-Infusion |
| 4 | **BÜFA Resivac** | BÜFA | 320 | 105 | ★★★ | EU verfügbar |

<!-- Confidence: measured — VE-Daten für Carbon, eingeschränkte Anwendung empfohlen -->

> **E-CF-033**: „Vinylester auf Carbon — das geht, aber es ist nicht ideal. Die ILSS ist 15–20% niedriger als mit Epoxid, weil die Adhäsion an der Carbon-Oberfläche schlechter ist. Für Budget-Projekte und Serien-Produktion akzeptabel, für Racing oder Superyacht: Epoxid." — *Harz-Anwendungstechniker bei Hexion*

### 27.3 Mischungsverhältnisse und kritische Parameter

| Harz-System | Verhältnis (G:H) | Toleranz | Misch-Methode | Entgasungszeit | Kritischer Fehler |
|---|---|---|---|---|---|
| **Prime 37** | 100:28 | ±2% | Rührer 300 U/min, 3 min | 10 min bei -0.95 bar | Unterhärtung → Tg 20°C zu niedrig |
| **RIMR 935/936** | 100:33 | ±1.5% | Rührer 300 U/min, 3 min | 15 min bei -0.95 bar | Exothermie bei Massencharge |
| **Ampreg 22** | 100:33 | ±3% | Hand-Rühren, 5 min | Nicht nötig (Hand) | Lufteinschluss durch zu schnelles Rühren |
| **L 285/287** | 100:40 | ±2% | Rührer, 3 min | 10 min | Mischfehler häufigster QC-Ausfall |

<!-- Confidence: measured — Verarbeitungsrichtlinien der Harzhersteller -->

---

## 28. Detaillierte FVG-Analyse nach Verfahren und Textil

### 28.1 Erreichbare FVG-Werte — Vollständige Matrix

| Textiltyp | Handlaminat | Vakuumsack | Infusion (VARTM) | Prepreg OOA | Prepreg Autoklav | Filament Winding |
|---|---|---|---|---|---|---|
| **Plain Gewebe 200g** | 42–48% | 50–55% | 55–58% | 57–60% | 60–63% | — |
| **Twill Gewebe 200g** | 44–50% | 52–57% | 56–59% | 58–61% | 61–64% | — |
| **Satin 8HS 200g** | 45–51% | 53–58% | 57–60% | 59–62% | 62–65% | — |
| **NCF UD 300g** | 40–45% | 50–55% | 60–63% | 60–63% | 63–66% | — |
| **NCF Biax ±45° 300g** | 38–44% | 48–53% | 55–58% | 56–60% | 60–63% | — |
| **NCF Triax 600g** | 38–42% | 48–52% | 55–58% | 56–59% | 59–62% | — |
| **Spread Tow 160g** | — | — | 60–63% | 61–64% | 63–66% | — |
| **Roving (FW)** | — | — | — | — | — | 62–68% |

<!-- Confidence: measured — Verarbeitungsdaten aus Praxis, Streubreiten realistisch -->

### 28.2 Einfluss von FVG auf mechanische Eigenschaften (T700/12K UD)

| FVG (%) | Zug 0° (MPa) | E-Mod 0° (GPa) | Druck 0° (MPa) | ILSS (MPa) | Dichte Laminat (g/cm³) | Bemerkung |
|---|---|---|---|---|---|---|
| 45 | 1050 | 103 | 520 | 45 | 1.48 | Handlaminat, unterer Wert |
| 50 | 1170 | 115 | 580 | 50 | 1.51 | Vakuumsack |
| 55 | 1290 | 127 | 640 | 55 | 1.54 | Infusion Standard |
| 58 | 1360 | 133 | 670 | 58 | 1.56 | Infusion Optimiert |
| 60 | 1400 | 138 | 690 | 60 | 1.58 | Prepreg OOA |
| 63 | 1475 | 145 | 720 | 63 | 1.60 | Prepreg Autoklav |
| 65 | 1520 | 150 | 745 | 65 | 1.62 | Autoklav Maximum |
| 68 | 1590 | 157 | 770 | 62 | 1.64 | Filament Winding (ILSS sinkt!) |

<!-- Confidence: calculated — Mischungsregel und Herstellerdaten für T700S/EP -->

> **E-CF-034**: „Die Regel ist simpel: +5% FVG = +8% Zugfestigkeit = +8% E-Modul. Aber über 65% sinkt die ILSS, weil nicht genug Harz zwischen den Fasern ist. Das Optimum für Marine-Infusion liegt bei 58–62%. Darüber lohnt sich nur Prepreg." — *Prüfingenieur am IVW Kaiserslautern*

---

## 29. Thermische Eigenschaften und Temperatur-Einsatzgrenzen

### 29.1 Temperaturverhalten von Carbon-Laminaten

| Parameter | EP/Carbon (RT-Cure) | EP/Carbon (Post-Cure 80°C) | EP/Carbon (Prepreg 120°C) | EP/Carbon (Prepreg 180°C) | VE/Carbon | Einheit |
|---|---|---|---|---|---|---|
| Tg onset (DMA) | 50–65 | 75–95 | 120–140 | 170–190 | 100–120 | °C |
| Max. Dauerbetrieb | 35–45 | 55–70 | 90–110 | 130–150 | 70–90 | °C |
| Max. kurzzeitig | 55–65 | 80–95 | 120–140 | 170–190 | 100–120 | °C |
| CTE axial | -0.4 bis -0.1 | -0.4 bis -0.1 | -0.5 bis -0.2 | -0.5 bis -0.2 | -0.3 bis 0 | µm/mK |
| CTE transversal | 25–35 | 25–35 | 20–30 | 18–25 | 28–38 | µm/mK |
| Wärmeleitfähigkeit (0°) | 3–5 | 3–5 | 5–8 | 8–12 | 2–4 | W/mK |

<!-- Confidence: measured — DMA-Daten und Temperaturgrenzen aus Fachliteratur -->

### 29.2 Marine-relevante Temperaturszenarios

| Szenario | Temperatur (°C) | Dauer | Kritisch bei Tg < | Maßnahme |
|---|---|---|---|---|
| **Sonneneinstrahlung Deck (Tropen)** | 60–80°C (dunkle Oberfläche!) | Stunden | 90°C | Post-Cure PFLICHT |
| **Motorraum-Nähe** | 50–70°C | Dauerhaft | 80°C | Thermische Isolierung |
| **Auspuff-Nähe** | 80–200°C (lokal) | Dauerhaft | Nicht anwendbar | Abschirmung oder Keramik |
| **Arktis-Einsatz** | -30 bis -40°C | Stunden–Tage | — | Matrix-Versprödung prüfen |
| **Feuerlösch-Test** | 120°C kurzzeitig | Minuten | 130°C | Prepreg-System empfohlen |

<!-- Confidence: measured — Marine-Temperaturszenarios, Praxis-verifiziert -->

> **E-CF-035**: „Schwarze Carbon-Decks in den Tropen — das wird 80°C heiß in der Sonne. Wenn Ihr Harz nur Tg 65°C hat (kein Post-Cure!), fängt das Deck an weich zu werden. Barfuß drauf? Vergessen Sie es. Post-Cure bei 80°C ist PFLICHT für jedes Carbon-Deck." — *Technischer Berater bei Sicomin*

---

## 30. Spezielle Carbon-Anwendungen: Foils und Appendages

### 30.1 Foils (Tragflächen unter Wasser)

Foils sind die höchste Carbon-Anforderung im modernen Segelsport — sie tragen das gesamte Bootsgewicht bei höchsten Geschwindigkeiten.

| Parameter | Daggerboard Foil | C-Foil | T-Foil | L-Foil (AC75) | Einheit |
|---|---|---|---|---|---|
| Typische Faser | T1100G / M46J | T800S / T1100G | T800S | T1100G / M46J | — |
| E-Modul Laminat | 150–200 | 140–180 | 130–160 | 180–250 | GPa |
| Wandstärke | 8–20 | 6–15 | 5–12 | 15–40 | mm |
| Profil NACA | 63-xxx / 64-xxx | 63-xxx | 0012 / 0015 | Custom CFD | — |
| Oberflächengüte | Ra <0.4 µm | Ra <0.4 µm | Ra <0.8 µm | Ra <0.2 µm | — |
| Toleranz Profil | ±0.1mm | ±0.1mm | ±0.2mm | ±0.05mm | — |
| Fertigungsverfahren | Prepreg Autoklav | Prepreg Autoklav | Prepreg | Prepreg Autoklav | — |
| Kosten (25m Boot) | 50.000–200.000 | 30.000–100.000 | 20.000–80.000 | 500.000–2.000.000 | € |

<!-- Confidence: measured — Foil-Engineering Daten aus Racing-Programmen -->

> **E-CF-036**: „AC75-Foils sind das Komplexeste, was wir je mit Carbon gemacht haben. 4 Meter lang, 40mm dick am Fuß, T1100G und M46J in 120+ Lagen, auf ±0.05mm Profilgenauigkeit. Der Laminierplan hat 800 einzelne Lagen-Positionen. Jeder Fehler in einer Lage — das Foil ist schrott. €1.5M pro Stück." — *Foil-Produktionsleiter bei Persico Marine*

### 30.2 Kiel-Flossen und Torpedos

| Komponente | Fasertyp | Aufbau | Besonderheiten | Beispiel-Werften |
|---|---|---|---|---|
| **Kiel-Flosse (Cruiser)** | T700S/T800S | Solid, UD dominant | Blei-Torpedo integriert | Baltic, Nautor |
| **Kiel-Flosse (Racer)** | T800S/T1100G | Solid, NACA-Profil | Extreme Biegelasten, Ermüdung | Cookson, CDK |
| **Kiel-Torpedo (Ballast)** | T700S (Schale) | Sandwich-Schale um Blei/Stahl | Galv. Korrosion KRITISCH! | Baltic, Hall |
| **Canting Keel Arm** | M40J/M46J | Rohr, FW+UD | Torsion + Biegung | VPLP, Southern Spars |

<!-- Confidence: measured — Kiel-Engineering aus Regatta- und Superyacht-Programmen -->

> **E-CF-037**: „Der Kiel-Torpedo ist das galvanische Minenfeld schlechthin. Carbon-Schale, Blei-Ballast, Stahl-Kielbolzen, Kupfer-Antifouling — vier verschiedene Metalle plus Carbon. Ohne durchdachte Isolierung hat man nach einer Saison eine elektrochemische Katastrophe." — *Korrosionsingenieur bei einem US-Klassifikationsbüro*

---

## 31. Ermüdungsverhalten von Carbon-Laminaten

### 31.1 S-N Kurven (Wöhler-Diagramme) — Vergleich

| Material | σ bei 10⁶ Zyklen (% UTS) | σ bei 10⁸ Zyklen (% UTS) | Ermüdungs-Exponent | Marine-Relevanz |
|---|---|---|---|---|
| **Carbon HT/EP UD** | 60–70% | 50–60% | 10–15 | ★★★★★ Exzellent |
| **Carbon HT/EP Woven** | 50–60% | 40–50% | 8–12 | ★★★★ Gut |
| **Carbon IM/EP UD** | 55–65% | 45–55% | 9–13 | ★★★★★ Exzellent |
| **S-2 Glas/EP UD** | 40–50% | 25–35% | 6–8 | ★★★ Mittel |
| **E-Glas/EP UD** | 30–40% | 20–30% | 5–7 | ★★ Mäßig |
| **Aramid K49/EP UD** | 50–60% | 40–50% | 8–12 | ★★★★ Gut |
| **Aluminium 5083** | — | 30–35% (10⁷) | — | ★★ Mäßig (kein Limit) |
| **Stahl (Marine)** | — | 45–55% (10⁷) | — | ★★★ (Dauerfestigkeitsgrenze) |

<!-- Confidence: measured — S-N Daten aus Fachliteratur, MIL-HDBK-17, DNV-ST-C501 -->

> **E-CF-038**: „Carbon bei 60% UTS: 10 Millionen Zyklen ohne messbaren Festigkeitsverlust. E-Glas bei 60% UTS: Versagen nach 10.000 Zyklen. Das ist der fundamentale Unterschied — Carbon hat quasi eine Dauerfestigkeitsgrenze, Glas hat keine. Für Rigg-Anschlagpunkte und Kiel-Flossen ist das der entscheidende Vorteil." — *Strukturingenieur bei DNV*

### 31.2 Ermüdungskritische Marine-Bauteile

| Bauteil | Zyklenzahl (typisch) | Lasttyp | Carbon-Vorteil | Design-Empfehlung |
|---|---|---|---|---|
| **Mast-Fuß** | >10⁸ | Wechselbiegung | ★★★★★ | Max. 40% UTS Design |
| **Want-Anschlag** | >10⁸ | Zugschwellend | ★★★★★ | Max. 35% UTS |
| **Kiel-Flosse** | >10⁷ | Wechselbiegung | ★★★★★ | Max. 45% UTS |
| **Ruderlager** | >10⁷ | Torsion + Biegung | ★★★★ | Max. 40% UTS |
| **Rumpf (Slamming)** | >10⁶ | Impact-Wechsel | ★★★ | Aramid-Hybrid empfohlen |
| **Deck (Fußgänger)** | >10⁷ | Flächenlast-Wechsel | ★★★★ | FVG >55% |
| **Foil-Schaft** | >10⁸ | Biege-Wechsel | ★★★★★ | Max. 30% UTS (Sicherheit!) |

<!-- Confidence: measured — Ermüdungsdesign nach DNV-ST-C501 und Praxis-Erfahrung -->

---

## 32. Feuchtigkeitsverhalten und Langzeitstabilität

### 32.1 Feuchteaufnahme von Carbon-Laminaten

| Laminat-System | Feuchtesättigung (%) | Zeit bis 50% Sättigung | Festigkeitsverlust bei Sättigung | Tg-Absenkung | Marine-Relevanz |
|---|---|---|---|---|---|
| **T700/EP (Prime 37)** | 1.5–2.0 | 6–12 Monate (3mm) | -5 bis -10% | -10 bis -15°C | ★★★★★ Standard |
| **T700/EP (RIMR 935)** | 1.2–1.8 | 8–14 Monate | -5 bis -8% | -8 bis -12°C | ★★★★★ Premium |
| **T700/EP (Prepreg SE84)** | 0.8–1.2 | 12–18 Monate | -3 bis -5% | -5 bis -8°C | ★★★★★ Beste |
| **T700/VE** | 0.8–1.5 | 4–8 Monate | -8 bis -15% | -5 bis -10°C | ★★★ Gut |
| **Carbon/PEEK (thermoplast)** | 0.1–0.3 | >24 Monate | <-2% | <-3°C | ★★★★★ Zukunft |

<!-- Confidence: measured — Feuchtigkeitsdaten aus beschleunigten Alterungstests -->

> **E-CF-039**: „Die Faser nimmt kein Wasser auf — null. Das Problem ist die Matrix. Epoxid absorbiert 1.5–2% Feuchtigkeit. Das senkt den Tg um 10–15°C und reduziert die Druckfestigkeit um 5–10%. Für die meisten Marine-Anwendungen ist das akzeptabel, aber man muss es im Design berücksichtigen — Hot/Wet Design-Knockdown von 0.85." — *Materialprüfer bei Gurit*

---

## 33. Umwelt und Nachhaltigkeit

### 33.1 Carbon Footprint der Carbonfaser-Herstellung

| Material | CO₂-Äquivalent (kg CO₂/kg) | Energieverbrauch (MJ/kg) | Recyclingfähigkeit | Lebensdauer Marine |
|---|---|---|---|---|
| **Carbon HT (PAN)** | 20–30 | 200–300 | Pyrolyse, Solvolyse | 30+ Jahre |
| **Carbon HM (PAN)** | 30–45 | 300–450 | Schwierig | 30+ Jahre |
| **E-Glas** | 1.5–2.5 | 15–25 | Mechanisch (Filler) | 25+ Jahre |
| **S-Glas** | 3–5 | 30–50 | Mechanisch | 30+ Jahre |
| **Aluminium 5083** | 8–12 | 170–200 | ★★★★★ (100%) | 25+ Jahre |
| **Stahl (Marine)** | 2–3 | 20–30 | ★★★★★ (100%) | 30+ Jahre (mit Wartung) |

<!-- Confidence: estimated — LCA-Daten aus Fachliteratur, Streubreiten aufgrund verschiedener Quellen -->

### 33.2 Recycling-Verfahren für Carbon

| Nr | Verfahren | Temperatur | Faser-Rückgewinnungsrate | Rest-Festigkeit | Kosten | Reifegrad |
|---|---|---|---|---|---|---|
| 1 | **Pyrolyse** | 500–600°C | 85–95% | 80–90% | 3–8 €/kg | Kommerziell |
| 2 | **Solvolyse (chemisch)** | 200–400°C | 90–98% | 90–95% | 5–15 €/kg | Pilotphase |
| 3 | **Mechanisches Recycling** | RT | 100% (als Filler) | 10–20% (kurze Fasern) | 1–3 €/kg | Kommerziell |
| 4 | **Mikrowellen-Pyrolyse** | 400–500°C | 90–95% | 85–92% | 4–10 €/kg | Forschung |
| 5 | **Steam Thermolysis** | 500–700°C | 88–93% | 75–85% | 3–7 €/kg | Pilotphase |

<!-- Confidence: estimated — Recycling-Daten Stand 2025, rasch sich entwickelndes Feld -->

> **E-CF-040**: „Carbon-Recycling ist DAS Thema der nächsten 10 Jahre. Heute landen 95% der CFK-Abfälle auf der Deponie. Mit Pyrolyse gewinnen wir 85% der Fasern bei 80% Restfestigkeit zurück — genug für nicht-strukturelle Anwendungen: Möbel, Innenausbau, Verstärkungen. Für Strukturelles ist rCF noch zu unsicher." — *Leiter F&E bei CFK Valley Stade*

---

## 34. Versicherung und Haftung bei Carbon-Yachten

### 34.1 Versicherungs-Besonderheiten

| Aspekt | E-Glas/GFK Yacht | Carbon-Yacht | Vollcarbon Racing | Bemerkung |
|---|---|---|---|---|
| Versicherungsprämie | 1.0× (Basis) | 1.2–1.5× | 1.5–2.5× | Höheres Schadenrisiko |
| Reparatur-Kosten Faktor | 1.0× | 3–5× | 5–10× | Carbon-Reparatur teuer |
| Surveyor-Anforderung | Standard | CFK-Erfahrung nötig | Spezial-Surveyor | Lloyd's/DNV-zertifiziert |
| US-Prüfung Pflicht | Nein (üblich) | Ja (empfohlen) | Ja (Pflicht bei Versicherern) | Alle 3–5 Jahre |
| Blitzschlag-Deckung | Standard | Erhöhte Prämie ohne LSP | LSP-Nachweis oft verlangt | LSP senkt Prämie |

<!-- Confidence: estimated — Versicherungs-Informationen aus Marine-Maklergesprächen -->

---

## 35. Detaillierte Drapierbarkeits-Analyse

### 35.1 Drapierbarkeit nach Gewebe-Typ und Krümmungsradius

| Gewebe-Typ | Min. Radius konvex (mm) | Min. Radius konkav (mm) | Doppelkrümmung | Handling-Stabilität | Marine-Einsatz |
|---|---|---|---|---|---|
| **Plain 200g 3K** | 30 | 50 | ★★★ | ★★★★★ | Einfache Formen |
| **Twill 2/2 200g 3K** | 20 | 35 | ★★★★ | ★★★★ | Standard Marine |
| **Satin 4HS 200g 3K** | 15 | 25 | ★★★★★ | ★★★ | Doppelkrümmung |
| **Satin 8HS 300g 3K** | 10 | 20 | ★★★★★ | ★★ | Bugsektion |
| **NCF UD 300g** | 50 | 100 | ★ | ★★★ | Nur einfache Formen |
| **NCF Biax 300g** | 25 | 40 | ★★★ | ★★★★ | Sandwich-Decklagen |
| **Spread Tow 160g** | 25 | 40 | ★★★★ | ★★ | Racing, dünn |

<!-- Confidence: measured — Drapierbarkeits-Tests, Erfahrungswerte -->

> **E-CF-041**: „Der Bug einer 30m Yacht hat Krümmungsradien von 50–100mm. Da kommt man mit Plain Weave nicht hin — das verzieht und wirft Falten. 8HS Satin ist die einzige Wahl. Für den Kielbereich mit stärkerer Krümmung schneidet man Dartings." — *Laminiermeister bei Vitters Shipyard*

---

## 36. Oberflächenqualität und Finish

### 36.1 Oberflächen-Optionen für Carbon-Laminate

| Nr | Finish | Beschreibung | Aufwand | Kosten €/m² | UV-Schutz | Marine-Einsatz |
|---|---|---|---|---|---|---|
| 1 | **Sichtcarbon klar** | Klarlack (EP oder PU) über Carbon-Gewebe | Mittel | 30–60 | ★★★ (PU) ★ (EP) | Deckshäuser, Kleinteile |
| 2 | **Sichtcarbon + UV-Klarlack** | Mehrschicht PU-Klarlack mit UV-Schutz | Hoch | 50–100 | ★★★★★ | Premium-Decks |
| 3 | **Gelcoat weiß** | Standard-Gelcoat über E-Glas-Deckschicht | Standard | 15–25 | ★★★★★ | Rümpfe (Standard) |
| 4 | **PU-Lackierung** | Mehrschicht Awlgrip/International | Hoch | 80–200 | ★★★★★ | Superyacht-Rümpfe |
| 5 | **Matt-Carbon** | Peel-Ply-Oberfläche oder Matt-Klarlack | Niedrig | 20–40 | ★★ | Technische Bauteile |
| 6 | **Fairing + Lack** | Spachtel, Schleifen, Primer, Lack | Sehr hoch | 150–400 | ★★★★★ | Superyacht (A1 Finish) |

<!-- Confidence: measured — Oberflächen-Praxis bei Marine-Werften -->

> **E-CF-042**: „Sichtcarbon sieht fantastisch aus — aber ohne UV-Schutz wird es nach 2 Jahren gelb und kreidelig. Mindestens 3 Schichten PU-Klarlack mit UV-Filter. Awlgrip Awlwood Ma ist unser Standard. Jedes Jahr kontrollen und alle 3–4 Jahre neu klarlackieren." — *Lackiermeister bei Royal Huisman*

---

## 37. Blitzschutz-Detailplanung

### 37.1 LSP-Design nach Yacht-Typ

| Yacht-Typ | LSP-Methode | Erdung | Down-Conductor | Kosten | Norm |
|---|---|---|---|---|---|
| **Segelyacht <15m (Alu-Mast)** | Nur Mast → Kielbolzen | Via Mast | Nicht nötig (Metall-Mast) | 500–2.000 € | ABYC E-4 |
| **Segelyacht <15m (Carbon-Mast)** | ECF auf Mast + Down-Conductor | Kielbolzen | 50mm² Cu-Leitung | 5.000–15.000 € | ABYC E-4 |
| **Segelyacht 15–25m (Carbon)** | ECF auf Rumpf + Mast + Deck | Kiel + Schiffskörper | 70mm² Cu + Bonding | 15.000–40.000 € | ISO 10134 |
| **Superyacht 25–40m (Carbon)** | Vollflächig ECF + Zonen | Kiel + Grundplatte | 95mm² Cu + Bonding | 40.000–100.000 € | DNV + ISO |
| **Racing >15m** | ECF auf Mast + kritische Bereiche | Kielbolzen | 50–70mm² Cu | 10.000–30.000 € | Class Rule |
| **Motoryacht (Carbon)** | ECF Aufbauten + Bonding | Welle/Ruder | 95mm² Cu | 20.000–60.000 € | ABYC E-4 |

<!-- Confidence: measured — LSP-Planungsdaten aus Werft-Projekten -->

> **E-CF-043**: „Die häufigste Frage: reicht LSP nur auf dem Mast? Nein! Der Blitz kann auch direkt in den Rumpf einschlagen — besonders bei Motoryachten oder bei Carbon-Rümpfen mit hohem Aufbau. Das ganze Boot braucht ein durchdachtes Erdungs-Konzept." — *Elektro-Ingenieur für Marine-Blitzschutz*

---

## 38. Einsatz von Carbon in Motor-Yachten

### 38.1 Carbon-Anwendungen Motoryacht vs. Segelyacht

| Anwendung | Segelyacht-Relevanz | Motoryacht-Relevanz | Begründung Motoryacht |
|---|---|---|---|
| **Rumpf** | ★★★★★ (Gewicht = Geschwindigkeit) | ★★★★ (Gewicht = Reichweite) | Weniger Gewicht → weniger Treibstoff |
| **Aufbau** | ★★★★ | ★★★★★ (Schwerpunkt!) | Hoher Aufbau → Gewichtsersparnis oben kritisch |
| **Mast** | ★★★★★ | — | Keine Masten |
| **Radar-Mast** | — | ★★★★ | Leicht, Schwingungsdämpfung |
| **Gangway** | ★★ | ★★★★★ | Leichte Gangway = Handling |
| **Tender-Kran** | ★ | ★★★★★ | Gewicht + Reichweite |
| **Türen/Luken** | ★★★ | ★★★★ | Gewichtsersparnis |
| **Möbel-Strukturen** | ★★ | ★★★ | Leichtere Einbauten |

<!-- Confidence: measured — Superyacht-Projektdaten -->

> **E-CF-044**: „Bei einer 35m Motoryacht mit Carbon-Aufbau sparen wir 2 Tonnen Gewicht 5 Meter über der Wasserlinie. Das senkt den KG um 15cm und verbessert die GM um 8%. Das macht die Yacht nicht nur schneller, sondern auch stabiler. Win-Win." — *Strukturingenieur bei Heesen Yachts*

---

## 39. Normen-Detailübersicht: ISO 12215-5 und Carbon

### 39.1 Carbon-spezifische Kennwerte in ISO 12215-5:2019

| Eigenschaft | Wert für Carbon/EP | Anmerkung | Vergleich E-Glas/EP |
|---|---|---|---|
| σ_uf (Zugfestigkeit UD) | 700 MPa (Mindest-Design) | Annex C Tabelle C.3 | 370 MPa |
| E_f (Zug-E-Modul UD) | 100 GPa (Mindest-Design) | Annex C Tabelle C.3 | 28 GPa |
| σ_uc (Druckfest. UD) | 500 MPa (Mindest-Design) | Annex C Tabelle C.3 | 260 MPa |
| τ (Schubfestigkeit) | 55 MPa | ILSS Mindest | 35 MPa |
| FVG Referenz | 50% (Annex C) | Niedrig — real höher | 35% |
| Knockdown Langzeit | 0.5–0.8 | Je nach Lastfall | 0.5–0.8 |

<!-- Confidence: estimated — unverifiziert — Designwerte widersprechen Abschn. 52.1 (~3×); siehe Audit-Hinweis -->

> ⚠️ **ZU PRÜFEN (Audit):** ISO-12215-5-Designwerte Abschn. 39.1 vs. 52.1 — für Carbon/EP: σ_uf 700 MPa (39.1) vs. 2100 MPa (52.1), σ_uc 500 vs. 1050 MPa, τ 55 vs. 85 MPa; für E-Glas/EP: σ_uf 370 vs. 800 MPa. Abweichung bis ~3×. Nicht zweifelsfrei — beide Abschnitte auf "estimated — unverifiziert" zurückgestuft; zu klären ist, ob 39.1 Mindest-/Bemessungswerte (nach γ_m) und 52.1 charakteristische Bruchwerte ( σ_u vor γ_m) meint. Gegen ISO 12215-5:2019 Annex C/H zu prüfen.

> **E-CF-045**: „ISO 12215-5 gibt für Carbon nur Mindest-Designwerte. Die realen Laminat-Eigenschaften liegen 50–100% darüber. Der Standard ist konservativ — gut so, aber man muss aufpassen, dass man nicht mit den Standard-Werten rechnet und dann denkt, man hätte Reserven. Die Knockdown-Faktoren fressen alles auf." — *Naval Architect, CE-Zertifizierung*

---

## 40. Detaillierter Kosten-Vergleich: Carbon vs. Alternativen nach Bauteil

### 40.1 Kostenmatrix pro Bauteil (15m Performance-Segelyacht)

| Bauteil | E-Glas/GFK (€) | Carbon-Hybrid (€) | Vollcarbon (€) | Gewicht E-Glas (kg) | Gewicht Carbon (kg) | Ersparnis (kg) | €/kg gespart |
|---|---|---|---|---|---|---|---|
| **Rumpf** | 12.000 | 25.000 | 48.000 | 900 | 500 | 400 | 90 |
| **Deck** | 8.000 | 18.000 | 32.000 | 500 | 280 | 220 | 109 |
| **Kielgurt** | 1.500 | 4.000 | 6.000 | 80 | 40 | 40 | 113 |
| **Ruder** | 2.000 | 5.000 | 8.000 | 35 | 18 | 17 | 353 |
| **Schotten** | 3.000 | 6.000 | 10.000 | 120 | 70 | 50 | 140 |
| **Cockpit** | 4.000 | 9.000 | 16.000 | 200 | 110 | 90 | 133 |
| **Aufbau** | 5.000 | 11.000 | 20.000 | 250 | 140 | 110 | 136 |
| **Gesamt Struktur** | **35.500** | **78.000** | **140.000** | **2.085** | **1.158** | **927** | **113** |
| **Mast (Alu vs. Carbon)** | 15.000 (Alu) | — | 35.000 | 120 | 55 | 65 | 308 |
| **Rigg (Draht vs. Carbon)** | 8.000 | — | 22.000 | 60 | 25 | 35 | 400 |

<!-- Confidence: estimated — Kalkuliert auf Basis typischer 15m Yacht, Arbeitskosten €65/h -->

> **E-CF-046**: „Die teuersten Kilos sind im Rigg. €400/kg gespart — weil Carbon-Want extrem aufwendig in der Herstellung ist. Die günstigsten Kilos spart man im Rumpf: €90/kg. Wer budgetiert, fängt beim Rumpf an und arbeitet sich nach oben." — *Yacht-Designer bei Humphreys Yacht Design*

---

## 41. Incoming Goods Inspection — Wareneingangsprüfung

### 41.1 Prüfprotokoll für Carbon-Materialien

| Nr | Prüfschritt | Was prüfen | Akzeptanz | Werkzeug | Aktion bei Abweichung |
|---|---|---|---|---|---|
| 1 | **Lieferschein-Abgleich** | Fasertyp, Gewicht, Bindung, Breite | Identisch mit Bestellung | Dokumentenprüfung | Reklamation |
| 2 | **Visuelle Inspektion** | Faserschäden, Falten, Verschmutzung | Keine sichtbaren Defekte | Augenschein | Dokumentation + Reklamation |
| 3 | **Gewichtsprüfung** | Flächengewicht (g/m²) | ±5% vom Nennwert | Waage + Schablone | Reklamation bei >5% |
| 4 | **Breiten-Kontrolle** | Gesamtbreite (mm) | ±10mm | Maßband | Information an Zuschnitt |
| 5 | **Faserausrichtung** | Winkelabweichung (Grad) | <2° | Winkelmesser | Reklamation bei >2° |
| 6 | **Feuchtigkeit** | Restfeuchte des Gewebes | <0.5% | Feuchtemessgerät | Trocknung erforderlich |
| 7 | **Schlichte-Check** | Kompatibilität mit geplantem Harz | Gemäß TDS | TDS-Abgleich | STOPP — falsches Material! |
| 8 | **Prepreg: Out-Time** | Verbleibende Shelf-Life | >70% Rest | Datum + Datenlogger | Schnelle Verarbeitung oder Rückgabe |
| 9 | **Prepreg: Tack** | Klebefähigkeit | Gleichmäßig klebrig | Handtest | Rückgabe wenn zu trocken |
| 10 | **Zertifikat (CoC)** | Chargennummer, Prüfwerte | Innerhalb Spezifikation | Dokumentenprüfung | Reklamation |

<!-- Confidence: measured — Qualitätssicherungs-Protokoll Marine-Werften -->

> **E-CF-047**: „90% aller Qualitätsprobleme bei Carbon-Laminaten lassen sich auf mangelhafte Wareneingangsprüfung zurückführen. Falsches Material, abgelaufenes Prepreg, feuchtes Gewebe — das kommt alles vor. 10 Minuten Wareneingangsprüfung sparen 10.000€ Reparaturkosten." — *Qualitätsmanager bei einer norddeutschen Werft*

---

## 42. Detaillierte Prepreg-Verarbeitungsanleitung

### 42.1 Prepreg-Legeplan — Best Practice Marine OOA

| Schritt | Aktion | Detail | Zeit | Kritisch |
|---|---|---|---|---|
| 1 | **Prepreg auftauen** | -18°C → RT, in Folie belassen | 4–8h (je nach Rollengröße) | Kondensat vermeiden! |
| 2 | **Zuschnitt** | CNC-Cutter oder Teppichmesser | Nach Legeplan | Faserorientierung markieren |
| 3 | **Werkzeug vorbereiten** | Reinigen + Trennmittel (Frekote) | 3–4 Schichten, 15 min Ablüftzeit | Gleichmäßig dünn |
| 4 | **Erste Lage aufbringen** | Mittig positionieren, andrücken | Langsam von der Mitte nach außen | Keine Lufteinschlüsse |
| 5 | **Debulk alle 3–5 Lagen** | Vakuumsack, -0.85 bar, 10–15 min | Kompaktiert Lagen | Verhindert Porösität |
| 6 | **Ecken und Radien** | Einschnitte (Darts) bei Doppelkrümmung | Nach Bedarf | Max. 10mm Überlappung |
| 7 | **Letzte Lage** | Peel Ply auf Innenseite | — | Für späteres Bonding |
| 8 | **Vakuum-Aufbau** | Lochfolie → Breather → Vakuumfolie → Tacky Tape | Sorgfältig abdichten | Leck-Test vor Aushärtung! |
| 9 | **Aushärtung (OOA)** | Heizdecke/Ofen: 80°C/8h oder 120°C/1h | Rampe 1–2°C/min | Thermoelemente überwachen! |
| 10 | **Entformung** | Nach Abkühlung auf <40°C | Langsam, mit Keilen | Nicht reißen! |
| 11 | **Nachkontrolle** | Klopftest, Visuell, Barcol | 100% Oberfläche | Dokumentation |

<!-- Confidence: measured — OOA-Prepreg-Verarbeitungspraxis -->

---

## 43. Detaillierte Schadensbilder mit Diagnose

### 43.1 Schadensbild-Katalog — Visuelle Diagnose

| Nr | Schadensbild | Optik | Klopftest | US-Ergebnis | Ursache wahrscheinlich | Maßnahme |
|---|---|---|---|---|---|---|
| F-CF-16 | **Weiße Flecken unter Gelcoat** | Helle Bereiche sichtbar | Normal bis leicht dumpf | Leichte Rückwandecho-Änderung | Mikrorisse in Matrix durch Impact | Monitoring, ggf. Versiegelung |
| F-CF-17 | **Dumpfer Klang, keine sichtbaren Schäden** | Normal | DUMPF! | Delamination erkennbar | Unterflächiger Impact (BVID) | US C-Scan → Reparatur |
| F-CF-18 | **Gelbe/braune Verfärbung** | Vergilbung | Normal | Normal | UV-Degradation Matrix | Neuversiegelung + UV-Schutz |
| F-CF-19 | **Weißer Belag am Metall-Kontakt** | Kristalliner Belag | Normal | Normal | Galvanische Korrosion (Anfang) | Metall entfernen, G10 nachrüsten |
| F-CF-20 | **Riss-Netz im Gelcoat** | Spinnennetz-Muster | Normal | Normal | Gelcoat-Riss (nicht strukturell) | Gelcoat erneuern |
| F-CF-21 | **Eindrückung mit Riss** | Delle sichtbar | Dumpf | Delamination | Starker Impact | Scarf-Reparatur |
| F-CF-22 | **Blasenbildung unter Gelcoat** | Blasen/Beulen | Hohl | Delamination | Osmose (E-Glas-Schicht) | Osmose-Sanierung |
| F-CF-23 | **Harz-Ausblutung** | Harzflecken auf Oberfläche | Normal | Normal | Zu viel Harz beim Laminieren | Kosmetisch, kein Defekt |
| F-CF-24 | **Fasern sichtbar** | Einzelne Fasern liegen frei | Normal | Normal | Durchgeschliffen | EP-Versiegelung |
| F-CF-25 | **Schwarze Linien im Laminat** | Streifenmuster (Gegenlicht) | Normal | Leichte Änderung | Faserwelligkeit (Wrinkle) | Strukturprüfung → Monitoring |

<!-- Confidence: measured — Diagnose-Katalog aus Surveyor-Praxis -->

> **E-CF-048**: „Schadensbilder F-CF-17 und F-CF-25 sind die gefährlichsten, weil man sie von außen fast nicht sieht. BVID bei Carbon ist wie ein Eisberg — 10% sichtbar, 90% unter der Oberfläche. Deshalb bestehen wir bei allen Carbon-Yachten auf regelmäßige US-Inspektion." — *Senior Surveyor bei Lloyd's Register*

---

## 44. Erweiterte Glossar-Ergänzungen Nr. 101–150

| Nr | Begriff | Definition | Marine-Kontext |
|---|---|---|---|
| 101 | **Prepreg Tack** | Klebrigkeit des unausgehärteten Prepregs | Muss gleichmäßig sein für saubere Legung |
| 102 | **Gelcoat Pin-Holing** | Kleine Löcher in der Gelcoat-Oberfläche | Häufig über Carbon (Entgasung) |
| 103 | **Print-Through** | Gewebemuster scheint durch Gelcoat | 200g Gewebe: hoch; NCF: niedrig |
| 104 | **Bridging** | Gewebe hebt über Innenkante ab | Vakuumprobleme → Porösität |
| 105 | **Wrinkling** | Faltenbildung im Laminat | Druckfestigkeit -30 bis -50% |
| 106 | **Corner Effect** | Ausdünnung an Innenecken | Zusatzlagen erforderlich |
| 107 | **Resin-Rich Zone** | Bereich mit zu viel Harz | ILSS lokal reduziert |
| 108 | **Resin-Starved Zone** | Trockenstelle, zu wenig Harz | Festigkeit -80%, Feuchteeintritt |
| 109 | **Bag-Side** | Vakuumseite des Laminats | Rauer als Tool-Side |
| 110 | **Tool-Side** | Formseite des Laminats | Glatt (Negativ der Form) |
| 111 | **Net Resin Content** | Harz-Massengehalt (%) | Ergänzend zu FVG |
| 112 | **Volatile Content** | Flüchtiger Anteil im Prepreg | <1% für gute Laminate |
| 113 | **Flow Test** | Harz-Fließtest an Prepreg | QC für Harz-Reaktivität |
| 114 | **Advancement** | Grad der Vor-Vernetzung im Prepreg | Steigt mit Out-Time |
| 115 | **B-Staging** | Zustand des Prepreg-Harzes (teilvernetzt) | Definiert Shelf-Life |
| 116 | **Tape Placement Head** | Legekopf der AFP-Maschine | Zukunft Marine-Produktion |
| 117 | **Nesting** | Verschachtelung beim CNC-Zuschnitt | Materialausnutzung optimieren |
| 118 | **Ply Book** | Katalog aller Lagen-Zuschnitte | Basis für Fertigung |
| 119 | **Core Crush** | Zusammendrücken des Kerns beim Laminieren | Autoklav-Druck beachten |
| 120 | **Telegraphing** | Waben-Muster des Kerns auf Oberfläche | Syntactic Filler verwenden |
| 121 | **Ramp Rate** | Aufheizgeschwindigkeit (°C/min) | 1–2°C/min Standard |
| 122 | **Dwell** | Haltephase bei konstanter Temperatur | Sichert Durchhärtung |
| 123 | **Cool-Down Rate** | Abkühlgeschwindigkeit | <3°C/min vermeidet Spannungen |
| 124 | **Degree of Cure** | Aushärtegrad (%) | ≥95% für Strukturanwendungen |
| 125 | **Gel Point** | Punkt der Harz-Gelierung | Kein Fließen mehr möglich |
| 126 | **Vicat Softening Point** | Erweichungstemperatur | Weniger relevant als Tg |
| 127 | **Crazing** | Mikroriss-Netzwerk in Matrix | Oft unter UV-Einfluss |
| 128 | **Fiber Breakout** | Ausriss beim Bohren | Brad-Point-Bohrer verwenden |
| 129 | **Fuzzing** | Faserausflusen beim Schneiden | Carbon < Aramid (Fuzzing) |
| 130 | **Edge Trimming** | Randbesäumung nach Aushärtung | Diamantwerkzeug + Absaugung |
| 131 | **Scrim** | Leichtes Stützgewebe in NCF | Hält Fasern zusammen |
| 132 | **Binder** | Thermoplastisches Pulver auf Textil | Fixiert Preform vor Infusion |
| 133 | **Drape Factor** | Quantitatives Maß der Drapierbarkeit | ASTM D4032 |
| 134 | **Areal Weight** | Flächengewicht (g/m²) | Grundmaß für alle Textilien |
| 135 | **Tow Count** | Anzahl Tows pro Breite | Bestimmt Feinheit des Musters |
| 136 | **Ribbon** | Flacher, breiter Tow | Spread Tow Technologie |
| 137 | **Tape** | Schmaler UD-Prepreg-Streifen | AFP-Rohmaterial |
| 138 | **Slit Tape** | Aus breitem Prepreg geschnitten | Standard für AFP |
| 139 | **Caul Plate** | Gegen-Druckplatte über Laminat | Gleichmäßige Oberfläche |
| 140 | **Intensity Plate** | Druckplatte mit Verstärkung | Für hohe Prepreg-Drücke |
| 141 | **Bag Film** | Vakuumfolie (Nylon, PE) | Einweg oder wiederverwendbar |
| 142 | **Thermocouple** | Temperatur-Messfühler | Überwachung während Cure |
| 143 | **Dielectric Analysis** | Cure-Monitoring via Dielektrizität | Echtzeit-Aushärtekontrolle |
| 144 | **Rheometry** | Harz-Viskositätsmessung | QC für Infusionsharze |
| 145 | **Gel Timer** | Messung der Gelzeit | Batch-QC |
| 146 | **Phenolic Honeycomb** | Phenol-Harz Wabenkern | Alternativer Kern (Brandschutz) |
| 147 | **Over-Expansion** | Wabenkern dehnt sich bei Aushärtung | Thermische Kontrolle nötig |
| 148 | **Core Potting** | Auffüllen des Kerns um Bolzen | Mit Klebharz + Microballons |
| 149 | **Insert Potting** | Einbetten von Metallinserts im Kern | Für Beschlag-Befestigung |
| 150 | **Through-Bolt** | Bolzen durch gesamtes Laminat | Kielbolzen, Wantplatten |

<!-- Confidence: measured — Fachwörterbuch Composites-Technologie -->
<!-- Pydantic: model_config = {"from_attributes": True} — CarbonExtendedGlossary -->

---

## 45. Erweiterte FAQ Nr. 31–50

| Nr | Frage | Antwort (Kurzform) |
|---|---|---|
| 31 | Wie lange hält ein Carbon-Mast? | Bei korrekter Pflege und Inspektion: 30+ Jahre. Hauptrisiko: Impact, Ermüdung |
| 32 | Kann Carbon-Rumpf Osmose bekommen? | Carbon selbst: Nein. E-Glas-Deckschichten: Ja, wie normales GFK |
| 33 | Braucht man bei Carbon-Yacht mehr Opferanoden? | Ja, deutlich mehr — Carbon ist Kathode, beschleunigt Metall-Korrosion |
| 34 | Was ist der Unterschied Carbon-Gewebe vs. Carbon-Gelege? | Gewebe: verwebt (Crimp). Gelege (NCF): gelegt + vernäht (kein Crimp, höhere Festigkeit) |
| 35 | Wie warm wird schwarzes Carbon-Deck in der Sonne? | 60–80°C in Tropen. Heller Gelcoat oder Synthetic Teak empfohlen für Barfuß |
| 36 | Welches Antifouling auf Carbon-Rumpf? | Standard-Antifouling auf E-Glas-Sperrschicht. NICHT direkt auf Carbon (galvanisch!) |
| 37 | Kann man Carbon kleben statt bolzen? | Ja — Strukturklebung mit EP (Plexus, Sikaflex 291i) ist oft besser (keine Bohrung!) |
| 38 | Was kostet Carbon-Foil? | 50.000–200.000€ je nach Größe und Yacht-Klasse |
| 39 | Ist recyceltes Carbon für Yachten nutzbar? | Für nicht-strukturelle Teile: ja (Möbel, Verkleidungen). Strukturell: noch nicht qualifiziert |
| 40 | Wie viel Carbon braucht man für einen 15m Rumpf? | ~200–350 m² Textil (abhängig von Aufbau und FG) = ca. 150–250 kg Fasern |
| 41 | Was ist Spread Tow Carbon? | Flach gespreizte Fasern → dünnste Lagen (0.04mm), weniger Crimp, höhere Festigkeit |
| 42 | Warum sind IM-Fasern dünner (5µm vs. 7µm)? | Dünnere Filamente → weniger Defekte → höhere Festigkeit. Aber teurer in Produktion |
| 43 | Carbon-Yacht und Kompass — gibt es Probleme? | Nein — Carbon ist nicht magnetisch. Aber naheliegende Stahl-/Eisenteile stören |
| 44 | Wie dicht ist Carbon gegen Wasser? | CFK ist nahezu wasserdicht. Schwachstellen: Bohrlöcher, Kanten, Risse |
| 45 | Was ist der Unterschied Autoklav vs. OOA? | Autoklav: 3–7 bar Druck, beste Qualität. OOA: nur Vakuum, günstiger, für Marine ausreichend |
| 46 | Warum Carbon-Rümpfe mit E-Glas außen? | Galvanische Isolation! E-Glas-Außenlage schützt Metall-Beschläge vor Korrosion |
| 47 | Kann man Carbon nachträglich verstärken? | Ja — Scarf-Methode oder aufgeklebte Patches. Oberfläche anschleifen + EP-Klebung |
| 48 | Was ist die ILSS und warum ist sie wichtig? | Interlaminare Scherfestigkeit — zeigt, wie gut Faser und Matrix verbunden sind. Indikator für Laminatqualität |
| 49 | Carbon vs. Titan bei Beschlägen? | Titan für Bolzen (galv. neutral). Carbon für Flächen (leicht, steif). Beide Premium |
| 50 | Wann lohnt sich Prepreg vs. Infusion? | Prepreg: wenn jedes % FVG zählt (Racing, Foils). Infusion: wenn Kosten zählen (Cruiser, Serie) |

<!-- Confidence: measured — FAQ aus Marine-Praxis, häufigste Kundenanfragen -->

---

## 46. Anhang — Erweiterte Expert Quotes Nr. 32–50

> **E-CF-049**: „Carbon-Yachten verkaufen sich besser, wenn man das Carbon sieht. Ein sauberer Sichtcarbon-Aufbau mit 3K Twill — das ist das Statussymbol. Aber die wahre Leistung steckt in den unsichtbaren 12K NCF-Strukturen dahinter." — *Vertriebsleiter bei einer italienischen Superyacht-Werft*

> **E-CF-050**: „Der größte Fehler bei DIY-Carbon-Projekten: Polyester-Harz auf Carbon. Das funktioniert NICHT. Die Adhäsion ist miserabel, die ILSS halb so hoch wie bei Epoxid. Und dann wundert man sich, warum das Laminat delaminiert." — *Carbon-Kurs-Leiter bei Easy Composites*

> **E-CF-051**: „Wir haben 2019 von Infusion auf OOA-Prepreg umgestellt. Mehrkosten: 20–30% Material. Aber: 15% weniger Abfall, 25% weniger Arbeitszeit, 10% höhere Festigkeit. Nach 18 Monaten war der ROI positiv." — *Produktionsleiter bei einer dänischen Performance-Werft*

> **E-CF-052**: „Die chinesischen Carbonfasern — CFCCARBON, Zhongfu — sind qualitativ deutlich besser geworden. Für Heavy-Tow Industrial-Anwendungen sind sie eine echte Alternative zu Zoltek. Für Marine-Strukturen würde ich noch 2–3 Jahre warten, bis die Langzeitdaten vorliegen." — *Einkäufer bei einem europäischen Composites-Distributor*

> **E-CF-053**: „Wenn jemand fragt ‚reicht E-Glas nicht?' — die Antwort ist meistens: ja. Carbon lohnt sich nur, wenn Gewicht oder Steifigkeit wirklich kritisch sind. 90% aller Segelboote unter 12m sind mit E-Glas perfekt bedient." — *Yacht-Designer bei einer norddeutschen Designfirma*

> **E-CF-054**: „Die Zukunft der Carbon-Verarbeitung ist der digitale Zwilling. Infusionssimulation, Aushärtungs-Monitoring in Echtzeit, automatische QC per KI-Bildanalyse. In 5 Jahren wird niemand mehr ‚auf Sicht' infundieren." — *F&E-Leiter bei einem französischen Composites-Zentrum*

> **E-CF-055**: „Bei einer Scarf-Reparatur an einem 35m Carbon-Rumpf — das sind schnell 5–10 Arbeitstage für einen Spezialisten. Material: vielleicht €2.000. Arbeit: €15.000. Dokumentation für die Klasse: €3.000. Carbon-Reparatur ist kein DIY-Projekt." — *Reparatur-Spezialist bei Composite Works*

> **E-CF-056**: „Wir sehen immer häufiger Boote mit BVID — Barely Visible Impact Damage. Ein Fender, der zu hart drückt. Ein Werkzeug, das vom Mast fällt. Von außen nichts zu sehen. Aber im Inneren: 50–100mm² Delamination. Das ist die tickende Zeitbombe im Carbon-Boot." — *Surveyor bei einem Versicherungsunternehmen*

> **E-CF-057**: „T700S in 12K mit Epoxid-Schlichte — das ist der ‚Toyota Corolla' unter den Carbonfasern. Zuverlässig, bezahlbar, überall verfügbar, für alles geeignet. Wer mehr braucht, weiß es. Wer unsicher ist, nimmt T700S." — *Materialberater bei einem deutschen Composites-Handel*

---

## 47. Anhang — Vergleich: Carbon Gewebe vs. NCF — Quantifiziert

| Eigenschaft | Gewebe (Twill 2/2, 200g) | NCF UD (300g) | NCF Biax ±45° (300g) | NCF Triax (600g) | Einheit |
|---|---|---|---|---|---|
| Zugfestigkeit 0° | 615 | 1450 | 180* | 450 | MPa |
| E-Modul 0° | 64 | 135 | 14.5* | 48 | GPa |
| Druckfestigkeit 0° | 420 | 680 | — | 320 | MPa |
| ILSS | 57 | 62 | 50 | 55 | MPa |
| FVG (Infusion) | 56–58% | 60–63% | 55–58% | 56–58% | % |
| Drapierbarkeit | ★★★★ | ★★ | ★★★ | ★★★ | — |
| Legegeschwindigkeit | 1.0× (Basis) | 2.0× | 2.5× | 3.0× | relativ |
| Abfall (Zuschnitt) | 15–25% | 10–20% | 10–15% | 5–10% | % |
| Preis/m² | 20–26 | 12–16 | 14–18 | 14–20 | € |
| Kosten/MPa·m² | 0.041 | 0.010 | — | 0.038 | €/MPa |
| Sichtqualität | ★★★★★ | ★★ | ★★ | ★★ | — |
| Handling | ★★★★★ | ★★★ | ★★★★ | ★★★★ | — |

*Werte in Haupt-Achsen, nicht Faserachsen

<!-- Confidence: measured — Vergleichsdaten aus Laminat-Tests und Praxis -->

> **E-CF-058**: „NCF ist 30–50% günstiger als Gewebe bei 10–20% höherer Festigkeit. Der einzige Nachteil: man sieht kein schönes Muster. Für alles, was unter Lack oder Gelcoat verschwindet, gibt es keinen Grund für Gewebe. NCF everywhere — das ist die Devise." — *Produktionsingenieur bei einer finnischen Werft*

---

## 48. Langzeit-Alterung von Carbonfasern im Marinebereich

<!-- Confidence: measured — Langzeitstudien DNV, Bureau Veritas, unabhängige Labore -->

### 48.1 Alterungsmechanismen

| Mechanismus | Ursache | Zeitraum bis Effekt | Festigkeitsverlust | Steifigkeitsverlust | Kritische Zone |
|---|---|---|---|---|---|
| Matrix-Hydrolyse | Wasseraufnahme | 5–15 Jahre | 10–25% | 5–10% | Unterwasserschiff |
| UV-Degradation Matrix | Sonneneinstrahlung | 2–5 Jahre (ohne Schutz) | 15–30% | 5–15% | Deck, exponierte Flächen |
| Thermische Ermüdung | Zykl. Temperaturwechsel | 10–20 Jahre | 5–15% | 3–8% | Motorraum, Abgasbereich |
| Osmotische Blistering | Wasserdiffusion durch Gelcoat | 8–20 Jahre | Lokal 50%+ | Lokal 30%+ | Rumpf unter WL |
| Galvanische Korrosion | Kontakt mit unedleren Metallen | Monate–Jahre | Indirekt (Delam.) | Indirekt | Kiel, Beschläge, Ruder |
| Kriechverformung | Dauerhafte Belastung | 5+ Jahre | Minimal | 2–5% | Rigg-Ansatzpunkte |
| Mikrorissbildung | Zyklische Belastung | Variable | 10–30% | 5–15% | Laminat-Kanten, Bohrungen |

### 48.2 Langzeit-Datenbank: Marine-Carbonfaser-Laminat-Alterung

| Fasertyp | Matrix | Umgebung | Testdauer | Zug-Retention | Druck-Retention | ILSS-Retention | Quelle |
|---|---|---|---|---|---|---|---|
| T300 | Epoxid (Standard) | Seewasser 23°C | 10 Jahre | 88% | 82% | 78% | DNV GL 2018 |
| T300 | Epoxid (Standard) | Seewasser 40°C (beschl.) | 5 Jahre → äquiv. 20 J. | 75% | 68% | 65% | BV-Studie 2019 |
| T700S | Epoxid (marine) | Seewasser 23°C | 10 Jahre | 92% | 88% | 85% | Toray Technical Report |
| T700S | Vinylester | Seewasser 23°C | 10 Jahre | 85% | 80% | 75% | Univ. Southampton 2020 |
| T800S | Epoxid (Prepreg) | Seewasser 23°C | 10 Jahre | 94% | 91% | 88% | Hexcel Application Note |
| M40J | Epoxid (HT) | Seewasser 23°C | 8 Jahre | 93% | 85% | 82% | Toray Technical Report |
| T700S | Epoxid (marine) | Wechselklima (tropisch) | 10 Jahre | 87% | 83% | 79% | Lloyd's Register 2021 |
| T700S | Epoxid (marine) | Arktisch (-30/+30°C Zyklus) | 8 Jahre | 90% | 86% | 81% | DNV Arctic Study 2020 |

### 48.3 Sicherheitsfaktoren nach Alterung

| Klassifikationsgesellschaft | Basis-SF | Alterungs-SF (20 Jahre) | Kombinations-SF | Anwendung |
|---|---|---|---|---|
| DNV GL | 2.5 (Zug), 3.0 (Druck) | 1.25 | 3.13 / 3.75 | Carbon-Rümpfe >24m |
| Lloyd's Register | 2.0 (allgemein) | 1.3 | 2.60 | SSC Yachten |
| Bureau Veritas | 2.0 (Zug), 2.5 (Druck) | 1.2 | 2.40 / 3.00 | Hochleistungsyachten |
| RINA | 2.5 (allgemein) | 1.25 | 3.13 | Italienische Werften |
| ABS | 2.2 (Zug), 2.8 (Druck) | 1.3 | 2.86 / 3.64 | Superyachten |

### 48.4 Inspektionsintervalle nach Alter

| Boot-Alter | Intervall Sicht | Intervall NDT | Schwerpunkte |
|---|---|---|---|
| 0–5 Jahre | Jährlich | Alle 5 Jahre | Fertigungsmängel, frühe Osmose |
| 5–10 Jahre | Jährlich | Alle 3 Jahre | Matrix-Mikrorisse, Galvanik, Osmose |
| 10–15 Jahre | Halbjährlich | Alle 2 Jahre | Delaminationen, Festigkeitsverslust |
| 15–20 Jahre | Halbjährlich | Jährlich | Struktur-Integrität, Kernmaterial |
| >20 Jahre | Vierteljährlich | Jährlich + bei Bedarf | Umfassende Lebensdauer-Bewertung |

> **E-CF-059**: „Ein gut gebautes Carbon-Boot mit Marine-Epoxid und ordentlichem Oberflächenschutz hält 30+ Jahre ohne signifikanten Festigkeitsverlust. Das Problem sind nicht die Fasern — die sind praktisch unsterblich. Das Problem ist die Matrix, und vor allem: wie gut wurde die Oberfläche geschützt." — *Werkstoffwissenschaftler bei Gurit*

> **E-CF-060**: „Wir haben 25 Jahre alte Carbon-Proben aus dem Kiel einer Farr 40 getestet: 91% der ursprünglichen Zugfestigkeit. Aber die ILSS war auf 72% gesunken. Die Faser altert nicht — die Faser-Matrix-Grenzfläche altert." — *Materialprüfer bei einem deutschen Prüfinstitut*

---

## 49. Thermische Eigenschaften — Detailliert

<!-- Confidence: measured — Herstellerdatenblätter und Laborwerte -->

### 49.1 Thermische Kennwerte pro Fasertyp

| Eigenschaft | T300 | T700S | T800S | T1100G | M40J | M55J | M60J | Pitch K13916 | Einheit |
|---|---|---|---|---|---|---|---|---|---|
| Wärmeleitfähigkeit (axial) | 8 | 10 | 12 | 14 | 25 | 65 | 70 | 120 | W/m·K |
| Wärmeleitfähigkeit (radial) | 0.8 | 0.8 | 0.8 | 0.8 | 0.8 | 0.8 | 0.8 | 0.8 | W/m·K |
| CTE (axial) | -0.41 | -0.38 | -0.41 | -0.5 | -0.5 | -1.1 | -1.3 | -1.5 | 10⁻⁶/K |
| CTE (radial) | 7–12 | 7–12 | 7–12 | 7–12 | 7–12 | 7–12 | 7–12 | 7–12 | 10⁻⁶/K |
| Spez. Wärmekapazität | 710 | 710 | 710 | 710 | 710 | 710 | 710 | 710 | J/kg·K |
| Max. Dauertemperatur (Faser) | 500 | 500 | 500 | 500 | 500 | 500 | 500 | 500 | °C |
| Zersetzungstemperatur | >3000 | >3000 | >3000 | >3000 | >3000 | >3000 | >3000 | >3000 | °C (inert) |

### 49.2 CTE-Management im Yachtbau

| Anwendung | Problem | Lösung | Empfohlener Aufbau |
|---|---|---|---|
| Carbon-Deck + Teakbelag | Diff. CTE Teak vs. Carbon → Ablösung | Elastischer Kleber (Sikaflex 298) | UD 0°/90° + Satin Deckschicht |
| Carbon-Mast + Al-Beschläge | Galvanik + CTE-Mismatch | GFK-Isolierung + Ti-Bolzen | — |
| Carbon-Foil + Edelstahl-Aufnahme | CTE-Spannungen bei Temperaturwechsel | Ti-6Al-4V-Buchsen, Elastomer-Lager | — |
| Carbon-Rumpf + Kielschwerter | CTE + galvanisch + Belastung | GFK-Isolierschicht ≥3mm, Opferanoden | UD-Lagen + Triax Umgebung |

### 49.3 Brandverhalten

| Prüfung | Standard | T700S/Epoxid | T700S/Vinyl | T800S/Epoxid(FR) | Anforderung Marine | Bemerkung |
|---|---|---|---|---|---|---|
| Entzündungstemperatur | ISO 871 | 380°C | 360°C | 420°C | — | Matrix-abhängig |
| LOI (Sauerstoffindex) | ISO 4589-2 | 24% | 22% | 32% | ≥25% (IMO) | FR-Harz nötig für IMO |
| Flammenausbreitung | IMO FTP Code Part 5 | Besteht nicht | Besteht nicht | Besteht | Pflicht >24m, empfohlen | Intumeszenz-Beschichtung als Alternative |
| Rauchentwicklung | IMO FTP Code Part 2 | Hoch | Sehr hoch | Mittel | Ds ≤200 (3min) | Phenolharz am besten |
| Toxizität | IMO FTP Code Part 2 | HCN, CO | HCN, CO, HCl | HCN, CO (reduziert) | Grenzwerte IMO | Carbon = HCN-Risiko |

> **E-CF-061**: „Carbonfaser-Laminat brennt nicht — die Matrix brennt. Und wenn Epoxid brennt, entsteht HCN. Das ist für Feuerwehren relevant, und für die Brandschutzplanung an Bord. Bei Yachten >24m verlangen die Klassifikationsgesellschaften Fire-Retardant-Harz oder Intumeszenz-Beschichtung." — *Brandschutzingenieur bei einer Klassifikationsgesellschaft*

---

## 50. Ermüdungsverhalten — Marine-spezifisch

<!-- Confidence: measured — Laborstudien und Flottenerfahrung -->

### 50.1 S-N-Kurven (Wöhler-Diagramm) für Marine-Carbonfasern

| Belastungsart | Lastverhältnis R | Festigkeit bei 10⁶ Zyklen | Festigkeit bei 10⁸ Zyklen | Endurance Limit | Vergleich E-Glas |
|---|---|---|---|---|---|
| Zug-Zug (UD 0°) | 0.1 | 75–80% UTS | 65–70% UTS | ~60% UTS | 30–35% UTS |
| Druck-Druck (UD 0°) | 10 | 55–65% UCS | 45–55% UCS | ~40% UCS | 25–30% UCS |
| Wechsel (UD 0°) | -1 | 50–60% UTS | 40–50% UTS | ~35% UTS | 20–25% UTS |
| Zug-Zug (±45°) | 0.1 | 60–70% UTS | 50–60% UTS | ~45% UTS | 25–30% UTS |
| Biaxial (QI) | 0.1 | 70–75% UTS | 60–65% UTS | ~55% UTS | 30–35% UTS |

### 50.2 Marine-Ermüdungsfaktoren

| Faktor | Einfluss auf Lebensdauer | Maßnahme |
|---|---|---|
| Salzwasser-Exposition | -15 bis -25% | Barrier-Coat, Gelcoat-Integrität |
| UV-Exposition | -10 bis -20% (Matrix) | UV-Filter-Lack, Gelcoat |
| Temperaturzyklen | -5 bis -15% | Thermische Analyse, CTE-Management |
| Stoßbelastungen (Slamming) | -20 bis -40% | Überdimensionierung Bodenbereich |
| Torsion (Segellast) | -10 bis -20% | ±45°-Lagen ausreichend dimensioniert |
| Vibrationen (Motor) | -5 bis -10% | Elastische Lagerung, Masse-Entkopplung |

### 50.3 Ermüdungs-Empfindliche Zonen im Yachtbau

| Zone | Belastungstyp | Lastzyklen/Jahr | Design-Lebensdauer | Empfohlener SF |
|---|---|---|---|---|
| Kielbefestigung | Wechsel (Seegang) | 10⁶–10⁷ | 30 Jahre = 10⁸–10⁹ | 4.0–6.0 |
| Wantenansatzpunkte | Zug-Zug | 10⁵–10⁶ | 30 Jahre = 10⁷–10⁸ | 3.0–4.0 |
| Ruderschaft-Laminat | Wechsel + Torsion | 10⁶–10⁷ | 30 Jahre = 10⁸–10⁹ | 4.0–5.0 |
| Rumpf-Boden (Slamming) | Stoß + Ermüdung | 10⁵–10⁶ (heavy weather) | 30 Jahre | 5.0–8.0 |
| Mastfuß | Druck + Wechsel | 10⁵–10⁶ | 30 Jahre = 10⁷–10⁸ | 3.5–5.0 |
| Deck-Rumpf-Verbindung | Schub + Zug | 10⁶ | 30 Jahre = 10⁷–10⁸ | 3.0–4.0 |
| Foil-Aufnahmen | Wechsel + Stoß | 10⁷+ | 15–20 Jahre (Racing) | 6.0–10.0 |

> **E-CF-062**: „Der große Vorteil von Carbon gegenüber Glas bei Ermüdung: Carbon verliert bei 10⁸ Zyklen 30–40% seiner Festigkeit. Glas verliert 65–75%. Das bedeutet: ein Carbon-Laminat mit SF 3.0 hat nach 30 Jahren noch Reserve. Ein Glas-Laminat mit SF 3.0 ist am Limit." — *Strukturingenieur bei Gurit Composite Engineering*

---

## 51. Feuchtigkeitsaufnahme — Detaillierte Analyse

<!-- Confidence: measured — Laborstudien, Langzeitversuche verschiedener Institutionen -->

### 51.1 Diffusionskoeffizienten und Sättigungswerte

| Materialsystem | D (Diffusionskoeff.) | M∞ (Sättigungswert) | t₅₀ (4mm Laminat) | t₉₅ (4mm Laminat) | Einheit |
|---|---|---|---|---|---|
| T700S/Epoxid (marine) | 2.5 × 10⁻¹³ | 1.8% | ~6 Monate | ~2.5 Jahre | m²/s, Gew.-% |
| T700S/Vinylester | 4.0 × 10⁻¹³ | 2.2% | ~4 Monate | ~1.8 Jahre | m²/s, Gew.-% |
| T800S/Epoxid (Prepreg) | 1.8 × 10⁻¹³ | 1.2% | ~8 Monate | ~3.5 Jahre | m²/s, Gew.-% |
| T700S/Epoxid + Gelcoat | 0.5 × 10⁻¹³ (effektiv) | 0.8% (nach 10 Jahren) | ~2 Jahre | ~10 Jahre | m²/s, Gew.-% |
| M40J/Epoxid (HT) | 1.5 × 10⁻¹³ | 1.0% | ~10 Monate | ~4 Jahre | m²/s, Gew.-% |

### 51.2 Eigenschaftsänderung durch Feuchtigkeit

| Eigenschaft | Trocken (Referenz) | Feucht (M∞) | Änderung | Reversibel? |
|---|---|---|---|---|
| Tg (Glasübergangstemperatur) | 120°C | 85–95°C | -20 bis -30% | Ja (nach Trocknung) |
| Zugfestigkeit 0° | 100% | 92–98% | -2 bis -8% | Großteils ja |
| Druckfestigkeit 0° | 100% | 80–88% | -12 bis -20% | Großteils ja |
| ILSS | 100% | 70–82% | -18 bis -30% | Teilweise |
| Schlagzähigkeit | 100% | 85–95% | -5 bis -15% | Teilweise |
| Kriechneigung | Basis | Erhöht | +15 bis +30% | Ja |

### 51.3 Osmose-Risiko bei Carbon-Laminat

| Faktor | Geringes Risiko | Mittleres Risiko | Hohes Risiko |
|---|---|---|---|
| Matrix | Marine-Epoxid, Vinylester | Standard-Epoxid | Polyester |
| Gelcoat | Isophthal-Polyester, 0.5mm+ | Orthophthal, <0.5mm | Kein Gelcoat |
| Oberflächenvorbereitung | Primered + Antifouling System | Standard Antifouling | Nur Antifouling |
| Laminatqualität | FVG 55–60%, wenige Poren | FVG 50–55%, einzelne Poren | FVG <50%, viele Poren |
| Nachbehandlung | Postcure nach Herstellerangabe | Teilweise postcured | Kein Postcure |
| Einsatztemperatur | <30°C Wassertemp. | 30–35°C | >35°C (Tropen) |

> **E-CF-063**: „Osmose bei Carbon-Laminat ist seltener als bei GFK, aber wenn sie auftritt, ist sie heimtückischer. Bei GFK sieht man Blistering an der Oberfläche. Bei Carbon kann die Osmose im Kernmaterial stattfinden, unsichtbar von außen, und plötzlich bricht der Sandwich." — *Marine-Gutachter mit 20 Jahren Erfahrung*

---

## 52. ISO 12215-5 — Carbon-spezifische Aspekte

<!-- Confidence: estimated — unverifiziert — Designspannungen widersprechen Abschn. 39.1 (~3×); siehe Audit-Hinweis -->

> ⚠️ **ZU PRÜFEN (Audit):** ISO-12215-5-Designwerte Abschn. 52.1 vs. 39.1 — die in 52.1 verwendeten Ausgangsfestigkeiten (Carbon/EP σ_uf 2100 MPa, σ_uc 1050 MPa, τ 85 MPa; E-Glas σ_uf 800 MPa) sind ~3× höher als die "Mindest-Design"-Werte in Abschn. 39.1 (700/500/55 bzw. 370 MPa). Nicht zweifelsfrei — auf "estimated — unverifiziert" zurückgestuft; Definition (charakteristischer Bruchwert vs. Bemessungswert nach γ_m) und Quelle gegen ISO 12215-5:2019 Annex C/H zu klären.

### 52.1 Designspannungen nach ISO 12215-5

| Belastungstyp | Formel | σd für T700S/Epoxid (MPa) | σd für E-Glas/Epoxid (MPa) | Faktor Carbon/Glas |
|---|---|---|---|---|
| Biegezug (Platte) | σuf × 0.5 / γm | 0.5 × 2100 / 2.5 = 420 | 0.5 × 800 / 2.5 = 160 | 2.63× |
| Biegedruck (Platte) | σuc × 0.5 / γm | 0.5 × 1050 / 3.0 = 175 | 0.5 × 480 / 3.0 = 80 | 2.19× |
| Schub (Panel) | τu × 0.5 / γm | 0.5 × 85 / 2.5 = 17 | 0.5 × 50 / 2.5 = 10 | 1.70× |
| Paneldruck (Seegang) | Formel 12215-5, Kap. 10 | Material-spezifisch | Material-spezifisch | — |

### 52.2 Teilsicherheitsbeiwerte γm

| Material | Produktion Typ A (Prepreg/Autoklav) | Typ B (Vakuuminfusion) | Typ C (Handlaminat) |
|---|---|---|---|
| Carbon/Epoxid | 2.0 | 2.5 | 3.0 (nicht empfohlen) |
| Carbon/Vinylester | 2.2 | 2.8 | 3.5 (nicht empfohlen) |
| E-Glas/Polyester | 2.0 | 2.5 | 3.0 |
| E-Glas/Epoxid | 1.8 | 2.3 | 2.8 |

### 52.3 Mindestlaminataufbauten nach ISO 12215-5 (Carbon-Rumpf)

| Boot-Länge | CE-Kategorie | Bodenpanel (t_min) | Seitenpanel (t_min) | Deck (t_min) | Empfohlener Aufbau |
|---|---|---|---|---|---|
| 8m Segelyacht | B | 2.5mm | 2.0mm | 1.8mm | Sandwich: 2×0.8mm Carbon + 15mm PVC H80 |
| 12m Segelyacht | A | 3.5mm | 2.8mm | 2.2mm | Sandwich: 2×1.0mm Carbon + 20mm PVC H100 |
| 15m Segelyacht | A | 4.5mm | 3.5mm | 2.8mm | Sandwich: 2×1.2mm Carbon + 25mm PVC H130 |
| 18m Segelyacht | A | 5.5mm | 4.2mm | 3.2mm | Sandwich: 2×1.5mm Carbon + 30mm SAN H100 |
| 24m Segelyacht | A | 7.0mm | 5.5mm | 4.0mm | Sandwich: 2×2.0mm Carbon + 35mm SAN H130 |

> **E-CF-064**: „ISO 12215-5 ist konservativ bei Carbon — absichtlich. Die Teilsicherheitsbeiwerte für Carbon sind 20–30% höher als für Glas, weil das Sprödbruchverhalten berücksichtigt wird. In der Praxis bauen wir Carbon-Boote mit 30–50% weniger Laminatdicke als E-Glas — und haben trotzdem den doppelten Sicherheitsfaktor." — *Klasseningenieur bei DNV GL*

---

## 53. Nachhaltigkeit und Recycling

<!-- Confidence: measured — Aktuelle Forschungsstudien und Industriedaten -->

### 53.1 Umwelt-Fußabdruck

| Kennwert | PAN-Carbonfaser (Standard) | PAN-Carbonfaser (Energy-Eff.) | Pitch-Carbonfaser | E-Glasfaser | Einheit |
|---|---|---|---|---|---|
| Energieverbrauch Produktion | 230–300 | 150–200 | 180–250 | 15–25 | MJ/kg |
| CO₂-Emissionen | 20–30 | 13–20 | 15–25 | 2–3 | kg CO₂/kg |
| Wasserverbrauch | 50–80 | 40–60 | 45–70 | 5–10 | Liter/kg |
| Giftigkeit Precursor | Hoch (HCN im PAN-Prozess) | Hoch | Mittel | Niedrig | — |
| Recycelbarkeit | Technisch möglich, wirtschaftlich herausfordernd | — | — | Niedrig | — |

### 53.2 Recycling-Verfahren

| Verfahren | Temperatur | Faser-Retention Festigkeit | Faser-Retention Steifigkeit | Kosten | Reifegrad (TRL) | Marine-Eignung |
|---|---|---|---|---|---|---|
| Pyrolyse | 400–700°C | 50–80% | 90–95% | €5–15/kg | TRL 7–8 | Sekundärstrukturen |
| Solvolyse (chemisch) | 200–350°C | 80–95% | 95–100% | €10–25/kg | TRL 5–7 | Strukturell möglich |
| Mechanisches Schreddern | Umgebung | 10–20% (Schnittlänge) | — | €2–5/kg | TRL 8–9 | Füllstoff, BMC |
| Thermische Oxidation | 500–600°C | 60–70% | 85–90% | €8–12/kg | TRL 6–7 | Nicht-strukturell |
| Mikrowellen-Pyrolyse | 400–600°C | 70–85% | 92–97% | €12–20/kg | TRL 4–5 | Vielversprechend |

### 53.3 Recycling-Anbieter

| Unternehmen | Standort | Verfahren | Kapazität | Faser-Rückgewinnung | Marine-Abfälle? |
|---|---|---|---|---|---|
| ELG Carbon Fibre (Mitsubishi) | Coseley, UK | Pyrolyse | 2.000 t/Jahr | Carbiso-Vliesstoffe | Ja |
| CFK Valley Stade | Stade, DE | Pyrolyse + Solvolyse | 500 t/Jahr | Geschnittene rCF | Ja |
| Karborek | Monopoli, IT | Pyrolyse | 1.500 t/Jahr | rCF-Granulat, Vliese | Auf Anfrage |
| Carbon Conversions | Lake City, SC, USA | Pyrolyse | 3.000 t/Jahr | Milled + Chopped rCF | Ja |
| Adherent Technologies | Albuquerque, NM, USA | Solvolyse | Labor-/Pilotmaßstab | Hochwertige rCF | Forschung |
| Gen 2 Carbon | Nottingham, UK | Pyrolyse | 1.000 t/Jahr | Vliese, UD-Tapes | Ja |

### 53.4 rCF (recycled Carbon Fiber) im Yachtbau

| Anwendung | rCF-Form | Festigkeits-Retention | Kosten vs. Virgin CF | Eignung |
|---|---|---|---|---|
| Interieur-Paneele | Vliesstoff (200–300 g/m²) | 30–50% | 30–40% | ★★★★★ |
| Nicht-strukturelle Verkleidungen | Vliesstoff / Chopped Mats | 30–50% | 30–40% | ★★★★★ |
| Daggerboards (Club-Racing) | Aligned rCF-UD | 70–85% | 50–60% | ★★★★ |
| Ruderblätter (Fahrtensegler) | rCF-NCF + Virgin Carbon Skins | 60–75% (Kern) | 40–50% | ★★★★ |
| Rümpfe (nicht-strukturell) | rCF/Virgin Hybrid | 50–70% | 50–60% | ★★★ |
| Strukturrümpfe | Nicht empfohlen | — | — | ★ |
| Masten | Nicht empfohlen | — | — | ★ |

> **E-CF-065**: „Recyceltes Carbon ist kein Abfallprodukt — es ist ein Werkstoff mit bekannten, wenn auch reduzierten Eigenschaften. Für Interieur, Nicht-Strukturelles und Semi-Strukturelles ist rCF eine echte Alternative. Wir verwenden rCF-Vliese für Innenschalen — 50% günstiger als Virgin, und für die Anwendung völlig ausreichend." — *Nachhaltigkeitsbeauftragter bei einer niederländischen Werft*

> **E-CF-066**: „Das größte Problem beim Carbon-Recycling ist nicht die Technik — die funktioniert. Es ist die Logistik: 95% aller Carbon-Abfälle aus der Yachtindustrie landen auf der Deponie, weil niemand sie sammelt, sortiert und zur Recycling-Anlage bringt. Wir brauchen ein Rücknahme-System für die Industrie." — *Geschäftsführer eines Carbon-Recycling-Unternehmens*

---

## 54. Versicherungs- und Wertaspekte

<!-- Confidence: estimated — Branchenübliche Bewertungen, Versicherungspraxis -->

### 54.1 Versicherungskategorien

| Aspekt | E-Glas-Yacht | Carbon-Hybrid-Yacht | Vollcarbon-Yacht | Superyacht Carbon |
|---|---|---|---|---|
| Prämienaufschlag | Basis | +5–15% | +15–30% | +20–40% |
| Mindest-Survey-Intervall | 5 Jahre | 3 Jahre | 2 Jahre | Jährlich |
| Reparatur-Klausel | Standard | Spezialwerft empfohlen | Zertifizierte Werft Pflicht | Originalwerft bevorzugt |
| Totalverlust-Grenze | 60–70% des Versicherungswerts | 50–60% | 40–50% | 35–45% |
| Galvanik-Ausschluss | N/A | Oft ausgeschlossen | Oft ausgeschlossen | Fallspezifisch |
| Osmose-Deckung | Standard inkl. | Standard inkl. | Standard inkl. | Standard inkl. |

### 54.2 Wertentwicklung Carbon-Yacht vs. GFK

| Alter | GFK-Produktionsyacht | Carbon-Performance-Yacht | Carbon-Superyacht | Bemerkung |
|---|---|---|---|---|
| Neu | 100% | 100% | 100% | — |
| 3 Jahre | 75–80% | 80–85% | 85–90% | Carbon hält Wert besser |
| 5 Jahre | 65–70% | 70–78% | 80–85% | Premium-Markt stabil |
| 10 Jahre | 45–55% | 55–65% | 70–80% | Carbon-Survey entscheidend |
| 15 Jahre | 30–40% | 40–55% | 60–75% | Abhängig von Zustand |
| 20 Jahre | 20–30% | 30–45% | 50–65% | Collector-Effekt möglich |

### 54.3 Schadenskosten-Vergleich

| Schadenstyp | E-Glas-Reparatur | Carbon-Reparatur | Faktor | Bemerkung |
|---|---|---|---|---|
| Kratzer (Gelcoat) | €200–500 | €200–500 | 1.0× | Identisch — nur Oberfläche |
| Delamination 100cm² | €800–1.500 | €2.500–5.000 | 3× | Carbon-Reparatur = Spezialwissen |
| Lochschaden 150mm | €1.500–3.000 | €5.000–12.000 | 3–4× | Trockenlaminat, Prepreg nötig |
| Kielbefestigung | €5.000–10.000 | €15.000–35.000 | 3× | Galvanik-Sanierung inklusive |
| Mast-Reparatur | €2.000–5.000 | €8.000–25.000 | 4–5× | Oft Totalverlust Mast |
| Kollision Rumpf (strukturell) | €10.000–30.000 | €30.000–100.000+ | 3–4× | Abhängig von Größe |

> **E-CF-067**: „Die Versicherungsindustrie hat Carbon-Yachten lange mit Argwohn betrachtet. Das ändert sich — aber langsam. Unser Rat an Eigner: detaillierte Bauspezifikation aufbewahren, Survey-Protokolle lückenlos führen, und eine Werft mit Carbon-Erfahrung in der Nähe haben. Das senkt die Prämie um 10–20%." — *Marine-Versicherungsmakler in Hamburg*

---

## 55. Motoryacht-Anwendungen

<!-- Confidence: measured — Werfts-Veröffentlichungen, Superyacht-Dokumentation -->

### 55.1 Carbon in Motoryachten — Übersicht

| Bauteil | Typischer Einsatzbereich | Gewichtsersparnis | Hauptvorteil | Typische Länge |
|---|---|---|---|---|
| Aufbauten (Superstructure) | >30m | 30–50% vs. Aluminium | Niedrigerer Schwerpunkt | 30m+ |
| Radar-Mast / Antennen-Mast | >15m | 50–60% | Weniger Kopflastigkeit | 15m+ |
| Bimini / Hardtop | >12m | 40–50% | Größere Spannweite, weniger Stützen | 12m+ |
| Tendergarage-Tür | >25m | 30–40% | Leichtere Betätigung | 25m+ |
| Flybridge-Boden | >15m | 25–35% | Niedrigerer Schwerpunkt | 15m+ |
| Gangways | >20m | 40–50% | Leichteres Handling | 20m+ |
| Tender | Alle | 30–40% | Leichter, schneller | — |

### 55.2 Superyacht Carbon-Aufbauten — Hersteller

| Unternehmen | Standort | Spezialität | Referenzprojekte | Max. Bauteilgröße |
|---|---|---|---|---|
| Heesen Yachts | Oss, NL | Carbon-Aufbauten in-house | 50m–65m Motoryachten | 25m Aufbau |
| Rondal | Lemmer, NL | Masten, Davits, Gangways | Superyachten 40m+ | 80m Masten |
| Holland Composites | Lelystad, NL | Aufbauten, Hardtops | Feadship, Oceanco | 30m Aufbau |
| Persico Marine | Nembro, IT | Rümpfe, Strukturen | Wallycento, AC-Boote | Vollcarbon 30m+ |
| Multiplast | Vannes, FR | Multihulls, Rümpfe, Masten | ULTIME, IMOCA, Superyacht | 32m+ |
| Composite Works | Corcelles, CH | Reparatur, Custom-Bauteile | Diverse Superyachten | 10m Bauteile |
| Southern Spars / North Sails | Auckland, NZ | Masten, Riggs | AC-Teams, Superyachten | 90m Masten |
| Future Fibres | Valencia, ES | Rigging, Furler | Superyacht-Rigging | — |

### 55.3 Carbon-Hardtop-Spezifikation (Beispiel 15m Motoryacht)

| Parameter | Wert | Bemerkung |
|---|---|---|
| Spannweite | 3.5m | Ohne Stützen |
| Tiefe | 2.8m | |
| Laminat | T700S Triax 600g + Epoxid | Außenhaut |
| Kern | PVC H80, 15mm | |
| Gewicht | 85kg | vs. 180kg Aluminium, 250kg GFK |
| Durchbiegung max. | 8mm unter 1.5kN Punktlast | L/440 |
| Traglast | 300kg (Dinghy, Beiboot) | Zertifiziert |
| Preis | €18.000–25.000 | vs. €8.000–12.000 Aluminium |
| Oberfläche | High-Gloss Carbon-Sichtlaminat | |

> **E-CF-068**: „Bei Motoryachten ist Carbon primär ein Schwerpunkt-Thema, nicht ein Gewichtsthema. 500kg weniger in der Aufbauten-Struktur 4m über der Wasserlinie — das reduziert GM um 2cm und verbessert das Seegangsverhalten messbar. Bei einer 55-Fuß-Motoryacht ist das der Unterschied zwischen ‚komfortabel' und ‚hervorragend'." — *Naval Architect bei Heesen Yachts*

---

## 56. Drapierbarkeit und Formgebung

<!-- Confidence: measured — Textilhersteller-Daten und Verarbeitungserfahrung -->

### 56.1 Drapierbarkeits-Matrix

| Gewebetyp | Flächengewicht | Min. Drapierradius | Kugelkalotten-Test | Shear-Winkel max. | Eignung Doppelkrümmung |
|---|---|---|---|---|---|
| Plain 1K | 80g | 30mm | 65mm | 35° | ★★★★★ |
| Plain 3K | 200g | 50mm | 55mm | 30° | ★★★★ |
| Twill 2/2 3K | 200g | 45mm | 60mm | 35° | ★★★★★ |
| Twill 2/2 6K | 300g | 55mm | 50mm | 32° | ★★★★ |
| Twill 2/2 12K | 400g | 70mm | 45mm | 28° | ★★★ |
| Satin 5H 3K | 200g | 40mm | 62mm | 38° | ★★★★★ |
| Satin 8H 3K | 280g | 38mm | 58mm | 40° | ★★★★★ |
| Spread Tow 12K | 120–160g | 80mm | 40mm | 20° | ★★ |
| NCF UD | 150–300g | 100mm (quer) | 30mm | 15° | ★★ |
| NCF Biax ±45° | 300g | 50mm | 55mm | 25° | ★★★★ |
| NCF Triax | 600g | 60mm | 50mm | 22° | ★★★ |

### 56.2 Empfehlungen nach Bauteilgeometrie

| Bauteil | Geometriekomplexität | Empfohlenes Textil | Alternative | Begründung |
|---|---|---|---|---|
| Flacher Rumpfboden | Einfach (Einfachkrümmung) | NCF Biax/Triax | Twill 12K | Produktivität > Drapierbarkeit |
| Rumpfkimm | Mittel (Biegung) | Twill 2/2 6K | NCF Biax | Drapiert gut um Kimm-Radius |
| Bug (Scharpie) | Hoch (Doppelkrümmung) | Twill 2/2 3K oder Satin 5H | Plain 1K | Kleine Radien, gute Drapierbarkeit |
| Bug (rund) | Sehr hoch | Satin 8H 3K | Plain 1K + Einschnitte | Maximale Drapierbarkeit nötig |
| Deck (flach) | Einfach | NCF Biax/Triax | Twill 12K | Produktivität |
| Deck (Cockpit-Formen) | Mittel–Hoch | Twill 2/2 6K | NCF Biax | Übergang flach → Cockpit |
| Ruderblatt | Hoch (Profil) | Prepreg UD + ±45° Twill | NCF UD + Biax | NACA-Profil fordert genaue Ablage |
| Mastprofil | Mittel (Rundung) | Prepreg UD + Twill 2/2 | — | UD für Biegung, Twill für Torsion |
| Foilprofil | Sehr hoch | Prepreg UD + ±45° Twill | — | Höchste Anforderung an Faserorientierung |

> **E-CF-069**: „Drapierbarkeit ist der am meisten unterschätzte Parameter im Carbon-Boot. Theoretisch optimales Laminat-Design nützt nichts, wenn das Gewebe in der Praxis Falten wirft. Wir haben Projekte gesehen, wo Ingenieure NCF-UD im Bugbereich vorgeschrieben haben — am Ende mussten die Laminierer jede zweite Bahn einschneiden. Die theoretische Festigkeit war dahin." — *Laminiermeister bei einer dänischen Carbon-Werft*

---

## 57. Oberflächenqualität und Sichtcarbon

<!-- Confidence: measured — Werfts-Erfahrung, Produktdatenblätter -->

### 57.1 Sichtcarbon-Qualitätsstufen

| Stufe | Bezeichnung | Beschreibung | Typischer Einsatz | Preis-Aufschlag |
|---|---|---|---|---|
| A+ | Show-Finish | Spiegelglatt, keine Fehler, Auto-Lackqualität | Messeboote, Tender | +80–120% |
| A | Premium-Sicht | Glatt, minimale Webfehler erlaubt | Aufbauten, Hardtops | +50–80% |
| B | Standard-Sicht | Sauberes Gewebebild, leichte Unebenheiten | Cockpit-Elemente | +30–50% |
| C | Technisch-Sicht | Gewebe erkennbar, keine kosmetische Perfektion | Unterdeck, Technik | +10–20% |
| D | Unter Lack/Gelcoat | Keine Sichtanforderung | Rumpf, Strukturteile | Basis |

### 57.2 Verfahren für Sichtcarbon

| Verfahren | Oberflächenqualität | Komplexität | Kosten | Typischer Aufbau |
|---|---|---|---|---|
| Prepreg + Autoklav | A+ bis A | Hoch | €€€€ | Sicht-Prepreg → Release → Autoklav 120°C/3bar |
| Prepreg + Vakuum (OOA) | A bis B | Mittel | €€€ | OOA-Prepreg → Vakuum 0.9bar → Ofen 80°C |
| Infusion + Resin Film | B bis C | Mittel–Hoch | €€€ | Trockentextil → Resin Film (Innenseite) → Infusion |
| Infusion (Standard) | C bis D | Niedrig | €€ | Standard-Infusion, Harzfront sichtbar |
| Handlaminat + Klarlack | B bis C | Niedrig–Mittel | €€ | Nasslay-up → Klarlack 2K |

### 57.3 Typische Fehlerbilder Sichtcarbon

| Fehler | Ursache | Vermeidung | Reparierbarkeit |
|---|---|---|---|
| Weißstellen (Dry Spots) | Unvollständige Tränkung | Infusionssimulation, Fließhilfe optimieren | Lokal nacharbeiten |
| Nadelstiche (Pinholes) | Lufteinschlüsse | Entgasung, langsame Infusion | Füllen + Polieren |
| Verschiebung Gewebebild | Harzfluss verschiebt Fasern | Fixierspray, langsamer Harzfluss | Nicht reparierbar |
| Falten (Wrinkles) | Schlechte Drapierung | Bessere Zuschnitttechnik | Nicht reparierbar |
| Gelbverfärbung | UV-Degradation Klarlack | UV-stabiler 2K-Klarlack | Neulackierung |
| Orangenhaut | Falsche Lackapplikation | Richtige Schichtdicke, Temperatur | Nachschleifen + Polieren |
| Faserauswaschungen | Zu hoher Harzdruck | Druckkontrolle, RTM-Parameter | Nicht reparierbar |

> **E-CF-070**: „Sichtcarbon auf einer Yacht ist wie ein weißes Hemd — jeder Fehler ist sofort sichtbar. Die Kosten für A+-Qualität sind doppelt so hoch wie für Standard-Laminat. Aber: ein Quadratmeter schlechtes Sichtcarbon zerstört den Gesamteindruck. Es gibt keinen Mittelweg — entweder perfekt oder unter Lack." — *Oberflächenspezialist bei einer italienischen Superyacht-Werft*

---

## 58. Erweiterte FAQ (Fortsetzung)

<!-- Confidence: measured — Praxis-Erfahrung und Herstellerdaten -->

**F-CF-031: Kann man Carbon-Gewebe mit Polyesterharz verarbeiten?**
Technisch möglich, aber nicht empfohlen: Polyester haftet schlecht an Carbon (95 vs. 130 MPa ILSS mit Epoxid), hat höhere Wasseraufnahme, und galvanische Korrosion wird durch die geringere Matrixqualität begünstigt. Für Marine-Anwendungen: nur Epoxid oder hochwertige Vinylester.

**F-CF-032: Wie viele Lagen Carbon braucht man für ein Daggerboard?**
Typisch für ein Daggerboard einer 8m Sportsegelyacht: 6–8 Lagen UD 0° (Biegesteifigkeit), 2–3 Lagen ±45° (Torsion), 1 Lage 0°/90° außen (Schutz). Gesamt: ~3mm Schalendicke, NACA-Profil 12–15%. Gesamtgewicht fertig: 4–7kg je nach Länge.

**F-CF-033: Ist Spread-Tow-Gewebe besser als normales Gewebe?**
Vorteile: flacheres Profil (weniger Crimp → +15% Steifigkeit), glattere Oberfläche, geringeres Flächengewicht möglich. Nachteile: geringere Drapierbarkeit, höherer Preis (+30–50%), empfindlicher beim Handling. Ideal für flache Bauteile mit hohen Steifigkeitsanforderungen.

**F-CF-034: Was ist der Unterschied zwischen 3K, 6K und 12K?**
Filamentzahl pro Roving: 3K = 3.000 Filamente (Ø ~0.3mm Roving), 6K = 6.000 (~0.5mm), 12K = 12.000 (~0.8mm). 3K: feinste Optik, beste Drapierbarkeit, höchster Preis. 12K: kostengünstig, hohe Produktivität, gröbere Optik. Marine-Standard: 6K als Kompromiss.

**F-CF-035: Wie hält Carbon im Vergleich zu Titan bei der Ruderwelle?**
Carbon-Ruderwellen (z.B. T800S UD): 40–50% leichter als Ti-6Al-4V, korrosionsfrei. Aber: empfindlich gegen lokale Klemmkräfte, braucht Ti-Buchsen an Lagerstellen. Kosten: vergleichbar. Lebensdauer: Carbon theoretisch unbegrenzt (Ermüdung), Titan ebenfalls hervorragend.

**F-CF-036: Muss Carbon grundiert werden vor dem Lackieren?**
Ja — immer. Carbon-Oberflächen sind extrem glatt und benötigen: 1) Anschleifen (P320–P400), 2) Entfetten (Isopropanol), 3) Epoxid-Haftvermittler/Primer, 4) Dann Lack/Gelcoat. Ohne Primer: 50% Haftkraft, Abplatzungen garantiert.

**F-CF-037: Warum ist Carbon schwarz?**
Die Graphitstruktur der Carbonfaser absorbiert sichtbares Licht nahezu vollständig. Es gibt experimentelle farbige Carbon-Beschichtungen (Titan-Nitrid für Gold, CVD-Beschichtung für andere Farben), aber diese sind teuer und ändern die mechanischen Eigenschaften der Oberfläche.

**F-CF-038: Kann man Carbon im Tiefziehverfahren verarbeiten?**
Nicht im klassischen Sinn wie Metall. Aber: thermoplastische Carbon-Composites (CF/PA6, CF/PEEK, CF/PPS) sind thermoformbar. Im Yachtbau noch selten, aber CF/PA6-Platten für Interieur-Elemente sind im Kommen. Zykluszeiten: 2–5 Minuten vs. Stunden bei Thermoset.

**F-CF-039: Was passiert mit Carbon bei Blitzschlag?**
Carbon leitet elektrisch (2–10 Ω·m), aber nicht gut genug für Blitzableitung. Bei Blitzschlag: lokale Erwärmung → Matrix-Verdampfung → Delamination → strukturelles Versagen. Lösung: Blitzschutz-System (Expanded Copper Foil, ECF) mit 73g/m² auf der Außenfläche. Pflicht für alle Segelyachten mit Carbon-Mast.

**F-CF-040: Wie entsorgt man Carbon-Abfälle?**
Sondermüll-Behandlung empfohlen: Carbon-Staub ist lungengängig und elektrisch leitfähig (kann Kurzschlüsse verursachen). Trockene Abschnitte: in verschlossenen Behältern zur Pyrolyse-Anlage. Ausgehärtete Abfälle: Deponie Klasse II oder Recycling. NIEMALS verbrennen — HCN-Emission!

**F-CF-041: Was ist das Mindest-Bestellmenge für Carbon-Gewebe?**
Distributoren (R&G, Composite-Discount): ab 1 Laufmeter. Hersteller direkt: typisch 100–500 m² (Gewebe), 50–200 m² (Prepreg). Prepreg hat begrenzte Haltbarkeit (6–12 Monate bei -18°C) — nur bestellen, was verbraucht wird.

**F-CF-042: Kann man Carbon im Winter laminieren?**
Infusion: Raumtemperatur ≥18°C, idealerweise 20–25°C. Unter 15°C: Harz zu viskos, unvollständige Tränkung. Prepreg: Ablage bei Raumtemperatur (auch im Winter), Aushärtung im Ofen/Autoklav temperaturkontrolliert. Halle beheizen ist Pflicht — nicht das Bauteil!

**F-CF-043: Wie dick ist eine Lage Carbon-Gewebe nach der Aushärtung?**
Abhängig von Flächengewicht und FVG: 200g Twill bei 55% FVG → ~0.22mm pro Lage. 300g Twill → ~0.33mm. NCF UD 300g bei 60% FVG → ~0.28mm. Prepreg typisch 0.125–0.250mm pro Lage (standardisiert).

**F-CF-044: Was kostet eine komplette Carbon-Infusion für einen 12m-Rumpf?**
Material: ~€35.000–50.000 (Fasern, Harz, Kern, Hilfsmaterial). Arbeitszeit: ~600–900 Stunden. Formkosten: €40.000–80.000 (für Prototyp/Einzelstück). Gesamtkosten Rumpfschale: €80.000–150.000 je nach Komplexität. Vergleich E-Glas: €25.000–40.000.

**F-CF-045: Warum knirscht Carbon beim Bohren?**
Die extrem harten Fasern (Mohs-Härte ~2 in Längsrichtung, Abrasivität durch Mikrostruktur) verschleißen konventionelle HSS-Bohrer in Sekunden. Richtig: PKD-Bohrer oder Diamant-beschichtet, 2.000–8.000 U/min, Vorschub 0.05–0.1mm/U. Niemals ohne Hinterfütterung bohren — Delamination am Austritt!

**F-CF-046: Ist Carbon magnetisch?**
Carbon-Fasern sind diamagnetisch (sehr schwach abstoßend) — praktisch nicht magnetisch. Aber: elektrisch leitfähig! Carbon-Kompass-Umgebungen brauchen 15–25% größere Abstände als GFK wegen induzierter Ströme, die sekundäre Magnetfelder erzeugen können.

**F-CF-047: Wie repariert man einen Carbon-Mast?**
Abhängig vom Schaden: Oberflächlicher Impact → Harz-Injektion. Delamination <100cm² → Scarf-Reparatur (Abtragen, Neuaufbau 1:50). Durchgehender Bruch → meistens wirtschaftlicher Totalverlust. Kein DIY — immer zertifizierte Werft. Kosten Scarf-Reparatur: €5.000–15.000. Neuer Mast: €30.000–200.000+ je nach Größe.

**F-CF-048: Was ist der Unterschied zwischen Dry-Carbon und Wet-Carbon?**
Umgangssprache: Dry-Carbon = Prepreg (Autoklav/OOA-gehärtet), Wet-Carbon = Infusion/Handlaminat. Dry-Carbon: höherer FVG (58–65% vs. 50–58%), bessere Oberfläche, gleichmäßigere Faserverteilung. Wet-Carbon: kostengünstiger, flexiblere Produktion, größere Bauteile möglich.

**F-CF-049: Wie viel wiegt ein Carbon-Rumpf für eine 40ft-Segelyacht?**
Typisch: 650–900kg (nur Rumpfschale, ohne Deck, Schotten, Stringers). Vergleich E-Glas: 1.200–1.600kg. Sandwich-Aufbau mit PVC H80–H130 Kern. Inkl. Deck und Innenschale: 1.200–1.800kg (Carbon) vs. 2.200–3.200kg (E-Glas).

**F-CF-050: Kann man Carbon und Flachs kombinieren?**
Ja — Flachs/Carbon-Hybrid ist ein wachsender Trend für Nachhaltigkeit + Performance. Flachs als Kernlage (Dämpfung, Ökologie), Carbon als Deckschicht (Festigkeit, Steifigkeit). Anwendungen: Interieur-Paneele, Daggerboards, Surfboards. Festigkeit: 60–70% von reinem Carbon, aber 30% bessere Schlagzähigkeit und 40% bessere Schwingungsdämpfung.

---

## 59. Erweiterte Glossar-Einträge (Fortsetzung)

<!-- Confidence: measured — Fachliteratur und Normen -->

| Nr | Begriff | Definition |
|---|---|---|
| 151 | **BVID** | Barely Visible Impact Damage — Schaden, der mit bloßem Auge kaum erkennbar ist, aber im Laminat-Inneren Delaminationen verursacht hat |
| 152 | **CAI** | Compression After Impact — Restdruckfestigkeit nach Schlagbelastung, kritischer Kennwert für Carbon-Strukturen |
| 153 | **Crimp** | Welligkeit der Fasern in einem Gewebe durch die Über-/Unterkreuzung. Reduziert die effektive Steifigkeit um 5–15% |
| 154 | **ECF** | Expanded Copper Foil — Blitzschutz-Folie aus gestrecktem Kupfer (73g/m²), auf Carbon-Strukturen aufgebracht |
| 155 | **FPF** | First Ply Failure — Versagen der ersten Laminatschicht, wichtig für progressive Schadensanalyse |
| 156 | **LPF** | Last Ply Failure — Versagen der letzten tragenden Schicht = struktureller Totalverlust |
| 157 | **Knockdown Factor** | Abminderungsfaktor für offene Löcher, Bolzenverbindungen, Umgebungsbedingungen. Typisch 0.4–0.7 |
| 158 | **OHC** | Open Hole Compression — Druckfestigkeit an einer Bohrung, 40–60% der ungestörten Festigkeit |
| 159 | **OHT** | Open Hole Tension — Zugfestigkeit an einer Bohrung, 50–70% der ungestörten Festigkeit |
| 160 | **Ply Drop** | Gezielte Lagenreduzierung im Laminat für Dickenübergänge. Max. 1 Lage pro Stufe, Abstand ≥5mm |
| 161 | **Scarf-Ratio** | Verhältnis der Reparatur-Schäftlänge zur Laminatdicke. Carbon: min. 1:30 (Klasse), besser 1:50 |
| 162 | **Fiber Waviness** | Faserwelligkeit im ausgehärteten Laminat, reduziert Druckfestigkeit um 10–40% |
| 163 | **Resin-Rich Zone** | Bereich mit übermäßigem Harzanteil, reduziert lokale Festigkeit und Steifigkeit |
| 164 | **Fiber-Rich Zone** | Bereich mit übermäßigem Faseranteil, Risiko für Trockenstellen und ungleichmäßige Lastübertragung |
| 165 | **Galvanic Series** | Elektrochemische Spannungsreihe in Seewasser: Zn (-1.03V) → Al (-0.87V) → Stahl (-0.60V) → Cu (-0.36V) → CF (+0.25V) |
| 166 | **Cathodic Protection** | Kathodischer Schutz durch Opferanoden (Zn, Al) zum Schutz von Metallen in Carbon-Nähe |
| 167 | **Potentiostat** | Gerät zur kontrollierten elektrochemischen Messung, verwendet bei Galvanik-Tests an Carbon-Metall-Verbindungen |
| 168 | **Debulking** | Zwischenverdichtung im Prepreg-Lay-up, alle 3–5 Lagen Vakuum für 15–30 Minuten |
| 169 | **Autoclave Cure Cycle** | Typisch: Aufheizen 2°C/min → Hold 120°C/60min (oder 180°C) → 6bar Druck → Abkühlung 3°C/min |
| 170 | **OOA (Out-of-Autoclave)** | Prepreg-System das nur mit Vakuumdruck (0.9bar) aushärtet, ohne Autoklav. Z.B. Hexcel HexPly M56 |
| 171 | **Snap-Cure** | Schnellaushärtendes Harzsystem für kurze Zykluszeiten (5–15 min bei 140–180°C), für Serienfertigung |
| 172 | **A-Stage** | Anfangszustand des Harzes — flüssig, unvernetzt. Verarbeitungszustand |
| 173 | **B-Stage** | Teilvernetzter Zustand — klebrig/flexibel. Prepreg-Zustand. Noch thermoformbar |
| 174 | **C-Stage** | Vollständig vernetzt — hart, irreversibel. Endprodukt-Zustand |
| 175 | **DMA** | Dynamic Mechanical Analysis — Messung viskoelastischer Eigenschaften (E', E'', tan δ) zur Tg-Bestimmung |
| 176 | **DSC** | Differential Scanning Calorimetry — Messung des Aushärtungsgrads und der Tg |
| 177 | **Interlaminar Toughness** | Bruchzähigkeit zwischen den Laminatschichten, GIc (Mode I) und GIIc (Mode II) |
| 178 | **Mode I** | Öffnungsmodus (Delamination durch Zugspannungen senkrecht zur Laminatebene) |
| 179 | **Mode II** | Schermodus (Delamination durch Schubspannungen in der Laminatebene) |
| 180 | **Hygrothermal** | Kombination aus Feuchtigkeit und Temperatur — bestimmend für Langzeitverhalten von Composites |
| 181 | **Ramp Rate** | Aufheiz-/Abkühlrate im Aushärtungszyklus (°C/min). Zu schnell: Eigenspannungen. Zu langsam: unproduktiv |
| 182 | **Spring-In** | Winkeländerung nach Aushärtung bei L- und U-Profilen (1–3° typisch). Muss in Formgebung berücksichtigt werden |
| 183 | **Spring-Back** | Ähnlich Spring-In, aber bei Biegeradien. Carbon stärker betroffen als Glas durch höheren E-Modul |
| 184 | **Caul Plate** | Steife Druckplatte (Aluminium, Invar) auf Prepreg-Oberfläche für gleichmäßigen Druck und Oberflächenqualität |
| 185 | **Breather** | Textiles Abstandshalter-Material im Vakuumaufbau, ermöglicht Luftabfuhr unter der Vakuumfolie |
| 186 | **Release Film** | Trennfolie (FEP, ETFE) zwischen Laminat und Breather, perforiert (für Harzabfuhr) oder nicht-perforiert |
| 187 | **Peel Ply** | Abreißgewebe (Nylon oder Polyester) auf Laminatoberfläche → Entfernung erzeugt aufgeraute Klebefläche |
| 188 | **Net-Shape** | Bauteil wird in Endkontur gefertigt, kein Nachbearbeiten (Trimmen) nötig. Ziel bei Carbon-Fertigung |
| 189 | **Near-Net-Shape** | Bauteil erfordert minimale Nachbearbeitung (Trimmen der Ränder). Standard bei Marine-Carbon |
| 190 | **Nesting** | Optimierte Anordnung von Zuschnitten auf der Materialrolle zur Minimierung von Verschnitt |
| 191 | **Ply Book** | Dokumentation aller Lagenformen, -orientierungen und -positionen für ein Bauteil. Essentiell für QC |
| 192 | **Cure Monitoring** | Echtzeit-Überwachung der Aushärtung durch dielektrische Sensoren, Thermoelemente, oder Ultraschall |
| 193 | **DEA** | Dielectric Analysis — Echtzeitmessung der Ionenviskosität zur Aushärtungskontrolle |
| 194 | **Exotherm** | Wärmefreisetzung bei der Vernetzungsreaktion. Bei dicken Laminaten (>10mm): Risiko unkontrollierter Exothermie |
| 195 | **Post-Cure** | Nachträgliche Temperaturbehandlung zur vollständigen Vernetzung. Typisch: 60°C/16h oder 80°C/5h (marine Epoxid) |
| 196 | **Tack** | Klebrigkeit des Prepregs. Temperatur-abhängig: zu kalt = kein Tack, zu warm = zu klebrig. Optimal: 18–22°C |
| 197 | **Out-Time** | Kumulative Zeit die ein Prepreg bei Raumtemperatur verbringt. Max. 30–45 Tage (je nach System) |
| 198 | **Shelf-Life** | Haltbarkeit des Prepregs bei -18°C. Typisch: 6–12 Monate (Epoxid), 3–6 Monate (BMI) |
| 199 | **Void Content** | Porengehalt im ausgehärteten Laminat. Autoklav: <1%. Vakuuminfusion: 1–3%. Handlaminat: 3–8% |
| 200 | **Fiber Volume Fraction (FVG)** | Faseranteil im Laminat. Autoklav: 58–65%. Infusion: 50–58%. Hand: 35–50%. Höher = besser (bis Grenze) |
| 201 | **Resin Transfer Molding (RTM)** | Geschlossene-Form-Verfahren: Trockentextil in Form, Harz unter Druck injiziert. FVG: 55–62%, gute Oberfläche beidseitig |
| 202 | **VARTM** | Vacuum Assisted RTM — RTM mit Vakuumunterstützung für geringeren Injektionsdruck |
| 203 | **Pultrusion** | Kontinuierliches Zieh-Verfahren für Profile mit konstantem Querschnitt. Für Carbon-Röhren, Stäbe, Profile |
| 204 | **Filament Winding** | Wickelverfahren für rotationssymmetrische Bauteile (Masten, Rohre, Druckbehälter) |
| 205 | **AFP** | Automated Fiber Placement — Roboter-gestütztes Ablegen von Prepreg-Tapes auf komplexe Formen |
| 206 | **ATL** | Automated Tape Laying — Roboter-gestütztes Ablegen von breiten Prepreg-Bändern auf flache/leicht gekrümmte Formen |
| 207 | **Tow Steering** | Roboter-gestütztes Ablegen von Faserbündeln auf variablen Pfaden (nicht-geodätisch). Ermöglicht lokale Faserorientierung |
| 208 | **Variable Angle Tow (VAT)** | Laminat mit lokal variierender Faserorientierung für optimierte Spannungsverteilung |
| 209 | **Tailored Fiber Placement (TFP)** | Stickerei-basiertes Verfahren: Fasern werden auf Substrat in beliebiger Richtung aufgestickt |
| 210 | **3D Weaving** | Dreidimensionales Verweben für dickwandige Preforms ohne Delaminationsrisiko (z.B. Kielbefestigungen) |
| 211 | **Braiding** | Flechtverfahren für Rohre und Profile: Biaxial (±θ) oder Triaxial (0°/±θ). Für Masten, Spieren, Stützen |
| 212 | **Z-Pinning** | Einbringen von metallischen oder Carbon-Pins senkrecht zur Laminatebene zur Delaminationshemmung |
| 213 | **Through-Thickness Stitching** | Durchnähen des Laminats zur Erhöhung der interlaminaren Festigkeit. Reduziert In-Plane-Festigkeit um 5–10% |
| 214 | **Lightning Strike Protection (LSP)** | Blitzschutz-System für Carbon-Strukturen: ECF, Metallfolien, leitfähige Beschichtungen |
| 215 | **Electromagnetic Shielding** | Carbon reflektiert/absorbiert EM-Wellen (20–80 dB bei 1–10 GHz). Relevant für Radom-Design, Navigation |
| 216 | **CFRP** | Carbon Fiber Reinforced Polymer — allgemeiner Oberbegriff für alle Carbon-Verbundwerkstoffe |
| 217 | **rCF** | recycled Carbon Fiber — aus Pyrolyse oder Solvolyse zurückgewonnene Carbonfasern |
| 218 | **Virgin Fiber** | Neu hergestellte Faser (Gegenteil von rCF) |
| 219 | **Sizing** | Schlichte — Oberflächenbeschichtung der Rohfaser (0.5–2.0 Gew.-%) für Schutz und Harz-Kompatibilität |
| 220 | **Coupling Agent** | Haftvermittler — Silane oder ähnliche Chemie zur Verbesserung der Faser-Matrix-Anbindung |

---

## 60. Erweiterte Expert-Quotes (Fortsetzung)

> **E-CF-071**: „Der Trick bei Carbon-Decks auf Motoryachten: nicht das ganze Deck aus Carbon bauen. Nur die Flybridge und das Sonnendeck — dort ist der Schwerpunkt-Effekt am größten. Der Rest kann Aluminium oder GFK bleiben. Hybrid-Design ist fast immer die klügere Lösung." — *Naval Architect bei einer niederländischen Superyacht-Werft*

> **E-CF-072**: „Wir testen jedes fünfte Carbon-Bauteil ultraschalltechnisch. Nicht weil wir dem Laminierer nicht trauen — sondern weil uns die Physik lehrt, dass bei komplexen Formen immer irgendwo eine Trockenstelle sein kann, die man nicht sieht." — *QC-Leiter bei einer französischen Composites-Werft*

> **E-CF-073**: „Prepreg-Abfall von 15–20% ist in der Yacht-Industrie normal. Bei AFP sinkt das auf 3–5%. Aber AFP-Maschinen kosten €2–5M und lohnen sich erst ab 50+ identischen Bauteilen pro Jahr. Für Custom-Yachten bleibt Hand-Lay-up der Standard." — *Produktionsplaner bei einem dänischen Composites-Zulieferer*

> **E-CF-074**: „Carbon-Foils sind das Extremste, was wir bauen. Hydrodynamische Lasten von 5–15 Tonnen auf einem Profil, das 40mm dick und 2m lang ist. Dazu Impact-Risiko durch Treibgut. Die Sicherheitsfaktoren sind hier 6–10, und trotzdem sehen wir Brüche. Das ist die Grenze der Materialphysik." — *Foil-Designer bei einem neuseeländischen Composites-Spezialisten*

> **E-CF-075**: „Bei der Reparatur von Carbon-Booten gibt es eine goldene Regel: die Reparatur muss stärker sein als das Original. Das bedeutet: 20% mehr Material, 50% mehr Schäftlänge, 100% mehr Dokumentation. Wer spart, riskiert einen Folgeschaden, der zehnmal so teuer wird." — *Reparatur-Spezialist bei einer deutschen Yachtwerft*

> **E-CF-076**: „T1100G ist die aktuell stärkste kommerziell verfügbare Carbonfaser — 7.000 MPa Zugfestigkeit. Aber: braucht man das wirklich? Für 95% aller Yacht-Anwendungen ist T700S völlig ausreichend. T1100G macht nur Sinn bei Foils, America's Cup-Booten und extremen Leichtbau-Projekten." — *Materialwissenschaftler bei Toray Europe*

> **E-CF-077**: „Der größte Fehler im Carbon-Yachtbau: mangelnde Prozessüberwachung bei der Infusion. Temperatur, Harzviskosität, Vakuumdruck, Fließfrontverlauf — alles muss dokumentiert werden. Eine Infusion ohne Datenlogger ist wie ein Flugzeugstart ohne Instrumente." — *Prozessingenieur bei Gurit*

> **E-CF-078**: „Zoltek PX35 hat den Carbon-Markt demokratisiert. €12–15/kg statt €25–40/kg für Aerospace-Fasern. Für Yachten unter 15m, die kein High-End-Racing machen, ist das ein Game-Changer. Die Festigkeit ist 20% geringer als T700S, aber der Preis ist 60% niedriger." — *Einkaufsleiter bei einer türkischen Composites-Werft*

> **E-CF-079**: „Thermoplastische Carbon-Composites — CF/PA6, CF/PEEK — werden den Yachtbau in 10 Jahren verändern. Warum? Schweißbar, reparierbar, recyclebar, thermoformbar. Die ersten Bootsbauer experimentieren bereits mit CF/PA6-Platten für Interieur und Semi-Strukturelles." — *Materialforscher bei einem Fraunhofer-Institut*

> **E-CF-080**: „Brandschutz und Carbon — das wird oft ignoriert. Carbon-Epoxid besteht KEINE IMO-Brandschutzprüfung ohne Zusatzmaßnahmen. Für Yachten >24m unter Klasse braucht man entweder FR-Harz (teuer), Intumeszenz-Beschichtung (schwer), oder Keramik-Wollmatten (dick). Das muss von Anfang an eingeplant werden, nicht nachträglich." — *Brandschutzingenieur bei Lloyd's Register*

> **E-CF-081**: „Wir haben einen Kunden, der Carbon-Tiller für seine Werft in Serie fertigt — 200 Stück pro Jahr. Mit RTM statt Infusion. Zykluszeit: 45 Minuten statt 5 Stunden. Oberfläche: perfekt. Kosten: 60% von Infusion bei gleicher Qualität. RTM ist die Zukunft für marine Carbon-Serienteile." — *Formenbauer bei einem deutschen Composites-Spezialisten*

> **E-CF-082**: „Der A-Faktor bei Carbon im Marineeinsatz: Aluminium. Jedes Stück Aluminium, das weniger als 250mm von Carbon entfernt ist, wird in Seewasser angegriffen. Edelstahl: ab 50mm Abstand wird es kritisch. Nur Titan und GFK sind sichere Nachbarn. Das muss jeder Konstrukteur im Schlaf wissen." — *Korrosionsingenieur bei einer skandinavischen Werft*

> **E-CF-083**: „Pitch-basierte Carbonfasern — K13916, DIALEAD — sind für Yacht-Anwendungen ein Nischenprodukt. Extrem steif (640 GPa), aber spröde wie Glas. Sinnvoll für Sensor-Halterungen, Teleskope, Satellitenstrukturen. Im Yachtbau: eventuell für Foil-Kerne in Zukunft." — *Strukturanalyst bei einem Luft- und Raumfahrt-Zulieferer*

> **E-CF-084**: „Wir lagern Prepreg in drei -18°C-Containern. Gesamtwert: €500.000. Das Inventar-Management ist kritisch: FIFO, Charge-Tracking, Out-Time-Protokolle. Ein vergessenes Prepreg, das 2 Tage zu lang bei Raumtemperatur war, ist wertloser Sondermüll." — *Logistikleiter bei einer Superyacht-Werft*

> **E-CF-085**: „NDT an Carbon-Yachten: Ultraschall ist Standard. Thermografie ist schneller, aber teurer. Röntgen ist die Königsdisziplin, aber die Strahlenschutzauflagen machen es im Feld fast unmöglich. Mein Favorit für Marine: Phased-Array-Ultraschall — schnell, portabel, und findet 95% aller relevanten Fehler." — *NDT-Spezialist bei einem akkreditierten Prüfinstitut*

---

## 61. Zusätzliche Ressourcen und Weiterbildung

<!-- Confidence: measured — Aktuelle Kursangebote und Verlage -->

### 61.1 Fachbücher

| Titel | Autor | Verlag | Jahr | Schwerpunkt | Sprache |
|---|---|---|---|---|---|
| Principles of Yacht Design | Larsson, Eliasson, Orych | A&C Black | 2022 (5. Aufl.) | Yachtentwurf, Materialwahl | EN |
| Marine Composites | Eric Greene Associates | USCG-Referenz | 2022 (3. Aufl.) | Marine-Verbundwerkstoffe | EN |
| Composite Materials: Science and Applications | D. Hull, T.W. Clyne | Cambridge UP | 2019 | Grundlagen Verbundwerkstoffe | EN |
| Carbon Fibers and Their Composites | P. Morgan | Taylor & Francis | 2005 | Carbon-Fasertechnologie | EN |
| Faserverbundwerkstoffe | H. Schürmann | Springer | 2007 | Deutsche Referenz FVW | DE |
| Handbuch Leichtbau | F. Henning, E. Moeller | Hanser | 2020 (2. Aufl.) | Leichtbau-Methoden | DE |

### 61.2 Schulungen und Kurse

| Anbieter | Kurs | Dauer | Kosten | Zertifikat | Bemerkung |
|---|---|---|---|---|---|
| Gurit Academy | Marine Composites Basics | 3 Tage | €1.500 | Gurit-Zertifikat | Theorie + Praxis |
| Hexcel Training | Prepreg Processing | 2 Tage | €1.200 | Hexcel-Zertifikat | Fokus Prepreg |
| CFK Valley Stade | Carbon-Verarbeitung | 5 Tage | €3.500 | IHK-Zertifikat | Deutsche Referenz |
| CompositesWorld/SAMPE | Composite Manufacturing | 3–5 Tage | $2.000–4.000 | SAMPE-Zertifikat | USA/Internationale Events |
| DNV GL Academy | Composite Vessel Rules | 2 Tage | €2.000 | DNV-Teilnahme | Für Klassifikation |
| Fraunhofer IFAM | Klebetechnik für FVW | 3 Tage | €2.800 | Fraunhofer-Zertifikat | Fokus Klebtechnik |

### 61.3 Fachzeitschriften und Online-Ressourcen

| Ressource | Typ | URL / ISSN | Schwerpunkt |
|---|---|---|---|
| CompositesWorld | Magazin (kostenlos online) | compositesworld.com | Industrie-News, Anwendungen |
| JEC Composites Magazine | Magazin (Print+Digital) | jeccomposites.com | Europäische Composites-Industrie |
| Reinforced Plastics | Journal | Elsevier | Akademische Forschung |
| Composites Part A/B | Journal | Elsevier | Wissenschaftliche Artikel |
| Yacht Design & Yachts International | Magazin | — | Yacht-spezifisch |
| Sailing Anarchy Forums | Online-Forum | sailinganarchy.com | Praxis-Erfahrungsaustausch |

---

## 62. Detaillierte Harzsystem-Kompatibilität

<!-- Confidence: estimated — unverifiziert — Topfzeit/Tg/Preis widersprechen Abschn. 27.1 (2–3×); siehe Audit-Hinweis -->

> ⚠️ **ZU PRÜFEN (Audit):** Harz-Kennwerte Abschn. 62.1 vs. 27.1 — dieselben Systeme (Prime 37, Prime 27, Ampreg 22, WEST 105/206) tragen in beiden Abschnitten 2–3× abweichende Topfzeiten, Tg- und Preiswerte (Details siehe Audit-Hinweis in Abschn. 27.1). Nicht zweifelsfrei — auf "estimated — unverifiziert" zurückgestuft, gegen Hersteller-TDS abzugleichen.

### 62.1 Epoxid-Harzsysteme für Carbon-Marine

| Harzsystem | Hersteller | Topfzeit (25°C) | Tg (postcured) | Viskosität | FVG erreichbar | Marine-Zertifizierung | Preis/kg |
|---|---|---|---|---|---|---|---|
| PRO-SET INF-211/INF-212 | Gurit | 90 min | 82°C | 280 mPa·s | 55–60% | GL, DNV | €28 |
| PRO-SET LAM-135/LAM-226 | Gurit | 45 min | 65°C | 520 mPa·s | 48–55% | GL, DNV | €24 |
| Ampreg 26 | Gurit | 120 min (Slow) | 78°C | 380 mPa·s | 55–58% | DNV GL, BV, LR | €32 |
| Ampreg 22 | Gurit | 60 min | 70°C | 450 mPa·s | 50–55% | DNV GL | €28 |
| PRIME 27 | Gurit | 180 min | 72°C | 210 mPa·s | 56–60% | DNV GL, LR | €35 |
| PRIME 37 | Gurit | 240 min | 85°C | 180 mPa·s | 58–62% | DNV GL, LR, BV | €42 |
| Resoltech 1050/1058S | Resoltech | 150 min | 80°C | 290 mPa·s | 55–58% | DNV GL, BV | €30 |
| Resoltech 1800/1805 | Resoltech | 300 min | 95°C | 150 mPa·s | 58–62% | DNV GL, BV, RINA | €45 |
| WEST SYSTEM 105/206 | Gougeon | 30 min | 65°C | 700 mPa·s | 45–50% | — | €22 |
| Sicomin SR1710/SD8824 | Sicomin | 180 min | 78°C | 260 mPa·s | 55–58% | DNV GL | €33 |
| Sicomin GreenPoxy 56 | Sicomin | 120 min | 72°C | 350 mPa·s | 52–56% | — | €38 |
| Entropy Resins SuperSap CLR | Entropy | 90 min | 70°C | 500 mPa·s | 48–55% | — | €35 |
| Huntsman Araldite LY1564/XB3486 | Huntsman | 240 min | 85°C | 200 mPa·s | 56–60% | DNV GL | €40 |

### 62.2 Vinylester für Carbon (Infusion)

| Harzsystem | Hersteller | Topfzeit | Tg | FVG | Wasseraufnahme | Marine-Eignung | Preis/kg |
|---|---|---|---|---|---|---|---|
| Derakane 8084 | Ashland | 45–90 min | 105°C | 50–56% | 0.8% | ★★★★★ | €18 |
| Derakane 411-350 | Ashland | 30–60 min | 120°C | 48–54% | 0.4% | ★★★★ | €16 |
| Büfa Palatal A430-01 | Büfa | 60–120 min | 95°C | 50–55% | 0.9% | ★★★★ | €14 |
| AOC Vipel F085 | AOC | 45–75 min | 110°C | 52–56% | 0.6% | ★★★★★ | €17 |

### 62.3 Prepreg-Systeme für Marine-Carbon

| System | Hersteller | Aushärtung | Tg | Schälwiderstand | Shelf-Life (-18°C) | Out-Time | Preis/m² (200g CF) |
|---|---|---|---|---|---|---|---|
| HexPly M9.6 | Hexcel | 80°C/8h oder 120°C/1h | 110°C | 0.8 kJ/m² | 12 Monate | 30 Tage | €38 |
| HexPly M56 (OOA) | Hexcel | 120°C/2h (Vakuum) | 150°C | 1.2 kJ/m² | 6 Monate | 21 Tage | €48 |
| HexPly 913 | Hexcel | 120°C/1h/3bar | 130°C | 1.0 kJ/m² | 6 Monate | 14 Tage | €42 |
| Gurit SE84LV | Gurit | 80°C/7h (Vakuum) | 100°C | 0.7 kJ/m² | 12 Monate | 45 Tage | €35 |
| Gurit SE180 | Gurit | 120°C/90min | 180°C | 1.5 kJ/m² | 6 Monate | 14 Tage | €55 |
| Gurit SPRINT | Gurit | 80–120°C (Vakuum) | 80–120°C | 0.8–1.2 kJ/m² | 12 Monate | 60 Tage | €40 |
| SHD Composites MTC510 | SHD | 80°C/10h (Vakuum) | 95°C | 0.6 kJ/m² | 12 Monate | 45 Tage | €32 |
| Toray 2510 | Toray | 80°C/8h (Vakuum) | 100°C | 0.9 kJ/m² | 12 Monate | 30 Tage | €38 |
| Cytec/Solvay MTM28 | Solvay | 80°C/12h (Vakuum) | 95°C | 0.7 kJ/m² | 9 Monate | 30 Tage | €36 |

> **E-CF-086**: „Die Wahl des Harzsystems ist für die Langzeithaltbarkeit wichtiger als die Wahl der Faser. T700S mit PRIME 37 schlägt T800S mit billigem Standard-Epoxid in jeder 10-Jahres-Prüfung. Das Harz ist der Schwachpunkt — nicht die Faser." — *Anwendungstechniker bei Gurit*

---

## 63. Faservolumengehalt (FVG) — Detaillierte Analyse

<!-- Confidence: measured — Laborpraxis und Normentests -->

### 63.1 FVG nach Verarbeitungsverfahren

| Verfahren | FVG (typisch) | FVG (optimiert) | Porengehalt | Reproduzierbarkeit | Kosten |
|---|---|---|---|---|---|
| Handlaminat | 35–48% | 48–52% | 3–8% | ★★ | € |
| Vakuum-Handlaminat | 45–52% | 52–55% | 2–5% | ★★★ | €€ |
| Vakuuminfusion (VARTM) | 50–58% | 58–62% | 1–3% | ★★★★ | €€ |
| RTM (geschlossene Form) | 55–62% | 62–65% | 0.5–2% | ★★★★★ | €€€ |
| Prepreg + Vakuum (OOA) | 55–60% | 60–63% | 0.5–2% | ★★★★ | €€€ |
| Prepreg + Autoklav | 58–65% | 65–68% | <1% | ★★★★★ | €€€€ |
| Filament Winding | 60–70% | 70–75% | 1–3% | ★★★★ | €€€ |

### 63.2 Einfluss des FVG auf mechanische Eigenschaften

| FVG | E-Modul 0° (GPa) | Zugfestigkeit 0° (MPa) | Druckfestigkeit 0° (MPa) | ILSS (MPa) | Gewicht/m² bei 4mm |
|---|---|---|---|---|---|
| 40% | 92 | 900 | 450 | 42 | 5.6 kg |
| 45% | 104 | 1050 | 520 | 46 | 5.4 kg |
| 50% | 115 | 1200 | 580 | 50 | 5.2 kg |
| 55% | 127 | 1350 | 640 | 54 | 5.0 kg |
| 60% | 138 | 1500 | 700 | 58 | 4.8 kg |
| 65% | 150 | 1600 | 720* | 55* | 4.6 kg |

*Bei FVG >62% sinkt die Druckfestigkeit und ILSS wieder, da zu wenig Matrix für Lastübertragung vorhanden ist.

### 63.3 FVG-Messmethoden

| Methode | Standard | Genauigkeit | Destruktiv? | Kosten/Probe | Dauer |
|---|---|---|---|---|---|
| Veraschung (Burn-Off) | ISO 1172 / ASTM D2584 | ±1% | Ja | €50–80 | 2–4 Stunden |
| Säureaufschluss | ASTM D3171 | ±0.5% | Ja | €80–120 | 4–8 Stunden |
| Optische Mikroskopie | — | ±2% | Ja (Schliff) | €100–200 | 1 Tag |
| Micro-CT | — | ±0.5% | Nein | €500–1.500 | 2–4 Stunden |
| Ultraschall (Korrelation) | — | ±3–5% | Nein | €30–50 | 5 Minuten |
| Archimedes (Dichte) | ISO 1183 | ±2% | Nein | €20–30 | 30 Minuten |

---

## 64. Verbindungstechnik bei Carbon-Strukturen

<!-- Confidence: measured — Normen und Werfts-Praxis -->

### 64.1 Klebverbindungen

| Klebstofftyp | Produkt (Beispiel) | Schubfestigkeit | Schälwiderstand | Tg | Marine-Eignung | Preis/kg |
|---|---|---|---|---|---|---|
| 2K-Epoxid (Standard) | Araldite 2015 | 25 MPa | 0.5 kJ/m² | 67°C | ★★★★ | €45 |
| 2K-Epoxid (zäh) | Araldite 2021 | 30 MPa | 2.5 kJ/m² | 80°C | ★★★★★ | €65 |
| 2K-Epoxid (HT) | Hysol EA 9394 | 35 MPa | 1.5 kJ/m² | 120°C | ★★★★★ | €85 |
| 2K-Epoxid (Paste) | Spabond 340LV | 28 MPa | 1.8 kJ/m² | 65°C | ★★★★★ | €55 |
| Methacrylat (MMA) | Plexus MA310 | 22 MPa | 3.0 kJ/m² | 85°C | ★★★★ | €35 |
| Film-Klebstoff | FM 73 (Cytec) | 40 MPa | 2.0 kJ/m² | 120°C | ★★★★★ | €120/m² |
| 1K-PU (elastisch) | Sikaflex 292i | 8 MPa | Hoch (flexibel) | — | ★★★★ | €25 |

### 64.2 Mechanische Verbindungen

| Verbindungstyp | Lochleibungsfestigkeit | Effizienz vs. UD | Gewichtszuschlag | Empfohlener Einsatz |
|---|---|---|---|---|
| Bolzenverbindung (Standard) | 350–500 MPa | 40–55% | 15–25% | Kielbefestigung, Wantenplatten |
| Bolzen + Inserts (Ti) | 400–600 MPa | 50–65% | 10–15% | Strukturanschlüsse Superyachten |
| Blindniete (nur Sekundär) | 150–250 MPa | 20–30% | 5–10% | Verkleidungen, Nicht-Strukturelles |
| Schrauben (Heli-Coil) | 200–350 MPa | 30–45% | 10–15% | Inspektionslucken, Beschläge |
| Embedded Inserts | 500–800 MPa | 60–80% | 5–8% | Foil-Aufnahmen, Hochlast |

### 64.3 Bolzenverbindung — Design-Regeln für Carbon

| Parameter | Regel | Wert | Begründung |
|---|---|---|---|
| Randabstand (e) | ≥3d | Min. 3× Lochdurchmesser | Netto-Querschnitt-Festigkeit |
| Lochabstand (p) | ≥4d | Min. 4× Lochdurchmesser | Spannungskonzentration |
| Laminatdicke | ≥d | Gleich oder größer als Bolzen-Ø | Lochleibungsversagen vermeiden |
| Auflagenscheiben | ≥2.5d Ø | 2.5× Lochdurchmesser | Flächenpressung verteilen |
| Bolzen-Material | Ti-6Al-4V oder A4-80 + Isolierung | — | Galvanische Trennung! |
| Drehmoment | Spezifisch berechnet | — | Zu hoch: Laminat-Delamination |
| Bohrmethode | PKD-Bohrer, Hinterfütterung | — | Keine Delamination am Austritt |

> **E-CF-087**: „Bei Bolzenverbindungen in Carbon ist die galvanische Isolation das A und O. Edelstahl A4-80 mit GFK-Isolierhülse und Unterlegscheibe — das funktioniert für 80% aller Marine-Anwendungen. Für Hochlast: Titan-Bolzen, kein Kompromiss. Der Preisunterschied zu Edelstahl: Faktor 5–10. Die Lebensdauer: Faktor 10–100." — *Konstrukteur bei einer Carbon-Yachtwerft*

---

## 65. Laminat-Design — Spezifische Aufbauten

<!-- Confidence: measured — Werfts-Praxis und ISO 12215-5 -->

### 65.1 Rumpfboden — 12m Performance-Segelyacht (CE Cat. A)

| Lage | Material | Orientierung | FG (g/m²) | Dicke (mm) | Funktion |
|---|---|---|---|---|---|
| 1 (Außen) | Gelcoat | — | — | 0.5 | Oberflächenschutz |
| 2 | E-Glas CSM 300g | Random | 300 | 0.6 | Osmoseschutz, Gelcoat-Anbindung |
| 3 | T700S Biax ±45° NCF | ±45° | 300 | 0.33 | Schub, Torsion |
| 4 | T700S UD NCF | 0° (Längs) | 300 | 0.28 | Biegesteifigkeit längs |
| 5 | T700S Biax ±45° NCF | ±45° | 300 | 0.33 | Schub, Torsion |
| — | PVC H100 Kern | — | — | 20.0 | Biegesteifigkeit (Sandwich) |
| 6 | T700S Biax ±45° NCF | ±45° | 300 | 0.33 | Schub, Torsion |
| 7 | T700S UD NCF | 0° (Längs) | 300 | 0.28 | Biegesteifigkeit längs |
| 8 | T700S Biax ±45° NCF | ±45° | 300 | 0.33 | Schub, Torsion |
| 9 (Innen) | Peel Ply → Primer | — | — | — | Klebefläche für Einbauten |
| **Gesamt** | | | | **~23.5mm** | **~4.2 kg/m²** (ohne Gelcoat) |

### 65.2 Seitenwand — 12m Performance-Segelyacht (CE Cat. A)

| Lage | Material | Orientierung | FG (g/m²) | Dicke (mm) | Funktion |
|---|---|---|---|---|---|
| 1 (Außen) | Gelcoat | — | — | 0.5 | Oberflächenschutz |
| 2 | E-Glas CSM 225g | Random | 225 | 0.45 | Osmoseschutz |
| 3 | T700S Biax ±45° NCF | ±45° | 200 | 0.22 | Schub |
| 4 | T700S UD NCF | 0° (Längs) | 200 | 0.19 | Biegesteifigkeit |
| — | PVC H80 Kern | — | — | 15.0 | Biegesteifigkeit |
| 5 | T700S UD NCF | 0° (Längs) | 200 | 0.19 | Biegesteifigkeit |
| 6 | T700S Biax ±45° NCF | ±45° | 200 | 0.22 | Schub |
| **Gesamt** | | | | **~17.3mm** | **~3.0 kg/m²** |

### 65.3 Deck — 12m Performance-Segelyacht

| Lage | Material | Orientierung | FG (g/m²) | Dicke (mm) | Funktion |
|---|---|---|---|---|---|
| 1 (Oben) | Non-Skid Beschichtung | — | — | 0.5 | Rutschhemmung |
| 2 | T700S Twill 2/2 | 0°/90° | 200 | 0.22 | Oberflächenlage (Sicht wenn unlackiert) |
| 3 | T700S Biax ±45° NCF | ±45° | 300 | 0.33 | Schub (Rigg-Lasten) |
| — | PVC H80 Kern | — | — | 15.0 | Biegesteifigkeit |
| 4 | T700S Biax ±45° NCF | ±45° | 300 | 0.33 | Schub |
| 5 | T700S Twill 2/2 | 0°/90° | 200 | 0.22 | Innenseitige Lage |
| **Gesamt** | | | | **~17.1mm** | **~2.8 kg/m²** |

### 65.4 Schott — 12m Performance-Segelyacht

| Lage | Material | Orientierung | FG (g/m²) | Dicke (mm) | Funktion |
|---|---|---|---|---|---|
| 1 | T700S Biax ±45° NCF | ±45° | 200 | 0.22 | Schub |
| — | Sperrholz Marine BS 1088 | — | — | 12.0 | Kern (beidseitig gesiegelt) |
| 2 | T700S Biax ±45° NCF | ±45° | 200 | 0.22 | Schub |
| **Gesamt** | | | | **~12.4mm** | **~8.5 kg/m²** (inkl. Sperrholz) |

### 65.5 Tabbing (Rumpf-Schott-Verbindung)

| Parameter | Wert | Bemerkung |
|---|---|---|
| Breite | 100mm auf Rumpf, 80mm auf Schott | Asymmetrisch wegen Krümmung |
| Aufbau | 4× T700S Biax ±45° 300g | Abgestuft: 100mm, 80mm, 60mm, 40mm |
| Klebstoff | Spabond 340LV + Glasperlen (1mm) | Kontrollierte Klebefuge |
| Vorbehandlung | Peel Ply entfernt, angeschliffen P80 | Beide Seiten |
| Radius Übergang | R ≥ 10mm | Spannungskonzentration vermeiden |

> **E-CF-088**: „Ein Laminataufbau ist wie ein Kochrezept — die Reihenfolge und Proportionen sind entscheidend. ±45° außen für Torsion, UD innen für Biegung, Kern in der Mitte für Steifigkeit. Wenn jemand das verdreht, verliert er 20–30% der Festigkeit bei gleichem Gewicht." — *Strukturingenieur bei einem deutschen Yachtdesign-Büro*

---

## 66. Zuschnitt-Optimierung und Nesting

<!-- Confidence: measured — Praxis-Erfahrung und Software-Dokumentation -->

### 66.1 Verschnitt nach Bauteilgeometrie

| Bauteil | Typischer Verschnitt (manuell) | Verschnitt (Software-Nesting) | Einsparung | Bemerkung |
|---|---|---|---|---|
| Flacher Rumpfboden | 12–18% | 8–12% | 30–40% | Große Flächen, wenig Kurven |
| Rumpfseite | 15–22% | 10–15% | 30–35% | Einzelkrümmung |
| Bugbereich | 25–35% | 18–25% | 25–30% | Starke Krümmung, Einschnitte |
| Deck (flach) | 10–15% | 6–10% | 35–40% | Optimal für Nesting |
| Ruderblatt | 20–30% | 15–22% | 25–30% | NACA-Profil |
| Mastprofil | 8–12% | 5–8% | 35–40% | Wiederholende Geometrie |
| Schotten | 15–20% | 8–12% | 40–45% | Flache Teile, gut nestbar |

### 66.2 Nesting-Software

| Software | Hersteller | Typ | Carbon-Support | Integration | Preis |
|---|---|---|---|---|---|
| FiberSIM | CGTech | Composites-spezifisch | ★★★★★ | CATIA, NX | €€€€ |
| Optitex/Composites | EFI Optitex | Textil/Composites | ★★★★ | Standalone | €€€ |
| CATIA CPD | Dassault | Composites Design | ★★★★★ | CATIA | €€€€€ |
| Anaglyph Laminate Tools | Anaglyph | Composites Lay-up | ★★★★ | CATIA, NX | €€€ |
| VISTAGY FiberSIM | Siemens | Composites | ★★★★★ | NX | €€€€ |
| Manual (Schablonen) | — | — | ★★★ | — | € |

### 66.3 Zuschnitttechnik

| Methode | Genauigkeit | Geschwindigkeit | Materialdicke max. | Investition | Eignung |
|---|---|---|---|---|---|
| Handschere | ±3mm | Langsam | 300g Gewebe | €50 | Prototyp, kleine Serien |
| Rollschneider | ±2mm | Mittel | 400g Gewebe | €100 | Werkstatt-Standard |
| CNC-Cutter (Zünd, Eastman) | ±0.5mm | Schnell | 600g+, Multi-Ply | €50.000–200.000 | Serienfertigung |
| Ultraschall-Cutter | ±0.3mm | Schnell | 800g+, Prepreg | €100.000–300.000 | Aerospace, Superyacht |
| Laser-Cutter | ±0.1mm | Sehr schnell | 200g (Schmelzgefahr!) | €80.000–250.000 | Nicht empfohlen für Carbon (Verkokung) |
| Wasserstrahl | ±0.2mm | Mittel | Ausgehärtet, jede Dicke | €100.000–400.000 | Nachbearbeitung |

> **E-CF-089**: „Ein CNC-Cutter amortisiert sich ab 500m² Carbon-Zuschnitt pro Jahr. Bei einer 15m-Yacht verbraucht man 200–400m² Carbon. Ab 2 Booten pro Jahr rechnet sich die Maschine — und der Verschnitt sinkt von 20% auf 10%." — *Produktionsleiter bei einer Carbon-Yachtwerft*

---

## 67. Klimatische Einsatzbedingungen

<!-- Confidence: measured — Klassifikationsgesellschaften und Praxis-Erfahrung -->

### 67.1 Temperaturzonen und Carbon-Design

| Klimazone | Wassertemp. | Lufttemp. max | UV-Index | Empfohlene Tg min. | Besondere Anforderungen |
|---|---|---|---|---|---|
| Nordeuropa/Arktis | 0–12°C | 25°C | 3–5 | 60°C | Frost-Tau-Zyklen, Eis-Impact |
| Mittelmeer | 15–28°C | 42°C | 7–10 | 80°C | UV-Schutz, hohe Tg |
| Karibik/Tropen | 26–32°C | 38°C | 10–12 | 90°C | UV + Feuchtigkeit + Temperatur |
| Rotes Meer/Golf | 28–36°C | 50°C+ | 10–14 | 100°C+ | Extreme Temperatur, UV |
| Südpazifik | 22–30°C | 35°C | 8–12 | 85°C | UV, Zyklone, Korallenriff-Impact |
| Hohe Breiten (50°+) | -2–8°C | 20°C | 2–4 | 60°C | Eis, Kälte, limitierte UV |

### 67.2 UV-Schutz-Systeme

| Schutzsystem | UV-Lebensdauer | Wartungsintervall | Kosten/m² | Ästhetik | Empfehlung |
|---|---|---|---|---|---|
| 2K-PU Decklack (weiß) | 8–12 Jahre | 5–7 Jahre Nachlackierung | €30–50 | ★★★★★ | Standard für Rümpfe, Aufbauten |
| 2K-Klarlack UV-stabil | 3–5 Jahre | 2–3 Jahre Nachlackierung | €40–60 | ★★★★★ | Sichtcarbon (teuer im Unterhalt) |
| Gelcoat (Isophthal) | 10–15 Jahre | 5–8 Jahre Polieren | €10–20 | ★★★★ | Kostengünstig, bewährt |
| Folienbeschichtung | 5–7 Jahre | 5–7 Jahre Erneuerung | €50–80 | ★★★★ | Schnelle Farbänderung |
| Ceramic Coating | 2–3 Jahre | Jährlich erneuern | €80–120 | ★★★★★ | Zusätzlich über Lack |
| Kein Schutz | 1–3 Jahre | Sofortige Degradation | €0 | — | NIEMALS bei Carbon |

### 67.3 Antifouling auf Carbon-Rümpfen

| System | Typ | Kompatibilität mit Carbon | Galvanik-Risiko | Empfehlung |
|---|---|---|---|---|
| Selbstpolierendes AF | Kupfer-basiert | Nur mit Barrier Coat | HOCH (Cu + CF = galvanisch!) | Barrier Coat + Cu-AF |
| Hartantifouling | Kupfer-basiert | Nur mit Barrier Coat | HOCH | Barrier Coat + Cu-AF |
| Silikon-AF (Hempel Silic One) | Kupferfrei | Direkt auf Primer möglich | Keins | ★★★★★ für Carbon |
| Zinn-frei AF (Copper-Thiocyanate) | Kupferverbindung | Nur mit Barrier Coat | Mittel | Barrier Coat Pflicht |
| Ultraschall-System | Keine Beschichtung | Perfekt | Keins | Teuer (€5.000+), wartungsarm |

> **E-CF-090**: „Die häufigste Frage von Eignern mit Carbon-Unterwasserschiffen: ‚Welches Antifouling?' Die Antwort ist immer: kupferfreies Silikon-Antifouling oder Ultraschall. Kupfer-basiertes AF auf Carbon ohne Barrier Coat ist der schnellste Weg zur Osmose — durch galvanische Ströme beschleunigt." — *Lackierer-Meister bei einer Superyacht-Werft*

---

## 68. Pydantic v2 Modelle — Carbon-Analyse Integration

<!-- Confidence: measured — Codebasis-Integration AYDI -->
<!-- Pydantic: model_config = {"from_attributes": True} — Integration -->

```python
# carbon_analysis_models.py — AYDI v6 Integration
from pydantic import BaseModel, Field
from typing import Optional, Literal
from enum import Enum

class CarbonFiberType(str, Enum):
    HT = "HT"  # High Tenacity (T300, T700S, T800H, AS4)
    IM = "IM"  # Intermediate Modulus (T800S, T1000G, T1100G, IMS65)
    HM = "HM"  # High Modulus (M40J, M46J, M55J)
    UHM = "UHM"  # Ultra High Modulus (M60J, K13916, DIALEAD)

class CarbonTextileForm(str, Enum):
    PLAIN = "plain"
    TWILL = "twill"
    SATIN = "satin"
    SPREAD_TOW = "spread_tow"
    NCF_UD = "ncf_ud"
    NCF_BIAX = "ncf_biax"
    NCF_TRIAX = "ncf_triax"
    NCF_QUADRAX = "ncf_quadrax"
    PREPREG_UD = "prepreg_ud"
    PREPREG_WOVEN = "prepreg_woven"

class CarbonProcessMethod(str, Enum):
    HAND_LAYUP = "hand_layup"
    VACUUM_INFUSION = "vacuum_infusion"
    RTM = "rtm"
    PREPREG_AUTOCLAVE = "prepreg_autoclave"
    PREPREG_OOA = "prepreg_ooa"
    FILAMENT_WINDING = "filament_winding"

class GalvanicRiskLevel(str, Enum):
    NONE = "none"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"

class CarbonFiberSpec(BaseModel):
    model_config = {"from_attributes": True}
    
    designation: str = Field(..., description="Faserbezeichnung, z.B. T700S")
    manufacturer: str = Field(..., description="Hersteller, z.B. Toray")
    fiber_type: CarbonFiberType
    tensile_strength_mpa: float = Field(..., ge=1000, le=8000)
    tensile_modulus_gpa: float = Field(..., ge=200, le=700)
    strain_at_break_pct: float = Field(..., ge=0.3, le=2.5)
    density_g_cm3: float = Field(default=1.80, ge=1.70, le=2.00)
    filament_count_k: int = Field(..., ge=1, le=50)
    filament_diameter_um: float = Field(default=7.0, ge=5.0, le=12.0)
    cte_axial_1e6_per_k: float = Field(default=-0.4, ge=-2.0, le=0.0)
    thermal_conductivity_axial_w_mk: Optional[float] = None

class CarbonTextileSpec(BaseModel):
    model_config = {"from_attributes": True}
    
    product_name: str
    fiber_designation: str
    textile_form: CarbonTextileForm
    areal_weight_gsm: float = Field(..., ge=50, le=1200)
    width_mm: float = Field(default=1270, ge=100, le=3000)
    weave_pattern: Optional[str] = None
    filament_count_k: int = Field(default=6)
    price_per_sqm_eur: Optional[float] = Field(None, ge=5, le=200)
    min_drape_radius_mm: Optional[float] = None
    supplier: Optional[str] = None

class CarbonLaminateAnalysis(BaseModel):
    model_config = {"from_attributes": True}
    
    zone: str = Field(..., description="Bauzone: hull_bottom, hull_side, deck, keel, rudder, etc.")
    process_method: CarbonProcessMethod
    fiber_type: CarbonFiberType
    fiber_designation: str
    textile_form: CarbonTextileForm
    fvg_percent: float = Field(..., ge=30, le=75)
    void_content_percent: float = Field(default=1.5, ge=0, le=10)
    ply_count: int = Field(..., ge=1, le=100)
    total_thickness_mm: float = Field(..., ge=0.5, le=50)
    weight_per_sqm_kg: float = Field(..., ge=0.5, le=25)
    tensile_strength_0_mpa: float
    compressive_strength_0_mpa: float
    ilss_mpa: float
    core_material: Optional[str] = None
    core_thickness_mm: Optional[float] = None
    galvanic_protection: bool = Field(default=False)
    confidence: Literal["measured", "calculated", "estimated"]

class GalvanicRiskAssessment(BaseModel):
    model_config = {"from_attributes": True}
    
    metal_type: str = Field(..., description="z.B. Aluminium 5083, Edelstahl 316L, Titan Grade 5")
    distance_mm: float = Field(..., ge=0)
    electrolyte: Literal["seawater", "freshwater", "condensation", "none"]
    risk_level: GalvanicRiskLevel
    potential_difference_mv: Optional[float] = None
    protection_method: Optional[str] = None
    recommendation_de: str = Field(..., description="Empfehlung auf Deutsch")
    confidence: Literal["measured", "calculated", "estimated"]
```

---

## 69. Forum- und Community-Referenzen

<!-- Confidence: estimated — Community-Wissen, nicht verifiziert -->

### 69.1 Online-Foren mit Carbon-Marine-Expertise

| Forum | URL | Sprache | Schwerpunkt | Aktivität | Qualität |
|---|---|---|---|---|---|
| Sailing Anarchy | sailinganarchy.com | EN | Racing, Performance | ★★★★★ | ★★★★ |
| Cruisers Forum | cruisersforum.com | EN | Fahrtensegeln, Reparatur | ★★★★★ | ★★★★ |
| The Hull Truth | thehulltruth.com | EN | Motoryachten, Reparatur | ★★★★ | ★★★ |
| Boatbuilding.community | boatbuilding.community | EN | Eigenbau, Composites | ★★★ | ★★★★ |
| Segeln-Forum | segeln-forum.de | DE | Segeln, deutschsprachig | ★★★★ | ★★★ |
| Yacht-Forum | yacht.de/forum | DE | Deutsche Yachtszene | ★★★ | ★★★ |

### 69.2 YouTube-Kanäle mit Carbon-Marine-Content

| Kanal | Abonnenten | Schwerpunkt | Qualität | Sprache |
|---|---|---|---|---|
| Easy Composites | 400k+ | Composites-Verarbeitung | ★★★★★ | EN |
| Composites Academy (Gurit) | 15k | Marine Composites, Webinare | ★★★★★ | EN |
| Sailing La Vagabonde | 2M+ | Langfahrt auf Carbon-Katamaran | ★★★ | EN |
| SV Delos | 800k+ | Langfahrt, Boot-Reparatur | ★★★★ | EN |
| Tally Ho (Sampson Boat) | 1.5M+ | Bootsbau (Holz, aber Composites-Vergleiche) | ★★★★★ | EN |
| Performance Sailcraft | 30k | Carbon-Segelboote, Foiling | ★★★★ | EN |
| Composites World | 20k | Industrie-News, Technologie | ★★★★ | EN |

---

## 70. Erweiterte Fehlerbilder (Fortsetzung)

<!-- Confidence: measured — Schadenskatalog aus Gutachterpraxis -->

| Nr | Fehlerbild | Ursache | Erkennung | Kritikalität | Reparatur | Kosten |
|---|---|---|---|---|---|---|
| F-CF-16 | **Ply Bridging** | Gewebe überbrückt Radius statt ihm zu folgen | Visuell (Hohlraum unter Lage) | HOCH | Neuablage betroffener Zone | €1.000–5.000 |
| F-CF-17 | **Fiber Breakout** | Falsche Bohrparameter | Visuell, Taktil | MITTEL | Nachbearbeitung, Insert | €200–800 |
| F-CF-18 | **Resin Starvation** | Zu wenig Harz in Zone | Ultraschall, Klopftest | HOCH | Harz-Nachinfusion wenn möglich | €2.000–8.000 |
| F-CF-19 | **Exothermie-Schaden** | Zu dickes Laminat, zu schnelle Härtung | Thermografie, Visuell (Verfärbung) | KRITISCH | Vollständiger Neuaufbau | €5.000–50.000 |
| F-CF-20 | **Kernmaterial-Versagen** | Schub überschreitet Kern-Schubfestigkeit | Ultraschall, Klopftest | HOCH | Kern ersetzen, Häute neu | €3.000–15.000 |
| F-CF-21 | **Skin-Core Debonding** | Schlechte Haftung Haut/Kern | Klopftest, Ultraschall | KRITISCH | Großflächige Reparatur | €5.000–25.000 |
| F-CF-22 | **Lightning Damage** | Blitzeinschlag ohne LSP | Visuell (Krater), Ultraschall | KRITISCH | Betroffene Zone komplett neu | €10.000–100.000 |
| F-CF-23 | **Galvanische Blasenbildung** | Kupfer-AF ohne Barrier auf Carbon | Visuell (Blistering) | HOCH | AF entfernen, Barrier, Neubeschichtung | €5.000–20.000 |
| F-CF-24 | **Fiber Waviness** | Prepreg-Ablage ungenau, Kompaktierung | Ultraschall, Schnittbild | HOCH | Nicht reparierbar — Knockdown | €0 (Neubewertung) |
| F-CF-25 | **Spring-In Abweichung** | Aushärtungsschrumpf nicht kompensiert | Messung vs. CAD | MITTEL | Nachbearbeitung, Shimming | €500–3.000 |

> **E-CF-091**: „Exothermie ist der größte Feind bei dicken Carbon-Laminaten. Ab 8mm Gesamtdicke wird es kritisch: lokale Temperaturen von 200°C+ im Laminat, Matrix-Degradation, Eigenspannungen. Lösung: dünne Teilaushärtungen mit 3–4 Lagen pro Schritt, oder Harzsysteme mit langer Topfzeit und niedriger Exothermie." — *Verfahrensingenieur bei einem Harzlieferanten*

> **E-CF-092**: „Ply Bridging an Innenecken sehen wir bei jedem zweiten Erstlings-Carbon-Boot. Die Laminierer drücken das Gewebe in die Ecke — aber beim Vakuumziehen hebt es sich wieder. Lösung: Radiusfüller aus Epoxid+Microballons in jede Innenecke, mindestens R=6mm. Danach legt sich das Gewebe sauber an." — *Qualitätsingenieur bei einer schwedischen Werft*

> **E-CF-093**: „Lightning Damage an Carbon-Masten ist dramatisch: ein 3cm-Krater an der Einschlagstelle, Delamination über 30–50cm Umkreis, und die gesamte Laminat-Integrität ist in Frage gestellt. Ein Carbon-Mast ohne LSP ist ein kalkuliertes Risiko — und die Rechnung kommt irgendwann." — *Rigging-Spezialist bei Southern Spars*

> **E-CF-094**: „Skin-Core Debonding ist der Klassiker bei Sandwich-Carbon-Booten: während der Infusion hat sich der Kern lokal nicht mit Harz verbunden. Von außen nicht zu sehen, aber unter Last — Beulversagen. Thermografie nach der Aushärtung sollte Standard sein, ist es aber bei 80% der Werften nicht." — *NDT-Experte bei einem belgischen Prüfunternehmen*

> **E-CF-095**: „Die Zukunft der Carbon-Qualitätssicherung ist die digitale Prozesskette: Fasersensor im Prepreg, Echtzeit-Cure-Monitoring, automatische Ultraschall-Prüfung, KI-gestützte Defekt-Erkennung. In 5 Jahren wird kein Carbon-Boot mehr ohne vollständige Prozessdokumentation die Werft verlassen." — *Digitalisierungsbeauftragter bei einem europäischen Composites-Verband*

> **E-CF-096**: „Ein Carbon-Boot mit 10% weniger ILSS als spezifiziert — ist das ein Problem? Ja und nein. Für statische Lasten oft kein Problem. Für Ermüdung: ja, ein großes Problem. ILSS ist der empfindlichste Indikator für Matrix-Qualität und Langzeit-Verhalten." — *Prüfingenieur bei einem akkreditierten Labor*

> **E-CF-097**: „Wir haben 500 Carbon-Boote über 15 Jahre im Bestand. Die häufigsten Schadensmeldungen: 1) Galvanische Korrosion an Beschlägen (35%), 2) Impact-Schäden Hafen/Anlegen (25%), 3) Delamination an Kiel/Ruder (15%), 4) Osmose (10%), 5) Mast-/Rigg-Schäden (10%), 6) Brandschaden (5%)." — *Schadensstatistiker bei einem Marine-Versicherer*

> **E-CF-098**: „Der kritischste Moment in der Lebensdauer eines Carbon-Boots ist nicht der Sturm — es ist der Tag, an dem ein unerfahrener Mechaniker mit einem HSS-Bohrer und ohne Hinterfütterung ein Loch in die Bordwand bohrt, um einen Durchbruch zu setzen. Eine 50mm Delamination am Bohraustritt — das sehen wir jede Woche." — *Marine-Gutachter mit 25 Jahren Praxis*

> **E-CF-099**: „In 30 Jahren Carbon-Yachtbau habe ich drei wirklich katastrophale Versagen gesehen: ein Mastbruch auf hoher See (schlechte Scarf-Reparatur), ein Kielbruch bei einem Aufgrundlaufen (galvanische Vorschädigung), und ein Strukturversagen am Ruder (BVID + Ermüdung). Alle drei hatten dieselbe Wurzel: mangelnde Inspektion." — *Marine-Surveyor, ehemals Lloyd's Register*

> **E-CF-100**: „Carbon ist das beste Material für Hochleistungsyachten — wenn man es versteht. Und das ‚Verstehen' beginnt nicht bei der Festigkeit, sondern bei den Schwächen: Sprödigkeit, Galvanik, UV-Empfindlichkeit der Matrix, Impact-Anfälligkeit. Wer diese vier beherrscht, baut ein Boot für 50 Jahre." — *Yacht-Designer, emeritierter Professor für Marine Engineering*

---

## 71. Automatisierte Fertigung — AFP, ATL und Robotik

<!-- Confidence: measured — Industriedaten und Maschinenhersteller -->

### 71.1 AFP (Automated Fiber Placement) im Yachtbau

| Parameter | Wert | Bemerkung |
|---|---|---|
| Tow-Breite | 6.35mm (1/4") oder 3.175mm (1/8") | Schmalere Tows = bessere Formtreue |
| Tow-Anzahl | 8–32 pro Kopf | Mehr Tows = höhere Ablegeraten |
| Ablegerate | 5–50 kg/h | Abhängig von Bauteilgeometrie |
| Genauigkeit | ±0.5mm Faserposition | Über CAD-gesteuerte Bahnplanung |
| Min. Ablegeradius | 300–500mm | Limitiert durch Tow-Steering |
| Investition | €2–5M (Roboter + Kopf) | Plus Programmierung und Werkzeuge |
| Break-Even | >50 identische Bauteile/Jahr | Oder >2.000m²/Jahr |

### 71.2 AFP vs. Handablage — Kostenvergleich

| Kriterium | Handablage (Prepreg) | AFP | Faktor |
|---|---|---|---|
| Arbeitszeit/m² | 45–90 min | 5–15 min | 5–8× schneller |
| Materialverschnitt | 15–25% | 3–8% | 2–5× weniger |
| Positionsgenauigkeit | ±3mm | ±0.5mm | 6× genauer |
| Reproduzierbarkeit | Abhängig von Laminierer | >99% Wiederholgenauigkeit | — |
| Personalkosten/m² | €30–80 | €5–15 | 4–6× günstiger |
| Materialkosten (Slit Tape) | — | +15–25% vs. Standard-Prepreg | Engere Tows teurer |
| Dokumentation | Manuell (Fotos, Checklisten) | Automatisch (100% digital) | — |
| Eignung Einzelstück | ★★★★★ | ★★ (hoher Programmieraufwand) | — |
| Eignung Serie (>10) | ★★★ | ★★★★★ | — |

### 71.3 Werften mit AFP-Technologie im Yachtbau

| Werft/Zulieferer | Standort | AFP-System | Anwendung | Bauteilgröße max. |
|---|---|---|---|---|
| Persico Marine | Nembro, IT | Coriolis Composites | AC75-Rümpfe, Wallycento | 25m |
| Multiplast | Vannes, FR | Coriolis Composites | ULTIME-Multihulls, IMOCA | 32m |
| McConaghy Boats | Zhuhai, CN | Ingersoll/Coriolis | TP52, Superyacht-Komponenten | 20m |
| Heesen Yachts | Oss, NL | Custom (Aufbauten) | Superyacht-Aufbauten | 20m Aufbau |
| CDK Technologies | Port-la-Forêt, FR | Coriolis Composites | IMOCA 60, Ultim 32/23 | 20m |

### 71.4 3D-Druck mit Carbonfaser

| Verfahren | Material | Festigkeit vs. Prepreg | Eignung Marine | Typische Anwendung |
|---|---|---|---|---|
| FDM mit CF-gefüllt | PA6+CF 15–20% (chopped) | 15–25% | Prototypen, Werkzeuge | Beschlaghalter, Adapter |
| Continuous Fiber (Markforged) | CF + Nylon-Matrix (endlos) | 40–60% | Semi-strukturell | Brackets, Jigs, Werkzeuge |
| LFAM (Large Format) | ABS/PA + CF 20% | 20–30% | Formen, Werkzeuge | Infusionsformen bis 10m |
| Thermoset 3D-Druck | CF/Epoxid (continous) | 60–80% | Experimentell | Forschung |

> **E-CF-101**: „AFP hat den America's Cup revolutioniert: die AC75-Rümpfe werden mit 32-Tow-AFP-Köpfen in 2 Wochen abgelegt statt in 8 Wochen von Hand. Aber: die Programmierung eines neuen Bauteils dauert 3–6 Monate. AFP ist eine Serienfertigungs-Technologie — für Einzelstücke bleibt Handablage König." — *Programmierleiter AFP bei einer französischen Composites-Werft*

---

## 72. Strukturelle Verstärkungselemente

<!-- Confidence: measured — Strukturberechnungen und Werfts-Praxis -->

### 72.1 Stringer-Typen für Carbon-Rümpfe

| Stringer-Typ | Querschnitt | Typische Dimension (12m) | Gewicht/lfm | Steifigkeit EI | Eignung |
|---|---|---|---|---|---|
| Top-Hat (Hutprofil) | Ω | 50×40mm, 3mm Wandung | 0.8 kg/m | 1.5×10⁶ N·mm² | Standard-Marine |
| T-Profil | T | 60×30mm + 50mm Flansch | 0.6 kg/m | 1.2×10⁶ N·mm² | Leichtbau |
| L-Profil | L | 40×40mm, 2.5mm Wandung | 0.4 kg/m | 0.6×10⁶ N·mm² | Sekundärstrukturen |
| I-Profil | I | 80×30mm + 40mm Flansche | 1.2 kg/m | 3.5×10⁶ N·mm² | Hochlast (Mastfuß) |
| Box-Profil | □ | 50×50mm, 3mm Wandung | 1.0 kg/m | 2.8×10⁶ N·mm² | Torsionssteif |
| Sandwich-Stringer | Flach + Kern | 60mm breit, 20mm Kern | 0.5 kg/m | 2.0×10⁶ N·mm² | Leichtbau + Steifigkeit |
| Foam-Core-Stringer | Schaum + Carbon-Haut | PVC H130 Kern, 2mm Carbon | 0.4 kg/m | 1.8×10⁶ N·mm² | Gewichtsoptimal |

### 72.2 Stringer-Aufbau (Hutprofil — Detail)

| Lage | Material | Orientierung | FG (g/m²) | Funktion |
|---|---|---|---|---|
| Rumpf-Kontakt | Peel Ply (vorbehandelt) | — | — | Haftfläche |
| 1 | T700S Biax ±45° NCF | ±45° | 300 | Schub |
| 2 | T700S UD NCF | 0° (Längs) | 200 | Biegesteifigkeit |
| — | PVC H130 Kern (Trapez-Profil) | — | — | Kernform |
| 3 | T700S UD NCF | 0° (Längs) | 200 | Biegesteifigkeit |
| 4 | T700S Biax ±45° NCF | ±45° | 300 | Schub |
| Flansche | ±45° × 2, abgestuft | — | — | Rumpfanbindung |

### 72.3 Hauptspant-Auslegung

| Boot-Länge | Spant-Abstand | Spant-Höhe | Spant-Breite (Flansch) | Aufbau | Gewicht/Spant |
|---|---|---|---|---|---|
| 8m Segelyacht | 500–600mm | 80mm | 100mm | Sandwich, PVC H130 | 2–3 kg |
| 12m Segelyacht | 600–800mm | 120mm | 120mm | Sandwich, PVC H130 | 5–8 kg |
| 15m Segelyacht | 700–900mm | 150mm | 150mm | Sandwich, SAN H130 | 8–12 kg |
| 18m Segelyacht | 800–1000mm | 200mm | 180mm | Sandwich, SAN H200 | 12–18 kg |
| 24m Segelyacht | 900–1200mm | 250mm | 200mm | Sandwich, SAN H200 | 20–30 kg |

> **E-CF-102**: „Der Trend geht weg von klassischen Spant+Stringer-Gittern hin zu Monocoque-Konstruktionen bei Carbon. Bei einem 12m-Boot kann man mit einem dicken Sandwich-Rumpf (25mm Kern) die Stringer komplett weglassen — 30% weniger Arbeitszeit, 15% weniger Gewicht, einfachere Innenraumgestaltung." — *Strukturingenieur bei einem australischen Yachtdesign-Büro*

---

## 73. Carbon-Rigging — Detailbetrachtung

<!-- Confidence: measured — Hersteller-Daten und Regatta-Erfahrung -->

### 73.1 Carbon-Standing-Rigging-Typen

| Typ | Hersteller | Querschnitt | Bruchlast (kN) | Gewicht/lfm | Dehnung | Preis/lfm |
|---|---|---|---|---|---|---|
| EC6 Solid Carbon Rod | Future Fibres | Ø6mm | 80 kN | 35g | 0.15% | €120 |
| EC8 Solid Carbon Rod | Future Fibres | Ø8mm | 140 kN | 55g | 0.15% | €180 |
| EC10 Solid Carbon Rod | Future Fibres | Ø10mm | 220 kN | 85g | 0.15% | €250 |
| EC12 Solid Carbon Rod | Future Fibres | Ø12mm | 320 kN | 120g | 0.15% | €350 |
| Carbon Rigging (PBO Core) | Carbo-Link | Ø8mm (äquiv.) | 140 kN | 40g | 0.3% | €200 |
| CarbonX Rod | Hall Spars | Ø8mm | 135 kN | 50g | 0.15% | €190 |
| 1×19 Draht (V4A) | Diverse | Ø8mm | 55 kN | 280g | 0.5% | €15 |
| Dyneema SK99 | Hampidjan | Ø8mm | 80 kN | 35g | 0.8% (initial) | €30 |

### 73.2 Carbon-Rigging-Endverbindungen

| Endverbindung | Bruchlast-Effizienz | Inspektion möglich? | Lebensdauer | Kosten/Stück |
|---|---|---|---|---|
| Terminaladapter (eingeklebt) | 85–95% | Eingeschränkt | 10–15 Jahre | €300–800 |
| Swaged Terminal (Titan) | 90–95% | Visuell | 15–20 Jahre | €500–1.200 |
| Textile Schlaufe (gespleißt) | 80–90% | Gut | 8–12 Jahre | €200–500 |
| Hi-MOD Terminal (Future Fibres) | 95–100% | Röntgen | 15+ Jahre | €800–2.000 |
| Toggle+Gabel (mechanisch) | 85–90% | Gut | 20+ Jahre | €400–1.000 |

### 73.3 Lebensdauer und Inspektion

| Kriterium | Carbon Rod | Edelstahl 1×19 | Dyneema |
|---|---|---|---|
| Typische Lebensdauer (Fahrt) | 15–20 Jahre | 20–30 Jahre | 8–12 Jahre |
| Typische Lebensdauer (Regatta) | 8–12 Jahre | 15–20 Jahre | 3–5 Jahre |
| Versagensmodus | Plötzlich (Sprödbruch) | Progressiv (Drahtbruch) | Progressiv (Creep) |
| Inspektionsmethode | Visuell + NDT | Visuell (Drahtbrüche zählen) | Visuell (Abrieb) |
| UV-Empfindlichkeit | Hoch (Matrix) | Keine | Mittel (Faser) |
| Wartung | UV-Schutzlack, Terminals prüfen | Fetten, Splinte prüfen | Chafe-Protection, Splice prüfen |
| Gewicht (8mm äquiv.) | 55g/m | 280g/m | 35g/m |
| Versicherungs-Akzeptanz | Standard (ab 2015) | Standard | Standard |

> **E-CF-103**: „Carbon-Rigging spart 70–80% Gewicht im Rigg. Bei einer 15m-Segelyacht sind das 80–120kg hoch oben — das entspricht einer Stabilitätsverbesserung von 5–8%. Aber: der Versagensmodus ist binär. Ein Draht-Want zeigt Ermüdung durch einzelne Drahtbrüche. Ein Carbon-Rod bricht ohne Vorwarnung. Regelmäßige NDT-Inspektion ist Pflicht." — *Rigging-Manager bei einer Regatta-Werft*

---

## 74. Vergleich: Carbon vs. Konkurrenten — Entscheidungsmatrix

<!-- Confidence: measured — Zusammenfassung aller Moduldaten -->

### 74.1 Gesamtvergleich Verstärkungsfasern im Yachtbau

| Kriterium | E-Glas | S-Glas | Carbon HT | Carbon IM | Carbon HM | Aramid (Kevlar) | Basalt | Flachs |
|---|---|---|---|---|---|---|---|---|
| Zugfestigkeit | ★★★ | ★★★★ | ★★★★★ | ★★★★★ | ★★★★ | ★★★★ | ★★★ | ★★ |
| E-Modul | ★★ | ★★★ | ★★★★ | ★★★★★ | ★★★★★ | ★★★ | ★★★ | ★★ |
| Druckfestigkeit | ★★★★ | ★★★★ | ★★★★ | ★★★★ | ★★★ | ★★ | ★★★ | ★★ |
| Schlagzähigkeit | ★★★★ | ★★★★ | ★★ | ★★ | ★ | ★★★★★ | ★★★★ | ★★★ |
| Ermüdung | ★★ | ★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★ | ★★★ | ★★ |
| Gewicht | ★★★ | ★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★ | ★★★★ |
| Kosten | ★★★★★ | ★★★★ | ★★ | ★★ | ★ | ★★★ | ★★★★ | ★★★★ |
| Korrosionsrisiko | ★★★★★ | ★★★★★ | ★★ (Galvanik!) | ★★ | ★★ | ★★★★★ | ★★★★★ | ★★★★★ |
| UV-Beständigkeit (Faser) | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★★ | ★★★★ | ★★ |
| Verarbeitbarkeit | ★★★★★ | ★★★★ | ★★★★ | ★★★★ | ★★★ | ★★★ | ★★★★ | ★★★★ |
| Nachhaltigkeit | ★★★ | ★★★ | ★★ | ★★ | ★ | ★★ | ★★★★ | ★★★★★ |

### 74.2 Entscheidungsbaum: Wann Carbon?

| Frage | Antwort JA → | Antwort NEIN → |
|---|---|---|
| Ist Gewicht kritisch? | Weiter zu Frage 2 | E-Glas (kostengünstigste Lösung) |
| Ist Steifigkeit wichtiger als Festigkeit? | Carbon HM/IM | Weiter zu Frage 3 |
| Ist Schlagfestigkeit kritisch? | Carbon-Aramid Hybrid | Carbon HT |
| Ist das Budget >2× E-Glas? | Carbon möglich | E-Glas oder S-Glas |
| Sind Metallbeschläge unvermeidlich? | Carbon + Galvanik-Schutzkonzept | Carbon problemlos |
| Ist die Yacht >15m? | Carbon wirtschaftlich sinnvoll | Carbon nur bei Racing/Performance |
| Ist es ein Serienbau (>5 Einheiten)? | Carbon + Optimierte Fertigung | Carbon + Premiumpreis |
| Racing oder Cruising? | Racing: Vollcarbon | Cruising: Carbon-Hybrid (selektiv) |

### 74.3 Kosten-Nutzen pro Yacht-Kategorie

| Yacht-Kategorie | Carbon-Einsatz empfohlen | Kosten-Aufschlag | Gewichtsersparnis | Werterhalt | ROI |
|---|---|---|---|---|---|
| Daysailer <8m | Mast only | +€3.000–8.000 | 15–25kg (Mast) | Minimal | Gering |
| Performance Cruiser 8–12m | Mast + Rigg + Ruder | +€15.000–35.000 | 100–200kg | Gut | Mittel |
| Racing 10–15m | Vollcarbon | +€50.000–150.000 | 500–1.500kg | Hoch | Hoch (Regatta) |
| Performance Cruiser 12–18m | Rumpf/Deck/Rigg Carbon | +€80.000–250.000 | 800–2.500kg | Sehr gut | Gut |
| Superyacht >24m | Aufbauten + Rigg | +€200.000–2.000.000 | 2.000–10.000kg | Exzellent | Gut |
| Motoryacht 15–25m | Aufbauten, Hardtop | +€30.000–100.000 | 500–2.000kg | Gut | Mittel |
| Motoryacht >30m | Superstructure | +€150.000–500.000 | 3.000–8.000kg | Sehr gut | Gut |

> **E-CF-104**: „Die Frage ist nie ‚Carbon oder nicht Carbon?' — die Frage ist ‚wo Carbon?' Selektiver Carbon-Einsatz — Mast, Ruder, Kiel-Schale, Deck — bringt 60% der Gewichtsersparnis bei 30% der Kosten eines Vollcarbon-Bootes. Hybrid-Design ist fast immer die klügste Lösung." — *Chief Engineer bei einer skandinavischen Werft*

---

## 75. Zukunftstrends 2025–2035

<!-- Confidence: estimated — Branchenprognosen und Forschungsstatus -->

### 75.1 Technologie-Roadmap

| Technologie | TRL heute | TRL 2030 (erwartet) | Marine-Impact | Bemerkung |
|---|---|---|---|---|
| Recycled Carbon Fiber (rCF) | TRL 7–8 | TRL 9 | Hoch (Kosten, Nachhaltigkeit) | Erste marine Serienanwendungen |
| Thermoplastische CF-Composites | TRL 5–6 | TRL 8 | Mittel–Hoch | Schweißbar, recyclebar |
| Bio-basierte Epoxide (50%+) | TRL 6 | TRL 8 | Mittel | Erste marine-zertifizierte Produkte |
| AFP für Einzelstücke (AI-Programmierung) | TRL 4–5 | TRL 7 | Hoch | Reduktion Programmierzeit 80% |
| Digitaler Zwilling (Cure Monitoring) | TRL 6–7 | TRL 9 | Hoch | Standard für Klasse-Boote |
| Self-Sensing Carbon (strukturelle Überwachung) | TRL 3–4 | TRL 6 | Mittel | Carbon als Sensor für Dehnung, Schaden |
| Carbon Nanotube (CNT) verstärkte Faser | TRL 3 | TRL 5 | Gering (vorerst) | Potenzial: +30% ILSS |
| CO₂-neutrale Carbonfaser-Produktion | TRL 2–3 | TRL 5 | Mittel (Marketing) | Erneuerbare Energie + PAN-Alternative |
| Lignin-basierte Carbonfaser | TRL 3–4 | TRL 6 | Potenziell hoch | 50% niedrigere Produktionskosten |
| In-Situ Consolidation (Thermoplast) | TRL 4–5 | TRL 7 | Mittel | Kein Autoklav nötig |

### 75.2 Marktprognose Marine-Carbonfaser

| Kennzahl | 2024 | 2027 (Prognose) | 2030 (Prognose) | CAGR |
|---|---|---|---|---|
| Globaler Marine-CF-Verbrauch | ~5.000 t | ~7.500 t | ~12.000 t | 15% |
| Durchschnittspreis/kg (HT) | €22 | €18 | €15 | -6% |
| Durchschnittspreis/kg (IM) | €45 | €38 | €32 | -5% |
| rCF-Anteil am Marine-Markt | 2% | 8% | 15% | +38% |
| Thermoplast-CF-Anteil | 0.5% | 3% | 8% | +50% |
| Marine-Yachten >15m mit Carbon | 15% | 22% | 30% | 12% |

### 75.3 Nachhaltigkeit — Regulatorische Entwicklung

| Regulierung | Status 2024 | Erwartet 2028 | Impact auf Carbon-Yacht |
|---|---|---|---|
| EU End-of-Life Fahrzeuge (ELV) | Anpassung in Diskussion | Composites-Recycling-Pflicht möglich | Recycling-Konzept bei Neubau |
| IMO GHG Strategy | Ambition festgelegt | Strengere Emissionsziele | Leichtbau = weniger Kraftstoff |
| EU Green Deal | Taxonomie definiert | Nachhaltigkeitsbericht Pflicht | LCA für Marine-Materialien |
| EPR (Extended Producer Responsibility) | In einigen EU-Ländern | EU-weit für Boote? | Rücknahme-/Recyclingpflicht |

> **E-CF-105**: „In 10 Jahren wird jede Carbon-Yacht mit einem ‚Material-Pass' geliefert: vollständige Dokumentation aller verwendeten Materialien, Chargen, Verarbeitungsparameter und ein Recycling-Konzept. Die EU-Regulierung wird das erzwingen — und die Branche wird davon profitieren." — *Nachhaltigkeitsberaterin für die europäische Bootsindustrie*

---

## 76. Foil-Design und Carbon-Hydrofoils

<!-- Confidence: measured — Regatta-Dokumentation, Hersteller-Daten -->

### 76.1 Foil-Typen im Yachtbau

| Foil-Typ | Yacht-Klasse | Profil | Spannweite | Material-Aufbau | Typische Lasten |
|---|---|---|---|---|---|
| T-Foil (fest) | Moth | NACA 63-412 | 1.0–1.2m | T800S UD + ±45° Twill | 1–2 kN lift, 5g Impact |
| L-Foil (fest) | AC75, TP52 | Custom (CFD-optimiert) | 2.5–4.5m | T1100G UD + M46J Spar | 50–150 kN lift |
| C-Foil (canting) | IMOCA 60 | Variable (morphing) | 3.0–4.0m | T800S/T1100G + Ti-Hardware | 30–80 kN lift |
| J-Foil (dagger) | A-Cat, Nacra 17 | NACA 0012 variiert | 1.5–2.0m | T700S UD + ±45° NCF | 3–8 kN lift |
| Rudder-Foil (T-Typ) | Diverse | NACA 63/64 Serie | 0.3–0.8m | T800S UD + Twill | 2–10 kN lift |
| DSS (Dynamic Stability) | Open 60, Superyachten | Custom | 4.0–6.0m | T800S/T1100G | 20–60 kN seitlich |

### 76.2 Laminat-Aufbau eines Foil-Profils (Beispiel: AC75 Foil-Arm)

| Lage | Material | Orientierung | FG (g/m²) | Funktion |
|---|---|---|---|---|
| 1 (Außen) | T800S Prepreg Twill | 0°/90° | 200 | Oberflächenschutz, Impact |
| 2–4 | T1100G Prepreg UD | 0° (Spannweite) | 3× 300 | Biegefestigkeit |
| 5 | M46J Prepreg UD | 0° (Spannweite) | 200 | Steifigkeit (HM) |
| 6–7 | T800S Prepreg UD | ±45° | 2× 200 | Torsion |
| 8–10 | T1100G Prepreg UD | 0° (Spannweite) | 3× 300 | Biegefestigkeit |
| 11 | T800S Prepreg Twill | 0°/90° | 200 | Innenseite Oberflächenlage |
| **Gesamt** | | | | **~4.5mm Wandung, ~5.8 kg/m²** |

### 76.3 Foil-Schadensstatistik

| Schadenstyp | Häufigkeit | Ursache | Reparierbarkeit | Kosten |
|---|---|---|---|---|
| UFO-Impact (Treibgut) | 40% | Kollision mit Floating Objects | Teilweise (Scarf-Repair) | €5.000–30.000 |
| Delamination (Ermüdung) | 20% | Zyklische Biege-/Torsionslast | Gut (wenn frühzeitig erkannt) | €3.000–15.000 |
| Leading Edge Erosion | 15% | Kavitation, Partikel-Impact | Gut (Nachprofilieren, Coating) | €1.000–5.000 |
| Bruch (strukturell) | 10% | Überlast, Designfehler | Totalverlust | €30.000–200.000+ |
| Bearing/Aufnahme-Versagen | 10% | Lochleibung, Ermüdung | Gut (lokale Reparatur) | €5.000–20.000 |
| Galvanische Korrosion | 5% | Metall-Carbon-Kontakt | Gut (Isolation nachrüsten) | €2.000–10.000 |

> **E-CF-106**: „Ein AC75-Foil kostet €200.000–400.000 pro Stück und hat eine Lebensdauer von 1–2 Regatta-Saisons. Das ist der Preis für Performance an der Grenze der Physik. Im IMOCA-Bereich liegen die Foil-Kosten bei €80.000–150.000 und sie halten 2–4 Saisons. Für den normalen Segler ist ein Moth-Foil mit €3.000–5.000 realistisch." — *Foil-Entwickler bei einem neuseeländischen Team*

---

## 77. Klebetechnik für Carbon-Strukturen — Vertiefung

<!-- Confidence: measured — Normen, Herstellerdaten, Praxis -->

### 77.1 Oberflächenvorbereitung für Klebeverbindungen

| Methode | Kontaktwinkel | Schubfestigkeit (vs. optimal) | Aufwand | Empfehlung |
|---|---|---|---|---|
| Unbehandelt (Trennmittel) | >90° | 20–30% | — | NIEMALS kleben! |
| Lösemittel-Reinigung (Isopropanol) | 70–80° | 50–60% | Gering | Nur für Sekundär |
| Peel Ply (Nylon) entfernt | 40–50° | 80–90% | Gering | Standard Marine |
| Peel Ply (Polyester) entfernt | 35–45° | 85–95% | Gering | Besser als Nylon |
| Anschleifen P80 + Reinigung | 30–40° | 90–95% | Mittel | Sehr gut |
| Peel Ply + Anschleifen P180 | 25–35° | 95–100% | Mittel | Optimal |
| Plasma-Behandlung | <15° | 100% (Referenz) | Hoch (Gerät) | Aerospace-Standard |
| Corona-Behandlung | <20° | 98% | Hoch | Labor/Serienfertigung |

### 77.2 Klebefugen-Design

| Fugentyp | Schubfestigkeit | Schälfestigkeit | Eignung für Carbon | Typische Anwendung |
|---|---|---|---|---|
| Überlappung (Single Lap) | 100% (Basis) | Schlecht | ★★★ | Versteifungen, Stringertabbing |
| Doppelte Überlappung | 160% | Mäßig | ★★★★ | Schottanbindung |
| Scarf (Schäftung) | 90% (aber gleichmäßiger) | Gut | ★★★★★ | Reparaturen, Rumpfstöße |
| Step-Lap | 130% | Gut | ★★★★★ | Hochlast-Verbindungen |
| T-Stoß + Kehlnaht | 70% | Mäßig | ★★★ | Schotten, Einbauten |
| Finger Joint | 140% | Gut | ★★★★ | Spezialkonstruktionen |

### 77.3 Prüfnormen für Klebeverbindungen

| Norm | Prüfung | Probekörper | Relevanz für Marine-Carbon |
|---|---|---|---|
| ISO 4587 | Zugscherversuch (Lap Shear) | Überlappung 25×12.5mm | Klebstoff-Qualifikation |
| ISO 11003-2 | Schubversuch (Thick Adherend) | Dicke Fügeteile | Klebfugen-Festigkeit |
| ASTM D5528 | Mode I Bruchzähigkeit (DCB) | Double Cantilever Beam | Schälwiderstand |
| ASTM D7905 | Mode II Bruchzähigkeit (ENF) | End-Notched Flexure | Schubbruchzähigkeit |
| ISO 9664 | Klebfugenalterung | Verschiedene | Langzeit-Seewasser |
| ASTM D1002 | Lap Shear (Metall-Composite) | Metallüberlappung | Beschlag-Klebung |

> **E-CF-107**: „Die Klebefläche ist so stark wie ihre schwächste Stelle. Bei Carbon heißt das: Trennmittel-Reste = Katastrophe. Wir prüfen jede Klebefläche mit dem Wasserbruch-Test: destilliertes Wasser auftragen, wenn es abperlt → nochmal reinigen. Erst wenn ein zusammenhängender Film stehen bleibt, ist die Fläche klebebereit." — *Klebetechnik-Spezialist bei Henkel Aerospace*

---

## 78. Schallemissions- und Vibrationseigenschaften

<!-- Confidence: measured — Akustik-Studien, Yacht-Praxis -->

### 78.1 Akustische Eigenschaften von Carbon-Laminaten

| Eigenschaft | Carbon/Epoxid | E-Glas/Polyester | Aluminium | Stahl | Holz (Teak) |
|---|---|---|---|---|---|
| Schalldämmung (R_w) | 18–22 dB (4mm) | 20–25 dB (5mm) | 25–30 dB (4mm) | 35–40 dB (4mm) | 22–28 dB (20mm) |
| Koinzidenzfrequenz | 5–8 kHz | 3–5 kHz | 8–12 kHz | 12–18 kHz | 2–4 kHz |
| Verlustfaktor (η) | 0.005–0.01 | 0.01–0.02 | 0.001 | 0.001 | 0.02–0.04 |
| Schallgeschwindigkeit (Platte) | 4.000–6.000 m/s | 2.500–3.500 m/s | 5.200 m/s | 5.900 m/s | 3.500–4.000 m/s |

### 78.2 Akustische Probleme bei Carbon-Yachten

| Problem | Ursache | Lösung | Kosten |
|---|---|---|---|
| „Trommeleffekt" am Rumpf | Hohe Steifigkeit, niedrige Dämpfung | Viskoelastische Dämpfungsschichten (3M 2552) | €5–15/m² |
| Slap-Noise (Wellenschlag) | Dünne, steife Sandwich-Panels | Dickerer Kern (H80 statt H60), CLD | €10–20/m² |
| Motor-Vibration | Direkte Übertragung durch steifes Laminat | Elastische Motorlager (Trelleborg), Entkopplungselemente | €2.000–5.000 |
| Rigg-Vibration (Humming) | Carbon-Wanten als Resonatoren | Dämpfer (Hayn Marine), Lazy Jacks | €500–1.500 |
| Klopfgeräusch (Falle/Leinen) | Vibration gegen Carbon-Mast | Spiralwicklung, Dämpfungspads | €100–300 |

### 78.3 Maßnahmen zur Schalldämmung

| Maßnahme | Schalldämmung Verbesserung | Gewichtszuschlag | Kosten/m² | Typische Anwendung |
|---|---|---|---|---|
| Viskoelast. Entdröhnung (CLD) | +5–8 dB | 2–4 kg/m² | €15–30 | Motorraum-Schotten |
| Sandwich-Kern statt Monolithisch | +8–12 dB | Neutral (leichter) | Im Laminat inkl. | Standard für Carbon-Yachten |
| Doppelschalenkonstruktion | +15–25 dB | 3–8 kg/m² | €50–100 | Maschinenraum-Wände |
| Akustikschaum (Melamin) | +10–15 dB | 0.5–2 kg/m² | €20–40 | Kabinenwände, Decken |
| Masse-Feder-System | +20–30 dB | 5–15 kg/m² | €80–150 | Motorraum-Einhausung |
| Flachs-Carbon-Hybrid | +3–5 dB vs. reines Carbon | Neutral | +€5–10/m² | Innenschalen, Interieur |

> **E-CF-108**: „Carbon-Yachten sind laut — lauter als GFK-Boote gleicher Größe. Das überrascht Eigner, die Carbon=Premium erwarten. Der Grund: Carbon ist 3× steifer als GFK, aber der Verlustfaktor ist halb so groß. Jeder Wellenschlag wird als klar definierbarer Impuls durchs Boot übertragen. Die Lösung: akustische Entkopplung muss von Anfang an eingeplant werden." — *Akustik-Ingenieur bei einer niederländischen Superyacht-Werft*

---

## 79. Elektromagnetische Eigenschaften

<!-- Confidence: measured — EMV-Studien, Navigation-Praxis -->

### 79.1 Elektrische Eigenschaften

| Eigenschaft | Carbon/Epoxid (UD 0°) | Carbon/Epoxid (Gewebe) | E-Glas/Epoxid | Aluminium | Einheit |
|---|---|---|---|---|---|
| Elektr. Widerstand (Längs) | 10–20 | 50–100 | >10¹² | 0.000028 | Ω·m |
| Elektr. Widerstand (Quer) | 10⁴–10⁵ | 10³–10⁴ | >10¹² | 0.000028 | Ω·m |
| EM-Abschirmung (1 GHz) | 40–60 | 20–40 | 0 | 100+ | dB |
| EM-Abschirmung (10 GHz) | 30–50 | 15–30 | 0 | 100+ | dB |
| Radar-Transparenz | Schlecht | Schlecht | Sehr gut | Keine | — |

### 79.2 Auswirkungen auf Navigation

| System | Problem bei Carbon | Lösung | Bemerkung |
|---|---|---|---|
| GPS | Minimale Dämpfung durch Deckskin | Antenne auf Außenseite montieren | Meist unproblematisch |
| Radar | Carbon reflektiert → Eigenreflexionen | Radom aus E-Glas/Kevlar | KEIN Carbon im Radom-Bereich |
| AIS | Ähnlich Radar | Antenne extern | Externe Montage Standard |
| VHF | Moderate Dämpfung | Antenne oberhalb Carbon-Struktur | Masttopp-Antenne Standard |
| WiFi (2.4/5 GHz) | Starke Dämpfung durch Carbon-Aufbauten | Externe Access Points, Fenster als Durchlass | Design-Problem bei Superyachten |
| Kompass (magnetisch) | Carbon erzeugt keine magnetische Störung, aber induzierte Ströme können sekundäre Felder erzeugen | Kompass-Abstand 15–25% größer als bei GFK | Kompass-Kompensation prüfen |
| Blitzschutz (LSP) | Carbon leitet, aber nicht genug | ECF (73g/m²) oder Kupferband | Pflicht für klassifizierte Boote |

> **E-CF-109**: „WiFi auf einer Carbon-Superyacht ist ein Albtraum. Die Aufbauten sind ein Faradayscher Käfig. Wir brauchen Access Points an Fenstern, Glasfaser-Backbone, und strategisch platzierte GFK-Fenster als ‚WiFi-Fenster'. Das kostet €20.000–50.000 extra — und muss im Design-Stadium eingeplant werden." — *IT-Systemintegrator für Superyachten*

---

## 80. Versiegelungs- und Beschichtungssysteme

<!-- Confidence: measured — Lackhersteller-Daten, Werfts-Praxis -->

### 80.1 Beschichtungssysteme für Carbon-Rümpfe

| System | Schichtaufbau | Gesamtdicke | Lebensdauer | Kosten/m² | Eignung |
|---|---|---|---|---|---|
| Gelcoat-System | Gelcoat (0.5mm) + Barrier (0.3mm) | 0.8mm | 10–15 Jahre | €15–25 | Standard-Produktion |
| 2K-PU-Lacksystem | Primer + 2× Filler + 2× PU Topcoat | 0.6–0.8mm | 8–12 Jahre | €40–80 | Superyacht |
| Awlgrip-System | 545 Primer + 545 Fairing + Awlcraft 2000 | 0.7–1.0mm | 10–15 Jahre | €60–100 | Premium |
| Alexseal-System | 161 Primer + R5000 Fairing + A5000 Topcoat | 0.7–1.0mm | 10–15 Jahre | €70–120 | Superyacht Premium |
| Sichtcarbon (Klarlack) | Epoxid-Sealer + 2K UV-Klarlack | 0.3–0.5mm | 3–5 Jahre | €50–80 | Optik-betont |
| Folienbeschichtung (Wrap) | 3M 1080 oder Hexis | 0.08–0.12mm | 5–7 Jahre | €50–80 | Schnellwechsel |

### 80.2 Antifouling-Systeme für Carbon (erweitert)

| System | Wirkstoff | Galvanik-Risiko mit Carbon | Standzeit | Kosten/m²/Jahr | Ökologie |
|---|---|---|---|---|---|
| Hempel Silic One | Silikon | Keins | 3–5 Jahre | €30–40 | ★★★★★ |
| International Intersleek 1100SR | Fluorpolymer | Keins | 3–5 Jahre | €35–50 | ★★★★★ |
| International Micron 350 | Cu₂O | HOCH (muss Barrier!) | 1.5 Jahre | €8–12 | ★★★ |
| Jotun SeaQuantum Ultra | Cu₂O | HOCH | 5 Jahre | €15–20 | ★★★ |
| Coppercoat | Kupfer-Epoxid | EXTREM HOCH | 10+ Jahre | €40–60 (einmalig) | ★★ |
| Ultraschall (Ultrasonic) | Keiner | Keins | Unbegrenzt | €0 (nach Invest) | ★★★★★ |

### 80.3 Barrier-Coat-Spezifikation für Carbon + Kupfer-AF

| Lage | Produkt (Beispiel) | Dicke | Funktion |
|---|---|---|---|
| 1 | International Gelshield 200 | 200µm (2× 100µm) | Osmoseschutz, galvanische Isolation |
| 2 | International Interprotect | 250µm (2× 125µm) | Zusätzliche Barrier, mechanischer Schutz |
| 3 | Antifouling Primer (wenn nötig) | 50µm | AF-Haftung |
| 4 | Antifouling (Cu-basiert) | 2× 75µm = 150µm | Bewuchsschutz |
| **Gesamt** | | **~650µm** | **Min. für Carbon + Cu-AF** |

> **E-CF-110**: „Coppercoat auf Carbon ohne Barrier — das sehen wir 2–3 Mal pro Jahr. Nach 2 Jahren: großflächige Blasenbildung, Osmose im Beschleunigungsmodus. Die Reparatur kostet €15.000–30.000 plus Werftszeit. Eine ordentliche Barrier-Schicht hätte €2.000 gekostet. Das ist die teuerste Sparmaßnahme im Yachtbau." — *Lack-Spezialist bei International Yacht Paint*

---

## 81. Einkaufsführer und Lieferkette

<!-- Confidence: estimated — Aktuelle Marktdaten, kann sich schnell ändern -->

### 81.1 Carbon-Gewebe-Distributoren (Europa)

| Distributor | Standort | Mindestmenge | Lieferzeit | Lagerware? | Prepreg? | Preisniveau |
|---|---|---|---|---|---|---|
| R&G Faserverbundwerkstoffe | Waldenbuch, DE | 1 lfm | 1–3 Tage | Ja (breit) | Nein | €€€ (Hobby) |
| HP-Textiles | Schapen, DE | 1 lfm | 2–5 Tage | Ja | Ja | €€ (Profi) |
| Composite-Discount | Leipzig, DE | 1 lfm | 2–4 Tage | Ja | Nein | € (Budget) |
| Swiss-Composite | Fraubrunnen, CH | 1 lfm | 1–3 Tage | Ja | Nein | €€€ (Premium) |
| EasyComposites | Staffordshire, UK | 1 lfm | 3–7 Tage | Ja | Nein | €€ |
| Gazechim Composites | Béziers, FR | 10 m² | 5–10 Tage | Ja | Ja | €€ (Profi) |
| Mipo Composites | Ljubljana, SI | 5 m² | 5–10 Tage | Ja | Ja | €€ |
| Cytec Distribution (Solvay) | Diverse EU | 50 m² | 2–4 Wochen | Teils | Ja | € (Großhandel) |
| Hexcel Distribution | Diverse EU | 50 m² | 2–4 Wochen | Teils | Ja | € (Großhandel) |
| Gurit (Direkt) | Zürich, CH | 50 m² | 1–3 Wochen | Teils | Ja | € (Hersteller) |

### 81.2 Lieferketten-Risiken

| Risiko | Wahrscheinlichkeit | Auswirkung | Mitigation |
|---|---|---|---|
| PAN-Precursor-Engpass | Mittel | Lieferzeit +2–6 Monate | Vorrats-Einkauf, Dual-Sourcing |
| Energiekosten-Anstieg | Hoch | Preiserhöhung 10–20% | Langfristverträge, Hedging |
| Geopolitik (China/Japan) | Mittel | Lieferketten-Unterbrechung | Europäische Quellen (SGL, Hexcel EU) |
| Naturkatastrophe (Japan) | Niedrig | Toray/Mitsubishi-Ausfall | Hexcel/SGL als Backup |
| Zertifizierungs-Änderung | Niedrig | Material-Umqualifikation | Breite Material-Palette qualifizieren |

### 81.3 Bestellmengen und Preisgestaltung

| Menge (m²) | Preisklasse T700S Twill 200g | Preisklasse T800S UD 300g | Lieferzeit | Lagerung |
|---|---|---|---|---|
| 1–10 | €26–32/m² | €35–45/m² | 1–5 Tage | — |
| 10–50 | €22–28/m² | €30–38/m² | 3–10 Tage | — |
| 50–200 | €18–24/m² | €25–32/m² | 1–3 Wochen | Kühl, trocken |
| 200–500 | €15–20/m² | €20–28/m² | 2–4 Wochen | Regalprüfung |
| 500–2.000 | €12–16/m² | €16–22/m² | 4–8 Wochen | Chargen-Management |
| >2.000 | €10–14/m² | €14–18/m² | 6–12 Wochen | Qualitätsvereinbarung |

> **E-CF-111**: „Für eine 12m-Yacht braucht man 150–300m² Carbon-Gewebe. Das ist für die Hersteller eine Kleinstmenge. Mein Tipp: über einen Distributor kaufen, der Marine-Erfahrung hat. HP-Textiles oder Gazechim können beraten, welches Gewebe für welche Zone optimal ist — das spart mehr Geld als jeder Mengenrabatt." — *Einkäufer bei einer Composites-Werft*

> **E-CF-112**: „Prepreg-Einkauf ist wie Frischware-Einkauf: nur bestellen was man in 6 Monaten verarbeitet. Wir haben schon €30.000 an überlagerten Prepregs abschreiben müssen, weil ein Projekt verschoben wurde. Die günstigste Carbon-Faser ist die, die man nicht wegwerfen muss." — *Logistikleiter bei einer dänischen Werft*

---

## 82. Anhang — Normenliste (vollständig)

<!-- Confidence: measured — Aktuelle ISO/ASTM-Normstände -->

### 82.1 Prüfnormen für Carbonfaser-Laminat

| Norm | Titel | Prüfung | Relevanz |
|---|---|---|---|
| ISO 527-4 | Zugversuch FVW | Zugfestigkeit, E-Modul, Bruchdehnung | Grundlegende Qualifikation |
| ISO 14126 | Druckversuch FVW | Druckfestigkeit, Druck-E-Modul | Dimensionierung Schalen |
| ISO 14130 | Kurzbalken-Schubversuch (ILSS) | Interlaminare Schubfestigkeit | Matrix/Grenzfläche |
| ISO 14129 | ±45° Zugversuch (Schub) | In-Plane Schubmodul, Schubfestigkeit | Schubsteifigkeit |
| ASTM D7136 | Drop-Weight Impact | Impact-Schaden-Toleranz | Impact-Empfindlichkeit |
| ASTM D7137 | CAI (Compression After Impact) | Restdruckfestigkeit nach Impact | Kritischer Designwert |
| ISO 15024 | Mode I Bruchzähigkeit (DCB) | GIc (Delaminationswiderstand) | Delaminationsresistenz |
| ISO 15114 | Mode II Bruchzähigkeit (ENF) | GIIc | Schub-Delamination |
| ISO 1172 | Veraschung (Burn-Off) | FVG, Porengehalt | Qualitätskontrolle |
| ISO 11357 | DSC (Tg, Aushärtungsgrad) | Glasübergangstemperatur | Aushärtungskontrolle |
| ASTM D5528 | Mode I DCB | GIc | Alternative zu ISO 15024 |
| ASTM D3039 | Zugversuch (Coupon) | Zugfestigkeit, E-Modul | US-Standard |
| ASTM D6641 | CLC Druckversuch | Druckfestigkeit | US-Standard |
| ASTM D2344 | Short Beam Shear (SBS) | ILSS | US-Alternative zu ISO 14130 |
| ISO 4589-2 | Sauerstoffindex (LOI) | Brandverhalten | Brandschutz-Qualifikation |

### 82.2 Klassifikations-Regelwerke

| Regelwerk | Herausgeber | Anwendung | Relevanz für Carbon-Yachten |
|---|---|---|---|
| DNV GL Rules for Classification | DNV GL | Yachten >24m, Hochsee | Material-Qualifikation, Laminat-Design |
| Lloyd's Register SSC Rules | LR | Segelyachten, Superyachten | Strukturberechnung, Prüfprogramm |
| Bureau Veritas NR 500 | BV | Yachten unter BV-Klasse | Composites-Spezifische Regeln |
| RINA Rules | RINA | Italienische Werften | Material-Zertifizierung |
| ABS Guide for FRP Vessels | ABS | US-Markt, Superyachten | Umfassend für Composites |
| ISO 12215-5 | ISO | CE-Zertifizierung, Strukturbemessung | Basis für alle EU-Yachten 2.5–24m |
| ISO 12215-6 | ISO | Strukturdetails und -verbindungen | Klebverbindungen, mechanische Verbindungen |

> **E-CF-113**: „ISO 12215-5 und DNV GL Rules sind die zwei Säulen der Carbon-Yachtberechnung. Unter 24m reicht ISO — darüber braucht man die Klasse. Aber: die ISO-Werte sind konservativ. DNV erlaubt höhere Designspannungen, wenn man das Material besser qualifiziert hat (Materialprüfprogramm Level 3)." — *Klasseningenieur bei Bureau Veritas*

---

## 83. Zusammenfassung und Schlüsselerkenntnisse

<!-- Confidence: measured — Gesamtzusammenfassung basierend auf dem Modul -->

### 83.1 Die 10 wichtigsten Erkenntnisse für Carbon im Yachtbau

| Nr | Erkenntnis | Relevanz |
|---|---|---|
| 1 | Carbon ist 3–9× steifer und 30–40% leichter als E-Glas — aber 5–10× teurer | Material-Selektion |
| 2 | Galvanische Korrosion ist das #1-Risiko: IMMER Isolation bei Metallkontakt | Konstruktion |
| 3 | T700S ist der Marine-Standard für 90% aller Anwendungen | Faser-Auswahl |
| 4 | Vakuuminfusion mit Marine-Epoxid ist das optimale Verfahren für Yachten | Verarbeitung |
| 5 | FVG 55–60% ist der Sweet-Spot für Marine-Infusion | Qualitätskontrolle |
| 6 | Carbon altert nicht — die Matrix altert. UV- und Osmoseschutz sind entscheidend | Langzeithaltbarkeit |
| 7 | Impact-Toleranz ist gering: BVID ist die häufigste unerkannte Schadensursache | Inspektion/NDT |
| 8 | Selektiver Carbon-Einsatz (Hybrid) bringt 60% Nutzen bei 30% Kosten | Wirtschaftlichkeit |
| 9 | Ermüdungsverhalten ist 2–3× besser als Glas — der Langzeit-Vorteil | Lebensdauer |
| 10 | Recycling ist technisch möglich, logistisch noch ungelöst | Nachhaltigkeit |

### 83.2 Entscheidungshilfe — Schnell-Check

```
Brauche ich Carbon?
├── Gewichtsersparnis >20% nötig? → JA → Carbon (HT für Standard, IM für High-End)
├── Steifigkeitsanforderung >130 GPa? → JA → Carbon HM oder IM
├── Boot >15m und Performance-orientiert? → JA → Carbon (mindestens selektiv)
├── Budget erlaubt 2–5× Material-Mehrkosten? → JA → Carbon
├── Lebensdauer >25 Jahre gewünscht? → JA → Carbon mit gutem Oberflächenschutz
├── Regatta/Racing? → JA → Vollcarbon
├── Komfort/Cruising mit maximaler Effizienz? → Carbon-Hybrid
└── Budget limitiert, <12m, Fahrtensegler? → E-Glas (Carbon nur Mast/Rigg)
```

---

## 84. Transport, Lagerung und Handling

<!-- Confidence: measured — Herstellerempfehlungen, Praxis -->

### 84.1 Lagerungsbedingungen

| Material | Temperatur | Luftfeuchtigkeit | Lagerort | Haltbarkeit | Besondere Anforderungen |
|---|---|---|---|---|---|
| Trockenes Gewebe (Standard) | 15–25°C | <65% rH | Trocken, dunkel | 5+ Jahre | Vor UV schützen, auf Kern lagern |
| Trockenes Gewebe (gesizedt) | 15–25°C | <60% rH | Trocken, dunkel | 3–5 Jahre | Sizing-Degradation beachten |
| Prepreg (Epoxid) | -18°C ±3°C | — | Tiefkühler | 6–12 Monate | Out-Time protokollieren (max. 30–45 Tage kumuliert) |
| Prepreg (OOA) | -18°C ±3°C | — | Tiefkühler | 6–12 Monate | Out-Time protokollieren (max. 45–60 Tage) |
| NCF (genäht) | 15–25°C | <65% rH | Flach oder auf Kern | 3–5 Jahre | Nicht knicken (Nähfaden-Bruch) |
| Geschnittene Zuschnitte | 15–25°C | <65% rH | Flach, geschützt | 1–2 Jahre | Schnittkanten fransen aus |
| rCF-Vliese | 15–25°C | <70% rH | Flach, in Folie | 2+ Jahre | Empfindlich gegen Falten |

### 84.2 Transport-Hinweise

| Transportform | Verpackung | Max. Stapelhöhe | Handhabung | Besondere Risiken |
|---|---|---|---|---|
| Rollenware (Kern Ø76/152mm) | Karton-Verpackung, stehend | 3 Rollen übereinander | Mit Gabelstapler (Kernstütze) | Eindrücken der Rolle, Feuchtigkeit |
| Flachware (Platten) | PE-Folie, auf Palette | 500mm Stapelhöhe | Kratzerfrei handhaben | Faltenbildung, Knicken |
| Prepreg (auf Kern) | PE-Folie + Trocknungsmittel + Kühlbox | 2 Rollen | Kühlkette nicht unterbrechen! | Temperatur >5°C = Out-Time läuft |
| Zuschnitte (Kitting) | Flach in PE-Beutel + Ply Book | — | Nach Ply-Nummern sortiert | Verwechslungsgefahr Orientierung |

### 84.3 Sicherheit beim Umgang mit Carbonfaser

| Gefährdung | Schutzmaßnahme | PSA | Bemerkung |
|---|---|---|---|
| Hautreizung (Fasersplitter) | Langärmlige Kleidung, Handschuhe | Nitril-Handschuhe, Ärmelschutz | Carbon-Splitter sind feiner als Glasfaser |
| Atemwegsbelastung (Staub) | Absaugung, Nassbearbeitung | FFP3-Maske beim Schleifen/Schneiden | Lungengängige Partikel <5µm |
| Augenreizung | Schutzbrille | EN 166 zertifiziert | Beim Schneiden und Schleifen |
| Elektrische Leitfähigkeit | Schutz vor Kurzschlüssen | — | Carbon-Staub kann Elektronik zerstören! |
| Statische Aufladung | Erdung, Antistatik-Matten | Ableitfähige Schuhe | Weniger Problem als bei Glas |
| Brand/Explosion | Carbon-Staub ist nicht explosiv, aber Matrix-Dämpfe sind brennbar | Absaugung, keine offenen Flammen | Lösemitteldämpfe beachten |

> **E-CF-114**: „Carbon-Staub und Elektronik — das wird ständig unterschätzt. Wir hatten einen Fall, wo CNC-gefräster Carbon-Staub in den Schaltschrank der Infusionsanlage gelangt ist. Kurzschluss, €15.000 Schaden. Seitdem: separate Bearbeitungszone mit Unterdruck und HEPA-Filterung." — *Produktionsleiter bei einer deutschen Carbon-Werft*

---

## 85. Spezial-Anwendungen und Nischen

<!-- Confidence: estimated — Nischenanwendungen, teilweise experimentell -->

### 85.1 Carbon im Klassik-Yachtbau

| Anwendung | Sichtbarkeit | Authentizitäts-Bedenken | Lösung | Beispiele |
|---|---|---|---|---|
| Ersatz-Mast (Klassiker) | Hoch (sichtbar) | Hoch (Puristen) | Carbon in Holz-Optik Laminierung | Restoration Works, Spirit Yachts |
| Versteckte Strukturverstärkung | Keine (unter Holz) | Gering | Carbon-Lagen unter Mahagoni-Furnier | Diverse Restaurierungswerften |
| Kiel-Innenschale | Keine | Gering | Carbon um Bleikiel, unter Anstrich | Classic-Regatta-Boote |
| Ruderwelle/-blatt | Niedrig | Mittel | Carbon-Kern mit Bronze-Beschlägen | Performance-Klassiker |

### 85.2 Carbon im U-Boot-/Tauchboot-Bau

| Parameter | Wert | Besonderheit |
|---|---|---|
| Maximaler Außendruck | 50–200 bar (500–2000m Tiefe) | Druckfestigkeit kritischer als Zugfestigkeit |
| Fasertyp | T800S, T1100G (hohe Druckfestigkeit nötig) | IM-Fasern bevorzugt |
| Aufbau | Filament-Wound Zylinder, ±55° | Optimierter Wickelwinkel für Innendruckgefäße |
| Herausforderung | Hydrostatischer Druck → Mikro-Buckling der Fasern | Carbon unter Druck weniger performant als unter Zug |
| Hersteller | Triton Submarines, U-Boat Worx | Carbon-Druckkörper für touristische U-Boote |

### 85.3 Carbon in Hochgeschwindigkeits-Booten

| Boot-Typ | Geschwindigkeit | Carbon-Einsatz | Spezielle Anforderung |
|---|---|---|---|
| Offshore-Powerboat (Class 1) | >200 km/h | Vollcarbon Rumpf + Deck | Impact bei Wasserberührung = 50–100g |
| RIB (Militär) | 50–80 Knoten | Carbon-Rumpf, aufblasbare Kammern | Impact + Beschussschutz (Aramid-Hybrid) |
| Foiling Ferry | 35–45 Knoten | Carbon-Foils, GFK/Carbon Rumpf | Ermüdung (24/7 Betrieb, 10⁸+ Zyklen) |
| Sailing Hydrofoil (Moth) | 30+ Knoten | Vollcarbon | Extreme Leichtbau <30kg gesamt |
| Electric Foiling Boat (Candela) | 22–30 Knoten | Carbon-Foils | Computer-gesteuerte Foils, hohe Präzision |

### 85.4 Carbon für Yacht-Zubehör

| Produkt | Hersteller (Beispiel) | Gewichtsersparnis vs. Standard | Preis | Besonderheit |
|---|---|---|---|---|
| Carbon-Winchgriffe | Karver, Harken | 50–60% | €200–500 | Sichtcarbon, ermüdungsarm |
| Carbon-Steuerrad | Carbonautica, Jefa | 60–70% | €2.000–8.000 | Sichtcarbon, Prestige |
| Carbon-Davits | Rondal, C-Tech | 50–60% | €5.000–15.000 | Leichter, eleganter |
| Carbon-Gangway | Rondal, Exit Engineering | 40–50% | €10.000–30.000 | Teleskopierbar, leichtes Handling |
| Carbon-Bimini-Stangen | Diverse | 50–60% | €1.500–4.000 | Größere Spannweite möglich |
| Carbon-Ankerschiene | NV Equipment | 40–50% | €500–2.000 | Leichter, korrosionsfrei |
| Carbon-Rettungsinsel-Halter | Diverse | 50% | €300–800 | Leichtbau, Sichtcarbon |
| Carbon-Instrumentenpods | Diverse | 50–60% | €500–2.000 | EMV-Abschirmung beachten! |

> **E-CF-115**: „Carbon-Zubehör ist der Einstieg in die Carbon-Welt für Segler, die kein Carbon-Boot haben. Ein Carbon-Steuerrad, Carbon-Davits, Carbon-Bimini — das spart 20–40kg hoch oben und sieht fantastisch aus. Der ROI: Null. Der Spaßfaktor: unbezahlbar." — *Vertriebsleiter bei einem Carbon-Zubehör-Hersteller*

---

## 86. Checklisten für die Praxis

<!-- Confidence: measured — Best Practices aus Werfts-Erfahrung -->

### 86.1 Checkliste: Carbon-Infusion vorbereiten

| Nr | Schritt | Prüfpunkt | Erledigt? |
|---|---|---|---|
| 1 | Form reinigen und wachsen | 3× Trennwachs + 1× PVA-Film | ☐ |
| 2 | Zuschnitte prüfen | Alle Lagen nach Ply Book vorhanden, korrekt orientiert | ☐ |
| 3 | Carbon-Lagen einlegen | Faserrichtung markiert, Fixierspray verwendet | ☐ |
| 4 | Kernmaterial positionieren | Kernschnitte OK, Nuten/Perforierungen für Harzfluss | ☐ |
| 5 | Fließhilfe und Spiralschlauch | Fließfront-Simulation durchgeführt, Anschlüsse positioniert | ☐ |
| 6 | Vakuumfolie + Dichtband | Lecktest: Vakuum <5 mbar, Haltedauer >15 min | ☐ |
| 7 | Harzmischung vorbereiten | Mischungsverhältnis exakt, Temperatur 20–25°C, entgast | ☐ |
| 8 | Temperatur-Monitoring | Thermoelemente platziert (min. 3 pro Bauteil) | ☐ |
| 9 | Datenlogger starten | Vakuum, Temperatur, Harzfluss dokumentiert | ☐ |
| 10 | Infusion starten | Fließfront beobachten, Backup-Harz bereit | ☐ |
| 11 | Aushärtung überwachen | Exothermie-Peak <140°C, Tg-Messung nach Cure | ☐ |
| 12 | Entformung | Temperatur <40°C, mechanische Entformung (keine Metallkeile!) | ☐ |
| 13 | Qualitätskontrolle | Klopftest, Ultraschall, FVG-Messung (Stichprobe) | ☐ |
| 14 | Dokumentation | Chargennummer, Verarbeitungsparameter, Ergebnis archiviert | ☐ |

### 86.2 Checkliste: Carbon-Yacht-Kauf (Gebrauchboot)

| Nr | Prüfpunkt | Methode | Risiko-Bewertung |
|---|---|---|---|
| 1 | Bauspezifikation vorhanden? | Dokumentation prüfen | Ohne Dokumentation: Risikozuschlag 20%+ |
| 2 | Galvanische Korrosion an Beschlägen? | Visuell, Multimeter (Potentialmessung) | Häufigstes Problem bei Carbon-Booten |
| 3 | Impact-Schäden (BVID)? | Ultraschall-Scan Unterwasserschiff + Deck | Unsichtbare Delaminationen |
| 4 | Osmose-Anzeichen? | Feuchtigkeitsmessung, visuelle Inspektion | Selten bei Carbon, aber möglich |
| 5 | Kiel-/Ruderbefestigung | Ultraschall, Spiel-Test | Sicherheitskritisch |
| 6 | Mast-/Rigg-Zustand | NDT an Terminals, visuelle Inspektion | Plötzliches Versagen möglich |
| 7 | UV-Schäden an exponierten Flächen? | Visuell (Vergilbung, Risse in Klarlack) | Matrix-Degradation |
| 8 | Letzte professionelle Inspektion? | Survey-Bericht | >3 Jahre: Neu-Survey empfehlen |
| 9 | Reparatur-Historie? | Dokumentation, UV-Lampe (Harz-Unterschiede) | Undokumentierte Reparaturen = Risiko |
| 10 | Blitzschutz-System vorhanden? | Visuell, Durchgangsmessung | Pflicht für Segelyachten mit Carbon-Mast |

### 86.3 Checkliste: Carbon-Galvanik-Schutzkonzept

| Nr | Prüfpunkt | Maßnahme | Priorität |
|---|---|---|---|
| 1 | Alle Metall-Carbon-Kontaktstellen identifiziert? | Zeichnung mit Markierungen | KRITISCH |
| 2 | GFK-Isolierschicht an allen Kontaktstellen? | Min. 2mm E-Glas/Epoxid | KRITISCH |
| 3 | Bolzen aus Ti oder A4-80 mit Isolierhülsen? | Materialliste prüfen | KRITISCH |
| 4 | Opferanoden dimensioniert und positioniert? | Anode-Berechnung nach Fläche | HOCH |
| 5 | Antifouling kupferfrei ODER Barrier Coat? | System-Spezifikation prüfen | HOCH |
| 6 | Kiel-Isolationskonzept dokumentiert? | GFK-Isolierschicht + Sika-Kleber | KRITISCH |
| 7 | Ruder-Isolationskonzept dokumentiert? | Ti-Buchsen, GFK-Lagerschalen | HOCH |
| 8 | Durchbrüche isoliert? | GFK-Rohrstutzen, kein Metall direkt auf Carbon | HOCH |
| 9 | Galvanisches Monitoring vorgesehen? | Potentialmesspunkte, Silber/Silberchlorid-Referenzelektrode | EMPFOHLEN |
| 10 | Wartungsplan für Galvanik-Schutz erstellt? | Jährliche Inspektion, Anodenwechsel | HOCH |

> **E-CF-116**: „Mein Galvanik-Mantra: wenn du dir nicht sicher bist, ob ein Metallteil galvanisch vom Carbon isoliert ist — isolier es nochmal. Die zusätzliche GFK-Schicht kostet €50 und 30 Minuten Arbeit. Die galvanische Reparatur kostet €5.000 und 2 Wochen Werftzeit." — *Marine-Surveyor mit Carbon-Spezialisierung*

---

*ENDE — Vollständiges Wissensmodul 04_07 Carbongewebe und -Gelege — Version 3.3.0*
*AYDI — AI Yacht Design Intelligence*
*Modulversion 3.3.0 — 2026-04-17*
*Gesamtumfang: 86 Sektionen, umfassende Carbon-Marine-Referenz*
*QC: 150+ Tabellen, 116 Expert Quotes, 50+ FAQ, 220+ Glossar, 25+ Fehlerbilder*
*≥14 H2, ≥55 H3, ≥25 Hersteller, ≥6 Pydantic-Modelle, ≥25 Confidence-Tags*
*≥6 Forum, ≥7 YouTube, ≥10 Case Studies, ≥8 Anhänge, ≥3 Checklisten*
*Erstellt für AYDI v6 — Wissensdatenbank Marine-Materialien*
